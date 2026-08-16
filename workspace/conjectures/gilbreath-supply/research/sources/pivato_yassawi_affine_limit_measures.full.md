<!-- source: https://arxiv.org/pdf/math/0108082 | converted from PDF -->

arXiv:math/0108082v2  [math.DS]  31 Aug 2002
Ergod. Th. & Dynam. Sys. (2002), 22, 1269–1287
Printed in the United Kingdom c⃝ 2002 Cambridge University Press

Limit Measures for Aﬃne Cellular Automata

Marcus Pivato† and Reem Yassawi‡†

† Department of Mathematics, University of Houston,
Houston, TX 77204-3476 USA
(e-mail: pivato@math.uh.edu or mpivato@trentu.ca)
‡ Department of Mathematics, Trent University, Lady Eaton College,
Peterborough, Ontario, K9L 1Z6 Canada
(e-mail: ryassawi@trentu.ca)

(Received 8 August 2000 and accepted in revised form 17 September 2001;
ArXiv version submitted 31 August 2002)

Abstract. Let M be a monoid (e.g. N, Z, or Z
D), and A an abelian group. A
M is then a
compact abelian group; a linear cellular automaton (LCA) is a continuous endomorphism
F : A
M −→ A
M that commutes with all shift maps.
Let µ be a (possibly nonstationary) probability measure on A
M; we develop suﬃcient
conditions on µ and F so that the sequence {FN µ}∞
N =1 weak*-converges to the Haar measure
on A
M, in density (and thus, in Ces`aro average as well). As an application, we show: if
A = Z/p (p prime), F is any “nontrivial” LCA on A(ZD), and µ belongs to a broad class
of measures (including most Bernoulli measures (for D ≥ 1) and “fully supported” N -step
Markov measures (when D = 1), then FN µ weak*-converges to Haar measure in density.

1. Introduction
Let A be a ﬁnite set, and let M be a monoid (e.g. M = Z
D, NE, or Z
D × NE). Let A
M be
the conﬁguration space of M-indexed sequences in A. Treat A as a discrete space; then
A
M is compact and totally disconnected in the Tychonoﬀ product topology. The action of
M on itself by translation induces a natural shift action of M on conﬁguration space: for
all e ∈ M, and a ∈ A
M, deﬁne σe[a] = [
bm|m∈M] where, ∀m, bm = ae.m, where “.” is the
monoid operator (“+” for M = Z
D × NE, etc.).
A cellular automaton (CA) is a continuous self-map F : A
M −→ A
M which commutes
with all shifts: for any e ∈ M, F ◦ σe = σe ◦ F. Hedlund [2] proved that any such map
is determined by a local function f : A
U −→ A, where U ⊂ M is some ﬁnite set (thought
of as a “neighbourhood around the identity” in M), so that, for any a = [
am|m∈M] ∈ A
M,
with F(a) = [
bm|m∈M] ∈ A
M, we have:

∀m ∈ M, bm = f (
a|(m.U)) .

† This research partially supported by NSERC Canada.

Prepared using etds.cls [Version: 1999/07/21 v1.0]

1270 M. Pivato, R. Yassawi

If A is a ﬁnite abelian group with operator “+”, then A
M is a compact abelian group under
componentwise addition. A linear cellular automaton (LCA) is a CA which is also a
group endomorphism from A
M to itself. This is equivalent to requiring f to be a group
homomorphism from A
U into A. An aﬃne cellular automaton (ACA) is one having a local
map of the form f = h + b, where h : A
U −→ A is a homomorphism, and b ∈ A is some
constant.
The term “linear” comes from the special case when A = Z/p, for some prime p. Since
Z/p is also a ﬁnite ﬁeld, this map is actually a linear map from the (Z/p)-vector space (Z/p)
U

into Z/p; it generally takes the form:

f [a] = ∑

u∈U fuau (1)

where a = [
au|u∈U] is an element of A
U, and where {fu ; u ∈ U} is a set of coeﬃcients in
Z/p.
The Haar measure on A
M is the measure H
aar assigning mass A
−N to any cylinder
set on N coordinates, where A = Card [A]. H
aar is F-invariant for any LCA F, raising the
question: for what measures µ do the iterates FN µ := µ ◦ F−N converge to H
aar in the
weak* topology, as N → ∞?
This was ﬁrst investigated by D. Lind [5], who studied the LCA on (
Z/2)Z with local
map f(a) = a(−1) + a1. Using methods from harmonic analysis, Lind showed that, if µ is

any nontrivial Bernoulli probability measure on (
Z/2)Z, then

lim
N →∞ 1
N
 N∑

n=1 FN µ = H
aar .

Lind also showed that the sequence of measures {FN µ ; N ∈ N} does not itself converge to
Haar measure; for all j ∈ {2n ; n ∈ N} the measure Fjµ is quite far from Haar.
Ferrari et al. [9, 10] studied LCA with local maps f(a) = k0a0 + k1a1 acting on A
N,
where A = Z/q, q = pn for some prime p, and k0 and k1 are relatively prime to p, and
showed Ces`aro convergence to Haar measure in the weak* topology for a broad class of
measures satisfying a certain “correlation decay” property, including most Bernoulli and
Markov measures. These results are summarized in [1], where the authors also prove that
most Markov measures on A
Z will Ces`aro -converge to Haar, when A = (Z/2) ⊕ (Z/2), and
f : A
2 −→ A is deﬁned f [(x1, y1), (x2, y2)] = (y1, x1 + y2).
These results raise four questions:
1. Is there some broader class of measures whose F-iterates converge to Haar measure in
Ces`aro mean?
2. Rather than Ces`aro convergence, can we obtain convergence in density? (If µ is
stationary, then Ces`aro -convergence to H
aar is equivalent to convergence in density.
However, when µ is nonstationary, convergence in density is a stronger result.)
3. For what other linear CA can we prove convergence to Haar? What about aﬃne CA?
4. Can these results be generalized to LCA on higher dimensional lattices (e.g. M = Z
D,
ND) or nonabelian monoids such as free groups?
We address these questions by developing a suﬃcient condition for the sequence of
measures {FN µ|N ∈N} to converge, in density, to Haar measure, where F : A
M −→ A
M

is an LCA, and M is a ﬁnitely generated monoid. We require the measure µ to have a kind

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata 1271

of mixing property, called harmonic mixing —we demonstrate that, for example, Bernoulli
measures (on A
M, where M is any monoid) and N -step Markov measures (when M is Z or
N) have this property. We also require the automata F to have a kind of “expansiveness”
property, called diﬀusion, which we show is true for all “nontrivial” LCA when A = Z/p.

This paper is organized as follows: in §2, we develop background on harmonic analysis
over A
M (§2.1) and linear cellular automata (§2.2). In §3 we discuss harmonic mixing and
exhibit some examples of it. In §4 we discuss diﬀusion and its consequences. In §5, we show
that, for any prime p and D ≥ 1, if A = Z/p, then all “nontrivial” linear cellular automata

on A(ZD) are diﬀusive; hence, such automata take harmonically mixing measures on A(ZD)

into Haar measure.

Notation: Elements of A will be written as a, b, c, . . . . We often identify the elements of
A with the set [0..p) := {0, 1, . . . , p − 1}. Sans-serif letters (e.g. m, n, u, . . . ) are elements
of M. Boldface letters (e.g. a, b, . . . ) are elements of A
M, and a = [am|m∈M]. Capitalized
Gothic letters (eg. F, G) denote cellular automata. The corresponding lower-case Gothic
letters (eg. f, g) denote the corresponding local maps.

2. Preliminaries
2.1. Harmonic Analysis on A
M Let T
1 be the unit circle group. A character of A is a
group homomorphism φ : A −→ T
1. Let ̂A be the group of all characters of A.
If A = Z/n, then ̂A is canonically isomorphic with A. First deﬁne γ ∈ ̂A by

