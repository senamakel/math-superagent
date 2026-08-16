<!-- source: https://arxiv.org/pdf/1308.5320 | converted from PDF -->

arXiv:1308.5320v5  [math.CA]  13 Dec 2019
POLYNOMIAL PROBLEMS OF THE CASAS-ALVERO TYPE

S. YAKUBOVICH

ABSTRACT. We establish necessary and sufﬁcient conditions for an arbitrary polynomial of degree n, espe-
cially with only real roots, to be trivial, i.e. to have the form a(x − b)n. To do this, we derive new properties
of polynomials and their roots. In particular, it concerns new bounds and genetic sum representations of the
Abel -Goncharov interpolation polynomials. Moreover, we prove the Sz.-Nagy type identities, the Laguerre and
Obreshkov-Chebotarev type inequalities for roots of polynomials and their derivatives. As applications these
results are associated with the known problem, conjectured by Casas- Alvero in 2001, which says, that any com-
plex univariate polynomial, having a common root with each of its non-constant derivative must be a power of a
linear polynomial. We investigate particular cases of the problem, when the conjecture holds true or, possibly, is
false.
 1. INTRODUCTION AND PRELIMINARY RESULTS

It is well known from elementary calculus that an arbitrary polynomial f with complex coefﬁcients (com-
plex polynomial) of degree n ∈ N

f (z) = a0z
n + a1z
n−1 + · · · + an−1z + an, a0 ̸= 0, (1)

having a root λ ∈ C of multiplicity µ, 1 ≤ µ ≤ n, shares it with each of its derivatives up to order µ − 1, but
f (µ)(λ) ̸= 0. When λ is a unique root of f , it has the form f (z) = a(z − λ)n, µ = n and λ is the same root
of each derivative of f up to order n − 1. We will call such a polynomial a trivial polynomial. Obviously,
as it follows from the fundamental theorem of algebra, f has at least two distinct roots, i.e. a polynomial of
degree n is non-trivial, if and only if its maximum multiplicity of roots r does not exceed n − 1.
In 2001 Casas- Alvero [1] conjectured that an arbitrary polynomial f degree n ≥ 1 with complex coef-
ﬁcients is of the form f (z) = a(z − b)
n, a, b ∈ C, if and only if f shares a root with each of its derivatives
f (1), f (2), . . . , f (n−1).
We will call a possible non-trivial polynomial, which has a common root with each of its non-constant
derivatives a CA-polynomial. The conjecture says that there exist no CA-polynomials. The problem is still
open. However, it is proved for small degrees, for inﬁnitely many degrees, for instance, for all powers n,
when n is a prime (see in [2], [3], [4] ). We observe that such a kind of CA-polynomial of degree n ≥ 2
cannot have all distinct roots since at least one root is common with its ﬁrst derivative. Therefore it has a
multiplicity at least 2 and a maximum of possible distinct roots is n − 1.
Our main goal here is to derive necessary and sufﬁcient conditions for an arbitrary polynomial (1) to
be trivial. For example, solving a simple differential equation of the ﬁrst order, we easily prove that a
polynomial is trivial, if and only if it is divisible by its ﬁrst derivative. In the sequel we establish other
criteria, which will guarantee that an arbitrary polynomial has a unique joint root.

Date: December 16, 2019.
2000 Mathematics Subject Classiﬁcation. Primary 26C05, 12D10, 41A05 ; Secondary 13F20 .
Key words and phrases. Casas-Alvero conjecture, Abel-Goncharov polynomials, polynomial ring, Rolle theorem, Vi´ete formulas,
Sz.-Nagy identities, Laguerre inequalities.
 1

2 S. YAKUBOVICH

Without loss of generality one can assume in the sequel that f is a monic polynomial of degree n, i.e.
a0 = 1 in (1). Generally, it has k distinct roots λj of multiplicities r j, j = 1, . . . , k, 1 ≤ k ≤ n such that

r1 + r2 + . . .rk = n (2).

By r we will denote the maximum of multiplicities (2), r = max1≤ j≤k(r j), r0 = min1≤ j≤k(r j) and by
ξ (m)
ν , ν = 1, . . . , n − m the zeros of the m-th derivative f (m), m = 1, . . . , n − 1. For further needs we specify
zeros of the n − 1st and n − 2nd derivatives, denoting them by ξ (n−1)
1 = zn−1 and ξ (n−2)
2 = zn−2, respectively.
It is easy to ﬁnd another zero of the n − 2-th derivative, which is equal to ξ (n−2)
1 = 2zn−1 − zn−2. When
zeros zn−1, zn−2 are real we write, correspondingly, xn−1, xn−2. The value zn−1 is called the centroid. It is a
center of gravity of roots and by Gauss-Lucas theorem it is contained in the convex hull of all non-constant
polynomial derivatives (see details in [5]).
The paper is structured as follows: In Section 2 we study properties of the Abel-Goncharov interpo-
lation polynomials, including integral and series representations and upper bounds. Section 3 deals with
the Sz.-Nagy type identities and Obreshkov-Chebotarev type inequalities for roots of polynomials and their
derivatives. As applications new criteria are found for an arbitrary polynomial with only real roots to be
trivial. Section 4 is devoted to the Laguerre type inequalities for polynomials with only real roots to localize
their zeros. The ﬁnal Section 5 contains applications of these results towards solution of the Casas-Alvero
conjecture and its particular cases.

2. ABEL-GONCHAROV POLYNOMIALS, THEIR UPPER BOUNDS AND INTEGRAL AND GENETIC SUM’S
REPRESENTATIONS

We begin, choosing a sequence of complex numbers (repeated terms are permitted) z0, z1, z2, . . . , zn−1, n ∈
N, where z0 ∈ {λ1, λ2, . . . , λk}, zm ∈ {ξ (m)
1 , ξ (m)
2 , . . . , ξ (m)
n−m}, m = 1, 2, . . ., n−1, satisfying conditions f (m)(zm) =
0, m = 0, 1, . . . , n − 1 and, clearly f (n)(z) = n!. Then we represent f (z) in the form

f (z) = z
n + Pn−1(z), (3)
where Pn−1(z) is a polynomial of degree at most n − 1. To determine Pn−1(z) we differentiate the latter
equality m times, and we calculate the corresponding derivatives in zm to obtain

P(m)
n−1(zm) = − n!
(n − m)!z
n−m
m , m = 0, 1, . . . , n − 1. (4)

But this is the known Abel-Goncharov interpolation problem (see [6]) and the polynomial Pn−1(z) can be
uniquely determined via the linear system (4) of n equations with n unknowns and triangular matrix with
non-zero determinant. So, following [6], we derive

Pn−1(z) = − n−1
∑
k=0
 n!
(n − k)! z
n−k
k Gk(z), (5)

where Gk(z), k = 0, 1, . . . , n − 1 is the system of the Abel-Goncharov polynomials [6], [7], [8]. On the other
hand it is known that
 Gn(z) = z
n − n−1
∑
k=0
 n!
(n − k)! z
n−k
k Gk(z). (6)

Thus comparing with (3), we ﬁnd that

Gn(z) ≡ Gn (z, z0, z1, z2, . . . , zn−1) = f (z),

POLYNOMIAL PROBLEMS 3

and Gn (λj, z0, z1, z2, . . . , zn−1) = f (λj) = 0, j = 1, 2, . . . , k.

Plainly, one can relate possible CA-polynomials with the corresponding Abel-Goncharov polynomials, ﬁx-
ing a sequence {zm}n−1
0 such that

zm ∈ {λ1, λ2, . . . , λk}, m = 0, 1, . . . , n − 1.

