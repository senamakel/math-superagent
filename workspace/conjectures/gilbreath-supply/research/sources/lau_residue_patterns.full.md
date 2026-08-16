<!-- source: https://arxiv.org/pdf/2409.12819 | converted from PDF -->

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES

CHEUK FUNG (JOSHUA) LAU

Abstract. Dickson’s conjecture and the Hardy–Littlewood prime tuple conjecture pre-
dict that every pattern of reduced residue classes modulo q is attained by infinitely many
strings of m consecutive primes. At present, however, even proving that a single non-
constant residue class pattern of length m occurs infinitely often is beyond the reach of
existing methods. Combining Dirichlet’s theorem on primes in arithmetic progressions
with a theorem of Shiu (2000) shows that, for any m, q ∈ N with q ≥ 3, at least mφ(q)
residue class patterns of length m are attained by infinitely many consecutive primes.

In this paper, we prove that if q is squarefree, every prescribed sequence of at least
60m log m reduced residue classes mod q contains, in order, an m-term block pattern that
occurs infinitely often among consecutive primes, with each constant block of length at
most ⌈log m⌉. A recursive combinatorial argument then shows that if q is squarefree and
q ≫ (log m)
2, then at least ≫ m
(log m)10 φ(q)
2

residue class patterns of length m occur infinitely often among consecutive primes. More-
over, we also show that if q is squarefree and q ≫ (log m)
2, then at least

≫ e
−O(m log2 m/ log m)φ(q)
m/⌈log m⌉

residue class patterns of length m occur infinitely often among consecutive primes. The
proof consists of a modification of the Maynard–Tao sieve found in Banks, Freiberg, and
Maynard (2016), by considering the r-th moment instead of the 2nd moment for an inte-
ger r depending on m, which is then combined with an Erdős–Rankin type construction.

Contents

1. Introduction 2

2. Outline 5

3. Acknowledgements 6

4. Notation 6

5. A Modified Maynard–Tao Sieve 7

6. A Modified Erdős–Rankin Type Construction 16

7. Proofs of Main Result 19

8. Number of Attainable Residue Class Patterns 21

References 25

2020 Mathematics Subject Classification. Primary 11N05, 11N13; Secondary 11N36.
Key words and phrases. prime numbers, sieve methods, residue classes.
1

arXiv:2409.12819v2  [math.NT]  13 Jul 2026

2 CHEUK FUNG (JOSHUA) LAU

1. Introduction

A central theme in analytic number theory is that, after accounting for the obvious
local congruence obstructions, the prime numbers should behave like a random set. This
philosophy underlies the Hardy–Littlewood prime tuple conjecture and predicts that ev-
ery admissible local pattern of primes should occur infinitely often. One way to study
this phenomenon is to examine the residue classes of consecutive primes modulo a fixed
integer q.

For q, m ∈ N with q ≥ 2, x ∈ R and a ∈ ∏m
i=1(Z/qZ)
×, define

π(x; q, a) = #{pn ≤ x : pn+i−1 ≡ ai (mod q) for all i = 1, 2, . . . , m},

where pi denotes the i-th prime. Thus π(x; q, a) counts occurrences of a prescribed residue
class pattern among m consecutive primes.

Understanding these patterns is closely related to the broader question of how ran-
domly distributed consecutive primes are. Numerical investigations and probabilistic mod-
els suggest that, apart from congruence restrictions, every residue class pattern should
occur infinitely often. A consequence of Dickson’s conjecture states the following.

Conjecture 1.1. For any q, m ∈ N with q ≥ 2 and a ∈ ∏m
i=1(Z/qZ)
×, π(x; q, a) → ∞ as
x → ∞. Equivalently,

#
 {

a ∈
 m∏

i=1(Z/qZ)
× : π(x; q, a) → ∞ as x → ∞

}
 = φ(q)
m.

Additionally, the Hardy–Littlewood prime tuple conjecture predicts the quantitative
asymptotic behaviour of π(x; q, a). Recently, more refined heuristics were developed by
Lemke Oliver and Soundararajan (2016). Their work predicts substantial biases for finite
ranges, for example, consecutive primes tend to avoid repeating the same residue class
modulo q more often than naive randomness would suggest, but these biases are expected
to disappear asymptotically.

Despite these strong heuristic predictions, our current understanding remains ex-
tremely limited. Dirichlet’s theorem on primes in arithmetic progressions states that
π(x; q, a) → ∞ as x → ∞ for any a ∈ (Z/qZ)
×, so Conjecture 1.1 is known when
m = 1. For general m ∈ N, we have the following result of Shiu (2000).

Theorem 1.2 (Shiu). For any m, q ∈ N with q ≥ 2 and a ∈ (Z/qZ)
×, let a = (a, . . . , a) ∈∏m
i=1(Z/qZ)
×. Then, π(x; q, a) → ∞ as x → ∞.

Moreover, Maynard (2016) proved that π(x; q, (a, . . . , a)) ≫ π(x). However, even prov-
ing that a single non-constant residue class pattern of length m occurs infinitely often
among consecutive primes is beyond the reach of existing methods. In an easier setting of
consecutive sums of two squares instead of primes, Kimmel and Kuperberg (2024, 2025)
considered E = {c
2 + d2 : c, d ∈ N} = {En : n ∈ N},

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 3

and call a ∈ Z/qZ E-admissible if there is c, d ∈ N such that c
2 + d
2 ≡ a (mod q). For an
m-tuple of admissible residue classes a = (a1, ..., am) ∈ (Z/qZ)m, let

N (x, q, a) = #{En ≤ x : En+i−1 ≡ ai (mod q) ∀1 ≤ i ≤ m}.

Kimmel and Kuperberg (2024) proved that for any q ∈ N with q ≥ 2 and a1, a2, a3 ∈ Z/qZ
E-admissible, N (x, q, (a1, a2, a3)) → ∞ as x → ∞. For a general m ∈ N and squarefree
q ∈ N, Kimmel and Kuperberg (2025) proved that for any m-tuple a that is a concate-
nation of two constant tuples (a1, . . . , a1) and (a2, . . . , a2) with a1, a2 ∈ (Z/qZ)
×, we have
N (x, q, a) → ∞ as x → ∞. Even in this easier setting, we are very far from proving that
all E-admissible tuples of residue classes are indeed attained by infinitely many consecu-
tive sums of two squares.

In this paper, we investigate the number of residue class patterns that are attained by
infinitely many consecutive primes. One may use Dirichlet’s theorem to show that for any
q, m ∈ N with q ≥ 2, there are at least φ(q) many m-tuples a ∈ ∏m
i=1(Z/qZ)
× such that
π(x; q, a) → ∞ as x → ∞. Using Shiu (2000) along with Dirichlet’s theorem, we may
obtain a better lower bound.

Proposition 1.3. For any q, m ∈ N with q ≥ 3, there are at least mφ(q) many m-tuples
a ∈ ∏m
i=1(Z/qZ)
× such that π(x; q, a) → ∞ as x → ∞.

Proof. For each a ∈ (Z/qZ)×, Shiu’s theorem states π(x; q, (a, . . . , a)) → ∞ as x → ∞.
By Dirichlet’s theorem, we know that each string of consecutive primes all congruent to
a (mod q) must terminate. Since φ(q) ≥ 2, by the pigeonhole principle there must exist
a′ ∈ (Z/qZ)× with a′ ̸= a such that π(x; q, (a, . . . , a, a
′)) → ∞ as x → ∞. Repeating this
‘shifting’ argument m − 1 more times, we obtain for each a ∈ (Z/qZ)
× there are m many
m-tuples attained by infinitely many consecutive primes. By considering the first entry,
the m-tuples obtained in this way for distinct a ∈ (Z/qZ)× are distinct, so in total we
can obtain at least mφ(q) such tuples. □

In fact, this lower bound is optimal if the only property of primes we use is Theorem
1.2. Let q ∈ Z>1, and let (Z/qZ)
× = {c1, . . . , cφ(q)}. Consider the sequence

bn = ck, where k − 1 < n ≤ k, 1 ≤ k ≤ φ(q),

bφ(q)+n = ck, where 2(k − 1) < n ≤ 2k, 1 ≤ k ≤ φ(q),

b3φ(q)+n = ck, where 3(k − 1) < n ≤ 3k, 1 ≤ k ≤ φ(q),

and so on, i.e.

br(r−1)φ(q)/2+n = ck, where (k − 1)r < n ≤ kr, 1 ≤ k ≤ φ(q), r ≥ 1.

For m ∈ N and a = (a1, . . . , am) ∈ ∏m
i=1(Z/qZ)
×, define the corresponding counting
function
 ̃πq(x; a) = #{bn ≤ x : bn+i−1 ≡ ai (mod q) for all i = 1, 2, . . . , m}.

