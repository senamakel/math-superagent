<!-- source: https://arxiv.org/pdf/1611.09985 | converted from PDF -->

arXiv:1611.09985v2  [math.NT]  24 Mar 2017
GOWERS NORMS FOR THE THUE-MORSE AND
RUDIN-SHAPIRO SEQUENCES

JAKUB KONIECZNY

Abstract. We estimate Gowers uniformity norms for some classical auto-
matic sequences, such as the Thue-Morse and Rudin-Shapiro sequences. The
methods are quite robust and can be extended to a broader class of sequences.
As an application, we asymptotically count arithmetic progressions of a
given length in the set of integers ≤ N where the Thue-Morse (resp. Rudin-
Shapiro) sequence takes the value +1.

1. Introduction

The Thue-Morse sequence is among the simplest automatic sequences. It can be
described by the recursive relations:

t(0) = 1, t(2n) = t(n), t(2n + 1) = −t(n),

or by the explicit formula t(n) = (−1)
s2(n), where s2(n) denotes the sum of digits
of n base 2. Arguably, the Thue-Morse sequence is very structured — in particular,
its subword complexity (i.e. number of distinct subsequences of a given lenght) has
linear rate of growth (this is a general feature of automatic sequences). On the
other hand, there are also ways in which it can be construed as pseudorandom.
Mauduit and Sark¨ozy [MS98] studied several measures of pseudorandomness for
the Thue-Morse sequence, and showed that t(n) is highly uniform according to
some but not all of those measures. In particular, it is shown that for any positive
integers a, b, M, N with a(M − 1) + b < N , we have

(1)
 M−1∑

n=0 t(an + b) = O(N log 3/ log 4),

where the implied constant is absolute. In fact, this easily follows from the bound
obtained by Gelfond [Gel68]:

(2) sup
α∈R
 ∣
∣
∣
∣
∣
N −1∑

n=0 t(n)e(αn)

∣
∣
∣
∣
∣ = O(N log 3/ log 4),

where as usual e(x) := e2πix. However, for all suﬃciently large integers N , there
exist positive integers M and h with M + h ≤ N such that

(3)
 ∣
∣
∣
∣
∣

M−1∑

n=0 t(n)t(n + h)

∣
∣
∣
∣
∣ ≥ cN,

2010 Mathematics Subject Classiﬁcation. 11B85, 11B30.

1

2 J. KONIECZNY

where c > 0 is an absolute constant. (We may take c = 1/12 and h = 1.) Thus,
the Thue-Morse sequence does not correlate with arithmetic progressions but can
have some large self-correlations.
In a diﬀerent direction, t(n) is believed to look highly random when restricted to
certain subsequences. Several conjectures to this eﬀect, in a slightly more general
situation, are known as the Gelfond Problems [Gel68].
Let P denote the set of prime numbers and π(N ) = |P ∩ [N ]|. Gelfond conjec-
tured that it should hold that

(4) |{p ∈ [N ] ∩ P | t(p) = +1}| = 1
2 π(N ) + O(N 1−c),

where c > 0 is an absolute constant. This was proved only recently by Mauduit
and Rivat [MR10].
Let p(x) ∈ Q[x] be a polynomial with p(Z) ⊂ Z, and extend t(n) to Z by putting
t(−n) = t(n). Another of Gelfond’s conjectures asserts that we should have

(5) |{n ∈ [N ] | t(p(n)) = +1}| = 1
2 N + O(N 1−c),

for an absolute constant c > 0. This is only known for polynomials of degree 2 by
work of Mauduit and Rivat [MR09]. In fact, for p(n) = n2, a much stronger result
is shown in [DMR13], implying in particular that t(n2) is normal (i.e. that each
block of ±1’s of length l appears in t(n2) with frequency 1/2l). Namely, for each l
and each ǫ0, . . . , ǫl−1 ∈ {−1, +1} we have

(6) ∣
∣{
n ∈ [N ] ∣
∣ t((n + i)
2) = ǫi for 0 ≤ i < l}∣
∣ = 1
2l N + O(N 1−c),

where the constant c depends only on l.
Finally, let α ∈ R>0 \ Z. It is conjectured (see e.g. [Drm14]) that the sequence
t(⌊nα⌋) should be normal for any such α. This is conﬁrmed in the quantitative
sense by M¨ullner and Spiegelhofer [MS15], who showed that for any 1 < α < 3/2,
for any l and εi ∈ {−1, +1} for 0 ≤ i < l it holds that

(7) |{n ∈ [N ] | t(⌊(n + i)
α⌋) = ǫi for 0 ≤ i < l}| = 1
2l N + O(N 1−c),

