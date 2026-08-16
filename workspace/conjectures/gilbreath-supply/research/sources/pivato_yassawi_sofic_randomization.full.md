<!-- source: https://arxiv.org/pdf/math/0306136 | converted from PDF -->

arXiv:math/0306136v2  [math.DS]  13 Apr 2006
Ergod. Th. & Dynam. Sys. (2006), 26, 1–26
Printed in the United Kingdom c⃝ 2006 Cambridge University Press

Asymptotic Randomization of Soﬁc Shifts by
Linear Cellular Automata†

Marcus Pivato and Reem Yassawi

Department of Mathematics, Trent University, 1600 West Bank Drive, Peterborough,
Ontario, K9J 7B8, Canada
(e-mail: marcuspivato@trentu.ca and ryassawi@trentu.ca)

(Received July 31, 2004; accepted April 6, 2006 )

Abstract. Let M = Z
D be a D-dimensional lattice, and let (A, +) be an abelian group.
A
M is then a compact abelian group under componentwise addition. A continuous function
Φ : A
M−→A
M is called a linear cellular automaton (LCA) if there is a ﬁnite subset F ⊂ M
and nonzero coeﬃcients ϕf ∈ Z so that, for any a ∈ A
M, Φ(a) = ∑
f∈F ϕf · σf (a).
Suppose µ is a probability measure on A
M whose support is a subshift of ﬁnite type or
soﬁc shift. We provide suﬃcient conditions (on Φ and µ) under which Φ asymptotically
randomizes µ, meaning that wk∗− lim
J∋j→∞ Φjµ = η, where η is the Haar measure on A
M,

and J ⊂ N has Ces`aro density 1. In the case when Φ = 1 + σ and A = (Z/p)
s (p prime), we
provide a condition on µ that is both necessary and suﬃcient. We then use this to construct
zero-entropy measures which are randomized by 1 + σ.

MSC: Primary: 37B15; Secondary: 37A50

Let D ≥ 1, and let M := Z
D be the D-dimensional lattice. If A is a (discretely
topologised) ﬁnite set, then A
M is compact in the Tychonoﬀ topology. For any v ∈ M,
let σv : A
M−→A
M be the shift map: σv(a) := [
bm|m∈M], where bm := am−v, ∀m ∈ M.
A cellular automaton (CA) is a continuous map Φ : A
M−→A
M which commutes with all
shifts: for any m ∈ M, σm ◦ Φ = Φ ◦ σm. Let η be the uniform Bernoulli measure on
A
M. If µ is another probability measure on A
M, we say Φ asymptotically randomizes µ if
wk∗− lim
J∋j→∞ Φjµ = η, where J ⊂ N has Ces`aro density one.

If (A, +) is a ﬁnite abelian group, then A
M is a product group, and η is the Haar measure.
A linear cellular automaton (LCA) is a CA Φ with a ﬁnite subset F ⊂ M (with # (F) ≥ 2),
and nonzero coeﬃcients ϕf ∈ Z (for all f ∈ F) so that, for any a ∈ A
M,

Φ(a) = ∑

f∈F ϕf · σf(a). (1)

† This research was partially supported by NSERC Canada, and was also supported by the kind hospitality
of the Universidad de Chile during July 2003.

Prepared using etds.cls [Version: 1999/07/21 v1.0]

2 M. Pivato and R. Yassawi

Linear cellular automata are known to asymptotically randomize a wide variety of measures
[MM98, MM99, MHM03, Lin84, FMMN00], including those satisfying a correlation-
decay condition called harmonic mixing [PY02, PY04, MMPY06]. However, all known
suﬃcient conditions for asymptotic randomization (and for harmonic mixing, in particular)
require µ to have full support, i.e. supp (µ) = A
M.

We here investigate asymptotic randomization when supp (µ) ⊊ A
M. In particular we
consider the case when supp (µ) is a soﬁc shift or subshift of ﬁnite type. In §1, we let
A = Z/p (p prime), and demonstrate asymptotic randomization for any Markov random
ﬁeld that is locally free, a much weaker assumption than full support. However, in §2 we
show that harmonic mixing is a rather restrictive condition, by exhibiting a measure whose
support is a mixing soﬁc shift but which is not harmonically mixing.

Thus, in §3, we introduce the less restrictive concept of dispersion mixing (for measures)
and the dual concept of dispersion (for LCA), and state our main result: any dispersive
LCA asymptotically randomizes any dispersion mixing measure. In §4, we let A = (Z/p)
s

(p prime, s ∈ N) and introduce bipartite LCA, a broad class exempliﬁed by the automaton
1 + σ. We then show that any bipartite LCA is dispersive.

In §5, we show that any uniformly mixing and harmonically bounded measure is dispersion
mixing. In particular, in §6, we show this implies that any mixing Markov measure
(supported on a subshift of ﬁnite type), and any continuous factor of a mixing Markov
measure (supported on a soﬁc shift) is dispersion mixing, and thus, is asymptotically
randomized by any dispersive LCA (e.g. 1 + σ). Thus, the example of §2 is asymptotically
randomized, even though it is not harmonically mixing.

In §7, we reﬁne the results of §3-§4 by introducing Lucas mixing, (a weaker condition
than dispersion mixing). When A = (Z/p)
s, we show that a measure is asymptotically
randomized by the automaton 1 + σ if and only if it is Lucas mixing. Finally, in §8, we
use Lucas mixing to construct a class of zero-entropy measures which are asymptotically
randomized by randomized by 1 + σ, thereby refuting the conjecture that positive entropy
is necessary for asymptotic randomization.

Preliminaries & Notation: Throughout, (A, +) is an abelian group (usually A =
(Z/p)
s,where p is prime and s ∈ N). Elements of A
M are denoted by boldfaced letters
(e.g. a, b, c), and subsets by gothic letters (e.g. A, B, C). Elements of M are sans serif
(e.g. l, m, n) and subsets are U, V, W.

If U ⊂ M and a ∈ A
M then aU := [au|u∈U] is the ‘restriction’ of a to an element of
A
U. For any b ∈ A
U, let [b] := {c ∈ A
M ; cU = b} be the corresponding cylinder set. In
particular, if a ∈ A
M, then [aU] := {c ∈ A
M ; cU = aU}
.

Measures: Let M(A
M) be the set of Borel probability measures on A
M. If µ ∈ M(A
M)
and I ⊂ M, then let µI ∈ M(A
I) be the marginal projection of µ onto A
I. If J ⊂ M and
b ∈ A
J, then let µ(b) ∈ M(A
M) be the conditional probability measure in the cylinder set
[b]. In other words, for any X ⊂ A
M, µ(b)[X] := µ (X ∩ [b]) /µ [b]. In particular, if I ⊂ M
is ﬁnite, then µ(b)
I ∈ M(A
M) is the conditional probability measure on the I coordinates:
for any c ∈ A
I, µ(b)
I [c] := µ ([c] ∩ [b]) /µ [b].

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 3

Subshifts: A subshift [Kit98, LM95] is a a closed, shift-invariant subset X ⊂ A
M. If
U ⊂ M, then let XU := {xU ; x ∈ X} be all admissible U-blocks in X. If U ⊂ M is ﬁnite,
and W = {w1, . . . , wN } ⊂ A
U is a collection of admissible blocks, then the induced subshift
of ﬁnite type (SFT) is the largest subshift X ⊂ A
M such that XU = W. In other words,
X := ⋂
m∈M σm [W], where [W] := {
a ∈ A
M ; aU ∈ W}. A soﬁc shift is the image of an
SFT under a block map.
In particular, if M = Z and U = {0, 1}, then X is called topological Markov shift, and the
transition matrix of X is the matrix P = [pab]a,b∈A, where pab = 1 if [ab] ∈ W, and pab = 0
if [ab] ̸∈ W.

Characters: Let T
1 ⊂ C be the circle group. A character of A
M is a continuous
homomorphism χ : A
M−→T
1; the group of such characters is denoted ̂AM. For any χ ∈ ̂AM

there is a ﬁnite subset K ⊂ M, and nontrivial χk ∈ ̂A for all k ∈ K, such that, for any
a ∈ A
M, χ(a) = ∏

k∈K χk(ak). We indicate this by writing: “χ = ⊗

k∈K χk”. The rank of χ

is the cardinality of K.

Ces`aro Density: If ℓ, n ∈ Z, then let [ℓ...n) := {m ∈ Z ; ℓ ≤ m < n}. If J ⊂ N, then the

Ces`aro density of J is deﬁned: density (J) := lim
N →∞ 1
N # (
J ∩ [0...N )
)
. If J, K ⊂ N, then

