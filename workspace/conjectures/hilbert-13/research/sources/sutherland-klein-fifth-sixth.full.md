<!-- source: https://arxiv.org/pdf/1911.02358 | converted from PDF -->

arXiv:1911.02358v1  [math.HO]  4 Nov 2019”About the Solution of the General Equations of
Fifth and Sixth Degree (Excerpt from a letter to
Mr. K. Hensel.)”∗

English Translation of ” ¨Uber die Auﬂ¨osung der
allgemeinen Gleichungen f¨unften und sechsten
Grades (Auszug aus einem Schreiben an Herrn K.
Hensel)” †

Original Author: Felix Klein
Translation: Alex Sutherland

Original Year of Publication: 1905
Year of Translation: 2019

First appeared in the Dirichletbande (Vol. 129) of the
Journal for Pure and Applied Mathematics (1905).
Reprinted in the Math. Annalen, Vol. 61 (1905).

There are a few footnotes added to this translation, that may add extra insight
or clariﬁcation to the reader. All of these footnotes begin with ”Translator’s
Note:”.
 Here is a link to the original paper.

∗Printed from the Dirichletbande (Bd. 129) of the Journal for Pure and Applied Mathe-
matics.
†Abgedruckt aus dem Dirichletbande (Bd. 129) des Journals f¨ur reine und angewandte
Matiiematik.
 1

1 Introduction

From,

Felix Klein in G¨ottingen.

By responding to your earnest request to contribute to the journal’s book
dedicated to the memory of Dirichlet, I refer to a note I published six years
ago in the Rendiconti dell’Accademia dei Lincei [9], and in which I outlined a
general solution of equations of sixth degree.

I set myself the goal of explaining in more detail and in more concrete terms
what was suggested there. In fact, even an expert of the relevant literature
(such as Mr. Lachtin) has not taken the approach in question in its simplicity
(as I will explain more below). 1

Moreover, I act under the impulses of my old friend Mr. Gordan, who has
recently turned his great algebraic ability to the problem in question. Mr. Gor-
dan will soon publish a ﬁrst relevant treatise in the Math. Annalen [7] 2. But
this is only a beginning; I hope that his continued eﬀorts will succeed in clarify-
ing the subject in every respect as fully as we have been able to do in the past
with the theory of equations of the ﬁfth degree.

I would like to discuss this theory of the equations of the ﬁfth degree in
advance, as I summarized them in my ”Lectures on the Icosahedron” [13], in
such a way that I bring forth those moments which are generalized when dealing
with the considerations of the sixth degree. In Chapter V of these Lectures, I
have dealt with two methods for solving equations of the ﬁfth degree (which,
incidentally, diﬀer only by the order in which the steps are carried out) and the
second of these methods will prove to be the natural continuation of Kronecker’s
(and Brioschi’s) method. This method, like the ﬁrst one, is developed in ge-
ometric form, with special relations that emerge only in equations of the ﬁfth
degree. Instead, I refer here to the algebraic justiﬁcation developed in Volume
15 of the Math. Annalen [11] and accompanied with reﬂections on the solution
of arbitrary higher equations. 3

The icosahedral theory of the equations of the ﬁfth degree and the general
considerations connected with it have since been portrayed several times by
others, especially in the second volume of the excellent textbook on algebra by
Mr. Weber [19], as well as in the detailed report that Mr. Wiman has made

11901, Moscow Mathematical Collection, Vol. XXLI, pp. 181-218 (Russian)

2A contribution to the solution of the general equations of the sixth degree. Compare with
a message to the Heidelberg International Congress of Mathematics

3In particular, see Section 4 - ”The formulas of Kronecker and Brioschi for the ﬁfth degree”

2

in Volume I of the Encyclopedia of Mathematical Sciences [22]. Nevertheless,
it seems that the basic meaning of the whole approach in the mathematical
audience is still often not understood. It is not a matter of considerations which
are to the sides of the earlier investigations on the solution of equations of the
ﬁfth degree, but of those which claim to constitute the very core of these earlier
investigations. Accordingly, in the following report, I will try to describe the
main points of the theory (which will later be found mutatis mutandis in the
approach to the equations of the sixth degree) as accurately as possible while
maintaining brevity.

The ﬁrst is that we have the icosahedral equation, i.e. the equation of the
sixtieth degree, which is written in the above Lectures as follows:

H 3(x)
1728f 5(x) = X (1)

as a Normalgleichung sui generis (Normal General Equation) which, by virtue
of their excellent qualities, is the next generalization of the ”pure” equations:

x
n = X. (2)

In fact, given any root of (1), the 60 roots of (1) can be calculated by the 60
linear equations that are already known (the icosahedral substitutions), just as
the n roots of (2) can be found from any one of them by the n substitutions
given by x
′ = e 2πik
n x. Now, the group of icosahedral substitutions proves to be
isomorphic with the group of 60 alternating permutations on ﬁve letters (i.e.
A5). In this way, it is impossible to trace the solution of the general equations
of the ﬁfth degree back to a sequence of pure equations (2). The task is thus to
solve the equations of the ﬁfth degree with the help of an icosahedral equation.
Here we distinguish an algebraic and a transcendental part of the investigation.
The ﬁrst part will deal with the algebraic construction of a root x of an icosahe-
dral equation (1) from the roots z1, . . . , z5 of a given ﬁfth degree equation - the
parameter X of (1) is determined by the coeﬃcients of the ﬁfth degree equa-
tion. We ﬁrst calculate the square root of the discriminant of the ﬁfth degree
equation in terms of the z1, . . . , z5. The transcendental part is to calculate the
root x of the icosahedral equation from the parameter X by inﬁnite processes.
This is due to the hypergeometric series, as well as the transcendental solution
of equation (2) by the binomial series. In the ”Lectures on the Icosahedron,”
it has been shown, in particular, that all algebraic investigations which have
been made for the purpose of solving the general equations of the ﬁfth degree
are reenactments of the aforementioned algebraic problem. The transcendental
part of the task is only barely touched. It is clearly stated, however, what the
connection is with the so-called ’solution of the equations of the ﬁfth degree by
elliptic functions.’ I refer here to my other detailed explanations in the ”Lec-
tures on the Theory of Elliptic Modular Functions” [14], edited by Fricke and
myself. There is a necessary connection between the ﬁfth order transformation
of the elliptic functions and the theory of the icosahedron. In (1), substituting

3

J (the absolute invariant of an elliptic modular function for X), the variable x
gets the meaning of the ”principal modular function of the principal congruence
group of the ﬁfth degree.”4

All modes of relating the solution of the ﬁfth degree equations to the elliptic
functions are based on this fundamental theorem. In particular, x can be rep-
resented by elliptic theta functions; it is a formula of principled simplicity, you
have (if I may use Jacobi notation for the sake of brevity):

x = q 2
5 θ1 ( 2iK ′π
K , q5)

θ1 ( iK ′π
K , q5) (3)

However, the use of this formula to solve the icosahedral equation (or similar
formulas for solving any resolvents of the Icosahedral equation) is just as much
a detour as the solution of the pure equation (2) by logarithms:

x = e 1
n log(X) (4)

You have to ﬁrst calculate K ′
K , respectively, by calculating log(X) from X be-
fore applying formulas (3),(4). The meaning of the formulas for the solution is
at most a practical one, namely if one has a logarithm table of elliptic periods
K, K ′. Thus, we can ﬁnally realize that the use of elliptic functions is not the
essence of the theory of equations of the ﬁfth degree. This mode of expression
via elliptic functions is only a residue of accidental historical development: the
transformation theory of functions has given the ﬁrst approach to establishing
certain simple equations closely related to the icosahedral equation, namely the
modular equations and multiplier equations for the ﬁfth degree transformation.

