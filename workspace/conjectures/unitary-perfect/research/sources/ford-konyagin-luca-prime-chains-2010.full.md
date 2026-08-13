<!-- source: https://arxiv.org/pdf/0904.0473 | converted from PDF -->

PRIME CHAINS AND PRATT TREES

KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

ABSTRACT. Prime chains are sequences p1, . . . , pk of primes for which pj+1 ≡ 1 (mod pj) for
each j. We introduce three new methods for counting long prime chains. The ﬁrst is used to show
that N (x; p) = Oε(x1+ε), where N (x; p) is the number of chains with p1 = p and pk ⩽ px. The
second method is used to show that the number of prime chains ending at p is ≍ log p for most
p. The third method produces the ﬁrst nontrivial upper bounds on H(p), the length of the longest
chain with pk = p, valid for almost all p. As a consequence, we also settle a conjecture of Erd˝os,
Granville, Pomerance and Spiro from 1990. A probabilistic model of H(p), based on the theory
of branching random walks, is introduced and analyzed. The model suggests that for most p ⩽ x,
H(p) stays very close to e log log x.
 1. INTRODUCTION

1.1. For positive integers a and b, write a ≺ b if b ≡ 1 (mod a). We are interested in properties
of prime chains p1 ≺ p2 ≺ · · · ≺ pk, e.g. 3 ≺ 7 ≺ 29 ≺ 59. Prime chains are multiplicative
analogs of the well-studied additive prime k-tuples (sequences p1 < · · · < pk of primes with
pk − p1 small). Important quantities of study are N (x), the number of prime chains with pk ⩽ x
(k variable), N (x; p), the number of prime chains with p1 = p and pk/p1 ⩽ x, f (p), the number of
prime chains with pk = p, and H(p), the length of the longest prime chain with pk = p. Estimates
for these quantities have arisen in investigations of iterates of Euler’s totient function φ(n) and
Carmichael’s function λ(n) (e.g. [5], [6], [7], [19], [28], [29], [30]), the value distribution of λ(n)
[21], common values of φ(n) and the sum-of-divisors function σ(n) [22], and the complexity of
primality certiﬁcates ([8], [33]).
In studying long chains, where the ratios log pj+1/ log pj are small on average, we require infor-
mation about the large prime factors of shifted primes p − 1. That is, we require good estimates
for π(x; q, 1) when q is large, where π(x; q, a) = |{p ⩽ x : p ≡ a (mod q)}|. Progress, however,

Date: July 27, 2021.
2000 Mathematics Subject Classiﬁcation. Primary 11N05, 11N36; Secondary 60J80.
The research of K. F. was supported in part by NSF grants DMS-0555367 and DMS-0901339, that of S. K. was
supported in part by Grant 08-01-00208 from the Russian Foundation for Basic Research, and that of F. L. was
supported in part by projects PAPIIT 100508 and SEP-CONACyT 79685. Some of this work was accomplished while
the third author visited the University of Illinois at Urbana-Champaign in February 2007, supported by NSF grant
DMS-0555367. The ﬁrst and second authors enjoyed the hospitality of the Institute for Advanced Study, where some
of this work was done in November 2007 and spring 2010, the ﬁrst author being supported by The Ellentuck Fund and
The Friends of the Institute for Advanced Study. The ﬁrst author was also supported by the NSF sponsored Workshop
in Linear Analysis and Probability at Texas A&M University, August 2008.
1arXiv:0904.0473v4  [math.NT]  15 Sep 2010
2 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

is hampered by our poor knowledge when q > √x. Let li(x) = ∫ x
2 dt/ log t. The Bombieri-
Vinogradov theorem ([16], Ch. 28) implies that

(1.1) ∑

m⩽Q max
y⩽x
 ∣
∣
∣
∣π(y; m, 1) − li(y)
φ(m)
∣
∣
∣
∣ ≪ R,

with Q = x1/2(log x)
−B and R = x(log x)
−A (here A > 0 is arbitrary and B depends on A).
The corresponding statement with Q = xθ is not known for any ﬁxed θ > 1/2, however it is
conjectured (the Elliott-Halberstam conjecture; abbreviated EH) that (1.1) holds with Q = xθ and
R = x(log x)
−A for any θ < 1 and A > 0. The one-sided Brun-Titchmarsh inequality

(1.2) π(x; q, 1) ⩽ 2x
(q − 1) log(x/q),

however, is useful in some situations.
If one asks just for the existence of many shifted primes p − 1 with a large prime factor, we can
do a little bit better than Bombieri-Vinogradov. Let P +(n) denote the largest prime factor of n,
and let θ0 be the supremum of real numbers θ so that there are inﬁnitely many primes p ⩽ x such
that P +(p − 1) ⩾ xθ. EH implies θ0 = 1, and the best unconditional result is due to Baker and
Harman [4], who showed that θ0 ⩾ 0.677.
In this paper, we prove new bounds for N (x; p), N (x), f (p) and H(p). At the core of our
arguments is a kind of duality principle: in a chain p1 ≺ · · · ≺ pk, there are integers mj
with pj+1 = mjpj + 1, and there is an obvious bijection between the k-tuples (p1, . . . , pk) and
(p1, m1, . . . , mk−1). It is often more efﬁcient to focus on properties of the latter vector rather than
the former.

1.2. We begin with the problem of bounding N (x; p). By iterating (1.2), one arrives at a uniform
bound (e.g. [19], Theorem 3.5)

(1.3) Nk(x; p) ≪ x(c log2 x)
k−1

log x
for the number, Nk(x; p), of prime chains of length k with p1 = p and pk/p1 ⩽ x. Here logk x is
the k-th iterate of the logarithm of x, and c is some constant. Summing (1.3) over k ⩽ log x
log 2 + 1,
one obtains the weak estimate N (x; p) ≪ xO(log3 x).

Theorem 1. For p ⩾ 2 and x ⩾ 20, we have the effective estimate

N (x; p) ⩽ x exp { log x(log3 x + O(1))
log2 x
 } .

In particular, for every ε > 0 there is an effective constant C(ε) so that N (x; p) ⩽ C(ε)x1+ε.

Theorem 1 has applications to problems which, at ﬁrst glance, have nothing to do with prime
chains. First, it is a crucial tool in the recent proof by Ford, Luca and Pomerance [22] that the
equation φ(a) = σ(b) has inﬁnitely many solutions, settling a well-known 50-year old prob-
lem of Erd˝os. In [21], Theorem 1 is used to show that for some effective q0, if π(p3a; pa, 1) −
π(p3a; pa+1, 1) ⩾ 113p 7a−3
4 / log(pa+1) for all prime powers pa ∈ (10
10, q0], then for every positive
integer n, there is another positive integer m with λ(n) = λ(m). This nearly settles a conjecture
from [5], the analog for λ of the famous Carmichael Conjecture for φ.

PRIME CHAINS AND PRATT TREES 3

Theorem 1 is nearly best possible, since N (x; p) ⩾ N2(x; p) = π(px; p, 1), which is expected
to be ≫ x/(log px) unless x is very small relative to p.

Conjecture 1. We have N (x; p) ≪ x.

Conjecture 1 is easy to prove when p is bounded. Using f (2) = 1 and the recursive formula

(1.4) f (p) = 1 + ∑

q|(p−1) f (q),

we have

(1.5) f (p) ⩽ 2 log p
log 2 − 1 (all p).

Summing on p ⩽ x using the prime number theorem gives N (x) ≪ x and hence N (x; p) ≪ px.
Lower bounds on f (p) and N (x) are more difﬁcult, since f (p) is sometimes very small, e.g. if
p = 1 + 2a3
b then f (p) = 4 (it is conjectured that there are inﬁnitely many such primes).

Theorem 2. (i) We have f (p) ⩾ 0.378 log p for almost all primes p. Hence, N (x) ≫ x.

(ii) For all x ⩾ 3 and any positive integer h, |{p ⩽ x : f (p) = h}| ⩽ ( 6 log x
h
 )h .

