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
challenge of arranging nine distinct integer squares in a 3 × 3 grid so that the
three numbers in each column, row, and diagonal add to the same total (yet
unsolved for both ordinary integers and Gaussians).

4

An important side-effect of these rules is that the magic total must be triple
the middle number. By algebraic rearrangement,

3T = (A2 + M 2 + a
2) + (B2 + M 2 + b2) + (C 2 + M 2 + c
2)

= (A2 + B2 + C 2) + (M 2 + M 2 + M 2) + (a
2 + b
2 + c
2) = 2T + 3M 2

Or instead, we may offer a more intuitive visual proof:

Figure 7: A visual proof that T = 3M 2.

This side-effect in turn means any central sum (i.e. the sums containing the
center) must form an arithmetic triplet. Taking a diagonal for example,

A2 + M 2 + a2 = T = 3M 2

⇓

A2 − M 2 = M 2 − a
2

All together, this means a magic square of Gaussian squares forms a slant
3 × 3 grid2 in the complex plane, containing 8 arithmetic triplets.

Figure 8: General form of a magic square of Gaussian squares plotted when in
the complex plane.

2Called a 3x3 general arithmetic progression, or GAP, in related articles such as [2].

5

And from these 8 arithmetic triplets, we may construct another 16 using the
3-to-1 arithmetic-Pythagorean correspondence. Taking the same diagonal for
example, A2 − M 2 = M 2 − a
2

⇓
( A + a
2 i + M )2 − ( A − a
2
 )2 = ( A − a
2
 )2 − ( A + a
2 i − M )2

( A − a
2 i + M )2 − ( A + a
2
 )2 = ( A + a
2
 )2 − ( A − a
2 i − M )2

Thus any Magic Square of Squares necessarily brings into existence, not 8, but
rather 24 Gaussian arithmetic triplets.
To maintain a distinction within these 16 new arithmetic triplets, we call
8 of them the older siblings and 8 of them the younger siblings. Specifically,
the arithmetic triplets having sums at their centers, like ( A+a
2 )2, are the older
siblings. And the arithmetic triplets having differences at their centers, like
( A−a
2 )2, are the younger siblings.

Figure 9: A slant grid (first quadrant) with the older siblings (third quadrant)
and younger siblings (second/fourth quadrant) it generates.

These siblings can be generated from any 3 × 3 slant grid in the complex
plane. And if the slant grid is composed of perfect squares, then so too will its
siblings be. But alas, no 3 × 3 magic square of Gaussian squares has been found
and the visuals presented here are of non-perfect squares3.

3For visual clarity, we are actually displaying a rotation of the older sibling, which would
normally also sit in the 1st quadrant. I.e. displaying −( A+a
2 )2 = ( A+a
2i )2 instead of ( A+a
2 )2.

6

4 From Solutions to Misses

There is an abundance of “near-miss solutions” to the Magic Square of Squares
puzzle online[3][4].

Figure 10: Two well known near-misses: the Bremner square (left) and the
Parker square (right).

To be clear, by a “near-miss”, we mean a 3 × 3 grid of numbers that nearly
meets the constraints of the Magic Square of Squares puzzle, say by having
duplicates, a mismatched sum, or a few non-square entries.
Interestingly, we can find near-misses in the siblings of a true Magic Square of
(Gaussian) Squares. Zooming in on the older siblings from the previous section,

Figure 11: The older siblings of an arbitrary slant grid.

7

Six of the arithmetic triplets depicted above seem to form slant grids.

Figure 12: Two near-misses amongst older siblings.

So normally, one might solve a puzzle by starting with a near-miss and
creating a true solution from it. But our 3-to-1 correspondence indicates that
oddly the reverse is true of the Magic Square of Squares. That is, if one finds a
solution, there is a good chance it will generate a handful of near-misses. The
Magic Square of Squares thus has the mischievous characteristic that it hands
you more hints as soon as you’ve solved it.
But are these really always near-misses? Indeed, from looks alone, it seems
we have two new slant grids. Sadly each is slightly kinked. For instance, let’s
inspect the red pseudo-grid algebraically. The midpoints of the red line segments
are ( D + b
2
 )2, ( c + C
2
 )2, and ( B + d
2
 )2

If we had a true slant grid, these three terms ought to form an arithmetic triplet
themselves. That is, we ought to have

( D + b
2
 )2 + ( B + d
2
 )2 = 2
( C + c
2
 )2

However, the true relationship between these terms is

( D + b
2
 )2 + ( B + d
2
 )2 = (D2 + B2) + (d
2 + b2) + 2Db + 2Bd
4

= 2c
2 + 2C 2 + 2Db + 2Bd
4

= 2
( C + c
2
 )2 + Db + Bd − 2Cc
2

8

which differs from a true arithmetic triplet by the error term

Db + Bd − 2Cc
2

To see why Db + Bd − 2Cc is nearly zero is algebraically tedious. But the
following derivation will do.

(Db + Bd − 2Cc)(Db + Bd + 2Cc) = (Db + Bd)
2 − (2C 2)(2c2)

= (D2b2 + 2BbDd + B2d2) − (B2 + b
2)(D2 + d2)

= 2BbDd + (D2b2 + B2d2) − (B2d2 + D2b2) − B2b
2 − D2d
2

= −(B2b2 − 2BbDd + D2d
2) = −(Bb − Dd)2

In particular, from this we can rewrite our error term as

Db + Bd − 2Cc
2 = − (Bb − Dd)
2

2(Db + Bd + 2Cc)

However, this error is only small if our magic square is distanced from the
origin. For instance, if we shift the slant grid from the prior figures to overlap
with the origin, pseudo-grids are no longer present among the siblings.

Figure 13: A slant grid covering the origin (blue) along with its older/younger
siblings (green/red) amongst which, there are no near-misses.

9

5 Back to Reality

Any normal Magic Square of Squares sits on the real number line. And the real
number line sits in the complex plane. So we can even generate the complex
siblings of a real Magic Square of Squares. As no true solution has yet been
found, we show here the siblings of two near-misses, the Bremner square and
the Parker square (see Figure 10).

Figure 14: Siblings of the Bremner square.

Figure 15: Siblings of the Parker square.

10

The interesting bit here is that the personality of each near-miss carries over
to its siblings. The Bremner Square has perfect sums and thus its siblings are
made of perfect arithmetic triplets. But the Bremner Square has two non-square
entries and so its siblings consist only partially of perfect squares.
The Parker Square, on the other hand, has perfectly square entries and thus
its siblings are made entirely of perfect Gaussian squares. However, the Parker
Square fails to have perfect sums and thus its siblings have a few kinks. And the
Parker square fails to have totally distinct entries and thus so do its siblings.
So do these siblings tell us anything about the existence of the Magic Square
of Squares? Not that the author sees directly. The author simply wished to make
known here the rather spirited personality which the Magic Square of Squares
seems to take on in the Gaussians. And the author would be glad to see more
serious analyses of the puzzle over the Gaussians in the future.

References

[1] James T. Cross (1986) Primitive Pythagorean Triples of Gaussian Integers,
Mathematics Magazine

[2] Javier Cillereulo & Andrew Granville (2006) Lattice Points on Cir-
cles, Squares in Arithmetic Progressions and Sumsets of Squares,
arXiv:math/0608109 [math.NT]

[3] Christian Boyer, The Magic Square of Squares,
http://www.multimagie.com/English/SquaresOfSquares.htm

[4] Matt Parker, (2016) The Parker Square, Numberphile,
Interview by Brady Haran,
https://www.youtube.com/watch?v=aOT_bG-vWyg

11
