<!-- source: https://arxiv.org/pdf/1204.0708 | converted from PDF -->

arXiv:1204.0708v3  [math.NT]  17 Jul 2012
THE VARIANCE OF THE NUMBER OF PRIME
POLYNOMIALS IN SHORT INTERVALS AND IN RESIDUE
CLASSES

J.P. KEATING AND Z. RUDNICK

Abstract. We resolve a function ﬁeld version of two conjectures con-
cerning the variance of the number of primes in short intervals (Goldston
and Montgomery) and in arithmetic progressions (Hooley). A crucial in-
gredient in our work are recent equidistribution results of N. Katz.

1. Introduction

In this note we study a function ﬁeld version of two outstanding problems
in classical Prime Number Theory, concerning the variance of the number
of primes in short intervals and in arithmetic progressions.

1.1. Problem 1: Primes in short intervals. The Prime Number The-
orem (PNT) asserts that the number π(x) of primes up to x is asymptoti-
cally Li(x) = ∫ x
2 dt
log t . Equivalently, deﬁning the von Mangoldt function as
Λ(n) = log p if n = pk is a prime power, and 0 otherwise, then PNT is
equivalent to the assertion that

(1.1) ψ(x) := ∑

n≤x Λ(n) ∼ x as x → ∞ .

To study the distribution of primes in short intervals, we deﬁne for 1 ≤
H ≤ x,

(1.2) ψ(x; H) := ∑

n∈[x− H
2 ,x+ H
2 ] Λ(n) .

The Riemann Hypothesis guarantees an asymptotic formula ψ(X; H) ∼ H
as long as H > X 1
2 +o(1). To understand the behavior in shorter intervals,
Goldston and Montgomery [6] studied the variance of ψ(x; H) and showed

Date: March 31, 2022.
JPK was supported by a grant from the Leverhulme Trust and by the Air Force Oﬃce
of Scientiﬁc Research, Air Force Material Command, USAF, under grant number FA8655-
10-1-3088. The U.S. Government is authorized to reproduce and distribute reprints for
Governmental purpose notwithstanding any copyright notation thereon. ZR was sup-
ported by the Israel Science Foundation (grant No. 1083/10).
1

2 J.P. KEATING AND Z. RUDNICK

conditionally that for X δ < H < X 1−δ,

(1.3) 1
X
 ∫ X

2 |ψ(x; H) − H|2 dx ∼ H(log X − log H) ,

assuming the Riemann Hypothesis and the (”strong”) pair correlation con-
jecture. Furthermore, they showed that under RH (1.3) and the strong pair
correlation conjecture are in fact equivalent. At this time (1.3) is still open.

1.2. Problem 2: Primes in arithmetic progressions. The Prime Num-
ber Theorem for arithmetic progression states that for a modulus Q and A
coprime to Q, the number of primes p ≤ X with p = A mod Q is asymptot-
ically π(x)/φ(Q), where π(X) is the number of primes up to X and φ(Q)
is the Euler totient function, giving the number of reduced residues modulo
Q. Equivalently, if

(1.4) ψ(X; Q, A) := ∑

n≤X
n=A mod Q
 Λ(n)

then PNT for arithmetic progressions states that for a ﬁxed modulus Q,

(1.5) ψ(X; Q, A) ∼ X
φ(Q) , as X → ∞ .

In most arithmetic applications it is crucial to allow the modulus to grow
with X. Thus the remainder term in (1.5) is of the essence. For very large
moduli Q > X, there can be at most one prime in the arithmetic progression
P = A mod Q so that the interesting range is Q < X. Assuming the
Generalized Riemann Hypothesis (GRH) gives (1.5) for Q < X 1/2−o(1).
The ﬂuctuations of ψ(X; Q, A) have been studied over several decades,
notably allowing also averaging over the modulus Q. Thus deﬁne

(1.6) G(X, Q) = ∑

A mod Q
gcd(A,Q)=1
 ∣
∣
∣
∣ψ(X; Q, A) − X
φ(Q)
 ∣
∣
∣
∣

2

and

(1.7) H(X, Q) = ∑

Q′≤Q G(X, Q ′) .

The study of the sum H(X, Q) has a long history, going under the name of
theorems of Barban-Davenport-Halberstam type. Among other results is the
one due to Montgomery [15] and Hooley [8] asserting that for X/(log X)A <
Q < X one has

(1.8) H(X, Q) = QX log Q − cQX + O(Q5/4X 3/4 + X 2

(log X)A ) ,

for all A > 0, where

(1.9) c = γ + log(2π) + 1 + ∑

p
 log p
p(p − 1) .

VARIANCE OF THE NUMBER OF PRIME POLYNOMIALS 3

Hooley [9] showed that assuming GRH, (1.8) holds for X 1/2+ǫ < Q < X
with remainder O(X 2/(log X)A).
The individual variance G(X, Q) is much less understood. Hooley [10]
conjectured that under some (unspeciﬁed) conditions,

(1.10) G(X, Q) ∼ X log Q .

Friedlander and Goldston [4] show that in the range Q > X,

(1.11) G(X, Q) = X log X − X − X 2

φ(Q) + O( X
(log X)A ) + O((log Q)
3) .

Note that in this range, there is at most one integer n = A mod Q with
n < X. They conjecture that (1.10) holds if

(1.12) X 1/2+ǫ < Q < X

and further conjecture that if X 1/2+ǫ < Q < X 1−ǫ then

(1.13) G(X, Q) = X log Q − X(γ + log 2π + ∑

p|Q
 log p
p − 1 ) + o(X) .

They show that both (1.10) (in the range X 1/2+ǫ < Q < X) and (1.13)
(in the range X 1/2+ǫ < Q < X 1−ǫ) hold assuming a Hardy-Littlewood
conjecture with small remainders.
For Q < X 1/2 very little seems to be known. Hooley addresses this in
paper V of his series of papers on the subject [11], which he opens by stating
An interesting anomaly in the theory of primes is presented
by the situation in which known forms of the prime number
theorem for arithmetic progressions are only valid for (rela-
tively) small values of the common diﬀerence
1 k, whereas the
theorems of Barban-Davenport-Halberstam type discussed 2

in I, II, IV are only fully signiﬁcant for the (relatively) larger
values of k. The most striking illustration of this contrast
is perhaps provided by the conditional theorems at present
available on the extended Riemann hypothesis, the ranges of
signiﬁcance of the prime number theorem and of the Barban-
Montgomery theorem given in II being then, respectively,
k < x1/2−ǫ and k > x1/2+ǫ.
. . . it is therefore certainly desirable to elicit further forms
of the Barban-Davenport-Halberstam theorem that should
be valid for the smaller values of k.
Concerning Conjectures (1.10) and (1.13) for G(X, Q), Friedlander and
Goldston say [4, page 315]
It may well be that these also hold for smaller Q, but below
X = Q1/2 we are somewhat skeptical.