Further, It is known [6] that the Abel-Goncharov polynomial can be represented as a multiple integral in
the complex plane
 Gn(z) = n! ∫ z

z0
 ∫ s1

z1 · · · ∫ sn−1

zn−1 dsn . . . ds1. (6)

Moreover, making simple changes of variables in (6), it can be veriﬁed that Gn(z) is a homogeneous function
of degree n (cf. [7]). Therefore

Gn(αz) = Gn (αz, αz0, αz1, . . . , αzn−1) = αnGn(z), α ̸= 0. (7)

The following Goncharov upper bound holds for Gn (see [9], [6], [7], [11])

|Gn(z)| ≤
 (
|z − z0| + n−2
∑
s=0 |zs+1 − zs|
)n . (8)

Let us represent the Abel-Goncharov polynomials Gn(z) in a different way. To do this, we will use the
following representation of the Gauss hypergeometric function given by relation (2.2.6.1) in [12], namely
∫ b

a (z − a)
α−1(b − z)
β−1(z + c)
γdz = (b − a)
α+β−1(a + c)
γB(α, β)2F1
 (
α, −γ;α + β; a − b
a + c
 ) , (9)

where α, β, γ are positive integers, a, b, c ∈ C and B(α, β) is the Euler beta-function. So, our goal will
be a representation of the Abel-Goncharov polynomials in terms of the so-called genetic sums considered,
for instance, in [10]. Moreover, this will lead us to another than (8) upper bound for these polynomials.
Indeed, G1(z) = z − z0. When n ≥ 2, we use the multiple integral representation (6), and appealing to the
representation (9), we obtain recursively

Gn(z) = n! ∫ z

z0
 ∫ s1

z1 · · · ∫ sn−2

zn−2 (sn−1 − zn−1)dsn−1 . . . ds1

= n!(zn−2 − zn−1) ∫ z

z0
 ∫ s1

z1 · · · ∫ sn−3

zn−3 (sn−2 − zn−2)2F1
 (
1, −1; 2; zn−2 − sn−2
zn−2 − zn−1
 ) dsn−2 . . . ds1

= n! 1
∑
j1=0
 (−1) j1(−1) j1

(2) j1 (zn−2 − zn−1)
1− j1 ∫ z

z0
 ∫ s1

z1 · · · ∫ sn−3

zn−3 (sn−2 − zn−2)
1+ j1dsn−2 . . . ds1.

Hence, employing properties of the Pochhammer symbol and repeating this process, we ﬁnd

Gn(z) = n! 1
∑
j1=0
 (zn−2 − zn−1)1− j1

(2) j1 (1 − j1)!
 ∫ z

z0
 ∫ s1

z1 · · · ∫ sn−3

zn−3 (sn−2 − zn−2)
1+ j1dsn−2 . . . ds1

= n! 1
∑
j1=0
 1+ j1
∑
j2=0
 (zn−2 − zn−1)1− j1(zn−3 − zn−2)1+ j1− j2

(2) j2 (1 − j1)!(1 + j1 − j2)!
 ∫ z

z0
 ∫ s1

z1 · · · ∫ sn−4

zn−4 (sn−3 − zn−3)
1+ j2dsn−3 . . . ds1.

4 S. YAKUBOVICH

Continuing to calculate iterated integrals with the use of (9), we arrive ﬁnally at the following genetic sum
representation of the Abel-Goncharov polynomials ( j0 = jn = 0, z−1 ≡ z)

Gn(z) = n! 1
∑
j1=0
 1+ j1
∑
j2=0 · · ·
 1+ jn−2
∑
jn−1=0
 n−1
∏
s=0
 (zn−2−s − zn−1−s)1+ js− js+1

(1 + js − js+1)! . (10)

Analogously, we derive the genetic sum representation for the m-th derivative G(m)
n (z), namely ( j0 = 0)

G(m)
n (z) = n! 1
∑
j1=0
 1+ j1
∑
j2=0 · · ·
 1+ jn−2−m
∑
jn−1−m=0
 (z − zm)1+ jn−1−m

(1 + jn−1−m)!
 n−2−m
∏
s=0
 (zn−2−s − zn−1−s)1+ js− js+1

(1 + js − js+1)! , (11)

where m = 0, 1, . . . , n − 1.
Meanwhile, the Taylor expansions of G(m)
n (z) in the neighborhood of points zm give the formulas

G(m)
n (z) = n!
(n − m)! (z − zm)
n−m + G(n−1)
n (zm)
(n − m − 1)!(z − zm)
n−m−1 + · · · + G(1+m)
n (zm)(z − zm), (12)

where m = 0, 1, . . . , n − 1. Thus comparing coefﬁcients in front of (z − zm)s, s = 1, . . . , n − m − 1 in (11)
and (12), we ﬁnd the values of derivatives G(s+m)
n (zm) in terms of zm, zm+1, . . . , zn−1. Precisely, we obtain
( j0 = 0)

G(s+m)
n (zm) = n! 1
∑
j1=0
 1+ j1
∑
j2=0 · · ·
 1+ jn−3−m
∑
jn−2−m=0
 (zm − zm+1)2+ jn−2−m−s

(2 + jn−2−m − s)!
 n−3−m
∏
l=0
 (zn−2−l − zn−1−l)1+ jl − jl+1

(1 + jl − jl+1)! , (13)

where s = 1, 2, . . . , n − m, m = 0, 1, . . . , n − 1.
Finally, in this section, we will establish an upper bound for the Abel-Goncharov polynomials (cf. (8)).
We have
Theorem 1. Let z, z0, z1, z2, . . . , zn−1 ∈ C, n ≥ 1. The following upper bound holds for the Abel-Goncharov
polynomials

|Gn (z, z0, z1, z2, . . . , zn−1) | ≤ 1
∑
k0=0
 2−k0
∑
k1=0· · ·
 n−1−k0−k1−···−kn−3
∑
kn−2=0
 ( n
k0, k1, . . . , kn−2, n − k0 − k1 − · · · − kn−2
)

×|z − z0|n−k0−k1−···−kn−2 n−2
∏
s=0 |zn−2−s − zn−1−s|ks , (14)

where z−1 ≡ z and ( n
l0, l1, . . . , lm
) = n!
l0!l1! . . . lm! , l0 + l1 + · · · + lm = n

are multinomial coefﬁcients.

Proof. In fact, making simple substitutions ks = 1 + js − js+1, s = 0, 1, . . . , n − 1, j0 = jn = 0 and writing
identity (10) for the Abel-Goncharov polynomials (6), we estimate their absolute value, coming out imme-
diately with inequality (14). □

POLYNOMIAL PROBLEMS 5

3. SZ.-NAGY TYPE IDENTITIES FOR ROOTS OF POLYNOMIALS AND THEIR DERIVATIVES

In this section we prove Sz.-Nagy type identities [5] for zeros of monic polynomials with complex coef-
ﬁcients and their derivatives. All notations of roots and their multiplicities given in Section 1 are involved.
We begin with
Lemma 1. Let f be a monic polynomial of degree n ≥ 2 with complex coefﬁcients, m = 0, 1, . . . , n − 2 and
z ∈ C. Then the following Sz.-Nagy type identities, which relate the roots of f and its m-th derivative, hold

zn−1 − z = 1
n
 k
∑
j=1 r j(λj − z) = 1
n − m
 n−m
∑
j=1(ξ (m)
j − z), (15)

(zn−1 − zn−2)
2 = 1
n(n − 1)
 [ k
∑
j=1r j(λj − z)
2 − n(zn−1 − z)
2]
 = 1
(n − m)(n − m − 1)

×
 [
n−m
∑
j=1(ξ (m)
j − z)
2 − (n − m)(zn−1 − z)
2]
 , (16)

