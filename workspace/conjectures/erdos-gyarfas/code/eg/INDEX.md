# Index — code/eg

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `crosscheck_fast_vs_oracle.py` | _(undescribed)_ |
| `expansion_census.py` | Enumerates the K4-triangle-expansion family (== Apollonian networks / planar 3-trees, A027610) up to isomorphism via nauty-labelg canonical forms, and per size reports #classes, #avoiding-C4, #avoiding-C4&C8. Produced sequences: classes 1,1,1,3,7,24,93,434,2110 (matches A027610 a(3..8)); avoidsC4 1,1,2,5,15,50 (matches A279553/A107590 prefix); avoidsC4C8 all 0 to n=20. Exponential census, oracle bound n<=24. |
| `expansion_census_fast.py` | _(undescribed)_ |
| `expansion_resume_24.py` | _(undescribed)_ |
| `expansion_resume_26.py` | Resumable n=24->26 census driver for the K4-triangle-expansion family (cubic Apollonian duals == planar 3-trees). Three checkpointed phases: A parallel expansion pool (58713 classes x 144 = 8,454,672 pool lines), B chunked nauty-labelg canonicalisation+dedup -> level_26_classes.txt, C exact power-of-two cycle profile. Output in code/out/expansion_census_26/. VERIFIED: total classes 321,776 = A027610(11) exact (12th term), profile avoidsC4=3408, avoidsC4C8=0, avoidsC4C16=0, avoidsC4C8C16=0, c4free_hasC8_notC16=0; independent recount script (sibling one-off) reproduces all counts byte-for-byte; all members cubic. Wall 837.9s on 28 cores. |
| `find_c4c8_free_24.py` | _(undescribed)_ |
| `k4_expansion_base.py` | Single n=base K4-expansion step: expand vertex 0 of K4 into a triangle xyz attached bijectively (identity) to the three neighbours; prints the resulting graph's full cycle-length set via the oracle. Verified: n=6 (the text says 8; read strictly the construction gives 6 — flagged in output), triangular prism, cubic, cycle set {3,4,5,6} — 4 present, claim MATCH. Only the base step, no family generation. |
| `markstrom_membership.py` | _(undescribed)_ |
| `markstrom_membership2.py` | _(undescribed)_ |
| `markstrom_membership_control.py` | _(undescribed)_ |
| `markstrom_membership_debug.py` | _(undescribed)_ |
| `markstrom_membership_debug2.py` | _(undescribed)_ |
| `markstrom_second_route.py` | Second-route cross-check of the Markström graph reconstruction: loads markstrom.graph6 via nx.from_graph6_bytes AND markstrom.edgelist as an edge list (two independent routes), and for each route checks min degree 3, cycle-length set {3,5,6,7}∪{9..24} (4,8 absent, 16 present), 36 edges, planarity, node-connectivity 3 — with lib.cycle_oracle and brute.py's nx.simple_cycles implementation side by side. Verified: ALL MATCH on both routes (also confirmed graph6 == edgelist graph). |
| `recount_26.py` | _(undescribed)_ |
| `verify_a027610.py` | Attempts to verify the A027610 closed form against census counts. NOTE: the in-line formula transcription has integer-division bugs and MISMATCHes — do not rely on the harness; the identity is confirmed instead by the OEIS-listed A027610 terms (a(9)=11002, a(10)=58713) matching the census. |
