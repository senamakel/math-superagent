<!-- source: https://warwick.ac.uk/fac/sci/maths/people/staff/michaud/magisquarestalk.pdf | converted from PDF -->

Magic Squares of Squares

Philippe Michaud-Rodgers

WMS Talk

26.02.2019

What is a Magic Square?

Magic squares have been studied by Chinese mathematicians as far
back as 190 BCE.
Figure: The Lo Shu magic square.

4 9 2

3 5 7

8 1 6

Magic Squares of Squares: An Open Problem

Open Problem
Does there exist a magic square with nine distinct square entries?

History and Progress
▶ Euler solved the 4 × 4 case aﬃrmatively in 1770. In 1876
Edouard Lucas studied the 3 × 3 case.
▶ It is known that if a magic square of squares (with nine
distinct entries) does exist, then its central element has size
> 25 × 1024, so probably not! This is not a very convincing
argument...
▶ The problem has been studied for a long time using
elementary number theory techniques and traditional
magic-square constructions. My project looks at the
problem using algebraic geometry.

Euler’s 4 × 4 magic square of squares

The entries in each row, column, and main diagonal sum to 8515.

68
2 29
2 41
2 37
2

17
2 31
2 79
2 32
2

59
2 28
2 23
2 61
2

11
2 77
2 8
2 49
2

