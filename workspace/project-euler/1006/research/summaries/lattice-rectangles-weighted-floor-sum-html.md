# Babichev & Babichev — *Counting all lattice rectangles in the square grid in near-linear time* (arXiv:2604.22456)

Source: https://arxiv.org/html/2604.22456v2 (full text; the PDF is
https://arxiv.org/pdf/2604.22456). Landing page mirror at
`research/sources/lattice-rectangles-weighted-floor-sum-ar5iv.full.md`
(abstract only — the HTML file is the real content).

## What this source establishes

Counting axis-parallel AND tilted lattice rectangles in the n×n grid
(computational geometry). The object of interest to PE1006 is not the
rectangle count but the **floor-sum machinery developed as the method**:

**The six-moment kernel (eq. 5, Section 5.1).** For integers N ≥ 0, m ≥ 1,
a, b ≥ 0 define

  H_{p,q}(N; m, a, b) = Σ_{t=0}^{N−1} t^p · ⌊(a·t + b)/m⌋^q

for (p,q) ∈ {(0,1),(1,1),(2,1),(0,2),(1,2),(0,3)} — i.e. all moments with
total weighted degree p+q ≤ 3.

- **Lemma 4 (affine closure):** reducing a, b mod m expresses any H_{p,q}
  as a linear combination of states of the same six-state family plus
  ordinary polynomial sums.
- **Lemma 5 (reciprocal closure):** the transposed-staircase step (the
  Euclidean "flip") maps the family to itself — the reciprocal floor
  g(t) = ⌊(m·t + m−b−1)/a⌋ produces H_{p',q'}(Y; a, m, m−b−1) with (p',q')
  still in the family.
- **Corollary 6 (O(log n) evaluation):** the recursion alternates affine
  normalization and the reciprocal step; each cycle strictly decreases the
  larger Euclidean parameter (m → a < m), so depth is O(log m) = O(log n),
  each step O(1) arithmetic on the constant-size moment family. **Closed:
  no moments outside the family are generated.**

Also: sign reversal lemma (Lemma 3) converting negative-slope interval sums
into the kernel; the ten-moment weighted floor-sum reduction (Section 6) —
the O(n log³ n) algorithm with the same closure principle applied to
geometric/weighted sums; the constant-size "O(1) state size" recursive
floor-sum kernels.

## What it implies for PE1006

This is the **primary, proof-carrying literature statement of the structural
fact the run's O(log) primitive rests on**: finite floor-sum moment families
are closed under the affine + reciprocal Euclidean steps, so
Σ t^p ⌊(at+b)/m⌋^q is evaluable in O(log n) with a constant-size state. The
tuple directive 2 must carry — (count, Σ x^j, Σ x^j⌊·⌋, Σ x^j⌊·⌋²) — is (a
geometric-weight variant of) the same closure, now anchored to a
peer-written arXiv treatment with proofs. The existing operational anchors
(OI-wiki / fhq / LOJ138 / AtCoder `floor_sum`, with the exact monoid
merge-and-flip recursion and geometric weights x^t) remain the *how*; this
paper is the *why it is O(log) and why the family is closed*.

**Honest scope note (not a supersession):** the paper's kernel uses
*polynomial* index weights t^p. The run's sums use *geometric* weights
x^t = 10^{−t} mod M in the index (directive 2's 10^{k−1−j} factors). The
closure principle is the same (constant-size state, affine + reciprocal
steps, O(log) depth), but the geometric-weight monoid is stated exactly in
the fhq/LOJ138/AtCoder sources, and the fact that x is a unit mod M
(gcd(10,M)=1) is what keeps geometric weights well-defined. Use this paper
as the theorem-level anchor for the *family-closure* claim; use the
OI-wiki/fhq sources for the *geometric-weight recursion* the solver codes.

## Claims anchored here

Corroborates `governing-universal-euclidean` / `universal-euclidean-geometric-floor-sum`
(Lemmas 4–5, Corollary 6: six-moment floor-sum family closed under affine +
reciprocal Euclidean steps, O(log) evaluation, constant-size state).

## What it does NOT establish

- Does not state the geometric-weight (x^t) version of the kernel; that
  remains anchored to the OI-wiki/fhq/LOJ138/AtCoder sources.
- Does not state anything about Sturmian words, the Fibonacci word, or
  Ψ(k).
- Does not state the A(d) autocorrelation counting (that is the
  Alessandri–Berthé three-gap/three-distance home).