We observe that for any m ∈ N, a ∈ (Z/qZ)×, and a = (a, . . . , a) ∈ ∏m
i=1(Z/qZ)
×, the
sequence (bn)
∞
n=1 satisfies ̃πq(x; a) → ∞ as x → ∞. However, there are exactly mφ(q)

4 CHEUK FUNG (JOSHUA) LAU

many m-tuples a ∈ ∏m
i=1(Z/qZ)
× such that ̃πq(x; a) → ∞ as x → ∞, namely

(ct, . . . , ct︸ ︷︷ ︸
r times , ct+1, . . . , ct+1︸ ︷︷ ︸
m−r times ) ∈
 m∏

i=1(Z/qZ)
×, 1 ≤ r ≤ m, 1 ≤ t ≤ φ(q), cφ(q)+1 := c1.

For general m ∈ N, despite knowing that mφ(q) tuples of residue classes are attained
by infinitely many consecutive primes, it is currently not known whether any other specific
tuple of residue classes is attained by infinitely many consecutive primes. To state our
main results, we make the following definitions.

Definition 1.4. For a squarefree integer q ≥ 2, m ∈ Z
+, and A ⊆ ∏m
i=1(Z/qZ)
×, define

π(x; q, A) = #{pn ≤ x : (pn mod q, . . . , pn+m−1 mod q) ∈ A}.

Also, for r ∈ Z
+ with r > 1, define

M =
 ⌈( 2
3r−2(r − 1)
2r−1

r!
 ) 1
r−1 m(m(r − 1) + r) 1
r−1
 ⌉
 ,

and define the set of functions

Jr(m, M ) = {j : {1, . . . , m} → {1, . . . , M } : j(i+1) ≥ j(i), no consecutive r values j(i) are equal}.

The main result of this paper is the following theorem, proven in Section 7.

Theorem 1.5. Let q be a squarefree integer, and r, m ∈ Z+ with r > 1. Recall π(x; q, A),
M , and Jr(m, M ) from Definition 1.4. For any a1, . . . , aM ∈ (Z/qZ)
×, let

A = {(c1, . . . , cm) : ∃j ∈ Jr(m, M ) s.t. ci = aj(i)∀1 ≤ i ≤ m}.

Then π(x; q, A) → ∞ as x → ∞.

Using this, one can argue combinatorially to obtain the following result for q in
‘medium’ range, which is proven in Section 8.

Corollary 1.6. For any 0 < c < 1, if q ≥ 2 is squarefree and φ(q) > 8c−1e
2(log m)2,
then for m sufficiently large,

#
 {

a ∈
 m∏

i=1(Z/qZ)
× : lim
x→∞ π(x; q, a) = ∞

}
 ≥ ⌊(1 − c)m⌋c5

256e10(log m)10 φ(q)(φ(q) − 1).

Choosing c = 5/6, this gives a better lower bound than that of Proposition 1.3 when

φ(q) > 3823e10(log m)10 + 1.

In Section 8, we also obtain a corresponding lower bound when q is in a ‘large’ range.

Corollary 1.7. For m, r ∈ Z
+, recall M from Definition 1.4. If q ≥ 2 is squarefree and
φ(q) ≥ M , there are at least

⌈m/(r − 1)⌉!
M (M − 1) · · · (M − ⌈m/(r − 1)⌉ + 1) · φ(q)(φ(q) − 1) · · · (φ(q) − ⌈m/(r − 1)⌉ + 1)

m-tuples a such that π(x; q, a) → ∞ as x → ∞.

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 5

For example, for m = 2, we may choose r = 2 in Corollary 1.7 to show that for any q
squarefree and φ(q) ≥ 64,

#{(a1, a2) ∈ (Z/qZ)× × (Z/qZ)× : lim
x→∞ π(x; q, (a1, a2)) = ∞} ≥ 1
2016φ(q)(φ(q) − 1).

In particular, when φ(q) > 4033, we beat the lower bound in Proposition 1.3. This misses
the conjectured lower bound of φ(q)
2 by a constant. Putting r = ⌈log m + 1⌉ in Corollary
1.7, we get

Corollary 1.8. If q ≥ 2 is squarefree and φ(q) > 8e2m log m, then for m sufficiently
large,
 #
 {

a ∈
 m∏

i=1(Z/qZ)
× : lim
x→∞ π(x; q, a) = ∞

}
 ≫ e
−O(m log2 m/ log m)φ(q)
m/⌈log m⌉.

In both corollaries, we chose r = ⌈log m + 1⌉. Heuristically this is because for m large,
we have M = Θ(r1+o(1)m1+1/r+o(1/r)). To minimise M , we choose r ≈ log m.

2. Outline

The proof of Theorem 1.5 has two main ingredients. First, in Section 5 we develop
a modification of the Maynard–Tao sieve which guarantees the existence of several clus-
ters of primes satisfying prescribed spacing conditions. Second, in Section 6 we adapt the
Erdős–Rankin construction so that these clusters consist of consecutive primes lying in
prescribed residue classes modulo q. Combining these two ingredients yields Theorem 1.5,
from which the lower bounds for the number of attainable residue class patterns follow
by a combinatorial argument in Section 8.

A finite set of integers H is said to be admissible if for every prime p,

#
 {

n (mod p) : ∏

h∈H(n + h) ≡ 0 (mod p)

}
 < p.

Fix m, r ∈ Z
+ with r > 1, and let q be squarefree. Define the parameter M as in Definition
1.4. For sufficiently large N , let W denote the usual product of small primes appearing
in the Maynard–Tao sieve. We also introduce the Maynard–Tao sieve weights

wn =
 



 ∑

d1,...,dk
di|qn+hi
 λd1,...,dk






2
 ,

where the coefficients λd1,...,dk are defined in Section 5. Our main sieve result (Proposition
5.6) states that if H = {h1, . . . , hk} ⊂ [0, N ] is an admissible k-tuple whose pairwise
differences are ε log N -smooth, then one can choose a residue class b (mod W ) satisfying
suitable local congruence conditions so that, for any partition

H = H1 ∪ · · · ∪ HM
into equal-sized subsets, there exists n ∈ [N, 2N ] for which m + 1 of the sets qn + Hi each
contain between 1 and r − 1 primes, while every intermediate block contains no primes.

6 CHEUK FUNG (JOSHUA) LAU

The proof of Proposition 5.6 follows the ideas of Banks et al. (2016) and Merikoski
(2020). Observe that it suffices to establish the positivity of the sum

S = ∑

N <n≤2N
 ( k∑

i=1 1P(qn + hi) − m(r − 1)

− (m(r − 1) + r)
 M∑

j=1
 ∑

hj1 ,...,hjr ∈Hj
j1<···<jr
 r∏

i=1 1P(qn + hji)
)

wn.(2.1)

To do this, in Lemma 5.5 we first establish estimates for the total weight, the weighted
count of primes, and the weighted r-fold correlations
∑

N <n≤2N
n≡b ( mod W )
 wn,

∑

N <n≤2N
n≡b ( mod W )
 1P(qn + hj) wn,

∑

N <n≤2N
n≡b ( mod W )
 1P(qn + hj1) · · · 1P(qn + hjr) wn.

These estimates are then combined to prove the positivity of (2.1).

To apply Proposition 5.6, Section 6 develops a modified Erdős–Rankin construction.
Given prescribed residue classes r1, ..., rk (mod q), in Lemma 6.2 we construct an admissi-
ble tuple {h1, . . . , hk} with hi ≡ ri (mod q), whose pairwise differences are ε log N -smooth,
together with the required residue class b (mod W ). This construction also ensures that
the primes detected by the sieve are consecutive, completing the proof of Theorem 1.5.

Finally, Section 8 uses Theorem 1.5 in a recursive combinatorial argument to obtain
lower bounds for the number of residue class patterns attained by infinitely many consec-
utive primes.
 3. Acknowledgements

We would like to thank Jori Merikoski for suggesting this question, and for numerous
helpful comments throughout the writing of this paper.

4. Notation

Throughout this paper, we use ⌊x⌋ to denote the largest integer not greater than x,
and ⌈x⌉ to denote the least integer not less than x. We say f ≪ g and f = O(g) when
there exists a constant C > 0 such that |f (x)| ≤ Cg(x) for x sufficiently large. If the
implied constant depends on parameter ε say, then we write f ≪ε g or f = Oε(g). We
use f = o(g) to mean limx→∞ f (x)/g(x) = 0.

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 7

Sums of the form ∑

p range over primes, and P denotes the set of primes. We use 1P(n)
to denote the indicator function of whether n ∈ P. Given integers d1, d2 we use gcd(d1, d2)
or (d1, d2) to denote the greatest common divisor of d1 and d2, and lcm(d1, d2) or [d1, d2]
to denote the least common multiple of d1 and d2. For a positive integer q > 1, denote by
P +(q) the largest prime factor of q. We use φ(q) to denote the Euler totient function of
q. Given integers k and n, logk n denotes the k-fold iterated logarithm of n in base e, for
example log1 n = log n and log2 n = log log n.

