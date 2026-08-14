# Structure theorem for Minkowski sums of unit-distance graphs

**Status**: derived exactly here; computationally verified against the
calibrated oracle `code/brute.py::unit_graph` by `code/verify_minkowski.py`
over the exact field Q(√3, √11) — five concrete (A, B) pairs, every ordered
pair of distinct summands `((a1,b1),(a2,b2))` tested by both the derived
characterisation (criterion (*)) and the oracle, with full agreement on the
edge set. All coordinates are exact field elements; there is no floating point
anywhere in either computation.

## 0. Setting, notation, and the exact identity

Let `A, B ⊂ R²` be **finite, non-empty** point sets. The Minkowski sum is

    A + B = { a + b : a ∈ A, b ∈ B }.

Identify `R²` with `C`. For `d, e ∈ R²` write

    u = |d|² = d·d        (Euclidean squared norm),
    ⟨d, e⟩ = Re(d·conj(e)) = Re(conj(d)·e)   (real inner product).

For two summands `(a1, b1), (a2, b2) ∈ A × B` with differences

    d = a1 − a2,   e = b1 − b2,

the squared distance between the two sum points is, by direct expansion,

    |(a1 + b1) − (a2 + b2)|² = |d + e|² = (d + e)·(d + e)
                             = d·d + e·e + 2(d·e)
                             = u + v + 2⟨d, e⟩.

This is an **identity over R**, valid for all `d, e`, and it is exact — the
parallelogram law `|d+e|² = |d|² + |e|² + 2⟨d,e⟩` specialised to the pair
`(d, e)`. It is the only identity the whole structure theory uses.

**Characterisation (the claim being proved).** For finite non-empty
`A, B ⊂ R²` and any two pairs `(a1, b1) ≠ (a2, b2) ∈ A × B`:

    (a1 + b1) ~ (a2 + b2)   (unit distance in R²)
        ⟺   |(a1 − a2) + (b1 − b2)| = 1
        ⟺   |d|² + |e|² + 2⟨d, e⟩ = 1
        ⟺   u + v + 2⟨d, e⟩ = 1.          (*)

*Proof.* First equivalence: `d + e = (a1 + b1) − (a2 + b2)` is a rearrangement
of the differences, so the unit-distance condition is exactly `|d + e|² = 1`.
The second and third are the identity above. □

**Convention remark on the displayed "u + v + 2·⟨d, e⟩ = 1".** The coefficient
2 is correct in the real-inner-product convention `⟨d, e⟩ = Re(d·conj(e))`; in
the complex-bilinear convention the same number is written
`d·conj(e) + conj(d)·e = 2 Re(d·conj(e))`. Both readings agree; the real
convention is used throughout this note and in the verifier.

**Reduction to a pair of difference vectors.** The criterion (*) depends on
`(a1, b1), (a2, b2)` **only through `(d, e) = (a1 − a2, b1 − b2)`**. Hence the
whole unit structure of `A + B` is a predicate on the Cartesian product of the
two difference sets

    ΔA = A − A = { a1 − a2 : a1, a2 ∈ A },   ΔB = B − B,

namely: the unordered pair `{a1+b1, a2+b2}` is an edge of `G_{A+B}` iff
`(d, e) ≠ (0, 0)` and `(d, e) ∈ ΔA × ΔB` satisfies `u + v + 2⟨d,e⟩ = 1`.
(Note `d + e = 0` gives squared distance 0 ≠ 1, so an edge can never have
coinciding sum points: the criterion automatically produces no loops.) This
reduction is the exact computational content of the theorem and is precisely
what `code/verify_minkowski.py` checks pair by pair against the oracle.

## 1. Which pairs (d, e) of difference vectors can contribute

From `|d + e|² = 1`, `u = |d|²`, `v = |e|²`, and the triangle inequality
`| |d| − |e| | ≤ |d + e| ≤ |d| + |e|`:

**(1a) Triangle restrictions.** A contributing pair must satisfy

    |d| ≤ |e| + 1,   |e| ≤ |d| + 1,   1 ≤ |d| + |e|,

i.e. with `r = |d|`, `s = |e|`: `|r − s| ≤ 1 ≤ r + s`. The unit segment
`d + e` is a side of a (possibly degenerate) triangle with sides `r, s, 1`.

