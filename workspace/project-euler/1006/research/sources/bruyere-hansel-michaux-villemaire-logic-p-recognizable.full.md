<!-- source: https://www-verimag.imag.fr/~iosif/LAT/bru.pdf | converted from PDF -->

LOGIC AND p-RECOGNIZABLE SETS OF
INTEGERS

V´eronique Bruy`ere∗ Georges Hansel Christian Michaux∗†

Roger Villemaire‡

Abstract

We survey the properties of sets of integers recognizable by automata when
they are written in p-ary expansions. We focus on Cobham’s theorem which
characterizes the sets recognizable in diﬀerent bases p and on its generaliza-
tion to Nm due to Semenov. We detail the remarkable proof recently given
by Muchnik for the theorem of Cobham-Semenov, the original proof being
published in Russian.

1 Introduction

This paper is a survey on the remarkable theorem of A. Cobham stating that the
only sets of numbers recognizable by automata, independently of the base of repre-
sentation, are those which are ultimately periodic. The proof given by Cobham, even
if it is elementary, is rather diﬃcult [15]. In his book [24], S. Eilenberg proposed as
a challenge to ﬁnd a more reasonable proof. Since this date, some researchers found
more comprehensible proofs for subsets of N, and more generally of Nm.The more
recent works demonstrate the power of ﬁrst-order logic in the study of recognizable
sets of numbers [54, 49, 50].
One aim of this paper is to collect, from B¨uchi to Muchnik’s works [9, 54], all the
base-dependence properties of sets of numbers recognizable by ﬁnite automata, with
some emphasis on logical arguments. It contains several examples and some logical
proofs. In particular, the fascinating proof recently given by A. Muchnik is detailed

∗This work was partially supported by ESPRIT-BRA Working Group 6317 ASMICS and Co-
operation Project C.G.R.I.-C.N.R.S. Th´eorie des Automates et Applications.
†Partially supported by a F.N.R.S. travel grant. The author thanks for its hospitality the
Department of Mathematics and Computer Science of UQAM and the Centre Ricerca Matematica
at Barcelona.
‡The author thanks for its hospitality the team of Mathematical Logic at Paris 7 and also the
Department of Mathematics and Computer Science of UQAM for ﬁnancial support.

Received by the editors November 1993, revised February 1994.
Communicated by M. Boﬀa.
AMS Mathematics Subject Classiﬁcation : 11B85, 03D05, 68R15, 68Q45.
Keywords : inﬁnite words, p-recognizable sequences, ﬁnite automata, ﬁrst-order deﬁnabil-
ity, formal power series.

Bull. Belg. Math. Soc. 1 (1994), 191–238

192 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

and simpliﬁed. It states Cobham’s theorem and the generalization of Semenov to
Nm. The paper also contains bibliographic notes on the history of the results.
This survey is born of several lectures given by the authors, respectively V.
Bruy`ere, 29 April 93 - Universit´e Libre de Bruxelles, G. Hansel, 26 April and 3 May
93 - Universit´e Paris 6, C. Michaux, 2 September 92 - Universit´e de Mons-Hainaut
and R. Villemaire, 23 November 92 - University McGill, 3 December 92 - Universit´e
UQAM. It addresses readers accustomed with automata, but less familiar with ﬁrst-
order logic. It may be read in diﬀerent ways, depending on the interests of the
reader.
The paper is arranged in the following way. It begins with a brief section on
automata and a lesson of logic to make the reader more familiar with ﬁrst-order
structures, deﬁnable sets and decidable theories.
Next, Section 4 deals with p-recognizable sets of numbers, i.e., sets of numbers
whose p-ary expansions are recognizable by a ﬁnite automaton. Various characteri-
zations of p-recognizability are related in Theorem 4.1 : iterated uniform morphisms,
algebraic formal power series, and deﬁnability by ﬁrst-order formulae. Section 4 is
centered around these four models of p-recognizability. It begins and ends with two
generic examples. It also contains some bibliographic notes related to Theorem 4.1,
as well as notes about the automata associated with p-recognizable sets.
Section 5 is in the same spirit but for p-recognizable subsets of Nm. The four
models still hold and are again equivalent (Theorem 5.1).
Among the diﬀerent characterizations of p-recognizability, Section 6 emphasizes
the logical one. The currently simplest proof of this equivalence is given, following
the references [40, 74]. At the origin, it was proved by R. B¨uchi in his paper [9].
Some corollaries of decidability and non p-recognizability are easily derived, together
with a powerful tool for operations preserving p-recognizability (Corollaries 6.2, 6.3
and 6.4).
Next, Section 7 studies the dependence of p-recognizability on the base of repre-
sentation. In particular it contains Cobham’s theorem (Theorem 7.7). It shows that
there are essentially three kinds of subsets of Nm : the sets recognizable in every base
p, the sets recognizable in certain bases only, and the sets recognizable in no base.
The ﬁrst class is quite restricted, as it is limited to the rational sets of the monoid
(Nm, +). When m = 1, it is precisely the ultimately periodic sets. It is rather easy
to see that ultimately periodic sets are p-recognizable for every integer p ⩾ 2, but
the converse relies on the deep theorem of Cobham. As for p-recognizable sets, sets
recognizable in every base are characterized in various ways (Theorems 7.3 and 7.4),
including a logical characterization and a ﬁne deﬁnability criterion found recently
by A. Muchnik [54]. Muchnik’s criterion is at the heart of his remarkable proof of
Cobham’s theorem over Nm, it also allows one to decide whether a p-recognizable
set of Nm is recognizable in every base (Proposition 7.6).
Section 8 is devoted to Muchnik’s proofs of the deﬁnability criterion and of the
theorem of Cobham-Semenov over Nm. The original proof is in Russian. We follow
it, simplifying some parts and detailing others.
The last section is a brief introduction to related works and references. The list
is certainly not complete; however it may give a ﬂavour of connected research works.

Logic and p-recognizable sets of integers 193

2 Preliminaries

We brieﬂy recall some deﬁnitions about automata, automata with output and ra-
tional operations. These notions are well detailed in [24, 43, 58].
The sets A and B are ﬁnite alphabets.We denote by B∗ the set of all words
written with letters of B, including the empty word λ.Set B∗ is a monoid called
the free monoid generated by B, with concatenation as product operation and λ
as neutral element. The symbol |w| denotes the length of the word w ∈ B∗ and
wR the reverse of w.In this paper, A and B are often ﬁnite subsets of the set
N = {0, 1, 2,...} of natural numbers.
An automaton A =(Q, I, F, T ) is a graph with a set Q of vertices or states and
aset T ⊆ Q × B × Q of edges or transitions labelled by an alphabet B.Set I ⊆ Q
is the set of initial states and F ⊆ Q the set of ﬁnal states. A word w ∈ B∗ is
accepted (orcomputed)by A if it is the label of some path in A beginning with an
initial state and ending with a ﬁnal state. We say that L ⊆ B∗ is recognizable if
it is the set of words computed by some ﬁnite automaton, i.e., with Q ﬁnite. An
automaton A is deterministic if it has a unique initial state and if T is a (partial)
function T : Q × B → Q.If T is a total function, A is moreover called complete.
Automata with output generalize the concept of automaton. Instead of a set
F of ﬁnal states, they have an output function labelling each state by a letter of
some alphabet A. For classical automata, A = {0, 1}, and a state is labelled by 1
if it is ﬁnal; otherwise it is labelled by 0. An automaton with output computes a
relation R ⊆ B∗ × A in the following way : (w, a)is in R if and only if there is a
path labelled by w from some initial state to some state whose output is a.Any
complete deterministic automaton with output computes a function s : B∗ → A.
Several proofs in this paper use well-known properties of automata and recogniz-
able sets, for instance the equivalence between automata and complete deterministic
automata, the closure under Boolean operations of the family of recognizable sets,
and the equivalence between automata reading words from left to right and those
reading them from right to left.
In particular, we frequently use properties of right-congruences associated with
recognizable sets. Let L ⊆ B∗; recall that the following relation ∼L over B∗

u ∼L v ⇔ [ ∀w ∈ B∗,uw ∈ L ⇔ vw ∈ L ]

is a right-congruence, i.e., an equivalence relation which is right-stable :

u ∼L v ⇒ uw ∼L vw .

Set L is the union of some equivalence classes of ∼L.Moreover, L is recognizable if
and only if ∼L has ﬁnite index. All these porperties are known as the Myhill-Nerode
theorem.
The minimal automaton A(L) of a recognizable set L ⊆ B∗ is the smallest (in
number of states) complete deterministic automaton computing it. It is unique up
to isomorphism and can be constructed in the following way. Its states are the
classes of ∼L, the initial state is the class of the empty word and the ﬁnal states are
the classes containing the words of L. A transition labelled by b ∈ B goes from the
class of w to the class of wb.

194 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

The automaton A(L) has two nice properties. For any pair of distinct states
q, q′, there exists w ∈ B∗ such that T (q, w) is ﬁnal and T (q′,w)is not, orvice versa.
Any class C of ∼L is a state of A(L), but it is also the set of words labelling paths
from the initial state to state C.
As usual, the rational operations are ∪, · and ∗. They operate on sets of words
L, L
′ ⊆ B∗, L ∪ L
′ is their union, L·L
′ = {ww′ | w ∈ L, w′ ∈ L
′} their concatenation
and L
∗ the submonoid of B∗ generated by L.The set L ⊆ B∗ is then said to be
rational if it can be constructed from ﬁnite subsets of B∗ using a ﬁnite number of
rational operations. Kleene’s theorem states that L ⊆ B∗ is rational if and only if
it is recognizable.
The set N = {0, 1, 2,...} is also a monoid, with operation + and neutral element
0. The same holds for Nm,m ⩾ 2, with the vectorial sum + and neutral element 0.
We use the notation n for the m-tuple (n1,... ,nm). Rational operations and rational
subsets can also be deﬁned in these monoids. In Nm, the rational operations ∪, ·
and ∗ are interpreted as the operations ∪, + and the closure under addition (L
∗ is the
submonoid of Nm generated by L). On the other hand, the notion of recognizable
set is extended to Nm using the right-congruence deﬁned above : L ⊆ Nm is said to
be recognizable if the right-congruence ∼L has ﬁnite index. Kleene’s theorem holds
in N which is the free monoid generated by 1, but it is no longer true in Nm,m ⩾ 2.
Indeed, any recognizable subset is rational, but the converse is false. For instance
the diagonal L = {(n, n) | n ∈ N} is the rational set (1, 1)∗ of N2 but it is not
recognizable (since any two points (n, 0) and (m, 0) with n ̸= m are not equivalent
for ∼L) (see for example [58, page 16]).

3 Some Notions of Logic

In this section, we give a short lesson in ﬁrst-order logic. The reader is referred to
[3] for more details about ﬁrst-order logic.

3.1 Structures and Formulae

In the sequel, we will often meet the structures ⟨N, +⟩ and ⟨N, +,Vp⟩. In ﬁrst-order
logic, a structure S = ⟨D, (Ri)i∈I, (fj)j∈J, (ck)k∈K⟩

consists of a domain D (some set), a family of relations (Ri)i∈I on D, a family of
functions (fj)j∈J on D and a family of constants (ck)k∈K of D. The relation Ri is a
subset of Dni and fj is a function from Dnj to D.The set {(Ri)i∈I, (fj)j∈J, (ck)k∈K}
is called the language of the structure S.
For instance, the structure ⟨N, +⟩ has the set N of natural numbers as domain
and the usual function +. It has no relation and no constant.
First-order formulae of the structure S (or in the language of S) are constructed
by certain rules. But ﬁrst we need to list the symbols used in the formulae and to
deﬁne the terms.
In addition to the symbols of relations Ri, functions fj and constants ck,there
are also a countable set of variables x, y, z,..., the usual connectives ∨ (or), ∧ (and),

Logic and p-recognizable sets of integers 195

¬ (not), → (if then), ↔ (if and only if), the quantiﬁers ∀ (for all), ∃ (there exists)
and the symbol = (equal).
The terms are deﬁned by induction following two rules :

1. any variable and constant is a term,

2. if fj is a n-ary function and t1,...,tn are terms, then fj(t1,... ,tn) is a term.

The formulae are generated by four rules :

1. if t1,t2 are terms, then t1 = t2 is a formula,

2. if Ri is a n-ary relation and t1,... ,tn are terms, then Ri(t1,... ,tn)is a formula,

3. if ϕ, φ are formulae, then ϕ ∨ φ, ϕ ∧ φ, ¬ϕ, ϕ → φ, ϕ ↔ φ are formulae,

4. if ϕ is a formula and x is a variable, then ∀xϕ, ∃xϕ are formulae.

For clarity, parentheses (, ) are necessary during the construction of formulae. For-
mulae generated only by the ﬁrst two rules are called atomic formulae. Sentences
are formulae with no free variables, i.e., variables which are not under the scope of a
quantiﬁer. We sometimes write ϕ(x1,... ,xn) to explicitly mention the free variables
of the formula ϕ.
We point out that the presentation is here a bit diﬀerent from the one usually
given in logic textbooks.

3.2 Examples

The formula (∃z)(x + z = y)

of the structure ⟨N, +⟩ means “there exists z ∈ N such that x + z = y”; hence it
deﬁnes the relation x ⩽ y. The constant x = 0 can also be deﬁned in ⟨N, +⟩ by the
formula “x ⩽ y for all y ∈ N”, i.e.
 (∀y)(x ⩽ y)

where x ⩽ y is the formula above. More generally, any element of N can be deﬁned
in the language of ⟨N, +⟩.For x = 1, it is the following formula

(¬(x =0)) ∧ ((∀y)(¬(y =0)) → (x ⩽ y)) .

which means that x is not 0 and x ⩽ y for any y ∈ N\{0}.We use x =0 as a
short-hand for the formula (∀y)(x ⩽ y) deﬁning it.
It is also easy to see that the multiplication by a constant can be deﬁned in
⟨N, +⟩. Multiplication of x by 3, y =3x, is simply the formula y = x + x + x.
Finally, the property of commutativity of addition is described by the sentence

(∀x)(∀y)(x + y = y + x) .

196 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

3.3 Deﬁnable Sets and Functions

Let ϕ(x1,...,xn) be a formula of the structure S and d1,... ,dn elements of the
domain D. Weuse thenotation
 S|= ϕ(d1,...,dn)

to state that ϕ(x1,... ,xn) is true when the free variables xi are replaced by the
elements di of D,1 ⩽ i ⩽ n. Therefore

{ (d1,... ,dn) ∈ Dn |S |= ϕ(d1,... ,dn) }

is the set of n-tuples of elements of D for which ϕ is true. We say that this set is
ﬁrst-order deﬁnable (or in short deﬁnable) in the structure S by the formula ϕ.
We say that a constant c is deﬁnable in the structure S if the singleton {c} is
deﬁnable in S. A relation R is deﬁnable in S if the subset associated with R is
deﬁnable in S. In the same way, we say that a function f : Dn → D is deﬁnable in
the structure S if its graph

{ (d1,... ,dn,d) ∈ Dn+1 | f(d1,...,dn)= d }

is deﬁnable in S.
In this paper, we mainly study sequences (sn)n⩾0 and more generally multi-
dimensional sequences, whose values belong to a ﬁnite subset A of N. These se-
quences are simply functions s : Nm → A, m ⩾ 1. Thus, we can speak of ﬁrst-order
deﬁnable sequences.
For instance the sequence s : N → A deﬁned by sn = n mod 3 is deﬁnable in the
structure ⟨N, +⟩. Indeed, s
−1(0) is the set of multiples of 3 which is deﬁned by the
formula ϕ0(x) (∃z)(x =3z) .

The set s
−1(1) is deﬁned by ϕ1(x)equal to (∃z)(x =3z +1), and s
−1(2) by ϕ2(x)
equal to (∃z)(x =3z + 2). Therefore, the sequence s : N →{0, 1, 2},or equivalently
its graph, is ﬁrst-order deﬁnable by the following formula ϕ(x, y)

