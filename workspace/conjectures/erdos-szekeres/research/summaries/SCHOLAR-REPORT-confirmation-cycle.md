# Scholar report — confirmation cycle: library verified complete, closures confirmed, one gap outstanding

## What this pass verified (from disk, not from memory)

### 1. The steer-11 gsplit re-capture reproduced exactly — claim promoted to checked

`code/out/gsplit_phase2.captured.txt` (read back this cycle) shows the rotating-line
enumerator `gsplit_enum_definitive.py` re-captured with full provenance:

- Phase 1: N(N−1) exact match vs the 2^N convex-hull-separation oracle at
  N = 8,10,12,14,16, zero missing, zero extra.
- Phase 2 split counts on the verified `es_construct` ES template (both halves of
  size 2^{n-3}, both (n−1)-avoiding): **n=5 → 4, n=6 → 2, n=7 → 0.**
- `EXIT: 0`.

Tasks ledger: `gsplit-enumeration-recheck` closed `done` with the full steer-11
execution (promote claim, retire superseded claim, write scoped Established
finding). Claims ledger: `gsplit-enum-completeness-and-n7-zero` status `checked`,
bearing the scoped statement (splitting-line induction f(n) ≤ 2f(n−1) holds on this
es_construct template through n=6 and fails on it at n=7 — NOT the general G-split
lemma). `gsplit-exhaustive-esconstruct` retired, pointing at
`code/out/gsplit_phase2.captured.txt`. The superseded pair-line counts (57/241/993,
50/222/946, 6/4/2/0) are dead; do not cite.

### 2. The allowable-sequence closure IS in the ledger — nothing was dropped

The steering flagged that scholar/agent-run-79's `record_entry` failed
('unknown tool record_entry') and feared the adjudication payload was lost. It was
not: `read_ledger { ledger: "approaches", query: "allowable-sequence" }` returns
`allowable-sequence-circular-representation` with `status: refuted` and the full
"What closed, and why" text — both load-bearing mechanisms refuted
(reversal-depth = block index is a STRUCTURAL impossibility: constant per-point
reversal count N−1 by the pair-reversal axiom, observed 3,7,15,31 at n=4..7 vs the
binomials; contiguous-block/staircase convexity FALSE in both directions, n=6
62096/64839 agreement with false positives and false negatives), the survivor
(pointwise extreme-in-projection agrees with the exact oracle on every |S|≥4
subset, n=6 64839/64839), and the instruction "Do NOT re-derive depth=block or
contiguous-block convexity." The approaches ledger derives from the approach
file, which carries `status: refuted` and the complete VERDICT
(`research/approaches/allowable-sequence-circular-representation.md`). The
thread `research/threads/allowable-sequence.md` is likewise `status: dead`.

