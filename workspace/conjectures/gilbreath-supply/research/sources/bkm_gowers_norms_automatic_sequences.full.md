<!-- source: https://arxiv.org/pdf/2002.09509 | converted from PDF -->

DISCRETE ANALYSIS, 2023:4, 62 pp.
www.discreteanalysisjournal.com

Gowers Norms for Automatic Sequences

Jakub Byszewski* Jakub Konieczny† Clemens Müllner‡

Received 17 May 2021; Published 24 May 2023

Abstract: We show that any automatic sequence can be separated into a structured part
and a Gowers uniform part in a way that is considerably more efficient than guaranteed
by the Arithmetic Regularity Lemma. For sequences produced by strongly connected and
prolongable automata, the structured part is rationally almost periodic, while for general
sequences the description is marginally more complicated. In particular, we show that
all automatic sequences orthogonal to periodic sequences are Gowers uniform. As an
application, we obtain for any l ≥ 2 and any automatic set A ⊂ N0 lower bounds on the
number of l-term arithmetic progressions – contained in A – with a given difference. The
analogous result is false for general subsets of N0 and progressions of length ≥ 5.

Key words and phrases: Gowers norms, automatic sequences, higher degree uniformity

1 Introduction

Automatic sequences, that is, sequences computable by finite automata, constitute one of the basic classes
of sequences defined in terms of complexity. Being both simple enough to be rigorously analysed and
complex enough to be interesting, they are the subject of extensive investigation in various branches of
mathematics and computer science. (For precise definitions and extended background, see Section 3.)

*Supported by National Science Centre, Poland grant number 2018/29/B/ST1/01340.
†Supported by the ERC grant ErgComNum 682150 at the Hebrew University of Jerusalem and is currently working within
the framework of the LABEX MILYON (ANR-10-LABX-0070) of Université de Lyon, within the program "Investissements
d’Avenir" (ANR-11-IDEX-0007) operated by the French National Research Agency (ANR). He also acknowledges support
from the Foundation for Polish Science (FNP).
‡Supported by European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation
programme under the Grant Agreement No 648132, by the project F55-02 of the Austrian Science Fund FWF which is part of
the Special Research Program “Quasi-Monte Carlo Methods: Theory and Applications” and by Project I1751 (FWF), called
MUDERA (Multiplicativity, Determinism, and Randomness).

© 2023 Jakub Byszewski, Jakub Konieczny, and Clemens M¨ullner
cb Licensed under a Creative Commons Attribution License (CC-BY) DOI: 10.19086/da.75201arXiv:2002.09509v3  [math.NT]  23 May 2023
JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

The study of various notions of uniformity for automatic sequences can be traced back at least as
far as 1968, when Gelfond [Gel68] showed that the integers whose sum of base-k digits lie in a given
residue class modulo l are well distributed in arithmetic progressions (subject to certain congruence
conditions). In the same paper, Gelfond posed several influential questions on distribution of the sum of
base-k digits within residue classes along subsequences which sparked much subsequent research [Kim99,
MR09, MR10, MR15, DMR13, Mül18, MR18, DMR11, MS15, Spi18]. An accessible introduction can
be found in [Mor08].
A systematic study of various notions of pseudorandomness was undertaken by Mauduit and Sarközy
in [MS98] for the Thue–Morse and Rudin–Shapiro sequences. Specifically, they showed that these
sequences do not correlate with periodic sequences, but do have large self-correlations. In this paper we
consider a notion of pseudorandomness originating from higher order Fourier analysis, corresponding to
Gowers uniformity norms (for more on Gowers norms, see Section 2). The second-named author showed
[Kon19] that the Thue–Morse and Rudin–Shapiro sequences are highly Gowers uniform of all orders.
Here, we obtain a similar result in a much more general context.
The celebrated Inverse Theorem for Gowers uniformity norms [GTZ12] provides a helpful criterion
for Gowers uniformity. It asserts, roughly speaking, that any sequence which does not correlate with
nilsequences of bounded complexity has small Gowers norms. We do not follow this path here directly,
but want to point out some striking similarities to related results. For the purposes of this paper, there is
no need to define what we mean by a nilsequence or its complexity, although we do wish to point out that
nilsequences include polynomial phases, given by n ↦→ e (p(n)) where e(t) = e2πit and p ∈ R[x].
For a number of natural classes of sequences, in order to verify Gowers uniformity of all orders it
is actually sufficient to verify lack of correlation with linear phases n ↦→ e(nα) where α ∈ R, or even
just with periodic sequences. In particular, Frantzikinakis and Host [FH17] showed that a multiplicative
sequence which does not correlate with periodic sequences is Gowers uniform of all orders. Eisner
and the second-named author showed [EK18] that an automatic sequence which does not correlate with
periodic sequences also does not correlate with any polynomial phases. This motivates the following
result. For the sake of brevity, we will say that a bounded sequence a : N0 → C is highly Gowers uniform
if for each d ≥ 1 there exists c = cd > 0 such that ∥a∥U d [N] ≪d N−c. (1)

(See Sec. 2.2.1 for the asymptotic notation and Sec. 2.2.2 for the definition of ∥a∥U d [N].)

Theorem A. Let a : N0 → C be an automatic sequence and suppose that a does not correlate with
periodic sequences in the sense that
 lim
N→∞ 1
N
 N−1
∑
n=0 a(n)b(n) = 0

for any periodic sequence b : N0 → C. Then a is highly Gowers uniform.

In fact, we obtain a stronger decomposition theorem. The Inverse Theorem is essentially equivalent
to the Arithmetic Regularity Lemma [GT10a], which asserts, again roughly speaking, that any 1-bounded
sequence f : [N] → [−1, 1] can be decomposed into a sum

f = fnil + fsml + funi, (2)

DISCRETE ANALYSIS, 2023:4, 62pp. 2

GOWERS NORMS FOR AUTOMATIC SEQUENCES

where the structured component fnil is a (bounded complexity) nilsequence, fsml has small L2 norm and
funi has small Gowers norm of a given order. In light of the discussion above, one might expect that in
the case when f is an automatic sequence, it should be possible to ensure that fnil is essentially a periodic
sequence.
This expectation is confirmed by the following new result, which is a special case of our main
theorem. For standard terminology used, see Section 2 (for Gowers norms) and 3 (for automatic
sequences). Rationally almost periodic sequences were first introduced in [BR02], and their properties
are studied in more detail in [BKPLR16]. A sequence is rationally almost periodic (RAP) if it can be
approximated by periodic sequences arbitrarily well in the Besicovitch metric; i.e., x : N0 → Ω is RAP
if for any ε > 0 there is a periodic sequence y : N0 → Ω with |{n < N | x(n) ̸= y(n)}| /N ≤ ε for large
enough N.

Theorem B. Let a : N0 → C be an automatic sequence produced by a strongly connected, prolongable
automaton. Then there exists a decomposition

a(n) = astr(n) + auni(n), (3)

where astr is rationally almost periodic and auni is highly Gowers uniform (cf. (1)).

Note that any RAP sequence can be decomposed as the sum of a periodic sequence and a sequence
with a small L1 norm. Hence, (3) can be brought into the form analogous to (2), with a periodic sequence
in place of a general nilsequence. Furthermore, this decomposition works simultaneously for all orders.
For general automatic sequences we need a more general notion of a structured sequence. There
are three basic classes of k-automatic sequences which fail to be Gowers uniform, which we describe
informally as follows:

1. periodic sequences, whose periods may be assumed to be coprime to k;

2. sequences which are only sensitive to terminal digits, such as νk(n) mod 2 where νk(n) is the
largest power of k which divides n;

3. sequences which are only sensitive to initial digits, such as νk(nrev
k + 1) mod 2 where nrev
k denotes
the result of reversing the base k digits of n.

By changing the basis, we can include in the last category also sequences which depend on the length of
the expansion of n. For instance, if lengthk(n) denotes the length of the expansion of n in base k then
lengthk(n) mod 2 depends only on the leading digit of n in base k2.
Our main result asserts that any automatic sequence can be decomposed as the sum of a structured part
and a highly Gowers uniform part, where the structured part is a combination of the examples outlined
above. More precisely, let us say that a k-automatic sequence a : N0 → Ω is weakly structured if there
exist a periodic sequence aper : N0 → Ωper with period coprime to k, a forward synchronising k-automatic
sequence afs : N0 → Ωfs and a backward synchronising k-automatic sequence abs : N0 → Ωbs, as well as
a map F : Ωper × Ωfs × Ωbs → Ω such that

a(n) = F (
aper(n), afs(n), abs(n)
) . (4)

(For definitions of synchronising sequences, we again refer to Sec. 3.)

DISCRETE ANALYSIS, 2023:4, 62pp. 3

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

Theorem C. Let a : N0 → C be an automatic sequence. Then there exists a decomposition

a(n) = astr(n) + auni(n), (5)

where astr is weakly structured (cf. (4)) and auni is highly Gowers uniform (cf. (1)).

Remark 1.1. The notion of a weakly structured sequence is very sensitive to the choice of the basis. If
k, k′ ≥ 1 are both powers of the same integer k0 then k-automatic sequences are the same as k′-automatic
sequences, but k-automatic weakly structured sequences are not the same as a k′-automatic weakly
structured sequences. If the sequence a in Theorem C is k-automatic then astr is only guaranteed to be
weakly structured in some basis k′ that is a power of k, but it does not need to be weakly structured in the
basis k.

Example 1.2. Let a : N0 → R be the 2-automatic sequence computed by the following automaton.

s0/4start
 s2/1 s3/2

s1/1

0
 0

1
1 1
1

0
 0

Formal definitions of automata and the associated sequence can be found it Section 3. For now, it suffices
to say that in order to compute a(n), n ∈ N0, one needs to expand n in base 2 and traverse the automaton
using the edges corresponding to the consecutive digits of n and then read off the output at the final state.
For instance, the binary expansion of n = 26 is (26)2 = 11010, so the visited states are s0, s1, s3, s3, s2, s3
and a(26) = 2.
Let b : N0 → R be the sequence given by b(n) = (−1)ν2(n+1), where ν2(m) is the largest value of ν
such that 2ν | m. For instance, ν2(27) = 0 and b(26) = 1. Then the structured part of a is astr = 2 + b,
and the uniform part is necessarily given by auni = a − astr. Note that b (and hence also astr and auni) can
be computed by an automaton with the same states and transitions as above, but with different outputs.
Let also c : N0 → R denote the sequence given by c(n) = (−1) f (n) where f (n) is the number of those
maximal blocks of 1s in the binary expansion of n that have length congruent to 2 or 3 modulo 4. For
instance, f (26) = 1 and c(26) = −1. Then auni = ( 1
2 + 1
2 b)c.

This example is very convenient as it allows one to give easy representations of the structured and
uniform part. However, the situation can be more complicated in general and we include another example
to emphasize this fact.

Example 1.3. Let a : N0 → R be the 2-automatic sequence computed by the following automaton.

DISCRETE ANALYSIS, 2023:4, 62pp. 4

GOWERS NORMS FOR AUTOMATIC SEQUENCES

s0/1start
 s3/4 s4/5

s1/2 s2/3

0
 1
 0

1
 0 1

0, 1 0
1

It turns out that the structured part can again be expressed using b, i.e., astr = 3b − 1, but it is very
difficult to find a simple closed form for the uniform part. Indeed, even writing it as an automatic sequence
requires an automaton with 6 states rather than the 5 states needed for a.

We discuss three possible applications of Theorems B and C as well as of the related estimates of
Gowers norms of automatic sequences. Firstly, they can be used to study subsequences of automatic
sequences along various sparse sequences. Secondly, they allow us to count solutions to linear equations
with variables taking values in automatic sets, that is, subsets of N0 whose characteristic functions are
automatic sequences. Lastly, they give a wide class of explicit examples of sequences with small Gowers
norms of all orders. We will address these points independently.
We start by discussing the treatment of automatic sequences along primes by the third author to
highlight the usefulness of a structural result as in Theorem B. In [Mül17] a similar decomposition was
used (with the uniform component satisfying a weaker property (called the Fourier-Property in [ADM]),
which is almost the same as being Gowers uniform of order 1) together with the so called carry Property
(see already [MR15] and a more general form in [Mül18]). This essentially allows one to reduce the
problem to the case of structured and uniform sequences. The structured component is very simple to
deal with, as it suffices to study primes in arithmetic progressions. The study of the uniform component
followed the method of Mauduit and Rivat developed to treat the Rudin–Shapiro sequence along primes
[MR15]. A similar approach was used by Adamczewski, Drmota and the third author to study the
occurrences of digits in automatic sequences along squares [ADM]. It seems likely that a higher-order
uniformity as in Theorem B might allow one to study the occurrences of blocks in automatic sequences
along squares (see for example [DMR13, Mül18] for related results).
Recently, Spiegelhofer used the fact that the Thue–Morse sequence is highly Gowers uniform to
show that the level of distribution of the Thue–Morse sequence is 1 [Spi18]. As a result, he proves
that the sequence is simply normal along ⌊nc⌋ for 1 < c < 2, i.e. the asymptotic frequency of both 0
and 1 in the Thue–Morse sequence along ⌊nc⌋ is 1/2. This result, together with our structural result
(Theorem B) indicates a possible approach to studying automatic sequences produced by strongly
connected, prolongable automata along ⌊nc⌋. As the structured component is rationally almost periodic,
we can simply study ⌊nc⌋ mod m to deal with the first component. The uniform component needs to
be dealt with similarly to Spiegelhofer’s treatment of the Thue–Morse sequence, but conditioned on
⌊nc⌋ mod m, to take care of the structured component at the same time. For the possible treatment of
all the subsequences of automatic sequences discussed above it is essential to have (for the uniform

DISCRETE ANALYSIS, 2023:4, 62pp. 5

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

component) both some sort of Gowers uniformity as well as the carry Property. Both these properties
are guaranteed by the decomposition used in this paper, while the Arithmetic Regularity Lemma cannot
guarantee the carry Property for the uniform component.
Secondly, let us recall one of the many formulations of the celebrated theorem of Szemerédi on arith-
metic progressions which says that any set A ⊂ N0 with positive upper density d(A) = lim supN→∞ |A ∩ [N]| /N >
0 contains arbitrarily long arithmetic progressions. It is natural to ask what number of such progressions
are guaranteed to exist in A ∩ [N], depending on the length N and the density of A.
Following the work of Bergelson, Host and Kra (and Ruzsa) [BHK05], Green and Tao [GT10a]
showed that for progressions of length ≤ 4, the count of d-term arithmetic progressions in a subset A ⊂ [N]
is essentially greater than or equal to what one would expect for a random set of similar magnitude.

Theorem 1.4. Let 2 ≤ l ≤ 4, α > 0 and ε > 0. Then for any N ≥ 1 and any A ⊂ [N] of density |A| /N ≥ α
there exist ≫α,ε N values of m ∈ [N] such that A contains ≥ (α l − ε)N l-term arithmetic progressions
with common difference m. The analogous statement is false for any l ≥ 5.

For automatic sets, the situation is much simpler: Regardless of the length l ≥ 1, the count of l-term
arithmetic progressions in A ∩ [N] is, up to a small error, at least what one would expect for a random set.

Theorem D. Let l ≥ 3, and let A be an automatic set (that is, a subset of N0 whose characteristic
sequence is automatic). Then there exists C = Ol,A(1) such that for any N ≥ 1 and ε > 0 there exist
≫l,A εCN values of m ∈ [N] such that A ∩ [N] contains ≥ (α l − ε)N l-term arithmetic progressions with
common difference m, where α = |A| /N.

Thirdly, we remark that there are few examples of sequences that are simultaneously known to be
highly Gowers uniform and given by a natural, explicit formula. Polynomial phases e(p(n)) (p ∈ R[x])
are standard examples of sequences that are uniform of order deg p − 1 but dramatically non-uniform of
order deg p. Random sequences are highly uniform (cf. [TV06, Ex. 11.1.17]) but are not explicit. As
already mentioned, many multiplicative sequences are known to be Gowers uniform of all orders, but
with considerably worse bounds than the power saving which we obtain. For a similar result for a much
simpler class of q-multiplicative sequences, see [FK19]. Examples of highly Gowers uniform sequences
of number-theoretic origin in finite fields of prime order were found in [FKM13]; see also [Liu11] and
[NR09] where Gowers uniformity of certain sequences is derived from much stronger discorrelation
estimates.

2 Gowers norms

2.1 Notation

We use standard asymptotic notation — if f and g are two functions defined on (sufficiently large) positive
integers, we write f ≪ g or f = O(g) if there exists a constant C > 0 such that | f (n)| ≤ C|g(n)| for all
sufficiently large n. If the constant C is allowed to depend on some extra parameters (α, ε, etc.), we may
specify that by writing f ≪α,ε g or f = Oα,ε (g). In some cases when such dependence is clear from the
context, we may omit such indices (this is the case for example for the order d of Gowers uniformity
norms, defined below).
 DISCRETE ANALYSIS, 2023:4, 62pp. 6

GOWERS NORMS FOR AUTOMATIC SEQUENCES

We also use the Iverson bracket notation JPK for the value of a logical statement P, that is,

