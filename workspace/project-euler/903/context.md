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

## Gaps

What the run still needs from the literature and has not found.

- What the library newly establishes (Hultman's machine) still does NOT cover:
  the sum of Lehmer/factoradic ranks (a non-class statistic) over the cyclic
  subgroup {pi^i} of a single permutation.  memory.md has reduced Q(10^6) to
  closed forms for A_n and B_n, but no source gives those closed forms; that
  remains the core open step.
