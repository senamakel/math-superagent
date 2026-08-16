<!-- source: https://arxiv.org/pdf/1702.08216 | converted from PDF -->

arXiv:1702.08216v1  [math.CA]  27 Feb 2017
On higher-order discriminants

Vladimir Petrov Kostov
Universit´e Cˆote d’Azur, CNRS, LJAD, France
e-mail: kostov@math.unice.fr

Abstract

For the family of polynomials in one variable P := x
n + a1x
n−1 + · · · + an, n ≥ 4, we con-
sider its higher-order discriminant sets { ˜Dm = 0}, where ˜Dm :=Res(P, P (m)), m = 2, . . ., n−
2, and their projections in the spaces of the variables ak := (a1, . . . , ak−1, ak+1, . . . , an). Set
P (m) := ∑n−m
j=0 cjajx
n−m−j, Pm,k := ckP −x
mP (m). We show that Res( ˜Dm, ∂ ˜Dm/∂ak, ak) =
Am,kBm,kC2
m,k, where Am,k = an−m−k
n , Bm,k =Res(Pm,k, P ′
m,k) if 1 ≤ k ≤ n − m and
Am,k = an−k
n−m, Bm,k =Res(P (m), P (m+1)) if n − m + 1 ≤ k ≤ n. The equation Cm,k = 0
deﬁnes the projection in the space of the variables ak of the closure of the set of values of
(a1, . . . , an) for which P and P (m) have two distinct roots in common. The polynomials
Bm,k, Cm,k ∈ C[ak] are irreducible. The result is generalized to the case when P (m) is re-
placed by a polynomial P∗ := ∑n−m
j=0 bjajx
n−m−j, 0 ̸= bi ̸= bj ̸= 0 for i ̸= j.

AMS classiﬁcation: 12E05; 12D05

Key words: polynomial in one variable; discriminant set; resultant; multiple root

1 Introduction

In this paper we consider for n ≥ 4 the general family of monic polynomials in one variable
P (x, a) := xn + a1xn−1 + · · · + an, x, aj ∈ C. For its mth derivative w.r.t. x we set P (m) :=
c0xn−m + c1a1xn−m−1 + · · · + cn−man−m, where cj = (n − j)!/(n − m − j)!. For m = 1, . . ., n − 1
we deﬁne the mth order discriminant of P as ˜Dm :=Res(P, P (m)) which is the determinant of
the Sylvester matrix S(P, P (m)). We remind that S(P, P (m)) is (2n − m) × (2n − m), its ﬁrst
(resp. (n − m + 1)st) row equals

(1, a1, . . . , an, 0, . . . , 0) (resp. (c0, c1a1, . . . , cn−man−m, 0, . . . , 0) ) ,

the second (resp. (n − m + 2)nd) row is obtained from this one by shifting by one position to
the right and by adding 0 to the left etc. We say that the variable aj is of quasi-homogeneous
weight j because up to a sign it equals the jth elementary symmetric polynomial in the roots of
the polynomial P ; the quasi-homogeneous weight of x is 1.
There are at least two problems in which such discriminants are of interest. One of them is
the Casas-Alvero conjecture that if a complex univariate polynomial has a root in common with
each of its nonconstant derivatives, then it is a power of a linear polynomial, see [2], [16] and
[17] and the claim in [15] that the answer to the conjecture is positive.
Another one is the study of the possible arrangements of the roots of a hyperbolic polynomial
(i.e. real and with all roots real) and of all its nonconstant derivatives on the real line. This
problem can be generalized to a class of polynomial-like functions characterized by the property
their nth derivative to vanish nowhere. It turns out that for this class Rolle’s theorem gives only

1

necessary, but not suﬃcient conditions for realizability of a given arrangement by the zeros of a
polynomial-like function, see [9], [10], [11] and [12]. Pictures of discriminants for the cases n = 4
and n = 5 can be found in [6]. Properties of the discriminant set { ˜D1 = 0} for real polynomials
are proved in [14].
A closely related question to the one of the arrangement of the roots of a hyperbolic poly-
nomial is the one to study overdetermined strata in the space of the coeﬃcients of the family of
polynomials P (the deﬁnition is given by B. Z. Shapiro in [13]); these are sets of values of the
coeﬃcients for which there are more equalities between roots of the polynomial and its deriva-
tives than expected. Example: the family of polynomials x4 + ax3 + bx2 + cx + d depends on 4
parameters two of which can be eliminated by shifting and rescaling the variable x which gives
(up to a nonzero constant factor) the family S := x4 − x2 + cx + d. For c = 0, d = 1/2 the
polynomial has two double roots ±1/
√2, and 0 is a common root for S′ and S′′′. This makes
three independent equalities, i.e. more than the number of parameters. For polynomials of small
degree, overdetermined strata have been studied in [3] and [4]. The study of overdetermined
strata is interesting both in the case of complex and in the case of real coeﬃcients.
In what follows we enlarge the context by considering instead of the couple of polynomials
(P, P (m)) the couple (P, P∗), where P∗ := ∑n−m
j=0 bjajxn−m−j, bj ̸= 0 and bi ̸= bj for i ̸= j. By
abuse of notation we set ˜Dm :=Res(P, P∗).

Proposition 1. The polynomial ˜Dm is irreducible. It is a degree n polynomial in each of the
variables aj, j = 1, . . ., n − m, and a degree n − m polynomial in each of the variables aj,
j = n − m + 1, . . ., n. It contains monomials Mj := ±bn
j an
j (1 − b0/bj)jan−m−j
n , j = 1, . . .,
n − m, and Ns := ±bm−s
n−ma
m−s
n−mbn−m+s
0 an−m
n−m+s, s = 1, . . ., m − 1. It is quasi-homogeneous,
of quasi-homogeneous weight n(n − m). The monomial Mj (resp. Ns) is the only monomial
containing an
j (resp. an−m
n−m+s).

Proof. We prove ﬁrst the presence in ˜Dm of the monomials Mj and Ns. For each j ﬁxed,
1 ≤ j ≤ n − m, one can subtract the (n − m + ν)th row of S(P, P∗) multiplied by 1/bj from its
νth one, ν = 1, . . ., n − m. We denote by T the new matrix. One has det T = det S(P, P∗) and
the variable aj is not present in the ﬁrst n − m rows of T . Thus there remains a single term of
det T containing n factors aj; it is obtained when the entries bjaj in positions (n − m + µ, j + µ)
of T , µ = 1, . . ., n, are multiplied by the entries an in positions (ℓ, n + ℓ), ℓ = j + 1, . . ., n − m,
and by the entries 1 − b0/bj in positions (ℓ, ℓ), ℓ = 1, . . ., j; this gives the monomial Mj. (If
when computing det S(P, P∗) one chooses to multiply the n entries bjaj, then they must be
multiplied by entries of the matrix obtained from S(P, P∗) by deleting the rows and columns
of the entries bjaj. This matrix is block-diagonal, its upper left block is upper-triangular, with
diagonal entries equal to 1 − b0/bj, its right lower block is lower-diagonal, with diagonal entries
equal to an. Hence Mj is the only monomial containing n factors aj.)
To obtain the monomial Ns one chooses in the deﬁnition of T above j = n − m. Hence
the ﬁrst n − m rows of T do not contain the variable an−m. The monomial Ns is obtained by
multiplying the entries an−m+s in positions (r, n − m + s + r), r = 1, . . ., n − m, by the entries
bn−man−m in positions (q, q), q = 2n − 2m + s + 1, . . ., 2n − m and by the entries b0 in positions
(n − m + p, p), p = 1, . . ., n − m + s. The monomial Ns is the only one containing n − m factors
an−m+s (proved by analogy with the similar claim about the monomial Mj).
The matrix S(P, P∗) contains each of the variables aj, j = 1, . . ., n−m (resp. as, s = n−m+1,
. . ., n) in exactly n (resp. n − m) of its columns. The presence of the monomials Mj (resp. Ns)
in ˜Dm shows that ˜Dm is a degree n polynomial in the variables aj and a degree n − m one in
the variables as.
 2

Quasi-homogeneity of ˜Dm follows from the fact that its zero set and the zero sets of the
polynomials P and P∗ remain invariant under the quasi-homogeneous dilatations x ↦→ tx, aκ ↦→
tκaκ, κ = 1, . . ., n. Each of the monomials Mj and Ns is of quasi-homogeneous weight n(n − m).
Irreducibility of ˜Dm results from the impossibility to present simultaneously all monomials
Mj and Ns as products of two monomials, of quasi-homogeneous weights u and n(n − m) − u,
for any 1 ≤ u ≤ n(n − m) − 1.

Notation 2. For Q, R ∈ C[x] we denote by Res(Q, R) the resultant of Q and R and we write
P (m) for dmP/dxm. This refers also to the case when the coeﬃcients of Q and R depend on
parameters. We set a := (a1, . . . , an) (resp. aj = (a1, . . . , aj−1, aj+1, . . . , an)) and we denote
by A ≃ Cn (resp. Aj ≃ Cn−1) the space of the variables a (resp. aj). For K, L ∈ C[a] we
write S(K, L, ak) and Res(K, L, ak) for the Sylvester matrix and the resultant of K and L when
considered as polynomials in ak. We set ˜Dm,k :=Res( ˜Dm, ∂ ˜Dm/∂ak, ak). For a matrix A we
denote by Ak,ℓ its entry in position (k, ℓ) and by [A]k,ℓ the matrix obtained from A by deleting
its kth row and ℓth column. By Ω (indexed, with accent or not) we denote throughout the paper
nonspeciﬁed nonzero constants. By Pm,k (1 ≤ k ≤ n−m) we denote the polynomial bkP −xmP∗;
its coeﬃcients of xn and xk equal bk − b0 ̸= 0 and 0.

Deﬁnition 3. For 1 ≤ m ≤ n − 2 we denote by Θ and ˜M the subsets of the hypersurface
{ ˜Dm = 0} ⊂ A such that for a ∈ Θ (resp. for a ∈ ˜M ) the polynomial P has a root which is
a double root of P∗ (resp. the polynomials P and P∗ have two simple roots in common). The
remaining roots of P and P∗ are presumed simple and mutually distinct. We call the set ˜M the
Maxwell stratum of { ˜Dm = 0}.

In the present paper we prove the following theorem;

Theorem 4. Suppose that 2 ≤ m ≤ n − 2. Then:
(1) The polynomial ˜Dm,k can be represented in the form

˜Dm,k = Am,kBm,kC 2
m,k , (1)

where Am,k = an−m−k
n if k = 1, . . ., n − m, and Am,k = an−k
n−m if k = n − m + 1, . . ., n, Bm,k
and Cm,k are irreducible polynomials in the variables ak.
(2) One has Bm,k =Res(Pm,k, P ′
m,k) if k = 1, . . ., n − m, and Bm,k =Res(P∗, P ′
∗) if k =
n − m + 1, . . ., n.
(3) The equation Cm,k = 0 deﬁnes the projection in the space Ak of the closure of the Maxwell
stratum.