(zn−1 − zn−2)
2 = 1
n2(n − 1) ∑
1≤ j<s≤k r jrs(λj − λs)
2 = 1
(n − m)2(n − m − 1) ∑
1≤ j<s≤n−m
(ξ (m)
j − ξ (m)
s )
2. (17)

Proof. In fact, the ﬁrst Vi´ete formula (see [5]) says that the coefﬁcient a1 (a0 = 1) in (1) is equal to

−a1 = r1λ1 + r2λ2 + · · · + rkλk.

On the other hand, differentiating (1) n − 1 times, we ﬁnd zn−1 = −a1/n. Thus in view of (2) we prove
the ﬁrst identity in (15). The second identity can be done similarly, using that a centroid is differentiation
invariant, see, for instance, [5]. In order to establish the ﬁrst identity in (16), we call formula (11) to ﬁnd

f (n−2)(z)
(n − 2)! = n(n − 1)
2 (z − zn−2)(z + zn−2 − 2zn−1). (18)

Moreover, as a consequence of the second Vi´ete formula, the coefﬁcient a2 in (1), which equals

a2 = f (n−2)(z)
(n − 2)! − n(n − 1)
2 z
2 + n(n − 1)zn−1z (19)

can be expressed as follows
 a2 = 1
2
 ( k
∑
j=1 r jλj
)2 − 1
2
 k
∑
j=1 r jλ 2
j . (20)

Hence letting z = zn−2 in (18), and taking into account (15) with z = 0, we deduce

2a2 = n2z
2
n−1 − k
∑
j=1r jλ 2
j = 2n(n − 1)zn−1zn−2 − n(n − 1)z
2
n−2.

Therefore, using again (15) and (2), we easily come up with the ﬁrst identity in (16). The second one can
be proven in the same manner, involving roots of derivatives. Finally, we prove the ﬁrst identity in (17).
Concerning the second identity, see Lemma 6.1.5 in [5]. Indeed, calling the ﬁrst identity in (16), letting
z = zn−1 and employing (15), we derive

6 S. YAKUBOVICH

n2(n − 1)(zn−1 − zn−2)
2 = n k
∑
j=1r jλ 2
j +
 ( k
∑
s=1 rsλs
)2 − 2
 ( k
∑
s=1 rsλs
) ( k
∑
j=1 r jλj
)

= n k
∑
j=1r jλ 2
j − k
∑
s=1r2
j λ 2
j − 2 ∑
1≤ j<s≤kr jrsλjλs = ∑
1≤ j<s≤k r jrs(λj − λs)
2.
 □

The following result gives an identity, which is associated with zeros of a monic polynomial and common
zeros of its derivatives. Precisely, we have
Lemma 2. Let f be a monic polynomial of exact degree n ≥ 2, having k distinct roots of multiplicities
(2). Let zn−1 = λ1 be a common root of f of multiplicity r1 with the unique root of its n − 1st derivative. Let
also zm = ξ (m)
n−m = λkm be a common root of f of multiplicity rkm and its m-th derivative, m ∈ {1, 2, . . ., n − 2}.
Then, involving other roots of f (m), the following identity holds

[ n − m − 2
(n − m)2 + rkm + r1 − n
n(n − 1)
 ] n−m−1
∑
s=1 (zm − ξ (m)
s )
2 + n − m − 2
(n − m)2 ∑
1≤s<t≤n−m−1
(ξ (m)
s − ξ (m)
t )
2

= (n − m)2rkm − (n − r1)(n − m + 2)
n(n − 1) (zm − zn−1)
2

+ 2
n(n − 1) ∑
j̸=1,km r j ∑
1≤s<t≤n−m−1
(λj − ξ (m)
s )(λj − ξ (m)
t ). (21)

Proof. We begin, appealing to (15) and letting z = 0. We get

n−m
∑
s=1 ξ (m)
s = (n − m)zn−1, ξ (m)
n−m = zm. (22)

Hence via identities (17) with z = zm we write the chain of equalities

∑
1≤s<t≤n−m
(ξ (m)
s − ξ (m)
t )
2 = (n − m − 1)(n − m)2

n(n − 1) rkm (zm − zn−1)
2 + (n − m − 1)(n − m)2

n(n − 1) ∑
j̸=1,km r j(λj − zn−1)
2

= (n − m − 1)(n − m)2

n(n − 1) rkm (zm − zn−1)
2 + n − m − 1
n(n − 1) ∑
j̸=1,km r j
 (
λj − zm + n−m−1
∑
s=1 (λj − ξ (m)
s )

)2

= (n − m − 1)(n − m)2

n(n − 1) rkm (zm − zn−1)
2 + n − m − 1
n(n − 1)
 

 ∑
j̸=1,km r j(λj − zm)
2 + ∑
j̸=1,km r j
 (n−m−1
∑
s=1 (λj − ξ (m)
s )

)2

+2 ∑
j̸=1,km r j
 n−m−1
∑
s=1 (λj − zm)(λj − ξ (m)
s )

]
 = (n − m − 1)(n − m)2

n(n − 1) rkm (zm − zn−1)
2

+ n − m − 1
n(n − 1)
 

(2(n − m) − 1) ∑
j̸=1,km r j(λj − zm)
2 + ∑
j̸=1,km r j
 (n−m−1
∑
s=1 (λj − ξ (m)
s )

)2

+2 ∑
j̸=1,km r j
 n−m−1
∑
s=1 (λj − zm)(zm − ξ (m)
s )

]
 = (n − m − 1)(n − m)
2

n(n − 1) rkm (zm − zn−1)
2

POLYNOMIAL PROBLEMS 7

+ n − m − 1
n(n − 1)
 

(2(n − m) − 1) ∑
j̸=1,km r j(λj − zm)
2 + ∑
j̸=1,km r j
 (n−m−1
∑
s=1 (λj − ξ (m)
s )

)2

−2(n − m)(n − r1)(zm − zn−1)
2] = (n − m − 1)
n(n − 1)
 (
(n − m)
2rkm − n + r1) (zm − zn−1)
2

+(n − m − 1)(3(n − m) − 2)(zn−1 − zn−2)
2 + (n − m − 1)(n − r1)
n(n − 1)
 n−m−1
∑
s=1 (zn−1 − ξ (m)
s )
2

− rkm (n − m − 1)
n(n − 1)
 n−m−1
∑
s=1 (zm − ξ (m)
s )
2 + 2 n − m − 1
n(n − 1) ∑
j̸=1,km r j ∑
1≤s<t≤n−m−1
(λj − ξ (m)
s )(λj − ξ (m)
t ).

Applying again (17), (22), we split the right-hand side of the latter identity in (17) in two parts, selecting the
root zm. Thus in the same manner after straightforward calculations it becomes
[ n − m − 2
(n − m)2 + rkm + r1 − n
n(n − 1)
 ] n−m−1
∑
s=1 (zm − ξ (m)
s )
2 + n − m − 2
(n − m)2 ∑
1≤s<t≤n−m−1
(ξ (m)
s − ξ (m)
t )
2

= (n − m)
2rkm − (n − r1)(n − m + 2)
n(n − 1) (zm − zn−1)
2 + 2
n(n − 1) ∑
j̸=1,km r j ∑
1≤s<t≤n−m−1
(λj − ξ (m)
s )(λj − ξ (m)
t ),

completing the proof of Lemma 2. □

Remark 1. It is easy to verify identity (21) for the least case m = n − 2, when the double sums are empty
and ξ (n−2)
1 = 2zn−1 − zn−2 (see above).
Corollary 1. A polynomial with only real roots of degree n ≥ 2 is trivial, if and only if its n − 2nd
derivative has a double root.