“Permettez-moi, Monsieur, que je vous parle encore d’un probl`eme
qui me paraˆıt fort curieux et digne de toute attention.”

Leonhard Euler in a letter to Joseph Lagrange (1770).

Algebra + Geometry = Algebraic Geometry!

Algebraic Geometry
Algebraic Geometry is, very broadly, the study of solutions of sets
of polynomial equations in many variables, using techniques from
(commutative) algebra and geometry.

The Algebra-Geometry Correspondence
Algebra: The polynomial ring k[x1, . . . , xn]
Geometry: Aﬃne Space k n(≈ An)
▶ The variety of a subset {f1, . . . , fm} ⊆ k[x1, . . . , xn] is
{(x1, . . . , xn) ∈ k n | fi (x1, . . . , xn) = 0, i = 1, . . . , n}. We write
this as V (f1, . . . , fm).
▶ The ideal of a subset X ⊆ k n is
{f ∈ k[x1, . . . , xn] | f (x) = 0 for any x ∈ X }. We write this as
I (X ).
This correspondence is almost a bijection!

Magic Squares of Squares using Algebraic Geometry

Consider the magic square:

a b c
d e f
g h i
 

 .

We can write out the equations of a magic square of squares as
follows:
 a2 + b2 + c 2 − d 2 − e2 − f 2 = 0

a2 + b2 + c 2 − g 2 − h2 − i 2 = 0

a2 + b2 + c 2 − b2 − e2 − h2 = 0

a2 + b2 + c 2 − a2 − d 2 − g 2 = 0

a2 + b2 + c 2 − c 2 − f 2 − i 2 = 0

a2 + b2 + c 2 − a2 − e2 − i 2 = 0

a2 + b2 + c 2 − c 2 − e2 − g 2 = 0.

Projective Space

Most of algebraic geometry is carried out in projective space, but
don’t worry! Projective space is a variant on the usual k n which
makes things work nicely.

Deﬁning Projective Space
Projective space is deﬁned as Pn = (k n+1\{0})/ ∼, where
(x1, . . . , xn) ∼ (y1, . . . , yn) if there is a λ ∈ k\{0} such that
λ(x1, . . . , xn) = (y1, . . . , yn) (so when the two points lie on the
same line through the origin). We denote a point in projective
space by (x0 : · · · : xn).

Polynomials and points in projective space
It makes sense to say that (x0 : · · · : xn) is the zero of a
homogeneous polynomial F (X0, . . . , Xn).

Since our equations for a magic square of squares are all
homogeneous, and moreover, a rescaling of a magic square is still a
magic square, it makes sense to work in projective space.

The Magic Square Variety

We deﬁne the magic square variety, which we denote X , to be the
projective variety in P8 given as

X = {(a : b : c : d : e : f : g : h : i) ∈ P
8 | the equations hold
} .

This is a geometric object. Our aim is to understand the geometry
of this object as much as possible to gain insight into whether a
magic square of squares may exist.

▶ What is its dimension?

▶ What are its singular points?

▶ Does it contain lines?

▶ Does it contain curves?

Hilbert Polynomials and Dimension (I)

Intuitively, the dimension of a variety (the zero set of polynomial
equations) is what it looks like close up.

The dimension of a variety can be deﬁned in many diﬀerent ways,
all of which are complicated!

A natural way is using Hilbert Polynomials. There are two versions:
aﬃne and projective. They work in more or less the same way.

Coordinate Ring
Let X ∈ An be an aﬃne variety. We deﬁne the coordinate ring of
X , which we denote k[X ], as the quotient ring k[x1, . . . , xn]/I (X ).
This is also a vector space over k.

Rather than think of k[X ] as a quotient ring, we think of it as
polynomial functions restricted to X . The coordinate ring encodes
almost all the information of X .

Hilbert Polynomials and Dimension (II)

let I ⊆ k[x1, . . . , xn] be an ideal. The (aﬃne) Hilbert function of I ,
denoted by HI , is deﬁned as

HI (s) = dim ( k[x1, . . . , xn]≤s
I≤s
 )

= dim (k[x1, . . . , xn]≤s ) − dim (I≤s ) .

For s large enough, this is a polynomial, known as the (aﬃne)
Hilbert polynomial.

We deﬁne the dimension of an aﬃne variety X ∈ An to be
deg HI (X )(s) for s large enough.

As the monomials form a basis for these vector spaces, this is the
number of monomials of degree ≤ s in the complement of I .

It turns out, that using Gr¨obner bases, it is enough to understand
how to calculate the Hilbert Polynomial of a monomial ideal.

Hilbert Polynomials and Dimension (III)

We want to understand the number of monomials of degree ≤ s in
the complement of I . We can visualise this in k[x, y ].

To ﬁnd the dimension of the magic square variety, we ﬁnd a
Gr¨obner basis for I (X ) and ﬁnd the Hilbert polynomial of
LT (I (X )), which has degree 2, so the magic square variety is a
surface!

Singular Points

Intuitively, a singular point is a ’non-smooth’ point. More formally,
it is a point where the dimension of the tangent space at that
point is not equal to the dimension of the variety.

The singular points of the magic square variety are given by



 ±1 ±
√2 0
0 ±1 ±
√2
±
√2 0 1
 

 ,
 

 0 ±1 ±
√−1
±
√−1 0 ±1
1 ±
√−1 0
 

 ,
 


±√
−1 0 ±1
±
√
2 0 ±
√
−2
±√
−1 0 1
 

 ,

as well as their transposes, and the matrices obtained by reﬂecting
in the central column. All the ± signs are independent from one
another.

There are precisely 256 singular points (note that we work over C
here). Each singular point has precisely three zero entries.

Lines on varieties (I): The Grassmannian

Grassmannians
The Grassmannian is the set of two-dimensional subspaces of k n+1.
We denote it Gr (2, n + 1). Equivalently, it is the set of lines in Pn.

So Gr (2, 4) is the set of lines in P3.

Our aim is to ﬁnd an injective map, ψ, called the Pl¨ucker
embedding: ψ : Gr (2, n + 1) −→ Pm,

for some m.

So, we want to embed Gr (2, n + 1) into projective space. If we can
do this, then any point in the image of ψ will correspond to a
unique line in Pn, and vice-versa.

Lines on varieties (II): The Pl¨ucker embedding

We will try and understand the Pl¨ucker embedding when n = 4 (so
we are looking at lines in P3).

Let W ⊆ k 4 be a two-dimensional subspace. Let

v1 = (u11, u12, u13, u14) and v2 = (u21, u22, u23, u24)

be a basis for W and form the matrix

MW = (
u11 u12 u13 u14
u21 u22 u23 u24
)

We deﬁne
 ψ(W ) = (ω12 : ω13 : ω14 : ω23 : ω24 : ω34),

where ωij is the (i, j)th minor of MW . So ω24 = u12u24 − u14u22,
for example. This map is well deﬁned (independent of the choice
of basis).

Lines on Varieties (III): The Grassmannian (again)

Key Facts
▶ The Pl¨ucker embbedding, ψ is an embedding (i.e. it is
injective).
▶ The image of ψ is a projective variety (i.e. we can ﬁnd
deﬁning equations).

We also call the image of the Pl¨ucker embedding the
Grassmannian.

The image of the Pl¨ucker embedding, ψ(Gr (2, 4)) ∈ P5, is known
as the Pl¨ucker quadric and is deﬁned by the single equation

ω12ω34 − ω13ω24 + ω14ω23 = 0.

So, any point in P5 satisfying this equation corresponds to a
unique line in P3, and any line in P3 corresponds to a unique point
in P5 satisfying this equation. We have parametrised the lines in
P3 using a projective variety in P5.

Lines on Varieties (IV): Open subsets of the Grassmannian

Suppose ω12 ̸= 0. Then the ﬁrst 2 × 2 minor of the corresponding
matrix, MW , is non-zero, so by row reducing MW we can put it
into the following form: (
1 0 a b
0 1 c d
) .

The row space of this matrix still gives us the subspace W ,
because row reducing does not change the rowspace.

So, a general two-dimensional subspace of k 4 corresponding to a
point with ω12 ̸= 0 under the Pl¨ucker embedding, can be
expressed parametrically as

{(λ, µ, λa + µc, λb + µd) | λ, µ ∈ k}.

Lines on Varieties (V): Grassmannians in action!

Consider the variety Ω ∈ P3 deﬁned by the equation

X 3 + Y 3 + Z 3 + W 3 = 0.

This is known as the Fermat cubic. It is a surface and it is smooth
(no singular points). We would like to ﬁnd the lines contained in
this surface (if there are any).

We work on the subset {ω12 ̸= 0} of the Grassmannian. If a line

l = {(λ, µ, λa + µc, λb + µd) | λ, µ ∈ k}

is contained in Ω, then by substituting into the equation for Ω, we
get that

1 + a3 + b3 = 0, 1 + c 3 + d 3 = 0, a2c + b2d = 0, ac 2 + bd 2 = 0.

Lines on Varieties (VI): Grassmannians in action! (Cont.)

From the matrix (
1 0 a b
0 1 c d
) , we see that

a = −ω23, b = −ω24, c = ω13, d = ω14.

So, substituting in for a, b, c, and d, we obtain the four equations

1−ω3
23 −ω3
24 = 0, 1+ω3
13 +ω3
14 = 0, ω2
23ω13 +ω2
24ω14 = 0, −ω23ω2
13 −ω24ω2
14 = 0.

We combine these with the dehomogenised Pl¨ucker quadric (where
ω12 = 1), ω34 − ω13ω24 + ω14ω23 = 0.

Then any point in P5 satisfying these ﬁve equations corresponds to
a unique line in P3 lying on Ω. We ﬁnd that there are 18 such
points by solving the equations.

Lines on Varieties (VII): Grassmannians in action! (Cont.)
One such point is (ξ : 0 : −ξ : 1 : 0 : 1), where ξ = e 2πi
3 . We ﬁnd
that this has corresponding matrix
(
−ξ 0 1 0
0 −1 0 1
) ,

and we read oﬀ the line in P3 given by the two equations
X + ξZ = 0 and Y + W = 0.

We then repeat for the other 17 points.

We then repeat the whole process on each other set {ωij ̸= 0}. We
end up with a total of 27 lines:

X + ξr Z = 0 and Y + ξs W = 0, 0 ≤ r , s ≤ 2
X + ξr W = 0 and Y + ξs Z = 0, 0 ≤ r , s ≤ 2
X + ξr Y = 0 and W + ξs Z = 0, 0 ≤ r , s ≤ 2.

Theorem: Any smooth cubic surface in P3 over an algebraically
closed ﬁeld contains 27 distinct lines.

Lines on Varieties (VII): Magic Squares and Variants

▶ The magic square variety contains no lines.

▶ The magic hourglass variety contains no lines.

a2 b2 c 2

d 2

e2 f 2 g 2

▶ The near magic square of squares variety contains
inﬁnitely many lines (in fact a two-dimensional set of lines).

582 462 1272

942 1132 22

972 822 742

Lines on Varieties (VII): Curves on Varieties

By eliminating variables from sets of equations we can ﬁnd lines on
the corresponding subsets, and then ’lift’ these up to curves on the
original variety.

Carrying out this process on the magic square variety, we ﬁnd a
whole class of degree 8 curves lying on the variety. Unfortunately,
none of these curves go through any rational points. This is
perhaps further evidence on the non-existence of solutions to our
original problem.

One such curve is given by the following equations:

c = a + b, g = α(a − b), h = α(2a + b), i = α(a + 2b),
1
3 (2a2 − 4ab − b2) − f 2 = 0, 2
3 (a2 + ab + b2) − e2 = 0,

2
3 (a2 + 4ab + b2) − d 2 = 0,

where α = 1√−3 .

The Fourth-Year Project (I): Timeline

Disclaimer: The process may diﬀer in future years. Moreover, any
of the advice I give is personal and should be taken as such.

▶ Two options: Research Project and Maths In Action.

- Term 3 Year 3: Speak to potential supervisors, agree
roughly on a project.

- Term 1 Year 4: Meetings with supervisor, mainly
background reading. Write up some pages of project.

- Christmas holidays: Write up project and progress report.

- Term 2 Year 4: Less background reading, more research.
Continue meetings with supervisor.

- Easter Holidays: Submit project, usually third week of
holidays.

- Term 3 Year 4: Presentation.

The Fourth-Year Project (II): Some advice

▶ Speak to members of staﬀ early!

▶ Try and ﬁnd a good project-module balance.

▶ Writing up takes a long time.

▶ Don’t be afraid of research!

Thank you for listening! :)

Contact: p.rodgers@warwick.ac.uk or via Facebook.