where the constant c depends on l and α.
In general, it is believed that t(n) restricted to any of the aforementioned se-
quences should be a normal sequence (we refer e.g. to [Drm14], which is also an
excellent reference for related results).
Here, we consider a diﬀerent notion of pseudorandomness related to Gowers
uniformity norms. First introduced by Gowers in his work on an new proof of
Szemeredi’s theorem [Gow01], these norms now play a crucial role in additive com-
binatorics. For exposition of the relevant theory, we refer to [Gre] and [Tao12].

Deﬁnition 1.1. Fix s ∈ N. For N ∈ N and f : [N ] → R, the s-th Gowers uniformity
norm of f is deﬁned by

(8) ∥f ∥
2
s

U s[N ] := E
n,h
 ∏

ω∈{0,1}s f (n + ω · h)

where ω · h = ∑s
i=1 ωihi, and the expectation is taken over all n ∈ Z, h ∈ Z
s for
which the cube {n + ω · h | ω ∈ {0, 1}s} is contained in [N ].

GOWERS NORMS FOR THE THUE-MORSE AND RUDIN-SHAPIRO SEQUENCES 3

A sequence is (informally) said to be Gowers uniform of order s if its U s[N ]-norm
is small. We show that t(n) indeed is highly Gowers uniform, which makes it one
of the simplest sequences known to be Gowers uniform of all orders.

Theorem A. Let t : N0 → {±1} denote the Thue-Morse sequence. For any s ∈ N,
there exists c = c(s) > 0 such that ∥t∥U s[N ] = O(N −c) as N → ∞.

A key reason for interest in the Gowers uniformity norms is their usefulness in
counting linear patterns. In particular, as an immediate corrolary of Theorem A
we conclude via the Generalised von Neumann Theorem that the number of k-term
arithmetic progressions in {n ∈ [N ] | t(n) = +1} is N 2/2k + O(N 2−c).
We also remark that sequences with small Gowers norms do not correlate with
polynomials phases: if p ∈ R[x] with deg p = s − 1 then En<N f (n)e(p(n)) ≪
∥f ∥U s[N ] . Hence, Theorem A implies that t(n) is a fully oscillating sequence in
the terminology of [Fan]. As an application, for any dynamical system with quasi-
discrete spectrum (X, T ) and any f1, . . . , fl ∈ C(X), q1, . . . , ql ∈ Q[x] with qi(N0) ⊂
N0 for 1 ≤ i ≤ l, we have

(9) lim
N →∞ E
n<N t(n)
 l∏

i=1 fi(T qi(n)x) = 0

for any point x ∈ X.
A subtly diﬀerent type of uniformity norms ∥·∥U(s) on l∞(Z) is introduced and
studied in [HK09]. In fact, it follows from results obtained there that ∥t∥U(s) = 0 for
all s ∈ N (cf. Proposition 2.21), and Theorem A can be construed as an analogue
of this result. As an example application (cf. remarks after Theorem 2.25), this
implies that for any measure preserving system (X, T, µ), any f1, . . . , fl ∈ L∞(X)
we have

(10) E
n<N t(n)
 l∏

i=1 fi(T inx) → 0 in L2(µ) as N → ∞.

A slightly more complicated sequence we deal with carries the name of Rudi-
Shapiro. It is recursively given by

r(0) = 0, r(2n) = r(n), r(4n + 1) = r(n), r(4n + 3) = −r(2n + 1),

or explicitly by r(n) = (−1)
f11(n), where f11(n) denotes the number of times the
pattern 11 appears in the binary expansion of n.
Much like in the case of the Thue-Morse sequence, various pseudorandomness
properties of the Rudin-Shapiro sequence have long been studied. In [MS98] it
is shown that r(n) does not correlate with arithmetic progressions, but has large
self-correlations. More precisely, we have

(11)
 M−1∑

n=0 t(an + b) = O(N 1/2),

for any a, b, M with a(M − 1) + b < N , while there exist M, h with M + h ≤ N
such that

(12)
 ∣
∣
∣
∣
∣

M−1∑

n=0 t(n)t(n + h)

∣
∣
∣
∣
∣ ≥ cN,

4 J. KONIECZNY

where one can take c = 1/6 if N is suﬃciently large.
There are also exist results asserting pseudorandomness of the restrictions of
r(n) to certain subsequences. In the case of the primes, in analogy with (4), we
have

(13) |{p ∈ [N ] ∩ P | t(p) = +1}| = 1
2 π(N ) + O(N 1−c),

where c > 0 is an absolute constant [MR15]. Likewise, in analogy to (7), it follows
as a special case from results in [DDM12] that

(14) |{n ∈ [N ] | r(⌊nα⌋) = +1}| = 1
2 N + o(N ).

for any 1 < α < 7/5. (It is not known if r(⌊nα⌋) is normal.)
We show that r(n) is highly Gowers uniform. As an application we conclude that
the number of k-term arithmetic progressions in {n ∈ [N ] | r(n) = +1} is N 2/2k +
O(N 2−c).