JPK =
 {
1 if P is true;
0 otherwise.

2.2 Basic facts and definitions

Gowers norms, originally introduced by Gowers in his work on Szemerédi’s theorem [Gow01], are a
fundamental object in what came to be known as higher order Fourier analysis. For extensive background,
we refer to [Gre] or [Tao12]. Here, we just list several basic facts. Throughout, we treat d (see below) as
fixed unless explicitly stated otherwise, and allow all implicit error terms to depend on d.
For a finite abelian group G and an integer d ≥ 1, the Gowers uniformity norm on G of order d is
defined for f : G → C by the formula

∥ f ∥2d
U d (G) = E
⃗n∈Gd+1 ∏
⃗ω∈{0,1}d C |⃗ω| f (1⃗ω ·⃗n), (6)

where C denotes the complex conjugation, ⃗ω and ⃗n are shorthands for (ω1, . . . , ωd) and (n0, n1, . . . , nd),
respectively, |⃗ω| = |{i ≤ d | ωi = 1}|, and 1⃗ω ·⃗n = n0 + ∑
d
i=1 ωini. More generally, for a family of
functions f⃗ω : G → C with ⃗ω ∈ {0, 1}d we can define the corresponding Gowers product
〈
( f⃗ω )⃗ω∈{0,1}d 〉

U d (G) = E
⃗n∈Gd+1 ∏
⃗ω∈{0,1}d C |⃗ω| f⃗ω (1⃗ω ·⃗n). (7)

A simple computation shows that ∥ f ∥U 1(G) = |En∈G f (n)| and

∥ f ∥
4
U 2(G) = E
n,m,l∈G f (n) ¯f (n + m) ¯f (n + l) f (n + m + l) = ∑
ξ ∈ ˆG
 ∣
∣ ˆf (ξ )
∣
∣4 ,

where ˆG is the group of characters G → S1 and ˆf (ξ ) = En∈G ¯ξ (n) f (n).
One can show that definition (6) is well-posed in the sense that the right hand side of (6) is real and
non-negative. If d ≥ 2, then ∥·∥U d (G) is indeed a norm, meaning that it obeys the triangle inequality
∥ f + g∥U d (G) ≤ ∥ f ∥U d (G) + ∥g∥U d (G), is positive definite in the sense that ∥ f ∥U d (G) ≥ 0 with equality
if only if f = 0, and is homogeneous in the sense that ∥λ f ∥U d (G) = |λ | ∥ f ∥U d (G) for all λ ∈ C. If
d = 1, then ∥·∥U d (G) is only a seminorm. Additionally, for any d ≥ 1 we have the nesting property
∥ f ∥U d (G) ≤ ∥ f ∥U d+1(G).
In this paper we are primarily interested in the uniformity norms on the interval [N], where N ≥ 1 is
an integer. Any such interval can be identified with the subset [N] = {0, 1, . . . , N − 1} of a cyclic group
Z/ ̃NZ, where ̃N is an integer significantly larger than N. For d ≥ 1 and f : [N] → C we put

∥ f ∥U d [N] = ∥
∥1[N] f ∥
∥
U d (Z/ ̃NZ) / ∥
∥1[N]∥
∥
U d (Z/ ̃NZ) . (8)

The value of ∥ f ∥U d [N] given by (8) is independent of ̃N as long as ̃N exceeds 2dN, and for the sake of

concreteness we let ̃N = ̃N(N, d) be the least prime larger than 2dN (the primality assumption will make

DISCRETE ANALYSIS, 2023:4, 62pp. 7

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

Fourier analysis considerations slightly easier at a later point). As a consequence of the corresponding
properties for cyclic groups, ∥·∥U d [N] is a norm for all d ≥ 2 and a seminorm for d = 1, and for all d ≥ 1
we have a slightly weaker nesting property ∥ f ∥U d [N] ≪d ∥ f ∥U d+1[N].
Definition (8) can equivalently be expressed as

∥ f ∥2d
U d (G) = E
⃗n∈Π(N) ∏
⃗ω∈{0,1}d C |⃗ω| f (1⃗ω ·⃗n), (9)

where the average is taken over the set (implicitly dependent on d)

Π(N) = {
⃗n ∈ Z
d+1 ∣
∣ 1⃗ω ·⃗n ∈ [N] for all ⃗ω ∈ {0, 1}d} . (10)

As a direct consequence of (9), we have the following phase-invariance: If p ∈ R[x] is a polynomial of
degree < d and g : [N] → C is given by g(n) = e(p(n)), then ∥ f ∥U d [N] = ∥ f · g∥U d [N] for all f : [N] → C.
(Here and elsewhere, e(t) = exp(2πit).) In particular, ∥g∥U d [N] = 1. The analogous statement is also true
for finite cyclic abelian groups. In particular, if p ∈ Z[x] is a polynomial of degree < d and g : Z/NZ → C
is given by g(n) = e(p(n)/N), then ∥ f ∥U d (Z/NZ) = ∥ f · g∥U d (Z/NZ) for all f : Z/NZ → C.
We will say that a bounded sequence a : N0 → C is uniform of order d ≥ 1 if ∥a∥U d [N] → 0 as N → ∞.
The interest in Gowers norms stems largely from the fact that uniform sequences behave much like
random sequences in terms of counting additive patterns. To make this intuition precise, for a (d + 1)-
tuple of sequences f0, f1, . . . , fd : N0 → C let us consider the corresponding weighted count of arithmetic
progressions
 Λ
N
d ( f0, . . . , fd) = ∑
n,m∈Z
 d
∏
i=0( fi1[N])(n + im),

so that in particular ΛN
d (1A, . . . , 1A) is the number of arithmetic progressions of length d +1 in A∩[N]. The
following proposition is an easy variant of the generalised von Neumann theorem, see for example [Tao12,
Exercise 1.3.23] We say that a function f : X → C is 1-bounded if | f (x)| ≤ 1 for all x ∈ X.

Proposition 2.1. Let d ≥ 1 and let f0, f1, . . . , fd : N0 → C be 1-bounded sequences. Then

ΛN
d ( f0, . . . , fd) ≪ N2 min
0≤i≤d ∥ fi∥U d [N] .

As a direct consequence, if fi, gi : N0 → C are 1-bounded and ∥ fi − gi∥U d [N] ≤ ε for all 0 ≤ i ≤ d,
then Λ
N
d ( f0, . . . , fd) = ΛN
d (g0, . . . , gd) + O(εN2).

In particular, if A ⊂ N0 has positive asymptotic density α and 1A − α1N0 is uniform of order d, then the
count of (d + 1)-term arithmetic progressions in A ∩ [N] is asymptotically the same as it would be if A
was a random set with density α.
It is often helpful to control Gowers norms by other norms which are potentially easier to understand.
We equip [N] with the normalised counting measure, whence ∥ f ∥Lp([N]) = (En<N | f (n)|p)
1/p. The
following bound is a consequence of Young’s inequality (see e.g. [ET12] for a derivation).

Proposition 2.2. Let d ≥ 1 and pd = 2d/(d + 1). Then ∥ f ∥U d [N] ≪ ∥ f ∥Lpd ([N]) for any f : [N] → C.

DISCRETE ANALYSIS, 2023:4, 62pp. 8

GOWERS NORMS FOR AUTOMATIC SEQUENCES

2.3 Fourier analysis and reductions

We will use some simple Fourier analysis on finite cyclic groups Z/NZ. We equip Z/NZ with the
normalised counting measure and its dual group ̂Z/NZ (which is isomorphic to Z/NZ) with the counting
measure. With these conventions, the Plancherel theorem asserts that for f : Z/NZ → C we have

E
n∈Z/NZ | f (n)|
2 = ∥ f ∥
2
L2(Z/NZ) = ∥
∥ ˆf ∥
∥2
ℓ2(Z/NZ) = ∑
ξ ∈Z/NZ
 ∣
∣ ˆf (ξ )
∣
∣2 ,

where ˆf (ξ ) = En∈Z/NZ f (n)e(−ξ n/N). Recall also that for f , g : Z/NZ → C we have ̂f ∗ g = ˆf · ˆg where
f ∗ g(n) = Em∈Z/NZ f (m)g(n − m).
The following lemma will allow us to approximate characteristic functions of arithmetic progressions
with smooth functions. While much more precise variants exist (cf. Erd˝os–Turán inequality), this basic
result will be sufficient for the applications we have in mind. We say that a set P ⊂ Z/NZ is an arithmetic
progression of length M if |P| = M and P takes the form {am + b | m ∈ [M]} with a, b ∈ Z/NZ.

Lemma 2.3. Let N be prime and let P ⊂ Z/NZ be an arithmetic progression of length M ≤ N. Then for
any 0 < η ≤ 1 there exists a function f = fP,η : Z/NZ → [0, 1] such that

1. ∥ f − 1P∥Lp(Z/NZ) ≤ η 1/p for each 1 ≤ p < ∞;

2. ∥
∥ ˆf ∥
∥
ℓ1(Z/NZ) ≪ η −1/2.

Remark 2.4. We will usually take η = N−ε where ε > 0 is a small constant.

Proof. We pick f = 1P ∗ N
K 1a[K], where a is the common difference of the arithmetic progression and the
integer K ≥ 1 remains to be optimised. Note that f (n) ̸= 1P(n) for at most 2K values of n ∈ Z/NZ, and
| f (n) − 1P(n)| ≤ 1 for all n ∈ Z/NZ. Hence,

∥ f − 1P∥Lp ≤ (2K/N)
1/p .

Using the Cauchy–Schwarz inequality and Plancherel theorem we may also estimate
∥
∥ ˆf ∥
∥
ℓ1 = N
K
 ∥
∥ˆ1P · ˆ1a[K]∥
∥
ℓ1 ≤ N
K
 ∥
∥ˆ1P∥
∥
ℓ2 · ∥
∥ˆ1a[K]∥
∥
ℓ2

= N
K ∥1P∥L2 · ∥
∥1a[K]∥
∥
L2 ≤ (N/K)
1/2.

It remains to put K = max(⌊ηN/2⌋ , 1) and note that if K = 1, then f = 1P.

As a matter of general principle, the restriction of a Gowers uniform sequence to an arithmetic
progression is again Gowers uniform. We record the following consequence of Lemma (2.3) which makes
this intuition more precise.

Proposition 2.5. Let d ≥ 2 and αd = (d + 1)/(2d−1 + d + 1). Let a : [N] → C be a 1-bounded function
and let P ⊂ [N] be an arithmetic progression. Then

∥a1P∥U d [N] ≪ ∥a∥αd
U d [N] .

(Recall that we allow the implicit constants to depend on d.)

DISCRETE ANALYSIS, 2023:4, 62pp. 9

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

Proof. Throughout the argument we consider d as fixed and allow implicit error terms to depend on d.
Let ̃N = ̃N(N, d) be the prime with N < ̃N ≪ N defined in Section 2.2. Let η > 0 be a small parameter,
to be optimised in the course of the proof, and let f : Z/ ̃NZ → [0, 1] be the approximation of 1P such that

∥ f − 1P∥Lpd (Z/ ̃NZ) ≪ η 1/pd and ∥
∥ ˆf ∥
∥
ℓ1(Z/ ̃NZ) ≪ η −1/2,

whose existence is guaranteed by Lemma 2.3. (Recall that pd is defined in Proposition 2.2.) Using the
triangle inequality we can now estimate

∥a1P∥U d [N] ≪ ∥a1P∥U d (Z/ ̃NZ) = ∥
∥a ( f 1[N] + (1P − f )1[N])∥
∥
U d (Z/ ̃NZ)
≤ ∥
∥a f 1[N]∥
∥
U d (Z/ ̃NZ) + ∥
∥a(1P − f )1[N]∥
∥
U d (Z/ ̃NZ) .

We consider the two summands independently. For the first one, expanding f (n) = ∑ξ ˆf (ξ )e(ξ n/ ̃N)
and using phase-invariance of Gowers norms we obtain
∥
∥a f 1[N]∥
∥
U d (Z/ ̃NZ) ≤ ∥
∥ ˆf ∥
∥
ℓ1(Z/ ̃NZ) · ∥
∥a1[N]∥
∥
U d (Z/ ̃NZ) ≪ η −1/2 ∥a∥U d [N] .

For the second one, it follows from Proposition 2.2 that
∥
∥a(1P − f )1[N]∥
∥
U d (Z/ ̃NZ) ≪ ∥
∥a(1P − f )1[N]∥
∥
Lpd (Z/ ̃NZ)

≤ ∥1P − f ∥Lpd (Z/ ̃NZ) ≤ η 1/pd .

It remains to combine the two estimates and insert the near-optimal value η = ∥a∥1/(1/2+1/pd )
U d [N] .

We will use Proposition 2.5 multiple times to estimate Gowers norms of restrictions of uniform
sequences to sets which can be covered by few arithmetic progressions. For now, we record one immediate
consequence, which will simplify the task of showing that a given sequence is Gowers uniform by allowing
us to restrict our attention to uniformity norms on initial intervals whose length is a power of k.

Corollary 2.6. Let d ≥ 2 and k ≥ 2. Let a : N0 → C be a 1-bounded sequence, and suppose that

∥a∥U d [kL] ≪ k−cL as L → ∞ (11)

for a constant c > 0. Then ∥a∥U d [N] ≪k N−αd c as N → ∞. (12)

Proof. Let N be a large integer and put L = ⌈logk N⌉. We may then estimate

∥a∥U d [N] ≪ ∥
∥a1[N]∥
∥
U d [kL] ≪ ∥a∥
αd
U d [kL] .

Remark 2.7. The argument is not specific to powers of k. The same argument shows that to prove that
∥a∥U d [N] ≪ N−c, it suffices to check the same condition for an increasing sequence Ni where the quotients
Ni+1/Ni are bounded.
 DISCRETE ANALYSIS, 2023:4, 62pp. 10

GOWERS NORMS FOR AUTOMATIC SEQUENCES

3 Automatic sequences

3.1 Definitions

In this section we review the basic terminology concerning automatic sequences. Our general reference
for this material is [AS03]. To begin with, we introduce some notation concerning digital expansions.
For k ≥ 2, we let Σk = {0, 1, . . . , k-1} denote the set of digits in base k. For a set X we let X ∗ denote
the monoid of words over the alphabet X, with the operation of concatenation and the neutral element
being the empty word ε. In particular, Σ∗
k is the set of all possible expansions in base k (allowing leading
zeros). While formally Σk ⊂ N0, we use different fonts to distinguish between the digits 0, 1, 2 . . . and
numbers 0, 1, 2, . . . ; in particular 11 = 12 denotes the string of two 1s, while 11 = 10 + 1 denotes the
integer eleven. For a word w ∈ X ∗, we let |w| denote the length of the word w, that is, the number of
letters it contains, and we let wrev denote the word whose letters have been written in the opposite order
(for instance, 10110rev = 01101).
For an integer n ∈ N0, the expansion of n in base k without leading zeros is denoted by (n)k ∈ Σ∗
k (in
particular (0)k = ε). Conversely, for a word w ∈ Σ∗
k the corresponding integer is denoted by [w]k. We
also let lengthk(n) = |(n)k| be the length of the expansion of n (in particular lengthk(0) = 0).
Leading zeros are a frequent source of technical inconveniences, the root of which is the fact that
we cannot completely identify N0 with Σ∗
k. This motivates us to introduce another piece of notation. For
n ∈ N0 we let (n)l
k ∈ Σl
k denote the expansion of n in base k truncated or padded with leading zeros to
length l, that is, (n)l
k is the suffix of the infinite word 0∞(n)k of length l (for example, (43)8
2 = 00101011
and (43)4
2 = 1011).
A (deterministic finite) k-automaton without output A = (S, s0, Σk, δ ) consists of the following data:

• a finite set of states S with a distinguished initial state s0;

• a transition function δ : S × Σk → S.

A (deterministic finite) k-automaton with output A = (S, s0, Σk, δ , Ω, τ) additionally includes

• an output function τ : S → Ω taking values in an output set Ω.

By an automaton we mean a k-automaton for some unspecified k ≥ 2. By default, all automata are
deterministic, finite and with output. When we refer to automata without output, we say so explicitly.
The transition map δ : S ×Σk → S extends naturally to a map (denoted by the same letter) δ : S ×Σ∗
k →
S so that δ (s, uv) = δ (δ (s, u), v). If A = (S, s0, Σk, δ , Ω, τ) is an automaton with output, then aA denotes
the automatic sequence produced by A, which is defined by the formula a(n) = τ(δ (s0, (n)k)). More
generally, for s ∈ S, aA,s denotes the automatic sequence produced by (S, s, Σk, δ , Ω, τ); if A is clear
from the context, we simply write as. A sequence a : N0 → Ω is k-automatic if it is produced by some
k-automaton.
We say that an automaton (with or without output) with initial state s0 and transition function δ is
prolongable (or ignores the leading zeros) if δ (s0, 0) = s0. Any automatic sequence can be produced by
an automaton ignoring leading zeros. We call an automaton A idempotent if it ignores the leading zeros
and δ (s, 00) = δ (s, 0) for each s ∈ S, that is, if the map δ (·, 0) : S → S is idempotent.

DISCRETE ANALYSIS, 2023:4, 62pp. 11

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

Note that with the above definitions, automata read input forwards, that is, starting with the most
significant digit. One can also consider the opposite definition, where the input is read backwards, starting
from the least significant digit, that is, arev
A (n) = τ (
δ (s0, (n)rev
k )
)
. The class of sequences produced by
automata reading input forwards is precisely the same as the class of sequences produced by automata
reading input backwards. However, the two concepts lead to different classes of sequences if we impose
additional assumptions on the automata, such as synchronisation.
An automaton A is synchronising if there exists a synchronising word w ∈ Σ∗
k, that is, a word w such
that the value of δ (s, w) does not depend on the state s ∈ S. Note that a synchronising word is by no
means unique; indeed, any word w′ containing a synchronising word as a factor is itself synchronising. As
a consequence, if A is synchronising then the number of words w ∈ Σl
k that are not synchronising for A is
≪ kl(1−c) for some constant c > 0. An automatic sequence is forwards (resp. backwards) synchronising
if it is produced by a synchronising automaton reading input forwards (resp. backwards).
An automaton A is invertible if for each j ∈ Σk the map δ (·, j) : S → S is bijective and additionally
δ (·, 0) = idS. A sequence is invertible if it is produced by an invertible automaton (reading input forwards).
One can show that reading input backwards leads to the same notion, but we do not need this fact. Any
invertible sequence is a coding of a generalised Thue–Morse sequence, meaning that there exists a group
G and group elements idG = g0, g1, . . . , gk−1 such that the sequence is produced by an automaton with
S = G, s0 = eG and δ (s, j) = sg j for each j ∈ Σk [DM12].
A state s in an automaton A is reachable if δ (s0, w) = s for some w ∈ Σ∗
k. Unreachable states in an
automaton are usually irrelevant, as we may remove them from the automaton without changing the
automatic sequence produced by it. We call two distinct states s, s′ ∈ S satisfying τ(δ (s, v)) = τ(δ (s′, v))
for all v ∈ Σ∗
k nondistinguishable. One sees directly, that we could merge them (preserving outgoing
arrows of one of the states) and still obtain a well-defined automaton producing a and having a smaller
number of states. This leads us to the definition of a minimal automaton, i.e. an automaton with no
unreachable states and no nondistinguishable states. It is classical, that for any automatic sequence there
exists a minimal automaton producing that sequence (see for example [AS03, Corollary 4.1.9]).
An automaton A is strongly connected if for any two states s, s′ of A there exists w ∈ Σ∗
k with
δ (s, w) = s′. A strongly connected component of A is a strongly connected automaton A′ whose set of
states S′ in a subset of S and whose transition function δ ′ is the restriction of the transition function δ of
A; we often identify A′ with S′. The following observation is standard, but we include the proof for the
convenience of the reader.

Lemma 3.1. Let A be an automaton, as introduced above. Then there exists a word w ∈ Σ∗
k such that
if v ∈ Σ∗
k contains w as a factor then for every state s of A, δ (s, v) belongs to a strongly connected
component of A.

Proof. Let S = {s0, s1, . . . , sN−1} be an enumeration of S. We construct inductively a sequence of words
ε = w0, . . . , wN, with the property that δ (si, w j) belongs to a strongly connected component for any
0 ≤ i < j ≤ N. Once w j has been constructed, it is enough to define w j+1 = w ju, where u ∈ Σ∗
k is an
arbitrary word such that δ (δ (s j, w j), u) belong to a strongly connected component, which is possible
since from any state there exists a path leading to a strongly connected component.

We can consider k-automata with or without output as a category. A morphism between automata
without output A = (S, s0, Σk, δ ) and A = (S′, s′
0, Σk, δ ′) is a map φ : S → S′ such that φ (s0) = s′
0 and

DISCRETE ANALYSIS, 2023:4, 62pp. 12

GOWERS NORMS FOR AUTOMATIC SEQUENCES

φ (δ (s, j)) = δ ′(φ (s), j) for all s ∈ S and j ∈ Σk. A morphism between automata with output A =
(S, s0, Σk, δ , Ω, τ) and A′ = (S′, s′
0, Σk, δ ′, Ω′, τ ′) is a pair (φ , σ ) where φ is a morphism between the
underlying automata without output and σ : Ω → Ω′ is a map such that σ (τ(s)) = τ ′(φ (s)). In the
situation above, aA′ is the image of aA via a coding, that is, aA′(n) = σ (aA(n)) for all n ∈ N0. While
this—perhaps overly abstract—terminology is not strictly speaking needed for our purposes, it will be
helpful at a later point when we consider morphisms between group extensions of automata.

3.2 Change of base

A sequence a : N0 → Ω is eventually periodic if there exists n0 ≥ 0 and d ≥ 1 such that a(n + d) = a(n)
for all n ≥ n0. Two integers k, k′ ≥ 2 are multiplicatively independent if log(k)/ log(k′) is irrational. A
classical theorem of Cobham asserts that if k, k′ ≥ 2 are two multiplicatively independent integers, then
the only sequences which are both k- and k′-automatic are the eventually periodic ones, and those are
automatic in all bases. On the other hand, if k, k′ ≥ 2 are multiplicatively dependent, meaning that k = kl
0
and k′ = kl′
0 for some integers k0, l, l′ ≥ 1, then the classes of k-automatic and k′-automatic sequences
coincide.
Hence, when we work with a given automatic sequence that is not ultimately periodic, the base
(denoted by k) is determined uniquely up to the possibility to replace it by its power k′ = kt, t ∈ Q. We
will take advantage of this possibility, which is useful because some of the properties discussed above
(specifically synchronisation and idempotence) depend on the choice of base. We devote the remainder of
this section to recording how various properties of automatic sequences behave when the base is changed.
An instructive example to keep in mind is that n ↦→ length2(n) mod 2 is backwards synchronising in base
4 but not in base 2 (see Proposition 3.3 for details).
We first briefly address the issue of idempotency. Any automatic sequence is produced by an
idempotent automaton, possibly after a change of basis [BK19b, Lem. 2.2]. Additionally, if the sequence
aA is produced by the automaton A = (S, s0, Σk, δ , Ω, τ) then for any power k′ = kl, l ∈ N, there is a
natural construction of a k′-automaton A′ which produces the same sequence aA′ = aA and is idempotent.
We next consider synchronising sequences. The following lemma provides a convenient criterion for
a sequence to be synchronising.

Lemma 3.2. Let a : N0 → Ω be a k-automatic sequence and let w ∈ Σ∗
k. Then the following conditions
are equivalent:

1. the sequence a is produced by a k-automaton A reading input forwards (resp. backwards) for
which w is synchronising;

2. there exists a map b : Σ∗
k → Ω such that for any u, v ∈ Σ∗
k we have a([uwv]k) = b(v) (resp.
a([uwv]k) = b(u)).

Proof. For the sake of clarity we only consider the “forward” variant; the “backward” case is fully
analogous. It is clear that (1) implies (2), so it remains to prove the reverse implication. Let A be a
minimal k-automaton which produces a. We will show that if w satisfies (2) then it is synchronising for
A.
 DISCRETE ANALYSIS, 2023:4, 62pp. 13

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

Let s, s′ ∈ S be any two states. Pick u, u′ such that s = δ (s0, u) and s′ = δ (s0, u′). Since

τ(δ (s, wv)) = a([uwv]k) = b(v) = a([u
′wv]k) = τ(δ (s′, wv))

for any v, w ∈ Σ∗
k, we get that τ(δ (δ (s, w), v)) = τ(δ (δ (s′, w), v)) for all v ∈ Σ∗
k. This implies by
minimality of A that δ (s, w) = δ (s′, w). Thus, we have showed that the word w is synchronising.

As a consequence, we obtain a good understanding of how a change of base affects the property of
being synchronising.

Proposition 3.3. Let a : N0 → Ω be a k-automatic sequence and let l ∈ N.

1. If a is forwards (resp. backwards) synchronising as a k-automatic sequence, then a is also forwards
(resp. backwards) synchronising as a kl-automatic sequence.

2. If a is forwards synchronising as a kl-automatic sequence, then a is also forwards synchronising
as a k-automatic sequence.

3. If l ≥ 2 then there exist backwards synchronising kl-automatic sequences which are not backwards
synchronising as k-automatic sequences.

Proof. 1. Let w ∈ Σ∗
k be a synchronising word for a k-automaton producing a. Replacing w with a
longer word if necessary, we may assume without loss of generality that the length of w is divisible by l.
Hence, we may identify w with an element of Σ∗
kl ≃ (
Σl
k)∗ in a natural way. It follows from Lemma 3.2
that w is a synchronising word for a kl-automaton producing a.

2. Let w ∈ Σ∗
kl ≃ (
Σl
k)∗ be a synchronising word for a kl-automaton which produces a and consider
the word w′ = (w0)l ∈ Σ∗
k. This is set up so that if the expansion (n)k of an integer n ≥ 0 contains w′ as a
factor then (n)kl contains w as a factor. It follows from Lemma 3.2 that w′ is a synchronising word for a
k-automaton producing a.

3. Consider the sequence b(n) = lengthk(n) mod l. In base kl, the value of b(n) depends only on the
leading digit of n, whence b is backwards synchronising. On the other hand, b([v]k) ̸= b([v0]k) for all
v ∈ Σ∗
k with [v]k ̸= 0, whence b is not backwards synchronising as a k-automatic sequence.

4 Derivation of the main theorems

4.1 Strongly connected case

Having set up the relevant terminology in Sections 2 and 3, we are now ready to deduce our main results,
Theorems A, B, C and D from the following variant, applicable to strongly connected automata. We also
address the issue of uniqueness of the decomposition in Theorems B and C.
We say that a k-automatic sequence a : N0 → Ω is strongly structured if there exists a periodic
sequence aper : N0 → Ωper with period coprime to k, a forwards synchronising k-automatic sequence
afs : N0 → Ωfs, as well as a map F : Ωper × Ωfs → Ω such that

a(n) = F (
aper(n), afs(n)
) . (13)

DISCRETE ANALYSIS, 2023:4, 62pp. 14

GOWERS NORMS FOR AUTOMATIC SEQUENCES

Note that thanks to Proposition 3.3 this notion does not change upon replacing the base k by a multiplica-
tively dependent one.

Theorem 4.1. Let a : N0 → C be a k-automatic sequence produced by a strongly connected, prolongable
automaton. Then there exists a decomposition

a = astr + auni, (14)

where astr is strongly structured (cf. (13)) and auni is highly Gowers uniform (cf. (1)).

Note that the formulation of Theorem 4.1 is very reminiscent of Theorem B, except that the as-
sumptions on the structured part are different. Indeed, one is an almost immediate consequence of the
other.

Proof of Theorem B assuming Theorem 4.1. The only difficulty is to show that any forwards synchronis-
ing automatic sequence is rationally almost periodic. This is implicit in [DDM15], and showed in detail
in [BKPLR16, Proposition 3.4]. It follows that any strongly structured sequence is rationally almost
periodic.

The derivation of Theorem C is considerably longer, and involves reconstruction of an automatic
sequence produced by an arbitrary automaton from the automatic sequences produced by the strongly
connected components.

Proof of Theorem C assuming Theorem 4.1. Let a : N0 → C be an automatic sequence. We may assume
(changing the base if necessary) that a is produced by an idempotent automaton A = (S, s0, Σk, δ , C, τ)
with δ (s0, 0) = s0. Throughout the argument we consider A to be fixed and we do not track dependencies
of implicit error terms on A.
Let S0 denote the set of states s ∈ S which lie in some strongly connected component of S which also
satisfy δ (s, 0) = s (or, equivalently, δ (s′, 0) = s for some s′ ∈ S0). Note that each strongly connected
component of S contains a state in S0. For each s ∈ S0, the sequence as = aA,s is produced by a strongly
connected automaton, so it follows from Theorem 4.1 that there exists a decomposition

as = as,str + as,uni,

where as,str is strongly structured and as,uni is highly Gowers uniform. For s ∈ S0 let

as,str(n) = Fs (
as,per(n), as,fs(n)
)

be a representation of as,str as in (13). Let M be an integer coprime to k and divisible by the period of
as,per for each s ∈ S0 (for instance, the least common multiple of these periods). Let z ∈ Σ∗
k be a word that
is synchronising for as,fs for each s ∈ S0 (it can be obtained by concatenating synchronising words for all
strongly connected components of A).
We will also need a word y ∈ Σ∗
k with the property that if we run A on input which includes y as a
factor, we will visit a state from S0 at some point when the input read so far encodes an integer divisible
by M. More formally, we require that for each u ∈ Σ∗
k there exists a decomposition y = x1x2 such that
δ (s0, ux1) ∈ S0 and M | [ux1]k. The word y can be constructed as follows. Take a word y0 ∈ Σ∗
k with

DISCRETE ANALYSIS, 2023:4, 62pp. 15

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

the property that δ (s, y0) belongs to a strongly connected component for each s ∈ S, whose existence is
guaranteed by Lemma 3.1. Let A ≥ 1 be an integer that is multiplicatively rich enough that M | kA − 1,
and let B ≥ M − 1. Put y = y0(0A−11)B. Then, using notation above, we can take x1 = y0(0A−11)i, where
i ≡ −[uy0]l mod M.
For n ∈ N0 such that (n)k contains yz as a factor, fix the decomposition (n)k = unvn where δ (s0, un) ∈
S0, M | [un]k and un is the shortest possible subject to these constraints. Note that vn contains z as a
factor. Let Z ⊂ N0 be the set of those n for which (n)k does not contain yz as a factor, and for the sake of
completeness define un = vn = ♢ for n ∈ Z, where ♢ is a symbol not belonging to Σ∗
k. Note also that
there exists a constant γ > 0 such that |Z ∩ [N]| ≪ N1−γ .
We are now ready to identify the structured part of a, which is given by

astr(n) = ∑
s∈S0 Jδ (s0, un) = sK as,str(n). (15)

(If n ∈ Z, the statement δ (s0, un) = s is considered to be false by convention, whence in particular
astr(n) = 0; recall that Jδ (s0, un) = sK uses the Iverson bracket notation, that is, Jδ (s0, un) = sK equals 1
if δ (s0, un) = s, and equals 0 otherwise.) The uniform part is now necessarily given by auni = a − astr. It
remains to show that astr and auni are strongly structured and highly Gowers uniform, respectively (note
that strongly structured sequences are necessarily automatic).
We begin with astr. For any s ∈ S0, we will show that n ↦→ Jδ (s0, un) = sK is a backwards synchronising
k-automatic sequence. This is most easily accomplished by describing a procedure which computes it. To
this end, we consider an automaton that mimics the behaviour of A, and additionally keeps track of the
remainder modulo M of the part of the input read so far. Next, we modify it so that if an arbitrary state s′

in S0 and residue 0 is reached, the output becomes fixed to Js′ = sK. The output for all remaining pairs of
states and residues are 0. More formally, we take A′ = (S × (Z/MZ), (s0, 0), Σk, δ ′, {0, 1}, τ ′)), where δ ′

