# ROOT — Casas-Alvero: structure of the library's understanding

Phase-1 deliverable. This states the status of the problem as of the primary
sources this library holds, the structure of a minimal counterexample, the
verification bound, and the restricted classes already settled — each marked
with its evidence class and pointing to the source that establishes it.

## Status of the problem (priority question: has CA been proved?)

**A complete proof has been CLAIMED but is unverified, through 2026.** Soham
Ghosh, "Proof of the Casas-Alvero conjecture" (arXiv:2501.09272): v1 16 Jan
2025, v2 21 Mar 2026 with comment "Major revisions" (15 KB → 30 KB), claims
Theorem A: CA holds for every degree d≥3 over any characteristic-0 field, by
Koszul homology + a downward induction with a Brouwer-degree (topological,
over ℂ) step. Status verified from the arXiv abs page (held): **preprint,
not peer-reviewed, not withdrawn, not independently validated** — no journal
publication anywhere in the 2025-26 record; a deep search of the literature
finds no confirmation and no retraction. Wikipedia (held) still lists CA as
"Unsolved problem in number theory" with degree 20 the smallest open degree.
Evidence class: **claimed/asserted-by-source, unverified.** See
`research/summaries/ghosh2025_proof_html.md` (v1 full text),
`research/summaries/ghosh2025_proof_arxiv-abstract-v2.md` (version record).

**The claimed-proof family is now well documented**: Battiston 2015
(withdrawn), Fernández de las Heras 2013 (unpublished claim), Yakubovich 2015
(unpublished claim), Lu 2017 (claim whose F_p-counting core is suspected to
fall in the char-p trap), Ghosh 2025/26 (unverified). None has become an
accepted resolution; every refereed 2024-2025 source treats CA as open.

Per GOAL.md, this run's target changes only if a proof *stands*. The Ghosh
proof does not yet stand; the working assumption remains **CA is open**.
The Ghosh preprint is the single most important object to stress-test:
identify its char-0-only step (the Brouwer-degree / ℂ-local step and the
char-0 downward induction) and confirm it has no char-p analogue. The Lu
paper is the second one to stress-test, and its char-p failure point is
sharper (see `research/summaries/lu2017_casas-alvero-computational-ag.md`).

## Minimal-counterexample structure

From Laterveer–Ounaïes (arXiv:1204.0450, full text held):
- A non-trivial CA polynomial (counterexample) of degree N has **at least two
  distinct roots in its open Gauss–Lucas hull**; in particular N≥5 and ≥4
  distinct roots (Prop 4). Moreover **N≥6 and ≥5 distinct roots** (Prop 5).
- If f has at most **4 distinct roots**, CA holds (Prop 5 of §1).
- If f has a root of multiplicity ≥ N−2, then f = (x−a)^N (Prop 3).
- The set {α_1,…,α_{N−1}} of shared roots cannot have cardinality **two**
  (Prop 1, from [DdJ]).
- If f^(3) = (N!/(N−3)!)(z−a)^{N−3}, then f=(z−a)^N (Prop 2).

So a counterexample is quite non-degenerate: ≥5 distinct roots, no root of
huge multiplicity, shared-root set not of size 2. Source:
`research/sources/laterveer_ounaies_constraints_2012.full.md`.

## Verification bound

- Computer verification: **degree ≤ 7** by Diaz-Toca & Gonzalez-Vega (2006);
  degree 8 by the same authors (personal comm. per Graf-von-Bothmer).
- **Degree 12** settled (Castryck–Laterveer–Ounaïes, arXiv:1208.5404, 2012)
  by a combination of theoretical constraints + reduction-mod-p + Gröbner in
  characteristic p. Cost: ~3 weeks and ~90 GB RAM per scenario (5 scenarios).
  The paper states d=20 "the next open case" is "utopic" for this method.
