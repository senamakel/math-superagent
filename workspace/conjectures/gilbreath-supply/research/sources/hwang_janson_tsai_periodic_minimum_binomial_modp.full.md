<!-- source: https://arxiv.org/pdf/2408.06817 | converted from PDF -->

Periodic minimum in the count of binomial
coefficients not divisible by a prime

Hsien-Kuei Hwang
Institute of Statistical Science
Academia Sinica
Taipei 115
Taiwan
 Svante Janson
Department of Mathematics
Uppsala University
Uppsala
Sweden

Tsung-Hsi Tsai
Institute of Statistical Science
Academia Sinica
Taipei 115
Taiwan

August 14, 2024

Abstract

The summatory function of the number of binomial coefficients not divisible by a prime
is known to exhibit regular periodic oscillations, yet identifying the less regularly behaved
minimum of the underlying periodic functions has been open for almost all cases. We propose
an approach to identify such minimum in some generality, solving particularly a previous
conjecture of B. Wilson [Asymptotic behavior of Pascal’s triangle modulo a prime, Acta Arith.
83 (1998), pp. 105–116].

1 Introduction

Let Fp(n) denote the number of binomial coefficients (
m
k )
, 0 ⩽ k ⩽ m < n, that are not divisible
by a given prime p. In particular, for p = 2, F2(n) is the number of odd numbers in the first n
rows of Pascal’s triangle. The study of the quantity Fp(n) has a long history; see, for example,
the historical account in Stolarsky’s paper [11]. Some sequences of Fp(n) appear in the On-Line
Encyclopedia of Integer Sequences (OEIS) [9]: A006046 (p = 2), A006048 (p = 3), and A194458
(p = 5).
 1arXiv:2408.06817v1  [math.NT]  13 Aug 2024
Fine [3] proved that “almost all” binomial coefficients are divisible by a prime p, more precisely
that
 lim
n→∞ Fp(n)
(
n+1
2 ) = 0. (1.1)

He [3] also gave the expression (with n = ∑
0⩽i⩽s bi2
i, bi ∈ {0, 1})

Fp(n + 1) − Fp(n) = ∏

0⩽i⩽s
(bi + 1) (1.2)

for the number of binomial coefficients (
n
k)
, 0 ⩽ k ⩽ n, not divisible by p.
Later Stein [10] observed that, for any prime p,

Fp(pn) = (
p + 1
2
 )
Fp(n), n ⩾ 1, (1.3)

Thus the sequence ψp(n) := Fp(n)/n
ρp, where ρp = logp (
p+1
2 )
, satisfies ψp(pn) = ψp(n), so
that ψp can be extended by this property to all positive p-adic rational numbers. Stein [10] also
showed that ψp can be further extended to a continuous function on (0, ∞); in other words, there
exists a continuous 1-periodic function Pp(t) on R such that

Fp(n) = n
ρpPp(logp n), n ⩾ 1. (1.4)

It follows immediately from this that

αp := lim sup
n→∞ Fp(n)
nρp = sup
n⩾1
 Fp(n)
nρp = max
t∈[0,1] Pp(t) ∈ [0, ∞), (1.5)

βp := lim inf
n→∞ Fp(n)
nρp = inf
n⩾1 Fp(n)
nρp = min
t∈[0,1] Pp(t) ∈ [0, ∞), (1.6)

furthermore, αp = 1 for every p, and that (
p+1
2 )−1 ⩽ βp < 1; see [10]. The extremal properties
of P2 had earlier been treated by Stolarsky [11] and Harborth [5]. In particular, Harborth proved
that α2 = 1 and derived the numerical value β2 .
= 0.812556 to 6 decimal places; see A077464
(Stolarsky-Harborth constant) for more information. Further numerical estimates of βp for various
p have been made later; of special mention is Chen and Ji’s inequalities [1]:

1
(1 + p−r)ρp min
pr⩽n⩽pr+1 Fp(n)
nρp ⩽ βp ⩽ min
pr⩽n⩽pr+1 Fp(n)
nρp , (1.7)

which in principle makes it possible to calculate βp to any given degree of precision. However, an
exact expression remains unknown.
For p ⩾ 3, Volodin [13] conjectured that

β3 = (3
2
 )1−ρ3 = 2
log3 2−1, (1.8)

2

which was proved by Franco [4]; however, his proof does not extend to other primes p.
Wilson [16] calculated β3, β5, . . . , β19 to six decimal places and showed that

lim
p→∞ βp = 0.5. (1.9)

He furthermore conjectured that

β5 = (3
2
)1−ρ5 , β7 = (3
2
)1−ρ7 , β11 = 59
44
 (22
31
 )ρ11 . (1.10)

The main purpose of the present paper is to prove this conjecture, and to give similar results
for further primes p. More precisely, by a detailed examination of the periodic function Pp(x),
coupling with analytic bounds and numerical calculations, we are able to find the minimum βp
for all odd primes 3 ⩽ p ⩽ 113, proving particularly Wilson’s conjectures (1.10) and differently
(1.8). Our approach can be readily extended to higher values of p, but a proof for all odd primes p
remains open.
In our approach we fix an odd prime p. After a change of variables (see Section 3 for details),
we obtain βp = mins∈[p−1,1] G(s) for the function G(s) = Gp(s) defined in (3.2). The main part
of our argument is to show that (for the primes p that we have studied, at least) this minimum is
attained at the point
 ˆsp = ˆsp(ξ, η) := 2ξ + 1
2p − η
p2 , (1.11)

for a suitable pair of integers (ξ, η) with 1 ⩽ ξ < p and 0 ⩽ η ⩽ p−1
2 . In terms of p-ary expansion,

ˆsp = (0.b1b2 . . . ), where b1 = ξ, b2 = p−1
2 − η, and bj = p−1
2 for j ⩾ 3. (1.12)

When this holds, we thus have βp = Bξ,η := G(ˆsp), which explicitly is given by (see Lemma 4.1)

Bξ,η = (
ξ + 1
2
 ) (
1 + (p − 2η)(p − 2η + 1)
2ξp(p + 1)
 ) (2ξ + 1
2 − η
p
 )−ρp . (1.13)

One complication is that the correct choice of (ξ, η) is not obvious and depends on p, as is illus-
trated in the following theorem, which is our main result.

Theorem 1.1. Wilson’s conjecture (1.10) holds true. More generally, for an odd prime p, 3 ⩽ p ⩽
113, we have βp = Bξ,η where the pair of values (ξ, η) (together with ˆsp(ξ, η)) are given in the
following table:

p {3, 5, 7} {11, 13, 17, 19, 23} {29} {31, 37, 41, 43, 47, 53}

(ξ, η) (1, 0) (1, 1) (2, 1) (2, 2)

ˆsp(ξ, η) 3
2p 3
2p − 1
p2 5
2p − 1
p2 5
2p − 2
p2

p {59, 61, 67, 71, 73, 79} {83, 89, 97, 101, 103, 107} {109, 113}

(ξ, η) (2, 3) (2, 4) (2, 5)

ˆsp(ξ, η) 5
2p − 3
p2 5
2p − 4
p2 5
2p − 5
p2
 (1.14)

3

Indeed, the same result βp = Bξ,η holds for larger values of p with suitably chosen (ξ, η), and
our numerical calculations confirmed this for p up to several thousand (see Section 6); however, a
proof for all odd primes remains open.
In particular, we obtain

p 13 17 βp(p = 3, . . . , 113)

βp
 124
91 ( 26
37)log13 91

≈ 0.73266
 71
51 ( 34
49 )log17 153

≈ 0.72758

p 19 113

βp
 533
380 ( 38
55 )log19 190

≈ 0.72575
 7780
2147 ( 226
555)log113 6441

≈ 0.68432
 (1.15)

To prove Theorem 1.1, in view of (1.6), it suffices to find the minimum of Pp(logp s) for
s ∈ [p−1, 1] . Wilson (1998) conjectured (in a different formulation for integers n, see Remark 3.1
below) that for any p, the minimum βp occurs at some point ˆsp such that all but a finite number of
its base p digits are equal to p−1
2 . Note that the point ˆsp of (1.11)–(1.12) is of the type consistent
with Wilson’s conjecture.
We observe that the graph of Pp(log s) has a self-similar nature, and if the graph is “zoomed in”
on such points s, the resulting function converges uniformly. We then find the local behavior from
the limiting function. The proof of (1.14) then builds on this idea, and this implies in particular
Wilson’s conjecture (1.10); see Section 4 for the details of the proof.

