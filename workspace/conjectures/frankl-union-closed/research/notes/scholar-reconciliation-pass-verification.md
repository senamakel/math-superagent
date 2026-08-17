# Scholar reconciliation pass — verification audit of load-bearing claims

Date: this cycle. Role: scholar. Question: which claims the run leans on are
(a) confirmed against their primary source, (b) independently checked, and
(c) consistently stated across stores. The library is mature (61+ sources,
claim blocks broadly in place); this pass audited the active fronts rather
than re-digesting.

Cognee note: `remember_memory` was unavailable for this whole pass (health
check timeout, 3 attempts). The durable records below are all on disk via
claim blocks in notes, which is the path the ledger re-derives from, so
nothing is lost; memory should be re-checked when the server recovers.

## 1. Colbert topological-DCC — upgraded from unchecked to confirmed

- The claim `colbert-topological-dcc` (from the arXiv version
  `research/summaries/colbert-chain-conditions-2412.md`) carried
  holds-here: **unchecked** in the store.
- The journal version of record (Colbert, Order 43:5, 2026,
  DOI 10.1007/s11083-025-09717-w, open access, full text on disk) states it
  as **Theorem 3.21** with the full proof present (lines ~540-560):
  T0 separation, Alexandroff property, Lemma 3.3 (optimal element), Lemma
  3.14 (I_x = {x}), Cor 3.16 (abundance); Cor 3.22 recovers Mehr in the
  finite case. Example 3.23 shows DCC cannot be dropped (the
  {{i,i+1,...}} counterexample — same family the survey cites for infinite
  failure of UC, negative control #3).
- **Action taken**: edited `research/summaries/colbert-chain-conditions-2412.md`
  claim block: added the journal anchor, `follows-from: colbert-order-2026-version-of-record`.
- Result: the recorded boundary of negative control #3 is now confirmed at the
  peer-reviewed source, not merely the preprint.

## 2. Hu–Shi–Zhou density-transfer arithmetic — verified by hand, exact

The transfer identities feeding the abundance-profile thread check exactly
(full derivation in `code/out/hsz_transfer_verify.md`, claim
`hsz-transfer-identities-check`):

- c2 >= 1/(1 + 2(1-c1)/c1): at c1 = 1/2 gives c2 >= 1/3; at c1 = 0.38234
  (record) gives c2 >= 0.23636 ≈ the paper's 0.23635; sanity c1=2/3 gives 1/2.
- Nagel iteration identity 1/(1+2(1-1/(2^{k-1}+1))/(1/(2^{k-1}+1))) = 1/(2^k+1)
  holds symbolically (substitute x = 1/(2^{k-1}+1): 2(1-x)/x = 2(1/x - 1) =
  2(2^{k-1}+1-1) = 2^k). This is the mechanism by which Frankl's level-1 bound
  (1/2) iterates into Nagel's kth-frequency bound — confirming the
  Frankl ⟺ Nagel equivalence (already held via daswu-nagel, now with a second
  independent algebraic route).
- One-element-of-any-k-set bound 1/(2^{|A|-2}+1): |A|=2 → 1/2 (Sarvate–Renaud),
  |A|=3 → 1/3, |A|=4 → 1/5, |A|=5 → 1/9.
- Nagel k=1: 1/(2^0+1) = 1/2 = Frankl exactly.
- The mechanical sympy route (`code/out/hsz_transfer_verify.py`) is written
  but NOT executed (no executor in this scholar role) — the check above is
  hand-arithmetic, recorded honestly as such.

## 3. KPT counterexample corollary — derivation re-checked, sound

`kpt-thm5-counterexample-corollary`: KPT Thm 5(3) f ≥ min{n, 2k−n+1}; a
counterexample has f=0, so min{n, 2k−n+1} ≤ 0; since n ≥ 1 (a nonempty set
exists), n > 0, so 2k−n+1 ≤ 0 ⟹ n ≥ 2k+1. Sound. The corollary is marked
"proved (as a corollary of the sourced theorem)" which is the right status:
it inherits the theorem's proof and adds only this elementary step. Its
corroboration at n≤4 (vacuous: no f=0 empty-free family exists there) is
appropriately labelled vacuous in the claim.

## 4. Consistency checks that PASSED (no contradiction found)

- Gilmer → AHS(3−√5)/2 → Sawin escape → Yu 0.38234 published / Cambie
  0.3823455 preprint / Liu 0.38271 conditional: coherent across the store,
  ROOT.md, CONTEXT.md, and the librarian's live re-checks. Barrier scope (iid
  class only) correctly stated everywhere; `contradiction-sawin-ahs` thread
  records the resolution as a misread, not a contradiction.
