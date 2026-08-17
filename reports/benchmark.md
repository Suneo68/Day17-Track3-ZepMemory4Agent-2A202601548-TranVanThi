# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **2**
- Passed: **2/2**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **379.3 ms**
- Average token reduction vs full source context: **89.0%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E06 | semantic | PASS | 509.0 | 56 | 87.8% |  |
| E11 | semantic | PASS | 249.6 | 55 | 90.3% |  |

## Evidence excerpts

### E06 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata=`

### E11 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata=`