γ(a) = exp ( 2πi
n a) .

(where we identify A with [0..n) in the obvious way). Then, for each k ∈ A and a ∈ A, deﬁne
γk ∈ ̂A by: γk(a) := γ(k · a) = exp ( 2πi
n k · a)
, where “k · a” refers to multiplication,
mod n. Then ̂A = {γk ; k ∈ A
}, and the map A ∋ k ↦→ γ k ∈ ̂A is an isomorphism.

Let ̂AM be the group of characters of A
M. If A is any abelian group, then ̂AM is in
bijective correspondence with the set
{
[χm|m∈M] ∈ ( ̂A
)M ; χm = 11 for all but ﬁnitely many m ∈ M
} .

If [χm|m∈M] is such a sequence, then deﬁne

χ = ⊗

m∈M χm ∈ ̂AM.

That is: if a = [am|m∈M] is an element of A
M, then χ(a) = ∏

m∈M χm(am), (where all but

ﬁnitely many terms in this product are equal to 1.) The sequence [χm|m∈M] is called the
coeﬃcient system of χ. The rank of the character χ is the number of nontrivial entries
in [
χm|m∈M].

For example, if A = Z/n, then ̂AM is naturally isomorphic to the group
{ [χm|m∈M] ∈ A
M ; χm = 0 for all but ﬁnitely many m ∈ M} .

Prepared using etds.cls

1272 M. Pivato, R. Yassawi

If [
χm|m∈M] is such a sequence, then let χ = ⊗

m∈M γχm : A
M −→ T
1. Thus, if a = [
am|m∈M]

is an element of A
M, then χ(a) = ∏

m∈M exp ( 2πi
p χm · am
)
.

Let M [
A
M] be the space of (possibly nonstationary) probability measures on A
M. If
µ ∈ M [A
M], then the Fourier coeﬃcients of µ are deﬁned:

̂µ[χ] = ⟨µ, χ⟩ = ∫
AM χ dµ,

for all χ ∈ ̂AM. These coeﬃcients completely identify µ. We will use the following basic
result from harmonic analysis:

Theorem 1. If µ1, µ2, µ3, . . . , µ∞ ∈ M [
A
M], then
( ̂µn[χ] −−−−
n→∞−→ ̂µ∞[χ] for all χ ∈ ̂AM ) ⇐⇒ ( µn −−−−n→∞−→ µ∞ in the weak*-topology ) .

2.2. Linear Cellular Automata If A = Z/n, and f : A
U −→ A is a homomorphism,
then there is a unique collection of constant coeﬃcients [fu|u∈U] ∈ A
U so that, for any
a = [au|u∈U] ∈ A
U, we have: f(a) = ∑

u∈U fuau. Thus, if F : A
M −→ A
M is the corresponding

LCA, then, ∀ a = [am|m∈M] ∈ A
M, F(a) = ∑

u∈U fu · σu(a). In other words, we can formally

write F as a “polynomial of shift maps”:

F = ∑

u∈U fu · σu.

This deﬁnes an isomorphism of between the ring of LCA over A
M and the ring of formal
polynomials with coeﬃcients in A and “powers” in M. Composition of cellular automata
corresponds to multiplication of these polynomials.

Proposition 2. If F = ∑

u∈U fuσu, and G = ∑

v∈V gvσv, then F◦G = ∑

k∈M
 

 ∑

u∈U, v∈V
u.v=k
 fugv


 σk.

✷
 If F is a linear cellular automata with coeﬃcient system f = [fu|u∈U], and χ is a
character with coeﬃcient system χ = [χm|m∈M]
, then deﬁne χ ∗ f = [ξk|k∈M], where, for
all k ∈ M, ξk ∈ A is deﬁned:
 ξk = ∑

u∈U, m∈M
m.u=k
 (χm · fu)

(almost all terms in this sum are equal to 0). Then it is not hard to show:

Proposition 3. If χ ∈ ̂AM and F : A
M −→ A
M are determined by coeﬃcient systems χ
and f respectively, then χ ◦ F is also a character, and is determined by coeﬃcient system
χ ∗ f . ✷

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata 1273

3. Harmonic Mixing
A measure µ on A
M is called harmonically mixing if, for all ǫ > 0, there is some R > 0
so that, for all χ ∈ ̂AM, ( rank [χ] > R ) =⇒ ( |̂µ[χ]| < ǫ ). (Notice that this deﬁnition
does not require µ to be stationary.)
For example, H
aar is harmonically mixing; indeed, for all χ except the trivial character
11, we have: ⟨χ, H
aar ⟩ = 0.
Let M [A
M; C] be the Banach algebra of complex-valued measures (with convolution
operator “∗” and the total variation norm “∥•∥var”), and let H ⊂ M [
A
M; C] be the set of
harmonically mixing measures.

Proposition 4. H is an ideal of M [
A
M; C]
, closed under ∥•∥var.

Proof: H is clearly closed under linear operations. To show that H is a convolution ideal,
use the fact that ̂µ ∗ ν = ̂µ · ̂ν and that ̂ν is bounded by ∥ν∥var. Thus, if µ is harmonically
mixing, then so are µ ∗ ν and ν ∗ µ.

To show closure in ∥•∥var, use the fact that, for any measures µ and ν, ∥µ − ν∥var =
sup {
|⟨φ, µ⟩ − ⟨φ, ν⟩| ; φ ∈ C (
A
M; C) , ∥φ∥∞ = 1}
. ✷

Not all measures on A
M are harmonically mixing. For example, m ∈ M, we say
µ ∈ M [
A
M] is m-quasiperiodic if there is an orthonormal basis {ξn|n∈N} of L
2 (
A
M; µ)
,
consisting entirely of eigenfunctions of the shift map σm. It is not diﬃcult to show that, if
µ is m-quasiperiodic for any m ̸= IdM, then µ is not harmonically mixing.
Also, if χ : A
M −→ T
1 is a nontrivial character, then the Markov subgroup [12, 6, 4]
induced by χ is deﬁned:

A
M
χ := {a ∈ A
M ; χ ◦ σm(a) = 1, ∀m ∈ M
} .

If A
M
χ is nontrivial, it is a subshift of ﬁnite type. If µ is a stationary probability measure on
A
M
χ , then µ cannot be harmonically mixing: if m1, . . . , mK ∈ M are spaced widely enough

apart, and ξ :=
 K∏

k=1 χ ◦ σmk , then ⟨µ, ξ⟩ = 1, no matter how large K becomes.

However, µ may still be harmonically mixing relative to the elements of ̂AM
χ; see Corollary
13.

3.1. Harmonic Mixing of Bernoulli Measures

Proposition 5. Let A = Z/p, where p is prime. Let β be any measure on A which is

not entirely concentrated on one point. Let β⊗M = ⊗

m∈M β be the corresponding Bernoulli

measure on A
M. Then β⊗M is harmonically mixing.

Proof: ∀k ∈ A, let ck := 〈
γk, β〉
, where γk ∈ ̂A is as in §2.1. Since p is prime, |ck| < 1,

unless k = 0, while c0 = 1. Thus, c := max
0<k<p |ck| < 1. Thus, if χ ∈ ̂AM and rank [χ] = R,

then ∣
∣〈
χ, β⊗M〉∣
∣ =
 ∣
∣
∣
∣
∣
〈 ⊗

m∈M χm, ⊗

m∈M β
〉∣
∣
∣
∣
∣ =
 ∣
∣
∣
∣
∣
 ∏

m∈M ⟨χm, β⟩

∣
∣
∣
∣
∣ < cR becomes arbitrarily

small as R gets large. ✷

Prepared using etds.cls

1274 M. Pivato, R. Yassawi

A similar argument shows:

