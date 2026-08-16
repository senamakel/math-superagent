<!-- source: https://arxiv.org/pdf/2405.10352 | converted from PDF -->

arXiv:2405.10352v3  [math.NT]  31 Aug 2024
SUMS OF BINOMIAL COEFFICIENTS IN PASCAL’S TRIANGLE TAKEN
MODULO p AND THEIR RELATION TO GROUPS OF EXPONENT pn

FERNANDO SZECHTMAN

Abstract. We give a simple matrix-based proof of congruence equations modulo a prime p
involving sums of binomial coeﬃcients appearing in Pascal’s triangle. These equations can be
used to construct some groups of exponent pn. These groups, as well as others of exponent pn+1,
explain why p = 2 is not really an exceptional prime in relation to the Heisenberg group over
the ﬁeld with p elements.
 1. Introduction

It is common for the prime 2 to play the role of villain in Mathematics. We consider one such a
case and then we use the sum of binomial coeﬃcients appearing in Pascal’s triangle taken modulo
a prime to show that, in fact, all primes behave in the exactly the same manner.
Some notation is required for this purpose. We ﬁx throughout p, m ∈ N, with p a prime, and
write F for the ﬁeld with p elements. We let J ∈ Mm(F ) and A = I + J ∈ Mm(F ) stand for
the upper triangular Jordan blocks with eigenvalues 0 and 1, respectively. We also ﬁx an F -vector
space V of dimension m. For v ∈ V and γ ∈ End(V ), we write vγ = vγ for the result of applying
γ to v. In keeping with this notation function composition is considered from left to right, and
the matrix of an endomorphism of V relative to a basis of V is constructed row by row instead
of column by column. Let G be a group. If x, y ∈ G, we write x
y = y−1xy. If G is ﬁnite, its
exponent is the smallest natural number m such that x
m = 1 for all x ∈ G. Given a subgroup H
of Aut(G), we write Hol(G, H) for the holomorph of G relative to H. This is the group having
(copies of) G and H as subgroups, with G normal, G ∩ H trivial, Hol(G, H) = HG, and if g ∈ G
and α ∈ H, then α
−1gα = gα is the result of applying α to g. If H = ⟨α⟩, we write Hol(G, α)
instead of Hol(G, H).
Consider the Heisenberg group H(p), namely the group of all 3 × 3 upper triangular matrices
with 1’s along the main diagonal. Then H(p) ∼= Hol(V, α), where m = 2 and α ∈ GL(V ) can be
represented by A relative to some basis of V . It is well known and easy to see that the exponent
of H(p) is p when p is odd and 4 when p = 2. The reason for this dichotomy is the fact that
1 + · · · + p − 1 is congruent to 0 or 1 modulo p depending on whether p is odd or p = 2, respectively.
There seems to be nothing that can salvage the prime 2 from its unique role in this setting.
However, a wider view of Pascal’s triangle reveals that all primes are equally exceptional.
Perhaps the two most well-known results concerning binomial coeﬃcients and their divisibility
by a given prime are the following theorems of Kummer [K] and Lucas [L].

Theorem (Kummer). Let p be a prime. Given integers 0 ≤ m ≤ n the number of times that p
divides the binomial coeﬃcient ( n
m) is the amount of carries when adding m and n − m in base p.

2020 Mathematics Subject Classiﬁcation. 11B65, 11A07, 20D15, 05A10.
Key words and phrases. Pascal’s triangle, binomial coeﬃcients, groups of prime-power exponent.
The author was partially supported by NSERC grant 2020-04062.

1

2 FERNANDO SZECHTMAN

Theorem (Lucas). Let p be a prime. Given integers 0 ≤ m ≤ n, such that m = (mℓ . . . m1m0)p
and m = (nℓ . . . n1n0)p, we have ( n
m
) ≡ Π
0≤i≤ℓ
( ni
mi
) mod p,

where (0
0
) = 1 and (
a
b) = 0 if a < b.

In these note we are concerned with sums of binomial coeﬃcients when taken modulo a prime,
with an application to group theory.

2. Congruence equations mod p in Pascal’s triangle and groups of exponent pn

Proposition 2.1. Suppose that n ∈ N satisﬁes m < pn. Then

(1) I + A + · · · + A
p
n−1 = 0.

Proof. The minimal polynomial of A is (X − 1)
m, which is a factor of

