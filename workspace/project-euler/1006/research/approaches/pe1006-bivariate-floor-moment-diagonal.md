# Bivariate floor-moment diagonal (intercept as second coordinate)

```approach
slug: pe1006-bivariate-floor-moment-diagonal
idea: Couple the two boundary offsets in one universal-Euclidean node instead of k+1 separate intercepts, writing the double floor-product sum in the diagonal coordinate h=j-m.
mechanism: Squaring the telescoped mechanical value gives a double sum over (m,j,l); the hope was that h=j-m turns both floors into affine functions of one Euclidean path index, closed by LOJ138's bivariate moment node and Babichev-Shpakova Lemma 13.
status: refuted
killed-by: Two independent obstructions, both source/check backed. (1) Verified formulation (B) has g(t)=floor(t·p/q)-[t=0] depending only on l-m (Toeplitz in (l,m)), so v_m=Σ_l w_l g(l-m) with decimal weight w_l=10^(k-1-l) depending on the ABSOLUTE l; under h=l-m the weight factorises 10^(k-1-h)·10^(-m), so the m-sum keeps a geometric weight 10^(-2m) and the truncation l∈[0,k] becomes h∈[-m,k-m]: the diagonal and the window boundary stay coupled, not independent coordinates. (2) The truncated correlation C_k(j,l)=Σ_{m=0}^k g(j-m)g(l-m) is non-Toeplitz at general k (mechanically checked: pe1006-pair-correlation-boundary; Toeplitz only at k=F_n-1, claim dir1-domain-autocorrelation). Babichev-Shpakova Lemma 13 closes ONE staircase with two per-intercept endpoint markers (u,v), and their algorithm pays L² marker-slot operators (Lemma 14), i.e. per-intercept work = the O(k) this route exists to remove.
first-step: Use code/investigate_bivariate_diagonal.py as the exact bounded oracle to test any proposed state map before attempting composition; it falsifies any h-only affine state via the -[t=m] boundary term.
```

## Restatement and governing theory

The target is `Psi(k)=Σ_{m=0}^k v_m²`, where, for a Fibonacci rational convergent `a=p/q` with `q>k`,

`G_m(t)=floor((t-m)a)-[t=m]`,

`v_m=G_m(k)-10^(k-1)G_m(0)+9 Σ_{j=1}^{k-1}10^(k-1-j)G_m(j)`.

The adopted idea was to aggregate the resulting double floor-product sum over `(m,j,l)` by the diagonal `h=j-m`, using a fixed-dimensional universal-Euclidean moment state.

The relevant named theory is Euclidean reciprocity for finite floor staircases and polynomial moment monoids. LOJ138 closes moments of one affine floor sequence. Babichev–Shpakova Lemma 13 closes six lattice moments of one finite staircase under a fixed quotient trace, with a degree-4 bivariate boundary correction. Their Definition 3 retains two endpoint-marker quotient words `(U_i),(V_i)` in addition to the coefficient quotient word.

## The exact obstruction

Verified formulation (B) of `code/mech/mech_psi.py` shows `g` depends only on `l-m`: a single sequence `g(t)=floor(t·p/q)-[t=0]`, `t=-k..k`, evaluated at diagonals. So `v_m=Σ_l w_l g(l-m)` with `w_l=10^(k-1-l)`, and

`Psi(k)=Σ_{j,l} w_j w_l C_k(j,l)`,  `C_k(j,l):=Σ_{m=0}^k g(j-m)g(l-m)`.

This is a **double-diagonal truncation correlation**. Two facts close the route:

1. `C_k(j,l)` would need to be Toeplitz in `(j,l)` — a function of `j-l` only — for a fixed-dimensional diagonal state to exist. The run's own mechanically-checked refutation (`pe1006-pair-correlation-boundary`) shows the residual `R(j,l)=C_k(j,l)-T(j-l)` is NOT zero at general k; Toeplitz holds only at `k=F_n-1` (claim `dir1-domain-autocorrelation`).
2. Babichev–Shpakova Lemma 13 is a *one-staircase* closure: six lattice moments plus a degree-4 bivariate correction in **two** endpoint markers `(u,v)` whose quotient words vary with the intercept. PE1006 needs one operator covering all `k+1` intercepts at once; the source's own design enumerates marker *slots* (`L²` cell operators, Lemma 14) — per-marker work, which here is the very O(k) the route exists to remove.

Moreover the decimal weight couples the diagonal to the window boundary: under `h=l-m`, `w_l=10^(k-1-h)·10^(-m)`, so the m-sum retains a geometric weight `10^(-2m)` and the range `l∈[0,k]` becomes `h∈[-m,k-m]`. The two coordinates `(h,m)` are not separable, so "bivariate moment with the diagonal as second coordinate" is not a fixed-dimensional state.

## Falsification test

`code/investigate_bivariate_diagonal.py` is an exact bounded oracle: it builds the rational left-limit matrix `G_m(t)=floor((t-m)p/q)-[t=m]` and, for each fixed `h=j-m`, counts distinct local data `(G_m(j),G_m(j+1),[j=m])`. Any proposed `h`-only affine state is falsified as soon as a diagonal has more than one datum — which the boundary term `-[t=m]` guarantees for every k≥1 on the diagonal crossing zero. The script is deliberately bounded/exponential in the oracle dimension and is not a full-size method.

A separate previously executed oracle (`code/refute/run_bivariate_diagonal_oracle.py`) found the smallest aggregate-moment collision at `k=1`: prefixes `01` and `10` share `(count,sum,sumsq)` but give different boundary corrections after appending a symbol. That kills aggregate degree-2 moments without boundary state; it does not prove every richer fixed-dimensional state impossible.

The ordinary mechanical oracle `code/mech/mech_psi.py` is the semantic check: it reproduces the factor oracle for `k≤50`, and its two exact formulations agree. That validates the target expression, not the missing closure.

## Final status

**Refuted in its specified form**; it must not be used to compute `Psi(10^18)`. The precise missing lemma for any revival is a uniform finite-state encoding of all `k+1` endpoint-marker traces of this Fibonacci orbit under a geometric weight `10^(-2m)` on the coupled range `h∈[-m,k-m]`. No such statement is in any source on disk; it is the open G4 gap, not a closure this route currently has.
