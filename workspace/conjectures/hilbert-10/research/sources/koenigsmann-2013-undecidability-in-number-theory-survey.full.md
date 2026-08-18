<!-- source: https://arxiv.org/pdf/1309.0441 | converted from PDF -->

arXiv:1309.0441v1  [math.NT]  2 Sep 2013Undecidability in number theory

Jochen Koenigsmann
Oxford

1

Contents

Introduction 3

1 Decidability, Turing machines and Gödel’s 1st Incomplete-
ness Theorem 6
1.1 Turing machines . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.2 Coding 1st-order Lring-formulas and Turing machines . . . . . 7
1.3 Proof of Gödel’s 1st Incompleteness Theorem (sketch) . . . . . 8

2 Undecidability of number rings and ﬁelds 9
2.1 The ﬁeld Qp of p-adic numbers . . . . . . . . . . . . . . . . . . 9
2.2 The Local-Global-Principle (LGP) for quadratic forms over Q 14
2.3 Julia Robinson’s deﬁnition for Z in Q and in other number ﬁelds 14
2.4 Totally real numbers . . . . . . . . . . . . . . . . . . . . . . . 16
2.5 Large algebraic extensions of Q and geometric LGP’s . . . . . 19

3 Hilbert’s 10th Problem and the DPRM-Theorem 20
3.1 The original problem and ﬁrst generalisations . . . . . . . . . 20
3.2 Listable, recursive and diophantine sets . . . . . . . . . . . . . 23
3.3 The Davis-Putnam-Robinson-Matiyasevich
(= DPRM)–Theorem . . . . . . . . . . . . . . . . . . . . . . . 24
3.4 Consequences of the DPRM-Theorem . . . . . . . . . . . . . . 26

4 Deﬁning Z in Q 27
4.1 Key steps in the proof of Theorem 4.1 . . . . . . . . . . . . . 29
4.2 More diophantine predicates in Q . . . . . . . . . . . . . . . . 33
4.3 Why Z should not be diophantine in Q . . . . . . . . . . . . . 33

5 Decidability and Hilbert’s 10th Problem over other rings 37
5.1 Number rings . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.2 Function ﬁelds . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.3 Open problems . . . . . . . . . . . . . . . . . . . . . . . . . . 40

2

Introduction

These lectures are variations on a theme that is faintly echoed in the follow-
ing loosely connected counterpointing pairs:

Euclid versus Diophantos
geometry versus arithmetic
decidability versus undecidability
Tarski versus Gödel
Hilbert versus Matiyasevich

Let me explain how.
With his Elements which in the Middle Ages was the most popular ‘book’
after the bible, Euclid laid a foundation for modern mathematics already
around 300 BC. He introduced the axiomatic method according to which
every mathematical statement has to be deduced from (very few) ﬁrst prin-
ciples (axioms) that have to be so evident that no further justiﬁcation is
required. The paradigm for this is Euclidean geometry.
It wasn’t quite so easy for arithmetic (for good reasons as we know now).
In the 3rd century AD, Diophantos of Alexandria, often considered the great-
est (if not only) algebraist of antique times, tackled what we call today dio-
phantine equations, that is, polynomial equations over the integers, to be
solved in integers. Diophantos was the ﬁrst to use symbols for unknowns, for
diﬀerences and for powers; in short, he invented the polynomial. He was the
ﬁrst to do arithmetic in its own right, not just embedded into geometry (like,
e.g., Pythagorean triples). The goal was to ﬁnd a systematic method, a pro-
cedure, an algorithm by which such diophantine equations could be solved
(like the well known formulas for quadratic equations). One of the oldest,
very eﬃcient such algorithm is the Euclidean (!) algorithm for ﬁnding the
greatest common divisor gcd(a, b) for two integers a, b. This is a diophantine
problem: for any intergers a, b, c,

c = gcd(a, b) ⇔
 



 the three diophantine equations
cu = a, cv = b and c = ax + by
are solvable

(for even more surprising examples of mathematical problems that are dio-
phantine problems ‘in disguise’, see section 3.4).

3

In his 10th problem from the famous list of 23 problems presented to
the Congress of Mathematicians in Paris in 1900, David Hilbert, rather than
asking for an algorithm to produce solutions to diophantine equations, asked
for a more modest algorithm that decides whether or not a given diophantine
equation has a solution. In modern logic terminology, such an algorithm
would mean that the existential 1st-order theory of Z (in the language of
rings, Lring := {+, ×; 0, 1}) would be decidable (cf. section 3.1).
It would have been even more challenging — and quite in Hilbert’s spirit
— to show that the full 1st-order theory of Z, often simply called arithmetic,
would be decidable. However, in 1931, Gödel showed in the ﬁrst of his two
Incompleteness Theorems that this is not the case: no algorithm can answer
every arithmetic YES/NO-question correctly. It is called ‘Incompleteness
Theorem’ because it says that every eﬀectively (= algorithmically) producible
list of axioms true in Z is incomplete, i.e., cannot axiomatize the full 1st-order
theory of Z (section 1).
This undecidability result generalises to other number theoretic objects,
like all number ﬁelds (= ﬁnite extensions of Q) and their rings of integers, by
showing — following Julia Robinson — that Z is 1st-order deﬁnable in any
of these (section 2.3). The key tools are the ﬁeld Qp of p-adic numbers (2.1)
and the Hasse-Minkowski Local-Gobal-Principle for quadratic forms (2.2).
In contrast, around the same time as Gödel’s Incompleteness Theorem,
Tarski showed that the other classical mathematical discipline, geometry
(at least elementary geometry), is decidable; this holds true not only for
Euclidean geometry, but for all of algebraic geometry where, when translated
into cartesian coordinates, geometric objects don’t necessarily obey linear or
quadratic equations, but polynomial equations of arbitrary degree over R or
C: The full 1st-order theory of R (and hence that of C) is decidable.
1

There is a whole zoo of interesting natural intermediate rings between Z
and C (or rather between Z and the ﬁeld ̃Q of complex algebraic numbers).
To explore the boundaries within this zoo of species that belong to the de-
cidable world (like ̃Q, or the ﬁeld Q
alg
p := Qp ∩ ̃Q of p-adic algebraic numbers

1Even though Tarski may be better known for his decidability results than his un-
decidability results, one should point out that his ‘Undeﬁnability Theorem’ (1936) that
arithmetical truth cannot be deﬁned in arithmetic is very much in the spirit of Gödel’s
Incompleteness Theorems (in fact, it was discovered independently by Gödel while prov-
ing these). Tarski also proved undecidability of various other ﬁrst-order theories, like,
e.g., abstract projective geometry. This may put our very rough initial picture of the ﬁve
counterpointing pairs into a more accurate historical perspective.

4

or the ﬁeld of totally real numbers or the ring ̃Z of all algebraic integers) and
those on the undecidable side (like number rings or number ﬁelds or the ring
of totally real integers) is a fascinating task with more open questions than
answers (sections 2.4 and 2.5).
With the full 1st-order theory of Z being undecidable, there still might
be an algorithm to solve Hilbert’s 10th Problem, i.e., an eﬀective decision
procedure for the existential 1st-order theory of Z. That this is also not
the case is the celebrated result due to Martin Davis, Hilary Putnam, Ju-
lia Robinson and Yuri Matiyasevich (sometimes, for short, referred to as
‘Matiyasevich’s Theorem’ as his contribution in 1970 was the last and per-
haps most demanding): Hilbert’s 10th Problem is unsolvable — no algorithm
can decide correctly for all diophantine equations whether or not they have
integer solutions (section 3).
Maybe the most prominent open problem in the ﬁeld is the question
whether Hilbert’s 10th Problem can be solved over Q, i.e., whether there is
an algorithm deciding solvability of diophantine equations with solutions in
Q. If we had an existential deﬁnition of Z in Q (which is still open) the
answer would again be no because then Hilbert’s original 10th Problem over
Z would be reducible to that over Q, and an algorithm for the latter would
give one for the former, contradicting Matiyasevich’s Theorem.
Instead, in section 4, we reproduce the author’s universal deﬁnition of Z in
Q which, at least in terms of logical complexity, comes as close to the desired
existential deﬁnition as one could get so far (4.1) and, modulo either of two
conjectures from arithmetic geometry, as one ever possibly gets: assuming
Mazur’s Conjecture or the Bombieri-Lang Conjecture, there is no existential
deﬁnition of Z in Q (4.3).
In section 5 we brieﬂy discuss the question of full/existential decidability
for several other important rings, not all arising from number theory.
In these notes we do not aim at an encyclopedic survey of what has been
achieved in the area, nor do we provide full detailed proofs of the theorems
treated (each proof ought to be followed by an exercise: ‘ﬁll in the gaps ...’).
We rather try to point to the landmarks in the ﬁeld and their relative position,
to allow glimpses into the colourful variety of beautiful methods developed
for getting there. Many (often, but not always long-standing) open problems
are mentioned to whet the appetite, while the exercises provide working
experience with some of the tools introduced. What makes the topic really
attractive, especially for graduate students, is that most results don’t use very
heavy machinery, are elementary in this sense, though, obviously, people did

5

have very good ideas.
I would like to express my warmest thanks to Dugald Macpherson and
Carlo Toﬀalori for giving me the opportunity to hold these lectures in the
superb setting of Cetraro, and to the enthusiastic audience for their immense
interest, their encouraging questions and their critical remarks. I am also
very grateful to the anonymous referee and the editors for their most valuable
suggestions for improving on an earlier version of these notes.

1 Decidability, Turing machines and Gödel’s
1st Incompleteness Theorem

In this lecture we would like to sketch the proof of the ﬁrst of Gödel’s cel-
ebrated two Incompleteness Theorems. Denoting by N := ⟨N; +, ·; 0, 1⟩ the
natural numbers as Lring-structure, where Lring := {+, ·; 0, 1}, and by Th(N )
its 1st-order Lring-theory, a weak version of the theorem is the following

Theorem 1.1 ([Göd31]). Th(N ) is undecidable.

I.e., there is no algorithm which, on INPUT any Lring-sentence α, gives

