<!-- source: https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf | converted from PDF -->

Effective Versions of the Chebotarev Density
Theorem

J.C. Lagarias and A.M. Odlyzko

Typeset by the TeXromancers†, credits go to: Aareyan Manzoor, Andrew Lin,
Celeste Yuan, Seewoo Lee, Sadanand Abhyankar

Contents

Contents 1

1 Introduction 2

2 Outline of the main argument 7

3 Artin L-functions and Mellin transform 9

4 Reduction to the case of Hecke L-functions 15

5 Density of zeroes of Hecke L-functions 17

6 The contour integral 23

7 The explicit formula 28

8 Zero-free regions 32

9 Final estimates 35

Bibliography 40

†Link to Github for TeX: https://github.com/AareyanManzoor/Lagarias-Odlyzko
A dyslexic friendly version is linked in the Github.

1

Effective versions of Chebotarev Typeset by the TeXromancers

1 Introduction

Let K be an algebraic number field (finite extension of the rationals Q) and L

a normal extension of K with Galois group G = G(L/K). Let ∆L and ∆K

denote the absolute values of the discriminants of L and K, respectively, and let

nL = [L : Q], nK = [K : Q]. Throughout this paper p will denote a prime ideal of

K and P a prime ideal of L. If p is a prime ideal of K which is unramified in L,

then we use the Artin symbol [ L/K
p
 ] to denote the conjugacy class of Frobenius

automorphisms corresponding to prime ideals P | p. For each conjugacy class C

of G, we define

πC(x, L/K) = ∣
∣
∣
∣{
p : p unramified in L, [ L/K
p
 ] = C, NK/Q p ≤ x}∣
∣
∣
∣.

The Chebotarev density theorem [Tsc26] asserts that

πC(x, L/K) ∼ |C|
|G| Li(x) as x → ∞, (1.1)

where Li(x) is the familiar logarithmic integral

Li(x) = ∫ x

2
 dt
log t ∼ x
log x as x → ∞

The Chebotarev density theorem generalizes many of the classical results on

the distribution of primes and prime ideals. For example, if we consider the trivial

extension L = K of K (K does not have to be normal over Q), then there is only

one conjugacy class, and (1.1) shows that the number of prime ideals of K with

norm ≤ x is asymptotic to Li(x), which is exactly the prime ideal theorem. If

we let K = Q and L = Q(e2πi/q), then the conjugacy classes of G correspond to

the residue classes modulo q, and (1.1) gives us the prime number theorem for

arithmetic progressions.
 2

Lagarias and Odlyzko Section 1: Introduction

One of the most important of the many applications of the Chebotarev density

theorem deals with the group of an equation. Suppose that f (x) is a monic

polynomial whose coefficients are algebraic integers in K and which is irreducible

over K. Suppose further that L is the splitting field of f (x) over K. If we

regard G = G(L/K) as a permutation group acting on the roots of f (x), then

for almost all prime ideals p of K the cycle structure of [ L/K
p
 ] depends on the

factorization of f (x) modulo p, and vice versa. Thus if G is known, then the

Chebotarev density theorem tells us how often various factorizations occur as p

runs through all the prime ideals of K. On the other hand, if we do not know G,

then factoring f (x) modulo the prime ideals of K will yield the complete cycle

structures of G, since by (1.1) for every conjugacy class C there are infinitely

many primes p with [ L/K
p
 ] = C. This can be very helpful in the determination

of G [Wae70, vol. 1, pp. 189-192], especially since by considering enough primes

we can even determine the relative densities of elements of G which have a given

cycle structure. (Unfortunately, sometimes this is not enough to determine G

completely, since it is possible to construct two nonisomorphic groups which

have transitive permutation representations in which the number of elements

with a given cycle structure is the same for both groups.) In these situations it

is important to be able to compute a bound below which every conjugacy class

will occur as the Artin symbol of a prime ideal of K.

The usual proofs of the Chebotarev theorem contains either no error estimates

at all, or else estimates which contain constants depending in some undetermined

way on the fields K and L. In particular, such estimates do not allow us to specify

effectively a value x0 = x0(L/K) such that

πC(x, L/K) > 0 if x ≥ x0. (1.2)

The purpose of this paper is to prove two versions of the Chebotarev theorem,

3

Effective versions of Chebotarev Typeset by the TeXromancers

each of which has an error term which is an explicit and effectively computable

function of x, nL, ∆L, and |C|/|G|. One version assumes the truth of the Gen-

eralized Riemann Hypothesis (GRH) and the other holds unconditionally.

We first state the conditional result.

Theorem 1.1. There exists an effectively computable positive absolute constant

c1 such that if GRH holds for the Dedekind zeta function of L, then for every

x > 2,
 ∣
∣
∣
∣πC(x, L/K) − |C|
|G| Li(x)
∣
∣
∣
∣ ≤ c1
{ |C|
|G| x 1
2 log(∆LxnL) + log ∆L
}. (1.3)

