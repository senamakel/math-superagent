<!-- source: https://arxiv.org/pdf/0801.4459 | converted from PDF -->

arXiv:0801.4459v4  [math.NT]  16 Mar 2010
INTEGRAL POINTS ON HYPERELLIPTIC CURVES

Y. BUGEAUD, M. MIGNOTTE, S. SIKSEK, M. STOLL, SZ. TENGELY

Abstract. Let C : Y 2 = anX n + · · · + a0 be a hyperelliptic curve with the
ai rational integers, n ≥ 5, and the polynomial on the right irreducible. Let
J be its Jacobian. We give a completely explicit upper bound for the integral
points on the model C, provided we know at least one rational point on C
and a Mordell–Weil basis for J(Q). We also explain a powerful reﬁnement of
the Mordell–Weil sieve which, combined with the upper bound, is capable of
determining all the integral points. Our method is illustrated by determining
the integral points on the genus 2 hyperelliptic models Y 2 − Y = X 5 − X and(Y
2 ) = (X
5 ).
 1. Introduction

Consider the hyperelliptic curve with aﬃne model

(1) C : Y 2 = anX n + an−1X n−1 + · · · + a0,

with a0, . . . , an rational integers, an ̸= 0, n ≥ 5, and the polynomial on the right
irreducible. Let H = max{|a0|, . . . , |an|}. In one of the earliest applications of his
theory of lower bounds for linear forms in logarithms, Baker [2] showed that any
integral point (X, Y ) on this aﬃne model satisﬁes

max(|X|, |Y |) ≤ exp exp exp{(n10nH)
n
2 }.

Such bounds have been improved considerably by many authors, including Sprindˇzuk
[43], Brindza [6], Schmidt [39], Poulakis [37], Bilu [3], Bugeaud [14] and Voutier
[50]. Despite the improvements, the bounds remain astronomical and often involve
inexplicit constants.
In this paper we explain a new method for explicitly computing the integral
points on aﬃne models of hyperelliptic curves (1). The method falls into two
distinct steps:
(i) We give a completely explicit upper bound for the size of integral solutions
of (1). This upper bound combines the many reﬁnements found in the
papers of Voutier, Bugeaud, etc., together with Matveev’s bounds for linear
forms in logarithms [30], and a method for bounding the regulators based
on a theorem of Landau [28].
(ii) The bounds obtained in (i), whilst substantially better than bounds given
by earlier authors, are still astronomical. We explain a powerful variant of
the Mordell–Weil sieve which, combined with the bound obtained in (i), is
capable of showing that the known solutions to (1) are the only ones.
Step (i) requires two assumptions:

Date: October 23, 2018.
2000 Mathematics Subject Classiﬁcation. Primary 11G30, Secondary 11J8.

1

2 Y. BUGEAUD, M. MIGNOTTE, S. SIKSEK, M. STOLL, SZ. TENGELY

(a) We assume that we know at least one rational point P0 on C.
(b) Let J be the Jacobian of C. We assume that a Mordell–Weil basis for J(Q)
is known.
For step (ii) we need assumptions (a), (b) and also:

(c) We assume that the canonical height ˆh : J(Q) → R is explicitly computable
and that we have explicit bounds for the diﬀerence

(2) µ1 ≤ h(D) − ˆh(D) ≤ µ′
1
where h is an appropriately normalized logarithmic height on J that allows
us to enumerate points P in J(Q) with h(P ) ≤ B for a given bound B.
Assumptions (a)–(c) deserve a comment or two. For many families of curves of
higher genus, practical descent strategies are available for estimating the rank of the
Mordell–Weil group; see for example [17], [36], [38] and [45]. To provably determine
the Mordell–Weil group one however needs bounds for the diﬀerence between the
logarithmic and canonical heights. For Jacobians of curves of genus 2 such bounds
have been determined by Stoll [44], [46], building on previous work of Flynn and
Smart [24]. At present, no such bounds have been determined for Jacobians of
curves of genus ≥ 3, although work on this is in progress. The assumption about
the knowledge of a rational point is a common sense assumption that brings some
simpliﬁcations to our method, although the method can be modiﬁed to cope with
the situation where no rational point is known. However, if a search on a curve of
genus ≥ 2 reveals no rational points, it is probable that there are none, and the
methods of [11], [12], [13] are likely to succeed in proving this.
We illustrate the practicality of our approach by proving the following results.

Theorem 1. The only integral solutions to the equation

(3) Y 2 − Y = X 5 − X

are
 (X, Y ) = (−1, 0), (−1, 1), (0, 0), (0, 1), (1, 0), (1, 1), (2, −5),

(2, 6), (3, −15), (3, 16), (30, −4929), (30, 4930).

Theorem 2. The only integral solutions to the equation

(4) (Y
2
 ) = (
X
5
 )

are

(X, Y ) = (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1), (5, −1),

(5, 2), (6, −3), (6, 4), (7, −6), (7, 7), (15, −77), (15, 78), (19, −152), (19, 153).

Equations (3) and (4) are of historical interest and Section 2 gives a brief outline
of their history. For now we merely mention that these two equations are the
ﬁrst two problems on a list of 22 unsolved Diophantine problems [19], compiled by
Evertse and Tijdeman following a recent workshop on Diophantine equations at
Leiden.
To appreciate why the innocent-looking equations (3) and (4) have resisted pre-
vious attempts, let us brieﬂy survey the available methods which apply to hyper-
elliptic curves and then brieﬂy explain why they fail in these cases. To determine
the integral points on the aﬃne model C given by an equation (1) there are four
available methods:
 3

(I) The ﬁrst is Chabauty’s elegant method which in fact determines all rational
points on C in many cases, provided the rank of the Mordell–Weil group
of its Jacobian is strictly less than the genus g; see for example [22], [54].
Chabauty’s method fails if the rank of the Mordell–Weil group exceeds the
genus.
(II) A second method is to use coverings, often combined with a version of
Chabauty called ‘Elliptic Curve Chabauty’. See [8], [9], [25], [26]. This
approach often requires computations of Mordell–Weil groups over number
ﬁelds (and does fail if the rank of the Mordell–Weil groups is too large).
(III) A third method is to combine Baker’s approach through S-units with the
LLL algorithm to obtain all the solutions provided that certain relevant
unit groups and class groups can be computed; for a modern treatment,
see [4] or [42, Section XIV.4]. This strategy often fails in practice as the
number ﬁelds involved have very high degree.
(IV) A fourth approach is to apply Skolem’s method to the S-unit equations
(see [42, Section III.2]). This needs the same expensive information as the
third method.

The Jacobians of the curves given by (3) and (4) respectively have ranks 3 and 6
and so Chabauty’s method fails. To employ Elliptic Curve Chabauty would require
the computation of Mordell–Weil groups of elliptic curves without rational 2-torsion
over number ﬁelds of degree 5 (which does not seem practical at present). To apply
the S-unit approach (with either LLL or Skolem) requires the computations of the
unit groups and class groups of several number ﬁelds of degree 40; a computation
that seems completely impractical at present.

Our paper is arranged as follows. Section 2 gives a brief history of equations (3)
and (4). In Section 3 we show, after appropriate scaling, that an integral point
(x, y) satisﬁes x − α = κξ2 where α is some ﬁxed algebraic integer, ξ ∈ Q(α), and
κ is an algebraic integer belonging to a ﬁnite computable set. In Section 9 we give
bounds for the size of solutions x ∈ Z to an equation of the form x − α = κξ2 where
α and κ are ﬁxed algebraic integers. Thus, in eﬀect, we obtain bounds for the size of
solutions integral points on our aﬃne model for (1). Sections 4–8 are preparation for
Section 9: in particular Section 4 is concerned with heights; Section 5 explains how
a theorem of Landau can be used to bound the regulators of number ﬁelds; Section 6
collects and reﬁnes various results on appropriate choices of systems of fundamental
units; Section 7 is devoted to Matveev’s bounds for linear forms in logarithms; in
Section 8 we use Matveev’s bounds and the results of previous sections to prove a
bound on the size of solutions of unit equations; in Section 9 we deduce the bounds
for x alluded to above from the bounds for solutions of unit equations. Despite our
best eﬀorts, the bounds obtained for x are still so large that no naive search up
to those bounds is conceivable. Over the next three sections 10, 11, 12 we explain
how to sieve eﬀectively up to these bounds using the Mordell–Weil group of the
Jacobian. In particular, Section 11 gives a powerful reﬁnement of the Mordell–
Weil sieve ([11], [13]) which we expect to have applications elsewhere. Finally, in
Section 13 we apply the method of this paper to prove Theorems 1 and 2.
We are grateful to the referee and editors for many useful comments, and to Mr.
Homero Gallegos–Ruiz for spotting many misprints.

