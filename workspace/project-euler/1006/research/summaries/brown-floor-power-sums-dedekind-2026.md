# Brown — Sums of powers of the floor function and generalized Dedekind sums

Source: Steven Brown, "On a family of sums of powers of the floor function and
their links with generalized Dedekind sums", Notes on Number Theory and Discrete
Mathematics 32(1) (2026), 76–87, DOI 10.7546/nntdm.2026.32.1.76-87 (Open
Access CC-BY 4.0). Full text:
`research/sources/brown-floor-power-sums-dedekind-2026.full.md`
(converted from the journal PDF; arXiv version: 2507.11666).

## Objects

S_r(n, m) := Σ_{k=1}^{n−1} ⌊km/n⌋^r  (r ≥ 0; n, m positive integers).

## Statements it establishes

- **S_1 closed form** (well known): the coprimality case
  S_1 = ½(m−1)(n−1).
- **S_2 and S_3 closed forms** (Theorems 4.1, 4.3): for coprime a, b,
  explicit polynomial formulas plus the **reciprocity laws** they satisfy
  (swapping the roles of the two arguments), analogous to the classical
  Dedekind-sum reciprocity.
- **Theorem 4.2** (reciprocity for the auxiliary W): W_n(m) := Σ_{k=1}^{n−1}
  ⌊km/n⌋² follows a reciprocity law; Proposition 3.2 states the gcd-stripping
  rule W_n(m) = d²·W_b(a) + (1/4)n²(d−1)(b−1) for n = db, m = da, gcd(a,b)=1.
- **Proposition 5.1**: every S_r(b,a) is expressible as a sum of generalized
  Dedekind sums (Zagier's definition); the classical Dedekind sum gets a
  closed form via the Euclidean algorithm.
- Method: Euclidean-algorithm remainder sequences + Faulhaber sums + Zagier's
  generalized Dedekind sums δ(b; a_1,…,a_n).

## Relation to PE1006

- The sums S_r are exactly the *ung weighted* floor-power sums that appear when
  the geometric weight x^i (x = 10^{−1} mod M) is stripped off: directive 2's
  telescoped Ψ(k) is a linear combination of Σ x^j·⌊x_0+ja⌋ and
  Σ x^j·⌊x_0+ja⌋²-type terms; with x = 1 those are S_1, S_2 multiplied by
  10-powers. This paper's closed forms for S_1, S_2 and their reciprocity laws
  are the *no-weight* sanity baseline and a literature anchor for the
  "second moment of a floor sum" object.
- The gcd-stripping rule (Prop 3.2) is the same divisibility bookkeeping the
  Euclidean recursion performs at each step (extracting integer parts of a/c,
  b/c).
- Not the solving method: PE1006's sum requires the geometric weight x^i and
  arc-midpoint intercepts, which this paper does not treat. It anchors the
  algebra that the weighted monoid generalizes.