5. A Modified Maynard–Tao Sieve

In order to use the methods of Banks et al. (2016), we need the following results.

Lemma 5.1. Let T ≥ 3 and P ≥ T 1/ log2 T . Among all primitive characters χ (mod q)
with q ≤ T and P +(q) ≤ P , there exists at most one such character such that L(s, χ) has
a zero in the region

ℜ(s) > 1 − c
log P , |ℑ(s)| ≤ exp (log P/
√
log T ) ,

where c is a positive absolute constant. If this character χ (mod q) exists and is real, then
L(s, χ) has precisely one zero in the above region, which is simple and real, and satisfies

P +(q) ≫ log q ≫ log2 T.

Proof. This is (Banks et al., 2016, Lemma 4.1). □

We fix the absolute constant c in Banks et al. (2016) and define ZT = P +(q) if such
exceptional modulus q exists, and set ZT = 1 otherwise.

Theorem 5.2 (Modified Bomberi–Vinogradov). Let N > 2. Fix any C > 0, θ = 1/2−δ ∈
(0, 1/2) and ε > 0. Suppose q0 is a squarefree integer with q0 < N ε and P +(q0) < N ε/ log2 N .
If ε is sufficiently small in terms of C, δ, c in Lemma 5.1, then with ZN 2ε as above we have
∑

q<N θ
q0|q
(q,ZN 2ε )=1
 max
(q,a)=1
 ∣
∣
∣
∣ψ(N ; q, a) − ψ(N )
φ(q)
 ∣
∣
∣
∣ ≪δ,C N
φ(q0)(log N )C .

Proof. This is (Banks et al., 2016, Theorem 4.2). □

Given a squarefree integer q ≥ 2 and an admissible tuple (h1, . . . , hk), define the set

H(n) = {qn + h1, . . . , qn + hk}.

We define the sieve weights λd1,...,dk the same way as Banks et al. (2016), i.e.

λd1,...,dk =
 




( k∏

i=1 µ(di)

) J∑

j=1
 k∏

ℓ=1 Fℓ,j
 ( log dℓ
log N
 ) , if gcd(d1 · · · dk, ZN 4ε) = 1

0, otherwise

8 CHEUK FUNG (JOSHUA) LAU

for some fixed J, where Fℓ,j : [0, ∞) → R are fixed smooth compactly supported functions
that are not identically zero, with support condition

sup
 { k∑

ℓ=1 tℓ :
 k∏

ℓ=1 Fℓ,j(tℓ) ̸= 0
}
 ≤ δ

for all j = 1, 2, . . . , J and some small δ > 0. Let

F (t1, . . . , tk) :=
 J∑

j=1
 k∏

ℓ=1 F ′
ℓ,j(tℓ),

where F ′
ℓ,j denotes the derivative of Fℓ,j. We also assume Fℓ,j are chosen such that
F (t1, . . . , tk) is symmetric. Since J and Fℓ,j for 1 ≤ ℓ ≤ k and 1 ≤ j ≤ J are fixed,
we have λd1,...,dk ≪ 1 uniformly in d1, . . . , dk. We further define

wn =
 



 ∑

d1,...,dk
di|qn+hi
 λd1,...,dk






2
 ,

and for ε > 0 define
 W = ∏

p≤ε log N
p∤ZN 4ε
 p, B = φ(W )
W log N.

We remark here, for N sufficiently large in terms of q, we have q | W , so

φ(qW )
qW = φ(W )
W .

We define the following quantities for r ∈ Z
+ and k ≥ r

Ik(F ) := ∫ ∞

0 · · · ∫ ∞

0 F (t1, . . . , tk) dt1 · · · dtk,

J (r)
k (F ) := ∫ ∞

0 · · · ∫ ∞

0
 (∫ ∞

0 · · · ∫ ∞

0 F (t1, . . . , tk) dtk−r+1 · · · dtk
)2 dt1 · · · dtk−r.

Lemma 5.3. Let N be sufficiently large in terms of q. If F1, . . . , Fk, G1, . . . , Gk : [0, ∞) →
R are compactly supported functions, then

∑′

d1,...,dk
d′
1,...,d′
k
 k∏

j=1
 µ(dj)µ(d
′
j)
[dj, d
′
j] Fj
 ( log dj
log N
 ) Gj
 ( log d′
j
log N
 ) = (c + o(1))B−k,

where ∑′ denotes the additional restriction of [d1, d
′
1], . . . , [dk, d
′
k], qW ZN 4ε being pairwise
coprime, and
 c =
 k∏

j=1
 ∫ ∞

0 F ′
j(tj)G
′
j(tj) dtj.

The same result holds if [dj, d
′
j] are replaced by φ([dj, d
′
j]), i.e.

∑′

d1,...,dk
d′
1,...,d′
k
 k∏

j=1
 µ(dj)µ(d
′
j)
φ([dj, d
′
j]) Fj
 ( log dj
log N
 ) Gj
 ( log d′
j
log N
 ) = (c + o(1))B−k.

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 9

Proof. If N is sufficiently large in terms of q such that ZN 4ε > P +(q) and q | W , then
the additional restriction is the same as saying [d1, d
′
1], . . . , [dk, d
′
k], W ZN 4ε being pairwise
coprime, which is just (Banks et al., 2016, Lemma 4.5). □

We have an estimate for J (r)
k (F ) in terms of Ik(F ).

Lemma 5.4. Let 0 < ρ < 1 and r ∈ Z
+ with 2 ≤ r ≤ k. Then there is a fixed choice of J
and Fℓ,j for ℓ ∈ {1, 2, . . . , k} and j ∈ {1, 2, . . . , J} with the required properties such that

J (1)
k (F ) ≥ (1 + O((log k)
−1/2)) ( ρδ log k
k
 ) Ik(F ),

J (r)
k (F ) ≤ (1 + O((log k)
−1/2)) (ρδ log k
k
 )r Ik(F ).

Proof. The proof is similar to (Banks et al., 2016, Lemma 4.7). The result is trivial if k
is bounded, so assume k is sufficiently large. Define Fk = Fk(t1, . . . , tk) by

Fk(t1, . . . , tk) =
 



 k∏

i=1 g(kti), if
 k∑

i=1 ti ≤ 1,

0, otherwise,

g(t) =
 



 1
1 + At , if t ∈ [0, T ],

0, otherwise,
A = log k − 2 log2 k,

T = e
A − 1
A .

The first assertion follows from (Banks et al., 2016, Lemma 4.7). For the second assertion,
we will first prove that for all x ≥ 0 we have

(∫

t1+···+tr≤x g(t1) · · · g(tr) dt1 · · · dtr
)2 ≤ (log k)r ∫

t1+···+tr≤x g(t1)2 · · · g(tr)
2 dt1 · · · dtr.

(5.1)

For 0 ≤ x ≤ log k, by Cauchy–Schwarz we have

(∫

t1+···+tr≤x g(t1) · · · g(tr) dt1 · · · dtr
)2 ≤ xr

2r
 ∫

t1+···+tr≤x g(t1)2 · · · g(tr)2 dt1 · · · dtr

≤ (log k)r ∫

t1+···+tr≤x g(t1)
2 · · · g(tr)
2 dt1 · · · dtr.

10 CHEUK FUNG (JOSHUA) LAU

We now prove (5.1) for x ≥ log k. Let y = min(x, T ) and note log(1 + Ay) ≤ A. Hence

∫

t1+···+tr≤x g(t1)
2 · · · g(tr)
2 dt1 · · · dtr

≥ ∫

t1+···+tr≤y g(t1)2 · · · g(tr)
2 dt1 · · · dtr

= ∫

t1+···+tr−1≤y
t1,...,tr−1≥0
 1
(1 + At1)2 · · · 1
(1 + Atr−1)2 dt1 · · · dtr−1

× ∫

0≤tr≤y−(t1+···+tr−1)
 1
(1 + Atr)2 dtr

≥ ∫

t1+···+tr−1≤y−1
t1,...,tr−1≥0
 1
(1 + At1)2 · · · 1
(1 + Atr−1)2 dt1 · · · dtr−1

× ∫

0≤tr≤1
 1
(1 + Atr)2 dtr

= 1
A + 1
 ∫

t1+···+tr−1≤y−1
t1,...,tr−1≥0
 1
(1 + At1)2 · · · 1
(1 + Atr−1)2 dt1 · · · dtr−1.

Since y ≥ log k ≥ r for k sufficiently large, we can do this r − 1 more times, and we get

∫

t1+···+tr≤x g(t1)
2 · · · g(tr)
2 dt1 · · · dtr ≥ 1
(A + 1)r ≥ 1
(log k)r

for k sufficiently large. Since the integral of g over [0, ∞) is 1, for all x ≥ 0 we have