4 Y. BUGEAUD, M. MIGNOTTE, S. SIKSEK, M. STOLL, SZ. TENGELY

2. History of Equations (3) and (4)

The equation (3) is a special case of the family of Diophantine equations

(5) Y p − Y = X q − X, 2 ≤ p < q.

This family has previously been studied by Fielder and Alford [20] and by Mignotte
and Peth˝o [31]. The (genus 1) case p = 2, q = 3 was solved by Mordell [32] who
showed that the only solutions in this case are

(X, Y ) = (0, 0), (0, 1), (±1, 0), (±1, 1), (2, 3), (2, −2), (6, 15), (6, −14).

Fielder and Alford presented the following list of solutions with X, Y > 1:

(p, q, X, Y ) = (2, 3, 2, 3), (2, 3, 6, 15), (2, 5, 2, 6), (2, 5, 3, 16),

(2, 5, 30, 4930), (2, 7, 5, 280), (2, 13, 2, 91), (3, 7, 3, 13).

Mignotte and Peth˝o proved that for given p and q with 2 ≤ p < q, the Diophantine
equation (5) has only a ﬁnite number of integral solutions. Assuming the abc-
conjecture, they showed that equation (5) has only ﬁnitely many solutions with X,
Y > 1.
If p = 2, q > 2 and y is a prime power, then Mignotte and Peth˝o found all
solutions of the equation and these are all in Fielder and Alford’s list.

Equation (4) is a special case of the Diophantine equation

(6) (
n
k
) = (
m
l
 )
,

in unknowns k, l, m, n. This is usually considered with the restrictions 2 ≤ k ≤ n/2,
and 2 ≤ l ≤ m/2. The only known solutions (with these restrictions) are the
following
(
16
2
 ) = (
10
3
 )
, (
56
2
 ) = (
22
3
 )
, (
120
2
 ) = (
36
3
 )
,
(
21
2
 ) = (
10
4
 )
, (
153
2
 ) = (
19
5
 )
, (
78
2
 ) = (
15
5
 ) = (
14
6
 )
,
(
221
2
 ) = (17
8
 )
, (
F2i+2F2i+3
F2iF2i+3
 ) = (
F2i+2F2i+3 − 1
F2iF2i+3 + 1
 ) for i = 1, 2, . . . ,

where Fn is the nth Fibonacci number. It is known that there are no other non-
trivial solutions with (
n
k) ≤ 1030 or n ≤ 1000; see [53]. The inﬁnite family of
solutions was found by Lind [29] and Singmaster [41].
Equation (6) has been completely solved for pairs

(k, l) = (2, 3), (2, 4), (2, 6), (2, 8), (3, 4), (3, 6), (4, 6), (4, 8).

These are the cases when one can easily reduce the equation to the determination
of solutions of a number of Thue equations or elliptic Diophantine equations. In
1966, Avanesov [1] found all solutions of equation (6) with (k, l) = (2, 3). De Weger
[52] and independently Pint´er [34] solved the equation with (k, l) = (2, 4). The case
(k, l) = (3, 4) reduces to the equation Y (Y +1) = X(X +1)(X +2) which was solved
by Mordell [32]. The remaining pairs (2, 6), (2, 8), (3, 6), (4, 6), (4, 8) were treated
by Stroeker and de Weger [49], using linear forms in elliptic logarithms.
There are also some general ﬁniteness results related to equation (6). In 1988,
Kiss [27] proved that if k = 2 and l is a given odd prime, then the equation has

5

only ﬁnitely many positive integral solutions. Using Baker’s method, Brindza [7]
showed that equation (6) with k = 2 and l ≥ 3 has only ﬁnitely many positive
integral solutions.
 3. Descent

Consider the integral points on the aﬃne model of the hyperelliptic curve (1).
If the polynomial on the right-hand side is reducible then the obvious factorisation
argument reduces the problem of determining the integral points on (1) to deter-
mining those on simpler hyperelliptic curves, or on genus 1 curves. The integral
points on a genus 1 curve can be determined by highly successful algorithms (e.g.
[42], [48]) based on LLL and David’s bound for linear forms in elliptic logarithms.
We therefore suppose henceforth that the polynomial on the right-hand side of
(1) is irreducible; this is certainly the most diﬃcult case. By appropriate scaling,
one transforms the problem of integral points on (1) to integral points on a model
of the form

(7) ay2 = x
n + bn−1x
n−1 + · · · + b0,

where a and the bi are integers, with a ̸= 0. We shall work henceforth with this
model of the hyperelliptic curve. Denote the polynomial on the right-hand side by
f and let α be a root of f . Then a standard argument shows that

x − α = κξ2

where κ, ξ ∈ K = Q(α) and κ is an algebraic integer that comes from a ﬁnite
computable set. In this section we suppose that the Mordell–Weil group J(Q)
of the curve C is known, and we show how to compute such a set of κ using our
knowledge of the Mordell–Weil group J(Q). The method for doing this depends on
whether the degree n is odd or even.

3.1. The Odd Degree Case. Each coset of J(Q)/2J(Q) has a coset representative
of the form ∑m
i=1(Pi − ∞) where the set {P1, . . . , Pm} is stable under the action
of Galois, and where all y(Pi) are non-zero. Now write x(Pi) = γi/d
2
i where γi is
an algebraic integer and di ∈ Z≥1; moreover if Pi, Pj are conjugate then we may
suppose that di = dj and so γi, γj are conjugate. To such a coset representative of
J(Q)/2J(Q) we associate
 κ = a(m mod 2) m∏

i=1
 (
γi − αd
2
i ) .

Lemma 3.1. Let K be a set of κ associated as above to a complete set of coset
representatives of J(Q)/2J(Q). Then K is a ﬁnite subset of OK and if (x, y) is an
integral point on the model (7) then x − α = κξ2 for some κ ∈ K and ξ ∈ K.

Proof. This follows trivially from the standard homomorphism

θ : J(Q)/2J(Q) → K ∗/K ∗2

that is given by

θ
 ( m∑

i=1(Pi − ∞)

)
 = am m∏

i=1 (x(Pi) − α) (mod K ∗2)

for coset representatives ∑(Pi − ∞) with y(Pi) ̸= 0; see Section 4 of [45]. □

6 Y. BUGEAUD, M. MIGNOTTE, S. SIKSEK, M. STOLL, SZ. TENGELY

3.2. The Even Degree Case. As mentioned in the introduction, we shall assume
the existence of at least one rational point P0. If P0 is one of the two points at
inﬁnity, let ǫ0 = 1. Otherwise, as f is irreducible, y(P0) ̸= 0; write x(P0) = γ0/d
2
0
with γ0 ∈ Z and d0 ∈ Z≥1 and let ǫ0 = γ0 − αd
2
0.
Each coset of J(Q)/2J(Q) has a coset representative of the form ∑m
i=1(Pi − P0)
where the set {P1, . . . , Pm} is stable under the action of Galois, and where all y(Pi)
are non-zero for i = 1, . . . , m. Write x(Pi) = γi/d
2
i where γi is an algebraic integer
and di ∈ Z≥1; moreover if Pi, Pj are conjugate then we may suppose that di = dj
and so γi, γj are conjugate. To such a coset representative of J(Q)/2J(Q) we
associate
 ǫ = ǫ(m mod 2)
0
 m∏

i=1
 (
γi − αd
2
i ) .