Proof. Indeed, necessity is obvious. To prove sufﬁciency we see that since the n − 2nd derivative has a
double real root xn−2, it is equal to the root xn−1 of the n − 1st derivative. Therefore letting in (16) z = xn−1,
we ﬁnd that its left-hand side becomes zero and, correspondingly, all squares in the right-hand side are zeros.
This gives the conclusion that all roots are equal to xn−1. □

Corollary 2. Let f be an arbitrary polynomial of degree n ≥ 3 with at least two distinct roots, whose
n − 2nd derivative has a double root. Then it contains at least one complex root.

Proof. In fact, if all roots are real it is trivial via Corollary 1. □

Evidently, each derivative up to f (r−1) of a polynomial f with only real roots, where r is the maximal
multiplicity, shares a root with f . Moreover, owing to the Rolle theorem all roots of f (m), m = r, r + 1, . . . , n −
1 are simple, we have that a possible common root with f is simple too (we note, that a number of common
roots does not exceed k − 2, because minimal and maximal roots cannot be zeros of f (m), m ≥ r). This
circumstance gives an immediate
Corollary 3. There exists no non-trivial polynomial with only real roots, having two distinct zeros and
sharing a root with at least one of its derivatives, whose order exceeds r − 1, r = max1≤ j≤k(r j).

8 S. YAKUBOVICH

Proof. Indeed, in the case of existence of such a polynomial, these two distinct roots cannot be within zeros
of any derivative f (m), m > r owing to the Rolle theorem. Moreover, if any of the two roots are in common
with roots of f (r), its multiplicity is greater than r, which is impossible. □

We extend Corollary 3 to three distinct real roots. Precisely, it leads to
Corollary 4. There exists no non-trivial polynomial f of degree n ≥ 3 with only real roots, having three
distinct zeros and sharing a root with its n − 2nd and n − 1st derivatives.

Proof. Assume such a polynomial exists and let’s denote its roots λ1 = xn−1, λ2 = xn−2 and λ3 of multiplic-
ities r1, r2, r3, respectively. Hence employing identities (16), we write for this case

(n2 − n − r2)(xn−1 − xn−2)
2 = r3(λ3 − xn−1)
2.

In the meantime, squaring both sides of the ﬁrst identity in (15) for this case after simple modiﬁcations , we
obtain r2
2(xn−1 − xn−2)
2 = r2
3(λ3 − xn−1)
2.

Hence, comparing with the previous equality, we come out with the relation

(n2 − n − r2)r3 = r2
2.

But n = r1 + r2 + r3, r j ≥ 1, j = 1, 2, 3. Consequently,

r2
2 ≥ n(n − 1) − r2 > (n − 1)
2 − r2 ≥ (r1 + r2)
2 − r2 ≥ r2
2 + r2 + r2
1 > r2
2,

which is impossible. □

Remark 2. If we omit the condition for f to have a common root with the n − 2nd derivative in Corollary
4, it becomes false. In fact, this circumstance can be shown by the counterexample f (x) = x3 − x.
The following result deals with the case of 4 distinct roots. We have,
Corollary 5. There exists no non-trivial polynomial f of degree n ≥ 4 with only real roots, having four
distinct zeros and sharing a root with its n − 2nd and n − 1st derivatives.

Proof. Similarly to the previous corollary, we assume the existence of such a polynomial and call its roots
λ1 = xn−1, λ2 = xn−2 and λ3, λ4 of multiplicities r j, j = 1, 2, 3, 4, respectively. Hence the ﬁrst identity in
(16) yields (n2 − n − r2)(xn−1 − xn−2)
2 = r3(λ3 − xn−1)
2 + r4(λ4 − xn−1)
2. (23)

Meanwhile, using the ﬁrst identity in (15) for this case, we derive in a similar manner

r2
2(xn−1 − xn−2)
2 = r2
3(λ3 − xn−1)
2 + r2
4(λ4 − xn−1)
2 + 2r3r4(λ3 − xn−1)(λ4 − xn−1).

Thus, after straightforward calculations, we come out with the quadratic equation

Ay2 + By + C = 0

in the variable y = (λ3 − xn−1)/(λ4 − xn−1) with coefﬁcients A = r3r2
2 − r2
3(n2 − n − r2), B = −2r3r4(n2 − n −
r2), C = r4r2
2 − r2
4(n2 − n − r2). But, it is easy to verify that B2 − 4AC > 0. Therefore the quadratic equation
has two distinct real roots. Writing λ3 − xn−1 = y(λ4 − xn−1) and substituting into (23), we obtain

(n2 − n − r2)(xn−1 − xn−2)
2 = (r3y2 + r4)(λ4 − xn−1)
2.

At the same time, since y ̸= 0, we have λ4 − xn−1 = y−1(λ3 − xn−1) and

y2(n2 − n − r2)(xn−1 − xn−2)
2 = (r3y2 + r4)(λ3 − xn−1)
2.

POLYNOMIAL PROBLEMS 9

Hence,
 λ4 = xn−1 ±
 √ n2 − n − r2
r3y2 + r4 |xn−1 − xn−2|,

λ3 = xn−1 ± |y|
√ n2 − n − r2
r3y2 + r4 |xn−1 − xn−2|.

Consequently,

λ4 − λ3 =
 √ n2 − n − r2
r3y2 + r4 |xn−1 − xn−2|(1 − |y|) = −
√ n2 − n − r2
r3y2 + r4 |xn−1 − xn−2|(1 + |y|)

=
 √ n2 − n − r2
r3y2 + r4 |xn−1 − xn−2|(1 + |y|) =
 √ n2 − n − r2
r3y2 + r4 |xn−1 − xn−2|(|y| − 1),

which is possible only in the case xn−1 = xn−2, λ3 = λ4. Thus we get a contradiction with Corollary 1 and
complete the proof. □

In the same manner we prove
Corollary 6. There exists no non-trivial polynomial f of degree n ≥ 5 with only real roots, having ﬁve
distinct zeros and sharing roots with its n − 2nd and n − 1st derivatives.

Proof. Assuming its existence, it has the roots λ1 = xn−1, λ2 = xn−2, λ3 = 2xn−1 − xn−2, λ4 and λ5 of
multiplicities r j, j = 1, 2, 3, 4, 5, respectively. Hence

(n2 − n − r2 − r3)(xn−1 − xn−2)
2 = r4(λ4 − xn−1)
2 + r5(λ5 − xn−1)
2.

Therefore using similar ideas as in the proof of Corollary 5, we come out again to the contradiction. □

For an arbitrary number of distinct zeros we establish the following
Corollary 7. There exists no non-trivial polynomial f of degree n with only real roots, having k ≥ 2
distinct zeros of multiplicities (2) r j, j = 1, . . . , k and among them all roots of f (m) for some m, satisfying
the relations
 r ≤ m < 1
2
 (
1 − 1
r0
 ) (n − 1), (24)

where r, r0 are maximum and minimum multiplicities of roots of f .

Proof. In fact, as a consequence of (16) we have the identity

(n − m)(n − m − 1)
n(n − 1)
 k
∑
j=1r j(λj − xn−1)
2 = n−m
∑
j=1(ξ (m)
j − xn−1)
2 (25)

for some m, satisfying condition (24). Hence, since m ≥ r, it has n − m ≤ k − 2 and ξ (m)
j = λm j , m j ∈
{1, . . . , k}, j = 1, . . . , n − m are simple roots of f (m). Thus we ﬁnd

n−m
∑
j=1
 [rm j (n − m)(n − m − 1)
n(n − 1) − 1](λm j − xn−1)
2 + (n − m)(n − m − 1)
n(n − 1)
 k