Problem 1.2. The apparently simplest case p = 2 seems to be actually the most complicated.
Despite many digits of β2 are known (see A077464 and the references therein), to the best of our
knowledge, no exact expression for β2 is available or proposed or conjectured. How to character-
ize the minimum point ˆs2, and what is the corresponding minimum value β2?

Problem 1.3. The main open question is whether βp = Bξ,η for some (ξ, η) for all odd primes p.
Equivalently, is the minimum point always some ˆsp (defined in (1.11))?

Our approach is based on the resolution of the recurrence (2.1) satisfied by Fp(n), which we
prove below in Theorem 2.1, following the same arguments used in our previous paper [8]. No
other number-theoretic properties are needed. This then yields the representation (1.4) with a
continuous periodic functions Pp, and a special explicit formula for Pp that we will use. Indeed,
in the case p = 2, this recurrence is of the binary form studied in [8], and F2(n) was one of the
many examples discussed there. We show in Appendix A that the method of [8] can be generalized
to a general class of p-ary recursions including (2.1). (The results in the appendix are valid for any
integer p ⩾ 2.)
More generally, a number of authors have studied Fp,d(n), the number of multinomial coeffi-
cients ( m
j1,...,jd) with 0 ⩽ m < n that are not divisible by p.

Problem 1.4. Extend the methods and results of the present paper to multinomial coefficients.

4

2 A recurrence and its solutions

In this section, we fix a prime p ⩾ 2.

Theorem 2.1. The total number of binomial coefficients (
m
k ) with m, k < n that are not divisible
by p satisfies the recurrence

Fp(n) = ∑

0⩽j<p(p − j)Fp
 (⌊n + j
p
 ⌋) (n ⩾ p), (2.1)

with the initial values {Fp(j) = (
j+1
2 ) : j = 1, . . . , p − 1}. In fact, (2.1) holds for all n ⩾ 0, with
Fp(0) := 0.

Proof. It is obvious that ( j
k
) is not divisible by a prime p if k ⩽ j < p. Thus the initial values are

Fp(j) = (
j + 1
2
 ) for j = 1, . . . , p − 1. (2.2)

We use the following expression from Volodin [12] (there stated more generally for multinomial
coefficients):
 Fp(n) = 1
2
 ∑

0⩽j⩽ν
 (
p + 1
2
 )jbj ∏

j⩽i⩽ν
(bi + 1), (2.3)

[see also [1]] where bj ∈ {0, . . . , p − 1} are the base p digits of n = b0 + b1p + · · · + bνpν.
(The formula (2.3) holds trivially for n = 0 too, with an empty sum.) If n = kp, then b0 = 0 and
k = b1 + b2p + · · · + bνpν−1. Thus, from (2.3),

Fp(n) = 1
2
 ∑

1⩽j⩽ν
 (
p + 1
2
 )jbj ∏

j⩽i⩽ν
(bi + 1)

= (
p + 1
2
 ) · 1
2
 ∑

1⩽j⩽ν
 (
p + 1
2
 )j−1bj ∏

j⩽i⩽ν
(bi + 1)

= (
p + 1
2
 ) · 1
2
 ∑

0⩽j⩽ν−1
 (
p + 1
2
 )jbj+1 ∏

j⩽i⩽ν−1
(bi+1 + 1)

= (
p + 1
2
 )
Fp(k). (2.4)

In general, suppose n = kp + r, where k ⩾ 0 and 0 ⩽ r < p. Then b0 = r and (2.3) yields

Fp(n) − Fp(kp) = r
2
 ∏

0⩽i⩽ν
(bi + 1) = r(r + 1)
2
 ∏

1⩽i⩽ν
(bi + 1) (2.5)

since all but the first term in the sums cancel. By Fine’s result (1.2), this yields

Fp(n) − Fp(kp) = (
r + 1
2
 ) (Fp(k + 1) − Fp(k)) . (2.6)

5

Thus we have
 Fp(n) = Fp(kp) + (Fp(n) − Fp(kp))

= (
p + 1
2
 )
Fp(k) + (
r + 1
2
 ) (Fp(k + 1) − Fp(k))

= ∑

0⩽j<p(p − j)Fp(k) + (
r + 1
2
 ) (Fp(k + 1) − Fp(k))

= ∑

0⩽j⩽p−r−1
(p − j)Fp(k) + ∑

p−r⩽j<p(p − j)Fp(k + 1)

= ∑

0⩽j<p(p − j)Fp
 (⌊n + j
p
 ⌋) . (2.7)

This proves the recurrence (2.1).

Theorem 2.1 shows that Fp(n) satisfies a recurrence of the type treated in Appendix A. From
Theorem A.3 we thus immediately obtain the representation (1.4), together with the following
formula for Pp(t). (This formula is essentially given in [2].)

Theorem 2.2. Define
 A = Ap := (
p + 1
2
 )
. (2.8)

Then the number of binomial coefficients in the first n rows that are not divisible by p satisfies

Fp(n) = n
ρP (
logp n
) for all n ⩾ 1, (2.9)

where ρ = ρp := logp A and P(t) = Pp(t) is a continuous 1-periodic function given by

P(t) := A1−{t}φ(p{t}−1), (2.10)

with the function φ = φp : [0, 1] → R given by the explicit formula

φ
 (∑

j⩾1 bjp−j)
 = 1
2
 ∑

j⩾1
 bj
Aj ∏

1⩽i⩽j
(bi + 1), (2.11)

for any bj ∈ {0, 1, 2, . . . , p − 1}; furthermore, φ satisfies that for j = 0, 1, . . . , p − 1,

φ(t) = j + 1
A φ({pt}) +
 (
j+1
2 )

A , if j
p ⩽ t ⩽ j + 1
p . (2.12)

Proof. By Theorem 2.1, Fp(n) satisfies the recurrence (A.1) with γi = p − i. We have

∑

p−j⩽i<p γi = (
j + 1
2
 ) = Fp(j) for j = 1, . . . , p − 1, (2.13)

6

and thus the condition (A.26) is satisfied; see also Remark A.5. Similarly, A in (A.2) is given by
(2.8). The results follow by Theorem A.3 and Lemma A.1; (2.12) follows by plugging γj = p − j
into (A.3), and (A.4) yields

φ
 (∑

j⩾1 bjp−j)
 = ∑

j⩾1
 ∑p
i=p−bj(p − i)

Aj ∏

1⩽i<j
(bi + 1)

= 1
2
 ∑

j⩾1
 bj(bj + 1)
Aj ∏

1⩽i<j
(bi + 1)

= 1
2
 ∑

j⩾1
 bj
Aj ∏

1⩽i⩽j
(bi + 1), (2.14)

for any bj ∈ {0, 1, 2, . . . , p − 1}, which is (2.11).

3 Our approach

In this section, p is a fixed odd prime. Recall that A = (
p+1
2 ) and ρp = logp A.
By (1.6) and Theorem 2.2, βp is the minimum of the periodic function

P(t) := A1−tφ(pt−1) for t ∈ [0, 1), (3.1)

where φ is given by (2.11). (By continuity, we may as well take the minimum for t ∈ [0, 1].) We
make the change of variables s = pt−1 and consider

G(s) := A− logp sφ(s) for s ∈ [p−1, 1]; (3.2)

thus P(t) = G(pt−1) for t ∈ [0, 1), and thus βp = min{G(s) : s ∈ [p−1, 1]}. Note that

A− logp s = p−ρp logp s = s−ρp. (3.3)

Remark 3.1. For any n ⩾ 1, by (2.9)–(2.10) and (3.1)–(3.2), we see that

Fp(n)n
−ρp = P(logp n) = P({logp n}) = G
(
p{logp n}−1) = G
(
np
−⌊logp n⌋−1)
. (3.4)

It follows that if G attains its minimum on [p−1, 1] at ˆs, then the sequence nk := ⌊pk ˆs⌋ satisfies

Fp(nk)n
−ρp
k → G(ˆs) = βp, (3.5)

and thus the infimum βp is asymptotically reached by the sequence (nk). Conversely, Wilson [16]
conjectured (in a somewhat stronger form) that

βp = lim
k→∞(Fp(nk)n
−ρp
k ), (3.6)

