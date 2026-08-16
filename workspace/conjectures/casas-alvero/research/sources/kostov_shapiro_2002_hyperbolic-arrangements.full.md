<!-- source: https://arxiv.org/pdf/math/0204272 | converted from PDF -->

arXiv:math/0204272v2  [math.AG]  16 Feb 2003
On arrangements of real roots of a real polynomial and its
derivatives

Vladimir Petrov Kostov

To Prof. A.A.Bolibrukh

Abstract

We prove that all arrangements (consistent with the Rolle theorem and some other natural
restrictions) of the real roots of a real polynomial and of its s-th derivative are realizable by
real polynomials.
Key words: arrangement of roots
AMS classiﬁcation: 12D10

In the present paper we consider a real polynomial of one real variable P (x, a) = xn +
a1xn−2 + . . . + an−1. We are interested in the question what arrangements between the real
roots of P and P (s) are possible (1 ≤ s ≤ n − 1). To deﬁne an arrangement means to write down
the roots of P and P (s) in a chain in which every two consecutive roots are connected either by
an equality or by an inequality <. The arrangement α is said to belong to the closure of the
arrangement β if it is obtained from β by replacing some inequalities by equalitites. The results
are the ﬁrst step towards the study of real discriminant sets {a ∈ Rn−1|Res(P, P (s)) = 0}.
In an earlier paper [KoSh] it is shown that if P is hyperbolic, i.e. with n real roots, then the
standard Rolle restrictions are necessary and suﬃcient conditions for a root arrangement to be
realizable (see Theorems 2 and 4.4 in [KoSh]). Namely, denote by x1 ≤ . . . ≤ xn the roots of P
and by ξ1 ≤ . . . ≤ ξn−s the ones of P (s) (which is also hyperbolic). Then one has

xl ≤ ξl ≤ xl+s (1)

for l = 1, . . . , n − s and every arrangement of the roots of P and P (s) which is consistent with
(1) is realizable. One presumes also that the following conditions hold:
A) If a root of P of multiplicity d > s coincides with a root of P (s) of multiplicity g, then
g = d − s (self-evident).
B) If a root ξ of P (s) coincides with a root of P of multiplicity κ ≤ s, then ξ is a simple root
of P (s) (see [KoSh], Lemma 4.2) and one has κ ≤ s − 1.
C) If xl = ξl or xl+s = ξl, then xl = xl+1 = . . . = xl+s = ξl (self-evident for s = 1 and easy
to prove by induction on s for s > 1).

Example 1 If n = 2, s = 1, then there are two possible arrangements (i.e. consistent with
(1), A) B) and C)) : x1 < ξ1 < x2 and x1 = ξ1 = x2. They are both realizable by hyperbolic
polynomials.

In the present paper we treat the case when P is arbitrary (not necessarily hyperbolic).
(Notice that P (s) can be hyperbolic even if P is not.)

1

Deﬁnition 2 Suppose that P has m conjugate couples of complex roots and n − 2m real roots.
Then a priori P (s) has at least n − 2m − s real roots counted with the multiplicities. Indeed, a
real root of P (i) of multiplicity l ≥ 1 is a root of P (i+1) of multiplicity l − 1 and between every two
real roots of P (i) there is a root of P (i+1). Iterating this rule s times one obtains the existence
of n − 2m − s real roots of P (s) (we call them Rolle roots) which together with the real roots of
P satisfy conditions (1), A) and B). A Rolle root is multiple only if it coincides with a root of
P of multiplicity > s. Eventually, P (s) can have ≤ 2m other (non-Rolle) real roots counted with
the multiplicities some (or all) of which can coincide with Rolle ones. Which real roots of P (s)

should be chosen as Rolle and which as non-Rolle ones is not always uniquely deﬁned and when
it is not we assume that a choice is made.

Example 3 The polynomial x6 − x2 = x2(x2 − 1)(x2 + 1) has real roots x1 = −1, x2 = x3 = 0,
x4 = 1 (and complex roots ±i). One has P ′ = 6x5 − 2x = 2x(
√3x2 − 1)(
√3x2 + 1), i.e. P ′

has three Rolle roots (and no non-Rolle ones) – 0 and ±1/31/4 where 0 is a common root for P
and P ′, see A). It has also two complex roots ±i/31/4. One has P ′′ = 30x4 − 2, i.e. P ′′ has two
Rolle roots ±1/151/4, no non-Rolle ones and two complex roots ±i/151/4. One has P ′′′ = 120x3,
i. e. P ′′′ has a triple real root at 0 and no complex roots. One copy of this real root should be
considered as a Rolle one and the other two as non-Rolle ones.