their relative Ces`aro density is deﬁned:

rel density [J/K] := lim
N →∞ # (J ∩ [0...N ))
# (K ∩ [0...N )) .

In particular, density (J) = rel density [J/N].

1. Harmonic Mixing of Markov Random Fields
Let B ⊂ M be a ﬁnite subset, symmetric under multiplication by −1 (usually, B =
{−1, 0, 1}D). For any U ⊂ M, we deﬁne

cl (U) := {u + b ; u ∈ U and b ∈ B} and ∂U := cl (U) \ U.

For example, if M = Z and B = {−1, 0, 1}, then ∂{0} = {±1}.
Let µ ∈ M(A
M). Suppose U ⊂ M, and let V := ∂U and W = M \ cl (U). If b ∈ A
V, then
we say b isolates U from W if the conditional measure µ(b) is a product of µ(b)
U and µ(b)
W .
That is, for any U ⊂ A
U and W ⊂ A
W, we have µ(b) (U ∩ W) = µ(b)
U (U) · µ(b)
W (W).
We say that µ is a Markov random ﬁeld [Br´e99, KS80] with interaction range B (or write,
“µ is a B-MRF”) if, for any U ⊂ M with V = ∂U and W = M \ cl (U), any choice of b ∈ A
V

isolates U from W.
For example, if M = Z and B = {−1, 0, 1}, then µ is a B-MRF iﬀ µ is a (one-step) Markov
chain. If B = [−N...N ], then µ is a B-MRF iﬀ µ is an N -step Markov chain.

Lemma 1.1. If µ is a Markov random ﬁeld, then supp (µ) is a subshift of ﬁnite type. ✷

For example, if µ is a Markov chain on A
Z, then supp (µ) is a topological Markov shift.

Let B ⊂ M, and let µ ∈ M(A
M) be B-MRF. Let S := B \ {0}. For any b ∈ A
S, let
µ(b)
0 ∈ M(A) be the conditional probability measure on the zeroth coordinate. We say that

µ is locally free if, for any b ∈ A
S, # (
supp (µ(b)
0 )) ≥ 2.

Prepared using etds.cls

4 M. Pivato and R. Yassawi

Example: If D = 1, then B = {−1, 0, 1}, S = {±1}, and µ is a Markov chain. Thus,
supp (µ) is a topological Markov shift, with transition matrix P = [pab]a,b∈A. For any
a, b ∈ A, write a ❀ b if pab = 1, and deﬁne the follower and predecessor sets

F (a) := {b ∈ A ; a ❀ b} and P (b) := {a ∈ A ; a ❀ b}.

It is easy to show that the following are equivalent:
1. µ is locally free.
2. Every entry of P
2 is 2 or larger.
3. For any a, b ∈ A, # (F (a) ∩ P (b)) ≥ 2.
Recall that ̂A is the dual group of A. For any χ ∈ ̂A and ν ∈ M(A), let ⟨χ, ν⟩ :=∑

a∈A χ(a) · ν{a}. It is easy to check:

Lemma 1.2. Let p be prime and A = Z/p. If µ is a locally free MRF on A
M, then there is

some c < 1 such that, for all nontrivial χ ∈ ̂A, and any b ∈ A
S, ∣
∣
∣〈χ, µ(b)
0 〉∣
∣
∣ ≤ c. ✷

For any χ ∈ ̂AM and µ ∈ M (
A
M)
, deﬁne ⟨χ, µ⟩ := ∫

AM χ(a) dµ[a]. A measure µ is

called harmonically mixing if, for any ǫ > 0, there is some R ∈ N such that, for any χ ∈ ̂AM,
(rank [χ] > R) =⇒ (
|⟨χ, µ⟩| < ǫ) .

The signiﬁcance of this is the following [PY02, Theorem 12]:

Theorem: Let A = Z/p, where p is prime. Any LCA on A
M asymptotically randomizes
any harmonically mixing measure. ✷

Most MRFs with full support are harmonically mixing [PY04, Theorem 15]. We now
extend this.

Theorem 1.3. Let A = Z/p, where p is prime. Any locally free MRF on A
M is
harmonically mixing.

Proof. Let µ be a locally free B-MRF. A subset I ⊂ M is B-separated if (i − j) ̸∈ B for all
i, j ∈ I with i ̸= j. Let K ⊂ M be ﬁnite, and let χ := ⊗

k∈K χk be a character of A
M.

Claim 1: Let K := # (K) = rank [χ], and let B := max {|b1 − b2| ; b1, b2 ∈ B}. There
exists a B-separated subset I ⊂ K such that

# (I) = I ≥ K
BD . (2)

Proof. Let ̃B := [0...B)D be a box of sidelength B. Cover K with disjoint translated copies
of ̃B, so that K ⊂ ⊔

i∈I
 (̃B + i)

for some set I ⊂ K. Thus, |i − j| ≥ B for any i, j ∈ I with i ̸= j, so (i − j) ̸∈ B. Also,

# (̃B
) = BD, so each copy covers at most BD points in K. Thus, we require at least

K
BD copies to cover all of K. In other words, I ≥ K
BD . ✸ Claim 1

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 5

Thus, χ = χI · χK\I, where χI(a) := ∏

i∈I χi(ai), and χK\I(a) := ∏

k∈K\I χk(ak).

Let J := (∂ I) ∪ (K \ I); ﬁx b ∈ A
J, and let µ(b)
I ∈ M(A
I) be the corresponding
conditional probability measure. Since µ is a Markov random ﬁeld, and the I coordinates
are ‘isolated’ from one another by J coordinates, it follows that µ(b)
I is a product measure.
In other words, for any a ∈ A
I,
 µ(b)
I [a] = ∏

i∈I µ(b)
i {ai}. (3)

Thus, the conditional expectation of χI is given:
〈χI, µ(b)
I 〉 = ∑

a∈AI µ(b)
I [a] ·
 (∏

i∈I χi(ai)

)
 (∗) ∑

a∈AI
 (∏

i∈I µ(b)
i {ai} · χi(ai)

)

= ∏

i∈I
 ( ∑

ai∈A µ(b){ai} · χi(ai)

)
 = ∏

i∈I
 〈χi, µ(b)
i 〉,

where (∗) is by equation (3). Thus, 〈χ, µ(b)〉 = χK\I(b) · 〈
χI, µ(b)
I 〉 = χK\I(b) ·
∏

i∈I
 〈χi, µ(b)
i 〉. Thus, if I = # (I), then

∣
∣
∣〈
χ, µ(b)〉∣
∣
∣ = ∣
∣
∣χK\I(b)
∣
∣
∣ · ∏

i∈I
 ∣
∣
∣〈
χi, µ(b)
i 〉∣
∣
∣ ≤ 1 · cI (4)

where the last step follows from Lemma 1.2. But ⟨χ, µ⟩ = ∑

b∈AJ µ[b] · 〈χ, µ(b)〉
, so

|⟨χ, µ⟩| ≤ ∑

b∈AJ µ[b]·∣
∣
∣〈
χ, µ(b)〉∣
∣
∣ ≤

(∗)
 ∑

b∈AJ µ[b]·cI = cI ≤

(†) cK/(BD )−−−−
K→∞−→0.

Here (∗) is by equation (4) and (†) is by equation (2). ✷

2. The Even Shift is Not Harmonically Mixing
We will now construct a measure ν, supported on a soﬁc shift, which is not harmonically
mixing. Nonetheless, we’ll show in §3-§5 that this measure is asymptotically randomized by
many LCA.
Let X ⊂ (
Z/3)Z be the subshift of ﬁnite type deﬁned by the transition matrix

A =
 

 1 0 1
1 0 1
0 1 0
 

, where, ∀i, j ∈ Z/3, aij = { 1 if j ❀ i is allowed
0 if j ❀ i is not allowed

Let Φ : X → (
Z/2)Z be the factor map of radius 0 which sends 0 into 0 and both 1 and 2 to
1. Then S := Φ(X) is Weiss’s Even Soﬁc Shift: if s ∈ S, then there are an even number
of 1’s between any two occurrences of 0 in s.
For any N ∈ N, and i, j ∈ Z/3, let XN
ij := {x ∈ X ; x0 = i, xN = j}, and let:

EN :=
 {
s ∈ S ;
 N∑

n=0 sn is even
 }
, and ON :=
 {
s ∈ S ;
 N∑

n=0 sn is odd
 }
.

Prepared using etds.cls

6 M. Pivato and R. Yassawi

Lemma 2.1. ∀i, j ∈ Z/3, either Φ (
XN
i,j) ⊂ EN or Φ (
XN
i,j) ⊂ ON . In particular,

Φ (
XN
0,0 ⊔ XN
1,2 ⊔ XN
2,1 ⊔ XN
0,2 ⊔ XN
1,0) = EN and Φ (
XN
1,1 ⊔ XN
0,1 ⊔ XN
2,0 ⊔ XN
2,2) = ON .

Proof. Let x ∈ XN
ij , and s := Φ(x). Note that, if k < k∗ are any two values such that

xk = 0 = xk∗ , then
 k∗
∑

n=k sn is even. In particular, let k be the ﬁrst element of [0...N ] where

xk = 0, and let k∗ be the last element of [0...N ] where xk∗ = 0. Thus,
 k∗
∑

n=k sn ≡ 0 (mod 2),

so that
 N∑

n=0 sn ≡
 k−1∑

n=0 sn +
 N∑

n=k∗+1 sn (mod 2).

But since xk−1 ̸= 0 ̸= xk∗+1 by construction, the deﬁnition of X forces xk−1 = 2 and

xk∗+1 = 1. Thus the parity of
 k−1∑

n=0 sn depends only on the value of x0 = i. Similarly the

parity of
 N∑

n=k∗+1 sn depends only on xN = j. ✷

Let µ ∈ M [X] be a mixing Markov measure on X, with transition matrix P and Perron
measure ρ = (ρ0, ρ1, ρ2) ∈ M [
Z/3]. Let ν := Φµ ∈ M [S], so that if U ⊂ S is measurable,
then ν[U] := µ [
Φ−1(U)
].

For all N ∈ N, deﬁne character χN by χN (x) :=
 N∏

n=0
(−1)
xn for all x ∈ (
Z/2)Z. Then

Lemma 2.1 implies:

⟨χN , ν⟩ = ν(EN ) − ν(ON )

= µ (
XN
0,0 ⊔ XN
1,2 ⊔ XN
2,1 ⊔ XN
0,2 ⊔ XN
1,0) − ν (XN
1,1 ⊔ XN
0,1 ⊔ XN
2,0 ⊔ XN
2,2) .

But µ is mixing, so lim
N →∞ µ(XN
i,j) = ρi · ρj. Thus, lim
N →∞ ⟨χN , ν⟩ = ρ2
0 + 2ρ1ρ2 − ρ2
1 − ρ2
2.

So for example if
 P =
 

 1/2 0 1/2
1/2 0 1/2
0 1 0
 



with Perron measure ρ = ( 2
5 , 1
5 , 2
5 )
, then lim
N →∞ ⟨χN , ν⟩ ̸= 0. But clearly, rank [χN ] = N ,

so that lim
N →∞ rank [χN ] = ∞. Thus ν is not harmonically mixing.

3. Dispersion Mixing
The example from §2 suggests the need for an asymptotic randomization condition on
measures that is less restrictive than harmonic mixing. In this section, we’ll deﬁne the
concepts of dispersion mixing (for measures) and dispersion (for automata) which together
yield asymptotic randomization. In §4 we’ll show that many LCA are dispersive. In §5
and §6 we’ll show that many measures (including the Even Shift measure ν from §2) are
dispersion mixing.

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 7

Let Φ be an LCA as in equation (1). The advantage of this ‘polynomial’ notation is that
composition of two LCA corresponds to multiplication of their respective polynomials. For
example, suppose A = (Z/p)
s, where p ∈ N is prime, and s ∈ N. Suppose M = Z and
Φ = 1 + σ; that is, Φ(a)0 = a0 + a1 (mod p). Then the Binomial Theorem implies:

For any N ∈ N, ΦN =
 N∑

n=0
 [ N
n
 ]
p σn, where [ N
n
 ]
p := ( N
n
 ) mod p. (5)

Let S > 0, and let K, J ⊂ M be subsets. We say that K and J are S-separated if

min {|k − j| ; k ∈ K and j ∈ J} ≥ S

If F, G ⊂ M, and Φ = ∑

f∈F ϕf · σf and Γ = ∑

g∈G γg · σg are two LCA, then we say Φ and

Γ are S-separated if F and G are S-separated. Likewise, if K, X ⊂ M, and χ = ⊗

k∈K χk

and ξ = ⊗

x∈X ξx are two characters, then we say χ and ξ are S-separated if K and X are

S-separated.
If Φ = ∑

f∈F ϕf · σf is an LCA, then let rankS (Φ) be the maximum number of S-separated

LCA which can be summed to yield Φ. That is:

rankS (Φ) := max {R ; ∃ Φ1, . . . , ΦR mutually S-separated, with Φ = Φ1 + · · · + ΦR}
.

For example, if Φ = 1 + σ5 + σ6 + σ11 + σ12 + σ13,

then rank4 (Φ) = 3, because Φ = Φ1 + Φ2 + Φ3, where

Φ1 = 1, Φ2 = σ5 + σ6, and Φ3 = σ11 + σ12 + σ13.

On the other hand, clearly, rank1 (Φ) = 6, while rank7 (Φ) = 1.
Likewise, if χ = ⊗

k∈K χk is a character, and S > 0, then we deﬁne

rankS (χ) := max {
R ; ∃ χ1, . . . , χR mutually S-separated, with χ = χ1 ⊗ · · · ⊗ χR}
.

(In the notation of §1, rank [χ] = rank1 (χ).)
We say that µ is dispersion mixing (DM) if, for every ǫ > 0, there exist S, R > 0 such that,

for any character χ ∈ ̂AM, (rankS (χ) > R) =⇒ (
|⟨χ, µ⟩| < ǫ
). Note that dispersion
mixing is less restrictive than harmonic mixing.
If Φ is an LCA and χ is a character, then χ ◦ Φ is also a character. We say that Φ is
dispersive if, for any S > 0, and any character χ ∈ ̂AM, there is a subset J ⊂ N of density 1
such that lim
J∋j→∞ rankS (
χ ◦ Φj) = ∞. It follows:

Theorem 3.1. Let A be any ﬁnite abelian group. If Φ : A
M−→A
M is a dispersive LCA
and µ ∈ M(A
M) is dispersion mixing, then Φ asymptotically randomizes µ. ✷

Theorem 3.1 is an immediate consequence of an easily veriﬁed lemma:

Prepared using etds.cls

8 M. Pivato and R. Yassawi

Lemma 3.2. Φ asymptotically randomizes µ if and only if, for all χ ∈ ̂AM, there is a subset
J ⊂ N with density (J) = 1, such that lim
J∋j→∞
 ∣
∣
∣〈
χ ◦ Φj, µ〉∣
∣
∣ = 0.

Proof. See the proof of Theorem 12 in [PY02]. ✷

4. Dispersion and Bipartite CA
If m = (m1, m2, . . . , mD) ∈ M, then let |m| := |m1| + |m2| + · · · + |mD|. If Γ = ∑

g∈G γg · σg

is a linear cellular automaton, then deﬁne diam [Γ] := max {|g − h| ; g, h ∈ G}.
The centre of Γ is the centroid of G (as a subset of Rn):

centre (Γ) := 1
# (G)
 ∑

g∈G g.

We say Γ is centred if |centre (Γ)| < 1. For any prime p ∈ N, let

Kp := min { 1
2 , 4p − 7
4p + 4
 } . Thus, K2 = 1
12 , K3 = 5
16 , and Kp = 1
2 , for p ≥ 5.

Let A := (Z/p)
s (where p is prime and s ∈ N). If Φ : A
M−→A
M is an LCA, then we say Φ
is bipartite if Φ = 1 + Γ ◦ σf , where Γ is centred and diam [Γ] ≤ Kp · |f|. For example:

Φ = 1 + σf is bipartite for any nonzero f ∈ M and any prime p ∈ N.
Φ = 1 + σ12 + σ13 = 1 + (1 + σ) ◦ σ12 is bipartite for any prime p ∈ N.
Φ = 1 + σ14 + σ19 = 1 + (
σ−2 + σ3) ◦ σ16 is bipartite for any prime p ≥ 3.
Φ = 1 + σ2 + σ3 = 1 + (1 + σ) ◦ σ2 is bipartite for any prime p ≥ 5.

Our goal in this section is to prove:

Theorem 4.1. Let A = (Z/p)
s, where p prime and s ∈ N. If Φ is bipartite, then Φ is
dispersive. ✷

For any N ∈ N, let [
N (i)|∞
i=0] denote the p-ary expansion of N , so that N =
 ∞∑

i=0 N (i)pi.

Let L (N ) := {n ∈ [0...N ] ; n(i) ≤ N (i), for all i ∈ N}.

Lemma 4.2. (Lucas’s Theorem)

(a) [ N
n
 ]
p =
 ∞∏

i=0
 [ N (i)

n(i)
 ]
p, where we deﬁne [ N (i)

n(i) ]
p := 0 if n(i) > N (i), and [ 0
0 ]
p := 1.

(b) Thus, [ N
n ]

p ̸= 0 iﬀ n ∈ L (N ). ✷

For example, suppose M = Z and Φ = 1 + σ. If we interpret equation (5) in the light of

Lemma 4.2, we get: ΦN = ∑

n∈L(N )
 [ N
n
 ]

p σn.

Lemma 4.3. Let r, H ∈ N.

(a) If M < pr, and N = M + pr · H, then L (N ) = L (M ) + pr · L (H) (see Figure 1).

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 9

L(H)
 L(H)

L(N)

L(M) pr

Figure 1. Lemma 4.3.

(b) If m ∈ L (M ), h ∈ L (H), and n = m + pr · h, then [ N
n
 ]
p = [ M
m
 ]
p · [ H
h
 ]

p. ✷

For example, suppose p = 2 and N = 53 = 5 + 48 = 5 + 24 · 3. Then M = 5, r = 4,
and H = 3, and

L (53) = L (5) + 24 · L (3) = {0, 1, 4, 5} + 16 · {0, 1, 2, 3}

= {0, 1, 4, 5, 16, 17, 20, 21, 32, 33, 37, 38, 48, 49, 52, 53}.

If χ = ⊗

k∈K χk is a character, then deﬁne diam [χ] := max {|k − j| ; k, j ∈ K}. It follows:

Lemma 4.4. Let Φ be an LCA, and let S > 0.
(a) If χ is a character, and S0 = S + diam [χ], then rankS (χ ◦ Φ) ≥ rankS0 (Φ).

(b) If Γ is an LCA, and S0 = S + diam [Γ], then rankS (Γ ◦ Φ) ≥ rankS0 (Φ). ✷

Corollary 4.5. Φ is dispersive if and only if, for any S0 > 0, there is a subset J ⊂ N of
density 1 such that lim
J∋j→∞ rankS0 (
Φj) = ∞. ✷

To prove Theorem 4.1, we’ll use Lemma 4.3 to verify the condition of Corollary 4.5. For
any S0 > 0, deﬁne

J(S0) := {
N ∈ N ; N = MN + prN HN , for some HN , rN > 0 such that MN , S0 < prN −1}
.

For example, if p = 2 and S0 = 7, then 53 ∈ J(7), because 53 = 5 + 24 · 3, so that
M53 = 5, r53 = 4, and H53 = 3. Thus, 2r53−1 = 23 = 8, and 7 < 8 and 5 < 8. Note that
53 = 20 + 22 + 24 + 25; thus, 53(3) = 0. This is exactly why 53 ∈ J(7):

Lemma 4.6. J(S0) = {N ∈ N ; N ≥ p · S0, and N (r) = 0 for some r ∈ (
logp(S0) . . . logp(N )
]}
.

Proof. Suppose N = MN + prN HN , for some HN , rN > 0 and MN ≥ 0, such that
MN , S0 < prN −1. Let r := rN − 1; then N (r) = 0 and logp(S0) < r < logp(N ).

Conversely, suppose N (r) = 0, where logp(S0) < r < logp(N ). Let rN := r + 1; then

S0 < pr = prN −1. Let MN :=
 r−1∑

i=0 N (i)pi; then MN < pr = prN −1 also. Now let

HN :=
 ∞∑

i=rN N (i)pi−rN ; then N = MN + prN HN . ✷

Prepared using etds.cls

10 M. Pivato and R. Yassawi

Lemma 4.7. density (J(S0)) = 1.

Proof. Let I := [pS0 . . . ∞]. Then I is a set of density one, and Lemma 4.6 implies that

I \ J(S0) = {
N ∈ I ; N (r) ̸= 0 for all r ∈ (
logp(S0) . . . logp(N )
]},

which is a set of density zero. It follows that density (J(S0)) = density (I) = 1. ✷

Lemma 4.8. If N ∈ J(S0), and N = M + prH, then ΦN = ΦM ◦ ΘH , where Θ = Φ(p
r).

Proof. Recall that Φ = 1 + Γ ◦ σf . Thus,

ΦN
 (L) ∑

n∈L(N )
 [ N
n
 ]
p
 (
Γ ◦ σf)n
 (‡) ∑

m∈L(M)
 ∑

h∈L(H)
 [ H
h
 ]
p
 [ M
m
 ]
p
 (
Γ ◦ σf)(m+p
rh)

= ∑

h∈L(H)
 [ H
h
 ]

p
 

 ∑

m∈L(M)
 [ M
m
 ]
p
 (
Γ ◦ σf )m

 ◦ (Γ ◦ σf )hp
r

(†) ∑

h∈L(H)
 [ H
h
 ]

p ΦM ◦ (
Γ ◦ σf)p
r h
 (⋆) ΦM ◦ ΘH .

(L) is by Lucas Theorem and (‡) is by Lemma 4.3(b). (†) is because ΦM =
∑

m∈L(M)
 [ M
m
 ]

p
 (
Γ ◦ σf )m. Finally, (⋆) is because Θ = (1 + Γ ◦ σf )p
r
 (L) 1 + (Γ ◦ σf )
p
r .

Thus, ΘH
 (L) ∑

h∈L(H)
 [ H
h
 ]
p
 (Γ ◦ σf )p
r h. ✷

Proof of Theorem 4.1. It suﬃces to verify the condition of Corollary 4.5. So, let
S1 := S0 + diam [ΦM ]. Then

rankS0 (
ΦN )
 (∗) rankS0 (
ΦM ◦ ΘH ) ≥

(†) rankS1 (
ΘH ) . (6)

where (∗) is by Lemma 4.8 and (†) is by Lemma 4.4(b). Thus, we want to show that
rankS1 (
ΘH ) −−−−
H→∞−→∞ for H in a set of density 1. To do this, we’ll use gaps in L (H). If
h0, h1 ∈ L (H), we say that h0 and h1 bracket a gap if:

(i) h1 ≥ p · h0 and (ii) [h0...h1) ∩ L (H) = ∅.

Claim 1: Let h0, h1 ∈ L (H), with p ≤ h0 < h1, and suppose h0 and h1 bracket a gap

in L (H). Then (Γ ◦ σf )p
r h0 and (
Γ ◦ σf)p
r h1 are S1-separated.

Proof. Suppose |h0 − h1| = w. Then (
σf )p
rh0 and (
σf )p
r h1. are (pr · w · |f|)-separated.

Thus, if D = diam [Γ], then (
Γ ◦ σf)p
r h0 and (Γ ◦ σf )p
r h1 are W -separated, where

W := prw|f| − (
diam [
Γpr h0] + diam [Γprh1 ]) = prw|f| − (prh0D + prh1D)

≥ pr · (w|f| − D · (h1 + h0)
) . (7)

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 11

L(H)

prh1 prh2 prh3 prh4 prh5 prh6 prh7 prh8

L(H)pr
 Γ
prh5

prh4 D prh5 D

w

pr w |f|

W > pr[w |f| -(h4+h5) D]

Γ prh1 Γ prh2Γ prh3 Γ
prh4 Γ
prh6 Γ prh7 Γ prh8

Figure 2. Claim 1 of Theorem 4.1.

(see Figure 2). We want W ≥ S1, or, equivalently, W − diam [
ΦM ] ≥ S0 (because
S1 = S0 + diam [ΦM ]). First, note that

diam [ΦM ] ≤ M · |f| + 2 · max
m∈L(M) diam [Γm] = M · |f| + 2M · D

= M · (|f| + 2D) ≤ pr−1 · (|f| + 2D) . (8)

Thus,
 W − diam [ΦM ] ≥

(∗) pr · (w · |f| − D · (h1 + h0)
) − pr−1 · (|f| + 2D)

= pr−1 · (pw · |f| − pD · (h1 + h0) − |f| − 2D)

≥

(†) S0 · (
pw · |f| − pD · (h1 + h0) − |f| − 2D) .

where (∗) is by equations (7) and (8), and (†) is because S0 < pr−1.
Thus, it suﬃces to show that

pw · |f| − pD · (h1 + h0) − |f| − 2D ≥ 1.

To see this, observe that

pw · |f| − pD · (h1 + h0) − |f| − 2D

= (pw − 1) · |f| − [p · (h1 + h0) − 2] · D ≥

(♭) (pw − 1) · |f| − [
p · (h1 + h0) − 2] · Kp · |f|

= (
pw − 1 − [p · (h1 + h0) − 2] Kp) · |f| ≥

(∗) p · (h1 − h0) − 1 − [p · (h1 + h0) − 2] Kp

= p · ((1 − Kp) · h1 − (1 + Kp) · h0) − (1 + 2 · Kp)

≥

(†) p · ((1 − Kp) · p − (1 + Kp)
) · h0 − 2 ≥

(‡) p2 · (
(1 − Kp) · p − (1 + Kp)
) − 2

≥

(⋆) 3
4 p2 − 2 ≥

(⋄) 3 − 2 = 1.

Prepared using etds.cls

12 M. Pivato and R. Yassawi

(♭) is by hypothesis that Γ is bipartite. (∗) is because |f| ≥ 1, and w = h1 − h0.

(†) is because h1 ≥ p · h0, and Kp ≤ 1
2 . (‡) is because h0 ≥ p.

(⋆) is because Kp ≤ 4p−7
4p+4 = p− 7
4
p+1 , thus, (p + 1)Kp ≤ p − 7
4 = p − 1 − 3
4 ; thus,
3
4 ≤ (p − 1) − (p + 1)Kp = (1 − Kp)p − (1 + Kp).

(⋄) is because p ≥ 2, so p2 ≥ 4.

It follows that W − diam [ΦM ] ≥ S0, so that W ≥ S1. ✸ Claim 1

Let rank [H] := # of gaps in L (H). Then Claim 1 implies that

rankS1 (
ΘH ) ≥ rank [H]. (9)

Thus, we want to show that the number of gaps is large.

Suppose i < k. We say that i and k bracket a zero-block in the p-ary expansion of H
if H (i−1) ̸= 0 ̸= H (k), but H (j) = 0, for all i ≤ j < k. For example, suppose p = 2 and
H = 19. Then 3 and 5 bracket a zero block in the binary expansion ...010011.

Claim 2: If i and k bracket a zero-block in the p-ary expansion of H, then pi and pj

bracket a gap in L (H).

Proof. H (i) = 0, so the largest element in L (H) less than pi is

h0 =
 i−1∑

j=1 H (j) · pj ≤
 i−1∑

j=1(p − 1) · pj = pi − 1.

Now, k = min {
j > i ; H (j) ̸= 0}
, so h1 = pk is the smallest element in L (H) greater
than pi. Also, h1 ≥ pi+1 > p · (pi − 1) ≥ p · h0. ✸ Claim 2

Let #ZB (H) := #of zero-blocks in the p-ary expansion of H.

Then Claim 2 implies that
 rank [H] ≥ #ZB (H) . (10)

Deﬁne H := {
H ∈ N ; #ZB (H) ≥ 1
p3 logp(H)
}
.

Claim 3: density (H) = 1.

Proof. Observe that #ZB (H) is no less than the number of occurrences of the word “101”
in the p-ary expansion of H (because 101 is a zero-block). Let

H′ := {
H ∈ N ; (# of occurrences of “101”) ≥ 1
p3 logp(H)
}
.

Then H′ ⊂ H. The Weak Law of Large Numbers implies density (H′) = 1. ✸ Claim 3

Deﬁne J := {N ∈ J(S0) ; N = MN + prN HN , where rN ≤ 1
2 logp(N ), and HN ∈ H}
.

Claim 4: density (J) = 1.

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 13

Proof. J = J1 ∩ J2, where

J1 := {N ∈ J(S0) ; N = MN + prN HN , where HN ∈ H}

and J2 := {N ∈ J(S0) ; N = MN + prN HN , where rN ≤ 1
2 logp(N )
}.

Now, density (J1) = 1 by Lemma 4.7 and Claim 3. To see that density (J2) = 1, note that

J(S0) \ J2 ⊂ {
N ∈ N ; N (r) ̸= 0 for all r ∈ (
logp(S0) . . . 1
2 logp(N )
]}
,

which is a set of density zero. ✸ Claim 4

If N = MN + prN HN is an element of J, then

logp(HN ) ≥ logp(N ) − rN ≥ logp(N ) − 1
2 logp(N ) = 1
2 logp(N ). (11)

Thus,
 rankS0 (
ΦN ) ≥

(♥) rankS1 (
ΘHN ) ≥

(♦) rank [HN ] ≥

(♣) #ZB (HN )

≥

(∗) 1
p3 logp(HN ) ≥

(♠) 1
2p3 logp(N ).

Here, (♥) is by equation (6), (♦) is by equation (9), (♣) is by equation (10), (♠) is by
equation (11), and (∗) is because H ∈ H by hypothesis.

Thus lim
J∋N →∞ rankS0 (
ΦN ) ≥ 1
2p3 lim
J∋N →∞ logp(N ) = ∞. ✷

5. Uniform Mixing and Dispersion Mixing
A measure µ ∈ M(A
Z) is uniformly mixing if, for any ǫ > 0, there is some M > 0 such that,
for any cylinder subsets L ⊂ A
(−∞...0] and R ⊂ A
[0...∞), and any m > M ,

µ [σm(L) ∩ R] ̃ǫ µ [L] · µ [R] (12)

(here, “x ̃ǫ y” means |x − y| < ǫ.)

Example 5.1:

⟨a⟩ Any mixing N -step Markov chain is uniformly mixing. (See §6).

⟨b⟩ If ν ∈ M(BZ) is uniformly mixing, and Ψ : BZ−→A
Z is a block map, then µ := Φ(ν)
is also uniformly mixing. (If Ψ has local map ψ : B[−ℓ...r]−→A, then replace the M
in (12) with M + ℓ + r + 1).

⟨c⟩ Hence, if F ⊂ BZ is an SFT, and S := Ψ(F) ⊂ A
Z a soﬁc shift, and ν ∈ M(F) is any
mixing N -step Markov chain, then µ := Φ(ν) is a uniformly mixing measure on S.
We call µ a quasi-Markov measure. ♦

We say that µ is harmonically bounded (HB) if there is some C < 1 such that |⟨χ, µ⟩| < C
for all χ ∈ ̂AZ except χ = 11. The goal of this section is to prove:

Prepared using etds.cls

14 M. Pivato and R. Yassawi

Theorem 5.2. Let A be a ﬁnite abelian group. If µ ∈ M(A
Z) is uniformly mixing and
harmonically bounded, then µ is dispersion mixing. ✷

We will then apply Theorem 5.2 to get:

Corollary 5.3. Let A = Z/p, where p is prime. If µ ∈ M(A
Z) is a mixing quasi-Markov
measure, then µ is asymptotically randomized by any dispersive LCA. ✷

Harmonic boundedness and entropy:

Lemma 5.4. Let A = (Z/p)
s, where p is prime and s ∈ N. If µ ∈ M(A
Z) and
h(µ, σ) > (s − 1) · log2(p), then µ is harmonically bounded.

Proof. Suppose µ was not HB. Then for any α > 0, we can ﬁnd 11 ̸= χ ∈ ̂AZ with
|⟨χ, µ⟩| > 1 − α. Let I := image (χ) ⊂ T
1, and let ν := χ(µ) ∈ M(I) be the projected
measure on I. Thus, ⟨χ, µ⟩ = ∑

i∈I i · ν{i}. The following four claims are easy to check.

Claim 1: For any β > 0, there exists α > 0 such that, for any probability measure

ν ∈ M(I) with
 ∣
∣
∣
∣
∣
∑

i∈I i · ν{i}
∣
∣
∣
∣
∣ > 1 − α, there is some i0 ∈ I with ν{i0} > 1 − β. ✸

Suppose χ = ⊗

k∈K χk, where K ⊂ [0...K] and K ∈ K. Thus, if ξ := ⊗

k∈K\{K} χk,

then χ = ξ ⊗ χK. For any b ∈ A
[0...K), let µ(b)
K be the conditional measure on the Kth

coordinate, and let ν(b)
K := χK (µ(b)
K ) ∈ M(I) be the projected measure on I.

Claim 2: For any γ > 0, there exists β > 0 such that, if ∃ i0 ∈ I with ν{i0} > 1 − β,
then there is a subset B ⊂ A
[0...K) with µ[B] > 1 − γ, such that, for every b ∈ B, there is
some ib ∈ I with ν(b)
K {ib} > 1 − γ. Thus, if Pb = χ−1
K {ib} ⊂ A, then µ(b)
K [Pb] > 1 − γ.

(Observe that # (Pb) ≤ ps−1 for all b ∈ A
[0...K).) ✸

For any measure ρ ∈ M(A), deﬁne H(ρ) := − ∑

a∈A ρ{a} log2 (
ρ{a})
. Recall (e.g.

[Pet89, Proposition 5.2.12]) that the σ-entropy of µ can be computed:

h(µ, σ) = lim
N →∞
 ∑

b∈A[0...N ) µ [b] · H (µ(b)
N ) (13)

Claim 3: For any δ > 0, there exists γ1 > 0 such that, for any probability measure
ρ on A, if there is a subset P ⊂ A with # (P) ≤ ps−1 and ρ[P] > 1 − γ1, then
H(ρ) < (s − 1) · log2(p) + δ. ✸

Claim 4: For any ǫ > 0, and S > 0, there exist δ, γ2 > 0 such that, for any K ∈ N and
probability measure µ on A
[0...K], if there is a subset B ⊂ A
[0...K) with µ[B] > 1 − γ2,

such that, for all b ∈ B, H (
µ(b)
K ) < S − δ, then ∑

b∈A[0...K) µ [b] · H (µ(b)
K ) < S − ǫ. ✸

Now, set S := (s − 1) · log2(p). For any ǫ > 0, ﬁnd δ, γ2 > 0 as in Claim 4. Then
ﬁnd γ1 > 0 as in Claim 3, and let γ := min{γ1, γ2}. Next, ﬁnd β as in Claim 2 and then
ﬁnd α as in Claim 1. Finally, ﬁnd χ ∈ ̂AZ with |⟨χ, µ⟩| > 1 − α. It then follows from

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 15

Claims 1-4 that ∑

b∈A[0...K) µ [b] · H (µ(b)
N ) < (s − 1) · log2(p) − ǫ. But the limit in (13) is a

decreasing limit, so we conclude that h(µ, σ) < (s − 1) · log2(p) − ǫ. Since this is true for
any ǫ > 0, we conclude that h(µ, σ) ≤ (s − 1) · log2(p), contradicting our hypothesis. ✷

Corollary 5.5. If A = Z/p (where p is prime), and h(µ, σ) > 0, then µ is harmonically
bounded. ✷

Say µ is uniformly multiply mixing if, for any ǫ > 0, there is some S > 0 such that,
for any R > 0, if K0, K1, . . . , KR ⊂ M are ﬁnite, mutually S-separated subsets of M, and
U0 ⊂ A
K0 , . . . , UR ⊂ A
KR are cylinder sets, then:

µ
 ( R⋂

r=0 Ur
)
 ˜Rǫ
 R∏

r=0 µ (Ur) . (14)

Lemma 5.6. If µ ∈ M(A
Z) is uniformly mixing, then µ is uniformly multiply mixing.

Proof. (by induction on R). The case R = 1 is just uniform mixing. Suppose (14) is true
for all R′ < R. Find S > 0 so that, if K0, . . . , KR are mutually S-separated, then

µ
 ( R⋂

r=0 Ur
)
 = µ
 (
U0 ∩
 R⋂

r=1 Ur
)
 ̃ǫ µ (U0)·µ
 ( R⋂

r=1 Ur
)
 ̃(R−1)ǫ µ (U0)·
 R∏

r=1 µ (Ur) ,

where “ ̃ǫ ” comes by setting R′ = 1, and “ ̃(R−1)ǫ ” comes by setting R′ = R − 1. ✷

Lemma 5.7. Suppose µ ∈ M(A
Z) is uniformly multiply mixing. For any ǫ > 0 and
R ∈ N, there is some S > 0 such that: if K0, . . . , KR ⊂ Z are S-separated sets,

and, for all r ∈ [0...R], χr : A
Kr −→C are characters, and χ =
 R∏

r=0 χr, then

⟨χ, µ⟩ ˜ǫ/2
 R∏

r=0 ⟨χr, µ⟩. ✷

Proof of Theorem 5.2. Let ǫ > 0. We want to ﬁnd S > 0 and R > 0 such that, if χ is any
character, and rankS (χ) > R, then |⟨χ, µ⟩| < ǫ.

Let C < 1 be the harmonic bound. Find R ∈ N such that CR < ǫ/2. Let S > 0 be as

in Lemma 5.7. Suppose rankS (χ) > R, and let χ :=
 R⊗

r=0 χr, where χr : A
Kr −→C are

characters, and K0, . . . , KR ⊂ Z are S-separated. Then Lemma 5.7 implies:

⟨χ, µ⟩ ˜ǫ/2
 R∏

r=0 ⟨χr, µ⟩. (15)

By harmonic boundedness, we know |⟨χr, µ⟩| < C for all r ∈ [0...R]. Thus, (15) implies:

|⟨χ, µ⟩| ˜ǫ/2
 R∏

r=0 |⟨χr, µ⟩| <
 R∏

r=0 C = CR+1 < CR < ǫ/2. ✷

Prepared using etds.cls

16 M. Pivato and R. Yassawi

Proof of Corollary 5.3. From examples 5.1(a) and 5.1(b), we know µ is uniformly mixing.
Any mixing quasi-Markov measure has nonzero entropy, so Corollary 5.5 says that µ is
harmonically bounded. Theorem 5.2 says µ is dispersion mixing. Theorem 3.1 says µ is
asymptotically randomized by any dispersive CA. ✷

6. Markov Words
If m, n ∈ Z, and m ≤ n, let A
[m...n) be the set of all words of the form a =
[am, am+1, . . . , an−1]. Let A
∗ := ⋃

−∞<m<n<∞ A
[m...n) be the set of all ﬁnite words. Elements

of A
∗ are denoted by boldfaced letters (e.g. a, b, c), and subsets by gothic letters (e.g. A,
B, C). Concatenation of words is indicated by juxtaposition. Thus, if a = [a0 . . . an] and
b = [b0 . . . bm], then ab = [a0 . . . anb0 . . . bm].
If V > 0 and v ∈ A
[−V...V ), we say that v is a Markov word for µ if (in the terminology
of §1), v isolates (−∞... −V ) from [V...∞).

Example 6.1:

⟨a⟩ If µ is an N -step Markov shift, and N ≤ 2V , then every v ∈ A
[−V...V ) is a Markov
word.

⟨b⟩ Let F ⊂ BZ be a subshift of ﬁnite type, let Ψ : F−→A
Z be a block map, so that
S := Ψ(F) is a soﬁc shift. Let ν be a Markov measure on F and let µ := Ψ(ν). If
s ∈ S[−V...V ] is a synchronizing word for Ψ, then s is a Markov word for µ. ♦

Proposition 6.2. If µ ∈ M(A
Z) is mixing and has a Markov word, then µ is uniformly
mixing.

Proof. Fix ǫ > 0. For any words a, b ∈ A
∗, the mixing of µ implies that there is some
Mǫ (a, b) < ∞ such that, for all m > Mǫ(a, b), µ (σm [a] ∩ [b]) ̃ǫ µ [a] · µ [b]. Our goal
is to ﬁnd some M > 0 such that Mǫ(a, b) < M for all a, b ∈ A
∗.

Let v ∈ A
∗ be a Markov word for µ.

Claim 1: Let u, w, u′, w′ ∈ A
∗, and consider the words uvw and u′vw′. We have:
Mǫ (uvw, u′vw′) = Mǫ (vw, u′v).

Proof. Deﬁne transition probabilities: µ(u L99 v) := µ(uv)/µ(v) and µ(v 99K w) :=
µ(vw)/µ(v). If m > Mǫ (vw, u′v), then

µ (σm [uvw] ∩ [u′vw′] ) = µ(u L99 v) · µ (
σm [vw] ∩ [u′v] ) · µ(v 99K w′) (16)

̃ǫ µ(u L99 v) · µ [vw] · µ [u′v] · µ(v 99K w′) (17)

= µ [uvw] · µ [u′vw′] . (18)

(16) and (18) are because v is a Markov word; (17) is because m > Mǫ (vw, u′v).
✸ Claim 1

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 17

If a ∈ A
∗, we say that v occurs in a if a
∣
∣[n−V...n+V ) = v for some n.

Claim 2: There is some N > 0 such that µ{a ∈ A
[0...N ] ; v occurs in a
} > 1 − ǫ.

Proof. By ergodicity, ﬁnd N such that µ
 ( N⋃

n=0 σn [v]
)
 > 1 − ǫ. ✸ Claim 2

Let A
∗
v be the set of words (of length at least N ) in A
∗ with v occuring in the last (N + V )
coordinates, and let vA
∗ be the set of all words in A
∗ with v occuring in the ﬁrst (N + V )
coordinates. Then Claim 2 implies that:

µ(A
∗
v) > 1 − ǫ and µ(vA
∗) > 1 − ǫ. (19)

Let A
<N :=
 N⋃

n=1 A
[0...n]. Then

A
∗
v = {uvw ; u ∈ A
∗ and w ∈ A
<N }
.
and vA
∗ = {u′vw′ ; u′ ∈ A
<N and w′ ∈ A
∗}, (20)

Deﬁne M1 := max
a∈A∗
v max
b∈vA∗ Mǫ(a, b) (∗) max
u∈A
∗

w∈A
<N max
u′∈A
<N
w′∈A
∗ Mǫ (uvw, u′vw′)

(†) max
w,u′∈A<N Mǫ (vw, u′v) .

where (∗) is by equation (20) and (†) is by Claim 1. Likewise, deﬁne

M2 := max
a∈A∗
v max
b∈A<N Mǫ(a, b) = max
w∈A<N max
b∈A<N Mǫ(vw, b),

M3 := max
a∈A<N max
b∈vA∗ Mǫ(a, b) = max
a∈A<N max
u′∈A<N Mǫ(a, u′v),

and M4 := max
a∈A<N max
b∈A<N Mǫ(a, b).

Thus, M1, . . . , M4 each maximizes a ﬁnite collection of ﬁnite values, so each is ﬁnite. Thus,
M := max{M1, . . . , M4} is ﬁnite.

Claim 3: For any a, b ∈ A
∗, Mǫ(a, b) < M .

Proof. If a ∈ A
<N ∪ A
∗
v and b ∈ A
<N ∪ vA
∗, then Mǫ(a, b) < M by deﬁnition.

So, suppose a ̸∈ A
<N ∪ A
∗
v. Then equation (19) implies that µ[a] < ǫ. Hence, for
any m ∈ N, µ(σm[a] ∩ b) < ǫ and µ[a] · µ[b] < ǫ. Thus, µ(σm[a] ∩ b) ̃ǫ µ[a] · µ[b]
automatically. Hence, Mǫ(a, b) = 0 < M .

Likewise, if b ̸∈ A
<N ∪ vA
∗, then Mǫ(a, b) = 0 < M . ✸ Claim 3

Thus, µ is uniformly mixing. ✷

Corollary 6.3. If µ is harmonically bounded, mixing and has a Markov word, then µ is
asymptotically randomized by Φ = 1 + σ.

Proof. Combine Proposition 6.2 with Theorems 3.1 and 5.2. ✷

Prepared using etds.cls

18 M. Pivato and R. Yassawi

7. Lucas Mixing
Throughout this section, let D := 1, so that M = Z. Let A := (Z/p)
s, where p ∈ N is
prime, and s ∈ N. Let Φ := 1 + σ. We will introduce a condition on µ which is weaker than
dispersion mixing, and which is both suﬃcient and necessary for asymptotic randomization.
Let χ ∈ ̂AZ, and suppose χ = ⊗

k∈K χk. We deﬁne |[χ]| := max(K) − min(K), and deﬁne

⟨⟨χ⟩⟩ := pr, where r := ⌈ logp |[χ]|
⌉ .

It follows from Lucas’ Theorem that Φ⟨⟨χ⟩⟩ = 1 + σ⟨⟨χ⟩⟩. Thus, for any h ∈ N,

Φh·⟨⟨χ⟩⟩ = ∑

ℓ∈L(h)
 [ h
ℓ
 ]
p σ⟨⟨χ⟩⟩·ℓ, and thus, χ ◦ Φh·⟨⟨χ⟩⟩ = ⊗

ℓ∈L(h)
 [ h
ℓ
 ]
p χ ◦ σ⟨⟨χ⟩⟩·ℓ.

Observe that K+prℓ and K+prℓ′ are disjoint for any ℓ ̸= ℓ′ ∈ L (h). Hence, if L := # (L (h)),
then χ ◦ Φh·⟨⟨χ⟩⟩ is a product of L ‘disjoint translates’ of χ.
If µ is a measure on A
Z, we say that µ is Lucas mixing if, for any nontrivial character χ ∈
̂AZ, there is a subset H ⊂ N of Ces`aro density one such that lim
H∋h→∞
 〈
