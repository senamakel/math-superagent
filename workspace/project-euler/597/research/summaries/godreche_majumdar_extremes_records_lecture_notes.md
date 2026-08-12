# Godrèche & Majumdar, "Extremes and Records" lecture notes — summary

- Source: Claude Godrèche & Satya N. Majumdar, "Extremes and Records" lecture notes, ICTS (International Centre for Theoretical Sciences), Bengaluru. URL: https://www.icts.res.in/sites/default/files/NOTES.pdf (full text: research/sources/godreche_majumdar_extremes_records_lecture_notes.full.md)
- Content: lecture notes on extreme value statistics, near-extreme events, and record statistics. iid-record section: a record occurs at position n if X_n exceeds all previous; record indicators I_n are independent with P(I_n = 1) = 1/n (Rényi); E[#records] = H_N ≈ ln N + γ; joint record distribution; statistics of the number of records (connected to the number of cycles of a uniform random permutation: P(#records = m) = S1(N,m)/N!); records of random walks and continuous-time random walks (correlated case: ages, growth exponents).
- Bearing on PE597: the iid record facts are exactly the pure no-finish bump-race leader/cluster facts: in the no-finish race the cluster leaders are the (right-to-left) record minima of the iid speeds and the cluster-count distribution is S1(N,k)/N! (verified by the run in code/verify_cm_face_dist.py). The random-walk record sections are background contrasts (speeds are iid, not a correlated walk, so the iid section governs).
- Restriction: record theory only; no bump dynamics, no finish line, no parity.

```claim
id: renyi-record-independence
statement: For iid continuous X_1,…,X_N the record indicators are independent with P(I_k=1)=1/k; the number of records has distribution S1(N,m)/N! (same as number of cycles of a uniform random permutation).
hypotheses: iid, continuous law.
holds-here: holds; the no-finish bump race's cluster leaders are record minima of iid speeds.
status: verified-against-source (Godrèche–Majumdar notes; Wikipedia Record value; Goldie 2022; run code/verify_cm_face_dist.py)
bearing: exact no-finish cluster-count distribution.
anchor: research/sources/godreche_majumdar_extremes_records_lecture_notes.full.md
```