Proposition 4 Suppose that a real root of P of multiplicity d coincides with a real root of P (s)

of multiplicity g. Then
1) if d > s, then one has g = d − s; in this case this is a Rolle root of P (s) of multiplicity
d − s;
2) if 0 ≤ d ≤ s, then one has g ≤ 2m + 1 (and if g ≥ 1, then d < s).

Observe that in the above example one has m = 1 and for s = 3 the estimation 2m + 1 is
attained by the multiplicity of 0 as a root of P ′′′. The proposition generalizes conditions A) and
B) in the case of arbitrary m.
Proof:
Part 1) is self-evident. Prove part 2). If the root is non-Rolle and does not coincide with
a Rolle one, then its multiplicity is ≤ 2m. If the root is Rolle and does not coincide with a
non-Rolle one, then either it coincides with a root of P of multiplicity > s and we are in case 1)
or it is a simple root. Finally, if the root is Rolle and coincides with a non-Rolle one, then the
Rolle root must be simple (otherwise there will be a contradiction with part 1)) and the sum of
their two multiplicities is ≤ 2m + 1. ✷

Deﬁnition 5 An arrangement of the real roots of P and P (s) is called a priori admissible if
there exist n − 2m − s Rolle roots of P (s) in the sense of Deﬁnition 2 and if conditions 1) and
2) of Proposition 4 hold.

Theorem 6 All a priori admissible root arrangements are realizable by real polynomials of de-
gree n.

Proof:
10. We explain ﬁrst in 10 – 70 why all a priori admissible arrangements in which the derivative
P (s) is hyperbolic and which are the least generic are realizable. ”Least generic” means that all
non-Rolle roots of P (s) coincide with Rolle ones or with roots of P . The general case is treated
in 80 – 110.
To realize an a priori admissible arrangement with P (s) hyperbolic and with the necessary
multiplicities of the real roots of P consider the family of polynomials

2

P (x, w, g, t) =
 q∏

j=1
(x − wj)
mj m∏

j=1
((x − gj)
2 + t2
j ) (2)

where wj, j = 1, . . . , q, are the real roots of P , of multiplicities mj (w0 = 0 ≤ w1 ≤ . . . ≤ wq ≤
1 = wq+1), and gj ± itj are its complex roots (not necessarily distinct), tj ≥ 0, 0 ≤ gj ≤ 1. We
allow here equalities between the roots wj for convenience; it will be shown that the necessary
arrangement is realizable for roots with strict inequalities between them.
Denote by ξ1 ≤ . . . ≤ ξn−s the real parts of the roots of P (s) (n − 2m − s of them are just
Rolle roots) and by θ1 ≤ . . . ≤ θm the biggest nonnegative imaginary parts of the roots of P (s)

(recall that for a least generic arrangement one has θj = 0). Set ξ0 = 0, ξn−s+1 = 1. (Notice
that P (s) has not more conjugate couples of complex roots than P , i.e. not more than m.) The
functions ξi, θj are continuous in (w, g, t).
20. Suppose that for the desired arrangement of the real roots of P and P (s) the Rolle
and non-Rolle roots of P (s) are ﬁxed. Denote the non-Rolle roots by u1 ≤ . . . ≤ u2m. Impose
additional requirements upon the numbers gj as follows: if the non-Rolle roots with odd indices
u2p−1, u2p+1, . . . , u2p+2p′−1 belong to the interval [wj, wj+1), j < q, or to [wq, wq+1], then we
require that wj ≤ gp ≤ . . . ≤ gp+p′ ≤ wj+1. Deﬁne the variables h1 ≤ . . . ≤ hq+m as the union
of the variables wj (j = 1, . . . , q) and gi (i = 1, . . . , m) with the order deﬁned above. Hence,
they belong to the unit simplex Σq+m.
30. In what follows we assume that the variables tj belong to some interval [0, N ] where
N > 1. We deﬁne with the help of the variables hj, ti continuous functions ηj, ζi such that
(η1, . . . , ηq+m) ∈ Σq+m, ζi ∈ [0, N ]. The set S = Σq+m × [0, N ]m is homeomorphic to Σq+2m.
By the Brouwer ﬁxed point theorem (see [Do], p. 57), there exists a ﬁxed point of the mapping
τ : S → S, τ : (h, t) ↦→ (η, ζ), i.e. a point where one has ηj = hj, ζi = ti. The functions ηj, ζi
are deﬁned such that the arrangement of the real roots of P and P (s) at the ﬁxed point is the
required one.
40. Deﬁne the functions ηj by the following rules:
1) We want to achieve the additional conditions (at the ﬁxed point) gp = u2p−1, . . ., gp+p′ =
u2p+2p′−1 for all appropriate indices, see 20; therefore we set ηi1 = ξi2 whenever hi1 is a variable
gp+l and ξi2 is the corresponding function u2p+2l−1;
2) If a variable hj, which is a root wi of multiplicity < s + 1, must coincide with a simple
root ξk of P (s) or, more generally, with the roots ξk = ξk+1 = . . . = ξk+l, then we set ηj = ξk;
3) If the variables hr < hr+1 < . . . < hr+l (which are all consecutive roots wj and among
which there might be roots wj of multiplicity ≥ s + 1) lie between the Rolle roots ξk and
ξk+v of P (s) and all roots among the roots ξk+1, . . ., ξk+v−1 (if v > 1) coincide with roots wj
(r ≤ j ≤ r + l) of multiplicity ≥ s + 1, then we set
ηr+j = ξk + (j + 1)(ξk+v − ξk)/(l + 2), j = 0, 1, . . . , l.

