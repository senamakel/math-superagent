# Zhu 1998 — Pattern periodic coloring of distance graphs

**Subject:** The periodic-colouring technique that the adopted
`flat-torus-periodic-6col` upper-bound approach names as its discrete spine.
A primary source, now in the library; it was previously cited in
`research/approaches/flat-torus-periodic-6col.md` but **absent from
`sources/` and mis-attributed** (that note cites "Liu & Zhu"; the primary
paper is by **Xuding Zhu alone**).

## Source

- **Xuding Zhu**, "Pattern periodic coloring of distance graphs",
  *Journal of Combinatorial Theory, Series B* **73** (1998) 195–206.
- DOI: **10.1006/jctb.1998.1831**
- ScienceDirect: https://www.sciencedirect.com/science/article/pii/S0095895698918317
- Citation record: https://doi.org/10.1006/jctb.1998.1831 (22 citations)

## What the paper establishes (from the retrieved abstract / records)

Distance graph **G(Z, D)**: vertex set the integers Z; two vertices x, y
adjacent iff |x − y| ∈ D for a distance set D of positive integers. The paper
introduces and studies the **pattern periodic coloring** method for these
graphs — a colouring of the integer line given by a repeating finite pattern —
and compares it with other general colouring methods of distance graphs. It
investigates the **fractional**, **regular**, and **circular** chromatic numbers
of G(Z, D) for distance sets of the forms

- **D_{m,[k,k′]} = {1, 2, …, m} ∖ {k, k+1, …, k′}**, with m ≥ k′ ≥ k, and
- **D_{m,k,s} = {1, 2, …, m} ∖ {k, 2k, …, sk}**, with m > sk.

**Main result retrieved:** the chromatic number of **G(Z, D_{m,[2,k′]})** is
**completely determined** for arbitrary m and k′. For the class D_{m,k,s} the
paper determines the **circular** chromatic number.

The paper also connects pattern-periodic colourings to *regular* colourings and
the corresponding *regular chromatic number* (introduced by Zhu), which link to
Diophantine-approximation / number-theoretic structure.

## Why this is in the library

The adopted `flat-torus-periodic-6col` approach rests its discrete spine on the
claim that, for *integral/lattice-point* distance graphs, the chromatic number
is reached **periodically** and equals a minimum over finite quotients. That
claim is the Barajas–Serra 2005 circulant-reduction theorem (already in the
library: `barajas-serra-2005-distance-graphs-maximum-chromatic.md`). Zhu 1998 is
the technique tier that *defines* the pattern/periodic colouring being searched,
and its "completely determined chromatic number" for the D_{m,[2,k′]} family is
the model of exactly the kind of finite-exact determination the run is after.

**Boundary of the claim:** the theorems retrieved are for *integer* distance
graphs G(Z, D). They do **not** settle the continuous plane: that is the open
Hadwiger–Nelson problem (4 ≤ χ ≤ 7; see `liu-2008-distance-graph-survey.md`).
The periodic-suffices mechanism, and its finite-quotient reduction, transfer
only to the *lattice-point* analogue the approach makes precise with its own
thickening lemma — a run-side derivation, not this source.

## Attribution correction (recorded)

`research/approaches/flat-torus-periodic-6col.md` cites
"Liu & Zhu, 'Pattern periodic coloring of distance graphs', JCTB 1998". The
primary DOI (10.1006/jctb.1998.1831) resolves to **Xuding Zhu, single author**.
(Daphne Liu is not an author of this paper; she is an author of the later
*related* papers "Asymptotic clique covering ratios of distance graphs"
(with Zhu, EJC 2002) and of the 2008 survey.) The claim blocks below therefore
cite the correct single author.

## Fetch status

Direct download of the ScienceDirect full text is blocked at the network
boundary (recorded in `sources/README.md`); this record is the scholar's
synthesis of the retrieved abstract/record plus the citation-graph entry.
The main-theorem statement (complete χ for D_{m,[2,k′]}) is asserted-by-source
from the retrieved abstract, not re-proved here.

```claim
id: zhu-1998-pattern-periodic-coloring
statement: For the integral distance graph G(Z, D) with D = D_{m,[k,k']} =
{1,...,m} \ {k,k+1,...,k'}, the pattern periodic coloring method determines the
chromatic number completely for the class G(Z, D_{m,[2,k']}) (arbitrary m, k');
and for D_{m,k,s} = {1,...,m} \ {k,2k,...,sk} it determines the circular
chromatic number. Pattern periodic colourings are a named, comparative general
method for colouring integral distance graphs, tied to regular colourings and
to Diophantine-approximation structure.
hypotheses: G(Z, D) an integral distance graph (vertices Z, edges |x-y| in D);
D of the stated one-interval or arithmetic-progression-punctured forms;
pattern periodic colouring = colouring by a repeating finite integer pattern.
holds-here: partially — the *lattice-point* analogue is the discrete spine of
the adopted flat-torus-periodic-6col approach (the periodic-suffices mechanism
for *integral* distance graphs); it does NOT settle the continuous plane.
status: asserted (from retrieved abstract/record; full text blocked)
bearing: primary-source backing for the pattern/periodic-colouring technique
the flat-torus-periodic-6col approach searches; fixes the correct attribution
of the 1998 JCTB paper to Xuding Zhu alone.
anchor: research/sources/zhu-1998-pattern-periodic-coloring-distance-graphs.md
```
