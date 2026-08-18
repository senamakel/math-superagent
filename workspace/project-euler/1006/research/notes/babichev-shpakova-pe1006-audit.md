# Babichev–Shpakova audit for PE1006

## Question
Does Babichev–Shpakova, *Counting Lattice Rectangles in the Square Grid in Near-Linear Time* (arXiv:2607.17961v1, https://arxiv.org/html/2607.17961v1), prove the fixed-dimensional joint-intercept aggregation needed for PE1006?

## Answer
No. It proves closure for the moments of **one normalized finite affine staircase**, and an algorithm for a different lattice-rectangle count. It does not prove aggregation over the k+1 mechanical-word intercepts of PE1006, nor a polylogarithmic evaluator for Ψ(k).

## Precise source hypotheses and result
For integers `q>0`, `0<b<a`, and `0≤β<a`, the source defines
`f(t)=floor((b t+β)/a)` for `0≤t<q`, and its lattice staircase `Λ_f={(t,s):0≤t<q, 1≤s≤f(t)}`. It transports six lattice moments
`L_ij=Σ_{0≤t<q}Σ_{1≤s≤f(t)} t^i s^j` for `(i,j)=(0,0),(1,0),(2,0),(0,1),(1,1),(0,2)`; these linearly recover six floor moments including first, second and third powers. The reciprocal step introduces endpoint markers `u=a−β−1` and `v`, and Definition 3 retains the coefficient quotient word plus two marker quotient words `(U_i)` and `(V_i)`.

Lemma 13 states: for each **fixed coefficient prefix and fixed marker rectangle**, terminal affine state and root six-moment vector are an affine/linear transform of terminal data plus a bivariate polynomial boundary correction of total degree ≤4. Composition/application costs O(1). The main theorem is an O(n log n) algorithm for the lattice-rectangle quantity F(n), not an O(log n) algorithm in a queried n.

## Why this is not PE1006 G4
PE1006 needs, for `k`-dependent intercepts `m=0,…,k`, an identity/evaluator for `Σ_m v_m²`, equivalently the joint products of the floor traces `G_m(j)G_m(l)`, with a state dimension and boundary data independent of k. Each intercept changes the finite staircase/endpoints and hence can change the marker trace. Babichev–Shpakova explicitly says a shared operator is indexed by the coefficient word **and both marker words**. Lemma 13 therefore gives conditional closure after a marker rectangle is fixed; it does not sum over a growing family of marker traces, identify their distribution for the Fibonacci orbit, or show that diagonalizing by `j−m` absorbs them.

Also, its weights are polynomial in the staircase coordinates (`t^i s^j`), not the geometric decimal weights `10^i` in PE1006. Thus even its one-staircase moment vector is not the required geometric-weighted joint intercept state without an additional theorem.

## Evidence/check status
This conclusion is source-backed by Sections 3 and 5.1, Definition 3, Lemma 13, and Theorem 19 of the downloaded full text, and agrees with `research/approaches/pe1006-bivariate-floor-moment-diagonal.md` and `research/notes/reference-library-report-current.md`. It is not a proof that no richer fixed-dimensional PE1006 state exists; it establishes only that the cited source does not supply it. The workspace's bounded oracle/refutation already finds marker/boundary-summary collisions, so replacing marker data by aggregate degree-2 moments is unsound.