1Hooley’s k corresponds to Q and x to X
2Here he is referring to the earlier papers in the series

4 J.P. KEATING AND Z. RUDNICK

In this paper we resolve the function-ﬁeld versions of Conjectures (1.3)
and (1.10), indicating that (1.10) should hold all the way down to Q > X ǫ.
A crucial ingredient in our work are recent equidistribution results of Katz
[13, 14] described in § 4, § 5.

2. Results for function fields

Let Fq be a ﬁnite ﬁeld of q elements and Fq[T ] the ring of polynomials
with coeﬃcients in Fq. Let Pn = {f ∈ Fq[T ] : deg f = n} be the set of
polynomials of degree n and Mn ⊂ Pn the subset of monic polynomials.
The von Mangoldt function in this case is deﬁned as Λ(N ) = deg P ,
if N = cP k with P an irreducible monic polynomial, and c ∈ F×
q , and
Λ(N ) = 0 otherwise. The Prime Polynomial Theorem in this context is the
identity

(2.1) ∑

f ∈Mn Λ(f ) = qn .

2.1. Short intervals. For A ∈ Pn of degree n, and h < n, we deﬁne “short
intervals”

(2.2) I(A; h) := {f : ||f − A|| ≤ qh} = A + P≤h ,

where the norm of a polynomial 0 ̸= f ∈ Fq[T ] is

(2.3) ||f || := qdeg f

and

(2.4) P≤h = {0} ∪ ⋃

0≤m≤h Pm

is the space of polynomials of degree at most h (including 0). We have

(2.5) #I(A; h) = qh+1 .

Note: For h < n, if ||f − A|| ≤ qh then A monic if and only if f is monic.
Hence for A monic, I(A; h) consists of only monic polynomials and all monic
f ’s of degree n are contained in one of the intervals I(A; h) with A monic.
We deﬁne for 1 ≤ h < n and A ∈ Pn,

(2.6) ν(A; h) = ∑

f ∈I(A;h)
f (0)̸=0
 Λ(f )

to be the number of prime powers co-prime to T in the interval I(A; h),
weighted by the degree of the corresponding prime.
We will show in Lemma 4.3 that the mean value of ν(A; h) when we
average over monic A ∈ Mn is

(2.7) ⟨ν(•; h)⟩ := 1
qn ∑

A∈Mn ν(A; h) = qh+1(1 − 1
qn ) .

VARIANCE OF THE NUMBER OF PRIME POLYNOMIALS 5

Our goal is to compute the variance

Var ν(•; h) = 1
qn ∑

A∈Mn |ν(A; h) − ⟨ν(•; h)⟩ |
2

in the limit q → ∞.

Theorem 2.1. Let h < n − 3. Then

(2.8) lim
q→∞ 1
qh+1 Var(ν(•; h)) = n − h − 2 .

We may compare (2.8) with (1.3) if we make the dictionary

(2.9) X ↔ qn, H ↔ qh+1, log X ↔ n, log H ↔ h + 1 ,

the conclusion being that Theorem 2.1 is precisely the analogue of the con-
ditional result (1.3) of Goldston and Montgomery.

2.2. Arithmetic progressions. Our second result concerns the analogue
of the conjectures of Hooley (1.10) and Friedlander-Goldston (1.13) and
allows us to make a deﬁnite conjecture in that case.
For a polynomial Q ∈ Fq[T ] of positive degree, and A ∈ Fq[T ] coprime to
Q and any n > 0, set

(2.10) Ψ(n; Q, A) = ∑

N ∈Mn
N =A mod Q
 Λ(N )

(the sum over monic polynomials). The Prime Polynomial Theorem in arith-
metic progressions states that as n → ∞,

(2.11) Ψ(n; Q, A) ∼ qn

Φ(Q)

where Φ(Q) is the Euler totient function for this context, namely the number
of reduced residue classes modulo Q. Now set

(2.12) G(n; Q) = ∑

A mod Q
gcd(A,Q)=1
 ∣
∣
∣
∣Ψ(n; Q, A) − qn

Φ(Q)
 ∣
∣
∣
∣

2 .

We wish to show an analogue of Conjecture (1.10) in the limit of large
ﬁnite ﬁeld size, that is q → ∞.

Theorem 2.2. i) Given a ﬁnite ﬁeld Fq, let Q ∈ Fq[T ] be a polynomial of
positive degree, and 1 ≤ n < deg Q. Then

(2.13) G(n; Q) = nqn − q2n

Φ(Q) + O(n2qn/2) + O((deg Q)
2) ,

the implied constant absolute.
ii) Fix n ≥ 2. Given a sequence of ﬁnite ﬁelds Fq and square-free polyno-
mials Q(T ) ∈ Fq[T ] of positive degree with n ≥ deg Q − 1, then as q → ∞,

(2.14) G(n; Q) ∼ qn(deg Q − 1) .

6 J.P. KEATING AND Z. RUDNICK

We can compare (2.14) to (1.10) in the range (1.12), if we make the
dictionary

(2.15) Q ↔ ||Q|| = qdeg Q, log Q ↔ deg Q, X ↔ qn, log X ↔ n .

The result (1.11) in the range Q > X corresponds to n < deg Q, and the
range X 1/2 < Q < X of (1.12) corresponds to deg Q < n < 2 deg Q, so that
we recover the function ﬁeld version of conjecture (1.10). Note that (2.14)
holds for all n, not just that range. Thus Conjecture (1.10) may well be
valid for all Q > X ǫ.

3. Background on characters and L-functions

We review some standard background concerning Dirichlet L-functions
for the rational function ﬁeld, see e.g. [17, 18].

3.1. The Prime Polynomial Theorem. Let Fq be a ﬁnite ﬁeld of q ele-
ments and Fq[T ] the polynomials over F. The zeta function Z(u) of Fq[T ]
is

(3.1) Z(u) := ∏

P (1 − udeg P )
−1

where the product is over all monic irreducible polynomials in Fq[T ]. The
product is absolutely convergent for |u| < 1/q.
By unique factorization into irreducibles in Fq[T ], we have for |u| < 1/q,

(3.2) Z(u) = 1
1 − qu .

Taking the logarithmic derivative of (3.1) and (3.2) leads to the “Explicit
formula”

(3.3) Ψ(n) := ∑

N ∈Mn Λ(N ) = qn

from which we immediately deduce the Prime Polynomial Theorem, for the
number π(n) of monic irreducible polynomials of degree n:

(3.4) π(n) = qn

n + O(qn/2) .

Lemma 3.1.

(3.5) ∑