So much for the introduction of the icosahedron into the theory of the ﬁfth
degree in general. I now have to limit myself to the algebraic side of the task.
And here, above all else, I have to mention a fundamental proposition about the
icosahedral substitutions, which becomes particularly important in what follows.
One can pass from the icosahedral substitutions of the variable x appearing in
(1) to homogeneous substitution formulas (by replacing x in the substitution
formulas everywhere by x1 : x2 and separating numerator and denominator
in an appropriate manner). If one chooses the determinant of the resulting
binary substitutions equal to 1, one has 120 binary substitutions; speciﬁcally, the
identity substitution x
′ = x corresponds to the two homogeneous substitution
formulas
 x
′
1 = x1, x
′
2 = x2 and x
′
1 = −x1, x
′
2 = −x2. (5)

It is not possible in any way (even if you change the value of the determinant),
to assemble from such homogeneous substitutions a group which is isomorphic

4Translator’s Note: The terms ”principal congruence [sub]group of the ﬁfth degree” [of the
modular group] and ”principal modular function” are deﬁned in [14]. See pages 388 and 591
in the original German books, or pages 323 and 475 in the English translation.

4

with the non-homogeneous substitution group (which contains fewer than 120
substitutions). The surjective homomorphism from the substitution group of
the x1 : x2 to the substitution group of the x therefore has a non-trivial kernel.
This fundamental proposition, which is somewhat abstract, gives the algebraic
theory of equations of the ﬁfth degree its peculiar form, as we shall have to
explain at once. Let us note in advance that it is not diﬃcult to prove it. On
pages 46 and 47 of my book on the icosahedron, it is traced back to the fact
that the group of non-homogeneous icosahedral substitutions contains the Klein
four-group and the corresponding proposition already applies to the Klein four-
group. Let us take the following to be the simplest representation of the Klein
four-group as (non-homogeneous) substitutions; it is given by

I : ξ′ = ξ II : ξ′ = −ξ III : ξ′ = 1
ξ IV : ξ′ = − 1
ξ (6)

Here, II, III, and IV are substitutions of order 2 and, at the same time,

II · III · IV = I. (7)

If one now wishes to create an isomorphic group of homogeneous substitutions,
one certainly has a group with

I ′ : ξ′
1 = ξ1, ξ′
2 = ξ2

and replacing II, III, and IV by

II ′ : ξ′
1 = ∓ξ1, ξ′
2 = ±ξ2
III ′ : ξ′
1 = ±ξ2, ξ′
2 = ±ξ1
IV ′ : ξ′
1 = ∓ξ2, ξ′
2 = ±ξ1

(where, in the individual horizontal rows, the upper or lower signs are to be
taken as desired). But, as one must also choose the signs here, the substitutions
II ′, III ′, and IV ′ each have determinant −1 and thus it is impossible that

II ′ · III ′ · IV ′ = I ′

However, this contradicts (7) and no such isomorphism can exist. From now on,
we will understand the homogeneous icosahedral substitutions as the 120 binary
substitutions with determinant +1, corresponding to the 60 non-homogeneous
substitutions of x.
 5

I will now formulate the central problem for which we are responsible:

From the ﬁve independent variables z1, . . . , z5 (the roots of the equation of the
ﬁfth degree), one has to compose a function x(z1, . . . , z5) which gives an
isomorphism from the 60 icosahedral substitutions to the 60 even permutations
of z1, . . . , z5.

From our fundamental proposition, it immediately follows that there is no such
rational function of the ﬁve free variables (Lectures on the Theory of Elliptic
Modular Functions [14], p.255). Namely, by dividing x into coprime polynomials
corresponding to the numerator and denominator; i.e. writing

x(z1, . . . , z5) = φ(z1, . . . , z5)
ψ(z1, . . . , z5)

with φ and ψ coprime, the φ, ψ thus introduced would necessarily be homo-
geneously linear in the 60 permutations of the z1, . . . , z5. These homogeneous
substitutions would correspond individually to the icosahedral substitutions of
x. So, one would have a group of binary homogeneous substitutions that is
isomorphic with the group of inhomogeneous icosahedral substitutions and such
an isomorphism does not exist, as we have seen previously.

The required function x(z1, . . . , z5) must therefore depend on its argument
algebraically 5. With this, we are led into the domain of those irrationalities of
the theory of equations which I call accessory in my Lectures ([13], p. 158,159),
because they are added as something new to the immediately existing irrational-
ities of the rational functions of the z1, . . . , z5. 6 The usual Galois theory of
equations can only deal with the immediately existing irrationalities and not the
accessory irrationalities, as usually happens when something new comes forward.

We do not know anything about the eﬃcacy of these accessory irrationalities
in general. Rather, we are dependent on tentative experiments in individual
cases. Certainly, in the solution of any higher equation, the only allowable
accessory irrationalities are those calculated from the symmetric functions of
the roots (possibly the predetermined rational functions) by means of lower
equations. 7 In the equations of the ﬁfth degree, which we treat here, the
symmetric functions of the z1, . . . , z5 and its diﬀerence product (the square root
of its discriminant) are known.

5Translator’s Note: In particular, this dependence is not rational.
6Translator’s Note: We refer to these in modern language as natural irrationalities.
7Translator’s Note: This is Klein’s statement of resolvent degree.

6

We can successfully construct (in many ways) one of the icosahedrally-dependent
x(z1, . . . , z5) as soon as we adjoin the square root of a suitable rational function
of the z1, . . . , z5. 8 The two methods of solving equations of the ﬁfth degree,
which I give in my lectures, diﬀer only by where they adjoin this accessory
square root. In the ﬁrst method, the accessory square root (transforming the
ﬁfth-degree equation by a Tschirnhaus transformation into a so-called ﬁfth de-
gree ’principal’ equation - that is an equation in which the sum of the roots and
the sum of the square roots vanishes) comes ﬁrst. In the second method, we
ﬁrst take a step towards the icosahedral problem and then adjoin the accessory
square root. As we said in the introduction, I give preference to the second
method here, by introducing its individual steps in such a way that the whole
approach can analogously be transferred to the sixth degree.

Here, in numbered order, are the main considerations (of the second
method):

1. When x1 : x2 undergo the 120 homogeneous binary icosahedral substitu-
tions, the squares and the product

x
2
1, x1x2, x
2
2.

undergo only 60 homogeneous ternary substitutions of determinant 1 (whose
group is isomorphic to the 60 non-homogeneous icosahedral substitutions
of x1
x2 , and thus to the 60 even permutations of the ﬁve quantities z1, . . . , z5).

2. The same is true, according to the general principles of invariant theory,
of the coeﬃcients of the quadratic binary form of x1 : x2. In order to have
an immediate connection to the style of Kronecker and Brioschi (also used
in my Lectures), I shall hereby designate such a form as follows:

A1x
2
1 + 2A0x1x2 − A2x
2
2 (8)

The A1, 2A0, A2 depend contragrediently on x
2
1, x1x2, x
2
2, according to
the notions of invariant theory. 9

3. We readily conclude that it is possible to form (from any given ﬁve vari-
ables z1, . . . , z5) rational functions such that the alternating permutations
of the z1, . . . , z5 also permute the A0, A1, A2. In fact, in the work already
mentioned in the introduction to Vol. 15 of the Math. Annalen, I have
given a general approach which implies that whenever two given sets of