χ ◦ Φh·⟨⟨χ⟩⟩, µ〉 = 0.

Our goal in this section is to prove:

Theorem 7.1. (
Φ = 1 + σ asymptotically randomizes µ) ⇐⇒ (µ is Lucas mixing
). ✷

It is relatively easy to see that:

Lemma 7.2. If µ is dispersion-mixing, then µ is Lucas mixing. ✷

Thus, the “⇐=” direction of Theorem 7.1 is an extension of Theorem 3.1, in the case
Φ = 1 + σ. The “=⇒” direction makes this the strongest possible extension for this LCA.

Set S := |[χ]|, and let ̃J := J(S), where J(S) is deﬁned as in §4. It follows from Lemma
4.7 that density (
̃J
) = 1. For any m ∈ N, let χm := χ ◦ Φm.

Lemma 7.3. Let j ∈ ̃J, with j = m + pr · h. Then χ ◦ Φj = χm ◦ Φh′·⟨⟨χm⟩⟩, where
h′ = ps · h for some s ≥ 0.

Proof. Apply Lemma 4.8 to observe that Φj = Φm ◦ Φh·(p
r). Thus,

χ ◦ Φj = χ ◦ Φm ◦ Φh·(p
r) = χm ◦ Φh·(p
r).

By deﬁnition, r is such that m < pr−1 and |[χ]| < pr−1. Thus,

