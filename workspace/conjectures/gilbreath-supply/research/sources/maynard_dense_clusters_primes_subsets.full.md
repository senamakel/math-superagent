<!-- source: https://arxiv.org/pdf/1405.2593 | converted from PDF -->

arXiv:1405.2593v2  [math.NT]  16 Dec 2014
DENSE CLUSTERS OF PRIMES IN SUBSETS

JAMES MAYNARD

Abstract. We prove a generalization of the author's work to show that a ny subset of the
primes which is `well-distributed' in arithmetic progress ions contains many primes which
are close together. Moreover, our bounds hold with some uniformity in the parameters. As
applications, we show there are inﬁnitely many intervals of length (log x)ǫ containing ≫ǫ
log log x primes, and show lower bounds of the correct order of magnitude for the number of
strings of m congruent primes with pn+m − pn ≤ ǫ log x.

1. Introduction

Let L = {L1, . . . , Lk} be a set of distinct linear functions Li(n) = ain + bi (1 ≤ i ≤ k) with
coeﬃcients in the positive integers. We say such a set is admissible if ∏k
i=1 Li(n) has no ﬁxed
prime divisor (that is, for every prime p there is an integer np such that ∏k
i=1 Li(np) is coprime
to p). Dickson made the following conjecture.

Conjecture (Prime k-tuples conjecture). Let L = {L1, . . . , Lk} be admissible. Then there are
inﬁnitely many integers n such that all Li(n) (1 ≤ i ≤ k) are prime.

Although such a conjecture appears well beyond the current techniques, recent progress (
[20], [13], and unpublished work of Tao) has enabled us to prove weak forms of this conjec-
ture, where instead we show that there are inﬁnitely many integers n such that several (rather
than all) of the Li(n) are primes.
As noted in [13], the method of Maynard and Tao can also prove such weak versions
of Dickson's conjecture in various more general settings. T his has been demonstrated in
the recent work [18], [3], [1], [16], [12]. In this paper we consider generalized versions of
Dickson's conjecture, and prove corresponding weak versio ns of them.
Based on heuristics from the Hardy-Littlewood circle method, it has been conjectured that
the number of n ≤ x such that all the Li(n) are prime should have an asymptotic formula
(S(L) + o(1))x/(log x)
k, where S(L) is a constant depending only on L (with S(L) > 0 iﬀ L
is admissible). Moreover, these heuristics would suggest that the formulae should hold even
if we allow the coeﬃcients ai, bi and the number k of functions in L to vary slightly with x.
One can also speculate that Dickson's conjecture might hold for more general sets, where
we ask for inﬁnitely many integers n ∈ A such that all of Li(n) are primes in P, for some
`nice' sets of integers A and of primes P, and provided L satisﬁes some simple properties
in terms of A and P. For example, Schinzel's Hypothesis H would imply this if ei ther A or
P are restricted to the values given by an irreducible polynomial, and a uniform version of
Dickson's conjecture would give this if A or P were restricted to the union of short intervals.
The aim of this paper is to show that the ﬂexibility of the method introduced in [13] allows
us to prove weak analogues of these generalizations of Dickson's conjecture. In particular, if
A and P ∩ L(A) are well-distributed in arithmetic progressions, then we can obtain a lower
bound close to the expected truth for the number of n ∈ A, n ≤ x such that several of the Li(n)
are primes in P, and we can show this estimate holds with some uniformity in the size of ai, bi
and k. 1

2 JAMES MAYNARD

2. Well-distributed sets

Given a set of integers A, a set of primes P, and a linear function L(n) = l1n + l2, we deﬁne

A(x) = {n ∈ A : x ≤ n < 2x}, A(x; q, a) = {n ∈ A(x), n ≡ a (mod q)},
L(A) = {L(n) : n ∈ A}, ϕL(q) = ϕ(|l1|q)/ϕ(|l1|),(2.1) PL,A(x) = L(A(x)) ∩ P, PL,A(x; q, a) = L(A(x; q, a)) ∩ P.

This paper will focus on sets which satisfy the following hypothesis, which is given in terms
of (A, L, P, B, x, θ) for L an admissible set of linear functions, B ∈ N, x a large real number,
and 0 < θ < 1.

Hypothesis 1. (A, L, P, B, x, θ). Let k = #L.
(1) A is well-distributed in arithmetic progressions: We have
∑

q≤xθ max
a
 ∣∣∣∣#A(x; q, a) − #A(x)
q
 ∣∣∣∣ ≪ #A(x)
(log x)100k2 .

(2) Primes in L(A) ∩ P are well-distributed in most arithmetic progressions: For any
L ∈ L we have
∑

q≤xθ
(q,B)=1
 max
(L(a),q)=1
∣∣∣∣#PL,A(x; q, a) − #PL,A(x)
ϕL(q)
 ∣∣∣∣ ≪ #PL,A(x)
(log x)100k2 .

(3) A is not too concentrated in any arithmetic progression: For any q < x
θ we have

#A(x; q, a) ≪ #A(x)
q .

We expect to be able to show this Hypothesis holds (for all large x, some ﬁxed θ > 0 and
some B < x
O(1) with few prime factors) for sets A, P where we can establish `Siegel-Walﬁsz'
type asymptotics for arithmetic progressions to small moduli, and a large sieve estimate to
handle larger moduli.
We note that the recent work of Benatar [2] showed the existence of small gaps between
primes for sets which satisfy similar properties to those considered here.

3. Main Results

Theorem 3.1. Let α > 0 and 0 < θ < 1. Let A be a set of integers, P a set of primes,
L = {L1, . . . , Lk} an admissible set of k linear functions, and B, x integers. Let the coeﬃcients
Li(n) = ain + bi ∈ L satisfy 1 ≤ ai, bi ≤ x
α for all 1 ≤ i ≤ k, and let k ≤ (log x)
α and
1 ≤ B ≤ x
α.
There is a constant C depending only on α and θ such that the following holds. If k ≥ C
and (A, L, P, B, x, θ) satisfy Hypothesis 1, and if δ > (log k)
−1 is such that
1
k ϕ(B)
B
 ∑

L∈L
 ϕ(ai)
ai #PL,A(x) ≥ δ#A(x)
log x ,

then #{n ∈ A(x) : #({L1(n), . . . , Lk(n)} ∩ P) ≥ C−1δ log k} ≫ #A(x)
(log x)k exp(Ck) .

Moreover, if P = P, k ≤ (log x)
1/5 and all L ∈ L have the form an + bi with |bi| ≤ (log x)k−2

and a ≪ 1, then the primes counted above can be restricted to be consecutive, at the cost of
replacing exp(Ck) with exp(Ck5) in the bound.

DENSE CLUSTERS OF PRIMES IN SUBSETS 3

All implied constants in Theorem 3.1 are eﬀectively computable if the implied constants in
Hypothesis 1 for (A, L, P, B, x, θ) are.
We note that Theorem 3.1 can show that several of the Li(n) are primes for sets A, P where
it is not the case that there are inﬁnitely many n ∈ A such that all of the Li(n) are primes in
P. For example, if P = {p2n : n ∈ N} is the set of primes of even index and A = N, then we
would expect P to be equidistributed in the sense of Hypothesis 1. However, there are clearly
no integers n such that n, n + 2 ∈ P, and so the analogue of the twin prime conjecture does not
hold in this case. Similarly if P is restricted to the union of arithmetic progressions in short
intervals1. Therefore without extra assumptions on our sets A, P we cannot hope for a much
stronger statement than several of the Li(n) are primes in P.
We also note that Theorem 3.1 can apply to very sparse sets A, and no density assumptions
are required beyond the estimates of Hypothesis 1. Of course, for such sets the major obstacle
is in establishing Hypothesis 1.
We give some applications of this result.

Theorem 3.2. For any x, y ≥ 1 there are ≫ x exp(− √log x) integers x0 ∈ [x, 2x] such that

π(x0 + y) − π(x0) ≫ log y.

Theorem 3.2 is non-trivial in the region y = o(log x) (and y suﬃciently large), when typi-
cally there are no primes in the interval [x, x + y]. For such values of y, it shows that there are
many intervals of length y containing considerably more than the typical number of primes.
By comparison, a uniform version of the prime k-tuples conjecture would suggest that for
small y there are intervals [x, x + y] containing ≫ y/ log y primes. For large ﬁxed y, we
recover the main result of [13], that lim infn(pn+m − pn) ≪m 1 for all m.

Theorem 3.3. Fix ǫ > 0 and let x > x0(ǫ, q). There is a constant cǫ > 0 (depending only on
ǫ) such that uniformly for m ≤ cǫ log log x, q ≤ (log x)
1−ǫ and (a, q) = 1 we have

#{pn ≤ x : pn ≡ · · · ≡ pn+m ≡ a (mod q), pn+m − pn ≤ ǫ log x} ≫ǫ π(x)
(2q)exp(Cm) .

Here C > 0 is a ﬁxed constant.

Theorem 3.3 extends a result of Shiu [17] which showed the same result but with a lower
bound ≫ x
1−ε(x) for ε(x) ≈ Cqm(log log x)
−1/ϕ(q) in the shorter range m ≪ (log log x)
1/ϕ(q)−ǫ

and without the constraint pn+m − pn ≤ ǫ log x, and a result of Freiberg [5] which showed for
ﬁxed a, q, ǫ inﬁnitely many n such that pn+1 ≡ pn ≡ a (mod q) and pn+1 − pn ≤ ǫ log pn.
We see that for ﬁxed m, q, Theorem 3.3 shows a positive proportion of primes pn are
counted (and so our lower bound is of the correct order of magnitude). In particular, for
a positive proportion of primes pn we have
2 pn ≡ pn+1 ≡ · · · ≡ pn+m ≡ a (mod q) and
pn+m − pn ≤ ǫ log pn. This extends a result of Goldston, Pintz and Yıldırım [7] which showed
a positive proportion of pn have pn+1 − pn ≤ ǫ log pn.

Theorem 3.4. Fix m ∈ N and ǫ > 0. There exists a k = exp(O(m)), such that for x > x0(ǫ, m)
and x
7/12+ǫ ≤ y ≤ x and for any admissible set L = {L1, . . . , Lk} where Li(n) = ain + bi with
1 ≤ ai ≪ (log x)
1/ǫ and 0 ≤ bi ≪ x we have

#{n ∈ [x, x + y] : at least m of Li(n) are prime} ≫ y
(log x)k .

1For example, one could take P = ∪x=2 j ∪i≤x1/4/2 {x + (2i − 1)x3/4 < p ≤ x + 2ix3/4] : n ≡ i (mod 5)}. This set
is equidistributed in the sense of Hypothesis 1, but also has no gaps of size 2.
2This disproves the conjecture #{pn ≤ x : pn ≡ pn+1 ≡ 1 (mod 4)} = o(π(x)) of Knapowski and Tur´an [10].

4 JAMES MAYNARD

Theorem 3.4 relies on a Bombieri-Vinogradov type theorem for primes in intervals of
length x
7/12+ǫ , the best such result being due to Timofeev [19]. By adapting Hypothesis 1
to allow for weighted sums instead of #PL,A(x), we could use presumably the results of [8]
and [11] to extend this to the wider range x
0.525 ≤ y ≤ x.
Theorem 3.4 explicitly demonstrates the claim from [13] that the method also shows the
existence of bounded gaps between primes in short intervals, and for linear functions. We
note that we would expect the lower bound to be of size y/(log x)
m, and so our bound is
smaller that the expected truth by a factor of a ﬁxed power of log x. It appears such a loss is
an unavoidable feature of the method when looking at bounded length intervals.
Our ﬁnal application uses Theorem 3.1 to apply to a subset P of the primes. This extends
the result of Thorner [18] to sets of linear functions, and with an explicit lower bound.

Theorem 3.5. Let K/Q be a Galois extension of Q with discriminant ∆K. There exists a
constant CK depending only on K such that the following holds. Let C ⊆ Gal(K/Q) be a
conjugacy class in the Galois group of K/Q, and let

P = {p prime : p ∤ ∆K, [ K/Q
p
 ] = C}
,

where [ K/Q
· ] denotes the Artin symbol. Let m ∈ N and k = exp (CKm). For any ﬁxed admissible
set L = {L1, . . . , Lk} of k linear functions Li(n) = ain + bi with (ai, ∆K) = 1 for each 1 ≤ i ≤ k,
we have
 #{x ≤ n ≤ 2x : at least m of L1(n), . . . , Lk(n) are in P} ≫ x
(log x)exp(CK m) ,

provided x ≥ x0(K, L).

Thorner gives several arithmetic consequences of ﬁnding such primes of a given splitting
type; we refer the reader to the paper [18] for such applications.
As with Theorem 3.4, we only state the result for ﬁxed m, because it relies on other work
which establishes the Bombieri-Vinogradov type estimates of Hypothesis 1, and these results
only save an arbitrary power of log x. One would presume these results can be extended to
save exp(−c √log x) or similar (having excluded some possible bad moduli), which would
allow uniformity for m ≤ ǫ log log x, but we do not pursue this here. Similarly, the implied
constant in the lower bounds of Theorem 3.4 and Theorem 3.5 is not eﬀective as stated,
but presumably a small modiﬁcation to the underlying results would allow us to obtain an
eﬀective bound.
 4. Notation

We shall view 0 < θ < 1 and α > 0 as ﬁxed real constants. All asymptotic notation such
as O(·), o(·), ≪, ≫ should be interpreted as referring to the limit x → ∞, and any constants
(implied by O(·) or denoted by c, C with subscripts) may depend on θ, α but no other variable,
unless otherwise noted. We will adopt the main assumptions of Theorem 3.1 throughout. In
particular we will view A, P as given sets of integers and primes respectively and k = #L
will be the size of L = {L1, . . . , Lk} an admissible set of integer linear functions, and the
coeﬃcients ai, bi ∈ Z of Li(n) = ain + bi, satisfy |ai|, |bi| ≤ x
α and ai , 0. B ≤ x
α will be an
integer, and x, k will always to be assumed suﬃciently large (in terms of θ, α).
All sums, products and suprema will be assumed to be taken over variables lying in the
natural numbers N = {1, 2, . . . } unless speciﬁed otherwise. The exception to this is when

DENSE CLUSTERS OF PRIMES IN SUBSETS 5

sums or products are over a variable p (or p′), which instead will be assumed to lie in the
prime numbers P = {2, 3, . . . , }.
Throughout the paper, ϕ will denote the Euler totient function, τr(n) the number of ways
of writing n as a product of r natural numbers and µ the Moebius function. We let #A denote
the number of elements of a ﬁnite set A, and 1A(x) the indicator function of A (so 1A(x) = 1
if x ∈ A, and 0 otherwise). We let (a, b) be the greatest common divisor of integers a and b,
and [a, b] the least common multiple of integers a and b. (For real numbers x, y we also use
[x, y] to denote the closed interval. The usage of [·, ·] should be clear from the context.)
To simplify notation we will use vectors in a way which is somewhat non-standard. d will
denote a vector (d1, . . . , dk) ∈ Nk. Given a vector d, when it does not cause confusion, we
write d = ∏k
i=1 di. Given d, e, we will let [d, e] = ∏k
i=1[di, ei] be the product of least common
multiples of the components of d, e, and similarly let (d, e) = ∏k
i=1(di, ei) be the product of
greatest common divisors of the components, and d|e denote the k conditions di|ei for each
1 ≤ i ≤ k. An unlabeled sum ∑d should be interpreted as being over all d ∈ Nk.

5. Outline

The methods of this paper are based on the `GPY method' for det ecting primes. The GPY
method works by considering a weighted sum associated to an admissible set L = {L1, . . . , Lk}