(∫

t1+···+tr≤x g(t1) · · · g(tr) dt1 · · · dtr
)2 ≤ (log k)r ∫

t1+···+tr≤x g(t1)2 · · · g(tr)
2 dt1 · · · dtr,

so (5.1) holds for all x ≥ 0. Therefore

J (r)
k (Fk) = ∫ · · · ∫

∑k−r
i=1 ti≤1
 (k−r∏

i=1 g(kti)2)

×
 (∫ 1−
∑k−r
i=1 ti

0 g(ktk−r+1) · · · ∫ 1−
∑k−1
i=1 ti

0 g(ktk) dtk · · · dtk−r+1
)2 dt1 · · · dtk−r

≤ ( log k
k
 )r ∫ · · · ∫

∑k−r
i=1 ti≤1
 (k−r∏

i=1 g(kti)2)

×
 (∫ 1−
∑k−r
i=1 ti

0 g(ktk−r+1)
2 · · · ∫ 1−
∑k−1
i=1 ti

0 g(ktk)
2 dtk · · · dtk−r+1
)
 dt1 · · · dtk−r

= ( log k
k
 )r Ik(Fk).

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 11

By the Stone-Weierstrass Theorem, we take F (t1, . . . , tk) to be a smooth approximation
to Fk(ρδt1, . . . , ρδtk) such that

Ik(F ) = (δρ)
k(1 + O((log k)−1/2))Ik(Fk)

J (r)
k (F ) = (δρ)
k+r(1 + O((log k)−1/2))J (r)
k (Fk)

for all r ∈ Z+, and we are done. □

Lemma 5.5. Let q ≥ 2 be squarefree and N sufficiently large in terms of q. Suppose
{h1, . . . , hk} ⊆ [0, N ] is an admissible k-tuple such that for all 1 ≤ i < j ≤ k, we have
gcd(hi, q) = 1 and
 p | hi − hj =⇒ p ≤ ε log N.

Let b ∈ Z such that for all j ∈ {1, . . . , k}, we have gcd(qb+hj, W ) = 1. Then the following
are true.

(1) We have
 ∑

N <n≤2N
n≡b (mod W )
 wn = (1 + o(1)) N
W B−kIk(F ).

(2) For each j ∈ {1, . . . , k}, we have

∑

N <n≤2N
n≡b (mod W )
 1P(qn + hj)wn = (1 + o(1)) N
W B−kJ (1)
k (F ).

(3) For r ∈ {1, 2, . . . , k} and j1, . . . , jr ∈ {1, . . . , k} strictly increasing, we have

∑

N <n≤2N
n≡b (mod W )
 1P(qn + hj1) · · · 1P(qn + hjr)wn ≤ (4
r−1(r − 1)
r−1 + O(δ)) N
W B−kJ (r)
k (F ).

Proof. Parts (1) and (2) is nearly identical to (Banks et al., 2016, Lemma 4.6), and any
differences can be found in the proof of (3), so we only prove (3). We will use the sieve
upper bound
 1P(qn + hji) ≤
 

 ∑

ei|qn+hji µ(ei)Gi
 ( log ei
log N
 )



2

for smooth decreasing functions Gi : [0, ∞) → R supported on [0, 1
4(r−1) − 2δ
r−1 ] with
G(0) = 1, for each i = 1, 2, . . . , r − 1. Observe that there is no contribution from any
summand in the definition of wn unless dj1 = · · · = djr = 1, since 1P(qn + hji) together
with the divisibility condition dji | (qn + hji) forces dji = 1 for each i = 1, . . . , r. Thus,

12 CHEUK FUNG (JOSHUA) LAU

we have

∑

N <n≤2N
n≡b (mod W )
 r∏

i=1 1P(qn + hji)
 





 ∑

d1,...,dk
di|qn+hji ∀i
 λd1···dk
 





2

≤ ∑

N <n≤2N
n≡b (mod W )
 1P(qn + hjr )
 r−1∏

i=1
 

 ∑

ei|qn+hji
 µ(ei)Gi
 ( log ei
log N
 )



2 ( ∑

d1,...,dk
di|qn+hji ∀i
dj1 =···=djr =1
 λd1···dk
 )2

= ∑

N <n≤2N
n≡b (mod W )
 1P(qn + hjr )

( ∑

d1,...,dk
e1,...,er−1
di|qn+hji ∀i
dj1 =···=djr =1
eℓ|qn+hjℓ ∀ℓ
 λd1,...,dk µ(e1) · · · µ(er−1)G1
 ( log e1
log N
 ) · · · Gr−1
 ( log er−1
log N
 ) )2.

Expanding the square,

= ∑

N <n≤2N
n≡b (mod W )
 1P(qn + hjr ) ∑

d1,...,dk
e1,...,er−1
di|qn+hji ∀i
dj1 =···=djr =1
eℓ|qn+hjℓ ∀ℓ
 ∑

d′
1,...,d′
k
e′
1,...,e′
r−1
d′
i|qn+hji ∀i
d′
j1 =···=d′
jr =1
e′
ℓ|qn+hjℓ ∀ℓ
 λd1,...,dk λd′
1,...,d′
k

×
 r−1∏

i=1 µ(ei)µ(e
′
i)Gi
 ( log ei
log N
 ) Gi
 ( log e′
i
log N
 )

= ∑

d1,...,dk
e1,...,er−1
dj1 =···=djr =1
gcd(di,q)=1∀i
gcd(eℓ,q)=1∀ℓ
 ∑

d′
1,...,d′
k
e′
1,...,e′
r−1
d′
j1 =···=d′
jr =1
gcd(d′
i,q)=1∀i
gcd(e′
ℓ,q)=1∀ℓ
 λd1,...,dk λd′
1,...,d′
k
 r−1∏

i=1 µ(ei)µ(e
′
i)Gi
 ( log ei
log N
 ) Gi
 ( log e′
i
log N
 )

× ∑

N <n≤2N
n≡b mod W
n≡−q−1hji mod [di,d′
i]∀i
n≡−q−1hjℓ mod [eℓ,e′
ℓ]∀ℓ
 1P(qn + hjr ),

since we assumed gcd(q, hji) = 1 for all 1 ≤ i ≤ r − 1. The innermost sum is

π(2qN + hjr) − π(qN + hjr)

φ(qW ) ∏k
i=1 φ([di, d
′
i]) ∏r−1
i=1 φ([ei, e
′
i]) + O
 (
E
 (

qN ; qW
 k∏

i=1[di, d
′
i]
 r−1∏

i=1[ei, e
′
i]
))
 ,

where

E(qN ; q′) = max
(a,q′)=1
h∈H
 ∣
∣
∣
∣π(2qN + h; q′, a) − π(qN + h; q′, a) − π(2qN + h) − π(qN + h)
φ(q′)
 ∣
∣
∣
∣ ,

because by the support of λd1,...,dk and the choice of b we have [di, d
′
i], [eℓ, e
′
ℓ] are all pairwise
coprime, and by assumption q | W . We first deal with the error term. In the same way as

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 13

(Banks et al., 2016, Lemma 4.6(iii)), we can restrict to arithmetic progressions mod sW ,
where
 s =
 k∏

i=1[di, d
′
i]
 r−1∏

i=1[ei, e
′
i] ≤ N 1/2−δ.

Using the bound λd1,...,dk ≪ 1 and the trivial bound E(qN ; q′) ≪ 1 + qN/φ(q′), using
Cauchy–Schwarz and Theorem 5.2, the error term contributes

∑′

d1,...,dk
d′
1,...,d′
k
dj1 =···=djr =1
d′
j1 =···=d′
jr =1
e1,...,er−1
e′
1,...,e′
r−1
 |λd1,...,dkλd′
1,...,d′
k|E
 (
qN ; qW
 k∏

i=1[di, d
′
i]
 r−1∏

i=1[ei, e
′
i]

)

≪ ∑

s≤N 1
2 −δ

gcd(s,W ZN 4ε )=1
 µ(s)
2τ6k(s)E (qN ; sqW )

≪
 ( ∑

s≤N 1
2 −δ

gcd(s,W ZN 4ε )=1
 µ(s)
2τ6k(s)2 (
1 + qN
φ(sqW )
) )1/2( ∑

s≤N 1
2 −δ

gcd(s,W ZN 4ε )=1
 µ(s)2E (qN ; sqW )
 )1/2

≪ N
W (log N )2k ,

where ∑′ denotes the additional pairwise coprimality condition between [di, d
′
i], [eℓ, e
′
ℓ], qW ZN 2ε
and τ6k(s) denotes the number of ordered 6k-tuples of positive integers whose product is
s. The main term is treated the same as (Banks et al., 2016, Lemma 4.6(ii)). Expanding
λd1,...,dk, the main term is

(1 + o(1)) qN
log N
 J∑

j=1
 ∑′

d1,...,dk
d′
1,...,d′
k
dj1 =···=djr =1
d′
j1 =···=d′
jr =1
 k∏

