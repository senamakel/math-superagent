<!-- source: https://arxiv.org/pdf/1812.01224 | converted from PDF -->

FOURIER UNIFORMITY OF BOUNDED MULTIPLICATIVE
FUNCTIONS IN SHORT INTERVALS ON AVERAGE

KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Abstract. Let λ denote the Liouville function. We show that as X → ∞,
∫ 2X

X sup
α
 ∣
∣
∣
∣
∣
∣
 ∑

x<n≤x+H λ(n)e(−αn)

∣
∣
∣
∣
∣
∣ dx = o(XH)

for all H ≥ X θ with θ > 0 ﬁxed but arbitrarily small. Previously, this was only
known for θ > 5/8. For smaller values of θ this is the ﬁrst “non-trivial” case of
local Fourier uniformity on average at this scale. We also obtain the analogous
statement for (non-pretentious) 1-bounded multiplicative functions.
We illustrate the strength of the result by obtaining cancellations in the sum of
λ(n)Λ(n + h)Λ(n + 2h) over the ranges h < X θ and n < X, and where Λ is the
von Mangoldt function.
 1. Introduction

Let λ denote
1 the Liouville function, that is, a completely multiplicative function
with λ(p) = −1 at all primes p. Among bounded multiplicative functions, λ plays a
distinguished role since the prime number theorem is equivalent to
2
∑

n≤x λ(n) = o(x) (1)

as x → ∞, and the Riemann Hypothesis is equivalent to
∑

n≤x λ(n) = Oε(x1/2+ε) for all ε > 0.

A far reaching generalization of (1) is Chowla’s conjecture [4], according to which,
for any sequence of distinct integers h1, h2, . . . , hk, one has
∑

n≤x λ(n + h1) · · · λ(n + hk) = o(x) (2)

1All the results for λ discussed here are also applicable to the M¨obius function µ with only minor
changes to the arguments; we leave the details to the interested reader.
2Our conventions for asymptotic notation are given at the end of this introduction.
1arXiv:1812.01224v1  [math.NT]  4 Dec 2018
2 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

as x → ∞, where we adopt the convention that λ(n) = 0 for n ≤ 0. Because of the
equivalence of (1) and the prime number theorem, Chowla’s conjecture is frequently
viewed as a “higher order” prime number theorem.
In recent years there has been a substantial amount of progress on Chowla’s con-
jecture. Following the work of the ﬁrst two authors [23] the authors established in
[24] an averaged form3 of this conjecture in the case k = 2, namely,
∑

|h|≤H
 ∣
∣
∣ ∑

n≤x λ(n)λ(n + h)∣
∣
∣ = o(Hx) (3)

provided that H → ∞ as x → ∞; see also [1, 18, 19, 26, 12, 7, 25] for some other
averaged forms of Chowla’s conjecture (as well as the closely related Elliott and
Hardy-Littlewood conjectures). An equivalent form of (3) (for related discussion,
see [32]) states that
 sup
α
 ∫ 2X

X
 ∣
∣
∣ ∑

x<n≤x+H λ(n)e(−αn)
∣
∣
∣dx = o(HX) (4)

provided that H → ∞ as X → ∞. The estimate (4) along with the entropy decre-
ment argument was used by the third author [31] to establish a logarithmically
averaged version of Chowla’s conjecture, that is,
∑

n≤x
 λ(n)λ(n + h)
n = o(log x)

as x → ∞, for any ﬁxed integer h ̸= 0. Subsequently for odd k, the third author and
Ter¨av¨ainen [34] used the entropy decrement argument and the Gowers uniformity of
the (W -tricked) von Mangoldt function (but avoiding the use of (4)), to show that

∑

n≤x
 λ(n + h1) . . . λ(n + hk)
n = o(log x) (5)

as x → ∞, for any distinct integers h1, . . . , hk and k odd. Their argument only
partially generalizes to arbitrary multiplicative functions (see [33]); in the case of the
Liouville function, it relies crucially on the assumption that k is odd.
In order to establish (5) for all k it is necessary to establish (the logarithmically av-
eraged version of) what we call the local (higher order) Fourier uniformity conjecture
(see [32]).

3By applying H¨older’s inequality to (3), it is also possible to obtain an averaged version of (2)
over all shifts h1, . . . , hk; see [24] for details.

FOURIER UNIFORMITY 3

Conjecture 1.1 (Local higher order Fourier Uniformity). Let s ≥ 0. Let G\Γ be
an s-step nilmanifold. Let F : G\Γ → C be Lipschitz continuous and let x0 ∈ G\Γ.
Then ∫ 2X

X sup
g∈G
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H λ(n)F (gn−⌊x⌋x0)

∣
∣
∣
∣
∣ dx = o(HX)

as soon as H → ∞ with X → ∞.

We refer to [14] for the deﬁnition of the terms above, however we will not need
these notions in this paper. Informally, the conjecture asserts that on most short
intervals, λ does not exhibit signiﬁcant correlation with any s-step nilsequence (of
bounded complexity). The estimate (4) proven in [24] essentially corresponds to the
case s = 0 of Conjecture 1.1; this is currently the only case of the conjecture that is
completely settled.
In this paper we make a ﬁrst step in going beyond the case of s = 0 and establish
the case s = 1 of Conjecture 1.1 when H = X θ with θ > 0 ﬁxed but otherwise
arbitrarily small. Let us ﬁrst re-state our main result for the Liouville function in a
more elementary fashion.

Theorem 1.2 (Local Fourier Uniformity for s = 1 at scale X θ). Let θ ∈ (0, 1) be
given and set H = X θ. Then
∫ 2X

X sup
α
 ∣
∣
∣ ∑

x<n≤x+H λ(n)e(−αn)
∣
∣
∣dx = o(XH).

as X → ∞.

We restrict attention here to the regime θ ∈ (0, 1), since the case θ ≥ 1 follows
from the classical work of Davenport [5] (and see [11], [13] for the s = 2 and s > 2
cases respectively of Conjecture 1.1 for this range of θ). Informally, Theorem 1.2
asserts that on most intervals of the form [x, x + xθ], the Liouville function λ(n) does
not exhibit singiﬁcant correlation with linear phases e(αn); it can easily be shown to
imply the s = 1 case of Conjecture 1.1 in the range H ≥ X θ by approximating the
1-step nilsequence n ↦→ F (gn−⌊x⌋x0) by a Fourier series.
Previously, Theorem 1.2 was known unconditionally only for θ > 5/8 from the
work of Zhan [36], who showed that as X → ∞ the bound ∑
x<n≤x+H λ(n)e(−αn) =
o(XH) holds pointwise in x ∈ [X, 2X] for H > X 5/8+ε. It is likely that our method
can be pushed to reach H = exp((log x)1−δ) for some δ > 0, and conditionally on
the Riemann Hypothesis one should in principle be able to reach H = (log X)ψ(X)

for any function ψ(X) going to inﬁnity arbitrarily slowly with X, although this may
require a more careful reworking of the arguments here. It may be possible to extend
the methods to this paper to also cover the s > 1 case (again with H = X θ for any
ﬁxed θ > 0); we plan to investigate this direction in future work.

4 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Theorem 1.2 allows us to obtain cancellations in rather general triple correlations
such as those of the form λ(n)a(n + h)b(n + 2h), for sequences a(·) and b(·) for which
sharp sieve majorants can be constructed. We illustrate the ﬂavor of these results in
the corollary below.

Corollary 1.3. Let θ ∈ (0, 1) be given. Let H = X θ. Then
∑

|h|≤H
 (
1 − |h|
H
 ) ∑

n≤X λ(n)Λ(n + h)Λ(n + 2h) = o(HX)

as X → ∞.

Interestingly we are unable to obtain an asymptotic for
∑

|h|≤H
 (
1 − |h|
H
 ) ∑

n≤X Λ(n + h)Λ(n + 2h)

for this range of H, since this latter problem is essentially equivalent to evaluating
asymptotically ∑
x≤n<x+H Λ(n) for almost all x ≤ X. The best result in this direction
allows one to take H > X 1/6−ε(X) with ε(X) tending to zero arbitrarily slowly as
X → ∞. This is due to Zaccagnini [35], building on ideas of Heath-Brown [15] and
Huxley [16]. Thus, Corollary 1.3 gives a rare example of a sum involving the Liouville
function that becomes harder to control when the Liouville function is removed!
In a subsequent paper we will obtain variants of Theorem 1.2 and Corollary 1.3
for unbounded multiplicative functions such as the divisor function or coeﬃcients of
automorphic forms. This will improve (in the H aspect) earlier results of Blomer [3]
that allowed one to take H = X 1/3+ε in the triple correlations of the divisor function;
however, in contrast to the results of [3], we will not obtain power-savings in the error
terms.
Theorem 1.2 can in fact be generalized to almost all multiplicative functions f :
N → C with |f | ≤ 1 (we call such multiplicative functions 1-bounded ). There is
however one obstruction: if f (n) = n
itχ(n) with |t| ≤ εX 2/H 2 for a small absolute
constant ε > 0 and χ a Dirichlet character of bounded conductor q, then one can
check (using a Taylor expansion) that
∫ 2X

X sup
α
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H f (n)e(−αn)

∣
∣
∣
∣
∣ dx ≫ XH. (6)

In fact for each x ∈ [X, 2X] one can set α equal to t
x + a
q for some integer a coprime to
q, and then f (n)e(−αn) ≈ χ(n)e(−an/q)xit will typically have a mean of magnitude
≍ 1/
√q if χ is primitive.
Therefore the proper analogue of Theorem 1.2 can only hold for multiplicative
functions f that “do not pretend” to be any multiplicative function of the form

FOURIER UNIFORMITY 5

n ↦→ nitχ(n) with |t| ≤ X 2/H 2 and χ of bounded conductor. To quantify this notion
of “pretentiousness”, we follow Granville and Soundararajan [9] and introduce the
distance function

D(f ; X; Q) := inf
χ mod q
q≤Q
|t|≤X
 ( ∑

p≤X
 1 − Re(f (p)pitχ(p))
p
 )1/2.

In particular D(f ; X; Q) is small whenever f is close to n ↦→ nitχ(n) with4 |t| ≤ X
and χ of conductor ≤ Q.
Our main theorem, stated below, conﬁrms that n ↦→ n
itχ(n) with |t| ≤ X 2/H 2−o(1)

and χ of bounded conductor are essentially the only examples of 1-bounded multi-
plicative functions for which (6) can happen.

Theorem 1.4 (Main theorem). Let θ ∈ (0, 1) and η > 0. Let f : N → C be a
multiplicative function with |f | ≤ 1. Suppose that, for H = X θ, we have
∫ 2X

X sup
α
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H f (n)e(−αn)
∣
∣
∣
∣
∣ dx ≥ ηHX.

Then, for any ρ ∈ (0, 1
8),
 D(f ; X 2/H 2−ρ; Q) ≪η,θ,ρ 1

for some Q ≪η,θ,ρ 1.

Theorem 1.4 yields an analogous result to Corollary 1.3 for general multiplicative
functions. Without going into full generality we highlight that the result holds for
correlations f (n)a(n + h)b(n + 2h) and sequences a(n), b(n) that admit sharp sieve
majorants. We illustrate this principle in the corollary below.

Corollary 1.5. Let θ ∈ (0, 1). Let f : N → C be a 1-bounded multiplicative function.
Suppose that a(n), b(n) are sequences such that a(n), b(n) ≪ 1 + Λ(n) for all n ≥ 1.
If ∣
∣
∣
∣
∣
∣
 ∑

|h|≤H
 (1 − |h|
H
 ) ∑

n≤X f (n)a(n + h)b(n + 2h)

∣
∣
∣
∣
∣
∣ > ηXH

with H = X θ, then for any ρ ∈ (0, 1
8),

D(f ; X 2/H 2−ρ; Q) ≪η,θ,ρ 1

for some Q ≪η,θ,ρ 1.

4The role of the parameter X here is mostly to control the size of t. It is not important that the
sum over p runs up to X; it could run up to X B for any B > 0, since primes in (X α, X β] contribute
only Oα,β(1) to the distance.

6 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

The claim holds also when f (n)a(n+h)b(n+2h) is replaced by a(n)f (n+h)b(n+2h)
or by a(n)b(n + h)f (n + 2h).

We give the short derivation of Corollary 1.5 from Theorem 1.4 in Section 6. It is
possible to extend Corollary 1.5 to sequences b(n) or a(n) equal to a multiplicative
function h : N → C such that |h(n)| ≤ dk(n) for all n ≥ 1 and k ≥ 1 a ﬁxed integer.
Since we will obtain a stronger result along these lines in a follow-up paper we do
not include the details here.
It is immediate from Corollary 1.5 that given 1-bounded multiplicative functions
f1, f2, f3, the correlations
∑

|h|≤H
 (
1 − |h|
H
 ) ∑

n≤X f1(n)f2(n + h)f3(n + 2h)

vanish asymptotically whenever at least one of the fi is non-pretentious in the sense
that D(fi; X, Q) → ∞ as X → ∞ for each Q. In the remaining case that all of the fi
are pretentious, an asymptotic for the correlations, without an average over h, can
be obtained using the method of [20] (see also the references therein).

1.1. An overview of the proof. We now describe in some detail the main ideas
behind the proof of Theorem 1.4. Our presentation here is somewhat oversimpliﬁed
to avoid technical issues; the actual rigorous argument will not quite follow the
outline given here, but uses essentially the same ideas, despite being arranged slightly
diﬀerently to resolve these technicalities.
First we notice that, by the “analytic” large sieve inequality (or more precisely,
a maximal version of this inequality due to Montgomery [28]), given an interval
I = (x, x + H], there are at most ≪ η−2 values αI (modulo 1 and up to perturbations
by O(1/H)) for which ∣
∣
∣
∣
∣
∑

n∈I ′ f (n)e(−αIn)

∣
∣
∣
∣
∣ > ηH (7)

for some I ′ ⊂ I; see Lemma 2.2. For sake of this informal presentation, one can
pretend that in fact there is only one such value αI (modulo 1 and perturbations by
O(1/H)). Thus, if there are two subintervals I ′
1, I ′
2 of I (or of a slight dilate of I)
and two frequencies αI,1, αI,2 obeying (7), one can pretend that

αI,1 = αI,2 + O ( 1
H
 ) (mod 1). (8)

Informally, the estimate (7) asserts that f exhibits signiﬁcant oscillation at fre-
quency αI on the interval I (or a large subinterval of this interval). We depict this
situation schematically in Figure 1. In the schematic depictions we are pretending

FOURIER UNIFORMITY 7

Figure 1. A schematic depiction of an interval I in which f oscillates
with frequency αI.

that if two such intervals I1, I2 overlap (or are very near to each other), then their
associated frequencies αI1, αI2 are close modulo 1 in the sense of (8).
At this point we point out a key example: if f (n) = n
it for some t = o(X 2/H 2),
some Taylor expansion of the phase n ↦→ t log n of f in I reveals that one has the
above inequality for some η ≫ 1 and αI = t
xI , where xI denotes the starting point
of I. Thus, under the hypotheses of Theorem 1.4, we expect αI to vary in I in a
manner which is “inversely proportional” to the location of I in some sense. The bulk
of our argument is devoted to rigorously verifying some version of this expectation;
the main obstacle to overcome arises from the fact that αI is only determined up
modulo 1 and up to perturbations by O(1/H).
Next, we recall an observation of Elliott [6] that by an application of the arithmetic
large sieve inequality for a big set of primes P = PI ⊂ [2, H 1/2], we have, for all p ∈ P,

1
p
 ∣
