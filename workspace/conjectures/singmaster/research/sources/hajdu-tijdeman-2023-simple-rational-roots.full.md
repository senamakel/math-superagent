<!-- source: https://arxiv.org/pdf/2204.12345 | converted from PDF -->

arXiv:2204.12345v1  [math.NT]  26 Apr 2022
THE DIOPHANTINE EQUATION f (x) = g(y) FOR
POLYNOMIALS WITH SIMPLE RATIONAL ROOTS

L. HAJDU AND R. TIJDEMAN

Abstract. In this paper we consider Diophantine equations of
the form f (x) = g(y) where f has simple rational roots and g
has rational coeﬃcients. We give strict conditions for the cases
where the equation has inﬁnitely many solutions in rationals with
a bounded denominator. We give examples illustrating that the
given conditions are necessary. It turns out that such equations
with inﬁnitely many solutions are strongly related to Prouhet-
Tarry-Escott tuples. In the special, but important case when g
has only simple rational roots as well, we can give a simpler state-
ment. Also we provide an application to equal products with terms
belonging to blocks of consecutive integers of bounded length. The
latter theorem is related to problems and results of Erd˝os and Turk,
and of Erd˝os and Graham.

1. Introduction

Let a1, . . . , ak be distinct rationals and a0 ∈ Q with a0 ̸= 0. Put

(1) f (x) = a0(x − a1) · · · (x − ak)

and let g(y) ∈ Q[y]. In this paper we investigate for which f, g equation

(2) f (x) = g(y)

has inﬁnitely many solutions. Moreover, we study for which f, g this
holds if g is of the form

(3) g(y) = b0(y − b1) · · · (y − bℓ),

where b1, . . . , bℓ are distinct elements of Q and b0 ∈ Q with b0 ̸= 0.
We say that an equation f (x) = g(y) has inﬁnitely many rational
solutions with a bounded denominator if there exists a positive integer

2010 Mathematics Subject Classiﬁcation. 11N32, 11B75, 11D41.
Key words and phrases. Polynomials with rational roots, polynomial values,
equal values, the Prouhet-Tarry-Escott problem, products of integers from a block
of bounded length.
Research of L.H. supported in part by the NKFIH grants 115479, 128088, and
130909, and the projects EFOP-3.6.1-16-2016-00022 co-ﬁnanced by the European
Union and the European Social Fund. 1

2 L. HAJDU AND R. TIJDEMAN

∆ such that f (x) = g(y) has inﬁnitely many solutions (x, y) ∈ Q
2 with
(∆x, ∆y) ∈ Z
2. Our focus is the question for which f, g equation (2)
has inﬁnitely many solutions (x, y) ∈ Q
2 with a bounded denominator.
Using results of Bilu and Tichy [11] and of Davenport, Lewis and
Schinzel [22], both based on a theorem of Siegel [73], we prove the
following theorem.

Theorem 1.1. Let f (x) ∈ Q[x] have only simple rational roots and
let g(x) ∈ Q[x]. Suppose the equation f (x) = g(y) has inﬁnitely many
solutions (x, y) ∈ Q
2 with a bounded denominator.
Then there exist m ∈ {1, 2, 3, 4, 6}, n, s ∈ Z>0 or n ∈ {1, 2}, m, s ∈
Z>0 such that deg(f ) = ms, deg(g) = ns.
If also g has only simple rational roots and deg(f ) ≤ deg(g), then
there exist m ∈ {1, 2}, n, s ∈ Z>0 such that deg(f ) = ms, deg(g) = ns.

The ﬁrst statement will be proved in Section 7. After the proof we
shall argue that if m ∈ {1, 2, 3, 4, 6} for every such m, n, s a pair of
polynomials (f, g) can be constructed with f having only simple ratio-
nal roots such that f (x) = g(y) has inﬁnitely many integral solutions
(x, y). For the remaining cases, see Section 11.
The second statement will be proved in Section 9. Observe that it
follows that deg(f ) | 2 deg(g).

As illustration of Theorem 1.1 we present some nontrivial examples.
Later more examples will follow.

Example 1.1. An example of the second statement where deg(f ) does
not divide deg(g). Let

f (x) = (x − 6)(x + 6), g(y) = (y − 1)(y − 4)(y − 9).

Then f (x) = g(y) has solution

(x, y) = (X(X 2 − 7), X 2) for every X ∈ Z.

Example 1.2. An example of the second statement where deg(f )
divides deg(g). Let

f (x) = (x − 7)(x − 1)(x + 1)(x + 7), g(y) = 4(y − 5)(y − 1)(y + 1)(y + 5).

Consider the Pell equation x
2 = 2y2 − 1. It has solutions (Xi, Yi)∞
i=1
given by (X1, Y1) = (1, 1), (X2, Y2) = (7, 5) and

Xi+1 = 6Xi − Xi−1, Yi+1 = 6Yi − Yi−1 (i = 2, 3, . . . ).

Then f (x) = g(y) has as solution

(x, y) = (Xi, Yi) for every i ∈ Z>0.

THE DIOPHANTINE EQUATION f (x) = g(y) 3

Example 1.3. An example of the ﬁrst statement for m = 3, n = 4
and s = 1. Let

f (x) = (x + 286)(x + 13)(x − 299), g(y) = y4 − 8788y2 + 8541936.

For every X ∈ Z there is a solution

(x, y) = (X 4 − 52X 2 + 338, X 3 − 39X).

In Section 2 we give a historical overview of the literature on equa-
tions f (x) = g(y) where f has only simple rational roots. In Section
3 we present the Bilu-Tichy decomposition which is fundamental for
our treatment. Bilu and Tichy distinguish ﬁve kinds of standard pairs.
We exclude the ﬁfth kind and rephrase Theorem 1.1 as Lemma 3.1. In
Section 4 we present Prouhet-Tarry-Escott (PTE-)sets, an extension of
ideal PTE-pairs. In Section 5 we consider standard pairs of the ﬁrst
and second kind where g need not satisfy (3). In the next section we
assume that g satisﬁes (3) too. Section 7 deals with standard pairs
of the third and fourth kind where g need not satisfy (3). Section 8
restricts the cases with standard pairs of the third and fourth kind if
g has only simple rational roots, too. In Section 9 we give a more pre-
cise statement than Theorem 1.1 under (3) which completes the proof
of Theorem 1.1. We give an application of our results to equal prod-
ucts with terms belonging to blocks of consecutive integers of bounded
lengths in Section 10. We ﬁnish the paper with some conclusions and
open problems.
 2. Historical overview

There are numerous publications on the title equation where f has
only simple rational roots. In most of them the roots of f and g form
almost arithmetic progressions. This overview is far from complete and
the results in the mentioned papers are mostly more general than cited.

2.1. The roots of f form an arithmetic progression and g is
almost a perfect power. First we consider the case that the roots
of f form an arithmetic progression and g is almost a perfect power,
more precisely:

(4) x(x + d) · · · (x + (k − 1)d) = b0yℓ + bℓ

where b0, bℓ, d, k and ℓ are integers with k > 1, ℓ > 1, kℓ > 4, b0 ̸= 0 ℓ-
th power free, the greatest prime factor of b0 is at most k and solutions
(x, y) ∈ Z
2 satisfy gcd(x, d) = 1, y > 1. (If k = ℓ = 2, then we may
have a Pell equation which has inﬁnitely many solutions.) If bℓ = 0,

4 L. HAJDU AND R. TIJDEMAN

then there are only ﬁnitely many solutions according to a theorem of
Siegel [72] if ℓ > 2 and by a result of Schinzel [69], Corollary 7 if ℓ = 2.
Let d = 1. In 1975 Erd˝os and Selfridge [28] proved that equation
(4) has no solutions when b0 = 1, bℓ = 0. Erd˝os [26] for k ≥ 4 and
Gy˝ory [32] for k = 2, 3 showed that the equation (
x+k−1
k ) = yℓ, which
agrees with the case b0 = k!, bℓ = 0 in (4), has only the solution(
50
3 ) = 1402. Saradha [58] for k ≥ 4 and Gy˝ory [33] for k = 2, 3 proved
that equation (4) with b0 > 1, bℓ = 0 has no solution provided that
the greatest prime factor of the left-hand side is larger than k. Bilu,
Kulkarny and Sury [10] proved that equation (4) has only ﬁnitely many
solutions (k, ℓ, m, n) if bℓ is not a perfect power and that all solutions
can be explicitly determined. For more results with d = 1 see [19], [36],
[79].
Next let d > 1, b0 = 1, bℓ = 0. A famous result due to Euler is that
the product of four distinct positive integers in arithmetic progression
cannot be a square. Gy˝ory, Hajdu and Saradha [35] generalized this
by proving that the product of four or ﬁve consecutive terms of an
arithmetic progression with d, x coprime cannot be a perfect power.
This result has been extended to at most 11 terms by Bennett, Bruin,
Gy˝ory and Hajdu [7] and to at most 34 terms by Gy˝ory, Hajdu and
Pint´er [34]. Another generalization of Euler’s result in the square case
by Hirata, Laishram, Shorey and Tijdeman [45] extending [7], [34],
[54] is that equation (4) with 4 ≤ k ≤ 109, ℓ = 2 has no solutions.
For a similar result for ℓ = 3 see Hajdu, Tengely and Tijdeman [42],
and for ℓ = 5 see Hajdu and Kov´acs [37]. Bennett [6] obtained the
following strong ﬁniteness result: There exist at most ﬁnitely many
integer tuples d, k, ℓ, x, y, with 4 ≤ k ≤ 15177 for which equation (4) is
satisﬁed. Bennett and Siksek [8] proved for some eﬀectively computable
k0 that for ﬁxed k > k0 there are only ﬁnitely many integers d, ℓ, x, y
satisfying equation (4). For some other papers in this case see [30],
[58], [59], [70].
Case d > 1, b0 > 1. Saradha and Shorey [64] proved that for d at
most some explicitly given d0 = d0(ℓ) and bℓ = 0 equation (4) has no
solutions. It follows from Yuan [79] that if k ≥ 8 then all solutions
of (4) satisfy max(x, y, ℓ) < C where C is an eﬀectively computable
constant depending only on k, b0, bℓ. For other results with bℓ = 0 see
[30], [47], [53], [63], [64]. For a more complete survey of papers on
equation (4) see [71].

2.2. The roots of f form almost an arithmetic progression and
g is almost a perfect power. First we turn to the case that the
roots of f form an arithmetic progression with some terms missing,

THE DIOPHANTINE EQUATION f (x) = g(y) 5

more precisely, to the equation

(5) (x + d1d) · · · (x + dkd) = b0yℓ + bℓ
where 0 ≤ d1 < d2 < · · · < dk < K, d, b0, bℓ and ℓ are integers with
k > 2, ℓ > 1, b0 is ℓ-th power free, the greatest prime factor of b0 is at
most k and solutions (x, y) ∈ Z
2 satisfy gcd(x, d) = 1.
Several papers deal with the case K − k = 1. Saradha and Shorey
[61], Hanrot, Saradha and Shorey [44] and Bennett [5] together proved
that for d = K − k = b0 = 1, bℓ = 0 the only solutions of (5) are
given by 4!/3 = 23, 6!/5 = 122, 10!/7 = 7202. For other papers with
K − k = 1, bℓ = 0 see [21], [62], [63], [65], [67]. Hajdu and Papp [38]
proved that equation (5) with K − k = 1, K ≥ 8 has only ﬁnitely many
solutions x, y, ℓ.
Mukhopadhyay and Shorey [53] for ℓ = 2 and Saradha and Shorey
[66] for ℓ ≥ 3 determined all solutions of equation (5) with K − k = 2,
k ≥ 4, ℓ ≥ 3. For papers with K − k ≥ 2, bℓ = 0 see [3] and [20].
Hajdu, Papp and Tijdeman [39] provided eﬀective upper bounds for
max(|x|, |y|, ℓ) in (5) under the assumption that K − k < cK 2/3 for
some explicit c > 0.
In the case when instead of omitting terms from an arithmetic pro-
gression we have an extra term we recall some results concerning so-
called ﬁgurate numbers. The x-th ﬁgurate number with integer param-
eters k, m is deﬁned as fk,m(x) = x(x+1)...(x+k−2)((m−2)x+k+2−m)
k! . Note
that these numbers are generalizations of factorials, and have been in-
tensively studied by many authors. Here, in relation with (5) we only
mention that Hajdu and Varga [43] proved that the equation

(6) fk,m(x) = b0yℓ + bℓ
with k ≥ 3, m ≥ 4, b0, bℓ ∈ Q, b0 ̸= 0 has only ﬁnitely many solutions
(x, y, ℓ) ∈ Z
3 with ℓ ≥ 2, |y| > 1, unless (k, ℓ) = (3, 2) or (k, m, ℓ) =
(4, 4, 2), (4, 6, 2), (4, 4, 4). For many related results and history, see [43].

2.3. Both f and g have simple rational roots almost in arith-
metic progressions. In the literature many papers deal with special
cases of the equation

(7) a0x(x + d1) · · · (x + (k − 1)d1) = b0y(y + d2) · · · (y + (ℓ − 1)d2)

