# Reopened — the collapse hypothesis is refuted

This workspace was closed with `research/CONCLUSION.md` naming one surviving
open statement and adding that **equivalence to switch density was "the
indicated answer"**, on the grounds that every second-moment object built here
collapsed at the coarsest dyadic scale `g=0` to the mod-4 switch-pair
correlation, observed across eight independent candidate routes.

**That indication is now contradicted.** A dedicated run
(`workspace/conjectures/gilbreath-collapse`, `2628fcfb`) asked whether the
collapse is a theorem about `Φ` or an artifact of the eight, and refuted it with
an explicit witness.

## What was refuted, precisely

At `n = 8`:

```
h  = 00000010     C₁ = (5, 1, 1, 0)     S² = 0
h' = 00000100     C₁ = (5, 1, 1, 0)     S² = 4
```

Identical correlation vectors, different `S²`. Hand-verified against the submask
definition, independently of the run's oracle: `h` has its 1 at index 6, seen by
depth `d` exactly when `d−1 ⊆ d`, true for `d = 3,5,7`, so `S = 6 − 2·3 = 0`;
`h'` has its 1 at index 5, seen when `d−2 ⊆ d`, true for `d = 2,3,6,7`, so
`S = 6 − 2·4 = −2` and `S² = 4`.

The substantive finding is the **threshold**, measured `n = 4..20`:

```
K*(n) ≈ ⌈n/2⌉        n=8 → 4,  n=12 → 6,  n=16 → 8,  n=20 → 10
```

Witnesses exist up to correlation order about `n/2`. **No uniform bound exists,
and `Φ` sees structure to an order linear in `n`.**

Controls held: `witness@K = n−1` is `False` at every `n` — full-order
correlations determine `h` up to the kernel and `S²` is kernel-invariant, so the
test demonstrably can fail. The run also flagged its own `⌈n/2⌉` guess as
mismatching at `n=5` rather than smoothing it over.

## What this does and does not change here

**Does not change.** The fold-genericity result stands untouched. It is a
*measurement*: no measurable statistic of `ν₂` is prime-specific, matched iid
strings at the measured switch density reproduce the dip counts and last-dip
positions almost exactly. That was never a claim about what `Φ` is capable of
seeing — only about what the primes were observed to carry.

**Does change.** The mechanism behind "equivalence indicated" is gone. There is
no theorem forcing every functional of the fold to factor through pair
correlations, so the eight collapses were a property of the eight routes chosen,
not a law about `Φ`. Any statement in `CONCLUSION.md` reading the collapses as
evidence for equivalence must be discounted to what it is: eight routes that
happened to share a weakness.

**The synthesis, and the sharpened question.** `Φ` *can* see structure up to
order `~n/2`; the primes were *not observed* to carry any that distinguishes
them from random. Those are compatible, and together they say exactly where to
look:

> Is there a functional of the fold, sensitive to correlation order `K` with
> `1 < K ≲ n/2`, that is controllable by an arithmetic input strictly weaker
> than pointwise mod-4 switch density?

That is GOAL priority 2, reopened, and now with a measured budget for how much
room exists — `K*(n) ≈ ⌈n/2⌉` says how far past pairs a functional may reach.

## Rules carried forward

Every operational lesson from the first pass still applies and is not to be
relearned: one canonical oracle with the entry guard; temp-file-then-move
captures; a negative control shown failing in every verification; the `n` or `N`
range stated on every claim; measurement labelled as measurement; the six closed
doors in `problem.md` never reopened.

Two of those doors deserve re-reading in this light, and **neither is reopened**:
door 1 (weight alone) and door 4 (anti-dyadicity) are refuted by explicit
witnesses that remain valid. The refutation above is about the *collapse
hypothesis*, which was never one of the doors.