|[χm]| = |[χ]| + m < pr−1 + pr−1 ≤ pr.

Now, let s := r − logp |[χm]|, and let h′ := ps · h. Then h · (pr) = h′ · ⟨⟨χm⟩⟩, so that
Φh·(p
r) = Φh′·⟨⟨χm⟩⟩. ✷

Proof of Theorem 7.1. We will use Lemma 3.2.

‘⇐=’ For any m ∈ N, let r(m) := ⌈logp (max {m, |[χ]| })⌉ + 1, and deﬁne

̃Jm := {m + pr(m)h ; h ∈ N}
. (21)

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 19

It follows that: ̃J = ⋃

m∈N ̃Jm. (22)

If j = m + pr(m)h is an element of ̃Jm, then Lemma 7.3 says χ ◦ Φj = χm ◦ Φh′·⟨⟨χm⟩⟩,
for some h′ ≥ h. Now, µ is Lucas mixing, so ﬁnd a subset ̃Hm ⊂ N of density one with
lim
̃Hm∋h→∞
 〈χm ◦ Φh·⟨⟨χm⟩⟩, µ〉 = 0. Deﬁne:

Hm := {
h ∈ ̃Hm ; ∣
∣
∣〈χm ◦ Φh·⟨⟨χm⟩⟩, µ〉∣
∣
∣ ≤ 1
m
 }