8The ﬁfth root of unity ǫ = e 2πi
5 occurs in the icosahedral substitutions and will be useful
in the construction of a suitable function x. If we count the accessory irrationalities rigorously,
then one has accessory irrationalities in the theory of equations from the beginning - namely,
in the reduction of the cyclic equations to pure equations.

9Translator’s Note: Recall that given a group G and linear G-representations V and W , a
W -valued contragredient of V is a G-equivariant regular map A(V ∨) ! A(W ).

7

variables (here the z1, . . . , z5 and the A0, A1, A2) undergo isomorphic ho-
mogeneous linear substitutions, we can simply construct rational functions
from which we can translate the ﬁrst set of variables (like the z1, . . . , z5)
into the second set (like the A0, A1, A2).

4. We do not reproduce the general approach here (which would be unnec-
essarily lengthy), but instead give the abbreviated form relevant to our
particular problem, which deals directly with the developments of Kro-
necker and Brioschi on equations of ﬁfth degree [1]. These are the following
points:

(a) We form six quadratic expressions in x1 : x2:
√5x1x2, ǫνx
2
1 + x1x2 − ǫ4νx
2
2 where ǫ = e 2πi
5 , 0 ≤ ν ≤ 4 (9)

which are permuted when x1 : x2 undergo the icosahedral substitu-
tions.

(b) Further, let v(z1, . . . , z5) be a rational function of z1, . . . , z5, which
remains invariant by the cyclic permutation of z1, . . . , z5 taken in
natural order. We form the diﬀerence

v(z1, . . . , z5) − v(z5, . . . , z1)

and square it. Then, we have a ”metacyclic” function,10 which should
be called u2
∞, while the ﬁve other values that result from it by
the alternating permutations of z1, . . . , z5 may be labeled u2
ν in a
proper order (ν = 0, 1, 2, 3, 4). One can then choose the signs of the
u∞, u0, . . . , u4 such that the alternating permutations of the z1, . . . , z5
permute the
 u∞, u0, . . . , u4 (10)

isomorphically by the corresponding icosahedral substitutions of x1, x2;
namely, they undergo the same sign changes as (9).

(c) We conclude that the following form

Ω(z1, . . . , z5|x1 : x2) = √5u∞x1x2 +
 4∑

ν=0 uν (
ǫνx
2
1 + x1x2 − ǫ4νx
2
2)

(11)

remains invariant if one simultaneously applies an alternating per-
mutation to the z1, . . . , z5 and the corresponding icosahedral substi-
tution to the x1 : x2.

10Translator’s Note: This means that the corresponding stabilizer is a metacyclic group.
Recall that a group is metacyclic if it is an extension of a cyclic group by a cyclic group. In
this case, the corresponding stabilizer is D10, the dihedral group with 10 elements, which is
indeed metacyclic.
 8

(d) We now put, in accordance with (8):

Ω(z1, . . . , z5|x1, x2) = A1x
2
1 + 2A0x1x2 − A2x
2
2

and ﬁnd by comparison




2A0 = √
5u∞ + 4∑

ν=0 uν

A1 = 4∑

ν=0 ǫνuν

A2 = 4∑

ν=0 ǫ4νuν
 (12)

Thus, we have constructed from z1, . . . , z5 the quantities A0, A1, A2 which
are permuted in the desired way when the z1, . . . , z5 undergo an alternating
permutation.

5. We refer to the above result by saying that we have assigned a covariant
quadratic binary form (8) to the z1, . . . , z5. 11 The discriminant of (8) is

A = A
2
0 + A1A2, (13)

which is a binary function of z1, . . . , z5 that is invariant under alternating
permutations of z1, . . . , z5; it is thus a rational function of the coeﬃcients
of the given ﬁfth degree equation and the square root of its discriminant.
The goal is not to assign to z1, . . . , z5 a covariant binary quadratic form
or a ”pair of points” of the binary form

A1x
2
1 + 2A0x1x2 − A2x
2
2 = 0, (14)

but to assign a quotient x1
x2 , i.e. a point. We do this in the simplest way
by solving the quadratic equation (14) and accordingly writing

x1
x2 = x = −A0 + √
A2
0 + A1A2
A1 . (15)

6. Thus, we have solved our central task: to compose such an x from the
z1, . . . , z5 which undergoes the icosahedral substitutions corresponding to
the alternating permutations of the z1, . . . , z5. Note that the A0, A1, A2
of item 4d are rational functions of z1, . . . , z5 and their construction uses
only one irrationality - the ﬁfth root of unity ǫ. According to item 5, we
see that the expression of A0, A1, A2 under the square root
12 is invariant
under alternating permutations of the z1, . . . , z5. We have thus achieved
the goal with the aid of such accessory irrationalities, which in the theory
of the ﬁfth degree, will suitably be called lower irrationalities.

11Translator’s Note: Given a group G and linear G-representations V and W , a W -valued
covariant of V is a G-equivariant regular map A(V ) ! A(W ).

12Translator’s note: e.g. the A2
0 + A1A2 in equation (15)

9

7. We now further investigate the parameter X of the icosahedral equation,
which satisﬁes our x (15) as a function of the coeﬃcients of the equation
of the ﬁfth degree whose roots are the z1, . . . , z5, respectively. We will
say that the equation is solved if we calculate the square root of the dis-
criminant and how the z1, . . . , z5 are rationally represented by x from the
coeﬃcients [of the equation of the ﬁfth degree] and the adjoined square
root [i.e. we do not concern ourselves with the transcendental portion].

8. In summary, let us emphasize why one can justiﬁably speak of such a
solution of equations of the ﬁfth degree. Not only is there a sequence of
steps that could be numerically traversed (in the given case) so that one
actually obtains the numerical values of z1, . . . , z5, but it is also a full theo-
retical insight into the internal nature of the problem of solution. 13 After
all, the z1, . . . , z5 are the diﬀerent branches of a ﬁnite-valued algebraic
function, which depends on the coeﬃcients of the ﬁfth degree equation
and is initially of a very confusing design. These ﬁve branches z1, . . . , z5
are deﬁned over the ﬁeld of rationality determined by the icosahedral ir-
rationality. 14 The ﬁeld of rationality is given by the coeﬃcients of the
ﬁfth degree equation, the square root of the discriminant, and the adjoined
accessory irrationalities. The icosahedral irrationality is of a more trans-
parent construction and is a higher irrationality that depends only on a
single parameter from the ﬁeld of rationality.

I would like to take up at this point a more personal remark about the re-
lationship between my papers on the equations of the ﬁfth degree and those of
Kronecker - as you, dear colleague, are in the position of being able to see the
manuscripts of Kronecker and thus can complete my information in an authen-
tic way. As is well known, Kronecker and Brioschi [1] used the same quantities
A0, A1, A2 in their ﬁrst papers on equations of the ﬁfth degree (from 1858)
which I quoted earlier (in list item 4b); they then constructed the sixth-degree
equation satisfying ζ = 5A
2
0, and which Brioschi calls a ”Jacobi equation” be-
cause of its close connection with certain equations established by Jacobi for
the transformation of elliptic functions; ﬁnally, they state that by adjoining a
root, one can arrive at an equation with only one parameter. This square root
deﬁnes an accessory irrationality equivalent to that used in formula (15). Fur-
thermore, Kronecker [15] set up the fundamental theorem, which I designate
as Kronecker’s theorem in my Lectures. Moreover, the exposition and proof of
Kronecker’s theorem are the crowning achievement of my Lectures; the theorem
is that it is impossible to form a resolvent to the general equation of the ﬁfth

