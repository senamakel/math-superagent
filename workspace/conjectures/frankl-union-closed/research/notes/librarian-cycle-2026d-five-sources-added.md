# Librarian cycle 2026d — five primary sources added, Reimer gap made precise

Cycle outcome: five previously frontier-only primary treatments are now in the
library with full bodies, indexed, and digested into claim blocks; the one
remaining primary-text gap (Reimer 2003) was confirmed unobtainable and
recorded precisely. The published-record and verification-bound rows were
re-confirmed stable by the on-disk 2026 audits; nothing here moves the constant.

## Added (all previously absent; each with source URL in the file)

1. **Marković, "An Attempt at Frankl's Conjecture"** (Publ. Inst. Math.
   81(95):29–43, 2007; DOI 10.2298/PIM0795029M).
   `research/sources/markovic-attempt-frankl-2007.full.md` (45 KB, from
   https://people.dmi.uns.ac.rs/~markovicp/papers/2007-Frankl10.pdf).
   Proves UC for |⋃F| ≤ 10; multi-weight (simultaneous Poonen weights) method;
   author explicitly says it "will most probably not prove the whole
   conjecture". Claims: `markovic-uc-holds-n10`, `markovic-multi-weight-technique`.

2. **Czédli, "On averaging Frankl's conjecture for large union-closed-sets"**
   (JCTA 116:724–729, 2009; DOI 10.1016/j.jcta.2008.08.002).
   `research/sources/czedli-averaging-large-union-closed-2009.full.md` (22 KB,
   from the author's submitted version:
   https://www.math.u-szeged.hu/~czedli/m/publ.pdf/czedli_on-averaging-Frankl's-conjecture-for-large-union-closed-sets.pdf).
   **Averaged Frankl property** for n=|F| ≥ 2^m − 2^(m/2): Σ_a(n−2s(a)) ≤ 0;
   lattice proof via P(X)/θ representation, excess e([u])=|[u]|−1, height bound
   h([u]) ≤ m/4−1 for abundant classes. Claims: `czedli-averaged-frankl-large-families`,
   `czedli-lattice-averaged-large`. This is the primary for the "|F| close to
   2^m" threshold row and the sibling of the on-disk Czédli–Maróti–Schmidt
   averaging-limits paper.

3. **Raz, "Note on the union-closed sets conjecture"** (EJC 24(3):#P3.53,
   2017; DOI 10.37236/6989).
   `research/sources/raz-note-union-closed-2017.full.md` (12 KB, from
   https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p53/pdf/).
   Disproves Balla/Gowers' Conjecture 3: Reimer's Condition 1 (filter +
   bijection A↦F_A with A⊆F_A and disjoint intervals [A,F_A]) does NOT force an
   abundant element; explicit counterexample on [8] with |A|=11, each element
   in ≤ 5 sets; n ≥ 8 necessary (digraph/tournament argument). Claim:
   `raz-reimers-condition-insufficient`. This is the primary of the
   Lu–Raz 2024 note already on disk (`lu-raz-reimer-note-2024.full.md`).

4. **Pulaj–Raymond–Theis, "New Conjectures for Union-Closed Families"**
   (EJC 23(3):#P3.23, 2016; DOI 10.37236/5749).
   `research/sources/pulaj-raymond-theis-new-conjectures-2016.full.md` (46 KB,
   from https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i3p23/pdf).
   IP reformulations (2a upper bound / most-frequent count), optimal values
   observed independent of n, new conjectures proved NOT equivalent to Frankl.
   Claim: `pulaj-raymond-theis-ip-reformulation`. Companion to the on-disk
   cutting-planes and local-configurations papers by Pulaj.

5. **Moghaddas Mehr, "A Note on the Union-closed Sets Conjecture"**
   (arXiv:2309.01704v3, 2023).
   `research/sources/moghaddas-note-uc-2023.full.md` (17 KB, from
   https://arxiv.org/pdf/2309.01704).
   Binary-matrix translation of UC; closure under material conditional
   (¬M_i ∨ M_j) yields a column with ≥ n/2 ones (weaker relaxation, does NOT
   settle UC). Claim: `moghaddas-material-conditional-bound`. Cited 3× by
   on-disk sources (bouchard-2511, colbert-2412, moghaddas-2025).

## Indexing and claims

- All five full texts indexed (`index_document`): searchable by
  `search_documents`.
- Six claim blocks written into their summaries and confirmed in the store via
  `search_claims` (markovic-uc-holds-n10, markovic-multi-weight-technique,
  czedli-averaged-frankl-large-families, czedli-lattice-averaged-large,
  raz-reimers-condition-insufficient, pulaj-raymond-theis-ip-reformulation,
  moghaddas-material-conditional-bound).
- research/ has no INDEX.md by design (research is recalled via Cognee; no
  parallel index per instructions).

## Not obtainable, recorded precisely

- **Reimer, "An Average Set Size Theorem", CPC 12(1):89–93 (2003)** — the
  primary of the averaging line. Confirmed: Cambridge Core paywalled; Semantic
  Scholar `openAccessPdf` status CLOSED (checked via the Graph API); no arXiv
  copy; no author deposit found. The DOI landing page was downloaded as
  `research/sources/reimer-average-set-size-2003.trial.full.md` — **abstract
  only, NOT the primary text; do not cite it as the proof**. The theorem and
  Condition 1 are on disk through Raz's restatement (new this cycle) and the
  Bruhn–Schaudt survey Thm 21 + up-compression outline, but Reimer's own proof
  that union-closure implies Condition 1 is not in the library.
  `request_research` declined to queue this as a gap because 8 claim blocks
  bear on Reimer's theorem — but those claims carry the *restatements*, not the
  primary proof, so the gap is real even though the run's claims cover the
  theorem's content. Recorded here so a future pass with a working request
  queue (or a different source, e.g. an institutional scan) knows exactly what
  is missing.
- **Hachimori–Kashiwabara, "Several minimality concepts…", Graphs Combin.
  40(6):130 (2024)** — already tracked as `hak-minimality-concepts-2024-paywalled-gap`
  (paywalled, no arXiv; the on-disk `.biblio` file is the author's publication
  page, not the paper). Not re-searched.

## Memory server status

`remember_memory` failed throughout this cycle (10 failures; the memory server
did not answer its health check). Per tool direction, the durable record is
this note on disk instead. If the server recovers, store: "Librarian cycle
2026d added Marković 2007, Czédli 2009 (averaged-Frankl large families),
Raz 2017 (Reimer Condition 1 insufficiency), Pulaj–Raymond–Theis 2016,
Moghaddas 2023 to research/sources with six claims; Reimer 2003 primary proof
remains a precise registered gap (paywalled, no OA)."

## Frontier audit (top rows vs on-disk)

Re-checked the frontier's most-cited rows against the sources directory: all
remaining top candidates (Knill math/9409215, Bruhn–Schaudt, Gowers polymath,
AHS/Cambie/Liu DOIs, Wikipedia) were already on disk. This cycle's five
additions were the items cited ≥2× by the library's own sources that were NOT
yet primary-held (Marković, Czédli JCTA, Reimer, Hachimori–Kashiwabara GCOM,
Pulaj–Raymond–Theis, and the JCTA 1998/2012 rows). Reimer and Hachimori–
Kashiwabara remain unobtainable as full texts; everything else is now primary.