,

Jm := {
m + pr(m)h ; h ∈ Hm}
, (23)

and J := ⋃

m∈N Jm. (24)

Claim 1: density (J) = 1.

Proof. For any m ∈ N, there is some K such that Hm = ̃Hm ∩ [K...∞). Thus,

rel density [Hm/ ̃Hm] = 1. Thus, density (Hm) = density ( ̃Hm) = 1. Compare (21)

and (23) to see that rel density [Jm/̃Jm] = 1. Then compare (22) and (24) to see that

rel density [J/̃J
] = 1. Thus, density (J) = density (
̃J
) = 1. ✸ Claim 1

Claim 2: lim
J∋j→∞ 〈
χ ◦ Φj, µ〉 = 0.

Proof. Fix ǫ > 0. Let M be large enough that 1
M < ǫ. For all m ∈ N with m < M ,
ﬁnd Hm such that, if h ∈ ̃Hm and h > Hm, then ∣
∣〈
χm ◦ Φh·⟨⟨χm⟩⟩, µ〉∣
∣ < ǫ. Let
Jm := m + 2r(m) · Hm. Thus, if j = m + 2r(m) · h is an element of Jm, and j > Jm,
then we must have h > Hm, so that ∣
∣〈
χ ◦ Φj, µ〉∣
∣ = ∣
∣〈
χm ◦ Φh·⟨⟨χm⟩⟩, µ〉∣
∣ < ǫ.