13Translator’s note: By ”problem of solution”, Klein means the problem of solving generic
polynomials.

14Translator’s Note: For more on ﬁelds of rationality, see Ackerman’s English translation
of ”Development of Mathematics in the 19th Century” by Felix Klein. In particular, see
Chapter VII - Deeper Insight into the Nature of Algebraic Varieties and Structures, Section 3:
The Theory of Algebraic Integers and Its Interaction with the Theory of Algebraic Functions,
p.312-314.
 10

degree with only one parameter and without resorting to accessory irrationali-
ties. As in the 12th volume of the Math. Annalen [10], I prove this proposition
by invoking the property of the icosahedral group discussed above, namely the
doubling (at least) of its substitutions in the transition to homogeneous sub-
stitutions. My ﬁrst proof, which I gave in 1877 in the reports of the Erlangen
physical-medical school (meeting of January 13), was considerably more com-
plicated. Twenty-four years ago (Easter, 1881), I had the opportunity to talk
in detail with Kronecker about these things. It turned out that in his inves-
tigations, Kronecker was unaware of the icosahedral substitutions to which he
had come so close and, accordingly, did not have suﬃcient proof for his main
claim! I think this is a very remarkable fact, but also very common, for it con-
ﬁrms in a particularly interesting case what Gauss so often emphasizes: that
the discovery of the most important mathematical theorems is more a matter of
intuition than of deduction, and the production of the proof is a very diﬀerent
business from the discovery of the theorems. I did not return to the subject
later with Kronecker, but some years ago, I heard that after the publication of
my Lectures in a college, Kronecker has commented on the solution of the ﬁfth
degree equations and the theory of the icosahedron. I would be very interested
(as certainly would other mathematicians) in ﬁnding out what may be contained
in Kronecker’s papers on these matters, and I would like to ask you to review
the relevant material and publish it soon.

A new proof of Kronecker’s theorem has been given by Mr. Gordan in Vol-
ume 29 of the Math. Annalen [6]. 15 It is easier to read than mine, in that
it does not refer to an explicit knowledge of the icosahedral substitutions any-
where. Nevertheless, as I shall point out, it is most closely related to the basic
idea of my proof. Following a development by Mr. L¨uroth [18], we both use a
proposition which can be formulated as follows: 16

Suppose an equation of nth degree, whose roots are the independent vari-
ables z1, . . . , zn, has a rational resolvent with only one parameter. Then, the nth

degree equation must have a rational function x of the z1, . . . , zn such that when
the z1, . . . , zn are permuted by the Galois group, x undergoes a linear transfor-
mation. We have the same understanding that, when changing to homogeneous
coordinates x1 : x2, we must go from our group of linear substitutions to an
isomorphic groups of homogeneous linear substitutions. On the other hand, of
course, this group must be isomorphic to the Galois group of the equation mod-
ulo a speciﬁed subgroup.

15Compare this with the presentation of Gordan’s proof in the textbook of Weber and
Netto’s ”Algebra”

16Translator’s Note: The theorem of L¨uroth that Klein and Kronecker use can be stated
as follows - Letkbe an algebraically closed ﬁeld of characteristic 0. Then, any unirational
function ﬁeld of transcendence degree 1 is isomorphic tok(t), where t is transcendental overk.
 11

Now, on p.44-47 of my Lectures, I have given the proposition that only the
following groups of linear substitutions of a single variable can be converted
isomorphically to their corresponding binary forms:

1. The cyclic groups

2. The dihedral groups of odd n.

It follows that an equation of the nth degree (whose roots are the independent
variables z1, . . . , zn) only admits a rational resolvent with only one parameter
(which can be immediately transformed into a pure equation, or dihedral equa-
tion of odd n) if its Galois group is (isomorphic to) a normal subgroup of a
cyclic group or a dihedral group of odd n. 17 An associated resolvent with only
one parameter can then be set up immediately according to the principles in the
Math. Annalen Vol 15 [11]. The general statement above is included in both
Gordan’s proof and my proof of Kronecker’s theorem. Indeed, my proof is done
by pointing out that the group of a ﬁfth degree equation with the square root
of the discriminant adjoined is simple; however, it is isomorphic to the group
of linear substitutions of the icosahedron and thus the previous theorem yields
the claim. Gordan’s proof, on the other hand (if I understand it correctly), uses
the obvious fact that the group in question, like every group, contains itself as
a normal subgroup. The quotient of the group by itself is isomorphic to the
identity group. And the identical substitution falls under the premise of our
theorem. Thus, there are in fact resolvents with one parameter, but they are
completely useless for the solution of the equations of the ﬁfth degree! Namely,
there are linear resolvents whose square root is a function of the z1, . . . , z5 that
is invariant under the alternating permutations of the z1, . . . , z5. But there are
no other (rational) resolvents with just one parameter, or better: every ratio-
nal resolvent of our ﬁfth degree equation with just one parameter is linear and
therefore useless.

So much for the icosahedral substitutions and the solution of ﬁfth degree
equations mediated by them. Instead of the ”unitary” substitutions x
′ = e 2πik
n ,
which link the roots of a pure equation to one another, ”binary” linear substi-
tutions of two homogeneous variables x1 : x2 have entered. At the same time,
the way to new generalizations has opened up - one simply has to use groups of
linear substitutions of several homogeneous variables! I cannot possibly repeat
here the reﬂections which I gave in this regard ﬁrst in the 15th volume of the
Math. Annalen [11] or recall the elaborations which have later been concluded.
It suﬃces to refer to Weber’s textbook [19] and to the already cited encyclo-
pedia article by Wiman [22]. 18 In this sequence, we consider an equation of
sixth degree along with the square root of its discriminant, whose Galois group
consists of the 360 alternating permutations of the roots z1, . . . , z6. It will be

17Translator’s Note: In modern language, this is the classiﬁcation of groups of essential
dimension 1.
18A ﬁrst clear introduction is also the Lecture IX of my Evanston Colloquium, held at the
World’s Fair in Chicago (Macmillan, New York, 1894)

12

necessary to use the smallest number of homogeneous x1 : . . . : xµ for which
there exists a surjective homomorphism from the group of linear substitutions
of the x1 : · · · : xµ to the group of the 360 alternating permutations. If this
surjective homomorphism were to prove to be an isomorphism, we would be able
to write down rational functions of z1, . . . , z6 (according to the prescriptions of
[11]) which are linear in the 360 alternating permutations of z1, . . . , z6 and yield
x1 : . . . : xµ as a result. However, it turns out that here, as in the equations of
the ﬁfth degree, the homomorphism must have a non-trivial kernel, so that we
are asked the question whether (or respectively, how) we can get by with the
help of lower accessory irrationalities.

My ﬁrst approach to the formulation of this question is in Volume 28 of the
Math. Annalen (1886, On the Theory of General Equations of the Sixth and
Seventh Degrees)
19 [12]. At the time, it seemed like the preliminary work of
Mr. C. Jordan would not allow a ternary group of linear substitutions with the
requisite surjective homomorphism to the group of the 360 alternating permu-
tations on six letters; such a group was ﬁrst discovered by Mr. Valentiner in
1889 (Volume 6 of Series V of the Danish Academy’s papers: The Deﬁnitions
of the Final Transformation Groups) [20] and examined by structural and re-
lated fundamental invariants for the ﬁrst time by Mr. Wiman in 1895 20 (Math.
Annalen 47: About the Simple Group of 360 Plane Collineations) [21]. At
that time, I constructed a group of quarternary collineations that is isomorphic
to the group for the general equation of degree six - and also for the general
equation of degree seven - and showed that the original problems rest on the
corresponding problems for the groups of quarternary collineations, which can
be obtained from the general equations of degree six (respectively, seven) with
at most two accessory square roots. 21

