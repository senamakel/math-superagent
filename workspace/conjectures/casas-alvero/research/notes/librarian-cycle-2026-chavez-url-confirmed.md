# Librarian cycle — frontier closed, Chávez URL confirmed, Peinado abstract captured

Date: this cycle. State of the library: **comprehensive and current through the
2026 record**; the top of `derived/FRONTIER.md` (all rows with cited-by ≥ 3) is
already held in full text, verified by grep against `research/sources/` for
every lead (2312.08742, 1705.01704, 1208.5404, math/0605090, Draisma–de Jong
EMS survey, de Jong 2011, W1579326781, Polstra RHUMJ).

## What this cycle changed (three durable items)

### 1. Chávez Martínez 2018 thesis — CONFIRMED direct PDF URL (new)

The single still-unchecked claim in the library
(`chavez-martinez-2018-fixed-roots`, unchecked, asserted-by-abstract) is the
Chávez 2018 UCrea thesis. All prior cycles documented `repositorio.unican.es`
and `hdl.handle.net/10902/15246` as network-blocked; **this cycle the
`read_sources` triage instrument succeeded on the same pages where
`download_document` fails, proving the exact PDF bitstream exists and reading
its metadata**:

`https://repositorio.unican.es/xmlui/bitstream/handle/10902/15246/Chavez%20Martinez%20Yemile%20del%20Socorro.pdf?sequence=1&isAllowed=y`
(421 Kb; confirmed by the triage read, which also re-confirmed the 302/627
degree-20 result, the "2 and 3 distinct roots" char-0 proof, the Gröbner-basis
of-top-k-derivatives method, and the tropical-geometry closing example).

`download_document` on that exact URL still fails at the network layer, and
`read_sources` will not parse a raw PDF — so the **full text remains
unobtained this run**, but the confirmed URL is now in the note
(`research/notes/chavez-martinez2018-fixed-roots-thesis.md`) so a later pass
(or a separate network path) needs zero re-discovery. The claim's `unchecked`
status is unchanged and correct: nothing quotable beyond the abstract is held.

### 2. Peinado Asensi 2018 (UPV master's, "La Conjetura de Casas-Alvero") — abstract captured

Newly found and downloaded from `investmat.webs.upv.es` (primary hosted by the
UPV mathematical research group). The PDF conversion retained only the title
page + abstract (873 bytes) — the body did not convert. Content: a didactic
exposition (CA statement, known low-degree results, an equivalent simplified
statement, counterexamples under relaxed hypotheses); **no new theorem** — it
is a lecture note, not a research advance. Held as
`research/summaries/peinado2018_la-conjetura-casas-alvero.md`. Marginal value;
kept for the record, low priority to upgrade.

### 3. Chávez bitstream URL recorded in the workspace note (edit)

Updated `research/notes/chavez-martinez2018-fixed-roots-thesis.md` from
"full text NOT obtainable" to "full text NOT obtainable THIS RUN,
direct bitstream URL confirmed" with the exact URL and the `?show=full`
alternate. The note's "do not re-attempt" applies to *this run's* network
path, not forever.

## Re-confirmed (no change, cheap checks)

- **Ghosh claimed proof (arXiv:2501.09272)**: still an unverified preprint
  (v2 21 Mar 2026 "Major revisions"); citation graph empty; CA remains open;
  smallest open degree = 20. The AJM acceptance covers only the *finiteness*
  result (arXiv:2402.18717), not the full proof. (Held: ghosh2025_proof_*,
  uw-news, uw-seminar, scholar-digest-assessment.)
- **2026-01+ arXiv sweep**: only held works reappear (Ghosh ×2, Schaub–
  Spivakovsky ×4, GvB, Castryck, Massri, Laterveer–Ounaïes, Wikipedia). No
  new settled degree, no published refutation, no independent verification.
- **Diaz-Toca & Gonzalez-Vega 2006/2005 origin** (verification d≤7): still
  not digitised, claim doubly corroborated by held Draisma–de Jong survey and
  Castryck et al. — already documented, not chased further.
- **Integrity markers in place**: the two wrong-paper fetches
  (1010.2358 Campagna–Pagh; 1010.2667 Guo–Zhang) are clearly marked
  NOT-A-SOURCE and the true Abdesselam–Chipalkatti (arXiv:1203.4761) is held
  and verified. No claim cites a wrong-content file (trace: claim
  `abdesselam-chipalkatti-file-mislabel-corrected`).

## Requests ledger

`derived/REQUESTS.md` has never rendered — nothing has been written to it in
prior cycles. The one genuine gap (Chávez full text) is described exactly in
the workspace note with a falsifier and the confirmed URL; `request_research`
correctly declined to duplicate it because the 8 existing claims already
carry the abstract-level content. The fetch gap itself is a network-access
fact, not a knowledge gap: recorded in the note, recoverable by any run with
reach to UCrea.

## Verdict

Nothing further to add this cycle. The library's canonical tier, survey tier,
computational-attack tier, char-p witness tier, claimed-proof tier, and
Abel–Gontcharoff/u-resultant toolchain tier are all held in full text; the
frontier top is worked; the single unchecked claim has a confirmed fetch
target and an exact falsifier recorded. Next cycle: re-check UCrea reachability
for the Chávez bitstream URL; otherwise re-run the 2026-now arXiv sweep for a
status change on the Ghosh claim.