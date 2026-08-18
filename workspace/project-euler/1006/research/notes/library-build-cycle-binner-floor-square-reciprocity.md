# Library build cycle — Binner reciprocity: peer-reviewed anchor for the floor-sum second moment

## What was added

**Damanvir Singh Binner, "Reciprocity Relations for Summations of Squares of
Floor Functions and Fractional Parts of Fractions", arXiv:2107.08308 (2021).**

- `research/sources/bin̄ner-reciprocity-fulltext.full.md` (45949 B, the full
  HTML text)
- `research/sources/binner-reciprocity-floor-square-functions.full.md` (5930 B,
  the arXiv landing/abstract page — keep the fulltext as the authoritative copy)

This is a **peer-reviewed-math paper in number theory (arXiv math.NT)** giving
a direct reciprocity-theoretic treatment of *exactly* the second-moment floor
sums the PE1006 primitive is built on — closing a genuine gap, since the
geometric-weight monoid sources (OI-wiki, fhq, LOJ138, AtCoder) are
competitive-programming notes.

## What it establishes

For positive coprime `a`, `b` and natural `h`, with `q_i, r_i` the quotient and
remainder of `i·b / a`:

- `T1(a,b,h) = Σ_{i=1}^h {i·b/a}² = (1/a²)·Σ r_i²`
- `T2(a,b,h) = Σ_{i=1}^h i·⌊i·b/a⌋ = Σ i·q_i`
- `T3(a,b,h) = Σ_{i=1}^h ⌊i·b/a⌋² = Σ q_i²`

**Section 4 — the O(log) complexity (the go/no-go fact).**
- `T1` (the square of fractional parts) is evaluated in **O(log t)** steps,
  `t = max(a,b)`.
- `T2` (the weighted first moment Σ i·floor) in **O((log t)²)** steps.
- `T3` (the square of floors — the *second moment of the floor function*
  itself) is obtained from T1 and T2 via eq. (38) in **O((log t)²)** steps.
- The recursion is a Euclidean reciprocity: Theorem 3 (Binner 2020) gives
  `Σ_{i=1}^d ⌊i·b/a⌋ + Σ_{i=1}^K ⌊i·a/b⌋ = d·K` with `K=⌊bd/a⌋`, and Theorem 6
  gives the analogous reciprocity for the squares; each application swaps the
  roles of a,b — a Euclidean step, so depth is O(log t).

## Why it matters for PE1006

Directive 2's reduction writes Ψ(k) as a second moment of a geometrically
weighted floor sum `v(x) = ⌊x+ka⌋ − 10^{k−1}⌊x⌋ + 9·Σ_j 10^{k−1−j}⌊x+ja⌋`.
Expanding `v(x)²` over the k+1 arc-midpoint intercepts x produces sums of the
form `Σ x^j·⌊x_0+ja⌋` and `Σ x^j·⌊x_0+ja⌋²` — the geometric-weight versions
of Binner's T2/T3. Binner gives the *unweighted* (x^j = 1, i.e. at x=1) second
moment, its reciprocity relation, and the O((log t)²) bound: the exact
algebraical structure and the exact complexity the Euclidean monoid
generalises to geometric weights. It is the independence/anchoring companion
to the OI-wiki/fhq/LOJ138 monoid (whose merge-and-flip recursion is stated but
not peer-reviewed) and to Babichev–Babichev's polynomial-weight floor-sum
family closure.

**Scope boundary:** Binner treats the unweighted sums (coefficient 1), not the
geometric weights x^i = 10^{−i} mod M. The geometric-weight closure stays with
fhq/LOJ138/OI-wiki (and becomes *routine* once the unweighted case is an
accepted reciprocity theorem). Binner also fixes coprime (a,b), whereas the PE
recursion needs general (a,b,c) — the affine-normalisation extraction of
integer parts (the u^⌊b/c⌋, (a mod c) steps of the monoid) is the piece the
competitive-programming sources supply. So: Binner anchors *second-moment
floor-sum reciprocity & O(log)*; OI-wiki/fhq anchor *general (a,b,c) geometric
weights*.

## Answers

- Partially answers `citable-precise-statement-600d`, `citable-precise-
  statement-d2e7`, `citable-name-treatment-0c91`: strengthens the
  "perform this floor-sum computes in O(log)" claim with a peer-reviewed
  reciprocity theorem for the unweighted second moment.