In particular, part (ii) implies that primes with f (p) = o(log p) are exceptionally rare, the count-
ing function being xo(1) as x → ∞. Also, by (i), we have N (x; 2) = 1
2N (x) ≫ x.
It is likely that f (p) has normal order1 c log p for some c. A very similar problem was considered
in Section 2 of [19], namely the behavior of I(n) = min{j : φj(n) = 1}, where φj is the j-th
iterate of φ. It turns out that F (n) = I(n)−{
1 n odd
0 n even is completely additive, and F (p) = F (p−1) =∑

qa∥p−1 aF (q) for odd primes p. This is similar to (1.4), the only difference being the behavior
at proper prime powers, which play an insigniﬁcant role in the arguments in [19]. Summing (1.4)
over primes p ⩽ x gives
 N (x) = π(x) + ∑

q⩽x/2 f (q)π(x; q, 1).

Inserting this relation into the proof of Theorem 2.1 in [19] (combine Lemma 2.4, Corollary 2.5,
(2.8) and Theorem 2.1 therein), we obtain the following.

Theorem A. If (1.1) holds with Q = x1−(log2 x)−1−δ and R = x(log x)
−2 for some ﬁxed δ > 0,
then N (x) ∼ cx for some constant c > 0 and f (p) has normal order c log p.

Conjecture 1 implies that for all ε > 0 and prime q > (log x)1+ε, for most p ⩽ x there is no
prime chain q ≺ · · · ≺ p. This gives, conditionally, the ﬁrst part of [19, Conjecture 1]. By contrast,
the proof of Theorem 4.5 of [19] implies that if q ⩽ (log x)
c, for some small constant c > 0, then
for almost all primes p ⩽ x, there is a prime chain q ≺ · · · ≺ p.

1for every ε > 0, |f (p) − c log p| ⩽ ε log p for all primes but o(π(x)) exceptions up to x.

4 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA 0 2 4 6 8 10 12 14 16 18 20 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
number of primes (millions)HeightPratt tree height, primes < 1,000,000,000 0 50 100 150 200 250 300 350 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
number of primesHeightPratt tree height, random primes near 10^40
FIGURE 1. Pratt tree height

1.3. The Pratt tree T (p) for a prime p is the tree with root node p, below p are nodes labelled
with the prime factors q of p − 1, below each q are nodes labelled with the prime factors of q − 1,
and so on. In 1975, V. Pratt [33] used it in conjunction with Lucas’ primality test ([15], §4.1) to
show that every prime has a short certiﬁcate (proof of primality). Pomerance [32] gave another
method for producing primality certiﬁcates, but it is an open problem whether the Pratt certiﬁcate
has longer complexity for most primes (see §1 of [32]). Two important statistics of the Pratt tree
are the total number of nodes f (p) and the height H(p), the latter being the length of the longest
prime chain ending at p. It is known (see [7], [18], [20]) that the number of primes at a ﬁxed level
n in the Pratt tree for most p is ∼ (log2 p)n/n!. The idea is that for most primes p, p − 1 has a
multiplicative structure similar to that of a typical integer of its size; namely, p − 1 has about log2 p
prime factors, uniformly distributed on a log log-scale (see [25], Ch. 1). This, however, does not
give much information about H(p).
Figure 1 shows histograms of H(p) for all primes p ⩽ 10
9 and for 1000 randomly chosen primes
near 10
40. Very little is known about the distribution of H(p), the extremal behavior being a case
in point. First, H(p) = 2 if and only if p is a Fermat prime, that is, p = 2
2m + 1 for some m. It
seems plausible that H(p) = 3 for inﬁnitely many p, but this is hopeless to prove at this time. At
the other extreme, we have the trivial upper bound H(p) ⩽ log p
log 2 + 1. Large values of H(p) may be
obtained using the special chain 2 = q1 ≺ q2 ≺ · · · , where, for each j, qj+1 is the smallest prime
≡ 1 (mod qj). By Linnik’s theorem, qj+1 ⩽ qL
j for some constant L, hence H(qj) ⩾ log log qj
log L .
It is conjectured that qj+1 ⩽ qj(log qj)
C for some ﬁxed C and this implies a far stronger bound
H(qj) ≫ log qj
log log qj . Even showing H(p)/ log2 p → ∞ for an inﬁnite sequence of p is extremely
hard, as it implies θ0 = 1: a prime chain p1 ≺ · · · ≺ pk = p with k = H(p) satisﬁes

log pk
log p1 =
 k−1∏

j=1
 log pj+1
log pj ⩾ ( min
1⩽j⩽k−1 log pj+1
log pj
 )k−1 ,

and hence

(1.6) Λ := lim sup
p→∞ H(p)
log2 p ⩽ 1
− log θ0 .

PRIME CHAINS AND PRATT TREES 5

On the other hand, K´atai [27] proved that for some constant c > 0, H(p) ⩾ c log2 p for almost all
primes p (for all primes p ⩽ x with o(x/ log x) exceptions). We prove a version with the constant
made explicit in terms of the level of distribution of primes in progressions.

Theorem 3. (a) If (1.1) holds with Q = xθ and R = o(x/ log x), then for any c < 1
e−1−log θ ,
H(p) > c log2 p for almost all primes p;
(b) If (1.1) holds with Q = xθ and R = x(log x)−A for every A > 1, then for every c < 1
− log θ ,
there is a K so that H(p) > c log2 p for ≫ x/(log x)
K primes p ⩽ x. Consequently, Λ ⩾ 1
− log θ .

Corollary 1. EH implies that for every c < e, H(p) > c log2 p for almost all p.

Remark 1. By the Bombieri-Vinogradov theorem and (1.2), for every ε > 0, (1.1) holds with
Q = x1−ε and R = Oε(x/ log x).
If Λ ⩾ −1/ log θ for some θ < 1, then there are many chains 2 = p1 ≺ · · · ≺ pk with log pj+1
log pj at
most 1/θ on average. Thus, although (1.6) is likely an equality, to prove this would require strong
information about the set of primes with P +(p−1) near pθ0. The same difﬁculty arises when trying
to prove (a) with θ = θ0.
The bound on H(p) in (a) is weaker than in (b), since it is unusual in a chain p1 ≺ · · · ≺ pk
for most of the ratios log pj+1
log pj to be close to 1/θ. The constant e−1 appearing in (a) is likely best
possible; see Conjecture 2 below.

Turning to upper bounds, before our work it was unknown if there is an inﬁnite sequence of
primes with H(p) = o(log p). A natural approach is to ﬁnd p such that P +(p − 1) is small and
use H(p) = 1 + maxq|(p−1) H(q) ≪ maxq|(p−1) log q. However, our knowledge of smooth shifted
primes is very weak (the world record is P +(p − 1) < p0.2961 inﬁnitely often [4]). Using a new
and very different approach, we give a much stronger upper bound.

Theorem 4. We have H(p) ⩽ (log p)
0.9503 for almost all p.

The proof of Theorem 4 involves showing that for most primes p, all the primes at some bounded
level of the tree are small. In particular, this settles [19, Conjecture 2].

Theorem 5. For every ε > 0 and δ > 0, there is an integer k so that for large x and at least
(1 − δ)x integers n ⩽ x, P +(φk(n)) ⩽ xε.

There is a folklore conjecture that H(p) = O(log2 p) for most p.

Conjecture 2. H(p) has normal order e log2 p.

Remark 2. The lower bound in Conjecture 2 follows from EH (Corollary 1). Conversely, by (1.6),
the lower bound in Conjecture 2 implies that θ0 ⩾ e−1/e = 0.6922 . . . (with a bit more work using
(1.2), one can deduce θ0 ⩾ 0.73).
The upper bound in Conjecture 2 appears to be even more difﬁcult. We cannot see a way to
deduce it from standard conjectures in prime number theory, e.g. EH plus a uniform prime k-
tuples conjecture, although Theorem 4 can be signiﬁcantly improved under such hypotheses.

Understanding H(p) requires detailed knowledge of the distribution of the large prime factors of
shifted primes p − 1. Making a reasonable assumption for this distribution (a consequence of EH),
in Section 6 we model the Pratt tree by a branching random walk. The model provides a much
more precise version of Conjecture 2.

6 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

Conjecture 3. H(p) = e log2 p − 3
2 log3 p + E(p), where for some ﬁxed c, c
′ > 0 and any z ⩾ 0,
the number of p ⩽ x for which E(p) ⩾ z is ≫ e−c′zπ(x) and ≪ e−czπ(x), and E(p) ⩽ −z for
O(exp{−e
cz}π(x)) primes ⩽ x.

Notable features of Conjecture 3 are (i) the tightness of E(p): the distribution of H(p) over
p ⩽ x does not widen as x → ∞, and (ii) the pronounced asymmetry of the distribution of E(p).
The analogs of these features for our probabilistic model are proved rigorously.
Assuming Median{H(p) : p ⩽ x} grows slowly, we show that H(p) is tight to the left of its
median.

Theorem 6. Suppose g and h are increasing, 0 ⩽ g(x) ⩽ h(x), h(x2) − h(x) ⩽ K and g(x2) −
g(x) ⩽ K for x ⩾ 1. Suppose, for large x, that H(p) ⩾ h(p) for at least cπ(x) primes ⩽ x. Then
H(p) ⩾ h(p) − g(p) for all primes p ⩽ x with at most O(π(x) exp{− c log 2
K g(x)}) exceptions.

We conclude this section with a conjecture about prime chains, which follows from the prime
k-tuples conjecture (with m = 2 below) but should be “easier”. It is a multiplicative analog of
the statement that the primes contain arbitrarily long arithmetic progressions, recently proved by
Green and Tao [23]. Even the case k = 3 is not known.

Conjecture 4. For each k ⩾ 3, there are inﬁnitely many prime k-tuples (p1, . . . , pk) where, for
some m, pj+1 = mpj + 1 for 1 ⩽ j ⩽ k − 1.

Notation. The letters p and q, with or without subscripts, always denote primes. Constants
implied by the O, ≪ and ≍ symbols do not depend on any parameter unless indicated. In Section
6, we use P for probability and E for probabilistic expectation.

2. SIFTED CHAINS: PROOF OF THEOREM 1

The underlying idea is a sieve; relax the condition that the numbers in the chain are prime, and
only require that they do not have small prime factors. Let y ⩾ 2 and let r be the product of the
primes ⩽ y. For (a, r) = 1, let Ga(x; y) be the number of chains n1 ≺ · · · ≺ nk with n1 = a, with
nk/n1 ⩽ x and consisting of numbers coprime to r. If p > y, then N (x; p) ⩽ Gp(x, y). There are
integers (“links”) m1, . . . , mk−1 with nj+1 = mjnj + 1 for 1 ⩽ j ⩽ k − 1. For positive integers
a, b and real s > 1,
 S(a, b) = S(a, b; r, s) = ∑

m⩾1
am+1≡b( mod r)
 m
−s

encodes the possible links m from a number ni ≡ a (mod r) to a number ni+1 ≡ b (mod r).
Fix r, s and let Ur = (Z/rZ)∗. Let Ak(a1, ak) be the sum of (m1 · · · mk−1)−s over all tuples
(m1, . . . , mk−1) which could serve as links in a chain starting from a number n1 ≡ a1 (mod r),
ending with a number nk ≡ ak (mod r) and with all numbers in the chain coprime to r. Then
A2(a1, a2) = S(a1, a2) and for k ⩾ 3,

Ak(a1, ak) = ∑

a2,...,ak−1∈Ur S(a1, a2)S(a2, a3) · · · S(ak−1, ak).

PRIME CHAINS AND PRATT TREES 7

Let Vk(a1) be the column vector (Ak(a1, ak) : ak ∈ Ur). For consistency, let V1(a1) be a vector
with all zero entries except for an entry of 1 in the a1 position. Since

Ak+1(a1, ak+1) = ∑

ak∈Ur Ak(a1, ak)S(ak, ak+1),

we obtain Vk+1(a1) = M Vk(a1), where M = M (r, s) = (S(a, b)
)

b,a∈Ur. The rows of M are
indexed by b and the columns are indexed by a. Finally, let Fk(a1) = ∑
ak Ak(a1, ak), so that

Fk(a1) = (1, . . . , 1)Vk(a1) = (1, . . . , 1)M k−1V1(a1);

i.e., Fk(a1) is the sum of the entries of column a1 in M k−1. Since m1 · · · mk−1 ⩽ nk/n1 ⩽ x,

(2.1) Ga(x; y) ⩽ inf
s>1
 (xs ∑

1⩽k⩽ log x
log 2 +1 Fk(a)).

Observe that the sum on k in (2.1), if extended to k = ∞, is convergent if and only if M is a
contracting matrix, i.e., all the eigenvalues of M have modulus < 1. Since M has positive real
entries, the Perron-Frobenius Theorem implies that the eigenvalue with largest modulus is positive,
real and simple. Call this eigenvalue λ(s; y).
We show below that if y is large and s ⩾ 1 + log2 y
log y , then λ(s; y) < 1. Accurate estimation
of λ(s; y) is difﬁcult for large y, but the largest row sum of M serves as an upper bound. For a
generic matrix A, let Rb(A) be the sum of the entries in the row indexed by b, and let R(A) be the
maximum row sum of A. For row b of M , write d = (b − 1, r) and b′ = b−1
d . Then

Rb(M ) = ∑

a∈Ur
 ∑

am≡b−1( mod r) m
−s = d
−s ∑

(k,r/d)=1 k−s#{a ∈ Ur : ak ≡ b′ (mod r/d)}.

The congruence ak ≡ b′ (mod r/d) has a unique solution modulo r/d, and hence has φ(d) solu-
tions a ∈ Ur. Thus,

Rb(M ) = φ(d)
ds ∑

(k,r/d)=1 k−s = φ(d)
ds ∏

p∤(r/d)
(1 − p−s)
−1 = ∏

p>y(1 − p−s)
−1 ∏

p|d
 p − 1
ps − 1.

Therefore, since d is always even,

(2.2) R(M ) = 1
2s − 1
 ∏

p>y(1 − p−s)
−1.

Since R(AB) ⩽ R(A)R(B), R(M k−1) ⩽ R(M )k−1. To bound Ga(x; y), we need to bound the
largest column sum of M k−1. Lacking a better approach, we use the crude bound φ(r)R(M )
k−1.
Thus, Fk(a) ⩽ φ(q)R(M k−1) ⩽ φ(r)R(M )
k−1. By (2.1),

Ga(x; y) ⩽ φ(r) inf
s:R(M )<1 xs

1 − R(M ).

By standard prime number estimates, if 1 < s ⩽ 2, then

− ∑

p>y log(1 − p−s) = O(1/y2s−1) + ∑

p>y p−s ≪ e−(s−1) log y

(s − 1) log y .

8 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

Take y = log x
log2 x and s = 1 + log2 y
log y . Since 2
s − 1 = 1 + (2 log 2)(s − 1) + O((s − 1)
2), (2.2) implies
1 − R(M ) ∼ (2 log 2)(s − 1) as x → ∞. Since φ(r) ⩽ r = e
(1+o(1))y as x → ∞, this proves
Theorem 1.
 3. PROOF OF THEOREM 2

Let Q(p) be the multiset of prime labels appearing in T (p), and let T ′(p) be the subtree of T (p)
consisting of nodes with odd prime labels. There is a natural bijection between T (p) and T ′(p),
obtained by adding to every node in T ′(p) a child node with label 2. Let l(n) = ∏
pa∥n pa−1. The
quantity q
q−1l(q − 1) measures the “loss of mass” when descending from a node labelled q to its
child nodes: in fact, it is easy to see that

∏

q∈Q(p)
 ( q
q − 1l(q − 1)) = p.

If p > 2, exactly half of the nodes in T (p) are labelled with 2, thus

(3.1) ∏

q∈Q(p) l(q − 1) ⩽ p2
− 1
2 f (p).

Consider the set of p ⩽ x with f (p) = h, where h = 2n is positive and even. Let T be the
set of rooted trees on n nodes. For each T ′ ∈ T , we consider separately the primes p with T ′(p)
tree-isomorphic to T ′. Form the tree T on h nodes, by adding to each node of T ′ an additional
child node. We count in how many ways we can label with primes the nodes of T , with the leafs
having label 2 and the root having label p ⩽ x. For a given prime p, there may be more than one
way to assign primes in the Pratt tree to the nodes of T ′; this occurs when some node has two or
more child trees that are isomorphic (as rooted trees). Thus, for each T ′, we count ways to assign
primes to the nodes, and divide by the number of ways in which we can permute the nodes; that
is, the number I(T ′) of isomorphisms of T ′. Assign to each node an ordinal number 1, 2, . . . , h so
that the children of node j are assigned lower ordinals (e.g., node 1 will be a lowest leaf, and node
h will be the root). To node number j, we let qj be its prime label and lj = l(qj − 1). Let Bj be
the set of ordinal numbers of the children of node j, and observe that B1, . . . , Bh depend only on
T ′. With this notation,

(3.2) qj − 1 = lj ∏

k∈Bj qk.

With T ﬁxed, (3.2) implies a natural bijection between (q1, . . . , qh) and (l1, . . . , lh) (recall that
leafs have qj = lj = 2). By (3.1), we have for any β > 0

|{p ⩽ x : f (p) = h}| ⩽ ∑

T ′∈T
 1
I(T ′)
 ∑

l1,...,lh
 ( x2
−h/2

l1 · · · lh
 )β .

Suppose that j ⩾ 2 and that l1, . . . , lj−1 have been chosen. If node j is a leaf of T , then lj = 1.
Otherwise, using (3.2), the primes qk for k ∈ Bj are determined by l1, . . . , lj−1. Moreover, a prime

PRIME CHAINS AND PRATT TREES 9

r|lj must equal one of these primes qk. Hence
∑

lj l−β
j ⩽ ∏

k∈Bj
 (1 − q−β
k )−1 ⩽ (
1 − 2
−β)−1 (
1 − 3
−β)1−|Bj | .

By Borchardt’s formula
2 [13] for counting labelled trees,
∑

T ′∈T
 1
I(T ′) = nn−2

(n − 1)! = nn−1

n! ⩽ en.

Since ∑

|Bj |⩾1(|Bj| − 1) = h/2 − 1, we conclude that

(3.3) |{p ⩽ x : f (p) = h}| ⩽ eh/2 (
x2
−h/2)β (
1 − 2
−β)−h/2 (
1 − 3
−β)−h/2

Taking β = 0.37, the right side of (3.3) is ⩽ x0.37(27.8371)
h/2 ⩽ x0.999 for h ⩽ 0.378 log x. For
the second part of Theorem 2, assume h ⩽ (2/5) log x (if h ⩾ 3 log x, there are no such p and for
(2/5) log x < h ⩽ 3 log x, ( 6 log x
h )h > x). Take β = h/ log x. Since 0 < β ⩽ 2/5, 2
β −1 ⩾ β log 2
and 1 − 3
−β ⩾ 0.889β. Hence, the right side of (3.3) is ⩽ xβ(4.412/β2)h/2.
We remark that numerical improvements are possible by reﬁning the above analysis; e.g. using
the fact that leafs of T ′ must be labelled with a Fermat prime.

4. LOWER BOUNDS FOR H(p): PROOF OF THEOREM 3

We show part (b) ﬁrst, as the proof is much easier.

Proof of Theorem 3 (b). Let c′ and θ′ satisfy θ′ > 1/3 and c < c
′ < 1
− log θ′ < 1
− log θ , and deﬁne
K by 8θK = θ − θ′. Let x0 be large, depending on K, c, c
′, θ, θ′ and put c′′ = c′ log2(x3
0). Let
P = {p : H(p) ⩾ c′ log2 p − c′′}. In particular, P contains all primes ⩽ x3
0. We shall prove

(4.1) Q(x) := |P ∩ (x/2, x]| ⩾ x
(log x)K

for x ⩾ x0, which implies the desired conclusion (since c′ > c). By the prime number theorem
and the fact that K > 1, if x0 is large enough then (4.1) holds for x0 ⩽ x ⩽ x3
0. Suppose y ⩾ x3
0
and (4.1) holds for x0 ⩽ x ⩽ y. Assume y < x ⩽ 2y and put I = P ∩ (xθ′, x
θ]. Suppose that
x/2 < p ⩽ x, and that q|p − 1, where q ∈ I. Then

H(p) ⩾ 1 + H(q) ⩾ 1 + c′ log2 q − c′′

⩾ 1 + c′ log2 x + c′ log θ′ − c′′ > c
′ log2 p − c′′,

so that p ∈ P. For x/2 < p ⩽ x, p − 1 is divisible by at most two primes from I, hence

Q(x) ⩾ 1
2
 ∑

q∈I
 (π(x; q, 1) − π(x/2; q, 1)
) ⩾ x
4 log x
 ∑

q∈I
 1
q + O ( x
(log x)K+1
 ) .

Since (4.1) holds for xθ′ < y ⩽ xθ, the sum on q ∈ I is

⩾ ∑

2j ⩽xθ−θ′
 Q(2
jxθ′)
2jxθ′ ⩾ ( (θ − θ′) log x
log 2 − 1
) 1
(log xθ)K ⩾ θ − θ′

θK(log x)K−1 = 8
(log x)K−1 .

2commonly known as Cayley’s formula.

10 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

Therefore, (4.1) holds. By induction on dyadic intervals, (4.1) holds for all x ⩾ x0. □

Remark. The same proof gives, assuming that (1.1) holds with Q = x1−ε(x) and R(x) =
x(log x)−g(x) where ε(x) → 0 and g(x) → ∞ as x → ∞, that H(p) ⩾ h(p) log2 p for inﬁnitely
many p, where h(p) → ∞ as p → ∞ (the function h depending on the functions ε, g).

Proof of Theorem 3 (a). We proceed by induction as in part (b), but instead we iterate by many
levels in the chain at once rather than one level at a time. Suppose that c < h < c′ < 1/(e
−1 −
log(θ)). For some constant c′′, described below, let P = {p : H(p) ⩾ c′ log2 p − c′′}. We will
show, for some δ > 0, that

(4.2) P(x) := |{p ⩽ x : p ∈ P}| ⩾ δ x
log x .

Consequently, a positive proportion of primes p satisfy H(p) > h log2 p, and Theorem 3 (a) follows
from Theorem 6.
By Stirling’s formula, there is an integer k ⩾ 2 such that 1/c
′ > 1
k (k!)
1/k − log(θ). Let α, β
satisfy e−k/c′ < β < θk exp (
−(k!)
1/k) and β exp (
(k!)
1/k) < α < θk. Suppose that δ is sufﬁ-
ciently small, depending only on the choice of c′, θ, k, α, β. Let x0 be sufﬁciently large, depending
on c′, θ, k, α, β, δ, and put c′′ = c′ log2(x0). Observe that (4.2) holds trivially for 2 ⩽ x ⩽ x0, pro-
vided δ is small enough. Throughout this proof, constants implied by the O− and ≪ −symbols
may depend on c′, θ, k, α, β, but not on δ.
Next, suppose that Y ⩾ x0 and that inequality (4.2) holds for 2 ⩽ x ⩽ Y . Let S be a subset of
the primes in P ∩ [Y β, Y θk]. Let M (S) be the number of primes p0 ∈ (Y, 2Y ] so that there is a
prime chain pk ≺ pk−1 ≺ · · · ≺ p0 with pk ∈ S. For such p0, we have

H(p0) ⩾ k + H(pk) ⩾ k + c′ log2 pk − c′′

= c′ log2(2Y ) − c′′ + c′ log β + k + O ( 1
log Y
 ) ⩾ c′ log2 p0 − c′′

if x0 is large enough. We will show, for appropriate S, that

(4.3) M (S) ⩾ δ Y
log Y ,

which implies P (2Y ) ⩾ P (Y )+M (S) ⩾ 2δY / log(2Y ). By induction over dyadic intervals, (4.3)
implies (4.2), and hence Theorem 3 (a).
To prove (4.3), we will consider chains satisfying not only pk ∈ S, but also

(4.4) pj+1 ⩽ pθ
j (0 ⩽ j ⩽ k − 1), p1 ⩽ Y θ.

With (4.4), we can use (1.1) to accurately count such chains. We have M (S) ⩾ M1(S) − M2(S),
where M1(S) is the number of chains satisfying pk ∈ S and (4.4), and M2(S) is the number of
pairs of distinct chains satisfying these conditions with the same p0. We begin with

M1(S) = ∑

pk∈S
 ∑

pk−1 · · · ∑

p1
 (π(2Y, p1, 1) − π(Y, p1, 1)
)
,

PRIME CHAINS AND PRATT TREES 11

where pk ≺ · · · ≺ p0 and (4.4) in the summations. By (1.1) and induction on 1 ⩽ j ⩽ k,

(4.5) M1(S) = Y
log Y
 ∑

pk
 ∑

pk−1 · · · ∑

pj
 ( log2 Y θj − log2 pj)j−1

pj(j − 1)! + o ( Y
log Y
 ) .

Here, we used that for each pj, there are O(1) chains pk ≺ · · · ≺ pj with pk ⩾ Y β. By (4.5) with
j = k,
 M1(P ∩ [Y β, Y α]) ⩾ δY
log Y
 ∫ Y α

Y β (log2 Y α − log2 t)
k−1

(k − 1)!t log t dt + o ( Y
log Y
 )

= δY
log Y (log(α/β))
k

k! + o ( Y
log Y
 ) .

By hypothesis, log(α/β) > (k!)
1/k. The summands in (4.5) (with j = k) are ≍ 1/pk for Y β ⩽
pk ⩽ Y α. Hence, if δ is small enough, there is a set S ⊆ P ∩ [Y β, Y α] such that

(4.6) ∑

pk∈S
 1
pk ≪ δ, M1(S) ⩾ (δ + δ3/2) Y
log Y .

We have M2 = M2,0 + · · · + M2,k−1 where M2,j counts pairs of coupled chains

pk ≺ · · · ≺ pj+1

p′
k ≺ · · · ≺ p′
j+1
 〉 pj ≺ · · · ≺ p0

with each of the two chains satisfying (4.4), pj+1 ̸= p′
j+1 and pk, p
′
k ∈ S. We further write
M2,j = M ′
2,j +M ′′
2,j, where M ′
2,j counts pairs of such chains with pj ⩽ pj+1p′
j+1Y δ2. As before, for
each pair (pj+1, p′
j+1), there are O(1) choices for pk, p
′
k, . . . , pj+2, p
′
j+2. For M ′
2,0, p1p′
1 ⩾ Y 1−δ2,
and for each p0, there are O(1) choices for p1, p
′
1. By sieve methods (e.g. Theorem 2.2 of [24]),

M ′
2,0 ≪ ∑

1⩽k⩽Y δ2 |{n ⩽ Y : n ≡ 1 (mod k), P −(n( n−1
k )) > Y β}|

≪ ∑

1⩽k⩽Y δ2
 Y
φ(k) log2 Y ≪ δ2Y
log Y .

Here, P −(m) is the smallest prime factor of m. For j ⩾ 1, an argument similar to that leading to
(4.5), followed by the same sieve bound, gives

M ′
2,j ≪ Y
log Y
 ∑

pj+1,p′
j+1
 ∑

pj
 1
pj ≪ ∑

k⩽Y δ2
 ∑

n⩽Y,n≡1 (mod k)
P −(n( n−1
k )>Y β
 1
n ≪ δ2 Y
log Y .

For chains counted by M ′′
2,j, the Brun-Titchmarsh inequality sufﬁces for the estimations. When
j ⩾ 1 and pj is given, as before we have
∑

pj−1 · · · ∑

p1 π(2Y, p1, 1) ≪ Y
pj log Y .

12 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

By partial summation and (1.2), given pj+1 and p′
j+1,
∑

pj
 1
pj ≪ 1
pj+1p′
j+1δ2 log Y + log(1/δ)
pj+1p′
j+1 ≪ log(1/δ)
pj+1p′
j+1 .

For j + 1 ⩽ r ⩽ k − 1,

(4.7) ∑

pr
 1
pr ≪ 1
pr+1 , ∑

p′
r
 1
p′
r ≪ 1
p′
r+1 .

Finally, by (4.6), we arrive at

(4.8) M ′′
2,j ≪ δ2 log(1/δ) Y
log Y .

In a similar way, when j = 0, we have by (1.2) and partial summation,
∑

p1p′
1⩽2Y 1−δ2 π(2Y, p1p′
1, 1) ≪ log(1/δ)
p2p′
2 .

A second application of (4.7) then gives (4.8) in this case.
Finally, combining our estimates for M ′
2,j and M ′′
2,j, we obtain M2(S) ≪ δ2 log(1/δ)Y / log Y.
Together with (4.6), if δ is small enough then (4.3) holds, and this completes the proof. □

5. PROOF OF THEOREMS 4 AND 5

The proofs of Theorems 4 and 5 rely on the fact that the largest prime factor of p − 1 cannot be
too large too often. At the core is a sieve upper bound for k-tuples of primes which is uniform in
k, and careful averages of the associated singular series. There is a potentially troublesome factor
2
kk! in the sieve estimate, which is partly overcome by observing that if H(p) is large, then there
must be a prime chain in the Pratt tree for p which is very condensed in a multiplicative sense.

Lemma 5.1. There is a positive constant δ so that the following holds. Let a1, . . . , ak be positive
integers, let b1, . . . , bk be integers with (aj, bj) = 1 for all j, and let ξ(p) be the number of solutions
of ∏k
i=1(ain + bi) ≡ 0 (mod p). If x ⩾ 10, 1 ⩽ k ⩽ δ log x
log2 x and

B := ∑

p
 k − ξ(p)
p log p ⩽ δ log x,

then the number of integers n ⩽ x for which a1n + b1, . . . , akn + bk are all prime and > k is

≪ 2
kk!
(log x)k xS · exp (O ( kB + k2 log2 x
log x
 )) , S = ∏

p
 (
1 − ξ(p)
p
 ) (
1 − 1
p
)−k .

Proof. Since ξ(p) = k for large p, S > 0 if and only if ξ(p) < p for all p. Also, ξ(p) ⩽ k for all
p. Hence, if S = 0, the number of n is zero. If S > 0, Montgomery’s large sieve estimate [12,
Th´eor`eme 6] implies that the number of n in question is ≪ x/G(
√x), where

G(z) = ∑

n⩽z g(n), g(n) = µ2(n) ∏

p|n
 ξ(p)
p − ξ(p),

PRIME CHAINS AND PRATT TREES 13

and µ is the M¨obius function. For ﬁxed k, the argument in [24, §5.3] gives G(z) ∼ (log z)k/(k!S).
We sketch how to make explicit the dependence on k. By the argument in [24, p. 147–148],
∑

d⩽z g(d) log d = ∑

d⩽z g(d) ∑

p⩽z/d
 ξ(p) log p
p + ∑

h⩽z g(h) ∑

p|h
p>z/h
 ξ(p) log p
p

= k ∑

d⩽z g(d) log z
d + O (G(z)(B + k log2 z)) .

Adding the sum on the right side to both sides yields

G(z) log z = (k + 1) ∫ z

1
 G(t)
t dt + r(z)G(z) log z,

where r(z) ≪ B+k log2 z
log z . If δ is small enough and z ⩾ √x, then |r(z)| ⩽ 1
2. By the argument in
[24, p. 150], for some constant D and for z ⩾ √x,

(1 − r(z)) G(z)
logk z = D exp {O ( kB + k2 log2 z
log z
 )} .

By the argument on [24, p. 151–152], D−1 = k!S. Taking z = √x completes the proof. □

For given integers m1, . . . , mk−1 ⩾ 2, we will apply Lemma 5.1 with the forms f1(n) = n,
fj+1(n) = mjfj(n) + 1 (1 ⩽ j ⩽ k − 1). We have fj(n) = ajn + bj, where

(5.1) aj = m1 · · · mj−1 (j ⩾ 1), b1 = 0, bj = 1 +
 j−1∑

i=2 mi · · · mj−1 (j ⩾ 2).

Clearly, (aj, bj) = 1. Let S(m) = S be the associated singular series and let ξ(p, m) = ξ(p).

Lemma 5.2. There is a positive constant c1 so that S(m) ≪ (c1 log2(4m1 · · · mk−1))
k−1. Also,
∑

p
 k − ξ(p, m)
p log p ⩽ k (log2(4m1 · · · mk−1) + O(1)) .

Proof. We have ξ(p, m) = k if p ∤ N , where N = m1 · · · mk−1 ∏
i<j |aibj − ajbi|. Also, ξ(p, m) ⩾
1 for all p. Let x = m1 · · · mk−1 ⩾ 2
k−1. By (5.1), aj ⩽ x and bj ⩽ 1 + ∑k−2
j=1 x/2
j ⩽ x for each
j. Thus, N ⩽ xk(k−1)+1 ⩽ exp{O(log3 x)}. Since 1 − k/p ⩽ (1 − 1/p)
k for p > k, if S(m) > 0
then S(m) ⩽ ∏
p|N (1 − 1/p)
1−k ⩽ (c1 log2 N )k−1 for a constant c1. The second bound follows
from ∑

p|N (log p)/p ⩽ log2 N + O(1). □

Lemma 5.3. Let k ⩾ 1 and I ⊆ {1, . . . , k−1}. If the variables mi are ﬁxed (1 ⩽ i ⩽ k−1, i ̸∈ I),
then for any prime p, ∑

0⩽mi<p (i∈I) ξ(p, (m1, . . . , mk−1)) ⩾ p|I|+1 − (p − 1)|I|+1.

Proof. Fix p and let N (k, I) be the sum on the left side. We use induction on k, the case
k = 1 being trivial. Suppose k ⩾ 2 and the lemma holds with k replaced by k − 1. If k −
1 ̸∈ I, then ξ(p, (m1, . . . , mk−1)) ⩾ ξ(p, (m1, . . . , mk−2)) implies N (k, I) ⩾ N (k − 1, I).

14 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

If k − 1 ∈ I, then N (k, I) counts the number of (|I| + 1)−tuples (mi(i ∈ I), n) modulo p
with p|f1(n) · · · fk−1(n)(mk−1fk−1(n) + 1). The number of tuples with p|f1(n) · · · fk−1(n) is
pN (k − 1, I − {k − 1}) and the number of remaining tuples is p|I| − N (k − 1, I − {k − 1}). By the
inductive hypothesis, N (k, I) = p|I| + (p − 1)N (k − 1, I − {k − 1}) ⩾ p|I|+1 − (p − 1)
|I|+1. □

Lemma 5.4. Let k ⩾ 4, and suppose that Mi, Ni are integers satisfying Mi ⩾ 2 and 2 ⩽ Ni ⩽
2kMi for 1 ⩽ i ⩽ k − 1. For some positive constant c2, we have

∑

Ni<mi⩽Ni+Mi
(1⩽i⩽k−1)
 S(m) ≪ M1 · · · Mk−1 (c2 log k)
b exp {
O ( k log2 k
log k
 )} ,

where b is the number of variables Mi which are ⩽ 2
k2 log3 k.

Proof. Let L = ⌊log k⌋ + 1 and r = k2L. We will perform a precise averaging of the factors in
S(m) for primes p ⩽ r, and use crude estimates for larger p. If p ∤ m1 · · · mk−1, each congruence
fj(n) ≡ 0 (mod p) has exactly one solution. For h > j, fj(n) ≡ 0 (mod p) and fh(n) ≡ 0
(mod p) have a common solution if and only if p|(ajbh − ahbj). Write

(5.2) ajbh − ahbj = m1 · · · mj−1gj,h(m), gj,h(m) := 1 +
 h−1∑

i=j+1 mi · · · mh−1.

Deﬁne
 ψr(n) = ∏

p|n
p>r
 p
p − 1 , Gj,h(m) = ∏

p>r,p|gj,h(m)
p∤gi,h(m) (j+1⩽i⩽h−2)
p∤m1···mk−1
 p.

We then have
 ∏

p∤m1···mk−1
p>r
 (
1 − ξ(p, m)
p
 ) (
1 − 1
p
 )−k ⩽ ∏

1⩽j<h⩽k−1
h⩾j+2
 ψr(Gj,h(m)).

Let
 J = {(j, h) : 1 ⩽ j < h ⩽ k − 1, h ⩾ j + 2, max
j+1⩽i⩽h−1 Mi > 2
k2 log3 k},

and put J = |J | ⩽ (k−3)(k−2)
2 . Also let I = {i : Mi > 2
k2 log3 k}. Write I = ⋃A
a=1([ia, i
′
a] ∩ N),
where ia+1 ⩾ i′
a + 2 for each a. For each a and 2 + i
′
a ⩽ h ⩽ ia+1 (so h ̸∈ I),

∏

i′
a⩽j⩽h−2 ψr(Gj,h(m)) = ψr(Gh), Gh = ∏

i′
a⩽j⩽h−2 Gj,h(m).

PRIME CHAINS AND PRATT TREES 15

Since Gh ⩽ (k2
k2 log3 k)
k, Gh has O(k3 log3 k) prime factors, and thus for some constant C > 1,
ψr(Gh) ⩽ exp{
∑
p|Gh,p>r 1
p−1} ⩽ C. There are b such numbers h. Hence, by H¨older’s inequality,

∑

m S(m) ⩽ C b ∑

m
 ∏

p⩽r
 (
1 − ξ(p, m)
p
 ) (
1 − 1
p
 )−k k−1∏

i=1 ψr(mi)k−1 ∏

(j,h)∈J ψr(Gj,h(m))

⩽ C b(∑

m
 [∏

p⩽r
 (1 − ξ(p, m)
p
 ) (
1 − 1
p
 )−k] L
L−1 )1− 1
L

×
 k−1∏

i=1
 (∑

m ψr(mi)
2L(k−1)2) 1
2L(k−1) ∏

(j,h)∈J
 (
∑

m ψr(Gj,h(m))
2JL) 1
2JL .

(5.3)

If we write ψs
r = 1 ∗ βs, then βs is multiplicative and supported on square-free integers composed
of primes > r. Furthermore, if p > r ⩾ s + 1, then

(5.4) βs(p) = ( p
p − 1
 )s − 1 ⩽ es/(p−1) − 1 ⩽ 4s
p .

Thus, for each i,
∑

Ni<mi⩽Ni+Mi ψr(mi)
2L(k−1)2 ⩽ ∑

d⩽Ni+Mi β2L(k−1)2(d)Ni + Mi
d

⩽ (2k + 1)Mi ∏

p>r
 (
1 + β2L(k−1)2(p)
p
 ) ≪ kMi.
(5.5)

For ﬁxed (j, h) ∈ J , let Ml = max(Mj+1, . . . , Mh−1) > 2
k2 log3 k and write

(5.6) gj,h(m) = ml(ml+1 · · · mh−1)gj,l(m) + gl,h(m).

We’ll use
 Gj,h(m)|G
′
j,h(m) := ∏

p>r, p|gj,h(m)
p∤m1···mk−1gl,h(m)
 p,

and note that G
′
j,h(m) ⩽ gj,h(m) ⩽ k(2k + 1)
kMj+1 . . . Mh−1 ⩽ (6kMl)
k by (5.2). Fix all of
mj+1, . . . , mh−1 except for ml. By (5.4) and (5.6),

∑

ml ψr(G
′
j,h(m))
2JL = ∑

d⩽(6kMl)k
(d,gl,h(m) ∏
i̸=l mi)=1

β2JL(d) ∑

Nl<ml⩽Nl+Ml
d|G′
j,h(m)
 1 ⩽ ∑

d⩽(6kMl)k
 ( Ml
d + 1) β2JL(d)

⩽ Ml ∏

p>r
 (1 + 8JL
p2
 ) + ∏

r<p⩽(6kMl)k
 (1 + 8JL
p
 ) ≪ Ml.

(5.7)

16 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

Also,
[∏

p⩽r
 (
1 − ξ(p, m)
p
 ) (
1 − 1
p
 )−k] L
L−1 −1 ⩽ ∏

p⩽r
 (1 − 1
p
 )− k
L−1 = exp {O ( k log2 k
log k
 )} .

Therefore, by (5.3), (5.5) and (5.7),
∑

m S(m) ≪ C b (M1 · · · Mk−1)
 1
L S1− 1
L exp {
O ( k log2 k
log k
 )} ,

where
 S = ∑

m
 ∏

p⩽r
 (
1 − ξ(p, m)
p
 ) (
1 − 1
p
 )−k .

Let M ′ = ∏
p⩽r p. Since M ′ ⩽ e2r, for each i ∈ I, Mi ≫ kM ′. Hence, the number of mi ∈
(Ni, Ni + Mi] lying in a given residue class modulo M ′ is ⩽ Mi/M ′ + 1 ⩽ (1 + O(1/k))Mi/M ′.
Thus, by Lemma 5.3 and the Chinese Remainder Theorem,

S ⩽ ∑

Ni<mi⩽Ni+Mi
(i̸∈I)
 ∏

i∈I
 Mi
M ′
 (
1 + O ( 1
k
 )) ∑

mi mod M ′
(i∈I)
 ∏

p⩽r
 (1 − ξ(p, m)
p
 ) (
1 − 1
p
)−k

≪ ∏

i∈I Mi ∑

Ni<mi⩽Ni+Mi
(i̸∈I)
 ∏

p⩽r
 1
p|I|
 ( p
p − 1
)k [p|I| − 1
p
 ∑

0⩽mi<p
(i∈I)
 ξ(p, m)]

≪ M1 · · · Mk−1 ∏

p⩽r
 ( p
p − 1
 )k−1−|I| .

Noting that b = k − 1 − |I|, the lemma follows from Mertens’ estimate. □

Theorem 7. Suppose that η > 0, r ⩾ 1, and l and x are sufﬁciently large as a function of η. There
are
 ≪ x
log x (2ηe1+η)
l/2 +
 r∑

j=1 x(log2 x)
O(jl) ( (jl)
3+η

log x
 )⌊jl/(log2 jl)2⌋

primes p ⩽ x, such that there is a prime chain prl ≺ prl−1 ≺ · · · ≺ p0 = p with prl > x
(r+1)−η .

Proof. Suppose 2ηe
1+η < 1 and rl ⩽ (log x)
1/(3+η), else the theorem is trivial. Put kj = jl and
xj = x(j+1)−η for 0 ⩽ j ⩽ r. Suppose p ⩽ x and there are even integers h1, . . . , hkr so that

(5.8) p = p0 = h1p1 + 1, p1 = h2p2 + 1, . . . , pkr−1 = hkrpkr + 1,

with p0, . . . , pkr prime and pkr ⩾ xr. The vector (h1, . . . , hkr) may not be unique, but we associate
to each such p a single such vector. Each p lies in Q1 ∪ · · · ∪ Qr, where Qj is the set of primes p
so that pki < xi (i < j) and pkj ⩾ xj. By assumption, kr ⩽ (log xr)1/3.
Fix j and even integers h1, . . . , hkj satisfying h1 · · · hkj ⩽ x/xj. By Lemma 5.2,
∑

p
 kj − ξ(p; (hkj , . . . , h1))
p log p ≪ kj log2 x ≪ (log xr)
1/3 log2 x.

PRIME CHAINS AND PRATT TREES 17

By Lemma 5.1 and Stirling’s formula, the number of p = p0 ⩽ x satisfying (5.8) is

(5.9) ≪ x
h1 · · · hkj
 (2kj/e)
kj +3/2S(hkj , . . . , h1)

(log xj)kj +1 .

Let 1 ⩽ bj ⩽ kj be a parameter to be chosen later, and put Aj = 22k2
j log3 kj . Let Qj,1 be the set of
p ∈ Qj for which at least bj of the variables h1, . . . , hkj are ⩽ Aj, and Qj,2 = Qj\Qj,1.
To estimate |Qj,1|, ﬁx a set B ⊆ {1, . . . , kj} of size bj so that hi ⩽ Aj for each i ∈ B. Let
I = {1 ⩽ i ⩽ kj : i ̸∈ B} and, for 0 ⩽ i ⩽ j − 1, put ai = |B ∩ {ki + 1, . . . , ki+1}|,
Ii = I ∩ {ki + 1, . . . , ki+1}. By the deﬁnition of Qj,

(5.10) ∏

g∈Ii∪···∪Ij−1 hg ⩽ hki+1 · · · hkj ⩽ xi
xj (0 ⩽ i ⩽ j − 1).

Since hi ⩾ 2 for all i,

(5.11) ∏

g∈B
 ∑

2⩽hg⩽Aj
 1
hg ⩽ (2k2
j log3 kj)bj .

Let α = l/log xj. By (5.10) and the elementary estimate ∑
2⩽h⩽y h
−1−s ⩽ 1/s,

∑

hg (g∈I)
 1
∏
g∈I hg ⩽ ∑

hg⩾2 (g∈I)
 1
∏
g∈I hg
 j−1∏

i=0
 ( xi
xj
 )α 1
∏
g∈Ii∪···∪Ij−1 hα
g

=
 j−1∏

i=0
 ( xi
xj
 )α ∑

hg⩾2 (g∈Ii)
 1
∏
g∈Ii h
1+(i+1)α
g

⩽
 j−1∏

i=0
 ( xi
xj
 )α ( 1
(i + 1)α
 )ki+1−ki−ai

= ( 1
α
 )kj −bj 1
a02
a1 · · · jaj−1

(j!)l exp
 {

l
 j∑

i=0
 [( j + 1
i + 1
 )η − 1
]}
 .

The last sum is ⩽ η
1−η (j + 1) ⩽ 2j. Also, 1
a02
a1 · · · jaj−1 ⩽ jbj and j! ⩾ (j/e)
j. Hence,

(5.12) ∑

hg (g∈I)
 1
∏
g∈I hg ⩽ e3kj ( log xj
kj
 )kj −bj .

18 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

The number of choices for B is (
kj
bj ) ⩽ (ekj/bj)bj . By (5.9), (5.11), (5.12), and Lemma 5.2,

|Qj,1| ≪ x (c1kj log2 x)
kj +3/2

(log xj)kj +1
 (2ek3
j log3 kj
bj
 )bj e3kj ( log xj
kj
 )kj −bj

= x
log xj k3/2
j (c1e3 log2 x)kj +3/2 (2ek3
j (kj/bj) log3 kj(j + 1)η

log x
 )bj

≪ x exp
{
O(kj log3 x) + bj
[(3 + η) log kj + log (kj
bj
 ) − log2 x]}
.

(5.13)

We next estimate |Qj,2|. Place each variable hi into an interval Ji. If hi ⩽ Aj, then take
Ji = (2
li−1, 2
li] for an integer li ⩾ 1, and if hi > Aj, then take

Ji = (⌊Aj(1 + 1/kj)li−1⌋, ⌊Aj(1 + 1/kj)
li⌋]

for some integer li ⩾ 1. For brevity, write Ji = (Hi, Ki] for each i. Since Ki − Hi ⩾ Hi/(2kj),
there are at most bj values of i with Ki − Hi ⩽ Aj. Lemma 5.4 then gives
∑

h1∈J1 · · · ∑

hkj ∈Jkj
 S(hkj , . . . , k1)
h1 · · · hkj ⩽ 1
H1 · · · Hkj
 ∑

h1∈J1 · · · ∑

hkj ∈Jkj S(hkj , . . . , h1)

≪ (c2 log kj)
bj exp {
O ( kj log2 kj
log kj
 )} kj∏

i=1
 Ki − Hi
Hi .

By our deﬁnition of the intervals Ji,

kj∏

i=1
 Ki − Hi
Hi ⩽ ∏

1⩽i⩽kj
Ki−Hi<Aj
 2 ∑

Hi<hi⩽Ki
 1
hi
 ∏

1⩽i⩽kj
Ki−Hi⩾Aj
 (
1 + O ( 1
kj
 )) ∑

Hi<hi⩽Ki
 1
hi

≪ 2
bj ∑

h1∈J1 · · · ∑

hkj ∈Jkj
 1
h1 · · · hkj .

Thus, after summing over all possibilities for J1, . . . , Jkj , we obtain by (5.9)

|Qj,2| ≪ x(2kj/e)
kj +3/2

(log xj)kj +1 exp {
O ( kj log2 kj
log kj + bj log2 kj
)} ∑

h′
1,...h′
kj
 1
h
′
1 · · · h
′
kj ,

where h
′
ki+1 · · · h
′
kj ⩽ 2
kj −kihki+1 · · · hkj ⩽ 2
kj xi/xj for 0 ⩽ i ⩽ j − 1. For positive α0, . . . , αj−1,

∑

h′
1,...,h′
kj
 1
h
′
1 · · · h
′
kj ⩽
 j−1∏

i=0
[(
2
kj xi
xj
 )αi ∞∑

h′
ki+1,...,h′
ki+1 =2
 1
(h
′
ki+1 · · · h
′
ki+1)1+α0+···+αi
 ]

⩽
 j−1∏

i=0
 (2
kj xi
xj
 )αi ( 1
α0 + · · · + αi
 )l .

PRIME CHAINS AND PRATT TREES 19

If we ignore the factors 2
kj αi, the optimal choice of parameters is

αi = l
(j + 1)η log xj
 [ (i + 2)η(i + 1)η

(i + 2)η − (i + 1)η − (i + 1)ηi
η

(i + 1)η − iη
 ], i = 0, . . . , j − 1.

Since (i + 2)η − (i + 1)η ⩾ η(i + 2)η−1,

α0 + · · · + αi ∈ [ l(i + 1)(i + 2)η

η(j + 1)η log xj , l(i + 2)(i + 1)η

η(j + 1)η log xj
 ]
.

Recalling kj = jl, the sum on h
′
1, . . . , h′
kj is at most

2
kj (α0+···+αj−1) exp
 { j−1∑

i=0 αi
[( j + 1
i + 1
 )η − 1
] log xj
} ( η(j + 1)η log xj
l
 )kj 1
(j!)l((j + 1)!)ηl .

The exponential factor is e
lj = e
kj and (j + 1)! ⩾ e
−j−1(j + 1)j+1, so
∑

h′
1,...,h′
kj
 1
h
′
1 · · · h
′
kj ⩽ 2
2k2
j /(η log xj ) ( ηe2+η log xj
kj
 )kj .

Therefore,

(5.14) |Qj,2| ≪ x
log x (
2ηe
1+η)kj exp {
O ( kj log2 kj
log kj + bj log2 kj
)} .

Finally, put bj = ⌊kj/(log2 kj)2⌋, and sum the inequalities (5.13) and (5.14) for 1 ⩽ j ⩽ r. □

Proof of Theorem 4. Let η = 0.15718, l = ⌊(log x)
ε⌋ and r = ⌊(log x)
β⌋
, where ε and β are ﬁxed
and satisfy 0 < ε + β < 1
3+η . Then log xr ≍ (log x)
1−ηβ. For the primes p not counted in Theorem
7, the primes at level rl of the Pratt tree are all < xr, so H(p) ⩽ log xr
log 2 + 1 + rl ≪ (log x)
0.95022

if we take β sufﬁciently close to 1
3+η . By Theorem 7, the number of exceptional primes p ⩽ x is
O(x exp{−(log x)δ}) for some δ > 0. □

Proof of Theorem 5. Let x be large, x/ log x < n ⩽ x and suppose there is a prime p > x
ε/2 such
that p|φk(n). Then either (i) there is a prime q > xε/2 and 0 ⩽ j ⩽ k such that q2|φj(n), or (ii)
there is a prime chain p = pk ≺ pk−1 ≺ · · · ≺ p1 ≺ p0 with p0|n. In case (i), let j be the smallest
such index. Using the uniform estimate ∑

p⩽x
p≡1 (mod m)
 1
p ≪ log2 x
φ(m) ,

coming from the Brun-Titchmarsh inequality, the number of integers in category (i) is

⩽ ∑

q>xε/2
 x
q2 +
 k∑

j=1
 ∑

xε/2<q⩽x
 ∑

pj−1≡1 (mod q2)
pj−1⩽x
 ∑

pj−2≡1 (mod pj−1)
pj−2⩽x
 · · · ∑

p0≡1 (mod p1)
p0⩽x
 x
p0

≪ε,k x1−ε/2

log x +
 k∑

j=1
 x1−ε/2(log2 x)
j

log x ≪ε,k x1−ε/2.

20 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

Consider n in category (ii). Take η = 1
7, let r be the smallest integer with (r + 1)
−η < ε/2, let l be
sufﬁciently large, l ⩽ log2 x and k = rl. By Theorem 7, for xε/2 < y ⩽ x, the number of p0 ⩽ y is
O(y/ log2 y + y(2ηe
1+η)−l/2/ log y). By partial summation, the number of n is ≪ε x(2ηe1+η)
−l/2.
Taking l large enough, depending on ε and δ, completes the proof. □

6. STOCHASTIC MODEL OF PRATT TREES

In this section, we develop a model of the Pratt trees which explains Conjectures 2 and 3. Factor
n as n = ∏Ω(n)
j=1 pj(n), with p1(n) ⩾ p2(n) ⩾ · · · . Put pj(n) = 1 for j > Ω(n) and let

S(n) = ( log p1(n)
log n , log p2(n)
log n , . . .
) .

The distribution of the ﬁrst component of S(n) has been greatly studied, the results having wide
application in the theory of numbers (see e.g. the comprehensive survey article [26]). We have
3

P(log p1(n) ⩽ 1
u log n) = ρ(u), where ρ is the Dickman function, the unique continuous solution
of the differential-delay equations ρ(u) = 1 (0 ⩽ u ⩽ 1), uρ
′(u) = −ρ(u − 1) (u > 1). The com-
plete distribution of S(n), found by Billingsly in 1972 [11], corresponds to the Poisson-Dirichlet
distribution with parameter 1, P D(1) for short (more precisely, for each j, the ﬁrst j components
of S(n) are distributed as the ﬁrst j components of the P D(1) distribution). The joint distribution
of the components in the P D(1) distribution can easily be expressed in terms of ρ. There is a
simpler characterization of the distribution, found by Donnelly and Grimmett [17]. Let U1, U2, . . .
be independent random variables with uniform distribution on [0, 1]. Let x = (x1, x2, . . .) be the
inﬁnite dimensional vector formed from the decreasing rearrangement of the numbers

(6.1) y1 = U1, y2 = (1 − U1)U2, y3 = (1 − U1)(1 − U2)U3, . . . .

Then x has the P D(1) distribution. The paper [17] gives a simple, transparent proof that (x1, . . . , xk)
and the ﬁrst k components of S(n) have the same distribution.
Since ∑ xi = 1 with probability 1, we can interpret the P D(1) distribution as a random partition
of the unit interval [0, 1] into an inﬁnite number of parts achieved by cutting [0, 1] at a random place
(with uniform distribution), then cutting the right sub-interval at a random place, and so on.

Conjecture 5. As p runs over the set of primes, S(p − 1) has P D(1) distribution.

Conjecture 5 is widely believed, and is a simple consequence of EH. Unconditionally, we know
little about primes in progressions to very large moduli. Assume that S(p − 1) has P D(1) distribu-
tion, S(q − 1) has P D(1) distribution for each prime q|(p − 1), the vectors S(q − 1) for q|(p − 1)
are independent, and so forth. The primes o4n the ﬁrst level of the tree, on a logarithmic scale,
correspond to a random partition of [0, 1]. The primes on the second level correspond to randomly
partitioning each of the parts of the original partition, etc. The entire procedure corresponds to
what is known as a discrete-time random fragmentation process. Random fragmentation processes
have been used to model a variety of physical phenomena (e.g., genetic mutations, planet forma-
tion) and the growth of certain data structures in computer science. Discrete time fragmentation
processes may be recast in the language of branching random walks, which we now describe.

3If B ⊆ A ⊆ N, we say P(n ∈ B|n ∈ A) = α if lim
x→∞ |{n ∈ B : n ⩽ x}|
|{n ∈ A : n ⩽ x}| = α.

PRIME CHAINS AND PRATT TREES 21

Let Mn be the size of the largest object at time n. Then Mn is a model of Qn := log qn
log p , where qn
is the largest prime at level n of the tree. The event {Mn < log 2
log p } is a model of the statement “all
the primes at level n of the Pratt tree for p are < 2”; that is, H(p) < n. Thus, H(p) is modeled by
the random variable T ( log 2
log p ), where T (ε) = min{n : Mn ⩽ ε}.
Assuming EH, Lamzouri [28] showed that Qn has the same distribution as Mn for each ﬁxed n
(he studies the distribution of P +(φn(m)) for all integers m; the same proofs give the distribution
of Qn). Further, on EH, Lamzouri shows that P{Qn ⩽ 1
u} = P{Mn ⩽ 1
u } = ρn(u), where, for
each ﬁxed n,

(6.2) ρn(u) = ( 1 + o(1)
logn−1(u) logn(u)
)u (u → ∞),

with log0(u) = u. Our goal is to understand the distribution of Mn as n → ∞.
Create a tree structure from the random fragmentation process as follows: label the root node
with zero, beneath the root node put an inﬁnite number of child nodes, each corresponding to
one of the fragments of the initial segment [0, 1]. Each of these nodes has an inﬁnite number of
child nodes, corresponding to the fragments in the second step of the process, and so on. Each
node is labeled with the number − log x, where x is the fragment size. This randomly labeled
tree corresponds to a branching random walk (BRW). More generally, an initial ancestor is at
the origin, and who forms the zeroth generation. This parent then produces children, the ﬁrst
generation, which are randomly displaced from the parent according to some law. Each of these
children behaves like an independent copy of the parent, their children randomly displaced from
their parent according to the same law, and forming the second generation, and so on. In our case,
each parent produces an inﬁnite number of offspring, the displacements from their parent given by
V = {− log y : y ∈ Z}, where Z is a point set with P D(1) distribution. We’ll say that V has
LP D (logarithmic Poisson-Dirichlet) distribution from now on.
Let Bn be the minimum label of an individual at time n, so that Bn = − log Mn. The ﬁrst order
behavior of the analog of Bn (law of large numbers) for a general BRW was determined in the
1970s by Biggins, Hammersley and Kingman (see [9]). In our case, Biggins’ theorem [9] implies
Bn ∼ n
e as n → ∞ almost surely. Thus, T ( log 2
log p ) ∼ e log2 p as p → ∞ almost surely, which
justiﬁes Conjecture 2.
Let bn = median(Bn). The study of Bn naturally breaks into two parts: (i) global behavior:
asymptotics for bn, and (ii) local behavior: the distribution of Bn − bn. A result of McDiarmid [31]
can be used to prove bn = n
e + O(log n), and this was sharpened by Addario-Berry and Ford [1] to

Theorem 8. We have bn = n
e + 3
2e log n + O(1).

Corollary 2. We have median
(
T (ε)) = e log(1/ε) − 3
2 log2(1/ε) + O(1).

This justiﬁes part of Conjecture 3. One ingredient in the proof is the following expectation
identity. Let Zn(t) be the number of generation n individuals with position ⩽ t, and let z
(n) be the
set of positions of generation n individuals. If v = (v1, v2, . . .) has P D(1) distribution, (6.1) gives

E
 ∞∑

j=1 vs
j = E
 ∞∑

k=1
(
(1 − U1) · · · (1 − Uk−1)Uk)s =
 ∞∑

k=1
 1
(1 + s)k = 1
s ,

22 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

since EU s
i = E(1 − Ui)s = 1/(1 + s). By the branching property,

E ∑

zn∈z(n) e−szn = E ∑

zn−1∈z(n−1) e
−szn−1E ∑

z1∈z(1) e−sz1 = 1
s E ∑

zn−1∈z(n−1) e
−szn−1.

By induction, the left side is 1/s
n, so ∫ ∞
0 e−stdEZn(t) = 1/s
n. Therefore, EZn(t) = tn/n!.
Because t
n/n! ≈ 1 when t = n
e + 1
2e log n+O(1), a naive guess would be bn = n
e + 1
2e log n+O(1).
However, for reasons clearly explained in [2] and executed in [1], the leftmost point in the n-th
generation of a branching random walk has an atypical ancestry with high probability. Denote the
locations of points in the ancestral line of this leftmost point by 0, z1, z2, . . . , zn = Bn with Bn
close to bn. Then usually zj ⩾ j
n zn − O(1) (1 ⩽ j ⩽ n/2). A randomly chosen point zj ∈ z
(n)

has this property with probability of order 1/n, so the expected number of such zj is in fact of
order t
n/(n · n!), which is ⩾ 1 when t ⩾ n
e + 3
2e log n + O(1).
We next discuss the local behavior of Bn. Under very general conditions on the BRW, it is
known that Bn − bn is a tight sequence.4 The basic idea is that a single individual will, with high
probability, produce many offspring a few generations later which are close by. In our situation,
tightness on the left for H(p) is relatively easy to prove unconditionally:

Proof of Theorem 6. The conclusion is trivial if g(x1/2) ⩽ 3K, so we will assume that g(x1/2) >
3K. Let m = ⌊g(x1/2)/K⌋ so that m ⩾ 3. Put Q = x2−m and let T be the set of primes
x1/2 < p ⩽ x such that there is a prime q|(p − 1) with Q < q ⩽ x1/4 and H(q) ⩾ h(q). For p ∈ T ,

H(p) ⩾ 1 + h(q) ⩾ h(Q) ⩾ h(x) − mK ⩾ h(p) − g(p),

while by sieve methods (Theorem 4.2 of [24]), for large x

|{x1/2 < p ⩽ x : p ̸∈ T }| ≪ x
log x
 ∏

Q<q⩽x1/4
H(q)⩾h(q)
 (
1 − 1
q
 ) ≪ x
log x2
−mc. □

It is also known that under certain conditions on the displacement law of the BRW (e.g. [3]), the
analog of Bn − bn converges in probability to a random variable as n → ∞. This is not known in
our case.

Conjecture 6. Bn − bn → X as n → ∞ for a random variable X with continuous distribution.

If X exists, and the medians satisfy bn+1 − bn → e−1 as n → ∞ (plausible in light of Theorem
(8)), it is easy to see that X d
= −1/e + mini(zi + Xi), where (z1, z2, . . .) has LP D distribution,
X1, X2, . . . are independent copies of X, and d
= means “has the same distribution as”. This follows
by conditioning on the positions of the ﬁrst generation individuals (the points zi); that is, using
Bn d
= mini(zi + B(i)
n−1), where B(i)
n−1 are independent copies of Bn−1. The solutions X of this
recursive distributional equation are not known, however.
Unconditionally (whether X exists or not), we prove that Bn − bn has an exponentially decreas-
ing left tail and doubly-exponentially decreasing right tail. Consequently, if Conjecture 6 holds,
then all moments of X exist.

4A sequence X1, X2, . . . of random variables is tight if for every ε > 0 there is a number M so that for all j,
P(|Xj| > M ) ⩽ ε. In other words, the distribution of Xj does not spread out as j → ∞.

PRIME CHAINS AND PRATT TREES 23

Theorem 9. (a) For any c1 < e, we have

P{Bn − bn ⩽ −x} ≪c1 e−c1x (n ⩾ 1, x ⩾ 0),

and for any c2 > 2e log(2e) and η > 0,

P{Bn − bn ⩽ −x} ≫c2,η e
−c2x (n ⩾ 1, 0 ⩽ x ⩽ (1/2e − η)n);

(b) for any c3 < 1 there is a constant c4, depending on c3, so that

P{Bn ⩾ bn + x} ⩽ exp (
−e
c3(x−c4)) (n ⩾ 1, x ⩾ 0).

Remark 3. By (6.2), part (b) is nearly best possible; that is, the conclusion is false if c3 > 1.

The next two lemmas hold for very general branching random walks. A notable feature is that
they are local results, and tightness of Bn − bn can be proved without knowing anything about the
growth of bn. We will use Theorem 8 to prove the stronger tail estimates.

Lemma 6.1. For positive integers m, n and positive real numbers M , N ,

P{Bm+n ⩾ M + N } ⩽ E[(P{Bn ⩾ N })
Zm(M )].

Proof. Suppose Bm+n ⩾ M + N and Zm(M ) = k. For each of these k individuals, all of their
descendants in generation m + n are offset from their generation m ancestor by at least N . □

Lemma 6.2. Let m, n be positive integers and let M > 0, ε > 0 be real. If E{(1 − ε)
Zm(M )} ⩽ 1
2,
then P{Bn ⩽ bn+m − M } ⩽ ε. In particular, the conclusion holds if P{Zm(M ) < 1/ε} ⩽ 1
5.

Proof. Let q be the ε-quantile of Bn, that is, P{Bn ⩽ q} = ε. By Lemma 6.1,

P{Bm+n ⩾ M + q} ⩽ E [(P{Bn ⩾ q})
Zm(M )] ⩽ 1
2 .

Therefore, M + q ⩾ bm+n, and thus P{Bn ⩽ bm+n − M } ⩽ P{Bn ⩽ q} = ε. To prove the
second part, assume that P{Zm(M ) < 1/ε} ⩽ 1
5. Then

E {(1 − ε)Zm(M )} ⩽ P{Zm(m) < 1
ε } + (1 − P{Zm(M ) < 1
ε })(1 − ε)
1/ε ⩽ 1
5 + 4
5e < 1
2. □

Lemma 6.3. For real t ⩾ 1 and integer k ⩾ 1, we have P{Z1(t) ⩾ k} ⩽ (et/k)
k−1.

Proof. The conclusion is trivial if k ⩽ et, so we suppose k > et. Take s = k
t − 1. By (6.1),

P{Z1(t) ⩾ k} ⩽ P {(1 − U1) · · · (1 − Uk−1) ⩾ e−t}

⩽ est ∫ 1

0 · · · ∫ 1

0 [(1 − u1) · · · (1 − uk−1)]
sdu1 · · · duk−1 = e
st

(1 + s)k−1 . □

Lemma 6.4. For all r ⩾ 1, θ > 1 and ε > 0, if x is large then P{Zr(x) ⩾ θx} ⩽ exp{−(θ − ε)x}.

Proof. When r = 1, this follows from Lemma 6.3. Assume it to be true for some r ⩾ 1, let
θ and ε be given, and assume without loss of generality that θ − ε > 1. The probability that
Zr(x) ⩾ (θ − ε/3)
x is ⩽ exp{−(θ − ε/2)x} for large x. Now suppose Zr(x) = j < (θ − ε/3)
x and
Zr+1(x) ⩾ θx. Let mi be the number of children of the i-th largest point in z(r) which are offset at

24 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

most x from their parent. Let I be the set of indices with mi ⩾ 100x. Note that m1+· · ·+mj ⩾ θx.
With j, m1, . . . , mj ﬁxed, by Lemma 6.3 the probability that Zr+1(x) ⩾ θx is at most

j∏

i=1 P{Z1(x) ⩾ mi} ⩽ ∏

i∈I e−2mi ⩽ e−2(θx−100xj) ⩽ exp {−θx} .

As mi ⩽ ex, the number of choices for j, m1, . . . , mj is at most exp{(θ − ε/4)
x}. For large x,

P{Zr(x) ⩾ θx} ⩽ exp{−(θ − ε/2)
x} + exp{(θ − ε/4)x − θx} ⩽ exp{−(θ − ε)x}. □

Proof of Theorem 9. Let a > 1/e and 0 < η < ae/2. By [10, Theorem 2], for large r we have
P{Zr(ar) ⩽ (ae − η)r} ⩽ 1
5. Let r be so large that, in addition, bn+r ⩾ bn + (1/e − η)r for all
n (r exists by Theorem 8). Apply Lemma 6.2 with M = ar, m = r, ε = (ae − η)−r. For large
integers r,
 P{Bn ⩽ bn − (a − 1/e + η)r} ⩽ P{Bn ⩽ bn+r − ar} ⩽ (ae − η)
−r.

The ﬁrst estimate follows with c1 = log(ae−η)
(a−1/e+η) . Fix a, let η → 0, then let a → 1/e, so that c1 → e.
For the second part of (a), take η > 0 and r as before (but ﬁxed here), and let δ = (1/e − η)r, so
that bn+r ⩾ bn + δ for all n. Since ρ(u) = 1 − log u for 1 ⩽ u ⩽ 2, P(Z1(ε) ⩾ 1) = 1 − ρ(e
ε) = ε
when 0 ⩽ ε ⩽ log 2. Considering the “leftmost child of the leftmost child of the . . . of the initial
ancestor” in the branching random walk, we have P{Bkr ⩽ δk/2} ⩾ P{Z1(δ/2r) ⩾ 1}kr =
(δ/2r)
kr for every k ⩾ 1. Hence,

P{Bn ⩽ bn−kr + δk/2} ⩾ P{Bn−kr ⩽ bn−kr}P{Bkr ⩽ δk/2} ⩾ 1
2
 ( δ
2r
 )kr .

By assumption, bn−kr + δk/2 ⩽ bn − δk/2. Hence, for 0 ⩽ k ⩽ n/r we have

P{Bn ⩽ bn − δk/2} ⩾ 1
2
 ( δ
2r
 )kr .

This gives the desired bound when 0 ⩽ x ⩽ δn
2r , with c′
1 = 2r
δ log 2r
δ .
To show part (b), we use induction on n to show that

(6.3) P{Bn ⩾ bn + x} ⩽ 2
− exp{c3(x−c5)}

for n ⩾ 1 and x ⩾ 0, where c5 is sufﬁciently large. Theorem 9 (c) then follows with c4 =
c5 − log log 2
c3 . As (6.3) is trivial for 0 ⩽ x ⩽ c5, we may assume x ⩾ c5. Let r, δ be such that
bn+r − bn ⩾ δ > 0 for all n (the relationship between r and δ is unimportant). Let A be a large
integer, so that if R = Ar and ∆ = Aδ, then 2e
2−∆ ⩽ 1 − c3. Also suppose c3 ⩾ 1
2. For
1 ⩽ n ⩽ R, (6.2) implies P{Bn ⩾ bn + x} ⩽ P{Bn ⩾ x} = ρn(e
x) ⩽ exp{−e
x} if c5 is large
enough. Suppose now that (6.3) has been proved for 1 ⩽ n ⩽ m − 1, where m − 1 ⩾ R. Deﬁne
λj = ∆ + log j−1
c3 for j ⩾ 1 Let j0 be the largest index j with λj ⩽ x + ∆. Let z1 ⩽ z2 ⩽ · · · be
the points in z
(R). For 1 ⩽ j ⩽ j0, let Pj be the event {zi > λi (i < j), zj ⩽ λj}, and the Q be the
event {zi > λi (1 ⩽ i ⩽ j0)}. If Pj, then the generation m points descending from each of the j

PRIME CHAINS AND PRATT TREES 25

points z1, . . . , zj are offset from their generation R ancestor by at least bm + x − λj. So

P{Bm ⩾ bm + x} ⩽
 j0∑

j=1 P[Pj]P{Bm−R ⩾ bm + x − λj}j + P[Q].

Since bm ⩾ bm−R + ∆, the induction hypothesis implies that the sum on j is

⩽
 j0∑

j=1 P[Pj]2
−j exp{c3(x−c5+∆−λj )} ⩽
 j0∑

j=1 P[Pj]2
− exp{c3(x−c5)+1} ⩽ 2
−1−exp{c3(x−c5)}.

Now suppose that Q holds. By the assumption on A,

∑

j⩽j0 e−zj ⩽
 j0∑

j=1 e−λj ⩽ e−∆+1/c3 ∞∑

j=1 j−1/c3 ⩽ 1
2 .

As λj0 ⩾ x + ∆ − (λj0+1 − λj0) ⩾ x,
∑

z∈z(R)
z⩾x
 e
−z = 1 − ∑

z∈z(R)
z<x
 e−z ⩾ 1
2.

Let ε = 1
3(e − ec3) and θ = e − ε, so that ec3 < θ − ε < θ < e. For some integer k ⩾ x, there are
⩾ θk points of z(R) in [k − 1, k), for otherwise

∑

z∈z(R)
z⩾x
 e−z ⩽ ∑

k⩾x e ( θ
e
 )k < 1
2 .

By Lemma 6.4, P[Q] ⩽ ∑

k P{ZR(k) ⩾ θk} ⩽ 2e
−(θ−ε)x. This completes the proof of (b). □

Acknowledgments. The authors wish to thank L. Addario-Berry, J. Bertoin, C. Elsholtz, A.
Granville, A. Hildebrand, I. K´atai, C. Pomerance, Y. Sinai, and R. Song for helpful conversations.

REFERENCES

[1] L. Addario-Berry and K. Ford, Poisson-Dirichlet branching random walks, preprint.
[2] L. Addario-Berry and B. Reed, Minima in branching random walks, Ann. Prob. 37 (2009), 1044–1079.
[3] M. Bachman, Limit theorems for the minimal position in a branching random walk with independent log-
concave displacements, Adv. Appl. Prob. 32 (2000), 159–176.
[4] R. C. Baker and G. Harman, Shifted primes without large prime factors, Acta Arith. 83 (1998), 331–361.
[5] W. D. Banks, J. Friedlander, F. Luca, F. Pappalardi and I. E. Shparlinski, Coincidences in the values of the
Euler and Carmichael functions, Acta Arith. 122 (2006), 207–234.
[6] W. D. Banks and I. E. Shparlinski, On values taken by the largest prime factor of shifted primes, J. Aust.
Math. Soc. 82 (2007), no. 1, 133–147.
[7] N. L. Bassily, I. K´atai and M. Wijsmuller, Number of prime divisors of φk(n), where φk is the k-fold iterate
of φ, J. Number Theory 65 (1997), 226–239.
[8] J. Bayless, The Lucas-Pratt primality tree, Math. Comp. 77 (2008), 495-502.
[9] J. D. Biggins, The ﬁrst- and last-birth problems for a multitype age-dependent branching process, Adv.
Appl. Prob. 31 (1976), 446–459.
[10] J. D. Biggins, Chernoff’s theorem in the branching randon walk, J. Appl. Prob. 14 (1977), 630–636.

26 KEVIN FORD, SERGEI V. KONYAGIN AND FLORIAN LUCA

[11] P. Billingsly, On the distribution of large prime divisors, Collection of articles dedicated to the memory of
Alfr´ed R´enyi, I. Period. Math. Hungar. 2 (1972), 283–289.
[12] E. Bombieri, Le grand crible dans la th´eorie analytique des nombres, 2nd ed. (French. English summary)
Ast´erisque No. 18. Soci´et´e Math´ematique de France, Paris, 1987.
[13] C. W. Borchardt, ¨Uber eine Interpolationsformel f¨ur eine Art Symmetrischer Functionen und ¨uber Deren
Anwendung, Math. Abh. der Akademie der Wissenschaften zu Berlin (1860), 1–20.
[14] M. A. Cherepnev, Some properties of large prime divisors of numbers of the form p − 1, Mat. Zametki 80
(2006), 920–925. (Russian). English translation in Math. Notes 80 (2006), 863–867.
[15] R. Crandall and C. Pomerance, Prime numbers: a computational perspective, 2nd ed., Springer-Verlag,
2005.
[16] H. Davenport, Multiplicative number theory, 3rd ed., Graduate Texts in Mathematics vol. 74, Springer-
Verlag, New York, 2000.
[17] P. Donnelly and G. Grimmett, On the asymptotic distribution of large prime factors, J. London Math. Soc.
(2) 47 (1993), 395–404.
[18] P. Erd˝os, On the normal number of prime factors of p − 1 and some related problems concerning Euler’s
φ-function, Quart. J. Math. Oxford 6 (1935), 205-213.
[19] P. Erd˝os, A. Granville, C. Pomerance, and C. Spiro, On the normal behavior of the iterates of some arith-
metic functions, in Analytic Number Theory, Proceedings of a conference in honor of Paul T. Bateman,
Birkh¨auser, Boston, 1990, 165–204.
[20] P. Erd˝os and C. Pomerance, On the normal number of prime factors of φ(n), Number theory (Winnipeg,
Man., 1983). Rocky Mountain J. Math. 15 (1985), no. 2, 343–352.
[21] K. Ford and F. Luca, The number of solutions of λ(x) = n, to appear in INTEGERS, special volume in
honor of Melvyn Nathanson and Carl Pomerance.
[22] K. Ford, F. Luca and C. Pomerance, Common values of the arithmetic functions φ and σ, Bull. London
Math. Soc. 42 (2010), 478–488.
[23] B. Green and T. Tao, The primes contain arbitrarily long arithmetic progressions, Ann. Math. 167 (2008),
481–547.
[24] H. Halberstam and H.-E. Richert, Sieve methods, Academic Press, London, 1974.
[25] R. R. Hall and G. Tenenbaum, Divisors, Cambridge Tracts in Math., 1988.
[26] A. Hildebrand and G. Tenenbaum, Integers without large prime factors, J. de Th´eorie des Nombres de
Bordeaux, 5 (1993), 411–484.
[27] I. K´atai, Some problems on the iteration of multiplicative number-theoretical functions, Acta Math. Acad.
Scient. Hung. 19 (1968), 441–450.
[28] Y. Lamzouri, Smooth values of iterates of the Euler phi-function, Canad. J. Math. 59 (2007), 127–147.
[29] F. Luca and C. Pomerance, Irreducible radical extensions and Euler-function chains, in “Combinatorial
number theory”, 351–361, de Gruyter, Berlin (2007).
[30] G. Martin and C. Pomerance, The iterated Carmichael λ-function and the number of cycles of the power
generator, Acta Arith. 188 (2005), 305–335.
[31] C. McDiarmid, Minimal positions in a branching random walk, Ann. Appl. Prob. 5 (1995), no. 1, 128–139.
[32] C. Pomerance, Very short primality proofs, Math. Comp. 48 (1987), 315–322.
[33] V. Pratt, Every prime has a succinct certiﬁcate, SIAM J. Comput. 4 (1975), no. 3, 214–220.

KF: DEPARTMENT OF MATHEMATICS, UNIVERSITY OF ILLINOIS AT URBANA-CHAMPAIGN URBANA, 1409
WEST GREEN ST., URBANA, IL 61801, USA
E-mail address: ford@math.uiuc.edu

SVK: DEPARTMENT OF MECHANICS AND MATHEMATICS, MOSCOW STATE UNIVERSITY, MOSCOW, 119992,
RUSSIA
E-mail address: konyagin@ok.ru

PRIME CHAINS AND PRATT TREES 27

FL : INSTITUTO DE MATEM ´ATICAS, UNIVERSIDAD NACIONAL AUTONOMA DE M ´EXICO, AP. POSTAL 61-3
(XANGARI), C.P. 58089, MORELIA, MICHOAC ´AN, M ´EXICO
E-mail address: fluca@matmor.unam.mx