Now let J := max
1≤m≤M Jm. Thus, for all j ∈ J, if j > J, then either j ∈ Jm for

some m ≤ M , in which case ∣
∣〈
χ ◦ Φj, µ〉∣
∣ < ǫ by construction of J, or j ∈ Jm for some
m > M , in which case
 ∣
∣
〈
χ ◦ Φj, µ〉∣
∣ <

(∗) 1
m < 1
M <

(†) ǫ.

Here, (∗) follows by deﬁnition of Hm, and (†) follows by deﬁnition of M . ✸ Claim 2

Lemma 3.2 and Claims 1 and 2 imply that Φ asymptotically randomizes µ.

‘=⇒’ Suppose µ was not weakly harmonically mixing. Thus, there is some χ ∈ ̂AZ

and some subset H ⊂ N of density δ > 0 such that lim sup
H∋h→∞
 ∣
∣
∣〈
χ ◦ Φh·⟨⟨χ⟩⟩, µ〉∣
∣
∣ > 0.

But χ ◦ Φh·⟨⟨χ⟩⟩ = χ ◦ Φp
r ·h (where r = ⌈ logp |[χ]|⌉). Hence, if J := pr · H, then

density (J) = p−r · δ > 0, and lim sup
J∋j→∞
 ∣
∣〈
χ ◦ Φj, µ〉∣
∣ = lim sup
H∋h→∞
 ∣
∣
∣
〈χ ◦ Φh·⟨⟨χ⟩⟩, µ〉∣
∣
∣ > 0.

But then Lemma 3.2 implies that Φ cannot randomize µ. ✷

Prepared using etds.cls

20 M. Pivato and R. Yassawi

8. Randomization of Zero-Entropy Measures
Of the probability measures which are asymptotically randomized by LCA, every known
example has positive entropy. However, we’ll show that positive entropy is not necessary,
by constructing a class of zero-entropy measures which are Lucas mixing, and thus (by
Theorem 7.1) randomized by Φ = 1 + σ.
For both eﬃciency and lucidity, we will employ probabilistic language. Let (Ω, B, ρ) be
an abstract probability space (called the sample space). If (X, X ) is any measurable space,
then an (X-valued) random variable is a measurable function f : Ω−→X. In particular, a
random sequence is a measurable function a : Ω−→A
Z. By convention, we suppress the
argument of random variables. Thus, if a, b, c are random sequences, then the equation
“a + b = c” means “a(ω) + b(ω) = c(ω), for ρ-almost all ω ∈ Ω.”
If f : Ω−→X is a random variable, and U ⊂ X, then “Prob [f ∈ U]” denotes ρ [f −1(U)
].
If g : Ω−→Y is another random variable, then f and g are independent if, for any measurable
U ⊂ X and V ⊂ Y, Prob [f ∈ U and g ∈ V] = Prob [f ∈ U] · Prob [g ∈ V] —i.e.
ρ [
f −1(U) ∩ g−1(V)
] = ρ [
f −1(U)
] · ρ [
g−1(V)
]. The distribution of f is the probability
measure µ := f (ρ) on (X, X ); we then say that f is a µ-random variable. Thus, every random
variable determines a probability measure on its range. However, given a measure µ, we can
construct inﬁnitely many independent µ-random variables.

Let A := Z/2 and µ ∈ M(A
Z), and consider a µ-random sequence a ∈ A
Z. We say µ
has independent random dyadic increments (IRDI) if, for any n ∈ N, and all m ∈ [1...2n],
am+2n = am + d
n
m, where d
n
1 , . . . , d
n
2n are independent A-valued random variables. If
d
n
1 , . . . , d
n
2n have distributions δn
1 , . . . , δn
2n , then µ has lower decay rate α ∈ (0, 1) if there
is some L > 0 such that, for all n ≥ L, and all m ∈ [1...2n], α
n ≤ δn
m{1}.

Proposition 8.1. If µ has IRDI with lower decay rate α > 1√2 , then µ is Lucas Mixing.

Proof. Let χ ∈ ̂AZ be a nontrivial character. We seek H ⊂ N with density (H) = 1, such
that lim
H∋h→∞
 〈χ ◦ Φh·⟨⟨χ⟩⟩, µ〉 = 0.

If n ∈ N, let I = I(n) := ⌈log2(n)⌉, and suppose n has binary expansion {n(i)}I
i=0. Let
I(n) := {
j ∈ [0...I] ; n(j) = 1}
. Let ǫ > 0 be small, and deﬁne:

H := {h ∈ N ; # (I(h)) ≥ 1
2 I(h) − ǫ}
.

Then density (H) = 1. Suppose n ∈ H is large; let I := I(n) and I := I(n). Assume I is
large (in particular, I > L).

