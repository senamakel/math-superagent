# Pattern-finder deliverable: the correlation-order budget K*(n) = floor(n/2)

## The question this settles (GOAL priority 3)

The run was reopened specifically because `Φ` provably sees structure up to
correlation order `K*(n) ≈ ⌈n/2⌉`, with an explicit witness at n=8. GOAL.md
flags that "the first pass's n=5 mismatch says the closed form is not yet
right", and asks whether `K*` really is `⌈n/2⌉` or merely close.

**Answer: neither `K*(n)=⌈n/2⌉` nor "merely close". Under the faithful nested
reading, `K*(n) = floor(n/2)` exactly.** The `⌈n/2⌉` budget comes from an
*imported* table (`research/witness-hunt-n20-imported.txt`); every computed
definition on the canonical oracle fails to reproduce it, and the single
definition that makes `K*` a genuine monotone threshold gives `floor(n/2)`.

## The three working definitions, and why only one is sound

With `S(n)=(n−2)−2ν₂(n)` the signed fold excess and `C_K(h)` the empirical
`(K+1)`-gram histogram of `h`:

1. **Single-histogram reading**: `K*(n) = min{K : S² is constant on every C_K-fiber}`.
   The `⌈n/2⌉` table lives here. But this is NOT a threshold: `C_{K+1}` does
   not determine `C_K` (the last boundary window is lost on marginalisation),
   so "no witness at K" is not inherited upward. Concretely n=14 has no
   witness at K=8 yet a witness at K=9. With no monotonicity, `K*` is not a
   well-defined crossing and has no closed form. *(capture: kstar_structural)*

2. **Cumulative / nested reading** (the faithful reading of `C_1..C_K`):
   `K*(n) = min{K : S² constant on every fiber of (C_1,...,C_K)}`. Here
   `CUM_{K+1}` refines `CUM_K`, so no-witness is inherited upward and `K*` is
   a genuine threshold. **This gives `K*(n) = floor(n/2)` exactly.**

3. **Run-length characterization**: `K*=R(n)−1` where `R(n)` is the max run
   length of `M_d △ M_{d'}`. REFUTED directly (n=6,K=3 counterexample:
   a=001001,b=010010 same C_3-fiber, S²=4 vs 0). `R(n)` is a 2-power block
   function (`2^k` on `(2^k,2^{k+1})`, `2^j−3` at `n=2^j`), which is far above
   `floor(n/2)` except at coincidences. *(capture: kstar_structural; closed
   form independently reproduced on n=2..32)*

## Measurement (independent, cumulative definition)

`code/pattern_finder/kstar_cum_independent.py` — exhaustive `2^n` brute,
canonical `s_sos` oracle cross-checked on 200 random `(n,h)` against a direct
submask-XOR oracle (all agree):

```
n= 2..18 :  K*_cum = floor(n/2) = 1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9   MATCH at every n
```

Extends the catalogued range (n=2..16) to n=17,18 — the first two terms past
the previously measured budget — and both match `floor(n/2)`. This agrees with
the catalogued captures `kstar_exact` and `kstar_settle` (both `floor(n/2)`,
n=2..16), so three independent implementations plus mine coincide.

`floor(n/2)` is A004526 / A008619 ("nonnegative integers repeated") — the
trivial closed form.

## Status

**Verified numerically (exact over n=2..18)**: `K*(n) = floor(n/2)` under the
cumulative nested reading. **Not a proof for all n.** The next term that would
falsify it is n=19 (predicts floor(19/2)=9); n=19/20 are the natural extension
targets (2^19, 2^20 strings — the n=20 exhaustive pass is the expensive one).

## What this corrects in the catalogued ledger

- Claim `kstar-n20-measured-table` asserts `K*=⌈n/2⌉` except n=5, citing the
  imported table. That table does **not** reproduce from any computed
  definition on the canonical oracle (`kstar_resolve` verdict). Its
  inconsistencies (n=5 vs n=6,7,8 matching different definitions) are the
  signature of mixing the two readings.
- The "n=5 mismatch" is an artifact: n=5 is where `⌈5/2⌉=3` first disagrees
  with `floor(5/2)=2`, and it is the odd case where the two definitions
  diverge earliest.
- The GOAL.md phrasing "K*(n) ≈ ⌈n/2⌉" should read "K*(n) = floor(n/2)", which
  still satisfies the reopening premise `1 < K ≲ n/2` (floor(n/2) ≲ n/2).

## Why this matters for the main question

The reopening's single question was: is there a functional of the fold,
sensitive to correlation order `K` with `1 < K ≲ n/2`, controllable by an
arithmetic input strictly weaker than pointwise mod-4 switch density? The
budget `floor(n/2)` confirms the functional breadth: `Φ` reads correlations
out to half the string length. The candidate functional — the second moment
`E[S²]=O(n)` — is exactly the `K ≍ n/2`-sensitive object the witness at n=8
exhibits, and the open arithmetic input remains (A): a second-moment /
submask-window autocorrelation bound on the prime gap-parity string `h`
(pattern_finder_deliverable_2.md §rec). **No sequence tool extends this** — the
sequence side is exhausted; the next step is a derivation of `floor(n/2)` and
then the priced arithmetic bound.

> **Directive 42 correction — do not follow the candidate named above:** naming
> `E[S²]=O(n)` as *the* candidate functional is circling; it is the first pass's
> surviving open statement (CONCLUSION.md §5), never shown weaker than switch
> density. The un-attempted directive-41 work is the hit-set functional (thread
> `hit-set-functional`, task `build-hit-set-functional`), defined from the
> per-position submask hit sets `H_j`, not from `E[S²]`.

## Files
- `code/pattern_finder/kstar_cum_independent.py` — independent cumulative brute (n=2..18).
- captures agreeing: `kstar_exact.captured.txt`, `kstar_settle.captured.txt`,
  `kstar_resolve.captured.txt`, `kstar_structural_capture.txt`.
