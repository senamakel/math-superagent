# Cima–Gasull–Mañosas 2020 — "Around some extensions of Casas-Alvero conjecture for non-polynomial functions"

**Source:** Extracta Mathematicae 35(2) (2020), 221–228. doi:10.17398/2605-5686.35.2.221 ·
Full text: `research/sources/cima_gasull_manosas_2020_extensions-casas-alvero.full.md`

**What this source is.** A short primary paper whose *main* content is two
non-polynomial extensions of the real Casas-Alvero conjecture, shown to be
false. Its interest to this run is (a) the up-to-date status survey in its
introduction, and (b) the char-p counterexample it reproduces.

## The status survey (with a real discrepancy)

The introduction reviews the state of CA as of 2020:

- For n ≤ 4 it is "a simple consequence of the Gauss–Lucas Theorem."
- In 2006, proved for n ≤ 8 by Maple (Díaz-Toca & González-Vega [5]).
- Later proved when n is p^m, 2p^m, 3p^m or 4p^m for a prime p (Draisma–de
  Jong [6], Graf von Bothmer et al. [7]).
- They cite Castryck–Laterveer–Ounaïes [3] "verification in degree 12."
- **"The first cases left open are those where n = 24, 28 or 30."**

The last claim **skips 20**. This directly contradicts the run's established
claim `smallest-open-degree = 20` (sourced from Castryck et al. 2012 and
Schaub–Spivakovsky 2024). Reconcile:

- 20 = 4·5. The 4p^e theorem **excludes p ∈ {3,5,7}** (Draisma–de Jong), so
  p=5 is excluded: **20 is NOT covered by 4p^e.**
- 20 is not p^k, 2p^k, 3p^k, or 5p^e (5·4 needs a prime-power base 4, which is
  not p^e in the needed sense), nor is 20 of form np^ℓ with known good p for
  base n.
- The run already holds Massri 2018 (a *partial* result toward degree 20:
  "no counterexamples with three recycled roots"), which would be vacuous if
  20 were settled.

**Verdict:** 20 is genuinely open; the 2020 survey's "24, 28, 30" is an error
in a passing status remark (it is not the paper's focus, and its own cited
[3] settles 12, not 20). The run's `smallest-open-degree = 20` stands.

## The char-p counterexample it reproduces

In characteristic 5, P(x) = x²(x²+1), roots {0,0,2,3} (note 2²=4≡−1 mod 5,
so x²+1 = (x−2)(x−3)). Derivatives: P′ = 2x(2x²+1), P″ = 12x²+2 = 2(x²+1),
P″′ = 4x — each shares a root with P, and P is not a pure power. This is a
further char-p family, distinct from the run's held x^{p+1}−x^p witness but of
the same form (x^{p−1}·quadratic). It confirms (not contradicts) the central
hard constraint: **CA is false in char p, so any proof must use char 0.**

## The non-polynomial results (out of scope, recorded for completeness)

- **Q1 (smooth C^n, F^(n)≠0, n real zeroes):** rigidity holds for n ≤ 4 but
  fails for n = 5 (explicit F via repeated integration; c₁≈1.79343, d≈3.32178).
- **Q2 (real analytic, all but one derivative):** already false for n = 2
  (F(x) = 4x²+π²(cos x − 1)).

These reinforce the authors' closing intuition: CA rigidity is specific to
polynomials, so a functional-analytic route would have to explain what the
polynomial structure supplies that smooth/analytic functions lack.

## For the run

- **Records a cross-source discrepancy** (survey says 24/28/30; Castryck &
  Schaub–Spivakovsky say 20). Resolved in favour of 20. See research/sources
  list and the contradiction row.
- **Documents a second char-p counterexample family** — a negative control
  the oracle already handles, now with a second primary citation.
- No new hypothesis or theorem for the algebraic attack; this is status and
  context.