The paper is structured as follows. After some examples and remarks in Section 2, we justify
in Section 3 the form of the factor Am,k, see Proposition 9; Section 3 begins with Lemma 8 which
gives the form of the determinant of certain matrices that appear in the proof of Theorem 4.
Section 4 contains Lemma 12 and Statements 13, 14 and 15 (the latter claims that the factors
Bm,k and Cm,k are irreducible). They imply that one has ˜Dm,k = Am,kBsm,k
m,k C rm,k
m,k , where sm,k,
rm,k ∈ N, see Remark 17. Thus after Section 4 there remains to show only that sm,k = 1 and
rm,k = 2. In Section 5 we prove Theorem 4 in the case m = n − 2, see Proposition 18. In
Section 6 we show that sm,k = 1. We ﬁnish the proof of Theorem 4 in Section 7, by induction on
n and m, as follows. Statement 24 deduces formula (1) for n = n0 + 1, k = k0 + 1 from formula
(1) for n = n0, k = k0. Statement 25 justiﬁes formula (1) for n = n0, 2 ≤ m < n0 − 2, k = 1
using formula (1) for n = n0, m = n0 − 2, k = 1 (recall that the latter is justiﬁed in Section 5).
Acknowledgement. The author is deeply grateful to B. Z. Shapiro from the University
of Stockholm for having pointed out to him the importance to study discriminants and for the
fruitful discussions of this subject.
 3

2 Examples and remarks

Although Theorem 4 speaks about the case 2 ≤ m ≤ n − 2, our ﬁrst example treats the case
m = 1 in order to show its diﬀerences with the case 2 ≤ m ≤ n − 2:

Example 5. For n = 3, m = 1 we set P := x3 +ax2 +bx+c, P∗ := x2 +Aax+Bb, 0 ̸= A, B ̸= 1,
A ̸= B. Then

˜D1 = (1 − A)B(B − A)a2b2 + (3AB − A − 2B)abc + c2 + A2(1 − A)a3c + B(1 − B)2b3

˜D1,1 = −A2(A − 1)2 c (−27A2(1 − A)c2 + 4(A − B)3b3) (−Ac2 + (1 − A)B2(1 − B)b3)2

˜D1,2 = −B2(B − 1)2 c (−27B(1 − B)2c + 4(A − B)3a3) (−(1 − B)c + A(1 − A)2Ba3)2

˜D1,3 = −(−4Bb + A2a2) ((1 − B)b − A(1 − A)a2)2 .

The condition P and P∗ to have two roots in common is tantamount to P∗ dividing P . One has
P = (x + a(1 − A))P∗ + W1x + W0, where

W1 := (1 − B)b − A(1 − A)a2 , W0 := c − B(1 − A)ab .

The quadratic factors in the above presentations of ˜D1,k, k = 1, 2 and 3, are obtained by
eliminating respectively a, b and c from the system of equations W1 = W0 = 0 which is the
necessary and suﬃcient condition P∗ to divide P .
In the particular case A = 2/3, B = 1/3 (i.e. P∗ = P ′/3) one obtains

˜D1,1 = (−2
6/3
15) c (−27c
2 +b3)
3 , ˜D1,2 = (−2
6/3
15) c (−27c+a3)
3 , ˜D1,3 = (2
4/3
6) (3b−a2)
3 .

Remarks 6. (1) For n ≥ 4, m = 1 and P∗ = P ′ a result similar to Theorem 4 holds true.
Namely, if n ≥ 4, then ˜D1,k is of the form A1,kB3
1,kC 2
1,k, where for m = 1 the polynomials
Bm,k and Cm,k are deﬁned in the same way as for 2 ≤ m ≤ n − 2 (with P∗ = P ′), but
A1,k = amin(1,n−k)+max(0,n−k−2)
n , see [7] and [8]. Hence for m = 1 and P∗ = P (m) there are two
diﬀerences w.r.t. the case m ≥ 2 – the degree 3 (instead of 1) of B1,k, and A1,n−1 = an (instead
of A1,n−1 = 1). This diﬀerence can be assumed to stem from the fact that for m = 1, if P has
a root of multiplicity ≥ 3, then this is a root of multiplicity ≥ 2 for P ′. This explanation is
detailed below and in Remark 16.
For n = 4 and for generic values of bj the polynomials ˜D1,k, up to a constant nonzero factor,
are of the form

˜D1,1 = (b1/b0)3(1 − b1/b0)2 a2
4 ˜B1,1 ˜C 2
1,1 , ˜D1,2 = −(b2/b0)2(1 − b2/b0)2 a4 ˜B1,2 ˜C 2
1,2 ,

˜D1,3 = −(b3/b0)2(1 − b3/b0)3 a4 ˜B1,3 ˜C 2
1,3 , ˜D1,4 = ˜B1,4 ˜C 2
1,4 ,

where the polynomials ˜B1,k and ˜C1,k, when considered as polynomials in the variables aj and
bj, are irreducible. Set b1 = 3b0/4, b2 = b0/2, b3 = b0/4. This is the case P∗ = P ′; we
write ˜B1,k|b1=3b0/4,b2=b0/2,b3=b0/4 = B1,k and ˜C1,k|b1=3b0/4,b2=b0/2,b3=b0/4 = C1,k. In this case the
polynomials ˜C1,k become reducible; they equal B1,kC1,k which explains the presence of the cubic
factor B3
1,k.
 4

Thus for m = 1 the genericity condition 0 ̸= bj ̸= bi ̸= 0 (which we assume to hold true in
the formulation of Theorem 4) is not suﬃcient in order to have the presentation (1) for ˜Dm,k. At
the same time imposing a more restrictive condition means leaving outside the most interesting
case P∗ = P ′.
(2) For m = n − 1 the analog of the factor Cm,k does not exist because P∗ has a single
root −b1/b0. For P∗ = P (n−1) := n!(x + a1/n) this is x = −a1/n. In this case one ﬁnds that
˜Dn−1 = (−1)n(n!)nP (−a1/n). To see this one subtracts for j = 1, . . ., n the jth column of the
Sylvester matrix S(P, x + a1/n) multiplied by −a1/n from its (j + 1)st column. This yields an
(n + 1) × (n + 1)-matrix W whose entry in position (1, n + 1) equals P (−a1/n) and which below
the ﬁrst row has units in positions (ν + 1, ν), ν = 1, . . ., n, and zeros elsewhere. Hence det W =
(−1)nP (−a1/n). There remains to remind that ˜Dn−1 = det S(P, n!(x + a1/n)) = (n!)n det W .
One ﬁnds directly that ˜Dn−1,k = ∂ ˜Dn−1/∂ak = (−1)n(n!)n(−a1/n)n−k, 2 ≤ k ≤ n. To ﬁnd
also ˜Dn−1,1 one ﬁrst observes that

Pn−1,1(x)/(n − 1)! = −(n − 1)xn + a2xn−2 + a3xn−3 + · · · + an

and that P (−a1/n) = Pn−1,1(−a1/n)/(n − 1)!. Hence up to a nonzero rational factor the deter-
minants of the matrices S(Pn−1,1, P ′
n−1,1) and S( ˜Dn−1, ∂ ˜Dn−1/∂a1, a1) coincide, i.e. ˜Dn−1,1 =
ˆc Res(Pn−1,1, P ′
n−1,1), ˆc ∈ Q.
(3) The fact that the factor Cm,k is squared (see formula (1)) is not astonishing. At a generic
point of the Maxwell stratum the hypersurface { ˜Dm = 0} ⊂ A is locally the intersection of two
analytic hypersurfaces, see Statement 13. Consider a point Ψ ∈ Ak close to the projection Λ0 in
Ak of a generic point Λ ∈ ˜M . There exist two points Kj ∈ { ˜Dm = 0}, j = 1, 2, which belong to
these hypersurfaces and are close to Λ, and whose common projection in Ak is Ψ. There exists
a loop γ ⊂ Ak, Ψ ∈ γ, which circumvents the projection in Ak of the set Θ ∪ ˜M such that if
one follows the two liftings on { ˜Dm = 0} of the points of γ which at Ψ are the points Kj, then
upon one tour along γ these liftings are exchanged. Hence in order to deﬁne the projection of
˜M in Ak by the zeros of an analytic function one has to eliminate this monodromy of rank 2 by
taking the square of Cm,k. For the case m = 1 a detailed construction of such a path γ is given
in [8].
 c c cO OO
 d d

d
 L

H

S T

V U

Figure 1: The sets { ˜D2 = 0}|a=0,b=−1, { ˜D2 = 0}|a=b=0 and { ˜D2 = 0}|a=0,b=1 for n = 4.

Example 7. For n = 4 we consider the case of real polynomials. We write P = x4 + ax3 +
bx2 + cx + d and we limit ourselves to the situation when P∗ := P (m). On Fig. 1 we show the
sets { ˜D1 = 0}|a=0 and { ˜D2 = 0}|a=0 when b, c and d are real. The sets { ˜D1 = 0}|a=0 and

5

{ ˜D2 = 0}|a=0 are invariant under the quasi-homogeneous dilatations a ↦→ ta, b ↦→ t2b, c ↦→ t3c,
d ↦→ t4d, therefore the intersections of the sets with the subspaces {b = 0} and {b = ±1} give
a suﬃcient idea about them. For each of these three intersections we represent the axes c and
d, see Fig. 1. For b = −1 the set { ˜D1 = 0}|a=0 is a curve with one self-intersection point at S
and two ordinary 2/3-cusps at U and V ; it is drawn in solid line. At U and V the polynomial
P has one triple and one simple real root. The set { ˜D2 = 0}|a=0,b=−1 consists of two straight
(dashed) lines intersecting at H and tangent to the set { ˜D1 = 0}|a=0 at the cusps U and V .
The sets { ˜D1 = 0}|a=0,b=0 and { ˜D1 = 0}|a=0,b=1 are parabola-like curves, the former has a
4/3-singularity at the origin while the latter is smooth everywhere. The set { ˜D1 = 0}|a=0,b=1
contains an isolated double point T . The set { ˜D2 = 0}|a=0,b=0 (resp. { ˜D2 = 0}|a=0,b=1) is the
c-axis (resp. the point L). The points S, T and for b = 0 the origin belong to a parabola
(because the quasi-homogeneous weights of the variables a2 and a4 equal 2 and 4 respectively).
So do the points H, L and the origin for b = 0. At S (resp. T ) the polynomial P has two real
(resp. two imaginary conjugate) double roots. At H and L the polynomial P is divisible by P ′′.
Globally the set { ˜D2 = 0}|a=0 is diﬀeomorphic to a Whitney umbrella. The set { ˜D2 = 0}|a=0
is smooth along the c-axis for b = 0 (except at the origin) and its tangent plane is the cd-plane.

3 The factor Am,k

The following lemma will be used in several places of this paper:

Lemma 8. Consider a p × p-matrix A having nonzero entries only
i) on the diagonal (denoted by rj, in positions (j, j), j = 1, . . ., p);
ii) in positions (ν, ν + s), ν = 1, . . ., p − s (denoted by qν), 1 ≤ s ≤ p − 1, and
iii) in positions (µ + p − s, µ), µ = 1, . . ., s (denoted by qµ+p−s).
Then det A = r1 · · · rp ± q1 · · · qp.

Proof. Developing det A w.r.t. its ﬁrst row one obtains the equality

det A = r1 det B + (−1)
s+2q1 det C , where B = [A]1,1 and C = [A]1,s+1 .

