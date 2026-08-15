# Maynard 2015, "Small gaps between primes" (Ann. Math. 181:383–413)

<!-- source: https://arxiv.org/pdf/1311.4600 (v3, 28 Oct 2019) | full text at research/sources/maynard-2015-small-gaps-between-primes.full.md -->

**FILE CORRECTION (this run):** this summary now describes the genuine paper.
Earlier the full-text file held the wrong document (a portfolio-selection
cs.CE paper from a mis-resolved arXiv id, then a bibliometrics paper, then a
WASP solver paper). The correct arXiv id is **1311.4600** ("Small gaps between
primes", Daniel/James Maynard). The run must not cite the previous content.

## What it establishes (verbatim-anchored)

- **Theorem 1.1.** For every m ∈ ℕ, `liminf_n (p_{n+m} − p_n) ≪ m³ e^{4m}`.
  New: arbitrarily many primes in bounded-length intervals (breaks the
  θ = 1/2 GPY barrier).
- **Theorem 1.2.** For r large and A an r-element set, a positive proportion
  (≫_m 1) of the m-subsets of A satisfy the prime m-tuples conjecture
  (infinitely many n with all n+h′_i prime).
- **Theorem 1.3 (unconditional).** `liminf_n (p_{n+1} − p_n) ≤ 600`.
- **Theorem 1.4.** Assuming primes level of distribution θ for every θ < 1
  (Elliott–Halberstam), `liminf (p_{n+1}−p_n) ≤ 12`, `liminf (p_{n+2}−p_n) ≤ 600`.
- **Proposition 4.3 mechanism.** Mk > log k − 2 log log k − 2 for large k;
  M_5 > 2, M_105 > 4. The method relies only on Bombieri–Vinogradov
  (θ = 1/2 − ε) in the unconditional cases.

## What it does NOT say

- It does **not** contain a normalized-gap bound `liminf (p_{n+1}−p_n)/(√log·(loglog)²) < ∞`.
  The librarian's earlier summary attributed that to "Primes in tuples II
  (Acta Math. 2010)"; it is not in this paper and must not be cited to it.
- All results are **existence** ("there are infinitely many n with..."), not
  **frequency** lower bounds ("such n have positive lower density"). In
  particular the sieve proves the existence of close prime pairs in a
  prescribed residue configuration infinitely often only in the existence
  sense (Thm 1.2's "positive proportion" is positive proportion of admissible
  *tuples*, not of integers n).

## Consequence for this run (Route B ν_2 supply)

The atomic bit feeding Granville's ν_2 is `[p_{n+1} ≢ p_n mod 4]`, a
**two-point** consecutive-pair statistic. Maynard's sieve gives no lower bound
on the *frequency* of a prescribed consecutive-pair residue switch, so it
cannot supply `ν_2 ≥ n^{0.525+δ}`. It is the named two-point machinery but
stops short of the frequency the reduction consumes. Consistent with
`gap-bounds-cannot-force-block-growth` and the adopted
`chebyshev-bias-granville-nu2-supply` approach.

```claim
id: maynard-2015-existence-not-frequency
statement: Under only Bombieri–Vinogradov (θ=1/2−ε), liminf_n(p_{n+1}−p_n) ≤ 600; more generally liminf_n(p_{n+m}−p_n) ≪ m³e^{4m}, and a positive proportion of admissible m-tuples satisfy the prime m-tuples conjecture. All results are existence, not frequency, lower bounds.
hypotheses: primes; Bombieri–Vinogradov (unconditional) for Thm 1.3/1.1; Elliott–Halberstam for Thm 1.4.
holds-here: yes (primes are the object); but the results do not imply ν_2 ≥ n^β
status: proved
bearing: delimits the two-point sieve: it proves closeness of primes (existence), never the frequency of a mod-4 consecutive-pair switch, so Route B's ν_2 supply needs Hardy–Littlewood/LOS-level input, still open.
anchor: research/sources/maynard-2015-small-gaps-between-primes.full.md
answers: supply-frequency-vs-existence
```

```claim
id: maynard-file-content-corrected
statement: The Maynard 2015 full-text file previously held the wrong document (finance cs.CE paper at the mis-resolved id); it now holds the genuine "Small gaps between primes" (arXiv:1311.4600). The librarian's earlier summary credited this paper with a normalized-gap bound that is not in it.
hypotheses: none
holds-here: yes
status: checked
bearing: prevents citing a false result to Maynard and stops re-fetching the wrong arXiv id.
anchor: research/sources/maynard-2015-small-gaps-between-primes.full.md
contradicts: (prior summary content, now overwritten)
```