Proposition 6. Let A be an arbitrary ﬁnite abelian group, and β a measure on A. Suppose
that, for any subgroup G ⊂ A, the support of µ extends over more than one coset of G. Then
β⊗M is harmonically mixing. ✷

Corollary 7. H is weak* dense in M [
A
M]
.

Proof: Let µ ∈ M [
A
M] be arbitrary. For any ǫ ∈ [0, 1], let νǫ = β⊗M
ǫ ∈ M [
A
M] be
the Bernoulli measure with one-dimensional marginal βǫ, where βǫ[0] = 1 − ǫ, and, for
all a ∈ A \ {0}, βǫ[a] = ǫ/(A − 1) (where A = Card [A]). νǫ ∈ H by Proposition 5 so
νǫ ∗ µ ∈ H also, by Proposition 4.

We want to show that wk
∗−lim
ǫ→0 νǫ ∗ µ = µ; it is equivalent to show that lim
ǫ→0 ̂νǫ ∗ µ = ̂µ,

pointwise. Clearly, wk
∗−lim
ǫ→0 νǫ = δ0, where δ0 is the point mass on the constant zero

conﬁguration 0 ∈ A
M. Thus, for any χ ∈ ̂AM, ̂νǫ ∗ µ(χ) = ̂νǫ(χ) · ̂µ(χ) −−−−
ǫ→0−→
̂δ0(χ) · ̂µ(χ) = χ(0) · ̂µ(χ) = ̂µ(χ). ✷

3.2. Harmonic Mixing of Markov Measures Now let M = Z, and suppose that µ is
a Markov measure on A
Z, is determined by the transition probability matrix Q =
[
qa
b |a,b∈A]
, with stationary probability vector ν = [
νa|a∈A], so that Q · ν = ν.

Thus, if c ∈ A
Z is a µ-random conﬁguration, then νa = Prob [c0 = a], and
qa
b := Prob [c1 = b | c0 = a].

Proposition 8. Let A be any ﬁnite abelian group. If all entries of Q are nonzero, then µ
is harmonically mixing.

Proof: Let CA be the set of all functions ξ : A −→ C.

Deﬁne the operator Q : CA −→ CA as follows: for any ξ ∈ CA and any a ∈ A,

Q[ξ](a) = ∑

b∈A qa
b ξ(b).

In other words, Q[ξ](a) = ⟨ξ, q
a⟩, where q
a is the “ath” column of the matrix Q, and
we treat ξ as an A-indexed vector.

Next, for any χ ∈ ̂A, deﬁne the multiplication-by-χ operator: Mχ : CA −→ CA so that,
for any ξ ∈ CA and any a ∈ A, Mχ[ξ](a) = χ(a) · ξ(a).

Now, suppose χ = χ0 ⊗ χ1 ⊗ . . . ⊗ χN is a character on A
M (in other words, χ = ⊗

n∈Z χn,

but χn = 11 for all n > N and n < 0).

Claim 1:

(a) If N ≥ 1, then ⟨χ, µ⟩ = 〈
Mχ0 ◦ Q ◦ Mχ1 ◦ Q ◦ . . . ◦ MχN −1 ◦ Q[χN ], ν〉 .

(b) For any φ ∈ CA and any χ ∈ ̂A, ∥Mχ[φ]∥∞ = ∥φ∥∞.

(c) For any nonconstant φ ∈ CA, ∥Q[φ]∥∞ < ∥φ∥∞ .

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata 1275

Proof: (a) is just linear algebra. (b) is because, ∀a ∈ A, |χ(a)| = 1. To see (c), note

that, ∀a ∈ A, |Q[φ](a)| =
 ∣
∣
∣
∣
∣
∑

b∈A qa
b φ(b)

∣
∣
∣
∣
∣ ≤ ∑

b∈A qa
b |φ(b)| ≤ sup
b∈A |φ(b)| = ∥φ∥∞. The

ﬁrst (triangle) inequality is an equality if and only if all the elements of {φ(b) ; b ∈ A}
have the same phase angle. The second inequality is an equality if and only if they all
have the same magnitude. Hence, |Q[φ](a)| ≤ ∥φ∥∞, with equality if and only if φ is
constant. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ✷ [Claim 1]

Now, for any ξ, ζ ∈ ̂A, with ζ ̸= 11, deﬁne Pξ,ζ := Mξ ◦Q◦Mζ ◦Q. Then Pξ,ζ : CA −→ CA

is a linear operator. If CA is endowed with the ∥•∥∞ norm, then let ∥Pξ,ζ∥∞ be the
operator norm of Pξ,ζ.

Claim 2: ∥Pξ,ζ∥∞ < 1.

Proof: Let φ ∈ CA, with ∥φ∥∞ = 1. If φ is not constant, then by Claim 1c,
∥Q[φ]∥∞ < 1; thus, by Claim 1b and Claim 1c, ∥Mξ ◦ Q ◦ Mζ ◦ Q[φ]∥∞ ≤
∥Q[φ]∥∞ < 1. If φ is constant, then Mζ ◦ Q[φ] is not constant; thus, by Claim
1c, ∥Mξ ◦ Q ◦ Mζ ◦ Q[φ]∥∞ < ∥Mζ ◦ Q[φ]∥∞ ≤ ∥φ∥∞ = 1.

CA is ﬁnite-dimensional, so the unit ball B relative to the supremum norm ∥•∥∞ is
compact; hence ∥Pξ,ζ∥∞ = sup
φ∈B ∥Pξ,ζ[φ]∥∞ < 1. . . . . . . . . . . . . . . . . . . ✷ [Claim 2]

Thus, for all ξ, ζ ∈ ̂A, with ζ ̸= 11, let cξ,ζ := ∥Pξ,ζ∥∞, and let

C := max {
cξ,ζ ; ξ, ζ ∈ ̂A and ζ ̸= 11}

Thus, since cξ,ζ < 1 for all ξ, ζ, and since ̂A is ﬁnite, we conclude that C < 1 also. So,
given any ǫ > 0, if K is large enough, then CK < ǫ.

Now, if rank [χ] > 2K, then the product: χ = χ0 ⊗ χ1 ⊗ . . . ⊗ χN can be rewritten:

χ =
 

11 ⊗ . . . ⊗ 11
︸ ︷︷ ︸
n0
 

 ⊗ (ξ1 ⊗ ζ1) ⊗
 

11 ⊗ . . . ⊗ 11
︸ ︷︷ ︸
n1
 

 ⊗ (ξ2 ⊗ ζ2) ⊗ . . .

. . . ⊗
 


11 ⊗ . . . ⊗ 11
︸ ︷︷ ︸
nR−1
 


 ⊗ (ξR ⊗ ζR) ⊗
 

11 ⊗ . . . ⊗ 11
︸ ︷︷ ︸
nR
 

 ,

where R > K, and, for all r ∈ [0..R), ξr, ζr are successive elements in the list
χ0, χ1, . . . , χN −1, with ζr ̸= 11, and where n0, n1, . . . , nR ≥ 0, so that n0 + n1 +
. . . + nR + 2R = N . Thus, the operator Mχ0 ◦ Q ◦ Mχ1 ◦ Q ◦ . . . ◦ MχN −1 ◦ Q can be
rewritten as

Prepared using etds.cls

1276 M. Pivato, R. Yassawi

(Qn0 ◦ Pξ1,ζ1 ) ◦ (Qn1 ◦ Pξ2,ζ2 ) ◦ . . . ◦ (QnR−1 ◦ PξR,ζR) ◦ QnR. But then

|⟨χ, µ⟩| =(1) ∣
∣
〈Mχ0 ◦ Q ◦ Mχ1 ◦ Q ◦ . . . ◦ MχN −1 ◦ Q[χN ], ν〉∣
∣

