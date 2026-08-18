# Scholar digest — cycle: library close-out, remaining templates resealed, anchors verified

## What the research agent added this cycle, and its verdicts

The reference library (`research/sources/*.full.md` → `research/summaries/*.md`)
arrived already ~fully digested by prior cycles. This cycle the scholar:
(1) resealed the last three surviving "Digest only" templates with honest
verdicts, and (2) re-confirmed the state of the two load-bearing execution
gates.

### The three resealed templates

- **`dekking-keane-conjugacy-fibonacci-dynamical-system`** — **does not help.**
  The on-disk `.full.md` is only the arXiv *abstract page*; the converter never
  captured the paper's body, so no theorem is quotable from it. Its content
  (topological conjugacy of Fibonacci-class substitution systems) is an
  indirect structural question on directive 9's family, not the arithmetic of
  Ψ(k). Kept as a citation of record only; flagged so nobody vents a claim
  from a title.
- **`allouche-mendesfrance-automata-automatic-sequences`** (+ `-oeis` copy) —
  **does not help — unreadable.** Both downloads of this PDF carry the same
  non-embedded-font mojibake; neither holds recoverable text. Recorded as a
  conversion failure (not a missing paper), so nobody re-attempts the same two
  URLs. Subject covered by readable held texts (Berstel 2007, Lothaire C2,
  Coven–Hedlund 1973).

### Sources confirmed already digested / correctly classified (not re-digested)

Frid (Ostrowski prefix decomposition; background, one claim), Schaeffer
(local period; background, no claim), Brown (unweighted floor-power sums;
anchors the algebra the weighted monoid generalises), Sivasankar–Rama 2207.04304
(load-bearing position theorem: Lemma 2 conjugate-prefix form + Prop 1
contiguous-window form, the primary anchor for directive 9's claim 1),
Schaeffer–Shallit / Hieronymi / the Cobham tier (negative result, correct),
the OEIS catalogue (closed). All carry their statement-level notes and claim
blocks; nothing load-bearing was left as a bare abstract restatement. The
`library-build-status.md` outline confirms the library is saturated on every
load-bearing side and the bottleneck is the solver's wiring, not references.

## Resolution of the standing ueuclid contradiction

The one internal contradiction this cycle's records carried was the
`ueuclid-incontainer-fails-s1s2` alarm ("65 FAILURES, do not trust ueuclid")
against the asserted "verified on current code" of directive 11. **Now
conclusively resolved as a false alarm** by two independent refutations
(`research/notes/refuter-ueuclid-s1s2-false-alarm.md`,
`code/refute/ueuclid-S1-index-refutation.md`):

- `code/lib/ueuclid.py` is **1-indexed** (t = 1..n, weight z^{t-1}), matching the
  fhq/LOJ138/OI-wiki universal-Euclidean convention; the 0-indexed sum is the
  `ue0` wrapper.
- Hand-check `ueuclid(1,0,1,5,3)` → S0=121, S1=547, S2=2551: **correct**
  1-indexed values; the claim's "426/1578" were the 0-indexed quantity.
- The captured `code/out/ueuclid_main.captured.txt` reports "ALL MONOID TESTS
  PASSED (ueuclid == ueuclid_direct on every trial)" — 30/30 random + 30/30
  floor_sum + 6/6 deterministic, plus a 10^18 sanity
  (dU = 381966011250351898 = floor((514229·10^18+3)/1346269)).
- **There is no compose boundary-shift bug to fix.** The genuine remaining
  hazard is *reduction* indexing (which power of 10 the j-th digit of the
  telescoped v carries), to be pinned against mech_psi at small k — not the
  primitive's arithmetic.

This is stored in Cognee (the memory server is back up this cycle).

## Advance over the standing CONTEXT: directive-6 anchors verified in-container

CONTEXT.md, `research/backward/g4-universal-euclidean-floor-sum.md` and the
open-gap list still describe the directive-6 anchors as **asserted, not yet
verified in-container**. That is now stale:

- `code/out/verify/window_residue_route.captured.txt` (an in-container run of
  `window_residue_route.py`) shows **ALL CHECKS PASS**: Psi(3)=20302,
  Psi(10)=10699667, **Psi(10^4)=34432237 (count 10001)**,
  **Psi(10^6)=20938836 (count 1000001)**, and k=1..60 agree with brute.py.
- This is exactly the captured file the **directive-10 hard gate** requires
  before the Lean arm may run. The gate is now crossed.
- Two-modulus dedup is required (single-modulus undercounts at k=10^6:
  995071 vs true 1000001) — the route as-captured uses it.

Filed as a `status: checked` claim block
(`code/out/verify/directive6-anchors-verified.md`) and stored in Cognee, so
the run need not re-derive or distrust these anchors. Caveat: this verifies
the anchors by the *independent window route*; it is **not** yet the
universal-Euclidean monoid's own output for those k (acceptance steps 4–5 of
`implement-solution`), which remains the open item before k=10^18.

## Contradictions with recalled memory

- The in-memory record of `ueuclid-incontainer-fails-s1s2` ("65 failures") is
  **refuted** by this cycle's analysis; the resolved state is stored so an
  older reading does not resurface and burn a cycle "fixing the compose dU bug".
- No other source contradicted durable memory. The standing slope conflict
  (`steer-d2-literal-slope` holds-here: no) vs the corrected
  F(n-2)/F(n) → 1/φ² is unchanged and stays resolved in favour of the corrected
  slope.

## What the run still lacks

Not a reference gap — the library is saturated. The open item is execution:
`implement-solution` (wire mech_psi formulation B through `code/lib/ueuclid.py`;
reproduce Psi(k) k=1..150 and Psi(10)=10699667; then Psi(10^4/10^6) through the
monoid; then k=10^18 under two Fibonacci approximants). With the anchors now
verified and the LEAN gate crossed, that wiring is the sole critical path.
