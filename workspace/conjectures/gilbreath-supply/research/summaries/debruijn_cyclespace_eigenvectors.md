# Philippakis, Mallinar, Pandit, Belkin — Eigenvectors of the De Bruijn Graph Laplacian (arXiv:2410.07622)

**This source does not help SUPPLY.** The full text on disk is only the arXiv
abstract/metadata page (6810 bytes of citation-tool boilerplate); no paper
body was downloaded, so nothing beyond the abstract is available.

## What the abstract claims

The undirected De Bruijn graph over alphabet A of order k has Laplacian whose
eigenvalues were found by Delorme–Tillich (1998), but whose eigenvectors were
not explicitly described. This paper finds the eigenvectors in closed form and
shows they give a canonical basis for the cut- and cycle-spaces of De Bruijn
graphs; the constructed cycle basis is a cycle-space basis for both the
undirected and the directed De Bruijn graph, via a Fourier-analogue that
diagonalises the Laplacian. The cycle space across all orders k carries a
graded Hopf-algebra structure.

## Hypotheses and bearing

- Hypotheses: finite-alphabet De Bruijn graph, its graph Laplacian, cut/cycle
  spaces. These do not bear on the fold's Pascal-mod-2 / submask-XOR matrix
  `Φ_n` or on `wt(Φ_n h)` for the prime gap-parity string.
- The only connection is nominal: the run's `debruijn-cyclespace-kstar`
  approach (status **proposed**) wanted to characterise `K*(n)` as membership
  of S² in the coboundary (cut) space of the order-K De Bruijn graph `B_K`.
  This paper's eigenvectors of *graph Laplacians* are not the cut-space
  dimension/rank computation that approach needs, and in any case that
  approach is moot: directive 41 settled `K*(n) = ⌊n/2⌋` as a known number, so
  computing K* further is closed (`threads/kstar-definition-resolution.md`,
  status dead).
- What it allows the run to compute/bound/rule out: nothing for `wt(Φ_n h) ≥ c·n`.
  It neither supplies a switch-density-weaker arithmetic input nor a Walsh/
  submask bound. Request `walsh-spectral-subset-b904` stays open.

## Do not re-read

This is an abstract-only metadata page. Its abstract's topic (De Bruijn graph
cut/cycle-space bases) does not reach the fold object. The genuine full texts
on De Bruijn/cycle-space structure that matters for SUPPLY are already digested
elsewhere; this one adds nothing.

[[debruijn_cyclespace_eigenvectors.full]]
