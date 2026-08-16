# Multi-point residue patterns ⇒ odd fold cells: the Maynard/Lau densification route

```approach
idea: >
  Attack GOAL priority 2 from the pattern side, not the pair-correlation
  side. The fold cell at depth d is a fixed XOR over a WINDOW of the switch
  string h: for example depth d=2 reads T(n,2) = h[n−3] ⊕ h[n−1] (submasks
  of 2 are {0,2}), and in the residue string r_j = q_j mod 4 this is
  [r_{n−3}≠r_{n−2}] ⊕ [r_{n−1}≠r_n] — a genuine 4-point residue pattern of
  consecutive primes. ν₂(n) = #{d ∈ [2,n−1] : T(n,d)=1} therefore counts how
  many of these window patterns are odd, and SUPPLY asks for c·n of them.
  The dead reduction needs the ADJACENT two-point switch (open, ABGS §9); this
  route instead asks: does the prime residue string contain, with positive
  density, a FAMILY of multi-point patterns (each a fixed XOR of switch bits,
  i.e. a fixed ±1 product of the quadratic character at consecutive indices)
  whose oddness forces many fold cells? The named engines are the
  unconditional theorems on consecutive-prime residue PATTERNS: Maynard's
  admissible-tuple machine, Banks–Freiberg–Turnage-Butterbaugh (equal-residue
  strings with bounded gaps — on disk as bftb-bounded-gap-equal-residue-strings),
  and Lau's theorem (lau-pattern-count-bound: ≫ m/(log m)^10 · φ(q)² of the
  φ(q)² residue m-tuples occur infinitely often, including NON-constant
  patterns). The route's job is the densification step none of them states:
  infinitely-often (or bounded-gap) non-constant patterns ⇒ a positive
  density of odd fold cells.
mechanism: >
  (1) Fold-cell = window pattern: by the linearisation, T(n,d) = ⊕_{o⊆d}
  h[n−1−d+o], and each h[j] = [r_j ≠ r_{j+1}], so each cell is a polynomial
  (XOR product) in the residue comparisons at consecutive indices — a
  multiplicative character correlation of the shape already proved
  (endpoint-sign-corrected-identity) but indexed by a single d, i.e. a fixed
  pattern of the residue string, not a sum over all d. (2) Counting transfer:
  let P be a family of residue m-tuples with the property that, whenever a
  translate of P occurs in the residue string at the right window, some set of
  fold cells is odd. Maynard/BFTB give such translates with bounded gaps
  (equal-residue patterns are the wrong parity direction, so P must be chosen
  NON-constant, which is where Lau's infinitely-often result enters). (3) The
  load-bearing step is a densification lemma: a sparse-but-infinite supply of
  non-constant patterns spread over bounded gaps forces, through the window
  overlap of consecutive depths, a positive density of odd T(n,d) — i.e. the
  fold converts "infinitely often" into "positive density" by reading each
  pattern at many (n,d) simultaneously. This is the step to price; if it
  needs positive pattern density (the open form) the route collapses to the
  parity barrier and must say so.
status: refuted
precedent: >
  The named arithmetic engines are real and precisely stated but FAIL their
  hypotheses at the fold's modulus or supply the wrong direction; no source applies
  them to wt(Φ_n h). (1) Lau, arXiv:2409.12819, Thm 1.5 / Cor 1.6–1.8
  (lau-pattern-count-bound): for q SQUAREFREE with φ(q) ≫ (log m)^10, at least
  ≫ m/(log m)^10·φ(q)^2 residue m-tuples occur infinitely often — but 4=2^2 is
  NOT squarefree, so it does not apply at q=4, m=2; and Lau's own emphasis
  (lau-nonconstant-pattern-open) is that even one non-constant pattern of length m
  is beyond reach. (2) Maynard 3.3 (maynard-positive-density-congruent-strings) and
  BFTB (bftb-bounded-gap-equal-residue-strings): unconditional at q=4 but the
  EQUAL-residue (wrong) direction — runs of equal residues are runs of constant h,
  i.e. closed doors #2/#3, not a source of odd/switch cells. (3) ABGS
  (abgs-p1-wide-open): positive mod-4 switch density is L-function-inaccessible.
  Grounding: research/grounding_three_current_candidates.md §3.
killed-by: >
  lau-pattern-count-bound hypotheses fail at q=4 (modulus must be squarefree; 4=2^2
  is not) AND lau-nonconstant-pattern-open (even one non-constant mod-4 pattern is
  beyond reach) AND maynard-positive-density-congruent-strings / bftb-bounded-gap-
  equal-residue-strings supply only the equal-residue (wrong) direction. The
  densification step has nothing to densify: there is no provably-infinitely-often
  supply of the non-constant patterns the fold's odd cells need, so the window-
  overlap lemma is never fed. The route collapses into the dead switch-density
  reduction at its first step (its own falsifier (a)/(c)).
first-step: >
  tool_builder + scholar, exact residue arithmetic, real primes up to x=10^6:
  (1) enumerate, for each small depth d ∈ {2,3,4,5}, the residue pattern(s)
  that make T(n,d)=1, as explicit m-tuples over {1,3} (e.g. d=2 gives the
  4-point patterns above). (2) For each such pattern measure its occurrence
  DENSITY in the real residue string up to 10^6, and its bounded-gap /
  infinitely-often status against the named theorems (BFTB equal side; Lau
  non-constant side). (3) The decisive experiment: for the patterns that
  Lau/BFTB are known to guarantee infinitely often, compute how many fold
  cells they force as n runs to 10^6 — if the forced cells have positive
  density in n, the densification lemma is empirically real and the theorem
  is the target; if they have density 0, the route dies here with that
  reason. FALSIFIER: if NO non-constant pattern is provably infinitely often
  (Lau gives many but the specific window patterns may not be among them), or
  if infinitely-often patterns force density-0 cells, the route is dead.
falsifies: >
  (a) the specific window patterns (fixed-XOR patterns of switch bits) are not
  among the m-tuples Lau/BFTB/Maynard guarantee to occur infinitely often
  (then the arithmetic input does not reach the fold's own patterns); (b) the
  densification lemma is false — infinitely-often non-constant patterns force
  only o(n) fold cells (then the fold does NOT convert sparse pattern
  occurrence into density, and the route closes); (c) the patterns that ARE
  provably infinitely often are all equal-residue (the known direction), so
  the non-constant side is the open parity barrier and this route collapses
  into the dead reduction.
