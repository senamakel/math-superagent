# Scholar pass — the genuinely new source is one undigested De Bruijn Laplacian metadata page

This pass was tasked with reading what is now in `research/` against the goal.
Prior passes had repeatedly concluded "no undigested claim-bearing source"
(counting 50 full texts ↔ 50 digests). This pass **found the one source every
prior pass missed** and digested it.

## The genuinely new item

`research/sources/debruijn_cyclespace_eigenvectors.full.md` (arXiv:2410.07622,
Philippakis, Mallinar, Pandit, Belkin) — its summary was still the
auto-generated placeholder template ("Digest only — read this first … Replace
this digest with a summary"), so the source was on disk but never digested.
The file contains **only the arXiv abstract/metadata page** (6810 bytes of
citation-tool boilerplate); no paper body was downloaded. Its abstract claims:
explicit closed-form eigenvectors of the undirected De Bruijn graph Laplacian
(eigenvalues known since Delorme–Tillich 1998), giving a canonical cut/cycle
space basis valid for both undirected and directed De Bruijn graphs, with a
graded Hopf-algebra structure across orders.

## Why it does not help SUPPLY

- Its hypotheses (graph Laplacian eigenvectors of De Bruijn graphs) do not bear
  on the Pascal-mod-2 / submask-XOR fold matrix `Φ_n` or on `wt(Φ_n h)` for the
  prime gap-parity string.
- The only connection is nominal: the run's `debruijn-cyclespace-kstar` approach
  (status proposed) wanted K*(n) via membership of S² in the cut space of a
  De Bruijn graph. That approach is moot — directive 41 settled `K*(n)=⌊n/2⌋`
  as a known number, thread dead — and this paper's Laplacian eigenvectors are
  not that rank computation anyway.
- It supplies no switch-density-weaker arithmetic input and no Walsh/submask
  bound; request `walsh-spectral-subset-b904` stays open.

## State of the run

Unchanged by this source. The three open items remain exactly as recorded by
the prior passes: the finite-prefix transfer, request `walsh-spectral-subset-b904`
(E[S(n)²]=O(n) for the prime string, CONCLUSION.md §5), and `s2_N → 0`. The
terminus verdict (GOAL hypothesis refuted, sixth door, CONCLUSION.md) is
untouched.

```claim
id: debruijn-laplacian-source-does-not-help
statement: "The source research/sources/debruijn_cyclespace_eigenvectors.full.md (arXiv:2410.07622, Philippakis-Mallinar-Pandit-Belkin) is an abstract-only arXiv metadata page whose summary was left as the auto-generated placeholder. Its abstract claims explicit closed-form eigenvectors of the undirected De Bruijn graph Laplacian giving a canonical cut/cycle-space basis (eigenvalues known since Delorme-Tillich 1998), valid for undirected and directed De Bruijn graphs, with a graded Hopf-algebra structure. Its hypotheses (finite-alphabet De Bruijn graph Laplacian, cut/cycle spaces) do not bear on the Pascal-mod-2 submask-XOR fold matrix Phi_n or on wt(Phi_n h) for the prime gap-parity string; it supplies no switch-density-weaker arithmetic input and no Walsh/submask bound. The only connection is nominal to the proposed (not grounded) debruijn-cyclespace-kstar approach, which is moot since directive 41 settled K*(n)=floor(n/2). The run's state is unchanged: finite-prefix transfer, request walsh-spectral-subset-b904 (E[S(n)^2]=O(n), CONCLUSION.md s5), and s2_N->0 remain open; the terminus verdict stands."
hypotheses: the full text on disk is the arXiv abstract page only (6810 bytes, verified this pass); no paper body, so only the abstract's statements are available.
holds-here: yes — this is an audit statement about a source's bearing, not a theorem about the fold.
status: checked (read this pass; full text is abstract/metadata only)
bearing: nobody should re-fetch De Bruijn graph-Laplacian eigenvector material expecting a way past the parity barrier or a second-moment input for the fold; the source adds nothing to SUPPLY. Recorded so a later reader does not re-read it.
anchor: research/summaries/debruijn_cyclespace_eigenvectors.md; research/sources/debruijn_cyclespace_eigenvectors.full.md
```

## Housekeeping footnote

File counts: with this source the sources/ list is **51** full-text files (not
50 as prior passes counted — they missed `debruijn_cyclespace_eigenvectors`),
all now with a real (non-placeholder) digest. The two DELETED_* files are
overwrite/provenance notes, not sources. The 7 `citations_w*` files remain
lead-only lookup tables; the OEIS rows, HAL page, and two Krawtchouk/MacWilliams
metadata stubs carry no theorems beyond primary digests. FRONTIER.md's
"Mentzer supply-chain" contamination ring remains — read it by subject, not
rank.