The matrix B contains p − 1 entries rj (namely, r2, . . ., rp) and p − 2 entries qν (the ones with
1 ̸= ν ̸= 1 + p − s). In the same way, the matrix C contains p − 2 entries rj (1 ̸= j ̸= s + 1) and
p − 1 entries qν (ν ̸= 1).
When ﬁnding det B one can develop it w.r.t. that row or column in which there is an entry
rj and there is no entry qν. By doing so p − 1 times one ﬁnds that det B = r2 · · · rp. The + sign
of this product follows from the entries rj being situated on the diagonal. When ﬁnding det C
one can develop it w.r.t. that row or column in which there is an entry qν and there is no entry
rj. By doing so p − 1 times one ﬁnds that det C = ±q2 · · · qp which proves the lemma.

In the present section we prove the following proposition:

Proposition 9. (1) For k = n − m + 1, . . ., n, the polynomial ˜Dm,k is not divisible by any of
the variables aj, j ̸= n − m.
(2) For k = 1, . . . , n − m, the polynomial ˜Dm,k is not divisible by any of the variables aj,
j ̸= n.
(3) For k = 1, . . ., n − m, the polynomial ˜Dm,k is divisible by an−m−k
n and not divisible by
an−m−k+1
n .
(4) For k = n − m + 1, . . . ,n, it is divisible by a
n−k
n−m and not divisible by a
n−k+1
n−m .

6

Proof of part (1): We show ﬁrst that for ai = 0, n − m ̸= i ̸= k, the polynomial ˜Dm is of
the form Ω′an
n−m + Ω′′an−k
n−ma
n−m
k . Indeed, in this case one can list the nonzero entries of the
(2n − m) × (2n − m)-matrix S(P, P∗) and the positions in which they are situated:

1 (j, j) , an−m (j, j + n − m) ,

ak (j, j + k) , j = 1, . . . , n − m ,

b0 (ν + n − m, ν) , bn−man−m (ν + n − m, ν + n − m) , ν = 1, . . . , n .

Subtract the (µ + n − m)th row multiplied by 1/bn−m from the µth one for µ = 1, . . ., n − m.
This makes disappear the terms an−m in positions (j, j + n − m) while the terms 1 in positions
(j, j) become equal to Ω∗ := 1 − b0/bn−m. The determinant of the matrix doesn’t change. We
denote the new matrix by T . To compute det T one can develop it n − k times w.r.t. the last
column; each time one has a single nonzero entry in this column, this is bn−man−m in position
(2n − m − ℓ, 2n − m − ℓ), ℓ = 0, . . ., n − k − 1. The matrix T1 which remains after deleting the
last n − k rows and columns of T has the following nonzero entries, in the following positions:

Ω∗ (j, j) , ak (j, j + k) , j = 1, . . . , n − m ,

b0 (ν + n − m, ν) , bn−man−m (ν + n − m, ν + n − m) , ν = 1, . . . , k .

Clearly det T = (bn−man−m)n−k det T1. On the other hand the matrix T1 satisﬁes the conditions
of Lemma 8 with p = n − m + k and s = k. Hence det T1 = ˜Ω′ak
n−m + ˜Ω′′an−m
k and ˜Dm =
Ω′an
n−m + Ω′′an−k
n−ma
n−m
k .
But then the (2n − 2m − 1) × (2n − 2m − 1)-Sylvester matrix S∗ := S( ˜Dm, ∂ ˜Dm/∂ak, ak)
has only the following nonzero entries, in the following positions:

Ω′′an−k
n−m (j, j) , Ω′an
n−m (j, j + n − m) , j = 1, . . . , n − m − 1 ,

(n − m)Ω′′an−k
n−m (ν + n − m − 1, ν) , , ν = 1 . . . , n − m .

Part (1) follows from det S∗ = ±(Ω′an
n−m)n−m−1((n − m)Ω′′an−k
n−m)n−m ̸≡ 0.

Proof of part (2): We prove that for ai = 0, k ̸= i ̸= n, the polynomial ˜Dm is of the form
Ω†an−m
n + Ω††an−m−k
n an
k . Indeed, we list below the nonzero entries of the matrix S(P, P∗) and
their positions:

1 (j, j) , ak (j, j + k) ,

an (j, j + n) , j = 1, . . . , n − m ,

b0 (ν + n − m, ν) , bkak (ν + n − m, ν + k) , ν = 1, . . . , n .

One can develop n − m − k times det S(P, P∗) w.r.t. its last column, where the only nonzero
entries equal an. Thus det S(P, P∗) = ±an−m−k
n det H, where H is obtained from S(P, P∗) by

7

deleting the last n − m − k columns and the rows with indices k + 1, . . ., n − m. The matrix H
has the following nonzero entries, in the following positions:

1 (j, j) , ak (j, j + k) ,

an (j, j + n) , j = 1, . . . , k ,

b0 (ν + k, ν) , bkak (ν + k, ν + k) , ν = 1, . . . , n .

For µ = 1, . . ., k one can subtract the (µ + k)th row multiplied by 1/bk from the µth one to
make disappear the terms ak in positions (µ, µ + k); the entries 1 in positions (µ, µ) change to
Ω∗ := 1 − b0/bk. We denote the newly obtained matrix by H1. Obviously det H1 = det H; we
list the nonzero entries of H1 and their respective positions:

Ω∗ (j, j) , an (j, j + n) , j = 1, . . . , k ,

b0 (ν + k, ν) , bkak (ν + k, ν + k) , ν = 1, . . . , n .

One applies Lemma 8 with p = n + k, s = n to the matrix H1 to conclude that det H = det H1 =
(Ω∗)k(bkak)n ± bn
0 ak
n, so ˜Dm = det S(P, P∗) = Ω†an−m
n + Ω††an−m−k
n an
k .
But then the (2n − 1) × (2n − 1)-Sylvester matrix S( ˜D, ∂ ˜D/∂ak, ak) has only the following
nonzero entries, in the following positions:

Ω††an−m−k
n (j, j) , Ω†an−m
n (j, j + n) , j = 1, . . . , n − 1 ,

nΩ††an−m−k
n (ν + n − 1, ν) , ν = 1, . . . , n .

Its determinant equals ±(Ω†an−m
n )n−1(nΩ††an−m−k
n )n ̸≡ 0 which proves part (2).

Proof of part (3): For k = 1, . . . ,n − m the polynomial ˜Dm contains the monomial Mk :=
±bn
k an
k (1 − b0/bk)kan−m−k
n , and it does not contain any other monomial of the form Ωan
k E,
where E is a product of powers of variables ai with i ̸= k, see Proposition 1.
Hence the ﬁrst column of the (2n − 1) × (2n − 1)-matrix Y := S( ˜Dm, ∂ ˜Dm/∂ak, ak) contains
only two nonzero entries, and these are Y1,1 = ±bn
k (1 − b0/bk)kan−m−k
n and Yn,1 = ±nbn
k (1 −
b0/bk)kan−m−k
n . Thus ∆ := det Y is divisible by an−m−k
n . We consider two cases:
Case 1: k = n−m. We have to prove that ˜Dm,n−m|an=0 ̸≡ 0. Set aj = 0 for n−m ̸= j ̸= n−1.
Hence the nonzero entries of the matrix S(P, P∗) and their positions are

1 (j, j) , an−m (j, j + n − m) ,

an−1 (j, j + n − 1) , j = 1, . . . , n − m ,

b0 (ν + n − m, ν) , bn−man−m (ν + n − m, ν + n − m) , ν = 1, . . . , n .

One can subtract the (j +n−m)th row multiplied by 1/bn−m from the jth one, j = 1, . . ., n−m,
to make disappear the terms an−m in the ﬁrst n − m rows. This doesn’t change det S(P, P∗).
The terms 1 in positions (j, j) are replaced by 1 − b0/bn−m. Hence ˜Dm is of the form Ω1an
n−m +
Ω2an−m
n−1 an−m (one ﬁrst develops det S(P, P∗) w.r.t. the last column, where there is a single
nonzero entry bn−man−m in position (2n − m, 2n − m), and then applies Lemma 8 with p =
2n − m − 1 and s = n − 1).
 8

Thus the matrix SH := S( ˜Dm, ∂ ˜Dm/∂an−m, an−m) contains only the following nonzero en-
tries, in the following positions:

Ω1 (j, j) , Ω2an−m
n−1 (j, j + n − 1) , j = 1, . . . , n − 1 ,

nΩ1 (ν + n − 1, ν) , Ω2an−m
n−1 (ν + n − 1, ν + n − 1) , ν = 1, . . . , n .

One can subtract the (j + n − 1)st row from the jth one, j = 1, . . ., n − 1, to make disappear
the terms Ω2a
n−m
n−1 in the ﬁrst n − 1 rows; the terms Ω1 become (1 − n)Ω1. Hence det SH =

Ω3an(n−m)
n−1 ̸≡ 0.
Case 2: 1 ≤ k ≤ n − m − 1. To prove that ∆ is not divisible by an−m−k+1
n we develop it
w.r.t. its ﬁrst column:

∆ := (±bn
k (1 − b0/bk)
kan−m−k
n )(det([Y ]1,1) + (−1)
n+1n det([Y ]n,1)) .

Our aim is to show that for an = 0 the sum Z := det([Y ]1,1) + (−1)n+1n det([Y ]n,1) is nonzero;
this implies an−m−k+1
n not dividing ∆. Notice that for an = 0 the only nonzero entries in the
second column of Y (i.e. of Y |an=0 =: Y 0) are Y 0
1,2 and Y 0
n,2 = (n − 1)Y 0
1,2. Thus

Z|an=0 = (Y 0
1,2 + (−1)
n+1(−1)
nnY 0
n,2) det(Y †) = (1 − n(n − 1))Y 0
1,2(det Y †) , (2)

where the matrix Y † is obtained from Y 0 by deleting its ﬁrst two columns, its ﬁrst and its nth
rows.

Lemma 10. The entry Y 0
1,2 is a not identically equal to 0 polynomial in the variables aj, k ̸=
j ̸= n.

Proof. Indeed, this is the coeﬃcient of a
n−1
k in R0 :=Res(P, P∗)|an=0. The matrix S∗ :=
S(P, P∗)|an=0 has a single nonzero entry in its last column; this is (S∗)2n−m,2n−m = bn−man−m.
Hence R0 = bn−man−m det M , where M := [S∗]2n−m,2n−m (M is (2n − m − 1) × (2n − m − 1)).
For ν = 1, . . . , n − m one can subtract the (n − m + ν)th row of M multiplied by 1/bk
from its νth row to make disappear the terms ak in its ﬁrst n − m rows. The new matrix is
denoted by M 1; one has det M = det M 1. The only terms of det M 1 containing an−1
k are now
obtained by multiplying the entries bkak of the last n − 1 rows of M 1. To get these terms up
to a sign one has to multiply (bkak)n−1 by det M ∗, where M ∗ is obtained from M 1 by deleting
the rows and columns of the entries bkak. The matrix M ∗ is block-diagonal, its left upper
block is upper-triangular and its right lower block is lower-triangular. The diagonal entries of
these blocks (of sizes k × k and (n − m − k) × (n − m − k)) equal 1 − b0/bk and an−1. Hence
Y 0
1,2 = ±bn−man−m(1 − b0/bk)kbn−1
k an−m−k
n−1 ̸≡ 0.

