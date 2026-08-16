<!-- source: https://dml.cz/bitstream/handle/10338.dmlcz/133405/ActaOlom_47-2008-1_5.pdf | converted from PDF -->

Acta Universitatis Palackianae Olomucensis. Facultas Rerum
Naturalium. Mathematica

Gábor Czédli; E. Tamás Schmidt
Frankl’s conjecture for large semimodular and planar semimodular lattices

Acta Universitatis Palackianae Olomucensis. Facultas Rerum Naturalium. Mathematica, Vol. 47 (2008), No.
1, 47--53

Persistent URL: http://dml.cz/dmlcz/133405

Terms of use:

© Palacký University Olomouc, Faculty of Science, 2008

Institute of Mathematics of the Academy of Sciences of the Czech Republic provides access to
digitized documents strictly for personal use. Each copy of any part of this document must contain
these Terms of use.
 This paper has been digitized, optimized for electronic delivery and stamped
with digital signature within the project DML-CZ: The Czech Digital Mathematics
Library http://project.dml.cz

    *

Gábor CZÉDLI 1, E. Tamás SCHMIDT 2

1

2

(Received April 11, 2008)

Abstract

A lattice L is said to satisfy (the lattice theoretic version of) Frankl’s
conjecture if there is a join-irreducible element f ∈ L such that at most
half of the elements x of L satisfy f ≤ x. Frankl’s conjecture, also called
as union-closed sets conjecture, is well-known in combinatorics, and it
is equivalent to the statement that every ﬁnite lattice satisﬁes Frankl’s
conjecture.
Let m denote the number of nonzero join-irreducible elements of L.It
is well-known that L consists of at most 2
m elements. Let us say that L
is large if it has more than 5 · 2
m−3 elements. It is shown that every large
semimodular lattice satisﬁes Frankl’s conjecture. The second result states
that every ﬁnite semimodular planar lattice L satisﬁes Frankl’s conjecture.
If, in addition, L has at least four elements and its largest element is join-
reducible then there are at least two choices for the above-mentioned f .

Key words: Union-closed sets; Frankl’s conjecture; lattice, semi-
modularity; planar lattice.

2000 Mathematics Subject Classiﬁcation: 05A05, sec.: 06E99

*

 47

48 Gábor CZÉDLI, E. Tamás SCHMIDT

Given an m-element ﬁnite set A = {a1,...,am}, m ≥ 3,a  (or, in
other words, a set) F of at least two subsets of A, i.e. F⊆ P (A), is called
a   (over A)if X ∪ Y ∈F whenever X, Y ∈F.It was
Peter Frankl in 1979 (cf. Frankl [9]) who formulated the following conjecture,
now called as   or    :if F is as
above then there exists an element of A which is contained in at least half of
the members of F . In spite of at least three dozen papers, cf. the bibliography
given in [8], this conjecture is still open.
Now let L be a ﬁnite lattice. As usual, the set of its nonzero join-irreducible
elements will be denoted by J(L).We say that L satisﬁes (the lattice theoretic
version of) Frankl’s conjecture if |L| =1 or there is an f ∈ J(L) such that for
the principal ﬁlter ↑f = {x ∈ L : f ≤ x} we have |↑f |≤ |L|/2.Stanley [17]
and Poonen [14] or Abe and Nakano [3] have shown that (the original) Frankl’s
conjecture is true if and only if all ﬁnite lattices satisfy (the lattice theoretic)
Frankl’s conjecture. (For details one can also see [6].) This fact has initiated
a series of lattice theoretical results given by Abe and Nakano [1], [2], [3], [4],
Herrmann and Langsdorf [13], and Reinhold [15], and two combinatorial results
achieved by means of lattices, cf. [6] and [8]. In particular, lower semimodular
lattices satisfy Frankl’s conjecture by [15], and the method of [15] makes it
clear that the situation for (upper) semimodular lattices is much harder. In
fact, it is (and it remains) unknown if semimodular lattices satisfy Frankl’s
conjecture. The goal of the present paper is to present two subclasses of the
class of ﬁnite semimodular lattices such that every lattice L in these subclasses
satisﬁes Frankl’s conjecture; in fact, L usually satisﬁes the conjecture in a bit
stronger form.
For elements x and y of a lattice L,let x ≼ y denote the “covers or equals”
relation. That is, x ≼ y iﬀ x ≤ y and there is no z ∈ L with x<z < y.
Recall that L is called (upper)  if, for any a, b, c ∈ L, a ≼ b implies
a ∨ c ≼ b ∨ c.Let J(L) denote the set of non-zero join-irreducible elements of L,
and let m = |J(L)|. Since each element of L is the join of a subset of J(L), L
has at most 2m elements. Strengthening a former result of Gao and Yu [10], it
is shownin[6] that L satisﬁes Frankl’s conjecture provided |L|≥ 2m − 2m/2.In
the semimodular case we can prove more. For simplicity, ﬁnite lattices L with
more than 5·2m−3 =2m − 3
8 ·2m elements will be called  .The  h(x) of
an element x ∈ L is the length (number of elements minus one) of any maximal
chain in the principal ideal ↓x. (This makes sense, for any two maximal chains
has the same length by semimodularity.)

