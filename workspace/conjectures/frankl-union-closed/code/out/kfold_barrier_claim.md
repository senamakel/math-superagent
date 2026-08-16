# The k-fold iid-OR barrier is maximised at k = 2

**Object.** For the k-fold iid-OR entropy argument, define the barrier constant
`c_k` as the unique root in `(0,1)` of

```
(1 - x)^k = x,
```

i.e. the density at which the k-fold union coordinate's entropy equals the
original, `R_k(c_k) = h(1-(1-c_k)^k)/h(c_k) = 1` (nontrivial branch of
`h(a)=h(b) ⇔ a=b or a=1-b`). Equivalently `c_k = ψ_k` (Yuster's root of
`(1-x)^k=x`) = `α_k/(1+α_k)` (Ho, `α_k` the root of `x(1+x)^{k-1}=1`) — the
`psi-alpha-tieback` claim. For `k=2`, `c_2 = (3−√5)/2 ≈ 0.381966`, the classic
iid-OR barrier.

**Claim (proved).** `c_k` is strictly decreasing in `k ≥ 2`. Hence the k=2
member `(3−√5)/2` is the *largest* of the whole family.

*Proof.* Let `g_k(x) = (1-x)^k − x`. Then `g_k'(x) = −k(1−x)^{k−1} − 1 < 0` on
`(0,1)`, so `g_k` is strictly decreasing with a unique root `c_k`. For fixed
`x ∈ (0,1)`, `(1−x)^k` strictly decreases in `k` (base `1−x ∈ (0,1)`), so
`g_{k+1}(c_k) = (1−c_k)^{k+1} − c_k < (1−c_k)^k − c_k = 0`. Since
`g_{k+1}(0) = 1 > 0` and `g_{k+1}` is continuous and strictly decreasing, its
root `c_{k+1}` lies strictly between `0` and `c_k`. ∎

**Numerical corroboration** (mpmath 50 digits): `c_2..c_60` strictly
decreasing, `c_2 = 0.38196601125 = (3−√5)/2`, `c_60 ≈ 0.049018`; the ratio
`k·c_k / ln k` at `k=60` is `0.718`, consistent with the Lambert-W / the root
of `e^{−kx} = x` asymptotic `c_k ~ W(k)/k ~ (ln k − ln ln k)/k → ln k / k`.
For k = 2,3,4,5,10,20: `R_k(c_k) = 1` exactly (to 40 digits) and the entropy
difference `h(1−(1−p)^k) − h(p)` is nonnegative on `[0,c_k]` over a 4000-point
grid (min > 0 on each), consistent with `R_k ≥ 1` below the barrier.

**Falsifier.** A `k' > 2` with `c_{k'} ≥ c_2` would contradict the proof
(impossible by the argument above); a numeric counterexample would show a bug
in the root-finder, not in the mathematics.

**Bearing.** Within the *iid* k-fold-OR entropy family, pushing the number of
copies `k` upward does not improve the frequent-element constant — the maximum
is the k=2 value `(3−√5)/2`. This is exactly why the escape to `1/2` and to the
record `≈0.38234` must come from *dependent* couplings (Sawin/Yu/Cambie/Liu),
not from using more iid copies. It corroborates `psi-alpha-tieback` and
`yuster-psi-k-approx-optimal`, and adds the provable monotonicity.

```claim
id: kfold-barrier-maximised-at-k2
statement: c_k = unique root of (1-x)^k = x in (0,1) (the k-fold iid-OR barrier,
  = Yuster's psi_k = Ho's alpha_k/(1+alpha_k)) is strictly decreasing in k>=2.
  Hence c_2 = (3-sqrt5)/2 = 0.381966 is the maximum of the family; the iid
  k-fold method does not beat (3-sqrt5)/2 for any k, matching the iid-barrier.
hypotheses: k real >= 2; c_k the unique root of (1-x)^k = x in (0,1)
holds-here: yes
status: proved (monotonicity: g_k decreasing + g_{k+1}(c_k)<0<g_{k+1}(0) forces
  c_{k+1} in (0,c_k)); numeric corroboration c_2..c_60 and R_k(c_k)=1, R_k>=1
  on [0,c_k] for k=2,3,4,5,10,20 (grid, numerical not standalone proof)
bearing: within the iid-k-fold-OR family the best constant is the k=2 value
  (3-sqrt5)/2; escaping it requires a dependent coupling (Sawin/Yu/Cambie/Liu),
  not more iid copies. Corroborates psi-alpha-tieback and yuster-psi-k.
anchor: code/out/kfold_barrier.py, code/out/kfold_barrier_ratios.py
follows-from: psi-alpha-tieback, iid-barrier-exact
```

*Commands:* `python code/out/kfold_barrier.py`, `python code/out/kfold_barrier_ratios.py`
