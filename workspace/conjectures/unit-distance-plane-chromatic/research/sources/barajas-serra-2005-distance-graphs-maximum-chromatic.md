# Distance graphs with maximum chromatic number (Barajas–Serra 2005)

**Subject:** The discrete-spine theorem of the run's **adopted**
`flat-torus-periodic-6col` approach. It establishes that for an *integral*
distance graph G(D), the chromatic number is attained *periodically* and equals
the minimum over finite circulant reductions — which is what turns the
(continuum) plane-colouring search into a finite SAT object, at least in the
lattice-setting analogue.

**Source (primary, retrieved via server-side `read_sources`; direct download
blocked at the network boundary):**
- Javier Barajas, Oriol Serra, *Distance graphs with maximum chromatic number*,
  Discrete Mathematics and Theoretical Computer Science (DMTCS) 2005,
  DOI 10.46298/dmtcs.3391.
  URL: https://doi.org/10.46298/dmtcs.3391

## Exact statements recovered (from the source's own text)

**Theorem (periodic attainment for integral distance graphs).** For a finite
set of positive integers D, let G(D) be the distance graph on Z with edges
between x,y whenever |x-y| in D, and let chi(D,n) be the chromatic number of the
circulant reduction G(D,n) (the graph on Z_n with edges at distances D mod n).
Then

    chi(G(D)) = min { chi(D,n) : n in N, n > max{D} },

and the minimum is attained by a **periodic** colouring of G(D).

Supporting content: "a distance graph G(D) always admits colouring with
chi(D) colours which is periodic. Therefore chi(D) is also the chromatic number
of G(D,n) for all multiples n of the period of the periodic colouring."
Barajas–Serra use this to settle the four-distance case, building on Zhu's
settlement of the three-distance case (chi determined by reducing to a
two-generator circulant graph).

## Why it matters here

The flat-torus approach splits the continuum plane problem into (1) a discrete
spine (lattice-point distance graph, whose colouring is periodically attained
by this theorem) and (2) a thickening lemma (margin > 1+2rho lifts a lattice
colouring to a proper plane colouring). This Barajas–Serra theorem is the
discrete-spine half — the evidence that periodic colourings suffice to reach
the chromatic number in the lattice analogue. **Caveat recorded in the approach
note:** this is proved for *integral distance graphs on Z*, not for the
continuous plane R^2 with the full unit circle as distance set; the continuous
question (whether a periodic 6-colouring of the plane can beat 7) remains open
in the literature. So this source strengthens the *method*, not the answer.

## Basis and status

- Theorem statement and periodic-attainment content: sourced from the paper's
  text via `read_sources`. The exact statement is attributed here; the
  derivation (Zhu's three-distance case, the reduction to circulants) is the
  paper's subject.
- Not re-derived computationally here.

## Claim block

```claim
id: barajas-serra-periodic-attainment
statement: For a finite D of positive integers, the integral distance graph
  G(D) satisfies chi(G(D)) = min { chi(D,n) : n in N, n > max D }, attained by
  a periodic colouring (periodic colourings suffice to reach the chromatic
  number of an integral distance graph).
hypotheses: D a finite set of positive integers; G(D) the distance graph on Z
  with distance set D; chi(D,n) the chromatic number of the circulant reduction.
holds-here: partially — this is the lattice-point / integral-distance analogue
  that justifies the flat-torus approach's *discrete spine* layer, but the
  continuous plane R^2 with the full unit circle is not the integral distance
  graph Z, and whether a periodic 6-colouring can beat 7 there remains open.
status: asserted-by-source (Barajas–Serra 2005, DMTCS).
bearing: discrete-spine theorem of the adopted flat-torus-periodic-6col
  approach: the spine of a periodic colouring search is a finite SAT object
  because periodic colourings attain the chromatic number in the lattice
  analogue. Does NOT settle the continuous plane upper bound.
anchor: research/sources/barajas-serra-2005-distance-graphs-maximum-chromatic.md
falsifies: a continuous-plane periodic 6-colouring contradicting chi=7 would
  not falsify this theorem (it is about Z-distance graphs); the honest reading
  is that this theorem does not by itself carry the plane answer.
```
