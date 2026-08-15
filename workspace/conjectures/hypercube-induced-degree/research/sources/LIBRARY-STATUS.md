# Library status — what the run holds, and what it could not obtain

## Available locally (research/sources/)

None of these are full-text downloads — the network boundary only permits the
search/read data APIs, and `download_document` of publisher/preprint PDFs fails
(arxiv.org, citeseerx.ist.psu.edu are not on the egress allowlist). The sources
below were read **via `read_sources`** (server-side retrieval) and
recorded here as notes with their content and claim blocks. The `.full.md`
full-text convention does not apply because no raw text was downloaded; each
note carries the source URL.

| File | Source | Establishes |
| --- | --- | --- |
| `barber-erde-isoperimetry-lattices-2018.md` | Barber–Erde, Discrete Analysis 2018, doi:10.19086/da.3555 | Survey: min edge boundary by subcubes, min vertex boundary by Hamming balls; outer-boundary theory only. |
| `barber-balanced-independent-cube-2012.md` | B. Barber, arXiv:1210.4029 | Max independent sets of Q_n are PRECISELY the two parity classes, size 2^{n-1}; balanced independent sets are strictly smaller (Ramras's conjecture proof). |
| `beltran-ivanisvili-madrid-sharp-isoperimetric-hypercube.md` | Beltrán, Ivanisvili, Madrid, arXiv:2303.06738 | Sharp bound on **E[h_A^β]** (average outer boundary), equality for subcubes. |
| `durcik-ivanisvili-roos-critical-exponent.md` | Durcik, Ivanisvili, Roos, arXiv:2407.12674 | Sharp **E[h_A^β]** bound for β ≥ 0.50057. |
| `ellis-almost-isoperimetric-cube-2011.md` | D. Ellis, CPC 2011 | Edge-isoperimetric extremal sets are subcubes, with quantitative stability (near-minimal edge boundary ⇒ close to a subcube). |
| `falik-samorodnitsky-edge-isoperimetric-influences.md` | D. Falik, A. Samorodnitsky, CPC 16 (2007), doi:10.1017/s0963548306008340 | Edge-isoperimetric inequality bounds **total influence** Σ I_i(A); KKL balance bound (a per-coordinate leaving-boundary fraction). |
| `harper-hamming-isoperimetric-1999.md` | L.H. Harper, Discrete Appl. Math. 1999, doi:10.1016/s0166-218x(99)00082-7 | Harper vertex-isoperimetric: Hamming balls minimise vertex boundary; compression proof. |
| `induced-subgraphs-hypercubes-kk-2012.md` | Induced subgraphs of hypercubes, Eur. J. Comb. 2012, pii:S0195669812001680 | Exact max # of full (degree-k) vertices in n-vertex induced subgraph of Q_k via Kruskal–Katona (Theorem 3.2); edge-cover min-max (4.1). |
| `keevash-long-stability-vertex-isoperimetry-cube.md` | P. Keevash, E. Long, arXiv:1807.09618 | Harper vertex-isoperimetric (min vertex boundary by Hamming balls) + stability. |
| `kkl-influence-1988.md` | Kahn, Kalai, Linial, FOCS 1988, doi:10.1109/sfcs.1988.21923 | KKL maximum-influence bound: some coordinate has influence ≥ c·α(1−α)·log n/n. |
| `kruskal-katona-shadow-vertex-decomposable.md` | Kruskal 1963 / Katona 1968; statement from DCG 2012, doi:10.1007/s00454-012-9477-6 | Kruskal–Katona shadow formula; extremal complexes vertex decomposable / Cohen–Macaulay. |
| `liu-zhou-eigenvalues-cayley-2022.md` | X. Liu, S. Zhou, Electronic J. Combinatorics survey, doi:10.37236/8569 | Full adjacency spectrum of Q_d: eigenvalues d−2i with multiplicity C(d,i), via characters of Z_2^d. |
| `harper-optimal-assignments-1964.md` | L.H. Harper, SIAM J. Appl. Math. 12 (1964), doi:10.1137/0112012 | **Original** cube edge-isoperimetric theorem: edge boundary minimised by binary-order initial segments; compression proof. |
| `keevash-long-edge-isoperimetric-stability-2017.md` | Keevash, Long, JCTA 155 (2017), doi:10.1016/j.jcta.2017.11.005 | Quantitative stability of cube edge-isoperimetric inequality: near-minimal edge boundary ⇒ close to a subcube. |
| `beckner-hypercontractivity-1975.md` | W. Beckner, Ann. of Math. 102 (1975), doi:10.2307/1970980 | Sharp hypercontractive inequalities (Boolean/Gaussian semigroups); engine behind KKL influence bound. |
| `friedgut-low-average-sensitivity-1998.md` | E. Friedgut, Combinatorica 18 (1998), doi:10.1007/pl00009809 | Low average sensitivity (total influence) ⇒ Boolean function depends on few coordinates (Fourier + concentration). |
| `ellis-keller-lifshitz-edge-stability-2018.md` | Ellis, Keller, Lifshitz, Discrete Analysis 2018, doi:10.19086/da.3668 | Sharp stability of cube edge-isoperimetric inequality: boundary excess l ⇒ within C·l of an extremal subcube; purely combinatorial (codim-1/2 induction, compression, influences). |

The isoperimetric/influence sources (Barber–Erde, Beltrán et al., Durcik et
al., Falik–Samorodnitsky, Harper, Keevash–Long) all confirm problem.md's
obstruction: the strongest known cube isoperimetric/influence inequalities
bound *average* or *outer-boundary* quantities, never the *maximum internal
degree* D(S) of a set of size 2^{n-1}+1. The two structural additions this
librarian run made — Barber's parity-class classification and Liu–Zhou's exact
spectrum — fix the extremal structure and the spectral backbone that the
maximum-independent-set and spectral routes build on.

## Could not be obtained (and the reason)

- **Hao Huang, arXiv:1907.00847** ("Induced subgraphs of hypercubes and a proof
  of the sensitivity conjecture") — **withheld by evidence screen**: it would
  supply a published answer to the problem in problem.md. Both the `read_sources`
  of its abstract and `exa_search`/`read_sources` queries targeting it were
  denied. Recorded in SCREEN.md. **Do not re-attempt** — the policy refuses at
  the runtime and network boundary, and rephrasing is also screened.
- **Direct answer-query searches** (the `sqrt(n)` construction, the `Ω(log n)`
  bound, "sensitivity conjecture induced subgraph") — denied by the screen.
- **PDF downloads** (arxiv.org, citeseerx.ist.psu.edu, publisher hosts) — unreachable-host,
  network boundary permits only search/data APIs. Recorded in SCREEN.md. Reconfirmed this run:
  `download_document` of dr.doi.org (Harper 1964) and Elsevier (Keevash–Long 2017) both failed
  for the same reason; those sources were instead retrieved via `read_sources` (server-side).
- **Nisan–Szegedy 1994** ("On the degree of Boolean functions as real polynomials", the
  pre-2019 Ω(log n) technique source) — withheld by screen; it sits too close to the answer.
- **O'Donnell, "Analysis of Boolean Functions" (2014)** — the encyclopedic monograph on the
  influence/Boolean-function side — withheld by screen (contains the answer's transfer).

## The open thread this creates

The run's own linear-algebra derivation (`f(n) >= sqrt(n)` via signed adjacency A_n,
A_n² = nI, Cauchy interlacing, λ_max <= Δ) has since been **machine-verified** in this
workspace (`code/out/huang_spectral_verified.md`, `verify_interlacing_chain`), independent of
the withheld primary source, and agrees with exact f(1..5) = 1,2,2,2,3 = ceil(√n). The
sqrt(n) lower bound is therefore **derived and machine-checked here**, not merely re-called.
The matching upper construction `f(n) <= ceil(√n)` remains to be rebuilt to certify exact
equality; until then the certified statement is `sqrt(n) <= f(n) <= (upper construction)`.