**Process lesson to keep (the steering's second point stands):** when a role's
write is refused for lack of a tool, the content must be handed to a role that
holds the tool or written with `write_document` — never silently abandoned. In
this case the fallback proved unnecessary because the ledger is derived from the
on-disk approach file and had already captured the verdict; a future refusal of
that kind should be followed by an explicit check of the on-disk source, then a
`write_document` fallback only if the content is actually absent.

### 3. Every substantive primary has a claim-bearing digest; no undigested sources remain

Grep for ` ```claim ` across `research/summaries/` (91 files) shows claim blocks in
38 files — all substantive primaries (ES 1935, ES 1961 construction ×2, Tóth–Valtr,
Chung–Graham, Kleitman–Pachter, Norin–Yuditsky, Vlachos, Mojarrad–Vlachos, Suk,
HMPT, Pór–Valtr, Bárány–Valtr, Fox–Pach–Sudakov–Suk, Moshkovitz–Shapira, Morris–Soltan
survey, Baek–Balko SoCG 2025, Baek ETV, Balko–Valtr ENDM 2015, Felsner–Weil,
Felsner chirotope-NP, Hoffman–Merckx, Bergold–Felsner–Scheucher, SMQH, PointSAT,
Koshelev–Koshka, Dumitru, Damásdi et al., Horton 1983, Aichholzer, Duque et al.,
Gärtner, Goaoc–Welzl, GP–Sturmfels, slmath allowable-sequence chapter, Wikipedia
CC-system / ES / Happy-Ending, Mathlib monotone-subsequence, LeanPool, Marić
ES(6)). Files without claim blocks are deliberately non-claim-bearing and are
marked as such: MIS-DOWNLOAD redirect stubs (never cite), encyclopedic pointers
(MathWorld, erdosproblems), framework-only notes (Cardinal–Santos; Dobbins–
Holmsen–Hubard held as abstract page only), abstract-page pointers superseded by a
full-text digest (Goaoc–Welzl, dumitru, heule-scheucher, subercaseaux, scheucher),
and the librarian cycle records (process prose; the two horton claims also sit in
`LIBRARIAN-ACQUISITIONS-HORTON-AND-GAPS.md`).

### 4. Requests are answered; the claims ledger is authoritative

`balko-valtr-attack-baa4` and `open-access-full-1e6e` are answered by
`research/summaries/balko-valtr-A-SAT-attack-on-ES-ENDM2015.md` (claim blocks carry
`answers: balko-valtr-attack-baa4` and `answers: open-access-full-1e6e`);
`full-text-faithful-b96b` by both the 1961 digests (`answers: full-text-faithful-b96b`).
The `derived/REQUESTS.md` rows still rendering open are a re-derivation artifact —
the claims ledger is the record. Documented-but-not-held primaries (ETV 1996,
Bonnice 1974, Kalbfleisch–Stanton 1970) are flagged "do not re-search" with the
faithful second-hand coverage noted.

### 5. State of the art un-moved: ES(7)=33 still open

Dumitru arXiv:2512.24061 (Dec 2025) remains the latest direct attack, UNSAT for
anchored convex-layer subfamilies only. SMQH (no realizable 4-fold-symmetric 32-pt
no-7-gon), PointSAT (200k abstract candidates, none realizable), and Dumitru
together: every computational route reaches 32-point no-7-gon candidates and none
has realized one; none exhausts the abstract space, so none refutes ES(7)=33.

## What is still lacking (the honest tail)

- **Horton machine verification still pending.** `code/out/horton_verify.py`
  (exact integer, `lib.es_geom` oracle, self-tests included) and
  `code/out/horton_verify_HANDOFF.md` exist; `horton_verify.captured.txt` does
  NOT — the handoff to coder has not been executed. Until it runs, claim
  `horton-no-empty-7gon` rests on the source's argument (`status: proved` from the
  primary) and is NOT machine-checked. Adjacent-problem watch applies: the empty
  convex 7-gon is the Erdős–Szekeres–Horton side, kept out of Established.
- **ES(7)=33** remains open; the strongest route per the library is structural
  (split/decomposable forcing, or stability/uniqueness of extremal sets), not
  counting — counting is provably lossy (`ms-cups-caps-tight`), and the abstract
  hypergraph analogue fails (`balko-valtr-refutes-PS`, `baek-balko-weak7-fails`).
- **Baek–Balko Theorem 8 (decomposable sets) stays asserted-by-source** — the SoCG
  2025 PDF defers its proof to JCTA 2026, which this run does not hold. Treat the
  decomposable claim as load-bearing-but-unverified until then.

## Memory store

`remember_memory` calls this cycle and last failed: the memory server's health
check did not answer within 8s, and the tool refuses to accept-and-drop. The
durable findings are on disk:
`research/summaries/LIBRARIAN-confirmation-cycle-library-verified-complete.md` and
this note. Re-store to Cognee once the server recovers — the four-point
verification summary (canonical tier present; requests answered; ES(7) open;
allowable-sequence closure confirmed in ledger) is the payload.

## Bottom line for the run

The library is complete, digested, and internally consistent; the claims ledger
(105 entries) matches the on-disk notes; the steer-11 computation is closed and
promoted; the allowable-sequence closure is confirmed in the ledger. Nothing
remains to acquire. The next valuable work is run-side: (a) execute the Horton
verification handoff (one command), and (b) after that, the scored search under
`code/search/es-nogon` (steer 6) — k=6 rung capping at 16, then ≥50 k=7
candidates on the verified `lib.es_geom` orientation predicate; 32 reproduces
`es_construct`, 33+ refutes ES(7)=33 and must be re-verified independently.