As far as the equations of the sixth degree are concerned (to which we conﬁne
ourselves here), this approach is currently unnecessary, because of the discov-
ery of the Valentiner group. 22 I note this expressly, because this is where
Mr. Lachtin makes an unnecessary detour (as mentioned at the beginning of
this letter). In order to connect the equation of degree six with the Valentiner
group, Mr. Lachtin goes through the development given in Volume 28 of the

19Translator’s Note: Klein gives the correct volume for the article, but the incorrect year.
This article is from December 1887 in Issue 4 of Volume 28.

20Translator’s Note: While Klein gives the correct volume, this work was actually published
in December of 1896.

21The group which I put forward for the sixth degree equation contains as many as 720
collineations, so that it is not necessary to use all of them; adjoin the square root of the
discriminant of the sixth degree equation beforehand. In contrast, the group corresponding
to the equations of the seventh degree contains only 7!
2 = 2520 collineations.

22For the equations of seventh degree, the quaternary approach persists; but it is impossible
to pursue the interesting questions in this text.

13

Math. Annalen. 23 [16]

This is not uninteresting, 24 but is by no means necessary for what we do
next. The transition from the equations of the sixth degree to the Valentiner
group (as I suggested in my Roman note of 1899) and which I now wish to
introduce in more detail, does not require any reference to the quarternary
substitution group. For the sake of clarity, I shall again divide the considerations
in question into a numbered list below which makes clear the analogy with the
train of thought followed for the equations of the ﬁfth degree:

1. The task is to compose three functions x1, x2, x3 from the six free variables
z1, . . . , z6 such that the homogeneous x1 : x2 : x3 undergo the correspond-
ing collineations of the Valentiner group when the z1, . . . , z6 undergo one
of the 360 alternating permutations.

2. Now, Mr. Wiman has already noticed that the number of collineations
from the Valentiner group at least triples when one goes from substitutions
of the plane to the corresponding ternary linear substitutions. Therefore,
it is not possible for the required x1, x2, x3 to be rational functions of
z1, . . . , z6.

3. From now on, we want to ﬁx the homogeneous linear Valentiner substi-
tutions so that their determinant is always 1. Thus, there are exactly
3(360) = 1080 of them and the three substitutions corresponding to the
identity substitution [of the plane] are:




x
′
1 = jν x1,
x
′
2 = jν x2,
x
′
3 = jν x3, j = e 2πi
3 , 0 ≤ ν ≤ 2 (16)

4. We now note that in these 1080 homogeneous substitutions, the ten degree
three terms coming from the x1, x2, x3 are:

x
3
1, x
2
1x2, . . .

23Translator’s Note: Lachtin only has two articles in the Mathematische Annalen. The one
Klein is referring to from September 1898 in Issue 3 of Volume 51. Lachtin’s other article is
on the septic and is from September 1902 in Issue 3 of Volume 56.

24Mr. Lachtin notes that in the quaternary group, the degree two surfaces in space in-
terchange in much the same way as the degree three curves of the plane. From here, as is
noted in passing, it is possible without any great diﬃculty to arrive at the same Σ, which I
communicate below under (19). One only has to keep in mind that the roots z1, . . . , z6 of
the sixth degree equation, and also their squares z2
1, . . . , z2
6 deﬁne a linear complex in space
according to the developments of Volume 28, and that these two complexes together with the
”unitary complex” introduced there determine a degree two surface through their common
lines. No accessory irrationality occurs here. It is then in no way necessary, in the transition
from space to plane, to refer to the comparatively complicated formulas, as Mr. Lachtin does,
by which in Volume 28 I have assigned a point of space to the roots z1, . . . , z6, so also in this
regard, the approach of Mr. Lachtin can be shortened.

14

which only undergo 360 homogeneous linear substitutions (and whose
group will be isomorphic with the group of alternating permutations of
z1, . . . , z6).

5. We now consider any cubic ternary form

a1,1,1x
3
1 + 3a1,1,2x
2
1x2 + · · ·

(which, if set equal to 0, represents a ”degree three curve” in the plane of
x1, x2, x3). The coeﬃcients a1,1,1, 3a1,1,2, . . . for any homogeneous linear
substitutions of x1 : x2 : x3 are related to the x
3
1, x
2
1x2, . . . contravariantly.
Thus, in the substitutions of the Valentiner group, they also undergo ex-
actly 360 homogeneous linear substitutions, which can be uniquely iden-
tiﬁed with the 360 alternating permutations of z1, . . . , z6.

6. We readily conclude that it is possible to form ten rational functions of
the free variables z1, . . . , z6 denoted by:

φ1,1,1, φ1,1,2, . . .

which, in the case of the alternating substitutions of the z1, . . . , z6, are
substituted just as the
 a1,1,1, a1,1,2, . . .

are by the corresponding substitutions of the Valentiner group; i.e., the
roots z1, . . . , z6 rationally and covariantly assign a degree three curve.

7. To put it another way, one can construct (in many diﬀerent ways and
without the use of accessory irrationalities 25), a cubic form depending on
the z1, . . . , z6 and x1, x2, x3

Ω(z1, . . . , z6|x1, x2, x3) = φ1,1,1x
3
1 + 3φ1,1,2x
2
1x2 + · · · (17)

which remains invariant if one simultaneously performs an alternating
permutation on the z1, . . . , z6 and its corresponding Valentiner substitution
on the x1, x2, x3.

8. As far as the actual construction of such a form Ω is concerned, I do not
give the general and extensive process which I provided in [11], but develop
it in an abbreviated manner that emerged from my correspondence with
Mr. Gordan (last winter), just as with equations of the ﬁfth degree. One
has to combine the following relationships:

25Apart, of course, from the numerical irrationalities that occur in the substitutions of the
Valentiner group. These are (in accordance with the following formulas (18), etc.) the square
roots √
−3 and √5.
 15

(a) The 360 collineations of the Valentiner group play an important role
in two systems of six conic sections, as Mr. Wiman proved ﬁrst.
The six conic sections of each of the two systems are permuted by the
corresponding 360 collineations in 360 ways.

(b) The equations of these 2 · 6 = 12 conic sections were ﬁrst proposed
by Mr. Gerbaldi [5] (Rendiconti del Circolo Matematico di Palermo,
t. XII, 1898: ”Sul gruppo semplice di 360 collineazioni piane, I;
already published in 1882 in the Atti di Torino, Vol. XV, p. 358
ﬀ., Note: ”Sui gruppi di sei coniche in involuzione”)
26. Here we
equate the corresponding ternary quadratic forms of determinant 1
by restricting to the one system of six conic sections, according to
the procedure of Mr. Gordan. We can then write: 27