(2) 1 + X + · · · + X p
n−1 = (X p
n − 1)/(X − 1) = (X − 1)
p
n /(X − 1) = (X − 1)
p
n−1.
 □

Proposition 2.2. Suppose that n ∈ N and i ∈ Z satisfy 0 ≤ i < pn − 1, and set

Spn,i = (i
i

) + (
i + 1
i
 ) + · · · + (
pn − 1
i
 )
.

Then

(3) Spn,i ≡ 0 mod p.

Proof. Take m = pn − 1. Then I + A + · · · + A
p
n−1 = 0 by Proposition 2.1. On the other hand

(4) I + A + · · · + A
p
n−1 = Spn,0 · I + Spn,1 · J + · · · + Spn,pn−2 · J p
n−2 + Spn,pn−1 · J p
n−1.

For 0 ≤ i < pn − 1, J i is the upper triangular matrix with 1’s along the ith superdiagonal and 0’s
everywhere else. Thus, I, J, . . . , J p
n−2 are linearly independent over F . Since J p
n−1 = 0, it follows
that Spn,i ≡ 0 mod p for all 0 ≤ i < pn − 1. □

Note that if n ∈ N and m = pn − 1, then making use of (4), the linear independence of
I, J, . . . , J p
n−2, and J p
n−1 = 0, the equations (1) and (3) become equivalent to each other.

Proposition 2.3. Suppose that n ∈ N satisﬁes pn−1 < m ≤ pn. Let α ∈ GL(V ) be an automor-
phism of V that is represented by A with respect to some basis of V , and set G = Hol(V, α). Then
G has order pm+n and exponent pn if m < pn and pn+1 if m = pn.

Proof. The minimal polynomial of A is (X − 1)
m. This is not a factor of (X − 1)
p
n−1 = X p
n−1 − 1,
but it is a factor of (X − 1)
p
n = X p
n − 1, so α
p
n−1 ̸= 1 but α
p
n = 1. Thus the order of α is pn. As
|V | = pm, it follows that |G| = pm+n.
Let v ∈ V and β ∈ ⟨α⟩. Then β = α
i for some i ∈ N, so that i = psj, where j ∈ N, s ≥ 0,
and gcd(p, j) = 1. Clearly, βp
n = 1. Set γ = α
j. As gcd(p, j) = 1, then α is similar to γ, so
γ can also be represented by A relative to some other basis, say B = {v1, . . . , vm}, of V . Set
δ = 1 + γ + · · · + γp
n−1 and ǫ = δp
s, so that 1 + β + · · · + βp
n−1 = ǫ and therefore

(5) (βv)
p
n = βp
n vǫ = vǫ.

Suppose ﬁrst that m < pn. Then δ = 0 by Proposition 2.1, so (βv)
p
n = 1 by (5), whence the
exponent of G is exactly pn. Suppose next that m = pn. Then by (5),

(βv)
p
n+1 = (vǫ)
p = 1.

SUMS OF BINOMIAL COEFFICIENTS MODULO p AND GROUPS OF EXPONENT p
n 3

Let E ∈ Mm(F ) be the matrix having a 1 in position (1, m) and 0’s elsewhere. Then (A − 1)
p
n−1 =
J p
n−1 = E, so (2) ensures that δ is represented by E relative to B, whence

(γv1)
p
n = γp
nv1+γ+···+γpn−1

1 = vδ
1 = vm.

Therefore the exponent of G is precisely pn+1. □

Observe that when m < pn the fact that the exponent of G is pn is equivalent to (1) and (3).
Notice also if n = 1 and m = 2, then any odd prime p satisﬁes pn−1 < m < pn and G ∼= H(p).
Note as well that if n = 1 and m = 2, then p = 2 satisﬁes m = pn and G ∼= H(p).

References

[K] E. Kummer, ¨Uber die Erg¨anzungss¨atze zu den allgemeinen Reciprocit¨atsgesetzen, Journal f¨ur die
reine und angewandte Mathematik 44 (1852) 93—146.
[L] ´E. Lucas, Sur les congruences des nombres eul´eriens et les coeﬃcients diﬀ´erentiels des functions
trigonom´etriques suivant un module premier, Bulletin de la Soci´et´e Math´ematique de France 6
(1878) 49—54.

Department of Mathematics and Statistics, University of Regina, Canada
Email address: fernando.szechtman@gmail.com