∣
∣
∣
∣
∑

n∈I f (n)e(−αIn)

∣
∣
∣
∣
∣ ≈
 ∣
∣
∣
∣
∣
∣
 ∑

n∈I/p f (n)e(−αInp)

∣
∣
∣
∣
∣
∣ ; (9)

see Proposition 2.5. To make things simpler we proceed in this outline as if the
approximation (9) held for all primes p ≍ P with P := H ε and some small absolute
constant ε > 0. Informally, (9) asserts that if f (n) behaves like a constant multiple of
e(αIn) for n ∈ I, then f (m) behaves like a constant multiple of e(αImp) for m ∈ I/p.
Heuristically, this follows from the relationship f (mp) = f (p)f (m) (at least when
m is coprime to p). We describe the estimate (9) schematically by the diagram in
Figure 2. Note that this is consistent with the previous heuristic that αI should be
inversely proportional to the location of I.
By the hypotheses of Theorem 1.4, we have some frequencies α(x,x+H] for which
∫ 2X

X
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H f (n)e(−α(x,x+H]n)
∣
∣
∣
∣
∣ dx ≥ ηXH,

and hence by a pigeonhole principle argument, we can ﬁnd a large (≍ X/H) set
of disjoint intervals I of length H in [X, 2X] for which (7) holds (after modifying
η slightly). From this, (9), and the Cauchy-Schwarz inequality, we will be able to
locate a large set of quadruples (I, J, p, q) with I and J disjoint intervals of length

8 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Figure 2. If f oscillates at frequency αI on a long interval I, then
one expects f to oscillate at frequency pαI on the shorter interval I/p.
(The intervals are not drawn to scale.) The dotted arrow indicates the
fact that if one dilates I/p by p one returns to the interval I.

Figure 3. If f oscillates at frequencies αI, αJ on I, J respectively,
and I/p overlaps J/q, then one expects pαI and qαJ to often be close
to each other (modulo integers).

H = X ε for which
∣
∣
∣
∣
∣
∑

n∈I f (n)e(−αIn)
∣
∣
∣
∣
∣ ≫ H and
 ∣
∣
∣
∣
∣
∑

n∈J f (n)e(−αJ n)

∣
∣
∣
∣
∣ ≫ H (10)

and p, q ≍ P = H ε are primes for which (9) holds and such that I/p ∩ J/q ̸= ∅; see
Figure 3.
Since the intervals I/p and J/q are nearby and the frequencies pαI, qαJ lead to
very large values of the short trigonometric polynomial supported respectively on
I/p and J/q, we conclude from (8) that these frequencies lie (modulo 1 and up to
perturbations by O(P/H)) in a bounded set of ≪ 1 frequencies. In particular by

FOURIER UNIFORMITY 9

the pigeonhole principle it follows that, for a positive proportion of disjoint intervals
I, J of length H and primes p, q of size P = H ε with I/p ∩ J/q ̸= ∅, we have the
fundamental approximate equation

pαI ≡ qαJ + O(P/H) (mod 1) (11)

relating the frequencies αI, αJ associated to these intervals. The number of such
quadruples (I, J, p, q) is ≍ (X/H) · (P/ log P )
2, since once I, p, q are chosen, J is
essentially determined by I/p ∩ J/q ̸= ∅.
It would be nice if the congruence (11) held (mod p) rather than just (mod 1),
as one could then proﬁtably divide by p. Fortunately, by the Chinese remainder
theorem there exists a (potentially very large!) integer k depending on J and q such
that if we redeﬁne αJ by shifting it by k, then we do indeed have

pαI ≡ qαJ + O ( P
H
 ) (mod p)

or equivalently
 αI ≡ q
p · αJ + O ( 1
H
 ) (mod 1)

for all p ≍ P , with p ̸= q. Importantly, shifting αJ by k ∈ Z maintains the property
(10), no matter how large k is. The dependence of the integer k on q is a bit
problematic; however let us suppose for sake of discussion that k is independent of
q (we essentially end up achieving this through a diﬀerent argument that involves
two consecutive applications of the arithmetic large sieve). Then applying Cauchy-
Schwarz we conclude that, for a positive proportion of intervals J1, J2 and primes
q1, q2 ≍ P with
5 J1
q1 ∩ J2
q2 ̸= ∅, we have

q1
p αJ1 ≡ q2
p αJ2 + O ( 1
H
 ) (mod 1) (12)

for many primes p ≍ P . This is essentially the outcome of Section 3, though the
argument there proceeds using a somewhat diﬀerent arrangement of the above in-
gredients, most notably in that the prime p ends up being at a diﬀerent scale to the
primes q1, q2, and the intervals J1, J2 have length a bit less than H (and are located
at spatial scales a bit less than X). For sake of this discussion we assume that for the
data J1, J2, q1, q2 as above, the relation (12) holds for all p ≍ P , not just for many
such primes. We depict this relationship in graph theoretic language by connecting
J1 to J2 by an edge which we label by the ratio q2
q1 of the primes needed to get from
J1 to (the vicinity of) J2 by multiplication; see the dashed line in Figure 4. The

5More precisely, J1
q1 and J2
q2 will both intersect a third interval I
p , but this is almost the same as
requiring that these intervals intersect each other, as they are all of comparable size; see Figure 4.
For sake of this discussion, we ignore this technical distinction.

10 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Figure 4. A pair of intervals J1, J2 and primes q1, q2 such that J1/q1
and J2/q2 both meet I/p for many pairs (I, p), and are thus close to
each other. The frequencies αJ1, αJ2 have been adjusted by suitable
integers so that q1
p αJ1, q2
p αJ2 are both close (modulo integers) to αI,
and thus also close to each other (again modulo integers). When one
has the above diagram for all (or most) p ≍ P , we draw a dashed line
from J1 to J2 as indicated. Note that if one dilates J1 by q2
q1 then one
will end up with an interval close to J2.

resulting graph G is essentially undirected (except that if one wanted to get from
J2 to J1 one would use the label q1
q2 rather than q2
q1 ) and multiplicity-free (the ratios
q2
q1 for q1 ̸= q2 are all well separated from each other, so each pair J1, J2 of distinct
intervals may be connected by at most one such ratio).
Notice that the number of intervals J1, J2 and primes q1, q2 ≍ P constructed above
is ≍ (X/H) · (P/ log P )
2; thus the graph G described above has ≍ X/H vertices and
average degree ≍ (P/ log P )
2. We begin Section 4 by applying H¨older’s inequality
on G in a way that is motivated by Sidorenko’s conjecture (see [30]). We choose k
to be the ﬁrst even integer for which
( P
log P
 )2k−2 ≥ ( X
H
 )2 .

Because of our hypotheses H = X θ and P = H ε, we can take k to be independent
of X. Roughly speaking, k is the ﬁrst integer at which we expect to see a very large
number of non-trivial cycles of length 2k in the graph G . After many applications of
H¨older’s ineqality, we can conclude that, for a positive proportion of disjoint intervals
I1, J1 ⊂ [X, 2X] of length H and primes p1, q1 ≍ P with I1/p1 ∩ J1/q1 ̸= ∅, there

FOURIER UNIFORMITY 11

exist
 ≫ H 2

X 2
 ( P
log P
 )4k ≫ 1

“chains” of intervals I2 . . . , Ik, J2 . . . , Jk ⊂ [X, 2X] of length H and primes

p1,1, . . . , pk,1, p1,2, . . . , pk,2, q1,1, . . . , qk,1, q1,2, . . . , qk,2 ≍ P

such that, for all ℓ = 1, 2, . . . , k,
Iℓ
pℓ,1 ∩ Iℓ+1
pℓ,2 ̸= ∅, Jℓ
qℓ,1 ∩ Jℓ+1
qℓ,2 ̸= ∅ (13)

and furthermore the approximate identities

pℓ,1
p αIℓ ≡ pℓ,2
p αIℓ+1 + O ( 1
H
 ) mod 1

qℓ,1
p αJℓ ≡ qℓ,2
p αJℓ+1 + O ( 1
H
 ) mod 1

p1
p αI1 ≡ q1
p αJ1 + O ( 1
H
 ) (mod 1)
 (14)

hold for all p ≍ P , where we adopt the cyclic conventions Ik+1 = I1, Jk+1 = J1. The
above set of relationships corresponds to two cycles of length k in G connected by a
further edge in G; see Figure 5. The choice of k is just large enough to ensure that
the conﬁguration in this ﬁgure will usually be non-degenerate in the sense that the
primes p1,1, . . . , qk,2, p1, q1 that arise are all distinct for most of the conﬁgurations.
Since the primes p in our case are of size P = H ε = X εθ, it suﬃces to take k bounded
in terms of ε, θ to guarantee the existence of a large number of such chains.
Notice that we can interpret each of the relationships in (14) as holding (mod p)
instead of (mod 1) by multiplying by p, thus obtaining the system of equations

pℓ,1αIℓ ≡ pℓ,2αIℓ+1 + O ( P
H
 ) mod p

qℓ,1αJℓ ≡ qℓ,2αJℓ+1 + O ( P
H
 ) mod p

p1αI1 ≡ q1αJ1 + O ( P
H
 ) mod p
 (15)

for all p ≍ P . We can then use the Chinese remainder theorem to replace the
(mod p) congruences in (15) with (mod Q) where Q := ∏

p≍P p. A key point for later
analysis is that Q is going to be extremely large (of size about exp(P ) = exp(X εθ)), so
much so that we will eventually be able to drop the congruence (mod Q) altogether,
once we obtain some more control on the location of the αI.

12 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Figure 5. Two cycles of length k = 4 connected by an edge. Each
dashed line corresponds to a situation of the form described in Figure 4
(for all p ≍ P ). The frequencies αIℓ, αJℓ are not depicted here to reduce
clutter; however, they will obey the approximate identities (14).

After applying some algebra to (15) to eliminate all frequencies except αI1, αJ1,
we eventually conclude the estimates

q′
1αI1 ≡ O (P k

H
 ) (mod Q) (16)

q′
2αJ1 ≡ O ( P k

H
 ) (mod Q) (17)

p1αI1 ≡ q1αJ1 + O ( P
H
 ) (mod Q) (18)

where q′
1 := ∣
∣
∣∏k
ℓ=1 pℓ,1 − ∏k
ℓ=1 pℓ,2∣
∣
∣ and q′
2 := ∣
∣
∣∏k
ℓ=1 qℓ,1 − ∏k
ℓ=1 qℓ,2∣
∣
∣. The integers

q′
1, q′
2 are small; in fact the condition (13) will give the bound q′
1, q′
2 ≪ H O(ε). We can
also assume that these integers are non-zero, because the number of intervals Iℓ, Jℓ
and primes pi,j, qi,j for which q′
j could be zero is negligible. It follows then from (16),

FOURIER UNIFORMITY 13

(17) that
 αI1 ≡ a1
q′
1 Q + TI1
xI1 (mod Q)

αJ1 ≡ a2
q′
2 Q + TJ1
xJ1 (mod Q)

for some a1, a2 ∈ Z, 0 < q′
1, q′
2 ≪ H O(ε), and TI1, TJ1 ≪ X 2/H 2−ρ, where xI1, xJ1 the
starting points of the intervals I1, J1, respectively.
Suppose now for simplicity that q′
1 = q′
2 = 1, so that

αI1 ≡ TI1
xI1 (mod Q) (19)

αJ1 ≡ TJ1
xJ1 . (mod Q) (20)

Notice that since I1 ∩ p1
q1 J1 ̸= ∅ we have xI1 ≈ p1
q1 xJ1. Combining (19), (20) with (18)
we obtain the key relationship

TI1 = TJ1 + O(P X/H) (mod Q);

since TI1, TJ1 are much smaller in magnitude than Q, we may now drop the congru-
ence and conclude in fact that

TI1 = TJ1 + O(P X/H);

informally speaking, this means that the map I ↦→ TI is approximately locally con-
stant on the graph G. Obtaining these quadruples (I1, I2, p1, p2) with all the described
properties is essentially the content of Section 4.
A Taylor expansion shows that if αI1 is as in (19), then e(−αI1n) ≈ e
iθI1 n
2πiTI1
with θI1 ∈ R depending only on I1. Similarly for (20). Thus there exists a positive
proportion set of disjoint intervals I, J connected by an edge in G such that
∣
∣
∣
∣
∣
∑

n∈I f (n)n
2πiTI ∣
∣
∣
∣
∣ ≫ H and
 ∣
∣
∣
∣
∣
∑

n∈J f (n)n2πiTJ ∣
∣
∣
∣
∣ ≫ H.

for some TI, TJ ≪ X 2/H 2 with TI = TJ + O(P X/H). To proceed further, we claim
that the graph G is essentially an “expander graph” and in particular that it has one
very large and highly connected component. This is the content of Section 5.
To see this claim, notice that taking a O(P X/H)-spaced set of values V in the
range {T : T = O(X 2/H 2−ρ)}, we can group the intervals I into subsets A(V )
of those intervals I for which TI = V + O(P X/H). Then, because many pairs of
intervals I, J connected by an edge in G belong to the same A(V ), we obtain a large

14 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

lower bound of the form

X
H · ( P
log P
 )2 ≪ ∑

V
 








 ∑

p,q≍P
 ∑

I∈A(V )
J∈A(V )
I
p ∩ J
q ̸=∅
 1










 (21)

where P := H ε. That is we obtain a lower bound that corresponds to a positive
proportion of disjoint intervals I, J ⊂ [X, 2X] of length H and primes p, q ≍ P such
that I
p ∩ J
q ̸= ∅. Now, since the exponential sum ∑
p≍H ε pit exhibits cancellations, we
can (using a bit of harmonic analysis) essentially bound the above by

≪ ∑

V
 (
#A(V )
2 · H
X · ( P
log P
 )2)

Noticing that ∑

V #A(V) ≪ X/H, we see that the above expression is in turn

≪ (sup
V #A(V )
) · ( P
log P
 )2 , (22)

and therefore, combining (21) and (22), there exists a value V for which #A(V ) ≫
X/H. That is, there exists a universal T ≪ X 2/H 2 (up to non-essential perturba-
tions by O(P X/H) that we can ignore) such that for a positive proportion of disjoint
intervals I of length H we have, ∣
∣
∣
∣
∣
∑

n∈I f (n)n
iT ∣
∣
∣
∣
∣ ≫ H

Averaging over such intervals it follows that, there exists T ∈ R such that |T | ≪
X 2/H 2 and ∫ 2X

X
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H f (n)niT ∣
∣
∣
∣
∣ dx ≫ XH.

By the main theorem of [23] (or rather more precisely its extension to complex valued
functions as in [24, Theorem A.3]) this implies that f has to behave essentially as
n−iT χ(n) with χ a Dirichlet character of bounded conductor and |T | ≪ X 2/H 2, thus
ﬁnishing the proof.
 FOURIER UNIFORMITY 15

1.2. Some ﬁnal remarks. It is very likely that it is possible, at the expense of ad-
ditional technical diﬃculties, to push our argument down to H = exp((log X)
1−δ) for
some δ > 0. However we start running into diﬃculties when H hits exp((log X)
2/3+ε)
and our argument appears to hit a hard limit when H enters the neighborhood of
powers of log X.
The ﬁrst obstruction occurs because we require the set of primes P ⊂ [1, H] to be
suﬃciently dense so that at the very least ∏

p∈P p > X 2. This implies that H needs
to be larger than log X.
The second obstruction which prevents H from going below exp((log X)2/3) occurs
because we require the exponential sum ∑
p≍H ε pit to exhibit cancellations for t of size
X. This is only known for H > exp((log X)2/3+ε) following the work of Vinogradov-
Korobov. This obstruction can be circumvented (in the case of the Liouville function,
at least) by assuming the Riemann Hypothesis. In that case the exponential sum∑