Theorem 1  L    L
|L| > 5 · 2m−3 m = |J(L)| L

Proof Let A(L) denote the set of atoms of L.
First we show that |J(L) \ A(L)|≤ 1. By way of contradiction, assume that
a1 and a2 are distinct elements of J(L) \ A(L).Let a3,... ,am be the rest of
nonzero join-irreducible elements, i.e., J(L)= {a1,a2,... ,am}.Let Bm be the
boolean lattice with atoms x1,... ,xm, and consider both Bm =(Bm; ∨, 0) and

Frankl’s conjecture and semimodularity 49

L =(L; ∨, 0) as join-semilattices with 0. Since Bm is the free join-semilattice
with 0, there is a surjective homomorphism ϕ : Bm → L, xi ↦→ ai.Let Θ denote
the kernel of ϕ. Then, for i =1, 2,the Θ-class [xi] of xi is not a singleton, for
otherwise ai would be an atom. Since ai ̸=0, we conclude that 0 /∈ [xi].Since
Θ-classes are convex subsemilattices, there are elements y1 ∈ [x1] and y2 ∈ [x2]
such that y1 ≻ x1 and y2 ≻ x2. They are distinct, for a1 ̸= a2.Let z = y1 ∧ y2;
it is an atom or the zero of Bm.
 J :

1y 2y

1x 2xz

I :

1y 2y

1x 2x

Fig. 1: Two ideals in Bm

First assume that z is an atom, and consider the ideal I = ↓(y1∨y2) in Bm,cf.
Figure 1. Let K denote the subsemilattice generated by those atoms of Bm that
are not in I; K is not indicated in the ﬁgure. It follows from (x1,y1), (x2,y2) ∈ Θ
that the restriction Θ|I to I includes the semilattice congruence indicated in the
ﬁgure. Hence Θ collapses I to ﬁve or less elements. For u ∈ K,let u ∨ I =
{u ∨ t : t ∈ I}.If (t1,t2) ∈ Θ|I then (u ∨ t1,u ∨ t2) ∈ Θ. Hence Θ collapses u ∨ I
to ﬁve or less elements. Now Bm is the union of the pairwise disjoint subsets
u ∨ I, u ∈ Bm. Therefore L ∼= Bm/Θ consists of at most 5 ·|K| =5 · 2m−3

elements, which contradicts the assumption that L is large.
Secondly, assume that z =0, and consider the ideal J = ↓(y1 ∨ y2),cf.
Figure 1. Then the same argument as above gives |L|≤ 9 · 2m−4 < 5 · 2m−3,a
contradiction again. This proves that |J(L) \ A(L)|≤ 1.
Now, let us recall a well-known fact on semimodular lattices. An n-element
subset U = {c1,... ,cn} of A(L) is called  if the sublattice [U ]
generated by U is boolean with A([U ]) = U . It is well-known, cf. e.g., Theorem
IV.2.4 in Gr¨atzer [11], that U is independent if and only if

(c1 ∨ ··· ∨ ci) ∧ ci+1 =0 for i =1, 2,... ,n − 1. (1)

We need another, much easier version of independence: U ⊆ J(L) will be called
an   if u ̸≤ ⋁(
U \{u}) for every u ∈ U .In other words, U =
{c1,...,cn} is independent if no joinand can be omitted from c1 ∨ ··· ∨ cn.
Now, armed with |J(L) \ A(L)|≤ 1, let us introduce some new notations. If
|J(L) \ A(L)| =1,thenlet a1 be the only element of J(L) \ A(L),let a2,... ,ak
be the atoms in ↓a1,and let b1,...,bm−k be the rest of atoms. (Note that
k ≥ 2.) Otherwise, when J(L)= A(L),let k =1,let a1 be an arbitrarily ﬁxed
atom, and let b1,...,bm−1 be the rest of atoms.

50 Gábor CZÉDLI, E. Tamás SCHMIDT

