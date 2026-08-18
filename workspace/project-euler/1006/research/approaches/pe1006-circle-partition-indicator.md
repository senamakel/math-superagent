# Circle-partition interval-indicator route: exact reduction and obstruction

```approach
slug: pe1006-circle-partition-indicator
idea: Express each digit as an interval indicator on R/Z, sort the k+1 orbit cut points, and aggregate the squared decimal observable through interval-intersection counts.
status: refuted
```

## Governing theory

The relevant theory is mechanical/Sturmian coding of an irrational rotation, together with exact interval discrepancy (equivalently lattice-point/floor-sum counting). For slope `alpha=1/phi^2`, the `k+1` factors correspond to the `k+1` arcs cut by `{ -m alpha : 0<=m<=k }`. A digit is the indicator of a fixed interval (up to endpoint convention). The three-gap theorem controls the *arc lengths* of the sorted cut points, but does not identify all weighted pair intersections with a bounded number of types.

The literature checked: Allouche–Glen, *Extremal properties of (epi)Sturmian sequences and distribution modulo 1*, https://doi.org/10.4171/lem/56-3-5, establishes the mechanical rotation coding and balance; Alessandri–Berthé, *Three distance theorems and combinatorics on words*, https://doi.org/10.5169/seals-63900, establishes the rotation/word and factor-frequency setting. Neither gives the requested finite-dimensional exact aggregation. Berstel–Vuillon, *Coding rotations on intervals*, https://doi.org/10.48550/arxiv.math/0106217, gives an automaton for coding interval partitions, not a constant-size weighted-square evaluator.

## Exact formula

Let `d_j(x)` be the j-th binary digit and `w_j=10^(k-1-j)`. If `I_j` denotes the interval on the circle for which `d_j=1`, then

`v(x)=sum_j w_j 1_{I_j}(x)` and therefore

`Psi(k)=sum_{m=0}^k sum_{j,l=0}^{k-1} w_j w_l 1_{I_j}(x_m)1_{I_l}(x_m)`.

Thus it is exactly a finite sum of interval-intersection counts

`C_k(j,l)=#{m: x_m in I_j intersect I_l}`.

For a rational convergent `alpha=p/q`, every such count is a floor/difference-of-floor count after lifting the interval endpoints. This proves the requested *finite floor-sum representation* in the literal sense, but it has `k^2` pair terms (or `k` correlation rows), not a fixed number independent of `k`.

## Concrete obstruction

The interval indicators are translated copies: `I_j = I_0 - j alpha`. Hence `C_k(j,l)` is a truncated orbit correlation depending on both the shift `l-j` and the boundary placement. Only on the special domain `k=F_n-1` does the cyclic-window symmetry remove the boundary dependence and make the correlation Toeplitz. At general `k`, the boundary survives and is exactly the previously verified joint-intercept obstruction. Three-gap structure limits the number of *gap lengths* to at most three; it does not limit the number of weighted correlation rows or their endpoint placements.

The decimal weights make this decisive: after grouping by `h=l-j`, the factor `10^{-j-l}` leaves a position-dependent boundary contribution. A bounded-variation discrepancy estimate gives an error/bound for unweighted counts, but cannot recover the exact integer weighted sum: each of the `k^2` pair coefficients is multiplied by a distinct power of 10 modulo `M` in general.

## Executable test

`code/g4_circle_partition_test.py` is a bounded oracle (`complexity_class: exponential`, `oracle_bound: 80`). It independently constructs the circle arcs, computes `Psi` directly, forms every pair correlation by interval indicators, and checks the exact expansion. It also reports the number of distinct correlation rows and distinct pair values, testing the proposed bounded-state premise. Run with:

`python3 code/g4_circle_partition_test.py`

The environment provides no command-execution tool in this research role, so the file is supplied for the tool-builder to run; execution output must be added before treating the numerical rows as evidence. The smaller existing oracles already verify the same mechanical semantics against brute force through k=50 and residues through k=400.

## Verdict

The proposed route answers the first half only: yes, sorting cut points and interval indicators gives an exact sum of floor-sum counts, but not a finite number of floor sums in the complexity-independent sense required by G4. The second half fails: three-gap/bounded-variation theory controls geometry or discrepancy, not the exact weighted square. A genuine O(log k) method would need a new theorem collapsing the family `C_k(j,l)` (including boundary data) to a fixed-dimensional renormalisation state. No such theorem was found in the sources checked.
