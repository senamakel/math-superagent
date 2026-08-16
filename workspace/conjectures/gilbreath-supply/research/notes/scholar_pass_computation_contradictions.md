# Scholar pass: computation-driven corrections and the switch-side refutation

Follows `scholar_pass_new_material.md` (Pivato bridge, fold-rank, RW caveat).
This pass covers the freshly computed/checked work-product and the five
citation digests, against GOAL (test whether the fold Φ does work the
switch-density form cannot see).

## Newly established (computed/checked, the strongest evidence class)

**R-finite-verified is FALSE at its full range** (`r-finite-verified-contradicted`).
The settled rung "ν₂(n)/n ≥ 0.42 for all 50 ≤ n ≤ 4000" fails: exactly 10
points have ν₂/n < 0.42 (deepest ν₂(53)/53 = 0.3585; n ∈ {62,66,71,103,105,145,153,210,274}),
all in [50,274]. Two independent exact computations (exact DP cross-checked vs
brute oracle) agree. Correct: ν₂/n ≥ 0.42 for all n ≥ 500; exceptional set ⊆ [50,274];
tail min ≥ 0.443. The full measured range over [50,4000] is [0.3396, 0.6170], not
problem.md's [0.42,0.52] sampled band. Averaged/density-1 conclusions survive
(tail still ≥0.44, only 10 violations). Contradicts recalled `R-finite-verified`.

**Convention collision (the single most important correction of this pass).**
The literal geometric suffix definition — "maximal {0,2} suffix of the right
diagonal, A_k(n−1−k)" — gives **ν₂(n) = 0 for every n**: the bottom cell is
always 1 (Gilbreath's first-column 1), which truncates any {0,2} run
(`literal_suffix_nu2(10)=0` vs `fold_nu2(10)=7`). The operative object is the
FOLD wt(Φ_n h) (problem.md fact 1, G-dict). Every ratio, kernel fact, and
control refers to the fold. This is not papered over; it is the re-grounded
definition.

**Switch-side lemmas are FALSE as literally stated** (`single-boundary-one-refutes-switch-equivalence-as-stated`).
The per-window family h^{(n)} = e_{n−1} (single 1 at the final index) has switch
density 1/(n−1)→0 yet ν₂(n) = wt(Φ_n h^{(n)}) = n−2 = Θ(n): the depth-d diagonal
reads the window's final index n−1 (offset o=d, always a submask of d) for every
d ∈ [2,n−1]. Refutes R-switch-equivalence and G-eq-sparse-fold-is-sublinear
("switch density 0 ⇒ ν₂ = o(n)") and the literal windowed G-sup-implies-switch.
**Restriction:** per-window, NOT a fixed string — a fixed single 1 at one position
does not give linear ν₂ across all large n, so the prime-realizable equivalence
(GOAL 3) and G-weak-input-strictness remain open.

**Oracle validation** (oracle_fold_verify.py): two independent routes (Lucas
submask shortcut, explicit Pascal-product construction) agree wt(Φ_n h) on
n=2..80 within the documented ±1 floor-at-2 slack; ν₂(4000)/4000 = 0.4938
reproduces problem.md's 0.4933. BUT problem.md's figure (c) min ν₂/w = 0.7049
over n=100..2000 is NOT reproduced (brute gives 0.597 at n=105) — either a
different w, convention, or n-range; flagged, untraced, must not be leaned on.
Band (a) "no downward drift" has mild outliers (n=53→0.34).

## Sources that do not help (so nobody re-reads them)

- `citations_w1554274636/2027719385/2295728007/2953389333/4210391712` — five
  citation-graph lookup files (Maynard, ABGS, LOS, Pivato-Yassawi, Allouche–
  Shallit). Each is a reference list, explicitly "filed by a citation-graph
  lookup, not read", "none of them is evidence". No claim. Their cited sources
  that bear on this problem are already digested (Shiu, Maynard, ABGS, LOS,
  Pivato, AS). No action.
- `odlyzko_gilbreath` — a bibliography index page, not evidence; canonical
  Odlyzko 1993 already digested.
- `granville_martin_prime_number_races` / `_prime_races` — two mirrors of one
  paper, both kept intentionally; single-residue race context only (already
  `gm-chebyshev-bias-positive-density`).

## What the library still lacks (unchanged, now sharper)

- **Finite-prefix transfer**: quantitative wt(Φ_n h) ≥ c·n (all n ≥ N₀ or on a
  density-1 set) from an arithmetic input on the prime-gap parity prefix. Both
  halves missing: (a) is h Lucas mixing / does its measure satisfy the
  correlation decay; (b) quantitative weak-* → weight. Central gap, still open.
  Request `walsh-spectral-subset-b904` stays OPEN (the Pivato note's `answers:`
  retracted as overclaim).
- The trace of figure (c) 0.7049 (see oracle validation) is unresolved.

## Cross-checks added this pass

- The single-boundary-one refutation is consistent with `switch-equivalence.md`'s
  earlier kill (h=e_{2^m}) — same single-sparse amplification obstruction,
  now shown to survive the literal windowing because the 1 sits at the read
  boundary every depth shares. Both are per-window / boundary-realizable, not
  fixed-string; the converses (GOAL 3) are unscathed.
- nu2_range note reconciles an internal edge: pattern_finder's min 0.3585 at
  n=53 (ν₂=19) vs capture's 0.3396 (ν₂=18) is the ±1 floor convention edge, not
  a sweep contradiction.

## Memory written

Fold-rank correction, R-finite-verified contradiction + true range, convention
collision, single-boundary-one refutation, Pivato Thm 7.1 + finite-transfer
caveat, RW-does-not-cover-fold, averaged empirical + negative controls,
switch-side-open/equal-side-strengthened synthesis. The first bulk of durable
entries; recall was empty before (Cognee 404s have cleared).