p≍H ε pit will be non-trivially small provided that H is a large power of the logarithm
(speciﬁcally H > (log X)
3/ε). However, we have not veriﬁed that the remaining
portions of the argument extend to this range (among other things, one would need
to make more precise the dependence of various implied constants on the parameter
k, which now must grow with X instead of being ﬁxed).

Notational conventions. As usual f ≪ g, g ≫ f or f = O(g) means that there
is an absolute constant C > 0 such that |f | ≤ Cg. If C needs to depend on some
parameters then we indicate this by subscripts, for instance f ≪η g denotes the
estimate |f | ≤ Cηg for some Cη depending on g. If we write f = o(g) as X → ∞ this
means that |f | ≤ c(X)g where c(X) is a quantity that goes to zero as X tends to
inﬁnity (which may make other quantities dependent on X, such as H, go to inﬁnity
also). We also write f ≍ g for f ≪ g ≪ f .
We set e(x) := e
2πix. The symbol p always denotes a prime, and so do p′, p
′′. Given
an interval I = [a, b] we deﬁne I/p := [a/p, b/p]. Whenever we write α ≡ β + O(η)
(mod 1) we mean that there exists an absolute constant C such that, ∥α − β∥ ≤ C|η|
where ∥x∥ denotes the distance of x from the nearest integer. Similarly whenever
we write α ≡ β + O(η) (mod q) we mean α/q ≡ β/q + O(η/q) (mod 1). Given two
intervals I = [a, b] and J = [c, d] with b < c, whenever we write dist(I, J) ≤ η, we
mean that |c − b| ≤ η. If I = [a, b] and c > 0, we write cI := [ca, cb], thus for instance
I/p = [a/p, b/p].

Acknowledgments. KM was supported by Academy of Finland grant no. 285894.
MR was supported by an NSERC DG grant, the CRC program and a Sloan Fellow-
ship. TT was supported by a Simons Investigator grant, the James and Carol Collins
Chair, the Mathematical Analysis & Application Research Fund Endowment, and by

16 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

NSF grant DMS-1266164. Part of this paper was written while the authors were in
residence at MSRI in Spring 2017, which is supported by NSF grant DMS-1440140.

2. Auxiliary results

We collect here some standard results that will be used (mostly) in section 3.
In order to use some tools from graph theory, it is convenient6 to replace the
continuous integral ∫ 2X
X dx in Theorem 1.4 by something more discrete. Given
X, H, deﬁne a (X, H)-family of intervals to be a ﬁnite collection I of intervals
I = [xI, xI + H] of length H contained in [X/10, 10X], such that any pair of intervals
in I are separated by a distance at least 500H; in particular, the intervals in I are
disjoint, and thus the cardinality of I cannot exceed X/H.
We then have

Lemma 2.1 (Discretizing). Let a(n) be a sequence of complex numbers with |a(n)| ≤
1 for all integers n ≥ 1. Let η > 0 and X ≥ H ≥ 1. Suppose that
∫ 2X

X sup
α∈R
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H a(n)e(−αn)

∣
∣
∣
∣
∣ dx ≥ ηHX. (23)

Then there exist an (X, H)-family of intervals I of cardinality ≥ ηX
1000H and real
numbers αI associated to each I ∈ I such that, for all I ∈ I,
∣
∣
∣
∣
∣
∑

n∈I a(n)e(−αIn)

∣
∣
∣
∣
∣ ≥ ηH
2 . (24)

Proof. It follows from (23) and the pigeonhole principle that there exists y ∈ [0, H)
such that ∑

0≤ℓ<X/H
 

sup
α∈R
 ∣
∣
∣
∣
∣
∣
 ∑

ℓH+y<n≤(ℓ+1)H+y a(n)e(−αn)
 ∣
∣
∣
∣
∣
∣


 ≥ ηX (25)

Given 0 ≤ v < 500, let Iv be the sub-collection of intervals I = ((500ℓ + v)H +
y, (500ℓ + v + 1)H + y] with X
500H ≤ ℓ ≤ X
250H for which

sup
α∈R
 ∣
∣
∣
∣
∣
∣
 ∑

(500ℓ+v)H+y<n≤(500ℓ+v+1)H+y a(n)e(−αn)

∣
∣
∣
∣
∣
∣ ≥ ηH
2 .

6It should also be possible to work in a purely continuous setting, replacing various summations in
our arguments with appropriately normalized integrals, using Fubini’s theorem in place of double
counting arguments, allowing the intervals under consideration to overlap each other, and with
various graph-theoretic inequalities replaced by their continuous counterparts. We leave the details
of this alternate arrangement of the argument to the interested reader.

FOURIER UNIFORMITY 17

Let I = ⋃
0≤v<500 Iv. It follows from (25) and the trivial bound |a(n)| ≤ 1, that

|I| · H ≥ ∑

I∈I
 ∣
∣
∣
∣
∣
∑

n∈I a(n)e(−αn)
∣
∣
∣
∣
∣ ≥ ηX
2 .

Thus there exists an 0 ≤ v < 500 for which Iv is an (X, H)-family of intervals of
cardinality ≥ ηX
1000H . Setting I = Iv, we obtain the claim. □

The frequency αI in the above proposition is not unique: one can shift it by
any integer, and one can also perturb it by up to a small multiple of η/H without
signiﬁcantly aﬀecting (24). However, it turns out that modulo these freedoms, there
are only a bounded number of choices for αI (if one views η as being ﬁxed). More
precisely, one has

Lemma 2.2 (Maximal large sieve). Let H ≥ 1 and let I be an interval of length 10H.
Let η > 0 be given. Let |a(n)| ≤ 1 be a sequence of complex numbers. Suppose that
there exist J ≥ 1, frequencies α1, α2, . . . , αJ ∈ R and sub-intervals I1, I2, . . . , IJ ⊂ I
of length at most H such that
∣
∣
∣
∣
∣
∣
∑

n∈Ij a(n)e(−αjn)

∣
∣
∣
∣
∣
∣ ≥ ηH

for all j = 1, . . . , J. Assume H suﬃciently large depending on η. Then there exist
a natural number K ≤ Cη−2 with C an absolute constant and frequencies β1, . . . , βK
depending only on η > 0, the sequence {a(·)} and the interval I, such that, for each
1 ≤ j ≤ J, there exists k ∈ {1, . . . , K} with

∥αj − βk∥ ≤ 1
H

where we recall that ∥x∥ = dist(x, Z).

Proof. Let γ1 be the frequency γ that maximizes the quantity

sup
L⊂I
 ∣
∣
∣
∣
∣
∑

n∈L a(n)e(−γn)
∣
∣
∣
∣
∣ . (26)

with the supremum taken over all sub-intervals L of I. For i ≥ 2 we deﬁne γi
inductively as the frequency that maximizes (26) in the region [0, 1]\ ⋃i−1
j=1[γj − 1
H , γj +
1
H ]. We thus obtain frequencies γ1, . . . , γR with R a parameter to be chosen later,
and moreover ∥γi − γj∥ > 1
H for i ̸= j.

18 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Using the Carleson-Hunt theorem, it was proven by Montgomery [28, Theorem 2]
that one has the maximal large sieve inequality
7

R∑

r=1 sup
L⊂I
 ∣
∣
∣
∣
∣
∑

n∈L a(n)e(−γrn)

∣
∣
∣
∣
∣
2 ≤ C(R + H) ∑

n∈I |a(n)|
2

with C an absolute constant. The right-hand side is O(H(R + H)). Choosing R to
be a large multiple of η−2, it follows that there are at most K ≪ η−2 frequencies γi
for which
 sup
L⊂I
 ∣
∣
∣
∣
∣
∣
∑

n∈Ij a(n)e(−γrn)
∣
∣
∣
∣
∣
∣ ≥ ηH.

Therefore for any α lying outside of

K⋃

i=1
 [γi − 1
H , γi + 1
H
 ]

we have
 sup
L⊂I
 ∣
∣
∣
∣
∣
∑

n∈L a(n)e(−αn)

∣
∣
∣
∣
∣ < ηH.

Our assumption is that for each αj with 1 ≤ j ≤ J there exists an interval Ij with
Ij ⊂ I for which ∣
∣
∣
∣
∣
∣
∑

n∈Ij a(n)e(−αjn)

∣
∣
∣
∣
∣
∣ ≥ ηH

Therefore α1, . . . , αJ ∈ ⋃K
i=1[γi − 1
H , γi + 1
H ] and the claim follows. □

We record also the following variant of the large sieve that we will need in Section
5.

Lemma 2.3 (Variant of large sieve). Let 1 ≤ H ≤ X and R ∈ N. Let x1, . . . , xR ∈
[1, X] be H-separated (thus |xi − xj| ≥ H for all 1 ≤ i < j ≤ R). Then

∫

|t|≤X/H
 ∣
∣
∣
∣
∣
 R∑

n=1 e(it log xn)
∣
∣
∣
∣
∣
2
 dt ≪ R · X
H . (27)

7At the cost of worsening the dependence on η slightly, one could also use the standard large
sieve inequality [27] here, combined with Lemma 2.4 below.

FOURIER UNIFORMITY 19

Proof. Let Φ(t) be a smooth function such that Φ(t) ≥ 1 for |t| ≤ 1 and with
supp ̂Φ ⊂ (−1, 1). Then the left-hand side of (27) is

≪ ∫

R
 ∣
∣
∣
∣
∣
 R∑

n=1 e(it log xn)

∣
∣
∣
∣
∣
2
 · Φ ( tH
X
 ) dt = X
H
 ∑

1≤m,n≤R ̂Φ ( X
H log xn
xm
 ) ≪ R · X
H

as claimed. □

We will also need the following tool from harmonic analysis.

Lemma 2.4 (Completion of sums). There exists an absolute constant η0 > 0 such
that the following holds. Let J be an interval of length H and a(n) complex coeﬃcients
with |a(n)| ≤ 1 for all integers n ≥ 1. Let I be an interval with I ⊂ J. Suppose that
η ∈ (0, η0) and α ∈ R are such that
∣
∣
∣
∣
∣
∑

n∈I a(n)e(−αn)
∣
∣
∣
∣
∣ > ηH.

Then there exists θ ∈ R such that |θ| ≤ 1
η2H and
∣
∣
∣
∣
∣
∑

n∈J a(n)e(−(α + θ)n)

∣
∣
∣
∣
∣ > η4H.

Proof. Let y, z ∈ R be chosen so that I = [y, z]. Let f be a smooth function with
f (n) = 1 for n ∈ I , |f (n)| ≤ 1 for all integers n, and compactly supported in
[y − η
100 · H, z + η
100 · H]. Moreover we can ensure that f is a Schwartz function with
|f (j)(x)| ≪j (ηH)
−j for all x ∈ R and therefore with | ̂f (x)| = | ∫

R f (u)e(−xu)du| ≪A
H(1 + ηH|x|)
−A for all A ∈ N. Let

g(β) := ∑

n f (n)e(nβ).

Applying Poisson summation to g(β) and using the above bound on ̂f we see that
∫

1− 1
η2H >|β|> 1
η2H |g(β)|
2dβ = ∫

1− 1
η2H >|β|> 1
η2H
 ∣
∣
∣
∣
∣
∑

m ̂f (m + β)
∣
∣
∣
∣
∣
2 dβ ≪ Hη4. (28)

Moreover by construction of g,

ηH ≤
 ∣
∣
∣
∣
∣
∑

n∈I a(n)e(−αn)

∣
∣
∣
∣
∣ ≤
 ∣
∣
∣
∣
∣
∫

T
 (
∑

n∈J a(n)e(−(α + β)n)

)
 g(β)dβ
∣
∣
∣
∣
∣ + η
100 · H.

We split the integral on the right-hand side into two parts, namely |β| ≤ 1
η2H and
the complement. We estimate the part over |β| < 1
η2H trivially only using the bound

20 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

|g(β)| < 2H. On the second part we apply Cauchy-Schwarz, Plancherel and (28) to
see that it is bounded by ≪ η2H. Collecting these estimates we conclude that

ηH < 4H ∫

|β|< 1
η2H
 ∣
∣
∣
∣
∣
∑

n∈J a(n)e(−(α + β)n)

∣
∣
∣
∣
∣ dβ

Therefore there exists β ∈ R such that |β| < 1
η2H and
∣
∣
∣
∣
∣
∑

n∈J a(n)e(−(α + β)n)

∣
∣
∣
∣
∣ > η4H

as needed. □

In section 3 we will frequently relate the Fourier behavior of f on an interval I
with the behavior on dilated intervals I/p for various primes p. The key tool here is

Proposition 2.5 (Mean scales down). Let x ≥ H ≥ 1, and let f : (x, x + H] → C
obey the bound ∑

n∈(x,x+H] |f (n)|
2 ≪ H

(thus f = O(1) on average on (x, x + H] in an L
2 sense). Then

∑

p≤H p ·
 ∣
∣
∣
∣
∣
∣
∣
 ∑

m∈( x
p , x+H
p ] f (pm) − 1
p
 ∑

n∈(x,x+H] f (n)

∣
∣
∣
∣
∣
∣
∣
2
 ≪ H 2. (29)

In particular, by Markov’s inequality, for any δ > 0 we have
∑

m∈( x
p , x+H
p ] f (pm) = 1
p
 ∑

n∈(x,x+H] f (n) + O (δ H
p
 )

for all primes p ≤ H outside of an exceptional set P of primes with ∑

p∈P 1
p ≪ δ−2.

Proof. See [6, Lemma 4.7]. □

We will also need the following number-theoretic estimate, in particular to dispose
of some degenerate cases.

Lemma 2.6 (Counting nearby products of primes). Let k ∈ N and P ′, N ≥ 3 be
such that (P ′)
k−1 ≫ N . Write d = P ′2/(log P ′)2. Then the number of 2k-tuples
(p′
1,1, . . . , p′
1,k, p
′
2,1, . . . , p′
2,k) of primes in [P ′, 2P ′] obeying the condition
∣
∣
∣
∣
∣
 k∏

j=1 p′
2,j −
 k∏

j=1 p′
1,j
∣
∣
∣
∣
∣ ≤ C · (P ′)
k

N (30)

FOURIER UNIFORMITY 21

with C > 0 a constant, is at most Ok,C( (P ′)2k

N log2k P ′ ) = Ok,C( dk
N ).
If we also impose the additional condition

k∏

j=1 p′
2,j =
 k∏

j=1 p′
1,j mod q (31)

for some modulus q ∈ N, then the number of tuples is bounded by

Ok,C
 ( d
k

N
 ( 1
ϕ(q) + 1
log N
 )) .

Proof. Since the ﬁrst claim follows from the second by specializing to q = 1 it is
enough to prove the second claim.
First notice that without loss of generality we can assume that q ≤ (log N )3k since
otherwise the claim is trivial by replacing products of primes by integers (i.e., using
the crude bound that every integer has at most Ok(1) representations as a product
of k primes) and counting trivially.
Let w be a smooth function such that w(x) = 1 for |x| ≤ 100C. Then, the number
of primes p′
1,j, p
′
2,ℓ for which (30) and (31) hold is

≪ ∑

p′
1,1,...,p′
1,k∈[P ′,2P ′]
p′
2,1,...,p′
2,k∈[P ′,2P ′]
p′
1,1...p′
1,k≡p′
2,1...p′
2,k mod q
 w
 (
N log p′
1,1 . . . p
′
1,k
p′
2,1 . . . p′
2,k
 )
 (32)

