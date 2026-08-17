<!-- source: https://arxiv.org/pdf/2102.08207 | converted from PDF -->

Logical Methods in Computer Science
Volume 20, Issue 3, 2024, pp. 12:1–12:38
https://lmcs.episciences.org/ Submitted Aug. 31, 2022
Published Aug. 05, 2024

DECIDABILITY FOR STURMIAN WORDS

PHILIPP HIERONYMI a, DUN MA b, REED OEI c, LUKE SCHAEFFER d, CHRIS SCHULZ e,f ,
AND JEFFREY SHALLIT g

a Mathematisches Institut, Universit¨at Bonn, Endenicher Allee 60, D-53115 Bonn, Germany
e-mail address: hieronymi@math.uni-bonn.de
URL: https://www.math.uni-bonn.de/people/phierony/

b Department of Computer Science and Engineering, University of California, San Diego, 9500 Gilman
Drive, La Jolla, CA 92093-0404, USA
e-mail address: d4ma@ucsd.edu

c Department of Mathematics, University of Illinois at Urbana-Champaign, 1409 West Green Street,
Urbana, IL 61801, USA

d Institute for Quantum Computing, University of Waterloo, Waterloo, Ontario, N2L 3G1, Canada
e-mail address: lrschaeffer@gmail.com

e Department of Mathematics, University of Illinois at Urbana-Champaign, 1409 West Green Street,
Urbana, IL 61801, USA

f Department of Pure Mathematics, 200 University Avenue West, Waterloo, Ontario, N2L 3G1,
Canada
e-mail address: chris.schulz@uwaterloo.ca

g School of Computer Science, University of Waterloo, Waterloo, Ontario, N2L 3G1, Canada
e-mail address: shallit@uwaterloo.ca
URL: https://cs.uwaterloo.ca/~shallit/

In Memory of Reed Oei (1999-2022)

Abstract. We show that the first-order theory of Sturmian words over Presburger arith-
metic is decidable. Using a general adder recognizing addition in Ostrowski numeration
systems by Baranwal, Schaeffer and Shallit, we prove that the first-order expansions of
Presburger arithmetic by a single Sturmian word are uniformly ω-automatic, and then
deduce the decidability of the theory of the class of such structures. Using an implementa-
tion of this decision algorithm called Pecan, we automatically reprove classical theorems
about Sturmian words in seconds, and are able to obtain new results about antisquares
and antipalindromes in characteristic Sturmian words.

LOGICAL METHODSlIN COMPUTER SCIENCE DOI:10.46298/LMCS-20(3:12)2024 © P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit

CC⃝ Creative Commons

12:2 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

1. Introduction