for a sequence nk given by the recursion nk+1 = pnk+ p−1
2 for a suitably chosen n1; this sequence
is of the form just mentioned (up to a shift of indices), and Wilson’s conjecture thus would imply
that the minimum on [p−1, 1] is attained at a point ˆs such that all but a finite number of the digits
in base p of ˆs are p−1
2 . Note that all points ˆs that we consider as potential minimum points are of
this type, see (1.12). △

7

Our methods of proof consists of two major techniques: magnifying mapping and piecewise
monotonic majorization. The former defines first a mapping θ and magnifies the local difference
of G(θ(s)) − G(θ( 1
2)) in a small neighborhood, say J, of ˆs = θ( 1
2 ) into the global difference
φ(s) − φ( 1
2), justifying that G(ˆs) is a local minimum in J. The latter bounds crudely the ratio
between two monotonic functions by their extreme values in the targeted interval, which, after
partitioning the interval [0, 1] \ J into proper subintervals, is used interval-by-interval to check that
G(ˆs) is also a minimum in [0, 1] \ J.

3.1 A magnifying mapping

As the minimum ˆs of G(s) we are going to prove all have the form (1.11) whose p-ary expansion
has an infinity number of trailing digits of the form p−1
2 , we construct a linear mapping as follows.
Fix M and m with 1 ⩽ m < p
M. Let µ be the middle point of [ m
pM , m+1
pM ]:

µ := m + 1
2
pM . (3.7)

For every k ⩾ 0, define a linear mapping θk from [0, 1] onto the interval

IM+k := [µ − 1
2pM+k , µ + 1
2pM+k
 ] (3.8)

by
 θk(t) := m
pM + ∑

M<j⩽M+k
 p − 1
2 pj + t
pM+k , t ∈ [0, 1]. (3.9)

Thus µ = θk( 1
2). In terms of the p-ary expansion, if

m = a1pM−1 + · · · + aM−1p + aM, (3.10)

then µ has the form µ = (0. ˆb1 ˆb2 · · · )p, where

ˆbi = ai for 1 ⩽ i ⩽ M and ˆbi = p − 1
2 for i ⩾ M + 1. (3.11)

We prove that the “zoomed” functions G(θk(t)) − G(µ), suitably scaled, converge uniformly
on [0, 1], and we give a sufficient condition for G(µ) to be a minimum in an explicitly specified
interval.
Note that φ(µ) has the form, by (2.11) and (3.11),

φ(µ) = 1
2
 ∑

1⩽j⩽M
 aj ∏j
i=1(1 + ai)
Aj + τM
4 = 1
2
 ∑

1⩽j⩽M
 aj ∏j
i=1(1 + ai)
Aj + τMφ (1
2
) , (3.12)

where
 τM := ∏M
i=1(1 + ai)
AM . (3.13)

The construction of the mapping θk is helpful in bringing the local difference φ(θk(t)) −
φ(θk( 1
2 )) into a global one in terms of φ(t) − φ( 1
2 ).

8

Lemma 3.2. We have
 pk(
φ(θk(t)) − φ(µ)) = τM
 (
φ(t) − φ (1
2
)) . (3.14)

Proof. Let bi and ˜bi be the base p digits of t and θk(t), respectively. Then (3.9) shows that the
first M + k digits ˜bi coincide with those of µ given by (3.11):

˜bi = ˆbi = ai for 1 ⩽ i ⩽ M and ˜bi = ˆbi = p − 1
2 for M + 1 ⩽ i ⩽ M + k, (3.15)

and also that the remaining digits of ˜bi are the digits of t, i.e.,

˜bi+k+M = bi, i ⩾ 1. (3.16)

Hence, if we compute φ(θk(t)) and φ(µ) by (2.11), then the first M + k terms are equal, and we
obtain

φ(θk(t)) − φ(µ) = 1
2
 ∑

j⩾k+M+1
 ˜bj ∏j
i=1 ( ˜bi + 1)

Aj (3.17)

− 1
2
 ∑

j⩾k+M+1
 p−1
2 ∏M
i=1 (ai + 1) ∏j
i=M+1 ( p−1
2 + 1)

Aj

= ∏M
i=1 (ai + 1)
Ak+M
 (p + 1
2
 )k 1
2
 (∑

l⩾1
 bl ∏l
i=1 (bi + 1)
Al − ∑

l⩾1
 p−1
2 ( p+1
2 )l

Al
 )

= τM
pk
 (
φ(t) − φ (1
2
)) .

The crucial properties we need of the magnifying mapping θk are given as follows, the first for
large k and the second for finite one.

Theorem 3.3. With the notations as above, we have, uniformly for t ∈ [0, 1],

pk (G(θk(t)) − G(µ)) = µ−ρp−1 (
Qµ(t) + O (
p−k)) , (3.18)

for large k, where the limiting function Qµ(t) is given by

Qµ(t) := τMµ (
φ(t) − φ (1
2
)) − ρpφ(µ)
pM
 (
t − 1
2
) . (3.19)

Furthermore, if for some k ⩾ 0,

Qµ(t) ⩾ Eµ,k(t) for all t ∈ [0, 1
2 − 1
2p
 ] ∪ [ 1
2 + 1
2p , 1
] , (3.20)

where
 Eµ,k(t) := τMρp
pM+k
 (
φ(t) − φ (1
2
)) (t − 1
2
 ) , (3.21)

then G(µ) is the minimum of the function G in the interval IM+k (defined in (3.8)), and this
minimum is attained only at µ.
 9

Proof. For simplicity, we use the abbreviations (with an abuse of notation): ∇G(θ) := G(θk(t))−
G(µ), ∇φ(θ) := φ(θk(t)) − φ(µ), ∇φ := φ(t) − φ( 1
2 ), ∇θ := θk(t) − µ and ∇t := t − 1
2.
Observe first that a Taylor expansion yields

θ
−ρp − µ−ρp + ρpµ−ρp−1(θ − µ) = Jθ,µµ−ρp−1(θ − µ)2, (3.22)

where
 Jθ,µ := µρp+1ρp(ρp + 1) ∫ 1

0 x(µx + θ(1 − x))−ρp−2dx (3.23)

remains positive whenever θ, µ > 0 and θ ̸= µ (or t ̸= 1
2 ). Applying this expansion, we obtain

∇G(θ) = θk(t)−ρp(
φ(θk(t)) − φ(µ)) + φ(µ)(
θk(t)−ρp − µ−ρp)

= µ−ρp−1∇φ(θ) (
µ − ρp∇θ + Jθk(t),µ(
∇θ
)2)

− φ(µ)µ−ρp−1 (
ρp∇θ − Jθk(t),µ(
∇θ
)2) ; (3.24)

thus

µρp+1∇G(θ) = µ∇φ(θ) − ρpφ(µ)∇θ − ρp∇φ(θ)∇θ + Jθk(t),µφ(θk(t))(
∇θ
)2. (3.25)

By (3.9) pk∇θ = p−M∇t. (3.26)

This, together with (3.25), Lemma 3.2, and the definitions (3.19) and (3.21) of Qµ and Eµ,k, gives

pk∇G = µ−ρp−1(Qµ(t) − Eµ,k(t) + Rµ,k(t)), (3.27)

where
 Rµ,k(t) := pkJθk(t),µφ(θk(t))(
∇θ
)2. (3.28)

We note for later use that, by (3.28) and (3.23),

Rµ,k(t) > 0, if θk(t) ̸= µ (i.e., t ̸= 1
2 ). (3.29)

Since p, M, and (ai)M
1 are fixed, and φ(t) is bounded, we see that

Rµ,k(t) = O (
p−k) , (3.30)

Similarly, (3.21) implies that Eµ,k(t) = O (
p−k) . (3.31)

Hence, (3.18) follows from (3.27), (3.30), and (3.31).
Now assume that (3.20) holds for some k. Then it also holds for all larger k as well, since
Eµ,k(t) ⩾ 0 and the only factor in (3.21) that depends on k is p−k.

10

Let x ∈ IM+k = [µ − 1
2 p−(M+k), µ + 1
2p−(M+k)] with x ̸= µ. Let kx ⩾ k be the largest
integer such that x ∈ IM+kx, and let tx ∈ [0, 1] be such that θkx(tx) = x. Then x /∈ IM+kx+1 and
thus
 tx ∈ [0, 1
2 − 1
2p
 ) ∪ (1
2 + 1
2p , 1
] . (3.32)

Hence, by (3.27), (3.29), and (3.20),