≤(2) ∥
∥Mχ0 ◦ Q ◦ Mχ1 ◦ Q ◦ . . . ◦ MχN −1 ◦ Q[χN ]∥
∥
∞
≤(3) ∥
∥Mχ0 ◦ Q ◦ Mχ1 ◦ Q ◦ . . . ◦ MχN −1 ◦ Q∥
∥
∞
= ∥(Qn0 ◦ Pξ1,ζ1) ◦ (Qn1 ◦ Pξ2,ζ2 ) ◦ . . .

. . . ◦ (QnR−1 ◦ PξR,ζR) ◦ QnR∥∞
≤ ∥Pξ1,ζ1∥∞ · ∥Pξ2,ζ2∥∞ · . . . · ∥PξR,ζR∥∞
≤ CR < CK < ǫ

(1) by Claim 1a. (2) ν is a probability measure. (3) ∥χN ∥∞ = 1.

In summary, if rank [χ] > 2R, then |⟨χ, µ⟩| < ǫ. ✷

Corollary 9. Let A and µ be as in Theorem 8, and suppose ν is a measure on A
Z

absolutely continuous relative to µ. Then ν is also harmonically mixing.

Proof: Let φ = dν
dµ , and suppose ﬁrst that φ = 11[a]
µ[a] is the (renormalized) characteristic

function of some cylinder set [a] = {b ∈ A
Z ; bU = a
}
, where U = [−U . . . U ] ⊂ Z and
a ∈ A
U. Thus ν = µ[a], the (renormalized) restriction of µ to a probability measure on
[a] (that is: ν(B) = µ ([a] ∩ B) /µ ([a]) for any measurable B ⊂ A
Z).

Let χ =
 N⊗

n=−N χn be a character, and suppose N > U . Let χ(−) =
 −U−1⊗

n=−N χn and

χ(+) =
 N⊗

n=U+1 χn. Let µ(+)
[a] ∈ M [
A
(U...∞)] be the projection of µ[a] onto coordinates

(U...∞) (thus, if b ∈ A
(U..N ], then µ(+)
[a] [b] = qaU
b(U +1) · qb(U +1)
b(U +2) · . . . · qb(N −1)
bN ). Similarly,

let µ(−)
[a] be the projection of µ[a] onto coordinates (−∞ . . . −U ). Thus, using the Markov
property of µ,
 ⟨χ, ν⟩ = 〈χ(−), µ(−)
[a] 〉 ·
 ( U∏

u=−U χuau
)
 · 〈χ(+), µ(+)
[a] 〉

Now, analogous to Claim 1a of Theorem 8, we have:
〈χ(−), µ(−)
[a] 〉 = 〈Mχ(−N ) ◦ Q ◦ Mχ(1−N ) ◦ Q ◦ . . . ◦ Mχ(−U −1) ◦ Q[χU ], qa(−U ) 〉 ,

where qa(−U ) is the a(−U)th “row” of transition matrix Q, and, in a manner analagous to
the proof of Theorem 8, we can show that
∣
∣
∣〈
χ(−), µ(−)
[a] 〉∣
∣
∣ → 0 as rank [
χ(−)] → ∞.

By a similar argument (with reversed time), we can show
∣
∣
∣〈χ(+), µ(+)
[a] 〉∣
∣
∣ → 0 as rank [
χ(+)] → ∞.

This shows that ν is harmonically mixing.

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata 1277

The case when φ is simple —ie. a ﬁnite linear combination of characteristic functions of
cylinder sets —then follows immediately, via Proposition 4. If φ ∈ L
1(µ) is arbitrary, let
{φn|n∈N} be a sequence of simple functions converging to φ in the L
1 norm. Let {νn|n∈N}
be the corresponding measures (all harmonically mixing); thus, {νn|n∈N } converges to ν
in total variation norm, so ν is also harmonically mixing, by Proposition 4. ✷

Notice that the measure ν need not be stationary (and will not be, unless φ is shift-
invariant.)
An N -step Markov process is analogous to a Markov process, but the probability
distribution of each letter is dependent upon the previous N letters, and conditionally
independent of what comes before. When N = 0, we have a Bernoulli process; when
N = 1, a standard Markov process. In general, an N -step process is determined by a
collection of transition probabilities Q = {
qa
b ; a ∈ A
[0..N ), b ∈ A
} so that, for each

a ∈ A
[0..N ), ∑

b∈A qa
b = 1. One can then ﬁnd a (generally unique) stationary distribution ν

on A
[0..N ).

Corollary 10. Let A be a ﬁnite abelian group and let α be an N -step Markov process on
A, where all elements of Q are nonzero. Then α is harmonically mixing.

Proof: Let B = A
[1..N ], and consider the standard N -block coding map φ : A
Z −→ BZ,
deﬁned:

φ(. . . , a1, . . . , aN , aN +1, . . . , a2N , . . . ) =
 


. . . ,
 



 a1
.
aN
 


 ,
 



 aN +1
.
a2N
 


 , . . .





This is an isomorphism of topological groups, and the following diagram commutes:

A
Z σN
−→ A
Z

φ


↓ 

↓φ

BZ σ
−→ BZ

Thus, β = φ
∗α is a (1-step) Markov measure, with transition matrix
 P = [
pa
b|a,b∈B]
,

where p(a1,... ,aN )
(b1,... ,bN ) = q(a1,... ,aN )
b1 · q(a2,... ,aN ,b1)
b2 · q(a3,... ,aN ,b1,b2)
b3 · . . .· q(aN ,b1,... ,b(N −1))
bN . Clearly,

if all entries of Q are nonzero, then, so are all entries of P, and thus, by Proposition 8, β
is harmonically mixing. Hence, it suﬃces to show:

Claim 1: If β is harmonically mixing, then so is α.

Proof: The isomorphism φ : A
Z −→ BZ induces isomorphism ̂φ : ̂BZ −→ ̂AZ given:
̂φ(χ) := χ ◦ φ. Thus, ̂φ
−1 : ̂AZ −→ ̂BZ is an isomorphism, and, for any χ ∈ ̂AZ,

1. rank [ ̂φ
−1(χ)
] ≥ 1
N rank [χ].

2. 〈 ̂φ
−1(χ), β〉 = ⟨χ, α⟩.

Thus, if rank [χ] is large, then so is rank [ ̂φ
−1(χ)
]
; then 〈 ̂φ
−1(χ), β〉 is small, and thus

so is ⟨χ, α⟩. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ✷ [Claim 1]

Prepared using etds.cls

1278 M. Pivato, R. Yassawi
 ✷

An N -step Markov measure satisfying the hypothesis of Corollary 10 gives nonzero
probability to all cylinder sets of ﬁnite length; we might say it has “full support”.
The technique of Proposition 8 can be used to prove the corresponding result for
stationary Markov random ﬁelds on free groups and monoids [13, 14]. Now, instead of one
transition probability matrix, there are several: one for each generator of the group/monoid.
As long as there are ﬁnitely many generators, the bound C on the operator norms in the
proof of Proposition 8 will still be less than 1, and the same argument can be used to show:

Theorem 11. Let A be a ﬁnite group. Let M be a free group or free monoid on ﬁnitely
many generators, and let µ be a stationary Markov random ﬁeld on A
M so that all entries
in all transition probability matrices are nonzero. Then µ is harmonically mixing. ✷

4. Diﬀusive Linear Automata
Let F : A
M −→ A
M be a linear cellular automaton. We say that F is diﬀusive if, for every
nontrivial χ ∈ ̂AM, lim
n→∞ rank [χ ◦ Fn] = ∞.
For example, let A = Z/p for some prime p. Let M be the free group or free monoid on
D ≥ 2 generators. Let U ⊂ M be a ﬁnite subset with at least two elements, so that each
u ∈ U is a product of at least two distinct generators. It is straightforward to show:

