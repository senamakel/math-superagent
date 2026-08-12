# MathWorld — Multiperfect Number

Source: https://mathworld.wolfram.com/MultiperfectNumber.html — `[[mathworld_multiperfect_number.full]]`

## What it establishes

n is **P_k-multiperfect** if σ(n) = k·n for integer k>2 (k=2 is the perfect
numbers). Tables of first few P_k for k=2..6 (e.g. P_3: 120, 672, 523776,
459818240, 1476304896, 51001180160; P_4: 30240, 32760, 2178540, 23569920; ...).

- **Lehmer (1900–1901) lower bounds:** P_3 has ≥ 3 distinct prime factors,
  P_4 ≥ 4, P_5 ≥ 6, P_6 ≥ 9, P_7 ≥ 14, etc. (a structural result on the
  integer-abundancy side; has no direct half-integer analogue used by the run).
- 251 pluperfect (multiperfect) numbers were known by 1911 (Carmichael &
  Mason).

## Relation to PE 241

- Integer-abundancy theory is the twin of this run's half-integer-abundancy
  problem; the run already covers it via A007691, OEIS-wiki,
  Numericana, Flammenkamp (claims `flammenkamps-tree-search-method`).
- Lehmer's prime-factor bounds do **not** transfer: the run's DFS force-cancels
  denominators and never needs to bound the number of distinct primes of the
  *completion*, only that the cofactor's smallest prime factor is forced.
- No half-integer-abundancy content; no bound ≤ 1e18; no member of the answer
  set (integer abundancy ≥ 1 is disjoint from half-integer).

## Verdict

**Background only; does not help the solver.** It corroborates the
multiperfect landscape the library already documents and adds Lehmer's
prime-factor-count bounds for integer abundance, which this run does not use
(the hemiperfect DFS's completeness argument is Alekseyev's
`alekseyev-tree-search-complete`, not Lehmer's bounds). No contradiction with
anything on disk.

Keep one line: MathWorld P_k tables corroborate A007691's multiply-perfect
side. Do not re-read for the DFS.