k1 = x
2
1 + jx
2
2 + j2x
2
3
k2 = x
2
1 + j2x
2
2 + jx
2
3
k3 = α (
x
2
1 + x
2
2 + x
2
3) + β (x2x3 + x3x1 + x1x2)
k4 = α (
x
2
1 + x
2
2 + x
2
3) + β (x2x3 − x3x1 − x1x2)
k5 = α (
x
2
1 + x
2
2 + x
2
3) + β (−x2x3 + x3x1 − x1x2)
k6 = α (
x
2
1 + x
2
2 + x
2
3) + β (−x2x3 − x3x1 + x1x2)
 (18)

where α = 1−√−15
8 and β = −3+√
−15
4 .

(c) The k1, . . . , k6 are determined, up to a third root of unity, by the
requirement that their determinant be 1. In fact, the 1080 Valen-
tiner substitutions permute the k1, . . . , k6 by multiplication by cer-
tain third roots of unity.

(d) We want, now, from any three of the k:

k′, k′′, k′′′

one whose coeﬃcients form a trilinear covariant and a similar invari-
ant. For the former, we choose the functional determinant |k′k′′k′′′|,
which changes its sign when two of the k′, k′′, k′′′ are exchanged. As
an invariant, we take a symmetric combination of the coeﬃcients
of the k′, k′′, k′′′ (namely the expression used in the development of
the coeﬃcient-determinant of the form λ
′k′ + λ
′′k′′ + λ
′′′k′′′ in which
λ
′λ
′′λ
′′′ appears). I will temporarily call it (k′k′′k′′′) here; this is a
simple numerical quantity in the present case.

(e) For all possible triples k′, k′′, k′′′, we now form the quotient

|k′k′′k′′′|
(k′k′′k′′′) .

26Translator’s Note: The modern reference for this article is the one appearing in the
Mathematische Annalen, which is what we give. Thus, we have left the two previous journal
references Klein gave in the main text.

27Translator’s note: As in equation (16), j is the primitive 3rd root of unit e 2πi
3 .

16

One can show that the (
6
3) = 20 quotients obtained above undergo
the same sign changes from the 1080 substitutions of the Valentiner
groups that the 20 diﬀerence products

(z′′ − z′′′)(z′′′ − z′)(z′ − z′′)

undergo from the corresponding alternating permutations of the z1, . . . , z6.

(f) Therefore, the sum of all triples

∑(z′′ − z′′′)(z′′′ − z′)(z′ − z′′) · |k′k′′k′′′|
(k′k′′k′′′) (19)

is a simple example of a form

Ω (z1, . . . , z6, x1, x2, x3)

as we were looking for in item number 7 above.

(g) More general examples (which we do not need in the following) are
obtained by substituting the determinant
∣
∣
∣
∣
∣
∣
z′α z′′α z′′′α

z′β z′′β z′′′β

z′γ z′′γ z′′′γ
 ∣
∣
∣
∣
∣
∣

for the diﬀerence product of z′, z′′, z′′′ in (19).

(h) Let us now assign the sum (19) to the successive terms x
3
1, x
2
1x2, . . .
by writing, as in formula (17):

∑(z′′ − z′′′)(z′′′ − z′)(z′ − z′′) · |k′k′′k′′′|
(k′k′′k′′′) = φ1,1,1x
3
1 + 3φ1,1,2x
2
1x2 + · · · ,

(20)

so that the φ1,1,1, φ1,1,2, . . . , are just such the rational functions of
z1, . . . , z6 that we looked for in item number 6 above.

9. The degree three curve

∑(z′′ − z′′′)(z′′′ − z′)(z′ − z′′) · |k′k′′k′′′|
(k′k′′k′′′) = 0 (21)

(whose coeﬃcients depend rationally on the z1, . . . , z6) covariantly assigns
a point x1 : x2 : x3 using accessory irrationalities that are as low as
possible.

10. The theory of degree three plane curves oﬀers various possibilities. For the
sake of brevity, as I did in my Roman note, I want to choose an inﬂection
point in third-order curve here.
 17

11. According to the well-known theory of Hesse, the determination of such an
inﬂection point requires only square roots and cube roots; for the solution
of the equations of the sixth degree, these are indeed lower irrationalities.
The details [of the process of determining an inﬂection point] are not
discussed here.

12. On the other hand, the inﬂection point is certainly connected in a covariant
manner with the degree three curve: if any collineation is performed on
a curve with a chosen inﬂection point P , then P is taken to an inﬂection
point P ′ on the new curve and each of the nine inﬂection points can be
realized in this manner. In particular, this applies to the 360 collineations
of the Valentiner group.

13. We now think of the coordinates x1 : x2 : x3 of our chosen inﬂection
point, instead of the coeﬃcients φ1,1,1, φ1,1,2, . . . of the curve of third order
(whose values come from (20) and the z1, . . . , z6).

14. If the z1, . . . , z6 undergo an alternating permutation, the x1 : x2 : x3 un-
dergo the corresponding collineation of the Valentiner group.

We conclude that the rational functions of z1, . . . , z6 that remain invariant
after the reductions in the expressions of x1 : x2 : x3 from the occurring
square roots and cubic roots also remain invariant under the alternating
permutations of the z1, . . . , z6. Thus, they can be represented as rational
functions of the coeﬃcients of the presented sixth degree equation and the
square root of their discriminant.

15. Therefore, we will are justiﬁed in designating the irrationalities required
in the calculation of the inﬂection point as lower accessory irrationalities.

16. By computing the coordinates x1 : x2 : x3 of an inﬂection point of our
C3 [our degree three curve], we have accomplished the goal: we form the
functions x1, x2, x3 from the free variables z1, . . . , z6 and lower accessory
irrationalities such that when the the z1, . . . , z6 undergo an alternating
permutation, the x1, x2, x3 undergo the corresponding collineation of the
Valentiner group.

This is the explanation of the particular content of my Roman note, which
I thought to give here. 28

One might wish for a closer examination of the inference used in list item
number 14. The simplest thing would be to calculate all the known equations
leading to the determination of an inﬂection point of the degree three curve (21)

28The ﬁnal sentence of the note has become incomprehensible when printed in the Rendiconti
of the Accademia dei Lincei by a strange change. It should read ”And with the aid of accessory
irrationalities, which we usually regard as elementary, we come to the goal.” Instead, what is
printed is ”And so, with the aid of ancillary irrationalities, we come to the goal, which usually
regarded as elementary.”
 18

and thus actually conﬁrm the assertion. Moreover, as Mr. Gordan remarks, the
whole of the conclusion can be dealt with in the following way. Just consider the
ninth degree equation, which satisﬁes the nine values that an absolute invariant
of the Valentiner group (e.g. the ν to be named immediately) assumes in the
nine inﬂection points! This equation must be the same for all 360 third-order
curves (which results from the substitutions of the Valentiner group and thus by
the alternating substitutions of the two). After disposing of indiﬀerent factors,
the coeﬃcients are rational functions of the z1, . . . , z6 that are invariant under
the alternating permutations of the z1, . . . , z6. The aﬀect of this ninth degree
equation can be none other than that of the original inﬂection point equation. It
is thus solved by square roots and cubic roots of rational functions of z1, . . . , z6
that are invariant under the alternating permutations of z1, . . . , z6.

Now, if we adjoin one of the resulting nine values of our absolute invariant
(ν), then it and the equation (21) of the third order curve, (respectively, of
the equation of its Hessian curve), becomes the corresponding single inﬂection
point x1 : x2 : x3 and is calculated rationally. Consequently, the assertion of
list item number 14 concerning the irrationalities required in the calculation of
the inﬂection point, is self-evident.

The further treatment of equations of the sixth degree will have to be done,
in any case, by calculating the absolute invariants of the Valentiner group of the
selected inﬂection point of our third order curve. According to Mr. Wiman, the
Valentiner group has three lowest invariants:

