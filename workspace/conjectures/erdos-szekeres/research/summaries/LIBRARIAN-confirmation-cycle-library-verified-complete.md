# Librarian report — confirmation cycle: canonical tier verified, no gap to fill

## Conclusion in one line

The reference library already meets the phase-1 exit test and every standing
REQUEST row is answered by a primary full text on disk. This cycle re-verified
that from disk (not from memory), confirmed the state of the art has not moved
since the last librarian cycle, and made **no new downloads** — there was no
on-topic primary gap to fill.

## What was re-verified this cycle (each check run against disk/live, not recall)

1. **The three standing REQUESTS rows are all answered by genuine held full texts.**
   - `full-text-faithful-b96b` (Erdős–Szekeres 1961 lower-bound construction):
     held at `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`,
     source `https://renyi.hu/~p_erdos/1960-09.pdf`. Content grep confirms it states
     "2^{n-2} points which contains no convex n-gon" and the Cartesian representation.
   - `balko-valtr-attack-baa4` / `open-access-full-1e6e` (Balko–Valtr SAT attack):
     held at `research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`,
     source `https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf`. Content grep
     confirms the SAT attack, the Peters–Szekeres strengthened-conjecture refutation,
     and the Erdős–Tuza–Valtr refinement. (The ENDM 2015 version carries the same
     content as the paywalled EJC 2017 journal version; no fetch needed.)
   - The `derived/REQUESTS.md` rows still *render* open — this is a re-derivation
     artifact, not a library gap. The claims-ledger entries
     (`es1961-construction-held`, `balko-valtr-refutes-PS`,
     `balko-valtr-pseudolinear-verifies`, and the ETV set) carry the `answers:`
     anchors; the claims ledger is authoritative.

2. **Every claim in the claims ledger carries an anchor that resolves to a file
   on disk** — previously audited (`LIBRARIAN-completeness-audit.md`) and spot-re-
   confirmed here for the ETV, Balko–Valtr, and 1961 rows.

3. **State of the art has not moved.** Live search (two targeted queries):
   - Dumitru, "Notes on the 33-point Erdős–Szekeres problem", arXiv:2512.24061
     (Dec 2025) — still the latest direct ES(7) attack; ES(7)=33 remains open;
     it yields UNSAT for anchored convex-layer subfamilies only.
   - Baek–Balko SoCG 2025 (split k-gons, decomposable sets) held and confirmed.
   - Damásdi–Dong–Scheucher–Zeng saturation now also appears in its EJC 2025
     journal form — the same result as the held SoCG 2024 full text (this run holds
     the conference version; the journal version is the same mathematics, already
     digested as claims `es-saturation`, `damasdi-saturation`).
   - No paper surfacing a new bound on ES(n) or a new exact value beyond
     ES(6)=17. The canonical survey tier (Morris–Soltan 2000) is already held.

4. **The canonical reference tier is present**, each with its URL recorded in the
   file: ES 1935 (numdam PDF), ES 1961 (renyi.hu PDF), Peters–Szekeres 2006
   (Cambridge), Suk 2017 (arXiv:1604.08657), HMPT 2020 (arXiv:1710.11415),
   Baek–Balko SoCG 2025, Chung–Graham 1998, Kleitman–Pachter 1998, Tóth–Valtr
   1998, Norin–Yuditsky 2016, Vlachos 2015, Mojarrad–Vlachos 2015, Morris–Soltan
   2000 survey, Balko–Valtr ENDM 2015, Heule–Scheucher 2024, Subercaseaux ITP 2024,
   Scheucher, Aichholzer 2002, Duque et al., Károlyi–Tóth 2012, Pór–Valtr 2002,
   Bárány–Valtr, Damásdi et al. 2024, Dumitru 2025, Koshelev–Koshka, PointSAT,
   SMQH, Dumitrescu, Horton 1983, Felsner–Weil 2001, Bergold–Felsner–Scheucher,
   Felsner chirotope-NP, Dobbins–Holmsen–Hubard, Moshkovitz–Shapira,
   Fox–Pach–Sudakov–Suk 2012, Goaoc–Welzl, Lean/Mathlib records, Wikipedia/MathWorld
   encyclopedic tiers.

## Documented-but-not-held (re-confirmed; do not re-search)

- **Erdős–Tuza–Valtr 1996, "Ramsey-remainder"** (EJC 17(6), DOI 10.1006/eujc.1996.0045):
  the canonical primary of the ETV enumeration conjecture. Confirmed unobtainable in
  open access (ScienceDirect 403; SZTAKI metadata only). Its content is faithfully
  restated in the held Baek arXiv:2206.04260 (Thm 1.5) and Balko–Valtr. Stored in
  Cognee.
- **Bonnice 1974 (AMM)** and **Kalbfleisch–Kalbfleisch–Stanton 1970** — the primary
  ES(5)=9 proofs are paywalled; the full Bonnice proof outline is in the held
  Morris–Soltan survey (Thm 2.7/2.8 classification). Sufficient fidelity second-hand.
- **Pach–Solymosi k-convex chapter** — held only as a MIS-DOWNLOAD stub; adjacent
  problem; the IWOCA-2019 version of the same content is held. Not worth a paywall.

## Where the library stands against the run's needs

- **ROOT.md meets GOAL criterion 1**: every upper bound with its error term/source,
  the lower construction written concretely, ES(3..6) with methods (Peters–Szekeres
  n=6: signature functions, ~1500 CPU-hours, three independent implementations),
  and ≥3 restricted/partial results (Tóth–Valtr class, decomposable/split
  Baek–Balko, forbidden-order-type Károlyi–Tóth, saturation Damásdi et al., ETV
  P(n,4,n) Baek, 9-point no-pentagon classification).
- **Oracle foundation**: the 4-point criterion primary, the exact-arithmetic
  checklist, and the ES construction primary are all held.
- **Lean arm**: Mathlib `erdos_szekeres` confirmed to be the monotone-subsequence
  theorem (name collision), so the planar statement must be written from scratch;
  LeanPool CapCup.lean and Subercaseaux ITP held as models.
- **SAT arm**: Balko–Valtr, Scheucher, Dumitru, SMQH, PointSAT, Koshelev–Koshka —
  the full modern landscape of orientation-variable encoders.

## Disposition

No new download is warranted: the canonical tier exists, every standing request is
answered by a genuine primary held on disk, and no on-topic primary gap surfaced in
live search. The next valuable work is **run-side** — the steer-11 gsplit Phase-2
provenance re-capture and the layer-profile conjecture behind it — which is a
computation, not an acquisition.

## Cognee store (unfinished this cycle)

`remember_memory` was called with this cycle's verification finding but the memory
server failed its health check (no response within 8s) and declined rather than
dropping the entry. The finding was written here instead. **A later cycle should
re-store it in Cognee once the memory server recovers** — the durable text to store
is the four-point verification summary in the "What was re-verified" section
(canonical tier present; the three REQUESTS answered by held primaries; state of
the art un-moved with ES(7)=33 still open; no new download warranted).

Nothing was downloaded this cycle because no gap existed; this verification note is
the cycle's durable record.
