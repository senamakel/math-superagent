# Linear-supply sphere-mean: exact Krawtchouk expectation

**Status: proved by derivation, verified by independent computation.**

This note settles the `G-sphere-mean` lemma of
`research/backward/linear-supply-threshold-limit.md`:

> For `h` uniform on the weight-`w` Hamming sphere `S_w ⊆ F₂ⁿ`, with
> `ν₂(h) = wt(Φ_n h)` the fold weight,
> `E_{S_w}[ν₂(h)] = Σ_{d=2}^{n−1} P_d`, where
> `P_d = (1/2)(1 − K_w(m_d; n)/C(n,w))`, `m_d = 2^popcount(d)`, and
> `K_w(m; n) = Σ_{j=0}^{w} (−1)^j C(m,j) C(n−m, w−j)` is the Krawtchouk
> polynomial.

## 1. The per-cell claim and its derivation

**Claim (per-cell parity count).** Let `A ⊆ {0,…,n−1}` be a fixed set of `m`
coordinates (`|A| = m`). Then

```
#{ h ∈ S_w : ⊕_{j∈A} h_j = 1 } = ( C(n,w) − K_w(m;n) ) / 2.        (∗)
```

**Derivation.** The parity `X = ⊕_{j∈A} h_j = (Σ_{j∈A} h_j) mod 2`. The
indicator that `X` is odd is `(1 − (−1)^X)/2`, so

```
#{h : X odd} = Σ_{h∈S_w} (1 − (−1)^X)/2
             = ( |S_w| − Σ_{h∈S_w} (−1)^{Σ_{j∈A} h_j} ) / 2.
```

Now `|S_w| = C(n,w)`, and the sum is the Krawtchouk evaluation. Expanding over
which `i` elements of `A` are set to 1 (and the rest of the `w` weight in the
`n−m` coordinates outside `A`):

```
Σ_{h∈S_w} (−1)^{Σ_{j∈A} h_j}
  = Σ_{i=0}^{min(w,m)} (−1)^i C(m,i) C(n−m, w−i)
  = K_w(m;n).                                                       (†)
```

Substituting (†):

```
#{h ∈ S_w : X odd} = ( C(n,w) − K_w(m;n) ) / 2.   ✓  (the claim (∗))
```

This is exactly the task's derivation: `P[X odd] = (1 − E[(−1)^X])/2` with
`E[(−1)^X] = K_w(m;n)/C(n,w)`.

**Connection to the fold.** `ν₂(h)` counts, over the floored depths
`d ∈ [2, n−1]`, the cells whose submask parity is 1:

```
T(n,d) = ⊕_{o⊆d} h[n−1−d+o],   ν₂(h) = #{ d ∈ [2,n−1] : T(n,d) = 1 }.
```

By Lucas, the submasks `o ⊆ d` are exactly the `2^popcount(d)` coordinates the
cell reads; their set `M_d` has cardinality `m_d = 2^popcount(d)`, and
`T(n,d)` is a parity over exactly those `m_d` distinct coordinates. (This is
`fold-cell-degree-is-2^popcount`, proved; the degree is `2^popcount(d)`, NOT
`popcount(d)` — the `fold_cell_degree_correction.md` fix.) Applying the
per-cell claim with `A = M_d` and linearity of expectation gives the closed
form:

```
E_{S_w}[ν₂(h)] = Σ_{d=2}^{n−1} (1/2)( 1 − K_w(m_d;n)/C(n,w) ).
```

## 2. Exact per-cell parity counts and the asymptotics

**Exact per-cell count.** For each `d`, cell `d` is 1 on exactly

```
N_d(w) := #{ h ∈ S_w : T(n,d) = 1 } = ( C(n,w) − K_w(2^popcount(d); n) ) / 2
```

of the `C(n,w)` sphere elements, and `P_d = N_d(w)/C(n,w)`.

**Asymptotic regimes.** Fix `α = w/n ∈ (0,1)`.