j=1 µ(dj) ∏

1≤ℓ≤k
ℓ̸=j1,...,jr−1
 Fℓ,j
 ( log dℓ
log N
 ) r−1∏

i=1 Fji,j(0) Gi
 ( log di
log N
 )

k∏

j=1 µ(d
′
j) ∏

1≤ℓ≤k
ℓ̸=j1,...,jr−1
 Fℓ,j
 ( log d′
ℓ
log N
 ) r−1∏

i=1 Fji,j(0) Gi
 ( log d′
i
log N
 )

× φ(qW )−1φ([d1, d
′
1])
−1 · · · φ([dk, d
′
k])
−1,

where ∑′ denotes the additional restriction of [d1, d
′
1], . . . , [dk, d
′
k], qW ZN 4ε being pairwise
coprime. Let

̃F (t1, . . . , tk) =G
′
1(tj1) · · · G
′
r−1(tjr−1)

× ∫ ∞

0 · · · ∫ ∞

0 F (t1, . . . , tj1−1, uj1, . . . , ujr−1, tjr+1, . . . , tk) duj1 · · · dujr−1.

14 CHEUK FUNG (JOSHUA) LAU

Note ̃F is supported on t1, . . . , tk with ∑k
i=1 ti ≤ 1/4 − δ. Using Lemma 5.3, the main
term is

(1 + o(1)) qN
φ(qW ) log N B−k+1 J∑

j=1
 ∏

1≤ℓ≤k
ℓ̸=j1,...,jr
 ∫ ∞

0 F ′
ℓ,j(tℓ)2 dtℓ
 r∏

i=1 Fji,j(0)
2 r−1∏

i=1
 ∫ ∞

0 G
′
i(ti)
2 dti

≤ (1 + o(1)) N
W B−k ∫ ∞

0 · · · ∫ ∞

0
 (∫ ∞

0 ̃F (t1, . . . , tk) dtjr
)2 dt1 · · · dtjr−1 dtjr+1 · · · dtk.

Combined with the above error term bound we have

∑

N <n≤2N
n≡b (mod W )
 r∏

i=1 1P(qn + hji)

( ∑

d1,...,dk
di|qn+hji ∀i
dj1 =···=djr =1
 λd1,...,dk
)2

≤ (1 + o(1)) N
W B−k ∫ ∞

0 · · · ∫ ∞

0
 (∫ ∞

0 ̃F (t1, . . . , tk) dtjr
)2 dt1 · · · dtjr−1 dtjr+1 · · · dtk

= (1 + o(1)) N
W B−kJ (r)
k (F ) ∫ ∞

0 · · · ∫ ∞

0
 r−1∏

i=1 G
′
i(tji)
2 dtj1 · · · dtjr−1.

Taking Gi(t) to be a fixed smooth approximation to 1 − t/( 1
4(r−1) − 2δ
r−1 ) with G(0) = 1
and ∫ ∞
0 G
′
i(t)
2 dt ≤ 4(r − 1) + O(δ), we are done. □

It will be helpful to make the following definitions.

Definition 1.4. For a squarefree integer q ≥ 2, m ∈ Z
+, and A ⊆ ∏m
i=1(Z/qZ)
×, define

π(x; q, A) = #{pn ≤ x : (pn mod q, . . . , pn+m−1 mod q) ∈ A}.

Also, for r ∈ Z
+ with r > 1, define

M =
 ⌈( 2
3r−2(r − 1)
2r−1

r!
 ) 1
r−1 m(m(r − 1) + r) 1
r−1
 ⌉
 ,

and define the set of functions

Jr(m, M ) = {j : {1, . . . , m} → {1, . . . , M } : j(i+1) ≥ j(i), no consecutive r values j(i) are equal}.

Proposition 5.6. Let m, r ∈ Z
+ with r > 1, q ≥ 2 be a squarefree integer and recall M
from Definition 1.4. Let k be a sufficiently large multiple of M in terms of m and r. Let
ε > 0 be sufficiently small. Define
 W := ∏

p≤ε log N
p∤ZN 4ε
 p.

Let H = {h1, . . . , hk} ⊆ [0, N ] be an admissible k-tuple such that for all 1 ≤ i < j ≤ k,
gcd(hi, q) = 1 and p | hi − hj =⇒ p ≤ ε log N.
Let b ∈ Z such that ( k∏

j=1(qb + hj), W
 )
 = 1.

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 15

Let H = H1 ∪ · · · ∪ HM be a partition of H into M sets of equal size. Then for all
sufficiently large N in terms of m, q, k, ε, there is n ∈ [N, 2N ] with n ≡ b (mod W ) and
some set of distinct indices {i1, . . . , im+1} such that

1 ≤ |Hi(n) ∩ P| ≤ r − 1 for all i ∈ {i1, . . . , im+1},

|Hi(n) ∩ P| = 0 for all i1 < i < im+1 such that i ̸= i1, . . . , im+1.

Proof. The proof is similar to that of (Banks et al., 2016, Theorem 4.3). Consider

S = ∑

N <n≤2N
 ( k∑

i=1 1P(qn + hi) − m(r − 1) − (m(r − 1) + r)
 M∑

j=1
 ∑

hj1 ,...,hjr ∈Hj
j1<···<jr
 r∏

i=1 1P(qn + hji)

)
wn.

By Lemma 5.5, we have

S ≥
 k∑

i=1 (1 + o(1)) N
W B−kJ (1)
k (F ) − m(r − 1)(1 + o(1)) N
W B−kIk(F )

− (m(r − 1) + r) ∑

hj1 ,...,hjr ∈Hj
j1<···<jr
 (4
r−1(r − 1)r−1 + o(δ)) N
W B−kJ (r)
k (F ).

Using Lemma 5.4 and choosing 0 < ρ < 1 such that ρδ log k = 2(r − 1)m, we get

S ≥ N
W B−kIk(F )

(

k · 2(r − 1)m
k − m(r − 1)

− 4r−1(r − 1)
r−1(m(r − 1) + r)M (
k/M
r
 ) (2(r − 1)m
k
 )r − O(δ)

)

> N
W B−kIk(F ) (
m(r − 1) − 4
r−1(r − 1)
r−1(m(r − 1) + r) · 2
r(r − 1)
rm
r

r!M r−1
 ) ,

so S > 0 since
 M =
 ⌈( 2
3r−2(r − 1)
2r−1

r!
 ) 1
r−1 m(m(r − 1) + r) 1
r−1
 ⌉
 .

Therefore, there must exist n ∈ (N, 2N ] making a positive contribution to S. Observe
that

(1) every Hi with |Hi(n) ∩ P| ≥ r contributes at most r − m(r − 1) − r = −m(r − 1)
to S,
(2) every Hi with |Hi(n) ∩ P| ∈ [1, r − 1] contributes at most r − 1.

For each n ∈ (N, 2N ], define

sn = number of indices i for which |Hi(n) ∩ P| ≥ r,

tn = number of indices i for which |Hi(n) ∩ P| ∈ [1, r − 1].

For those n making a positive contribution to S, we must have

−m(r − 1)sn − m(r − 1) + tn(r − 1) > 0,

which implies tn ≥ m+1+msn, i.e. number of indices j for which |Hj(n)∩P| ∈ [1, r −1] is
at least m+1+msn. In particular, there must be some set of m+1 indices i1 < · · · < im+1

16 CHEUK FUNG (JOSHUA) LAU

for which |Hi(n) ∩ P| ∈ [1, r − 1] for i = i1, . . . , im+1 and |Hi(n) ∩ P| = 0 for i1 < i < im+1
and i ̸= i1, . . . , im+1. □

6. A Modified Erdős–Rankin Type Construction

We have the following elementary lemma.