(ϕ0(x) ∧ y =0) ∨ (ϕ1(x) ∧ y =1) ∨ (ϕ2(x) ∧ y =2) .

This example also shows that a sequence s : Nm → A,with A a ﬁnite subset of
N, is deﬁnable if and only if all the sets s
−1(a),a ∈ A, are deﬁnable.

3.4 Equivalent Structures

Consider two structures S, S ′ with the same domain D.Any formula ϕ(x1,... ,xn)
of S deﬁnes the set

Mϕ = { (d1,... ,dn) ∈ Dn |S |= ϕ(d1,...,dn) } .

In the same way, any formula ϕ′ of S ′ deﬁnes the set Mϕ′.
We say that S and S ′ are equivalent if for every formula ϕ(x1,... ,xn)of S,there
exists a formula ϕ′(x1,... ,xn)of S ′ such that

Mϕ = Mϕ′

Logic and p-recognizable sets of integers 197

and conversely. In other words, the sets deﬁnable in S are the same as in S ′.
It is easy to check that two structures are equivalent. This holds if the relations,
the functions and the constants of the ﬁrst structure are deﬁnable in the second
structure, and conversely.
For instance, ⟨N, +⟩ and ⟨N, +, ⩽⟩ are equivalent structures, because ⩽ is de-
ﬁnable in ⟨N, +⟩ (see above). Another example of equivalent structures is ⟨N, +, ·⟩
and ⟨N, +,x2⟩,where · is the usual product and y = x2 the square function. The
function y = x2 is of course deﬁnable in ⟨N, +, ·⟩ and conversely the product x· y = z
is deﬁnable in ⟨N, +,x2⟩ by the formula

(x + y)2 = x2 +2· z + y2 .

Notice that any structure ⟨D, (Ri)i∈I, (fj)j∈J, (ck)k∈K⟩ is equivalent to a structure
with relations only. Functions fj and constants ck are easily replaced by relations
(its graph for the function fj and {ck} for the constant ck).

3.5 Decidable Theories

Given a structure S, the set of the sentences true for S is the theory of S, denoted
by Th(S). The theory Th(S)is decidable if there exists an algorithm which decides
if any sentence of S is true or false for S, i.e., if it belongs to Th(S)ornot. There
exist various techniques to prove the decidability of a theory : quantiﬁer elimination,
axiomatisation of the theory, ﬁnite automata [60].
A classical example of a decidable theory is Th(⟨N, +⟩) [59, 28], and an unde-
cidable theory is Th(⟨N, +, ·⟩) [14, 28].

4 Recognizability over N

4.1 An Appetizing Example

In this section we intuitively introduce four diﬀerent methods to generate the char-
acteristic sequence of the powers of 2. The deﬁnitions will be more precise in the
next section.
Let p : N →{0, 1} be the characteristic sequence of the powers of 2 :

011010001000000010 ... .

The alphabet is A = {0, 1} and pn =1 if n is a power of 2, pn = 0 otherwise. This
sequence has remarkable properties.

1. It is generated by a 2-substitution
Let
 f : {a, b, c}→ {a, b, c}2 : a → ab
b → bc
c → cc

g : {a, b, c}→ {0, 1} : a → 0
b → 1
c → 0

198 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

The iteration of f on the letter a gives rise to a sequence on the alphabet {a, b, c},
whose image by g is the sequence p.

a f
→ ab f
→ abbc f
→ abbcbccc f
→ abbcbcccbccccccc . . .
↓ g ↓ g ↓ g ↓ g ↓ g
0 → 01 → 0110 → 01101000 → 0110100010000000 ...

Figure 1. Iteration of the 2-substitution f

2. It is 2-recognizable
The sequence p is computed by the following ﬁnite automaton with output (the
output of each state is indicated under the state).

Figure 2. An automaton computing p in base 2

The automaton computes the symbol pn from the binary expansion (n)2 of n.More
precisely the automaton reads the word (n)2 (the most signiﬁcant digit of (n)2 is
read ﬁrst) from the initial state q0 to some state q whose output symbol is pn.For
instance, the binary expansion (8)2 of 8 is 1000, the state reached after reading 1000
is q1 with output 1, so p8 =1.

3. It is 2-deﬁnable
Consider the structure ⟨N, +,V2⟩ where V2 is the function deﬁned by

V2(x)= y where y is the greatest power of 2 dividing x (x ̸=0),
V2(0) = 1.

The sequence p is ﬁrst-order deﬁnable in ⟨N, +,V2⟩ since the subsets of integers
p
−1(0) and p
−1(1) are both deﬁnable by a formula of ⟨N, +,V2⟩ (see Section 3.3).
Indeed pn =1 if and only if n is a power of 2 if and only if V2(n)= n.Let P2(x)be
the formula V2(x)= x;then

p
−1(1) = { n ∈ N |⟨N, +,V2⟩|= P2(n) } ,
p
−1(0) = { n ∈ N |⟨N, +,V2⟩|= ¬P2(n) } .

4. It is 2-algebraic
Consider the ﬁnite ﬁeld F2 = {0, 1}.The formal power series P (x) ∈ F2[[x]]

P (x)= ∑

n⩾0 pnxn = ∑

n⩾0 x2n

is naturally associated with the sequence p. One veriﬁes that P (x) is algebraic over
the ring F2[x], i.e., P (x) is a root of the following polynomial Q(t) with coeﬃcients
in F2[x]: Q(t)= t2 + t + x.

Indeed, P (x)2 = P (x2)= P (x) − x (remember that −1= 1 and (a + b)2 = a2 + b2

in F2).

Logic and p-recognizable sets of integers 199

4.2 Four Modes of Computing

We now give precise deﬁnitions of the four methods intuitively described in the
previous section. Theorem 4.1 states that they all generate the same sequences.
Let p ⩾ 2 be an integer and s : N → A a sequence with values in a ﬁnite alphabet
A ⊂ N.

1. p-substitution
Let B be a ﬁnite alphabet. Let f : B → Bp be a function called a p-substitution,
which replaces each letter of B by some word of B∗ of length p. The function f
can be extended to a morphism on B∗.If f(b) begins with the letter b for some
b ∈ B, then the sequence (f n(b))n⩾0 converges towards a ﬁxed point f ω(b)of f.Let
g : B → A be a function. Then, the image by g of the ﬁxed point f ω(b) yields a
sequence s : N → A.
A sequence s generated by this kind of process is said to be generated by p-
substitution.

2. p-automaton
A p-automaton is a complete deterministic ﬁnite automaton with output, whose
transitions are labelled by {0, 1,...,p − 1} and whose states are labelled by A (the
output).
A sequence s is called p-recognizable if it is computed by some p-automaton in
the following way. The p-ary expansion (n)p of n ∈ N is a word of {0, 1,...,p − 1}∗.
Starting in the initial state and using the transitions labelled by the letters of (n)p,
one reaches some state q.Then sn is equal to the output of q.The way a p-
automaton reads (n)p is from the most signiﬁcant digit to the least one; this choice
is arbitrary.

3. p-deﬁnability
We consider the structure ⟨N, +,Vp⟩, where the function Vp is deﬁned as

Vp(x)= y where y is the greatest power of p dividing x (x ̸=0),
Vp(0) = 1.

A sequence s is p-deﬁnable if for each letter a ∈ A, there exists a ﬁrst-order formula
ϕa of ⟨N, +,Vp⟩ such that

s
−1(a)= { n ∈ N |⟨N, +,Vp⟩|= ϕa(n) } .

4. p-algebraicity
We assume that p is a prime number.
Let K be a ﬁnite ﬁeld with characteristic p such that A is embedded into K (for
instance K = Fp = {0, 1,...,p − 1} if the cardinality of A is less than or equal to
p). With the sequence s is associated the formal power series

S(x)= ∑

n⩾0 snxn ∈ K[[x]] .

We say that s is p-algebraic if S(x) is algebraic over K[x], i.e., if there exist poly-
nomials qi(x) ∈ K[x] such that S(x) is a root of

Q(t)= qj(x)tj + qj−1(x)tj−1 + ··· + q0(x) ∈ K[x][t]\{0} .

200 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

Theorem 4.1 Let p ⩾ 2 be an integer and s : N → A a sequence with values in a
ﬁnite alphabet A ⊂ N. The following are equivalent :
(1) s is generated by p-substitution,
(2) s is p-recognizable,
(3) s is p-deﬁnable,
(4) s is p-algebraic (under the additional assumption that p is prime).

Some hints on the proof are given in Section 4.4.
There exist sequences which are not p-recognizable, for any p ⩾ 2; for instance
the characteristic sequence of the squares, or the prime numbers (see [9, 63, 51]; see
also Corollary 6.3).

4.3 Notes on p-Automata

Given an integer n,its p-ary expansion is the word (n)p = w0w1 ...wk of {0, 1,...,p−
1}∗ such that w0 ̸=0 and

n = w0p
k + w1p
k−1 + ··· + wkp
0 .

By convention, (0)p is the empty word λ. Conversely, to any word w = w0w1 ...wk ∈
{0,...,p − 1}∗ corresponds its value [w]p ∈ N equal to w0p
k + w1p
k−1 + ··· + wkp
0.
Diﬀerent words can have the same integer as value, due to the leading zeros. In fact,
any n ∈ N has an inﬁnite number of representations w such that [w]p = n;it is the
inﬁnite set 0
∗(n)p.
By deﬁnition, p-automata only treat the p-ary expansion of each integer n.We
can always suppose that a transition labelled by 0 exists, which loops on the initial
state q0. In this way, the p-automaton identically treats all the words w such that
[w]p = n (see Figure 2). From now on, we will always assume that any p-automaton
has a loop labelled by 0 on its initial state.
The family of p-recognizable subsets of N are also much studied. We say that
M ⊆ N is p-recognizable if its characteristic sequence m : N →{0, 1} deﬁned by

mn =1 ⇔ n ∈ M

is p-recognizable.
Equivalently M is p-recognizable if and only if there is a ﬁnite automaton ac-
cepting the set { w ∈{0,... ,p − 1}∗ | [w]p ∈ M }. This automaton is, for instance,
some p-automaton computing the sequence m whose states with output 1 are con-
sidered as ﬁnal states. Actually we have the following more general result, stating
that p-recognizability is independent of leading zeros (see [24, page 106]).

Proposition 4.2 Aset M ⊆ N is p-recognizable if and only if there exists a ﬁnite
(deterministic or not) automaton accepting L ⊆{0,... ,p − 1}∗ such that

M = {[w]p | w ∈ L} .