where k, ℓ, a0, b0 are integers with 1 < k ≤ ℓ, a0b0 ̸= 0, and d1, d2 are
positive integers with d1 ̸= d2 if k = ℓ.
First the case a0 = b0 = d1 = d2 = 1 attracted attention. In 1963
Mordell [52] proved that for (k, ℓ) = (2, 3) the only positive integer
solutions are given by (x, y) = (2, 1) and (14, 5). In 1972 Boyd and
Kisilevsky [14] proved that (x, y) = (2, 1), (4, 2), (55, 19) are the only

6 L. HAJDU AND R. TIJDEMAN

positive integer solutions if (k, ℓ) = (3, 4), while Hajdu and Pint´er [40]
showed that the only positive integer solution for (k, ℓ) = (4, 6) is (7, 2).
Several results are covered by the theorem of Saradha and Shorey [60]
that the only solution with ℓ = 2k is given by (k, ℓ, x, y) = (3, 6, 8, 1).
They, together with Mignotte (see [51]) determined all solutions in case
ℓ/k ∈ {3, 4, 5, 6}.
Saradha, Shorey and Tijdeman [68] studied the cases a0 = b0 = 1,
d1 = 1, d2 > 1, ℓ/k is integral. All cases with a0 = b0 = 1 were covered
by Beukers, Shorey and Tijdeman [9]. They proved that equation (7)
admits only ﬁnitely many positive integral solutions x, y except for the
inﬁnite class of solutions x = y2 +3d2y when k = 2, ℓ = 4 and d1 = 2d2
2.
By a similar reasoning the restriction a0 = b0 = 1 can be replaced by
ℓ > 2.
By taking a0 = ℓ!, b0 = k!, d1 = d2, m = x + k − 1, n = y + ℓ − 1 in
(7) the question becomes which binomial coeﬃcients are equal,

(8) (m
k
 ) = (
n
ℓ
).

Without loss of generality we assume 1 < k < ℓ, k ≤ m/2, ℓ ≤ n/2. In
1966 Avanesov [1] provided all solutions to equation (8) if (k, ℓ) = (2, 3),
and in 1963 Mordell [52] did so for the case (k, ℓ) = (3, 4). Stroeker
and de Weger [76] dealt with (k, ℓ) = (2, 6), (2, 8), (3, 6), (4, 6), (4, 8)
and Bugeaud, Mignotte, Siksek, Stoll and Tengely [17] solved the case
(k, ℓ) = (2, 5). Several pairs (k, ℓ) were treated by other authors.
Gallegos-Ruiz, Katsipis, Tengely and Ulas [31] completely solved the
equations (m
k
 ) = (n
ℓ
) + d, −3 ≤ d ≤ 3

for pairs (k, ℓ) = (2, 3), (2, 4), (2, 6), (2, 8), (3, 4), (3, 6), (4, 6), (4, 8). It
follows from their work that for every integer r the equation

(x + r)(x − r − 1) = 2(
y
5
)

has two surprising large solutions.1 Surveys on (almost) equal binomial
coeﬃcients are Blokhuis, Brouwer, de Weger [12]2 and Gallegos-Ruiz
et al. [31].

1Tengely tells us that the correct conjecture on page 434 of their paper reads
that the only solutions in positive integers of the equation (y
2) = (
x
5)+66 are (x, y) =
(1, 12), (2, 12), (3, 12), (4, 12), (11, 33), (28, 444), (7935, 723632383), (7939, 724544908).
Note that the equation (y + 11)(y − 12) = 2(
x
5) (i.e. r = 11) has the same solutions.
2In their list on page 2 the sporadic solution n = 78, k = 2, m = 15, ℓ = 5 is
missing.
 THE DIOPHANTINE EQUATION f (x) = g(y) 7

A generalization concerns the equation

fk,m(x) = fℓ,n(y)

of ﬁgurate numbers (deﬁned in the previous subsection). We only men-
tion that Hajdu, Pint´er, Tengely and Varga [41] obtained various ﬁnite-
ness results concerning this equation. For history and further related
results see [41].

2.4. The roots of f are simple and rational and g(y) ∈ Q[y].
Consider the equation

(9) f (x) := (x + d1d) · · · (x + dkd) = g(y)

in integers x, y where d, k, K, d1, d2, . . . , dk are integers with 0 ≤ d1 <
d2 < · · · < dk < K and k > 2, g(y) ∈ Q[y] of degree ℓ ≥ 2. Kulkarni
and Sury [46] proved that if d = 1, k = K, ℓ > 2 and (9) has inﬁnitely
many solutions, then either g = f (G) for some G(y) ∈ Q[y], or k is
even and g = ϕ(G) where

ϕ(x) =
 (
x − (1
2
 )2) (
x − (3
2
 )2)
 · · ·
 (
x − ( k − 1
2
 )2)

and G(y) ∈ Q[y] is a polynomial whose squarefree part has at most two
roots, or k = 4 and g(y) = bv(y)2 + 9/16 where b ∈ Q, b ̸= 0 and v is a
linear polynomial with rational coeﬃcients. They showed in particular
that there are only ﬁnitely many such solutions k, x, y if g is irreducible.
Hajdu, Papp and Tijdeman [39] proved the ﬁniteness of the number of
solutions of (9) under the assumption that K − k ≤ cK 2/3 with c an
explicit constant, provided that g does not belong to two explicitly
given classes in which there can be inﬁnitely many solutions. The
latter two papers are based on a theorem of Bilu and Tichy [11], which
will also play an important role in our present study and is formulated
in the next section. For other papers related to (9) see [3], [16], [56],
[57], [75]. For ﬁniteness results when f (x) in (9) is replaced by fk,m(x)
(related to ﬁgurate numbers), see [41], [43], and the references there.

2.5. Power values and equal values of products with terms
coming from an interval. Finally, we recall some papers and results
from the literature concerning products with terms coming from blocks
of consecutive integers. These are related to our results in Section 10.
First we mention a result of Erd˝os and Turk [29]. They (among
others) studied the existence of terms from ‘short’ intervals I having a
power product, and also the existence of two distinct sets of integers in
I with equal product. Roughly speaking, they proved that these prop-
erties never hold for ‘very short’ intervals; that they hold in inﬁnitely

8 L. HAJDU AND R. TIJDEMAN

many cases, but also fail in inﬁnitely many cases for ‘medium sized’
intervals; and that they always hold if the size of I is ‘large enough’.
They gave precise formulas for the sizes in their paper [29].
Another problem of somewhat similar ﬂavor is due to Erd˝os and
Graham [27], who asked when the product of two or more disjoint
blocks of consecutive integers can be a power inﬁnitely often. Ulas
[78] was the ﬁrst to provide examples yielding a positive answer: he
exhibited families of blocks of precisely four integers whose product
gives perfect squares. Bauer and Bennett [4] described the ‘minimal
examples’ yielding perfect square products. For related results, see [74],
[77] and the references there.

3. The Bilu-Tichy theorem

We say that a polynomial f as in (1) is symmetric, if there exists an
a ∈ Q such that the set {a1, . . . , ak} is symmetric around a.
We call polynomials f, ˜f ∈ Q[x] similar if there exist a, b ∈ Q, a ̸= 0
such that f (x) = ˜f (ax + b). Notation f ≃ ˜f . Obviously this induces
an equivalence relation on Q[x]. Observe that if f has only simple
rational roots, then ˜f has only simple rational roots too. In every
equivalence class there are polynomials with sum of roots equal to 0.
Moreover, if the roots of f are all rational, then there exists a similar
polynomial ˜f (x) ∈ Z[x] of which the roots are integers with sum 0.
If the polynomial equation f (x) = g(y) has inﬁnitely many solutions
(x, y) ∈ Q
2 with a bounded denominator and f ≃ ˜f , g ≃ ˜g, then the
equation ˜f (x) = ˜g(y) has also inﬁnitely many solutions (x, y) ∈ Q
2

with a bounded denominator. We call equations f (x) = g(y) and
˜f (x) = ˜g(y) with f ≃ ˜f , g ≃ ˜g similar equations.
We call f (x) ∈ Q[x] decomposable over Q if there exist G(x), H(x) ∈
Q[x] with deg(G) > 1, deg(H) > 1 such that f = G(H), and otherwise
indecomposable. Since deg(f ) = deg(G) · deg(H), f is indecomposable
if deg(f ) is prime.
Let δ be a non-zero rational number and µ be a positive integer.
Then the µ-th Dickson polynomial is deﬁned by

Dµ(x, δ) :=
 ⌊µ/2⌋∑

i=0 dµ,ix
µ−2i where dµ,i = µ
µ − i
(µ − i
i
 )(−δ)i.

For properties of Dickson polynomials see e.g. [50].
In this section we prove a variant of Theorem 1.1. In the proof the
following result of Bilu and Tichy [11] on equation (2) is crucial. Here

THE DIOPHANTINE EQUATION f (x) = g(y) 9

Kind Standard pair (unordered) Parameter restrictions
First (x
q, αx
pv(x)q) 0 ≤ p < q, (p, q) = 1,
p + deg(v) > 0
Second (x
2, (αx
2 + β)v(x)2) -
Third (Dµ(x, αν), Dν(x, αµ)) gcd(µ, ν) = 1
Fourth (α−µ/2Dµ(x, α), −β−ν/2Dν(x, β)) gcd(µ, ν) = 2
Fifth ((αx
2 − 1)3, 3x
4 − 4x
3) -
Table 1. Standard pairs. Here α, β are non-zero rational
numbers, µ, ν, q are positive integers, p is a non-negative inte-
ger, v(x) ∈ Q[x] is a non-zero, but possibly constant polyno-
mial.

the polynomials F, G ∈ Q[x] form a standard pair over Q if either
(F (x), G(x)) or (G(x), F (x)) appears in Table 1.

Theorem 3.1 (Bilu, Tichy [11], Theorem 1.1). Let f (x), g(x) ∈ Q[x]
be non-constant polynomials. Then the following two statements are
equivalent.

(I) The equation f (x) = g(y) has inﬁnitely many rational solutions
x, y with a bounded denominator.
(II) We have f = ϕ(F (κ)) and g = ϕ(G(λ)), where κ(x), λ(x) ∈
Q[x] are linear polynomials, ϕ(x) ∈ Q[x], and F (x), G(x) form
a standard pair over Q such that the equation F (x) = G(y) has
inﬁnitely many rational solutions with a bounded denominator.

Observe that F (κ) ≃ F and G(λ) ≃ G. The Bilu-Tichy theorem
implies that if (I) holds then the equation F (κ(x)) = G((λ(y)) has
inﬁnitely many rational solutions with a bounded denominator. The
converse is obvious.
In Theorem 1.1 one may read m = deg(F ), n = deg(G), s = deg(ϕ).

An interesting result in connection with Theorem 3.1 is due to Avanzi
and Zannier [2]. Namely, Theorem 1 of [2] implies that if the equation
f (x) = g(y) with f (x), g(x) ∈ Q[x], gcd(k, ℓ) = 1 and k, ℓ > 6 has
inﬁnitely many rational solutions, then inﬁnitely many of them have a
bounded denominator. (Cf. Bilu’s MathSciNet review MR1845348 of
that paper.)

We start with investigating when the equation

(10) F (x) = G(y)

10 L. HAJDU AND R. TIJDEMAN

for standard pairs (F, G) has inﬁnitely many solutions (x, y) with a
bounded denominator in our settings. Lemma 3.1 shows that condition
(1) restricts the possibilities.

Lemma 3.1. Suppose f is of the form (1) and equation (2) has inﬁn-
itely many rational solutions with a bounded denominator. Let (F, G)
be a corresponding standard pair. Then one of the following cases holds:
1) (F, G) is of the ﬁrst or second kind, min(deg(F ), deg(G)) ≤ 2,
2) (F, G) is of the third or fourth kind.

Proof. Without loss of generality we may assume f = ϕ(F ), g = ϕ(G).
Since f has only simple rational roots, f ′ = ϕ′(F )F ′ has only simple
real roots. Hence F ′ has only simple real roots. If (F, G) is of the ﬁfth
kind, then F ′ has a multiple root and so the ﬁfth kind is excluded.
Therefore, if we are not in case 2), we have a pair (F, G) of the ﬁrst or
second kind. By 1) we may assume that deg(F ) ≥ 3 and deg(G) ≥ 3.
Then (F, G) is not of the second kind. If (F, G) is of the ﬁrst kind, then
q ≥ 3 and if deg(v) = 0 then p ≥ 3. However, then F ′ has a multiple
root, which is not the case. □

Remark 3.1. It follows that if (F, G) is a standard pair of the ﬁrst or
second kind, then deg(f ) | 2 deg(g) or deg(g) | 2 deg(f ).

Remark 3.2. In Examples 1.1, 1.2, 1.3 we may take

F (x) = x
2, G(y) = y(y − 7)2, ϕ(x) = x − 36,

F (x) = x
2, G(y) = 2y2 − 1, ϕ(x) = (x − 1)(x − 49),

F (x) = D3(x, 134), G(y) = D4(y, 133), ϕ(x) = x − 1111682,
respectively.
 4. ptek polynomial sets

Let f (x) ∈ Q[x] with only simple rational zeros be decomposable
over Q as ϕ(F (x)). Let

ϕ(x) = p0(x − p1)(x − p2) · · · (x − ps)

with s > 0, p0 ∈ Q (p0 ̸= 0) and pi ∈ C (i = 1, . . . , s). Then

f (x) = p0(F (x) − p1)(F (x) − p2) · · · (F (x) − ps).

