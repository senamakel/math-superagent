# Tasks

- [x] Oracle definition check: run `python code/brute.py` at the statement's reachable worked examples; D(2)=3 and D(10)=44499 both matched (tool-builder re-ran this run: exit 0, ~seconds).
- [x] Reproduce D(12)=514419 and D(13)=1749267 via the bitmask oracle (matches frozenset values).
- [x] Extend BFS as far as feasible under cap=5,000,000: reached D(14)=5949063, stopped cleanly (frontier 5.95M > cap).
- [x] Verify D(14) by a second independent implementation (amoeba_verify.py) — both give 5949063.
- [x] Dump per-config structural features (level histogram a_k, bbox dims, max level M) for N=2..12 into /workspace/data/ with an INDEX.md.
- [x] Report extended D(N) list, timing, and data files.
- [x] Test conjecture C1 (reachable <=> origin-connected) in 2D and 3D.
      DISPROVEN both: C1 counts = directed-animal counts, not D(N). Program
      code/test_c1.py, independent oracle code/out/verify_c1_subsets.py, writeup
      code/out/c1_test_results.md.
- [x] Pure naive frozenset BFS oracle (code/brute.py) as definition check:
      reproduces the worked examples D(2)=3 and D(10)=44499, reaches
      D(0..13)=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267
      (all match), and stops before the D(14) step which OOMs the 2 GiB cgroup
      cap (~5.9M-config frontier). Confirms D(20)=9204559704 unreachable by
      exact BFS (level-20 state space ~9.2e9, ~5-9 TB). Output
      code/out/brute_fs_oracle_run.txt.
- [x] Re-confirm exact-BFS D(N) for N=0..14 with D(2)=3, D(10)=44499 (brute.py).
- [x] Verify top-cap claims over the WHOLE computable range (check_recurrence.py
      N<=7, definitive_check.py N<=12, new check_a1a2_bitmask.py N=14,
      check_a12_lean_large.py N=13). RESULT: A1 holds (A1bad=0), A2_tri holds
      (top-3 always a full child-triangle of ONE parent), but A2_empty fails
      from N=4 (701262 bad at N=14), A3 fails from N=5, and B
      (D(N+1)=sum f(C)) fails from N=3 (forward map not injective). Details in
      MEMORY.md.
- [ ] (future) A structural/combinatorial formula for D(N) to reach N=10000 — brute-force BFS caps out near N=14.
