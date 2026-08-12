# Record value — Wikipedia; Godrèche–Majumdar extremes/records lecture notes — summary

- Source 1: Wikipedia "Record value" (record statistic). URL: https://en.wikipedia.org/wiki/Record_value (full text: research/sources/record_value_wikipedia.full.md)
- Source 2: Claude Godrèche & Satya N. Majumdar, "Extremes and Records" lecture notes, ICTS (International Centre for Theoretical Sciences), Bengaluru. URL: https://www.icts.res.in/sites/default/files/NOTES.pdf (full text: research/sources/godreche_majumdar_extremes_records_lecture_notes.full.md)
- Content: record statistics of iid sequences. For continuous iid X_1,…,X_N, the record indicators I_k are independent with P(I_k = 1) = 1/k (Rényi / Dwass–Rényi theorem); expected number of records = H_N = ln N + γ; the record-count distribution equals the number-of-cycles distribution of a uniform random permutation (P(#records = m) = S1(N,m)/N!), and the inter-record "ages" have universal structure. Godrèche–Majumdar's notes cover iid records, records of random walks (correlated), and the connection to random permutations/cycles ("number of records = number of cycles").
- Bearing on PE597: record minima of speeds are exactly the GCM vertex positions / convoy leaders in the pure no-finish race (right-to-left records); the independence/Bernoulli(1/k) structure is the engine behind the no-finish cluster-count identity. Statement tier for `cm-composition-distribution`; the random-walk-record sections are background for the correlated case (not needed for PE597's iid speeds).
- Restriction: iid/record theory only; no bump dynamics, no finish line.

```claim
id: renyi-record-independence
statement: For iid continuous X_1,…,X_N, the indicators I_k = 1{X_k is a record} are independent with P(I_k=1)=1/k; the number of records has the same distribution as the number of cycles of a uniform random permutation, P(#records = m) = S1(N,m)/N!.
hypotheses: iid, continuous law.
holds-here: holds; the no-finish bump race's cluster leaders are the record minima of the iid speeds, so this governs the no-finish cluster count.
status: verified-against-source (Wikipedia Record value; Godrèche–Majumdar notes; cross-checked by run's code/verify_cm_face_dist.py)
bearing: exact no-finish cluster-count distribution; not the finite-finish parity.
anchor: research/sources/record_value_wikipedia.full.md, research/sources/godreche_majumdar_extremes_records_lecture_notes.full.md
```