We claim that |↑a1|≤ |L|/2. It suﬃces to show that for each x ∈↑a1 there
exists an y = y(x) ∈ L \↑a1 such that a ∨ y = x. (If there are several elements
y with this property then we choose one of them.) Indeed, then the existence of
the  mapping ↑a1 → L \↑a1, x ↦→ y(x) will complete the proof. So, let
x ∈↑a1 be an arbitrary element. Then, clearly, there is an irredundant subset
U of J(L) whose join is x.
First let us assume that ai is in U for some 1 ≤ i ≤ k. Now we deﬁne
y = ⋁(
U \{ai})
.Then x = ai ∨ y and ai ≤ a1 ≤ x gives x = a1 ∨ y while the
irredundance of U yields ai ̸≤ y, implying y/∈↑a1.
Secondly, we assume that no ai belongs to U .Then U is a set of atoms, say
U = {b1,...,bn}. Using condition (1) and the irredundance of U we conclude
that U is an independent set. Deﬁne di = b1 ∨ ··· ∨ bi−1 ∨ bi+1 ∨ ··· bn.Then
the di, 1 ≤ i ≤ n, are the coatoms of the boolean sublattice generated by U .
If a1 ≤ di for all i,then a1 ≤ ⋀n
i=1 di =0, a contradiction. Hence we can
select an i ∈{1,... ,n} such that a1 ̸≤ di.Then y = di does the job, for
di =0 ∨ di ≺ bi ∨ di = x by semimodularity, and di <a1 ∨ di ≤ x. 

Let us recall that ﬁnite, atomistic, semimodular lattices are
by deﬁnition. Using the ideas around Figure 1, it is easy to see that (x1,y1) ∈ Θ
implies that at leat 2m−2 elements of Bm are collapsed, i.e., L has at most
2m − 2m−2 =6 · 2m−3 elements. This means that |L| > 6 · 2m−3 implies
J(L)= A(L) and |[xi]| =1 (i =1,... ,m), whence the above proof clearly
yields the following

Corollary 1  L     |L| > 6 · 2m−3
m = |J(L)| L        f  L |↑f |≤
|L|/2

If L has a Hasse diagram whose edges cross only at vertices then L is called
a   . Recently, Gr¨atzer and Knapp [12] has given a useful struc-
ture theorem for ﬁnite planar semimodular lattices; this is what the present
paper relies on. Although this structure theorem is now generalized to all ﬁnite
semimodular lattices in [7], we have been able to treat the planar case only.
If a ∥ b,then S = {a, b, a ∧ b, a ∨ b}⊆ L will be called a  of L.If,
in addition, a ∧ b ≺ a and a ∧ b ≺ b,then S is called a   .By
semimodularity, a ∨ b covers both a and b when S is a covering square. If each
covering square of L is an interval then L is said to be  . A mapping is called
cover-preserving if it preserves the relation ≼. Let us recall

Lemma 1

•

•

Frankl’s conjecture and semimodularity 51

Using the connection between Frankl’s original conjecture and its lattice
theoretic version, Roberts [16] yields that lattices with at most forty elements
satisfy Frankl’s conjecture. However, to explain why |L|≥ 4 is assumed in our
main result below, we need only the obvious observation that lattices with less
than four elements satisfy Frankl’s conjecture.

Theorem 2  L
   L

•  1 ∈ J(L)  |↑f |≤ |L|/4  f =1

•      f1  f2  J(L)   |↑fi|≤
|L|/2  i =1, 2

Proof Let L be a ﬁnite planar semimodular lattice with |L|≥ 4. We will
assume that L is not a chain and 1 /∈ J(L), for otherwise the statement is
evident.

First we consider the case when L is slim. We will treat it as a join-semilattice
(L, ∨). In virtue of Lemma 1, there are two chains, {0 < 1 < ··· <n} and
{0 < 1 < ··· <m}, and a join-congruence Θ of

D = {0 < 1 < ··· <n}×{0 < 1 < ··· <m}

such that, up to isomorphism, L =(L, ∨) equals D/Θ. (We will not use the
cover-preserving property of the canonical L → L/Θ homomorphism.) Since L
is not a chain, n ≥ 2 and m ≥ 2. We assume that n and m are chosen such
that m + n is minimal, and we prove the slim case via induction on m + n.The
smallest case, m = n =2 is evident. So we assume that m + n> 4.For brevity,
let u =(n, 0), v =(0,m), 1= (m, n), h =(n − 1,m), cf. Figure 2.

1=(n,m)=

0=(0,0)

u=(n,0) v=(0,m)

h=(n-1,m)

a b

c c’ c’’
 d’’
t=d’
d
 w=(0,m-1)

Fig. 2