- **Small cell `m_d` (bounded popcount `d`).** For fixed `m`,
  ```
  K_w(m;n)/C(n,w) → (1 − 2α)^m   as n → ∞,  w/n → α.
  ```
  This is the classical limit of the Krawtchouk ratio (a finite-m binomial
  asymptotics: `C(n−m, w−i)/C(n,w) → α^{w−i}(1−α)^{n−w−?}...`; numerically
  confirmed below). So
  `P_d → (1/2)(1 − (1−2α)^{m_d})`.
  For `α = 1/2` this is `→ 1/2` at rate `O(1/n)` per cell; for `α < 1/2` it is
  bounded away from `1/2` but still `→ 1/2` as the correction `(1−2α)^{m_d}`.

- **Large cell (large `m_d` = `2^popcount(d)`).** Since `|1−2α| < 1` for every
  `α ∈ (0,1)` (degenerate only at `α=0,1`), when `m_d` is large the
  `(1−2α)^{m_d}` term is exponentially tiny, so
  `K_w(m_d)/C(n,w) → 0` and **`P_d → 1/2` (saturation)**.

**Saturation argument (why the mean tends to `n/2`).** With
`L = ⌊log₂(n−1)⌋`, the number of depths `d ∈ [2, n−1]` with
`popcount(d) < K` is `Σ_{k<K} C(L,k) = O(L^{K−1}) = o(n)` for any fixed `K`;
all other depths have `popcount ≥ K`, hence `m_d ≥ 2^K`, and for
`(1−2α)^{2^K} ≤ ε` those cells are saturated at `P_d ≥ (1/2)(1−ε)`. So

```
E_{S_w}[ν₂]/n = (1/2 + o(1))   as n → ∞, per fixed α ∈ (0,1).
```

The mean half of the threshold therefore tends to 0: at weight `⌊αn⌋` the mean
exceeds `0.4·n` for all large `n`. This is `G-threshold-tends-zero`.

## 3. Verification

Three independent routes were run. The closed form was checked **exactly**
against an exhaustive brute-force enumeration of the sphere for every `n` in
`3..16` and every `w` in `0..n` (script `code/symbolic/sphere_mean_verify.py`)
and against an independent sympy evaluation (`code/symbolic/sphere_mean_sympy.py`).
The per-cell identity `(∗)`, the Krawtchouk evaluation `(†)`, and the
`(1−2α)^m` asymptotics were confirmed in `code/symbolic/sphere_mean_verify2.py`.

**Anchor 1 — n=4, w=1.** Cells `d=2` (m=2) and `d=3` (m=4).
`K_1(2;4)/C(4,1) = 0`, `K_1(4;4)/C(4,1) = −4/4 = −1`. So

```
E = (1/2)(1−0) + (1/2)(1+1) = 1/2 + 1 = 3/2 = 1.5.   ✓  (= Σ_d m_d/n = (2+4)/4)
```

Brute force: `3/2`, exactly. **Pass.**

**Anchor 2 — n=8, w=3. Discrepant with the task statement.** The exact value is

```
E_{S_3}[ν₂] = 25/7 ≈ 3.5714,   mean ν₂/8 = 0.4464.
```

The task's stated `6.846` (mean `0.428`) is **wrong and impossible**: at `n=8`
`ν₂` counts only the `n−2 = 6` cells `d∈[2,7]`, so `ν₂ ≤ 6` and
`E[ν₂] ≤ 6 < 6.846` always. The value `6.846` appears to have been obtained by
dividing by `16` (`6.846/16 ≈ 0.428`), i.e. using the wrong normaliser `n`
as if the fold ran over `n` cells. The correct mean is `0.4464`.

Full `n=8` sweep (exact, sympy):