There remains to prove that det Y † ̸≡ 0, see (2). The matrix Y † is obtained as follows. Set
D† := ˜Dm|an=0 = det S∗; recall that det S∗ = bn−man−m det M 1, see the proof of Lemma 10.
Then Y † = S(D†, ∂D†/∂ak, ak). Notice that D† is a degree n − 1, not n, polynomial in ak,
therefore Y † is (2n − 3) × (2n − 3). It suﬃces to show that for aj = 0, j ̸= k, n − m, n − 1,
one has det Y † ̸≡ 0. This results from det M 1|aj =0,k̸=j̸=n−1 not having multiple roots (which we
prove below).
One can develop n − m − k times det M 1 w.r.t. its last column, where it has a single
nonzero entry an−1, to obtain det M 1 = ±an−m−k
n−1 det M †; M † is (n + k − 1) × (n + k − 1), it
is obtained from M 1 by deleting the last n − m − k columns and the rows with indices k + 1,
. . ., n − m. The matrix M † satisﬁes the conditions of Lemma 8 with p = n + k − 1 and s = k,

9

the entries rj from the lemma equal 1 − b0/bk ̸= 0 (for j = 1, . . ., k) or bkak (for j = k + 1,
. . ., n + k − 1); one has qj = an−1 (1 ≤ j ≤ k) or qj = b0 (k + 1 ≤ j ≤ n + k − 1). Hence
det M †|aj =0,k̸=j̸=n−1 = (1 − b0/bk)k(bkak)n−1 ± bn−1
0 ak
n−1. For an−1 ̸= 0 it has n − 1 distinct
roots. Part (3) is proved.

Proof of part (4): We use sometimes the same notation as in the proof of part (3), but with
diﬀerent values of the indices, therefore the proofs of the two parts of the proposition should
be considered as independent ones. For k = n − m + 1, . . . ,n, the polynomial ˜Dm contains the
monomial Nk−n+m := ±bn−k
n−man−k
n−mbk
0a
n−m
k ; it does not contain any other monomial of the form
Ωan−m
k D, where D is a product of powers of variables ai with i ̸= k, see Proposition 1.
The ﬁrst column of the (2n − 2m − 1) × (2n − 2m − 1)-matrix Y := S( ˜Dm, ∂ ˜Dm/∂ak, ak) con-
tains only two nonzero entries, namely Y1,1 = ±bn−k
n−ma
n−k
n−mbk
0 and Yn−m,1 = ±(n−m)bn−k
n−man−k
n−mbk
0.
Thus det Y is divisible by a
n−k
n−m. We consider two cases:
Case 1: k = n. We show that det Y ̸≡ 0 if an−m = 0. We prove this for aj = 0, n − m − 1 ̸=
j ̸= n. In this case the nonzero entries of the matrix S(P, P∗) and their positions are

1 (j, j) , an−m−1 (j, j + n − m − 1) ,

an (j, j + n) , j = 1, . . . , n − m ,

b0 (ν + n − m, ν) , bn−m−1an−m−1 (ν + n − m, ν + n − m − 1) , ν = 1, . . . , n .

Subtracting the (j + n − m)th row multiplied by 1/bn−m−1 from the jth one for j = 1, . . ., n − m,
one makes disappear the terms an−m−1 in the ﬁrst n − m rows. The only nonzero entry in the
last column is now an in position (n − m, 2n − m), so

det S(P, P∗) = (−1)
nan det[S(P, P∗)]n−m,2n−m .

The last matrix satisﬁes the conditions of Lemma 8 with p = 2n−m−1, s = n and one ﬁnds that
its determinant is of the form Ω4an
n−m−1+Ω5an−m−1
n . Hence det S(P, P∗) = (−1)nan(Ω4an
n−m−1+
Ω5an−m−1
n ). This means that the matrix S( ˜Dm, ∂ ˜Dm/∂an, an) has only the following entries in
the following positions:

Ω5 (j, j) , Ω4an
n−m−1 (j, j + n − m − 1) ,

j = 1, . . . , n − m − 1 ,

(n − m)Ω5 (ν + n − m − 1, ν) , Ω4an
n−m−1 (ν + n − m − 1, ν + n − m − 1) ,

ν = 1, . . . , n − m .

One can subtract the (j + n − m − 1)st row from the jth one, j = 1, . . ., n − m − 1, to make
disappear the terms Ω4an
n−m−1 in the ﬁrst n − m − 1 rows. The matrix becomes lower-triangular,
with diagonal entries equal to (1−n+m)Ω5 or to Ω4an
n−m−1, so its determinant is not identically
equal to 0.
Case 2: n − m + 1 ≤ k ≤ n − 1. To prove that det Y is not divisible by a
n−k+1
n−m we develop
it w.r.t. its ﬁrst column:

det Y = (±bn−k
n−man−k
n−mb
k
0)(det([Y ]1,1) + (−1)
n−m(n − m) det([Y ]n−m,1)) .

10

Our aim is to show that for an−m = 0 the sum U := det([Y ]1,1) + (−1)n−m(n − m) det([Y ]n−m,1)
is nonzero; this implies an−k+1
n−m not dividing det Y . Notice that for an−m = 0 the only nonzero
entries in the second column of Y 0 := Y |an−m=0 are Y 0
1,2 and Y 0
n−m,2 = (n − m − 1)Y 0
1,2. Thus

U |an−m=0 = (Y 0
1,2 + (−1)n+1(−1)n−m(n − m)Y 0
n−m,2) det Y †

= (1 − (n − m)(n − m − 1))Y 0
1,2 det Y † , (3)

where the matrix Y † is obtained from Y 0 by deleting its ﬁrst two columns, its ﬁrst and (n−m)th
rows.

Lemma 11. The entry Y 0
1,2 is a not identically equal to 0 polynomial in the variables aj, k ̸=
j ̸= n − m.

Proof. Indeed, this is the coeﬃcient of an−m−1
k in R0 :=Res(P, P∗)|an−m=0. The matrix S∗ :=
S(P, P∗)|an−m=0 has a single nonzero entry in its last column; this is (S∗)n−m,2n−m = an. Hence
R0 = an det M , where M := [S∗]n−m,2n−m (M is (2n − m − 1) × (2n − m − 1)).
The only terms of det M containing a
n−m−1
k are obtained by multiplying the entries ak of
the ﬁrst n − m − 1 rows of M . To obtain these terms up to a sign one has to multiply an−m−1
k by
det M ∗, where M ∗ is obtained from M by deleting the rows and columns of the entries ak. The
matrix M ∗ is block-diagonal, its left upper block is upper-triangular and its right lower block is
lower-triangular. The diagonal entries of these blocks (of sizes k×k and (n−m−k)×(n−m−k))
equal b0 and an−m−1. Hence Y 0
1,2 = ±anbk
0an−m−k
n−m−1 ̸≡ 0.

There remains to prove that det Y † ̸≡ 0, see (3). The matrix Y † is obtained as follows. Set
D† := ˜Dm|an−m=0 = det S∗; recall that det S∗ = an det M (see the proof of Lemma 11). Then
Y † = S(D†, ∂D†/∂ak, ak). Notice that D† is a degree n − m − 1, not n − m, polynomial in ak,
therefore Y † is (2n−2m−3)×(2n−2m−3). It suﬃces to show that for aj = 0, k ̸= j ̸= n−m−1,
one has det Y † ̸≡ 0. This results from det M |aj =0,k̸=j̸=n−m−1 not having multiple roots (which
we prove below).
For aj = 0, k ̸= j ̸= n − m − 1, one can develop n − k times det M w.r.t. its last column
in which there is a single nonzero entry bn−m−1an−m−1 (on the diagonal). Hence det M =
(bn−m−1an−m−1)n−k det M †, where M † is (n − m + k − 1) × (n − m + k − 1); it is obtained
from M by deleting the last n − k rows and columns. The matrix M † satisﬁes the conditions of
Lemma 8 with p = n − m + k − 1, s = k, rj = 1, qj = ak (j = 1, . . ., n − m − 1) or rj = an−m−1,
qj = b0 (j = n − m, . . ., n − m + k − 1). Hence det M † = ak
n−m−1 ± bk
0an−m−1
k . For an−m−1 ̸= 0
it has n − m − 1 distinct roots.

4 Some properties of the sets Θ and ˜M

Lemma 12. Suppose that all roots of P∗(., a0) (a0 ∈ A) are simple and nonzero and that
P (., a0) and P∗(., a0) have exactly one root in common. Then for any j = n − m + 1, . . ., n, in a
neighbourhood of a0 ∈ A the set { ˜Dm = 0} is locally the graph of a smooth analytic function in
the variables aj. If in addition all roots of Pm,k(., a0) are simple and nonzero (1 ≤ k ≤ n − m),
then in a neighbourhood of a0 ∈ A the set { ˜Dm = 0} is locally the graph of a smooth analytic
function in the variables ak.

Proof. Denote by [a]n−m the ﬁrst n−m coordinates of a ∈ A. Any simple root of P∗ is locally (in
a neighbourhood of [a0]n−m) the value of a smooth analytic function λ in the variables [a]n−m.

11

As λ([a0]n−m) ̸= 0, the condition P (λ, a)/λj = 0, j < m, allows to express an−j locally (for ai
close to a0
i , i ̸= j) as a smooth analytic function in the variables an−j. Suppose that all roots
of Pm,k(., a0) are simple and nonzero. Then any of these roots is a smooth analytic function in
the variables ak. This refers also to µ, the root in common of P and P∗ which is also a root of
Pm,k. Hence one can express ak as a function in ak from the condition P (µ, a)/µn−k = 0.

Statement 13. At a point of the Maxwell stratum the hypersurface { ˜Dm = 0} is locally the
transversal intersection of two smooth analytic hypersurfaces along a smooth analytic subvariety
of codimension 2.

Proof. Suppose ﬁrst that the roots in common of P and P∗ are 0 and 1. The two conditions
P∗(0) = P∗(1) = 0 deﬁne a codimension 2 linear subspace S in the space A of the variables
a. Adding to them the two conditions P (0) = P (1) = 0 means deﬁning a codimension 2
linear subspace T ⊂ S; hence T is a codimension 4 linear subspace of A. The two linear
subspaces {P (0) = 0} and {P (1) = 0} and their intersections with {P∗(0) = P∗(1) = 0}
intersect transversally (along respectively {P (0) = P (1) = 0} and T ).
By means of a linear change τ : x ↦→ αx + β, α ∈ C∗, β ∈ C, one can transform any
pair of distinct complex numbers into the pair (0, 1). Hence at a point of T the Maxwell
stratum is locally the direct product of T and the two-dimensional orbit of the group of linear
diﬀeomorphisms induced in the space A by the group of linear changes τ . This proves the
statement.

Statement 14. (1) At a point of the set Θ (see Deﬁnition 3) the set { ˜Dm = 0} is not repre-
sentable as the graph in the space A of a smooth analytic function in the variables aj, for any
j = n − m + 1, . . ., n.
(2) At a point of the set Θ this set is a smooth analytic variety of dimension n − 2 in the
space of variables a.

Proof of part (1): Suppose that for some a = a0 ∈ A one has P∗(x0, a0) = P ′
∗(x0, a0) = 0.
Suppose ﬁrst that x0 ̸= 0. Consider the equation

P∗(x, a0) = ε , where ε ∈ (C, 0) . (4)

Its left-hand side equals P ′′
∗ (x0, a0)(x − x0)2/2 + o((x − x0)2) (with P ′′
∗ (a0, x0) ̸= 0). Thus locally
(for x close to x0) one has
 x − x0 = (2/P ′′
∗ (x0, a0))
1/2ε
1/2 + o(ε
1/2) . (5)

