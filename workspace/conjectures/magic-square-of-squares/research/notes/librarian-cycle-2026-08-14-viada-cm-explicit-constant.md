# Librarian cycle — CM-case explicit-constant finding (dp07-explicit-constant lane)

## What was added this cycle

**New source (filed, indexed, claim-blocked):**
`research/sources/viada-intersection-curve-algebraic-subgroups-product-elliptic-2003.full.md`
(59.5 KB) — Evelina Viada, "The intersection of a curve with algebraic subgroups
in a product of elliptic curves", Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 2
(2003) 47–75. Fetched from the numdam archive
(http://archive.numdam.org/article/ASNSP_2003_5_2_1_47_0.pdf) — the CM-case
primary the explicit-constant lane implicitly excludes.
Summary: `research/summaries/viada-intersection-curve-algebraic-subgroups-product-elliptic-2003.md`.

## Why it was fetched

Open request `dp07-explicit-constant-for-e3-ap` asks whether the
David–Philippon 2007 explicit constant, specialised to the AP subvariety of E³,
can give C^(1+r) < 3 for the run's Robertson curve E: y²=x(x²−c²). The DP07
paper itself is paywalled (a prior cycle recorded that). This cycle found that
the *documented* explicit-height-constant program (Veneziano–Viada 2021,
Checcoli–Veneziano–Viada 2019, MDPI 2017) is developed for **non-CM** elliptic
curves, and the **CM** case — which is our curve (j=1728, CM by Z[i]) — has
bounds described as far too large to use.

## What it establishes (claim `viada-2003-cm-subgroup-structure-richer`, checked)

Viada 2003 proves for a transverse curve C in Eⁿ (E/Q elliptic):
- points of C in the union of proper algebraic subgroups of Eⁿ have bounded
  canonical height;
- **CM case**: those lying in codim ≥ 2 algebraic subgroups form a **finite**
  set;
- **non-CM case**: those in codim ≥ n/2 + 2 subgroups are finite.

The Subgroup Lemma gives the structural reason: for non-CM E a codim-r subgroup
needs r Z-linearly independent equations (Hom(Eⁿ,E) rank 1 over Z); for CM E
(rang End-module, O of rank 2 over Z) it needs r O-linearly independent
equations — a richer module structure. This is exactly why the explicit-constant
technology blows up in the CM case and is only worked out for non-CM E.

## Bearing on the open request and the run

Our curve E: y²=x³−c²x is the congruent-number curve, j=1728, **CM by the
Gaussian integers** (anchored by Conrad, "The Congruent Number Problem", already
on disk: this is the quadratic-twist class of y²=x³−x). Therefore the
DP07/Veneziano–Viada explicit-constant lane, even if the DP07 number were
fetched, is **non-CM oriented** and gives no usable C for our CM curve. This
corroborates (does not fully close) open request `dp07-explicit-constant-for-e3-ap`:
the constant-size blockage of the uniform-height-bound-elliptic-ap approach is
now seen to be **structural (CM)**, not merely a fetch failure. The request
stays open for the literal value of DP07's constant but is grounded as far as
usefulness.

## What could NOT be fetched (recorded, not dead ends)

- DP07 primary (OUP, 403 on every route) — recorded in a prior cycle.
- MDPI "Lattices and Rational Points" (2227-7390/5/3/36, 2017) — 403 on the
  HTML page and on /pdf. Its abstract, which states the explicit-formula height
  bound, was captured via search (non-CM E). The full text was NOT stored;
  the CM-vs-nonCM contrast it documents is corroborated by Viada's own comments
  in Checcoli–Veneziano–Viada (Forum Math. Sigma 2019, an arXiv-accessible
  paper, not fetched this cycle because Viada 2003 already settles the needed
  structural point).

## Status

The explicit-constant angle is now covered as far as it can serve this run: the
CM obstruction is documented with a primary source on disk. Further gathering on
this lane is not worth a download until someone obtains the DP07 number itself,
which no accessible source provides.
