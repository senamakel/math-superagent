# Adjudication of three candidate lines of attack

File: research/approaches/adjudication-notes-2025.md
Author: research specialist. Verdicts below are literature-grounded (sources cited)
and recorded in the three approach files, which are the canonical ledger source.

## 1. `antimatroid-mobius-beta-bound` — REFUTED (as a reduction)

**What the reformulation is actually called.** The object is the *convex-geometry
closed-set lattice* (a meet-distributive lattice) of a planar point set, and the
functional is the Crapo-style **β-invariant** (equivalently, in the "convex
geometry / antimatroid" language, the β-invariant of the free-set complex / NBC
complex). Related to the Möbius function of the closed-set lattice.

**Precise statement of the theorem it relies on.** Ahrens–Gordon–McMahon,
"Convexity and the Beta Invariant", *Discrete Comput. Geom.* 22 (1999)
doi 10.1007/pl00009469, Theorem 4.1: for a finite planar point set C (affine span
the plane), the β-invariant of the convex-set lattice equals the number of
interior points, β(C) = |int(C)|, equivalently Σ_{K free} (−1)^{|K|−1}|K| =
|int(C)|. Edelman–Reiner, "Counting the Interior Points of a Point Configuration",
*DCG* 23 (2000) doi 10.1007/pl00009483, proved the Ahrens–Gordon–McMahon
conjecture topologically (each interior point contributes (−1)^{d−1} via the link
in the free complex). Edelman–Reiner–Welker, *DCG* 27 (2002)
doi 10.1007/s00454-001-0055-6, generalize to oriented matroids:
β(L_conv(M)) = (−1)^{r(M)−1}·(#interior elements).

**Do the hypotheses hold here?** Yes — the planar realizable case is exactly the
paper's setting. But the theorem is an **identity** (it *computes* #interior =
|X| − h exactly), never an inequality.

**Applied to this problem?** No published work connects the closed-set lattice
Möbius/β data to the ES upper bound. The identity is realization-invariant
(order-type-determined), which is a real property — parallel to the already
adopted order-dimension marker.

**What it would buy / why it fails.** N = h + i; i is computed by β, not bounded.
The step "bound i ≤ 2^{n-2} − h for n-avoiding sets" is the conjecture restated in
lattice language; no lattice/Möbius/β inequality in the literature delivers it.
Verdict: a faithful restatement (like order-dimension), legitimate as a
realization-invariant MARKER, refused as a reduction. Precedent URLs/DOIs in the
approach file.

## 2. `halfplane-separator-depth` — GROUNDED, with scope

**What it relies on.** The single-line (k=1) balanced split into two (n−1)-avoiding
halves is precisely the *decomposable-set* case that Baek & Balko, "The Erdős–
Szekeres Conjecture Revisited", SoCG 2025, doi 10.4230/LIPIcs.SoCG.2025.13, prove
recovers the sharp threshold 2^{k−2}+1 (claims `baek-balko-split`,
`baek-balko-decomposable`). Split k-gons have threshold *exactly* 2^{k-2}+1.

**What is open / what fails.** (a) The mechanism's cell count is wrong: an
arrangement of k half-plane boundaries has O(k²) regions, not O(k), and a boolean
combination of k half-planes has ≤ 2^k sign-vector classes, so no 2^{n-2} doubling
follows at constant k. (b) The run's own exhaustive search gives 0 valid k=1
single-line splits of es_construct(7) into two 6-avoiding 16-sets; the even/odd
bipartition needs exactly k=3 (`code/out/triple_inter.captured.txt`). So the k=1
split does not hold on the extremal template, and the k≥2 covering-family
generalization has no literature or computation support.

**Verdict.** Grounded as a reformulation of the known decomposable/split result;
not grounded as a proof mechanism for the general conjecture. Precedent including
the k-bisector literature (Nedela 2017) recorded in the approach file.

## 3. `strict-convex-lifting` — GROUNDED (description) / REFUTED (exact charge)

**What it is called / support.** Convex position = single up/down alternation: a
convex n-gon is the union of a k-cup and (n+2−k)-cap sharing leftmost and
rightmost points (classical; see Morris–Soltan survey doi 10.1090/s0273-0979-00-
00877-6; Kleitman–Pachter doi 10.1007/pl00009358). This is exactly the lifting /
cup-cap description and it is correct.

**Why the exact charge fails.** The budget "avoid an n-cap and n-cup" is the
Moshkovitz–Shapira partition count C(2n,n)+1 ≈ 4^n (run's own claims
`ms-n3q-partition-count`, `ms-esz-downset-injectivity`), not Σ_i C(n−2,i) =
2^{n-2}. So the "single 1-dimensional alternation whose binomial charge is the
sum" is the same error as the refuted ETV/grid route: the alternation charge is
intrinsically the ~4^n product/binomial. Forcing the two branches to close (share
both endpoints) — turning a split k-gon into a genuine convex polygon — is exactly
the difficulty Baek–Balko's split relaxation isolates and the abstract analogue
fails to deliver (`baek-balko-weak7-fails`).

**Verdict.** Correct description with the known 4^n-type cups-caps bound; the
proposed exact 2^{n-2} charge mechanism is refuted by the fact the alternation
budget is a product/binomial, not the required sum. Precedent in the approach file.

## Note on memory
remember_memory was down (4 failures) during this run; the durable findings are
instead stored in the three approach files (which are the canonical ledger source
for approaches) and summarised here. Retry Cognee writes once the memory server
recovers.