Theorem B. Let r : N0 → {±1} denote the Rudin-Shapiro sequence. For any
s ∈ N, there exists c = c(s) > 0 such that ∥r∥U s[N ] = O(N −c) as N → ∞.

While we focus our attention on these two speciﬁc sequences, many of the ob-
servations apply to more general automatic sequences. A sequence a : N0 → C is
k-automatic if a(n) can be computed by a ﬁnite automaton taking k-ary expansion
of n on input. For comprehensive background, we refer to [AS03].

Notation. We write N = {1, 2, . . . } and N0 = N∪{0}. We use standard asymptotic
notation. For any expressions X, Y , we write X = O(Y ) or X ≪ Y if there exists
a constant c > 0 such that X < cY . We consistently use boldface letter x to denote
vector with coordinates (xi); and also write |x| := ∑i |xi|. By [N ] we denote the
interval {0, 1, . . . , N − 1}.

Acknowledgements. The author is grateful to Tanja Eisner for her hospitality
during his stay in Leipzig when the work on this project began; to Jakub Byszewski
for many long and productive discussions; to Christian Mauduit, Clemens M¨ullner,
and Aihua Fan for helpful comments; and to Ben Green for his encouragement and
valuable advice.
 2. Thue-Morse sequence

The purpose of this section is to prove Theorem A, asserting that the uniformity
norms of the Thue-Morse sequence t(n) = (−1)
s2(n) are small. Throughout this
section, let s ∈ N≥2 be ﬁxed. (We may assume that s ≥ 2 since ∥t∥U 2[N ] ≫
∥t∥U 1[N ].) It will be convenient to study somewhat more general averages

(15) A(L, r) := E
n,h
 ∏

ω∈{0,1}s t(n + ω · h + rω),

where n, h parametrize the cubes {n + ω · h | ω ∈ {0, 1}s} ⊂ [2L], L ∈ N0 and
r = (rω)ω∈{0,1}s with rω ∈ Z. Note that if r = 0, then (15) deﬁnes ∥r∥2
s

U s[2L].

Lemma 2.1. The averages A(L, r) satisfy the recursive relation

(16) A(L, r) = (−1)
|r| E
e A(L − 1, δ(r; e)) + O(2−L),

GOWERS NORMS FOR THE THUE-MORSE AND RUDIN-SHAPIRO SEQUENCES 5

where the average is taken over e = (ei)
s
i=0 ∈ {0, 1}s+1 and δ(r; e) is given by

(17) δ(r; e)ω = ⌊ rω + (1, ω) · e
2
 ⌋ = ⌊ rω + e0 + ∑s
i=1 ωiei
2
 ⌋ .

Proof. For any cube Q = {n + ω · h | ω ∈ {0, 1}s}, there exists a choice of a unique
cube Q′ = {n′ + ω · h′ | ω ∈ {0, 1}s} and a vector e ∈ {0, 1}s such that Q =
{2(n′ + ω · h′) + (1, ω) · e | ω ∈ {0, 1}s}; we simply take n = 2n′ + e0 and hi =
2hi + ei. Moreover, if Q ⊂ [2L] is chosen uniformly at random, then Q′ ⊂ [2L−1]
with probability 1 − O(2−L), and conversely if Q′ ⊂ [2L−1] and e ∈ {0, 1}s are
chosen uniformly at random then Q ⊂ [2L] with probability 1 − O(2−L). It follows
that
 A(L, r) = E
e E
n′,h′
 ∏

ω∈{0,1}s t(2n′ + 2ω · h′ + (1, ω) · e + rω) + O(2−L)

= E
e E
n′,h′
 ∏

ω∈{0,1}s(−1)
(1,ω)·e+rω t(n′ + ω · h′ + δ(r; e)ω) + O(2−L)

= E
e (−1)
S(e)A(L − 1, δ(r; e)) + O(2−L),

where δ(r; e) is deﬁned by (17) and S(e) = ∑ω rω +2se0 +2s−1 ∑s
i=1 ei ≡ |r| mod 2
(expectation is over e ∈ {0, 1}s and {n′ + ω · h′ | ω ∈ {0, 1}s} ⊂ [2L−1]). □

Lemma 2.1 motivates us to introduce a random walk WTM on a directed graph
G = (V, E) deﬁned as follows. The set of vertives is V = V+ ∪ V− where V± ={
(r, ±1) ∣
∣ r ∈ Z
{0,1}
s}. The transition probabilities are given by

