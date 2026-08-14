# Brown, "Computation of the Totient Summatory Function" — arXiv abstract page

Source: https://arxiv.org/pdf/2506.07386 — the PDF landing page; full text at
`research/sources/arxiv-2506.07386-totient-summatory.full.md`
[[arxiv-2506.07386-totient-summatory.full]]. **The substantive content of the
paper is in the HTML full text**
(`research/sources/arxiv-2506.07386-totient-summatory.html.full.md`, digest
`research/summaries/arxiv-2506.07386-totient-summatory.html.md`) — this file
is the metadata page and is kept only for provenance.

## What this source establishes

Abstract: an algorithm for computing Φ(n) = φ(1) + … + φ(n) in time
Θ̃(n^{2/3}) and space Θ̃(n^{1/3}), starting from an existing algorithm based
on the Dirichlet hyperbola method and the Mertens function; used to compute
Φ(10¹⁹) = 30396355092701331435065976498046398788.

Lucas Augustus Brown, arXiv:2506.07386 [math.NT], submitted 9 Jun 2025,
29 pages. Ancillary file: `totientsum.py`.

## What it lets this run do

- Identifies the canonical sublinear algorithm for the quantity PE 351
  reduces to (see the HTML digest for the formulas, complexity, and Table 1
  reference values). The run's own n = 10⁸ sieve does not need the sublinear
  machinery; the paper is the Θ(n^{2/3}) verification context.

## Claims

None here — the claims live in `research/summaries/arxiv-2506.07386-totient-summatory.html.md`.