From this, we see that pi ∈ Q (i = 1, . . . , s), and that these numbers
are distinct. Further, writing Fi(x) = F (x) − pi for i = 1, 2, . . . , s we
obtain that F1(x), F2(x), . . . , Fs(x) ∈ Q[x] are such that Fi(x)/Fj(x) /∈
Q, Fi(x) − Fj(x) ∈ Q for 1 ≤ i < j ≤ s and, moreover, Fi(x) has
only simple rational roots for 1 ≤ i ≤ s. These polynomials have the

THE DIOPHANTINE EQUATION f (x) = g(y) 11

same degree, m say. It follows that there are rationals r1, r2, . . . , rm
independent of i such that Fi(x) = rmx
m + rm−1x
m−1 + . . . + r1x + fi
for all i with f1, f2, . . . , fs ∈ Q distinct. We call f a PTEm-polynomial,
{F1, F2, . . . , Fs} a PTEm set and F a PTEs component of f . Of course
deg(f ) = ms. Note that every polynomial with only rational roots is
a PTE1 component of itself. On the other hand, PTEm polynomials of
degree > m > 1 are decomposable.
If {F1, F2, . . . , Fs} is a PTEm set, then the ﬁrst m − 1 symmetric
polynomials of the roots of Fi(x) are independent of i. By the formulas
of Newton-Girard we obtain that the sum of the j-th powers of the roots
of Fi are independent of i for j = 1, 2, . . . , m − 1. In case all the roots
are rational, the union of the sets of roots is called an ideal Prouhet-
Tarry-Escott set. Ideal Prouhet-Tarry-Escott pairs (i.e. corresponding
to the case s = 2) are known for 2 ≤ m ≤ 10 and for m = 12.
For general information on the PTE-problem we refer to [55]. In this
section we shall show that for m ∈ {3, 4, 6} we can construct arbitrarily
large integral PTEm sets, that is s sets of m integers having the same
sums of j-th powers for 1 ≤ j ≤ m − 1, with s arbitrary. In our
construction r2 = 0 for m = 3 and for m = 4, 6 we have pκ+m/2 = −pκ
for κ = 1, 2, . . . , m/2 and therefore ri = 0 for i odd. Note that PTEm
sets turn into PTEm sets under linear transformations. Therefore, if
there exists a PTEm set of m rationals, there exists a similar PTEm
set of m integers. (In the literature, see [55], PTEm sets of integers are
considered. However, in view of the last remark, one can work with
rational PTEm sets as well.)

Case m = 4. Choosing F as an even polynomial, it suﬃces to prove
that for any s there are s monic polynomials Fi(x) of degree 4 with
distinct integer roots αi1, αi2, −αi1, −αi2 such that 2α2
i1 + 2α2
i2 has the
same value, independent of i. Let M be the product of ρ distinct primes
of the form ≡ 1 (mod 4). Then the number of representations of M
as α2
1 + α2
2 with α1, α2 ∈ Z, α1 > α2 > 0, gcd(α1, α2) = 1 equals 2ρ−1

according to Theorem 7.5 of [49]. Thus for every ρ we can construct
2ρ−1 distinct primitive polynomials Fi of degree 4 diﬀering only in their
constant terms.

Example 4.1. We have

5 · 13 · 17 = 1105 = x
2 + y2 for (x, y) = (33, 4), (32, 9), (31, 12), (24, 23).

Hence the polynomial P (x) = x
4 − 1105x
2 has simple rational roots
when 17424, 82944, 138384 or 304704 is added, since the corresponding
polynomials equal

(x2−33
2)(x2−4
2), (x2−32
2)(x2−9
2), (x2−31
2)(x2−12
2), (x2−24
2)(x2−23
2),

12 L. HAJDU AND R. TIJDEMAN

respectively.

Case m = 6. It suﬃces to prove that for any s there are s monic
polynomials Fi(x) of degree 6 with distinct integer roots ±αi1, ±αi2,
±αi3 such that both ∑3
κ=1 α2
iκ and ∑3
κ=1 α4
iκ are independent of i. Let
M be the product of ρ distinct primes of the form ≡ 1 (mod 6). The
number of representations of M as x
2+xy+y2 with coprime integers x, y
with x > y > 0 equals 2ρ−1 (see [24] par. 48, item 4). Suppose (xi, yi)
is such a pair. Choose as roots of Fi the six integers ±xi, ±yi, ±(xi +
yi) for i = 1, 2, . . . , 2ρ−1. We have x
2
i + y2
i + (xi + yi)2 = 2M and
x
4
i + y4
i + (xi + yi)4 = M 2 (cf. Choudhry [18], Sec. 4). Thus both the
sum of the squares and the sum of the biquadrates of the roots of Fi
are independent of i. The formulas of Newton-Girard imply Fi(x) =
x
6 − 2Mx
4 + M 2x
2 − fi for distinct integers fi and all i. We conclude
that for every ρ we can construct 2ρ−1 distinct primitive polynomials of
degree 6 with integer roots, which diﬀer by their constant terms only.

Example 4.2. We have

7·13·19 = 1729 = x
2+xy+y2 for (x, y) = (40, 3), (37, 8), (32, 15), (25, 23).

Hence the polynomial P (x) = x
6 − 2 · 1729x
4 + 17292x
2 has simple
integer roots when 26625600, 177422400, 508953600 or 761760000 is
subtracted, since the corresponding polynomials equal

(x
2 − 32)(x
2 − 402)(x
2 − 432), (x
2 − 82)(x
2 − 372)(x
2 − 452),

(x
2 − 152)(x
2 − 322)(x
2 − 472), (x
2 − 232)(x
2 − 252)(x
2 − 482),
respectively.

Case m = 3. Take ρ distinct primes of the form ≡ 1 (mod 6). Then
as above we can construct s := 2ρ−1 distinct pairs (xi, yi) ∈ Z
2 with
xi > yi > 0 such that the sum x
2
i + xiyi + y2
i is equal to the product M
of these primes. Consider the triples

(M + xi(yi − xi), −M + yi(yi − xi), x
2
i − y2
i ) (i = 1, 2, . . . , s).

Each triple has sum 0 and sum of squares

2M 2 − 2M(x
2
i − 2xiyi + y2
i ) + 2x
4
i − 2x
3
i yi − 2xiy3
i + 2y4
i .

Using that M = x
2
i + xiyi + y2
i , we obtain that the sums of squares
equal 2M 2. Of course, this is also true for the opposite triples

−(M + xi(yi − xi)), M − yi(yi − xi), y2
i − x
2
i (i = 1, 2, . . . , s).

Thus the polynomial x
3 − M 2x has simple integer roots if 0 or

(M + xi(yi − xi))(M − yi(yi − xi))(x
2
i − y2
i )

THE DIOPHANTINE EQUATION f (x) = g(y) 13

is added or subtracted, for i = 1, 2, . . . , s.

Example 4.3. We start again from the pairs

(x, y) = (40, 3), (37, 8), (32, 15), (25, 23)

from Example 4.2 which all satisfy M = x
2+xy+y2 = 1729. According
to the above rules they lead to the nine triples

(−1729, 0, 1729), (±1840, ∓249, ∓1591), (±1961, ∓656, ∓1305),

(±1984, ∓1185, ∓799), (±1775, ∓96, ∓1679),
which all have sum 0 and sum of squares 2 · 17292 = 5978882. Thus
the polynomial P (x) = x
3 − 17292x has simple integer roots when one
from

0, ±728932560, ±1678772880, ±1878480960, ±286101600

is added. Namely, we get the polynomials (x − 1729)x(x + 1729),

(x ± 1840)(x ∓ 249)(x ∓ 1591), (x ± 1961)(x ∓ 656)(x ∓ 1305),

(x ± 1984)(x ∓ 1185)(x ∓ 799), (x ± 1775)(x ∓ 96)(x ∓ 1679),
respectively.

5. Standard pairs of the first or second kind

In this section we return to the original problem on equation (2) sub-
ject to (1) and show by the help of examples that all cases of the ﬁrst
or second kind which are not excluded may indeed occur. Suppose the
equation f (x) = g(y) with f (x), g(x) ∈ Q[x] has inﬁnitely many solu-
tions (x, y) ∈ Q
2 with a bounded denominator. According to Theorem
3.1 we have f = ϕ(F (κ)) and g = ϕ(G(λ)), where κ(x), λ(x) ∈ Q[x]
are linear polynomials, ϕ(x) ∈ Q[x], and F (x), G(x) form a standard
pair over Q such that the equation F (x) = G(y) has inﬁnitely many
rational solutions with a bounded denominator. In the sequel we sup-
pose that f = ϕ(F ) and g = ϕ(G). The results then extend to all
equations similar to the equation ϕ(F (x)) = ϕ(G(y)), in particular to
the original equation f (x) = g(y).
Let ϕ(x) = p0(x−p1) · · · (x−ps) with p0 ∈ Q (p0 ̸= 0), p1, . . . , ps ∈ C.
Then f (x) = p0(F (x) − p1) · · · (F (x) − ps). Since f has only simple
rational roots, pi is in fact rational, F (x) − pi has only simple rational
roots and is a PTEs component of f for i = 1, . . . , s. We assume
that (F, G) is a standard pair of the ﬁrst or second kind and consider
successively the cases deg(F ) = 1, deg(F ) = 2 and deg(F ) > 2. As
we shall see, in each case deg(ϕ) can attain any positive integer value,
hence deg(f ), deg(g) can each be arbitrarily large.

14 L. HAJDU AND R. TIJDEMAN

Case deg(F ) = 1. The standard pair is of the ﬁrst kind and we may
assume that F (x) = x. Then f = ϕ. Hence for every X ∈ Z equation
F (x) = G(y) has as solution (x, y) = (G(X), X). Thus equation f (x) =
g(y) has also solution (x, y) = (G(X), X) for every X ∈ Z. Here the
choice of G(y) ∈ Q[y] is free, deg(f ) | deg(g) and deg(f ), deg(g) can
be arbitrarily large.

Example 5.1. For every set of nonzero rationals {a1, a2, . . . , ak} the
equation

(x − a1)(x − a2) · · · (x − ak) = (G(y) − a1)(G(y) − a2) · · · (G(y) − ak),

for G(y) ∈ Q[y] with deg(G) ≥ 1 arbitrary, has solutions (x, y) =
(G(X), X) (X ∈ Z). Here ϕ(x) = f (x), F (x) = x. Writing n =
deg(G), we have deg(f ) = k | nk = deg(g), where k and n can be
arbitrary.
Example 5.2. We start out from two triples from Example 4.3,
(1840, −249, −1591) and (1961, −656, −1305) both having sum zero
and equal sums of squares. Let
(11)
f (x) = (x
2−18402)(x
2−2492)(x
2−15912)(x
2−19612)(x
2−6562)(x
2−13052).

Since v(x) ± 728932560 and v(x) ± 1678772880 with v(x) = x
3 − 17292x
are given by

(x ± 1840)(x ∓ 249)(x ∓ 1591), (x ± 1961)(x ∓ 656)(x ∓ 1305),

respectively, we see that

f (x) = (v(x)2 − 7289325602)(v(x)2 − 16787728802).

Hence, putting F (x) = v(x), G(y) = y,

g(x) = ϕ(x) = (x
2 − 7289325602)(x
2 − 16787728802),

we obtain that the equation f (x) = g(y) has inﬁnitely many integral
solutions, given by (x, y) = (X, v(X)) (X ∈ Z). Here both f and g
have only simple rational roots.

Case deg(F ) = 2. Then either F (x) = x
2 or F (x) = αx
2 + βx + γ,
G(y) = yq with α ̸= 0, q ∈ Z>0. In the latter case we ﬁrst use that
F (x) ≃ x
2 + c for some c ∈ Q. Here p = 0, q = 1, deg(v) = 2 if
(F, G) is of the ﬁrst kind and deg v = 0 if (F, G) is of the second kind.
Subsequently we replace ϕ(x) by ϕ(x − c) by which we get F (x) =
x
2, G(y) = yq − c. Thus we may choose F (x) = x
2 in both cases.
We obtain that f (x) is of the form

ϕ(F (x)) = p0(x
2 − p1) · · · (x
2 − ps)

THE DIOPHANTINE EQUATION f (x) = g(y) 15

has only simple rational roots. It follows that p1, p2, . . . , ps are squares
of distinct rational numbers and that the roots ±b1, ±b2, . . . , ±bs of f
are symmetric around 0. Furthermore, g(y) = p0(G(y) −b
2
1) · · · (G(y) −
b
2
s). By Theorem 3.1 the equation x
2 = G(y) has to have inﬁnitely many
rational solutions x, y with a bounded denominator. Let Xi, Yi (i =
1, 2, . . . ) be such solutions. By the main result of LeVeque [48] (for the
eﬀective version see Brindza [15]) we obtain that the polynomial G can
have at most two roots of odd multiplicities. It follows that the equation
f (x) = g(y) has inﬁnitely many rational solutions (x, y) = (Xi, Yi)
(i = 1, 2, . . . ) with a bounded denominator. Writing n = deg(G),
we have deg(f ) = 2s | 2ns = 2 deg(g). In this case s and n can be
arbitrary, and hence deg(f ), deg(g) may be arbitrarily large.

Example 5.3. Let

F (x) = x
2, G(y) = yv2(y), ϕ(x) = (x − b
2
1) · · · (x − b
2
s)