N ∈Mn Λ(N )
2 = nqn + O(n2qn/2)

where the implied constant is absolute (independent of q and n).

Proof. We start with the Explicit Formula (3.3)

(3.6) ∑

d|m dπ(d) = qm

and hence

(3.7) mπ(m) ≤ qm .

VARIANCE OF THE NUMBER OF PRIME POLYNOMIALS 7

Now

(3.8) qn = ∑

d|n dπ(d) = nqn + ∑

d|n
d<n
 dπ(d)

and hence

(3.9) π(n) = qn

n + O(qn/2) .

Likewise

(3.10) ∑

N ∈Mn Λ(N )
2 = ∑

d|n d
2π(d) = n2π(n) + ∑

d|n
d<n
 d
2π(d)

with remainder term bounded by

(3.11) ∑

d|n
d<n
 d
2π(d) ≤ ∑

d≤n/2 d
2π(d) ≤ ∑

1≤d≤n/2 nqd/2 ≤ nq qn/2 − 1
q − 1 < 2nqn/2 .

Inserting (3.9) into (3.10) gives the claim. □

3.2. Dirichlet characters. For a polynomial Q(x) ∈ Fq[T ] of positive de-
gree, we denote by Φ(Q) the order of the group (Fq[T ]/(Q))× of invertible
residues modulo Q. A Dirichlet character modulo Q is a homomorphism

χ : (Fq[T ]/(Q))× → C×

that is, after extending χ to vanish on polynomials which are not coprime
to Q, we require χ(f g) = χ(f )χ(g) for all f, g ∈ Fq[T ], χ(1) = 1 and
χ(f + hQ) = χ(f ) for all f, h ∈ Fq[T ]. The number of Dirichlet characters
modulo Q is Φ(Q).
The orthogonality relations for Dirichlet characters are

(3.12) 1
Φ(Q)
 ∑