**(1b) Degenerate summands are automatic.** `u = v = 0` gives `0 ≠ 1`
(excluded anyway by distinctness of the pairs). `u = 0, v = 1` gives
`|d + e|² = 1` automatically: an edge `(a1 + b1) ~ (a1 + b2)` consists of two
vertices sharing the summand `a1 ∈ A`, differing only in the B-coordinate —
exactly the unit edges of `B`, each replicated `|A|` times. Symmetrically,
`u = 1, v = 0` are exactly the unit edges of `A`, replicated `|B|` times.

**(1c) Extreme pairs are rigid.** If `u = v = 1` then
`|d + e|² = 2 + 2⟨d, e⟩ = 1` forces `⟨d, e⟩ = −1/2`: two unit difference
vectors contribute **iff** they meet at angle exactly 2π/3 (or −2π/3),
`e = d·e^{±2πi/3}`. These are the only "genuinely new" (cross) edges.

**(1d) General norm pairs fix at most two angles.** For any allowable
`(r, s)` (triangle with side 1), the identity forces
`cos θ = (1 − r² − s²)/(2rs)` for the angle `θ = ∠(d, e)`, so at most two
angles modulo 2π per `(r, s)`; the edge set of `A + B` is organised by the
finite table of `(r, s, §angle)` types, with multiplicities given by how many
difference pairs realise each type. In particular `(u, v) = (1/2, 1/2)` with
`d ⟂ e` contributes (cos θ = 0, `1/2 + 1/2 + 0 = 1`) — an edge that is **not**
of any strong-product type. This is why equality with the strong product
(§4) needs the hypothesis that all mutual squared distances of `A` and of `B`
lie in `{0, 1}`.

## 2. Special cases: u, v ∈ {0, 1} (both A and B unit-distance graphs)

"u, v ∈ {0, 1}" means: **every** pair of points of `A` is at squared distance
0 or 1, and likewise for `B` — i.e. `A` and `B` each have diameter at most 1
and every pair of distinct points is either at distance 1 (an edge of the
unit-distance graph) or not at unit distance. Concrete such sets: any subset
of an equilateral-triangle lattice taken from a hexagonal cluster (e.g.
`{0, 1, u}`, `u = e^{iπ/3}`; or the 7-point wheel `{0, ±1, ±u, ±(u−1)}` minus
the opposite pairs at distance √3 — see §5 case 5 note). Note the rhombus
`{0, 1, u, 1+u}` does **not** qualify (its diagonal `0–(1+u)` has squared
length 3); the case analysis below applies to it only through the general
criterion (*), which the verifier also checks on it.

**Proposition (u, v ∈ {0,1} classification).** Let `A, B ⊂ R²` be finite
non-empty with `|x − x′|² ∈ {0, 1}` for all `x, x′ ∈ A` and likewise for `B`.
Then for distinct pairs `(a1,b1) ≠ (a2,b2) ∈ A × B`, with
`d = a1 − a2`, `e = b1 − b2`:

    |(a1+b1) − (a2+b2)|² = 1
        ⟺  (u, v) = (1, 0)  or  (u, v) = (0, 1)  or
            (u, v) = (1, 1) and ⟨d, e⟩ = −1/2.

*Proof.* `u, v ∈ {0, 1}` and `u + v + 2⟨d,e⟩ = 1`. `(0,0)` gives 0 ≠ 1.
`(1,0)` and `(0,1)` give `1 + 0 + 0 = 1`, automatic (in `(1,0)`, `e = 0`).
`(1,1)` gives `2 + 2⟨d,e⟩ = 1 ⟺ ⟨d,e⟩ = −1/2`. □

**Interpretation.** (i) `u = 1, v = 0`: `b1 = b2` and `a1 ~ a2` in `G_A` — the
unit edges of `A`, each replicated once per `b ∈ B`. (ii) `u = 0, v = 1`:
symmetrically the unit edges of `B`, replicated once per `a ∈ A`. (iii)
`u = v = 1`: cross edges, only at mutual angle ±2π/3, i.e. when two unit
segments, one from `ΔA` and one from `ΔB`, are oriented 120° apart.

**Corollary (120°-while-sum lemma).** If `a1 ~ a2` in `A` and `b1 ~ b2` in
`B`, then `(a1 + b1) ~ (a2 + b2)` iff `⟨d, e⟩ = −1/2`, i.e. the oriented
segments make angle exactly 120°. The sum of two unit differences is a unit
difference **only** at the 120° configuration — the precise sense in which
unit-distance structure is mostly lost under addition, and exactly the sense
in which a little survives.

