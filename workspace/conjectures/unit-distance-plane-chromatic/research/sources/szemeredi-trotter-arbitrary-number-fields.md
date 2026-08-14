# Szemerédi–Trotter constructions over arbitrary number fields (nice bases)

**Subject:** The technique by which algebraic number fields generate sharp
incidence/unit-distance-dense configurations. Direct extension of the Guth–Silier
Q(√k) construction to **arbitrary number fields over Q** — exactly the universe
the run's exact coordinates occupy (`Q(sqrt3, sqrt11, sqrt33)`).

## Source

- *Sharp Szemerédi–Trotter constructions from arbitrary number fields*,
  Electronic Journal of Combinatorics 32(4) (2025), #P4.28, retrieved via
  `read_sources` (server-side; direct download blocked at the network boundary).

## What it establishes

### Nice bases
Let `K/Q` be a number field and `Lambda = {lambda_1, ..., lambda_n}` a basis of
`K` over `Q`. `Lambda` is a **nice basis** if every product `lambda_i lambda_j`
is a Z-linear combination of basis elements:

    lambda_i lambda_j = sum_k c_{i,j,k} lambda_k  (integers c_{i,j,k}).

Any **integral basis** is an example, and such a basis exists for every number
field. The coefficients `c_{i,j,k}` are what make products of coordinates stay
inside the field — the algebraic closure condition that produces the density.

### Construction over arbitrary number fields
The `Q(√k)` construction of Guth–Silier is generalised (via Elekes's unequal-size
product idea) to any nice basis `Lambda` of any number field `K`:

- Coordinates of points in `P = A_r(Lambda) x A_{N/r}(Lambda)` are written in
  the basis: a field element `m = sum_k m_k lambda_k` with integer `m_k`,
  ranging in a GAP-sized window.
- Slopes `m = sum_k m_k lambda_k` and intercepts `b = sum_k b_k lambda_k` are
  drawn from the same field, with the nice-basis product rule keeping all
  products/mixtures inside the GAP structure.
- One shows `P` determines `Omega(N^2 / r^3)` `r`-rich lines for `r <= sqrt{N}`
  (Theorem 3 of that source), matching the Szemerédi–Trotter bound.

### Key structural principle (the load-bearing idea)
The density comes from **products of field elements closing inside the basis**.
A transcendental replacement for `sqrt{k}` would make the construction fail —
the algebraic structure, not mere size, is what makes many points incident with
many lines. As the Guth–Silier paper states it: replacing `√k` by a
transcendental number makes the construction far from sharp.

## Why it matters here

- The run's exact coordinates live in `Q(sqrt3, sqrt11, sqrt33)` — a number
  field. This source proves (as a technique, not a claim about the Hadwiger–
  Nelson answer) that **algebraic number fields are the right universe** for
  generating incidence-dense, rigid configurations: the extremal behaviour of
  the neighbouring incidence theory concentrates exactly on algebraic point
  sets closed under products.
- It gives the run's construction engine a proven closure recipe: choose bases
  closed under products (nice bases), draw coordinates/slopes/rotations from the
  field, and the configuration inherits the rigidity that makes unit distances
  abundant.
- It generalises Guth–Silier's `Q(√k)` to the composite/extension fields the
  Moser-spindle construction already needs (`sqrt33 = sqrt3 * sqrt11`).

## Basis and status

- Statements, definition of nice basis, and construction = sourced (retrieved
  verbatim). Peer-reviewed (EJC 2025).
- Not re-verified computationally here (asymptotic construction).

## Claim block

```claim
id: number-field-extremal-constructions
statement: Sharp Szemerédi-Trotter-type incidence constructions exist over any
  number field K/Q using a nice basis Lambda (an integral basis always
  qualifies): the point set A_r(Lambda) x A_{N/r}(Lambda) with slopes and
  intercepts drawn from the field's Z-span determines Omega(N^2/r^3) r-rich
  lines for r <= sqrt N. The algebraic closure of the basis (products stay in
  the field) is what produces the density; replacing the algebraic generator by
  a transcendental makes the construction collapse.
hypotheses: K a number field over Q, Lambda a basis closed under products
  (e.g. any integral basis); points/slopes/intercepts in the Z-span of Lambda.
holds-here: YES — the run's exact coordinates are in the number field
  Q(sqrt3, sqrt11, sqrt33); this source shows algebraic-field point sets closed
  under products are exactly where incidence/unit-distance density concentrates.
status: asserted-by-source (EJC 2025, arbitrary-number-field Szemerédi-Trotter
  constructions).
bearing: the structural recipe for the construction engine — use an integral
  basis closed under products (the run's Q(sqrt3, sqrt11, sqrt33) already has
  sqrt33 = sqrt3 sqrt11), draw coordinates and rotations from it, and density
  follows from algebraic closure, not from size or randomness.
anchor: research/sources/szemeredi-trotter-arbitrary-number-fields.md
falsifies: a correct construction where replacing the algebraic generator by a
  transcendental preserves the sharp incidence count — would contradict the
  stated algebraic-structure necessity; the sources assert the opposite.
```