for some v(y) ∈ Q[y] and distinct positive rationals b1, b2, . . . , bs. Then

f (x) = (x−b1)(x+b1) · · · (x−bs)(x+bs), g(x) = (G(y)−b
2
1) · · · (G(y)−b
2
s),

and f (x) = g(y) has solutions (Xv(X 2), X 2) for every X ∈ Z.

Example 5.4. Let

F (x) = x
2, G(y) = (2y2 − 1)v2(y), ϕ(x) = (x − b
2
1) · · · (x − b
2
s)

for some v(y) ∈ Q[y] and distinct positive rationals b1, b2, . . . , bs. Let
(Xi)∞
i=1 be distinct integers such that 2Y 2
i − 1 = X 2
i for integers Yi.
Then

f (x) = (x−b1)(x+b1) · · · (x−bs)(x+bs), g(x) = (G(y)−b
2
1) · · · (G(y)−b
2
s),

and f (x) = g(y) has solutions (Xiv(Yi), Yi) for i = 1, 2, . . . .

Note that Examples 5.3 and 5.4 are generalizations of Examples 1.1
and 1.2, respectively. See also Remark 3.2.

Case deg(F ) > 2. Here either F (x) = x
q for some q > 2 or G(x) = x
q

for some positive integer q.
If F (x) = x
q, then f (x) = p0(x
q − p1)(x
q − p2) · · · (x
q − ps) has
simple rational roots which implies q ≤ 2, but since deg(F ) > 2 this
is not possible. If G(x) = x
q, then from Table 1 we see that either
F (x) = αx
pv(x)q with 0 ≤ p < q, (p, q) = 1 (if (F, G) is of the ﬁrst
kind), or q = 2 and F (x) = (αx
2 + β)v(x)2 (if (F, G) is of the second
kind). Since f has simple rational roots, f ′ = ϕ′(F )F ′ has only simple
real roots and therefore F ′ has only simple real roots. So q ≤ 2 and in
view of deg(F ) > 2, we have only the following possibilities:
a) G(x) = x and F (x) = αv(x) has only simple rational roots.

16 L. HAJDU AND R. TIJDEMAN

b) G(x) = x
2 and F (x) is αxv(x)2 or (αx
2 + β)v(x)2.
In any case, F is a PTEs component of f . Observe in particular that
in case a) we have ϕ = g, so that it also suﬃces that F is a PTEs
component of f , thus the roots of f form an ideal PTEs set. In case
a) we clearly have deg(g) | deg(f ), while in case b), obviously deg(g) |
2 deg(f ) holds. From the examples it will be clear that the degree of ϕ
can be arbitrary, hence the degrees of f, g can be arbitrarily large.

Example 5.5. First we give an example for a). We start from two
triples from Example 4.3,

(−1729, 0, 1729), (1840, −249, −1591),

both having sum 0 and sum of squares 2 · 17292. So letting

f (x) = (x + 1729)x(x − 1729)(x − 1840)(x + 249)(x + 1591)

and g(y) = y(y − 728932560), we have ϕ = g, F (x) = x
3 − 17292x,
G(y) = y. The equation f (x) = g(y) has solution (x, y) = (X, F (X))
for every X ∈ Z. Also g has only simple integer roots.

In case b), we give examples to show that both possibilities for the
choice of F (x) are possible. Recall that in both cases we have G(y) =
y2.

Example 5.6. F (x) = αxv(x)2. Let

f (x) = (x−2492)(x−15912)(x−18402)(x−6562)(x−13052)(x−19612).

Observe that we simply wrote x in place of x
2 in (11). Then by

(x − 18402)(x − 2492)(x − 15912) = x(x − 17292)2 − 7289325602,

(x
2 − 19612)(x − 6562)(x − 13052) = x(x − 17292)2 − 16787728802

we obtain that setting

F (x) = x(x − 17292)2, ϕ(x) = (x − 7289325602)(x − 16787728802),

and g(y) = (y2 − 7289325602)(y2 − 16787728802),
the equation f (x) = g(y) has inﬁnitely many solutions given by (x, y) =
(X 2, X(X 2 − 17292)) (X ∈ Z). Again g has only simple rational roots.

Example 5.7. F (x) = (αx
2 + β)v(x)2. We use data from Example
4.1. We start from 1105 = 332 + 42 = 322 + 92, and put

f (x) = 262(x
2 − 332)(x
2 − 42)(x
2 − 322)(x
2 − 92).

Then f has only simple rational roots. Put

F (x) = 26x
2(x
2−1105), ϕ(x) = (x+26·(33·4)2)(x+26·(32·9)2), g(y) = ϕ(y2).

THE DIOPHANTINE EQUATION f (x) = g(y) 17

A Magma [13] calculation shows that the equation

26(x
2 − 1105) = Y 2

has solutions (x, y) = (Xi, Yi) (i ∈ Z), with (X1, Y1) = (247, −1248),
(X2, Y2) = (117, 572), and

(Xi, Yi) = 102(Xi−1, Yi−1) − (Xi−2, Yi−2) (i ∈ Z>2).

So the equation f (x) = g(y) has inﬁnitely many integral solutions
(X, Y ) = (Xi, XiYi).

6. Both f and g have only simple rational roots and
(F, G) is of the first or second kind

In this section we consider equation (2) with both f and g having
only simple rational roots. Without loss of generality we may assume
deg(f ) ≤ deg(g), hence deg(F ) ≤ deg(G). We again assume f =
ϕ(F ), g = ϕ(G).

Theorem 6.1. Let f (x), g(x) ∈ Q[x], both having only simple ratio-
nal roots. Suppose that the equation f (x) = g(y) has inﬁnitely many
rational solutions x, y with a bounded denominator and that the cor-
responding standard pair (F (x), G(x)) ∈ Q[x] is of the ﬁrst or second
kind. Then we can choose F, G, ϕ such that one of the following items
holds:
1. deg(f ) | deg(g), there exist p0 ∈ Q, p0 ̸= 0 and distinct p1, p2, . . . , ps ∈
Q such that

(12) f (x) = p0
 s∏

i=1(x − pi), g(y) = p0
 s∏

i=1(G(y) − pi),

F (x) = x and (G(y) − pi)s
i=1 forms a PTEn set, where n = deg(G), for
every X ∈ Z the equation f (x) = g(y) has solution (x, y) = (G(X), X).
2. deg(f ) | 2 deg(g), there exist q0 ∈ Q, q0 ̸= 0 and distinct q1, q2, . . . , qs ∈
Q>0 such that

(13) f (x) = q0
 s∏

i=1(x − qi)(x + qi), g(y) = q0
 s∏

i=1(G(y) − q2
i ),

F (x) = x
2, G(y) ∈ Q[y] has at most two roots of odd multiplicities,
(G(y) − q2
i )s
i=1 forms a PTEn set, the equation x
2 = G(y) has in-
ﬁnitely many rational solutions (x, y) = (Xi, Yi) (i = 1, 2, . . . ) with
a bounded denominator and the equation f (x) = g(y) has solutions
(x, y) = (Xi, Yi) (i = 1, 2, . . . ) too.

18 L. HAJDU AND R. TIJDEMAN

Proof. By Lemma 3.1 we know that deg(F ) ≤ 2.
If deg(F ) = 1, then (using the notation of Table 1) we have p = 0,
q = 1, F (x) = x, G = v, f = ϕ and G(y) − p1, . . . , G(y) − ps form a
PTEn set. Then f, g are as in (12). For every X ∈ Z there is a solution
(x, y) = (G(X), X) to the equation. This case is covered by 1.
If deg(F ) = 2 then we may assume F (x) = x
2 according to the argu-
ment given in the preceding section. As before, we see that p1, p2, . . . , ps
are squares in Q. Let pi = q2
i for i = 1, 2, . . . , s. Then f, g are as in
(13) where G(y) − q2
1, . . . , G(y) − q2
s form a PTEn set. Further, by
Theorem 3.1 we know that the equation x
2 = G(y) has inﬁnitely many
solutions in rationals x, y with a bounded denominator. Clearly, these
solutions will be solutions to the original equation, too. The main re-
sult of LeVeque [48] shows that G(y) can have at most two roots of
odd multiplicities. This is covered by 2. □

The following example illustrates that the results in Section 4 imply
that there are instances for deg(F ) = 1 with deg(G) ∈ {3, 4, 6} and
arbitrary deg(ϕ) (and hence arbitrarily large deg(f ), deg(g) as well).
This is obvious for deg(G) = 2, cf. Example 5.1.

Example 6.1. (Cf. Examples 4.1, 4.2 and 4.3.) For deg(G) = 4
choose G(y) = y4 − 1105y2, F (x) = x and

f (x) = ϕ(x) = (x + 17424)(x + 82944)(x + 138384)(x + 304704).

Then g(y) = ϕ(G(y)) is given by

(y2−332)(y2−42)(y2−322)(y2−92)(y2−312)(y2−122)(y2−242)(y2−232).

For every integer X we obtain a solution (x, y) = (G(X), X) of equation
(2). It is obvious that the roots of g are symmetric around 0.
Similarly, for deg(G) = 6 choose

G(y) = y6 − 2 · 1729y4 + 17292y2, F (x) = x,

