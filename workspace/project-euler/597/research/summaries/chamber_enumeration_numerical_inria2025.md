# Dussault–Gilbert–Plaquevent-Jourdain: Primal and dual chamber enumeration of affine hyperplane arrangements

Dussault, Gilbert, Plaquevent-Jourdain, Inria/Sherbrooke research report hal-05002249 (2025), 40 pp. [[chamber_enumeration_numerical_inria2025.full]]

## What it establishes

State-of-the-art **chamber enumeration** for general real affine hyperplane arrangements A(V,τ) = {x ∈ R^n : v_i^T x = τ_i, i=1..p}, i.e. listing every chamber (connected component of the complement) or, equivalently, the feasible sign-vector set S(V,τ) = {s ∈ {±1}^p : s·(V^T x − τ) > 0 for some x}.

- **Primal S-tree** (Rada–Černý): a tree whose leaves are the chambers, built by adding hyperplanes one at a time, using linear-optimization feasibility tests; several cost-cutting heuristics (A: start from a full-rank independent subset; B: detect two children near a hyperplane without an LOP; C: choose hyperplane order to minimize nodes).
- **Dual approach via stem vectors**: a sign vector s ∈ S(V,τ)^c (infeasible) is characterized iff it restricts to a **stem vector** on some subset J ⊆ [1:p] (Prop 3.9, covering test). Stem vectors are built from the matroid **circuits** of V: each circuit J gives either one asymmetric or two symmetric stem vectors (Rem 3.6(3)); number of circuits is between (p choose r+1) and 2(p choose r+1), "can be exponential in p" (Rem 3.6(6)). Motzkin's theorem of the alternative is the engine.
- **Compact forms**: because S(V,0) ⊆ S(V,τ) ⊆ S([V;τ^T],0) = S(V,τ) ∪ S(V,−τ), and Ss(V,τ)=S(V,0), only the positive subtree plus the asymmetric part of the negative needs computing (Prop 3.10, Prop 6.1); this saves up to ~2× (mean improvement 1.51, median 1.50 on the compact primal-dual).
- **Best solver PDC** (primal+dual+compact) achieves speedup 1.72–22.87 (mean 9.10) over Rada–Černý across 42 tested arrangements.
- **Bounded chambers**: when rank(V)=n and the arrangement is in linear general position, the bounded chambers are exactly the asymmetric sign vectors (Prop 3.15); count (p−1 choose n) in affine general position (Buck).
- **Cardinality bounds**: |S(V,0)| ≤ 2·Σ_{i<r}(p−1 choose i) (Schläfli), |S(V,τ)| ≤ Σ_{i≤r}(p choose i), attained in general position ((3.21),(3.22)).

## Hypotheses and whether they hold here

The algorithms apply to any real affine arrangement, so the torpids arrangement (hyperplanes = bump event equalities and finish histories, all affine-linear in the simplex) is in scope. Two qualifications for our problem:

1. **Cost is proportional to the number of chambers**, and every method here lists chambers. The run's n=5 torpids arrangement already has ~13,750 chambers; n=12–13 has an astronomically larger (super-exponential) count. **Output-polynomiality means each chamber is cheap, not that there are few.** The 42 benchmarks top out at |S|=1.1e7 chambers (crossplt-13) and already cost 2,024 s (RC) — and crossplt has only p=24 hyperplanes in R^13 with heavy symmetry. Our arrangement's cell count is the wall.
2. The dual/stem-vector viewpoint is algebraically elegant but the **number of circuits (stem vectors) is itself exponential in p** (Rem 3.6(6)), so the dual route does not dodge the explosion; it trades LOPs for circuit computation.

## What it lets this run compute / rule out

Confirms, with a 2025 authoritative source, that (i) chamber enumeration of a real arrangement is a solved, output-polynomial task and (ii) the **binding constraint is the number of chambers, which no technique here removes**. It is precisely the general-position bound |S(V,τ)| ≤ Σ_{i≤n} (p choose i) with the torpids p ~ O(n²) that is the combinatorial ceiling the run already hit at n=5 (~13,750 cells). This **rules in** the run's conclusion that the exact route needs an arrangement-free reduction, and **rules out** "use a better chamber enumerator" as an n=13 strategy. It also corroborates the run's L-independence of the parity-cell count: the *set* S(V,τ) of chambers is a purely combinatorial object (fixed by V,τ combinatorics across the physical L range).

## Does not settle

No coefficient or value of p(n,L); no reduction of the parity sum to a charpoly; nothing that scales with n rather than with the arrangement. If a future method needs to actually list cells for n ≤ 5 (the largest the run can reach), the S-tree/PDC techniques here are the right way to do it faster than the naive vertex solver — that is the genuine use of this source. A per-cell parity weight (the run has it) plus a fast enumerator = the existing exact small-n route, not an n=13 solver.

```claim
id: chamber-enumeration-output-polynomial-bounded-by-count
statement: Chamber enumeration of a real affine hyperplane arrangement can be done output-polynomial (S-tree) and in compact primal/dual forms (stem vectors from matroid circuits); the cost is the total number of chambers, which for the torpids arrangement is super-exponential in n (p~O(n^2) hyperplanes).
hypotheses: proper real affine arrangement; chamber count is the binding resource
holds-here: yes
status: proved
bearing: rules OUT "use a better chamber enumerator" as an n=13 strategy (the cell count is the wall at n=5 ~13,750); rules IN an arrangement-free reduction as the only exact route; the algorithms are usable to accelerate the reachable n<=5 exact cell enumeration
anchor: research/sources/chamber_enumeration_numerical_inria2025.full.md
answers: whether-a-chamber-enumerator-reaches-n-13
```
