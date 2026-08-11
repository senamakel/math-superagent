# Tasks

- [x] Run verify_hypothesis.py with N=200000; report MC + consistency verdict.
- [x] Diagnose why MC returned 1.000000 (parity comparator bug in brute.py).
- [x] Fix parity comparator; re-verify against the n=3,L=160 table.
- [x] Re-run at N=200000; report corrected MC and the (now meaningful) consistency verdict.
- [x] Verify brute oracle: reproduce all 5 n=3,L=160 rows + both examples (MC).
- [x] Investigate multi-bump edge-loss bug (examine_multibump): CONFIRMED real
      (brute kept only last bumper per boat, losing ~40% of edges), but never
      flipped order/parity (2M trials). FIXED brute.py and exact_race.py to
      record every bump edge and compute above by full reachability; now
      byte-identical to simulate_order_nobug.
- [x] Large MC p(13,1800): 100k=0.500470, 200k=0.499400, 300k=0.499027,
      1.2M=0.500880, combined 1.5M=0.500316. Ballpark target ~0.500.
- [x] High-precision parallel MC (high_precision_mc.py): p(13,1800) at 10M
      =0.500380 SE=0.000158 and 60M=0.500203 SE=0.000065; convergence series
      n=5..8 L=1800: 0.531964,0.486980,0.491648,0.505779 (all SE~0.0007, all
      within ~2-3 SE of 0.5). Conclusion: p(13,1800) indistinguishable from 0.5.
- [ ] Solve p(13,1800) exactly. Hypothesis of w-order-only reduction is refuted;
      need the true continuous dynamics (bump/finish chronology over Exp speeds).
- [x] research_recursion_test.py: the L1.1/CONTEXT library recursion
      (root=argmin W, p=sum distance-ratio weight·p(left)·p(right)·(-1)^cross,
      parity parity(left)·parity(right)·(−1)^cross) is REFUTED. Value-level
      gives p(3,160)=2/3 (truth 56/135) and p(4,400)=5/6 (truth 0.5108);
      per-vector smallest counterexample n=2,L=160,speeds=[0.89157,0.33049]
      (oracle odd, recursion even); crux claims C1 decoupling (fails
      20177/300000) and C2 cross=|L||R| (fails 152466/300000) both false.
      The finish events (inverse-exponential, non-clocks) break the treap
      sum-of-products form; an exact route must handle bump/finish chronology
      over Exp speeds directly.
- [x] test_treap.py: Cartesian-tree/min-heap-treap hypothesis REFUTED. n=2..6,
      L in (160,400,1800), 20k trials each -> 30 mismatches by trial ~60.
      Trivial n=2 counterexample (v0<v1, no bump, even; treap predicts odd).
      Tree-model MC p(3,160)=0.333 (given 0.4148), p(4,400)=0.833 (given 0.5108),
      p(13,1800)=0.536. Structure of the treap does not match the bump-chronology.
- [x] EXACT rational integration oracle for small n (cell_exact.py +
      toolkits/arr_enum.py + toolkits/arr_polytope.py). p(3,160)=56/135 and
      p(4,400)=521/1020=0.5107843137 EXACTLY; full small-n table (n=2,3,4;
      L=160,400,1800) in MEMORY.md + code/out/exact_small_n_results.json.
      Verified by a second independent solver (arrangement_pn.py) and MC.
- [x] Parity-cell counts: n=3 -> 32 cells (17 even), n=4 -> 1202 (595 even),
      L-independent. n=5 arrangement = 85 planes / ~13,750 cells: too heavy
      for the naive vertex solver -> p(5,1800)=0.5327±0.0003 by MC (per steering).
- [ ] Exact p(13,1800). The n<=4 arrangement is exact but n=13 requires a
      completely different route: the research library's treap/Plackett-Luce
      recursion is the candidate (see CONTEXT.md), though cross-range coupling
      tests (cross_*, crux_*) remain open. Not yet solved exactly.
- [x] Validation-oracle extras: exact p(3,L) for 16 extra integer L
      (120,200,280,360,440,520,560,720,900,1100,1400,2000,2400,3000,4000,5000)
      with ncells, saved to code/out/exact_p3_extra.json by code/exact_p3_extra.py.
      All 12 anchors re-derived exactly; all 16 extras double-verified by the
      independent enumerator p_cell_exact + MC. (n=3 only, as requested.)
- [x] structure_taxonomy.py: reproduce n=3,L=160 five-row table + p(4,400) MC;
      collect bump-graph taxonomy (out/in degree, forest/cycle, chain length,
      distinct structures) over 360k races -> bump graph is always a forest;
      findings in structure_report.md.