In a neighbourhood of a0 ∈ A one can introduce new coordinates two of which are x0 and ε.
Indeed, one can write

(n − m − 1)!P ′
∗/n! = (x − x0)(xn−m−2 + g1xn−m−3 + · · · + gn−m−2)

= xn−m−1 + b∗
1a1xn−m−2 + · · · + b∗
n−m−1an−m−1 ,

where b∗
j = (n − j)!(n − m − 1)!/(n − m − j − 1)!n!. Hence

b∗
1a1 = g1 − x0 , b∗
2a2 = g2 − x0g1 , . . . ,

b∗
n−m−2an−m−2 = gn−m−2 − x0gn−m−3 , b∗
n−m−1an−m−1 = −x0gn−m−2 .

12

The Jacobian matrix ∂(a1, . . ., an−m−1)/ ∂(x0, g1, . . ., gn−m−2) is, up to multiplication of the
columns by nonzero constants followed by transposition, the Sylvester matrix of the polynomials
x − x0 and xn−m−2 + g1xn−m−3 + · · · + gn−m−2. Its determinant is nonzero because x0 is not a
root of the second of these polynomials.
Thus in the space of the variables (a1, . . ., an−m−1) one can choose as coordinates (x0, g1, . . .,
gn−m−2). The polynomial P∗ is a primitive of P ′
∗ and (−ε) can be considered as the constant of
integration, see (4), therefore (x0, g1, . . ., gn−m−2, ε) can be chosen as coordinates in the space
of the variables (a1, . . ., an−m). Adding to them (an−m+1, . . ., an), one obtains local coordinates
in the space A.
Hence the double root µ of P∗ is not an analytic, but a multivalued function of the local
coordinates in A, see (5). Consider the condition P (µ, a)/µn−j = 0. One can express from it aj
(n − m + 1 ≤ j ≤ n) as a linear combination of the variables aj with coeﬃcients depending on
µ. This expression is of the form A + ε1/2B, where A and B (B ̸≡ 0) depend analytically on
the local coordinates in A. This proves the statement for x0 ̸= 0. For x0 = 0 the statement also
holds true – if for x0 = 0 the set { ˜Dm = 0} is locally the graph of a holomorphic function in
the variables aj, then this must be the case for nearby values of x0 as well which is false. Such
values exist – the change x ↦→ x + δ, δ ∈ C, shifts simultaneously by −δ all roots of P (hence of
all its nonconstant derivatives as well).

Proof of part (2): Denote by ξ the root of P ′
∗ which is also a root of P∗ and of P . Then ξ is a
smooth analytic function in the variables a† := (a1, . . ., an−m−1). The condition P∗(ξ, a) = 0 al-
lows to express an−m as a smooth analytic function α in the variables a†. Set a∗ := a|an−m=α(a†).
One can express an as a smooth analytic function in the variables aj, n − m ̸= j ̸= n, from the
condition P (ξ, a∗) = 0. Thus locally Θ is the graph of a smooth analytic vector-function in the
variables aj, n − m ̸= j ̸= n, with two components.

Statement 15. For 2 ≤ m ≤ n − 2 the polynomials Bm,k and Cm,k deﬁned in Theorem 4 are
irreducible.

Proof. Irreducibility of the factor Bm,k is proved by analogy with Proposition 1. (For n−m+1 ≤
k ≤ n the analogy is complete because after the dilatations aj ↦→ aj/bj, j = 1, . . ., n − m, the
polynomial P∗ becomes b0P ∗, where P ∗ is the polynomial P deﬁned for n − m instead of n. For
1 ≤ k ≤ n − m the coeﬃcients of the polynomial Pm,k are not aj (we set a0 = 1), but (bk − bj)aj,
and one can perform similar dilatations. Only the variable ak is absent; this, however, is not an
obstacle to the proof of irreducibility. The details are left for the reader.)
Irreducibility of the factors Cm,k can be proved like this. Denote by ξ and η two of the
roots of P∗. They are multivalued functions of the coeﬃcients a1, . . ., an−m. The system of
two equations P (ξ, a) = P (η, a) = 0 allows to express for ξ ̸= η the coeﬃcients an and an−1 as
functions of a1, . . ., an−2. These multivalued functions are deﬁned over a Zariski dense open
subset of the space of variables (a1, . . ., an−2) from which irreducibility of the set ˜M follows.
Hence its projections in the hyperplanes Ak are also irreducible.

Remark 16. In the case m = 1 one cannot prove in the same way as above that the polynomials
C1,k are irreducible because the coeﬃcient an−1 is in fact an−m.

Remark 17. Proposition 9, Lemma 12, Statements 13, 14 and 15 allow to conclude that ˜Dm,k
is of the form Am,kBsm,k
m,k C rm,k
m,k , where sm,k, rm,k ∈ N. Indeed, the form of the factor Am,k is
justiﬁed by Proposition 9. It follows from Lemma 12 and its proof that for Am,kBm,kCm,k ̸= 0
the polynomials ˜Dm and ∂ ˜Dm/∂ak, when considered as polynomials in ak, have no root in
common. Hence a priori ˜Dm,k is of the form Am,kBsm,k
m,k C rm,k
m,k , with sm,k, rm,k ∈ N ∪ 0 (implicitly

13

we use the irreducibility of Bm,k and Cm,k here). Statements 13 and 14 imply that one cannot
have sm,k = 0 or rm,k = 0. To prove formula (1) now means to prove that sm,k = 1, rm,k = 2.
This is performed in the next sections.

5 The case m = n − 2

Proposition 18. For m = n − 2, n ≥ 4, one has sm,k = 1 and rm,k = 2.

Proof for 3 ≤ k ≤ n. For 3 ≤ k ≤ n the polynomial ˜Dn−2 is a degree 2 polynomial in ak,
see Proposition 1, so one can set ˜Dn−2 := U a2
k + V ak + W and ∂ ˜Dn−2/∂ak = 2U ak + V ,

where U , V , W ∈ C[ak], U ̸≡ 0. Hence S( ˜Dn−2,∂ ˜Dn−2/∂ak, ak) =
 

 U V W
2U V 0
0 2U V
 

 and

˜Dn−2,k = U (4U W − V 2). The second factor is up to a sign the discriminant of the quadratic
polynomial (in the variable ak) U a2
k +V ak +W . Up to a sign, U is the determinant of the matrix
SL obtained from S(P, P∗) by deleting its ﬁrst two rows and the columns, where its entries ak
are situated. Hence U = ωa
n−k
2 , ω ∈ C∗. Indeed, SL is block-diagonal, with diagonal blocks of
sizes k × k (upper left) and (n − k) × (n − k) (lower right). They are respectively upper- and
lower-triangular, with diagonal entries equal to b0 and b2a2.
For a2 = 0 the factor 4U W − V 2 reduces to −V 2 ∈ C[a]. From the following lemma we
deduce (after its proof) that the factor Cn−2,k must be squared.

Lemma 19. The polynomial −V 2 is a quadratic polynomial in the variables ai, i = 3, . . ., n,
with the square of at least one of them present in −V 2. For k < n (resp. k = n) it contains the
monomial a2
n(b0)2k(b1a1)2(n−k) (resp. a2
n−1(b0)2(n−1)(b1a1)2).

Proof. Indeed, if k < n, then set V ∗ := V |aj =0,j̸=1,k,n and S∗ := S(P, P∗)|aj =0,j̸=1,k,n. There
are two entries ak (resp. a1 and an) in S∗, in positions (1, k + 1) and (2, k + 2) (resp. (1, 2),
(2, 3), and (1, n + 1), (2, n + 2)). The other nonzero entries of S∗ are b0 (resp. b1a1) in positions
(ν + 2, ν) (resp. (ν + 2, ν + 1)), ν = 1, . . ., n. Thus

V ∗ = det V ∗∗ + det V ∗∗∗ , where V ∗∗ = [S∗]1,k+1|ak=0 , V ∗∗∗ = [S∗]2,k+2|ak=0 .

The matrices V ∗∗ and V ∗∗∗ are (n + 1) × (n + 1). Hence

det V ∗∗ = (−1)
nan det[V ∗∗]1,n+1 , det V ∗∗∗ = 0

(because all entries in the last column of V ∗∗∗ equal 0). The matrix [V ∗∗]1,n+1 is block-diagonal,
with diagonal blocks of sizes k × k (left upper, it is upper-triangular) and (n − k) × (n − k) (right
lower, it is lower-triangular). Their diagonal entries equal respectively b0 and b1a1. Thus

V ∗ = det V ∗∗ = (−1)
nan(b0)
k(b1a1)
n−k .

Hence for k < n the term −V 2 contains the monomial a2
n(b0)2k(b1a1)2(n−k).
For k = n we set aj = 0, j ̸= 1, n − 1, n, S† := S(P, P∗)|aj =0,j̸=1,n−1,n and V † :=
V |aj =0,j̸=1,n−1,n. Hence

V † = det V †† + det V ††† , where V †† = [S†]1,n+1|an=0 , V ††† = [S†]2,n+2|an=0 .

14

One has det V †† = 0 (all entries in the last column are 0) and V ††† has an entry an−1 in
position (1, n); no other entry of V ††† depends on an−1. Hence det V ††† contains the monomial
(−1)n+1an−1 det[V †††]1,n. The matrix [V †††]1,n is block-diagonal, with diagonal blocks of sizes
(n − 1) × (n − 1) (upper left, it is upper-triangular, with diagonal entries equal to b0) and 1 × 1
(lower right, it equals b1a1). Hence −V 2 contains the monomial a2
n−1(b0)2(n−1)(b1a1)2.

The factor Cn−2,k is a linear function in the variables a3, . . ., an, with coeﬃcients depending
on a1 and a2. Indeed, set P∗ := b0(x − α)(x − β), 0 ̸= α ̸= β ̸= 0. One can choose (α, β)
as coordinates in the space (a1, a2). The polynomial P is obtained from P∗ by rescaling of its
coeﬃcients followed by (n − 2)-fold integration with constants of integration of the form ηsas,
ηs ∈ Q∗, s = 3, . . ., n. Consider the two conditions P (α, a)/αn−k = 0 and P (β, a)/βn−k = 0.
Each of them is a linear form in the variables a3, . . ., an, with coeﬃcients depending on a1 and
a2; the one of ak equals 1. The projection of the Maxwell stratum in the space of the variables
ak is given by the condition
 βn−kP (α, a) − α
n−kP (β, a) = 0 . (6)

Its left-hand side is a linear form in the variables a3, . . ., ak−1, ak+1, . . ., an, with coeﬃcients de-
pending on α and β. The presence of the monomial a2
n(b0)2k(b1a1)2(n−k) or a2
n−1(b0)2(n−1)(b1a1)2

