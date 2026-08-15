# REFUTED: G-threshold-shadow — the Hamming ball is not extremal for |O_{<=d}|

Status: `refuted` — concrete counterexample, checked by hand (entirely exact
structural computation, not enumeration).

## The lemma attacked

`G-threshold-shadow` (skeleton `bipartite-threshold-shadow`):

> For each n and 0 ≤ d ≤ n, the function
> A ↦ |O_{≤d}(A)| = |{x ∈ O : |N(x)∩A| ≤ d}|, over A ⊆ E with |A| = a,
> is maximised by a Hamming ball in E (equivalently an initial segment of the
> simplicial or colex order).

## The counterexample (n=4, d=1, a=2)

Take `A = {0000, 1111}` (vertex integers 0 and 15). Both have even weight, so
`A ⊆ E`, and `|A| = 2`. This is **not** any Hamming ball and **not** any initial
segment of a weight order (1111 is the maximum-weight element of E).

- Neighbours of `0000` = {1000, 0100, 0010, 0001} = {8,4,2,1}, four odd vertices.
- Neighbours of `1111` = {0111, 1011, 1101, 1110} = {7,11,13,14}, four odd vertices.
- Since 0000 and 1111 are at Hamming distance 4 (antipodal), they share **no**
  common neighbour. Together their neighbours are exactly all 8 odd vertices O.

So every odd vertex x has `|N(x) ∩ A| = 1 ≤ 1`, hence
`|O_{≤1}(A)| = 8 = |O|`, the global maximum.

Every size-2 initial segment of E (simplicial/colex order, by weight) is
`{0000, w}` with w a weight-2 vertex; the two weight-1 neighbours of w are also
adjacent to 0000, so exactly two odd vertices have `|N(x)∩A| = 2` and the count
is `|O_{≤1}(initial segment)| = 6`.

**8 > 6**: A beats every Hamming ball / initial segment. The lemma is false as
stated.

## The true extremal shape (structural finding)

The threshold shadow `|O_{≤d}(A)|` is maximised not by a *concentrated* A (a
ball) but by a *spread-out / antipodal* A (here the remote pair 0000,1111).
This is the opposite geometry from Harper's vertex-boundary phenomenon, and it
is exactly why the threshold-shadow quantity is not governed by the classical
isoperimetric ball family.

## Bearing on the skeleton

G2 was supposed to supply `U_d(a)`, an upper bound on `|O_{≤d}(A)|` valid for
every A, to feed G1's contrapositive. If `U_d(a)` is taken at the Hamming ball
value it is **not** a valid upper bound: at n=4, d=1, a=2 the ball gives 6 but
the true maximum is 8. The G1 inequality `|O_{≤d}(A)| ≤ 2^{n-1} − a` (here
8−2=6) correctly fails for `A={0000,1111}` (8 > 6), which is *consistent* with
f(4)=2 but shows the ball is the wrong extremal family. The skeleton's own
fallback — "exhibit any explicit order whose initial segments majorise
|O_{≤d}|" — is therefore required; a ball/weight order does not do it.

Note: this refutes the *lemma as stated* but not the *goal* (f(n)=ω(log n)).
The skeleton anticipated the fallback. The finding locates the obstruction: an
upper bound on the threshold shadow cannot be read off the simplicial order.

## Machine evidence

`code/refute/mech_prop8.p` → `find_counterexample`: **refuted** (CounterSatisfiable)
for the propositional core (all 8 odd vertices le1). The numeric-constant
full-cube encoding fell back to `undecided` (the model finder does not search
domains large enough to carry 16 distinct cube constants), so the full cube
structure was verified by the hand computation above instead, which is exact.

```claim
id: threshold-shadow-ball-not-extremal
statement: For n=4, d=1, a=2, A={0000,1111} ({0,15}) subset E with |A|=2 has
  |O_{<=1}(A)| = 8 = |O|, a global maximum. Every size-2 initial segment of E
  (Hamming ball / simplicial or colex order) has |O_{<=1}(A)| = 6. Hence the
  function A |-> |O_{<=d}(A)| is NOT maximised by a Hamming ball; G-threshold-
  shadow is false as stated. The true extremal family is antipodal/spread-out.
hypotheses: n=4, d=1, a=2; E = even-weight vertices, O = odd; |O_{<=d}(A)| =
  |{x in O : |N(x) cap A| <= d}|.
holds-here: yes (this is exactly the setting of the lemma it refutes)
status: checked (hand computation: 0000's 4 odd neighbours and 1111's 4 odd
  neighbours partition O, antipodal so no shared neighbour => every odd vertex
  has exactly 1 neighbour in A => count 8. Initial segment {0000,w}: two weight-1
  neighbours of w also adjacent to 0000 => count 6. Propositional machine core
  refuted via find_counterexample.)
bearing: kills G2-as-stated (ball extremal family); requires the skeleton's
  fallback order rather than the simplicial order. Does NOT refute the goal.
falsifies: the lemma G-threshold-shadow in its current formulation.
anchor: code/refute/threshold_shadow_finding.md, code/refute/mech_prop8.p
```
