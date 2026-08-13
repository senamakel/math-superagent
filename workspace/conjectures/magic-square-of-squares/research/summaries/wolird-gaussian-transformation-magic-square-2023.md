> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/wolird-gaussian-transformation-magic-square-2023.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2310.12164 | converted from PDF -->

A New Transformation of the Magic Square of
Squares

Christian Wolird
chris.wolird@email.ucr.edu

July 2023

Abstract
We show arithmetic triplets of Gaussian squares are in 3-to-1 corre-
spondence with Pythagorean triples thereof. This correspondence would
transform a solution to the Magic Square of Squares puzzle into a larger
structure of perfect Gaussian squares. In particular, we obtain the back-
wards result that a puzzle solution would generate non-trivial near-miss
solutions in the Gaussian integers. Results are applied to popular near-
misses.

1 Triples and Triplets

Sometimes three perfect squares form an evenly spaced triplet.

Figure 1: Arithmetic triplets.

For brevity, we call such a creature an arithmetic triplet (of squares unless
specified otherwise). In 1225 Fibonacci published The Book of Squares describ-
ing, among other things, a connection between these arithmetic triplets and
their more popular relative, the Pythagorean triple.
Specifically, there’s a 1-to-1 correspondence where the hypotenuse-square of
any Pythagorean triple is also the middle-square of an arithmetic triplet (and
the other way round).

A2 + B2 = C 2 ⇒ (A + B)2 − C 2 = C 2 − (A − B)
2

( L+R
2 )2 + ( L−R
2 )2 = C 2 ⇐ L
2 − C 2 = C 2 − R2

1arXiv:2310.12164v1  [math.HO]  1 Oct 2023
Figure 2: Arithmetic triplet and Pythagorean triple correspondence examples.

Because we’re concerning ourselves with integer solutions here, notice that
L±R
2 must be an integer since L
2 + R2 = 2C 2 means that L and R are both odd
or both even.

Figure 3: The general arithmetic-Pythagorean correspondence.

2 Unfolding

Over the integers, this correspondence is like a lawn chair folded flat. To see its
real shape, we can unfold in the complex plane.

Figure 4: The arithmetic-Pythagorean correspondence “unfolded” into Z[i].

2

With Pythagorean triples of integers, one square, C 2, is doomed to be the
hypotenuse and remain forever alone. But with Pythagorean triples of Gaussian
integers1, the squares can be collected all together.

(8 − 4i)
2 + (4 + 7i)
2 = (4 − i)
2

⇓

(4 − i)
2 + (4 + 8i)
2 + (7 − 4i)
2 = 0

Whereas before, an integer Pythagorean triple (A, B, C) meant a solution
to A2 + B2 = C 2, we now think of a Gaussian Pythagorean triple (α, β, γ)
as a solution to α2 + β2 + γ2 = 0, acknowledging no one square doomed to
hypotenusity. Thus we create three Gaussian arithmetic triplets from any one
Gaussian Pythagorean triple by treating each of α, β, and γ as the “hypotenuse”
in turn. (4 − i)
2 + (4 + 8i)
2 + (7 − 4i)
2 = 0

⇓

(4 − i)
2 = (8 − 4i)
2 + (4 + 7i)
2

(4 + 8i)2 = (1 + 4i)2 + (4 + 7i)2

(7 + 4i)2 = (1 + 4i)2 + (8 − 4i)2

⇓

(12 + 3i)
2 − (4 − i)2 = (4 − i)
2 − (4 − 11i)2

(5 + 12i)
2 − (4 + 8i)
2 = (4 + 8i)
2 − (3 + 3i)
2

(9)
2 − (7 + 4i)2 = (7 + 4i)2 − (7 + 8i)2

The arithmetic-Pythagorean correspondence is thus 3 -to-1 in the Gaussians.
Any two arithmetic triplets resulting from the same Pythagorean triple, we call
siblings. The general correspondence can there be visualized (see Figure 4) as
a triangle in the complex plane having

1. its centroid at zero,

2. its vertices at perfect integer squares,

3. and vertices which are themselves the midpoints of three line segments
having perfect integer squares for endpoints.

As far as the author could find, the existing treatments of Pythagorean
Triples over the Gaussians (such as in [1]) make no mention of these arithmetic
triplets.

1Complex numbers with integer parts: 2 + i, −17 + 5i, 83i, etc.

3

For an instance in the wild, we plot the prior algebraic example:

Figure 5: Plot of (4 − i)2 + (4 + 8i)2 + (7 − 4i)
2 = 0 and the arithmetic triplets
it generates.

3 The Magic Square of (Gaussian) Squares

Figure 6: The Lo Shu magic square (left) and the general Magic Square of
Squares template (right).

The ever-loved and ever-frustrating “Magic Square of Squares” puzzle is the

*[excerpt ends; 7272 characters not shown — see `research/sources/wolird-gaussian-transformation-magic-square-2023.full.md`]*
