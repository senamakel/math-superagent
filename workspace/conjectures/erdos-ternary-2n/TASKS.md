# Tasks

## Done (this attempt and prior)

- [x] Oracle `digit_free` written, verified on the three witnesses 1, 4, 256 and on
  32 (`1012_3`) and 64 (`2101_3`) which contain a 2. (`code/out/prove_count_doubles.py`, section 1 PASS.)
- [x] Sieve count `|A_k|` computed; `|A_k| = 2^(k-1)` exact — bijection proof
  (SIEVE-EXACT) + fresh exact verification k=1..12 direct and k=1..40 order checks.
- [x] LTE mechanism verified: `2^(2·3^(k-2)) ≡ 1 + 3^(k-1) (mod 3^k)` with
  quotient c = 1 exactly, k=2..40. (Section 5 PASS.)
- [x] 2-to-1 lifting verified: each A_k class lifts to exactly 2 of 3 survivors.
- [x] **Main negative result (proved):** no power-of-3 modular obstruction can
  prove the conjecture — the count doubles forever, so no finite 3-adic precision
  suffices. Density `|A_k|/(2·3^(k-1)) = (1/2)(2/3)^(k-1) → 0` while count grows.
- [x] Frontier stated: any counterexample is `2^x` with ≥26 ones and zero 2s
  (DH-1); improving the 26 and coupling top/bottom digits is the open work
  (`research/FRONTIER.md`).
- [x] Approaches log written (`research/APPROACHES.md`), including why the pure
  sieve and the naive-count estimate cannot close.
- [x] Witnesses n=0,2,8 confirmed digit-free at every level k=1..40.

## Outstanding (open work, not this run's deliverable)

- [ ] Prove the conjecture (open since 1979; believed true, not proved here).
- [ ] Improve DH-1's ones-threshold 26 for the no-2 restricted shape.
- [ ] Couple top-digit (real) and bottom-digit (3-adic) controls (LAG-4: open).