(18) P ((r, ±1); (r
′, ±(−1)
|r|) = Pe (δ(r; e) = r
′) ,

where e = (ei)
s
i=0 is uniformly distributed in {0, 1}
s+1 and δ(r; e) is given by (17).
(By convention, the two occurrences of the symbol ± both denote the same sign.)
The remaining transition probabilities (i.e. those where the signs do not agree) are
declared to be identically 0.
The set E of (directed) edges of G consists of the pairs (v, v′) ∈ V 2 with
P (v, v′) > 0; hence the edge (r, ±1) → (r
′, ±(−1)
|r|) is present if and only if there
exists e ∈ {0, 1}s+1 such that δ(r; e) = r
′ (with δ(r; e) given by (17)). We will be
particularly interested in the graph G0 supported on the vertices V0 reachable from
the initial vertex v0 = (0, +1).
We note that WTM comes with a natural symmetry R : V → V given by
(r, ±1) ↦→ (r, ∓1). We have R(R(v)) = v and P (R(v), R(v′)) = P (v, v′) for all
v, v′ ∈ V . In particular, R preserves the edges of G.
Denote further by P (l)(v, v′) the probability of reaching vertex v′ after l steps,
starting from v. Iterating Lemma 2.1 we obtain the following formula.

Corollary 2.2. The averages A(L, r) satisfy for any l < L the recursive relation

A(L, r) = ∑

r′,σ P (l)(
(r, +1), (r
′, σ)
)
σA(L − l, r
′) + O(2−(L−l)),(19)

6 J. KONIECZNY

where the sum runs over all pairs (r
′, σ) ∈ V which are reachable from (r, +1). In
particular,

∥t∥
2
s

U s[N ] = ∑

r′
 (P (l) (v0, (r
′, +1)) − P (l) (v0, (r
′, −1))
) A(L − l, r
′) + O(2−(L−l)),

(20)

where the sum runs over all r
′ such that at least one of (r
′, ±1) belongs to V0.

Proof. Apply Lemma 2.1 l times. Note that the recurrence relation (16) can be
equivalently written as

A(L, r) = ∑

r′,σ P (
(r, +1), (r
′, σ)
)σA(L − 1, r
′) + O(2−L),

which is the same as (19) for l = 1. For general l ∈ N, the main term follows directly
from how P (l)(v, v′) are deﬁned. The total error term is ≪ 2−L + 2(−L−1) + · · · +
2−(L−l) ≪ 2−(L−l). □

Recall that a directed graph is strongly connected if there exists a directed path
from any vertex to any other vertex. A graph is aperiodic if the greatest common
divisor of all cycles present in the graph equals 1.

Proposition 2.3. Let G0 be the graph constructed above. Then G0 is ﬁnite,
strongly connected, aperiodic, and preserved by R.

Proof. Aperiodicity follows immediately from the observation that G0 contains a
loop at (0, +1) since δ((0, +1); 0) = (0, +1).
If G contains an edge from v = (r, ±1) to v′ = (r
′, ±1) then r′
ω = δ(r; e) =⌊ rω +(1,ω)·e
2 ⌋ for some e ∈ {0, 1}s+1, and in particular 0 ≤ (1, ω) · e ≤ |ω| + 1. An

elementary inductive argument now shows that if (r, ±1) ∈ V0 then 0 ≤ rω ≤ |ω|,
which proves ﬁniteness.
Similarly, taking e = 0 ∈ {0, 1}s+1, we see that any vertex v = (r, ±1) has an
edge to some v′ = (r
′, ±1) with |r
′| ≤ |r| /2. Repeating this argument, we may
ﬁnd a path from any v ∈ V0 to one of (0, +1), (0, −1). Thus, to prove that G0
is strongly connected, it will suﬃce to show that there exists a path from (0, −1)
to (0, +1), which (in light of symmetry) is equivalent to (0, −1) ∈ V0. Since G is
symmetric under R, this will also imply that R(V0) = V0.
It remains to show that (0, −1) ∈ V0. We do this by explicitly constructing the
path from (0, +1) to (0, −1). Let r
(0) = r
(s+1) = 0, and for j = 1, 2, . . . , s let
r
(j) = (r(j)
ω ) be given by

r(j)
ω =
 {1 if ω1 = ω2 = · · · = ωi = 1,
0 otherwise.

We claim that for each j = 0, 1, . . . , s − 1, there is an edge from (r
(j), +1) to
(r
(j+1), +1), and for j = s there is an edge from (r
(s), +1) to (r
(s+1), −1).
For j = 0, deﬁne e(0) by e(0)
0 = e(0)
1 = 1 and e(0)
i = 0 for i ̸= 0, 1. Direct
computation shows that δ(r
(0); e(0))ω = ⌊ 1+ω1
2 ⌋ = 1 if ω1 = 1 and 0 otherwise. We
also have ∣
∣r
(0)∣
∣ = 0. Hence, G contains an edge from (r
(0), +1) to (r
(1), +1).

For 1 ≤ j ≤ s − 1, let e(j)
j+1 = 1 and e(j)
i = 0 for i ̸= j + 1. We compute

that δ(r
(j); e(j))ω = ⌊ r(j)
ω +ωj+1
2 ⌋ = 1 if ωj+1 = 1 and r(j)
ω = 1, and 0 otherwise.

GOWERS NORMS FOR THE THUE-MORSE AND RUDIN-SHAPIRO SEQUENCES 7

Also, ∣
∣r
(j)∣
∣ = 2s−j ≡ 0 (mod 2). Hence, G contains an edge from (r
(j), +1) to
(r
(j+1), +1).
Finally, for j = s, let e(s) = 0. Computation similar to the one above shows
that G contains an edge from (r
(s), +1) to (r
(s+1), −1). □

Corollary 2.4. There exists a constant c > 0 such that A(L, 0) = O(2−cL).

Proof. Because G is aperiodic and strongly connected, the Frobenius-Perron The-
orem implies that there exists a stationary distribution π : V0 → [0, 1] such that for
each v, v′ ∈ V0 we have P (l)(v, v′) → π(v′) with exponential convergence rate:

(21) max
v,v′∈V0
 ∣
∣
∣P (l)(v, v′) − π(v′)
∣
∣
∣ = O(2−cl)

for some c > 0. Because R(V0) = V0, by symmetry we have π(R(v)) = π(v) for all
v ∈ V0. Combining this with (21), we obtain

(22) max
v,v′
 ∣
∣
∣P (l)(v, v′) − P (l)(v, R(v′))
∣
∣
∣ = O(2−cl).

Using this estimate and the trivial bound |A(L, r)| ≤ 1 in (20), we arrive at

(23) A(L, 0) = O(2−cl + 2−(L−l)).

It remains to put l = L/2 (say) to conclude that A(L, 0) = O(2−c′L) with c′ >
0. □

Remark 2.5. Computation of the constant c in the argument above is essentially
equivalent to computing the spectral gap for the matrix (P (v, v′))v,v′∈V0 . In par-
ticular, for ﬁxed s, this is a computationally tractable problem.

Proof of Theorem A. Split [N ] into intervals Ij = [mj2Lj , (mj + 1)2Lj ) where L1 >
L2 > . . . . We then have

(24) ∥t∥U s[N ] =
 ∥
∥
∥
∥
∥
∥

∑

j 1Ij t
∥
∥
∥
∥
∥
∥
U s[N ]
 ≤ ∑

j
 ∥
∥1Ij t∥
∥
U s[N ] .

The cubes {n + ω · h | ω ∈ {0, 1}s} ⊂ Ij are precisely the translations of the cubes
{n + ω · h | ω ∈ {0, 1}s} ⊂ [2Lj ] by 2Lj mj. Since t(2Lj mj + n) = t(2Lj mj)t(n) for
n ∈ [2Lj ], we conclude that
∥
∥1Ij t∥
∥
U s[N ] = ∥
∥1[Ij]∥
∥
U s[N ] · ∥t∥U s[2
Lj ] ≪ 2Lj

N ∥t∥U s[2
Lj ] .

Inserting this into (24) and applying Corollary 2.4 yields (with c′ = c/2s using
notation therein) we obtain

∥t∥U s[N ] ≪ ∑

j 2Lj(1−c′)/N ≪ N −c′. □

3. Rudin-Shapiro sequence

We now move on to the Rudin-Shapiro sequence r(n) = (−1)
f11(n), and embark
upon the proof of Theorem B. Our argument is similar to the one in Section 2,
although slightly more technical. Complications arise because of the fact that the
2-kernel
 N2(r) = {n ↦→ r(2ln + m) ∣
∣ 0 ≤ m < 2l} = {±r(n), ±r(2n + 1)}

8 J. KONIECZNY

contains other functions apart from ±r(n), which forces us to deal with averages
more general than those in (15).
A key feature of r(n) which allows our argument to work is that N2(r) is sym-
metric, i.e. N2(r) = −N2(r). Denote N +
2 (r) = {r(n), r(2n + 1)}, and ﬁx from now
on the value of s ∈ N≥2. We will study the averages

(25) A(L, a, r) := E
n,h
 ∏

ω∈{0,1}s aω(n + ω · h + rω),

where {n + ω · h | ω ∈ {0, 1}s} ⊂ [2L], L ∈ N0, a = (aω)ω∈{0,1}s with aω ∈ N +
2 (r)
and r = (rω)ω∈{0,1}s with rω ∈ Z.
We record a recurrence relation analogous to Lemma 2.1. Now, it will be more
convenient to consider l consecutive steps.

Lemma 3.1. For any l, the averages A(L, a, r) obey the recursive relation:

(26) A(L, a, r) = E
e A(L − l, δ(l)(a; r, e), δ(l)(r; e)) + O(2−(L−l)),

where the average is taken over e = (ei)
s
i=0 ∈ [2l]s+1, δ(l)(a; r, e) is given by

(27) δ(l)(a; r, e)ω(n) = aω (
2ln + (rω + (1, ω) · e mod 2l)) ,

and δ(l)(r; e) is given by

(28) δ(l)(r; e)ω = ⌊ rω + (1, ω) · e
2l
 ⌋ .

Proof. Fix the value of l. Any cube Q = {n + ω · h | ω ∈ {0, 1}s} can be uniquely
written as {
2l(n′ + ω · h′) + (1, ω) · e ∣
∣ ω ∈ {0, 1}s}
, where e ∈ [2l]s+1. Up to errors
of the order of O(2−(L−l)), choosing Q ⊂ [2L] uniformly at random is equivalent
to choosing e ∈ [2l]s+1 and Q′ = {n′ + ω · h′ | ω ∈ {0, 1}s} ⊂ [2L−l] uniformly at
random, hence

A(L, a, r) = E
e E
n′,h′
 ∏

ω∈{0,1}s aω(2k(n′ + ω · h′) + (1, ω) · e + rω) + O(2−(L−l))

= E
e E
n′,h′
 ∏

ω∈{0,1}s δ(l)(a; r, e)ω(n′ + ω · h′ + δ(l)(r; e)ω) + O(2−(L−l)),

which is precisely the stated formula. □

For l = 1, we write δ for δ(1). Note that the symbol δ is used to denote several
diﬀerent functions, but this will not lead to ambiguity because it can always be
inferred from the arguments which function is meant.
Like in the previous section, we introduce a random walk WRS on a graph G =
(V, E), which is associate to the averages A(L, a, r). The set of vertices V consists
of triples (a, r, ±1), where aω ∈ N +
2 (r) and rω ∈ Z. For v = (a, r, σ) ∈ V , we write
A(L, v) = σA(L, a, r).
Using the fact that N2(r) = N +
2 (r) ∪ (−N +
2 (r)), we see that for any a with
aω ∈ N2(r), we can ﬁnd ¯a = (¯aω)ω∈{0,1}s with ¯aω ∈ N +
2 (r) and σ = ±1, such that∏
ω aω(xω) = σ ∏ω ¯aω(xω). In particular, for any r we have A(L, a, r) = A(L, v)
for any L, where v = (¯a, r, σ) ∈ V .
Let l ∈ N be ﬁxed. Then, for e ∈ [2l]s+1 and v = (a, r, σ) ∈ V , we let
δ(l)(v; e) ∈ V denote the vertex constructed above, corresponding to the aver-
ages A(L, δ(l)(a; r, e), δ(l)(r; e)). (In other words, δ(l)(v; e) = (a
′, r
′, σ′), where

GOWERS NORMS FOR THE THUE-MORSE AND RUDIN-SHAPIRO SEQUENCES 9

a′
ω = ±δ(l)(a; r, e)ω, r′
ω = δ(l)(r; e) and σ′ = ±1 is chosen so that σ′ ∏
ω aω(xω) =
σ ∏
ω δ(l)(a; r, e)ω(xω)).
The transition probabilities are given by P (v, v′) = Pe∈{0,1}s+1(δ(v; e) = v′) for
v, v′ ∈ V , so that (26) for l = 1 is equivalent to

(29) A(L, v) = ∑

v′∈V P (v, v′) A(L − 1, v′) + O(2−L).

The edge from v to v′ is present in the edge set E of G if P (v, v′) > 0.
More generally, for arbitrary l ∈ N we have

(30) A(L, v) = ∑

v′∈V P (l) (v, v′) A(L − l, v′) + O(2−(L−l)),

where P (l) (v, v′) = Pe∈[2l]s+1(δ(l)(v; e) = v′) denotes the probability of transition
from v to v′ in l steps. Accordingly, a path of length l from v = (a, r, +1) to v′ ∈ V
exists if and only if the average A(L − l, v′) is present on the right hand side of (26),
meaning that there exists e = (ei)
k
i=0, 0 ≤ ei < 2l, such that δ(l)((a, r, +1); e) = v′.
Following the same reasoning as before, we note that G has a natural symmetry
R : V → V given by (a, r, σ) ↦→ (a, r, −σ), which preserves the transition proba-
bilities. We will denote by V0 the set of vertices reachable from the initial vertex
v0 = ((r)ω∈{0,1}s , 0, +1) and by G0 the induced graph.

Proposition 3.2. Let G0 be the graph constructed above. Then G0 is ﬁnite,
strongly connected, aperiodic, and preserved by R.

Proof. Finiteness, aperiodicity, and strong connectedness follow from essentially the
same argument as in Propositions 2.3. It remains to prove that R(v0) is reachable
from v0.
Pick any l ≥ s + 2, and ei = 2i−1 for i = 1, 2, . . . , s; we leave 0 ≤ e0 < 2s

undeﬁned for the time being. It follows from Lemma 3.1 and subsequent discussion
that G0 contains a path of length l from v0 to v1 = (a, r, σ) equal to δ(l)(v0; e).
We will now identify the vertex v1. As for a = (aω)ω, we notice that

(31) aω(n) = ±r(2ln + (1, ω) · e) = ±r(n)r((1, ω) · e) = r(n).

Above, we use that fact that (1, ω) · e < 2l−1. Next, r = (rω)ω is given by

rω = ⌊ (1, ω) · e
2l
 ⌋ = 0,

by virtue of the same estimate as before. Finally, σ is the product of the ±1 factors
implicit in (31), hence

σ = ∏

ω∈{0,1}s r((1, ω) · e) =
 2
s−1∏

m=0 r(m + e0).

Thus, v1 is equal to R(v0), provided that σ = σ(e0) deﬁned above is equal to
−1, and v1 = v0 otherwise. It remains to ﬁnd e0 for which σ(e0) = −1. In
fact, it will suﬃce to show that σ(e0) is not constant with respect to e0. Since
σ(e0 + 1)/σ(e0) = r(2s + e0)/r(e0), we have σ(e0 + 1) = −σ(e0) for any choice
2s−1 ≤ e0 < 2s, which ﬁnishes the argument. □

Corollary 3.3. There exists a constant c > 0 such that ∥t∥U s[2L] = O(2−cL).

Proof. Direct adaptation of the argument in Corollary 2.4. □

10 J. KONIECZNY

Proof of Theorem B. We begin by splitting the interval [N ] into a disjoint union
of intervals Ij of the form [mj2Lj+1, mj2Lj+1 + 2Lj ), and a remainder part J so
that |J| ≪ log N and each exponent L appears among Lj’s at most log N times.
This can be accomplished by ﬁrst splitting [N ] into dyadic intervals [m′
j2L′
j , (m′
j +
1)2L′
j ) (with L′
j all distinct), and then splitting each of these further into intervals
[(m′
j + 1)2L′
j − 2k, (m′
j + 1)2L′
j − 2k + 2k−2) for 2 ≤ k < L′
j, and the singleton of
(m′
j + 1)2L′
j − 1 (which we put in J).
For each of the intervals Ij and for any n+ mj2Lj +1 ∈ Ij , n ∈ [2j], we have r(n+
mj2Lj +1) = r(n)r(mj ), whence ∥
∥1Ij r∥
∥U s[N ] ≪ 2
Lj
N ∥r∥U s[2
Lj ]. Using Corollary 3.3

and the bound ∥1J∥U s[N ] ≪ (|J| /N )
1/2
s , we may now estimate:

∥t∥U s[N ] ≪ ∑

j
 2Lj(1−c)

N + N −1/2
s+o(1)

≪ log N
N
 ∑

L≤log N 2L(1−c) + N −1/2
s+o(1) ≪ N −c′,

where 0 < c′ < min(c, 1/2s) is arbitrary. □

4. Closing remarks

Our argument in Section 3 dealing with the Rudin-Shapiro sequence can be gen-
eralised to other automatic sequences. We hope to address this in an upcoming
paper with Jakub Byszewski and Clemens M¨ullner. Here, we discuss some simple
generalisations which can be obtained by slight adaptations of the existing argu-
ment, as well as the key obstacles which need to be overcome for further progress
to be made.
A crucial feature of the Rudin-Shapiro sequence which we exploited was the sym-
metry of the kernel, so for the time being let us restrict our attention to 2-automatic
sequences a(n) with N2(a) = −N2(a). Natural examples of such sequences are the
given by the “pattern counting” sequences of the form a(n) = (−1)
fπ(n), where π
is a word over the alphabet {1, 0} and fπ(n) denotes the number of times π ap-
pears in the binary expansion of n. (Hence, π = 1 for Thue-Morse and π = 11 for
Rudin-Shapiro. To avoid technical complications, assume that π begins and ends
with 1.)
The recursive relation analogous to (26) from Lemma 3.1 holds in full general-
ity, and similarly the corresponding random walk can be constructed without any
signiﬁcant modiﬁcations. It remains true that the underlying graph is symmetric,
and that the analogue of (30) holds. Provided that the graph has the properties
mentioned in Proposition 3.2, the analogue of Corollary 3.3 stating that ∥a∥U s[2L] =
O(2−cL) follows immediately. To obtain the bound ∥a∥U s[N ] = O(N −c) for general
N , one can apply a decomposition of [N ] analogous to that in the Proof of Theorem
B. For pattern counting sequences introduced above, this construction is repeated
almost verbatim, except one uses intervals of the form [2L(2|π|m), 2L(2|π|m + 1)),
where |π| denotes the length of the pattern.
The key diﬃculty lies in proving the analogue of Proposition 3.2, asserting that
the graph supported on the vertices reachable from the origin in the random walk
is ﬁnite, aperiodic, strongly connected and preserved under the natural symmetry.

GOWERS NORMS FOR THE THUE-MORSE AND RUDIN-SHAPIRO SEQUENCES 11

Finiteness is clear in full generality, by the same reasoning as in Proposition 2.3. We
expect that aperiodicity should be easy to check; for pattern counting sequences
we simply have a loop labelled 0 at the origin. Strong connectedness does not
appear to be crucial, since we may consider the strongly connected components
independently; for pattern counting sequences continuing from any vertex along
the edges labelled 0 leads to either the origin or its symmetric image.
Proving the symmetry is presumably the most diﬃcult part. However, in the
case of pattern counting sequences, it can be carried out by a slight modiﬁcation
of the argument in Proposition 3.2. The only diﬀerence is that (with the notation
taken from the proof of Proposition 3.2) we need to take l ≥ s + |π| now, and notice
that σ(e0 + 1)/σ(e0) = a(2s + e0)/a(e0) = −1 for suitable choice of e0. Hence,
we expect that for a pattern counting sequence such a(n) = (−1)
fπ(n) we have
∥a∥U s[N ] = O(N −c) for a constant c = c(a, s) > 0.
Conversely, one may ask about the minimal conditions under which it can be
shown that ∥a∥U s[N ] = o(1). It is well-known that a sequence with small uniformity
norms cannot correlate with a polynomial phase, or indeed with an s-step nilse-
quence. While it would be surprising to ﬁnd an automatic sequence correlating
with (say) a quadratic phase e2πiαn
2 (with α ∈ R \ Q), it is certainly possible to
have automatic sequences which correlate with periodic sequences. (In fact, in the
situation above it is not hard to show that En<N a(n)e2πiαn
2 = o(1) as N → ∞.)
Motivated by our main theorems and the above discussion, we are led to suspect
the following. The suspicion is especially strong in the case of sequences with
symmetric kernel.

Conjecture. Let a(n) be a 2-automatic sequence such that En<N a(qn + r) → 0
as N → ∞ for any q ∈ N, r ∈ N0. Then, ∥a∥U s[N ] → 0 as N → ∞ for any s ∈ N.

References

[AS03] Jean-Paul Allouche and Jeﬀrey Shallit. Automatic sequences. Cambridge University
Press, Cambridge, 2003. Theory, applications, generalizations.
[DDM12] Jean-Marc Deshouillers, Michael Drmota, and Johannes F. Morgenbesser. Subse-
quences of automatic sequences indexed by ⌊nc⌋ and correlations. J. Number Theory,
132(9):1837–1866, 2012.
[DMR13] Michael Drmota, Christian Mauduit, and Jo¨el Rivat. The Thue-Morse sequence along
squares is normal, 2013. Preprint.
[Drm14] Michael Drmota. Subsequences of automatic sequences and uniform distribution. In
Uniform distribution and quasi-Monte Carlo methods, volume 15 of Radon Ser. Com-
put. Appl. Math., pages 87–104. De Gruyter, Berlin, 2014.
[Fan] Aihua Fan. Oscillating sequences of higher order and topological systems of quasi-
discrete spectrum. Preprint.
[Gel68] A. O. Gel’fond. Sur les nombres qui ont des propri´et´es additives et multiplicatives
donn´ees. Acta Arith., 13:259–265, 1967/1968.
[Gow01] W. T. Gowers. A new proof of Szemer´edi’s theorem. Geom. Funct. Anal., 11(3):465–588,
2001.
[Gre] Ben Green. Higher-Order Fourier Analysis, I. (Notes available from the author).
[HK09] Bernard Host and Bryna Kra. Uniformity seminorms on ℓ∞ and applications. J. Anal.
Math., 108:219–276, 2009.
[MR09] Christian Mauduit and Jo¨el Rivat. La somme des chiﬀres des carr´es. Acta Math.,
203(1):107–148, 2009.
[MR10] Christian Mauduit and Jo¨el Rivat. Sur un probl`eme de Gelfond: la somme des chiﬀres
des nombres premiers. Ann. of Math. (2), 171(3):1591–1646, 2010.

12 J. KONIECZNY

[MR15] Christian Mauduit and Jo¨el Rivat. Prime numbers along Rudin-Shapiro sequences. J.
Eur. Math. Soc. (JEMS), 17(10):2595–2642, 2015.
[MS98] Christian Mauduit and Andr´as S´ark¨ozy. On ﬁnite pseudorandom binary sequences. II.
The Champernowne, Rudin-Shapiro, and Thue-Morse sequences, a further construction.
J. Number Theory, 73(2):256–276, 1998.
[MS15] Clemens M¨ullner and Lukas Spiegelhofer. Normality of the Thue-Morse sequence along
Piatetski-Shapiro sequences, II, 2015. Preprint. arXiv:1511.01671 [math.NT].
[Tao12] Terence Tao. Higher order Fourier analysis, volume 142 of Graduate Studies in Math-
ematics. American Mathematical Society, Providence, RI, 2012.

Mathematical Institute, University of Oxford, Andrew Wiles Building, Radcliffe
Observatory Quarter, Woodstock Road, Oxford, OX2 6GG
E-mail address: jakub.konieczny@gmail.com