Now we claim that [u]Θ and [v]Θ belong to J(L)= J(D/Θ). Their role is
symmetric, so it suﬃces to deal with [u]Θ. Suppose, by way of contradiction,
that [u]Θ is not join-irreducible. Then there are a, b ∈ D such that [u]Θ =
[a]Θ ∨ [b]Θ = [a ∨ b]Θ but [a]Θ < [u]Θ and [b]Θ < [u]Θ, cf. Figure 2. (Although
Figure 2 does not reﬂect the full generality, Θ is at least as large as indicated

52 Gábor CZÉDLI, E. Tamás SCHMIDT

by dotted lines.) Let c = a ∨ b.Since [a]Θ < [u]Θ and [b]Θ < [u]Θ,we
conclude that a, b, c ∈↓h.Let c ≺ c′ ≺ c′′ ≺··· denote the unique maximal
chaininthe interval [c, c ∨ v] ⊆↓h,and let d = u ∨ c, d
′ = u ∨ c′, d
′′ =
u ∨ c′′,... be the corresponding chain in the interval [d, 1]. Now, computing
modulo Θ,for x ∈ [u, d] we have x = u ∨ x ≡ c ∨ x = d = u ∨ c ≡ c ∨ c = c.
Further, d
′ = d ∨ c′ ≡ c ∨ c′ = c′, d
′′ = d ∨ c′′ ≡ c ∨ c′′ = c′′,etc. This
means that each element of [u, 1] is congruent to some element in ↓h modulo Θ.
Therefore, by the Third Isomorphism Theorem (cf. e.g., Thm. 6.18 in Burris and
Sankappanavar [5]), (L, ∨) is isomorphic to (↓h)/Ψ where Ψ is the restriction
of Θ to ↓h. However, this contradicts the minimality of m + n. We have seen
that [u]Θ and [v]Θ are join-irreducible. [u]Θ = [0]Θ is impossible, for otherwise
L would clearly be a chain Finally, [u]Θ and [v]Θ are distinct, for otherwise
[u]Θ = [u]Θ ∨ [v]Θ=[u ∨ v]Θ=[1]Θ, a contradiction.
Now, we claim that
(
(0,i − 1), (0,i)
) /∈ Θ for i =1,... m. (2)

By way of contradiction, suppose the opposite for some ﬁxed i.Let Φ be the
semilattice congruence of D whose two-element blocks are the {(j, i − 1), (j, i)},
j =0, 1,... ,n, and all other blocks are singletons. Since
(
(j, i − 1), (j, i)
) = (
(j, 0) ∨ (0,i − 1), (j, 0) ∨ (0,i)
) ∈ Θ,

we have Φ ⊆ Θ. Hence the Second Isomorphism Theorem (cf. e.g., Thm. 6.15
in [5]) gives that (L, ∨) is a homomorphic image of {0 < 1 < ··· <n}×{0 <
1 < ··· <m − 1}, which contradicts the minimality of m + n.
Now, it follows from (2) that

|↓[v]Θ|≥ m +1. (3)

If, for a ∈ D, [u]Θ ≤ [a]Θ then [a]Θ = [u ∨ a]Θ. This implies that

|↑[u]Θ|≤ m +1. (4)

We claim that ↑[u]Θ is disjoint from ↓[v]Θ. (5)

This comes easily, for in the opposite case we would have

[1]Θ = [u ∨ v]Θ=[u]Θ ∨ [v]Θ=[v]Θ ∈ J(D/Θ) = J(L),

which has been excluded previously. Now (3), (4) and (5) settle the slim case.
Finally, according to Lemma 1, the general case is obtained from the slim
case via inserting new doubly irreducible elements into the interior (understood
in geometrical sense in the Hasse diagram) of covering squares. Since ↑[u]Θ and
↑[v]Θ are chains, they include no covering square. Hence no new element is
inserted into them. I.e., the size of ↑[u]Θ and that of ↑[v]Θ remain ﬁxed while
the size of L increases. 

Frankl’s conjecture and semimodularity 53

  Excess of a lattice.

  Strong semimodular lattices and Frankl’s conjecture.

     Frankl’s conjecture is true for modular lattices, Graphs and
Combinatorics.

     Lower semimodular types of lattices: Frankl’s conjecture holds
for lower quasi-semimodular lattices.

   A Course in Universal Algebra.

 ∼

  On averaging Frankl’s conjecture for large union-closed sets

 How to derive ﬁnite semimodular lattices from distributive
lattices?

     On the scope of averaging for Frankl’s conjecture.

  Extremal set systems. Handbook of combinatorics.

   Note on the union-closed sets conjecture.

      Birkh¨auser Verlag, Basel–Stuttgart

    A note on planar semimodular lattices.

    Frankl’s conjecture for lower semimodular lattices.
 ∼

  Union-closed families.

   Frankl’s conjecture is true for lower semimodular lattices.

     School Math. Stat., Curtin Univ. Tech., Perth

     Wadsworth & Brooks/Coole, Bel-
mont, CA