µρp+1pkx (G(x) − G(µ)) = µρp+1pkx(
G(θkx(tx)) − G(µ))

= Qµ(tx) − Eµ,kx(tx) + Rµ,kx(tx)
> Qµ(tx) − Eµ,kx(tx) ⩾ 0. (3.33)

Thus G(x) > G(µ) for every x ̸= µ in IM+k, which shows that µ is the unique minimum point of
G in the interval IM+k.

3.2 Monotonic majorization

Once we convert the minimality of G(s) at s = µ in IM+k to the positivity of ∆µ,k(t) := Qµ(t) −
Eµ,k(t) for t in the unit interval excluding a small neighborhood of t = 1
2 (see (3.20)), we then need
means of handling the positivity of the difference of two monotonic functions because ∆µ,k(t) can
be expressed as:

∆µ,k(t) := Qµ(t) − Eµ,k(t)

=
 



 ρpφ(µ)
pM ( 1
2 − t) − τM (
φ ( 1
2) − φ(t)) (
µ + ρp
pM+k ( 1
2 − t)) , if t ∈ [0, 1
2 ],

τMµ (
φ(t) − φ ( 1
2 )) − ρp
pM (
t − 1
2 ) (
φ(µ) + τM
pk (
φ(t) − φ ( 1
2))) , if t ∈ [ 1
2 , 1],

(3.34)

the first being the difference of two positive decreasing functions, the second that of two increasing
functions, and the condition (3.20) then being equivalent to ∆µ,k(t) ⩾ 0.
On the other hand, G(s) = s−ρpφ(s) can also be regarded as the ratio of two increasing
functions. Thus to show that G attains nowhere the minimum value β for s outside a small neigh-
borhood of µ, we need to handle the ratio of two increasing functions.
Since the function φ(t) is of fractal type, we use the following simple idea.

Lemma 3.4. Assume that f, g are increasing functions on [a, b] with f ⩾ 0 and g > 0 there.
If f(a)/g(b) > C, then f(x)/g(x) > C for x ∈ [a, b]. Similarly, if f(a) − g(b) > C, then
f(x) − g(x) > C for x ∈ [a, b].

Proof. By monotonicity, for x ∈ [a, b],
f(x)
g(x) ⩾ f(a)
g(b) > C. (3.35)

The difference version is similar: f(x) − g(x) ⩾ f(a) − g(b) > C.

11

The case when f, g are decreasing functions is similar.
In particular, for δ > 0, if (x + δ)−ρpφ(x) > β, then G(t) = t−ρpφ(t) > β for t ∈ [x, x + δ].
Such a simple idea will be applied numerically to sufficiently small subintervals after a suitable
partition of the target interval.

4 Proof of Theorem 1.1 for p = 3, 5, 7

We begin with the proof of (1.13). Again p ⩾ 3 is a prime number.

Lemma 4.1. G(ˆsp) = Bξ,η given in (1.13), where ˆsp = 2ξ+1
2p − η
p2 .

Proof. The p-ary expansion of ˆsp has the form ˆsp = (0.b1b2 . . . )p with b1 = ξ, b2 = p−1
2 − η
and bj = p−1
2 for j ⩾ 3. Then, by (2.11),

2φ(ˆsp)
ξ + 1 = ξ
A + 1
A2
 (p − 1
2 − η
) (p + 1
2 − η
)

+ p − 1
2
 (p + 1
2 − η
) ∑

k⩾3
 1
Ak
 (p + 1
2
 )k−2

= ξ
A + (p − 2η)(p − 2η + 1)
4A2 , (4.1)

or
 φ(ˆsp) = ξ + 1
2A
 (
ξ + (p − 2η)(p − 2η + 1)
2p(p + 1)
 ) . (4.2)

Thus
G(ˆsp) = ˆs−ρp
p φ(ˆsp) = ξ + 1
2
 (
ξ + (p − 2η)(p − 2η + 1)
2p(p + 1)
 ) (2ξ + 1
2 − η
p
 )−ρp , (4.3)

which is the same as (1.13).

We prove Wilson’s conjecture for p = 3, 5, 7, and establish the values β3, β5, β7 in (1.8) and
(1.10). Let s1 := ˆsp(1, 0) = 3
2p, whose p-ary expansion is of the form (0.1bbb . . . )p, where
b = p−1
2 .

4.1 Minimality of G(s) in I2 = [ 3
2p − 1
2p2 , 3
2p + 1
2p2 ]

Take m = M = 1 and k = 1 in Theorem 3.3 so that µ = s1 = 3
2p and I2 = [ 3
2p − 1
2p2 , 3
2p + 1
2p2 ].
We have a1 = 1 and we obtain from (3.13) and (4.2) with (ξ, η) = (1, 0),

τ1 = 2
A and φ(µ) = 3
2A . (4.4)

12

Then (3.19) and (3.21) in Theorem 3.3 yield

Qs1(t) = 3
pA
 (
φ(t) − φ (1
2
)

︸ ︷︷ ︸
=:K1(t)
 −ρp
2
 (
t − 1
2
)

︸ ︷︷ ︸
=:K2(t)
 )
, (4.5)

and
 Es1,1(t) = 2ρp
Ap2
 (
φ(t) − φ (1
2
)) (t − 1
2
) =: 3
pA K3(t). (4.6)

Thus, we can write
 pA