χ mod Q ¯χ(A)χ(N ) =
 {
1, N = A mod Q
0, otherwise

where the sum is over all Dirichlet characters mod Q and A is coprime to
Q, and

(3.13) 1
Φ(Q)
 ∑

A mod Q χ1(A) ¯χ2(A) =
 {
1, χ1 = χ2
0, otherwise.

A Dirichlet character χ is “even” if χ(cF ) = χ(F ) for 0 ̸= c ∈ Fq. This
is in analogy to the number ﬁeld case, where a Dirichlet character is called
”even” if χ(−1) = +1, and ”odd” if χ(−1) = −1. The number Φev(Q) of
even characters modulo Q is

(3.14) Φev(Q) = 1
q − 1 Φ(Q) .

We require the following orthogonality relations for even Dirichlet char-
acters

8 J.P. KEATING AND Z. RUDNICK

Lemma 3.2. Let χ1, χ2 be Dirichlet characters modulo T m, m > 1. Suppose
χ1χ2 is even. Then

(3.15) 1
qm−1 ∑

B mod T m
B(0)=1
 χ1(B)χ2(B) = δχ1,χ2 .

Proof. We start with the standard orthogonality relation

(3.16) 1
Φ(T m)
 ∑

B mod T m χ1(B)χ2(B) = δχ1,χ2 .

The only nonzero contributions in the sum are those B with B(0) ̸= 0
(equivalently coprime to T m). We can write each such B uniquely as B =
cB1, with B1(0) = 1. Since χ1χ2 is even, we have

(3.17) χ1χ2(cB1) = χ1χ2(B1)

and hence

(3.18) ∑

B mod T m χ1(B)χ2(B) = (q − 1) ∑

B mod T m
B(0)=1
 χ1(B)χ2(B) .

Comparing with (3.16) and using Φ(T m) = (q − 1)qm−1 gives the required
result. □

3.3. Primitive characters. A character is primitive if there is no proper
divisor Q′ | Q so that χ(F ) = 1 whenever F is coprime to Q and F =
1 mod Q′. Denoting by Φprim(Q) the number of primitive characters modulo
Q, we clearly have Φ(Q) = ∑D|Q Φprim(D) and hence by M¨obius inversion,

(3.19) Φprim(Q) = ∑

D|Q µ(D)Φ( Q
D )

the sum over all monic polynomials dividing Q. Therefore

(3.20) ∣
∣
∣
∣ Φprim(Q)
Φ(Q) − 1
∣
∣
∣
∣ ≤ 2deg Q

q .

Hence as q → ∞, almost all characters are primitive in the sense that

(3.21) Φprim(Q)
Φ(Q) = 1 + O( 1
q ) ,

the implied constant depending only on deg Q.
Likewise, the number Φev
prim(Q) of primitive even characters is given by

(3.22) Φev
prim(Q) = ∑

D|Q µ(D)Φev( Q
D ) = 1
q − 1
 ∑

D|Q µ(D)Φ( Q
D ) .

For instance, for Q(T ) = T m, m ≥ 2, we ﬁnd

(3.23) Φev
prim(T m) = qm−2(q − 1) .

VARIANCE OF THE NUMBER OF PRIME POLYNOMIALS 9

The number Φprim
odd (Q) of odd primitive characters is then

(3.24) Φodd
prim(Q) = Φprim(Q) − Φev
prim(Q) = (1 − 1
q − 1 )Φprim(Q)

and hence we ﬁnd that as q → ∞ with deg Q ﬁxed, almost all characters are
primitive and odd:

(3.25) Φodd
prim(Q)

Φ(Q) = 1 + O( 1
q ) ,

the implied constant depending only on deg Q.

3.4. L-functions. The L-function L(u, χ) attached to χ is deﬁned as

(3.26) L(u, χ) = ∏

P ∤Q
(1 − χ(P )udeg P )
−1

where the product is over all monic irreducible polynomials in Fq[T ]. The
product is absolutely convergent for |u| < 1/q. If χ = χ0 is the trivial
character modulo q, then

(3.27) L(u, χ0) = Z(u) ∏

P |Q
(1 − udeg P ) .

The basic fact about L(u, χ) is that if Q ∈ Fq[T ] is a polynomial of degree
deg Q ≥ 2, and χ ̸= χ0 a nontrivial character mod Q, then the L-function
L(u, χ) is a polynomial in u of degree deg Q − 1.
Moreover, if χ is an “even” character , that is χ(cF ) = χ(F ) for 0 ̸= c ∈
Fq, then there is a ”trivial” zero at u = 1: L(1, χ) = 0 and hence

(3.28) L(u, χ) = (1 − u)P (u, χ)

where P (u, χ) is a polynomial of degree deg Q − 2.
We may factor L(u, χ) in terms of the inverse roots

(3.29) L(u, χ) =
 deg Q−1∏

j=1 (1 − αj(χ)u) .

The Riemann Hypothesis, proved by Andre Weil (1948) in general, is that
for each (nonzero) inverse root, either αj(χ) = 1 or

(3.30) |αj(χ)| = q1/2 .

We deﬁne

(3.31) Ψ(n, χ) := ∑

deg f =n Λ(f )χ(f )

the sum over monic polynomials of degree n. Taking logarithmic derivative
of the L-function gives a formula for Ψ(n, χ) in terms of the inverse roots

10 J.P. KEATING AND Z. RUDNICK

αj(χ): If χ ̸= χ0 is nontrivial then

(3.32) Ψ(n, χ) = −
 deg Q−1∑

j=1 αj(χ)
n .

The Riemann Hypothesis (3.30) gives for n > 0

(3.33) |Ψ(n, χ)| ≤ (deg Q − 1)qn/2, χ ̸= χ0 .

3.5. The unitarized Frobenius matrix. We may state the results in
cleaner form if we assume that χ is a primitive character modulo Q.
We also deﬁne

(3.34) λχ :=
 {1, χ “even”
0, otherwise.

Then for Q ∈ Fq[T ] a polynomial of degree ≥ 2, and χ a primitive Dirichlet
character modulo Q,
 L∗(u, χ) := (1 − λχu)
−1L(u, χ)

is a polynomial of degree

(3.35) N = deg Q − 1 − λχ

so that L∗(u, χ) = ∏N
j=1(1 − αj(χ)u) and

(3.36) |αj| = √
q, ∀j = 1, . . . , N .

For a primitive character modulo Q, we write the inverse roots as αj =
q1/2eiθj and the completed L-function L∗(u, χ) as

(3.37) L∗(u, χ) = det(I − uq1/2Θχ), Θχ = diag(e
iθ1, . . . , e
iθN ) .

The unitary matrix Θχ (or rather, the conjugacy class of unitary matrices)
is called the unitarized Frobenius matrix of χ.
Taking the logarithmic derivative of (3.37) we get an Explicit Formula
for primitive characters:

(3.38) Ψ(n, χ) = −qn/2 tr Θn
χ − λχ .

4. Prime polynomials in short intervals

In this section we prove Theorem 2.1, the analogue of the Goldston-
Montgomery result (1.3).

VARIANCE OF THE NUMBER OF PRIME POLYNOMIALS 11

4.1. An involution. For 0 ̸= f ∈ Fq[T ] we deﬁne

(4.1) f ∗(T ) := T deg f f ( 1
T )

or if f (T ) = f0 + f1T + · · · + fnT n, n = deg f (so that fn ̸= 0), then f ∗ is
the “reversed” polynomial

(4.2) f ∗(T ) = f0T n + f1T n−1 + · · · + fn .

We also set 0∗ = 0.
Note that f ∗(0) ̸= 0 and f (0) ̸= 0 if and only if deg f ∗ = deg f . Moreover
restricted to polynomials which do not vanish at 0, equivalently are co-prime
to T , then ∗ is an involution:

(4.3) f ∗∗ = f, f (0) ̸= 0 .

We also have multiplicativity:

(4.4) (f g)
∗ = f ∗g∗ .

Lemma 4.1. For f ∈ Pn with f (0) ̸= 0, we have Λ(f ∗) = Λ(f ).

Proof. For polynomials which do not vanish at 0, i.e. are co-prime to T , P
is irreducible if and only if P ∗ is irreducible. This is because if P = AB
with A, B of positive degree then P ∗ = (AB)∗ = A∗B∗ and if P (0) ̸= 0 then
the same holds for A, B and then deg A∗ = deg A > 0, deg B∗ = deg B > 0
so P is reducible; applying ∗ again and using that it is an involution (since
P (0) ̸= 0) gives the reverse implication. □

4.2. A fundamental relation. We can now express the number of primes
in our short intervals in terms of the number of primes in a suitable arith-
metic progression. Deﬁne

(4.5) ˜Ψ(n; Q, A) = ∑

f ∈Pn
f =A mod Q
 Λ(f ) .

the sum over all polynomials of degree n, not necessarily monic.

Lemma 4.2. For B ∈ Pn−h−1,

(4.6) ν(T h+1B; h) = ˜Ψ(n; T n−h, B∗) .

Proof. Let B ∈ Pn−h−1. We have f = T h+1B + g ∈ I(T h+1B; h), g ∈ P≤h
if and only if f ∗ = B∗ + T n−hg∗, and thus we ﬁnd

(4.7) f ∈ I(T h+1B; h) ⇔ f ∗ ≡ B∗ mod T n−h .

As f runs over I(T h+1B; h) with the proviso that f (0) ̸= 0, f ∗ runs over
all polynomials of degree exactly n satisfying f ∗ ≡ B∗ mod T n−h, and for
these Λ(f ) = Λ(f ∗). □

12 J.P. KEATING AND Z. RUDNICK

4.3. Averaging. We want to compute the mean value and variance of
ν(A, h). To perform the average over A, note that every monic polynomial
f ∈ Mn can be written uniquely as

(4.8) f = T h+1B + g, B ∈ Mn−(h+1), g ∈ P≤h .

We therefore can decompose Mn as the disjoint union of “intervals” I(T h+1B; h)
parameterized by B ∈ Mn−(h+1):

(4.9) Mn = ∐

B∈Mn−(h+1) I(T h+1B; h) .

To compute averages ν on short intervals, it suﬃces, by the foregoing, to
take A = T h+1B and to average over all B ∈ Mn−(h+1).
The map ∗ gives a bijection

∗ : Mn−(h+1) → {B∗ ∈ P≤(n−h−1) : B∗(0) = 1}

B ↦→ B∗(4.10)

with polynomials of degree ≤ n − (h + 1) with constant term 1. Thus as
B ranges over Mn−(h+1), B∗ ranges over (Fq[T ]/(T n−h))×, all invertible
residue class mod T n−h so that B∗(0) = 1.
Thus the mean value is

⟨ν(•; h)⟩ = 1
#Mn−h−1
 ∑

B∈Mn−h−1 ν(T h+1B; , h)

= 1
qn−h−1 ∑

B∗ mod T n−h
B∗(0)=1
 ˜Ψ(n; T n−h, B∗)
(4.11)

and the variance is

Var(ν(•; h)) = 1
#Mn−h−1
 ∑

B∈Mn−h−1
 ∣
∣
∣ν(T h+1B; , h) − ⟨ν⟩
∣
∣
∣
2

= 1
qn−h−1 ∑

B∗ mod T n−h
B∗(0)=1
 ∣
∣
∣ ˜Ψ(n; T n−h, B∗) − ⟨ν⟩
∣
∣
∣
2 .
(4.12)

4.4. The mean value. The computation of the mean value ⟨ν(•; h)⟩ =
1
qn ∑A∈Mn ν(A; h) is a simple consequence of the Prime Polynomial Theo-
rem. The result is

Lemma 4.3. Let 0 < h < n. The mean value of ν(A, ; h) is

(4.13) ⟨ν(•; h)⟩ = qh+1(1 − 1
qn ) .

VARIANCE OF THE NUMBER OF PRIME POLYNOMIALS 13

Proof. We do the computation in two diﬀerent ways as a check of the all-
important relation (4.6). By using the deﬁnition of ν, we get

⟨ν(•; h)⟩ = 1
#Mn−h−1
 ∑

B∈Mn−h−1
 ∑

f ∈I(T h+1B;h)
f (0)̸=0
 Λ(f )

= 1
#Mn−h−1
 

 ∑

f ∈Mn Λ(f ) − Λ(T n)



 .

(4.14)

Note that

(4.15) #Mn−h−1 = qn−h−1 = Φ(T n−h)
q − 1 .

Using (4.6), the mean value of ν(•; h) is

⟨ν(•; h)⟩ = 1
Φ(T n−h)
 ∑

B∗ mod T n−h
B∗(0)=1
 ˜Ψ(n; T n−h, B∗)

= 1
Φ(T n−h)
 ∑

deg f ∗=n
f ∗(0)=1
 Λ(f ∗)

= 1
Φ(T n−h)
 

 ∑

deg f ∗=n Λ(f ∗) − ∑

c∈F∗
q Λ(cT n)





= 1
qn−h−1
 

 ∑

f ∗∈Mn Λ(f ∗) − Λ(T n)



 .

(4.16)

Hence

(4.17) ⟨ν(•; h)⟩ = 1
qn−h−1 (qn − 1) = qh+1(1 − 1
qn )

on using the Prime Polynomial Theorem in the form (3.3). □

4.5. An alternate expression for ν(A; h). Using the standard orthogo-
nality relation (3.16) for Dirichlet characters modulo T n−h gives an alternate
expression for ˜Ψ(n; T n−h, B∗) and hence for ν(T h+1B; h):

(4.18) ˜Ψ(n; T n−h, B∗) = 1
Φ(T n−h)
 ∑

χ mod T n−h χ(B∗) ∑

deg f ∗=n Λ(f ∗)χ(f ∗) .

Only even characters give a non-zero term, because Λ(cf ) = Λ(f ) for
c ∈ F×
q , and each even character contributes a term

(4.19) χ(B∗) q − 1
Φ(T n−h)
 ∑

deg f =n
monic
 Λ(f )χ(f ) = χ(B∗) 1
qn−h−1 Ψ(n, χ)

14 J.P. KEATING AND Z. RUDNICK

where

(4.20) Ψ(n, χ) = ∑

deg f =n
monic
 Λ(f )χ(f ) .

Note that the number of even characters mod T n−h is exactly 1
q−1 Φ(T n−h) =
qn−h−1.
The trivial character χ0 contributes the term

(4.21) (q − 1)(qn − 1)
Φ(T n−h) = qh+1(1 − 1
qn ) = ⟨ν⟩ .

Thus we ﬁnd that the diﬀerence between ν(T h+1B; h) and its mean ⟨ν⟩ is

(4.22) ν(T h+1B; h) − ⟨ν⟩ = 1
qn−h−1 ∑

χ̸=χ0 mod T n−h
even
 χ(B∗)Ψ(n, χ) .

4.6. The variance. Our result here is that

Theorem 4.1. Fix n > 0 and let 0 < h < n. As q → ∞, the variance of ν
is given by

(4.23) Var(ν) = qh+1 ·
 ( 1
qn−h−1
 ∗∑

χ | tr Θn
χ|
2 + O( n − h
qn/2 + n2

q )

)

where the sum is over primitive even characters modulo T n−h, the implied
constant depending only on n.

Proof. By (4.22) we have

(4.24) Var(ν) = 1
qn−h−1 ∑

B∗ mod T n−h
B∗(0)=1
 1
q2(n−h−1)
 ∣
∣
∣
∣
∣
∣
∣
 ∑

χ̸=χ0
even
 χ(B∗)Ψ(n, χ)

∣
∣
∣
∣
∣
∣
∣
2
 .

Expanding the sum over characters, and interchanging the order of summa-
tion to use the orthogonality relation of Lemma 3.2 gives

(4.25) Var(ν) = 1
q2(n−h−1) ∑

χ̸=χ0
even
 |Ψ(n, χ)|
2 .

There are altogether ϕ(T n−h)/(q − 1) = qn−h−1 even characters modulo
T n−h, of which O(qn−h−2) are non-primitive. We bound the contribution
of the nontrivial non-primitive characters by Ψ(n, χ) = O(nqn/2) via the
Riemann Hypothesis. Thus the non-primitive characters contribute a total
of O(n2qh) to Var(ν).
Using the Explicit Formula (3.38) for primitive even characters and the
Riemann Hypothesis gives

(4.26) |Ψ(n, χ)|
2 = qn| tr Θn
χ|
2 + O((n − h)qn/2) .

VARIANCE OF THE NUMBER OF PRIME POLYNOMIALS 15

Therefore

(4.27) Var(ν) = qh+1 ·
 ( 1
qn−h−1
 ∗∑

χ | tr Θn
χ|
2 + O( n − h
qn/2 + n2

q )

)

where the sum is over primitive even characters modulo T n−h, whose number
is qn−h−1(1 − 1
q ). □

4.7. Proof of Theorem 2.1. Thus we found that for h < n−3, the variance
of ν is given by

(4.28) 1
qh+1 Var(ν) = (1 − 1
q ) 〈| tr Θn
χ|
2〉 + O( n − h
qn/2 + n2

q )

with 〈| tr Θn
χ|2〉 being the mean value of | tr Θn
χ|2 over the set of all primitive
even Dirichlet characters modulo T n−h. Thus as q → ∞, Var(ν)/qh+1 is
asymptotically equal to the ”form factor” 〈| tr Θn
χ|2〉.
To proceed further, we need to invoke a recent result of N. Katz [14]:

Theorem 4.2. [14, Theorem 1.2] Fix
3 m ≥ 3. The unitarized Frobenii Θχ
for the family of even primitive characters mod T m+1 become equidistributed
in the projective unitary group P U (m − 1) of size m − 1, as q → ∞.

Applying Theorem 4.2 gives

(4.29) lim
q→∞ 1
qn−h−1(1 − 1
q )
 ∗∑

χ | tr Θn
χ|
2 = ∫
P U (n−h−2) | tr U n|
2dU .

We may pass from the projective unitary group P U (n−h−2) to the unitary
group because the function | tr U n|2 being averaged is invariant under scalar
multiplication. As is well known (see e.g. [3]), for n > 0

(4.30) ∫

U (N ) | tr U n|
2dU = min(n, N ) .

Therefore we ﬁnd

(4.31) Var(ν) ∼ qh+1(n − h − 2), q → ∞ .

This concludes the proof of Theorem 2.1.

5. Prime polynomials in arithmetic progressions

In this section we prove Theorem 2.2, giving the function ﬁeld analogue
of the conjectures of Hooley (1.10) and Friedlander-Goldston (1.13).

3If the characteristic of Fq is diﬀerent than 2 or 5 then the result also holds for m = 2.

16 J.P. KEATING AND Z. RUDNICK

5.1. The range n < deg Q. We prove the result in the range n < deg Q by
elementary arguments:

Proposition 5.1. For 0 < n < deg Q, we have

(5.1) G(n; Q) = nqn − q2n

Φ(Q) + O(n2qn/2) + O((deg Q)
2)

where the implied constant is independent of q, n and Q.

Proof. Assume as we may that deg A < deg Q. If n < deg Q then the only
solution to the congruence N = A mod Q, with deg N = n < deg Q is A (if
deg A = n) or else there is no solution. Therefore if n < deg Q then

(5.2) Ψ(n; Q, A) =
 {
Λ(A), A is monic and deg A = n
0, otherwise.

Thus

G(n; Q) = ∑

gcd(A,Q)=1
 ∣
∣
∣
∣
∣ qn

Φ(Q) −
 {Λ(A), A is monic and deg A = n
0, otherwise
 ∣
∣
∣
∣
∣

2

= ∑

deg A=n
A monic
gcd(A,Q)=1
 Λ(A)
2 − 2 qn

Φ(Q)
 ∑

deg A=n
A monic
gcd(A,Q)=1
 Λ(A) + q2n

Φ(Q) .

By the Prime Polynomial Theorem (3.3),

(5.3) ∑

deg A=n
A monic
gcd(A,Q)=1
 Λ(A) = qn − ∑

P |Q prime
deg P |n
 deg P = qn + O(deg Q) .

According to Lemma 3.1,
∑

deg A=n
A monic
gcd(A,Q)=1
 Λ(A)
2 = ∑

deg A=n Λ(A)
2 − ∑

P |Q
deg P |n

(deg P )
2

= nqn + O(n2qn/2) + O((deg Q)
2)

(5.4)

and so we ﬁnd

(5.5) G(n; Q) = nqn − q2n

Φ(Q) + O(n2qn/2) + O((deg Q)
2) + O( qn

Φ(Q) deg Q) .

Since for n < deg Q,

(5.6) qn

Φ(Q) ≤ 1
q
 ∏

P |Q
prime

(1 − 1
|P | )
−1 ≤ 1
q
 ∏

deg P ≤deg Q
prime
 (1 − 1
|P | )
−1 ≪ deg Q
q

VARIANCE OF THE NUMBER OF PRIME POLYNOMIALS 17

we ﬁnd

(5.7) G(n; Q) = nqn − q2n

Φ(Q) + O(n2qn/2) + O((deg Q)
2)

as claimed. □

5.2. The range n ≥ deg Q. To deal with the range n ≥ deg Q we relate
the problem to an equidistribution statement for the unitarized Frobenii
of primitive odd characters. It transpires that G(n; Q) is related to the
mean value of the modulus squared of the trace of the Frobenius matrices
associated to the family of Dirichlet L-functions for characters modulo Q:

Theorem 5.1. Fix n and let Q ∈ Fq[T ] have degree deg Q ≥ 2. Then

(5.8) G(n; Q)
qn = 〈| tr Θn
χ|
2〉 (1 + 1
q ) + O( (deg Q)2

q )

where ⟨⟩ denotes the average over all odd primitive characters modulo Q.

Proof. The orthogonality relation (3.12) gives

Ψ(n; Q, A) = 1
Φ(Q)
 ∑

χ mod Q ¯χ(A) ∑

deg N =n χ(N )Λ(N )

= 1
Φ(Q)
 ∑

χ mod Q ¯χ(A)Ψ(n, χ) .
(5.9)

The trivial character χ0 gives a contribution of

(5.10) 1
Φ(Q)
 ∑

deg N =n
gcd(N,Q)=1
 Λ(N ) = qn

Φ(Q) − 1
Φ(Q)
 ∑

P |Q
deg P |n
 deg P .

Hence
(5.11)

Ψ(n; Q, A) − qn

Φ(Q) = − 1
Φ(Q)
 ∑

P |Q
deg P |n
 deg P + 1
Φ(Q)
 ∑

χ̸=χ0 χ(A)Ψ(n, χ) .

We square out and average over all A mod Q coprime with Q. Using the
orthogonality relation (3.13) gives

(5.12) G(n; Q) = 1
Φ(Q)
 ∑

χ̸=χ0 |Ψ(n, χ)|
2 + 1
Φ(Q) ( ∑

P |Q
deg P |n
 deg P )
2 .

For nontrivial characters which are either even or imprimitive, we use the
Riemann Hypothesis (3.33) to bound |Ψ(n, χ)|2 ≤ qn(deg Q − 1)2. Therefore

18 J.P. KEATING AND Z. RUDNICK

we ﬁnd

(5.13) G(n; Q) = 1
Φ(Q)
 ∑

χ primitive, odd |Ψ(n, χ)|
2

+ O(qn(deg Q)
2 #{χ either even or imprimitive}
Φ(Q) ) .

The number of even characters is Φ(Q)/(q−1), and the number of imprim-
itive characters is O(Φ(Q)/q). Hence the remainder term above is bounded
by O(qn−1(deg Q)2).
For each primitive odd character, the “explicit formula” (3.38) says

(5.14) Ψ(n, χ) = −qn/2 tr Θn
χ

and therefore

(5.15) G(n; Q) = qn 1
Φ(Q)
 ∑

χ odd primitive
 ∣
∣tr Θn
χ∣
∣2 + O(qn−1(deg Q)
2) .

Replacing Φ(Q) by the number of odd primitive characters times 1 + O( 1
q )
gives (5.8). □

We now use another recent equidistribution result of Katz [13]:

Theorem 5.2 (Katz [13]). Fix m ≥ 2. Suppose we are given a sequence
of ﬁnite ﬁelds Fq and squarefree polynomials Q(T ) ∈ Fq[T ] of degree m.
As q → ∞, the conjugacy classes Θχ with χ running over all primitive
odd characters modulo Q, are uniformly distributed in the unitary group
U (m − 1).

Using Theorem 5.2 we get for n > 0,

(5.16) lim
q→∞
 〈∣
∣tr Θn
χ∣
∣2〉 = ∫

U (deg Q−1) |tr U n|
2 dU

where dU is the Haar probability measure on the unitary group U (N ). Since
[3]

(5.17) ∫

U (N ) |tr U n|
2 dU = min(n, N ) ,

we ﬁnd

(5.18) lim
q→∞ G(n; Q)
qn = min(n, deg Q − 1)

which is the statement of Theorem 2.2.

VARIANCE OF THE NUMBER OF PRIME POLYNOMIALS 19

Appendix A. A calculation based on a Hardy-Littlewood-type
conjecture

In the number-ﬁeld setting, the problems we have considered here have
previously been explored using the Hardy-Littlewood conjecture relating to
the density of generalized twin primes [4, 16]. In this appendix we sketch
a heuristic calculation showing how the corresponding conjecture in the
function-ﬁeld setting may be used in the same way. As an example, we
focus on estimating G(n, Q).
The twin prime conjecture of Hardy and Littlewood for the rational
function ﬁeld Fq[T ] states that, given a polynomial 0 ̸= K ∈ Fq[T ], and
n > deg K,

(A.1) ∑

degf =n Λ(f )Λ(f + K) ∼ S(K)qn

as qn → ∞, where the ”singular series” S(K) is given by

(A.2) S(K) = ∏

P (1 − 1
|P | )
−2(1 − νK (P )
|P | ),

with the product involving all monic irreducible P and

(A.3) νK(P ) = #{A mod P : A(A + K) = 0 mod P } =
 {
1, P | K
2, P ∤ K.

While for ﬁxed q and n → ∞ the problem is currently completely open, for
ﬁxed n and q → ∞, (A.1) is known to hold [2, 1] for q odd, in the form

(A.4) ∑

degf =n Λ(f )Λ(f + K) = qn + On(qn− 1
2 ) .

Note that S(K) = 1 + On( 1
q ).
We want to use (A.1) to compute G(n; Q) and to show that the result is
consistent with

(A.5) G(n; Q) ∼ qn(deg Q − 1), n > deg Q .

It turns out that this can be done if we ignore the contribution from the
remainder implicit in (A.1). The remainder term in (A.4) is insuﬃcient for
our purposes.
Starting with

(A.6) G(n; Q) = ∑

gcd(A,Q)=1
 ∣
∣
∣
∣Ψ(n; Q, a) − qn

Φ(Q)
 ∣
∣
∣
∣

2 ,

we have
(A.7)

G(n; Q) = ∑

gcd(A,Q)=1 Ψ(n; Q, A)
2 − 2 qn

Φ(Q)
 ∑

gcd(A,Q)=1 Ψ(n; Q, A) + q2n

Φ(Q) .

20 J.P. KEATING AND Z. RUDNICK

The ﬁrst moment of Ψ(n; Q, A) is
∑

gcd(A,Q)=1 Ψ(n; Q, A) = ∑

deg f =n
gcd(f,Q)=1
 Λ(f )

= ∑

deg f =n Λ(f ) − ∑

deg f =n
deg gcd(f,Q)>0
 Λ(f )

= qn − ∑

deg P |n
P |Q prime
 deg P .

(A.8)

By Lemma 3.1 we may safely replace

(A.9) ∑

gcd(A,Q)=1 Ψ(n; Q, A) = qn + negligible.

For the second moment of Ψ(n; Q, A) we have
∑

gcd(A,Q)=1 Ψ(n; Q, A)
2 = ∑

deg f =deg g=n
f ≡g mod Q
gcd(f,Q)=1
 Λ(f )Λ(g)

= ∑

deg f =n
gcd(f,Q)=1
 Λ(f )
2 + ∑

deg f =deg g=n
f ≡g mod Q
f ̸=g
gcd(f,Q)=1
 Λ(f )Λ(g) .
(A.10)

Now

(A.11) ∑

deg f =n
gcd(f,Q)=1
 Λ(f )
2 = nqn + O(n2qn/2) − ∑

P |Q
deg P |n

(deg P )
2 .

For the sum over f ̸= g, we write the condition f = g mod Q as g = f + JQ,
J ̸= 0, deg J < n − deg Q (the number of such J of degree j is (q − 1)qj)
and then

(A.12) ∑

deg f =deg g=n
f ≡g mod Q
f ̸=g
gcd(f,Q)=1
 Λ(f )Λ(g) = ∑

deg J<n−deg Q
J̸=0
 ψ2(n; JQ)

where for K ̸= 0, deg K < n,

(A.13) ψ2(n; K) := ∑

deg f =n
f monic
 Λ(f )Λ(f + K) .

VARIANCE OF THE NUMBER OF PRIME POLYNOMIALS 21

Clearly we can split the right hand side of (A.12) as follows

(A.14) ∑

deg f =deg g=n
f ≡g mod Q
f ̸=g
gcd(f,Q)=1
 Λ(f )Λ(g) =
 n−deg Q∑

j=0
 ∑

deg J=j
J̸=0
 ψ2(n; JQ) .

The J-sum here is not restricted to monic polynomials. We can restrict it
to monics, multiplying by q − 1. Then inserting (A.1) we have

(A.15) ∑

deg f =deg g=n
f ≡g mod Q
f ̸=g
gcd(f,Q)=1
 Λ(f )Λ(g) ∼ qn(q − 1)
 n−deg Q∑

j=0
 ∑

deg J=j
J̸=0
Jmonic
 S(JQ)

as qn → ∞.
In order to estimate the J-sum in (A.15), consider

(A.16) ∑

Jmonic
 S(JQ)
|J|s = α ∑

Jmonic
 1
|J|s ∏

P |JQ
 |P | − 1
|P | − 2

where the equality follows from inserting (A.2) and

(A.17) α = ∏

P
 (1 − 1
(|P | − 1)2
 ) .

Hence

(A.18) ∑

Jmonic
 S(JQ)
|J|s = α ∏

P |Q
 |P | − 1
|P | − 2
 ∑

Jmonic
 1
|J|s ∏

P |J
P ∤Q
 |P | − 1
|P | − 2 .

Since the summand on the right hand side is multiplicative, we may write
this as
(A.19)
∑

Jmonic
 S(JQ)
|J|s = α ∏

P |Q
 |P | − 1
|P | − 2
 ∏

P ∤Q
 (1 + 1
|P |s − 1 |P | − 1
|P | − 2
 ) ∏

P |Q
 (1 − 1
|P |s
 )−1 .

Therefore

(A.20) ∑

Jmonic
 S(JQ)
|J|s = αζA(s) ∏

P |Q
 |P | − 1
|P | − 2
 ∏

P ∤Q
 (1 + 1
|P |s(|P | − 2)
 )

with

(A.21) ζA(s) = ∏

P
 (1 − 1
|P |s
 )−1 .

22 J.P. KEATING AND Z. RUDNICK

Hence
(A.22)
∑

Jmonic
 S(JQ)
|J|s = αζA(s) ∏

P |Q
 |P | − 1
|P | − 2
 (1 + 1
|P |s(|P | − 2)
 )−1 ∏

P
 (1 + 1
|P |s(|P | − 2)
 ) .

Furthermore

(A.23)
∑

Jmonic
 S(JQ)
|J|s = αζA(s)ζA(s + 1) ∏

P |Q
 |P | − 1
|P | − 2
 (
1 + 1
|P |s(|P | − 2)
 )−1

× ∏

P
 (1 + 2
|P |s+1(|P | − 2) − |P |
|P | − 2 1
|P |2s+2
 ) .

It is convenient to re-express these formulae in terms of the variable u =
1/qs. Thus |J| = u−degJ , |P | = u−degP , and

(A.24) ∑

Jmonic S(JQ)u
degJ = αZ(u)Z(u/q) ∏

P |Q
 |P | − 1
|P | − 2
 (1 + udegP

(|P | − 2)
 )−1

× ∏

P
 (1 + 2udegP

|P |(|P | − 2) − u2degP

|P |(|P | − 2)
 )

with

(A.25) Z(u) = ∏

P (1 − u
degP )
−1 = 1
1 − qu .

We can now estimate the J-sum in (A.15) by denoting

(A.26) F (u) = ∑

Jmonic S(JQ)udegJ

and using

(A.27) ∑

deg J=j
J̸=0
Jmonic
 S(JQ) = 1
2πi
 ∮ F (u)
uj+1 du ,

where the contour is a small circle enclosing the origin but no other singu-
larities of the integrand. Expanding the contour beyond the poles of F (u) at
u = 1/q and u = 1 (coming from the factors of Z(u) and Z(u/q) in (A.24)),
we ﬁnd that as q → ∞

(A.28) ∑

deg J=j
J̸=0
Jmonic
 S(JQ) ∼ qj |Q|
Φ(Q) − 1
q − 1 ,

VARIANCE OF THE NUMBER OF PRIME POLYNOMIALS 23

where we have used

(A.29) ∏

P |Q
 |P |
|P | − 1 = |Q|
Φ(Q) .

Note that the ﬁrst term in (A.28) coincides after the usual translation with
that in the corresponding expression in the number ﬁeld calculation [4], but
that interestingly the second term has a diﬀerent form.
Finally, substituting (A.28) into (A.15) and incorporating the estimates
for the other terms in (A.7), we ﬁnd that

(A.30) G(n; Q) ∼ qn (degQ − |Q|
Φ(Q)
 ) .

We now observe that as q → ∞

(A.31) |Q|
Φ(Q) → 1

and so in this limit, when n is ﬁxed with degQ ≤ n + 1, this calculation
matches Theorem 2.2. Furthermore, when degQ → ∞ with q ﬁxed we have
that

(A.32) G(n; Q) ∼ qndegQ

which is consistent with the Hooley’s conjecture (1.10) in the number ﬁeld
case.

Acknowledgements: We thank Nick Katz for several discussions, and
Julio Andrade and the referees for their comments.

References

[1] L. Bary-Soroker, Twin prime analog over large ﬁnite ﬁelds. preprint
arXiv:1206.3930v1.
[2] A. Bender and P. Pollack, On quantitative analogues of the Goldbach and twin prime
conjectures over Fq[t], preprint arXiv:0912.1702v1
[3] P. Diaconis and M. Shahshahani. On the eigenvalues of random matrices. Studies in
applied probability. J. Appl. Probab. 31A (1994), 4962.
[4] J. B. Friedlander and D. A. Goldston, Variance of distribution of primes in residue
classes. Quart. J. Math. Oxford Ser. (2) 47 (1996), no. 187, 313–336.
[5] Gallagher, P. X. On the distribution of primes in short intervals. Mathematika 23
(1976), no. 1, 4–9.
[6] D. A. Goldston, and H. L. Montgomery, Pair correlation of zeros and primes in short
intervals. Analytic number theory and Diophantine problems (Stillwater, OK, 1984),
183–203, Progr. Math., 70, Birkh¨auser Boston, Boston, MA, 1987.
[7] Goldston, D. A.; Yildirim, C. Y. Primes in short segments of arithmetic progressions.
Canad. J. Math. 50 (1998), no. 3, 563–580.
[8] C. Hooley, On the Barban-Davenport-Halberstam theorem. I. Collection of articles
dedicated to Helmut Hasse on his seventy-ﬁfth birthday, III. J. Reine Angew. Math.
274/275 (1975), 206–223.
[9] C. Hooley, On the Barban-Davenport-Halberstam theorem. II. J. London Math. Soc.
(2) 9 (1974/75), 625–636.

24 J.P. KEATING AND Z. RUDNICK

[10] C. Hooley, The distribution of sequences in arithmetic progression, Proc. ICM Van-
couver (1974), 357–364.
[11] C. Hooley, On the Barban-Davenport-Halberstam theorem. V. Proc. London Math.
Soc. (3) 33 (1976), no. 3, 535–548.
[12] N .M. Katz, Convolution and Equidistribution: Sato-Tate Theorems for Finite-Field
Mellin Transforms, Annals of Mathematics Studies, 180. Princeton University Press,
Princeton, NJ, 2012.
[13] N. M. Katz, On a Question of Keating and Rudnick about Primitive Dirichlet Char-
acters with Squarefree Conductor, Int Math Res Notices ﬁrst published online June
4, 2012 doi:10.1093/imrn/rns143
[14] N. M. Katz, Witt vectors and a question of Keating and Rudnick, Int Math Res
Notices, ﬁrst published online June 20, 2012 doi:10.1093/imrn/rns144 .
[15] H. L. Montgomery, Primes in arithmetic progressions. Michigan Math. J. 17 1970
33–39.
[16] H. L. Montgomery and K. Soundararajan. Primes in short intervals. Comm. Math.
Phys. 252 (2004), no. 1-3, 589–617.
[17] M. Rosen, Number theory in function ﬁelds. Graduate Texts in Mathematics, 210.
Springer-Verlag, New York, 2002.
[18] A. Weil, Basic number theory. Third edition. Die Grundlehren der Mathematischen
Wissenschaften, Band 144. Springer-Verlag, New York-Berlin, 1974

School of Mathematics, University of Bristol, Bristol BS8 1TW, UK
E-mail address: j.p.keating@bristol.ac.uk

Raymond and Beverly Sackler School of Mathematical Sciences, Tel Aviv
University, Tel Aviv 69978, Israel
E-mail address: rudnick@post.tau.ac.il