Remark 7 It follows from rules 1) – 3) that there are q + m functions ηj – as many as the
variables hj.

Recall that the arrangement is least generic, i.e. for every non-Rolle root ξi of P (s) one has
either ξi = ξi1 where ξi1 is a Rolle one or ξi = wi2 = hj for some i2, j. Denote by l1, . . ., l2m the
absolute values |ξi − ξi1| and |ξi − wi2| for all i, i1 and i2 as above. Set Φ = l1 + . . . + l2m and

ζi =
 ∣
∣
∣
∣
∣
∣ti − 1
3m
 m∑

j=1 θj − ti
3(N + 1)m |t1t2 . . . tm − 1| − ti
12m Φ
∣
∣
∣
∣
∣
∣ (3)

3

50. Denote by ti0 the greatest variable ti at the ﬁxed point (see 30). Observe ﬁrst that one
can assume that ti0 > 0. Indeed, if ti0 = 0, then ti = 0 for all i, P is hyperbolic and the roots
of P and P (s) deﬁne an arrangement α from the closure of the desired least generic one β.

Lemma 8 If ti0 = 0, then there exists a real-analytic deformation of P into a real polynomial
which together with its s-th derivative deﬁnes the arrangement β.

The lemma is proved after the theorem. It allows one to consider only the case ti0 > 0.
60. One has
 ζi0 = ti0 − 1
3m
 m∑

j=1 θj − ti0
3(N + 1)m |t1t2 . . . tm − 1| − ti0
12m Φ .

Indeed, all roots of P (s) lie within the convex hull of all roots of P (see [PoSz], p. 108). Hence,
one has θj ≤ ti0, j = 1, . . . , m. One has also |t1t2 . . . tm − 1| ≤ t1t2 . . . tm + 1 < (N + 1)m and
Φ ≤ 4m (because for each term lj one has lj ≤ 2). Thus

1
3m
 m∑

j=1 θj + ti0
3(N + 1)m |t1t2 . . . tm − 1| + ti0
12m Φ < mti0/3m + ti0/3 + 4mti0/12m = ti0 (4)

and for i = i0 one can delete the absolute value sign in the right hand-side of (3). But then to
have ζi0 = ti0 one must have θj = 0 for j = 1, . . . , m, t1t2 . . . tm − 1 = 0 and l1 = . . . = l2m = 0.
This means that tj ̸= 0, i.e. no root gj + itj of P will be real, that P (s) will indeed be hyperbolic
(θj = 0) and that all non-Rolle roots of P (s) equal either roots wj of P or Rolle roots of P (s).

Remark 9 The condition N > 1 makes possible the choice of the values of the variables ti so
that t1t2 . . . tm − 1 = 0. One can prove by analogy with (4) that |ζi| < N , i.e. the mapping τ is
indeed from S into itself.

