# verify_bundle — four-section exact-integer verification

Executed `code/verify_bundle.py`, EXIT 0, under `timeout 540`.
Captured at `code/out/verify_bundle.captured.txt`. Total runtime 431.7s.

All exact integer arithmetic (Python ints, gmpy2.isqrt / gmpy2.iroot when
available, `pow` for modular exponentiation). No floats, no logarithms for
comparison. None of these sections is a proof — each is a bounded exact check
that *extends* the range of a prior verified-numeric result.

## Section 1 — oracle bound extension (runtime 0.74s)

`solutions(N)` from `scholar_oracle.oracle`:

- `solutions(10^10) = [(3,2,2,3)]` exact (0.04s)
- `solutions(10^12) = [(3,2,2,3)]` exact (0.70s)

Settles: no second solution of `x^p - y^q = 1` with both `x^p, y^q <= 10^12`
(prior bound was `10^8`). Exact integer arithmetic — the oracle enumerates
perfect powers as a set and checks consecutive values.

## Section 2 — Case-A descent subclaim extension (runtime 0.78s)

`r^q - 2^(m*q-2) s^q = ±1`, q odd prime, m>=1, r,s>=1, gcd(r,s)=1.

Extended range: **q odd prime <= 101 (25 primes), m in [1,10], r,s in [1,2000].**
(prior: q<=37, m<=8, r,s<=500).

Method: for each (q,m,s) check whether `2^(mq-2)·s^q ± 1` is an exact q-th
power (gmpy2.iroot), the root being r. gcd(r,s)=1 is forced by construction.

Result: only hit is `(q,m,r,s,sgn) = (3,1,1,1,-1)` — the known solution
`1^3 - 2^1 = -1` (Lebesgue image `3^2 - 2^3 = 1`). **Zero counterexamples.**

## Section 3 — Case-B Ljunggren step extension (runtime 33.35s)

`T(c,p) = sum_{i=0}^{p-1} (c^2+1)^i = ((c^2+1)^p - 1)/(c^2)`.

Extended box: **c in [1, 10^5], odd primes p in [3, 251] (53 primes)**
= 5,300,000 `(c,p)` pairs (prior: c<=2000, p<=101).

Exact integer isqrt square test. **0 squares found** (expected 0). Closest
near-miss: `(c,p) = (1,3)`, `T = (2^3-1)/1 = 7`, `isqrt=2`, gap `7-4 = 3`.

## Section 4 — cross-prime survivor re-check (runtime 396.9s + 0.00s)

Recomputed `h^-(Q(zeta_p))` for **all 45 odd primes < 200** via
`lib.cyclo.h_minus` (exact cyclotomic Bernoulli product). All values match the
prior `crossprime_sweep200` run and OEIS A000927 (p=3..199, e.g. h^-(47)=695,
h^-(139)=1753848916484925681747).

Then exact integer division for every pair `p<q<200`:
`q | h^-(Q(zeta_p))` AND `p | h^-(Q(zeta_q))`.

- **Survivors: exactly one — `(47, 139)`.** Confirmed.
- **Double-Wieferich on (47,139):**
  - `pow(139,46,47^2) = 1035 (mod 2209)`, `==1`? **False**
  - `pow(47,138,139^2) = 7507 (mod 19321)`, `==1`? **False**
  - → (47,139) fails **both** double-Wieferich congruences. Confirmed.

## Where the known solution sits (falsifier)

- S1 returns the known solution `(3,2,2,3)` — satisfied.
- S2 returns the known descent root `(3,1,1,1)` — satisfied (uniqueness claim).
- S3/S4 are conditional on a hypothetical odd-prime solution `x^p-y^q=1`
  (p,q odd primes, both exponent-2 cases handled separately elsewhere); the
  known solution has `p=2` (even), so it is **excluded by hypothesis**, never
  rejected.

## Status

Four independently-extended verified-numeric ranges, each reproduced by exact
integer arithmetic and each agreeing with its prior smaller run where the
ranges overlap. Not proofs. `verify_bundle.py` is the single reproducible
bundle; these numbers are all traceable to
`code/out/verify_bundle.captured.txt`.

```claim
id: verify-bundle-2024-ext
statement: (1) solutions(x^p-y^q=1) with x^p,y^q<=10^12 is exactly [(3,2,2,3)].
  (2) r^q - 2^(mq-2)s^q = +/-1 over q odd prime<=101, m<=10, r,s<=2000,
  gcd=1, has only (3,1,1,1). (3) T(c,p)=((c^2+1)^p-1)/c^2 over c<=1e5,
  odd prime p<=251 is never a square (5.3e6 pairs, 0 squares). (4) the
  cross-prime h^- condition q|h^-(Q(zeta_p)) AND p|h^-(Q(zeta_q)) has
  exactly one survivor p<q<200, namely (47,139), and (47,139) fails both
  double-Wieferich congruences.
hypotheses: exact integer arithmetic; bound N<=10^12 for S1, q<=101/m<=10/
  r,s<=2000 for S2, c<=1e5/p<=251 for S3, p<q<200 for S4.
holds-here: yes — every claim is satisfied at the known solution or excludes
  it by hypothesis (odd-prime gate); zero counterexamples found.
status: checked (verified-numeric over the stated extended ranges; not proofs)
bearing: pushes oracle bound 4 orders, descent subclaim range from
  (q<=37,m<=8,r,s<=500) to (q<=101,m<=10,r,s<=2000), Ljunggren box from
  (c<=2000,p<=101) to (c<=1e5,p<=251); re-confirms the unique cross-prime
  h^- survivor (47,139) below 200 and its non-double-Wieferich-ness.
anchor: code/out/verify_bundle.captured.txt
```

## Next (gaps this leaves)

These are still *verified-numeric*, not proved: the Case-A descent subclaim,
the Case-B Ljunggren step (T never a square for all c,p), and the cross-prime
h^- condition as a *consequence* of a hypothetical solution (the descent
reduction itself is cited, not proved in-workspace). The effective analytic
bound remains astronomically far from any computational closure; these only
widen the verified envelope.
