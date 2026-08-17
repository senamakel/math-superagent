# Erdős–Lacampagne–Selfridge 1993 — "Estimates of the least prime factor of a binomial coefficient"

<!-- source: https://doi.org/10.1090/s0025-5718-1993-1199990-6 (AMS Math. Comp. 61 (1993) 203, 215–224; accessed via ADS abstract) -->

P. Erdős, C. B. Lacampagne, J. L. Selfridge, "Estimates of the least prime
factor of a binomial coefficient", Mathematics of Computation 61(203) (1993)
215–224 (Special issue dedicated to D. H. Lehmer). DOI
10.1090/s0025-5718-1993-1199990-6.

**Hold status: ABSTRACT-ONLY.** The AMS PDF exceeds this run's 5 MB download
cap (attempted and abandoned); no free mirror is known. What is recorded here is
the *published abstract*, quoted verbatim in two independent sources (ADS
1993MaCom..61..215E and the AMS DOI record), plus the definitions that
abstract carries. This is attestation of the statements, not possession of the
proofs.

## What the abstract establishes (verbatim facts)

- Studies the **least prime factor p = p(N,k)** of C(N,k) for k ≥ 2.
- **Conjecture: p(C(N,k)) ≤ max(N/k, 29)**, supported by "considerable
  numerical evidence".
- **Good** binomial coefficient: p(C(N,k)) > k.
- **Deficiency**: for 1 ≤ i ≤ k write N−k+i = a_i·b_i where b_i contains just
  the prime factors > k; the deficiency of a good coefficient is the number of
  i for which b_i = 1.
- **g(k)** = least integer N > k+1 such that C(N,k) is good; the paper proves
  **g(k) > c·k²/log k** (c an absolute constant).
- Conjecture: the list of 17 binomial coefficients with deficiency > 1 is
  complete; the number with deficiency 1 is probably finite; **all C(N,k) with
  positive deficiency and k < 101 are listed** in the paper.

Facts about the same line from the paper's citations (per the search record):
p(C(N,k)) < N/k for N > k² with noted exceptions; for each k > 2 there exist N
with 2k < N < 4k and p(C(N,k)) > N/k.

## Bearing for this run

Relevant to the `zsigmondy-primitive-prime` and `binary-lucas-submask` threads'
engine: how small the least prime factor of C(n,k) can be, in every k-regime.
The "good" coefficients (all prime factors > k) are exactly the ones where the
Sylvester/EEES large-prime-dominance picture applies cleanly; the paper's
deficiency machinery and its 17-member conjecture quantify how often that fails.
The g(k) > c·k²/log k lower bound is a structural limitation on how far above 2k
one must go to escape small primes — useful when arguing that representations of
a fixed a with large k cannot all sit below 2k.

```claim
id: els-1993-least-prime-factor-bounds
statement: Erdos-Lacampagne-Selfridge 1993 (abstract): conjectured
  p(C(N,k)) <= max(N/k, 29); 'good' binomial coefficients (least prime factor
  > k) have g(k) = least N > k+1 with C(N,k) good satisfying g(k) > c k^2/log k;
  the 17 binomial coefficients with deficiency > 1 are conjectured complete;
  all positive-deficiency C(N,k) with k < 101 are listed.
hypotheses: k >= 2; definitions as in the abstract (a_i,b_i split at prime k).
holds-here: yes — relevant to every bound on representations of a fixed a:
  for k in a middle range the least prime factor is <= max(N/k, 29) (conjecture)
  so the distinct-k representations of a must share a small supply of primes.
status: asserted-by-source (published abstract quoted verbatim in two
  independent records; the paper body is NOT on disk — AMS PDF exceeds cap)
bearing: the quantitative face of the Sylvester-line: least-prime-factor
  control per (N,k); complements EEES 1978 (held, partial) and BFT 2009 (held,
  full) on the large-prime side.
anchor: research/summaries/els-1993-least-prime-factor.md
```