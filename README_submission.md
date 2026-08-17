# README_submission — Lab 17 Multi-Memory Agent

## 3 câu bắt buộc (mục 5.2)

**Layer quan trọng nhất:** Long-term (Zep Context Block) — phủ 4/11 case
(E02, E03, E08, E09), là layer duy nhất phải tự xử lý conflict/recency
(E08: `BLUEBIRD-42` dùng TypeScript dù `ORCHID-27` vẫn ưu tiên Python) và
user isolation (E09: query của Lan không lẫn `ORCHID-27` của Minh). Sai
layer này ảnh hưởng nhiều case nhất, và cũng là layer tốn token nhất.

**Trade-off Context Block/Zep vs Redis+Qdrant:** Zep tự làm extraction,
dedup, conflict resolution và trả context tổng hợp sẵn, nhưng là managed
service, độ trễ ~1-1.3s/case, không kiểm soát ranking nội bộ. Redis+Qdrant
(`src/local_baseline.py`) kiểm soát schema/TTL/tốc độ (không round-trip
mạng) nhưng phải tự viết extraction/fact-merge/conflict-resolution — baseline
hiện chỉ làm KV + vector search thô, không tự sinh summary/fact.

**Guardrail chống memory poisoning:** Theo `control_plane/AGENTS.md` +
`MEMORY_SCHEMA.md`: (1) mọi durable write giữ `source`/`timestamp`/
`confidence`/`scope` để truy vết; (2) conflict theo "recency + scope", fact
cũ không xoá mà đánh `superseded`; (3) `heartbeat.py` không được tự thêm
instruction/quyền mới vào durable memory, chỉ de-duplicate/đánh dấu
stale/tạo recap; (4) user-scoped namespace (test ở E09) chặn user này
"đầu độc" memory user khác.

## 4 câu phân tích benchmark

1. **Layer hit rate thấp nhất:** thực tế cả 4 layer đạt 100% (11/11), không
   FAIL. Rủi ro cao nhất nếu ground truth khó hơn là long_term — retrieved
   tokens cao nhất (900-960/case), sát giới hạn budget nhất.
2. **Case tốn token nhất:** E03 ("Minh còn open loop hay deadline nào chưa
   hoàn thành?") — 958 token (Context Block gồm summary + facts + entities).
3. **E07 (mixed):** cần `long_term` + `semantic`, evidence bắt buộc `Python`
   (long-term) và `Idempotency-Key` (semantic KB).
4. **Token reduction không phản ánh hit rate:** no-memory giảm 81.8% token
   nhưng hit rate chỉ 18.2% (2/11) vì không lấy gì cả, không phải nén tốt.
   Memory-enabled giảm ít hơn (14.2%) nhưng hit rate 100% — reduction chỉ có
   ý nghĩa khi đọc cùng hit rate.

## E08 (recency) & E10 (compaction)

E08: fact mới (`BLUEBIRD-42` → TypeScript/NestJS) không xoá fact cũ
(`ORCHID-27` → Python) vì khác scope dự án — Context Block trả cả hai, đúng
`Conflict rule` trong `control_plane/MEMORY.md`. E10: dù giảm
`max_recent_messages` 6→4, `sliding` vẫn giữ `REVIEW-DEADLINE-1600` qua
`durable_notes` (pattern-match) thay vì để evict cùng raw turns — buffer
thuần không tách được constraint khỏi transcript.
