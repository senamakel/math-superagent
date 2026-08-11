# Tasks

- [x] Reproduce D(12)=514419 and D(13)=1749267 via the bitmask oracle (matches frozenset values).
- [x] Extend BFS as far as feasible under cap=5,000,000: reached D(14)=5949063, stopped cleanly (frontier 5.95M > cap).
- [x] Verify D(14) by a second independent implementation (amoeba_verify.py) — both give 5949063.
- [x] Dump per-config structural features (level histogram a_k, bbox dims, max level M) for N=2..12 into /workspace/data/ with an INDEX.md.
- [x] Report extended D(N) list, timing, and data files.
- [x] Test conjecture C1 (reachable <=> origin-connected) in 2D and 3D.
      DISPROVEN both: C1 counts = directed-animal counts, not D(N). Program
      code/test_c1.py, independent oracle code/out/verify_c1_subsets.py, writeup
      code/out/c1_test_results.md.
- [ ] (future) A structural/combinatorial formula for D(N) to reach N=10000 — brute-force BFS caps out near N=14.