∑
j=n−m+1rm j (λm j − xn−1)
2 = 0.

But, owing to condition (24)

rm j (n − m)(n − m − 1)
n(n − 1) − 1 ≥ r0 (n − m)(n − m − 1)
n(n − 1) − 1 ≥ 0, j = 1, . . . , n − m.

10 S. YAKUBOVICH

Indeed, we have from the latter inequality

m ≤ n − 1
2 −
 √ n2 − n
r0 + 1
4

and, in turn,

n − 1
2 −
 √ n2 − n
r0 + 1
4 = 2(1 − r−1
0 )(n2 − n)

2n − 1 + √
4(n2 − n)r−1
0 + 1 ≥ (1 − r−1
0 )(n2 − n)
2n − 1 > 1
2
 (
1 − 1
r0
 ) (n − 1).

Therefore λj = xn−1, j = 1, . . . , k and this contradicts to the fact that all roots are distinct. □

Finally, in this section, we will employ identities (17) to prove an analog of the Obreshkov- Chebotarev
theorem for multiple roots (see [5], Theorem 6.4.3), involving estimates for smallest and largest of distances
between consecutive zeros of polynomials and their derivatives. Namely, it has
Theorem 2. Let f be a polynomial of degree n > 2 with only real zeros. Denote the largest and the small-
est of the distances between consecutive zeros of f by ∆ and δ, respectively. Denoting the corresponding
quantities associated with f (m), m = 1, 2, . . . , n − 2 by ∆(m) and δ (m), the following inequalities hold

δ (m) ≤ ∆ rk
n
 √ k2 − 1
(n − m + 1)(n − 1), (26)

δ r0k
n
 √ k2 − 1
(n − m + 1)(n − 1) ≤ ∆(m), (27)

δ r0k
2n
 √ k2 − 1
3(n − 1) ≤ |xn−1 − xn−2| ≤ ∆ rk
2n
 √ k2 − 1
3(n − 1), (28)

where r0, r are minimum and maximum multiplicities of roots of f , respectively, and k ≥ 2 is a number of
distinct roots.

Proof. Following similar ideas as in the proof of Theorem 6.4.3 in [5], we assume distinct roots of f in the
increasing order and roots of its m-th derivative in the non-decreasing order, and taking the second identity
in (17), we deduce
 [δ (m)]2

(n − m)2(n − m − 1) ∑
1≤ j<s≤n−m
(s − j)
2 ≤ [∆r]2

n2(n − 1) ∑
1≤ j<s≤k
(s − j)
2.

Hence, in view of the value of the sum
 ∑
1≤ j<s≤q
(s − t)
2 = 1
12 q2(q2 − 1),

after simple manipulations we arrive at the inequality (26). In the same manner (cf. [5]) we establish
inequalities (27), (28), employing Sz.-Nagy type identities (17). □

POLYNOMIAL PROBLEMS 11

4. LAGUERRE TYPE INEQUALITIES

In 1880 Laguerre proved his famous theorem for polynomials with only real roots, which provides their
localization with upper and lower bounds (see details in [5]). Precisely, we have the following Laguerre
inequalities
 xn−1 − (n − 1) |xn−1 − xn−2| ≤ w j ≤ xn−1 + (n − 1) |xn−1 − xn−2| , j = 1, . . . , n,

where w j are roots of the polynomial f of degree n and xn−1, xn−2 are roots of f (n−1), f (n−2), respectively.
First we prove an analog of the Laguerre inequalities for multiple roots.
Lemma 3. Let f be a polynomial with only real roots of degree n ∈ N, having k distinct roots λj, j =
1, . . . , k of multiplicities (2) and xn−1, xn−2 be roots of f (n−1), f (n−2), respectively. Then the following
Laguerre type inequalities hold

xn−1 −
 √ (n − r j)(n − m − 1)
r j − m |xn−1 − xn−2| ≤ λj ≤ xn−1 +
 √ (n − r j)(n − m − 1)
r j − m |xn−1 − xn−2| , (29)

where j = 1, . . . , k, m = 0, 1, . . . , r j − 1.

Proof. In fact, appealing to the Sz.-Nagy type identities (15), (16) and the Cauchy -Schwarz inequality, we
ﬁnd
 (xn−1 − xn−2)
2 = 1
(n − m)(n − m − 1)
 [n−m
∑
s=1 (ξ (m)
s − λj)
2 − (n − m)(xn−1 − λj)
2]

≥ 1
(n − m)(n − m − 1)
 

 1
n − r j
 (n−m
∑
s=1 (ξ (m)
s − λj)

)2 − (n − m)(xn−1 − λj)
2




= r j − m
(n − r j)(n − m − 1) (xn−1 − λj)2 , m = 0, 1, . . . , r j − 1,

which yields (29). □

As a corollary we improve the Laguerre inequality (28) for multiple roots.
Corollary 8. Let f be a polynomial with only real roots of degree n ∈ N. Then the multiple zero λj of
multiplicity r j ≥ 1, j = 1, . . . , k lies in the interval
[

xn−1 −
 √( n
r j − 1)(n − 1)|xn−1 − xn−2| , xn−1 +
 √( n
r j − 1)(n − 1)|xn−1 − xn−2|
]
 . (30)

Proof. Indeed, the fraction (n−r j)(n−m−1)
r j −m attains its minimum value, letting m = 0 in (29). □

Remark 3. When all roots are simple, the latter interval coincides with the one generated by (28).
A localization of roots of the m-th derivative f (m), m = 0, 1, . . . , n − 2 is given by
Lemma 4. Roots of the m-th derivative f (m), m = 0, 1, . . . , n − 2 satisfy the following Laguerre type
inequalities
 xn−1 − (n − m − 1) |xn−1 − xn−2| ≤ ξ (m)
ν ≤ xn−1 + (n − m − 1) |xn−1 − xn−2| , (31)

where ν = 1, . . . , n − m.

12 S. YAKUBOVICH

Proof. Similarly to the proof of Lemma 3, we employ the Sz.-Nagy type identities (15), (16) and the Cauchy
-Schwarz inequality to deduce

(xn−1 − xn−2)
2 = 1
(n − m)(n − m − 1)
 [n−m
∑
s=1 (ξ (m)
s − ξ (m)
ν )
2 − (n − m)(xn−1 − ξ (m)
ν )
2]

≥ 1
(n − m)(n − m − 1)
 

 1
n − m − 1
 (
n−m
∑
s=1 (ξ (m)
s − ξ (m)
ν )

)2 − (n − m)(xn−1 − ξ (m)
ν )
2




= 1
(n − m − 1)2
 (xn−1 − ξ (m)
ν )2 , m = 0, 1, . . . , n − 2.

Thus we come up with (31) and complete the proof. □

When the root xn−1 = λ1 be in common with f of multiplicity r1, we have
Lemma 5. Let f be a polynomial with only real roots of degree n ≥ 2 and xn−1 = λ1 be a common zero
with f of multiplicity r1, having k ≥ 2 distinct roots λj of multiplicities r j, j = 1, . . . , k. Then the following
Laguerre type inequalities hold

xn−1 −
 √( 1
rs − 1
n − r1
 ) (n2 − n)|xn−1 − xn−2| ≤ λs ≤ xn−1

+
√( 1
rs − 1
n − r1
 ) (n2 − n)|xn−1 − xn−2| , (32)

where s = 2, . . . , k.

Proof. In the same manner we involve the ﬁrst Sz.-Nagy type identity in (15) with z = λs, which can be
written in the form
 (n − r1)(xn−1 − λs) = k
∑
j=2r j(λj − λs).