## 3. B a rotated copy of A; the rotation enters only through ⟨d, R(e)⟩

Let `B = R(A)` with `R(z) = e^{iθ} z` a rotation about the origin.

**General rotated-copy criterion.** For `a1, a2 ∈ A`, `b1, b2 ∈ B = R(A)`,
write `d = a1 − a2 ∈ ΔA` and `e = b1 − b2 = R(d′)` for `d′ ∈ ΔA`. The theorem
gives

    (a1 + b1) ~ (a2 + b2)  ⟺  u + v + 2⟨d, R(d′)⟩ = 1,      (†)
    u = |d|²,  v = |d′|² = |R(d′)|².

The norm terms `u, v` are rotation-invariant; **all** dependence on `θ` sits
in the one inner-product term

    ⟨d, R(d′)⟩ = |d|·|d′|·cos(θ + φ),   φ = angle from d′ to d.

Since `cos` is 2π-periodic, each `(d, d′) ∈ ΔA × ΔA` and each target value
`c = (1 − u − v)/2` admits at most **two rotation angles θ modulo 2π**
(and none if `|c| > |d||d′|`). So a rotation is a finite list of exactly
computable angle knobs, one per difference-vector pair of `A`.

**Uniform-distance specialisation.** If additionally `|d| = |d′| = 1`
(`a1 ~ a2` in the original copy and `b1 ~ b2` in the rotated copy), (†)
becomes

    2 + 2⟨d, R(d′)⟩ = 1  ⟺  ⟨d, R(d′)⟩ = −1/2:

the rotated difference vector `R(d′)` must be at angle exactly ±2π/3 from
`d`. For a rotated copy of a unit-distance graph, every cross unit edge is
explained by "some difference vector of A, rotated by θ, lands at 120° from
another difference vector of A".

**The worked example as an instance.** The calibration graph (`problem.md`,
`code/brute.py`) is built from `A = {0, 1, u, 1+u}` (`u = e^{iπ/3}`, a unit
rhombus of two equilateral triangles) and its rotated copy
`B = e^{iθ}A` with `e^{iθ} = 5/6 + i√11/6`, designed so that
`sin(θ/2) = 1/(2√3)`, i.e. `|1 − e^{iθ}|² = 2 − 2(5/6) = 1/3`. The extra edge
is between the two far vertices `1+u` and `e^{iθ}(1+u)`. In the Minkowski-sum
view this is the summand-pair `((1+u, 0), (0, e^{iθ}(1+u)))` (both belong to
`A × B`, since `0 ∈ A` and `0 ∈ B`), with differences `d = 1+u`,
`e = −e^{iθ}(1+u)`. The criterion (†) gives, exactly,

    |d + e|² = |(1+u) − e^{iθ}(1+u)|² = |1+u|² · |1 − e^{iθ}|² = 3 · (1/3) = 1. ✓

Note the naive same-`a` pairing would be the WRONG pairing:
`|d + R(d)|² = |1+u|²|1 + e^{iθ}|² = 3·(2 + 2·5/6) = 11 ≠ 1`. The edge comes
from *different* `a`-coordinates and a *negated* rotated difference; the
correct statement is the pair-of-difference-vectors criterion (†), not any
single-vector formula.

**Design rule.** Given `A ⊂ R²`, the unit edges of `A + R(A)` are exactly
those pairs of difference vectors `(d, d′) ∈ ΔA × ΔA` whose rotated image
`satisfies |d|² + |d′|² + 2⟨d, R(d′)⟩ = 1`. Each `(d, d′)` contributes at most
two rotation angles modulo 2π; the rigid-construction search is the search
over those finitely many pairs and angle targets. This is the construction
engine stated as a theorem.

## 4. The strong product: exact survival criterion, containment, equality

**Definitions.** `G_A = (A, E_A)` with `E_A = {{a, a′} : |a − a′|² = 1}`;
`G_B` likewise. The **strong product** `G_A ⊠ G_B` has vertex set `A × B` and
an edge between distinct pairs iff

    (a1 = a2 or a1 ~_A a2)  AND  (b1 = b2 or b1 ~_B b2).