If 0 ̸= fu ∈ Z/p, for all u ∈ U, then the automaton F = ∑

u∈U fuσu is diﬀusive.

Unfortunately, linear cellular automata on (
Z/p)(ZD) are never diﬀusive: if F is such an
LCA (e.g. F = f0 + f1 · σm1 + f2 · σm2 ), then, for any n ∈ N the LCA F(p
n) is simply F,
“rescaled” by a factor of pn (e.g. Fp = f0 + f1 · σ(p·m1) + f2 · σ(p·m2)). This follows from the
Fermat property for the ﬁeld Z/p. Thus, the polynomial of F(p
n) has the same number of
nonzero coeﬃcients as that of F, so F cannot “diﬀuse” along the subsequence {pn ; n ∈ N}.
This motivates a slight weakening of the concept of diﬀusion: we say that F is diﬀusive
in density if, for every nontrivial χ ∈ ̂AM, there is a subset J ⊂ N of Ces`aro density 1 so
that lim
j→∞
j∈J rank [χ ◦ Fj] = ∞.

Theorem 12. Let A be a ﬁnite abelian group, and M a countable monoid. Suppose that
F : A
M −→ A
M is a linear cellular automata, and suppose that µ is a measure on A
M that
is harmonically mixing.
1. If F is diﬀusive, then wk
∗−lim
j→∞ Fjµ = H
aar .

2. If F is diﬀusive in density, then there is a set J ⊂ N of Ces`aro density 1 so that

wk
∗−lim
j→∞
j∈J Fjµ = H
aar . Thus wk
∗− lim
N →∞ 1
N
 N∑

n=1 Fnµ = H
aar .

Proof: We’ll prove convergence in density, from which Ces`aro convergence follows
immediately. The proof of strict convergence is much the same.

We’ll show that the Fourier coeﬃcients of Fnµ all converge to zero in density. Weak*
convergence in density then follows by Theorem 1. So, let χ ∈ ̂AM. Then

⟨χ, Fnµ⟩ = ∫

AM χ d (Fnµ) = ∫

AM χ ◦ Fn dµ = ⟨(χ ◦ Fn) , µ⟩

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata 1279

Now, since F is diﬀusive in density, we can ﬁnd a subset Jχ ⊂ N of density 1 so that
lim
j→∞
j∈Jχ rank [χ ◦ Fj] = ∞. But then, since µ is harmonically mixing, it follows that

lim
j→∞
j∈Jχ
 〈(
χ ◦ Fj) , µ〉 = 0.

Now, A is ﬁnite and M is countable; thus, ̂AM is countable, so we can ﬁnd a “common
tail set” J ⊂ N so that:

• J has Ces`aro density 1.

• For every χ ∈ ̂AM, there is some N > 0 so that Jχ ∩ [N..∞) ⊂ J.

([11], Remark 2.6.3, or [3]). Thus, for all χ ∈ ̂AM, lim
j→∞
j∈J ⟨(χ ◦ Fn) , µ⟩ = 0. ✷

The same reasoning applies stationary measures supported on shift-invariant subgroups
of A
M:

Corollary 13. Let F : A
M −→ A
M be as in Theorem 12. Suppose that G ⊂ A
M is a closed
subgroup, and µ is a measure supported on G. Suppose µ is harmonically mixing relative to
the elements of ̂G, and F(G) ⊆ G. If F is diﬀusive (in density), then wk
∗−lim
j→∞ Fjµ = H
aar
G ,

where H
aar
G is the Haar measure on the compact group G (and where convergence is either
absolute or in density, as appropriate). ✷

To extend these results to aﬃne cellular automata, use the following:

Proposition 14. Let A be any ﬁnite group. Let F : A
M −→ A
M be an LCA with local
transformation f : A
U −→ A. Let c ∈ A be some constant, and let G be the ACA with local
map g : A
U −→ A given: g(a) = f(a) + c.
Let µ be a measure on A
M, and let J ⊂ N.

If wk
∗−lim
j→∞
j∈J Fjµ = H
aar then wk
∗−lim
j→∞
j∈J G
jµ = H
aar .

Proof: Let c0 ∈ A
M be the constant conﬁguration whose entries are all equal to c, and,
∀n ∈ N, let cn = Fn(c0). Let hn = c0 + c1 + . . . + cn, and deﬁne Hn : A
M −→ A
M by:
Hn(a) = a + hn. A simple computation establishes:

∀n ∈ N, G
n = Hn ◦ Fn.

If χ ∈ ̂AM, then for any a ∈ A
M, we have: χ ◦ Hn(a) = χ (a + hn) = Kn · χ(a), where
Kn = χ (hn) is some element of T
1. Concisely: χ ◦ Hn = Kn · χ.

Now, Fnµ converges in density to the Haar measure, in the weak* topology, which is
equivalent to saying: for every nontrivial character χ, there is a subset J ⊂ N of density
one such that lim
j→∞
j∈J
 〈
χ ◦ Fj, µ〉 = 0.

Now, for any j, 〈χ ◦ G
j, µ〉 = 〈
χ ◦ Hj ◦ Fj, µ〉 = 〈
Kj · χ ◦ Fj, µ〉 =
Kj · 〈χ ◦ Fj, µ〉
. But |Kj| = 1, and thus,
∣
∣〈
χ ◦ G
j , µ〉∣
∣ = ∣
∣〈
χ ◦ Fj, µ〉∣
∣ −−−−
j∈J
j→∞−→ 0.

Since this is true for each character, we conclude that G
nµ also converges in density to
the Haar measure. ✷

Prepared using etds.cls

1280 M. Pivato, R. Yassawi

5. Diﬀusion on Lattices
Say that an LCA F on A
M is nontrivial if F is not merely a shift map or the identity map.
If we write F as a polynomial of shift maps, then F is nontrivial if this polynomial contains
two or more nonzero coeﬃcients.

Theorem 15. Let p be a prime number, and A = Z/p. Let D ≥ 1. Then any nontrivial

linear cellular automaton on A(ZD) is diﬀusive in density.

The proof of this theorem will occupy the rest of this section. We will eventually
accomplish a reduction to the case when D = 1; hence, the reader may initially ﬁnd it
helpful to assume D = 1, and to treat all elements of Z
D (indicated as vectors, eg. “ ⃗m”) as
elements of Z instead (indicated as scalars, eg. “m”). It will also be helpful to ﬁrst work
through the details of the proof in the special case when p = 2; we will make reference to
this special case in footnotes.
We will represent LCA using the polynomial notation introduced in §2.2. It will be
convenient to write these polynomials in a special recursive fashion. For example, suppose
D = 1, and suppose that g0, g1, g2 ∈ [1..p), and ℓ0, ℓ1, ℓ2 ∈ Z. Let G be the linear CA on A
Z

deﬁned: G = g0σℓ0 + g1σℓ1 + g2σℓ2. Then we can rewrite G as:

G = g0 · (
F ◦ σℓ0 ) , where F = Id + f1σm1 (1 + f2σm2 ) , (2)

with m1 = ℓ1 − ℓ0, m2 = ℓ2 − ℓ1, f1 = g−1
0 g1 and f2 = g−1
1 g2 (with inversion in the ﬁeld
Z/p)†. More generally, we have the following:

Lemma 16. Let g0, g1, . . . , gJ ∈ [1..p), and ⃗ℓ0, ⃗ℓ1, . . . , ⃗ℓJ ∈ Z
D, and suppose that G is the
linear CA on A
(ZD ) deﬁned:

G = g0σ⃗ℓ0 + g1σ⃗ℓ1 + . . . + gJ σ⃗ℓJ . (3)

Then G = g0 · (
F ◦ σ⃗ℓ0 ) , where:

F = (4)

