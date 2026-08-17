# Librarian cycle report — independent re-verification of a complete library

## Conclusion in one line

The reference library already meets the phase-1 exit test and every standing
REQUEST row is answered by a primary full text on disk. This cycle independently
re-verified that from disk (not from recall), re-confirmed the state of the art
has not moved via live search, and made **no new downloads** — there was no
on-topic primary gap to fill.

## What this cycle did (verified against disk and live web, not memory)

1. **The three standing REQUESTS rows are answered by genuine held full texts.**
   - `full-text-faithful-b96b` (Erdős–Szekeres 1961 lower-bound construction):
     `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`,
     source `https://renyi.hu/~p_erdos/1960-09.pdf`.
   - `balko-valtr-attack-baa4` / `open-access-full-1e6e` (Balko–Valtr SAT attack):
     `research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`,
     source `https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf`. Read in
     full this cycle: refutes the strengthened Peters–Szekeres conjecture
     (cES(7)>32, cES(8)>64 — but all counterexamples are non-pseudolinear, so
     they do NOT touch the geometric ES conjecture), verifies the
     ES-equivalent ETV Conjecture 3.1 over pseudolinear colorings at
     a=4,u=k=7 (N=16) and a=4,u=k=8 (N=22). This is the orientation-variable
     SAT encoding the run's computational arm reproduces against.
   - The `derived/REQUESTS.md` rows still *render* open — a re-derivation
     artifact, not a library gap: the claims-ledger entries carry the `answers:`
     anchors and the claims ledger is authoritative.

2. **Every claim's anchor resolves to a file on disk.** The claims ledger's
   `anchor:` fields all point at real files in `research/sources/` (audited in
   the completeness-audit cycle and spot-re-confirmed here for the ETV,
   Balko–Valtr, 1961, ES-lower, and cup/cap rows).

3. **State of the art has not moved (live search, two targeted queries).**
   - The newest direct ES(7) attack is still Dumitru, "Notes on the 33-point
     Erdős–Szekeres problem", arXiv:2512.24061 (Dec 2025), HELD. ES(7)=33
     remains open; the triple-orientation + 4-set-criterion + convex-layer
     SAT encoding yields UNSAT only for anchored subfamilies.
   - Baek–Balko SoCG 2025 (split k-gons = 2^{k-2}+1 tight; decomposable sets;
     ordered 3-uniform hypergraph generalization fails), HELD.
   - No paper surfaced with a new bound on ES(n) or a new exact value beyond
     ES(6)=17. Suk 2016 (2^{n+o(n)}) and HMPT (2^{n+O(√(n log n))}) remain the
     best asymptotic upper bounds; Tóth–Valtr binomial bound still best of
     binomial form.
   - Baek, "On the Erdős–Tuza–Valtr conjecture", EJC 124:104085 — the journal
     version of the held arXiv:2206.04260 (P(n,4,n)); same mathematics, held.

4. **The canonical reference tier is present with URLs recorded in-file**: ES
   1935 (numdam), ES 1961 (renyi.hu), Peters–Szekeres 2006 (ANZIAM),
   Suk 2017, HMPT 2017, Baek–Balko 2025, Chung–Graham 1998, Kleitman–Pachter
   1998, Tóth–Valtr 1998, Norin–Yuditsky 2016, Vlachos 2015,
   Mojarrad–Vlachos 2015, Morris–Soltan 2000 survey, Balko–Valtr ENDM 2015,
   Heule–Scheucher 2024, Subercaseaux ITP 2024, Scheucher, Aichholzer 2002,
   Duque et al., Károlyi–Tóth 2012, Pór–Valtr 2002, Bárány–Valtr, Damásdi et
   al. 2024, Dumitru 2025, Koshelev–Koshka, PointSAT (Krapivin et al.), SMQH,
   Dumitrescu, Horton 1983, Felsner–Weil 2001, Bergold–Felsner–Scheucher,
   Felsner chirotope-NP, Dobbins–Holmsen–Hubard, Moshkovitz–Shapira,
   Fox–Pach–Sudakov–Suk 2012, Goaoc–Welzl, Lean/Mathlib records, and the
   Wikipedia/MathWorld encyclopedic tiers.

## Documented-but-not-held (re-confirmed; do not re-search)

- **Erdős–Tuza–Valtr 1996, "Ramsey-remainder"** (EJC 17(6):519–532): the
  canonical primary of the ETV enumeration conjecture. Confirmed unobtainable
  in open access (ScienceDirect 403; SZTAKI metadata only). Its content is
  faithfully restated in the held Baek arXiv:2206.04260 (Thm 1.5) and Balko–Valtr.
- **Bonnice 1974 (AMM)** and **Kalbfleisch–Kalbfleisch–Stanton 1970** — ES(5)=9
  primary proofs paywalled; the full Bonnice outline is in the held Morris–Soltan
  survey (Thm 2.7/2.8). Sufficient fidelity second-hand.
- **Pach–Solymosi k-convex chapter** — held only as a MIS-DOWNLOAD stub;
  adjacent problem; the IWOCA-2019 version of the same content is held.
- The MIS-DOWNLOAD quarantine files each have their genuine `correct` sibling;
  none is citable.

## Where the library stands against the run's needs

- **ROOT.md meets GOAL criterion 1**: every upper bound with error term/source,
  the lower construction written concretely, ES(3..6) with methods (Peters–Szekeres
  n=6: signature functions, ~1500 CPU-hours, three independent implementations),
  and ≥3 restricted/partial results (Tóth–Valtr class, decomposable/split
  Baek–Balko, forbidden-order-type Károlyi–Tóth, saturation Damásdi et al.,
  ETV P(n,4,n) Baek, 9-point no-pentagon classification).
- **Oracle foundation**: the 4-point criterion primary, the exact-arithmetic
  checklist, and the ES construction primary all held.
- **Lean arm**: Mathlib `erdos_szekeres` is the monotone-subsequence theorem
  (name collision), so the planar statement must be written from scratch;
  LeanPool CapCup.lean and Subercaseaux ITP held as models.
- **SAT arm**: Balko–Valtr, Scheucher, Dumitru, SMQH, PointSAT, Koshelev–Koshka —
  the full modern landscape of orientation-variable encoders.

## Disposition

No new download is warranted: the canonical tier exists, every standing request
is answered by a genuine primary held on disk, and no on-topic primary gap
surfaced in live search. The next valuable work is **run-side** — the steer-11
gsplit Phase-2 provenance re-capture and the layer-profile conjecture behind it,
which is a computation, not an acquisition.