in ˜Dn−2,k (see Lemma 19) implies that the factor Cn−2,k must be squared.
There remains to prove that sn−2,k = 1, see Remark 17. The left-hand side of equation (6)
is divisible by α − β. Represent this expression in the form (α − β)Q(α, β, a). The polynomial
Q depends in fact on α + β = −b1a1/b0, αβ = b2a2/b0 and a, hence this is a polynomial in a
(denoted by K(a)).
Clearly K depends linearly on the variables a3, . . ., an. On the other hand K is quasi-
homogeneous. Hence K is irreducible. Indeed, should K be the product of two factors, then one
of the two (denoted by Z) should not depend on any of the variables a3, . . ., an, i.e. Z should
be a polynomial in a1 and a2.
This polynomial should divide the coeﬃcients of all variables a3, . . ., an in K. But for
3 ≤ s ≤ n the coeﬃcient of as in K equals (see (6)) cs := (βn−kαn−s −αn−kβn−s)/(α−β). Hence
Z divides cs − βcs−1 = αn−s−1βn−k for all s ̸= k, and by symmetry Z divides αn−kβn−s−1 for
all s ̸= k. Hence Z = 1 and the polynomial Cn−2,k equals (βn−kP (α, a) − αn−kP (β, a))/(α − β).
Its quasi-homogeneous weight (QHW) is 2n − k − 1 (notation: QHW(Cn−2,k) = 2n − k − 1).
Indeed, one has to consider QHW(α) and QHW(β) to be equal to 1 because α and β are roots
of P∗ and their QHW is the same as the one of the variable x.
Obviously QHW( ˜Dn−2,k) = 2QHW(U )+QHW(W ) because ˜Dn−2,k = U (4U W − V 2) and
˜Dn−2,k is quasi-homogeneous. As U = ωa
n−k
2 , one has QHW(U ) = 2(n − k). The polynomial
˜Dn−2,k contains a monomial ˜ωan
2 , ˜ω ̸= 0 (see Proposition 1). This monomial is contained also
in W = ˜Dn−2|ak=0 hence QHW( ˜Dn−2) =QHW(W ) = 2n. Thus

QHW( ˜Dn−2,k) = 2QHW(U ) + QHW( ˜Dn−2) = 6n − 4k .

On the other hand one knows already that a priori ˜Dn−2,k = An−2,kBsn−2,k
n−2,k C 2
n−2,k, sn−2,k ∈ N,
An−2,k = an−k
2 . Hence

sn−2,kQHW(Bn−2,k) = QHW( ˜Dn−2,k) − QHW(An−2,k) − 2QHW(Cn−2,k)
= 6n − 4k − 2(n − k) − 2(2n − k − 1) = 2 ,

and as Bn−2,k = b2
1a2
1 − 4b0b2a2, one has QHW(Bn−2,k) = 2, so sn−2,k = 1.

15

Proof for k = 1 and k = 2. In order to deal with the cases k = 1 and k = 2 we need to know
the degrees and quasi-homogeneous weights of certain polynomials in the variables a:

Lemma 20. (1) dega1 ˜Dn−2 = n, dega2 ˜Dn−2 = n;
(2) QHW( ˜Dn−2) = 2n, QHW(∂ ˜Dn−2/∂a1) = 2n − 1, QHW(∂ ˜Dn−2/∂a2) = 2n − 2;
(3) QHW( ˜Dn−2,1) = n(3n − 2);
(4) QHW( ˜Dn−2,2) = 2n(n − 1);
(5) QHW(Bn−2,1) = n(n − 1), QHW(Bn−2,2) = n(n − 1);
(6) QHW(Cn−2,1) = n(n − 1), QHW(Cn−2,2) = n(n − 1)/2.

For k = 1 or 2 one has to ﬁnd positive integers u and v such that

QHW( ˜Dn−2,k) = (2 − k)n + uQHW(Bn−2,k) + vQHW(Cn−2,k) ,

because An−2,k = a2−k
n . For k = 2 parts (4), (5) and (6) of the lemma imply that u = 1,
v = 2 is the only possible choice. For k = 1 there remain two possibilities – (u, v) = (1, 2) or
(u, v) = (2, 1) – so we need another lemma as well:

Lemma 21. For aj = 0, j ̸= 1, n − 1, n, the polynomials ˜Dn−2, ˜Dn−2,1, Bn−2,1 and Cn−2,1 are
of the form respectively (with ∆i ̸= 0)

˜Dn−2 = ∆1anan
1 + ∆2anan−1a1 + ∆3a2
n , ˜Dn−2,1 = ∆4a2n−1
n an
n−1 + ∆5a3n−2
n ,

Bn−2,1 = ∆6an−1
n + ∆7an
n−1 and Cn−2,1 = ∆8an−1
n .

The lemma implies that it is possible to have (u, v) = (1, 2), but not (u, v) = (2, 1). Indeed,
otherwise the product ˜Dn−2,1 = An−2,1B2
n−2,1Cn−2,1, with An−2,1 = an, should contain three
diﬀerent monomials whereas it contains only two.

Proof of Lemma 20. Parts (1) and (2) follow directly from Proposition 1. To prove parts (3)
and (4) one has to observe that as the polynomial ˜Dn−2 contains a monomial c∗a2
n, c∗ ̸= 0,
the (2n − 1) × (2n − 1)-Sylvester matrices S∗
k := S( ˜Dn−2, ∂ ˜Dn−2/∂ak, ak), k = 1 or 2, contain
this monomial in positions (j, j + n), j = 1, . . ., n − 1 and only there. The matrix S∗
1 (resp.
S∗
2) has entries c†an, c† ̸= 0 (resp. c∗∗ ̸= 0) in positions (ν + n − 1, ν), ν = 1, . . ., n. Hence
˜Dn−2,k contains a monomial ±(c†an)n(c∗a2
n)n−1 for k = 1 and ±(c∗∗)n(c∗a2
n)n−1 for k = 2 whose
quasi-homogeneous weight is respectively n(3n − 2) and 2n(n − 1).
To prove part (5) recall that the (2n − 1) × (2n − 1)-Sylvester matrix S0 := S(Pn−2,k, P ′
n−2,k),
k = 1 or 2, has entries of the form c∗∗an, c∗∗ ̸= 0, in positions (j, j + n), j = 1, . . ., n − 1 and
only there, and constant nonzero terms in positions (ν + n − 1, ν), ν = 1, . . ., n. Thus Bn−2,k
contains a monomial ±c∗∗∗(an)n−1, c∗∗∗ ̸= 0 and QHW(Bn−2,k) = n(n − 1).
For the proof of part (6) we need to recall that the factors Cn−2,k are related to polynomials
P divisible by P∗. When one performs this Euclidean division one obtains a rest of the form
U †(a)x+V †(a), where U †, V † ∈ C[a], QHW(U †) = n−1, QHW(V †) = n, U † (resp. V †) contains
monomials ω1an−1
1 and ω2an−1 (resp. ω3an−2
1 a2 and ω4an), ωi ̸= 0. (To see that the monomials
ω1an−1
1 and ω3an−2
1 a2 are present one has to recall that at each step of the Euclidean division
one replaces a term Lxs, L ∈ C[a], by the sum −L(b1/b0)a1xs−1 − L(b2/b0)a2xs−2.)
To obtain the factor Cn−2,1 one has to eliminate a1 from the system of equations U †(a) =
V †(a) = 0, i.e. one has to ﬁnd the subset in the space of variables a1 for which U † and V †

have a common zero when considered as polynomials in a1. The (2n − 3) × (2n − 3)-Sylvester
matrix S(U †, V †, a1) contains terms ω2an−1 in positions (j, j + n − 1), j = 1, . . ., n − 2, and

16

terms ω3a2 in positions (ν + n − 2, ν), ν = 1, . . ., n − 1. Hence Cn−2,1 contains a monomial
±(ω2an−1)n−2(ω3a2)n−1, of quasi-homogeneous weight n(n − 1).
The proof of the second statement of part (6) is performed separately for the cases of even
and odd n. If n is even, then U † (resp. V †) contains monomials Ω1a1an/2−1
2 and Ω2an−1 (resp.
Ω3an/2
2 and Ω4an), Ωi ̸= 0. The (n − 1) × (n − 1)-Sylvester matrix S(U †, V †, a2) contains terms
Ω4an in positions (j, j +n/2), j = 1, . . ., n/2−1, and Ω1a1 in positions (ν +n/2−1, ν), ν = 1, . . .,
n/2. Hence Cn−2,2 contains a monomial ±(Ω4an)n/2−1(Ω1a1)n/2, of quasi-homogeneous weight
n(n − 1)/2.
When n is odd, then U † (resp. V †) contains monomials ˜Ω1a
(n−1)/2
2 and ˜Ω2an−1 (resp.
˜Ω3a1a
(n−1)/2
2 and ˜Ω4an), ˜Ωi ̸= 0. The (n − 1) × (n − 1)-Sylvester matrix S(U †, V †, a2) contains
terms ˜Ω2an−1 in positions (j, j + (n − 1)/2), j = 1, . . ., (n − 1)/2, and ˜Ω3a1 in positions
(ν +(n−1)/2, ν), ν = 1, . . ., (n−1)/2. Thus Cn−2,2 contains a monomial ±( ˜Ω2an−1 ˜Ω3a1)(n−1)/2,
of quasi-homogeneous weight n(n − 1)/2.

Proof of Lemma 21. One can develop det S(P, P∗) w.r.t. the last column in which there is a
single nonzero entry (an, in position (2, n + 2)). Hence ˜Dn−2 = (−1)nan det S♯, where S♯ :=
[S(P, P∗)]2,n+2. The last column of S♯ contains only two nonzero entries (an in position (1, n+1)
and b1a1 in position (n + 1, n + 1)), therefore

det S♯ = (−1)
nan det S♯1 + b1a1 det S♯2 , where S♯1 := [S♯]1,n+1 , S♯2 := [S♯]n+1,n+1 .

The matrix S♯1 is upper-triangular, with diagonal entries equal to b0, so det S♯1 = bn
0 , while S♯2

contains only two nonzero entries in its last column (an−1 in position (1, n) and b1a1 in position
(n, n)). Hence

det S♯2 = (−1)
n+1an−1 det S♯3 + b1a1 det S♯4 , where S♯3 := [S♯2]1,n , S♯4 := [S♯2]n,n .

The matrix S♯3 is upper-triangular, with diagonal entries equal to b0, so det S♯3 = b
n−1
0 . The
matrix S♯4 becomes lower-triangular after subtracting its second row multiplied by 1/b1 from
the ﬁrst one, with diagonal entries 1−b0/b1, b1a1, . . ., b1a1, from which the form of ˜Dn−2 follows.
Hence the (2n−1)×(2n−1)-Sylvester matrix S( ˜Dn−2, ∂ ˜Dn−2/∂a1, a1) has only the following
nonzero entries, in the following positions:

∆1an (j, j) , ∆2anan−1 (j, j + n − 1) , ∆3a2
n (j, j + n) ,

j = 1, . . . , n − 1,

n∆1an (ν + n − 1, ν) , ∆2anan−1 (ν + n − 1, ν + n − 1) , ν = 1, . . . , n .

One can subtract the (j + n − 1)st row from the jth one (j = 1, . . . , n − 1) to make disappear the
terms ∆2anan−1 in positions (j, j + n − 1). This does not change the determinant; the entries
∆1an in positions (j, j) become (1 − n)∆1an. The form of ˜Dn−2,1 follows now from Lemma 8.
For aj = 0, j ̸= 1, n − 1, n, the polynomial Pn−2,1 is of the form α1xn + α2an−1x + α3an,
αi ̸= 0, so the (2n − 1) × (2n − 1)-Sylvester matrix S(Pn−2,1, P ′
n−2,1) has nonzero entries only

17