The **Minkowski-sum graph** `G_{A+B}` has vertex set `A + B` and edges
`{a1+b1, a2+b2}` iff `|(a1+b1) − (a2+b2)|² = 1`. The comparison map is

    Φ : A × B → A + B,   (a, b) ↦ a + b.

By construction, a strong edge has `(u, v) ∈ {(1,0), (0,1), (1,1)}` with
`(u,v) ≠ (0,0)` (both coordinates are each either coincident or at unit
distance, not both coincident). The identity (*) therefore decides every
strong edge exactly:

**Theorem (survival criterion — the correct, unconditional statement).**
For all finite non-empty `A, B ⊂ R²` and distinct summand pairs:

1. If `(u, v) = (1, 0)` or `(0, 1)`, then always
   `|(a1+b1) − (a2+b2)|² = 1`: the strong edge **survives unconditionally**
   (these are exactly the replicated unit edges of `A` and of `B`).
2. If `(u, v) = (1, 1)`, then
   `|(a1+b1) − (a2+b2)|² = 2 + 2⟨d, e⟩`, so the strong edge survives **iff**
   `⟨d, e⟩ = −1/2` (angle exactly 2π/3 or 4π/3 between `d` and `e`). This is
   necessary **and** sufficient — no other hypothesis is needed.
3. If `(u, v) ∉ {(1,0), (0,1), (1,1)}` — which cannot happen for a strong
   edge but can for a general pair — the sum distance² is `u + v + 2⟨d,e⟩`,
   and it equals 1 exactly when that equation holds (e.g. the
   `(u,v) = (1/2, 1/2), d ⟂ e` edge mentioned in §1d).

*Proof.* Each clause is the identity (*) evaluated at the stated `(u, v)`:
`1 + 0 + 0 = 1`, `0 + 1 + 0 = 1`, `2 + 2⟨d,e⟩ = 1` iff `⟨d,e⟩ = −1/2`. □

**Consequences for containment.**

- **Failure mode A — angle.** A strong edge with `u = v = 1` and
  `⟨d, e⟩ ≠ −1/2` is NOT an edge of `G_{A+B}` (its sums sit at distance
  `√(2 + 2⟨d,e⟩) ≠ 1`). This happens whenever the same difference direction
  (or any non-120° pair of unit directions) occurs in both `ΔA` and `ΔB` —
  and, because difference sets are centrally symmetric (`ΔB = −ΔB`), it is
  *generic*: e.g. `A = {0, 1, u}`, `B = ωA` (ω = e^{2πi/3}) both unit
  triangles, yet the strong edge `((1, 0), (0, −1))` has `d = e = 1`,
  `⟨d,e⟩ = 1`, so `|d + e|² = 4` and the edge does not survive. Consequently
  the naive claim "the sum graph contains the strong product" is FALSE in
  general, and even a 120°-rotated copy does not rescue it.
- **Failure mode B — collapse.** If `Φ` is not injective, distinct strong
  vertices map to the same point; a strong edge between two collapsing vertices
  becomes a loop (not an edge of `G_{A+B}`), and distinct strong edges can
  collide. Minimal example: `A = B = {0, 1}`: strong product is `K₄` on
  `{(0,0),(0,1),(1,0),(1,1)}`; `Φ` maps `(1,0)` and `(0,1)` both to `1 ∈ {0,1,2}`,
  so four edges collapse to the single edge `{0, 1}`... precisely:
  `G_{A+B}` is the path `0–1–2` with edges `{0,1}`, `{1,2}`; the diagonal
  strong edge `(0,0)~(1,1)` maps to `{0, 2}` which is not an edge
  (`|0−2|² = 4`), and the strong edge `(1,0)~(0,1)` maps to the loop `{1,1}`.
  Both failure modes occur in this one example.

**Theorem (exact survival — necessary AND sufficient, no hypotheses).**
For all finite non-empty `A, B`, let `Φ` map `G_A ⊠ G_B` to the complete
graph on `A + B`. Then for each unordered pair of distinct summands with
`(u,v) ∈ {(1,0),(0,1),(1,1)}`:

    {Φ(a1,b1), Φ(a2,b2)} is an edge of G_{A+B}
        ⟺  (u,v) ≠ (1,1)  or  ⟨d,e⟩ = −1/2,

