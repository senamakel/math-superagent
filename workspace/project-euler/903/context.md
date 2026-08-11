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
- **Gap-aware exact pair-inversion probabilities are known and proved two
  independent ways.** Conjugacy-class (Campion-Loth et al., arXiv:2301.00898,
  Lemma 4.7) gives a per-cycle-type closed form affine in the gap and depending
  on a_1, a_2; Pinsky & Schickentanz (arXiv:2510.20654, Thm 1a + Prop 10a)
  give exact per-gap formulas (uniform θ=1 and fixed-point-conditioned), a
  concrete summation route to A_n and B_n.
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
- **Fixed-point counts of powers determine the conjugacy class.** Nathanson
  arXiv:2206.04021 (research/nathanson_fixed_points_powers*, Archiv der Math
  120, 2023): for permutation σ with C(k) k-cycles, the fixed-point count of
  σ^ℓ is F(σ^ℓ) = Σ_{k|ℓ} k·C(k), with cycle counts recovered by Möbius
  inversion C(ℓ) = (1/ℓ)Σ_{d|ℓ}μ(ℓ/d)F(σ^d). A third, character-free way to
  express the conjugacy-class (a₁,a₂) data behind A_n, B_n in terms of fixed
  points of powers — a cross-check machine beside the inversion-probability
  routes, not a closed form.

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
- **A second, fully independent and complete exact derivation of the same
  gap-affine, fixed-point-driven inversion mechanism exists, for the uniform
  case the run sums over.** Pinsky & Schickentanz, arXiv:2510.20654
  (research/pinsky_schickentanz_ewens_html*): exact pair-inversion probability
  under Ewens sampling P_θ^(n) (uniform = θ=1), unconditioned (Thm 1a: affine in
  the gap, translation-invariant) and conditioned on exactly m fixed points
  (Prop 10a: exact five-term closed form, each term affine in the gap j−i; the
  fixing probabilities D_{n,m} are Prop 4).  So translation-invariance and
  gap-affineness are now backed by *two* independent proofs, and Prop 10a/4 give
  a concrete per-gap, per-m (a_1) summation route to closed forms for A_n, B_n —
  the run's only remaining inputs for Q(10^6).
- **θ=0 (cyclic/rotation) exact pair-inversion probability:**
  1/2 + (j−i−1)/[(n−1)(n−2)] (recoverable from Thm 1a), the small-exponent
  inversion structure f_n(k) aggregates.
- **This turn: fixed-points-of-powers identity added.** Nathanson arXiv:2206.04021
  (research/nathanson_fixed_points_powers*): F(σ^ℓ)=Σ_{k|ℓ}k·C(k), Möbius
  reconstruction of cycle counts, conjugacy class determined by fixed points of
  powers — a third independent, character-free structural fact for the a₁/a₂
  conjugacy-class sums behind A_n, B_n.
- **Implication / open step refined.**  As with Campion-Loth and Cambie-Yan,
  neither source covers the still-open core: summing Lehmer/factoradic ranks over
  the cyclic subgroup {π^i} of a single permutation; and the exact derivations
  here concern the inversion statistic of a single random π, not inversion counts
  of powers π^k across k.  So they give mechanism and route, not the Q(n)
  computation itself.

## Gaps

What the run still needs from the literature and has not found.

- The sum of Lehmer/factoradic ranks (a non-class statistic) over the cyclic
  subgroup {pi^i} of a single permutation.  memory.md has reduced Q(10^6) to
  closed forms for A_n and B_n; Campion-Loth et al. now gives the per-gap,
  per-class mechanism but still no closed form for A_n, B_n themselves.  That
  remains the core open step.

- A closed form / full summation for A_n and B_n (the only remaining inputs for
  Q(10^6)).  The library now has three independent structural facts tying these
  to conjugacy-class data (Campion-Loth Lemma 4.7; Pinsky–Schickentanz
  Prop 10a/4; Nathanson fixed-points-of-powers identity), plus a
  character-theoretic machine (Hultman) — all routes to the summation, none yet
  executed to a closed form.
