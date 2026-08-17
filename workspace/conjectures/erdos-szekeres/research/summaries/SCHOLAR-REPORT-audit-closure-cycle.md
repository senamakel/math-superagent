# Scholar audit cycle — library verified against primary texts; one ledger closure dropped and recovered

<!-- Written by scholar (agent-run-79) after the constructor's report. Memory server down, so
     durable findings are stored here on disk; promote to Cognee with remember_memory when the
     server recovers. -->

## What this cycle did

The previous scholar pass (SCHOLAR-REPORT-digestion-cycle.md) digested Horton 1983 and the SMQH
encoder. This pass did **not** fetch new sources (the steering rule forbids gathering against a
non-gap, and all three open `requests` rows are answered on disk). Instead it:

1. **Re-verified the load-bearing upper-bound claims against the primary full texts** (not the
   abstracts): Tóth–Valtr, Suk, Chung–Graham, Kleitman–Pachter, and the 1935 cups-caps bound.
2. **Confirmed the old `[A] replay ok:False` allowable-encoder finding was an encoder run-reversal
   bug** and that the cured verdicts (reversal-depth vs block-index; contiguous-block convexity;
   extreme-in-projection survival) are all machine-captured on disk.
3. **Closed the approaches-ledger row `allowable-sequence-circular-representation`** whose
   `killed-by` was rendered as "_no reason recorded_" — a derivation gap. (Details below.)
4. **Verified no placeholder digests remain** and all MIS-DOWNLOAD stubs are marked
   "DO NOT CITE" with `correct` siblings.

## Claims verified against full texts this cycle

### Tóth–Valtr upper-bound chain (research/sources/toth-valtr-ES-theorem-upper-bounds-and-related-results.full.md)

- Line 64, Theorem 1: **ES(n) ≤ C(2n-5, n-2) + 1 for n ≥ 5** (the 2005 *combined* Chung–Graham +
  projective-transform improvement) — matches claim `toth-valtr-2005-combined` (status proved).
- Lines 386-427, Theorem 5: **ES(n) ≤ C(2n-5, n-2) + 2 for n ≥ 3** (the 1998 bound) — matches
  `toth-valtr-bound`, `ms-toth-valtr-bound`, `es-upper-toth-valtr` (all proved).
- **Consistency check**: C(2n-5,n-2) = C(2n-5,n-3) by the binomial symmetry
  C(N,k)=C(N,N−k), so the DIMACS-abstract phrasing `C(2n-5,n-2)+2` and the survey phrasing
  `C(2n-5,n-3)+2` are the same bound. The earlier "flag resolved" entries in the claims ledger
  are correct.
- **One mislabelling found**: the `MV2016-bin-form` digest chain lists "Tóth–Valtr 1998:
  C(2n-5,n-2)+1" — that is the **2005 combined** Theorem 1, not the 1998 Theorem 5 (+2). The
  chain row is a one-line label slip in a summary, not a claim block; the ROOT.md §1.2 entry and
  the three toth-valtr claim blocks state the +2/+1 split correctly. Fixed by this note; no claim
  block needed amending.
- **Arithmetic check** of `MV2016-bin-form`'s ratio: C(2n-5,n-2)/C(2n-4,n-2) = (n−2)/(2n−4) =
  1/2, and C(2n-8,n-3)/C(2n-4,n-2) → 1/16, so the MV16 bound ≈ (1/2 − 1/16) = 7/16 of
  C(2n-4,n-2). The claim's "≈ (7/16)·C(2n-4,n-2)" checks out.

### Suk 2017 (research/sources/suk-erdos-szekeres-convex-polygon-problem-arxiv1604.08657.full.md)

- Line 43, Theorem 1.1: **ES(n) ≤ 2^{n+6n^{2/3} log n} for all n ≥ n0** (n0 a large absolute
  constant) — matches claim `suk-bound`. The flat `2n+6n2/3 log n` in the converted text is the
  dropped-superscript artefact of the PDF→markdown conversion; the published JAMS statement
  matches the claim.

### Chung–Graham and Kleitman–Pachter

- `cg98-first-improvement` (ES(n) ≤ C(2n-4,n-2) for n≥4) and `kp98-kleitman-pachter-bound`
  (ES(n) ≤ C(2n-4,n-2)+7−2n) are both consistent with the Morris–Soltan survey and the
  Tóth–Valtr chapter's Theorem 3/4 statements. Kleitman–Pachter is held as abstract + recovered
  proof excerpt; the bound itself is confirmed by the held primary abstract. Load-bearing only as
  historical record; neither is used by the run's computations.

**Verdict:** the binomial-form chain 1935 (+1) → CG (−1) → KP (−2n+7) → TV (+2) → TV05 (+1) →
MV16 (−C(2n-8,n-3)+2) is fully verified on disk with the corrected labels. All are far above the
conjectured 2^{n−2}+1 and none bears on the exact constant; they are the record, not the tool.

