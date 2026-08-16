# K*(n) = floor(n/2) — independent confirmation, extension, and OEIS identification

## What was computed (pattern-finder, this run)

Two fully independent exact implementations of the correlation-order budget
`K*(n)` of the SUPPLY fold, on the authoritative **cumulative** definition
(`C_m(h)` = histogram of `(m+1)`-grams of `h` over overlapping windows;
`C_1..C_K` = tuple of histograms for word-lengths `2..K+1`;
`K*(n) = min{ K >= 1 : S(n)^2 constant on every C_1..C_K fibre }`):

- `code/order_k/kstar_settle.py` (n=2..16): in-place cumulative keymap; the
  `s_sos` oracle was cross-checked against a fully independent direct
  submask-XOR brute on 200 random `(n,h)` — **ALL AGREE**.
- `code/order_k/kstar_settle_minmax.py` (n=17, 19, memory-light per-fibre
  (min,max) of S^2): the two **divergence points** where ceil and floor differ
  inside the range `16..20` previously only in the imported (ceil) table.

Together: n=2..19, including every odd n where ceil and floor disagree.

## Result

`K*(n) = floor(n/2)` = **OEIS A004526** for every `n = 2..19`, with **no
exceptional n**. Witnesses exist at every correlation order up to `floor(n/2)-1`
and cease at `floor(n/2)`.

```
K* = 1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9   (n = 2..19)
```

This was checked against OEIS (A004526, "Nonnegative integers repeated,
floor(n/2)") — exact match.

## Why this is a correction

The imported tables (`research/witness-hunt-n20-imported.txt`,
`research/*/order-k-second-moment*`, `conclusions.md §260`) carry the **ceil**
reading `K*(n)=ceil(n/2)` with an `n=5` "exception" and claim `K*(17)=9,
K*(19)=10`. Under the exact cumulative definition the true values at those
divergence points are `K*(17)=8, K*(19)=9`, i.e. **floor**. The old "n=5
exception" was this same tell: `n=5`: ceil=3 vs true floor=2.

Under the floor reading there is **no exceptional n at all** — a strictly
cleaner closed form than the ceil reading (which needed both odd-n errors and
an `n=5` carve-out). This matches the earlier `kstar_exact.py` reached-to-n=15
verdict, now extended past the previous ceiling to n=19 and matched to OEIS.

## Status

**Correction confirmed (not a proof for all n).** Exact over `n=2..19`
(exhaustive 2^n oracle, three independent implementations agreeing). The
closed-form continuation to all `n` is a conjecture consistent with every
term supplied; there is no theorem forcing `floor(n/2)` past n=19. This is
`measured`/verified, not `proved`.

The substance of the reopened goal is unaffected: witnesses still reach
correlation order `~n/2` (linear in n — `1 < K ≲ n/2`), so the fold `Φ` still
sees structure to linear order. Only the stated closed form is tightened from
`ceil(n/2)` (+ an n=5 exception) to the cleaner `floor(n/2)` (no exception).

## Files
- `code/order_k/kstar_settle.py` — in-place cumulative implementation, n=2..16,
  with independent direct-submask cross-check.
- `code/order_k/kstar_settle_minmax.py` — memory-light per-fibre (min,max),
  n=17,19.
- `code/out/kstar_settle.captured.txt`, `code/out/kstar_settle_minmax.captured.txt`
- This note.