70. A priori the ﬁxed point assures the existence of an arrangement only from the closure of
the necessary one. The fact that at the ﬁxed point no inequality between roots of P is replaced
by equality is proved by analogy with 40 – 70 of the proof of Theorem 4.4 from [KoSh] where the
case of P hyperbolic is considered. The proof there shows that equalities replacing inequalities
between roots of P imply that a root of P of multiplicity m ≥ s+1 is a root of P (s) of multiplicity
≥ m − s + 1 which contradicts part 1) of Proposition 4. In the general case (P not necessarily
hyperbolic) the proof is essentially the same, the presence of eventual non-Rolle roots can only
increase the multiplicity of the root as a root of P (s).
Hence, the ﬁxed point provides the necessary arrangement.
80. To obtain (in 80 – 90) all arrangements in which P (s) is hyperbolic but which are not
necessarily least generic we use the same construction but with another function Φ. Namely,
consider a family of such functions Φ depending on a parameter b ∈ (R+, 0) deﬁned as follows:
if instead of ξi − ξi1 = 0, see 40, one must have ξi − ξi1 > 0 or ξi − ξi1 < 0 (and no root ξj or wj
lies between ξi and ξi1), then in Φ we replace the absolute value lν = |ξi − ξi1| by |ξi − ξi1 − b|
(resp. by |ξi − ξi1 + b|); in the same way for ξi − wi2, see 40. In a sense, we obtain the not least
generic arrangements by deforming least generic ones the deformation parameter being b.
90. Denote by F (b) the set of ﬁxed points of the mapping τ from 30. For b small enough
one has (η, ζ) ∈ S. The set F (0) contains all limit points of the family of sets F (b) when b → 0
and there exists at least one such limit point because all sets F (b) (for b small enough) are

4

non-empty and belong to S which is compact. Hence, one can choose b > 0 small enough and
a ﬁxed point of F (b) at which there is an inequality between two roots in the arrangement if
there is an inequality in the arrangement for b = 0, and the equalities ξi − ξi1 = 0 or ξi − wi2 = 0
where this is necessary are replaced by the desired inequalities.
100. Obtain all arrangements in which P (s) is not hyperbolic and which are least generic.
Suppose that P (s) must have exactly m′ conjugate couples of complex roots. In this case we
assume that m′ of the couples of roots gj ± itj are replaced by a couple ±iv where v > 0 is
“large”, i.e. much bigger than N . Hence, P (s) also has exactly m′ couples of conjugate complex
roots with “large” imaginary parts. One has

Q := P/v2m′ = (1 + x2/v2)
m′ q∏

j=1
(x − wj)
mj m−m′
∏

j=1 ((x − gj)
2 + t2
j ) ,

i.e. the family Q is a one-parameter deformation of a family of polynomials like (2) (the role
of the small parameter is played by 1/v2) and the existence of the necessary arrangements can
be deduced by analogy with 10 – 70 (see 90 for the role of the small parameter; however, the
function Φ is the one from 10 – 70).
110. To obtain the existence of all arrangements (which are not necessarily least generic
and with P (s) not necessarily hyperbolic) one has to combine 80, 90 and 100. The theorem is
proved. ✷
Proof of Lemma 8:
10. We assume that P has the same number of distinct real roots as in the desired arrange-
ment β. If not, then one can ﬁrst deform P within the class of hyperbolic polynomials (while
remaining in the closure of β) to achieve this condition. See [Ko] for such deformations.
We begin with two observations:
1) for a > 0, µ ∈ N ∪ {0} and ν even the polynomial Q = xµ(xν + a) has a µ-fold root for
x = 0 and its s-th derivative for s > µ has a (µ + ν − s)-fold one; Q has also ν/2 couples of
conjugate complex roots;
2) with a, µ and ν as above, the polynomial Q1 = xµ(xν + a + aQ2(x, a)) where Q2 is a
polynomial in x of degree ≤ ν −1, Q2(0, a) ≡ 0, has ν complex zeros for a small enough and a real
µ-fold root at 0; to see this set a = cν, x = cy; one has Q1(cy, cν ) = cµ+νyµ(yν + 1 + Q2(cy, cν ));
the last polynomial has a µ-fold root at 0 and ν roots which for c small enough are close to the
roots of yν + 1, hence, are complex.
20. Suppose that the polynomial P of degree n realizing with P (s) the arrangement α has
a real root of multiplicity µ + ν (with ν even) which (in order to obtain the arrangement β)
must split into ν/2 couples of conjugate complex roots and into a real root of multiplicity µ. (If
several roots of P must split, we make them split one by one.) Suppose in addition that in the
deformed polynomial (denoted by R) the real root of multiplicity µ must coincide with a root
of R(s) of multiplicity µ + ν − s. Assume that the bifurcating root is at 0 and that

