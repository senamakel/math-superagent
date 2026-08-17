# Reimbayev 2025 — Hamiltonian Subgraphs of Order Seven in srg(n,k,1,2)

**Source (full text):** `research/sources/reimbayev-hamiltonian-order7-srg-l1-mu2.full.md`
**arXiv:** https://doi.org/10.48550/arxiv.2511.06572 · https://arxiv.org/html/2511.06572v1
**Author / date:** Reimbay Reimbayev, 09 Nov 2025, arXiv:2511.06572v1 [math.CO]. Preprint, not peer-reviewed.
**Type:** primary source, order-7 continuation of the two in-library Reimbayev papers
(hexagon bound 2409.10620; order-six subgraphs 2508.03377).

## What it establishes

The 19 possible Hamiltonian subgraphs of order seven (Figure 1); the counts h0..h18 as
element-wise linear forms in (n,k) terms plus **TWO free variables n3 and h11**, with the
nonnegativity of h16 and h18 giving **4n3 ≥ h11 ≥ 2n3**. Headline formulas:

- h0 (heptagons C7) = (1/14)nk(k−2)(k−4)(2k²−30k+133) − 10·n3 − h11
- p7 ≤ (1/14)nk(k−2)(k−4)(2k²−30k+133)  (upper bound, conjectured exact, not proved)
- p6 ≥ (1/12)nk(k−2)(2k²−21k+53) (restates the in-library 2024 paper)
- closed forms for h1..h18; several are pure ±c·n3 (h4, h6, h10, h14, h15, h17) and several
  mix n3 and h11/2.

## Significance for the run

The order-7 counts do **not** force n3 ≥ 1: they depend on n3 **and** a second free variable
h11, and n3=0 (⇒ h11=0) is consistent at every family member, including 99. The p7 upper
bound is parameter-determined, giving zero separating power between 99 and the two n3=0
controls (9, 243). This closes the "counting identity of order ≥ 7 pins n3 into an empty
range" route through order 7: the free-variable count only grows (order-6: one; order-7:
two), exactly as the n3-forced thread predicted. G-n3-positive can only be closed by a
**global forced-count obstruction**, not an order-k subgraph-count identity.

Full statement and hand-verified arithmetic in
`research/notes/librarian-order7-acquisition.md`; automation
`code/out/check_order7_reimbayev.py`.