Since q < P ′ and all of the p′
1,j, p
′
2,ℓ are primes, we can express the congruence
condition using Dirichlet characters, thus

1p′
1,1...p′
1,k≡p′
2,1...p′
2,k mod q = 1
ϕ(q)
 ∑

χ (mod q) χ(p′
1,1) . . . χ(p′
1,k)χ(p′
2,1) . . . χ(p′
2,k)

where the sum is over all Dirichlet characters of period q. Using this identity and
the Fourier inversion formula w(x) = ∫

R ̂w(t)e2πixtdt, we see that the expression (32)
is equal to
 1
ϕ(q)N
 ∑

χ (mod q)
 ∫

R ̂w ( t
N
 ) ·
 ∣
∣
∣
∣
∣
∣
 ∑

p∈[P ′,2P ′] pitχ(p)

∣
∣
∣
∣
∣
∣
2k
 dt,

Since q ≤ (log N )3k ≪k (log P ′)3k, the zero-free region for L(s, χ) gives
∑

p∈[P ′,2P ′] pitχ(p) ≪ P ′

log P ′ · 1
1 + |t| · δχ=χ0 + P ′ exp(−(log P ′)
1/100);

22 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

see for instance [21, Lemma 2.4]. Using this pointwise estimate it follows that

1
ϕ(q)N
 ∑

χ (mod q)
 ∫

|t|≪exp((log P ′)1/100)
 ∣
∣
∣
∣
∣
∣
 ∑

p∈[P ′,2P ′] pitχ(p)

∣
∣
∣
∣
∣
∣
2k
 dt ≪ 1
ϕ(q)N P ′2k

(log P ′)2k = d
k

ϕ(q)N .

To bound the part of the integral with large |t| we notice that for arbitrary coeﬃcients
a(n), we have the L
2 mean value theorem
∫

R ̂w ( t
N
 ) ·
 ∣
∣
∣
∣
∣
 ∑

A≤n≤B a(n)nit∣
∣
∣
∣
∣
2 ≪ (N + B) ∑

A≤n≤B |a(n)|
2 (33)

(see e.g., [17, Theorem 9.1]), while from the pointwise estimate we have

1
ϕ(q)N
 ∑

χ (mod q)
 ∫

|t|≫exp((log P ′)1/100) ̂w ( t
N
 ) ∣
∣
∣
∣
∣
∣
 ∑

p∈[P ′,2P ′] pitχ(p)

∣
∣
∣
∣
∣
∣
2k
 dt

≪P ′2 exp(−(log P ′)
1/100) · sup
χ (mod q)
 1
N
 ∫

R ̂w ( t
N
 ) ∣
∣
∣
∣
∣
∣
 ∑

p∈[P ′,2P ′] pitχ(p)

∣
∣
∣
∣
∣
∣
2k−2
 dt

Since ∣
∣
∣
∣
∣
∣
 ∑

p∈[P ′,2P ′] pitχ(p)

∣
∣
∣
∣
∣
∣
2k−2
 =
 ∣
∣
∣
∣
∣
∣
 ∑

n∈[(P ′)k−1,(2P ′)k−1] a(n)n
it
∣
∣
∣
∣
∣
∣
2

where a(n) := χ(n) ∑

p1,...,pk−1∈[P ′,2P ′]:n=p1...pk−1 1 = Ok(1)

we may thus bound the part of the integral with |t| > exp((log P ′)
1/100) using (33)
by
 ≪k P ′2 exp(−(log P ′)
1/100) · 1
N · (N + P ′k−1)P ′k−1 ≪k P ′2k

N exp(−(log P ′)
1/100)

as required. Combining the two bounds, the claim follows. □

3. Intervals and frequencies

Assume we have the hypotheses of Theorem 1.4, thus there exists an η > 0 such
that ∫ 2X

X sup
α
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H f (n)e(−αn)

∣
∣
∣
∣
∣ dx ≥ ηXH.

FOURIER UNIFORMITY 23

Informally speaking, the main purpose of this section is to produce a large set I ′′ of
disjoint intervals I ′′, each of length comparable to some quantity L (which will be
slightly shorter than H), as well as associated frequencies α′′
I ′′ with
∣
∣
∣
∣
∣
 ∑

n∈I ′′ f (n)e(−α′′
I ′′n)

∣
∣
∣
∣
∣ ≫η L,

and a scale P ′ with the following property: For a positive proportion of quadruples
(I ′′, J ′′, p
′, q′) ∈ I 2 × [P ′, 2P ′]2 with p′, q′ prime such that I ′′ is close to p′

q′ J ′′ we have

q′

p′′ α′′
I ′′ ≈ p′

p′′ α′′
J ′′ (mod 1)

for a positive proportion of primes p′′ in some range [P ′′/2, P ′′] (compare with (12)).
Moreover the ranges P ′′, P ′, L are all related by log P ′′ ≍ log P ′ ≍ log L and L ≍
H/P ′P ′′. This is the content of Proposition 3.2 below. We ﬁrst need a preliminary
proposition.

Proposition 3.1 (Scaling down). Let 1 ≤ P ≤ Q ≤ H ≤ X and η > 0, and
let f : N → C be a 1-bounded multiplicative function. Assume that P and log Q
log P are
suﬃciently large depending on η. Suppose that there exist an (X, H)-family I of
intervals of cardinality ≫η X/H and a real number αI associated to each I ∈ I such
that ∣
∣
∣
∣
∣
∑

n∈I f (n)e(−αIn)

∣
∣
∣
∣
∣ ≫η H (34)

for all I ∈ I. Then there exist P ′ ∈ [P, Q/2], an ( X
P ′ , H
P ′ )-family I ′ of intervals of
cardinality ≫η X/H, and a real number α′
I ′ associated to each I ′ ∈ I ′, such that
∣
∣
∣
∣
∣
∑

n∈I ′ f (n)e(−α′
I ′n)

∣
∣
∣
∣
∣ ≫η H
P ′

for all I ′ ∈ I ′. Furthermore, for each I ′ ∈ I ′, one can ﬁnd ≫η P ′
log P ′ pairs (I, p′),
where I is an interval in I and p′ is a prime in [P ′, 2P ′], such that I/p
′ lies within
3 H
P ′ of I ′, and such that
 p′αI = α′
I ′ + Oη
 ( P ′

H
 ) mod 1.

The conclusions of Proposition 3.1 are depicted schematically in Figure 6.

24 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Figure 6. A depiction of Proposition 3.1; the frequencies p′αI and
α′
I ′ will be close modulo integers, and each I ′ ∈ I ′ will be associated
to many pairs (I, p′) in this fashion. Compare this with Figure 2.

Proof. For each I ∈ I, we apply Proposition 2.5 to the function n ↦→ f (n)e(−αIn)
on I, and with δ suﬃciently small depending on η, to conclude that
∣
∣
∣
∣
∣
∣
 ∑

n∈I/p′ f (np
′)e(−αInp
′)
∣
∣
∣
∣
∣
∣ ≫η H
P ′ (35)

for all primes p′ ∈ [P, Q] outside of an exceptional set PI with
∑

p′∈PI
 1
p′ ≪η 1.

Summing over all I ∈ I (recalling that this collection of intervals has cardinality at
most X/H), we conclude ∑

P ≤p′≤Q
 1
p′ #{I ∈ I : p′ ∈ PI} ≪η X
H .

From Mertens’ theorem and the pigeonhole principle, we may thus ﬁnd P ′ ∈ [P, Q/2]
such that ∑

p′∈[P ′,2P ′] #{I ∈ I : p′ ∈ PI} ≪η X
H log log Q
log P
 P ′

log P ′ .

Fix this quantity P ′. If log Q
log P is large enough, we conclude from the prime number
theorem that ∑

p′∈[P ′,2P ′] #{I ∈ I : p′ ̸∈ PI} ≫η X
H P ′

log P ′ ,

and thus we have (35) for ≫η X
H P ′
log P ′ pairs (I, p′) with I ∈ I and p′ ∈ [P ′, 2P ′].

FOURIER UNIFORMITY 25

As f is multiplicative, we have f (np
′) = f (n)f (p′) unless n is a multiple of p′. The
latter contributes at most O( H
p′P ) to the left-hand side of (35), which is negligible
compared to the right-hand side as P (and hence p′) is large. Thus we may freely
replace f (np
′) by f (n)f (p′), and conclude that
∣
∣
∣
∣
∣
∣
 ∑

n∈I/p′ f (n)e(−αInp′)

∣
∣
∣
∣
∣
∣ ≫η H
P ′ (36)

for ≫η X
H P ′
log P ′ pairs (I, p′). (Compare with Figure 2.)
Let S denote the collection of these pairs (I, p′), and let I1 denote the collection
of all intervals of the form I/p
′ where (I, p′) ∈ S. These are intervals in [0, 10X/P ′]
of length between H/2P ′ and H/P ′. By a simple greedy algorithm, we may ﬁnd
a subfamily I2 of these intervals which are separated by distance at least 2H/P ′,
with the property that every interval in I1 lies within a distance 3H/P ′ of one of the
intervals in I2.
By (36) and Lemma 2.2, we can associate to each interval I ′ ∈ I2 some real
numbers βI ′,1, . . . , βI ′,K(I ′) for some K(I ′) ≪η 1, with the property that, for each
pair (I, p′) ∈ S with I/p
′ within 3H/P ′ of I ′, one has

p′αI = βI ′,k + Oη
 ( P ′

H
 ) mod 1

for some 1 ≤ k ≤ K(I ′). By adding dummy values of β if necessary we may take
K = K(I ′) independent of I ′. By the pigeonhole principle, we may ﬁnd 1 ≤ k0 ≤ K
such that one has
 p′αI = βI ′,k0 + Oη
 ( P ′

H
 ) mod 1 (37)

for ≫η X
H P ′
log P ′ triples (I, p′, I ′) with (I, p′) ∈ S and I ′ ∈ I2 with 1
p′ I within distance
3 H
P ′ of I ′. If we let T be the collection of such triples, then one can ﬁnd a subset I3
of I2 of cardinality ≫η X
H with the property that for each I ′ ∈ I3, there are ≫η P ′
log P ′
pairs (I, p′) ∈ S with (I, p′, I ′) ∈ T .
For I ′ ∈ I3, pick one of the pairs (I(I ′), p
′(I ′)) ∈ S with (I(I ′), p
′(I ′), I ′) ∈ T , then
from (36) we have ∣
∣
∣
∣
∣
∣
∣
 ∑

n∈ 1
p′(I′) I(I ′) f (n)e(−αI(I ′)np
′(I ′))

∣
∣
∣
∣
∣
∣
∣ ≫η H
P ′ (38)

26 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

while from (37) we have

p′αI = p′(I ′)αI(I ′) + Oη
 (P ′

H
 ) mod 1

whenever (I, p′) ∈ S with (I, p′, I ′) ∈ T .
The interval I(I ′)/p
′(I ′) lies in [0, 10X/P ′] with length between H/2P ′ and H/P ′.
Let J(I ′) be an interval in [0, 10X/P ′] of length exactly H/P ′ containing I(I ′)/p
′(I ′).
By Lemma 2.4 and (38), we have
∣
∣
∣
∣
∣
∣
 ∑

n∈J(I ′) f (n)e(−α′
J(I ′)n)

∣
∣
∣
∣
∣
∣ ≫η H
P ′

for some real number
 α′
J(I ′) = p′(I ′)αI(I ′) + Oη
 ( P ′

H
 ) .

In particular
 p′αI = α′
J(I ′) + Oη
 (P ′

H
 ) mod 1

whenever (I, p′) ∈ S with (I, p′, I ′) ∈ T .
Setting I ′ to be a 500H/P ′-separated collection of ≫ X/H intervals of the form
J(I ′) with I ′ ∈ I3, we obtain the claim. □

We are now ready to prove the main result of this section.

Proposition 3.2. Let X ≥ 2, θ ∈ (0, 1), η > 0, and ρ ∈ (0, 1/8). Let f : N → C be
a multiplicative function with |f | ≤ 1. Suppose that, for H = X θ, we have
∫ 2X

X sup
α
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H f (n)e(−αn)

∣
∣
∣
∣
∣ dx ≥ ηHX.

Let ε ∈ (0, ρ/100) be suﬃciently small depending on θ and η, and assume X is
suﬃciently large depending on θ, η, ρ, and ε. Then there exist P ′, P ′′ ∈ [X ε2, X ε],
an ( X
P ′P ′′ , H
P ′P ′′ )-family I ′′ of intervals of cardinality ≫ X/H, and a real number α′′
I ′′
associated to each I ′′ ∈ I ′′ such that
∣
∣
∣
∣
∣
 ∑

n∈I ′′ f (n)e(−α′′
I ′′n)
∣
∣
∣
∣
∣ ≫η H
P ′P ′′

for all I ′′ ∈ I ′′. Furthermore, there exist ≫η ( P ′
log P ′ )2 X
H quadruples (I ′′
1 , I ′′
2 , p
′
1, p
′
2) with
I ′′
1 , I ′′
2 distinct intervals in I ′′ and p′
1, p
′
2 distinct primes in [P ′, 2P ′], such that I ′′
1 lies

FOURIER UNIFORMITY 27

within 50 H
P ′P ′′ of p′
2
p′
1 I ′′
2 , and such that

p′
2α′′
I ′′
1 − p′
1α′′
I ′′
2 = Oη
 ( (P ′)
2P ′′

H
 ) mod p′′ (39)

for ≫η P ′′
log P ′′ primes p′′ ∈ [P ′′/2, P ′′].

Proof. By Lemma 2.1, one can ﬁnd (X, H)-family I of intervals of cardinality ≫
ηX/H and a real number αI associated to each I ∈ I such that
∣
∣
∣
∣
∣
∑

n∈I f (n)e(−αIn)
∣
∣
∣
∣
∣ ≫ ηH

for all I ∈ I. Applying Proposition 3.1, one can ﬁnd P ′ ∈ [X ε2, X ε], an ( X
P ′ , H
P ′ )-
family I ′ of intervals of cardinality ≫η X/H, and a real number α′
I ′ associated to
each I ′ ∈ I ′, such that ∣
∣
∣
∣
∣
∑

n∈I ′ f (n)e(−α′
I ′n)
∣
∣
∣
∣
∣ ≫η H
P ′

for all I ′ ∈ I ′. Furthermore, for each I ′ ∈ I ′, one can ﬁnd ≫η P ′
log P ′ pairs (I, p′),
where I is an interval in I and p′ is a prime in [P ′, 2P ′], such that I/p
′ lies within
3 H
P ′ of I ′ and
 p′αI = α′
I ′ + Oη
 ( P ′

H
 ) mod 1.

By a second application of Proposition 3.1, one can ﬁnd P ′′ ∈ [(X/P ′)
ε2, (X/P ′)
ε],
an ( X
P ′P ′′ , H
P ′P ′′ )-family I ′′ of intervals of cardinality ≫η X/H, and a real number α′′
I ′′
associated to each I ′′ ∈ I ′′, such that
∣
∣
∣
∣
∣
 ∑

n∈I ′′ f (n)e(−α′′
I ′′n)
∣
∣
∣
∣
∣ ≫η H
P ′P ′′ (40)

for all I ′′ ∈ I ′′. Furthermore, for each I ′′ ∈ I ′′, one can ﬁnd ≫η P ′′
log P ′′ pairs (I ′, p
′′),
where I ′ is an interval in I ′ and p′′ is a prime in [P ′′/2, P ′′], such that I ′/p
′′ lies
within 3 H
P ′P ′′ of I ′′, and such that