OUTPUT { YES if α ∈ Th(N ), i.e., N |= α
NO otherwise

In order to make this statement precise, we will deﬁne the notion of an
algorithm using Turing machines. There have been many alternative deﬁni-
tions (via register machines, λ-calculus, recursive functions etc.) all of which
proved to be equivalent. And, indeed, it is the credo of what has come to
be called Church’s Thesis that, no matter how we pin down an exact (and
sensible) notion of algorithm, it is going to be equivalent to the existing ones.
Whether or not one should take this as more than an empirical fact about
the algorithms checked sofar, is an interesting philosophical question.

1.1 Turing machines

A Turing machine T over a ﬁnite alphabet A = {a1, a2, . . . , an} consists of a
tape · · · ai aj ak · · ·

6

with inﬁnitely many cells, each of which is either empty (contains the empty
letter a0) or contains exactly one ai (1 ≤ i ≤ n).
In each step the tape head is on exactly one cell and performs exactly one
of the following four operations:

ai type ai on the working cell (0 ≤ i ≤ n)

r go to the next cell on the right

l go to the next cell on the left

s stop

The program (action table) of T is a ﬁnite sequence of lines of the shape

z a b z′

where a ∈ A ∪ {a0}, where b is one of the above operations, and where z, z′

are from a ﬁnite set Z = {z1, . . . , zm} of states.
The program determines T by asking T to interpret

z a b z′

as ‘if T is in state z and the tape head reads a then do b and go to state z′’.
T may stop on a given INPUT after ﬁnitely many steps (and then the
OUTPUT is what’s on the tape then) or it runs forever (with no OUTPUT
given). A decision algorithm always stops, by deﬁnition.

1.2 Coding 1st-order Lring-formulas and Turing machines

Let A = {+, ·; 0, 1; .
=, (, ), ¬, →, ∀, v,
′ } be the ﬁnite alphabet for 1st-order
arithmetic, thinking of the variable vn as the string v′′...′ of length 1 + n, and
assign to the ﬁnitely many elements of the disjoint union

A ∪ Z ∪ {a0, r, l, s}

distinct positive integers (their codes). Code formulas via unique prime de-
composition, e.g., if ¬, 0, .
=, 1 have codes 2, 4, 1, 3 resp., the formula
ρ = ¬0 .
= 1 has code
 ⌈ρ⌉ = 22 · 34 · 51 · 73 = 555660

and can be recovered from it.
Similarly, one can deﬁne a unique code ⌈T⌉ for (the program of) each
Turing machine T by coding the sequence of lines in the program.

7

1.3 Proof of Gödel’s 1st Incompleteness Theorem (sketch)

Suppose, for the sake of ﬁnding a contradiction, that there is a Turing ma-
chine T which decides for any Lring-sentence α whether N |= α or N ̸|= α.
Then there is an arithmetic function fT : N → N describing T such that for
any Lring-sentence α,
 f (⌈α⌉) = { 1 if N |= α
2 if N ̸|= α

Here we call a function f : N → N arithmetic if there is an Lring-formula
φ(v0, v1) such that for any n, m ∈ N,

f (n) = m ⇔ N |= φ(n, m).

(φ is then called a deﬁning formula for f .) That there is such a deﬁning
formula φT for fT comes from the 1st-order fashion in which Turing programs
come along; the logical connectives and quantiﬁers translate into arithmetic
operations.
So for any Lring-sentence α we have

N |= φT(⌈α⌉, 1) ⇐⇒ N |= α,

which means that we can ‘talk’ about the truth of a sentence about N inside
N , and so we are in a position to simulate the liar’s paradox: Deﬁne g : N →
N such that for all Lring-formulas ρ(v0)

g(⌈ρ⌉) = { 1 if N |= ¬ρ(⌈ρ⌉)
2 if N |= ρ(⌈ρ⌉)

Then g is arithmetic, say with deﬁning formula ψ, so that

N |= ψ(⌈ρ⌉, 1) ⇔ N |= ¬ρ(⌈ρ⌉).

Applied to the formula ρ0(v0) := ψ(v0, 1) this gives

N |= ρ0(⌈ρ0⌉) ⇔ N |= ¬ρ0(⌈ρ0⌉),

the contradiction we were looking after.

Since there is an eﬀective algorithm (a Turing machine) listing the Peano
axioms, and since Th(N ) is complete we get the following immediate

8

Corollary 1.2. The Peano axioms don’t axiomatise all of Th(N ).

Nevertheless, a great many theorems about N do follow from the Peano
axioms, and there has been an exciting controversy launched by Angus Mac-
intyre as to whether Fermat’s Last Theorem belongs (cf. the Appendix in
[Mac11]).

Another immediate consequence is the following

Corollary 1.3. Th(⟨Z; +, ·; 0, 1⟩) is undecidable.

Proof: Otherwise, as the natural numbers are exactly the sums of four
squares of integers, Th(N ) would be decidable.

2 Undecidability of number rings and ﬁelds

2.1 The ﬁeld Qp of p-adic numbers

The ﬁeld of p-adic numbers was discovered, or rather invented, by Kurt
Hensel over 100 years ago and has ever since played a crucial role in number
theory. It is, like the ﬁeld R of real numbers, the completion of Q, though not
w.r.t. the ordinary (real) absolute value, but rather w.r.t. a ‘p-adic’ analogue
(for each prime p a diﬀerent one). This allows to bring new (p-adic) analytic
methods into number theory and to reduce some problems about number
ﬁelds (which are so-called ‘global’ ﬁelds) to the ‘local’ ﬁelds R and Qp. This
is of particular interest in our context because, as we will see, number ﬁelds
are undecidable, whereas the ﬁelds of real or p-adic numbers are decidable.
So whenever a number theoretic problem is reducible to a problem about the
local ﬁelds R and Qp (one then says that the problem satisﬁes a Local-Global-
Principle) the number theoretic problem becomes decidable as well.
2

2The use of the terms ‘local’ and ‘global’ which one more typically encounters in analysis
or in algebraic geometry hints at a deep analogy between number theory and algebraic
geometry, more speciﬁcally between number ﬁelds (i.e. ﬁnite extensions of Q, the global
ﬁelds of characteristic 0) and algebraic function ﬁelds in one variable over ﬁnite ﬁelds (i.e.,
ﬁnite extensions of the ﬁeld Fp(t) of rational functions over Fp, the global ﬁelds of positive
characteristic). It is one of the big open problems in model theory whether or not the
positive characteristic analogue of Qp, i.e., the local ﬁeld Fp((t)) of (formal) Laurent series
over Fp, is decidable.
 9

Let us ﬁx a rational prime p. The p-adic valuation vp on Q is deﬁned by
the formula

vp(pr · m
n ) = r for any r, m, n ∈ Z with p ̸ | m · n ̸= 0,

with vp(0) := ∞. It is easy to check that this is a well deﬁned valuation (for
background in valuation theory cf. [Dri13] in this volume or [EP05]). The
corresponding valuation ring is

Z(p) = {q ∈ Q vp(q) ≥ 0} = { a
b a ∈ Z, p ̸ | b ∈ Z \ {0}}

with maximal ideal

pZ(p) = {q ∈ Q vp(q) > 0} = { a
b p | a ∈ Z, p ̸ | b ∈ Z \ {0}} .

vp induces the p-adic norm | . |p on Q given by

| q |p:= p−vp(q) for q ̸= 0,

with | 0 |p:= 0. Observe that the sequence p, p2, p3, . . . converges to 0 w.r.t.
| . |p.
We can now deﬁne the ﬁeld Qp of p-adic numbers as the completion of
Q w.r.t. | . |p, i.e., the ﬁeld obtained by taking the quotient of the ring of
(p-adic) Cauchy sequences by the maximal ideal of (p-adic) zero sequences
(version 1). Equivalently (version 2), one may deﬁne

Qp :=
 {

α =
 ∞∑

ν=n aνpν n ∈ Z, aν ∈ {0, 1, . . . , p − 1}
}

as the ring of formal Laurent series in powers of p with coeﬃcients from
0, 1, . . . , p − 1, where addition is componentwise modulo p starting with the
lowest non-zero terms and carrying over whenever aν + bν ≥ p (so if this hap-
pens for the ﬁrst time at ν the (ν + 1)-th coeﬃcient becomes 1 + aν+1 + bν+1
modulo p etc.) — like adding decimals, but from the left. Similarly, multi-
plication is like multiplying polynomials in the ‘unknown’ p with coeﬃcients
modulo p, and again carrying over whenever necessary.

Exercise 2.1. Show that −1 = ∑∞
ν=0(p − 1)pν and 1
1−p = 1 + p + p2 + . . ..

10

Given this presentation of p-adic numbers, one deﬁnes the p-adic valuation
on Qp, again denoted by vp, for any non-zero α ∈ Qp as

vp(α) := min{ν | aν ̸= 0}.

This is a prolongation of the p-adic valuation on Q; its value group is, obvi-
ously, still Z, and its valuation ring is

Zp := Ovp = {α ∈ Qp vp(α) ≥ 0} =
 { ∞∑

ν=0 aνpν aν ∈ {0, 1, . . . , p − 1}
}
 ,

the ring of p-adic integers with maximal ideal

pZp = {α ∈ Qp vp(α) > 0} =
 { ∞∑

ν=1 aνpν aν ∈ {0, 1, . . . , p − 1}
}
 ,

and with residue ﬁeld

Zp/pZp ∼= Z(p)/pZ(p) ∼= Z/pZ = Fp.

By deﬁnition, Q is dense in Qp w.r.t. the p-adic topology induced by (the
two) vp, and Z is dense in Zp: in fact, Zp is the completion of Z (w.r.t. the
norm induced by | . |p on Z).
Yet another way to think about the ring of p-adic integers (version 3)
is to view it as an inverse limit

Zp = lim
← Z/pnZ

of the rings Z/pnZ w.r.t. the canonical projections Z/pnZ → Z/pmZ for
m ≤ n. Note that, for n > 1, the rings Z/pnZ have zero divisors whereas the
projective limit Zp becomes an integral domain (with Qp as ﬁeld of fractions).

Exercise 2.2. Prove the equivalence of versions 1, 2, 3.

One of the key facts about Zp is Hensel’s Lemma which uses the analytic
tool of Newton approximation to ﬁnd a precise zero of a polynomial, given
an approximate zero. For α ∈ Zp, let us denote its image under the canonical
residue map Zp → Fp by α. Similarly, we will write f for the image of the
polynomial f ∈ Zp[X] under the coeﬃcientwise extension of the residue map
to Zp[X] → Fp[X].
 11

Lemma 2.3 (Hensel’s Lemma). Simple zeros lift: Let f ∈ Zp[X] be a
monic polynomial and assume α ∈ Zp is such that α is a simple zero of f
(i.e., f (α) = 0 ̸= f ′(α)). Then there is some β ∈ Zp with f (β) = 0 and
β = α.

Exercise 2.4. The proof is an adaptation of the proof in van den Dries’
contribution to this volume, section 2.2, the details being left to the reader as
an exercise.

Example If p > 2 then every 1-unit, that is, every x ∈ 1 + pZp is a square:
consider the polynomial f (X) = X 2 − x and let α = 1; these satisfy the
assumptions of Hensel’s Lemma, and so f has a zero β (with β = 1); hence
x = β2.

Similarly, if one denotes by ζn a primitive n-th root of unity, then ζp−1 ∈ Zp:
the polynomial X p−1 − 1 has (p − 1) distinct linear factors over Fp, and so,
by Hensel’s Lemma, the same holds in Zp.
Thus we can write the multiplicative group of Qp as a direct product of
three ‘natural’ subgroups:

Q
×
p = pZ · ⟨ζp−1⟩ · (1 + pZp)

From this one immediately reads oﬀ that, for p > 2, there are precisely four
square classes (elements in Q
×
p /(Q
×
p )2), represented by

1, p, ζp−1 and pζp−1.

As a consequence, one obtains the following well-known 1st-order Lring-
deﬁnition of Zp in Qp:

Zp = {x ∈ Qp | ∃y ∈ Qp such that 1 + px
2 = y2}.

Exercise 2.5. Show that, for p = 2, a similar deﬁnition works with squares
replaced by cubes.

Exercise 2.6. Show that, for p a prime ≡ 3 mod 4,

Zp = {t ∈ Qp | ∃x, y, z ∈ Qp such that 2 + pt
2 = x
2 + y2 − pz2},

and, if p ≡ 1 mod 4 and q ∈ N a quadratic non-residue mod p,

Zp = {t ∈ Qp | ∃x, y, z ∈ Qp such that 2 + pqt
2 = x
2 + qy2 − pz2}.

12

With the valuation ring, also the maximal ideal, the residue ﬁeld, the
group of units, the value group and the valuation map all become inter-
pretable in Lring. Thus, the axiomatization given below can be phrased
entirely in Lring-terms. Now here is a milestone in the model theory of Qp:

Theorem 2.7 (Ax-Kochen/Ershov). Th(Qp) is decidable. It is eﬀectively
axiomatized by the following axioms:

• vp is henselian

• the residue ﬁeld of vp is Fp

• the value group Γ is a Z-group, i.e., Γ ≡ ⟨Z; +; 0; <⟩ which can be
axiomatized by saying that there is a minimal positive element and that
[Γ : nΓ] = n for all n

• vp(p) is minimal positive

The proof, again, is similar to the proof of the other Ax-Kochen/Ershov
Theorem presented in section 6 of van den Dries’ contribution [Dri13] to this
volume.
Fields elementarily equivalent to Qp are called p-adically closed3.

Exercise 2.8. Check that ﬁelds which are relatively algebraically closed in a
p-adically closed ﬁeld are again p-adically closed.

So, for example, the ﬁeld
 Q
alg
p := Qp ∩ ̃Q

of algebraic p-adic numbers is p-adically closed (we use the notation ̃K for
the algebraic closure of K). Note that Q
alg
p is countable while Qp isn’t.

Exercise 2.9. Show that K := Qp((Q)) (in the notation of [Dri13], after
Deﬁnition 3.3, this is Qp((t
Q))) is p-adically closed and solve the mystery
that, on the one hand, K and Qp are elementarily equivalent, on the other,
they both have a henselian valuation with the same residue ﬁeld Qp, but with
non-elementarily equivalent value groups (Q for K and {0} for Qp).

3Sometimes the term p-adically closed refers, more generally, to ﬁelds elementarily
equivalent to ﬁnite extensions of Qp — cf. [PR84].

13

2.2 The Local-Global-Principle (LGP) for quadratic forms
over Q

Let q(X1, . . . , Xn) be a quadratic form over Q, i.e., a homogeneous polyno-
mial of degree 2 in Q[X1, . . . , Xn]. An element a ∈ Q is said to be represented
by q if there is x = (x1, . . . , xn) ∈ Q
n such that a = q(x).

Theorem 2.10 (Hasse-Minkowski-Theorem). A rational a is represented by
q in Q if and only if a is represented by q in all Qp and in R.

The proof is trivial for n = 1, it uses the so-called geometry of numbers
for n = 2, it requires delicate case distinctions ‘modulo 8’ for n = 3 and
n = 4, and then follows more easily by general quadratic form tricks for
n > 4. (cf. [O’Me73], for an alternative proof using Hilbert symbols and
quadratic reciprocity cf. [Ser73]).
The above LGP-principle is eﬀective: by a simple linear transformation
any quadratic form can be brought into diagonal form:

q(X1, . . . , Xn) = a1X 2
1 + · · · + anX 2
n

Then the only primes p where representability of a by q in Qp need to be
checked are p = 2, p = ∞ (where Q∞ := R), those p where vp(a) ̸= 0, and
those where vp(ai) ̸= 0 for some i ≤ n. So only these ﬁnitely many primes
need checking and, since all the Qp and R are decidable, the whole procedure
is eﬀective.
For cubic forms no such LGP holds: By an example of Selmer ([Sel51]),
5 is represented by the cubic form

3X 3 + 4Y 3

in R and in every Qp, but not in Q.

2.3 Julia Robinson’s deﬁnition for Z in Q and in other
number ﬁelds

Julia Robinson’s contribution to questions of decidability in number theory
is enormous. Her ﬁrst big result in this direction is the 1st-order deﬁnability
of Z (or N) in Q from which the undecidability of Th(Q) immediately follows
(1949), given Gödel’s 1st Incompleteness Theorem. 10 years later she ex-
tended this to arbitrary number ﬁelds. Later she became heavily involved in

14

Hilbert’s 10th Problem (section 3). The very appealing documentary ‘Julia
Robinson and Hilbert’s Tenth Problem’ by George Csicsery came out in 2010
([Csi10]).
To give Julia Robinson’s explicit deﬁnition of Z in Q, let us introduce the
following formulas: for a, b ∈ Q
× and k ∈ Q, let

φ(a, b, k) := ∃x, y, z(2 + abk2 + bz2 = x
2 + ay2)

and let, for n ∈ Q,

ψ(n) := ∀a, b ̸= 0 [{φ(a, b, 0) ∧ ∀k⟨φ(a, b, k) → φ(a, b, k + 1)⟩} → φ(a, b, n)]

Theorem 2.11 ([Rob49]). For any n ∈ Q,

Q |= ψ(n) ⇔ n ∈ Z.

Proof: The easy direction ‘⇐’ follows, for n ∈ N, by the principle of
induction, and for n ∈ Z, from the observation that ψ(n) ⇔ ψ(−n), because
n occurs only squared in ψ.
For the non-trivial direction one ﬁrst shows, using Exercise 2.6 and The-
orem 2.10, that, for a prime p ≡ 3 mod 4 and k ∈ Q,

φ(1, p, k) ⇔ vp(k) ≥ 0 and v2(k) ≥ 0,

and that, for primes p, q with p ≡ 1 mod 4 and q a quadratic non-residue
mod p, φ(q, p, k) ⇔ vp(k) ≥ 0 and vq(k) ≥ 0.

So, in either case, the {. . .}-bit in ψ is satisﬁed, and, thus, for ψ(n) to hold
we must have φ(1, p, n) for any prime p ≡ 3 mod 4 resp. φ(q, p, n) for any
pair p, q of primes in the second case. But then, by the equivalences above,
vp(n) ≥ 0 for any prime p, and so n ∈ Z.

Corollary 2.12. Th(Q) is undecidable.

Let us recall, that number ﬁelds are ﬁnite extensions of Q, and that the
ring of integers in K, denoted by OK, is the integral closure of Z in K, i.e.,
the set of elements of K satisfying a monic polynomial with coeﬃcients in Z.

Theorem 2.13 ([Rob59]). For any number ﬁeld K, OK is deﬁnable in K
and Z is deﬁnable in OK. In particular, Th(OK ) and Th(K) are undecidable.

15

Proof: The deﬁnition of OK in K proceeds along similar lines as that of
Z in Q, especially as the LGP for quadratic forms holds in arbitrary number
ﬁelds.
That N is deﬁnable in OK uses the fact that for all non-zero f ∈ OK
there are only ﬁnitely many a ∈ OK such that

a + 1 | f ∧ . . . ∧ a + l | f,

where l = [K : Q].
Now deﬁne, for a, f, g, h ∈ OK,

ρ(a, f, g, h) := f ̸ .
= 0 ∧ (a + 1 | f ∧ . . . ∧ a + l | f ) ∧ 1 + ag | h

Then, for any n ∈ OK,

n ∈ N ⇔ ∃f, g, h [ρ(0, f, g, h) ∧ ∀a{ρ(a, f, g, h) → ⟨ρ(a + 1, f, g, h) ∨ a .
= n⟩}]

To prove the easy direction ‘⇐’, assume n satisﬁes the right hand side. By
the fact above, there are only ﬁnitely many a with ρ(a, f, g, h). The inductive
form of the deﬁnition ensures that ρ(0, f, g, h), ρ(1, f, g, h), . . . terminating
only for a = n. Therefore, n must be a natural number.
For the converse direction ‘⇒’, assume n ∈ N. It suﬃces to ﬁnd f, g, h ∈
OK such that
 ρ(a, f, g, h) ↔ a = 0 ∨ a = 1 ∨ . . . ∨ a = n.

Put f := (n + l)! and let S := {a ∈ OK | a + 1 | f ∧ . . . ∧ a + l | f }. Then, by
the fact above, S is ﬁnite and we can ﬁnd some g ∈ N large enough so that,
for any two distinct a, b ∈ S, a − b | g and, for any non-zero a ∈ S, 1 + ag ̸ | 1.
Then, for any distinct a, b ∈ S, 1 + ag and 1 + bg are relatively prime (if there
is a prime ideal of OK containing both 1 + ag and 1 + bg then it contains
(a − b)g, hence g2 and so g, but it cannot contain both g and 1 + ag).
Now put h = (1 + g)(1 + 2g) · · · (1 + ng). Then ρ(a, f, g, h) is satisﬁed for
a = 1, . . . , n. If, however, there is some other a ∈ S then 1 + ag is not a unit
and is prime to h. Therefore, 1 + ag ̸ | h and ρ(a, f, g, h) does not hold.

2.4 Totally real numbers

There are many inﬁnite algebraic extensions of Q (sometimes misleadingly
called ‘inﬁnite number ﬁelds’) which are also known to be undecidable. In

16

fact, most of them are: there are only countably many decision algorithms,
but uncountably many non-isomorphic, and hence, in this case, non-elementarily
equivalent algebraic extensions of Q. To give an explicit example, let A be an
undecidable (= non-recursive, cf. section 3.2) subset of the set of all primes
and let K := Q({√p | p ∈ A}).

Then (the 1st-order theory of) K, and hence also OK, is undecidable: oth-
erwise A = {p ∈ N | p is prime and ∃x ∈ K p = x
2} would be decidable.
While this example seems artiﬁcial, there is a number of ‘natural’ inﬁnite
algebraic extensions of Q for which it makes sense to ask about decidability
of the ﬁeld or of its ring of integers. We will treat some of these in this
section and the next, and we will list some nice open problems in section
5.3. The ﬁeld of totally real numbers is special in that its ring of integers is
undecidable whereas the ﬁeld is decidable.
The ﬁeld of totally real numbers is deﬁned to be the maximal Galois
extension T of Q inside R. T is an inﬁnite algebraic extension of Q, the
intersection of all real closures of Q (inside a ﬁxed algebraic closure ̃Q). T
can also be thought of as the compositum of all ﬁnite extensions F/Q for
which all embeddings F ֒→ C are real.
As for ﬁnite extensions of Q one deﬁnes OT , the ring of integers of T , as
the integral closure of Z in T .

Theorem 2.14 ([Rob62]). Th(OT ) is undecidable.

Let us separate the key ingredients of the proof in the two lemmas below.

Lemma 2.15. Let R be an integral domain with N ⊆ R. Let F ⊆ ℘(R)
be a family of subsets of R which is arithmetically deﬁned (or uniformly
parametrised), say, by an Lring-formula φ(x; y1, . . . , yk), i.e., for any F ⊆ R,

F ∈ F ⇔ ∃y ∈ Rk ∀x ∈ R[x ∈ F ↔ φ(x; y)].

Assume that all F ∈ F are ﬁnite and each initial segment {0, 1, . . . , n} of N
is in F . Then N is deﬁnable in R.

Proof: For any n ∈ R,

n ∈ N ⇔ ∃y ∈ Rk [φ(0, y) ∧ ∀x{φ(x, y) → ⟨φ(x + 1, y) ∨ x = n⟩}] .

17

For a, b ∈ T , we use the notation ‘a ≪ b’ to indicate that a < b for any
ordering < on T . Note that this is expressible by an Lring-formula:

a ≪ b ⇐⇒ a ̸= b ∧ ∃x b = a + x
2

(totally positive elements are always sums of squares, and, in T , every sum
of squares is a square).

Lemma 2.16.

min{M ∈ R | ∃∞-ly many t ∈ OT s.t. 0 ≪ t ≪ M} = 4

Proof: That there are inﬁnitely many t ∈ OT with 0 ≪ t ≪ 4 is easy: for
any n > 1 and any n-th root ζn of unity, tn := 2 + ζn + ζ −1
n has this property.
Conversely, any t with this property is one of these tn: This follows
from Kronecker’s 1857 Theorem ([Kro57]) that algebraic integers all of whose
conjugates have absolute value ≤ 1 are roots of unity: if α = α1, α2, . . . , αn
are all the conjugates of such an algebraic integer α, then, for any k, the
coeﬃcients ak,s of the polynomial

fk(X) := (X − αk
1) · · · (X − αk
n) = X n + ak,n−1X n−1 + . . . + ak,0

satisfy | ak,s |≤ ( n
s
 ); being integers as well, there can only be ﬁnitely many

such ak,s, hence only ﬁnitely many such fk, and so αk = αl for some k < l,
making α an (l − k)-th root of unity.
From this one obtains that totally real integers all of whose conjugates
have absolute value ≤ 2 are of the shape α + α−1 for some root of unity α:
let β ∈ OT be such an element with conjugates β = β1, . . . , βn and let

α = β
2 +
 √ β2

4 − 1;

then α is an algebraic integer with α2 − βα + 1 = 0 and any conjugate α′ of
α (over Q) satisﬁes α′2 − βiα′ + 1 = 0 for some i; as | βi |≤ 2 (and, in fact,
w.l.o.g., < 2) the two roots of this equation are the two complex conjugates
of α′, hence
 | α′ |2= β2
i
4 + 1 − β2
i
4 = 1,

so, by Kronecker’s Theorem, α is a root of unity and β = α + α−1 is of the
indicated shape.
 18

Now the Lemma follows easily.

Proof of Theorem 2.14: The family F ⊆ ℘(OT ) deﬁned by

φ(x; p, q) ⇔ 0 ≪ qx ≪ p ∧ p ≪ 4q

contains, by Lemma 2.16, only ﬁnite sets, but arbitrarily large ones. Hence,
by a variant of Lemma 2.15, N is deﬁnable in OT .

2.5 Large algebraic extensions of Q and geometric LGP’s

As in the previous section, we denote the ﬁeld of totally real numbers by T .
In the literature, it is also often denoted by Q
tot−r or Q
t.r..

Theorem 2.17. T is pseudo-real-closed (‘PRC’), i.e. T satisﬁes the follow-
ing geometric LGP: for each (aﬃne) algebraic variety V /T ,

V (T ) ̸= ∅ ⇔ V (R) ̸= ∅ for all real closures R of T.

The theorem was ﬁrst proved by Moret-Bailly ([Mor89]) using heavy ma-
chinery from algebraic geometry, with a more elementary proof given later
by Green, Pop and Roquette ([GPR95]).
By explicitly describing the structure of the absolute Galois group GT
of T , that is, the Galois group of the algebraic closure ̃T = ̃Q of T over T ,
Fried, Völklein and Haran showed in [FVH94], using the above theorem:

Theorem 2.18. Th(T ) is decidable.

The axiomatization expresses the PRC property in elementary terms (it
is not at all obvious how to do this, but it had long been established, e.g., in
[Pre81]) as well as the fact that GT is the free (proﬁnite) product of all GR,
where R runs through a set of representatives of the conjugacy classes of all
real closures of T (so each GR ∼= Z/2Z). The latter can be ‘axiomatized’ via
so-called embedding problems in a similar fashion as, by a famous Theorem of
Iwasawa, free proﬁnite groups of inﬁnite countable rank can be characterized.
An interesting immediate consequence of this tension between T being
decidable and OT not, is the following:

Corollary 2.19. OT is not deﬁnable in T .

The decidability of (the 1st-order theory of) T implies that the ﬁeld
T (√
−1) is decidable as well. No answer is known to the following:

19

Question 2.20. Is OT (
√−1) decidable?

A p-adic analogue of Theorem 2.17 and 2.18 was given by Pop in [Pop96]:
One deﬁnes the ﬁeld Q
tot−p, the ﬁeld of totally p-adic numbers, as the maxi-
mal Galois extension of Q inside Qp, that is, the intersection of all conjugates
of Q
alg
p over Q. Pop showed that Q
tot−p is pseudo-p-adically-closed, i.e. it sat-
isﬁes an analogous LGP (with real closures replaced by p-adic closures), and
that the absolute Galois group is similarly well behaved. As a consequence,
Q
tot−p is decidable. We have no answer to the following

Question 2.21. Is OQtot−p decidable?

Let us close this section by mentioning another celebrated LGP, that is,
Rumely’s Local-Global-Principle ([Rum86]) which concerns the ring ̃Z of all
algebraic integers, i.e., the integral closure of Z in the algebraic closure ̃Q of
Q:

Theorem 2.22. Let V be an aﬃne variety deﬁned over ̃Z. Then

V (̃Z) ̸= ∅ ⇔ V (O) ̸= ∅ for all valuation rings O of ̃Q.

Using this, van den Dries ([Dri88]) showed the following Theorem via
some quantiﬁer elimination, Prestel and Schmid ([PS90]) showed it via an
explicit axiomatization:

Theorem 2.23. Th(̃Z) is decidable.

Note that ̃Z is not deﬁnable in ̃Q (by quantiﬁer elimination in ACF0,
every deﬁnable subset of ̃Q is ﬁnite or coﬁnite), so there is no cheap way of
proving the above Theorem.
For a survey on geometric LGP’s and many more results in this direction
cf. [Dar00].

3 Hilbert’s 10th Problem and the DPRM-Theorem

3.1 The original problem and ﬁrst generalisations

In 1900, at the Conference of Mathematicians in Paris, Hilbert presented his
celebrated and inﬂuential list of 23 mathematical problems ([Hil00]). One of
them is
 20

Hilbert’s 10th Problem (‘H10’) Find an algorithm which gives on INPUT
any f (X1, . . . , Xn) ∈ Z[X1, . . . , Xn]

OUTPUT { YES if ∃x ∈ Z
n such that f (x) = 0
NO else

Hilbert did not ask to prove that there is such an algorithm. He was convinced
that there should be one, and that it was all a question of producing it —
one of those instances of Hilbert’s optimism reﬂected in his famous slogan
‘wir müssen wissen, wir werden wissen’ (‘we must know, we will know’). As
it happens, Hilbert was too optimistic: after previous work since the 50’s by
Martin Davis, Hilary Putnam and Julia Robinson, in 1970, Yuri Matiyasevich
showed that there is no such algorithm (Corollary 3.7).
The original formulation of Hilbert’s 10th problem was weaker than the
standard version we have given above in that he rather asked ‘Given a polyno-
mial f , ﬁnd an algorithm ...’. So maybe one could have diﬀerent algorithms
depending on the number of variables and the degree. However, it is even pos-
sible to ﬁnd a single polynomial for which no such algorithm exists (Corollary
3.14) — this is essentially because there are universal Turing Machines.
One should, however, mention that, in the special case of n = 1, that
is, for polynomials in one variable, there is an easy algorithm: if, for some
x ∈ Z, f (x) = 0 then x | f (0); hence one only has to check the ﬁnitely many
divisors of f (0). Similarly, by the eﬀective version of the Hasse-Minkowski-
LGP (Theorem 2.10) and some extra integrality considerations, one also has
an algorithm for polynomials in an arbitrary number of variables, but of total
degree ≤ 2. And, even if there is no general algorithm, it is one of the major
projects of computational arithmetic geometry to exhibit other families of
polynomials for which such algorithms exist.
To conclude these introductory remarks let us point in a diﬀerent direc-
tion of generalizing Hilbert’s 10th Problem, namely, generalizing it to rings
other than Z: If R is an integral domain, there are two natural ways of gen-
eralizing H10:

H10/R = H10 with the 2nd occurrence of Z replaced by R
H10+/R = H10 with both occurrences of Z replaced by R

Observation 3.1. Let R be an integral domain whose ﬁeld of fractions does

21

not contain the algebraic closure of the prime ﬁeld (Fp resp. Q). Then

H10/R is solvable ⇔ Th∃+(R) is decidable
H10+/R is solvable ⇔ Th∃+(⟨R; r | r ∈ R⟩) is decidable,

where Th∃+ denotes the positive existential theory consisting of existential
sentences where the quantiﬁer-free part is a conjunction of disjunctions of
polynomial equations (no inequalities).

Note that the language on the right hand side of the 2nd line contains a
constant symbol for each r ∈ R.

Proof: ‘⇐’ is obvious in both cases. For ‘⇒’ one has to see that a disjunction
of two polynomial equations is equivalent to (another) single equation, and,
likewise, for conjunctions: By our assumption we can ﬁnd some monic g ∈
Z[X] of degree > 1 which is irreducible over R. Then, for any polynomials
f1, f2 over Z resp. R and for any tuple x over R,

f1(x) = 0 ∨ f2(x) = 0 ⇐⇒ f1(x) · f2(x) = 0
f1(x) = 0 ∧ f2(x) = 0 ⇐⇒ g( f1(x)
f2(x)) · f2(x)deg g = 0

Since in ﬁelds, inequalities can be expressed by a positive existential for-
mula (f (x) ̸= 0 ↔ ∃y f (x) · y = 1), we immediately obtain the following:

Corollary 3.2. Let K be a ﬁeld not containing the algebraic closure of the
prime ﬁeld. Then

H10/K is solvable ⇔ Th∃(K) is decidable.

In fact, the same is true for OK, the ring of integers of a number ﬁeld K:

Exercise 3.3. Show that, if K is a number ﬁeld,

OK |= ∀x[x ̸= 0 ↔ ∃y x | (2y − 1)(3y − 1)].

Deduce that Th∃(OK) = Th∃+(OK).

One of the biggest open questions in the area is

Question 3.4. Is H10/Q solvable?
 22

3.2 Listable, recursive and diophantine sets

A subset A ⊆ Z is called

• diophantine if there is some m ∈ N and some polynomial p ∈ Z[T ; X1, . . . , Xm]
such that A = {a ∈ Z | ∃x ∈ Z
m with p(a; x) = 0}

e.g., N is diophantine in Z: take p = T − X 2
1 − X 2
2 − X 2
3 − X 2
4

• listable (= recursively enumerable) if there is an algorithm (= a Turing
machine) printing out the elements of A (and only those), e.g., the set
P of primes or S := {a
3 + b
3 + c3 | a, b, c ∈ Z}

• recursive (= decidable) if there is an algorithm deciding membership in
A, e.g., N and P are recursive, about S it is not known.

It is clear that every diophantine set is listable and that every recursive set
is listable. That, conversely, every listable set is diophantine is the content
of the ‘DPRM-Theorem’ (next section).
That not every listable set is recursive follows from the following

Proposition 3.5 (The Halting Problem of Computer Science is un-
decidable). There is no algorithm to decide whether a program (with code)
p halts on INPUT x.

Proof: Otherwise deﬁne a new program H by:

H halts on input x ⇔ x does not halt on input x

(we identify x with ⌈x⌉). For x = H we are in trouble then.
Using this, we ﬁnd a listable, but non-decidable set:

A = {2p3x | p halts on input x}

It is non-decidable by the proposition, but we can list it: for x, p ≤ N print
2p3x if p halts on input x in ≤ N steps.

23

3.3 The Davis-Putnam-Robinson-Matiyasevich
(= DPRM)–Theorem

..., often for short referred to as Matiyasevich’s Theorem, is the following
remarkable

Theorem 3.6 ([Mat70], conjectured by Davis 1953, building on work of
Davis, Putnam and Robinson). Every listable subset of Z is diophantine.

Corollary 3.7. Hilbert’s 10th problem is unsolvable.

Proof: The set A at the end of the previous section is listable, hence, by
the Theorem, diophantine. So there is some m ∈ N and some polynomial
p ∈ Z[T ; X1, . . . , Xm] such that A = {a ∈ Z | ∃x ∈ Z
m with p(a; x) = 0}.
By construction, however, it is not decidable. Hence there is no algorithm
which decides, on input t ∈ Z, whether or not p(t; x) = 0 has a solution
x ∈ Z
m.

We will only give a brief history and sketch of the proof of the Theorem.
For a full account of the history see the excellent survey article [Mat00], and,
for a full self-contained proof (not always following the historic path), see
[Dav73].
Whether, in H10, we ask for solutions in Z
n or in Nn doesn’t make a
diﬀerence: as every integer is a diﬀerence of two natural numbers and as every
natural number is the sum of 4 squares of integers we can easily transform a
polynomial equation into another such that the former has integer solutions if
and only if the latter has solutions in natural numbers, and we ﬁnd a similar
transformation for the other way round. Following history (and because N
has the advantage of having a least element) we will stick to ﬁnding solutions
in N.

Theorem 3.8 ([Dav53]). If A ⊆ N is listable then A is almost diophantine,
i.e., there is a polynomial g ∈ Z[T ; X; Y, Z] such that for all a ∈ N

a ∈ A ⇔ ∃z∀y ≤ z ∃x g(a; x; y, z) = 0.

Note that every A with such a presentation, later called ‘Davis normal
form’, is listable.

Exercise 3.9. Observe that 2N is listable. Find an almost diophantine pre-
sentation.
 24

A big challenge at the time was to ﬁnd a diophantine presentation for
2N, or, more generally, for exponentiation. Julia Robinson showed that, in
order to achieve this, it suﬃces to ﬁnd a diophantine relation ‘of exponential
growth’ (what then went under the name ‘Julia Robinson-predicate’):

Theorem 3.10 ([Rob52]). There is a polynomial q ∈ Z[A, B, C; X] such that
for all a, b, c ∈ N a = b
c ⇔ ∃x q(a, b, c; x) = 0,

provided there is a diophantine relation J(u, v) of exponential growth, i.e.,
for all u, v ∈ N

• J(u, v) ⇒ v < uu

• ∀k ∈ N ∃u, v with J(u, v) and v > uk.

That it is, indeed, enough to show that exponentiation is diophantine,
was then proved in the joint paper of Davis, Putnam and Julia Robinson
4.
They used the term exponential polynomial to refer to expressions obtained by
applying the usual operations of addition, multiplication and exponentiation
to integer coeﬃcients and the variables:

Theorem 3.11 ([DPR61]). If A ⊆ N is listable then there are exponential
polynomials EL and ER such that, for all a ∈ N,

a ∈ A ⇔ ∃x EL(a; x) = ER(a; x).

As predicted by Martin Davis, it then needed a young Russian mathe-
matician, Yuri Matiyasevich from St Petersborough, to ﬁll the gap:

Theorem 3.12 ([Mat70]). There is a diophantine relation J(u, v) of expo-
nential growth.

The original proof used Fibonacci numbers. In [D73], Davis gave a simpler
proof using the so called Pell equation

x
2 − dy2 = 1,

4That we write the ﬁrst name only for the lady is neither gallantry nor sexism: the
reason is that there are other Robinsons in the same area: Abraham Robinson, one of the
founders of model theory, and the logician and number theorist Raphael Robinson, also
Julia’s husband
 25

where d = a
2 − 1 ∈ N is a non-square. It is not hard to verify that, for the
number ﬁeld K := Q(√d),

O×
K ⊇ {x + y√
d | x, y ∈ Z with x
2 − dy2 = 1}
= {±1} · (a + √a2 − 1)Z

It then requires a series of elementary computations to actually check that,
on N × N, the relation

J(x, y) ⇔ x
2 − (a
2 − 1)y2 = 1 ⇔ x + y√
d = (a + √a2 − 1)m for some m ∈ N

is of exponential growth, or, at least, close to it.

DPRM-Theorem 3.6 = Theorem 3.10 + 3.11 + 3.12

3.4 Consequences of the DPRM-Theorem

One of the reasons why Davis’ conjecture (the later DPRM-Theorem) was
considered dubious was the fact that it implies the existence of a prime
producing polynomial (P denotes the set of prime numbers):

Corollary 3.13. There is some n ∈ N and a polynomial f ∈ Z[X1, . . . , Xn]
such that P = f (Z
n) ∩ N>0.

Today, even an explicit polynomial (with n = 10) is known ([Mat81]).
Proof: Obviously, P is listable. Hence, by the DPRM-Theorem 3.6, there
is a polynomial p ∈ Z[T ; X] such that

P = {a ∈ Z | ∃x p(a; x) = 0}.

But then the polynomial

f (T1, . . . , T4; X) := [1 − p(T 2
1 + . . . + T 2
4 ; X)](T 2
1 + . . . + T 2
4 )

does the job.
As indicated at the beginning of this section, Hilbert’s 10th problem has
a negative solution even if one asks it for a single polynomial, or, to put it
less misleadingly, for polynomials of a ﬁxed shape, in particular of a ﬁxed
number of variables and a ﬁxed degree:

26

Corollary 3.14. There is a polynomial U ∈ Z[T ; X] and an algorithm pro-
ducing, for each algorithm A, some tA (a counterexample) such that A fails
to answer correctly whether there is some x ∈ Z
n with U(tA; x) = 0.

The proof relies on the fact that there are universal recursive functions/
Turing machines which, in addition to an INPUT-tuple x, take an INPUT-
code tA, and give as OUTPUT the OUTPUT of the algorithm A on input
x. Let us close this section by mentioning that many famous mathemat-
ical problems can be translated into diophantine problems. For example,
Goldbach’s Conjecture that every even number > 2 is the sum of two prime
numbers: Clearly, the set of counterexamples to this conjecture is listable,
hence, by DPRM, diophantine, i.e., we can ﬁnd a polynomial g ∈ Z[T ; X]
such that, for any t ∈ N, g(t; x) = 0

has a solution if and only if t spoils the conjecture. So Goldbach’s Conjecture
is equivalent to the statement that g(t; x) = 0 has no solution at all.
Similar translations can be found for Fermat’s Last Theorem, the Four
Colour Theorem and the Riemann Hypothesis. This may serve as an ‘expla-
nation’ why Hilbert’s 10th problem had to be unsolvable: such diﬃcult and
diverse mathematical problems cannot be expected to be solvable by just one
universal process.

4 Deﬁning Z in Q

Hilbert’s 10th problem over Q, i.e., the question whether Th∃(Q) is decidable,
is still open.
If one had an existential (= diophantine) deﬁnition of Z in Q (i.e., a
deﬁnition by an existential 1st-order Lring-formula) then Th∃(Z) would be
interpretable in Th∃(Q), and the answer would, by (for short) Matiyasevich’s
Theorem, again be no. But it is still open whether Z is existentially deﬁnable
in Q.
We have seen the earliest 1st-order deﬁnition of Z in Q, due to Julia
Robinson ([R49]), in section 2.3. It can be expressed by an ∀∃∀-formula of
the shape

φ(t) : ∀x1∀x2∃y1 . . . ∃y7∀z1 . . . ∀z6 f (t; x1, x2; y1, . . . , y7; z1, . . . , z6) = 0

27

for some f ∈ Z[t; x1, x2; y1, . . . , y7; z1, . . . , z6], i.e., for any t ∈ Q,

t ∈ Z iﬀ φ(t) holds in Q.

In 2009, Bjorn Poonen ([P09a]) managed to ﬁnd an ∀∃-deﬁnition with 2
universal and 7 existential quantiﬁers (earlier, in [CZ07], an ∀∃-deﬁnition
with just one universal quantiﬁer was proved modulo an open conjecture on
elliptic curves). In this section we present our ∀-deﬁnition of Z in Q:

Theorem 4.1 ([Koe10]). There is a polynomial g ∈ Z[T ; X1, . . . , X418] such
that, for all t ∈ Q,
 t ∈ Z iﬀ ∀x ∈ Q
418 g(t; x) ̸= 0.

If one measures logical complexity in terms of the number of changes of
quantiﬁers then this is the simplest deﬁnition of Z in Q, and, in fact, it is
the simplest possible:

Exercise 4.2. Show that there is no quantiﬁer-free deﬁnition of Z in Q.

Corollary 4.3. Q \ Z is diophantine in Q.

Corollary 4.4. T h∀∃(Q) is undecidable.

Theorem 4.1 came somewhat unexpected because it does not give what
one would like to have, namely an existential deﬁnition of Z in Q. However,
if one had the latter the former would follow:

Observation 4.5. If there is an existential deﬁnition of Z in Q then there
is also a universal one.

Proof: If Z is diophantine in Q then so is

Q \ Z = {x ∈ Q | ∃m, n, a, b ∈ Z with n ̸= 0, ±1, am + bn = 1 and m = xn}

In fact, we will indicate in section 4.3 why we do not expect there to be
an existential deﬁnition of Z in Q.
Using heavier machinery from number theory, Jennifer Park has recently
generalised Theorem 4.1 to number ﬁelds:

Theorem 4.6 ([Par12]). For any number ﬁeld K, the ring of integers OK
is universally deﬁnable in K.
 28

4.1 Key steps in the proof of Theorem 4.1

Like all previous deﬁnitions of Z in Q, we use the Hasse-Minkowski Local-
Global-Principle for quadratic forms (Theorem 2.10). What is new in our
approach is the use of the Quadratic Reciprocity Law and, inspired by the
model theory of local ﬁelds, the transformation of some existential formulas
into universal formulas.

Step 1: Poonen’s diophantine deﬁnition of quaternionic semi-local
rings

The ﬁrst step essentially copies Poonen’s proof ([Poo09a]). We adopt his
terminology:

Deﬁnition 4.7. For a, b ∈ Q
×, let

• Ha,b := Q · 1 ⊕ Q · α ⊕ Q · β ⊕ Q · αβ be the quaternion algebra over Q
with multiplication deﬁned by α2 = a, β2 = b and αβ = −βα,

• ∆a,b := {l ∈ P∪{∞} | Ha,b ⊗Ql ̸∼= M2(Ql)} the set of primes (including
∞) where Ha,b does not split locally (Q∞ := R) — ∆a,b is always ﬁnite,
and ∆a,b = ∅ iﬀ a ∈ N(b), i.e., a is in the image of the norm map
Q(√b) → Q,

• Sa,b := {2x1 ∈ Q | ∃x2, x3, x4 ∈ Q : x
2
1 − ax
2
2 − bx
2
3 + abx
2
4 = 1} the set
of traces of norm-1 elements of Ha,b, and

• Ta,b := Sa,b + Sa,b – note that Ta,b is an existentially deﬁned subset of
Q.

Lemma 4.8. Ta,b = ⋂
l∈∆a,b Z(l), where, for l ∈ P, Z(l) = Zl ∩ Q is Z localised
at l, and Z(∞) := {x ∈ Q | −4 ≤ x ≤ 4}. (Ta,b = Q if ∆a,b = ∅.)

The proof follows essentially that of [Poo09a], Lemma 2.5, using Hensel’s
Lemma, the Hasse bound for the number of rational points on genus-1 curves
over ﬁnite ﬁelds, and the local-global principle for quadratic forms. Poonen
then obtains his ∀∃-deﬁnition of Z in Q from the fact that

Z = ⋂

l∈P Z(l) = ⋂

a,b>0 Ta,b.

Note that ∞ ̸∈ ∆a,b iﬀ a > 0 or b > 0.

29

Step 2: Towards a uniform diophantine deﬁnition of all Z(p)’s in Q

We will present a diophantine deﬁnition for the local rings Z(p) = Zp ∩ Q
(i.e., Z localized at pZ) depending on the congruence of the prime p modulo
8, and involving p (and if p ≡ 1 mod 8 an auxiliary prime q) as a param-
eter. However, since in any ﬁrst-order deﬁnition of a subset of Q we can
only quantify over the elements of Q, and not, e.g., over all primes, we will
allow arbitrary (non-zero) rationals p and q as parameters in the following
deﬁnition.

Deﬁnition 4.9. For p, q ∈ Q
× let

• R[3]
p := T−p,−p + T2p,−p

• R[5]
p := T−2p,−p + T2p,−p

• R[7]
p := T−p,−p + T2p,p

• R[1]
p,q := T2pq,q + T−2pq,q

The R’s are all existentially deﬁned subrings of Q containing Z, since for
any a, b, c, d ∈ Q
×
 Ta,b + Tc,d = ⋂

l∈∆a,b∩∆c,d Z(l),

and since in each case at least one of a, b, c, d is > 0, so ∞ ̸∈ ∆a,b ∩ ∆c,d.

Deﬁnition 4.10. (a) P[k] := {l ∈ P | l ≡ k mod 8}, where k = 1, 3, 5 or
7

(b) For p ∈ Q
×, deﬁne

• P(p) := {l ∈ P | vl(p) is odd}, where vl denotes the l-adic valua-
tion on Q

• P[k](p) := P(p) ∩ P[k], where k = 1, 3, 5 or 7

• p ≡2 k mod 8 iﬀ p ∈ k + 8Z(2), where k ∈ {0, 1, 2, . . . , 7}

• for l a prime, the generalized Legendre symbol (( p
l
 )) = ±1 to

indicate whether or not the l-adic unit pl−vl(p) is a square modulo
l.
 30

Lemma 4.11. (a) Z(2) = T3,3 + T2,5

(b) For p ∈ Q
× and k = 3, 5 or 7, if p ≡2 k mod 8 then

R[k]
p = { ⋂
l∈P[k](p) Z(l) if P[k](p) ̸= ∅
Q if P[k](p) = ∅

In particular, if p is a prime (≡ k mod 8) then Z(p) = R[k]
p .

(c) For p, q ∈ Q
× with p ≡2 1 mod 8 and q ≡2 3 mod 8,

R[1]
p,q = { ⋂
l∈P(p,q) Z(l) if P(p, q) ̸= ∅
Q if P(p, q) = ∅

where

l ∈ P(p, q) :⇔ l ∈
 



 P(p) \ P(q) with (( q
l
 )) = −1, or

P(q) \ P(p) with (( 2p
l
 )) = (( −2p
l
 )) = −1, or

P(p) ∩ P(q) with (( 2pq
l
 )) = (( −2pq
l
 )) = −1

In particular, if p is a prime ≡ 1 mod 8 and q is a prime ≡ 3 mod 8

with ( q
p
 ) = −1 then Z(p) = R[1]
p,q.

Corollary 4.12.
 Z = Z(2) ∩ ⋂

p,q∈Q×(R[3]
p ∩ R[5]
p ∩ R[7]
p ∩ R[1]
p,q)

The proof of the Lemma uses explicit norm computations for quadratic
extensions of Q2, the Quadratic Reciprocity Law and the following

Observation 4.13. For a, b ∈ Q
× and for an odd prime l,

l ∈ ∆a,b ⇔
 



 vl(a) is odd, vl(b) is even, and (( b
l
 )) = −1, or

vl(a) is even, vl(b) is odd, and (( a
l
 )) = −1, or

vl(a) is odd, vl(b) is odd, and (( −ab
l
 )) = −1

31

Corollary 4.14. The following properties are diophantine properties for any
p ∈ Q
×:

• p ≡2 k mod 8 for k ∈ {0, 1, 2, . . . , 7}

• P(p) ⊆ P[1] ∪ P[k] for k = 3, 5 or 7

• P(p) ⊆ P[1]

Step 3: From existential to universal

In Step 3, we try to ﬁnd universal deﬁnitions for the R’s occurring in Corollary
4.12 imitating the local situation: First one observes that for R = Z(2), or
for R = R[k]
p with k = 3, 5 or 7, or for R = R[1]
p,q, the Jacobson radical J(R)
(which is deﬁned as the intersection of all maximal ideals of R) can be deﬁned
by an existential formula using Observation 4.13. Now let

̃R := {x ∈ Q | ¬∃y ∈ J(R) with x · y = 1}.

Proposition 4.15. (a) ̃R is deﬁned by a universal formula in Q.

(b) If R = ⋂
l∈P\R× Z(l) then ̃R = ⋃
l∈P\R× Z(l), provided P \ R× ̸= ∅, i.e.,
provided R ̸= Q.

(c) In particular, if R = Z(l) then ̃R = R.

The proviso in (b), however, can be guaranteed by diophantinely deﬁnable
conditions on the parameters p, q:

Lemma 4.16. (a) Deﬁne for k = 1, 3, 5 and 7,

Φk := {p ∈ Q
× p ≡2 k mod 8 and P(p) ⊆ P[1] ∪ P[k]}

Ψ := {(p, q) ∈ Φ1 × Φ3 p ∈ 2 · (Q
×)2 · (1 + J(R[3]
q ))} .

Then Φk and Ψ are diophantine in Q.
(b) Assume that

• R = R[k]
p for k = 3, 5 or 7, where p ∈ Φk, or

• R = R[1]
p,q where (p, q) ∈ Ψ.
 32

Then R ̸= Q.

The proof of this lemma is somewhat involved, though purely combina-
torial, playing with the Quadratic Reciprocity Law and Observation 4.13.
The universal deﬁnition of Z in Q can now be read oﬀ the equation

Z = ˜Z(2) ∩ ( ⋂

k=3,5,7
 ⋂

p∈Φk
 ˜
R[k]
p ) ∩ ⋂

(p,q)∈Ψ
 ˜
R[1]
p,q,

where Φk and Ψ are the diophantine sets deﬁned in Lemma 4.16.
The equation is valid by Lemma 4.11, Proposition 4.15(b), (c) and Lemma
4.16(b). The deﬁnition is universal as one can see by spelling out the equation
and applying Lemma 4.15(a) and Corollary 4.14: for any t ∈ Q,

t ∈ Z ⇔ t ∈ ˜Z(2)∧

∀p ⋀
k=3,5,7(t ∈ ˜
R[k]
p ∨ p ̸∈ Φk)∧

∀p, q(t ∈ ˜
R[1]
p,q ∨ (p, q) ̸∈ Ψ)

Theorem 4.1 is now obtained by diophantine routine arguments and counting
quantiﬁers.

4.2 More diophantine predicates in Q

From the results and techniques of section 4.1, one obtains new diophantine
predicates in Q. Among them are

• x ̸∈ Q
2

• x ̸∈ N(y), where N(y) is the image of the norm Q(√y) → Q

The ﬁrst was also obtained in [Poo09b], using a deep result of Colliot-Thélène
et al. on Châtelet surfaces — our techniques are purely elementary.

4.3 Why Z should not be diophantine in Q

There are two conjectures in arithmetic geometry that imply that Z is not
diophantine in Q, Mazur’s Conjecture and, what one may call the Bombieri-
Lang Conjecture.

Mazur’s Conjecture ([Maz98]) For any aﬃne variety V over Q the (real)

33

topological closure of V (Q) in V (R) has only a ﬁnite number of connected
components.

It is clear that, under this conjecture, Z cannot be diophantine in Q, as
the latter would mean that Z is the projection of V (Q) for some aﬃne (not
necessarily irreducible) variety V over Q, but then, passing to the topological
closure in R, V (R) would have ﬁnitely many connected components whereas
the projection (which is still the closed subset Z of R) has inﬁnitely many -
contradiction.

The next conjecture, though never explicitly formulated by Lang and
Bombieri in this form, may (arguably) be called ‘Bombieri-Lang Conjecture’
(following [HS00]). In order to state it we deﬁne, given a projective algebraic
variety V over Q, the special set Sp(V ) to be the Zariski closure of the union
of all φ(A), where φ : A → V runs through all non-constant morphisms from
abelian varieties A over Q to V .

Bombieri-Lang Conjecture
If V is a projective variety over Q then V (Q) \ (Sp(V )(Q)) is ﬁnite.

We shall use the following consequence of the conjecture:

Lemma 4.17. Assume the Bombieri-Lang Conjecture. Let f ∈ Q[x1, . . . , xn+1]\
Q[x1, . . . , xn] be absolutely irreducible and et V = V (f ) ⊆ An+1 be the aﬃne
hypersurface deﬁned by f over Q. Assume that V (Q) is Zariski dense in
V . Let π : An+1 → A1 be the projection on the 1st coordinate. Then
V (Q) ∩ π−1(Q \ Z) is also Zariski dense in V .

The proof uses a highly non-trivial ﬁniteness result on integral points on
abelian varieties by Faltings ([Fal91]).

Theorem 4.18 ([Koe10]). Assume the Bombieri-Lang Conjecture as stated
above. Then there is no inﬁnite subset of Z existentially deﬁnable in Q. In
particular, Z is not diophantine in Q.

Proof: Suppose A ⊆ Z is inﬁnite and deﬁnable in Q by an existential
formula φA(x) in the language of rings. Replacing, if necessary, A by −A,
we may assume that A ∩ N is inﬁnite.
Choose a countable proper elementary extension Q
⋆ of Q realizing the
type {φA(x) ∧ x > a | a ∈ A} and let A
⋆ = {x ∈ Q
⋆ | φA(x)}. Then A
⋆ con-

tains some nonstandard natural number x ∈ N⋆ \ N. The map { N → N
n ↦→ 2n

34

is deﬁnable in N and hence in Q, so 2x ∈ N⋆. As 2x is greater than any
element algebraic over Q(x), the elements x, 2x, 22x, . . . are algebraically in-
dependent over Q. We therefore ﬁnd an inﬁnite countable transcendence
base ξ1, ξ2, . . . of Q
⋆ over Q with ξ1 ∈ A
⋆.
Let K = Q(ξ1, ξ2, . . .). As Q
⋆ is countable we ﬁnd αi ∈ Q
⋆ (i ∈ N) such
that
 K(α1) ⊆ K(α2) ⊆ · · · with
 ∞⋃

i=1 K(αi) = Q
⋆,

where we may in addition assume that, for each i ∈ N, the minimal polyno-
mial fi ∈ K[Z] of αi over K has coeﬃcients in Q[ξ1, . . . , ξi]. As Q is relatively
algebraically closed in Q
⋆, all the fi ∈ Q[X1, . . . , Xi, Z] are absolutely irre-
ducible over Q.
Now consider the following set of formulas in the free variables x1, x2, . . .:

p = p(x1, x2, . . .) := {g(x1, . . . , xi) ̸= 0 | i ∈ N, g ∈ Q[x1, . . . , xi] \ {0}}
∪ {∃z fi(x1, . . . , xi, z) = 0 | i ∈ N}
∪ {x1 is not an integer}

Then p is ﬁnitely realizable in Q: Let p0 ⊆ p be ﬁnite and let j be the
highest index occurring in p0 among the formulas from line 2. Since the
K(αj) are linearly ordered by inclusion all formulas from line 2 with index
< j follow from the one with index j. Hence one only has to check that
V (fj) has Q-Zariski dense many Q-rational points (x1, . . . , xj, z) ∈ Aj+1

with x1 ̸∈ Z. But this is, assuming the Bombieri-Lang Conjecture, exactly
the conclusion of the above Lemma. Note that V (fj)(Q) is Q-Zariski dense
in V (fj) because there is a point (ξ1, . . . , ξj, αj) ∈ V (fj)(Q
⋆) with ξ1, . . . , ξi
algebraically independent over Q.
Hence p is a type that we can realize in some elementary extension Q
⋆⋆

of Q. Calling the realizing ω-tuple in Q
⋆⋆ again ξ1, ξ2, . . . our construction
yields that we may view Q
⋆ as a subﬁeld of Q
⋆⋆.
But now ξ1 ∈ A
⋆ ⊆ Z
⋆ and ξ1 ̸∈ Z
⋆⋆, hence ξ1 ̸∈ A
⋆⋆. This implies that
there is after all no existential deﬁnition for A in Q.

Let us conclude with a collection of closure properties for pairs of models
of Th(Q) (in the ring language), one a substructure of the other, which might
have a bearing on the ﬁnal (unconditional) answer to the question whether
or not Z is diophantine in Q.
 35

Proposition 4.19. Let Q
⋆, Q
⋆⋆ be models of Th(Q) (i.e., elementary exten-
sions of Q) with Q
⋆ ⊆ Q
⋆⋆, and let Z
⋆ and Z
⋆⋆ be their rings of integers.
Then

(a) Z
⋆⋆ ∩ Q
⋆ ⊆ Z
⋆.

(b) Z
⋆⋆ ∩ Q
⋆ is integrally closed in Q
⋆.

(c) (Q
⋆⋆)2 ∩ Q
⋆ = (Q
⋆)2, i.e. Q
⋆ is quadratically closed in Q
⋆⋆.

(d) If Z is diophantine in Q then Z
⋆⋆ ∩ Q
⋆ = Z
⋆ and Q
⋆ is algebraically
closed in Q
⋆⋆.

(e) Q is not model complete, i.e., there are Q
⋆ and Q
⋆⋆ such that Q
⋆ is not
existentially closed in Q
⋆⋆.

Proof: (a) is an immediate consequence of our universal deﬁnition of Z in
Q. The very same deﬁnition holds for Z
⋆ in Q
⋆ and for Z
⋆⋆ in Q
⋆⋆ (it is part
of Th(Q) that all deﬁnitions of Z in Q are equivalent). So if this universal
formula holds for x ∈ Z
⋆⋆ ∩ Q
⋆ in Q
⋆⋆ it also holds in Q
⋆, i.e., x ∈ Z
⋆.
(b) is true because Z
⋆⋆ is integrally closed in Q
⋆⋆.
(c) follows from the fact that both being a square and, by section 4.2, not
being a square are diophantine in Q.
(d) If Z is diophantine in Q then Z
⋆⋆ ∩ Q
⋆ ⊇ Z
⋆ and hence equality holds,
by (a).
To show that then also Q
⋆ is algebraically closed in Q
⋆⋆, let us observe
that, for each n ∈ N,

An := {(a0, . . . , an−1) ∈ Z
n | ∃x ∈ Z with x
n + an−1x
n−1 + . . . + a0 = 0}

is decidable: zeros of polynomials in one variable are bounded in terms of
their coeﬃcients, so one only has to check ﬁnitely many x ∈ Z. In particular,
by (for short) Matiyasevich’s Theorem, there is an ∃-formula φ(t0, . . . , tn−1)
such that

Z |= ∀t0 . . . tn−1 ({∀x[x
n + tn−1x
n−1 + . . . + t0 ̸= 0]} ↔ φ(t0, . . . , tn−1)) .

Since both An and its complement in Z
n are diophantine in Z, the same holds
in Q, by our assumption of Z being diophantine in Q, i.e., A
⋆⋆
n ∩ (Q
⋆)n = A
⋆
n.
As any ﬁnite extension of Q
⋆ is generated by an integral primitive element
this implies that Q
⋆ is relatively algebraically closed in Q
⋆⋆.

36

(e) Choose a recursively enumerable subset A ⊆ Z which is not decidable.
Then B := Z \ A is deﬁnable in Z, and hence in Q. If B were diophantine
in Q it would be recursively enumerable. But then A would be decidable:
contradiction.
So not every deﬁnable subset of Q is diophantine in Q, and hence Q is
not model complete. Or, in other words, there are models Q
⋆, Q
⋆⋆ of Th(Q)
with Q
⋆ ⊆ Q
⋆⋆ where Q
⋆ is not existentially closed in Q
⋆⋆.

We are conﬁdent that with similar methods as used in this paper one
can show for an arbitrary prime p that the unary predicate ‘x ̸∈ Q
p’ is also
diophantine. This would imply that, in the setting of the Proposition, Q
⋆ is
always radically closed in Q
⋆⋆. However, we have no bias towards an answer
(let alone an answer) to the following (unconditional)

Question 4.20. For Q
⋆ ≡ Q
⋆⋆ ≡ Q with Q
⋆ ⊆ Q
⋆⋆, is Q
⋆ always alge-
braically closed in Q
⋆⋆?

5 Decidability and Hilbert’s 10th Problem over
other rings

In this section we only report on major achievements under this heading and
on a small choice of big open problems. There is a multitude of surveys on
the subject, each with its own emphasis. For the interested reader, let us
mention at least some of them: [RRo51], [Maz94], [Phe94], [PZ00], [Shl00],
[Poo03], [Shl07] and [Poo08].

5.1 Number rings

For number rings and number ﬁelds, the question of decidability has been
answered in the negative by Julia Robinson (Theorem 2.13). The question
whether Hilbert’s 10th Problem is solvable is much harder. Given that we
don’t know the answer over Q (though almost everyone working in the ﬁeld
believes it to be no) there is even less hope that we ﬁnd the answer for
arbitrary number ﬁelds in the near future. For number rings the situation is
much better.
Let K be a number ﬁeld with ring of integers OK. Then Hilbert’s 10th
Problem could be shown to be unsolvable over OK in the following cases:

37

• if K is totally real (i.e., K ⊆ T ) or a quadratic extension of a totally
real number ﬁeld ([Den75], [DL78] and [Den80])

• if [K : Q] ≥ 3 and cK = 2 ([Phe88])5.

• if K/Q is abelian ([SS89]).

In each of the proofs the authors managed to ﬁnd an existential deﬁnition of
Z in OK using Pell-equations, the Hasse-Minkowski Local-Global Principle
(which holds in all number ﬁelds) and ad hoc methods that are very speciﬁc
to each of these special cases.
The hope for a uniform proof of the existential undecidability of all num-
ber rings only emerged when elliptic curves were brought into the game:

Theorem 5.1 ([Poo02]). Let K be a number ﬁeld. Assume
6 there is an ellip-
tic curve E over Q with rk(E(Q)) = rk(E(K)) = 1. Then Z is existentially
deﬁnable in OK and so Hilbert’s 10th Problem over OK is unsolvable.

In his proof, Poonen uses divisibility relations for denominators of x-
coordinates of n · P , where P ∈ E(K) \ Etor(K) and n · P ∈ E(Q) (for a
similar approach cf. [CPZ05]).
The assumption made in the theorem turns out to hold modulo a generally
believed conjecture, the so called Tate-Shafarevich Conjecture. For an elliptic
curve E over a number ﬁeld K, it refers to the Tate-Shafarevich group (or
Shafarevich-Tate group) XE/K, an abelian group deﬁned via cohomology
groups. It measures the deviation from a local-global principle for rational
points on E.

Tate-Shafarevich Conjecture XE/K is ﬁnite.

Weak Tate-Shafarevich Conjecture dimF2 XE/K/2 is even

The latter follows from the former due to the Cassels pairing (Theorem 4.14
in [Sil86] which is an excellent reference on elliptic curves).

5cK denotes the class number of K, that is, the size of the ideal class group of K. It
measures how far OK is from being a PID: cK = 1 iﬀ OK is a PID, so cK = 2 is ‘the next
best’. It is not known whether there are inﬁnitely many number ﬁelds with cK = 1.
6The set E(K) of K-rational points of E is a ﬁnitely generated abelian group isomorphic
to the direct product of its torsion subgroup Etor(K) and a free abelian group of rank
‘rk(E(K))’.
 38

Theorem 5.2 ([MR10]). Let K be a number ﬁeld. Assume the weak Tate-
Shafarevich Conjecture for all elliptic curves E/K. Then there is an elliptic
curve E/Q with rk(E(Q)) = rk(E(K)) = 1.

Taking those two theorems together one obtains immediately the follow-
ing

Corollary 5.3. Let K be a number ﬁeld. Assume the weak Tate-Shafarevich
Conjecture for all elliptic curves E/K. Then Hilbert’s 10th Problem is un-
solvable over OK.

5.2 Function ﬁelds

It is natural to ask decidability questions not only over number ﬁelds, but
also over global ﬁelds of positive characteristic, i.e., algebraic function ﬁelds
in one variable over ﬁnite ﬁelds, and also, more generally, for function ﬁelds.
Hilbert’s 10th Problem has been shown to be unsolvable for the following
function ﬁelds:

• R(t) ([Den78])

• C(t1, t2) ([KR92])

• Fq(t) ([Phe91] and [Vid94])

• ﬁnite extensions of Fq(t) ([Shl92] and [Eis03])

The ﬁrst two cases were achieved by existentially deﬁning Z in the ﬁeld, and
then applying Matiyasevich’s Theorem. This is, clearly, not possible in the
last two cases. Instead of existentially deﬁning Z the authors existentially in-
terpret Z via elliptic curves: the multiplication by n-map on an elliptic curve
E/K where E(K) contains non-torsion points easily gives a diophantine in-
terpretation of the additive group ⟨Z; +⟩. The diﬃculty is to ﬁnd an elliptic
curve E/K such that there is also an existential deﬁnition for multiplication
on that additive group.
For the ring of polynomials Fq[t], Demeyer has even shown the analogue
of the DPRM-Theorem: listible subsets are diophantine ([Dem07]).
Generalizing earlier results ([Che84], [Dur86] and [Phe04]), it is shown in
[ES09], that the full ﬁrst-order theory of any function ﬁeld of characteristic
> 2 is undecidable.
For analogues of Hilbert’s 10th Problem for ﬁelds of meromorphic or
analytic functions cf., e.g., [Rub95], [Vdau03] and [Pas13].

39

5.3 Open problems

Hilbert’s 10th Problem is open for

• Q and all number ﬁelds

• the ring of totally real integers OT (cf. sections 2.4 and 2.5)

Hilbert’s 10th Problem and full 1st-order decidability are open for

• C(t): this may well be considered the most annoying piece of our ig-
norance in the area. On the other hand, C[t] and, in fact, R[t] for any
integral domain R is known to be existentially undecidable in Lring∪{t}
([Den78] and [Den84]).

• Fp((t)) and Fp[[t]] — in this case the answer to either question will
be the same for the ﬁeld and the ring: in his recent thesis [Ans12],
Will Anscombe found a parameter-free existential deﬁnition of Fp[[t]] in
Fp((t)). In [DS03], Jan Denef and Hans Schoutens show that Hilbert’s
10th Problem is solvable, if one assumes resolution of singularities in
characteristic p.

• the ﬁeld Ω of constructible numbers (= the maximal pro-2 Galois exten-
sion of Q). What is known here is that OΩ is deﬁnable in Ω ([Vid99]),
and, more generally ([Vid00]), that for any prime p and any pro-p Galois
extension F of a number ﬁeld, OF is deﬁnable in F . As a consequence,
the ﬁeld of real numbers constructible with ruler and scale, i.e., the
maximal totally real Galois subextension Ω ∩ T of Ω is undecidable.

• the maximal abelian extension Q
ab of Q and its ring of integers Z
ab

— recall that, by the Kronecker-Weber Theorem, Q
ab is the maximal
cyclotomic extension of Q, obtained from Q by adjoining all roots of
unity. Here the answer may be related to the famous Shafarevich Con-
jecture that the absolute Galois group of Q
ab is a free proﬁnite group (if
this is true decidability becomes more likely, cf. the remarks following
Theorem 2.18).

Let us remark that the ring of integers Z
rab of the ﬁeld Q
rab := Q
ab ∩ R
of real abelian algebraic numbers is undecidable, by the identical proof
as Theorem 2.14. Note that Q
ab = Q
rab(i) and that Q
rab is the ﬁxed
ﬁeld of Q
ab under complex conjugation. We do not know whether Q
rab

40

is deﬁnable in Q
ab, but we conjecture that Z
rab is deﬁnable in Z
ab which
would result in undecidability of Z
ab.

• the maximal solvable extension Q
solv of Q and its ring of integers Z
solv

— here the answer may be related to the longstanding open question
whether Q
solv is pseudo-algebraically-closed (PAC) (Problem 10.16 in
[FJ86], or Problem 11.5.9(a) in the 3rd edition; a ﬁeld K is PAC if
every absolutely irreducible algebraic variety deﬁned over K has a K-
rational point): if the answer to this question is yes and if Shafarevich’s
Conjecture holds then Q
solv is decidable, axiomatized by being PAC,
by the algebraic part and ‘by its absolute Galois group’, the minimal
normal subgroup of a free group with prosolvable quotient.

• the ring of integers of the ﬁeld of totally p-adic numbers — here the
question is whether there is an analogue of Kronecker’s Theorem used
in Lemma 2.16.

All known examples either have both the full theory and the existential theory
decidable or both undecidable. We have no answer to the following

Question 5.4. Is there a ‘naturally occurring’ ring R with Th∃(R) decidable,
but Th(R) not?

We are conﬁdent that one can build ‘unnatural’ examples using some
Shelah-style construction (though we haven’t followed up on that). A positive
answer to an analogue of this question is Lipshitz’s result that addition and
divisibility over Z is ∃-decidable, but ∀∃-undecidable ([Lip78]).
Let us cconclude these notes by mentioning decidability questions for
ﬁelds that come up in other parts of this volume:

• Let k be a ﬁeld of characteristic 0 and let Γ be an ordered abelian
group. Then, by the Ax-Kochen/Ershov principle (see [Dri13]),

k((Γ)) is decidable ⇔ k and Γ are decidable
k((Γ)) is ∃-decidable ⇔ k and Γ are ∃-decidable

• Let Rexp be the real exponential ﬁeld and let SC+ be the ‘souped up’
version of Schanuel’s Conjecture as in [MW96]. Then

Rexp is decidable ⇔ SC+ holds
⇔ Rexp is ∃-decidable

41

• The complex exponential ﬁeld Cexp is, clearly, undecidable, as Z is
deﬁnable via the kernel of exponentiation (this was already known to
Tarski). In fact, Z is even existentially deﬁnable in Cexp: In the 1980’s,
Angus Macintyre observed that, for any x ∈ C,

x ∈ Q ⇔ ∃t, v, u [(v − u)t = 1 ∧ e
v = e
u = 1 ∧ vx = u] ,

and in 2002, Miklós Laczkovich found, that for any x ∈ C,

x ∈ Z ⇔ x ∈ Q ∧ ∃z (e
z = 2 ∧ e
zx ∈ Q).

Hence, Cexp is even existentially undecidable (cf. section 2.2 in [KMO12]).

References

[Ans12] Will Anscombe, Deﬁnability in Henselian ﬁelds, PhD thesis, Oxford
2012.

[Che84] Gregory L. Cherlin, Undecidability of rational function ﬁelds in
nonzero characteristic, Stud. Logic Found. Math. 112 (1984), 85-
95.

[CPZ05] Gunther Cornelissen, Thanases Pheidas, Karim Zahidi, Division-
ample sets and the Diophantine problem for rings of integers, J.
Th. Nombres de Bordeaux 17 (2005), 727-735.

[Csi00] George Csicsery, Julia Robinson and Hilbert’s Tenth Problem, doc-
umentary ﬁlm by Zala Films 2010.

[CZ07] Gunther Cornelissen, Karim Zahidi, Elliptic divisibility sequences
and undecidable problems about rational points, J. Reine Angew.
Math. 613 (2007), 1-33.

[Dar00] Luck Darnière, Decidability and local-global principles, in [DPLG00]
(2000), 139-167.

[Dav53] Martin Davis, Arithmetical problems and recursively enumerable
predicates, J. Symb. Logic 18(1) (1953), 33-41.

[Dav73] —, Hilbert’s tenth problem is unsolvable, Amer. Math. Monthly
80(3) (1973), 233-269.
 42

[DPR61] Martin Davis, Hilary Putnam, Julia Robinson, The decision prob-
lem for exponential Diophantine equations, Ann. Math. (2) 74
(1961), 425-436.

[Dem07] Jeroen Demeyer, Recursively enumerable sets of polynomials over a
ﬁnite ﬁeld are Diophantine, Invent. Math. 170(3) (2007), 655-670.

[Den75] Jan Denef, Hilbert’s 10th Problem for quadratic rings, Proc. AMS
48 (1975), 214-220.

[Den78] —, The diophantine problem for polynomial rings and ﬁelds of ra-
tional functions, Trans. AMS 242 (1978), 391-399.

[Den80] —, Diophantine sets over algebraic integer rings II, Trans. AMS
257 (1980), 227-236.

[Den84] —, The diophantine problem for polynomial rings of positive char-
acteristic, Logic Colloquium 78, North Holland (1984), 131-145.

[DL78] Jan Denef, Leonard Lipshitz, Diophantine sets over some rings of
algebraic integers, J. LMS 18 (1978), 385-391.

[DLPG00] Jan Denef, Leonard Lipshitz, Thanases Pheidas, Jan Van Geel,
Hilbert’s Tenth Problem: relations with arithmetic and algebraic
geometry, Contemporary Math. (AMS) 270, 2000.

[Dri88] Lou van den Dries, Elimination theory for the ring of algebraic in-
tegers, J. Reine Angew. Math. 388 (1988), 189-205.

[Dri13] —, Lectures on the Model Theory of Valued Fields, this volume.

[DS03] Jan Denef, Hans Schoutens, On the decidability of the existential
theory of Fp[[T ]], in: Franz-Viktor Kuhlmann et al. (eds), Valuation
theory and its applications 2, Fields Inst. Comm. 33 (2003), 43-60.

[Dur86] Jean-Louis Duret, Sur la théorie élémentaire des corps de fonctions,
J. Symb. Logic 51(4), 948-956.

[Eis03] Kirsten Eisenträger, Hilbert’s 10th Problem for algebraic function
ﬁelds of characteristic 2, Pac. J. Math. 210(2) (2003), 261-281.

43

[ES09] Kirsten Eisenträger, Alexandra Shlapentokh, Undecidability in
function ﬁelds of positive characteristic, Int. Math. Res. Not. 2009
(2009), 4051-4086.

[EP05] Antonio J. Engler, Alexander Prestel, Valued ﬁelds, Springer 2005.

[Fal91] Gerd Faltings, Diophantine approximation on abelian varieties,
Ann. of Math. 133 (1991), 549-576.

[FHV94] Michael Fried, Dan Haran, Helmuth Völklein, Real hilbertianity and
the ﬁeld of totally real numbers, Contemp. Math. 74 (1994), 1-34.

[FJ86] Michael Fried, Moshe Jarden, Field arithmetic, Springer 1986, 3rd
edition 2008.

[Göd31] Kurt Gödel, Über formal unentscheidbare Sätze der Principia Math-
ematica und verwandter Systeme, Monatshefte Math. Phys. 38
(1931), 173-198.

[GPR95] Barry Green, Florian Pop, Peter Roquette, On Rumely’s local-
global principle, Jber. Dt. Math.-Verein. 97 (1995), 43-74.

[Hil00] David Hilbert, Mathematische Probleme. Vortrag, gehalten auf dem
internationalen Mathematiker Kongress zu Paris 1900, Nachr. K.
Ges. Wiss., Göttingen, Math.-Phys. Kl. (1900), 253-297.

[HS00] Marc Hindry, Joseph H. Silverman, Diophantine geometry, Springer
Graduate Texts in Mathematics 201, 2000.

[KMO12] Jonathan Kirby, Angus Macintyre, Alf Onshuus, The algebraic
numbers deﬁnable in various exponential ﬁelds, J. Inst. Math.
Jussieu 11(04) (2012), 825-834.

[Koe10] Jochen Koenigsmann, Deﬁning Z in Q, arXiv:1011.3424v1 (2010),
to appear in Ann. of Math.

[KR92] Ki Hang Kim, Fred W. Roush, Diophantine undecidability of
C(t1, t2), J. Algebra 150(1), 35-44.

[Kro57] Leopold Kronecker, Zwei Sätze über Gleichungen mit ganzzahligen
Coeﬃcienten, J. Reine Angew. Math. 53 (1857), 173-175.

44

[Lac02] Miklós Laczkovich, The removal of π from some undecidable prob-
lems involving elementary functions, Proc. AMS 131(7) (2002),
2235-2240.

[Lip78] Leonard Lipshitz, The diophantine problem for addition and divis-
ibility, Trans. AMS 235 (1978), 271-283.

[Mac11] Angus Macintyre, The impact of Gödel’s Incompleteness Theorems
on mathematics in: Matthias Baaz et al., Kurt Gödel, CUP 2011,
3-25.

[MW96] Angus Macintyre, Alex Wilkie, On the decidability of the real ex-
ponential ﬁeld, in: Piergiorgio Odifreddi, Kreiseliana, A.K. Peters
1996, 441-467

[Mat70] Yuri V. Matiyasevich, Diofantovost’ perechislimykh mnozhestv,
Dokl. AN SSSR 191(2) (1970), 278-282. Translated in: Soviet
Math. Doklady 11(2) (1970), 354-358.

[Mat81] —, Prostye chisla perechislyayutsya polinomom ot 10peremennykh,
translated in: J. Sov. Math. 15(19) (1981), 33-44.

[Mat00] —, Hilbert’s 10th Problem: what was done and what is to be done,
in: [DLPG00] (2000), 1-47.

[Maz94] Barry Mazur, Questions of Decidability and Undecidability in Num-
ber Theory, J. Symb. Logic 59(2) (1994), 353-371.

[Maz98] —, Open problems regarding rational points on curves and varieties,
in: Anthony J. Scholl, Richard L. Taylor (eds.) Galois representa-
tions in arithmetic algebraic geometry, CUP 1998, 239-266.

[Mor89] Laurent Moret-Bailly, Groupes de Picard et problèmes de Skolem
I and II, Ann. Scien. Ec. Norm. Sup. 22(2) (1989), 161-179 and
181-194.

[MR10] Barry Mazur, Karl Rubin Ranks of twists of elliptic curves and
Hilbert’s tenth problem, Invent. Math. 181(3) (2010), 541-575.

[O’Me73] Onorato T. O’Meara, Introduction to quadratic forms, Springer
1973.
 45

[Par12] Jennifer Park, A universal ﬁrst order formula deﬁning the ring of
integers in a number ﬁeld, arXiv:1202.6371v1 (2012).

[Pas13] Hector Pasten, Powerful Values of polynomials and a conjecture of
Vojta, J. Number Theory 133(9) (2013), 2843-3206.

[Phe88] Thanases Pheidas, Hilbert’s tenth problem for a class of rings of
algebraic integers, Proc. AMS 104 (1988), 611-620.

[Phe91] —, Hilbert’s 10th Problem for ﬁelds of rational functions over ﬁnite
ﬁelds, Invent. Math. 103 (1991), 1-8.

[Phe94] —, Extensions of Hilbert’s 10th Problem, J. Symb. Logic 59(2)
(1994), 372-397.

[Phe04] —, Endomorphisms of elliptic curves and undecidability in function
ﬁelds of positive characteristic, J. Algebra 273(1) (2004), 395-411.

[PZ00] Thanases Pheidas, Karim Zahidi, Undecidability of existential the-
ories of rings and ﬁelds: A survey, in: [DLPG00] (2000), 49-105.

[Poo02] Bjorn Poonen, Using elliptic curves of rank one towards the unde-
cidability of Hilbert’s 10th Problem over rings of algebraic integers,
in: Claus Fieker, David R. Kohel (eds.) Algorithmic number theory,
Springer 2002, 33-42.

[Poo03] —, Hilbert’s 10th problem over rings of number-theoretic interest,
www-math.mit.edu/ poonen/papers/aws2003.pdf, 2003.

[Poo08] —, Undecidability in Number Theory, Notices AMS 55(3) (2008),
344-350.

[Poo09a] —, Characterizing integers among rational numbers with a
universal-existential formula, Amer. J. Math. 131(3) (2009), 675-
682.

[Poo09b] —, The set of nonsquares in a number ﬁeld is diophantine, Math.
Res. Lett. 16(1) (2009), 165-170.

[Pop96] Florian Pop, Embedding problems over large ﬁelds, Ann. Math. (2)
144(1) (1996), 1-34.
 46

[Pre81] Alexander Prestel, Pseudo real closed ﬁelds, in: Ronald B. Jensen,
Alexander Prestel (eds.) Set Theory and Model Theory, Springer
Lecture Notes 872 (1981), 127-156.

[PR84] Alexander Prestel, Peter Roquette, Formally p-adic ﬁelds, Springer
Lecture Notes 1050, 1984.

[PS90] Alexander Prestel, Joachim Schmid, Existentially closed domains
with radical relations, J. Reine Angew. Math. 407 (1990), 178-201.

[Rob49] Julia Robinson, Deﬁnability and decision problems in arithmetic, J.
Symb. Logic 14(2) (1949), 98-114.

[Rob52] —, Existential deﬁnability in arithmetic, Trans. AMS 72 (1952),
437-449.

[Rob59] —, The undecidability of algebraic rings and ﬁelds, Proc. AMS 10
(1959), 950-957.

[Rob62] —, On the decision problem for algebraic rings, in: Gabor Szegö
(ed.) Studies in Mathematical Analysis and related Topics, Stanford
1962, 297-304.

[RRo51] Raphael M.Robinson, Undecidable Rings, Trans. AMS 70(1)
(1951), 137-159.

[Rub95] Lee A. Rubel, An essay on diophantine equations for analytic func-
tions, Exp. Math 13 (1995), 81-92.

[Rum86] Robert Rumely, Arithmetic over the ring of all algebraic integers,
J. Reine Angew. Math. 368(5) (1986), 127-133.

[Sel51] Ernst S. Selmer, The diophantine equation ax
3 +by3 +cz3 = 0, Acta
Math. 85 (1951), 203-362 and 92 (1954), 191-197.

[Ser73] Jean-Pierre Serre, A course in arithmetic, Springer 1973.

[Shl92] Alexandra Shlapentokh, Hilbert’s 10th Problem for rings of alge-
braic functions in one variable over ﬁelds of constants of positive
characteristic, Trans. AMS 333 (1992), 275-298.

47

[Shl00] —, Hilbert’s 10th problem over number ﬁelds, a survey, in [DPLG]
(2000), 107-137.

[Shl07] —, Hilbert’s Tenth Problem, Diophantine classes and extensions to
global ﬁelds, CUP 2007.

[SS89] Alexandra Shlapentokh, Harold N. Shapiro, Diophantine relation-
ships between algebraic number ﬁelds, Comm. Pure Appl. Math. 42
(1989), 1113-1122.

[Sil86] Joseph H. Silverman, The arithmetic of elliptic curves, Springer
1986.

[Vdau03] Xavier Videaux, An analogue of Hilbert’s 10th problem for ﬁelds
of meropmorphic functions over non-Archimedean valued ﬁelds, J.
Number Theory 101 (2003), 48-73.

[Vid94] Carlos Videla, Hilbert’s 10th Problem for rational function ﬁelds in
characteristic 2, Proc. AMS 120(1) (1994), 249-253.

[Vid99] —, On the constructible numbers, Proc. AMS 127(3) (1999), 851-
860.

[Vid00] —, Deﬁnability of the ring of integers in pro-p Galois extensions of
number ﬁelds, Isr. J. Math. 118(1) (2000), 1-14.

Mathematical Institute, 24-29 St Giles’, Oxford OX1 3LB, UK
koenigsmann@maths.ox.ac.uk
 48