- Karpas 2^{n−1} sharpens BBE (2/3)2^n and Eccles (2/3 − 1/104)2^n —
  consistent, Eccles' stability content (a counterexample must be far from the
  near-extremal shape) not contradicted by Karpas.
- spence-minimum-counterexample-odd (|F| odd, freq ≤ k, tight-witness per
  deletion) is compatible with |F| ≥ 4q−1 ≥ 51 and KPT n ≥ 2k+1 — different
  axes (cardinality parity vs. size ratio vs. count bounds).
- odd-filter non-uniqueness (n+1 minimizers) is recorded with its verdict and
  matches `half-density-max-eq-bool-subalgebra` (the correct max-density
  characterisation); no contradiction with the coordinate-wise-false claim,
  which is separately flagged false.
- The `R-uc-with-three-set` refuted verdict is an encoding bug, resolved
  (`three-set-refutation-is-encoding-bug`); R-uc-with-three-set stays open.
  No source in the library claims the 3-set case settled — Ellis–Ivan–Leader
  kills only the "smallest 3-set forces an abundant element in it" route.

## 5. Sources that do not help (audited, closed)

- `vaughan-families-implying-frankl-2002.full.md`: WRONG PAPER (arXiv:math/0208012
  is a differential-geometry paper). Defect recorded via claim
  `vaughan-file-is-defective`; Vaughan's 3-set content is carried by Morris /
  Pulaj / Poonen errata / Bruhn–Schaudt survey, all genuine on disk.
- `demontis-union-closed-set-conjecture-is-true-2024`: a claimed full proof with
  0 citations, 26-day OPAST journal acceptance, no engagement with the entropy
  literature. Filed as unaudited claimed-proof artifact (`demontis-claimed-uc-proof-unaudited`),
  NOT established; nothing in it may be cited as a result. Do not revisit unless
  a later pass audits the specific failing step.
- `eccles-stability-result-2015.full.md` (original): wrong paper in the file;
  corrected body is `eccles-stability-result-2015-html.full.md`; the summary
  records the defect. Read the correct file.

## What the run still lacks (gaps carried forward, not settled here)

- The global-sup Γ̂(1/2) = φ/2 over α > 0 is proved for the α=0 collapsed
  branch only; the sup over α is numerical corroboration, not a theorem
  (`yugamma-half-collapse` open; interval B&B certified 0 boxes).
- Novelty of Γ̂(1/2) = φ/2 unchecked against Yu/Cambie (treat as
  unchecked-novelty, not new).
- The (2,3,7) exact-two-abundant construction existence stays open
  (650k+ family probe found min f=3, but not exhaustive).
- R-uc-with-three-set stays open.

## Durable findings to re-store when Cognee recovers

1. Colbert topological-DCC confirmed at published source (Thm 3.21, Order
   43:5, 2026); claim block updated on disk.
2. HSZ transfer identities hand-verified exact (claim
   `hsz-transfer-identities-check`, `code/out/hsz_transfer_verify.md`);
   mechanical sympy route pending execution.
3. KPT corollary derivation re-checked sound (min{n,2k−n+1} ≤ 0 with n ≥ 1 ⟹
   n ≥ 2k+1).