(5.1) S = ∑

x≤n≤2x
( k∑

i=1 1P(Li(n)) − m)
wn,

where m and k are ﬁxed integers, x is a large positive number and wn are some non-negative
weights (typically chosen to be of the form of the weights in Selberg's Λ2 sieve).
If S > 0, then at least one integer n must make a positive contribution to S . Since the
weights wn are non-negative, if n makes a positive contribution then the term in parentheses
in (5.1) must be positive at n, and so at least m + 1 of the Li(n) must be prime. Thus to show
at least m + 1 of the Li(n) are simultaneously prime inﬁnitely often, it suﬃces to show that
S > 0 for all large x.
The shape of S means that one can consider the terms weighted by 1P(Li(n)) separately
for each Li ∈ L, which makes these terms feasible to estimate accurately using current tech-
niques. In particular, the only knowledge about the joint behaviour of the prime values of the
Li is derived from the pigeonhole principle described above.
The method only succeeds if the weights wn are suitably concentrated on integers n when
many of the Li(n) are prime. To enable an unconditional asymptotic estimate for S , the wn
are typically chosen to mimic sieve weights, and in particular Selberg sieve weights (which
tend to be the best performing weights when the `dimension' k of the sieve is large). One
can then hope to estimate a quantity involving such sieve weights provided one can prove
suitable equidistribution results in arithmetic progressions. The strength of concentration of
the weights wn on primes depends directly on the strength of equidistribution results available.
The original work of Goldston Pintz and Yıldırım showed that one could construct weights
wn which would show that S > 0 for m = 1 (and for k suﬃciently large) if one could prove
a suitable extension of the Bombieri-Vinogradov theorem. Zhang [20] succeeded in proving
such an extension3, and as a consequence showed the existence of bounded gaps between
primes.

3The actual form of Zhang's extension is slightly weaker than that considered in original conditional result
of Goldston, Pintz and Yıldırım, although it is suﬃcient for the argument.

6 JAMES MAYNARD

The author's work [13] introduced a modiﬁcation to the choic es of the sieve weights wn
(this modiﬁcation was also independently discovered by Terence Tao at the same time). This
modiﬁcation enables wn to be rather more concentrated on n for which many of the Li(n) are
prime. This allows one to show S > 0 for any m ∈ N, and moreover the method works even
if one has much more limited knowledge about primes in arithmetic progressions.
As remarked in [13], the fact that the method now works even with only a limited amount of
knowledge about primes in arithmetic progressions makes it rather ﬂexible, and in particular
applicable to counting primes in subsets, where we have more limited equidistribution results.
Moreover, it is possible to exploit the ﬂexibility of the the pigeonhole principle setup in (5.1)
to consider slightly more exotic combinations, which can ensure that the n making a positive
contribution to S also satisfy `typical' properties.
Therefore we can consider modiﬁed sums of the form

S = ∑

n∈A(x)
( k∑

i=1 1P(Li(n)) − m − k1B(n)
)wn

for some set of integers A, set of primes P and set of `atypical' integers B. Provided we
have some weak distribution results available (such as those asserted by Hypothesis 1) then
we can estimate all the terms involved in this sum. Again, by the pigeonhole principle, we
see that if n ∈ A(x) makes a positive contribution to S , then at least m + 1 of the Li(n) are
primes in P, and that n < B. We expect that if B represents an `atypical' set, and P is not
too sparse (relative to A) then we can choose wn similarly to before and show that S > 0
for k suﬃciently large. Moreover, by modifying some of the technical aspects of the method
in [13], we can obtain suitable uniform estimates for such sums S even when we allow the
coeﬃcients ai, bi of Li(n) = ain + bi, the number k of functions and the number m of primes
we ﬁnd to vary with x in certain ranges.
Our work necessarily builds on previous work in [13], and a certain degree of familiarity
with [13] is assumed.
 6. Proof of theorems 3.1, 3.2, 3.3, 3.4 and 3.5

The proof of theorems 3.1-3.5 relies on the following key proposition.

Proposition 6.1. Let α > 0 and 0 < θ < 1. Let A be a set of integers, P a set of primes,
L = {L1, . . . , Lk} an admissible set of k linear functions, and B, x integers. Assume that the
coeﬃcients Li(n) = ain + bi ∈ L satisfy |ai|, |bi| ≤ x
α and ai , 0 for all 1 ≤ i ≤ k, and that
k ≤ (log x)
α and 1 ≤ B ≤ x
α. Let x
θ/10 ≤ R ≤ x
θ/3. Let ρ, ξ satisfy k(log log x)
2/(log x) ≤
ρ, ξ ≤ θ/10, and deﬁne
 S(ξ; D) = {n ∈ N : p|n =⇒ (p > x
ξ or p|D)}.

There is a constant C depending only on α and θ such that the following holds. If k ≥ C
and (A, L, P, B, x, θ) satisfy Hypothesis 1, then there is a choice of nonnegative weights wn =
wn(L) satisfying
 wn ≪ (log R)
2k k∏

i=1
 ∏

p|Li(n),p∤B 4

such that
 DENSE CLUSTERS OF PRIMES IN SUBSETS 7

(1) We have ∑

n∈A(x) wn = (
1 + O( 1
(log x)1/10 )) Bk

ϕ(B)k SB(L)#A(x)(log R)
kIk.

(2) For any L(n) = aLn + bL ∈ L with L(n) > R on [x, 2x], we have
∑

n∈A(x) 1P(L(n))wn ≥ (
1 + O( 1
(log x)1/10 )) Bk−1

ϕ(B)k−1 SB(L)ϕ(|aL|)
|aL| #PL,A(x)(log R)
k+1Jk

+O( Bk

ϕ(B)k SB(L)#A(x)(log R)
k−1Ik)
.

(3) For L = a0n + b0 < L and D ≤ x
α, if ∆L , 0 we have
∑

n∈A(x) 1S(ξ;D)(L(n))wn ≪ ξ−1 ∆L
ϕ(∆L) D
ϕ(D) Bk

ϕ(B)k SB(L)#A(x)(log R)
k−1Ik,

where
 ∆L = |a0|
 k∏

j=1 |a0b j − b0a j|.

(4) For L ∈ L we have
∑

n∈A(x)
( ∑

p|L(n)
p<xρ
p∤B
 1)
wn ≪ ρ2k4(log k)
2 Bk

ϕ(B)k SB(L)#A(x)(log R)
kIk.

Here Ik, Jk are quantities depending only on k, and SB(L) is a quantity depending only on L,
and these satisfy

SB(L) = ∏

p∤B
 (1 − #{1 ≤ n ≤ p : p| ∏k
i=1 Li(n)}
p
 )(
1 − 1
p
 )−k ≫ 1
exp(O(k)) ,

Ik = ∫ ∞

0 · · · ∫ ∞

0 F2(t1, . . . , tk)dt1 . . . dtk ≫ (2k log k)
−k,

Jk = ∫ ∞

0 . . . ∫ ∞

0
 (∫ ∞

0 F(t1, . . . , tk)dtk)2dt1 . . . dtk−1 ≫ log k
k Ik,

for a smooth function F = Fk : R
k → R depending only on k. Moreover, if all functions L ∈ L
are of the form L = an+bL, for some ﬁxed a and bL ≪ log x/(k log k), then for η ≥ (log x)
−9/10,
we have ∑

b≪η log x
L(n)=an+b
 ∆L
ϕ(∆L) ≪ η(log x)(log k).

Here the implied constants depend only on θ, α, and the implied constants from Hypothesis 1.

Assuming Proposition 6.1, we now establish theorems 3.1-3.5 in turn.

Proof of Theorem 3.1. We ﬁrst note that by passing to a subset of L, it is suﬃcient to show
that in the restricted range C ≤ k ≤ (log x)
1/5 we have the weaker bound

(6.1) #{n ∈ A(x) : #({L1(n), . . . , Lk(n)} ∩ P) ≥ C−1δ log k} ≫ #A(x)
(log x)k exp(Ck5) .

The main result then follows with a suitably adjusted value of C.

8 JAMES MAYNARD

For m ∈ N, we consider the sum

(6.2) S = ∑

n∈A(x)

( k∑

i=1 1P(Li(n)) − m − k
 k∑

i=1
 ∑

p|Li(n)
p<xρ
p∤B
 1)
wn = S 1 − S 2 − S 3,

where wn are the weights whose existence is guaranteed by Proposition 6.1. We note that for
any n ∈ A(x), the term in parentheses in (6.2) is positive only if at least m + 1 of the Li(n)
are primes in P, and none of the Li(n) have any prime factors p ∤ B less than x
ρ. Moreover,
we see that if this is the case then since ai, bi < x
α, each Li(n) can have at most O(1/ρ) prime
factors p ∤ B, and so

(6.3) wn ≪ (log x)
2k k∏

i=1
 ∏

p|Li(n)
p∤B
 4 ≪ (log x)
2k exp(O(k/ρ)).

Since the term in parentheses in (6.2) can be at most k, we have that

(6.4) #{n ∈ A(x) : #({L1(n), . . . , Lk(n)} ∩ P) ≥ m} ≫ S
k(log x)2k exp(O(k/ρ)).

Thus it is suﬃcient to obtain a suitable lower bound for S . (Essentially the same idea has
been used by Goldston, Pintz and Yıldırım in [7].) Using Proposition 6.1, we have

S 1 = ∑

n∈A(x)
 k∑

i=1 1P(Li(n))wn ≥ (1 + o(1)) Bk−1

ϕ(B)k−1 SB(L)(log R)
k+1 Jk
 k∑

i=1
 ϕ(ai)
ai #PLi,A(6.5)
 + o( Bk

ϕ(B)k SB(L)#A(x)(log R)
kIk)
,

S 2 = m ∑

n∈A(x) wn = m(1 + o(1)) Bk

ϕ(B)k SB(L)#A(x)(log R)
kIk,(6.6)
 S 3 = k ∑

n∈A(x)
 k∑

i=1
 ∑

p|Li(n)
p<xρ
p∤B
 wn ≪ ρ2k6(log k)
2 Bk

ϕ(B)k SB(L)#A(x)(log R)
kIk.(6.7)

We choose ρ = c0k−3(log k)
−1 with c0 a small absolute constant such that S 3 ≤ (1/3 + o(1))S 2.
(This choice satisﬁes the bounds of Proposition 6.1 since k ≤ (log x)
1/5 and k is taken to be
suﬃciently large in terms of θ.) Thus, for x suﬃciently large, we have

S ≥ Bk

ϕ(B)k SB(L)(log R)
k( Jk
2 log R
 k∑

i=1
 ϕ(ai)ϕ(B)
aiB #PLi,A(x) − 2mIk#A(x)
).(6.8)

By the assumption of Theorem 3.1, we have

(6.9) 1
k
 k∑

i=1
 ϕ(ai)ϕ(B)
aiB #PLi,A(x) ≥ δ#A(x)
log x .

From Proposition 6.1, we have Jk/Ik ≫ (log k)/k. Combining this with (6.8) and (6.9), we
have (for x suﬃciently large)

(6.10) S ≥ (θ/3)
k Bk

ϕ(B)k SB(L)#A(x)(log x)
kIk(
3c1δ log k − 2m)
,

DENSE CLUSTERS OF PRIMES IN SUBSETS 9

for some constant c1 depending only on θ. In particular, if m = c1δ log k, then m ≫ 1
(since δ ≥ (log k)
−1 by assumption), and S > 0. Using the bounds Ik ≫ (2k log k)
−k and
SB(L) ≥ exp(−Ck) from Proposition 6.1, along with the trivial bound B/ϕ(B) ≥ 1, we obtain

(6.11) S ≫ (θ/3)
k Bk

ϕ(B)k SB(L)#A(x)(log x)
kIk ≫ #A(x)(log x)
k exp(−C2k2),

for a suitable constant C2 depending only on θ. Combining this with (6.4), and recalling our
choices of m, ρ gives for x ≥ C3

(6.12) #{n ∈ A(x) : #({L1(n), . . . , Lk(n)} ∩ P) ≥ c1δ log k} ≥ #A(x) exp(−C3k5)
(log x)k ,

provided C3 is chosen suﬃciently large in terms of θ and α. This gives (6.1), and so the ﬁrst
claim of the theorem.
For the second claim, we have Li = an + bi for all 1 ≤ i ≤ k, with a ≪ 1 and bi ≤ η(log x).
(We will eventually take η = c4(k log k)
−1, for some ﬁxed c4 which implies the bound in the
statement of Theorem 3.1.) In place of S we consider

S ′ = ∑

n∈A(x)
( k∑

i=1 1P(Li(n)) − m − k
 k∑

i=1
 ∑

p|Li(n)
p<xρ,p∤B
 1 − k ∑

b≤η log x
L=an+b<L
 1S(θ/10;1)(L(n))
)wn(6.13)
 = S 1 − S 2 − S 3 − S 4.

The term in parentheses in (6.13) is positive only if at least m of the Li(n) are primes, none of
the Li(n) have a prime factor p ∤ B smaller than x
ρ, and all integers not in {L1(n), . . . , Lk(n)}
of the form an + b with b ≤ η log x have a prime factor less than x
θ/10. In particular, there can
be no primes in the interval [an, an + η(log x)] apart from possibly {L1(n), . . . , Lk(n)}, and so
the primes counted in this way must be consecutive.
For S 4, we notice that ∆L , 0 for all L we consider since any L has the same lead coeﬃcient
as the Li (and so can't be a multiple of one of them). By Proposition 6.1 , we have

(6.14) S 4 ≪ k Bk

ϕ(B)k #A(x)(log R)
k−1SB(L)Ik ∑

b≤η log x
L=an+b<L
 ∆L
ϕ(∆L) ≪ ηk(log k)S 2.

We choose η = c4/(k log k) for some suﬃciently small constant c4 (this satisﬁes the require-
ments of Proposition 6.1). We then see that the bound (6.8) holds for S ′ in place of S provided
x, k are suﬃciently large. The whole argument then goes through as before. □

Proof of Theorem 3.2. We note that the result is trivial if y ≫ (log x)
2, y = O(1) or x = O(1)
by the pigeonhole principle, Bertrand's postulate and the p rime number theorem. Therefore,
by changing the implied constant if necessary, it is suﬃcient to establish the result for y ≤
(log x)
1/5 with y suﬃciently large.
We take θ = 1/3, P = P, A = N, L = {L1, . . . , Lk}, with Li(n) = n + hi, where hi is the
ith prime larger than k. By the prime number theorem, hi ≤ 2k log k for all i (provided k is
suﬃciently large). This is an admissible set.
By the Landau-Page theorem (see, for example, [4, Chapter 14]) there is at most one mod-
ulus q0 ≤ exp(2c1 √log x) such that there exists a primitive character χ modulo q0 for which
L(s, χ) has a real zero larger than 1 − c2(log x)
−1/2 (for suitable ﬁxed constants c1, c2). If this
exceptional modulus q0 exists, we take B to be the largest prime factor of q0, and otherwise

10 JAMES MAYNARD

we take B = 1. For all q ≤ exp(c1 √log x) with q , q0 we then have the eﬀective bound (see,
for example, [4, Chapter 20])

(6.15) ϕ(q)
−1 ∑∗

χ |ψ(x, χ)| ≪ x exp(−3c1 √log x),

where the summation is over all primitive χ mod q and ψ(x, χ) = ∑
n≤x χ(n)Λ(n). Following
a standard proof of the Bombieri-Vinogradov Theorem (see [4, Chapter 28], for example), we
have
(6.16)
∑

q<x1/2−ǫ
(q,B)=1
 sup
(a,q)=1

∣∣∣∣π(x; q, a) − π(x)
ϕ(q)
∣∣∣∣ ≪ x exp(−c1 √log x) + log x ∑

q<exp(2c1 √
log x)
(q,B)=1
 ∑∗

χ
 |ψ
′(x, χ)|
ϕ(q) .

With this choice of parameters, we therefore have error terms for part (ii) of Hypothesis
1 of size #A(x) exp(−c3 √log x), and so Hypothesis 1 holds for (A, L, P, B, x, 1/3) for any
k ≤ (log x)
1/5 provided k is suﬃciently large, since parts (i) and (iii) are trivial. Moreover,
if q0 exists it must be square-free apart from a possible factor of at most 4, and must satisfy
q0 ≫ (log x)/(log log x)
2 (from the class number formula). Therefore if q0 exists, log log x ≪
B ≪ exp(c1 √log x). Thus, whether or not q0 exists, we have

(6.17) B
ϕ(B) = 1 + O( 1
log log x
 )
.

We have

(6.18) #PL,A(x) = (1 + o(1))x
log x = (1 + o(1))#A(x)
log x ,

and so we may take δ = (1 + o(1)) in Theorem 3.1. Theorem 3.1 then gives

(6.19) #{x ≤ n ≤ 2x : π(n + 2k log k) − π(n) ≫ log k} ≫ x
(log x)k exp(Ck) .

Thus, given any x, y suitably large with y ≤ (log x)
1/5 we can take k = ⌊y/(2 log y)⌋, and see
that the above gives the result. All constants we have used are eﬀectively computable. □

Proof of Theorem 3.3. To get lower bounds of the correct order of magnitude, we average
over admissible sets. We assume without loss of generality that a is reduced modulo q, so
1 ≤ a < q. We then adopt the same set-up as in the proof of Theorem 3.2 for our choice
of A, P, θ, R. If an exceptional modulus q0 exists (as deﬁned in the proof of Theorem 3.2),
then we take B to be the largest prime factor of q0 coprime to q. Since q ≤ (log x)
1−ǫ and
q0 ≫ log x (with q0 essentially square-free) we have log log x ≪ǫ B ≪ x if q0 exists. Thus
B/ϕ(B) = 1 + o(1) regardless of whether q0 exists.
Instead of our individual choice of L, we will average over all admissible choices of L with
#L = k and where L = {L1, . . . , Lk} contains functions of the form Li(n) = qn + a + qbi with
qbi ≤ η log x. We write L(b) for such a set given by b1, . . . , bk. We consider

S ′′ = ∑

b1<···<bk
qbk≤η log x
L=L(b) admissible
 ∑

n∈A(x)
( k∑

i=1 1P(Li(n)) − m − k
 k∑

i=1
 ∑

p|Li(n)
p<xρ,p∤B
 1 − k ∑

b≤2η log x
L=qn+b<L
 1S(ρ;B)(L(n))
)wn(L).

(6.20)
 DENSE CLUSTERS OF PRIMES IN SUBSETS 11

Here wn(L) are the weights given by Proposition 6.1 for the admissible set L = L(b). For a
given admissible set L, the sum over n is then essentially the same quantity as S ′ from (6.13),
except in the ﬁnal term in parentheses we are considering elements with no prime factor less
than x
ρ instead of x
θ/10.
We see the term in parentheses in (6.20) is positive only if at least m of the Li(n) are
primes, all the remaining Li(n) have no prime factors p ∤ B less than x
ρ, and all other qn + b
with b ≤ 2η log n have a prime factor p ∤ B less than x
ρ. We see from this than no n can
make a positive contribution from two diﬀerent admissible sets (since if n makes a positive
contribution for some admissible set, the Li(n) are uniquely determined as the integers in
[qn, qn + η log x] with no prime factors p ∤ B less than x
ρ). By (6.3), we see that if n makes
a positive contribution then wn ≪ (log x)
2k exp(O(k/ρ)), with the implied bound uniform in
L(b).
As before, we choose ρ = c0k−3(log k)
−1, which makes the contribution of the third of the
terms in parentheses small compared to the second one. Following the argument of the proof
of Theorem 3.1, using S(ρ; B) in place of S(θ/10; 1) increases the size of the contribution of
the ﬁnal term by a factor O(ρ−1) = O(k3 log k). Thus to show the ﬁnal term is suitably small,
we take η ≤ ǫ to be a small multiple of k−4(log k)
−2 instead of 1/(k log k) (which is acceptable
for Proposition 6.1). With these choices, we ﬁnd that for a suitable constant c1 we have

(6.21) S ′′ ≥ (θ/3)
k Bk

ϕ(B)k SB(L)#A(x)(log x)
kIk ∑

b1<···<bk
qbk≤η log x
L(b) admissible
(3c1 log k − 2m)
.

Therefore, given m ∈ N we choose k = ⌈exp(m/c1)⌉. With this choice we see that S ′′ >
0. Using the bounds Ik ≫ (k log k)
−k and SB(L) ≫ exp(−Ck) from Proposition 6.1 and
Bk/ϕ(B)
k ≥ 1 we see that for a suitable constant C2 we have

(6.22) S ′′ ≫ x(log x)
k exp(−C2k2) ∑

b1<···<bk
qbk≤η log x
L admissible
 1.

Thus we are left to obtain a lower bound for the inner sum of (6.22). We see all the bi lie
between 0 and η(log x)/q. We greedily sieve this interval by removing for each prime p ≤ k
in turn any elements from the residue class modulo p which contains the fewest elements.
The resulting set has size at least

(6.23) η log x
q
 ∏

p≤k
 (1 − 1
p
 ) ≫ log x
qk4(log k)3 .

Any choice of k distinct bi from this set will the cause the resulting L(b) to be admissible. We
now recall from the theorem that we are only considering q ≤ (log x)
1−ǫ and m ≤ cǫ log log x.
For a suitably small choice of cǫ, we see that k = ⌈exp(m/c1)⌉ ≤ (log x)
ǫ/10. Therefore from
(6.23) we see the length of the interval is at least k2 if x is suﬃciently large in terms of ǫ. In
this case, we obtain the bound

(6.24) ∑

b1<···<bk
qbk≤η log x
L admissible
 1 ≥ k−k( c3 log x
qk4 log
3 k − k)k ≫ (log x
q
 )k exp(−C4k2),

for some constants c3, C4 > 0. Thus, substituting (6.24) into (6.22) we obtain

(6.25) S ′′ ≫ x(log x)
2k exp(−C5k2)q−k.

12 JAMES MAYNARD

We recall that every pair (n, L) for which n makes a positive contribution to S ′′ when consid-
ering L is counted with weight at most kwn(L) ≪ k(log x)
2k exp(O(k/ρ)) (uniformly over all
choices of L). Putting this all together, we obtain the number N of integers n with x ≤ n ≤ 2x
such that there are ≫ log k consecutive primes all congruent to a (mod q) in the interval
[qn, qn + η log x] satisﬁes

(6.26) N ≫ x
qk exp(C6k5).

We see that the initial prime in each such interval is counted by at most log x values of n.
Therefore, changing the count to be over the initial prime, recalling k = ⌈exp(m/c1)⌉, recalling
that η ≤ ǫ, and replacing x with x/3q gives

(6.27) #{pn ≤ x : pn ≡ · · · ≡ pn+m ≡ a (mod q), pn+m − pn ≤ ǫ log x} ≫ǫ π(x)
(2q)exp(Cm) ,

for a suitable constant C > 0, as required. □

Proof of Theorem 3.4. We take P = P, A = [x, x + y], B = 1, θ = 1/30 − ǫ. Given m, we
choose k = exp(Cm) for some suitable constant C > 0.
Timofeev [19] (improving earlier work of Huxley and Iwaniec [9] and Perelli, Pintz and
Salerno [15]) has shown that, for θ = 1/30 − ǫ/2, for any x
7/12+ǫ/2 ≤ y ≤ x and any ﬁxed
C′ > 0 we have

(6.28) ∑

q<xθ sup
(a,q)=1
∣∣∣∣π(x + y; q, a) − π(x; q, a) − π(x + y) − π(x)
ϕ(q)
 ∣∣∣∣ ≪C′,ǫ y
(log x)C′ .

By taking C′ suﬃciently large in terms of k, we see that (6.28) implies Hypothesis 1 holds for
our choice of θ = 1/30 − ǫ provided x is suﬃciently large in terms of m and ǫ. Theorem 3.1
then automatically gives Theorem 3.4. □

Proof of Theorem 3.5. We take A = N, B = ∆K and P, L the sets given by the statement
of the theorem. To avoid confusion, we note that ∆K here is the discriminant of K/Q, and
unrelated to ∆L from Proposition 6.1. Murty and Murty [14] have then established the key
estimate (2) of Hypothesis 1 with any θ < min(1/2, 2/#G), where G = Gal(K/Q) (the other
estimates being trivial). Finally, we have

(6.29) 1
k B
ϕ(B)
 k∑

i=1
 ϕ(ai)
ai #PLi,A(x) ≥ (1 + o(1)) ∆K#C
ϕ(∆K)#G x
log x,

and so for x suﬃciently large, we may take δ to be a constant depending only on K. The result
now follows directly from Theorem 3.1. □

7. Initial Considerations

We recall that we are given a set A of integers, a set P of primes, an admissible set L =
{L1, . . . , Lk} of integer linear functions, an integer B and quantities R, x. We assume that the
coeﬃcients of Li(n) = ain + bi ∈ L satisfy |ai|, |bi| ≤ x
α, ai , 0, and k = #L is suﬃciently
large in terms of the ﬁxed quantites θ, α and satisﬁes k ≤ (log x)
1/5. B, R satisfy 1 ≤ B ≤ x
α,
and x
θ/10 ≤ R ≤ x
θ/3. Finally, we assume from now on that the set A satisﬁes

(7.1) ∑

q≤xθ max
a
 ∣∣∣∣#A(x; q, a) − #A(x)
q
 ∣∣∣∣ ≪ #A(x)
(log x)100k2 ,

DENSE CLUSTERS OF PRIMES IN SUBSETS 13

and

(7.2) #A(x; q, a) ≪ #A(x)
q

for any q < x
θ. Together these assumptions are a slight generalization of the assumptions of
Proposition 6.1.
We deﬁne the multiplicative functions ω = ωL and ϕω = ϕω,L and the singular series SD(L)
for an integer D by

ω(p) =
 

#{1 ≤ n ≤ p : ∏k
i=1 Li(n) ≡ 0 (mod p)}, p ∤ B,
0, p|B,
(7.3)
 ϕω(d) = ∏

p|d (p − ω(p)),(7.4)
 SD(L) = ∏

p∤D
(1 − ω(p)
p
 )(
1 − 1
p
 )−k.(7.5)

Since L is admissible, we have ω(p) < p for all p and so ϕω(n) > 0 and SD(L) > 0 for any
integer D. Since ω(p) = k for all p ∤ ∏k
i=1 ai ∏
i, j(aib j − bia j) we see the product SD(L)
converges.
The main innovation in [13] was a diﬀerent choice of the sieve weights used in the GPY
method to detect small gaps between primes. In order to adapt the argument of [13] to the
more general situation considered here, we need to modify the choice of these weights further
to produce a choice more amenable to obtaining uniform estimates. In particular, in [13] the
`W-trick' was used to eliminate the need for consideration o f the singular series which would
naturally arise. In our situation, however, in order to obtain suitable uniform estimates without
stronger assumptions on the error terms in Hypothesis 1, we need to take these singular series
into account.
We will consider sieve weights wn = wn(L), which are deﬁned to be 0 if ∏k
i=1 Li(n) is a
multiple of any prime p ≤ 2k2 with p ∤ B. We let W = ∏p≤2k2,p∤B p. If (Li(n), W) = 1 for all
1 ≤ i ≤ k we have

(7.6) wn = ( ∑

di|Li(n)∀i λd)2,

for some real variables λd depending on d = (d1, . . . , dk). We ﬁrst restrict our λd to be sup-
ported on d with d = ∏k
i=1 di square-free and coprime to W B.
Given a prime p ∤ W B, let 1 ≤ rp,1 < · · · < rp,ω(p) ≤ p be the ω(p) residue classes
for which ∏k
i=1 Li(n) vanishes modulo p. For each such prime p, we ﬁx a choice of indices
jp,1, . . . , jp,ω(p) ∈ {1, . . . , k} such that jp,i is the smallest index such that

(7.7) L jp,i (rp,i) ≡ 0 (mod p)

for each i ∈ {1, . . . , ω(p)}. (We could choose any index satisfying the above condition; we
choose the smallest index purely for concreteness.) All the functions Li are linear and, since
L is admissible, none of the Li are a multiple of p. This means that for any L ∈ L there is
at most one residue class for which L vanishes modulo p. Thus the indices jp,1, . . . , jp,ω(p)
we have chosen must be distinct. We now restrict the support of λd to (d j, p) = 1 for all
j < { jp,1, . . . , jp,ω(p)}.

14 JAMES MAYNARD

We see these restrictions are equivalent to the restriction that the support of λd must lie the
set

(7.8) Dk = Dk(L) = {d ∈ Nk : µ
2(d) = 1, (d j, W j) = 1∀ j},

where W j are square-free integers each a multiple of W B, and any prime p ∤ W B divides
exactly k − ω(p) of the W j (such p|W j if j < { jp,1, . . . , jp,ω(p)}). We recall that in our notation
µ
2(d) = µ
2(
∏k
i=1 di).
The key point of these restrictions is so that diﬀerent components of diﬀerent d occurring
in our sieve weights will be relatively prime. Indeed, let d and e both occur in the sum (7.6).
If p|di then p|Li(n), and so i must be the chosen index for the residue class n (mod p). But if
we also have p|e j then similarly j must be the chosen index for this residue class, and so we
must have i = j. Hence (di, e j) = 1 for all i , j.
Similar to [13], we deﬁne λd in terms of variables yr supported on r ∈ Dk by

(7.9) λd = µ(d)d ∑

d|r
 yr
ϕω(r) , yr = 1Dk(r)W kBk

ϕ(W B)k SW B(L)F(log r1
log R , . . . , log rk
log R
 ),

(again, we recall d = ∏k
i=1 di) where x
θ/10 ≤ R ≤ x
θ/3 and F : R
k → R is a smooth function
given by

(7.10) F(t1, . . . , tk) = ψ
( k∑

i=1 ti) k∏

i=1
 ψ(ti/Uk)
1 + Tkti , Tk = k log k, Uk = k−1/2.

Here ψ : [0, ∞) → [0, 1] is a ﬁxed smooth non-increasing function supported on [0, 1] which
is 1 on [0, 9/10]. In particular, we note that this choice of F is non-negative, and that the
support of ψ implies that

(7.11) λd = 0 if d = ∏k
i=1 di > R.

We will ﬁnd it useful to also consider the closely related functions F1 and F2 which will
appear in our error estimates, deﬁned by

(7.12) F1(t1, . . . , tk) =
 k∏

i=1
 ψ(ti/Uk)
1 + Tkti , F2(t1, . . . , tk) = ∑

1≤ j≤k
( ψ(t j/2)
1 + Tkt j
 ∏

1≤i≤k
i, j
 ψ(ti/Uk)
1 + Tkti
 ).

Finally, by Moebius inversion, we see that (7.9) implies that for r ∈ Dk

(7.13) yr = µ(r)ϕω(r) ∑

r|f
 yf
ϕω( f )
 ∑

d
r|d,d|f
 µ(d) = µ(r)ϕω(r) ∑

r|d
 λd
d .

8. Preparatory Lemmas

Lemma 8.1. (i) There is a constant C, such that for any admissible set L of size k we have

SB(L) ≥ exp(−Ck).

(ii) Let all functions Li ∈ L be of the form Li = an + bi, for some integers |a| ≪ 1 and
|bi| ≪ log x. Let ∆L = |a|k+1 ∏k
i=1 |bi − b| and η ≥ (log x)
−9/10. Then we have
∑

|b|≤η log x
L(n)=an+b<L
 ∆L
ϕ(∆L) ≪ η(log x)(log k).

DENSE CLUSTERS OF PRIMES IN SUBSETS 15

Proof. Since ω(p) ≤ min(k, p − 1) for any admissible L of size k, we have

SB(L) = ∏

p∤B
 (
1 − ω(p)
p
 )(1 − 1
p
 )−k ≥ ∏

p≤k,p∤B
 1
p
 ∏

p>k,p∤B

(1 − k
p
 )(1 − 1
p
 )−k.(8.1)

Since all terms in the products on the right hand side are less than 1, we can drop the restriction
p ∤ B for a lower bound. This gives

(8.2) SB(L) ≥ ∏

p≤k
 1
p
 ∏

p>k
 (1 + O(k2/p2)
) ≥ exp(−Ck).

We now consider the second statement. We have Li(n) = an+bi with |bi| ≪ log x, and consider
L = an + b < L with |b| ≤ η log x. If k ≫ log log x then we use the bound ∆L/ϕ(∆L) ≪
log log ∆L ≪ log k to give

(8.3) ∑

|b|≤η log x
L=an+b<L
 ∆L
ϕ(∆L) ≪ η(log k)(log x).

We now establish (8.3) in the case k ≪ log log x. Using the identity e/ϕ(e) = ∑d|e µ
2(d)/ϕ(d),
and splitting the terms depending on the size of divisors, we have
∑

|b|≤η log x
L=an+b<L
 ∆L
ϕ(∆L) = a
ϕ(a)
 ∑

|b|≤η log x
L=an+b<L
 ∑

d|∆L
(d,a)=1
 µ
2(d)
ϕ(d)

≪ ∑

|b|≤η log x
L=an+b<L
( ∑

1≤d≤η log x
d|∆L,(d,a)=1
 µ
2(d)
ϕ(d) + ∑

d>η log x
d|∆L
 µ
2(d) ∑p|d log p
ϕ(d) log(η log x)
)

≪ ∑

1≤d≤η log x
(d,a)=1
 µ
2(d)
ϕ(d)
 ∑

|b|≤η log x
L=an+b<L
d|∆L
 1 + ∑

|b|≤η log x
L=an+b<L
 ∑

p|∆L
 log p
p log(η log x) ∆L
ϕ(∆L).(8.4)

We ﬁrst consider the second term on the right hand side of (8.4). We have ∑p|∆L p−1 log p ≪
log log ∆L and ∆L/ϕ(∆L) ≪ log log ∆L. But we are only we only considering k ≪ log log x
and η ≥ (log x)
−9/10, and so (log log ∆L)
2 ≪ (log log log x)
2 = o(log(η log x)). Therefore we
see that the total contribution from the second term in (8.4) is o(η log x).
We now consider the ﬁrst sum in (8.4). For every prime p|d, there are at most k choices for
the residue class b (mod p) such that p|∆L, and trivially there are also at most p choices. Thus
the inner sum can be written as ∏p|d min(p, k) sums over b in a ﬁxed arithmetic progression
modulo d. For each such sum there are ≪ η(log x)/d possible values of b. Thus we have
∑

1≤d≤η log x
(d,a)=1
 µ
2(d)
ϕ(d)
 ∑

|b|≤η log x
L=an+b<L
d|∆L
 1 ≪ ∑

d≤η log x
 µ
2(d) ∏p|d min(p, k)
ϕ(d)
 (η log x
d
 )

≪ η log x ∏

p≤k
 (1 + 1
p − 1
 ) ∏

p>k
 (
1 + k
p(p − 1)
)

≪ η(log x)(log k).(8.5)

This gives the result. □

16 JAMES MAYNARD

Lemma 8.2. Let
 Yr = W kBkSW B(L)
ϕ(W B)k F2(log r1
log R , . . . , log rk
log R
 ),

where F2 is given by (7.12). Then
(i) Let r, s ∈ Dk with si = ri for all i , j, and s j = Ar j for some A ∈ N. Then

ys = yr + O(
TkYr log A
log R
 )
.

(ii) Let r, s ∈ Dk with r = s and let A be the product of primes dividing r but not (r, s). Then

ys = yr + O(
Tk(Yr + Ys)log A
log R
 ).

Proof. We recall the deﬁnitions of ψ, F2, Uk = k−1/2 and Tk = k log k from Section 7. Given
u, v ≥ 0 with |u − v| ≤ ǫ, we have

(8.6) 1
1 + Tku = 1 + O(Tkǫ)
1 + Tkv , ψ(u) = ψ(v) + O(ǫ).

We let ui = log ri/ log R, vi = log si/ log R and ǫi = vi − ui. For part (i) we have ǫi = 0 for i , j
and ǫ j = log A/ log R. We may assume ǫ j ≤ 1, u j ≤ Uk since otherwise the result is trivial. By
(8.6) we have

ψ
( k∑

i=1 vi) ψ(v j/Uk)
1 + Tkv j = (ψ
( k∑

i=1 ui) + O( log A
log R
 ))(
ψ
( u j
Uk
 ) + O( log A
Uk log R
 ))1 + O(
Tk log A
log R )

1 + Tku j .(8.7)

Since 1+U−1
k ≪ Tk, 0 ≤ ψ ≤ 1 and ψ(v j/2) = 1 (since v j = u j +ǫ j ≤ 1+Uk < 9/5), expanding
the terms and multiplying by ∏
i, j ψ(ui/Uk)/(1 + Tkui) gives the result for (i).
We now consider part (ii). We let t be the vector with ti = [ri, si]. By applying part (i) to
each component in turn, and using the fact that Yr is decreasing, we ﬁnd that

(8.8) ys = yt + O(
TkYs
 k∑

i=1
 log [ri, si]/si
log R
 ) = yt + O(
TkYs log A
log R
 ).

We obtain the same expression for r in place of s, and hence the result follows. □

We use the following lemma to estimate the various smoothed sums of multiplicative func-
tions which we will encounter.

Lemma 8.3. Let A1, A2, L > 0. Let γ be a multiplicative function satisfying

0 ≤ γ(p)
p ≤ 1 − A1, and − L ≤ ∑

w≤p≤z
 γ(p) log p
p − log z/w ≤ A2

for any 2 ≤ w ≤ z. Let g be the totally multiplicative function deﬁned on primes by g(p) =
γ(p)/(p−γ(p)). Finally, let G : [0, 1] → R be smooth, and let Gmax = supt∈[0,1](|G(t)|+|G′(t)|).
Then ∑

d<z µ(d)
2g(d)G(log d
log z
 ) = cγ log z ∫ 1

0 G(x)dx + OA1,A2(cγLGmax),

where cγ = ∏

p
 (
1 − γ(p)
p
 )−1(1 − 1
p
 ).

Proof. This is [6, Lemma 4], with κ = 1 and slight changes to the notation. □

DENSE CLUSTERS OF PRIMES IN SUBSETS 17

Lemma 8.4. Let r ≤ k ≪ (log R)
1/5. Let W1, . . . , Wr ≤ RO(k) all be a multiple of ∏p≤2k2 p. Let
g be a multiplicative function with g(p) = p + O(k). Let G : R → R be a smooth function
supported on the interval [0, 1] such that

sup
t∈[0,1](|G(t)| + |G′(t)|) ≤ ΩG
 ∫ ∞

0 G(t)dt,

for some quantity ΩG which satisﬁes rΩG = o((log R)/(log log R)). Let Φ : R → R be smooth
with Φ(t), Φ′(t) ≪ 1 for all t.
Then for k suﬃciently large we have
∑

e∈Nr
(ei,Wi)=1∀i
 µ
2(e)
g(e) Φ( k∑

i=1
 log ei
log R
 ) k∏

i=1 G(log ei
log R
 ) = Πg(log R)
r (

t1,...,tr≥0 Φ(
 r∑

i=1 ti)
 r∏

i=1 G(ti)dti

+ O(rΩGΠg(log R)
r−1 log log R (

t1,...,tr≥0
 r∏

i=1 G(ti)dti)
,

where Πg = ∏

p
 (
1 + n(p)
g(p)
)(1 − 1
p
 )r, n(p) = #{i ∈ {1, . . . , r} : p ∤ Wi}.

Proof. We let Σ denote the sum in the statement of the lemma. We estimate the Σ by applying
Lemma 8.3 r times to each variable e1, . . . , er in turn. We use induction to establish that,
having applied the lemma j times, we obtain the estimate

Σ = c j(log R) j ∑

e j+1,...,er
(ei,Wi)=1∀i
 µ(e j+1 . . . er)
2

g j(e j+1 . . . ek)
 r∏

i= j+1 G(ui) (

t1,...,t j≥0 Φ( j∑

i=1 ti +
 r∑

i= j+1 ui) j∏

i=1 G(ti)dti

+c j(log R) j(∫ ∞

0 G(t)dt) j( j∑

ℓ=1
 ( j
ℓ
)
O(ΩG log log R
log R
 )ℓ) ∑

e j+1,...,er
(ei,Wi)=1∀i
 µ(e j+1 . . . er)
2

g j(e j+1 . . . ek)
 r∏

i= j+1 G(ui),(8.9)

where
 ui = log ei
log R , n j(p) = #{i ∈ {1, . . . , j} : p ∤ Wi},(8.10)
 g j(d) = ∏

p|d (g(p) + n j(p)), c j = ∏

p
 (1 + n j(p)
g(p)
 )(1 − 1
p
 ) j.

We see that (8.9) clearly holds when j = 0. We now assume that (8.9) holds for some j < r,
and apply Lemma 8.3 to the sum over e j+1. In the notation of Lemma 8.3, we have

γ(p) =
 

0, p|W j+1 ∏r
i= j+2 ei,
p(1 + n j(p) + g(p))
−1 = 1 + O(k/p), p ∤ W j+1 ∏r
i= j+2 ei.
(8.11)

Since W j+1 is a multiple of all primes p ≤ 2k2 (by assumption of the lemma), we see that we
can take A1 and A2 to be ﬁxed constants (independent of j, k, r, x) provided k is suﬃciently
large. With this choice of γ(p), we see that

L ≪ 1 + ∑

p|W j+1 ∏r
i= j+2 ei
 log p
p + ∑

p>2k2
 k log p
p2 ≪ log log R.(8.12)

18 JAMES MAYNARD

Here we used the fact the ﬁrst sum is over prime divisors of an integer which is ≪ RO(k2), and
this sum is largest when all the prime divisors are smallest, and that k ≪ (log R)
1/5 ≪ log R.
We apply Lemma 8.3 to the main term with the smooth function G1, and to the error term
with the smooth function G2 deﬁned by

G1(t) = (

t1,...,t j≥0 G(t)Φ( j∑

i=1 ti + t +
 r∑

i= j+2 ui)( j∏

i=1 G(ti)dti)( r∏

i= j+2 G(ui)
),(8.13)
 G2(t) = G(t)
(∫
t≥0 G(t′)dt′) j( r∏

i= j+2 G(ui)
),(8.14)

where we recall ui = (log ei)/ log R for i > j+1. With this choice, we see that from the bounds
on Φ, G given in the lemma, we have

sup
t∈[0,1]
(|G1(t)| + |G′
1(t)| + |G2(t)| + |G′
2(t)|) ≪ ΩG(∫
t≥0 G(t)dt) j+1( r∏

i= j+2 G(ui)
)

= ΩG
 ∫
t≥0 G2(t)dt.(8.15)

Thus Lemma 8.3 gives

∑

e j+1
(e j+1,W j+1 ∏r
i= j+2 ei)=1
 µ
2(e j+1)
g j(e j+1) G1(log e j+1
log R
 ) = log R ∏

p
 (1 − γ(p)
p
 )−1(1 − 1
p
 ) ∫ ∞

0 G1(t)dt

+O(ΩG log log R ∏

p
 (
1 − γ(p)
p
 )−1(1 − 1
p
 ) ∫ ∞

0 G2(t)dt)
,(8.16)

and we obtain the same expression when summing with G2 instead of G1, except ∫ ∞

0 G1(t)dt is
replaced by ∫ ∞

0 G2(t)dt in the main term. The implied constant in the error term is independent
of j. We note that

c j ∏

p
 (1 − γ(p)
p
 )−1(
1 − 1
p
 ) = ∏

p|W j+1
(
1 + n j(p)
g(p)
 )(1 − 1
p
 ) j+1 ∏

p∤W j+1
(
1 + n j(p) + 1
g(p)
 )(
1 − 1
p
 ) j+1

× ∏

p|e j+2...er
p∤W j+1
 ( n j(p) + g(p)
n j(p) + g(p) + 1
 )

= c j+1g j(e j+2 . . . er)
g j+1(e j+2 . . . er) .(8.17)

Therefore substituting (8.16) and (8.17) into (8.9) gives the result for j + 1. We conclude that
(8.9) holds for all j ≤ r.
Finally, let ε = (ΩG log log R)/ log R. By assumption of the lemma, we have ε = o(1/r).
We see the sum over ℓ in (8.9) is (1+O(ε)) j −1 = O( jε) where, by our bound on ε, the implied
constant is independent of j ≤ r. Substituting this into (8.9) with j = r gives the result. □

DENSE CLUSTERS OF PRIMES IN SUBSETS 19

Lemma 8.5. Let k ≤ (log x)
1/5 be suﬃciently large in terms of θ. Then we have

(i) |λd| ≪ k−k(log R)
k,

(ii) wn ≪ k−2k(log x)
2k k∏

i=1
 ∏

p|Li(n),p∤B 4,

(iii) wn ≪ R2+o(1).

Proof. Substituting in our choice of yr, we have for d ∈ Dk

(8.18) |λd| = d ∑

d|r
 yr
ϕω(r) = dW kBkSW B(L)
ϕω(d)ϕ(W B)k ∑

d|r∈Dk
 1
ϕω(r/d) F( log r1
log R , . . . , log rk
log R
 )
.

We obtain an upper bound for (8.18) by replacing the log ri/ log R in the argument of F with
σi = (log ri/di)/ log R, since F is decreasing in each argument.
We now estimate the sum using Lemma 8.4. We see from (7.10) that F is of the form
Φ(
∑k
i=1 ti) ∏k
i=1 G(ti), and we have a bound on G, Φ which corresponds to ΩG = O(kTk)
(where Tk = k log k is the constant given by (7.10)). Since k ≤ (log x)
1/5, we see that
k2Tk = o(log log R/ log R). Finally, we note that the condition r ∈ Dk forces (r j, dW j) = 1 for
integers W1, . . . , W j ≤ x
O(k) which are all a multiple of W B. Thus we can apply Lemma 8.4,
which gives

∑

d|r∈Dk
 F(σ1, . . . , σk)
ϕω(r/d) ≤ ϕ(W B)
k

W kBk ∏

p∤W B

(1 + ω(p)
p − ω(p)
)(
1 − 1
p
 )k (

t1,...,tk≥0 H(t1, . . . , tk)dt1 . . . dtk,

(8.19)

where
 H(t1, . . . , tk) = F(t1, . . . , tk) + O(k2Tk log log R
log R F1(t1, . . . , tk)
).(8.20)

Substituting (8.19) into (8.18), noting that the singular series cancel and that H ≤ (1+o(1))F1,
we have
 |λd| ≤ (1 + o(1))(log R)
k (

t1,...,tk≥0 F1(t1, . . . , tk)dt1 . . . dtk

≪ (log R)
k(∫ Uk

0
 dt
1 + Tkt
 )k ≪ (log R
k
 )k.(8.21)

This gives the ﬁrst claim. The second claim now follows from this bound and the deﬁnition
(7.6) of wn, recalling that λd = 0 unless d1, . . . , dk are all squarefree and coprime to B. Finally,
for the third claim, the fact that λd is supported on d = d1 · · · dk < R gives

wn ≪ (log R)
2k

k2k ( ∑

d1···dk<R 1)2 ≪ R2+o(1)( ∑

d1···dk<R
 1
d1 . . . dk
 )2 ≪ R2+o(1). □

We will eventually be interested in the quantities Ik, Jk considered in the following lemma.

Lemma 8.6. Given a square-integrable function G : R
k → R, let

Ik(G) = ∫ ∞

0 · · · ∫ ∞

0 G2dt1 . . . dtk, Jk(G) = ∫ ∞

0 . . . ∫ ∞

0
 (∫ ∞

0 G dtk)2dt1 . . . dtk−1.

20 JAMES MAYNARD

Let F, F1, F2 be as given by (7.10) and (7.12). Then

1
(2k log k)k ≪ Ik(F) ≤ 1
(k log k)k , log k
k ≪ Jk(F)
Ik(F) ≪ log k
k ,

Ik(F) ≤ Ik(F1) ≤ Ik(F2)/k2 ≪ Ik(F), Jk(F) ≤ Jk(F1) ≤ Jk(F2)/k2 ≪ Jk(F).

Proof. A minor adaption of the argument of [13, Section 7] to account for the slightly diﬀerent
deﬁnition of F shows

Jk(F) ≥ (

∑k−1
i=1 ti<9/10−Uk
 (∫ ∞

0 F1dtk)2dt1 . . . dtk−1

≫ (

t1,...,tk−1≥0
 (∫ ∞

0 F1dtk)2dt1 . . . dtk−1 = Jk(F1).(8.22)

Applying the same concentration of measure argument to Ik(F) yields

Ik(F) ≥ (

∑k
i=1 ti<9/10
 F2
1dt1 . . . dtk ≫ (

t1,...,tk≥0 F2
1dt1 . . . dtk = Ik(F1).(8.23)

We also have the trivial bounds Ik(F) ≤ Ik(F1) ≤ k−2Ik(F2) and Jk(F) ≤ Jk(F1) ≤ k−2Jk(F2).
For our choice of ψ, Tk, Uk from (7.10), we see that
∫ ∞

0
 ψ(t/Uk)dt
1 + Tkt = ∫ 9Uk/10

0
 dt
1 + Tkt + O(∫ Uk

9Uk/10
 dt
1 + Tkt
 ) = 1
2k + O( 1
k log k
 ),(8.24)
 ∫ ∞

0
 ψ(t/Uk)
2dt
(1 + Tkt)2 = ∫ 9Uk/10

0
 dt
(1 + Tkt)2 + O(∫ Uk

9Uk/10
 dt
(1 + Tkt)2 ) = 1 + O(k−1/2)
k log k ,(8.25)
 ∫ ∞

0
 ψ(t/2)
2dt
(1 + Tkt)2 = ∫ 9/5

0
 dt
(1 + Tkt)2 + O(∫ 2

9/5
 dt
(1 + Tkt)2 ) = 1 + O(k−1)
k log k .(8.26)

From these bounds it follows immediately that k−2Jk(F2) ≪ Jk(F1) and k−2Ik(F2) ≪ Ik(F1)
and

(8.27) Jk(F1)
Ik(F1) = log k
4k
 (
1 + O( 1
log k
 )).

Combining these statements gives the bounds of the Lemma. □

9. Proof of Propositions

We see that Lemmas 8.1, 8.5 and 8.6 verify the claims at the end of Proposition 6.1 for
wn given by (7.6). We are therefore left to establish the four main claims of Proposition 6.1,
which we now do in turn. To obtain results with the desired uniformity in k, we need to
perform calculations in a slightly diﬀerent manner to the corresponding ones in [13].

Proposition 9.1. Let wn be as described in Section 7. Then we have
∑

n∈A(x) wn = (1 + O( 1
(log x)1/10 )) Bk

ϕ(B)k SB(L)#A(x)(log R)
kIk(F).

The implied constant depends only on θ, α and the implied constants from (7.1) and (7.2).

DENSE CLUSTERS OF PRIMES IN SUBSETS 21

Proof. We recall W = ∏p≤2k2,p∤B p < exp((log x)
2/5), and consider the summation over n in
the residue class v0 (mod W). If (
∏k
i=1 Li(v0), W) , 1 then we have wn = 0, and so we restrict
our attention to v0 with (
∏k
i=1 Li(v0), W) = 1. We substitute the deﬁnition (7.6) of wn, expand
the square and swap order of summation. This gives
∑

n∈A(x)
n≡v0 (mod W)
 wn = ∑

d,e∈Dk λdλe ∑

n∈A(x)
n≡v0 (mod W)
[di,ei]|Li(n)∀i
 1.(9.1)

By our choice of support of the λd, there is no contribution unless (diei, d je j) = 1 for all i , j.
In this case, given d, e ∈ Dk (so in particular (d je j, a jW) = 1 for 1 ≤ j ≤ k), we can combine
the congruence conditions by the Chinese remainder theorem, and see that the inner sum is
A(x; q, a) for some a and for q = W[d, e]. We let E(1)
q = maxa |#A(x; q, a) − #A(x)/q|, and
substitute #A(x; q, a) = #A(x)/q + O(E(1)
q ) into (9.1).
We ﬁrst show the contribution from the errors E(1)
q are small. There are O(τ3k(q)) ways of
writing q = W[d, e] and all such q are square-free, coprime to B and less than R2W < x
θ

(since λd is supported on d < R ≤ x
θ/3). Since |λd| ≪ (log x)
k by Lemma 8.5, these contribute
∑

d,e∈Dk |λdλe|E(1)
q ≪ (log x)
2k ∑

q<R2W,(q,B)=1 µ
2(q)τ3k(q)E(1)
q

≪ (log x)
2k( ∑

q<R2W,(q,B)=1 µ
2(q)τ3k(q)
2E(1)
q )1/2( ∑

q<R2W,(q,B)=1 µ
2(q)E(1)
q )1/2.(9.2)

We apply Hypothesis 1 to estimate these terms. Using E(1)
q ≪ #A(x)/q for the ﬁrst sum, and
the average of E(1)
q for the second sum, we see the contribution is

≪ (log x)
2k(#A(x) ∑

q<R
 τ9k2(q)
q
 )1/2( #A(x)
(log x)100k2 )1/2 ≪ #A(x)
W(log x)2k2 .(9.3)

By Lemma 8.1 and Lemma 8.6, we see that this is o(#A(x)SB(L)Ik(F)/W), and so will be
negligible compared with our main term.
We now consider the main term. We substitute our expression (7.9) for λd in terms of yr to
give

(9.4) #A(x)
W
 ∑′

d,e∈Dk
 λdλe
[d, e] = #A(x)
W
 ∑

r,s∈Dk
 yrys
ϕω(r)ϕω(s)
 ∑′

d|r,e|s
 µ(d)µ(e)de
[d, e] ,

where ∑′ indicates the restriction that (diei, d je j) = 1 for all i , j. By multiplicativity, we can
write the inner sum as ∏p|rs S p(r, s), where, for r, s such that p|rs and yrys , 0, we have

(9.5) S p(r, s) = ∑′

d|r,e|s
di,ei|p∀i
 µ(d)µ(e)de
[d, e] =
 


p − 1, p|(r, s),
−1, p|r, p|s, p ∤ (r, s),
0, (p|r and p ∤ s) or (p|s and p ∤ r).

(We remind the reader that in our notation, r = ∏k
i=1 ri and that (r, s) = ∏k
i=1(ri, si), and
similarly for e, d, s.)
Since ∏p|rs S p(r, s) = 0 if there is a prime p which divides one of r, s but not the other, we
can restrict to r = s. We let A = A(r, s) = r/(r, s) be the product of primes dividing r but
not (r, s), so that ∏p|rs S p(r, s) = µ(A)ϕ(r)/ϕ(A). Given a choice of r ∈ Dk and A|r, for each
prime p|A there are ω(p) − 1 possible choices of which components of s can be a multiple of

22 JAMES MAYNARD

p (since there are ω(p) indices j for which p ∤ W j, but for one of these we have p|r j), and so∏p|A(ω(p) − 1) choices of s. By Lemma 8.2, for each such choice we have

(9.6) ys = yr + O(
Tk(Yr + Ys)log A
log R
 ).

Thus our main term becomes

(9.7) #A(x)
W
 ∑

r∈Dk
 yrϕ(r)
ϕω(r)2 ∑

A|r
 (∏

p|A
 −(ω(p) − 1)
p − 1
 )(
yr + O(
Tk(Yr + Ys)log A
log R
 ))
.

Since yr ≤ Yr/k and YrYs ≪ Y 2
r + Y 2
s , the contribution of the error here is

≪ Tk
k #A(x)
W
 ∑

r∈Dk
 ϕ(r)Y 2
r
ϕω(r)2 ∑

A|r
 ω(A)
ϕ(A)
 ∑

p|A
 log p
log R

≪ Tk
k #A(x)
W log R
 ∑

p>2k2 log p ∑

(A,W B)=1
p|A
 ω(A)
ϕ(A)
 ∑

r∈Dk
A|r
 ϕ(r)Y 2
r
ϕω(r)2 .(9.8)

We let r
′ be the vector formed by removing from r any factors of A, so r′
i = ri/(ri, A). Since
Yr is decreasing, we have Yr′ ≥ Yr. Given r
′, there are O(ω(A)) possible choices of r. Thus,
swapping the summation to r
′, and letting A = pA′, we obtain the bound

≪ Tk
k #A(x)
W log R
 ( ∑

p>2k2
 ω(p)
2 log p
ϕω(p)2 )( ∑

(A′,W B)=1
 ω(A′)
2

ϕω(A′)2 )( ∑

r′∈Dk
 ϕ(r′)Y 2
r′
ϕω(r′)2 )
.(9.9)

The ﬁrst two terms in parentheses can both be seen to be O(1), since all prime factors are
greater than 2k2. We estimate the ﬁnal term by Lemma 8.4 (taking ΩG = O(T 2
k )). This gives
a bound for (9.9) of size

≪ TkW k−1Bk(log R)
k−1SW B(L)
2#A(x)
kϕ(W B)k ∏

p∤W B

(
1 + ω(p)(p − 1)
(p − ω(p))2 )(
1 − 1
p
 )kIk(F2).(9.10)

We note that

(9.11) ∏

p∤W B

(1+ ω(p)(p − 1)
(p − ω(p))2 )(1− 1
p
 )k = ∏

p∤W B

(
1+ ω(p)
p − ω(p)
)(
1+O( k2

p2 ))(1− 1
p
)k ≪ SW B(L)
−1,

since the product is only over primes p > 2k2. Using Ik(F2) ≪ k2Ik(F) from Lemma 8.6, we
see that (9.10) is

(9.12) ≪ kTkW k−1BkSW B(L)#A(x)(log R)
k−1

ϕ(W B)k Ik(F).

This is negligible, and can be absorbed into the error term in the statement of the Lemma. We
now consider the main term. We have

(9.13) #A(x)
W
 ∑

r∈Dk
 y
2
rϕ(r)
ϕω(r)2 ∑

A|r
 ∏

p|A
 −(ω(p) − 1)
p − 1 = #A(x)
W
 ∑

r∈Dk
 y
2
r
ϕω(r).

DENSE CLUSTERS OF PRIMES IN SUBSETS 23

We estimate the inner sum here by applying Lemma 8.4 (again with ΩG = T 2
k ). This gives
∑

r∈Dk
 y
2
r
ϕω(r) = W kBkSW B(L)
2

ϕ(W B)k (log R)
k ∏

p∤W B

(
1 + ω(p)
p − ω(p)
)(
1 − 1
p
 )kIk(F)

+ O(W kBkSW B(L)
2

ϕ(W B)k (log R)
k ∏

p∤W B

(
1 + ω(p)
p − ω(p)
)(1 − 1
p
 )k kT 2
k log log R
log R Ik(F1)
)

= W kBkSW B(L)
ϕ(W B)k (log R)
k(
1 + O(kT 2
k log log R
log R
 ))Ik(F).(9.14)

In the last line we have used the fact Ik(F1) ≪ Ik(F) given by Lemma 8.6. Putting this all
together (and recalling k ≤ (log x)
1/5 and Tk = k log k), we have shown that

(9.15) ∑

n∈A(x)
n≡v0 (mod W)
 wn = (
1 + O( 1
(log x)1/10 )) W k−1BkSW B(L)#A(x)
ϕ(W B)k (log R)
kIk(F).

Summing this over the ϕω(W) residue classes v0 (mod W) such that (
∏k
i=1 L(v0), W) = 1 then
gives the result. □

Proposition 9.2. Let wn be as described in Section 7. Let L(n) = amn + bm ∈ L satisfy
L(n) > R for n ∈ [x, 2x] and

(9.16) ∑

q≤xθ
(q,B)=1
 max
(L(a),q)=1
∣∣∣∣#PL,A(x; q, a) − #PL,A(x)
ϕL(q)
 ∣∣∣∣ ≪ #PL,A(x)
(log x)100k2 .

Then we have
∑

n∈A(x) 1P(L(n))wn = (1 + O( 1
(log x)1/10 )) Bk−1

ϕ(B)k−1 SB(L)#PL,A(x)(log R)
k+1Jk(F) ∏

p|am
p∤B
 p − 1
p

+O( Bk

ϕ(B)k SB(L)#A(x)(log R)
k−1Ik(F)
).

The implied constants depend only on θ, α and the implied constants from (7.1), (7.2) and
(9.16).

Proof. Again we split the sum into residue classes n ≡ v0 (mod W). If (
∏k
i=1 Li(v0), W) , 1
then we have wn = 0, and so we restrict our attention to v0 with (
∏k
i=1 Li(v0), W) = 1. We
substitute the deﬁnition (7.6) of wn, expand the square and swap order of summation. This
gives

(9.17) ∑

n∈A(x)
n≡v0 (mod W)
 1P(L(n))wn = ∑

d,e∈Dk λdλe ∑

n∈A(x)
n≡v0 (mod W)
[di,ei]|Li(n)∀i
 1P(L(n)).

We ﬁrst show that there is no contribution to our sum from λd for which (d j, a jbm − amb j) , 1
for some j , m. If p|d j then the inner sum requires that p|a jn + b j. However, if we also have
p|a jbm − b jam then this means p|amn + bm (since (a j, b j) = 1 by admissibility of L). Since
there is no contribution to our sum unless L(n) = Lm(n) = amn + bm is a prime and since
d j < R < L(n) by the support of λd and assumption of the Lemma, we see that there is no
contribution from λd with (d j, a jbm − amb j) , 1.

24 JAMES MAYNARD

Thus we may restrict the support of λd to D′
k, deﬁned by

D′
k = {d ∈ R
k : µ
2(d) = 1, (d j, W ′
j) = 1∀ j}, W ′
j = ∏

p|W j(a jbm−amb j) p.(9.18)

We write λ′
d for λd with this restricted support. We see from this that p|W ′
j/W j iﬀ p ∤ am and
j was the chosen index for the residue class −bmam (mod p). (For our ﬁxed set of choices of
residue classes given in Section 7.)
We now observe that given d, e ∈ D′
k, the inner sum of (9.17) is empty unless (diei, d je j) = 1
for all i , j (since otherwise the divisibility conditions are incompatible). If (diei, d je j) =
1∀i , j, then we can combine the conditions by the Chinese remainder theorem. This shows
the sum is #PL,A(x; q, a) for q = W[d, e] and some a. We note #PL,A(x; q, a) , 0 iﬀ (L(a), q) =
1, which occurs iﬀ dm = em = 1. For such a choice of d, e, we write #PL,A(x; q, a) =
#PL,A(x)/ϕL(q) + O(E(2)
q ), where E(2)
q = max(a,q)=1 |#PL,A(x; q, a) − #PL,A(x)/ϕL(q)|.
We treat the error term E(2)
q in the same manner as we treated E(1)
q in the proof of Proposition
9.1. We note that for all d, e ∈ D′
k we have (q, B) = 1, allowing us to use Proposition 6.1 for
the average of E(2)
q . We also note that trivially #PL,A(x; q, a) ≪ #A(x; q, a), which gives us the
bound E(2)
q ≪ #A(x)/ϕL(q). Thus the same argument shows that these error terms contribute
O(#A(x)W −1(log x)
−2k2 ).
We now consider the main term, given by

(9.19) #PL,A(x)
ϕL(W)
 ∑′

d,e∈D′
k
dm=em=1
 λ′
dλ′
e
ϕL([d, e]) ,

where we recall ∑′ indicates the sum is restricted to (diei, d je j) = 1 for all i , j. We change
variables to y
(m)
r , satisfying

(9.20) y
(m)
r = µ(r)ϕω(r) ∑

r|d,dm=1
 λ′
d
ϕL(d), λ′
d = µ(d)ϕL(d) ∑

d|r
 y
(m)
r
ϕω(r).

We see from (9.20) that yr are supported on r ∈ D′
k with rm = 1. Substituting our expression
(9.20) for λ′
d into our main term (9.19) gives

(9.21) #PL,A(x)
ϕL(W)
 ∑′

d,e
dm=em=1
 λ′
dλ′
e
ϕL([d, e]) = #PL,A(x)
ϕL(W)
 ∑

r,s
 y
(m)
r y
(m)
s
ϕω(r)ϕω(s)
 ∏

p|rs S (m)
p (r, s),

where now, if r and s are such that y
(m)
r y
(m)
s , 0 (so rm = sm = 1) and p|rs, we have

(9.22) S (m)
p (r, s) = ∑′

d|r,e|s
di,ei|p∀i
dm=em=1
 µ(d)µ(e)ϕL(d)ϕL(e)
ϕL([d, e]) =
 


p − 2, p|(r, s), p ∤ am
p − 1, p|(r, s), p|am
−1, p|r, p|s, p ∤ (r, s),
0, (p|r and p ∤ s) or (p|s and p ∤ r),

so again we may restrict to r = s. We use the following lemma to relate y
(m)
r to yr.

Lemma 9.3. Let r ∈ D′
k with rm = 1, and let ti = log ri/ log R for i , m. Then we have

y
(m)
r = log R ϕ(amW B)W k−1Bk−1SW B(L)
amϕ(W B)k
 ∫ ∞

0 H(t1, . . . , tk)dtm

DENSE CLUSTERS OF PRIMES IN SUBSETS 25

where
 H(t1, . . . , tk) = F(t1, . . . , tk) + O(Tk(log log R)
2

log R F2(t1, . . . , tk)
).

We ﬁrst complete the proof of Proposition 9.2, and then establish the lemma. Given r, s ∈
D′
k with rm = sm = 1 and r = s, let A = A(r, s) be the product of primes dividing r but not
(r, s). Analogously to Lemma 8.2, we have (for A > 1)

y
(m)
r = y
(m)
s + O( Tk
k (Yr + Ys)ϕ(amW B)
amW B (log A + (log log R)
2)
)

= y
(m)
s + O( Tk
k (Yr + Ys)ϕ(amW B)
amW B (log A)(log log R)
2)
.(9.23)

Substituting this into our main term (9.21), we are left to estimate
∑

r,s∈D′
k
rm=sm=1
r=s
 y
(m)
r
ϕω(r)2 ∏

p|rs S (m)
p (r, s)
(
y
(m)
r + O( Tk
k (Yr + Ys)ϕ(amW B)
amW B (log A)(log log R)
))
.(9.24)

We note that for r = s the value of ∏p|rs S (m)
p (r, s) depends only on r and A. Substituting this
value for S (m)
p (r, s) gives a main term

(9.25) ∑

r∈D′
k
rm=1
 (y
(m)
r )
2

ϕω(r)2 (∏

p|r (ϕL(p) − 1)
) ∑

A|r
 (∏

p|A
 −1
ϕL(p) − 1
 ) ∑

s∈D′
k
A(r,s)=A
 1,

and (using y
(m)
r ≤ Yr(log R)/k and YrYs ≤ Y 2
r + Y 2
s ) an error term of size

≪ Tkϕ(amW B)
2 log R
k2a2
mB2W 2 ∑

r∈D′
k
rm=1
 Y 2
r ∏p|r(ϕL(p) − 1)
ϕω(r)2 ∑

A|r
 log A
∏p|A(ϕL(p) − 1)
 ∑

s∈D′
k
A(r,s)=A

(log log R)
2.

(9.26)

We ﬁrst estimate the inner sum over s which occurs in both terms. We ﬁx a choice of r ∈ D′
k
and A = A(r, s) with A|r. For each prime p|A, we count how many components of s can be a
multiple of p, subject to the constraints that p ∤ (si, ri) and p ∤ (si, W ′
i ) for all i. If p|A, p ∤ am
then there are ω(p) − 2 possible choices of which component of s can be a multiple of p (there
are ω(p) − 1 indices j , m for which p ∤ W ′
j, but for one of these indices p|r j). If p|A and
p|am, then instead there are ω(p) − 1 choices (since there are ω(p) indices j , m for which
p ∤ W ′
j, but for one of these indices p|r j). Thus we have
∑

s∈D′
k
A(r,s)=A
 1 = ∏

p|A,p∤am(ω(p) − 2) ∏

p|A,p|am(ω(p) − 1).(9.27)

We now consider the error term (9.26). We follow an analogous argument to that in the proof
of Proposition 9.1. Substituting our expression (9.27) for the inner sum, and crudely bounding
the multiplicative functions gives a bound

≪ Tkϕ(amW B)
2(log R)(log log R)
2

k2a2
mB2W 2 ∑

(A,W B)=1 log A ω(A)
ϕω(A)2 ∑

r∈D′
k
rm=1
A|r
 Y 2
r ϕ(r/A)
ϕω(r/A)2 .(9.28)

26 JAMES MAYNARD

We let r
′ be given by r′
i = ri/(ri, A) and see Yr′ ≥ Yr. Moreover, we see that there are O(ω(A))
choices of r given r
′. Therefore we obtain the bound
∑

(A,W B)=1 log A ω(A)
ϕω(A)2 ∑

r∈D′
k
rm=1
A|r
 Y 2
r ϕ(r/A)
ϕω(r/A)2 ≪ ( ∑

(A,W B)=1 log A ω(A)
2

ϕω(A)2 ) ∑

r′∈Dk
r′
m=1
 Y 2
r′ϕ(r′)
ϕω(r′)2 .(9.29)

Here dropped the requirement that (r′, A) = 1 for an upper bound. We substitute log A =∑p|A log p, A = pA′, and swap the order of summation. This shows the right hand side of
(9.29) is
 ≪ ( ∑

p>2k2
 ω(p)
2 log p
ϕω(p)2 )( ∑

(A′,W B)=1
 ω(A′)
2

ϕω(A′)2 )( ∑

r
′∈D
′
k
rm=1
 ϕ(r′)Y 2
r′
ϕω(r′)2 )
.(9.30)

The ﬁrst two sums are seen to be O(1) since they only involve primes p > 2k2. The ﬁnal sum
we estimate using Lemma 8.4. This gives a bound for (9.30) of

≪ W k+1Bk+1SW B(L)
2(log R)
k−1

ϕ(W B)k+1 ∏

p∤W B

(
1 + ω(p) − 1
p + O(k)
 )(
1 − 1
p
 )k−1

× (

t1,...,tk≥0,tm=0 F2(t1, . . . , tk)
2 ∏

i,m dti.(9.31)

We see that the product is O(SW B(L)
−1) analogously to (9.11). We also have, from the deﬁ-
nition (7.12) of F2
(9.32)(

t1,...,tk≥0,tm=0 F2(t1, . . . , tk)
2 ∏

i,m dti ≤ k2(∫ ∞

0
 ψ(t/Uk)
2dt
(1 + Tkt)2 )k−2(∫ ∞

0
 ψ(t/2)
2dt
(1 + Tkt)2 ) ≪ k2T 2
k Jk(F).

Putting this together, the contribution of the error term to (9.24) is

≪ T 3
k ϕ(amW B)
2W k−1Bk−1SW B(L)(log R)
k(log log R)
2

a2
mϕ(W B)k+1 Jk(F),(9.33)

which contributes only to the error term in the statement of the Lemma.
We now consider the main term in (9.24), given by (9.25). Substituting our expression
(9.27) for the inner sum, and evaluating the sum over A gives
∑

r∈Dk
rm=1
 (y
(m)
r )
2

ϕω(r)2 (∏

p|r (ϕL(p) − 1)
) ∑

A|r
 (∏

p|A
 −1
ϕL(p) − 1
 ) ∑

s∈D′
k
A(r,s)=A
 1 = ∑

r∈D′
k
rm=1
 (y
(m)
r )
2

ϕω(r) .(9.34)

We evaluate this sum using Lemma 8.4. This gives

∑

r∈D
′
k
rm=1
 (y
(m)
r )
2

ϕω(r) = ∏

p∤am BW
(1 + ω(p) − 1
ϕω(p)
 )(1 − 1
p
 )k−1 ∏

p|am,p∤W B

(
1 + ω(p)
ϕω(p)
 )(
1 − 1
p
 )k−1

× (log R)
k+1 ϕ(amW B)
2W k−1Bk−1SW B(L)
2

a2
mϕ(W B)k+1 (Jk(H) + O(kT 2
k (log log R)
2

log R Jk(F1)
)).(9.35)
 DENSE CLUSTERS OF PRIMES IN SUBSETS 27

By Lemma 8.6, we have Jk(F1) ≫ Jk(F). From the deﬁnition of H, we have

Jk(H) = Jk(F + O( Tk log log R
log R F2)) = Jk(F) + O( Tk log log R
log R Jk(F2)
)

= Jk(F)
(1 + O(k2Tk log log R
log R
 )).(9.36)

We recall k ≤ (log x)
1/5 and Tk = k log k, so the errors appearing are o((log x)
−1/10). Therefore,
simplifying the products in (9.35) gives

(9.37) ∑

r∈D′
k
rm=1
 (y
(m)
r )
2

ϕω(r) = (1 + ( 1
(log x)1/10 ))
(log R)
k+1 W k−1Bk−1SW B(L)
ϕ(W B)k−1 Jk(F) ∏

p|am,p∤W B
 p − 1
p .

Thus, putting everything together, we have
∑

n∈A(x)
n≡v0 (mod W)

1P(L(n))wn = #PL,A(x)
ϕL(W)
 ∑′

d,e
dm=em=1
 λ′
dλ′
e
ϕL([d, e]) + O( #A(x)
W(log x)2k2 )

= (
1 + O( 1
(log x)1/10 ))(log R)
k+1 W k−1Bk−1SW B(L)#PL,A(x)
ϕ(W B)k−1ϕL(W) Jk(F) ∏

p|am,p∤W B
 p − 1
p

+ O( #A(x)
W(log x)2k2 ).(9.38)

Summing over the ϕω(W) residue classes v0 (mod W) then gives the result (recalling (W, B) =
1). □

We now return to prove Lemma 9.3.

Proof of Lemma 9.3. We substitute our expression (7.9) for λd into the deﬁnition (9.20) of
y
(m)
r . For rm = 1 and r ∈ D′
k, we obtain

y
(m)
r = µ(r)ϕω(r) ∑

d∈D′
k
r|d,dm=1
 λd
ϕL(d) = µ(r)ϕω(r) ∑

r|e
 ye
ϕω(e)
 ∑

d∈D′
k
r|d,d|e,dm=1
 µ(d)d
ϕL(d)

= rϕω(r)
ϕL(r)
 ∑

r|e
 ye
ϕω(e)
 ∏

p|e/r S ′(m)
p (e, r),(9.39)

where if p|em then S ′(m)
p (e, r) = 1 and if p|e j/r j with j , m, we have

(9.40) S ′(m)
p (e, r) = ∑

d∈D′
k
d j|(e j/r j,p),dm=1
 µ(d)d
ϕL(d) =
 


−1/(p − 1), p ∤ amW ′
j,
0, p|am, p ∤ W ′
j,
1, p|W ′
j/W j.

(Since e ∈ Dk, we have (e j, W j) = 1 and so if p|e j/r j we only need consider p ∤ W j.)
We let e j = r js jt j for each j , m, where s j is the product of primes dividing e j/r j but not
W ′
j, and t j is the product of primes dividing both e j/r j and W ′
j/W j. We put sm = tm = 1, and
consider em separately.
We can restrict to the case when (s j, am) = 1 for all j, since otherwise the product of
S ′(m)
p (e, r) vanishes. For e ∈ Dk, the product in (9.39) is then µ(s)/ϕ(s) by (9.40). Since

28 JAMES MAYNARD

(am, W ′
j/W j) = 1 for all j, we can also restrict to (t j, am) = 1 for all j. (If p|W ′
j/W j then
p|amb j − a jbm, so if p|am and p|W ′
j/W j, then p|a j and hence p|W j, meaning p ∤ W ′
j/W j).
We let r
′ = (r1, . . . , rm−1, em, rm+1, . . . , rk). By Lemma 8.2, we have

(9.41) ye = yr′ + O(
TkYr′ log st
log R
 )
.

Substituting this into (9.39) gives

(9.42) y
(m)
r = r
ϕL(r)
 ∑

em
 yr′
ϕω(em)
 ∑

s,t
 µ(s)
ϕ(s)ϕω(st) + O( Tkr
ϕL(r) log R
 ∑

em
r′∈Dk
 Yr′
ϕω(em)
 ∑

s,t
 log st
ϕ(s)ϕω(st)
),

where the sum is over s ∈ D′
k, t ∈ Dk subject to sm = tm = 1, (s, t) = (st, remam) = 1, and
t j|W ′
j/W j.
We ﬁrst estimate the error term from (9.42). We have log st ≪ s1/2(1 + log t), and we
drop the requirement that (s, t) = 1. The sum over s then factorizes as an Euler product,
which can be seen to be O(1) since there are O(ω(u)) choices of s with s = u, and we only
consider primes p > 2k2. We are summing over square-free t|∆ = ∏k
i=1(ambi − aibm) with
(t, W Bremam) = 1, and for every such t there is at most one possible t (since for every prime
p|t with p|Wm there is a unique index j such that p|W ′
j/W j, and if p ∤ Wm there is no such
index). Thus the sum over t contributes at most
∑

t∈Dk:t|∆
 1 + ∑p|t log p
ϕω(t) ≪ (
1 + ∑

p>2k2:p|∆
 log p
p
 ) ∏

p>2k2:p|∆
(
1 + 1
ϕω(p)
 )

≪ (log log ∆)
2 ≪ (log log R)
2,(9.43)

since both sum and product are largest if ∆ is composed of primes ≪ log ∆, and ∆ ≪ x
O(k).
Thus, relaxing the constraint (em, rWm) = 1 to (em, amW Br) = 1, and using Lemma 8.4 to
estimate the sum over em, we see the error contributes a total

≪ Tk(log log R)
2

log R r
ϕL(r)
 ∑

(em,amW Br)=1
 Yr′
ϕω(em)

≪ Tk(log log R)
2ϕ(amW B)W k−1Bk−1SW B(L)
amϕ(W B)k
 ∫ ∞

0 F2(t1, . . . , tk)dtm.(9.44)

We now return to the main term from (9.42). We ﬁrst consider the inner sum, which by
multiplicativity we can rewrite as a product

(9.45) ∑∗

s,t
 µ(s)
ϕ(s)ϕω(st) = ∏

p
 ∑∗

s,t
si|p,ti|p∀i
 µ(s)
ϕ(s)ϕω(st),

where the asterisk indicates that sums are subject to the additional constraints that sm = tm = 1,
(s, t) = 1 and that (si, W ′
i remam) = 1, (ti, Wiremam) = 1, and ti|W ′
i /Wi for all 1 ≤ i ≤ k. Since
the summand only depends on s and t we can evaluate it by counting how many pairs s, t
correspond to a given choice of s, t.
If p|W Bremam then no component of s or t can be a multiple of p. If p ∤ W Bremam
then there are ω(p) − 1 components of s which can be a multiple of p (corresponding to the
indices for all residue classes chosen mod p except for the index corresponding to −bmam). If
p ∤ Wmrem then no components of t can be a multiple of p (p ∤ Wm means m was the chosen
index for the residue class −bmam (mod p), so p ∤ W ′
j/W j for any j). If p|Wm, p ∤ W Bram

DENSE CLUSTERS OF PRIMES IN SUBSETS 29

then exactly one component of t can be a multiple of p (t j can be a multiple of p if j was the
chosen index for the residue class −bmam (mod p), and this occurs for the unique j such that
p|W ′
j/W j). Finally, since (s, t) = 1, no component of s can be a multiple of p if t is a multiple
of p. Putting this together, we obtain (since (em, rWm) = 1)
∑∗

s,t
 µ(s)
ϕ(s)ϕω(st) = ∏

p|Wm,p∤W Bram
(
1 − ω(p) − 1
ϕ(p)ϕω(p) + 1
ϕω(p)
 ) ∏

p∤Wmrem
(
1 − ω(p) − 1
ϕ(p)ϕω(p)
)

= ∏

p|Wm,p∤W Bram
 p
p − 1
 ∏

p∤Wmr
( p
p − 1 − 1
ϕω(p)
 ) ∏

p|em
 ( p
p − 1 − 1
ϕω(p)
 )−1.(9.46)

Now, using Lemma 8.3, we estimate the summation over em. This gives
∑

(em,rWm)=1
 yr′
ϕω(em)
 ∏

p|em
 ( p
p − 1 − 1
ϕω(p)
)−1

= log R SW B(L)W kBk

ϕ(W B)k ∏

p|rWm
(1 − 1
p
 ) ∏

p∤rWm
( p
p − 1 − 1
ϕω(p)
)−1 ∫ ∞

0 H(t1, . . . , tk)dtm,(9.47)

where we have written ri = Rti for i , m to simplify notation, and where

H(u1, . . . , uk) = F(u1, . . . , uk) + O(Tk(log log R)
2

log R F2(u1, . . . , uk)
)
.

We have added an additional factor of log log R into the error term for H so we can absorb
(9.44) into the error term.
Thus, combining (9.46) and (9.47) gives
r
ϕL(r)
 ∑

em
 yr′
ϕω(em)
 ∑

s,t
 µ(s)
ϕ(s)ϕω(st)

= log R W kBkSW B(L)
ϕ(W B)k r
ϕL(r)
 ∏

p|r
 (1 − 1
p
 ) ∏

p|W Bam
p∤r
 (
1 − 1
p
 ) ∫ ∞

0 H(t1, . . . , tk)dtm

= log R ϕ(amW B)W k−1Bk−1SW B(L)
amϕ(W B)k
 ∫ ∞

0 H(t1, . . . , tk)dtm.(9.48)

Here we have used the fact r ∈ D′
k, and so (r, W B) = 1. Combining (9.44) and (9.48) gives
the result. □

Proposition 9.4. Let wn be as described in Section 7. Given D, ξ satisfying D ≤ x
α, and
k(log log x)
2/(log x) ≤ ξ ≤ θ/10 let

S(ξ; D) = {n ∈ N : p|n =⇒ (p > x
ξ or p|D)}.

For L = a0n + b0 < L, with |a0|, |b0| ≤ x
α and ∆L , 0, we have
∑

n∈A(x) 1S(ξ;D)(L(n))wn ≪ ξ−1 ∆L
ϕ(∆L) D
ϕ(D) Bk

ϕ(B)k SB(L)#A(x)(log R)
k−1Ik(F),

where
 ∆L = |a0|
 k∏

i=1 |a jb0 − a0b j|.

The implied constant depends only on θ, α and the implied constants from (7.1) and (7.2).

30 JAMES MAYNARD

Proof. We ﬁrst split the sum into residue classes v0 modulo V = ∏p≤2k2 p for which L(v0)
is coprime to ∏p≤2k2,p∤D p and each of the Li(v0) are coprime to W (the other residue classes
make no contribution because of the support of wn and 1S(ξ;D)). We use the Selberg sieve
upper bound

(9.49) 1S(ξ;D)(L(n)) ≤ ˜λ−2
1 ( ∑

d0|L(n)
d0<xξ
(d0,D)=1
 ˜λd0)2.

(This holds for any choice of the values of ˜λd ∈ R with ˜λ1 , 0). For the residue class v0
(mod V), this gives

(9.50) ∑

n∈A(x)
n≡v0 (mod V)
 1S(ξ;D)(L(n))wn ≤ 1
˜λ2
1
 ∑

n∈A(x)
n≡v0 (mod V)

( ∑

d0|L(n)
(d0,D)=1,d0<xξ
 ˜λd0)2( ∑

di|Li(n) λd)2.

We restrict the support of ˜λd0 in a similar way to that of λd. We force ˜λd0 = 0 if p|d0 for any
prime with p|W0 where

(9.51) W0 = DV∆L.

Similarly, we force ˜λd0 = 0 if d0 > x
ξ. Note that we allow ˜λd0 , 0 if (d0, B) , 1.
We return to (9.50). Expanding the squares and swapping the order of summation gives

(9.52) 1
˜λ2
1
 ∑

n∈A(x)
n≡v0 (mod V)

( ∑

d0|L(n) ˜λd0)2( ∑

di|Li(n) λd)2 = ˜λ−2
1 ∑

d0,e0
(d0e0,W0)=1
 ˜λd0 ˜λe0 ∑

d,e∈Dk λdλe ∑

n∈A(x)
n≡v0 (mod V)
[di,ei]|Li(n)∀0≤i≤k
 1.

We see that by our restrictions on the support of λd, ˜λd0, there is no contribution to (9.52)
unless d0, e0, d, e are such that (diei, d je j) = 1 for all 0 ≤ i , j ≤ k, and d, e < R and
d0, e0 < x
ξ. (To avoid confusion, we recall that d = ∏k
i=1 di and e = ∏k
i=1 ei). For such
values, we can combine the congruence conditions using the Chinese remainder theorem,
which shows the inner sum is #A(x; q, a) for some a and q = V ∏k
i=0[di, ei]. We see that
q < VR2x
2ξ < x
θ since ξ ≤ θ/10. We substitute #A(x; q, a) = #A(x)/q + O(E(1)
q ), and the
contribution from E(1)
q can be seen to be negligible by an identical argument to that in the
proof of Proposition (9.1). We are therefore left to evaluate

(9.53) #A(x)
V ˜λ2
1
 ∑

d0,e0
(d0,e0,W0)=1
 ˜λd0 ˜λe0
[d0, e0]
 ∑′

d,e∈Dk
(de,d0e0)=1
 λdλe
[d, e] .

We let ω∗ be the totally multiplicative function deﬁned by

(9.54) ω∗(p) =
 

#{1 ≤ n ≤ p : L(n) ∏k
i=1 Li(n) ≡ 0 (mod p)}, p ∤ B,
1, p|B.

We note that with this choice, ω∗(p) = ω(p) if p|∆L and p ∤ B, and ω∗(p) = ω(p) + 1
otherwise. We also deﬁne

(9.55) yr,r0 = µ(r0r)ϕw∗(r0r) ∑

r|d
r0|d0
(d0,d)=1
 λd ˜λd0
dd0 , ˜yr0 = µ(r0)ϕ(r0) ∑

r0|d0
 ˜λd0
d0 .

DENSE CLUSTERS OF PRIMES IN SUBSETS 31

By Moebius inversion, we see that this deﬁnition of ˜yr0 implies that

(9.56) ˜λd0 = µ(d0)d0 ∑

r0|d0
 ˜yr0
ϕ(r0),

For (r0, W0) = 1 and r0 < x
ξ we choose

(9.57) ˜yr0 = W0
ϕ(W0),

and ˜yr0 = 0 otherwise. This gives rise to a suitable choice of ˜λd0 supported on d0 < x
ξ with
(d0, W0) = 1. Since ξ ≫ k(log log x)
2/(log x), Lemma 8.3 shows that

˜λ1 = ∑

r0<xξ
(r0,W0)=1
 ˜yr0µ
2(r0)
ϕ(r0) = ξ log x + O(log log x) ≫ ξ log x.(9.58)

As in the proof of Proposition 9.1 (this is exactly the same argument but for (k+1)-dimensional
vectors instead of k-dimensional ones) changing variables using (9.55) shows that
∑

d0,e0
 ˜λd0 ˜λe0
[d0, e0]
 ∑′

d,e∈Dk
(de,d0e0)=1
 λdλe
[d, e] = ∑

r,s∈Dk,r0,s0
 yr,r0ys,s0
ϕω∗(rr0)ϕω∗(ss0)
 ∏

p|rr0ss0 S p(r, s, r0, s0),(9.59)

where
 S p(r, s, r0, s0) =
 


p − 1, p|(r, s)(r0, s0),
−1, p|rr0 and p|ss0 but p ∤ (r, s)(r0, s0),
0, (p|rr0 and p ∤ ss0) or (p|ss0 and p ∤ rr0).
(9.60)

Thus we may restrict to rr0 = ss0. Using the bound yr,r0ys,s0 ≪ y
2
r,r0 + y
2
s,s0, we see that (by
symmetry) the right hand side of (9.59) may be bounded by

∑

r,r0
 y
2
r,r0
ϕω∗(rr0)2 ∑

s,s0
ss0=rr0
 ∏

p|rr0 |S p(r, s, r0, s0)| ≤ ∑

r,r0 y
2
r,r0 ∏

p|rr0
 p + ω∗(p) − 2
(p − ω∗(p))2 = ∑

r,r0
 y
2
r,r0∏p|rr0(p + O(k)) .

(9.61)

To evaluate this, we express yr,r0 in terms of yr and ˜yr0. Substituting (7.9) into (9.55), we ﬁnd
that for (r0, rW0) = 1 and r ∈ Dk

yr,r0 = µ(r0r)ϕω∗(r0r) ∑

r0|d0 µ(d0) ∑

d0| f0
 ˜y f0
ϕ( f0)
 ∑

r|d
(d,d0)=1
 µ(d) ∑

d|f
 yf
ϕω( f )

= µ(r0r)ϕω∗(r0r) ∑

r|f,r0| f0
 yf ˜y f0
ϕω( f )ϕ( f0)
 ∑

r0|d0,d0| f0
r|d,d|f
(d,d0)=1
 µ(d)µ(d0).(9.62)

The inner sum is 0 unless every prime dividing one of f, f0 but not the other is a divisor of
rr0. In this case the sum is ±1. Thus, using the fact that yr ≥ yf and ˜yr0 ≥ ˜y f0 (since F is
decreasing), we have the crude bound

(9.63) yr,r0 ≤ ϕω∗(r0r)yr ˜yr0 ∑

r0| f0
( f0,W0)=1
 ∑

r|f∈Dk
p∤( f, f0)⇒p|rr0
 µ
2( f0)
ϕ( f0)ϕω( f ).

32 JAMES MAYNARD

We let f0 = r0 f ′
0g0 and fi = ri f ′
i gi for 1 ≤ i ≤ k, where f ′
i = fi/( fi, rr0) is fi with any factors
of rr0 removed, g0|r and gi|r0 for 1 ≤ i ≤ k. We see the constraint p ∤ ( f, f0) ⇒ p|rr0 means
that f ′
0 = ∏k
i=1 f ′
i . Therefore we can bound the double sum above by

1
ϕ(r0)ϕω(r)
 ∑

f′∈Dk
 1
ϕ( f ′)ϕω( f ′)
 ∑

g∈Dk
gi|r0∀1≤i≤k
 1
ϕω(g)
 ∑

g0|r
(g0,W0)=1
 1
ϕ(g0)

= 1
ϕ(r0)ϕω(r)
 ∏

p∤W B

(
1 + ω(p)
(p − 1)(p − ω(p))
) ∏

p|r0
 (
1 + ω(p)
p − ω(p)
 ) ∏

p|r,p∤W0
(
1 + 1
p − 1
).(9.64)

The ﬁrst product is O(1) since it is over primes p > 2k2. Thus, simplifying the remaining
products, we obtain

(9.65) yr,r0 ≪ yr ˜yr0( ∏

p|(r,W0)
 p − ω∗(p)
p − ω(p)
 )( ∏

p|rr0,p∤W0
 p(p − ω∗(p))
(p − 1)(p − ω(p))
) ≤ yr ˜yr0.

Here we have used the fact that ω∗(p) = ω(p) + 1 if p ∤ W0.
Recalling the deﬁnitions (9.57) and (7.9) of ˜yr0 and yr, and applying Lemma 8.4, we ﬁnd
that (since ξ ≫ k(log log x)
2/(log x))
∑

r,r0
 (yr,r0)
2
∏p|r0r(p + O(k)) ≪ ( ∑

r0<xξ
(r0,W0)=1
 ˜y
2
r0∏p|r0(p + O(k))
)(∑

r∈Dk
 y
2
r∏p|r(p + O(k))
)

≪ ξ(log R)
k+1 W kBkW0SW B(L)
2

ϕ(W B)kϕ(W0)
 ∏

p∤W0
(
1 + O(k)
p2 ) ∏

p∤W B

(1 + ω(p)
p + O(k)
)(1 − 1
p
 )kIk(F).(9.66)

We note that the ﬁrst product is O(1) and the second product is O(SW B(L)
−1), since all primes
in the products are greater than 2k2 and ω(p) ≤ k. Thus, we obtain (recalling ˜λ1 ≫ ξ log x)

(9.67) #A(x)
V ˜λ2
1
 ∑

r,r0
 (yr,r0)
2
∏p|rr0(p + O(k)) ≪ ξ−1(log R)
k−1#A(x)W0W kBkSW B(L)
Vϕ(W0)ϕ(W B)k Ik(F).

We now sum over residue classes v0 mod V, for which L(v0) is coprime to ∏p≤2k2,p∤D p and
each of the Li(v0) are coprime to W. The number N of such residue classes is given by

(9.68) N = ∏

p|W
p∤D∆L
(p − ω(p) − 1) ∏

p|W
p|D∆L
(p − ω(p)) ∏

p|V/W
p∤Da0
(p − 1) ∏

p|V/W
p|Da0
 p.

This then gives,
∑

n∈A(x) 1S(ξ;D)(L(n))wn ≪ ξ−1 Bk

ϕ(B)k (log R)
k−1#A(x)SW B(L)Ik(F) NW0W k

Vϕ(W0)ϕ(W)k .(9.69)

Finally, by calculation we ﬁnd that

NW0W k

Vϕ(W0)ϕ(W)k = SB(L)∆LD
SW B(L)ϕ(∆LD)
 ∏

p|(∆L,V)
p∤a0W D
 p − 1
p
 ∏

p|W
p∤∆LD
 (p − ω(p) − 1)p
(p − ω(p))(p − 1)

≤ SB(L)∆LD
SW B(L)ϕ(∆L)ϕ(D).(9.70)

This gives the result. □

DENSE CLUSTERS OF PRIMES IN SUBSETS 33

Proposition 9.5. Let wn be as described in Section 7. For L ∈ L and ρ ≤ θ/10, we have
∑

n∈A(x)
( ∑

p|L(n)
p<xρ
p∤B
 1)
wn ≪ ρ2k4(log k)
2SB(L)#A(x)(log R)
kIk(F).

The implied constant depends only on θ, α and the implied constants from (7.1) and (7.2).

Proof. We let L(n) = Lm(n) = amn + bm be the mth function in L. As with Propositions 9.1 and
9.2, we consider the sum restricted to n ≡ v0 (mod W) for some v0 with (
∏k
i=1 Li(v0), W) = 1,
since the other choices of v0 make no contribution. This means we can also restrict the sum
to p ∤ W.
Expanding the square and swapping the order of summation gives

(9.71) ∑

n∈A(x)
n≡v0 (mod W)
( ∑

p|L(n)
p<x
ρ
p∤W B
 1)
wn = ∑

p<xρ
p∤W B
 ∑

d,e∈Dk λdλe ∑

n∈A(x)
[di,ei]|Li(n)
n≡v0 (mod W)
p|Lm(n)
 1.

The inner sum is empty unless (diei, d je j) = 1 for all i , j and (diei, p) = 1 for all i , m.
In this case, by the Chinese remainder theorem, we can combine the congruence conditions
and see that the inner sum is #A(x; q, a) for q = [dm, em, p] ∏
i,m[di, ei] and some a. We write
#A(x; q, a) = #A(x)/q + O(E(1)
q ) as in the proof of Propostion 9.1. We treat the error E(1)
q from
making this change in the same manner as in Proposition 9.1, noting that all moduli q we need
to consider are square-free and satisfy q < WR2x
ρ < x
θ, and for any q there are O(τ3k+4(q))
choices of d, e, p which give rise to the modulus q. Thus these error terms make a negligible
contribution.
We use (7.9) to change to our yr variables, which gives us a main term of
(9.72)
#A(x)
W
 ∑

p≤xρ
p∤W B
 ∑′

d,e∈Dk
(diei,p)=1
 λdλe
[dm, em, p] ∏

i,m[di, ei] = #A(x)
W
 ∑

p<xρ
p∤W B
 1
p
 ∑

r,s∈Dk
 yrys
ϕω(r)ϕω(s)
 ∏

p′|rs S p′(r, s, p).

Here if p′ , p then S p′(r, s, p) = S p′(r, s), given by (9.5), whereas if p′ = p we have

(9.73) S p(r, s, p) = ∑′

d|r,e|s
di,ei|p∀i
(diei,p)=1∀i,m
 pµ(d)µ(e)de
[dm, em, p] ∏
i,m[di, ei] =
 


(p − 1)
2, p|(rm, sm),
−(p − 1), p|rmsm, p ∤ (rm, sm),
1, p ∤ rmsm.

We let u = (r1/(r1, p), . . . , rk/(rk, p)) be the vector formed by removing a possible factor of p
from the components of r. We note that for a ﬁxed choice u, s ∈ Dk and p ∤ W we have

(9.74) ∑

r∈Dk
ri/(ri,p)=ui∀i
(ri,Wi)=1
 S p(r, s, p)
ϕω(r) = µ((sm, p))ϕ((sm, p))
ϕω(u)
 (
1 + ω(p) − 1
p − ω(p) − p − 1
p − ω(p)
) = 0.

Here the ﬁrst term in parentheses represents the contribution when (r, p) = 1, the second term
represents the contribution when p|r but p ∤ rm (and so there are ω(p) − 1 choices of which
index can be a multiple of p) and the ﬁnal term represents the contribution when p|rm.
We substitute yr = yu + (yr − yu) into our main term. By (9.74) we ﬁnd the yu term makes
a total contribution of 0, leaving only the contribution from (yr − yu). Similarly we let v
be the vector obtained by removing a possible factor of p from s. We make the equivalent

34 JAMES MAYNARD

substitution ys = yv + (ys − yv), with the yv term making no contribution. By Lemma 8.2 we
have

(9.75) (yr − yu)(ys − yv) ≪ YuYvT 2
k (log p)
2/(log R)
2.

Substituting this bound into our main term (9.72), we obtain the bound

(9.76) ≪ T 2
k #A(x)
W
 ∑

p<x
ρ
p∤W B
 1
p
 ( log p
log R
)2 ∑

u,v
(u,p)=(v,p)=1
 YuYv ∏

p′|uv |S p′(u, v)| ∑

r,s∈Dk
ri/(ri,p)=ui∀i
si/(si,p)=vi∀i
 |S p(r, s, p)|
ϕω(r)ϕω(s)

A calculation reveals that the inner sum is O(ϕω(u)
−1ϕω(v)
−1) for all p ∤ W B. This gives the
bound
 ≪ T 2
k #A(x)
W
 ∑

p<xρ
p∤W B
 1
p
 ( log p
log R
 )2 ∑

u,v∈Dk
(u,p)=(v,p)=1
 YuYv
ϕω(u)ϕω(v)
 ∏

p′|uv |S p′(u, v)|

≪ T 2
k ρ2#A(x)
W
 ∑

u,v∈Dk
 Y 2
u + Y 2
v
ϕω(u)ϕω(v)
 ∏

p′|uv |S p′(u, v)|.(9.77)

Here we have dropped the requirement that (u, p) = (v, p) = 1 and used YuYv ≤ Y 2
u + Y 2
v for
an upper bound.
We recall from (9.5) that S p′(u, v) = 0 unless u = v. By multiplicativity and from the
deﬁnition (9.5) of S p′(u, v), we ﬁnd that given u ∈ Dk, we have

(9.78) ∑

v∈Dk
 ∏p′|uv |S p′(u, v)|
ϕω(v) = ∏

p′|u
 ( ∑

w∈Dk
wi|p′ ∀i
 |S p′(u, w)|
ϕω(w)
 ) = ∏

p′|u
 ( p − 1
p − ω(p) + ω(p) − 1
p − ω(p)
 )
.

(Here the ﬁrst term in parentheses in the ﬁnal product corresponds to the w such that p|(u, w)
and the second term to the ω(p) − 1 choices of w such that p ∤ (u, w).) Thus, we ﬁnd
∑

u,v∈Dk
 Y 2
u + Y 2
v
ϕω(u)ϕω(v)
 ∏

p′|uv |S p′(u, v)| ≪ ∑

r∈Dk
 Y 2
r
g(r),(9.79)

where g is the multiplicative function deﬁned by g(p) = (p − ω(p))
2/(p + ω(p) − 2). Applying
Lemma 8.4, we see that this is

≪ BkW kSW B(L)
2

ϕ(W B)k (log R)
k ∏

p∤W B

(1 + ω(p)
g(p)
 )(1 − 1
p
 )kIk(F2),(9.80)

By Lemma 8.6 we have Ik(F2) ≪ k2Ik(F). Since any prime p ∤ W B has p > 2k2 and
g(p) = p + O(k), we see the product is ≪ SW B(L)
−1. Thus (9.80) is

≪ k2 BkW kSW B(L)
ϕ(W B)k (log R)
kIk(F).(9.81)

Putting this all together gives

(9.82) ∑

n∈A(x)
n≡v0 (mod W)

( ∑

p|L(n)
p<xρ
p∤B
 1)
wn ≪ k2T 2
k ρ2#A(x) BkW k−1SW B(L)
ϕ(W B)k (log R)
kIk(F).

Summing over the ϕω(W) residue classes mod W then gives the result. □

DENSE CLUSTERS OF PRIMES IN SUBSETS 35

10. Acknowledgements

I would like to thank Sary Drappeau, Andrew Granville, Dimitris Koukoulopoulos and
Jesse Thorner for many useful comments and suggestions. The author is funded by a CRM-
ISM postdoctoral fellowship at the Universit´e de Montr´eal.

References

[1] W. D. Banks, T. Freiberg, and C. L. Turnage-Butterbaugh. Consecutive primes in tuples. preprint,
http://arxiv.org/abs/1311.7003.
[2] J. Benatar. The existence of small prime gaps in subsets of the integers. preprint,
http://arxiv.org/abs/1305.0348.
[3] A. Castillo, C. Hall, R. J. Lemke Oliver, P. Pollack, and L. Thompson. Bounded gaps between primes in
number ﬁelds and function ﬁelds. preprint, http://arxiv.org/abs/1403.5808.
[4] H. Davenport. Multiplicative number theory, volume 74 of Graduate Texts in Mathematics. Springer-
Verlag, New York, third edition, 2000. Revised and with a preface by Hugh L. Montgomery.
[5] Tristan Freiberg. Strings of congruent primes in short intervals. J. Lond. Math. Soc. (2), 84(2):344–364,
2011.
[6] D. A. Goldston, S. W. Graham, J. Pintz, and C. Y. Yıldırım. Small gaps between products of two primes.
Proc. Lond. Math. Soc. (3), 98(3):741–774, 2009.
[7] D. A. Goldston, J. Pintz, and C. Y. Yıldırım. Positive proportion of small gaps between consecutive primes.
Publ. Math. Debrecen, 79(3-4):433–444, 2011.
[8] G. Harman, N. Watt, and K. Wong. A new mean-value result for Dirichlet L-functions and polynomials.
Q. J. Math., 55(3):307–324, 2004.
[9] M. N. Huxley and H. Iwaniec. Bombieri's theorem in short i ntervals. Mathematika, 22(2):188–194, 1975.
[10] S. Knapowski and P. Tur´an. On prime numbers ≡ 1 resp. 3mod 4. In Number theory and algebra, pages
157–165. Academic Press, New York, 1977.
[11] A. Kumchev. The diﬀerence between consecutive primes in an arithmetic progression. Q. J. Math.,
53(4):479–501, 2002.
[12] H. Li and H. Pan. Bounded gaps between primes of the special form. preprint,
http://arxiv.org/abs/1403.4527.
[13] J. Maynard. Small gaps between primes. Ann. of Math. (2), to appear.
[14] M. R. Murty and V. K. Murty. A variant of the Bombieri-Vinogradov theorem. In Number theory (Montreal,
Que., 1985), volume 7 of CMS Conf. Proc., pages 243–272. Amer. Math. Soc., Providence, RI, 1987.
[15] A. Perelli, J. Pintz, and S. Salerno. Bombieri's theore m in short intervals. II. Invent. Math., 79(1):1–9,
1985.
[16] P. Pollack. Bounded gaps between primes with a given primitive root. preprint,
http://arxiv.org/abs/1404.4007.
[17] D. K. L. Shiu. Strings of congruent primes. J. London Math. Soc. (2), 61(2):359–373, 2000.
[18] J. Thorner. Bounded gaps between primes in Chebotarev sets.
[19] N. M. Timofeev. Distribution of arithmetic functions in short intervals in the mean with respect to progres-
sions. Izv. Akad. Nauk SSSR Ser. Mat., 51(2):341–362, 447, 1987.
[20] Y. Zhang. Bounded gaps between primes. Ann. of Math. (2), 179(3):1121–1174, 2014.

Centre de recherches math´ematiques, Universit´e de Montr´eal, Pavillon Andr´e-Aisenstadt, 2920 Chemin
de la tour, Room 5357, Montr´eal (Qu´ebec) H3T 1J4
E-mail address: maynardj@dms.umontreal.ca
