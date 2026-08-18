# Handoff: universal-Euclidean monoid ready for execution

The operator's steering directive for this cycle ("tool_builder: put
code/lib/ueuclid.py on disk", directive 7) is written and source-verified, but
**execution is still pending**: the scholar has no run tool in this cycle's
function set, so the pass/fail counts have not been produced. That single step
belongs to tool_builder.

## On disk (this cycle)

- `code/lib/ueuclid.py` — the directive-4 monoid: `Node(dU,dR,w,S0,S1,S2)`,
  `compose`, `chain`, `pow_node`, `_solve` (fhq/OI-wiki/LOJ138 Euclidean
  recursion, O(log)), `ueuclid(p,q,r,n,z)` and `ueuclid_direct` (O(n) oracle).
  Formulas verified by hand against three full texts this cycle.
- `code/out/test_ueuclid.py` — acceptance tests 1-3 (S0/S1/S2 vs direct loop
  and plain floor_sum, dU/dR/w, identity, associativity), fixed edge cases +
  40 random (p,q,r,n,z) with n in the low thousands. Prints pass/fail counts.

## What tool_builder must run

    cd /workspace && python3 code/out/test_ueuclid.py

Expect "ALL PASS, 0 failures". The output is the deliverable; if it fails, the
bug is almost certainly in a dU-shift across a segment boundary (the one place
the primitive goes wrong), not in the Euclidean recursion itself (which is a
verbatim translation of the three sources).

## Verified (this cycle, source-backed)

- Compose formulas S0/S1/S2 (claim `monoid-composition-formulas-verified`,
  proved) — checked against LOJ138's general binomial rule
  `C.ans[a,b] = A.ans[a,b] + Σ C(a,i)C(b,j)·A.cnt1^i·A.cnt2^j·B.ans[a-i,b-j]`
  specialised to geometric weights and floor moments ≤ 2.
- Recursion: verbatim translation of fhq (cnblogs 15719155), OI-wiki universal
  Euclidean, and LOJ138 mizu164.
- O(log max{p,r}) complexity, n never a loop bound — the k=10^18 fact.

## After (1) passes

Acceptance (4) v-tele vs code/mech/mech_psi.py k=1..150 and Ψ(10)=10699667,
then (5) the directive-6 anchors Psi(10^4)=34432237 / Psi(10^6)=20938836
(verify in-container first), then k=10^18 with F(n)>k, two approximants.

The Cognee memory server is down this cycle; durable findings are persisted on
disk (`research/notes/scholar-verified-monoid-primitive.md`).