p′′α′
I ′ = α′′
I ′′ + Oη
 ( P ′P ′′

H
 ) mod 1. (41)

Also, since the I ′ are 500H-separated, we see that each prime p′′ is associated to at
most one I ′ in this fashion (for a ﬁxed choice of I ′′). The above situation is depicted
in Figure 7.

28 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Figure 7. The relationship between the intervals I, I ′, I ′′, primes
p′, p
′′, and frequencies αI, α′
I ′, α′′
I ′′.

Note that if I ′′ ∈ I ′′, then one can add an arbitrary integer to each real number α′′
I ′′
without aﬀecting any of the above properties. In particular, if one adds an integer
with an appropriate residue class mod p′′, one can upgrade (41) to

p′′α′
I ′ = α′′
I ′′ + Oη
 ( P ′P ′′

H
 ) mod p′′ (42)

for any pair (I ′, p
′′) appearing previously. By the Chinese remainder theorem, we
may thus select α′′
I ′′ so that (42) holds for all pairs (I ′, p
′′) appearing previously.
Combining the above properties, we see that we can ﬁnd ≫η P ′
log P ′ P ′′
log P ′′ X
H quintu-
plets (I, I ′, I ′′, p
′, p
′′), where I ∈ I, I ′ ∈ I ′, I ′′ ∈ I ′′, p′ is a prime in [P ′, 2P ′], p′′ is
a prime in [P ′′/2, P ′′], 1
p′ I lies within 3 H
P ′ of I ′, 1
p′′ I ′ lies within 3 H
P ′P ′′ of I ′′, and one
has the equations
 p′αI = α′
I ′ + Oη
 ( P ′

H
 ) mod 1

and
 p′′α′
I ′ = α′′
I ′′ + Oη
 ( P ′P ′′

H
 ) mod p′′.

FOURIER UNIFORMITY 29

Multiplying the ﬁrst equation by p′′ and combining with the second equation, we
conclude in particular that

p′p′′αI = α′′
I ′′ + Oη
 ( P ′P ′′

H
 ) mod p′′.

The number of possible choices for (I, p′′) is (trivially) at most P ′′
log P ′′ X
H . Applying
the Cauchy-Schwarz inequality, we conclude that we can ﬁnd ≫η ( P ′
log P ′ )
2 P ′′
log P ′′ X
H
octuplets (I, I ′
1, I ′
2, I ′′
1 , I ′′
2 , p
′
1, p
′
2, p
′′), where
• I ∈ I, I ′
1, I ′
2 ∈ I ′, I ′′
1 , I ′′
2 ∈ I ′′;
• p′
1, p
′
2 are primes in [P ′, 2P ′], and p′′ is a prime in [P ′′/2, P ′′];
• For i = 1, 2, 1
p′
i I lies within 3 H
P ′ of I ′
i, and 1
p′′ I ′
i lies within 3 H
P ′P ′′ of I ′′
i .
• We have
 p′
1p′′αI = α′′
I ′′
1 + Oη
 ( P ′P ′′

H
 ) mod p′′ (43)

and
 p′
2p′′αI = α′′
I ′′
2 + Oη
 ( P ′P ′′

H
 ) mod p′′. (44)

See Figure 8.
Multiplying (43) by p′
2 and (44) by p′
1 and then subtracting, we see that

p′
2α′′
I ′′
1 − p′
1α′′
I ′′
2 = Oη
 ((P ′)
2P ′′

H
 ) mod p′′. (45)

Also, p′
1I ′
1 lies within 6H of p′
1p′′I ′′
1 and p′
2I ′
2 lies within 6H of p′
2p′′I ′′
2 , so by the triangle
inequality p′
1p′′I ′′
1 and p′
2p′′I ′′
2 lie at distance at most 24H from each other. Hence,
on dividing by p′
1p′′, I ′′
1 and p′
2
p′
1 I ′′
2 lie at distance at most 48 H
P ′P ′′ from each other. In
particular, if p′
1 = p′
2, then I ′′
1 = I ′′
2 , and similarly I ′
1 = I ′
2. As a consequence, the
number of octuplets with this property is at most O( P ′
log P ′ P ′′
log P ′′ X
H ). Since P ′ ≥ X ε2

and X is suﬃciently large depending on ε, the contribution of this case is thus
negligible, so that there are ≫η ( P ′
log P ′ )
2 P ′′
log P ′′ X
H octuplets (I, I ′
1, I ′
2, I ′′
1 , I ′′
2 , p
′
1, p
′
2, p
′′)
with p′
1 ̸= p′
2.
Observe that if I ′′
1 , I ′′
2 , p
′
1, p
′
2 are ﬁxed, then I, I ′
1, I ′
2 are completely determined by
p′′ thanks to the separation properties of I and I ′′; in particular, there are O( P ′′
log P ′′ )
ways to complete the quadruplet (I ′′
1 , I ′′
2 , p
′
1, p
′
2) to an octuplet. Similarly, I ′′
1 is com-
pletely determined by I ′′
2 , p
′
1, p
′
2 (since there is at most one interval in I ′′ that lies
within 48 H
P ′P ′′ from p′
2
p′
1 I ′′
2 ). Thus the number of eligible quadruplets (I ′′
1 , I ′′
2 , p
′
1, p
′
2) is

O(( P ′
log P ′ )
2 X
H ). We conclude that there exist ≫η ( P ′
log P ′ )
2 X
H quadruplets (I ′′
1 , I ′′
2 , p
′
1, p
′
2),
each of which can be completed to an octuplet in ≫η P ′′
log P ′′ ways. In particular, for

30 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Figure 8. The relationship between the intervals I, I ′
1, I ′
2, I ′′
1 , I ′′
2 ,
primes p′
1, p
′′
2, p
′′, and frequencies αI, α′′
I ′′
1 , α′′
I ′′
2 . Some frequencies are
omitted from the ﬁgure to reduce clutter. If this situation occurs for
many values of p′′, we draw a dashed line from I ′′
1 to I ′′
2 labeled by
p′
1/p
′
2. Compare with Figure 4.

such a quadruplet, (45) holds for ≫η P ′′
log P ′′ choices of p′′ (recalling that I, I ′
1, I ′
2 are
completely determined by the remaining coeﬃcients of the octuplet). The claim
follows. □

4. Local structure of α′′

We now analyse the structure of the function α′′ appearing in Proposition 3.2.
The main result of this section asserts that α′′
I ′′ locally behaves like T
xI′′ with T “not
too large” (and up to a shift a
q with small denominator), where xI ′′ denotes the left
endpoint of the interval I ′′. Crucially, T will not vary much with I ′′, at least “locally”.
It is here that we will rely on the hypothesis H = X θ that H is of polynomial size
in X.

Proposition 4.1. Let θ, η, ρ, X, H, f, ε, P ′, P ′′, I ′′, α′′ be as in Proposition 3.2. Then,

for ≫ε X
H ( P ′
log P ′ )2 of the pairs (I ′′
1 , I ′′
2 ) of intervals in (I ′′)
2, there exist a natural

FOURIER UNIFORMITY 31

number 1 ≤ q ≪ H ρ,
integers a1, a2, a real number
 T ≪θ,η,ε,ρ X 2

H 2−ρ ,

and a set P(I ′′
1 , I ′′
2 ) of primes in [P ′′/2, P ′′] of cardinality ≫θ,η,ε,ρ P ′′
log P ′′ such that

α′′
I ′′
j = T
xI ′′
j + aj
q
 ∏

p′′∈P(I ′′
1 ,I ′′
2 ) p′′ + Oθ,η,ε,ρ
 ( 1
H 1−ρ
 ) mod ∏

p′′∈P(I ′′
1 ,I ′′
2 ) p′′

for j = 1, 2. Furthermore, for each such pair, there exist primes p′
1, p
′
2 ∈ [P ′, 2P ′]
such that I ′′
1 lies within 100 H
P ′P ′′ of p′
2
p′
1 I ′′
2 , and such that

p′
2a1 = p′
1a2 mod q. (46)

Proof. Let θ, η, ρ, X, H, f, ε, P ′, P ′′, I ′′, α′′ be as in Proposition 3.2. Thus for instance
we now have P ′′, P ′ ≤ H ρ/100. Henceforth we allow implied constants to depend on
θ, η, ε, ρ. We abbreviate
 N := #I ′′ ≍ X
H
for the cardinality of I ′′ and d for the quantity

d := ( P ′

log P ′
 )2 ,

thus the number of quadruples (I ′′
1 , I ′′
2 , p
′
1, p
′
2) in Proposition 3.2 is ≫ dN . We con-
struct a graph G = (V, E) whose vertices are just the intervals in I ′′ (thus V = I ′′

has N vertices), and the edges e are those unordered pairs e = {I ′′
1 , I ′′
2 } for which
there exist distinct primes p′
1, p
′
2 in [P ′, 2P ′] such that p′
1I ′′
1 lies within 100 H
P ′′ of p′
2I ′′
2 ,
and such that
 p′
2α′′
I ′′
1 − p′
1α′′
I ′′
2 = Oη
 ( (P ′)
2P ′′

H
 ) mod p′′ (47)

for a set P(e) of primes p′′ in [P ′′/2, P ′′] of cardinality ≫ P ′′
log P ′′ (note that these
properties are symmetric in I ′′
1 and I ′′
2 ). Observe that the primes p′
1, p
′
2 are uniquely
determined by I ′′
1 , I ′′
2 , for if there was another pair of primes p′
3, p
′
4 with the same
properties, then p′
2
p′
1 I ′′
2 and p′
4
p′
3 I ′′
2 would lie within 200 H
P ′P ′′ of each other, which implies
that p′
2
p′
1 − p′
4
p′
3 = O ( H
X
 ) ,

but if (p′
1, p
′
2) ̸= (p′
3, p
′
4) then the left-hand side has magnitude at least 1
p′
3p′
1 ≫ X −2ε2,
which leads to a contradiction if ε is small enough and X is large enough. Thus, by

32 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Proposition 3.2, we see that the number of edges in G is ≫ dN . On the other hand,
the degree of each vertex in G is O(d), since for ﬁxed I ′′
1 there are only O(d) choices
for p′
1 and p′
2, and I ′′
2 is uniquely determined by these choices. Thus G has ≍ dN
edges and the mean degree of G is ≍ d.
At present, the sets P(e) of primes associated to each edge e are large, but the
intersections P(e1) ∩ · · · ∩ P(ek) could be small. This will cause diﬃculties later.
To get around this problem we use a random reﬁnement trick of Gowers [8]. Let p′′

be a prime in [P ′′/2, P ′′] selected uniformly at random, and let G = (V, E) be the
subgraph of G consisting of the same vertex set V as G, and with the edge set E
consisting of all edges e ∈ E with P(e) containing p. By the prime number theorem,
each edge has probability ≫ 1 of lying in G, so by linearity of expectation the
expected number of edges in G is ≫ dN . In particular, we see that with probability
≫ 1, the random graph G has ≫ dN edges. Of course, G has maximum degree
O(d) since it is a subgraph of G. As we shall see later, the advantage of working with
G instead of G is that the intersections P(e1) ∩ · · · ∩ P(ek) have a high probability
of being large when e1, . . . , ek are all constrained to lie in G.
If A is the adjacency matrix of G, then by the preceding discussion we have
1
T A1 ≫ dN (where 1 denotes the all-ones column vector) with probability ≫ 1.
By the Blakley-Roy inequality [2], we now see that for any natural number k, we
have 1
T Ak1 ≫k dkN with probability ≫ 1. That is to say, with probability ≫ 1,
the number of (k + 1)-tuples (I ′′
0 , . . . , I ′′
k ) in V k+1 such that {I ′′
j , I ′′
j+1} ∈ E for j =
0, . . . , k − 1 is ≫k dkN .
Now let k be the ﬁrst even integer for which

dk ≥ N 2 · d.

Then (since P ′, P ′′ ≤ X ε) we have k = O(1) and

N 2d ≤ dk ≤ N 2d
3. (48)

In particular, we may allow implied constants to depend
8 on k. From the preceding
discussion, with probability ≫ 1, the number of (k + 2)-tuples

(I ′′
k/2,1, . . . , I ′′
0,1, I ′′
0,2, . . . , I ′′
k/2,2) ∈ V k+2 (49)

such that {I ′′
j,1, I ′′
j+1,1}, {I ′′
j,2, I ′′
j+1,2}, {I ′′
0,1, I ′′
0,2} ∈ E for j = 0, . . . , k/2−1 is ≫ d
k+1N .
This situation is depicted in Figure 9.
The number of possible choices for the quadruplet (I ′′
k/2,1, I ′′
0,1, I ′′
0,2, I ′′
k/2,2) is O(dN 3),
since there are N 3 choices for I ′′
k/2,1, I ′′
0,1, I ′′
k/2,2, and once I ′′
0,1 is ﬁxed there are O(d)
choices for I ′′
0,2. Thus by the Cauchy-Schwarz inequality, with probability ≫ 1, we
have there are ≫ (dk+1N )
2/(dN 3) = d2k+1/N pairs of such tuples with a common

8If one were to extend the arguments here to smaller values of H, one would need to pay more
attention as to the precise dependence of these constants on k.

FOURIER UNIFORMITY 33

Figure 9. A tuple (49) in G with k = 4. Here we discard any
orientation or labeling of the edges of G.

quadruplet (I ′′
k/2,1, I ′′
0,1, I ′′
0,2, I ′′
k/2,2). Relabeling, we conclude
9 that with probability
≫ 1, the number of 2k-tuples
⃗I ′′ := (I ′′
j,i)j∈{0,1,...,k−1};i=1,2 ∈ V 2k (50)

such that {I ′′
j,i, I ′′
j+1,i}, {I ′′
0,1, I ′′
0,2} ∈ E for j = 0, . . . , k − 1, i = 1, 2 is ≫ d
2k+1/N ,
where we adopt the periodic convention I ′′
k,i = I ′′
0,i for i = 1, 2. In particular, by
deﬁnition of G, we have

p ∈ P({I ′′
0,1, I ′′
0,2}) and p ∈ P({I ′′
j,i, I ′′
j+1,i})

for all j = 0, 1, . . . , k − 1 and i = 1, 2. The situation is depicted in Figure 10.
Call the 2k-tuples ⃗I ′′ of the above form good, thus there are ≫ d2k+1/N good
tuples. Given a good tuple, to each edge {I ′′
j,i, I ′′
j+1,i} we have (uniquely determined)

primes p′
1,j,i, p
′
2,j,i in [P ′, 2P ′], such that I ′′
j+1,i lies within 100 H
P ′P ′′ of p′
1,j,i
p′
2,j,i I ′′
j,i for j =
0, 1, . . . , k − 1 and i = 1, 2; we also have primes p′
1, p
′
2 ∈ [P ′, 2P ′] such that I ′′
0,2 lies
within 100 H
P ′P ′′ of p′
1
p′
2 I ′′
0,1. Again, we refer the reader to Figure 10 for a depiction of

9This bound also follows from the work of Sidorenko [30], as the graph consisting of two k-cycles
(with k even) connected by an edge is one of the conﬁrmed cases of Sidorenko’s conjecture.

34 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Figure 10. A tuple (50) in G with k = 4, with the orientation and
labels restored. Compare with Figure 5.

these relationships. Iterating the former claim, we see that I ′′
0,i lies within O( H
P ′P ′′ )

from
 ∏k
