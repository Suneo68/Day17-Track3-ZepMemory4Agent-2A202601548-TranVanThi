# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **869.6 ms**
- Average token reduction vs full source context: **14.8%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1304.3 | 655 | 0.0% |  |
| G09 | semantic | PASS | 236.1 | 155 | 66.2% |  |
| G10 | semantic | PASS | 249.2 | 100 | 78.2% |  |
| G14 | mixed | PASS | 1285.7 | 436 | 0.0% |  |
| G03 | long_term | PASS | 1068.8 | 954 | 0.0% |  |
| G04 | long_term | PASS | 1130.5 | 955 | 0.0% |  |
| G07 | episodic | PASS | 241.2 | 564 | 0.0% |  |
| G08 | episodic | PASS | 260.3 | 578 | 0.0% |  |
| G11 | mixed | PASS | 1311.8 | 444 | 21.4% |  |
| G13 | mixed | PASS | 507.3 | 413 | 26.9% |  |
| G15 | mixed | PASS | 1553.1 | 744 | 0.0% |  |
| G16 | mixed | PASS | 1299.9 | 492 | 12.9% |  |
| G17 | mixed | PASS | 1372.7 | 492 | 12.9% |  |
| G18 | mixed | PASS | 496.6 | 364 | 35.6% |  |
| G19 | mixed | PASS | 1341.5 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1080.3 | 949 | 0.0% |  |
| G12 | mixed | PASS | 1237.8 | 390 | 38.3% |  |
| G20 | mixed | PASS | 1415.3 | 614 | 2.9% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend examples and do not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:02:34     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Minh la Lan, phap ly hoi gat truoc khi bat memory tren san pham. Viet hop dong ngan: backend minh dang dung ngon ngu/framework nao, va quy tac luu/xoa bo nho ca nhan trong lab yeu cau opt-in va verify ra sao? Chi stack cua Lan.   - Created At: 2026-08-01 11:00:20     Sou`

### G09 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata=`

### G10 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata=`

### G14 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend examples and do not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:07:01     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: message    `

### G03 - long_term

`<USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They have a deadline for a benchmark report, LAB-REPORT-1600, due by Saturday at 16:00. The user has been debugging async HTTP requests and resolved an issue by reusing an aiohttp ClientSession and setting concurrency to 20, which was related to connection churn rather than a timeout threshold, identified as the ASYNC-FIX-20 incident. The user's projects include BLUEBIRD-42 and ORCHID-27. For BLUEBIRD-42, TypeScript with NestJS is required for the backend, and Python is not to be`

### G04 - long_term

`<USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They have a deadline for a benchmark report, LAB-REPORT-1600, due by Saturday at 16:00. The user has been debugging async HTTP requests and resolved an issue by reusing an aiohttp ClientSession and setting concurrency to 20, which was related to connection churn rather than a timeout threshold, identified as the ASYNC-FIX-20 incident. The user's projects include BLUEBIRD-42 and ORCHID-27. For BLUEBIRD-42, TypeScript with NestJS is required for the backend, and Python is not to be`

### G07 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngo`

### G08 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon `

### G11 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They have a deadline for a benchmark report, LAB-REPORT-1600, due by Saturday at 16:00. The user has been debugging async HTTP requests and resolved an issue by reusing an aiohttp ClientSession and setting concurrency to 20, which was related to connection churn rather than a timeout threshold, identified as the ASYNC-FIX-20 incident. The user's projects include BLUEBIRD-42 and ORCHID-27. For BLUEBIRD-42, TypeScript with NestJS is required for the backend, and Python `

### G13 - mixed

`<EPISODIC> EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Minh sap giai thich coroutine cho ban, dong thoi can nhac policy retry payment vao vi du. Minh hoc kieu nao thi de nho? Va request retry payment phai mang header nao? Dun`

### G15 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They have a deadline for a benchmark report, LAB-REPORT-1600, due by Saturday at 16:00. The user has been debugging async HTTP requests and resolved an issue by reusing an aiohttp ClientSession and setting concurrency to 20, which was related to connection churn rather than a timeout threshold, identified as the ASYNC-FIX-20 incident. The user's projects include BLUEBIRD-42 and ORCHID-27. For BLUEBIRD-42, TypeScript with NestJS is required for the backend, and Python `

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They have a deadline for a benchmark report, LAB-REPORT-1600, due by Saturday at 16:00. The user has been debugging async HTTP requests and resolved an issue by reusing an aiohttp ClientSession and setting concurrency to 20, which was related to connection churn rather than a timeout threshold, identified as the ASYNC-FIX-20 incident. The user's projects include BLUEBIRD-42 and ORCHID-27. For BLUEBIRD-42, TypeScript with NestJS is required for the backend, and Python `

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They have a deadline for a benchmark report, LAB-REPORT-1600, due by Saturday at 16:00. The user has been debugging async HTTP requests and resolved an issue by reusing an aiohttp ClientSession and setting concurrency to 20, which was related to connection churn rather than a timeout threshold, identified as the ASYNC-FIX-20 incident. The user's projects include BLUEBIRD-42 and ORCHID-27. For BLUEBIRD-42, TypeScript with NestJS is required for the backend, and Python `

### G18 - mixed

`<EPISODIC> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Pr`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They have a deadline for a benchmark report, LAB-REPORT-1600, due by Saturday at 16:00. The user has been debugging async HTTP requests and resolved an issue by reusing an aiohttp ClientSession and setting concurrency to 20, which was related to connection churn rather than a timeout threshold, identified as the ASYNC-FIX-20 incident. The user's projects include BLUEBIRD-42 and ORCHID-27. For BLUEBIRD-42, TypeScript with NestJS is required for the backend, and Python `

### G05 - long_term

`<USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They have a deadline for a benchmark report, LAB-REPORT-1600, due by Saturday at 16:00. The user has been debugging async HTTP requests and resolved an issue by reusing an aiohttp ClientSession and setting concurrency to 20, which was related to connection churn rather than a timeout threshold, identified as the ASYNC-FIX-20 incident. The user's projects include BLUEBIRD-42 and ORCHID-27. For BLUEBIRD-42, TypeScript with NestJS is required for the backend, and Python is not to be`

### G12 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They have a deadline for a benchmark report, LAB-REPORT-1600, due by Saturday at 16:00. The user has been debugging async HTTP requests and resolved an issue by reusing an aiohttp ClientSession and setting concurrency to 20, which was related to connection churn rather than a timeout threshold, identified as the ASYNC-FIX-20 incident. The user's projects include BLUEBIRD-42 and ORCHID-27. For BLUEBIRD-42, TypeScript with NestJS is required for the backend, and Python `

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