α1 at (j, j) , α2an−1 at (j, j + n − 1) , α3an at (j, j + n) , j = 1, . . . , n − 1,

nα1 at (ν, ν) , α2an−1 at (ν, ν + n − 1) , ν = 1, . . . , n .

By analogy with the reasoning about ˜Dn−2,1 one ﬁnds that Bn−2,1 = ∆6an−1
n + ∆7an
n−1.
To justify the form of Cn−2,1 it suﬃces to observe that for aj = 0, j ̸= 1, n − 1, n, one has
(see the deﬁnition of U † and V † in the proof of Lemma 20) U † = α4an−1 + α5an−1
1 , V † = α6an,
αi ̸= 0, so dega1 U † = n−1 and dega1 V † = 0. When eliminating a1 from the system of equalities
U † = V † = 0 one obtains Res(U †, V †, a1) = 0, i.e. (α6an)n−1 = 0.

6 The proof of sm,1 = 1

In the present section we prove the following

Proposition 22. With the notation of Remark 17 one has sm,1 = 1.

The proof of the proposition makes use of the following lemma:

Lemma 23. Set aj = 0 for j ̸= 1, ℓ and n, where n − m + 1 ≤ ℓ ≤ n − 1. Then S(P, P∗) is of
the form Ω1an−m−1
n an
1 + Ω2an−m−1
n aℓa
n−ℓ
1 + Ω3an−m
n .

Proof of Proposition 22: Lemma 23 with ℓ = n − 1 implies that the matrix S( ˜Dm, ∂ ˜Dm/∂a1, a1)
has only the following nonzero entries, in the following positions:

Ω1an−m−1
n (j, j) , Ω2an−m−1
n an−1 (j, j + n − 1) ,

Ω3an−m
n (j, j + n) , j = 1, . . . , n − 1 ,

nΩ1an−m−1
n (ν + n − 1, ν) , Ω2an−m−1
n an−1 (ν + n − 1, ν + n − 1) ,

ν = 1, . . . , n .

Subtract for j = 1, . . ., n−1 its (j +n−1)st row from the jth one. This preserves its determinant
and leaves only the following nonzero entries, in the following positions:

(1 − n)Ω1an−m−1
n (j, j) , Ω3an−m
n (j, j + n) ,

j = 1, . . . , n − 1 ,

nΩ1an−m−1
n (ν + n − 1, ν) , Ω2an−m−1
n an−1 (ν + n − 1, ν + n − 1) ,

ν = 1, . . . , n .

The new matrix satisﬁes the conditions of Lemma 8 with p = 2n − 1, s = n. Hence its
determinant is of the form
 a(n−m−1)(2n−1)
n (Ω4an
n−1 + Ω5a
n−1
n ) , (7)

where Ω4 = ((1 − n)Ω1)n−1Ωn
2 and Ω5 = ±Ωn−1
3 Ωn
1 . The polynomial Res(Pm,1, P ′
m,1) contains
monomials αan−1
n and βan
n−1, α ̸= 0 ̸= β; this can be proved by complete analogy with the

18

analogous statement of Proposition 1 with m = 1 and we leave the proof for the reader. Hence
the polynomial (7) is not divisible by a power of Res(Pm,1, P ′
m,1) higher than 1, because in this
case it would contain at least three diﬀerent monomials in an and an−1. Thus sm,1 = 1.

Proof of Lemma 23: The matrix S(P, P∗) has only the following nonzero entries, in the following
positions:
 1 (j, j) , a1 (j, j + 1) , aℓ (j, j + ℓ) ,

an (j, j + n) , j = 1, . . . , n − m ,

b0 (ν + n − m, ν) , b1a1 (ν + n − m, ν + 1) , ν = 1, . . . , n .

One can develop the determinant n − m − 1 times w.r.t. the last column in which each time
there will be a single nonzero entry an. Thus det S(P, P∗) = ±an−m−1
n det S‡, where the ﬁrst row
of S‡ contains the entries 1, a1, aℓ and an in positions respectively (1, 1), (1, 2), (1, ℓ + 1) and
(1, n + 1); its second row is of the form (b0, b1a1, 0, . . ., 0) and the next rows are the consecutive
shifts of this one by one position to the right. Developing of det S‡ w.r.t. the last column yields

det S‡ = (−1)
nan det[S‡]1,n+1 + b1a1 det[S‡]n+1,n+1 .

The matrix [S‡]1,n+1 is upper-triangular, with diagonal entries equal to b0 (hence det[S‡]1,n+1 =
bn
0 ). The determinant of the matrix S‡‡ := [S‡]n+1,n+1 can be developed n − ℓ − 1 times w.r.t.
its last column, where each time it has a single nonzero entry b1a1 in its right lower corner:

det S‡‡ = (b1a1)
n−ℓ−1 det S∗† ,

where S∗† is (ℓ + 1) × (ℓ + 1); it is obtained by deleting the last n − ℓ − 1 rows and columns of
S‡‡. The determinant det S∗† can be developed w.r.t. its last column:

det S∗† = (−1)
ℓaℓ det[S∗†]1,ℓ+1 + b1a1 det[S∗†]ℓ+1,ℓ+1 .

The matrix [S∗†]1,ℓ+1 (resp. [S∗†]ℓ+1,ℓ+1) is upper-triangular, with diagonal entries equal to b0,
so its determinant equals bℓ
0 (resp. becomes lower-triangular (after subtracting its second row
multiplied by 1/b1 from its ﬁrst row), with diagonal entries equal to 1 − b0/b1, b1a1, . . ., b1a1,
so its determinant equals (1 − b0/b1)(b1a1)ℓ−1). This implies the lemma.

7 Completion of the proof of Theorem 4

Statement 24. If formula (1) is true for n = n0, k = k0, then it is true for n = n0 + 1,
k = k0 + 1.

Statement 25. If formula (1) is true for n = n0, m = n0 − 2, k = 1, then it is true for n = n0,
2 ≤ m < n0 − 2, k = 1.

Proof of Statement 24: Recall that we have shown already (see Remark 17) that for each n
ﬁxed the polynomials ˜Dm,k (2 ≤ m ≤ n − 2, 1 ≤ k ≤ n) are of the form Am,kBsm,k
m,k C rm,k
m,k ,
sm,k, rm,k ∈ N. Suppose that for 4 ≤ n ≤ n0 one has sm,k = 1, rm,k = 2. (Using MAPLE one
can obtain this result for n0 = 4.) Set P (a, x) := xn0 + a1xn0−1 + · · ·+ an0, a := (a1, . . . , an0) and
consider the polynomials F := uxn0+1 +P and F∗ := b−1uxn0−m+1 +P∗, u ∈ (C, 0), 0 ̸= b−1 ̸= bj
for 0 ≤ j ≤ n0 − m. They are deformations respectively of P and P∗. Our reasoning uses the
following
 19

Observation 26. One has

F = u(xn0+1 + xn0/u + ∑n0−1
j=0 (an−j/u)xj) ,

F∗ = u(b−1xn0−m+1 + b0xn0−m/u + ∑n0−1
j=0 (bn−jan−j/u)xj ) ,

so after the change of parameters ˜a1 = 1/u, ˜as = as−1/u, s = 2, . . ., n0 (which is well-deﬁned
for u ̸= 0) and the shifting by 1 of the indices of the constants bj, the polynomials F and F∗
(up to multiplication by 1/u) become P and P∗ deﬁned for n0 + 1 instead of n0.

Lemma 27. The zero set of Res(F, F∗) for u ̸= 0 is deﬁned by an equation of the form ˜Dm +
uH/d = 0, where H ∈ C[u, a] and d ̸= 0.

Proof. Consider the (2n0 − m + 2) × (2n0 − m + 2)-Sylvester matrix ˜S := S(F, F∗). Permute
the rows of ˜S as follows: place the (n0 − m + 2)nd row in second position while shifting the
ones with indices 2, . . ., n0 − m + 1 by one position backward. This preserves up to a sign the
determinant and yields a matrix T which we decompose in four blocks the diagonal ones being
of size 2 × 2 (upper left, denoted by T ∗) and (2n0 − m) × (2n0 − m) (lower right, denoted by
T ∗∗); the left lower block is denoted by T 0 and the right upper by T 1. An easy check shows that

T ∗ = ( u 1
b−1u b0
 ) , T ∗∗|u=0 = S(P, P∗) ,

and that the only nonzero entries of the left lower block T 0 are u and b−1u, in positions (3, 2)
and (n0 − m + 3, 2) respectively.
Divide the ﬁrst column of T by u (we denote the thus obtained matrix by T †). This does not
change the zero set of det T for u ̸= 0. For u = 0 the matrix T † is block-upper-triangular, with

diagonal blocks equal to ( 1 1
b−1 b0
 ) and S(P, P∗). Hence det T † = d det S(P, P∗) + uH(u, a),

d := det T ∗|u=0 = b0 −b−1 ̸= 0, H ∈ C[u, a]. Thus the zero set of Res(F, F∗) for u ̸= 0 suﬃciently
small is deﬁned by the equation ˜Dm + uH/d = 0.

For u ̸= 0 (resp. for u = 0) the quantity det T † is a degree n0−m+1 (resp. n0−m) polynomial
in ak for k = n0 − m + 1, . . ., n0, and a degree n0 + 1 (resp. n0) polynomial in ak for k = 1, . . .,
n0 − m, see Proposition 1. Hence for each k = 1, . . ., n0 there is one simple root −1/wk(u, a) of
Res(F, F∗) that tends to inﬁnity as u → 0. Thus one can set Res(F, F∗) = (1 + wk(u, a)ak) ˜D∗
m,
where ˜D∗
m|u=0 ≡ ˜Dm and degak ˜D∗
m = n0 − m (resp. n0) for k = n0 − m + 1, . . ., n0 (resp. for
k = 1, . . ., n0 − m).

Lemma 28. Set Em :=Res(F, F∗) and ˜D∗
m,k :=Res(Em, ∂Em/∂ak, ak). Then for u ̸= 0 one has
˜D∗
m,k = Ω♭♭(a2(n0−m−k)
n0 ˜Dm,k + uHm,k(u, a)), where Hm,k ∈ C[u, a].

Remark 29. One can set u := a2(n0−m−k)
n0 v to obtain the equality

˜D∗
m,k = Ω♭♭a2(n0−m−k)
n0 ( ˜Dm,k + vHm,k(a2(n0−m−k)
n0 v, a)) .

Now in a neighbourhood of each an0 ̸= 0 ﬁxed the zero set of ˜D∗
m,k is deﬁned by the equation
˜Dm,k + vHm,k(a
2(n0−m−k)
n0 v, a) = 0, i.e. by deforming the equation ˜Dm,k = 0.

20