Id + f1σ ⃗m1 (Id + f2σ ⃗m2 [ . . . (
Id + fJ−1σ ⃗mJ−1 [Id + fJ σ ⃗mJ ]) . . .])

and, for all j ∈ [1..J], ⃗mj = ⃗ℓj − ⃗ℓj−1, and fj = g−1
j−1 · gj. ✷

Composing with the shift σ⃗ℓ0 and multiplying by the scalar g0 does not aﬀect the diﬀusion
property; hence, it is suﬃcient to prove Theorem for polynomials like (4). On ﬁrst reading,
it may be helpful to assume that J = 2, as in (2).
By Proposition 2, the powers FN of the linear cellular automaton F correspond to powers
of the corresponding polynomial. To prove Theorem 15, we will therefore need to develop
some machinery concerning multiplication of polynomials with coeﬃcients in Z/p, by using
the classical formula of Lucas [7] for the mod p binomial coeﬃcients, which has become
ubiquitous in the theory of LCA.

Definition 17. p-ary expansion, Index set.:

† If p = 2, we can assume that f1 = f2 = 1.

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata 1281

If n ∈ N, then the p-ary expansion of n is the sequence P(n) = {n[i]}∞
i=0 ∈ [0..p)
N,

such that n =
 ∞∑

i=0 n[i]pi.

The index set S(n) of n is deﬁned to be: S(n) = {i ∈ N ; n[i] ̸= 0} .

If m ∈ N, then let [m]p be the congruence class of m, mod p.

Lucas’ Theorem: Let N, n ∈ N, with p-ary expansions as before. Then
[ N
n
 ]
p =
 ∞∏

k=0
 [ N [k]

n[k]
 ]
p

where we deﬁne ( 0
0
 ) = 1, and ( a
b
 ) = 0, for any b > a > 0. ✷[7]

Write “n ≪ N ” if n[i] ≤ N [i] for all i ∈ N. Thus, Lucas’ Theorem implies:
( [ N
n
 ]
p ̸= 0
 )
 ⇐⇒ ( n ≪ N ) .

If n ∈ N, then the Lucas set of n is the set L(n) := {k ∈ N ; k ≪ n}.
The following elementary arithmetic observation will be used later.

Lemma 18. Let n1, n2, . . . , nL ∈ N. If M > 0, and for all ℓ ∈ [1..L] and i ≥ M , n[i]
l = 0,

then, for all i ≥ M + ⌈logp L⌉,
 ( L∑

l=1 nl
)[i]
 = 0.

(Here, ⌈n⌉ ∈ N is the smallest integer such that ⌈n⌉ ≥ n.)

Proof: The “logp” term comes from the fact that, in summing L distinct p-ary numbers,
there is the possibility of up to logp[L] digits of carried value spilling forward. ✷

With Lucas’ theorem, one can obtain expressions for powers of linear automata. For
example, if f ∈ Z/p, and F is the linear automata on A
Z deﬁned by F(x) = x + f · σ(x),
then Lucas’ Theorem tell us that

FN (x) = ∑

k ∈L(N )
 [ N
k
 ]
p f k · σkx .

Next, if m1, m2 ∈ Z, and f1, f2 ∈ Z/p, and F is as in (2), then

FN = ∑

k1 ∈L(N )
 [ N
k1
 ]
p f k1
1 · σm1k1 (1 + f2 · σm2 )
k1

= ∑

k1 ∈L(N )
 [ N
k1
 ]
p f k1
1 · σm1k1
 

 ∑

k2 ∈L(k1)
 [ k1
k2
 ]
p f k2
2 · σm2k2
 



= ∑

k1∈L(N )
 ∑

k2∈L(k1)
 ([ N
k1
 ]
p
 [ k1
k2
 ]
p f k1
1 f k2
2
 )
 · σm1k1+m2k2 .

= ∑

k1∈L(N )
 ∑

k2∈L(k1) f(k1,k2) · σm1k1+m2k2 ,

where we deﬁne f(k1,k2) := [ N
k1
 ]
p
 [ k1
k2
 ]
p f k1
1 f k2
2 .

Prepared using etds.cls

1282 M. Pivato, R. Yassawi

A similar argument works in Z
D, and for an arbitrary number of “nested” polynomial terms
of this type. This leads to the following

Lemma 19. If ⃗m1, ⃗m2, . . . , ⃗mJ ∈ Z
D, and f1, . . . , fJ ∈ Z/p, and F is as in (4), then

FN = ∑

k∈LJ (N ) f(k)σ⟨k,m⟩, (5)

where: m := [ ⃗m1, ⃗m2, . . . , ⃗mJ ] ,

L
J (N ) := {[k1, k2, . . . , kJ ] ∈ NJ ; kJ ≪ kJ−1 ≪ . . . k2 ≪ k1 ≪ N } ,

and, for any such k = [k1, k2, . . . , kJ ], we deﬁne

⟨k, m⟩ := k1 ⃗m1 + k2 ⃗m2 + . . . + kJ ⃗mJ

and f(k) := [ N
k1
 ]
p
 [ k1
k2
 ]
p . . . [ kJ−1
kJ
 ]
p f k1
1 f k2
2 . . . f kJ
J .

(the dependence on N is suppressed in the notation “f(k)”.) ✷

Proof of Theorem 15: It suﬃces to prove the theorem for polynomials F like (4).
So, suppose F is not diﬀusive in density. Thus, there exists some nontrivial character
χ ∈ ̂A(ZD ), some R ∈ N, and a subset B ⊂ N (of “bad” numbers), of upper density δ > 0,
so that, for all n ∈ B, rank [χ ◦ Fn] ≤ R.

Now, for each ⃗n ∈ Z
D, let pr⃗n : A
(ZD) −→ A be projection onto the ⃗nth coordinate:
pr⃗n(a) = a⃗n. Let γ : A −→ T
1 be the character introduced in §2.1: γ(a) =

exp ( 2πi
p · a). Thus, there is a ﬁnite subset Q ⊂ Z
D, and a collection of coeﬃcients
{χ⃗q ∈ [1..p) ; ⃗q ∈ Q} so that χ is deﬁned†:

χ(a) = ∏

⃗q∈Q γ (
χ⃗q · pr⃗q(a)
) (6)

Thus, if FN is as in (5) of Lemma 19, and χ is as in (6), then, by Proposition 3, the
character χ ◦ FN has the following expansion†:

χ ◦ FN = ∏

⃗q∈Q
 ∏

k∈LJ (N ) γ (χ⃗q · f(k) · pr(⟨k,m⟩+⃗q)) . (7)

Note that, for every ⃗q ∈ Q and k ∈ L
J (N ), the factor γ (
χ⃗q · f(k) · pr(⟨k,m⟩+⃗q))

is nontrivial: f(k) is never a multiple of p, and thus, if χ⃗q is nontrivial, then

γ (χ⃗q · f(k) · pr(⟨k,m⟩+⃗q)) is also nontrivial. Thus, the only way the coeﬃcients
of the character deﬁned by (7) can be trivial is if two terms of the form

† In the case when p = 2, we can write this: χ(a) = ∏

⃗q∈Q
(−1)
a⃗q .

† When J = 2 = p, and D = 1 the expansion is:

χ ◦ F
n(x) = ∏

q∈Q
 ∏

k1∈L(n)
 ∏

k2∈L(k1) (−1)
(k1m1+k2m2+q)

.

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata 1283

γ (χ∗
⃗q · f(k∗) · pr(⟨k∗,m⟩+⃗q∗)) and γ (
χ⃗q · f(k) · pr(⟨k,m⟩+⃗q)) cancel out, which can only
occur when
 ⟨k
∗, m⟩ + ⃗q∗ = ⟨k, m⟩ + ⃗q. (8)

This is an equation of D-tuples of integers, and hence, is only true if, for all d ∈ [1...D],

