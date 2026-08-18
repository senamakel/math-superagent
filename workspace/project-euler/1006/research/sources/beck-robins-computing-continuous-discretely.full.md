<!-- source: https://matthbeck.github.io/papers/ccdnew.pdf | converted from PDF -->

Matthias Beck & Sinai Robins

Computing the Continuous
Discretely

Integer-Point Enumeration in Polyhedra

With illustrations by David Austin
February 18, 2023

Springer

To Tendai To my mom, Michal Robins

with all our love

Preface

The world is continuous, but the mind is discrete.

David Mumford

The mathematical interplay between polytopes and lattices comes to life when
we study the relationships between the continuous volume of a polytope and
its discrete volume. Since the humbling and positive reception of the ﬁrst
edition of this book, published in 2007, the ﬁeld of integer-point enumeration
in polyhedra has gained considerable momentum. Many ﬁelds of mathematics
have begun to interact in even more surprising ways, and a beautifully simple
uniﬁcation among a multitude of classical problems continues to emerge when
we use this combinatorial-geometric lens.
In this second edition, and with encouragement from many wonderful
readers, we have added two new chapters: Chapter 9 introduces zonotopes,
an extremely useful class of polytopes, and Chapter 10 explores some deep
yet elegant relationships that are satisﬁed by the h-polynomials and h
∗-
polynomials. We have also added many new exercises, new and updated open
problems, and graphics.
Examples of polytopes in three dimensions include crystals, boxes, tetra-
hedra, and any convex object whose faces are all ﬂat. It is amusing to see
how many problems in combinatorics, number theory, and many other mathe-
matical areas can be recast in the language of polytopes that exist in some
Euclidean space. Conversely, the versatile structure of polytopes gives us
number-theoretic and combinatorial information that ﬂows naturally from
their geometry.
The discrete volume of a body P can be described intuitively as the number
of grid points that lie inside P, given a ﬁxed grid in Euclidean space. The
continuous volume of P has the usual intuitive meaning of volume that we
attach to everyday objects we see in the real world.
 3

4 Preface

Fig. 0.1 Continuous and discrete volume.

Indeed, the diﬀerence between the two realizations of volume can be
thought of in physical terms as follows. On the one hand, the quantum-level
grid imposed by the molecular structure of reality gives us a discrete notion of
space and hence discrete volume. On the other hand, the Newtonian notion of
continuous space gives us the continuous volume. We see things continuously at
the Newtonian level, but in practice, we often compute things discretely at the
quantum level. Mathematically, the grid we impose in space—corresponding
to the grid formed by the atoms that make up an object—helps us compute
the usual continuous volume in very surprising and charming ways, as we
shall discover.
In order to see the continuous/discrete interplay come to life among the
three ﬁelds of combinatorics, number theory, and geometry, we begin our focus
with the simple-to-state coin-exchange problem of Frobenius. The beauty
of this concrete problem is that it is easy to grasp, it provides a useful
computational tool, and yet it has most of the ingredients of the deeper
theories that are developed here.
In the ﬁrst chapter, we give detailed formulas that arise naturally from the
Frobenius coin-exchange problem in order to demonstrate the interconnections
between the three ﬁelds mentioned above. The coin-exchange problem provides
a scaﬀold for identifying the connections between these ﬁelds. In the ensuing
chapters, we shed this scaﬀolding and focus on the interconnections themselves:

(1) Enumeration of integer points in polyhedra—combinatorics,
(2) Dedekind sums and ﬁnite Fourier series—number theory,
(3) Polygons and polytopes—geometry.

We place a strong emphasis on computational techniques and on computing
volumes by counting integer points using various old and new ideas. Thus,
the formulas we get should not only be pretty (which they are!) but also allow
us to compute volumes eﬃciently using some nice functions. In the very rare
instances of mathematical exposition when we have a formulation that is both
“easy to write” and “quickly computable,” we have found a mathematical
nugget. We have endeavored to ﬁll this book with such mathematical nuggets.
Much of the material in this book is developed by the reader in the more
than three hundred exercises. Most chapters contain warmup exercises that

Preface 5

do not depend on the material in the chapter and can be assigned before the
chapter is read. Some exercises are central, in the sense that current or later
material depends on them. Those exercises are marked with ♣, and we give
detailed hints for them at the end of the book. Most chapters also contain
lists of open research problems.
It turns out that even a ﬁfth grader can write an interesting paper on integer-
point enumeration [193], while the subject lends itself to deep investigations
that attract the current eﬀorts of leading researchers. Thus, it is an area of
mathematics that attracts our innocent childhood questions as well as our
reﬁned insight and deeper curiosity. The level of study is highly appropriate
for a junior/senior undergraduate course in mathematics. In fact, this book
is ideally suited to be used for a capstone course. Because the three topics
outlined above lend themselves to more sophisticated exploration, our book
has also been used eﬀectively for an introductory graduate course.
To help the reader fully appreciate the scope of the connections between
continuous volume and discrete volume, we begin the discourse in two dimen-
sions, where we can easily draw pictures and quickly experiment. We gently
introduce the functions we need in higher dimensions (Dedekind sums) by
looking at the coin-exchange problem geometrically as the discrete volume of
a generalized triangle, called a simplex.
The initial techniques are quite simple, essentially nothing more than
expanding rational functions into partial fractions. Thus, the book is easily
accessible to a student who has completed a standard college calculus and
linear algebra curriculum. It would be useful to have a basic understanding of
partial fraction expansions, inﬁnite series, open and closed sets in Rd, complex
numbers (in particular, roots of unity), and modular arithmetic.
An important computational tool that is harnessed throughout the text
is the generating function f (x) = ∑∞
m=0 a(m) x
m, where the a(m)’s form a
sequence of numbers that we are interested in analyzing. When the inﬁnite
sequence of numbers a(m), m = 0, 1, 2, . . . , is embedded into a single generat-
ing function f (x), it is often true that for hitherto unforeseen reasons, we can
rewrite the whole sum f (x) in a surprisingly compact form. It is the rewriting
of these generating functions that allows us to understand the combinatorics
of the relevant sequence a(m). For us, the sequence of numbers might be the
number of ways to partition an integer into given coin denominations, or the
number of points in an increasingly large body, and so on. Here we ﬁnd yet
another example of the interplay between the discrete and the continuous: we
are given a discrete set of numbers a(m), and we then carry out analysis on
the generating function f (x) in the continuous variable x.

What Is the Discrete Volume?

The physically intuitive description of the discrete volume given above rests
on a sound mathematical footing as soon as we introduce the notion of a

6 Preface

lattice. The grid is captured mathematically as the collection of all integer
points in Euclidean space, namely Z
d = {(x1, . . . , xd) : all xk ∈ Z}. This
discrete collection of equally spaced points is called a lattice. If we are given a
geometric body P ⊂ Rd, its discrete volume is simply deﬁned as the number
of lattice points inside P, that is, the number of elements in the set Z
d ∩ P.
Intuitively, if we shrink the lattice by a factor k and count the number
of newly shrunken lattice points inside P, we obtain a better approximation
for the volume of P, relative to the volume of a single cell of the shrunken
lattice. It turns out that after the lattice is shrunk by an integer factor k, the
number # (P ∩ 1
k Z
d) of shrunken lattice points inside an integral polytope P
is magically a polynomial in k. This counting function # (P ∩ 1
k Z
d) is known
as the Ehrhart polynomial of P. If we kept shrinking the lattice by taking a
limit, we would of course end up with the continuous volume that is given by
the usual Riemannian integral deﬁnition of calculus:

vol P = lim
k→∞ # (P ∩ 1
k Z
d) 1
kd .

However, pausing at ﬁxed dilations of the lattice gives surprising ﬂexibility
for the computation of the volume of P and for the number of lattice points
that are contained in P.
Thus, when the body P is an integral polytope, the error terms that measure
the discrepancy between the discrete volume and the usual continuous volume
are quite nice; they are given by Ehrhart polynomials, and these enumeration
polynomials are the content of Chapter 3.

The Fourier–Dedekind Sums Are the Building Blocks: Number
Theory

Every polytope has a discrete volume that is expressible in terms of certain
ﬁnite sums that are known as Dedekind sums. Before giving their deﬁnition,
we ﬁrst motivate these sums with some examples that illustrate their building-
block behavior for lattice-point enumeration. To be concrete, consider, for
example, a 1-dimensional polytope given by an interval P = [0, a], where a is
any positive real number. It is clear that we need the greatest integer function
⌊x⌋ to help us enumerate the lattice points in P, and indeed, the answer is
⌊a⌋ + 1.
Next, consider a 1-dimensional line segment that is sitting in the 2-
dimensional plane. Let’s choose our segment P so that it begins at the origin
and ends at the lattice point (c, d). As becomes apparent after a moment’s
thought, the number of lattice points on this ﬁnite line segment involves an
old friend, namely the greatest common divisor of c and d. The exact number
of lattice points on the line segment is gcd(c, d) + 1.

Preface 7

To unify both of these examples, consider a triangle P in the plane whose
vertices have rational coordinates. It turns out that a certain ﬁnite sum is
completely natural because it simultaneously extends both the greatest integer
function and the greatest common divisor, although the latter is less obvious.
An example of a Dedekind sum in two dimensions that arises naturally in the
formula for the discrete volume of the rational triangle P is the following:

s(a, b) =
 b−1∑

m=1
 ( m
b − 1
2
 ) ( ma
b − ⌊ ma
b
 ⌋ − 1
2
 ) .

The deﬁnition makes use of the greatest integer function. Why do these
sums also resemble the greatest common divisor? Luckily, the Dedekind sums
satisfy a remarkable reciprocity law, quite similar to the Euclidean algorithm
that computes the greatest common divisor. This reciprocity law allows the
Dedekind sums to be computed in roughly log(b) steps rather than the b steps
that are implied by the deﬁnition above. The reciprocity law for s(a, b) lies
at the heart of some amazing number theory that we treat in an elementary
fashion, but that also comes from the deeper subject of modular forms and
other modern tools.
We ﬁnd ourselves in the fortunate position of viewing an important summit
of an enormous mountain of ideas, submerged by the waters of geometry. As
we delve more deeply into these waters, more and more hidden beauty unfolds
for us, and the Dedekind sums are an indispensable tool that allow us to see
farther as the waters get deeper.

The Relevant Solids Are Polytopes: Geometry

The examples we have used, namely line segments and polygons in the plane,
are special cases of polytopes in all dimensions. One way to deﬁne a polytope
is to consider the convex hull of a ﬁnite collection of points in Euclidean
space Rd. That is, suppose someone gives us a set of points v1, . . . , vn in
Rd. The polytope determined by the given points vj is deﬁned by all linear
combinations c1v1 +c2v2 +· · ·+cnvn, where the coeﬃcients cj are nonnegative
real numbers that satisfy the relation c1 + c2 + · · · + cn = 1. This construction
is called the vertex description of the polytope.
There is another equivalent deﬁnition, called the hyperplane description
of the polytope. Namely, if someone hands us the linear inequalities that
deﬁne a ﬁnite collection of half-spaces in Rd, we can deﬁne the associated
polytope as the simultaneous intersection of the half-spaces deﬁned by the
given inequalities.
There are some “obvious” facts about polytopes that are intuitively clear
to most students but are, in fact, subtle and often nontrivial to prove from
ﬁrst principles. One of these facts, namely that every polytope has both a
vertex and a hyperplane description, forms a crucial basis to the material we

8 Preface

will develop in this book. We carefully prove this fact in the appendix. The
statement is intuitively clear, so that novices can skip over its proof without
any detriment to their ability to compute continuous and discrete volumes
of polytopes. All theorems in the text (including those in the appendix) are
proved from ﬁrst principles, with the exception of Chapter 14, where we
assume basic notions from complex analysis.

Chapter 1
The Coin-Exchange
Problem of Frobenius

@@R

?
 Chapter 2
A Gallery of Discrete Volumes

  

Chapter 3
Counting Lattice Points in
Polytopes: The Ehrhart Theory XXXz
 Chapter 9
Zonotopes?
Chapter 7
Finite Fourier Analysis



 Chapter 4
Reciprocity

?

˘˘˘˘˘9 XXXXz
Chapter 8
Dedekind Sums Chapter 6
Magic Squares

Chapter 5
Face Numbers and the
Dehn–Sommerville Relations
 HH
Hj

Chapter 10
h- and h∗-polynomials?
Chapter 14
A Discrete Version
of Green’s Theorem Chapter 11
The Decomposition of a
Polytope into Its Cones

 
 	 @@R
Chapter 12
Euler–MacLaurin
Summation in Rd
 Chapter 13
Solid Angles

Fig. 0.2 The partially ordered set of chapter dependencies

The text naturally ﬂows into two parts, which we now explicate.

Preface 9

Part I

We have taken great care in making the content of the chapters ﬂow seamlessly
from one to the next, over the span of the ﬁrst six chapters.

• Chapters 1 and 2 introduce some basic notions of generating functions, in
the visually compelling context of discrete geometry, with an abundance of
detailed motivating examples.
• Chapters 3, 4, and 5 develop the full Ehrhart theory of discrete volumes of
rational polytopes.
• Chapter 6 is a “dessert” chapter, in that it enables us to use the theory
developed to treat the enumeration of magic squares, an ancient topic that
enjoys active current research.

Part II

We now begin anew.

• Having attained experience with numerous examples and results about
integral polytopes, we are ready to learn about the Dedekind sums of Chap-
ter 8, which form the atomic pieces of the discrete-volume polynomials. On
the other hand, to fully understand Dedekind sums, we need to understand
ﬁnite Fourier analysis, which we therefore develop from ﬁrst principles in
Chapter 7, using only partial fractions.
• In Chapter 9, we study a concrete class of polytopes—projections of cubes,
which go by the name zonotopes—whose discrete volume is tractable and
has neat connections to number theory and graph theory.
• Chapter 10 develops inequalities among the coeﬃcients of an Ehrhart poly-
nomial, based on a polynomial decomposition formula that arises naturally
from the arithmetic and combinatorial data of triangulations.
• Chapter 11 answers a simple yet tricky question: how does a ﬁnite geometric
series in one dimension extend to higher-dimensional polytopes? Brion’s
theorem gives an elegant and decisive answer to this question.
• In Chapter 12, we extend the interplay between the continuous volume and
the discrete volume of a polytope (already studied in detail in Part I) by
introducing Euler–Maclaurin summation formulas in all dimensions. These
formulas compare the continuous Fourier transform of a polytope to its
discrete Fourier transform, yet the material is completely self-contained.
• Chapter 13 develops an exciting extension of Ehrhart theory that deﬁnes
and studies the solid angles of a polytope; these are the natural extensions
of 2-dimensional angles to higher dimensions.
• Finally, we end with another “dessert” chapter that uses complex-analytic
methods to ﬁnd an integral formula for the discrepancy between the discrete
and continuous areas enclosed by a closed curve in the plane.

10 Preface

Because polytopes are both theoretically useful (in triangulated manifolds,
for example) and practically essential (in computer graphics, for example) we
use them to link results in number theory and combinatorics. Many research
papers have been written on these interconnections, and it is impossible to
capture them all here, especially since some are being written even as we are
writing this sentence! However, we hope that these modest beginnings will
give the reader who is unfamiliar with these ﬁelds a good sense of their beauty,
inexorable connectedness, and utility. We have written a gentle invitation to
what we consider a gorgeous world of counting and of links between the ﬁelds
of combinatorics, number theory, and geometry for the general mathematical
reader.
There are a number of excellent books that have a nontrivial intersection
with ours and contain material that complements the topics discussed here.
We heartily recommend the monographs of Barvinok [21, 22] (on general
convexity topics and Ehrhart theory), Bruns–Gubeladze [74] (on commutative
algebra and K-theory connected with polytopes), De Loera–Hemmecke–K¨oppe
[96] (on connections to optimization), De Loera–Rambau–Santos [99] (on
triangulations of point conﬁgurations), Ehrhart [112] (the historic introduction
to Ehrhart theory), Ewald [113] (on connections to algebraic geometry),
Hibi [135] (on the interplay of algebraic combinatorics with polytopes), Miller–
Sturmfels [178] (on combinatorial commutative algebra), and Stanley [231]
(on general enumerative problems in combinatorics).

Acknowledgments

We have had the good fortune of receiving help from many gracious people in
the process of writing this book. First and foremost, we thank the students of
the classes in which we could try out this material, at Binghamton University
(SUNY), Nanyang Technological University, San Francisco State University,
and Temple University. We are indebted to our MSRI/Banﬀ 2005 graduate
summer school students. We give special thanks to Kristin Camenga and
Kevin Woods, who ran the problem sessions for this summer school, detected
numerous typos, and provided us with many interesting suggestions for this
book. We are grateful for the generous support for the summer school from the
Mathematical Sciences Research Institute, the Paciﬁc Institute of Mathematics,
and the Banﬀ International Research Station.
Many colleagues have supported this endeavor, and we are particularly
grateful to everyone notifying us of mistakes and typos and to those who have
made useful suggestions: Daniel Antonetti, Alexander Barvinok, Nathanael
Berglund, Andrew Beyer, Tristram Bogart, Garry Bowlin, Benjamin Braun,
Swee Hong Chan, Robin Chapman, Yitwah Cheung, Jessica Cuomo, Dimitros
Dais, Jesus De Loera, David Desario, Mike Develin, Ricardo Diaz, Michael
Dobbins, Jeﬀ Doker, Han Minh Duong, Richard Ehrenborg, David Einstein,
Joseph Gubeladze, Christian Haase, Mary Halloran, Friedrich Hirzebruch,

Preface 11

Brian Hopkins, Serkan Ho¸sten, Benjamin Howard, Piotr Maciak, Evgeny
Materov (Chapter 5 rocks!), Asia Matthews, Peter McMullen, Mart´ın Mereb,
Ezra Miller, Mel Nathanson, Julian Pfeiﬂe, Peter Pleasants, Jorge Ram´ırez
Alfons´ın, Bruce Reznick, Adrian Riskin, Junro Sato, Melissa Simmons, Richard
Stanley, Bernd Sturmfels, Thorsten Theobald, Read Vanderbilt, Andrew Van
Herick, Sven Verdoolaege, Mich`ele Vergne, Julie Von Bergen, Neil Weickel,
Carl Woll, Zhiqiang Xu, Jon Yaggie, Ruriko Yoshida, Thomas Zaslavsky,
G¨unter Ziegler, and two anonymous referees.
We are indebted to the Springer editorial staﬀ, ﬁrst and foremost to Mark
Spencer, for facilitating the publication process in an always friendly and sup-
portive spirit. We thank David Kramer for the impeccable copyediting, Frank
Ganz for sharing his LATEX expertise, and Felix Portnoy for the seamless pro-
duction process. The Springer editors in Germany and Japan kindly suggested
translations of our book, and we are particularly grateful to Kord Eickmeyer
and Yoshio Okamoto for taking on the monumental task of translating this
work.
Many colleagues have sent us suggestions and updates for this second
edition; in addition to the ones listed above, we thank Ana Berrizbeitia,
Steven Collazos, Aaron Dall, Maryam Farahmand, Katharina Jochemko,
Michael Joswig, Victor Katsnelson, Jim Lawrence, Nhat Le Quang, Matthias
Lenz, Pieter Moree, Bruce Sagan, Steven Sam, Raman Sanyal, Kim Seashore,
and Ed Swartz. Special thanks go to Philippe Clauss for permission to include
Eug`ene Ehrhart’s self-portrait.
Perhaps the most visible change can be seen in the ﬁgures, whose new and
much-improved looks owe their beauty to David Austin. We are huge fans of
his work and thank him for his time and energy on this project.
We thank Eugene Ha for facilitating the publication process of this second
edition. We will collect further corrections, updates, etc., at the Internet
website math.sfsu.edu/beck/ccd.html.
Matthias Beck’s work has been partially supported by the United States
National Science Foundation (DMS-0810105 & DMS-1162638). Sinai Robins’s
work has been partially supported by the Singapore Ministry of Education
(Tier 2 Research Grant MOE2011-T2-1-090), by the Institute for Constructive
and Experimental Mathematics (ICERM), and by Brown University.
Matthias Beck would like to express his deepest gratitude to Tendai
Chitewere for her patience, support, and unconditional love. He thanks his
family for always being there for him. Sinai Robins would like to thank his
mother, Michal Robins, and his brothers, Shani Robins and Gabriel Robins,
for their relentless support and understanding during the completion of this
project. We both thank all the caf´es we have inhabited over the past 14 years
for enabling us to turn their coﬀee into theorems.

San Francisco, CA Matthias Beck
Providence, RI Sinai Robins
September 2015

Contents

Part I The Essentials of Discrete Volume Computations

1 The Coin-Exchange Problem of Frobenius . . . . . . . . . . . . . . . . 3
1.1 Why Use Generating Functions? . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Two Coins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.3 Partial Fractions and a Surprising Formula . . . . . . . . . . . . . . . . 8
1.4 Sylvester’s Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.5 Three and More Coins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

2 A Gallery of Discrete Volumes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.1 The Language of Polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.2 The Unit Cube . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
2.3 The Standard Simplex . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
2.4 The Bernoulli Polynomials as Lattice-Point Enumerators of
Pyramids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
2.5 The Lattice-Point Enumerators of the Cross-Polytopes . . . . . . 38
2.6 Pick’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
2.7 Polygons with Rational Vertices . . . . . . . . . . . . . . . . . . . . . . . . . . 43
2.8 Euler’s Generating Function for General Rational Polytopes . 48
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

3 Counting Lattice Points in Polytopes: The Ehrhart Theory 59
3.1 Triangulations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
3.2 Cones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
3.3 Integer-Point Transforms for Rational Cones . . . . . . . . . . . . . . . 64
3.4 Expanding and Counting Using Ehrhart’s Original Approach . 68

13

14 Contents

3.5 The Ehrhart Series of an Integral Polytope . . . . . . . . . . . . . . . . 71
3.6 From the Discrete to the Continuous Volume of a Polytope . . 76
3.7 Interpolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
3.8 Rational Polytopes and Ehrhart Quasipolynomials . . . . . . . . . . 80
3.9 Reﬂections on the Coin-Exchange Problem and the Gallery of
Chapter 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

4 Reciprocity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
4.1 Generating Functions for Somewhat Irrational Cones . . . . . . . . 90
4.2 Stanley’s Reciprocity Theorem for Rational Cones . . . . . . . . . . 92
4.3 Ehrhart–Macdonald Reciprocity for Rational Polytopes . . . . . 93
4.4 The Ehrhart Series of Reﬂexive Polytopes . . . . . . . . . . . . . . . . . 94
4.5 More “Reﬂections” on Chapters 1 and 2 . . . . . . . . . . . . . . . . . . . 96
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100

5 Face Numbers and the Dehn–Sommerville Relations in
Ehrhartian Terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
5.1 Face It! . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
5.2 Dehn–Sommerville Extended . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
5.3 Applications to the Coeﬃcients of an Ehrhart Polynomial . . . 105
5.4 Relative Volume . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109

6 Magic Squares . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
6.1 It’s a Kind of Magic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
6.2 Semimagic Squares: Points in the Birkhoﬀ–von Neumann
Polytope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
6.3 Magic Generating Functions and Constant-Term Identities . . . 119
6.4 The Enumeration of Magic Squares . . . . . . . . . . . . . . . . . . . . . . . 124
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128

Contents 15

Part II Beyond the Basics

7 Finite Fourier Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
7.1 A Motivating Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
7.2 Finite Fourier Series for Periodic Functions on Z . . . . . . . . . . . 135
7.3 The Finite Fourier Transform and Its Properties . . . . . . . . . . . . 139
7.4 The Parseval Identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
7.5 The Convolution of Finite Fourier Series . . . . . . . . . . . . . . . . . . . 143
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146

8 Dedekind Sums . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
8.1 Fourier–Dedekind Sums and the Coin-Exchange Problem
Revisited . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
8.2 The Dedekind Sum and Its Reciprocity and Computational
Complexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
8.3 Rademacher Reciprocity for the Fourier–Dedekind Sum . . . . . 154
8.4 The Mordell–Pommersheim Tetrahedron . . . . . . . . . . . . . . . . . . 158
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164

9 Zonotopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
9.1 Deﬁnitions and Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
9.2 Paving a Zonotope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
9.3 The Permutahedron . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
9.4 The Ehrhart Polynomial of a Zonotope . . . . . . . . . . . . . . . . . . . . 176
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181

10 h-Polynomials and h
∗-Polynomials . . . . . . . . . . . . . . . . . . . . . . . . 183
10.1 Simplicial Polytopes and (Unimodular) Triangulations . . . . . . 183
10.2 Fundamental Parallelepipeds Open Up, with an h-Twist . . . . . 187
10.3 Palindromic Decompositions of h
∗-Polynomials . . . . . . . . . . . . . 189
10.4 Inequalities for h
∗-Polynomials . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197

11 The Decomposition of a Polytope into Its Cones . . . . . . . . . . 199
11.1 The Identity “∑

m∈Z zm = 0” . . . or “Much Ado About
Nothing” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
11.2 Technically Speaking. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
11.3 Tangent Cones and Their Rational Generating Functions . . . . 204
11.4 Brion’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205

16 Contents

11.5 Brion Implies Ehrhart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210

12 Euler–Maclaurin Summation in Rd . . . . . . . . . . . . . . . . . . . . . . . . 213
12.1 Todd Operators and Bernoulli Numbers . . . . . . . . . . . . . . . . . . . 214
12.2 A Continuous Version of Brion’s Theorem . . . . . . . . . . . . . . . . . 216
12.3 Polytopes Have Their Moments . . . . . . . . . . . . . . . . . . . . . . . . . . 218
12.4 Computing the Discrete Continuously . . . . . . . . . . . . . . . . . . . . . 221
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225

13 Solid Angles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
13.1 A New Discrete Volume Using Solid Angles . . . . . . . . . . . . . . . . 227
13.2 Solid-Angle Generating Functions and a Brion-Type Theorem 231
13.3 Solid-Angle Reciprocity and the Brianchon–Gram Relations . . 232
13.4 The Generating Function of Macdonald’s Solid-Angle
Polynomials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238
Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239

14 A Discrete Version of Green’s Theorem Using Elliptic
Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
14.1 The Residue Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
14.2 The Weierstraß ℘- and ζ-Functions . . . . . . . . . . . . . . . . . . . . . . . 243
14.3 A Contour-Integral Extension of Pick’s Theorem . . . . . . . . . . . 245
Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248

Appendix: Vertex and Hyperplane Descriptions of Polytopes . 249
A.1 Every h-Cone Is a v-Cone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
A.2 Every v-Cone Is an h-Cone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252

Hints for ♣ Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255

References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267

List of Symbols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279

Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281

Part I
The Essentials of Discrete Volume
Computations

Chapter 1
The Coin-Exchange Problem of
Frobenius

The full beauty of the subject of generating functions emerges only from tuning in on both
channels: the discrete and the continuous.

Herbert Wilf [253]

Suppose we are interested in an inﬁnite sequence of numbers (ak)
∞
k=0 that
arises geometrically or recursively. Is there a “good formula” for ak as a
function of k? Are there identities involving various ak’s? Embedding this
sequence into the generating function

F (z) = ∑

k≥0 ak zk

allows us to retrieve answers to the questions above in a surprisingly quick
and elegant way. We can think of F (z) as lifting our sequence ak from its
discrete setting into the continuous world of functions.

1.1 Why Use Generating Functions?

To illustrate these concepts, we warm up with the classic example of the
Fibonacci sequence fk, named after Leonardo Pisano Fibonacci (c. 1170–
c. 1250)1 and deﬁned by the recurrence relation

f0 = 0, f1 = 1, and fk+2 = fk+1 + fk for k ≥ 0 .

This gives the sequence (fk)∞
k=0 = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, . . . ) (see also [1,
Sequence A000045]). Now let’s see what generating functions can do for us.

1 For more information about Fibonacci, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Fibonacci.html.
 3

4 1 The Coin-Exchange Problem of Frobenius

Let F (z) := ∑

k≥0 fk zk.

We embed both sides of the recurrence identity into their generating functions:
∑

k≥0 fk+2 zk = ∑

k≥0 (fk+1 + fk) zk = ∑

k≥0 fk+1 zk + ∑

k≥0 fk zk. (1.1)

The left–hand side of (1.1) is

∑

k≥0 fk+2 zk = 1
z2 ∑

k≥0 fk+2 zk+2 = 1
z2 ∑

k≥2 fk zk = 1
z2 (F (z) − z) ,

while the right–hand side of (1.1) is

∑

k≥0 fk+1 zk + ∑

k≥0 fk zk = 1
z F (z) + F (z) .

So (1.1) can be restated as

1
z2 (F (z) − z) = 1
z F (z) + F (z) ,

or F (z) = z
1 − z − z2 .

It is fun to check (e.g., with a computer) that when we expand the function
F into a power series, we indeed obtain the Fibonacci numbers as coeﬃcients:

z
1 − z − z2 = z + z2 + 2 z3 + 3 z4 + 5 z5 + 8 z6 + 13 z7 + 21 z8 + 34 z9 + · · · .

Now we use our favorite method of handling rational functions: the partial
fraction expansion. In our case, the denominator factors as 1 − z − z2 =(1 − 1+
√5
2 z) (
1 − 1−√5
2 z), and the partial fraction expansion is (see Exer-

cise 1.1)
 F (z) = z
1 − z − z2 = 1/
√5

1 − 1+
√5
2 z − 1/
√5

1 − 1−
√5
2 z . (1.2)

The two terms suggest the use of the geometric series

∑

k≥0 xk = 1
1 − x (1.3)

(see Exercise 1.2) with x = 1+
√5
2 z and x = 1−
√5
2 z, respectively:

1.2 Two Coins 5

F (z) = z
1 − z − z2 = 1
√5
 ∑

k≥0
 ( 1 + √5
2 z
)k
 − 1
√5
 ∑

k≥0
 ( 1 − √5
2 z
)k

= ∑

k≥0
 1
√5
 


( 1 + √5
2
 )k
 −
 ( 1 − √5
2
 )k

 zk.

Comparing the coeﬃcients of zk in the deﬁnition of F (z) = ∑
k≥0 fk zk and
the new expression above for F (z), we discover the closed-form expression

fk = 1
√5
 ( 1 + √5
2
 )k
 − 1
√5
 ( 1 − √5
2
 )k

for the Fibonacci sequence.
This method of decomposing a rational generating function into partial
fractions is one of our key tools. Because we will use partial fractions time
and again throughout this book, we record the result on which this method is
based.

Theorem 1.1 (Partial fraction expansion). Given a rational function

F (z) := p(z)
∏m
k=1 (z − ak)
ek ,

where p is a polynomial of degree less than e1 + e2 + · · · + em and the ak are
distinct complex numbers, there exists a decomposition

F (z) =
 m∑

k=1
 ( ck,1
z − ak + ck,2
(z − ak)2 + · · · + ck,ek
(z − ak)ek
 )
 ,

where ck,j ∈ C are unique.

One possible proof of this theorem is based on the fact that the polynomials
form a Euclidean domain. For readers who are acquainted with this notion,
we outline this proof in Exercise 1.37.

1.2 Two Coins

Let’s imagine that we introduce a new coin system. Instead of using pennies,
nickels, dimes, and quarters, let’s say that we agree on using 4-cent, 7-cent,
9-cent, and 34-cent coins. The reader might point out the following ﬂaw of this
new system: certain amounts cannot be obtained (that is, created with the
available coins), for example, 2 or 5 cents. On the other hand, this deﬁciency
makes our new coin system more interesting than the old one, because we

6 1 The Coin-Exchange Problem of Frobenius

can ask the question, “which amounts can be obtained?” In fact, we will
prove in Exercise 1.20 that there are only ﬁnitely many integer amounts
that cannot be obtained using our new coin system. A natural question,
ﬁrst tackled by Ferdinand Georg Frobenius (1849–1917),
2 and James Joseph
Sylvester (1814–1897)
3 is, what is the largest amount that cannot be changed?
As mathematicians, we like to keep questions as general as possible, and so
we ask, given coins of denominations a1, a2, . . . , ad that are positive integers
without any common factor, can you give a formula for the largest amount
that cannot be obtained using the coins a1, a2, . . . , ad? This problem is known
as the Frobenius coin-exchange problem.
To be precise, suppose we are given a set of positive integers

A = {a1, a2, . . . , ad}

with gcd (a1, a2, . . . , ad) = 1. We call a positive integer n representable by
the set A if there exist nonnegative integers m1, m2, . . . , md such that

n = m1a1 + · · · + mdad .

In the language of coins, this means that we can obtain the amount n
using the coins a1, a2, . . . , ad. The Frobenius problem (often called the linear
Diophantine problem of Frobenius) asks us to ﬁnd the largest integer that is
not representable. We call this largest integer the Frobenius number and
denote it by g(a1, . . . , ad). The following theorem gives us a pretty formula
for d = 2.

Theorem 1.2. If a1 and a2 are relatively prime positive integers, then

g (a1, a2) = a1a2 − a1 − a2 .

This simple-looking formula for g inspired a great deal of research into
formulas for g (a1, a2, . . . , ad) with only limited success; see the notes at the
end of this chapter. For d = 2, Sylvester gave the following result.

Theorem 1.3 (Sylvester’s theorem). Let a1 and a2 be relatively prime
positive integers. Exactly half of the integers between 1 and (a1 − 1) (a2 − 1)
are representable by {a1, a2}.

Our goal in this chapter is to prove these two theorems (and a little more)
using the machinery of partial fractions. We approach the Frobenius problem
through the study of the restricted partition function

pA(n) := # {(m1, . . . , md) ∈ Z
d : all mj ≥ 0, m1a1 + · · · + mdad = n} ,

2 For more information about Frobenius, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Frobenius.html.
3 For more information about Sylvester, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Sylvester.html.

1.2 Two Coins 7

the number of partitions of n using only the elements of A as parts.
4 In view
of this partition function, g(a1, . . . , ad) is the largest positive integer n for
which pA(n) = 0.
There is a beautiful geometric interpretation of the restricted partition
function. The geometric description begins with the set

P = {(x1, . . . , xd) ∈ Rd : all xj ≥ 0, x1a1 + · · · + xdad = 1
} . (1.4)

The nth dilate of a set S ⊆ Rd is

{(nx1, nx2, . . . , nxd) : (x1, . . . , xd) ∈ S} .

The function pA(n) counts precisely those integer points in Z
d that lie in the
nth integer dilate of the body P. The set Z
d is an example of a lattice,5 and
so integer points are often called lattice points. The dilation process in this
context is tantamount to replacing x1a1 + · · · + xdad = 1 in the deﬁnition of
P by x1a1 + · · · + xdad = n. The set P turns out to be a polytope. We can
easily picture P and its dilates for dimension d ≤ 3; Figure 1.1 shows the
3-dimensional case.

Fig. 1.1 The polytope P
for d = 3.

n
a
1
a

n
b

1
b

n
c
 1
c
 x

y

z
 4 A partition of a positive integer n is a multiset (i.e., a set in which we allow repetition)
{n1, n2, . . . , nk} of positive integers such that n = n1 + n2 + · · · + nk. The numbers
n1, n2, . . . , nk are called the parts of the partition.

5 A lattice is a discrete subgroup of Rd, where d is a positive integer.

8 1 The Coin-Exchange Problem of Frobenius

1.3 Partial Fractions and a Surprising Formula

We ﬁrst concentrate on the case d = 2 and study

p{a,b}(n) = # {(k, l) ∈ Z
2 : k, l ≥ 0, ak + bl = n} .

Recall that we require a and b to be relatively prime. To begin our discussion,
we play around with generating functions. Consider the following product of
two geometric series:
( 1
1 − za
 ) ( 1
1 − zb
 ) = (1 + za + z2a + · · ·) (
1 + zb + z2b + · · ·)

(see Exercise 1.2). If we multiply out all the terms, we obtain a power series all
of whose exponents are linear combinations of a and b. In fact, the coeﬃcient
of zn in this power series counts the number of ways that n can be written as
a nonnegative linear combination of a and b. In other words, these coeﬃcients
are precisely evaluations of our counting function p{a,b}:
( 1
1 − za
 ) ( 1
1 − zb
 ) = ∑

k≥0
 ∑

l≥0 zakzbl = ∑

n≥0 p{a,b}(n) zn.

So this function is the generating function for the sequence of integers(p{a,b}(n)
)∞
n=0. The idea is now to study the compact function on the left.
We would like to uncover an interesting formula for p{a,b}(n) by looking at
the generating function on the left more closely. To make our computational
life easier, we study the constant term of a related series; namely, p{a,b}(n) is
the constant term of

f (z) := 1
(1 − za) (1 − zb) zn = ∑

k≥0 p{a,b}(k) zk−n.

The latter series is not quite a power series, since it includes terms with negative
exponents. These series are called Laurent series, after Pierre Alphonse Laurent
(1813–1854). For a power series (centered at 0), we could simply evaluate the
corresponding function at z = 0 to obtain the constant term; once we have
negative exponents, such an evaluation is no longer possible. However, if we
ﬁrst subtract all terms with negative exponents, we obtain a power series
whose constant term (which remains unchanged) can now be computed by
evaluating this remaining function at z = 0.
To be able to compute this constant term, we will expand f into partial
fractions. As a warmup to partial fraction decompositions, we ﬁrst work out
a 1-dimensional example. Let’s denote the a
th root of unity e2πi/a by ξa:

ξa := e2πi/a = cos 2π
a + i sin 2π
a ;

1.3 Partial Fractions and a Surprising Formula 9

then the collection of all a
th roots of unity comprises 1, ξa, ξ2
a, ξ3
a, . . . , ξa−1
a .

Example 1.4. Let’s ﬁnd the partial fraction expansion of 1
1−za . The poles of
this function are located at all a
th roots of unity ξk
a for k = 0, 1, . . . , a − 1. So
we expand 1
1 − za =
 a−1∑

k=0
 Ck
z − ξk
a .

To ﬁnd the coeﬃcients Ck, we proceed as follows:

Ck = lim
z→ξk
a
 (z − ξk
a ) ( 1
1 − za
 ) = lim
z→ξk
a
 1
−a za−1 = − ξk
a
a ,

where we have used L’Hˆopital’s rule in the penultimate equality. Therefore,
we arrive at the expansion
 1
1 − za = − 1
a
 a−1∑

k=0
 ξk
a
z − ξk
a . ⊓⊔

Returning to restricted partitions, the poles of f are located at z = 0 with
multiplicity n, at z = 1 with multiplicity 2, and at all the other a
th and bth

roots of unity with multiplicity 1, because a and b are relatively prime. Hence
our partial fraction expansion looks like this:

f (z) = A1
z + A2
z2 +· · ·+ An
zn + B1
z − 1 + B2
(z − 1)2 +
a−1∑

k=1
 Ck
z − ξk
a +
b−1∑

j=1
 Dj
z − ξj
b . (1.5)

We invite the reader to compute the coeﬃcients (Exercise 1.21)

Ck = − 1

a (1 − ξkb
a ) ξk(n−1)
a , (1.6)

Dj = − 1

b (1 − ξja
b ) ξj(n−1)
b .

To compute B2, we multiply both sides of (1.5) by (z − 1)
2 and take the limit
as z → 1 to obtain
 B2 = lim
z→1 (z − 1)2

(1 − za) (1 − zb) zn = 1
ab ,

by applying L’Hˆopital’s rule twice, for example. For the more interesting
constant B1, we compute

B1 = lim
z→1 (z − 1)
 ( 1
(1 − za) (1 − zb) zn −
 1
ab
(z − 1)2
 )
 = 1
ab − 1
2a − 1
2b − n
ab ,

10 1 The Coin-Exchange Problem of Frobenius

again by applying L’Hˆopital’s rule.
We do not need to compute the coeﬃcients A1, . . . , An, since they contribute
only to the terms with negative exponents, which we can safely neglect, because
those terms are diﬀerent from the constant term of f . Once we have the other
coeﬃcients, the constant term of the Laurent series of f is—as we said
above—the following function evaluated at 0:

p{a,b}(n) =
 

 B1
z − 1 + B2
(z − 1)2 +
 a−1∑

k=1
 Ck
z − ξk
a +
 b−1∑

j=1
 Dj
z − ξj
b
 



∣
∣
∣
∣
∣
∣z=0

= −B1 + B2 −
 a−1∑

k=1
 Ck
ξk
a −
 b−1∑

j=1
 Dj
ξj
b .

With (1.6) in hand, this simpliﬁes to

p{a,b}(n) = 1
2a + 1
2b + n
ab + 1
a
 a−1∑

k=1
 1
(1 − ξkb
a )ξkn
a + 1
b
 b−1∑

j=1
 1

(1 − ξja
b )ξjn
b . (1.7)

Encouraged by this initial success, we now proceed to analyze each sum in
(1.7) with the hope of recognizing them as more familiar objects.
For the next step, we need to deﬁne the greatest-integer function ⌊x⌋,
which denotes the greatest integer less than or equal to x. A close sibling
to this function is the fractional-part function {x} = x − ⌊x⌋. To readers
not familiar with the functions ⌊x⌋ and {x} we recommend working through
Exercises 1.3–1.5.
What we will do next is to study a special case, namely b = 1. This is
appealing, because p{a,1}(n) simply counts integer points in an interval:

p{a,1}(n) = # {(k, l) ∈ Z
2 : k, l ≥ 0, ak + l = n}

= # {k ∈ Z : k ≥ 0, ak ≤ n}

= # {
k ∈ Z : 0 ≤ k ≤ n
a
 }

= ⌊ n
a
 ⌋ + 1 .

(See Exercise 1.3.) On the other hand, in (1.7), we just computed a diﬀerent
expression for this function, so that

1
2a + 1
2 + n
a + 1
a
 a−1∑

k=1
 1
(1 − ξk
a ) ξkn
a = p{a,1}(n) = ⌊ n
a
 ⌋ + 1 .

With the help of the fractional-part function {x} = x − ⌊x⌋, we have derived
a formula for the following sum over the nontrivial a
th roots of unity:

1.3 Partial Fractions and a Surprising Formula 11

1
a
 a−1∑

k=1
 1
(1 − ξk
a ) ξkn
a = − { n
a
 } + 1
2 − 1
2a . (1.8)

We are almost there: we invite the reader (Exercise 1.22) to show that

1
a
 a−1∑

k=1
 1
(1 − ξbk
a ) ξkn
a = 1
a
 a−1∑

k=1
 1
(1 − ξk
a ) ξb−1kn
a , (1.9)

where b
−1 is an integer such that b−1b ≡ 1 mod a, and to conclude that

1
a
 a−1∑

k=1
 1
(1 − ξbk
a ) ξkn
a = − { b
−1n
a
 } + 1
2 − 1
2a . (1.10)

Now all that is left to do is to substitute this expression back into (1.7), which
yields the following beautiful formula due to Peter Barlow (1776–1862)
6 and
(in the form we state here) Tiberiu Popoviciu (1906–1975).

Theorem 1.5 (Barlow–Popoviciu formula). If a and b are relatively
prime, then
 p{a,b}(n) = n
ab − { b−1n
a
 } − { a−1n
b
 } + 1 ,

where b−1b ≡ 1 mod a and a
−1a ≡ 1 mod b. ⊓⊔

50 100 150 200 250 300 350 400 450 500

5

10
15
20
 n

p f 4,7g ( n )
 Fig. 1.2 The graph of p{4,7}(n).

6 For more information about Barlow, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Barlow.html.

12 1 The Coin-Exchange Problem of Frobenius

We shall have more to say about the arithmetic nature of restricted partition
functions in general; for now, let’s note that the function p{a,b}(n) behaves
roughly linearly, with a periodic part that stems from the fractional-part
functions. Figure 1.2 shows the behavior of the function for a = 4, b = 7.
Theorem 1.5 can be neatly and easily rewritten using greatest-integer
functions, as follows (Exercise 1.28):

Corollary 1.6. Given relatively prime positive integers a and b, let p and q
be positive integers such that aq − bp = 1. Then

p{a,b}(n) =
 {⌊ qn
b ⌋ − ⌊ pn
a ⌋ if a ∤ n ,
⌊ qn
b ⌋ − pn
a + 1 if a | n .

1.4 Sylvester’s Result

Before we apply Theorem 1.5 to obtain the classical Theorems 1.2 and 1.3, we
return for a moment to the geometry behind the restricted partition function
p{a,b}(n). In the 2-dimensional case (which is the setting of Theorem 1.5), we
are counting integer points (x, y) ∈ Z
2 on the line segments deﬁned by the
constraints ax + by = n , x, y ≥ 0 .

Thus this line segment connects the points (0, n
b ) and ( n
a , 0); we denote this
line segment by [(0, n
b ), ( n
a , 0)]. (More generally, we deﬁne the closed line
segment joining the points x and y ∈ Rd as follows:

[x, y] := {λ x + (1 − λ) y : 0 ≤ λ ≤ 1} ,

and we will use the usual similar notation to denote an open line segment
(x, y) and a half-open line segment (x, y].)
As n increases, the line segment [(0, n
b ), ( n
a , 0)] becomes dilated. It is not
too far-fetched (although Exercise 1.13 teaches us to be careful with such
statements) to expect that the likelihood for an integer point to lie on the
line segment increases with n. In fact, one might even guess that the number
of points on the line segment increases linearly with n, since the line segment
is a 1-dimensional object. Theorem 1.5 quantiﬁes the previous statement in
a very precise form: p{a,b}(n) has the “leading term” n
ab , and the remaining
terms are bounded as functions of n. Figure 1.3 shows the geometry behind
the counting function p{4,7}(n) for the ﬁrst few values of n. Note that the
thick line segment for n = 17 = 4 · 7 − 4 − 7 is the last one that does not
contain any integer point.

Lemma 1.7. If a and b are relatively prime positive integers and n ∈ [1, ab−1]
is not a multiple of a or b, then

1.4 Sylvester’s Result 13

1 2 3 4 5

1
2
3
 x

y
 Fig. 1.3 The nonnegative integer solutions to 4x + 7y = n for n = 0, 1, 2, . . . .

p{a,b}(n) + p{a,b}(ab − n) = 1 .

In other words, for n between 1 and ab − 1 and not divisible by a or b, exactly
one of the two integers n and ab − n is representable in terms of a and b.

Proof. This identity follows directly from Theorem 1.5:

p{a,b}(ab − n) = ab − n
ab − { b
−1(ab − n)
a
 } − { a
−1(ab − n)
b
 } + 1

= 2 − n
ab − { −b
−1n
a
 } − { −a
−1n
b
 }

(⋆)
= − n
ab + { b−1n
a
 } + { a
−1n
b
 }

= 1 − p{a,b}(n) .

Here, (⋆) follows from the fact that {−x} = 1 − {x} if x ̸∈ Z (see Exercise 1.5).
⊓⊔

Proof of Theorem 1.2. We have to show that p{a,b}(ab − a − b) = 0 and that
p{a,b}(n) > 0 for every n > ab − a − b. The ﬁrst assertion follows from
Exercise 1.24, which states that p{a,b}(a + b) = 1, and Lemma 1.7. To prove
the second assertion, we note that { m
a } ≤ 1 − 1
a for every integer m. Hence
for every positive integer n,

p{a,b}(ab − a − b + n) ≥ ab − a − b + n
ab − (1 − 1
a
 ) − (1 − 1
b
 ) + 1 = n
ab > 0 .

⊓⊔

14 1 The Coin-Exchange Problem of Frobenius

Proof of Theorem 1.3. Recall that Lemma 1.7 states that for n between 1 and
ab − 1 and not divisible by a or b, exactly one of n and ab − n is representable.
There are ab − a − b + 1 = (a − 1)(b − 1)

integers between 1 and ab − 1 that are not divisible by a or b. Finally, we note
that p{a,b}(n) > 0 if n is a multiple of a or b, by the very deﬁnition of p{a,b}(n).
Hence the number of nonrepresentable integers is 1
2 (a − 1)(b − 1). ⊓⊔

Note that we have proved even more. Essentially by Lemma 1.7, every
positive integer less than ab has at most one representation. Hence, the
representable integers less than ab are uniquely representable (see also Exer-
cise 1.25).

1.5 Three and More Coins

What happens to the complexity of the Frobenius problem if we have more
than two coins? Let’s return to our restricted partition function

pA(n) = # {
(m1, . . . , md) ∈ Z
d : all mj ≥ 0, m1a1 + · · · + mdad = n} ,

where A = {a1, . . . , ad}. By the very same reasoning as in Section 1.3, we can
easily write down the generating function for pA(n):

∑

n≥0 pA(n) zn = ( 1
1 − za1
 ) ( 1
1 − za2
 ) · · · ( 1
1 − zad
 ) .

We use the same methods that were exploited in Section 1.3 to recover our
function pA(n) as the constant term of a useful generating function. Namely,

pA(n) = const ( 1
(1 − za1 ) (1 − za2) · · · (1 − zad ) zn
 ) .

We now expand the function on the right into partial fractions. For reasons of
simplicity, we assume in the following that a1, . . . , ad are pairwise relatively
prime; that is, no two of the integers a1, a2, . . . , ad have a common factor.
Then our partial fraction expansion looks like this:

f (z) = 1
(1 − za1) · · · (1 − zad ) zn

= A1
z + A2
z2 + · · · + An
zn + B1
z − 1 + B2
(z − 1)2 + · · · + Bd
(z − 1)d (1.11)

+
 a1−1∑

k=1
 C1k
z − ξk
a1 +
 a2−1∑

k=1
 C2k
z − ξk
a2 + · · · +
 ad−1∑

k=1
 Cdk
z − ξk
ad .

1.5 Three and More Coins 15

By now, we are experienced in computing partial fraction coeﬃcients, so that
the reader will easily verify that (Exercise 1.31)

C1k = − 1

a1 (1 − ξka2
a1 ) (
1 − ξka3
a1 ) · · · (1 − ξkad
a1 ) ξk(n−1)
a1 . (1.12)

As before, we do not have to compute the coeﬃcients A1, . . . , An, because
they do not contribute to the constant term of f . For the computation of
B1, . . . , Bd, we may use a symbolic manipulation program such as Maple,
Mathematica, or Sage. Again, once we have calculated these coeﬃcients, we
can compute the constant term of f by dropping all negative exponents and
evaluating the remaining function at 0:

pA(n) =
 ( B1
z − 1 + · · · + Bd
(z − 1)d +
 a1−1∑

k=1
 C1k
z − ξk
a1 + · · · +
 ad−1∑

k=1
 Cdk
z − ξk
ad
 )∣
∣
∣
∣
∣z=0

= −B1 + B2 − · · · + (−1)
dBd −
 a1−1∑

k=1
 C1k
ξk
a1 − · · · −
 ad−1∑

k=1
 Cdk
ξk
ad .

Substituting the expression we found for C1k into the latter sum over the
nontrivial a
th
1 roots of unity, for example, gives rise to

1
a1
 a1−1∑

k=1
 1
(1 − ξka2
a1 ) (
1 − ξka3
a1 ) · · · (1 − ξkad
a1 ) ξkn
a1 .

This motivates the deﬁnition of the Fourier–Dedekind sum

sn (a1, a2, . . . , am; b) := 1
b
 b−1∑

k=1
 ξkn
b(1 − ξka1
b ) (
1 − ξka2
b ) · · · (1 − ξkam
b ) . (1.13)

We will study these sums in detail in Chapter 8. With this deﬁnition, we have
arrived at the following result.

Theorem 1.8. The restricted partition function for A = {a1, a2, . . . , ad},
where the ak’s are pairwise relatively prime, can be computed as

pA(n) = −B1 + B2 − · · · + (−1)dBd + s−n (a2, a3, . . . , ad; a1)

+ s−n (a1, a3, a4, . . . , ad; a2) + · · · + s−n (a1, a2, . . . , ad−1; ad) .

Here B1, B2, . . . , Bd are the partial fraction coeﬃcients in the expansion (1.11).
⊓⊔

Example 1.9. We give the restricted partition functions for d = 3 and 4.
These closed-form formulas have proven useful in the reﬁned analysis of the
periodicity that is inherent in the restricted partition function pA(n). For

16 1 The Coin-Exchange Problem of Frobenius

example, one can visualize the graph of p{a,b,c}(n) as a “wavy parabola,” as its
formula plainly shows (Figure 1.4 gives an example, the case A = {4, 7, 15}):

p{a,b,c}(n) = n2

2abc + n
2
 ( 1
ab + 1
ac + 1
bc
 ) + 1
12
 ( 3
a + 3
b + 3
c + a
bc + b
ac + c
ab
 )

+ 1
a
 a−1∑

k=1
 1
(1 − ξkb
a ) (1 − ξkc
a ) ξkn
a + 1
b
 b−1∑

k=1
 1
(1 − ξkc
b ) (
1 − ξka
b ) ξkn
b

+ 1
c
 c−1∑

k=1
 1
(1 − ξka
c ) (1 − ξkb
c ) ξkn
c ,

p{a,b,c,d}(n) = n3

6abcd + n2

4
 ( 1
abc + 1
abd + 1
acd + 1
bcd
 )

+ n
12
 ( 3
ab + 3
ac + 3
ad + 3
bc + 3
bd + 3
cd + a
bcd + b
acd + c
abd + d
abc
 )

+ 1
24
 ( a
bc + a
bd + a
cd + b
ad + b
ac + b
cd + c
ab + c
ad + c
bd

+ d
ab + d
ac + d
bc
 ) − 1
8
 ( 1
a + 1
b + 1
c + 1
d
 )

+ 1
a
 a−1∑

k=1
 1
(1 − ξkb
a ) (1 − ξkc
a ) (1 − ξkd
a ) ξkn
a

+ 1
b
 b−1∑

k=1
 1
(1 − ξkc
b ) (
1 − ξkd
b ) (
1 − ξka
b ) ξkn
b

+ 1
c
 c−1∑

k=1
 1
(1 − ξkd
c ) (1 − ξka
c ) (1 − ξkb
c ) ξkn
c

+ 1
d
 d−1∑

k=1
 1
(1 − ξka
d ) (
1 − ξkb
d ) (
1 − ξkc
d ) ξkn
d . ⊓⊔

Notes

1. The theory of generating functions has a long and powerful tradition. We
only touch on its utility. For those readers who would like to dig a little deeper
into the vast generating-function garden, we strongly recommend Herb Wilf’s
generatingfunctionology [253] and L´aszl´o Lov´asz’s Combinatorial Problems and
Exercises [166]. The reader might wonder why we do not stress convergence
aspects of the generating functions we play with. Almost all of our series

Notes 17

20 40 60 80 100 120 140 160 180 200

10
20
30
40
50
 n

p f 4,7,15 g ( n )
 Fig. 1.4 The graph of p{4,7,15}(n).

are geometric series and have trivial convergence properties. In the spirit of
not muddying the waters of lucid mathematical exposition, we omit such
convergence details.

2. The Frobenius problem is named after Georg Frobenius, who apparently
liked to raise this problem in his lectures [61]. Theorem 1.2 is one of the famous
folklore results and might be one of the most misquoted theorems in all of
mathematics. People usually cite James J. Sylvester’s problem in [240], but
his paper contains Theorem 1.3 rather than Theorem 1.2. In fact, Sylvester’s
problem had previously appeared as a theorem in [239]. It is not known who
ﬁrst discovered or proved Theorem 1.2. It is very conceivable that Sylvester
knew about it when he came up with Theorem 1.3.

3. The linear Diophantine problem of Frobenius should not be confused with
the postage-stamp problem. The latter problem asks for a similar determination,
but adds an additional independent bound on the size of the integer solutions
to the linear equation.

4. Theorem 1.5 has a fascinating history. The earliest appearance of this result
(in the form of Corollary 1.6) that we are aware of is in a book on elementary
number theory, from 1811, by Peter Barlow [18, p. 323–325]. The version we
state in Theorem 1.5 (which is our ﬁrst example of a quasipolynomial, a term
we will see frequently in the coming chapters) seems to go back to a paper
by Tiberiu Popoviciu [196]. The Barlow–Popoviciu formula has since been
resurrected at least twice [216, 246].

18 1 The Coin-Exchange Problem of Frobenius

Guglielmo Libri (1803–1869),7 a mathematical prodigy, wrote down a
version of the Barlow–Popoviciu formula in terms of trigonometric functions.
His exceedingly colorful life is perhaps best summed up in the following
quotataion from [206]:

Admirable in the salons and incomparably friendly, ﬂexible, with gentle epigrams of
sweet humour, elegant ﬂattery, a good writer in both French and Italian, a profound
mathematician, geometer, physicist, knowing history through and through, a very
analytic and comparative mind . . . more expert than an auctioneer or a bookseller
in the science of books, this man had only one misfortune: he was essentially a thief.

5. Fourier–Dedekind sums ﬁrst surfaced implicitly in Sylvester’s work (see,
e.g., [238]) and explicitly in connection with restricted partition functions
in [144]. They were rediscovered in [38], in connection with the Frobenius
problem. The papers [114, 209] contain interesting connections to Bernoulli
and Euler polynomials. We will resume the study of Fourier–Dedekind sums
in Chapter 8.

6. As we mentioned above, the Frobenius problem for d ≥ 3 is much harder
than the case d = 2 that we have discussed. Certainly beyond d = 3, the
Frobenius problem is wide open, though much eﬀort has been put into its
study. The literature on the Frobenius problem is vast, and there is still much
room for improvement. The interested reader might consult the comprehensive
monograph [202], which surveys the references to almost all articles dealing
with the Frobenius problem and gives about 40 open problems and conjectures
related to the Frobenius problem. To give a ﬂavor, we mention two landmark
results that go beyond d = 2.
The ﬁrst one concerns the generating function r(z) := ∑

k∈R zk, where
R is the set of all integers representable by a given set of relatively prime
positive integers a1, a2, . . . , ad. It is not hard to see (Exercise 1.36) that r(z) =
p(z)/ (1 − za1) (1 − za2) · · · (1 − zad ) for some polynomial p. This rational
generating function contains all the information about the Frobenius problem;
for example, the Frobenius number is the total degree of the rational function
1
1−z − r(z). Hence the Frobenius problem reduces to ﬁnding the polynomial
p, the numerator of r. Marcel Morales [180, 181] and Graham Denham [103]
discovered the remarkable fact that for d = 3, the polynomial p has either four
or six terms. Moreover, they gave semiexplicit formulas for p. The Morales–
Denham theorem implies that the Frobenius number in the case d = 3 is
quickly computable, a result that is originally due, in various disguises, to
J¨urgen Herzog [133], Harold Greenberg [125], and J. Leslie Davison [94]. As
much as there seems to be a well-deﬁned border between the cases d = 2
and d = 3, there also seems to be such a border between the cases d = 3
and d = 4: Henrik Bresinsky [65] proved that for d ≥ 4, there is no absolute

7 For more information about Libri, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Libri.html.

Exercises 19

bound on the number of terms in the numerator p, in sharp contrast to the
Morales–Denham theorem.
On the other hand, Alexander Barvinok and Kevin Woods [24] proved that
for ﬁxed d, the rational generating function r(z) can be written as a “short”
sum of rational functions; in particular, r can be eﬃciently computed when d
is ﬁxed. A corollary of this fact is that the Frobenius number can be eﬃciently
computed when d is ﬁxed; this theorem is due to Ravi Kannan [145]. On the
other hand, Jorge Ram´ırez-Alfons´ın [201] proved that trying to compute the
Frobenius number eﬃciently is hopeless if d is left as a variable.
While the above results settle the theoretical complexity of the computation
of the Frobenius number, practical algorithms are a completely diﬀerent
matter. Both Kannan’s and Barvinok–Woods’s ideas seem complex enough
that nobody has yet tried to implement them. The currently most competitive
algorithms include [50, 60, 208].

Exercises

1.1. ♣ Check the partial fraction expansion (1.2):

z
1 − z − z2 = 1/
√5

1 − 1+
√5
2 z − 1/
√5

1 − 1−
√5
2 z .

1.2. ♣ Suppose z is a complex number, and n a positive integer. Show that

(1 − z) (1 + z + z2 + · · · + zn) = 1 − zn+1,

and use this to prove that if |z| < 1, then

∑

k≥0 zk = 1
1 − z .

1.3. ♣ Find a formula for the number of lattice points in [a, b] for arbitrary
real numbers a and b.

1.4. Prove the following. Unless stated diﬀerently, n ∈ Z and x, y ∈ R.

(a) ⌊x + n⌋ = ⌊x⌋ + n.
(b) ⌊x⌋ + ⌊y⌋ ≤ ⌊x + y⌋ ≤ ⌊x⌋ + ⌊y⌋ + 1.

(c) ⌊x⌋ + ⌊−x⌋ = { 0 if x ∈ Z,
−1 otherwise.

(d) For n ∈ Z>0, ⌊ ⌊x⌋
n ⌋ = ⌊ x
n ⌋.

(e) − ⌊−x⌋ is the least integer greater than or equal to x, denoted by ⌈x⌉.
(f) ⌊x + 1
2 ⌋ is the nearest integer to x (and if two integers are equally close
to x, it is the larger of the two).

20 1 The Coin-Exchange Problem of Frobenius

(g) ⌊x⌋ + ⌊
x + 1
2 ⌋ = ⌊2x⌋.
(h) If m and n are positive integers, ⌊ m
n ⌋ is the number of integers among
1, . . . , m that are divisible by n.
(i) ♣ If m ∈ Z>0, n ∈ Z, then ⌊ n−1
m ⌋ = − ⌊ −n
m ⌋ − 1.
(j) ♣ If m ∈ Z>0, n ∈ Z, then ⌊ n−1
m ⌋ + 1 is the least integer greater than or
equal to n
m .

1.5. Rewrite in terms of the fractional-part function as many of the above
identities as you can make sense of.

1.6. Suppose m and n are relatively prime positive integers. Prove that

m−1∑

k=0
 ⌊ kn
m
 ⌋ =
 n−1∑

j=0
 ⌊ jm
n
 ⌋ = 1
2 (m − 1)(n − 1) .

1.7. Prove the following identities. They will come in handy at least twice:
when we study partial fractions, and when we discuss ﬁnite Fourier series. For
φ, ψ ∈ R, n ∈ Z>0, m ∈ Z,

(a) e
i0 = 1
(b) e
iφ eiψ = ei(φ+ψ)

(c) 1
eiφ = e
−iφ

(d) ei(φ+2π) = eiφ

(e) e2πi = 1
(f) ∣
∣eiφ∣
∣ = 1
(g) d
dφ e
iφ = i e
iφ

(h)
 n−1∑

k=0 e
2πikm/n =
 {n if n | m ,
0 otherwise

(i) If n > 1 then
 n−1∑

k=1 k e2πik/n = n
e2πi/n − 1 .

1.8. Suppose m, n ∈ Z and n > 0. Find a closed form for

n−1∑

k=0
 { k
n
 } e2πikm/n =
 n−1∑

k=0
 k
n e
2πikm/n

(as a function of m and n).

1.9. ♣ Suppose m and n are relatively prime integers, and n is positive. Show
that {
e2πimk/n : 0 ≤ k < n
} = {
e2πij/n : 0 ≤ j < n
}

and {
e2πimk/n : 0 < k < n
} = {
e2πij/n : 0 < j < n
} .

Exercises 21

Conclude that if f is any complex-valued function, then

n−1∑

k=0 f (e
2πimk/n) =
 n−1∑

j=0 f (e2πij/n)

and n−1∑

k=1 f (e2πimk/n) =
 n−1∑

j=1 f (e
2πij/n) .

1.10. Suppose n is a positive integer. If you know what a group is, prove
that the set {
e2πik/n : 0 ≤ k < n
} forms a cyclic group of order n (under
multiplication in C).

1.11. Fix n ∈ Z>0. For an integer m, let (m mod n) denote the least nonneg-
ative integer in G1 := Zn to which m is congruent. Let’s denote by ⋆ addition
modulo n, and by ◦ the following composition:

{ m1
n
 } ◦ { m2
n
 } = { m1 + m2
n
 } ,

deﬁned on the set G2 := {{ m
n } : m ∈ Z
}. Deﬁne the following functions:

φ ((m mod n)) = e2πim/n,

ψ (e2πim/n) = { m
n
 } ,

χ ({ m
n
 }) = (m mod n) .

Prove the following:

φ ((m1 mod n) ⋆ (m2 mod n)) = φ ((m1 mod n)) φ ((m2 mod n)) ,

ψ (e2πim1/ne2πim2/n) = ψ (e2πim1/n) ◦ ψ (e2πim2/n) ,

χ ({ m1
n
 } ◦ { m2
n
 }) = χ ({ m1
n
 }) ⋆ χ ({ m2
n
 }) .

Prove that the three maps deﬁned above, namely φ, ψ, and χ, are one-to-one.
Again, for the reader who is familiar with the notion of a group, let G3 be the
group of nth roots of unity. What we have shown is that the three groups G1,
G2, and G3 are all isomorphic. It is very useful to cycle among these three
isomorphic groups.

1.12. ♣ Given integers a, b, c, d, form the line segment [(a, b), (c, d)] ⊂ R2

joining the points (a, b) and (c, d). Show that the number of integer points on
this line segment is gcd(a − c, b − d) + 1.

1.13. Give an example of a line with

22 1 The Coin-Exchange Problem of Frobenius

(a) no lattice points;
(b) one lattice point;
(c) an inﬁnite number of lattice points.

In each case, state—if appropriate—necessary conditions about the (ir)rationa-
lity of the slope.

1.14. Suppose a line y = mx + b passes through the lattice points (p1, q1) and
(p2, q2). Prove that it also passes through the lattice points
(p1 + k(p2 − p1), q1 + k(q2 − q1)), k ∈ Z .

1.15. Given positive irrational numbers p and q with 1
p + 1
q = 1, show that
Z>0 is the disjoint union of the two integer sequences {⌊pn⌋ : n ∈ Z>0} and
{⌊qn⌋ : n ∈ Z>0}. This theorem from 1894 is due to Lord Rayleigh and was
rediscovered in 1926 by Sam Beatty. Sequences of the form {⌊pn⌋ : n ∈ Z>0}
are often called Beatty sequences.

1.16. Let a, b, c, d ∈ Z. We say that {(a, b) , (c, d)} is a lattice basis of Z
2 if
every lattice point (m, n) ∈ Z
2 can be written as

(m, n) = p (a, b) + q (c, d)

for some p, q ∈ Z. Prove that if {(a, b) , (c, d)} and {(e, f ) , (g, h)} are lattice
bases of Z
2, then there exists an integer matrix M with determinant ±1 such
that ( a b
c d
 ) = M ( e f
g h
 ) .

Conclude that the determinant of ( a b
c d
 ) is ±1.

1.17. ♣ Prove that a triangle with vertices on the integer lattice has no other
interior/boundary lattice points if and only if it has area 1
2 . (Hint: You may
begin by “doubling” the triangle to form a parallelogram.)

1.18. Let’s deﬁne a northeast lattice path as a path through lattice points
that uses only the steps (1, 0) and (0, 1). Let Ln be the line deﬁned by
x + 2y = n. Prove that the number of northeast lattice paths from the origin
to a lattice point on Ln is the (n + 1)th Fibonacci number fn+1.

1.19. Compute the coeﬃcients of the Taylor series of 1
(1−z)2 expanded at
z = 0

(a) by a counting argument,
(b) by diﬀerentiating the geometric series.

Generalize.

1.20. ♣ Prove that if a1, a2, . . . , ad ∈ Z>0 do not have a common factor, then
the Frobenius number g(a1, . . . , ad) is well deﬁned.

Exercises 23

1.21. ♣ Compute the partial fraction coeﬃcients (1.6).

1.22. ♣ Prove (1.9): for relatively prime positive integers a and b,

1
a
 a−1∑

k=1
 1
(1 − ξbk
a ) ξkn
a = 1
a
 a−1∑

k=1
 1
(1 − ξk
a ) ξb−1kn
a ,

where b
−1b ≡ 1 mod a, and deduce from this (1.10), namely,

1
a
 a−1∑

k=1
 1
(1 − ξbk
a ) ξkn
a = − { b
−1n
a
 } + 1
2 − 1
2a .

(Hint: Use Exercise 1.9.)

1.23. Prove that for relatively prime positive integers a and b,

p{a,b}(n + ab) = p{a,b}(n) + 1 .

1.24. ♣ Show that if a and b are relatively prime integers ≥ 2, then

p{a,b}(a + b) = 1 .

1.25. To extend the Frobenius problem, we say that an integer n is k-
representable if pA(n) = k; that is, n can be represented in exactly k
ways using the integers in the set A. Deﬁne gk = gk(a1, . . . , ad) to be the
largest k-representable integer. Prove:

(a) Let d = 2. For every k ∈ Z≥0, there is an N such that all integers larger
than N have at least k representations (and hence gk(a, b) is well deﬁned).
(b) gk(a, b) = (k + 1)ab − a − b.
(c) Given k ≥ 2, the smallest k-representable integer is ab(k − 1).
(d) The smallest interval containing all uniquely representable integers is
[min(a, b), g1(a, b)].
(e) Given k ≥ 2, the smallest interval containing all k-representable integers
is [gk−2(a, b) + a + b, gk(a, b)].
(f) There are exactly ab − 1 integers that are uniquely representable. Given
k ≥ 2, there are exactly ab k-representable integers.
(g) Extend all of this to d ≥ 3 (see Open Problem 1.43).

1.26. Find a formula for p{a}(n).

1.27. Prove the following recurrence formula for n ∈ Z≥0:

p{a1,...,ad}(n) =
 ⌊ n
ad ⌋
∑

m=0 p{a1,...,ad−1}(n − m ad) .

Use it in the case d = 2 to give an alternative proof of Theorem 1.2.

24 1 The Coin-Exchange Problem of Frobenius

1.28. Prove the equivalence of Theorem 1.5 and Corollary 1.6.

1.29. Give an alternative proof of Corollary 1.6 (i.e., one that does not use
partial fraction expansions of generating functions).

1.30. Prove the following extension of Theorem 1.5: Suppose gcd(a, b) = d.
Then
 p{a,b}(n) =
 { nd
ab − { βn
a } − { αn
b } + 1 if d|n,
0 otherwise,

where β b
d ≡ 1 mod a
d and α a
d ≡ 1 mod b
d .

1.31. ♣ Compute the partial fraction coeﬃcient (1.12).

1.32. Find a formula for p{a,b,c}(n) for the case gcd(a, b, c) ̸= 1.

1.33. ♣ With A = {a1, a2, . . . , ad} ⊂ Z>0, let

p◦
A(n) := # {(m1, . . . , md) ∈ Z
d : all mj > 0, m1a1 + · · · + mdad = n} ;

that is, p
◦
A(n) counts the number of partitions of the positive integer n using
only the elements of A as parts, where each part is used at least once. Find
formulas for p
◦
A for A = {a} , A = {a, b} , A = {a, b, c} , A = {a, b, c, d}, where
a, b, c, d are pairwise relatively prime positive integers. Observe that in all
examples, the counting functions pA and p
◦
A satisfy the algebraic relation

p◦
A(−n) = (−1)d−1 pA(n) .

(What we mean here is the following: using the algebraic expression for p◦
A(n),
substitute n by −n, even though negative arguments do not make sense in
terms of the combinatorial deﬁnition of p
◦
A(n). Then compare this formula
with the algebraic expression for (−1)d−1 pA(n).)

1.34. Prove that p◦
A(n) = pA (n − a1 − a2 − · · · − ad) for n ≥ a1+a2+· · ·+ad.
(Here, as usual, A = {a1, a2, . . . , ad}.) Conclude that in the examples of
Exercise 1.33, the algebraic relation

pA(−n) = (−1)d−1 pA (n − a1 − a2 − · · · − ad)

holds.

1.35. For relatively prime positive integers a, b, let

R := {am + bn : m, n ∈ Z≥0} ,

the set of all integers representable by a and b. Prove that

∑

k∈R zk = 1 − zab

(1 − za) (1 − zb) .

Exercises 25

Use this rational generating function to give alternative proofs of Theorems 1.2
and 1.3.

1.36. For relatively prime positive integers a1, a2, . . . , ad, let

R := {m1a1 + m2a2 + · · · + mdad : m1, m2, . . . , md ∈ Z≥0} ,

the set of all integers representable by a1, a2, . . . , ad. Prove that

r(z) := ∑

k∈R zk = p(z)
(1 − za1) (1 − za2) · · · (1 − zad )

for some polynomial p.

1.37. Prove Theorem 1.1: Given a rational function p(z)∏m
k=1(z−ak)
ek , where p is
a polynomial of degree less than e1 + e2 + · · · + em and the ak are distinct,
there exists a decomposition

m∑

k=1
 ( ck,1
z − ak + ck,2
(z − ak)
2 + · · · + ck,ek
(z − ak)ek
 )
 ,

where the ck,j ∈ C are unique.
Here is an outline of one possible proof. Recall that the set of polynomials
(over R or C) forms a Euclidean domain, that is, given two polynomials
a(z), b(z), there exist polynomials q(z), r(z) with deg(r) < deg(b) such that

a(z) = b(z) q(z) + r(z) .

Applying this procedure repeatedly (the Euclidean algorithm) gives the great-
est common divisor of a(z) and b(z) as a linear combination of a(z) and b(z),
that is, there exist polynomials c(z) and d(z) such that a(z)c(z) + b(z)d(z) =
gcd (a(z), b(z)).

Step 1: Apply the Euclidean algorithm to show that there exist polynomials
u1, u2 such that

u1(z) (z − a1)e1 + u2(z) (z − a2)e2 = 1 .

Step 2: Deduce that there exist polynomials v1, v2 with deg (vk) < ek such
that p(z)
(z − a1)e1 (z − a2)e2 = v1(z)
(z − a1)
e1 + v2(z)
(z − a2)
e2 .

(Hint: Long division.)
Step 3: Repeat this procedure to obtain a partial fraction decomposition for

p(z)
(z − a1)e1 (z − a2)
e2 (z − a3)
e3 .

26 1 The Coin-Exchange Problem of Frobenius

Open Problems

1.38. Come up with a new approach or a new algorithm for the Frobenius
problem in the d = 4 case.

1.39. There are a very good lower [94] and several upper bounds [202, Chap-
ter 3] for the Frobenius number. Come up with improved upper bounds.

1.40. Solve Vladimir I. Arnold’s Problems 1999–2008 through 1999–2011 [11].
To give a ﬂavor, we mention two of the problems explicitly:

(a) Explore the statistics of g (a1, a2, . . . , ad) for typical large a1, a2, . . . , ad. It
is conjectured that g (a1, a2, . . . , ad) grows asymptotically like a constant
times d−1√a1a2 · · · ad. (See [4, 5, 116].)
(b) Determine what fraction of the integers in the interval [0, g (a1, a2, . . . , ad)]
are representable, for typical large a1, a2, . . . , ad. It is conjectured that
this fraction is asymptotically equal to 1
d . (Theorem 1.3 implies that this
conjecture is true in the case d = 2.)

1.41. Study vector generalizations of the Frobenius problem [204, 222].

1.42. There are several special cases of A = {a1, a2, . . . , ad} for which the
Frobenius problem is solved, for example arithmetic sequences [202, Chapter 3];
see also [217, 247, 248]. Study these special cases in light of the generating
function r(x), deﬁned in the notes and in Exercise 1.36.

1.43. Study the generalized Frobenius number gk (deﬁned in Exercise 1.25;
see also [42, 45, 218]), e.g., in light of the Morales–Denham theorem mentioned
in the notes. Derive formulas for special cases, e.g., arithmetic sequences.

1.44. For which 0 ≤ n ≤ b − 1 is sn (a1, a2, . . . , ad; b) = 0? (See also Open
Problem 8.24.)

Chapter 2
A Gallery of Discrete Volumes

Few things are harder to put up with than a good example.

Mark Twain (1835–1910)

A unifying theme of this book is the study of the number of integer points in
polytopes, where the polytopes live in a real Euclidean space Rd. The integer
points Z
d form a lattice in Rd, and we often call the integer points lattice
points. This chapter carries us through concrete instances of lattice-point
enumeration in various integral and rational polytopes. There is a tremendous
amount of research taking place along these lines, even as the reader is looking
at these pages.

2.1 The Language of Polytopes

A polytope in dimension 1 is a closed interval; the number of integer points
in [ a
b , c
d ] is easily seen to be ⌊ c
d ⌋ − ⌊ a−1
b ⌋ (Exercise 2.1; here we assume that
a, b, c, d ∈ Z with a
b < c
d ). A 2-dimensional convex polytope is a convex
polygon: a compact convex subset of R2 bounded by a simple closed curve
that is made up of ﬁnitely many line segments.
In general dimension d, a convex polytope is the convex hull of ﬁnitely
many points in Rd. To be precise, for a ﬁnite point set {v1, v2, . . . , vn} ⊂ Rd,
the polytope P is the smallest convex set containing those points; that is,

P = {λ1v1 + λ2v2 + · · · + λnvn : all λk ≥ 0 and λ1 + λ2 + · · · + λn = 1} .

This deﬁnition is called the vertex description of P, and we use the notation

P = conv {v1, v2, . . . , vn} ,
 27

28 2 A Gallery of Discrete Volumes

the convex hull of v1, v2, . . . , vn. In particular, a polytope is a closed subset of
Rd. Many polytopes that we will study, however, are not deﬁned in this way, but
rather as bounded intersections of ﬁnitely many half-spaces and hyperplanes.
One example is the polytope P deﬁned by (1.4) in Chapter 1. (A set, bounded
or not, that can be described as the intersection of ﬁnitely many half-spaces
and hyperplanes is a polyhedron.) This hyperplane description of a
polytope is, in fact, equivalent to the vertex description. The fact that every
polytope has both a vertex and a hyperplane description is highly nontrivial,
both algorithmically and conceptually. We carefully work out a proof in
Appendix A.
The dimension of a polytope P is the dimension of the aﬃne space

span P := {x + λ(y − x) : x, y ∈ P, λ ∈ R}

spanned by P. If P has dimension d, we use the notation dim P = d and call
P a d-polytope. Note that P ⊂ Rd does not necessarily have dimension d. For
example, the polytope P deﬁned by (1.4) has dimension d − 1.
For a convex polytope P ⊂ Rd, we say that the hyperplane H ={
x ∈ Rd : a · x = b} is a supporting hyperplane of P if P lies entirely
on one side of H, that is,

P ⊂ {
x ∈ Rd : a · x ≤ b} or P ⊂ {
x ∈ Rd : a · x ≥ b} .

A face of P is a set of the form P ∩ H, where H is a supporting hyperplane
of P. Note that P itself is a face of P, corresponding to the degenerate
hyperplane Rd,1 and the empty set ∅ is a face of P, corresponding to a
hyperplane that does not meet P. The (d − 1)-dimensional faces are called
facets, the 1-dimensional faces edges, and the 0-dimensional faces vertices
of P. Vertices are the “extreme points” of a polytope.
A convex d-polytope has at least d + 1 vertices. A convex d-polytope with
exactly d + 1 vertices is called a d-simplex. Every 1-dimensional convex
polytope is a 1-simplex, namely, a line segment. The 2-dimensional simplices
are the triangles, the 3-dimensional simplices the tetrahedra.
A convex polytope P is called integral if all of its vertices have integer
coordinates,2 and P is called rational if all of its vertices have rational
coordinates.

1 In the remainder of the book, we will reserve the term hyperplane for nondegenerate
hyperplanes, i.e., sets of the form {x ∈ Rd : a · x = b}, where not all of the entries of a
are zero.

2 Integral polytopes are also called lattice polytopes.

2.2 The Unit Cube 29

2.2 The Unit Cube

As a warmup example, we begin with the unit d-cube 2 := [0, 1]d, which
simultaneously oﬀers simple geometry and an endless fountain of research
questions. The vertex description of 2 is given by the set of 2d vertices
{(x1, x2, . . . , xd) : all xk = 0 or 1}. The hyperplane description is

2 = {(x1, x2, . . . , xd) ∈ Rd : 0 ≤ xk ≤ 1 for all k = 1, 2, . . . , d} .

Thus, there are the 2d bounding hyperplanes x1 = 0, x1 = 1, x2 = 0, x2 =
1, . . . , xd = 0, xd = 1.
We now compute the discrete volume of an integer dilate of 2. That is, we
seek the number of integer points t 2 ∩ Z
d for all t ∈ Z>0. Here tP denotes
the dilated polytope

{(tx1, tx2, . . . , txd) : (x1, x2, . . . , xd) ∈ P} ,

for a polytope P. What is the discrete volume of 2? We dilate by the positive
integer t, as depicted in Figure 2.1, and count:

# (t 2 ∩ Z
d) = # ([0, t]
d ∩ Z
d) = (t + 1)d.

Fig. 2.1 The 6th dilate of
2 in dimension 2.

6

6
 1

1
 x 1

x 2

P
 6 P
 We generally denote the lattice-point enumerator for the tth dilate of
P ⊂ Rd by LP (t) := # (tP ∩ Z
d) ,

a useful object that we also call the discrete volume of P. We may also
think of leaving P ﬁxed and shrinking the integer lattice:

LP (t) = # (P ∩ 1
t Z
d) .

30 2 A Gallery of Discrete Volumes

With this convention, L2(t) = (t + 1)
d, a polynomial in the integer variable t.
Notice that the coeﬃcients of this polynomial are the binomial coeﬃcients(d
k), deﬁned through
(
m
n
 ) := m(m − 1)(m − 2) · · · (m − n + 1)
n! (2.1)

for m ∈ C, n ∈ Z>0.
What about the interior 2
◦ of the cube? The number of interior integer
points in t 2
◦ is

L2◦ (t) = # (t 2
◦ ∩ Z
d) = # ((0, t)d ∩ Z
d) = (t − 1)d.

Notice that this polynomial equals (−1)dL2(−t), the evaluation of the poly-
nomial L2(t) at negative integers, up to a sign.
We now introduce another important tool for analyzing a polytope P,
namely the generating function of LP :

EhrP (z) := 1 + ∑

t≥1 LP (t) zt.

This generating function is also called the Ehrhart series of P.
In our case, the Ehrhart series of P = 2 takes on a special form. To
illustrate, we deﬁne the Eulerian number A (d, k) through3

∑

j≥0 jd zj = ∑d
k=0 A (d, k) zk

(1 − z)d+1 . (2.2)

It is not hard to see that the polynomial ∑d
k=1 A (d, k) zk is the numerator of
the rational function
(z d
dz
 )d ( 1
1 − z
 ) = z d
dz · · · z d
dz︸ ︷︷ ︸
d times
 ( 1
1 − z
 ) .

The Eulerian numbers have many fascinating properties, including

A (d, k) = A (d, d + 1 − k) ,

A (d, k) = (d − k + 1) A (d − 1, k − 1) + k A (d − 1, k) ,

d∑

k=0 A (d, k) = d! , (2.3)

3 There are two slightly conﬂicting deﬁnitions of Eulerian numbers in the literature: some-

times, they are deﬁned through ∑

j≥0(j + 1)d zj =
 ∑d
k=0 A(d,k)zk

(1−z)d+1 instead of (2.2).

2.3 The Standard Simplex 31

A (d, k) =
 k∑

j=0(−1)
j(d + 1
j
 )(k − j)
d.

The ﬁrst few Eulerian numbers A (d, k) for 0 ≤ k ≤ d are

d = 0: 1
d = 1: 0 1
d = 2: 0 1 1
d = 3: 0 1 4 1
d = 4: 0 1 11 11 1
d = 5: 0 1 26 66 26 1
d = 6: 0 1 57 302 302 57 1

(see also [1, Sequence A008292]).
With this deﬁnition, we can now express the Ehrhart series of 2 in terms
of Eulerian numbers:

Ehr2(z) = 1 + ∑

t≥1(t + 1)d zt = ∑

t≥0(t + 1)d zt = 1
z
 ∑

t≥1 td zt

= ∑d
k=1 A (d, k) zk−1

(1 − z)d+1 .

To summarize, we have proved the following theorem.

Theorem 2.1. Let 2 be the unit d-cube.

(a) The lattice-point enumerator of 2 is the polynomial

L2(t) = (t + 1)d =
 d∑

k=0
 (d
k
)t
k.

(b) Its evaluation at negative integers yields the relation

(−1)dL2(−t) = L2◦ (t) .

(c) The Ehrhart series of 2 is Ehr2(z) =
 ∑d
k=1 A(d,k)zk−1

(1−z)d+1 . ⊓⊔

2.3 The Standard Simplex

The standard simplex ∆ in dimension d is the convex hull of the d + 1
points e1, e2, . . . , ed and the origin; here ej is the unit vector (0, . . . , 1, . . . , 0),
with a 1 in the jth position. Figure 2.2 shows ∆ for d = 3. On the other hand,
∆ can also be realized by its hyperplane description, namely

32 2 A Gallery of Discrete Volumes

Fig. 2.2 The standard
simplex ∆ in dimension 3.

x 1

x 2
 x 3
 1

1
 1
 ∆ = {(x1, x2 . . . , xd) ∈ Rd : x1 + x2 + · · · + xd ≤ 1 and all xk ≥ 0} .

In the case of the standard simplex, the dilate t∆ is now given by

t∆ = {(x1, x2, . . . , xd) ∈ Rd : x1 + x2 + · · · + xd ≤ t and all xk ≥ 0
} .

To compute the discrete volume of ∆, we would like to use the methods
developed in Chapter 1, but there is an extra twist. The counting func-
tions in Chapter 1 were deﬁned by equalities, whereas the standard simplex
is deﬁned by an inequality. We are trying to count all integer solutions
(m1, m2, . . . , md) ∈ Z
d
≥0 to

m1 + m2 + · · · + md ≤ t . (2.4)

To translate this inequality in d variables into an equality in d + 1 vari-
ables, we introduce a slack variable md+1 ∈ Z≥0, which picks up the diﬀer-
ence between the right-hand and left-hand sides of (2.4). So the number of
solutions (m1, m2, . . . , md) ∈ Z
d
≥0 to (2.4) equals the number of solutions
(m1, m2, . . . , md+1) ∈ Z
d+1
≥0 to

m1 + m2 + · · · + md+1 = t .

Now the methods of Chapter 1 apply:

2.3 The Standard Simplex 33

# (t∆ ∩ Z
d) = const
 





 ∑

m1≥0 zm1



 

 ∑

m2≥0 zm2
 

 · · ·
 

 ∑

md+1≥0 zmd+1


 z−t




= const ( 1
(1 − z)d+1zt
 ) . (2.5)

In contrast with Chapter 1, we do not require a partial fraction expansion
but simply use the binomial series

1
(1 − z)d+1 = ∑

k≥0
 (
d + k
d
 )zk (2.6)

for d ≥ 0. The constant-term identity (2.5) requires us to ﬁnd the coeﬃcient
of zt in the binomial series (2.6), which is (d+t
d ). Hence the discrete volume
of ∆ is given by L∆(t) = (d+t
d ), a polynomial in the integer variable t of
degree d. Incidentally, the coeﬃcients of this polynomial function in t have an
alternative life in traditional combinatorics:

L∆(t) = 1
d!
 d∑

k=0
(−1)d−k stirl(d + 1, k + 1) tk,

where stirl(n, j) is the Stirling number of the ﬁrst kind (see Exercise 2.11).
We also notice that (2.6) is, by deﬁnition, the Ehrhart series of ∆.
Let’s repeat this computation for the interior ∆
◦ of the standard d-simplex.
Now we introduce a slack variable md+1 > 0, so that strict inequality is forced:

L∆◦ (t) = # {
(m1, m2, . . . , md) ∈ Z
d
>0 : m1 + m2 + · · · + md < t
}

= # {
(m1, m2, . . . , md+1) ∈ Z
d+1
>0 : m1 + m2 + · · · + md+1 = t
} .

Now

L∆◦ (t) = const
 



( ∑

m1>0 zm1 ) ( ∑

m2>0 zm2 )
 · · ·
 

 ∑

md+1>0 zmd+1


 z−t




= const
 (( z
1 − z
 )d+1 z−t)

= const
 

zd+1−t ∑

k≥0
 (
d + k
d
 )
zk


 = (t − 1
d
 ).

It is a fun exercise to prove that

(−1)d(d − t
d
 ) = (t − 1
d
 ) (2.7)

34 2 A Gallery of Discrete Volumes

(see Exercise 2.10). We have arrived at our destination:

Theorem 2.2. Let ∆ be the standard d-simplex.

(a) The lattice-point enumerator of ∆ is the polynomial L∆(t) = (d+t
d ).
(b) Its evaluation at negative integers yields (−1)dL∆(−t) = L∆◦ (t).
(c) The Ehrhart series of ∆ is Ehr∆(z) = 1
(1−z)d+1 . ⊓⊔

2.4 The Bernoulli Polynomials as Lattice-Point
Enumerators of Pyramids

There is a fascinating connection between the Bernoulli polynomials and
certain pyramids over unit cubes. The Bernoulli polynomials Bk(x) are
deﬁned through the generating function

z e
xz

ez − 1 = ∑

k≥0
 Bk(x)
k! zk (2.8)

and are ubiquitous in the study of the Riemann zeta function, among other
objects; they are named after Jacob Bernoulli (1654–1705).4 The Bernoulli
polynomials will play a prominent role in Chapter 12 in the context of Euler–
Maclaurin summation. The ﬁrst few Bernoulli polynomials are

B0(x) = 1 ,

B1(x) = x − 1
2 ,

B2(x) = x2 − x + 1
6 ,

B3(x) = x3 − 3
2 x2 + 1
2 x ,

B4(x) = x4 − 2x3 + x2 − 1
30 ,

B5(x) = x5 − 5
2 x4 + 5
3 x3 − 1
6 x ,

B6(x) = x6 − 3x5 + 5
2 x4 − 1
2 x
2 + 1
42 .

The Bernoulli numbers are Bk := Bk(0) (see also [1, Sequences A000367
& A002445]) and have the generating function

z
ez − 1 = ∑

k≥0
 Bk
k! zk.

4 For more information about Bernoulli, see
http://www-history.mcs.st-and.ac.uk/Mathematicians/Bernoulli Jacob.html.

2.4 The Bernoulli Polynomials as Lattice-Point Enumerators of Pyramids 35

Lemma 2.3. For integers d ≥ 1 and n ≥ 2,

n−1∑

k=0 kd−1 = 1
d (Bd(n) − Bd) .

Proof. We play with the generating function of Bd(n)−Bd
d! :

∑

d≥0
 Bd(n) − Bd
d! zd = z enz − 1
ez − 1 = z
 n−1∑

k=0 ekz = z
 n−1∑

k=0
 ∑

j≥0
 (kz)
j

j!

= ∑

j≥0
 (
n−1∑

k=0 kj) zj+1

j! = ∑

j≥1
 (
n−1∑

k=0 kj−1) zj

(j − 1)! .

Now compare coeﬃcients on both sides. ⊓⊔

Consider a (d − 1)-dimensional unit cube embedded into Rd and form a
d-dimensional pyramid by adjoining one more vertex at (0, 0, . . . , 0, 1), as
depicted in Figure 2.3. More precisely, this geometric object has the following
hyperplane description:

P = {
(x1, x2, . . . , xd) ∈ Rd : 0 ≤ x1, x2, . . . , xd−1 ≤ 1 − xd ≤ 1
} . (2.9)

By deﬁnition, P is contained in the unit d-cube; in fact, its vertices are a
subset of the vertices of the d-cube.

Fig. 2.3 The pyramid P
in dimension 3.

x 1

x 3

x 2
 1

1

1
 We now count lattice points in integer dilates of P. This number equals

# {
(m1, m2, . . . , md) ∈ Z
d : 0 ≤ mk ≤ t − md ≤ t for k = 1, 2, . . . , d − 1
} .

36 2 A Gallery of Discrete Volumes

In this case, we just count the solutions to 0 ≤ mk ≤ t − md ≤ t directly: once
we choose the integer md (between 0 and t), we have t − md + 1 independent
choices for each of the integers m1, m2, . . . , md−1. Hence

LP (t) =
 t∑

md=0 (t − md + 1)d−1 =
 t+1∑

k=1 kd−1 = 1
d (Bd(t + 2) − Bd) , (2.10)

by Lemma 2.3. (Here we need to require d ≥ 2.) This is, naturally, a polynomial
in t.
We now turn our attention to the number of interior lattice points in P:

LP ◦ (t) = # {(m1, m2, . . . , md) ∈ Z
d : 0 < mk < t − md < t
for all k = 1, 2, . . . , d − 1
 } .

By a similar counting argument,

LP ◦ (t) =
 t−1∑

md=1 (t − md − 1)d−1 =
 t−2∑

k=0 kd−1 = 1
d (Bd(t − 1) − Bd) .

Incidentally, the Bernoulli polynomials are known (Exercise 2.15) to have the
symmetry Bd(1 − x) = (−1)dBd(x) . (2.11)

This identity coupled with the fact (Exercise 2.16) that

Bd = 0 for all odd d ≥ 3 (2.12)

gives the relation

LP (−t) = 1
d (Bd(−t + 2) − Bd) = 1
d (Bd (1 − (t − 1)) − Bd)

= (−1)d 1
d (Bd(t − 1) − Bd) = (−1)
d LP ◦ (t) .

Next we compute the Ehrhart series of P. We can actually do this in
somewhat greater generality. Namely, for a polytope Q ⊂ Rd−1 with vertices
v1, v2, . . . , vm, deﬁne Pyr(Q), the pyramid over Q, as the convex hull of
(v1, 0) , (v2, 0) , . . . , (vm, 0) , (0, . . . , 0, 1) in Rd. In our example above, the d-
polytope P is equal to Pyr(2) for the unit (d − 1)-cube 2. The number of
integer points in t Pyr(Q) is, by construction,

LPyr(Q)(t) = 1 + LQ(1) + LQ(2) + · · · + LQ(t) = 1 +
 t∑

j=1 LQ(j) ,

because in t Pyr(Q), there is one lattice point with xd-coordinate t, we have
LQ(1) lattice points with xd-coordinate t − 1, there are LQ(2) lattice points

2.4 The Bernoulli Polynomials as Lattice-Point Enumerators of Pyramids 37

with xd-coordinate t−2, etc., up to LQ(t) lattice points with xd = 0. Figure 2.4
shows an instance for a pyramid over a square.

Fig. 2.4 Counting the
lattice points in t Pyr(Q).

x 1

x 3

x 2
 t

t

t t Q
 This identity for LPyr(Q)(t) allows us to compute the Ehrhart series of
Pyr(Q) from the Ehrhart series of Q:

Theorem 2.4. EhrPyr(Q)(z) = EhrQ(z)
1 − z .

Proof.

EhrPyr(Q)(z) = 1 + ∑

t≥1 LPyr(Q)(t) zt = 1 + ∑

t≥1
 

1 +
 t∑

j=1 LQ(j)


 zt

= ∑

t≥0 zt + ∑

t≥1
 t∑

j=1 LQ(j) zt = 1
1 − z + ∑

j≥1 LQ(j) ∑

t≥j zt

= 1
1 − z + ∑

j≥1 LQ(j) zj

1 − z = 1 + ∑j≥1 LQ(j) zj

1 − z . ⊓⊔

Our pyramid P that began this section is a pyramid over the unit (d − 1)-
cube, and so

EhrP (z) = 1
1 − z
 ∑d−1
k=1 A (d − 1, k) zk−1

(1 − z)d = ∑d−1
k=1 A (d − 1, k) zk−1

(1 − z)d+1 . (2.13)

Let’s summarize what we have proved for the pyramid over the unit cube.

38 2 A Gallery of Discrete Volumes

Theorem 2.5. Given d ≥ 2, let P be the d-pyramid

P = {(x1, x2, . . . , xd) ∈ Rd : 0 ≤ x1, x2, . . . , xd−1 ≤ 1 − xd ≤ 1} .

(a) The lattice-point enumerator of P is the polynomial

LP (t) = 1
d (Bd(t + 2) − Bd) .

(b) Its evaluation at negative integers yields (−1)dLP (−t) = LP ◦ (t).

(c) The Ehrhart series of P is EhrP (z) =
 ∑d−1
k=1 A(d−1,k)zk−1

(1−z)d+1 . ⊓⊔

Patterns are emerging. . .

2.5 The Lattice-Point Enumerators of the
Cross-Polytopes

Consider the cross-polytope 3 in Rd given by the hyperplane description

3 := {(x1, x2, . . . , xd) ∈ Rd : |x1| + |x2| + · · · + |xd| ≤ 1} . (2.14)

Figure 2.5 shows the 3-dimensional instance of 3, an octahedron. The vertices
of 3 are (±1, 0, . . . , 0) , (0, ±1, 0, . . . , 0) , . . . , (0, . . . , 0, ±1).

Fig. 2.5 The cross-
polytope 3 in dimension 3.

x 1

x 2

x 3
 1

1

1
 To compute the discrete volume of 3, we use a process similar to that of
Section 2.4. Namely, for a (d − 1)-polytope Q with vertices v1, v2, . . . , vm

2.5 The Lattice-Point Enumerators of the Cross-Polytopes 39

such that the origin is in Q, we deﬁne BiPyr(Q), the bipyramid over Q, as
the convex hull of

(v1, 0) , (v2, 0) , . . . , (vm, 0) , (0, . . . , 0, 1) , and (0, . . . , 0, −1) .

In our example above, the d-dimensional cross-polytope is the bipyramid
over the (d − 1)-dimensional cross-polytope. The number of integer points in
t BiPyr(Q) is, by construction,

LBiPyr(Q)(t) = 2 + 2LQ(1) + 2LQ(2) + · · · + 2LQ(t − 1) + LQ(t)

= 2 + 2
 t−1∑

j=1 LQ(j) + LQ(t) .

This identity allows us to compute the Ehrhart series of BiPyr(Q) from the
Ehrhart series of Q, in a manner similar to the proof of Theorem 2.4. We
leave the proof of the following result as Exercise 2.23.

Theorem 2.6. If Q contains the origin, then EhrBiPyr(Q)(z) = 1+z
1−z EhrQ(z).
⊓⊔

This theorem allows us to compute the Ehrhart series of 3 eﬀortlessly:
The cross-polytope 3 in dimension 0 is the origin, with Ehrhart series 1
1−z .
The higher-dimensional cross-polytopes can be computed recursively through
Theorem 2.6 as
 Ehr3(z) = (1 + z)d

(1 − z)d+1 .

Since Ehr3(z) = 1 + ∑

t≥1 L3(t) zt, we can retrieve L3(t) by expanding
Ehr3(z) into its power series at z = 0:

Ehr3(z) = (1 + z)
d

(1 − z)d+1 = ∑d
k=0 (d
k)zk

(1 − z)d+1

=
 d∑

k=0
 (d
k
)zk ∑

t≥0
 (t + d
d
 )zt =
 d∑

k=0
 (d
k
) ∑

t≥k
 (t − k + d
d
 )zt

=
 d∑

k=0
 (d
k
) ∑

t≥0
 (t − k + d
d
 )zt.

In the last step, we used the fact that (t−k+d
d ) = 0 for 0 ≤ t < k. But then

1 + ∑

t≥1 L3(t) zt = ∑

t≥0
 d∑

k=0
 (d
k
)(t − k + d
d
 )
zt,

and hence L3(t) = ∑d
k=0 (d
k)(t−k+d
d ) for all t ≥ 1.

40 2 A Gallery of Discrete Volumes

We ﬁnish this section by counting the interior lattice points in t3. We
begin by noticing, since t is an integer, that

L3◦ (t) = # {(m1, m2, . . . , md) ∈ Z
d : |m1| + |m2| + · · · + |md| < t
}

= # {(m1, m2, . . . , md) ∈ Z
d : |m1| + |m2| + · · · + |md| ≤ t − 1
}

= L3(t − 1) .

On the other hand, we can use (2.7):

L3(−t) =
 d∑

k=0
 (d
k
)(−t − k + d
d
 )

=
 d∑

k=0
 (d
k
)(−1)d(t − 1 + k
d
 )

= (−1)d d∑

k=0
 ( d
d − k
)(t − 1 + d − k
d
 )

= (−1)dL3(t − 1) .

Comparing the last two computations, we see that (−1)dL3(−t) = L3◦(t).
Let’s summarize:

Theorem 2.7. Let 3 be the cross-polytope in Rd.

(a) The lattice-point enumerator of 3 is the polynomial

L3(t) =
 d∑

k=0
 (d
k
)(t − k + d
d
 ).

(b) Its evaluation at negative integers yields (−1)dL3(−t) = L3◦ (t).
(c) The Ehrhart series of P is Ehr3(z) = (1+z)
d

(1−z)d+1 . ⊓⊔

2.6 Pick’s Theorem

Returning to basic concepts, we now give a complete account of LP for all
integral convex polygons P in R2. Denote the number of integer points inside
the polygon P by I, and the number of integer points on the boundary of P
by B. The following result, called Pick’s theorem in honor of its discoverer
Georg Alexander Pick (1859–1942), presents the astonishing fact that the
area A of P can be computed simply by counting lattice points:

2.6 Pick’s Theorem 41

Theorem 2.8 (Pick’s theorem). For an integral convex polygon,

A = I + 1
2 B − 1 .

Proof. We begin by proving that Pick’s identity has an additive character:
we can decompose P into the union of two integral polygons P1 and P2 by
joining two vertices of P with a line segment, as shown in Figure 2.6.

Fig. 2.6 Decomposition of
a polygon into two.

P 1
 P 2
 We claim that the validity of Pick’s identity for P follows from the validity
of Pick’s identity for P1 and P2. Denote the area, number of interior lattice
points, and number of boundary lattice points of Pk by Ak, Ik, and Bk,
respectively, for k = 1, 2. Clearly,

A = A1 + A2 .

Furthermore, if we denote the number of lattice points on the edge common
to P1 and P2 by L, then

I = I1 + I2 + L − 2 and B = B1 + B2 − 2L + 2 .

Thus
 I + 1
2 B − 1 = I1 + I2 + L − 2 + 1
2 B1 + 1
2 B2 − L + 1 − 1

= I1 + 1
2 B1 − 1 + I2 + 1
2 B2 − 1 .

This proves the claim. Note that our proof also shows that the validity of
Pick’s identity for P1 follows from the validity of Pick’s identity for P and P2.
Now, every convex polygon can be decomposed into triangles that share a
common vertex, as illustrated in Figure 2.7. Hence it suﬃces to prove Pick’s
theorem for triangles. Further simplifying the picture, we can embed every
integral triangle into an integral rectangle, as suggested by Figure 2.8.
This reduces the proof of Pick’s theorem to proving the theorem for integral
rectangles whose edges are parallel to the coordinate axes, and for rectangular

42 2 A Gallery of Discrete Volumes

Fig. 2.7 Triangulation of
a polygon.

triangles two of whose edges are parallel to the coordinate axes. These two
cases are left to the reader as Exercise 2.25. ⊓⊔

Fig. 2.8 Embedding a
triangle in a rectangle.

Pick’s theorem allows us to count not only the lattice points strictly inside
the polygon P, but also the total number of lattice points contained in P,
because this number is

I + B = A − 1
2 B + 1 + B = A + 1
2 B + 1 . (2.15)

From this identity, it is now easy to describe the lattice-point enumerator LP :

Theorem 2.9. Suppose P is an integral convex polygon with area A and B
lattice points on its boundary.

(a) The lattice-point enumerator of P is the polynomial

LP (t) = A t
2 + 1
2 B t + 1 .

(b) Its evaluation at negative integers yields the relation

LP (−t) = LP ◦ (t) .

(c) The Ehrhart series of P is

EhrP (z) =
 (A − B
2 + 1) z2 + (A + B
2 − 2
) z + 1
(1 − z)3 .

2.7 Polygons with Rational Vertices 43

Note that in the numerator of the Ehrhart series, the coeﬃcient of z2 is
LP ◦ (1), and the coeﬃcient of z is LP (1) − 3.

Proof. Statement (a) will follow from (2.15) if we can prove that the area of
tP is At2 and that the number of boundary points on tP is Bt, which is the
content of Exercise 2.26. Statement (b) follows with LP ◦(t) = LP (t) − Bt.
Finally, the Ehrhart series is

EhrP (z) = 1 + ∑

t≥1 LP (t) zt

= ∑

t≥0
 (A t
2 + B
2 t + 1) zt

= A z2 + z
(1 − z)3 + B
2 z
(1 − z)2 + 1
1 − z

=
 (A − B
2 + 1) z2 + (A + B
2 − 2) z + 1
(1 − z)3 . ⊓⊔

2.7 Polygons with Rational Vertices

In this section we will establish formulas for the number of integer points in a
rational convex polygon and its integral dilates.
A natural ﬁrst step is to ﬁx a triangulation of the polygon P, which reduces
our problem to that of counting integer points in rational triangles. However,
this procedure merits some remarks. After counting lattice points in the
triangles, we need to reassemble the triangles to form the polygon. But then
we need to take care of the overcounting on line segments (where the triangles
meet). Computing the number of lattice points on rational line segments is
considerably easier than enumerating lattice points in 2-dimensional regions;
however, it is still nontrivial (see Theorem 1.5).
After triangulating P, we can further simplify the picture by embedding an
arbitrary rational triangle in a rational rectangle, as in Figure 2.8. To compute
lattice points in a triangle, we can ﬁrst count the points in a rectangle with
edges parallel to the coordinate axes, and then subtract the number of points
in three right triangles, each with two edges are parallel to the axes, and
possibly another rectangle, as shown in Figure 2.8. Since rectangles are easy
to deal with (see Exercise 2.2), the problem reduces to ﬁnding a formula for a
right triangle two of whose edges are parallel to the coordinate axes.
We now adjust and expand our generating-function machinery to these
right triangles. Such a triangle T is a subset of R2 consisting of all points
(x, y) satisfying
 x ≥ a
d , y ≥ b
d , ex + f y ≤ r

44 2 A Gallery of Discrete Volumes

for some integers a, b, d, e, f, r (with ea + f b ≤ rd; otherwise, the triangle
would be empty). Because the lattice-point count is invariant under horizontal
and vertical integer translations and under ﬂipping about the x- or y-axis,
we may assume that a, b, d, e, f, r ≥ 0 and a, b < d. (One should meditate
about this fact for a minute.) Thus we arrive at the triangle T depicted in
Figure 2.9.
 x

y
  a
d ; b
d
   r   f b=d
e ; b
d
 

 a
d ; r   ea=d
f
 
 Fig. 2.9 A right rational triangle.

To make our life a little easier, let’s assume for the moment that e and f
are relatively prime; we will deal with the general case in the exercises. So let

T = {(x, y) ∈ R2 : x ≥ a
d , y ≥ b
d , ex + f y ≤ r} . (2.16)

To derive a formula for

LT (t) = # {(m, n) ∈ Z
2 : m ≥ ta
d , n ≥ tb
d , em + f n ≤ tr} ,

we want to use methods similar to those in Chapter 1. As in Section 2.3, we
introduce a slack variable s:

LT (t) = # {(m, n) ∈ Z
2 : m ≥ ta
d , n ≥ tb
d , em + f n ≤ tr}

= # {(m, n, s) ∈ Z
3 : m ≥ ta
d , n ≥ tb
d , s ≥ 0, em + f n + s = tr} .

This counting function can now, as earlier, be interpreted as the coeﬃcient of
ztr in the function

2.7 Polygons with Rational Vertices 45


 ∑

m≥ ta
d
 zem



 

 ∑

n≥ tb
d
 zf n



 

∑

s≥0 zs


 .

Here the subscript (e.g., m ≥ ta
d ) under a summation sign means sum over
all integers satisfying this condition. For example, in the ﬁrst sum, we begin
with the least integer greater than or equal to ta
d , which is denoted by ⌈ ta
d ⌉

(and is equal to ⌊ ta−1
d ⌋ + 1 by Exercise 1.4(j)). Hence the above generating
function can be rewritten as



 ∑

m≥⌈ ta
d ⌉ zem




 


 ∑

n≥⌈ tb
d ⌉ zf n




 


∑

s≥0 zs


 = z⌈ ta
d ⌉e

1 − ze z⌈ tb
d ⌉f

1 − zf 1
1 − z

= zu+v

(1 − ze) (1 − zf ) (1 − z) ,

(2.17)

where we have introduced, for ease of notation,

u := ⌈ ta
d
 ⌉ e and v := ⌈ tb
d
 ⌉ f . (2.18)

To extract the coeﬃcient of ztr of our generating function (2.17), we use
familiar methods. As usual, we shift this coeﬃcient to a constant term:

LT (t) = const ( zu+v−tr

(1 − ze) (1 − zf ) (1 − z)
 )

= const ( 1
(1 − ze) (1 − zf ) (1 − z)ztr−u−v
 ) .

Before we apply the partial fraction machinery to this function, we should
make sure that it is indeed a proper rational function, that is, that the total
degree satisﬁes u + v − tr − e − f − 1 < 0 (2.19)

(see Exercise 2.33). Then we expand into partial fractions (here we are using
our assumption that e and f do not have any common factors):

1
(1 − ze) (1 − zf ) (1 − z)ztr−u−v

=
 e−1∑

j=1
 Aj
z − ξj
e +
 f −1∑

j=1
 Bj
z − ξj
f +
 3∑

k=1
 Ck
(z − 1)k +
 tr−u−v∑

k=1
 Dk
zk . (2.20)

As we have seen numerous times before, the coeﬃcients Dk do not contribute
to the constant term, so that we obtain

46 2 A Gallery of Discrete Volumes

LT (t) = −
 e−1∑

j=1
 Aj
ξj
e −
 f −1∑

l=1
 Bl
ξl
f − C1 + C2 − C3 . (2.21)

We invite the reader to compute the coeﬃcients appearing in this formula
(Exercise 2.34):

Aj = − ξj(v−tr+1)
e

e (1 − ξjf
e ) (1 − ξj
e) ,

Bl = − ξl(u−tr+1)
f

f (1 − ξle
f ) (1 − ξl
f ) ,

C1 = − (u + v − tr)
2

2ef + u + v − tr
2
 (
− 1
ef + 1
e + 1
f
 ) + 1
4
 ( 1
e + 1
f − 1
)

− 1
12
 ( e
f + 1
ef + f
e
 ) , (2.22)

C2 = − u + v − tr + 1
ef + 1
2e + 1
2f ,

C3 = − 1
ef .

Putting these ingredients into (2.21) yields the following formula for our
lattice-point count.

Theorem 2.10. For the rectangular rational triangle T given by (2.16), where
e and f are relatively prime,

LT (t) = 1
2ef (tr − u − v)
2 + 1
2 (tr − u − v) ( 1
e + 1
f + 1
ef
 )

+ 1
4
 (
1 + 1
e + 1
f
 ) + 1
12
 ( e
f + f
e + 1
ef
 )

+ 1
e
 e−1∑

j=1
 ξj(v−tr)
e(1 − ξjf
e ) (
1 − ξj
e) + 1
f
 f −1∑

l=1
 ξl(u−tr)
f(1 − ξle
f ) (
1 − ξl
f ) . ⊓⊔

This identity can be rephrased in terms of the Fourier–Dedekind sum that
we introduced in (1.13):

LT (t) = 1
2ef (tr − u − v)
2 + 1
2 (tr − u − v) ( 1
e + 1
f + 1
ef
 )

+ 1
4
 (1 + 1
e + 1
f
 ) + 1
12
 ( e
f + f
e + 1
ef
 )

+ sv−tr(f, 1; e) + su−tr(e, 1; f ) .

2.7 Polygons with Rational Vertices 47

The general formula for LT —not assuming that e and f are relatively
prime—is the content of Exercise 2.36.
Let’s pause for a moment and study the nature of LT as a function of t.
Aside from the last two ﬁnite sums (which will be put in the spotlight in
Chapter 8) and the appearance of u and v, the function LT is a quadratic
polynomial in t. And in those two sums, t appears only in the exponent of
roots of unity, namely as the exponent of ξe and ξf . As a function of t, ξt
e is
periodic with period e, and similarly, ξt
f is periodic with period f . We should
also remember that u and v are functions of t; but they can be easily written
in terms of the fractional-part function, which again gives rise to periodic
functions in t. So LT (t) is a (quadratic) “polynomial” in t, whose coeﬃcients
are periodic functions in t. This is reminiscent of the counting functions of
Chapter 1, which showed a similar periodic-polynomial behavior. Inspired by
both examples, we deﬁne a quasipolynomial Q as an expression of the form

Q(t) = cn(t) tn + · · · + c1(t) t + c0(t) ,

where c0, . . . , cn are periodic functions in t. The degree of Q is n,5 and
the least common period of c0, . . . , cn is the period of Q. Alternatively,
for a quasipolynomial Q, there exist a positive integer k and polynomials
p0, p1, . . . , pk−1 such that

Q(t) =
 




p0(t) if t ≡ 0 mod k,
p1(t) if t ≡ 1 mod k,
...
pk−1(t) if t ≡ k − 1 mod k.

The minimal such k is the period of Q, and for this minimal k, the polynomials
p0, p1, . . . , pk−1 are the constituents of Q.
By the triangulation and embedding-in-a-box arguments that began this
section, we can now state a general structural result for rational polygons.

Theorem 2.11. Let P be any rational polygon. Then LP (t) is a quasipolyno-
mial of degree 2. Its leading coeﬃcient is the area of P (in particular, it is a
constant).

We have the technology at this point to study the period of LP ; we let the
reader enjoy the ensuing details (see Exercise 2.37).

Proof. By Exercises 2.2 and 2.36 (the general form of Theorem 2.10), the
theorem holds for rational rectangles and right triangles whose edges are
parallel to the axes. Now use the additivity of both degree-2 quasipolynomials
and areas along with Theorem 1.5. ⊓⊔

5 Here we tacitly assume that cn is not the zero function.

48 2 A Gallery of Discrete Volumes

2.8 Euler’s Generating Function for General Rational
Polytopes

By now, we have computed several instances of counting functions by setting
up a generating function that ﬁts the particular problem in which we are
interested. In this section, we set up such a generating function for the lattice-
point enumerator of an arbitrary rational polytope. Such a polytope is given
by its hyperplane description as an intersection of half-spaces and hyperplanes.
The half-spaces are algebraically given by linear inequalities, the hyperplanes
by linear equations. If the polytope is rational, we can choose the coeﬃcients
of these inequalities and equations to be integers (Exercise 2.7). To unify
both descriptions, we can introduce slack variables to turn the half-space
inequalities into equalities. Furthermore, by translating our polytope into the
nonnegative orthant (we can always shift a polytope by an integer vector
without changing the lattice-point count), we may assume that all points in
the polytope have nonnegative coordinates. In summary, after a harmless
integer translation, we can describe every rational polytope P as

P = {
x ∈ Rd
≥0 : A x = b
} (2.23)

for some integral matrix A ∈ Z
m×d and some integer vector b ∈ Z
m. (Note
that d is not necessarily the dimension of P.) To describe the t
th dilate of P,
we simply scale a point x ∈ P by 1
t , or alternatively, multiply b by t:

tP = {
x ∈ Rd
≥0 : A x
t = b
} = {x ∈ Rd
≥0 : A x = tb
} .

Hence the lattice-point enumerator of P is the counting function

LP (t) = # {x ∈ Z
d
≥0 : A x = tb
} . (2.24)

Example 2.12. Suppose P is the quadrilateral with vertices (0, 0), (2, 0),
(1, 1), and (0, 3
2 ) pictured in Figure 2.10. The half-space-inequality description
of P is
 P = {(x1, x2) ∈ R2 : x1, x2 ≥ 0, x1 + 2x2 ≤ 3,
x1 + x2 ≤ 2
 } .

Thus,

LP (t) = # {(x1, x2) ∈ Z
2 : x1, x2 ≥ 0, x1 + 2x2 ≤ 3t,
x1 + x2 ≤ 2t
 }

= # {(x1, x2, x3, x4) ∈ Z
4 : x1, x2, x3, x4 ≥ 0, x1 + 2x2 + x3 = 3t,
x1 + x2 + x4 = 2t
 }

= # {x ∈ Z
4
≥0 : ( 1 2 1 0
1 1 0 1
 ) x = ( 3t
2t
 )} .

2.8 Euler’s Generating Function for General Rational Polytopes 49

Fig. 2.10 The quadrilat-
eral P from Example 2.12.

(0 ; 0) (2 ; 0)

(1 ; 1)
(0 ; 32 )
 x 1

x 2
 Using the ideas from Sections 1.3, 1.5, 2.3, and 2.7, we now construct a
generating function for this counting function. In those previous sections, the
lattice-point enumerator could be described with only one nontrivial linear
equation, whereas now we have a system of such linear constraints. However,
we can use the same approach of encoding the linear equation into geometric
series; we just need more than one variable. When we expand the function

f (z1, z2) := 1
(1 − z1z2) (1 − z2
1z2) (1 − z1) (1 − z2) z3t
1 z2t
2

into geometric series,

f (z1, z2) =

=
 ( ∑

n1≥0 (z1z2)n1 )( ∑

n2≥0
 (z2
1z2)n2 )( ∑

n3≥0 zn3
1
 )( ∑

n4≥0 zn4
2
 ) 1
z3t
1 z2t
2

= ∑

n1,...,n4≥0 zn1+2n2+n3−3t
1 zn1+n2+n4−2t
2 .

When we compute the constant term (in both z1 and z2), we are counting
solutions (n1, n2, n3, n4) ∈ Z
4
≥0 to

( 1 2 1 0
1 1 0 1
 ) 




 n1
n2
n3
n4
 



 = ( 3t
2t
 ) ,

that is, the constant term of f (z1, z2) counts the integer points in P:

LP (t) = const 1
(1 − z1z2) (1 − z2
1z2) (1 − z1) (1 − z2) z3t
1 z2t
2 .

50 2 A Gallery of Discrete Volumes

We invite the reader to actually compute this constant term (Exercise 2.38).
It turns out to be 7
4 t2 + 5
2 t + 7 + (−1)t

8 . ⊓⊔

Returning to the general case of a polytope P given by (2.23), we denote
the columns of A by c1, c2, . . . , cd. Let z = (z1, z2, . . . , zm) and expand the
function 1
(1 − zc1 ) (1 − zc2) · · · (1 − zcd ) ztb (2.25)

in terms of geometric series:


 ∑

n1≥0 zn1c1



 

 ∑

n2≥0 zn2c2


 · · ·
 

 ∑

nd≥0 zndcd
 

 1
ztb .

Here we use the abbreviating notation za := za1
1 za2
2 · · · zam
m for the vectors
z = (z1, z2, . . . , zm) ∈ Cm and a = (a1, a2, . . . , am) ∈ Z
m. In multiplying out
everything, a typical exponent will look like

n1c1 + n2c2 + · · · + ndcd − tb = An − tb ,

where n = (n1, n2, . . . , nd) ∈ Z
d
≥0. That is, if we take the constant term of our
generating function (2.25), we are counting integer vectors n ∈ Z
d
≥0 satisfying

An − tb = 0 , that is, An = tb .

So this constant term will pick up exactly the number of lattice points n ∈ Z
d
≥0
in tP:

Theorem 2.13 (Euler’s generating function). Suppose the rational poly-
tope P is given by (2.23). Then the lattice-point enumerator of P can be
computed as follows:

LP (t) = const ( 1
(1 − zc1) (1 − zc2 ) · · · (1 − zcd ) ztb
 ) . ⊓⊔

We ﬁnish this section with rephrasing this constant-term identity in terms
of Ehrhart series.

Corollary 2.14. Suppose the rational polytope P is given by (2.23). Then
the Ehrhart series of P can be computed as

EhrP (x) = const
 ( 1
(1 − zc1) (1 − zc2) · · · (1 − zcd ) (1 − x
zb )
 )
 .

Proof. By Theorem 2.13,

Notes 51

EhrP (x) = ∑

t≥0 const ( 1
(1 − zc1) (1 − zc2 ) · · · (1 − zcd ) ztb
 ) xt

= const
 

 1
(1 − zc1 ) (1 − zc2) · · · (1 − zcd )
 ∑

t≥0
 xt

ztb
 



= const ( 1
(1 − zc1) (1 − zc2 ) · · · (1 − zcd ) 1
1 − x
zb
 ) . ⊓⊔

Notes

1. Convex polytopes are beautiful objects with a rich history and interesting
theory, which we have only glimpsed here. For good introductions to poly-
topes, we recommend [69,127,259]. Polytopes appear in a vast range of current
research areas, including Gr¨obner bases and commutative algebra [237], com-
binatorial optimization [96, 214], integral geometry [150], K-theory [74], and
geometry of numbers [221].

2. The distinction between the vertex and hyperplane description of a convex
polytope leads to an interesting algorithmic question; namely, how quickly can
we retrieve the ﬁrst piece of data from the second and vice versa [214, 259]?

3. Ehrhart series are named after Eug`ene Ehrhart (1906–2000),
6 who proved
the main structure theorems which we will see in Chapter 3. The Ehrhart
series of a polytope is an example of a Hilbert–Poincar´e series. These series
appear in the study of graded algebras (see, for example, [135, 230]); in the
Ehrhart case, this algebra lives in C[z±1
1 , z±1
2 , . . . , z±1
d , zd+1] and is generated
by the monomials zm, where m ranges over all integer points in cone(P), the
cone over P, which we will deﬁne in Chapter 3. Ehrhart series also appear in
the context of toric varieties, a vast and fruitful subject [92, 117].

4. The Eulerian numbers A (d, k) are named after Leonhard Euler (1707–
1783)7 and arise naturally in the statistics of permutations: A (d, k) counts
permutations of {1, 2, . . . , d} with k − 1 ascents. For more on A (d, k), see [88,
Section 6.5] and [140]; for more connections between A (d, k) and Ehrhart
theory, see [33].

5. The pyramids of Section 2.4 have an interpretation as order polytopes [231].
A curious fact about the lattice-point enumerators of these pyramids is that
they have arbitrarily large real roots as the dimension grows [37].

6 For more information about Ehrhart, see http://icps.u-strasbg.fr/∼clauss/Ehrhart.html.
7 For more information about Euler, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Euler.html.

52 2 A Gallery of Discrete Volumes

6. The counting function L3 for the cross-polytope can, incidentally, also be
written as min(d,t)∑

k=0 2
k(d
k
)(t
k
).

In particular, L3 is symmetric in d and t. The cross-polytope counting
functions bear a connection to Laguerre polynomials, the d-dimensional
harmonic oscillator, and the Riemann hypothesis. This connection appeared
in [76], where Daniel Bump, Kwok–Kwong Choi, P¨ar Kurlberg, and Jeﬀrey
Vaaler also found a curious fact about the roots of the polynomials L3: they
all have real part − 1
2 (an instance of a local Riemann hypothesis). This fact
was proved independently by Peter Kirschenhofer, Attila Peth˝o, and Robert
Tichy [149]; see also the notes in Chapter 4.

7. Theorem 2.8 marks the beginning of the general study of lattice-point
enumeration in polytopes. Its amazingly simple statement was discovered
by Georg Alexander Pick (1859–1942)8 in 1899 [191]. Pick’s theorem holds
also for a nonconvex polygon, provided its boundary forms a simple curve.
In Chapter 14, we prove a generalization of Pick’s theorem that includes
nonconvex curves.

8. The results of Section 2.7 appeared in [44]. We will see in Chapter 8 that
the ﬁnite sums over roots of unity can be rephrased in terms of Dedekind–
Rademacher sums, which—as we will also see in Chapter 8—can be computed
very quickly. The theorems of Section 2.7 will then imply that the discrete
volume of every rational polygon can be computed eﬃciently.

9. If we replace tb in (2.24) by a variable integer vector v, the counting
function f (v) = # {x ∈ Z
d
≥0 : A x = v}

is called a vector partition function: it counts partitions of the vector v in
terms of the columns of A. Vector partition functions are the multivariate
analogues of our lattice-point enumerators LP (t). They have many interesting
properties and give rise to intriguing open questions [31, 59, 91, 236, 241].

10. While Leonhard Euler most likely did not think of lattice-point enumer-
ation in the sense of Ehrhart, we attribute Theorem 2.13 to him, since he
certainly worked with generating functions of this type, probably thinking of
them as vector partition functions. Percy MacMahon (1854–1929)
9 developed
powerful machinery for manipulating multivariate generating functions [168];
his viewpoint and motivation came from integer partitions, but his work

8 For more information about Pick, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Pick.html.
9 For more information about MacMahon, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/MacMahon.html.

Exercises 53

can be applied to more general linear-constraint settings, such as vector
partition functions. The potential of Euler’s generating function for Ehrhart
polynomials was already realized by Ehrhart [110, 112]. Several modern ap-
proaches to computing Ehrhart polynomials are based on Theorem 2.13 (see,
for example, [30, 68, 160]).

Exercises

2.1. ♣ Fix positive integers a, b, c, d such that gcd(a, b) = gcd(c, d) = 1 and
a
b < c
d , and let P be the interval [ a
b , c
d ] (so P is a 1-dimensional rational
convex polytope). Compute LP (t) = # (tP ∩ Z) and LP ◦ (t) and show directly
that LP (t) and LP ◦ (t) are quasipolynomials with period lcm(b, d) that satisfy

LP ◦ (−t) = −LP (t) .

(Hint: Exercise 1.4(i).)

2.2. ♣ Fix positive rational numbers a1, b1, a2, b2 and let R be the rectan-
gle with vertices (a1, b1), (a2, b1), (a2, b2), and (a1, b2). Compute LR(t) and
EhrR(z).

2.3. Fix positive integers a and b, and let T be a triangle with vertices (0, 0),
(a, 0), and (0, b).

(a) Compute LT (t) and EhrT (z).
(b) Use (a) to derive the following formula for the greatest common divisor of
a and b:
 gcd(a, b) = 2
 b−1∑

k=1
 ⌊ ka
b
 ⌋ + a + b − ab .

(Hint: Exercise 1.12.)

2.4. Prove that for two polytopes P ⊂ Rm and Q ⊂ Rn,

# ((P × Q) ∩ Z
m+n) = # (P ∩ Z
m) · # (Q ∩ Z
n) .

Hence, LP×Q(t) = LP (t) LQ(t).

2.5. Prove that if F is a face of P and G is a face of F, then G is also a face
of P. (That is, the face relation is transitive.)

2.6. ♣ Suppose ∆ is a d-simplex with vertices V = {v1, v2, . . . , vd+1}. Prove
that for every nonempty subset W ⊆ V , conv W is a face of ∆, and conversely,
that every face of ∆ is of the form conv W for some W ⊆ V . Conclude the
following corollaries from this characterization of the faces of a simplex:

(a) A face of a simplex is again a simplex.

54 2 A Gallery of Discrete Volumes

(b) The intersection of two faces of a simplex ∆ is again a face of ∆.

2.7. ♣ Prove that a rational convex polytope can be described by a system
of linear inequalities and equations with integral coeﬃcients.

2.8. ♣ Prove the properties (2.3) of the Eulerian numbers for all integers
1 ≤ k ≤ d, namely:

(a) A (d, k) = A (d, d + 1 − k)
(b) A (d, k) = (d − k + 1) A (d − 1, k − 1) + k A (d − 1, k)

(c)
 d∑

k=0 A (d, k) = d!

(d) A (d, k) =
 k∑

j=0(−1)j(
d + 1
j
 )
(k − j)d.

2.9. ♣ Prove (2.6); namely, for d ≥ 0, 1
(1−z)d+1 = ∑

k≥0 (d+k
d )zk.

2.10. ♣ Prove (2.7): For t, k ∈ Z and d ∈ Z>0,

(−1)d(−t + k
d
 ) = (t + d − 1 − k
d
 )
.

2.11. The Stirling numbers of the ﬁrst kind, stirl(n, m), are deﬁned
through the ﬁnite generating function

x(x − 1) · · · (x − n + 1) =
 n∑

m=0 stirl(n, m) xm.

(See also [1, Sequence A008275].) Prove that

1
d!
 d∑

k=0
(−1)d−k stirl(d + 1, k + 1) tk = (d + t
d
 ),

the lattice-point enumerator for the standard d-simplex.

2.12. Give a direct proof that the number of solutions (m1, m2, . . . , md+1) ∈
Z
d+1
≥0 to m1 + m2 + · · · + md+1 = t equals (d+t
d ). (Hint: think of t objects lined
up and separated by d walls.)

2.13. Compute LP (t), where P is the regular tetrahedron with vertices
(0, 0, 0) , (1, 1, 0) , (1, 0, 1) , (0, 1, 1).

2.14. ♣ Prove that the power series

∑

k≥0
 Bk
k! zk

that deﬁnes the Bernoulli numbers has radius of convergence 2π.

Exercises 55

2.15. ♣ Prove (2.11); namely, Bd(1 − x) = (−1)
dBd(x).

2.16. ♣ Prove (2.12); namely, Bd = 0 for all odd d ≥ 3.

2.17. Show that for each positive integer n,

n x
n−1 =
 n∑

k=1
 (n
k
)Bn−k(x) .

This gives us a change of basis for the polynomials of degree ≤ n, allowing us
to represent every polynomial as a sum of Bernoulli polynomials.

2.18. As a complement to the previous exercise, show that we also have a
change of basis in the other direction. Namely, we can represent a single
Bernoulli polynomial in terms of the monomials as follows:

Bn(x) =
 n∑

k=0
 (
n
k
)Bk xn−k.

2.19. Show that for all positive integers m, n and for all x ∈ R,

1
m
 m−1∑

k=0 Bn
 (
x + k
m
 ) = m−nBn(mx) .

(This is a Hecke-operator -type identity, originally found by Joseph Ludwig
Raabe in 1851.)

2.20. Show that Bn(x + 1) − Bn(x) = n x
n−1.

2.21. An alternative way to deﬁne the Bernoulli polynomials is to give ele-
mentary properties that uniquely characterize them. Show that the following
three properties uniquely determine the Bernoulli polynomials, as deﬁned in
the text by (2.8):

(a) B0(x) = 1.
(b) dBn(x)
dx = n Bn−1(x), for all n ≥ 1.
(c) ∫ 1
0 Bn(x) dx = 0, for all n ≥ 1.

2.22. Use (2.13) to derive the following identity, which expresses a Bernoulli
polynomial in terms of Eulerian numbers and binomial coeﬃcients:

1
d (Bd(t + 2) − Bd) = A (d − 1, d − 1) (t + d − 2
d
 )

+ A (d − 1, d − 2) (t + d − 3
d
 ) + · · · + A (d − 1, 1) (t
d

) .

2.23. ♣ Prove Theorem 2.6: EhrBiPyr(Q)(z) = 1+z
1−z EhrQ(z).

56 2 A Gallery of Discrete Volumes

2.24. A Delannoy path is a path through lattice points in the plane with
steps (1, 0), (0, 1), and (1, 1) (i.e., “east,” “north,” and “northeast”). Find a
recurrence for the number D(m, n) of Delannoy paths from the origin to the
point (m, n), and use it to compute the two-variable generating function

∑

m≥0
 ∑

n≥0 D(m, n) zmwn = 1
1 − z − w − zw .

Conclude from this generating function that the Ehrhart polynomial L3(t)
of the d-dimensional cross-polytope equals D(t, d). (Hint: start with the d
th

derivative of the generating function of D(t, d) with respect to w.)

2.25. ♣ Let R be an integral rectangle whose edges are parallel to the
coordinate axes, and let T be a rectangular triangle two of whose edges are
parallel to the coordinate axes. Show that Pick’s theorem holds for R and T .

2.26. ♣ Suppose P is an integral polygon with area A and with B lattice
points on its boundary. Show that the area of tP is At2, and the number of
boundary points on tP is Bt. (Hint: Exercise 1.12.)

2.27. Let P be the self-intersecting polygon deﬁned by the line segments
[(0, 0), (4, 2)], [(4, 2), (4, 0)], [(4, 0), (0, 2)], and [(0, 2), (0, 0)]. Show that Pick’s
theorem does not hold for P.

2.28. Suppose that P and Q are integral polygons, and that Q lies entirely
inside P. Then the area bounded by the boundaries of P and Q, denoted
by P − Q, is a “doubly connected polygon.” Find and prove the analogue
of Pick’s theorem for P − Q. Generalize your formula to a polygon with n
“holes” (instead of one).

2.29. Show that every convex integral polygon with more than four vertices
must have an interior lattice point.

2.30. Consider the rhombus

R = {(x, y) : a|x| + b|y| ≤ ab} ,

where a and b are ﬁxed positive integers. Find a formula for LR(t).

2.31. We deﬁne the nth Farey sequence to be the sequence, in order from
smallest to largest, of all the rational numbers a
b in the interval [0, 1] such
that a and b are coprime and b ≤ n. For instance, the sixth Farey sequence is
0
1 , 1
6 , 1
5 , 1
4 , 1
3 , 2
5 , 1
2 , 3
5 , 2
3 , 3
4 , 4
5 , 5
6 , 1
1 .

(a) For two consecutive fractions a
b and c
d in a Farey sequence, prove that
bc − ad = 1.
(b) For three consecutive fractions a
b , c
d , and e
f in a Farey sequence, show
that c
d = a+e
b+f .

Exercises 57

2.32. Let ⌈x⌉ denote the smallest integer greater than or equal to x. Prove
that for all positive integers a and b,

a + (−1)
b a∑

m=0
(−1)⌈ bm
a ⌉ ≡ b + (−1)a b∑

n=0
(−1)⌈ an
b ⌉ mod 4 .

(Hint: This is a variation of Exercise 1.6. One way to obtain this identity is by
counting lattice points in a certain triangle, keeping track only of the parity.)

2.33. ♣ Verify (2.19).

2.34. ♣ Compute the partial fraction coeﬃcients (2.22).

2.35. ♣ Let a, b be positive integers. Show that

1
1 − zab = − ξk
a
ab (z − ξk
a )−1+ ab − 1
2ab + terms with positive powers of (z − ξk
a ) .

2.36. ♣ Let T be given by (2.16), and let c = gcd(e, f ). Prove that

LT (t) = 1
2ef (tr − u − v)2 + 1
2 (tr − u − v) ( 1
e + 1
f + 1
ef
 )

+ 1
4
 (1 + 1
e + 1
f
 ) + 1
12
 ( e
f + f
e + 1
ef
 )

+ ( 1
2e + 1
2f − u + v − tr
ef
 ) c−1∑

k=1
 ξ−ktr
c
1 − ξk
c − 1
ef
 c−1∑

k=1
 ξk(−tr+1)
c
(1 − ξk
c )2

+ 1
e
 e−1∑

j=1
e
c ̸ | j
 ξj(v−tr)
e(1 − ξjf
e ) (
1 − ξj
e) + 1
f
 f −1∑

l=1
f
c ̸ | l
 ξl(u−tr)
f(1 − ξle
f ) (
1 − ξl
f ) .

2.37. Let P be a rational polygon, and let d be the least common multiple of
the denominators of the vertices of P. Prove directly (using Exercise 2.36)
that the period of LP divides d.

2.38. ♣ Finish the calculation in Example 2.12, that is, compute

const 1
(1 − z1z2) (1 − z2
1z2) (1 − z1) (1 − z2) z3t
1 z2t
2 .

2.39. Compute the vector partition function of the quadrilateral given in
Example 2.12, that is, compute the counting function

f (v1, v2) := # {x ∈ Z
4
≥0 : ( 1 2 1 0
1 1 0 1
 ) x = ( v1
v2
 )}

for v1, v2 ∈ Z. (This function depends on the relationship between v1 and v2.)

58 2 A Gallery of Discrete Volumes

2.40. Search on the Internet for the program polymake [119]. You can down-
load it for free. Experiment.

Open Problems

2.41. Choose d + 1 of the 2
d vertices of the unit d-cube 2, and let ∆ be the
simplex deﬁned by their convex hull.

(a) Which choice of vertices maximizes vol ∆?
(b) What is the maximum volume of such a ∆?

2.42. Find classes of integral d-polytopes (Pd)d≥1 for which LPd(t) is sym-
metric in d and t. (The standard simplices ∆ and the cross-polytopes 3 form
two such classes.)

2.43. We mentioned already in the notes that all the roots of the polynomials
L3 have real part − 1
2 ; see [76, 149]. Find other classes of polytopes whose
lattice-point enumerator exhibits such special behavior.

Chapter 3
Counting Lattice Points in Polytopes:
The Ehrhart Theory

Ubi materia, ibi geometria.

Johannes Kepler (1571–1630)

Fig. 3.1 Self-portrait of
Eug`ene Ehrhart.

Given the profusion of examples that gave rise to the polynomial behavior
of the integer-point counting function LP (t) for special polytopes P, we now
ask whether there is a general structure theorem. As the ideas unfold, the
reader is invited to look back at Chapters 1 and 2 as appetizers and indeed
as special cases of the theorems developed below.

3.1 Triangulations

Because most of the proofs that follow work like a charm for a simplex, we ﬁrst
dissect a polytope into simplices. This dissection is captured by the following
deﬁnition.
 59

60 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

A triangulation of a convex d-polytope P is a ﬁnite collection T of
d-simplices with the following properties:

• P = ⋃

∆∈T ∆ .

• For every ∆1, ∆2 ∈ T , ∆1 ∩ ∆2 is a face common to both ∆1 and ∆2.

Figure 3.2 exhibits two triangulations of the 3-cube. We say that P can be
triangulated using no new vertices if there exists a triangulation T such
that the vertices of every ∆ ∈ T are vertices of P.

Fig. 3.2 Two (very diﬀerent) triangulations of the 3-cube.

Theorem 3.1 (Existence of triangulations). Every convex polytope can
be triangulated using no new vertices.

This theorem seems intuitively obvious, but it is not entirely trivial to prove.
We will introduce a speciﬁc type of triangulation for a given polytope P, in the
hope of achieving a maximum level of concreteness. Namely, given the polytope
P ⊆ Rd with vertices v1, v2, . . . , vn, randomly choose h1, h2, . . . , hn ∈ R, and
deﬁne a new polytope

Q := conv {(v1, h1), (v2, h2), . . . , (vn, hn)} ⊆ Rd+1. (3.1)

The lower hull of Q consists of all points that are “visible from below,” that
is, all points (x1, x2, . . . , xd+1) ∈ Q for which there is no ϵ > 0 such that
(x1, x2, . . . , xd+1 − ϵ) ∈ Q. A lower face of Q is a face of Q that is in the
lower hull. Let π : Rd+1 → Rd be deﬁned through

π(x1, x2, . . . , xd, xd+1) := (x1, x2, . . . , xd) ,

the projection that forgets the last coordinate. Exercise 3.3(a) implies that a
lower face F projects to π(F ) bijectively; in particular, F and π(F ) have the
same face structure (we say that they are combinatorially equivalent). In
a moment, we will show that all lower faces of Q are simplices, and that their
projections form a triangulation of P. A triangulation that can be constructed
from “lifting” a polytope in the above fashion is called regular. Figure 3.3
shows an example.

3.1 Triangulations 61

Fig. 3.3 Constructing a regular triangulation of a 9-gon.

Proof of Theorem 3.1. We may assume that P = conv {v1, v2, . . . , vn} ⊆ Rd

is full dimensional. Construct a lifted polytope Q as in (3.1); our ﬁrst goal is
to show that every lower face of Q is a simplex. To achieve this goal, it suﬃces
to prove that every lower facet is a simplex. This, in turn, is equivalent to the
statement that every aﬃnely independent set of d + 1 vertices of P gets lifted
to a set of d + 1 points in Rd+1 that determine a hyperplane H ⊆ Rd+1 that
does not contain any other lifted vertex of P. After relabeling, we may assume
that the chosen d + 1 aﬃnely independent vertices are v1, v2, . . . , vd+1, and
so H is given by the equation

det
 

 1 1 1 1
v1 v2 · · · vd+1 x
h1 h2 hd+1 xd+1
 

 = 0 (3.2)

in the variables x1, x2, . . . , xd+1. If we now specialize (x, xd+1) = (vj, hj) for
some j > d + 1, the determinant on the left-hand side of (3.2) cannot be zero,
since h1, h2, . . . , hd+1, hj were chosen randomly; in other words, the lifted
vertex (vj, hj) is not on H for j > d + 1. We have thus proved that every
lower face of Q is a simplex. By our earlier bijective argument,

T := {π(F) : F is a lower face of Q}

consists of simplices contained in P; we claim that T is a triangulation of P.
To prove that P = ⋃
∆∈T ∆, we have “only” to show that P ◦ ⊆ ⋃
∆∈T ∆.
So let x ∈ P ◦; our goal is to construct a lower face F of Q such that x ∈ π(F ).

62 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

Consider the line L := {x + λ ed+1 : λ ∈ R} ,

where ed+1 denotes the (d + 1)st unit vector; that is, L is a vertical line
through x. Note that L ∩ Q◦ ̸= ∅ , (3.3)

since x ∈ P ◦. So L ∩ Q is a line segment with endpoints (x, y) and (x, z) for
some y < z. Since (x, y) is on the boundary of Q, it is contained in some
(proper) face F of Q. Thus we can ﬁnd a supporting hyperplane

H = {
p ∈ Rd+1 : a · p = b}

that deﬁnes F such that Q ⊆ {p ∈ Rd+1 : a · p ≥ b
}. Note that (x, z) cannot
lie on H, since otherwise, the entire line segment from (x, y) to (x, z) would
be in H, contradicting (3.3). Thus

a · (x, y) = b and a · (x, z) > b ,

which implies ad+1(z − y) > 0 and so ad+1 > 0. But then we can use
Exercise 3.3(b) to conclude that F is a lower face of Q. By construction,
x ∈ π(F), which proves P ⊆ ⋃∆∈T ∆.
That the second deﬁning property for a triangulation holds for T , namely
that for every ∆1, ∆2 ∈ T , ∆1 ∩ ∆2 is a face common to both ∆1 and ∆2, is
left to show in Exercise 3.3(c). ⊓⊔

3.2 Cones

A pointed cone K ⊆ Rd is a set of the form

K = {v + λ1w1 + λ2w2 + · · · + λmwm : λ1, λ2, . . . , λm ≥ 0} ,

where v, w1, w2, . . . , wm ∈ Rd are such that there exists a hyperplane H
for which H ∩ K = {v}; that is, K \ {v} lies strictly on one side of H. The
vector v is called the apex of K, and the wk are the generators of K. The
cone is rational if v, w1, w2, . . . , wm ∈ Qd, in which case we may choose
w1, w2, . . . , wm ∈ Z
d by clearing denominators. The dimension of K is the
dimension of the aﬃne space spanned by K; if K is of dimension d, we call it a
d-cone. The d-cone K is simplicial if K has precisely d linearly independent
generators.
Just as polytopes have a description as an intersection of half-spaces, so
do pointed cones: a rational pointed d-cone is the d-dimensional intersection
of ﬁnitely many half-spaces of the form
{
x ∈ Rd : a1x1 + a2x2 + · · · + adxd ≤ b}

3.2 Cones 63

with integral parameters a1, a2, . . . , ad, b ∈ Z such that the corresponding
hyperplanes of the form
{
x ∈ Rd : a1x1 + a2x2 + · · · + adxd = b}

meet in exactly one point.
Cones are important for many reasons. The most practical for us is a
process called coning over a polytope. Given a convex polytope P ⊂ Rd with
vertices v1, v2, . . . , vn, we lift these vertices into Rd+1 by adding a 1 as their
last coordinate. So, let

w1 = (v1, 1) , w2 = (v2, 1) , . . . , wn = (vn, 1) .

Now we deﬁne the cone over P as

cone(P) = {λ1w1 + λ2w2 + · · · + λnwn : λ1, λ2, . . . , λn ≥ 0} ⊂ Rd+1.

This pointed cone has the origin as apex, and we can recover our original
polytope P (strictly speaking, the translated set {(x, 1) : x ∈ P}) by cutting
cone(P) with the hyperplane xd+1 = 1, as shown in Figure 3.4.

x 2

x 3

x 1
 Fig. 3.4 Coning over a polytope.

By analogy with the language of polytopes, we say that the hyperplane
H = {x ∈ Rd : a · x = b} is a supporting hyperplane of the pointed d-cone
K if K lies entirely on one side of H, that is,

64 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

K ⊆ {
x ∈ Rd : a · x ≤ b} or K ⊆ {
x ∈ Rd : a · x ≥ b} .

A face of K is a set of the form K ∩ H, where H is a supporting hyperplane
of K. The (d − 1)-dimensional faces are called facets, and the 1-dimensional
faces edges, of K. The apex of K is its unique 0-dimensional face.
Just as polytopes can be triangulated into simplices, pointed cones can be
triangulated into simplicial cones. So, a collection T of simplicial d-cones is a
triangulation of the d-cone K if it satisﬁes the following:

• K = ⋃

S∈T S .

• For every S1, S2 ∈ T , S1 ∩ S2 is a face common to both S1 and S2.

We say that K can be triangulated using no new generators if there
exists a triangulation T such that the generators of every S ∈ T are generators
of K.

Theorem 3.2. Every pointed cone can be triangulated into simplicial cones
using no new generators.

Proof. This theorem is really a corollary to Theorem 3.1. Given a pointed
d-cone K with apex v, there exists a hyperplane H that intersects K only
at v. Choose w ∈ K◦; then

P := (w − v + H) ∩ K

is a (d − 1)-polytope whose vertices are determined by the generators of K.
(This construction yields a variant of Figure 3.4.) Now triangulate P using no
new vertices. Each simplex ∆j in this triangulation gives naturally rise to a
simplicial cone Sj := {v + λ x : λ ≥ 0, x ∈ ∆j} ,

and these simplicial cones, by construction, triangulate K. ⊓⊔

3.3 Integer-Point Transforms for Rational Cones

We want to encode the information contained by the lattice points in a set
S ⊂ Rd. It turns out that the following multivariate generating function allows
us to do this in an eﬃcient way if S is a rational cone or polytope:

σS(z) = σS (z1, z2, . . . , zd) := ∑

m∈S∩Zd zm.

The generating function σS simply lists all integer points in S in a special
form: not as a list of vectors, but as a formal sum of Laurent monomials. We
call σS the integer-point transform of S; the function σS also goes by the

3.3 Integer-Point Transforms for Rational Cones 65

name moment generating function or simply generating function of S. The
integer-point transform σS opens the door to both algebraic and analytic
techniques.

Example 3.3. As a warmup example, consider the 1-dimensional cone K =
[0, ∞). Its integer-point transform is our old friend

σK(z) = ∑

m∈[0,∞)∩Z
zm = ∑

m≥0 zm = 1
1 − z . ⊓⊔

Example 3.4. Now we consider the 2-dimensional cone

K := {λ1(1, 1) + λ2(−2, 3) : λ1, λ2 ≥ 0} ⊂ R2

depicted in Figure 3.5. To obtain the integer-point transform σK, we tile K

x 1

x 2
 K


 (1 ; 1)

(   2 ; 3)
 Fig. 3.5 The cone K from Example 3.4 and its fundamental parallelogram.

by copies of the fundamental parallelogram

Π := {λ1(1, 1) + λ2(−2, 3) : 0 ≤ λ1, λ2 < 1} ⊂ R2.

More precisely, we translate Π by nonnegative integer linear combinations of
the generators (1, 1) and (−2, 3), and these translates will exactly cover K.
How can we list the integer points in K as Laurent monomials? Let’s ﬁrst list
all vertices of the translates of Π. These are nonnegative integer combinations

66 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

of the generators (1, 1) and (−2, 3), so we can list them using geometric series:

∑

m=j(1,1)+k(−2,3)
j,k≥0
 zm = ∑

j≥0
 ∑

k≥0 zj(1,1)+k(−2,3) = 1
(1 − z1z2) (1 − z−2
1 z3
2) .

We now use the integer points (m, n) ∈ Π to generate a subset of Z
2 by adding
to (m, n) nonnegative linear integer combinations of the generators (1, 1) and
(−2, 3). Namely, we let

L(m,n) := {(m, n) + j(1, 1) + k(−2, 3) : j, k ∈ Z≥0} .

It is immediate that K ∩ Z
2 is the disjoint union of the subsets L(m,n) as
(m, n) ranges over Π ∩ Z
2 = {(0, 0), (0, 1), (0, 2), (−1, 2), (−1, 3)}. Hence

σK(z) = (1 + z2 + z2
2 + z−1
1 z2
2 + z−1
1 z3
2) ∑

m=j(1,1)+k(−2,3)
j,k≥0
 zm

= 1 + z2 + z2
2 + z−1
1 z2
2 + z−1
1 z3
2
(1 − z1z2) (1 − z−2
1 z3
2) . ⊓⊔

Similar geometric series suﬃce to describe integer-point transforms for
rational simplicial d-cones. The following result utilizes the geometric series
in several directions simultaneously.

Theorem 3.5. Suppose

K := {λ1w1 + λ2w2 + · · · + λdwd : λ1, λ2, . . . , λd ≥ 0}

is a simplicial d-cone, where w1, w2, . . . , wd ∈ Z
d. Then for v ∈ Rd, the
integer-point transform σv+K of the shifted cone v + K is the rational function

σv+K(z) = σv+Π(z)
(1 − zw1) (1 − zw2) · · · (1 − zwd ) ,

where Π is the half-open parallelepiped

Π := {λ1w1 + λ2w2 + · · · + λdwd : 0 ≤ λ1, λ2, . . . , λd < 1} .

The half-open parallelepiped Π is called the fundamental parallelepiped
of K.

Proof. In σv+K(z) = ∑

m∈(v+K)∩Zd zm, we list each integer point m in v + K
as the Laurent monomial zm. Such a lattice point can, by deﬁnition, be
written as m = v + λ1w1 + λ2w2 + · · · + λdwd

for some numbers λ1, λ2, . . . , λd ≥ 0. Because the wk form a basis of Rd,
this representation is unique. Let’s write each λk in terms of its integer and

3.3 Integer-Point Transforms for Rational Cones 67

fractional parts: λk = ⌊λk⌋ + {λk}. So

m = v+({λ1} w1+{λ2} w2+· · ·+{λd} wd)+⌊λ1⌋ w1+⌊λ2⌋ w2+· · ·+⌊λd⌋ wd ,

and we should note that since 0 ≤ {λk} < 1, the vector

p := v + {λ1} w1 + {λ2} w2 + · · · + {λd} wd

is in v + Π. In fact, p ∈ Z
d, since m and ⌊λk⌋ wk are all integer vectors. Again,
the representation of p in terms of the wk is unique. In summary, we have
proved that every m ∈ v + K ∩ Z
d can be uniquely written as

m = p + k1w1 + k2w2 + · · · + kdwd (3.4)

for some p ∈ (v + Π) ∩ Z
d and some integers k1, k2, . . . , kd ≥ 0. On the other
hand, let’s write the rational function on the right-hand side of the theorem
as a product of series:

σv+Π(z)
(1 − zw1 ) · · · (1 − zwd ) =
 

 ∑

p∈(v+Π)∩Zd
zp



 

 ∑

k1≥0 zk1w1
 

 · · ·
 

 ∑

kd≥0 zkdwd
 

 .

If we multiply everything out, a typical exponent will look exactly like (3.4).
⊓⊔

Our proof contains a crucial geometric idea. Namely, we tile the cone v + K
with translates of v + Π by nonnegative integral combinations of the wk. It is
this tiling that gives rise to the nice integer-point transform in Theorem 3.5.
Computationally, we therefore favor cones over polytopes due to our ability to
tile a simplicial cone with copies of the fundamental domain, as above. More
reasons for favoring cones over polytopes appear in Chapters 10 and 11.
Theorem 3.5 shows that the real complexity of computing the integer-
point transform σv+K is embedded in the location of the lattice points in the
parallelepiped v + Π.
By mildly strengthening the hypothesis of Theorem 3.5, we obtain a slightly
easier generating function, a result we shall need in Section 3.5 and Chapter 4.

Corollary 3.6. Suppose

K := {λ1w1 + λ2w2 + · · · + λdwd : λ1, λ2, . . . , λd ≥ 0}

is a simplicial d-cone, where w1, w2, . . . , wd ∈ Z
d, and v ∈ Rd, such that the
boundary of v + K contains no integer point. Then

σv+K(z) = σv+Π(z)
(1 − zw1) (1 − zw2) · · · (1 − zwd ) ,

where Π is the open parallelepiped

68 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

Π := {λ1w1 + λ2w2 + · · · + λdwd : 0 < λ1, λ2, . . . , λd < 1} .

Proof. The proof of Theorem 3.5 goes through almost verbatim, except that
v + Π now has no boundary lattice points, so that there is no harm in choosing
Π to be open. ⊓⊔

Since a general pointed cone can always be triangulated into simplicial
cones, the integer-point transforms add up in an inclusion–exclusion manner
(note that the intersection of simplicial cones in a triangulation is again a
simplicial cone, by Exercise 3.5). Hence we have the following corollary.

Corollary 3.7. For a pointed cone

K = {v + λ1w1 + λ2w2 + · · · + λmwm : λ1, λ2, . . . , λm ≥ 0}

with v ∈ Rd, w1, w2, . . . , wm ∈ Z
d, the integer-point transform σK(z) evalu-
ates to a rational function in the coordinates of z. ⊓⊔

Philosophizing some more, one can show that the original inﬁnite sum
σK(z) converges only for z in a subset of Cd, whereas the rational function
that represents σK gives us its meromorphic continuation. In Chapters 4
and 11, we will make use of this continuation.

3.4 Expanding and Counting Using Ehrhart’s Original
Approach

Here is the fundamental theorem concerning the lattice-point count in an
integral convex polytope.

Theorem 3.8 (Ehrhart’s theorem). If P is an integral convex d-polytope,
then LP (t) is a polynomial in t of degree d.

This result is due to Eug`ene Ehrhart, in whose honor we call LP the
Ehrhart polynomial of P. Naturally, there is an extension of Ehrhart’s
theorem to rational polytopes, which we will discuss in Section 3.8.
Our proof of Ehrhart’s theorem uses generating functions of the form∑

t≥0 f (t) zt, similar in spirit to those discussed at the beginning of Chapter 1.
If f is a polynomial, this power series takes on a special form, which we invite
the reader to prove (Exercise 3.13):

Lemma 3.9. If ∑

t≥0 f (t) zt = g(z)
(1 − z)d+1 ,

then f is a polynomial of degree d if and only if g is a polynomial of degree at
most d and g(1) ̸= 0. ⊓⊔

3.4 Expanding and Counting Using Ehrhart’s Original Approach 69

The reason we introduced generating functions of the form σS(z) =∑

m∈S∩Zd zm in Section 3.3 is that they are extremely handy for lattice-
point problems. The connection to lattice points is evident, since we are
summing over them. If we are interested in the lattice-point count, we simply
evaluate σS at z = (1, 1, . . . , 1):

σS(1, 1, . . . , 1) = ∑

m∈S∩Zd
1m = ∑

m∈S∩Zd
1 = # (S ∩ Z
d) .

(Here we denote by 1 a vector all of whose components are 1.) Naturally, we
should make this evaluation only if S is bounded; Theorem 3.5 already tells
us that it is no fun evaluating σK(1) if K is a cone.
But the magic of the generating function σS does not stop there. To literally
take it to the next level, we cone over a convex polytope P. If P ⊂ Rd has
the vertices v1, v2, . . . , vn ∈ Z
d, recall that we lift these vertices into Rd+1 by
adding a 1 as their last coordinate. So let

w1 = (v1, 1) , w2 = (v2, 1) , . . . , wn = (vn, 1) .

Then

cone(P) = {λ1w1 + λ2w2 + · · · + λnwn : λ1, λ2, . . . , λn ≥ 0} ⊂ Rd+1.

Recall that we can recover our original polytope P by cutting cone(P) with
the hyperplane xd+1 = 1. We can recover more than just the original polytope
in cone(P): by cutting the cone with the hyperplane xd+1 = 2, we obtain
a copy of P dilated by a factor of 2. (The reader should meditate on why
this cut is a 2-dilate of P.) More generally, we can cut the cone with the
hyperplane xd+1 = t and obtain tP, as suggested by Figure 3.6.
Now let’s form the integer-point transform σcone(P) of cone(P). By what we
just said, we should look at diﬀerent powers of zd+1: there is one term (namely,
1), with z0
d+1, corresponding to the origin; the terms with z1
d+1 correspond to
lattice points in P (listed as Laurent monomials in z1, z2, . . . , zd), the terms
with z2
d+1 correspond to points in 2P, etc. In short,

σcone(P) (z1, z2, . . . , zd+1)

= 1 + σP (z1, . . . , zd) zd+1 + σ2P (z1, . . . , zd) z2
d+1 + · · ·

= 1 + ∑

t≥1 σtP (z1, . . . , zd) zt
d+1 .

Specializing further for enumeration purposes, we recall that σP (1, 1, . . . , 1) =
# (P ∩ Z
d), and so

70 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

x 2

x 3

x 1
 Fig. 3.6 Recovering dilates of P in cone(P).

σcone(P) (1, 1, . . . , 1, zd+1) = 1 + ∑

t≥1 σtP (1, 1, . . . , 1) zt
d+1

= 1 + ∑

t≥1 # (tP ∩ Z
d) zt
d+1 .

But by deﬁnition, the enumerators on the right-hand side are just evaluations
of Ehrhart’s counting function, that is, σcone(P) (1, 1, . . . , 1, zd+1) is nothing
but the Ehrhart series of P:

Lemma 3.10. σcone(P) (1, 1, . . . , 1, z) = 1 + ∑

t≥1 LP (t) zt = EhrP (z) . ⊓⊔

With this machinery at hand, we can prove Ehrhart’s theorem.

Proof of Theorem 3.8. It suﬃces to prove the theorem for simplices, because
we can triangulate any integral polytope into integral simplices, using no new
vertices. Note that these simplices will intersect in lower-dimensional integral
simplices.
By Lemma 3.9, it suﬃces to prove that for an integral d-simplex ∆,

Ehr∆(z) = 1 + ∑

t≥1 L∆(t) zt = g(z)
(1 − z)d+1

3.5 The Ehrhart Series of an Integral Polytope 71

for some polynomial g of degree at most d with g(1) ̸= 0. In Lemma 3.10,
we showed that the Ehrhart series of ∆ equals σcone(∆) (1, 1, . . . , 1, z), so let’s
study the integer-point transform attached to cone(∆).
The simplex ∆ has d + 1 vertices v1, v2, . . . , vd+1, and so cone(∆) ⊂ Rd+1

is simplicial, with apex the origin and generators

w1 = (v1, 1) , w2 = (v2, 1) , . . . , wd+1 = (vd+1, 1) ∈ Z
d+1.

Now we use Theorem 3.5:

σcone(∆) (z1, z2, . . . , zd+1) = σΠ (z1, z2, . . . , zd+1)
(1 − zw1) (1 − zw2 ) · · · (1 − zwd+1) ,

where Π = {λ1w1 + λ2w2 + · · · + λd+1wd+1 : 0 ≤ λ1, λ2, . . . , λd+1 < 1}. This
parallelepiped is bounded, so the attached generating function σΠ is a Laurent
polynomial in z1, z2, . . . , zd+1.
We claim that the zd+1-degree of σΠ is at most d. In fact, since the xd+1-
coordinate of each wk is 1, the xd+1-coordinate of a point in Π is λ1 +λ2 +· · ·+
λd+1 for some 0 ≤ λ1, λ2, . . . , λd+1 < 1. But then λ1 + λ2 + · · · + λd+1 < d + 1,
so if this sum is an integer, it is at most d, which implies that the zd+1-degree
of σΠ (z1, z2, . . . , zd+1) is at most d. Consequently, σΠ (1, 1, . . . , 1, zd+1) is a
polynomial in zd+1 of degree at most d. The evaluation σΠ (1, 1, 1, . . . , 1) of this
polynomial at zd+1 = 1 is not zero, because σΠ (1, 1, 1, . . . , 1) = # (Π ∩ Z
d+1),
and the origin is a lattice point in Π.
Finally, if we specialize zwk to z1 = z2 = · · · = zd = 1, we obtain z1
d+1, so
that
 σcone(∆) (1, 1, . . . , 1, zd+1) = σΠ (1, 1, . . . , 1, zd+1)

(1 − zd+1)
d+1 .

The left-hand side is Ehr∆ (zd+1) = 1 + ∑

t≥1 L∆(t) zt
d+1 by Lemma 3.10. ⊓⊔

3.5 The Ehrhart Series of an Integral Polytope

We can actually take our proof of Ehrhart’s theorem one step further by
studying the polynomial σΠ (1, 1, . . . , 1, zd+1). As mentioned above, the coef-
ﬁcient of zk
d+1 simply counts the integer points in the parallelepiped Π cut
with the hyperplane xd+1 = k. Let’s record this.

Corollary 3.11. Suppose ∆ is an integral d-simplex with vertices v1, v2, . . . ,
vd+1, and let wj = (vj, 1). Then

Ehr∆(z) = 1 + ∑

t≥1 L∆(t) zt = h
∗
d zd + h
∗
d−1 zd−1 + · · · + h
∗
1 z + h
∗
0
(1 − z)d+1 ,

where h
∗
k equals the number of integer points in

72 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

{λ1w1 + λ2w2 + · · · + λd+1wd+1 : 0 ≤ λ1, λ2, . . . , λd+1 < 1}

with last coordinate equal to k. ⊓⊔

This result can actually be used to compute Ehr∆, and therefore the
Ehrhart polynomial, of an integral simplex ∆ in low dimensions very quickly
(a fact that the reader may discover in some of the exercises). We remark,
however, that things are not as simple for arbitrary integral polytopes. Not
only is triangulation a nontrivial task in general, but one would also have to
deal with overcounting where simplices of a triangulation meet.
Corollary 3.11 implies that the numerator of the Ehrhart series of an
integral simplex has nonnegative coeﬃcients, since they count something.
Although it is not known whether the coeﬃcients of the Ehrhart series of
a general polytope count something, the nonnegativity property magically
survives.

Theorem 3.12 (Stanley’s nonnegativity theorem). Suppose P is an
integral convex d-polytope with Ehrhart series

EhrP (z) = h
∗
d zd + h
∗
d−1 zd−1 + · · · + h
∗
0
(1 − z)d+1 .

Then h
∗
0, h
∗
1, . . . , h∗
d are nonnegative integers.

We call the numerator h
∗
P (z) of the Ehrhart series EhrP (z) the h
∗-po-
lynomial of P.1 Theorem 3.12 says that it always has nonnegative integer
coeﬃcients; we will have (much) more to say about h
∗
P (z) in Chapter 10.

Proof. Triangulate cone(P) ⊂ Rd+1 into the simplicial cones K1, K2, . . . , Km.
Exercise 3.19 ensures that there exists a vector v ∈ Rd+1 such that

cone(P) ∩ Z
d+1 = (v + cone(P)) ∩ Z
d+1

(that is, we neither lose nor gain any lattice points in shifting cone(P) by
v) and neither the facets of v + cone(P) nor the translated triangulation
hyperplanes contain any lattice points. This implies that every lattice point
in v + cone(P) belongs to exactly one simplicial cone v + Kj:

cone(P) ∩ Z
d+1 = (v + cone(P)) ∩ Z
d+1 =
 m⋃

j=1
 ((v + Kj) ∩ Z
d+1) , (3.5)

and this union is a disjoint union. If we translate the last identity into
generating-function language, it becomes

1 Other names for h∗
P (z) used in the literature are δ-vector/polynomial and Ehrhart
h-vector/polynomial of P.

3.5 The Ehrhart Series of an Integral Polytope 73

σcone(P) (z1, z2, . . . , zd+1) =
 m∑

j=1 σv+Kj (z1, z2, . . . , zd+1) .

But now we recall that the Ehrhart series of P is just a special evaluation of
σcone(P) (Lemma 3.10):

EhrP (z) = σcone(P) (1, 1, . . . , 1, z) =
 m∑

j=1 σv+Kj (1, 1, . . . , 1, z) . (3.6)

It suﬃces to show that the rational generating functions σv+Kj (1, 1, . . . , 1, z)
for the simplicial cones v + Kj have nonnegative integer numerator. But
this fact follows from evaluating the rational function in Corollary 3.6 at
(1, 1, . . . , 1, z). ⊓⊔

This proof shows a little more: Since the origin is in precisely one simplicial
cone on the right-hand side of (3.5), we get on the right-hand side of (3.6)
precisely one term that contributes 1/(1 − z)d+1 to EhrP ; all other terms
contribute to higher powers of the numerator polynomial of EhrP . That is,
the constant term h
∗
0 equals 1. The reader might feel that we are chasing our
tail at this point, since we assumed from the very beginning that the constant
term of the inﬁnite series EhrP is 1, and hence h
∗
0 has to be 1, as a quick
look at the expansion of the rational function representing EhrP shows. The
above argument shows merely that this convention is geometrically sound.
Let’s record this:

Lemma 3.13. Suppose P is an integral convex d-polytope with Ehrhart series

EhrP (z) = h
∗
d zd + h
∗
d−1 zd−1 + · · · + h
∗
0
(1 − z)d+1 .

Then h
∗
0 = 1. ⊓⊔

For a general integral polytope P, the reader has probably already discov-
ered how to extract the Ehrhart polynomial of P from its Ehrhart series:

Lemma 3.14. Suppose P is an integral convex d-polytope with Ehrhart series

EhrP (z) = 1 + ∑

t≥1 LP (t) zt = h
∗
d zd + h
∗
d−1 zd−1 + · · · + h
∗
1 z + 1
(1 − z)d+1 .

Then
 LP (t) = (
t + d
d
 ) + h
∗
1
(t + d − 1
d
 ) + · · · + h
∗
d−1
(t + 1
d
 ) + h
∗
d
(t
d
)
.

Proof. Expand into a binomial series:

74 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

EhrP (z) = h
∗
d zd + h
∗
d−1 zd−1 + · · · + h
∗
1 z + 1
(1 − z)d+1

= (h
∗
d zd + h
∗
d−1 zd−1 + · · · + h
∗
1 z + 1) ∑

t≥0
 (t + d
d
 )zt

= h
∗
d ∑

t≥0
 (t + d
d
 )zt+d + h
∗
d−1 ∑

t≥0
 (t + d
d
 )zt+d−1 + · · ·

+ h
∗
1 ∑

t≥0
 (t + d
d
 )zt+1 + ∑

t≥0
 (t + d
d
 )
zt

= h
∗
d ∑

t≥d
 (t
d

)zt + h
∗
d−1 ∑

t≥d−1
 (
t + 1
d
 )zt + · · ·

+ h
∗
1 ∑

t≥1
 (t + d − 1
d
 )zt + ∑

t≥0
 (t + d
d
 )zt.

In all inﬁnite sums on the right-hand side, we can begin the index t with 0
without changing the sums, by the deﬁnition (2.1) of the binomial coeﬃcient.
Hence

EhrP (z)

= ∑

t≥0
 (
h
∗
d
(t
d

) + h
∗
d−1
(
t + 1
d
 ) + · · · + h
∗
1
(t + d − 1
d
 ) + (t + d
d
 )) zt.

⊓⊔

The representation of the polynomial LP (t) in terms of the coeﬃcients of
EhrP can be interpreted as the Ehrhart polynomial expressed in the basis(t
d
), (t+1
d ), . . . , (t+d
d ) (see Exercise 3.14). This representation is very useful, as
the following results show.

Corollary 3.15. If P is an integral convex d-polytope, then the constant term
of the Ehrhart polynomial LP is 1.

Proof. Use the expansion of Lemma 3.14. The constant term is

LP (0) = (
d
d
) + h
∗
1
(d − 1
d
 ) + · · · + h
∗
d−1
(1
d

) + h
∗
d
(0
d
) = (
d
d
) = 1 . ⊓⊔

This proof is exciting, because it marks the ﬁrst instance in which we extend
the domain of an Ehrhart polynomial beyond the positive integers, for which
the lattice-point enumerator was initially deﬁned. More precisely, Ehrhart’s
theorem (Theorem 3.8) implies that the counting function

LP (t) = # (tP ∩ Z
d) ,

3.5 The Ehrhart Series of an Integral Polytope 75

originally deﬁned for positive integers t, can be extended to all real or even
complex arguments t (as a polynomial). A natural question arises: are there
nice interpretations of LP (t) for arguments t that are not positive integers?
Corollary 3.15 gives such an interpretation for t = 0. In Chapter 4, we will
give interpretations of LP (t) for negative integers t.

Corollary 3.16. Suppose P is an integral convex d-polytope with Ehrhart
series
 EhrP (z) = h
∗
d zd + h
∗
d−1 zd−1 + · · · + h
∗
1 z + 1
(1 − z)d+1 .

Then h
∗
1 = LP (1) − d − 1 = # (P ∩ Z
d) − d − 1.

Proof. Use the expansion of Lemma 3.14 with t = 1:

LP (1) = (
d + 1
d
 ) + h
∗
1
(
d
d
) + · · · + h
∗
d−1
(2
d
) + h
∗
d
(1
d

) = d + 1 + h
∗
1 . ⊓⊔

The proof of Corollary 3.16 suggests that there are also formulas for
h
∗
2, h
∗
3, . . . in terms of the evaluations LP (1), LP (2), . . . , and we invite the
reader to ﬁnd them (Exercise 3.15).
A ﬁnal corollary to Theorem 3.12 and Lemma 3.14 states how large the
denominators of the Ehrhart coeﬃcients can be:

Corollary 3.17. Suppose P is an integral polytope with Ehrhart polynomial
LP (t) = cd t
d + cd−1 t
d−1 + · · · + c1 t + 1. Then all coeﬃcients satisfy d! ck ∈ Z.

Proof. By Lemma 3.14,

LP (t) = (
t + d
d
 ) + h
∗
1
(t + d − 1
d
 ) + · · · + h
∗
d−1
(t + 1
d
 ) + h
∗
d
(t
d
)
,

where the h
∗
k are integers by Corollary 3.11 and our proof of Theorem 3.12.
Hence multiplying out this expression yields a polynomial in t whose coeﬃ-
cients can be written as rational numbers with denominator d!. ⊓⊔

We ﬁnish this section with a general result that gives relations between
negative integer roots of a polynomial and its generating function. This
theorem will become handy in Chapter 4, in which we ﬁnd an interpretation
for the evaluation of an Ehrhart polynomial at negative integers.

Theorem 3.18. Suppose p is a degree-d polynomial with the rational gener-
ating function

∑

t≥0 p(t) zt = hd zd + hd−1 zd−1 + · · · + h1 z + h0
(1 − z)d+1 .

Then hd = hd−1 = · · · = hk+1 = 0 and hk ̸= 0 if and only if p(−1) = p(−2) =
· · · = p (−(d − k)) = 0 and p (−(d − k + 1)) ̸= 0.

76 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

Proof. Suppose hd = hd−1 = · · · = hk+1 = 0 and hk ̸= 0. Then the proof of
Lemma 3.14 gives

p(t) = h0
(
t + d
d
 ) + · · · + hk−1
(t + d − k + 1
d
 ) + hk
(
t + d − k
d
 )
.

All the binomial coeﬃcients are zero for t = −1, −2, . . . , −d + k, so those are
roots of p. On the other hand, all binomial coeﬃcients but the last one are
zero for t = −d + k − 1, and since hk ̸= 0, −d + k − 1 is not a root of p.
Conversely, suppose p(−1) = p(−2) = · · · = p (−(d − k)) = 0 and
p (−(d − k + 1)) ̸= 0. The ﬁrst root −1 of p gives

0 = p(−1) = h0
(
d − 1
d
 )+h1
(d − 2
d
 )+· · ·+hd−1
(0
d

)+hd
(−1
d
 ) = hd
(−1
d
 ),

so we must have hd = 0. The next root −2 forces hd−1 = 0, and so on, up to
the root −d + k, which forces hk+1 = 0. It remains to show that hk ̸= 0. But
if hk were zero, then by a similar line of reasoning as in the ﬁrst part of the
proof, we would have p(−d + k − 1) = 0, a contradiction. ⊓⊔

3.6 From the Discrete to the Continuous Volume of a
Polytope

Given a geometric object S ⊂ Rd, its volume, deﬁned by the integral vol S :=∫

S dx, is one of the fundamental data of S. By the deﬁnition of the integral, say
in the Riemannian sense, we can think of computing vol S by approximating
S with d-dimensional boxes that get smaller and smaller. To be precise, if we
take the boxes with side length 1
t , then they each have volume 1
td . We might
further think of the boxes as ﬁlling out the space between grid points in the
lattice ( 1
t Z
)d. This means that volume computation can be approximated by

counting boxes, or equivalently, lattice points in ( 1
t Z
)d:

vol S = lim
t→∞ 1
td · #
 (

S ∩ ( 1
t Z
)d)
 .

It is a short step to counting integer points in dilates of S, because

#
 (

S ∩ ( 1
t Z
)d)
 = # (tS ∩ Z
d) .

Let’s summarize:

3.6 From the Discrete to the Continuous Volume of a Polytope 77

Lemma 3.19. Suppose S ⊂ Rd is d-dimensional. Then

vol S = lim
t→∞ 1
td · # (tS ∩ Z
d) . ⊓⊔

We emphasize here that S is d-dimensional, because otherwise (since S could
be lower-dimensional although living in d-space), by our current deﬁnition,
vol S = 0. We will extend our volume deﬁnition in Chapter 5 to give nonzero
relative volume to objects that are not full-dimensional.
Part of the magic of Ehrhart’s theorem lies in the fact that for an integral
d-polytope P, we do not have to take a limit to compute vol P; we need to
compute “only” the d + 1 coeﬃcients of a polynomial.

Corollary 3.20. Suppose P ⊂ Rd is an integral convex d-polytope with
Ehrhart polynomial cd td + cd−1 t
d−1 + · · · + c1 t + 1. Then cd = vol P.

Proof. By Lemma 3.19,

vol P = lim
t→∞ cd t
d + cd−1 td−1 + · · · + c1 t + 1
td = cd . ⊓⊔

On the one hand, this should not come as a surprise, because the number
of integer points in some object should grow roughly like the volume of the
object as we make it bigger and bigger. On the other hand, the fact that we
can compute the volume as one term of a polynomial should be very surprising:
the polynomial is a counting function and as such is something discrete, yet
by computing it (and its leading term), we derive some continuous data. Even
more, we can—at least theoretically—compute this continuous datum (the
volume) of the object by calculating a few values of the polynomial and then
interpolating; this can be described as a completely discrete operation!
We ﬁnish this section by showing how to retrieve the continuous volume of
an integral polytope from its Ehrhart series.

Corollary 3.21. Suppose P ⊂ Rd is an integral convex d-polytope, and

EhrP (z) = h
∗
d zd + h
∗
d−1 zd−1 + · · · + h
∗
1 z + 1
(1 − z)d+1 .

Then vol P = 1
d! (h
∗
d + h
∗
d−1 + · · · + h
∗
1 + 1) .

Proof. Use the expansion of Lemma 3.14. The leading coeﬃcient is

1
d! (h
∗
d + h
∗
d−1 + · · · + h
∗
1 + 1) . ⊓⊔

78 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

3.7 Interpolation

We now use the polynomial behavior of the discrete volume LP of an integral
polytope P to compute the continuous volume vol P and the discrete volume
LP from ﬁnite data.
Two points uniquely determine a line. There exists a unique quadratic whose
graph passes through any three given noncollinear points. More generally, a
degree-d polynomial p is determined by d + 1 points (x, p(x)) ∈ R2 in general
position. Namely, evaluating p(x) = cdx
d + cd−1xd−1 + · · · + c0 at distinct
inputs x1, x2, . . . , xd+1 gives






 p (x1)
p (x2)
...
p (xd+1)
 




 = V
 





 cd
cd−1
...
c0
 




 , (3.7)

where
 V =
 





 xd
1 xd−1
1 · · · x1 1
xd
2 xd−1
2 · · · x2 1
... ... ... ...
xd
d+1 xd−1
d+1 · · · xd+1 1
 




 ,

so that 





 cd
cd−1
...
c0
 




 = V−1
 





 p (x1)
p (x2)
...
p (xd+1)
 




 . (3.8)

(Exercise 3.21 makes sure that V is invertible.) The identity (3.8) gives the
famous Lagrange interpolation formula.
This gives us an eﬃcient way to compute LP , at least when dim P is not
too large. The continuous volume of P will follow instantly, since it is the
leading coeﬃcient cd of LP . In the case of an Ehrhart polynomial LP , we
know that LP (0) = 1, so that (3.7) simpliﬁes to







 LP (x1) − 1
LP (x2) − 1
...
LP (xd) − 1
 




 =
 





 xd
1 x
d−1
1 · · · x1
xd
2 x
d−1
2 · · · x2
... ... ...
xd
d xd−1
d · · · xd
 





 





 cd
cd−1
...
c1
 




 .

Example 3.22 (Reeve’s tetrahedron). Let Th be the tetrahedron with
vertices (0, 0, 0), (1, 0, 0), (0, 1, 0), and (1, 1, h), where h is a positive integer
(see Figure 3.7).

3.7 Interpolation 79

T h 2 T h
 y

z
 x
 (2 ; 2 ; 2 h )

(1 ; 1 ; h )
 Fig. 3.7 Reeve’s tetrahedron Th (and 2Th).

To interpolate the Ehrhart polynomial LTh(t) from its values at various
points, we use Figure 3.7 to deduce the following:

4 = LTh (1) = vol (Th) + c2 + c1 + 1 ,

h + 9 = LTh (2) = vol (Th) · 2
3 + c2 · 2
2 + c1 · 2 + 1 .

Using the volume formula for a pyramid, we know that

vol (Th) = 1
3 (base area)(height) = h
6 .

Thus h + 1 = h + 2c2 − 1, which gives us c2 = 1 and c1 = 2 − h
6 . Therefore,

LTh (t) = h
6 t3 + t2 + (2 − h
6
 ) t + 1 . ⊓⊔

80 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

3.8 Rational Polytopes and Ehrhart Quasipolynomials

We do not have to change much to study lattice-point enumeration for rational
polytopes, and most of this section will consist of exercises for the reader. The
structural result paralleling Theorem 3.8 is as follows.

Theorem 3.23 (Ehrhart’s theorem for rational polytopes). If P is a
rational convex d-polytope, then LP (t) is a quasipolynomial in t of degree d. Its
period divides the least common multiple of the denominators of the coordinates
of the vertices of P.

We will call the least common multiple of the denominators of the co-
ordinates of the vertices of P the denominator of P. Theorem 3.23, also
due to Ehrhart, extends Theorem 3.8, because the denominator of an inte-
gral polytope P is 1. Exercises 3.26 and 3.27 show that the word divides in
Theorem 3.23 is far from being replaceable by equals.
We set out along the path toward a proof of Theorem 3.23 by stating the
analogue of Lemma 3.9 for quasipolynomials (see Exercise 3.24):

Lemma 3.24. If ∑

t≥0 f (t) zt = g(z)
h(z) ,

then f is a quasipolynomial of degree d with period dividing p if and only if g
and h are polynomials such that deg(g) < deg(h), all roots of h are p
th roots
of unity of multiplicity at most d + 1, and there is a root of multiplicity equal
to d + 1 (all of this assuming that g
h has been reduced to lowest terms). ⊓⊔

Our goal is now evident: we will prove that if P is a rational convex
d-polytope with denominator p, then

EhrP (z) = 1 + ∑

t≥1 LP (t) zt = g(z)

(1 − zp)d+1 ,

for some polynomial g of degree less than p(d + 1). As in Section 3.4, we will
have to prove this only for the case of a rational simplex. So suppose the
d-simplex ∆ has vertices v1, v2, . . . , vd+1 ∈ Qd, and the denominator of ∆ is
p. Again we will cone over ∆: let

w1 = (v1, 1) , w2 = (v2, 1) , . . . , wd+1 = (vd+1, 1) ;

then

cone(∆) = {λ1w1 + λ2w2 + · · · + λd+1wd+1 : λ1, λ2, . . . , λd+1 ≥ 0} ⊂ Rd+1.

To be able to use Theorem 3.5, we ﬁrst have to ensure that we have a
description of cone(∆) with integral generators. But since the denominator of

Notes 81

∆ is p, we can replace each generator wk by pwk ∈ Z
d+1, and we are ready
to apply Theorem 3.5. From this point, the proof of Theorem 3.23 proceeds
exactly like that of Theorem 3.8, and we invite the reader to ﬁnish it up
(Exercise 3.25).
Although the proofs of Theorem 3.23 and Theorem 3.8 are almost identical,
the arithmetic structure of Ehrhart quasipolynomials is much more subtle
and less well known than that of Ehrhart polynomials.

3.9 Reﬂections on the Coin-Exchange Problem and the
Gallery of Chapter 2

At this point, we encourage the reader to look back at the ﬁrst two chapters
in light of the basic Ehrhart-theory results. Theorem 1.5 and its higher-
dimensional analogue give a special set of Ehrhart quasipolynomials. On the
other hand, in Chapter 2 we encountered many integral polytopes. Ehrhart’s
theorem (Theorem 3.8) explains why their lattice-point enumeration functions
were all polynomials.

Notes

1. Triangulations of polytopes and manifolds are an active source of research
with many interesting open problems; for further study, we highly recom-
mend [99].

2. Eug`ene Ehrhart laid the foundation for the central theme of this book in
the 1960s, starting with the proof of Theorem 3.8 in 1962 [110]. The proof
we give here follows Ehrhart’s original lines of thought. An interesting fact
is that he did his most beautiful work as a teacher at a lyc´ee in Strasbourg
(France), receiving his doctorate at age 60 on the urging of some colleagues.

3. Given any d linearly independent vectors w1, w2, . . . , wd ∈ Rd, the lat-
tice generated by them is the set of all integer linear combinations of
w1, w2, . . . , wd. Alternatively, one can deﬁne a lattice as a discrete subgroup
of Rd, and these two notions can be shown to be equivalent. One might wonder
whether replacing the lattice Z
d by an arbitrary lattice L throughout the
statements of the theorems—requiring now that the vertices of a polytope be
in L—gives us any diﬀerent results. The fact that the theorems of this chapter
remain the same follows from the observation that every d-dimensional lattice
can be mapped to Z
d by an invertible linear transformation.

82 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

4. Richard Stanley developed much of the theory of Ehrhart (quasi)polyno-
mials, initially from a commutative-algebra point of view. Theorem 3.12 is
due to him [227]. The proof we give here appeared in [47]. We will give several
extensions of Theorem 3.12 in Chapter 10.

5. The tetrahedron Th of Example 3.22 was used by John Reeve to show that
Pick’s theorem does not hold in R3 (see Exercise 3.23) [203]. Incidentally, the
formula for LTh also proves that the coeﬃcients of an Ehrhart polynomial are
not always positive.

6. There are several interesting questions (some of which are still open)
regarding the periods of Ehrhart quasipolynomials. Some particularly nice
examples about what can happen with periods were given by Tyrrell McAllister
and Kevin Woods [170].

7. Most of the results remain true if we replace convex polytope by polytopal
complex, which is a ﬁnite union of polytopes. One important exception is
Corollary 3.15: the constant term of an “Ehrhart polynomial” of an integral
polytopal complex C is the Euler characteristic of C.

8. The reader might wonder why we do not discuss polytopes with irrational
vertices. The answer is simple: nobody has yet found a theory that would
parallel the results in this chapter, even in dimension 2. One notable exception
is [20], in which irrational extensions of Brion’s theorem are given; we will
study the rational case of Brion’s theorem in Chapter 11. On the other hand,
there has been recent activity to study Ehrhart quasipolynomials of rational
polytopes with real dilation parameters [14, 165]. Ehrhart theory has been
extended to functions other than strict lattice-point counting; one instance is
described in Chapter 13.

Exercises

3.1. Show that the number of triangulations of a polygon P that uses only
the n vertices of P equals 1
n−1 (2n−4
n−2 ).
2

3.2. To each permutation π ∈ Sd on d elements, we associate the simplex

∆π := conv {0, eπ(1), eπ(1) + eπ(2), . . . , eπ(1) + eπ(2) + · · · + eπ(d)} ,

where e1, e2, . . . , ed denote the unit vectors in Rd.

(a) Prove that {∆π : π ∈ Sd} is a triangulation of the unit d-cube [0, 1]d.

2 The integer 1
n+1 (
2n
n ) is known as the nth Catalan number.

Exercises 83

(b) Prove that all ∆π are congruent to each other, that is, each one can be
obtained from any other by reﬂections, translations, and rotations.
(c) Show that for all π ∈ Sd, L∆π (t) = (d+t
d ).

3.3. ♣ Given the polytope P ⊆ Rd, construct a lifted polytope Q as in (3.1).

(a) Let F be a lower face of Q. Show that one can ﬁnd a supporting hyper-
plane H = {x ∈ Rd+1 : a · x = b} with ad+1 ̸= 0. (This means that the
hyperplane is not vertical.)
(b) Let F be a face of Q. Prove that F is a lower face if and only if one can
ﬁnd a supporting hyperplane H = {x ∈ Rd+1 : a · x = b} with ad+1 > 0.
(c) Let F1 and F2 be lower faces of Q. Prove that π(F1) ∩ π(F2) is a face
common to both π(F1) and π(F2).

3.4. Prove that every triangulation of a polygon P that uses only the vertices
of P is regular. Give an example of a (3-dimensional) polytope that has a
nonregular triangulation. (Hint: Begin by proving that the triangulation of
the 2-dimensional point conﬁguration pictured in Figure 3.8 is not regular.
3)

Fig. 3.8 A nonregular
triangulation of a point
conﬁguration. s
 s

s
 s
ss

3.5. ♣ Suppose T is a triangulation of a pointed cone. Prove that the inter-
section of two simplicial cones in T is again a simplicial cone.

3.6. Find the generating function σK(z) for the following cones:

(a) K = {λ1(0, 1) + λ2(1, 0) : λ1, λ2 ≥ 0} ;
(b) K = {λ1(0, 1) + λ2(1, 1) : λ1, λ2 ≥ 0} ;
(c) K = {(3, 4) + λ1(0, 1) + λ2(2, 1) : λ1, λ2 ≥ 0} .

3.7. Fix two relatively prime positive integers a and b, and let

K = {λ1(0, 1) + λ2(a, b) : λ1, λ2 ≥ 0} .

Show that
 σK(z1, z2) = 1 + ∑a−1
k=1 zk
1 z⌊ kb
a ⌋+1
2
(1 − z2) (1 − za
1 zb
2) .

3 A triangulation of a point conﬁguration {x1, x2, . . . , xn} is a triangulation of
conv {x1, x2, . . . , xn} using x1, x2, . . . , xn as vertices.

84 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

3.8. ♣ Let S ⊆ Rm and T ⊆ Rn. Show that σS×T (z1, z2, . . . , zm+n) =
σS (z1, z2, . . . , zm) σT (zm+1, zm+2, . . . , zm+n) .

3.9. ♣ Let K be a rational d-cone, and let m ∈ Z
d. Show that σm+K(z) =
zmσK(z).

3.10. ♣ For a set S ⊂ Rd, let −S := {−x : x ∈ S}. Prove that

σ−S (z1, z2, . . . , zd) = σS
 ( 1
z1 , 1
z2 , . . . , 1
zd
 ) .

3.11. Given a pointed cone K ⊂ Rd with apex at the origin, let S := K ∩ Z
d.
Show that if x, y ∈ S, then x + y ∈ S. (In algebraic terms, S is a semigroup,
since 0 ∈ S and associativity of the addition in S follows trivially from
associativity in Rd.)

3.12. Suppose K ⊂ Rd is a pointed cone with apex v, H is a supporting
hyperplane of K with H ∩ K = {v}, and w ∈ Rd is such that v + w ∈ K.
Show that (H + w) ∩ K is a convex polytope.

3.13. ♣ Prove Lemma 3.9: If

∑

t≥0 f (t) zt = g(z)
(1 − z)d+1 ,

then f is a polynomial of degree d if and only if g is a polynomial of degree
at most d and g(1) ̸= 0.

3.14. Prove that (x+n
n ), (x+n−1
n ), . . . , (x
n
) is a basis for the vector space Poln
of polynomials (in the variable x) of degree less than or equal to n.

3.15. For a polynomial p(t) = cdtd + cd−1td−1 + · · · + c0, let Hp(z) be deﬁned
by ∑

t≥0 p(t) zt = Hp(z)
(1 − z)d+1 .

Consider the map φd : Pold → Pold given by p ↦→ Hp.

(a) Show that φd is a linear transformation.
(b) Compute the matrix describing φd for d = 0, 1, 2, . . . .
(c) Deduce formulas for h∗
2, h
∗
3, . . . , similar to the one in Corollary 3.16.

3.16. Compute the Ehrhart polynomials and the Ehrhart series of the sim-
plices with the following vertices:

(a) (0, 0, 0), (1, 0, 0), (0, 2, 0), and (0, 0, 3);
(b) (0, 0, 0, 0), (1, 0, 0, 0), (0, 2, 0, 0), (0, 0, 3, 0), and (0, 0, 0, 4).

Exercises 85

3.17. Deﬁne the hypersimplex ∆(d, k) as the convex hull of

{ej1 + ej2 + · · · + ejk : 1 ≤ j1 < j2 < · · · < jk ≤ d} ,

where e1, e2, . . . , ed are the standard basis vectors in Rd. For example, ∆(d, 1)
and ∆(d, d − 1) are regular (d − 1)-simplices. Compute the Ehrhart polynomial
and the Ehrhart series of ∆(d, k).

3.18. ♣ Suppose H is the hyperplane given by

H = {x ∈ Rd : a1x1 + a2x2 + · · · + adxd = 0
}

for some a1, a2, . . . , ad ∈ Z, which we may assume to have no common factor.
Prove that there exists v ∈ Z
d such that ⋃
n∈Z ((nv + H) ∩ Z
d) = Z
d. (This
implies, in particular, that the points in Z
d \ H are all at least some minimal
distance from H; this minimal distance is essentially given by the dot product
of v with (a1, a2, . . . , ad).)

3.19. ♣ A hyperplane H is rational if it can be written in the form

H = {
x ∈ Rd : a1x1 + a2x2 + · · · + adxd = b}

for some a1, a2, . . . , ad, b ∈ Z. A hyperplane arrangement in Rd is a ﬁnite
set of hyperplanes in Rd. Prove that a rational hyperplane arrangement H
can be translated so that no hyperplane contains any integer points.

3.20. The conclusion of the previous exercise can be strengthened: Prove
that a rational hyperplane arrangement H can be translated such that no
hyperplane contains any rational points.

3.21. ♣ Show that

det
 





 xd
1 xd−1
1 · · · x1 1
xd
2 xd−1
2 · · · x2 1
... ... ... ...
xd
d+1 xd−1
d+1 · · · xd+1 1
 




 = ∏

1≤j<k≤d+1 (xj − xk) .

Conclude that for distinct numbers x1, x2, . . . , xd+1, the matrix

V =
 





 xd
1 xd−1
1 · · · x1 1
xd
2 xd−1
2 · · · x2 1
... ... ... ...
xd
d+1 xd−1
d+1 · · · xd+1 1
 






is not singular. (V is known as the Vandermonde matrix.)

3.22. Let P be an integral d-polytope. Show that

86 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

vol P = 1
d!
 (

(−1)d +
 d∑

k=1
 (d
k
)
(−1)
d−kLP (k)

)
 .

3.23. As in Example 3.22, let Tn be the tetrahedron with vertices (0, 0, 0),
(1, 0, 0), (0, 1, 0), and (1, 1, n), where n is a positive integer. Show that the
volume of Tn is unbounded as n → ∞, yet for all n, Tn has no interior
and precisely four boundary lattice points. This example proves that Pick’s
theorem does not hold for a 3-dimensional integral polytope P, in the sense
that there is no linear relationship among vol P, LP (1), and LP ◦ (1).

3.24. ♣ Prove Lemma 3.24: If

∑

t≥0 f (t) zt = g(z)
h(z) ,

then f is a quasipolynomial of degree d with period dividing p if and only if g
and h are polynomials such that deg(g) < deg(h), all roots of h are p
th roots
of unity of multiplicity at most d + 1, and there is a root of multiplicity equal
to d + 1 (all of this assuming that g
h has been reduced to lowest terms).

3.25. ♣ Provide the details for the proof of Theorem 3.23: If P is a rational
convex d-polytope, then LP (t) is a quasipolynomial in t of degree d. Its period
divides the least common multiple of the denominators of the coordinates of
the vertices of P.

3.26. Let T be the rational triangle with vertices (0, 0), (1, p−1
p ), and (p, 0),

where p is a ﬁxed integer ≥ 2. Show that LT (t) = p−1
2 t2 + p+1
2 t + 1; in
particular, LT is a polynomial.

3.27. Prove that for every d ≥ 2 and p ≥ 1, there exists a d-polytope P whose
Ehrhart quasipolynomial is a polynomial (i.e., it has period 1), yet P has a
vertex with denominator p.

3.28. Prove that the period of the Ehrhart quasipolynomial of a 1-dimensional
polytope is always equal to the least common multiple of the denominators
of its vertices.

3.29. Let T be the triangle with vertices (− 1
2 , − 1
2 ), ( 1
2 , − 1
2 ), and (0, 3
2 ). Show
that LT (t) = t2 + c(t) t + 1, where

c(t) =
 {
1 if t is even,
0 if t is odd.

(This shows that the periods of the “coeﬃcients” of an Ehrhart quasipolyno-
mial do not necessarily increase with decreasing power.) Find the Ehrhart
series of T .

Exercises 87

3.30. Prove the following extension of Theorem 3.12: Suppose P is a rational
d-polytope with denominator p. Then

EhrP (z) = h
∗(z)

(1 − zp)
d+1 ,

where h
∗(z) is a polynomial with nonnegative integral coeﬃcients.

3.31. Find and prove a statement that extends Lemma 3.14 to Ehrhart
quasipolynomials.

3.32. ♣ Prove the following extension of Corollary 3.15 to rational polytopes.
Namely, the Ehrhart quasipolynomial LP of the rational convex polytope
P ⊂ Rd satisﬁes LP (0) = 1.

3.33. Prove the following analogue of Corollary 3.17 for rational polytopes:
Suppose P is a rational polytope with Ehrhart quasipolynomial LP (t) =
cd(t) td + cd−1(t) td−1 + · · · + c1(t) t + c0(t). Then for all t ∈ Z and 0 ≤ k ≤ d,
we have d! ck(t) ∈ Z.

3.34. ♣ Prove that Corollary 3.20 also holds for rational polytopes: Suppose
P ⊂ Rd is a rational convex d-polytope with Ehrhart quasipolynomial cd(t) td+
cd−1(t) td−1 + · · · + c0(t). Then cd(t) equals the volume of P; in particular,
cd(t) is constant.

3.35. Suppose P is a rational convex polytope. Show that as rational functions,

Ehr2P (z) = 1
2 (EhrP (√z) + EhrP (−√z)) .

3.36. Suppose f and g are quasipolynomials. Prove that the convolution

F (t) :=
 t∑

s=0 f (s) g(t − s)

is also a quasipolynomial. What can you say about the degree and the period
of F , given the degrees and periods of f and g?

3.37. Given two positive integers a and b, let

f (t) :=
 {1 if a|t,
0 otherwise, and g(t) :=
 {1 if b|t,
0 otherwise.

Form the convolution of f and g. What function is it?

3.38. Suppose P ⊂ Rm and Q ⊂ Rn are rational polytopes. Prove that the
convolution of LP and LQ equals the Ehrhart quasipolynomial of the polytope
given by the convex hull of P × {0n} × {0} and {0m} × Q × {1}. Here 0d
denotes the origin in Rd.

88 3 Counting Lattice Points in Polytopes: The Ehrhart Theory

3.39. We deﬁne the unimodular group SLd (Z) as the set of all d × d
matrices with integer entries and determinant ±1.

(a) Show that each element of SLd (Z) acts on the integer lattice Z
d in a
bijective fashion.
(b) Let P be an integral polytope, and let Q := A (P), where A ∈ SLd (Z),
so that P and Q are unimodular images of each other. Show that LP (t) =
LQ(t).

3.40. Search on the Internet for the program LattE: Lattice-Point Enumera-
tion [95, 155]. You can download it for free. Experiment.

Open Problems

3.41. How many triangulations are there for a given polytope?

3.42. What is the minimal number of simplices needed to triangulate the unit
d-cube? (These numbers are known for d ≤ 7.)

3.43. Classify the polynomials of a ﬁxed degree d that are Ehrhart polynomials.
This has been done completely for d = 2 [215] and is partially known for d = 3
and 4 [37, Section 3]. (See also Open Problem 10.21.)

3.44. Study the roots of Ehrhart polynomials of integral polytopes in a ﬁxed
dimension [37, 56, 63, 132]. Study the roots of the numerators of Ehrhart series.

3.45. Come up with an eﬃcient algorithm that computes the period of an
Ehrhart quasipolynomial. (See [254], in which Woods describes an eﬃcient
algorithm that checks whether a given integer is a period of an Ehrhart
quasipolynomial.)

3.46. Suppose P and Q are integral polytopes with the same Ehrhart poly-
nomial, that is, LP (t) = LQ(t). What additional conditions on P and Q do
we need to ensure that integer translates of P and Q are unimodular images
of each other? That is, when is Q = A(P) + m for some A ∈ SLd (Z) and
m ∈ Z
d?

3.47. Find an “Ehrhart theory” for irrational polytopes.

Chapter 4
Reciprocity

In mathematics you don’t understand things. You just get used to them.

John von Neumann (1903–1957)

While Exercise 1.4(i) gave us the elementary identity
⌊ t − 1
a
 ⌋ = − ⌊ −t
a
 ⌋ − 1 (4.1)

for t ∈ Z and a ∈ Z>0, this fact is a special instance of a more general theme.
Namely, (4.1) marks the simplest (1-dimensional) case of a reciprocity theorem
that is central to Ehrhart theory. Let I := [
0, 1
a ] ⊂ R, a rational 1-polytope

0 t
a

Fig. 4.1 Lattice points in t I.

(see Figure 4.1). Its discrete volume is (recalling Exercise 1.3)

LI(t) = ⌊ t
a
 ⌋ + 1 .

The lattice-point enumerator for the interior I ◦ = (0, 1
a ), on the other hand,
is
 LI◦ (t) = ⌊ t − 1
a
 ⌋ (4.2)

89

90 4 Reciprocity

(see Exercise 4.1). We remind the reader that both LI(t) and LI◦(t), by
deﬁnition, are functions in the positive-integer variable t. However, we can
see in the above formulas that they are given by quasipolynomials, and (4.1)
gives an algebraic relation between these two quasipolynomials:

LI◦ (t) = −LI(−t) .

This chapter is devoted to proving that a similar identity holds for rational
polytopes in any dimension:

Theorem 4.1 (Ehrhart–Macdonald reciprocity). Suppose P is a convex
rational polytope. Then the evaluation of the quasipolynomial LP at negative
integers yields LP (−t) = (−1)
dim P LP ◦ (t) .

This theorem belongs to a class of famous reciprocity theorems. A common
theme in combinatorics is to begin with an interesting object P , and

1. deﬁne a counting function f (t) attached to P that makes physical sense
for positive integer values of t;
2. recognize the function f as a polynomial in t;
3. substitute negative integral values of t into the counting function f , and
recognize f (−t) as a counting function of a new mathematical object Q.

For us, P is a polytope, and Q is its interior.

4.1 Generating Functions for Somewhat Irrational
Cones

Our approach to proving Theorem 4.1 parallels the steps of Chapter 3: we
deduce Theorem 4.1 from an identity for rational cones. We begin with a
reciprocity theorem for simplicial cones.

Theorem 4.2. Fix linearly independent vectors w1, w2, . . . , wd ∈ Z
d, and
let K = {λ1w1 + λ2w2 + · · · + λdwd : λ1, . . . , λd ≥ 0}, the simplicial cone
generated by the wj. Then for those v ∈ Rd for which the boundary of the
shifted simplicial cone v + K contains no integer point,

σv+K
 ( 1
z1 , 1
z2 , . . . , 1
zd
 ) = (−1)d σ−v+K (z1, z2, . . . , zd) .

Remark. This theorem is meaningless on the level of formal power series;
however, the identity holds at the level of rational functions. We will establish
that σv+K is a rational function in the process of proving the theorem.

Proof. As in the proofs of Theorem 3.5 and Corollary 3.6,

4.1 Generating Functions for Somewhat Irrational Cones 91

σv+K(z) = σv+Π(z)
(1 − zw1) (1 − zw2) · · · (1 − zwd ) ,

where Π is the open parallelepiped

Π = {λ1w1 + λ2w2 + · · · + λdwd : 0 < λ1, λ2, . . . , λd < 1} . (4.3)

This also proves that σv+K is a rational function. Note that by assumption,
v + Π contains no integer points on its boundary. Naturally,

σ−v+K(z) = σ−v+Π(z)
(1 − zw1) (1 − zw2 ) · · · (1 − zwd ) ,

so we need to relate the parallelepipeds v + Π and −v + Π. This relation is
illustrated in Figure 4.2 for the case d = 2; the identity for general d is (see
Exercise 4.2)
 v + Π = −(−v + Π) + w1 + w2 + · · · + wd . (4.4)

Now we translate the geometry of (4.4) into generating functions:

w 1

w 2

v

v + 

  v +    (   v + )   (   v + ) + w 1 + w 2

Fig. 4.2 From −v + Π to v + Π.

92 4 Reciprocity

σv+Π(z) = σ−(−v+Π)(z) zw1 zw2 · · · zwd

= σ−v+Π ( 1
z1 , 1
z2 , . . . , 1
zd
 ) zw1zw2 · · · zwd

(the last equation follows from Exercise 3.10). Let’s abbreviate the vector( 1
z1 , 1
z2 , . . . , 1
zd
 ) by 1
z . Then the last identity is equivalent to

σv+Π
 ( 1
z
 ) = σ−v+Π(z) z−w1z−w2 · · · z−wd ,

whence
 σv+K
 ( 1
z
 ) = σv+Π ( 1
z )

(1 − z−w1) (1 − z−w2) · · · (1 − z−wd )

= σ−v+Π(z) z−w1z−w2 · · · z−wd

(1 − z−w1) (1 − z−w2) · · · (1 − z−wd )

= σ−v+Π(z)
(zw1 − 1) (zw2 − 1) · · · (zwd − 1)

= (−1)
d σ−v+Π(z)
(1 − zw1) (1 − zw2) · · · (1 − zwd )

= (−1)
d σ−v+K(z) . ⊓⊔

4.2 Stanley’s Reciprocity Theorem for Rational Cones

For the general reciprocity theorem for cones, we patch the simplicial cones
of a triangulation together, in a manner very similar to what we did in our
proof of Theorem 3.12.

Theorem 4.3 (Stanley reciprocity). Suppose K is a rational d-cone with
the origin as apex. Then

σK
 ( 1
z1 , 1
z2 , . . . , 1
zd
 ) = (−1)d σK◦ (z1, z2, . . . , zd) .

Proof. Triangulate K into simplicial cones K1, K2, . . . , Km. Exercise 3.19 en-
sures that there exists a vector v ∈ Rd such that the shifted cone v + K
contains exactly the interior lattice points of K,

K◦ ∩ Z
d = (v + K) ∩ Z
d, (4.5)

and there are no boundary lattice points on any of the triangulation cones:

∂ (v + Kj) ∩ Z
d = ∅ for all j = 1, . . . , m, (4.6)

4.3 Ehrhart–Macdonald Reciprocity for Rational Polytopes 93

as well as ∂ (−v + Kj) ∩ Z
d = ∅ for all j = 1, . . . , m. (4.7)

We invite the reader (Exercise 4.4) to realize that (4.5)–(4.7) imply

K ∩ Z
d = (−v + K) ∩ Z
d. (4.8)

Now by Theorem 4.2,

σK ( 1
z ) = σ−v+K ( 1
z ) =
 m∑

j=1 σ−v+Kj ( 1
z ) =
 m∑

j=1(−1)d σv+Kj (z)

= (−1)d σv+K (z) = (−1)
d σK◦ (z) .

Note that the second and fourth equalities are true because of the validity
of (4.7) and (4.6), respectively. ⊓⊔

4.3 Ehrhart–Macdonald Reciprocity for Rational
Polytopes

In preparation for the proof of Theorem 4.1, we deﬁne the Ehrhart series
for the interior of the rational polytope P as

EhrP ◦ (z) := ∑

t≥1 LP ◦ (t) zt.

Our convention of beginning the series with t = 1 stems from the fact that
this generating function is a special evaluation of the integer-point transform
of the open cone (cone(P))◦: much in sync with Lemma 3.10,

EhrP ◦ (z) = σ(cone(P))◦ (1, 1, . . . , 1, z) . (4.9)

We are now ready to prove the Ehrhart-series analogue of Theorem 4.1.

Theorem 4.4. Suppose P is a convex rational polytope. Then the evaluation
of the rational function EhrP at 1
z yields

EhrP
 ( 1
z
 ) = (−1)
dim P+1 EhrP ◦ (z) .

Proof. Suppose P is a d-polytope. We recall Lemma 3.10, which states that
the generating function of the Ehrhart polynomial of P is an evaluation of
the generating function of cone(P):

EhrP (z) = ∑

t≥0 LP (t) zt = σcone(P) (1, 1, . . . , 1, z) .

94 4 Reciprocity

Equation (4.9) gives the analogous evaluation of σ(cone(P))◦ that yields EhrP ◦ .
Now we apply Theorem 4.3 to the (d + 1)-cone K = cone(P):

σ(cone(P))
◦ (1, 1, . . . , 1, z) = (−1)
d+1 σcone(P) (1, 1, . . . , 1, 1
z ) . ⊓⊔

Theorem 4.1 now follows like a breeze.

Proof of Ehrhart–Macdonald reciprocity (Theorem 4.1). We ﬁrst apply Exer-
cise 4.7 to the Ehrhart series of P: namely, as rational functions,

EhrP
 ( 1
z
 ) = ∑

t≤0 LP (−t) zt = − ∑

t≥1 LP (−t) zt.

Now we combine this identity with Theorem 4.4 to obtain

∑

t≥1 LP ◦ (t) zt = (−1)
d+1 EhrP
 ( 1
z
 ) = (−1)d ∑

t≥1 LP (−t) zt.

Comparing the coeﬃcients of the two power series yields the reciprocity
theorem. ⊓⊔

With Ehrhart–Macdonald reciprocity, we can now restate Theorem 3.18 in
terms of Ehrhart polynomials:

Theorem 4.5. Suppose P is an integral d-polytope with Ehrhart series

EhrP (z) = h
∗
d zd + h
∗
d−1 zd−1 + · · · + h
∗
1 z + 1
(1 − z)d+1 .

Then h
∗
d = h∗
d−1 = · · · = h
∗
k+1 = 0 and h
∗
k ̸= 0 if and only if (d − k + 1)P is
the smallest integer dilate of P that contains an interior lattice point.

Proof. Theorem 3.18 says that h
∗
k is the highest nonzero coeﬃcient if and only
if LP (−1) = LP (−2) = · · · = LP (−(d − k)) = 0 and LP (−(d − k + 1)) ̸= 0.
Now use Ehrhart–Macdonald reciprocity (Theorem 4.1). ⊓⊔

The largest k for which h
∗
k ̸= 0 is called the degree of P. The above
theorem says that the degree of P is k precisely if (d − k + 1)P is the smallest
integer dilate of P that contains an interior lattice point.

4.4 The Ehrhart Series of Reﬂexive Polytopes

As an application of Theorem 4.4, we now study a special class of integral
polytopes whose Ehrhart series have an additional symmetry structure. We
call a polytope P reﬂexive if it is integral and has the hyperplane description

4.4 The Ehrhart Series of Reﬂexive Polytopes 95

P = {x ∈ Rd : A x ≤ 1
} ,

where A is an integral matrix. (Here 1 denotes a vector all of whose coordinates
are 1.) The following theorem gives a characterization of reﬂexive polytopes
through their Ehrhart series.

Theorem 4.6 (Hibi’s palindromic theorem). Suppose P is an integral
d-polytope that contains the origin in its interior and that has the Ehrhart
series
 EhrP (z) = h
∗
d zd + h
∗
d−1 zd−1 + · · · + h
∗
1 z + h
∗
0
(1 − z)d+1 .

Then P is reﬂexive if and only if h
∗
k = h∗
d−k for all 0 ≤ k ≤ d
2 .

The two main ingredients for the proof of this result are Theorem 4.4 and
the following:

Lemma 4.7. Suppose a1, a2, . . . , ad, b ∈ Z satisfy gcd (a1, a2, . . . , ad, b) = 1
and b > 1. Then there exist positive integers c and t such that tb < c < (t + 1)b
and {(m1, m2, . . . , md) ∈ Z
d : a1m1 + a2m2 + · · · + admd = c
} ̸= ∅.

Proof. Let g = gcd (a1, a2, . . . , ad); by our assumption, gcd(g, b) = 1, so one
can ﬁnd integers k and t such that

kg − tb = 1 . (4.10)

Furthermore, we can choose k and t in such a way that t > 0. Let c = kg;
Equation (4.10) and the condition b > 1 imply that tb < c < (t + 1)b. Finally,
since g = gcd (a1, a2, . . . , ad), there exist m1, m2, . . . , md ∈ Z such that

a1m1 + a2m2 + · · · + admd = kg = c . ⊓⊔

Proof of Theorem 4.6. We recall that P is reﬂexive if and only if

P = {
x ∈ Rd : A x ≤ 1} for some integral matrix A. (4.11)

We claim that P has such a hyperplane description if and only if

(t + 1)P ◦ ∩ Z
d = tP ∩ Z
d for all t ∈ Z≥0 . (4.12)

This condition means that the only lattice points that we gain in passing from
tP to (t + 1)P are those on the boundary of (t + 1)P. The fact that (4.11)
implies (4.12) is the content of Exercise 4.13. Conversely, if P satisﬁes (4.12),
then there are no lattice points between tH and (t + 1)H for any facet
hyperplane H of P (Exercise 4.14). That is, if a facet hyperplane is given
by H = {x ∈ Rd : a1x1 + a2x2 + · · · + adxd = b}
, where we may assume
gcd (a1, a2, . . . , ad, b) = 1, then
{x ∈ Z
d : tb < a1x1 + a2x2 + · · · + adxd < (t + 1)b
} = ∅ .

96 4 Reciprocity

But then Lemma 4.7 implies that b = 1, and so P has a hyperplane description
of the form (4.11).
Thus we have established that P is reﬂexive if and only if it satisﬁes (4.12).
Now by Theorem 4.4,

EhrP ◦ (z) = (−1)
d+1 EhrP
 ( 1
z
 ) = h
∗
0 zd+1 + h
∗
1 zd + · · · + h
∗
d−1 z2 + h
∗
d z
(1 − z)d+1 .

By condition (4.12), P is reﬂexive if and only if this rational function is equal
to ∑

t≥1 LP (t − 1) zt = z ∑

t≥0 LP (t) zt = z EhrP (z)

= h
∗
d zd+1 + h
∗
d−1 zd + · · · + h
∗
1 z2 + h
∗
0 z
(1 − z)d+1 ,

that is, if and only if h
∗
k = h
∗
d−k for all 0 ≤ k ≤ d
2 . ⊓⊔

4.5 More “Reﬂections” on the Coin-Exchange Problem
and the Gallery of Chapter 2

We have already encountered special cases of Ehrhart–Macdonald reciprocity
several times. Note that Theorem 4.1 allows us to conclude that counting
the number of interior lattice points in a rational polytope is tantamount to
counting lattice points in its closure. Exercises 1.33, 2.1, and 2.7, as well as
part (b) of each theorem in the gallery of Chapter 2, conﬁrm that

LP (−t) = (−1)
dim P LP ◦ (t) .

Notes

1. Ehrhart–Macdonald reciprocity (Theorem 4.1) had been conjectured (and
proved in several special cases) by Eug`ene Ehrhart for about a decade before
I. G. Macdonald found a general proof in 1971 [167]. One can actually relax the
condition of Ehrhart–Macdonald reciprocity: it holds for polytopal complexes
that are homeomorphic to a d-manifold. The proof we give here (including the
proof of Theorem 4.3) appeared in [47]. An attractive alternative approach
was given by Steven Sam [210].

2. Theorem 4.3 is due to Richard Stanley [226], who proved more general
versions of this theorem. The reader might recall that the rational function

Notes 97

representing the Ehrhart series of a rational cone can be thought of as
its meromorphic continuation. Stanley reciprocity (Theorem 4.3) gives a
functional identity for such meromorphic continuations.

3. The term reﬂexive polytope was coined by Victor Batyrev, who found
exciting applications of these polytopes to mirror symmetry in physical string
theory [26]. Batyrev proved that the toric variety XP deﬁned by a reﬂexive
polytope P is Fano, and that every generic hypersurface of XP is Calabi–
Yau. That the Ehrhart series of a reﬂexive polytope exhibits an unexpected
symmetry (Theorem 4.6) was discovered by Takayuki Hibi [136]. Matthew
Fiset and Alexander Kasprzyk proved a version of Theorem 4.6 for rational
polytopes [115]. The number of reﬂexive polytopes in dimension d is known
for d ≤ 4 [157, 158]; for example, there are precisely 16 reﬂexive polytopes in
dimension 2, up to symmetries (see also [1, Sequence A090045]).

4. Reﬂexive polytopes bear some pleasant surprises beyond those mentioned in
Section 4.4. For example, Benjamin Braun [62] proved that if P is reﬂexive and
Q is an integral polytope that contains the origin in its interior, where P and Q
live in orthogonal subspaces of Rd, then the free sum P ⊕ Q := conv (P ∪ Q)
has Ehrhart series
 EhrP⊕Q(z) = (1 − z) EhrP (z) EhrQ(z) , (4.13)

an analogue of sorts to Exercise 2.4; see Exercise 4.17. Another striking result
is that the sum of the numbers of lattice points on the boundaries of a reﬂexive
polygon and its dual is always 12 [138,195]. A similar result holds in dimension
3 (with 12 replaced by 24) [27], but no elementary proof of the latter fact is
known [35, Section 4].

5. There is an equivalent deﬁnition for reﬂexive polytopes: P is reﬂexive if and
only if both P and its dual P ∗ are integral polytopes. The dual polytope of
P (often also called the polar polytope) is deﬁned as

P ∗ := {
x ∈ Rd : x · y ≤ 1 for all y ∈ P} .

The concept of (polar) duality is not conﬁned to polytopes but can be deﬁned
for any nonempty subset of Rd. Duality is a crucial chapter in the theory of
polytopes, and one of its applications is the equivalence of the vertex and
hyperplane description of a polytope. For more about (polar) duality, the
reader might consult [21, Chapter IV].

6. The cross-polytopes 3 from Section 2.5 form a special class of reﬂexive
polytopes. We mentioned in the notes of Chapter 2 that the roots of the
Ehrhart polynomials L3 all have real part − 1
2 [76,149]. Christian Bey, Martin
Henk, and J¨org Wills proved in [56] that if all complex roots of LP (t), for

98 4 Reciprocity

some integral polytope P, have real part − 1
2 , then P is the unimodular image
of a reﬂexive polytope.

7. An integral polytope P ⊂ Rd for which there exists a positive integer k such
that (k −1)P ◦ ∩Z
d = ∅, #(kP ◦ ∩Z
d) = 1 and #(tP ◦ ∩Z
d) = #((t−k)P ∩Z
d)
for all integers t > k is called Gorenstein of index k. Thus reﬂexive polytopes
are Gorenstein of index 1. (Some of the polytopes in Chapters 2 and 6 are
Gorenstein.) Theorem 4.6 can be extended to the statement that an integral
polytope is Gorenstein if and only if its nonzero h
∗
j ’s are symmetric (not
necessarily with center of symmetry d
2 as in the case of reﬂexive polytopes);
see Exercise 4.8.

Exercises

4.1. ♣ Prove (4.2): for a, t ∈ Z>0, L(0, 1
a )(t) = ⌊ t − 1
a
 ⌋.

4.2. ♣ Explain (4.4): if w1, w2, . . . , wd ∈ Rd are linearly independent and

Π = {λ1w1 + λ2w2 + · · · + λdwd : 0 < λ1, λ2, . . . , λd < 1} ,

then v + Π = −(−v + Π) + w1 + w2 + · · · + wd .

4.3. Revisit Exercise 2.15, but now give a one-line proof that the Bernoulli
polynomials satisfy Bd(1 − x) = (−1)dBd(x).

4.4. ♣ Prove that (4.5)–(4.7) imply (4.8); that is, if K is a rational pointed
d-cone with the origin as apex and v ∈ Rd is such that

K◦ ∩ Z
d = (v + K) ∩ Z
d,

∂ (v + Kj) ∩ Z
d = ∅ for all j = 1, . . . , m,

and
 ∂ (−v + Kj) ∩ Z
d = ∅ for all j = 1, . . . , m,

then
 K ∩ Z
d = (−v + K) ∩ Z
d.

4.5. Prove the following generalization of Theorem 4.3 to rational pointed
cones with arbitrary apex: Suppose K is a rational pointed d-cone with the
origin as apex, and v ∈ Rd. Then the integer-point transform σv+K(z) of the
pointed d-cone v + K is a rational function that satisﬁes

Exercises 99

σv+K
 ( 1
z
 ) = (−1)dσ(−v+K)◦ (z) .

4.6. Generalize Theorem 4.3 by showing that we do not need to assume that
K is full dimensional.

4.7. ♣ Suppose Q : Z → C is a quasipolynomial. We know that R+
Q(z) :=
∑

t≥0 Q(t) zt evaluates to a rational function.

(a) Prove that R−
Q(z) := ∑

t<0 Q(t) zt also evaluates to a rational function.
(b) Let Q(t) = 1. Prove that as rational functions, R+
Q(z) + R−
Q(z) = 0.
(c) Suppose Q is a polynomial. Prove that as rational functions, R+
Q(z) +
R−
Q(z) = 0.
(d) Suppose Q is a quasipolynomial. Prove that as rational functions, R+
Q(z) +
R−
Q(z) = 0.

4.8. ♣ Suppose that P is an integral d-polytope for which

LP ◦ (t) = LP (t − k) and LP ◦ (1) = LP ◦ (2) = · · · = LP ◦ (k − 1) = 0

for some integer k (so P is a Gorenstein polytope, as mentioned in the notes).
Prove that
 EhrP
 ( 1
z
 ) = (−1)d+1zk EhrP (z) .

4.9. Suppose P is an integral d-polytope with Ehrhart series

EhrP (z) = h
∗
d zd + h
∗
d−1 zd−1 + · · · + h
∗
1 z + 1
(1 − z)d+1 .

Prove that h
∗
d = LP ◦ (1).

4.10. Suppose P is an integral d-polytope. Show that the dilate (d + 1)P
contains an interior lattice point.

4.11. Suppose P is an integral polytope. Denote the boundary of P by ∂P.
Prove that L∂P (t) is a polynomial that is either even or odd. Determine its
constant term.

4.12. Recall the restricted partition function

p{a1,a2,...,ad}(n) := # {(m1, . . . , md) ∈ Z
d
≥0 : m1a1 + · · · + mdad = n}

from Chapter 1. Prove that as quasipolynomials,

p{a1,a2,...,ad}(−n − a1 − a2 − · · · − ad) = (−1)d−1 p{a1,a2,...,ad}(n)

and that

100 4 Reciprocity

p{a1,a2,...,ad}(−1) = p{a1,a2,...,ad}(−2) = · · ·

= p{a1,a2,...,ad}(−a1 − a2 − · · · − ad + 1) = 0 .

4.13. ♣ Prove that (4.11) implies (4.12), that is, show that if the polytope P
is given by P = {x ∈ Rd : A x ≤ 1
} for an integral matrix A, then

(t + 1)P ◦ ∩ Z
d = tP ∩ Z
d

for all t ∈ Z≥0.

4.14. ♣ Suppose P is an integral polytope that satisﬁes (4.12): P ◦ ∩ Z
d = {0}
and for all t ∈ Z>0, (t + 1)P ◦ ∩ Z
d = tP ∩ Z
d. Then for every t ∈ Z, there are
no lattice points between tH and (t + 1)H for any facet hyperplane H of P.

4.15. Compute the dual polytope of the d-dimensional cross-polytope 3.

4.16. Suppose P ⊂ Rd is an integral d-polytope with 0 ∈ P ◦. Show that its
dual P ∗ is integral if and only if P is of the form {x ∈ Rd : A x ≤ 1
} for
some integral matrix A.

4.17. Prove (4.13): if P is reﬂexive and Q is an integral polytope that contains
the origin in its interior, where P and Q live in orthogonal subspaces of Rd,
then the free sum P ⊕ Q := conv (P ∪ Q) has Ehrhart series

EhrP⊕Q(z) = (1 − z) EhrP (z) EhrQ(z) .

Open Problems

4.18. Suppose P is a 3-dimensional reﬂexive polytope. Denote by e∗ the
edge in the dual polytope P ∗ that corresponds to the edge e in P. Give an
elementary proof that ∑

e edge of P length (e) · length (e∗) = 24 .

4.19. Find the number of reﬂexive polytopes in dimension d ≥ 5.

4.20. Prove Mahler’s conjecture: if K is a d-dimensional centrally symmetric
convex set, then
 vol(K) vol(K∗) ≥ 4
d

d! .

(The right-hand side is the quantity vol(K) vol(K∗) for K = [−1, 1]
d. See [126,
Chapter 9] for further background and references.)

Chapter 5
Face Numbers and the
Dehn–Sommerville Relations in
Ehrhartian Terms

“Data! Data! Data!” he cried, impatiently. “I can’t make bricks without clay.”

Sherlock Holmes (The Adventure of the Copper Beeches, by Arthur Conan Doyle, 1859–
1930)

Our goal in this chapter is twofold, or rather, there is one goal in two diﬀerent
guises. The ﬁrst is to prove a set of fascinating identities, which give linear
relations among the face numbers of a polytope. They are called Dehn–
Sommerville relations, in honor of their discoverers Max Wilhelm Dehn (1878–
1952)
1 and Duncan MacLaren Young Sommerville (1879–1934).
2 Our second
goal is to unify the Dehn–Sommerville relations (Theorem 5.1 below) with
Ehrhart–Macdonald reciprocity (Theorem 4.1).

5.1 Face It!

We denote the number of k-dimensional faces of P by the symbol fk. As k
varies from 0 to d, the face numbers fk encode intrinsic information about
the polytope P. The d-polytope P is simple if each vertex of P lies on
precisely d edges of P.

Theorem 5.1 (Dehn–Sommerville relations). If P is a simple d-polytope
and 0 ≤ k ≤ d, then
 fk =
 k∑

j=0(−1)
j(d − j
d − k
)
fj .

1 For more information about Dehn, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Dehn.html.
2 For more information about Sommerville, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Sommerville.html.
 101

102 5 Face Numbers and the Dehn–Sommerville Relations in Ehrhartian Terms

This theorem takes on a particularly nice form for k = d, namely the
famous Euler relation, which holds for every polytope (not just simple ones).

Theorem 5.2 (Euler relation). If P is a convex d-polytope, then

d∑

j=0(−1)jfj = 1 .

This identity is less trivial than it might look. We give a quick proof
for rational polytopes, for which we can use Ehrhart–Macdonald reciprocity
(Theorem 4.1).

Proof of Theorem 5.2, assuming that P is rational. Let us count the integer
points in tP according to the (relatively) open faces that contain them:
3

LP (t) = ∑

F ⊆P LF ◦ (t) = ∑

F ⊆P(−1)dim F LF (−t) . (5.1)

Here and in the remainder of this chapter, the sums are over all nonempty faces.
(Alternatively, we could agree that L∅(t) = 0.) Note that the ﬁrst equality
in (5.1), while innocent-looking, uses the not entirely trivial Exercise 5.3. The
constant term of LF (t) is 1 for every face F (by Exercise 3.32). Hence the
constant terms of (5.1) give

1 = ∑

F ⊆P(−1)
dim F =
 d∑

j=0(−1)
jfj ,

which proves our claim. ⊓⊔

There is a natural structure on the faces of a polytope P induced by the
containment relation F ⊆ G. This relation gives a partial ordering on the set
of all faces of P, called the face lattice of P.
4 A useful way to illustrate this
partially ordered set is through a directed graph whose nodes correspond to
the faces of P, and we have an edge from F to G if

F ⊂ G and dim G = dim F + 1 .

We draw this directed graph in such a way that the edge directions are upward;
Figure 5.1 shows the face lattice for a triangle. Exercise 2.6 implies that the
face lattice of every simplex is a Boolean lattice, which is the partially
ordered set formed by all subsets of a ﬁnite set, where the partial ordering is
again subset containment.
We already mentioned that we will unify the Dehn–Sommerville relations
(Theorem 5.1) with Ehrhart–Macdonald reciprocity (Theorem 4.1). It is for

3 Note that the relative interior of a vertex is the vertex itself.

4 The use of the word lattice here is disjoint from our previous deﬁnition of the word.

5.2 Dehn–Sommerville Extended 103


v 1
 v 2

v 3
 E 3
E 2
 E 1
 

E 1 E 2 E 3

v 1 v 2 v 3

,

Fig. 5.1 The face lattice of a triangle.

this reason that we will prove Theorem 5.1 only for rational polytopes. To
combine the notions of face numbers and lattice-point enumeration, we deﬁne

Fk(t) := ∑

F ⊆P
dim F =k
 LF (t) ,

the sum being taken over all k-faces of P. By Ehrhart’s theorem (Theo-
rem 3.23), Fk is a quasipolynomial. Since LF (0) = 1 for all F,

Fk(0) = fk ,

the number of k-faces of P. We also remark that the leading coeﬃcient of Fk
measures the relative volume of the k-skeleton of P, that is, the union of all
k-faces; see Section 5.4 for a precise deﬁnition of relative volume.
Our common extension of Theorems 5.1 and 4.1 is the subject of the next
section.

5.2 Dehn–Sommerville Extended

Theorem 5.3. If P is a simple rational d-polytope and 0 ≤ k ≤ d, then

Fk(t) =
 k∑

j=0(−1)j(d − j
d − k
)Fj(−t) .

The classical Dehn–Sommerville equations (Theorem 5.1)—again, only
for rational polytopes—are obtained from the constant terms of the count-
ing functions on both sides of the identity. On the other hand, for k = d,
Theorem 5.3 gives (with t replaced by −t)

104 5 Face Numbers and the Dehn–Sommerville Relations in Ehrhartian Terms

LP (−t) = Fd(−t) =
 d∑

j=0(−1)jFj(t) = (−1)d d∑

j=0(−1)d−jFj(t) .

The sum on the right-hand side is an inclusion–exclusion formula for the
number of lattice points in the interior of tP (count all the points in tP,
subtract the ones on the facets, add back what you have overcounted, etc.),
so in a sense, we recover Ehrhart–Macdonald reciprocity.

Proof. Suppose F is a k-face of P. Then again by counting the integer points
in F according to relatively open faces of F (Exercise 5.3),

LF (t) = ∑

G⊆F LG◦ (t) ,

or by the Ehrhart–Macdonald reciprocity (Theorem 4.1),

LF (t) = ∑

G⊆F(−1)dim GLG(−t) =
 k∑

j=0(−1)
j ∑

G⊆F
dim G=j
 LG(−t) . (5.2)

Now sum both left- and right-hand sides over all k-faces and rearrange the
sum on the right-hand side:

Fk(t) = ∑

F ⊆P
dim F =k
 k∑

j=0(−1)j ∑

G⊆F
dim G=j
 LG(−t)

=
 k∑

j=0(−1)
j ∑

F ⊆P
dim F =k
 ∑

G⊆F
dim G=j
 LG(−t)

=
 k∑

j=0(−1)
j ∑

G⊆P
dim G=j
 fk(P/G)LG(−t)

=
 k∑

j=0(−1)j ∑

G⊆P
dim G=j
 (d − j
d − k
)LG(−t)

=
 k∑

j=0(−1)j(d − j
d − k
)Fj(−t) .

Here fk(P/G) denotes the number of k-faces of P containing a given j-face G
of P. Since P is simple, this number equals (d−j
d−k) (see Exercise 5.5). ⊓⊔

5.3 Applications to the Coeﬃcients of an Ehrhart Polynomial 105

5.3 Applications to the Coeﬃcients of an Ehrhart
Polynomial

We will now apply Theorem 5.3 to the computation of the Ehrhart polynomial
of an integral d-polytope P. The only face-lattice-point enumerator involving
the face P is Fd(t), for which Theorem 5.3 specializes to

LP (t) = Fd(t) =
 d∑

j=0(−1)jFj(−t) .

In fact, we do not have to assume that P is simple, since this identity simply
counts integer points by faces. (Recall that (−1)jFj(−t) counts the integer
points in the t-dilates of the interior of the j-faces.)5 The last term on the
right-hand side is
 (−1)dFd(−t) = (−1)dLP (−t) = LP ◦ (t)

by Ehrhart–Macdonald reciprocity. Shifting this term to the left gives

LP (t) − LP ◦ (t) =
 d−1∑

j=0(−1)
jFj(−t) . (5.3)

The diﬀerence on the left-hand side of this identity has a natural interpretation:
it counts the integer points on the boundary of tP. (And in fact, the right-hand
side is once more an inclusion–exclusion formula for this number.) Let us
write LP (t) = cd t
d + cd−1 t
d−1 + · · · + c0. Then LP ◦(t) = cd td − cd−1 t
d−1 +
· · · + (−1)dc0, so that

LP (t) − LP ◦ (t) = 2cd−1 td−1 + 2cd−3 td−3 + · · · ,

where this sum ends with 2c0 if d is odd and 2c1t if d is even (this should
look familiar; see Exercise 4.11). Combining this expression with (5.3) yields
the following useful result.

Theorem 5.4. Suppose LP (t) = cd t
d + cd−1 td−1 + · · · + c0 is the Ehrhart
polynomial of P. Then

cd−1 td−1 + cd−3 t
d−3 + · · · = 1
2
 d−1∑

j=0(−1)jFj(−t) . ⊓⊔

We can make the statement of this theorem more precise (but also messier)
by writing

5 So one might argue that we did not need the Dehn–Sommerville machinery for the
computations in the current section. This argument is correct, although Theorem 5.3 is a
strong motivation.

106 5 Face Numbers and the Dehn–Sommerville Relations in Ehrhartian Terms

Fj(t) = ∑

F ⊆P
dim F =j
 LF (t) = cj,j tj + cj,j−1tj−1 + · · · + cj,0 .

Then collecting the coeﬃcients of t
k in Theorem 5.4 yields the following
relations.

Corollary 5.5. If k and d are of diﬀerent parities, then

ck = 1
2
 d−1∑

j=0(−1)j+kcj,k . ⊓⊔

If k and d have the same parity, then the left-hand side has to be replaced
by 0.
The ﬁrst coeﬃcient ck in the Ehrhart polynomial of a d-polytope P satisfy-
ing the parity condition is cd−1. In this case, Corollary 5.5 tells us that cd−1
equals 1
2 times the sum of the leading coeﬃcients of the Ehrhart polynomials
of the facets of P.
The next interesting coeﬃcient is cd−3. For example, if dim P = 4, we can
use Corollary 5.5 to compute c1 entirely from (the linear coeﬃcients of) the
Ehrhart polynomials of the faces of dimension ≤ 3.

x

y
 Fig. 5.2 The line segment from (0, 0) to (4, 2) and its aﬃne sublattice.

5.4 Relative Volume

It is time to return to continuous volume. Recall Lemma 3.19: if S ⊂ Rd

is d-dimensional, then vol S = limt→∞ 1
td · # (tS ∩ Z
d). Back in Chapter 3,
we stressed the importance of S being d-dimensional, because otherwise
(i.e., S is lower-dimensional although living in d-space), by our deﬁnition,
vol S = 0. However, the case that S ⊂ Rd is not of dimension d is often very

5.4 Relative Volume 107

interesting; an example is the polytope P that we encountered in connection
with the coin-exchange problem in Chapter 1. We still would like to compute
the volume of such objects, in the relative sense. This makes for a slight
complication. Let us say S ⊂ Rd is of dimension m < d, and let span S =
{x + λ(y − x) : x, y ∈ S, λ ∈ R}, the aﬃne span of S. If we follow the same
procedure as above (counting boxes or grid points), we compute the volume
relative to the sublattice (span S) ∩ Z
d; we call this the relative volume
of S.
For example, the line segment L from (0, 0) to (4, 2) in R2 has the relative
volume 2, because in span L = {
(x, y) ∈ R2 : y = 1
2 x}
, L is covered by two
segments of “unit length” in this aﬃne subspace, as pictured in Figure 5.2. A
3-dimensional instance that should be reminiscent of Chapter 1 is illustrated
in Figure 5.3.

x

y

z
 5

20

2
 Fig. 5.3 The triangle deﬁned by x
5 + y
20 + z
2 = 1, x ≥ 0, y ≥ 0, z ≥ 0. The shaded region
is a fundamental domain for the sublattice that lies on the aﬃne span of the triangle.

If S ⊆ Rd has full dimension d, the relative volume coincides with the
“full-dimensional” volume. Henceforth, when we write vol S we refer to the

108 5 Face Numbers and the Dehn–Sommerville Relations in Ehrhartian Terms

relative volume of S. With this convention, we can rewrite Lemma 3.19 to
accommodate a set S ⊂ Rd that is m-dimensional: its relative volume can be
computed as
 vol S = lim
t→∞ 1
tm · # (tS ∩ Z
d) .

In the case that # (tS ∩ Z
d) has the special form of a polynomial—for
example, if S is an integral polytope—we can further simplify this theorem.
Suppose P ⊂ Rd is an integral m-polytope with Ehrhart polynomial

LP (t) = cm tm + cm−1 tm−1 + · · · + c1 t + 1 .

Then according to the above discussion, and much in sync with Lemma 3.19,

vol P = lim
t→∞ 1
tm LP (t) = lim
t→∞ cm tm + cm−1 tm−1 + · · · + c1 t + 1
tm = cm .

The relative volume of P is the leading term of the corresponding counting
function LP .
For example, in the previous section we found that Corollary 5.5 implies
that the second leading coeﬃcient cd−1 of the Ehrhart polynomial of the
d-polytope P equals 1
2 times the sum of the leading terms of the Ehrhart
polynomials of the facets of P. The leading term for one facet is simply the
relative volume of that facet:

Theorem 5.6. Suppose LP (t) = cd t
d + cd−1 td−1 + · · · + c0 is the Ehrhart
polynomial of the integral polytope P. Then

cd−1 = 1
2
 ∑

F a facet of P
vol F . ⊓⊔

Notes

1. The Dehn–Sommerville relations (Theorem 5.1) ﬁrst surfaced in the work
of Max Dehn, who proved them in 1905 for dimension 5 [101]. (The Dehn–
Sommerville relations are not that complicated for d ≤ 4; see Exercise 5.4.)
Some two decades later, D. M. Y. Sommerville proved the general case [224].
Theorem 5.1 was neither well known nor much used in the ﬁrst half of
the twentieth century, achieving renown only after its rediscovery by Victor
Klee [151] and its appearance in Branko Gr¨unbaum’s famous and widely
read book [127]. The Dehn–Sommerville relations will play a prominent role
in Chapter 10.

2. The Euler relation (Theorem 5.2) is easy to prove directly for d = 3 (this
case is attributed to Euler), but for higher dimension, one has to be somewhat

Exercises 109

careful, as we already remarked in the text. The classical proof for general
d was found in 1852 by Ludwig Schl¨aﬂi [212], although it (like numerous
later proofs) assumes that the boundary of a convex polytope can be built up
inductively in a “good” way. This nontrivial fact—which is called shelling of a
polytope—was proved by Heinz Bruggesser and Peter Mani in 1971 [72]. (One
instance of a shelling will be the subject of Exercise 10.16.) Shellability is
nicely discussed in [259, Lecture 8]. There are short proofs of the Euler relation
that do not use the shelling of a polytope (see, for example, [163, 185, 249]).

3. The reader might suspect that proving Theorems 5.1 and 5.2 for rational
polytopes suﬃces for the general case, since it seems that we can transform a
polytope with irrational vertices slightly to one with only rational vertices
without changing the face structure of the polytope. This is true in our
everyday world, but it fails in dimension ≥ 4 (see [207] for dimension 4
and [259, pp. 172–173] for general dimension).

4. Theorem 5.3 is due to Peter McMullen [172], who, in fact, proved this
result in somewhat greater generality. Another generalization of Theorem 5.3
can be found in [85].

Exercises

5.1. Consider a simple 3-polytope with at least ﬁve facets. Two players play
the following game: each player, in turn, signs his or her name on a previously
unsigned face. The winner is the player who ﬁrst succeeds in signing three
facets that share a common vertex. Show that the player who signs ﬁrst will
always win by playing as well as possible.6

5.2. Show that for the d-cube, fk = 2
d−k(d
k).

5.3. ♣ Given a polytope P, prove that

P = ⋃

F ⊆P F ◦

as a disjoint union over all faces of P, and deduce from this (5.1).

5.4. Give an elementary proof of the Dehn–Sommerville relations (Theo-
rem 5.1) for d ≤ 4.

5.5. ♣ Let P be a simple d-polytope. Prove that the number of k-faces of P
containing a given j-face of P equals (d−j
d−k).

5.6. ♣ Show directly, without using Theorem 5.2, that for a d-simplex,

6 This was one of the 2002 Putnam contest problems.

110 5 Face Numbers and the Dehn–Sommerville Relations in Ehrhartian Terms

(a) fk = (d+1
k+1
);

(b)
 d∑

k=0
(−1)kfk = 1.

5.7. ♣ Prove Theorem 5.1 directly (and hence not requiring P to be an
integral polytope). (Hint: Orient yourself along the proof of Theorem 5.3,
but start with the Euler relation (Theorem 5.2) for a given face F instead
of (5.2).)

5.8. Let F be a face of a simple polytope P. Prove that for 0 ≤ k ≤ d,

∑

G⊇F(−1)dim G(
dim G
k
 ) = (−1)
d (dim F
d − k
 ) .

5.9. ♣ The dual polytope of P (often also called the polar polytope) is
deﬁned as P ∗ := {
x ∈ Rd : x · y ≤ 1 for all y ∈ P} .

(For P ∗ to be a polytope, we need to require that the origin be in the interior
of P; see also the notes at the end of Chapter 4.)

(a) Prove that the face lattice of P ∗ equals the face lattice of P turned upside
down.
(b) Show that P ∗ is simple if and only if P is simplicial, that is, all nontrivial
faces of P are simplices.
(c) Prove the Dehn–Sommerville relations for a simplicial d-polytope: for
0 ≤ k < d,
 fk =
 d−1∑

j=k(−1)d−j−1(j + 1
k + 1
)fj .

This identity also holds for k = −1 if we deﬁne f−1 := 1. (Hint: Try a
proof that is dual to the one hinted at in Exercise 5.7.)

5.10. Show that the equations in Theorem 5.3 are equivalent to the following
identities. If P is a simple lattice d-polytope and k ≤ d, then

k∑

j=0(−1)
k−j(d − j
k − j
)
Fd−j(−t) =
 d∑

i=k(−1)i−k( i
k
)
Fi(t) .

5.11. Prove that the equations in the previous exercise imply the following
identities, which compare the number of lattice points in faces and relative
interiors of faces of the simple polytope P:

k∑

j=0(−1)
j(d − j
k − j
) ∑

F ⊆P
dim F =d−j
 # (F ∩ Z
d) =
 d∑

i=k
 ( i
k
) ∑

G⊆P
dim G=i
 # (G◦ ∩ Z
d) ,

Exercises 111

where k = 0, . . . , d = dim P. For example, for k = 0,

#(P ∩ Z
d) = ∑

G⊆P # (G◦ ∩ Z
d) ,

and for k = d, we obtain the inclusion–exclusion formula

#(P ◦ ∩ Z
d) =
 d∑

j=0(−1)d−j ∑

F ⊆P
dim F =j
 # (F ∩ Z
d) .

5.12. Another nice reformulation of Theorem 5.3 is the following generalized
reciprocity law. For a simple integral d-polytope P, deﬁne the generalized
Ehrhart polynomial

Ek(t) :=
 k∑

j=0(−1)
j(d − j
k − j
) ∑

F ⊆P
dim F =d−j
 LF (t) ,

for 0 ≤ k ≤ d. Prove the following generalized reciprocity law: for 0 ≤ k ≤ d,

Ek(−t) = (−1)d Ed−k(t) ,

which implies Ehrhart–Macdonald reciprocity (Theorem 4.1) for simple inte-
gral polytopes when k = 0.

5.13. What happens when P is not simple? Give an example for which
Theorem 5.3 fails.

5.14. This exercise shows that sometimes, we may use the pigeonhole principle
in a surprising way to ﬁnd geometric structure.

(a) Given any collection of ﬁve points on the unit sphere in R3, show that
there is a closed half-space containing at least four of them.
(b) Suppose we are given a collection of ﬁve vectors in R3 such that no three
of those vectors span a plane. Show that we can always ﬁnd four of them
that form the edges of a 3-dimensional pointed cone.

5.15. Let P ⊂ R3 be a 3-dimensional integral polytope. Show that the sum
of the relative areas of the facets of P equals the number of integer points on
the boundary of P minus 2.

5.16. Give an alternative proof of Theorem 5.6 by considering LP (t) − LP ◦ (t)
as the lattice-point enumerator of the boundary of P.

Chapter 6
Magic Squares

The peculiar interest of magic squares and all lusus numerorum in general lies in the fact
that they possess the charm of mystery.

W. S. Andrews

Fig. 6.1 Magic square at
the Temple de la Sagrada
Fam´ılia (Barcelona, Spain).

Equipped with a solid base of theoretical results, we are now ready to return
to computations. We use Ehrhart theory to assist us in enumerating magic
squares.
Loosely speaking, a magic square is an n × n array of integers (usually
required to be positive, often restricted to the numbers 1, 2, . . . , n2, usually
required to have distinct entries) whose sum along every row, column, and
main diagonal is the same number, called the magic sum. Magic squares
have turned up time and again, some in mathematical contexts, others in
philosophical or religious contexts. According to legend, the ﬁrst magic square

113

114 6 Magic Squares

(the ancient Luo Shu square) was discovered in China sometime before the
ﬁrst century B.C.E. on the back of a turtle emerging from a river. It looked
like this:
 4 9 2

3 5 7

8 1 6

Our task in this chapter is to develop a theory for counting certain classes
of magic squares, which we now introduce.

6.1 It’s a Kind of Magic

One should notice that the Luo Shu square has the distinct entries 1, 2, . . . , 9,
so these entries are distinct positive integers drawn from a particular set. Such
requirements are too restrictive for our purposes. We deﬁne a semimagic
square to be a square matrix whose entries are nonnegative integers and
whose rows and columns sum to the same number. A magic square is a
semimagic square whose main diagonals also add up to the line sum. Here is
one example each of a semimagic and a magic square:

3 0 0

0 1 2

0 2 1
 1 2 0

0 1 2

2 0 1

We caution the reader about clashing deﬁnitions in the literature. For
example, some people reserve the term magic square for what we will call
a traditional magic square, a magic square of order n whose entries are
the distinct integers 1, 2, . . . , n2. (The Luo Shu square is an example of a
traditional magic square.) Others are slightly less restrictive and use the term
magic square for a magic square with distinct entries. We stress that we do
not make this requirement in this chapter.
Our goal is to count semimagic and magic squares. In the traditional case,
this is in some sense not very interesting:1 for each order, there is a ﬁxed
number of traditional magic squares. For example, there are 7040 traditional
4 × 4 magic squares.
The situation becomes more interesting if we drop the condition of tradi-
tionality and study the number of magic squares as a function of the line sum.

1 It is, nevertheless, an incredibly hard problem to count all traditional magic squares of a
given size n. At present, these numbers are known only for n ≤ 5 [1, Sequence A006052].

6.2 Semimagic Squares: Points in the Birkhoﬀ–von Neumann Polytope 115

We denote the total numbers of semimagic and magic squares of order n and
line sum t by Hn(t) and Mn(t), respectively.

♥ t − ♥

t − ♥ ♥
 t
2 t
2

t
2 t
2

Fig. 6.2 Semimagic and magic squares for n = 2.

Example 6.1. We illustrate these notions for the case n = 2, which is not
very complicated. Here a semimagic square is determined once we know one
entry, say the upper left one, denoted by ♥ in Figure 6.2. Because of the
upper row sum, the upper right entry has to be t − ♥, as does the lower left
entry (because of the left column sum). But then the lower right entry has to
be t − (t − ♥) = ♥ (for two reasons: the lower row sum and the right column
sum). The entry ♥ can be any integer between 0 and t. Since there are t + 1
such integers, H2(t) = t + 1 . (6.1)

In the magic case, we have also to think of the diagonals. Looking back at our
semimagic square in Figure 6.2, we see that the ﬁrst diagonal gives 2 · ♥ = t,
or ♥ = t
2 . In this case, t − ♥ = t
2 , and so a 2 × 2 magic square has to have
identical entries in each position. Because we require the entries to be integers,
this is possible only if t is even, in which case we obtain precisely 1 solution,
the square on the right in Figure 6.2. That is,

M2(t) = { 1 if t is even,
0 if t is odd.

These easy results already hint at something: the counting function Hn is of
a diﬀerent character from that of the function Mn. ⊓⊔

6.2 Semimagic Squares: Integer Points in the
Birkhoﬀ–von Neumann Polytope

Just as the Frobenius problem was intrinsically connected to questions about
integer points on line segments, triangles, and higher-dimensional simplices,
magic squares and their relatives have a life in the world of geometry. The
most famous example is connected to semimagic squares.

116 6 Magic Squares

A semimagic n × n square has n2 nonnegative entries that sum to the same
number along every row and along every column. Consider, therefore, the
polytope

Bn :=
 








 x11 · · · x1n
... ...
xn1 . . . xnn
 


 ∈ Rn2 : xjk ≥ 0, ∑
j xjk = 1 for all 1 ≤ k ≤ n
∑

k xjk = 1 for all 1 ≤ j ≤ n
 


 ,

(6.2)
consisting of nonnegative real matrices, in which all rows and columns sum to
1. The polytope Bn is called the nth Birkhoﬀ–von Neumann polytope,
in honor of Garrett Birkhoﬀ (1911–1996)2 and John von Neumann (1903–
1957).
3 Because the matrices contained in the Birkhoﬀ–von Neumann polytope
appear frequently in probability and statistics (the line sum 1 representing
probability 1), Bn is often described as the set of all n × n doubly stochastic
matrices.
Geometrically, Bn is a subset of Rn2 and as such is diﬃcult to picture once
n exceeds 1.
4 However, we can get a glimpse of B2 ⊂ R4 when we think about
what form points in B2 can possibly attain. Very much in sync with Figure 6.2,
such a point is determined by its upper left entry ♥ and looks like this:
( ♥ 1 − ♥
1 − ♥ ♥
 ) .

The entry ♥ is a real number between 0 and 1, which suggests that B2 should
look like a line segment in 4-space. Indeed, the vertices of B2 should be given
by ♥ = 0 and ♥ = 1, that is, by the points
( 1 0
0 1
 ) , ( 0 1
1 0
 ) ∈ B2 .

These results generalize: Bn is an (n − 1)
2-polytope (see Exercise 6.3) whose
vertices (Exercise 6.5) are the permutation matrices, namely, those n × n
matrices that have precisely one 1 in each row and column (every other entry
being zero). For dimensional reasons, we can talk about the continuous volume
of Bn only in the relative sense, following the deﬁnition of Section 5.4.
The connection of the semimagic counting function Hn(t) to the Birkhoﬀ–
von Neumann polytope Bn becomes clear in the light of the lattice-point
enumerator for Bn: the counting function Hn(t) enumerates precisely the
integer points in tBn, that is,

2 For more information about Birkhoﬀ, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Birkhoff Garrett.html.
3 For more information about von Neumann, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Von Neumann.html.
4 And the case n = 1 is not terribly interesting: B1 = {1} is a point.

6.2 Semimagic Squares: Points in the Birkhoﬀ–von Neumann Polytope 117

Hn(t) = # (tBn ∩ Z
n2) = LBn (t) .

We can say more after noticing that permutation matrices are integer points
in Bn, and so Ehrhart’s theorem (Theorem 3.8) applies:

Theorem 6.2. Hn(t) is a polynomial in t of degree (n − 1)
2. ⊓⊔

The fact that Hn is a polynomial—apart from being mathematically
appealing—has the same nice computational consequence that we exploited
in Section 3.7: we can calculate this counting function by interpolation. For
example, to compute H2, a linear polynomial, we need to know only two
values. In fact, since we know that the constant term of H2 is 1 (by Corol-
lary 3.15), we need only one value. It is not hard to convince even a lay person
that H2(1) = 2 (which two semimagic squares are those?), from which we
interpolate H2(t) = t + 1 .

To interpolate the polynomial H3, we need to know four values aside from
H3(0) = 1. In fact, we do not even have to know that many values, because
Ehrhart–Macdonald reciprocity (Theorem 4.1) assists us in computations. To
see this, let H ◦
n(t) denote the number of n × n square matrices with positive
integer entries summing up to t along each row and column. A moment’s
thought (Exercise 6.6) reveals that

H ◦
n(t) = Hn(t − n) . (6.3)

But there is a second relationship between Hn and H ◦
n, namely, H ◦
n(t) counts,
by deﬁnition, the integer points in the relative interior of the Birkhoﬀ–von Neu-
mann polytope Bn, that is, H ◦
n(t) = LB◦
n(t). Ehrhart–Macdonald reciprocity
(Theorem 4.1) now gives

H ◦
n(−t) = (−1)(n−1)2Hn(t) .

Combining this identity with (6.3) gives us a symmetry identity for the
counting function for semimagic squares:

Theorem 6.3. The polynomial Hn satisﬁes

Hn(−n − t) = (−1)
(n−1)2Hn(t)

and Hn(−1) = Hn(−2) = · · · = Hn(−n + 1) = 0 . ⊓⊔

The roots of Hn at the ﬁrst n−1 negative integers follow from (Exercise 6.7)

H ◦
n(1) = H ◦
n(2) = · · · = H ◦
n(n − 1) = 0 .

Theorem 6.3 gives the degree of Bn, and it implies that the numerator of the
Ehrhart series of the Birkhoﬀ–von Neumann polytope is palindromic:

118 6 Magic Squares

Corollary 6.4. The Ehrhart series of the Birkhoﬀ–von Neumann polytope
Bn has the form

EhrBn (z) = h
∗
(n−1)(n−2) z(n−1)(n−2) + · · · + h
∗
0

(1 − z)
(n−1)2+1 ,

where h
∗
0, h
∗
1, . . . , h∗
(n−1)(n−2) ∈ Z≥0 satisfy h
∗
k = h
∗
(n−1)(n−2)−k for 0 ≤ k ≤

(n−1)(n−2)
2 .

Proof. Denote the Ehrhart series of Bn by

EhrBn (z) = h
∗
(n−1)2 z(n−1)
2 + · · · + h∗
0

(1 − z)
(n−1)2+1 .

The fact that h
∗
(n−1)2 = · · · = h
∗
(n−1)2−(n−2) = 0 follows from the second
part of Theorem 6.3 and Theorem 4.5. The palindromicity of the numerator
coeﬃcients follows from the ﬁrst part of Theorem 6.3 and Exercise 4.8: it
implies
 EhrBn
 ( 1
z
 ) = (−1)(n−1)
2+1zn EhrBn (z) ,

which yields h
∗
k = h
∗
(n−1)(n−2)−k on simplifying both sides of the equation. ⊓⊔

Let’s return to the interpolation of H3: Theorem 6.3 gives, in addition to
H3(0) = 1, the values

H3(−3) = 1 and H3(−1) = H3(−2) = 0 .

These four values together with H3(1) = 6 (see Exercise 6.1) suﬃce to
interpolate the quartic polynomial H3, and one computes

H3(t) = 1
8 t4 + 3
4 t
3 + 15
8 t2 + 9
4 t + 1 . (6.4)

This interpolation example suggests the use of a computer; we let it calculate
enough values of Hn and then simply interpolate. As far as computations
are concerned, however, we should not get too excited about the fact that
we computed H2 and H3 so eﬀortlessly. In general, the polynomial Hn has
degree (n − 1)2, so we need to compute (n − 1)2 + 1 values of Hn to be
able to interpolate. Of those, we know n (the constant term and the roots
given by Theorem 6.3), so n2 − 3n + 2 values of Hn remain to be computed.
Ehrhart–Macdonald reciprocity reduces the number of values to be computed
to n2−3n+2
2 . That is still a large number, as anyone can testify who has tried
to get a computer to enumerate all semimagic 7 × 7 squares with line sum
15. Nevertheless, it is a fun fact that we can compute Hn for small n by
interpolation. It is amusing to test one’s computer against the constant-term
computation we will outline below, and we invite the reader to try both.

6.3 Magic Generating Functions and Constant-Term Identities 119

For small n, interpolation is clearly superior to a constant-term computation
in the spirit of Chapter 1. The turning point is somewhere around n = 5:
the computer needs more and more time to compute the values Hn(t) as t
increases. Methods superior to interpolation are needed.

6.3 Magic Generating Functions and Constant-Term
Identities

Now we will construct a generating function for Hn, for which we will use
Theorem 2.13. The semimagic counting function Hn is the Ehrhart polynomial
of the nth Birkhoﬀ–von Neumann polytope Bn, which, in turn, is deﬁned as a
set of matrices by (6.2). First we rewrite the deﬁnition of Bn to ﬁt the general
description (2.23) of a polytope. If we consider the points in Bn as column
vectors in Rn2 (rather than as matrices in Rn×n), then

Bn = {
x ∈ Rn
2
≥0 : A x = b
} ,

where
 A =
 












 1 · · · 1 1 · · · 1 . . . 1 · · · 1
1 1 1
. . . . . . · · · . . .
1 1 1
 












 ∈ Z
2n×n2 (6.5)

(here we do not show the zero entries) and

b =
 





 1
1
...
1
 




 ∈ Z
2n.

From this description of Bn, we can easily build the generating function
for Hn. According to Theorem 2.13, for a general rational polytope P ={
x ∈ Rd
≥0 : A x = b
}
,

LP (t) = const ( 1
(1 − zc1) (1 − zc2 ) · · · (1 − zcd ) ztb
 ) ,

where c1, c2, . . . , cd denote the columns of A. In our special case, the columns
of A are of a simple form: they contain exactly two 1’s and elsewhere 0’s. We

120 6 Magic Squares

need one generating-function variable for each row of A. To keep things as clear
as possible, we use z1, z2, . . . , zn for the ﬁrst n rows of A (representing the row
constraints of Bn) and w1, w2, . . . , wn for the last n rows of A (representing
the column constraints of Bn). With this notation, Theorem 2.13 applied to
Bn gives the following starting point for our computations:

Theorem 6.5. The number Hn(t) of semimagic n × n squares with line sum
t satisﬁes

Hn(t) = const
 


 1
∏

1≤j,k≤n (1 − zjwk) (∏

1≤j≤n zj ∏

1≤k≤n wk)t
 


 . ⊓⊔

This identity is of both theoretical and practical use. One can use it to compute
H3 and even H4 by hand. For now, we work on reﬁning it further, exempliﬁed
by the case n = 2.
We ﬁrst note that in the formula for H2, the variables w1 and w2 are
separated, in the sense that we can write this formula as a product of two
factors, one involving only w1 and the other involving only w2:

H2(t) = const ( 1
zt
1zt
2
 1
(1 − z1w1) (1 − z2w1) wt
1
 1
(1 − z1w2) (1 − z2w2) wt
2
 ) .

Now we put an ordering on the constant-term computation: let’s ﬁrst compute
the constant term with respect to w2, then the one with respect to w1. (We
do not order the computation with respect to z1 and z2 just yet.) Since z1,
z2, and w1 are considered constants when we do constant-term computations
with respect to w2, we can simplify:

H2(t) = constz1,z2
 ( 1
zt
1zt
2 constw1
 ( 1
(1 − z1w1) (1 − z2w1) wt
1

× constw2
 ( 1
(1 − z1w2) (1 − z2w2) wt
2
 ))) .

Now we can see the eﬀect of the separate appearance of w1 and w2: the
constant-term identity factors. This is very similar to the factoring that can
appear in computations of integrals in several variables. Let’s rewrite our
identity to emphasize the factoring:

H2(t) = constz1,z2
 ( 1
zt
1zt
2 constw1
 ( 1
(1 − z1w1) (1 − z2w1) wt
1
 )

× constw2
 ( 1
(1 − z1w2) (1 − z2w2) wt
2
 )) .

But now the expressions in the last two sets of parentheses are identical,
except that in one case, the constant-term variable is called w1, and in the

6.3 Magic Generating Functions and Constant-Term Identities 121

other case, w2. Since these are just “dummy” variables, we can call them w,
and combine:

H2(t) = constz1,z2
 ( 1
zt
1zt
2
 (constw 1
(1 − z1w) (1 − z2w) wt
 )2)
 .

(Note the square!) Naturally, all of this factoring works in the general case,
and we invite the reader to prove it (Exercise 6.8):

Hn(t) = constz1,...,zn
 ((z1 · · · zn)
−t (
constw 1
(1 − z1w) · · · (1 − znw)wt
 )n) .

(6.6)
We can go further, namely, we can compute the innermost constant term

constw 1
(1 − z1w) · · · (1 − znw)wt .

It should come as no surprise that we shall use a partial fraction expansion to
do so. The w-poles of the rational function are at w = 1
z1 , w = 1
z2 , . . . , w =
1
zn , w = 0, and so we expand

1
(1 − z1w) · · · (1 − znw)wt = A1
w − 1
z1 + A2
w − 1
z2 +· · ·+ An
w − 1
zn +
 t∑

k=1
 Bk
wk . (6.7)

Just as in Chapter 1, we can forget about the Bk-terms, since they do not
contribute to the constant term, that is,

constw 1
(1 − z1w) · · · (1 − znw)wt

= constw
 ( A1
w − 1
z1 + A2
w − 1
z2 + · · · + An
w − 1
zn
 )

= −A1z1 − A2z2 − · · · − Anzn .

We invite the reader to show (Exercise 6.9) that

Ak = − zt−1
k(1 − z1
zk
 ) · · · (1 − zk−1
zk
 ) (
1 − zk+1
zk
 ) · · · (1 − zn
zk
 )

= − zt+n−2
k∏

j̸=k(zk − zj) . (6.8)

Putting these coeﬃcients back into the partial fraction expansion yields the
following identity.

122 6 Magic Squares

Theorem 6.6. The number Hn(t) of semimagic n × n squares with line sum
t satisﬁes
 Hn(t) = const
 (

(z1 · · · zn)
−t ( n∑

k=1
 zt+n−1
k∏

j̸=k(zk − zj)
 )n)
 . ⊓⊔

Amidst all this generality, we almost forgot to compute H2 with our partial
fraction approach. The last theorem says that

H2(t) = const
 (

(z1z2)
−t ( zt+1
1
z1 − z2 + zt+1
2
z2 − z1
 )2)

= const ( zt+2
1 z−t
2
(z1 − z2)2 − 2 z1z2
(z1 − z2)2 + z−t
1 zt+2
2
(z1 − z2)2
 ) . (6.9)

It is now time to put more order on the constant-term computation. Let’s say
that we ﬁrst compute the constant term with respect to z1, and after that
with respect to z2. So we have to compute ﬁrst

constz1
 ( zt+2
1 z−t
2
(z1 − z2)2
 ) , constz1
 ( z1z2
(z1 − z2)2
 ) , and constz1
 ( z−t
1 zt+2
2
(z1 − z2)2
 ) .

To obtain these constant terms, we need to expand the function 1
(z1−z2)2 . As
we know from calculus, this expansion depends on the order of the magnitudes
of z1 and z2. For example, if |z1| < |z2|, then

1
z1 − z2 = 1
z2
 1
z1
z2 − 1 = − 1
z2
 ∑

k≥0
 ( z1
z2
 )k = − ∑

k≥0
 1
zk+1
2 zk
1 ,

and hence
 1
(z1 − z2)2 = − d
dz1
 ( 1
z1 − z2
 ) = ∑

k≥1
 k
zk+1
2 zk−1
1 = ∑

k≥0
 k + 1
zk+2
2 zk
1 .

So let’s assume for the moment that |z1| < |z2|. This might sound funny, since
z1 and z2 are variables. However, as such they are simply tools that enable
us to compute some quantity that is independent of z1 and z2. In view of
these ideas, we may assume any order of the magnitudes of the variables. In
Exercise 6.11, we will check that indeed the order does not matter. Now,

constz1
 ( zt+2
1 z−t
2
(z1 − z2)2
 ) = z−t
2 constz1
 ( zt+2
1
(z1 − z2)2
 )

= z−t
2 constz1
 

zt+2
1 ∑

k≥0
 k + 1
zk+2
2 zk
1
 

 (6.10)

6.3 Magic Generating Functions and Constant-Term Identities 123

= z−t
2 constz1
 

∑

k≥0
 k + 1
zk+2
2 zk+t+2
1
 



= 0 ,

since there are only positive powers of z1 (recall that t ≥ 0). Analogously (see
Exercise 6.10), one checks that

constz1
 ( z1z2
(z1 − z2)2
 ) = 0 . (6.11)

For the last constant term, we compute

constz1
 ( z−t
1 zt+2
2
(z1 − z2)2
 ) = zt+2
2 constz1
 

z−t
1 ∑

k≥0
 k + 1
zk+2
2 zk
1
 



= zt+2
2 constz1
 

∑

k≥0
 k + 1
zk+2
2 zk−t
1
 

 .

The constant term on the right-hand side is the term with k = t, that is,

constz1
 ( z−t
1 zt+2
2
(z1 − z2)2
 ) = zt+2
2 t + 1
zt+2
2 = t + 1 .

So of the three constant terms, only one survives, and with constz2 (t+1) = t+1
we recover what we have known since the beginning of this chapter:

H2(t) = const ( zt+2
1 z−t
2
(z1 − z2)2 − 2 z1z2
(z1 − z2)2 + z−t
1 zt+2
2
(z1 − z2)2
 ) = t + 1 .

This was a lot of work for this seemingly trivial polynomial. Recall, for
example, that we can get the same result by an easy interpolation. However,
to compute a similar interpolation, e.g., for H4, we likely would need to
use a computer (to obtain the interpolation values). On the other hand, the
constant-term computation of H4 boils down to only ﬁve iterated constant
terms, which can actually be computed by hand (see Exercise 6.14). The
result is

H4(t) = 11
11340 t
9 + 11
630 t8 + 19
135 t7 + 2
3 t
6 + 1109
540 t
5 + 43
10 t4 + 35117
5670 t3

+ 379
63 t2 + 65
18 t + 1 .

124 6 Magic Squares

6.4 The Enumeration of Magic Squares

What happens when we bring the diagonal constraints, which are not present
in the semimagic case, into the magic picture? In the introduction of this
chapter we have already seen an example, namely the number of 2 × 2 magic
squares,
 M2(t) = { 1 if t is even,
0 if t is odd.

This is a very simple example of a quasipolynomial. In fact, like Hn, the
counting function Mn is deﬁned by integral linear equations and inequalities,
so it is the lattice-point enumerator of a rational polytope, and Theorem 3.23
gives at once the following result.

Theorem 6.7. The counting function Mn(t) is a quasipolynomial in t. ⊓⊔

We invite the reader to prove that the degree of Mn is n2 − 2n − 1 (Exer-
cise 6.16).
Let’s see what happens in the ﬁrst nontrivial case, 3 × 3 magic squares.
We follow our recipe and assign variables m1, m2, . . . , m9 to the entries of our
3 × 3 squares:
 m1 m2 m3

m4 m5 m6

m7 m8 m9

The magic conditions require now that m1, m2, . . . , m9 ∈ Z≥0 and

m1 + m2 + m3 = t ,

m4 + m5 + m6 = t ,

m7 + m8 + m9 = t ,

m1 + m4 + m7 = t ,

m2 + m5 + m8 = t ,

m3 + m6 + m9 = t ,

m1 + m5 + m9 = t ,

m3 + m5 + m7 = t ,

according to the row sums (the ﬁrst three equations), the column sums (the
next three equations), and the diagonal sums (the last two equations). By
now, we are experienced in translating this system into a generating function:
we need one variable for each equation, so let’s take z1, z2, z3 for the ﬁrst
three, w1, w2, w3 for the next three, and y1, y2 for the last two equations. The
function M3(t) is thus the constant term of

Notes 125

1
(1 − z1w1y1) (1 − z1w2) (1 − z1w3y2) (1 − z2w1) (1 − z2w2y1y2) (1 − z2w3)

× 1
(1 − z3w1y2) (1 − z3w2) (1 − z3w3y1) (z1z2z3w1w2w3y1y2)
t . (6.12)

It does take some work, but it is instructive to compute this constant term
(just try it!). The result is

M3(t) =
 { 2
9 t2 + 2
3 t + 1 if 3|t,
0 otherwise. (6.13)

As predicted by Theorem 6.7, M3 is a quasipolynomial. It has degree 2 and
period 3. This may be more apparent if we rewrite it as

M3(t) =
 



 2
9 t2 + 2
3 t + 1 if t ≡ 0 mod 3,
0 if t ≡ 1 mod 3,
0 if t ≡ 2 mod 3,

and we can see the three constituents of the quasipolynomial M3. There is
an alternative way to describe M3; namely, let

c2(t) =
 



 2
9 if t ≡ 0 mod 3,
0 if t ≡ 1 mod 3,
0 if t ≡ 2 mod 3,

c1(t) =
 



 2
3 if t ≡ 0 mod 3,
0 if t ≡ 1 mod 3,
0 if t ≡ 2 mod 3,

c0(t) =
 



1 if t ≡ 0 mod 3,
0 if t ≡ 1 mod 3,
0 if t ≡ 2 mod 3.

Then the quasipolynomial M3 can be written as

M3(t) = c2(t) t2 + c1(t) t + c0(t) .

Notes

1. Magic squares date back to China in the ﬁrst millennium B.C.E. [78]; they
underwent much further development in the Islamic world late in the ﬁrst
millennium C.E. and in the next millennium (or sooner; the data are lacking)
in India [79]. From Islam, they passed to Christian Europe in the later Middle

126 6 Magic Squares

Ages, probably initially through the Jewish community [79, Part II, pp. 290
ﬀ.] and later possibly Byzantium [79, Part I, p. 198], and no later than the
early eighteenth century (the data are buried in barely tapped archives) to
sub-Saharan Africa [257, Chapter 12]. The contents of a magic square have
varied with time and writer; usually they have been the ﬁrst n2 consecutive
integers, but often any arithmetic sequence or arbitrary positive numbers.
In the past century, mathematicians have made some simpliﬁcations in the
interest of obtaining results about the number of squares with a ﬁxed magic
sum, in particular, allowing repeated entries as in this chapter.

2. The problem of counting magic squares (other than traditional magic
squares) seems not to have occurred to anyone before the twentieth century, no
doubt because there was no way to approach the question previously. The ﬁrst
nontrivial formulas addressing the counting problem, namely (6.4) and (6.13)
for H3 and M3, were established by Percy Macmahon in 1915 [168]. Recently,
there has grown up a literature on exact formulas (see, for example, [111, 225]
for semimagic squares; for magic squares, see [2, 36]; for magic squares with
distinct entries, see [48, 49, 255]).

3. Another famous kind of square is a Latin square (see, for example, [102]).
Here each row and column has n diﬀerent numbers, the same n numbers in
every row/column (usually taken to be the ﬁrst n positive integers). There
are counting problems associated with Latin squares, which can be attacked
using Ehrhart theory [49] (see also [1, Sequence A002860]).

4. Recent work includes mathematical-historical research, such as the discovery
of unpublished magic squares of Benjamin Franklin [3, 188]. Aside from
mathematical research, magic squares and their siblings naturally continue
to be an excellent source of topics for popular mathematics books (see, for
example, [7, 192]).

5. The Birkhoﬀ–von Neumann polytope Bn possesses fascinating combinatorial
properties [57,70,71,84,258] and relates to many mathematical areas [105,152].
Its name honors Garrett Birkhoﬀ and John von Neumann, who proved that the
extremal points of Bn are the permutation matrices [58,252] (see Exercise 6.5).
A long-standing open problem is the determination of the relative volume of
Bn, which is known only for n ≤ 10 [1, Sequence A037302]. In fact, the last
two records (n = 9 and 10) for computing vol Bn rely on the theory of counting
functions that is introduced in this book, more precisely, Theorem 6.6 [43].

6. An important generalization of the Birkhoﬀ–von Neumann polytope is
given by transportation polytopes, which consist of contingency tables. They
have applications to statistics and in particular to disclosure limitation proce-
dures [98]. The Birkhoﬀ–von Neumann polytopes are special transportation
polytopes that consist of two-way contingency tables with given 1-marginals.

Exercises 127

7. The polynomiality of Hn (Theorem 6.2) and its symmetry (Theorem 6.3)
were conjectured in 1966 by Harsh Anand, Vishwa Dumir, and Hansraj Gupta
[6] and proved seven years later independently by Eug`ene Ehrhart [111] and
Richard Stanley [225]. See [73,232] for more about the history of Theorems 6.2
and 6.3 and their connections to commutative algebra. Stanley also conjectured
that the numerator coeﬃcients in Corollary 6.4 are unimodal, a fact that
was proved only in 2005, by Christos Athanasiadis [13] (see also [75]). The
quasipolynomiality of Mn (Theorem 6.7) and its degree are discussed in [36].
The period of Mn is in general not known. In [36], it is conjectured that it
is always nontrivial for n > 1. The work in [2] gives some credence to this
conjecture by proving that the polytope of magic n × n squares is not integral
for n ≥ 2.

8. We close with a story about Cornelius Agrippa’s De Occulta Philosophia,
written in 1510. In it he describes the spiritual powers of magic squares and
produces some squares of orders from three up to nine. His work, although
inﬂuential in the mathematical community, enjoyed only brief success, for
the Counter-Reformation and the witch hunts of the Inquisition began soon
thereafter: Agrippa himself was accused of being allied with the devil.

Exercises

6.1. ♣ Find and prove a formula for Hn(1).

6.2. Let (xij)1≤i,j≤3 be a magic 3 × 3 square.

(a) Show that the center term x22 is the average over all xij.
(b) Show that M3(t) = 0 if 3 does not divide t.

6.3. ♣ Prove that dim Bn = (n − 1)2.

6.4. Prove the following characterization of a vertex of a convex polytope P:
A point v ∈ P is a vertex of P if and only if for every line L through v and
every neighborhood N of v, there exists a point in L ∩ N that is not in P.

6.5. ♣ Prove that the vertices of Bn are the n × n permutation matrices.

6.6. ♣ Let H ◦
n(t) denote the number of n × n matrices with positive integer
entries summing up to t along each row and column. Show that H ◦
n(t) =
Hn(t − n) for t > n.

6.7. ♣ Show that H ◦
n(1) = H ◦
n(2) = · · · = H ◦
n(n − 1) = 0.

6.8. ♣ Prove (6.6):

Hn(t) = constz1,...,zn
 ((z1 · · · zn)
−t (
constw 1
(1 − z1w) · · · (1 − znw)wt
 )n) .

128 6 Magic Squares

6.9. ♣ Compute the partial fraction coeﬃcients (6.8).

6.10. ♣ Verify (6.11).

6.11. Repeat the constant-term computation of H2 starting from (6.9), but
now by ﬁrst computing the constant term with respect to z2, and after that
with respect to z1.

6.12. Use your favorite computer program to calculate the formula for H3(t),
H4(t), . . . by interpolation.

6.13. Compute H3 using Theorem 6.6.

6.14. Compute H4 using Theorem 6.6.

6.15. Show that
n∑

k=1
 zt+n−1
k∏

j̸=k(zk − zj) = ∑

m1+···+mn=t zm1
1 · · · zmn
n ,

and use this identity to give an alternative proof of Theorem 6.6.

6.16. ♣ Prove that for n ≥ 3, the degree of Mn is n2 − 2n − 1.

6.17. Explain the period of M3 by computing the vertices of the polytope of
3 × 3 magic squares.

6.18. ♣ Verify (6.12) and use it to compute M3.

6.19. Compute M3 by interpolation. (Hint: Use Exercises 6.2 and 6.17.)

6.20. A symmetric semimagic square is a semimagic square that is a
symmetric matrix. Show that the number of symmetric semimagic n × n
squares with line sum t is a quasipolynomial in t. Determine its degree and
period.

Open Problems

6.21. Compute the number of traditional magic n × n squares for n > 5.

6.22. Compute vol Bn for n > 10. Compute Hn for n > 9.

6.23. Prove that the period of Mn is nontrivial for n > 1.

6.24. The vertices of the Birkhoﬀ–von Neumann polytope are in one-to-one
correspondence with the elements of the symmetric group Sn. Consider a
subgroup of Sn and take the convex hull of the corresponding permutation ma-
trices. Compute the Ehrhart polynomials of this polytope. (The face numbers
of the polytope corresponding to the subgroup An, the even permutations,
were studied in [142].)

Open Problems 129

6.25. Consider the rational polytope Sn formed by all symmetric n × n doubly
stochastic matrices (see Exercise 6.20).

(a) Write EhrSn(z) as a rational function with denominator (1 − z2)(
n
2)+1.
Prove that the numerator polynomial is palindromic.
(b) Prove that the numerator polynomial of Ehr2Sn (z) is palindromic.

(See [93] for partial results.)

6.26. Prove that the graph formed by the vertices and edges of every 2-way
transportation polytope is Hamiltonian.
 Part II
Beyond the Basics

Chapter 7
Finite Fourier Analysis

God created inﬁnity, and man, unable to understand inﬁnity, created ﬁnite sets.

Gian–Carlo Rota (1932–1999)

We now consider the vector space of all complex-valued periodic functions on
the integers with period b. It turns out that every such function a(n) on the
integers can be written as a polynomial in the b
th root of unity ξn := e2πin/b.
Such a representation for a(n) is called a ﬁnite Fourier series. Here we
develop ﬁnite Fourier theory using rational functions and their partial fraction
decomposition. We then deﬁne the Fourier transform and the convolution of
ﬁnite Fourier series, and show how one can use these ideas to prove identities
on trigonometric functions, as well as ﬁnd connections to the classical Dedekind
sums.
The more we know about roots of unity and their various sums, the
deeper are the results that we can prove (see Exercise 7.20); in fact, certain
statements about sums of roots of unity even imply the Riemann hypothesis!
However, this chapter is elementary and draws connections to the sawtooth
functions and Dedekind sums, two basic sums over roots of unity. The general
philosophy here is that ﬁnite sums of rational functions of roots of unity are
basic ingredients in many mathematical structures.

7.1 A Motivating Example

To ease the reader into the general theory, let’s work out the ﬁnite Fourier
series for a simple example ﬁrst, an arithmetic function with a period of 3.

Example 7.1. Consider the following arithmetic function, of period 3:
 133

134 7 Finite Fourier Analysis

n : 0, 1, 2, 3, 4, 5, . . .

a(n) : 1, 5, 2, 1, 5, 2, . . .

We ﬁrst embed this sequence into a generating function as follows:

F (z) := 1 + 5z + 2z2 + z3 + 5z4 + 2z5 + · · · = ∑

n≥0 a(n) zn.

Since the sequence is periodic, we can simplify F (z) using a geometric series
argument:

F (z) = ∑

n≥0 a(n) zn

= 1 + 5z + 2z2 + z3 (1 + 5z + 2z2) + z6 (1 + 5z + 2z2) + · · ·

= (1 + 5z + 2z2) ∑

k≥0 z3k

= 1 + 5z + 2z2

1 − z3 .

We now use the same technique that was employed in Chapter 1, namely the
technique of expanding a rational function into its partial fraction decompo-
sition. Here all the poles are simple, and located at the three cube roots of
unity, so that
 F (z) = ˆa(0)
1 − z + ˆa(1)
1 − ρz + ˆa(2)
1 − ρ2z , (7.1)

where the constants ˆa(0), ˆa(1), ˆa(2) remain to be found, and where ρ := e2πi/3,
a third root of unity. Using the geometric series for each of these terms
separately, we arrive at

F (z) = ∑

n≥0
 (ˆa(0) + ˆa(1)ρn + ˆa(2)ρ2n) zn,

so that we have derived the ﬁnite Fourier series of our sequence a(n). The
only remaining piece of information that we need is the computation of the
constants ˆa(j), for j = 0, 1, 2. It turns out that this is also quite easy to do.
We have, from (7.1) above, the identity

ˆa(0) (1 − ρz) (1 − ρ2z) + ˆa(1) (1 − z) (1 − ρ2z) + ˆa(2) (1 − z) (1 − ρz)

= 1 + 5z + 2z2,

valid for all z ∈ C. On letting z = 1, ρ2, and ρ, respectively, we obtain

7.2 Finite Fourier Series for Periodic Functions on Z 135

3 ˆa(0) = 1 + 5 + 2 ,

3 ˆa(1) = 1 + 5ρ2 + 2ρ4,

3 ˆa(2) = 1 + 5ρ + 2ρ2,

where we have used the identity (1 − ρ)(1 − ρ2) = 3 (see Exercise 7.2). We
can simplify a bit to get ˆa(0) = 8
3 , ˆa(1) = −4−3ρ
3 , and ˆa(2) = −1+3ρ
3 . Thus
the ﬁnite Fourier series for our sequence is

a(n) = 8
3 + (− 4
3 − ρ
) ρ
n + (
− 1
3 + ρ) ρ2n. ⊓⊔

The object of the next section is to show that this simple process follows just
as easily for every periodic function on Z. The ensuing sections contain some
applications of the ﬁnite Fourier series of periodic functions.

7.2 Finite Fourier Series for Periodic Functions on Z

The general theory is just as easy conceptually as Example 7.1, and we now
develop it. Consider a periodic sequence on Z, deﬁned by {a(n)}
∞
n=0, of period
b. Throughout the chapter, we ﬁx the bth root of unity ξ := e2πi/b. As before,
we embed our periodic sequence {a(n)}∞
n=0 into a generating function,

F (z) := ∑

n≥0 a(n) zn,

and use the periodicity of the sequence to immediately get

F (z) =
 (b−1∑

k=0 a(k) zk)
 +
 (b−1∑

k=0 a(k) zk)
 zb +
 (b−1∑

k=0 a(k) zk)
 z2b + · · ·

= ∑b−1
k=0 a(k) zk

1 − zb = P (z)
1 − zb ,

where the last step simply deﬁnes the polynomial P (z) = ∑b−1
k=0 a(k) zk. Now
we expand the rational generating function F (z) into partial fractions, as
before:
 F (z) = P (z)
1 − zb =
 b−1∑

m=0
 ˆa(m)
1 − ξmz .

As in Example 7.1, we expand each of the terms 1
1−ξmz as a geometric series,
and substitute into the sum above to get

136 7 Finite Fourier Analysis

F (z) = ∑

n≥0 a(n) zn =
 b−1∑

m=0
 ˆa(m)
1 − ξmz

=
 b−1∑

m=0 ˆa(m) ∑

n≥0 ξmnzn = ∑

n≥0
 ( b−1∑

m=0 ˆa(m) ξmn)
 zn.

Comparing the coeﬃcients of any ﬁxed zn gives us the ﬁnite Fourier series
for a(n), namely
 a(n) =
 b−1∑

m=0 ˆa(m) ξmn.

We now ﬁnd a formula for the Fourier coeﬃcients ˆa(n), as in the example.
To recapitulate,
 P (z) =
 b−1∑

m=0 ˆa(m) 1 − zb

1 − ξmz .

To solve for P (ξ−n), we note that

lim
z→ξ−n 1 − zb

1 − ξmz = 0 if m − n ̸≡ 0 mod b ,

and
 lim
z→ξ−n 1 − zb

1 − ξmz = lim
z→ξ−n bzb−1

ξm = b ξn−m = b if m − n ≡ 0 mod b .

Thus P (ξ−n) = b ˆa(n), and so

ˆa(n) = 1
b P (ξ−n) = 1
b
 b−1∑

k=0 a(k) ξ−nk.

We have just proved the main result of ﬁnite Fourier series, using only
elementary properties of rational functions:

Theorem 7.2 (Finite Fourier series expansion and Fourier inver-
sion). Let a(n) be any periodic function on Z, with period b. Then we have
the following ﬁnite Fourier series expansion:

a(n) =
 b−1∑

k=0 ˆa(k) ξnk,

where the Fourier coeﬃcients are

ˆa(n) = 1
b
 b−1∑

k=0 a(k) ξ−nk, (7.2)

7.2 Finite Fourier Series for Periodic Functions on Z 137

with ξ = e2πi/b. ⊓⊔

The coeﬃcients ˆa(m) are known as the Fourier coeﬃcients of the function
a(n), and if ˆa(m) ̸= 0, we sometimes say that the function has frequency m.
The ﬁnite Fourier series of a periodic function provides us with surprising
power and insight into its structure. We are able to analyze the function
using its frequencies (only ﬁnitely many), and this window into the frequency
domain becomes indispensable for computations and simpliﬁcations.
We note that the Fourier coeﬃcients ˆa(n) and the original sequence elements
a(n) are related by a linear transformation given by the matrix

L := (ξ(i−1)(j−1)) , (7.3)

where 1 ≤ i, j ≤ b, as is evident from (7.2) in the proof above. We further note
that the second half of the proof, namely solving for the Fourier coeﬃcients
ˆa(n), is just tantamount to inverting this matrix L.
One of the main building blocks of our lattice-point enumeration formulas
in polytopes is the sawtooth function, deﬁned by

((x)) :=
 {{x} − 1
2 if x /∈ Z,
0 if x ∈ Z. (7.4)

(As a reminder, {x} = x − ⌊x⌋ is the fractional part of x.) The graph of this
function is displayed in Figure 7.1. We have seen a closely related function
before, in Chapter 1, in our study of the coin-exchange problem. Equation (1.8)
gave us the ﬁnite Fourier series for essentially this function from the discrete-
geometry perspective of the coin-exchange problem; however, we now compute
the ﬁnite Fourier series for this periodic function directly, pretending that we
do not know about its other life as a counting function.

-1 1 2 3 4
-0.5
 0.5
 y = (( x ))
 x

Fig. 7.1 The sawtooth function y = ((x)).

Lemma 7.3. The ﬁnite Fourier series for the discrete sawtooth function (( a
b )),
a periodic function of a ∈ Z with period b, is given by

138 7 Finite Fourier Analysis

(( a
b
 )) = 1
2b
 b−1∑

k=1
 1 + ξk

1 − ξk ξak = i
2b
 b−1∑

k=1 cot πk
b ξak.

Here the second equality follows from 1+e2πix
1−e2πix = i cot(πx), by the deﬁnition
of the cotangent.

Proof. Using Theorem 7.2, we know that our periodic function has a ﬁnite
Fourier series (( a
b )) = ∑b−1
k=0 ˆa(k) ξak, where

ˆa(k) = 1
b
 b−1∑

m=0
 (( m
b
 )) ξ−mk.

We ﬁrst compute ˆa(0) = 1
b ∑b−1
m=0 (( m
b )) = 0, by Exercise 7.15. For k ̸= 0,

ˆa(k) = 1
b
 b−1∑

m=1
 ( m
b − 1
2
 ) ξ−mk = 1
b2
 b−1∑

m=1 m ξ−mk + 1
2b

= 1
b
 ( ξk

1 − ξk + 1
2
 ) = 1
2b 1 + ξk

1 − ξk ,

where we used Exercise 7.5 in the penultimate equality above. ⊓⊔

We deﬁne the Dedekind sum by

s(a, b) =
 b−1∑

k=0
 (( ka
b
 )) (( k
b
 )) ,

for any two relatively prime integers a and b > 0 (although it may be easily
extended to all integers—see Exercise 8.11). Note that the Dedekind sum is a
periodic function of the variable a, with period b, by the periodicity of the
sawtooth function. That is,

s(a + jb, b) = s(a, b) for all j ∈ Z . (7.5)

Using the ﬁnite Fourier series for the sawtooth function, we can now easily
reformulate the Dedekind sums as a ﬁnite sum over the b
th roots of unity or
cotangents:

Lemma 7.4.

s(a, b) = 1
4b
 b−1∑

µ=1
 1 + ξµ

1 − ξµ 1 + ξ−µa

1 − ξ−µa = 1
4b
 b−1∑

µ=1 cot πµ
b cot πµa
b .

We will see and use this alternative formulation of the Dedekind sum time
and again.

7.3 The Finite Fourier Transform and Its Properties 139

Proof.
 s(a, b) =
 b−1∑

k=0
 (( ka
b
 )) (( k
b
 ))

= 1
4b2
 b−1∑

k=0
 ((b−1∑

µ=1
 1 + ξµ

1 − ξµ ξµka) (b−1∑

ν=1
 1 + ξν

1 − ξν ξνk))

= 1
4b2
 b−1∑

µ=1
 b−1∑

ν=1
 1 + ξµ

1 − ξµ 1 + ξν

1 − ξν
 (b−1∑

k=0 ξk(ν+µa))
 .

We note that the last sum ∑b−1
k=0 ξk(ν+µa) vanishes, unless ν ≡ −µa mod b
(Exercise 7.6), in which case the sum equals b, and we obtain

s(a, b) = 1
4b
 b−1∑

µ=1
 1 + ξµ

1 − ξµ 1 + ξ−µa

1 − ξ−µa .

Rewriting the right-hand side in terms of cotangents gives

s(a, b) = i
2

4b
 b−1∑

µ=1 cot πµ
b cot −πµa
b = 1
4b
 b−1∑

µ=1 cot πµ
b cot πµa
b ,

because the cotangent is an odd function. ⊓⊔

7.3 The Finite Fourier Transform and Its Properties

Given a periodic function f on Z, we have seen that f possesses a ﬁnite
Fourier series, with the ﬁnite collection of Fourier coeﬃcients that we called
ˆf (0), ˆf (1), . . . , ˆf (b − 1). We now regard f as a function on the ﬁnite set
G = {0, 1, 2, . . . , b − 1}, and let VG be the vector space of all complex-valued
functions on G. Equivalently, VG is the vector space of all complex-valued
periodic functions on Z with period b.
We deﬁne the Fourier transform of f , denoted by F(f ), to be the periodic
function on Z deﬁned by the sequence of uniquely determined values

ˆf (0), ˆf (1), . . . , ˆf (b − 1) .

Thus F(f )(m) = ˆf (m) .

Theorem 7.2 above gave us these coeﬃcients as a linear combination of the
values f (k), with k = 0, 1, 2, . . . , b − 1. Thus F(f ) is a linear transformation of

140 7 Finite Fourier Analysis

the function f , thought of as a vector in VG. In other words, we have shown
that F(f ) is a one-to-one and onto linear transformation of VG.
The vector space VG is a vector space of dimension b; indeed, an explicit
basis can easily be given for VG using the delta functions (see Exercise 7.7)
deﬁned by
 δm(x) :=
 {1 if x = m + kb, for some integer k,
0 otherwise.

In other words, δm(x) is the periodic function on Z that picks out the arith-
metic progression {m + kb : k ∈ Z}.
But there is another natural basis for VG. For a ﬁxed integer a, the roots
of unity {ea(x) := e2πiax/b : x ∈ Z} can be thought of as a single function
ea(x) ∈ VG because of its periodicity on Z. As we saw in Theorem 7.2, the
functions {e1(x), . . . , eb(x)} give a basis for the vector space of functions VG.
A natural question now arises: how are the two bases related to each other?
An initial observation is
 ̂δa(n) = 1
b e
−2πian/b,

which simply follows from the computation

̂δa(n) = 1
b
 b−1∑

k=0 δa(k) ξ−kn = 1
b ξ−an = 1
b e−2πian/b.

So to get from the ﬁrst basis to the second basis, we need precisely the ﬁnite
Fourier transform!
It is extremely useful to deﬁne the following inner product on the vector
space VG:
 ⟨f, g⟩ =
 b−1∑

k=0 f (k) g(k) , (7.6)

for two functions f, g ∈ VG. Here the bar denotes complex conjugation. The
following elementary properties show that ⟨f, g⟩ is an inner product (see
Exercise 7.8):

1. ⟨f, f ⟩ ≥ 0, with equality if and only if f = 0, the zero function.
2. ⟨f, g⟩ = ⟨g, f ⟩.

Equipped with this inner product, VG can now be regarded as a metric space:
We can measure distances between two functions, and in particular between
two basis elements ea(x) := e2πiax/b and ec(x) := e2πicx/b. Every positive
deﬁnite inner product gives rise to the distance function √⟨f − g, f − g⟩.

7.4 The Parseval Identity 141

Lemma 7.5 (Orthogonality relations).

1
b ⟨ea, ec⟩ = δa(c) =
 {
1 if b | (a − c),
0 otherwise.

Proof. We compute the inner product

⟨ea, ec⟩ =
 b−1∑

m=0 ea(m) ec(m) =
 b−1∑

m=0 e2πi(a−c)m/b.

If b | (a − c), then each term equals 1 in the latter sum, and hence the sum
equals b. This veriﬁes the ﬁrst case of the lemma.
If b ∤ (a − c), then ea−c(m) = e2πim(a−c)/b is a nontrivial root of unity, and
we have the ﬁnite geometric series

b−1∑

m=0 e
 2πi(a−c)m
b = eb 2πi(a−c)
b − 1

e 2πi(a−c)
b − 1 = 0 ,

verifying the second case of the lemma. ⊓⊔

Example 7.6. We recall the sawtooth function again, since it is one of the
building blocks of lattice-point enumeration, and compute its Fourier trans-
form. Namely, we deﬁne

B(k) := (( k
b
 )) =
 {{ k
b } − 1
2 if k
b /∈ Z,
0 if k
b ∈ Z,

a periodic function on the integers with period b. What is its ﬁnite Fourier
transform? We have already seen the answer, in the course of the proof of
Lemma 7.3: ̂B(n) = 1
2b 1 + ξn

1 − ξn = i
2b cot πn
b

for n ̸= 0 and ̂B(0) = 0. As always, ξ = e2πi/b. ⊓⊔

In the next section, we delve more deeply into the behavior of this inner
product, where the Parseval identity is proved.

7.4 The Parseval Identity

A nontrivial property of the inner product deﬁned above is the following
identity, linking the “norm of a function” to the “norm of its Fourier transform.”
It is known as the Parseval identity, and also goes by the name of the Plancherel
theorem.

142 7 Finite Fourier Analysis

Theorem 7.7 (Parseval identity). For all f ∈ VG,

⟨f, f ⟩ = b ⟨ ˆf , ˆf ⟩ .

Proof. Using the deﬁnition em(x) = ξmx and the relation

ˆf (x) = 1
b
 b−1∑

m=0 f (m) em(x)

from Theorem 7.2,

⟨ ˆf , ˆf ⟩ =
 〈 1
b
 b−1∑

m=0 f (m) em , 1
b
 b−1∑

n=0 f (n) en
 〉

= 1
b2
 b−1∑

k=0
 b−1∑

m=0 f (m) em(k)
 b−1∑

n=0 f (n) en(k)

= 1
b2
 b−1∑

m=0
 b−1∑

n=0 f (m) f (n) ⟨em, en⟩

= 1
b
 b−1∑

m=0
 b−1∑

n=0 f (m) f (n) δm(n)

= 1
b ⟨f, f ⟩ ,

where the essential step in the proof was using the orthogonality relations
(Lemma 7.5) in the fourth equality above. ⊓⊔

A basically identical proof yields the following stronger result, showing
that the “distance between two functions” is essentially equal to the “distance
between their Fourier transforms.”

Theorem 7.8. For all f, g ∈ VG,

⟨f, g⟩ = b ⟨ ˆf , ˆg⟩ . ⊓⊔

Example 7.9. A nice application of the generalized Parseval identity above
now gives us Lemma 7.4 very quickly, the reformulation of the Dedekind sum
as a sum over roots of unity. Namely, we ﬁrst ﬁx an integer a relatively prime
to b and deﬁne f (k) = (( k
b )) and g(k) = (( ka
b )). Then, using Example 7.6,
ˆf (n) = i
2b cot πn
b . To ﬁnd the Fourier transform of g, we need an extra twist.
Since (( ka
b
 )) = i
2b
 b−1∑

m=1 cot πm
b ξmka,

we can multiply each index m by a−1, the multiplicative inverse of a modulo
b (recall that we require a and b to be relatively prime for the reformulation

7.5 The Convolution of Finite Fourier Series 143

of the Dedekind sum). Since a−1 is relatively prime to b, this multiplication
just permutes m = 1, 2, . . . , b − 1 modulo b, but the sum remains invariant
(see Exercise 1.9):

b−1∑

m=1 cot πm
b ξmka =
 b−1∑

m=1 cot πma
−1

b ξma
−1ka =
 b−1∑

m=1 cot πma
−1

b ξmk,

that is,
 ˆg(n) = i
2b cot πna
−1

b .

Hence Theorem 7.8 immediately gives us the reformulation of the Dedekind
sum:
 s(a, b) :=
 b−1∑

k=0
 (( k
b
 )) (( ka
b
 ))

= b
 b−1∑

m=1
 ( i
2b cot πm
b
 ) ( i
2b cot πma−1

b
 )

= 1
4b
 b−1∑

m=1 cot πm
b cot πma
−1

b

= 1
4b
 b−1∑

m=1 cot πma
b cot πm
b .

For the last equality, we again used the trick of replacing m by ma. ⊓⊔

7.5 The Convolution of Finite Fourier Series

Another basic tool in ﬁnite Fourier analysis is the convolution of two ﬁnite
Fourier series. Namely, suppose f and g are periodic functions with period b.
We deﬁne the convolution of f and g by

(f ∗ g)(t) :=
 b−1∑

m=0 f (t − m) g(m) .

Indeed, it is this convolution tool (the proof of the convolution theorem
below is almost trivial) that is responsible for the fastest known algorithm for
multiplying two polynomials of degree b in O(b log(b)) steps (see the notes at
the end of this chapter).

Theorem 7.10 (Convolution theorem for ﬁnite Fourier series). Let
f (t) = 1
b ∑b−1
k=0 ak ξkt and g(t) = 1
b ∑b−1
k=0 ck ξkt, where ξ = e2πi/b. Then their

144 7 Finite Fourier Analysis

convolution satisﬁes
 (f ∗ g)(t) = 1
b
 b−1∑

k=0 akck ξkt.

Proof. The proof is straightforward: we just compute the left-hand side, and
obtain
 b−1∑

m=0 f (t − m)g(m) = 1
b2
 b−1∑

m=0
 (b−1∑

k=0 ak ξk(t−m)) (b−1∑

l=0 cl ξlm)

= 1
b2
 b−1∑

k=0
 b−1∑

l=0 akcl
 ( b−1∑

m=0 ξkt+(l−k)m)

= 1
b
 b−1∑

k=0 akck ξkt,

because the sum ∑b−1
m=0 ξ(l−k)m vanishes, unless l = k (see Exercise 7.6). In
the case that l = k, we have ∑b−1
m=0 ξ(l−k)m = b. ⊓⊔

It is an easy exercise (Exercise 7.23) to show that this convolution theorem
is equivalent to the following statement:

F(f ∗ g) = b F(f ) F(g) .

Note that the proof of Theorem 7.10 is essentially identical to the proof of
Lemma 7.4 above; we could have proved the lemma, in fact, by applying the
convolution theorem. We now show how Theorem 7.10 can be used to derive
identities on trigonometric functions.

Example 7.11. We claim that

b−1∑

k=1 cot
2 ( πk
b
 ) = (b − 1)(b − 2)
3 .

The sum suggests the use of the convolution theorem, with a function whose
Fourier coeﬃcients are ak = ck = cot πk
b . But we already know such a function!
It is just the sawtooth function 2b
i (( m
b )). Therefore,

− 1
4b
 b−1∑

k=1 cot
2 ( πk
b
 ) ξkt =
 b−1∑

m=1
 (( t − m
b
 )) (( m
b
 )) ,

where the equality follows from Theorem 7.10. On setting t = 0, we obtain

Notes 145

b−1∑

m=1
 (( −m
b
 )) (( m
b
 )) = −
 b−1∑

m=1
 (( m
b
 )) (( m
b
 ))

= − 1
b2
 b−1∑

m=1 m2 + 1
b
 b−1∑

m=1 m − 1
4 (b − 1)

= − (b − 1)(b − 2)
12b ,

as desired. We used the identity (( −m
b )) = − (( m
b )) in the ﬁrst equality above,
and some algebra was used in the last equality. Notice, moreover, that the
convolution theorem gave us more than we asked for, namely an identity for
every value of t. ⊓⊔

Notes

1. Finite Fourier analysis oﬀers a wealth of applications and is, for example, one
of the main tools in quantum information theory. For the reader interested in
going further than the humble beginnings outlined in this chapter, we heartily
recommend Audrey Terras’s monograph [243].

2. The Dedekind sum is our main motivation for studying ﬁnite Fourier series,
and in fact, Chapter 8 is devoted to a detailed investigation of these sums, in
which the Fourier–Dedekind sums of Chapter 1 also ﬁnally reappear.

3. The reader may consult [156, p. 501] for a proof that two polynomials of
degree N can be multiplied in O(N log N ) steps. The proof of this fact runs
along the following conceptual lines. First, let the two given polynomials of
degree N be f (x) = ∑N
n=0 a(n) xn and g(x) = ∑N
n=0 b(n) xn. Then we know
that f (ξ) and g(ξ) are two ﬁnite Fourier series, and we abbreviate them by
f and g, respectively. We now note that bf g = F(F−1(f ) ∗ F−1(g)). If we
can compute the ﬁnite Fourier transform (and its inverse) quickly, then this
argument shows that we can multiply polynomials quickly. It is a fact of life
that we can compute the Fourier transform of a periodic function of period
N in O(N log N ) steps, by an algorithm known as the fast Fourier transform
(again, see [156] for a complete description).

4. The continuous Fourier transform, deﬁned by ∫ ∞
−∞ f (t) e−2πitx dt, can be
related to the ﬁnite Fourier transform in the following way. We approximate
the continuous integral by discretizing a large interval [0, a]. Precisely, we let
∆ := a
b , and we let tk := k∆ = ka
b . Then

146 7 Finite Fourier Analysis

∫ a

0 f (t) e−2πitx dt ≈
 b∑

k=1 f (tk) e−2πitkx∆ ,

which is in essence a ﬁnite Fourier series for the function f ( a
b x) as a function
of x ∈ Z. Hence ﬁnite Fourier series ﬁnd an application to continuous Fourier
analysis as an approximation tool.

Exercises

Throughout the exercises, we ﬁx an integer b > 1 and let ξ = e2πi/b.

7.1. Show that 1 − xb = ∏b
k=1(1 − ξkx).

7.2. ♣ Show that ∏b−1
k=1(1 − ξk) = b.

7.3. Consider the matrix that arose in the proof of Theorem 7.2, namely
L = (aij), with aij := ξ(i−1)(j−1) and with 1 ≤ i, j ≤ b. Show that the matrix
1√b L is a unitary matrix (recall that a matrix U is unitary if U ∗U = I, where
U ∗ is the conjugate transpose of U ). Thus, this exercise shows that the Fourier
transform of a periodic function is always given by a unitary transformation.

7.4. Show that ∣
∣
∣det ( 1√b L)∣
∣
∣ = 1, where |z| denotes the norm of the complex

number z. (It turns out that det(L) can sometimes be a complex number, but
we will not use this fact here.)

7.5. ♣ Show that for every integer a relatively prime to b,

1
b
 b−1∑

k=1 k ξ−ak = ξa

1 − ξa .

7.6. ♣ Let n be an integer. Show that the sum ∑b−1
k=0 ξkn vanishes, unless
n ≡ 0 (mod b), in which case it is equal to b.

7.7. ♣ For an integer m, recall that we deﬁned the delta function

δm(x) =
 {1 if x = m + ab, for some integer a,
0 otherwise.

The b functions δ1(x), . . . , δb(x) are clearly in the vector space VG, since they
are periodic on Z with period b. Show that they form a basis for VG.

7.8. ♣ Prove that for all f, g ∈ VG:

(a) ⟨f, f ⟩ ≥ 0, with equality if and only if f = 0, the zero function.

Exercises 147

(b) ⟨f, g⟩ = ⟨g, f ⟩.

7.9. Show that ∑b−1
k=1 1
1−ξk = b−1
2 .

7.10. Show that ⟨δa, δc⟩ = δa(c).

7.11. Prove that (f ∗ δa)(x) = f (x − a).

7.12. Prove that δa ∗ δc = δ(a+c) mod b .

7.13. Let g(x) = x − a. Prove that ̂f ◦ g(x) = ̂f (x) e− 2πiax
b .

7.14. Show that the Fourier transform can have only the eigenvalues ±1, ±i.

7.15. ♣ Prove that for every real number x, ((x)) = ∑b−1
k=0 (( x+k
b )).

7.16. If x is not an integer, show that ∑b−1
n=0 cot (π n+x
b ) = b cot (πx).

7.17. Show that for every integer a relatively prime to b,

∑

ξ
 ξa+1 − 1
(ξa − 1)(ξ − 1) = 0 ,

where the sum is taken over all bth roots of unity ξ except ξ = 1.

7.18. We call a root of unity e2πia/b a primitive bth root of unity if a is
relatively prime to b. Let Φb(x) denote the polynomial with leading coeﬃcient
1 and of degree φ(b)1 whose roots are the φ(b) distinct primitive bth roots
of unity. This polynomial is known as the cyclotomic polynomial of order b.
Show that ∏

d|b Φd(x) = xb − 1 ,

where the product is taken over all positive divisors d of b.

7.19. We deﬁne the M¨obius function for positive integers n by

µ(n) =
 




1 if n = 1,
0 if n is divisible by a square,
(−1)k if n is square-free and has k prime divisors.

Deduce from the previous exercise that

Φb(x) = ∏

d|b
 (xd − 1
)µ(b/d) .

1 φ(b) := # {k ∈ [1, b − 1] : gcd(k, b) = 1} is the Euler φ-function.

148 7 Finite Fourier Analysis

7.20. Prove that for every positive integer b,
∑

1≤a≤b
gcd(a,b)=1
 e2πia/b = µ(b) ,

the M¨obius function.

7.21. Show that for every positive integer k,

s(1, k) = (k − 1)(k − 2)
12k .

7.22. Show that, if b is odd, then ∑b−1
k=1 tan
2 ( πk
b ) = b(b − 1).

7.23. ♣ Show that Theorem 7.10 is equivalent to the following statement:

F(f ∗ g) = b F(f ) F(g) .

7.24. Consider the trace of the linear transformation L = (ξ(i−1)(j−1)), de-
ﬁned in (7.3). The trace of L is G(b) := ∑b−1
m=0 ξm2, known as a Gauß sum.
Show that |G(b)| = √b if b is an odd prime.

Chapter 8
Dedekind Sums, the Building Blocks of
Lattice-Point Enumeration

If things are nice there is probably a good reason why they are nice: and if you don’t know
at least one reason for this good fortune, then you still have work to do.

Richard Askey

We encountered Dedekind sums in our study of ﬁnite Fourier analysis in
Chapter 7, and we became intimately acquainted with their siblings in our
study of the coin-exchange problem in Chapter 1. They have one shortcoming,
however (which we shall remove): the deﬁnition of s(a, b) requires us to sum
over b terms, which is rather slow when b = 2
100, for example. Luckily, there
is a magical reciprocity law for the Dedekind sum s(a, b) that allows us to
compute it in roughly log2(b) = 100 steps, in the example above. This is the
kind of magic that saves the day when we try to enumerate lattice points in
integral polytopes of dimension d ≤ 4. There is an ongoing eﬀort to extend
these ideas to higher dimensions, but there is much room for improvement. In
this chapter, we focus on the computational-complexity issues that arise when
we try to compute Dedekind sums explicitly. In many ways, the Dedekind
sums extend the notion of the greatest common divisor of two integers.

8.1 Fourier–Dedekind Sums and the Coin-Exchange
Problem Revisited

Recall from Chapter 1 the Fourier–Dedekind sum (deﬁned in (1.13))

sn (a1, a2, . . . , ad; b) = 1
b
 b−1∑

k=1
 ξkn
b(1 − ξka1
b ) (
1 − ξka2
b ) · · · (1 − ξkad
b ) ,
 149

150 8 Dedekind Sums

which appeared as a main player in our analysis of the Frobenius coin-
exchange problem. We can now recognize the Fourier–Dedekind sums as
honest ﬁnite Fourier series with period b. The Fourier–Dedekind sums unify
many variations of the Dedekind sum that have appeared in the literature, and
form the building blocks of Ehrhart quasipolynomials. For example, we showed
in Chapter 1 that sn (a1, a2, . . . , ad; b) appears in the Ehrhart quasipolynomial
of the d-simplex
{
(x1, . . . , xd+1) ∈ Rd+1
≥0 : a1x1 + · · · + adxd + bxd+1 = 1
} .

Example 8.1. We ﬁrst notice that when n = 0 and d = 2, the Fourier–
Dedekind sum reduces to a classical Dedekind sum (which—ﬁnally—explains
the name): for relatively prime positive integers a and b,

s0(a, 1; b) = 1
b
 b−1∑

k=1
 1
(1 − ξka
b ) (
1 − ξk
b )

= 1
b
 b−1∑

k=1
 ( 1
1 − ξka
b − 1
2
 ) ( 1
1 − ξk
b − 1
2
 )

+ 1
2b
 b−1∑

k=1
 1
1 − ξk
b + 1
2b
 b−1∑

k=1
 1
1 − ξka
b − 1
b
 b−1∑

k=1
 1
4

= 1
4b
 b−1∑

k=1
 ( 1 + ξka
b
1 − ξka
b
 ) ( 1 + ξk
b
1 − ξk
b
 ) + 1
b
 b−1∑

k=1
 1
1 − ξk
b − b − 1
4b .

In the last step, we used the fact that multiplying the index k by a does
not change the middle sum. This middle sum can be further simpliﬁed by
recalling (1.8):
 1
b
 b−1∑

k=1
 1
(1 − ξk
b ) ξkn
b = − { n
b
 } + 1
2 − 1
2b ,

whence
 s0(a, 1; b) = 1
4b
 b−1∑

k=1
 ( 1 + ξka
b
1 − ξka
b
 ) ( 1 + ξk
b
1 − ξk
b
 ) + 1
2 − 1
2b − b − 1
4b

= − 1
4b
 b−1∑

k=1 cot ( πka
b
 ) cot ( πk
b
 ) + b − 1
4b (8.1)

= −s(a, b) + b − 1
4b . ⊓⊔

Example 8.2. The next special evaluation of a Fourier–Dedekind sum is
very similar to the computation above, so we leave it to the reader to prove

8.1 Fourier–Dedekind Sums and the Coin-Exchange Problem Revisited 151

(Exercise 8.7) that for a1, a2 relatively prime to b,

s0 (a1, a2; b) = −s (a1a
−1
2 , b
) + b − 1
4b , (8.2)

where a
−1
2 a2 ≡ 1 mod b. ⊓⊔

Returning to the general Fourier–Dedekind sum, we now prove the ﬁrst of
a series of reciprocity laws: identities for certain sums of Fourier–Dedekind
sums. We ﬁrst recall how these sums came up in Chapter 1, namely, from the
partial fraction expansion of the function

f (z) = 1
(1 − za1) · · · (1 − zad ) zn

= A1
z + A2
z2 + · · · + An
zn + B1
z − 1 + B2
(z − 1)2 + · · · + Bd
(z − 1)d (8.3)

+
 a1−1∑

k=1
 C1k
z − ξk
a1 +
 a2−1∑

k=1
 C2k
z − ξk
a2 + · · · +
 ad−1∑

k=1
 Cdk
z − ξk
ad .

(Here we assume that a1, a2, . . . , ad are pairwise relatively prime.) Theorem 1.8
states that with the help of the partial fraction coeﬃcients B1, . . . , Bd and
Fourier–Dedekind sums, we can compute the restricted partition function for
A = {a1, a2, . . . , ad}:

pA(n) = −B1 + B2 − · · · + (−1)
dBd + s−n (a2, a3, . . . , ad; a1)

+ s−n (a1, a3, a4, . . . , ad; a2) + · · · + s−n (a1, a2, . . . , ad−1; ad) .

It is not hard to see that B1, B2, . . . , Bd are polynomials in n (Exercise 8.8),
whence we call
 polyA(n) := −B1 + B2 − · · · + (−1)dBd

the polynomial part of the restricted partition function pA(n). These poly-
nomials can be computed from ﬁrst principles (and we give some of them
in Example 8.3) but in fact, they are relatives of the Bernoulli polynomials,
which we deﬁned in (2.8) in Section 2.4: We deﬁne the Bernoulli–Barnes
polynomials BA
k (x) through the generating function

zdexz

(ea1z − 1) (ea2z − 1) · · · (eadz − 1) = ∑

k≥0 BA
k (x) zk

k! ,

where as usual, A = {a1, a2, . . . , ad}. (The Bernoulli polynomials are the
special cases B{1}
k .) Then

polyA(n) = (−1)d−1

(d − 1)! BA
d−1(−n) , (8.4)

152 8 Dedekind Sums

an identity that can be proved most easily with a pinch of complex analysis
(Exercise 14.3 in Chapter 14).

Example 8.3. The ﬁrst few expressions for poly{a1,...,ad}(n) are

poly{a1}(n) = 1
a1 ,

poly{a1,a2}(n) = n
a1a2 + 1
2
 ( 1
a1 + 1
a2
 ) ,

poly{a1,a2,a3}(n) = n2

2a1a2a3 + n
2
 ( 1
a1a2 + 1
a1a3 + 1
a2a3
 ) (8.5)

+ 1
12
 ( 3
a1 + 3
a2 + 3
a3 + a1
a2a3 + a2
a1a3 + a3
a1a2
 ) ,

poly{a1,a2,a3,a4}(n) = n3

6a1a2a3a4

+ n2

4
 ( 1
a1a2a3 + 1
a1a2a4 + 1
a1a3a4 + 1
a2a3a4
 )

+ n
4
 ( 1
a1a2 + 1
a1a3 + 1
a1a4 + 1
a2a3 + 1
a2a4 + 1
a3a4
 )

+ n
12
 ( a1
a2a3a4 + a2
a1a3a4 + a3
a1a2a4 + a4
a1a2a3
 )

+ 1
24
 ( a1
a2a3 + a1
a2a4 + a1
a3a4 + a2
a1a3 + a2
a1a4 + a2
a3a4

+ a3
a1a2 + a3
a1a4 + a3
a2a4 + a4
a1a2 + a4
a1a3 + a4
a2a3
 )

+ 1
8
 ( 1
a1 + 1
a2 + 1
a3 + 1
a4
 ) . ⊓⊔

We are about to combine the Ehrhart results of Chapter 3 with the partial
fraction expansion of Chapter 1 that gave rise to the Fourier–Dedekind sums.

Theorem 8.4 (Zagier reciprocity). For all pairwise relatively prime posi-
tive integers a1, a2, . . . , ad,

s0 (a2, a3, . . . , ad; a1) + s0 (a1, a3, a4, . . . , ad; a2) + · · ·

+ s0 (a1, a2, . . . , ad−1; ad)

= 1 − poly{a1,a2,...,ad}(0) .

At ﬁrst sight, this reciprocity law should come as a surprise. The Fourier–
Dedekind sums can be long, complicated sums, yet when combined in this
fashion, they add up to a trivial rational function in a1, a2, . . . , ad.

Proof. We compute the constant term of the quasipolynomial pA(n):

8.2 The Dedekind Sum and Its Reciprocity and Computational Complexity 153

pA(0) = polyA(0) + s0 (a2, a3, . . . , ad; a1)

+ s0 (a1, a3, a4, . . . , ad; a2) + · · · + s0 (a1, a2, . . . , ad−1; ad) .

On the other hand, Exercise 3.32 (the extension of Corollary 3.15 to Ehrhart
quasipolynomials) states that pA(0) = 1, whence

1 = polyA(0) + s0 (a2, a3, . . . , ad; a1)

+ s0 (a1, a3, a4, . . . , ad; a2) + · · · + s0 (a1, a2, . . . , ad−1; ad) . ⊓⊔

8.2 The Dedekind Sum and Its Reciprocity and
Computational Complexity

We derived in (8.1) the classical Dedekind sum s(a, b) as a special evaluation
of the Fourier–Dedekind sum. Naturally, Theorem 8.4 takes on a particular
form when we specialize this reciprocity law to the classical Dedekind sum.

Corollary 8.5 (Dedekind’s reciprocity law). For all relatively prime pos-
itive integers a and b,

s(a, b) + s(b, a) = 1
12
 ( a
b + b
a + 1
ab
 ) − 1
4 .

Proof. A special case of Theorem 8.4 is

s0(a, 1; b) + s0(b, a; 1) + s0(1, b; a) = 1 − poly{a,1,b}(0)

= 1 − 1
12
 ( 3
a + 3 + 3
b + a
b + 1
ab + b
a
 )

= 3
4 − 1
12
 ( a
b + b
a + 1
ab
 ) − 1
4a − 1
4b .

Now we use the fact that s0(b, a; 1) = 0 and the identity (8.1):

s0(a, 1; b) = −s(a, b) + 1
4 − 1
4b . ⊓⊔

Dedekind’s reciprocity law allows us to compute the Dedekind sum s(a, b)
as quickly as the gcd algorithm for a and b, also known as the Euclidean
algorithm. Let’s get a better feeling for the way we can compute the Dedekind
sum by working out an example. We remind the reader of another crucial
property of the Dedekind sums that we already pointed out in (7.5): s(a, b)
remains invariant when we replace a by its residue modulo b, that is,

s(a, b) = s(a mod b, b) . (8.6)

154 8 Dedekind Sums

Example 8.6. Let a = 100 and b = 147. Now we alternately use Corollary 8.5
and the reduction identity (8.6):

s(100, 147) = 1
12
 ( 100
147 + 147
100 + 1
14700
 ) − 1
4 − s(147, 100)

= − 1249
17640 − s(47, 100)

= − 1249
17640 − ( 1
12
 ( 47
100 + 100
47 + 1
4700
 ) − 1
4 − s(100, 47)
)

= − 773
20727 + s(6, 47)

= − 773
20727 + 1
12
 ( 6
47 + 47
6 + 1
282
 ) − 1
4 − s(47, 6)

= 166
441 − s(5, 6)

= 166
441 − ( 1
12
 ( 5
6 + 6
5 + 1
30
 ) − 1
4 − s(6, 5))

= 2003
4410 + s(1, 5)

= 2003
4410 − 1
4 + 1
30 + 5
12

= 577
882 .

In the last step, we used Exercise 7.21: s(1, k) = − 1
4 + 1
6k + k
12 . A priori,
s(100, 147) takes 147 steps to compute, whereas we were able to compute it
in nine steps using Dedekind’s reciprocity law and (8.6). ⊓⊔

As a second corollary to Theorem 8.4, we mention the following three-
term reciprocity law for the special Fourier–Dedekind sum s0(a, b; c). This
reciprocity law could be restated in terms of the classical Dedekind sum via
the identity (8.2).

Corollary 8.7. For pairwise relatively prime positive integers a, b, and c,

s0(a, b; c) + s0(c, a; b) + s0(b, c; a) = 1 − 1
12
 ( 3
a + 3
b + 3
c + a
bc + b
ca + c
ab
 ) .

⊓⊔

8.3 Rademacher Reciprocity for the Fourier–Dedekind
Sum

The next reciprocity law will be again for the general Fourier–Dedekind sums.
It extends Theorem 8.4 beyond n = 0.

8.3 Rademacher Reciprocity for the Fourier–Dedekind Sum 155

Theorem 8.8 (Rademacher reciprocity). Let a1, a2, . . . , ad be pairwise
relatively prime positive integers. Then for n = 1, 2, . . . , (a1 + · · · + ad − 1),

sn (a2, a3, . . . , ad; a1) + sn (a1, a3, a4, . . . , ad; a2) + · · ·

+ sn (a1, a2, . . . , ad−1; ad) = − poly{a1,a2,...,ad}(−n) .

Proof. We recall the deﬁnition

p
◦
A(n) = # {(m1, . . . , md) ∈ Z
d : all mj > 0, m1a1 + · · · + mdad = n}

of Exercise 1.33, that is, p
◦
A(n) counts the number of partitions of n using
only the elements of A as parts, where each part is used at least once. This
counting function is, naturally, connected to pA through Ehrhart–Macdonald
reciprocity (Theorem 4.1):

p
◦
A(n) = (−1)d−1pA(−n) ,

that is,

(−1)d−1p◦
A(n) = polyA(−n) + sn (a2, a3, . . . , ad; a1)

+ sn (a1, a3, a4, . . . , ad; a2) + · · · + sn (a1, a2, . . . , ad−1; ad) .

On the other hand, by its very deﬁnition,

p
◦
A(n) = 0 for n = 1, 2, . . . , (a1 + · · · + ad − 1) ,

so that for those n,

0 = polyA(−n) + sn (a2, a3, . . . , ad; a1)

+ sn (a1, a3, a4, . . . , ad; a2) + · · · + sn (a1, a2, . . . , ad−1; ad) . ⊓⊔

Just as Zagier reciprocity takes on a special form for the classical Dedekind
sum, Rademacher reciprocity specializes for d = 2 to a reciprocity identity for
the Dedekind–Rademacher sum

rn(a, b) :=
 b−1∑

k=0
 (( ka + n
b
 )) (( k
b
 )) .

The classical Dedekind sum is, naturally, the specialization r0(a, b) = s(a, b).
To be able to state the reciprocity law for the Dedekind–Rademacher sums,
we deﬁne the function
 χa(n) :=
 {
1 if a|n,
0 otherwise,

which will come in handy as a bookkeeping device.

156 8 Dedekind Sums

Corollary 8.9 (Reciprocity law for Dedekind–Rademacher sums).
Let a and b be relatively prime positive integers. Then for n = 1, 2, . . . , a + b,

rn(a, b) + rn(b, a) = n2

2ab − n
2
 ( 1
ab + 1
a + 1
b
 ) + 1
12
 ( a
b + b
a + 1
ab
 )

+ 1
2
 ((( a
−1n
b
 )) + (( b−1n
a
 )) + (( n
a
 )) + (( n
b
 )))

+ 1
4 (1 + χa(n) + χb(n)) ,

where a
−1a ≡ 1 mod b and b−1b ≡ 1 mod a.

This identity follows almost instantly once we are able to express the
Dedekind–Rademacher sum in terms of Fourier–Dedekind sums.

Lemma 8.10. Suppose a and b are relatively prime positive integers and
n ∈ Z. Then

rn(a, b) = −sn(a, 1; b) + 1
2
 (( n
b
 )) + 1
2
 (( na−1

b
 )) − 1
4b + 1
4 χb(n) ,

where a
−1a ≡ 1 mod b.

Proof. We begin by rewriting the ﬁnite Fourier series (1.8) for the sawtooth
function ((x)):

1
b
 b−1∑

k=1
 ξkn
b
1 − ξk
b = − { −n
b
 } + 1
2 − 1
2b = − (( −n
b
 )) + 1
2 χb(n) − 1
2b

= (( n
b
 )) + 1
2 χb(n) − 1
2b .

Hence we also have

1
b
 b−1∑

k=1
 ξkn
b
1 − ξka
b = 1
b
 b−1∑

k=1
 ξka−1n
b
1 − ξk
b = (( a
−1n
b
 )) + 1
2 χb (a−1n
) − 1
2b

= (( a
−1n
b
 )) + 1
2 χb (n) − 1
2b .

Now we use the convolution theorem for ﬁnite Fourier series (Theorem 7.10)
for the functions

f (n) := 1
b
 b−1∑

k=1
 ξkn
b
1 − ξk
b and g(n) := 1
b
 b−1∑

k=1
 ξkn
b
1 − ξka
b .

It gives

8.3 Rademacher Reciprocity for the Fourier–Dedekind Sum 157

1
b
 b−1∑

k=1
 ξkn
b(1 − ξk
b ) (
1 − ξka
b ) =
 b−1∑

m=0 f (n − m) g(m) =

b−1∑

m=0
 ((( n − m
b
 )) + 1
2 χb(n − m) − 1
2b
 ) ((( a
−1m
b
 )) + 1
2 χb (m) − 1
2b
 ) .

We invite the reader to check (Exercise 8.12) that the sum on the right-hand
side simpliﬁes to

−
 b−1∑

m=0
 (( am + n
b
 )) (( m
b
 )) + 1
2
 (( a
−1n
b
 )) + 1
2
 (( n
b
 )) − 1
4b + 1
4 χb(n) ,

whence

sn(a, 1; b) = −rn(a, b) + 1
2
 (( a
−1n
b
 )) + 1
2
 (( n
b
 )) − 1
4b + 1
4 χb(n) . ⊓⊔

Proof of Corollary 8.9. We use the following special case of Theorem 8.8:

sn(a, 1; b) + sn(1, a; b) + sn(a, b; 1) = − poly{a,1,b}(−n)

= − n2

2ab + n
2
 ( 1
ab + 1
a + 1
b
 ) − 1
12
 ( 3
a + 3
b + 3 + a
b + b
a + 1
ab
 ) ,

which holds for n = 1, 2, . . . , a + b. Lemma 8.10 allows us to translate this
identity into one for Dedekind–Rademacher sums:

rn(a, b) + rn(b, a) = n2

2ab − n
2
 ( 1
ab + 1
a + 1
b
 ) + 1
12
 ( a
b + b
a + 1
ab
 )

+ 1
2
 ((( a
−1n
b
 )) + (( b−1n
a
 )) + (( n
a
 )) + (( n
b
 )))

+ 1
4 (1 + χa(n) + χb(n)) . ⊓⊔

The two-term reciprocity law allows us to compute the Dedekind–-
Rademacher sum as quickly as the gcd algorithm, just as obtained for the
classical Dedekind sum. This fact has an interesting consequence: In Theo-
rem 2.10 and Exercise 2.36, we showed implicitly (see Exercise 8.13) that
Dedekind–Rademacher sums are the only nontrivial ingredients of the Ehrhart
quasipolynomials of rational polygons. Corollary 8.9 ensures that these Ehrhart
quasipolynomials can be computed almost instantly.

158 8 Dedekind Sums

8.4 The Mordell–Pommersheim Tetrahedron

In this section, we return to Ehrhart polynomials and illustrate how Dedekind
sums appear naturally in generating-function computations. We will study
the tetrahedron that historically ﬁrst gave rise to the connection of Dedekind
sums and lattice-point enumeration in polytopes. It is given by

P = {
(x, y, z) ∈ R3 : x, y, z ≥ 0, x
a + y
b + z
c ≤ 1
} , (8.7)

a tetrahedron with vertices (0, 0, 0), (a, 0, 0), (0, b, 0), and (0, 0, c), where a, b, c
are positive integers. We insert the slack variable n and interpret

LP (t) = # {(k, l, m) ∈ Z
3 : k, l, m ≥ 0, k
a + l
b + m
c ≤ t}

= # {
(k, l, m, n) ∈ Z
4 : k, l, m, n ≥ 0, bck + acl + abm + n = abct
}

as the Taylor coeﬃcient of zabct for the function


∑

k≥0 zbck



 


∑

l≥0 zacl



 

 ∑

m≥0 zabm



 

∑

n≥0 zn




= 1
(1 − zbc) (1 − zac) (1 − zab) (1 − z) .

As we have done numerous times before, we shift this coeﬃcient to the constant
term:
 LP (t) = const ( 1
(1 − zbc) (1 − zac) (1 − zab) (1 − z) zabct
 ) .

To reduce the number of poles, it is convenient to change this function slightly;
the constant term of 1/(1 − zbc)(1 − zac)(1 − zab)(1 − z) is 1, so that

LP (t) = const ( z−abct − 1
(1 − zbc) (1 − zac) (1 − zab) (1 − z)
 ) + 1 .

This trick becomes useful in the next step, namely expanding the function into
partial fractions. Strictly speaking, we cannot do that, since the numerator
is not a polynomial in z. However, we can think of this rational function as
a sum of two functions. The higher-order poles of both summands that we
will not include in our computation below cancel each other, so we can ignore
them at this stage. The only poles of

z−abct − 1
(1 − zbc) (1 − zac) (1 − zab) (1 − z) (8.8)

8.4 The Mordell–Pommersheim Tetrahedron 159

are at the ath, b
th, cth roots of unity and at 0. (As before, we do not have to
bother with the coeﬃcients of z = 0 of the partial fraction expansion.) To
make life momentarily easier (the general case is the subject of Exercise 8.18),
let’s assume that a, b, and c are pairwise relatively prime; then all the poles
besides 0 and 1 are simple. The computation of the coeﬃcients for z = 1 is
very similar to what we did with the restricted partition function in Chapter 1.
The coeﬃcient in the partial fraction expansion of a nontrivial root of unity,
say ξk
a , is also computed practically as easily as in earlier examples: it is

− t
a (1 − ξkbc
a ) (1 − ξk
a ) (8.9)

(see Exercise 8.15). Summing this fraction over k = 1, 2, . . . , a − 1 gives rise
to the Fourier–Dedekind sum

− t
a
 a−1∑

k=1
 1
(1 − ξkbc
a ) (1 − ξk
a ) = −t s0 (bc, 1; a) .

Putting this coeﬃcient and its siblings for the other roots of unity into the
partial fraction expansion and computing the constant term yields (Exer-
cise 8.15)

LP (t) = abc
6 t
3 + ab + ac + bc + 1
4 t
2

+ ( a + b + c
4 + 1
4
 ( 1
a + 1
b + 1
c
 ) + 1
12
 ( bc
a + ca
b + ab
c + 1
abc
 )) t

+ (s0 (bc, 1; a) + s0 (ca, 1; b) + s0 (ab, 1; c)) t

+ 1 .

We recognize instantly that the Fourier–Dedekind sums in this Ehrhart
polynomial are in fact classical Dedekind sums by (8.1), and so we arrive at
the following celebrated result.

Theorem 8.11. Let P be given by (8.7) with a, b, and c pairwise relatively
prime. Then

LP (t) = abc
6 t3 + ab + ac + bc + 1
4 t2 + ( 3
4 + a + b + c
4

+ 1
12
 ( bc
a + ca
b + ab
c + 1
abc
 ) − s (bc, a) − s (ca, b) − s (ab, c)) t + 1 .

⊓⊔

We ﬁnish this chapter by giving the Ehrhart series of the Mordell–Pommers-
heim tetrahedron P. It follows simply from the transformation formulas
(computing the Ehrhart numerator coeﬃcients from the Ehrhart polynomial

160 8 Dedekind Sums

coeﬃcients) of Corollary 3.16 and Exercise 3.15, and hence the Ehrhart series
of P naturally contains Dedekind sums.

Corollary 8.12. Let P be given by (8.7) with a, b, and c pairwise relatively
prime. Then
 EhrP (z) = h
∗
3 z3 + h
∗
2 z2 + h
∗
1 z + 1
(1 − z)4 ,

where

h
∗
3 = abc
6 − ab + ac + bc + 1
4 + a + b + c
4 + 1
12
 ( bc
a + ca
b + ab
c + 1
abc
 )

− (s (bc, a) + s (ca, b) + s (ab, c))

h
∗
2 = 2abc
3 − a + b + c
2 + 3
2 − 1
6
 ( bc
a + ca
b + ab
c + 1
abc
 )

+ 2 (s (bc, a) + s (ca, b) + s (ab, c))

h
∗
1 = abc
6 + ab + ac + bc + a + b + c
4 − 9
4 + 1
12
 ( bc
a + ca
b + ab
c + 1
abc
 )

− (s (bc, a) + s (ca, b) + s (ab, c)) . ⊓⊔

It is a curious fact that the above expressions for h
∗
1, h
∗
2, and h∗
3 are
nonnegative integers due to Corollary 3.11.

Notes

1. The classical Dedekind sums came to life in the 1880s when Richard
Dedekind (1831–1916)
1 studied the transformation properties of the Dedekind
η-function [100] η(z) := e πiz
12 ∏

n≥1
 (1 − e2πinz) ,

a useful computational gadget in the land of modular forms in number theory.
Dedekind’s reciprocity law (Corollary 8.5) follows from one of the functional
transformation identities for η. Dedekind also proved that

12k s(h, k) ≡ k + 1 − 2 ( h
k
 ) (mod 8) ,

establishing a beautiful connection between the Dedekind sum and the Jacobi
symbol ( h
k ) (the reader may want to consult the lovely Carus monograph
Dedekind Sums, by Emil Grosswald and Hans Rademacher, where the above
result is proved [200, p. 34]), and then used this identity to show that the

1 For more information about Dedekind, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Dedekind.html.

Notes 161

reciprocity law for the Dedekind sums (for which [200] contains several diﬀerent
proofs) is equivalent to the reciprocity law for the Jacobi symbol.

2. The Dedekind sums and their generalizations appear in various contexts
besides analytic number theory and discrete geometry. Other mathematical
areas in which Dedekind sums show up include topology [141, 177, 256],
algebraic number theory [175, 223], and algebraic geometry [118]. They also
have connections to algorithmic complexity [154] and continued fractions
[17, 137, 184].

3. The reciprocity laws (Theorems 8.4 and 8.8) for the Fourier–Dedekind sums
were proved in [38], though the connection to Bernoulli–Barnes polynomials
was noticed only in [28]. On the other hand, the appearance of Bernoulli–
Barnes polynomials as part of the restricted partition function goes back to
an 1857 paper by Sylvester [238]—almost 50 years before Barnes introduced
Bernoulli–Barnes polynomials [19]. Theorem 8.4 is equivalent to the reciprocity
law for Don Zagier’s higher-dimensional Dedekind sums [256]. Corollary 8.7
(stated in terms of the classical Dedekind sum) is originally due to Hans
Rademacher [198]. Theorem 8.8 generalizes reciprocity laws by Rademacher
[199] (essentially Corollary 8.9) and Ira Gessel [120].

4. The Fourier–Dedekind sums form only one set of generalizations of the
classical Dedekind sums. A long, but by no means complete, list of other
generalizations is [8, 9, 29, 32, 34, 40, 52–54, 81, 82, 108, 109, 120, 129, 131, 153,
175–177, 199, 242, 256].

5. The connection of Dedekind sums and lattice-point problems, namely
Theorem 8.11 for t = 1, was ﬁrst established by Louis Mordell in 1951 [182].
Some 42 years later, James Pommersheim established a proof of Theorem 8.11
as part of a much more general machinery [194]. In fact, Pommersheim’s work
implies that the classical Dedekind sum is the only nontrivial ingredient one
needs for Ehrhart polynomials in dimensions 3 and 4.

6. We touched the question of eﬃcient computability of Ehrhart (quasi-)po-
lynomials in this chapter. Unfortunately, our current state of knowledge on
generalized Dedekind sums does not suﬃce to make any general statement.
However, Alexander Barvinok proved in 1994 [25] that in ﬁxed dimension,
the rational generating function of the Ehrhart quasipolynomial of a ratio-
nal polytope can be eﬃciently computed. Barvinok’s proof did not employ
Dedekind sums but rather used a decomposition theorem of Brion, which is
the subject of Chapter 11.

162 8 Dedekind Sums

Exercises

8.1. Show that s(a, b) = 0 if and only if a
2 ≡ −1 mod b.

8.2. Prove that 6b s(a, b) ∈ Z. (Hint: Start with rewriting the Dedekind sum
in terms of the greatest-integer function.)

8.3. Prove that s(−a, b) = −s(a, b), for all a ∈ Z with gcd(a, b) = 1.

8.4. For a ﬁxed prime modulus p, show that we can solve s(a, p) = s(b, p) in
integers a, b if and only if a ≡ b mod p or ab ≡ 1 mod p.

8.5. Let a and b be any two relatively prime positive integers. Show that the
reciprocity law for the Dedekind sums implies that for b ≡ r mod a,

12ab s(a, b) = −12ab s(r, a) + a
2 + b2 − 3ab + 1 .

Deduce the following identities:

(a) For b ≡ 1 mod a,

12ab s(a, b) = −a
2b + b2 + a
2 − 2b + 1 .

(b) For b ≡ 2 mod a,

12ab s(a, b) = − 1
2 a
2b + a
2 + b
2 − 5
2 b + 1 .

(c) For b ≡ −1 mod a,

12ab s(a, b) = a
2b + a
2 + b2 − 6ab + 2b + 1 .

8.6. Denote by fn the sequence of Fibonacci numbers, deﬁned as in Chapter 1
by f1 = f2 = 1 and fn+2 = fn+1 + fn for n ≥ 1 .

Prove that s (f2k, f2k+1) = 0

and 12f2k−1f2k s (f2k−1, f2k) = f 2
2k−1 + f 2
2k − 3f2k−1f2k + 1 .

8.7. ♣ Prove (8.2):
 s0(a1, a2; b) = − s (a1a
−1
2 , b
) + b − 1
4b ,

where a
−1
2 a2 ≡ 1 mod b.

8.8. Prove that B1, B2, . . . , Bd in the partial fraction expansion (8.3),

Exercises 163

f (z) = 1
(1 − za1) · · · (1 − zad ) zn

= A1
z + A2
z2 + · · · + An
zn + B1
z − 1 + B2
(z − 1)2 + · · · + Bd
(z − 1)d

+
 a1−1∑

k=1
 C1k
z − ξk
a1 +
 a2−1∑

k=1
 C2k
z − ξk
a2 + · · · +
 ad−1∑

k=1
 Cdk
z − ξk
ad ,

are polynomials in n (of degree less than d) and rational functions in a1, . . . , ad.

8.9. ♣ Verify the ﬁrst few expressions for poly{a1,...,ad}(n) in (8.5).

8.10. Show that the Dedekind–Rademacher sum satisﬁes r−n(a, b) = rn(a, b).

8.11. The deﬁnition s(a, b) := ∑b−1
k=0 (( ka
b )) (( k
b )) of the Dedekind sum may
be extended to encompass all pairs of integers (a, b) with b > 0. Show that if
g := gcd(a, b), then s(a, b) = s( a
g , b
g ). (This exercise shows that the Dedekind
sum may also be thought of as a function of the fraction a
b , deﬁned for any
two integers a and b > 0.)

8.12. ♣ Show that

b−1∑

m=0
 ((( n − m
b
 )) + 1
2 χb(n − m) − 1
2b
 ) ((( a
−1m
b
 )) + 1
2 χb (m) − 1
2b
 )

= −
 b−1∑

m=0
 (( am − n
b
 )) (( m
b
 )) + 1
2
 (( a
−1n
b
 )) + 1
2
 (( −n
b
 )) − 1
4b

+ 1
4 χb(n) .

8.13. Rephrase the Ehrhart quasipolynomials for rational triangles given in
Theorem 2.10 and Exercise 2.36 in terms of Dedekind–Rademacher sums.

8.14. Rephrase the restricted partition p{a,b,c}(n) from Example 1.9 in terms
of Dedekind–Rademacher sums, and use an explicit formula for p{a,1,1}(n) to
derive a formula for rn(1, a).

8.15. ♣ Prove Theorem 8.11 by verifying (8.9) and computing the coeﬃcients
for z = 1 in the partial fraction expansion of (8.8).

8.16. Let P be given by (8.7) with a = k and b = c = 1. Compute LP (t) from
ﬁrst principles and conclude from this an alternative proof of the formula for
s(1, k) given in Exercise 7.21.

8.17. Let P be given by (8.7) with gcd(a, b) = 1 and c = 1. Use Dedekind’s
reciprocity law (Corollary 8.5) to derive from Theorem 8.11 a formula for
LP (t) not depending on Dedekind sums. Can you prove this formula from
ﬁrst principles?

164 8 Dedekind Sums

8.18. Generalize the Ehrhart polynomial of the Mordell–Pommersheim tetra-
hedron given in Theorem 8.11 to the case that a, b, and c are not necessarily
pairwise relatively prime.

8.19. Compute the Ehrhart polynomial of the 4-simplex
{
(x1, x2, x3, x4) ∈ R4
≥0 : x1
a + x2
b + x3
c + x4
d ≤ 1
} ,

where a, b, c, d are pairwise relatively prime positive integers. (Hint: You may
use Corollary 5.5 to compute the linear term.)

8.20. This exercise gives an alternative proof (and extension) of Dedekind’s
reciprocity law (Corollary 8.5) by way of a polynomial analogue of the
Dedekind sum, the Carlitz polynomial

c(u, v; a, b) :=
 b−1∑

k=1 u⌊ ka
b ⌋vk−1.

Here u and v are indeterminates, and a and b are positive integers.

(a) Continuing Exercise 3.7, express the integer-point transforms of the ratio-
nal cones
 K1 = {λ1(0, 1) + λ2(a, b) : λ1, λ2 ≥ 0}

K2 = {λ1(1, 0) + λ2(a, b) : λ1 > 0, λ2 ≥ 0}

in terms of Carlitz polynomials. Here a and b are relatively prime positive
integers.
(b) Verify that R2
≥0 is the disjoint union of K1 and K2, and use this fact to
prove the Carlitz reciprocity law

(v − 1) c(u, v; a, b) + (u − 1) c(v, u; b, a) = u
a−1vb−1 − 1 .

(c) Apply the operators u ∂u twice and v ∂v once to Carlitz’s reciprocity law
to deduce (once more) Corollary 8.5.

Open Problems

8.21. Find new relations between various Dedekind sums.

8.22. It is known [32] that the Fourier–Dedekind sums are eﬃciently com-
putable. Find a fast algorithm that can be implemented in practice.

8.23. For a ﬁxed integer modulus c, ﬁnd all integer solutions a, b ∈ Z to
s(a, c) = s(b, c). (See Exercise 8.4 for the case that c is prime.)

Open Problems 165

8.24. What is {s(a, b) : a, b ∈ Z, b > 0} ,

the set of all rational numbers that occur as Dedekind sums? (It is known
that this set is dense in R [17, 137] and that every rational number between
0 and 1 occurs as the fractional part of a Dedekind sum [121]. On the other
hand, we know that 12 s(a, b) is never an integer unless s(a, b) = 0 [130].)

Chapter 9
Zonotopes

“And what is the use of a book,” thought Alice, “without pictures or conversations?”

Lewis Carroll (Alice in Wonderland)

We have seen that the discrete volume of a general integral polytope may be
quite diﬃcult to compute. It is therefore useful to have an inﬁnite class of
integral polytopes whose discrete volume is more tractable, and yet they are
robust enough to be “closer” in complexity to generic integral polytopes. One
initial class of more tractable polytopes is that of parallelepipeds, and as we
will see in Lemma 9.2, the Ehrhart polynomial of a d-dimensional half-open
integer parallelepiped P is equal to vol(P) td. In this chapter, we generalize
parallelepipeds to projections of cubes.

9.1 Deﬁnitions and Examples

In order to extend the notion of a parallelepiped, we begin by deﬁning the
Minkowski sum of the polytopes P1, P2, . . . , Pn ⊂ Rd as

P1 + P2 + · · · + Pn := {x1 + x2 + · · · + xn : xj ∈ Pj} .

For example, if P1 is the rectangle [0, 2] × [0, 1] ⊂ R2 and P2 is the line
segment [(0
0
), (2
3
)] ⊂ R2, then their Minkowski sum P1 + P2 is the hexagon
whose vertices are (0
0
), (2
0
), (0
1
), (4
3
), (2
4
), and (4
4
), as depicted in Figure 9.1.
Parallelepipeds are special instances of Minkowski sums, namely those of line
segments whose direction vectors are linearly independent, plus a point.
We will also make use of the following handy construct: given a polynomial
p(z1, z2, . . . , zd) in d variables, the Newton polytope N (p(z1, z2, . . . , zd))
of p(z1, z2, . . . , zd) is the convex hull of all exponent vectors appearing in the

167

168 9 Zonotopes

+ =

Fig. 9.1 The Minkowski sum ([0, 2] × [0, 1]) + [(
0
0)
, (
2
3)].

nonzero terms of p(z1, z2, . . . , zd). For example, the hexagon in Figure 9.1 can
be written as
 N (1 + 3z2
1 − z2 − 5z4
1z3
2 + 34z2
1z4
2 + z4
1z4
2) .

It turns out (Exercise 9.1) that the constructions of Newton polytopes
and Minkowski sums are intimately related. Namely, if p(z1, z2, . . . , zd) and
q(z1, z2, . . . , zd) are polynomials, then

N (p(z1, z2, . . . , zd) q(z1, z2, . . . , zd)
)

= N (p(z1, z2, . . . , zd)
) + N (q(z1, z2, . . . , zd)
) . (9.1)

Suppose that we are now given n line segments in Rd, such that each line
segment has one endpoint at the origin and the other endpoint is located at
the vector uj ∈ Rd, for j = 1, . . . , n. Then by deﬁnition, the Minkowski sum
of these n segments is

Z(u1, u2, . . . , un) := {x1 + x2 + · · · + xn : xj = λjuj with λj ∈ [0, 1]} .

Fig. 9.2 The zono-
tope Z ((
0
4)
, (
3
3
), (
4
1))
—a
hexagon.

Let’s rewrite the deﬁnition above in matrix form:

9.1 Deﬁnitions and Examples 169

Z(u1, u2, . . . , un) = {λ1u1 + λ2u2 + · · · + λnun : 0 ≤ λj ≤ 1}

=
 



(u1 u2 · · · un)
 





 λ1
λ2
...
λn
 




 : 0 ≤ λj ≤ 1





= A [0, 1]n,

where A is the (d×n) matrix whose jth column is uj. Just a bit more generally,
a zonotope is deﬁned to be any translate of A [0, 1]n, i.e.,

A [0, 1]n + b ,

for some vector b ∈ Rd. So we now have two equivalent deﬁnitions of a
zonotope—the ﬁrst is as a Minkowski sum of line segments, while the second
is as a projection of the unit cube [0, 1]n. Figures 9.2–9.4 show example
zonotopes.

Fig. 9.3 The rhombic do-
decahedron is a zonotope.

It is sometimes useful to translate a zonotope so that the origin becomes
its new center of mass. To this end, we now dilate the matrix A by a factor
of 2 and translate the resulting image so that its new center of mass is at the
origin. Precisely,

2 A [0, 1]
n − (u1 + · · · + un)

= {2u1λ1 + · · · + 2unλn − (u1 + · · · + un) : 0 ≤ λj ≤ 1}

= {u1(2λ1 − 1) + · · · + un(2λn − 1) : 0 ≤ λj ≤ 1}

= A [−1, 1]n, (9.2)

where the last step holds because −1 ≤ 2λj − 1 ≤ 1 when 0 ≤ λj ≤ 1. In
other words, (9.2) is a linear image of the larger cube [−1, 1]n, centered at
the origin. We thus deﬁne

170 9 Zonotopes

Z(±u1, ±u2, . . . , ±un) := A [−1, 1]n,

and we see that Z(±u1, ±u2, . . . , ±un) is indeed a zonotope, by deﬁnition.
We say that a polytope P is symmetric about the origin when it has the
property that x ∈ P if and only if −x ∈ P. In general, a polytope P is called
centrally symmetric if we can translate P by some vector b such that P +b
is symmetric about the origin. The zonotope Z(±u1, ±u2, . . . , ±un) is an
example of a polytope that is symmetric about the origin. We go through the
full argument here, because it justiﬁes our choice of a symmetric representation:
Choose x ∈ Z(±u1, ±u2, . . . , ±un), so that x = A y, with y ∈ [−1, 1]
n. Since
−y ∈ [−1, 1]n as well,

−x = A (−y) ∈ Z(±u1, ±u2, . . . , ±un) .

It is, moreover, true that each face of a zonotope is again a zonotope and that
therefore, every face of a zonotope is centrally symmetric (Exercise 9.2).

Fig. 9.4 A few more zonotopes.

9.2 Paving a Zonotope

Next we will show that every zonotope can be neatly decomposed into a disjoint
union of half-open parallelepipeds. Suppose that w1, w2, . . . , wm ∈ Rd are
linearly independent, and let σ1, σ2, . . . , σm ∈ {±1}. Then we deﬁne

Πσ1,σ2,...,σm
w1,w2,...,wm := {λ1w1 + λ2w2 + · · · + λmwm : 0 ≤ λj < 1 if σj = −1
0 < λj ≤ 1 if σj = 1
 } .

In plain English, Πσ1,σ2,...,σm
w1,w2,...,wm is a half-open parallelepiped generated by
w1, w2, . . . , wm, and the signs σ1, σ2, . . . , σm keep track of those facets of
the parallelepiped that are included or excluded from the closure of the
parallelepiped.

9.2 Paving a Zonotope 171

Lemma 9.1. The zonotope Z(u1, u2, . . . un) can be written as a disjoint union
of translates of Π
σ1,σ2,...,σm
w1,w2,...,wm , where {w1, w2, . . . , wm} ranges over all linearly
independent subsets of {u1, u2, . . . un}, each equipped with an appropriate
choice of signs σ1, σ2, . . . , σm.

Figure 9.5 illustrates the decomposition of a zonotope as suggested by
Lemma 9.1.

Fig. 9.5 A zonotopal decomposition of Z ((
0
4)
, (
3
3)
, (
4
1))
.

Proof of Lemma 9.1. We proceed by induction on n. If n = 1, Z(u1) is a line
segment and 0 ∪ (0, u1] is a desired decomposition.
For general n > 1, we have by induction the decomposition

Z(u1, u2, . . . , un−1) = Π1 ∪ Π2 ∪ · · · ∪ Πk

into half-open parallelepipeds of the form given in the statement of Lemma 9.1.
Now we deﬁne the hyperplane H := {x ∈ Rd : x · un = 0} and let π : Rd → H
denote the orthogonal projection onto H. Then π(u1), π(u2), . . . , π(un−1) are
line segments or points, and thus Z(π(u1), π(u2), . . . , π(un−1)) is a zonotope
living in H. Once more by induction, we can decompose

Z(π(u1), π(u2), . . . , π(un−1)) = Φ1 ∪ Φ2 ∪ · · · ∪ Φm

into half-open parallelepipeds of the form given in Lemma 9.1. Each Φj is a
half-open parallelepiped generated by some of the vectors π(u1), π(u2), . . . ,
π(un−1); let ̃Φj denote the corresponding parallelepiped generated by their
unprojected counterparts. Then (Exercise 9.5) the desired disjoint union of
Z(u1, u2, . . . , un) is given by Π1 ∪ Π2 ∪ · · · ∪ Πk ∪ P1 ∪ P2 ∪ · · · ∪ Pm, where

172 9 Zonotopes

Pj := ̃Φj + (0, un] . ⊓⊔

This decomposition lemma is useful, e.g., to compute the Ehrhart polyno-
mial of a zonotope. To this end, we now ﬁrst work out the Ehrhart polynomial
of a half-open parallelepiped, which is itself a (particularly simple) zonotope.

Lemma 9.2. Suppose w1, w2, . . . , wd ∈ Z
d are linearly independent, and let

Π := {λ1w1 + λ2w2 + · · · + λdwd : 0 ≤ λ1, λ2, . . . , λd < 1} .

Then # (Π ∩ Z
d) = vol Π = |det (w1, . . . , wd)| ,

and for every positive integer t,

# (t Π ∩ Z
d) = (vol Π) t
d.

In other words, for the half-open parallelepiped Π, the discrete volume
# (t Π ∩ Z
d) coincides with the continuous volume (vol Π) td.

Proof. Because Π is half open, we can tile the tth dilate t Π by td translates
of Π, and hence
 LΠ(t) = # (t Π ∩ Z
d) = # (Π ∩ Z
d) td.

On the other hand, by the results of Chapter 3, LΠ(t) is a polynomial with
leading coeﬃcient vol Π = |det (w1, . . . , wd)|. Since we have equality of these
polynomials for all positive integers t, it follows that

# (Π ∩ Z
d) = vol Π . ⊓⊔

Our proof shows that Lemma 9.2 remains true if we switch the ≤ and <
inequalities for some of the λj in the deﬁnition of Π, a fact that we will use
freely, e.g., in the following tool to compute Ehrhart polynomials of zonotopes,
which follows from a combination of Lemmas 9.1 and 9.2.

Corollary 9.3. Decompose the zonotope Z ⊂ Rd into half-open parallelepipeds
according to Lemma 9.1. Then the coeﬃcient ck of the Ehrhart polynomial
LZ (t) = cd td + cd−1 td−1 + · · · + c0 equals the sum of the (relative) volumes
of the k-dimensional parallelepipeds in the decomposition of Z.

9.3 The Permutahedron

To illustrate that Corollary 9.3 is useful for computations, we now study a
famous polytope, the permutahedron

Pd := conv {(π(1) − 1, π(2) − 1, . . . , π(d) − 1) : π ∈ Sd} ,

9.3 The Permutahedron 173

that is, the convex hull of (0, 1, . . . , d−1) and all points formed by permuting its
entries. It is not hard to show (see Exercise 9.9) that Pd is (d − 1)-dimensional
and has d! vertices. Figures 9.6 and 9.7 show P3 and P4 (the latter projected
into R3).

Fig. 9.6 The permutahe-
dron P3.
 x

y

z

(0 ; 2 ; 1)
 (1 ; 2 ; 0)
 (2 ; 1; 0)

(2 ; 0 ; 1)
(1 ; 0 ; 2)

(0 ; 1; 2)
 The reason that permutahedra make an appearance in this chapter is the
following result.

Theorem 9.4.
 Pd = [e1, e2] + [e1, e3] + · · · + [ed−1, ed] ,

in words: the permutahedron Pd is the Minkowski sum of the line segments
between each pair of unit vectors in Rd.

Proof. We make use of a matrix that already made its debut in Section 3.7:
the permutahedron Pd is the Newton polytope of the polynomial

det
 





 xd−1
1 xd−2
1 · · · x1 1
xd−1
2 xd−2
2 · · · x2 1
... ... ... ...
xd−1
d xd−2
d · · · xd 1
 




 .

One can see the vertices of Pd appearing in the exponent vectors by computing
this determinant by cofactor expansion. Now we use Exercise 3.21:

det
 





 xd−1
1 xd−2
1 · · · x1 1
xd−1
2 xd−2
2 · · · x2 1
... ... ... ...
xd−1
d xd−2
d · · · xd 1
 




 = ∏

1≤j<k≤d (xj − xk) ,

174 9 Zonotopes

(0 ; 1 ; 2 ; 3)
 (1 ; 0 ; 2 ; 3)

(1 ; 0 ; 3 ; 2)

(0 ; 1 ; 3 ; 2)
 (0 ; 2 ; 1 ; 3)
 (2 ; 0 ; 1 ; 3)
 (2 ; 1 ; 0 ; 3)

(1 ; 2 ; 0 ; 3)

(0 ; 2 ; 3 ; 1)

(0 ; 3 ; 2 ; 1)

(0 ; 3 ; 1 ; 2)
 (3 ; 0 ; 1 ; 2)
 (3 ; 1 ; 0 ; 2)
 (1 ; 3 ; 0 ; 2)

(1 ; 3 ; 2 ; 0)
 (1 ; 2 ; 3 ; 0)

(2 ; 0 ; 3 ; 1)

(2 ; 3 ; 0 ; 1)
 (2 ; 3 ; 1 ; 0)
 (2 ; 1 ; 3 ; 0)

(3 ; 2 ; 0 ; 1)

(3 ; 0 ; 2 ; 1)
 (3 ; 2 ; 1 ; 0)

(3 ; 1 ; 2 ; 0)

Fig. 9.7 The permutahedron P4 (projected into R3).

and so by (9.1),

Pd = N (x1 − x2) + N (x1 − x3) + · · · + N (xd−1 − xd) .

The right-hand side is the Minkowski sum of the line segments [e1, e2], [e1, e3],
. . . , [ed−1, ed]. ⊓⊔

Now we will apply Corollary 9.3 to the special zonotope Pd. A forest is a
graph that does not contain any closed paths.

Theorem 9.5. The coeﬃcient ck of the Ehrhart polynomial

LPd (t) = cd−1 t
d−1 + cd−2 td−2 + · · · + c0

of the permutahedron Pd equals the number of labeled forests on d nodes with
k edges.

For example, we can compute LP3(t) = 3t
2 + 3t + 1 by looking at the
labeled forests in Figure 9.8.
An important ingredient to the proof of Theorem 9.5 is the following cor-
respondence: to a subset S ⊆ {e1 + e2, e1 + e3, . . . , ed−1 + ed} we associate
the graph GS with node set [d] and edge set

{jk : ej + ek ∈ S} .

We invite the reader to prove the following lemma (Exercise 9.13):

9.3 The Permutahedron 175

Fig. 9.8 The 3 + 3 + 1
labeled forests on three
nodes.

Lemma 9.6. A subset S ⊆ {e1 − e2, e1 − e3, . . . , ed−1 − ed} is linearly inde-
pendent if and only if GS is a forest.

Proof of Theorem 9.5. The zonotope

Z (e1 − e2, e1 − e3, . . . , ed−1 − ed)

is a lattice translate of Pd (by the vector (d − 1) e1 + (d − 2) e2 + · · · + ek−1)
and, by Lemma 9.1, can be written as disjoint union of lattice translates of
half-open parallelepipeds of the form
∑

ej −ek∈S (0, ej − ek] (9.3)

(written as a Minkowski sum), one for each nonempty linearly independent
subset S of {e1 − e2, e1 − e3, . . . , ed−1 − ed} .

Exercise 9.14 says that (9.3) has relative volume 1. Thus Corollary 9.3 gives
the coeﬃcient ck of the Ehrhart polynomial

LPd (t) = cd−1 t
d−1 + cd−2 td−2 + · · · + c0

as the sum of the relative volumes of the k-dimensional parallelepipeds in our
zonotopal decomposition. As mentioned above, each of these volumes is 1,
and Lemma 9.6 now gives the statement of Theorem 9.5. ⊓⊔

The leading coeﬃcient of the Ehrhart polynomial of Pd is, of course, its
relative volume, about which we can say slightly more. A tree is a connected
forest.

Corollary 9.7. The (relative) volume of the permutahedron Pd equals the
number of labeled trees on d nodes.

176 9 Zonotopes

It turns out (Exercise 9.15) that there are precisely d
d−2 labeled trees on d
nodes, so the relative volume of Pd equals d
d−2.

Proof. By Theorem 9.5, the leading coeﬃcient of Pd equals the number of
labeled forests on d nodes with d − 1 edges. But (as the reader should show
in Exercise 9.16) every such forest is connected. ⊓⊔

9.4 The Ehrhart Polynomial of a Zonotope

Next we will generalize Lemma 9.2 to reﬁne the formula of Corollary 9.3
for Ehrhart polynomials of zonotopes. Lemma 9.2 computed the (continuous
and discrete) volume of a half-open parallelepiped Π spanned by d linearly
independent vectors in Z
d; this volume equals the number of integer points
in Π. We need a version of this lemma in which Π is spanned by n linearly
independent vectors in Z
d where n < d. It turns out that the (continuous and
discrete) volume of Π is still given by the number of integer points in Π, but
this number is not quite as easily computed as in Lemma 9.2.

Lemma 9.8. Suppose w1, w2, . . . , wn ∈ Z
d are linearly independent, let

Π := {λ1w1 + λ2w2 + · · · + λnwn : 0 ≤ λ1, λ2, . . . , λn < 1} ,

and let V be the greatest common divisor of all n × n minors of the matrix
formed by the column vectors w1, w2, . . . , wn. Then the relative volume of Π
equals V . Furthermore, # (Π ∩ Z
d) = V,

and for every positive integer t,

# (t Π ∩ Z
d) = V t
n.

As with Lemma 9.2, the statement of Lemma 9.8 remains true if we switch
the ≤ and < inequalities for some of the λj in the deﬁnition of Π.

Proof. We will make use of the Smith normal form of an integer matrix (or
more generally, a matrix with entries in an integral domain): more precisely,
one proves in linear algebra that for every full-rank matrix A ∈ Z
m×n, say
for which m ≥ n, there exist invertible matrices S ∈ Z
m×m and T ∈ Z
n×n

such that

9.4 The Ehrhart Polynomial of a Zonotope 177

S A T =
 















d1 0 · · · 0
0 d2
... . . . ...
dn−1 0
0 · · · 0 dn
0 · · · 0
... ...
0 · · · 0
 















with diagonal integer entries whose product d1d2 · · · dn equals the greatest
common divisor of all n × n minors of A.
Geometrically, our matrices S and T transform Π into the half-open
rectangular parallelepiped

̃Π := [0, d1) × [0, d2) × · · · × [0, dn) ⊂ Rd

in such a way that the integer lattice Z
d is preserved; in particular, the relative
volumes of Π and ̃Π are equal, namely d1d2 · · · dn = V . Furthermore,

# (Π ∩ Z
d) = # (̃Π ∩ Z
d) = d1d2 · · · dn = V.

The remainder of our proof follows that of Lemma 9.2: since Π is half open,
we can tile the t
th dilate t Π by tn translates of Π, and so

# (t Π ∩ Z
d) = # (Π ∩ Z
d) tn. ⊓⊔

Lemma 9.8 is the crucial ingredient for the following reﬁnement of Corol-
lary 9.3.

Theorem 9.9. Let Z := Z(u1, . . . , un) be a zonotope generated by the integer
vectors u1, . . . , un. Then the Ehrhart polynomial of Z is given by

LZ (t) = ∑

S m(S) t
|S|,

where S ranges over all linearly independent subsets of {u1, . . . , un}, and
m(S) is the greatest common divisor of all minors of size |S| of the matrix
whose columns are the elements of S.

For example, returning to the zonotope Z ((0
4
), (3
3), (4
1
)) featured in Fig-
ure 9.5, we compute

LZ((
0
4),(
3
3),(
4
1))(t) = ∣
∣
∣
∣det (0 3
4 3
)∣
∣
∣
∣ t2 + ∣
∣
∣
∣det (0 4
4 1

)∣
∣
∣
∣ t2 + ∣
∣
∣
∣det (3 4
3 1

)∣
∣
∣
∣ t2

+ gcd(0, 4) t + gcd(3, 3) t + gcd(4, 1) t + 1

= 37 t2 + 8 t + 1 .

178 9 Zonotopes

We remark that the numbers m(S) appearing in Theorem 9.9 have ge-
ometric meaning: if V (S) and L(S) denote respectively the vector space
and lattice generated by S, then m(S) equals the cardinality of the group(V (S) ∩ Z
d) /L(S).

Proof of Theorem 9.9. Decompose Z as described in Lemma 9.1. Corollary 9.3
says that the coeﬃcient ck of the Ehrhart polynomial

LZ (t) = cd td + cd−1 td−1 + · · · + c0

equals the sum of the relative volumes of the k-dimensional parallelepipeds
in this decomposition. Lemma 9.8 implies that these relative volumes are
the greatest common divisors of the minors of the matrices formed by the
generators of these parallelepipeds. ⊓⊔

Notes

1. The word zonotope appears to have originated from the fact that for each
line segment uj that comes into the Minkowski-sum deﬁnition of a zonotope
Z, there corresponds a “zone,” composed of all of the facets of Z that contain
parallel translates of uj. This zone separates the zonotope into two isometric
pieces, a “northern” hemisphere and a “southern” hemisphere, a property
that is sometimes useful in their study.

2. The combinatorial study of zonotopes, starting with Lemma 9.1, was
brought to the forefront (if not initiated) by Peter McMullen and Geoﬀrey
Shephard [171, 174, 220].

3. The permutahedron seems to have been ﬁrst studied by Pieter Hendrik
Schoute [213] in 1911. It tends to play a central role whenever one tries to
“geometrize” a situation involving the symmetric group. The permutahedron
is a simple zonotope and as such quite a rare animal. It is not clear from the
literature who ﬁrst discovered Theorem 9.5, but we suspect it was Richard
Stanley [231, Exercises 4.63 and 4.64]. There has been a recent ﬂurry of research
activity on generalized permutahedra (initiated by Alexander Postnikov [197]),
which share many of the fascinating geometric and arithmetic properties of
permutahedra.

4. Corollary 9.3 and Theorem 9.9 are due to Stanley [229] (see also [227,
Example 3.1] and [231, Exercise 4.31]), and we follow his proof closely in this
chapter. The formula for the leading coeﬃcient of the Ehrhart polynomial in
Theorem 9.9, i.e., the volume of the zonotope, goes back to Shephard [220,
equation (57)].

Exercises 179

5. Zonotopes have played a central role in the recently established theory
of arithmetic matroids and arithmetic Tutte polynomials, and Corollary 9.3
was restated in this language by Michele D’Adderio and Luca Moci [90,
Theorem 3.2]. Ehrhart polynomials of zonotopes and their arithmetic Tutte
siblings are in general harder to compute than what this chapter might convey;
some examples for computable formulas (for arithmetic Tutte polynomials for
the classical root systems) were given by Federico Ardila, Federico Castillo,
and Michael Henley [10].

Exercises

9.1. ♣ Prove (9.1): if p(z1, z2, . . . , zd) and q(z1, z2, . . . , zd) are polynomials,
then
 N (p(z1, z2, . . . , zd) q(z1, z2, . . . , zd)
)

= N (p(z1, z2, . . . , zd)
) + N (q(z1, z2, . . . , zd)
) .

9.2. Prove that every face of a zonotope is a zonotope, and conclude that
every face of a zonotope is centrally symmetric.

9.3. Let P be a d-dimensional integral parallelepiped in Rn. Prove that if
there exists only one integer point x in the interior of P, then x must be the
center of mass of P.

9.4. Let P be a d-dimensional integral parallelepiped in Rn. Prove that the
convex hull of all the integer points in the interior of P is a centrally symmetric
polytope.

9.5. ♣ Complete the proof of Lemma 9.1 by showing (using the notation from
the proof) that Z(u1, u2, . . . , un) equals the disjoint union of Π1, Π2, . . . , Πk
and P1, P2, . . . , Pm.

9.6. (a) Show that for all real vectors u1, . . . , un, w ∈ Rd,

Z(u1, . . . , un, −w) = Z(u1, . . . , un, w) − w,

where the latter diﬀerence is deﬁned as a translation of the zonotope
Z(u1, . . . , un, w) by the vector −w.
(b) Show that given a zonotope Z, we may always choose all of the generators
of a translate of Z in some half-space containing the origin on its boundary.

9.7. Prove that the following statements are equivalent for a polytope P:

(a) P is a zonotope;
(b) every 2-dimensional face of P is a zonotope;
(c) every 2-dimensional face of P is centrally symmetric.

180 9 Zonotopes

9.8. Given a zonotope Z(±u1, ±u2, . . . , ±un) ⊂ Rd, consider the hyperplane
arrangement H consisting of the n hyperplanes in Rd through the origin with
normal vectors u1, u2, . . . , un. Show that there is a one-to-one correspondence
between the vertices of Z(±u1, ±u2, . . . , ±un) and the regions of H (i.e., the
maximal connected components of Rd \ ⋃ H). Can you give an analogous
correspondence for the other faces of Z(±u1, ±u2, . . . , ±un)?

9.9. ♣ Show that the dimension of the permutahedron

Pd = conv {(π(1) − 1, π(2) − 1, . . . , π(d) − 1) : π ∈ Sd}

is d − 1 and that Pd has d! vertices.

9.10. Show that the permutahedron Pd is the image of the Birkhoﬀ–von
Neumann polytope Bd from Chapter 6 under a suitable linear map.

9.11. Give a hyperplane description of the permutahedron Pd.

9.12. According to Exercise 9.9, the permutahedron Pd lies in a hyperplane
H ⊂ Rd. Show that Pd tiles H. (Hint: begin by drawing the case d = 3. For
the general case, the viewpoint of Exercise 9.8 might be useful.)

9.13. Prove Lemma 9.6: A subset S ⊆ {e1 − e2, e1 − e3, . . . , ed−1 − ed} is
linearly independent if and only if GS is a forest.

9.14. Let S be a linearly independent subset of

{e1 − e2, e1 − e3, . . . , ed−1 − ed} .

Show that the half-open parallelepiped
∑

ej −ek∈S (0, ej − ek]

(written as a Minkowski sum) has relative volume 1.

9.15. Prove that there are precisely dd−2 labeled trees on d nodes.

9.16. Show that every forest on d nodes with d − 1 edges is connected, i.e., it
is a tree.

9.17. Given a graph G with node set [d], we deﬁne the graphical zonotope
ZG as the Minkowski sum of the line segments [ej, ek] for all edges jk of G.
(Thus the permutahedron Pd is the graphical zonotope of the complete graph
on d nodes.) Prove that the volume of ZG equals the number of spanning
trees of G. Give an interpretation of the Ehrhart coeﬃcients of ZG, in analogy
with Theorem 9.5.
1

1 An intimately related polytope, which is in fact older than the graphical zonotope associ-
ated with G, is the acyclotope, the convex hull of net degree vectors of acyclic orientations
of G. For example, the acyclotope of the complete graph on d nodes is the shifted permuta-
hedron conv {(π(1), π(2), . . . , π(d)) : π ∈ Sd}. It turns out that the acyclotope associated
with G is the Minkowski sum of the line segments [ej − ek, ek − ej ] for all edges jk of G.

Open Problems 181

9.18. Let G be a graph with node set [d], and let deg(j) denote the number
of edges incident to j (the degree of the node j). The vector

deg(G) := (deg(1), deg(2), . . . , deg(d))

is the labeled degree sequence of G. Let Zd be the zonotope generated by
the vectors ej + ek for 1 ≤ j < k ≤ d.

(a) Show that every labeled degree sequence of a graph with d nodes is an
integer point in Zd.
(b) If you know the Erd˝os–Gallai theorem (and if you don’t, look it up), prove
that every integer point in Zd whose coordinate sum is even is a labeled
degree sequence of a graph with d nodes.

9.19. Let K be a compact, convex set in Rd, symmetric about the origin,
whose volume is greater than 2
d. Prove that K must contain a nonzero integer
point. (This result is known as Minkowski’s fundamental theorem, and it lies
at the core of the geometry of numbers, as well as algebraic number theory.
Its applications have shown how interesting and useful symmetric bodies can
be.)

Open Problems

9.20. Classify the polynomials in Z[t] that are Ehrhart polynomials of integral
zonotopes. (This is hard: if the matrix deﬁning a zonotope is unimodular,
then its Ehrhart coeﬃcients are the entries of the f -vector of the underlying
matroid—see Note 5; the classiﬁcation of f -vectors of matroids is an old and
diﬃcult problem.)

9.21. The unlabeled degree sequence (often simply called degree se-
quence) of a graph G is the vector deg(G) (deﬁned in Exercise 9.18) rede-
ﬁned such that its entries are in decreasing order. How many distinct degree
sequences are there for graphs on n nodes? (For known values for the ﬁrst
few n, see [1, Sequence A004251]. The analogous question for labeled degree
sequences was answered in [229]; that proof begins with Exercise 9.18.)

9.22. Let K ⊂ Rd be a d-dimensional convex body with the origin as its
barycenter. If K contains only the origin as an interior lattice point, then
vol(K) ≤ (d+1)d
d! , where equality holds if and only if K is unimodularly
equivalent to (d + 1)∆, where ∆ is the d-dimensional standard simplex from
Section 2.3. (This is a conjecture of Ehrhart from 1964. Ehrhart himself
proved this upper bound for all d-dimensional simplices, and also completely in
dimension 2, but it remains open in general. The interested reader may consult
[186] about the current state of Ehrhart’s conjecture and its relationship to
the Ricci curvature of Fano manifolds.)

Chapter 10
h-Polynomials and h
∗-Polynomials

Life is the twofold internal movement of composition and decomposition at once general
and continuous.

Henri de Blainville (1777–1850)

In Chapters 2 and 3, we developed the Ehrhart polynomial and Ehrhart
series of an integral polytope P and realized that the arithmetic information
encoded in an Ehrhart polynomial is equivalent to the information encoded
in its Ehrhart series. More precisely, when the Ehrhart series is written as a
rational function, we introduced the name h
∗-polynomial for its numerator:

EhrP (z) = 1 + ∑

t≥1 LP (t) zt = h
∗
P (z)
(1 − z)dim(P)+1 .

Our goal in this chapter is to prove several decomposition formulas for h
∗
P (z)
based on triangulations of P. As we will see, these decompositions will involve
both arithmetic data from the simplices of the triangulation and combinatorial
data from the face structure of the triangulation.

10.1 Simplicial Polytopes and (Unimodular)
Triangulations

In Chapter 5—more precisely, in Theorem 5.1—we derived relations among
the face numbers fk of a simple polytope. The twin sisters of these Dehn–
Sommerville relations for simplicial polytopes—all of whose nontrivial faces
are simplices—were the subject of Exercise 5.9. It turns out they can be stated
in a compact way by introducing the h-polynomial of the d-polytope P:

183

184 10 h-Polynomials and h∗-Polynomials

hP (z) :=
 d−1∑

k=−1 fk zk+1 (1 − z)d−1−k ,

where we set f−1 := 1. The following is a nifty restatement of Exercise 5.9, as
the reader should check (Exercise 10.1).

Theorem 10.1 (Dehn–Sommerville relations). If P is a simplicial d-
polytope, then hP is a palindromic polynomial.

We need this simplicial version of the Dehn–Sommerville relations because
it naturally connects to triangulations. The h-polynomial of P encodes combi-
natorial information about the faces in the boundary of P, and so the natural
setting in the world of triangulations will consist of a triangulation of the
boundary of a polytope. By analogy with the face numbers of a polytope,
given a triangulation T of the boundary ∂P of a given d-dimensional polytope
P, we deﬁne fk to be the number of k-simplices in T ; they will be encoded,
as above, in the h-polynomial

hT (z) :=
 d−1∑

k=−1 fk zk+1 (1 − z)
d−1−k ,

where again we set f−1 := 1. The typical scenario we will encounter is that we
are given a triangulation T of the polytope P and then consider the induced
triangulation {∆ ∈ T : ∆ ⊂ ∂P}

of the boundary of P.

Theorem 10.2 (Dehn–Sommerville relations for boundary triangu-
lations). Given a regular triangulation of the polytope P, the h-polynomial
of the induced triangulation of ∂P is palindromic.

Proof. Given a regular triangulation T of P ⊆ Rd, let Q ⊆ Rd+1 be the
corresponding lifted polytope as in (3.1). Choose a point v ∈ P ◦ and lift it
to (v, h + 2) ∈ Rd+1, where h is the maximal height among the vertices of Q.
Let R be the convex hull of (v, h + 2) and the vertices of the lower hull of Q,
and let S := R ∩ {x ∈ Rd+1 : xd+1 = h + 1} .

Figure 10.1 shows an instance of this setup. (The polytope S is a vertex
ﬁgure of Q at v.) Exercise 10.2 says that S is a simplicial polytope whose
face numbers fk equal the face numbers of the triangulation of ∂P induced
by T . Thus the h-polynomial of this triangulation of ∂P equals hS (z), which
is palindromic by Theorem 10.1. ⊓⊔

When we are given a triangulation T of a polytope (rather than of its
boundary), we adjust our deﬁnition of the accompanying h-polynomial to

10.1 Simplicial Polytopes and (Unimodular) Triangulations 185

S
 Fig. 10.1 The geometry of our proof of Theorem 10.2.

hT (z) :=
 d∑

k=−1 fk zk+1 (1 − z)
d−k .

In general, there is no analogue of Theorem 10.2 for this h-polynomial, though
an (important) exception is given in Exercise 10.3.
There is a second reason for us to introduce the h-polynomial of a triangu-
lation. We call a triangulation T unimodular if each simplex

∆ = conv{v0, v1, . . . , vk} ∈ T

has the property that the vectors v1 − v0, v2 − v0, . . . , vk − v0 form a lattice
basis of span(∆) ∩ Z
d. In this case, we also call the simplex ∆ unimodu-
lar. One example of a unimodular simplex is the standard k-simplex ∆ of
Section 2.3. We recall that in this case,

Ehr∆(z) = 1
(1 − z)k+1 , (10.1)

and we invite the reader to prove that the same Ehrhart series comes with
every unimodular k-simplex (Exercise 10.4).
Here is the main result of this section.

Theorem 10.3. If P is an integral d-polytope that admits a unimodular
triangulation T , then

186 10 h-Polynomials and h∗-Polynomials

EhrP (z) = hT (z)
(1 − z)d+1 .

In words, the h
∗-polynomial of P is given by the h-polynomial of the triangu-
lation T .
 [[=
 Fig. 10.2 A triangulation of a hexagon and the corresponding decomposition (10.2).

Proof. We begin by writing P as the union of all open simplices in T , pictured
in an example in Figure 10.2:
 P = ⋃

∆∈T ∆◦ (10.2)

(here we are using Exercise 5.3). Since this union is disjoint, we can compute

EhrP (z) = 1 + ∑

∆∈T Ehr∆◦ (z) = 1 + ∑

∆∈T
 ( z
1 − z
 )dim ∆+1 .

Here the last equality follows from the Ehrhart–Macdonald reciprocity theorem
(Theorem 4.4) applied to the Ehrhart series (10.1) of a unimodular simplex.
Since the above summands depend only on the dimension of each simplex, we
can rewrite

EhrP (z) = 1 +
 d∑

k=0 fk
 ( z
1 − z
 )k+1 =
 d∑

k=−1 fk
 ( z
1 − z
 )k+1

=
 ∑d
k=−1 fk zk+1(1 − z)
d−k

(1 − z)d+1 = hT (z)
(1 − z)d+1 . ⊓⊔

Theorem 10.3 says something remarkable: the arithmetic of a polytope
(its discrete volume) is completely determined by the combinatorics of the
unimodular triangulation (its face structure). Unfortunately, not all integral
polytopes admit unimodular triangulations—in fact, most do not (see Exer-
cise 10.5). Our next goal is to ﬁnd an analogue of Theorem 10.3 that holds
for every integral polytope.

10.2 Fundamental Parallelepipeds Open Up, with an h-Twist 187

10.2 Fundamental Parallelepipeds Open Up, with an
h-Twist

Our philosophy in constructing a generalization of Theorem 10.3 rests in
revisiting the cone over a given polytope from Chapter 3, using a decomposition
of P into open simplices.
Given an integral d-polytope P, ﬁx a (not necessarily unimodular) trian-
gulation T . As in (10.2), we can write P as the disjoint union of the open
simplices in T ; from this point of view, the following deﬁnition should look
natural. Given a simplex ∆ ∈ T , let Π(∆) be the fundamental parallelepiped
of cone(∆) (as deﬁned in Section 3.3), and let

B∆(z) := σΠ(∆)◦ (1, 1, . . . , 1, z) .

Thus B∆(z) is an “open” variant of h
∗
∆(z) = σΠ(∆)(1, 1, . . . , 1, z), an equation
we used several times in Chapters 3 and 4.
Looking back at our proof of Theorem 10.3, it makes moral sense to include
∅ in the collection of faces of a triangulation of a given polytope, with
the convention dim(∅) := −1. (This explains in hindsight our convention
f−1 := 1.) We will assume for the rest of this chapter that every triangulation
T includes the “empty simplex” ∅. Along the same lines, we deﬁne B∅(z) := 1.
We need one more concept to be able to state our generalization of Theo-
rem 10.3. Given a simplex ∆ ∈ T , let

linkT (∆) := {Ω ∈ T : Ω ∩ ∆ = ∅, Ω ⊆ Φ for some Φ ∈ T with ∆ ⊆ Φ} ,

the link of ∆. In words, every simplex in linkT (∆) is disjoint from ∆, yet it
is the face of a simplex in T that also contains ∆ as a face; see Figure 10.3
for two examples. When the triangulation T is clear from the context, we

v

link( v )

l
 link( l )
 Fig. 10.3 The links of a vertex and an edge in a triangulation of the 3-cube.

suppress the subscript and simply write link(∆). We remark that by deﬁnition,
link(∅) = T . In general, link(∆) consists of a collection of simplices in T , the
largest dimension of which is d − dim(∆) − 1 (Exercise 10.8), and so it is

188 10 h-Polynomials and h∗-Polynomials

reasonable to deﬁne

hlink(∆)(z) :=
 d−dim(∆)−1∑

k=−1 fk zk+1 (1 − z)
d−dim(∆)−1−k ,

where fk denotes the number of k-simplices in link(∆). The h-polynomial
of link(∆) encodes combinatorial data coming from the simplices in T that
contain ∆. This statement can be made more precise, as we invite the reader
to prove in Exercise 10.9:

hlink(∆)(z) = (1 − z)
d−dim(∆) ∑

Φ⊇∆
 ( z
1 − z
 )dim(Φ)−dim(∆) , (10.3)

where the sum is over all simplices Φ ∈ T containing ∆.

Theorem 10.4 (Betke–McMullen decomposition of h
∗). Fix a trian-
gulation T of the integer d-polytope P. Then

EhrP (z) = ∑

∆∈T hlink(∆)(z) B∆(z)
(1 − z)d+1 .

Before proving Theorem 10.4, we explain its relation to Theorem 10.3.
If a simplex ∆ ∈ T is unimodular, then the corresponding fundamental
parallelepiped Π(∆) of cone(∆) contains the origin as its sole integer lattice
point, and thus B∆(z) = 0, unless ∆ = ∅. Thus if the triangulation T is
unimodular, then the sum giving the h
∗-polynomial in Theorem 10.4 collapses
to hlink(∅)(z) B∅(z) = hT (z), and so Theorem 10.3 follows as a special case
of Theorem 10.4.

Proof of Theorem 10.4. We begin, as in our proof of Theorem 10.3, by writing
P as the disjoint union of all open nonempty simplices in T as in (10.2), and
thus, using Ehrhart–Macdonald reciprocity (Theorem 4.4),

EhrP (z) = 1 + ∑

∆∈T \{∅} Ehr∆◦ (z) = 1 + ∑

∆∈T \{∅}(−1)dim(∆)+1 h
∗
∆ ( 1
z )

(1 − 1
z )dim ∆+1

= 1 +
 ∑

∆∈T \{∅} zdim(∆)+1(1 − z)
d−dim(∆)h
∗
∆( 1
z )

(1 − z)d+1 . (10.4)

Here h
∗
∆(z) denotes the h
∗-polynomial of the simplex ∆. Now we use Exer-
cise 10.10: σΠ(∆)(z) = 1 + ∑

Ω⊆∆
Ω̸=∅
 σΠ(Ω)◦ (z) ,

where the sum is over all nonempty faces of ∆. This identity specializes, if we
choose z = (1, 1, . . . , 1, z), to

10.3 Palindromic Decompositions of h∗-Polynomials 189

h
∗
∆(z) = ∑

Ω⊆∆ BΩ(z) ,

where now the sum is over all faces of ∆, including ∅ (recall that B∅(z) = 1).
Substituting this back into (10.4) yields

EhrP (z) = 1 +
 ∑

∆∈T \{∅} zdim(∆)+1(1 − z)d−dim(∆) ∑

Ω⊆∆ BΩ( 1
z )

(1 − z)d+1

=
 ∑
∆∈T zdim(∆)+1(1 − z)
d−dim(∆) ∑

Ω⊆∆ BΩ( 1
z )

(1 − z)d+1 . (10.5)

Recall that the polynomial B∆(z) encodes data about the lattice points in
the interior of the fundamental parallelepiped of cone(∆). The symmetry of
this parallelepiped gets translated into the palindromicity of the associated
polynomial (Exercise 10.7):

B∆(z) = zdim(∆)+1B∆ ( 1
z ) . (10.6)

This allows us to rewrite (10.5) further:

h
∗
P (z) = ∑

∆∈T zdim(∆)+1(1 − z)
d−dim(∆) ∑

Ω⊆∆ BΩ
 ( 1
z
 )

= ∑

∆∈T zdim(∆)+1(1 − z)
d−dim(∆) ∑

Ω⊆∆ z− dim(Ω)−1BΩ(z)

= ∑

Ω∈T
 ∑

∆⊇Ω zdim(∆)−dim(Ω)(1 − z)
d−dim(∆)BΩ(z)

= ∑

Ω∈T (1 − z)
d−dim(Ω)BΩ(z) ∑

∆⊇Ω
 ( z
1 − z
 )dim(∆)−dim(Ω) .

Theorem 10.4 follows now with (10.3). ⊓⊔

10.3 Palindromic Decompositions of h
∗-Polynomials

Our next goal is to reﬁne Theorem 10.4 in the case that T comes from a
boundary triangulation of P, for which we can exploit Theorem 10.2, or rather
its analogue for links, which is the subject of Exercise 10.12. To keep our
exposition accessible, we will discuss only the case that P contains an interior
lattice point; the identities in this section and the next have analogues without
this condition, which we will address in the notes at the end of the chapter.

Theorem 10.5. Suppose P is an integral d-polytope that contains an interior
lattice point. Then there exist unique polynomials a(z) and b(z) such that

190 10 h-Polynomials and h∗-Polynomials

h
∗
P (z) = a(z) + z b(z) ,

a(z) = zd a( 1
z ), and b(z) = zd−1 b( 1
z ).

The identities for a(z) and b(z) say that a(z) and b(z) are palindromic
polynomials; the degree of a(z) is necessarily d (because the constant coeﬃcient
of a(z) is h
∗
P (0) = 1), while the degree of b(z) is d − 1 or less. In fact, b(z)
can be the zero polynomial—this happens if and only if P is the translate of
a reﬂexive polytope, by Theorem 4.6.

Proof. After a harmless lattice translation, we may assume that 0 ∈ P ◦. Fix
a regular boundary triangulation T of P and let

T0 := T ∪ {conv(∆, 0) : ∆ ∈ T } .

Thus T0 is a triangulation of P whose simplices come in two ﬂavors: those on
the boundary of P and those of the form conv(∆, 0) for some ∆ ∈ T . (We say
that T0 comes from coning over the boundary triangulation T .) Figure 10.4
shows an example. Perhaps not surprisingly, the two kinds of simplices in T0

T 0 T
 Fig. 10.4 A triangulation T0 and its two types of simplices; the middle picture shows the
boundary triangulation T .

are related: Exercise 10.11 says that for every nonempty simplex ∆ ∈ T ,

hlinkT0 (∆)(z) = hlinkT0 (conv(∆,0))(z) = hlinkT (∆)(z) . (10.7)

Thus Theorem 10.4 gives in this case

h
∗
P (z) = ∑

∆∈T0 hlinkT0 (∆)(z) B∆(z)

= ∑

∆∈T hlinkT (∆)(z) (B∆(z) + Bconv(∆,0)(z)
) .

Now let

10.4 Inequalities for h∗-Polynomials 191

a(z) := ∑

∆∈T hlinkT (∆)(z) B∆(z) (10.8)

b(z) := 1
z
 ∑

∆∈T hlinkT (∆)(z) Bconv(∆,0)(z) . (10.9)

The fact that each Bconv(∆,0)(z) has constant term zero ensures that b(z)
is a polynomial (of degree at most d − 1). Furthermore, by Exercise 10.12
and (10.6),

zd a ( 1
z
 ) = ∑

∆∈T zd−dim(∆)−1hlinkT (∆)
 ( 1
z
 ) zdim(∆)+1B∆
 ( 1
z
 )

= ∑

∆∈T hlinkT (∆)(z) B∆(z) = a(z) ,

and b(z) = zd−1 b( 1
z ) follows analogously. Thus our setup gives rise to the
decomposition h
∗
P (z) = a(z) + z b(z)

with palindromic polynomials a(z) and b(z), and Exercise 10.13 says that
this decomposition is unique. (Note that this means, in particular, that every
boundary triangulation yields the same decomposition.) ⊓⊔

10.4 Inequalities for h
∗-Polynomials

The proof of Theorem 10.5 has a powerful consequence due to the following fact,
whose proof would lead us too far astray (though we outline a self-contained
proof in Exercises 10.16–10.18).

Theorem 10.6. The h-polynomial of a link in a regular triangulation has
nonnegative coeﬃcients.

Looking back how the polynomials a(z) and b(z) were constructed
(see (10.8) and (10.9)), we can thus deduce the following corollary:

Corollary 10.7. The polynomials a(z) and b(z) appearing in Theorem 10.5
have nonnegative coeﬃcients.

Naturally, the fact that the coeﬃcients of a(z) and b(z) have nonnegative
coeﬃcients can be translated into inequalities among the coeﬃcients of the
accompanying h
∗-polynomials: the following corollary of Corollary 10.7 is
easily proved (Exercise 10.14).

Corollary 10.8. Suppose P is an integral d-polytope that contains an interior
lattice point. Then its h
∗-polynomial h
∗
P (x) = h
∗
dx
d + h
∗
d−1xd−1 + · · · + h
∗
0
satisﬁes

192 10 h-Polynomials and h∗-Polynomials

h
∗
0 +h
∗
1 +· · ·+h∗
j+1 ≥ h
∗
d +h
∗
d−1 +· · ·+h
∗
d−j for 0 ≤ j ≤ ⌊ d
2 ⌋−1 (10.10)

and

h
∗
0 + h
∗
1 + · · · + h
∗
j ≤ h
∗
d + h
∗
d−1 + · · · + h
∗
d−j for 0 ≤ j ≤ d. (10.11)

Notes

1. Theorem 10.3 is only one indication of how important (and special) unimod-
ular triangulations are; see [99, Chapter 9] for more. If an integral polytope
P admits a unimodular triangulation, then it is integrally closed: for every
positive integer k and every integer point x ∈ kP, there exist integer points
y1, y2, . . . , yk ∈ P such that y1 + y2 + · · · + yk = x.1 (See Exercise 10.6.)
There are integrally closed polytopes that do not admit a unimodular trian-
gulation. These two notions are part of an interesting hierarchy of integral
polytopes, with connections to commutative algebra and algebraic geometry;
see, e.g., [74].

2. Theorem 10.4 is due to Ulrich Betke and Peter McMullen, as is Theo-
rem 10.5, published in an inﬂuential paper [55] in 1985. Corollary 10.7 should
perhaps have been in [55] (the nonnegativity of the h-polynomials in Betke–
McMullen’s formulas was established in the 1970s), but it appeared only—in
the guise of Corollary 10.8—in the 1990s, in papers by Takayuki Hibi [134] and
Richard Stanley [228]. Neither paper gives the impression that the inequalities
of Corollary 10.8 follow immediately from Betke–McMullen’s work, though
both hold without the condition of the existence of an interior lattice point
(here d has to be replaced by the degree of h
∗
P (z) in (10.11)) and in situations
more general than the realm of Ehrhart series.

3. Theorem 10.5 and Corollary 10.7 are not the end of the story. Building on
work of Sam Payne [189] (which gave a multivariate version of Theorem 10.4),
Alan Stapledon [235] generalized Theorem 10.5 and Corollary 10.7 to arbitrary
integral polytopes. His theorem says that if h
∗
P (z) has degree s (recall from
Chapter 4 that in this case, we say P has degree s), then there exist unique
polynomials a(z) and b(z) with nonnegative coeﬃcients such that
(1 + z + · · · + zd−s) h
∗
P (z) = a(z) + zd+1−s b(z) , (10.12)

1 Integrally closed polytopes are also said to have the integer decomposition prop-
erty. There is a related notion for integral polytopes, namely that of normality. For full-
dimensional polytopes, the terms integrally closed and normal are equivalent, but this is
not the case when the subgroup ∑
x, y∈P∩Zd Z(x − y) of Zd is not a direct summand of
Zd. For more about this subtlety (and much more), see [74, 89].

Exercises 193

a(z) = zd a( 1
z ), b(z) = zs−1 b( 1
z ), and, writing a(z) = adzd + ad−1zd−1 + · · · +
a0, 1 = a0 ≤ a1 ≤ aj for 2 ≤ j ≤ d − 1. (10.13)

These inequalities imply Corollary 10.8 without the condition that P contain
an interior lattice point (again here d has to be replaced by s in (10.11)); see
Exercise 10.15. Stapledon has recently improved this theorem further, giving
inﬁnitely many classes of linear inequalities among the h
∗-coeﬃcients [233].
This exciting new line of research involves additional techniques from additive
number theory. He also introduced a weighted variant of the h
∗-polynomial that
is always palindromic, motivated by motivic integration and the cohomology
of certain toric varieties [234]. One can easily recover h
∗
P (x) from this weighted
h
∗-polynomial, but one can also deduce the palindromicity of both a(x) and
b(x) as coming from the same source (and this perspective has some serious
geometric applications).

Exercises

10.1. ♣ Show that the f -vector and the h-vector of a simplicial d-polytope
are related via

hk =
 k∑

j=0(−1)k−j(d − j
d − k
)fj−1 and fk−1 =
 k∑

j=0
 (d − j
k − j
)
hj ,

and conclude that the Dehn–Sommerville relations in Exercise 5.9 are equiva-
lent to Theorem 10.1.

10.2. ♣ As in the setup of our proof of Theorem 10.2, let Q ⊆ Rd+1 be the
lifted polytope giving rise to a regular triangulation T of the polytope P ⊆ Rd,
choose v ∈ P ◦, and lift it to (v, h + 2) ∈ Rd+1, where h is the maximal height
among the vertices of Q. Let R be the convex hull of (v, h+2) and the vertices
of the lower hull of Q, and let

S := R ∩ {x ∈ Rd+1 : xd+1 = h + 1} .

Prove that S is a simplicial polytope whose face numbers fk equal the face
numbers of the triangulation of ∂P induced by T .

10.3. Given a triangulation T of the boundary of a d-polytope P and a point
v ∈ P ◦, construct a triangulation K of P consisting of T with the simplices
conv(∆, v) for all ∆ ∈ T appended; i.e., the new triangulation K comes from
coning over T . Prove that
 hK(z) = hT (z) .

194 10 h-Polynomials and h∗-Polynomials

10.4. ♣ Show that if ∆ is a unimodular k-simplex, then

Ehr∆(z) = 1
(1 − z)k+1 .

10.5. Show that every integral polygon admits a unimodular triangulation.
Give an example of an integral d-polytope that does not admit a unimodular
triangulation for any d ≥ 3.

10.6. Recall from the notes that an integral polytope P is integrally closed
if for every positive integer k and every integer point x ∈ kP, there exist
integer points y1, y2, . . . , yk ∈ P such that y1 + y2 + · · · + yk = x. Prove that
every integral polytope that admits a unimodular triangulation is integrally
closed.

10.7. ♣ Prove (10.6): B∆(z) = zdim(∆)+1B∆ ( 1
z ) .

10.8. ♣ Let T be a triangulation of the d-polytope P. Given ∆ ∈ T , show
that the largest dimension occurring among the simplices in link(∆) is d −
dim(∆) − 1.

10.9. ♣ Prove (10.3): given a triangulation T of a d-dimensional polytope,
then for every simplex ∆ ∈ T ,

hlink(∆)(z) = (1 − z)
d−dim(∆) ∑

Φ⊇∆
 ( z
1 − z
 )dim(Φ)−dim(∆) ,

where the sum is over all simplices Φ ∈ T that contain ∆.

10.10. ♣ For an integral simplex ∆, let Π(∆) denote the fundamental paral-
lelepiped of cone(∆). Show that

σΠ(∆)(z) = 1 + ∑

Ω⊆∆ σΠ(Ω)◦ (z) ,

where the sum is over all nonempty faces of ∆.

10.11. ♣ Prove (10.7): Fix a regular triangulation T0 of a polytope P with 0 ∈
P ◦ whose vertices are 0 and the vertices of P, and let T := {∆ ∈ T0 : ∆ ⊆ ∂P}.
Then for every nonempty ∆ ∈ T ,

hlink(∆)(z) = hlink(conv(∆,0))(z) .

10.12. ♣ Let ∆ be a simplex in a regular boundary triangulation of a d-
dimensional polytope. Prove that hlink(∆)(z) is palindromic. (Hint: establish
a one-to-one correspondence between link(∆) and the boundary faces of a
polytope of dimension d − dim(∆) − 1, respecting the face relations.)

Exercises 195

10.13. ♣ Let p(z) be a polynomial of degree d. Show that there are unique
polynomials a(z) and b(z) such that

p(z) = a(z) + z b(z) ,

a(z) = zd a( 1
z ), and b(z) = zd−1 b( 1
z ).

10.14. ♣ Consider the polynomial decomposition h
∗
P (z) = a(z) + z b(z) of
an integral d-polytope that contains an interior lattice point, given in The-
orem 10.5. Prove that the fact that a(z) has nonnegative coeﬃcients im-
plies (10.10):

h
∗
0 + h
∗
1 + · · · + h
∗
j+1 ≥ h
∗
d + h
∗
d−1 + · · · + h
∗
d−j for 0 ≤ j ≤ ⌊ d
2 ⌋ − 1,

and the fact that b(z) has nonnegative coeﬃcients implies (10.11):

h
∗
0 + h
∗
1 + · · · + h
∗
j ≤ h
∗
d + h
∗
d−1 + · · · + h
∗
d−j for 0 ≤ j ≤ d.

10.15. Derive the analogue of Corollary 10.8 without the condition that P
contain an interior lattice point, using (10.12) and (10.13).

10.16. A shelling of the d-polyhedron P is a linear ordering of the facets
F1, F2, . . . , Fm of P such that the following recursive conditions hold:

(1) F1 has a shelling.
(2) For every j > 1, (F1 ∪ F2 ∪ · · · ∪ Fj−1) ∩ Fj is of dimension d − 2 and

(F1 ∪ F2 ∪ · · · ∪ Fj−1) ∩ Fj = G1 ∪ G2 ∪ · · · ∪ Gk ,

where G1 ∪ G2 ∪ · · · ∪ Gk ∪ · · · ∪ Gn is a shelling of Fj.
2

Fig. 10.5 Constructing a line shelling of a pentagon.

Given a d-polytope P ⊂ Rd, choose a generic vector v ∈ Rd (e.g., you can
choose a vector at random). If we think of P as a planet and we place a hot-air

2 Note that this condition implies that (F1 ∪ F2 ∪ · · · ∪ Fj−1) ∩ Fj is connected for d ≥ 3.

196 10 h-Polynomials and h∗-Polynomials

balloon on one of the facets of P, we will slowly see more and more facets,
one at a time, as the balloon rises in the direction of v (see Figure 10.5). Here
seeing means the following: we say that a facet F is visible from the point
x /∈ P if the line segment between x and any point y ∈ F intersects P only
in y.
Our balloon ride gives rise (no pun intended) to an ordering F1, F2, . . . , Fm
of the facets of P. Namely, F1 is the facet on which we are beginning our
journey, F2 is the next visible facet, etc., until we are high enough so that
no more visible facets can be added. At this point, we “pass through inﬁnity”
and let the balloon approach the polytope planet from the opposite side. The
next facet in our list is the ﬁrst one that will disappear as we move toward the
polytope, then the next facet that will disappear, etc., until we are landing
back on the polytope. (That is, the second half of our list of facets is the
reversed list of what we would get had we started our ride at Fm.)
Prove that this ordering F1, F2, . . . , Fm of the facets of P is a shelling
(called a line shelling).

10.17. Suppose P is a simplicial d-polytope with facets F1, F2, . . . , Fm, or-
dered by some line shelling. We collect the vertices of Fj in the set Fj. Let
̃Fj be the set of all vertices v ∈ Fj such that Fj \ {v} is contained in one of
F1, F2, . . . , Fj−1 (which deﬁne the facets coming earlier in the shelling order).

(a) Prove that the new faces appearing in the jth step of the construction of
the line shelling, i.e., the faces in Fj \ (F1 ∪ F2 ∪ · · · ∪ Fj−1), are precisely
those sets conv(G) for some ̃Fj ⊆ G ⊆ Fj.
(b) Show that
 fk−1 =
 k∑

m=0
 (d − m
k − m

)
̃hm ,

where ̃hm denotes the number of sets ̃Fj of cardinality m.
(c) Conclude that ̃hm = hm and thus that hm ≥ 0.

10.18. Given a regular triangulation of the polytope P, prove that the h-
polynomial of the induced triangulation of ∂P has nonnegative coeﬃcients,
as does the h-polynomial of the link of every simplex in this triangulation.

10.19. Show that the construction in Exercise 10.17 gives the following char-
acterization of the h-polynomial of a simple polytope P: ﬁx a generic direction
vector v and orient the graph of P so that each oriented edge (viewed as a
vector) forms an acute angle with v. Then hk equals the number of vertices
of this oriented graph with in-degree k.

Open Problems 197

Open Problems

10.20. Which integral polytopes admit a unimodular triangulation? (The
property of admitting unimodular triangulations is part of an interesting
hierarchy of integral polytopes; see [74].)

10.21. Find a complete set of inequalities for the coeﬃcients of all h
∗-
polynomials of degree ≤ 3, i.e., piecewise linear regions in R3 all of whose
integer points (h
∗
1, h
∗
2, h
∗
3) come from an h
∗-polynomial of a 3-dimensional
integral polytope. (See also Open Problem 3.43.)

10.22. A linear inequality a0x0 + a1x1 + . . . adxd ≥ 0 is balanced if a0 + a1 +
· · · + ad = 0. Find a complete set of balanced inequalities for the coeﬃcients
of every h
∗-polynomial of degree ≤ 6. (For degree ≤ 5, see [233].)

10.23. Prove that every integrally closed reﬂexive polytope has a unimodal
h
∗-polynomial. More generally, prove that every integrally closed polytope has
a unimodal h
∗-polynomial. Even more generally, classify integral polytopes
with a unimodal h
∗-polynomial. (See [12, 64, 75, 211] for possible starting
points.)

Chapter 11
The Decomposition of a Polytope into
Its Cones

Mathematics compares the most diverse phenomena and discovers the secret analogies that
unite them.

Jean Baptiste Joseph Fourier (1768–1830)

In this chapter, we return to integer-point transforms of rational cones and
polytopes and connect them in a magical way that was ﬁrst discovered by
Michel Brion. The power of Brion’s theorem has been applied to various
domains, such as Barvinok’s algorithm in integer linear programming, and to
higher-dimensional Euler–Maclaurin summation formulas, which we study in
Chapter 12. In a sense, Brion’s theorem is the natural extension of the familiar
ﬁnite geometric series identity ∑b
m=a zm = zb+1−za
z−1 to higher dimensions.

11.1 The Identity “∑

m∈Z zm = 0”. . .
Or “Much Ado About Nothing”

We begin gently by illustrating Brion’s theorem in dimension 1. To this end,
let’s consider the line segment I := [20, 34]. We recall that its integer-point
transform lists the lattice points in I in the form of monomials:

σI(z) = ∑

m∈I∩Z zm = z20 + z21 + · · · + z34.

Already in this simple example, we are too lazy to list all integers in I and
use · · · to write the polynomial σI. Is there a more compact way to write
σI? The reader might have guessed it even before we asked the question: this
integer-point transform equals the rational function
 199

200 11 The Decomposition of a Polytope into Its Cones

σI(z) = z20 − z35

1 − z .

This last sentence is not quite correct: the deﬁnition of σI(z) yielded a
polynomial in z, whereas the rational function above is not deﬁned at z = 1.
We can overcome this deﬁciency by noticing that the limit of this rational
function as z → 1 equals the evaluation of the polynomials σI(1) = 15, by
L’Hˆopital’s rule. Notice that the rational-function representation of σI has
the unquestionable advantage of being much more compact than the original
polynomial representation. The reader who is not convinced of this advantage
should replace the right vertex 34 of I by 3400.
Now let’s rewrite the rational form of the integer-point transform of I
slightly:
 σI(z) = z20 − z35

1 − z = z20

1 − z + z34

1 − 1
z . (11.1)

There is a natural geometric interpretation of the two summands on the
right-hand side. The ﬁrst term represents the integer-point transform of the
interval [20, ∞):
 σ[20,∞)(z) = ∑

m≥20 zm = z20

1 − z .

The second term in (11.1) corresponds to the integer-point transform of the
interval (−∞, 34]:
 σ(−∞,34](z) = ∑

m≤34 zm = z34

1 − 1
z .

So (11.1) says that on a rational-function level,

σ[20,∞)(z) + σ(−∞,34](z) = σ[20,34](z) . (11.2)

20 34

20 34

20 34
 Fig. 11.1 Decomposing a line segment into two inﬁnite rays.

This identity, which we illustrate graphically in Figure 11.1, should come
as a mild surprise. Two rational functions that represent inﬁnite sequences

11.2 Technically Speaking. . . 201

somehow collapse, when being summed up, to a polynomial with a ﬁnite
number of terms. We emphasize that (11.2) does not make sense on the level
of inﬁnite series; in fact, the two inﬁnite series involved here have disjoint
regions of convergence.
Even more magical is the geometry behind this identity: on the right-hand
side, we have a polynomial that lists the integer points in a ﬁnite interval P,
while on the left-hand side, each of the rational generating functions represents
the integer points in an inﬁnite ray that begins at a vertex of P. The two
half-lines will be called vertex cones below, and indeed, the remainder of
this chapter is devoted to proving that an identity similar to (11.2) holds in
general dimension.
We recall a deﬁnition that was touched on only brieﬂy in Exercises 3.19
and 9.8: A hyperplane arrangement H is a ﬁnite collection of hyperplanes.
An arrangement H is rational if all its hyperplanes are rational, that is, if each
hyperplane in H is of the form {
x ∈ Rd : a1x1 + a2x2 + · · · + adxd = b} for
some a1, a2, . . . , ad, b ∈ Z. An arrangement H is called a central hyperplane
arrangement if its hyperplanes meet in (at least) one point.
Our next deﬁnition generalizes (ﬁnally) the notion of a pointed cone, deﬁned
in Chapter 3. A cone is the intersection of ﬁnitely many half-spaces of the
form {
x ∈ Rd : a1x1 + a2x2 + · · · + adxd ≤ b}

for which the corresponding hyperplanes
{
x ∈ Rd : a1x1 + a2x2 + · · · + adxd = b}

form a central arrangement. This deﬁnition extends that of a pointed cone: a
cone is pointed if the deﬁning hyperplanes meet in exactly one point. Thus
nonpointed cones are cones that contain a line. A cone is rational if all of
its deﬁning hyperplanes are rational. Cones and polytopes are special cases
of polyhedra, which are convex bodies deﬁned as the intersection of ﬁnitely
many half-spaces. Our next goal is to prove that every rational cone that
contains a line essentially has integer-point transform equal to zero, in a sense
that we have to make mathematically precise.

11.2 Technically Speaking. . .

To understand integer-point transforms of general cones, we need a small
aspect of the theory of modules, the technically necessary tools to make things
rigorous. To see what kind of problems might arise, consider the situation
of Alice who decides to glue together a few pointed cones Aj to form some
(not necessarily convex) polyhedral region K, and her friend Bob decides
to glue together some other pointed cones Bj, to form the same region K.
Why should it be true that the sum of the rational functions that we have

202 11 The Decomposition of a Polytope into Its Cones

associated with the pointed cones Aj equals the sum of the rational functions
that we have associated with the pointed cones Bj? We must account for this
inherent potential ambiguity and show that it is in fact unambiguous—Alice
and Bob will always get the same rational functions.
We recall that a module M over a ring R is a generalization of a vector
space over a ﬁeld, where the salient new feature is that the ﬁeld of scalars is
replaced by a ring of scalars. Consider, for example, the set of all polynomials
in d variables with coeﬃcients in Z, under addition. We can think intuitively
of this particular module over the ring Z as a discretized version of a vector
space over the ﬁeld of real numbers.
The only module notions that are important to us in this chapter are that
M forms an Abelian group under addition, that we can multiply elements of R
by elements of M in a sensible way (e.g., compatible with ring multiplication
in R), and that we preserve the deﬁnition of a linear map φ between two
modules M and N over the same ring R, namely, φ satisﬁes

φ(m1 + r m2) = φ(m1) + r φ(m2)

for every m1, m2 ∈ M and r ∈ R.
From the point of departure for this chapter, it might not come as a surprise
that the two modules we will use are formed by Laurent series and by rational
functions. We cannot multiply two Laurent series in a meaningful way (and
a reader who has not thought about this should construct an example in
which things go wrong), but we can multiply a Laurent series by a Laurent
polynomial, i.e., a ﬁnite Laurent series. This motivates the choice of ring with
which we will be operating, namely, the ring

C [
z±] := C [
z±
1 , z±
2 , . . . , z±
d ]

of Laurent polynomials in d variables with coeﬃcients in C. We will con-
sider two modules over C [z±]: on the one hand, the set CLd of all (for-
mal) Laurent series of rational cones in Rd, and on the other hand, the set
C(z) := C(z1, z2, . . . , zd) of rational functions in d variables.
In Chapter 3, we saw that certain Laurent series, namely integer-point
transforms of rational simplicial cones, naturally evaluate to rational functions,
by a natural tiling argument. The following lemma says that we can think of
this evaluation as one instance of a linear map between the modules CLd and
C(z) over C [z±].

Lemma 11.1. There is a unique linear map φ : CLd → C(z) that maps an
integer-point transform (viewed as a Laurent series) of a rational simplicial
cone
 {v + λ1w1 + λ2w2 + · · · + λkwk : λ1, λ2, . . . , λk ≥ 0} ⊆ Rd

to the rational function

11.2 Technically Speaking. . . 203

σΠ(z)
(1 − zw1) (1 − zw2) · · · (1 − zwk ) ,

where σΠ(z) is the integer-point transform of the half-open parallelepiped

Π := {v + λ1w1 + λ2w2 + · · · + λkwk : 0 ≤ λ1, λ2, . . . , λk < 1} . (11.3)

To understand the signiﬁcance of this lemma, we note that CLd is generated
by the integer-point transforms of rational simplicial cones, since every rational
cone can be triangulated by rational simplicial cones. Thus Lemma 11.1 says
that the rational forms of integer-point generating functions of simplicial
cones, which we derived in Chapter 3, extend uniquely to rational forms of
integer-point generating functions of all rational cones.

Proof of Lemma 11.1. Let

K := {v + λ1w1 + λ2w2 + · · · + λkwk : λ1, λ2, . . . , λk ≥ 0}

be a simplicial rational k-cone in Rd. For clarity, let’s consider σK(z) as an
element in CLd, and for this Laurent series we proved in Chapter 3 the identity

(1 − zw1) (1 − zw2 ) · · · (1 − zwk ) σK(z) = σΠ(z) , (11.4)

where Π is given by (11.3). We remark that (11.4) is an identity in the module
CLd over C [z±]: the factor (1 − zw1 ) (1 − zw2) · · · (1 − zwk ) on the left-hand
side and the right-hand side σΠ(z) are Laurent polynomials in C [z±], whereas
σK(z) is in CLd.
If K is now a general rational cone, we can triangulate it into simplicial cone,
each of which comes with a version of (11.4). The integer-point transform
σK(z) ∈ CLd of our general cone K can naturally be written in an inclusion–
exclusion form as a sum (with positive and negative terms) of integer-point
transforms of these simplicial cones and their faces, which are also simplicial
cones. Applying the same sum to the identities of the form (11.4) for these
simplicial cones gives an identity

g(z) σK(z) = f (z)

for some Laurent monomials f (z) and g(z). This yields our sought-after linear
map: we deﬁne
 φ (σK(z)) := f (z)
g(z) ∈ C(z) .

That this map φ is linear follows by construction, and that it is unique
follows from the uniqueness of the rational-function form of σK(z) when K is
simplicial. ⊓⊔

204 11 The Decomposition of a Polytope into Its Cones

The linear map φ in Lemma 11.1 allows us to make precise our aforemen-
tioned statement that integer-point transforms of rational cones that contain
a line are philosophically equal to zero.

Lemma 11.2. Let φ : CLd → C(z) be the linear map in Lemma 11.1, and let
K ⊆ Rd be a rational cone that contains a line. Then

φ (σK(z)) = 0 .

Proof. Let K ⊆ Rd be a rational cone that contains a line. This implies that
there exists a vector w ∈ Z
d \ {0} such that w + K = K. Translated into the
language of Laurent series, this means that zw σK(z) = σK(z), and thus, since
φ is linear, zw φ (σK(z)) = φ (σK(z)) .

But this gives the identity (1 − zw) φ (σK(z)) = 0 in the world C(z) of rational
functions. Since 1 − zw is not a zero divisor in this world, we conclude that
φ (σK(z)) = 0. ⊓⊔

11.3 Tangent Cones and Their Rational Generating
Functions

The goal of this section, apart from developing the language that allows us
to prove Brion’s theorem, is to prove a sort of analogue of (11.2) in general
dimension.
We now attach a cone to each face F of P, namely its tangent cone,
deﬁned by
 KF := {x + λ (y − x) : x ∈ F, y ∈ P, λ ∈ R≥0} .

We note that KP = span P. For a vertex v of P, the tangent cone Kv is often
called a vertex cone; it is pointed, and we show an example in Figure 11.2.
For a k-face F of P with k > 0, the tangent cone KF is not pointed. For
example, the tangent cone of an edge of a 3-polytope is a wedge.

Lemma 11.3. For every face F of P, we have span F ⊆ KF .

Proof. As x and y vary over all points of F, the points x + λ (y − x) vary
over span F. ⊓⊔

We note that this lemma implies that KF contains a line unless F is a
vertex. More precisely, if KF is not pointed, it contains the aﬃne space span F ,
which is called the apex of the tangent cone. (A pointed cone has a point as
apex. We also remark that KF is the smallest convex cone with apex span F
that contains P.) Consequently, Lemma 11.2 implies the following:

11.4 Brion’s Theorem 205

Fig. 11.2 A vertex cone.

v
 P
 K v
 Corollary 11.4. Let φ : CLd → C(z) be the linear map in Lemma 11.1, and
let F be a face of P that is not a vertex. Then

φ (σKF (z)) = 0 .

11.4 Brion’s Theorem

The following theorem is a classical identity of convex geometry named after
Charles Julien Brianchon (1783–1864)1 and Jørgen Pedersen Gram (1850–
1916).2 It holds for every convex polytope. However, its proof for simplices
is considerably simpler than that for the general case. We need only the
Brianchon–Gram identity for simplices, so we restrict ourselves to this special
case. (One could prove the general case along similar lines as below; however,
we would need some additional machinery not covered in this book.) The
indicator function 1S of a set S ⊆ Rd is deﬁned by

1S(x) := { 1 if x ∈ S,
0 if x ̸∈ S.

Theorem 11.5 (Brianchon–Gram identity for simplices). Let ∆ be a
d-simplex. Then 1∆(x) = ∑

F ⊆∆(−1)
dim F 1KF (x) ,

where the sum is taken over all nonempty faces F of ∆.

Proof. We distinguish between two disjoint cases: whether or not x is in the
simplex.

1 For more information about Brianchon, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Brianchon.html.
2 For more information about Gram, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Gram.html.

206 11 The Decomposition of a Polytope into Its Cones

Case 1: x ∈ ∆. Then x ∈ KF for each F of ∆, and the identity becomes

1 = ∑

F ⊆∆(−1)dim F =
 dim ∆∑

k=0 (−1)
kfk .

This is the Euler relation for simplices, proved in Exercise 5.6.

Case 2: x /∈ ∆. Then there is a unique minimal face F of ∆ (minimal with
respect to dimension) such that x ∈ KF and x ∈ KG for all faces G ⊆ ∆ that
contain F (Exercise 11.4). The identity to be proved is now

0 = ∑

G⊇F(−1)dim G. (11.5)

The validity of this identity again follows from the logic of Exercise 5.6; the
proof of (11.5) is the subject of Exercise 11.6. ⊓⊔

Corollary 11.6 (Brion’s theorem for simplices). Suppose ∆ is a ratio-
nal simplex. Then we have the following identity of rational functions:

σ∆(z) = ∑

v a vertex of ∆ σKv (z) .

Proof. We translate the Brianchon–Gram theorem into the language of inte-
ger-point transforms: we sum both sides of the identity in Theorem 11.5 for
all m ∈ Z
d, ∑

m∈Zd 1∆(m) zm = ∑

m∈Zd
 ∑

F ⊆∆(−1)dim F 1KF (m) zm,

which is equivalent to
 σ∆(z) = ∑

F ⊆∆(−1)
dim F σKF (z) .

Now we apply the linear map φ : CLd → C(z) from Lemma 11.1 to this
identity: φ (σ∆(z)) = ∑

F ⊆∆(−1)
dim F φ (σKF (z)) .

The left-hand side is the Laurent polynomial σ∆(z). On the right-hand side,
we can see the rational-function versions (which we may still denote by
σKv (z)) of the integer-point transforms of the (simplicial) vertex cones Kv,
and the remaining terms, namely φ (σKF (z)) for nonvertices F, disappear by
Corollary 11.4. ⊓⊔

Now we extend Corollary 11.6 to every convex rational polytope:

11.5 Brion Implies Ehrhart 207

Theorem 11.7 (Brion’s theorem). Suppose P is a rational convex poly-
tope. Then we have the following identity of rational functions:

σP (z) = ∑

v a vertex of P σKv (z) . (11.6)

Proof. We use the same irrational trick as in the proofs of Theorems 3.12
and 4.3. Namely, we begin by triangulating P into the simplices ∆1, ∆2, . . . , ∆m
(using no new vertices). Consider the hyperplane arrangement

H := {span F : F is a facet of ∆1, ∆2, . . . , or ∆m} .

We will now shift the hyperplanes in H, obtaining a new hyperplane arrange-
ment Hshift. Those hyperplanes of H that deﬁned P now deﬁne, after shifting,
a new polytope that we will call P shift. Exercise 11.8 ensures that we can shift
H in such a way that:

• no hyperplane in Hshift contains a lattice point;
• Hshift yields a triangulation of P shift;
• the lattice points contained in a vertex cone of P are precisely the lattice
points contained in the corresponding vertex cone of P shift.

This setup implies that

• the lattice points in P are precisely the lattice points in P shift;
• the lattice points in a vertex cone of P shift can be written as a disjoint
union of lattice points in vertex cones of simplices of the triangulation that
Hshift induces on P shift.

The latter two conditions, in turn, mean that Brion’s identity (11.6) follows
from Brion’s theorem for simplices: the integer-point transforms on both sides
of the identity can be written as a sum of integer-point transforms of simplices
and their vertex cones. ⊓⊔

11.5 Brion Implies Ehrhart

We conclude this chapter by showing that Ehrhart’s theorem (Theorem 3.23)
for rational polytopes (which includes the integral case, Theorem 3.8) follows
from Brion’s theorem (Theorem 11.7) in a relatively straightforward manner.

Second Proof of Theorem 3.23. As in our ﬁrst proof of Ehrhart’s theorem,
it suﬃces to prove Theorem 3.23 for simplices, because we can triangulate
any polytope (using only the vertices). So suppose ∆ is a rational d-simplex
whose vertices have coordinates with denominator p. Our goal is to show that
for a ﬁxed 0 ≤ r < p, the function L∆(r + pt) is a polynomial in t; this means
that L∆ is a quasipolynomial with period dividing p.

208 11 The Decomposition of a Polytope into Its Cones

First, if r = 0, then L∆(pt) = Lp∆(t), which is a polynomial by Ehrhart’s
theorem (Theorem 3.8), because p∆ is an integer simplex.
Now we assume r > 0. By Theorem 11.7,

L∆(r + pt) = ∑

m∈(r+pt)∆∩Zd
1

= lim
z→1 σ(r+pt)∆(z) (11.7)

= lim
z→1
 ∑

v vertex of ∆ σ(r+pt)Kv (z) .

We used the limit computation for the integer-point transform σ(r+pt)∆ rather
than the evaluation σ(r+pt)∆(1), because that evaluation would have yielded
singularities in the rational generating functions of the vertex cones. Note
that the vertex cones Kv are all simplicial, because ∆ is a simplex. So suppose

Kv = {v + λ1w1 + λ2w2 + · · · + λdwd : λ1, λ2, . . . , λd ≥ 0} ;

then

(r + pt)Kv = {(r + pt)v + λ1w1 + λ2w2 + · · · + λdwd : λ1, λ2, . . . , λd ≥ 0}

= tpv + {rv + λ1w1 + λ2w2 + · · · + λdwd : λ1, λ2, . . . , λd ≥ 0}

= tpv + rKv .

What is important to note here is that pv is an integer vector. In particular,
we can safely write σ(r+pt)Kv (z) = ztpvσrKv (z)

(we say safely because tpv ∈ Z
d, so ztpv is indeed a monomial). Now we can
rewrite (11.7) as
 L∆(r + pt) = lim
z→1
 ∑

v vertex of ∆ ztpvσrKv (z) . (11.8)

The exact form of the rational functions σrKv (z) is not important for the
purposes of the proof, except for the fact that they do not depend on t. We
know that the sum of the generating functions of all vertex cones is a Laurent
polynomial in z; that is, the singularities of the rational functions cancel. To
compute L∆(r + pt) from (11.8), we combine all of the rational functions on
the right-hand side over one denominator and use L’Hˆopital’s rule to compute
the limit of this one huge rational function. The variable t appears only in
the simple monomials ztpv, so the eﬀect of L’Hˆopital’s rule is that we obtain
linear factors of t every time we diﬀerentiate the numerator of this rational
function. At the end, we evaluate the remaining rational function at z = 1.
The result is a polynomial in t. ⊓⊔

Notes 209

Notes

1. Theorem 11.5 (in its general form for convex polytopes) has an interesting
history. In 1837, Charles Brianchon proved a version of this theorem involving
volumes of polytopes in R3 [66]. In 1874, Jørgen Gram gave a proof of the
same result [122]; apparently, he was unaware of Brianchon’s paper. In 1927,
Duncan Sommerville published a proof for general d [224], which was corrected
in the 1960s by Victor Klee [151], Branko Gr¨unbaum [127, Section 14.1], and
many others.

2. Michel Brion discovered Theorem 11.7 in 1988 [67]. His proof involved the
Baum–Fulton–Quart Riemann–Roch formula for equivariant K-theory of toric
varieties. A more elementary proof of Theorem 11.7 was found by Masa-Nori
Ishida a few years later [143]. Our approach in this chapter follows [41].

3. Around the time Theorem 11.7 was conceived, Jim Lawrence [162] and
Alexander Varchenko [250] discovered a companion theorem—it also gives the
integer-point transform of a rational polytope as a sum of rational functions
stemming from cones based at the vertices of the polytopes, but slightly
diﬀerent from the vertex cones. Both the Brion and the Lawrence–Varchenko
theorems can be neatly understood using the theory of valuations, which we
do not use here (see, for example, [161]).

4. As we have already remarked earlier, Brion’s theorem led to an eﬃcient
algorithm by Alexander Barvinok to compute Ehrhart quasipolynomials [25].
More precisely, Barvinok proved that in ﬁxed dimension, one can eﬃciently
3

compute the Ehrhart series ∑

t≥0 LP (t) zt as a short sum of rational functions.
4

Brion’s theorem essentially reduces the problem to computing the integer-
point transforms of the rational tangent cones of the polytope. Barvinok’s
ingenious idea was to use a signed decomposition of a rational cone to compute
its integer-point transform: the cone is written as a sum and diﬀerence of
unimodular cones, which we will encounter in Section 12.4 and which have
a trivial integer-point transform. Finding a signed decomposition involves
triangulations, Minkowski’s theorem on lattice points in convex bodies (see,
for example, [83, 179, 187, 221]), and the LLL algorithm, which ﬁnds a short
vector in a lattice [164]. At any rate, Barvinok proved that one can ﬁnd a
signed decomposition quickly, which is the main step toward computing the
Ehrhart series of the polytope. Barvinok’s algorithm has been implemented
in the software packages barvinok [251] and LattE [95, 97, 155]. Barvinok’s
algorithm is described in detail in [23].

3 Eﬃciently here means that for every dimension, there exists a polynomial that gives an
upper bound on the running time of the algorithm when evaluated at the logarithm of the
input data of the polytope (e.g., its vertices).

4 Short means that the set of data needed to output this sum of rational functions is also
of polynomial size in the logarithm of the input data of the polytope.

210 11 The Decomposition of a Polytope into Its Cones

Exercises

11.1. Prove that the cones in Rd are precisely the sets of the form

v + {x ∈ Rd : A x ≤ 0
}

for some v ∈ Rd and A ∈ Rm×d.

11.2. Recall that the orthogonal complement A⊥ of an aﬃne space A is
deﬁned by A⊥ := {x ∈ Rd : x · v = 0 for all v ∈ A} .

Prove that for every face F of a polytope, (span F)
⊥ ∩ KF is a pointed cone.
(Hint: Show that if H is a deﬁning hyperplane for F, then H ∩ (span F)
⊥ is
a hyperplane in the vector space (span F)
⊥.)

11.3. Let P ⊂ Rd be a full-dimensional polytope. A face F of P is visible
from the point x ∈ Rd if the line segment between x and any point y ∈ F
intersects P only in y. (We used this notion already in Exercise 10.16.) Show
that F is visible from x if and only if x /∈ KF .

11.4. ♣ Suppose ∆ is a simplex and x /∈ ∆. Prove that there is a unique
minimal face F ⊆ ∆ (minimal with respect to dimension) such that the
corresponding tangent cone KF contains x. Show that x ∈ KG for all faces
G ⊆ ∆ that contain F, and x /∈ KG for all other faces G.

11.5. Show that Exercise 11.4 fails to be true if ∆ is a quadrilateral (for
example). Show that the Brianchon–Gram identity holds for your quadrilateral.

11.6. ♣ Prove (11.5): for a face F of a simplex ∆,
∑

G⊇F(−1)dim G = 0 ,

where the sum is taken over all faces of ∆ that contain F.

11.7. Give a direct proof of Brion’s theorem for the 1-dimensional case.

11.8. ♣ Provide the details of the irrational-shift argument in the proof of
Theorem 11.7: Given a rational polytope P, triangulate it into the simplices
∆1, ∆2, . . . , ∆m (using no new vertices). Consider the hyperplane arrangement

H := {span F : F is a facet of ∆1, ∆2, . . . , ∆m} .

We will now shift the hyperplanes in H, obtaining a new hyperplane arrange-
ment Hshift. Those hyperplanes of H that deﬁned P now deﬁne, after shifting,
a new polytope that we will call P shift. Prove that we can shift H in such a
way that:

Exercises 211

• no hyperplane in Hshift contains any lattice point;
• Hshift yields a triangulation of P shift;
• the lattice points contained in a vertex cone of P are precisely the lattice
points contained in the corresponding vertex cone of P shift.

11.9. ♣ Prove the following “open polytope” analogue for Brion’s theorem: If
P is a rational convex polytope, then we have the identity of rational functions

σP ◦ (z) = ∑

v a vertex of P σK◦
v (z) .

11.10. Prove the following extension of Ehrhart’s theorem (Theorem 3.23):
Suppose P ⊂ Rd is a rational convex polytope and q is a polynomial in d
variables. Then L
q
P (t) := ∑

m∈tP∩Zd q(m)

is a quasipolynomial in t. (Hint: Modify the proof in Section 11.5 by intro-
ducing a diﬀerential operator.)

Chapter 12
Euler–Maclaurin Summation in Rd

All means (even continuous) sanctify the discrete end.

Doron Zeilberger

Thus far we have often been concerned with the diﬀerence between the discrete
volume of a polytope P and its continuous volume. In other words, the quantity

∑

m∈P∩Zd
1 − ∫

P dy , (12.1)

which is by deﬁnition LP (1) − vol(P), has been on our minds for a long time
and has arisen naturally in many diﬀerent contexts. An important extension is
the diﬀerence between the discrete integer-point transform and its continuous
sibling: ∑

m∈P∩Zd
e
m·x − ∫

P ey·xdy , (12.2)

where we have replaced the variable z that we have commonly used in generat-
ing functions by the exponential variable (z1, z2, . . . , zd) = (ex1, e
x2, . . . , exd ).
Note that on setting x = 0 in (12.2), we get the former quantity (12.1). Rela-
tions between the two quantities ∑

m∈P∩Zd em·x and ∫
P ey·xdy are known as
Euler–Maclaurin summation formulas for polytopes. The “behind-the-scenes”
operators that are responsible for aﬀording us with such connections are the
diﬀerential operators known as Todd operators, whose deﬁnition utilizes the
Bernoulli numbers in a surprising way.
 213

214 12 Euler–Maclaurin Summation in Rd

12.1 Todd Operators and Bernoulli Numbers

Recall the Bernoulli numbers Bk from Section 2.4, deﬁned by the generating
function z
ez − 1 = ∑

k≥0
 Bk
k! zk.

We now introduce a diﬀerential operator via essentially the same generating
function, namely
 Toddh := ∑

k≥0
(−1)k Bk
k!
 ( d
dh
 )k . (12.3)

This Todd operator is often abbreviated as

Toddh =
 d
dh
1 − e− d
dh ,

but we should keep in mind that this is only a shorthand notation for the
inﬁnite series (12.3). We ﬁrst show that the exponential function is an eigen-
function of the Todd operator.

Lemma 12.1. For z ∈ C \ {0} with |z| < 2π,

Toddh ezh = z e
zh

1 − e−z .

Proof.
 Toddh ezh = ∑

k≥0
(−1)
k Bk
k!
 ( d
dh
 )k ezh

= ∑

k≥0
(−1)k Bk
k! zke
zh

= ezh ∑

k≥0
(−z)
k Bk
k!

= ezh −z
e−z − 1 .

The condition |z| < 2π is needed in the last step, by Exercise 2.14. ⊓⊔

The Todd operator is a discretizing operator, in the sense that it transforms
a continuous integral into a discrete sum, as the following theorem shows.

Theorem 12.2 (Euler–Maclaurin in dimension 1). For all a < b ∈ Z
and z ∈ C with |z| < 2π,

12.1 Todd Operators and Bernoulli Numbers 215

Toddh1 Toddh2
 ∫ b+h1

a−h2 ezxdx

∣
∣
∣
∣
∣h1=h2=0 =
 b∑

k=a e
kz.

Proof. Case 1: z = 0. Then ezx = 1, and so

Toddh1 Toddh2
 ∫ b+h1

a−h2 ezxdx
∣
∣
∣
∣
∣
h1=h2=0

= Toddh1 Toddh2
 ∫ b+h1

a−h2 dx
∣
∣
∣
∣
∣h1=h2=0
= b − a + Toddh1 h1 + Toddh2 h2|h1=h2=0

= b − a + h1 + 1
2 + h2 + 1
2
 ∣
∣
∣
∣
h1=h2=0
= b − a + 1

by Exercise 12.1. Since ∑b
k=a ek·0 = b − a + 1, we have veriﬁed the theorem
in this case.

Case 2: z ̸= 0. Then

Toddh1 Toddh2
 ∫ b+h1

a−h2 ezxdx = Toddh1 Toddh2 1
z
 (ez(b+h1) − ez(a−h2))

= 1
z (Toddh1 ezb+zh1 − Toddh2 eza−zh2)

= ezb

z Toddh1 ezh1 − eza

z Toddh2 e−zh2

= e
zb

z z e
zh1

1 − e−z − eza

z −z e
−zh2

1 − ez ,

where the last step follows from Lemma 12.1. Hence

Toddh1 Toddh2
 ∫ b+h1

a−h2 ezxdx
∣
∣
∣
∣
∣h1=h2=0 = ezb 1
1 − e−z + eza 1
1 − ez

= ez(b+1) − eza

ez − 1

=
 b∑

k=a ekz. ⊓⊔

We will need a multivariate version of the Todd operator later, so we deﬁne
for h = (h1, h2, . . . , hm),

216 12 Euler–Maclaurin Summation in Rd

Toddh :=
 m∏

j=1
 


 ∂
∂hj

1 − exp (− ∂
∂hj
 )
 

 ,

keeping in mind that this is a product over inﬁnite series of the form (12.3).

12.2 A Continuous Version of Brion’s Theorem

In the following two sections, we develop the tools that, once fused with the
Todd operator, will enable us to extend Euler–Maclaurin summation to higher
dimensions. We ﬁrst give an integral analogue of Theorem 11.7 for simple
rational polytopes. We begin by translating Brion’s integer-point transforms

σP (z) = ∑

v a vertex of P σKv (z)

into an exponential form:

σP (exp z) = ∑

v a vertex of P σKv (exp z) ,

where we used the notation exp z = (ez1, e
z2 , . . . , ezd ). For the continuous
analogue of Brion’s theorem, we replace the sum on the left-hand side,

σP (exp z) = ∑

m∈P∩Zd (exp z)
m = ∑

m∈P∩Zd exp(m · z) ,

by an integral.

Theorem 12.3 (Brion’s theorem: continuous form). Suppose P is a
simple rational convex d-polytope. For each vertex cone Kv of P, ﬁx a set of
generators w1(v), w2(v), . . . , wd(v) ∈ Z
d. Then
∫

P exp(x · z) dx = (−1)
d ∑

v a vertex of P
 exp (v · z) |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · z)

for all z such that the denominators on the right-hand side do not vanish.

Proof. We begin with the assumption that P is an integral polytope; we will
see in the process of the proof that this assumption can be relaxed. Let’s
write out the exponential form of Brion’s theorem (Theorem 11.7), using the
assumption that the vertex cones are simplicial (because P is simple). By
Theorem 3.5,

∑

m∈P∩Zd exp(m · z) = ∑

v a vertex of P
 exp(v · z) σΠv (exp z)
∏d
k=1 (1 − exp (wk(v) · z)) , (12.4)

12.2 A Continuous Version of Brion’s Theorem 217

where

Πv = {λ1w1(v) + λ2w2(v) + · · · + λdwd(v) : 0 ≤ λ1, λ2, . . . , λd < 1}

is the fundamental parallelepiped of the vertex cone Kv. We would like to
rewrite (12.4) with the lattice Z
d replaced by the reﬁned lattice ( 1
n Z
)d, because
then, the left-hand side of (12.4) will give rise to the sought-after integral by
letting n approach inﬁnity. The right-hand side of (12.4) changes accordingly;
now every integral point has to be scaled down by 1
n :

∑

m∈P∩( 1
n Z)
d exp(m · z) = ∑

v a vertex of P
 exp(v · z) ∑

m∈Πv∩Zd exp ( m
n · z)

∏d
k=1 (1 − exp ( wk(v)
n · z)) .

(12.5)
The proof of this identity is in essence the same as that of Theorem 3.5; we
leave it as Exercise 12.2. Now our sought-after integral is
∫

P exp(x · z) dx = lim
n→∞ 1
nd ∑

m∈P∩( 1
n Z)
d exp(m · z)

= lim
n→∞ 1
nd ∑

v a vertex of P
 exp(v · z) ∑
m∈Πv∩Zd exp ( m
n · z)

∏d
k=1 (1 − exp ( wk(v)
n · z)) .

(12.6)

At this point, we can see that our assumption that P has integral vertices
can be relaxed to the rational case, since we may compute the limit only for
n’s that are multiples of the denominator of P. The numerators of the terms
on the right-hand side have a simple limit:

lim
n→∞ exp(v · z) ∑

m∈Πv∩Zd exp ( m
n · z) = exp(v · z) ∑

m∈Πv∩Zd 1

= exp (v · z) |det (w1(v), . . . , wd(v))| ,

where the last identity follows from Lemma 9.2. Hence (12.6) simpliﬁes to
∫

P exp(x · z) dx = ∑

v a vertex of P
 exp (v · z) |det (w1(v), . . . , wd(v))|
∏d
k=1 limn→∞ n (1 − exp ( wk(v)
n · z)) .

Finally, using L’Hˆopital’s rule,

lim
n→∞ n (1 − exp ( wk(v)
n · z)) = −wk(v) · z ,

and the theorem follows. ⊓⊔

218 12 Euler–Maclaurin Summation in Rd

It turns out (Exercise 12.6) that for each vertex cone Kv,
∫

Kv exp(x · z) dx = (−1)
d exp (v · z) |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · z) , (12.7)

and Theorem 12.3 shows that the Fourier–Laplace transform of P equals the
sum of the Fourier–Laplace transforms of the vertex cones. In other words,
∫

P exp(x · z) dx = ∑

v a vertex of P
 ∫

Kv exp(x · z) dx .

We also remark that |det (w1(v), . . . , wd(v))| has a geometric meaning: it
is the volume of the fundamental parallelepiped of the vertex cone Kv.
The curious reader might wonder what happens to the statement of Theo-
rem 12.3 if we scale each of the generators wk(v) by a diﬀerent factor. It is
immediate (Exercise 12.7) that the right-hand side of Theorem 12.3 remains
invariant.
There is an important diﬀerence between the vertex cone generating func-
tions (integrals) that appear in the continuous version of Brion’s theorem
(Theorem 12.3) and the vertex cone generating functions (sums) that appear
in the discrete Brion theorem (Theorem 11.7). To see the diﬀerence, consider
the following example:
Let K0 be the ﬁrst quadrant in R2, having generators (1, 0) and (0, 1).
Let K1 be the cone deﬁned as the nonnegative real span of (1, 0) and (1, k).
For k = 2100, say, we see that for all practical purposes, K1 is very close to
K0 in its geometry, in the sense that their angles are almost the same for
computational purposes, and thus their continuous Brion generating functions
are almost the same, computationally.
However, σK0(z) is quite far from σK1(z), since the latter has 2100 terms
in its numerator, while the former has only 1 as its trivial numerator. Thus,
tangent cones that are “arbitrarily close” geometrically may simultaneously
be “arbitrarily far” from each other in the discrete sense dictated by the
integer points in their fundamental domains.

12.3 Polytopes Have Their Moments

The most common notion for moments of a set P ⊂ Rd is the collection of
monomial moments deﬁned by the real numbers

µa := ∫

P ya dy = ∫

P ya1
1 ya2
2 · · · yad
d dy, (12.8)

for a ﬁxed vector a = (a1, a2, . . . , ad) ∈ Cd. For example, when a = 0 =
(0, 0, . . . , 0), we get µ0 = vol P. As an application of moments, consider the

12.3 Polytopes Have Their Moments 219

problem of ﬁnding the center of mass of P, which is deﬁned by

1
vol P
 (∫

P y1 dy , ∫

P y2 dy , . . . , ∫

P yd dy) .

This integral is equal to

1
µ0
 (µ(1,0,0,...,0), µ(0,1,0,...,0), . . . , µ(0,...,0,1)) .

Similarly, one can deﬁne the variance of P and other statistical data attached
to P and use moments to compute them.
Our next task is to relate the monomial moments µa to the formula of
Theorem 12.3. One way to do this is to diﬀerentiate the continuous Brion
identity in Theorem 12.3 repeatedly with respect to each zj, and in fact,
interchanging these derivatives with the integral is valid because we are
integrating over a compact region P. Thus, for a simple rational polytope P,
∫

P xa1
1 xa2
2 · · · xad
d exp(x · z) dx

= ∫

P
 ( ∂
∂z1
 )a1
· · · ( ∂
∂zd
 )ad exp(x · z) dx

= (−1)d ∑

v a vertex of P
 ( ∂
∂z1
 )a1
· · · ( ∂
∂zd
 )ad exp (v · z) |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · z) .

If we take the limit as each zj → 0 of both sides of the latter identity, we have
a formula (albeit a messy one) for the monomial moments:

(−1)dµa =

lim
z→0
 ∑

v a vertex of P
 ( ∂
∂z1
 )a1
· · · ( ∂
∂zd
 )ad exp (v · z) |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · z) .

This formula for the monomial moments may be used eﬀectively for rela-
tively small integer values of the exponent a = (a1, a2, . . . , ad). Going a step
further, we can use Theorem 12.3 to obtain information about a diﬀerent set
of moments, which are sometimes called axial moments. Along the way, we
stumble upon the following amazing formula for the continuous volume of a
polytope.

Theorem 12.4. Suppose P is a simple rational convex d-polytope. For each
vertex cone Kv of P, ﬁx a set of generators w1(v), w2(v), . . . , wd(v) ∈ Z
d.
Then
 vol P = (−1)d

d!
 ∑

v a vertex of P
 (v · z)
d |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · z)

220 12 Euler–Maclaurin Summation in Rd

for all z such that the denominators on the right-hand side do not vanish.
More generally, for every integer j ≥ 0,

∫

P (x · z)
j dx = (−1)
dj!
(j + d)!
 ∑

v a vertex of P
 (v · z)
j+d |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · z) .

Proof. We replace the variable z in the identity of Theorem 12.3 by sz, where
s is a scalar:
∫

P exp (x · (sz)) dx = (−1)d ∑

v a vertex of P

exp (v · (sz)) |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · (sz)) ,

which can be rewritten as
∫

P exp (s (x · z)) dx = (−1)
d ∑

v a vertex of P

exp (s (v · z)) |det (w1(v), . . . , wd(v))|

sd ∏d
k=1 (wk(v) · (z)) .

The general statement of the theorem follows now by ﬁrst expanding the
exponential functions as Taylor series in s, and then comparing coeﬃcients
on both sides:

∑

j≥0
 ∫

P (x · z)j dx s
j

j!

= (−1)d ∑

v a vertex of P
 ∑

j≥0 (v · z)j s
j−d

j! |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · (z))

= ∑

j≥−d(−1)
d ∑

v a vertex of P
(v · z)
j+d |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · (z))
 s
j

(j + d)! . ⊓⊔

The proof of this theorem reveals yet more identities between rational
functions. Namely, the coeﬃcients of the negative powers of s in the last line
of the proof have to be zero. This immediately yields the following curious
set of d identities for simple d-polytopes:

Corollary 12.5. Suppose P is a simple rational convex d-polytope. For each
vertex cone Kv of P, ﬁx a set of generators w1(v), w2(v), . . . , wd(v) ∈ Z
d.
Then for each 0 ≤ j ≤ d − 1,

∑

v a vertex of P
(v · z)j |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · (z)) = 0 . ⊓⊔

12.4 Computing the Discrete Continuously 221

12.4 Computing the Discrete Continuously

In this section, we apply the Todd operator to a perturbation of the continuous
volume. Namely, consider a simple full-dimensional polytope P, which we
may write as P = {x ∈ Rd : A x ≤ b
} .

Then we deﬁne the perturbed polytope

P(h) := {
x ∈ Rd : A x ≤ b + h
}

for a small vector h ∈ Rm (we will quantify the word small in a moment). A
famous theorem due to Askold Khovanski˘ı and Aleksandr Pukhlikov says that
the integer-point count in P can be obtained by applying the Todd operator
to vol (P(h)). Here we prove the theorem for a certain class of polytopes,
which we need to deﬁne ﬁrst.
We call a rational pointed d-cone unimodular if its generators are a basis
of Z
d. An integral polytope is unimodular if each of its vertex cones is
unimodular.
1

Theorem 12.6 (Khovanski˘ı–Pukhlikov theorem). For a unimodular d-
polytope P, # (P ∩ Z
d) = Toddh vol (P(h))|h=0 .

More generally,
 σP (exp z) = Toddh
 ∫

P(h) exp(x · z) dx
∣
∣
∣
∣
∣h=0 .

Proof. We use Theorem 12.3, the continuous version of Brion’s theorem; note
that if P is unimodular, then P is automatically simple. For each vertex
cone Kv of P, denote its generators by w1(v), w2(v), . . . , wd(v) ∈ Z
d. Then
Theorem 12.3 states that
∫

P exp(x · z) dx = (−1)d ∑

v a vertex of P
 exp (v · z) |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · z)

= (−1)d ∑

v a vertex of P
 exp (v · z)
∏d
k=1 (wk(v) · z) , (12.9)

where the last identity follows from Exercise 12.3. A similar formula holds
for P(h), except that we have to account for the shift of the vertices. The
vector h shifts the facet-deﬁning hyperplanes. This shift of the facets induces
a shift of the vertices; let’s say that the vertex v gets moved along each edge
direction wk (the vectors that generate the vertex cone Kv) by hk(v), so that

1 Unimodular polytopes go by two additional names, namely smooth and Delzant.

222 12 Euler–Maclaurin Summation in Rd

P(h) has now the vertex v − ∑d
k=1 hk(v)wk(v). If h is small enough, P(h)
will still be simple,
2 and we can apply Theorem 12.3 to P(h):

∫

P(h) exp(x · z) dx = (−1)
d ∑

v a vertex of P
 exp ((v − ∑d
k=1 hk(v)wk(v)
) · z)

∏d
k=1 (wk(v) · z)

= (−1)d ∑

v a vertex of P
 exp (
v · z − ∑d
k=1 hk(v)wk(v) · z)

∏d
k=1 (wk(v) · z)

= (−1)d ∑

v a vertex of P
 exp(v · z) ∏d
k=1 exp (−hk(v)wk(v) · z)
∏d
k=1 (wk(v) · z) .

Strictly speaking, this formula holds only for h ∈ Qm, so that the vertices
of P(h) are rational. Since we will eventually set h = 0, this is a harmless
restriction. Now we apply the Todd operator:

Toddh
 ∫

P(h) exp(x · z) dx
∣
∣
∣
∣
∣h=0

= (−1)d ∑

v vertex of P Toddh exp(v · z) ∏d
k=1 exp (−hk(v)wk(v) · z)
∏d
k=1 (wk(v) · z)
 ∣
∣
∣
∣
∣
h=0

= (−1)d ∑

v vertex of P
 exp(v · z)
∏d
k=1 (wk(v) · z)

×
 d∏

k=1 Toddhk(v) exp (−hk(v)wk(v) · z)

∣
∣
∣
∣
∣hk(v)=0 .

By a multivariate version of Lemma 12.1,

Toddh
 ∫

P(h) exp(x · z) dx
∣
∣
∣
∣
∣h=0

= (−1)d ∑

v vertex of P
 exp (v · z)
∏d
k=1 (wk(v) · z)
 d∏

k=1
 −wk(v) · z
1 − exp(wk(v) · z)

= ∑

v vertex of P exp (v · z)
 d∏

k=1
 1
1 − exp(wk(v) · z) .

However, Brion’s theorem (Theorem 11.7), together with the fact that P is
unimodular, says that the right-hand side of this last formula is precisely the
integer-point transform of P (see also (12.9)), and thus

2 The cautious reader may consult [259, p. 66] to conﬁrm this fact.

Notes 223

Toddh
 ∫

P(h) exp(x · z) dx
∣
∣
∣
∣
∣h=0 = σP (exp z) .

Finally, setting z = 0 gives

Toddh
 ∫

P(h) dx
∣
∣
∣
∣
∣h=0 = ∑

m∈P∩Zd 1 ,

as claimed. ⊓⊔

We note that ∫
P(h) exp(x · z) dx is, by deﬁnition, the continuous Fourier–
Laplace transform of P(h). Upon being acted on by the discretizing operator
Toddh, the integral ∫
P(h) exp(x · z) dx gives us the discrete integer-point
transform σP (z).

Notes

1. The classical Euler–Maclaurin formula states that

n∑

k=1 f (k) = ∫ n

0 f (x) dx + f (0) + f (n)
2 +
 p∑

m=1
 B2m
(2m)!
 [
f (2m−1)(x)
]n

0

+ 1
(2p + 1)!
 ∫ n

0 B2p+1 ({x}) f (2p+1)(x) dx ,

where Bk(x) denotes the kth Bernoulli polynomial. It was discovered indepen-
dently by Leonhard Euler and Colin Maclaurin (1698–1746).3 This formula
provides an explicit error term, whereas Theorem 12.2 provides a summation
formula with no error term.

2. The Todd operator was introduced by Friedrich Hirzebruch in the 1950s
[139], following a more complicated deﬁnition by John A. Todd [244,245] some
twenty years earlier. The Khovanski˘ı–Pukhlikov theorem (Theorem 12.6) can
be interpreted as a combinatorial analogue of the algebrogeometric Hirzebruch–
Riemann–Roch theorem, in which the Todd operator plays a prominent role.

3. Theorem 12.3, the continuous form of Brion’s theorem, was generalized by
Alexander Barvinok to every polytope [20]. In fact, [20] contains a certain
extension of Brion’s theorem to irrational polytopes as well. The decomposition
formula for moments of a polytope in Theorem 12.4 is due to Michel Brion
and Mich`ele Vergne [68].

3 For more information about Maclaurin, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Maclaurin.html.

224 12 Euler–Maclaurin Summation in Rd

4. A natural question arises regarding moments of a given polytope, namely
the following inverse problem: how many axial moments of a polytope P
do we need to know in order to reconstruct the vertices of P? A solution
was given in [123] recently, and it turns out to be at most O(dN ), where
d = dim(P) and N is the number of vertices of P . Practical implementations
of this algorithm, which ﬁnd applications in computer graphics and computer
vision, are still being developed. A nice resource for related moment problems
is the book [159].

5. Theorem 12.6 was ﬁrst proved in 1992 by Askold Khovanski˘ı and Aleksandr
Pukhlikov [148]. The proof we give here is essentially theirs. Their paper [148]
also draws parallels between toric varieties and lattice polytopes. Subsequently,
many attempts to provide formulas for Ehrhart quasipolynomials—some
based on Theorem 12.6—have provided fertile ground for deeper connections
and future work; a long but by no means complete list of references is
[15, 16, 51, 68, 80, 86, 87, 107, 128, 146, 147, 160, 169, 183, 194, 241].

Exercises

12.1. ♣ Show that Toddh h = h + 1
2 . More generally, prove that

Toddh h
k = Bk(h + 1)

for k ≥ 1, where Bk(x) denotes the kth Bernoulli polynomial. Thus, the Todd
operators take the usual monomial basis to the basis of Bernoulli polynomials.

12.2. ♣ Prove (12.5): Suppose P is a simple integral d-polytope. For each
vertex cone Kv of P, denote its generators by w1(v), w2(v), . . . , wd(v) ∈ Z
d

and its fundamental parallelepiped by Πv. Then

∑

m∈P∩( 1
n Z)d exp(m · z) = ∑

v a vertex of P
 exp(v · z) ∑
m∈Πv∩Zd exp ( m
n · z)

∏d
k=1 (1 − exp ( wk(v)
n · z)) .

12.3. ♣ Given a unimodular cone

K = {v + λ1w1 + λ2w2 + · · · + λdwd : λ1, λ2, . . . , λd ≥ 0} ,

where v, w1, w2, . . . , wd ∈ Z
d such that w1, w2, . . . , wd are a basis for Z
d,
show that σK(z) = zv
∏d
k=1 (1 − zwk )

and |det (w1, . . . , wd)| = 1.

Open Problems 225

12.4. Compute the integral (Fourier–Laplace transform) given by the formula
of Theorem 12.4 for the standard simplex in Rd,

∆ = {(x1, x2 . . . , xd) ∈ Rd : x1 + x2 + · · · + xd ≤ 1 and all xk ≥ 0} .

12.5. Using the previous exercise, compute the center of mass of the standard
simplex in Rd.

12.6. ♣ Prove (12.7). That is, for the simplicial cone

K =
 {
v +
 d∑

k=1 λkwk : λk ≥ 0

}

with v, w1, w2, . . . , wd ∈ Qd, show that
∫

K exp(x · z) dx = (−1)d exp (v · z) |det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · z) .

12.7. Show that in the statement of Theorem 12.3, the expression

|det (w1(v), . . . , wd(v))|
∏d
k=1 (wk(v) · z)

remains invariant on scaling each wk(v) by an independent positive integer.

12.8. The binomial transform of a given sequence (an)
∞
n=0 is the sequence
bn := ∑n
k=0(−1)k(n
k)ak. Prove that the Bernoulli numbers Bn are self-dual
with respect to this transform:

Bn =
 n∑

k=0
(−1)k(n
k
)Bk .

12.9. Prove that if P is an integral d-polytope and f (x1, x2, . . . , xd) is a
polynomial in d variables, then the following expression is a polynomial in t:

LP,f (t) := ∑

m∈tP∩Zd f (m) .

Open Problems

12.10. Find all diﬀerentiable eigenfunctions of the Todd operator.

12.11. (a) Classify all polytopes whose discrete and continuous volumes coin-
cide, that is, LP (1) = vol(P).
(b) Classify all (not necessarily closed) polytopes for which LP (t) = vol(P) t
d.

Chapter 13
Solid Angles

Everything you’ve learned in school as “obvious” becomes less and less obvious as you
begin to study the universe. For example, there are no solids in the universe. There’s not
even a suggestion of a solid. There are no absolute continuums. There are no surfaces.
There are no straight lines.

Buckminster Fuller (1895–1983)

The natural generalization of a 2-dimensional angle to higher dimensions is
called a solid angle. Given a pointed cone K ⊂ Rd, the solid angle at its apex
is the proportion of space that the cone K occupies. In slightly diﬀerent words,
if we pick a point x ∈ Rd “at random,” then the probability that x ∈ K is
precisely the solid angle at the apex of K. Yet another view of solid angles is
that they are in fact volumes of spherical polytopes: the region of intersection
of a cone with a sphere. There is a theory here that parallels the Ehrhart
theory of Chapters 3 and 4, but which has some genuinely new ideas.

13.1 A New Discrete Volume Using Solid Angles

Suppose P ⊂ Rd is a convex rational d-polyhedron. The solid angle ωP (x)
of a point x (with respect to P) is a real number equal to the proportion of a
small ball centered at x that is contained in P. That is, we let Bϵ(x) denote
the ball of radius ϵ centered at x and deﬁne

ωP (x) := vol (Bϵ(x) ∩ P)
vol Bϵ(x)

for all positive ϵ suﬃciently small; this notion is depicted in Figure 13.1. We
note that when x /∈ P, ωP (x) = 0; when x ∈ P ◦, ωP (x) = 1; when x ∈ ∂P,

227

228 13 Solid Angles

0 < ωP (x) < 1. The solid angle of a face F of P is deﬁned by choosing a
point x in the relative interior F ◦ and setting ωP (F) = ωP (x).

Fig. 13.1 A solid angle.

v
 Example 13.1. We compute the solid angles of the faces belonging to the
standard 3-simplex ∆ = conv {(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)}. As we just
mentioned, a point interior to ∆ has solid angle 1. Every facet has solid angle
1
2 (and this remains true for every polytope).
The story gets interesting with the edges: here we are computing dihedral
angles. The dihedral angle of a 1-dimensional edge is deﬁned by the angle
between the outward-pointing normal to one of its deﬁning facets and the
inward-pointing normal to its other deﬁning facet.

Fig. 13.2 The simplex ∆
from Example 13.1.

A
 B

C

O
 Each of the edges OA, OB, and OC in Figure 13.2 has the same solid
angle 1
4 . Turning to the edge AB, we compute the angle between its deﬁning
facets as follows:

13.1 A New Discrete Volume Using Solid Angles 229

1
2π cos−1 ( 1
√3 (−1, −1, −1) · (0, 0, −1)) = 1
2π cos−1 ( 1
√3
 ) .

The edges AC and BC have the same solid angle by symmetry.
Finally, we compute the solid angle of the vertices: the origin has solid
angle 1
8 , and the other three vertices all have the same solid angle ω. With
Corollary 13.9 below (the Brianchon–Gram relation), we can compute this
angle via

0 = ∑

F ⊆P(−1)dim F ωP (F) = −1 + 4 · 1
2 − 3 · 1
4 − 3 · 1
2π cos−1 ( 1
√3
 ) + 1
8 + 3 · ω ,

which gives ω = 1
2π cos−1 ( 1√3
 ) − 1
8 . ⊓⊔

We now introduce another measure of discrete volume; namely, we let

AP (t) := ∑

m∈tP∩Zd ωtP (m) ,

the sum of the solid angles at all integer points in tP; recalling that ωP (x) = 0
if x /∈ P, we can also write

AP (t) = ∑

m∈Zd ωtP (m) .

This new discrete volume measure diﬀers in a substantial way from the Ehrhart
counting function LP (t). Namely, suppose P is a d-polytope that can be
written as the union of the polytopes P1 and P2 such that dim (P1 ∩ P2) < d,
that is, P1 and P2 are glued along a lower-dimensional subset. Then at each
lattice point m ∈ Z
d, we have ωP1 (m)+ωP2 (m) = ωP (m), and so the function
AP has an additive property:

AP (t) = AP1(t) + AP2(t) . (13.1)

In contrast, the Ehrhart counting functions satisfy

LP (t) = LP1(t) + LP2(t) − LP1∩P2 (t) .

On the other hand, we can transfer computational eﬀort from the Ehrhart
counting functions to the solid-angle sum and vice versa, with the use of the
following lemma.

Lemma 13.2. Let P be a polytope. Then

AP (t) = ∑

F ⊆P ωP (F) LF ◦ (t) .

230 13 Solid Angles

Proof. The dilated polytope tP is the disjoint union of its relative open faces
tF ◦ (Exercise 5.3), so that we can write

AP (t) = ∑

m∈Zd ωtP (m) = ∑

F ⊆P
 ∑

m∈Zd ωtP (m) 1tF ◦ (m) .

But ωtP (m) is constant on each relatively open face tF ◦, and we called this
constant ωP (F), whence

AP (t) = ∑

F ⊆P ωP (F) ∑

m∈Zd 1tF ◦ (m) = ∑

F ⊆P ωP (F) LF ◦ (t) . ⊓⊔

Thus AP (t) is a polynomial (respectively quasipolynomial) in t for an
integral (respectively rational) polytope P. We claim that Lemma 13.2 is in
fact useful in practice. To drive the point home, we illustrate this identity by
computing the solid-angle sum over all integer points of ∆ in Example 13.1.

Example 13.3. We continue the solid-angle computation for the 3-simplex
∆ = conv {(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)}. We recall from Section 2.3 that
L∆◦ = (t−1
3 ). The facets of ∆ are three standard triangles and one triangle
that appeared in the context of the Frobenius problem. All four facets have
the same interior Ehrhart polynomial (t−1
2 ). A similar phenomenon holds for
the edges of ∆: all six of them have the same interior Ehrhart polynomial
t − 1. These polynomials add up, by Lemma 13.2 and Example 13.1, to the
solid-angle sum

A∆(t) = (t − 1
3
 ) + 4 · 1
2
 (t − 1
2
 ) + (3 · 1
4 + 3 · 1
2π cos−1 ( 1
√3
 )) (t − 1)

+ 1
8 + 3 · ( 1
2π cos−1 ( 1
√3
 ) − 1
8
 )

= 1
6 t3 + ( 3
2π cos−1 ( 1
√3
 ) − 5
12
 ) t .

The magic cancellation of the even powers of this polynomial is not a coinci-
dence, as we will discover in Theorem 13.7. The curious reader may notice
that the coeﬃcient of t in this example is not a rational number, in stark
contrast with Ehrhart polynomials. ⊓⊔

The analogue of Ehrhart’s theorem (Theorem 3.23) in the world of solid
angles is as follows.

Theorem 13.4 (Macdonald’s theorem). Suppose P is a rational convex
d-polytope. Then AP is a quasipolynomial of degree d whose leading coeﬃcient
is vol P and whose period divides the denominator of P.

Proof. The denominator of a face F ⊂ P divides the denominator of P, and
hence so does the period of LF , by Ehrhart’s theorem (Theorem 3.23). By

13.2 Solid-Angle Generating Functions and a Brion-Type Theorem 231

Lemma 13.2, AP is a quasipolynomial with period dividing the denominator
of P. The leading term of AP equals the leading term of LP ◦ , which is vol P,
by Corollary 3.20 and its extension in Exercise 3.34. ⊓⊔

13.2 Solid-Angle Generating Functions and a
Brion-Type Theorem

By analogy with the integer-point transform of a polyhedron P ⊆ Rd, which
lists all lattice points in P, we form the solid-angle generating function

αP (z) := ∑

m∈P∩Zd ωP (m) zm.

Using the same reasoning as in (13.1) for AP , this function satisﬁes a nice
additivity relation. Namely, if the d-polyhedron P equals P1 ∪ P2, where
dim (P1 ∩ P2) < d, then
 αP (z) = αP1(z) + αP2(z) . (13.2)

The solid-angle generating function obeys the following reciprocity relation,
which parallels both the statement and proof of Theorem 4.3:

Theorem 13.5. Suppose K is a rational pointed d-cone with the origin as
apex, and v ∈ Rd. Then the solid-angle generating function αv+K(z) of the
pointed d-cone v + K is a rational function that satisﬁes

αv+K
 ( 1
z
 ) = (−1)d α−v+K (z) .

Proof. Because solid angles are additive by (13.2), it suﬃces to prove this
theorem for simplicial cones. The proof for this case proceeds along the same
lines as the proof of Theorem 4.2; the main geometric ingredient is Exercise 4.2.
We invite the reader to ﬁnish the proof (Exercise 13.6). ⊓⊔

The analogue of Brion’s theorem in terms of solid angles is as follows.

Theorem 13.6. Suppose P is a rational convex polytope. Then we have the
following identity of rational functions:

αP (z) = ∑

v a vertex of P αKv (z) .

Proof. As in the proof of Theorem 11.7, it suﬃces to prove Theorem 13.6 for
simplices. So let ∆ be a rational simplex. We write ∆ as the disjoint union of
its open faces and use Brion’s theorem for open polytopes (Exercise 11.9) on

232 13 Solid Angles

each face. That is, if we denote the vertex cone of F at vertex v by Kv(F),
then by a monomial version of Lemma 13.2,

α∆(z) = ∑

F ⊆∆ ω∆(F) σF ◦ (z)

= ∑

v a vertex of ∆ ω∆(v) zv + ∑

F ⊆∆
dim F >0
 ω∆(F) ∑

v a vertex of F σKv(F )◦ (z) ,

where we used Brion’s theorem for open polytopes (Exercise 11.9) in the
second step. By Exercise 13.7,
∑

F ⊆∆
dim F >0
 ω∆(F) ∑

v a vertex of F
σKv(F )◦ (z) = ∑

v a vertex of ∆
 ∑

F ⊆Kv
dim F >0

ωKv (F) σF ◦ (z) ,

and so

α∆(z) = ∑

v a vertex of ∆ ω∆(v) zv + ∑

v a vertex of ∆
 ∑

F ⊆Kv
dim F >0
 ωKv (F) σF ◦ (z)

= ∑

v a vertex of ∆
 ∑

F ⊆Kv ωKv (F) σF ◦ (z)

= ∑

v a vertex of ∆ αKv (z) . ⊓⊔

13.3 Solid-Angle Reciprocity and the Brianchon–Gram
Relations

With the help of Theorems 13.5 and 13.6, we can now prove the solid-angle
analogue of Ehrhart–Macdonald reciprocity (Theorem 4.1):

Theorem 13.7 (Macdonald’s reciprocity theorem). Suppose P is a ra-
tional convex polytope. Then the quasipolynomial AP satisﬁes

AP (−t) = (−1)dim P AP (t) .

Proof. We give the proof for an integral polytope P and invite the reader to
generalize it to the rational case. The solid-angle counting function of P can
be computed through the solid-angle generating function of tP:

AP (t) = αtP (1, 1, . . . , 1) = lim
z→1 αtP (z) .

By Theorem 13.6,

13.3 Solid-Angle Reciprocity and the Brianchon–Gram Relations 233

AP (t) = lim
z→1
 ∑

v a vertex of P αtKv (z) ,

where Kv is the tangent cone of P at the vertex v. We write Kv = v + K(v),
where K(v) := Kv − v is a rational cone with the origin as its apex. Then
tKv = tv + K(v), because a cone whose apex is the origin does not change
under dilation. Hence we obtain, with the help of Exercise 13.5,

AP (t) = lim
z→1
 ∑

v a vertex of P αtv+K(v)(z) = lim
z→1
 ∑

v a vertex of P ztvαK(v)(z) .

The rational functions αK(v)(z) on the right-hand side do not depend on t. If
we think of the sum over all vertices as one big rational function, to which we
apply L’Hˆopital’s rule to compute the limit as z → 1, this gives an alternative
proof that AP (t) is a polynomial, in line with our proof for the polynomiality
of LP (t) in Section 11.5. At the same time, this means that we can view the
identity AP (t) = lim
z→1
 ∑

v a vertex of P ztvαK(v)(z)

in a purely algebraic fashion: on the left-hand side, we have a polynomial
that makes sense for every complex t, and on the right-hand side, we have a
rational function of z, whose limit we compute, for example, by L’Hˆopital’s
rule. So the right-hand side, as a function of t, makes sense for every integer
t. Hence we have the algebraic relation, for integral t,

AP (−t) = lim
z→1
 ∑

v a vertex of P z−tvαK(v)(z) .

But now by Theorem 13.5, αK(v)(z) = (−1)
d αK(v) ( 1
z ), and so

AP (−t) = lim
z→1
 ∑

v a vertex of P z−tv(−1)d αK(v)
 ( 1
z
 )

= (−1)d lim
z→1
 ∑

v a vertex of P
 ( 1
z
 )tv αK(v)
 ( 1
z
 )

= (−1)d lim
z→1
 ∑

v a vertex of P αtv+K(v)
 ( 1
z
 )

= (−1)d lim
z→1 αtP
 ( 1
z
 )

= (−1)dAP (t) .

In the third step, we used Exercise 13.5 again.
This proves Theorem 13.7 for integral polytopes. The proof for rational
polytopes follows along the same lines; one deals with rational vertices in the

234 13 Solid Angles

same manner as in our second proof of Ehrhart’s theorem in Section 11.5. We
invite the reader to ﬁnish the details in Exercise 13.8. ⊓⊔

We remark that throughout the proof, we cannot simply take the limit
inside the ﬁnite sum over the vertices of P, since z = 1 is a pole of each
rational function αK(v). It is precisely the magic of Brion’s theorem that
makes these poles cancel each other, to yield AP (t).
If P is an integral polytope, then AP is a polynomial, and Theorem 13.7
tells us that AP is always even or odd:

AP (t) = cd td + cd−2t
d−2 + · · · + c0 .

We can say more.

Theorem 13.8. Suppose P is a rational convex polytope. Then AP (0) = 0.

This is a meaningful zero. We note that the constant term of AP is given by

AP (0) = ∑

F ⊆P ωP (F) LF ◦ (0) = ∑

F ⊆P ωP (F) (−1)dim F ,

by Lemma 13.2 and Ehrhart–Macdonald reciprocity (Theorem 4.1). Hence
Theorem 13.8 implies a classical and useful geometric identity:

Corollary 13.9 (Brianchon–Gram relation). For a rational convex poly-
tope P, ∑

F ⊆P(−1)dim F ωP (F) = 0 .

Example 13.10. Consider a triangle T in R2 with vertices v1, v2, v3 and
edges E1, E2, E3. The Brianchon–Gram relation tells us that for this triangle,

ωT (v1) + ωT (v2) + ωT (v3) − (ωT (E1) + ωT (E2) + ωT (E3)) + ωT (T ) = 0 .

Since the solid angles of the edges are all 1
2 and ωT (T ) = 1, we recover our
friendly high-school identity the sum of the angles in a triangle is 180 degrees:

ωT (v1) + ωT (v2) + ωT (v3) = 1
2 .

Thus the Brianchon–Gram relation is the extension of this well-known fact to
every dimension and every convex polytope. ⊓⊔

Proof of Theorem 13.8. It suﬃces to prove A∆(0) = 0 for a rational simplex
∆, since solid angles of a triangulation simply add, by (13.1). Theorem 13.7
gives A∆(0) = 0 if dim ∆ is odd.
So now suppose ∆ is a rational d-simplex, where d is even, with vertices
v1, v2, . . . , vd+1. Let P(n) be the (d + 1)-dimensional pyramid that we obtain

13.3 Solid-Angle Reciprocity and the Brianchon–Gram Relations 235

Fig. 13.3 The pyramid
P(n) for a triangle ∆.

n
 x

z

y
 by taking the convex hull of (v1, 0) , (v2, 0) , . . . , (vd+1, 0), and (0, 0, . . . , 0, n),
where n is a positive integer (see Figure 13.3). Note that since d + 1 is odd,

AP(n)(0) = ∑

F (n)⊆P(n)
(−1)dim F (n) ωP(n)(F(n)) = 0 .

We will conclude from this identity that ∑

F ⊆∆(−1)dim F ω∆(F) = 0, which
implies that A∆(0) = 0. To this end, we consider two types of faces of P(n):

(a) those that are also faces of ∆;
(b) those that are not contained in ∆.

We begin with the latter: Aside from the vertex (0, 0, . . . , 0, n), every face
F(n) of P(n) that is not a face of ∆ is the pyramid over a face G of ∆; let’s
denote this pyramid by Pyr (G, n). Further, as n grows, the solid angle of
Pyr (G, n) (in P(n)) approaches the solid angle of G (in ∆):

lim
n→∞ ωP(n) (Pyr (G, n)) = ω∆ (G) ,

since we are forming ∆ × [0, ∞) in the limit. On the other hand, a face
F(n) = G of P(n) that is also a face of ∆ obeys the following limit behavior:

lim
n→∞ ωP(n) (F(n)) = 1
2 ω∆ (G) .

The only face of P(n) that we still have to account for is the vertex v :=
(0, 0, . . . , 0, n). Hence

0 = ∑

F (n)⊆P(n)
(−1)
dim F (n)ωP(n)(F(n))

= ωP(n)(v) + ∑

G⊆∆(−1)dim G+1ωP(n) (Pyr (G, n)) + ∑

G⊆∆(−1)dim GωP(n) (G) .

236 13 Solid Angles

Now we take the limit as n → ∞ on both sides; note that limn→∞ ωP(n)(v) =
0, so that we obtain

0 = ∑

G⊆∆(−1)dim G+1ω∆ (G) + ∑

G⊆∆
(−1)
dim G 1
2 ω∆ (G)

= 1
2
 ∑

G⊆∆(−1)dim G+1ω∆ (G) ,

and so A∆(0) = ∑

G⊆∆(−1)dim Gω∆(G) = 0 . ⊓⊔

The combination of Theorems 13.7 and 13.8 implies that summing solid
angles in a polygon is equivalent to computing its area:

Corollary 13.11. Suppose P is a 2-dimensional integral polytope with area a.
Then AP (t) = a t
2.

13.4 The Generating Function of Macdonald’s
Solid-Angle Polynomials

We conclude this chapter with the study of the solid-angle analogue of Ehrhart
series. Given an integral polytope P, we deﬁne the solid-angle series of P as
the generating function of the solid-angle polynomial, encoding the solid-angle
sum over all dilates of P simultaneously:

SolidP (z) := ∑

t≥0 AP (t) zt.

The following theorem is the solid-angle analogue to Theorems 3.12 and 4.4,
with the added bonus that we get the palindromicity of the numerator of
SolidP for free.

Theorem 13.12. Suppose P is an integral d-polytope. Then SolidP is a ra-
tional function of the form

SolidP (z) = adzd + ad−1zd−1 + · · · + a1z

(1 − z)
d+1 .

Furthermore, we have the identity

SolidP
 ( 1
z
 ) = (−1)
d+1 SolidP (z),

or equivalently, ak = ad+1−k for 1 ≤ k ≤ d
2 .

Notes 237

Proof. The form of the rational function SolidP follows, by Lemma 3.9, from
the fact that AP is a polynomial. The palindromicity of a1, a2, . . . , ad is
equivalent to the relation

SolidP
 ( 1
z
 ) = (−1)d+1 SolidP (z) ,

which, in turn, follows from Theorem 13.7:

SolidP (z) = ∑

t≥0 AP (t) zt = ∑

t≥0(−1)
dAP (−t) zt = (−1)
d ∑

t≤0 AP (t) z−t.

Now we use Exercise 4.7:

(−1)
d ∑

t≤0 AP (t) z−t = (−1)
d+1 ∑

t≥1 AP (t) z−t = (−1)d+1 SolidP
 ( 1
z
 ) .

In the last step, we used the fact that AP (0) = 0 (Theorem 13.8). ⊓⊔

Notes

1. I. G. Macdonald inaugurated the systematic study of solid-angle sums
in integral polytopes. The fundamental Theorems 13.4, 13.7, and 13.8 can
be found in his 1971 paper [167]. The proof of Theorem 13.7 we give here
follows [39].

2. The Brianchon–Gram relation (Corollary 13.9) is the solid-angle analogue
of the Euler relation for face numbers (Theorem 5.2). The 2-dimensional case
discussed in Example 13.10 is ancient; it was most certainly known to Euclid.
The 3-dimensional case of Corollary 13.9 was discovered by Charles Julien
Brianchon in 1837 and—as far as we know—was independently re-proved
by Jørgen Gram in 1874 [122]. It is not clear who ﬁrst proved the general
d-dimensional case of Corollary 13.9. The oldest proofs we could ﬁnd were
from the 1960s, by Branko Gr¨unbaum [127], Micha A. Perles, and Geoﬀrey C.
Shephard [190, 219].

3. Theorem 13.5 is a particular case of a reciprocity relation for simple
lattice-invariant valuations due to Peter McMullen [173], who also proved
a parallel extension of Ehrhart–Macdonald reciprocity to general lattice-
invariant valuations. There is a current resurgence of activity on solid angles;
see, for example, [46, 77, 104, 116, 205].

238 13 Solid Angles

Exercises

13.1. Compute AP (t), where P is the regular tetrahedron with vertices
(0, 0, 0), (1, 1, 0), (1, 0, 1), and (0, 1, 1) (see Exercise 2.13).

13.2. Compute AP (t), where P is the rational triangle with vertices (0, 0),( 1
2 , 1
2 ), and (1, 0).

13.3. For a simplex ∆, let S(∆) denote the sum of the solid angles at the
vertices of ∆.

(a) Prove that S(∆) ≤ 1
2 .
(b) Construct a sequence ∆n of simplices in a ﬁxed dimension, such that
limn→∞ S(∆n) = 1
2 .

13.4. Let Z be a d-dimensional integral zonotope. Show that AZ (t) =
vol(Z) td.

13.5. ♣ Let K be a rational d-cone and let m ∈ Z
d. By analogy with Exer-
cise 3.9, show that αm+K(z) = zm αK(z).

13.6. ♣ Complete the proof of Theorem 13.5: For a rational pointed d-cone
K, αK(z) is a rational function that satisﬁes

αK
 ( 1
z
 ) = (−1)
d αK (z) .

13.7. ♣ Suppose ∆ is a rational simplex. Prove that
∑

F ⊆∆
dim F >0
 ω∆(F) ∑

v a vertex of F
σKv(F )◦ (z) = ∑

v a vertex of ∆
 ∑

F ⊆Kv
dim F >0

ωKv (F) σF ◦ (z) .

13.8. ♣ Provide the details of the proof of Theorem 13.7 for rational polytopes:
Prove that if P is a rational convex polytope, then the quasipolynomial AP
satisﬁes AP (−t) = (−1)dim P AP (t) .

13.9. Recall from Exercise 3.2 that to a permutation π ∈ Sd on d elements,
we can associate the simplex

∆π := conv {0, eπ(1), eπ(1) + eπ(2), . . . , eπ(1) + eπ(2) + · · · + eπ(d)} .

Prove that for all π ∈ Sn, A∆π (t) = 1
d! td.

13.10. Give a direct proof of Corollary 13.11, e.g., using Pick’s theorem
(Theorem 2.8).

13.11. State and prove the analogue of Theorem 13.12 for rational polytopes.

Open Problems 239

Open Problems

13.12. Study the roots of solid-angle polynomials.

13.13. Classify all polytopes that have only rational solid angles at their
vertices.

13.14. Classify all rational polytopes P such that AP (t) = vol(P) t
d.

13.15. Which integral polytopes P have an integral solid-angle sum? More
generally, which integral polytopes P have solid-angle polynomials AP (t) ∈
Q[t]? That is, for which integral polytopes P are all the coeﬃcients of AP (t)
rational? (For one such class of polytopes, see [124].)

Chapter 14
A Discrete Version of Green’s
Theorem Using Elliptic Functions

The shortest route between two truths in the real domain passes through the complex do-
main.

Jacques Salomon Hadamard (1865–1963)

We now allow ourselves the luxury of using basic complex analysis. In par-
ticular, we assume that the reader is familiar with contour integration and
the residue theorem. We may view the residue theorem as yet another result
that intimately connects the continuous and the discrete: it transforms a
continuous integral into a discrete sum of residues.
Using the Weierstraß ℘- and ζ-functions, we show here that Pick’s theorem
is a discrete version of Green’s theorem in the plane. As a bonus, we also
obtain an integral formula (Theorem 14.5 below) for the discrepancy between
the area enclosed by a general curve C and the number of integer points
contained in C.

14.1 The Residue Theorem

We begin this chapter by reviewing a few concepts from complex analysis.
Suppose the complex-valued function f has an isolated singularity w ∈ G;
that is, there is an open set G ⊂ C such that f is analytic on G \ {w}. Then
f can be expressed locally by the Laurent series

f (z) = ∑

n∈Z cn (z − w)
n ,

valid for all z ∈ G \ {w}; here cn ∈ C. The coeﬃcient c−1 is called the
residue of f at w; we will denote it by Res(z = w). The reason to give c−1

241

242 14 A Discrete Version of Green’s Theorem Using Elliptic Functions

a special name can be found in the following theorem. We call a function
meromorphic if it is analytic in C with the exception of isolated poles.

Theorem 14.1 (Residue theorem). Suppose f is meromorphic and C is
a positively oriented, piecewise diﬀerentiable simple closed curve that does not
pass through any pole of f . Then
∫

C f = 2πi ∑

w Res(z = w) ,

where the sum is taken over all singularities w inside C. ⊓⊔

If f is a rational function, Theorem 14.1 gives the same result as a partial
fraction expansion of f . We illustrate this philosophy by returning to the
elementary beginnings of Chapter 1.

Example 14.2. Recall our constant-term identity for the restricted partition
function for A = {a1, a2, . . . , ad} in Chapter 1:

pA(n) = const ( 1
(1 − za1 ) (1 − za2) · · · (1 − zad ) zn
 ) .

Computing the constant term of the Laurent series of 1
(1−za1 )···(1−zad )zn
expanded about z = 0 is naturally equivalent to “shifting” this function by
one exponent and computing the residue at z = 0 of the function

f (z) := 1
(1 − za1) (1 − za2) · · · (1 − zad ) zn+1 .

Now let Cr be a positively oriented circle of radius r > 1, centered at the
origin. The residue Res(z = 0) = pA(n) is one of the residues that are picked
up by the integral

1
2πi
 ∫

Cr f = Res(z = 0) + ∑

w Res(z = w) ,

where the sum is over all nonzero poles w of f that lie inside Cr. These
poles are at the a
th
1 , a
th
2 , . . . , ath
d roots of unity. Moreover, with the help of
Exercise 14.1, we can show that

0 = lim
r→∞ 1
2πi
 ∫

Cr f

= lim
r→∞
 (

Res(z = 0) + ∑

w Res(z = w)

)

= Res(z = 0) + ∑

w Res(z = w) ,

14.2 The Weierstraß ℘- and ζ-Functions 243

where the sum extends over all a
th
1 , a
th
2 , . . . , ath
d roots of unity. In other words,

pA(n) = Res(z = 0) = − ∑

w Res(z = w) .

To obtain the restricted partition function pA, it remains to compute the
residues at the roots of unity, and we invite the reader to realize that this
computation is equivalent to the partial fraction expansion of Chapter 1
(Exercise 14.2). ⊓⊔

Analogous residue computations could replace any of the constant-term
calculations that we performed in the earlier chapters.

14.2 The Weierstraß ℘- and ζ-Functions

The main character in our play is the Weierstraß ζ-function, deﬁned by

ζ(z) = 1
z + ∑

(m,n)∈Z2\(0,0)
 ( 1
z − (m + ni) + 1
m + ni + z

(m + ni)2
 )
 . (14.1)

This inﬁnite sum converges uniformly on compact subsets of the lattice-
punctured plane C \ Z
2 (Exercise 14.5), and hence forms a meromorphic
function of z.
The Weierstraß ζ-function possesses the following salient properties, which
follow immediately from (14.1):

(1) ζ has a simple pole at every integer point m + ni and is analytic elsewhere.
(2) The residue of ζ at each integer point m + ni equals 1.

We can easily check (Exercise 14.6) that

℘(z) := −ζ ′(z) = 1
z2 + ∑

(m,n)∈Z2\(0,0)
 ( 1

(z − (m + ni))2 − 1

(m + ni)
2
 )
 ,

(14.2)
the Weierstraß ℘-function. The ℘-function has a pole of order 2 at each
integer point m + ni and is analytic elsewhere, but has residue equal to zero at
each integer point m + ni. However, ℘ possesses a very pleasant property that
ζ does not: ℘ is doubly periodic on C. We may state this more concretely:

Lemma 14.3. ℘(z + 1) = ℘(z + i) = ℘(z) .

Proof. We ﬁrst invite the reader to prove the following two properties of ℘
′

(Exercises 14.7 and 14.8):

244 14 A Discrete Version of Green’s Theorem Using Elliptic Functions

℘
′ (z + 1) = ℘
′(z) , (14.3)
∫ z1

z0 ℘
′ (z) dz is path-independent. (14.4)

By (14.3), d
dz (℘ (z + 1) − ℘(z)) = ℘
′ (z + 1) − ℘
′(z) = 0 ,

so ℘ (z + 1) − ℘(z) = c for some constant c. On the other hand, ℘ is an even
function (Exercise 14.9), and so z = − 1
2 gives us

c = ℘ ( 1
2 ) − ℘ (− 1
2 ) = 0 .

This shows that ℘ (z + 1) = ℘(z) for all z ∈ C \ Z
2. An analogous proof, which
we invite the reader to construct in Exercise 14.10, shows that ℘ (z + i) = ℘(z).
⊓⊔

Lemma 14.3 implies that ℘(z + m + ni) = ℘(z) for all m, n ∈ Z. The
following lemma shows that the Weierstraß ζ-function is only a conjugate-
analytic term away from being doubly periodic.

Lemma 14.4. There is a constant α such that the function ζ(z) + αz is
doubly periodic with periods 1 and i.

Proof. We begin with w = m + ni:

ζ (z + m + ni) − ζ(z) = − ∫ m+ni

w=0 ℘ (z + w) dw , (14.5)

by deﬁnition of ℘(z) = −ζ ′(z). To make sure that (14.5) makes sense, we
should also check that the deﬁnite integral in (14.5) is path-independent
(Exercise 14.11).
Due to the double periodicity of ℘,

∫ m+ni

w=0 ℘ (z + w) dw = m ∫ 1

0 ℘ (z + t) dt + ni ∫ 1

0 ℘ (z + it) dt

= mα(z) + niβ(z) ,

where
 α(z) := ∫ 1

0 ℘ (z + t) dt and β(z) := ∫ 1

0 ℘ (z + it) dt .

Now we observe that α (z + x0) = α(z) for every x0 ∈ R, so that α (x + iy)
depends only on y. Similarly, β (x + iy) depends only on x. But

ζ (z + m + in) − ζ(z) = − (mα(y) + inβ(x))

14.3 A Contour-Integral Extension of Pick’s Theorem 245

must be analytic for all z ∈ C \ Z
2. If we now set m = 0, we conclude that
β(x) must be analytic in C \ Z
2, so that β(x) must be a constant by the
Cauchy–Riemann equations for analytic functions. Similarly, setting n = 0
implies that α(y) is constant. Thus

ζ (z + m + in) − ζ(z) = − (mα + inβ)

with constants α and β. Returning to the Weierstraß ℘-function, we can
integrate the identity (Exercise 14.12)

℘(iz) = −℘(z) (14.6)

to obtain the relationship β = −α, since

β = ∫ 1

0 ℘ (z + it) dt = ∫ 1

0 ℘ (it) dt = − ∫ 1

0 ℘ (t) dt = −α .

To summarize,

ζ (z + m + in) − ζ(z) = −mα + inα = −α (z + m + in − z) ,

so that ζ(z) + αz is doubly periodic. ⊓⊔

14.3 A Contour-Integral Extension of Pick’s Theorem

For the remainder of this chapter, let C be any piecewise-diﬀerentiable simple
closed curve in the plane, with a counterclockwise parameterization. We let
D denote the region that C contains in its interior.

Theorem 14.5. Let C avoid every integer point, that is, C ∩ Z
2 = ∅. Let
I denote the number of integer points interior to C, and A the area of the
region D enclosed by the curve C. Then

1
2πi
 ∫

C (ζ(z) − πz) dz = I − A .

Proof. We have
∫

C (ζ(z) + αz) dz = ∫

C ζ(z) dz + α ∫

C (x − iy) (dx + idy) ,

where α is as in Lemma 14.4. By Theorem 14.1, ∫
C ζ(z) dz is equal to the
sum of the residues of ζ at all of its interior poles. There are I such poles,
and each pole of ζ has residue 1. Thus

246 14 A Discrete Version of Green’s Theorem Using Elliptic Functions

1
2πi
 ∫

C ζ(z) dz = I . (14.7)

On the other hand, Green’s theorem tells us that
∫

C (x − iy) (dx + idy) = ∫

C (x − iy) dx + (y + ix) dy

= ∫

D
 ∂
∂x (y + ix) − ∂
∂y (x − iy)

= ∫ ∫

D 2i

= 2iA .

Returning to (14.7), we get
∫

C (ζ(z) + αz) dz = 2πiI + α (2iA) . (14.8)

We have only to show that α = −π. Consider the particular curve C that is
a square path, centered at the origin, traversing the origin counterclockwise
and bounding a square of area 1. Thus I = 1 for this path. Since ζ(z) + αz
is doubly periodic by Lemma 14.4, the integral in (14.8) vanishes. We can
conclude that 0 = 2πi · 1 + α (2i · 1) ,

so that α = −π. ⊓⊔

Notice that Theorem 14.5 has given us information about the Weierstraß
ζ-function, namely that α = −π.
This chapter oﬀers a detour into an inﬁnite landscape of discrete results
that meet their continuous counterparts. Equipped with the modest tools
oﬀered in this book, we hope that we have motivated the reader to explore
this landscape further.

Notes

1. The Weierstraß ℘-function, named after Karl Theodor Wilhelm Weier-
straß (1815–1897),1 can be extended to every 2-dimensional lattice L =
{kw1 + jw2 : k, j ∈ Z} for some w1, w2 ∈ C that are linearly independent
over R:
 ℘L(z) = 1
z2 + ∑

m∈L\{0}
 ( 1

(z − m)
2 − 1
m2
 )
 .

1 For more information about Weierstraß, see
http://www-history.mcs.st-andrews.ac.uk/Biographies/Weierstrass.html.

Exercises 247

The Weierstraß ℘L-function and its derivative ℘
′
L satisfy a polynomial rela-
tionship, namely, (℘
′
L)2 = 4 (℘L)3 − g2 ℘L − g3 for some constants g2 and g3
that depend on L. This is the beginning of a wonderful friendship between
complex analysis and elliptic curves.

2. Theorem 14.5 appeared in [106]. There it is also shown that one can recover
Pick’s theorem (Theorem 2.8) from Theorem 14.5.

Exercises

14.1. ♣ Show that for positive integers a1, ad, . . . , ad, n,

lim
r→∞
 ∫

Cr
 1
(1 − za1) · · · (1 − zad ) zn+1 = 0 .

This computation shows that the integrand above “has no pole at inﬁnity.”

14.2. ♣ Compute the residues at the nontrivial roots of unity of

f (z) = 1
(1 − za1 ) · · · (1 − zad ) zn+1 .

For simplicity, you may assume that a1, a2, . . . , ad are pairwise relatively
prime.

14.3. This exercise yields a proof of (8.4), namely, that the Bernoulli–Barnes
polynomials BA
k (x), deﬁned in Chapter 8 through the generating function

zdexz

(ea1z − 1) (ea2z − 1) · · · (eadz − 1) = ∑

k≥0 BA
k (x) zk

k! ,

allow us to express the polynomial part of pA(n) as

polyA(n) = (−1)d−1

(d − 1)! BA
d−1(−n) .

As above, we let
 f (z) = 1
(1 − za1 ) · · · (1 − zad ) zn+1

and assume that a1, a2, . . . , ad are pairwise relatively prime.

(a) Show that polyA(n) equals the negative of the residue of f (z) at z = 1.
(b) Deduce the above formula for polyA(n) in terms of a Bernoulli–Barnes
polynomial. (Hint: convince yourself that the residue of f (z) at z = 1
equals the residue of ezf (ez) at z = 0.)

248 14 A Discrete Version of Green’s Theorem Using Elliptic Functions

14.4. Give an integral version of Theorem 2.13.

14.5. ♣ Show that

ζ(z) = 1
z + ∑

(m,n)∈Z2\(0,0)
 ( 1
z − (m + ni) + 1
m + ni + z

(m + ni)2
 )

converges absolutely for z belonging to compact subsets of C \ Z
2.

14.6. ♣ Prove (14.2), that is,

ζ ′(z) = − 1
z2 − ∑

(m,n)∈Z2\(0,0)
 ( 1

(z − (m + ni))2 − 1

(m + ni)
2
 )
 .

14.7. ♣ Prove (14.3), that is, show that ℘
′ (z + 1) = ℘
′(z).

14.8. ♣ Prove (14.4), that is, show that for all z0, z1 ∈ C \ Z
2, the integral∫ z1
z0 ℘
′(w) dw is path-independent.

14.9. ♣ Show that ℘ is even, that is, ℘ (−z) = ℘(z).

14.10. ♣ Finish the proof of Lemma 14.3 by showing that ℘ (z + i) = ℘(z).

14.11. ♣ Prove that the integral in (14.5),

ζ (z + m + ni) − ζ(z) = − ∫ w=m+ni

w=0 ℘ (z + w) dw ,

is path-independent.

14.12. ♣ Prove (14.6), that is, ℘(iz) = −℘(z).

Open Problems

14.13. Can we get even more information about the Weierstraß ℘- and ζ-
functions using more detailed knowledge of the discrepancy between I and A
for special curves C?

14.14. Find a complex-analytic extension of Theorem 14.5 to higher dimen-
sions.

Appendix A
Vertex and Hyperplane Descriptions of
Polytopes

Everything should be made as simple as possible, but not simpler.

Albert Einstein

In this appendix, we prove that every convex polytope has both a vertex and
a hyperplane description. This appendix owes everything to G¨unter Ziegler’s
beautiful exposition in [259]; in fact, these pages contain merely a few cherries
picked from [259, Lecture 1].
As in Chapter 3, it is easier to move to the world of cones. To be as concrete
as possible, let’s call K ⊆ Rd an h-cone if

K = {x ∈ Rd : A x ≤ 0
}

for some A ∈ Rm×d; in this case, K is given as the intersection of m half-spaces
determined by the rows of A. We use the notation K = hcone(A).
On the other hand, we call K ⊆ Rd a v-cone if

K = {B y : y ≥ 0}

for some B ∈ Rd×n, that is, K is a pointed cone with the column vectors of
B as generators. In this case, we use the notation K = vcone(B).
Note that according to our deﬁnitions, every h-cone and every v-cone
contains the origin in its apex. We will prove that every h-cone is a v-cone
and vice versa. More precisely:

Theorem A.1. For every A ∈ Rm×d, there exists B ∈ Rd×n (for some n)
such that hcone(A) = vcone(B). Conversely, for every B ∈ Rd×n, there exists
A ∈ Rm×d (for some m) such that vcone(B) = hcone(A).

We will prove the two halves of Theorem A.1 in Sections A.1 and A.2. For
now, let’s record that Theorem A.1 implies our goal, that is, the equivalence
of the vertex and half-space description of a polytope:
 249

250 Appendix A: Vertex and Hyperplane Descriptions of Polytopes

Corollary A.2. If P is the convex hull of ﬁnitely many points in Rd, then
P is the intersection of ﬁnitely many half-spaces in Rd. Conversely, if P is
given as the bounded intersection of ﬁnitely many half-spaces in Rd, then P is
the convex hull of ﬁnitely many points in Rd.

Proof. If P = conv {v1, v2, . . . , vn} for some v1, v2, . . . , vn ∈ Rd, then coning
over P (as deﬁned in Chapter 3) gives

cone(P) = vcone ( v1 v2 . . . vn
1 1 1
 ) .

By Theorem A.1, we can ﬁnd a matrix (A, b) ∈ Rm×(d+1) such that

cone(P) = hcone(A, b) = {x ∈ Rd+1 : (A, b) x ≤ 0} .

We recover the polytope P on setting xd+1 = 1, that is,

P = {x ∈ Rd : Ax ≤ −b
} ,

which is a hyperplane description of P.
These steps can be reversed: Suppose the polytope P is given as

P = {x ∈ Rd : Ax ≤ −b
}

for some A ∈ Rm×d and b ∈ Rm. Then P can be obtained from

hcone(A, b) = {
x ∈ Rd+1 : (A, b) x ≤ 0
}

by setting xd+1 = 1. By Theorem A.1, we can construct a matrix B ∈ R(d+1)×n

such that hcone(A, b) = vcone(B) .

We may normalize the generators of vcone(B), that is, the columns of B, such
that they all have their (d + 1)st variable equal to 1:

B = ( v1 v2 . . . vn
1 1 1
 ) .

Since P can be recovered from vcone(B) by setting xd+1 = 1, we conclude
that P = conv {v1, v2, . . . , vn}. ⊓⊔

A.1 Every h-Cone Is a v-Cone

Suppose K = hcone(A) = {
x ∈ Rd : Ax ≤ 0
}

A.1 Every h-Cone Is a v-Cone 251

for some A ∈ Rm×d. We introduce an auxiliary m-dimensional variable y and
write
 K = {(x
y
) ∈ Rd+m : A x ≤ y} ∩ {(x
y
) ∈ Rd+m : y = 0
} . (A.1)

(Strictly speaking, this is K lifted into a d-dimensional subspace of Rd+m.)
Our goal in this section is to prove the following two lemmas.

Lemma A.3. The h-cone {(x
y) ∈ Rd+m : A x ≤ y} is a v-cone.

Lemma A.4. If K ⊆ Rd is a v-cone, then so is K ∩ {x ∈ Rd : xk = 0
}
, for
every k.

The ﬁrst half of Theorem A.1 follows with these two lemmas, since we can
start with (A.1) and intersect with one hyperplane yk = 0 at a time.

Proof of Lemma A.3. We begin by noting that

K = {(x
y
) ∈ Rd+m : A x ≤ y}

= {(x
y
) ∈ Rd+m : (A, −I) (x
y
) ≤ 0}

is an h-cone; here I represents the m × m identity matrix. Let’s denote the
kth unit vector by ek. Then we can decompose

(x
y
) =
 d∑

j=1 xj
( ej
A ej
) +
 m∑

k=1 (yk − (A x)k) ( 0
ek
)

=
 d∑

j=1 |xj| sign (xj) ( ej
A ej
) +
 m∑

k=1 (yk − (A x)k) ( 0
ek
) .

Note that if (x
y) ∈ K, then yk − (A x)k ≥ 0 for all k, and so (x
y) can be written
as a nonnegative linear combination of the vectors sign (xj) ( ej
A ej), 1 ≤ j ≤ d,

and ( 0
ek), 1 ≤ k ≤ m. But this means that K is a v-cone. ⊓⊔

Proof of Lemma A.4. Suppose K = vcone(B), where B has the column vec-
tors b1, b2, . . . , bn ∈ Rd; that is, b1, b2, . . . , bn are the generators of K. Fix
k ≤ d and construct a new matrix Bk whose column vectors are all the bj for
which bjk = 0 together with the combinations bikbj − bjkbi whenever bik > 0
and bjk < 0. We claim that

K ∩ {x ∈ Rd : xk = 0
} = vcone (Bk) .

252 Appendix A: Vertex and Hyperplane Descriptions of Polytopes

Every x ∈ vcone (Bk) satisﬁes xk = 0 by construction of Bk, and so
vcone (Bk) ⊆ K ∩ {
x ∈ Rd : xk = 0
} follows immediately. We need to do
some more work to prove the reverse containment.
Suppose x ∈ K ∩ {
x ∈ Rd : xk = 0
}, that is, x = λ1b1 + λ2b2 + · · · + λnbn
for some λ1, λ2, . . . , λn ≥ 0 and xk = λ1b1k + λ2b2k + · · · + λnbnk = 0. This
allows us to deﬁne
 Λ = ∑

i: bik>0 λibik = − ∑

j: bjk<0 λjbjk .

Note that Λ ≥ 0. Now consider the decomposition

x = ∑

j: bjk=0 λjbj + ∑

i: bik>0 λibi + ∑

j: bjk<0 λjbj . (A.2)

If Λ = 0, then λibik = 0 for all i such that bik > 0, and so λi = 0 for those i.
Similarly, λj = 0 for all j such that bjk < 0. Thus we conclude from Λ = 0
that x = ∑

j: bjk=0 λjbj ∈ vcone (Bk) .

Now assume Λ > 0. Then we can expand the decomposition (A.2) into

x = ∑

j: bjk=0 λjbj + 1
Λ
 

− ∑

j: bjk<0 λjbjk



 ( ∑

i: bik>0 λibi
)

+ 1
Λ
 ( ∑

i: bik>0 λibik
) 

 ∑

j: bjk<0 λjbj




= ∑

j: bjk=0 λjbj + 1
Λ
 ∑

i: bik>0
j: bjk<0
 λiλj (bikbj − bjkbi) ,

which is by construction in vcone (Bk). ⊓⊔

A.2 Every v-Cone Is an h-Cone

Suppose K = vcone(B) = {B y : y ≥ 0}

for some B ∈ Rd×n. Then K is the projection of
{(x
y
) ∈ Rd+n : y ≥ 0, x = B y} (A.3)

A.2 Every v-Cone Is an h-Cone 253

to the subspace {(x
y) ∈ Rd+n : y = 0
}
. The constraints for (A.3) can be
written as
 y ≥ 0 and (I, −B) (x
y
) = 0 .

Thus the set (A.3) is an h-cone, for which we can project one component of
y at a time to obtain K. This means that it suﬃces to prove the following
lemma to ﬁnish the second half of Theorem A.1.

Lemma A.5. If K is an h-cone, then the projection {x − xkek : x ∈ K} is
also an h-cone, for every k.

Proof. Suppose K = hcone(A) for some A ∈ Rm×d. Fix k and consider

Pk = {x + λek : x ∈ K, λ ∈ R} .

The projection we are after can be constructed from this set as

{x − xkek : x ∈ K} = Pk ∩ {x ∈ Rd : xk = 0
} ,

so that it suﬃces to prove that Pk is an h-cone.
Suppose a1, a2, . . . , am are the row vectors of A. We construct a new matrix
Ak whose row vectors are all aj for which ajk = 0, and the combinations
aikaj − ajkai whenever aik > 0 and ajk < 0. We claim that Pk = hcone (Ak).
If x ∈ K, then A x ≤ 0, which implies Ak x ≤ 0 because each row of Ak
is a nonnegative linear combination of rows of A; that is, K ⊆ hcone (Ak).
However, the kth component of Ak is zero by construction, and so K ⊆
hcone (Ak) implies Pk ⊆ hcone (Ak).
Conversely, suppose x ∈ hcone (Ak). We need to ﬁnd λ ∈ R such that
A (x − λek) ≤ 0, that is,

a11x1 + · · · + a1k (xk − λ) + · · · + a1dxd ≤ 0,
...

am1x1 + · · · + amk (xk − λ) + · · · + amdxd ≤ 0 .

The jth constraint is aj · x − ajkλ ≤ 0, that is, aj · x ≤ ajkλ. This gives the
following conditions on λ:

λ ≥ ai · x
aik if aik > 0 ,

λ ≤ aj · x
ajk if ajk < 0 .

Such a λ exists, because if aik > 0 and ajk < 0, then (since x ∈ hcone (Ak))

(aikaj − ajkai) · x ≤ 0 ,

254 Appendix A: Vertex and Hyperplane Descriptions of Polytopes

which is equivalent to ai · x
aik ≤ aj · x
ajk .

Thus we can ﬁnd λ that satisﬁes

ai · x
aik ≤ λ ≤ aj · x
ajk ,

which proves hcone (Ak) ⊆ Pk. ⊓⊔

Hints for ♣ Exercises

Well here’s another clue for you all.

John Lennon & Paul McCartney (“Glass Onion,” The White Album)

Chapter 1

1.1 Set up the partial fraction expansion as

z
1 − z − z2 = A

1 − 1+
√5
2 z + B

1 − 1−
√5
2 z

and clear denominators to compute A and B; one can do so, for example, by
specializing z.

1.2 Multiply out (1 − z) (1 + z + z2 + · · · + zn). For the inﬁnite sum, note
that limk→∞ zk = 0 if |z| < 1.

1.3 Start with the observation that there are ⌊x⌋ + 1 lattice points in the
interval [0, x].

1.4 (i) & (j) Write n = qm + r for some integers q, r such that 0 ≤ r < m.
Distinguish the cases r = 0 and r > 0.

1.9 Use the fact that for m and n relatively prime and a ∈ Z, there exists
b ∈ Z (which is unique modulo n) such that mb ≡ a (mod n). For the second
equality of sets, think about the case a = 0.

1.12 First translate the line segment to the origin and explain why this
translation leaves the integer-point enumeration invariant. For the case (a, b) =
(0, 0), ﬁrst study the problem under the restriction that gcd (c, d) = 1.

1.17 Given a triangle T with vertices on the integer lattice, consider the
parallelogram P formed by two ﬁxed edges of T . Use integral translates of

255

256 Hints for ♣ Exercises

P to tile the plane R2. Conclude from this tiling that P contains only its
vertices as lattice points if and only if the area of P is 1.

1.20 Given an integer b, the Euclidean algorithm asserts the existence
of m1, m2, . . . , md ∈ Z such that b can be represented as b = m1a1 +
m2a2 + · · · + mdad. Convince yourself that we can demand that in this
representation, 0 ≤ m2, m3, . . . , md < a1. Conclude that all integers beyond
(a1 − 1) (a2 + a3 + · · · + ad) are representable in terms of a1, a2, . . . , ad. (This
argument can be reﬁned to yield another proof of Theorem 1.2.)

1.21 Use the setup

f (z) = A1
z + A2
z2 + · · · + An
zn + B1
z − 1 + B2
(z − 1)2 +
 a−1∑

k=1
 Ck
z − ξk
a +
 b−1∑

j=1
 Dj
z − ξj
b .

To compute Ck, multiply both sides by (z − ξk
a ) and calculate the limit as
z → ξk
a . The coeﬃcients Dj can be computed in a similar fashion.

1.22 Use Exercise 1.9 (with m = b−1) on the left-hand side of the equation.

1.24 Suppose a > b. The integer a + b certainly has a representation in terms
of a and b, namely, 1 · a + 1 · b. Think about how the coeﬃcient of b would
change if we changed the coeﬃcient of a.

1.31 Use the partial fraction setup (1.11), multiply both sides by (z − ξk
a1),
and take the limit as z → ξk
a1 .

1.33 Convince yourself of the generating-function setup

∑

n≥1 p◦
A(n) zn = ( za1

1 − za1
 ) ( za2

1 − za2
 ) · · · ( zad

1 − zad
 ) .

Now use the machinery of Section 1.5.

Chapter 2

2.1 Use Exercise 1.3 for the closed interval. For open intervals, you can
use Exercise 1.4(j) or the ⌈. . . ⌉ notation of Exercise 1.4(e). To show the
quasipolynomial character, rewrite the greatest-integer function in terms of
the fractional-part function.

2.2 Write R as a direct product of two intervals and use Exercise 1.3.

2.6 Start by showing that the convex hull of a d-element subset W of V is a
face of ∆. This allows you to prove the ﬁrst statement by induction (using
Exercise 2.5). For the converse statement, given a supporting hyperplane H
that deﬁnes the face F of ∆, let W ⊆ V consist of those vertices of ∆ that

Hints for ♣ Exercises 257

are in H. Now prove that every point

x = λ1v1 + λ2v2 + · · · + λd+1vd+1

in F has to satisfy λk = 0 for all vk /∈ W .

2.7 First show that the linear inequalities and equations describing a rational
polytope can be chosen with rational coeﬃcients, and then clear denominators.

2.8

(a) Prove that as rational functions, ∑

j≥0 jdzj = (−1)d+1 ∑

j≥0 jd ( 1
z )j.

(b) Use the fact that
 ∑d
k=0 A(d,k)zk

(1−z)d+1 = z d
dz ( ∑d−1
k=0 A(d−1,k)zk

(1−z)d ).

(c) Begin by proving one of the remarks in the notes of Chapter 2, namely,
that A (d, k) counts the permutations of {1, 2, . . . , d} with k − 1 ascents.
(d) Use the fact that ∑d
k=0 A (d, k) zk = (1 − z)d+1 ∑

j≥0 jdzj.

2.9 Write 1
(1−z)d+1 = (∑

k1≥0 zk1) (∑

k2≥0 zk2) · · · (∑

kd+1≥0 zkd+1) and
come up with a combinatorial enumeration scheme to compute the coeﬃcients
of this power series.

2.10 Write (t+k
d ) = (t+k)(t+k−1)···(t+k−d+1)
d! and switch t to −t.

2.14 Think about the poles of the function z
ez−1 and use a theorem from
complex analysis.

2.15 Compute the generating function of Bd(1 − x) and rewrite it as z e−xz
1−e−z .

2.16 Show that z
ez−1 + 1
2 z is an even function of z.

2.23 Follow the steps of the proof of Theorem 2.4.

2.25 Extend T to a rectangle whose diagonal is the hypotenuse of T , and
consider the lattice points on this diagonal separately.

2.26 For the area use elementary calculus. For the number of boundary
points on tP, extend Exercise 1.12 to a set of line segments whose union forms
a simple closed curve.

2.33 Rewrite the inequality as (⌈ ta
d ⌉ − 1
) e + (⌈ tb
d ⌉ − 1
) f ≤ tr and compare
this with the deﬁnition of T .

2.34 To compute C3, multiply both sides of (2.20) by (z − 3)
2 and compute
the limit as z → 1. The coeﬃcients Aj and Bl can be computed in a similar
fashion. To compute C2, ﬁrst move C3
(z−1)3 in (2.20) to the left-hand side,
then multiply by (z − 1)2 and take the limit as z → 1. A similar, even more
elaborate, computation gives C1. (Alternatively, compute the Laurent series
of the function in (2.20) at z = 1 with a computer algebra system such as
Maple, Mathematica, or Sage.)

258 Hints for ♣ Exercises

2.35 Show that limz→ξk
a 1
1−zab + ξk
a
ab (z − ξk
a )−1 = ab−1
2ab .

2.36 Follow the proof of Theorem 2.10. Use Exercise 2.35 to compute the
additional coeﬃcients in the partial fraction expansion of the generating
function corresponding to this lattice-point count.

2.38 Start with computing the constant term of

1
(1 − z1z2) (1 − z2
1z2) (1 − z1) (1 − z2) z3t
1 z2t
2

with respect to z2 by treating z1 as a constant and setting up a partial fraction
expansion of this function with respect to z2.

Chapter 3

3.3

(a) Convince yourself that if the supporting hyperplane of F is vertical, then
h1, h2, . . . , hn in (3.1) were not chosen randomly.
(b) Prove that if ad+1 > 0, then there cannot exist a point (x1, x2, . . . , xd+1) ∈
F and an ϵ > 0 such that (x1, x2, . . . , xd+1 − ϵ) ∈ Q, and if ad+1 <
0 and (x1, x2, . . . , xd+1) ∈ F, then there exists ϵ > 0 such that
(x1, x2, . . . , xd+1 − ϵ) ∈ Q.
(c) Use the fact that F1 ∩ F2 is a face common to both F1 and F2.

3.5 Write the simplicial cones as cones over simplices and use Exercise 2.6.

3.8 Write down a typical term of the product

σS (z1, z2, . . . , zm) σT (zm+1, zm+2, . . . , zm+n) .

3.9 Multiply out zmσK(z).

3.10 Write a typical term in σS ( 1
z1 , 1
z2 , . . . , 1
zd
 ) = σS (z−1
1 , z−1
2 , . . . , z−1
d ) .

3.13 Given the polynomial f , split up the generating function on the left-hand
side according to the terms of f and use (2.2). Conversely, if the polynomial
g is given, use (2.6).

3.18 Show that H ∩ Z
d is a Z-module. Therefore, it has a basis; extend this
basis to a basis of Z
d.

3.19 Think about a small (even irrational) perturbation of all hyperplanes
in the right direction.

Hints for ♣ Exercises 259

3.21 View
 det
 





 x
d
1 xd−1
1 · · · x1 1
xd
2 xd−1
2 · · · x2 1
... ... ... ...
xd
d+1 xd−1
d+1 · · · xd+1 1
 






as a polynomial in x1, considering x2, x3, . . . , xd+1 constants. Show that this
polynomial has roots at x1 = x2, x1 = x3, . . . , x1 = xd+1, and compute its
leading coeﬃcient.

3.24 Given f , split up the generating function on the left-hand side according
to the constituents of f ; then use Exercise 3.13. Conversely, given g and h,
multiply both by a polynomial to get the denominator on the right-hand side
into the form (1 − zp)
d+1; then use (2.6).

3.25 Start with the setup on page 80, and closely orient yourself along the
proof of Theorem 3.8.

3.32 Convince yourself that if P has denominator p, then LP (0) equals the
constant term of the Ehrhart polynomial of pP.

3.34 Use Lemma 3.19.

Chapter 4

4.1 Use Exercise 2.1.

4.2 Use the explicit description of Π given by (4.3).

4.4 Consider each simplicial cone Kj separately, and look at the arrangement
of its bounding hyperplanes. For each hyperplane, use Exercise 3.18.

4.7 For (a), convince yourself that Q(−t) is also a quasipolynomial. For (b),
use (1.3). For (c), diﬀerentiate (1.3). For (d), think about one constituent of
the quasipolynomial at a time.

4.8 In the generating function for LP (t − k), make a change in the summation
variable; then use Theorem 4.4.

4.13 Use the fact that A has only integral entries. For the second part, write
down the explicit hyperplane descriptions of (t + 1)P ◦ and tP.

4.14 Assume that there exist t ∈ Z and a facet hyperplane H of P such that
there is a lattice point between tH and (t + 1)H. Translate this lattice point
to a lattice point that violates (4.12).

260 Hints for ♣ Exercises

Chapter 5

5.3 To prove the inclusion ⊆ (the other inclusion is clear), you need to show
that every point in P lies in the interior of some face F of P, and that the
relative interiors of two diﬀerent faces are disjoint. One can prove both facts
by looking for a minimal face that contains a given point in P in its relative
interior.

5.5 Consider an interval [F, P] in the face lattice of P; namely, [F, P]
contains all faces G such that F ⊆ G ⊆ P. Prove that if P is simple, then
every such interval is isomorphic to a Boolean lattice.

5.6 Use Exercise 2.6 to show that the face lattice of a simplex is isomorphic
to a Boolean lattice.

5.7 Orient yourself along the proof of Theorem 5.3, but start with the Euler
relation (Theorem 5.2) for a given face F instead of (5.2).

5.9 Assume that the origin is in the interior of P.

(a) Given a face F of P, show that

F ∗ := {x ∈ Rd : x · y ≤ 1 for all y ∈ P, x · y = 1 for all y ∈ F}

is a face of P ∗, and that G ⊆ F if and only if G∗ ⊇ F ∗.
(b) Figure out a prominent property of the face lattice of every sim-
ple/simplicial polytope; then use (a).
(c) Try a proof that is dual to the one hinted at in Exercise 5.7.

5.14

(a) First choose any two of the ﬁve points on the sphere, and draw a great
circle through them. This great circle partitions the sphere into two
hemispheres, and the union of these two hemispheres now contains three
of the ﬁve given points. Now the pigeonhole principle tells us that (at
least) two of the ﬁve given points must lie in one of these two hemispheres.
(b) Normalize the ﬁve given vectors to have unit length and use part (a) of
this exercise.

Chapter 6

6.1 Think permutation matrices.

6.3 Show that the rank of (6.5) is 2n − 1.

6.5 Start by showing that all permutation matrices are indeed vertices. Then
use Exercise 6.4 to show that there are no other vertices.

Hints for ♣ Exercises 261

6.6 Establish a bijection between semimagic squares with line sum t − n and
semimagic squares with positive entries and line sum t.

6.7 Think about the smallest possible line sum if the entries of the square
are positive integers.

6.8 Follow the computation on page 120 that led to the formula for H2.

6.9 Multiply both sides of (6.7) by (w − 1
zk
 ) and take the limit as w → 1
zk .

6.10 Orient yourself along the computation in (6.10).

6.16 Compute the matrix equivalent to (6.5) for the polytope describing all
magic squares of a given size. Show that this matrix has rank 2n + 1.

6.18 Orient yourself along the computation on page 120.

Chapter 7

7.2 Use Exercise 7.1.

7.5 Diﬀerentiate (1.3).

7.6 Use (1.3).

7.7 Write an arbitrary function on Z with period b in terms of δm(x),
1 ≤ m ≤ b.

7.8 Use the deﬁnition (7.6) of the inner product and the properties zz = |z|
2

and (zw) = z · w for complex numbers z and w.

7.15 Use the deﬁnition (7.4) and simplify the fractional-part function in the
sum on the right-hand side.

7.23 Use the deﬁnition of F.

Chapter 8

8.7 Use Exercise 1.9.

8.9 Use the methods outlined in the hints for Exercises 1.21 and 2.34 to
compute the partial fraction coeﬃcients for z = 1 in (8.3).

8.12 Multiply out all the terms on the left-hand side and make use of
Exercises 1.9 and 7.15.

8.15 Use the methods outlined in the hints for Exercises 1.21 and 2.34 to
compute a partial fraction expansion of (8.8).

262 Hints for ♣ Exercises

Chapter 9

9.1 Write out a typical term in p(z1, z2, . . . , zd) q(z1, z2, . . . , zd).

9.5 Review the deﬁnition of Z(u1, u2, . . . un) to show that

Π1 ∪ Π2 ∪ · · · ∪ Πk ∪ P1 ∪ P2 ∪ · · · ∪ Pm = Z(u1, u2, . . . un)

and then show that this union is disjoint, using the precise deﬁnition of
the Pj’s.

9.9 Convince yourself that Pd lies in the hyperplane given by the equation
x1 + x2 + · · · + xd = (d
2), and ﬁnd d − 1 linearly independent vectors among
those deﬁning Pd. To show that v = (π(1) − 1, π(2) − 1, . . . , π(d) − 1) is a
vertex of Pd, consider the hyperplane through v with normal vector v.

Chapter 10

10.1 Expand the powers of (1 − z) in the deﬁnition of hP (z).

10.2 Assume that P is full-dimensional and consider a facet of S by con-
structing one of its supporting hyperplanes. Show that this hyperplane can
contain no more than d vertices of S. To show that the face numbers of S
equal those of the triangulation of ∂P, try to construct a bijection.

10.4 Given the unimodular k-simplex ∆ ⊂ Rd, construct a bijection
span(∆) → Rk that maps ∆ to {
x ∈ Rk
≥0 : x1 + x2 + · · · + xk ≤ 1
} and
span(∆) ∩ Z
d to Z
k.

10.7 Start by showing that if ∆ is a k-simplex and

Π := {λ1w1 + λ2w2 + · · · + λk+1wk+1 : 0 < λ1, λ2, . . . , λk+1 < 1}

is the open fundamental parallelepiped of cone(∆), then

Π = −Π + w1 + w2 + · · · + wk+1 .

10.8 Carefully review the deﬁnition of link(∆).

10.9 Begin by rewriting (10.3), collecting terms stemming from simplices Φ
of the same dimension.

10.10 Begin by proving that

Π(∆) = {0} ∪ ⋃

Ω⊆∆ Π(Ω)◦,

Hints for ♣ Exercises 263

where the union is over all nonempty faces of ∆, and that this union is disjoint.

10.11 Build an almost-one-to-one correspondence between the simplices in
T and those in T0 \ T , and see what this correspondence gives about the
respective h-vectors of links.

10.12 Establish a one-to-one correspondence between link(∆) and the bound-
ary faces of a polytope of dimension d − dim(∆) − 1 respecting the face
relations.

10.13 Writing a(z) = adzd + ad−1zd−1 + · · · + a0 and b(z) = bd−1zd−1 +
bd−2zd−2 + · · · + b0, give a concrete rule how to compute a0, ad, bd−1, b0, a1,
ad−1, bd−2, . . . from the coeﬃcients of p(z).

10.14 See what your rule from Exercise 10.13 says about the coeﬃcients of
h
∗
P (z) when one takes into account that the aj’s and bj’s are nonnegative.

Chapter 11

11.4 Consider the hyperplanes H1, H2, . . . , Hd+1 that bound ∆. For each
hyperplane Hk, denote by H +
k the closed half-space bounded by Hk that
contains ∆, and by H −
k the open half-space bounded by Hk that does not
contain ∆. Show that every tangent cone of ∆ is the intersection of some
of the H +
k ’s, and conversely, that every intersection of some of the H +
k ’s,
except for ∆ = ⋂d+1
k=1 H +
k , is a tangent cone of ∆. Since H +
k ∪ H −
k = Rd as a
disjoint union, for each k, the point x is either in H +
k or H −
k . Prove that the
intersection of those H +
k that contain x is the sought-after tangent cone.

11.6 As in Exercise 5.6, show that the face lattice of a simplex is a Boolean
lattice. Note that every sublattice of a Boolean lattice is again Boolean.

11.8 One approach to this problem is ﬁrst to dilate P and the corresponding
hyperplanes in H by a small factor. To avoid subtleties, ﬁrst translate P by
an integer vector, if necessary, to ensure that none of the hyperplanes in H
contains the origin. Use Exercise 3.18.

11.9 Adjust the steps in Section 11.4 to open polytopes. Start by proving a
Brianchon–Gram identity for open simplices, by analogy with Theorem 11.5.
This implies a Brion-type identity for open simplices, as in Corollary 11.6.
Finally, adjust the proof of Theorem 11.7 to open polytopes.

Chapter 12

12.1 Use (12.3), Exercise 2.18, and (2.11).

264 Hints for ♣ Exercises

12.2 Review the proof of Theorem 3.5.

12.3 Use the deﬁnition of unimodularity to show that the only integer point
in the fundamental parallelepiped of K is v.

12.6 Orient yourself along the proof of Theorem 12.3; instead of a sum over
vertex cones, just consider one simple cone K.

Chapter 13

13.5 Multiply out zmαK(z).

13.6 Orient yourself along the proof of Theorem 4.2. Note that for solid
angles, we do not require the condition that the boundary of K contains no
lattice point.

13.7 As a warmup exercise, show that
∑

F ⊆∆
dim F >0
 ∑

v a vertex of F σKv(F )◦ (z) = ∑

v a vertex of ∆
 ∑

F ⊆Kv
dim F >0
 σF ◦ (z) .

13.8 Start with the setup of our second proof of Ehrhart’s theorem in
Section 11.5; that is, it suﬃces to prove that if p is the denominator of P, then
AP (−r − pt) = (−1)dim P AP (r + pt) for all integers r and t with 0 ≤ r < p
and t > 0. (Think of r as ﬁxed and t as variable.) Now orient yourself along
the proof on page 232.

Chapter 14

14.1 Bound the integral from above, using the length of Cr and an upper
bound for the absolute value of the integrand.

14.2 The nontrivial roots of unity are simple poles of f , for which the residue
computation boils down to a simple limit.

14.5 Start by combining the terms 1
z−(m+ni) and 1
m+ni into one fraction.

14.6 Diﬀerentiate (14.1) term by term.

14.7 Compute ℘
′ explicitly.

14.8 Use a famous theorem from complex analysis.

14.9 Compute ℘ (−z) and use the fact that (−(m + in))
2 = (m + in)
2.

Hints for ♣ Exercises 265

14.10 Repeat the proof of Lemma 14.3, but now starting with the proof of
℘
′ (z + i) = ℘
′(z).

14.11 Use a famous theorem from complex analysis.

14.12 Use the deﬁnition of the Weierstraß ℘-function.

References

1. The On-Line Encyclopedia of Integer Sequences, published electronically at
http://oeis.org, 2014.
2. Maya Ahmed, Jes´us A. De Loera, and Raymond Hemmecke, Polyhedral cones of
magic cubes and squares, Discrete and Computational Geometry, Algorithms Com-
bin., vol. 25, Springer, Berlin, 2003, pp. 25–41, arXiv:math.CO/0201108.
3. Maya Mohsin Ahmed, How many squares are there, Mr. Franklin? constructing and
enumerating Franklin squares, Amer. Math. Monthly 111 (2004), no. 5, 394–410.
4. Iskander Aliev, Martin Henk, and Aicke Hinrichs, Expected Frobenius numbers, J.
Combin. Theory Ser. A 118 (2011), no. 2, 525–531.
5. Iskander M. Aliev and Peter M. Gruber, An optimal lower bound for the Frobenius
problem, J. Number Theory 123 (2007), no. 1, 71–79.
6. Harsh Anand, Vishwa Chander Dumir, and Hansraj Gupta, A combinatorial distri-
bution problem, Duke Math. J. 33 (1966), 757–769.
7. W. S. Andrews, Magic Squares and Cubes, Dover Publications Inc., New York, 1960.
8. Tom M. Apostol, Generalized Dedekind sums and transformation formulae of certain
Lambert series, Duke Math. J. 17 (1950), 147–157.
9. Tom M. Apostol and Thiennu H. Vu, Identities for sums of Dedekind type, J. Number
Theory 14 (1982), no. 3, 391–396.
10. Federico Ardila, Federico Castillo, and Michael Henley, The arithmetic Tutte polyno-
mials of the classical root systems, Int. Math. Res. Not. (to appear), arXiv:1305.6621.
11. Vladimir I. Arnold, Arnold’s problems, Springer-Verlag, Berlin, 2004, Translated and
revised edition of the 2000 Russian original, with a preface by V. Philippov, A.
Yakivchik, and M. Peters.
12. Christos A. Athanasiadis, h∗-vectors, Eulerian polynomials and stable polytopes of
graphs, Electron. J. Combin. 11 (2004/06), no. 2, Research Paper 6, 13 pp.
13. , Ehrhart polynomials, simplicial polytopes, magic squares and a conjecture
of Stanley, J. Reine Angew. Math. 583 (2005), 163–174, arXiv:math/0312031.
14. Velleda Baldoni, Nicole Berline, Matthias K¨oppe, and Mich`ele Vergne, Intermediate
sums on polyhedra: computation and real Ehrhart theory, Mathematika 59 (2013),
no. 1, 1–22, arXiv:math/1011.6002.
15. Velleda Baldoni, Nicole Berline, and Mich`ele Vergne, Local Euler–Maclaurin expan-
sion of Barvinok valuations and Ehrhart coeﬃcients of a rational polytope, Integer
points in polyhedra—geometry, number theory, representation theory, algebra, opti-
mization, statistics, Contemp. Math., vol. 452, Amer. Math. Soc., Providence, RI,
2008, pp. 15–33.
16. Velleda Baldoni and Mich`ele Vergne, Residue formulae for volumes and Ehrhart
polynomials of convex polytopes, Preprint (arXiv:math.CO/0103097).
 267

268 References

17. Philippe Barkan, Sur les sommes de Dedekind et les fractions continues ﬁnies, C. R.
Acad. Sci. Paris S´er. A-B 284 (1977), no. 16, A923–A926.
18. Peter Barlow, An Elementary Investigation of the Theory of Numbers, J. Johnson &
Co., London, 1811.
19. Ernest W. Barnes, The theory of the double gamma function, Philos. Trans. R. Soc.
London, Ser. A 196 (1901), 265–387.
20. Alexander Barvinok, Exponential integrals and sums over convex polyhedra, Funkt-
sional. Anal. i Prilozhen. 26 (1992), no. 2, 64–66.
21. , A Course in Convexity, Graduate Studies in Mathematics, vol. 54, American
Mathematical Society, Providence, RI, 2002.
22. , Integer points in polyhedra, Zurich Lectures in Advanced Mathematics, Eu-
ropean Mathematical Society (EMS), Zurich, 2008.
23. Alexander Barvinok and James E. Pommersheim, An algorithmic theory of lattice
points in polyhedra, New Perspectives in Algebraic Combinatorics (Berkeley, CA,
1996–97), Math. Sci. Res. Inst. Publ., vol. 38, Cambridge Univ. Press, Cambridge,
1999, pp. 91–147.
24. Alexander Barvinok and Kevin Woods, Short rational generating functions
for lattice point problems, J. Amer. Math. Soc. 16 (2003), no. 4, 957–979,
arXiv:math.CO/0211146.
25. Alexander I. Barvinok, A polynomial time algorithm for counting integral points in
polyhedra when the dimension is ﬁxed, Math. Oper. Res. 19 (1994), no. 4, 769–779.
26. Victor V. Batyrev, Dual polyhedra and mirror symmetry for Calabi–Yau hy-
persurfaces in toric varieties, J. Algebraic Geom. 3 (1994), no. 3, 493–535,
arXiv:alg-geom/9310003.
27. Victor V. Batyrev and Dimitrios I. Dais, Strong McKay correspondence, string-
theoretic Hodge numbers and mirror symmetry, Topology 35 (1996), no. 4, 901–929.
28. Abdelmejid Bayad and Matthias Beck, Relations for Bernoulli–Barnes numbers
and Barnes zeta functions, Int. J. Number Theory 10 (2014), no. 5, 1321–1335,
arXiv:1301.7097.
29. Abdelmejid Bayad and Yilmaz Simsek, Dedekind sums involving Jacobi modular
forms and special values of Barnes zeta functions, Ann. Inst. Fourier (Grenoble)
61 (2011), no. 5, 1977–1993 (2012).
30. Matthias Beck, Counting lattice points by means of the residue theorem, Ramanujan
J. 4 (2000), no. 3, 299–310, arXiv:math.CO/0306035.
31. , Multidimensional Ehrhart reciprocity, J. Combin. Theory Ser. A 97 (2002),
no. 1, 187–194, arXiv:math.CO/0111331.
32. , Dedekind cotangent sums, Acta Arith. 109 (2003), no. 2, 109–130,
arXiv:math.NT/0112077.
33. Matthias Beck and Benjamin Braun, Euler–Mahonian statistics via polyhedral geom-
etry, Adv. Math. 244 (2013), 925–954, arXiv:1109.3353.
34. Matthias Beck and Anastasia Chavez, Bernoulli-Dedekind sums, Acta Arith. 149
(2011), no. 1, 65–82, arXiv:1008.0038.
35. Matthias Beck, Beifang Chen, Lenny Fukshansky, Christian Haase, Allen Knutson,
Bruce Reznick, Sinai Robins, and Achill Sch¨urmann, Problems from the Cottonwood
Room, Integer Points in Polyhedra—Geometry, Number Theory, Algebra, Optimiza-
tion, Contemp. Math., vol. 374, Amer. Math. Soc., Providence, RI, 2005, pp. 179–191.
36. Matthias Beck, Moshe Cohen, Jessica Cuomo, and Paul Gribelyuk, The number of
“magic” squares, cubes, and hypercubes, Amer. Math. Monthly 110 (2003), no. 8,
707–717, arXiv:math.CO/0201013.
37. Matthias Beck, Jes´us A. De Loera, Mike Develin, Julian Pfeiﬂe, and Richard P. Stan-
ley, Coeﬃcients and roots of Ehrhart polynomials, Integer Points in Polyhedra—
Geometry, Number Theory, Algebra, Optimization, Contemp. Math., vol. 374, Amer.
Math. Soc., Providence, RI, pp. 15–36, arXiv:math.CO/0402148.

References 269

38. Matthias Beck, Ricardo Diaz, and Sinai Robins, The Frobenius problem, rational
polytopes, and Fourier–Dedekind sums, J. Number Theory 96 (2002), no. 1, 1–21,
arXiv:math.NT/0204035.
39. Matthias Beck and Richard Ehrenborg, Ehrhart–Macdonald reciprocity extended,
Preprint (arXiv:math.CO/0504230).
40. Matthias Beck, Christian Haase, and Asia R. Matthews, Dedekind–Carlitz polynomi-
als as lattice-point enumerators in rational polyhedra, Math. Ann. 341 (2008), no. 4,
945–961, arXiv:0710.1323.
41. Matthias Beck, Christian Haase, and Frank Sottile, Formulas of Brion, Lawrence,
and Varchenko on rational generating functions for cones, Math. Intelligencer 31
(2009), no. 1, 9–17, arXiv:math.CO/0506466.
42. Matthias Beck and Curtis Kifer, An extreme family of generalized Frobenius numbers,
Integers 11 (2011), Paper A24, 6 pp.
43. Matthias Beck and Dennis Pixton, The Ehrhart polynomial of the Birkhoﬀ polytope,
Discrete Comput. Geom. 30 (2003), no. 4, 623–637, arXiv:math.CO/0202267.
44. Matthias Beck and Sinai Robins, Explicit and eﬃcient formulas for the lattice
point count in rational polygons using Dedekind–Rademacher sums, Discrete Comput.
Geom. 27 (2002), no. 4, 443–459, arXiv:math.CO/0111329.
45. , A formula related to the Frobenius problem in two dimensions, Number the-
ory (New York, 2003), Springer, New York, 2004, pp. 17–23, arXiv:math.NT/0204037.
46. Matthias Beck, Sinai Robins, and Steven V Sam, Positivity theorems for solid-angle
polynomials, Beitr¨age Algebra Geom. 51 (2010), no. 2, 493–507, arXiv:0906.4031.
47. Matthias Beck and Frank Sottile, Irrational proofs for three theorems of Stanley,
European J. Combin. 28 (2007), no. 1, 403–409, arXiv:math.CO/0506315.
48. Matthias Beck and Andrew van Herick, Enumeration of 4 × 4 magic squares, Math.
Comp. 80 (2011), no. 273, 617–621, arXiv:0907.3188.
49. Matthias Beck and Thomas Zaslavsky, An enumerative geometry for magic and magi-
latin labellings, Ann. Comb. 10 (2006), no. 4, 395–413, arXiv:math.CO/0506315.
50. Dale Beihoﬀer, Jemimah Hendry, Albert Nijenhuis, and Stan Wagon, Faster algo-
rithms for Frobenius numbers, Electron. J. Combin. 12 (2005), no. 1, Research Paper
27, 38 pp.
51. Nicole Berline and Mich`ele Vergne, Local Euler–Maclaurin formula for polytopes,
Mosc. Math. J. 7 (2007), no. 3, 355–386, 573, arXiv:math.CO/0507256.
52. Bruce C. Berndt, Reciprocity theorems for Dedekind sums and generalizations, Ad-
vances in Math. 23 (1977), no. 3, 285–316.
53. Bruce C. Berndt and Ulrich Dieter, Sums involving the greatest integer function and
Riemann–Stieltjes integration, J. Reine Angew. Math. 337 (1982), 208–220.
54. Bruce C. Berndt and Boon Pin Yeap, Explicit evaluations and reciprocity theorems
for ﬁnite trigonometric sums, Adv. in Appl. Math. 29 (2002), no. 3, 358–385.
55. Ulrich Betke and Peter McMullen, Lattice points in lattice polytopes, Monatsh. Math.
99 (1985), no. 4, 253–265.
56. Christian Bey, Martin Henk, and J¨org M. Wills, Notes on the roots of Ehrhart poly-
nomials, Discrete Comput. Geom. 38 (2007), no. 1, 81–98, arXiv:math.MG/0606089.
57. Louis J. Billera and A. Sarangarajan, The combinatorics of permutation polytopes,
Formal Power Series and Algebraic Combinatorics (New Brunswick, NJ, 1994), Amer.
Math. Soc., Providence, RI, 1996, pp. 1–23.
58. Garrett Birkhoﬀ, Tres observaciones sobre el ´algebra lineal, Revista Faculdad de
Ciencias Exactas, Puras y Aplicadas Universidad Nacional de Tucum´an, Serie A
(Matem´aticas y F´ısica Te´oretica) 5 (1946), 147–151.
59. G. R. Blakley, Combinatorial remarks on partitions of a multipartite number, Duke
Math. J. 31 (1964), 335–340.
60. Sebastian B¨ocker and Zsuzsanna Lipt´ak, The money changing problem revisited: com-
puting the Frobenius number in time O(ka1), Computing and combinatorics, Lecture
Notes in Comput. Sci., vol. 3595, Springer, Berlin, 2005, pp. 965–974.

270 References

61. Alfred Brauer, On a problem of partitions, Amer. J. Math. 64 (1942), 299–312.
62. Benjamin Braun, An Ehrhart series formula for reﬂexive polytopes, Electron. J. Com-
bin. 13 (2006), no. 1, Note 15, 5 pp.
63. , Norm bounds for Ehrhart polynomial roots, Discrete Comput. Geom. 39
(2008), no. 1–3, 191–193, arXiv:math.CO/0602464.
64. Benjamin Braun and Robert Davis, Ehrhart series, unimodality, and integrally closed
reﬂexive polytopes, to appear in Ann. Comb., arXiv:math/1403.5378.
65. Henrik Bresinsky, Symmetric semigroups of integers generated by 4 elements,
Manuscripta Math. 17 (1975), no. 3, 205–219.
66. Charles J. Brianchon, Th´eor`eme nouveau sur les poly`edres, J. Ecole (Royale) Poly-
technique 15 (1837), 317–319.
67. Michel Brion, Points entiers dans les poly`edres convexes, Ann. Sci. ´Ecole Norm. Sup.
(4) 21 (1988), no. 4, 653–663.
68. Michel Brion and Mich`ele Vergne, Residue formulae, vector partition functions and
lattice points in rational polytopes, J. Amer. Math. Soc. 10 (1997), no. 4, 797–833.
69. Arne Brøndsted, An Introduction to Convex Polytopes, Graduate Texts in Mathe-
matics, vol. 90, Springer-Verlag, New York, 1983.
70. Richard A. Brualdi and Peter M. Gibson, Convex polyhedra of doubly stochastic
matrices. I. Applications of the permanent function, J. Combinatorial Theory Ser. A
22 (1977), no. 2, 194–230.
71. , Convex polyhedra of doubly stochastic matrices. III. Aﬃne and combinato-
rial properties of Un, J. Combinatorial Theory Ser. A 22 (1977), no. 3, 338–351.
72. Heinz Bruggesser and Peter Mani, Shellable decompositions of cells and spheres, Math.
Scand. 29 (1971), 197–205 (1972).
73. Winfried Bruns, Commutative algebra arising from the Anand–Dumir–Gupta conjec-
tures, Commutative algebra and combinatorics, Ramanujan Math. Soc. Lect. Notes
Ser., vol. 4, Ramanujan Math. Soc., Mysore, 2007, pp. 1–38.
74. Winfried Bruns and Joseph Gubeladze, Polytopes, rings, and K-theory, Springer
Monographs in Mathematics, Springer, Dordrecht, 2009.
75. Winfried Bruns and Tim R¨omer, h-vectors of Gorenstein polytopes, J. Combin. The-
ory Ser. A 114 (2007), no. 1, 65–76.
76. Daniel Bump, Kwok-Kwong Choi, P¨ar Kurlberg, and Jeﬀrey Vaaler, A local Riemann
hypothesis. I, Math. Z. 233 (2000), no. 1, 1–19.
77. Kristin A. Camenga, Vector spaces spanned by the angle sums of polytopes, Beitr¨age
Algebra Geom. 47 (2006), no. 2, 447–462, arXiv:math.MG/0508629.
78. Schuyler Cammann, Old Chinese magic squares, Sinologica 7 (1962), 14–53.
79. , Islamic and Indian magic squares, Parts I and II, History of Religions 8
(1969), 181–209; 271–299.
80. Sylvain E. Cappell and Julius L. Shaneson, Euler–Maclaurin expansions for lattices
above dimension one, C. R. Acad. Sci. Paris S´er. I Math. 321 (1995), no. 7, 885–890.
81. Leonard Carlitz, Some theorems on generalized Dedekind sums, Paciﬁc J. Math. 3
(1953), 513–522.
82. , Some polynomials associated with Dedekind sums, Acta Math. Acad. Sci.
Hungar. 26 (1975), no. 3–4, 311–319.
83. John W. S. Cassels, An Introduction to the Geometry of Numbers, Classics in Math-
ematics, Springer-Verlag, Berlin, 1997, Corrected reprint of the 1971 edition.
84. Clara S. Chan, David P. Robbins, and David S. Yuen, On the volume of a certain
polytope, Experiment. Math. 9 (2000), no. 1, 91–99, arXiv:math.CO/9810154.
85. Beifang Chen, Weight functions, double reciprocity laws, and volume formulas for
lattice polyhedra, Proc. Natl. Acad. Sci. USA 95 (1998), no. 16, 9093–9098.
86. , Lattice points, Dedekind sums, and Ehrhart polynomials of lattice polyhedra,
Discrete Comput. Geom. 28 (2002), no. 2, 175–199.
87. Beifang Chen and Vladimir Turaev, Counting lattice points of rational polyhedra,
Adv. Math. 155 (2000), no. 1, 84–97.

References 271

88. Louis Comtet, Advanced Combinatorics, enlarged ed., D. Reidel Publishing Co., Dor-
drecht, 1974.
89. David Cox, Christian Haase, Takayuki Hibi, and Akihiro Higashitani, Integer decom-
position property of dilated polytopes, Electron. J. Combin. 21 (2014), no. 4, P4.28,
17 pp.
90. Michele D’Adderio and Luca Moci, Ehrhart polynomial and arithmetic Tutte polyno-
mial, European J. Combin. 33 (2012), no. 7, 1479–1483, arXiv:math/1102.0135.
91. Wolfgang Dahmen and Charles A. Micchelli, The number of solutions to linear Dio-
phantine equations and multivariate splines, Trans. Amer. Math. Soc. 308 (1988),
no. 2, 509–532.
92. Vladimir I. Danilov, The geometry of toric varieties, Uspekhi Mat. Nauk 33 (1978),
85–134, 247.
93. Robert Davis, Ehrhart series of polytopes related to symmetric doubly-stochastic ma-
trices, Preprint (arXiv:math/1409.2742).
94. J. Leslie Davison, On the linear Diophantine problem of Frobenius, J. Number Theory
48 (1994), no. 3, 353–363.
95. Jes´us A. De Loera, David Haws, Raymond Hemmecke, Peter Huggins, and Ruriko
Yoshida, A user’s guide for LattE v1.1, software package LattE, 2004. Electronically
available at https://www.math.ucdavis.edu/ latte/.
96. Jes´us A. De Loera, Raymond Hemmecke, and Matthias K¨oppe, Algebraic and Geo-
metric Ideas in the Theory of Discrete Optimization, MOS-SIAM Series on Optimiza-
tion, vol. 14, Society for Industrial and Applied Mathematics (SIAM), Philadelphia,
PA; Mathematical Optimization Society, Philadelphia, PA, 2013.
97. Jes´us A. De Loera, Raymond Hemmecke, Jeremiah Tauzer, and Ruriko Yoshida, Ef-
fective lattice point counting in rational convex polytopes, J. Symbolic Comput. 38
(2004), no. 4, 1273–1302.
98. Jes´us A. De Loera and Shmuel Onn, The complexity of three-way statistical tables,
SIAM J. Comput. 33 (2004), no. 4, 819–836, arXiv:math.CO/0207200.
99. Jes´us A. De Loera, J¨org Rambau, and Francisco Santos, Triangulations, Algorithms
and Computation in Mathematics, vol. 25, Springer-Verlag, Berlin, 2010.
100. Richard Dedekind, Erl¨auterungen zu den Fragmenten XXVIII, Collected Works of
Bernhard Riemann, Dover Publ., New York, 1953, pp. 466–478.
101. Max Dehn, Die Eulersche Formel im Zusammenhang mit dem Inhalt in der nicht-
euklidischen Geometrie, Math. Ann. 61 (1905), 561–586.
102. J´ozsef D´enes and Anthony D. Keedwell, Latin squares and their applications, Aca-
demic Press, New York, 1974.
103. Graham Denham, Short generating functions for some semigroup algebras, Electron.
J. Combin. 10 (2003), Research Paper 36, 7 pp.
104. David Desario and Sinai Robins, Generalized solid-angle theory for real polytopes, Q.
J. Math. 62 (2011), no. 4, 1003–1015, arXiv:0708.0042.
105. Persi Diaconis and Anil Gangolli, Rectangular arrays with ﬁxed margins, Discrete
Probability and Algorithms (Minneapolis, MN, 1993), Springer, New York, 1995,
pp. 15–41.
106. Ricardo Diaz and Sinai Robins, Pick’s formula via the Weierstrass ℘-function, Amer.
Math. Monthly 102 (1995), no. 5, 431–437.
107. , The Ehrhart polynomial of a lattice polytope, Ann. of Math. (2) 145 (1997),
no. 3, 503–518.
108. Ulrich Dieter, Das Verhalten der Kleinschen Funktionen log σg,h(ω1, ω2) gegen¨uber
Modultransformationen und verallgemeinerte Dedekindsche Summen, J. Reine
Angew. Math. 201 (1959), 37–70.
109. , Cotangent sums, a further generalization of Dedekind sums, J. Number The-
ory 18 (1984), no. 3, 289–305.
110. Eug`ene Ehrhart, Sur les poly`edres rationnels homoth´etiques `a n dimensions, C. R.
Acad. Sci. Paris 254 (1962), 616–618.

272 References

111. , Sur les carr´es magiques, C. R. Acad. Sci. Paris S´er. A-B 277 (1973), A651–
A654.
112. , Polynˆomes arithm´etiques et m´ethode des poly`edres en combinatoire,
Birkh¨auser Verlag, Basel, 1977, International Series of Numerical Mathematics, Vol.
35.
113. G¨unter Ewald, Combinatorial convexity and algebraic geometry, Graduate Texts in
Mathematics, vol. 168, Springer-Verlag, New York, 1996.
114. Leonid G. Fel and Boris Y. Rubinstein, Restricted partition function as Bernoulli
and Euler polynomials of higher order, Ramanujan J. 11 (2006), no. 3, 331–348,
arXiv:math.NT/0304356.
115. Matthew H. J. Fiset and Alexander M. Kasprzyk, A note on palindromic δ-vectors
for certain rational polytopes, Electron. J. Combin. 15 (2008), no. 1, Note 18, 4 pp.
116. Lenny Fukshansky and Sinai Robins, Bounds for solid angles of lattices of rank three,
J. Combin. Theory Ser. A 118 (2011), no. 2, 690–701, arXiv:1006.0743.
117. William Fulton, Introduction to Toric Varieties, Annals of Mathematics Studies, vol.
131, Princeton University Press, Princeton, NJ, 1993.
118. Stavros Garoufalidis and James E. Pommersheim, Values of zeta functions at negative
integers, Dedekind sums and toric geometry, J. Amer. Math. Soc. 14 (2001), no. 1,
1–23.
119. Ewgenij Gawrilow and Michael Joswig, polymake: a framework for analyzing convex
polytopes, Polytopes—combinatorics and computation (Oberwolfach, 1997), DMV
Sem., vol. 29, Birkh¨auser, Basel, 2000, pp. 43–73, Software polymake available at
www.polymake.org/.
120. Ira M. Gessel, Generating functions and generalized Dedekind sums, Electron. J.
Combin. 4 (1997), no. 2, Research Paper 11, 17 pp.
121. Kurt Girstmair, On the fractional parts of Dedekind sums, Int. J. Number Theory
11 (2015), no. 1, 29–38.
122. Jørgen P. Gram, Om rumvinklerne i et polyeder, Tidsskrift for Math. (Copenhagen)
4 (1874), no. 3, 161–163.
123. Nick Gravin, Jean B. Lasserre, Dmitrii V. Pasechnik, and Sinai Robins, The inverse
moment problem for convex polytopes, Discrete Comput. Geom. 48 (2012), no. 3,
596–621.
124. Nick Gravin, Sinai Robins, and Dmitry Shiryaev, Translational tilings by a polytope,
with multiplicity, Combinatorica 32 (2012), no. 6, 629–649, arXiv:1103.3163.
125. Harold Greenberg, An algorithm for a linear Diophantine equation and a problem of
Frobenius, Numer. Math. 34 (1980), no. 4, 349–352.
126. Peter M. Gruber, Convex and discrete geometry, Grundlehren der Mathematischen
Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 336, Springer,
Berlin, 2007.
127. Branko Gr¨unbaum, Convex Polytopes, second ed., Graduate Texts in Mathematics,
vol. 221, Springer-Verlag, New York, 2003, Prepared and with a preface by Volker
Kaibel, Victor Klee, and G¨unter M. Ziegler.
128. Victor Guillemin, Riemann–Roch for toric orbifolds, J. Diﬀerential Geom. 45 (1997),
no. 1, 53–73.
129. Ulrich Halbritter, Some new reciprocity formulas for generalized Dedekind sums, Re-
sults Math. 8 (1985), no. 1, 21–46.
130. Richard R. Hall and Martin N. Huxley, Dedekind sums and continued fractions, Acta
Arith. 63 (1993), no. 1, 79–90.
131. Richard R. Hall, J. C. Wilson, and Don Zagier, Reciprocity formulae for general
Dedekind–Rademacher sums, Acta Arith. 73 (1995), no. 4, 389–396.
132. Martin Henk, Achill Sch¨urmann, and J¨org M. Wills, Ehrhart polynomials and succes-
sive minima, Mathematika 52 (2005), no. 1–2, 1–16 (2006), arXiv:math.MG/0507528.
133. J¨urgen Herzog, Generators and relations of abelian semigroups and semigroup rings.,
Manuscripta Math. 3 (1970), 175–193.

References 273

134. Takayuki Hibi, Some results on Ehrhart polynomials of convex polytopes, Discrete
Math. 83 (1990), no. 1, 119–121.
135. , Algebraic Combinatorics on Convex Polytopes, Carslaw, 1992.
136. , Dual polytopes of rational convex polytopes, Combinatorica 12 (1992), no. 2,
237–240.
137. Dean Hickerson, Continued fractions and density results for Dedekind sums, J. Reine
Angew. Math. 290 (1977), 113–116.
138. Lutz Hille and Harald Skarke, Reﬂexive polytopes in dimension 2 and certain relations
in SL2(Z), J. Algebra Appl. 1 (2002), no. 2, 159–173.
139. Friedrich Hirzebruch, Neue topologische Methoden in der algebraischen Geometrie,
Ergebnisse der Mathematik und ihrer Grenzgebiete (N.F.), Heft 9, Springer-Verlag,
Berlin, 1956.
140. , Eulerian polynomials, M¨unster J. Math. 1 (2008), 9–14.
141. Friedrich Hirzebruch and Don Zagier, The Atiyah–Singer Theorem and Elementary
Number Theory, Publish or Perish Inc., Boston, Mass., 1974.
142. Jeﬀrey Hood and David Perkinson, Some facets of the polytope of even permutation
matrices, Linear Algebra Appl. 381 (2004), 237–244.
143. Masa-Nori Ishida, Polyhedral Laurent series and Brion’s equalities, Internat. J. Math.
1 (1990), no. 3, 251–265.
144. Maruf Israilovich Israilov, Determination of the number of solutions of linear Dio-
phantine equations and their applications in the theory of invariant cubature formu-
las, Sibirsk. Mat. Zh. 22 (1981), no. 2, 121–136, 237.
145. Ravi Kannan, Lattice translates of a polytope and the Frobenius problem, Combina-
torica 12 (1992), no. 2, 161–177.
146. Jean-Michel Kantor and Askold G. Khovanski˘ı, Une application du th´eor`eme de
Riemann–Roch combinatoire au polynˆome d’Ehrhart des polytopes entiers de Rd,
C. R. Acad. Sci. Paris S´er. I Math. 317 (1993), no. 5, 501–507.
147. Yael Karshon, Shlomo Sternberg, and Jonathan Weitsman, The Euler–Maclaurin
formula for simple integral polytopes, Proc. Natl. Acad. Sci. USA 100 (2003), no. 2,
426–433.
148. Askold G. Khovanski˘ı and Aleksandr V. Pukhlikov, The Riemann–Roch theorem for
integrals and sums of quasipolynomials on virtual polytopes, Algebra i Analiz 4 (1992),
no. 4, 188–216.
149. Peter Kirschenhofer, Attila Peth˝o, and Robert F. Tichy, On analytical and Diophan-
tine properties of a family of counting polynomials, Acta Sci. Math. (Szeged) 65
(1999), no. 1–2, 47–59.
150. Daniel A. Klain and Gian-Carlo Rota, Introduction to Geometric Probability, Lezioni
Lincee, Cambridge University Press, Cambridge, 1997.
151. Victor Klee, A combinatorial analogue of Poincar´e’s duality theorem, Canad. J. Math.
16 (1964), 517–531.
152. Donald E. Knuth, Permutations, matrices, and generalized Young tableaux, Paciﬁc
J. Math. 34 (1970), 709–727.
153. , Notes on generalized Dedekind sums, Acta Arith. 33 (1977), no. 4, 297–325.
154. , The Art of Computer Programming. Vol. 2, second ed., Addison-Wesley
Publishing Co., Reading, Mass., 1981.
155. Matthias K¨oppe, A primal Barvinok algorithm based on irrational decompositions,
SIAM J. Discrete Math. 21 (2007), no. 1, 220–236, arXiv:math.CO/0603308. Software
LattE macchiato available at http://www.math.ucdavis.edu/ mkoeppe/latte/.
156. Thomas W. K¨orner, Fourier Analysis, Cambridge University Press, Cambridge, 1988.
157. Maximilian Kreuzer and Harald Skarke, Classiﬁcation of reﬂexive polyhedra
in three dimensions, Adv. Theor. Math. Phys. 2 (1998), no. 4, 853–871,
arXiv:hep-th/9805190.
158. , Complete classiﬁcation of reﬂexive polyhedra in four dimensions, Adv. Theor.
Math. Phys. 4 (2000), no. 6, 1209–1230, arXiv:hep-th/0002240.

274 References

159. Jean B. Lasserre, Moments, positive polynomials and their applications, Imperial
College Press Optimization Series, vol. 1, Imperial College Press, London, 2010.
160. Jean B. Lasserre and Eduardo S. Zeron, On counting integral points in a convex
rational polytope, Math. Oper. Res. 28 (2003), no. 4, 853–870.
161. Jim Lawrence, Valuations and polarity, Discrete Comput. Geom. 3 (1988), no. 4,
307–324.
162. , Polytope volume computation, Math. Comp. 57 (1991), no. 195, 259–271.
163. , A short proof of Euler’s relation for convex polytopes, Canad. Math. Bull.
40 (1997), no. 4, 471–474.
164. Arjen K. Lenstra, Hendrik W. Lenstra, Jr., and L´aszl´o Lov´asz, Factoring polynomials
with rational coeﬃcients, Math. Ann. 261 (1982), no. 4, 515–534.
165. Eva Linke, Rational Ehrhart quasi-polynomials, J. Combin. Theory Ser. A 118 (2011),
no. 7, 1966–1978, arXiv:1006.5612.
166. L´aszl´o Lov´asz, Combinatorial Problems and Exercises, second ed., North-Holland
Publishing Co., Amsterdam, 1993.
167. Ian G. Macdonald, Polynomials associated with ﬁnite cell-complexes, J. London Math.
Soc. (2) 4 (1971), 181–192.
168. Percy A. MacMahon, Combinatory Analysis, Chelsea Publishing Co., New York, 1960,
reprint of the 1915 original.
169. Evgeny N. Materov, The Bott formula for toric varieties, Mosc. Math. J. 2 (2002),
no. 1, 161–182, arXiv:math.AG/9904110.
170. Tyrrell B. McAllister and Kevin M. Woods, The minimum period of the Ehrhart
quasi-polynomial of a rational polytope, J. Combin. Theory Ser. A 109 (2005), no. 2,
345–352, arXiv:math.CO/0310255.
171. Peter McMullen, On zonotopes, Trans. Amer. Math. Soc. 159 (1971), 91–109.
172. , Valuations and Euler-type relations on certain classes of convex polytopes,
Proc. London Math. Soc. (3) 35 (1977), no. 1, 113–135.
173. , Lattice invariant valuations on rational polytopes, Arch. Math. (Basel) 31
(1978/79), no. 5, 509–516.
174. Peter McMullen and Geoﬀrey C. Shephard, Diagrams for centrally symmetric poly-
topes, Mathematika 15 (1968), 123–138.
175. Curt Meyer, ¨Uber einige Anwendungen Dedekindscher Summen, J. Reine Angew.
Math. 198 (1957), 143–203.
176. Jeﬀrey L. Meyer, Character analogues of Dedekind sums and transformations of
analytic Eisenstein series, Paciﬁc J. Math. 194 (2000), no. 1, 137–164.
177. Werner Meyer and Robert Sczech, ¨Uber eine topologische und zahlentheoretische An-
wendung von Hirzebruchs Spitzenauﬂ¨osung, Math. Ann. 240 (1979), no. 1, 69–96.
178. Ezra Miller and Bernd Sturmfels, Combinatorial Commutative Algebra, Graduate
Texts in Mathematics, vol. 227, Springer-Verlag, New York, 2005.
179. Hermann Minkowski, Geometrie der Zahlen, Bibliotheca Mathematica Teubneriana,
Band 40, Johnson Reprint Corp., New York, 1968.
180. Marcel Morales, Syzygies of monomial curves and a linear Diophantine problem of
Frobenius, Preprint, Max-Planck-Institut f¨ur Mathematik, Bonn, 1986.
181. , Noetherian symbolic blow-ups, J. Algebra 140 (1991), no. 1, 12–25.
182. Louis J. Mordell, Lattice points in a tetrahedron and generalized Dedekind sums, J.
Indian Math. Soc. (N.S.) 15 (1951), 41–46.
183. Robert Morelli, Pick’s theorem and the Todd class of a toric variety, Adv. Math.
100 (1993), no. 2, 183–231.
184. Gerald Myerson, On semiregular ﬁnite continued fractions, Arch. Math. (Basel) 48
(1987), no. 5, 420–425.
185. Walter Nef, Zur Einf¨uhrung der Eulerschen Charakteristik, Monatsh. Math. 92
(1981), no. 1, 41–46.
186. Benjamin Nill and Andreas Paﬀenholz, On the equality case in Ehrhart’s volume
conjecture, Adv. Geom. 14 (2014), no. 4, 579–586, arXiv:1205.1270.

References 275

187. C. D. Olds, Anneli Lax, and Giuliana P. Davidoﬀ, The Geometry of Numbers, An-
neli Lax New Mathematical Library, vol. 41, Mathematical Association of America,
Washington, DC, 2000.
188. Paul C. Pasles, The lost squares of Dr. Franklin: Ben Franklin’s missing squares and
the secret of the magic circle, Amer. Math. Monthly 108 (2001), no. 6, 489–511.
189. Sam Payne, Ehrhart series and lattice triangulations, Discrete Comput. Geom. 40
(2008), no. 3, 365–376, arXiv:math/0702052.
190. Micha A. Perles and Geoﬀrey C. Shephard, Angle sums of convex polytopes, Math.
Scand. 21 (1967), 199–218.
191. Georg Alexander Pick, Geometrisches zur Zahlenlehre, Sitzenber. Lotos (Prague) 19
(1899), 311–319.
192. Cliﬀord A. Pickover, The Zen of Magic Squares, Circles, and Stars, Princeton Uni-
versity Press, Princeton, NJ, 2002.
193. Christopher Polis, Pick’s theorem extended and generalized, Math. Teacher (1991),
399–401.
194. James E. Pommersheim, Toric varieties, lattice points and Dedekind sums, Math.
Ann. 295 (1993), no. 1, 1–24.
195. Bjorn Poonen and Fernando Rodriguez-Villegas, Lattice polygons and the number 12,
Amer. Math. Monthly 107 (2000), no. 3, 238–250.
196. Tiberiu Popoviciu, Asupra unei probleme de patitie a numerelor, Acad. Republicii
Populare Romane, Filiala Cluj, Studii si cercetari stiintiﬁce 4 (1953), 7–58.
197. Alexander Postnikov, Permutohedra, associahedra, and beyond, Int. Math. Res. Not.
(2009), no. 6, 1026–1106, arXiv:math/0507163.
198. Hans Rademacher, Generalization of the reciprocity formula for Dedekind sums, Duke
Math. J. 21 (1954), 391–397.
199. , Some remarks on certain generalized Dedekind sums, Acta Arith. 9 (1964),
97–105.
200. Hans Rademacher and Emil Grosswald, Dedekind Sums, The Mathematical Associa-
tion of America, Washington, D.C., 1972.
201. Jorge L. Ram´ırez Alfons´ın, Complexity of the Frobenius problem, Combinatorica 16
(1996), no. 1, 143–147.
202. , The Diophantine Frobenius Problem, Oxford Lecture Series in Mathematics
and its Applications, vol. 30, Oxford University Press, Oxford, 2005.
203. J. E. Reeve, On the volume of lattice polyhedra, Proc. London Math. Soc. (3) 7 (1957),
378–395.
204. Les Reid and Leslie G. Roberts, Monomial subrings in arbitrary dimension, J. Alge-
bra 236 (2001), no. 2, 703–730.
205. Jason M. Ribando, Measuring solid angles beyond dimension three, Discrete Comput.
Geom. 36 (2006), no. 3, 479–487.
206. Adrian Rice, Brought to book: the curious story of Guglielmo Libri (1803–69), Euro-
pean Mathematical Society Newsletter 48 (2003), 12–14.
207. J¨urgen Richter-Gebert, Realization spaces of polytopes, Lecture Notes in Mathemat-
ics, vol. 1643, Springer-Verlag, Berlin Heidelberg, 1996.
208. Bjarke Hammersholt Roune, Solving thousand-digit Frobenius problems using
Gr¨obner bases, J. Symbolic Comput. 43 (2008), no. 1, 1–7, arXiv:math/0702040.
209. Boris Y. Rubinstein, Expression for restricted partition function through Bernoulli
polynomials, Ramanujan J. 15 (2008), no. 2, 177–185.
210. Steven V Sam, A bijective proof for a theorem of Ehrhart, Amer. Math. Monthly 116
(2009), no. 8, 688–701, arXiv:0801.4432v5.
211. Jan Schepers and Leen Van Langenhoven, Unimodality questions for integrally closed
lattice polytopes, Ann. Comb. 17 (2013), no. 3, 571–589, arXiv:math/1110.3724.
212. Ludwig Schl¨aﬂi, Theorie der vielfachen Kontinuit¨at, Ludwig Schl¨aﬂi, 1814–1895,
Gesammelte Mathematische Abhandlungen, Vol. I, Birkh¨auser, Basel, 1950, pp. 167–
387.

276 References

213. Pieter Hendrik Schoute, Analytic treatment of the polytopes regularly derived from
the regular polytopes, Verhandelingen der Koninklijke Akademie von Wetenschappen
te Amsterdam 11 (1911), no. 3.
214. Alexander Schrijver, Combinatorial Optimization. Polyhedra and Eﬃciency. Vol. A–
C, Algorithms and Combinatorics, vol. 24, Springer-Verlag, Berlin, 2003.
215. Paul R. Scott, On convex lattice polygons, Bull. Austral. Math. Soc. 15 (1976), no. 3,
395–399.
216. Sinan Sert¨oz, On the number of solutions of the Diophantine equation of Frobenius,
Diskret. Mat. 10 (1998), no. 2, 62–71.
217. Jeﬀrey Shallit, The Frobenius problem and its generalizations, Developments in lan-
guage theory, Lecture Notes in Comput. Sci., vol. 5257, Springer, Berlin, 2008, pp. 72–
83.
218. Jeﬀrey Shallit and James Stankewicz, Unbounded discrepancy in Frobenius numbers,
Integers 11 (2011), A2, 8 pp.
219. Geoﬀrey C. Shephard, An elementary proof of Gram’s theorem for convex polytopes,
Canad. J. Math. 19 (1967), 1214–1217.
220. , Combinatorial properties of associated zonotopes, Canad. J. Math. 26 (1974),
302–321.
221. Carl Ludwig Siegel, Lectures on the Geometry of Numbers, Springer-Verlag, Berlin,
1989, Notes by B. Friedman, rewritten by Komaravolu Chandrasekharan with the
assistance of Rudolf Suter, with a preface by Chandrasekharan.
222. R. Jamie Simpson and Robert Tijdeman, Multi-dimensional versions of a theorem
of Fine and Wilf and a formula of Sylvester, Proc. Amer. Math. Soc. 131 (2003),
no. 6, 1661–1671.
223. David Solomon, Algebraic properties of Shintani’s generating functions: Dedekind
sums and cocycles on PGL2(Q), Compositio Math. 112 (1998), no. 3, 333–362.
224. Duncan M. Y. Sommerville, The relation connecting the angle-sums and volume of
a polytope in space of n dimensions, Proc. Roy. Soc. London, Ser. A 115 (1927),
103–119.
225. Richard P. Stanley, Linear homogeneous Diophantine equations and magic labelings
of graphs, Duke Math. J. 40 (1973), 607–632.
226. , Combinatorial reciprocity theorems, Advances in Math. 14 (1974), 194–253.
227. , Decompositions of rational convex polytopes, Ann. Discrete Math. 6 (1980),
333–342.
228. , On the Hilbert function of a graded Cohen–Macaulay domain, J. Pure Appl.
Algebra 73 (1991), no. 3, 307–314.
229. , A zonotope associated with graphical degree sequences, Applied geometry and
discrete mathematics, DIMACS Ser. Discrete Math. Theoret. Comput. Sci., vol. 4,
Amer. Math. Soc., Providence, RI, 1991, pp. 555–570.
230. , Combinatorics and Commutative Algebra, second ed., Progress in Mathe-
matics, vol. 41, Birkh¨auser Boston Inc., Boston, MA, 1996.
231. , Enumerative Combinatorics. Volume 1, second ed., Cambridge Studies in
Advanced Mathematics, vol. 49, Cambridge University Press, Cambridge, 2012.
232. , How the Upper Bound Conjecture Was Proved, Ann. Comb. 18 (2014), no. 3,
533–539.
233. Alan Stapledon, Additive number theory and inequalities in Ehrhart theory, Preprint
(arXiv:0904.3035v2).
234. , Weighted Ehrhart theory and orbifold cohomology, Adv. Math. 219 (2008),
no. 1, 63–88, arXiv:math/0711.4382.
235. , Inequalities and Ehrhart δ-vectors, Trans. Amer. Math. Soc. 361 (2009),
no. 10, 5615–5626, arXiv:math/0801.0873.
236. Bernd Sturmfels, On vector partition functions, J. Combin. Theory Ser. A 72 (1995),
no. 2, 302–309.
237. , Gr¨obner Bases and Convex Polytopes, University Lecture Series, vol. 8,
American Mathematical Society, Providence, RI, 1996.

References 277

238. James J. Sylvester, On the partition of numbers, Quaterly J. Math. 1 (1857), 141–152.
239. , On subinvariants, i.e. semi-invariants to binary quantics of an unlimited
order, Amer. J. Math. 5 (1882), 119–136.
240. , Mathematical questions with their solutions, Educational Times 41 (1884),
171–178.
241. Andr´as Szenes and Mich`ele Vergne, Residue formulae for vector partitions and
Euler–Maclaurin sums, Adv. in Appl. Math. 30 (2003), no. 1–2, 295–342,
arXiv:math.CO/0202253.
242. Lajos Tak´acs, On generalized Dedekind sums, J. Number Theory 11 (1979), no. 2,
264–272.
243. Audrey Terras, Fourier Analysis on Finite Groups and Applications, London Math-
ematical Society Student Texts, vol. 43, Cambridge University Press, Cambridge,
1999.
244. John A. Todd, The geometrical invariants of algebraic loci, Proc. London Math. Soc.
43 (1937), 127–141.
245. , The geometrical invariants of algebraic loci (second paper), Proc. London
Math. Soc. 45 (1939), 410–424.
246. Amitabha Tripathi, The number of solutions to ax + by = n, Fibonacci Quart. 38
(2000), no. 4, 290–293.
247. , On the Frobenius problem for geometric sequences, Integers 8 (2008), A43,
5 pp.
248. , On the Frobenius problem for {ak, ak + 1, ak + a, . . . , ak + ak−1}, Integers
10 (2010), A44, 523–529.
249. Helge Tverberg, How to cut a convex polytope into simplices, Geometriae Dedicata
3 (1974), 239–240.
250. Alexander N. Varchenko, Combinatorics and topology of the arrangement of aﬃne
hyperplanes in the real space, Funktsional. Anal. i Prilozhen. 21 (1987), no. 1, 11–22.
251. Sven Verdoolaege, Software package barvinok, (2004), electronically available at
http://freshmeat.net/projects/barvinok/.
252. John von Neumann, A certain zero-sum two-person game equivalent to the optimal
assignment problem, Contributions to the Theory of Games, vol. 2, Annals of Mathe-
matics Studies, no. 28, Princeton University Press, Princeton, N. J., 1953, pp. 5–12.
253. Herbert S. Wilf, generatingfunctionology, second ed., Academic Press Inc., Boston,
MA, 1994, electronically available at
http://www.math.upenn.edu/∼wilf/DownldGF.html.
254. Kevin Woods, Computing the period of an Ehrhart quasi-polynomial, Electron. J.
Combin. 12 (2005), no. 1, Research Paper 34, 12 pp.
255. Guoce Xin, Constructing all magic squares of order three, Discrete Math. 308 (2008),
no. 15, 3393–3398, arXiv:math.CO/0409468.
256. Don Zagier, Higher dimensional Dedekind sums, Math. Ann. 202 (1973), 149–172.
257. Claudia Zaslavsky, Africa Counts, Prindle, Weber & Schmidt, Inc., Boston, Mass.,
1973.
258. Doron Zeilberger, Proof of a conjecture of Chan, Robbins, and Yuen, Electron. Trans.
Numer. Anal. 9 (1999), 147–148.
259. G¨unter M. Ziegler, Lectures on Polytopes, Springer-Verlag, New York, 1995.

List of Symbols

The following table contains a list of symbols that are frequently used through-
out the book. The page numbers refer to the ﬁrst appearance/deﬁnition of
each symbol.

Symbol Meaning Page
ˆa(m) Fourier coeﬃcient of a(n) 137
A (d, k) Eulerian number 30
A
⊥ orthogonal complement of A 210
AP (t) solid-angle sum of P 229
αP (z) solid-angle generating function 231
Bk(x) Bernoulli polynomial 34
Bk Bernoulli number 34
Bn Birkhoﬀ polytope 116
BiPyr (P) bipyramid over P 39
cone P cone over P 63
const f constant term of the generating function f 14
conv S convex hull of S 27
d-cone d-dimensional cone 62
d-polytope d-dimensional polytope 28
dim P dimension of P 28
δm(x) delta function 140
EhrP (z) Ehrhart series of P 30
EhrP ◦ (z) Ehrhart series of the interior of P 93
ea(x) root-of-unity function e2πiax/b 140
fk face number 101
Fk(t) lattice-point enumerator of the k-skeleton 103
F(f ) Fourier transform of f 139
g (a1, a2, . . . , ad) Frobenius number 6
h
∗
P (z) h
∗-polynomial of P 72
Hn(t) number of semimagic n × n squares with line sum t 115

279

280 List of Symbols

Symbol Meaning Page
KF tangent cone of F ⊆ P 204
LP (t) lattice-point enumerator of P 29
LP ◦ (t) lattice-point enumerator of the interior of P 30
Mn(t) number of magic n × n squares with line sum t 115
N (p(z1, z2, . . . , zd)) Newton polytope of p(z1, z2, . . . , zd) 167
ωP (x) solid angle of x (with respect to P) 227
pA(n) restricted partition function 6
polyA(n) polynomial part of pA(n) 151
P a closed polytope 27
P ◦ interior of the polytope P 30
P1 + P2 + · · · + Pn Minkowski sum of P1, P2, . . . , Pn 167
P(h) perturbed polytope 221
Pyr (P) pyramid over P 36
℘(z) Weierstraß ℘-function 243
Π fundamental parallelepiped of a cone 66
rn(a, b) Dedekind–Rademacher sum 155
s(a, b) Dedekind sum 138
sn (a1, a2, . . . , am; b) Fourier–Dedekind sum 15
SolidP (x) solid-angle series 236
span P aﬃne space spanned by P 28
σS(z) integer-point transform of S 64
tP tth dilation of P 29
Toddh Todd operator 214
vol P (continuous) volume of P 76
VG vector space of all complex-valued functions 139
on G = {0, 1, 2, . . . , b − 1}
ξa root of unity e2πi/a 8
ζ(z) Weierstraß ζ-function 243
Z(u1, u2, . . . , un) zonotope spanned by u1, u2, . . . , un 168
[x, y] line segment joining x and y ∈ Rd 12
⌊x⌋ greatest integer function 10
{x} fraction-part function 10
((x)) sawtooth function 137
zc zc1
1 zc2
2 · · · zcm
m 50(m
n ) binomial coeﬃcient 30
⟨f, g⟩ inner product of f and g 140
(f ∗ g)(t) convolution of f and g 143
1S(x) characteristic function of S 205
#S number of elements in S 6
♣ an exercise that is used in the text 5

Index

acyclotope, 181
aﬃne space, 28
aﬃne span, 107
algebra, 51
angle sum in a triangle, 234
apex, 62, 204
area, 40
arithmetic matroid, 179
arithmetic Tutte polynomial, 179
arrangement of hyperplanes, 85, 201

Barlow–Popoviciu formula, 11
Barvinok’s algorithm, 161, 209
basis, 140
Beatty sequence, 22
Bernoulli number, 34, 54, 214
Bernoulli polynomial, 34, 55, 151, 224
Bernoulli–Barnes polynomial, 151, 247
binomial coeﬃcient, 30, 74
binomial series, 33, 73
binomial transform, 225
bipyramid over a polytope, 39
Birkhoﬀ–von Neumann polytope, 116, 126,
180
Boolean lattice, 102, 263
boundary, 105
boundary triangulation, 184
Brianchon–Gram relation
for indicator functions, 205
for solid angles, 234
Brion’s theorem, 207
continuous form of, 216
for solid angles, 231

Carlitz polynomial, 164
Catalan number, 82
centrally symmetric, 170
 complex conjugation, 140
cone, 62, 201, 249
pointed, 62
rational, 201
simplicial, 63
unimodular, 221
coning over a polytope, 63, 69, 80
constant term, 8, 14, 45, 124, 152, 158
constituent, 47, 125
contingency table, 126
continuous Fourier transform, 145
continuous volume, 76, 106, 116, 230
convex hull, 27
convex polygon, 27
convex polytope, 27, 51, 249
convolution
of ﬁnite Fourier series, 143
of quasipolynomials, 87
cotangent, 138
cross-polytope, 38, 52
cube, 29
cyclotomic polynomial, 147

d-polytope, 28
decomposition
of h∗, 188
of a polytope into cones, 206
of a zonotope, 171
palindromic, 189
Dedekind η-function, 160
Dedekind sum, 138, 142, 150, 158
Dedekind’s reciprocity law, 153
Dedekind–Rademacher sum, 155
degenerate hyperplane, 28
degree
of a polytope, 94, 192
of a quasipolynomial, 47
 281

282 Index

degree sequence, 181
Dehn–Sommerville relations, 101, 110, 184
Delannoy path, 56
delta function, 140
Delzant polytope, 221
denominator, 80
dihedral angle, 228
dilate, 7, 29
dimension
of a pointed cone, 63
of a polytope, 28
discrete volume, 29, 32, 38, 78, 89, 229
distance, 140
doubly periodic function, 243
doubly stochastic matrix, 116
dual polytope, 97, 110

edge
of a pointed cone, 64
of a polytope, 28
Ehrhart polynomial, 68, 72, 94, 105, 158
constant term of, 74
interpolation of, 78
leading coeﬃcient of, 77
of a zonotope, 176
second coeﬃcient of, 108
Ehrhart quasipolynomial, 80
Ehrhart series, 30, 51, 72, 93, 159, 183
Ehrhart’s theorem, 68, 80, 117
Ehrhart–Macdonald reciprocity, 90, 102,
117, 155
empty simplex, 187
Erd˝os–Gallai theorem, 181
Euclidean algorithm, 25, 153
Euler φ-function, 147
Euler characteristic, 82
Euler relation, 102
Euler–Maclaurin summation, 213
Eulerian number, 30, 51
exponential function, 214

face
lattice, 102
number, 101
of a pointed cone, 64
of a polytope, 28
visible, 210
facet
of a pointed cone, 64
of a polytope, 28
visible, 196
Farey sequence, 56
Fibonacci sequence, 3, 162
ﬁnite Fourier series, 133
 ﬁnite Fourier transform, 139
ﬁnite geometric series, 19, 141, 199
forest, 174
Fourier coeﬃcient, 136
Fourier transform, 139
Fourier–Dedekind sum, 15, 149
Fourier–Laplace transform, 218
fractional-part function, 10, 20, 137
free sum, 97
frequency, 137
Frobenius number, 6
Frobenius problem, 3
fundamental parallelepiped, 66, 187, 217

Gauß sum, 148
gcd algorithm, 153
generalized permutahedron, 178
generating function, 3, 8, 14, 30, 65, 68,
119
constant term of, 8, 14, 45, 124, 158
multivariate, 49
rational, 64, 199
generator of a pointed cone, 63
geometric series, 4, 19, 66, 134
geometry of numbers, 181
Gorenstein polytope, 98
graded algebra, 51
graph, 102, 129, 174, 196
graphical zonotope, 181
greatest-integer function, 10, 19, 89, 137

h-cone, 249
h∗-polynomial, 72, 183
half-space, 28
hemisphere, 178
Hibi’s palindromic theorem, 95
Hilbert–Poincar´e series, 51
hyperplane, 28, 63
degenerate, 28
rational, 85
hyperplane arrangement, 85, 180, 201
central, 201
rational, 201
hyperplane description, 28, 51, 249
hypersimplex, 85

indicator function, 205
induced triangulation, 184
inﬁnite sequence, 3
inner product, 140, 146
integer decomposition property, 192
integer-point transform, 64, 69, 90, 199
of a simplicial cone, 66
integral polygon, 40

Index 283

integral polytope, 28, 68, 108, 236
integrally closed, 192
interior, 30, 89, 93
relative, 102, 117, 228
interpolation, 77, 117
interval, 27
isolated singularity, 241

Jacobi symbol, 160

k-skeleton, 103
Khovanski˘ı–Pukhlikov theorem, 221

labeled degree sequence, 181
Lagrange interpolation formula, 78
Laguerre polynomial, 52
Latin square, 126
lattice, 7, 27, 81, 246
lattice basis, 22
lattice point, 7, 27, 35, 64
lattice-point enumerator, 29, 48
Laurent monomial, 64
Laurent series, 8, 241
line segment, 12, 21, 28, 89, 167, 199
line shelling, 196
linear Diophantine problem of Frobenius, 6
linear map, 84, 202
link, 187
local Riemann hypothesis, 52
lower face, 60
lower hull, 60, 184
Luo Shu square, 114

magic square, 114
traditional, 114
magic sum, 113
Mahler’s conjecture, 100
matrix
doubly stochastic, 116
unimodular, 88, 181
matroid, 179
metric space, 140
Minkowski sum, 167
Minkowski’s fundamental theorem, 181
M¨obius function, 147
module, 201
moment, 218
moment generating function, 65
monomial moment, 218

Newton polytope, 167
northeast lattice path, 22

octahedron, 38
 order polytope, 51
orthogonal complement, 210
orthogonality relations, 141

palindromicity
of the Ehrhart series of a reﬂexive
polytope, 95
of the Ehrhart series of the Birkhoﬀ–von
Neumann polytope, 117
of the solid-angle generating function,
236
parallelepiped, 66, 167
fundamental, 66, 187
Parseval identity, 141
part of a partition, 7
partial fractions, 4, 8, 14, 45, 134, 151, 158
partition, 7
period, 47, 80
periodic function, 47, 133, 139
periodic sequence, 135
permutahedron, 172
generalized, 178
permutation matrix, 116
perturbation, 221
Pick’s theorem, 40, 245
Plancherel theorem, 141
pointed cone, 62, 201
rational, 62
polar polytope, 97, 110
polygon, 27
integral, 40
rational, 43, 47
polyhedron, 28, 201
polynomial, 30, 33, 36, 42, 68, 75, 77, 84,
108, 117, 145, 199
interpolation of, 78, 117
polytope, 7, 27, 249
centrally symmetric, 170
Delzant, 221
dual, 97, 110
Gorenstein, 98
integral, 28, 68, 108, 236
integrally closed, 192
Newton, 167
polar, 97, 110
rational, 28, 48, 80, 230
simple, 101, 196, 216
simplicial, 110, 183
smooth, 221
unimodular, 221
power series, 8
primitive root of unity, 147
pyramid, 35, 51, 235
over a polytope, 36

284 Index

quasipolynomial, 47, 80, 86, 124, 230
constituent of, 47, 125
degree of, 47
period of, 47, 80

Rademacher reciprocity, 155
rational cone, 201
rational generating function, 64, 199
short, 209
rational pointed cone, 62
rational polygon, 43, 47
rational polytope, 28, 48, 80, 230
reciprocity law
for the Carlitz polynomial, 164
for the classical Dedekind sum, 153
for the Dedekind–Rademacher sum, 155
for the Fourier–Dedekind sum, 152, 154
reciprocity theorem
for integer-point transforms, 92
for lattice-point enumeration, 90
for solid-angle generating functions, 231
for solid-angle sums, 232
regular tetrahedron, 54, 238
regular triangulation, 60, 184
relative interior, 102, 117, 228
relative volume, 107
representable, 6
residue, 241
residue theorem, 242
restricted partition function, 6, 14, 151
polynomial part of, 151, 247
rhombic dodecahedron, 169
Riemann zeta function, 34
root, 75
root of unity, 8
primitive, 147

sawtooth function, 137, 156
semigroup, 84
semimagic square, 114
symmetric, 128
shelling, 109, 195
line, 196
short rational generating function, 209
simple polytope, 101, 196, 216
simplex, 28, 59, 80
empty, 187
faces of, 53
standard, 31, 185, 228
unimodular, 185
simplicial
cone, 63
polytope, 110, 183
skeleton, 103
 slack variable, 32, 44, 48
Smith normal form, 176
smooth polytope, 221
solid angle, 227
generating function, 231
of a face, 228
polynomial, 234
series, 236
sum of, 229
standard simplex, 31, 185, 228
Stanley’s nonnegativity theorem, 72
Stanley’s reciprocity theorem, 92
Stirling number of the ﬁrst kind, 33, 54
sublattice, 107
supporting hyperplane, 28, 63
Sylvester’s theorem, 6
symmetric about the origin, 170
symmetric semimagic square, 128

tangent cone, 204
tetrahedron, 28, 158
Todd operator, 214, 221
toric variety, 51, 224
traditional magic square, 114
transportation polytope, 126
tree, 176
triangle, 22, 28, 43
triangulation
boundary, 184
induced, 184
of a pointed cone, 64
of a polygon, 41
of a polytope, 59
regular, 60, 184
unimodular, 185
trigonometric identities, 144
trivial, 123
Tutte polynomial, 179

unimodal, 127, 197
unimodular
cone, 221
group, 88
matrix, 88
polytope, 221
simplex, 185
triangulation, 185
unit cube, 29, 35, 169
unit vector, 31
unitary transformation, 146
unlabeled degree sequence, 181

v-cone, 249
valuation, 237

Index 285

Vandermonde matrix, 85, 173
vector partition function, 52
vector space, 139
vertex, 28, 127
vertex cone, 204
vertex description, 27, 51, 249
vertex ﬁgure, 184
visible, 60, 196, 210
volume, 29, 76, 89, 116, 221, 230
relative, 106
 Weierstraß ℘-function, 243
Weierstraß ζ-function, 243

Zagier reciprocity, 152
zero, 234
zonotopal decomposition, 171
zonotope, 169
graphical, 181
history, 178