j=1 p′
2,j,i
∏k
j=1 p′
1,j,i I ′′
0,i for i = 1, 2, thus
∏k
j=1 p′
2,j,i
∏k
j=1 p′
1,j,i = 1 + O ( H
X
 ) = 1 + Oε,k
 ( 1
N
 ) .

Multiplying out, we conclude that

k∏

j=1 p′
2,j,i −
 k∏

j=1 p′
1,j,i ≪ (P ′)
k

N ≪ε dk/2(log P ′)
k

N ≪ε d2 (51)

thanks to (48).
We now eliminate some degenerate cases. Suppose ∏k
j=1 p′
2,j,1 − ∏k
j=1 p′
1,j,1 = 0.
Then, by the fundamental theorem of arithmetic, the p′
1,j,1 are a permutation of
the p′
2,j,1. By the prime number theorem, the total number of possibilities for the
p′
1,j,1, p
′
2,j,1 is then at most ≪k (P ′/ log P ′)
k ≪ dk/2. By Lemma 2.6, there are
O(d
k/N ) choices for p′
1,j,2, p
′
2,j,2, and ﬁnally there are O(d) possibilities for p′
1, p
′
2
and O(N ) possibilities for I ′′
0,1. All the other I ′′
j,i are uniquely determined by this

FOURIER UNIFORMITY 35

data, so the number of tuples with ∏k
j=1 p′
2,j,1 − ∏k
j=1 p′
1,j,1 = 0 is

≪ dk/2 dk

N dN = d3k/2+1

which is negligible compared to d2k+1/N thanks to (48). Thus there are ≫ d2k+1/N
good tuples for which ∏k
j=1 p′
2,j,1 − ∏k
j=1 p′
1,j,1 does not vanish. Repeating this argu-
ment for ∏k
j=1 p′
2,j,2 − ∏k
j=1 p′
1,j,2, we may see that with probability ≫ 1, there are
≫ d2k+1/N good tuples for which ∏k
j=1 p′
2,j,i − ∏k
j=1 p′
1,j,i ̸= 0 for i = 1, 2. We will
call such good tuples non-degenerate.
Another case we would like to exclude is when the set

P(⃗I ′′) :=
 k⋂

j=1
 ⋂

i=1,2 P({I ′′
j,i, I ′′
j+1,i}) ∩ P({I ′′
0,1, I ′′
0,2})

is unusually small, say
 #P(⃗I ′′) ≤ δ P ′

log P ′ (52)

for some small δ > 0 depending on ε, θ, ρ, η) to be chosen later. Deﬁne a candidate tu-
ple to be a tuple ⃗I ′′ = (I ′′
j,i)j∈{0,1,...,k−1};i=1,2 ∈ V 2k with {I ′′
0,1, I ′′
0,2} ∈ E, {I ′′
j,i, I ′′
j+1,i} ∈
E for j = 0, . . . , k − 1, and i = 1, 2 obeying (52) and with ∏k
j=1 p′
2,j,i − ∏k
j=1 p′
1,j,i
non-vanishing for i = 1, 2. Observe that a tuple ⃗I ′′ is a non-degenerate good tuple
obeying (52) precisely if it is a candidate tuple with p ∈ P(⃗I ′′). In particular, the
probability that a given candidate tuple is actually good is O(δ). On the other hand,
from two applications of Lemma 2.6, the number of candidate tuples is at most

≪ε N × d × (dk

N )
2 = d2k+1/N,

and so, by linearity of expectation, the expected number of good tuples obeying
(52) is O(δd2k+1/N ). On the other hand, with probability ≫ 1 we have ≫ d2k+1/N
non-degenerate good tuples. With X large enough (which makes P ′ large compared
with η, ε, ρ, θ), and setting δ suﬃciently small depending on η, ε, ρ, θ, we thus have
with positive probability that there are ≫ d2k+1/N non-degenerate good tuples ⃗I ′′

for which
 #P(⃗I ′′) > δ P ′

log P ′ . (53)

Let us call such tuples very good, thus we can ﬁnd a deterministic choice of p such
that there are ≫ d2k+1/N very good tuples.
Henceforth p is chosen deterministically as above. Let ⃗I ′′ be a very good tuple,
with attendant primes p′
1,j,i, p
′
2,j,i and p′
1, p
′
2 for j ∈ {0, 1, . . . , k − 1} and i = 1, 2.

36 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

From (47), (53) we see that there is a collection P(⃗I ′′) of primes in [P ′′/2, P ′′] of
cardinality
 #P(⃗I ′′) ≫ P ′

log P ′

such that
 p′
2,j,iα′′
I ′′
j,i − p′
1,j,iα′′
I ′′
j+1,i = O ( (P ′)2P ′′

H
 ) mod p′′

and
 p′
2α′′
I ′′
0,1 − p′
1α′′
I ′′
0,2 = Oη
 ( (P ′)
2P ′′

H
 ) mod p′′

for all p′′ ∈ P(⃗I ′′), j ∈ {0, 1, . . . , k − 1}, and i = 1, 2. For X large enough, the
error term Oη( (P ′)2P ′′

H ) is less than 1/2 in magnitude; thus the nearest integer to
p′
2,j,iα′′
I ′′
j,i − p′
1,j,iα′′
I ′′
j+1,i is divisible by all the primes in P(⃗I ′′), and is hence divisible by
the product Q := ∏

p′′∈P(⃗I ′′) p′′ of all the primes. Thus

p′
2,j,iα′′
I ′′
j,i − p′
1,j,iα′′
I ′′
j+1,i = O ( (P ′)2P ′′

H
 ) mod Q

for all j = 0, 1, . . . , k − 1 and i = 1, 2 and similarly

p′
2α′′
I ′′
0,1 − p′
1α′′
I ′′
0,2 = O ( (P ′)
2P ′′

H
 ) mod Q. (54)

We multiply the former equation by ∏

0≤j′<j p′
1,j′,i ∏

j<j′<k p′
2,j′,i and sum the tele-
scoping series for j = 0, . . . , k − 1 to conclude that
(
k−1∏

j=0 p′
2,j,i
)
 α′′
I ′′
0,i −
 (k−1∏

j=0 p′
1,j,i
)
 α′′
I ′′
0,i = O ( (P ′)
k+1P ′′

H
 ) mod Q.

This implies that
 qiα′′
I ′′
0,i = O ( (P ′)
k+1P ′′

H
 ) mod Q (55)

for i = 1, 2, where qi is the non-negative integer

qi :=
 ∣
∣
∣
∣
∣
 k∏

j=1 p′
2,j,i −
 k∏

j=1 p′
1,j,i
∣
∣
∣
∣
∣ .

As ⃗I ′′ is non-degenerate, qi is strictly positive. From (51) we conclude that

1 ≤ qi ≪ d
2.

FOURIER UNIFORMITY 37

From (55), we may write

α′′
I ′′
0,i = bi
qi Q + O ( (P ′)
k+1P ′′

H
 ) mod Q (56)

for i = 1, 2 and some integers b1, b2. Inserting this into (54), we conclude that
(
p′
2 b1
q1 − p′
1 b2
q2
 ) Q = O ( (P ′)k+2P ′′

H
 ) mod Q

or equivalently
 p′
2 b1
q1 − p′
1 b2
q2 = O ( (P ′)k+2P ′′

QH
 ) mod 1.

The left-hand side is a rational of denominator at most O(d4). Meanwhile, since
P(⃗I ′′) has cardinality ≫ P ′
log P ′ ≫ X ε2/ log X, we have

Q ≫ exp(cX ε2) (57)

for some c > 0 depending on ε, ρ, θ, η. Thus the expression O( (P ′)k+2P ′′

QH ) is far smaller
than the denominator on the left-hand side, and hence

p′
2 b1
q1 − p′
1 b2
q2 = 0 mod 1.

Since we can modify b1
q1 and b2
q2 by arbitrary integers without aﬀecting the claimed
properties, and p′
1, p
′
2 are distinct, we may in fact assume without loss of generality
that p′
2 b1
q1 − p′
1 b2
q2 = 0,

thus we can write bi
qi = ap′
i
q for some integer a, some 1 ≤ q ≪ d2, and for i = 1, 2. In
particular, from (56) we have

α′′
I ′′
0,i = ap′
i
q Q + O ( (P ′)k+1P ′′

H
 ) mod Q

for i = 1, 2; from (48) we thus have

α′′
I ′′
0,i = ap′
i
q Q + O (
d3P ′′ · X
H 2
 ) mod Q.

We can then write
 α′′
I ′′
0,1 = ap′
1
q Q + T
xI ′′
0,1 mod Q

for some real number
 T = O (d
3P ′′ · X 2

H 2
 ) , (58)

38 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

and we then write
 α′′
I ′′
0,2 = ap′
2
q Q + T
xI ′′
0,2 + θ mod Q

for some real number
 θ = O (
d3P ′′ · X
H 2
 ) . (59)

Inserting these equations back into (54), we obtain

T
 ( p′
2
xI ′′
0,1 − p′
1
xI ′′
0,2
 )
 − p′
1θ = O ( (P ′)
2P ′′

H
 ) mod Q.

Since I ′′
0,2 lies within 100 H
P ′P ′′ of p′
1
p′
2 I ′′
0,1, we have

xI ′′
0,2 = p′
1
p′
2 xI ′′
0,1 + O ( H
P ′P ′′
 )

and hence by (58)
 p′
1θ = O ( d3

H + (P ′)
2P ′′

H
 ) mod Q.

Combining this with (59), (57) we conclude that

θ = O ( d3

H + (P ′)
2P ′′

H
 )

and thus
 α′′
I ′′
0,i = ap′
i
q Q + T
xI ′′
0,i + O ( d3

H + (P ′)2P ′′

H
 ) mod Q

for i = 1, 2.
Finally, by two applications of Lemma 2.6, each pair (I ′′
0,1, I ′′
0,2) is associated to at
most (O( dk
N ))
2 very good tuples; since there are ≫ d2k+1/N such tuples, the number
of pairs (I ′′
0,1, I ′′
0,2) that arise in this fashion is

≫ d
2k+1/N
( dk
N )2 ≫ dN ≫ X
H
 ( P ′

log P ′
 )2 .

The claim follows. □

FOURIER UNIFORMITY 39

5. Global structure of α′′

Proposition 4.1 gives some control on α′′, but it is currently “local” because the
parameters T, q that arise in this control depend on the pair I ′′
1 , I ′′
2 . Fortunately, one
can use the “mixing” or “ergodicity” properties of the graph of such pairs to convert
this local control to global control. To do this we ﬁrst need a lemma.

Lemma 5.1 (Mixing lemma). Let θ, η, X, H, f, ρ, ε, P ′, P ′′, I ′′, α′′ be as in Proposi-
tion 3.2. We allow implied constants to depend on θ, η, ρ, ε. Let A1, A2 be two subsets
of I ′′. Then the number of quadruplets (I ′′
1 , I ′′
2 , p
′
1, p
′
2) with I ′′
1 ∈ A1, I ′′
2 ∈ A2, p′
1, p
′
2
primes in [P ′, 2P ′], and I ′′
1 lying within 100 H
P ′P ′′ of p′
2
p′
1 I ′′
2 is