Hence squaring both sides of the latter equality and appealing to the Cauchy -Schwarz inequality, we derive
by virtue of (16)
 (n − r1)
2(xn−1 − λs)
2 =
 ( k
∑
j=2r j(λj − λs)

)2

≤ (n − r1 − rs) k
∑
j=2 r j(λj − λs)
2 = (n − r1 − rs) [(n2 − n)(xn−1 − xn−2)
2 + (n − r1)(xn−1 − λs)
2] .

Thus after simple calculations we easily arrive at (32). □

Remark 4. Inequalities (27) are sharper than the corresponding relations, generated by interval (30).
The following result gives a Laguerre type localization for common roots of a possible CA-polynomial
with only real roots and its m-th derivative.

POLYNOMIAL PROBLEMS 13

Lemma 6. Let f be a CA-polynomial of degree n ≥ 2 with only real distinct zeros of multiplicities (2),
including common roots xn−1 = λ1 of its n−1st derivative and xm of its m-th derivative, m = r, r +1, . . . , n−2,
where r = max1≤ j≤k(r j). Then the following Laguerre type inequality holds

n − r1 − rkm
(n − r1)2 (
n2 − r1 + (n − r1)(n − m)(n − m − 2)
)(xn−1 − xn−2)
2 ≥ (xn−1 − xm)
2, (33)

where xn−2 is a root of f (n−2) and rkm is the multiplicity of xm as a root of f .

Proof. Appealing again to Sz.-Nagy type identities (15), (16) with z = xm, inequality (31) and the Cauchy-
Schwarz inequality, we ﬁnd

(xn−1 − xn−2)
2 = 1
n(n − 1)
 [ k
∑
j=2 r j(λj − xm)
2 − (n − r1)(xn−1 − xm)
2]

≥ 1
n(n − 1)
 [ k
∑
j=2 r j(λj − xm)
2 − (n − r1)(n − m − 1)
2(xn−1 − xn−2)
2]

≥ 1
n(n − 1)
 

 1
n − r1 − r jm
 ( k
∑
j=2 r j(λj − xm)

)2 − (n − r1)(n − m − 1)
2(xn−1 − xn−2)
2




= n − r1
n(n − 1)
 [ n − r1
n − r1 − r jm (xn−1 − xm)
2 − (n − m − 1)
2(xn−1 − xn−2)
2] .

Hence, making straightforward calculations, we derive (33), completing the proof of Lemma 6. □

Let us denote by d, d(m), D, D(m) the following values

d = min2≤ j≤k|λj − xn−1|, d(m) = min1≤ j≤n−m|ξ (m)
j − xn−1|, (34)

D = max2≤ j≤k|λj − xn−1|, D(m) = max1≤ j≤n−m|ξ (m)
j − xn−1|, (35)

and by span( f ) = λ ∗ − λ∗,

where λ ∗ = max1≤ j≤k(λj), λ∗ = min1≤ j≤k(λj)

are roots of f with multiplicities r∗, r∗, respectively. Then D(m+1) ≤ D(m) ≤ D and (cf. [5]) span( f (m+1)) ≤
span( f (m)) ≤ span( f ), where span( f (m)) is the span of the m-th derivative. Moreover, the strict inequalities
D(m) < D, span( f (m)) < span( f ) hold when m is sufﬁciently large.
Lemma 7. Let xn−1 = λ1, xn−2 = λ2 be common roots of f with its n − 1st, n − 2nd derivatives, respec-
tively, of multiplicities r1, r2 as roots of f , and the maximum distance D (see (35)) be attained at the root
λs0, s0 ∈ {3, . . . , k}, k ≥ 3 of f of multiplicity rs0. Then the following inequalities hold
√ n2 − n − r2
n − r1 − r2 |xn−1 − xn−2| ≤ D ≤
 √ n2 − n − r2
rs0 |xn−1 − xn−2| , (36)

1
2
 √ rs0
3(n − r1)
 (
5 + r2
n2 − n − r2
 )
span( f ) ≤ D ≤
 √ 1
n − r1
 [
n − r1 − rs0
4
 (
5 + r2
n2 − n − r2
 )]span( f ). (37)

14 S. YAKUBOVICH

Proof. In order to establish (36), we employ identities (16) and under condition of the lemma we write

(n2 − n − r2)(xn−1 − xn−2)
2 = k
∑
j=3 r j(λj − xn−1)
2 ≤ (n − r1 − r2)D2.

Since n > r1 + r2 and xn−2 ̸= λs0 (otherwise f is trivial, because equalities xn−2 = λs0 = λ ∗ or xn−2 = λs0 = λ∗
mean that the maximum multiplicity r > n − 2, and we appeal to Corollary 3), we come up with the lower
bound (36) for D. The lower bound comes immediately from the estimate

(n2 − n − r2)(xn−1 − xn−2)
2 = k
∑
j=3 r j(λj − xn−1)
2 ≥ rs0D2.

Now, since 2D ≥ span( f ), we ﬁnd from (36)

span( f ) ≤ 2
√ n2 − n − r2
rs0 |xn−1 − xn−2| .

Hence, since D = max (|λ ∗ − xn−1|, |λ∗ − xn−1|), the n − 2nd derivative has roots xn−2 and 2xn−1 − xn−2 and
span( f ) = D + Λ, where Λ = min (|λ ∗ − xn−1|, |λ∗ − xn−1|), we appeal to the ﬁrst identity in (16), letting
z = λs0 and writing it in the form

(n − r1)(xn−1 − λs0)
2 = k
∑
j=2 r j(λj − λs0)
2 − n(n − 1)(xn−1 − xn−2)
2.

Therefore,
 (n − r1)D2 ≤ [n − r1 − 5
4 rs0 − rs0 r2
4(n2 − n − r2)
 ] [span( f )]
2

and we establish the upper bound (37) for D. On the other hand span( f ) = D + Λ. So,

D2 ≤ (
1 − rs0
4(n − r1)
 (
5 + r2
n2 − n − r2
 ) ) (
D2 + Λ2 + 2DΛ)

and we easily come out with the lower bound (37) for D, completing the proof of Lemma 7. □

Lemma 8. Let xn−1 = λ1, xn−2 = λ2 be common roots of f with its n − 1st, n − 2nd derivatives of
multiplicities r1, r2, r1 + r2 < n, respectively. Then we have the following lower bound for span( f )

span( f ) ≥
 √ n2 − r1
n − r1 − r2 |xn−1 − xn−2|. (38)

Proof. Indeed, identities (16) with z = xn−2 yield

(n2 − r1)(xn−1 − xn−2)
2 = k
∑
j=3r j(λj − xn−2)
2

and we derive (n2 − r1)(xn−1 − xn−2)
2 ≤ (n − r1 − r2)[span( f )]2,

which implies (38). □

POLYNOMIAL PROBLEMS 15

Next, we establish an analog of Lemma 5 for roots of derivatives. Precisely, we have
Lemma 9. Let xn−1, xn−2 be roots of the n − 1st, n − 2nd derivatives of f , respectively. Then

D(m) ≥ √
n − m − 1 |xn−1 − xn−2|, (39)

where m ∈ {r, r + 1, . . . , n − 2}, r = max1≤ j≤k(r j). Besides, if xn−1 is a root of f (m), then we have a stronger
inequality D(m) ≥ √
n − m |xn−1 − xn−2|. (40)

Moreover,
 2 D(m) ≥ span( f (m)) ≥ n − m
n − m − 1 D(m). (41)

and if xn−1 is a root of f (m), it becomes

2 D(m) ≥ span( f (m)) ≥
 √ (n − m)(n − m − 1) + 1
(n − m − 1)(n − m − 2) D(m), (42)

