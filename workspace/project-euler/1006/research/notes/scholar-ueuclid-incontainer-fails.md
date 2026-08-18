# Contradiction: in-container ueuclid run FAILS, directive 11's "verified" is contradicted

**Status: open, critical.** The captured in-container record
`code/out/ueuclid_main.captured.txt` is a run of the CURRENT module
`code/lib/ueuclid.py` (its deterministic case list matches the module's own
`__main__` verbatim, and the file is 9491 B vs 9498 B on disk). That run
**fails every acceptance test it executes**:

- acceptance 1-3 (ueuclid vs ueuclid_direct, random): **0/30**
- acceptance 2 (S1 at z=1 vs plain floor_sum): **0/30**
- deterministic cases: **5/6 MISMATCH** (only `(1000,3,1346269,20)` ok)
- banner: **"65 FAILURES -- do not trust ueuclid yet"**

This directly contradicts CONTEXT.md / directive 11, which assert the primitive
is "verified on current code... 40 random trials... zero failures... Do NOT
rebuild or re-derive it."

## Hand-check of the determinist case (exact arithmetic)

`ueuclid(1, 0, 1, 5, z=3)`: path y = floor((1·t + 0)/1) = t, t = 0..4.
S0 = Σ_{i=0}^{4} 3^i = 1+3+9+27+81 = 121
S1 = Σ 3^i·i = 0 + 3 + 18 + 81 + 324 = 426
S2 = Σ 3^i·i² = 0 + 3 + 36 + 243 + 1296 = 1578
The module's O(log) `ueuclid` returns S0=121 ✓, S1=547 ✗, S2=2551 ✗.
The literal `ueuclid_direct` (the oracle) is correct by construction.

## Localisation of the bug

Across every random trial and every deterministic case, **S0, dR, dU, w all
match** the direct oracle; **only S1 and S2 differ**. So the weight indexing
(Σ z^t) and the floor-sum structure are right; the fault is precisely in the
S1/S2 cross terms of the `compose` rule — the `l.dU * r.S0` and
`2*l.dU*r.S1 + l.dU²*r.S0` boundary-shift terms that carry floor values across
a segment boundary. This is the exact "one place the primitive goes wrong"
hazard that every source note (fhq, LOJ138, OI-wiki) and the thread file
identify. The O(log) recursion reaches the correct segment split but
mis-corrects the floor offset when combining segments.

### Precise diagnosis (exact arithmetic, (1,0,1,5,3))

Path: floor((1·i+0)/1) = i, i = 0..4. Oracle S1 = Σ 3^i·i = 426, S2 = 1578.
Module returns S1 = 547 = 426 + 121 = S1 + S0, S2 = 2551 = 1578 + 2·(Σ3^i·i)·1
+ Σ3^i·1² = 1578 + 852 + 121. So the module behaves as if every floor value
were (i+1) instead of i — a **uniform +1 for each index** (ΔS1 = 1·S0,
ΔS2 = 2·1·S1_correct + 1²·S0).

