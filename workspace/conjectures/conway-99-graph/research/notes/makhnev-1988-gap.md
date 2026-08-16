# Gap — the exact statement of Makhnev 1988 "Strongly regular graphs with λ=1"

## What is missing

The full text of A. A. Makhnev, "Strongly regular graphs with λ=1",
Mat. Zametki 44(5) 667–672 (1988), Engl. trans. Math. Notes 44 847–850,
DOI 10.1007/BF01158426. Only the paywalled Springer landing page is in the
library (`research/sources/makhnev-1988-lambda1.full.md`).

## Why it matters

Both Reimbayev papers (arXiv 2409.10620, arXiv 2508.03377, full texts now in
library) pin the run's most promising counting-identity attack on a **single
parameter n_3** = number of pairs of triangles sharing an edge / two triangles
joined by two edges. Reimbayev asserts: *if n_3 = 0 then Makhnev 1988 proves
srg(99,14,1,2) does not exist.*

That assertion is the load-bearing step. It is currently:
- `status: asserted-by-source` (on Reimbayev's word; Reimbayev does not
  reproduce Makhnev's argument in the body);
- **unverified** against the primary source (Makhnev 1988 is paywalled).

## Falsifiers (what a source would have to settle)

1. Makhnev 1988 makes **no** such nonexistence statement for (99,14,1,2) — the
   conditional is a misattribution, and the n_3=0 attack has no theorem behind
   it.
2. Makhnev's hypothesis is **different** from "n_3 = 0" — e.g. it needs an
   additional condition that the hexagon-bound lower bound does not imply, in
   which case forcing n_3=0 alone would not rule out 99.
3. The claim actually concerns a different parameter set (e.g. (57,14,1,1)-type
   or a local-subgraph result), and Reimbayev mis-applied it to 99.

## What would fill it

A traceable statement of Makhnev 1988's main theorem(s), ideally the full text
or a faithful summary from the primary source. The Bielefeld Makhnev lecture
note (`research/sources/makhnev-symmetric-graphs-automorphisms-lecture.full.md`)
and the Behbahani thesis may quote Makhnev's λ=1 result — grep those before
fetching further. If neither carries it, the gap is a genuine external request.

## Not to be confused with
- Makhnev & Minakova 2004, "On automorphisms of SRGs with λ=1, μ=2"
  (Diskret. Mat. 16, 95–104) — automorphism bounds, already sourced via the
  Behbahani thesis. Different paper from Makhnev 1988.
- Makhnev 2013 Doklady "On graphs whose local subgraphs are srg(99,14,1,2)" —
  distance-regular classification, already in library.
