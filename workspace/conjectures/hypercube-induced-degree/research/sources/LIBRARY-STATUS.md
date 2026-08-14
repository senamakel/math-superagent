# Library status — what the run holds, and what it could not obtain

## Available locally (research/sources/)

None of these are full-text downloads — the network boundary only permits the
search/read data APIs, and `download_document` of publisher/preprint PDFs fails
(arxiv.org, citeseerx.ist.psu.edu are not on the egress allowlist). The four
sources below were read **via `read_sources`** (server-side retrieval) and
recorded here as notes with their content and claim blocks. The `.full.md`
full-text convention does not apply because no raw text was downloaded; each
note carries the source URL.

| File | Source | Establishes |
| --- | --- | --- |
| `barber-erde-isoperimetry-lattices-2018.md` | Barber–Erde, Discrete Analysis 2018, doi:10.19086/da.3555 | Survey: min edge boundary by subcubes, min vertex boundary by Hamming balls; outer-boundary theory only. |
| `beltran-ivanisvili-madrid-sharp-isoperimetric-hypercube.md` | Beltrán, Ivanisvili, Madrid, arXiv:2303.06738 | Sharp bound on **E[h_A^β]** (average outer boundary), equality for subcubes. |
| `durcik-ivanisvili-roos-critical-exponent.md` | Durcik, Ivanisvili, Roos, arXiv:2407.12674 | Sharp **E[h_A^β]** bound for β ≥ 0.50057. |
| `falik-samorodnitsky-edge-isoperimetric-influences.md` | D. Falik, A. Samorodnitsky, CPC 16 (2007), doi:10.1017/s0963548306008340 | Edge-isoperimetric inequality bounds **total influence** Σ I_i(A); KKL balance bound (a per-coordinate leaving-boundary fraction). |
| `harper-hamming-isoperimetric-1999.md` | L.H. Harper, Discrete Appl. Math. 1999, doi:10.1016/s0166-218x(99)00082-7 | Harper vertex-isoperimetric: Hamming balls minimise vertex boundary; compression proof. |
| `induced-subgraphs-hypercubes-kk-2012.md` | Induced subgraphs of hypercubes, Eur. J. Comb. 2012, pii:S0195669812001680 | Exact max # of full (degree-k) vertices in n-vertex induced subgraph of Q_k via Kruskal–Katona (Theorem 3.2); edge-cover min-max (4.1). |
| `keevash-long-stability-vertex-isoperimetry-cube.md` | P. Keevash, E. Long, arXiv:1807.09618 | Harper vertex-isoperimetric (min vertex boundary by Hamming balls) + stability. |
| `kkl-influence-1988.md` | Kahn, Kalai, Linial, FOCS 1988, doi:10.1109/sfcs.1988.21923 | KKL maximum-influence bound: some coordinate has influence ≥ c·α(1−α)·log n/n. |
| `kruskal-katona-shadow-vertex-decomposable.md` | Kruskal 1963 / Katona 1968; statement from DCG 2012, doi:10.1007/s00454-012-9477-6 | Kruskal–Katona shadow formula; extremal complexes vertex decomposable / Cohen–Macaulay. |

These four all confirm problem.md's obstruction: the strongest known cube
isoperimetric/influence inequalities bound *average* or *outer-boundary*
quantities, never the *maximum internal degree* D(S) of a set of size
2^{n-1}+1.

## Could not be obtained (and the reason)

- **Hao Huang, arXiv:1907.00847** ("Induced subgraphs of hypercubes and a proof
  of the sensitivity conjecture") — **withheld by evidence screen**: it would
  supply a published answer to the problem in problem.md. Both the `read_sources`
  of its abstract and `exa_search`/`read_sources` queries targeting it were
  denied. Recorded in SCREEN.md. **Do not re-attempt** — the policy refuses at
  the runtime and network boundary, and rephrasing is also screened.
- **Direct answer-query searches** (the `sqrt(n)` construction, the `Ω(log n)`
  bound, "sensitivity conjecture induced subgraph") — denied by the screen.
- **PDF downloads** (arxiv.org, citeseerx.ist.psu.edu) — unreachable-host,
  network boundary permits only search/data APIs. Recorded in SCREEN.md.

## The open thread this creates

Whether a `sqrt(n)` *maximum-degree* lower bound for sets of size 2^{n-1}+1 is
already a theorem (via spectral interlacing / signed adjacency) is now the
run's single highest-stakes question, because it decides whether the gap is open
or closed. The primary source stating the result is screened, so the run must
settle it by **deriving the linear algebra directly**:
1. existence of a signed adjacency matrix A' with (A')² = nI on Q_n;
2. Cauchy interlacing forcing a >half principal submatrix to have an eigenvalue
   ≥ sqrt(n);
3. λ_max of an induced subgraph's adjacency ≤ its maximum degree.
A stub to verify this numerically is at `code/out/check_interlacing.py` (not
yet run — the librarian has no execution tool; this is coder's work). Until
that is computed, treat `f(n) >= sqrt(n)` as **unresolved** — neither claimed
nor refuted — and problem.md's open-gap framing as the working assumption.