Proof of Lemma 28: Indeed, Proposition 1 implies that ˜Dm contains a monomial Ω♭a
n0
k an0−m−k
n0 ,
1 ≤ k ≤ n0 − m (resp. Ω♭a
n0−m
k an0−k
n0−m, n0 − m + 1 ≤ k ≤ n0) and this is the only monomial
containing a
n0
k (resp. an0−m
k ). Similarly, Em contains a monomial I := uk+1Ω♮a
n0+1
k an0−m−k
n0 ,
1 ≤ k ≤ n0 − m (resp. J := uk+1Ω♮a
n0−m+1
k an0−k
n0−m, n0 − m + 1 ≤ k ≤ n0) and this is the
only monomial containing a
n0+1
k (resp. an0−m+1
k ). (The monomial I is obtained as follows: one
subtracts for ν = 1, . . ., n0 − m + 1 the (ν + n0 − m + 1)st row multiplied by 1/bk from the νth
one to make disappear the terms ak in the ﬁrst n0 − m + 1 rows. The monomial I is the product
of the terms bkak in the last n0 + 1 rows, the terms (1 − 1/bk)u in the ﬁrst k + 1 rows and the
terms an0 in the next n0 − m − k rows. The monomial J is obtained in a similar way. One has to
assume that QHW(u) = −1.) Knowing that degak Em = n0 + 1 (resp. degak Em = n0 − m + 1)
for u ̸= 0 and that degak ˜Dm = n0 (resp. degak ˜Dm = n0 − m) one concludes that

Em = uk+1Ω♮an0+1
k an0−m−k
n0 + Ω♭a
n0
k an0−m−k
n0 + uE∗(u, a)

(resp. Em = uk+1Ω♮a
n0−m+1
k an0−k
n0−m + Ω♭an0−m
k a
n0−k
n0−m + uE∗∗(u, a) ) ,

where E∗, E∗∗ ∈ C[u, a], degak E∗ ≤ n0, degak E∗∗ ≤ n0 − m. The Sylvester matrix S(Em,
∂Em/∂ak, ak) is (2n0 + 1) × (2n0 + 1) (resp. (2n0 − 2m + 1) × (2n0 − 2m + 1)). We permute its
rows by placing the (n0 + 1)st (resp. (n0 − m + 1)st) row in second position while shifting by
one position backward the second, third, . . ., n0th (resp. (n0 − m)th) rows. The new matrix T ♭

can be block-decomposed, with diagonal blocks T uℓ (2 × 2, upper left) and T ℓr; the other two
blocks are denoted by T ur and T ℓℓ. Hence

T uℓ =
 

 uk+1Ω♮an0−m−k
n0 Ω♭an0−m−k
n0 + uX 1(u, a)

(n0 + 1)uk+1Ω♮an0−m−k
n0 n0Ω♭an0−m−k
n0 + uX 2(u, a)
 

 ,

(resp. T uℓ =
 

 uk+1Ω♮an0−m−k
n0 Ω♭an0−m−k
n0 + uX 3(u, a)

(n0 − m + 1)uk+1Ω♮an0−m−k
n0 (n0 − m)Ω♭an0−m−k
n0 + uX 4(u, a)
 

 ) ,

X i ∈ C[u, a]. One has T ℓr|u=0 = S( ˜Dm, ∂ ˜Dm/∂ak, ak). The block T ℓℓ has just two nonzero
entries, in its second column, and T ℓℓ|u=0 = 0. The ﬁrst of these entries is in position (3, 2) and
equals uk+1Ω♮an0−m−k
n0 (resp. uk+1Ω♮an0−m−k
n0 ). The second of them is in position (n0 + 2, 2)
(resp. (n0 − m + 2, 2)) and equals (n0 + 1)uk+1Ω♮an0−m−k
n0 (resp. (n0 − m + 1)uk+1Ω♮an0−m−k
n0 ).
Thus for u = 0 ̸= an0 the zero set of ˜D∗
m,k is the one of ˜Dm,k. For u ̸= 0 small enough
this set does not change if one divides the ﬁrst column of the matrix T ♭ by uk+1. We denote
the new matrix by T ♭∗. Obviously det T ♭∗ = −Ω♮Ω♭(a2(n0−m−k)
n0 ˜Dm,k + uHm,k) (resp. det T ♭∗ =
−Ω♮Ω♭(a2(n0−m−k)
n0 ˜Dm,k + uHm,k)) for a suitably deﬁned polynomial Hm,k which proves the
lemma.

Further to distinguish between the sets Θ and ˜M (see Deﬁnition 3) deﬁned for the polyno-
mials P or F we write ΘP and ˜MP or ΘF and ˜MF . Consider a point A ∈ ΘP and a germ G of an
aﬃne space of dimension 2 which intersects ΘP transversally at A. Hence there exists a compact
neighbourhood N of A in the space A such that the parallel translates of G which intersect ΘP
at points of N , intersect ΘP transversally at these points. We assume that the value of |an0|
remains ≥ ρ in N for some ρ > 0. The restrictions of ˜Dm,k to each of these translates are

21

smooth analytic functions each of which has one simple zero at its intersection point with ΘP ;
this follows from the factor Bm,k participating in power 1 in formula (1) for n = n0. Hence
for all u ∈ C with 0 < |u| ≪ ρ the restriction of ˜D∗
m,k to these translates are smooth analytic
functions having simple zeros at the intersection points of the translates with ΘP .
But this means that the power of the factor Bm,k in formula (1) applied to the polynomial
F is equal to 1 on the intersection of ΘF with some open ball of dimension n0 + 1 centered at
(0, A) in the space of the variables (u, a). Hence this power equals 1 on some Zariski open dense
subset Θ0 of ΘF (if its complement ΘF \Θ0 is nonempty, then on Θ0 this power might be > 1).
Thus the equality sm,k = 1 is justiﬁed for n = n0 + 1, 2 ≤ k ≤ n0 + 1 (because it is the coeﬃcient
of xn0−k, not of xn0+1−k of F , that equals ak).
Now we adapt the above reasoning to the situation, where instead of a point A ∈ ΘP one
considers a point A ∈ ˜MP . Each of the translates of G intersects ˜MP transversally, at just one
point. The restriction of ˜Dm,k to the translate is a smooth analytic function having a double
zero, so a priori the restriction of ˜D∗
m,k to it has either one double or two simple zeros. (Under
an analytic deformation a double zero either remains such or splits into two simple zeros.)
However two simple zeros is impossible because these zeros would be two points of ˜MP whereas
the translate contains just one point. Thus the power 2 of the factor Cm,k is justiﬁed for some
Zariski open dense subset of ˜MF . Once again, this is suﬃcient to claim that formula (1) is valid
for n = n0 + 1 and for 2 ≤ k ≤ n0 + 1.

Proof of Statement 25: Recall that by Remark 17 we have to show that for n = n0 one has
sm,k = 1, rm,k = 2. The ﬁrst of these equalities was proved in Section 6 (see Proposition 22), so
there remains to prove the second one.
As in the proof of Statement 24 we set P (a, x) := xn0 +a1xn0−1 +· · ·+an0, a := (a1, . . . , an0).
We deﬁne the polynomial P∗ := x2 + b1a1x + b2a2 to correspond to the case m = n0 − 2 (i.e.
bk ̸= 0, 1, b3−k for k = 1, 2). For m = n0 −2 Theorem 4 is proved in Section 5, so we assume that
m < n0 − 2 and we set G := xn0−m−2P∗ + u(b3a3xn0−m−3 + · · · + bn0−man0−m), where u ∈ (C, 0)
and for i, j ≥ 3, i ̸= j, one has 0 ̸= bi ̸= bj ̸= 0. Denote by G♯ the (2n0 − m) × (2n0 − m)-matrix
S(P, G).

Lemma 30. One has det G♯|u=0 = an0−m−2
n0 det S(P, P∗) = an0−m−2
n0 ˜D2. Hence ˜G := det G♯ =
an0−m−2
n0 ˜D2 + uH ♯(u, a), H ♯ ∈ C[u, a].

Proof. All nonzero entries of the matrix G♯ in the intersection of its last n0 − m − 2 columns and
rows are 0 for u = 0. One can develop n0 − m − 2 times det G♯|u=0 w.r.t. its last column; each
time there is a single nonzero entry in it which equals an0. The matrix obtained from G♯|u=0
by deleting its last n0 − m − 2 columns and the rows with indices m + 2, . . ., n0 − 1 is precisely
S(P, P∗).

One can observe that det G♯ and det G♯|u=0 are both degree n0 polynomials in a1. Assume
that an0 belongs to a closed disk on which one has |an0| ≥ ρ♭ > 0. Suppose that |u| ≪ ρ♭, so
one can consider the quantity ˜D2 + (u/an0−m−2
n0 )H ♯(u, a) as a deformation of ˜D2. To this end
we set u := an0−m−2
n0 v, v ∈ (C, 0), see Remark 29. Now to prove Statement 25 one has just to
repeat the reasoning from the last paragraph of the proof of Statement 24.

22

References

[1] A. Albouy and Y. Fu, Some Remarks About Descartes Rule of Signs, Elemente der Math-
ematik 69 (2014), 186-194.

[2] W. Castryck, R. Laterveer and M. Ouna¨ıes, Constraints on counterexamples to the Casas-
Alvero conjecture and a veriﬁcation in degree 12, Mathematics of Computation Vol. 83, No.
290, (2014) 3017-3037.

[3] H. Ezzaldine, K. Houssam, M. Hossein and M. Sarrage, Overdetermined strata for degree
5 hyperbolic polynomials. Vietnam J. Math. 43, no. 1 (2015) 139-150.

[4] H. Ezzaldine and V.P. Kostov, Even and old overdetermined strata for degree 6 hyperbolic
polynomials. Serdica Math. J. 34, no. 4 (2008) 743-770.

[5] J. Forsg˚ard, V.P. Kostov and B.Z. Shapiro, Could Ren´e Descartes have known this?, Ex-
perimental Mathematics vol. 24, issue 4 (2015) 438-448.

[6] V.P. Kostov, Topics on hyperbolic polynomials in one variable. Panoramas et Synth`eses 33
(2011), vi + 141 p. SMF.

[7] V.P. Kostov, Some facts about discriminants, Comptes Rendus Acad. Bulg. Sci. (to appear).

[8] V.P. Kostov, A property of discriminants, arXiv:1701.02912.

[9] V.P. Kostov, On polynomial-like functions, Bulletin des Sciences Math´ematiques 129, No.
9 (2005) 775-781.

[10] V.P. Kostov, Root arrangements of hyperbolic polynomial-like functions, Revista
Matem´atica Complutense vol. 19, No. 1 (2006) 197-225.

[11] V.P. Kostov, On hyperbolic polynomial-like functions and their derivatives, Proc. Royal
Soc. Edinb. 137A (2007) 819-845.

[12] V.P. Kostov, On root arrangements for hyperbolic polynomial-like functions
and their derivatives, Bulletin des Sciences Math´ematiques 131 (2007) 477-492,
doi:10.1016/j.bulsci.2006.12.004.

[13] V.P. Kostov and B.Z. Shapiro, On arrangement of roots for a real hyperbolic polynomial
and its derivatives, Bulletin des Sciences Math´ematiques 126, No. 1 (2002) 45-60.

[14] I. M´eguerditchian, G´eom´etrie du Discriminant R´eel et des Polynˆomes Hyperboliques, Th`ese
de Doctorat (soutenue le 24 janvier 1991 `a Rennes).

[15] S. Yakubovich, The validity of the Casas-Alvero conjecture, arXiv:1504.00274v1 [math.CA]
1 April 2015.

[16] S. Yakubovich, On some properties of the Abel-Goncharov polynomials and the Casas-
Alvero problem, Integral Transforms Spec. Funct. 27, no. 8 (2016) 599-610.

[17] S. Yakubovich, Polynomial problems of the Casas-Alvero type, J. Class. Anal. 4, no. 2
(2014) 97-120.
 23
