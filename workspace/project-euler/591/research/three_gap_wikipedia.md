# Three-gap theorem (Steinhaus conjecture) — Wikipedia (background)

Source: https://en.wikipedia.org/wiki/Three-gap_theorem (full text read).

## What it establishes

**Statement.** For any irrational `θ/2π` and any positive integer `n`, the points
`θ, 2θ, …, nθ` on the circle have **at most three distinct** gaps between adjacent
points; when there are three, the largest gap equals the sum of the other two.
Equivalent algebraic form: the fractional parts `{α}, {2α}, …, {nα}` divide the
unit interval into subintervals of at most three distinct lengths. Unless `α` is a
rational multiple of something periodic, there are at least two distinct gaps.

History: conjectured by Steinhaus, first proved in the late 1950s by Sós (1957/58),
Surányi (1958), Świerczkowski (1959). Liang's short proof also shows the "largest =
sum of the two others" part and a `3d`-distance generalisation. Related: Slater's
earlier copy/itinerary variant, and higher-dimensional generalisations
(Halton; Bleher–Homma–Ji–Roeder–Shen).

## Hypotheses / applicability

Needs `n` points of a single rotation `x ↦ x+α (mod 1)`, `α` irrational. Holds here:
`α = {√d}` irrational (d non-square). It is a **homogeneous** statement — it counts
gap lengths of `{nα}` itself.

## What it implies for this problem

**Background only.** The three-gap theorem explains *why* the record-holding `b`
for `||bα − β||_Z` are few (the orbit near a target `β` is structured into
`δ_k`-scale gaps), and it is the basis on which the Berthé–Imbert algorithm is
built (their Algorithm 2 rests on it). But it does **not** give the minimizer for a
*fix target* `β`: that is the inhomogeneous problem, solved exactly by Cabanillas
Props 9/10 (and, one-sided, Berthe-Imbert), not by this theorem. The precise gap
lengths in terms of `δ_k` used in the run's notes come from van Ravenstein and from
Cabanillas Thm 1, not from this Wikipedia article.

## Does it contradict memory.md?

No. It supports the three-gap facts the notes record. Notably it *agrees* with the
memory claim that semiconvergents/densest-to-0 records describe the homogeneous
(target 0) case: the theorem has nothing to say about a target `β`, which is why
the run needed the inhomogeneous theory.

## Verdict

Useful background; references for proof history and the Liang proof. No
contradiction; does not compute anything. Nobody needs to re-read it in full.