f (x) = ϕ(x) = (x−26625600, (x−177422400)(x−508953600)(x−761760000).
Then g(y) = ϕ(G(y)) is the polynomial g(y) = ∏

a∈T (y2 − a
2) with
T = {3, 40, 43, 8, 37, 45, 15, 32, 47, 23, 25, 48}. Again, for every integer
X we obtain a solution (x, y) = (G(X), X) of equation (2).
Finally, for deg(G) = 3 let G(y) = y3 − 17292y, F (x) = x,

f (x) = ϕ(x) =

x(x
2−7289325602)(x
2−16787728802)(x
2−18784809602)(x
2−2861016002),

and so g(y) = y ∏

a∈T (y2 − a
2) with

T = {1729, 1840, 249, 1591, 1961, 656, 1305, 1984, 1185, 799, 1775, 96, 1679}.

THE DIOPHANTINE EQUATION f (x) = g(y) 19

Also in this case, for every integer X we obtain a solution (x, y) =
(G(X), X) of equation (2).

Now we turn to the case deg(F ) = 2. Our examples will show that
in all the possible cases, deg(ϕ) can be arbitrary (whence deg(f ) and
deg(g) can be arbitrarily large). Note that deg(G) ≥ 2. Interchanging
the roles of F and G if necessary if deg(F ) = deg(G) = 2, by the
analysis in the cases deg(F ) = 2 and deg(F ) > 2 in Section 5, we see
that G is of the form αxv(x)2 or (αx
2+β)v(x)2. The case where G(x) is
of the shape αxv(x)2 is covered by Example 5.6. The other possibility
is that G(x) is of the shape (αx
2 + β)v(x)2. The next example, which
is another generalization of Example 1.2, treats this situation with
deg(v) = 0.

Example 6.2. Suppose that the equation x
2 = ay2 + b with a, b ∈ Z,
ab ̸= 0 has solutions (Xi, Yi)∞
i=1 ∈ Z
2. Let s ≥ 1, F (x) = x
2, G(y) =
ay2 + b, ϕ(x) = ∏s
i=1(x − X 2
i ). Then we have

f (x) =
 s∏

i=1(x
2 − X 2
i ), g(y) =
 s∏

i=1(ay2 + b − X 2
i ) = a
s s∏

i=1(y2 − Y 2
i ).

So f (x) and g(y) both have simple rational roots. Further, clearly,
the equation f (x) = g(y) has as solutions (Xi, Yi) for all i = 1, 2, . . . .
We see that deg(ϕ) can be arbitrary, hence deg(f ) and deg(g) can be
arbitrarily large.

7. Standard pairs F, G of the third or fourth kind

To handle the cases corresponding to standard pairs of the third and
fourth kind, we apply the following result.

Lemma 7.1. Let a1, . . . , aN be distinct rationals, and assume that with
some rational numbers u1, u2, v1, v2, b with u1v1b ̸= 0 we have

(14) u1DN (x, b) + u2 = (v1x + v2 − a1) · · · (v1x + v2 − aN ),

where DN (x, b) is the N-th Dickson polynomial with parameter b. Then
N ∈ {1, 2, 3, 4, 6}.

Note that N ≤ 12 is already proved in [39] (see the proof of Theorem
2.3 there). However, in this paper we need a more precise statement.
To keep the presentation self-contained, we include the complete proof
of the statement.
For appropriate choices of the parameters the cases N ∈ {1, 2, 3, 4, 6}
are possible. In Theorem 7.1 we describe these cases completely.

20 L. HAJDU AND R. TIJDEMAN

Proof of Lemma 7.1. Writing wi = (v2 − ai)/v1 (i = 1, . . . , N) and
u = u2/vN
1 , dividing both sides of (14) by vN
1 and using that DN is
monic, we get the similar equation

(15) DN (x, b) + u = (x + w1) . . . (x + wN ).

Here u ∈ Q and w1, . . . , wN are distinct rationals.
Applying the well-known identity

DN
 (
y + b
y , b
) = yN + ( b
y
 )N

to (15), we obtain

(16) y2N + uyN + b
N =
 N∏

i=1(y2 + wiy + b) .

Write ζ, ξ for the roots of the polynomial Y 2 + uY + b
N . Clearly, ζ, ξ
are algebraic numbers of degrees at most two. Further, b ̸= 0 yields
ζξ ̸= 0. Also observe that ζ ̸= ξ, since the numbers wi in (15) are
distinct. If u = 0, then the roots of the left-hand side of (16) are given
by

(17) ηj√
b (j = 0, 1, . . . , 2N − 1),

where √b denotes one of the (complex) squareroots of b, and η is a
primitive 2N-th root of unity. In view of the right-hand side of (16),
we see that the numbers (17) are algebraic numbers of degrees at most
two. Hence ϕ(2N) = deg(η) ≤ 4. This implies N ∈ {1, 2, 3, 4, 6}.
So from this point on, we assume ζ + ξ = u ̸= 0. Then the roots of
the polynomial on the left hand side of (16) are given by

ζ0εi and ξ0εi (i = 0, 1, . . . , N − 1),

where ζ0 and ξ0 are N-th roots of ζ and ξ, respectively, and ε is a
primitive N-th root of unity. Since these are the roots of the polynomial
on the right hand side of (16), they are distinct algebraic numbers of
degrees at most two. In particular, ζ0 and ζ0ε are at most quadratic
algebraic numbers, so the degree of ε is at most four. Hence ϕ(N) ≤ 4,
and we obtain N ∈ {1, 2, 3, 4, 5, 6, 8, 10, 12}.
To reﬁne the restriction for N, we need a more careful consideration.
Write ζ1 := ζ0ε. Then we see that

(18) ε = ζ1
ζ0
belongs to the number ﬁeld K := Q(ζ0, ζ1). Observe that if ζ0 ∈ Q(ζ1),
then ε is (at most) quadratic, yielding ϕ(N) ≤ 2, and our claim follows.

THE DIOPHANTINE EQUATION f (x) = g(y) 21

So we may assume that deg(K) = 4, and also that K = Q(ε) and that
ζ0 is quadratic. Denoting its algebraic conjugate by ¯ζ0, we have

(ζ0)N = ζ N
0 = ¯ζ = ξ.

Therefore, without loss of generality we may assume that ξ0 = ζ0 holds,
in particular, that ζ0 and ξ0 belong to the same quadratic subﬁeld of
K. From this point on, we shall use this assumption. We deal with the
remaining cases in turn. For the calculations we used Magma [13].
If N = 5, 10, then K is deﬁned by x
4 + x
3 + x
2 + x + 1. The only
quadratic subﬁeld of K is given by T1 := Q(√5). So now ζ0, ξ0 ∈ T1.
Recall that ζ0, hence also ξ0 is not rational. However, the (unique)
factorization of

(19) P (x) := x
2N + ux
N + b
N = (x
N − ζ N
0 )(x
N − ξN
0 )

(into irreducible factors) in T1[x] contains both for N = 5 and for
N = 10 the factors

x
2 + (3 − √5)ζ0x + ζ 2
0 and x
2 + (3 − √5)ξ0x + ξ2
0.

Here the constant terms of the quadratic factors are not equal. Indeed,
otherwise ζ 2
0 = ξ2
0 would imply ζ0 = ±ξ0, whence ζ = ±ξ, which is
excluded. Hence we see that (16) is not possible in these cases.
Let now N = 8. Then K is deﬁned by x
4 + 1. The number ﬁeld
K has three quadratic subﬁelds, namely T2 = Q(i), T3 = Q(√2) and
T4 = Q(i
√2). Following the argument given above for the factorization
of P (x) deﬁned by (19) we get that

• x
2 + iζ 2
0 and x
2 + iξ2
0 are factors of P (x) in T2[x],
• x
2 + ζ 2
0 and x
2 + ξ2
0 are factors of P (x) in T3[x] and T4[x],

assuming that ζ0, ξ0 ∈ T2, T3, T4, respectively. In all cases the constant
terms of the quadratic factors are not the same. So N = 8 is also
impossible.
Finally, let N = 12. Then K is deﬁned by x
4 − x
2 + 1. The number
ﬁeld K has three quadratic subﬁelds, namely T5 = Q(i), T6 = Q(√3)
and T7 = Q(i
√3). Now, similarly as before, for the factorization of
P (x) given by (19) we obtain that

• x
2 + ζ0x + ζ 2
0 and x
2 + ξ0x + ξ2
0 are factors of P (x) in T5[x],
• x
2 + ζ 2
0 and x
2 + ξ2
0 are factors of P (x) in T6[x] and T7[x],

assuming that ζ0, ξ0 ∈ T5, T6, T7, respectively.
Again, in all cases we observe that the constant terms of the quadratic
factors are not identical. So N = 12 is excluded, too. □

22 L. HAJDU AND R. TIJDEMAN

Theorem 7.1. Let N ∈ {3, 4, 6}. For any w1, w2 ∈ Q we can choose
w3, . . . , wN , b, u ∈ Q such that (15) holds. On the other hand, this
provides the only solutions of equation (15).

The cases N = 1 and N = 2 are trivial. Indeed, for N = 1 we
have D1(x, b) = x, so w1 = u can be any rational number. Further, for
N = 2 we have D2(x, b) = x
2−2b, whence w1+w2 = 0, w1w2 = −2b+u.
Therefore all cases of (15) are given by

(x + w1)(x − w1) = D2(x, b) + (2b − w2
1),

i.e. with u = 2b − w2
1 for arbitrary b, w1 ∈ Q.

Proof of Theorem 7.1. We consider the possibilities in turn.
The case N = 3. We have

(20) D3(x, b) = x
3 − 3bx,

hence

w1 + w2 + w3 = 0, w1w2 + w1w3 + w2w3 = −3b, w1w2w3 = u.

This gives

(21) w3 = −w1 − w2, b = (w2
1 + w1w2 + w2
2)/3, u = −w2
1w2 − w1w2
2.

Thus we have for any w1, w2 ∈ Q that

(22) (x + w1)(x + w2)(x − w1 − w2) = D3(x, b) + u

and this provides all possibilities for (15).
The case N = 4. We have

(23) D4(x, b) = x
4 − 4bx
2 + 2b
2.

This implies w1 + w2 + w3 + w4 = 0

and w1w2w3 + w1w2w4 + w1w3w4 + w2w3w4 = 0.

It follows that

0 = w1w2w3−(w1w2+w1w3+w2w3)(w1+w2+w3) = −(w1+w2)(w1+w3)(w2+w3).

We assume, without loss of generality,

(24) w1 + w3 = 0, hence w2 + w4 = 0.

Further comparison of coeﬃcients gives

(25) b = −w1w2 + w1w3 + w1w4 + w2w3 + w2w4 + w3w4
4 = w2
1 + w2
2
4

THE DIOPHANTINE EQUATION f (x) = g(y) 23

and
(26)

u = w1w2w3w4 − 2b
2 = w2
1w2
2 − 1
8 (w2
1 + w2
2)2 = −1
8 (w4
1 − 6w2
1w2
2 + w4
2).

For any w1, w2 ∈ Q and b, u chosen as above we have

(27) (x + w1)(x − w1)(x + w2)(x − w2) = D4(x, b) + u

and this provides all possibilities for (15).
The case N = 6 is the most involved one. We have

(28) D6(x, b) = x
6 − 6bx
4 + 9b
2x
2 − 2b
3.

On the other hand, the roots of the polynomial on the left hand side
of (16) are given by

±ζ0, ±ζ0ε, ±ζ0ε2, ±ξ0, ±ξ0ε, ±ξ0ε2,

where ε is a primitive sixth root of unity (i.e. a root of x
2 − x + 1), and
either ζ0, ξ0 ∈ Q, or they are conjugated quadratic algebraic numbers
from the ﬁeld K = Q(ε). Anyhow, the factorization of the polynomial
on the right hand side of (16) over K reads as

(y − ζ0)(y + ζ0)(y − ζ0ε)(y + ζ0ε)(y − (1 − ε)ζ0)(y + (1 − ε)ζ0)·

· (y − ξ0)(y + ξ0)(y − ξ0ε)(y + ξ0ε)(y − (1 − ε)ξ0)(y + (1 − ε)ξ0).

Note that the (algebraic) conjugate of ε is 1 −ε. Hence we immediately
get that the right hand side of (16) is given by

(y2 − (ζ0 + ξ0)y + ζ0ξ0)(y2 + (ζ0 + ξ0)y + ζ0ξ0)·

· (y2 − (ζ0ε + ξ0(1 − ε))y + ζ0ξ0)(y2 + (ζ0ε + ξ0(1 − ε))y + ζ0ξ0)·

· (y2 − (ζ0(1 − ε) + ξ0ε)y + ζ0ξ0)(y2 + (ζ0(1 − ε) + ξ0ε)y + ζ0ξ0).

Here all the above quadratic polynomials have rational coeﬃcients. The
coeﬃcients of y are just the numbers wi from (16) (and (15)). Observe
that (by choosing an appropriate indexing) we have

(29) w3 = w1 + w2, w4 = −w1, w5 = −w2, w6 = −w3
in (15). Put W = w2
1 + w1w2 + w2
2. A simple calculation yields that

(x + w1)(x + w2)(x + w3)(x + w4)(x + w5)(x + w6) =

= x
6 − 2W x
4 + W 2x
2 − w2
1w2
2(w1 + w2)2.

Comparing the coeﬃcients with D6(x, b)+u = x
6−6bx
4+9b
2x
2−2b
3+u
we see that

(30) b = W
3 , u = 2W 3

27 − w2
1w2
2(w1 + w2)2.

24 L. HAJDU AND R. TIJDEMAN

On the other hand, for any w1, w2 ∈ Q we have, choosing b and u as
in (30), that
(31)
(x+w1)(x−w1)(x+w2)(x−w2)(x+w1+w2)(x−w1−w2) = D6(x, b)+u.

Thus this provides all possibilities for (15) if N = 6. □

We give some examples to show that for deg(F ) = m ∈ {3, 4, 6}
equation (2) with f of the form (1) can have inﬁnitely many solutions
(x, y) ∈ Q
2 with a bounded denominator. For the sake of completeness,
we shall do so both for the third and for the fourth kind. By the gcd
condition in Table 1, deg(F ) = m = 3 cannot occur in the latter case.

Example 7.1. Let (F, G) be a standard pair of the third kind, deg(F ) =
m = 3, deg(G) = n = 4 and b = 7. We have

3b
4 = 3 · 74 = 142 + 14 · 77 + 772 = 232 + 23 · 71 + 712.

We choose (w1, w2) = (14, 77), (23, 71), which, by (21), gives w3 =
−91, −94, respectively. Thus, by (22),

D3(x, 74) = (x + 14)(x + 77)(x − 91) + 14 · 77 · 91 =

= (x + 23)(x + 71)(x − 94) + 23 · 71 · 94.

According to formula (5) of [11] we have, for all coprime positive inte-
gers m, n and integers b,

(32) Dm(Dn(x, b), b
n) = Dn(Dm(x, b), b
m).

Therefore the equation F (x) := D3(x, b
4) = D4(y, b
3) =: G(y) has
solutions (x, y) = (D4(X, 7), D3(X, 7)) for every X ∈ Z. We obtain
that the equation

f (x) := (x + 14)(x + 77)(x − 91)(x + 23)(x + 71)(x − 94) =

= (D4(y, 73) − 14 · 77 · 91)(D4(y, 73) − 23 · 71 · 94) =: g(y)

has the same solutions. Note that here we have

ϕ(x) = (x − 14 · 77 · 91)(x − 23 · 71 · 94).

Example 7.2. Let (F, G) be of the third kind with deg(F ) = m = 4,
deg(G) = n = 3 and b = 5. We have 4b
3 = 4 · 53 = 42 + 222 =
102+202. Taking (w1, w2) = (4, 22), (10, 20), by (24), we get (w3, w4) =
(−4, −22), (−10, −20), and by (26), u = −23506, 8750, respectively.
That is, we have

D4(x, 53) = (x + 4)(x − 4)(x + 22)(x − 22) + 23506 =

= (x + 10)(x − 10)(x + 20)(x − 20) − 8750.

THE DIOPHANTINE EQUATION f (x) = g(y) 25

Since, by (32), the equation F (x) := D4(x, 53) = D3(y, 54) =: G(y) has
inﬁnitely many integral solutions (x, y) = (D3(X, 5), D4(X, 5)) (X ∈
Z), we obtain that the equation

f (x) := (x+4)(x−4)(x+22)(x−22)(x+10)(x−10)(x+20)(x−20) =

= (D3(y, 54) − 23506)(D3(y, 54) + 8750) =: g(y)

has the same solutions. Here we have ϕ(x) = (x − 23506)(x + 8750).

Example 7.3. The case (F, G) is a standard pair of the third kind,
deg(F ) = m = 6, deg(G) = n = 5 and b = 7. We have 3 · 75 =
2112 + 211 · 25 + 252 = 1962 + 196 · 49 + 492. Taking (w1, w2) = (211, 25),
(196, 49) by (29) we get

(w3, w4, w5, w6) = (236, −211, −25, −236), (245, −196, −49, −245),

and by (30), u = 7945347009886, 3958608139486, respectively. That
is, we have

D6(x, 75) =

(x+ 211)(x+ 25)(x+ 236)(x−211)(x−25)(x−236) −7945347009886 =

= (x+196)(x+49)(x+245)(x−196)(x−49)(x−245)−3958608139486.

Since, by (32), the equation F (x) := D6(x, 75) = D5(y, 76) =: G(y) has
inﬁnitely many integral solutions (x, y) = (D5(X, 7), D6(X, 7)) (X ∈
Z), we obtain that the equation

f (x) := (x + 211)(x + 25)(x + 236)(x − 211)(x − 25)(x − 236)·

· (x + 196)(x + 49)(x + 245)(x − 196)(x − 49)(x − 245) =

= (D5(y, 76) + 7945347009886)(D5(y, 76) + 3958608139486) =: g(y)

has the same solutions. Here we have

ϕ(x) = (x + 7945347009886)(x + 3958608139486).

Example 7.4. The case (F, G) is a standard pair of the fourth kind
with deg(F ) = m = 4, deg(G) = n = 10 and b = 5 · 13 = 65. We have
4b = 22 + 162 = 82 + 142. We take (w1, w2) = (2, 16), (8, 14), which, by
(24), gives (w3, w4) = (−2, −16), (−8, −14) and, by (26), u = −7426,
4094, respectively. Thus

D4(x, 65) = (x + 2)(x − 2)(x + 16)(x − 16) + 7426 =

= (x + 8)(x − 8)(x + 14)(x − 14) − 4094.

26 L. HAJDU AND R. TIJDEMAN

According to formula (10) of [11] with m = 4, n = 10 we have for
a, b, v1, v2 ∈ Q with

(33) b
2v2
1 + av2
2 = 4ab

that

(34) b
−2D4(b
−2(v5
2 − 5bv3
2 + 5b
2), b) = −a
−5D10(v1v2, a).

Here b = 65. We choose a = −10 · 652, and observe that then
(33) becomes the (generalized) Pell equation v2
1 − 10v2
2 = −2600, and
(v1, v2) = (Xi, Yi) given by (X0, Y0) = (−80, 30), (X1, Y1) = (280, 90)
and (Xi, Yi) = 38(Xi−1, Yi−1) − (Xi−2, Yi−2) (i ≥ 2)
are integral solutions to it. Thus, for any constant c,

b
−2D4(x, b) − cb
−2 = −a
−5D10(y, a) − cb
−2

has inﬁnitely many solutions (x, y) ∈ Q
2 with a bounded denominator
which are independent of c, and we obtain that the equation

f (x) := b
−4(x−2)(x+2)(x−16)(x+16)(x−8)(x+8)(x−14)(x+14) =

= (−a
−5D10(y, a) − 7426b
−2)(−a
−5D10(y, a) + 4094b
−2) =: g(y)

(with a = −10 · 652 and b = 65) has inﬁnitely many solutions (x, y) ∈
Q
2 with a bounded denominator. Here we have F (x) = b
−2D4(x, b),
G(x) = −a
−5D10(x, a), ϕ(x) = (x − 7426b
−2)(x + 4094b
−2).

Example 7.5. The case (F, G) is a standard pair of the fourth kind
with deg(F ) = m = 6, deg(G) = n = 10, and b = 7 · 13 = 91. We have
3b = 162 + 16 · 1 + 12 = 112 + 11 · 8 + 82. Letting (w1, w2) = (16, 1),
(11, 8) by (29) we obtain

(w3, w4, w5, w6) = (17, −16, −1, −17), (19, −11, −8, −19),

and (30) yields u = 1433158, −1288442, respectively. That is, we have

D6(x, 91) =

(x + 16)(x + 1)(x + 17)(x − 16)(x − 1)(x − 17) − 1433158 =

= (x + 11)(x + 8)(x + 19)(x − 11)(x − 8)(x − 19) + 1288442.

By formula (10) of [11] with m = 6, n = 10, if for a, b, v1, v2 ∈ Q we
have

(35) b
3v2
1 + av2
2 = 4ab

then

(36) b
−3D6(b
−2(v5
2 − 5bv3
2 + 5b
2), b) = −a
−5D10(v1(v2
2 − b), a).

THE DIOPHANTINE EQUATION f (x) = g(y) 27

Now b = 91. We take a = −14·913, and observe that then (35) becomes
the (generalized) Pell equation v2
1 − 14v2
2 = −5096, and (v1, v2) =
(Xi, Yi) given by (X0, Y0) = (−140, 42), (X1, Y1) = (252, 70) and

(Xi, Yi) = 30(Xi−1, Yi−1) − (Xi−2, Yi−2) (i ≥ 2)

are integer solutions to it. Hence, for any c ∈ Q,

b
−3D6(x, b) − cb
−3 = −a
−5D10(y, a) − cb
−3

has inﬁnitely many solutions (x, y) ∈ Q
2 with a bounded denominator
which are independent of c. This implies that the equation

f (x) := b
−6(x + 16)(x + 1)(x + 17)(x − 16)(x − 1)(x − 17)·

· (x + 11)(x + 8)(x + 19)(x − 11)(x − 8)(x − 19) =

= (−a
−5D10(y, a)+1433158b
−3)(−a
−5D10(y, a)−1288442b
−3) =: g(y)

(with a = −14 · 913 and b = 91) has inﬁnitely many solutions (x, y) ∈
Q
2 with a bounded denominator. Here we have F (x) = b
−3D6(x, b),
G(x) = −a
−5D10(x, a), ϕ(x) = (x + 1433158b
−3)(x − 1288442b
−3).

Remark 7.1. We recall that if M is the product of ρ distinct primes of
the form ≡ 1 (mod 4), then the number of representations of M as α2
1+
α2
2 with α1, α2 ∈ Z, α1 > α2 > 0, gcd(α1, α2) = 1 equals 2ρ−1 according
to Theorem 7.5 of [49]. Similarly, the number of representations of M
as x
2+xy+y2 with coprime integers x, y, x > y > 0 equals 2ρ−1 (see [24]
par. 48, item 4). It follows that in all the above examples deg(ϕ) can
equal any s ∈ Z>0, (hence deg(f ) and deg(g) can be made arbitrarily
large) by choosing suitable W with number of representations ≥ s and
corresponding values u = u1, u2, . . . , us.

Proof of the ﬁrst statement of Theorem 1.1. By Lemma 7.1 equation
(2) with (1) implies that deg(F ) ∈ {1, 2, 3, 4, 6}, if the corresponding
standard pair (F, G) is of the third or fourth kind. This combined with
Lemma 3.1 completes the proof of the ﬁrst statement of Theorem 1.1.
□

Remark 7.2. Let f (x) ∈ Q[x] have only simple rational roots and let
g(x) ∈ Q[x]. Suppose the equation f (x) = g(y) has inﬁnitely many
solutions (x, y) ∈ Q
2 with a bounded denominator. By Lemma 7.1
we have deg(F ) ∈ {1, 2, 3, 4, 6}. Put s = gcd(deg(f ), deg(g)), m =
deg(f )/s, n = deg(g)/s. Then gcd(m, n) = 1 and m ∈ {1, 2, 3, 4, 6} or
n ∈ {1, 2}.
If m = 1 we refer to Example 5.1 to see that all pairs n, s are possible.
For m = 2 Example 5.3 shows that all pairs (n, s) (with n odd since
m and n are coprime) are possible. By (32) the equation Dm(x, b
n) =

28 L. HAJDU AND R. TIJDEMANn(y, b
m) with gcd(m, n) = 1 has inﬁnitely many solutions in integers
(x, y) for any integer b. If m = 4, we proceed as in Example 7.2 (where
s = 2) using a b which is the product of suﬃciently many distinct
primes ≡ 1 (mod 4). If m = 3 or m = 6, then we proceed as in
Examples 7.1 or 7.3 (where s = 2 too) using a b which is the product of
suﬃciently many distinct primes ≡ 1 (mod 6). Remark 7.1 underlines
that this can be done for any s. Thus every pair (deg(f ), deg(g)) with
corresponding m ∈ {1, 2, 3, 4, 6} can be represented.

8. Both f and g have only simple rational roots and
(F, G) is of the third or fourth kind

If both f and g have simple rational roots, then by symmetry we
may assume that deg(f ) ≤ deg(g). Throughout this chapter we shall
do so without further mentioning. We show that if in this case the
equation f (x) = g(y) has inﬁnitely many rational solutions with a
bounded denominator and the corresponding standard pair (F, G) is of
the third or fourth kind, then deg(F ) ≤ 2. Note that deg(f ) ≤ deg(g)
implies deg(F ) ≤ deg(G).

Theorem 8.1. Suppose that f and g have only simple rational roots,
and the equation f (x) = g(y) has inﬁnitely many rational solutions
with a bounded denominator. If the corresponding standard pair (F, G)
is of the third or fourth kind, then deg(F ) ≤ 2 holds.

In the proof we use the following lemmas.
We denote the discriminant of a polynomial P by disc(P ).

Lemma 8.1 (Davenport, Lewis, Schinzel, [22], Theorem 1). Let F (x) ∈
Z[x] be of degree m > 1 and G(y) ∈ Z[x] of degree n > 1. Let

D(z) = disc(F (x) + z), E(z) = disc(G(y) + z).

Suppose there are at least [ 1

2m] roots of D(z) = 0 for which E(z) ̸= 0.
Then F (x) − G(y) is irreducible over the complex ﬁeld. Further, the
genus of the equation F (x)−G(y) = 0 is strictly positive except possibly
when n = 2 or m = n = 3. Apart from these possible exceptions, the
equation has at most a ﬁnite number of integral solutions.

Lemma 8.2. Let a, b, c be rational numbers such that

3a
2 + b
2 = c2.

Then there exist rational numbers u, v, w such that

a = ±w(2uv), b = ±w(3u2 − v2), c = ±w(3u2 + v2)

with independent choices of the ± signs.

THE DIOPHANTINE EQUATION f (x) = g(y) 29

Proof. If abc = 0 then we easily see that a = 0. Then letting u = 0
and v = 1, the statement follows.
So we may assume that a, b, c are positive. Then there exists a unique
t ∈ Q such that p := ta, q := tb, r := tc are coprime positive integers.
Observe that then p, q, r are pairwise coprime, r > q and

3p2 + q2 = r2.

By factoring r2 − q2 it follows that the solutions of this equation are
given by (cf. A. Desboves [23] and Dickson [25], II p. 405 3)

p = uv, q = 3u2 − v2

2 , r = 3u2 + v2

2 if q − r is odd, and

p = 2uv, q = 3u2 − v2, r = 3u2 + v2 if q − r is even,
for some integers u, v. Choose w = t
−1. □

Proof of Theorem 8.1. Suppose that the equation f (x) = g(y) has in-
ﬁnitely many solutions x, y ∈ Q with a bounded denominator, and
write (F, G) for the corresponding standard pair of the third or fourth
kind. Assume that deg(F ) ≥ 3. Then it follows from Lemma 7.1
that deg(F ), deg(G) ∈ {3, 4, 6}. In view of the gcd-restrictions on
standard pairs of the third and fourth kinds it remains to consider
(m, n) := (deg(F ), deg(G)) = (3, 4) for the third kind and = (4, 6) for
the fourth kind.

Standard pairs of the third kind. We have (m, n) = (3, 4). Write

ϕ(x) = p0(x − p1) · · · (x − ps)

with p0 ∈ Q, p0 ̸= 0 and pi ∈ C (i = 1, . . . , s). Since the roots of
f (x) = ϕ(F (x)) are simple and rational, we see that p1, . . . , ps are
distinct and rational. So we can write

F (x) − pi = (x − a
(i)
1 )(x − a
(i)
2 )(x − a
(i)
3 ),

G(y) − pi = (y − b
(i)
1 )(y − b
(i)
2 )(y − b
(i)
3 )(y − b
(i)
4 ) (i = 1, . . . , s).
Here the 3s numbers a form the set of roots of f and are therefore
distinct rationals. Similarly the 4s numbers b form the set of roots of
g and are therefore distinct rationals. We know that the equation

(37) F (x) − p1 = G(y) − p1

has inﬁnitely many solutions in rationals x, y with a bounded denomi-
nator. Since F is an odd and G is an even polynomial (because they are

3Dickson mentions only the second option. By that he misses, for example, the
trivial solution p = q = 1, r = 2.

30 L. HAJDU AND R. TIJDEMAN

Dickson polynomials of degree 3 and 4, respectively), this implies that
the equation (after changing the indexing of the roots if it is necessary)

(x − a
(1)
1 )(x − a
(1)
2 )(x + a
(1)
1 + a
(1)
2 ) = (y2 − (b
(1)
1 )2)(y2 − (b
(1)
2 )2)

has inﬁnitely many solutions in rationals x, y with a bounded denom-
inator. Then there exist positive integers ∆1, ∆2 such that, omitting
the superscript (1) for simplicity and putting

Ai = ∆1ai (i = 1, 2, 3) and Bj = ∆2bj (j = 1, 2),

the equation
(38)
U(x) := (x − A1)(x − A2)(x + A1 + A2) = ∆(y2 − B2
1 )(y2 − B2
2 ) =: V (y)

with ∆ = ∆
3
1/∆
4
2 has inﬁnitely many solutions in integers x, y.
It follows from Lemma 8.1 that, writing

D(z) = disc(U(x) + z) and E(z) = disc(V (y) + z),

every root of D(z) is a root of E(z). A Maple calculation reveals that
the roots of D(z) are

(39) − A
2
1A2 − A1A
2
2 ± 2
9
 √3(A
2
1 + A1A2 + A
2
2)3

and that the roots of E(z),

(40) − ∆B2
1B2
2, ∆ ( B2
1 − B2
2
2
 )2

(the latter one being a double root), are rational. So the roots of D(z)
have to be rational. Hence, for some s ∈ Q,

(41) 3(A
2
1 + A1A2 + A
2
2) = s2.

We rewrite (41) as
 3(2A1 + A2)2 + (3A2)2 = (2s)2.

By Lemma 8.2, we obtain

2A1 + A2 = ±w(2uv), 3A2 = ±w(3u2 − v2)

with some u, v, w ∈ Q and independent choice of the ± signs. This
yields
 (A1, A2) = w (−3u2 ± 6uv + v2

6 , ±3u2 − v2

3
 ) .

(Here in place of the factor ±w we can simply write w, since w ∈ Q is
arbitrary.) Therefore the roots of D(z) are given by
1
2w3u2(u − v)2(u + v)2, − 1
54 w3v2(3u − v)2(3u + v)2.

THE DIOPHANTINE EQUATION f (x) = g(y) 31

Since, by (40), the products of any two roots (40) of E(z) are ± squares
and 2 · 54 = 108 is not a square in Q, we see that one of the roots of
D(z) is zero. Then E(z) has also a root 0. However, then either
B1B2 = 0 or B1 = ±B2, which contradicts the distinctness of the roots
B1, B2, B3, B4. This contradiction proves that (38) has only ﬁnitely
many solutions (x, y) ∈ Z
2, hence (37) and thus also the equation
f (x) = g(y) has only ﬁnitely many rational solutions with a bounded
denominator. So this case cannot occur.

Standard pairs of the fourth kind. In this case the only possibility
is (m, n) = (4, 6), and Theorem 3.1 implies that the standard pair
(F (x), G(y)) is of the form (a
−2D4(x, a), −b
−3D6(y, b)). Further, the
equation

(42) a
−2D4(x, a) = −b
−3D6(y, b)

should have inﬁnitely many rational solutions x, y with bounded de-
nominator. However, by Theorem 7.1 we know that here b is of the
form (w2
1 + w1w2 + w2
2)/3 with some w1, w2 ∈ Q, in particular, b > 0.
However, since the signs of the leading coeﬃcients of the even degree
polynomials in (42) are diﬀerent, this equation can have only ﬁnitely
many solutions with a bounded denominator. So this case cannot occur
either, and the proof of Theorem 8.1 is complete. □

9. A sharpening for f, g with only simple rational roots

We give a reﬁnement of Theorem 1.1 in case both f and g have only
simple rational roots. This completes the proof of Theorem 1.1.

Theorem 9.1. Suppose that f and g have only simple rational roots,
and the equation f (x) = g(y) has inﬁnitely many rational solutions
with a bounded denominator. Let k = deg(f ), ℓ = deg(g). If k ≤ ℓ,
then k | 2ℓ, f is a PTEm-polynomial and g is a PTEℓm/k-polynomial
with some m ∈ {1, 2}.
Conversely, if k, ℓ are positive integers with k | ℓ and g is a PTEℓ/k-
polynomial of degree ℓ with only simple rational roots, then there exists
a polynomial f (x) ∈ Q[x] with deg(f ) = k and only simple rational
roots such that the equation f (x) = g(y) has inﬁnitely many rational
solutions with a bounded denominator.

Proof. Suppose that the equation f (x) = g(y) has inﬁnitely many
solutions x, y ∈ Q with a bounded denominator. Write (F, G) for
a corresponding standard pair. Combining Lemma 3.1 and Theo-
rem 8.1 we see that deg(F ) ≤ 2, hence deg(f ) | 2 deg(g). Without
loss of generality we may assume F (x) = x
m with m ∈ {1, 2}. If

32 L. HAJDU AND R. TIJDEMAN

ϕ(x) = p0(x − p1) · · · (x − ps), then the rationals p1, . . . , ps are dis-
tinct, f (x) is similar to p0(x
m − p1) · · · (x
m − ps) and g(y) is similar to
p0(G(y) − p1) · · · (G(y) − ps), which both have simple rational roots.
Thus f is a PTEm-polynomial, g is a PTEℓm/k-polynomial.
Conversely, let k | ℓ and g be a PTEℓ/k-polynomial of degree ℓ with
only simple rational roots. Then g is of the form

(43) g(y) = p0(G(y) − p1)(G(y) − p2) · · · (G(y) − pk)

for some p0, p1, . . . , pk ∈ Q with p1, p2, . . . , pk distinct. Write f (x) =
p0(x − p1) · · · (x − pk). Then the equation f (x) = g(y) has solutions
(x, y) = (G(X), X) for every X ∈ Z. □

Remark 9.1. If in (43) pi = b
2
i for bi ∈ Q, i = 1, . . . , k, then we
may choose F (x) = x
2, f (x) = (x − b1)(x + b1) · · · (x − bk)(x + bk).
This is the case m = 2 in which f is both a PTE1-polynomial and a
PTE2-polynomial.

Remark 9.2. In Sections 5 and 6 we have shown that deg(ϕ) can be
arbitrary, hence deg(f ), deg(g) can be arbitrarily large. A remaining
question is how large deg(v) in Table 1 can be, if both f and g have
only simple rational roots. Without loss of generality we may assume
F (x) = x or F (x) = x
2. Below we treat the cases with the largest
degree of v. As before we distinguish between the cases G(y) = αyv(y)2

and G(y) = (αy2 + β)v(y)2 with αβ ̸= 0.

Example 9.1. Case F (x) = x, G(y) = v(y). It is known that the sets

T1 := {±22, ±61, ±86, ±127, ±140, ±151},

T2 := {±35, ±47, ±94, ±121, ±146, ±148}
form an ideal PTE2,12 pair. Let

v(y) =
 ∏

t∈T1(y − t) + ∏

t∈T2(y − t)
2 and A =
 ∏

t∈T1 t − ∏

t∈T2 t
2 .

Then
g(y) := ∏

t∈T1∪T2(y − t) = (v(y) + A)(v(y) − A) = v(y)2 − A
2.

We deﬁne f (x) = x
2 − A
2. Thus f, g both have simple rational roots
and the equation f (x) = g(y) has solutions (x, y) = (±v(X), X) for
every X ∈ Z. Here ϕ(x) = x
2 − A
2.

Example 9.2. Case F (x) = x
2, G(y) is of the form αyv(y)2.
It is known that the symmetric sets

T3 := {−98, −82, −58, −34, 13, 16, 69, 75, 99} and T4 := {t ∈ T3 : −t}

THE DIOPHANTINE EQUATION f (x) = g(y) 33

form an ideal PTE2,9 pair. Put g(y) = ∏

t∈T3(y − t
2), A = ∏
t∈T3 t and
yT (y) = ∏

t∈T3(y − t) + A. Then

g(y2) := ∏

t∈T3(y − t) · ∏

t∈T4(y − t) = (yT (y) − A)(yT (y) + A).

Observe that yT (y) is an odd polynomial, so T (y) is an even polynomial
(the coeﬃcients of yi with i odd are 0 in T ). This yields that T (y) =
v(y2) for some v(y) ∈ Q[y] and therefore g(y) = yv(y)2 − A
2. So
letting f (x) = (x − A)(x + A), we see that the equation f (x) = g(y)
has solutions (x, y) = (Xv(X 2), X) for every X ∈ Z. Here we have
ϕ(x) = x − A
2, F (x) = x
2, G(y) = yv(y)2, deg(g)/ deg(f ) = 9/2.

Example 9.3. Case F (x) = x
2, G(y) is of the form (αy2 + β)v(y)2

with αβ ̸= 0. An example with deg(v) = 0 is given by Example 6.2.

10. Equal products from blocks

We give an application of Theorem 1.1 for equal products from blocks
of integers of bounded size. By a block we mean a set of consecutive
integers.

Theorem 10.1. For every positive integer N there exist only ﬁnitely
many pairs of disjoint blocks A and B of size at most N with the
property that for some k, ℓ with 1 ≤ k < ℓ and k ∤ 2ℓ, there exist
distinct elements a1, . . . , ak ∈ A and distinct elements b1, . . . , bℓ ∈ B
such that

(44) a1 · · · ak = b1 · · · bℓ.

Proof. Suppose the statement of the theorem is false for N. We may
clearly assume that k and ℓ are ﬁxed and that

a1 < · · · < ak and b1 < · · · < bℓ.

Then we may assume as well that the diﬀerences

ci := ai − a1 (1 < i ≤ k) and dj := bj − b1 (1 < j ≤ ℓ)

are ﬁxed. Therefore the equation

f (x) := x(x + c1) . . . (x + ck−1) = y(y + d1) . . . (y + dℓ−1) =: g(y)

would have inﬁnitely many solutions in rationals x, y with a bounded
denominator. By Theorem 9.1 the corresponding standard pair (F, G)
satisﬁes deg(F ) ≤ 2. This implies k | 2ℓ, and the statement follows. □

Remark 10.1. Example 5.1 provides examples with k | ℓ such that
(44) has inﬁnitely many integral solutions. Here k can be arbitrarily

34 L. HAJDU AND R. TIJDEMAN

large. Examples 5.6 and 9.2 provide examples with k | 2ℓ, k ∤ ℓ, and
(44) has inﬁnitely many integral solutions.

11. Conclusions and open problems

In this paper we have studied equation (2) subject to (1) and some-
times (3). In the introduction we formulated the main theorem which
demonstrates that the possibilities are restricted, even very restricted
if (3) holds too. In Section 3 we stated the fundamental theorem of
Bilu-Tichy that attaches a standard pair of polynomials (F, G) to each
equation f (x) = g(y) which has inﬁnitely many solutions. Here and
below solutions means solutions in rationals with a bounded denomina-
tor. There are ﬁve kinds of standard pairs. Lemma 3.1 shows that the
equation f (x) = g(y) under (1) cannot have inﬁnitely many solutions
with the ﬁfth standard pair. In Sections 5 and 6 we treat the equations
leading to standard pairs of the ﬁrst and second kind. Sections 7 and
8 deal with standard pairs of the third and fourth kind. In Section 7
we prove the ﬁrst statement of Theorem 1.1. In Section 9 we obtain a
reﬁnement of the main theorem. Finally we have given an application
of the obtained results in Section 10.

Suppose equation (2) for f (x), g(x) ∈ Q[x] admits inﬁnitely many in-
tegral solutions (x, y) with f subject to (1). Put s = gcd(deg(f ), deg(g)),
m = deg(f )/s, n = deg(g)/s. At the end of Section 7 we have proved
that m ∈ {1, 2, 3, 4, 6} or n ∈ {1, 2}. Moreover we have argued that
every pair (deg(f ), deg(g)) with corresponding m ∈ {1, 2, 3, 4, 6} can
be represented.
Problem 1. Which other possibilities are there for m, s, if n = 1 or 2
for equation (2) under (1)?

Now let f (x), g(x) ∈ Q[x] both have only simple rational roots and
equation (1.1) have inﬁnitely many integral solutions. We assume
deg(f ) ≤ deg(g), hence m ≤ n. Theorem 1.1 implies m ∈ {1, 2}.
Note that the cases m = s = 1, n arbitrary, m = n, s arbitrary and
m = 1, n = 2, s arbitrary are trivial, the latter in view of

(x − b
2
1) · · · (x − bs)2 = (y2 − b
2
1) · · · (y2 − b
2
s), F (x) = x, G(y) = y2

with solutions (X 2, X) for X ∈ Z. Example 6.1 shows that the cases
m = 1, n ∈ {3, 4, 6}, s arbitrary are possible, cf. Remark 7.2. Example
5.6 deals with the case m = 2, n = 3, s arbitrary. Using ideal PTE pairs
Example 9.1 can be extended to the cases m = 1, n ∈ {5, 7, 8, 9, 10, 12},
s = 2 and Example 9.2 to the cases m = 2, n ∈ {5, 7, 9}, s = 1.

THE DIOPHANTINE EQUATION f (x) = g(y) 35

Problem 2. Which other possibilities are there for triples m, n, s for
equation (2) under (1) and (3)?

Acknowledgements

Lajos Hajdu would like to express his thanks to the R´enyi Institute,
where he was a visiting professor during this research. The authors
thank Szabolcs Tengely for some useful remarks.

References

[1] E.T. Avanesov, Solution of a problem on ﬁgurate numbers (Russian), Acta
Arith. 12 (1966), 409–420.
[2] R.M. Avanzi, U.M. Zannier, Genus one curves deﬁned by separated variable
polynomials and a polynomial Pell equation, Acta Arith. 99 (2001), 227–256.
[3] R. Balasubramanian, T.N. Shorey, Squares in products from a block of consec-
utive integers, Acta Arith. 65 (1993), 213–220.
[4] M. Bauer, M.A. Bennett, On a question of Erd˝os and Graham, Enseign. Math.
53 (2007), 259–264.
[5] M.A. Bennett, Products of consecutive integers, Bull. London Math. Soc. 36
(2004), 683–694.
[6] M.A. Bennett, Powers from products of k terms in progression: ﬁniteness for
small k, Acta Arith. 184 (2018), 87–100.
[7] M.A. Bennett, N. Bruin, K. Gy˝ory, L. Hajdu, Powers from products of consec-
utive terms in arithmetic progression, Proc. London Math. Soc. (3) 92 (2006),
273–306.
[8] M.A. Bennett, S. Siksek, A conjecture of Erd˝os, supersingular primes and short
character sums, Ann. Math. (2) 191 (2020), 355–392.
[9] F. Beukers, T. N. Shorey and R. Tijdeman, Irreducibility of polynomials and
arithmetic progressions with equal product of terms, in: Number Theory in
Progress (Proc. Internat. Conf. in Number Theory in Honor of A. Schinzel,
Zakopane, 1997), K. Gy˝ory, H. Iwaniec and J. Urbanowicz (eds.), de Gruyter,
1999, pp. 11–26.
[10] Yu. Bilu, M. Kulkarni, B. Sury, The Diophantine equation x(x + 1) . . . (x +
(m − 1)) + r = yn, Acta Arith. 113 (2004), 303–308.
[11] Yu. Bilu, R. Tichy, The Diophantine equation f (x) = g(y), Acta Arith. 95
(2000), 261–288.
[12] A. Blokhuis, A. Brouwer, B. de Weger, Binomial collisions and near collisions
Integers 17 (2017), Nr. 64, 8 pp.
[13] W. Bosma, J. Cannon, C. Playoust, The Magma algebra system. I. The user
language, J. Symbolic Comput. 24 (1997), 235–265.
[14] D.W. Boyd, H.H. Kisilevsky, The diophantine equation u(u+1)(u+2)(u+3) =
v(v + 1)(v + 2), Paciﬁc J. Math. 40 (1972), 23–32.
[15] B. Brindza, On S-integral solutions of the equation ym = f (x), Acta Math.
Hungar. 44 (1984), 133–139.
[16] B. Brindza, Yu. Bilu, P. Kirschenhofer, ´A. Pint´er, R. Tichy, Diophantine equa-
tions and Bernoulli polynomials. With an appendix by A. Schinzel, Compositio
Math. 131 (2002), 173–188.

36 L. HAJDU AND R. TIJDEMAN

[17] Y. Bugeaud, M. Mignotte, S. Siksek, M. Stoll, Sz. Tengely, Integral points on
hyperelliptic curves, Algebra Number Theory 8 (2008), 859–885.
[18] A. Choudhry, A new approach to the Tarry-Escott problem, Intern. J. Number
Th. 13 (2017), 393–417.
[19] M.J. Cohen, The diﬀerence between the product of n consecutive integers and
the n-th power of an integer, Comput. Math. Appl. 39 (2000), 139–157.
[20] P. Das, S. Laishram, N. Saradha, Cubes in products of terms from an arithmetic
progression, Acta Arith. 184 (2018), 117–126.
[21] P. Das, S. Laishram, N. Saradha, Variants of Erd˝os-Selfridge superelliptic
curves and rational points, Mathematika 64 (2018), 380–386.
[22] H. Davenport, D.J. Lewis, A. Schinzel, Equations of the form f (x) = g(y),
Quart. J. Math. Oxford Ser. (2) 12 (1961), 304–312.
[23] A. Desboves, M´emoire sur la r´esolution en nombres entiers de l’´equation
aX m + bY m = cZ n. Nouv. Ann. Math. (2), 18 (1879), 269; proofs: Nouv.
Ann. Math. (3), 5 (1886), 226–233.
[24] L.E. Dickson, Modern Elementary Theory of Numbers, The University of
Chicago Press, 1939.
[25] L.E. Dickson, History of the Theory of Numbers, Vol. II, Diophantine Analysis,
Chelsea Publ., 1971. (First ed. 1919)
[26] P. Erd˝os, On a Diophantine equation, J. London Math. Soc. 26 (1951), 176–
178.
[27] P. Erd˝os, R.L. Graham, Old and New Problems and Results in Combinatorial
Number Theory, Monograph Enseign. Math. 28, Geneva, 1980.
[28] P. Erd˝os, J.L. Selfridge, The product of consecutive integers is never a power,
Illinois J. Math. 19 (1975), 292–301.
[29] P. Erd˝os, J. Turk, Products of integers in short intervals, Acta Arith. 44 (1984),
147–174.
[30] M. Filaseta, S. Laishram, N. Saradha, Solving n(n + d) · · · (n + (k − 1)d) = by2

with P (b) ≤ Ck, Int. J. Number Th. 8 (2012), 161–173.
[31] H.R. Gallegos-Ruiz, N. Katsipis, Sz. Tengely, M. Ulas, On the Diophantine
equation (
n
k) = (
m
ℓ ) = d, J. Number Th. 208 (2020), 418-440.
[32] K. Gy˝ory, On the Diophantine equation (
n
k) = x
l, Acta Arith. 80 (1997), 289–
295.
[33] K. Gy˝ory, On the Diophantine equation n(n + 1) · · · (n + k − 1) = bx
ℓ, Acta
Arith. 83 (1998), 87–92.
[34] K. Gy˝ory, L. Hajdu, ´A. Pint´er, Perfect powers from products of consecutive
terms in arithmetic progression, Compositio Math. 145 (2009), 845–864.
[35] K. Gy˝ory, L. Hajdu, N. Saradha, On the Diophantine equation n(n+d) · · · (n+
(k − 1)d) = byl, Canad. Math. Bull. 47 (2004), 373–388. Correction: ibid. 48
(2005), 636.
[36] K. Gy˝ory, ´A. Pint´er, Almost perfect powers in products of consecutive integers,
Monatsh. Math. 145 (2005), 19–33.
[37] L. Hajdu, T. Kov´acs, Almost ﬁfth powers in arithmetic progression, J. Number
Th. 131 (2011), 1912–1923.
[38] L. Hajdu, ´A. Papp, Polynomial values of products of terms from an arithmetic
progression, Monatsh. Math. 193 (2020), 637–655. Corr. 195 (2021), 377.
[39] L. Hajdu, ´A. Papp, R. Tijdeman, The Prouhet-Tarry-Escott problem, indecom-
posibility of polynomials and Diophantine equations, Ramanujan J. (to appear).

THE DIOPHANTINE EQUATION f (x) = g(y) 37

[40] L. Hajdu, ´A. Pint´er, Combinatorial Diophantine equations, Publ. Math. De-
brecen 56 (2000), 391–403.
[41] L. Hajdu, ´A. Pint´er, Sz. Tengely, N. Varga, Equal values of ﬁgurate numbers,
J. Number Theory 137 (2014), 130–141.
[42] L. Hajdu, Sz. Tengely, R. Tijdeman, Cubes in products of terms in arithmetic
progression, Publ. Math. Debrecen 74 (2009), 215–232.
[43] L. Hajdu, N. Varga, Polynomial values of ﬁgurate numbers, J. Number Theory
214 (2020), 79–99.
[44] G. Hanrot, N. Saradha, T.N. Shorey, Almost perfect powers in consecutive
integers, Acta Arith. 99 (2001), 13–25.
[45] N. Hirata-Kohno, S. Laishram, T.N. Shorey, R. Tijdeman, An extension of a
theorem of Euler, Acta Arith. 129 (2007), 71–102.
[46] M. Kulkarni, B. Sury, On the Diophantine equation x(x + 1)(x + 2) · · · (x +
(m − 1)) = g(y), Indag. Math. 14 (2003), 35–44.
[47] S. Laishram, T.N. Shorey, The equation n(n + d) · · · (n + (k − 1)d) = by2 with
ω(d) ≤ 106 or d ≤ 1010, Acta Arith. 129 (2007), 249–305.
[48] W.J. LeVeque, On the equation ym = f (x), Acta Arith, 9 (1964), 209–219.
[49] W.J. LeVeque, Topics in Number Theory, Vol. 1, Addison Wesley, 1965.
[50] R. Lidl, G. Mullen, G. Turnwald, Dickson polynomials, Pitman Monographs
and Surveys in Pure and Applied Mathematics 65, Longman Scientiﬁc & Tech-
nical, Harlow, 1993.
[51] M. Mignotte, T.N. Shorey, The equations (x+1) · · · (x+k) = (y+1) · · · (y+mk),
m = 5, 6, Indag. Math. (N.S.) 7 (1996), 215–225.
[52] L.J. Mordell, On the integer solutions of y(y + 1) = x(x + 1)(x + 2), Paciﬁc J.
Math. 13 (1963), 1347-1351.
[53] A. Mukhopadhyay, T.N. Shorey, Almost squares in arithmetic progression II,
Acta Arith. 110 (2003), 1–14.
[54] R. Obl´ath, ¨Uber das Product f¨unf aufeinander folgender Zahlen in einer arith-
metischen Reihe, Publ. Math. Debrecen 1 (1950), 222–226.
[55] S. Raghavendran, V.Varayanan, The Prouhet Tarry Escott problem: A review,
MDPI, Mathematics 7 (2019), 227, 14 pp.
[56] Cs. Rakaczki, On the Diophantine equation x(x − 1) · · · (x + (m − 1)) = λy(y −
1) · · · (y − (n − 1)) + ℓ, Acta Arith. 110 (2003), 339–360.
[57] Cs. Rakaczki, On the Diophantine equation F (x
n
) = b( y
m)
, Period. Math. Hun-
gar. 49 (2004), 119–132.
[58] N. Saradha, On perfect powers in products with terms from arithmetic progres-
sions, Acta Arith. 82 (1997), 147–172.
[59] N. Saradha, Squares in products with terms from arithmetic progressions, Acta
Arith. 86 (1998), 27–43.
[60] N. Saradha, T.N. Shorey, On the ratio of two blocks of consecutive integers,
Proc. Indian Acad. Sci. (Math. Sci.) 100 (1990), 107–132.
[61] N. Saradha, T.N. Shorey, Almost perfect powers in arithmetic progression, Acta
Arith. 99 (2001), 363–388.
[62] N. Saradha, T.N. Shorey, Almost squares in arithmetic progression II, Com-
positio Math. 138 (2003), 1–14.
[63] N. Saradha, T.N. Shorey, Almost squares and factorizations in consecutive
integers, Compositio Math. 138 (2003), 113–124.

38 L. HAJDU AND R. TIJDEMAN

[64] N. Saradha, T.N. Shorey, Contributions towards a conjecture of Erd˝os on per-
fect powers in arithmetic progression, Compositio Math. 141 (2005), 541–560.
[65] N. Saradha, T.N. Shorey, On the equation n(n + d) · · · (n + (i0 − 1)d)(n + (i0 +
1) · · · (n + (k − 1)d) = yℓ, Acta Arith. 129 (2007), 1–21.
[66] N. Saradha, T.N. Shorey, Almost perfect powers in consecutive integers, II,
Indag. Math. (N.S.) 19 (2008), 649–658.
[67] N. Saradha, T.N. Shorey, Squares in blocks from an arithmetic progression and
Galois group of Laguerre polynomials, Int. J. Number Th. 11 (2015), 233–250.
[68] N. Saradha, T.N. Shorey, R. Tijdeman, On the equation x(x+1) · · · (x+k−1) =
y(y + d) · · · (y + (mk − 1)d), m = 1, 2, Acta Arith. 71 (1995), 181–196.
[69] A. Schinzel, On two theorems of Gelfond and some of their applications, Acta
Arith. 13 (1967), 177–236.
[70] T.N. Shorey, Perfect powers in products of arithmetic progression with ﬁxed
initial term, Indag. Math. (N.S.) 7 (1996), 521–525.
[71] T.N. Shorey, Powers in arithmetic progressions III, The Riemann zeta function
and related themes: papers in honour of Professor K. Ramachandra, Ramanu-
jan Math. Soc. Lect. Notes Ser. 2, Ramanujan Math. Soc., 2006, 131–140.
[72] C.L. Siegel (under the pseudonym X), The integer solutions of the equation
y2 = ax
n + bx
n−1 + · · · + k, J. London Math. Soc. 1 (1926), 66–68.
[73] C.L. Siegel, ¨Uber einige Anwendungen diophantischer Approximationen. Abh.
Preuss. Akad. Wiss. Phys.-Math. Kl. 1929, Nr. 1, 70 pp. Gesammelte Abhand-
lungen, vol. I, 209-266. Springer, Berlin, 1966.
[74] M. Ska lba, Products of disjoint blocks of consecutive integers which are powers,
Colloq. Math. 98 (2003), 1–3.
[75] T. Stoll, R.F. Tichy, The Diophantine equation α
( x
m) + β(y
n
) = γ, Publ. Math.
Debrecen 64 (2004), 155–165.
[76] R.J. Stroeker, B.M.M. De Weger, Elliptic Binomial Diophantine Equations,
Math. Comp. 68 (1999), 1257–1281.
[77] Sz. Tengely, N. Varga, On a generalization of a problem of Erd˝os and Graham,
Publ. Math. Debrecen 84 (2014), 475–482.
[78] M. Ulas, On products of disjoint blocks of consecutive integers, Enseign. Math.
51 (2005), 331–334.
[79] P.-Z. Yuan, On a special diophantine equation a( x
m) = byr + c, Publ. Math.
Debrecen 44 (1994), 137–143.

L. Hajdu
Institute of Mathematics, University of Debrecen,
P. O. Box 12, H-4010 Debrecen, Hungary
Email address: hajdul@science.unideb.hu

R. Tijdeman
Mathematical Institute
Leiden University
Postbus 9512, 2300 RA Leiden, The Netherlands
Email address: tijdeman@math.leidenuniv.nl
