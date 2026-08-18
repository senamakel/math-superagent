# Mechanical/Ostrowski audit: concrete correction

## Restatement
For `S_0=0`, `S_1=01`, `S_n=S_{n-1}S_{n-2}`, let `Psi(k)` be the sum of squares of the decimal values of the `k+1` distinct length-`k` factors, modulo `M=101001001`.

## Governing theory
The infinite word is characteristic Sturmian of slope `alpha=1/phi^2`. The mechanical construction replaces the irrational slope by a convergent `p/q`, cuts the circle at `{-mp/q:0<=m<=k}`, and obtains one factor per arc. The decimal value on each arc is a geometrically weighted affine combination of floor functions. The universal-Euclidean monoid exactly evaluates moments of *one* sequence `floor((pt+q)/r)` in logarithmic Euclidean depth.

## Executed oracle check
`code/mech/independent_eval.py` was run. It compares the independently implemented `mech_psi` result with `code/brute.py` for every `k=1..20`; all 20 residues agree, including `Psi(3)=20302` and `Psi(10)=10699667`.

## Correction
The current `code/solution.py` does not contain an O(log) evaluation. Its `psi_mechanical` explicitly loops over `k+1` arcs and, within each arc, over `k` weighted floor terms: this is O(k^2) arithmetic (and exact fractions make the bit complexity larger). `ueuclid` cannot be substituted for the outer loop: its input has one affine floor sequence and returns its first/second geometric moments, whereas the mechanical sum requires the second moment of `k+1` different intercepts `x_m` (or equivalently a two-dimensional sum over intercept and digit position). No identity collapsing that intercept sum to a single affine floor sequence is present or verified.

This is not merely a performance concern: reporting a target residue from the current reduction would be unsupported. The old `solution.py` self-report “intercept aggregation has been established” is false/contradictory to its own docstring and must be removed or replaced by an explicit `NOT ESTABLISHED` status.

## Attack on the correction
It would be wrong if either (a) the outer intercept sum were secretly represented by one universal-Euclidean call, or (b) the fallback were already O(log). Inspection and execution disprove (b) directly. For (a), `ueuclid`'s contract has only one affine floor parameter and fixed moments; the mechanical formula has `k+1` distinct intercepts, and no map/identity in the repository eliminates that parameter. The tested small values establish correctness of the mechanical oracle, not an unproved collapse.

## Consequence
A genuine independent O(log) route still needs a new structural theorem, such as a verified constant-state Fibonacci-block monoid for the contiguous-window prefix sum. Until that theorem is derived and executed against the anchors `Psi(10^4)=34432237` and `Psi(10^6)=20938836`, the full-size answer is unknown.
