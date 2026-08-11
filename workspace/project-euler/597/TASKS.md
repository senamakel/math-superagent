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
- [x] test_treap.py: Cartesian-tree/min-heap-treap hypothesis REFUTED. n=2..6,
      L in (160,400,1800), 20k trials each -> 30 mismatches by trial ~60.
      Trivial n=2 counterexample (v0<v1, no bump, even; treap predicts odd).
      Tree-model MC p(3,160)=0.333 (given 0.4148), p(4,400)=0.833 (given 0.5108),
      p(13,1800)=0.536. Structure of the treap does not match the bump-chronology.
