# Reference library — Conway 99-graph problem

What is now available locally, where, and with which source URL. The canonical
catalogue/recall is Cognee; this is a human-facing map. Full texts are
never edited; corrections of mis-downloads are recorded in the corrected files
themselves.

## Sources (research/sources/, full texts editable only by download rewrite)

| File | Source | What it is |
|---|---|---|
| `conway-five-1000-problems` | https://oeis.org/A248380/a248380.pdf | Conway's own Five $1000 Problems, Problem 2 verbatim statement. **NOTE:** converted PDF lives in `research/summaries/conway-five-1000-problems.md` (summaries dir, not sources/) — see summaries index; no duplicate full text in sources/ |
| `wikipedia-conway-99-graph` | https://en.wikipedia.org/wiki/Conway%27s_99-graph_problem | Encyclopedic entry: properties, history, related graphs, references |
| `wikipedia-berlekamp-vanlint-seidel-graph` | https://en.wikipedia.org/wiki/Berlekamp%E2%80%93van_Lint%E2%80%93Seidel_graph | BvLS (243,22,1,2) graph: construction, properties |
| `brouwer-srg-table-1-50` | https://aeb.win.tue.nl/graphs/srg/srgtab1-50.html | Brouwer's SRG parameter tables, 1-50 (row 9: Paley(9) exists) |
| `brouwer-srg-table-51-100` | https://aeb.win.tue.nl/graphs/srg/srgtab51-100.html | Brouwer's tables 51-100 (row 99: `? 99 14 1 2 | 3 54 | -4 44` open) |
| `brouwer-srg-table-101-150` | https://aeb.win.tue.nl/graphs/srg/srgtab101-150.html | tables 101-150 |
| `van-lint-perfect-codes-survey-1975` | https://projecteuclid.org/.../10.1216/rmj-1975-5-2-199.pdf | van Lint survey; gives the FIVE-member list and explicit BvLS construction |
| `automorph-putative-conway-99-graph` | https://alco.centre-mersenne.org/articles/10.5802/alco.418/ | Cesarz-Woldar 2025, Algebraic Combinatorics 8(2):379-398; automorphism constraints |
| `cesarz-woldar-automorph-conway99` | https://arxiv.org/pdf/2308.02978 | arXiv landing page of Cesarz-Woldar (abstract only) |
| **`cesarz-woldar-automorph-conway99-body` (this cycle)** | https://arxiv.org/html/2308.02978v1 | **FULL PROOF BODY of Cesarz-Woldar 2023 (acquired this cycle)**. The one automorphism source whose proofs the library was missing. Sec 3: no order-14 automorphism. Sec 4: 7||G| ⟹ G ≅ Z₇ or Frob(21), with orbit valencies in the Frob(21) case. Secs 5-6: Frob(21) eliminated **by computer**, giving (1′) 7||G| ⟹ G ≅ Z₇ and (2′) 2||G| ⟹ |G| | 6 (G∈{Z₂,Z₆,S₃}). Confirms the claims-ledger note that Cesarz-Woldar's (1′)/(2′) are computer-free but the Frob(21) elimination is computer-assisted. |
| `crnkovic-maksimovic-composite-automorphism` | https://doi.org/10.55016/ojs/cdm.v15i1.62323 | Crnkovic-Maksimovic 2020; composite-order automorphism groups |
| `crnkovic-maksimovic-full-pdf` | https://cdm.ucalgary.ca/article/download/62323/54015 | **FULL TEXT of Crnkovic-Maksimovic 2020 — Section 7 exact mechanism ruling out Z6,S3,Z9,E9 automorphism groups; Thm 7.3 |Aut|=2^a 3^b, b in {0,1}** |
| `behbahani-2009-phd-thesis-pdf` | https://spectrum.library.concordia.ca/id/eprint/976720/1/NR63369.pdf | **FULL TEXT of Behbahani 2009 PhD thesis (primary source) — Thm 4.14: only primes 2,3; order-3 fixed-point-free; Makhnev-Minakova Thm 1.6 fixed-point dichotomy** |
| `guseinov-five-new-results-conway99` | https://doi.org/10.6084/m9.figshare.23732622.v1 | Guseinov preprint "Five New Results" (independence >= 10; not subgraph of BvLS; no H(4,3); etc.) — UNVERIFIED leads |
| `behbahani-2009-phd-thesis` | https://spectrum.library.concordia.ca/976720/ | Behbahani thesis landing page (abstract only) |
| `behbahani-lam-ostergard-triple-systems` | https://research.aalto.fi/en/publications/on-triple-systems-and-strongly-regular-graphs | **Metadata record** (not full text: JCTA paywalled) of Behbahani–Lam–Östergård 2012 "On triple systems and strongly regular graphs", JCTA 119(7) 1414–1426, doi 10.1016/j.jcta.2012.03.013. Confirms abstract content in `triangle-geometry-4vertex-enumeration.md`. |
| `makhnev-2013-local-subgraphs-srg-99` | https://link.springer.com/article/10.1134/S106456241306032X | Makhnev 2013 (Doklady) local subgraphs srg(99,14,1,2) |
| **`brouwer-neumaier-1988-combinatorica`** | https://ir.cwi.nl/pub/1721/1721D.pdf (Combinatorica 8(1) 57-61, doi 10.1007/BF02122552) | **FULL TEXT of the mu=2 / partial-linear-space girth-5 paper — the primary structural source; resolves the mu=2 bound and 99's open status in its own table** |
| `reimbayev-hexagon-bound-srg-lambda1-mu2` | https://arxiv.org/pdf/2409.10620 | Hexagon lower bound for srg with lambda=1,mu=2 (landing page) |
| `reimbayev-hexagon-bound-body` | https://arxiv.org/html/2409.10620v1 | **FULL TEXT** of hexagon bound: hexagon count >= (1/12)nk(k-2)(2k^2-21k+53), attained iff n_3=0; n_3 = pairs of triangles joined by two edges; if n_3=0 then Makhnev-1988 conditional rules out 99 (unverified) |
| `reimbayev-subgraphs-order-six-srg-l1-mu2` | https://arxiv.org/pdf/2508.03377 | Subgraphs of order six in this family (landing page) |
| `reimbayev-subgraphs-order-six-body` | https://arxiv.org/html/2508.03377v2 | **FULL TEXT**: all order-<=6 subgraph counts of the srg(v,k,1,2) family in closed form; order<=5 depend only on (n,k), all 62 order-6 counts depend on (n,k)+n_3 (pairs of edge-sharing triangles) |
| **`reimbayev-hamiltonian-order7-srg-l1-mu2` (acquired this cycle)** | https://arxiv.org/pdf/2511.06572 / https://arxiv.org/html/2511.06572v1 | **FULL TEXT (2025, preprint)**: order-7 continuation. The 19 Hamiltonian subgraphs of order seven; counts h0..h18 as linear forms in (n,k) + TWO free variables n3 AND h11 (4n3>=h11>=2n3 by nonnegativity); heptagons h0=(1/14)nk(k-2)(k-4)(2k^2-30k+133)-10n3-h11; heptagon upper bound p7 <= (1/14)nk(k-2)(k-4)(2k^2-30k+133), conjectured exact. **Order-7 counts do NOT force n3>=1** (n3=0, h11=0 is consistent at every family member incl 99); closes the counting-identity route through order 7. See note librarian-order7-acquisition.md, claim reimbayev-order7-counts-two-free-vars. |
| `shpectorov-zhao-srg85-full` | https://arxiv.org/pdf/2504.02449 | **FULL TEXT** (2025 preprint): srg(85,14,3,2) does not exist, by exhaustive local-configuration enumeration (478 segments, 4 types, around a maximal 3-clique in the 39 good cubic local graphs) + 34-dim Euclidean representation. Same k=14, mu=2 as 99, lambda=3. The closest successful nonexistence-by-local-enumeration precedent. |
| `bondarenko-radchenko-lambda1-family` | https://arxiv.org/pdf/1201.0383 (JCTB 2013, DOI 10.1016/j.jctb.2013.05.005) | **FULL TEXT**: complete classification of the lambda=1, g=k subfamily ((n^2+3n-1)^2, n^2(n+3), 1, n(n+1)) = exactly L_{3,3} (9,4,1,2), Brouwer-Haemers (81,20,1,6), Games (729,112,1,20, unique). Method: vertex-transitivity -> F3 vector space -> power of 3 -> Diophantine. (99,14,1,2) is NOT in this subfamily (g=44 != k=14). |
| `makhnev-1988-lambda1-russian-fulltext` | https://www.mathnet.ru/php/getFT.phtml?jrnid=mzm&option_lang=rus&paperid=4220&what=fullt | **PRIMARY SOURCE now in-hand, full Russian original (open on mathnet.ru).** The paper whose conditional (n_3=0 -> no 99) Reimbayev relies on. Thm 1: lambda=1 SRG satisfying (*) is mu<=3 or (27,10,1,5). Thm 2: no srg(99,14,1,2)/(115,18,1,3) satisfies (*); the 99-proof builds an srg(33,12,1,6) subobject from a triangle closure + 60 outer points (20 outer triangles), contradicting Thm 1. English translation paywalled (Springer 10.1007/BF01158426) but Russian original full text is open. Closes the single most valuable gap. |
| `keramatipour-sat-conway99` | https://arxiv.org/pdf/2604.23037 | SAT-solver approach; discussed limits + five-member list |
| `zehavi-oliveira-not-conway-99` | https://arxiv.org/pdf/1707.08047 | "Not Conway's 99-graph problem" — a solved variant, boundary work |
| `greaves-koolen-park-delsarte-bound` | https://arxiv.org/pdf/2012.09391 | **FULL TEXT** Greaves, Koolen, Park 2021 "Improving the Delsarte bound" — maximal-clique/Delsarte/claw repertoire; Theorem 4.3 infinite family excluded for srg with smallest eigenvalue -m; appendix tables of nonexistent srg at smallest eigenvalue -4,-5,-6,-7. **Checked: (99,14,1,2) appears in NONE of the tables** (the -4 table lists only 4 sets, all v>>99). |
| `koolen-cao-yang-smallest-eigenvalue-survey` | https://arxiv.org/pdf/2011.11935 | **FULL TEXT** Koolen, Cao, Yang 2021 survey "Recent progress on graphs with fixed smallest eigenvalue" — Hoffman-graph + distance-regular classification programme; confirms -2 theory complete (CGSS generalized line graphs), -3/-4 not; Neumaier geometric dichotomy fails its hypothesis at (99,14,1,2). The named survey for the least-eigenvalue-minus-4 approach. |
| `lou-murin-srg991412-2014` | https://math.mit.edu/research/highschool/primes/materials/2014/Lou-Murin.pdf | **FULL TEXT (acquired this cycle)** — Lou & Murin, MIT PRIMES-USA 2014, "On the Strongly Regular Graph of Parameters (99,14,1,2)". This fills the previously-unobtainable "Lou & Murin" lead. Unrefereed; carries alpha<=22 (independently matches run's checked closed form 22), alpha=9 not maximal, no automorphism of order p>14/13/11, and the alpha=22 => (22,4,2) block-design reduction (Sec. 7). |
| **`forced-structure-reduction-conway99`** | https://arxiv.org/html/2608.11211v1 | **FULL TEXT (CAISc 2026 preprint, AI agent, not peer-reviewed)**. Independently confirms the run's forced-structure reduction: inner–outer adjacency fully forced by λ=1 (N(0)=7K2) + μ=2; only unknown is the (k−2)-regular outer-outer graph = 12-regular on 84 vtx for (99,14,1,2). Prop 1 (exhaustive): no circulant on Z/99Z exceeds 33/49 difference-classes (68%). Orbit-existence CP-SAT validated on srg(9,4,1,2) & Paley(13,6,2,3), leaves open single-fixed-point Z_7 sub-case unresolved (48h/14 cores). Best heuristic 69.43% (3437/4950); a provable bound < 4950 would be a nonexistence proof, none claimed. See note `forced-structure-reduction-2026.md`. |
| `makhnev-symmetric-graphs-automorphisms-lecture` | https://www.math.uni-bielefeld.de/~baumeist/sommerschule/makhnev.pdf | Makhnev lecture note. Sources the Wilbrink 1984 order-11 exclusion and |G| divides 2·3³·7, plus Makhnev–Minakova fixed-point dichotomy & involution classification — the only traceable route to the paywalled Wilbrink 1984. |
| `ostergard-soicher-no-mclaughlin-geometry` | https://arxiv.org/pdf/1607.03372 (published JCTA 155, doi 10.1016/j.jcta.2017.10.004) | "There is no McLaughlin geometry". Cautionary: a pseudogeometric SRG achieving the Krein bound need not be geometric when α>1. NOTE: an initial guessed arXiv id 1705.06821 fetched a wrong ML paper; corrected. |

