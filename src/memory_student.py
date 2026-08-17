from __future__ import annotations

from types import SimpleNamespace
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # Context Block needs a current thread slice to decide relevance.
        prime_eval_thread(self.client, user_id, thread_id, query)
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        return getattr(user_context, "context", "") or ""

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # scope="episodes" returns raw episode content, keeping literal
        # markers (e.g. ASYNC-FIX-20) that an extracted-fact scope would drop.
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        # episode_char_cap keeps more distinct episodes readable instead of
        # letting one verbose session message crowd out the rest.
        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # scope="episodes" returns raw document text that keeps literal
        # markers (e.g. PAYMENT-RULE-3); "auto" extracts facts and drops them.
        q = cap_query(query)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=8,
            )
        except Exception:
            # Fallback for accounts/SDKs where the episodes scope differs.
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=8,
            )
        # add_semantic_documents ingests each KB doc twice: a verbose JSON
        # copy and a concise text summary that ends with the same literal
        # marker. Under a tight combined budget (e.g. the "mixed" case) the
        # JSON duplicates can crowd out a lower-ranked document entirely, so
        # keep only the shorter text copies.
        episodes = getattr(results, "episodes", None) or []
        text_episodes = [
            e for e in episodes if not (getattr(e, "content", "") or "").lstrip().startswith("{")
        ]
        filtered = SimpleNamespace(
            context=getattr(results, "context", None),
            edges=getattr(results, "edges", None),
            episodes=text_episodes or episodes,
            nodes=getattr(results, "nodes", None),
            observations=getattr(results, "observations", None),
            thread_summaries=getattr(results, "thread_summaries", None),
        )
        return render_graph_search(filtered)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        return self.budget.assemble(layers)