Lemma 6.1. Let {h1, . . . , hk} be an admissible k-tuple, let S ⊆ Z, and P be a set of
primes such that for some x ≥ 2, we have
{
{h1, . . . , hk} ⊆ S ⊆ [0, x
2],

|{p ∈ P : p > x}| > |S| + k.

Then, there is a set of integers {ap : p ∈ P} such that

{h1, . . . , hk} = S \ ⋃

p∈P{g : g ≡ ap (mod p)}.

Proof. This is (Banks et al., 2016, Lemma 5.1). □

As in Banks et al. (2016), we need Mertens’ 3rd Theorem: for x ≥ 2,
∏

p≤x
 (
1 − 1
p
) = e
−γ

log x
 (1 + O ( 1
log x
 )) ,(6.1)

where γ = 0.5772 . . . is the Euler-Mascheroni constant. Also, from (Davenport, 2013,
Chapter 20 (13)), for any positive constant c, there is a positive constant c′ depending
only on c such that ∑

x<p≤x+y
p≡a (mod q)
 log p = y
φ(q) + O (x exp (−c′√
log x))
(6.2)

uniformly for 2 ≤ y ≤ x, q ≤ exp(c
√log x) and gcd(q, a) = 1, except possibly when q is a
multiple of some q1 depending on x which satisfies P +(q1) ≫c log2 x.

Lemma 6.2. Fix k ∈ N, squarefree integer q ≥ 2 and integers 0 < r1 ≤ · · · ≤ rk all
coprime to q. There is a number y′ = y′(q, r, k) depending only on q, r1, . . . , rk and k such
that the following holds. Let x, y, z ∈ R satisfy x ≥ 1, y ≥ y′ and

2y(1 + (1 + rk)x) ≤ 2q
φ(q)z ≤ y(log2 y)(log3 y)
−1.

Let Z be any (possibly empty) set of primes such that for all p′ ∈ Z,
∑

p∈Z
p≥p′
 1
p ≪ 1
p′ ≪ 1
log z .(6.3)

There is a set {̃ap : p ≤ y, p /∈ Z} and an admissible k-tuple {h1, . . . , hk} ⊆ (y, z] such
that
 {h1, . . . , hk} = ((0, z] ∩ Z) \ ⋃

p≤y
p /∈Z
{g : g ≡ ̃ap (mod p)}

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 17

and p | ̃ap whenever p | q. Moreover, for 1 ≤ i < j ≤ k,

p | hi − hj =⇒ p ≤ y,

and for 1 ≤ i ≤ k, hi ≡ ri (mod q).

Proof. The proof is very similar to the proof of (Banks et al., 2016, Lemma 5.2). Let
y1, y2, y, z be numbers satisfying

2 < y1 < y2 < y < z < y1y2, 2 log y1 ≤ (log z)(log2 z)−1.

Let Z be any set consisting of primes satisfying (6.3). As in Banks et al. (2016), we have
the following estimates on Z:
∏

p∈Z
 (1 − 1
p
 )−1 = 1 + O ( 1
log z
 ) ,(6.4)
 ∑

p∈Z
p≤y0
 1 ≪ log y0 for all y0 ≥ 1.(6.5)

For y (and hence log z) sufficiently large, from (6.3) we may assume 2 /∈ Z. Suppose
further that y1 > P +(q). Let

P1 = ∏

2<p≤y1
p /∈Z,p̸=ℓ
 p, P2 = ∏

y1<p≤y2
p /∈Z
 p, P3 = ∏

y2<p≤y
p /∈Z
 p,

where ℓ is a prime satisfying ℓ ≫ log y1 chosen later. For p | P2, we choose ̃ap = 0, and let

N1 = ((0, z] ∩ Z) \ ⋃

p|P2{g : g ≡ ̃ap (mod p)} = {h ∈ (0, z] : gcd(h, P2) = 1}.

From the proof of (Banks et al., 2016, Lemma 5.2), we get

|N1| ≤ z
log y2 (log(z/y2) + O(1)).

For p | P1 and p ∤ q, we choose ̃ap greedily as in Banks et al. (2016), which is, for any
finite set S ⊆ Z, |S| = ∑

a (mod p)
 ∑

g∈S
g≡a (mod p)
 1,

so there is an integer ̃ap such that

|{g ∈ S : g ≡ ̃ap (mod p)}| ≥ |S|
p ,

For p | q, set ̃ap = 0. Repeating this process with p varied over all prime divisors of P1,
we obtain the set

N2 = N1 \ ⋃

p|P1{g : g ≡ ̃ap (mod p)}

= N1 \
 [ ⋃

p|P1
p∤q
 {g : g ≡ ̃ap (mod p)} ⋃

p|P1
p|q
 {g : g ≡ 0 (mod p)}
]

18 CHEUK FUNG (JOSHUA) LAU

whose cardinality satisfies the bound

|N2| ≤ |N1| ∏

p|P1
p∤q
 (1 − 1
p
) ≤ 2e
−γ qz(log(z/y2) + O(1))
φ(q)(log y1)(log y2)

by Mertens’ theorem (6.1) and (6.4). By the prime number theorem,

π(y) − π(y2) = y
log y + O ( y
(log y)2 + y2
log y2
 )

≥ y
log y2 − O ( y2
log y2
 )

if y2 ≥ y log(y/y2)/ log y, which is implied by y2 ≥ y log2 y/ log y. By (6.5), we have

|{p ∈ (y2, y] : p /∈ Z}| − |N2| ≥ y
log y2
 (
1 − 2e−γ qz log(z/y2)
φ(q)y log y1
 )

− O ( y2
log y2 + z
(log y1)(log y2)
) .

We now assume

y1 = (log y)
1/4, y2 = y(log3 y)
−1, y < 2qz
φ(q) ≤ y(log2 y)(log3 y)
−1.

Substituting, we have

|{p ∈ (y2, y] : p /∈ Z}| − |N2| ≥ y
log y (1 − e−γ) − O ( y
(log y)(log3 y)
) ,

which tends to infinity as y → ∞, so

|{p ∈ (y2, y] : p /∈ Z}| > |N2| + k

for y sufficiently large in terms of k, which we assume. Applying Lemma 6.1, if {h1, . . . , hk}
is any admissible k-tuple contained in N2, then there exist integers {̃ap : p | 2ℓP3} such
that {h1, . . . , hk} = N2 \ ⋃

p|2ℓP3{g : g ≡ ̃ap (mod p)}.

Note {p ≤ y : p /∈ Z} = {p ≤ y : p | 2ℓP1P2P3}, so we are done if we can show there
exists an admissible k-tuple {h1, . . . , hk} ⊆ N2 satisfying the required conditions. To do
this, we first define an arithmetic progression mod [q, P1]. For each prime p | [q, P1], let
Ai (mod p) be defined by

Ai =
 




−1, if ̃ap ≡ 1 (mod p), p ∤ q, p | P1,
1, if ̃ap ≡ −1 (mod p), p ∤ q, p | P1,
ri, if p | q,

Since these congruence conditions are prescribed modulo the distinct prime divisors of
[q, P1], the Chinese Remainder Theorem yields a unique residue class Ai (mod [q, P1])
satisfying all of them simultaneously. Suppose we could choose hi to be distinct primes in
(y, z] congruent to Ai (mod [q, P1]). Then, hi ∈ N1 implies hi ∈ N2 since gcd(Ai, P1) = 1.

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 19

By the prime number theorem, note P1 = e
(1+o(1))y1 as y tends to infinity, so for i ̸= j we
have
 p | hi − hj =⇒ p | ∏

p∤q
p|P1
 p or p | hi − hj∏ p∤q
p|P1 p =⇒ p ≤ max{y1, qz/P1} < y,

if y is sufficiently large. Also, {h1, . . . , hk} is admissible since min{h1, . . . , hk} ≥ y > k,
which we assume. Therefore, we are left to show that we can find k distinct primes in
(y, z] each congruent to Ai (mod [q, P1]).

To show this, note Chebyshev’s bound implies ∑

p≤y1 log p ≪ 2y1, so [q, P1] < e3(log y)1/4.
Therefore, by (6.2), for each 1 ≤ i ≤ k we have
∑

u≤p≤u+∆
p≡Ai (mod [q,P1])
 log p = ∆
φ([q, P1]) + O (y exp (−c
′√
log y))

uniformly for 2 ≤ ∆ ≤ y ≤ u ≤ z and c
′ an absolute constant, apart from when possibly
[q, P1] is a multiple of some q1 depending on u satisfying P +(q1) ≫c log2 u ≫ log y1.
Therefore we now pick ℓ such that this possibility doesn’t occur. Choosing ∆ = ye−(log y)1/4,
we have ∑

u≤p≤u+∆
p≡Ai (mod [q,P1])
 log p ≫ y exp (−4(log y)
1/4)

uniformly for y ≤ u ≤ z, so for each i, the left hand side is a sum of at least k primes for
every Ai if y is sufficiently large in terms of k. Now assume y sufficiently large in terms
of rk so that 2(1 + (1 + rk)) ≤ (log2 y)(log3 y)
−1,

and let x ≥ 1 be any number such that

2y(1 + (1 + rk)x) ≤ 2q
φ(q)z ≤ y(log2 y)(log3 y)
−1.

Let u = rkxy + y,

so that the interval (u, u + ∆] is contained in (y, z]. For 1 ≤ i ≤ k, we choose hi to be
distinct primes in (u, u + ∆] such that hi ≡ Ai (mod [q, P1]), and this is possible since
each arithmetic progression Ai (mod [q, P1]) contains at least k primes in the interval.
Therefore, we are done. □

7. Proofs of Main Result

In this section we combine the results of Sections 5 and 6 to prove Theorem 1.5.

Theorem 1.5. Let q ≥ 2 be a squarefree integer, and r, m ∈ Z+ with r > 1. Recall
π(x; q, A), M , and Jr(m, M ) from Definition 1.4. For any a1, . . . , aM ∈ (Z/qZ)
×, let

A = {(c1, . . . , cm) : ∃j ∈ Jr(m, M ) s.t. ci = aj(i)∀1 ≤ i ≤ m}.

Then π(x; q, A) → ∞ as x → ∞.

20 CHEUK FUNG (JOSHUA) LAU

Proof. The case m = 1 is known. Fix k ≥ m ≥ 2, let ε > 0 be sufficiently small, and let
k be a sufficiently large multiple of M . Let r = (r1, . . . , rk) ∈ Rk be given by

r = (a1 mod q, . . . , a1 mod q, a2 mod q, . . . , a2 mod q, . . . , aM mod q, . . . , aM mod q),

where there are k/M consecutive copies of each ai (mod q) appearing in r. We choose
suitable representatives ri mod q such that r1 ≤ · · · ≤ rk. Let N be sufficiently large in
terms of k, m, ε, and define parameters

x = ε−1, y = ε log N, z = φ(q)y(log2(y))(2q log3(y))
−1.

If N is sufficiently large in terms of r and k as well, then with y′(q, r, k) as in Lemma 6.2,
we have

x > 1, y ≥ y′(q, r, k), 2y(1 + (1 + rk)x) ≤ 2q
φ(q)z ≤ y(log2 y)(log3 y)
−1.

Let ZN 4ε be defined as in Section 5, W = ∏
p≤ε log N,p∤ZN 4ε p, and let

Z =
 {
∅, if ZN 4ε = 1
{ZN 4ε}, if ZN 4ε ̸= 1.

By Lemma 6.2, there is a set {ap : p ≤ y, p /∈ Z} and an admissible k-tuple {h1, . . . , hk} ⊆
(y, z] such that
 {h1, . . . , hk} = ((0, z] ∩ Z) \ ⋃

p≤y
p /∈Z
{g : g ≡ ̃ap (mod p)},

and p | ̃ap whenever p | q. Moreover, for 1 ≤ i < j ≤ k,

p | hi − hj =⇒ p ≤ y,

and define the partition H = H1 ⊔ · · · ⊔ HM
such that for each j = 1, 2, . . . , M we have

h ≡ rjk/M (mod q)

for all h ∈ Hj. Let b ∈ Z satisfying

b ≡ −q−1̃ap (mod p)

if p ≤ y, p /∈ Z and p ∤ q, whereas if p | q set b ≡ 0 (mod p). Therefore, the assumptions
of Proposition 5.6 hold, and there is some n ∈ (N, 2N ] with n ≡ b (mod W ) and some
set of distinct indices {i1, . . . , im+1} such that

1 ≤ |Hi(n) ∩ P| ≤ r − 1 for all i ∈ {i1, . . . , im+1},

|Hi(n) ∩ P| = 0 for all i1 < i < im+1 such that i ̸= i1, . . . , im+1.

To prove they are consecutive primes, note

(qn, qn + z] ∩ P = H(n) ∩ P,

since if g ∈ (0, z] and g /∈ {h1, . . . , hk}, then qn + g ≡ qb + ̃ap ≡ −̃ap + ̃ap ≡ 0 (mod p) for
some p ≤ y with p /∈ Z, so the primes in H(n) are consecutive primes. Therefore, there
must exist consecutive primes pn, . . . , pn+m−1 ∈ [qN, 3qN ] such that pn+i−1 ≡ aj′(i) mod q
for all 1 ≤ i ≤ m, where j′(i + 1) ≥ j′(i) for all 1 ≤ i ≤ m and no consecutive r of
(j′(i))
m
i=1 are congruent mod q. Taking N → ∞, we are done. □

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 21

8. Number of Attainable Residue Class Patterns

In this section, we use Theorem 1.5 and recursive combinatorial arguments to obtain
lower bounds for the number of m-tuples occurring infinitely often among consecutive
primes.

Corollary 8.1. For m, r ∈ Z+ with 2 ≤ r ≤ m/100, recall M from Definition 1.4. For
any constant 0 < c < 1, if q is squarefree and φ(q) ≥ ⌈ M
⌊c(m−1)/(r−1)⌋ ⌉, there are at least

4⌊(1 − c)m⌋ (⌈ M
⌊c(m − 1)/(r − 1)⌋
⌉)−5 φ(q)(φ(q) − 1)

m-tuples a such that π(x; q, a) → ∞ as x → ∞.

Proof. Using Theorem 1.5, for any a1, . . . , aM , there must exist a = (aj(1), . . . , aj(m)) with
j increasing and no consecutive r values the same, such that

π(x; q, a) → ∞ as x → ∞.

We call a m-tuple a with this property ‘good’. Define a set S1 consisting of all M -tuples
with entries in (Z/qZ)
× of the form

( a1, . . . , a1︸ ︷︷ ︸
⌊c(m−1)/(r−1)⌋ times, a2, . . . , a2︸ ︷︷ ︸
⌊c(m−1)/(r−1)⌋ times, · · · ), ai distinct.

Note S1 is non-empty since φ(q) ≥ ⌈ M
⌊c(m−1)/(r−1)⌋ ⌉ by assumption. We pick good m-tuples
with the following recursive process.

(1) Take a M -tuple (a1, . . . , a1, a2, . . .) ∈ S1. By Theorem 1.5, there is a good m-tuple
of the form (b1, . . . , b1, b2, . . . , b2, . . . , bℓ1, . . . , bℓ1),

where 2 ≤ ℓ1 ≤ ⌈ M
⌊c(m−1)/(r−1)⌋ ⌉.
(2) Define

S2 := S1 \ {(a1, . . . , a1, a2, . . . , a2, . . .) :∃i, i′, j s.t. i < i′ and ai = bj, ai′ = bj+1}.

(3) Take any element from S2, then repeat the above process until Sk is empty.

The good m-tuples obtained from this process must be piecewise constant with at least
2 distinct entries, and no two good tuples have the same two consecutive distinct entries
in the same order. To find the minimum number of good tuples obtained, note

number of good tuples obtained = number of times the process repeated,

which can be minimised if at each step k a good m-tuple (b(k)
1 , . . . , b(k)
1 , . . . , b(k)
ℓk , . . . , b(k)
ℓk )
is obtained such that

Sk ∩ {(a1, . . . , a1, a2, . . . , a2, . . .) : ∃i, i′, j s.t. i < i′ and ai = b
(k)
j , ai′ = b
(k)
j+1}

is maximised. However, the size of this set is clearly at most the size of

S1 ∩ {(a1, . . . , a1, a2, . . . , a2, . . .) : ∃i, i′, j s.t. i < i′ and ai = b
(k)
j , ai′ = b
(k)
j+1}

22 CHEUK FUNG (JOSHUA) LAU

Therefore, the number of elements removed every time is

≤ #(choices of j) · #(choices of i, i
′)

#(choices of ak for k ̸= i, i
′) · #(choices of order for ai with ai before ai′)