where m ∈ {r, r + 1, . . . , n − 3}.

Proof. In fact, since (see (16))

(n − m)(n − m − 1)(xn−1 − xn−2)
2 = n−m
∑
j=1(ξ (m)
j − xn−1)
2 ≤ (n − m) [
D(m)]2 ,

we get (39). Analogously, we immediately come out with (40), when xn−1 is a root of f (m), because one
element of the sum of squares is zero. In order to prove (41), we appeal again to (16), letting z = ξ (m)
s0 , s0 ∈
{1, 2, . . . , n − m}, m ∈ {r, r + 1, . . . , n − 2}, r = max1≤ j≤k(r j), which is a root of f (m), where the maximum
D(m) is attained. Hence owing to Laguerre type inequality (31)

(n − m) [
D(m)]2 ≤ (n − m − 1)[span( f (m))]2 − n − m
n − m − 1
 [
D(m)]2 ,

which leads to the lower bound for span( f (m)) in (41). The upper bound is straightforward since xn−1 belongs
to the smallest interval containing roots of f (m). In the same manner we establish (42), since in this case

(n − m − 1) [
D(m)]2 ≤ (n − m − 2)[span( f (m))]2 − n − m
n − m − 1
 [
D(m)]2 .
 □

Remark 5. The case m = n − 2 gives equalities in (39), (41). Letting the same value of m in (40), we
easily get a contradiction, which means that the only trivial polynomial is within polynomials with only real
roots, whose derivatives f (n−2), f (n−1) have a common root (see Corollary 1).

5. APPLICATIONS TO THE CASAS- ALVERO CONJECTURE

In this ﬁnal section we will discuss properties of possible CA-polynomials, which share roots with each of
their non-constant derivatives. We will investigate particular cases of the Casas-Alvero conjecture, especially
for polynomials with only real roots, showing when it holds true or, possibly, is false.
We begin with
Proposition 1. The Casas-Alvero conjecture holds true, if and only if it is true for common roots {zν}n−1
0
lying in the unit circle.

16 S. YAKUBOVICH

Proof. The necessity is trivial. Let’s prove the sufﬁciency. Let the conjecture be true for common roots
{zν}n−1
0 of a complex polynomial f and its non-constant derivatives, which lie in the unit circle. Associating
with f an Abel-Goncharov polynomial Gn (6), one can choose an arbitrary α > 0 such that |zν| < α−1, ν =
0, 1, . . . , n − 1. Hence owing to (7)

f (αzν ) = Gn (αz0, αzν, αz1, . . . , αzn−1) = αnGn(zν) = αn f (zν) = 0, ν = 0, 1, . . . , n − 1,

and
 f (ν)
n (αz) = n! dν

dzν
 ∫ αz

αz0
 ∫ s1

αz1· · · ∫ sn−1

αzn−1 dsn . . . ds1 = n!αν ∫ αz

αzν
 ∫ sν+1

αzν+1· · · ∫ sn−1

αzn−1 dsn . . . dsν+1,

we ﬁnd f (ν)
n (αzν) = 0. Hence αzν, ν = 0, 1, . . . , n − 1 are common roots of ν-th derivatives f (ν) and f , lying
in the unit circle. Consequently, since via assumption the Casas-Alvero conjecture is true when common
roots are inside the unit circle, we have that f is trivial and z0 = z1 = · · · = zn−1 = a is a unique joint root of
f of the multiplicity n. Proposition 1 is proved. □

The following lemma will be useful in the sequel.
Lemma 10. Let f be a CA-polynomial with only real roots of degree n ≥ 2 and {xν}n−1
0 be a sequence of
common roots of f and the corresponding derivatives f (ν). Let f (s+ν)(xν) ≥ 0, s = 1, 2, . . . , n − ν − 1 and
ν = 0, 1, . . . , n − 1. Then xν is a maximal root of the derivative f (ν).

Proof. In fact, the proof is an immediate consequence of the expansion (12), where we let Gn(x) = f (x).
Indeed, f (ν)(xν) = 0, ν = 0, 1, . . . , n − 1 and when x > xν we have from (12) f (ν)(x) > 0, ν = 0, 1, . . . , n − 1.
So, this means that there are no roots, which are bigger than xν. This completes the proof of Lemma 10. □

Proposition 2. Under conditions of Lemma 10 the Casas-Alvero conjecture holds true for polynomials
with only real roots.

Proof. We will show that under conditions of Lemma 10 there exists no CA-polynomial f with only real
roots. Indeed, assuming its existence, we ﬁnd via conditions of the lemma that the root x0 is a maximal zero
of f (x). This means that x0 ≥ x1. On the other hand, the classical theorem of Rolle states that between zeros
x0, x1 in the case x0 > x1 there exists at least one zero of the derivative f (1)(x), say ξ (1)
1 , which is bigger
than x1. But this is impossible because x1 is a maximal zero of the ﬁrst derivative. Thus x0 = x1 ≥ x2. Then
between x1 and x2 in the case x1 > x2 there exists a zero ξ (1)
2 of the ﬁrst derivative such that x1 > ξ (1)
2 > x2.
Hence between x1 and ξ (1)
2 there exists at least one zero of the second derivative, which is bigger than x2. But
this is impossible, since x2 is a maximal zero of f (2)(x). Therefore x0 = x1 = x2. Continuing this process we
observe that the sequence {xν}n−1
0 is stationary and f has a unique joint root, which contradicts the deﬁnition
of the CA-polynomial. □

Corollary 9. There exists no CA-polynomial f with only real roots, having a non-increasing sequence
{xν}n−1
0 of roots in common with f and its non-constant derivatives.

Proof. Obviously, via (13) f (s+ν)(xν) ≥ 0, s = 1, 2, . . . , n − ν − 1 and conditions of Lemma 10 are satisﬁed.
□

Corollary 10. There exists no CA-polynomial f with only real roots, such that each xν in the sequence
{xν}n−1
0 is a maximal root of the derivative f (ν)(x), ν = 0, 1, . . . , n − 1.

Proof. The proof is similar to the proof of Proposition 2. □

POLYNOMIAL PROBLEMS 17

An immediate consequence of Corollaries 3,4,5 is
Corollary 11. The CA-polynomial, if any, with only real roots has at least 5 distinct zeros.
Let us denote by l(m) the number of distinct roots of the m-th derivative f (m), m = 0, 1, . . . , n − 2, which
are in common with f and different from λ1 = xn−1, which is a common root with f (n−1), i.e. the m-th
derivative f (m) has l(m) common roots with f

λj1, . . . , λjl(m) ⊆ {λ2, λ3, . . . , λk}

of multiplicities r j1 , . . . , r jl(m) ⊆ {r2, r3, . . . , rk}.

For instance, l(0) = k − 1, l(1) = k − 1 − s, where s is a number of simple roots of f . So, we see that
n − m ≥ l(m) ≥ 0 and since f is a CA-polynomial, l(m) = 0 if and only if xn−1 = λ1 is the only common
root of f with f (m).
Lemma 11. There exists no CA-polynomial with only real roots, having the property l(m) = l(m + 1) = 0
for some m ∈ {r, r + 1, . . . , n − 2}, where r = max1≤ j≤k(r j).

Proof. In fact, as we saw above, since all roots are real, it follows that all roots of f (m), m ≥ r are simple,
which contradicts equalities l(m) = l(m + 1) = 0. Indeed, the latter equalities yield that xn−1 is a multiple
root of f (m). Therefore r ≥ r1 > m + 1 ≥ r + 1, which is impossible. □