and (the collapse clause) the two endpoints coincide only if `d + e = 0`, which
the criterion excludes (`|d+e|² = 0 ≠ 1`). Equivalently,

    Φ(G_A ⊠ G_B) — as an edge multiset on A + B — is obtained from
    G_A ⊠ G_B by (i) deleting exactly the (1,1)-edges with ⟨d,e⟩ ≠ −1/2
    and (ii) identifying vertices with equal sums;

nothing else is deleted, nothing else is added by the strong side.

*Proof.* Strong edges have `(u,v) ∈ {(1,0),(0,1),(1,1)}`; the survival
criterion applies verbatim; endpoint coincidence would require
`a1+b1 = a2+b2` i.e. `d + e = 0`, but survival forces `|d+e|² = 1`. □

**Theorem (equality `G_{A+B} = Φ(G_A ⊠ G_B)`, the useful sufficient form).**
Assume

- **(H1) injectivity:** `Φ : A × B → A + B` is injective (unique
  representation of sums);
- **(H2) diameter-box:** every mutual squared distance in `A` and in `B` lies
  in `{0, 1}` (so every difference has `u, v ∈ {0, 1}`);
- **(H3) 120°-closure on arising unit–unit pairs:** every pair
  `(d, e) ∈ (ΔA ∖ {0}) × (ΔB ∖ {0})` with `|d|² = |e|² = 1` arising from some
  pair of summands satisfies `⟨d, e⟩ = −1/2`.

Then, as graphs on `A × B ≅ A + B` (via `Φ`):

    G_{A+B}  =  G_A ⊠ G_B.

*Proof.* **(⊆, every Minkowski edge is strong):** a unit edge has
`u + v + 2⟨d,e⟩ = 1` with `(d,e) ≠ (0,0)`; by H2, `u, v ∈ {0,1}`; the identity
leaves only `(u,v) ∈ {(1,0), (0,1), (1,1)}` (as in §2), and in the `(1,1)`
case forces `⟨d,e⟩ = −1/2`. In every case `(a1,b1) ⊠ (a2,b2)`; H1 keeps the
two vertices distinct in `A + B`. **(⊇, every strong edge is a Minkowski
edge):** `(u,v) = (1,0)` gives distance² = 1; `(0,1)` gives 1; `(1,1)` gives
`1` by H3. H1 keeps endpoints distinct. □

**Why each hypothesis is genuinely needed** (concrete failures):

- Without H1: `A = B = {0, 1}` — collapse (failure mode B).
- Without H2: an edge of type `(u,v) = (1/2, 1/2)`, `d ⟂ e` — exists in
  `G_{A+B}` but is not a strong edge (e.g. `A = {0, (1/√2, 0)}`,
  `B = {0, (0, 1/√2)}`: `|(1/√2,0) + (0,1/√2)|² = 1`).
- Without H3: `A = {0, 1, u}`, `B = ωA` — the strong edge
  `((1,0),(0,−1))` with `d = e = 1` fails (failure mode A). Even a 120°-copy
  does not satisfy H3.

In particular, the task's naive suggestion that `A + B`'s graph "contains the
strong product" is false as a blanket statement, in exactly the two ways A and
B above; the precise truth is the survival criterion: the (1,0)/(0,1) strong
edges always survive, the (1,1) strong edges survive iff 120°, and equality
additionally requires H1, H2, H3.

## 5. What was verified, and how

`code/verify_minkowski.py` implements, in exact arithmetic over
`Q(√3, √11)` (the field `code/brute.py` works in), three independent
computations per case and asserts their agreement:

1. **Oracle edge set** `E_oracle` — dedupe `A + B` by exact field-element
   equality, call the calibrated `brute.unit_graph` (the verifier that
   certifies `|x − y|² == 1` as exact tuples of Fractions; calibrated on the
   Moser 7-vertex graph with 11 edges and χ = 4 — see
   `code/out/oracle_calibration.md`).
2. **Characterisation edge set** `E_char` — for every ordered pair of distinct
   summands `((a1,b1),(a2,b2))`, compute `d, e` in exact field arithmetic and
   declare an edge iff `|d + e|² == 1`, i.e. criterion (*).
3. **Strong-product edge set** `E_strong` — every distinct pair satisfying
   the strong-product rule, mapped through Φ; the program then checks the
   survival criterion §4 per edge (records which (1,1)-edges fail and which
   vertices collapse), reports H1/H2/H3 for the case, and asserts consistency
   of E_char and E_oracle.