F, H, Φ (22)

of degrees 6, 12, and 30 in the x1, x2, x3. From them, the two fundamental
absolute invariants come together, which I call v and w here in connection with
the work of Mr. Lachtin to be mentioned immediately:

v = Φ
F 3 , w = H
F 2 . (23)

If we enter the coordinates of our point of inﬂection for x1 : x2 : x3, then the
v, w are rational functions of the coeﬃcients of the sixth degree equation and
the square root of the discriminant (respectively, the occasionally introduced
accessory irrationalities). The Normalproblem 29 of solving equations of the
sixth degree is thus the reduction to calculating x1 : x2 : x3 from the known
v, w. As just stated, this is now a problem with two arbitrary parameters and
is distinguished by the fact that all of its 360 solutions x1 : x2 : x3 can be
determined from a given solution by the 360 collineations of the Valentiner
group. We do not currently have a method to reduce the number of parameters
to one by means of further lower irrationalities. For example, if we try to assign
a point x
′
1 : x
′
2 : x
′
3 to the degree six curve F = 0 in a covariant manner and

29In German, this was indeed one word - Normalproblem.

19

thus set the following (instead of the Normalproblem (23) to the inﬂection point
x1 : x2 : x3)
 F ′ = 0, t′ = Φ′2

H ′5 , (24)

in the usual approach (intersection of the curve F = 0 with a straight line co-
variantly dependent on the point x1 : x2 : x3 :), one encounters an auxiliary
equation which itself is of the sixth degree!

For the sake of completeness, we ﬁnally ask for a reverse form, i.e. to ra-
tionally calculate the quantities assumed to be known [v, w] from the roots
z1, . . . , z6 of the presented sixth order equation and a single solution system
x1 : x2 : x3 of (23). Thus, we have completely sketched the algebraic part of the
solution of the equations of the sixth degree.

The transcendental part will require inﬁnite processes to actually compute
the x1 : x2 : x3 from the equations (23). A ﬁrst approach to this is done by Mr.
Lachtin in a voluminuous work, which was ﬁrst published in Russian (1901) in
the 22nd volume of the Moscow Mathematics Collection and then in 1902 in
the German edition of Volume 56 of the Math. Annalen [17]. 30 Writing

y1 = x1

6√F , y2 = x2

6√
F , y3 = x3

6√
F , (25)

the y1, y2, y3 are a system of solutions to the three simultaneous linear partial
diﬀerential equations expressing the second derivatives

∂2y
∂v2 , ∂2y
∂v∂w , ∂2y
∂w2

linearly in the ( ∂y
∂v and ∂y
∂w ) and the y. Mr. Lachtin has shown that the coef-
ﬁcients of these equations are rational functions of the absolute invariants v, w,
which do not exceed certain deﬁnable degrees. However, he did not calculate
the numerical coeﬃcients of these polynomials. The remaining gap is now being
ﬁlled by the work of Mr. Gordan, which I referred to in the beginning of this
letter. 31 In fact, Mr. Gordan succeeded in making explicit the partial diﬀeren-
tial equations in question. It is thus possible to develop the y1, y2, y3 in powers
of v and w, or even in any series of linear functions of v and linear functions of
w; thus, it is no longer an issue to determine the regions in which the various
series thus formed converge - in other words, we can solve the transcendental
problem in a direct way.

30”The diﬀerential resolvent of an algebraic equation of the sixth degree of a general kind.”
(Math. Ann., Vol. 56, p. 445-481.)

31We believe that Klein is referring to the work that became [7]

20

Again, for the sake of completeness, it must be added that the special prob-
lem presented by equation (24) is already discussed in detail in terms of function
theory. In 1896, at the Frankfurter Scientiﬁc Congress, Mr. Fricke 32 dealt with
the decomposition of the Riemann surface (of genus 10) corresponding to the
Valentiner group into fundamental domains and a closed relation of the same
with the decomposition of the half plane in the semicircular triangles from the
angles
 π
2 , π
4 , π
5

Mr. Lachtin then conﬁrms this information in [16] and established the third-
order linear diﬀerential equation, for which - in the case of equations (24) - the
parameter t is satisﬁed by the variables xν multiplied by a suitable factor.

I am at the end of my presentation. I hope the analogy of the proposed
sixth degree equations with the solution of the equations of the ﬁfth degree by
the icosahedral equation appears convincing. A ﬁner examination of the de-
tails given by Mr. Gordan and myself for the equations of the ﬁfth degree, as
well as a geometric presentation, are given in my ”Lectures on the Icosahedron.”

G¨ottingen, March 22, 1905.

32Translator’s Note: For more information, see [4]

21

2 Ending Footnote

Mr. Gordan has been able to devote only one introductory essay to the questions
raised above [8]. There he makes a substantial simpliﬁcation of the necessary
accessory irrationality of x1, x2, x3. Instead of the degree three curve of the
x1, x2, x3-plane, which I rationally assigned to the value system z1, . . . , z6, it
uses a (1,1)-connection; i.e. a bilinear form in the x and u (whose coeﬃcients
must be assumed to be whole rational functions of z1, . . . , z6 and that the form
remains invariant under the 360 permutations of the z1, . . . , z6 and the corre-
sponding linear substitutions of the x and u). Then, to ﬁnd a covariant point
x1, x2, x3 for one of the permutations of the z1, . . . , z6, one only has to determine
one more root of an easy cubic equation, namely to go to a ﬁxed point of the
connection.

In particular, Gordan succeeds in setting up a linear form of the desired
kind, which is of degree 6 in the z1, . . . , z6. In the meantime, Mr. Coble showed
by a systematic process that one need only go to the fourth degree [3]. He sets
up the associated cubic equation and then further sketches the course of the
required algebraic calculation to determine the z1, . . . , z6. K.

I will conclude by mentioning the explanations given on p.491, footnote 10,
referring to Kronecker’s theorem.

First of all, for the sake of completeness, a few hints about my original proof
of January, 1877. At that time, I had operated on the fact that all icosahedral
forms, and also the tetrahedral form, have a direct degree. The circumstance is,
of course, in turn, a consequence of the doubling of the number of homogeneous
substitutions which I have emphasized in Abh. LIV, which was the actual rea-
son for the proof.

Incidentally, I must go into more detail about the reference between Kro-
necker and myself from Easter 1881 [see p.10]. At that time, I asked Kronecker
for a manuscript from 1861, from which I could copy the part that was suitable
for me (the copy bears the date of March 23). In the proof of his theorem,
Kronecker uses it exactly as I did later by anticipating L¨uroth’s theorem on
rational curves [18] and, from there on, the task is to form a rational function
φ
ψ out of ﬁve free variables x0, . . . , x4, which is a linear transformation in the 60
alternating permutations of the x0, . . . , x4. He then encounters a strange lapse.
Since Kronecker had not yet familiarized himself with the general notion of a
group of linear substitutions (of one variable), he erroneously concludes that the
60 linear transformations in question ought to arise from the repetition of the
same linear substitution; that is, from a cyclic equation of 60th degree, which
(according to Galois theory) is of course impossible. At that time, Kronecker
went quiet [on the subject].
 22