Further, as in Lemma 7 we involve the root λs0 of multiplicity rs0, and D = |λs0 − xn−1| (see (35)). Thus
λs0 = λ∗ or λs0 = λ ∗ and, correspondingly, rs0 = r∗ or rs0 = r∗. Hence, calling Sz.-Nagy identities (15), we
let z = xn−1 and assume without loss of generality that λs0 = λ ∗. Then we obtain for m ≥ r

r∗(xn−1 − λ∗) = r∗D + k
∑
j=2, r j̸=r∗, r∗ r j(λj − xn−1) ≥ r∗D − D(m) l(m)
∑
s=1 r js − D(m+1) l(m+1)
∑
s=1 rls

−
 (

n − r1 − r∗ − r∗ −
 l(m)
∑
s=1 r js −
 l(m+1)
∑
s=1 rls
 )
 D.

But xn−1 − λ∗ = span( f ) − D. Therefore,

r∗span( f ) + (n − r1 − 2(r∗ + r∗)) D ≥ (D − D(m))
 l(m)
∑
s=1 r js + (D − D(m+1))
 l(m+1)
∑
s=1 rls .

The right-hand side of the latter inequality is, obviously, greater or equal to r0 (l(m) + l(m + 1))(D − D(m)),
where 1 ≤ r0 = min1≤ j≤k(r j). Moreover, since span( f ) ≤ 2D, the left-hand side does not exceed (n − r1) D−
r∗span( f ). Thus we come up with the inequality

r0 (l(m) + l(m + 1))(D − D(m)) ≤ (n − r1) D − r∗span( f )

or since D − D(m) > 0 (m ≥ r), it becomes

l(m) + l(m + 1) ≤ (n − r1) D − r∗span( f )
r0(D − D(m)) . (43)

Meanwhile, appealing to (16), we get similarly

n(n − 1)(xn−1 − xn−2)
2 = r∗D2 + r∗(λ∗ − xn−1)
2 + k
∑
j=2, r j̸=r∗, r∗ r j(λj − xn−1)
2

18 S. YAKUBOVICH

≤ r∗D2 + r∗ (span( f ) − D)
2 + [
D(m)]2 l(m)
∑
s=1 r js + [
D(m+1)]2 l(m+1)
∑
s=1 rls

+
 (
n − r1 − r∗ − r∗ −
 l(m)
∑
s=1 r js −
 l(m+1)
∑
s=1 rls
 )
 D2.

Therefore, analogously to (43), we arrive at the inequality

l(m) + l(m + 1) ≤ (n − r1)D2 + r∗ [span( f )]2 − n(n − 1)(xn−1 − xn−2)2 − 2Dr∗ span( f )

r0(D2 − [
D(m)]2) .

Proposition 3. There exists no CA- polynomial with only real roots of degree n such that

span( f ) > (r∗)−1 [(n − r1 − r0)D + r0D(m)] , m ≥ r. (44)

Proof. Under condition (44), the right-hand side of (43) is less than one. Thus l(m) = l(m + 1) = 0 and
Lemma 11 completes the proof. □

Let m = n − 2. Then since l(n − 1) = 0, inequality (43) becomes

l(n − 2) ≤ (n − r1)D − r∗span( f )
r0(D − |xn−1 − xn−2|) . (45)

Proposition 4. There exists no CA- polynomial with only real roots of degree n such that

D <
 

r∗ √ n2 − r1
n − r1 − r2 − r0


 |xn−1 − xn−2|
n − r1 − r0 . (46)

Proof. Indeed, employing the lower bound (38) for span( f ), we ﬁnd that under condition (46) the right-hand
side of (45) is strictly less than one. Consequently, l(n − 2) = 0 and owing to Corollary 1 f is trivial. If the
maximum of multiplicities r > n − 2, f has at most 2 distinct zeros and it is trivial via Corollary 3. □

Finally, we prove
Proposition 5. Let CA- polynomial with only real roots exist. Then it has the property

d
D ≤
 √ 2(n − m − 1)
2(k − 1) − 1 , (47)

where d, D are deﬁned by (34), (35), respectively, and m, m+1 belong to the interval [
r, 1
2 (
1 − 1
r0
 ) (n − 1)
)
.

Proof. Since m, m + 1 are chosen from the interval [
r, 1
2 (
1 − 1
r0
 ) (n − 1)
)
, condition (24) holds for these
values. Hence assuming the existence of the CA-polynomial, we return to the Sz.-Nagy type identity (25) to
have the estimate

0 ≥ l(m) (r0 (n − m)(n − m − 1)
n(n − 1) − 1)d2 + (k − 1 − l(m))d2 − (n − m − l(m))D2

≥ (k − 1)d2 − (n − m)D2 + l(m)(D2 − d2).

Writing the same inequality for m + 1

0 ≥ (k − 1)d2 − (n − m − 1)D2 + l(m + 1)(D2 − d2)

POLYNOMIAL PROBLEMS 19

and adding two inequalities, we ﬁnd

0 ≥ 2(k − 1)d2 − (2(n − m) − 1)D2 + (l(m) + l(m + 1))(D2 − d2),

which means
 l(m) + l(m + 1) ≤ (2(n − m) − 1)D2 − 2(k − 1)d2

D2 − d2 .

So, for the existence of the CA-polynomial it is necessary that the right-hand side of the latter inequality is
greater than or equal to 1. Thus we come up with condition (47) and complete the proof. □

Acknowledgment. The present investigation was supported, in part, by the ”Centro de Matem´atica” of
the University of Porto.
 REFERENCES

1. E. Casas-Alvero, Higher order polar germs, J. Algebra 240, (2001), N 1, 326-337.
2. J. Draisma and J. P. de Jong, On the Casas-Alvero conjecture, Eur. Math.Soc. Newsl., (2011), N 80, 29-33.
3. H.-C. Graf von Bothmer, O. Labs, J. Schicho and C. van de Woestijne, The Casas-Alvero conjecture for inﬁnitely many degrees,
J. Algebra, 316 (2007), N 1, 224-230.
4. T.Posltra, Convex hulls and the Casas-Alvero conjecture for the complex plane, Rose-Hulman Undegrad. Math. J., 13 (2012), N 1,
33-42.
5. Q.I. Rahman and G. Schmeisser, Analytic Theory of Polynomials, Clarendon Press, Oxford, 2002.
6. M.A. Evgrafov, The Abel-Goncharov Interpolation Problem, Gosudarstv. Izdat. Tehn.-Teor. Lit., Moscow, 1954 (in Russian).
7. N. Levinson, The Gontcharoff polynomials, Duke Math. J., 11 (1944), 729- 733.
8. N. Levinson, Corrections to ”The Gontcharoff polynomials”, Duke Math. J., 12 (1945), p. 335.
9. V.L. Goncharov, Recherche sur les deriv´ees successives de fonctions analytiques. I. Generalization de la serie d’ Abel., Ann. ´Ecole
Norm., 47 (1930), 1-78 (in French).
10. A. Aptekarev, V. Kaliaguine, J. Van Iseghem, The genetic sum representation for the moments of a system of Stieltjes functions
and its application, Constr. Approx. 16, (2000), N 4, 487-524.
11. I.I. Ibragiumoff, Sur quelques syst´emes complets de fonctions analytiques, Izv. Akad. Nauk SSSR, S.M., (1939), 553-568 (in
French).
12. A.P. Prudnikov, Yu.A. Brychkov and O.I. Marichev, Integrals and Series: Elementary Functions, Gordon and Breach, New York,
1986.

DEPARTMENT OF MATHEMATICS, FAC. SCIENCES OF UNIVERSITY OF PORTO,RUA DO CAMPO ALEGRE, 687; 4169-007
PORTO (PORTUGAL)
E-mail address: syakubov@fc.up.pt
