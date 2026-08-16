# Subcube/Boolean-lattice pricing for `downset-row-code-distance-closed-form`

Answers the adopted approach's stated research step: *"research should price
whether [the fold-row intersection/distance formula] appears in the Boolean-cube
/subcube-intersection literature."* Author: librarian. The formula is held up
only where this note establishes it; mechanical verification (script provided,
run by coder) is still pending but the identity is elementary and hand-checked
here.

## The identity, verified by hand

For the fold row `M_d = { n-1-d+o : o ⊆ d }`, the reflection `x ↦ n-1-x` sends it
to the digital down-set `↓d = { y : y ⊆ d }`:

- `n-1-x = d - o` for `x = n-1-d+o`; since `o ⊆ d`, `d-o = d⊕o` (no borrows), and
  `o ↦ d⊕o` is a bijection of `↓d` (complement within support). ✓

Then, in the Boolean lattice, downsets meet as `↓d ∩ ↓d' = ↓(d∧d')`, so by the
reflection bijection:

- `M_d ∩ M_d' = M_{d∧d'}`, hence `|M_d ∩ M_d'| = 2^{pc(d∧d')}`, and
- `|M_d △ M_d'| = |M_d| + |M_d'| - 2|M_d ∩ M_d'| = 2^{pc(d)} + 2^{pc(d')} - 2^{pc(d∧d')+1}`. ✓

So the row family `R_n = {1_{M_d} : d ∈ [2,n-1]}` is closed under (set)
intersection — a meet-semilattice — even though it is not closed under XOR, which
is exactly why the Delsarte linearity hypothesis fails but an exact geometric
count does not. This is the "one-line" structure the approach builds on.

## Literature verdict (priced, not hunted)

- The **meet/intersection formula** is elementary and standard: it is the
  statement that downsets of a Boolean lattice form a meet-semilattice with
  `↓d ∩ ↓d' = ↓(d∧d')`, carried through the reflection `M_d ≅ ↓d` (affine
  subcubes). No specialised source states anything beyond this; it is a
  two-line argument, not a theorem to cite.
- The recent **subcube-intersection literature** (C. Groenland, thesis 2020,
  https://doi.org/10.5287/ora-xq64n475x; Melo–Winter *JCTA* 2018,
  https://doi.org/10.1016/j.jcta.2018.12.006; Alon–Axenovich–Goldwasser
  hypercube-statistics program; Xu arXiv:2604.13402) studies a **different
  question**: which intersection *cardinalities* a generic `k`-dimensional
  affine (or axis-aligned) subspace can have with `{0,1}^n`, and their
  distribution over all flats. It does NOT give, and is not needed for, the
  exact meet formula for a *specific* family of downset-rows. So none of it is
  load-bearing here.
- The genuinely **new object** is the distance distribution
  `A_k = #{(d,d')∈[2,n-1]² : |M_d △ M_d'| = k}` of this *specific* row set, and
  hence `F_n(z)=Σ_{d,d'} z^{|M_d△M_d'|}`. No source computes it; it is a
  pure n-local combinatorial count (popcount statistics of `d,d',d∧d'`), not a
  citation target. In particular `A_2` (the distance-2 pairs) reads the
  dyadic-lag autocorrelation of the switch-sign `u_j = s_j s_{j+1}` — a
  second-order object, distinct from single-point switch density.

## Conclusion for the run

No download is warranted: the formula is elementary (standard Boolean-lattice
fact + a reflection bijection), and the only open part is a computation
(the distance distribution `A_k`), not a missing source. This closes the
approach's research-pricing step and keeps directive 7's gate: the run's one
named request (`walsh-spectral-subset-b904`) remains open and is unrelated to
this pricing.

## Verification status

Script `code/librarian/verify_downset_intersection.py` checks all three formulas
by brute submask enumeration over all ordered pairs `(d,d')` with
`d,d'∈[2,n-1]`, `n=8..256`, plus a negative control (random same-size point sets
must fail the formula). The hand-check above establishes the identity
already; the script is coder/tool_builder's to run as the independent route.