is given by
 δ ′((r, i), j) =
 {
(δ (r, j), ki + j mod M) if i ̸= 0 or r ̸∈ S0,
(r, i) otherwise,

and the output function is given by

τ ′(r, i) =
 {
0 if i ̸= 0 or r ̸∈ S0,
Jr = sK otherwise.

It is clear that aA′ = Jδ (s0, un) = sK for all n ∈ N0. Additionally, since the output becomes constant
once we read yz, this procedure gives rise to a backwards synchronising sequence. Hence, each of
the summands in (15) is the product of a backwards synchronising sequence and a strongly structured
sequence. Moreover, we have by Lemma 3.2 that the cartesian product of forwards (backwards) synchro-
nizing k-automatic sequences is again a forwards (backwards) synchronizing k-automatic sequence. A
synchronizing word for the new automaton can be constructed by concatenating synchronizing words of
the individual automata. Thus, astr is weakly structured.
Next, let us consider auni. Thanks to Proposition 2.6, we only need to show that for any d ≥ 2 there
exists a constant c > 0 such that ∥auni∥U d [kL] ≪ k−cL. Fix a choice of d and let L be a large integer. If

DISCRETE ANALYSIS, 2023:4, 62pp. 16

GOWERS NORMS FOR AUTOMATIC SEQUENCES

n ∈ N0 \ Z and s = δ (s0, un), then

a(n) = a ([unvn]k) = as ([vn]k) = as,str([vn]k) + as,uni([vn]k)

= Fs (
as,per([vn]k), as,fs([vn]k)
) + as,uni([vn]k)

= Fs (
as,per(n), as,fs(n)
) + as,uni([vn]k) = as,str(n) + as,uni([vn]k),

where in the last line, we have used the fact M | [un]k and vn is synchronising for as,fs. Since astr(n) =
as,str(n), it follows that auni(n) = as,uni([vn]k).

For a word x ∈ Σ∗
k containing yz as a factor and integer l ≥ 0, consider the interval

P = {
[w]k ∣
∣ w ∈ xΣ
l
k} = [
[x]kkl, ([x]k + 1) kl) . (16)

Since un and |vn| are constant on P, it follows from Proposition 2.5 and the assumption that as,uni are
highly Gowers uniform that

∥auni1P∥U d [kL] = ∥as,uni1P∥U d [kL] ≪ max
s∈S0 ∥as,uni∥αd
U d [kL] ≪ k−c′L

for some constant 1 > c′ > 0, which does not depend on P. It remains to cover [kL] with a moderate
number of intervals P of the form (16) and a small remainder set.
Let η > 0 be a small parameter to be optimised in the course of the argument and let R be the set of
those n ∈ [kL] which are not contained in any progression P given by (16) with l ≥ (1 − η)L. Hence, if
n ∈ R then the word yz does not appear in the leading ⌊ηL⌋ digits of (n)L
k . It follows that |R| ≪ k−c′′
0 ηL

and consequently ∥auni1R∥U d [kL] ≪ ∥auni1R∥Lpd [kL] ≪ k−c′′ηL

by Proposition 2.2, where c′′
0 > 0 and c′′ = c′′
0/pd are constants. Each n ∈ [kL] \ R belongs to a unique
interval P given by (16) with l ≥ (1 − η)L and such that no proper suffix of x contains yz. There are
≤ kηL such intervals, corresponding to the possible choices of initial ⌊ηL⌋ digits of (n)L
k for n ∈ P. It
now follows from the triangle inequality that

∥auni∥U d [kL] ≤ ∥auni1R∥U d [kL] +∑
P ∥auni1P∥U d [kL] ≪ k−c′′ηL + k(η−c′)L.

It remains to pick η = c′/2, leading to ∥auni∥U d [kL] ≪ k−cηL with c = c′ min(c′′, 1)/2.

Finally, we record another reduction which will allow us to alter the initial state of the automaton in
the proof of Theorem 4.1. As the proof of the following result is very similar and somewhat simpler than
the proof of Theorem C discussed above, we skip some of the technical details. If fact, one could repeat
said argument directly, only replacing S0 with a smaller set (namely, a singleton); we do not pursue this
route because a simpler and more natural argument is possible.

Proposition 4.2. Let A = (S, s0, Σk, δ , Ω, τ) be a strongly connected, prolongable automaton and let
S0 ⊂ S be the set of s ∈ S such that δ (s, 0) = s. Then the following statements are equivalent:

DISCRETE ANALYSIS, 2023:4, 62pp. 17

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

1. Theorem 4.1 holds for aA,s for some s ∈ S0;

2. Theorem 4.1 holds for aA,s for all s ∈ S0.

Proof. It is clear that (2) implies (1). For the other implication, we may assume that Theorem 4.1 holds
for aA,s0 = aA. Hence, there exists a decomposition aA = astr + auni of aA as the sum of a strongly
structured and highly Gowers uniform sequence. Let

astr(n) = F (
aper(n), afs(n)
)

be a representation of astr as in (13).
Pick any s ∈ S0 and pick u ∈ Σ∗
k, not starting with 0 and such that δ (s0, u) = s, whence aA,s(n) =
aA([u(n)k]k) for all n ∈ N0. Since δ (s, 0) = s, we also have aA,s(n) = aA([u0m(n)k]k) for any m, n ∈ N0.
Let Q be a multiplicatively large integer, so that the period of aper divides kQ − 1, and put m(n) :=
Q − (lengthk(n) mod Q) ∈ {1, 2, . . . , Q}. For n ∈ N0 put

a
′
str(n) := astr([u0m(n)(n)k]k) and a
′
uni(n) := aA,s(n) − a′
str(n).

Clearly, aA,s = a′
str + a′
uni. Since the period of aper divides kQ − 1, for all n ∈ N0 we have

aper([u0m(n)(n)k]k) = aper(n + [u]k) (17)

Define the sequences a′
per and a′
fs by the formulas

a′
per(n) := aper([u0m(n)(n)k]k), a
′
fs(n) := afs([u0m(n)(n)k]k).

It follows from (17) that a′
per is periodic. Since the sequence m(n) is k-automatic, so is a′
fs. Indeed, in
order to compute a′
fs(n) it is enough to compute m(n) and afs([u0i(n)k]k) for 1 ≤ i ≤ Q. Since afs is
forwards synchronising, it follows from Lemma 3.2 that so is a′
fs. (Alternatively, one can also show that
a′
fs is automatic and forwards synchronising, by an easy modification of an automaton which computes
afs reading input from the least significant digit.) Since astr is given by

a′
str(n) = F (
a′
per(n), a′
fs(n)
) ,

it follows that a′
str is strongly structured. To see that a′
uni is highly Gowers uniform, we estimate the
Gowers norms ∥
∥a′
uni∥
∥
U d [kL] by covering [kL] with intervals P = [kl, kl+1) (0 ≤ l < L) and using Proposition

2.5 to estimate ∥
∥a′
uni1P∥
∥
U d [kL].

4.2 Uniqueness of decomposition

The structured automatic sequences we introduce in (4) and (13) are considerably easier to work with
than general automatic sequences (cf. the proof of Theorem D below). However, they are still somewhat
complicated and it is natural to ask if they can be replaced with a smaller class in the decompositions in
Theorems C and 4.1. Equivalently, one can ask if there exist any sequences which are structured in our
sense and highly Gowers uniform.
In this section we show that the weakly structured sequences defined in (4) are essentially the smallest
class of sequences for which Theorem C is true and that the decomposition in (14) is essentially unique.
As an application, we derive Theorem A as an easy consequence of Theorem C.

DISCRETE ANALYSIS, 2023:4, 62pp. 18

GOWERS NORMS FOR AUTOMATIC SEQUENCES

Lemma 4.3. Let a : N0 → C be a weakly structured k-automatic sequence such that

lim
N→∞
 ∣
∣
∣
∣ E
n<N a(n)b(n)
∣
∣
∣
∣ = 0 (18)

for any periodic sequence b : N0 → C. Then there exists a constant c > 0 such that

|{n < N | a(n) ̸= 0}| ≪ N1−c. (19)

Proof. Since a is weakly structured, we can represent it as

a(n) = F (
aper(n), afs(n), abs(n)
) , (20)

using the same notation as in (4). Let M be the period of aper. Pick any residue r ∈ Z/MZ and
synchronising words w, v ∈ Σ∗
k for afs, abs respectively. Assume additionally that w and v do not start with
0. Put x = aper(r) ∈ Ωper, y = afs([w]k) and z = abs([v]k). Our first goal is to show that F(x, y, z) = 0.
Let P be the infinite arithmetic progression

P = {n ∈ N0 | n mod M = r and (n)k ∈ Σ
∗
kw} . (21)

Since 1P is periodic, we have the estimate

N−1
∑
n=0 a(n)1P(n) = N−1
∑
n=0 F(x, y, abs(n))1P(n) = o(N) as N → ∞. (22)

Let L be a large integer an put N0 = [v]kkL and N1 = ([v]k + 1)kL. Applying the above estimate (22) with
N = N0, N1 we obtain
 N1−1
∑
n=N0 a(n)1P(n) = |[N0, N1) ∩ P| F(x, y, z) = o(kL) as L → ∞. (23)

This is only possible if F(x, y, z) = 0.
Since r, w, v were arbitrary, it follows that a(n) = 0 if (n)k is synchronising for both afs and abs.
The estimate (19) follows immediately from the estimate on the number of non-synchronising words,
discussed in Section 3.

Corollary 4.4. 1. If a : N0 → C is both structured and highly Gowers uniform then there exists a
constant c > 0 such that |{n < N | a(n) ̸= 0}| ≪ N1−c.

2. If a = astr + auni = a′
str + a′
uni are two decompositions of a sequence a : N0 → C as the sum of a
weakly structured part and a highly Gowers uniform part then there exists a constant c > 0 such that
{n < N | astr(n) ̸= a′
str(n)} ≪ N1−c.

Proof of Theorem A assuming Theorem C. Let a = astr + auni be the decomposition of a as the sum of a
weakly structured and a highly Gowers uniform part, whose existence is guaranteed by Theorem C. Then

lim sup
N→∞ E
n<N |astr(n)b(n)| = lim sup
N→∞ E
n<N |a(n)b(n)| = 0

for any periodic sequence b : N0 → C, for instance by Proposition 2.5. Hence, it follows from Lemma
4.3 that there exists c > 0 such that |{n < N | astr(n) ̸= 0}| ≪ N1−c. In particular, astr is highly Gowers
uniform, and hence so is a.
 DISCRETE ANALYSIS, 2023:4, 62pp. 19

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

Remark 4.5. Since there exist non-zero weakly structured sequences which vanish almost everywhere,
the decomposition in Theorem C is not quite unique. A prototypical example of such a sequence is the
Baum–Sweet sequence b(n), taking the value 1 if all maximal blocks of zeros in (n)2 have even length
and taking the value 0 otherwise. It seems plausible that with a more careful analysis one could make the
decomposition canonical. We do not pursue this issue further.

4.3 Combinatorial application

In this section we apply Theorem C to derive a result in additive combinatorics with a more direct appeal,
namely Theorem D. We will need the following variant of the generalised von Neumann theorem.

Lemma 4.6. Fix d ≥ 2. Let f0, f1, . . . , fd : [N] → C be 1-bounded sequences and let P ⊂ [N] be an
arithmetic progression. Then
∣
∣
∣
∣
∣ E
n,m<N
 d
∏
i=0(1[N] fi)(n + im)1P(m)

∣
∣
∣
∣
∣ ≪ min
0≤i≤d ∥ fi∥2/3
U d [N] .

Proof. This is essentially Lemma 4.2 in [GT10a]. Using Lemma 2.3 to decompose 1P into a sum of a
trigonometric polynomial and an error term small in the L1 norm, for any η > 0 we obtain the estimate
∣
∣
∣
∣
∣ E
n,m<N
 d
∏
i=0(1[N] fi)(n + im)1P(m)

∣
∣
∣
∣
∣ (24)

≪ (1/η)
1/2 sup
θ ∈R
 ∣
∣
∣
∣
∣ E
n,m<N
 d
∏
i=0(1[N] fi)(n + im)e(θ m)

∣
∣
∣
∣
∣ + η. (25)

Given θ ∈ R, put f ′
0(n) = e(−θ n) f0(n) and f ′
1(n) = e(θ n) f1(n), and f ′
i (n) = fi(n) for 1 < i ≤ d, so that
∥ fi∥U d [N] = ∥ f ′
i ∥U d [N] for all 0 ≤ i ≤ d and

d
∏
i=0(1[N] fi)(n + im)e(θ m) = d
∏
i=0(1[N] f ′
i )(n + im) for all n, m ∈ N0.

Applying [GT10a, Lemma 4.2] to f ′
i we conclude that

sup
θ ∈R
 ∣
∣
∣
∣
∣ E
n,m<N
 d
∏
i=0(1[N] fi)(n + im)e(θ m)

∣
∣
∣
∣
∣ ≪ min
0≤i≤d ∥ fi∥U d [N] . (26)

The claim now follows by optimising η.

Proof of Theorem D. Our argument follows a similar basic structure as the proof of Theorem 1.12 in
[GT10a], although it is considerably simpler. Throughout the argument, d = l − 1 ≥ 2 and the k-automatic
set A ⊂ N0 are fixed and all error terms are allowed to depend on d, k and A. We also let N denote a large
integer and put L = ⌈logk N⌉ and α = |A ∩ [N]| /N.
Let 1A = astr + auni be the decomposition given by Theorem C, and let c1 be the constant such that
∥auni∥U d [N] ≪ N−c1. Let M be the period of the periodic component aper of astr and let η > 0 be a small

DISCRETE ANALYSIS, 2023:4, 62pp. 20

GOWERS NORMS FOR AUTOMATIC SEQUENCES

parameter, to be optimised in the course of the argument. For notational convenience we additionally
assume that ηL is an integer. Consider the arithmetic progression

P = {
n < N ∣
∣
∣ n ≡ 0 mod M and (n)
L
k ∈ 0
ηLΣ
L−2ηL
k 0ηL} .

Note |P| /N ≫ N−2η and that the second condition is just another way of saying that n ≡ 0 mod kL and
n/kL < k−ηL. Our general goal is, roughly speaking, to show that many m ∈ P are common differences
of many (d + 1)-term arithmetic progressions in A ∩ [N]. Towards this end, we will estimate the average

E
m∈P E
n<N
 d
∏
i=0 1A∩[N](n + im). (27)

Substituting 1A∩[N] = 1[N](astr + auni) into (27) and expanding the product, we obtain the sum of 2d+1

expressions of the form
 E
m∈P E
n<N
 d
∏
i=0
 (
1[N]ai) (n + im), (28)

where ai = astr or ai = auni for each 0 ≤ i ≤ d. If ai = auni for at least one i then it follows from Lemma
4.6 that ∣
∣
∣
∣
∣ E
m∈P E
n<N
 d
∏
i=0
 (
1[N]ai) (n + im)

∣
∣
∣
∣
∣ ≪ N
|P| ∥auni∥
2/3 ≪ N2η−2c1/3. (29)

Inserting this into (27) we conclude that we may replace the function 1A∩[N] under the average with
1[N]astr at the cost of introducing a small error term:

E
m∈P E
n<N
 d
∏
i=0 1A∩[N](n + im) = E
m∈P E
n<N
 d
∏
i=0
 (
1[N]astr) (n + im) + O(N2η−2c1/3). (30)

Next, we will replace each of the terms (1[N]astr)(n + im) with (1[N]astr)(n) at the cost of introducing
another error term. If (1[N]astr)(n + im) ̸= (1[N]astr)(n) for some 0 ≤ i ≤ d, m ∈ P and n ∈ [N] then at
least one of the following holds:

1. either the words (n + im)L
k and (n)L
k differ at one of the first ηL/2 positions or n < N ≤ n + im;

2. the first ηL/2 digits of (n)L
k do not contain a synchronising word for the backward synchronising
component abs of astr;

3. the last ηL digits of (n)L
k do not contain a synchronising word for the forward synchronising afs
component of astr.

Indeed, if neither of these conditions held, the first ηL/2 digits of n and n + im would coincide,
as would their last ηL digits (because m ∈ P implies that the last ηL digits of m are zeros), and we
would have aper(n) = aper(n + im) (because m ∈ P implies that m is divisible by M, the period of aper);

DISCRETE ANALYSIS, 2023:4, 62pp. 21

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

moreover, we would have afs(n) = afs(n + im) (because the common last ηL digits of (n)L
k and (n + im)L
k
contain a synchronising word) and abs(n) = abs(n + im) (because the common first ηL/2 digits of (n)L
k
and (n + im)L
k contain a synchronising word). It would then follow that astr(n + im) = astr(n). Moreover,
the negation of condition (1) would guarantee that 1[N](n) = 1[N](n + im), contradicting our assumption
(1[N]astr)(n + im) ̸= (1[N]astr)(n).

If m ∈ P and n ∈ [N] are chosen uniformly at random then (1) holds with probability ≪ N−η/2, and
there exist constants cbs and cfs (dependent on the synchronising words for the respective components
of astr) such that (2) and (3) hold with probabilities ≪ N−cbsη and ≪ N−cfsη respectively. Letting
c2 = min (1/2, cbs, cfs) and using the union bound we conclude that

E
m∈P E
n<N
 d
∑
i=1
 q
(1[N]astr)(n + im) ̸= (1[N]astr)(n)
y ≪ N−c2η . (31)

Inserting (31) into (30) and removing the average over P we conclude that

E
m∈P E
n<N
 d
∏
i=0 1A∩[N](n + im) = E
n<N ad+1
str (n) + O(N2η−2c1/3 + N−c2η ). (32)

The main term in (32) can now be estimated using Hölder inequality:

E
n<N ad+1
str (n) ≥ ( E
n<N astr(n)
)d+1 ≥ α d+1 − O(N−c1), (33)

where in the last transition we use the fact that

E
n<N astr(n) = α − E
n<N auni(n) = α − O(N−c1).

Combining (32) and (33) and letting η be small enough that c2η < min (2c1/3 − 2η, c1), we obtain the
desired bound for the average (27):

E
m∈P E
n<N
 d
∏
i=0 1A∩[N](n + im) ≥ α d+1 − O(N−c2η ), (34)

Finally, applying a reverse Markov’s inequality to (34) we conclude that

E
m∈P
 t
 E
n<N
 d
∏
i=0 1A∩[N](n + im) ≥ α d+1 − ε
|
 ≥ ε − O(N−c2η ) (35)

for any ε > 0. Optimising the value of η for a given ε > 0 we conclude that there exists ≫ εCN values
of m such that
 E
n<N
 d
∏
i=0 1A∩[N](n + im) ≥ α d+1 − ε,

provided that ε > N−1/C for a certain constant C > 0 dependent on d, k and A. When ε < N−1/C, it is
enough to use m = 0.

Remark 4.7. The proof is phrased in terms which appear most natural when η is a constant and ε is a
small power of N. This choice is motivated by the fact that this case is the most difficult. However, the
theorem is valid for all ε in the range (N−1/C, 1), including the case when ε is constant as N → ∞.

DISCRETE ANALYSIS, 2023:4, 62pp. 22

GOWERS NORMS FOR AUTOMATIC SEQUENCES

4.4 Alternative line of attack

In this section we describe an alternative strategy one could try to employ in the proof of our main
theorems. Since this approach is possibly more natural, we find it interesting to see where the difficulties
arise and to speculate on how this hypothetical argument would differ from the one presented in the
remainder of the paper. As the material in this section is not used anywhere else and has purely
motivational purpose, we do not include all of the definitions (which the reader can find in [GT10a]) nor
do we prove all that we claim.
Let a : N0 → C be a sequence with |a(n)| ≤ 1 for all n ≥ 0. Fix d ≥ 1 and a small positive constant
ε > 0 and let also F : R>0 → R>0 denote a rapidly increasing sequence (its meaning will become apparent
in the course of the reasoning). The Arithmetic Regularity Lemma [GT10a] ensures that for each N > 0
there exists a parameter M = O(1) (allowed to depend on d, ε, F but not on N) and a decomposition

a(n) = astr(n) + asml(n) + auni(n), (n ∈ [N]), (36)

where astr, asml and auni : [N] → C are respectively structured, small and uniform in the following sense:

• astr(n) = F(g(n)Γ, n mod Q, n/N) where F is a function with Lipschitz norm ≤ M, Q is an integer
with 1 ≤ Q ≤ M, g : N0 → G/Γ is a (F(M), N)-irrational polynomial sequence of degree ≤ d − 1 and
complexity ≤ M, taking values in a nilmanifold G/Γ;

• ∥asml∥L2[N] ≤ ε;

• ∥auni∥U d [N] ≤ 1/F(M).

Note that F can always be replaced with a more rapidly increasing function and that definitions of many
terms related to astr are currently not provided. The decomposition depends on N, but for now we let N
denote a large integer and keep this dependence implicit.
Suppose now that a is additionally k-automatic. We can use the finiteness of the kernel of a to find
α ≥ 0 and 0 ≤ r < s < kα such that a(kα n + r) = a(kα n + s) for all n ≥ 0. For the sake of simplicity,
suppose that a stronger condition holds: for each q ∈ Z/QZ, there exist 0 ≤ r < s < kα as above with
r ≡ s ≡ q (mod Q). Define also N′ = N/kα and bstr(n) = astr(kα n + s) − astr(kα n + r) for all n ∈ [N′],
and accordingly for bsml and buni. Then bstr + bsml + buni = 0. In particular,

E
n<N′ |bstr(n)|
2 ≤ ∣
∣
∣
∣ E
n<N′ bsml(n)¯bstr(n)
∣
∣
∣
∣ + ∣
∣
∣
∣ E
n<N′ buni(n)¯bstr(n)
∣
∣
∣
∣ .

The first summand is O(ε) by Cauchy-Schwarz. It follows from the Direct Theorem for Gowers norms
that, as long as F increases fast enough (the required rate depends on ε), the second summand is ≤ ε.
Hence, E
n<N′ |astr(kα n + r) − astr(kα n + s)|
2 = E
n<N′ |bstr(n)|
2 = O(ε). (37)

Bearing in mind that kα n + r and kα n + s differ by a multiple of Q which is small compared to N, one
can hope to derive from (37) that for each q ∈ Z/QZ and each t ∈ [0, 1],

F(g(kα n + r)Γ, q,t) ≈ F(g(kα n + s)Γ, q,t), (n ∈ [N′]). (38)

DISCRETE ANALYSIS, 2023:4, 62pp. 23

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

(We intentionally leave vague the meaning of the symbol “≈”.) From here, it is likely that one could
show that F(x, n,t) is essentially constant with respect to x ∈ G/Γ. This could possibly be achieved by a
more sophisticated variant of the argument proving Theorem B in [BK19a]. For the sake of exposition,
let us rather optimistically suppose that F(x, n,t) = F(n,t) is entirely independent of x.
We are then left with the structured part taking the form astr(n) = F(n mod Q, n/N), which bears a
striking similarity to the definition of a weakly structured automatic sequence. Unfortunately, there is
no guarantee that astr produced by the Arithmetic Regularity Lemma is k-automatic (or that it can be
approximated with a k-automatic sequence in an appropriate sense). Ensuring k-automaticity of astr seems
to be a major source of difficulty. We note that (37) can be construed as approximate equality between
astr(kα n + r) and astr(kα n + s), which suggests (but does not prove) that astr should be approximately
equal to a k-automatic sequence a′
str.
If the line of reasoning outlined above succeeded, it would allow us to decompose an arbitrary
automatic sequence as the sum of a weakly structured automatic sequence and an error term, which is
small in an appropriate sense. However, it seems rather unlikely that this reasoning could give better
bounds on the error terms than the rather poor bounds provided by the Arithmetic Regularity Lemma.
Hence, in order to obtain the power saving, we are forced to argue along similar lines as in Section 6.
It is also worth noting that while the decomposition produced by our argument can be made explicit, it
is not clear how to extract an explicit decomposition from an approach using the Arithmetic Regularity
Lemma. Finally, our approach also ensures that the uniform component fulfills the carry Property, which
is essential to the possible applications discussed in Section 1, and which would be completely lost with
the use of the Arithmetic Regularity Lemma.

5 group extensions of automata

5.1 Definitions

In order to deal with automatic sequences more efficiently, we introduce the notion of a group extension
of an automaton.1 A group extension of a k-automaton without output (k-GEA) is a sextuple T =
(S, s0, Σk, δ , G, λ ) consisting of the following data:

• a finite set of states S with a distinguished initial state s0;

• a transition function δ : S × Σk → S;

• a labelling λ : S × Σk → G where (G, ·) is a finite group.

Note that T contains the data defining an automaton (S, s0, Σk, δ ) without output and additionally
associates group labels to each transition. Recall that the transition function δ extends naturally to a
map (denoted by the same letter) δ : S × Σ∗
k → S such that δ (s, vu) = δ (δ (s, v), u) for all u, v ∈ Σ∗
k. The
labelling function similarly extends to a map λ : S × Σ∗
k → G such that λ (s, vu) = λ (s, v) · λ (δ (s, v), u)

1This construction was called a (naturally induced) transducer in [Mül17], but this name seems better suited here. One main
motivation for this name is the fact that this construction corresponds to a group extension for the related dynamical systems, as
was shown in [LM18].
 DISCRETE ANALYSIS, 2023:4, 62pp. 24

GOWERS NORMS FOR AUTOMATIC SEQUENCES

for all u, v ∈ Σ∗
k. Thus, T can be construed as a means to relate a word w ∈ Σ∗
k to a pair consisting of the
state δ (s0, w) and the group element λ (s0, w).
A group extension of a k-automaton with output (k-GEAO) T = (S, s0, Σk, δ , G, λ , Ω, τ) additionally
includes

• an output function τ : S × G → Ω, where Ω is a finite set.

We use the term group extension of an automaton (GEA) to refer to a group extension of a k-automaton
where k is left unspecified. The term group extension of an automaton with output (GEAO) is used
accordingly.
Let T = (S, s0, Σk, δ , G, λ , Ω, τ) be a group extension of a k-automaton with output. Then T produces
the k-automatic map aT : Σ∗
k → Ω given by

aT (u) = τ (δ (s0, u), λ (s0, u)) , (39)

which in particular gives rise to the k-automatic sequence (denoted by the same symbol) aT : N0 → Ω
via the natural inclusion N0 ↪→ Σ∗
k, n ↦→ (n)k. Accordingly, we say that the GEA T produces a sequence
a : N0 → Ω if there exists a choice of the output function τ such that a = aT . More generally, to a pair
(s, h) ∈ S × G we associate the k-automatic sequence

aT ,s,h(u) = τ (δ (s, u), h · λ (s, u)) . (40)

If the GEA T is clear from the context, we omit it in the subscript. Note that with this terminology,
GEAs read input starting with the most significant digit. We could also define analogous concepts where
the input is read from the least significant digit, but these will not play a role in our reasoning.
A morhphism from T to another k-GEA T ′ = (S′, s′
0, Σk, δ ′, G′, λ ′) without output is a pair (φ , π)
where φ : S → S′ is a map and π : G → G′ is a morphism of groups obeying the following compatibility
conditions:

• φ (s0) = s′
0 and δ ′(φ (s), j) = φ (δ (s, j)) for all s ∈ S, j ∈ Σk;

• λ ′(φ (s), j) = π(λ (s, j)) for all s ∈ S, j ∈ Σk.

If φ and π are surjective, we will say that T ′ is a factor of T . A morphism from T to another group
extension of a k-automaton with output T ′ = (S′, s′
0, Σk, δ ′, G′, λ ′, Ω′, τ ′) is a triple (φ , π, σ ) where (φ , π)
is a morphism from T0 = (S, s0, Σk, δ , G, λ ) to T ′
0 = (S′, s′
0, Σk, δ ′, G′, λ ′) and σ : Ω → Ω′ is compatible
with (φ , π) in the sense that

• τ ′(φ (s), π(g)) = σ (τ(s, g)) for all s ∈ S, g ∈ G.

In the situation above the sequence aT ′ produced by T ′ is a coding of the sequence aT produced by T ,
that is, aT ′(n) = σ ◦ aT (n).
We say that a GEA T (with or without output) is strongly connected if the underlying automaton
without output A = (S, s0, Σk, δ ) is strongly connected. The situation is slightly more complicated
for synchronisation. We say that a word w ∈ Σ∗
k synchronises T to a state s ∈ S if δ (s′, w) = s and
λ (s′, w) = idG for each s′ ∈ S, and that T is synchronising if it has a word that synchronises it to the state

DISCRETE ANALYSIS, 2023:4, 62pp. 25

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

s0.2 (This is different than terminology used in [Mül17].) Note that if T is synchronising then so is the
underlying automaton but not vice versa, and that even if T is strongly connected and synchronising
there is no guarantee that all states s ∈ S have a synchronising word. We also say that T (or T ) is
prolongable if δ (s0, 0) = s0 and λ (s0, 0) = idG. Finally, T is idempotent if it ignores the leading zeros
and δ (s, 0) = δ (s, 00) and λ (s, 00) = λ (s, 0) for all s ∈ S.
As alluded to above, the sequence aT produced by the GEAO T is k-automatic. More explicitly, the
GEAO T = (S, s0, Σk, δ , G, λ , Ω, τ) gives rise to the automaton AT = (S′, s′
0, Σk, δ ′, Ω, τ) where S′ = S ×
G, s′
0 = (s0, idG) and δ ′((s, g), j) = (δ (s, j), g·λ (s, j)). Conversely, any automaton A = (S, s0, Σk, δ , Ω, τ)
can be identified with a GEAO TA = (S, s0, Σk, δ , {id}, λid, Ω, τ ′) with trivial group, λid(s, j) = id and
τ ′(s, id) = τ(s). At the opposite extreme, any invertible automaton A can be identified with a GEAO
T inv
A = ({s′
0}, s′
0, Σk, δ ′
0, Sym(S), λ , Ω, τ ′) with trivial state set where δ ′
0(s′
0, j) = s′
0, λ (s′
0, j) = δ (·, j) and
τ ′(s′
0, g) = τ(g(s0)). Accordingly, we will call any GEAO (or GEA) with a single state invertible and we
omit the state set from its description: any invertible GEAO is fully described by the data (G, λ , Ω, τ).

Example 5.1. The Rudin–Shapiro sequence r(n) is given recursively by r(0) = +1 and r(2n) = r(n),
r(2n + 1) = (−1)nr(n). It is produced by the following 2-automaton:

s00start
 s01 s11

s10

1

1 10 0
1
 00

where s00 is the initial state, an edge labelled j from s to s′ is present if δ (s, j) = s′ and the output function
is given by τ(s00) = τ(s01) = +1 and τ(s10) = τ(s11) = −1. Alternatively, r is produced by the GEAO
with group G = {+1, −1}, given by
 s0start
 s1

1/+ 0/+
 0/+

1/−

where s0 is the initial state, edge labelled j/± from s to s′ is present if δ (s, j) = s′ and λ (s, j) = ±1,
and the output function is given by τ(s, g) = g. This is an example of an efficient GEAO, which will be
defined shortly.

2It is not common to require a synchronizing word to a specific state, but this will not be a serious restriction for this paper.

DISCRETE ANALYSIS, 2023:4, 62pp. 26

GOWERS NORMS FOR AUTOMATIC SEQUENCES

Example 5.2. Recall the sequence a(n) defined in Example 1.2. It is produced by the GEAO with group
G = {+1, −1}, given by
 s0,2start
 s1,3

1/+ 0/+
1/−
 0/+

where we use the same conventions as in Example 5.1 above and the output is

τ(s0,2, +1) = 4, τ(s0,2, −1) = 2,

τ(s1,3, +1) = 1, τ(s1,3, −1) = 1.

Example 5.3. We also present a GEAO that produces the sequence a(n) defined in Example 1.3. The
group is given by the symmetric group on 3 elements Sym(3), where we use the cyclic notation to denote
the permutations.
 s0,1,2start
 s3,4,2
 0/(12)

1/(23)
0/(12)
1/id

The output is given by

τ(s0,1,2, id) = τ(s0,1,2, (23)) = 1, τ(s3,4,2, id) = τ(s3,4,2, (23)) = 4,

τ(s0,1,2, (12)) = τ(s0,1,2, (132)) = 2, τ(s3,4,2, (12)) = τ(s3,4,2, (132)) = 5,

τ(s0,1,2, (13)) = τ(s0,1,2, (123)) = 3, τ(s3,4,2, (13)) = τ(s3,4,2, (123)) = 3.

5.2 Efficient group extensions of automata

As we have seen, all sequences produced by GEAOs are automatic and conversely any automatic sequence
is produced by a GEAO. In [Mül17] it is shown that any sequence can be produced by an especially
well-behaved GEAO. We will now review the key points of the construction in [Mül17] and refer to that

DISCRETE ANALYSIS, 2023:4, 62pp. 27

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

paper for more details. For the convenience of the Reader, we add the notation used in [Mül17] in square
brackets.
Let A = (S, s0, Σk, δ , Ω, τ) [A = (S′, s′
0, Σk, δ ′, τ ′)] be an idempotent k-automaton. Let m [n0] be the
smallest possible cardinality of a set {δ (s, w) | s ∈ S} with w ∈ Σ∗
k. The states of the GEAO ˆS ⊂ Sm

[S ⊂ (S′)n0] consist of ordered m-tuples of distinct states ˆs = (s1, s2, . . . , sm) of A, no two of which contain
the same set of entries. The transition function is defined by the condition that for ˆs = (s1, . . . , sm) ∈ ˆS
and j ∈ Σk the entries of ˆδ ( ˆs, j) are, up to rearrangement, δ (s1, j), . . . , δ (sm, j). The initial state is any
m-tuple ˆs0 = (s0,1, . . . , s0,m) ∈ ˆS with s0,1 = s0. The group G [∆] consists of permutations of {1, 2, . . . , m},
G ⊂ Sym(m). The group labels are chosen so that for ˆs = (s1, . . . , sm) ∈ ˆS and j ∈ Σk the label g = λ ( ˆs, j)
is the unique permutation such that

ˆδ ( ˆs, j) = (
δ (sg(1), j), . . . , δ (sg(m), j)
) .

Hence, δ (s1, j), . . . , δ (sm, j) can be recovered by permuting the entries of ˆδ ( ˆs, j) according to λ ( ˆs, j)
[Mül17, Lem. 2.4]. More generally, for all u ∈ Σ∗
k we have

(δ (s1, u), . . . , δ (sm, u)) = λ ( ˆs, u) · ˆδ ( ˆs, u),

where Sym(m) acts on ˆS by g · (s1, . . . , sm) = (sg−1(1), . . . , sg−1(m)). Finally, for ˆs ∈ ˆS and g ∈ G we set
ˆτ( ˆs, g) = τ (pr1 (g · ˆs)), where pr1 denotes the projection onto the first coordinate. Put T = TA :=
( ˆS, ˆs0, Σk, ˆδ , G, λ , Ω, ˆτ). Then the construction discussed so far guarantees that aA = aT [Mül17, Prop.
2.5] and also that T is strongly connected and that the underlying automaton of T is synchronising
[Mül17, Prop. 2.2].
The GEAO T is essentially unique with respect to the properties mentioned above, except for two
important degrees of freedom: we may rearrange the elements of the m-tuples in ˆS and we may change
ˆs0 to any other state beginning with s0. Let S0 denote the image of δ (·, 0) and let ˆS0 ⊂ Sm
0 denote the
image of ˆδ (·, 0). The assumption that A is idempotent guarantees that for each ˆs ∈ ˆS0 we have ˆδ ( ˆs, 0) = ˆs
and λ ( ˆs, 0) = id. It follows that we may choose ˆs0 ∈ ˆS0, so that T ignores the leading zeros, i.e. it is
prolongable. Consequently, we may assume that T is idempotent.
Rearranging the m-tuples in ˆS corresponds to replacing the labels λ ( ˆs, j) ( ˆs ∈ ˆS, j ∈ Σk) with
conjugated labels λ ′(h( ˆs), j) = h( ˆs)λ ( ˆs, j)h( ˆδ ( ˆs, j))−1 for any h : ˆS → Sym(m) (to retain ˆs0 as a valid
initial state, we also need to guarantee that h( ˆs0)(1) = 1). More generally, for u ∈ Σ∗
k we have λ ′(h( ˆs), u) =
h( ˆs)λ ( ˆs, u)h( ˆδ ( ˆs, u))−1 [Mül17, Prop. 2.6]. To avoid redundancies, we always assume that the group G
is the subgroup of Sym(m) generated by all of the labels λ ( ˆs, j) ( ˆs ∈ ˆS, j ∈ Σk); such conjugation may
allow us to replace G with a smaller group. In fact, we may ensure a minimality property [Mül17, Thm.
2.7 + Cor. 2.26]:

(ˆT1) For any ˆs, ˆs′ ∈ ˆS and sufficiently large l ∈ N we have
{
λ ( ˆs, w) ∣
∣
∣ w ∈ Σ
l
k, ˆδ ( ˆs, w) = ˆs
′} = G.

This property is preserved by any further conjugations, as long as we restrict to h : ˆS → G.
The condition ˆT1 guarantees that all elements of G appear as labels attached to paths between any
two states. It is natural to ask what happens if additional restrictions are imposed on the integer [w]k

DISCRETE ANALYSIS, 2023:4, 62pp. 28

GOWERS NORMS FOR AUTOMATIC SEQUENCES

corresponding to a path. The remainder of [w]k modulo kl (l ∈ N) records the terminal l entries of w and
hence is of limited interest. We will instead be concerned with the remainder of [w]k modulo integers
coprime to k. This motivates us to let gcd∗
k(A) denote the greatest among the common divisors of a set
A ⊂ N0 which are coprime to k and put (following nomenclature from [Mül17])

d′ = d′
T = gcd ∗
k {
[w]k ∣
∣
∣ w ∈ Σ
∗
k, ˆδ ( ˆs0, w) = ˆs0, λ ( ˆs, w) = id
} . (41)

After applying further conjugations, we can find a normal subgroup G0 < G together with a group element
g0 ∈ G such that [Mül17, Thm. 2.16 + Cor. 2.26]:

(ˆT2) For any ˆs, ˆs′ ∈ ˆS and 0 ≤ r < d′ it holds that

{
λ ( ˆs, w) ∣
∣ w ∈ Σ
∗
k, δ ( ˆs, w) = ˆs
′, [w]k ≡ r mod d′} = G0gr
0 = g
r
0G0.

(ˆT3) For any ˆs, ˆs′ ∈ ˆS, any g ∈ G0 and any sufficiently large l ∈ N it holds that

gcd ∗
k {
[w]k ∣
∣
∣ w ∈ Σ
l
k, ˆδ ( ˆs, w) = ˆs′, λ ( ˆs, w) = g} = d′.

The properties listed above imply in particular that G/G0 is a cyclic group of order d′ generated by g0. We
also mention that [Mül17] has a somewhat stronger variant of ˆT3 which is not needed for our purposes.
Let w be a word synchronising the underlying automaton of T to ˆs0. Prolonging w if necessary we
may assume without loss of generality that d′ | [w]k and that w begins with 0. Repeating w if necessary we
may further assume that λ ( ˆs0, w) = id. Conjugating by h( ˆs) = λ −1( ˆs, w) ∈ G0 we may finally assume that
λ ( ˆs, w) = id for all ˆs ∈ ˆS, and hence that the GEAO T is synchronising. Note that thanks to idempotence,
for each ˆs ∈ S we have λ ( ˆs, 0) = λ ( ˆs, 0w) = λ ( ˆs, w) = idG.
In broader generality, let us say that a GEAO T = (S, s0, Σk, δ , G, λ , Ω, τ) (not necessarily arising
from the construction discussed above) is efficient if it is strongly connected, idempotent, synchronising,
λ (s, 0) = idG for all s ∈ S and it satisfies the “unhatted” versions of the properties ˆT1, ˆT2 and ˆT3, that is,
there exist d′ = d′
T , g0 ∈ G and G0 < G such that

(T1) For any s, s′ ∈ S and sufficiently large l ∈ N we have

{
λ (s, w) ∣
∣ w ∈ Σ
l
k, δ (s, w) = s
′} = G.

(T2) For any s, s′ ∈ S and 0 ≤ r < d′ it holds that

{
λ (s, w) ∣
∣ w ∈ Σ
∗
k, δ (s, w) = s′, [w]k ≡ r mod d′} = G0gr
0 = g
r
0G0.

(T3) For any s, s′ ∈ S, any g ∈ G0 and any sufficiently large l ∈ N it holds that

gcd ∗
k {
[w]k ∣
∣ w ∈ Σ
l
k, δ (s, w) = s′, λ (s, w) = g} = d′.

DISCRETE ANALYSIS, 2023:4, 62pp. 29

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

We let wT
0 denote a synchoronising word for T .
The above discussion can be summarised by the following theorem. We note that this theorem is
essentially contained in [Mül17], except for some of the reductions presented here. Additionally, [Mül17]
contains a slightly stronger version of property T2 where w is restricted to Σl
k for large l, which can be
derived from properties T1 and T2.

Theorem 5.4. Let A be a strongly connected idempotent automaton. Then there exists an efficient GEAO
T which produces the same sequence: aA = aT .

In analogy with Proposition 4.2, the veracity of Theorem 4.1 is independent of the initial state of the
group extension of an automaton with output.

Proposition 5.5. Let T = (S, s0, Σk, δ , G, λ , Ω, τ) be an efficient GEAO and let S0 ⊂ S denote the set of
all states s ∈ S such that δ (s, 0) = s and λ (s, 0) = idG. Then the following conditions are equivalent.

1. Theorem 4.1 holds for aT ,s,h for some s ∈ S0, h ∈ G;

2. Theorem 4.1 holds for aT ,s,h for all s ∈ S0, h ∈ G;

Proof. Assume without loss of generality that Theorem 4.1 holds for aT , and let s ∈ S, h ∈ G. It follows
from condition T1 there exists u ∈ Σ∗
k such that aT ,s,h(n) = aT ([u(n)k]k). The claim now follows from
Proposition 4.2 applied to the automaton AT corresponding to T discussed at the end of Section 5.1.

5.3 Representation theory

Let T = (S, s0, Σk, δ , G, λ , Ω, τ) be an efficient GEAO (cf. Theorem 5.4) and T0 = (S, s0, Σk, δ , G, λ ) be
the underlying GEA. In this section we use representation theory to separate the sequence aT produced
by T into simpler components, later shown to be either strongly structured or highly Gowers uniform.
We begin by reviewing some fundamental results from representation theory. A (unitary) representa-
tion ρ of the finite group G is a homomorphism ρ : G → U(V ), where U(V ) denotes the group of unitary
automorphisms of a finitely dimensional complex vector space V equipped with a scalar product. The
representation ρ is called irreducible if there exists no non-trivial subspace W ⊊ V such that ρ(g)W ⊆ W
for all g ∈ G. Every representation uniquely decomposes as the direct sum of irreducible representations.
The representation ρ induces a dual representation ρ ∗ defined on the dual space V ∗, given by
ρ ∗(g)(ϕ) = ϕ ◦ρ(g−1). Note that any element ϕ of V ∗ can be represented as ϕ = ϕv, where ϕv(u) = ⟨u, v⟩
for v ∈ V , and V ∗ inherits from V the scalar product given by the formula ⟨ϕv, ϕu⟩ = ⟨u, v⟩. The
representation ρ ∗ is unitary with respect to this scalar product. For a given choice of orthonormal basis,
the endomorphisms on V can be identified with matrices and V ∗ can be identified with V . Under this
identification, ρ ∗(g) is simply the complex conjugate of ρ(g).
There only exist finitely many equivalence classes of unitary irreducible representations of G and the
matrix coefficients of irreducible representations of G span the space of all functions f : G → C (see e.g.
[FH91, Cor 2.13, Prop. 3.29]; the latter can also be seen as a special case of the Peter–Weyl theorem).
Here, matrix coefficients of ρ are maps G → C of the form g ↦→ ⟨u, ρ(g)v⟩ for some u, v ∈ V . Hence, we
have the following decomposition result.

DISCRETE ANALYSIS, 2023:4, 62pp. 30

GOWERS NORMS FOR AUTOMATIC SEQUENCES

Lemma 5.6. Let T be an efficient group extension of an automaton. The C-vector space of maps G → C
is spanned by maps of the form α ◦ ρ where ρ : G → V is an irreducible unitary representation of G and
α is a linear map End(V ) → C.

We will call b : N0 → C a basic sequence produced by T if it takes the form

b(n) = α ◦ ρ(λ (s0, (n)k)) Jδ (s0, (n)k) = sK (n ∈ N0), (42)

where ρ : G → U(V ) is an irreducible unitary representation of G, α is a linear map End(V ) → C, and
s ∈ S is a state. As a direct consequence of Lemma 5.6 we have the following.

Corollary 5.7. Let T be an efficient group extension of an automaton. The C-vector space of sequences
N0 → C produced by T is spanned by basic sequences defined in (42).

It follows that in order to prove Theorem 4.1 in full generality it is enough to prove it for basic
sequences. There are two significantly different cases to consider, depending on the size of the kernel
ker ρ = {g ∈ G | ρ(g) = idV }. Theorem 4.1 follows immediately from the following result combined
with Theorem 5.4 and Corollary 5.7.

Theorem 5.8. Let T be an efficient group extension of an automaton and let b be a basic sequence given
by (42).

1. If G0 ⊂ ker ρ then b is strongly structured.

2. If G0 ̸⊂ ker ρ then b is highly Gowers uniform.

One of the items above is relatively straightforward and we prove it now. The proof of the other one
occupies the remainder of the paper.

Proof of Theorem 5.8(1). We use the same notation as in Theorem 5.4. Since ρ vanishes on G0, it
follows from property T2 that ρ(λ (s, w)) = ρ(g[w]k
0 ) for any w ∈ Σ∗
k. In particular, the sequence n ↦→
α ◦ ρ (λ (s0, (n)k)) is periodic with period d′. Since the underlying automaton of T is synchronising,
so is the sequence n ↦→ Jδ (s0, (n)k) = sK. It follows that b is the product of a periodic sequence and a
synchronising sequence, whence b is strongly structured.

Example 5.9. Let a, b, c be the sequences defined in Example 1.2. Recall the corresponding GEAO is
introduced in Example 5.2. The group of the labels is G = {+1, −1}, and the corresponding group G0
equals G. Note that G has two irreducible representations: the trivial one g ↦→ 1, and the non-trivial
one g ↦→ g. The trivial representation gives rise to the basic sequences 1+b
2 and 1−b
2 , which are strongly
structured. The non-trivial representations gives rise to the basic sequences 1+b
2 c and 1−b
2 c, which are
highly Gowers uniform. We have a = 3 1+b
2 + 1−b
2 + 1+b
2 c.

We close this section with a technical result which will play an important role in the proof of Theorem
5.8(2). Given two representations ρ : G → U(V ) and σ : H → U(W ) we can consider their tensor product
ρ ⊗ σ : G × H → U(V ⊗W ) which is uniquely determined by the property that (ρ ⊗ σ )(g, h)(v ⊗ w) =
ρ(g)(v) ⊗ σ (h)(w) for all v ∈ V, w ∈ W . (Note that V ⊗ W carries a natural scalar product such that
⟨v ⊗ w, v′ ⊗ w′⟩V ⊗W = ⟨v, v′⟩V ⟨w, w′⟩W , with respect to which ρ ⊗ σ is unitary.) In particular, for D ≥ 0
we can define the D-fold tensor product ρ ⊗D : GD → U(V ⊗D).

DISCRETE ANALYSIS, 2023:4, 62pp. 31

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

Proposition 5.10. Let ρ : G → U(V ) be an irreducible representation of a group G and let G0 be a
subgroup of G such that G0 ̸⊂ ker ρ. Then for any D ≥ 1 we have

∑
g∈GD
0 ρ ⊗D(g) = 0. (43)

Proof. By the definition of the tensor product we find

∑
g∈GD
0 ρ ⊗D(g) = ⊗

ω∈[D]
 ( ∑
gω ∈G0 ρ(gω )

)
 .

Thus it is sufficient to show that
 P := E
g∈G0 ρ(g) = 0. (44)

A standard computation shows that ρ(h)P = P for each h ∈ G0, whence in particular P2 = P. It follows
that P is a projection onto the space U < V consisting of the vectors u ∈ V such that ρ(g)u = u for all
g ∈ G0. Note that U ⊊ V because G0 ̸⊂ ker ρ.
We claim that U is an invariant space for ρ. It will suffice to verify that U is preserved by ρ(g0),
meaning that ρ(h)ρ(g0)u = ρ(g0)u for each u ∈ U and each h ∈ G0. Pick any h and let h′ := g
−1
0 hg0 ∈ G0.
Then, for each u ∈ U we have
 ρ(h)ρ(g0)u = ρ(g0)ρ(h
′)u = ρ(g0)u.

Since ρ is irreducible, it follows that U = {0} is trivial. Consequently, P = 0.

6 Recursive relations and the cube groupoid

6.1 Introducing the Gowers-type averages

The key idea behind our proof of Theorem 5.8(2) is to exploit recursive relations connecting ∥a∥U d [kL]
with ∥a∥U d [kL−l ] for 0 < l < L. In fact, in order to find such relations we consider somewhat more general
averages which we will shortly introduce. A similar idea, in a simpler form, was used in [Kon19].
Throughout this section, T = (S, s0, Σk, δ , G, λ , Ω, τ) denotes an efficient GEAO, d ≥ 1 denotes an
integer, and ρ : G → U(V ) denotes an irreducible unitary representation. All error terms are allowed to
depend on d and T .
In order to study Gowers norms of basic sequences, we need to define certain averages of linear
operators obtained from the representation ρ in a manner rather analogous as in the definition of Gowers
norms, the key difference being that the tensor product replaces the product of scalars. We define the
space (using the terminology of [Tao12, §2.2], we can construe it as a higher order Hilbert space)

E(V ) = Ed(V ) := ⊗

⃗ω∈{0,1}d
|⃗ω| even
 V ⊗ ⊗

⃗ω∈{0,1}d
|⃗ω| odd
 V ∗. (45)

DISCRETE ANALYSIS, 2023:4, 62pp. 32

GOWERS NORMS FOR AUTOMATIC SEQUENCES

Recall that E(V ) has a natural scalar product; we let ∥·∥ denote the corresponding norm on E(V ) and the
operator norm on End(E(V )).
The representation ρ of G on V induces a representation ρρρ of the group G[d] = ∏⃗ω∈{0,1}d G on E(V ),
given by the formula

ρρρ(g) := ⊗

⃗ω∈{0,1}d C |⃗ω|ρ(g⃗ω ) = ⊗

⃗ω∈{0,1}d
|⃗ω| even
 ρ(g⃗ω ) ⊗ ⊗

⃗ω∈{0,1}d
|⃗ω| odd
 ρ ∗(g⃗ω ), (46)

where g = (g⃗ω )⃗ω∈{0,1}d and C ρ = ρ ∗ denotes the dual representation (C 2ρ = ρ). This is nothing else
than the external tensor product of copies of ρ on V and ρ ∗ on V ∗, and as such it is irreducible and unitary
with respect to the induced scalar product on E(V ).
Using r as a shorthand for (r⃗ω )⃗ω∈{0,1}d , we consider the set

R := {
r ∈ Z
[d] ∣
∣
∣ ∃⃗t ∈ [0, 1)
d+1 ∀⃗ω ∈ {0, 1}
d r⃗ω = ⌊
1⃗ω ·⃗t⌋} .

Definition 6.1. For s = (s⃗ω )⃗ω∈{0,1}d ∈ S[d], r = (r⃗ω )⃗ω∈{0,1}d ∈ R and L ≥ 0 we define the averages
A(s, r; L) ∈ End(E(V )) by the formula

A(s, r; L) = 1
k(d+1)L ∑
⃗n∈Zd+1 ∏
⃗ω∈{0,1}d
 q1⃗ω ·⃗n + r⃗ω ∈ [kL]
y (47)

× ∏
⃗ω∈{0,1}d Jδ (s0, (1⃗ω ·⃗n + r⃗ω )k) = s⃗ω K

× ⊗

⃗ω∈{0,1}d C |⃗ω|ρ (λ (s0, (1⃗ω ·⃗n + r⃗ω )k)) .

Let us now elucidate the connection between the averages (47) and Gowers norms. For s ∈ S we let
s[d] = (s)⃗ω∈{0,1}d denote the ‘constant’ cube with copies of s on each coordinate.

Lemma 6.2. Let b be a basic sequence produced by T , written in the form (42) for some linear map
α : End(V ) → C and s ∈ S. Then
 ∥b∥U d [kL] ≪ ∥
∥
∥A(s[d], 0; L)
∥
∥
∥
1/2d , (48)

where the implicit constant depends on α.

Proof. Let α ∗ : End(V ∗) → C denote the conjugate dual map given by the formula α ∗(ψ ∗) = α(ψ). For
⃗ω ∈ {0, 1}d let α⃗ω := α if |⃗ω| is even and α⃗ω := α ∗ if |⃗ω| odd. Using the natural identification

End(E(V )) ∼= ⊗

⃗ω∈{0,1}d
|⃗ω| even
 End(V ) ⊗ ⊗

⃗ω∈{0,1}d
|⃗ω| odd
 End(V ∗),

we define a linear map ααα : End(E(V )) → C by the formula

ααα
 

 ⊗

⃗ω∈{0,1}d ψ⃗ω
 

 = ∏
⃗ω∈{0,1}d α⃗ω (ψ⃗ω ).

DISCRETE ANALYSIS, 2023:4, 62pp. 33

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

With these definitions, an elementary computation shows that

∥b∥2d
U d [kL] = k(d+1)L

Π(kL) ααα(A(s
[d], 0; L)). (49)

The factor k(d+1)L/Π(kL), corresponding to the different normalisations used in (47) and (9), has a finite
limit as L → ∞. Since ααα is linear, we have |ααα(B)| ≪ ∥B∥ and (48) follows.

Remark 6.3. 1. Generalising (49), the average ααα(A(s, r; L)) can be construed (up to a multiplicative
factor and a small error term) as the Gowers product of the 2d functions n ↦→ b(n + r⃗ω ) for all ⃗ω ∈ {0, 1}d.

2. As seen from the formulation of Lemma 6.2, we are ultimately interested in the averages (47)
when r = 0. The non-zero values of r correspond to ancillary averages, which naturally appear in the
course of the argument.

3. Note that for r = 0 the first product on the right hand side of (47) simply encodes the condition
that ⃗n ∈ Π(kL). The normalising factor k−(d+1)L ensures that A(s, r; L) remain bounded as L → ∞.

Our next goal is to obtain a recursive relation for the averages given by (47). Note that any ⃗n ∈ Zd+1

can be written uniquely in the form ⃗n = kl⃗m +⃗e where ⃗e ∈ [kl]d+1 and ⃗m ∈ Zd+1. Let v = (s, r) ∈ S[d] × R
be arbitrary. Writing ⃗n as above in the definition of A(v; L), and letting s′ ∈ S[d] and r′ ∈ N
[d]
0 denote the
‘intermediate data’, we obtain

A(v; L) = 1
k(d+1)L ∑
s′∈S[d] ∑

r′∈N
[d]
0 ∑
⃗m∈Zd+1 ∑
⃗e∈[kl ]d+1 (50)

∏
⃗ω∈{0,1}d
 q1⃗ω · ⃗m + r′
⃗ω ∈ [kL−l]
y · s⌊ 1⃗ω ·⃗e + r⃗ω
kl
 ⌋ = r′
⃗ω
 {

× ∏
⃗ω∈{0,1}d
 qδ (s0, (1⃗ω · ⃗m + r′
⃗ω )k) = s′
⃗ω y · qδ (s′
⃗ω , (1⃗ω ·⃗e + r⃗ω )
l
k) = s⃗ω y

× ⊗

⃗ω∈{0,1}d C |⃗ω|ρ (
λ (s0, (1⃗ω · ⃗m + r′
⃗ω )k)
) · C |⃗ω|ρ (
λ (s
′
⃗ω , (1⃗ω ·⃗e + r⃗ω )
l
k)
) .

In this formula the term corresponding to (s′, r′,⃗m,⃗e ) vanishes unless r′ belongs to R. Indeed, since r is
in R, we can write r⃗ω = ⌊1⃗ω ·⃗t⌋ for some⃗t ∈ [0, 1)d+1, and then the corresponding term vanishes unless

r′
⃗ω = ⌊ 1⃗ω ·⃗e + r⃗ω
kl
 ⌋ =
 ⌊ 1⃗ω ·⃗e + ⌊
1⃗ω ·⃗t⌋

kl
 ⌋
 = ⌊ 1⃗ω ·⃗e + 1⃗ω ·⃗t
kl
 ⌋ = ⌊1⃗ω ·⃗t′⌋,

where ⃗t′ := (⃗e +⃗t )/kl ∈ [0, 1)d+1. The key feature of formula (50) is that the two inner sums over ⃗m and
⃗e can be separated, leading to
 A(v; L) = ∑
v′∈S[d]×R A(v′; L − l) · M(v′, v; l), (51)

DISCRETE ANALYSIS, 2023:4, 62pp. 34

GOWERS NORMS FOR AUTOMATIC SEQUENCES

where the expression M(v′, v; l) is given for any v = (s, r) and v′ = (s′, r′) in S[d] × R by the formula

M(v
′, v; l) = 1
k(d+1)l ∑
⃗e∈[kl ]d+1
 s⌊ 1⃗ω ·⃗e + r⃗ω
kl
 ⌋ = r′
⃗ω
 { (52)

× ∏
⃗ω∈{0,1}d
 q
δ (s
′
⃗ω , (1⃗ω ·⃗e + r⃗ω )
l
k) = s⃗ω y

× ⊗

⃗ω∈{0,1}d C |⃗ω|ρ (
λ (s′
⃗ω , (1⃗ω ·⃗e + r⃗ω )
l
k)
) .

The form of the expression above is our main motivation for introducing in the next section the category
V.

6.2 The category Vd(T )

To keep track of the data parametrising the averages defined above, we define the d-dimensional category
V = Vd(T ) associated to the GEAO T (or, strictly speaking, to the underlying group extension of an
automaton without output). The objects ObV of this category are the pairs v = (s, r) ∈ S[d] × R. Since R
and S are finite, there are only finitely many objects. The morphisms of V will help us keep track of the
objects v′ = (s′, r′) appearing in formulæ (51) and (52). These morphisms are parametrised by the tuples

(l,⃗e, s
′, r) ∈ N0 × [kl]
d+1 × S[d] × R = MorV.

The tuple (l,⃗e, s′, r) describes an arrow from v′ = (s′, r′) to v = (s, r), where s = (s⃗ω )⃗ω and r′ = (r′
⃗ω )⃗ω
are given by the formulæ

s⃗ω = δ (s′
⃗ω , (1⃗ω ·⃗e + r⃗ω )
l
k) and r′
⃗ω = ⌊ 1⃗ω ·⃗e + r⃗ω
kl
 ⌋ . (53)

We will denote this morphism by ̃e = (l,⃗e ) : v′ → v. The number deg(̃e) := l is called the degree of ̃e. In
order to define the composition of morphisms, we state the following lemma.

Lemma 6.4. If ̃e′ = (l′,⃗e′) is a morphism from v′′ to v′ and ̃e = (l,⃗e) is a morphism from v′ to v, then
̃e′′ = (l + l′, kl⃗e′ +⃗e) is a morphism from v′′ to v.

Proof. Using the same notation as above, for each ⃗ω ∈ {0, 1}d we have the equality

(1⃗ω · ⃗e′′ + r′′
⃗ω )
l+l′
k = (1⃗ω ·⃗e′ + r′
⃗ω )
l′
k (1⃗ω ·⃗e + r⃗ω )
l
k (54)

which allows us to verify that

δ (
s
′′
⃗ω , (1⃗ω · ⃗e′′ + r′′
⃗ω )
l′′
k ) = δ (
s
′′
⃗ω , (1⃗ω ·⃗e′ + r′
⃗ω )
l′
k (1⃗ω ·⃗e + r⃗ω )
l
k)

= δ (
s
′
⃗ω , (1⃗ω ·⃗e + r⃗ω )
l
k) = s⃗ω ,

DISCRETE ANALYSIS, 2023:4, 62pp. 35

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

and by basic algebra we have

r′′
⃗ω =
 ⌊ 1⃗ω ·⃗e′ + r′
⃗ω
kl′
 ⌋
 =
 


 1⃗ω ·⃗e′ + ⌊ 1ω·⃗e+r⃗ω
kl ⌋

kl′
 




=
 ⌊ kl(1⃗ω ·⃗e′) + 1ω ·⃗e + r⃗ω
kl′+l
 ⌋
 =
 ⌊ 1⃗ω · ⃗e′′ + r⃗ω
kl′′
 ⌋
 .

Lemma 6.4 allows us to define the composition of two morphisms ̃e′ = (l′,⃗e′) : v′′ → v′ and ̃e =
(l,⃗e ) : v′ → v as ̃e′′ = ̃e′ ◦ ̃e := (l′′, ⃗e′′) = (l + l′, kl⃗e′ +⃗e) : v′′ → v. The composition is clearly associative,
and for each object v the map (0,⃗0) : v → v is the identity map. This shows that V is indeed a category.
We let Mor(v′, v) denote the set of morphism from v′ to v. The degree induces an N0-valued
gradation on this set, which means that Mor(v′, v) decomposes into a disjoint union∏∞
l=0 Morl(v′, v),
where Morl(v′, v) is the set of morphisms ̃e : v′ → v of degree l. The degree of the composition of two
morphisms is equal to the sum of their degrees. A crucial property of the category V is that morphisms
can also be uniquely decomposed in the following sense.

Lemma 6.5. Let ̃e′′ : v′′ → v be a morphism and let 0 ≤ l′ ≤ deg( ̃e′′) be an integer. Then there exist
unique morphisms ̃e′ and ̃e with ̃e′′ = ̃e′ ◦ ̃e and deg(̃e′) = l′.

Proof. Put v′′ = (s′′, r′′), v = (s, r), l = deg( ̃e′′) − l′ and ̃e′′ = (l′ + l′′, ⃗e′′). Then there exists a unique
decompositon ⃗e′′ = kl⃗e′ +⃗e, where ⃗e′ ∈ [kl′]d+1 and ⃗e ∈ [kl]d+1. Thus, we can define v′ = (s′, r′) by the
formulæ
 s′
⃗ω := δ (s′′
⃗ω , (1⃗ω ·⃗e′ + r′
ω )
l′
k ) and r′
⃗ω := ⌊ 1⃗ω ·⃗e + r⃗ω
kl′
 ⌋ .

A computation analogous to the one showing that composition of morphisms is well-defined shows that
(l′ + l, ⃗e′′) = (l′,⃗e′) ◦ (l,⃗e). Conversely, it is immediate that such a decomposition is unique.

Remark 6.6. As a particular case of (51), we can recover A(v; L) from M(v′, v; L). Indeed, it follows
from (51) that
 A(v; L) = ∑
v′∈S[d]×R A(v
′; 0) · M(v′, v; L). (55)

Recalling the definition of A(v′; 0) in (47) we see that the only non-zero terms in the sum (55) above
correspond to objects of the form v′ = (s[d]
0 , r′) where r′ ∈ R is such that there exists ⃗n ∈ Zd+1 with
r′
⃗ω = 1⃗ω ·⃗n for each ⃗ω ∈ {0, 1}d. Let R′ ⊂ R denote the set of all r′ with the property just described and

note that if r′ ∈ R′ then A(s[d]
0 , r′; 0) = idE(V ) is the identity map. It follows that

A(v; L) = ∑
r′∈R′ M((s[d]
0 , r′), v; L). (56)

We stress that 0 ∈ R′, but as long as d ≥ 2, R′ contains also other elements. For instance, when d = 2 the
set R consists of exactly the elements (r00, r01, r10, r11) of the form

(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 1), (0, 1, 0, 1), (0, 1, 1, 1), (0, 1, 1, 2),

DISCRETE ANALYSIS, 2023:4, 62pp. 36

GOWERS NORMS FOR AUTOMATIC SEQUENCES

while R′ consists of elements of the form

(0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1), (0, 1, 1, 2).

6.3 The subcategory Ud(T )

The object
 v0 = vT
0 = (s
[d]
0 , 0[d]) ∈ ObV (57)

is called the base object. In the recurrence formulæ above the objects of particular importance are those
which map to the base object. We define a (full) subcategory U of V, whose objects are those among
v ∈ ObV for which Mor(v, v0) ̸= /0 and Mor(v0, v) ̸= /0 (in fact, we will prove in Lemma 6.7 that the
former condition is redundant), and whose morphisms are the same as those in V.

Lemma 6.7. There exists l0 ≥ 0 such that Morl(v, v0) ̸= /0 for any v ∈ ObV and any l ≥ l0.

Proof. We first consider objects of the form v = (s, 0). Letting e0 = [wT
0 ]k3 and ei = 0 for 1 ≤ i ≤ d and
taking sufficiently large l we find a morphism ̃e = (l,⃗e) : v → v0.
In the general case, since Mor(v, v0) ⊂ Mor(v, v′) ◦ Mor(v′, v0), it only remains to show that for each
object v = (s, r) ∈ ObV there exists some v′ = (s′, 0) ∈ ObV such that Mor(v, v′) ̸= /0. Since r ∈ R, there
exists a vector⃗t ∈ [0, 1)d+1 such that

r⃗ω = ⌊1⃗ω ·⃗t⌋ for all ⃗ω ∈ {0, 1}d. (58)

It follows from piecewise continuity of the floor function that there exists an open set of⃗t ∈ [0, 1)d+1 that
fulfill (58). Hence, one can pick, for any sufficiently large l ≥ 0,⃗t of the form⃗t =⃗e/kl, where ⃗e ∈ [kl]d+1.
Choosing s′
⃗ω = δ (s⃗ω , (1⃗ω ·⃗e)l
k) finishes the proof.

Corollary 6.8. Let v, v′ ∈ ObV. If Mor(v, v′) ̸= /0 and v ∈ ObU, then v′ ∈ ObU.

Proof. By Lemma 6.7, we have Mor(v′, v0) ̸= /0. Moreover, we find by Lemma 6.4, that Mor(v0, v′) ⊃
Mor(v0, v) ◦ Mor(v, v′) ̸= /0.

Lemma 6.9. Let s ∈ S and let v = (s[d], 0) ∈ ObV. Then v ∈ ObU.

Proof. It is enough to show that v0 is reachable from v. Let w ∈ Σ∗
k be a word synchronising the
underlying automaton of T to s. Let e0 = [w]k, ei = 0 for 1 ≤ i ≤ d and let l > |w| + logk(d). Then we
have the morphism ̃e = (l,⃗e ) : v0 → v, as needed.

3We recall that wT
0 is a synchronizing word for T , i.e. for any s ∈ S we have δ (s, wT
0 ) = s0, λ (s, wT
0 ) = id.

DISCRETE ANALYSIS, 2023:4, 62pp. 37

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

6.4 The cube groupoid

By essentially the same argument as in (51) we conclude that for any v, v′, v′′ ∈ S[d] × R we have

M(v, v
′′; L) = ∑
v′∈S[d]×R M(v, v
′; L − l) · M(v
′, v
′′; l). (59)

Regarding the group G[d] as a category with one object, we define the d-dimensional fundamental
functor λλλ = λλλ d
T : Vd(T ) → G[d] as follows. All objects are mapped to the unique object of G[d] and an
arrow ̃e = (l,⃗e) : v = (s, r) → v′ = (s′, r′) is mapped to

λλλ (̃e) = (λ⃗ω (̃e))⃗ω∈{0,1}d = (
λ (s⃗ω , (1⃗ω ·⃗e + r′
⃗ω )
l
k)
⃗ω∈{0,1}d . (60)

It follows from Lemma 6.4 that λλλ is indeed a functor.
We are now ready to rewrite M in a more convenient form:

M(v, v′; l) = ∑
̃e∈Morl (v,v′) ρρρ(λλλ (̃e)). (61)

In order to keep track of the terms appearing in (61), we introduce the families of cubes Qd
l . For two
objects v, v′ ∈ ObV the cube family Qd
l (T )(v, v′) is defined to be the subset of G[d] given by

Q
d
l (T )(v, v
′) = {λλλ (̃e) | ̃e ∈ Morl(v, v′)}. (62)

6.5 Frobenius–Perron theory

In this section we review some properties of nonnegative matrices and their spectra. For a matrix W we
let ρ(W ) denote its spectral radius. By Gelfand’s formula, for any matrix norm ∥·∥ we have

ρ(W ) = lim
l→∞
 ∥
∥W l∥
∥
1/l . (63)

If W,W ′ are two matrices of the same dimensions, then we say that W ≥ W ′ if the matrix W −W ′ has
nonnegative entries. Accordingly, W > W ′ if W −W ′ has strictly positive entries. In particular, W has
nonnegative entries if and only if W ≥ 0.
Let W = (Wi j)i, j∈I be a nonnegative matrix with rows and columns indexed by a (finite) set I. For
J ⊂ I, we let W [J] = (Wi j)i, j∈J denote the corresponding principal submatrix. We define a directed graph
with the vertex set I and with an arrow from i ∈ I to j ∈ I whenever Wi j > 0. We say that i ∈ I dominates
j ∈ I if there is a directed path from i to j4, and that i and j are equivalent if they dominate each other.
We refer to the equivalence classes of this relation as the classes of W . We say that a class J1 dominates a
class J2 if j1 dominates j2 for some (equivalently, all) j1 ∈ J1 and j2 ∈ J2. This is a weak partial order on
the set of classes.
A nonnegative matrix W is called irreducible if it has only one class. The Frobenius–Perron theorem
says that every irreducible matrix has a real eigenvalue λ equal to its spectral radius, its multiplicity is

4We note that i always dominates itself via the empty path.

DISCRETE ANALYSIS, 2023:4, 62pp. 38

GOWERS NORMS FOR AUTOMATIC SEQUENCES

one, and there is a corresponding eigenvector with strictly positive entries [Min88, Thm. I.4.1 & I.4.3].
For any nonempty subset J ⊂ I we have ρ(W [J]) ≤ ρ(W ), and the inequality is strict if W is irreducible
and J ̸= I [Min88, Cor. II.2.1 & II.2.2]. We call a class J ⊂ I basic if ρ(W [J]) = ρ(W ), and nonbasic
otherwise.

Proposition 6.10. Let W = (Wi j)i, j∈I be a nonnegative matrix such that the matrices W l are jointly
bounded for all l ≥ 0. Let N ≤ W be a nonnegative matrix, and let J ⊂ I be a basic class of W such that
N[J] ̸= W [J]. Then there is a constant γ < 1 such that for all i ∈ I and j ∈ J we have

(Nl)i j ≪ γ l as l → ∞. (64)

Proof. Let V = RI denote the vector space with basis I equipped with the standard Euclidean norm. We
identify matrices indexed by I with linear maps on V and let ∥A∥ denote the operator norm of a matrix A
(in fact, we could use any norm such that 0 ≤ A1 ≤ A2 implies ∥A1∥ ≤ ∥A2∥). For J ⊂ I let V [J] denote
the vector subspace of V with basis J.
By Gelfand’s theorem, the spectral radius of W can be computed as ρ(W ) = liml→∞ ∥
∥W l∥
∥1/l . Since
the matrices W l are jointly bounded, we have ρ(W ) ≤ 1. Furthermore, if ρ(W ) < 1, then there is some
λ < 1 such that ∥
∥W l∥
∥ ≤ λ l for l large enough, and hence all entries of W l (and a fortiori of Nl) tend to
zero at an exponential rate, proving the claim. Thus, we may assume that ρ(W ) = 1.

Step 1. No two distinct basic blocks of W dominate each other.

Proof. Let J1 and J2 be distinct basic blocks of W , and for the sake of contradiction suppose that J1
dominates J2. By Frobenius–Perron theorem applied to the matrices W [J1] and W [J2], there are vectors
x1 ∈ V [J1] and x2 ∈ V [J2] with x1, x2 > 0 and W [J1]x1 = x1, W [J2]x2 = x2. Since J1 dominates J2, there
exists m ≥ 1 such that any vertex i ∈ J1 is connected to any vertex j ∈ J2 by a path of length < m. Let
U := 1
m (I +W + · · · +W m−1). It follows (cf. [Min88, Thm. I.2.1]) for a sufficiently small value of ε > 0
that we have Ux1 ≥ x1 + εx2, Ux2 ≥ x2. (65)

Iterating (65), for any l ≥ 0 we obtain U lx1 ≥ x1 + lεx2. (66)

On the other hand, powers of U are jointly bounded because the powers of W are jointly bounded, which
yields a contradiction.

Let x ∈ V [J], x > 0, be the eigenvector of W [J] with eigenvalue 1. Let K be the union of all the classes
of W dominated by J except for J itself. By Step 1 all the classes in K are nonbasic, and the subspace
V [K] is W -invariant. The spectral radius of the matrix W [K] is equal to the maximum of the spectral radii
of W [J′] taken over all the classes J′ ⊂ K, and hence ρ(W [K]) < 1.

Step 2. We have N[J]lx < W [J]lx for all l ≥ |J|.

Proof. As N[J] ̸= W [J], there exist i, i′ ∈ J such that N[J]i,i′ < W [J]i,i′. Since x > 0, we have (N[J]lx) j <
(W [J]lx) j for each j ∈ J that is an endpoint of a path of length l containing the arrow i, i′. As W [J] is
irreducible, such path exists for all l ≥ |J|.

DISCRETE ANALYSIS, 2023:4, 62pp. 39

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

Step 3. We have ∥
∥Nlx∥
∥ ≪ γ l for some γ < 1 as l → ∞

Proof. Since ρ(W [K]) < 1, it follows from Gelfand’s theorem that for any sufficiently large n we have

∥N[K]
n∥ ≤ ∥W [K]
n∥ < 1. (67)

By Step 2, for any sufficiently large n there exist λ < 1 and v ∈ V [K] such that

Nnx ≤ λ x + v. (68)

Pick n, λ and v such that (67) and (68) hold, and assume additionally that λ is close enough to 1 so that
∥N[K]n∥ ≤ λ , whence Nnv = N[K]
nv ≤ λ v. (69)

Applying (68) iteratively, for any l ≥ 0 we obtain

Nlnx ≤ λ lx + lλ l−1v.

It follows that Step 3 holds with any γ such that γ < λ 1/n.

Since x > 0 (as an element of V [J]) the claim (64) follows immediately from Step 3.

6.6 From recursion to uniformity

In Section 7 we obtain a fairly complete description of the cubes Qd
l (v, v′). The main conclusion is the
following (for a more intuitively appealing equivalent formulation, see Theorem 7.17).

Theorem 6.11. There exist cubes gv ∈ G[d], v ∈ ObU, and a threshold l0 ≥ 0 such that for each l ≥ l0
and each v, v′ ∈ ObU we have
 Q
d(T )(v, v
′) = g−1
v G
[d]
0 Hgv′,

where H < G[d] is given by
 H = {(
g
1⃗ω·⃗e
0 )
⃗ω∈{0,1}d
 ∣
∣
∣
∣ ⃗e ∈ N
d+1
0
 } .

Presently, we show how the above result completes the derivation of our main theorems. We will
need the following corollary.

Corollary 6.12. There exists l0 ≥ 0 such that for all l ≥ l0 we have

G
[d]
0 ⊂ Qd
l (v0, v0). (70)

Proof. Follows directly from the observation that id
[d]
G ∈ H (where we use the notation from Theorem
6.11) and G0 is normal in G.
 DISCRETE ANALYSIS, 2023:4, 62pp. 40

GOWERS NORMS FOR AUTOMATIC SEQUENCES

Proof of Theorem 5.8(2). Recall that in (49) we related the Gowers norms in question to the averages
A(v; L) with v ∈ ObV taking the form v = (s[d], 0) and that by Lemma 6.9 the relevant cubes belong to
ObU. Hence, it will suffice to show that for any v ∈ ObU we have the bound ∥A(v; L)∥ ≪ k−cL for a
positive constant c > 0.
Let us write A and M (defined in (47) and (52) respectively) in the matrix forms:

A(L) = (
A(v; L)
)

v∈ObV and M(L) = (
M(v, v
′; L)
)

v,v′∈ObV;

note that the entries of the matrices A(L) and M(L) are elements of End(E(V )). This allows us to rewrite
the recursive relations (51) and (59) as matrix multiplication:

A(l + l′) = A(l)M(l′), M(l + l′) = M(l)M(l′), (l, l′ ≥ 0). (71)

Consider also the real-valued matrices N(L) and W (L), of the same dimension as M(L), given by

N(L)v,v′ = ∥
∥M(L)v,v′∥
∥
2 = 1
k(d+1)L
 ∥
∥
∥
∥
∥ ∑
̃e∈MorL(v,v′) ρρρ(λλλ (̃e))

∥
∥
∥
∥
∥
2

W (L)v,v′ = |MorL(v, v′)|
k(d+1)L .

Note that 0 ≤ N(l) ≤ W (l) for each l ≥ 0 by a straightforward application of the triangle inequality
and the fact that ρρρ is unitary. Moreover, for reasons analogous to (71) we also have

N(l + l′) ≤ N(l)N(l′) W (l + l′) = W (l)W (l′), (l, l′ ≥ 0). (72)

As a consequence, W (l) = W l, where W := W (1). It also follows directly from how morphisms are
defined that W (l)v,v′ ≤ 1 for all v, v′ ∈ ObV and l ≥ 0.
Let l0 be the constant from Corollary 6.12. Then, by Proposition 5.10 we have N(l)v0,v0 ̸= W (l)v0,v0
for all l ≥ l0. We are now in position to apply Proposition 6.10, which implies that there exits γ < 1 such
that for any v ∈ V and any u ∈ U we have
 N(l0)
l
v,u ≪ γ l/l0. (73)

Using with (72), (73) can be strengthened to
N(L)v,u ≪ γ L. (74)

Finally, using (71) and the fact that all norms on finitely dimensional spaces are equivalent, for any
u ∈ ObU and L ≥ 0 we conclude that

∥A(u; L)∥ = ∥A(L)u∥ =
 ∥
∥
∥
∥
∥ ∑
v∈V A(0)vM(L)v,u
∥
∥
∥
∥
∥ ≪ ∑
v∈V N(L)v,u ≪ γ L. (75)

DISCRETE ANALYSIS, 2023:4, 62pp. 41

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

7 Cube groups

7.1 Groupoid structure

We devote the remainder of this paper to proving Theorem 6.11, which provides a description of the
cube sets Qd
l (v, v′). In this section we record some basic relations between the Qd
l (v, v′) for different
v, v′ ∈ ObV. Our key intention here is to reduce the problem of describing Qd
l (T )(v, v′) for arbitrary
v, v′ ∈ ObU to the special case when v = v′ = vT
0 .

Lemma 7.1. Let T be an efficient GEA and let v, v′, v′′ ∈ ObV and l, l′ ≥ 0. Then

Qd
l′(T )(v, v
′) · Q
d
l (T )(v′, v
′′) ⊆ Q
d
l+l′(T )(v, v′′).

Proof. This is an immediate consequence of the fact that λλλ is a functor.

Lemma 7.2. Let T be an efficient GEA and v, v′ ∈ ObU. Then the limit

Qd(T )(v, v′) = lim
l→∞ Q
d
l (T )(v, v
′) (76)

exists. Moreover, there exist cubes gv ∈ G[d] such that for any v, v′ ∈ ObU the limit in (76) is given by

Q
d(T )(v, v
′) = g
−1
v · Q
d(T )(v
T
0 , v
T
0 ) · gv′. (77)

Remark 7.3. Since Qd
l (T )(v, v′) are finite, (76) is just a shorthand for the statement that there exists
l0 = l0(T , v, v′) ≥ 0 and a set Qd(T )(v, v′) such that Qd
l (T )(v, v′) = Qd(T )(v, v′) for all l ≥ l0.

Proof. Note first that Qd
1(T )(vT
0 , vT
0 ) ̸= 0 contains the identity cube id
[d]
G , arising from the morphism
(1,⃗0) : vT
0 → vT
0 . It follows from Lemma 7.1 that the sequence Qd
l (T )(vT
0 , vT
0 ) is increasing in the
sense that Qd
l (T )(vT
0 , vT
0 ) ⊆ Qd
l+1(T )(vT
0 , vT
0 ) for each l ≥ 0. Since the ambient space G[d] is finite, it
follows that the sequence Qd
l (T )(vT
0 , vT
0 ) needs to stabilise, and in particular the limit (76) exists for
v = v′ = vT
0 .
It follows from Lemma 7.2 that for any m, m′, l ≥ 0 we have the inclusion

Q
d
m′(T )(vT
0 , v) · Q
d
l (T )(v, v
′) · Q
d
m(T )(v′, vT
0 ) ⊆ Q
d
m+m′+l(T )(vT
0 , vT
0 ).

Since there exist morphisms vT
0 → v, v′ → vT
0 , there exist m, m′ ≥ 0 and gv,̃gv′ (any elements of
Qd
m(T )(vT
0 , v) and Qd
m′(T )(v′, vT
0 )−1 respectively) such that for all l ≥ 0 we have

gv · Qd
l (T )(v, v′) · ̃g−1
v′ ⊆ Qd
m+m′+l(T )(v
T
0 , v
T
0 ).

We thus conclude that if l ≥ 0 is sufficiently large then

Q
d
l (T )(v, v
′) ⊆ g
−1
v · Q
d(T )(vT
0 , v
T
0 ) · ̃gv′. (78)

Reasoning in a fully analogous manner (with pairs (v, v′) and (vT
0 , vT
0 ) swapped), for sufficiently large l
we obtain the reverse inclusion

Qd(T )(v
T
0 , v
T
0 ) ⊆ h−1
v · Q
d
l (T )(v, v
′) · ̃hv′, (79)

DISCRETE ANALYSIS, 2023:4, 62pp. 42

GOWERS NORMS FOR AUTOMATIC SEQUENCES

for some cubes hv, ̃hv′ ∈ G[d]. Comparing cardinalities we conclude that both (78) and (79) are in fact
equalities. Hence, the limit (76) exists for all v, v′ ∈ ObU and

Q
d(T )(v, v
′) = g
−1
v · Q
d(T )(vT
0 , v
T
0 ) · ̃gv′. (80)

Note that gv and ̃gv are determined up to multiplication on the left by an element of Qd(T )(vT
0 , vT
0 )
and we may take gvT
0 = ̃gvT
0 = id
[d]
G . Hence, Qd(T )(vT
0 , vT
0 ) is a group. It now follows from Lemma
7.1 that Qd(T )(vT
0 , v) · Qd(T )(v, vT
0 ) ⊆ Qd(T )(vT
0 , vT
0 ), or equivalently

Qd(T )(v
T
0 , v
T
0 ) · ̃gvg
−1
v · Q
d(T )(vT
0 , v
T
0 ) ⊆ Qd(T )(v
T
0 , vT
0 ), (81)

meaning that ̃gvg−1
v ∈ Qd(T )(vT
0 , vT
0 ). Hence, we may take ̃gv = gv, since we can multiply ̃gv from the
left with (̃gvg−1
v )−1 ∈ Qd(T )(vT
0 , vT
0 ).

As a consequence of Lemma 7.2, the sets Qd(T )(v, v′) for v, v′ ∈ ObU form a groupoid, in the sense
that we have the following variant of Lemma 7.1.

Corollary 7.4. Let T be an efficient GEA and let v, v′, v′′ ∈ ObU. Then

Qd(T )(v, v′) · Q
d(T )(v
′, v′′) = Qd(T )(v, v′′).

In particular, in order to understand all of the sets Qd(v, v′) (up to conjugation) it will suffice to
understand one of them. This motivates us to put

Q
d(T ) = Q
d(T )(vT
0 , vT
0 ). (82)

We also mention that the sets Qd(T ) are easy to describe for small values of d.

Lemma 7.5. Let T be an efficient GEA and d ∈ {0, 1}. Then

Qd(T ) = G
[d].

Proof. Immediate consequence of the definition of Qd(T ) and property T1.

7.2 Characteristic factors

A morphism between GEA T and ¯T given by (φ , π) is a factor map if both φ : S → ¯S and π : G → ¯G
are surjective. In this case, ¯T is a factor of T . The group homomorphism π induces a projection map
πππ : G[d] → ¯G[d]. As λλλ is a functor, πππ(Qd(T )) ⊂ Qd( ¯T ) for all d ≥ 0. In fact, for large l ≥ 0 we have the
following commutative diagram:
 Morl(v0, v0) Morl(¯v0, ¯v0)

Qd
l (T ) Qd
l ( ¯T )

id

λλλ λλλ

πππ

DISCRETE ANALYSIS, 2023:4, 62pp. 43

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

The map labelled id takes the morphism (l,⃗e) : v0 → v0 to morphism given by the same data (l,⃗e) : ¯v0 →
¯v0. We will say that the factor ¯T of T is characteristic if for each d ≥ 0 we have the equality
Qd(T ) = πππ −1 (
Qd( ¯T )
)
. Note that if ¯T is a characteristic factor of T then the cube groups Qd(T ) are
entirely described in terms of the simpler cube groups Qd( ¯T ). It is also easy to verify that if ¯T is a
characteristic factor of T then any characteristic factor of ¯T is also a characteristic factor of T .
For instance, a GEA is always its own factor, which is always characteristic. A possibly even more
trivial5 example of a factor is the trivial GEA Ttriv with a single state, trivial group, and the other data
defined in the only possible way. In fact, Ttriv is the terminal object, meaning that it is a factor of any
GEA . The trivial GEA is a characteristic factor of T if and only if Qd(T ) = G[d] for all d ≥ 0.

Lemma 7.6. Let T be an efficient GEA and let (φ , π) be a factor map from T to ¯T . If ker π ⊂ G0 then
¯T is an efficient GEA and d′
T = d′ ¯T .

Proof. We verify each of the defining properties of an efficient GEA in turn. It is clear that ¯T is strongly
connected and that ¯T is synchronising; in fact, if w ∈ Σ∗
k is synchronising to the state s ∈ S for T then w
is also synchronising to the state φ (s) ∈ ¯S for ¯T . We also find that ¯T is idempotent and ¯λ ( ¯s, 0) = id for
all ¯s ∈ ¯S. Put also ¯G0 = π(G0) and ¯g0 = π(g0).
For T1, let ¯s, ¯s′ ∈ ¯S and let s ∈ φ −1( ¯s) and s′ ∈ φ −1( ¯s′). Then
{¯λ ( ¯s, w) ∣
∣ w ∈ Σ
l
k, ¯δ ( ¯s) = ¯s
′} ⊇ {
π (λ (s, w)) ∣
∣ w ∈ Σ
l
k, δ (s) = s
′} = ¯G,

and the reverse inclusion is automatic.
For T2, let. Let ¯s, ¯s′ ∈ ¯S and s ∈ φ −1( ¯s). Then
{¯λ ( ¯s, w) ∣
∣ w ∈ Σ
∗
k, ¯δ ( ¯s, w) = ¯s
′, [w]k ≡ r mod d′}

= ⋃

s′∈φ −1( ¯s′)
 {
π(λ (s, w)) ∣
∣ w ∈ Σ
∗
k, δ (s, w) = s′, [w]k ≡ r mod d′}

= ⋃

s′∈φ −1( ¯s′) π(gr
0G0) = ¯g
r
0 ¯G0.

For T3, let ¯s, ¯s′ ∈ ¯S, ¯g ∈ ¯G0, let s ∈ φ −1( ¯s). Then

gcd ∗
k ({
[w]k ∣
∣ w ∈ Σ
l
k, ¯δ ( ¯s, w) = ¯s
′, ¯λ ( ¯s, w) = ¯g})

= gcd ∗
k
 

 ⋃

g∈π −1( ¯g)
 ⋃

s′∈φ −1( ¯s′)
 {
[w]k ∣
∣ w ∈ Σ
l
k, δ (s, w) = s′, λ (s, w) = g}




= gcd ∗
k ({
c(g, s′) ∣
∣ g ∈ π −1( ¯g), s′ ∈ φ −1( ¯s′)
}) = d′,

where c(g, s′) is, thanks to T3 for T , given by

c(g, s′) = gcd ∗
k ({
[w]k ∣
∣ w ∈ Σ
l
k, δ (s, w) = s
′, λ (s, w) = g
}) = d′.

5no pun intended
 DISCRETE ANALYSIS, 2023:4, 62pp. 44

GOWERS NORMS FOR AUTOMATIC SEQUENCES

7.3 Group quotients

Let T = (S, s0, Σk, δ , G, λ ) be a GEA . One of the basic ways to construct a factor of T is to leave the
state set unaltered and replace G with a quotient group. More precisely, for a normal subgroup H < G, we
can consider the quotient GEA without output T /H = (S, s0, Σk, δ , G/H, ¯λ ) with the same underlying
automaton and group labels given by ¯λ (s, j) = λ (s, j) ∈ G/H for s ∈ S, j ∈ Σk. Thus defined GEA is a
factor of T , with the factor map given by (idS, π), where π : G → G/H is the quotient map. The purpose
of this section is to identify an easily verifiable criterion ensuring that the factor T /H is characteristic.
As a convenient byproduct, this will allow us to mostly suppress the dependency on the dimension d from
now on.
In fact, it is not hard to identify the maximal normal subgroup of G such that the corresponding factor
is characteristic. Let H < G be normal and let π : G → G/H denote the quotient map. For any d ≥ 0,
the map πππ : Qd(T ) → Qd(T /H) is surjective and for any g ∈ Qd(T ) we have πππ −1(πππ(g)) = gH[d]. It
follows that T /H is characteristic if and only if H[d] ⊂ Qd(T ). In particular, if T /H is characteristic
then Qd(T ) contains all cubes with an element of h at one vertex and idG elsewhere. In order to have
convenient access to such cubes, for g ∈ G and ⃗σ ∈ {0, 1}d put

c
d
⃗σ (h) = (
hJ⃗ω=⃗σ K)
⃗ω∈{0,1}d = (c⃗ω )⃗ω∈{0,1}d where c⃗ω =
 {
h if ⃗ω = ⃗σ ,
idG if ⃗ω ̸= ⃗σ . (83)

We also use the shorthand⃗1 = (1, 1, . . . , 1) ∈ {0, 1}d, where d will always be clear from the context. This
motivates us to define

K = K(T ) = {
h ∈ G ∣
∣ cd
⃗σ (h) ∈ Qd(T ) for all d ≥ 0 and ⃗σ ∈ {0, 1}d} . (84)

Since cd
⃗σ : G → G[d] is a group homomorphism for each d ≥ 0 and ⃗σ ∈ {0, 1}d, K is a group. As any cube
can be written as a product of cubes with a single non-identity entry, the condition H[d] ⊂ Qd(T ) for all
d ≥ 0 holds if and only if H < K. If T is an efficient group extension of an automaton then (84) and T2
guarantee that K < G0.

Proposition 7.7. Let T be an efficient GEA and let H < G be a normal subgroup. Then the following
conditions are equivalent:

1. T /H is a characteristic;

2. H < K(T ).

Proof. Immediate consequence of the above discussion.

We devote the remainder of this section to obtaining a description of K that is easier to work with.
Fix a value of d ≥ 0 for now, and let T be a GEA. For each 1 ≤ j ≤ d + 1, there is a natural projection
π j : {0, 1}d+1 → {0, 1}d which discards the j-th coordinate, that is,

π j(ω1, ω2, . . . , ω j−1, ω j, ω j+1, . . . ωd+1) = (ω1, . . . , ω j−1, ω j+1, . . . , ωd+1)

DISCRETE ANALYSIS, 2023:4, 62pp. 45

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

Accordingly, for each 1 ≤ j ≤ d + 1, we have the embedding ι j : G[d] → G[d+1] which copies the entries
along the j-th coordinate, that is,
 ι j(g) = (
gπ j(⃗ω))
⃗ω∈{0,1}d+1 .

Lemma 7.8. Let 1 ≤ j ≤ d + 1 and let T be an efficient GEA. Then

ι j (
Q
d(T )
) ⊂ Q
d+1(T ). (85)

Proof. Let ̃e = (l,⃗e) : vT
0 → vT
0 be a morphism in Vd(T ), and let g = λλλ (̃e) be an element of Qd(T ).
Then there is a corresponding morphism ̃f = (l, ⃗f ) : vT
0 → vT
0 in Vd+1(T ) obtained by inserting 0 in ⃗e
at j-th coordinate, that is,

( f0, f1, . . . , f j−1, f j, f j+1, . . . , fd+1) = (e0, e1, . . . , e j−1, 0, e j, . . . , ed).

It follows directly from the definition of λλλ that λλλ ( ̃f ) = ι j(λλλ (̃e)). Since ̃e was arbitrary, (85) follows.

Corollary 7.9. Let T be an efficient GEA. Then g[d] ∈ Qd(T ) for all d ≥ 0 and g ∈ G. Moreover, the
group K is normal in G and contained in G0.

Proof. The first statement follows from Lemma 7.5. The second one follows, since

c
d
⃗σ (ghg−1)g[d] = g[d]c
d
⃗σ (h) for all d ≥ 0, σ ∈ {0, 1}
d and g, h ∈ G.

Lemma 7.10. Let T be an efficient GEA and let h ∈ G. Suppose that for each d ≥ 0 there exists
⃗ρ = ⃗ρ(d) ∈ {0, 1}d such that cd
⃗ρ (h) ∈ Qd(T ). Then h ∈ K.

Proof. We need to show that cd
⃗σ (h) ∈ Qd(T ) for each d ≥ 0 and ⃗σ ∈ {0, 1}d. We proceed by double
induction, first on d and then on |{i ≤ d | σi ̸= ρi}|, where ⃗ρ = ⃗ρ(d). The cases d = 0 and ⃗σ = ⃗ρ are
clear.
Suppose now that d ≥ 1 and ⃗σ ̸= ⃗ρ. For the sake of notational convenience, assume further that
⃗ρ =⃗1; one can easily reduce to this case by reflecting along relevant axes. By inductive assumption
(with respect to ⃗σ ), Qd(T ) contains cd
⃗ω (h) for all ⃗ω ∈ {0, 1}d with |⃗ω| > |⃗σ |. Moreover, by inductive
assumption (with respect to d) and as Qd−1(T ) is a group, we have {id, h}[d−1] ⊆ Qd−1(T ). Consider
the product
 g = ∏
⃗ω≥⃗σ c
d
⃗ω (h) = (g⃗ω )⃗ω∈{0,1}d where g⃗ω =
 {
h if ⃗ω ≥ ⃗σ ,
idG otherwise,

where the order on {0, 1}d is defined coordinatewise, meaning that ⃗ω ≥ ⃗σ if and only if ω j ≥ σ j for all
1 ≤ j ≤ d. It follows from Lemma 7.8 that g ∈ Qd(T ). In fact g ∈ ι j({id, h}[d−1]) ⊆ ι j(Qd−1(T )) for
each 1 ≤ j ≤ d such that σ j = 0. It remains to notice that all terms in the product defining g, except for
cd
⃗σ (h), are independently known to belong to Qd(T ).

The following reformulation of Lemma 7.10 above will often be convenient.

DISCRETE ANALYSIS, 2023:4, 62pp. 46

GOWERS NORMS FOR AUTOMATIC SEQUENCES

Corollary 7.11. Let T be an efficient GEA and let g, h ∈ G. Suppose that for each d ≥ 0, the group
Qd(T ) contains a cube with h on one coordinate and g on all the remaining 2d − 1 coordinates. Then
g ≡ h mod K.

We are now ready to state the criterion for characteristicity of the quotient GEA in terms of the
generating set.

Corollary 7.12. Let T be an efficient GEA, let X ⊂ G be any set and put H := ⟨X⟩
G be the normal
closure of X. Suppose that for each h ∈ X and d ≥ 0 there exists ⃗ρ ∈ {0, 1}d such that cd
⃗ρ (h) ∈ Qd(T ).
Then the factor T /H is characteristic.

7.4 State space reduction

In this section we consider another basic way of constructing factor maps, namely by removing redun-
dancies in the set of states. Ultimately, we will reduce the number of states to 1 by repeatedly applying
Proposition 7.7 (which simplifies the group structure and hence makes some pairs of states equivalent)
and Proposition 7.14 below (which identifies equivalent states, leading to a smaller GEA). The following
example shows the kind of redundancy we have in mind.

Example 7.13. Consider the base-3 analogue of the Rudin–Shapiro sequence, given by the following
GEA with G = {+1, −1} and output function τ(s, g) = g (cf. Example 5.1).

s0start

s1 s2

1/+ 0/+ 2/+
0/+

1/− 2/−

0/+

1/−

2/−

The states s1 and s2 serve the same purpose and can be identified, leading to a smaller GEA:

s0start
 s∗

1,2/+ 0/+
 0/+

1,2/−

DISCRETE ANALYSIS, 2023:4, 62pp. 47

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

Motivated by the example above, for a GEA T we consider the equivalence relation ∼ of S, where
s ∼ s′ if and only if λ (s, u) = λ (s′, u) for all u ∈ Σ∗
k. Equivalently, ∼ is the minimal equivalence relation
such that s ∼ s′ implies that λ (s, j) = λ (s′, j) and δ (s, j) ∼ δ (s′, j) for all j ∈ Σk. We define the reduced
GEA Tred = ( ¯S, ¯s0, Σk, ¯δ , ¯λ , G), where ¯S = S/∼, ¯δ ( ¯s, j) = δ (s, j) and ¯λ ( ¯s, j) = λ (s, j) for all s ∈ S,
j ∈ Σk. There is a natural factor map T → ¯T given by (φ , idG) where φ : S → S/∼ takes s ∈ S to its
equivalence class. Note that if T is natural, then Lemma 7.6 guarantees that so is Tred.

Proposition 7.14. Let T be an efficient GEA. Then the factor Tred is characteristic.

Proof. Pick any d ≥ 0. Let S0 = {s ∈ S | s ∼ s0} be the equivalence class of s0. Any morphism
̃e = (l,⃗e) : ¯v0 → ¯v0 in Tred can be lifted to a morphism (l,⃗e) : (s, 0) → (s′, 0) in T , where s, s′ ∈ S[d]
0 .
Conversely, any morphism (l,⃗e) : (s, 0) → (s′, 0) in T with s, s′ ∈ S[d]
0 gives rise to the corresponding
morphism (l,⃗e) : ¯v0 → ¯v0. Hence,

Q
d(Tred) = ⋃

s,s′∈S[d]
0
 Qd(T )((s, 0), (s′, 0)). (86)

Let l be a large integer and let ⃗f = ([wT
0 ]k, 0, . . . , 0) ∈ Nd+1
0 6. Then 1⃗ω · ⃗f = [wT
0 ]k for each
⃗ω ∈ {0, 1}d, whence we have the morphism ̃f = (l, ⃗f ) : (s, 0) → vT
0 with λλλ ( ̃f ) = id
[d]
G for any s ∈
S[d]
0 . It follows from Lemma 7.2, that we can take g(s,0) = id
[d]
G , and said Lemma guarantees that

Qd(T ) ((s, 0), (s′, 0)) = Qd(T ) for all s, s′ ∈ S[d]
0 . Inserting this into (86) we conclude that Qd(Tred) =
Qd(T ), meaning that Tred is a characteristic factor of T .

7.5 Host–Kra cube groups

The groups Qd(T ) can be viewed as distant analogues of Host–Kra cube groups, originating from the
work of these two authors in ergodic theory [HK05, HK08] (the name, in turn, originates from [GT10b]).
Let G be a group and let d ≥ 0. The Host–Kra cube group HK
d(G) is the subgroup of G[d] generated
by the upper face cubes (
gJω j=1K)
⃗ω∈{0,1}d where 1 ≤ j ≤ d and g ∈ G. If G is abelian then HKd(G)

consists of the cubes g = (g⃗ω )⃗ω∈{0,1}d where g⃗ω = h0 ∏
d
j=1 hω j
j for some sequence h0, h1, . . . , hd ∈ G. In
general, let G = G0 = G1 ⊇ G2 ⊇ . . . be the lower central series of G, where for each i ≥ 1 the group
Gi+1 is generated by the commutators ghg−1h−1 with g ∈ Gi, h ∈ G. Let also ⃗σ1,⃗σ2, . . . ,⃗σ2d be an
ordering of {0, 1}d consistent with inclusion in the sense that if ⃗σi ≤ ⃗σ j (coordinatewise) then i ≤ j.
Then HKd(G) consists precisely of the cubes which can be written as g1g2 . . . g2d where for each j there
exists g j ∈ G|⃗σ j| such that g j = (
g j,⃗ω )
⃗ω∈{0,1}d and g j,⃗ω = g j if ⃗ω ≥ ⃗σ j (coordinatewise) and g j,⃗ω = idG
otherwise. The Host–Kra cube groups are usually considered for nilpotent groups G, that is, groups such
that Gs+1 = {idG} for some s ∈ N, called the step of G. (In fact, one can consider the Host–Kra cube
groups corresponding to filtrations other than the lower central series, but these are not relevant to the
discussion at hand.)
Let T be an invertible efficient GEA given by (Σk, G, λ ). Then a direct inspection of the definition
shows that Qd(T ) consists of all the cubes of the form (λ ((1⃗ω ·⃗e)k))⃗ω∈{0,1}d where⃗e ∈ Nk
0. In particular,

6We recall that wT
0 is a synchronizing word for T , i.e. for any s ∈ S we have δ (s, wT
0 ) = s0, λ (s, wT
0 ) = id.

DISCRETE ANALYSIS, 2023:4, 62pp. 48

GOWERS NORMS FOR AUTOMATIC SEQUENCES

letting ei = 0 for i ̸= j and taking e j ∈ N0 such that λ ((e j)k) = g (whose existence is guaranteed by T1)
we conclude that Qd(T ) contains the upper face cube corresponding to any g ∈ G and 1 ≤ j ≤ d. Hence,

Q
d(T ) ⊇ HK
d(G). (87)

In fact, the cube (λ ((1⃗ω ·⃗e)k))⃗ω∈{0,1}d belongs to HK
d(G) if ⃗e ∈ Nd+1
0 has non-overlapping digits in the
sense that for each m there is at most one j such that the m-th digit of (e j)k is non-zero. Since the cube
groups HKd(G) are relatively easy to describe, especially in the abelian case, one can view the indices
[Qd(T ) : HK
d(G)] (d ≥ 0) as a measure of complexity of T . We will ultimately reduce to the case when
Qd(T ) = HK
d(G).
As alluded to above, the inclusion in (87) can be strict. For instance, one can show that Q2(T ) =
HK2(G) if and only if λ ((e0)k)λ ((e0 +e1 +e2)k) ≡ λ ((e0 +e1)k)λ ((e0 +e2)k) mod G2 for all e0, e1, e2 ∈
N0. Suppose now, more generally, that Qd(T ) = HKd(G) for all d ≥ 0. Put G∞ := limn→∞ Gn. It follows
from Lemma 7.10 that K(T ) = G∞. If G is nilpotent then K(T ) = {idG} is trivial and consequently
T has no proper characteristic factors. If G is not nilpotent then the factor T /G∞ is characteristic,
and one can check that Qd(T /G∞) = HKd(G/G∞). In particular, iterating this reasoning we see that if
Qd(T ) = HKd(G) then T has a characteristic factor given by (Σk, ¯G, ¯λ ) where G is a nilpotent group.
In fact, this is only possible if G is a cyclic group, as shown by the following lemma. Since its importance
is purely as a motivation and we do not use it in the proof of our main results, we only provide a sketch of
the proof.

Lemma 7.15. Let T be an invertible efficient GEA given by (Σk, G, λ ). Assume further that G is nilpotent
and Qd(T ) = HKd(G) for all d ≥ 0. Then G is a subgroup of Z/(k − 1)Z and λ ((n)k) = λ (1)n for all
n ∈ Σk.

Sketch of a proof. Let s be the step of G so that Gs+1 = {idG}, and for ease of writing identify λ with
a map λ : N0 → G. Since λλλ = λ [d] maps parallelepipeds of the form (1⃗ω ·⃗e)⃗ω∈{0,1}d for ⃗e ∈ N
d+1
0 to
Qd(T ) = HKd(G), the sequence λ is a polynomial with respect to the lower central series (see e.g.
[GT12, Def. 1.8 and Prop. 6.5 ] for the relevant definition of a polynomial sequence). It follows [GT10a,
Lem. A.1] that there exist gi ∈ Gi for 0 ≤ i ≤ s such that

λ (n) = g0g
n
1g(
n
2)
2 . . . g(
n
s)
s , (n ∈ N0). (88)

Moreover, gi are uniquely determined by the sequence λ . Note also that g0 = idG since λ (0) = idG. We
will show that gi = idG for all i ≥ 2. In fact, we will show by induction on r that g2, g3, . . . , gr ∈ Gr+1 for
each r ≥ 1 (the case r = 1 being vacuously true).
Pick r ≥ 2 and assume that g2, g3, . . . , gr ∈ Gr. We will work modulo Gr+1, which means that (the
projections of) all of g1, g2, . . . , gr commute: gig jGr+1 = g jgiGr+1. It follows directly from how the
sequence λ is computed by T that for any m ≥ 0 and any I ⊂ N0 with |I| = m we have

λ (
∑l∈I kl) = λ ([10 j110 j2 . . . 10 jl ]k) = λ (1)
m = gm
1 , (89)

DISCRETE ANALYSIS, 2023:4, 62pp. 49

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

for some j1, . . . , jr ≥ 0. Let J = {l1, . . . , lr} be any set of cardinality |J| = r. Substituting (88) in (89) and
taking the oscillating product over all subsets I ⊂ J we conclude that

g
kl1 kl2 ·····klr
r ≡ ∏
I⊂J λ
 (
∑
l∈I kl)(−1)|I|
 ≡ idG (mod Gr+1), (90)

meaning that the order of gr in G/Gr+1 divides a power of k: gkLr
r ∈ Gr+1 for some Lr ≥ 0. (Equation
(90) can be verified by a direct computation, relying on the fact that the finite difference operator reduces
the degree of any polynomial by 1.)Reasoning inductively, we show that for each j = r − 1, r − 2, . . . , 2
there exists L j ≥ 0 such that gkL j
j ∈ Gr+1: towards this end, it is enough to repeat the same computation
as above with |J| = j and min J ≥ max(L j+1, . . . , Lr). In particular, there exists L∗ ≥ 0 such that for all
n ≥ 0 divisible by L∗ we have
 λ (n) = gn
1g
(
n
2)
2 . . . g(
n
s)
s ≡ gn
1 mod Gr+1. (91)

Next, recall that from how λ is computed by T it also follows that λ is invariant under dilation by k
in the sense that for any n ≥ 0 and any l ≥ 0 we have

λ (
nkl) = λ (n). (92)

Taking l ≥ L∗ and combining (88), (91) and (92), for any n ≥ 0 we obtain

gkl n
1 ≡ λ (kln) = λ (n) = g
n
1g
(
n
2)
2 . . . g
(
n
s)
s mod Gr+1. (93)

Since the representation of the sequence λ in the form (88) is unique, it follows that gr ≡ gr−1 ≡ · · · ≡
g2 ≡ idG mod Gr+1, which finishes this part of the argument.
We have now shown that g2 = g3 = · · · = gs = idG. It remains to notice that since gk
1 = λ (k) = λ (1) =
g1 and λ : N0 → G is surjective, the group G is cyclic and |G| | k − 1.

As suggested by the above lemma, group extensions of automata which arise from cyclic groups will
play an important role in our considerations. Let k ≥ 2 denote the basis, which we view as fixed. For
m ≥ 1 define the invertible GEA

Z(m) := (Σk, Z/mZ, λm) , λm : Σk ∋ j ↦→ j mod m ∈ Z/mZ. (94)

We will primarily be interested in the case when m | k − 1.

Lemma 7.16. Fix k ≥ 2 and let m, m′ ≥ 1 and let T be an efficient group extension of a k-automaton.

1. If m | k − 1 then the GEA Z(m) is efficient, λm(u) = [u]k mod m for all u ∈ Σ∗
k, and Qd(Z(m)) =
HKd(Z/mZ).

2. If m, m′ | k − 1 then Z(m) is a factor of Z(m′) if and only if m | m′. The factor is not characteristic
unless m = m′.
 DISCRETE ANALYSIS, 2023:4, 62pp. 50

GOWERS NORMS FOR AUTOMATIC SEQUENCES

3. If m | k − 1 then Z(m) is a factor of T if and only if m | d′
T .

4. If m | k − 1 and Z(m) is a characteristic factor of T then m = d′
T .

Proof. 1. Each of the defining properties of an efficient GEA can be verified directly (we take d′
0 = 1
and G0 = G).

2. This easily follows from the fact that Z/mZ is a subgroup of Z/m′Z if and only if m | m′.

3. Suppose first that Z(m) is a factor of T and the factor map is given by (φ , π). Then for any w ∈ Σ∗
k
with δ (s0, w) = s0 and λ (s0, w) = idG we have

0 = π(idG) = λm(w) = [w]k mod m.

Hence, by property T2, m | d′. In the opposite direction, property T2 guarantees that Z(d′) is a factor of
T , with the group homomorphism given by gr
0h ↦→ r mod d′ for all h ∈ G0, 0 ≤ r < d′. It remains to
notice that if m | d′ then Z(m) is a factor of Z(d′).

4. We already know that m | d′
T so it remains to show that m ≥ d′
T . Consider the probability p that a
random cube g ∈ G[2] belongs to Qd(T ). On one hand, since Z(d′
T ) is a factor of T , we have p ≤ 1/d′
T
(three coordinates of g determine the projection of the fourth to Z/d′
T Z). On the other hand, since Z(m)
is characteristic, we have p = 1/m. It follows that m ≥ d′
T .

We are now ready to reformulate our description of the cube groups Qd(T ) in Theorem (6.11) in a
more succinct way using the language of characteristic factors. Equivalence of the said theorem and the
following result is easily seen once one unwinds the definitions.

Theorem 7.17. Let T be an efficient GEA. Then Z(d′
T ) is a characteristic factor of T .

7.6 Strong synchronisation

Recall that efficient GEA are built on automata that are synchronising. A stronger synchronisation
property is enjoyed, for example, by the GEA producing the Rudin–Shapiro sequence discussed in
Example 5.1: all sufficiently long words are synchronising for the underlying automaton (in fact, all
nonempty words have this property). In this section we show that, passing to a characteristic factor, we
can ensure this stronger synchronisation property for the underlying automata in general.
Let T be a GEA. For the purposes of this section, we will say that a pair of states s, s′ ∈ S is mistakable
if for every length l there exists a word u ∈ Σ∗
k with |u| ≥ l and two states r, r′ ∈ S such that δ (r, u) = s and
δ (r′, u) = s′. Note that in this situation u cannot be a synchronising word for the underlying automaton
unless s = s′. We will also say that the pair s, s′ ∈ S is strongly mistakable if there exists a nonempty word
w ∈ Σ∗
k \ {ε} such that δ (s, w) = s and δ (s′, w) = s′, while λ (s, w) = λ (s′, w) = idG. As the terminology
suggests, if s, s′ are strongly mistakable then they are also mistakable (we may take u = wl and r = s,
r′ = s′). The following lemma elucidates the connection between mistakable states and synchronisation.

Lemma 7.18. Let T be a natural tranducer and let A be the underlying automaton. Then the following
properties are equivalent:
 DISCRETE ANALYSIS, 2023:4, 62pp. 51

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

1. There exists a pair of distinct mistakable states s, s′ ∈ S.

2. There exists a pair of distinct strongly mistakable states s, s′ ∈ S.

3. There exist infinitely many words in Σ∗
k which are not synchronising for A.

Proof. As any pair of strongly mistakable states is mistakable, (2) implies (1). Moreover, as we have
remarked above, (1) implies (3).
In the reverse direction, (3) implies (1): indeed, if (3) holds, then there exist infinitely many words
ui ∈ Σ∗
k (i ∈ N) with corresponding quadruples ri, r′
i, si, s′
i ∈ S such that si ̸= s′
i and δ (ri, ui) = si, δ (r′
i, ui) =
s′
i. Any pair s, s′ ∈ S such that s = si and s′ = s′
i for infinitely many values of i is mistakable, so (1) holds.
It remains to show that (1) implies (2). By definition, it follows from (1) that there exists a word
u = u1u2 . . . ul ∈ Σ∗
k with |u| = l ≥ |S|
2 and states r, r′, s, s′ ∈ S with s ̸= s′ such that δ (r, u) = s and
δ (r′, u) = s′. For 0 ≤ i ≤ l, let si and s′
i be the states reached form r and r′ respectively after reading the
first i digits of u. More precisely, si, s′
i are given by s0 = r, s′
0 = r′ and si = δ (si−1, ui), s′
i = δ (s′
i−1, ui) for
all 1 ≤ i ≤ l. Note that since sl ̸= s′
l we have more generally si ̸= s′
i for all 0 ≤ i ≤ l. By the pigdeonhole
principle, there exists a pair of indices 0 ≤ i < j ≤ l and a pair of states t,t′ such that si = s j = t and
s′
i = s′
j = t′. Put v = ui+1ui+2 . . . u j so that δ (t, v) = t and δ (t′, v) = t′. Finally, put w = v|G| so that
δ (t, w) = t and δ (t′, w) = t′ and by the Lagrange’s theorem we have λ (t, w) = λ (t, v)
|G| = idG and
likewise λ (t′, w) = idG. It follows that t,t′ are strongly mistakable.

Proposition 7.19. Let T be an efficient GEA. Then T has a characteristic factor ¯T such that every
sufficiently long word is synchronizing for the underlying automaton.

The proof of Proposition 7.19 proceeds by iterating the following lemma.

Lemma 7.20. Let T be an efficient GEA and let H < G be given by

H = 〈
λ (s, u)
−1λ (s′, u) : s and s
′ are strongly mistakable, u ∈ Σ
∗
k〉G . (95)

Then ¯T /H is a characteristic factor of T .

Proof. Recall from Section 7.3 that it will suffice to verify that H < K = K(T ). Let h be one of the
generators of H in (95). Pick a pair of strongly mistakable states s, s′ ∈ S and a word u ∈ Σ∗
k such
that h = λ (s, u)−1λ (s′, u). Replacing u with uwT
0 , where wT
0 is a synchronizing word of T , we may
assume without loss of generality that u synchronises the underlying automaton to s0, so in particular
δ (s, u) = δ (s′, u) = s0.
In order to construct the relevant morphism (l,⃗e) : vT
0 → vT
0 , we first need to specify several auxiliary
words with certain helpful properties, described by the diagram below. Let w be a word such that
δ (s0, w) = s and λ (s0, w) = idG, whose existence is guaranteed by property T1. Let v1 be a word such
that δ (s, v1) = s, δ (s′, v1) = s′, and λ (s, v1) = λ (s′, v1) = idG, which exists because s, s′ are strongly
mistakable. Lastly, let v0 be a word such that δ (s, v0) = δ (s′, v0) = s′ and λ (s′, v0) = λ (s′, v0) = idG.
One can obtain such a word by concatenating wT
0 with a word taking s0 to s′ with identity group label,
whose existence is guaranteed by property T1.

DISCRETE ANALYSIS, 2023:4, 62pp. 52

GOWERS NORMS FOR AUTOMATIC SEQUENCES

s0 s

s′

w/idG v1/idG

v1/idGv0/idG

0/idG
 v0/idG

We may additionally assume that the words v1 and v0 have the same length m; otherwise we can replace
them with v|v1|
0 and v|v2|
1 respectively. Note that v0 ̸= v1 since s ̸= s′. Assume for concreteness that
[v0]k < [v1]k; the argument in the case [v0]k > [v1]k is analogous. Let v = ([v1]k − [v0]k)
m
k be the result of
subtracting v0 from v1. Put also l = |w| + dm + |u|. We are now ready to define the coordinates ei, which
are given by
 e0 = [w v0v0 . . . v0︸ ︷︷ ︸
d times u]k; e j = [v 0m0m . . . 0m
︸ ︷︷ ︸
d − j times 0|u|]k (0 < j ≤ d).

This definition is set up so that for each ⃗ω ∈ {0, 1}d we have

1⃗ω ·⃗e = [wvω1vω2 . . . vωd u]k.

Since u synchronises the underlying automaton of T to s0 and 1⃗ω ·⃗e < kl for each ⃗ω ∈ {0, 1}d, it follows
directly from (53) that we have a morphism ̃e = (l,⃗e) : vT
0 → vT
0 , and so λλλ (̃e) ∈ Qd(T ). Our next step
is to compute λλλ (̃e).
It follows directly from the properties of w, v0 and v1 listed above that

δ (s0, wvω1vω2 . . . vω j ) =
 {
s, if ω1 = ω2 = · · · = ω j = 1,
s′, otherwise.

for any ⃗ω ∈ {0, 1}d and 0 ≤ j ≤ d (the case j = 0 corresponds to δ (s0, w) = s). Hence, for any ⃗ω ∈ {0, 1}d

different from⃗1 we have

λ (s0, (1ω ·⃗e)
l
k) = λ (s0, w)λ (s, v1) j−1λ (s, v0)λ (s
′, vω j+1) . . . λ (s
′, vωd )λ (s
′, u)

= λ (s′, u),

where j is the first index with ω j = 0. For ⃗ω =⃗1 we obtain a similar formula, which simplifies to

λ (s0, (⃗1 ·⃗e)
l
k) = λ (s, u).

Since d ≥ 0 was arbitrary, it follows from Corollary 7.11 that λ (s, u) ≡ λ (s′, u) mod K, and consequently
H < K, as needed.

Proof of Proposition 7.19. Let T ′ := (T /H)red, where H = H(T ) is given by (95). Recall that T ′ is
efficient by Lemma 7.6. Note that either

DISCRETE ANALYSIS, 2023:4, 62pp. 53

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

1. T ′ is a proper factor of T ; or

2. all sufficiently long words synchronise the underlying automaton of T .

Indeed, if (2) does not hold then it follows from Lemma 7.18 that there exists a pair of distinct strongly
mistakable states s, s′ ∈ S. The definition of H guarantees that the images of those states in T /H give
rise to the same label maps: ¯λ (s, u) = ¯λ (s′, u) for all u ∈ Σ∗
k. It follows that s and s′ are mapped to the
same state in (T /H)red. In particular, (T /H)red has strictly fewer states than T .
Iterating the construction described above, we obtain a sequence of characteristic factors

T ′ → T ′′ → · · · → T (n) → T (n+1) → . . . ,

where T (n+1) = (
T (n))′ = (
T (n)/H(T (n))
)

red for each n ≥ 0. Since all objects under consideration
are finite, this sequence needs to stabilise at some point, meaning that there exists n ≥ 0 such that
T (n) = T (n+1) = · · · := ¯T . Since ¯T ′ = ¯T , it follows from the discussion above that all sufficiently
long words are synchronising for the underlying automaton of ¯T . By Lemma 7.20, ¯T is a characteristic
factor of T .

Example 7.21. Consider the GEA described by the following diagram, where g, h ∈ G are two distinct
group elements.
 s0
 s1

s2

1/id

2/id
 1/g

1/h

0/id 2/id2/id

0/id

0/id

The word 0 is synchronising for the GEA and no word in {1, 2}∗ is synchronising for the underlying
automaton. The states s1 and s2 are strongly mistakable and the loops are given by 1m where m is any
common multiple of the orders of g and h. The group H in Lemma 7.20 is generated by gh−1 and its
conjugates, and the GEA T ′ = ¯T in the proof of Proposition 7.19 is obtained by collapsing s1 and s2
into a single state.

7.7 Invertible factors

In this section we further reduce the number of states of the GEA under consideration. In fact, we show
that it is enough to consider GEA with just a single state. Recall that such GEAs with one states are
called invertible.
 DISCRETE ANALYSIS, 2023:4, 62pp. 54

GOWERS NORMS FOR AUTOMATIC SEQUENCES

Proposition 7.22. Let T be an efficient GEA such that all sufficiently long words are synchronising for
the underlying automaton. Then T has an invertible characteristic factor.

It will be convenient to say for any N, L ≥ 0 that a GEA T is (N, L)-nondiscriminating if λ (s, u) =
λ (s′, u) for all s, s′ ∈ S and all u ∈ ΣL
k such that [u]k < N. In particular, any GEA T is vacuously (0, L)-
nondiscriminating for all L ≥ 0, and if T is additionally efficient then it is (1, L)-nondiscriminating for
all L ≥ 0 (recall that efficiency implies that λ (s, 0) = idG for all s ∈ S). Our proximate goal on the path to
prove Proposition 7.22 is to find a characteristic factor that is (N, L)-nondiscriminating for all N, L ≥ 0.
Indeed, note that any invertible GEA is (N, L)-nondiscriminating for all N, L ≥ 0. Conversely, as we will
shortly see, a GEA that is (N, L)-nondiscriminating for all N, L ≥ 0 can be reduced to an invertible GEA
by removing redundant states.

Lemma 7.23. Let T be an efficient group extension of a k-automaton. Suppose that there exist L ≥ 1 and
N ≥ kL such that T is (N, L)-nondiscriminating. Then T is (N, L)-nondiscriminating for all N, L ≥ 0.

Proof. It is clear that the property of being (N, L)-nondiscriminating becomes stronger as N increases.
The values of N above kL will be mostly irrelevant: if T is (kL, L)-nondiscriminating then it is immediate
that it is (N, kL)-nondiscriminating for all N ≥ 0. By assumption, T is (kL, L)-nondiscriminating for at
least one L ≥ 1. Let L denote the set of all L ≥ 0 with the aforementioned property (in particular, 0 ∈ L).
If L1, L2 ∈ L then also L1 + L2 ∈ L. Indeed, any u ∈ Σ
L1+L2
k can be written as u = u1u2 with u1 ∈ Σ
L1
k
and u2 ∈ Σ
L2
k , whence for any s, s′ ∈ S we have λ (s, u) = λ (s0, u1)λ (s0, u2) = λ (s′, u). Moreover, if L ∈ L
and L ̸= 0 then L − 1 ∈ L. Indeed, if u ∈ Σ
L−1
k then for any s, s′ ∈ S we have λ (s, u) = λ (s0, u0) = λ (s′, u).
It remains to note that the only set L ⊂ N0 with all of the properties listed above is N0.

Lemma 7.24. Let T be an efficient group extension of a k-automaton, let A be the underlying au-
tomaton and 0 < N < kL. Suppose that every word in ΣL
k is synchronising for A and that T is (N, L)-
nondiscriminating. Then T has a characteristic factor T ′ which is (N + 1, L)-nondiscriminating.

Proof. Following a strategy similar to the one employed in the proof of Proposition 7.19, let u = (N)L
k
and consider the normal subgroup of G given by

H := 〈
λ (s, u)
−1λ (s′, u) : s, s
′ ∈ S〉G . (96)

We aim to use Proposition 7.7 to show that T /H is a characteristic factor of T . Fix for now the
dimension d ≥ 0 and an integer M such that kM > d. Pick s ∈ S and a word v such that δ (s0, v) = s and
λ (s0, v) = idG, whose existence is guaranteed by property T1. We recall that wT
0 denotes a word that
synchronizes T to s0. Consider ⃗e ∈ Nd+1
0 given by

e0 = [vu0Mw
T
0 ]k − d[10|wT
0 |]k; e j = [10|wT
0 |]k (0 < j ≤ d).

Put also l := |v| + L + M + ∣
∣wT
0 ∣
∣ and let u′ := (N − 1)L
k . These definitions are arranged so that for each
⃗ω ∈ {0, 1}d the word (1⃗ω ·⃗e)l
k takes the form

(1⃗ω ·⃗e)
l
k =
 {
vu′x⃗ω wT
0 if ⃗ω ̸=⃗1;
vu0MwT
0 if ⃗ω =⃗1,

DISCRETE ANALYSIS, 2023:4, 62pp. 55

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

where x⃗ω = (kM − d + |⃗ω|)M
k ∈ ΣM
k . Since for each ⃗ω ∈ {0, 1}d the word (1⃗ω ·⃗e)l
k ends with wT
0 and
(1⃗ω ·⃗e)k < kL, the data constructed above describes a morphism ̃e = (l,⃗e) : vT
0 → vT
0 .

ss0start
 s1

s′
1

v/id
 u/λ (s, u)

u′/λ (s, u′)

x⃗ω wT
0 /λ (s′
1, x⃗ω )

0MwT
0 /id

Our next step is to compute λλλ (̃e). In fact, we only need some basic facts rather than a complete
description. For ⃗ω ̸= 1d we have

λ (
s0, (1⃗ω ·⃗e)
l
k)
) = λ (s0, v)λ (s, u
′)λ (δ (s, u
′), x⃗ω )λ (δ (s, u
′x⃗ω ), wT
0 )

= λ (s0, u
′)λ (s′
1, x⃗ω ),

where the state s′
1 = δ (s, u′) is independent of s because u′ is synchronising for A, and λ (s, u′) = λ (s0, u′)
because T is (N, L)-nondiscriminating. Similarly,

λ (
s0, (⃗1 ·⃗e)
l
k)
) = λ (s, u0M) = λ (s, u).

Note that out of all the coordinates of λλλ (̃e), only one depends on s. Let s′ ∈ S be any other state, and
let ̃e′ : vT
0 → vT
0 be the result of applying the same construction as above with s′ in place of s. Then

λλλ (̃e)λλλ (̃e
′)
−1 = cd
⃗1 (
λ (s, u)λ (s′, u)
−1) ∈ Qd(T ).

Since d ≥ 0 was arbitrary, it follows from Lemma 7.10 that λ (s, u) ≡ λ (s′, u) mod K. Since s, s′ ∈ S
were arbitrary, H < K and hence T /H is a characteristic factor.
Let ¯T = T /H. Then ¯T is (N, L)-nondiscriminating because T is. Moreover, it follows directly from
the definition of H that ¯λ (s, u) = ¯λ (s′, u) for all s, s′ ∈ S, whence ¯T is (N + 1, L)-nondiscriminating.

Proof of Proposition 7.22. Let L ≥ 0 be large enough that all words of length ≥ L are synchronising for
A. Applying Lemma 7.24 we can construct a sequence of characteristic factors

T = T0 → T1 → · · · → TkL

such that for each 0 ≤ N ≤ kL the GEA TN is (N, L)-nondiscriminating. In particular, T has a charac-
teristic factor ¯T = TkL which is (kL, L)-nondiscriminating. Hence, ¯T ′ is (N, M)-nondiscriminating for
all N, M ≥ 0 by Lemma 7.23. Next, it follows directly from the construction that ¯Tred is invertible. It
remains to recall that ¯Tred is a characteristic factor of T by Lemma 7.14.

DISCRETE ANALYSIS, 2023:4, 62pp. 56

GOWERS NORMS FOR AUTOMATIC SEQUENCES

Example 7.25. Consider the GEA described by the following diagram. Then each of the first three
applications of Lemma 7.24 removes one of the group labels gi.

s0 s10/id 1/id 2/id 3/id
0/id

1/g1

2/g2

3/g3

7.8 Invertible group extensions of automata

In this section we deal exclusively with invertible group extensions of automata. As pointed out in
Section 5.1, an invertible GEA can be identified with a triple (Σk, G, λ ) where λ : Σk → G is a labelling
map. By a slight abuse of notation we identify λ with a map N0 → G, denoted with the same symbol,
λ (n) = λ ((n)k). Recall that the cyclic group extensions of automata Z(m) were defined in Section 7.5.

Proposition 7.26. Let T be an invertible efficient group extension of a k-automaton. Then T has a
characteristic factor of the form Z(m) for some m which divides k − 1.

Proof. Following the usual strategy (cf. Propositions 7.19 and 7.22), we will consider the normal subgroup
of G given by
 H = 〈
λ (n + 1)λ (1)
−1λ (n)
−1 : n ≥ 0〉G . (97)

A simple inductive argument shows that λ (n) ≡ λ (1)n mod H for all n ≥ 0, and in fact H is the normal
subgroup of G generated by λ (n)λ (1)−n for n ≥ 0. In particular, G/H is cyclic.
We will show that the factor T /H is characteristic. Fix d ≥ 0, take any n ≥ 0. Let t = |G| so that
gt = idG for all g ∈ G. Consider the vector ⃗e ∈ N
d+1
0 given by

e0 = nk
td + 1; e j = (k
t − 1)k(d− j)t (1 ≤ j ≤ d).

Put also l = |(n)k| + td + 1 so that 1⃗ω ·⃗e < kl for all ⃗ω ∈ {0, 1}d and hence we have a morphism
̃e = (l,⃗e) : vT
0 → vT
0 . We next compute λλλ (̃e). If ⃗ω ∈ {0, 1}d \ {⃗1} and 0 ≤ j ≤ d be the largest index
such that ω j = 0, then (1⃗ω ·⃗e)
l
k = 0(n)kvω1vω2 . . . vω j−10
t−110
t(d− j),

DISCRETE ANALYSIS, 2023:4, 62pp. 57

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

where v1 = (kt − 1)k ∈ Σt
k and v0 = 0t ∈ Σt
k. Since λ (v0) = λ (v1) = idG, we have

λ (1⃗ω ·⃗e)
l
k = λ (n)λ (1).

By a similar reasoning, λ (
(⃗1 ·⃗e)
l
k) = λ (n + 1) .

Since d ≥ 0 was arbitrary, it follows by Corollary 7.11 that λ (n + 1) ≡ λ (n)λ (1) mod K. Since n was
arbitrary, H < K and T /H = (Σk, G/H, ¯λ ) is characteristic. Let m denote the order the cyclic group
G/H. Because ¯λ (n) = ¯λ (1)n for all n ≥ 0, T /H is isomorphic to Z(m), and because λ (1) = λ (k) ≡
λ (1)k mod H, m is a divisor of k − 1.

7.9 The end of the chase

In this section we finish the proof of the main result of this section. This task is virtually finished — we
just need to combine the ingredients obtained previously.

Proof of Theorem 6.11. Chaining together Propositions 7.19, 7.22 and 7.26 we conclude that the efficient
GEA T has a characteristic factor of the form Z(m) with m | k − 1. By Lemma 7.16 it follows that
m = d′
T .

Acknowledgments

The authors thank the anonymous reviewers for their careful reading of the paper and the feedback.

References

[ADM] Boris Adamczewski, Michael Drmota, and Clemens Müllner. (logarithmic) densities for
automatic sequences along primes and squares. 5

[AS03] Jean-Paul Allouche and Jeffrey Shallit. Automatic sequences. Cambridge University Press,
Cambridge, 2003. 11, 12

[BHK05] Vitaly Bergelson, Bernard Host, and Bryna Kra. Multiple recurrence and nilsequences.
Invent. Math., 160(2):261–303, 2005. With an appendix by Imre Ruzsa. 6

[BK19a] Jakub Byszewski and Jakub Konieczny. Automatic sequences and generalised polynomials.
Canadian Journal of Mathematics, 2019. To appear. 24

[BK19b] Jakub Byszewski and Jakub Konieczny. A density version of Cobham’s Theorem. To
appear in Acta Arithmetica, 2019+. arXiv: 1710.07261 [math.CO]. 13

[BKPLR16] Vitaly Bergelson, Joanna Kułaga-Przymus, Mariusz Lema´nczyk, and Florian K. Richter. Ra-
tionally almost periodic sequences, polynomial multiple recurrence and symbolic dynamics,
2016. 3, 15
 DISCRETE ANALYSIS, 2023:4, 62pp. 58

GOWERS NORMS FOR AUTOMATIC SEQUENCES

[BR02] V. Bergelson and I. Ruzsa. Squarefree numbers, IP sets and ergodic theory. In Paul Erd˝os
and his mathematics, I (Budapest, 1999), volume 11 of Bolyai Soc. Math. Stud., pages
147–160. János Bolyai Math. Soc., Budapest, 2002. 3

[DDM15] Jean-Marc Deshouillers, Michael Drmota, and Clemens Müllner. Automatic sequences
generated by synchronizing automata fulfill the Sarnak conjecture. Studia Math., 231(1):83–
95, 2015. 15

[DM12] Michael Drmota and Johannes F. Morgenbesser. Generalized Thue-Morse sequences of
squares. Israel J. Math., 190:157–193, 2012. 12

[DMR11] Michael Drmota, Christian Mauduit, and Joël Rivat. The sum-of-digits function of polyno-
mial sequences. J. Lond. Math. Soc., 84(1):81–102, 2011. 2

[DMR13] Michael Drmota, Christian Mauduit, and Joël Rivat. The Thue-Morse sequence along
squares is normal, 2013. Preprint. 2, 5

[EK18] Tanja Eisner and Jakub Konieczny. Automatic sequences as good weights for ergodic
theorems. Discrete Contin. Dyn. Syst., 38(8):4087–4115, 2018. 2

[ET12] Tanja Eisner and Terence Tao. Large values of the Gowers-Host-Kra seminorms. J. Anal.
Math., 117:133–186, 2012. 8

[FH91] William Fulton and Joe Harris. Representation theory, volume 129 of Graduate Texts in
Mathematics. Springer-Verlag, New York, 1991. A first course, Readings in Mathematics.
30

[FH17] Nikos Frantzikinakis and Bernard Host. Higher order Fourier analysis of multiplicative
functions and applications. J. Amer. Math. Soc., 30(1):67–157, 2017. 2

[FK19] Aihua Fan and Jakub Konieczny. On uniformity of q-multiplicative sequences. Bulletin of
the London Mathematical Society, 2019. 6

[FKM13] Étienne Fouvry, Emmanuel Kowalski, and Philippe Michel. An inverse theorem for Gowers
norms of trace functions over Fp. Math. Proc. Cambridge Philos. Soc., 155(2):277–295,
2013. 6

[Gel68] A. O. Gel’fond. Sur les nombres qui ont des propriétés additives et multiplicatives données.
Acta Arith., 13:259–265, 1967/1968. 2

[Gow01] W. T. Gowers. A new proof of Szemerédi’s theorem. Geom. Funct. Anal., 11(3):465–588,
2001. 7

[Gre] Ben Green. Higher-Order Fourier Analysis, I. (Notes available from the author). 7

[GT10a] Ben Green and Terence Tao. An arithmetic regularity lemma, an associated counting
lemma, and applications. In An irregular mind, volume 21 of Bolyai Soc. Math. Stud., pages
261–334. János Bolyai Math. Soc., Budapest, 2010. 2, 6, 20, 23, 49

DISCRETE ANALYSIS, 2023:4, 62pp. 59

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

[GT10b] Ben Green and Terence Tao. Linear equations in primes. Ann. of Math. (2), 171(3):1753–
1850, 2010. 48

[GT12] Ben Green and Terence Tao. The quantitative behaviour of polynomial orbits on nilmani-
folds. Ann. of Math. (2), 175(2):465–540, 2012. 49

[GTZ12] Ben Green, Terence Tao, and Tamar Ziegler. An inverse theorem for the Gowers U s+1[N]-
norm. Ann. of Math. (2), 176(2):1231–1372, 2012. 2

[HK05] Bernard Host and Bryna Kra. Nonconventional ergodic averages and nilmanifolds. Ann. of
Math. (2), 161(1):397–488, 2005. 48

[HK08] Bernard Host and Bryna Kra. Parallelepipeds, nilpotent groups and Gowers norms. Bull.
Soc. Math. France, 136(3):405–437, 2008. 48

[Kim99] Dong-Hyun Kim. On the joint distribution of q-additive functions in residue classes. J.
Number Theory, 74(2):307–336, 1999. 2

[Kon19] Jakub Konieczny. Gowers norms for the Thue–Morse and Rudin–Shapiro sequences. To
appear in Annales de l’Institut Fourier, 2019+. arXiv: 1611.09985 [math.NT]. 2, 32

[Liu11] Huaning Liu. Gowers uniformity norm and pseudorandom measures of the pseudorandom
binary sequences. Int. J. Number Theory, 7(5):1279–1302, 2011. 6

[LM18] Mariusz Lema´nczyk and Clemens Müllner. Automatic sequences are orthogonal to aperiodic
multiplicative functions. arXiv e-prints, page arXiv:1811.00594, Nov 2018. 24

[Min88] Henryk Minc. Nonnegative matrices. Wiley-Interscience Series in Discrete Mathematics and
Optimization. John Wiley & Sons, Inc., New York, 1988. A Wiley-Interscience Publication.
39

[Mor08] Johannes Morgenbesser. Gelfond’s sum of digits problems. Master’s thesis, TU Wien, 2008.
2

[MR09] Christian Mauduit and Joël Rivat. La somme des chiffres des carrés. Acta Math., 203(1):107–
148, 2009. 2

[MR10] Christian Mauduit and Joël Rivat. Sur un problème de Gelfond: la somme des chiffres des
nombres premiers. Ann. of Math. (2), 171(3):1591–1646, 2010. 2

[MR15] Christian Mauduit and Joël Rivat. Prime numbers along Rudin-Shapiro sequences. J. Eur.
Math. Soc. (JEMS), 17(10):2595–2642, 2015. 2, 5

[MR18] Christian Mauduit and Joël Rivat. Rudin-Shapiro sequences along squares. Trans. Amer.
Math. Soc., 370(11):7899–7921, 2018. 2

[MS98] Christian Mauduit and András Sárközy. On finite pseudorandom binary sequences. II. The
Champernowne, Rudin-Shapiro, and Thue-Morse sequences, a further construction. J.
Number Theory, 73(2):256–276, 1998. 2

DISCRETE ANALYSIS, 2023:4, 62pp. 60

GOWERS NORMS FOR AUTOMATIC SEQUENCES

[MS15] Clemens Müllner and Lukas Spiegelhofer. Normality of the Thue-Morse sequence along
Piatetski-Shapiro sequences, II, 2015. Preprint. arXiv:1511.01671 [math.NT]. 2

[Mül17] Clemens Müllner. Automatic sequences fulfill the Sarnak conjecture. Duke Math. J.,
166(17):3219–3290, 2017. 5, 24, 26, 27, 28, 29, 30

[Mül18] Clemens Müllner. The Rudin-Shapiro sequence and similar sequences are normal along
squares. Canad. J. Math., 70(5):1096–1129, 2018. 2, 5

[NR09] Harald Niederreiter and Joël Rivat. On the Gowers norm of pseudorandom binary sequences.
Bull. Aust. Math. Soc., 79(2):259–271, 2009. 6

[Spi18] Lukas Spiegelhofer. The level of distribution of the Thue–Morse sequence. arXiv e-prints,
page arXiv:1803.01689, Mar 2018. 2, 5

[Tao12] Terence Tao. Higher order Fourier analysis, volume 142 of Graduate Studies in Mathemat-
ics. American Mathematical Society, Providence, RI, 2012. 7, 8, 32

[TV06] Terence Tao and Van Vu. Additive combinatorics, volume 105 of Cambridge Studies in
Advanced Mathematics. Cambridge University Press, Cambridge, 2006. 6

AUTHORS

Jakub Byszewski
Faculty of Mathematics and Computer Science
Jagiellonian University
Łojasiewicza 6
30-348 Kraków, Poland
jakub byszewski uj edu pl

Jakub Konieczny
Camille Jordan Institute
Claude Bernard University Lyon 1
43 Boulevard du 11 novembre 1918
69622 Villeurbanne Cedex, France

Faculty of Mathematics and Computer Science
Jagiellonian University
Łojasiewicza 6
30-348 Kraków, Poland
jakub konieczny gmail com

DISCRETE ANALYSIS, 2023:4, 62pp. 61

JAKUB BYSZEWSKI, JAKUB KONIECZNY, AND CLEMENS M ¨ULLNER

Clemens Müllner
Institut für Diskrete Mathematik und Geometrie
TU Wien
Wiedner Hauptstr. 8–10
1040 Wien, Austria
clemens muellner tuwien ac at

DISCRETE ANALYSIS, 2023:4, 62pp. 62
