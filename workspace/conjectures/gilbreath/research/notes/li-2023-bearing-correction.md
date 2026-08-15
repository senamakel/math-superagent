# Li 2023 α = 0.52 — what it actually moves in Route B (correction)

**Source read:** Runbo Li, arXiv:2308.04458 v8 (Oct 2025), full text
`research/sources/li-2023-primes-in-short-intervals-harman-sieve.full.md`.

## What the source establishes (verified from the paper/abstract)

**Theorem 1:** for all sufficiently large x, the interval [x − x^θ, x] contains a
prime for every θ ≥ 0.52; equivalently G(x) ≤ x^0.52 ultimately. This sharpens
Baker–Harman–Pintz 2001's 0.525 toward 0.52. Theorem 2 gives nontrivial upper
and lower bounds on the prime count in [x − x^θ, x] for 0.52 ≤ θ ≤ 0.525.
Unconditional. **Status: asserted-by-source** (arXiv, not peer-reviewed as
downloaded; the 0.525 form is independently confirmed by the Visser survey and
BFT 2023).

## The correction: the demand side is NOT Route B's bottleneck

Granville Theorem 5.5 (verified in the Granville full text): if g*_n < n^α and
ν_2(q_{n−1}) > n^β with β > α, then q_n succeeds.

The librarian's summary framed Li's 0.52 as weakening the demand side ("β > 0.52
would suffice instead of β > 0.525"). That is **true but not the bottleneck.** The
supply quantity ν_2 is the count of 2s in the right-diagonal 0-2 cycle, **measured
at ≈ 0.5·n** (n/2 density, run's nu2 checks: ν_2/n ∈ [0.42, 0.52]). Any proof
that ν_2 ≥ c·n for a positive constant c immediately yields ν_2 > n^β for every
β < 1 (c·n > n^β for large n). So:

- The requirement β > α is satisfied as soon as one has a *positive-linear*
  lower bound on ν_2, for ANY α < 1. The exact value of α ∈ {0.52, 0.525} is
  immaterial — both give the same conclusion given an O(n) supply bound.
- Li's 0.005 shave does not make Route B more reachable. What is needed — and
  what no source provides — is a **positive-linear lower bound on ν_2**
  (the number of 2s in the 0-2 cycle of the prime right diagonal). That is the
  real open supply-side statement.

**The honest statement of Route B's gap:** not "β > 0.52 vs 0.525", but
"prove ν_2(q_{n−1}) ≥ c·n for some c > 0". The measure shows c ≈ 0.5; the proof
is open. Li does not help with this.

## What Li genuinely adds to the library

1. A proven-sharper short-interval theorem (0.52 unconditional), independently
   confirming the demand side without the unobtainable BHP primary.
2. A partial-routing to Granville's need: the demand requirement is "a gap bound
   of the form x^α with α < 1" — *any* sublinear unconditional gap bound would
   do, and BHP/Li provide α < 1. This is worth recording: the demand side is
   essentially free (α < 1), the supply side is not.

```claim
id: li2023-not-bottleneck
statement: Li's 0.52 short-interval exponent does not materially lower the
  barrier in Granville's Route B: since Theorem 5.5 needs nu2(q_{n-1}) > n^beta
  with beta > alpha and the measured nu2 is about n/2, any positive-linear lower
  bound nu2 >= c*n gives nu2 > n^beta for every beta < 1, so the alpha value in
  {0.52, 0.525} is irrelevant. The true supply-side gap is proving nu2 >= c*n.
hypotheses: Granville Theorem 5.5 reduction; nu2 density ~ n/2 measured but
  unproved.
holds-here: yes — this reframes Route B so the run does not spend effort
  shaving alpha; the bottleneck is the linear nu2 supply bound.
status: deduction (this run; consistent with li2023-short-interval-052,
  lemma54-rederivation-safe, granville-nu2-density-measured)
bearing: directs the remaining Route B work at the nu2 supply bound, not the
  demand exponent; prevents a wasted attempt chasing a smaller alpha.
anchor: research/sources/li-2023-primes-in-short-intervals-harman-sieve.full.md;
  research/notes/li-2023-bearing-correction.md
follows-from: lemma54-rederivation-safe, li2023-short-interval-052
contradicts: none (it narrows, not contradicts, the librarian's bearing on li2023)
```
