# Colbert, "Chain Conditions and Optimal Elements in Generalized Union-Closed Families of Sets" — summary

**Source:** Cory H. Colbert. *Order* 43, article 5 (2026). Published online 2025-12-08. Open access (CC BY 4.0).
**DOI:** https://doi.org/10.1007/s11083-025-09717-w
**Version of record on disk:** `research/sources/colbert-order-2026-openaccess.full.md` (downloaded from https://link.springer.com/content/pdf/10.1007/s11083-025-09717-w.pdf, 40 KB)
**arXiv version also held:** `research/sources/colbert-chain-conditions-2412.full.md` (arXiv:2412.17138) and related `colbert-chain-conditions-generalized-uc-2025.full.md`, `colbert-chain-conditions-order-2025.full.md`.

## What it establishes

The union-closed sets conjecture is known to be **false for arbitrary infinite families** (the survey's example `{{i,i+1,i+2,…}}`); this paper recovers positive results for infinite families under chain conditions, and gives new finite results:

- **Lemma 3.1** — a family satisfying ACC is closed under finite unions iff closed under arbitrary unions.
- **Lemma 3.3 / Corollary 3.5** — if `(F,⊆)` satisfies DCC (descending chain condition) and `a ∈ ∪F`, then there is an *optimal* element `b ∈ ∪F` with `F_a ⊆ F_b`; every finite-dimensional union-closed family is closed under arbitrary unions and has an optimal element.
- **Lemma 3.7** — if `(F,⊆)` satisfies DCC and for every inclusion-minimal `A ∈ F∖F_x`, `A∪{x} ∈ F`, then `x` is abundant. This is the main abundance-detection tool.
- **Proposition 3.9 / Theorem 3.17** — every union-closed family of dimension at most one has every element abundant (Prop 3.9); **every union-closed family of dimension two has an abundant element** (Thm 3.17). ("Dimension" = maximum, over chains, of (chain length − 1).)
- **Lemma 3.14 / Corollary 3.16** — a new proof that a family containing a singleton has that element abundant (with an injection `F∖F_x → F_x`).
- **Lemma 3.11** — if `x` is optimal in a separating family, then the intersection of all members containing `x` is `{x}`; in particular `∪F = A ∪ {x}` for any `A ∉ F_x` with `A∪X = ∪F` for all `X ∈ F_x`.
- **Theorem 3.21 / Corollary 3.22** — any topological space satisfying DCC on its open sets (in particular any finite space), `τ ≠ {∅}`, has an abundant open set.
- **Theorem 4.3 / Corollary 4.4** — a dominance condition on a family `T` ("α-tent") forces `F∪T` to have an abundant element; DCC union-closed families of nonempty sets with a height-one member exceeding every height-zero member satisfy UC after adjoining `∅`.

## Why it matters for this workspace

- Extends the settled-class list: **dimension ≤ 2** (finite and infinite) and **DCC topological spaces** are new settled classes with human proofs (also claimed in the arXiv version `colbert-chain-conditions-2412.full.md`, whose claim block `colbert-topological-dcc` is filed but marked unchecked).
- The chain-condition/optimal-element machinery is a genuine structural route distinct from the entropy line and from the lattice classes; the file `colbert-chain-conditions-2412.full.md` and claims `colbert-dim-at-most-2`, `colbert-infinite-uc-false` (UC is false for arbitrary infinite families) are the anchors.
- This version-of-record adds the journal's published pagination (Order 43, art. 5, 2026) and its referee-approved text; the claims above are asserted-by-source from the open-access full text now on disk.

## Caveats

- None of this touches the constant record (Yu 0.38234 published / Liu 0.38271 conditional): the dimension-2 and DCC-topology classes do not include all finite union-closed families, so UC itself stays open.

## Claim block

```claim
id: colbert-order-2026-version-of-record
statement: The journal version of record of Colbert's chain-condition results is
  now held in the library: Order 43, article 5 (2026), open access (CC BY 4.0),
  DOI 10.1007/s11083-025-09717-w, full text at
  research/sources/colbert-order-2026-openaccess.full.md. It states: every
  union-closed family of dimension at most two has an abundant element
  (Prop 3.9, Thm 3.17); every nontrivial topological space satisfying the
  descending chain condition on open sets has an abundant element
  (Thm 3.21); and a family containing a singleton has that element abundant via
  an injection F∖F_x → F_x (Lemmas 3.14, Cor 3.16).
hypotheses: finite or infinite union-closed families; DCC topological spaces;
  dimension = max over chains of (length − 1).
holds-here: yes
status: asserted-by-source (open-access journal full text on disk)
bearing: upgrades the filed claims colbert-dim-at-most-2 / colbert-topological-dcc
  (previously anchored to the arXiv version colbert-chain-conditions-2412.full.md,
  where colbert-topological-dcc was marked unchecked) to the peer-reviewed
  version of record; settles the DCC-topological-space class at the published
  source. Does not change the constant record or prove UC.
anchor: research/sources/colbert-order-2026-openaccess.full.md
falsifies: if the published text is shown to differ materially from the arXiv
  claims, or a dimension-2 / DCC-topology counterexample is exhibited.
```