Now, α > 1√2 , so ﬁnd β such that 1
α < β < √2. Deﬁne

M := # (I) − 1 ≥ 1
2 I − ǫ − 1 >

(∗) log2(β)I, (25)

where (∗) is because log2(β) < 1
2 and I is large, while ǫ is small.

Suppose I = {i1 < i2 < . . . < iM+1 = I}. Let ξ0 := χ, and for each m ∈ [0...M ], deﬁne
ξm+1 := ξm ⊗ (
ξm ◦ σLi )
, where Li := 2im · ⟨⟨χ⟩⟩. Thus, χ ◦ Φn·⟨⟨χ⟩⟩ = ξM+1.

Let r := rank [χ]. Then for all m ∈ [1...M + 1], rank [ξm] = 2m · r. In particular,
deﬁne R := rank [ξM ] = 2M · r >

(∗) βI · r. (26)

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 21

where (∗) is by equation (25). Thus, ξM = ⊗

x∈X ξx, where X ⊂ Z is a subset with

# (X) = R. Thus, if a ∈ A
Z is a µ-random sequence, then

ξM+1(a) = ξM (a) · (
ξM ◦ σ2
I (a)
) = ∏

x∈X ξx(ax) · ξx (ax+2I )

= ∏

x∈X ξx (ax + ax+2I ) = ∏

x∈X ξx (
d
I
x) , (27)

where {d
I
x}x∈X are independent random dyadic increments. If d
I
x has distribution δI
x, then

EδI
x [ξx (
d
I
x)] = δI
x{0}−δI
x{1} = 1−2δI
x{1} ≤

(∗) 1−2·α
I = 2α
−I − 1
2α−I . (28)

Here, (∗) is because µ has lower decay rate α, so δI
x{1} ≥ α
I (assuming I ≥ L).

Thus, ⟨µ, χ ◦ Φn⟩ (‡) Eµ
 [ ∏

x∈X ξx (
d
I
x)
]
 (∗) ∏

x∈X EδI
x [ξx (
d
I
x)] ≤

(†)
 ( 2α
−I − 1
2α−I
 )R .

Here, (‡) is by equation (27), (∗) is because {d
I
x}x∈X are independent, and (†) is by
equation (28) and because # (X) = R.

Thus, log ∣
∣
∣⟨µ, χ ◦ Φn⟩
∣
∣
∣ ≤ R · [ log (2α
−I − 1) − log(2α
−I )
] ≤

(∗) − R · log′ (
2α
−I )

= −R
2α−I <

(†) −βI r
2α−I = − r
2 (αβ)
I .

Here, (∗) is because log is a decreasing function, and (†) is by equation (26).

But β > 1
α , so αβ > 1. Thus, lim
H∋h→∞ log ∣
∣
∣〈µ, χ ◦ Φh·⟨⟨χ⟩⟩〉∣
∣
∣ = − r
2 lim
I→∞ (αβ)
I = −∞.

Hence lim
H∋h→∞
 ∣
∣
∣〈
µ, χ ◦ Φh·⟨⟨χ⟩⟩〉∣
∣
∣ = 0. ✷

Suppose µ ∈ M(A
Z) has independent random dyadic increments; for any n ∈ N, and all
m ∈ [1...2n], let δn
1 , . . . , δn
2n be the dyadic increment distributions, as before. Then µ has
upper decay rate α ∈ (0, 1) if there are constants L1, K > 0 such that, for all n ≥ L1, and
all m ∈ [1...2n], δn
m{1} ≤ K · α
n.

Proposition 8.2. If µ has IRDI with upper decay rate α < 1, then h(µ) = 0.

Proof. Let L1, K > 0 be as above. Assume without loss of generality that K > 4. Let

L2 := − log2(K) − 1
log2(α) . Let L := max{L1, L2}.

For any n ∈ N, and m ∈ [1...2n], let δn
m be as above. The entropy of δn
m is deﬁned:

H(δn
m) := −δn
m{0} log2(δn
m{0}) − δn
m{1} log2(δn
m{1}) (29)

Claim 1: There exists c1 > 0 such that, if n > L and m ∈ [1...2n], then
H(δn
m) < c1n · α
n.

Prepared using etds.cls

22 M. Pivato and R. Yassawi

Proof. α < 1, so log2(α) < 0; Thus, if n ≥ L2, then n log2(α) ≤ L2 log2(α). Thus,

log2(Kα
n) = log2(K) + n log2(α) ≤ log2(K) + L2 log2(α)

= log2(K) − log2(K) − 1 = −1. (30)

Thus, δn
m{1} ≤

(∗) Kα
n ≤

(†)
 1
2 , where (∗) is because n ≥ L1 and (†) is by equation (30).

But, if δn
m{1} < 1
2 in equation (29), then H(δn
m) decreases as δn
m{1} decreases. Hence,

H(δn
m) ≤ −Kα
n log2 (Kα
n) − (1 − Kα
n) log2 (1 − Kα
n)

< Kα
n (nA − k)
︸ ︷︷ ︸
(∗)
 + (1 − Kα
n) · 2Kα
n
︸ ︷︷ ︸
(†) = K (nA + 2 − k − 2Kα
n) · α
n

<

(‡) KnA · α
n <

(⋄) c1n · α
n.

Here, (∗) is the substitution k := log2(K) and A := − log2(α); (†) is because, if ǫ is
small, then log(1 − ǫ) ≈ −ǫ, thus, − log(1 − ǫ) < 2ǫ; (‡) is because 2 − k − 2Kα
n < 0
because k > 2 because we assume K > 4; (⋄) is where c1 := KA > 0. ✸ Claim 1

Let a ∈ A
Z be a µ-random sequence, and ﬁx n > L. To compute the conditional entropy
H (
a
∣
∣(2n...2n+1] |a
∣
∣[1...2n]
 )
, recall that, for all m ∈ [1...2n], a2n+m = am + d
n
m. Thus,

H (a
∣
∣(2n...2n+1]
 ∣
∣
∣ a
∣
∣[1...2n]
 ) = H (d
n
1 , d
n
2 , . . . , d
n
2n ) (∗)
 2
n
∑

m=1 H(δn
m)

<

(†) 2n · c1nα
n = c1n · (2α)
n. (31)

where (∗) is because d
n
1 , d
n
2 , . . . , d
n
2n are independent random variables with distributions
δn
1 , . . . , δn
2n , and (†) is by Claim 1. Thus, for any N > L,

H (a
∣
∣[1...2N ]
 ∣
∣
∣ a
∣
∣[1...2L]
 ) =
 N −1∑

n=L H (
a
∣
∣(2n...2n+1]
 ∣
∣
∣ a
∣
∣[1...2n]
 ) <

(∗)
 N −1∑

n=L c1n · (2α)
n

< c1N · (2α)
L N −L−1∑

n=0 (2α)
n = c1N · (2α)
L (2α)
N −L − 1
2α − 1

≤ c2N · (2α)
N , (32)

where (∗) is by equation (31), and where c2 ≈ c1
2α − 1 > 0 is another constant.

Thus, if H0 := H (a
∣
∣[1...2L]
 )
, then

H (a
∣
∣[1...2N ]
 ) = H (a
∣
∣[1...2N ]
 ∣
∣
∣ a
∣
∣[1...2L]
 ) + H0 ≤

(∗) c2N · (2α)
N + H0, (33)

where (∗) is by equation (32). Thus,

h(µ) = lim
M→∞ 1
M H (a
∣
∣[1...M]
 ) = lim
N →∞ 1
2N H (a
∣
∣[1...2N ]
 )

≤

(∗) lim
N →∞ c2N · (2α)
N + H0
2N ≤ c2 lim
N →∞ N α
N
 (†) 0,

where (∗) is by equation (33), and (†) is because |α| < 1. ✷

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 23

r4
0 r4
1 r4
2 r4
3 . . .

r3
0 r3
1 r3
2 r3
3 r3
4 r3
5 r3
6 r3
7

r2
0 r2
1 r2
2 r2
3 r2
0 r2
1 r2
2 r2
3

r1
0 r1
1 r1
0 r1
1 r1
0 r1
1 r1
0 r1
1 r1
0 r1
1 . . .

r0
0 r0
0 r0
0 r0
0 r0
0 r0
0 r0
0 r0
0 r0
0 r0
0 . . .
. . . a∞
0 a∞
1 a∞
2 a∞
3 a∞
4 a∞
5 a∞
6 a∞
7 a∞
8 a∞
9 a∞
10 a∞
11 a∞
12 a∞
13 a∞
14 a∞
15 a∞
16 a∞
17 a∞
18 a∞
19 . . .
. . . a0 a1 a2 a3 a4 a5 a6 a7 . . .

Figure 3. The construction of random sequence a∞; the approximation of a as a random translate of a∞.

It remains to actually construct a measure with IRDI. Let 0 < α < 1. For any n ∈ N, let
ρn be the probability distribution on A = Z/2 such that

ρn{1} = α
n and ρn{0} = 1 − α
n. (34)

For each n ∈ N, we will construct a random sequence a
n ∈ A
Z as follows. First, deﬁne
a
0 := [. . . 0000 . . .]. Now, suppose, inductively, that we have a
n. Let rn
0 , rn
1 , . . . , rn
2n−1 be
a set of 2n independent A-valued, ρn-random variables. Let r
n ∈ A
Z be the random,
2n+1-periodic sequence

r
n := [. . . ,

zeroth coordinate
↓
0, 0, . . . , 0
︸ ︷︷ ︸
2n , rn
0 , rn
1 , . . . , rn
2n−1, 0, 0, . . . , 0
︸ ︷︷ ︸
2n , rn
0 , rn
1 , . . . , rn
2n−1, . . .],

and inductively deﬁne a
n+1 := a
n + r
n.

Let µn ∈ M(A
Z) be the distribution of a
n, and let ̃µn := 1
2n
 2
n
∑

i=1 σi(µn) be the stationary

average of µn. Finally, let µ := wk∗−lim
n→∞ ̃µn.

Let µ∞ be the probability distribution of the random sequence a
∞ :=
 ∞∑

n=1 r
n (see Fig.3).

Then µ∞ = wk∗− lim
n→∞ µn, and loosely speaking, µ is the ‘σ-ergodic average’ of µ∞. Thus,
if a is a µ-random sequence, we can think of a as obtained by shifting a
∞ by a random
amount. The next lemma describes the structure of a
∞:

Lemma 8.3. Let M ∈ N have binary expansion M =
 ∞∑

n=0 mn2n. For all n ≥ 0, let

Mn :=
 n−1∑

i=0 mi2i. Then a∞
M =
 ∞∑