⟨k
∗, m⟩(d) + q∗
(d) = ⟨k, m⟩(d) + q(d) (9)

where the subscript “(d)” refers to the dth component of the D-tuple.

The idea of the proof is thus as follows: In order for the rank of the character χ ◦ FN

(for N ∈ B) to be less than R, most of the terms in the expression (7) must cancel out;
this requires a speciﬁc kind of “destructive interference” between the the index sets S(N )
and various translations of S(N ) so that virtually all elements (k, ⃗q) ∈ L
J (N ) × Q must
be paired up as in equation (8), so as to cancel with each other.

Our goal, then, is to show that the equation (8) is hard to achieve, so that, after the dust
settles, more than R nontrivial coeﬃcients remain. We will show that, the set B (indeed,
any set of nonzero density) must contain numbers for which suﬃcient cancellation fails
to occur.

Reduction to Case D = 1: In order for cancellation of terms (ie. equation (8)) to
occur in Z
D, equation (9) must be true for every d ∈ [1..D] simultaneously. Hence, it is
enough to disrupt the equation in one dimension. Hence, at this point, we can reduce
the argument to the case when D = 1. We will treat m1, . . . , mJ as elements of Z, and
m = [m1, . . . , mJ ] as a J-tuple of integers; thus, for any other J-tuple k = [k1, . . . , kJ ],
we have ⟨k, m⟩ = k1m1 + . . . kJ mJ . Likewise, Q will be some ﬁnite subset of Z.

Gaps in the Index set: We will use an ergodic argument to show that any subset
of N of nonzero density must contain numbers N possessing large “gaps” in their index
sets: i.e. P[N ] has long blocks of 0’s terminated by 1’s. We can then ﬁnd elements
k∗
1 ∈ L(N ) also exhibiting these long gaps. The gap in such a k∗
1 is long enough that
it is impossible to ﬁnd some other element (k, q) ∈ L
J (N ) × Q so that the terms in the
expression ⟨k, m⟩ + ⃗q sum together to “cancel” the terminating 1 in the gap of S(k∗
1 ).

Since there are many of these gaps, there are many such elements k∗
1, and thus, there
will be at least (R + 1) distinct 1’s that remain uncancelled, and thus at least (R + 1)
nontrivial terms in expression (7), contradicting the hypothesis that rank [χ ◦ FN ] ≤ R
for all N ∈ B.

We can assume that, when we transformed expression (3) into expression (4), we had
ℓ0 < ℓ1 < . . . < ℓJ ; hence, we can assume that m1, . . . , mJ > 0. Thus, they have
well-deﬁned Lucas sets, S(m1), . . . , S(mJ ). So, to begin, deﬁne:

Γ := max
 

 J⋃

j=1 S(mj )



 +
 



logp
 

 J∑

j=1 Card [S(mj )]


 + logp(J)





 + 2

Γ stands for “gap”, and is the size of the gaps we will require.

Prepared using etds.cls

1284 M. Pivato, R. Yassawi

Let q1 be the smallest element of Q, and deﬁne

Q1 := {
q − q1 ; q ∈ Q} , and U := ⋃

q∈Q1 S (q) .

Next, let w be the element of [0..p)
Γ+1 deﬁned: w := (0, . . . , 0
︸ ︷︷ ︸
Γ
 , 1). We will be concerned

with the frequency of occurrence of w in the p-ary expansions of integers.

Notation: If s = s0s1 . . . sn is a string in [0..p)
n, then we deﬁne the frequency of the
word w in s, denoted by f r[w, s], as

f r[w, s] := Card [
{i ∈ [0, n − 1] : sis(i+1)....s(i+Γ) = w}]

n

If sis(i+1) . . . s(i+Γ) = w, we’ll say that w occurs at si.

Claim 1: For any ǫ > 0, there exists M ∗ such that, for any M > M ∗, there is a set
GM
w (ǫ) ⊂ [1...p)
M so that:

Card [GM
w (ǫ)
] > (1 − ǫ)pM , and, ∀g ∈ GM
w (ǫ), f r[w, g] > (1 − ǫ)
p(Γ+1) .

Proof: Consider the ergodic dynamical system ([0..p)
N, H
aar , σ), where H
aar

is the Haar measure and σ : [0..p)
N → [0..p)
N is the shift action. The set{
a ∈ [0..p)
Z ; a[0...Γ] = w} has measure p−Γ−1. The result now follows from Birkhoﬀ’s

Ergodic Theorem. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ✷ [Claim 1]

In particular, let ǫ := δ
2p . Also, let ǫ∗ := 1 − ǫ
2 H
aar (w) = 1 − ǫ
2 p−1−Γ.

Claim 2: There exist M and N such that the following conditions are satisﬁed:

1. M ǫ∗ > R + 2,
2. U ⊂ [0, M ǫ∗],
3. N ∈ B ∩ [0, pM ),
4. f r[w, ⃗N ] > (1 − ǫ) p−1−Γ.

Proof: B has upper density δ, so there is some sequence {nk}∞
k=0 such that,

Card [B ∩ [0, nk]]
nk −−−−k→∞−→ δ.

Find K so that, for k > K, Card [B ∩ [0..nk]]
nk > δ
2 . Then choose M large enough to

satisfy [1] and [2], and such that pM−1 ≤ nk ≤ pM . Thus,

Card [B ∩ [
0, pM ]] ≥ Card [B ∩ [0, nk]] ≥ δnk
2 ≥ δpM−1

2

≥ δpM

2p . (10)

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata 1285

Also, by Claim 1, let M be large enough so that there is a subset GM
w (ǫ) ⊂ [0..p)
M so
that
 Card [GM
w (ǫ)
] > (1 − ǫ)pM = (
1 − δ
2p
 ) pM , (11)

and f r[w, a] > (1 − ǫ) p−1−Γ, for all a ∈ GM
w (ǫ).

Now, if G := {n ∈ [1..pM ] ; P(n) ∈ GM
w (ǫ)
}, then Card [G] = Card [GM
w (ǫ)
]. Thus,
combining (10) and (11), we see that Card [
B ∩ [0, pM ]] + Card [G] > pM ; hence, the
two sets must intersect nontrivially. Let N ∈ B ∩ [0, pM ] ∩ G; then N satisﬁes [3] and
[4]. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ✷ [Claim 2]

Claim 3: Let Q = ⌈M ǫ∗⌉. Then w occurs more than R times in the string:
(N [Q+1] N [Q+2] N [Q+3] . . . N [M]).

Proof: N satisﬁes condition [4] of Claim 2, and of course w occurs at most Q times
in the string (N 0 N [1] . . . N [Q]). Thus, beyond position Q, w must occurs at least
(
(1 − ǫ)p−1−ΓM ) − Q ≥ (
(1 − ǫ)p−1−ΓM ) − M ǫ∗ − 1

= (1 − ǫ)p−1−ΓM − (
M 1 − ǫ
2 p−1−Γ) − 1

= M 1 − ǫ
2 p−1−Γ − 1 = M ǫ∗ − 1

times and so, by condition [1] of Claim 1, at least R + 1 times. . . . . . . ✷ [Claim 3]

Say w occurs at some positions N [j1], N [j2], . . . , N [jR+1] beyond Q. Thus, for each
r ∈ [1...R + 1], we have: N [jr +k] = 0 for 0 ≤ k < Γ and N [jr +Γ] = 1. In particular,

∀r ∈ [1...R + 1], pjr +Γ ∈ L(N ). (12)

Now, N ∈ B, so rank [
χ ◦ FN ] ≤ R. This means that in the expression (7), all but at
most R of the terms are cancelled by a like term. In other words, for all but R of the
elements: (k
∗, q∗) ∈ L
J (N ) × Q, there exists some (k, q) ∈ L
J (N ) × Q so that