In the lectures of 1885-86, this mistake is corrected. It is concluded that
in the case of the alternating permutations of the free variables x0, . . . , x4, the
polynomials φ and ψ would have to be substituted in a linearly binary manner,
and further, that such a binary behavior is already impossible if one of the per-
mutations ﬁxes an xi and cyclically permutes the others xj ’s. Even without the
evidence of this impossibility, I still ﬁnd an unnecessary complication. I showed
above( p. 485) that even in the Klein four group, the impossibility in question
arises. In order to come to a contradiction, Kronecker instead combines an op-
eration of the Klein four group with the cyclic permutation of the x1, x2, x3 -
this is less transparent.

Aside from these secondary points, a complete consensus exists. There re-
mains only a subjective diﬀerence, which I already discussed in detail on pages
p.158-159 in the book on the icosahedron, but which I do not want to leave un-
touched here because of its importance. For the ﬁrst time in his investigations
into the solution of equations of the ﬁfth degree, Kronecker begged to have a
clear distinction between the natural irrationalities (which are rational functions
of x0, . . . , x4) and the other irrationalities (which I call accessory). Incidentally,
in his ﬁrst communication of 1858 [2] , he himself makes an unobjectionable use
of an accessory square root. Is is only in the later work of 1861 [15] that he
believes that he should forbid the use of accessory irrationalities in the theory
of equations altogether. In his 1885-86 lectures, he maintains this verdict:

...the use of accessory irrationalities is ”algebraically worthless,” be-
cause it ”tears apart” the type.

In order to emphasize this demand, he calls it the ”Abelian postulate.” In con-
trast to other authors of similar thinking, I have explored as far as possible in
my papers printed here above, as in the book on the icosahedron, the eﬃcacy
of using naturally occurring accessory irrationalities.

There is a principled diﬀerence in this thinking. I do not want to further
emphasize that Abel continues to use the roots of unity ǫ in his investigations
into the solution of the equations by radicals [which in the context of his consid-
erations are also accessory irrationalities (see above, p. 486 footnote 8)], which
incidentally Kronecker continues to do himself, because otherwise he would not
be able to act on the connection of the equation of the ﬁfth degree with the
Jacobian equations of the sixth degree. Nor do I want to argue that it [the
use of accessory irrationalities] is as advantageous in the theory of numbers as
it is in function theory, because of the simplicity of the higher-order algebraic
relations in transcendental ﬁelds. I only want to emphasize the fundamentals.

23

When presented with new phenomena (such as the eﬃcacy of the accessory irra-
tionalities), should we we stop developing these ideas to align with our current
conceptions, or rather push back against our narrow, systematic ways of think-
ing and pursue the new ideas in an unbiased way? Should one be a dogmatist
or a natural scientist, and endeavor to keep learning from new ideas?

There is nothing special to be inferred from Kronecker’s original notes, which
Mr. Hensel sent to me. These are mainly 23 unilaterally described folios, of
which 1-10 refer to the work of 1858 and 11-23 to those of 1861. It is worth
noting that the passages I copied in 1881 are missing. On the back of the pages
17-18, there are bills with ﬁfth roots of unity, by virtue of which Kronecker has
evidently been convinced that the G60 of broken icosahedral substitutions really
do exist.

The criticism which I then apply to the transmitted material is intended
to reﬂect the high position which I have given to Kronecker’s investigations
on the equations of the ﬁfth degree in the above reprinted essays, especially
in the historical account of the book on the icosahedron ([13], see p.141-161).
Kronecker ﬁrst found the path which leads into the fundamental questions of
the theory, only he did not ﬁnish it at ﬁrst and later, at least formally, refused
to accompany others on the way forward. K.

24

3 Appendix A: Formal Bibliography

References

[1] Brioschi, Francesco. Sul metodo di Kronecker per la risoluzione delle
equazioni di quinto grado. Atti dell’I. R. Istituto Lombardo di Scienze,
Lettere ed Arti, 1:275–282, 1858. Opere matematiche di F. Brioschi, III,
357-360.

[2] Brioschi, Francesco. Sur divers ´equations analogues aux ´equations mod-
ulaires dans la th´eorie des fonctions elliptiques (Extrait d’un lettre a M.
Hermite). Comptes Rendus de l’Acad´emie des Sciences de Paris, 47:337–
341, 1858. Opere matematiche di F. Brioschi, IV, 327-330.

[3] Coble, Arthur B. The reduction of the sextic equation to the valentiner
form-problem. Mathematische Annalen, 70(3):337–350, Sep 1911.

[4] Fricke, Robert. Notiz ¨uber die Discontinuit¨at gewisser Collineationsgrup-
pen. Math. Ann., 47(4):557–563, 1896.

[5] Gerbaldi, Francesco. Sul gruppo semplice di 360 collineazioni piane. Math.
Ann., 50(2-3):473–476, 1898.

[6] Gordan, Paul. Ueber biquadratische Gleichungen. Math. Ann., 29(3):318–
326, 1887.

[7] Gordan, Paul. Die partiellen Diﬀerentialgleichungen des Valentinerprob-
lems. Math. Ann., 61(4):453–526, 1906.

[8] Gordan, Paul. ¨Uber eine Kleinsche Bilinearform. Math. Ann., 68(1):1–23,
1909.

[9] Klein, Felix. On the solution of sixth degree equations (extracted from a
letter to Mr. Castelnuovo). Proc. Linc. Acad., 1st semester(1), 09 April
1899.

[10] Klein, Felix. Weitere Untersuchungen ¨uber des Ikosaeder. Math. Ann.,
12(4):503–560, 1877.

[11] Klein, Felix. Ueber die Auﬂ¨osung gewisser Gleichungen vom siebenten und
achten Grade. Math. Ann., 15(2):251–282, 1879.

[12] Klein, Felix. Zur theorie der allgemeinen gleichungen sechsten und sieben-
ten grades. Mathematische Annalen, 28(4):499–532, Dec 1887.

[13] Klein, Felix. Lectures on the icosahedron and the solution of equations of
the ﬁfth degree. Dover Publications, Inc., New York, N.Y., revised edition,
1956. Translated into English by George Gavin Morrice.

25

[14] Klein, Felix and Fricke, Robert. Lectures on the theory of elliptic modu-
lar functions. Vol. 1, volume 1 of CTM. Classical Topics in Mathematics.
Higher Education Press, Beijing, 2017. Translated from the German origi-
nal [ MR0247996] by Arthur M. DuPre.

[15] Kronecker, Leopold. Ueber die Gleichungen f¨unften Grades. J. Reine
Angew. Math., 59:306–310, 1861.

[16] Lachtin, L. Die diﬀerentialresolvente einer algebraischen gleichung 6ten
grades mit einer gruppe 360ster ordnung. Mathematische Annalen,
51(3):463–472, Sep 1898.

[17] Lachtin, L. Die diﬀerentialresolvente einer algebraischen gleichung sechsten
grades allgemeiner art. Mathematische Annalen, 56(3):445–481, Sep 1902.

[18] L¨uroth, Jacob. Beweis eines Satzes ¨uber rationale Curven. Math. Ann.,
9(2):163–165, 1875.

[19] Pierpont, James. Weber’s algebra. Bull. Amer. Math. Soc., 4(5):200–234,
02 1898.

[20] Valentiner, Herman. De endelige transformations-gruppers theori. Dan.
Acad. Pub., Series V6, 1889.

[21] Wiman, Anders. Ueber eine einfache gruppe von 360 ebenen collineationen.
Mathematische Annalen, 47(4):531–556, Dec 1896.

[22] Wiman, Anders. Finite groups of linear substitutions. Encyclopedia of
Mathematical Sciences, I:522–554, 1898.

26