It has been known for some time that, for certain infinite words c = c0c1c2 · · · over a finite
alphabet Σ, the first-order logical theory FO(N, <, +, 0, 1, n ↦→ cn) is decidable. In the case
where c is a k-automatic sequence for k ≥ 2, this is due to B¨uchi [B¨uc62], although
his original proof was flawed. The correct statement appears, for example, in Bruy`ere et
al. [BHMV94b, BHMV94a]. Although the worst-case running time of the decision procedure
is truly formidable (and non-elementary), it turns out that an implementation can, in many
cases, decide the truth of interesting and nontrivial first-order statements about automatic
sequences in a reasonable length of time. Thus, one can easily reprove known results, and
obtain new ones, merely by translating the desired result into the appropriate first-order
statement φ and running the decision procedure on φ. For an example of the kinds of things
that can be proved, see Goˇc, Henshall, and Shallit [GHS13].

More generally, the same ideas can be used for other kinds of sequences defined in terms of
some numeration system for the natural numbers. Such a numeration system provides a
unique (up to leading zeros) representation for n as a sum of terms of some other sequence
(sn)n≥1. If the sequence c = c0c1c2 · · · can be computed by a finite automaton taking the
representation of n as input, and if further, the addition of represented integers is computable
by another finite automaton, then once again the first-order theory FO(N, <, +, 0, 1, n ↦→ cn)
is decidable. This is the case, for example, for the so-called Fibonacci-automatic sequences
in Mousavi, Schaeffer, and Shallit [MSS16] and the Pell-automatic sequences in Baranwal
and Shallit [BS19].

More generally, the same kinds of ideas can handle Sturmian words. For quadratic numbers,
this was first observed by Hieronymi and Terry [HT18]. In this paper we extend those results
to all Sturmian characteristic words. Thus, the first-order theory of Sturmian characteristic
words is decidable. As a result, many classical theorems about Sturmian words, which
previously required intricate proofs, can be proved automatically by a theorem-prover in
a few seconds. As examples, in Section 7 we reprove basic results such as the balanced
property and the subword complexity of these words.

Let α, ρ ∈ R be such that α is irrational. The Sturmian word with slope α and
intercept ρ is the infinite {0, 1}-word cα,ρ = cα,ρ(1)cα,ρ(2) · · · such that for all n ∈ N

cα,ρ(n) = ⌊α(n + 1) + ρ⌋ − ⌊αn + ρ⌋ − ⌊α⌋.

When ρ = 0, we call cα,0 the characteristic word of slope α. Sturmian words and their
combinatorical properties have been studied extensively. We refer the reader to the survey
by Berstel and S´e´ebold [Lot02, Chapter 2]. Note that cα,ρ can be understood as a function
from N to {0, 1}. Let L be the signature1 of the first-order logical theory FO(N, <, +, 0, 1)
and denote by Lc the signature obtained by adding a single unary function symbol c to L.
Now let Nα,ρ be the Lc-structure (N, <, +, 0, 1, n ↦→ cα,ρ(n)), where we expand Presburger
arithmetic by a Sturmian word interpreted as a unary function. The main result of this paper
is the decidability of the theory of the collection of such expansions. Set Irr := (0, 1) \ Q.
Let Ksturmian := {Nα,ρ : α ∈ Irr, ρ ∈ R}, and let Kchar := {Nα,0 : α ∈ Irr}.

1In model theory this is usually called (or identified with) the language of the theory. However, here this
conflicts with the convention of calling an arbitrary set of words a language.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:3

Theorem A. The first-order logical theories
2 FO(Ksturmian) and FO(Kchar) are decidable.

So far, decidability was only known for individual FO(Nα,ρ), and only for very particular
α. By [HT18] the logical theory FO(Nα,0) is decidable when α is a quadratic irrational3.
Moreover, if the continued fraction of α is not computable, it can be seen rather easily that
FO(Nα,0) is undecidable.

Theorem A is rather powerful, as it allows to automatically decide combinatorial statements
about all Sturmian words. Consider the Lc-sentence φ

∀p (p > 0) → (∀i ∃j j > i ∧ c(j) ̸= c(j + p)
).

We observe that Nα,ρ |= φ if and only if cα,ρ is not eventually periodic. Thus the decision
procedure from Theorem A allows us to check that no Sturmian word is eventually peri-
odic. Of course, it is well-known that no Sturmian word is eventually periodic, but this
example indicates potential applications of Theorem A. We outline some of these in Section 7.

We not only prove Theorem A, but instead establish a vastly more general theorem of which
Theorem A is an immediate corollary. To state this general result, let Lm be the signature
of FO(R, <, +, Z); that is, the signature of FO(R, <, +) together with a unary predicate
for Z. Let Lm,a be the extension of Lm by another unary predicate. For α ∈ R>0, we
let Rα denote Lm,a-structure (R, <, +, Z, αZ). When α ∈ Q, it has long been known that
FO(Rα) is decidable (arguably due to Skolem [Sko31]). Recently this result was extended
to quadratic numbers.

Fact 1.1 (Hieronymi [Hie16, Theorem A]). Let α be a quadratic irrational. Then FO(Rα)
is decidable.

See also Hieronymi, Nguyen and Pak [HNP21] for a computational complexity analysis of
this decision procedure. The proof of Fact 1.1 establishes that if α is quadratic, then Rα is
an ω-automatic structure; that is, it can be represented by B¨uchi automata. Since every
ω-automatic structure has a decidable first-order theory, so does Rα. See Khoussainov and
Minnes [KM10] for a survey on ω-automatic structures. The key insight needed to prove
ω-automaticity of Rα is that addition in the Ostrowski-numeration system based on α is
recognizable by a B¨uchi automaton when α is quadratic. See Section 2 for a definition of
Ostrowski numeration systems.

As observed in [Hie16], there are examples of non-quadratic irrationals α such that Rα
has an undecidable theory and hence is not ω-automatic. However, in this paper we show
that the common theory of the Rα is decidable. Let K denote the class of Lm,a-structures
{Rα : α ∈ Irr}.

Theorem B. The theory FO(K) is decidable.

Indeed, we will even prove a substantial generalization of Theorem B. For each Lm,a-sentence
φ, we set Mφ := {α ∈ Irr : Rα |= φ}. Let Irrquad be the set of all quadratic irrational real
numbers in Irr. Define M := (Irr, <, (Mφ)φ, (q)q∈Irrquad)

2Given a signature L0 and a class K of L0-structures, the first-order logical theory of K is defined as the
set of all L0-sentences that are true in all structures in K. This theory is denoted by FO(K).
3A real number is quadratic if it is the root of a quadratic equation with integer coefficients.

12:4 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

to be the expansion of the dense linear order (Irr, <) by predicates for Mφ for each Lm,a-
sentence φ, and constant symbols for each quadratic irrational real number in Irr.

Theorem C. The theory FO(M) is decidable.

Observe that Fact 1.1 and Theorem B follow immediately from Theorem C. We outline how
Theorem B implies Theorem A. Note that for every irrational α, the structure Rα defines
the usual floor function ⌊·⌋ : R → Z, the singleton {α} and the successor function on αZ.
Hence Rα also defines the set {(ρ, αn, cα,ρ(n)) : ρ ∈ R, n ∈ N}. From the definability of
{α}, we have that the function from αN to {0, α} given by αn ↦→ αcα,ρ(n) is definable in
Rα. Thus the Lc-structure (αN, <, +, 0, α, αn ↦→ αcα,ρ(n)) can be defined in Rα, and this
definition is uniform in α. Since the former structure is Lc-isomorphic to Nα,ρ, we have that
for every Lc-sentence φ there is an Lm,a-formula ψ(x) such that
• φ ∈ FO(Ksturmian) if and only if ∀x ψ(x) ∈ FO(K) and
• φ ∈ FO(Kchar) if and only if ψ(0) ∈ FO(K).
Even Theorem C is not the most general result we prove. Its statement is more technical and
we postpone it until Section 6. However, we want to point out that we can add predicates for
interesting subsets of Irr to M without changing the decidability of the theory. Examples of
such subsets are the set of all α ∈ Irr such that the terms in the continued fraction expansion
of α are powers of 2, or the set of all α ∈ Irr such that the terms in the continued fraction
expansion of α are not in some fixed finite set. This means we can not only automatically
prove theorems about all characteristic Sturmian words, but also prove theorems about
all characteristic Sturmian words whose slope is one of these sets. There is a limit to this
technique. If we add a predicate for the set of all α ∈ Irr such that the terms of continued
fraction expansion of α are bounded, or add a predicate for the set of elements in Irr whose
continued fractions has strictly increasing terms, then our method is unable to conclude
whether the resulting structure has a decidable theory. See Section 6 for a more precise
statement about what kind of predicates can be added.

The proof of Theorem C follows closely the proof from [Hie16] of the ω-automaticity of Rα
for fixed quadratic α. Here we show that the construction of the B¨uchi automata needed to
represent Rα is actually uniform in α. See Abu Zaid, Gr¨adel and Reinhardt [AZGR17] for a
systematic study of uniformly automatic classes of structures. Deducing Theorem C from
this result is then rather straightforward. The key ingredient to establish the ω-automaticity
of Rα is an automaton that can perform addition in Ostrowski-numeration systems. By
[HT18] there is an automaton that recognizes the addition relation for α-Ostrowski numera-
tion systems for fixed quadratic α. So for a fixed quadratic number, there exists a 3-input
automaton that accepts the α-Ostrowski representations of all triples of natural numbers
x, y, z with x + y = z. In order to prove Theorem C, we need a uniform version of such an
adder. This general adder is described in Baranwal, Schaeffer, and Shallit [BSS21]. There a
4-input automaton is constructed that accepts 4-tuples consisting of an encoding of a real
number α and three α-Ostrowski representations of natural numbers x, y, z with x + y = z.
See Section 4 for details.

As mentioned above, an implementation of the decision algorithm provided by Theorem
A can be used to study Sturmian words. We created a software program called Pecan
[OMSH20] that includes such an implementation. Pecan is inspired by Walnut [Mou16]
by Mousavi, an automated theorem-prover for deciding properties of automatic words.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:5

The main difference is that Walnut is based on finite automata, while Pecan uses B¨uchi
automata. In our setting it is more convenient to work with B¨uchi automata instead of finite
automata, since the infinite families of words we want to consider—like Sturmian words—are
indexed by real numbers. Section 7 provides more information about Pecan and contains
further examples how Pecan is used to prove statements about Sturmian words. Pecan’s
implementation is discussed in more detail in [OMSH21].

This is an extended version of the paper [HMO+22] presented at CSL 2022.

Acknowledgments. Part of this work was done in the research project “Building a theorem-
prover” at the Illinois Geometry Lab in Spring 2020. P.H. and C.S. were partially supported
by NSF grant DMS-1654725. P.H. was partially supported by the Hausdorff Center for
Mathematics at the University of Bonn. We thank Mary Angelica Gramcko-Tursi and Sven
Manthe for carefully reading a draft of this paper.

2. Preliminaries

Throughout, i, j, k, ℓ, m, n are used for natural numbers. Let X, Y be two sets and Z ⊆ X ×Y .
For x ∈ X, we let Zx denote the set {y ∈ Y : (x, y) ∈ Z}. Similarly, given a function
f : X × Y → W and x ∈ X, we write fx for the function fx : Y → W that maps y ∈ Y to
f (x, y).

Given a (possibly infinite word) w over an alphabet Σ, we write wi for the i-th letter of
w, and w|n for w1 · · · wn. We write |w| for the length of w. We let Σω denote the set of
infinite words over Σ. If Σ is totally ordered by ≺, we let ≺lex denote the corresponding
lexicographic order on Σω. Letting u, v ∈ Σω, we also write u ≺colex v if there is a maximal
i such that ui ̸= vi, and ui < vi for this i. Note that while ≺lex is a total order on Σω, the
order ≺colex is only a partial order. However, for a given σ ∈ Σ, the order ≺colex is a total
order on the set of all words v ∈ Σω such that vj is eventually equal to σ.

We will also need to apply ≺lex and ≺colex to finite sequences u, v of the same length. We
do this by choosing a σ ∈ Σ (the choice does not matter) and stating that u ≺lex v iff
uσω ≺lex vσω, and similarly for ≺colex.

A B¨uchi automaton (over an alphabet Σ) is a quintuple A = (Q, Σ, ∆, I, F ) where Q
is a finite set of states, Σ is a finite alphabet, ∆ ⊆ Q × Σ × Q is a transition relation, I ⊆ Q
is a set of initial states, and F ⊆ Q is a set of accept states.

Let A = (Q, Σ, ∆, I, F ) be a B¨uchi automaton. Let σ ∈ Σω. A run of σ from p is an
infinite sequence s of states in Q such that s0 = p, (sn, σn, sn+1) ∈ ∆ for all n < |σ|. If
p ∈ I, we say s is a run of σ. Then σ is accepted by A if there is a run s0s1 · · · of σ such
that {n : sn ∈ F } is infinite. We call this run an accepting run. We let L(A) be the set of
words accepted by A.

If for every state s in A there is a run of some string from an initial state through s to an
accept state, where s is not the last state in the run, then we say A is trim. Every B¨uchi
automaton has an equivalent trim automaton, which may be obtained simply by removing

12:6 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

(possibly iteratively) every state failing this condition. There are other types of ω-automata
with different acceptance conditions, but in this paper we only consider B¨uchi automata.

Let Σ be a finite alphabet. We say a subset X ⊆ Σω is ω-regular if it is recognized by
some B¨uchi automaton. Let u1, . . . , un ∈ Σω. We define the convolution c(u1, . . . , un) of
u1, . . . , un as the element of (Σn)ω whose value at position i is the n-tuple consisting of the
values of u1, . . . , un at position i. We say that X ⊆ (Σω)n is ω-regular if c(X) is ω-regular.

Fact 2.1. The collection of ω-regular sets is closed under union, intersection, complementa-
tion and projection.

Closure under complementation is due to B¨uchi [B¨uc62]. We refer the reader to Khoussainov
and Nerode [KN01] for more information and a proof of Fact 2.1. As consequence of Fact
2.1, we have that for every ω-regular subset W ⊆ (Σω)m+n the set

{s ∈ (Σ
ω)
m : ∀t ∈ (Σ
ω)
n (s, t) ∈ W }

is also ω-regular.

The proof of Theorem 4.1 will utilize a few other related types of automaton. A finite
automaton has the same internal structure as a B¨uchi automaton i.e. is also a quintuple
A = (Q, Σ, ∆, I, F ) with the same restrictions, but it takes a finite word σ ∈ Σ∗ as input. In
the case of a finite automaton, runs are finite sequences instead of infinite sequences but
otherwise follow the same rule on transitions. We say that σ is accepted by A in this case
if there is a run of σ such that s|σ| ∈ F .

We will also refer to general finite and B¨uchi automata. These are the same as finite and
B¨uchi automata, respectively, but where Σ is no longer required to be a finite alphabet.
Note that Q is still finite in these cases; therefore ∆, viewed as a directed multigraph on Q,
still has finitely many vertices but may have infinitely many arrows between the same pair
of vertices. General finite and B¨uchi automata are not often considered, as they do not have
the same computability properties
4 , but they may sometimes be converted into “equivalent”
finite and B¨uchi automata, as we will see in Section 4.

2.1. ω-regular structures. Let U = (U ; R1, . . . , Rm) be a structure, where U is a non-
empty set and R1, . . . , Rm are relations on U . We say U is ω-regular if its domain and its
relations are ω-regular.

B¨uchi’s theorem [B¨uc62] on the decidability of the monadic second-order theory of one
successor immediately gives the following well-known fact.

Fact 2.2. Let U be an ω-regular structure. Then the theory FO(U) is decidable.

In this paper, we will consider families of ω-regular structures that are uniform in the
following sense. Fix m ∈ N and a map ar : {1, . . . , m} → N. Let Z be a set and for z ∈ Z
let Uz be a structure (Uz; R1,z, . . . , Rm,z) such that Ri,z ⊆ U ar(i)
z . We say that (Uz)z∈Z is a
uniform family of ω-regular structures if

4To see why, consider e.g. a generalized B¨uchi automaton recognizing words over N consisting of a
single initial state q0 and a single final state q1 such that there is a noncomputable set S ⊆ N with
∆ = {(q0, s, q1) : s ∈ S}.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:7

• {(z, y) : y ∈ Uz} is ω-regular,
• {(z, y1, . . . , yar(i)) : (y1, . . . , yar(i)) ∈ Ri,z} is ω-regular for each i ∈ {1, . . . , m}.

We refer the reader to [AZGR17] for an in-depth analysis of uniformity in automatic structure.

From B¨uchi’s theorem, we immediately obtain the following.

Fact 2.3. Let (Uz)z∈Z be a uniform family of ω-regular structures, and let φ be a formula
in the signature of these structures. Then the set

{(z, u) : z ∈ Z, u ∈ Uz, Uz |= φ(u)}

is ω-regular, and, the automaton recognizing this set can be effectively computed given φ.
Moreover, the theory FO({Uz : z ∈ Z}) is decidable.

Proof. When φ is an atomic formula, the statement follows immediately from the definition
of a uniform family of ω-regular structures and the ω-regularity of equality. By Fact 2.1, the
statement holds for all formulas.

Let w ∈ Σω. The acceptance problem for w is the following decision problem:

Given a B¨uchi automaton A over Σ, is w accepted by A?

For examples of non-ω-regular words with a decidable acceptance problem, see Elgot and
Rabin [ER66], Semenov [Sem83] or Carton and Thomas [CT02]. We obtain the following
well-known corollary of Fact 2.3.

Fact 2.4. Let (Uz)z∈Z be a uniform family of ω-regular structures, and let w ∈ Z be such
that the acceptance problem for w is decidable. Then the theory FO(Uw) is decidable.

2.2. Binary representations. For k ∈ N>1 and b = b0b1b2 · · · bn ∈ {0, 1, . . . , k − 1}∗, we
define [b]k := ∑n
i=0 biki. For N ∈ N we say b ∈ {0, 1}∗ is a binary representation of N if
[b]2 = N .

Throughout this paper, we will often consider infinite words over the (infinite) alphabet
{0, 1}∗. Let [·]2 : ({0, 1}∗)ω → Nω be the function that maps u = u1u2 · · · ∈ ({0, 1}∗)ω to

[u1]2[u2]2[u3]2 · · · .

We will consider the following different relations on ({0, 1}∗)ω.

Let u, v ∈ ({0, 1}∗)ω. We write u <lex,2 v if [u]2 is lexicographically smaller than [v]2. We
write u <colex,2 v if there is a maximal i such that [ui]2 ̸= [vi]2, and [ui]2 < [vi]2. Note that
while <lex,2 is a total order on ({0, 1}∗)ω, the order <colex,2 is only a partial order. How-
ever, <colex,2 is a total order on the set of all words v ∈ ({0, 1}∗)ω such that [v]j is eventually 0.

Let u = u1u2 · · · , v = v1v2 · · · ∈ ({0, 1}∗)ω. Let k be minimal such that [uk]2 ̸= [vk]2. We
write u <alex,2 v if either k is even and [uk]2 < [vk]2, or k is odd and [uk]2 > [vk]2; this is
the alternating lexicographic order on ({0, 1}∗)ω.

12:8 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

2.3. Ostrowski representations. We now introduce Ostrowski representations based on
the continued fraction expansions of real numbers. We refer the reader to Allouche and
Shallit [AS03] and Rockett and Sz¨usz [RS92] for more details. A finite continued fraction
expansion [a0; a1, . . . , ak] is an expression of the form

a0 + 1

a1 + 1

a2 + 1

. . . + 1
ak
For a real number α, we say [a0; a1, . . . , ak, . . . ] is a continued fraction expansion of
α if α = limk→∞[a0; a1, . . . , ak] and a0 ∈ Z, ai ∈ N>0 for i > 0. In this situation, we write
α = [a0; a1, . . . ]. Every irrational number has precisely one continued fraction expansion,
so we will usually refer to the continued fraction expansion of a number. We recall the
following well-known fact about continued fractions.

Fact 2.5. Let α = [a0; a1, . . . ], α′ = [a′
0; a′
1, . . . ] ∈ R be irrational. Let k ∈ N be minimal
such that ak ̸= a′
k. Then α < α′ if and only if
• k is even and ak < a′
k, or
• k is odd and ak > a′
k.

For the rest of this subsection, fix a positive irrational real number α ∈ (0, 1) and let
[a0; a1, a2, . . . ] be the continued fraction expansion of α.
Let k ≥ 1. A pair (pk, qk) is the k-th convergent of α if pk ∈ N, qk ∈ Z, gcd(pk, qk) = 1
and pk
qk = [a0; a1, . . . , ak].

Set p−1 := 1, q−1 := 0 and p0 := a0, q0 := 1. While formally a pair of integers, in practice we
will think of a convergent as the quotient pk
qk . The convergents satisfy the following equations
for n ≥ 1:
 pn = anpn−1 + pn−2, qn = anqn−1 + qn−2.

We now recall a numeration system due to Ostrowski [Ost22].

Fact 2.6 [RS92, Ch. II-§4]. Let X ∈ N. Then X can be written uniquely as

X =
 N∑

n=0 bn+1qn, (2.1)

where 0 ≤ b1 < a1, 0 ≤ bn+1 ≤ an+1 and bn = 0 whenever bn+1 = an+1.

For X ∈ N satisfying (2.1) we write

X = [b1b2 · · · bN bN +1]α

and call the word b1b2 · · · bN +1 an α-Ostrowski representation of X. This representation
is unique up to trailing zeros. Let X, Y ∈ N and let b1b2 · · · bN +1 and c1c2 · · · cN +1 be
α-Ostrowski representations of X and Y respectively. Since Ostrowski representations are
obtained by a greedy algorithm, one can see easily that X < Y if and only if b1b2 · · · bN +1 is
co-lexicographically smaller than c1c2 · · · cN +1.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:9

We now introduce a similar way to represent real numbers, also due to Ostrowski [Ost22].
The k-th difference βk of α is defined as βk := qkα − pk. We use the following facts about
k-th differences: for all n ∈ N
(1) βn > 0 if and only if n is even,
(2) β0 > −β1 > β2 > −β3 > β4 > . . . , and
(3) −βn = an+2βn+1 + an+4βn+3 + an+6βn+5 + . . . .
Let Iα be the interval [⌊α⌋ − α, 1 + ⌊α⌋ − α).

Fact 2.7 (cf. [RS92, Ch. II.6 Theorem 1]). Let x ∈ Iα. Then x can be written uniquely as

∞∑

k=0 bk+1βk, (2.2)

where bk ∈ Z with 0 ≤ bk ≤ ak, and bk−1 = 0 whenever bk = ak,(in particular, b1 ̸= a1), and
bk ̸= ak for infinitely many odd k.

For x ∈ Iα satisfying (2.2) we write
 x = [b1b2 · · · ]α

and call the infinite word b1b2 · · · the α-Ostrowski representation of x. This is closely
connected to the integer Ostrowski representation. Note that for every real number there a
unique element of Iα such that that their difference is an integer. We define fα : R → Iα to
be the function that maps x to x − u, where u is the unique integer such that x − u ∈ Iα.

Fact 2.8 [Hie16, Lemma 3.4]. Let X ∈ N be such that ∑N
k=0 bk+1qk is the α-Ostrowski
representation of X. Then
 fα(αX) =
 ∞∑

k=0 bk+1βk

is the α-Ostrowski representation of fα(αX), where bk+1 = 0 for k > N .

Since βk > 0 if and only if k is even, the order of two elements in Iα can be determined by
the Ostrowski representation as follows.

Fact 2.9 [Hie16, Fact 2.13]. Let x, y ∈ Iα with x ̸= y and let [b1b2 · · · ]α and [c1c2 · · · ]α be
the α-Ostrowski representations of x and y. Let k ∈ N be minimal such that bk ̸= ck. Then
x < y if and only if
(i) bk+1 < ck+1 if k is even;
(ii) bk+1 > ck+1 if k is odd.
 3. #-binary encoding

In this section, we introduce #-binary coding. A similar encoding has been used in Hodgson
[Hod82]. Fix the alphabet Σ# := {0, 1, #}. Let H∞ denote the set of all infinite Σ#-words
in which # appears infinitely many times. Clearly H∞ is ω-regular.

Let C# : ({0, 1}∗)ω → H∞ map an infinite word b = b1b2b3 · · · over {0, 1}∗ to the infinite
Σ#-word #b1#b2#b3# · · · .

12:10 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

We note that the map C# is a bijection.

Let u = u1u2u3 · · · , v = v1v2v3 · · · ∈ Σω
#. We say u and v are aligned if for all i ∈ N

ui = # if and only if vi = #.

This defines an ω-regular equivalence relation on Σω
#. We denote this equivalence relation
by ∼#. We say (w1, . . . , wn) ∈ (Σω
#)n is aligned if

w1 ∼# w2 ∼# · · · ∼# wn.

We say a subset X ⊆ (Σω
#)n is aligned if every w ∈ X is aligned.

The following fact follows easily.

Fact 3.1. The following sets are ω-regular:
• {(u, v) ∈ H 2
∞ : u ∼# v and C−1
# (u) <lex,2 C−1
# (v)},
• {(u, v) ∈ H 2
∞ : u ∼# v and C−1
# (u) <colex,2 C−1
# (v)},
• {(u, v) ∈ H 2
∞ : u ∼# v and C−1
# (u) <alex,2 C−1
# (v)}.

3.1. #-binary coding of continued fractions. We now code the continued fraction
expansions of real numbers as infinite Σ#-words.

Definition 3.2. Let α ∈ (0, 1) be irrational such that [0; a1, a2, . . . ] is the continued fraction
expansion of α. Let u = u1u2 · · · ∈ ({0, 1}∗)ω such that ui ∈ {0, 1}∗ is a binary representation
of ai for each i ∈ Z≥0. We say that C#(u) is a #-binary coding of the continued fraction
of α.

Let R be the set of elements of Σω
# of the form (#(0|1)∗1(0|1)∗)ω. Obviously, R is ω-regular.

Lemma 3.3. Let w ∈ R. Then there is a unique irrational number α ∈ [0, 1] such that w is
a #-binary coding of the continued fraction of α.

Proof. By the definition of R, there is w1w2 · · · ∈ ((0|1)∗1(0|1)∗)ω such that

w = #w1#w2# · · · .

Since wi ∈ (0|1)∗1(0|1)∗, we have that wi is a {0, 1}-word containing at least one 1. Let ai
be the natural number that ai = [wi]2. Because wi contains a 1, we must have ai ̸= 0. Thus
w is a #-binary coding of the infinite continued fraction of the irrational α = [0; a1, a2, . . . ].
Uniqueness follows directly from the fact that both binary expansions and continued fraction
expansions only represent one number.

For w ∈ R, let α(w) be the real number given by Lemma 3.3. When v = (v1, . . . , vn) ∈ Rn,
we write α(v) for (α(v1), . . . , α(vn)).

Even though continued fractions are unique, their #-binary codings are not, because binary
representations can have trailing zeroes. This ambiguity is required in order to properly
recognize relationships between multiple numbers, as one of the numbers involved may
require more bits in a coefficient than the other(s). Occasionally we need to ensure that all
possible representations of a given tuple of numbers are contained in a set. For this reason,
we introduce the zero-closure of subsets of Rn.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:11

Definition 3.4. Let X ⊆ Rn be aligned. The zero-closure of X is

{u ∈ Rn : u is aligned ∧ ∃v ∈ X α(u) = α(v)}.

Lemma 3.5. Let X ⊆ Rn be ω-regular and aligned. Then the zero-closure of X is also
ω-regular.

Proof. Let A be a B¨uchi automaton recognizing X. We use Q to denote the set of states of
A. We create a new automaton A′ that recognizes the zero-closure of X, as follows:

(Step 1) Start with the automata A.
(Step 2) For each transition on the n-tuple (#, . . . , #) from a state p to a state q, we add
a new state µ(p, q) that loops to itself on the n-tuple (0, . . . , 0) and transitions
to state q on (#, . . . , #). We add a transition from p to µ(p, q) on (0, . . . , 0).
(Step 3) For every pair p, q of states of A for which p has a run to q on a word of the
form (0, . . . , 0)m(#, . . . , #) for some m, we add a transition from state p to
a new state ν(p, q) on (#, . . . , #), and for every transition out of state q, we
create a copy of the transition that starts at state ν(p, q) instead. If any original
run from state p to state q passes through a final state, we make ν(p, q) a final
state.
(Step 4) Denote the resulting automaton by A′ and its set of states by Q′.

We now show that L(A′) is the zero-closure of X. We first show that the zero-closure is
contained in L(A′). Let v ∈ X and w ∈ Rn be such that w is aligned and α(v) = α(w).
Since both v and w are aligned, there are b = b1b2 · · · , c = c1c2 · · · ∈ (({0, 1}n)∗)ω such
that C#(b) = v and C#(c) = w. Since α(v) = α(w), we have that [bi]2 = [ci]2 for i ∈ N.
Therefore, for each i ∈ N, the words bi and ci only differ by trailing (tuples of) zeroes. Let
s = s1s2 · · · ∈ Qω be an accepting run of v on A. We now transfer this run into an accepting
run s′ = s′
1s′
2 · · · of w on A′. For i ∈ N, let y(i) be the position of the i-th (#, . . . , #) in v
and let z(i) be the position of the i-th (#, . . . , #) in w. For each i ∈ N, we define a sequence
s′
z(i)+1 · · · s′
z(i+1) of states of A′ as follows:

(1) If |ci| = |bi|, then ci = bi. We set

s′
z(i)+1 · · · s′
z(i+1) := sy(i)+1 · · · sy(i+1).

(2) If |ci| > |bi|, then ci = bi(0, . . . , 0)|ci|−|bi|. We set

s
′
z(i)+1 · · · s′
z(i+1)
:= sy(i)+1 · · · sy(i+1)−1 µ(sy(i+1)−1, sy(i+1)) · · · µ(sy(i+1)−1, sy(i+1)
︸ ︷︷ ︸
(|ci|−|bi|)-times
 sy(i+1).

Thus the new run follows the old run up to sy(i+1)−1 and then transitions to one of the
newly added states in the Step 2. It loops on (0, . . . , 0) for |ci| − |bi| − 1-times before
moving to sy(i+1).
(3) If |ci| < |bi|, then bi = ci(0, . . . , 0)|bi|−|ci|. We set

s
′
z(i)+1 · · · s′
z(i+1) := sy(i)+1 · · · sy(i)+|ci|ν(sy(i)+|ci|, sy(i+1)).

The new run utilizes one of the newly added (#, . . . , #) transitions and corresponding
states added in Step 3.

12:12 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

The reader can now easily check that s′ is an accepting run of w on A′.

We now show that L(A′) is contained in the zero-closure of X. We prove that the only
accepting runs on A′ are based on accepting runs on A with trailing zeroes either added or
removed. Let w = w1w2 · · · ∈ L(A′), and let s′ = s′
1s′
2 · · · ∈ Q′ω be an accepting run of w on
A′. We construct v ∈ X and a run s = s1s2 · · · ∈ Qω of w2 on A such that α(v) = α(w) and
s is an accepting run of v. We start by setting v := w1w2 · · · and s := s′
1s′
2 · · · . For each
i ∈ N, we replace wi in v and s′
i in s as follows:
(1) If s′
i ∈ Q, then we make no changes to s′
i and wi.
(2) If s′
i = µ(p, q) for some p, q ∈ Q, we delete the s′
i in s and delete wi in v.
(3) If si = ν(p, q) for some p, q ∈ Q, then we replace
(a) s′
i by a run t = t1 · · · tn+1 of (0, . . . , 0)n(#, ..., #) from p to q, and
(b) wi by (0, . . . , 0)n(#, ..., #).
If ν(p, q) is a final state of A′, we choose t such that it passed through a final state of A.
It is clear that the resulting s is in Qω. The reader can check s is an accepting run of v on
A and that α(v) = α(w). Thus w is in the zero-closure of X.

Lemma 3.6. The set

{(w1, w2) ∈ R2 : w1 ∼# w2 and α(w1) < α(w2)}

is ω-regular.

Proof. Let w1, w2 ∈ R be such that w1 ∼# w2. By Fact 2.5 we have that α(w1) < α(w2) if
only C−1
# (w1) <alex,2 C−1
# (w2). Thus ω-regularity follows from Fact 3.1.

Lemma 3.7. Let a ∈ [0, 1) be a quadratic irrational. Then

{w ∈ R : α(w) = a}

is ω-regular.

Proof. The continued fraction expansion of a is eventually periodic (see for example [HW79,
Theorem 177]). Thus there is an eventually periodic u ∈ ({0, 1}∗)ω such that C#(u) is a
#-binary coding of the continued fraction of a. The singleton set containing an eventually
periodic string is ω-regular. It remains to expand this set to contain all representations via
Lemma 3.5.

Lemma 3.8. The set {w ∈ R : α(w) < 1
2 } is ω-regular.

Proof. Let α(w) = [0; a1, a2, . . . ]. It is easy to see that α(w) < 1
2 if and only if a1 > 1. Thus
we need only check that a1 ̸= 1. The set of w ∈ R for which this true is just R \ Y , where
Y ⊆ Σω
# is given by the regular expression #10∗(#(0 ∪ 1)∗)ω.

3.2. #-Ostrowski-representations. We now extend the #-binary coding to Ostrowski
representations.

Definition 3.9. Let v, w ∈ (Σ#)ω, let x = x1x2x3 · · · ∈ Nω and let b = b1b2b3 · · · ∈ ({0, 1}∗)ω

be such that w = C#(b) and [bi]2 = xi for each i.
• For N ∈ N, we say that w is a #-v-Ostrowski representation of N if v and w are
aligned and x is an α(v)-Ostrowski representation of N .

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:13

• For c ∈ Iα(v), we say that w is a #-v-Ostrowski representation of c if v and w are
aligned and x is an α(v)-Ostrowski representation of c.
We let Av denote the set of all words w ∈ Σω
# such that w is a #-v-Ostrowski representation
of some c ∈ Iα(v), and similarly, by Afin
v the set of all words w ∈ Σω
# such that w is a
#-v-Ostrowski representation of some N ∈ N.

Lemma 3.10. The sets

Afin := {(v, w) : v ∈ R, w ∈ Afin
v }, and A := {(v, w) : v ∈ R, w ∈ Av}.

are ω-regular. Moreover, Afin ⊆ A.

Proof. The statement that Afin ⊆ A, follows immediately from the definitions of Afin and A
and Fact 2.8. It is left to establish the ω-regularity of the two sets.

For Afin: Let B ⊇ Afin be the set of all pairs (v, w) such that v ∈ R and v ∼# w. Note
that B is ω-regular. Let (v, w) ∈ B. Since v and w have infinitely many # symbols and
are aligned, there are unique a = a1a2 · · · , b = b1b2 · · · ∈ ({0, 1}∗)ω such that C#(a) = v,
C#(b) = w and |ai| = |bi| for each i ∈ N. Then by Fact 2.6, (v, w) ∈ Afin if and only if
(a) b has finitely many 1 symbols;
(b) b1 <colex a1;
(c) bi ≤colex ai for all i > 1;
(d) if bi = ai, then bi−1 = 0.
It is easy to check that all four conditions are ω-regular.

For A: As above, let (v, w) ∈ B. Since v and w have infinitely many # symbols and
are aligned, there are unique a = a1a2 · · · , b = b1b2 · · · ∈ ({0, 1}∗)ω such that C#(a) = v,
C#(b) = w and |ai| = |bi| for each i ∈ N. Then by Fact 2.7, (v, w) ∈ A if and only if
(e) b1 <colex a1;
(f) bi ≤colex ai for all i > 1;
(g) if bi = ai, then bi−1 = 0;
(h) bi ̸= ai for infinitely many odd i.
Again, it is easy to see that all four conditions are ω-regular.

Definition 3.11. Let v ∈ R. We define Zv : Afin
v → N to be the function that maps w to
the natural number whose #-v-Ostrowski representation is w.
Similarly, we define Ov : Av → Iα(v) to be the function that maps w to the real number
whose #-v-Ostrowski representation is w.

Lemma 3.12. Let v ∈ R. Then Zv : Afin
v → N and Ov : Av → Iα(v) are bijective.

Proof. We first consider injectivity. By Fact 2.6 and Fact 2.7 a number in N or in Iα(v) only
has one α(v)-Ostrowski representation. So we only need to explain why such a representation
will only have one encoding in Afin
v (respectively Av). This follows from the uniqueness
of binary representations up to the length of the representation, and from the fact that
the requirement of having the # symbols aligned with v determines the length of each
binary-encoded coefficient.

For surjectivity we only need to explain why an α(v)-Ostrowski representation can always
be encoded into a string in Afin
v (respectively Av). It suffices to show that the requirement of

12:14 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

having the # symbols aligned with v will never result in needing to fit the binary encoding
of a number into too few symbols, i.e., that it will never result in having to encode a natural
number n in binary in fewer than 1 + ⌊log2 n⌋ symbols. Since the function 1 + ⌊log2 n⌋ is
monotone increasing, we can encode any natural number below n in k symbols if we can
encode n in binary in k symbols. However, by Fact 2.6 and Fact 2.7, the coefficients in an
α(v)-Ostrowski representation never exceed the corresponding coefficients in the continued
fraction for α(v), i.e., bn ≤ an.

Definition 3.13. Let v ∈ R. We write 0v for Z−1
v (0), and 1v for Z−1
v (1).

Lemma 3.14. The relations 0∗ = {(v, 0v) : v ∈ R} and 1∗ = {(v, 1v) : v ∈ R} are
ω-regular.

Proof. Recognizing 0∗ is trivial, as the Ostrowski representations of 0 are of the form 0 · · · 0
for all irrational α. Thus 0∗ is just the relation

{(v, w) : v ∈ R, w is v with all 1 bits replaced by 0 bits}.

This is clearly ω-regular.

We now consider 1∗. Let α = [0; a1, a2, . . . ] be an irrational number. If a1 > 1, the
α-Ostrowski representations of 1 are of the form 10 · · · 0. If a1 = 1, the α-Ostrowski
representations of 1 are of the form 010 · · · 0. Thus, in order to recognize 1∗, we only need
to be able to recognize if a number in binary representation is 0, 1, or greater than 1. Of
course, this is easily done on a B¨uchi automaton.

Lemma 3.15. Let s ∈ Afin
v . Then α(v)Zv(s) − Ov(s) ∈ Z and

Ov(1v) =
 {
α(v) if α(v) < 1
2 ;
α(v) − 1 otherwise.

Proof. By Fact 2.8, Ov(s) = fα(v)(α(v)Zv(s)). Thus

α(v)Zv(s) − Ov(s) = α(v)Zv(s) − fα(v)(α(v)Zv(s)),

which is an integer by the definition of f . By the definition of 1v and by Fact 2.8, we know
Ov(1v) = fα(v)(α(v)) is the unique element of Iα(v) that differs from α(v) by an integer. If
0 < α(v) < 1
2 , then
 −α(v) < α(v) < 1 − α(v).

Thus in this case, α(v) ∈ Iα(v) and Ov(1v) = α(v). When 1
2 < α(v) < 1, then

−α(v) < α(v) − 1 < 1 − α(v).

Therefore α(v) − 1 ∈ Iα(v) and Ov(1v) = α(v) − 1.

Lemma 3.16. The sets

≺
fin := {(v, s, t) ∈ Σ3
# : s, t ∈ Afin
v ∧ Zv(s) < Zv(t)},

≺ := {(v, s, t) ∈ Σ3
# : s, t ∈ Av ∧ Ov(s) < Ov(t)}

are ω-regular.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:15

Proof. For ≺fin, first recall that for X, Y ∈ N and α irrational, we have X < Y if and only
if the α-Ostrowski representation of X is co-lexicographically smaller than the α-Ostrowski
representation of Y . Therefore, we need only recognize co-lexicographic ordering on the list
of coefficients, with each coefficient ordered according to binary. This follows immediately
from Fact 3.1.

For ≺, note that by Fact 2.9 the usual order on real numbers corresponds to the alternating
lexicographic ordering on real Ostrowski representations. Therefore, we need only recognize
the alternating lexicographic ordering on the list of coefficients, with each coefficient ordered
according to binary. This follows immediately from Fact 3.1.

We consider Rn as a topological space using the usual order topology. For X ⊆ Rn, we
denote its topological closure by X. This is of course defined using the product of order
topologies; i.e. x ∈ X iff every open box containing x also contains an element of X.

Corollary 3.17. Let W ⊆ (Σ
n+1
# )∗ ω-regular be such that

W ⊆ {(v, s1, . . . , sn) ∈ (Σn+1
# )
∗ : s1, . . . , sn ∈ Av}.

Then the following set is also ω-regular:

W := {(v, s1, . . . , sn) ∈ (Σ
n+1
# )
∗ : s1, . . . , sn ∈ Av ∧ (Ov(s1), . . . , Ov(sn)) ∈ O(Wv)}.

Proof. Let (v, s1, . . . , sn) ∈ (Σn+1
# )∗ be such that s1, . . . , sn ∈ Av. Let Xi = Ov(si). By the

definition of the topological closure, we have that (X1, . . . , Xn) ∈ O(Wv) if and only if for all
Y1, . . . Yn, Z1, . . . , Zn ∈ R with Yi < Xi < Zi for i = 1, . . . , n there are X ′ = (X ′
1, . . . , X ′
n) ∈
O(Wv) such that Yi < X ′
i < Zi for i = 1, . . . , n. Thus by Lemma 3.16, (v, s1, . . . , sn) ∈ W if
and only if for all t1, . . . tn, u1, . . . , un ∈ Av with ti ≺ si ≺ ui, there are s′ = (s′
1, . . . , s′
n) ∈ Wv
such that ti ≺ s′
i ≺ ui for i = 1, . . . , n. The latter condition is ω-regular by Fact 2.1.

4. Recognizing addition in Ostrowski numeration systems

The key to the rest of this paper is a general automaton for recognizing addition of Ostrowski
representations uniformly. We will prove the following:

Theorem 4.1. The set

⊕
fin := {(v, s1, s2, s3) : s1, s2, s3 ∈ A
fin
v ∧ Zv(s1) + Zv(s2) = Zv(s3)}

is ω-regular.

In order to prove this theorem, we will introduce a method to generate more complex
automata for strings in H∞, from general B¨uchi automata. For the reasons mentioned when
general B¨uchi automata were introduced in Section 2, we will not use these automata directly.
Instead, we will use the #-binary coding to convert the computation to a more familiar
setting. Similarly arguments have been made before, in particular in [Hod82, Section 4].

Definition 4.2. Let w = w1w2 · · · ∈ (Nn)ω. A #-binary coding of w is a word u =
u1u2 · · · ∈ (Σn
#)ω such that
 C#(u1,iu2,i · · · ) = w1,iw2,i · · · ,

12:16 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

where uj,i and wj,i denote the i-th component of j-th character of u and w.
Let X ⊆ (Nn)ω. The language of #-binary coding of X is the set of all #-binary codings
of its elements.

Lemma 4.3. Let A = (Q, Nn, ∆, I, F ) be a general B¨uchi automaton over Nn, possibly with
infinitely many transitions, such that for every s1, s2 ∈ Q the set

{u ∈ {0, 1}
∗ : (s1, [u]2, s2) ∈ ∆}

is regular. Then the #-binary coding of the language accepted by A is ω-regular.

Proof. We construct from A a new B¨uchi automaton A′ over (Σ#)n. It is constructed via
the following procedure:
(1) Copy the states (without their transitions) from A to A′. Any final states in A are to
remain final in A′.
(2) Add an initial state qstart, and endow it with transitions to every state that was an
initial state in A on the character (#, . . . , #). These states are no longer initial in A′,
so that qstart is the only initial state.
(3) For every pair s1, s2 ∈ Q:
(a) Let B be a finite automaton recognizing

{u ∈ {0, 1}
∗ : (s1, [u]2, s2) ∈ ∆}.

Add the states and transitions of B to A′.
(b) For every initial state t in B, whenever t transitions to t′ on a character, add a
transition from s1 to t′ on the same character. Make t no longer an initial state in
A′.
(c) For every final state t in B, add a transition from t to s2 on (#, . . . , #). Make t no
longer a final state in A′.
(d) If the empty word ϵ was accepted by B, then add a transition from q to r on
(#, . . . , #).
One can check that the language accepted by A′ is the #-binary coding of the language
accepted by A. Indeed, if a word is accepted by A′, it must begin with #n and be followed
by a sequence of binary codings that correspond to transitions in A, delimited by #, and
visiting final states of A infinitely often.

We will illustrate with an example. Figure 1 demonstrates the process of applying Lemma
4.3 to a simple automaton that accepts any infinite string of natural numbers containing at
least one odd number.

We may now give the full proof of Theorem 4.1.

Proof of Theorem 4.1. In [BSS21, Section 2] the authors generate a general finite au-
tomaton A0 over the alphabet N4 such that a finite word (d1, x1, y1, z1)(d2, x2, y2, z2) · · ·
(dm, xm, ym, zm) ∈ (N4)∗ is accepted by A0 if and only if there are dm+1, . . . ∈ N and
x, y, z ∈ N such that for α = [0; d1, d2, . . . ] we have

x = [x1x2 · · · xm]α
y = [y1y2 · · · ym]α
z = [z1z2 · · · zm]α
z = x + y.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:17

q0 q1

even
 odd
 any

(a)

qeven,0 qeven,1 qodd,0 qodd,1 qany,0
0
 0,1
 1
 0,1 0,1

(b)

qstart q0

qeven,0 qeven,1
 qodd,0 qodd,1 q1

qany,0

#
 0
 1

0
 0,1

#
 1
 0,1
 #
 0,1
 #

0,1
 #

(c)

Figure 1: The procedure of Lemma 4.3. (a) The original automaton, with transitions for
“any even number,” “any odd number,” and “any number.” (b) The finite automata
recognizing these sets in binary encoding. (c) The combined automaton produced
by Lemma 4.3.

12:18 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

Let A be the general B¨uchi automaton with the same underlying quintuple as A0. It follows
immediately that if (d1, x1, y1, z1)(d2, x2, y2, z2) · · · ∈ (N4)ω is accepted by A if and only if
there is an infinite subset U ⊆ N such that for all u ∈ N

[x1x2 · · · xu]α + [y1y2 · · · yu]α = [z1z2 · · · zu]α

Each transition in A corresponds to a linear equation with constant integer coefficients. As
an example, one of the transitions in Figure 3 of [BSS21] is given as “−di + 1,” meaning that
it represents all cases where, letting vi, s1i, s2i, s3i be the ith letter of v, s1, s2, s3 respectively,
we have s3i − s1i − s2i = −vi + 1. Note that the binary representation of the graph of
addition and subtraction, as well as of the constant 1, are regular. Thus A satisfies the
conditions of Lemma 4.3. Let X ⊆ (Σ4
#)ω be the #-binary coding of the language accepted
by A. By Lemma 4.3, we know that X is ω-regular. Observe that

⊕
fin = {(v, s1, s2, s3) ∈ X : s1, s2, s3 ∈ Afin
v }

and hence ω-regular.

The automaton constructed above has 82 states
5. Using our software Pecan, we can formally
check that this automaton recognizes the set in Theorem 4.1. Following a strategy already
used in Mousavi, Schaeffer, and Shallit [MSS16, Remark 2.1] we check that our adder satisfies
the standard inductive definition of addition on the natural numbers; that is, for all x, y ∈ N

0 + y = y

s(x) + y = s(x + y)

where x, y ∈ N and s(x) denotes the successor of x in N. The successor function on N can
be defined using only < as follows:

s(x) = y if and only if (x < y) ∧ (∀z (z ≤ x) ∨ (z ≥ y)).

Thus in Pecan we define bco_succ(a,x,y) as

bco_succ (a ,x , y ) : = bco_valid (a , x ) ∧ bco_valid (a , y )
∧ bco_leq (x , y ) ∧ ¬bco_eq (x , y )
∧ ∀z . if bco_valid (a , z ) then ( bco_leq (z , x ) ∨ bco_leq (y , z ))

where
• bco_eq recognizes {(x, y) : x = y},
• bco_leq recognizes {(x, y) : x ≤colex y}, and
• bco_valid recognizes Afin.
We now confirm that our adder satisfies the above equations using the following Pecan
code:

Let x ,y , z be ostrowski ( a ) .
Theorem ( " Addition base case (0 + y = y ). " , {
∀a . ∀x ,y , z . if bco_zero ( x )
then ( bco_adder (a ,x ,y , z ) iff bco_eq (y , z )) } ) .
Theorem ( " Addition inductive case ( s ( x ) + y = s ( x + y )). " , {
∀a . ∀x ,y ,z ,u , v . if ( bco_succ (a ,u , x ) ∧ bco_succ (a ,v , z ))
then ( bco_adder (a ,x ,y , z ) iff bco_adder (a ,u ,y , v )) } ) .

5Schmitthenner [Sch23] constructs an B¨uchi automaton with just 24 states accepting the same language.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:19

In the above code

• bco_adder recognizes ⊕fin,
• bco_zero recognizes 0∗, and
• bco_succ recognizes {(v, x, y) : x, y ∈ Afin
v , Zv(x) + 1 = Zv(y)}.
Pecan confirms both statements are true. This proves Theorem 4.1 modulo correctness
of Pecan and the correctness of the implementations of the automata for bco_eq, bco_leq,
bco_valid and bco_zero. For more details about Pecan, see Section 7.

We need the following well-known consequence of K¨onig’s Lemma (compare the proof of
[BGS23, Lemma 4.3]).

Fact 4.4. Let A be a B¨uchi automaton over Σ with all states accepting, let w ∈ Σω, and let
(un)n∈N be a sequence of words in Σω such that un|n = w|n for all n ∈ N. If un ∈ L(A) for
every n ∈ N, then w ∈ L(A).

Using this result, we can extend the automaton in Theorem 4.1 to an automaton for addition
modulo 1 on Iα.

Lemma 4.5. The set

⊕ := {(v, s1, s2, s3) : s1, s2, s3 ∈ Av ∧ Ov(s1) + Ov(s2) ≡ Ov(s3) (mod 1)}

is ω-regular. Moreover, ⊕fin ⊆ ⊕.

Proof. First, let v, s1, s2, s3 be such that s1, s2, s3 ∈ Afin
v . We claim that on this domain,
(s1, s2, s3) ∈ ⊕v if and only if (s1, s2, s3) ∈ ⊕fin
v . By Fact 2.8 we know that for all s ∈ Afin
v

α(v)Zv(s) − Ov(s) ≡ 0 (mod 1). (4.1)

Let (s1, s2, s3) ∈ ⊕fin
v . Then by (4.1)

Ov(s3) ≡ α(v)Zv(s3) (mod 1)

= α(v)Zv(s1) + α(v)Zv(s2)

≡ Ov(s1) + Ov(s2) (mod 1).

Thus (s1, s2, s3) ∈ ⊕v.

Let Bfin be a B¨uchi automaton recognizing ⊕fin. Assume that Bfin is trim. Let B′ be the
automaton Bfin, but with all states made accepting. Let S be the language accepted by B′.
We will show that Sv ∩ A3
v = ⊕v. Towards that goal, let (v, s1, s2, s3) ∈ (Σω
#)4 be such that
(s1, s2, s3) ∈ A3
v. It is left to prove that (s1, s2, s3) ∈ ⊕v if and if (s1, s2, s3) ∈ Sv.

Suppose first that (s1, s2, s3) ∈ ⊕v. Then

Ov(s3) ≡ Ov(s1) + Ov(s2) (mod 1).

The reader can check using properties of Ostrowski representations that there is a sequence
(sm,1, sm,2, sm,3)m∈N of elements of (Afin
v )3 such that

(1) Ov(sm,3) ≡ Ov(sm,1) + Ov(sm,2) (mod 1).
(2) sm,i|m = si|m for i ∈ {1, 2, 3}; i.e., the first m letters of sm,i agree with the first m letters
of si for i ∈ {1, 2, 3}.

12:20 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

By (Afin
v )3 ∩ ⊕v = ⊕fin
v and (1), we know that (v, sm,1, sm,2, sm,3) is accepted by Bfin. By
Fact 4.4 and (2), we deduce that B′ accepts (v, s1, s2, s3). Thus (s1, s2, s3) ∈ Sv.

Suppose now that (s1, s2, s3) ∈ Sv. Then (v, s1, s2, s3) is accepted by B′. For m ∈ N and
i ∈ {1, 2, 3}, let wm,i ∈ Σ∗
# be such that wm,i is si up through the (m + 1)-st occurrence
of #. Thus wm,i represents the first m-th Ostrowski coefficients of Ov(si). Since Bfin is
trim, there exist infinite extensions sm,1, sm,2, sm,3 ∈ Σω
# of wm,1, wm,2, wm,3 such that Bfin

accepts (v, sm,1, sm,2, sm,3). We now set

(xm, ym, zm) := (Ov(sm,1), Ov(sm,2), Ov(sm,3)), (x, y, z) := Ov(s1, s2, s3).

It follows from Fact 2.9 that
 lim
m→∞(xm, ym, zm) = (x, y, z).

Because xm+ym ≡ zm (mod 1) for every m ∈ N (by definition of Bfin and (Afin
v )3∩⊕v = ⊕fin
v ),
we have x + y ≡ z (mod 1). Hence (s1, s2, s3) ∈ ⊕v.

5. The uniform ω-regularity of Rα

In this section, we turn to the question of the decidability of the logical first-order theory
of Rα. Recall that Rα := (R, <, +, Z, αZ) for α ∈ R. The main result of this section is the
following:

Theorem 5.1. There is a uniform family of ω-regular structures (Dv)v∈R such that Dv ≃
Rα(v) for each v ∈ R.

Theorem 5.1 then hinges on the following lemma.

Lemma 5.2. There is a uniform family of ω-regular structures (Ca)a∈R such that for each
a ∈ R Ca ≃ ([−α(a), ∞), <, +, N, α(a)N).

Proof of Theorem 5.1. Let (Ca)a∈R be an uniform family of ω-regular structures as given by
Lemma 5.2. Within Ca, define the set L = {x ∈ [−α(a), ∞) : x ≥ 0}, where 0 is the <-least
element of N. This is an ordered commutative monoid. Let L′ be its Grothendieck group,
and let +′, <′ be the induced abelian group operation and ordering. There is a canonical
inclusion map ι : L ↪→ L′. Let Z′ = ι(N) ∪ −ι(N) and A′ = ι(α(a)N) ∪ −ι(α(a)N). Observe
that (L′, <′, +′, N ′, A′) is an isomorphic copy of Rα(a), defined in Ca in a manner uniform
in a. So let Da be this structure and conclude that (Da)a is a uniform family of ω-regular
structures.

The proof of Lemma 5.2 itself is a uniform version of the argument given in [Hie16] that also
fixes some minor errors of the original proof. By Lemma 3.16 and Theorem 4.1, we already
know that Zv : (Afin
v , ≺
fin
v , ⊕
fin
v ) → (N, <, +)
is an isomorphism for every v ∈ R. As our eventual goal also requires us to define the set
αN, it turns out to be much more natural to instead use the isomorphism

α(v)Zv : (Afin
v , ≺
fin
v , ⊕
fin
v ) → (α(v)N, <, +)

and recover N (and further Z). We do so by following (and correcting) the argument in
[Hie16].

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:21

Lemma 5.3. Let v ∈ R, and let t1, t2, t3 ∈ Av be such that t1 ⊕v t2 = t3. Then

Ov(t1) + Ov(t2) =
 




Ov(t3) + 1 if 0v ≺v t1 and t3 ≺v t2;
Ov(t3) − 1 if t1 ≺v 0v and t2 ≺v t3;
Ov(t3) otherwise.

Proof. For ease of notation, let α = α(v), and set xi = Ov(ti) for i = 1, 2, 3. By definition
of ⊕v, we have that x1, x2, x3 ∈ Iα(v) with x1 + x2 ≡ x3 (mod 1). Note that ti ≺v tj if and
only if xi < xj.

We first consider the case that 0 < x1 and x3 < x2. Thus x1 + x2 > 1 − α. Note that

−α = 1 − α − 1 < x1 + x2 − 1 < (1 − α) + (1 − α) − 1 = 1 − 2α < 1 − α.

Thus x1 + x2 − 1 ∈ Iα and x3 = x1 + x2 − 1.

Now assume that x1 < 0 and x2 < x3. Then x1 + x2 < −α, and therefore

1 − α > x1 + x2 + 1 ≥ (−α) + (−α) + 1 = (1 − α) − α > −α.

Thus x1 + x2 + 1 ∈ Iα and hence x3 = x1 + x2 + 1.

Finally consider that 0, x1 are ordered the same way as x2, x3. Since x1 + x2 ≡ x3 (mod 1),
we know that |x1 − 0| and |x3 − x2| differ by an integer k. If k > 0, would imply that
one of these differences is at least 1, which is impossible within the interval Iα. Therefore
x1 − 0 = x3 − x2 and hence x3 = x1 + x2.

For i ∈ N, set iv := 1v ⊕ · · · ⊕ 1v︸ ︷︷ ︸
i times
 .

Lemma 5.4. The set F := {(v, s) ∈ Afin : Zv(s)α(v) < 1} is ω-regular, and for each
(v, s) ∈ F
 Ov(s) =
 {
α(v)Zv(s) if (α(v) + 1)Zv(s) < 1;
α(v)Zv(s) − 1 otherwise.

Proof. By Lemma 3.8, we can first consider the case that α(v) > 1
2 . In this situation, Fv is
just the set {0v, 1v}, and hence obviously ω-regular.

Now assume that α(v) < 1
2 . Let w be the ≺fin
v -minimal element of Afin
v with w ≺v 0v. We
will show that Fv = {s ∈ Afin
v : s ⪯
fin
v w}.

Then ω-regularity of F follows then immediately.

Let n ∈ N be maximal such that nα(v) < 1. It is enough to show that Zv(w) = n. By Lemma
3.15, Ov(1v) = α(v). Hence 1α(v), 2α(v), . . . , (n − 1)α(v) ∈ Iα(v), but nα(v) > 1 − α(v).
Then for i = 1, . . . , n − 1

Ov(iv) = iα(v), Ov(nv) = nα(v) − 1 < 0.

So iv ⪰ 0v for i = 1, . . . , n, but nv ≺ 0v. Thus nv = w and Zv(w) = n.

12:22 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

Name Definition
A {(v, w) : v ∈ R, w is a #-v-Ostrowski representation}
Afin {(v, w) : v ∈ R, w is a #-v-Ostrowski representation and eventually 0}
B {(v, s) ∈ Afin : s ⪯v 0v}
C {(v, s, t) : (v, s) ∈ B ∧ (v, t) ∈ A}

Table 1: Definitions of sets used in the proof

Lemma 5.5. Let v ∈ R and t ∈ Afin
v . Then there is an s ∈ Fv and t′ ∈ Afin
v such that t′ ⪯v 0
and t = t′ ⊕v s. In particular,

A
fin
v = {t ∈ Afin
v : t ⪯v 0v} ⊕v Fv.

Proof. Let n ∈ N be maximal such that nα(v) < 1. Let t ∈ Afin
v . We need to find s ∈ Afin
v
and u ∈ Fv such that t = s⊕fin
v u. We can easily reduce to the case that t ≻ 0v and Zv(t) > n.

Let i ∈ {0, . . . , n} be such that 0 ≥ Ov(t) − iα(v) > −α(v). Then let s ∈ Afin
v be such that
Zv(s) = Zv(t) − i. Note t = s ⊕fin
v iv. Thus we only need to show that s ⪯ 0v.

To see this, observe that by Lemma 5.4

Ov(s) + α(v)i ≡ Ov(s) + Ov(iv) ≡ Ov(t) (mod 1).

Since Ov(t) − iα(v) ∈ Iα(v), we know that Ov(s) = Ov(t) − iα(v) ≤ 0.
Therefore Ov(s) ⪯ 0v.

Proof of Lemma 5.2. Define B ⊆ Afin to be {(v, s) ∈ Afin : s ⪯v 0v}. Clearly, B is
ω-regular. We now define ≺B and ⊕B such that for each v ∈ R, the structure (Bv, ≺B
v , ⊕B
v )
is isomorphic to (N, <, +) under the map gv defined as gv(s) = α(v)Zv(s) − Ov(s).

We define ≺B to be the restriction of ≺fin to B. That is, for (v, s1), (v, s2) ∈ B we have

(v, s1) ≺
B (v, s2) if and only if (v, s1) ≺
fin (v, s2).

It is immediate that ≺B is ω-regular, since both B and ≺fin are ω-regular.

We define ⊕B as follows:

(v, s1) ⊕
B (v, s2) =
 {
(v, s1 ⊕v s2) if s1 ⊕fin
v s2 ⪯v 0v;
(v, s1 ⊕v s2 ⊕v 1v) otherwise.

We now show that gv(s1 ⊕B
v s2) = gv(s1) + gv(s2) for every s1, s2 ∈ Bv.

Let (v, s1), (v, s2) ∈ B. We first consider the case that s1 ⊕v s2 ⪯v 0v. By Lemma 5.3,
Ov(s1 ⊕v s2) = Ov(s1) + Ov(s2). Thus

gv(s1 ⊕
B
v s2) = gv(s1 ⊕v s2)

= α(v)Zv(s1 ⊕v s2) − Ov(s1 ⊕v s2)

= αZv(s1) + αZv(s2) − Ov(s1) − Ov(s2)

= gv(s1) + gv(s2).

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:23

Map Domain Codomain
α R Irr
Ov Av Iα(v)
Zv Af in
v N
gv := α(v)Zv − Ov Bv N
Tv := gv + Ov Cv [−α(v), ∞) ⊆ R

Table 2: A list of the maps and their domains and codomains.

Now suppose that s1 ⊕v s2 ≻v 0v. Since −α(v) ≤ Ov(s1), Ov(s2) ≤ 0, we get that

1 − α(v) > Ov(s1) + Ov(s2) + α(v) ≥ −α(v).

Thus by Lemma 3.15,
 Ov(s1 ⊕v s2 ⊕v 1v) = Ov(s1) + Ov(s2) + α(v).

We obtain

gv(s1 ⊕
B
v s2) = gv(s1 ⊕v s2 ⊕v 1v)

= αZv(s1 ⊕v s2 ⊕v 1v) − Ov(s1 ⊕v s2 ⊕v 1v)

= α(v)(Zv(s1) + Zv(s2)) + α(v) − Ov(s1) − Ov(s2) − α(v)

= gv(s1) + gv(s2).

Since s1 ≺v s2 if and only if Zv(s1) < Zv(s2), we get that gv is an isomorphism between
(Bv, ≺B
v , ⊕B
v ) and (N, <, +).

Let C be defined by
 {(v, s, t) ∈ (Σω
#)
3 : (v, s) ∈ B ∧ (v, t) ∈ A}.

Clearly C is ω-regular. Let Tv : Cv → [−α(v), ∞) ⊆ R map (s, t) ↦→ gv(s) + Ov(t).

Note that Tv is bijective for each v ∈ R, since every real number decomposes uniquely into a
sum n + y, where n ∈ Z and y ∈ Iv.

We define an ordering ≺C
v on Cv lexicographically: (s1, t1) ≺C
v (s2, t2) if either

• s1 ≺B
v s2, or
• s1 = s2 and t1 ≺v t2.

The set {(v, s1, t1, s2, t2) : (s1, t1), (s2, t2) ∈ Cv ∧ (s1, t1) ≺
C
v (s2, t2)}

is ω-regular. We can easily check that (s1, t1) ≺C
v (s2, t2) if and only if Tv(s1, t1) < Tv(s2, t2).

Let 0B be g−1
v (0) and 1B be g−1
v (1). Let ⊖B be the (partial) inverse of ⊕B. We define ⊕C

for (s1, t1), (s2, t2) ∈ C as follows:

(s1, t1) ⊕
C
v (s2, t2) =
 




(s1 ⊕B
v s2 ⊖B 1B, t1 ⊕v t2) if t1 ≺ 0v ∧ t2 ≺v t1 ⊕v t2;
(s1 ⊕B
v s2 ⊕B
v 1B, t1 ⊕v t2) if 0v ≺ t1 ∧ t1 ⊕v t2 ≺v t2;
(s1 ⊕B
v s2, t1 ⊕v t2) otherwise.

12:24 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

(Note that ⊕C is only a partial function, as the case where s1 = s2 = 0B and t1 ≺ 0v ∧ t2 ≺v
t1 ⊕v t2 is outside of the domain of ⊖B.) It is easy to check that ⊕C is ω-regular. It follows
directly from Lemma 5.3 that

Tv((s1, t1) ⊕
C
v (s2, t2)) = Tv((s1, t1)) + Tv((s2, t2)).

Thus for each v ∈ R, the function Tv is an isomorphism between (Cv, ≺C
v , ⊕C
v ) and
([−α(v), ∞), <, +). To finish the proof, it is left to establish the ω-regularity of the following
two sets:
(1) {(v, s, t) ∈ C : Tv(s, t) ∈ N},
(2) {(v, s, t) ∈ C : Tv(s, t) ∈ α(u)N}.

For (1), observe that the set T −1
v (N) is just the set {(s, t) ∈ Cv : t = 0v}.

For (2), consider the following two sets:
• U1 = {(v, s, t) ∈ C : s = t},
• U2 = {(v, 0v, t) ∈ C : t ∈ Fv}.
Let 1C
v be T −1
v (1). Set

U := {(v, (s1, t1) ⊕
c
v (0v, t2)) : (v, s1, t1) ∈ U1, (v, 0v, t2) ∈ U2, t2 ⪰ 0}

∪ {(v, (s1, t1) ⊕
c
v (0v, t2) ⊕ 1C
v ) : (v, s1, t1) ∈ U1, (v, 0v, t2) ∈ U2, t2 ≺ 0}.

The set U is clearly ω-regular, since both U1 and U2 are ω-regular. We now show that
Tv(U ) = α(v)N.

Let (v, s, s) ∈ U1 and (v, 0v, t) ∈ U2. If t ⪰ 0v, then by Lemma 5.4

Tv((s, s) ⊕C (0v, t)) = Tv(s, s) + Tv(0v, t)

= α(v)Zv(s) − Ov(s) + Ov(s) + Ov(t)

= α(v)Zv(s) + α(v)Zv(t) = α(v)Zv(s ⊕v t).

If t ≺ 0v, then by Lemma 5.4

Tv((s, s) ⊕
C
v (0v, t) ⊕
C
v 1C
v ) = Tv(s, s) + Tv(0v, t) + 1

= α(v)Zv(s) − Ov(s) + Ov(s) + Ov(t) + 1

= α(v)Zv(s) + α(v)Zv(t) = α(v)Zv(s ⊕v t).

Thus Tv(U ) ⊆ α(v)N. By Lemma 5.5, Tv(U ) = α(v)N.

6. Decidability results

We are now ready to prove the results listed in the introduction. We first recall some
notation. Let Lm be the signature of the first-order structure (R, <, +, Z), and let Lm,a be
the extension of Lm by a unary predicate. For α ∈ R>0, let Rα denote the Lm,a-structure
(R, <, +, Z, αZ). For each Lm,a-sentence φ, we set

Rφ := {v ∈ R : Rα(v) |= φ}.

Theorem 6.1. Let φ be an Lm,a-sentence. Then Rφ is ω-regular.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:25

Proof. By Theorem 5.1 there is a uniform family of ω-regular structures (Dv)v∈R such that
such that Dv ≃ Rα(v) for each v ∈ R. Then Rφ = {v ∈ R : Dv |= φ}. This set is ω-regular
by Fact 2.3.

Let N = (R; (Rφ)φ, (X)X⊆Rn ω-regular) be the relational structure on R with the relations
Rφ for every L-sentences φ and X ⊆ Rn ω-regular. Because N is an ω-regular structure, we
obtain the following decidability result.

Corollary 6.2. The theory FO(N ) is decidable.

We now proceed towards the proof of Theorem C. Recall that Irr := (0, 1) \ Q.

Definition 6.3. Let X ⊆ Irrn. Let XR be defined by

XR := {(v1, . . . , vn) ∈ Rn : v1 ∼# v2 ∼# · · · ∼# vn ∧ (α(v1), . . . , α(vn)) ∈ X}

We say X is recognizable modulo ∼# if XR is ω-regular.

Lemma 6.4. The collection of sets recognizable modulo ∼# is closed under Boolean opera-
tions and coordinate projections.

Proof. Let X, Y ⊆ Irr be recognizable modulo ∼#. It is clear that (X ∩ Y )R = XR ∩ YR.
Thus X ∩ Y is recognizable modulo ∼#. Let X c be Irr
n \ X, the complement of X. For
ease of notation, set E := {(v1, . . . , vn) ∈ Rn : v1 ∼# v2 ∼# · · · ∼# vn}. Then

(X c)R = {(v1, . . . , vn) ∈ Rn : v1 ∼# v2 ∼# · · · ∼# vn ∧ (α(v1), . . . , α(vn)) /∈ X}

= E ∩ {(v1, . . . , vn) ∈ Rn : (α(v1), . . . , α(vn)) /∈ X}

= E ∩ {(v1, . . . , vn) ∈ Rn : (α(v1), . . . , α(vn)) /∈ X ∨ ¬(v1 ∼# v2 ∼# · · · ∼# vn)}

= E ∩ (Rn \ XR).

This set is ω-regular, and hence X c is recognizable modulo ∼#.

For coordinate projections, it is enough to consider projections onto the first n−1 coordinates.
Let n > 0 and let π be the coordinate projection onto first n − 1 coordinates. Observe that

π(X) = {(α1, . . . , αn−1) ∈ R
n−1 : ∃αn ∈ R (α1, . . . , αn−1, αn) ∈ X}.

Thus π(X)R is equal to

{(v1, . . . , vn−1) ∈ Rn−1 : v1 ∼# · · · ∼# vn−1 ∧ ∃αn : (α(v1), . . . , α(vn−1), αn) ∈ X}.

Note that v ↦→ α(v) is a surjection R ↠ (0, 1) \ Q. Thus π(X)R is also equal to:

{(v1, . . . , vn−1) ∈ Rn−1 : v1 ∼# · · · ∼# vn−1 ∧ ∃vn : (α(v1), . . . , α(vn)) ∈ X}.

Unfortunately, this set is not necessarily equal to π(XR). There might be tuples
(v1, . . . , vn−1) such that no vn can be found, because it would require more bits in one
of its coefficients than v1, . . . , vn−1 have for that coefficient. But π(XR) always contains
some representation of α(v1), . . . , α(vn−1) with the appropriate number of digits. We need
only ensure that removal of trailing zeroes does not affect membership in the language. Thus
π(X)R is just the zero-closure of π(XR). Thus π(X)R is ω-regular by Lemma 3.5.

Theorem 6.5. Let X1, . . . , Xn be recognizable modulo ∼# by B¨uchi automata A1, . . . , An,
and let Q be the structure (Irr; X1, . . . , Xn). Then the theory of Q is decidable.

12:26 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

Proof. By Lemma 6.4 every set definable in Q is recognizable modulo ∼#. Moreover, for
each definable set Y the automaton that recognizes Y modulo ∼#, can be computed from the
automata A1, . . . , An. Let ψ be a sentence in the signature of Q. Without loss of generality,
we can assume that ψ is of the form ∃x χ(x). Set

Z := {a ∈ Irrn : Q |= χ(a)}.

Observe that Q |= ψ if and only if Z is non-empty. Note for every a ∈ Irrn there are
v1, . . . , vn ∈ R such that v1 ∼# v2 ∼# · · · ∼# vn and (α(v1), . . . , α(vn)) = a. Thus Z is
non-empty if and only if

{(v1, . . . , vn) ∈ Rn : v1 ∼# v2 ∼# · · · ∼# vn ∧ (α(v1), . . . , α(vn)) ∈ Z}

is non-empty. Thus to decide whether Q |= ψ, we first compute the automaton B that
recognizes Z modulo ∼#, and then check whether the automaton accepts any word.

We are now ready to prove Theorem C; that is, decidability of the theory of the structure

M = (Irr, <, (Mφ)φ, (q)q∈Irrquad),

where Mφ is defined for each Lm,a-formula as

Mφ := {α ∈ Irr : Rα |= φ}.

Proof of Theorem C. We just need to check that the relations we are adding are all recogniz-
able modulo ∼#. By Lemma 3.6 the ordering < is recognizable modulo ∼#. By Lemma 3.7,
the singleton {q} is is recognizable modulo ∼# for every q ∈ Irrquad. Since Mφ = α(Rφ),
recognizability of Mφ modulo ∼# follows from Theorem 6.1.

We can add to M a predicate for every subset of Irrn that is recognizable modulo ∼#, and
preserve the decidability of the theory. The reader can check that examples of subsets of
Irr recognizable modulo ∼# are the set of all α ∈ Irr such that the terms in the continued
fraction expansion of α are powers of 2, the set of all α ∈ Irr such that the terms in the
continued fraction expansion of α are in (or are not in) some fixed finite set, and the set of
all α ∈ Irr such that all even (or odd) terms in their continued fraction expansion are 1.

7. Automatically Proving Theorems about Sturmian Words

We have created an automatic theorem-prover based on the ideas and the decision algorithms
outlined above, called Pecan [OMSH20], available at
https://github.com/ReedOei/Pecan
We use Pecan to provide proofs of known and unknown results about characteristic Sturmian
words. The Pecan code for the following examples is available at
https://github.com/ReedOei/SturmianWords
We quote some of this code throughout this section. These code snippets should be
understandable without further explanation, but interested readers can find more information
and explanations in [OMSH21]. We recommend downloading the code instead of copying
from this paper. In addition to the size of the automata created by Pecan, we sometimes
state the runtime of Pecan on a normal laptop to indicate how quickly these statements
have been proved.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:27

7.1. Classical theorems. We begin by giving automated proofs for several classical result
result about Sturmian words. We refer the reader to [Lot02] for more information and
traditional proofs of these results.

In the following, we assume that a is irrational and i, j, k, n, m, p, s are a-Ostrowski repre-
sentations. This can be expressed in Pecan as

Let a is bco_standard .
Let i ,j ,k ,n ,m ,p , s are ostrowski ( a ) .

Here bco_standard is a data type for real numbers encoded using #-binary coding. Then
ostrowski(a) determines the Ostrowski numeration system used for the variables i,j,k,n,m,p
and s. Pecan allows the use of Unicode characters such as ∃, ∀, ¬ and ∧, and we will use
these here for readability. Of course, Pecan also supports writing exists, forall, ! and and for
the same operations. We write ca,0(i) as $C[i] in Pecan.

Let wR denote the reversal of a word w. We say a word w is a palindrome if w = wR.

Theorem 7.1. Characteristic Sturmian words are balanced and aperiodic.

Proof. To show that a characteristic Sturmian word ca,0 is balanced, it is sufficient to
show that there is no palindrome w in ca,0 such that 0w0 and 1w1 are in ca,0 (see [Lot02,
Proposition 2.1.3]). We encode this in Pecan as follows. The predicate palindrome(a,i,n) is
true when ca,0[i..i + n] = ca,0[i..i + n]R. The predicate factor_len(a,i,n,j) is true when
ca,0[i..i + n] = ca,0[j..j + n]. Then Pecan takes 321.73 seconds to prove the following
theorem:

Theorem ( " Balanced " , {
∀a . ¬(∃i , n . palindrome (a ,i , n ) ∧
(∃j . factor_len (a ,i ,n , j ) ∧ $C [ j - 1] = 0 ∧ $C [ j + n ] = 0) ∧
(∃k . factor_len (a ,i ,n , k ) ∧ $C [ k - 1] = 1 ∧ $C [ k + n ] = 1))
} ) .

Encoding the property that a word is eventually periodic is straightforward:

eventually_periodic (a , p ) : =
p > 0 ∧ ∃n . ∀i . if i > n then $C [ i ] = $C [ i + p ]

The resulting automaton has 4941 states and 35776 edges, and takes 117.78 seconds to build.
We then state the theorem in Pecan, which confirms the theorem is true.

Theorem ( " Aperiodic " , {
∀a . ∀p . if p > 0 then ¬eventually_periodic (a , p )
} ) .

A word w is a factor of a word u if there exist words v1, v2 such that u = v1wv2. A factor
w of a word u right special if both w0 and w1 are also factors of u.

Theorem 7.2. For each natural number n, ca,0 contains a unique right special factor of
length n, and this factor is ca,0[1..n + 1]R.

Proof. We first define right special factors, as above. Recall that factor_len(a,i,n,j) checks
that ca,0[i..i + n] = ca,0[j..j + n].

12:28 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

right_special_factor (a ,i , n ) : =
(∃j . factor_len (a ,i ,n , j ) ∧ $C [ j + n ] = 0) ∧
(∃k . factor_len (a ,i ,n , k ) ∧ $C [ k + n ] = 1)

We then define the first right special factor, which is the first occurrence (by index) of the right
special factor in the word ca,0. This step is purely to reduce the cost of checking the theorem:
the right_special_factor automaton has 3375 states, but first_right_special_factor has
only 112.

f i r s t _ r i g h t _ s p e c i a l _ f a c t o r (a ,i , n ) : = special_factor (a ,i , n )
∧ ∀j . if ( j > 0 ∧ factor_len (a ,j ,n , i )) then i < = j

We then check that each of these right special factors is equal to ca,0[1..n + 1]R, which
also proves the uniqueness. The predicate reverse_factor(a,i,j,l) checks that ca,0[i..j] =
ca,0[k + 1..l + 1]R, where j − i = l − k. Then Pecan confirms:

Theorem ( " The unique special factor of length n is C [1.. n +1]^ R " , {
∀a . ∀i , n .
if i > 0 ∧ f i r s t _ r i g h t _ s p e c i a l _ f a c t o r (a ,i , n ) then
reverse_factor (a ,i , i +n , n )
} ) .

Another characterization of Sturmian words due to Droubay and Pirillo [DP99, Theorem 5]
is that a word is Sturmian if and only if it contains exactly one palindrome of length n if n
is even, and exactly two palindromes of length n if n is odd. We prove the forward direction
below.

Theorem 7.3 [DP99, Proposition 6]. For every n ∈ N, ca,0 contains exactly one palindrome
of length n if n is even, and exactly two palindromes of length n if n is odd.

Proof. We begin by defining a predicate defining the location of the first occurrence of each
length n palindrome in ca,0.

first_palindrome (a , i , n ) : = palindrome (a , i , n ) ∧
∀j . if j > 0 ∧ factor_len (a ,j ,n , i ) then i < = j

The resulting automaton has 247 states and 1281 edges. The following states the theorem,
and Pecan proves it in 428.85 seconds.

Theorem ( " " , {
∀a . ∀n . (
if even ( n ) ∧ n > 0 then
∃i . ∀k . first_palindrome (a ,k , n ) iff i = k ) ∧ (
if odd ( n ) then
∃i , j . i < j ∧ ∀k . first_palindrome (a ,k , n ) iff ( i = k ∨ j = k )
) } ) .

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:29

7.2. Powers. Next, we prove the follow results about powers of Sturmian words. A finite
nonempty subword x of a (finite or ω) word w is a n-th power if x = yn for some finite
word y. We call a 2nd power a square, and a 3rd power a cube.

Using Pecan, we construct an automaton recognizing the following property, stating that
there is a square of length n starting at ca,0(i):

square(a , i , n ) : = n > 0 ∧ i > 0
∧ ∀j . i < = j ∧ j < i + n ∧ $C [ j ] =$C [ j + n ] .

The resulting automaton has 80 states and 400 edges. All characteristic Sturmian words
contain such a square, as Pecan proves in 0.02 seconds:

Theorem ( " " , { ∀a . ∃i , n . square(a , i , n ) } ) .

Of course, it is easy to see all binary words of length at least four contain squares. However,
it is still useful to have created an automaton for recognizing squares, because it encodes
quite a bit more information than just that squares exist: it also tells us exactly where they
are in the Sturmian word. This allows Pecan to prove the following result.

Theorem 7.4 (Dubickas [Dub09, Theorem 1]). All characteristic Sturmian words start with
arbitrarily long squares.

Proof. Using Pecan and the automaton for squares that we constructed earlier, we prove
the following theorem, which takes 0.40 seconds.

Theorem ( " " , { ∀a . ∀j , n . ∃m . m > n ∧ square(a , j , m )
} ) .

Furthermore, we can use an automaton recognizing squares to efficiently build automata
recognizing higher-powers. Indeed, we ask Pecan to construct an automaton recognizing the
following property that there is a cube of length n starting at ca,0(i), as follows:

cube (a , i , n ) : = square(a , i , n ) ∧ square(a , i + n , n )

We can ask Pecan to prove the well-known fact that characteristic Sturmian words contain
cubes:

Theorem ( " " , { ∀a . ∃i , n . cube (a , i , m ) } ) .

Pecan proves this in 0.25 seconds.

Similar to squares, we have the following property for cubic prefixes.

Theorem 7.5. Let a ∈ (0, 1). Then ca,0 starts with arbitrarily long cubes if and only if the
continued fraction of a is not eventually 1.

Proof. First, we manually build an automaton recognizing a such that the continued fraction
of a is not eventually one, called eventually one. Pecan proves the following in 2.37
seconds:

Theorem ( " " , {
∀a . ((¬eventually_one ( a )) iff (∀m . ∃n . n > m cube (a , 1 , n )))
} ) .

12:30 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

The proof of Theorem 7.5 highlights the ability of our decision algorithm, and hence of
Pecan, to not only determine whether statements hold for all irrational numbers, but also
whether a statement holds for all elements of a subset that is recognizable modulo ∼#.
Indeed, we can use Pecan to show that if the continued fraction of a is not eventually 1,
then ca,0 contains a fourth power. To do so, we construct a predicate that holds whenever
there is a fourth power of length n starting at ca,0(i):

fourth_pow (a , i , n ) : = square(a , i , n ) ∧ cube (a , i + n , n )

Finally, Pecan proves the following in 0.56 seconds.

Theorem ( " " , {
∀a . if ¬eventually_one ( a ) then ∃i , n . forth_pow (a ,i , n )
) } ) .

The converse is not true. Although it is easy to see without Pecan why, we can also ask
Pecan for counterexamples using the following commands.

Restrict i , n are ostrowski ( a ) .
has_fourth_pow ( a ) : = ∃i , n . n > 0 ∧ fourth_pow (a ,i , n )
Example ( ostrowskiFormat , {
bco_standard ( a ) ∧ eventually_one ( a ) ∧ has_fourth_pow ( a )
} ) .

Pecan responds with:

[( a ,[6][3]([1])^ω )]

This means that a = [0, 6, 3, 1] is a counterexample. Recall that a ∈ (0, 1), so the first digit
of the continued fraction is always 0 and therefore omitted by Pecan. For this choice of
a, the characteristic Sturmian word ca,0 starts with 000001. Thus there is a fourth power
immediately at the beginning of ca,0.

7.3. Antisquares and more. Let w ∈ {0, 1}∗. We let w denote the {0, 1}-word obtained
by replacing each 1 in w by 0 and each 0 in w by 1. A word w ∈ {0, 1}∗ is an antisquare if
w = vv for some v ∈ {0, 1}∗. We define AO : (0, 1) \ Q → N ∪ {∞} to map an irrational a to
the maximum order of an antisquare in ca,0 if such a maximum exists, and to ∞ otherwise.
We let AL : (0, 1) \ Q → N ∪ {∞} map a to the maximum length of an antisquare in ca,0 if
such a maximum exists and ∞ otherwise. Note that AL(a) = 2AO(a).

Recall that wR denotes the reversal of a word w. A word w ∈ {0, 1}∗ is an antipalindrome
if w = wR. We set AP : (0, 1) \ Q → N ∪ {∞} to be the map that takes an irrational a to
the maximum length of an antipalindrome in ca,0 if such a maximum, and to ∞ otherwise.
We will use Pecan to prove that AO(a), AL(a) and AP (a) are finite for every a. While the
quantities AO(a), AP (a) and AL(a) can be arbitrarily large, we prove the new results that
the length of the Ostrowski representations of these quantities is bounded, independent of a.

Let a ∈ (0, 1) be irrational and N ∈ N. Let |N |a denote the length of the a-Ostrowski
representation of N , that is the index of the last nonzero digit of a-Ostrowski representation
of N , or 0 otherwise.

Theorem 7.6. For every irrational a ∈ (0, 1)

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:31

(i) |AO(a)|a ≤ 4,
(ii) |AP (a)|a ≤ 4,
(iii) |AL(a)|a ≤ 6,
(iv) AO(a) ≤ AP (a) ≤ AL(a) = 2AO(a).

There are irrational numbers a, β ∈ (0, 1) such that AO(a) = AP (a) and AP (β) = AL(β).

Proof. Using Pecan, we create automata which compute AO, AP , and AL:

AO(a, n) := has antisquare(a, n) ∧ ∀m.has antisquare(a, m) =⇒ m ≤ n

AP (a, n) := has antipalindrome(a, n) ∧ ∀m.has antipalindrome(a, m) =⇒ m ≤ n

AL(a, n) := has antisquare len(a, n) ∧ ∀m.has antisquare len(a, m) =⇒ m ≤ n

We build automata recognizing a-Ostrowski representations of at most 4 and 6 nonzero
digits, called has 4 digits(n) and has 6 digits(n). Then we use Pecan to prove all the
parts of the theorem by checking the following statement.

Theorem ( " ( i ) , ( ii ) , ( iii ) , and ( iv ) " , {
∀a . has_4_digits (max antisquare( a )) ∧
has_4_digits ( max_antipalindrome ( a )) ∧
has_6_digits (max antisquare len( a )) ∧
max antisquare( a ) < = max_antipalindrome ( a ) ∧
max_antipalindrome ( a ) < = max antisquare len( a )
} ) .

We also use Pecan to find examples of the equality: when a = [0; 3, 3, 1], we have AO(a) =
AP (a) = 2, and when a = [0; 4, 2, 1], we have AP (a) = AL(a) = 2.

Theorem 7.7. For every irrational a ∈ (0, 1), all antisquares and antipalindromes in ca,0
are either of the form (01)∗ or of the form (10)∗.

Proof. We begin by creating a predicate called is all 01 stating that a subword ca,0[i..i + n]
is of the form (01)∗ or (10)∗. We do this simply stating that ca,0[k] ̸= ca,0[k + 1] for all k
with i ≤ k < i + n − 1.

is all 01(a ,i , n ) : =
∀k . if i < = k ∧ k < i + n - 1 then $C [ k ] ̸= $C [ k + 1]

We can now directly state both parts of the theorem; Pecan proves both in 76.1 seconds.

Theorem ( " All antisquares are of the form (01)^* or (10)^* " , {
∀a . ∀i , n . if antisquare(a ,i , n ) then is all 01(a ,i , n )
} ) .

Theorem ( " All antipalindromes are of the form (01)^* or (10)^* " , {
∀a . ∀i , n . if antipalindrome(a ,i , n ) then is all 01(a ,i , n )
} ) .

12:32 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

7.4. Least periods of factors of Sturmian words. We now use Pecan to give short
automatic proofs a result about the least period of factors of characteristic Sturmian words.

The semiconvergents pn,ℓ and qn,ℓ of a continued fraction [0; a1, a2, . . .] are defined so that

pn,ℓ
qn,ℓ = ℓpn−1 + pn−2
ℓqn−2 + qn−2

for 1 ≤ ℓ < an.

Theorem 7.8. Let p be the least period of a factor of ca,0. Then p is the denominator of a
semiconvergent of a; that is p = qn,ℓ for some n and ℓ.

Proof. We define when a number p is a least period of a factor of ca,0 as an automaton
lp_occurs, as follows:

least_period (a ,p ,i , j ) : = p = min { n : period (a ,n ,i , j ) }
lp_occurs (a , p ) : = ∃i , j . i > 0 ∧ j > 0 ∧ least_period (a ,p ,i , j )

It is easy to recognize a-Ostrowski representations of denominators of semiconvergents of a,
because they are simply valid representations of the form [0 · · · 01b]a, where b is some valid
digit.

Theorem ( " " ,
{ ∀a , p . if lp_occurs (a , p ) then semiconvergent_denom ( p ) } ) .

Pecan proves the theorem in 5016.77 seconds.

A word w is called unbordered if the least period of w is |w|. We now are ready to
reprove Lemma 8 in Currie and Saari [CS09]. This is originally due to de Luca and De Luca
[dLDL06].

Theorem 7.9. The least period of ca,0[i..j] is the length of the longest unbordered factor of
ca,0[i..j].

Proof. We have previously defined least periods, so we can easily define unbordered factors.
Similarly, it is straightforward to define the longest unbordered subwords of ca,0:

m a x _ u n b o r d e r e d _ s u b f a c t o r _ l e n (a ,i ,j , n ) : =
n = max { m : ∃k . i < = k ∧ k + n < = j ∧ least_period (a ,n ,k , k + n ) }

Then the theorem we wish to prove is

Theorem ( " " , { ∀a ,i ,j , p . if i > 0 ∧ j > i ∧ p > 0 then
least_period (a ,p ,i , j ) iff m a x _ u n b o r d e r e d _ s u b f a c t o r _ l e n (a ,i ,j , p )
} ) .

Pecan confirms the theorem is true.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:33

7.5. Periods of the length-n prefix. In [GRS21] Gabric, Rampersand and Shallit charac-
terize all periods of the length-n prefix of a characteristic Sturmian word in terms of the
lazy Ostrowski representation. We are able implement their argument in Pecan.

Let a be a real number with continued fraction expansion [a0; a1, a2, . . .] and convergents
pk/qk ∈ Q. We recall the definition of the lazy a-Ostrowski numeration system [EFG+12].

Fact 7.10. Let X ∈ N. The lazy a-Ostrowski representation of X is the unique word
bN · · · b1 such that
 X =
 N∑

n=0 bn+1qn

where
(1) 0 ≤ b1 < a1;
(2) 0 ≤ bi ≤ ai for i > 1;
(3) if bi = 0 then bi−1 = ai for all i > 2;
(4) if b2 = 0, then b1 = a1 − 1;

Theorem 7.11 [GRS21, Theorem 6]. Let a be an irrational real number, and define Yn to
be the length n prefix of ca,0. Define PER(n) to be the set of all periods of Yn. Then
(1) The number of periods of Yn is equal to the sum of the digits in the lazy Ostrowski
representation of n.
(2) Let the lazy Ostrowski representation of n be b1 · · · bN , and define

A(n) =
 



iqj + ∑

j<k<N bk+1qk : 1 ≤ i ≤ bj+1 and 0 ≤ j ≤ N
 




Then PER(n) = A(n).

Proof. As in [GRS21], we note that it is sufficient to prove only (2). We begin by defining
the sets, indexed by the slope a. The set of periods of subwords of ca,0 can be defined by the
formula p > 0 ∧ ca,0[i..j − p] = ca,0[i + p..j], allowing us to create an automaton recognizing
this set, which we call period(a,p,i,j). This automaton is more expressive what what we
need for this theorem, so we then simply take the periods of the prefixes of ca,0, as follows:

p is $Per (a , n ) : = ∃s . s = 1 ∧ period (a ,p ,s , n + 1)

To define A(n), we first define several auxiliary automata and notions. Earlier, we defined
addition automata for the (greedy) Ostrowski numeration system, but we can also easily
handle the lazy Ostrowski numeration system using an automaton recognizing
{

(a, x, y) : x, y ∈ Afin
a , x = #x1#x2# · · · , y = #y1#y2# · · · ,
 ∞∑

i=0 xi+1qi =
 ∞∑

i=0 yi+1qi
}

which we call ost_equiv(a,x,y). The lazy_ostrowski(a,n) automaton checks whether n is
a valid lazy a-Ostrowski representation. These automata allow us to convert between the
two systems.
To define A(n), we break it up into smaller pieces; first, we wish to recognize the set

B(n) = {iqj : 1 ≤ j ≤ bj+1 and 0 ≤ j ≤ N }.

12:34 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

For each x ∈ (#(0|1)∗)ω, denote by |x|fin the length of the longest prefix y of x such that
x = yz where z ∈ (#0∗)ω, or ∞ if there is no such prefix. We then create the following
automata:

• as_long_as(x,y) recognizing the set {(x, y) : |x|fin ≥ |y|fin}.
• has_1_digit(x) recognizing the set (#0∗)∗((#0∗)|(#(0|1)∗1(0|1)∗))(#0∗)ω, i.e., words of
the form #w1#w2# · · · such that there is at most one wi such that wi ̸∈ 0∗.
• bounded_by(x,y) recognizing the set

{(x, y) : x and y are aligned, x = #x1#x2# · · · , y = #y1#y2# · · · , ∀i.xi ≤lex yi}

Then we can recognize the set B(n) from above by

i > 0 ∧ has_1_digits ( i ) ∧ as_long_as (n , i ) ∧ bounded_by (i , n_l )

where n_l is the lazy a-Ostrowski representation of n.
The last automaton we need to create is suffix_after(x,y,s), recognizing the set
{(x, y, s) : s = 0|x|fin · y[|x|fin..]}. We need this to be able to recognize the set of a-Ostrowski
representations

{m : 0 ≤ j ≤ N, ml = 0
jnl[j..N ], ml is the lazy a-Ostrowski representation of Za(m)}

where nl is the lazy a-Ostrowski representation of Za(n).
Finally, we can put everything together and define A(n), again indexed by the slope a,
as:

p is $A (a , n ) : =
∃ n_l , m_l . lazy_ostrowski (a , n_l ) ∧ ost_equiv (a ,n , n_l ) ∧
∃m . ost_equiv (a , m_l , m ) ∧
∃i . i > 0 ∧ has_1_digit ( i ) ∧ as_long_as (n , i ) ∧
bounded_by (i , n_l ) ∧ suffix_after (i , n_l , m_l ) ∧
i + m = p

Finally, we can state the theorem directly, which Pecan confirms is true.

Theorem ( " 6 ( b ) " , { ∀a . ∀p , n . p is $Per (a , n ) iff p is $A (a , n )
} ) .
 8. Conclusion and Outlook

8.1. Scalar multiplication. Recall that for α ∈ R>0 we use Rα to denote the Lm,a-
structure (R, <, +, Z, aZ). Let λα : R → R be the function mapping x to αx, and let
Sα denote the structure (R, <, +, Z, λα). It is clear that every set definable in Rα is also
definable in Sα. The inverse is known to be true for some α: By Hieronymi [Hie19, Theorem
D], the function λα is definable in Rα if α = √d for some d ∈ Q, and thus in this situation
every set definable in Sα is also definable in Rα.

Proposition 8.1. There is α ∈ R such that Rα does not define λα.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:35

Proof. By [Hie19, Theorem A] the theory FO(Sα) is undecidable when α is not quadratic.
Thus is enough to find a non-quadratic α such that the theory FO(Rα) is decidable. To do
so, it suffices by Theorem 5.1 to find some v ∈ R such that FO(Dv) is decidable but α(v) is
non-quadratic.
Let U be the set {i! : i ∈ N}. Define u = u1u2 · · · ∈ {0, 1}ω such that ui = 1 if i ∈ U , and
ui = 0 otherwise. Let v = v1v2 · · · ∈ Σω
# be such that

vi =
 




# i = 1,
# i > 2 and ui = 1,
1 otherwise.

That is, v = #1111#11111111111111111#1 · · · .
By Elgot and Rabin [ER66, Proof of Theorem 5], the acceptance problem for u is decidable.
This implies that the acceptance problem for v is decidable as well. Thus the theory FO(Dv)
is decidable by Fact 2.4. However, the coefficients of the continued fraction expansion of α(v)
are unbounded. Since quadratic numbers have periodic continued fractions, we conclude
that α(v) is not quadratic.

As argued in the proof above, it follows from Fact 2.4 that for every α ∈ Irr the theory
FO(Rα) is decidable whenever there is v ∈ R such that the acceptance problem for v is
decidable and α(v) = α. We leave it as an open question whether this sufficient condition is
also necessary. It would be interesting to know whether there are any natural non-quadratic
numbers, like e or π, for which this condition is satisfied.

Recall that Lm is the signature of FO(R, <, +) together with a unary precidate symbol P .
Let Lm,λ be the extension of Lm by a unary functions symbol λ. We consider Sα now as
an Lm,λ-structure. Let Kλ be the class of Lm,λ-structures {Sα : α ∈ Irr}. By Proposition
8.1 there is no hope of using Theorem B to deduce the decidability of the theory FO(Kλ).
Indeed, we can show the following.

Proposition 8.2. The theory FO(Kλ) is undecidable.

Proof. Consider the Lm,λ-sentence ψ

∀x1∀x2∀x3 (
 3⋀

i=1 P (xi) ∧
 3⋁

i=1 xi ̸= 0) → (λ(λ(x1)) + λ(x2) + x3 ̸= 0).

Hence Sα |= ψ if and only if α is not quadratic.
Consider U = (Q, Σ, σ1, δ, q1, q2) be the universal 1-tape Turing machine with 8 states and 4
symbols as defined by Neary and Woods [NW06]. By the proof of [HNP21, Theorem 7.1]6,
given an input x ∈ Σ∗, there is an Lm,λ-sentence φx such that for every non-quadratic α

Sα |= φx if and only if U halts on input x.

Combining this, we have that given an input x ∈ Σ∗

FO(Kλ) |= ψ → φx if and only if U halts on input x.

6In [HNP21] it is only stated that for every non-quadratic α we can find such an Lm,λ-sentence φx.
However, it is clear from the given construction that the sentence does not depend on the particular α.

12:36 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

Thus FO(Kλ) is undecidable.

Let Kq be the class of all Lm,a-structures Rα with α ∈ Irr quadratic, and similarly, let
Kλ,q be the class of all Lm,λ-structures Sα with α ∈ Irr quadratic. We leave it as an open
question whether the theories FO(Kq) and FO(Kλ,q) are decidable. It is unlikely that that
decidability of the latter theory could be deduced from the decidability of the theory FO(Kq),
because the definition of multiplication by √d in the proof of [Hie19, Theorem D] depends
on d.

8.2. Computational complexity. By [Hie16, Theorem D], the structure Rα defines an
isomorphic copy of the standard model of the monadic second-order theory of (N, +1) when-
ever α ∈ Irr. Hence there can not be a decision algorithm for FO(K) whose computational
complexity is in general lower than the complexity of the decision algorithm presented here.
See [HNP21] for more detailed results for FO(Sα) when α is quadratic. It would still be inter-
esting to know whether improvements can be obtained for specific fragments of these theories.

If we are only interested in deciding statements about Sturmian words, we only need decid-
ability of the less expressive theories Ksturmian and Kchar. Here we know very little about
lower bounds for the computational complexity of these decision problems. In particular, we
do not even know whether an analogue of [Hie16, Theorem D], stating the definability of an
isomorphic copy of the standard model of the weak monadic second-order theory of (N, +1),
holds for Nα,ρ, when α ∈ Irr.

Better results are likely obtainable when dropping the order relation. For α ∈ Irr, consider
Zα := (Z, +, 0, 1, fα), where fα : Z → Z is the function mapping x to ⌊αx⌋. Khani and
Zarei [KZ23] and Khani, Valizadeh and Zarei [KVZ21] prove quantifier-elimination results
for such structures that have the potential to produce more efficient decision algorithms (see
also G¨unaydın and ¨Ozsahakyan [GO22]). However, the usual order relation of Z is unlikely
to be definable in such structures, and therefore this setting might not be particularly useful
to decide statements about Sturmian words.

References

[AS03] Jean-Paul Allouche and Jeffrey Shallit. Automatic sequences. Cambridge University Press,
Cambridge, 2003. Theory, applications, generalizations. doi:10.1017/CBO9780511546563.
[AZGR17] Faried Abu Zaid, Erich Gr¨adel, and Frederic Reinhardt. Advice Automatic Structures and
Uniformly Automatic Classes. In Valentin Goranko and Mads Dam, editors, 26th EACSL
Annual Conference on Computer Science Logic (CSL 2017), volume 82 of Leibniz International
Proceedings in Informatics (LIPIcs), pages 35:1–35:20, Dagstuhl, Germany, 2017. Schloss
Dagstuhl – Leibniz-Zentrum f¨ur Informatik. doi:10.4230/LIPIcs.CSL.2017.35.
[BGS23] Alexi Block Gorman and Christian Schulz. Fractal dimensions of k-automatic sets. J. Symb.
Log., page to appear, 2023. doi:10.1017/jsl.2023.55.
[BHMV94a] V´eronique Bruy`ere, Georges Hansel, Christian Michaux, and Roger Villemaire. Correction to:
“Logic and p-recognizable sets of integers”. Bull. Belg. Math. Soc. Simon Stevin, 1(4):577, 1994.
[BHMV94b] V´eronique Bruy`ere, Georges Hansel, Christian Michaux, and Roger Villemaire. Logic and p-
recognizable sets of integers. Bull. Belg. Math. Soc. Simon Stevin, 1(2):191–238, 1994. Journ´ees
Montoises (Mons, 1992). doi:10.36045/bbms/1103408547.
[BS19] Aseem R. Baranwal and Jeffrey Shallit. Critical exponent of infinite balanced words via the Pell
number system. In Combinatorics on words, volume 11682 of Lecture Notes in Comput. Sci.,
pages 80–92. Springer, Cham, 2019. doi:10.1007/978-3-030-28796-2.

Vol. 20:3 DECIDABILITY FOR STURMIAN WORDS 12:37

[BSS21] Aseem Baranwal, Luke Schaeffer, and Jeffrey Shallit. Ostrowski-automatic sequences: theory
and applications. Theoret. Comput. Sci., 858:122–142, 2021. doi:10.1016/j.tcs.2021.01.018.
[B¨uc62] J. Richard B¨uchi. On a decision method in restricted second order arithmetic. In Logic, Method-
ology and Philosophy of Science (Proc. 1960 Internat. Congr.), pages 1–11. Stanford Univ. Press,
Stanford, Calif., 1962.
[CS09] James D. Currie and Kalle Saari. Least periods of factors of infinite words. Theor. Inform. Appl.,
43(1):165–178, 2009. doi:10.1051/ita:2008006.
[CT02] Olivier Carton and Wolfgang Thomas. The monadic theory of morphic infinite words and
generalizations. Inform. and Comput., 176(1):51–65, 2002. doi:10.1006/inco.2001.3139.
[dLDL06] Aldo de Luca and Alessandro De Luca. Some characterizations of finite Sturmian words. Theoret.
Comput. Sci., 356(1-2):118–125, 2006. doi:10.1016/j.tcs.2006.01.036.
[DP99] Xavier Droubay and Giuseppe Pirillo. Palindromes and Sturmian words. Theoret. Comput. Sci.,
223(1-2):73–85, 1999. doi:10.1016/S0304-3975(97)00188-6.
[Dub09] Art¯uras Dubickas. Squares and cubes in Sturmian sequences. Theor. Inform. Appl., 43(3):615–
624, 2009. doi:10.1051/ita/2009005.
[EFG+12] C. Epifanio, C. Frougny, A. Gabriele, F. Mignosi, and J. Shallit. Sturmian graphs and integer
representations over numeration systems. Discrete Appl. Math., 160(4-5):536–547, 2012. doi:
10.1016/j.dam.2011.10.029.
[ER66] Calvin Elgot and Michael Rabin. Decidability and undecidability of extensions of second (first)
order theory of (generalized) successor. J. Symb. Log., 31(2):169–181, 1966. doi:10.2307/
2269808.
[GHS13] Daniel Goˇc, Dane Henshall, and Jeffrey Shallit. Automatic theorem-proving in combi-
natorics on words. Internat. J. Found. Comput. Sci., 24(6):781–798, 2013. doi:10.1142/
S0129054113400182.
[GO22] Ayhan G¨unaydın and Melissa ¨Ozsahakyan. Expansions of the group of integers by Beatty
sequences. Ann. Pure Appl. Logic, 173(3):Paper No. 103062, 22, 2022. doi:10.1016/j.apal.
2021.103062.
[GRS21] Daniel Gabric, Narad Rampersad, and Jeffrey Shallit. An inequality for the number of periods in a
word. Internat. J. Found. Comput. Sci., 32(5):597–614, 2021. doi:10.1142/S0129054121410094.
[Hie16] Philipp Hieronymi. Expansions of the ordered additive group of real numbers by two discrete
subgroups. J. Symb. Log., 81(3):1007–1027, 2016. doi:10.1017/jsl.2015.34.
[Hie19] Philipp Hieronymi. When is scalar multiplication decidable? Ann. Pure Appl. Logic, 170(10):1162–
1175, 2019. doi:10.1016/j.apal.2019.05.001.
[HMO
+22] Philipp Hieronymi, Dun Ma, Reed Oei, Luke Schaeffer, Christian Schulz, and Jeffrey Shallit.
Decidability for Sturmian Words. In Florin Manea and Alex Simpson, editors, 30th EACSL
Annual Conference on Computer Science Logic (CSL 2022), volume 216 of Leibniz International
Proceedings in Informatics (LIPIcs), pages 24:1–24:23, Dagstuhl, Germany, 2022. Schloss
Dagstuhl – Leibniz-Zentrum f¨ur Informatik. doi:10.4230/LIPIcs.CSL.2022.24.
[HNP21] Philipp Hieronymi, Danny Nguyen, and Igor Pak. Presburger arithmetic with algebraic scalar mul-
tiplications. Log. Methods Comput. Sci., 17(3):Paper No. 4, 34, 2021. doi:10.46298/lmcs-17(3:
4)2021.
[Hod82] Bernard R. Hodgson. On direct products of automaton decidable theories. Theoret. Comput.
Sci., 19(3):331–335, 1982. doi:10.1016/0304-3975(82)90042-1.
[HT18] Philipp Hieronymi and Alonza Terry, Jr. Ostrowski numeration systems, addition, and finite
automata. Notre Dame J. Form. Log., 59(2):215–232, 2018. doi:10.1215/00294527-2017-0027.
[HW79] G. H. Hardy and E. M. Wright. An introduction to the theory of numbers. The Clarendon Press,
Oxford University Press, New York, fifth edition, 1979.
[KM10] Bakhadyr Khoussainov and Mia Minnes. Three lectures on automatic structures. In Logic
Colloquium 2007, volume 35 of Lect. Notes Log., pages 132–176. Assoc. Symbol. Logic, La Jolla,
CA, 2010. doi:10.1017/CBO9780511778421.008.
[KN01] Bakhadyr Khoussainov and Anil Nerode. Automata theory and its applications, volume 21 of
Progress in Computer Science and Applied Logic. Birkh¨auser Boston, Inc., Boston, MA, 2001.
doi:10.1007/978-1-4612-0171-7.
[KVZ21] Mohsen Khani, Ali N Valizadeh, and Afshin Zarei. The additive structure of integers with a
floor function. arXiv:2110.01673, 2021.

12:38 P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, and J. Shallit Vol. 20:3

[KZ23] Mohsen Khani and Afshin Zarei. The additive structure of integers with the lower Wythoff
sequence. Arch. Math. Logic, 62(1-2):225–237, 2023. doi:10.1007/s00153-022-00846-2.
[Lot02] M. Lothaire. Algebraic combinatorics on words, volume 90 of Encyclopedia of Mathematics and its
Applications. Cambridge University Press, Cambridge, 2002. doi:10.1017/CBO9781107326019.
[Mou16] Hamoon Mousavi. Automatic Theorem Proving in Walnut, 2016. arXiv:1603.06017.
[MSS16] Hamoon Mousavi, Luke Schaeffer, and Jeffrey Shallit. Decision algorithms for Fibonacci-
automatic words, I: Basic results. RAIRO Theor. Inform. Appl., 50(1):39–66, 2016. doi:10.
1051/ita/2016010.
[NW06] Turlough Neary and Damien Woods. Small fast universal Turing machines. Theoret. Comput.
Sci., 362(1-3):171–195, 2006. doi:10.1016/j.tcs.2006.06.002.
[OMSH20] Reed Oei, Eric Ma, Christian Schulz, and Philipp Hieronymi. Pecan. available at https:
//github.com/ReedOei/Pecan, 2020.
[OMSH21] Reed Oei, Eric Ma, Christian Schulz, and Philipp Hieronymi. Pecan: An Automated Theorem
Prover for Automatic Sequences using B¨uchi automata. arXiv:2102.01727, 2021.
[Ost22] Alexander Ostrowski. Bemerkungen zur Theorie der Diophantischen Approximationen. Abh.
Math. Sem. Univ. Hamburg, 1(1):77–98, 1922. doi:10.1007/BF02940581.
[RS92] Andrew M. Rockett and Peter Sz¨usz. Continued fractions. World Scientific Publishing Co., Inc.,
River Edge, NJ, 1992. doi:10.1142/1725.
[Sch23] Fabian Schmitthenner. Decidability Questions in Ostrowski Numeration Systems, 2023. The-
sis (Bachelor)–University of Bonn. URL: https://www.math.uni-bonn.de/people/phierony/
Schmitthenner.pdf.
[Sem83] Aleksei L. Semenov. Logical theories of one-place functions on the natural number series. Izv.
Akad. Nauk SSSR Ser. Mat., 47(3):623–658, 1983.
[Sko31] Thoralf Skolem. ¨Uber einige Satzfunktionen in der Arithmetik. Skr. Norske Vidensk. Akad.,
Oslo, Math.-naturwiss. Kl., 7:1–28, 1931.

This work is licensed under the Creative Commons Attribution License. To view a copy of this
license, visit https://creativecommons.org/licenses/by/4.0/ or send a letter to Creative
Commons, 171 Second St, Suite 300, San Francisco, CA 94105, USA, or Eisenacher Strasse 2,
10777 Berlin, Germany