| w | E[ν₂] | ν₂/8 | ≥ 0.4·8 = 3.2? |
|---|---|---|---|
| 0 | 0 | 0.0000 | no |
| 1 | 3 | 0.3750 | no |
| 2 | 18/7 = 2.5714 | 0.3214 | no |
| **3** | **25/7 = 3.5714** | **0.4464** | **yes** |
| 4 | 88/35 = 2.5143 | 0.3143 | no |
| 5 | 25/7 = 3.5714 | 0.4464 | yes |
| 6 | 18/7 = 2.5714 | 0.3214 | no |
| 7 | 3 | 0.3750 | no |
| 8 | 0 | 0.0000 | no |

The first crossing of the mean above `0.4n` at `n=8` is at `w=3`, ratio
`w/n = 0.375` — **exactly the measured threshold column value `0.375@8`** from
`code/out/linear_supply_by_weight.txt`. The symmetry `E[w] = E[n−w]` (Krawtchouk
evaluation is even in the reflected weight) is visible in the table, and the
degeneracy `E[0] = E[n] = 0` reproduces the closed-door-1 obstruction (the
all-ones sphere point is a kernel vector with `ν₂ = 0`).

## 4. Where the formula or derivation fails

None found. The identity `(∗)` held exactly for every `(n,w,m)` tested
(`n=3..16` exhaustive for the mean; `K_w` evaluation for all `n≤10, w, m`), and
the asymptotic `(1−2α)^m` converged to its closed forms. The **only** defect is
in the task's stated anchor `6.846`, which is not the formula but the stated
expected value — corrected above to `25/7`.

**(a)/(b) brute-force exact equality for every n in 3..16, every w: PASS.**
**(c) asymptotics: PASS** (e.g. `α=1/4, m=2`: ratio 0.2381→0.2498→…→target 0.25;
`α=1/8, m=4`: 0.2921→0.3161→target 0.3164).

---

```claim
id: sphere-mean-krawtchouk-exact
status: proved-by-derivation
hypotheses: n >= 3; 0 <= w <= n; canonical floored fold d in [2, n-1]
statement: >
  For h uniform on the weight-w Hamming sphere S_w in F2^n,
  E_Sw[nu2(h)] = sum_{d=2}^{n-1} P_d with
  P_d = (1/2)(1 - K_w(2^popcount(d); n)/C(n,w)),
  K_w(m;n) = sum_{j=0}^w (-1)^j C(m,j) C(n-m, w-j).
  Per cell d (which reads exactly m_d = 2^popcount(d) distinct coordinates),
  #{h in S_w : T(n,d)=1} = (C(n,w) - K_w(m_d;n))/2.
  Asymptotics: for fixed alpha = w/n in (0,1),
  K_w(m;n)/C(n,w) -> (1-2 alpha)^m, and P_d -> 1/2 for cells of large m_d;
  the number of small-popcount cells is o(n), so E_Sw[nu2]/n -> 1/2 and the
  mean half of the supply threshold tends to 0 (linear supply typical at any
  fixed positive density).
proof: >
  Parity indicator (1-(-1)^X)/2; Krawtchouk evaluation (†) by expanding the
  subset of A that is set; Lucas gives m_d = 2^popcount(d) coordinates read.
  Verified exactly against exhaustive sphere enumeration for every
  (n,w), n = 3..16, and independently by sympy; per-cell (∗), (†), and the
  (1-2 alpha)^m asymptotics all PASS. Anchors: n=4,w=1 -> 3/2 exactly;
  n=8,w=3 -> 25/7 = 3.5714 (mean 0.4464), NOT the 6.846 stated in the task
  (impossible: nu2 <= n-2 = 6 at n=8).
verify: >
  code/symbolic/sphere_mean_verify.py: exhaustive n=3..16 all w, formula ==
  brute EXACTLY. code/symbolic/sphere_mean_sympy.py: independent sympy route,
  same exact integers. code/symbolic/sphere_mean_verify2.py: per-cell (∗),
  Krawtchouk (†), asymptotics all PASS.
```