3 ∆µ,1(t) =
 {K2(t) − (−K1(t) + K3(t)), if t ∈ [0, 1
2 ],
K1(t) − (−K2(t) + K3(t)), if t ∈ [ 1
2 , 1], (4.7)

where K2(t) and −K1(t) + K3(t) are both positive and decreasing for t ∈ [0, 1
2], and K1(t) and
−K2(t) + K3(t) are both positive and increasing for t ∈ [ 1
2, 1]. According to Theorem 3.3, if

∆µ,1(t) ⩾ 0 for t ∈ [0, 1
2 − 1
2p
 ] ∪ [ 1
2 + 1
2p , 1
] , (4.8)

then s1 is the minimum of G(s) for s ∈ [ 1
2 − 1
2p2 , 1
2 + 1
2p2 ]. To check the validity of (4.8), we
partition the two intervals in (4.8) into equally-spaced subintervals in each of which we apply the
idea used in Lemma 3.4; namely, for some (large) integers N1 and N2,
{K2(tj+1) − (−K1(tj) + K3(tj)) ⩾ 0, with tj = (p−1)j
2pN1 ,
K1(˜tj) − (
−K2(˜tj+1) + K3(˜tj+1)) ⩾ 0, with ˜tj = 1
2 + 1
2p + (p−1)j
2pN2 , (4.9)

for j = 0, 1, . . . , Ni − 1, i = 1, 2. This process is purely numerical and brings the condition (4.8)
into a finitely computable one.
For example, take p = 3. Then N1 = 9 is sufficient for t ∈ [0, 1
2 − 1
2p], and N2 = 7 for
t ∈ [ 1
2 + 1
2p, 1]. More precisely, we have the numerical values in each case:

∆µ,1(t) > K2(tj+1) − (−K1(tj) + K3(tj)), tj = (p−1)j
2pN1 & N1 = 9

j 1 2 3 4 5 6 7 8 9

∆µ,1 > 0.082 0.060 0.044 0.033 0.016 0.009 0.012 0.00001 0.001

∆µ,1(t) > K1(˜tj) − (
−K2(˜tj+1) + K3(˜tj+1))

˜tj = 1
2 + 1
2p + (p−1)j
2pN2 & N2 = 7

j 1 2 3 4 5 6 7

∆µ,1 > 0.054 0.023 0.013 0.006 0.016 0.043 0.023

Similarly, for p = 5, we use (N1, N2) = (35, 10), and for p = 7, (N1, N2) = (114, 17), respec-
tively.
In this way, we prove, by Theorem 3.3, that s = s1 = 3
2p is the minimum of G(s) for s ∈ I2 =
[s1 − 1
2p2 , s1 + 1
2p2 ].
 13

Figure 1: Fluctuations of G(s), s ∈ [p−1, 1], for p = 3, 5, 7.

4.2 G(s) in [ 1
p, 1] \ I2

Following the same numerical procedure used above for justifying the minimality of G(s) at s = s1
for s ∈ I2, we partition the two intervals [ 1
p, 3
2p − 1
2p2 ] and [ 3
2p + 1
2p2 , 1] into N3 and N4 subintervals,
and check, by the simple monotonic bounds in Lemma 3.4, that G(s) > β for s in each of these
subintervals.
Since G(s) = s−ρpφ(s) is the ratio of two increasing functions in the unit interval, we check
the conditions

G(s) − β

>
 { σ
−ρp
j+1 φ(σj) − β > 0, if σj := 1
p + (p−1)j
2p2N3 , j = 0, . . . , N3 − 1

˜σ
−ρp
j+1 φ( ˜σj) − β > 0, if ˜σj := 3
2p + 1
2p2 + (2p2−3p−1)j
2p2N4 , j = 0, 1, . . . , N4 − 1,
 (4.10)

for s in each of the subintervals [σj, σj+1] and [ ˜σj, ˜σj+1], respectively.
For example, for p = 3, we can take N3 = 9 and N4 = 16 for which the corresponding
numerical values are listed as follows.

G(s) − β > σ
−ρp
j+1 φ(σj) − β > 0, σj given in (4.10) & N3 = 9
j 1 2 3 4 5 6 7 8 9
σ
−ρp
j+1 φ(σj) − β 0.168 0.123 0.091 0.067 0.040 0.027 0.023 0.008 0.008

G(s) − β > ˜σ
−ρp
j+1 φ( ˜σj) − β > 0, ˜σj given in (4.10) & N4 = 16
j 1 2 3 4 5 6 7 8
˜σ
−ρp
j+1 φ( ˜σj) − β) 0.029 0.002 0.006 0.044 0.131 0.090 0.060 0.049
j 9 10 11 12 13 14 15 16
˜σ
−ρp
j+1 φ( ˜σj) − β 0.054 0.033 0.026 0.042 0.088 0.076 0.079 0.112

Similarly, for p = 5, we can take (N3, N4) = (35, 77), and for p = 7, (N3, N4) = (147, 214).
This completes the proof that G(s) attains its minimum in [ 1
p, 1] at s1 for p = 3, 5, 7; consequently
βp = G(s1) which yields the values β3, β5, β7 in (1.8) and (1.10) and proves Theorem 1.1 (and
Wilson’s conjecture) for these p.
 14

Figure 2: Graphical rendering of Qs1(t) (in blue) and Es1,1(t) (in red) for p = 3, 5, 7.

Figure 3: A closer look at the fluctuations of G in the smaller interval [ 1
p, 2
p] for p = 3, 5, 7.

5 Proof of Theorem 1.1 for p ⩾ 11

When p ⩾ 11, we take M = 2, k = 0 and µ = ˆsp(ξ, η) = 2ξ+1
2p − η
p2 in Theorem 3.3, so that
a1 = ξ, a2 = p−1
2 − η (recall (1.12) and (3.11)). Then (3.13) yields

τ2 = (ξ + 1)(p + 1 − 2η)
2A2 , (5.1)

and φ(µ) is given in (4.2). Thus (3.19) and (3.21) yield

p2(Qµ(t) − Eµ,0(t))
ρpφ(µ) = C(t) (
φ(t) − φ (1
2
)) − (
t − 1
2
) , (5.2)

where
 C(t) := τ2
ρpφ(µ)
 (
p2µ − ρp
 (
t − 1
2
)) . (5.3)

5.1 p = 11, 13, 17, 19, 23: (ξ, η) = (1, 1)

For p = 11, s1 = 3
22 = 0.13636 . . . is no longer the minimum point of G; see Figures 4 and 5.
In this case, Wilson [16] conjectured (in an equivalent form) that the minimum occurs at s2 :=

15

Qs1(t) vs Es1,0 Qs2(t) vs Es2,0(t)

Figure 4: p = 11: Qsi(t) (in blue) and Esi,0 (in red) for i = 1, 2.

s1 − 1
p2 = 0.12809 . . . , which yields his conjecture for β11 in (1.10); see Lemma 4.1. (In base 11,
s2 = 0.14555 . . . .) Numerically, we have G(s1) = 0.7386 . . . and G(s2) = 0.7364 . . ..
To verify his conjecture, we apply Theorem 3.3 with M = 2, k = 0 and (ξ, η) = (1, 1); thus
µ = s2 = 3
2p − 1
p2 , which gives a1 = 1, a2 = p−3
2 , and then by (3.19)

Qs2(t) = (p − 1)s2
A2
 (
φ(t) − φ (1
2
)) − ρp
p2 φ(s2) (
t − 1
2
) , (5.4)

and by (3.21)
 Es2,0(t) = (p − 1)ρp
pk+2A2
 (
φ(t) − φ (1
2
)) (t − 1
2
) ; (5.5)

see Figure 4 for an illustration of the different effects for Qµ(t) and Eµ,k(t) between s1 and s2.
The same numerical recipes used in the previous section for p = 3, 5, 7 applies here with
(N1, N2) = (40, 148), which shows that (3.20) holds for µ = s2 and k = 0, but not for µ = s1.
Thus, Theorem 3.3 guarantees that G(s2) is the minimum of G in the interval I2 = [ 15
112 , 16
112 ]. The
same bounding techniques with (N3, N4) = (32, 236) also shows (see Figure 5) that G(s) > G(s2)
outside [ 15
112 , 16
112 ]. Thus, G(s2) is the minimum, and β11 = G(s2) (see (1.10)).
Similarly, the same procedure applies to p = 13, 17, 19, 23 with

p (N1, N2, N3, N4)
13 (62, 131, 53, 373)
17 (135, 132, 134, 331)
19 (211, 144, 257, 1517)
23 (611, 151, 992, 6812)

for which G also attains its minimum βp at s2; see Figures 6 and 7.
This proves Theorem 1.1 for 11 ⩽ p ⩽ 23. Using Lemma 4.1, we obtain the values of βp:

16

Figure 5: p = 11: G(x) for x ∈ [ 1
11 , 1
] (left) and [ 14
112 , 17
112 ] (right), respectively.

p 13 17 19 23

βp 124
91
 (26
37
)ρ13 71
51
(34
49
 )ρ17 533
380
 (38
55
 )ρ19 261
184
 (46
67
 )ρ23

5.2 p = 29: (ξ, η) = (2, 1)

For p = 29, s2 = ˆsp(1, 1) = 3
2p − 1
p2 is no longer the global minimum point of G(s). Instead
ˆsp(1, 2) = 3
2p − 2
p2 gives a smaller value of G(s), and an even smaller value of G is reached at
s3 := ˆsp(2, 1) = 5
2p − 1
p2 , which can be proved to be the minimum point by Theorem 3.3 with the
same numerical recipes used above.
When it comes to numerical check, a direct use of the preceding numerical recipes gives the
(minimum) numbers of partitions required in each of the intervals [0, 1
2 − 1
2p], [ 1
2 + 1
2p, 1], [ 1
p, 5
2p − 3
2p2 ]
and [ 5
2p − 1
2p2 ]: (N1, N2, N3, N4) = (3011, 216, 14996, 11942), respectively, which are somewhat
too large. We used above subintervals of the same length, but this is not optimal, and the computa-
tional complexity can be reduced by the following procedure: instead of fixing first the interval and
then finding a large enough number of subintervals (of equal length) such that the monotonicity
inequality holds in each of the subintervals, we fix first N, the number of subintervals to be pro-
cessed in each step, and then check either from the left end or the right end of the interval how far
towards the other end of the interval we can go with N subintervals of the same size such that the
monotonicity inequality holds in all subintervals. Then repeat the same procedure until reaching
the other end of the interval. Alternatively, a binary splitting technique of the target interval can be
used to identify a range where N partitions suffice.
For example, to check if Qs3(t) > Es3,0(t) holds in the interval [0, 1
2 − 1
2p], we choose, say
N = p2 = 841, which then suffices if we partition first [0, 1
2 − 1
2p] into the two subintervals [0, 1
2 − 4
p]
and [ 1
2 − 4
p, 1
2 − 1
2p], and then further partition each into N + 1 smaller subintervals before checking
the monotonicity inequality. Similarly, instead of using N3 = 14996 for the interval [ 1
p, 5
2p − 3
2p2 ],
we choose again N = p2 and split first this interval into [ 1
p, 3
p2 ] and [ 5
2p − 3
p2 , 5
2p − 3
2p2 ] before the

17

Figure 6: A graphical rendering of G(s) for p = 13, 17, 19.

numerical check in both subintervals. Finally, the use of the number N4 = 11942 for the interval
[ 5
2p − 1
2p2 , 1] can be replaced by taking N = p2 and splitting [ 5
2p − 1
2p2 , 1] into [ 5
2p − 1
2p2 , 4
p] and
[ 4
p, 1].

5.3 Primes from 31 to 113: ξ = 2

Exactly the same method of proof used above applies to higher values of p with the minimum
point of G in [ 1
p, 1] given in (1.14). The two-stage partitioning procedure is computationally more
efficient. For example, when p = 113, we have:

variable Interval first
partition
 split each
into N subintervals
(equal spacing)

t [0, 1
2 − 1
2p] [0, 1
2 − 3
p] ∪ [ 1
2 − 3
p, 1
2 − 1
2p] N = 500

[ 1
2 + 1
2p, 1] [ 1
2 + 1
2p, 1
2 + 7
2p] ∪ [ 1
2 + 1
2p, 1] N = 700

s [ 1
p, 5
2p − 11
2p2 ] [ 1
p, 5
2p − 11
p2 ] ∪ [ 5
2p − 11
p2 , 5
2p − 11
2p2 ] N = 500

[ 5
2p − 9
2p2 , 1] [ 5
2p − 9
2p2 , 5
2p] ∪ [ 5
2p, 5
p] ∪ [ 5
p, 1] N = 5000

6 p ⩾ 127

In this section, we discuss briefly the extension of our approach to larger primes.

6.1 p = 127, . . . , 2221

The same approach used so far is readily extended to primes of larger values. As far as our nu-
merical check was conducted, the minimum G(s) is always reached at s = ˆsp = 2ξ+1
2p − η
p2 for
a suitable choice of (ξ, η); consequently, then βp is given by (1.13). In general, the first-stage
partition can be chosen by standard binary search. The following table shows the choices of (ξ, η)
for p ⩽ 2221.
 18

Figure 7: Qs2(t) (in blue) vs Es2,0(t) (in red) for p = 13, 17, 19.

We list the partitions used in our numerical check for p = 127, p = 491 and p = 1993 for
which ξ jumps from i to i + 1, and the minimum of G is attained with the choices (ξ, η) = (3, 5),
(4, 15) and (5, 49), respectively. For simplicity, we use the notation [a, b] = [x0, x1, . . . , xd] to
mean the union ∪d
i=1[xi−1, xi] with x0 = a and xd = b.

p = 127: (ξ, η) = (3, 5)

variable Interval first
partition
 split each
into N subintervals
(equal spacing)

t [0, 1
2 − 1
2p] [0, 1
2 − 4
p, 1
2 − 1
2p] N = 500

[ 1
2 + 1
2p, 1] [ 1
2 + 1
2p, 1
2 + 9
2p, 1] N = 500

s [ 1
p, 7
2p − 11
2p2 ] [ 1
p, 2.3
p , 3.4
p , 7
2p − 11
2p2 ] N = 1000

[ 7
2p − 9
2p2 , 1] [ 7
2p − 9
2p2 , 3.51
p , 6
p, 1] N = 1200

19

3–7 11–23 29 31–53 59–79 83–107

(1, 0) (1, 1) (2, 1) (2, 2) (2, 3) (2, 4)

109–113 127–139 149–173 179–199 211–241 251–277

(2, 5) (3, 5) (3, 6) (3, 7) (3, 8) (3, 9)

281–311 313–347 349–383 389–419 421–449 457–487

(3, 10) (3, 11) (3, 12) (3, 13) (3, 14) (3, 15)

491–509 521–547 557–587 593–619 631–661 673–701

(4, 15) (4, 16) (4, 17) (4, 18) (4, 19) (4, 20)

709–743 751–787 797–829 839–863 877–911 919–953

(4, 21) (4, 22) (4, 23) (4, 24) (4, 25) (4, 26)

967–991 997–1033 1039–1069 1087–1117 1123–1163 1171–1201

(4, 27) (4, 28) (4, 29) (4, 30) (4, 31) (4, 32)

1213–1249 1259–1291 1297–1327 1361–1373 1381–1423 1427–1459

(4, 33) (4, 34) (4, 35) (4, 36) (4, 37) (4, 38)

1471–1511 1523–1553 1559–1597 1601–1637 1657–1669 1693–1723

(4, 39) (4, 40) (4, 41) (4, 42) (4, 43) (4, 44)

1733–1777 1783–1811 1823–1867 1871–1907 1913–1951 1973–1987

(4, 45) (4, 46) (4, 47) (4, 48) (4, 49) (4, 50)

1993–2003 2011–2039 2053–2089 2099–2141 2143–2179 2203–2221

(5, 49) (5, 50) (5, 51) (5, 52) (5, 53) (5, 54)

Table 1: The optimal pair (ξ, η) at which G(s) reaches its minimum at s = 2ξ+1
2p − η
p2 for odd
primes p = 3, . . . , 2221.
 p = 491: (ξ, η) = (4, 15)

variable Interval first
partition
 split each
into N subintervals
(equal spacing)

t [0, 1
2 − 1
2p] [0, 0.46, 1
2 − 5
2p, 1
2 − 1
2p] N = 1000

[ 1
2 + 1
2p, 1] [ 1
2 + 1
2p, 1
2 + 2.1
p , 0.53, 1] N = 1000

s [ 1
p, 4.5
p − 15.5
p2 ] [ 1
p, 3.4
p , 3.5
p , 4.45
p , 4.5
p − 15.5
p2 ] N = 5000

[ 4.5
p − 14.5
p2 , 1] [ 4.5
p − 14.5
p2 , 4.5
p − 6
p2 , 5
p, 8
p, 1] N = 500020

p = 1993: (ξ, η) = (5, 49)

variable Interval first
partition
 split each
into N subintervals
(equal spacing)

t [0, 1
2 − 1
2p] [0, 0.485, 0.498, 0.4994, 1
2 − 1
2p] N = 4000

[ 1
2 + 1
2p, 1] [ 1
2 + 1
2p, 0.501, 0.504, 0.515, 1] N = 3000

s [ 1
p, 5.5
p − 49.5
p2 ] [ 1
p, 4.45
p , 4.5
p , 5.46
p , 5.474
p , 5.5
p − 49.5
p2 ] N = 12000

[ 5.5
p − 48.5
p2 , 1] [ 5.5
p − 48.5
p2 , 5.5
p − 41
p2 , 5.6
p , 15
p , 1] N = 10000

6.2 Large p asymptotics

Assuming that G reaches its minimum at s = ˆsp(ξ, η) for some (ξ, η), so that the minimum value
βp is given by (1.13), we give here some simple, not completely rigorous, estimates of the two
parameters (ξ, η) and the minimum point ˆsp for a given large p. We note first that

ρp = log( 1
2 p(p + 1))
log p = 2 + log(1 + 1
p) − log 2

log p = 2 − 1
log2 p + O
( 1
p log p
 )
. (6.1)

We see from Table 1 in Section 6.1 that ξ and η both seem to grow as p grows (although not
monotonically in case of η). In fact, it is easy to see that at least ξ + η must tend to infinity, because
otherwise there would be an infinite subsequence with some fixed values of ξ and η, but then it
would follow from (1.13) that as p → ∞ along this subsequence, using ρp → 2 from (6.1),

βp = Bξ,η → ξ + 1
2ξ + 1 > 1
2, (6.2)

which contradicts (1.9).
We obtain more precise estimates by regarding ξ and η as continuous variables in (1.13) and
setting the partial derivatives of (1.13) with respect to ξ and η equal to 0. This yields the equations:




 (4ξ + 3)p2 + (4ξ − 4η + 3)p + 2η(2η − 1)
(ξ + 1)(2ξ + 1)p2 + (ξ + 1)(2ξ − 4η + 1)p + 2η(ξ + 1)(2η − 1) − 2ρpp
(2ξ + 1)p − 2η = 0,

ρp
(2ξ + 1)p − 2η − 2p − 4η + 1
(2ξ + 1)p2 + (2ξ − 4η + 1)p + 2η(2η − 1) = 0.
 (6.3)

The positive solution pair, say (ξ+, η+), already gives a very good approximation to the true values
of (ξ, η). Empirically, (⌊ξ+ + 0.5⌋, ⌊η+ + 0.45⌋) is identical to the true pair (ξ, η) at which G
attains the minimum for primes p from 11 to 79, and differs by at most 1 (at either ξ or η but
not both) for primes up to 7907. For p as large as p = 1, 000, 003, such a solution pair gives
(9, 13206), while the true minimum of G is reached at (ξ, η) = (9, 13203).

21

For large p, we may approximate the equations (6.3) by ignoring all terms that are O( 1
p) or
O( η
pξ) times the leading terms in the various numerators and denominators. (We assume that η
pξ
is small.) This gives the equations, using the notation ∆ := 1
p + η
pξ,

4ξ + 3
(ξ + 1)(2ξ + 1) = 2ρp
2ξ + 1
(
1 + O(∆))
, (6.4a)

ρp
2ξ + 1 = 2 − 4
pη

2ξ + 1
 (
1 + O(∆))
. (6.4b)

If we further define δp := 2 − ρp ∼ 1
log2 p (see (6.1)), then (6.4a) yields

(4 − 2δp)(ξ + 1) = 2ρp(ξ + 1) = (4ξ + 3)(
1 + O(∆)) = 4ξ + 3 + O(ξ∆). (6.5)

Assuming ξ, η = o(p), we have ξ∆ = ξ+η
p = o(1) and then (6.5) yields 2δpξ = 1 + o(1) and
finally, using (6.1),
 ξ ∼ 1
2δp ∼ log2 p
2 = log4 p. (6.6)

Similarly, (6.4b) yields
 2 − 4η
p = ρp + O(∆) = 2 − δp + O(∆) (6.7)

leading to the empirical approximation for η:

η ∼ 1
4pδp ∼ p
4 log2 p . (6.8)

The values (6.6) and (6.8) yield by (1.11) the estimate for the minimum point

ˆsp ∼ ξ
p ∼ log4 p
p . (6.9)

Finally, observe that if
 x = ∑

j⩾1 bjp−j = (0.b1b2 . . . )p, (6.10)

then b1 = ⌊px⌋, and

bm = ⌊pmx⌋ − p⌊pm−1x⌋ = p{pm−1x} − {pmx} (m ⩾ 2). (6.11)

Thus

φ(x) = 1
2
 ∑

j⩾1
 ⌊pjx⌋ − p⌊pj−1x⌋
Aj ∏

1⩽i⩽j
 (
1 + ⌊pix⌋ − p⌊pi−1x⌋
)

= 1 + ⌊px⌋
2
 ( ⌊px⌋
A + ∑

j⩾2
 p{pj−1x} − {pjx}
Aj ∏

2⩽i⩽j
 (
1 + p{pi−1x} − {pix})
)
 (6.12)

22

For large p, each term in the sum on the right-hand side is asymptotic to

2j−1

pj−1 x{px} · · · {pj−2x}{pj−1x}
2 (
1 + O (
p−1)) , (6.13)

for j ⩾ 2, and for j = 1:

⌊px⌋(⌊px⌋ + 1)
p(p + 1) = x
2 + x(1 − x − 2{px})
p + O (
p−2) . (6.14)

We then obtain
 φ(x) = x
2 + x(1 − x − 2{px} + 2{px}2)
p + O
(
p−2)
. (6.15)

Then
 G(x) = x
2−ρp + x
1−ρp(1 − x − 2{px} + 2{px}2)
p + · · · , (6.16)

where the piecewise differentiability of the terms on the right-hand side might be useful in further
identifying the true minimum of G for large p.

A The p-ary recurrence

In this appendix we study a more general recurrence, using the methods of [7] and [8] where binary
recurrences are studied; see also Section 7.1 in the earlier version of [8] on arXiv.
Let p be any integer larger than 1. Consider the recurrence

f(n) = ∑

0⩽j<p γjf (⌊n + j
p
 ⌋) for n ⩾ p, (A.1)

with given coefficients γ0, . . . , γp−1 and given initial values f(1), . . . , f(p − 1) . We assume for
simplicity that γ0, . . . , γp−1 > 0. Let
 A := ∑

0⩽j<p γj. (A.2)

Lemma A.1. Let γ0, . . . , γp−1 > 0. Then there exists a unique strictly increasing continuous
function φ on [0, 1] such that φ(0) = 0, φ(1) = 1 and for j = 0, 1, . . . , p − 1,

φ(t) = γp−j−1
A φ(pt − j) +
 ∑
p−j⩽i<p γi
A if j
p ⩽ t ⩽ j + 1
p . (A.3)

Moreover, we have the explicit formula

φ
 (∑

j⩾1 bjp−j)
 = ∑

j⩾1 A−j
 

 ∑

p−bj⩽i<p γi



 ( ∏

1⩽i<j γp−1−bi
)
 , (A.4)

when bj ∈ {0, 1, 2, . . . , p − 1} for j ⩾ 1.
 23

Proof. Define φ0(t) := t for t ∈ [0, 1], and recursively let

φk+1(t) := γp−j−1
A φk(pt − j) +
 ∑
p−j⩽i<p γi
A if j
p ⩽ t ⩽ j + 1
p , (A.5)

for j = 0, 1, . . . , p − 1. (Thus φk+1 consists of p suitably scaled copies of φk.) Observe first that
φk(0) = 0 and φk(1) = 1 by induction. Note also that if t0 = j0
p for j0 ∈ {1, . . . , p − 1}, then the
definition (A.5) can be applied with both j = j0 − 1 and j = j0. The first choice gives

φk+1 (t0) = γp−j0
A φk(1) +
 ∑
p−j0+1⩽i<p γi
A =
 ∑
p−j0⩽i<p γi
A , (A.6)

and the second one gives

φk+1 (t0) = γp−j0−1
A φk(0) +
 ∑
p−j0⩽i<p γi
A =
 ∑
p−j0⩽i<p γi
A . (A.7)

Since these are equal, the definition (A.5) is consistent. It is now obvious by induction that φk is
continuous and strictly increasing.
We claim that

|φk+1(t) − φk(t)| ⩽ (max0⩽j<p γj
A
 )k for all k ⩾ 0 and t ∈ [0, 1]. (A.8)

We prove this by induction. The case k = 0 is clear, since |φ1(t) − φ0(t)| ⩽ 1. Assume now that
(A.8) holds for k − 1. If j
p ⩽ t ⩽ j+1
p then

|φk+1(t) − φk(t)| = γp−j−1
A |φk(pt − j) − φk−1(pt − j)|

⩽ γp−j−1
A
 (max0⩽j<p γj
A
 )k−1

⩽ (max0⩽j<p γj
A
 )k . (A.9)

Thus, (A.8) holds, and since max0⩽j<p γj/A < 1, it follows that the sequence φk converges
uniformly to a function φ : [0, 1] → [0, 1]. By (A.5), φ satisfies (A.3). Since each φk is continuous
and strictly increasing, the limiting function φ is continuous and non-decreasing.
We next prove by induction that

φN
 ( ∑

1⩽j⩽N bjp−j)
 = ∑

1⩽j⩽N A−j
 

 ∑

p−bj⩽i<p γi



 ( ∏

1⩽i<j γp−1−bi
)
 , (A.10)

for any N ⩾ 0, where bj ∈ {0, 1, 2, . . . , p − 1}. This is trivial for N = 0. Suppose that (A.10) holds

24

for N. Let t = ∑
1⩽j⩽N+1 bjp−j, where bj ∈ {0, 1, 2, . . . , p − 1}. Then, by (A.5),

φN+1(t) = γp−b1−1
A φN (pt − b1) +
 ∑
p−b1⩽i<p γi
A

= γp−b1−1
A
 

 ∑

1⩽j⩽N A−j
 

 ∑

p−bj+1⩽i<p γi



 ( ∏

1⩽i<j γp−1−bi+1
)

 +
 ∑
p−b1⩽i<p γi
A

= ∑

2⩽j⩽N+1 A−j
 

 ∑

p−bj⩽i<p γi



 ( ∏

1⩽i<j γp−1−bi
)
 +
 ∑
p−b1⩽i<p γi
A

= ∑

1⩽j⩽N+1 A−j
 

 ∑

p−bj⩽i<p γi



 ( ∏

1⩽i<j γp−1−bi
)
 . (A.11)

Hence (A.10) holds for N + 1, and thus it holds in general by induction.
For any p-adic rational t = ∑
1⩽j⩽M bjp−j, let bj := 0 for j > M and apply (A.10) with
N ⩾ M. Letting N → ∞, we see that (A.4) holds for t. Since we have shown that φ is continuous,
it follows that (A.4) holds in general, for any ∑
1⩽j<∞ bjp−j. Furthermore, it follows from (A.10)
that for every N ⩾ M, we have φN(t) = φM(t). (A.12)

Thus φ(t) = limN→∞ φN(t) = φM(t). Accordingly,

φ(t) = φN(t) < φN(t + p−N) = φ(t + p−N). (A.13)

This shows that φ is strictly increasing on p-adic rationals. In general, for 0 ⩽ s1 < s2 ⩽ 1, there
exist p-adic rationals t1 and t2 such that s1 ⩽ t1 < t2 ⩽ s2. Then

φ(s1) ⩽ φ(t1) < φ(t2) ⩽ φ(s2). (A.14)

Consequently, φ is strictly increasing.

We next extend f(n) to a function of a real variable x ⩾ 1 by

f(n + t) := (1 − φ(t))f(n) + φ(t)f(n + 1) (A.15)

for n ⩾ 1 and 0 ⩽ t ⩽ 1.

Lemma A.2. Assume that the recurrence (A.1) holds. Then

f(x) = Af ( x
p
 ) for all real x ⩾ p. (A.16)

Proof. Define A−
k := ∑

0⩽i<k γi and A+
k := ∑

k⩽i<p γi. (A.17)

25

Rewrite (A.1) as f(pn + j) = A−
p−jf(n) + A+
p−jf(n + 1) (A.18)

for n ⩾ 1 and j = 0, 1, . . . , p − 1; note that for j = 0 (A.18) is f(pn) = Af(n), and it follows that
(A.18) holds for j = p too. Also rewrite (A.3) as

γp−1−jφ(pt) = Aφ ( j
p + t) − A+
p−j (A.19)

for 0 ⩽ t ⩽ 1
p and j = 0, 1, . . . , p − 1.
Now, for x ⩾ p, write x = pn + j + pt, (A.20)

where
 n = ⌊ x
p
 ⌋ , j = ⌊x⌋ mod p, t = {x}
p . (A.21)

Then, by (A.15), (A.18) and (A.19),

f(x) = f(pn + j + pt)
= (1 − φ(pt))f(pn + j) + φ(pt)f(pn + j + 1)

= (1 − φ(pt)) (
A−
p−jf(n) + A+
p−jf(n + 1)) (A.22)

+ φ(pt) (
A−
p−j−1f(n) + A+
p−j−1f(n + 1))

= (
A−
p−jf(n) + A+
p−jf(n + 1)) − φ(pt)γp−j−1 (f(n) − f(n + 1))

= (
A−
p−jf(n) + A+
p−jf(n + 1)) − (
Aφ ( j
p + t) − A+
p−j
) (f(n) − f(n + 1))

= Af(n) − Aφ ( j
p + t) f(n) + Aφ ( j
p + t) f(n + 1)

= A ((
1 − φ ( j
p + t)) f(n) + φ ( j
p + t) f(n + 1))

= Af (
n + j
p + t)

= Af ( x
p
 ) , (A.23)

which proves (A.16).

Theorem A.3. Assume that the recurrence (A.1) holds, with γ0, . . . , γp−1 > 0. Then

f(n) = n
ρP (
logp n
) for all n ⩾ 1, (A.24)

where ρ := logp A and P(t) := A−{t}f(p{t}) (A.25)

is a continuous 1-periodic function.
 26

Moreover, if the initial values satisfy

f(j) = ∑

p−j⩽i<p γi for j = 1, . . . , p − 1 (A.26)

then P(t) = A1−{t}φ(p{t}−1), (A.27)

where φ is defined in Lemma A.1.

Proof. Since f(x) is continuous, P(t) is continuous on [0, 1), and by (A.16)

lim
t↗1 P(t) = A−1f(p) = f(1) = P(0) = P(1), (A.28)

which shows that P(t) is a continuous 1-periodic function. For y ∈ [1, p)

f(y) = f(plogp y) = Alogp y (
A− logp yf(plogp y)) = Alogp yP (
logp y) , (A.29)

and, for each x ⩾ 1, p−⌊logp x⌋x ∈ [1, p). (A.30)

By applying Lemma A.2 repeatedly ⌊logp x⌋ times:

f(x) = A⌊logp x⌋f (
p−⌊logp x⌋x
)

= A⌊logp x⌋+logp(p
−⌊logp x⌋x)P (
logp (
p−⌊logp x⌋x
))

= Alogp xP (
logp x
) .
 (A.31)

Thus we get
 f(n) = Alogp nP (
logp n
) = pρ logp nP (
logp n
) = n
ρP (
logp n
) , (A.32)

proving (A.24).
Finally, suppose that condition (A.26) holds. For 1 ⩽ x < p, let j = ⌊x⌋. Then, using (A.15)
and (A.3), f(x) = f(j) + φ(x − j) (f(j + 1) − f(j))

= ∑

p−j⩽i<p γi + φ(x − j)γp−j−1

= A (γp−j−1
A φ(x − j) +
 ∑
p−j⩽i<p γi
A
 )

= Aφ ( x
p
 ) . (A.33)

Thus we have P(t) = A−{t}f(p{t}) = A1−{t}φ(p{t}−1). (A.34)

27

Corollary A.4. Assume that the recurrence (A.1) holds, with γ0, . . . , γp−1 > 0. Then

sup
n⩾1
 f(n)
nρ = lim sup
n→∞ f(n)
nρ = max
t∈[0,1] P(t), (A.35)

inf
n⩾1 f(n)
nρ = lim inf
n→∞ f(n)
nρ = min
t∈[0,1] P(t). (A.36)

Proof. By (A.24), since P(t) is a continuous 1-periodic function.

Remark A.5. In the case that γp−1 = 1, the condition (A.26) on the initial values is equivalent to
assuming that the recurrence (A.1) extends to all n ⩾ 2, with f(0) = 0 and f(1) = 1. △

References

[1] Chen, Y.-G. and Ji, C. (1998), The number of multinomial coefficients not divided by a prime.
Acta Sci. Math. (Szeged) 64(1-2), 37–48.

[2] Chen, Y. G. and Ji, C. G. (2002), On a function related to multinomial coefficients. I. Acta
Math. Sin. (Engl. Ser.) 18(4), 647–660.

[3] Fine, N. J. (1947), Binomial coefficients modulo a prime. Amer. Math. Monthly 54, 589–592.

[4] Franco, Z. M. (1998), Distribution of binomial coefficients modulo three. Fibonacci Quart.
36(3), 272–275.

[5] Harborth, H. (1977), Number of odd binomial coefficients. Proc. Amer. Math. Soc. 62, 19–22.

[6] Howard, F. T. (1974), The number of multinomial coefficients divisible by a fixed power of a
prime, Pacific J. Math. 50, 99–108.

[7] Hwang, H.-K., Janson, S., and Tsai, T.-H. (2017), Exact and asymptotic solutions of a divide-
and-conquer recurrence dividing at half: theory and applications. ACM Trans. Algorithms
13(4), Art. 47, 43 pp.

[8] Hwang, H.-K., Janson, S., and Tsai, T.-H. (2024), Identities and periodic oscillations of
divide-and-conquer recurrences splitting at half. Adv. in Appl. Math. 155, Paper No. 102653,
53 pp.

[9] OEIS Foundation Inc., The On-Line Encyclopedia of Integer Sequences (OEIS). Available
electronically at http://oeis.org.

[10] Stein, A. H. (1989), Binomial coefficients not divisible by a prime. Lecture Notes in Mathe-
matics 1383, pp. 170–177, Springer-Verlag,

[11] Stolarsky, K. B. (1977), Power and exponential sums of digital sums related to binomial
coefficient parity, SIAM J. Appl. Math. 32, 717–730.

28

[12] Volodin, N. A. (1989), Distribution of polynomial coefficients congruent modulo pN, Math.
Notes 45, 195–99.

[13] Volodin, N. A. (1994), Number of multinomial coefficients not divisible by a prime, Fi-
bonacci Quart. 32, 402–406.

[14] Volodin, N. A. (1999), Multinomial coefficients modulo a prime. Proc. Amer. Math. Soc.
127(2), 349–353.

[15] Wilson, B. (1996), LIM INF bounds for multinomial coefficients modulo a prime, Preprint,
SUNY College at Brockport, New York, 16 pp.

[16] Wilson, B. (1998), Asymptotic behavior of Pascal’s triangle modulo a prime. Acta Arith.
83(2), 105–116.
 29