This theorem yields immediately a value of x0 such that (1.2) holds. (We

utilize here the estimate n−1
L log ∆L > 1 + ε for some ε > 0, valid for nL > 1.

It follows from Minkowski’s discriminant bound, and it can also be derived from

(5.11) (see [Odl77]).

Corollary 1.2. There exists an effectively computable positive absolute constant

c2 such that if the GRH holds for the Dedekind zeta function of L ̸= Q, then for

every conjugacy class of G there exists an unramified prime ideal p in K such

that [ L/K
p
 ] = C and
 NK/Q p ≤ c2(log ∆L)2(log log ∆L)
4. (1.4)

(If L = Q, p = (2) yields a solution.)

At the end of this paper we will indicate how the above estimate can be

improved so as to eliminate the log log ∆L term.

We next state the unconditional result.

Theorem 1.3. If nL > 1 then ζL(s) has at most one zero in the region defined

4

Lagarias and Odlyzko Section 1: Introduction

by s = σ + it with

1 − (4 log ∆L)−1 ≤ σ ≤ 1, |t| ≤ (4 log ∆L)
−1. (1.5)

(If nL = 1, L = Q and there is no zero in |t| ≤ 14, σ > 0.)

If such a zero exists, it must be real and simple, and we denote it by β0.

Further, there exist absolute effectively computable constant c3 and c4 such

that if
 x ≥ exp(10nL(log ∆L)
2), (1.6)

then
 ∣
∣
∣
∣πC(x) − |C|
|G| Li(x)
∣
∣
∣
∣ ≤ |C|
|G| Li(xβ0) + c3x exp ( − c4n− 1
2
L (log x) 1
2 ), (1.7)

where the β0 term is present only when β0 exists.

Because of the presence of the β0 factor, Theorem 1.3 does not fully meet

our criterion of effectiveness, which is that the error term should depend only on

x, nL, ∆L, and |C|/|G|. However, this defect can be remedied by utilizing any

effective bound for β0. In most cases the best known such bound is that of Stark

[Sta74, p.148] which we quote below.

Theorem 1.4. Let the notation be as in Theorem 1.3, and let mL = 4 if 1 is

normal over Q, mL = 16 if there is a sequence of fields

Q = k1 ⊂ k1 ⊂ · · · ⊂ kr = L

with each field normal over the preceding one, and mL = 4nL! otherwise. Then

there exists an effectively computable absolute constant c5 such that

β0 < max
[
1 − (mL log ∆L)
−1, 1 − (c5∆1/nL
L )
−1]
. (1.8)

5

Effective versions of Chebotarev Typeset by the TeXromancers

Even if β0 does not exist, Theorem 1.3 does not give a good unconditional

bound for the smallest norm of a prime ideal whose Artin symbol is a given

conjugacy class. A reasonable conjecture might be that there should be an effec-

tively computable absolute constant c such that for every normal extension L/K

and every conjugacy class C of G(L/K), there should be an unramified p with[ L/K
p
 ] = C and
 NK/Q p ≤ (log ∆L)c. (1.9)

When L is a cyclomic extension of K = Q, (1.9) is equivalent to Linnik’s theorem

[Bom74, p.39]. However, if K = Q and L = Q(
√d) is a quadratic extension of

Q, the determinantion of the least prime p with [ L/Q
(p)
 ] ̸= {1} corresponds to

the problem of determining the least quadratic nonresidue (mod d), and for this

problem no unconditional bound better than

p ≤ c6∆c7
L (1.10)

is known, where c6 and c7 are positive constants. Thus without some major new

ideas it would probably be very difficult to prove an unconditional result as good

as (1.9). However, by using slightly different techniques (which are designed to

detect prime ideals rather than estimate their total number) one can prove the

following result [LMO79].

Theorem. There exist effectively computable positive absolute constants b1 and

b24 such that for every conjugacy class C of G there exists an unramified prime

ideal p of K such that [ L/K
p
 ] = C and

NK/Q p ≤ b1∆b2
L .

The approach used in this paper has a long history. The argument given here

6

Lagarias and Odlyzko Section 2: Outline of the main argument

may be viewed as a direct descendent of de la Vallee Poussin’s proof of the prime

number theorem. We follow closely with the pattern of Davenport’s treatment

[DM13] of the prime number theorem for arithmetic progressions. The main

innovation here is the careful treatment of the dependencies of various constants

on nL and ∆L (cf. [DM13]; [Fog61]; [Gol70]; [Lan71]; [Mor]).

Aside from some slight acquaintance with algebraic and analytic number the-

ory, this paper also assumes knowledge of the basic properties of Hecke and Artin

L-functions [Hei67]. The deepest of these results is the abelian reciprocity law,

which tells us that an abelian Artin L-series is a Hecke L-series, and so is analytic

for s ̸= 1.

Throughout this paper c1, c2, . . . will denote effectively computable positive

absolute constants. (In particular, they are independent of K and L.) The

Vinogradov notation
 f ≪ g

will be used to denote the existence of an effectively computable positive absolute

constant A (not necessary the esame in each occurance) such that

|f | ≤ Ag,

in the range indicated.

2 Outline of the main argument

The main argument is primarily concerned with the derivation of an asymptotic

formula with an explicit error term of a weighted prime-power-counting function

7

Effective versions of Chebotarev Typeset by the TeXromancers

ψC(x) = ψC(x, L/K) associated to πC(x, L/K). It is defined by

ψC(x, L/K) = ∑

NK/Q p
m≤x
p unramified[ L/K
p
 ]m=C
 log(NK/Q p)

The details of this argument are complicated, the main steps are simple in con-

ception:

(i) ψC(x) differs from a truncate inverse Mellin transform

IC(x, T ) = 1
2πi
 ∫ σ0+iT

σ0−iT FC(s) xs

s ds,

by a remainder term R1(x, T ).

(ii) FC(s) can in fact be written as a linear combination of logarithmic deriva-

tives of Hecke (abelian) L-functions. As a consequence, all the singularities

of FC(s), which are simply poles only, occur at zeroes and pole of ζL(s).

(iii) IC(x, T ) differs from a certain contour integral

BC(x, T ) = 1
2πi
 ∮

BT FC(s) xs

s ds,

by a remainder term R2(x, T ). This step is traditionally labelled “shifting

the line of integration to the left.”

Certain results on the density of zeros of ζL(s) in the critical strip

0 < Re s < 1 are necessary to estimate R2(x, T ).

(iv) The contour integral BC(x, T ) is evaluated by Cauchy’s residue theorem.

The integrand has poles at the zeroes and the pole of ζL(s), and the result

is a main term |C|
|G| x coming from the pole of ζL(s) at s = 1, together with

8

Lagarias and Odlyzko Section 3: Artin L-functions and Mellin
transform

a certain sum S(x, T ) over the zeroes of ζL(s) within the contour BT .

The end result of these steps is a truncated “explicit formula” for ψC(x)

with an unconditional error term, which is stated as Theorem 7.1

(v) The sum over the zeroes S(x, T ) is estimated. It is at this point that

unproved hypothesis about the zeroes can be helpful. An unconditional

upper bound for |S(x, T )| is obtained using the existence of a zero-free

region of ζL(s) near the vertical line σ = 1. A much better estimate for

|S(x, T )| is made assuming the Generalized Riemann hypothesis for ζL(s).

(vi) The asymptotic formula ψC(x) ∼ |C|
|G| x with an explicit remainder term is

derived by making an appropriate choice of T as a function of x, to minimize

the accumulated error terms. (This choice depends on whether the GRH is

assumed or not, of course.)

(vii) The asymptotic formula πC(x) ∼ |C|
|G| Li(x) with an explicit remainder term

is derived by partial summation from that for ψC(x).

The remaining sections of this paper carry out the details (although we will

not follow this outline exactly).

3 Artin L-functions and Mellin transform

In this section we establish the relation between ψC(x) and a certain truncated

inverse Mellin transform. Throughout this and subsequent sections we will use

the abbreviations πC(x), ψC(x) and N for πC(x, L/K), ψC(x, L/K), and NK/Q,

respectively. We will also use ϕ to denote irreducible characters of G = G(L/K).

For each irreducible character ϕ of G we define

ϕK(p
m) = 1
e
 ∑

α∈I ϕ(τ mα), (3.1)

9

Effective versions of Chebotarev Typeset by the TeXromancers

where I is the inertia group of P , one of the prime ideal factors of p, e = |I| and

τ is one of the Frobenius automorphisms corresponding to p. If L(s, ϕ, L/K) is

the Artin L-series associated to ϕ, then for Re(s) > 1 we have

− L′

L (s, ϕ, L/K) = ∑

p
 ∞∑

m=1 ϕK(p
m) log(N p)(N p)
−ms (3.2)

where the outer sum is over all the prime ideals of K. We should also note that

the definitions (3.1) and (3.2) apply equally well to reducible characters.

To single out those p
m with [ L/K
p
 ]m = C, we will use the characters ϕ.

(unfortunateky this works only to the extent that some extraneous prime powers

p
m corresponding to p that ramify in L are also included.) Suppose that g ∈ C.

We define a function fC : G −→ C by

fC = ∑

ϕ ϕ(g)ϕ. (3.3)

Then the orthogonality relations for characters imply that

fC(τ ) =
 



 |G|
|C| if τ ∈ C,

0 if τ /∈ C. (3.4)

Hence if
 FC(s) = − |C|
|G|
 ∑

ϕ ϕ(g) L
′

L (s, ϕ, L/K), (3.5)

then (3.2) through (3.5) show that for Re(s) > 1 we have the Dirichlet series

expansion
 FC(s) = ∑

p
 ∞∑

m=1 θ(p
m) log(N p)(N p)
−ms, (3.6)

10

Lagarias and Odlyzko Section 3: Artin L-functions and Mellin
transform

where for p unramified in L we have

θ(p
m) =
 




1 if [ L/K
p
 ]m = C,

0 otherwise,

and |θ(p
m)| ≤ 1 if p ramifies in L.

Equation (3.6) shows that except for the ramified prime factors, ψC(x) is a

partial sum of the coefficients of FC(s). To obtain ψC(x) from FC(s) we will

use the following well-known truncated version of the inverse Mellin transform

[Tsc26, p. 54], [DM13, pp. 109-110].

Lemma 3.1. If y > 0, σ > 0, and T > 0, then

∣
∣
∣
∣ 1
2πi
 ∫ σ+iT

σ−iT
 ys

s ds − 1
∣
∣
∣
∣ ≤ yσ min(1, T −1| log y|
−1) if y > 1

∣
∣
∣
∣ 1
2πi
 ∫ σ+iT

σ−iT
 ys

s ds − 1
2
 ∣
∣
∣
∣ ≤ σT −1 if y = 1

and
∣
∣
∣
∣ 1
2πi
 ∫ σ+iT

σ−iT
 ys

s ds
∣
∣
∣
∣ ≤ yσ min(1, T −1| log y|
−1) if 0 < y < 1.

Let σ0 > 1, x ≥ 2, and define

IC(x, T ) = 1
2πi
 ∫ σ0+iT

σ0−iT FC(s) xs

s ds. (3.7)

Since the Dirichlet series in (3.6) is absolutely convergent for Re(s) > 1, we can

integrate term by term (with the help of Lemma 3.1) to obtain

∣
∣
∣
∣
∣IC(x, T ) − ∑

p,m
N p
m≤x
 θ(p
m) log N p

∣
∣
∣
∣
∣ ≤ ∑

p,m
N p
m=x
{log N p + σ0T −1} + R0(x, T ), (3.8)

11

Effective versions of Chebotarev Typeset by the TeXromancers

where
 R0(x, T ) = ∑

p,m
N p
m̸=x
 ( x
N pm
 )σ0 min (1, T −1∣
∣
∣ log x
N pm
 ∣
∣
∣
−1) log N p (3.9)

and where the sum on the right side of (3.8) is present only when there are p and

m with N p
m = x. Now the sum of the left side of (3.8) equals ψC(x), except

for the ramified prime terms. However, N p ≥ 2 for each prime ideal p, all the

ramified prime ideals p divide the discriminant of L over K, and so

∣
∣
∣
∣
∣
 ∑

p,m
N p
m≤x
 θ(p
m) log N p − ψC(x)
∣
∣
∣
∣
∣ ≤ ∑

p,m
p ramified
N p
m≤x
 log N p

≤ ∑

p
p ramified
 log N p ∑

m
N p
m≤x
 1

≤ 2 log x ∑

p
p ramified
 log N p

≤ 2 log x log ∆L

(We should remark that this estimate would be the same even if C were a union

of conjugacy classes.) Also, there are at most nK distinct pair (p, m) such that

N p
m = x, and so ∑

p,m
N p
m=x
 log N p ≤ nK log x.

Thus (3.8) yields
 ψC(x) = IC(x, T ) + R1(x, T ), (3.10)

where
 R1(x, T ) ≤ 2 log x log ∆L + nKσ0T −1 + nK log x + R0(x, T ). (3.11)

12

Lagarias and Odlyzko Section 3: Artin L-functions and Mellin
transform

The remainder of this section is devoted to establishing an estimate for R0(x, T ).

So far we allowed σ0 to be any number > 1. We now define

σ0 = 1 + (log x)
−1. (3.12)

While this is only one of many possible choices, it is quite convenient, not least

because of the relation xσ0 = ex.

We now write R0(x, T ) = S1 + S2 + S3, where S1 consists of those terms of

(3.9) for which N p
m ≤ 3
4 x or N p
m ≥ 5
4 x, S2 of those for which |x − N p
m| ≤ 1,

and S3 of the remaining ones. If N p
m ≤ 3
4 x or N p
m ≥ 5
4 x, then

∣
∣
∣ log x
N pm
 ∣
∣
∣ ≥ log 5
4 ,

min (1, T −1∣
∣
∣ log x
N pm
 ∣
∣
∣−1) ≪ T −1 for T ≥ 1,

and so
 S1 ≪ xT −1 ∑

p,m(N p)
−mσ0 log N = xT −1[ − ζ ′
K
ζK (σ0)
]. (3.13)

To bound this term we use an auxiliary result.

Lemma 3.2. For σ > 1,
 − ζ ′
K
ζK (σ) ≤ −nK ζ ′
Q
ζQ (σ).

Proof. We have

− ζ ′
K
ζK (σ) = ∑

p
 log N p
(N p)σ − 1 , − ζ ′
Q
ζQ (σ) = ∑

p
 log p
pσ − 1

where in the second sum p runs through the rational primes. Now for each prime

13

Effective versions of Chebotarev Typeset by the TeXromancers

ideal p, N p = p
k for some positive integer k. Thus

log N p
(N p)σ − 1 = k log p
pkσ − 1 = k
p(k−1)σ + · · · + 1 · log p
pσ − 1 ≤ log p
pσ − 1 .

Also, there are at most NK distinct p lying over a given rational prime p, so that

− ζ ′
K
ζK (σ) ≤ nK ∑

p
 log p
pσ − 1 = −nk ζ ′
Q
ζQ (σ)

Since
 − ζ ′
Q
ζQ (σ) ≪ (σ − 1)−1

for σ > 1, Lemma 3.2 and (3.13) show that for T ≥ 1,

S1 ≪ nKxT −1 log x. (3.14)

The second sum S2 consists of those terms p
m for which 0 < | N p
m − x| ≤ 1.

There are at most 2nK of such p
m and since

min (1, T −1∣
∣
∣ log x
N pm
 ∣
∣
∣−1) ≤ 1,

we obtain
 S2 ≤ 2nK log(x + 1)( x
x − 1
 )σ0 ≪ nK log x. (3.15)

The final sum S3 consists of those terms p
m for which 1 < | N p
m − x| < 1
4 x. Here

we use the estimate ∣
∣
∣ log x
n
 ∣
∣
∣−1 ≤ 2n
|x − n| ,

14

Lagarias and Odlyzko Section 4: Reduction to the case of Hecke
L-functions

valid for N ≥ 1
2 x, to obtain

S3 ≪ T −1 log x ∑

n
1<|n−x|< 1
4 x
 ∣
∣
∣ log x
n
 ∣
∣
∣−1 ∑

p,m
N p
m=n
 1

≪ nKxT −1 log x ∑

1≤k< 1
4 x
 1
k

≪ nKxT −1(log x)
2. (3.16)

Putting (3.14)-(3.16) together we obtain

R0(x, T ) ≪ nK log x + nKxT −1(log x)
2, (3.17)

valid for all x ≥ 2, T ≥ 1. If we now combine (3.17) with (3.11), we obtain finally

the estimate
 R1(x, T ) ≪ log x log ∆L + nK log x + nKxT −1(log x)
2, (3.18)

valid for all x ≥ 2, T ≥ 1, which was the goal of this section. We should mention

here that the log x log ∆L term in (3.18) (which came from the ramified primes)

would have been the same even if C were to be the union of any number of

conjugacy classes. Let us also note that if L ̸= Q, then nK ≤ nL ≪ log ∆L, and

so the second term on the right side of (3.18) can be absorbed in the first one.

4 Reduction to the case of Hecke L-functions

Our definition (3.5) of FC(s) was in terms of Artin L-functions corresponding

to the (usually nonlinear) characters of G(L/K). In this section we show that

FC(s) can be written in terms of Hecke (abelian) L-functions. This will enable

us to obtain much better results on the location and density of the singularities

15

Effective versions of Chebotarev Typeset by the TeXromancers

of FC(s). The reduction we will use is due to Deuring [Deu35] (later rediscovered

by MacCluer [Mac68]). We learned of it from [Mor], and should like to thank

J. P. Serre for bringing Moreno’s paper to our attention and for supplying the

following formulation of Deuring’s idea.

In defining FC(s) by (3.5), we have already selected an element g ∈ C. Let

H = ⟨g⟩ be the cyclic group generated by g, E the fixed field of H, and let χ

denote the irreducible characters of H. Since H is cyclic, the characters χ are

one-dimensional. We will retain this notation for the rest of this paper.

Lemma 4.1. We have

FC(s) = − |C|
|G|
 ∑

χ χ(g) L
′

L (s, χ, L/E). (4.1)

Proof. Let τ : H −→ C be the class function defined by

τ (h) =
 




|H| if h = g,

0 if h ̸= g.

Then the orthogonality relations for characters of H imply that

τ = ∑

χ χ(g) χ.

Let τ ∗ denote the class function on G induced by τ , which by direct calculation

equals
 τ ∗(y) =
 



∣
∣CG(g)
∣
∣ y ∈ C,

0 y /∈ C,

where CG(g) is the centralizer of g in G. Now ∣
∣CG(g)
∣
∣∣
∣C∣
∣ = ∣
∣G
∣
∣ so that τ ∗ = fC

16

Lagarias and Odlyzko Section 5: Density of zeroes of Hecke
L-functions

[see (3.4)]. This implies ∑

χ χ(g)χ∗ = ∑

ϕ ϕ(g)ϕ,

so that for Re (s) > 1 we have

FC(s) = − |C|
|G|
 ∑

χ χ(g) L′

L (s, χ
∗, L/K). (4.2)

But L(s, χ
∗, L/K) = L(s, χ, L/E), and so (4.1) holds for Re (s) > 1, and therefore

(by analytic continuation) for all s.

5 Density of zeroes of Hecke L-functions

We have now shown that for x ≥ 2 and T ≥ 1, say,

ψC(x) = IC(x, t) + R1(x, T ),

where R1(x, T ) satisfies (3.18) and

IC(x, T ) = − |C|
|G|
 ∑

χ χ(g) 1
2πi
 ∫ σ0+iT

σ0−iT
 xs

s L
′

L (s, χ, L/E)ds, (5.1)

where σ0 = 1 + (log x)
−1 and χ runs through the (one-dimensional) irreducible

characters of H = ⟨g⟩. Our next goal will be to evaluate each of the integrals

in (5.1). [This turns out to be more convenient than integrating FC(s).] To

accomplish this we will need some upper bounds on the number of singularities

of L′ / L.

Since L and E are going to be fixed from now on, we will use L(s, χ) to denote

L(s, χ, L/E). Also, we let F (χ) denote the conductor of χ and set

A(χ) = ∆E NE/Q(F (χ)) (5.2)

17

Effective versions of Chebotarev Typeset by the TeXromancers

and
 δ(χ) =
 



1 if χ = χ1, the principal character,

0 otherwise. (5.3)

We recall that for each χ there exist non-negative integers a = a(χ), b = b(χ)

such that
 a(χ) + b(χ) = nE, (5.4)

and such that if we define

γχ(s) = [
π− s+1
2 Γ( s + 1
2
 )]b[
π− s
2 Γ
( s
2
 )]a (5.5)

and
 ξ(s, χ) = [s(s − 1)]
δ(χ)A(χ)
s/2γχ(s) L(s, χ), (5.6)

then ξ(s, χ) satisfies the functional equation

ξ(1 − s, χ) = W (χ)ξ(s, χ), (5.7)

where W (χ) is a certain constant of absolute value 1. Furthermore, ξ(s, χ) is

an entire function of order 1 and does not vanish at s = 0, and hence by the

Hadamard product theorem we have

ξ(s, χ) = eB1(χ)+B(χ)s ∏

ρ
 (1 − s
ρ
 )es/ρ (5.8)

for some constants B1(χ) and B(χ) where ρ runs through all the zeroes of ξ(s, χ),

which are precisely those zeroes ρ = β + iγ of L(x, χ) for which 0 < β < 1 [the

so-called “nontrivial zeroes” of L(s, χ)]. [We recall that L(s, χ) and hence ξ(s, χ)

have no zeroes ρ with Re (ρ) ≥ 1.] From now on ρ will denote the nontrivial

zeroes of L(s, χ).
 18

Lagarias and Odlyzko Section 5: Density of zeroes of Hecke
L-functions

Since we are interested in the integrals in (5.1), which involve L′/L, we dif-

ferentiate (5.6) and (5.8) logarithmically to obtain the important identity

L′

L (s, χ) = B(χ)+∑

ρ
 ( 1
s − ρ + 1
ρ
 )− 1
2 log A(χ)−δ(χ)
[ 1
s + 1
s − 1
 ]− γ′χ
γχ (s), (5.9)

valid identically in the complex variable s. A difficulty in the use of this formula

is caused by the presence of the constant B(χ), which depends in an as-yet-

undetermined way on χ. However, since (s−1)
δ(χ) L(s, χ) is entire, the functional

equation (5.7) easily implies the following result which is proved in [Odl77].

Lemma 5.1. With notation as above,

Re B(χ) = − ∑

ρ Re 1
ρ , (5.10)

and

L′

L (s, χ) + L
′

L (s, χ) = ∑

ρ
 ( 1
s − ρ + 1
s − ρ
 ) − log A(χ)

− 2δ(χ)
( 1
s + 1
s − 1
 ) − 2 γ′χ
γχ (s) (5.11)

holds identically in the complex variable s, where ρ runs through the nontrivial

zeroes of L(s, χ).

This lemma will enable us to obtain estimates of both of B(χ) and of the

density of zeroes of L(s, χ). We should mention, however, that an analog of the

above lemma could be proved for general Artin L-functions, but it would contain

sums over the possible poles of such L-functions, and these pole terms would

prevent us from obtaining an estimate as good as the one below. The purpose of

the preceding section’s reduction to the case of abelian L-function was to avoid

these difficulties.
 19

Effective versions of Chebotarev Typeset by the TeXromancers

We first derive some easy auxiliary results.

Lemma 5.2. If σ = Re (s) > 1, then

∣
∣
∣ L′

L (s, χ)
∣
∣
∣ ≪ nE
σ − 1 .

Proof. A comparison of the Dirichlet series shows that

∣
∣
∣ L
′

L (s, χ)
∣
∣
∣ ≤ − ζ ′
E
ζE (σ),

and the result follows from Lemma 3.2.

Lemma 5.3. If σ = Re (s) > −1/2 and |s| ≥ 1/8, then

∣
∣
∣
∣ γ′
χ
γχ (s)
∣
∣
∣
∣ ≪ nE log (|s| + 2).

Proof. This lemma follows from the definition of γχ(s) and the fact that

Γ
′

Γ (z) ≪ log (|z| + 2)

for z satisfying |z| ≥ 1/16, Re z > −1/4 [WW96, p.251] (cf. Lemma 6.1).

We now come to the main result of this section. We let nχ(t) denote the

number of zeroes ρ = β + iγ of L(s, χ) with 0 < β < 1, |γ − t| ≤ 1.

Lemma 5.4. For all t we have

nχ(t) ≪ log A(χ) + nE log (|t| + 2). (5.12)

Proof. We evaluate (5.11) at s = 2 + it. Lemmas 5.2 and 5.3 imply that

∑

ρ Re ( 1
s − ρ + 1
s − ρ
 ) ≪ log A(χ) + nE log (|t| + 2). (5.13)

20

Lagarias and Odlyzko Section 5: Density of zeroes of Hecke
L-functions

But Re (s − ρ)
−1 > 0 and Re (s − ρ)
−1 > 0 since 2 = Re (s) > Re (ρ) so

∑

ρ Re ( 1
s − ρ + 1
s − ρ
 ) ≥ ∑

ρ
|γ−t|≤1
 2 − β
(2 − β)2 + (t − γ)2

≥ ∑

ρ
|γ−t|≤1
 1
5 = 1
5 nχ(t),

since 1 < 2 − β < 2, which proves the lemma.

The bound (5.12) (which is essentially best possible) will be crucial in many

of our subsequent arguments. In the case of general Artin L-functions, we could

obtain an estimate similar to (5.13), but it would be for the difference of a sum

over the zeroes and a similar sum over the poles and the real part of the poles’

contribution would be negative.

We now utilize Lemma 5.4 to obtain two additional auxiliary results. We first

show that B(χ) depends mostly on the very small zeroes of L(s, χ).

Lemma 5.5. For any ε with 0 < ε ≤ 1 we have

B(χ) + ∑

ρ
|ρ|<ε
 1
ρ ≪ ε−1( log A(χ) + nE).

Proof. Set s = 2 in (5.9) and use lemmas 5.2 and 5.3 to estimate the L(s, χ) and

γχ terms, respectively. We obtain

B(χ) + ∑

ρ
 ( 1
2 − ρ + 1
ρ
 ) ≪ log A(χ) + nE.

Now ∣
∣
∣ 1
2 − ρ + 1
ρ
 ∣
∣
∣ = 2
∣
∣ρ(2 − ρ)∣
∣ ≤ 2
|ρ|2

21

Effective versions of Chebotarev Typeset by the TeXromancers

and so Lemma 5.4 implies

∑

ρ
|ρ|≥1
 ∣
∣
∣ 1
2 − ρ + 1
ρ
 ∣
∣
∣ ≪
 ∞∑

j=1
 nχ(j)
j2 ≪ log A(χ) + nE.

Also, |2 − ρ| ≥ 1, so ∑

|ρ|<1
 ∣
∣
∣ 1
2 − ρ
 ∣
∣
∣ ≪ log A(χ) + nE,

and hence
 B(χ) + ∑

ρ
|ρ|<ε
 1
ρ ≪ ∑

ρ
ε≤|ρ|<1
 1
|ρ| + log A(χ) + nE,

which together with Lemma 5.4 completes the proof.

Lemma 5.6. If s = σ + it with −1/2 ≤ σ ≤ 3, |s| ≥ 1/8, then

∣
∣
∣
∣ L′

L (s, χ) + δ(χ)
s − 1 − ∑

ρ
|γ−t|≤1
 1
s − ρ
 ∣
∣
∣
∣ ≪ log A(χ) + nE log (|t| + 2).

Proof. We evaluate (5.9) at σ + it and 3 + it and subtract the resulting relations

[in order to eliminate B(χ)] to obtain

L
′

L (s, χ) − L′

L (3 + it, χ) = ∑

ρ
 ( 1
s − ρ − 1
3 + it − ρ
 ) − γ′χ
γχ (s)

+ γ′χ
γχ (3 + it) − δ(χ)
( 1
s + 1
s − 1 − 1
2 + it − 1
3 + it
 ).

We now use Lemmas 5.2 and 5.3 to estimate the L(3 + it, χ) and the gamma

22

Lagarias and Odlyzko Section 6: The contour integral

factors, respectively. We discover that

∣
∣
∣
∣
∣ L′

L (s, χ)+ δ(χ)
s − 1 − ∑

ρ
|γ−t|≤1
 1
s − ρ
 ∣
∣
∣
∣
∣ ≪ nE log (|t| + 2)+ ∑

ρ
|γ−t|>1
 ∣
∣
∣ 1
s − ρ − 1
3 + it − ρ
 ∣
∣
∣

+ ∑

ρ
|γ−t|≤1
 ∣
∣
∣ 1
3 + it − ρ
 ∣
∣
∣. (5.14)

Since |3 + it − ρ| > 1 for all ρ and there are nχ(t) terms in the last sum, it

is ≪ log A(χ) + nE log (|t| + 2). For the first sum on the right side of (5.14) we

have
 ∑

ρ
|γ−t|>1
 ∣
∣
∣ 1
s − ρ − 1
3 + it − ρ
 ∣
∣
∣ = ∑

ρ
|γ−t|>1
 3 − σ
∣
∣s − ρ∣
∣∣
∣3 + it − ρ
∣
∣

≪
 ∞∑

j=1
 nχ(t + j) + nχ(t − j)
j2

≪ log A(χ) + nE log (|t| + 2),

and this proves the lemma.

6 The contour integral

The next step in the proof is to evaluate IC(x, T ) by evaluating

Iχ(x, T ) = 1
2πi
 ∫ σ0+iT

σ0−iT
 xs

s L
′

L (s, χ)ds (6.1)

for each character χ of H = ⟨g⟩. So far the only condition on T was T ≥ 1.

We now impose the additional requirement that T should not coincide with the

ordinate of a zero of any of the L(s, χ). We also introduce a new parameter, U ,

which will satisfy U = j + 1/2 for some non-negative integer j (eventually we will

23

Effective versions of Chebotarev Typeset by the TeXromancers

let U → ∞) and define

Iχ(x, T, U ) = 1
2πi
 ∫

BT ,U
 xs

s L′

L (s, χ)ds, (6.2)

where BT,U is the positively oriented rectangle with vertices at σ0 − iT , σ0 + iT ,

−U + it and −U − it. Now Iχ(x, T, U ) can easily be evaluated exactly in terms

of the singularities of the integrand as we we will show in the next section. In

this section, we will show that

Rχ(x, T, U ) = Iχ(x, T, U ) − Iχ(x, T ) (6.3)

is small.

The remainder Rχ(x, T, U ) may be divided into the vertical integral

Vχ(x, T, U ) = 1
2π
 ∫ T

−T
 x−U +it

−U + it L′

L (−U + it, χ)dt (6.4)

and the two horizontal integrals

Hχ(x, T, U ) = 1
2πi
 ∫ −1/4

−U
 { xσ−iT

σ − iT L′

L (σ − iT, χ) − xσ+iT

σ + iT L′

L (σ + iT, χ)}
dσ,

(6.5)

H ∗
χ(x, T ) = 1
2πi
 ∫ σ0

−1/4
 { xσ−iT

σ − iT L′

L (σ − iT, χ) − x
σ+iT

σ + iT L′

L (σ + iT, χ)
}
dσ. (6.6)

Vχ and Hχ will be estimated by using Lemma 6.2 to bound L′ / L. First, however,

we prove an auxiliary result about the digamma function.

Lemma 6.1. If |z + k| ≥ 1/8 for all non-negative integers k, then

Γ′

Γ (z) ≪ log(|z| + 2).

Proof. If Re(z) ≥ 1, this is well known [WW96, p.251]. If Re(s) < 1, then the

24

Lagarias and Odlyzko Section 6: The contour integral

recurrence relation Γ
′

Γ (u) = Γ
′

Γ (u + 1) − 1
u

iterated m times shows that

Γ′

Γ (z) = Γ′

Γ (z + m) −
 m−1∑

k=0
 1
z + k

for any positive integer m. Choose m = ⌊|z| + 2⌋. Then Re(z + m) > 1, so that

Γ′

Γ (z + m) ≪ log(|z| + 2),

while |z + k| ≥ 1/8 for all non-negative integers k implies

m−1∑

k=0
 1
z + k ≪
 m−1∑

k=0
 1
k + 1/8 ≪ log(|z| + 2),

which proves the lemma.

Lemma 6.2. If s = σ + it with σ ≤ −1/4, and |s + m| ≥ 1/4 for all non-negative

integers m, then L′

L (s, χ) ≪ log A(χ) + nE log(|s| + 2).

Proof. The functional equation (5.7) and the definitions (5.5) and (5.6) imply

that L
′

L (s, χ) = − L
′

L (1 − s, χ) − log A(χ) − γ′
χ
γχ (1 − s) − γ′
χ
γχ (s). (6.7)

Since Re(1 − s) ≥ 5/4, we can use Lemma 5.2 to bound (L
′ / L)(1 − s, χ). The

lemma then follows by an application of Lemma 6.1 to estimate the γχ terms.

Estimates for Vχ(x, T, U ) and Hχ(x, T, U ) are now very easy to obtain. By the

above lemma we have the crude estimates (U = j+1/2 so that |−U +it+m| ≥ 1/4

25

Effective versions of Chebotarev Typeset by the TeXromancers

for all integers m)

Vχ(x, T, U ) ≪ x−U

U
 ∫ T

−T
 ∣
∣
∣ L
′

L (−U + it, χ)∣
∣
∣dt ≪ x−U

U T {log A(χ) + nE log(T + U )},

(6.8)

and

Hχ(x, T, U ) ≪ ∫ −1/4

∞
 x
σ

T (log A(χ) + nE log(|σ| + 2) + nE log T )dσ

≪ x−1/4

T {log A(χ) + nE log T } (6.9)

Better estimates can easily be obtained, but would not be too significant, since

other error terms will be much larger.

It remains to estimate H ∗
χ(x, T ). Lemma 5.6 shows that

L′

L (σ + iT, χ) − ∑

ρ
|γ−T |≤1
 1
σ + iT − ρ ≪ log A(χ) + nE log T

if −1/4 ≤ σ ≤ σ0 = 1 + (log x)
−1, x ≥ 2, T ≥ 2, and a similar estimate holds for

L
′ / L at σ − iT . Therefore,

H ∗
χ(x, t)− 1
2πi
 ∫ σ0

−1/4
 { xσ−iT

σ − iT
 ∑

ρ
|γ+T |≤1
 1
σ − iT − ρ − xσ+iT

σ + iT
 ∑

ρ
|γ−T |≤1
 1
σ + iT − ρ
 }

dσ

≪ ∫ σ0

−1/4
 xσ

T {log A(χ) + nE log T }dσ

≪ x
T log x {log A(χ) + nE log T } (6.10)

To complete our estimate we show that the first integral in (6.10) is not too large.

Lemma 6.3. Let ρ = β + iγ have 0 < β < 1, γ ̸= t. If |t| ≥ 2, x ≥ 2, and

26

Lagarias and Odlyzko Section 6: The contour integral

1 < σ1 ≤ 3, then

∫ σ1

−1/4
 xσ+it

(σ + it)(σ + it − ρ) dσ ≪ |t|−1x
σ1(σ1 − β)−1.

Proof. Suppose first that γ > t. Let B be the rectangle with vertices at

σ1 + i(t − 1), σ1 + it, − 1
4 + it, − 1
4 + i(t − 1), oriented counterclockwise. By

Cauchy’s theorem, ∫

B
 xs

s(s − ρ) ds = 0

since the integrand has no singularities inside the contour. However, on the three

sides of the rectangle other than the segment from −1/4 + it to σ1 + it, the

integrand is majorized by xσ1

(|t| − 1)(σ1 − β)

which proves the result for γ > t. A similar proof for γ < t uses the rectangle

with vertices at σ0 + i(t + 1), σ0 + it, −1/4 + it, −1/4 + i(t + 1).

The above lemma shows that

1
2πi
 ∫ σ0

−1/4
 xσ−iT

σ − iT
 ( ∑

ρ
|γ+T |≤1
 1
σ + iT − ρ
 )

dσ ≪ xσ0

T (σ0 − 1)
−1nχ(−T )

≪ x log x
T (log A(χ) + nE log(T )) (6.11)

for x ≥ 2, T ≥ 2, and the same estimate holds for the integral involving zeroes

ρ with |γ − T | ≤ 1. [Note that if we assume the GRH for L(s, χ), then we can

delete the log x term in (6.11). Also, even without the GRH we could replace

log x by log log x by improving Lemma 6.3.] Therefore we finally obtain

H ∗
χ(x, T ) ≪ x log x
T (log A(χ) + nE log T ). (6.12)

27

Effective versions of Chebotarev Typeset by the TeXromancers

If we now combine (6.8), (6.9), and (6.12), we obtain the main result of this

section, namely that

Iχ(x, T ) − Iχ(x, T, U ) = −Vχ(x, T, U ) − Hχ(x, T, U ) − H ∗
χ(x, T )

≪ x log x
T {log A(χ) + nE log T }

+ T x
−U

U {log A(χ) + nE log(T + U )}. (6.13)

7 The explicit formula

In this section we combine the results of preceding sections in order to obtain an

explicit formula for ψC(x) in terms of the zeroes ρ.

We first evaluate the integral Iχ(x, T, U ) which was defined by (6.2). We recall

that x ≥ 2, U = j +1/2 for some non-negative integer j, and T ≥ 2 does not equal

the ordinate of any zero of any of the L(s, χ). By Cauchy’s theorem, Iχ(x, T, U )

equals the sum of the residues of the integrand at poles inside BT,U . Now if

χ = χ1, the principal character, then L′ / L has a first order pole of residue −1

at s = 1, and hence (this term being absent if χ ̸= χ1) we obtain a contribution

of
 −δ(χ)x

from the possible pole at s = 1. Further, L′ / L has a first order pole with residue

+1 at each nontrivial zero ρ of L(s, χ) (the ρ’s are counted according to their

multiplicity), and so such ρ’s contribute

∑

ρ
 xρ

ρ .

In addition, L
′ / L has first order poles at the so-called trivial zeroes, which are

real and nonpositive. In fact, (6.7) shows that L′ / L has first order poles at

28

Lagarias and Odlyzko Section 7: The explicit formula

s = −(2m − 1), m = 1, 2, . . . , where the residue is b(χ), and first order poles

at s = −2m, m = 0, 1, 2, . . . , where the residue if a(χ). Hence the residues at

points s with Re(s) < 0 contribute

−b(χ)
 ⌊(u+1)/2⌋∑

m=1
 x−(2m−1)

2m − 1 − a(χ)
 ⌊U/2⌋∑

m=1
 x−2m

2m .

The only remaining residue is at s = 0, where we have the complication that

both xs/s and L′ / L may have first order poles. The Laurent series expansions

show that there exist functions h1(s) and h2(s) which are analytic at s = 0 [h2(s)

depends on χ], such that
 xs

s = 1
s + log x + h1(s)s,

and [using (5.9)]
 L′

L (s, χ) = a(χ) − δ(χ)
s + r(χ) + h2(s)s,

where

r(χ) = B(χ) − 1
2 log A(χ) + nE
2 log π + δ(χ) − b(χ)
2 Γ
′

Γ
 ( 1
2
 ) − a(χ)
2 Γ′

Γ (1). (7.1)

Hence the residue at s = 0 is

r(χ) + (a(χ) − δ(χ)) log x.

29

Effective versions of Chebotarev Typeset by the TeXromancers

If we now collect all the residue terms, we find that

Iχ(x, T, U ) = −δ(χ)x + ∑

ρ
|γ|<T
 xρ

ρ − b(χ) +
 ⌊(u+1)/2⌋∑

m=1
 x1−2m

2m − 1

− a(χ)
 ⌊u/2⌋∑

m=1
 x−2m

2m + r(χ) + (a(χ) − δ(χ)) log(x). (7.2)

We now let U → ∞. Then (7.2) and (6.13) give us the explicit formula

Iχ(x, T ) + δ(χ)x − ∑

ρ
|γ|<T
 xρ

ρ − r(χ) − (a(χ) − δ(χ)) log x

− nE
2 log(1 − x−1) + 1
2 (b(χ) − a(χ)) log(1 + x−1)

≪ x log x
T {log A(χ) + nE log T }, (7.3)

valid for all x ≥ 2 and all T ≥ 2 which do not coincide with the ordinate of a

zero. If we now let T → ∞, (7.3) would give us an explicit formula for the inverse

Mellin transform 1
2πi
 ∫ σ0+i∞

σ0−i∞
 xs

s L
′

L (s, χ)ds

with no error term. However, for our purposes a cruder version of (7.3) will be

more useful.

Theorem 7.1. If x ≥ 2 and T ≥ 2, then

ψC(x)− |C|
|G| x+S(x, T ) ≪ |C|
|G|
 { x log x + T
T log ∆L +nL log x+ nLx log x log T
T
 }

+ log x log ∆L + nKxT −1(log x)
2, (7.4)

30

Lagarias and Odlyzko Section 7: The explicit formula

where
 S(x, T ) = |C|
|G|
 ∑

χ χ(g)
{ ∑

ρ
|γ|<T
 xρ

ρ − ∑

ρ
|ρ|< 1
2
 1
ρ
 }

. (7.5)

[The inner sums in (7.5) are over the nontrivial zeroes ρ of L(s, χ)].

Proof. Lemma 5.5 and (5.4) show that

r(χ) − ∑

ρ
|ρ|< 1
2
 1
ρ ≪ log A(χ) + nE,

and so

Iχ(x, T )+δ(χ)x− ∑

ρ
|γ|<T
 xρ

ρ − ∑

ρ
|ρ|< 1
2
 1
ρ ≪ log A(χ)+nE log x+ x log x
T {log A(χ)+nE log T }.

Hence by (5.1) and (6.1) we have for x ≥ 2, T ≥ 2 [T not coinciding with the

ordinate of any zero ρ of any L(s, χ)]

IC(x, T ) − |C|
|G|
 ∑

χ χ(g)
{

δ(χ)x − ∑

ρ
|γ|<T xρ
ρ
 − ∑

ρ
|ρ|< 1
2
 1
ρ
 }

≪ |C|
|G|
 ∑

χ
 { x log x + T
T log A(χ) + nE log x + nEx log x log T
T
 }

≪ |C|
|G|
 { x log x + T
T log ∆L + nL log x + nLx log x log T
T
 }

since ∑

χ log A(χ) = log ∆L

by the conductor-discriminant formula, and nE · [L : E] = nL. Since

ψC(x) = IC(x, T )+R1(x, T ), where R1(x, T ) satisfies (3.18), we obtain the bound

of the theorem, provided T does not equal the ordinate γ of some zero ρ = β + iγ.

31

Effective versions of Chebotarev Typeset by the TeXromancers

If, however, T = γ for some ρ, then we evaluate (7.4) with T replaced with T + ε

for a very small ε, and let ε → 0. The possible discontinuity in the function on

the left side comes from zeroes ρ with T = γ, and since there are ≪ ∑ nχ(T )

of them, their contribution can be absorbed in the error term by increasing the

constant implied by the ≪ notation.

The above theorem, which is the main result of this paper, serves to exhibit

ψC(x) as consisting of the main term |C|
|G| x, of S(x, T ), and of a relatively small

remainder. In the rest of this paper we will be concerned with estimating S(x, T ).

If we assume the GRH, then a good bound for S(x, T ) can be easily given with

what we already know. In order to obtain an unconditional result, however, we

need to show that the zeroes ρ do not approach close to the line Re(s) = 1.

8 Zero-free regions

In this section we will use the classical method to prove a zero-free region for

ζL(s). Since
 ζL(s) = ∏

χ L(s, χ) (8.1)

and the L(s, χ) are all analytic for s ̸= 1, any zero-free region for ζL(s) imme-

diately implies one for each of the L(s, χ). This approach does have the serious

disadvantage that one can often obtain directly with the L(s, χ) (cf. [DM13, Ch.

14]); in fact, one can essentially replace log ∆L by max(log A(χ)) and nL with

nE in the estimates below. The problem with that result is that in general nE

can be almost as large as nL and max(log A(χ)) almost as large as ∆L. Finally,

we should mention that for a fixed L a better zero-free region can be obtained by

more sophisticated methods [Sok68], but the published versions are not explicit

as to the dependence on the field L.
 32

Lagarias and Odlyzko Section 8: Zero-free regions

Lemma 8.1. There is an absolute, effectively computable constant c8 such that

ζL(s) has no zeroes ρ = β + iγ in the region

|γ| ≥ (1 + 4 log ∆L)−1

β ≥ 1 − c8(log ∆L + nL log(|γ| + 2))−1

Proof. We have
 − ζ ′
L
ζL =
 ∞∑

m=1 α(m)m
−s (8.2)

for σ = Re(s) > 1, where α(m) ≥ 0 for all m. Hence

Re ( − 3 ζ ′
L
ζL (σ) − 4 ζ ′
L
ζL (σ + it) − ζ ′
L
ζL (σ + 2it))

=
 ∞∑

m=1 α(m)m
−σ(3 + 4 cos(t log m) + cos(2t log m)) ≥ 0

by the classical identity

3 + 4 cos θ + 2 cos θ = 2(1 + cos θ)2 ≥ 0

If we now consider the trivial normal extension L of L, then ζL(s) is the Artin L-

function associated to the principal character, and if γL(s) denotes the associated

gamma factor then (5.11) shows that

2 ζ ′
L
ζL (s) = ∑

ρ
 ( 1
s − ρ + 1
s − ρ
 ) − log ∆L − 2
s − 2
s − 1 − 2 γ′
L
γL (s), (8.3)

where the summation is over the nontrivial zeroes ρ of ζL(s). We note here that

if Re s > 1, then Re(s − ρ)
−1 > 0 for each zero ρ. If ρ = β + iγ is some particular

33

Effective versions of Chebotarev Typeset by the TeXromancers

zero with γ ≥ (1 + 4 log ∆L)
−1, then we find that for σ > 1,

− ζ ′
L
ζL (σ) ≤ 1
σ − 1 + 1
σ + 1
2 log ∆L + γ′
L
γL (σ) − ∑

ρ Re(σ − ρ)
−1

≤ 1
σ − 1 + c9 log ∆L + c9nL,

− Re ζ ′
L
ζL (σ + 2iγ) ≤ 1
2 log ∆L + Re { 1
σ + 2iγ − 1 + 1
σ + 2iγ
 } + Re γ′
L
γL (σ + 2iγ)

≤ c10 log ∆L + c10nL log(|γ| + 2),

and
 − Re ζ ′
L
ζL (σ + iγ) ≤ c11 log ∆L + c11nL log(|γ| + 2) − 1
σ − β ,

where in the last inequality we have included the contribution of the zero

ρ = β + iγ. These inequalities and (8.2) show that for all σ > 1

4
σ − β < 3
σ − β + c12{log ∆L + nL log(|γ| + 2)}

If we now set σ = 1 + (100c12)
−1{log ∆L + nL log(|γ| + 2)}
−1, say, then we obtain

the result of the lemma.

In addition to Lemma 8.1 we also need information about zeroes ζL(s) very

near the real axis. Such information can be obtained by methods very similar to

those used above.

Lemma 8.2. If nL > 1 then ζL(s) has at most one zero ρ = β + iγ in the region

|γ| ≤ (4 log ∆L)
−1, (8.4)

β ≥ 1 − (4 log ∆L)
−1

34

Lagarias and Odlyzko Section 9: Final estimates

This zero, if it exists, has to be real and simple.

Proof. Identity (8.3) shows that for 1 < σ ≤ 2

∑

ρ
 σ − β
(σ − β)2 + γ2 = 1
σ − 1 + 1
2 log ∆L + ζ ′
L
ζL (σ) + 1
σ + γ′
L
γL (σ) (8.5)

≤ 1
σ − 1 + 1
2 log ∆L

since ζ ′/ζ ≤ 0 and it is easily verified that

1
σ + γ′
L
γL (σ) = ( 1
σ − nL
2 log π) + a(L)
2 Γ
′

Γ
 ( σ
2
 ) + b(L)
2 Γ
′

Γ
 ( σ + 1
2
 ) < 0

for 1 < σ ≤ 1 + (log 3)
−1. If ρ = β + iγ is in the region described by (8.4) and

γ ̸= 0, then (8.5) gives

2 σ − β
(σ − β)2 + γ2 ≤ 1
σ − 1 + 1
2 log ∆L,

which is false at σ = 1 + (log ∆L)−1 ≤ 1 + (log 3)−1. We similarly obtain a

contradiction if there is more than one real zero in our region.

If the possible zero described by the above lemma exists, we denote it β0

and call it the exceptional (Siegel) zero. We also note that if nL = 1 (so that

L = Q, log ∆L = 0), then ζL has no nontrivial zeroes ρ with |γ| < 14. If β0

exists, then (8.1) shows that there exists a unique χ0 such that L(β0, χ0) = 0.

This χ0 must then be a real character, as L(β0, χ0) = L(β0, χ0) = 0.

9 Final estimates

We conclude this paper by applying the explicit formula of Theorem 7.1 to es-

timate ψC(x) and πC(x). We start with the GRH estimate for ψC(x), which is

35

Effective versions of Chebotarev Typeset by the TeXromancers

the easiest to obtain.

Theorem 9.1. If ζL(s) satisfies the GRH, then

ψC(x) − |C|
|G| x ≪ |C|
|G| x 1
2 log x log ∆LxnL + log x log ∆L (9.1)

for all x ≥ 2.

Proof. If ζL(s) satisfies the GRH, then so do all of the L(s, χ). Therefore, for

each χ there are no nontrivial zeros ρ with |ρ| < 1/2, and so by Lemma 5.4.

∣
∣
∣
∣
∣
 ∑

ρ
|γ|<T
 xρ

ρ + ∑

|ρ|< 1
2
 1
ρ
 ∣
∣
∣
∣
∣ ≤ x 1
2 ∑

ρ
|γ|<T
 1
|ρ|

≪ x 1
2
 ⌊T ⌋∑

j=1
 nX (j)
j

≪ x 1
2 (log A(χ) + nE log T ) log T,

which together with (7.5) implies

S(x, T ) ≪ |C|
|G| x 1
2 (log ∆L + nL log T ) log T (9.2)

for all T ≥ 2. We choose T = x 1
2 + 1, way, and then (9.2) and (7.4) imply (9.1)

for x ≥ 2.

Theorem 9.2. There is an effectively computable positive absolute constant c13

such that if
 x ≥ exp(4nL(log ∆L)2) (9.3)

then
 ψC(x) = |C|
|G| x − |C|
|G| χ0(g) xβ0

β0 + R(x), (9.4)

36

Lagarias and Odlyzko Section 9: Final estimates

where
 |R(x)| ≤ x exp(−c13n− 1
2
L (log x) 1
2 ),

and where the second term on the right side of (9.4) occurs only if ζL(s) has an

exceptional zero β0, and χ0 is the (real) character of H = Gal(L/E) = ⟨g⟩ for

which L(s, χ0, L/E) has β0 as a zero.

Proof. If ρ = β + iγ ̸= β0 is a nontrivial zero of one of the L(s, χ) with |γ| ≤ T ,

then the unconditional bound of Lemma 8.1 shows that

|xρ| = xβ ≤ x exp ( − c14 log x
log ∆LT nL
 )

for x ≥ 2, T ≥ 2. Further, Lemma 5.4 shows that

∑

χ
 ∑

ρ
|ρ|≥ 1
2
|γ|≤T
 ∣
∣
∣
∣ 1
ρ
 ∣
∣
∣
∣ ≪ log T log(∆LT nL).

Also,
 ∑

χ
 ∑

ρ̸=1−β0
|ρ|< 1
2
 (∣
∣
∣ xρ

ρ
 ∣
∣
∣ + ∣
∣
∣ 1
ρ
 ∣
∣
∣) ≪ x 1
2 ∑

χ
 ∑

ρ̸=1−β0
|ρ|< 1
2
 ∣
∣
∣ 1
ρ
 ∣
∣
∣ ≪ x 1
2 (log ∆L)
2,

by Lemma 5.4 and the fact that for ρ ̸= 1−β0, |ρ| ≥ (4 log ∆L)
−1. (If log ∆L = 0,

L = Q, and the estimate holds trivially). Finally,

x1−β0

1 − β0 − 1
1 − β0 = xσ log x ≤ x 1
2 log x

37

Effective versions of Chebotarev Typeset by the TeXromancers

for some σ, 0 ≤ σ ≤ 1 − β0. Collecting all these estimates gives us

S(x, T )− |C|
|G| χ0(g) xβ0

β0 ≪ |C|
|G| x log T log(∆LT nL) exp (− c14 log x
log ∆LT nL
 )+ |C|
|G| x 1
2 (log ∆L)
2.

(9.5)

We now choose
 T = exp(n− 1
2
L (log x) 1
2 − log ∆L). (9.6)

The estimate of the theorem then follows from (9.5) and (7.4).

The deduction of Theorem 1.1 and 1.3 from the preceding theorem is now

straightforward. We first define the function

θC(x) = ∑

NK/Q p≤x
p unramified[ L/K
p
 ]
=C
 log(NK/Q p).

Since there are at most nK ideals p
m (p prime) of a given norm in K,

∑

p,m
m≥2
NK/Q p
m≤x
 log(NK/Q p) ≪ nKx 1
2 (9.7)

by an elementary Chebyshev-type estimate. This shows that the estimates of

Theorems 9.1 and 9.2 hold when ψC(x) is replaced by θC(x). Theorems 1.1

and 1.3 now follow from these estimates for θC(x) by simple partial summation

arguments.

We conclude this paper by indicating one way in which the GRH estimate of

Corollary 1.2 can be slightly improved. Instead of integrating

1
2πi xs

s FC(x),

38

we can integrate 1
2πi
 ( ys−1 − xs−1

s − 1
 )2FC(x),

where y > x > 1, along the contour BT,U of Section 6. We then first let U → ∞,

and then T → ∞. The integral from σ0 − i∞ to σ0 + i∞ gives us the term we

are interested in, i.e., ∑

p[ L/K
p
 ]

=C
 log N p
N p r(N p; y, x), (9.8)

where
 r(m; y, x) =
 



log m
x2 x2 ≤ m ≤ xy,

log y2

m xy ≤ m ≤ y2,

0 otherwise,

together with the contribution of the ramified primes and prime powers. By

Cauchy’s theorem the value of the integral also equals the contribution of the

poles of the integrand, which is

|C|
|G|
 (log y
x
 )2 − |C|
|G|
 ∑

χ ¯χ(g) ∑

ρ
 ( yρ−1 − xρ−1

ρ − 1
 )2, (9.9)

where ρ now runs through both the trivia and the nontrivial zeros of L(s, χ). If

we now choose x = log ∆L, y = c14x, then for c14 sufficiently large (and on the

assumption of GRH) the main term in (9.9) will dominate both the sum over the

zeroes and of the ramified prime and prime power factors, so that (9.8) will have

to be nonzero. Hence there will be a prime p with [ L/K
p
 ] = C and

N p ≤ y2 ≤ c
2
14 log2 ∆L.

39

Bibliography

[Bom74] Enrico Bombieri. Le grand crible dans la th´eorie analytique des nombres. fr.
Ast´erisque 18. Soci´et´e math´ematique de France, 1974. url: http://www.n
umdam.org/item/AST_1987__18__1_0/.

[Deu35] Max Deuring. “ ¨Uber den Tschebotareffschen Dichtigkeitssatz”. In: Mathe-
matische Annalen 110 (1935), pp. 414–415. doi: 10.1007/BF01448036.
[DM13] H. Davenport and H.L. Montgomery. Multiplicative Number Theory. Grad-
uate Texts in Mathematics. Springer New York, 2013. isbn: 9781475759273.
url: https://books.google.com/books?id=SFztBwAAQBAJ.
[Fog61] E Fogels. “On The zeros of Hecke’s L-functions I”. eng. In: Acta Arithmetica
7.2 (1961), pp. 87–106. url: http://eudml.org/doc/207002.
[Gol70] Larry Joel Goldstein. “A Generalization of the Siegel-Walfisz Theorem”. In:
Transactions of the American Mathematical Society 149.2 (1970), pp. 417–
429. issn: 00029947. url: http://www.jstor.org/stable/1995404 (visited
on 10/17/2022).
[Hei67] H. Heilbronn. “Zeta-functions and L-functions”. In: Algebraic Number The-
ory. Ed. by J.W.S. Cassels, A. Fr¨ohlich, and London Mathematical Society.
Acad. Press, 1967, pp. 204–230. isbn: 9780122689505. url: https://www
.math.arizona.edu/~cais/scans/Cassels-Frohlich-Algebraic_Number
_Theory.pdf.
[Lan71] Serge Lang. “On the zeta function of number fields”. In: Inventiones Math-
ematicae 12.4 (1971), pp. 337–345. doi: 10.1007/bf01403312.
[LMO79] J. C. Lagarias, H. L. Montgomery, and A. M. Odlyzko. “A bound for the
least prime ideal in the Chebotarev density theorem”. In: Inventiones Math-
ematicae 54.3 (1979), pp. 271–296. doi: 10.1007/bf01390234.
[Mac68] Charles MacCluer. “A reduction of the Cebotarev density theorem to the
cyclic case”. In: Acta Arithmetica 15 (Jan. 1968), pp. 45–47. doi: 10.4064
/aa-15-1-45-47.
[Mor] C.J. Moreno. “An effective Chebotarev density theory”. In: (). (preprint,
University of Illinois 1975).
[Odl77] A.M. Odlyzko. “On Conductors and Discriminants”. In: Algebraic Number
Fields: (L-functions and Galois properties). Ed. by A. Fr¨olich. Academic
Press, 1977, pp. 377–407.
[Sok68] A.V. Sokolovskii. “Теорема о нулях дзета-функции Дедекинда и рассто-
яние между “соседними” простыми идеалами”. In: arta arith. 13 (1968),
pp. 321–334. doi: 10.4064/aa-13-3-321-334.
[Sta74] H.M. Stark. “Some Effective Cases of the Brauer-Siegel Theorem.” In: In-
ventiones mathematicae 23 (1974), pp. 135–152. url: http://eudml.org/d
oc/142257.
[Tsc26] N. Tschebotareff. “Die Bestimmung der Dichtigkeit einer Menge von Primzahlen,
welche zu einer gegebenen Substitutionsklasse geh¨oren”. In: Mathematische
Annalen 95 (1926), pp. 191–228. url: http://eudml.org/doc/159125.
[Wae70] B.L. van der Waerden. Modern Algebra. Springer New York, NY, 1970. isbn:
978-0-387-40624-4. url: http://www.ru.ac.bd/stat/wp-content/upload
s/sites/25/2019/03/104_09_01_van-der-Waerden-B.L.-Modern-Algebr
a-I-1949.pdf.
 40

[WW96] E.T. Whittaker and G.N. Watson. A Course of Modern Analysis. Cam-
bridge University Press, 1996. isbn: 9780521588072. url: http://theory
.fi.infn.it/colomo/metodi_old/Whittaker-Watson.pdf.

41
