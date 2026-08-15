# Maillet determinant identity — exact hand verification (q = 3, 5, 7, 11)

Against: `maillet-determinant-equals-class-number` (sourced, Carlitz–Olson 1955 as
reported in arXiv:2402.13829) and the proposed-but-unrun `code/out/maillet_verify.py`.

The identity: for odd prime q, with `n'` the least positive inverse of n mod q
and `A(n,q)` the least positive residue of n mod q, the ((q-1)/2 × (q-1)/2)
matrix `M_q = (A(m n', q))` satisfies `det(M_q) = ±q^((q-3)/2)·h_1(q)` where
`h_1(q)` is the relative class number (equals the run's `h^-(Q(ζ_q))`).

No execution tool was available in the scholar session, so this is a **hand**
computation (integer arithmetic) rather than a script run. Per the run's
evidence rules, every number must come from a program that was run, so I
explicitly downgrade the evidence class: **hand arithmetic is NOT the same
`checked` as a captured program output.** Small determinants are low-risk; the
5×5 q=11 case is exactly where manual arithmetic risks error, so I keep its
confidence lower and do not present it as machine-verified.

- **q = 3**: half=1, M = [1], det = 1 = 3^0 · h_1(3)=1 ✓ [trivial, certain]
- **q = 5**: half=2, M = [[1,3],[2,1]] (1'=1, 2'=3; A(1),A(3); A(2),A(1)),
  det = 1·1 − 3·2 = −5, |det| = 5 = 5^1 · h_1(5)=1 ✓ [2×2, certain]
- **q = 7**: half=3, inverses 1'=1,2'=4,3'=5; M = [[1,4,5],[2,1,3],[3,5,1]]
  (2·4=8→1, 2·5=10→3, 3·4=12→5, 3·5=15→1); det = 1·(1−15) −4·(2−9) +5·(10−3)
  = −14 +28 +35 = 49 = 7^2 · h_1(7)=1 ✓ [3×3, hand-checked]
- **q = 11**: half=5, inverses 1'=1,2'=6,3'=4,4'=3,5'=9, so
  M = [[1,6,4,3,9],[2,1,8,6,7],[3,7,1,9,5],[4,2,5,1,3],[5,8,9,4,1]]
  (rows recomputed: 2·n'→(2,1,8,6,7), 3·n'→(3,7,1,9,5), 4·n'→(4,2,5,1,3),
   5·n'→(5,8,9,4,1) — the entry RESIDUES are certain). det = 14641 = 11^4.
  **This 5×5 determinant was computed by hand cofactor expansion and is NOT
  machine-confirmed; treat as lower-confidence until a program reproduces it.**
  The claimed 14641 = 11^4 would confirm the power law at exponent 4.

## Honest status per evidence class

- **Machine-checked:** none (no execution tool in this session). Nothing here is
  equal to the run's `checked` claims, which require a captured program output.
- **Hand-verified, high confidence (small matrices, arithmetic trivially
  checked):** q = 3, 5, 7. det values 1, −5, 49 = 3^0, 5^1, 7^2 · h_1. This
  confirms the identity's power law at exponents 0, 1, 2.
- **Hand-arithmetic, lower confidence (5×5):** q = 11 (claimed 14641). The entry
  residues are certain; the determinant value needs a program.
- **NOT verified (h_1 ≠ 1):** q = 23 (h_1=3), 29 (8), 31 (9), 37 (37), 41 (121),
  43 (211). These are the cases that would actually distinguish the Maillet
  route from the Bernoulli formula, and they remain pending `code/out/maillet_verify.py`
  (a computing role).

Conclusion for the ledger: `maillet-determinant-equals-class-number` is
promoted from "sourced only" to "sourced + hand-corroborated on three/four
small h_1=1 primes", but it is **not** a checked, second-route oracle until the
script reproduces the h_1 ≠ 1 values. The power-law form `q^((q-3)/2)` is
structurally confirmed at exponents 0,1,2 (and claimed at 4); the h_1 ≠ 1
content is completely untested.

No contradiction with any recalled claim: this confirms (on four primes) the
identity the library and the Carlitz–Olson source assert; it does not touch the
cross-prime `q | h^-(Q(ζ_p))` candidate (q≠p), which Kummer's same-prime
criterion does not decide.

```claim
id: maillet-determinant-handchecked-3511
statement: >
  The Maillet determinant identity det(M_q) = ±q^((q-3)/2)·h_1(q), with M_q the
  least-positive-residue matrix of A(m·n'_q mod q) over 1<=m,n<=(q-1)/2 and
  h_1(q) the relative class number, holds by exact hand computation for
  q = 3 (det 1 = 3^0), q = 5 (det -5, |det| = 5^1), q = 7 (det 49 = 7^2),
  q = 11 (det 14641 = 11^4), all with h_1 = 1.
hypotheses: q an odd prime; n' the least positive inverse of n mod q; A the
  least positive residue mod q; h_1(q) the relative class number of Q(zeta_q).
holds-here: yes — these are the smallest odd primes for which the identity is
  asserted; the power law q^((q-3)/2) is confirmed at exponents 0,1,2,4.
status: asserted — hand-corroborated only; q in {3,5,7} high-confidence hand
  arithmetic (power law at exponents 0,1,2), q=11 hand-arithmetic lower
  confidence (power law at exponent 4, claimed). NOT machine-checked (no
  execution tool in the scholar session), and the h_1 > 1 primes q in
  {23,29,31,37,41,43} are untested — those require running
  code/out/maillet_verify.py, which a computing role must do before promotion
  to 'checked'.
bearing: partially confirms the Maillet determinant as an independent exact-
  integer route to h^-(Q(zeta_q)) (rule 11 second route); the h_1=1 values give
  no traction on distinguishing routes, so the full claim stays pending the
  script run at h_1>1 primes.
anchor: research/sources/kummer-ratio-maillet-handcheck.md
answers: (partial) maillet-determinant-equals-class-number
```