Lemma 3.2. Let E be a set of ǫ associated as above to a complete set of coset
representatives of J(Q)/2J(Q). Let ∆ be the discriminant of the polynomial f . For
each ǫ ∈ E, let Bǫ be the set of square-free rational integers supported only by primes
dividing a∆ NormK/Q(ǫ). Let K = {ǫb : ǫ ∈ E, b ∈ Bǫ}. Then K is a ﬁnite subset
of OK and if (x, y) is an integral point on the model (7) then x − α = κξ2 for some
κ ∈ K and ξ ∈ K.

Proof. In our even degree case, the homomorphism θ takes values in K ∗/Q∗K ∗2.
Thus if (x, y) is an integral point on the model (7), we have that (x − α) = ǫbξ2 for
some ǫ ∈ E and b a square-free rational integer. A standard argument shows that
2 | ord℘(x − α) for all prime ideals ℘ ∤ a∆. Hence, 2 | ord℘(b) for all ℘ ∤ a∆ǫ. Let
℘ | p where p is a rational prime not dividing a∆ NormK/Q(ǫ). Then p is unramiﬁed
in K/Q and so ordp(b) = ord℘(b) ≡ 0 (mod 2). This shows that b ∈ Bǫ and proves
the lemma. □

3.3. Remarks. The following remarks are applicable both to the odd and the even
degree cases.
• We point out that even if we do not know coset representatives for J(Q)/2J(Q),
we can still obtain a suitable (though larger) set of κ that satisﬁes the con-
clusions of Lemmas 3.1 and 3.2 provided we are able to compute the class
group and unit group of the number ﬁeld K; for this see for example [8,
Section 2.2].
• We can use local information at small and bad primes to restrict the set K
further, compare [11] and [12], where this is applied to rational points. In
our case, we can restrict the local computations to x ∈ Zp instead of Qp.

4. Heights

We ﬁx once and for all the following notation.

K a number ﬁeld,
OK the ring of integers of K,
MK the set of all places of K,
M 0
K the set of non-Archimedean places of K,
M ∞
K the set of Archimedean places of K,
υ a place of K,
Kυ the completion of K at υ,
dυ the local degree [Kυ : Qυ].
 7

For υ ∈ MK, we let |·|υ be the usual normalized valuation corresponding to υ;
in particular if υ is non-Archimedean and p is the rational prime below υ then
|p|υ = p−1. Thus if L/K is a ﬁeld extension, and ω a place of L above υ then
|α|ω = |α|υ, for all α ∈ K.
Deﬁne
 ∥α∥υ = |α|dυ
υ .

Hence for α ∈ K ∗, the product formula states that
∏

υ∈MK∥α∥υ = 1.

In particular, if υ is Archimedean, corresponding to a real or complex embedding
σ of K then

