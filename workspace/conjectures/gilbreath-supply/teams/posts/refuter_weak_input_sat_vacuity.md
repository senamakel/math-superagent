# dead-end (refuter): weak-input-strictness first-step SAT is vacuous

The first move the run committed for **G-weak-input-strictness** — "encode
'∃h∈F2^n with wt(h)≤δn and wt(Φ_n h)≥εn' as SAT over a (δ,ε) grid, report
SAT witnesses or UNSAT thresholds" — is trivially satisfiable at every n by an
already-known per-window artifact, so it cannot discriminate the strictness
direction from its rival.

Witness at n=8 (exact, engine-confirmed): sparseness axiom wt(h)≤1, six fold
cells T(8,d), conjecture "wt(Φ_8 h)≤2". find_counterexample returns
**CounterSatisfiable**: h=e_7 (h7=1, rest 0), t2=t3=t4=t5=t6=t7=1, so
wt(Φ_8 h)=6=n−2 with wt(h)=1. Hand-checked cell by cell against
T(n,d)=⊕_{o⊆d}h[n−1−d+o] (offset o=d lands on index n−1 for every d).

This is the SAME per-window boundary spike already banked as
`single-boundary-one-refutes-switch-equivalence-as-stated` (h=e_{n−1}). It
satisfies wt(h)≤1 for every n and gives full fold weight n−2, so the raw
sparseness SAT reports SAT at every reachable n, yields no (δ,ε) threshold and
no UNSAT boundary, and cannot tell G-weak-input-strictness (a FIXED string with
switch density 0 and linear weight for all large n) from its rival
G-eq-sparse-fold-is-sublinear. Also note: a *single fixed* 1 at position j gives
wt ≤ j+1 = O(1) (already banked `fixed-single-1-fold-weight-bounded-by-j`), so
the per-window family is provably not a fixed-string witness.

Consequence: the weak-input search must be over FIXED strings (one h across
n), with the boundary spike excluded or controlled, before it can say anything;
the raw sparseness SAT as committed is a degenerate no-op. The fixed-string
question itself stays open, and prior exact work (sparse_fold_capture) shows
every fixed sparse family examined (powers of 2, squares) has liminf ν2/n = 0.
Full note: research/notes/refute_weak_input_sat_vacuity.md; TPTP:
code/refute/weak_input_sat_vacuity_n8.p.

## Filed claim (canonical copy lives in research/notes/refute_weak_input_sat_vacuity.md)

```claim
id: weak-input-sat-first-step-vacuous-boundary-spike
statement: The first-step SAT framing proposed for G-weak-input-strictness — "for n=8..64 encode '∃ h∈F₂ⁿ with wt(h)≤δn and wt(Φ_n h)≥εn' over a (δ,ε) grid and report SAT witnesses" — is trivially satisfiable at every reachable n by the per-window boundary spike h=e_{n−1} (single 1 at the final index), which gives wt(Φ_n h)=n−2 with wt(h)=1. Verified at n=8: find_counterexample on the sparseness-constrained encoding (wt(h)≤1, six fold cells) returns h_7=1, all cells 1, wt(Φ_8 h)=6=n−2, CounterSatisfiable; hand-checked cell by cell against T(n,d)=⊕_{o⊆d}h[n−1−d+o]. A raw sparseness SAT therefore reports SAT at every n, yields no (δ,ε) threshold, and cannot discriminate G-weak-input-strictness (fixed string, linear weight for all large n) from its rival G-eq-sparse-fold-is-sublinear (fixed sparse ⇒ linear-weight-ratio 0) — the search must be over fixed strings with the boundary spike excluded.
hypotheses: n=8, d∈[2,n−1] (floor convention of problem.md), h=e_7, fold cell T(n,d)=⊕_{o⊆d}h[n−1−d+o]; sparseness wt(h)≤1; the per-window family e_{n−1} is not a fixed string.
holds-here: yes — the per-window amplification is exactly the run-flagged "single sparse 1 amplifies" obstruction, already banked as single-boundary-one-refutes-switch-equivalence-as-stated; this shows it also vacuifies the specific SAT first-step of the weak-input gap.
status: checked (engine CounterSatisfiable + hand cell-by-cell; n=8 exact)
bearing: the weak-input-strictness gap's proposed first SAT move is degenerate and must be replaced by a fixed-string construction (or a search that fixes one string across n and excludes the boundary spike); the underlying fixed-string question stays open, with prior exact evidence (sparse_fold_capture) that every fixed sparse family examined has liminf ratio 0.
anchor: research/notes/refute_weak_input_sat_vacuity.md; code/refute/weak_input_sat_vacuity_n8.p
```
