# G4 thesis attack: is a fixed-dimensional O(log k) aggregation known/available?

## Thesis attacked

The workspace's standing theses — `g4-fixed-dimensional-collapse`, `joint-intercept-closure`, `bivariate-floor-moment-diagonal`, `g4-structural-aggregation` — all assert that **no fixed-dimensional O(log k) aggregation of Ψ(k) over all k+1 mechanical intercepts is known/available** in this workspace.

## What I tested

### 1. Reproduced both official anchors (small exact oracle)

From `code/refute/small_oracle_thesis_attack.py` (written for this attack, reproducing the logic of `code/brute.py`):

- F₃ = {001, 010, 100, 101}, Ψ(3) = 20302  ✓
- Ψ(10) ≡ 10699667 (mod 101001001)  ✓

The factor set and sum are exactly as the problem states. The mechanical model (`mech_psi.py`) agrees with brute-force enumeration at every k ≤ 400 (recorded: `code/out/mech_psi.captured.txt`, `code/out/psi_residues.txt`).

### 2. Checked the additive 3-number summary closure

**Existing recorded counterexample** (`code/out/fib_block_state_counterexample.txt`, `code/out/immediate_oracle_and_counterexample_capture.md`): at k=2, strings `010` and `101` have identical (count, Σw, Σw²) = (2, 11, 101), but appending 0 gives `0100` → (3, 11, 101) vs `1010` → (3, 21, 201). The three-number summary is **not closed** under concatenation.

### 3. Checked the single-intercept replacement

**Existing recorded failure** (`code/out/pinning_k123.txt`): the tempting reduction to a single `ue0` call (only m=0 intercept) disagrees with true Ψ(k) at k=1 (mech_psi=1 vs single=0), k=2 (101 vs 0), k=3 (20302 vs 100900000). The k+1 intercepts are not replaceable by one.

### 4. Checked for any *implemented* O(log k) evaluator in the workspace

Searched every file for references to 10^18, log-k evaluation, O(log), and fixed-dimensional state. All findings:

- `code/solution.py` raises `NotImplementedError` — explicitly an O(k) placeholder, not a full-size solver.
- `code/directive9_transfer.py` is O(N) finite-block experiment, not O(log k).
- `code/lib/ueuclid.py` is the verified O(log) primitive for *a single intercept* — but the joint-intercept aggregation theorem is missing.
- `code/out/verify/window_residue_route.py` is the validated O(k) sliding-window evaluator, producing the corrected anchors Ψ(10⁴)=34432237, Ψ(10⁶)=20938836. It is O(k), not O(log k).
- All Lean files (`G4Statement.lean`, `G4JointIntercept.lean`, `G4JointInterceptProposition.lean`) have `:= by sorry` for the joint-intercept theorem.

**No valid O(log k) joint-intercept evaluator exists in this workspace.**

### 5. Rechecked the adopted-surviving approaches

The two adopted approaches (Ostrowski/three-gap closed form, Rauzy right-special extension recurrence) are explicitly **not implemented** — their first steps are verification tasks, not completed evaluators. They are hypotheses, not counterexamples to the thesis.

## Verdict

**Thesis survives this attack.** No concrete counterexample falsifying the claim "no fixed-dimensional O(log k) aggregation is known/available" was found. The workspace's own evidence consistently confirms the obstruction:

| Claim | Evidence | Status |
|-------|----------|--------|
| (count,sum,sumsq) is closed | Falsified at k=2 (010 vs 101 sharing summary, diverging on '0') | Refuted |
| Single-intercept replacement works | Falsified at k=1,2,3 (mech_psi ≠ single-intercept S2) | Refuted |
| A k+1 intercept O(log) evaluator exists | No file in workspace implements one | Not found |
| Ostrowski/three-gap route is implemented | No code exists; first step is verification | Not implemented |
| Rauzy extension recurrence is implemented | No code exists; first step is verification | Not implemented |

## Boundary of the claim

The negative thesis is not *proved* — a richer fixed-dimensional state (preserving full prefix/suffix contexts) is not ruled out by the tested additive/single-intercept families. The two adopted approaches are the workspace's bets for constructing such a state. But as of this attack, neither is a working evaluator, and no third candidate is documented.

The thesis therefore stands: no fixed-dimensional O(log k) aggregation of Ψ(k) is **known/available** in this workspace.