|α|υ = |σ(α)| and ∥α∥υ =
 {|σ(α)| if σ is real
|σ(α)|2 if σ is complex.

For α ∈ K, the (absolute) logarithmic height h(α) is given by

(8) h(α) = 1
[K : Q]
 ∑

υ∈MK dυ log max {1, |α|υ} = 1
[K : Q]
 ∑

υ∈MK log max {1, ∥α∥υ} .

The absolute logarithmic height of α is independent of the ﬁeld K containing α.
We shall need the following elementary properties of heights.

Lemma 4.1. For any non-zero algebraic number α, we have h(α
−1) = h(α). For
algebraic numbers α1, . . . , αn, we have

h(α1α2 · · · αn) ≤ h(α1)+· · ·+h(αn), h(α1+· · ·+αn) ≤ log n+h(α1)+· · ·+h(αn).

Proof. The lemma is Exercise 8.8 in [40]. We do not know of a reference for
the proof and so we will indicate brieﬂy the proof of the second (more diﬃcult)
inequality. For υ ∈ MK, choose iυ in {1, . . . , n} to satisfy max{|α1|υ, . . . , |αn|υ} =
|αiυ |υ. Note that

|α1 + · · · + αn|υ ≤ ǫυ|αiυ |υ, where ǫυ =
 {
n if υ is Archimedean,
1 otherwise.

Thus

log max{1, |α1+· · ·+αn|υ} ≤ log ǫυ+log max{1, |αiυ |υ} ≤ log ǫυ+
 n∑

i=1 log max{1, |αi|υ}.

Observe that
 1
[K : Q]
 ∑

υ∈MK dυ log ǫυ = log n
[K : Q]
 ∑

υ∈M ∞
K dυ = log n;

the desired inequality follows from the deﬁnition of logarithmic height (8). □

8 Y. BUGEAUD, M. MIGNOTTE, S. SIKSEK, M. STOLL, SZ. TENGELY

4.1. Height Lower Bound. We need the following result of Voutier [51] concern-
ing Lehmer’s problem.

Lemma 4.2. Let K be a number ﬁeld of degree d. Let

∂K =
 



 log 2
d if d = 1, 2,

1
4 ( log log d
log d )3 if d ≥ 3.

Then, for every non-zero algebraic number α in K, which is not a root of unity,

deg(α) h(α) ≥ ∂K.

Throughout, by the logarithm of a complex number, we mean the principal
determination of the logarithm. In other words, if x ∈ C∗ we express x = reiθ

where r > 0 and −π < θ ≤ π; we then let log x = log r + iθ.

Lemma 4.3. Let K be a number ﬁeld and let

∂′
K = (
1 + π2

∂2
K
 )1/2 .

For any non-zero α ∈ K and any place υ ∈ MK
log|α|υ ≤ deg(α) h(α), log∥α∥υ ≤ [K : Q] h(α).

Moreover, if α is not a root of unity and σ is a real or complex embedding of K
then |log σ(α)| ≤ ∂′
K deg(α) h(α).

Proof. The ﬁrst two inequalities are an immediate consequence of the deﬁnition of
absolute logarithmic height. For the last, write σ(α) = ea+ib, with a = log|σ(α)|
and |b| ≤ π, and let d = deg(α). Then we have

|log σ(α)| = (a2 + b2)
1/2 ≤ (log2|σ(α)| + π2)
1/2 ≤ ((d h(α))
2 + π2)
1/2.

By Lemma 4.2 we have d h(α) ≥ ∂K , so

|log σ(α)| ≤ d h(α) (
1 + π2

∂2
K
 )1/2 ,

as required. □

5. Bounds for Regulators

Later on we need to give upper bounds for the regulators of complicated number
ﬁelds of high degree. The following lemma, based on bounds of Landau [28], is an
easy way to obtain reasonable bounds.

Lemma 5.1. Let K be a number ﬁeld with degree d = u + 2v where u and v
are respectively the numbers of real and complex embeddings. Denote the absolute
discriminant by DK and the regulator by RK, and the number of roots of unity in
K by w. Suppose, moreover, that L is a real number such that DK ≤ L. Let

a = 2−v π−d/2 √
L.

Deﬁne the function fK(L, s) by

fK(L, s) = 2−u w as (
Γ(s/2)
)u (
Γ(s)
)vsd+1 (s − 1)
1−d,

and let BK(L) = min {fK(L, 2 − t/1000) : t = 0, 1, . . . , 999}. Then RK < BK(L).

9

Proof. Landau [28, proof of Hilfssatz 1] established the inequality RK < fK(DK, s)
for all s > 1. It is thus clear that RK < BK(L). □

Perhaps a comment is in order. For a complicated number ﬁeld of high degree
it is diﬃcult to calculate the discriminant DK exactly, though it is easy to give an
upper bound L for its size. It is also diﬃcult to minimise the function fK(L, s)
analytically, but we have found that the above gives an accurate enough result,
which is easy to calculate on a computer.

6. Fundamental Units

For the number ﬁelds we are concerned with, we shall need to work with a certain
system of fundamental units, given by the following lemma due to Bugeaud and
Gy˝ory, which is Lemma 1 of [15].

Lemma 6.1. Let K be a number ﬁeld of degree d and let r = rK be its unit rank
and RK its regulator. Deﬁne the constants

c1 = c1(K) = (r !)
2

2r−1dr , c2 = c2(K) = c1
 ( d
∂K
 )r−1 , c3 = c3(K) = c1 d
r

∂K .

Then K admits a system {ε1, . . . , εr} of fundamental units such that:

(i)
 r∏

i=1 h(εi) ≤ c1RK,

(ii) h(εi) ≤ c2RK , 1 ≤ i ≤ r,

(iii) Write M for the r×r-matrix (log∥εi∥υ) where υ runs over r of the Archimedean
places of K and 1 ≤ i ≤ r. Then the absolute values of the entries of M−1

are bounded above by c3.

Lemma 6.2. Let K be a number ﬁeld of degree d, and let {ε1, . . . , εr} be a system
of fundamental units as in Lemma 6.1. Deﬁne the constant c4 = c4(K) = rdc3.
Suppose ε = ζεb1
1 . . . εbr
r , where ζ is a root of unity in K. Then

max{|b1|, . . . , |br|} ≤ c4 h(ε).

Proof. Note that for any Archimedean place v of K,

log∥ε∥v = ∑ bi log∥εi∥v.

The lemma now follows from part (iii) of Lemma 6.1, plus the fact that log∥ε∥v ≤
d h(ε) for all v given by Lemma 4.3. □

The following result is a special case of Lemma 2 of [15].

Lemma 6.3. Let K be a number ﬁeld of unit rank r and regulator K. Let α be
a non-zero algebraic integer belonging to K. Then there exists a unit ε of K such
that
 h(αε) ≤ c5RK + log|NormK/Q(α)|
[K : Q]
where
 c5 = c5(K) = rr+1

2∂r−1
K .

10 Y. BUGEAUD, M. MIGNOTTE, S. SIKSEK, M. STOLL, SZ. TENGELY

Lemma 6.4. Let K be a number ﬁeld, β, ε ∈ K ∗ with ε being a unit. Let σ be the
real or complex embedding that makes |σ(βε)| minimal. Then

h(βε) ≤ h(β) − log|σ(βε)|.

Proof. As usual, write d = [K : Q] and dυ = [Kυ : Qυ]. Note

h(βε) = h(1/βε)

= 1
d
 ∑

υ∈M ∞
K dυ max{0, log(|βε|−1
υ )} + 1
d
 ∑

υ∈M 0
K
 dυ max{0, log(|βε|−1
υ )}

≤ log(|σ(βε)|−1) + 1
d
 ∑

υ∈M 0
K
 dυ max{0, log(|β|−1
υ )}

≤ − log|σ(βε)| + 1
d
 ∑

υ∈MK dυ max{0, log(|β|−1
υ )}

≤ − log|σ(βε)| + h(β),

as required. □

7. Matveev’s Lower Bound for Linear Forms in Logarithms

Let L be a number ﬁeld and let σ be a real or complex embedding. For α ∈ L∗

we deﬁne the modiﬁed logarithmic height of α with respect to σ to be

hL,σ(α) := max{[L : Q] h(α) , |log σ(α)| , 0.16}.

The modiﬁed height is clearly dependent on the number ﬁeld; we shall need the
following Lemma which gives a relation between the modiﬁed and absolute height.

Lemma 7.1. Let K ⊆ L be number ﬁelds and write

∂L/K = max {[L : Q] , [K : Q]∂′
K , 0.16[K : Q]
∂K
 } .

Then for any α ∈ K which is neither zero nor a root of unity, and any real or
complex embedding σ of L,
 hL,σ(α) ≤ ∂L/K h(α).

Proof. By Lemma 4.3 we have

[K : Q]∂′
K h(α) ≥ ∂′
K deg(α) h(α) ≥ |log σ(α)|.

Moreover, by Lemma 4.2,

0.16[K : Q] h(α)
∂K ≥ 0.16 deg(α) h(α)
∂K ≥ 0.16.

The lemma follows. □

We shall apply lower bounds on linear forms, more precisely a version of Matveev’s
estimates [30]. We recall that log denotes the principal determination of the loga-
rithm.
 11

Lemma 7.2. Let L be a number ﬁeld of degree d, with α1, . . . , αn ∈ L∗. Deﬁne a
constant C(L, n) := 3 · 30n+4 · (n + 1)
5.5 d
2 (1 + log d).
Consider the “linear form”
 Λ := α
b1
1 · · · α
bn
n − 1,

where b1, . . . , bn are rational integers and let B := max{|b1|, . . . , |bn|}. If Λ ̸= 0,
and σ is any real or complex embedding of L then

log|σ(Λ)| > −C(L, n)(1 + log(nB))
 n∏

j=1 hL,σ(αj).

Proof. This straightforward corollary of Matveev’s estimates is Theorem 9.4 of
[16]. □

8. Bounds for Unit Equations

Now we are ready to prove an explicit version of Lemma 4 of [14]. The proposition
below allows us to replace in the ﬁnal estimate the regulator of the larger ﬁeld by the
product of the regulators of two of its subﬁelds. This often results in a signiﬁcant
improvement of the upper bound for the height. This idea is due to Voutier [50].

Proposition 8.1. Let L be a number ﬁeld of degree d, which contains K1 and K2
as subﬁelds. Let RKi (respectively ri) be the regulator (respectively the unit rank)
of Ki. Suppose further that ν1, ν2 and ν3 are non-zero elements of L with height
≤ H (with H ≥ 1) and consider the unit equation

(9) ν1ε1 + ν2ε2 + ν3ε3 = 0

where ε1 is a unit of K1, ε2 a unit of K2 and ε3 a unit of L. Then, for i = 1 and 2,

h(νiεi/ν3ε3) ≤ A2 + A1 log{H + max{h(ν1ε1), h(ν2ε2)}},

where

A1 = 2H · C(L, r1 + r2 + 1) · c1(K1)c1(K2)∂L/L · (∂L/K1)
r1 · (∂L/K2 )
r2 · RK1 RK2,

and A2 = 2H + A1 + A1 log{(r1 + r2 + 1) · max{c4(K1), c4(K2), 1}}.

Proof. Let {µ1, . . . , µr1 } and {ρ1, . . . , ρr2} be respectively systems of fundamental
units for K1 and K2 as in Lemma 6.1; in particular we know that

(10)
 r1∏

j=1 h(µj ) ≤ c1(K1)RK1,
 r2∏

j=1 h(ρj) ≤ c1(K2)RK2.

We can write ε1 = ζ1µb1
1 · · · µbr1
r1 , ε2 = ζ2ρf1
1 · · · ρfr2
r2 ,
where ζ1 and ζ2 are roots of unity and b1, . . . , br1, and f1, . . . , fr2 are rational
integers. Set

B1 = max{|b1|, . . . , |br1|}, B2 = max{|f1|, . . . , |fr2|}, B = max{B1, B2, 1}.

Set α0 = −ζ2ν2/(ζ1ν1) and b0 = 1. By (9),
ν3ε3
ν1ε1 = α
b0
0 µ−b1
1 · · · µ−br1
r1 ρf1
1 · · · ρfr2
r2 − 1.

12 Y. BUGEAUD, M. MIGNOTTE, S. SIKSEK, M. STOLL, SZ. TENGELY

Now choose the real or complex embedding σ of L such that |σ((ν3ε3)/(ν1ε1))| is
minimal. We apply Matveev’s estimate (Lemma 7.2) to this “linear form”, obtain-
ing
 log ∣
∣
∣
∣σ ( ν3ε3
ν1ε1
 )∣
∣
∣
∣ > −C(L, n)(1 + log(nB)) hL,σ(α0)
 r1∏

j=1 hL,σ(µj)
 r2∏

j=1 hL,σ(ρj),

where n = r1 + r2 + 1. Using Lemma 7.1 and equation (10) we obtain

r1∏

j=1 hL,σ(µj) ≤ (∂L/K1)
r1 r1∏

j=1 h(µj) ≤ c1(K1)(∂L/K1 )
r1RK1 ,

and a similar estimate for ∏r2
j=1 hL,σ(ρj). Moreover, again by Lemma 7.1 and
Lemma 4.1, hL,σ(α0) ≤ 2H∂L/L. Thus

log ∣
∣
∣
∣σ ( ν3ε3
ν1ε1
 )∣
∣
∣
∣ > −A1(1 + log(nB)).

Now applying Lemma 6.4, we obtain that

h ( ν3ε3
ν1ε1
 ) ≤ h ( ν3
ν1
 ) + A1(1 + log(nB)) ≤ 2H + A1(1 + log(nB)).

The proof is complete on observing, from Lemma 6.2, that

B ≤ max{c4(K1), c4(K2), 1)} max{h(ε1), h(ε2), 1},

and from Lemma 4.1, h(νiεi) ≤ h(εi) + h(νi) ≤ h(ε) + H. □

9. Upper Bounds for the Size of
Integral Points on Hyperelliptic Curves

We shall need the following standard sort of lemma.

Lemma 9.1. Let a, b, c, y be positive numbers and suppose that

y ≤ a + b log(c + y).

Then y ≤ 2b log b + 2a + c.

Proof. Let z = c + y, so that z ≤ (a + c) + b log z. Now we apply case h = 1 of
Lemma 2.2 of [33]; this gives z ≤ 2(b log b + a + c), and the lemma follows. □

Theorem 3. Let α be an algebraic integer of degree at least 3, and let κ be a integer
belonging to K. Let α1, α2, α3 be distinct conjugates of α and κ1, κ2, κ3 be the
corresponding conjugates of κ. Let

K1 = Q(α1, α2, √κ1κ2), K2 = Q(α1, α3, √
κ1κ3), K3 = Q(α2, α3, √
κ2κ3),

and L = Q(α1, α2, α3, √
κ1κ2, √
κ1κ3).
Let R be an upper bound for the regulators of K1, K2 and K3. Let r be the maximum
of the unit ranks of K1, K2, K3. Let

c∗
j = max
1≤i≤3 cj(Ki).

Let N = max
1≤i,j≤3 ∣
∣NormQ(αi,αj )/Q(κi(αi − αj))
∣
∣2 .
 13

Let
 H ∗ = c∗
5R + log N
min1≤i≤3[Ki : Q] + h(κ).

Let
 A
∗
1 = 2H ∗ · C(L, 2r + 1) · (c∗
1)
2∂L/L · ( max
1≤i≤3 ∂L/Ki
)2r · R2,

and A
∗
2 = 2H ∗ + A
∗
1 + A
∗
1 log{(2r + 1) · max{c∗
4, 1}}.
If x ∈ Z\{0} satisﬁes x − α = κξ2 for some ξ ∈ K then

log|x| ≤ 8A
∗
1 log(4A
∗
1) + 8A
∗
2 + H ∗ + 20 log 2 + 13 h(κ) + 19 h(α).

Proof. Conjugating the relation x − α = κξ2 appropriately and taking diﬀerences
we obtain

α1 − α2 = κ2ξ2
2 − κ1ξ2
1, α3 − α1 = κ1ξ2
1 − κ3ξ2
3, α2 − α3 = κ3ξ2
3 − κ2ξ2
2.

Let τ1 = κ1ξ1, τ2 = √
κ1κ2ξ2, τ3 = √
κ1κ3ξ3.
Observe that

κ1(α1 − α2) = τ 2
2 − τ 2
1 , κ1(α3 − α1) = τ 2
1 − τ 2
3 , κ1(α2 − α3) = τ 2
3 − τ 2
2 ,

and τ2 ± τ1 ∈ K1, τ1 ± τ3 ∈ K2, τ3 ± τ2 ∈ √
κ1/κ2K3.
We claim that each τi ± τj can be written in the form νε where ε is a unit in one of
the Ki and ν ∈ L is an integer satisfying h(ν) ≤ H ∗. Let us show this for τ2 − τ3;
the other cases are either similar or easier. Note that τ2 − τ3 = √
κ1/κ2ν′′ where
ν′′ is an integer belonging to K3. Moreover, ν′′ divides
√ κ2
κ1 (τ3 − τ2) · √ κ2
κ1 (τ3 + τ2) = κ2(α2 − α3).

Hence |NormK3/Q(ν′′)| ≤ N . By Lemma 6.3, we can write ν′′ = ν′ε where ε ∈ K3
and
 h(ν′) ≤ c5(K3)R + log N
[K3 : Q] .

Now let ν = √
κ1/κ2ν′. Thus τ2 − τ3 = νε where h(ν) ≤ h(ν′) + h(κ) ≤ H ∗ proving
our claim.
We apply Proposition 8.1 to the unit equation

(τ1 − τ2) + (τ3 − τ1) + (τ2 − τ3) = 0,

which is indeed of the form ν1ε1 + ν2ε2 + ν3ε3 = 0 where the νi and εi satisfy the
conditions of that proposition with H replaced by H ∗. We obtain

h ( τ1 − τ2
τ1 − τ3
 ) ≤ A
∗
2 + A
∗
1 log{H ∗ + max{h(τ2 − τ3), h(τ1 − τ2)}}.

Observe that h(τi ± τj) ≤ log 2 + h(τi) + h(τj )

≤ log 2 + 2 h(κ) + 2 h(ξ)

≤ log 2 + 3 h(κ) + h(x − α)

≤ 2 log 2 + 3 h(κ) + h(α) + log|x|,

14 Y. BUGEAUD, M. MIGNOTTE, S. SIKSEK, M. STOLL, SZ. TENGELY

where we have made repeated use of Lemma 4.1. Thus

h ( τ1 − τ2
τ1 − τ3
 ) ≤ A
∗
2 + A
∗
1 log(A
∗
3 + log|x|),

where A
∗
3 = H ∗ + 2 log 2 + 3 h(κ) + h(α).
We also apply Proposition 8.1 to the unit equation

(τ1 + τ2) + (τ3 − τ1) − (τ2 + τ3) = 0,

to obtain precisely the same bound for h ( τ1+τ2
τ1−τ3
 )
. Using the identity
( τ1 − τ2
τ1 − τ3
 ) · ( τ1 + τ2
τ1 − τ3
 ) = κ1(α2 − α1)
(τ1 − τ3)2 ,

we obtain that

h(τ1 − τ3) ≤ log 2 + h(κ)
2 + h(α) + A
∗
2 + A
∗
1 log(A
∗
3 + log|x|).

Now
 log|x| ≤ log 2 + h(α) + h(x − α1)

≤ log 2 + h(α) + h(κ) + 2 h(τ1) (using x − α1 = τ 2
1 /κ1)

≤ 5 log 2 + h(α) + h(κ) + 2 h(τ1 + τ3) + 2 h(τ1 − τ3)

≤ 5 log 2 + h(α) + h(κ) + 2 h ( κ1(α3 − α1)
τ1 − τ3
 ) + 2 h(τ1 − τ3)

≤ 7 log 2 + 5 h(α) + 3 h(κ) + 4 h(τ1 − τ3)

≤ 9 log 2 + 9 h(α) + 5 h(κ) + 4A
∗
2 + 4A
∗
1 log(A
∗
3 + log|x|).

The theorem follows from Lemma 9.1. □

10. The Mordell–Weil Sieve I

The Mordell–Weil sieve is a technique that can be used to show the non-existence
of rational points on a curve (for example [11], [13]), or to help determine the set
of rational points in conjunction with the method of Chabauty (for example [10]);
for connections to the Brauer–Manin obstruction see, for example, [23], [35] or [47].
In this section and the next we explain how the Mordell–Weil sieve can be used to
show that any rational point on a curve of genus ≥ 2 is either a known rational
point or a very large rational point.
In this section we let C/Q be a smooth projective curve (not necessarily hyperel-
liptic) of genus g ≥ 2 and we let J be its Jacobian. As indicated in the introduction,
we assume the knowledge of some rational point on C; henceforth let D be a ﬁxed
rational point on C (or even a ﬁxed rational divisor of degree 1) and let  be the
corresponding Abel–Jacobi map:

 : C → J, P ↦→ [P − D].

Let W be the image in J of the known rational points on C. The Mordell–Weil
sieve is a strategy for obtaining a very large and ‘smooth’ positive integer B such
that (C(Q)) ⊆ W + BJ(Q).
 15

Recall that a positive integer B is called A-smooth if all its prime factors are ≤ A.
By saying that B is smooth, we loosely mean that it is A-smooth with A much
smaller than B.
Let S be a ﬁnite set of primes, which for now we assume to be primes of good
reduction for the curve C. The basic idea is to consider the following commutative
diagram.
 C(Q)  //

  
 J(Q)/BJ(Q)

α
  ∏

p∈S C(Fp)  // ∏

p∈S J(Fp)/BJ(Fp)

The image of C(Q) in J(Q)/BJ(Q) must then be contained in the subset of
J(Q)/BJ(Q) of elements that map under α into the image of the lower horizontal
map. If we ﬁnd that this subset equals the image of W in J(Q)/BJ(Q), then we
have shown that (C(Q)) ⊆ W + BJ(Q)

as desired. Note that, at least in principle, the required computation is ﬁnite: each
set C(Fp) is ﬁnite and can be enumerated, hence (C(Fp)) can be determined, and
we assume that we know explicit generators of J(Q), which allows us to construct
the ﬁnite set J(Q)/BJ(Q). In practice, and in particular for the application we
have in mind here, we will need a very large value of B, so this naive approach is
much too ineﬃcient. In [11] and [13], the authors describe how one can perform
this computation in a more eﬃcient way.
One obvious improvement is to replace the lower horizontal map in the diagram
above by a product of maps
 C(Qp) 
→ Gp/BGp

with suitable ﬁnite quotients Gp of J(Qp). We have used this to incorporate in-
formation modulo higher powers of p for small primes p. This kind of information
is often called “deep” information, as opposed to the “ﬂat” information obtained
from reduction modulo good primes.
We can always force B to be divisible by any given (not too big) number. In our
application we will want B to kill the rational torsion subgroup of J.

11. The Mordell–Weil Sieve II

We continue with the notation of Section 10. Let W be the image in J(Q) of
all the known rational points on C. We assume that the strategy of Section 10
is successful in yielding a large ‘smooth’ integer B such that any point P ∈ C(Q)
satisﬁes (P ) − w ∈ BJ(Q) for some w ∈ W , and moreover, that B kills all the
torsion of J(Q).
Let φ : Z
r → J(Q), φ(a1, . . . , ar) = ∑ aiDi,

so that the image of φ is simply the free part of J(Q). Our assumption is now that

(C(Q)) ⊂ W + φ(BZ
n).

16 Y. BUGEAUD, M. MIGNOTTE, S. SIKSEK, M. STOLL, SZ. TENGELY

Set L0 = BZ
n. We explain a method of obtaining a (very long) decreasing
sequence of lattices in Z
n:

(11) BZ
n = L0 ⊋ L1 ⊋ L2 ⊋ · · · ⊋ Lk
such that (C(Q)) ⊂ W + φ(Lj)
for j = 1, . . . , k.
If q is a prime of good reduction for J we denote by

φq : Z
r → J(Fq), φq(a1, . . . , ar) = ∑ ai ˜Di,

and so φq(l) = ˜φ(l).

Lemma 11.1. Let W be a ﬁnite subset of J(Q), and let L be a subgroup of Z
r.
Suppose that (C(Q)) ⊂ W + φ(L). Let q be a prime of good reduction for C and
J. Let L′ be the kernel of the restriction φq|L. Let l1, . . . , lm be representatives of
the non-zero cosets of L/L′ and suppose that ˜w + φq(li) /∈ C(Fq) for all w ∈ W
and i = 1, . . . , m. Then (C(Q)) ⊂ W + φ(L′).

Proof. Suppose P ∈ C(Q). Since j(C(Q)) ⊂ W + φ(L), we may write (P ) =
w + φ(l) for some l ∈ L. Now let l0 = 0, so that l0, . . . , lm represent all cosets of
L/L′. Then l = li + l′ for some l′ ∈ L′ and i = 0, . . . , m. However, φq(l′) = 0, or in
other words, ˜φ(l′) = 0. Hence

( ˜P ) = ˜(P ) = ˜w + φq(l) = ˜w + φq(li) + φq(l′) = ˜w + φq(li).

By hypothesis, ˜w + φq(li) /∈ C(Fq) for i = 1, . . . , m, so i = 0 and so li = 0. Hence
(P ) = w + l′ ∈ W + L′ as required. □

We obtain a very long strictly decreasing sequence of lattices as in (11) by re-
peated application of Lemma 11.1. However, the conditions of Lemma 11.1 are
unlikely to be satisﬁed for a prime q chosen at random. Here we give criteria that
we have employed in practice to choose the primes q.
(I) gcd(B, #J(Fq)) > (#J(Fq))
0.6,
(II) L′ ̸= L,
(III) #W · (#L/L′ − 1) < 2q,
(IV) ˜w + φq(li) /∈ C(Fq) for all w ∈ W and i = 1, . . . , m.
The criteria I–IV are listed in the order in which we check them in practice. Cri-
terion IV is just the criterion of the lemma. Criterion II ensures that L′ is strictly
smaller than L, otherwise we gain no new information. Although we would like L′

to be strictly smaller than L, we do not want the index L/L′ to be too large and
this is reﬂected in Criteria I and III. Note that the number of checks required by
Criterion IV (or the lemma) is #W · (#L/L′ − 1). If this number is large then
Criterion IV is likely to fail. Let us look at this in probabilistic terms. Assume that
the genus of C is 2. Then the probability that a random element of J(Fq) lies in
the image of C(Fq) is about 1/q. If N = #W · (#L/L′ − 1) then the probability
that Criterion IV is satisﬁed is about (1 − q−1)
N . Since (1 − q−1)
q ∼ e−1, we do
not want N to be too large in comparison to q, and this explains the choice of 2q
in Criterion III.
We still have not justiﬁed Criterion I. The computation involved in obtaining L′

is a little expensive. Since we need to do this with many primes, we would like a

17

way of picking only primes where this computation is not wasted, and in particular
#L/L′ is not too large. Now at every stage of our computations, L will be some
element of our decreasing sequence (11) and so contained in BZ
n. Criterion I
ensures that a ‘large chunk’ of L will be in the kernel of φq : Z
n → J(Fq) and so
that #L/L′ is not too large. The exponent 0.6 in Criterion I is chosen on the basis
of computational experience.

12. Lower Bounds for the Size of Rational Points

In this section, we suppose that the strategy of Sections 10 and 11 succeeded in
showing that (C(Q)) ⊂ W + φ(L) for some lattice L of huge index in Z
r, where
W is the image of J of the set of known rational points in C. In this section we
provide a lower bound for the size of rational points not belonging to the set of
known rational points.

Lemma 12.1. Let W be a ﬁnite subset of J(Q), and let L be a sublattice of Z
r.
Suppose that (C(Q)) ⊂ W + φ(L). Let µ1 be a lower bound for h − ˆh as in (2).
Let
 µ2 = max {√ˆh(w) : w ∈ W } .

Let M be the height-pairing matrix for the Mordell–Weil basis D1, . . . , Dr and let
λ1, . . . , λr be its eigenvalues. Let

µ3 = min {√
λj : j = 1, . . . , r} .

Let m(L) be the Euclidean norm of the shortest non-zero vector of L, and suppose
that µ3m(L) ≥ µ2. Then, for any P ∈ C(Q), either (P ) ∈ W or

h((P )) ≥ (µ3m(L) − µ2)
2 + µ1.

Note that m(L) is called the minimum of L and can be computed using an
algorithm of Fincke and Pohst [21].

Proof. Suppose that (P ) /∈ W . Then (P ) = w + φ(l) for some non-zero element
l ∈ L. In particular, if ∥·∥ denotes Euclidean norm then ∥l∥ ≥ m(L).
We can write M = N ΛN t where N is orthogonal and Λ is the diagonal matrix
with diagonal entries λi. Let x = lN and write x = (x1, . . . , xr). Then

ˆh(φ(l)) = lM lt = xΛx
t ≥ µ2
3∥x∥2 = µ2
3∥l∥2 ≥ µ2
3m(L)
2.

Now recall that D ↦→ √ˆh(D) deﬁnes a norm on J(Q) ⊗ R and so by the triangle
inequality √ˆh((P )) ≥ √ˆh(φ(l)) − √ˆh(w) ≥ µ3m(L) − µ2.

The lemma now follows from (2). □

Remark. We can replace µ3m(L) with the minimum of L with respect to the
height pairing matrix. This is should lead to a very slight improvement. Since
in practice our lattice L has very large index, computing the minimum of L with
respect to the height pairing matrix may require the computation of the height
pairing matrix to very great accuracy, and such a computation is inconvenient. We
therefore prefer to work with the Euclidean norm on Z
r.

18 Y. BUGEAUD, M. MIGNOTTE, S. SIKSEK, M. STOLL, SZ. TENGELY

Table 1.

coset of unit rank bound R for bound for
J(Q)/2J(Q) κ of Ki regulator of Ki log x
0 1 12 1.8 × 1026 1.0 × 10263

D1 −2α 21 6.2 × 1053 7.6 × 10492

D2 4 − 2α 25 1.3 × 1054 2.3 × 10560

D3 −4 − 2α 21 3.7 × 1055 1.6 × 10498

D1 + D2 −2α + α
2 21 1.0 × 1052 3.2 × 10487

D1 + D3 2α + α
2 25 7.9 × 1055 5.1 × 10565

D2 + D3 −4 + α
2 21 3.7 × 1055 1.6 × 10498

D1 + D2 + D3 8α − 2α
3 25 7.9 × 1055 5.1 × 10565

13. Proofs of Theorems 1 and 2

The equation Y 2 − Y = X 5 − X is transformed into

(12) C : 2y2 = x
5 − 16x + 8,

via the change of variables y = 4Y − 2 and x = 2X which preserves integrality.
We shall work the model (12). Let C be the smooth projective genus 2 curve with
aﬃne model given by (12), and let J be its Jacobian. Using MAGMA [5] we know
that J(Q) is free of rank 3 with Mordell–Weil basis given by

D1 = (0, 2) − ∞, D2 = (2, 2) − ∞, D3 = (−2, 2) − ∞.

The MAGMA programs used for this step are based on Stoll’s papers [44], [45], [46].
Let f = x
5 − 16x + 8. Let α be a root of f . We shall choose for coset rep-
resentatives of J(Q)/2J(Q) the linear combinations ∑3
i=1 niDi with ni ∈ {0, 1}.
Then x − α = κξ2,
where κ ∈ K and K is constructed as in Lemma 3.1. We tabulate the κ correspond-
ing to the ∑3
i=1 niDi in Table 1.
Next we compute the bounds for log x given by Theorem 3 for each value of
κ. We implemented our bounds in MAGMA. Here the Galois group of f is S5 which
implies that the ﬁelds K1, K2, K3 corresponding to a particular κ are isomorphic.
The unit ranks of Ki, the bounds for their regulator as given by Lemma 5.1, and
the corresponding bounds for log x are tabulated in Table 1.
A quick search reveals 17 rational points on C:

∞, (−2, ±2), (0, ±2), (2, ±2), (4, ±22), (6, ±62),

(1/2, ±1/8), (−15/8, ±697/256), (60, ±9859).

Let W denote the image of this set in J(Q). Applying the implementation of the
Mordell–Weil sieve due to Bruin and Stoll which is explained in Section 10 we
obtain that (C(Q)) ⊆ W + BJ(Q) where

B = 4449329780614748206472972686179940652515754483274306796568214048000

= 28 · 34 · 53 · 73 · 112 · 132 · 172 · 19 · 23 · 29 · 312 · ∏

37≤p≤149
p̸=107
 p .
 19

For this computation, we used “deep” information modulo 29, 36, 54, 73, 113, 132,
172, 192, and “ﬂat” information from all primes p < 50000 such that #J(Fp) is
500-smooth (but keeping only information coming from the maximal 150-smooth
quotient group of J(Fp)). Recall that an integer is called A-smooth if all its prime
divisors are ≤ A. This computation took about 7 hours on a 2 GHz Intel Core 2
CPU.
We now apply the new extension of the Mordell–Weil sieve explained in Sec-
tion 11. We start with L0 = BZ
3 where B is as above. We successively apply
Lemma 11.1 using all primes q < 106 which are primes of good reduction and sat-
isfy criteria I–IV of Section 11. There are 78498 primes less than 106. Of these, we
discard 2, 139, 449 as they are primes of bad reduction for C. This leaves us with
78495 primes. Of these, Criterion I fails for 77073 of them, Criterion II fails for
220 of the remaining, Criterion III fails for 43 primes that survive Criteria I and II,
and Criterion IV fails for 237 primes that survive Criteria I–III. Altogether, only
922 primes q < 106 satisfy Criteria I–IV and increase the index of L.
The index of the ﬁnal L in Z
3 is approximately 3.32 × 103240. This part of the
computation lasted about 37 hours on a 2.8 GHZ Dual-Core AMD Opteron.
Let µ1, µ2, µ3 be as in the notation of Lemma 12.1. Using MAGMA we ﬁnd
µ1 = 2.677, µ2 = 2.612 and µ3 = 0.378 (to 3 decimal places). The shortest vector
of the ﬁnal lattice L is of Euclidean length approximately 1.156 × 101080 (it should
be no surprise that this is roughly the cube root of the index of L in Z
3). By
Lemma 12.1 if P ∈ C(Q) is not one of the 17 known rational points then

h((P )) ≥ 1.9 × 102159.

If P is an integral point, then h((P )) = log 2 + 2 log x(P ). Thus

log x(P ) ≥ 0.95 × 102159.

This contradicts the bounds for log x in Table 1 and shows that the integral point P
must be one of the 17 known rational points. This completes the proof of Theorem 1.
The proof of Theorem 2 is similar and we omit the details.
The reader can ﬁnd the MAGMA programs for verifying the above computations
at: http://www.warwick.ac.uk/staff/S.Siksek/progs/intpoint/

References

[1] `E. T. Avanesov, Solution of a problem on ﬁgurate numbers (Russian), Acta Arith. 12
(1966/1967), 409–420.
[2] A. Baker, Bounds for the solutions of the hyperelliptic equation, Proc. Cambridge Philos. Soc.
65 (1969), 439–444.
[3] Yu. Bilu, Eﬀective analysis of integral points on algebraic curves, Israel J. Math. 90 (1995),
235–252.
[4] Yu. F. Bilu and G. Hanrot, Solving superelliptic Diophantine equations by Baker’s method,
Compositio Mathematica 112 (1998), 273–312.
[5] W. Bosma, J. Cannon and C. Playoust: The Magma Algebra System I: The User Language,
J. Symb. Comp. 24 (1997), 235–265. (See also http://www.maths.usyd.edu.au/)
[6] B. Brindza, On S-integral solutions of the equation ym = f (x), Acta. Math. Hungar. 44
(1984), 133–139.
[7] B. Brindza, On a special superelliptic equation, Publ. Math. Debrecen 39 (1991), 159–162.
[8] N. Bruin, Chabauty methods and covering techniques applied to generalized Fermat equations,
Dissertation, University of Leiden, Leiden, 1999.
[9] N. Bruin, Chabauty methods using elliptic curves, J. reine angew. Math. 562 (2003), 27–49.

20 Y. BUGEAUD, M. MIGNOTTE, S. SIKSEK, M. STOLL, SZ. TENGELY

[10] N. Bruin and N. D. Elkies, Trinomials ax7 + bx + c and ax8 + bx + c with Galois groups of
order 168 and 8 · 168, pp. 172–188 of C. Fieker and D. R. Kohel (Eds.), Algorithmic Number
Theory, 5th International Symposium, ANTS-V, Lecture Notes in Computer Science 2369,
Springer-Verlag, 2002.
[11] N. Bruin and M. Stoll, Deciding existence of rational points on curves: an experiment,
Experiment. Math. 17, 181-189 (2008).
[12] N. Bruin and M. Stoll, Two-cover descent on hyperelliptic curves, arXiv:0803.2052v1
[math.NT].
[13] N. Bruin and M. Stoll, The Mordell–Weil sieve: proving the non-existence of rational points
on curves, in preparation.
[14] Y. Bugeaud, Bounds for the solutions of superelliptic equations, Compositio Math. 107
(1997), 187–219.
[15] Y. Bugeaud and K. Gy˝ory, Bounds for the solutions of unit equations, Acta Arith. 74 (1996),
67–80.
[16] Y. Bugeaud, M. Mignotte and S. Siksek, Classical and modular approaches to exponential
Diophantine equations I. Fibonacci and Lucas perfect powers, Annals of Math. 163 (2006), 969–
1018.
[17] J. W. S. Cassels and E. V. Flynn, Prolegomena to a middlebrow arithmetic of curves of genus
2, L.M.S. lecture notes series 230, Cambridge University Press, 1997.
[18] S. David, Minorations de formes lin´eaires de logarithmes elliptiques, M´em. Soc. Math. France
62 (1995).
[19] J.-H. Evertse and R. Tijdeman, Some open problems about Diophantine equations,
http://www.math.leidenuniv.nl/~evertse/07-workshop-problems.pdf
[20] D. C. Fielder and C. O. Alford, Observations from computer experiments on an integer
equation, in Applications of Fibonacci numbers 7 (Graz, 1996), pages 93–103, Kluwer Acad.
Publ. Dordrecht, 1998.
[21] U. Fincke and M. Pohst, Improved methods for calculating vectors of short length in a lattice,
including complexity analysis, Math. Comp. 44, 463–471, 1985.
[22] E. V. Flynn, A ﬂexible method for applying Chabauty’s Theorem, Compositio Math. 105
(1997), 79–94.
[23] E. V. Flynn, The Hasse principle and the Brauer-Manin obstruction for curves, Manuscripta
Math. 115 (2004), no. 4, 437–466.
[24] E. V. Flynn and N. P. Smart, Canonical heights on the Jacobians of curves of genus 2 and
the inﬁnite descent, Acta Arith. 79 (1997), no. 4, 333–352.
[25] E. V. Flynn and J. L. Wetherell, Finding rational points on bielliptic genus 2 curves,
Manuscripta Math. 100 (1999), no. 4, 519–533.
[26] E. V. Flynn and J. L. Wetherell, Covering collections and a challenge problem of Serre, Acta
Arith. 98 (2001), no. 2, 197–205.
[27] P. Kiss, On the number of solutions of the Diophantine equation (x
p) = (y
2)
, Fibonacci Quart.
26 (1988), 127–130.
[28] E. Landau, Verallgemeinerung eines P´olyaschen Satzes auf algebraische Zahlk¨orper, Nachr.
Kgl. Ges. Wiss. G¨ottingen, Math.-Phys. Kl. (1918), 478–488.
[29] D. A. Lind, The quadratic ﬁeld Q(
√5) and a certain Diophantine equation, Fibonacci Quart.
6 (1968), 86–93.
[30] E. M. Matveev, An explicit lower bound for a homogeneous rational linear form in logarithms
of algebraic numbers. II, Izv. Ross. Acad. Nauk Ser. Mat. 64 (2000), no. 6, 125–180; English
translation in Izv. Math. 64 (2000), no. 6, 1217–1269.
[31] M. Mignotte and A. Peth˝o, On the Diophantine equation xp − x = yq − y, Publ. Mat. 43
(1999), no. 1, 207–216.
[32] L. J. Mordell, On the integer solutions of y(y + 1) = x(x + 1)(x + 2), Paciﬁc J. Math. 13
(1963), 1347–1351.
[33] A. Peth˝o and B. M. M. de Weger, Products of prime powers in binary recurrence sequences
Part I: The hyperbolic case, with applications to the Generalized Ramanujan–Nagell equation,
Math. Comp. 47 (1987), 713–727.
[34] ´A. Pint´er, A note on the Diophantine equation (x
4) = (y
2)
, Publ. Math. Debrecen (1995) 47
(1995), 411–415.
[35] B. Poonen, Heuristics for the Brauer–Manin obstruction for curves, Experiment. Math. 15
(2006), no. 4, 415–420.
 21

[36] B. Poonen and E. F. Schaefer, Explicit descent on cyclic covers of the projective line, J. reine
angew. Math. 488 (1997), 141–188.
[37] D. Poulakis, Solutions enti`eres de l’´equation ym = f (x), S´em. Th´eor. Nombres Bordeaux 3
(1991), 187–199.
[38] E. F. Schaefer, 2–descent on the Jacobians of hyperelliptic curves, J. Number Theory 51
(1995), 219–232.
[39] W. M. Schmidt, Integer points on curves of genus 1, Compositio Math. 81 (1992), 33–59.
[40] J. H. Silverman, The Arithmetic of Elliptic Curves, GTM 106, Springer–Verlag, 1992.
[41] D. Singmaster, Repeated binomial coeﬃcients and Fibonacci numbers, Fibonacci Quart. 13
(1975), 295–298.
[42] N. P. Smart, The Algorithmic Resolution of Diophantine Equations, LMS Student Texts 41,
Cambridge University Press, 1998.
[43] V. G. Sprindˇzuk, The arithmetic structure of integer polynomials and class numbers, Trdu
Mat. Inst. Steklov LV (1977), 152–174.
[44] M. Stoll, On the height constant for curves of genus two, Acta Arith. 90 (1999), 183–201.
[45] M. Stoll, Implementing 2-descent for Jacobians of hyperelliptic curves, Acta Arith. 98 (2001),
245–277.
[46] M. Stoll, On the height constant for curves of genus two, II, Acta Arith. 104 (2002), 165–182.
[47] M. Stoll, Finite descent obstructions and rational points on curves, Algebra & Number The-
ory 1 (2007), 349–391.
[48] R. J. Stroeker and N. Tzanakis, Computing all integer solutions of a genus 1 equation, Math.
Comp. 72 (2003), no. 244, 1917–1933
[49] R. J. Stroeker and B. M. M. de Weger, Elliptic binomial Diophantine equations, Math. Comp.
68 (1999), 1257–1281.
[50] P. M. Voutier, An upper bound for the size of integral solutions to Y m = f (X), J. Number
Theory 53 (1995), no. 2, 247–271.
[51] P. M. Voutier, An eﬀective lower bound for the height of algebraic numbers, Acta Arith.
LXXIV.1 (1996), 81–95.
[52] B. M. M. de Weger, A binomial Diophantine equation, Quart. J. Math. Oxford Ser. (2), 186
(1996), 221–231.
[53] B. M. M. de Weger, Equal binomial coeﬃcients: some elementary considerations, J. Number
Theory, 63 (1997), 373–386.
[54] J. L. Wetherell, Bounding the Number of Rational Points on Certain Curves of High Rank,
Ph.D. dissertation, University of California at Berkeley, 1997.

Yann Bugeaud and Maurice Mignotte, Universit´e Louis Pasteur, U. F. R. de math´ematiques,
7, rue Ren´e Descartes, 67084 Strasbourg Cedex, France
E-mail address: bugeaud@math.u-strasbg.fr
E-mail address: mignotte@math.u-strasbg.fr

Samir Siksek, Institute of Mathematics, University of Warwick, Coventry, CV4 7AL,
United Kingdom
E-mail address: s.siksek@warwick.ac.uk

Michael Stoll, Mathematisches Institut, Universit¨at Bayreuth, 95440 Bayreuth,
Germany
E-mail address: Michael.Stoll@uni-bayreuth.de

Szabolcs Tengely, Institute of Mathematics, University of Debrecen and the Num-
ber Theory Research Group of the Hungarian Academy of Sciences, P.O.Box 12, 4010
Debrecen, Hungary
E-mail address: tengely@math.klte.hu