- **Smallest open degree (as of 2012–2018 sources): d = 20.** Confirmed by
  Castryck et al (2012, "d=20, the next open case"), Wikipedia, and
  Schaub–Spivakovsky (2024: "smallest degree for which CA is not known is
  n=20").
- **This corrects `problem.md`, which states n=30 is the smallest open.** The
  30-claim is a stale recall: it ignored the 2012 degree-12 verification.
  Standing here: degree 20 per multiple sources.

## Restricted classes already settled (with hypotheses)

1. **Prime powers p^k and 2p^k** (Graf von Bothmer, Labs, Schicho, van de
   Woestijne, J. Algebra 316 (2007) 224–230; arXiv:math/0605090). Char 0.
2. **3p^k (p≠2), 4p^k (p≠3,5,7)** (Draisma–de Jong survey 2011 and sources
   therein), via p-adic valuations.
3. **5p^k, 6p^k, 7p^k** with classified bad primes (Castryck et al 2012
   computational section).
4. **Char-p**: the conjecture is FALSE. x^{p+1} − x^p is a separable
   counterexample in char p (Graf-von-Bothmer §3, Schaub–Spivakovsky). This is
   the sharpest structural fact: any proof must use char 0 somewhere.
5. **≤4 distinct roots ⇒ CA**; **root of mult ≥ N−2 ⇒ pure power**
   (Laterveer–Ounaïes).
6. **Degree p^r+1**: possible counterexample in normal form has algebraic
   coefficients; **degree 20 has no counterexample with three recycled roots**
   (Massri, arXiv:1806.09561).
7. **Finiteness**: for each degree n, the arithmetic Casas-Alvero scheme has
   finitely many rational points over any field (Ghosh, arXiv:2402.18717,
   preprint 2024); the projective variety of CA polynomials is at most
   two-dimensional in every characteristic.

## Methodologies in the literature (to beat / build on)

- Reduction mod p + counting over F_p (Graf-von-Bothmer); p-adic valuation
  reformulation (Draisma–de Jong).
- Resultant formulation: R_i = Res_x(f, f^(i)), conjecture ⇔ R_i
  independent / √(R_1,…,R_{d−1}) = (a_1,…,a_{d−1}) (Schaub–Spivakovsky).
- Bad-primes program: verify small d, classify primes p where CA_{d,p} fails,
  lift to degrees dp^ℓ via good primes (Schaub–Spivakovsky).
- Koszul homology / regular sequences / complete-intersection reformulation
  (Ghosh 2024+2025).
- Gauss–Lucas / Abel–Gontcharoff polynomial analytic constraints (Laterveer–
  Ounaïes; Mas stri).

## Library layout

Canonical sources under `research/sources/` (full text read-only), one
technical digest per source in `research/summaries/`. See `research/README.md`
and the FRONTIER for the citation graph. Every claim above traces to a held
source; nothing here is recalled from memory.

## Library-integrity record (librarian, 2026-08)

- **Hilbert-covariants mislabel RESOLVED.** The intended Abdesselam–
  Chipalkatti paper, "On Hilbert covariants" (arXiv:**1203.4761** = Canad. J.
  Math. 66(1) 2014 3–30, DOI 10.4153/CJM-2012-046-1), IS held in full at
  `research/sources/abdesselam-chipalkatti2012_hilbert-covariants.full.md`
  (Prop 3.2: G_{1,d} = (F,F)_2 = Hessian of F). Two wrong-content files
  (arXiv:1010.2358 data-mining; arXiv:1010.2667 wireless) are marked
  DO-NOT-CITE in-file and in their summaries. → `research/notes/abdesselam-
  chipalkatti-mislabel.md` (corrected), claim
  `abdesselam-chipalkatti-file-mislabel-corrected`.
- **Origin paper (Casas-Alvero 2001, J. Algebra 240:326–337) is bronze-OA
  but network-blocked from this host** (OpenAlex content 401, ScienceDirect
  403). Full text still un-held; the statement/motivation/status are fully
  covered by the held secondary tier. A later run with working publisher
  access should retry. → `research/notes/librarian-cycle-hessian-anchored.md`.
- **Fresh arXiv sweep 2026-08-17: coverage confirmed complete.** No new
  primary 2023–2026 treatment absent. → `research/summaries/arxiv_search_
  casasalvero_fresh.md`.
