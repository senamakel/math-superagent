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
- [ ] Solve p(13,1800) exactly. Hypothesis of w-order-only reduction is refuted;
      need the true continuous dynamics (bump/finish chronology over Exp speeds).