≪ (#A1)(#A2) H
X
 ( P ′

log P ′
 )2 + (#A1)
1/2(#A2)
1/2 ( P ′

log P ′
 )2 log−100 P ′. (60)

Proof. Let ψ : R → R be a non-negative Schwartz function whose Fourier transform
ˆψ(ξ) := ∫
R ψ(x)e(−xξ) dx is supported on [−1, 1]. Observe that if (I ′′
1 , I ′′
2 , p
′
1, p
′
2) is a
quadruplet of the required form, then

ψ ( X
H (
log xI ′′
2 − log xI ′′
1 + log p′
2 − log p′
1)) ≫ 1.

Thus it will suﬃce to bound the expression
∑

I ′′
1 ∈A1,I ′′
2 ∈A2
 ∑

p′
1,p′
2∈[P ′,2P ′] ψ ( X
H (
log xI ′′
2 − log xI ′′
1 + log p′
2 − log p′
1)
)

by (60). Using the Fourier inversion formula ψ(x) = ∫

R ˆψ(ξ)e(xξ) dξ, we can write
this expression as

∫

R ˆψ(ξ)
 ( ∑

I ′′∈A1 e ( X
H · ξ log xI ′′))
· ∑

I ′′∈A2 e ( X
H · ξ log xI ′′)·

∣
∣
∣
∣
∣
∣
 ∑

p′∈[P ′,2P ′] e ( X
H · ξ log p′)∣
∣
∣
∣
∣
∣
2
 dξ,

which after a change of variable can be bounded by

≪ H
X
 ∫

|ξ|≤ X
H |S1(ξ)||S2(ξ)||T (ξ)|
2 dξ

where Si(ξ) := ∑

I ′′∈Ai e(ξ log xI ′′)

for i = 1, 2 and T (ξ) := ∑

p∈[P ′,2P ′] p2πiξ.

40 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

From the triangle inequality we have

sup
ξ∈R |Si(ξ)| ≪ #Ai

while from the large sieve inequality (Lemma 2.3) we have
∫

|ξ|≤ X
H |Si(ξ)|
2 ≪ #Ai X
H .

Furthermore from [22, Lemma 2] we have

T (ξ) ≪ P ′

log P ′
 ( 1
1 + |ξ| + log−100 P ′) .

for |ξ| ≤ X
H . The claim now follows from the triangle inequality and the Cauchy-
Schwarz inequality. □

Using this lemma, we have the following tool for converting local approximate
constancy to global approximate constancy. The corollary will allow us to show that
many of the intervals I ′′ in Proposition 4.1 share essentially same values of T and q.

Corollary 5.2 (Approximate ergodicity). Let θ, η, X, H, f, ρ, ε, P ′, P ′′, I ′′, α′′ be as in
Proposition 3.2. We allow implied constants to depend on θ, η, ρ, ε. Let M, K, δ > 0.
Let (Z, d) be a metric space, and let r > 0 be a radius with the property that every
ball of radius 5r/2 can contain at most M disjoint balls of radius r/2. For each
I ′′ ∈ I ′′, let F(I ′′) be a ﬁnite subset of Z with cardinality at most K. Let S be a
collection of sextuples (I ′′
1 , I ′′
2 , z1, z2, p
′
1, p
′
2) with I ′′
1 , I ′′
2 ∈ I ′′ with z1 ∈ F(I ′′
1 ), z2 ∈
F(I ′′
2 ), d(z1, z2) ≤ r, and p′
1, p
′
2 distinct primes in [P ′, 2P ′] with I ′′
1 lying within
100 H
P ′P ′′ of p′
2
p′
1 I ′′
2 . Suppose that

#S ≥ δ(X/H)(P ′/ log P ′)
2. (61)

Then either M K 3

δ ≫ log100 P ′ (62)

or else there exists z0 ∈ Z and a collection T of pairs (I ′′, z) with I ′′ ∈ I, z ∈ F(I ′′),
and d(z, z0) ≤ 2r such that
 #T ≫ δ
M K 3 X
H ,

and such that there are ≫ δ2
M K4 X
H (P ′/ log P ′)
2 sextuples (I ′′
1 , I ′′
2 , z1, z2, p
′
1, p
′
2) ∈ S such
that (I ′′
1 , z1), (I ′′
2 , z2) both lie in T .

FOURIER UNIFORMITY 41

Proof. For technical reasons we ﬁrst need to reﬁne the set S. Let T0 be the set of all
pairs (I ′′
1 , z1) with I ′′
1 ∈ I ′′ and z1 ∈ F(I ′′). From (61) we have
∑

(I ′′
1 ,z1)∈T0 N (I ′′
1 , z1) ≥ δ(X/H)(P ′/ log P ′)2

where N (I ′′
1 , z1) := #{(I ′′
2 , z2, p
′
1, p
′
2) : (I ′′
1 , I ′′
2 , z1, z2, p
′
1, p
′
2) ∈ S}.

We have #T0 ≤ 10KX/H. We conclude that there is a subset T1 of T0 with

N (I ′′
1 , z1) ≫ δ
K (P ′/ log P ′)
2 (63)

for all (I ′′
1 , z1) ∈ T1, such that
∑

(I ′′
1 ,z1)∈T1 N (I ′′
1 , z1) ≫ δ(X/H)(P ′/ log P ′)
2. (64)

Let Ω be a maximal r-separated net in Z, thus every point in Z lies within distance
r of at least one point in Ω. From (64) and the triangle inequality we conclude that
∑

z0∈Ω
 ∑

(I ′′
2 ,z2)∈T0:z2∈B(z0,2r)
(I ′′
1 ,z1)∈T1:z1∈B(z0,r)
 ∑

p′
1,p′
2∈[P ′,2P ′]

dist(I ′′
1 , p′
2
p′
1 I ′′
2 )≤100 H
P ′P ′′
 1 ≫ δ(X/H)(P ′/ log P ′)
2. (65)

If we deﬁne
 A1(z0) := {I ′′
1 ∈ I ′′ : ∃z1 ∈ B(z0, r) such that (I ′′
1 , z1) ∈ T1}

and A2(z0) := {I ′′
2 ∈ I ′′ : ∃z2 ∈ B(z0, 2r) such that (I ′′
2 , z2) ∈ T0}

then the left-hand side of (65) is bounded by

K 2 ∑

z0∈Ω
 ∑

I ′′
1 ∈A1(z0)
I ′′
2 ∈A2(z0)
 ∑

p′
1,p′
2∈[P ′,2P ′]

dist(I ′′
1 , p′
2
p′
1 I ′′
2 )≤100 H
P ′P ′′
 1

which by Lemma 5.1 is bounded by

≪ K 2 ( P ′

log P ′
 )2 ( ∑

z0∈Ω
(#A1(z0))(#A2(z0)) H
X

+ ∑

z0∈Ω
(#A1(z0))
1/2(#A2(z0))
1/2 log−100 P ′).

42 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Any pair (I ′′
2 , z2) ∈ T0 can contribute to A2(z0) only if B(z0, r/2) is contained in
B(z2, 5r/2). As the balls B(z0, r/2) with z0 ∈ Ω are disjoint, we conclude that each
such pair contributes to at most M sets A2(z0), and hence

∑

z0∈Ω #A2(z0) ≪ M K X
H

and similarly ∑

z0∈Ω #A1(z0) ≪ M K X
H .

By Cauchy-Schwarz, we may thus bound the left-hand side of (65) by

≪ M K 3 X
H
 ( P ′

log P ′
 )2 (sup
z0∈Ω #A1(z0) H
X + log−100 P ′)

and hence
 sup
z0∈Ω #A1(z0) H
X + log−100 P ′ ≫ δ
M K 3 .

Thus, either (62) holds, or there exists z0 ∈ Ω with

#A1(z0) ≫ δ
M K 3 X
H .

Suppose the latter claim is true. If we now let T2 denote the collection of those
(I ′′
1 , z1) ∈ T1 with I ′′
1 ∈ A1(z0) and z1 ∈ B(z0, r), then we have

#T2 ≫ δ
M K 3 X
H .

From (63) there exist ≫ δ
M K3 X
H δ
K (P ′/ log P ′)
2 sextuples (I ′′
1 , I ′′
2 , z1, z2, p
′
1, p
′
2) ∈ S
such that (I ′′
1 , z1) ∈ T2. Since z1 ∈ B(z0, r) and d(z1, z2) ≤ r, we have z2 ∈ B(z0, 2r).
Thus, if we take T to be the collection of those (I ′′
1 , z1) ∈ T0 with I ′′
1 ∈ A2(z0) and
z1 ∈ B(z0, 2r), we obtain the claim. □

Let θ, η, X, H, f, ε, ρ, P ′, P ′′, I ′′, α′′ be as in Proposition 3.2. Let δ > 0 be a small
quantity (depending on θ, η, ε) which we will specify in a moment. Inspired by
Proposition 4.1, deﬁne a good quadruple to be a quadruple (I ′′, T, q, a), where I ′′ is
an interval in I ′′ ∈ I ′′, T is a real number with

|T | ≤ 1
δ X 2

H 2−ρ , (66)

FOURIER UNIFORMITY 43

q is a natural number with 1 ≤ q ≤ H ρ/δ, a ∈ {0, . . . , q − 1} is coprime to q, and
there exists a real number θ with |θ| ≤ 1
δ 1
H 1−ρ such that

α′′
I ′′ = T
xI ′′ + a
q
 ∏

p′′∈P p′′ + θ mod ∏

p′′∈P p′′ (67)

for a set P of primes in [P ′′/2, P ′′] of cardinality at least δ P ′′
log P ′′ . Proposition 4.1
guarantees that once δ is chosen suﬃciently small in terms of θ, ε, η, ρ there exist
≫ X/H good quadruples. Throughout we ﬁx δ suﬃciently small so that this holds;
in particular, implied constants may now depend on δ in addition to θ, ε, η, ρ.
We have some limitations on how many good quadruples can be associated to a
single interval I ′′:

Proposition 5.3. Let δ, ρ be as above, and let I ′′ be an interval in I ′′. Let K ≥ 2
δ ,
and let (I ′′, Tj, qj, aj) for j = 1, . . . , K be a collection of good quadruples. Then there
exist 1 ≤ j < j′ ≤ K with the following properties:
(i) qj = qj′.
(ii) aj = aj′.
(iii) Tj = Tj′ + O ( X
H 1−ρ ).

Proof. Without loss of generality we may take K = ⌈ 2
δ ⌉. For j = 1, . . . , K, let Pj be
the set of primes in [P ′′/2, P ′′] associated to the good quadruple (I ′′, Tj, qj, aj). Then

∑

p′′∈[P ′′/2,P ′′]
 ( K∑

j=1 1p′′∈Pj
 )
 ≥ Kδ P ′′

log P ′′ ≥ 2 P ′′

log P ′′

and ∑K
j=1 1Pj ≤ K ≪ 1/δ. From this and the prime number theorem we conclude
that ∑K
j=1 1Pj ≥ 2 for at least ≫ P ′′
log P ′′ primes in [P ′, 2P ′]; this implies that there
exist distinct indices j, j′ ∈ {1, . . . , K} such that

#(Pj ∩ Pj′) ≫ P ′′

log P ′′ .

If one writes Q := ∏

p′′∈Pj ∩Pj′ p′′, we then have

Q ≫ exp(cδP ′′) ≥ exp(cδX ε2) (68)

for some cδ > 0. On the other hand, from (67) one has

α′′
I ′′ = Tj
xI ′′ + aj
qj Q + O ( 1
H 1−ρ
 ) mod Q (69)

and
 α′′
I ′′ = Tj′
xI ′′ + aj′
qj′ Q + O ( 1
H 1−ρ
 ) mod Q. (70)

44 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

In particular,
 (aj
qj − aj′
qj′ )Q = O ( X 2

H 2−ρ
 ) mod Q

which when combined with (68) (and noting that the denominator on the left-hand
side is at most Oδ(H 2ρ)) forces aj
qj − aj′
qj′ = 0 mod 1.

Since aj/qj and aj′/qj′ are in lowest terms and in [0, 1), this implies that aj = aj′
and qj = qj′. Subtracting (69) from (70), we conclude that

Tj − Tj′
xI ′′ = O ( 1
H 1−ρ
 ) mod Q;

since |Tj − Tj′| ≤ 2
δ X 2
H 2−ρ , we conclude from (68) that

Tj − Tj′
xI ′′ = O ( 1
H 1−ρ
 ) ,

and hence Tj − Tj′ ≪δ X
H 1−ρ . The claim follows. □

From the above proposition and the greedy algorithm, we conclude

Corollary 5.4. For each I ′′ ∈ I ′′, there exists a set F(I ′′) of triples (T, q, a) of
cardinality
 #F(I ′′) ≤ 2
δ ,

such that, for any good quadruple (I ′′, T, q, a), there exists T ′ ∈ R such that (T ′, q, a) ∈
F(I ′′) and
 T = T ′ + O ( X
H 1−ρ
 ) .

On the other hand, Proposition 4.1 provides us with a large number of quadruples:

Proposition 5.5. Let δ be as above and X suﬃciently large depending on δ and ε.
All implied constants may depend on ε, η, θ, ρ. Then, for ≫ (X/H) · (P ′/ log P ′)
2 of
the pairs (I ′′
1 , I ′′
2 ) of intervals (I ′′)
2, there exist T1, T2, q′, a
′
1, a
′
2 such that (T1, q′, a
′
1) ∈
F(I ′′
1 ) and (T2, q′, a
′
2) ∈ F(I ′′
2 ), and

T2 = T1 + O ( X
H 1−ρ
 ) . (71)

Furthermore, for each such pair, there exist primes p′
1, p
′
2 ∈ [P ′, 2P ′] coprime to q′

such that I ′′
1 lies within 100 H
P ′P ′′ of p′
2
p′
1 I ′′
2 , and such that

p′
2a′
1 = p′
1a′
2 mod q′. (72)

FOURIER UNIFORMITY 45

Proof. This is almost immediate from Proposition 4.1; the main diﬃculty is that the
integers a, q provided by that proposition need not be coprime.
We resolve this as follows. If I ′′ ∈ I ′′ and (T, q, a) ∈ F(I ′′), then q has at most
O( log X
log P ′′ ) = Oε(1) prime factors in [P ′′/2, P ′′]. Thus, for each I ′′ ∈ I ′′, there are at
most O(1) primes that divide q for some (T, q, a) ∈ F(I ′′).

Proposition 4.1 provides us with ≫ X
H ( P ′
log P ′ )2 pairs (I ′′
1 , I ′′
2 ) of intervals (I ′′)
2,
together with associated primes p′
1, p
′
2, obeying the properties of that proposition. It
could happen that p′
1 or p′
2 divides q for some (T, q, a) in F(I ′′
1 ) or F(I ′′
2 ), but by
the preceding paragraph, the number of times this can happen is at most O( X
H P ′
log P ′ ),

which is a negligible portion when X is large enough. Thus for ≫ X
H ( P ′
log P ′ )2 of the
above pairs, p′
1 or p′
2 do not divide any such q.
From Proposition 4.1, we have

α′′
I ′′
j = T
xI ′′
j + aj
q Q + O ( 1
H 1−ρ
 ) mod Q

for j = 1, 2, where Q := ∏

p′′∈P(I ′′
1 ,I ′′
2 ) p′′. We write a1/q in lowest terms as a′
1/q′.
Then (I ′′
1 , T, q′, a
′
1) is a good quadruple and p′
1, p
′
2 do not divide q′. From (46) we
may thus also write a2/q in lowest terms as a′
2/q′ and still have that (72) holds. Then
(I ′′
2 , T, q′, a
′
2) is a good quadruple, and the claim follows from Corollary 5.4. □

Let Z be the collection of triples (T, q, a) with T ∈ R, q ≥ 1, and a coprime to q,
endowed with the metric10

d((T1, q1, a1), (T2, q2, a2)) := c(δ)H 1−ρ

X |T1 − T2| + 1q1̸=q2 + 1
1001a1̸=a2. (73)

and some suﬃciently small constant c(δ) > 0 depending on δ (and thus ultimately
on θ, η, ρ, ε). Let S be the collection of sextuples

(I ′′
1 , I ′′
2 , (T1, q′, a1), (T2, q′, a2), p
′
1, p
′
2)

with I ′′
1 , I ′′
2 ∈ I ′′, (T1, q′, a1) ∈ F(I ′′
1 ), (T2, q′, a2) ∈ F(I ′′
2 ), and p′
1, p
′
2 distinct primes
in [P ′, 2P ′] with I ′′
1 lying within 100 H
P ′P ′′ of p′
2
p′
1 I ′′
2 , with p1, p2 coprime to q′ and obeying
(72) and (71). In particular (for c(δ) suﬃciently small) we have

d((T1, q′, a1), (T2, q′, a2)) ≤ 1
10.

10The 1
100 1a1̸=a2 term is present only to keep the metric Z from degenerating, but otherwise
plays no role in the argument; if one prefers, one could drop this term and observe that Corollary
5.2 also applies to degenerate metric spaces.

46 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

From Proposition 5.5 we have #S ≫ (X/H) · (P ′/ log P ′)2. Applying Corollary
5.2 with r = 1
10, M = 100, K = 2
δ , we conclude that there exists (T0, q0, a0) ∈ Z
and a collection T of quadruples (I ′′, T, q, a) with I ′′ ∈ I, (T, q, a) ∈ F(I ′′), and
d((T, q, a), (T0, q0, a0)) ≤ 1
5 such that
#T ≫ X
H , (74)

and there are ≫ X
H (P ′/ log P ′)2 sextuples (I ′′
1 , I ′′
2 , (T1, q1, a1), (T2, q2, a2), p
′
1, p
′
2) ∈ S
such that (I ′′
1 , T1, q1, a1), (I ′′
2 , T2, q2, a2) both lie in T .
If (I ′′, T, q, a) ∈ T , then d((T, q, a), (T0, q0, a0)) ≤ 1
5, and hence by (73) we have
q = q0 and
 T = T0 + O ( X
H 1−ρ
 ) . (75)

From (66) we thus have
 T0 ≪ X 2

H 2−ρ . (76)

At present q0 obeys the bounds 1 ≤ q0 ≪ H ρ. We can improve the control on q0
signiﬁcantly.

Proposition 5.6. q0 ≪ 1.

Proof. Consider the graph G whose vertex set V is the set T as above, and whose
edge set E consists of pairs (I ′′
1 , T1, q0, a1), (I ′′
2 , T2, q0, a2) in T with

(I ′′
1 , I ′′
2 , (T1, q0, a1), (T2, q0, a2), p
′
1, p
′
2) ∈ S

for some p′
1 and p′
2. Then by the preceding dicussion G has ≫ N vertices and ≫ dN
edges, where N := X/H and d := (P ′/ log P ′)
2.
Now let k be the ﬁrst even integer for which

dk ≥ N 2+ε.

Using the Blakley-Roy inequality as in Section 4, the number of ( k
2 + 1)-tuples

(Q0, . . . , Qk/2) ∈ V k/2+1

such that {Qj, Qj+1} ∈ E for 0 ≤ j < k/2 is ≫ dk/2N . The number of possible
values for the pair (Q0, Qk/2) is O(N 2). Thus by the Cauchy-Schwarz inequality,
there are ≫ dk pairs of k+2
2 -tuples of the above form with matching pairs (Q0, Qk/2).
Relabeling, we conclude that there the number of k-tuples

(Qj)j=0,1,...,k−1 ∈ V k

such that {Qj, Qj+1} ∈ E for j = 0, 1, . . . , k − 1 is ≫ d
k. On the other hand, we may
upper bound the number of such tuples in a diﬀerent way, as we will now do. Writing

FOURIER UNIFORMITY 47

Qj = (I ′′
j , Tj, q0, aj), we see from (72) that there are primes p′
j,1, p
′
j,2 ∈ [P ′, 2P ′] such
that p′
j,2aj = p′
j,1aj+1 mod q0

(with the periodic convention ak = a0) and such that I ′′
j lies within 100 H
P ′P ′′ of p′
j,2
p′
j,1 I ′′
j+1
for all j = 0, 1, . . . , k − 1. From the ﬁrst claim we have

k∏

j=1 p′
j,2 =
 k∏

j=1 p′
j,1 mod q0,

while from the second claim we have

k∏

j=1 p′
2,j −
 k∏

j=1 p′
1,j ≪ (P ′)
k

N .

by repeating the derivation of (51). By Lemma 2.6, the number of tuples of primes
(p′
1,1, . . . , p′
k,1, p
′
1,2, . . . , p′
k,2) obeying these constraints is ≪ dk
N ( 1
q1/2
0 + 1
log X )). There are

≪ N choices for I ′′
1 , and this interval and the tuple of primes determine all the other
I ′′
k . Since all the sets F(I ′′
j ) have cardinality Oδ(1), we conclude that the number of
k-tuples (Qj)j=0,1,...,k−1 under consideration is

≪ N dk

N
 ( 1

q1/2
0 + 1
log X
 )
 .

Comparing the upper and lower bounds yields

1

q1/2
0 + 1
log X ≫ 1

and the claim follows. □

From (67), (75) we see that whenever (I ′′, T, q0, a) ∈ T , one has

α′′
I ′′ = T0
xI ′′ + b
q0 + O ( 1
H 1−ρ
 ) mod 1 (77)

for some b ∈ Z/q0Z. Since each I ′′ is associated to O(1) quadruples in T , we conclude
from (74) that for ≫ε,δ X/H intervals I ′′ ∈ I ′′, one has (77) for some b ∈ Z/q0Z.
Let I ′′ be one of these intervals, so that (see (40))
∣
∣
∣
∣
∣
 ∑

n∈I ′′ f (n)e(−α′′
I ′′n)

∣
∣
∣
∣
∣ ≫ H
P ′P ′′ .

48 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

Let H ∗ := H 1−2ρ
P ′P ′′ . We may translate I ′′ by any shift of size at most H ∗ without
aﬀecting this estimate. Averaging over such shifts, we conclude that
∣
∣
∣
∣
∣
∫

I ′′
 ∑

x<n≤x+H ∗ f (n)e(−α′′
I ′′n) dx
∣
∣
∣
∣
∣ ≫ H
P ′P ′′ H ∗

and thus by the triangle inequality
∫

I ′′
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H ∗ f (n)e(−α′′
I ′′(n − x) − bx/q0)
∣
∣
∣
∣
∣ dx ≫ H
P ′P ′′ H ∗

From (77), (76) and Taylor expansion, we have

e(−α′′
I ′′(n − x) − bx/q0) = e (
−T0
x (n − x)
) e(bn/q0) + O(H −ρ)

= n−2πiT0x2πiT0e(bn/q0) + O(H −ρ).

The contribution of the O(H −ρ) is negligible, thus
∫

I ′′
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H ∗ f (n)n−2πiT0e(bn/q0)

∣
∣
∣
∣
∣ dx ≫ H
P ′P ′′ H ∗.

Recalling (b, q0) = 1 and Proposition 5.6, we can apply a Fourier decomposition

e(bn/q0) = ∑

q0=q1q2
 ∑

χ (q1) cb,χ1q2|nχ(n/q2) , cb,χ := 1
ϕ(q1)
 ∑

x mod q1 χ(x)e
( bx
q1
 )

where cb,χ ≪ 1 and χ ranges over Dirichlet characters of modulus q1. From the
triangle inequality, we thus have

∑

q0=q1q2
 ∑

χ (q1)
 ∫

I ′′
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H ∗ f (n)n
−2πiT01q2|nχ(n/q2)

∣
∣
∣
∣
∣ dx ≫ H
P ′P ′′ H ∗.

Summing over the ≫ε X/H intervals I ′′, we conclude that

∑

q0=q1q2
 ∑

χ (q1)
 ∫ 10X/P ′P ′′

X/10P ′P ′′
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H ∗ f (n)n
−2πiT01q2|nχ(n/q2)

∣
∣
∣
∣
∣ dx ≫ X
P ′P ′′ H ∗.

By the triangle inequality, there thus exist q0 = q1q2 and χ (q1) such that
∫ 10X/P ′P ′′

X/10P ′P ′′
 ∣
∣
∣
∣
∣
 ∑

x<n≤x+H ∗ f (n)n−2πiT01q2|nχ(n/q2)

∣
∣
∣
∣
∣ dx ≫ X
P ′P ′′ H ∗.

FOURIER UNIFORMITY 49

Writing n = dm with d|q∞
2 and (m, q2) = 1 we obtain by the triangle inequality

∑

d|q∞
2
q2|d
 ∫ 10X/P ′P ′′

X/10P ′P ′′
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

x<dn≤x+H ∗
(n,q2)=1
 f (n)n−2πiT0χ(n)

∣
∣
∣
∣
∣
∣
∣
∣
 dx ≫ X
P ′P ′′ H ∗.

where d|q∞
2 means that all the prime factors of d are also prime factors of q2. Since∑

d|q∞
2 d−1 ≪ 1 there exists an natural number d = O(1) such that,

∫ 10X/dP ′P ′′

X/10dP ′P ′′
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

x<n≤x+H ∗/d
(n,q2)=1
 f (n)n−2πiT0χ(n)

∣
∣
∣
∣
∣
∣
∣
∣
 dx ≫η,ε,δ X
P ′P ′′ H ∗.

Therefore by [24, Proposition A.3] we have D(f 1(n,q2)=1n
−2πiT0χ; T ′; Q) ≪ 1 for some
Q ≪ 1 and |T ′| ≪ X. Therefore D(f ; T ; Q) ≪ 1 for some |T | ≪ X 2/H 2−ρ and
Q ≪ 1 as claimed.

6. Proof of Corollary 1.5 and Corollary 1.3

Now we prove Corollary 1.5 and Corollary 1.3. It is enough to prove the former
corollary since, for any ﬁxed Q > 0 and A > 0, we have D(λ; X A; Q) → ∞ as X → ∞
by the Vinogradov-Korobov zero-free region [29, §9.5].
We restrict attention to the correlation for f (n)a(n + h)b(n + 2h), as the other
two correlations are handled similarly. The proof proceeds along classical lines by
noticing that ∑

|h|≤H
 (
1 − |h|
H
 ) f (n)a(n + h)b(n + 2h)

= 1
H
 ∫ X

1
 ∫ 1

0 Sx,f (α)Sx,b(α)Sx,a(−2α)dαdx + O(H) (78)

where Sx,g(α) := ∑

x<n≤x+2H g(n)e(αn).

Notice that
∣
∣
∣
∣
∫ 1

0 Sx,f (α)Sx,b(α)Sx,a(−2α)dα∣
∣
∣
∣ ≤ sup
α |Sx,f (α)|
1/3 ∫ 1

0 |Sx,b(α)| · |Sx,a(−2α)| · |Sx,f (α)|
2/3 dα

≤ sup
α |Sx,f (α)|
1/3 · (∫ 1

0 |Sx,b(α)|
3dα)1/3 · (∫ 1

0 |Sx,a(α)|
3dα)1/3 · (∫ 1

0 |Sx,f (α)|
2dα)1/3 .

50 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

We now claim the bound ∫ 1

0 |Sx,a(α)|
3dα ≪ H 2

If |a(n)| ≪ Λ(n) then this bound follows from [10, Proposition 4.2]. On the other
hand if |a(n)| ≪ 1 for all integers n ≥ 1, then, by H¨older’s inequality,
∫ 1

0 |Sx,a(α)|
3dα ≤ (∫ 1

0 |Sx,a(α)|
2dα)1/2 · (∫ 1

0 |Sx,a(α)|
4dα)1/2 ≪ H 1/2 · H 3/2 = H 2.

The general case a(n) ≪ 1 + Λ(n) now follows from the triangle inequality. Similarly
for b(n). Therefore,
∣
∣
∣
∣
∫ 1

0 Sx,f (α)Sx,b(α)Sx,a(−2α)dα∣
∣
∣
∣ ≪ sup
α |Sx,f (α)|
1/3 · H 5/3

and ﬁnally, ∫ X

1 sup
α |Sx,f (α)|
1/3dα ≤ (∫ X

1 sup
α |Sx,f (α)|dα)1/3 · X 2/3.

Thus,
∣
∣
∣
∣
∣
∣
 ∑

|h|≤H
 (
1 − |h|
H
 ) ∑

n≤X f (n)a(n + h)b(n + 2h)

∣
∣
∣
∣
∣
∣ ≤ H 2/3·X 2/3·(∫ X

1 sup
α |Sx,f (α)|dα)1/3

(79)
Therefore if the left-hand side of (79) is ≥ ηHX, then,

cη3HX ≤ ∫ X

1 sup
α |Sx,f (α)|dα

for some absolute constant c > 0. Hence, for some Y ∈ [cη3X/3, X], one has,
∫ 2Y

Y sup
α |Sx,f (α)|dα ≥ cη3

2 Y H.

Now the claim follows from Theorem 1.4.

References

[1] A. Balog. The prime k-tuplets conjecture on average. In Analytic number theory (Allerton
Park, IL, 1989), volume 85 of Progr. Math., pages 47–75. Birkh¨auser Boston, Boston, MA,
1990.
[2] G. R. Blakley and P. Roy. A H¨older type inequality for symmetric matrices with nonnegative
entries. Proc. Amer. Math. Soc., 16:1244–1245, 1965.
[3] V. Blomer. On triple correlations of divisor functions. Bull. Lond. Math. Soc., 49(1):10–22,
2017.
 FOURIER UNIFORMITY 51

[4] S. Chowla. The Riemann hypothesis and Hilbert’s tenth problem. Mathematics and Its Appli-
cations, Vol. 4. Gordon and Breach Science Publishers, New York-London-Paris, 1965.
[5] H. Davenport. On some inﬁnite series involving arithmetical functions. ii. Quart. J. Math. Oxf.,
8:313–320, 1937.
[6] P. D. T. A. Elliott. Probabilistic number theory. I, volume 239 of Grundlehren der Mathematis-
chen Wissenschaften [Fundamental Principles of Mathematical Science]. Springer-Verlag, New
York-Berlin, 1979. Mean-value theorems.
[7] N. Frantzikinakis and B. Host. Asymptotics for multilinear averages of multiplicative functions.
Math. Proc. Cambridge Philos. Soc., 161(1):87–101, 2016.
[8] W. T. Gowers. A new proof of Szemer´edi’s theorem for arithmetic progressions of length four.
Geom. Funct. Anal., 8(3):529–551, 1998.
[9] A. Granville and K. Soundararajan. Large character sums: pretentious characters and the
P´olya-Vinogradov theorem. J. Amer. Math. Soc., 20(2):357–384, 2007.
[10] B. Green and T. Tao. Restriction theory of the Selberg sieve, with applications. J. Th´eor.
Nombres Bordeaux, 18(1):147–182, 2006.
[11] B. Green and T. Tao. Quadratic uniformity of the M¨obius function. Ann. Inst. Fourier (Greno-
ble), 58(6):1863–1935, 2008.
[12] B. Green and T. Tao. Linear equations in primes. Ann. of Math. (2), 171(3):1753–1850, 2010.
[13] B. Green and T. Tao. The M¨obius function is strongly orthogonal to nilsequences. Ann. of
Math. (2), 175(2):541–566, 2012.
[14] B. Green and T. Tao. The quantitative behaviour of polynomial orbits on nilmanifolds. Ann.
of Math. (2), 175(2):465–540, 2012.
[15] D. R. Heath-Brown. The number of primes in a short interval. J. Reine Angew. Math., 389:22–
63, 1988.
[16] M. N. Huxley. On the diﬀerence between consecutive primes. Invent. Math., 15:164–170, 1972.
[17] H. Iwaniec and E. Kowalski. Analytic number theory, volume 53 of American Mathematical
Society Colloquium Publications. American Mathematical Society, Providence, RI, 2004.
[18] K. Kawada. The prime k-tuplets in arithmetic progressions. Tsukuba J. Math., 17(1):43–57,
1993.
[19] K. Kawada. A Montgomery-Hooley type theorem for prime k-tuplets. Acta Math. Hungar.,
66(3):177–200, 1995.
[20] O. Klurman. Correlations of multiplicative functions and applications. Compos. Math.,
153(8):1622–1657, 2017.
[21] D. Koukoulopoulos. Pretentious multiplicative functions and the prime number theorem for
arithmetic progressions. Compos. Math., 149(7):1129–1149, 2013.
[22] K. Matom¨aki and M. Radziwi l l. A note on the Liouville function in short intervals. arxiv:
1502.02374, 2015.
[23] K. Matom¨aki and M. Radziwi l l. Multiplicative functions in short intervals. Ann. of Math. (2),
183(3):1015–1056, 2016.
[24] K. Matom¨aki, M. Radziwi l l, and T. Tao. An averaged form of Chowla’s conjecture. Algebra
Number Theory, 9(9):2167–2196, 2015.
[25] K. Matom¨aki, M. Radziwi l l, and T. Tao. Correlations of the von mangoldt and higher divisor
functions i. long shift ranges. arXiv:1707.01315, 2017.
[26] H. Mikawa. On prime twins in arithmetic progressions. Tsukuba J. Math., 16(2):377–387, 1992.
[27] H. L. Montgomery. The analytic principle of the large sieve. Bull. Amer. Math. Soc., 84(4):547–
567, 1978.

52 KAISA MATOM ¨AKI, MAKSYM RADZIWI L L, AND TERENCE TAO

[28] H. L. Montgomery. Maximal variants of the large sieve. J. Fac. Sci. Univ. Tokyo Sect. IA
Math., 28(3):805–812 (1982), 1981.
[29] H. L. Montgomery. Ten lectures on the interface between analytic number theory and har-
monic analysis, volume 84 of CBMS Regional Conference Series in Mathematics. Published
for the Conference Board of the Mathematical Sciences, Washington, DC; by the American
Mathematical Society, Providence, RI, 1994.
[30] A. Sidorenko. A correlation inequality for bipartite graphs. Graphs Combin., 9(2):201–204,
1993.
[31] T. Tao. The logarithmically averaged Chowla and Elliott conjectures for two-point correlations.
Forum Math. Pi, 4:e8, 36, 2016.
[32] T. Tao. Equivalence of the logarithmically averaged Chowla and Sarnak conjectures. In Number
theory—Diophantine problems, uniform distribution and applications, pages 391–421. Springer,
Cham, 2017.
[33] T. Tao and J. Ter¨av¨ainen. The structure of logarithmically averaged correlations of multiplica-
tive functions, with applications to the Chowla and Elliott conjectures. arxiv: 1708.02610,
2017.
[34] T. Tao and J. Ter¨av¨ainen. Odd order cases of the logarithmically averaged Chowla conjecture.
J. Th´eor. Nombres Bordeaux, 2018.
[35] A. Zaccagnini. Primes in almost all short intervals. Acta Arith., 84(3):225–244, 1998.
[36] T. Zhan. On the representation of large odd integer as a sum of three almost equal primes. Acta
Math. Sinica (N.S.), 7(3):259–272, 1991. A Chinese summary appears in Acta Math. Sinica 35
(1992), no. 4, 575.

Department of Mathematics and Statistics, University of Turku, 20014 Turku,
Finland
E-mail address: ksmato@utu.fi

Department of Mathematics, Caltech, 1200 E California Blvd, Pasadena, CA,
91125
E-mail address: maksym.radziwill@gmail.com

Department of Mathematics, UCLA, 405 Hilgard Ave, Los Angeles CA 90095, USA
E-mail address: tao@math.ucla.edu
