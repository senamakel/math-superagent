# The pinned definition of order-K pair-correlation data C_K(h)

Question this note answers: **two candidate definitions** were circulating. Is
`C_K(h)` (a) the tuple of mod-2 inner products `<h,I>` over all intervals `I`
with `|I| ≤ K`, or (b) the fixed-lag pair products `h_i h_{i+t}` — or something
else? Tool_builder's implementation must match the run's own definition, so the
answer must be quoted, not paraphrased.

## Answer: neither candidate — it is the complete joint lag counts

There are actually **three** distinct "order-K correlation" objects in the run,
and conflating them is the exact trap tool_builder must avoid.

### The pinned decision object C_K — `research/backward/collapse-via-index-multiset.md`

This file carries the authoritative "Correlation order, pinned" section (the
G-witness / G-order gaps). Verbatim:

> "Pair correlations up to lag K are the complete joint counts
> `N_ab(k) = #{ i ∈ [n−k] : h_i = a, h_{i+k} = b }` for every
> `1 ≤ k ≤ K`, `a,b ∈ {0,1}`. `C_K(h)` is that list. 'S² factors through
> K-pair correlations' := S² is constant on each `C_K`-fiber."

and the file immediately warns that a coarser reading would test a claim the
problem does not make:

> "The adjacent 2-gram count `N_ab(1)` is only the lag-1 slice — strictly
> coarser than the full pair-correlation data `C_K`; testing only it would
> refute a claim the problem does not make, so the test below uses `C_K` for
> all lags ≤ K."

So `C_K(h)` = the complete list of joint counts, four per lag k = 1..K. This is
**not** the interval inner products `<h,I>` mod 2 (a linear object), and it is
**not** merely the fixed-lag products `h_i h_{i+t}`. It is strictly finer than
the fixed-lag products: knowing all four `N_ab(k)` determines the product sum
`Σ_i h_i h_{i+k} = N_11(k)`, but knowing the product sums does **not** determine
the joint counts (the `N_00, N_01, N_10` data is lost).

### The ladder's coarser correlation vector — `research/weakened/collapse-ladder.md`

`R-smalln-collapse` uses a different, *coarser* correlation object. Verbatim:

> "verify by exhaustive enumeration that S(n,h)² is a function of the
> short-range pair-correlation vector `c_t(h) = Σ_{i=0}^{n−1−t} h_i h_{i+t}`
> (t ≤ k) for the smallest k that works, or output an explicit witness pair
> h,h' with equal c_t for all t ≤ k but different S²."

So the ladder tests constancy on `c_t`-fibers (one autocorrelation integer per
lag). Since `c_t = N_11(k)` is determined by `C_K`, every `C_K`-fiber sits
inside a `c_t`-fiber, so "constant on c-fibers" is a **stronger** statement
than "constant on C_K-fibers". The pinned, harder test for a refutation witness
is `C_K` (equal joint counts, different S²) — the harder test to refute, and
the honest one: testing only the coarser `c_t` would let a false collapse
through.

### The interval-inner-product object is a *third*, different thing

`⟨h, I⟩ = Σ_{i∈I} h_i` (mod 2) over all intervals `I` with `|I| ≤ K` also
appears in the run — but **only on the affirmative-proof side**, never as the
decision `C_K`. `research/backward/collapse-shortrange.md` writes the
affirmative assembly target as:

> "S(n,h)² = F_K( (⟨h, I⟩)_{I interval, |I| ≤ K} )"

Interval characters are **linear** functionals of h (Walsh characters on
intervals); the joint counts are quadratic correlation statistics. They are not
equivalent, and they may give different collapse orders in K. The witness test
uses the joint-count `C_K`; the interval reading belongs to a proof attempt,
not to the decision object.

## What tool_builder's implementation actually does

`code/out/g_witness_fiber.py` implements `pair_counts(h, K)` returning the flat
tuple of `N_ab(k)` for all `1 ≤ k ≤ K, a,b ∈ {0,1}` — exactly the pinned `C_K`.
Its negative control drops the k=1 counts (offsetting by 4 per lag) and must
produce a witness where the true `C_K` does not. This matches the authoritative
definition; it should **not** be changed to interval inner products or to plain
fixed-lag products.

## Decision object (for tool_builder), in one line

```
C_K(h) = ( N_ab(k) )_{1 ≤ k ≤ K, a,b ∈ {0,1}},   N_ab(k) = #{ i ∈ [0,n-k-1] : h_i = a, h_{i+k} = b }
```
"Collapse at order K" := S² is constant on each C_K-fiber. A refutation (G-
witness) is strings h,h' with C_K(h) = C_K(h') yet S²(h) ≠ S²(h'), for K = n−1
(all lags).

---

## Families already suspected to give a witness

Three hand-derived index families, all **confirmed by the captured census**
`code/out/multiset_census_n128.txt` (example `(d,d')` pairs quoted from its
per-n "top spans" and dyadic-family sections). All three are "far" sets —
span comparable to n — and each carries multiplicity `m(A) = 2` in the
multiset, so none is invisible to the index multiset.

1. **A single far pair** (family 3): `d = 2^j, d' = 2^j + 1` gives
   `M_d △ M_{d'} = { n−2−2^j, n−2 }`, a pair at distance `2^j`.
   Census, n=64: `d=..., example (2^(...))` → sets `{60,62}`, `{58,62}`,
   `{54,62}`, `{46,62}`, `{30,62}` — pairs at distances 2, 4, 8, 16, 32.
2. **Alternating singletons** (family 2): `d = 2^m−2, d' = 2^m−1` gives
   `{ n−2^m, n−2^m+2, …, n−2 }` — `2^{m−1}` isolated singleton runs, span Θ(n).
   Census n=64: `example (3,62)` → runs `[1,1,…,1,2,1]`, 32 runs, span 62.
3. **One long run** (family 1): `d = 2^k−1, d' = 2^k` gives `[n−2^k−1, n−2]`,
   a single run of length `2^k`. Census n=64: `example (2,63)` → `[61,1]`,
   span 63.

The census shows the multiset's **weight** spreads across essentially all
spans (span histogram is supported on every span 3..n−1, with the max-span
class weighing 2 per n), so item 4's size-concentration does **not** by itself
rule out a witness — these far, weight-2 sets are exactly the cells that could
host one. Whether any of them yields two strings with equal `C_K` and different
S² is **gap G-witness, still open**: the fiber-test script is written but its
output is not captured in the workspace. No witness and no absence bound has
been posted yet.
