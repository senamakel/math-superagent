# Shared context

What the run's reference library establishes, in the words of the run rather
than of the sources. The research team writes this; everyone reads it.

It exists because `research/INDEX.md` answers a different question. The index
says what each file *is* — one row per source, so reading it means holding
thirteen descriptions in your head and doing the synthesis yourself, every
time, in every role. This file says what the library *means for this problem*:
the definitions and results now available, what they let the run compute or
rule out, and where two sources disagree.

Keep it short enough to read on every turn — a few hundred words. It is not a
summary of the sources; it is the standing brief that a new attempt, a new
approach, or a fresh judgement can act on without opening anything.

## Established

What the library now lets this run treat as known, with the file that
establishes each. Empty until the research team has read something.

- **Expected descents & inversions in pi^k have closed forms** (uniform pi,
  fixed k, n>=2k+1): explicit divisor-function formulas (tau, sigma, tau_o).
  Cambie-Yan arXiv:2408.01211 (research/cambie_yan_*). Confirms Archer-Geary.
  This is the mechanism behind the empirically-exact linear form of
  f_n(k) = A_n + (k-1)B_n for the small-exponent regime.
- **A general character-theoretic machine exists for expected permutation
  statistics on products of class-distributed random permutations** (mean
  statistic expanded in irreducible S_n characters; explicit expansions for
  excedance, inversion, descent, major index, k-cycle). Hultman arXiv:1301.0430
  (research/hultman_products_random_permutations.md). This is the standard
  non-enumerative tool for the conjugacy-class sums that A_n and B_n break
  into — but it covers products of independent permutations, NOT the cyclic
  subgroup {pi^i} nor lexicographic rank, which are the unresolved pieces.
- **Negative OEIS results**: A_n, B_n/(n-1)!, Q(n), and probe sequences are not
  in the OEIS — no catalogued closed form/recurrence (research/oeis_*.md).

## Contradictions

Where sources disagree, or where a source contradicts `memory.md`. These are
the most valuable rows here: record them rather than silently picking a side.

(none recorded yet)

## New

What this turn's enrichment added that was not known before.

- **Per-conjugacy-class inversion probabilities are affine in the gap and
  translation-invariant, with a closed form.** Campion Loth, Levet, Liu, Stucky,
  Sundaram, Yin, arXiv:2301.00898 (research/conjugacy_class_statistics_body*),
  Lemma 4.7: Pr_λ[I_{i,j}=1] = 1/2 + a_2/(n(n−1)) − a_1(a_1−1)/(2n(n−1))
  + (j−i−1)·[n − n·a_1 − a_1 + a_1² − 2a_2]/[n(n−1)(n−2)], depending on the gap
  j−i but not the absolute positions, and linear in that gap — the *proved*
  version of the run's empirical f_n(k)=A_n+(k−1)B_n.  λ is the cycle type
  (a_1 = #fixed points, a_2 = #2-cycles).  Weighted-inversion statistics
  (Theorem 4.8) have first moments depending only on n, a_1, a_2; higher moments
  are polynomial in n for symmetric constraints (Theorems 7.16, 7.26).
- **Implication / open step refined.**  This and Cambie-Yan (inversion counts
  in pi^k, n≥2k+1) are two complementary sources of the same gap-affine
  mechanism.  Together they make plausible the route to closed forms for A_n, B_n
  by summing the per-ν formula over cycle types.  Neither covers the still-open
  core: summing Lehmer/factoradic ranks over the cyclic subgroup {pi^i} of a
  single permutation.

## Gaps

What the run still needs from the literature and has not found.

- The sum of Lehmer/factoradic ranks (a non-class statistic) over the cyclic
  subgroup {pi^i} of a single permutation.  memory.md has reduced Q(10^6) to
  closed forms for A_n and B_n; Campion-Loth et al. now gives the per-gap,
  per-class mechanism but still no closed form for A_n, B_n themselves.  That
  remains the core open step.