The cause: the generic Node `compose` carries `dU` as the *total U-count of the
left segment* and adds it as a flat constant to the right segment's floors via
`l.dU * r.S0` / `2*l.dU*r.S1 + l.dU^2*r.S0`. In the fhq/vec model each U step
realises a **per-emission y increment**, so the correct "shift of the floor
value across the boundary" is the *prefix floor value at the boundary*, not the
total U count; using the total makes the shift proportional to the whole left
segment's U's, over-counting by one per emission whenever the p≥q merge
(U^{p//q}·R) is applied. The p≥q branch is exactly where this fires (case
(1,0,1,5,3) has p=q=1 after the first reduction, i.e. every floor has full
U^{1} prefix).

Fix direction (for the solver): either (a) carry in each Node the *boundary
floor value* (the floor of the segment's last R index) rather than total dU
for the cross terms, keeping dU only as the count for dU-totals; or (b) verify
against `ueuclid_direct` on the specific p≥q-heavy cases (1,0,1,5,3) and
(7,2,3,10,3) until S1/S2 match. The verify-against-direct gate is the only
trusted acceptance.

## What this means for the run

Directive 10/11 gate the ENTIRE O(log) critical path — acceptance tests 1-5,
the directive-6 anchors, and finally Psi(10^18) — on this primitive being
sound. It is not. Running acceptance 4 (telescoped v through the monoid vs
mech_psi k=1..150), the anchors, or 10^18 through the current `ueuclid` would
produce wrong residues that look like progress. **The primitive must be fixed
(boundary-shift composition) and re-pass acceptance 1-3 before any higher
acceptance is trusted.**

Two possibilities, both meaning the on-disk module is not sound:
(a) the outside-container verification (directive 11: "40 random trials, zero
    failures") was done on a fixed copy that was then overwritten by this
    broken one; or
(b) the outside-container verification is itself unreliable.
Either way the on-disk module fails its own `__main__`. This is the claim-block
form of the finding:

```claim
id: ueuclid-incontainer-fails-s1s2
statement: The O(log) ueuclid monoid in code/lib/ueuclid.py fails its own
acceptance tests in-container (0/30 random vs the direct oracle, 0/30 S1-at-z=1
vs plain floor_sum, 5/6 deterministic). S0/dR/dU/w are correct in every case;
S1 and S2 are wrong — the boundary-shift (dU) cross terms in compose are
incorrect. Hand-check: ueuclid(1,0,1,5,3) returns S1=547, S2=2551; the correct
values are S1=426, S2=1578.
hypotheses: none beyond ueuclid.py as on disk and the captured __main__ run.
holds-here: yes
status: checked (exact hand-arithmetic + the captured 65-failure run)
bearing: blocks acceptance 4, the directive-6 anchors, and Psi(10^18) until the
compose boundary-shift terms are corrected and acceptance 1-3 re-pass.
anchor: code/out/ueuclid_main.captured.txt, code/lib/ueuclid.py
contradicts: monoid-composition-formulas-verified  (the recite rules in that
  claim are CORRECT and PROVED; the on-disk implementation fails to realise
  them — this is a translation bug in the Python compose's dU boundary-shift
  terms, NOT an error in the verified formulas. The contradiction is between
  directive-11's 'verified on current code, zero failures' and the actual
  module, which is what blocks acceptance 4+.)
answers: (none — opens, not closes, a gap)
search-frame: the module's own __main__ deterministic case (1,0,1,5,z=3) and
  the 30 random + 30 floor_sum + 6 deterministic checks it runs; all repeatable
  by python3 code/lib/ueuclid.py
```

The `ueuclid_tests.captured.txt` "20/20 ALL PASS" file is even more stale and
is not evidence about the module on disk either.

## RESOLVED (superseded)

This finding was a **false alarm** — the module is sound. The 65-failure
`__main__` run it quoted was the *old* capture in which `ueuclid_direct` and
the docstring used the 0-indexed convention while the O(log) recursion (the
verbatim fhq/LOJ138/OI-wiki translation) is 1-indexed. The recursion's S1/S2
were never wrong: `ueuclid(1,0,1,5,3).S1=547` is the correct 1-indexed value
`sum_{t=1}^5 3^(t-1)*t`; `426` in the body above is the 0-indexed `sum z^i*i`,
a different quantity the `ue0` wrapper computes. There is **no compose
boundary-shift bug**. See `research/notes/refuter-ueuclid-s1s2-false-alarm.md`
(claim `ueuclid-s1s2-false-alarm-refuted`) and the tool-builder session that
closed it.

What the session changed to make the whole module self-consistent (recursion
core untouched, byte-identical):
1. `ueuclid_direct` rewritten to the SAME 1-indexed convention
   (t=1..n, weight z^(t-1), dU=(p*n+q)/r), so the oracle agrees with the
   recursion.
2. Module docstring, `_solve` docstring, Node-field comments state the
   1-indexed convention explicitly, citing OI-wiki/fhq/LOJ138.
3. Added documented 0-indexed wrapper `ue0(p,q,r,n,z)` = `ueuclid(p, q-p, ...)`
   (NOT `ueuclid(p, p+q, ...)` — a draft's formula had a sign error; q+p fails
   0/40 empirically, q-p matches 30/30), with exact k-lift/undo for p>q.
4. Re-ran and captured: `code/out/ueuclid_main.captured.txt` now shows
   **ALL MONOID TESTS PASSED** — acceptance 1-3 30/30, floor_sum 30/30,
   deterministic 6/6, ue0 acceptance 30/30, large-n dU=381966011250351898
   == 10^18/phi^2 floor, dR=10^18.