Assertions: `E_char == E_oracle` (set equality) for all five cases, and the
survival criterion — strong edges with `(u,v) ≠ (1,1)` all present in the
oracle set; strong `(1,1)`-edges present iff `⟨d,e⟩ = −1/2`. Each case prints
the vertex count of `A + B`, `|E_oracle|`, `|E_strong|`, the number of
surviving vs deleted strong edges, the number of collapsed vertices (Φ
non-injective), and checks H1–H3.

The five concrete cases (exact coordinates, all in the oracle's field):

| # | A | B | what it tests |
|---|---|---|---|
| 1 | `{0, 1}` | `{0, 1}` | the minimal counterexample: collapse + angle failure; honest statement of §4 |
| 2 | `{0, 1, u}` (unit triangle) | `ω·A`, `ω = e^{2πi/3}` (120° copy) | rotated copy; shows H3 fails even here (strong edge `((1,0),(0,−1))`), tests the survival criterion on a v = 1 unit–unit pair with ⟨d,e⟩ = 1 |
| 3 | `A = {0, 1, u, 1+u}` (unit rhombus) | `e^{iθ}A`, `e^{iθ} = 5/6 + i√11/6` | the Moser/spindle rotation parameters — the worked example, in the field, criterion (†) produces the far-vertex edge |
| 4 | `A = {0, 1, u, 1+u}` | `B = A + (1+√3) + √11·i`? — no: `B = A + t`, `t = 1 + √3` (translation) | u,v classification when B is a translate of A (G_B = G_A), exact translation by non-unit vector, cross edges only at permitted angles |
| 5 | `A = {0, ±1, ±u, 1−u}` and `B = u·A` | 7-point wheel and its 60° rotation | dense case: many unit–unit difference pairs, cross-edge census against the 120° rule; also tests u,v ∈ {0,1} (wheel: all mutual squared distances in {0,1,3} — see note) |

(Degenerate/choice details are exactly as coded — the program prints the
actual point lists.)

### Note on case 5's "u,v ∈ {0,1}" box in §2

The wheel `W = {0, ±1, ±u, 1−u}` has mutual squared distances in
`{0, 1, 3}` — the opposite hexagon vertices at distance √3 are *not* unit and
*not* coincident, so `W` violates the `{0,1}` diameter box; only the sub
-triangles `{0, 1, u}`, `{0, u, 1−u}`, `{0, 1−u, −1}`, `{0, −1, −u}`, etc. are
candidatess for §2's hypotheses. §2 is verified *on* those sub-triangles via
case 2 and case 3's rhombus-triangle pairs; case 5 verifies the general
criterion (*) beyond the box. An honest §2-satisfying large set is
`{0, 1, u, −1, 1−u}` (a pentagon in the lattice: distances 0-1, 0-u, 0-−1,
0-(1−u): all 1 ✓; 1-u? no wait `|1 − u|² = 1` ✓; 1-−1: 4 ✗ — so not that
either; the §2 box genuinely limits A, B to small configurations, which is a
finding: the classification says cross edges force 120° angles, so large sums
need non-{0,1} norm pairs and the general criterion (*) — exactly what cases
3–5 exercise).

## 6. Where the naive statement needed a hypothesis — summary for the record

The task's suggested reading — "the unit-distance graph of A+B contains the
strong product of the graphs of A and B" — is **false without hypotheses** in
two independent ways; both are exhibited by `A = B = {0, 1}`:

- the diagonal strong edge `(0,0) ~ (1,1)` maps to the pair `{0, 2}` at
  distance 2 (angle failure: `u = v = 1`, `⟨d,e⟩ = 1 ≠ −1/2`);
- the strong vertices `(1,0)` and `(0,1)` collapse to one sum `1`
  (Φ non-injective).

The correct unconditional statement is the **survival criterion** (§4): the
`(1,0)`/`(0,1)` strong edges always survive; the `(1,1)` strong edges survive
iff `⟨d,e⟩ = −1/2`; and equality `G_{A+B} = G_A ⊠ G_B` holds under H1
(injectivity), H2 (diameter box `{0,1}`), H3 (120°-closure on arising
unit–unit pairs) — each hypothesis shown necessary by a concrete failure.
The pairwise characterisation (*), the `u,v ∈ {0,1}` classification (§2), and
the rotation rule (†) (§3) are unconditional.