It is also possible to characterize p-recognizable sets M of integers by an equiva-
lence relation of ﬁnite index (see [24, page 107]. This relation is just the translation to

Logic and p-recognizable sets of integers 201

N of the right-congruence ∼L of a ﬁnite automaton computing L = { w | [w]p ∈ M }
(see Section 2). More precisely, the relation ∼p,M is deﬁned as follows. Let n, m ∈ N,

n ∼p,M m ⇔ [ np
k + r ∈ M ⇔ mp
k + r ∈ M ∀k ⩾ 0, ∀r 0 ⩽ r< p
k ] .

Consequently, we have

Proposition 4.3 Aset M ⊆ N is p-recognizable if and only if the equivalence
relation ∼p,M has ﬁnite index.

In the sequel, we will need automata reading p-ary expansions of integers from
right to left instead of left to right. In that case, the equivalence relation ∼p,M R is
slightly diﬀerent :

n ∼p,M R m ⇔ [ n + rp
k ∈ M ⇔ m + rp
l ∈ M ∀r, ∀p
k >n, p
l >m ] .

We have the analogues of Proposition 4.2 and Proposition 4.3 when reading words
from right to left. Since reading from left to right does not change the concept, the
choice is a matter of convenience. Later we will see that reading from right to left
is a good choice for generalization to higher dimensions.
We have seen that p-recognizable sets of integers coincide with p-recognizable
characteristic sequences. Conversely any p-recognizable sequence s : N → A with
values in a ﬁnite alphabet A is associated with the p-recognizable sets s
−1(a) ⊆ N.
Indeed, if A is a p-automaton for s,then s
−1(a) is computed by A where the states
with output a are considered as the ﬁnal states [24, Chapter 15].

Proposition 4.4 Let A ⊂ N be a ﬁnite alphabet and s : N → A a sequence. Then
s is p-recognizable if and only if each set s
−1(a), a ∈ A,is p-recognizable.

This proposition allows to transfer theorems on p-recognizable sets into theorems
on p-recognizable sequences. We will often use this principle in the sequel.
As for p-recognizable sets M ⊆ N,any p-recognizable sequence s is characterized
by the ﬁnite index of the equivalence ∼p,s (or ∼p,sR ) deﬁned by

n ∼p,s m ⇔ snpk+r = smpk+r ∀k, ∀r<p
k .

4.4 Bibliographic Notes

Theorem 4.1 results from several independent works.

The equivalence (1) ⇔ (2) is proved in [16] (see also [24, Chapter 15]). The idea
of the proof is the following. Let A be a p-automaton computing the sequence s.
Let Q be the set of states, q0 the initial state and T : Q ×{0,... ,p − 1}→ Q the
transition function. We can suppose that T (q0, 0) = q0 (see Section 4.3). We deﬁne
the p-substitution f : Q → Qp by

f(q)= T (q, 0)T (q, 1) ··· T (q, p − 1)

for each q ∈ Q. The function f has a ﬁxed point f ω(q0) because f(q0) begins with
q0.Let g be the function from Q to A deﬁned by g(q) equal to the output of q.Then

202 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

the image by g of the ﬁxed point of f is the sequence s (this is proved by induction
on the length of the p-ary expansion of n). The proof of the reversed implication
uses the same construction backwards.

The equivalence (2) ⇔ (4) is proved in [13] (see also [12]). Here p-automata for
the sequence s read p-ary expansions of n from right to left (see Section 4.3). The
proof is not easy; it is based on the ﬁniteness of the p-kernel of the sequence s.The
p-kernel is the set of subsequences of s equal to

{(snpk+r)n⩾0 | k ⩾ 0,r < p
k} .

The p-kernel is ﬁnite if and only if the equivalence relation ∼p,sR has ﬁnite index.

The equivalence (2) ⇔ (3) is proved in detail in Section 6, following [40, 74].
The ﬁrst proof of this equivalence was given by J. R. B¨uchi in 1960 [9]. It was
well detailed for p = 2 but just sketched for p> 2. B¨uchi proved that sequences
are 2-recognizable if and only if they are deﬁned by weak-monadic second-order
formulae of the structure ⟨N,S⟩ where S is the successor function
1. Roughly the
formulae describe how 2-automata compute 2-recognizable sequences. B¨uchi then
stated that these formulae are equivalent to ﬁrst-order formulae of the structure
⟨N, +,P2⟩,where P2(x) is the unary relation “x is a power of 2”.
In 1963, R. MacNaughton reviewed B¨uchi’s paper [46]. He noticed that this
equivalence with the structure ⟨N, +,P2⟩ was not correctly proved. He suggested
replacing it with the structure ⟨N, +, ∈2⟩,where ∈2(x, y) is the binary relation “y is
a power of 2 occurring in the binary expansion of x” (here “occurring” means that
the coeﬃcient of y is 1 in the binary expansion of x, i.e., x = ∑

∈2(x,y) y).

Referring to the works of [46, 72], M. Boﬀa suggested the use of the structure
⟨N, +,Vp⟩ instead of ⟨N, +,Pp⟩ [7]. This led to the work [8] where B¨uchi’s proof was
detailed and corrected for any p ⩾ 2. The implication (3) ⇒ (2) is proved directly
without any use of weak-monadic second-order formulae, based on the reference [40].
The other implication is in the same spirit as in [9].
C. Michaux and F. Point gave in 1986 another proof of (2) ⇔ (3) [48]. The proof
of the implication (3) ⇒ (2) was the same as in [8]. For the converse, they used an
induction on rational expressions over the alphabet {0,... ,p − 1}.
Recently, R. Villemaire gave a short proof for the implication (2) ⇒ (3) directly
using ﬁrst-order formulae describing sets of integers computed by p-automata [73,
74].
Let us come back to the structures ⟨N, +,P2⟩, ⟨N, +, ∈2⟩ and ⟨N, +,V2⟩.It
is easy to see that ⟨N, +, ∈2⟩ and ⟨N, +,V2⟩ are equivalent structures [48]. The
predicate P2(x) is deﬁnable in ⟨N, +,V2⟩ by the formula V2(x)= x. However A.
Semenov proved in [67] that the function V2 is not deﬁnable in ⟨N, +,P2⟩.This
shows that ⟨N, +,P2⟩ and ⟨N, +,V2⟩ are not equivalent structures, as conjectured by
MacNaughton [46].
More generally, the structures ⟨N, +,Pp⟩ and ⟨N, +,Vp⟩ are not equivalent. This
property is a corollary of several decidability results; this has been ﬁrst noticed by

1Weak-monadic second-order formulae of ⟨N,S⟩ are generalizations of ﬁrst-order ones by allow-
ing additional variables describing ﬁnite subsets of N and quantiﬁcation over them.

Logic and p-recognizable sets of integers 203

F. Delon [20] (see Figure 3). The theories of the following ﬁrst-order structures are
decidable : ⟨N, +,Vp⟩ [8], ⟨N, +,p
x⟩ where p
x is the exponential function [68, 11].
However, one can show that the theory of ⟨N, +,Vp,p
x⟩ is undecidable (see [11] or
[73]). On the other hand, Pp is deﬁnable in ⟨N, +,Vp⟩ and ⟨N, +,p
x⟩.

⟨N, +,Vp⟩ decidable
↗↘
⟨N, +,Pp⟩ decidable ⟨N, +,Vp,p
x⟩ undecidable
↘↗
⟨N, +,p
x⟩ decidable

Figure 3. Deﬁnability relations between four structures

Assume now that ⟨N, +,Pp⟩ and ⟨N, +,Vp⟩ are equivalent. Then the undecidable
theory ⟨N, +,Vp,p
x⟩ is equivalent to ⟨N, +,Pp,p
x⟩, itself equivalent to the decidable
theory ⟨N, +,p
x⟩. This is impossible.

4.5 A Dessert Example

We end Section 4 by considering the remarkable Thue-Morse sequence t : N →{0, 1}

1001011001101001 ... .

The alphabet is A = {0, 1} and tn =1 if (n)2 has an even number of 1, tn =0
otherwise. This sequence has all the properties described in Theorem 4.1.
It is easy to ﬁnd a 2-automaton computing it. This automaton counts the sym-
bols 1 inside the words w ∈{0, 1}∗.

Figure 4. A 2-automaton for the Thue-Morse sequence

From this automaton, we construct the following 2-substitution (see Section 4.4) :

f : 0 → 01
1 → 10 g :identity

One of the two ﬁxed points of f is the sequence t, the other is the sequence 1 − t.
The sequence t is also 2-algebraic. Indeed its 2-kernel

{ (tn2k+r)n⩾0 | k ⩾ 0,r < 2
k }

has two elements : the sequences t (for k =1,r =0) and 1 − t (for k =1,r =1).
Then
 T (x)= ∑ t2nx2n + ∑ t2n+1x2n+1

= ∑ tnx2n + ∑(1 − tn)x2n+1

= T (x2)+ x
1+ x2 − xT (x2) .

204 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

The series T (x) is a root of the polynomial

Q(t)= (1 + x)3t2 +(1 + x)2t + x ∈ F2[x][t] .

Finally t is 2-deﬁnable. We just give an idea of a formula of ⟨N, +,V2⟩ deﬁning
it. It will be made more precise in Section 6. The required formula should say that
tn = 1 if and only if the binary expansion (n)2 of n contains an even number of 1’s.
Equivalently, there exists an integer m such that (m)2 “counts” the even number
of 1’s in (n)2. Roughly, (m)2 is constructed from (n)2 by keeping one 1 among
two consecutive 1’s of (n)2 and replacing the other by 0, as shown on the following
example (for simplicity the case n = 0 is treated separately).

(n)2 = 100110100101000
(m)2 = 000100100001000

More precisely, tn =1,n ⩾ 1, if and only if ⟨N, +,V2⟩|= ϕ(n) where the formula
ϕ(x)says thatthere exists y such that

1. the ﬁrst power of 2 occurring in the 2-expansion of x is thesamethan the one
occurring in y ( V2(x)= V2(y)),

2. the last power of 2 (denoted by λ2(x)) occurring in the 2-expansion of x does
not occur in y ( ¬∈2(y, λ2(x)) ),

3. for any two consecutive powers of 2 occurring in x, one occurs in y if and only
if the other one does not.

This is a formula of ⟨N, +,V2⟩, because ∈2(x, y)and λ2(x) are deﬁnable in ⟨N, +,V2⟩.

5 Recognizability over Nm

5.1 Four Modes of Computing

The four modes of computing p-recognizable sequences s : N → A remain applicable
for functions s : Nm → A, for every m ⩾ 2. These functions s are called again
sequences. Theorem 4.1 is still valid in this general context. For simplicity, we only
consider sequences s : N2 → A. Each of the following deﬁnitions is easily generalized
to sequences s : Nm → A, for any m> 2.
Let p ⩾ 2 be an integer and s : N2 → A a sequence. We adapt to N2 the
four deﬁnitions of p-substitution, p-automaton, p-deﬁnability and p-algebraicity. We
illustrate each of them with a particular sequence t : N2 →{0, 1}, essentially Pascal’s
triangle modulo 2. It is deﬁned by tn,m =0 if, for some k ⩾ 0, the same power 2
k of
2 occurs in the binary expansions of n and m,otherwise tn,m =1.

Logic and p-recognizable sets of integers 205

↑ m ...

10 000 000
11 000 000
10 100 000
11 110 000
10 001 000 ···
11 001 100
10 101 010
11 111 111 n
→

Figure 5. A sequence similar to Pascal’s triangle modulo 2

1. p-deﬁnability
The sequence s is called p-deﬁnable if for any a ∈ A,the set s
−1(a) ⊆ N2 is
deﬁnable by a ﬁrst-order formula ϕa(x, y)of ⟨N, +,Vp⟩.
The example of sequence t is deﬁnable in ⟨N, +,V2⟩. Indeed the formula ϕ(x, y)

(∃z)( ∈2(x, z) ∧∈2(y, z))

deﬁnes the set t−1(0) ⊆ N2 and its negation deﬁnes the set t−1(1).

2. p-automaton
A p-automaton is a complete deterministic ﬁnite automaton with output (in the
alphabet A). Its transitions are labelled by the alphabet {0,...,p − 1}2 in a way to
read pairs of integers.
More precisely, any word (u, v) over the alphabet {0,... ,p − 1}2 has components
u, v with the same length. Its value ([u]p, [v]p)is a pair (n, m) of integers. It may
happen that u has leading zeros and v not, as |u| = |v|. Conversely, given a pair
(n, m) of integers (suppose for instance that n ⩾ m), let u =(n)p,v =(m)p and
i = |u|− |v|,then (0, 0)∗(u, 0
iv)is the setof all pairs (u′,v′) over the alphabet
{0,...,p − 1}2 such that [u′]p = n, [v′]p = m.
This p-automaton computes a p-recognizable sequence s : N2 → A in the follow-
ing way. Let (u, v) ∈ [{0,... ,p − 1}2]∗ such that n =[u]p,m =[v]p. Starting with
the initial state, the reading of (u, v) leads to some state whose ouput deﬁnes sn,m.
It is easy to construct a 2-automaton computing the particular sequence t.The
alphabet labelling the edges is {0, 1}2 = {( 0
0
 ) , ( 1
0
 ) , ( 0
1
 ) , ( 1
1
 )}.

Figure 6. A 2-automaton for sequence t

3. p-substitution
Let B be a ﬁnite alphabet. Let f : B → Bp×p be a p-substitution, it replaces
each letter of B by some square of Bp×p with side p. The substitution f extends

206 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

into a function operating over the set of squares (see the example below). It has
a ﬁxed point if the bottom-left corner of f(b)is equal to b for some letter b ∈ B.
Let g : B → A be a function; the image by g of this ﬁxed point yields a sequence
s : N2 → A.
A sequence s generated by this kind of process is said to be generated by p-
substitution.
The example t is generated by 2-substitution, in the following way. We construct
it by looking at the 2-automaton of Figure 6 (see also Section 4.4). Let A = B =
{0, 1}.Then f : B → B2×2 is deﬁned as

f(1) = 10
11 ,f(0) = 00
00

The function g : B → A is here the identity. The iteration of f on 1gives aﬁxed
point whose image by g is the sequence t.
 100 000 00
110 000 00
101 000 00
111 100 00
1 000 100 010 00
1 100 110 011 00
10 1 010 101 010 10
1 → 11 → 1 111 → 111 111 11 → ...

Figure 7. Iteration of the 2-substitution f

4. p-algebraicity
We assume that p is a prime number.
Let K be a ﬁnite ﬁeld with characteristic p such that A is embedded into K.
The sequence s : N2 → A is p-algebraic if the formal power series

S(x, y)= ∑

n,m⩾0 sn,mxnym ∈ K[[x, y]]

is algebraic over K[x, y], i.e., there exist polynomials qi(x, y) ∈ K[x, y] such that
S(x, y) is a root of the polynomial

Q(t)= qj(x, y)tj + qj−1(x, y)tj−1 + ··· + q0(x, y) ∈ K[x, y][t]\{0} .

The sequence t is 2-algebraic because the series T (x, y) is algebraic over F2[x, y]:

(1 + x + y)T (x, y)+ 1 = 0 .

Indeed, considering the 2-kernel of t,wesee that tn,m = t2n,2m = t2n+1,2m = t2n,2m+1
and that t2n+1,2m+1 =0 for all n, m ⩾ 0. So

T (x, y)= ∑ t2n,2mx2ny2m + ∑ t2n+1,2mx2n+1y2m

+ ∑ t2n,2m+1x2ny2m+1 + ∑ t2n+1,2m+1x2n+1y2m+1

=(1 + x + y) ∑ tn,mx2ny2m +0
=(1 + x + y)T (x2,y2) .

Logic and p-recognizable sets of integers 207

Theorem 5.1 Let p ⩾ 2 and m ⩾ 1.Let s : Nm → A be a sequence. The following
are equivalent :
(1) s is generated by p-substitution,
(2) s is p-recognizable,
(3) s is p-deﬁnable,
(4) s is p-algebraic (under the additional assumption that p is a prime number).

In each of the four modes, m is respectively the dimension of f(b),b ∈ B where f
is a p-substitution for s, the number of components of letters labelling the transitions
of a p-automaton computing s, the number of variables of a formula deﬁning s in
⟨N, +,Vp⟩, or the number of variables of the formal power series associated with s.

5.2 Notes

Several authors have independently contributed to Theorem 5.1. They all ob-
served that in Nm,m ⩾ 2, the “good” p-automata are those reading m-tuples
(w1,... ,wm)with components wi of equal length. In other words, the “good”
monoid is [{0,... ,p − 1}m]∗ rather than [{0,...,p − 1}∗]m. The monoid [{0,... ,p −
1}m]∗ is free, so Kleene’s theorem holds.
The proof of equivalence (1) ⇔ (2) is in the same spirit as for Theorem 4.1
(see [10] where more general substitutions and automata are also considered). We
followed this idea for the example t. The equivalence (2) ⇔ (3) was already included
in the one-dimensional case (see Section 4.4). It is proved in details in the next
section. The equivalence (2) ⇔ (4) is established in [23]. See also [64, 65] for
another proof of equivalences (1) ⇔ (2) ⇔ (4).
All the notes we gave for p-automata labelled by {0,... ,p − 1} still hold for the
labelling by {0,... ,p − 1}m, m ⩾ 2. By deﬁnition, p-recognizable sets M ⊆ Nm

are those sets whose characteristic sequence m : Nm →{0, 1} is p-recognizable.
Conversely, any p-recognizable sequence s : Nm → A gives the p-recognizable sets
s
−1(a) ⊆ Nm, a ∈ A.

Proposition 5.2 Let m ⩾ 1 and s : Nm → A be a sequence. Then s is p-
recognizable if and only if each set s
−1(a), a ∈ A,is p-recognizable.

6 Logic and Automata

We give here a simple proof of the equivalence (2) ⇔ (3) of Theorem 5.1. We
consider sets M ⊆ Nm instead of sequences s : Nm → A (see Proposition 5.2). The
proof follows the ideas of references [40, 74].

Theorem 6.1 Let m ⩾ 1 and M ⊆ Nm.Let p ⩾ 2.Then M is p-recognizable if
and only if M is p-deﬁnable.

Proof. (1) First we construct a ﬁnite automaton Aϕ for any formula ϕ(x1,... ,xm)
of ⟨N, +,Vp⟩ deﬁning the set

Mϕ = { (n1,...,nm) ∈ Nm |⟨N, +,Vp⟩|= ϕ(n1,...,nm) } .

208 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

This automaton Aϕ computes the set of all words (w1,...,wm) over the alphabet
{0,...,p − 1}m such that ([w1]p,..., [wm]p) ∈ Mϕ

(all the possible leading zeros are considered), it reads words from right to left, it is
complete and deterministic (see Sections 4.3 and 5.2).
The proof is by induction on the formulae. For simplicity of the proof, we work
with the structure ⟨N,R+,RVp⟩,where R+(x, y, z) is the relation x + y = z and
RVp(x, y) is the relation Vp(x)= y. This structure is equivalent to ⟨N, +,Vp⟩ (see
Section 3.4)
Theatomicformulae of ⟨N,R+,RVp⟩ are the equality x = y and the two relations
R+(x, y, z), RVp(x, y). The corresponding sets M=, M+, MVp are p-recognizable.
Indeed, for p = 2, the automata A=, A+, AVp are the following ones (each ﬁnal state
is denoted by an outgoing small arrow). The addition realized by A+ is the usual
addition with carry.
 Figure 8.1 Automata A= and A+ in base 2

Figure 8.2 Automaton AV2 in base 2

Now, by induction, assume that automata Aϕ and Aψ are constructed, for for-
mulae ϕ and ψ respectively. We show how to obtain automata Aϕ∨ψ, A¬ϕ and A∃xϕ.
First, consider the formula φ(x1,... ,xk,y1,... ,yl,z1,... ,zm) deﬁned as

ϕ(x1,... ,xk,y1,... ,yl) ∨ ψ(y1,...,yl,z1,... ,zm) .

Logic and p-recognizable sets of integers 209

Any edge of Aϕ is labelled by some letter (a1,... ,ak,b1,... ,bl) of the alphabet
{0,...,p − 1}k+l. We replace this letter by the set of letters

{(a1,...,ak,b1,... ,bl)}×{0,... ,p − 1}m .

In the same way, for any edge of Aψ, we replace its labelling (b1,... ,bl,c1,...,cm) ∈
{0,...,p − 1}l+m by the set of letters

{0,...,p − 1}k ×{(b1,... ,bl,c1,...,cm)} .

The two new automata have now their labelling in the same alphabet {0,...,p −
1}k+l+m. Their union gives the automaton Aφ∨ψ.
Secondly, consider the formula ϕ(x1,... ,xk) and the automaton Aϕ.The set
M¬ϕ is equal to Nk\Mϕ. The automaton A¬ϕ is simply the complement of Aϕ.
Finally, given the formula ϕ(x, x1,...,xk) and the automaton Aϕ,it remains to
construct the automaton A∃xϕ associated with the formula ∃xϕ(x, x1,...,xk). The
alphabet labelling the transitions of Aϕ is {0,...,p−1}k+1. Each letter (a, a1,... ,ak)
is then replaced by the letter (a1,... ,ak)where a is suppressed. The new automa-
ton is generally no longer in the suitable form : it may be not deterministic, and a
problem with the lack of leading zeros may happen whenever the label (a, 0,... , 0)
of a transition in Aϕ going to a ﬁnal state has been replaced by (0,..., 0). To solve
the last problem, use Proposition 4.2 in a way to have again all possible leading
zeros. Now the non deterministic automaton can be transformed to a deterministic
one in the usual way.

(2) For the converse, we show how to encode any automaton in ⟨N, +,Vp⟩.
First we introduce p new relations ∈0,p(x, y), ∈1,p(x, y),... , ∈p−1,p(x, y)and a new
function λp(x), generalizing ∈2(x, y)and λ2(x) introduced in Sections 4.4 and 4.5.
The relation ∈j,p(x, y), for 0 ⩽ j< p,means that y is a power of p,and the coeﬃcient
of y in the p-ary expansion of x is equal to j, i.e., x = ∑

∈j,p(x,y) j· y.For powers y

strictly greater than x,weconsider ∈0,p(x, y) to be satisﬁed (leading zeros). The
function λp(x) denotes the greatest power of p occurring with a nonzero coeﬃcient
in the p-ary expansion of x.By convention, λp(0) = 1.
The relation ∈j,p(x, y), 0 ⩽ j< p, is deﬁnable in ⟨N, +,Vp⟩ by the formula

Pp(y) ∧ [(∃z)(∃t)(x = z + j· y + t) ∧ (z< y) ∧ ((y< Vp(t)) ∨ (t =0) ) ] .

Roughly this formula says that the powers of p of the p-ary expansion of x are shared
into three groups : one group is y only (or equivalently the integer j· y), the powers
less than y are the second group (the integer z) and the powers greater than y are
the third group (the integer t). So, it is possible to express in ⟨N, +,Vp⟩ the diﬀerent
letters w0,...,wk of the p-ary expansion (n)p = w0 ... wk of any integer n,as well
as leading zeros.
There is also a formula in ⟨N, +,Vp⟩ for λp(x)= y :

[ Pp(y) ∧ y ⩽ x ∧ ((∀z)(Pp(z) ∧ y< z) → (x<z)) ]
∨ [(x =0) ∧ (y =1) ]

210 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

which means that y is a power of p less than or equal to x, such that any power of
p greater than y must be greater than x.
We now complete the proof of the theorem. The set M ⊆ Nm is p-recognizable by
hypothesis. Let A be a complete deterministic ﬁnite automaton with set of states Q,
initial state q0, set of ﬁnal states F and transition function T : Q×{0,...,p−1}m →
Q. For simplicity we suppose that A reads words from right to left. The m-tuple
(n1,...,nm) belongs to M if and only if there exists a word (w1,... ,wm)over the
alphabet {0,... ,p − 1}m such that [wi]p = ni, 1 ⩽ i ⩽ m,and if the m-tuple of
reversed words (wR
1 ,... ,wR
m)labels a path in A from q0 to some state q ∈ F .This
deﬁnes a ﬁnite sequence q0 ... q of states, beginning with q0, ending with q,and
respecting the transitions.
Without loss of generality, we can replace any of the l states of A by a l-tuple of
letters of {0,...,p − 1}, respectively q0 by (1, 0,..., 0), q1 by (0, 1, 0,..., 0),... and
ql−1 by (0,..., 0, 1). The ﬁnite sequence q0 ...q is now a word (u1,... ,ul)over the
alphabet {0,...,p− 1}l. This sequence can also be considered as a particular l-tuple
of integers (y1,... ,yl) equal to ([u1]p,..., [ul]p). The formula we want to construct
describes such a l-tuple.
For any integer n,we denoteby n(i),i ⩾ 0, the digit j such that ∈j,p (n, p
i)is
true. So n = ∑+∞
i=0 n(i)p
i. For any state q, wedenoteby q(i)its ith component,
1 ⩽ i ⩽ l.
Now (x1,...,xm) belongs to M if and only if there exists a l-tuple of integers
y1,... ,yl such that

1. (y1(0),... ,yl(0)) is the initial state q0 =(1, 0,..., 0),

2. (y1(k),... ,yl(k)) is some ﬁnal state of F ,with p
k ⩾ max
1⩽j⩽m λp(xj),

3. for all 0 ⩽ i< k,if (y1(i),... ,yl(i)) is the state q,then (y1(i +1),...,yl(i +1))
is the state T (q, (x1(i),... ,xm(i))).

These three conditions can be expressed by a formula ϕ(x1,... ,xm), precisely :

(∃y1) ... (∃yl)(∃z) Pp(z)
∧ (z ⩾ max
1⩽j⩽m λp(xj))

∧ ϕ1(y1,...,yl)
∧ ϕ2(y1,...,yl,z)
∧ ϕ3(x1,...,xm,y1,... ,yl,z)

with ϕ1 : ⋀l
j=1 ∈q0(j),p (yj, 1)
ϕ2 : ⋁

q∈F
 ⋀l
j=1 ∈q(j),p (yj,z)

ϕ3 :(∀t)( Pp(t) ∧ (t< z) ∧
⋀

T (q,(a1,...,am))=q′ [ ⋀l
j=1 ∈q(j),p (yj,t) ∧ ⋀m
j=1 ∈aj,p (xj,t)
→ ⋀l
j=1 ∈q′(j),p (yj,p· t)] .

Do notforgetthatthe automaton A is given and therefore is considered as a constant
in the previous formula.

Logic and p-recognizable sets of integers 211

Another simple proof of B¨uchi’s theorem is given in [71]. It has the same structure
as ours, but it uses second-order formulae applied to words (as in [9]) instead of
ﬁrst-order formulae applied to integers. So the proof given in [71] together with a
standard (for logicians) translation from second-order to ﬁrst-order logic, leads to
another way of proving Theorem 6.1.
The ﬁrst part of our proof follows ideas given by Hodgson in [40]. He showed
in this paper how automata can be used to prove that some theories are decidable.
In particular, the theory Th(⟨N, +,Vp⟩) is decidable, as a corollary of the previous
theorem (see also [9]).

Corollary 6.2 Th(⟨N, +⟩) and Th(⟨N, +,Vp⟩) are decidable theories.

Proof. It is enough to give the proof for ⟨N, +,Vp⟩.Let ϕ be a sentence in ⟨N, +,Vp⟩.
We can assume that ϕ is the formula (∃x)ψ(x)or ¬(∃x)ψ(x) (by making some
manipulations of formulae if necessary). The proof above shows how to construct
a p-automaton for the p-recognizable set Mψ = { n ∈ N |⟨N, +,Vp⟩|= ψ(n) }.
By classical results of automata theory, the emptiness of the set Mψ is decidable. It
follows that it is decidable whether the sentence ϕ is true or not.

In Section 8.1, we will prove the interesting Proposition 7.6, as an easy conse-
quence of the previous corollary. We have also the following corollary [9].

Corollary 6.3 The characteristic sequence of the set of squares {n
2 | n ∈ N} is
not p-recognizable, for any p ⩾ 2.

Proof. We ﬁrst prove that the square fonction y = x2 is deﬁnable in ⟨N, +,RS⟩
where RS(y) is the relation “y is a square”. The function y = x2 is deﬁned by a
formula saying that “y is a square and the next square z after y has the property
that y +2x +1 = z”. This formula exists in ⟨N, +,RS⟩.
Ab absurdo, assume that the characteristic sequence of the squares is p-deﬁnable,
i.e., the relation RS(y)is p-deﬁnable by some formula ϕ(y). Thus, the function
y = x2 is also p-deﬁnable. Indeed, in the formula deﬁning y = x2 in ⟨N, +,RS⟩,
replace each occurrence of RS by the formula ϕ of ⟨N, +,Vp⟩. More generally, any
formula of ⟨N, +,x2⟩ is a formula of ⟨N, +,Vp⟩.
This means that ⟨N, +,x2⟩ is decidable, since ⟨N, +,Vp⟩ is. But ⟨N, +,x2⟩ and
⟨N, +, ·⟩ are equivalent structures and Th(⟨N, +, ·⟩) is undecidable (see Section 3).
This yields the contradiction.

We have seen in the proof of Theorem 6.1 that p-recognizability is preserved by
the Boolean operations and also by projection. Another interesting corollary of this
theorem is that some operations over integers preserve p-recognizability.
For instance, if M ⊆ N is p-recognizable, then c· M is still p-recognizable where
c is any constant. Indeed, if ϕ(x)is a formula of ⟨N, +,Vp⟩ deﬁning M, then the for-
mula (∃y)( (x = c· y) ∧ ϕ(y) ) deﬁnes the set c· M. Also addition, substraction, mul-
tiplication or division by a constant are operations which preserve p-recognizability.
The diagonal of any p-recognizable subset M of N2, deﬁned by {n ∈ N | (n, n) ∈
M},is also a p-recognizable subset of N.If ϕ(x, y)is a formula for M,then ϕ(x, x)
is a formula for its diagonal.

212 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

Generally, any operation deﬁnable in ⟨N, +,Vp⟩, preserves p-recognizability. The
proof of this property is straightforward and uniform in ⟨N, +,Vp⟩.There also exist
proofs using automata for the operations given previously as examples (see [58] or
[65]). However, each operation needs its own proof and it soon becomes diﬃcult to
ﬁnd a proof for more complex operations.

Corollary 6.4 Let f : Nm → Nn be an operation over integers. If f is deﬁnable
in ⟨N, +,Vp⟩ and if M ⊆ Nm is p-recognizable, then f(M) is p-recognizable.

Proof. The proof is very easy. M is deﬁned by a formula ϕ(y1,...,ym). The graph
of f : Nm → Nn is deﬁned by a formula φ(y1,...,ym,x1,... ,xn). Then f(M)is
deﬁned by the formula (∃y1) ... (∃ym)ϕ(y1,... ,ym) ∧ φ(y1,... ,ym,x1,... ,xn).

7 Base-Dependence

Four equivalent modes characterize p-recognizable sequences s : Nm → A : p-
substitutions, p-automata, p-deﬁnability, p-algebraicity (Theorems 4.1, 5.1). They
heavily depend on the base p. We are going to see that there are three kinds
of sequences s : the sequences recognizable in every base p ⩾ 2, the sequences
recognizable in certain bases p only and the sequences recognizable in no base p.

7.1 Base p
k

Let us come back to the characteristic sequence p of the powers of two (see Section
4.1). It is generated by the 2-substitution

f : {a, b, c}→ {a, b, c}2 : a → ab
b → bc
c → cc

g : {a, b, c}→ {0, 1} : a → 0
b → 1
c → 0

It is also generated by some 2
k-substitution, for all k ⩾ 1. To see this, simply replace
f by the iteration f k. For instance, for k =2, f 2 is the 4-substitution

f 2 : {a, b, c}→ {a, b, c}4 : a → abbc
b → bccc
c → cccc

This property is also veriﬁed on automata. The 4-recognizable sequence p is
computed by the following 4-automaton.

Figure 9. A 4-automaton computing p

Logic and p-recognizable sets of integers 213

This automaton is simply the 2-automaton of Figure 2 with the transitions modiﬁed
in the following way. The edges are the paths of length 2 of the 2-automaton, with
the labelling 0, 1, 2, 3 instead of 00, 01, 10, 11 respectively.
From the logical point of view, the argument is simple too. The function V2 is
deﬁnable in ⟨N, +,V4⟩. Indeed, if V4(x)= V4(2· x), then V2(x)is equal to V4(x),
otherwise V2(x)is equal to 2· V4(x). The formula ϕ of ⟨N, +,V4⟩ deﬁning V2(x)= y
is then the following

((V4(x)= V4(2· x)) ∧ (y = V4(x))) ∨ ((V4(x) ̸= V4(2· x)) ∧ (y =2· V4(x))) .

The sequence p is then 4-deﬁnable. Indeed, in the formulae of ⟨N, +,V2⟩ deﬁning
p
−1(0) and p
−1(1), replace each occurrence of V2 by ϕ. The two new formulae are
formulae of ⟨N, +,V4⟩ showing the 4-deﬁnability of p.
The property observed on the example p holds for any p-recognizable sequences :
they are also p
k-recognizable. More generally, they are q-recognizable as soon as p, q
are multiplicatively dependent integers, i.e., there exist k, l ⩾ 1 such that p
k = ql,
or equivalently p = rk,q = rl,for some r ⩾ 2and k, l ⩾ 1.

Proposition 7.1 Let p, q ⩾ 2 be multiplicatively dependent integers. Let m ⩾ 1
and s : Nm → A be a sequence. Then s is p-recognizable if and only if s is q-
recognizable.

Proof.
We prove that the structures ⟨N, +,Vp⟩ and ⟨N, +,Vpk⟩ are equivalent. Function
Vpk is deﬁnable in ⟨N, +,Vp⟩ :

Vpk (x)= y if and onlyif“yis the greatest powerof p
k less than or equal to Vp(x)”

The predicate Ppk(y) is deﬁnable in ⟨N, +,Vp⟩, observing that “y is a power of p
k

if and only if y is a power of p and p
k − 1 divides y − 1”. Indeed, assume that
y − 1= (p
k − 1)z for some z ̸= 0 and write y as p
ak+b,with 0 ⩽ b< k.Then

y − 1= p
b· (p
ak − 1) + (p
b − 1) .

As p
k − 1 divides y − 1and p
ak − 1, it also divides p
b − 1. Hence b = 0. The other
implication is trivial.
Conversely, Vp is deﬁnable in ⟨N, +,Vpk⟩ (this is similar to the case V2 and V4 we
have just explained) :

“If Vpk(x)= Vpk(p
k−1· x), then Vp(x)= Vpk (x),
else if Vpk(x)= Vpk(p
k−2· x), then Vp(x)= p· Vpk (x),
...
else if Vpk(x)= Vpk(p· x), then Vp(x)= p
k−2· Vpk (x),
else Vp(x)= p
k−1· Vpk (x)” .

Then we have shown that the structures ⟨N, +,Vp⟩, ⟨N, +,Vpk⟩ are equivalent
and that the structures ⟨N, +,Vql⟩, ⟨N, +,Vq⟩ are also equivalent. By hypothesis p
and q are multiplicatively dependent. Let k, l ⩾ 1 be such that p
k = ql. It follows
that ⟨N, +,Vp⟩ and ⟨N, +,Vq⟩ are equivalent.

214 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

7.2 Base 1 over N

A sequence s : N → A is said to be ultimately periodic if there exists v ⩾ 1such
that ∃n0, ∀n ⩾ n0,sn = sn+v .

The integer v is called a period of the ultimately periodic sequence. Ultimately
periodic sequences are a family of interesting sequences, as they are p-recognizable
for any p ⩾ 2.
For instance, the sequence u : N →{0, 1} equal to 00001001001001 ... is ulti-
mately periodic (with v =3,n0 =2). It is p-recognizable for any p ⩾ 2. Indeed,
un equals 1 if and only if 3 divides n − 4. The set u
−1(1) is then deﬁned by the
following formula ϕ(x)of ⟨N, +⟩

(∃y)(x =3y +4) .

The set u
−1(0) is deﬁned by ¬ϕ(x). As any formula of ⟨N, +⟩ is a formula of
⟨N, +,Vp⟩, the sequence u is p-deﬁnable for any p ⩾ 2.
This property can also be proved with formal power series or automata. The
formal power series
 U(x)= ∑ x3m+4 = x4

1 − x3

associated with u, is rational. It is a root of the polynomial (1−x3)t − x4 ∈ Fp[x][t].
Hence u is p-algebraic for all prime numbers p.
Let p ⩾ 2. Let us deﬁne v : N →{0, 1} by vn = un+4, for all n. A p-automaton
A for v has 3 states {q0,q1,q2} and transitions T (qi,b)= qj,for b ∈{0,... ,p − 1},
such that j = p· i + b mod 3 .

The initial state is q0. The output of q0 is 1 and the ouput of q1,q2 is 0. It is easy
to modify A into a p-automaton computing u.

Proposition 7.2 Let s : N → A be a sequence. If s is ultimately periodic, then s
is p-recognizable for all p ⩾ 2.

Proof. Roughly, s
−1(a),a ∈ A, is a ﬁnite union of arithmetic progressions. As in
the example, one shows that any arithmetic progression is deﬁnable in the structure
⟨N, +⟩ and therefore in ⟨N, +,Vp⟩.

The previous example suggests intrinsic properties of ultimately periodic se-
quences. The next theorem characterizes ultimately periodic sequences via “auto-
matic”, logical and algebraic arguments.

Theorem 7.3 Let s : N → A be a sequence. The following are equivalent :
(1) s is ultimately periodic,
(2) s is deﬁnable in ⟨N, +⟩,
(3) The series S(x)= ∑n⩾0 snxn is rational :

S(x)= p(x)
q(x) with p(x) ∈ Z[x],q(x) ∈ Z[x]\{0} ,

Logic and p-recognizable sets of integers 215

(4) s is 1-recognizable (by a 1-automaton),
(5) The sets s
−1(a), a ∈ A, are rational subsets of the monoid N.

Theexample of thesequence u can help to imagine a proof for Theorem 7.3.
It is proved in [59] (see also [28]) that any formula ϕ(x1,...,xm)of ⟨N, +⟩ can
be written as a ﬁnite combination of disjunctions, conjunctions and negations of the
formulae
 ti(x1,...,xm) ⩾ ci 1 ⩽ i ⩽ r,
ti(x1,...,xm)= ci mod dr < i ⩽ s,

where ci ∈ Z,d,m ∈ N are constants and ti(x1,...,xm)is equal to ∑ ui,jxj,with
ui,j ∈ Z. This explains why implication (2) ⇒ (1) holds.
The equivalence (1) ⇔ (3) is analoguous to the fact that a real number has
periodic expansion if and only if it is rational.
A 1-automaton looks like a “frying pan”, it is something quite special and has
little relationship to p-automata. The integer n is represented by the “1-ary ex-
pansion” 0
n, here 0 could be replaced by any other symbol (see references [24, 8]
for more details). It is easy to prove the equivalence (1) ⇔ (4). For the preceding
example u, a 1-automaton looks like

Figure 10. A frying pan automaton

Saying that a sequence s is ultimately periodic is the same as saying that the sets
s
−1(a), a ∈ A, are rational (or equivalently recognizable) subsets of the free monoid
(N, +) generated by 1. Indeed, rational subsets of N are exactly ﬁnite unions of
integers and linear progressions. For instance, the set u
−1(1) of the sequence u is
the rational subset 1
4.(1
3)∗ of N (where the product operation is here interpreted as
the addition in N).

7.3 Base 1 over N
m

First we must deﬁne a convenient generalization to Nm of ultimately periodic se-
quences. In order to keep an analog of Theorem 7.3 and Proposition 7.2 in all
dimensions, the logical characterization (2) in Theorem 7.3 is clearly a good candi-
date, since deﬁnability in ⟨N, +⟩ is a notion independent of the dimension.
S. Ginsburg and E. Spanier showed in [35] that M ⊆ Nm is deﬁnable in ⟨N, +⟩
if and only if it is semilinear, which means that M is deﬁned by a ﬁnite disjunction
of formulae ϕ(x) of the following form :

either (x = a)
or (∃y1) ... (∃yj)(x = a0 + a1y1 + ··· + ajyj)

216 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

where x is the m-tuple (x1,... ,xm), a, a0,..., aj ∈ Nm are constants and a· y is
intended as the product (a1y,... ,amy). Hence M is semilinear if and only if it is
a ﬁnite union of points (formula x = a)and of cones (formula (∃y1) ... (∃yj)(x =
a0 + a1y1 + ··· + ajyj)).
Semilinearity is equivalent to rationality over the monoid Nm. Indeed the two
previous formulae deﬁne the rational sets {a} and a0·{a1, ··· , aj}∗ of Nm.Conversely
one can show that any rational subset of Nm is semilinear by induction on the rational
operations.
Recently A. Muchnik gave an impressive characterization of semilinear sets in
terms of “local periodicity” [54]. It is the last characterization in the next theorem.
Muchnik mentioned it as the deﬁnability criterion. We give the proof of this criterion
in Section 8.1.

Theorem 7.4 Let m ⩾ 1 and s : Nm → A be a sequence. Let Ma = s
−1(a),for
each a ∈ A. The following are equivalent :
(1) s is deﬁnable in ⟨N, +⟩,
(2) each Ma is semilinear,
(3) each Ma is a rational subset of the monoid Nm,
(4) each Ma is locally periodic and every (m − 1)-dimensional sections of Ma is
deﬁnable in ⟨N, +⟩.

The last characterization needs some explanations. Let M ⊆ Nm.The section
Mi,c of M is obtained by ﬁxing the ith component to the constant c :

Mi,c = {n ∈ M | ni = c} .

Then Mi,c ⊆ Ni−1 ×{c}× Nm−i can be considered as a subset of Nm−1.
We say that M is locally periodic if there exists a ﬁnite set V of vectors v ∈ Nm

diﬀerent from 0 such that for some K> |V | and L ⩾ 0, one has :

(∀n ∈ Nm, |n| ⩾ L)(∃v ∈ V )(M is v-periodic inside N (n, K)) .

Let X ⊆ Nm,set M is v-periodic inside X if for any m, m + v ∈ X

m ∈ M ⇔ m + v ∈ M.

The vector v is called a period for M.In N2, this means that M is periodic in the
direction of v, when looking at M through the “window” X.
The set N (n, K)is the K-neighbourhood of n,it is the set

N (n, K)= {n + r | r ∈ Nm, |r| <K} ,

where the norm |r| of r is equal to max{r1,...,rm}. For instance, in N2, thisisa
square with size K and bottom-left corner n. Finally, notation |V | means ∑v∈V |v|.
Therefore M is locally periodic if there exists a ﬁnite number of periods v for M
such that for some large enough K, for any K-neighbourhood N (n, K) far enough
from the origin 0, M seen through N (n, K) is periodic with one of the periods v.
Let us now look at an example. The following sequence c : N2 →{0, 1} is the
characteristic sequence of a semilinear set. Figure 11 shows two points (0, 1), (2, 4)
and two cones one of which is degenerated into the diagonal.

Logic and p-recognizable sets of integers 217

↑ x2 ...

00 000 000 000 000 10 000
00 000 000 011 111 11 111
00 000 000 000 010 00 000
00 000 000 111 111 11 111
00 000 000 001 000 00 000
00 000 001 111 111 11 111
00 000 000 100 000 00 000
00 000 011 111 111 11 111
00 000 010 000 000 00 000 ...
00 000 111 111 111 11 111
00 101 000 000 000 00 000
00 011 111 111 111 11 111
00 100 000 000 000 00 000
11 000 000 000 000 00 000 x1
10 000 000 000 000 00 000 −→

Figure 11. The characteristic sequence of a semilinear set

The set c−1(1) is deﬁned by the formula ϕ(x1,x2)of ⟨N, +⟩

(x1,x2)= (0, 1)
∨ (x1,x2)= (2, 4)
∨ (∃y)( (x1,x2)=(1, 1)y )
∨ (∃y1)(∃y2)( (x1,x2)=(4, 3) + (1, 2)y1 +(1, 0)y2 ) .

It is easy to ﬁnd, from this formula, a rational expression for c−1(1) :

c−1(1) = (0, 1) ∪ (2, 4) ∪ (1, 1)∗ ∪ (4, 3)·{(1, 2), (1, 0)}∗ .

Furthermore, c−1(1) is locally periodic with V = {(2, 2), (1, 2), (1, 0)} (see Figure
11). Indeed, far enough from the origin, a K-neighbourhood is either completely
inside the cone deﬁned by (∃y1)(∃y2)( (x1,x2)= (4, 3) + (1, 2)y1 +(1, 0)y2 ), either
completely outside this cone, or it overlaps one of its borders. In the last case, we
choose period (1,2) for the border deﬁned by (1,2) and period (1,0) for the other
border. When the K-neighbourhood is inside the cone, it can meet the diagonal
deﬁned by (∃y)( (x1,x2)=(1, 1)y ) or not. For both situations, period (2,2) is
convenient. Finally, outside the cone, any period works.
As any formula of ⟨N, +⟩ is trivially a formula of ⟨N, +,Vp⟩, for any p ⩾ 2, we
have the analog of Proposition 7.2.

Proposition 7.5 Any sequence s : Nm → A deﬁnable in ⟨N, +⟩ is p-recognizable,
for all p ⩾ 2.

218 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

Of course, there exist p-recognizable sequences which are not deﬁnable in ⟨N, +⟩.
The characteristic sequence p of the powers of 2 (Section 4.1) and the sequence
t describing Pascal triangle modulo 2 (Section 5.1) are such examples. Muchnik’s
deﬁnability criterion allows to decide whether a p-recognizable sequence s : Nm → A
is deﬁnable in ⟨N, +⟩ [54]. This result was already proved for the one-dimensional
case [39, 42, 55]. The proof in the general case is easy [54], using the decidability of
Th(⟨N, +,Vp⟩) (Corollary 6.2); it is given in Section 8.1.

Proposition 7.6 Let m ⩾ 1 and p ⩾ 2.Let s : Nm → A be a p-recognizable
sequence. It is decidable whether s is deﬁnable in ⟨N, +⟩.

To conclude this section, let us remark that in Nm, m ⩾ 2, Kleene’s theorem is
no longer true : the family of recognizable subsets is strictly included in the family
of rational subsets (the diagonal is rational but not recognizable). Recognizable sets
may be understood as a certain “tiling” of Nm by a ﬁnite number of parallelepipeds.
Theorem 7.4 shows that this concept does not give a suﬃcient generalization of
ultimately periodic sequences in Nm.
This is emphasized by the theorem of Cobham-Semenov in the next section.

7.4 Theorem of Cobham-Semenov

Any ultimately periodic sequence s : N → A, and more generally any sequence
s : Nm → A deﬁnable in ⟨N, +⟩,is p-recognizable for any p ⩾ 2 (Propositions 7.2,
7.5). In 1969, A. Cobham proved the converse in the case of N [15]. Later in 1977,
A. Semenov generalized this result to Nm [66]. As a matter of fact, Cobham and
Semenov proved a stronger property : as soon as a sequence s : Nm → A is p-
and q-recognizable, for some multiplicatively independent integers p, q ⩾ 2, then s
is deﬁnable in ⟨N, +⟩. We recall that p, q ⩾ 2are multiplicatively independent if
and only if the equation p
k = ql has the solution k = l = 0 only. Using the logical
characterizations (see Theorems 5.1 and 7.4), this is reformulated in the following
way : let p, q ⩾ 2 be multiplicatively independent integers, then s is both p-and
q-deﬁnable if and only if s is deﬁnable in ⟨N, +⟩. This result says that if s can be
deﬁned by using +,Vp or +,Vq, then it can be deﬁned by using + only. This is
clearly not obvious.
The theorem of Cobham-Semenov theorem is one of the most beautiful results in
the theory of recognizability of natural numbers. We give in Section 8.2 an elegant
proof of this result, following the reference [54].

Theorem 7.7 (Cobham-Semenov) Let m ⩾ 1,let p, q ⩾ 2 be multiplicatively
independent integers. Let s : Nm → A be a sequence. If s is p-recognizable and
q-recognizable, then s is deﬁnable in ⟨N, +⟩.

The characteristic sequence of powers of 2 is certainly not ultimately periodic. It
is 2-recognizable and also 2
k-recognizable, for all k ⩾ 1. As 3 and 2 are multiplica-
tively independent, this sequence is not 3-recognizable and thus not 3
k-recognizable,
k ⩾ 1. More generally, it is not p-recognizable, for each p ⩾ 2 which is not a power
of 2.

Logic and p-recognizable sets of integers 219

The relation “being multiplicatively dependent” is an equivalence relation on
N\{0, 1}. In each equivalence class, there exists a smallest integer p which we call
simple. Any other element of this class is a power p
k of p, k ⩾ 1. An integer
p is simple if and only if gcd(k1,...,kl)=1 where p = p
k1
1 ...p
kl
l is the prime
factorization of p. The ﬁrst simple integers are 2, 3, 5, 6, 7, 10, 11,... .
Assume the sequence s : Nm → A is p-recognizable, but not deﬁnable in ⟨N, +⟩.
We can suppose that p is simple. The theorem of Cobham-Semenov states that the
only bases q for which s is q-recognizable are q = p
k,k ⩾ 1.
To summarize, sequences s are classiﬁed into 3 distinct groups :

1. The sequences p-recognizable in every base p ⩾ 2

These sequences are exactly the sequences deﬁnable in ⟨N, +⟩.They are also
p-deﬁnable for each p ⩾ 2.

2. The sequences p-recognizable for certain bases p only

These sequences are not deﬁnable in ⟨N, +⟩.They are only p
k-recognizable for
k ⩾ 1(p being simple).

3. The sequences not p-recognizable for any p ⩾ 2

The characteristic sequence of squares belongs to this family (see Section 4.2
and Corollary 6.3).

7.5 Bibliographic Notes

The ﬁrst step towards the theorem of Cobham-Semenov is in B¨uchi’s paper [9].
He proved that Pp is deﬁnable in ⟨N, +,Pq⟩ if and only if p, q are multiplicatively
dependent. In this paper, he also showed that ultimately periodic sequences are
p-recognizable for all p ⩾ 2. He also proved that the p
k-recognizable sequences are
exactly the p-recognizable sequences.
In 1969, A. Cobham proved Theorem 7.7 in the case of subsets M of N.In a
footnote, he mentioned with no reference, the weaker theorem established indepen-
dently by J. Nievergelt, that “a set which is recognizable in n-ary notation for all
n ⩾ 2 is necessarily ultimately periodic”. The property proved by B¨uchi, that Pp
is deﬁnable in ⟨N, +,Pq⟩ if and only if p, q are multiplicatively dependent, helped
Cobham to formulate his theorem in the more general situation of sets M ⊆ N both
p-and q-recognizable, with p, q multiplicatively independent integers.
Cobham’s proof is diﬃcult. It is based on a deep analysis of p-and q-automata
computing the characteristic sequence m of M. The proof is divided into two parts.
The ﬁrst part states that if M ⊆ N is p-and q-recognizable, with p, q being
multiplicatively independent, then m is syndetic, that is there exists v ⩾ 1such
that ∃n0, ∀n ⩾ n0, ∃v′, 0 <v′ ⩽ v, mn = mn+v′ .

In other words, the distance between two consecutive occurrences of a given letter
in the sequence is bounded by v. The property of syndeticity is weaker than the
property of ultimate periodicity. Indeed the Thue-Morse sequence is syndetic but
not ultimately periodic (see Section 4.5).

220 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

The second part of the proof is more technical. Cobham proves that the sequence
m is ultimately periodic, by extracting the period of the sequence from the automata.

In his book [24], S. Eilenberg devotes Chapter 5 to the study of integers and the
diﬀerent notions of recognizability. He mentioned Cobham’s theorem without proof
but with the comment “It is a challenge to ﬁnd a more reasonable proof of this ﬁne
theorem” (p. 118).

In 1977, A. Semenov generalized Cobham’s theorem to subsets M of Nm, m ⩾ 1
[66]. His proof is by induction on m. The ﬁrst step, m = 1, isCobham’sproof.
Twenty-eight lemmas lead to the theorem. So, Cobham’s proof together with Se-
menov’s proof establish Theorem 7.7.

Stimulated by Eilenberg’s challenge, several researchers have attempted to ﬁnd
a simpler proof of Theorem 7.7 in the case m = 1. In 1982, G. Hansel succeeded in
proving Cobham’s theorem in a more reasonable way [36] (see also [62, 58]). The
proof is combinatorial. The ﬁrst part is the same than in [15] where the characteristic
sequence m of M ⊆ N is proved to be syndetic. The second part is simpler and
more comprehensible. To prove that m is ultimately periodic, instead of directly
constructing a period for the sequence as done by Cobham, Hansel used the following
characterization [52, 53] : a sequence s is ultimately periodic if and only if there
exists l ⩾ 1 such that the number of recurrent factors of length l of the sequence,
is bounded by l (a factor is a word snsn+1 ··· sm of consecutive letters of s;and a
factor is recurrent if it occurs inﬁnitely often inside s).

Very recently, C. Michaux and R. Villemaire gave another simpler proof [49].
Their proof has also two parts. The ﬁrst part is the syndeticity of the sequence as
in [15]. The second one is a proof ab absurdo. It uses all the expressive power of
the structure ⟨N, +,Vp⟩, as pointed out by Corollary 6.4. The combinatorial part of
the proof is very reduced.

Up to now, there does not exist a counterpart to the notion of syndeticity for
multi-dimensional sequences. In 1991, A. Muchnik gave a comprehensible proof
of the theorem of Cobham-Semenov, for any m ⩾ 1. The proof is based on his
powerful deﬁnability criterion [54] and has plenty of new ideas. It is much simpler
than Semenov’s proof and also gives a new proof of Cobham’s theorem. The most
impressive thing about Muchnik’s proof is that he attacks the problem in a direct
fashion but still succeeds in solving it. Actually he takes a natural number n ∈ M,
transforms it from base p to base q and conversely, using the relations ∼p,M and
∼q,M , in order to obtain a n
′ ∈ M which is close to n. He shows in this way that
M is ultimately periodic. Many researchers have tried to attack the question in this
way, but there are many diﬃculties that only Muchnik succeeded to overcome.

The main result of [49] is extended to the multi-dimensional case in [50], using
Muchnik’s deﬁnability criterion. They show that if M ⊆ Nm is not deﬁnable in
⟨N, +⟩, then there exists a non-syndetic 1-dimensional set L which is ﬁrst-order
deﬁnable in the structure ⟨N, +,RM ⟩ (RM is the relation of membership to M).
This yields a new proof of the theorem of Cobham-Semenov.

Logic and p-recognizable sets of integers 221

8 Muchnik’s proof

We give in this section an account as precise as possible of the work of Muchnik.
This is in order to make his result available to people who do not read Russian.

8.1 Deﬁnability Criterion

We here prove in details the deﬁnability criterion stated by Muchnik in [54]. We
recall its statement for sets M ⊆ Nm :

Theorem 8.1 Let M ⊆ Nm.Then M is deﬁnable in ⟨N, +⟩ if and only if M is
locally periodic and if any of the sections of M is deﬁnable in ⟨N, +⟩.

Proof. The proof of the ﬁrst implication is not given here, but in the Appendix.
This implication is not necessary to the proof of the theorem of Cobham-Semenov.
Only the other one is used.
For the converse, assume that all the sections of M are deﬁnable in ⟨N, +⟩ and
there exists a ﬁnite set V of periods v ∈ Nm\{0} such that for some K> |V | and
L ⩾ 0, we have

∀n ∈ Nm, |n| ⩾ L, ∃v ∈ V, M is v-periodic inside N (n, K) .

We prove by induction on Card V that M is deﬁnable in ⟨N, +⟩.

(1) First we suppose that V = {v}. Therefore, any neighbourhood has the
same period v. This means that M is v-periodic as soon as we are far enough from
the origin.
The set M is easily deﬁnable using its sections. Indeed, let v =(v1,...,vm), we
denote for any i,1 ⩽ i ⩽ m,

Mi = Mi,L ∪ Mi,L+1 ∪ ··· ∪ Mi,L+vi−1 .

Mi is the union of the vi consecutive sections of M where the ith component has
been ﬁxed to L, L+1,... ,L+vi−1 respectively. We also denote for any i, 1 ⩽ i ⩽ m,
the sets Ni = Mi,0 ∪ Mi,1 ∪ ··· ∪ Mi,L−1 .

The sets Mi,Ni and ⋃i Mi, ⋃i Ni are deﬁnable in ⟨N, +⟩ as all the sections of M are
deﬁnable by assumption.
We have M = ⋃

i Ni ∪ ⋃

i Mi· v∗

where ∪, · ,∗ are the rational operations in the monoid Nm.The set M is deﬁnable
in ⟨N, +⟩ because the set ⋃i Mi· v∗ is deﬁnable by the following formula ϕ(x) (recall
that v is a constant)
 (∃y ∈ ⋃

i Mi)(∃j ⩾ 0) (x = y + j.v) .

(2) Suppose now that Card V ⩾ 2. Let v ∈ V .

222 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

We show that M is deﬁnable in ⟨N, +⟩ via the sets B(M, v)and B(M, −v). These
sets will be deﬁnable in ⟨N, +⟩ by the induction hypothesis.
The set B(M, v) is the “border of M in the direction v” and is deﬁned as

B(M, v)= {n ∈ M | n + v/∈ M} .

In the same way, B(M, −v)= {n ∈ M | n − v/∈ M} .

The set B(M, −v) is never empty since M ⊆ Nm.
The set M is deﬁnable in ⟨N, +⟩ using the borders B(M, v), B(M, −v). Indeed,
given n ∈ M, consider the “line”

L = {n + j· v | j ∈ Z} .

This line always intersects B(M, −v). We have to consider two cases : this line
intersects B(M, v) or it does not. The second case is described by the following
formula ϕ(x)

(∃y ∈B(M, −v)) ((∃j1 ⩾ 0)(x = y + j1.v)) ∧ ((∀j2 ⩾ 0)(y + j2.v/∈B(M, v))) .

In the ﬁrst case, n is placed between a point of B(M, −v) and the point of B(M, v)
met just after, in the direction of v. The corresponding formula φ(x)is

(∃y1 ∈B(M, −v))(∃y2 ∈B(M, v))(∃j1,j2 ⩾ 0)
(x = y1 + j1.v) ∧ (y2 = x + j2.v)
∧(∀j)[ (0 <j <j1 + j2) → (y1 + j.v/∈B(M, −v) ∧ y1 + j.v/∈B(M, v)) ] .

Hence M is deﬁned by the formula ϕ(x) ∨ φ(x).
It remains to show that B(M, v)and B(M, −v) satisfy the induction hypothesis.
Their sections are deﬁnable in ⟨N, +⟩ because they can be deﬁned from the sections
of M. For instance, n belongs to section B(M, v)i,c where the ith component is ﬁxed
to c if and only if n ∈ Mi,c and n + v/∈ Mi,c+vi .
We now prove that B(M, v)is V \{v}-periodic. Let

K ′ = K −|v| > |V \{v}| and L
′ = L.

Let n ∈ Nm, |n| ⩾ L
′. By hypothesis, M is w-periodic in N (n, K), for some w ∈ V .
Consider N (n, K ′). If v ̸= w,take m and m + w in N (n, K ′). Then

m, m + w and m + v, m + w + v

all belong to N (n, K) inside which M is w-periodic. It follows that B(M, v)is w-
periodic inside N (n, K ′). If v = w,then B(M, v)is empty inside N (n, K ′)and then
w-periodic in N (n, K ′) for any w ∈ V \{v}.
In the same way, one proves that B(M, −v)is V \{v}-periodic with K ′ = K −|v|
and L
′ = L + |v|.

Logic and p-recognizable sets of integers 223

We now give the proof of Proposition 7.6 mentioned in Section 7.3, stating that
it is decidable whether a p-deﬁnable sequence is deﬁnable in ⟨N, +⟩.

Proposition 8.2 Let m ⩾ 1 and p ⩾ 2.Let s : Nm → A be a p-recognizable
sequence. Then it is decidable whether s is deﬁnable in ⟨N, +⟩.

Proof. By Proposition 5.2, it is suﬃcient to give the proof for p-recognizable sets
M ⊆ Nm.
We ﬁrst consider the one-dimensional case m =1. Let ϕM (x)be a formula of
⟨N, +,Vp⟩ deﬁning M. The characteristic sequence m of M is ultimately periodic if
and only if (∃t)(∃z)(∀x)[ (x ⩾ z ∧ ϕM (x)) → ϕM (x + t)] .

This is a sentence of ⟨N, +,Vp⟩.As Th(⟨N, +,Vp⟩) is a decidable theory, it is decid-
able whether this sentence is true, i.e., whether m is ultimately periodic.
We now treat the two-dimensional case. Let M ⊆ N2 be a p-recognizable set and
ϕM (x, y) a formula deﬁning M in ⟨N, +,Vp⟩. The proof is the same : again we want
to ﬁnd a formula in ⟨N, +,Vp⟩ which expresses that M is deﬁnable in ⟨N, +⟩.By the
deﬁnability criterion, M is deﬁnable in ⟨N, +⟩ if and only if M is locally periodic
and all its sections are deﬁnable in ⟨N, +⟩.
Consider the second condition. Sections of M have dimension 1. So they are de-
ﬁnable in ⟨N, +⟩ if and only if their characteristic sequences are ultimately periodic.
As we did before, the following formula of ⟨N, +,Vp⟩

(∀y)(∃t)(∃z)(∀x)[ (x ⩾ z ∧ ϕM (x, y)) → ϕM (x + t, y)]

states that all sections of M, when ﬁxing the second component y, are deﬁnable
in ⟨N, +⟩. The same kind of formula exists for sections of M, when ﬁxing the ﬁrst
component.
The local periodicity of M is also deﬁnable in ⟨N, +,Vp⟩. In the deﬁnition of local
periodicity, the ﬁnite set V of periods and the integer K> |V | cannot be directly
expressed in ⟨N, +,Vp⟩. However, we ﬁrst notice that the condition ∃K> |V | can
be replaced by the stronger condition ∀K (by checking the proof of the deﬁnability
criterion). Secondly, the set V can be replaced by the ﬁnite set of v ∈ Nm such that
|v| ⩽ d for some constant d. Hence M is locally periodic if and only if

(∃d)(∀K)(∃L)(∀n ∈ Nm, |n| ⩾ L)(∃v, |v| ⩽ d) M is v-periodic in N (n, K).

This new condition is deﬁnable in ⟨N, +,Vk⟩ : the norm || and the relation ∈
N (n, K) are both deﬁnable, the v-periodicity is also deﬁnable as follows

(∀x)[ ( x ∈N (n, K) ∧ x + v ∈N (n, K)) → ( ϕM (x) ↔ ϕM (x + v)) ] .

So it is possible to say with a sentence of ⟨N, +,Vp⟩ that M is deﬁnable in ⟨N, +⟩.
We can decide if this sentence is true, since Th⟨N, +,Vp⟩ is decidable.
The previous cases m =1 and m = 2 show how the general case works. The
proof is by induction on m. The basis of the induction is proved above. Let m ⩾ 2
be a ﬁxed integer. Let M be a p-recognizable subset of Nm deﬁned by some formula
ϕM (x)of ⟨N, +,Vp⟩. We express as before the local periodicity property. A formula
stating that the sections of M are deﬁnable exists by induction hypothesis, as the

224 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

sections have dimension m − 1. Therefore, there exists a sentence of ⟨N, +,Vp⟩ which
says that M satisﬁes the deﬁnability criterion. This sentence is certainly complex
but we can decide if it is true or false.

8.2 Proof of the Theorem of Cobham-Semenov

In this section, we give Muchnik’s proof for the theorem of Cobham-Semenov (The-
orem 7.7). The proof is not exactly the same as in [54]; some parts are modiﬁed or
shortened and other ones are given in more detail. It uses the deﬁnability criterion
stated in Theorem 8.1.

Theorem 8.3 Let m ⩾ 1,let p, q ⩾ 2 be multiplicatively independent integers.
If M ⊆ Nm is p-and q-recognizable, then its characteristic sequence is deﬁnable in
⟨N, +⟩.

We ﬁrst recall properties of the relation ∼p,M associated with any set M ⊆ Nm

(see Section 4.3 or [24]). Let n, m ∈ Nm,then

n ∼p,M m ⇔ [ np
k + r ∈ M ⇔ mp
k + r ∈ M ∀k ⩾ 0, ∀r ∈ Nm, |r| <p
k ] .

Set M is p-recognizable if and only if ∼p,M has ﬁnite index, M is a union of some
equivalence classes of ∼p,M. The relation ∼p,M is p-stable, i.e.,

n ∼p,M m ⇒ np
k + r ∼p,M mp
k + r

for |r| <p
k.
The following lemmas will be useful.

Lemma 8.4 Let m ⩾ 1 and p, q ⩾ 2.If M ⊆ Nm is p-and q-recognizable, then
any equivalence class C of ∼p,M is also p-and q-recognizable.

Proof. To simplify the notations, we limit the proof to the case m =1.
From the properties above, C is clearly p-recognizable. Consider the minimal
automaton A(L)= (Q, {q0},F,T )of the set

L = { w ∈{0,...,p − 1}∗ | [w]p ∈ M } .

The relation ∼p,M is the translation to N of the right-congruence ∼L deﬁned on
{0,...,p−1}∗.The class C of ∼p,M corresponds to a class CL of ∼L. By construction
of A(L), CL is some of its states, that we denote by r. Moreover, for any state r′ ̸= r,
there exists a word u, depending on r′, such that T (r, u) is ﬁnal and T (r′,u)is not,
or the opposite (see Section 2). We then deﬁne the subset of {0,...,p − 1}∗

L(r′)= {w | wu ∈ L} if T (r, u) is ﬁnal ,
= {w | wu /∈ L} otherwise .

One veriﬁes that CL = ⋂

r′̸=r L(r′) .

Logic and p-recognizable sets of integers 225

Coming back to N,this gives
 C = ⋂

r′̸=r M(r′) .

where M(r′)= {[w]p | w ∈ L(r′)}.Each set M(r′)is q-recognizable using Corollary
6.4. Indeed M is q-deﬁnable and wu ∈ L if and only if [w]p· p
|u| +[u]p ∈ M (p
|u| is
a constant). So C is itself q-recognizable.

Lemma 8.5 Let p, q ⩾ 2 be multiplicatively independent integers. Then for any
real numbers r1,r2 with 0 ⩽ r1 <r2, there exist arbitrarily large integers k, l such
r1 <ql/p
k <r2.

The proof of this lemma can be found in [58] for example. It is based on Kro-
necker’s theorem which states that if θ is an irrational number, then the fractional
parts of its multiples nθ, n ⩾ 0, are dense in the interval [0, 1] (see [38]).
We are now going to prove Theorem 8.3.

Proof.
The idea of the proof is the following.
We have to prove that M is locally periodic and all the sections of M are deﬁnable in
⟨N, +⟩. The proof will use induction on m; this is necessary to prove the deﬁnability
of the sections. However, the property of local periodicity will be proved directly,
independently of the induction.
We ﬁrst show that M is locally periodic but for the p
k-neighbourhoods N (np
k,p
k)of
np
k only, (for some well-chosen power p
k). This will be possible using an elaborate
equivalence relation ∼p,q,M deﬁned from the relations ∼p,M and ∼q,M .
In a way to reach all the neighbourhoods, we repeat the previous argument to the
following subset M ′ of N2m, instead of M :

M ′ = { (n1, n2) | n1 + n2 ∈ M } .

A well-chosen projection on Nm of the neighbourhoods N ((n1, n2)p
k,p
k)in N2m will
yield all the neighbourhoods of Nm.
We now go into the details of the proof.

(A) By Lemma 8.4, any equivalence class C of ∼p,M is p-and q-recognizable.
In particular, any ∼q,C has ﬁnite index. We deﬁne a new equivalence relation ∼p,q,M
over Nm, from the relations ∼p,M and ∼q,C :

n ∼p,q,M m ⇔ [ n ∼q,C m, for all classes C ] .

In other words, ∼p,q,M is the ﬁnite intersection (over the classes C of ∼p,M )ofthe
relations ∼q,C. The new relation has interesting properties : ∼p,q,M has ﬁnite index
and

1. n ∼p,q,M m ⇒ n ∼p,M m.

2. n ∼p,q,M m ⇒ n ∼q,M m.

226 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

The ﬁrst property is proved as follows. Let C be the equivalent class of ∼p,M
containing n.Then

n ∼p,q,M m ⇒ n ∼q,C m ⇒ m ∈ C.

And if n, m ∈ C,then n ∼p,M m. For the second property, the proof is the following
one. If n ∼p,q,M m,then n ∼q,C m for all classes C of ∼p,M ,and also nql + r ∼q,C
mql + r.Thus

nql + r ∈ M ⇒ nql + r ∈ C for some C ⊆ M ⇒ mql + r ∈ C ⊆ M.

The conclusion follows.

(B) We here prove that M is locally periodic but for some neighbourhoods
only. These neighbourhoods have the particular form N (np
k,p
k).
(a) For any inﬁnite class D of ∼p,q,M we choose a pair (xD, yD)of elements of
D, simply denoted (x, y), such that

1. for all α ∈ Z
m with |α| ⩽ 1, if x + α, y + α ∈ Nm,then x + α ∼p,q,M y + α,

2. there exists n ∈ Nm\{0} such that x + n = y, i.e., x< y.

This pair (x, y) always exists because ∼p,q,M has ﬁnite index and any set of Nm of
mutually incomparable elements is ﬁnite [25]. More precisely, given z ∈ D, for any
α ∈ Z
m such that |α| ⩽ 1and z + α ∈ Nm,let Dα be the class of ∼p,q,M containing
z + α. Now list these α’s and the related classes Dα.As D is inﬁnite, there are
inﬁnitely many z ∈ D with the same list of classes Dα.We choose x and y among
them.
Then using Lemma 8.5, we choose k and l such that 1 <ql/p
k < 1+ϵ,or equivalently

0 <ql − p
k <ϵp
k (1)

where ϵ satisﬁes the following condition : for any chosen y =(y1,... ,ym), for all
1 ⩽ i ⩽ m, (1 + yi)ϵ< 1 . (2)

In particular, as x< y,we have xiϵ< 1 . (3)

(b) We ﬁrst prove that (y − x)(ql − p
k)is a period for M inside the particular
neighbourhood N (xp
k,p
k): precisely forall m ∈N (xp
k,p
k),

m ∈ M ⇔ m +(y − x)(ql − p
k) ∈ M.

Let m = xp
k + r ∈N (xp
k,p
k). We deﬁne x
′ =(x′
1,...,x′
m)and r′ =(r′
1,... ,r′
m)
in Nm such that for any 1 ⩽ i ⩽ m, x′
i and r′
i are respectively the quotient and the
remainder of the division of xip
k + ri by ql.Then

x′ql + r′ = xp
k + r |r′| <ql . (4)

We have x
′ = x + α with |α| ⩽ 1and α ⩽ 0 .

Logic and p-recognizable sets of integers 227

Indeed as ql >p
k,then x′
i ⩽ xi for any 1 ⩽ i ⩽ m, by (1) and (4). On the other
hand, xi − 1 ⩽ x′
i otherwise x′
i ⩽ xi − 2 and by (1), (3),

x′
iql + r′
i < (xi − 2)ql + ql ⩽ xip
k + xi(ql − p
k) − ql <xip
k ,

which is impossible by (4). Therefore by (4)

(x + α)ql + r′ = xp
k + r. (5)

We have x + α, y + α ∈ Nm and as x + α ∼p,q,M y + α,

xp
k + r ∈ M ⇔ (y + α)ql + r′ ∈ M (6)

using (5) and property 2 of ∼p,q,M.
Now let y′ =(y′
1,... ,y′
m)and s =(s1,...,sm)in Nm be such that for any 1 ⩽
i ⩽ m, y′
i and si are respectively the quotient and the remainder of the division of
(yi + αi)ql + r′
i by p
k,that is

y′p
k + s =(y + α)ql + r′ |s| <p
k . (7)

We have y′ = y + β with |β| ⩽ 1and α ⩽ β.

Indeed as p
k <ql,then yi + αi ⩽ y′
i for all 1 ⩽ i ⩽ m, by (1) and (7). We have also
y′
i ⩽ yi +1 otherwise yi +2 ⩽ y′
i and by (1), (2) (remember α ⩽ 0),

y′
ip
k + si ⩾ (yi +2)p
k ⩾ (yi + αi)ql + yi(p
k − ql)+2p
k > (yi + αi)ql + ql ,

whichisincontradictionwith(7). Hence by (7)

(y + β)p
k + s =(y + α)ql + r′ . (8)

As y + β, x + β ⩾ x + α ∈ Nm and as y + β ∼p,q,M x + β, it follows from property 1
of ∼p,q,M that
 (y + α)ql + r′ ∈ M ⇔ (x + β)p
k + s ∈ M.

Together with (6), this yields

xp
k + r ∈ M ⇔ (x + β)p
k + s ∈ M ⇔ xp
k + r +(y − x)(ql − p
k) ∈ M.

Indeed using (8) and (5)

βp
k + s − r = βp
k +(y + α)ql − (y + β)p
k + r′ − r
=(y + α)ql − yp
k + xp
k − (x + α)ql

=(y − x)(ql − p
k) .

(c) For any inﬁnite class D of ∼p,q,M,we denote by vD the period (y−x)(ql−p
k).
The relation ∼p,q,M has ﬁnite index, then there exists U ⩾ 0 such that, as soon as
|n| ⩾ U,the class D of ∼p,q,M containing n is inﬁnite. Let us now show that M is vD-
periodic inside the p
k-neighbourhood N (np
k,p
k)of n.Let m, m + vD ∈N (np
k,p
k).

228 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

More precisely m = np
k + r with |r| <p
k and |r + vD| <p
k. Using (b), we have the
following equivalences
 m ∈ M ⇔ np
k + r ∈ M
⇔ xDp
k + r ∈ M
⇔ xDp
k + r + vD ∈ M
⇔ np
k + r + vD ∈ M
⇔ m + vD ∈ M.

Figure 12. The local periodicity of M inside the neighbourhoods N (npk,pk)

(C) To prove the local periodicity of M inside all the neighbourhoods, we
transfer the results of (B) to the subset of N2m

M ′ = {(n1, n2) | n1 + n2 ∈ M}

which is p-and q-recognizable by Corollary 6.4. We add the condition on ϵ that

ϵ< 1
6 ∑ |yD| . (9)

We denote by V ′ the ﬁnite set of periods vD =(y − x)(ql − p
k). We are going to
show that M is locally periodic with the set of periods

V = {v = v1 + v2 | (v1, v2) ∈ V ′}

and parameters K = ⌈p
k/3⌉ and L = Up
k (the constant U was deﬁned in (c)). We
ﬁrst verify that |V | <K with (1) and (9).

|V | = ∑

(v1,v2)∈V ′ |v1 + v2| ⩽ 2 ∑

vD∈V ′ |vD| ⩽ 2(ql − p
k) ∑ |yD − xD| <p
k/3 .

Logic and p-recognizable sets of integers 229

Let u ∈ Nm, |u| ⩾ L. We write u as u = np
k + r, |r| <p
k. We decompose r in Nm

such that r = r1 + r2 with |r1| < 2p
k/3and |r2| ⩽ p
k/3 (seeFigure13).

Figure 13. Projection from N2m to Nm

Then
 u = u1 + u2

with u1 = np
k + r1, u2 = r2. This corresponds in N2m to the point

(u1, u2)=(n, 0)p
k +(r1, r2) .

As |(n, 0)| ⩾ U, there exists a period vD =(v1, v2)in V ′ for which M ′ is vD-
periodic inside N ((n, 0)p
k,p
k). We will prove that this implies, in Nm,that M is
(v = v1 + v2)-periodic inside N (u, K). Let u + t and u + t + v in N (u, K). As
|vD| <p
k/3 by (1) and (9), the points

(u1, u2 + t)= (n, 0)p
k +(r1, r2 + t)
(u1, u2 + t)+(v1, v2)= (n, 0)p
k +(r1 + v1, r2 + t + v2)

both belong to N ((n, 0)p
k,p
k). Consequently

u + t ∈ M ⇔ (u1, u2 + t) ∈ M ′ ⇔ (u1, u2 + t)+(v1, v2) ∈ M ′ ⇔ u + t + v ∈ M.

Hence (B) and (C) show that M is locally periodic.

(D) We now ﬁnish the proof. If m =1, then M is locally periodic and any of
its sections is a constant which is trivially deﬁnable in ⟨N, +⟩.Let m> 1. Again M
is locally periodic. Its sections are deﬁnable in ⟨N, +⟩ by the induction hypothesis.
Indeed, any section has dimension m − 1 and it is p-and q-recognizable by Corollary
6.4.

230 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

9 Related Work

There exist diﬀerent possible generalizations of the notion of p-recognizable sequence
(see the survey [1]). One generalization is replacing p-substitutions f : B → Bp by
nonuniform substitutions (the images of the letters of B have diﬀerent lengths). One
well-known example is the Fibonacci substitution deﬁned on B = {0, 1} by f(0) =
01,f(1) = 0. This is related to nonstandard representations of numbers generalizing
p-ary expansions. For instance, any positive integer can be written as ∑ anfn where
fn is the n-th Fibonacci number and an is 0 or 1. Nonstandard representations of
numbers are studied in [56, 30, 6]. For connections between nonuniform substitutions
and nonstandard representations of integers, see [61, 70, 29]. See also [17, 47, 41] for
decision problems related to generalized number systems. Another generalization
of p-recognizable sequence is the notion of p-regular sequence introduced in [2]. A
sequence s has its values sn in a noetherian (possibly inﬁnite) ring R instead of a
ﬁnite alphabet A.It is p-regular if and only if the R-module generated by its p-
kernel {(snpk+r)n⩾0 | k ⩾ 0,r < p
k}, is ﬁnitely generated. The reference [2] contains
the following conjecture : if a sequence s is p-and q-regular, and p and q are
multiplicatively independent, then the formal power series ∑n⩾0 snxn is rational.
In Section 7, we classiﬁed the sequences into three groups, the last one containing
sequences recognizable in no base. The ﬁrst proofs of unrecognizability of the set
of squares (in any base) are logical ones [9, 26]. Later, Ritchie gives a more direct
combinatorial proof [63]. The references [51, 16, 24] introduce methods based on the
asymptotic behavior of functions dealing with the gaps between successive elements
of M ⊆ N.These gap theorems easily show that the set of squares or of prime
numbers are never p-recognizable, for any p ⩾ 2. For properties of star-height 0 of
p-recognizable sequences for suitable bases p, see also the work [22].
In the present paper, we considered the free monoid ({0, 1,...,p − 1}m)∗ for
deﬁning p-recognizable sets of Nm. The monoid ({0, 1,...,p − 1}∗)m, which is not
free, could be used for deﬁning another concept of p-recognizable subset of Nm.
For m =2, M ⊆ N2 is called p-recognizable in this context if and only if the
set L = {((n)p, (m)p) | (n, m) ∈ M} is a recognizable subset of {0, 1,...,p − 1}∗ ×
{0, 1,...,p− 1}∗. Mezei’s theorem then states that L is a ﬁnite union of sets L1 × L2
where L1,L2 are recognizable sets of {0, 1,...,p − 1}∗ (see [24, p. 68]). This leads
to another version of the theorem of Cobham-Semenov [37] : Let p, q ⩾ 2 be two
multiplicatively independent integers, if M ⊆ N2 is p-and q-recognizable, then M
is a recognizable subset of N2 (and not only a rational subset of N2 as in Theorem
7.7).
Rational (rather than recognizable) subsets of the monoid {0,... ,p − 1}∗ ×
{0,...,p − 1}∗ are also much studied in relation with nonstandard representations
of numbers [31, 32]. The related automata, called transducers, have their transitions
labelled by pairs of words (u, v) ∈{0,... ,p − 1}∗ ×{0,... ,p − 1}∗, rather than by
pairs of letters as done in this paper (see [24]). For the Fibonacci base (fn)n⩾0 for
example, a number can have several representations; the function of normalization
which transforms any representation into the normal one (obtained by the usual
algorithm) can be realized by a ﬁnite transducer [31].
The study of p-recognizable sequences leads to interesting transcendence results
in number theory. If p is a prime number and s a p-algebraic sequence which is not

Logic and p-recognizable sets of integers 231

ultimately periodic, then the real number ∑ snp
−n is transcendental [45]. This gives
a method to easily generate transcendental numbers, as ∑ 2
−2n for example. See
[18] for connections between number theory and ﬁnite automata.
In the context of algebraic formal power series, other interesting results concern
diagonals of series [33, 19, 23]. Among them, one states that for a ﬁnite ﬁeld K,the
series S(x) ∈ K[[x]] is algebraic over K[x] if and only if it is the diagonal of some
rational formal power series T (x, y)= ∑ tn,mxnym ∈ K[[x, y]], i.e., S(x)= ∑ tn,nxn.
Another result is : let K be a ﬁeld with characteristic p ̸=0, if S(x, y) ∈ K[[x, y]] is
algebraic over K[x, y], then its diagonal is also algebraic (this is also true for more
than 2 variables x, y) [19]. When K is ﬁnite, this second theorem follows from the
works of [64], it is also a corollary of Theorem 5.1. Indeed the sequence s associated
with S(x, y)is p-deﬁnable by a formula ϕ(x, y)of ⟨N, +,Vp⟩. The formula ϕ(x, x)
of ⟨N, +,Vp⟩ shows that the diagonal of S(x, y) is algebraic.
The theories of the structures ⟨N, +⟩ and ⟨N, +,Vp⟩ are decidable. It is no longer
true for the structure ⟨N, +,Vp,Vq⟩ with p and q multiplicatively independent inte-
gers. The structure is indeed equivalent to ⟨N, +, ·⟩ [73, 74]. This undecidability
result is in a certain way a counterpart to the theorem of Cobham-Semenov, as
indicated by Figure 14. See also [21] for related work.

⟨N, +,Vp⟩
↗↘
⟨N, +⟩⟨N, +,Vp,Vq⟩
↘↗
⟨N, +,Vq⟩

Figure 14. The theory Th(⟨N, +,Vp,Vq⟩) is undecidable

In the same spirit, the decidability of the weak-monadic second-order theory ⟨N,S⟩
extended by one relation or by one function, is studied in [27, 69]. Semenov proves
that this decision problem comes back to rather special decision problems for rational
sets [69] (see also [4] for a complete proof). For instance, the weak-monadic second-
order structure ⟨N,S⟩ enriched by the function y =2x, already allows to interpret
all the ﬁrst-order formulae of ⟨N, +, ·⟩ and thus is an undecidable theory [27].
Several papers study in details rational subsets of Nm (those which are semi-
linear or equivalently deﬁnable in ⟨N, +⟩ according to Theorem 7.4). These sets
are unambigously rational. In other words they are ﬁnite unions of points and of
disjoint cones, with cones generated by linearly independent vectors [25, 44]. This
property generally holds in any commutative monoid [25]. Rational subsets of Nm

are classiﬁed and characterized in [57] with respect to logical formulae. Another
hierarchy based on rational transductions is proposed for N2 in [5]. See also the
reference [34] for a theorem of Fine and Wilf in N2.

Appendix

We prove in this appendix that any M ⊆ Nm deﬁnable in ⟨N, +⟩ is locally periodic
and has all its sections deﬁnable in ⟨N, +⟩.
The condition on the sections is trivial (see Corollary 6.4).

232 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

By a classical result [59], we can suppose that the formula ϕ(x1,...,xm) deﬁning
M is a Boolean combination of the formulae

ti(x1,...,xm) ⩾ ci 1 ⩽ i ⩽ r,
tj(x1,...,xm)= ej mod dr < j ⩽ s,

where ci,ej,d,m are constants (see also Section 7.2).
Any equation ti(x1,... ,xm)= ∑ ui,kxk = ci,1 ⩽ i ⩽ r, deﬁnes an hyperplane
orthogonal to the vector ui =(ui,1,... ,ui,m). Formulae ti(x1,... ,xm) ⩾ ci divide
Nm into domains. We show how to construct a ﬁnite set V of periods for M,from
these inequalities. Let I be a subset of the set of indices {1,... ,r}.We say that I
is a ﬁrst-type set if the family of vectors (ui)i∈I generates Nm,otherwise I is called
a second-type set. For any set I ⊆{1,...,r} of second type, let v ∈ Nm\{0} be
such that v =(v1,... ,vm) is orthogonal to any ui,i ∈ I. We can suppose that the
components vj of v are all divisible by d. These vectors v form the set V (see also
Figure 11).
Let K> |V |, K is the size of the neighbourhoods. Consider a K-neighbourhood
N (n, K), suppose that the hyperplanes ti(x1,... ,xm)= ci intersecting it are indexed
by a set I of the ﬁrst type. The intersection of these hyperplanes contains at most
one point. As the size of the neighbourhood is the constant K, the intersection point
is close to N (n, K). Moreover, in Nm there is a ﬁnite number of such intersection
points. Soit is possible tochoose L ⩾ 0 such that any neighbourhood N (n, K),
with |n| ⩾ L, intersects a set of hyperplanes indexed by a second-type set only.
Now let n ∈ Nm, |n| ⩾ L. Then, there is v ∈ V such that v is parallel to each of
the hyperplanes intersecting N (n, K). Vector v is a period for N (n, K). Indeed let
m, m + v ∈N (n, K). Consider the inequality ti(x)= ti(x1,...,xm) ⩾ ci associated
with an hyperplane intersecting N (n, K). Then

ti(m) ⩾ ci ⇔ ti(m + v) ⩾ ci

as v is parallel to this hyperplane. By construction, d divides all the components of
v. itfollows that forany formula tj(x)= ej mod d, r < j ⩽ s,we have

tj(m)= ej mod d ⇔ tj(m + v)= ej mod d.

This proves that m ∈ M if and only if m + v ∈ M.

Acknowledgements

We are thankful to A. Semenov who informed us about Muchnik’s preprint [54].
K. Archangelsky kindly translated this paper into English. We thank J.-P. Allouche,
J. Berstel, M. Boﬀa, C. Frougny and F. Point for fruitful discussions. We also thank
D. Perrin and J. Sakarovitch for pointing out some of the references. We are grateful
to the referees for valuable advices in improving the presentation of this paper.

References

[1] J.-P. Allouche, q-regular sequences and other generalizations of q-automatic
sequences, Proc. Latin’92, Lecture Notes in Comput. Sci. 583 (1992) 15–23.

Logic and p-recognizable sets of integers 233

[2] J.-P. Allouche, J. Shallit, The ring of k-regular sequences, Theoret. Comput.
Sci 98 (1991) 163–197.

[3] J. Barwise, An introduction to ﬁrst-order logic, in : Handbook of Mathematical
Logic, J. Barwise, Ed., North Holland, Amsterdam (1977) 5–46.

[4] P.T. Bateman, C.G. Jockusch, A.R. Woods, Decidability and undecidability
with a predicate for the primes, J. Symbolic Logic 58 (1993) 672–687.

[5] J. Berstel, Une hi´erarchie des parties rationnelles de N2, Math. Systems Theory
7 (1973) 114–137.

[6] A. Bertrand-Mathis, Comment ´ecrire les nombres entiers dans une base qui
n’est pas enti`ere, Acta Math. Acad. Sci. Hungar. 54 (1989) 237–241.

[7] M. Boﬀa, personal communication to V. Bruy`ere (1985).

[8] V. Bruy`ere, Entiers et automates ﬁnis, M´emoire de ﬁn d’´etudes,Universit´ede
Mons (1985).

[9] J.R. B¨uchi, Weak second-order arithmetic and ﬁnite automata, Z. Math. Logik
Grundlag. Math. 6 (1960) 66–92.

[10] A. ˇCern´y, J. Gruska, Modular Trellises, in : The book of L,G.Rozenberg and
A. Salomaa, Eds., Springer Verlag (1985) 45–61.

[11] G. Cherlin, F. Point, On extensions of Presburger arithmetic, Proc. 4th Easter
Model Theory conference, Gross K¨oris 1986 Seminarberichte 86, Humboldt Uni-
versit¨at zu Berlin (1986) 17–34.

[12] G. Christol, Ensembles presque periodiques k-reconnaissables, Theoret. Com-
put. Sci 9 (1979) 141-145.

[13] G. Christol, T. Kamae, M. Mend`es France, G. Rauzy, Suites alg´ebriques, auto-
mates et substitutions, Bull. Soc. Math. France 108 (1980) 401–419.

[14] A. Church, A note on the Entscheidungsproblem, J. Symbolic Logic 1 (1936)
40–41, 101–102.

[15] A. Cobham, On the base-dependence of sets of numbers recognizable by ﬁnite
automata, Math. Systems Theory 3 (1969) 186–192.

[16] A. Cobham, Uniform tag sequences, Math. Systems Theory 6 (1972) 164–192.

[17] K. Culik II, A. Salomaa, Ambiguity and decision problems concerning number
systems, Inform. and Control 56 (1983) 139–153.

[18] M. Dekking, M. Mend`es-France, A.J. Van der Poorten, Folds I, II, III, Math.
Intelligencer 4 (1982) 130–138, 173–181, 190–195.

[19] P. Deligne, Int´egration sur un cycle ´evanescent, Invent. Math. 76 (1984) 129–
143.

234 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

[20] F. Delon, Personal communication to C. Michaux and F. Point (1991).

[21] F. Delon, Pour l’arithm´etique faible de Penzin, Z est ind´ecidable et Q est
d´ecidable, preprint (1994).

[22] A. de Luca, A. Restivo, Star-free sets of integers, Theoret. Comput. Sci. 43
(1986) 265–275.

[23] J. Denef, L. Lipshitz, Algebraic power series and diagonals, J. Number Theory
26 (1987) 46–67.

[24] S. Eilenberg, Automata, Languages and Machines,Vol.A, Academic Press,
New-York (1974).

[25] S. Eilenberg, M.-P. Sch¨utzenberger, Rational sets in commutative monoids, J.
Algebra 13 (1969) 173–191.

[26] C.C. Elgot, Decision problems of ﬁnite automata design and related arithmetics,
Trans. Amer. Math. Soc. 98 (1961) 21–51.

[27] C.C. Elgot, M.O. Rabin, Decidability and undecidability of second (ﬁrst) order
theory of (generalized) successor, J. Symbolic Logic 31 (1966) 169–184.

[28] H.E. Enderton, An introduction to mathematical logic, Academic Press (1972).

[29] S. Fabre, Substitution et ind´ependance des syst`emes de num´eration, Thesis,
Universit´e Aix-Marseille II (1992).

[30] A.S. Fraenkel, Systems of numeration, Amer. Math. Monthly 92 (1985) 105–
114.

[31] C. Frougny, Representations of numbers and ﬁnite automata, Math. Systems
Theory 25 (1992) 37–60.

[32] C. Frougny, J. Sakarovitch, From the Fibonacci numeration system to the
golden mean base and some generalizations, Proc. FPSAC’93, A.Barlotti,M.
Delest and R. Pinzani, Eds. (1993) 231–244.

[33] H. Furstenberg, Algebraic functions over ﬁnite ﬁelds, J. Algebra 7 (1967) 271–
277.

[34] R. Giancarlo, F. Mignosi, Generalizations of the periodicity theorem of Fine
and Wilf, to appear in Proc. CAAP’94, Lecture Notes in Comput. Sci. (1994).

[35] S. Ginsburg, E.H. Spanier, Semigroups, Presburger formulas and languages,
Paciﬁc J. Math. 16 (1966) 285–296.

[36] G. Hansel, A propos d’un th´eor`eme de Cobham, in : Actes de la fˆete des mots,
D. Perrin, Ed., Greco de Programmation, CNRS, Rouen (1982).

[37] G. Hansel, Personal communication to V. Bruy`ere (1993).

Logic and p-recognizable sets of integers 235

[38] G.H. Hardy, E.M. Wright, An introduction to the theory of numbers,Oxford
University Press, Oxford, 5th ed. (1979).

[39] T. Harju, M. Linna, On the periodicity of morphisms on free monoids, RAIRO
Inform. Th´eor. Appl. 20 (1986) 47–54.

[40] B.R. Hodgson, D´ecidabilit´e par automate ﬁni, Ann. Sci. Math. Qu´ebec 7 (1983)
39–57.

[41] J. Honkala, Bases and ambiguity of number systems, Theoret. Comput. Sci. 31
(1984) 61–71.

[42] J. Honkala, A decision method for the recognizability of sets deﬁned by number
systems, RAIRO Inform. Th´eor. Appl. 20 (1986) 395–403.

[43] J.E. Hopcroft, J.D. Ullman, Introduction to automata theory, languages and
computation, Addison-Wesley (1979).

[44] R. Ito, Every semilinear set is a ﬁnite union of disjoint linear sets, J. Comput.
System Sci. 3 (1969) 221–231.

[45] J.H. Loxton, A.J. van der Poorten, Arithmetic properties of the solutions of a
class of functional equations, J. Reine Angew. Math. 330 (1982) 159–195.

[46] R. MacNaughton, review of [9], J. Symbolic Logic 28 (1963) 100–102.

[47] H. Maurer, A. Salomaa, D. Wood, L codes and number systems, Theoret.
Comput. Sci. 22 (1983) 331–346.

[48] C. Michaux, F. Point, Les ensembles k-reconnaissables sont d´eﬁnissables dans
⟨N, +,Vk⟩, C. R. Acad. Sci. Paris 303 (1986) 939–942.

[49] C. Michaux, R. Villemaire, Cobham’s theorem seen through B¨uchi theorem,
Proc. Icalp’93, Lecture Notes in Comput. Sci. 700 (1993) 325–334.

[50] C. Michaux, R. Villemaire, Presburger arithmetic and recognizability of natural
numbers by automata : new proofs of Cobham’s and Semenov’s theorems, in
preparation (1993).

[51] M. Minsky, S. Papert, Unrecognizable sets of numbers, J. Assoc. Comput.
Mach. 13 (1966) 281–286.

[52] M. Morse, G.A. Hedlund, Symbolic dynamics, Amer. J. Math. 60 (1938) 815–
866.

[53] M. Morse, G.A. Hedlund, Symbolic dynamics II. Sturmian trajectories Amer.
J. Math. 62 (1940) 1–42.

[54] A. Muchnik, Deﬁnable criterion for deﬁnability in Presburger Arithmetic and
its application, preprint in Russian, Institute of New Technologies (1991).

[55] J.-J. Pansiot, Decidability of periodicity for inﬁnite words, RAIRO Inform.
Th´eor. Appl. 20 (1986) 43–46.

236 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

[56] W. Parry, On the β-expansions of real numbers, Acta Math. Acad. Sci. Hungar.
11 (1960) 401–416.

[57] P. P´eladeau, Logically deﬁned subsets of Nk, Theoret. Comput. Sci. 93 (1992)
169–183.

[58] D. Perrin, Finite automata, in : Handbook of Theoretical Computer Science,
vol. B, J. Van Leeuwen, Ed., Elsevier (1990) 2–57.

[59] M. Presburger, ¨Uber die Volst¨andigkeit eines gewissen Systems der Arithmetik
ganzer Zahlen, in welchem die Addition als einzige Operation hervortritt, C. R.
1er congr`es des Math´ematiciens des pays slaves, Varsovie (1929) 92–101.

[60] M.O. Rabin, Decidable theories, in : Handbook of Mathematical Logic,J.
Barwise, Ed., North Holland, Amsterdam (1977) 595–629.

[61] G. Rauzy, Nombres alg´ebriques et substitutions, Bull. Soc. Math. France 110
(1984) 147–178.

[62] C. Reutenauer, D´emonstration du th´eor`eme de Cobham sur les ensembles de
nombres reconnaissables par automate ﬁni, d’apr`es Hansel, in : S´eminaire
d’Informatique Th´eorique,Ann´ee 1983-84, Universit´e Paris 7, Paris (1984) 217–
224.

[63] R.W. Ritchie, Finite automata and the set of squares, J. Assoc. Comput. Mach.
10 (1963) 528–531.

[64] O. Salon, Suites automatiques `a multi-indices et alg´ebricit´e, C. R. Acad. Sci.
Paris 305 (1987) 501–504.

[65] O. Salon, Suites automatiques `a multi-indices, S´eminaire de Th´eorie des Nom-
bres de Bordeaux,Expos´e 4 (1986-1987) (suivi d’un appendice par J. Shallit).

[66] A.L. Semenov, Presburgerness of predicates regular in two number systems (in
Russian), Sibirsk. Mat. Zh. 1
¯
8 (1977) 403–418, English translation, Siberian
Math. J. 18 (1977) 289–299.

[67] A.L. Semenov, On certain extensions of the arithmetic of addition of natu-
ral numbers, Izv. Akad. Nauk. SSSR ser. Mat. 43 (1979) 1175–1195, English
translation, Math. USSR-Izv. 15 (1980) 401–418.

[68] A.L. Semenov, Logical theories of one-place functions on the set of natural
numbers (in Russian), Izv. Akad. Nauk. SSSR ser. Mat. 47 (1983) 623–658,
English translation, Math. USSR-Izv. 22 (1984) 587–618.

[69] A.L. Semenov, Decidability of monadic theories, in : Proc. MFCS’84, M.P.
Chytil and V. Koubek, Eds., Lecture Notes in Comput. Sci. 176 (1984) 162–
175.

[70] J. Shallit, A generalization of automatic sequences, Theoret. Comput. Sci. 61
(1988) 1–16.

Logic and p-recognizable sets of integers 237

[71] W. Thomas, Automata on inﬁnite objects, in : Handbook of Theoretical Com-
puter Science, vol. B, J. Van Leeuwen, Ed., Elsevier (1990) 135–191.

[72] L. van den Dries, The ﬁeld of reals with a predicate for the powers of two,
Manuscripta Math. 54 (1985) 187–195.

[73] R. Villemaire, Joining k-and l-recognizable sets of natural numbers, Proc.
Stacs’92, Lecture Notes in Comput. Sci. 577 (1992) 83–94.

[74] R. Villemaire, The theory of ⟨N, +,Vk,Vl⟩ is undecidable, Theoret. Comput.
Sci. 106 (1992) 337–349.
 V´eronique Bruy`ere, Christian Michaux
Universit´e de Mons-Hainaut
15, Avenue Maistriau
B-7000 Mons
Belgique

Georges Hansel
Universit´ede Rouen
Laboratoire d’Informatique de Rouen
Place Blondel
F-76134 Mont Saint-Aignan
France

Roger Villemaire
Universit´edu Qu´ebec `aMontr´eal
D´epartement de Math´ematiques et d’Informatique
C.P. 8888, succ. centre-ville
Montr´eal (Qu´ebec)
Canada H3C 3P8

238 V. Bruy`ere - G. Hansel - C. Michaux - R. Villemaire

Index

alphabet, 193
automaton, 193
complete, 193
compute, 193
deterministic, 193
minimal, 193
state, 193
transition, 193
with output, 193
theorem of Cobham-Semenov, 218
cone, 216
deﬁnability criterion, 216
diagonal, 194
equivalence relation
p-stable, 224
right-congruence, 193
right-stable, 193
formula, 195
atomic, 195
free monoid, 193
integer
simple, 219
integers
multiplicatively dependent, 213
multiplicatively independent, 218
Kleene’s theorem, 194
K-neighbourhood, 216
letter, 193
output function, 193
p-ary expansion, 200
p-automaton, 199, 205
period, 214, 216
p-kernel, 202
p-substitution, 199, 206
rational operations, 194
section, 216
sentence, 195
sequence, 199, 204
p-algebraic, 199, 206
p-deﬁnable, 199, 205
p-recognizable, 199, 205
syndetic, 219
ultimately periodic,214
set deﬁnable, 196
ﬁrst-type, 232
locally periodic, 216
p-recognizable, 200, 207
rational, 194
recognizable, 193, 194
second-type, 232
semilinear, 215
v-periodic, 216
 structure, 194
language, 194
weak-monadic, 202, 231
structures
equivalent, 196
term, 195
theory, 197
decidable, 197
value, 200
word, 193
empty, 193
length, 193
reverse, 193
wR, 193
∼L, 193
∼p,M , 201, 224
∼p,q,M, 225
|=, 196
Th(S), 197
V2(x), 198
Vp(x), 199
(n)p, 200
[w]p, 200
P2(x), 198, 202
Pp(x), 202
∈2(x, y), 202
∈j,p(x, y), 209
λ2(x), 204
λp(x), 209
N (n, K), 216
|r|, 216
|V |, 216
