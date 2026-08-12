# A Study of @-numbers (Adeyemi, arXiv:1906.05798)

<!-- source: https://arxiv.org/abs/1906.05798 | full text: research/sources/adeyemi_study_of_at_numbers.full.md -->

## What it establishes

Adeyemi (2019) treats a broad generalization of multiperfect and hemiperfect
numbers. An *@-number* of order (alpha, beta) is an integer n satisfying

    sigma_alpha(n) = alpha · n^beta,

where sigma_alpha(n) is the sum of alpha-th powers of divisors and alpha lies
in H (rationals/quaternions). The quantity alpha = alpha1/alpha2 with
1 ≤ max(alpha1,alpha2) ≤ omega(n) gives "strong", weak, or very weak
@-numbers.

## Relevance to PE 241

- The hemiperfect condition sigma(n)/n = k+1/2 is the special case
  alpha = k+1/2, beta = 1. So hemiperfect numbers sit inside this family as
  @-numbers of order ((2k+1)/2, 1).
- The paper conjectures there is **no odd strong @-number of order (1,1)**;
  its truth implies no odd perfect number and no odd multiperfect numbers
  exist. By A159907 all hemiperfects are even, consistent with this
  conjecture's spirit (there is a separate evenness proof for hemiperfects:
  2sigma(n)=(odd)n forces n even).
- It gives examples and catalogues solution families, but provides **no new
  enumeration method** and no bound relevant to 10^18. It is background
  confirming the abundance-index framework, not a computational technique.

This is a secondary/adjacent source; the forced-denominator DFS (Laatsch
framework + denominator-cancellation lemma) remains the operative method.
