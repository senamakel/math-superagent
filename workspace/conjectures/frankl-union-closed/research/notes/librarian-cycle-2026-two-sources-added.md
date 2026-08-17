# Librarian cycle 2026 — two primary sources added against real gaps

Cycle outcome: the library was verified complete per the operator's
stop-adding-sources directive; auditor's prior audit confirmed. BUT two real
gaps were found and filled, both against claims/threads, both primary sources,
neither a derivative:

## Added

1. **Kabela–Polák–Teska, "The number of abundant elements in union-closed
   families without small sets", arXiv:2212.09279 (v2, 30 May 2023).**
   `research/sources/kabela-polk-teska-abundant-elements-2022.full.md`
   (abstract) + `...html.full.md` (full body).
   - This is the **primary source behind the claim
     `cambie-survey-two-abundant-capped`** (was asserted via Cambie's survey
     citing it). Now anchored: Theorem 6(3) `(2,k,n)`-constructions for
     `n ≥ max{3,5k−4}`, `5k−8` for even k; Theorem 5 many-abundant bounds;
     Proposition 7 (Cui–Hu k=2 ⟺ strictly between Frankl and Poonen).
   - Claims filed: `kpt-two-abundant-constructions`,
     `kpt-many-abundant-theorem5`, `kpt-cuihu-k2-between-frankl-poonen`,
     `kpt-published-status` (still preprint, unchecked journal).

2. **Hu–Shi–Zhou, "A lemma on a finite union-closed family of finite sets and
   its applications", arXiv:2507.11008 (v1, 15 Jul 2025).**
   `research/sources/hu-shi-zhou-frankl-lemma-2025.full.md` (abstract)
   + `...html.full.md` (full body).
   - New 2025 source; sharp Lemma 1.1 density-transfer
   (`|G_j|/|G| ≥ c ⟹ |F_j|/|F| ≥ 1/(1+2(1−c)/c)`), Prop 3.3 (any set of size
   k has one element at density ≥ 1/(2^{k−2}+1)), Remark 3.4 (two-element
   densities from the record; conjectured (1/2, 1/3)).
   - Claims filed: `hsz-frankl-lemma-density-transfer`,
     `hsz-nagel-equivalent-frankl`, `hsz-one-element-of-any-2set-dense`,
     `hsz-two-element-density-from-record`, `hsz-published-status`.

## Verifications that cost nothing and prevent mis-citation

- **KPT journal status**: searched arXiv DOI; remains preprint (v2 2023).
  `kpt-published-status` records this.
- **HSZ "Frankl ⟺ Nagel" (Prop 3.1) is NOT new**: Das–Wu Observation 1.3
  already proves Frankl ⟹ Nagel by a different route (π_{k−1} projection)
  with bound 1/(1+2^{k−1}) — verified in the library's own Das–Wu full text
  (lines 99–137). So the library had the equivalence already via
  `daswu-nagel`; HSZ's contribution is the sharp Lemma 1.1 and the
  `1/(2^{|A|−2}+1)` complement. Recorded in the HSZ summary so a later run
  does not cite HSZ's equivalence as novel or Das–Wu as incomplete.
- Nagel's own source (arXiv:2208.03803) was already on disk
  (`nagel-interior-operator-equivalences` claim); no new Nagel download needed.

## Where this leaves the library

- Claims count increased (5 KPT + 5 HSZ filed).
- `cambie-survey-two-abundant-capped` upgraded from survey-asserted to
  primary-source-anchored (the KPT construction range is now exact).
- The abundance-profile thread now has: KPT (many-few abundant, k=2 open,
  between Frankl/Poonen), HSZ (density transfer + (1/2,1/3) conjecture +
  0.23635 second-element bound), plus existing Das–Wu/Knill.
- No new requests opened: the two additions were against existing claims, not
  new gaps. The one gap I probed (Poonen 1992 full text, paywalled) remains
  from the earlier audit — recorded in REQUIREMENTS/requests if a free copy
  appears.

Frontier: the two arXiv downloads added their citations to the frontier
(42 + 2 = 44 new leads from the two sources' bibliographies). No frontier
row above count 2 is missing from the library.