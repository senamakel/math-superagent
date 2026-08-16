# Refuter: the fixed single-1 bound — the sparsest case cannot discharge G-weak-input-strictness

Attacked the positive witness wanted by `G-weak-input-strictness`: *some fixed
binary string h\* with switch density 0 yet ν₂(n) ≥ c·n*. The sparsest possible
candidate is a single fixed 1.

## Hand analysis (the content)

The windowed fold cell is

    T(n,d) = ⊕_{o ⊆ d} h[n−1−d+o].

For a **fixed** single 1 at position `j` (h = e_j, all other entries 0 for all
n), the cell reads the 1 exactly when

    n−1−d+o = j  ⇔  o = d − (n−1−j).

Since o must be ≥ 0 and ≤ d, and d ≤ n−1, this needs

    d ≥ n−1−j.

So the only depths d that can contribute lie in the interval
`[n−1−j, n−1]`, which has **exactly j+1 elements independent of n**. Hence

    ν₂(n) = wt(Φ_n e_j) ≤ j+1 = O(1)   as n → ∞.

### Hand checks
j=1: eligible d ∈ {n−2, n−1}.
  - d=n−2: o = 0, submask of d → T=1 (reads h[1] ✓).
  - d=n−1: o = 1, submask of n−1 iff n even → T=1 iff n even.
  - ν₂(n) ∈ {1,2} ≤ j+1 = 2. ✓
j=2, n=7 (c = n−1−j = 4): eligible d ∈ {4,5,6}.
  - d=4(100): o=0 submask → T=1
  - d=5(101): o=1 submask → T=1
  - d=6(110): o=2(010) submask of 110 → T=1
  - ν₂(7)=3 ≤ j+1 = 3. ✓
j=3: eligible d ∈ {n−4, …, n−1}, ≤ 4 values → ν₂ ≤ 4. ✓

The upper bound j+1 is uniform in n, so a fixed single 1 gives **bounded, not
linear** weight. This is exactly what the run's scrupulous note
(`research/notes/refute_single_boundary_one.md`) conjectured; here it is
proved sharply for the single-spike family.

## Consequence for the run

`G-weak-input-strictness` wants a *fixed* h\* with switch density 0 yet
ν₂ ≥ c·n. This bound proves the **sparsest candidate fails**: a string with
finitely many 1s (in particular a single 1) gives ν₂(n) = O(1), since each
fixed 1 at j contributes at most j = O(1) for all n. A witnessing h\* must
therefore have **support growing with n** — its 1-count is o(n) (switch density
0) but unbounded. That pins the shape of the witness the run is searching for:
sparse-but-growing, never a finite spike.

## Separate, already-banked point

The *per-window* family h^{(n)} = e_{n−1} (a single 1 at the window's final
index, n-dependent) DOES amplify to linear weight ν₂(n) = n−2 — already banked
as `single-boundary-one-refutes-switch-equivalence-as-stated`. The contrast is
the instructive one: per-window the 1 lands at the read-boundary every depth
shares; fixed it lands at position j and only −j depths can reach it.

## Engine

Encoded both facts as TPTP under `code/refute/`:
- `single_boundary_n6.p` — per-window boundary amplification (each cell's
  parity via DNF of the submasks): `find_counterexample` = **undecided**.
- `fixed_single_bound_n7.p` — fixed j=2 bound at n=7: **undecided**.

The engine returns undecided on these because parity/XOR over a 2-element
domain is not cleanly a finite first-order model (the DNF parity encodings do
not yield a small finite counter-model to a forced witness). The mathematical
content is entirely in the hand derivations above; the engine confirms nothing
about this particular encoding class. Reported honestly: engine did not
independently confirm; the fixed-1 bound is a proof, the per-window one the
run's own program already confirmed.

```claim
id: fixed-single-1-fold-weight-bounded-by-j
statement: For a fixed single 1 at position j of an otherwise-zero string h
  (h = e_j, constant across n), the windowed fold weight is
  nu2(n) = wt(Phi_n e_j) <= j+1 = O(1) as n -> oo. Proof: cell T(n,d) can read
  the 1 only when d >= n-1-j (for o = d-(n-1-j) to be >= 0), and d <= n-1, so
  at most j+1 depths are eligible, independent of n. Consequently a string
  with finitely many 1s (in particular a single 1) gives nu2(n) = O(1),
  so the G-weak-input-strictness witness cannot be a finite sparse spike;
  its support must grow with n (1-count = o(n) but unbounded).
hypotheses: windowed fold cell T(n,d) = XOR_{o subseteq d} h[n-1-d+o], d in
  [2, n-1] (problem.md facts 1-2); h fixed across n.
holds-here: yes — hand-checked for j=1 (nu2 in {1,2}), j=2 at n=7 (nu2=3),
  j=3 (nu2<=4); matching the run's scrupulous note's conjecture with a sharp
  uniform bound.
status: checked by hand (three small cases); a direct counting proof;
  engine undecided (parity encoding limitation), not independently confirmed.
bearing: pins the shape of any G-weak-input-strictness witness (must be
  sparse-but-growing); confirms the run's scrupulous distinction that a fixed
  single 1 does NOT give linear weight, unlike the per-window boundary spike.
anchor: code/refute/fixed_single_one.py, code/refute/fixed_single_bound_n7.p,
  code/refute/single_boundary_n6.p; this note.
```
