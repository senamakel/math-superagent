# Refutation: G-weak-input-strictness's proposed per-window SAT is vacuous

Attacked the **first step** of the live gap `G-weak-input-strictness`
(research/backward/weak-input-fold.md, research/weakened/supply.md), as the run
committed it:

> "sat_solver / tool_builder: for n = 8..64, encode '∃ h ∈ F₂ⁿ with wt(h) ≤ δn
> and wt(Φ_n h) ≥ εn' as a CP-SAT/SAT instance over a grid of (δ, ε) with
> δ→0, and report SAT witnesses or UNSAT thresholds."

The statement I am attacking is the *reading* this step invites: that a SAT
witness to "∃ sparse h with linear fold weight" would be evidence for
`G-weak-input-strictness` (a fixed switch-density-0 string, or the fold
amplifying a sparse input, giving linear weight). I show the proposed finite
search is **trivially and uniformly satisfiable** by an already-known per-window
artifact, so it cannot discriminate the strictness direction from its rival.

## The witness, by hand and by the engine

Encode `n = 8`, `h = h_0..h_7`, fold cells `T(n,d) = ⊕_{o ⊆ d} h[7−d+o]` for
`d ∈ [2,7]`, sparseness axiom `wt(h) ≤ 1` (no two of `h_0..h_7` both 1), and
the conjecture "no three of the six cells are simultaneously 1, i.e.
`wt(Φ_8 h) ≤ 2`".

`find_counterexample` on `code/refute/weak_input_sat_vacuity_n8.p` returned
**refuted (CounterSatisfiable)**, with model `h_7 = 1`, `h_0..h_6 = 0`,
`t2=t3=t4=t5=t6=t7 = 1`. Hand check against the literal definition:

- `d=2` submasks{0,2}→cols{5,7}: `h5^h7 = 1`
- `d=3` submasks{0,1,2,3}→cols{4,5,6,7}: `h4^h5^h6^h7 = 1`
- `d=4` submasks{0,4}→cols{3,7}: `h3^h7 = 1`
- `d=5` submasks{0,1,4,5}→cols{2,3,6,7}: `h2^h3^h6^h7 = 1`
- `d=6` submasks{0,2,4,6}→cols{1,3,5,7}: `h1^h3^h5^h7 = 1`
- `d=7` all→cols{0..7}: `h0^..^h7 = 1`

So `wt(Φ_8 h) = 6 = n−2` while `wt(h) = 1`. Every axiom is satisfied, the
conjecture is falsified.

## What this is

This is the **same per-window boundary spike** already banked as claim
`single-boundary-one-refutes-switch-equivalence-as-stated`: `h = e_{n−1}`
(a single 1 at the window's final index) is read by *every* depth `d` — the
offset `o = d` is always a submask of `d` and lands on index `n−1` — so one 1
gives full weight `n−2`. The sparseness constraint `wt(h) ≤ 1` is satisfied,
and by the capacity curve (claim/`sparse_fold_capture.txt`) the max over
*any* `k`-sparse `h` is `n−2` or `n−3` for every `1 ≤ k ≤ n−1`.

## Why this kills the proposed first step as a discriminator

The run's proposed grid search "∃ h with `wt(h) ≤ δn` and `wt(Φ_n h) ≥ εn`"
returns a SAT witness **at every reachable n** — namely `h = e_{n−1}` — and
these witnesses are all the *same* per-window boundary spike, whose fold weight
is `n−2` for **every** n in the family (the family is `e_{n−1}` per window, not
a single fixed string). It therefore:

1. Always reports "SAT", producing no `(δ, ε)` threshold, no UNSAT boundary,
   and no statement distinguishing `G-weak-input-strictness` (a **fixed** string
   with switch density 0 and linear weight for all large n) from its rival
   `G-eq-sparse-fold-is-sublinear` (fixed sparse ⇒ sublinear weight).
2. Cannot distinguish a per-window family (which the run already knows is not a
   real witness: a *fixed* single 1 at position `j` gives `wt ≤ j+1 = O(1)`,
   claim `fixed-single-1-fold-weight-bounded-by-j`) from a genuine fixed-string
   amplification.

So the SAT/CP-SAT framing proposed to *start* `G-weak-input-strictness` is
vacuous: it is satisfied by a degenerate per-window artifact before any real
witness is searched for, and it has no mechanism to reject that artifact. The
search the run actually needs — and the one the existing `sparse_fold_capture`
already performed — is over **fixed** strings with control for the boundary
spike, not the raw sparseness SAT.

## What this does NOT settle (scrupulously)

This refutes the *method* (the per-window SAT first step) and the unqualified
"sparse ⇒ sublinear" transfer at `k=1`. It does **not** refute
`G-weak-input-strictness` in its correct fixed-string form, and it does **not**
disprove the central hypothesis. Prior exact work (`sparse_fold_capture`) shows
that every **fixed** sparse family examined (powers of 2, squares) has
`liminf ν₂/n = 0`, so `G-weak-input-strictness` as a *fixed-string* statement
remains open and its proposed first move does not advance it.

## Result

```claim
id: weak-input-sat-first-step-vacuous-boundary-spike
statement: The first-step SAT framing proposed for G-weak-input-strictness — "for n=8..64 encode '∃ h∈F₂ⁿ with wt(h)≤δn and wt(Φ_n h)≥εn' over a (δ,ε) grid and report SAT witnesses" — is trivially satisfiable at every reachable n by the per-window boundary spike h=e_{n−1} (single 1 at the final index), which gives wt(Φ_n h)=n−2 with wt(h)=1. Verified at n=8: find_counterexample on the sparseness-constrained encoding (wt(h)≤1, six fold cells) returns h_7=1, all cells 1, wt(Φ_8 h)=6=n−2, CounterSatisfiable; hand-checked cell by cell against T(n,d)=⊕_{o⊆d}h[n−1−d+o]. A raw sparseness SAT therefore reports SAT at every n, yields no (δ,ε) threshold, and cannot discriminate G-weak-input-strictness (fixed string, linear weight for all large n) from its rival G-eq-sparse-fold-is-sublinear (fixed sparse ⇒ linear-weight-ratio 0) — the search must be over fixed strings with the boundary spike excluded.
hypotheses: n=8, d∈[2,n−1] (floor convention of problem.md), h=e_7, fold cell T(n,d)=⊕_{o⊆d}h[n−1−d+o]; sparseness wt(h)≤1; the per-window family e_{n−1} is not a fixed string.
holds-here: yes — the per-window amplification is exactly the run-flagged "single sparse 1 amplifies" obstruction, already banked as single-boundary-one-refutes-switch-equivalence-as-stated; this shows it also vacuifies the specific SAT first-step of the weak-input gap.
status: checked (engine CounterSatisfiable + hand cell-by-cell; n=8 exact)
bearing: the weak-input-strictness gap's proposed first SAT move is degenerate and must be replaced by a fixed-string construction (or a search that fixes one string across n and excludes the boundary spike); the underlying fixed-string question stays open, with prior exact evidence (sparse_fold_capture) that every fixed sparse family examined has liminf ratio 0.
anchor: code/refute/weak_input_sat_vacuity_n8.p; this note
```
