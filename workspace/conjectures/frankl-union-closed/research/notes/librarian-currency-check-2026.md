# Librarian currency check — 2026 cycle

What this pass did: re-verified the library's record claims against the live web
(2025–2026), checked the one open request, tried the one recorded source gap
(Poonen 1992) again, and triaged two new claimed-proof surfaces.

## The record is unchanged — confirmed live

Searched 2025–2026 for any new constant or verification bound; nothing
supersedes the store:

- **Published record**: Yu, Entropy 25(5):767 (2023), c ≈ 0.38234
  (arXiv:2212.00658). Claims `published-record-current-verified`,
  `published-status-current`, `published-record-c` all hold.
- **(3−√5)/2 barrier**: peer-reviewed, Alweiss–Huang–Sellke EJC 31(3):P3.35
  (2024), doi:10.37236/12232. Claim `ahs-published-ejc` holds.
- **Cambie** (arXiv:2212.12500, c ≈ 0.3823455): still a preprint (v2 2025-02-16).
- **Liu** (arXiv:2306.08824, c ≈ 0.38271): IEEE CISS 2024 conference, not a
  journal; conditional on numerically-verified hypotheses. No 2025–2026 source
  exceeds ≈ 0.38271 unconditionally.
- Surviving 2025–2026 search hits are already on disk: Colbert (now published,
  Order 43:5 (2026), doi:10.1007/s11083-025-09717-w — held as
  `colbert-chain-conditions-order-2025`), Das–Wu (2412.03862 — held),
  Lu–Raz (2405.10639 — held), Bouchard (2503.00277 — held), Moghaddas Mehr
  (2501.02637 — held).
- **Verification bound consistent**: the Colbert survey's "counterexample has
  |F| ≥ 47" restates Roberts–Simpson with Bošnjak–Marković's q ≥ 12; the
  library's ROOT.md uses the sharper Vučković–Živković q ≥ 13 (computer-assisted
  n ≤ 12) giving |F| ≥ 51. Both sourced; no contradiction.
- The open request `exact-current-published-c8b8` is answered in the claim store
  by `published-record-current-verified` (and the four sibling claims).
- **Poonen 1992 (JCTA 59:253–268) remains unobtainable**: ScienceDirect PDF is
  paywalled (403). This is the library's one recorded source gap; its content
  is represented by the errata (held) and the Bruhn–Schaudt survey's
  restatement of the lattice formulation, Theorem 16, and the two Poonen
  conjectures (held).

## New claimed-proof surface — triaged, NOT added

Two 2026 deposits surfaced that the library does not hold:

1. **Pompetzki, "The Lattice Lock: A Linear-Algebraic Proof of Frankl's
   Union-Closed Sets Conjecture via the Arithmetic Reduction Principle"**
   (Zenodo doi:10.5281/zenodo.18527239, 2026-02-08). Claimed full proof, 0
   citations. **Decision: refuse.** The same author deposited a *verse* version
   of the same "proof" (doi:10.5281/zenodo.18527515) co-credited to a chatbot
   ("Yung Claude, Shouts Out to OG GPT", February 2026, "The Caravan of Linear
   Algebraic Truth"). A claimed proof whose companion artifact is AI-generated
   poetry is not a primary mathematical treatment; adding it would be noise,
   not reference material. The library's claimed-proof audit (Spence 2026) and
   Demontis (2024) notes establish the disposition for this genre: hold, flag
   unaudited, never cite as established — and this one does not even meet the
   hold-bar. If a later pass wants to audit it, the candidate failure points
   are the "Swell Injection Lemma" and the "deficiency form ⟨η, ãη⟩ < 0"
   dichotomy, per the abstract.
2. **Abdurakhmanov, "An Algorithmic Proof of Frankl's Union-Closed Sets
   Conjecture"** (Zenodo doi:10.5281/zenodo.18407784, 2026-01-29). This is a
   re-deposit of the same algorithm whose "Heavy Column Theorem" Spence audited
   and refuted (Prop 3.1/3.4: 5×4 matrix with distinct rows/columns, no all-zero
   column, every column exactly two ones — the row set is not union-closed, so
   the theorem fails as stated and the restricted version carries the
   unresolved combinatorial content). Already covered; no new download.

## Verdict

Library is complete per the operator directive; ROOT.md meets the phase-1 bar
(minimal-counterexample structure, verification bound, settled classes, all
source-anchored). Gathering stays closed. The only remaining gap is Poonen
1992's proof body (paywall), recorded here and in the library report.

```claim
id: pompetzki-lattice-lock-refused
statement: "The Lattice Lock: A Linear-Algebraic Proof of Frankl's Union-Closed
  Sets Conjecture via the Arithmetic Reduction Principle" (Pompetzki, Zenodo
  doi:10.5281/zenodo.18527239, 2026-02-08) is a claimed full proof of UC with
  0 citations, and the same author deposited a verse version of the proof
  (doi:10.5281/zenodo.18527515) co-credited to a chatbot ("Yung Claude (Shouts
  Out to OG GPT)", February 2026). It was triaged and NOT added to the
  reference library: it is not a primary mathematical treatment. Nothing in it
  is cited as established.
hypotheses: curation decision about a deposit, not a mathematical theorem.
holds-here: yes (decision recorded)
status: curation decision (librarian, 2026); refusal reason recorded in this note
bearing: prevents a later role from downloading, citing, or auditing this
  deposit; distinguishes it from the audited human-authored claimed proofs
  (Spence 2026 audits Abdurakhmanov/Schrader; Demontis 2024 held as an
  unaudited claimed proof).
falsifies: if the deposit becomes peer-engaged or the companion verse artifact
  is shown to be unrelated or disowned by the author, the refusal basis weakens.
```