⟨k
∗, m⟩ + q∗ = ⟨k, m⟩ + q. (13)

—we say that (k
∗, q∗) is annihilated by (k, q).

However, there are R + 1 elements in the set {jr}R+1
r=1 , and thus, there are R + 1 pairs of
the form (k
∗
r, q1), where k
∗
r = (
p(jr+Γ), 0, . . . , 0)
. Hence there exists some r such that
the pair (k
∗
r, q1) is annihilated by some other pair (k, q). Deﬁne n := jr + Γ; then
⟨k
∗
r, m⟩ = m1pn, so we can rewrite (13) as:

m1pn = ⟨k, m⟩ + (q − q1), (14)

where k = [k1, . . . , kJ ] is some other element in L
J (N ).

Claim 4: For all j ∈ [1..J], and all i ≥ n − Γ, we have: kj [i] = 0.

Prepared using etds.cls

1286 M. Pivato, R. Yassawi

Proof: First we’ll show k[i]
1 = 0 for i ≥ n. The RHS and LHS of (14) must come from
diﬀerent terms of the expansion (7), which means that either q ̸= q1 or kj ̸= 0 for some
j > 1 ; either way, one of the other terms on the RHS is positive besides “m1k1”, and
therefore, m1k1 < m1pn. Thus, k1 < pn, and thus, k[i]
1 = 0 for all i ≥ n.

Next we’ll show k[i]
1 for n − Γ ≤ i < n. Recall that k1 ∈ L(N ), and by hypothesis,
N [i] = 0 for all i ∈ [jr...(jr + Γ)), where n = jr + Γ and n − Γ = jr. Thus, k1[i] = 0 for
n − Γ ≤ i < n.
Since kJ ≪ kJ−1 ≪ . . . ≪ k2 ≪ k1, the same holds for k2, . . . , kJ . . . . . ✷ [Claim 4]

Claim 5: For all j ∈ [1..J], and all i ≥ n − 2 − logp(J), we have: (mj kj)
[i] = 0.

Proof: Fix j ∈ [1..J]. For any s ∈ S(mj), it follows from Claim 4 that
(m[s]
j pskj)[i] = 0, for all i ≥ n − Γ + s.

Hence, by Lemma 18,

(mjkj)[i] =
 

 ∑

s∈S(mj ) m[s]
j pskj



[i]

= 0, ∀i ≥ n − Γ + max [S(mj )] + logp (Card [S(mj )]) .

The claim now follows from the deﬁnition of Γ. . . . . . . . . . . . . . . . . . . . . ✷ [Claim 5]

Claim 6: For all i ≥ n − 3, (q − q1)
[i] = 0.

Proof: By deﬁnition, n − 3 > n − Γ = jr > Q ≥ M ǫ∗. Recall that condition [2]
deﬁning M was: U ⊂ [0, M ǫ∗]. Thus, (q − q1)
[i] = 0 for i ≥ M ǫ∗. . . . . ✷ [Claim 6]

Claim 7: For all i ≥ n − 1, (⟨k, m⟩ + (q − q1))[i] = 0.

Proof: Recall that ⟨k, m⟩ = (k1m1) + . . . + (kJ mJ ); thus, it follows from Claim 5
and Lemma 18 that ⟨k, m⟩
[i] = 0, ∀i ≥ n − 2.
Thus, the claim follows from Claim 6 and Lemma 18. . . . . . . . . . . . . . . . ✷ [Claim 7]

Now, by hypothesis, ⟨k, m⟩ + (q − q1) = m1pn. Hence, (⟨k, m⟩ + (q − q1))[i]

= (m1pn)
[i] for all i ∈ N. In particular, if I := min [S(m1)] ≥ 0, then

(⟨k, m⟩ + (q − q1))[I+n] = (m1pn)
[I+n] = m[I]
1 ̸= 0.

But I + n ≥ n, so this is a contradiction of Claim 7. ✷

Conclusion
We have shown that harmonically mixing measures on A
M, when acted upon by diﬀusive
linear cellular automata (possibly with an aﬃne part), will weak*-converge, in Ces`aro mean,
to the Haar measure. This suﬃcient condition is broadly applicable: in particular, if
A = Z/p, then any nontrivial linear cellular automata acting upon a “fully supported” N -
step Markov measure (in Z, a regular tree, or a free group) or a nontrivial Bernoulli measure
(in Z
D) will converge to Haar in Ces`aro mean.

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata 1287

In a forthcoming paper [8], we generalize the results on diﬀusion to the case when A = Z/n
(n ∈ N arbitrary) and A = (
Z/(pr ))J (p prime, r, J ∈ N), and we demonstrate harmonic

mixing for Markov random ﬁelds on A(ZD), for D ≥ 2. However, many questions remain
unanswered. What other classes of measures on Z or Z
D are harmonically mixing? Measures
on A
M exhibiting quasiperiodicity cannot be harmonically mixing; what is the Ces`aro limit
of such a measure, if anything? Also, what LCA are diﬀusive, when M is neither a lattice
nor a free group?

Acknowledgments: We would like to thank David Poole of Trent University for
introducing us to Lucas’ Theorem, and Dan Rudolph of the University of Maryland for
reminding us that, for stationary µ, Ces`aro convergence to H
aar is equivalent to convergence
in density.
 References

[1] Alejandro Maass and Servet Mart´inez. Time averages for some classes of expansive one-dimensional
cellular automata. In Eric Goles and Servet Martinez, editors, Cellular Automata and Complex
Systems, pages 37–54. Kluwer Academic Publishers, Dordrecht, 1999.
[2] G. Hedlund. Endomorphisms and automorphisms of the shift dynamical systems. Mathematical
System Theory, 3:320–375, 1969.
[3] Lee Kenneth Jones. A mean ergodic theorem for weakly mixing operators. Advances in Mathematics,
7:211–216, 1971.
[4] Bruce Kitchens and K. Schmidt. Markov subgroups of (Z/2Z)Z
2 . In Peter Walters, editor,
Symbolic Dynamics and its Applications, volume 135 of Contemporary Mathematics, pages 265–283,
Providence, 1992.
[5] Douglas Lind. Applications of ergodic theory and soﬁc systems to cellular automata. Physica D,
10:36–44, 1984.
[6] Douglas Lind and Brian Marcus. An Introduction to Symbolic Dynamics and Coding. Cambridge
University Press, New York, ﬁrst edition, 1995.
[7] E. Lucas. Sur les congruences des nombres Eul´eriens et des coeﬃcients diﬀ´erentiels des fonctions
trigonom´etriques, suivant un module premier. Bulletin de la Soci´et´e Math´ematique de France, 6:49–
54, 1878.
[8] Marcus Pivato and Reem Yassawi. Limit measures for aﬃne cellular automata
II. Submitted to Ergodic Theory and Dynamical Systems; preprint available at:
http://arXiv.org/abs/math.DS/0108083, April 2001.
[9] Servet Mart´inez Pablo Ferrari, Alejandro Maass. Ces`aro mean distribution of group automata
starting from Markov measures. (preprint), 1998.
[10] Servet Mart´inez Pablo Ferrari, Alejandro Maass and Peter Ney. Ces`aro mean distribution of group
automata starting from measures with summable decay. Ergodic Theory and Dynamical Systems,
20(6):1657–1670, 2000.
[11] Karl Petersen. Ergodic Theory. Cambridge University Press, New York, 1989.
[12] Klaus Schmidt. Dynamical Systems of Algebraic Origin. Birkh¨auser Verlag, Boston, Massachusetts,
1995.
[13] F. Spitzer. Markov random ﬁelds on an inﬁnite tree. Annals of Probability, 3:387–398, 1975.
[14] S. Zachary. Countable state space Markov random ﬁelds and Markov chains on trees. Annals of
Probability, 11:894–903, 1983.

Prepared using etds.cls
