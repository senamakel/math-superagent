# Second pass — conclusion

The pass ran with one question, set in `GOAL.md` after the collapse hypothesis
was refuted:

> Is there a functional of the fold, sensitive to correlation order `K` with
> `1 < K ≲ n/2`, that is controllable by an arithmetic input **strictly weaker**
> than pointwise mod-4 switch density?

**No such functional was found.** No candidate survived pricing. That is a
negative, not a failure, and it is narrower and better-evidenced than the
negative the first pass closed on.

Written by the operator at shutdown from the pass's own captures. The run was
stopped after three consecutive directives (41, 42, 43) failed to move it off a
settled sub-question; what follows is what it established before that.

## What this pass proved or measured

### 1. Linear supply does not require positive switch density (settled, by exhibition)

The single-1 string `h = e_{n−2}` has switch density `1/n → 0`, yet

```
ν₂(n) = ⌈(n−2)/2⌉ ≈ n/2
```

— full linear supply. The mechanism is exact: `e_{n−2}` is reached by depth `d`
exactly when `d−1` is a submask of `d`, which holds exactly when `d` is odd, so
the count is the number of odd `d ∈ [2, n−1]`. Verified by the canonical oracle,
by a from-scratch literal fold with no shared code, and by an independent
operator computation.

**Bearing.** Positive mod-4 switch density is **not necessary** for linear
supply. Together with the collapse refutation this closes the first pass's
"equivalence indicated" from both sides: its mechanism is gone, and its
necessity direction is false. This is `problem.md` result type 4 territory, and
it does not touch SUPPLY itself — a string with linear supply existing is not
the primes having linear supply.

### 2. Linear supply becomes typical at weight ratio ≈ 1/8 (measured)

Minimum weight at which linear supply is typical (mean `ν₂/n ≥ 0.40` and
fraction `≥ 0.5`), exhaustive to n=16 and sampled at 300 strings per weight
above:

```
n     8      10     12     14     16     32     64     128
w/n   0.375  0.300  0.250  0.286  0.188  0.156  0.125  0.125
```

The primes sit at switch density ≈ 0.585, far above. Whether the ratio tends to
0 or plateaus near 1/8 was **not settled** — the column had fallen monotonically
and then held at 0.125 twice, and the run was stopped before resolving it. That
is the single most valuable unfinished computation here.

### 3. `K*(n) = ⌊n/2⌋`, not `⌈n/2⌉` (settled, exhaustive n=2..18)

The imported figure was wrong at odd `n` — `n=7→3` not 4, `9→4`, `11→5`,
`13→6`, `15→7` — and this explains the `n=5` mismatch the collapse run flagged
rather than smoothing over. Confirmed by six independent implementations. The
substance is unaffected: `Φ` still sees structure to an order **linear in `n`**,
so the pass's territory was real.

Also settled: `order_budget.py`'s single-`C_K`-hash grouping relies on the
refuted "C₁..C_K iff C_K" reduction and is wrong — do not use it. And the
run-length characterisation `K*(n) = R(n) − 1` is **refuted** against ground
truth.

### 4. Two candidate arithmetic inputs closed

- **Mod-6 forbidden gap-blocks are parity-invisible for all `m`**, proved by a
  per-coordinate bijection: each parity bit reaches both values in every class
  and the coordinates are independent. So that whole family of unconditional
  arithmetic constraints cannot reach the fold.
- **Length-`k` pattern frequencies** sit behind the same barrier (Shiu/Maynard
  parts proved, the needed direction open).

### 5. The hit-set route is priced out (operator computation)

Directives 41 and 42 pushed a functional built from the hit sets
`H_j = {d ∈ [2,n−1] : j ∈ M_d}`. Computed directly:

| n | max \|H_j\| | median \|H_j\| | frac(\|H_j\| ≥ 0.4n) |
|---|---|---|---|
| 16 | 14 | 4 | 0.312 |
| 32 | 30 | 8 | 0.188 |
| 64 | 62 | 8 | 0.109 |
| 128 | 126 | 16 | 0.062 |
| 256 | 254 | 16 | 0.035 |

`|H_{n−2}|` equals the odd-`d` count exactly (7, 15, 31, 63, 127), confirming §1
independently. But the fraction of positions with a large hit set falls like
`1/n` while the median stays tiny. An input phrased as *"the switch bits land on
high-hit positions often enough"* would require `h` to concentrate on a set of
density → 0 — a **stronger** demand than positive switch density, so the route
fails the pricing test.

**Caveat, stated because it matters:** `ν₂` is an XOR over `M_d`, not a sum of
`|H_j|`. This prices the *positional resource*, it does not refute every
functional built from hit sets. One escaping this scarcity remains possible, but
must be priced against the table above.

## What remains open

Unchanged from the first pass, and now with one route added:

1. **The original arithmetic statement.** An unconditional second-moment or
   submask-window Walsh bound on the prime gap-parity string. Note that
   `E[S²] = O(n)` is *this* statement, not a weaker one — the pass caught itself
   restating it as if it were new.
2. **Whether the weight threshold tends to 0.** §2. If it does, the required
   input reduces to positive density plus non-adversariality; if it plateaus,
   the constant is real and belongs in the statement.
3. **A functional escaping positional scarcity.** §5's caveat.

## Honest notes

- Three real results (§1, §2, §3) landed in roughly the first hour. The run then
  produced **eight** artifacts re-confirming §3, across three directives telling
  it to stop, and never attempted the priority-1 construction. That is the same
  role-loop failure the first pass showed on scratch-file consolidation:
  directives are acknowledged in the ledger and not executed by the roles.
- The capture discipline, by contrast, held throughout this pass. Headers naming
  sequence/oracle/range, guards on the produced array, negative controls
  explicitly marked discriminating, and one capture whose 35 trailing zero rows
  were correctly labelled as the all-ones kernel control rather than left to read
  as a vacuous table. None of the first pass's six defect classes recurred.
- The operator was wrong twice here and both corrections are recorded: the
  hit-set direction was pushed twice and is priced out in §5, and a suggestion
  that the `K` budget might widen to `~0.75n` was closed by the run in §3.