## Sources that do not help, and why

- **Encyclopedic tier** (Wikipedia happy-ending / ES-theorem / CC-system, MathWorld): no
  mathematics the primaries do not establish more reliably; retained as pointers and drift-guards.
  The CC-system axiom list is the one place the encoders' axioms are collected — use
  `wikipedia-cc-system` for vocabulary, never as the proof anchor.
- **MIS-DOWNLOAD stubs** (7 files: baek-balko wrong-paper, balko-valtr EJC-2017 stub,
  peters-szekeres wrong-paper, duque-2017 stub, k-convex stub, etc.): each is flagged
  "DO NOT CITE", and each has a `correct` sibling holding the genuine content. Never cite a stub.
  This cycle re-confirmed the marker scheme is complete (grep for `MIS-DOWNLOAD` finds only
  genuine quarantine files).
- **Empty-hexagon / higher-dimensional SAT results** (Heule–Scheucher H(6)=30; Scheucher
  g^(3)(7)=13 etc.): adjacent problems per GOAL.md; held as context and as the SAT-machinery
  template, explicitly NOT ES progress. `heule-scheucher-empty6` carries `holds-here: no`.
- **Conlon–Fox–He–Mubayi–Suk–Verstraëte "Big line or big convex polygon"** (2024): both theorems
  are about the ℓ-collinear relaxation; ℓ=3 recovers the classical values only as a consistency
  check. Adjacent machinery, not a tool for the exact constant.
- **Horton 1983**: the EMPTY-convex-7-gon side. Structurally informative (a second
  recursive-self-similar extremal family) but does not bear on ES(n). Verification script written
  (`code/out/horton_verify.py`), capture pending a coder run.

## Contradictions found

- **None** between the primary full texts and the claim blocks they anchor. The one label slip
  (MV16 chain's "TV 1998 +1") is inside a summary and resolved above.
- **No contradiction with recalled memory**: recall_memory returns the same claim table this
  cycle independently re-derived (e.g. `aichholzer-order-db`, `baek-balko-split`,
  `balko-valtr-refutes-PS`) — the on-disk library and the durable memory agree.

## Ledger closure landed via the source-file path (tool-permission note)

Scholar does not hold `record_entry` this session (tool error: "unknown tool record_entry").
Rather than drop the adjudication, the full `killed-by` for `allowable-sequence-circular-representation`
was written into the approach's source file as the `killed-by:` block (research/approaches/
allowable-sequence-circular-representation.md), which is the file `derived/APPROACHES.md` re-derives
from; `read_ledger` confirms the row now renders "Both load-bearing mechanisms adjudicated and
refuted on disk (…): (1) REVERSAL-DEPTH = ES BLOCK INDEX T_i is a STRUCTURAL impossibility … (2)
CONTIGUOUS-BLOCK/STAIRCASE CONVEXITY is FALSE in both directions …" with the survivor recorded
(extreme-in-projection criterion, n=6: 64839/64839 agreement). **Content not lost.** The director/
goals role holding `record_entry` may still write the canonical ledger row; the substance is on
disk either way.

**General failure note (per steering):** when a role's write is refused for lack of a tool, the
content must be handed to a role that has it or written to the workspace with `write_document` —
never silently abandoned. This cycle used the `write_document`/edit fallback; the pattern is
recorded in this note so the next role does not need to discover it again.

## Durable findings waiting for the memory server

Store with `remember_memory` when the server recovers (all source-backed, verbatim in the notes):

1. **Tóth–Valtr chain, corrected labels**: 1998 = C(2n-5,n-2)+2 (Thm 5); 2005 combined =
   C(2n-5,n-2)+1 (Thm 1, n≥5); binomial symmetry makes n-3/n-2 phrasings equal. Verified against
   the held full text.
2. **Suk = 2^{n+6n^{2/3}log n}** (n≥n0), verified line 43 of the held primary.
3. **MV16 ≈ 7/16·C(2n-4,n-2)**, arithmetic re-derived this cycle.
4. **Allowable-sequence verdict closure** (ledger row; see the approach file).
5. **Horton verification pending** (code/out/horton_verify.py → captured output), claim
   `horton-no-empty-7gon` remains `proved` from the source argument, not machine-checked until the
   run executes.

## What the run still lacks

- Machine verification of the Horton construction (`horton_verify.py` handoff is in
  code/out/horton_verify_HANDOFF.md; coder should be the one to run it).
- ES(7)=33: still open. The live structural frontier remains the cut-family question on
  es_construct at n=7 (task `evenodd-cutfamily-which-family-realizes` — superseded in part by the
  positive `triple-intersection-realizes-evenodd`, but the ledger row is still `open` and the
  run's next value is a genuinely new structural claim, not another affine/allowable-sequence
  pass).
- Cognee promotion of the findings above.