≤ (ℓk − 1)(
⌈ M
⌊c(m−1)/(r−1)⌋ ⌉
2
 )( φ(q) − 2
⌈ M
⌊c(m−1)/(r−1)⌋ ⌉ − 2
) · ⌈ M
⌊c(m − 1)/(r − 1)⌋
⌉
! · 1
2.

To maximise the number of elements removed, we suppose for all k, ℓk = ⌈ M
⌊c(m−1)/(r−1)⌋ ⌉,
since this is the greatest possible value of ℓk. Repeating this process until it terminates,
the number of good tuples obtained in this way is

≥ 4
( φ(q)
⌈ M
⌊c(m−1)/(r−1)⌋ ⌉
)( φ(q) − 2
⌈ M
⌊c(m−1)/(r−1)⌋ ⌉ − 2
)−1 (⌈ M
⌊c(m − 1)/(r − 1)⌋
⌉)−3

≥ 4 (⌈ M
⌊c(m − 1)/(r − 1)⌋
⌉)−5 φ(q)(φ(q) − 1).

By Dirichlet’s Theorem on primes in arithmetic progressions, for each a ∈ (Z/qZ)×, there
are infinitely many primes p ≡ a (mod q). Therefore, for each good m-tuple

a = (a1, . . . , a1, . . . , aℓ, . . . , aℓ)

obtained from the above process, by the pigeonhole principle we can create another good
tuple by shifting: there exists a ∈ (Z/qZ)
× such that

a
′ := (a1, . . . , a1, . . . , aℓ, . . . , aℓ, a)

is good, and we can keep shifting the resultant good tuple to get another good tuple.

Let G0 ⊆ ∏m
i=1(Z/qZ)
× be the set of good tuples obtained from the above recursive
process, and let Gi be the set of good tuples obtained from shifting each tuple in G0 i
times. We claim that ∣
∣
∣
∣
∣
∣
⌊(1−c)m⌋⋃

i=0 Gi
∣
∣
∣
∣
∣
∣ = ⌊(1 − c)m⌋|G0|,

