# The orbit-matrix symmetry break is UNSOUND on the BvLS control

## What was settled (directive 35)

The symmetry-break question for the Z3 orbit matrix is CLOSED as UNSOUND. The
canonical-ordering break — `{diagonal nondecreasing, row-0 lex-min}` on the
orbit matrix M satisfying the necessary quotient equation — rejects the REAL,
KNOWN-GOOD BvLS = srg(243,22,1,2) orbit matrix. A symmetry break that excludes
a solution that provably exists makes any 99 INFEASIBLE produced under it
worthless: it would be a false nonexistence result for the order-3 case, the
same failure mode already recorded once with the localprop saturation branch.

This is the **second unsound engine** this workspace has caught before it
produced a false theorem, and it was caught by the control, as designed.

## What was checked (exact)

- **rook(3) m=3**: exhaustive over all 6 conjugates of the known-good M0 —
  all 6 satisfy the break; status = OPTIMAL. PASS. The break looks sound here
  because rook's orbit matrix has a *varying* diagonal.
- **BvLS m=81**: diagonal values `[2]`, i.e. **constant** → the
  diagonal-nondecreasing half of the break is **vacuous**; the whole burden
  falls on row-0 lex-min. **20,000 randomised conjugations** of the real BvLS
  orbit matrix were tried; **NONE satisfied the break**. Verdict UNSOUND.
- A separate **constructive** sorted-column witness (`orbit_z3_symbreak_constructive`)
  also found **0 vertex-roots** yielding a break-satisfying conjugate — the
  break has not been shown to admit the real BvLS class by construction either.

Capture: `code/out/orbit_z3_symbreak_soundness.captured.txt` records all of
this. The symbroken 99 detached run
`code/out/orbit_z3_enc_g99_symbreak_detached.captured.txt` is QUARANTINED with
header `NOT EVIDENCE — SYMMETRY BREAK UNVALIDATED`; no verdict from it may be
reported or filed.

## The mechanism (worth keeping, directive 35)

BvLS's orbit matrix has **constant diagonal [2]**, so the diagonal-nondecreasing
half of the break is vacuous and the whole burden falls on **row-0 lex-min**,
which the greedy relabelling cannot reach. That is why the break passed at m=3
(rook, variable diagonal) and failed at m=81 (BvLS). This precise defect is
what stops the next attempt repeating the break.

## Consequence for the run

**Do NOT rebuild this canonical-ordering symmetry break on the orbit matrix.** A
symmetry-broken 99 order-3 search is dead with it. The sound route remains the
**plain unbroken encoder**, whose UNKNOWN/timeout is honest and citable
(validated at both controls in 3.30s/0.01s via the fixed-acceptance gate). Any
future symmetry reduction must be validated at BOTH controls (rook m=3 AND BvLS
m=81) before a 99 INFEASIBLE is believed — never read a symbreak INFEASIBLE
until the break passes both controls.

## Files

- `code/out/orbit_z3_symbreak_soundness.captured.txt` — 20,000 random
  conjugations of the real BvLS orbit matrix, 0 satisfying the break; diag [2]
  constant → (A) vacuous; rook 6/6 PASS.
- `code/out/orbit_z3_symbreak_constructive.captured.txt` — constructive
  sorted-column witness, 0 vertex-roots → break not shown to admit BvLS class.
- `code/out/orbit_z3_symbreak_fixed_accept.captured.txt` —
  `AssertionError: row 0 not lex-min` (canonical_conjugate line 177) at m=81.
- `code/out/orbit_z3_enc_g99_symbreak_detached.captured.txt` — quarantined
  symbroken 99 detached run (NOT EVIDENCE).

```claim
id: symbreak-orbit-break-unsound
statement: The canonical-ordering symmetry break on the Z3 orbit matrix —
  {diagonal nondecreasing, row-0 lex-min} — rejects the REAL, KNOWN-GOOD BvLS
  = srg(243,22,1,2) orbit matrix, and is therefore UNSOUND as a constraint: a
  break that excludes a solution that provably exists makes any 99 INFEASIBLE
  from it worthless (a false nonexistence for the order-3 case). 20,000
  randomised conjugations of the real BvLS orbit matrix were tried, NONE
  satisfied the break; a separate constructive sorted-column witness also found
  0 vertex-roots yielding a break-satisfying conjugate. Rook(3) m=3 (varying
  diagonal) passes 6/6 conjugates, which is why the defect only surfaced at
  m=81. Verdict UNSOUND: a refutation-of-a-method result, NOT a graph-existence
  claim.
hypotheses: canonical_conjugate is the greedy relabelling over the S_33 orbit
  relabelling class; the necessary quotient equation is the validated plain
  encoder's constraint set (fixed-acceptance gate passed at both controls).
holds-here: yes — the break is discarded for any 99 order-3 search; a symbroken
  INFEASIBLE would be a false nonexistence.
status: checked (exact; exhaustive at m=3, 20,000 random conjugations at m=81,
  plus a constructive witness; the real BvLS m=81 orbit matrix is known-good
  and its conjugates are its genuine relabellings).
base: code/out/orbit_z3_symbreak_soundness.captured.txt,
  code/out/orbit_z3_symbreak_constructive.captured.txt,
  code/out/orbit_z3_symbreak_fixed_accept.captured.txt,
  code/out/orbit_z3_enc_g99_symbreak_detached.captured.txt
bearing: do NOT rebuild this canonical-ordering break on the orbit matrix. The
  sound route is the plain unbroken encoder (validated fixed-acceptance gate,
  both controls), whose UNKNOWN is honest and citable. Any future symmetry
  reduction must pass BOTH controls before a 99 INFEASIBLE is believed. This is
  the second unsound engine caught before it produced a false theorem.
mechanism: BvLS's orbit matrix has constant diagonal [2], so the
  diagonal-nondecreasing half of the break is VACUOUS; the whole burden falls
  on row-0 lex-min, which the greedy relabelling cannot reach. That is why it
  passed at m=3 (rook, varying diagonal) and failed at m=81 (BvLS).
```