### Corrected sources (initially mis-downloaded by guessing arXiv ids; corrected records)
| File | Note |
|---|---|
| `bondarenko-radchenko-lambda1-family` | An initial guess (arXiv 1303.3164) fetched Sawant & Chakrabarti, "Features and Aggregators for Web-scale Entity Search" — a wrong paper. Correct id is **1201.0383** (verified from the search result's title/abstract), re-fetched and verified before reliance. |
| `behbahani-lam-2011-srg-nontrivial-automorphisms` | Real paper is Discrete Math 311 (2011) 132-144, doi 10.1016/j.disc.2010.10.005, paywalled, NOT in library; file is a corrected identity record |
| `crnkovic-maksimovic-composite-order-srg` | Real paper in-library under `crnkovic-maksimovic-composite-automorphism`; correction duplicate |
| `bagchi-mu2-correct` | Bagchi "On SRGs with mu<=2" (2006), paywalled; corrected record. NOTE: an earlier guessed arXiv download (math/0512558, Gichev's Lie-algebra paper) is recorded as WRONG and must never be cited for graph theory |
| `index.full.md` | NOT an index. A misnamed Springer paywalled landing page of Brouwer–Neumaier 1988 (DOI 10.1007/BF02122552). The real full text of that paper is `brouwer-neumaier-1988-combinatorica.full.md` (ir.cwi.nl/pub/1721/1721D.pdf). Never read `index.full.md` for content, and never treat it as a catalogue; the library's summaries catalogue is `research/summaries/index.md`. |
| `pech-highly-regular-srg-ar5iv` / `pech-highly-regular-srg` / `pech-highly-regular-alco` | Landing-page / ar5iv duplicate variants of the real Pech full text. The primary is `pech-highly-regular-fulltext.full.md` (ALCO 4(5) 843-0, DOI 10.5802/alco.183); read that one. |

## Summaries (research/summaries/, one per source, read before full text)

One per source above, named `<source>.md`, carrying the structural digest / a
summary of what it establishes.

## Notes (research/notes/)

- `established-claims.md` — claim blocks c1-c6 (family, integrality, automorphism
  bounds, controls, locally-linear, Bagchi dichotomy).
- `bagchi-mu2-dichotomy-resolution.md` — the RESOLVED Bagchi contradiction: the
  mu=2 dichotomy does not bind 99 (nor 243); closes c6. Also carries the
  srg(33,8,1,2) mechanism claim answering request published-mechanism-ruling-5cf8.
- `brouwer-neumaier-1988-finding.md` — primary-source status of (99,14,1,2): open,
  spectrum 3^54,-4^44; corrects a FALSE secondary summary claiming BN1988
  "eliminates" it. (Superseded in part by bagchi-mu2-dichotomy-resolution.md on
  the BvLS worry, but its BN1988 table transcription stands.)
- `automorphism-orders-consolidated.md` — answers request exact-list-prime-051a;
  precise excluded orders and computer-assistance status.

## Claims ledger (research/CLAIMS.md — derived)

Highest-value claims (status: checked where computed over Z, else sourced):
- **Family is exactly five members** `(9,4),(99,14),(243,22),(6273,112),
  (494019,994)`; k=u²+u+2, u∈{1,3,4,10,31}. [checked]
- **srg(33,8,1,2) does not exist** — by multiplicity integrality (no
  structural precedent). Corrects problem.md. [checked]
- **The bound that matters for 99 from mu=2 theory is k>=lambda(lambda+3)/2=2,
  satisfied; the μ=2 dichotomy is NOT a 99-nonexistence route.** [sourced+reasoned]
- **Automorphism bounds**: |G| | 2·3³·7·11; 7||G| ⟹ Z₇, 2||G| ⟹ |G||6
  (Cesarz-Woldar, computer-free); no Z6,S3,Z9,E9 (Crnkovic-Maksimovic);
  prime divisors of |G| ⊆ {2,3} (Behbahani-Lam). [sourced]
- **Existence of (99,14,1,2) is open** (Brouwer '?'; BN1988 also lists '?';
  no confirmed claim since). [sourced]

## Durable memory (Cognee)
Stored: five-member family fact; the BN1988 mu=2 bound and open-99 status; the
automorphism bounds; the reconciled Bagchi finding; the srg(33,8,1,2) integrality
mechanism; the library-safety lesson (never guess arXiv ids); the
forced-structure-reduction-conway99 preprint (2026-04 acquisition; its Section 4
independently confirms the run's derived-design-at-a-vertex / g-reduce reduction
and its Section 5 documents the open Z_7 prescribed-automorphism sub-case).

## Gaps / could not obtain
- **Makhnev 1988 "Strongly regular graphs with λ=1" — CLOSED.** The full Russian
  original is now in the library
  (`research/sources/makhnev-1988-lambda1-russian-fulltext.full.md`, open on
  mathnet.ru paperid=4220). Condition (*) = Reimbayev's n_3=0; Thm 1 (mu<=3 or
  (27,10,1,5)); Thm 2 (no srg(99,14,1,2)/(115,18,1,3) under (*)). The n_3-pivot
  attack now rests on a real theorem. Remaining cost: n_3=0 is itself only
  Reimbayev's conjecture, and the oracle run that rook(3)/BvLS satisfy (*) is
  pending tool_builder/coder execution (admissibility check).
- **Von der Flaass 1984 "Strongly regular graphs with λ=1"** (conference abstract) — cited in Makhnev 1988's literature list; originals of the λ=1 classification. Not obtained.
- Behbahani & Lam 2011 journal paper full text (paywalled; Discrete Math 311(2-3) 132-144) — filled for the run by the 2009 PhD thesis (primary source, in-hand).
- Makhnev & Minakova 2004 journal full text (paywalled) — filled by verbatim Thm 1.6 in Behbahani thesis.
- Bagchi 2006 full text (ScienceDirect 403); theorem verified via independent verbatim summaries + BN1988.
- **Behbahani, Lam, Östergård 2012 "On triple systems and strongly regular graphs"** (JCTA 119, doi 10.1016/j.jcta.2012.03.013, paywalled); the triple-system/partial-line-space angle directly relevant to the triangle geometry. Full text still not obtained, but the **abstract is now captured** (see note `triangle-geometry-4vertex-enumeration.md`): STS whose block graphs meet the 4-vertex condition fall into two SRG families. So the 99 *partial* STS geometry escapes that classification; a genuine-STS realization at 99 is not decided by it. Official metadata (Aalto research-portal record, full citation + DOI + keywords) now captured at `research/summaries/behbahani-lam-ostergard-triple-systems.md` (open record retrieved 2026; no PDF there). [Relevant adjacent: Kaski–Khatirinejad–Östergård 2011 "Steiner triple systems satisfying the 4-vertex condition"; Kaski–Östergård 2004 STS(19) classification; Heinlein–Östergård 2023 STS(21) count — the latter two bound the geometry-enumeration frontier (see note).]

## Corrected download (do not re-fetch)
- `ostergard-soicher-no-mclaughlin-geometry`: an earlier guessed arXiv id
  `1705.06821` fetched a spatial-VAE ML paper. The correct id is `1607.03372`.
  Verified the full text is the McLaughlin-geometry paper before relying on it.

## Could not obtain (do not re-attempt without a new reason)
- **Cameron 1975, "Partial quadrangles", Quart. J. Math. Oxford (2) 26 (1975)
  61–73** (doi 10.1093/qmath/26.1.61) — paywalled on Oxford Academic. This is
  the defining paper of the run's *adopted* approach `pq-2-6-2-classification`.
  **Its mathematical content is fully carried by in-library secondary
  sources**: the exact PQ axioms (partial linear space of order (s,t); three
  pairwise-collinear points lie on one line; two non-collinear points meet
  exactly μ common points on lines) and the theorem that an SRG is the point
  graph of a PQ iff it is K4−e-free (diamond-free), with lines recoverable as
  maximal cliques, are stated verbatim in `brouwer-ihringer-kantor-4vertex-
  condition.full.md` (its citation [7]) and in the Mohammadian–Tayfeh-Rezaie
  abstract/body held at `research/sources/mohammadian-*-diamond-free-srg.full.md`.
  Only the original typescript is absent. Do not redownload.
- **Behbahani–Lam–Östergård 2012, "On triple systems and strongly regular
  graphs"** (JCTA 119, paywalled) — full text unobtainable; abstract captured.
- **Behbahani–Lam 2011; Makhnev–Minakova 2004; Bagchi 2006** — paywalled
  journal full texts; each filled by a primary/summary in-hand.

## Oracle inputs supplied
- Explicit BvLS construction: van Lint 1975 (5×11 parity-check H of ternary
  Golay code; coset graph), confirmed (243,22,1,2) with spectrum 4^132,-5^110.
- Rook's graph = Paley(9) = 3×3 grid: confirmed exists, spectrum 1^4,-2^4.
- Feasibility exact-arithmetic table at code/out/feasibility-candidates-corrected.md.