i.e. all good tuples obtained from shifting at most ⌊(1 − c)m⌋ times are distinct. Indeed,
observe from steps (1) and (2), G0 has the following property: If a, b ∈ G0, then there
does not exist 1 ≤ i, j ≤ m such that ai = bj and ai+1 = bj+1. Also, am appears in a at
most ⌊c(m−1)/(r −1)⌋·(r −1) ≤ c(m−1) < cm times. Therefore, if we shift a and b each
at most ⌊(1 − c)m⌋ times to obtain a
′ and b
′ respectively, we must have (a′
1, a
′
2) ̸= (b′
1, b
′
2)
and so a
′ ̸= b
′. Thus, shifting each m-tuple in G0 ⌊(1 − c)m⌋ times, we obtain a total of

4⌊(1 − c)m⌋ (⌈ M
⌊c(m − 1)/(r − 1)⌋
⌉)−5 φ(q)(φ(q) − 1)

m-tuples a such that π(x; q, a) → ∞ as x → ∞. □

To simplify the final expression, we have

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 23

Corollary 1.6. For any 0 < c < 1, if q ≥ 2 is squarefree and φ(q) > 8c−1e2(log m)2,
then for m sufficiently large,

#
 {

a ∈
 m∏

i=1(Z/qZ)
× : lim
x→∞ π(x; q, a) = ∞

}
 ≥ ⌊(1 − c)m⌋c5

256e10(log m)10 φ(q)(φ(q) − 1).

Proof. Letting r = ⌈log m+1⌉ in Theorem 1.5, we have M /(m−1) < 8e2 log m as m → ∞.
Using Corollary 8.1, for m sufficiently large there are at least

≥ 4⌊(1 − c)m⌋c5

45e10(log m)10 φ(q)(φ(q) − 1)

m-tuples a such that π(x; q, a) → ∞ as x → ∞. □

Remark. Shiu (2000) showed for all a ∈ (Z/qZ)× and a = (a, . . . , a) ∈ ∏m
i=1(Z/qZ)
×,

lim
x→∞ π(x; q, a) = ∞.

From Proposition 1.3, we have

#
 {

a ∈
 m∏

i=1(Z/qZ)
× : lim
x→∞ π(x; q, a) = ∞

}
 ≥ mφ(q).

Therefore, Corollary 1.6 provides a better bound when

φ(q) > 256e10c−5(1 − c)−1(log m)10 + 1.

To minimise this, we take c = 5/6, and we get a better bound when

φ(q) > 3823e10(log m)10 + 1.

We can get a better lower bound for the number of patterns attainable by consecutive
primes when φ(q) is larger. In this case, the ‘shifting’ argument does not generate many
more good tuples, so we do not consider it here.

Corollary 1.7. For m, r ∈ Z
+, recall M from Definition 1.4. If q ≥ 2 is squarefree and
φ(q) ≥ M , there are at least

⌈m/(r − 1)⌉!
M (M − 1) · · · (M − ⌈m/(r − 1)⌉ + 1) · φ(q)(φ(q) − 1) · · · (φ(q) − ⌈m/(r − 1)⌉ + 1)

m-tuples a such that π(x; q, a) → ∞ as x → ∞.

Proof. Using Theorem 1.5, for any a1, . . . , aM , there must exist a = (aj(1), . . . , aj(m)) with
j increasing and no consecutive r values the same, such that

π(x; q, a) → ∞ as x → ∞.

We call a m-tuple a with this property ‘good’. Define a set S1 consisting of all M -tuples
with distinct entries in (Z/qZ)×. We pick good m-tuples with the following recursive
process.

(1) Take an M -tuple (a1, . . . , aM ) ∈ S1. By Theorem 1.5, there is a good m-tuple of
the form (b1, . . . , b1, b2, . . . , b2, . . . , bℓ1, . . . , bℓ1),
where ⌈m/(r − 1)⌉ ≤ ℓ1 ≤ m.

24 CHEUK FUNG (JOSHUA) LAU

(2) Define

S2 := S1 \ {(a1, . . . , aM ) : there exists increasing injection σ : {1, . . . , ℓ1} → {1, . . . , M }

such that bi = aσ(i) for all i}.

(3) Take any element from S2, then repeat the above process until Sk is empty.

The good m-tuples obtained from this process must be piecewise constant with at least
m/(r − 1) distinct entries, and no two good tuples have the same two consecutive distinct
entries in the same order. To find the minimum number of good tuples obtained, note

number of good tuples obtained = number of times the process repeated,

which can be minimised if at each step k a good m-tuple (b
(k)
1 , . . . , b(k)
1 , . . . , b(k)
ℓk , . . . , b(k)
ℓk )
is obtained such that

Sk ∩ {(a1, . . . , aM ) : there exists increasing injection σ : {1, . . . , ℓk} → {1, . . . , M }

such that b
(k)
i = aσ(i) for all i}

is maximised. However, the size of this set is clearly at most the size of

S1 ∩ {(a1, . . . , aM ) : there exists increasing injection σ : {1, . . . , ℓk} → {1, . . . , M }

such that b
(k)
i = aσ(i) for all i}

Therefore, the number of elements removed every time is

≤ #(choices for aj ̸= bi) · #(choices of order for aσ(i) = b
(k)
i ∀i).

≤ (
φ(q) − ℓk
M − ℓk
 ) · M !
ℓk! .

To maximise the number of elements removed, we suppose for all k, ℓk = ⌈ m
r−1 ⌉, since this
is the smallest possible value of ℓk. Repeating this process until it terminates, the number
of good tuples obtained is

≥ ⌈ m
r − 1
⌉! · (φ(q)
M
 )(
φ(q) − ⌈ m
r−1⌉
M − ⌈ m
r−1 ⌉
 )−1

≥ ( M
⌈m/(r − 1)⌉
)−1φ(q)(φ(q) − 1) · · · (φ(q) − ⌈m/(r − 1)⌉ + 1).
 □

Simplifying the expression, we have

Corollary 1.8. If q ≥ 2 is squarefree and φ(q) > 8e2m log m, then for m sufficiently
large,
 #
 {

a ∈
 m∏

i=1(Z/qZ)
× : lim
x→∞ π(x; q, a) = ∞

}
 ≫ e
−O(m log2 m/ log m)φ(q)
m/⌈log m⌉.

RESIDUE CLASS PATTERNS OF CONSECUTIVE PRIMES 25

Proof. Letting r = ⌈log m+1⌉ in Theorem 1.5, we have M /(m−1) < 8e2 log m as m → ∞.
For m sufficiently large, using Stirling’s approximation we have
( M
⌈m/(r − 1)⌉
)

= M !
⌈m/(r − 1)⌉!(M − ⌈m/(r − 1)⌉)!

≪ M M e−M
√⌈m/(r − 1)⌉⌈m/(r − 1)⌉⌈m/(r−1)⌉e−⌈m/(r−1)⌉(M − ⌈m/(r − 1)⌉)M −⌈m/(r−1)⌉e⌈m/(r−1)⌉−M

≪
 ( M
⌈m/(r−1)⌉ − 1)⌈m/(r−1)⌉

√⌈m/(r − 1)⌉ (1 − ⌈m/(r−1)⌉
M )M

≪ (8e2(log m)2)m/ log m
√m/ log m e−m/ log m

≪ e
O(m log2 m/ log m).

Therefore by Corollary 1.7, we are done, since for m large it suffices to consider the leading
order contribution. □

References

[1] Banks, W. D., Freiberg, T., and Maynard, J. (2016). On limit points of the sequence of
normalized prime gaps. Proceedings of the London Mathematical Society, 113(4):515–539.
[2] Davenport, H. (2013). Multiplicative number theory, volume 74. Springer Science &
Business Media.
[3] Kimmel, N. and Kuperberg, V. (2024). Consecutive runs of sums of two squares.
Journal of Number Theory.
[4] Kimmel, N. and Kuperberg, V. (2025). Positive density for consecutive runs of sums
of two squares. Journal of the Institute of Mathematics of Jussieu, 24(5):1995–2046.
[5] Lemke Oliver, R. J. and Soundararajan, K. (2016). Unexpected biases in the dis-
tribution of consecutive primes. Proceedings of the National Academy of Sciences,
113(31):E4446–E4454.
[6] Maynard, J. (2016). Dense clusters of primes in subsets. Compositio Mathematica,
152(7):1517–1554.
[7] Merikoski, J. (2020). Limit points of normalized prime gaps. Journal of the London
Mathematical Society, 102(1):99–124.
[8] Shiu, D. K. (2000). Strings of congruent primes. Journal of the London Mathematical
Society, 61(2):359–373.

Mathematical Institute, University of Oxford, Radcliffe Observatory Quarter, Wood-
stock Road, OX2 6GG, Oxford, United Kingdom

Email address: joshua.lau@maths.ox.ac.uk