n=0 mn · rn
Mn . ✷

For example, suppose M := 13 = 1 + 4 + 8; then m0 = m2 = m3 = 1 and m1 = 0. Hence,
M0 = 0, M1 = M2 = 1, and M3 = 5. Thus, a∞
13 = r0
0 + r2
1 + r3
5 (see Figure 3).
Think of a
∞ as being generated by a process of ‘duplication with error’. Let w0 := [0]
be a word of length 1. Suppose, inductively, that we have wn = [w1w2 . . . w2n−1].
Let ̃wn := [ ̃w1 ̃w2 . . . ̃w2n−1] be an ‘imperfect copy’ of wn: for each m ∈ [0...2n),
̃wm := wm + rn
m, where rn
0 , rn
1 . . . , rn
2n−1 are the independent ρn-distributed variables from

Prepared using etds.cls

24 M. Pivato and R. Yassawi

before, which act as ‘copying errors’. Let wn+1 := wn ̃wn. Then a
∞ is the limit of wn as
n→∞.

Proposition 8.4. µ has IRDI, with upper and lower decay rate α.

Proof. Let a ∈ A
Z be a µ-random sequence, and ﬁx N ∈ N. By construction, there is some
k ∈ Z such that a looks like σk(a
∞) in a neighbourhood around 0. To be precise,

For all m ∈ [0...2N +1)
, am = a∞
k+m. (35)

For example, in Figure 3, let N = 2, so that 2N = 4; suppose k = 6. Thus,
[a0, a1, . . . , a7] = [a∞
6 , a∞
7 , . . . , a∞
13]. Thus, d
2
0 = a4 − a0 = a∞
10 − a∞
6 = r3
2 − r2
2 = r3
2 + r2
2.
More generally:

Claim 1: Let m ∈ [0...2N )
.

(a) There is a set S(m) := {(n0, m0), (n1, m1), . . . , (nJ , mJ )} (for some J ≥ 0), where
N = n0 ≤ n1 ≤ · · · ≤ nJ , and where mj ∈ [0...2nj ) for ∀ j ∈ [0...J], such that
d
N
m = rn0
m0 + rn1
m1 + . . . + rnJ
mJ .
(b) If m′ ∈ [
0...2N )
, and m′ ̸= m, then S(m′) ∩ S(m) = ∅.

Proof. Let M := k + m and let ̃M := k + m + 2N . If M =
 ∞∑

n=0 mn2n and ̃M =
 ∞∑

n=0 ̃mn2n,

then Lemma 8.3 says that

a∞
M =
 ∞∑

n=0 mn · rn
Mn ; and a∞
̃M =
 ∞∑

n=0 ̃mn · rn
̃Mn . (36)

Let N1 ≥ N be the smallest element of [N...∞) such that mN1 = 0. Hence, mn = 1 for
all n ∈ [N...N1), and mN1 = 0. Note that ̃M = M + 2N , so binary expansions of M and
̃M are related as follows:

(A) mn = ̃mn for all n ∈ [0...N ).

(B) Thus, ̃Mn = Mn for all n ∈ [0...N ].

(C) If mN = 0 then ̃mN = 1. If mN = 1 then ̃mN = 0.

(D) ̃mn = 0 for all n ∈ [N...N1) (possibly an empty set), and ̃mN1 = 1.

(E) mn = ̃mn for all n > N1.

Thus,

d
N
m = am+2N − am (∗) a∞
k+m+2N − a∞
k+m = a∞
̃M + a∞
M (mod 2)

(†)
 ∞∑

n=0
 ( ̃mn · rn
̃Mn + mn · rn
Mn )
 (ab)
 ∞∑

n=N
 ( ̃mn · rn
̃Mn + mn · rn
Mn )

= rN
MN︸︷︷︸
(bc)
 +
 N1−1∑

n=N +1 mn rn
Mn︸︷︷︸
(d)
 + rN1
̃MN1︸ ︷︷ ︸
(d)
 +
 ∞∑

n=N1+1 mn︸︷︷︸
(e)
 · (rn
̃Mn + rn
Mn ) (37)

Here, (∗) is by equation (35); (†) is by equation (36); (ab) is by (A) and (B); (bc)
is by (B) and (C); (d) is by (D), and (e) is by (E).

Prepared using etds.cls

Randomization of Soﬁc Shifts by Linear Cellular Automata 25

Now, to see (a), let

S(m) := {
(n, m) ; rn
m appears with nonzero coeﬃcient in expression (37)}
.

In particular, rN
MN appears in (37), so (n0, m0) := (N, MN ); thus, n0 = N .
To see (b), suppose m < m′; hence m′ = m + i for some i ∈ [
1...2N )
.

Let M ′ := M + i and ̃M ′ := ̃M + i. Suppose M ′ =
 ∞∑

n=0 m′
n2n and ̃M ′ =
 ∞∑

n=0 ̃m′
n2n.

Deﬁne M ′
n, ̃M ′
n, and N ′
1 analogously. Then, an argument identical to equation (37)
yields:

d
N
m′ = rN
M ′
N +
 N ′
1−1∑

n=N +1 m′
nrn
M ′
n + rN ′
1
̃M ′
N ′
1 +
 ∞∑

n=N ′
1+1 m′
n · (rn
̃M ′
n + rn
M ′
n
 ) (38)

Now, for all n ∈ [N...∞), M ′
n = Mn + i and ̃M ′
n = ̃Mn + i (because i < 2N ); thus,
rn
M ′
n = rn
Mn+i ̸∈ {rn
Mn , rn
̃Mn } and rn
̃M ′
n = rn
̃Mn+i ̸∈ {rn
Mn , rn
̃Mn }. Thus, every summand of

equation (38) is distinct from every summand of equation (37), so S(m′) ∩ S(m) = ∅.
✸ Claim 1

To see that the random variables d
N
0 , . . . , d
N
2N −1 are jointly independent, use Claim 1(a):

d
N
0 = ∑

(n,m)∈S(0) rn
m, d
N
1 = ∑

(n,m)∈S(1) rn
m, . . . . . . d
N
2N −1 = ∑

(n,m)∈S(2N −1) rn
m

The random variables {
rn
m ; n ∈ N, m ∈ [1...2N ]} are independent, and Claim 1(b) says
S(0), S(1) . . . , S(2N − 1) are pairwise disjoint; thus d
N
0 , . . . , d
N
2N −1 are jointly independent.

Lower Decay Rate: |α| < 1, so if N is suﬃciently large (e.g. N > L := −1/ log2(α)),
then α
N < 1
2 . Suppose d
N
m = rn0
m0 + rn1
m1 + . . . + rnJ
mJ , as in Claim 1(a). For all j ∈ [0...J],

let Pj := Prob
 ( J∑

i=j rni
mi = 1
)

. Thus,

δN
m{1} = P0 (†) ρN {0} · P1 + ρN {1} · (1 − P1) = (1 − α
N ) · P1 + α
N · (1 − P1)

= α
N + (1 − 2α
N ) · P1 ≥

(∗) α
N

(†) is because Claim 1(a) says n0 = N . (∗) is because 1 − 2α
N > 0, because α
N < 1
2 .

Upper Decay Rate: Let K := 1
1−α . We claim that, for any N and m, δN
m{1} ≤
Kα
N .

As before, let Pj := Prob (∑J
i=j rni
mi = 1)
. For any j ∈ [1...J), we have

Pj = (1 − α
nj )·Pj+1 + α
nj ·(1 − Pj+1) = Pj+1 + (1 − 2Pj+1)α
nj ≤ Pj+1 + α
nj ,
(39)
and PJ = α
nJ . Hence,

δN
m{1} = P0 ≤

(∗) α
n0 + α
n1 + . . . + α
nJ ≤
 ∞∑

i=n0 α
i = α
n0

1 − α = Kα
n0 (†) Kα
N .

Here, (∗) is obtained by applying equation (39) inductively, and (†) is because n0 = N .
✷

Prepared using etds.cls

26 M. Pivato and R. Yassawi

Thus, if 1√2 < α < 1, then µ satisﬁes the conditions of Propositions 8.1 and 8.2, so µ is
a zero-entropy, Lucas mixing measure. Hence, 1 + σ asymptotically randomizes µ.

References

[Br´e99] P. Br´emaud. Markov Chains: Gibbs ﬁelds, Monte Carlo Simulation, and Queues. Springer,
1999.
[FMMN00] Pablo A. Ferrari, Alejandro Maass, Servet Mart´ınez, and Peter Ney. Ces`aro mean
distribution of group automata starting from measures with summable decay. Ergodic Theory
Dynam. Systems, 20(6):1657–1670, 2000.
[Kit98] Bruce Kitchens. Symbolic dynamics: one-sided, two-sided, and countable state Markov shifts.
Springer, New York, 1998.
[KS80] Ross Kindermann and J. Laurie Snell. Markov Random Fields and their Applications.
American Mathematical Society, Providence, Rhode Island, 1980.
[Lin84] Doug Lind. Applications of ergodic theory and soﬁc systems to cellular automata. Physica
D, 10:36–44, 1984.
[LM95] Doug Lind and Brian Marcus. An Introduction to Symbolic Dynamics and Coding.
Cambridge UP, New York, 1995.
[MHM03] Alejandro Maass, Bernard Host, and Servet Mart´inez. Uniform Bernoulli measure in dynamics
of permutative cellular automata with algebraic local rules. Discrete & Continuous Dyn. Sys.,
9(6):1423–1446, November 2003.
[MM98] Alejandro Maass and Servet Mart´inez. On Ces`aro limit distribution of a class of permutative
cellular automata. Journal of Statistical Physics, 90(1-2):435–452, 1998.
[MM99] Alejandro Maass and Servet Mart´inez. Time averages for some classes of expansive one-
dimensional cellular automata. In Eric Goles and Servet Martinez, editors, Cellular Automata
& Complex Systems, pages 37–54. Kluwer Academic Publishers, Dordrecht, 1999.
[MMPY06] Alejandro Maass, Servet Mart´inez, Marcus Pivato, and Reem Yassawi. Asymptotic
randomization of subgroup shifts by linear cellular automata. to appear in Ergodic Theory
& Dynamical Systems, 26, 2006.
[Pet89] Karl Petersen. Ergodic Theory. Cambridge University Press, New York, 1989.
[PY02] Marcus Pivato and Reem Yassawi. Limit measures for aﬃne cellular automata. Ergodic
Theory Dynam. Systems, 22(4):1269–1287, 2002.
[PY04] Marcus Pivato and Reem Yassawi. Limit measures for aﬃne cellular automata. II. Ergodic
Theory Dynam. Systems, 24(6):1961–1980, 2004.

Prepared using etds.cls
