# iid-OR entropy barrier — exact symbolic computation

**Script:** `code/out/iid_barrier_exact.py` (sympy, no floats).
**Method:** exact symbolic algebra in `ℚ(√5)`. Every constant is a sympy
`Rational`/`sqrt` expression; log identities are resolved by entropy symmetry
`h(z) = h(1−z)` and the injection of `h` on each side of `1/2`. The "R ≥ 1 on
[0,p0]" direction is checked on an **exact-rational grid** at 40-digit
precision (a numerical check, not a standalone proof); the crossover location
`p0` is proved exactly.

## Setup

X, Y iid on `{0,1}^2`; each coordinate product-Bernoulli(p): `Pr[coord=1]=p`,
independent across coordinates and copies. Union coordinate `Z_j = X_j OR Y_j`
is Bernoulli with `Pr[Z_j = 1] = 2p − p²`. By independence,

```
H(X)      = 2·h(p)
H(X or Y) = 2·h(2p − p²)
ratio R(p) = h(2p−p²)/h(p)
```

with `h(a) = −a·log₂a − (1−a)·log₂(1−a)` the binary entropy. All conclusions
are log-base independent (nats used in sympy).

## 1. Exact solve of H(X or Y) = H(X)

`h(a) = h(b) ⇔ a = b or a = 1−b` (h symmetric about 1/2, injective on each
side). Two exact polynomial branches:

- **nontrivial** `2p−p² = 1−p`  ⟺  `p² − 3p + 1 = 0`:  sympy's `solve` returns
  `p = 3/2 ∓ √5/2`; the root in `[0,1]` is sympy-verified equal to
  `(3−√5)/2`, and `p0² − 3p0 + 1 = 0` is verified **exactly** (sympy
  `simplify(...) == 0`).
- **trivial** `2p−p² = p` ⟺ `p(p−1)=0`: sympy returns `p ∈ {0, 1}`.

Hence the only `p ∈ [0,1]` with `H(X or Y) = H(X)` are `0, (3−√5)/2, 1`.

## 2. Complement density at p0

With `φ = (1+√5)/2` and `p0 = (3−√5)/2`:

```
2p0 − p0² = 1 − p0 = 1/φ = (√5−1)/2          (sympy: all three simplify to equal)
1 − 1/φ   = 1/φ²  = (3−√5)/2 = p0
```

Entropy symmetry then gives `h(1/φ) = h(1 − 1/φ) = h(1/φ²) = h(p0)`, so
`H(X or Y) = 2h(2p0−p0²) = 2h(p0) = H(X)` **exactly**. sympy's `simplify` of
`h(2p0−p0²) − h(p0)` returns `0`; the ratio `R(p0)` is exactly `1`.

## 3. Barrier statement

At `p0` the iid coupling gives **no entropy gain**: `H(X or Y) = H(X)` exactly,
so `R(p0) = H(A or B)/H(A) = 1`. In the union-closed argument this ratio is
combined with `H(A or B) ≤ log |F| = H(A)`; equality at `p0` means the iid-OR
inequality certifies **no element density above `(3−√5)/2 ≈ 0.38197`**. The
script verifies `R(p) ≥ 1` on `[0, p0]` (min of `h(2p−p²) − h(p)` over 763
exact rational grid points in `(0, p0]` is `+5.0e−4`, always nonnegative; the
first equality `R=1` off `p=0,1` occurs exactly at `p0` by the branch solve).
So for every `c > (3−√5)/2` there is a product-Bernoulli density `p < 1/2`
whose iid coupling has ratio below `c`, and the argument stops — the barrier.

This makes the `(3−√5)/2` bound a **structural cap on the iid method**, matching
the sourced literature (Alweiss–Huang–Sellke, Pbody optimization: the value of
`min E[H(X∪Y)]/E[H(X)]` over the relevant distributions; Sawin's dependent
coupling escapes it). It is a barrier to the *iid-twin* form, **not** to the
conjecture.

```claim
id: iid-barrier-exact
statement: For X,Y iid product-Bernoulli(p) on {0,1}^2, the iid-OR entropy ratio R(p)=h(2p-p^2)/h(p) satisfies: (a) R(p)>=1 on [0,p0] with the only solutions of R(p)=1 being p in {0,p0,1}; (b) at p0=(3-sqrt5)/2, 2p0-p0^2 = 1-p0 = 1/phi (phi=(1+sqrt5)/2), so H(X or Y)=H(X) exactly and R(p0)=1, i.e. the iid coupling yields no entropy gain at the extremal product-Bernoulli(p0). Consequently the iid-OR entropy method certifies no element density above (3-sqrt5)/2.
hypotheses: X,Y iid on {0,1}^2, each coordinate product-Bernoulli(p), coordinates and copies independent; h binary entropy; p in [0,1].
holds-here: yes
status: checked
bearing: Proves exactly where the iid-OR equality H(XorY)=H(X) occurs (p0=(3-sqrt5)/2 with union coordinate at complementary density 1/phi) and that R>=1 on [0,p0] with first crossover R=1 at p0: the iid argument cannot certify any element density above (3-sqrt5)/2. The exact solve and complement-density identities are proved symbolically in QQ(sqrt5); the R>=1-on-interval claim is verified on an exact-rational grid at 40 digits (numerical, not standalone proof).
anchor: code/out/iid_barrier_exact.py
```

## What would falsify it

- An input `p ∈ [0, p0]` with `R(p) < 1`, i.e. `h(2p−p²) < h(p)`: the grid
  (763 exact-rational points at 40 digits) found none, and the branch analysis
  locates all `R = 1` points at `{0, p0, 1}`; a counterexample would have to be
  an interior point the grid missed with sign actually negative, or a missed
  solution of the polynomial branches.
- A density `p0' < 1/2` with `R(p0') = 1` strictly below `(3−√5)/2`, which
  would contradict the exact branch solve of `h(2p−p²) = h(p)`.
- Any claim that this *certifies* a constant above `(3−√5)/2` — the exact
  equality `R(p0) = 1` rules that out for the iid-OR coupling.

**Scope note:** this is only the one-variable entropy-ratio barrier for the iid
coupling. No union-closed-set result is claimed; the conjecture is not touched.
A dependent-coupling refinement (Sawin/Yu/Cambie, `~0.38234`) escapes this
iid barrier.
