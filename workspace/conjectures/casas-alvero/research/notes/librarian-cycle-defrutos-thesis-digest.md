# Librarian cycle — digest of the undigested de Frutos Marín thesis

## What this cycle did

The de Frutos Marín 2012 PhD thesis full text was added to `research/sources/`
in a prior cycle but its summary (`research/summaries/defrutosmarin2013_thesis.md`)
was still the auto-generated conversion template — no digest had been written, no
claim extracted. The run "held" the thesis without being able to say what it
establishes, which is the library's specific failure mode (a held file nobody can
cite).

This cycle read the load-bearing section (§5.6 Discriminantes, lines ~10580–11027 of
the full text), replaced the template with a real digest, stored the verified finding
in Cognee, and indexed the summary.

## What the thesis establishes that the library did not previously hold

**The discriminant ("superdiscriminant") route to the bad-prime lists** — independent
of, and structurally different from, the minor-criterion route the run verified at
n=4 and n=5.

- Δ(n,I): generator of 〈N_1(s_1), R(s_1)⟩ ∩ ℤ; δ(n,I) = Res(R(s_1), N_1(s_1)).
- **Obs 5.6.9**: Δ(n,I) ≠ 0 ⟺ δ(n,I) ≠ 0 ⟺ no {i,j,k}-counterexample to CA of degree n.
- **Lemma 5.6.10 / Thm 5.6.11**: for every prime p,
  `δ(n,I) ≢ 0 mod p ⟺ [Δ(n,I) ≢ 0 mod p and µ ≢ 0 mod p]`,
  µ = gcd of the leading coefficients of R and N_1.
- **Thm 5.6.13** (terminating): with superdiscriminant D_n = ∏_{i=1}^{n−2} Δ(n,I_i),
  for p ≥ n: **p ∤ D_n ⟹ p efficacious for n and CA holds for all degrees n·p^r**;
  **p ∤ D̃_n ⟹ CA holds in degree n itself.** This is a direct route from one prime to
  CA in degree n, alongside the family-lift.

**Worked example n=5** (the run's verified degree):
Δ(5;{3}) = C(5,3)−1 = 9 = 3²; Δ(5;{2,3}) = 2²·3²·11·3541;
δ(5;{1,2,3}) = 2²⁴·3⁶·7³·131·193·599²·8009 (µ = 1). Od Thm 5.6.11 the primes
dividing Δ(5;{1,2,3}) are {2,3,7,131,193,599,8009} (7 of the 9); the remaining two,
{11,3541}, come from Δ(5;{2,3}). Together these recover the full n=5 bad list
{2,3,7,11,131,193,599,3541,8009}. Same behaviour stated for n=3 and n=4.

## Why this matters

1. It is a **third, closed-form route** to the n=5 bad list the run already verified
   by rank-over-F_p minor criterion and semantic enumeration. The specific integers
   2²⁴·3⁶·7³·131·193·599²·8009 and 2²·3²·11·3541 are *checkable* — recomputing them
   cross-validates the held thesis against the run's own two routes. Recorded as the
   natural calibration in `research/summaries/defrutosmarin2013_thesis.md`.
2. **Thm 5.6.13(b)** is a route to CA in degree n from a single prime p ∤ D̃_n —
   conceptually the same "one good prime lifts the whole degree" engine the run's
   arithmetic-jet-lift rests on, stated with an explicit discriminant.
3. The thesis also holds char-p material on the "neta" derivative (§1.2, relevant to
   the closed hasse-vs-ordinary thread) and Gröbner-basis feasibility statements.

## Caveat / evidence class

All discriminant statements are **asserted-by-source** — read from the thesis, not yet
independently recomputed. The n=5 integers are the calibration a future run should
check; until then this is corroboration of the bad lists, not new proof. The thesis's
n=5 numbers match, prime-by-prime, the run's own verified degree-5 result, which is
indirect support that both are right.

## Status

Summary digested (`research/summaries/defrutosmarin2013_thesis.md`), indexed, finding
in Cognee. Library totals unchanged (no new download — the thesis was already held).
Frontier confirmed: searches on the multiplicity/dimension and Chebyshev/cyclotomic
angles return only already-held canonical sources; nothing new to fetch.
