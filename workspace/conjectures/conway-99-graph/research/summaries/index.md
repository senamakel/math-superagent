# Index of the reference summaries

This file is the pointer into `research/summaries/`. One entry per source.
**The summaries are the note; the `.full.md` files hold the complete text.**
Read the summary first; open the full text only when the summary does not
answer the question.

## Canonical / reference tier
- `conway-five-1000-problems.md` — Conway's own statement (OEIS A248380); the prize.
- `wikipedia-conway-99-graph.md` — encyclopedic statement; locally 7K2; open status.
- `wikipedia-berlekamp-vanlint-seidel-graph.md` — (243,22,1,2) control construction.
- `brouwer-srg-table-1-50.md`, `brouwer-srg-table-51-100.md`,
  `brouwer-srg-table-101-150.md` — Brouwer's feasibility tables; 99 row `?` open.
- `brouwer-haemers-srg-chapter.md` — SRG background chapter (paywalled preview).

## Primary structural sources (λ=1, μ=2)
- `brouwer-neumaier-1988-combinatorica.md` — PLS girth-5 theorem; μ=2 dichotomy;
  99 open (the `index.full.md` file is a duplicate landing page of it).
- `bagchi-mu2-correct.md` — records a WRONG download (pre-Lie paper); do not use.
- `bondarenko-radchenko-lambda1-family.md` — λ=1, g=k subfamily classification;
  99 not in it.
- `makhnev-1988-lambda1.md` / `makhnev-1988-lambda1-russian-fulltext.md` —
  Makhnev 1988 condition (*) theorems; Thm 2 = no srg(99,14,1,2) with (*).
- `makhnev-2013-local-subgraphs-srg-99.md` — local-subgraph srg classification.
- `pech-highly-regular-fulltext.md` — Pech 2021 (alco.183) full text: Thm 5.7
  PROVES PQ point graphs satisfy the 5-vertex condition; Prop 5.8 reduces the
  6-vertex condition to 8 types. Upgrades `bik-5vertex-holds-for-pq` from
  asserted to proved; shows 5-vertex is INERT, 6-vertex is the live rung.
- `reichard-7vertex-condition-gq.md` — Reichard 2014 (arXiv:1401.6816):
  primary proof that GQ point graphs satisfy the 5-vertex condition; 6/7-vertex
  machinery (8-type reduction). The GQ case behind the PQ extension.

## Automorphism / orbit-matrix
- `behbahani-2009-phd-thesis.md` / `-pdf.md` — orbit-matrix method; primes {2,3};
  order-3 fixed-point-free.
- `behbahani-lam-2011-srg-nontrivial-automorphisms.md` /
  `behbahani-lam-srg-nontrivial-automorphisms.md` — same result (published form).
- `crnkovic-maksimovic-*-.md` — no Z6/S3/Z9/E9 automorphism groups.
- `automorph-putative-conway-99-graph.md` — Cesarz–Woldar published version.
- `cesarz-woldar-automorph-conway99.md` — same paper, arXiv landing page (abstract only).
- `cesarz-woldar-automorph-conway99-body.md` — **FULL PROOF BODY** of Cesarz–Woldar
  (arXiv:2308.02978 HTML): the missing proofs. Sec 3 excludes order-14 automorphisms;
  Sec 4 proves divisibility by 7 ⟹ G ≅ Z₇ or Frob(21); Secs 5–6 eliminate Frob(21) by
  computer, giving (1′) 7||G| ⟹ G ≅ Z₇ and (2′) 2||G| ⟹ |G| | 6 (G ∈ {Z₂,Z₆,S₃}).

## Counting / subgraph structure
- `reimbayev-hexagon-bound-*.md` — hexagon lower bound; n_3 pivot.
- `reimbayev-subgraphs-order-six-*.md` — exact order≤6 subgraph counts in (n,k,n3).
- `reimbayev-hamiltonian-order7-srg-l1-mu2.md` — order-7 Hamiltonian subgraph counts
  (h0..h18) in (n,k,n3,h11); heptagon upper bound p7; FREE VARS n3 AND h11 (4n3>=h11>=2n3).
  [acquisition this cycle; full text in sources/]
- `reimbayev-srg19612-combinatorial.md` — spectrum-free proof srg(19,6,1,2) not exist.
- `brouwer-ihringer-kantor-4vertex-condition.md` — 4-vertex condition; common
  neighbours of a nonadjacent pair are nonadjacent.

## Nonexistence precedents (k=14)
- `wilbrink-brouwer-57141-does-not-exist.md` — srg(57,14,1,4) does not exist;
  Lemma-1 counting + coclique design; same 7K2 local structure.
- `milosevic-star-complement-57141.md` — star-complement reproof of same; 3720
  segments; same windmill local seed.
- `shpectorov-zhao-srg85-full.md` — srg(85,14,3,2) does not exist; 478 segments.
- `ostergard-soicher-no-mclaughlin-geometry.md` — 99-related search background.

## Surveys / context / leads
- `van-lint-perfect-codes-survey-1975.md` — five-member list; BvLS coset construction.
- `vanlint-brouwer-srg-partial-geometries-1984.md` — partial-geometry survey.
- `behbahani-lam-ostergard-triple-systems.md` — STS/4-vertex metadata record.
- `keramatipour-sat-conway99.md` — SAT attack cannot handle the problem.
- `zehavi-oliveira-not-conway-99.md` — solvable variant, NOT the problem.
- `guseinov-five-new-results-conway99.md` — five unverified claims (leads).
- `milosevic-star-complement-57141.md` — see precedents.
- `phillips-2026-clique-triangle-graphs.md` — clique/triangle-graph results.
- `oeis_a218293.md`, `oeis_a219272.md`, `citations_*.md` — OEIS/citation records.

## Not useful / wrong downloads (do not re-read expecting content)
- `bagchi-mu2-correct.md` — wrong paper (pre-Lie); the correct Bagchi content is
  resolved in research/notes/bagchi-mu2-dichotomy-resolution.md.
- `index.full.md` (under sources) — duplicate Springer landing page of
  Brouwer–Neumaier 1988.
- `cesarz-woldar-automorph-conway99.md` — duplicate arXiv landing page of the
  published automorph-putative-conway-99-graph.
- `makhnev-1988-lambda1.md` — paywalled landing page; the real content is in the
  Russian full-text summary.

## Where the threads live
The active directions are research/threads/hexagon-bound.md and the skeleton in
research/backward/. The root status is research/ROOT.md.