P = xµ+ν (1 + h(x)) , h(0) = 0 (5)

(P is not necessarily monic). Construct the necessary deformation of P in the form

R(x, a) = xµ(xν + a + bs−µxs−µ + . . . + bν−1xν−1)(1 + g(x, a)) (6)

where a ∈ (R, 0) and bi = bi(a) and g(x, a) (g(0, a) ≡ 0) are deﬁned such that all equalities of
the form xi = ξj deﬁning the arrangement β will be preserved.
30. Suppose ﬁrst that in (6) one has g(x, a) ≡ h(x). The condition

5

(A) : R(s) has a (µ + ν − s)−fold root at 0

is a triangular linear non-homogeneous system with unknown variables bi; the system deﬁnes
unique functions bi = b∗
i a, b∗
i ∈ R. This can be checked directly.
Suppose that in (6) one has g = h(x) + ∑l
j=1 djhj(x, d) where d = (d1, . . . , dl) ∈ (Rl, 0)
and hj depend smoothly on d. Then condition (A) deﬁnes unique functions bi(a, d) = b∗
i a +
a ∑l
j=1 dj˜bi,j(d) where b∗
i ∈ R and ˜bi,j are smooth in d. This can also be checked directly.
40. For each root wj ̸= 0 of P of multiplicity < s which must be equal to a root ξi of P (s)

denote by dj the deviation from its position in a deformation of P . Admitting such deviations
means that in (5) the function h should be replaced by h(x) + ∑l
j=1 djhj(x, d).
Denote by (B) the system of all conditions wj = ξi for all such equalities with wj ̸= 0
characterizing the arrangement β.
50. For any deformation R∗(x, a, d) = xµ(xν + a + bs−µxs−µ + . . . + bν−1xν−1)(1 + g(x, d)) of
P (where bk are considered as small parameters) one can ﬁnd d depending smoothly on a and bk
such that for all a small enough all equalities from (B) hold. This follows from Propositions 11
and 13 from [Ko] where it is shown that the linearizations of the conditions (B) w.r.t. d are
linearly independent. (In [Ko] their linear independence is proved only when P is hyperbolic;
this independence is an “open” property, so it holds for all nearby polynomials as well.)
60. The independence of these linearizations implies that for a small enough the system of
conditions (B) applied to the deformation

˜R(x, a, d) = xµ(xν + a + bs−µ(a, d)xs−µ + . . . + bν−1(a, d)xν−1)(1 + h(x) +
 l∑

j=1 djhj(x, d))

(with bi(a, d) deﬁned as in 30) deﬁnes unique dj = dj(a) smooth in a. Indeed, the linearizations
w.r.t. d of the system of conditions (B) from 60 and from 50 are the same.
On the other hand, bi were deﬁned such that condition (A) holds. Hence, for d = d(a) and
bi = bi(a, d(a)) (where a > 0 is small enough) the (µ + ν)-fold root of P at 0 splits into a real
µ-fold root at 0 and ν complex roots close to 0 (see observation 2) from 10) and P (s) has a
(µ + ν − s)-fold root at 0. The arrangement of the other real roots of P and P (s) remains the
same. ✷
Acknowledgement. The present text is written under the impetus of the fruitful discus-
sions with B.Z. Shapiro, the author’s host during a short visit at the University of Stockholm.
The author thanks both him and his university for the kind hospitality.

References

[Do] Albrecht Dold, Lectures on algebraic topology, Classics in Mathematics, Springer
(1980).

[Ko] Vladimir Petrov Kostov, On arrangements of the roots of a hyperbolic polynomial
and of one of its derivatives. Electronic preprint math.AG/0211132.

[KoSh] Vladimir Petrov Kostov, Boris Zalmanovich Shapiro, On arrangements of roots for a
real hyperbolic polynomial and its derivatives. Bull. Sci. Math. 126 (2002) 45-60.

[PoSz] G. Polya and G. Szeg¨o, Problems and theorems in analysis vol. 1, Springer-Verlag
(1972).
 6

Author’s address: Universit´e de Nice, Laboratoire de Math´ematiques, Parc Valrose, 06108
Nice Cedex 2, France. e-mail: kostov@math.unice.fr

7
