# Gebendorfer 2026 — "A Proof of the Erdős–Gyárfás Conjecture" (unverified preprint)

**A preprint claiming a complete proof of the conjecture, located this cycle. Do
not treat the conjecture's openness as settled without knowing this exists.**

Source: Jonas Jakob Gebendorfer, "A Proof of the Erdős-Gyárfás Conjecture",
Zenodo, doi:10.5281/zenodo.18232846, published 2026-01-13. **Full text NOT
obtained** — Zenodo returned 410 Gone on direct record/file fetch. The **abstract
only** is captured (via `read_sources` triage on the DOI).

## What the abstract claims

A complete proof of the conjecture (every finite simple graph with δ ≥ 3 has a
cycle of length 2^k, k ≥ 2). Argument outline given as a **girth dichotomy**:

- girth 4 → a 4-cycle exists by definition;
- girth ≥ 5 → claims an 8-cycle exists via a "fold forcing" structural analysis
  of the second neighbourhood;
- girth 3 → a dichotomy: either a 4-cycle exists (Cases 1–7) or the local
  structure mimics high-girth graphs (Case 8), which forces an 8-cycle.
- Exhibits an (unspecified) n = 15 graph matching Case 8 (no 4-cycles) but
  containing an 8-cycle, as a consistency check.

So the total thesis is, unpacked: **every δ ≥ 3 graph is forced (by girth case)
to contain a 4-cycle or an 8-cycle.** That is a much stronger statement than the
conjecture itself — it would imply verification stops at length 8 for every
graph, which is false.

## Why the central dichotomy cannot be right (contradicted by sources already held)

The abstract's thesis "δ ≥ 3 forces a C4 or C8" is **refuted by graphs already
in this library**:

- **Markström's four 24-vertex cubic graphs have no 4-cycle and no 8-cycle**
  (one is planar, girth 3). These are held in
  `sources/markstrom-extremal-graphs-cycles.full.md` ("smallest cubic graphs
  without cycles of length 4 and 8 ... displayed in Fig. 14").
- **Exoo's 78-vertex cubic graph has no 4-, 8-, or 16-cycle**, and his
  540-vertex graph avoids {4,8,16,32} — see `sources/exoo-cubic-no-4-8-16.full.md`.
- **Exoo's G420** (arXiv:1403.5636, `sources/exoo-three-graphs-G420-no-4-8-16.full.md`)
  is 3-connected cubic planar with no 4-, 8-, or 16-cycle — this one lives
  *inside* Heckman–Krakovski's already-settled class, so no "forces a 4-or-8"
  claim survives even there.

Each of these is an explicit counterexample to "a 4- or 8-cycle is forced."
Consequently the Gebendorfer abstract, read literally, is inconsistent with
established, multi-source-verified results. Whether the full preprint dodges
this (e.g. by restricting to minimal counterexamples or adding hypotheses the
abstract omits) was **not** checkable — no full text.

## Status

- **Unverified preprint**, single author, h-index 0, 0 citations, Zenodo
  (non-peer-reviewed). Claims a full proof of a 30-year-open problem with a
  short case analysis — exactly the profile of a run to be wary of.
- The abstract's own central dichotomy ("forces a 4- or 8-cycle") is
  contradicted by three independent held sources (Markström 24-vertex,
  Exoo 78/540, Exoo G420).
- Verdict for the run: treat the conjecture as **still open**; do not cite this
  preprint as a proof or as a refutation. If the run's oracle re-derives the
  existence of a δ≥3 graph with no 4- or 8-cycle, record it here.

```claim
id: gebendorfer-unverified-full-proof-claim
statement: A 2026 Zenodo preprint (Gebendorfer, doi:10.5281/zenodo.18232846) claims a full proof of the Erdős–Gyárfás conjecture via a girth dichotomy that forces a 4- or 8-cycle in every δ>=3 graph.
hypotheses: (claim is about all finite simple δ>=3 graphs)
holds-here: NOT established — full text unobtainable; abstract's central dichotomy (C4 or C8 forced) contradicts held Markström 24-vertex no-C4-C8 cubic graphs and Exoo's 78/540-vertex and G420 no-{4,8,16} graphs
status: unverified preprint claim, inconsistent with verified sources as read
bearing: the conjecture remains open; do not treat 'open' as stale without noting this preprint exists and why it is not accepted
anchor: research/summaries/gebendorfer-proof-of-erdos-gyarfas.abstract.md
contradicts: markstrom-24-vertex-near-misses, exoo-short-2power-avoidance, exoo-g420-no-4-8-16-cubic-planar
```
