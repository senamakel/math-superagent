<!-- source: https://orbi.uliege.be/bitstream/2268/39461/1/Chapter26.pdf | converted from PDF -->

On Cobham’s theorem

Fabien Durand
1 and Michel Rigo
2

1LAMFA - Universit´e de Picardie Jules Verne - CNRS UMR 6140
33 rue Saint Leu, F-80039 Amiens cedex 1, France
email: fabien.durand@u-picardie.fr

2Universit´e de Li`ege, Institut de Math´ematiques
12 All´ee de la d´ecouverte (B37), B-4000 Li`ege, Belgique
email: M.Rigo@ulg.ac.be

2010 Mathematics Subject Classiﬁcation: 68Q45, 68R15, 11B85, 11A67, 11U05, 37B20

Key words: Numeration systems, recognizable sets of integers, Cobham’s theorem, ultimate peri-
odicity, substitutions, dynamical systems.
Contents

1 Introduction 897
2 Numeration basis 899
3 Automatic sequences 903
4 Multidimensional extension and ﬁrst-order logic 905
4.1 Subsets of N
d . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 905
4.2 Logic and k-deﬁnable sets . . . . . . . . . . . . . . . . . . . . . . . . . 906
5 Numeration systems and substitutions 908
5.1 Substitutive sets and abstract numeration systems . . . . . . . . . . . . . 908
5.2 Cobham’s theorem for substitutive sets . . . . . . . . . . . . . . . . . . . 910
5.3 Density, syndeticity and bounded gaps . . . . . . . . . . . . . . . . . . . 914
5.3.1 The length of the iterates . . . . . . . . . . . . . . . . . . . . . . 914
5.3.2 Letters and words appear with bounded gaps . . . . . . . . . . . 915
5.4 Ultimate periodicity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 917
5.5 The case of ﬁxed points . . . . . . . . . . . . . . . . . . . . . . . . . . . 918
5.6 Back to numeration systems . . . . . . . . . . . . . . . . . . . . . . . . 919
5.6.1 Polynomially-growing abstract numeration systems . . . . . . . . 919
5.6.2 Bertrand basis and ωα-substitutive words . . . . . . . . . . . . . 919
6 Cobham’s theorem in various contexts 920
6.1 Regular sequences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 920
6.2 Algebraic setting and quasi-automatic functions . . . . . . . . . . . . . . 920

On Cobham’s theorem 897

6.3 Real numbers and veriﬁcation of inﬁnite-state systems . . . . . . . . . . . 921
6.4 Dynamical systems and subshifts . . . . . . . . . . . . . . . . . . . . . . 922
6.5 Tilings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 924
6.5.1 From deﬁnable sets . . . . . . . . . . . . . . . . . . . . . . . . . 924
6.5.2 Self-similar tilings . . . . . . . . . . . . . . . . . . . . . . . . . 925
6.6 Toward Cobham’s theorem for the Gaussian integers . . . . . . . . . . . . 925
6.7 Recognizability over Fq[X] . . . . . . . . . . . . . . . . . . . . . . . . . 926
7 Decidability issues 926
8 Acknowledgments 927
References 927

1 Introduction

In this chapter we essentially focus on the representation of non-negative integers in a
given numeration system. The main role of such a system — like the usual integer base-
k numeration system — is to replace numbers, or more generally sets of numbers, by
their corresponding representations, i.e., by words or languages. First we consider integer
base numeration systems to present the main concepts, but rapidly we will introduce non-
standard systems and their relationship with substitutions.
Let k ∈ N⩾2 be an integer, where N⩾2 denotes the set of non-negative integers greater
than or equal to 2. The set {0, . . . , k} is denoted by [[0, k]]. If we do not allow leading
zeroes when representing numbers, the function mapping a non-negative integer n onto its
k-ary representation repk(n) ∈ [[0, k − 1]]∗ is a one-to-one correspondence. In particular,
0 is assumed to be represented by the empty word ε. In the literature, one also ﬁnds
notation such as ⟨n⟩k, (n)k, or ρk(n) instead of repk(n). Hence every subset X ⊆ N
is associated with the language repk(X) consisting of the k-ary representations of the
elements of X.
It is natural to study the relation between the arithmetic or number-theoretic proper-
ties of integers and the syntactical properties of the corresponding representations in a
given numeration system. We focus on those sets X ⊆ N for which a ﬁnite automaton
can be used to decide, for any given word w over [[0, k − 1]], whether or not w belongs
to repk(X). Sets having the property that repk(X) is regular1 are called k-recognizable
sets. Such a set can be considered as a particularly simple set, because using the k-ary nu-
meration system it has a somehow elementary algorithmic description. In the framework
of inﬁnite-state system veriﬁcation, one also ﬁnds the terminology of Number Decision
Diagram or NDD [130].
The essence of Cobham’s theorem is to express that the property of being recognizable
by a ﬁnite automaton strongly depends on the choice of the base and more generally on the
considered numeration system. Naturally, this fact leads to and motivates the introduction
and the study of recognizable sets in non-standard numeration systems. Considering al-
ternative numeration systems may provide new recognizable sets and these non-standard
systems also have applications in computer arithmetic [63]. Last but not least, the proof

1We use the terminology of regular language, instead of rational language.

898 F. Durand, M. Rigo

of Cobham’s theorem is non-trivial and relies on quite elaborate arguments.
Now let us state Cobham’s celebrated result from 1969 and give all the needed details
and deﬁnitions. Several surveys have been written on the same subject; see [25, 26, 29,
28, 104].

Deﬁnition 1.1. Let α, β > 1 be two real numbers. If the equation αm = βn with
m, n ∈ N has only the trivial integer solution m = n = 0, then α and β are said
to be multiplicatively independent. Otherwise, α and β are said to be multiplicatively
dependent.

Deﬁnition 1.2. A subset of N is ultimately periodic if it is the union of a ﬁnite set and a
ﬁnite number of inﬁnite arithmetic progressions. In particular, X is ultimately periodic if
and only if there exist N ⩾ 0 and p ⩾ 1 such that for all n ⩾ N , n ∈ X ⇔ n + p ∈ X.
Recall that an arithmetic progression is a set of the form aN + b := {an + b | n ⩾ 0}.

Theorem 1.1 (Cobham’s theorem [37]). Let k, ℓ ⩾ 2 be two multiplicatively independent
integers. A set X ⊆ N is both k-recognizable and ℓ-recognizable if and only if it is
ultimately periodic.

In the various contexts that we will describe, showing that an ultimately periodic set
is recognizable is always the easy direction to prove (see Remark 1.3). So we focus on
the other direction.
Let k, ℓ ⩾ 2 be two integers. Notice that k and ℓ are multiplicatively independent if
and only if log k/ log ℓ is irrational. Note that for k and ℓ to be multiplicatively depen-
dent, it is not enough that k and ℓ share exactly the same prime factors occurring in their
decomposition. For instance, 6 and 18 are multiplicatively independent. But coprime
integers are multiplicatively independent.
The irrationality of log k/ log ℓ is a crucial point in the proof of Cobham’s theorem
(see Subsection 5.3). Recall that if θ > 0 is irrational, then the set {{nθ} | n > 0}
of fractional parts of the multiples of θ is dense in [0, 1]. For a proof of the so-called
Kronecker theorem; see [70].

Remark 1.2. Multiplicative dependence is an equivalence relation M over N⩾2. If k
and ℓ are multiplicatively dependent, then there exist a minimal q ⩾ 2 and two positive
integers m, n such that k = qm and ℓ = qn. Let us give the ﬁrst (with respect to their
minimal element) few equivalence classes for M partitioning N⩾2 : [2]M, [3]M, [5]M,
[6]M, [7]M, [10]M, [11]M, [12]M, . . . .

Remark 1.3. We show that if a set X ⊆ N is ultimately periodic then, for all k ⩾ 2, X
is k-recognizable. In the literature, one also ﬁnds the terminology of a recognizable set
X (without any mention to a base), meaning that X is k-recognizable for all k ⩾ 2. Note
that a ﬁnite union of regular languages is again a regular language. Hence it is enough to
check that repk(aN + b) is regular with 0 ⩽ b < a. We can indeed assume that b < a
because if we add a ﬁnite number of words to a regular language or if we or remove a ﬁnite
number of words from a regular language, we still have a regular language. Consider a
DFA having Q = [[0, a − 1]] as its set of states. For all state i ∈ Q and d ∈ [[0, k − 1]], the

On Cobham’s theorem 899

transitions are given by
 i d
−→ ki + d mod a.

The initial state is 0 and the unique ﬁnal state is b. As an example, a DFA accepting
exactly the binary representations of the integers congruent to 3 mod 4 is given in Figure 1.
A study of the minimal automaton recognizing such divisibility criteria expressed in an

0
 1
 2 30
 1 0
 1

0
 1
 0
 1

Figure 1. A ﬁnite automaton accepting rep2(4N + 3).

integer base is given in [3]. Also see the discussion in [117, Prologue]. The fact that a
divisibility criterion exists in every base for any ﬁxed divisor was already observed by
Pascal in [103, pp. 84–89].
 2 Numeration basis

It is remarkable that the recognizability of ultimately periodic sets extends to wider con-
texts (see Proposition 2.6 and Theorem 5.1). Let us introduce our ﬁrst generalization of
the integer base numeration system.

Deﬁnition 2.1. A numeration basis is a sequence U = (Un)n⩾0 of integers such that U
is increasing, U0 = 1 and that the set {Ui+1/Ui | i ⩾ 0} is bounded. This latter condition
ensures the ﬁniteness of the alphabet of digits used to represent integers. If w = wℓ · · · w0
is a word over a ﬁnite alphabet A ⊂ Z then the numerical value of w is

πA,U (w) =
 ℓ∑

i=0 wi Ui.

Using the greedy algorithm [61], any integer n has a unique (normal) U -representation
repU (n) = wℓ · · · w0, which is a ﬁnite word over a minimal ﬁnite alphabet called the
canonical alphabet of U and denoted by AU . The normal U -representation satisﬁes

πAU ,U (repU (n)) = n and i ∈ [[0, ℓ − 1]], πAU ,U (wi · · · w0) < Ui+1 for all i ∈ [[0, ℓ − 1]].

Again, repU (0) = ε. See [90, Chapter 7] or Ch. Frougny and J. Sakarovitch’s chapter in
[12, Chapter 2]. A subset X ⊆ N is U -recognizable if repU (X) is accepted by a ﬁnite
automaton. Let B ⊂ Z be a ﬁnite alphabet. If w ∈ B∗ is such that πB,U (w) ⩾ 0, then
the function mapping w onto repU (πB,U (w)) is called normalization.

900 F. Durand, M. Rigo

Deﬁnition 2.2. A numeration basis U is said to be linear if there exist k ∈ N \ {0},
d1, . . . , dk ∈ Z, dk ̸= 0, such that, for all n ⩾ k, Un = d1Un−1 + · · · + dkUn−k. The
polynomial PU (X) = X k − d1X k−1 − · · · − dk−1X − dk is called the characteristic
polynomial of U .

Deﬁnition 2.3. Recall that a Pisot-Vijayaraghavan number is an algebraic integer β > 1
whose Galois conjugates have modulus strictly less than one. We say that U = (Un)n⩾0
is a Pisot numeration system if the numeration basis U is linear and PU (X) is the minimal
polynomial of a Pisot number β. Integer base numeration systems are particular cases of
Pisot systems. For instance, see [27] where it is shown that most properties related to
k-recognizable sets, k ∈ N⩾2, can be extended to Pisot systems. In such a case, there
exists some c > 0 such that |Un − c βn| → 0, as n tends to inﬁnity.

Example 2.1. Consider the Fibonacci sequence deﬁned by U0 = 1, U1 = 2 and Un+2 =
Un+1 + Un for all n ⩾ 0. A word over {0, 1} is a U -representation if and only if it
belongs to the language L = 1{0, 01}
∗ ∪ {ε}. For instance, the word 10110 is not a U -
representation. Since πAU ,U (10110) = 13, the normalization maps 10110 to repU (13) =
100000. The characteristic polynomial of this linear numeration basis is the minimal
polynomial of the Pisot number (1 + √5)/2. This Pisot numeration system is presented
in [131].

The following result is an easy exercise, but also can be carried out in a wider context.

Theorem 2.1. [123] Let U be a numeration basis. If N is U -recognizable, then U is
linear.

Deﬁnition 2.4. [13] A Bertrand numeration basis U is a numeration basis satisfying the
following property: w ∈ repU (N) if and only if, for all n ∈ N, w0
n ∈ repU (N). It is a
natural condition satisﬁed by all integer base k ⩾ 2 systems. For instance, the sequence
deﬁned by U0 = 1, U1 = 3 and, for all n ⩾ 0, Un+2 = Un+1 + Un is not a Bertrand
numeration basis because repU (2) = 2, but πAU ,U (20) = 6 and repU (6) = 102.

Let α > 1 be a real number. The notion of α-expansion was introduced by Parry in
[102] (also see R´enyi’s paper [111]), or again see [90, Chapter 7]. All x ∈ [0, 1] can be
uniquely written in the following way:

x = ∑

n⩾1 anα−n, (2.1)

with x1 = x and for all n ⩾ 1, an = ⌊α xn⌋ and xn+1 = {αxn}, where ⌊·⌋ stands
for the integer part. The sequence dα(x) = (an)n⩾1 is the α-expansion of x and L(α)
denotes the set of ﬁnite words having an occurrence in some sequence dα(x), x ∈ [0, 1].
Let dα(1) = (tn)n⩾1. If there exist N ⩾ 0, p > 0 such that, for all n ⩾ N , we have
tn+p = tn then α is said to be a Parry number, sometimes called a β-number (for more
details about these numbers, see [102] or [62]). Observe that integers greater or equal to
2 are Parry numbers.
The following result relates Bertrand numeration systems to languages deﬁned by
some real number.
 On Cobham’s theorem 901

Theorem 2.2 (A. Bertrand-Mathis [14]). Let U be a numeration basis. It is a Bertrand
numeration basis if and only if there exists a real number α > 1 such that repU (N) =
L(α). In this case, if U is linear then α is a root of the characteristic polynomial of U .

Theorem 2.3 (A. Bertrand-Mathis [13]). Let α > 1 be a real number. The language
L(α) is regular if and only if α is a Parry number.

Associated with a Parry number β, one can deﬁne the notion of beta-polynomial. For
details, see [72] or [12, Chapter 2]. First we deﬁne the canonical beta-polynomial. If
dβ(1) is eventually constant and equal to 0: dβ(1) = t1 · · · tm0
ω, with tm ̸= 0, then
we set Gβ(X) = X m − ∑m=1 tiX m−i and r = m. Otherwise, dβ(1) is eventually
periodic: dβ(1) = t1 · · · tm(tm+1 · · · tm+p)ω, with m and p being minimal. Then we
set Gβ(X) = X m+p − ∑m+p
i=1 tiX m+p−i − X m + ∑m=1 tiX m−i and r = p. Let β
be a Parry number. An extended beta-polynomial is a polynomial of the form Hβ(X) =
Gβ(X)(1 + X r + · · · + X rk)X n for k, n ∈ N.

Proposition 2.4. [
72] Let U be a linear numeration basis with dominant root β, i.e.,
limn→∞ Un+1/Un = β for some β > 1. If repU (N) is regular, then β is a Parry number.

Theorem 2.5 (M. Hollander [72]). Let U be a linear numeration basis whose dominant
root β is a Parry number.
• If dβ(1) is inﬁnite and eventually periodic, then repU (N) is regular if and only if U
satisﬁes an extended beta-polynomial for β.
• If dβ(1) is ﬁnite of length m, then: if U satisﬁes an extended beta-polynomial
for β then repU (N) is regular; and conversely if repU (N) is regular, then U sat-
isﬁes either an extended beta-polynomial for β, Hβ(X), or a polynomial of the
form (X m − 1)Hβ(X).

Ultimately periodic sets are recognizable for any linear numeration basis.

Proposition 2.6 (Folklore [12, 90]). Let a, b ⩾ 0. If U = (Un)n⩾0 is a linear numeration
basis, then
 π−1
AU ,U (a N + b) = {
cℓ · · · c0 ∈ A
∗
U |
 ℓ∑

k=0 ck Uk ∈ a N + b}

is accepted by a DFA that can be effectively constructed. In particular, if N is U -recogni-
zable, then any ultimately periodic set is U -recognizable.

To conclude this section, consider again the integer base numeration systems.

Example 2.2. The set P2 = {2
n | n ⩾ 0} of powers of two is trivially 2-recognizable
because rep2(P2) = 10
∗. Since the difference between any two consecutive elements in
P2 is of the form 2
n, the set P2 is not ultimately periodic. As a consequence of Cobham’s
theorem, the set P2 is, for instance, neither 3-recognizable nor 5-recognizable.

One could also consider the case when the two bases k and ℓ are multiplicatively
dependent. This case is much easier and can be considered as an exercise.

902 F. Durand, M. Rigo

Proposition 2.7. Let k, ℓ ⩾ 2 be two multiplicatively dependent integers. A set X ⊆ N
is k-recognizable if and only if it is ℓ-recognizable.

The theorem of Cobham implies that ultimately periodic sets are the only inﬁnite sets
that are k-recognizable for every k ⩾ 2. We have seen so far that there exist sets (like the
set P2 of powers of two) that are only recognizable for some speciﬁc bases: exactly all
bases belonging to a unique equivalence class for the equivalence relation M over N⩾2.
To see that a given inﬁnite ordered set X = {x0 < x1 < x2 < · · · } is k-recognizable
for no base k ⩾ 2 at all, we can use results like the following one, where the behavior of
the ratio (resp., difference) of any two consecutive elements in X is studied through the
quantities
 RX = lim sup
i→∞
 xi+1
xi and DX = lim sup
i→∞ (xi+1 − xi) .

Theorem 2.8 (Gap theorem [38]). Let k ⩾ 2. If X ⊆ N is a k-recognizable inﬁnite
subset of N, then either RX > 1 or DX < +∞.

Corollary 2.9. Let a ∈ N⩾2. The set of primes and the set {n
a | n ⩾ 0} are not
k-recognizable for any integer base k ⩾ 2.

Proofs of the gap theorem and its corollary can also be found in [55]. For more results
on primes; also see Chapter 25 “Automata in number theory” of this handbook.

Deﬁnition 2.5. An inﬁnite ordered set X = {x0 < x1 < x2 < · · · } such that DX <
+∞ is said to be syndetic or with bounded gaps: there exists C > 0 such that for all
n ⩾ 0, xn+1 − xn < C. In particular, any ultimately periodic set is syndetic. The
converse does not hold; see, for instance Example 3.1.

Remark 2.10. Note that syndeticity occurs in various contexts, such as ergodic theory.
As an example, a subset of an Abelian group G is said to be syndetic if ﬁnitely many
translates of it cover G. The term “syndetic” was ﬁrst used in [66]. Note that in [68] the
following result is proved. Let α, β > 1 be multiplicatively independent real numbers. If
a set X ⊆ N is α-recognizable and β-recognizable, for the Bertrand numeration systems
based, respectively, on the real numbers α and β in the sense of [14] and Theorem 2.2,
then X is syndetic.

Cobham’s original proof of Theorem 1.1 appeared in [37] and we quote [55]: “The
proof is correct, long and hard. It is a challenge to ﬁnd a more reasonable proof of this
ﬁne theorem”. Then G. Hansel provided a simpler presentation in [67], and one can see
[104] or the dedicated chapter in [9] for an expository presentation. Prior to these last two
references, one should read [116]. Usually the ﬁrst step to prove Cobham’s theorem is to
show the syndeticity of the considered set. See Section 5.3. T. Krebs recently presented a
short proof of Cobham’s theorem without using Kronecker theorem [82].

On Cobham’s theorem 903

3 Automatic sequences

As explained in Corollary 3.3 presented in this section, the formalism of k-recognizable
sets is equivalent to that of of k-automatic sequences2. Let us recall brieﬂy what they are.
An inﬁnite word x = (xn)n⩾0 ∈ BN over an alphabet B is said to be k-automatic if there
exists a DFAO (deterministic ﬁnite automaton with output) over the alphabet [[0, k − 1]],
(Q, [[0, k − 1]], ·, q0, B, τ ) such that, for all n ⩾ 0,

xn = τ (q0 · repk(n)) .

The transition function is · : Q × [[0, k − 1]] → Q and can easily be extended to Q ×
[[0, k − 1]]∗ by q · ε = q and q · wa = (q · w) · a. The output function is τ : Q →
B. Roughly speaking, the nth term of the sequence is obtained by feeding a DFAO
with the k-ary representation of n. For a complete and comprehensive exposition on k-
automatic sequences and their applications, see the book [9]. We equally use the terms of
sequences or (right-) inﬁnite words. For more information about combinatorics on words,
see [89, 90] or also J. Cassaigne and F. Nicolas’ chapter in [12, Chapter 4].

Deﬁnition 3.1. Let σ : A
∗ → A
∗ be a morphism, i.e., σ(uv) = σ(u)σ(v) for all u, v ∈
A
∗. Naturally such a map can be deﬁned on A
ω. A ﬁnite or inﬁnite word x such that
σ(x) = x is said to be a ﬁxed point of σ. A morphism σ : A
∗ → A
∗ is completely
determined by the images of the letters in A. In particular, if there exists k ⩾ 0 such
that |σ(a)| = k for all a ∈ A, then σ is said to be of k-uniform or simply uniform. A
1-uniform morphism is called a coding. If there exist a letter a ∈ A and a word u ∈ A
+

such that σ(a) = au and moreover, if limn→+∞ |σn(a)| = +∞, then σ is said to be
prolongable on a or to be a substitution. Let σ : A
∗ → A
∗ be a morphism prolongable on
a. We have
 σ(a) = a u, σ2(a) = a u σ(u), σ3(a) = a u σ(u) σ2(u), . . . .

Since for all n ∈ N, σn(a) is a preﬁx of σn+1(a) and because |σn(a)| tends to inﬁnity
when n → +∞, the sequence (σn(a))n⩾0 converges (for the usual product topology on
words — see, for instance (6.2)) to an inﬁnite word denoted by σ∞(a) and given by

σ∞(a) := lim
n→+∞ σn(a) = a u σ(u) σ2(u) σ3(u) · · · .

This inﬁnite word is a ﬁxed point of σ. An inﬁnite word obtained by iterating a pro-
longable morphism in this way is said to be purely substitutive (or pure morphic). If
σ : A
∗ → B∗ is a non-erasing morphism, it can be extended to a map from A
N to BN

as follows. If x = x0x1 · · · is an inﬁnite word over A, then the sequence of words
(σ(x0 · · · xn−1))n⩾0 is easily seen to converge to an inﬁnite word over B. Its limit
is denoted by σ(x) = σ(x0)σ(x1)σ(x2) · · · . If x ∈ A
N is purely substitutive and if
τ : A → B is a coding, then the word y = τ (x) is said to be substitutive.

Another result due to A. Cobham is the following; see [38]. The idea is to associate a
DFA over [[0, k − 1]] with every k-uniform morphism.

2We indifferently use the terms sequence and inﬁnite word.

904 F. Durand, M. Rigo

Theorem 3.1. Let k ⩾ 2. A sequence x = (xn)n⩾0 ∈ BN is k-automatic if and only
if there exist a k-uniform morphism σ : A
∗ → A
∗ prolongable on a letter a ∈ A and a
coding τ : A → B such that x = τ (σ∞(a)).

Theorem 3.2 (Eilenberg [55]). A sequence x = (xn)n⩾0 is k-automatic if and only if its
k-kernel Nk(x) = {(xken+d)n⩾0 | e ⩾ 0, 0 ⩽ d < ke} is ﬁnite.

Deﬁnition 3.2. The characteristic sequence1X ∈ {0, 1}
N of a set X ⊆ N is deﬁned by1X (n) = 1 if and only if n ∈ X.

An inﬁnite word x ∈ A
ω is ultimately periodic if there exist two ﬁnite words u ∈ A
∗

and v ∈ A
+ such that x = uvω. If u = ε, then x is periodic. Obviously, a set X ⊆ N
is ultimately periodic if and only if1X is an ultimately periodic word over {0, 1}. In that
case, there exist two ﬁnite words u ∈ {0, 1}
∗ and v ∈ {0, 1}
+ such that1X = uvω. In
particular, |v| is a period of X. If u and v are chosen of minimal length, then |u| (resp.,
|v|) is said to be the preperiod or index of X (resp., the period of X). If u = ε, then X is
(purely) periodic. Periodic sets are, in particular, ultimately periodic.

Corollary 3.3. Let k ⩾ 2. If x = (xn)n⩾0 ∈ BN is a k-automatic sequence, then the
set {n ⩾ 0 | xn = b} is k-recognizable for all b ∈ B. Conversely, if a set X ⊆ N is
k-recognizable, then its characteristic sequence is k-automatic.

Theorem 3.4 (Cobham’s theorem, version 2). Let k, ℓ ⩾ 2 be two multiplicatively in-
dependent integers. An inﬁnite word x = (xn)n⩾0 ∈ BN is both k-automatic and ℓ-
automatic if and only if it is ultimately periodic.

Remark 3.5. Using the framework of k-automatic sequences instead of the formalism of
k-recognizable sets turns out to be useful. For instance, consider the complexity function
of an inﬁnite word x, which maps n ∈ N onto the number px(n) of distinct factors of
length n occurring in x. The Morse–Hedlund theorem states that x is ultimately periodic
if and only if px is bounded by some constant. This result appeared ﬁrst in [96]. Proofs
can be found in classical textbooks such as [9, 89].
It is also well known that for a k-automatic sequence x, px ∈ O(n); again see the
seminal paper [38]. This latter result can be used to show that particular sets are not k-
recognizable for any k ⩾ 2: for instance, those sets whose characteristic sequence1X
has a complexity function such that limn→+∞ p1X (n)/n = +∞. For the behavior of px
in the substitutive case, see the survey [4] or [12, Chapter 4].

Example 3.1. Iterating the morphism σ : 0 ↦→ 01, 1 ↦→ 10, we get the Thue–Morse
word (tn)n⩾0 = σ∞(0) = 0110100110010110100101100110 · · · . For an account of this
celebrated word, see [8] and [60, Chapter 2]. It is a 2-automatic word; the nth letter in the
word is 0 if and only if rep2(n) contains an even number of 1’s. This word is generated
by the DFAO represented in Figure 2. In particular, the set

X2 =
 {
n ∈ N | rep2(n) = ct · · · c0 and
 t∑

i=0 ci ≡ 0 (mod 2)
}

On Cobham’s theorem 905

0 1

0 0

1

1
Figure 2. A DFAO generating the Thue–Morse word.

is 2-recognizable. The Thue–Morse word is not ultimately periodic (see, for instance [23]
or [41] where the complexity function of this word is studied carefully) and therefore X2
is k-recognizable only for those k of the form 2
m, m ∈ N⩾1. Nevertheless, one can notice
that X2 is syndetic.

4 Multidimensional extension and ﬁrst-order logic

4.1 Subsets of N
d

To extend the concept of k-recognizability to subsets of N
d, d ⩾ 2, it is natural to con-
sider d-tuples of k-ary representations. To be self-contained, we repeat the discussions of
Chapter 25 “Automata in number theory” of this handbook. To get d words of the same
length that have to be read simultaneously by an automaton, the shortest ones are padded
with leading zeroes. We extend the deﬁnition of repk to a map of domain N
d as follows.
If n1, . . . , nd are non-negative integers, then we consider the word

repk(n1, . . . , nd) :=
 



0
m−| repk(n1)| repk(n1)
...
0
m−| repk(nd)| repk(nd)



 ∈ ([[0, k − 1]]d)∗

where m = max{| repk(n1)|, . . . , | repk(nd)|}. A subset X of N
d is k-recognizable if
the corresponding language repk(X) is accepted by a ﬁnite automaton over the alphabet
[[0, k − 1]]d which is the Cartesian product of d copies of [[0, k − 1]]. This automaton is
reading d digits at a time (one for each component): this is why we need d words of the
same length.

Example 4.1. Consider the automaton depicted in Figure 3 (the sink is not represented).
It accepts (ε, ε) and all pairs of words of the form (u0, 0u) where u ∈ 1{0, 1}
∗. This
means that the set {(2n, n) | n ⩾ 0} is 2-recognizable.

Note that the notion of k-automatic sequence and Theorem 3.1 have been extended
accordingly in [119, 120] where the images by a morphism of letters are d-dimensional
cubes of size k.
Extending the concept of ultimately periodic sets to subsets of N
d, with d ⩾ 2, is
at ﬁrst glance not so easy. We use bold face letters to represent elements in N
d. For
instance, one could take the following deﬁnition of a (purely) periodic subset X ⊆ N
d.

906 F. Durand, M. Rigo
(0
0) (1
1)

(1
0)

(0
1)
 (1
0)

Figure 3. A DFA recognizing {(2n, n) | n ⩾ 0}.

There exists a non-zero element p ∈ N
d such that x ∈ X if and only if x + p ∈ X. As we
will see (Remark 4.2, Proposition 6.9 and Theorem 6.11), it turns out that this deﬁnition
is not compatible with the extension of Cobham’s theorem in d dimensions. Therefore
we will consider sets deﬁnable in ⟨N, +⟩. Let us mention Nivat’s conjecture connecting
such a notion of periodicity in higher dimensions with the notion of block complexity as
introduced in Remark 3.5: let X ⊂ Z2. If there exist positive integers n1, n2 such that
pX (n1, n2) ⩽ n1n2, then X is periodic, where pX (n1, n2) counts the number of distinct
blocks of size n1 × n2 occurring in X. See [98] and, in particular, [109] for details and
pointers to the existing bibliography. The reference [53] establishes a connection with the
next section.
 4.2 Logic and k-deﬁnable sets

The formalism of ﬁrst-order logic is probably the best suited to present a natural exten-
sion (in the sense of Cobham’s theorem) of the deﬁnition of ultimately periodic sets in d
dimensions. See [107, 108] or the survey [16]. For a textbook presentation, see [114].
In Presburger arithmetic ⟨N, +⟩, the variables range over N and we have at our disposal
the connectives ∧, ∨, ¬, →, ↔, the equality symbol = and the quantiﬁers ∀ and ∃ that can
only be applied to variables. This is the reason we speak of ﬁrst-order logic; in second-
order logic, quantiﬁers can be applied to relations, and in monadic second-order logic,
only variables and unary relations, i.e., sets, may be quantiﬁed. If a variable is not within
the scope of any quantiﬁer, then this variable is said to be free. Formulas are built induc-
tively from terms and atomic formulas. Here details have been omitted; see, for instance
[29, 28, Section 3.1]. For example, order relations <, ⩽, ⩾ and > can be added to the
language by noticing that x ⩽ y is equivalent to

(∃z)(y = x + z). (4.1)

In the same way, constants can also be added. For instance, x = 0 is equivalent to
(∀y)(x ⩽ y) and x = 1 is equivalent to ¬(x = 0) ∧ (∀y)(¬(y = 0) → (x ⩽ y)). In
general, the successor function S(x) = y of x is deﬁned by

(x < y) ∧ (∀z)((x < z) → (y ⩽ z)) .

For a complete account on the interactions between ﬁrst-order logic and k-recognizable
sets, see the excellent survey [29, 28].

On Cobham’s theorem 907

Remark 4.1. We mainly discuss the case ⟨N, +⟩, but similar results are obtained for
⟨Z, +, ⩽⟩. Note that if the variables belong to Z, then it is no longer possible to deﬁne ⩽
as in (4.1). So this order relation has to be added to the structure. The constant 0 can be
deﬁned by x + x = x.

Let ϕ(x1, . . . , xd) be a formula with d free variables x1, . . . , xd. Interpreting ϕ in
⟨N, +⟩ permits one to deﬁne the set of d-tuples of non-negative integers for which the
formulas hold: {(r1, . . . , rd) | ⟨N, +⟩ |= ϕ[r1, . . . , rd]}.

We write ⟨N, +⟩ |= ϕ[r1, . . . , rd] whenever ϕ(x1, . . . , xd) is satisﬁed in ⟨N, +⟩ when
interpreting xi by ri for all i ∈ {1, . . . , d}. For the reader having no background in logic
and model theory, the ﬁrst chapters of [54] are worth reading.

Remark 4.2. The ultimately periodic sets of N are exactly the sets that are deﬁnable
in Presburger arithmetic. It is obvious that ultimately periodic sets of N are deﬁnable.
For instance, the set of even integers can be deﬁned by ϕ(x) ≡ (∃y)(x = y + y). Since
constants can easily be deﬁned, it is easy to write a formula for any arithmetic progression.
As an example, the formula ϕ(x) ≡ (∃y)(x = S(S(y + y + y))) deﬁnes the progression
3N + 2. In particular, multiplication by a ﬁxed constant is deﬁnable in ⟨N, +⟩. Note that
it is a classical result that the theory of ⟨N, +, ×⟩ is undecidable; see, for instance [15].

Adding congruences modulo any integer m permits quantiﬁer elimination, which
means that any formula expressed in Presburger arithmetic is equivalent to a formula
using only ∧, ∨, =, < and congruences; see [107, 108]. Presentations can also be found
in [56, 85].

Theorem 4.3 (Presburger). The structure ⟨N, +, <, (≡m)m>0⟩ admits elimination of
quantiﬁers.

This result can be used to prove that the theory of ⟨N, +⟩ is decidable. This can be
done using the formalism of automata; see, for instance [29, 28].

Corollary 4.4. Any formula ϕ(x) in Presburger arithmetic ⟨N, +⟩ deﬁnes an ultimately
periodic set of N.

Let k ⩾ 2. We add to the structure ⟨N, +⟩ a function Vk deﬁned by Vk(0) = 1
and for all x > 0, Vk(x) is the greatest power of k dividing x. As an example, we
have V2(6) = 2, V2(20) = 4 and V2(2
n) = 2
n for all n ⩾ 0. Again the theory of
⟨N, +, Vk⟩ can be shown to be decidable [29, 28]. The next result shows that, as for the
k-automatic sequences, the logical framework within the richer structure ⟨N, +, Vk⟩ gives
an equivalent presentation of the k-recognizable sets in any dimension. Proofs of the
next three theorems can again be found in [29, 28], where a full account of the different
approaches used to prove Theorem 4.5 is presented. For B¨uchi’s original paper; see [30].

Theorem 4.5 (B¨uchi theorem). Let k ⩾ 2 and d ⩾ 1. A set X ⊆ N
d is k-recognizable if
and only if it can be deﬁned by a ﬁrst-order formula ϕ(x1, . . . , xd) of ⟨N, +, Vk⟩.

908 F. Durand, M. Rigo

For instance, the set P2 introduced in Example 2.2 can be deﬁned by the formula
ϕ(x) ≡ V2(x) = x. Note that Theorem 4.5 holds for Pisot numeration systems given in
Deﬁnition 2.3; see [27] where the function Vk is modiﬁed accordingly. This is partially
based on the fact that in a Pisot numeration system the normalization function is realized
by a ﬁnite automaton (see [62]), which allows one to consider addition of integers: ﬁrst
perform addition digit-wise without any carry, then normalize the result.

Theorem 4.6 (Cobham’s theorem, version 3). Let k, ℓ ⩾ 2 be two multiplicatively in-
dependent integers. A set X ⊆ N can be deﬁned by a ﬁrst-order formula in ⟨N, +, Vk⟩
and by a ﬁrst-order formula in ⟨N, +, Vℓ⟩ if and only if it can be deﬁned by a ﬁrst-order
formula in ⟨N, +⟩.

This theorem still holds in higher dimensions, and is called the Cobham–Semenov
theorem. In this respect, the notion of subset of N
d deﬁnable in Presburger arithmetic
⟨N, +⟩ is the right extension of periodicity in a multidimensional setting. For Semenov’s
original paper; see [121].

Theorem 4.7 (Cobham–Semenov theorem). Let k, ℓ ⩾ 2 be two multiplicatively inde-
pendent integers. A set X ⊆ N
d can be deﬁned by a ﬁrst-order formula in ⟨N, +, Vk⟩
and by a ﬁrst-order formula in ⟨N, +, Vℓ⟩ if and only if it can be deﬁned by a ﬁrst-order
formula in ⟨N, +⟩.

Subsets of N
d deﬁned by a ﬁrst-order formula in ⟨N, +⟩ are characterized in [65]. The
nice criterion of Muchnik appeared ﬁrst in 1991 and is given in [97]. See Proposition 6.9
for its precise statement. Using this latter characterization, a proof of Theorem 4.7 is
presented in [29, 28]. The logical framework has given rise to several works. Let us
mention chronologically [126, 127] and [93, 94]. In [94, Section 5] the authors interest-
ingly show how to reduce Semenov’s theorem to Cobham’s theorem: “Nothing new in
higher dimensions”. Also extensions to non-standard numeration systems are considered
in [105] and [15]. In this latter paper, the Cobham–Semenov theorem is proved for two
Pisot numeration systems.

5 Numeration systems and substitutions

5.1 Substitutive sets and abstract numeration systems

In Sections 4.1 and 4.2, we have mainly extended the notion of recognizability to subsets
of N
d. Now we consider another extension of recognizability. In Corollary 3.3, we have
seen that a k-recognizable set has a characteristic sequence generated by a uniform sub-
stitution and the application of an extra coding. It is rather easy to deﬁne sets of integers
encoded by a characteristic sequence generated by an arbitrary substitution and an extra
coding; that is, those for which the characteristic sequence is morphic. This generaliza-
tion permits one to obtain a larger class of inﬁnite words, and hence a larger class of sets
of integers.
 On Cobham’s theorem 909

Example 5.1. Consider the morphism σ : {a, b, c}
∗ → {a, b, c}
∗ given by σ(a) = abcc,
σ(b) = bcc, σ(c) = c and the coding τ : a, b ↦→ 1, c ↦→ 0. We get

σ∞(a) = abccbccccbccccccbccccccccbccccccccccbcc · · ·

and τ (σ∞(a)) = 010010000100000010000000010000000000100 · · · . Using the special
form of the images by σ of b and c, it is not difﬁcult to see that the difference between
the position of the nth and (n + 1)st b in σ∞(a) is 2n + 1. Hence τ (σ∞(a)) is the
characteristic sequence of the set of squares and it is substitutive. From Corollary 2.9 the
set of squares is never k-recognizable for any integer base k.

Deﬁnition 5.1. As a natural extension of the concept of recognizability, we may consider
sets X ⊆ N having a characteristic sequence1X which is (purely) substitutive. Such a set
is said to be a (purely) substitutive set. In particular, k-recognizable sets are substitutive.

With Theorem 5.2 it will turn out that the formalism of substitutive sets is equivalent
to the one of abstract numeration systems.

Deﬁnition 5.2. [86] An abstract numeration system (or ANS) is a triple S = (L, A, <)
where L is an inﬁnite regular language over a totally ordered alphabet (A, <). The map
repS : N → L is the one-to-one correspondence mapping n ∈ N onto the (n + 1)th
word in the genealogically ordered language L, which is called the S-representation of
n. In particular, a set X ⊆ N is S-recognizable if repS (X) is regular, and N is trivially
S-recognizable because repS(N) = L. Recall that in the genealogical order (also called
radix or military order), words are ﬁrst ordered by increasing length and for words of the
same length, one uses the lexicographic ordering induced by the order < on A.

Example 5.2. Consider the language L = a∗b∗ ∪ a∗c∗ with a < b < c. The ﬁrst few
words in L are ε, a, b, c, aa, ab, ac, bb, cc, aaa, aab, aac, abb, . . .. This means that for the
ANS S built on L, the integer 0 is represented by ε, the integer 1 by a, the integer 2 by
b, the integer 3 by c, the integer 4 by aa, etc. Since L contains exactly 2n + 1 words of
length n for all n ⩾ 0, we have that n
2 is represented by an for all n ⩾ 0. In particular,
the set {n
2 | n ⩾ 0} is S-recognizable because a∗ is regular. It is well known that in
a regular language L, the set of the lexicographically ﬁrst words of each length in the
genealogically ordered language L is regular; see [123].

Pisot numeration systems are special cases of ANS. Indeed, if the numeration basis
U = (Un)n⩾0 deﬁnes a Pisot numeration system, then repU (N) is regular.

Example 5.3. Consider the Fibonacci sequence and the language L = 1{0, 01}
∗ ∪ {ε}
deﬁned in Example 2.1. To get the representation of an integer n, one can either decom-
pose n using the greedy algorithm or, order the words in L genealogically and take the
(n + 1)th element.

Theorem 5.1. [86] Let S = (L, A, <) be an abstract numeration system. Any ultimately
periodic set is S-recognizable.

910 F. Durand, M. Rigo

Note that in [83], it is, in particular, proved that this latter result cannot be extended to
context-free languages. Speciﬁc cases of S-recognizable sets are discussed in P. Lecomte
and M. Rigo’s chapter in [12, Chapter 3]. We have an extension of Theorem 3.1.

Theorem 5.2. Let x = (xn)n⩾0 be an inﬁnite word over an alphabet B. This word
is substitutive if and only if there exists an abstract numeration system S = (L, A, <)
such that x is S-automatic, i.e., there exists a DFAO (Q, A, ·, {q0}, B, τ ) such that for all
n ⩾ 0, xn = τ (q0 · repS (n)).

A proof of this result is given in [112, 115] and a comprehensive treatment is given in
[12, Chapter 3]. In that context, we also obtain an extension of Corollary 3.3.

Corollary 5.3. Let x = (xn)n⩾0 be an inﬁnite substitutive word over an alphabet B.
There exists an ANS S such that for all b ∈ B, {n ⩾ 0 | xn = b} is S-recognizable.
Conversely, if a set X ⊆ N is S-recognizable, then its characteristic sequence is S-
automatic.

Corollary 5.4. A set X ⊆ N is substitutive if and only if there exists an ANS S such that
X is S-recognizable.

5.2 Cobham’s theorem for substitutive sets

In the context of substitutive sets of integers, how could a Cobham-like theorem be ex-
pressed, i.e., what is playing the role of a base? Assume that there exist two purely
substitutive inﬁnite words x ∈ A
ω and y ∈ Bω, respectively, generated by the morphisms
σ : A
∗ → A
∗ prolongable on a ∈ A and τ : B∗ → B∗ prolongable on b ∈ B, i.e.,
σ∞(a) = x and τ ∞(b) = y. Consider two codings λ : A → {0, 1} and µ : B → {0, 1}
such that λ(x) = µ(y). This situation corresponds to the case where a set (here, given by
its characteristic word) is recognizable in two a priori different numeration systems.
If A = B and τ = σm for some m ⩾ 1, then nothing particular can be said about
the inﬁnite word λ(x): iterating σ or σm from the same prolongable letter leads to the
same ﬁxed point. So we must introduce a notion analogous to the one of multiplicatively
independent bases related to the substitutions σ and λ.

Deﬁnition 5.3. Let σ : A
∗ → A
∗ be a substitution over an alphabet A. The matrix
Mσ ∈ N
A×A associated with σ is called the incidence matrix of σ and is deﬁned as
follows: for all a, b ∈ A, (Mσ)a,b = |σ(b)|a .

A square matrix M ∈ R
n×n with entries in R⩾0 is irreducible if, for all i, j, there exists
k such that (Mk)i,j > 0. A square matrix M ∈ R
n×n with entries in R⩾0 is primitive if
there exists k such that, for all i, j, we have (Mk)i,j > 0. Similarly, a substitution over
the alphabet A is irreducible (resp., primitive) if its incidence matrix is irreducible (resp.,
primitive). Otherwise stated, a substitution σ : A
∗ → A
∗ is primitive if there exists an
integer n ⩾ 1 such that, for all a ∈ A, all the letters in A appear in the image of σn(a).

On Cobham’s theorem 911

Let us denote by P the abelianisation map (or Parikh map) that maps a word w over
A = {a1, . . . , ar} to the r-tuple t(|w|a1 , . . . , |w|ar ). The matrix Mσ can be deﬁned by
its columns: Mσ = (P(σ(a1)) · · · P(σ(ar))) ,

and it satisﬁes the condition

for all w ∈ A
∗, P(σ(w)) = MσP(w) .

Remark 5.5. If a matrix M is primitive, the celebrated theorem of Perron can be used; see
standard textbooks [76] or [64, 122]. A presentation is also given in [88]. To recap some
of the key points, M has a unique dominant real eigenvalue β > 0 and there exists an
eigenvector with positive entries associated with β. Also, for all i, j, there exists ci,j such
that (Mn)i,j = ci,jβn + o(βn). For instance, primitivity of Mσ implies the existence of
the frequency of any factor occurring in any ﬁxed point of σ. Note that

if P(w) = t(p1, . . . , pr), then |w| =
 r∑

i=1 pi. (5.1)

Hence, the value |σn(aj)| is obtained by summing up the entries in the jth column of
Mn for all n ⩾ 0. If σ is primitive, then there exists some Cj such that |σn(aj)| =
Cjβn + o(βn). In particular, if σ is prolongable on a, then |σn(a)| ∼ Cβn, for some
C > 0.
In the general case of a matrix M with non-negative entries, one can use the Perron–
Frobenius theorem for each of the irreducible components of M (they correspond to the
strongly connected components of the associated graph and are also called communicat-
ing classes). Thus any non-negative matrix M has a real eigenvalue α which is greater
or equal to the modulus of any other eigenvalue. We call α the dominant eigenvalue of
M. Moreover, if we exclude the case where α = 1, then there exists a positive integer p
such that Mp has a dominant eigenvalue αp which is a Perron number; see [88, p. 369].
A Perron number is an algebraic integer α > 1 such that all its algebraic conjugates have
modulus less than α. In particular, if we replace a prolongable substitution σ such that
Mσ has a dominant eigenvalue α > 1, with a convenient power σp of σ, then we can
assume that the dominant eigenvalue of σ is a Perron number.

Deﬁnition 5.4. Let σ : A
∗ → A
∗ be a substitution prolongable on a ∈ A such that
all letters of A have an occurrence in σ∞(a). Let α > 1 be the dominant eigenvalue
of the incidence matrix of σ. Let φ : A → B∗ be a coding. We say φ(σ∞(a)) is an
α-substitutive inﬁnite word (with respect to σ). In view of Deﬁnition 5.1, this notion can
be applied to subsets of N. If, moreover, σ is primitive, then φ(σ∞(a)) is said to be a
primitive α-substitutive inﬁnite word (w.r.t. σ).

Observe that k-automatic inﬁnite words are k-substitutive inﬁnite words.

Example 5.4. Consider the substitution σ deﬁned by σ(a) = aa0a, σ(0) = 01 and
σ(1) = 10. Its dominant eigenvalue is 3. It is prolongable on a, 0 and 1. The ﬁxed point
x of σ starting with 0 is the Thue-Morse sequence (see Example 3.1). Deﬁnition 5.4 does
not imply that x is 3-substitutive because a does not appear in x. But the ﬁxed point y of
σ starting with a is 3-substitutive.

912 F. Durand, M. Rigo

Example 5.5. Consider the so-called Tribonacci word, which is the unique ﬁxed point of
σ : a ↦→ ab, b ↦→ ac, c ↦→ a. See [125, 60]. The incidence matrix of σ is

Mσ =
 

1 1 1
1 0 0
0 1 0



 .

One can check that M3 contains only positive entries. So the matrix is primitive. Let
αT ≃ 1.839 be the unique real root of the characteristic polynomial −X 3 + X 2 + X + 1
of Mσ. The Tribonacci word T = abacabaab · · · is primitive αT -substitutive. Let τ :
a ↦→ 1, b, c ↦→ 0 be a coding. The word τ (T ) is the characteristic sequence of a primitive
αT -substitutive set of integers {0, 2, 4, 6, 7, . . .}.

To explain the substitutive extension of Cobham’s theorem we need the following
deﬁnition.

Deﬁnition 5.5. Let S be a set of prolongable substitutions and x be an inﬁnite word. If
x is an α-substitutive inﬁnite word w.r.t. a substitution σ belonging to S, then x is said to
be α-substitutive with respect to S.

Let us consider the following Cobham-like statement depending on two sets S and S ′

of prolongable substitutions. It is useful to chronologically describe known results gener-
alizing Cobham’s theorem in terms of substitutions leading to the most general statement
for all substitutions.

Statement (S, S ′). Let S and S ′ be two sets of prolongable substitutions. Let α and β
be two multiplicatively independent Perron numbers. Let x ∈ A
ω where A is a ﬁnite
alphabet. Then the following are equivalent:
(1) the inﬁnite word x is both α-substitutive w.r.t. S and β-substitutive w.r.t. S ′;
(2) the inﬁnite word x is ultimately periodic.

Note that this statement excludes 1-substitutions, i.e., substitutions with a dominant
eigenvalue equal to 1, because Perron numbers are larger than 1. The case of 1-substitutive
inﬁnite words will be mentioned in Subsection 5.6. Also notice that the substitutions we
are dealing with can be erasing, i.e., at least one letter is sent onto the empty word. But
from a result in [36, 9, 75], we can assume that the substitutions are non-erasing. Note
that α and αk are multiplicatively dependent.

Proposition 5.6. [52] Let x be an α-substitutive inﬁnite word. Then there exists an integer
k ⩾ 1 such that x is αk-substitutive with respect to a non-erasing substitution.

The implication (2) ⇒ (1) in the above general statement is not difﬁcult to obtain, as
mentioned in Remark 1.3 for the uniform situation.

Proposition 5.7. [48] Let x be an inﬁnite word over a ﬁnite alphabet and α be a Perron
number. If x is periodic (resp., ultimately periodic), then x is primitive α-substitutive
(resp., α-substitutive).
 On Cobham’s theorem 913

Deﬁnition 5.6. Let σ : A
∗ → A
∗ and τ : B∗ → B∗ be two substitutions. We say that σ
projects on τ if there exists a coding φ : A → B such that

φ ◦ σ = τ ◦ φ . (5.2)

The implication (1) ⇒ (2) in Statement (S, S ′) is known in many cases described
below:
(i) When S = S ′ is the set of uniform substitutions, this is the classical theorem of
Cobham.
(ii) In [57] S. Fabre proves the statement when S is the set of uniform substitutions and
S ′ is a set of non-uniform substitutions related to some non-standard numeration
systems.
(iii) When S = S ′ is the set of primitive substitutions, the statement is proved in [45].
The proof is based on a characterization of primitive substitutive sequences using
the notion of return word [44]. A word w is a return word to u if wu ∈ L(x), u is
a preﬁx of wu and u has exactly two occurrences in wu.
(iv) When S = S ′ is the set of substitutions projecting on primitive substitutions, the
statement is proved in [46]. This result is applied to generalize (ii). Using a char-
acterization of U -recognizable sets of integers for a Bertrand numeration basis U
[58], the main result of [46] extends Cobham’s theorem for a large family of non-
standard numeration systems. This latter result includes a result obtained previously
in [15] for Pisot numeration systems.
(v) Deﬁnition 5.8 and Theorem 5.17 describe the situation where S = S ′ = Sgood
(deﬁned later). It includes all known and previously described situations for substi-
tutions.
(vi) In [50], Statement (S, S ′) is proven for the most general case that is S and S ′ are
both the set of all substitutions. The ﬁnal argument is based on a careful study of
return words for non-primitive substitutive sequences.

Example 5.6. The Tribonacci word T is purely substitutive, but is k-automatic for no
integer k ⩾ 2. Proceed by contradiction. Assume that there exists an integer k ⩾ 2 such
that T is k-automatic. Then T is both k-substitutive and primitive αT -substitutive. By
Theorem 5.17, T must be ultimately periodic, but it is not the case. The factor complexity
of T is pT (n) = 2n + 1. By the Morse–Hedlund theorem (see Remark 3.5), T is not
ultimately periodic.

Let L(x) be the set of all factors of the inﬁnite word x. In [59], the following general-
ization of Cobham’s theorem is proved.

Theorem 5.8. Let k, ℓ ⩾ 2 be two multiplicatively independent integers. Let x be a k-
automatic inﬁnite word and y be a ℓ-automatic inﬁnite word. If L(x) ⊂ L(y), then x is
ultimately periodic.

The same result is valid in the primitive case.

Theorem 5.9. [45] Let x and y be, respectively, a primitive α-substitutive inﬁnite word
and a primitive β-substitutive inﬁnite word such that L(x) = L(y). If α and β are
multiplicatively independent, then x and y are periodic.

914 F. Durand, M. Rigo

Note that under the hypothesis of Theorem 5.9, x and y are primitive substitutive
inﬁnite words. Thus L(x) = L(y) whenever L(x) ⊂ L(y). Observe that if y is the ﬁxed
point starting with a, and x the ﬁxed point starting with 0 of the substitution σ deﬁned in
Example 5.4, then L(x) ⊂ L(y), but x is not ultimately periodic.
In Sections 5.3 and 5.4 we give the main arguments to prove Statement (Sgood, Sgood).

5.3 Density, syndeticity and bounded gaps

The proofs of most of the generalizations of Cobham’s theorem are divided into two parts.
(i) Dealing with a subset X of integers, we have to prove that X is syndetic. Equiva-
lently, dealing with an inﬁnite word x, we have to prove that the letters occurring
inﬁnitely many times in x appear with bounded gaps.
(ii) In the second part, the proof of the ultimate periodicity of X or x has to be carried
out.
This section is devoted to the description of the main arguments that lead to the com-
plete treatment of (i).
In the original proof of Cobham’s theorem one of the main arguments is that as k and
ℓ are multiplicatively independent (we refer to Theorem 1.1) the set {kn/ℓm | n, m ∈ N}
is dense in [0, +∞). In the uniform case, these powers refer to the length of the iterates
of the substitutions. Indeed, suppose σ : A
∗ → A
∗ is a k-uniform substitution. Then for
every a ∈ A we have |σn(a)| = kn. Unsurprisingly, to be able to treat the non-uniform
case, it is important to know that the set
{ | σn(a) |
| τ m(b) | | n, m ∈ N
}

is dense in [0, +∞), for some a, b ∈ A. We explain below that |σn(a)| and |τ m(b)| are
governed by the dominant eigenvalue of their incidence matrices. First we focus on part
(i) and consider inﬁnite words.

5.3.1 The length of the iterates The length of the iterates are described in the follow-
ing lemma. Note that it includes erasing substitutions and substitutions with a dominant
eigenvalue equal to 1. Observe that for the substitution σ deﬁned by 0 ↦→ 001 and 1 ↦→ 11
we have |σn(0)| = (n + 2)2
n−1 and |σn(1)| = 2
n, showing that the situation is different
from the uniform case. It can easily be described using the Jordan normal form of the
incidence matrix Mσ. Discussion of the following result can be found in [12, Section
4.7.3].

Lemma 5.10 (Chapter III.7 in [118]). Let σ : A → A
∗ be a substitution. For all a ∈ A
one of the two following situations occurs

(1) there exists N ∈ N such that for all n > N , |σn(a)| = 0, or,
(2) there exist d(a) ∈ N and real numbers c(a), θ(a) such that

lim
n→+∞ |σn(a)|
c(a) nd(a) θ(a)n = 1.

On Cobham’s theorem 915

Moreover, in the case (2), for all i ∈ {0, . . . , d(a)} there exists a letter b ∈ A appear-
ing in σj(a) for some j ∈ N and such that

lim
n→+∞ |σn(b)|
c(b) ni θ(a)n = 1.

Deﬁnition 5.7. Let σ be a non-erasing substitution. For all a ∈ A, the pair (d(a), θ(a))
deﬁned in Lemma 5.10 is called the growth type of a. If (d, θ) and (e, β) are two growth
types, then we say that (d, θ) is less than (e, β) (or (d, θ) < (e, β)) whenever θ < β or,
θ = β and d < e.

Consequently, if the growth type of a ∈ A is less than the growth type of b ∈ A, then
limn→+∞ |σn(a)|/|σn(b)| = 0. We say that a ∈ A is a growing letter if (d(a), θ(a)) >
(0, 1) or equivalently, if limn→+∞ |σn(a)| = +∞.
We set Θ := max{θ(a) | a ∈ A}, D := max{d(a) | ∀a ∈ A : θ(a) = Θ} and
Amax := {a ∈ A | θ(a) = Θ, d(a) = D}. The dominant eigenvalue of Mσ is Θ. We
say that the letters of Amax are of maximal growth and that (D, Θ) is the growth type of
σ. Consequently, we say that a substitutive inﬁnite word y is (D, Θ)-substitutive if the
underlying substitution is of growth type (D, Θ). Observe that, due to Lemma 5.10, any
substitutive sequence is (D, Θ)-substitutive for some pair (D, Θ).
Observe that if Θ = 1, then in view of the last part of Lemma 5.10, there exists at least
one non-growing letter of growth type (0, 1). Otherwise stated, if a letter has polynomial
growth, then there exists at least one non-growing letter. Consequently σ is growing (i.e.,
all its letters are growing) if and only if θ(a) > 1 for all a ∈ A. We deﬁne

λσ : A
∗ → R, u0 · · · un−1 ↦→
 n−1∑

i=0 c(ui)1Amax (ui) ,

where c : A → R+ is deﬁned in Lemma 5.10. From Lemma 5.10 we deduce the following
lemma.

Lemma 5.11. For all u ∈ A
∗, we have limn→+∞ |σn(u)|/n
DΘn = λσ(u).

We say that the word u ∈ A
∗ is of maximal growth if λσ(u) ̸= 0.

Corollary 5.12. Let σ be a substitution of growth type (D, Θ). For all k ⩾ 1, the growth
type of σk is (D, Θk).

5.3.2 Letters and words appear with bounded gaps Recall that the ﬁrst step in the
proof of Cobham’s theorem is to prove that the letters occurring inﬁnitely many times
appear with bounded gaps. In our context, this implies the same property for words.
Moreover, we can relax the multiplicative independence hypothesis in order to include
1-substitutions. Note that 1 and α > 1 are multiplicatively dependent.

Theorem 5.13. [52] Let d, e ∈ N \ {0} and α, β ∈ [1, +∞) such that (d, α) ̸= (e, β)
and satisfying one of the following three conditions:
(i) α and β are multiplicatively independent;

916 F. Durand, M. Rigo

(ii) α, β > 1 and d ̸= e;
(iii) (α, β) ̸= (1, 1) and, β = 1 and e ̸= 0, or, α = 1 and d ̸= 0.
Let C be a ﬁnite alphabet. If x ∈ C ω is both (d, α)-substitutive and (e, β)-substitutive,
then the words occurring inﬁnitely many times in x appear with bounded gaps.

The main argument used to prove this in [52] is the following.

Theorem 5.14. Let d, e ∈ N and α, β ∈ [1, +∞). The set

Ω = { αnn
d

βmme | n, m ∈ N
}

is dense in [0, +∞) if and only if one of the following three conditions holds:

(i) α and β are multiplicatively independent;
(ii) α, β > 1 and d ̸= e;
(iii) β = 1 and e ̸= 0, or, α = 1 and d ̸= 0.

Sketch of the proof of Theorem 5.13. We only consider the case where α and β are multi-
plicatively independent.
Let σ : A
∗ → A
∗ be a substitution prolongable on a letter a′ having growth type
(d, α). Let τ : B∗ → B∗ be a substitution prolongable on a letter b′ having growth
type (e, β). Let φ : A → C and ψ : B → C be two codings such that φ(σ∞(a′)) =
ψ(τ ∞(b′)) = x. Using Proposition 5.6 we may assume that σ and τ are non-erasing.
Suppose there is a letter a having inﬁnitely many occurrences in x, but that appears with
unbounded gaps. Then the letters in φ−1({a}) appear with unbounded gaps. To avoid
extra technicalities (a complete treatment is considered in [52]), we assume that there is
a letter in φ−1({a}) having maximal growth. Then it is quite easy to construct for all
n ∈ N, a word wn of length c1n
dαn, appearing in y at the index c2n
dαn, that does not
contain any letter of φ−1({a}). On the other hand, using a kind of pumping lemma for
substitutions, one can show that there is a letter of ψ−1({a}) in z at the index c3n
eβn.
Therefore, using Theorem 5.14, the letter a appears in a word φ(wn) for some n. This is
not possible.
Now let us explain how to extend this result for a single letter to words. It uses what
is called in [110] the substitutions of the words of length n. Let u be a word of length n
occurring inﬁnitely often in x. To prove that u appears with bounded gaps in x, it sufﬁces
to prove that the letter 1 appears with bounded gaps in the inﬁnite word t ∈ {0, 1}
N

deﬁned by
 ti = { 1, if xi · · · xi+n−1 = u;
0, otherwise.

Let A
n be the set of words of length n over A. The inﬁnite word y(n) = (yi · · · yi+n−1)i⩾0
over the alphabet A
n is a ﬁxed point of the substitution σn : (A
n)∗ → (A
n)∗ deﬁned, for
all (a1 · · · an) in A
n, by

σn((a1 · · · an)) = (b1 · · · bn)(b2 · · · bn+1) · · · (b|σ(a1)| · · · b|σ(a1)|+n−1)

where σ(a1 · · · an) = b1 · · · bk. For details; see Section V.4 in [110].

On Cobham’s theorem 917

Let ρ : A
n → A
∗ be the coding deﬁned by ρ((b1 · · · bn)) = b1 for all (b1 · · · bn) ∈
A
n. We have ρ ◦ σn = σ ◦ ρ, and then ρ ◦ σk
n = σk ◦ ρ. Hence, if σ is of growth type
(d, α), then y(n) is (d, α)-substitutive. Let f : A
n → {0, 1} be the coding deﬁned by

f ((b1 · · · bn)) = { 1, if b1 · · · bn = u;
0, otherwise.

It is easy to see that f (y(n)) = t, and hence t is (d, α)-substitutive. Then one proceeds in
the same way with τ and uses the result for letters to conclude the proof.

5.4 Ultimate periodicity

Deﬁnition 5.8. Let σ : A
∗ → A
∗ be a substitution. If there exists a sub-alphabet B ⊆ A
such that for all b ∈ B, σ(b) ∈ B∗, then the substitution τ : B∗ → B∗ deﬁned by
the restriction τ (b) = σ(b), for all b ∈ B, is a sub-substitution of σ. Note that σ is, in
particular, a sub-substitution of itself.
The substitution σ having α as dominant eigenvalue is a “good” substitution if it has
a primitive sub-substitution whose dominant eigenvalue is α. So let us stress the fact that
to be a “good” substitution, the sub-substitution has to be primitive and have the same
dominant eigenvalue as the original substitution. We let Sgood denote the set of good
substitutions.

Remark 5.15. For all growing substitutions σ, there exists an integer k such that σk has
a primitive sub-substitution. Hence by taking a convenient power of σ, the substitution
can always be assumed to have a primitive sub-substitution.

Note that primitive substitutions and uniform substitutions are good substitutions.
Now consider the substitution σ : {a, 0, 1}
∗ → {a, 0, 1}
∗ given by σ : a ↦→ aa0, 0 ↦→
01, 1 ↦→ 0. Its dominant eigenvalue is 2 and it has only one primitive sub-substitution
(0 ↦→ 01, 1 ↦→ 0) whose dominant eigenvalue is (1 + √5)/2, and hence it is not a good
substitution.

Remark 5.16. Let σ : A
∗ → A
∗ and τ : B∗ → B∗ be two substitutions such that σ
projects on τ ; recall (5.2) for the deﬁnition of projection. There exists a coding φ : A →
B such that φ ◦ σ = τ ◦ φ. Note that φ ◦ σn = τ n ◦ φ. If τ is primitive, then it follows
that σ belongs to Sgood.

Theorem 5.17. Let α and β be two multiplicatively independent Perron numbers. Let
x ∈ A
ω where A is a ﬁnite alphabet. Then the following are equivalent:
(i) the inﬁnite word x is both α-substitutive w.r.t. Sgood and β-substitutive w.r.t. Sgood;
(ii) the inﬁnite word x is ultimately periodic.

Proof. Let σ : B∗ → B∗ (resp., τ : C ∗ → C ∗) be a substitution in Sgood having α (resp.,
β) as its dominant eigenvalue and φ (resp., ψ) be a coding such that x = φ(σ∞(b)) for
some b ∈ B (resp., x = ψ(τ ∞(c)) for some c ∈ C).
Let us ﬁrst suppose that both substitutions are growing. In this way, taking a power if
needed, we can suppose that they have primitive sub-substitutions.

918 F. Durand, M. Rigo

By Theorem 5.13, the factors occurring inﬁnitely many times in x appear with bounded
gaps. Hence for any primitive and growing sub-substitutions σ and τ of σ and of τ re-
spectively, we have φ(L(σ)) = ψ(L(τ )) = L. Using Theorem 5.9 it follows that L is
periodic, i.e., there exists a shortest word u, appearing inﬁnitely many times in x, such
that L = L(uω). Thus u appears with bounded gaps. Let Ru be the set of return words
to u. We recall that a word w is a return word to u if wu belongs to L(x), u is a preﬁx of
wu and u has exactly two occurrences in wu. Since u appears with bounded gaps, the set
Ru is ﬁnite. There exists an integer N such that all words wu ∈ L(xN xN +1 · · · ) appear
inﬁnitely many times in x for all w ∈ Ru. Hence these words appear with bounded gaps
in x. We set t = xN xN +1 · · · and we will prove that t is periodic. Consequently x would
be ultimately periodic. We can suppose that u is a preﬁx of t. Then t is a concatenation
of return words to u. Let w be a return word to u. It appears with bounded gaps; hence it
appears in some φ(σn(a)), where σ is a primitive and growing sub-substitution, and there
exist two words, p and q, and an integer i such that wu = puiq. As |u| is the least period
of L, it must be that wu = ui. It follows that t = uω.
If, for example, σ is non-growing, then a result of J.-J. Pansiot [100] asserts that either
by modifying σ and φ in a suitable way (in that case α could be replaced by a power
of α) we can suppose σ is growing or L(σ∞(b)) contains the language of a periodic
inﬁnite word. We have treated the ﬁrst case before. For the second case it sufﬁces to use
Theorem 5.13.

Suppose α and β are multiplicatively independent real numbers and that x is a α-
substitutive inﬁnite word w.r.t. Sgood and y is a β-substitutive inﬁnite word w.r.t. Sgood
satisfying L(x) ⊂ L(y). Then the conclusion of Theorem 5.8 is far from true. It sufﬁces
to look at Example 5.4 and the observation made after Theorem 5.9.

Remark 5.18. The Statement (S, S ′) remains open when S is the set of substitutions
which are not good. Nevertheless there are cases where we can say more. For example, if
x is both α-substitutive and β-substitutive (with α and β being multiplicatively indepen-
dent), and, L(x) contains the language of a periodic sequence, then, from Theorem 5.13,
we deduce that x is ultimately periodic.
Moreover, as we will see in the next section, this statement holds in the purely substi-
tutive context.
 5.5 The case of ﬁxed points

Now let restrict ourselves to the purely substitutive case. In this setting Cobham’s theorem
holds. Note that in the statement of the following result, α and β are necessarily Perron
numbers. Moreover, since the substitutions are growing, then α and β must be larger than
one.

Theorem 5.19. Let σ : A
∗ → A
∗ and τ : A
∗ → A
∗ be two non-erasing growing sub-
stitutions prolongable on a ∈ A with respective dominant eigenvalues α and β. Suppose
that all letters of A appear in σ∞(a) and in τ ∞(a) and that α and β are multiplicatively
independent. If x = σ∞(a) = τ ∞(a), then x is ultimately periodic.

On Cobham’s theorem 919

Proof. Thanks to Remark 5.15, we may assume that σ has a primitive sub-substitution.
Using Theorem 5.13, the letters appearing inﬁnitely often in x appear with bounded gaps.
Let σ : A → A be a primitive sub-substitution of σ. Let c ∈ A. Suppose that there exists
a letter b, appearing inﬁnitely many times in x, which does not belong to A. Then the
word σn(c) = σn(c) does not contain b and b could not appear with bounded gaps. Con-
sequently all letters (and, in particular, a letter of maximal growth) appearing inﬁnitely
often in x belong to A. Hence σ also has α as dominant eigenvalue and σ is a “good”
substitution. In the same way τ is a “good” substitution. Theorem 5.17 concludes the
proof.
 5.6 Back to numeration systems

Let S be an abstract numeration system. There is no reason for the substitutions describ-
ing characteristic words of S-recognizable sets (see Corollary 5.4) to be primitive. To
obtain a Cobham-type theorem for families of abstract numeration systems, one has to
interpret Theorem 5.17 in this formalism.

5.6.1 Polynomially-growing abstract numeration systems Here we only mention the
following result. The paper [42] is also of interest. It is well-known that the growth func-
tion counting the number of words of length n in a regular language is either polynomial,
i.e., in O(n
k) for some integer k or exponential, i.e., in Ω(θn) for some θ > 1.

Proposition 5.20. [52] Let S = (L, A, <) (resp., T = (M, B, ≺)) be an abstract nu-
meration system where L is a polynomial regular language (resp., M is an exponential
regular language). A set X of integers is both S-recognizable and T -recognizable if and
only if X is ultimately periodic.

5.6.2 Bertrand basis and ωα-substitutive words Let U be a Bertrand numeration basis
such that repU (N) = L(α) where α is a Parry number which is not an integer. In [58]
a substitution denoted by ωα is deﬁned. The importance of this substitution is justiﬁed
by Theorem 5.21. If dα(1) = t1 · · · tn0
ω, tn ̸= 0, then ωα is deﬁned on the alphabet
{1, . . . , n} by 1 ↦→ 1
t1 2, . . . , n − 1 ↦→ 1
tn−1n, n ↦→ 1
tn .

If dα(1) = t1 · · · tn(tn+1tn+2 · · · tn+m)ω, where n and m are minimal and where tn+1 +
tn+2 + · · · + tn+m ̸= 0, then ωα is deﬁned on the alphabet {1, · · · , n + m} by

1 ↦→ 1
t1 2, . . . , n + m − 1 ↦→ 1
tn+m−1(n + m), n + m ↦→ 1
tn+m(n + 1) .

In both cases the substitution ωα is primitive and has α as dominant eigenvalue. A sub-
stitution that projects (see Deﬁnition 5.6) on ωα is called a ωα-substitution, and we call
each inﬁnite word which is the image under a coding of a ﬁxed point of a ωα-substitution
a ωα-substitutive inﬁnite word (α-automatic inﬁnite word in [58]).

Theorem 5.21. [58, Corollary 1] Let U be a Bertrand numeration basis such that
repU (N) = L(α) where α is a Parry number. A set X ⊂ N is U -recognizable if and
only if its characteristic sequence1X is ωα-substitutive.

920 F. Durand, M. Rigo

Remark 5.16 and Theorem 5.17 imply the following result.

Theorem 5.22. [46] Let U and V be two Bertrand numeration systems. Let α and
β be two multiplicatively independent Parry numbers such that repU (N) = L(α) and
repV (N) = L(β). A set X ⊆ N is U -recognizable and V -recognizable if and only if X
is ultimately periodic.

6 Cobham’s theorem in various contexts

6.1 Regular sequences

Regular sequences as presented in [6, 7, 9] are a generalization of automatic sequences to
sequences taking inﬁnitely many values. Many examples of such sequences are given in
the ﬁrst two references. Also see [43] for a generalization of the notion of automaticity
in the framework of group actions. Let R be a commutative ring. Let k ⩾ 2. Consider a
sequence x = (xn)n⩾0 taking values in some R-module. If the R-module generated by
all sequences in the k-kernel Nk(x) is ﬁnitely generated (recall Theorem 3.2), then the
sequence x is said to be (R, k)-regular.

Theorem 6.1 (Cobham–Bell theorem [10]). Let R be a commutative ring
3. Let k, ℓ be
two multiplicatively independent integers. If a sequence x ∈ RN is both (R, k)-regular
and (R, ℓ)-regular, then it satisﬁes a linear recurrence over R.

6.2 Algebraic setting and quasi-automatic functions

In [34] G. Christol characterized p-recognizable sets in terms of formal power series.

Theorem 6.2. Let p be a prime number and Fp be the ﬁeld with p elements. A subset
A ⊂ N is p-recognizable if and only if f (X) = ∑n∈A X n ∈ Fp[[X]] is algebraic over
Fp(X).

This was applied to Cobham’s theorem in [35] to obtain an algebraic version.

Theorem 6.3. Let A be a ﬁnite alphabet, x ∈ A
N, and, K1 and K2 be two ﬁnite ﬁelds
with different characteristics. Let α1 : A → K1 and α2 : A → K2 be two one-to-one
maps. If f (X) = ∑n∈N α1(xn)X n ∈ K1[[X]] is algebraic over K1(X) and f (X) =∑n∈N α2(xn)X n ∈ K2[[X]] is algebraic over K2(X), then f (X) is rational.

Quasi-automatic functions were introduced by Kedlaya in [78]. Also see [79], where
Christol’s theorem is generalized to Hahn’s generalized power series. In this algebraic
setting, an extension of Cobham’s theorem is proved by Adamczewski and Bell in [1].
Details are given in the chapter “Automata in number theory” of this handbook.

3Note that in [6] the ground ring R is assumed to be Noetherian (every ideal in R is ﬁnitely generated), but
this extra assumption is not needed in the above statement.

On Cobham’s theorem 921

6.3 Real numbers and veriﬁcation of inﬁnite-state systems

Sets of numbers recognized by ﬁnite automata arise when analyzing systems with un-
bounded mixed variables taking integer or real values. Therefore systems such as timed
or hybrid automata are considered [17]. One needs to develop data structures representing
sets manipulated during the exploration of inﬁnite state systems. For instance, it is often
needed to compute the set of reachable conﬁgurations of such a system. Let k ⩾ 2 be an
integer. Considering separately integer and fractional parts, a real number x > 0 can be
decomposed as
 x =
 d∑

i=0 ci ki +
 +∞∑

i=1 c−i k−i, ci ∈ [[0, k − 1]], i ⩽ d, (6.1)

and gives rise to the inﬁnite word cd · · · c0 ⋆ c−1c−2 · · · over [[0, k − 1]] ∪ {⋆}, which is
a k-ary representation of x. Note that rational numbers of the form p/kn have two k-ary
representations, one ending with 0
ω and one with (k − 1)ω. For the representation of
negative elements, one can consider base k-complements or signed number representa-
tions [81], the sign being determined by the most signiﬁcant digit which is thus 0 or k − 1
(and this digit may be repeated an arbitrary number of times). For deﬁnition of B¨uchi and
Muller automata, see the ﬁrst part of this handbook.

Deﬁnition 6.1. A set X ⊆ R is k-recognizable if there exists a B¨uchi automaton accept-
ing all the k-ary representations of the elements in X. Such an automaton is called a Real
Number Automaton or RNA.

These notions extend naturally to subsets of R
d and to Real Vector Automata or RVA.
Also the B¨uchi theorem 4.5 holds for a suitable structure ⟨R, Z, +, <, Vk⟩; see [22].

Theorem 6.4. [21] If X ⊆ R
d is deﬁnable by a ﬁrst-order formula in ⟨R, Z, +, <⟩, then
X written in base k ⩾ 2 is accepted by a weak deterministic RVA A.

Weakness means that each strongly connected component of A contains only accept-
ing states or only non-accepting states.

Theorem 6.5. [18] Let k, ℓ ⩾ 2 be two multiplicatively independent integers. If X ⊆
R is both k- and ℓ-recognizable by two weak deterministic RVA, then it is deﬁnable in
⟨R, Z, +, <⟩.

The extension of the Cobham–Semenov theorem for subsets of R
d in this setting is
discussed in [20]; also see [24] for a comprehensive presentation. The case of two coprime
bases was ﬁrst considered in [18]. Surprisingly, if the multiplicatively independent bases
k, ℓ ⩾ 2 share the same prime factors, then there exists a subset of R that is both k- and ℓ-
recognizable, but not deﬁnable in ⟨R, Z, +, <⟩; see [19]. This shows the main difference
between recognizability of subsets of real numbers written in base k for (general) B¨uchi
automata and weak deterministic RVA. Though written in a completely different language,
a similar result was independently obtained in [2]. This latter paper is motivated by the
study of some fractal sets. For extension to non-integer bases and graph directed iterated
systems; see [32].

922 F. Durand, M. Rigo

6.4 Dynamical systems and subshifts

In this section we would like to express a Cobham-type theorem in terms of dynamical
systems called substitutive subshifts. Theorem 5.9 will appear as a direct corollary.
We ﬁrst need some deﬁnitions.
A dynamical system is a pair (X, S) where X is a compact metric space and S a
continuous map from X onto itself. The dynamical system (X, S) is minimal whenever
X and the empty set are the only S-invariant closed subsets of X, that is, S(X) = X.
We say that a minimal system (X, S) is periodic whenever X is ﬁnite.
Let (X, S) and (Y, T ) be two dynamical systems. We say that (Y, T ) is a factor of
(X, S), or that (X, S) factorizes to (Y, S), if there is a continuous and onto map φ : X →
Y such that φ ◦ S = T ◦ φ (φ is called a factor map). If φ is one-to-one we say that φ is
an isomorphism and that (X, S) and (Y, T ) are isomorphic.
Let A be an alphabet. We endow A
ω with the inﬁnite product of the discrete topolo-
gies. It is a metric space where the metric is given by

d(x, y) = 1
2n with n = inf{k | xk ̸= yk}, (6.2)

where x = (xn)n⩾0 and y = (yn)n⩾0 are two elements of A
ω. A subshift on A is a pair
(X, T|X ) where X is a closed T -invariant subset of A
ω and T is the shift transformation
T : A
ω → A
ω, (xn)n⩾0 ↦→ (xn+1)n⩾0.
Let u be a word over A. The set [u]X = {x ∈ X | x0 · · · x|u|−1 = u} is a cylinder.
The family of these sets is a base of the induced topology on X. When there is no
misunderstanding, we write [u] and T instead of [u]X and T|X .
Let x ∈ A
ω. The set {y ∈ A
ω | L(y) ⊆ L(x)} is denoted Ω(x). It is clear that
(Ω(x), T ) is a subshift. We say that (Ω(x), T ) is the subshift generated by x. When x is
a sequence, we have Ω(x) = {T nx | n ∈ N}. Observe that (Ω(x), T ) is minimal if and
only if x is uniformly recurrent, i.e., all its factors occur inﬁnitely often in x and for each
factor u of x, there exists a constant K such that the distance between two consecutive
occurrences of u in x is bounded by K.
Let φ be a factor map from the subshift (X, T ) on the alphabet A onto the subshift
(Y, T ) on the alphabet B. Here x[i,j] denotes the word xi · · · xj, i ⩽ j. The Curtis–
Hedlund–Lyndon theorem [88, Thm. 6.2.9] asserts that φ is a sliding block code: there
exists an r-block map f : A
r → B such that (φ(x))i = f (x[i,i+r−1]) for all i ∈ N and
x ∈ X. We shall say that f is a block map associated to φ and that f deﬁnes φ. If u =
u0u1 · · · un−1 is a word of length n ⩾ r, then we deﬁne f (u) by (f (u))i = f (u[i,i+r−1]),
i ∈ {0, 1, · · · , n − r + 1}. Let C denote the alphabet A
r and Z = {(x[i,r+i−1])i⩾0 |
(xn)n⩾0 ∈ X}. It is easy to check that the subshift (Z, T ) is isomorphic to (X, T ) and
that f induces a 1-block map (a coding) from C onto B which deﬁnes a factor map from
(Z, T ) onto (Y, T ).
We can now state a Cobham-type theorem for subshifts generated by substitutive se-
quences. Observe that it implies Theorem 5.9 and Statement (S, S ′) when S = S ′ is the
set of primitive substitutions.

Theorem 6.6. Let (X, T ) and (Y, T ) be two subshifts generated, respectively, by a prim-
itive α-substitutive sequence x and by a primitive β-substitutive sequence y. Suppose
(X, T ) and (Y, T ) both factorize to the subshift (Z, T ). If α and β are multiplicatively

On Cobham’s theorem 923

independent, then (Z, T ) is periodic.

Below we give a sketch of the proof, which involves the concept of an ergodic mea-
sure. An invariant measure for the dynamical system (X, S) is a probability measure
µ, on the σ-algebra B(X) of Borel sets, with µ(S−1B) = µ(B) for all B ∈ B(X);
the measure is ergodic if every S-invariant Borel set has measure 0 or 1. The set of
invariant measures for (X, S) is denoted by M(X, S). The system (X, S) is uniquely
ergodic if #(M(X, S)) = 1. For expository books on subshifts and/or ergodic theory,
see [39, 80, 88, 110, 84].
It is well known that the subshifts generated by primitive substitutive sequences are
uniquely ergodic [110].
Let φ : X → Z and ψ : Y → Z be two factor maps. Suppose that (Z, T ) is not
periodic. We will prove that α and β are multiplicatively independent.
Let µ and λ be the unique ergodic measures of (X, T ) and (Y, T ) respectively. It
is not difﬁcult to see that (Z, T ) is also generated by a primitive substitutive sequence
and consequently is uniquely ergodic. Let δ be its unique ergodic measure. We notice
that φµ deﬁned by φµ(A) = µ(φ−1(A)), for all Borel sets A of Z, and ψλ deﬁned by
ψλ(A) = µ(ψ−1(A)), for all Borel sets A of Z, are invariant measures for (Z, T ). Hence
φµ = δ = ψλ. Let us give more details about both measures in order to conclude the
proof.

Theorem 6.7. [73] Let (Ω, T ) be a subshift generated by a primitive purely γ-substitutive
sequence and m be its unique ergodic measure. Then, the measures of cylinders in Ω lie
in a ﬁnite union of geometric progressions. There exists a ﬁnite set F of positive real
numbers such that {m(C) | C cylinder of X} ⊂ ⋃

n∈N γ−nF .

In conjunction with the next result and using the pigeonhole principle we will conclude
the proof.

Proposition 6.8. [47] Let (Ω, T ) be a subshift generated by a primitive substitutive se-
quence on the alphabet A. There exists a constant K such that for any block map
f : A
2r+1 → B, we have #(f −1({u})) ⩽ K for all u appearing in some sequence
of f (Ω).

From these last two results we deduce that there exist two sets of numbers FX and
FY such that

{δ(C) | C cylinder of Z} ={µ(φ−1(C)) | C cylinder of Z}

={λ(ψ−1(C)) | C cylinder of X}

⊂
 ( ⋃

n∈N α−nFX
 ) ⋂ ( ⋃

n∈N β−nFY
 )
 .

The sets FX and FY being ﬁnite, there exist two cylinder sets U and V of Z, a ∈ FX ,
b ∈ FY and n, m, r, s four distinct positive integers, such that

aα−n = δ(U ) = bβ−m and aα−r = δ(V ) = bβ−s .

924 F. Durand, M. Rigo

Consequently α and β are multiplicatively dependent.

6.5 Tilings

6.5.1 From deﬁnable sets Let A be a ﬁnite alphabet. An array in N
d is a map T :
N
d → A. It can be viewed as a tiling of R
d
+. The collection of all these arrays is A
Nd .
For all x ∈ N
d, let |x| denote the sum of the coordinates of x and B(x, r) be the set
{(y1, . . . , yd) ∈ N
d | 0 ⩽ yi − xi < r, 1 ⩽ i ⩽ d}.
We say T is periodic (resp., ultimately periodic) if there exists p ∈ N
d such that
T (x + p) = T (x) for all x ∈ N
d (resp., for all large enough x). We also need another
notion of periodicity. We say that Z ⊂ N
d is p-periodic inside X ⊂ N
d if for any x ∈ X
with x + p ∈ X we have
 x ∈ Z if and only if x + p ∈ Z .

We say that Z is locally periodic if there exists a non-empty ﬁnite set V ⊂ N
d of non-zero
vectors such that for some K > max{|v| | v ∈ V } and L ⩾ 0 one has

(∀x ∈ N
d, |x| ⩾ L)(∃v ∈ V )(Z is v-periodic inside B(x, K)) .

Observe that for d = 1, local periodicity is equivalent to ultimate periodicity. We
say T is pseudo-periodic if for all a ∈ A, T −1(a) is locally periodic and every (d − 1)-
section of T −1(a), say S(i, n) = {x ∈ T −1(a) | xi = n}, 1 ⩽ i ⩽ d and n ∈ N, is
pseudo-periodic (ultimately periodic when d − 1 = 1). The following criterion is due to
Muchnik; see [97] for the proof.

Proposition 6.9. Let E ⊂ N
d and T : N
d → {0, 1} be its characteristic function. The
following are equivalent:
(i) E is deﬁnable in Presburger arithmetic;
(ii) T is pseudo-periodic;
(iii) for all a ∈ {0, 1}, there exist n ∈ N, vi ∈ N
d and ﬁnite sets Vi ⊂ N
d, 0 ⩽ i ⩽ n
such that
 T −1(a) = V0 ∪
 

 ⋃

1⩽i⩽n
 (
vi + ∑

v∈Vi Nv
)

 .

Let p be a positive integer and A be a ﬁnite alphabet. A p-substitution (or substitu-
tion if we do not need to specify p) is a map S : A → A
Bp where Bp = B(0, p) =
Π
d=1{0, · · · , p − 1}. The substitution S can be considered as a function from A
Nd into
itself by setting S((T (x)) = [S(T (y))](z), for all T ∈ A
Nd

where y ∈ N
d and z ∈ Bp are the unique vectors satisfying x = py + z.
In the same way, we can deﬁne S : A
Bpn → A
Bpn+1 . We remark that Sn(a) =
S(Sn−1(a)) for all a ∈ A and n > 0. We say T is generated by a p-substitution if there
exist a coding φ and a ﬁxed point T0 of a p-substitution such that T = φ ◦ T0.
In [31] the authors proved the following theorem, which is analogous to Theorem 3.1.

On Cobham’s theorem 925

Theorem 6.10. Let p ⩾ 2 and d ⩾ 1. A set E ⊂ N
d is p-recognizable if and only if the
characteristic function of E is generated by a p-substitution.

Hence we can reformulate the Cobham–Semenov theorem as follows [121].

Theorem 6.11 (Cobham–Semenov theorem, Version 2). Let p and q be two multiplica-
tively independent integers greater or equal to 2. Then the array T is generated by both
a p-substitution and a q-substitution if and only if T is pseudo-periodic.

A dynamical proof of this can be given as for the unidimensional case; see [49] for the
primitive case.

6.5.2 Self-similar tilings In [40], a Cobham-like theorem is expressed in terms of self-
similar tilings of R
d with a proof using ergodic measures; see [124] for more about self-
similar tilings. From the point of view of dynamical systems, the main result in [99] is
also a Cobham-like theorem for self-similar tilings.

6.6 Toward Cobham’s theorem for the Gaussian integers

I. K´atai and J. Szab´o proved [77] that the sequences ((−p + i)n)n⩾0 and ((−p − i)n)n⩾0
give rise to numeration systems whose set of digits is {0, 1, . . . , p2}, p ∈ N \ {0}. It is
an exercise to check that when p ∈ N \ {0} and q ∈ N \ {0} are different then −p + i
and −q + i are multiplicatively independent. Therefore one could expect a Cobham-type
theorem for the set of Gaussian integers G = {a + ib | a, b ∈ Z}. A subset S ⊂ G is
periodic if there exists h ∈ G such that, for all g ∈ G, s ∈ S if and only if s + gh ∈ S.
G. Hansel and T. Safer conjectured the following [69]:

Conjecture 6.12. Let p and q be two different positive integers and S ∈ G. Then the
following are equivalent.
(i) The set S is (−p + i)-recognizable and (−q + i)-recognizable;
(ii) There exists a periodic set P such that the symmetric difference set S∆P is ﬁnite.

The proof that (ii) implies (i) is easy. They tried to prove the other implication using
the following (classical) steps:

(1) Dp,q = { (−p+i)n

(−q+i)m | n, m ∈ Z} is dense in C.
(2) S is syndetic
(3) S is periodic up to some ﬁnite set.

They succeeded in proving (ii) as given by the next result.

Theorem 6.13. Let p and q be two positive integers such that the set Dp,q is dense in C.
Let S ⊂ G be (−p + i)-recognizable and (−q + i)-recognizable. Then, S is syndetic.

Let us make some observations about the density of the set Dp,q. Let −p + i = aeiθ

and −q + i = beiφ.

926 F. Durand, M. Rigo

Proposition 6.14. The following are equivalent.
(i) The set Dp,q is dense in C;
(ii) The set Dp,q is dense on the circle: {eiθ | θ ∈ R} ⊂ Dp,q;
(iii) The following numbers are rationally independent (or linearly dependent over Q):

ln b
ln a , θ
2π ln b
ln a − φ
2π , 1 .

The equivalence between (i) and (iii) is proven in [69] from an easy computation.
The equivalence between (i) and (ii) comes from the fact that p2 + 1 and q2 + 1 are
multiplicatively independent; see [69, Prop. 2]. As an example, take p = 1 and p = 2.
Then, a = √2, b = √5, θ = 3π
4 and φ = arctan(− 1
2 ). Proving the density of D1,2
is equivalent to proving that ln 5/ ln 2 , arctan(1/2)/π and 1 are rationally independent.
In [69] the authors observe that the four exponentials conjecture (see [128]) would imply
that Dp,q is dense in C.

Conjecture 6.15 (“four exponentials conjecture”). Let {λ1, λ2} and {x1, x2} be two
pairs of rationally independent complex numbers. Then, one of the numbers eλ1x1 , eλ1x2,
eλ2x1 , eλ2x2 is transcendental.

6.7 Recognizability over Fq[X]

Using the analogy existing between Z and the ring of polynomials over a ﬁnite ﬁeld Fq
of positive characteristic, one can easily deﬁne B-recognizable sets of polynomials [113].
In [129, 106] characterization of these sets in a convenient logical structure analogous to
Theorem 4.5 is given. A family of sets of polynomials recognizable in all polynomial
bases is described in [113, 129]. Again, we can conjecture a Cobham-like theorem.

7 Decidability issues

So far we have seen that ultimately periodic sets have a very special status in the context
of numeration systems (recall Proposition 2.6, Theorem 5.1 or Theorems 5.17 and 5.19).
They can be described using a ﬁnite amount of data (two ﬁnite words for the preperiodic
and the periodic parts). Let us settle down once more to the usual integer base numera-
tion system. Let X ⊆ N be a k-recognizable set of integers given by a DFA accepting
repk(X). Is there an algorithmic decision procedure which permits one to decide for any
such set X, whether or not X is ultimately periodic? For an integer base, the problem
was solved positively in [74]. The main ideas are the following ones. Given a DFA A
accepting a k-recognizable set X ⊆ N, the number of states of A gives an upper bound
on the possible index and period for X. Consequently, there are ﬁnitely many candidates
to check. For each such pair (i, p) of candidates, produce a DFA for all possible corre-
sponding ultimately periodic sets and compare it with A. Using non-deterministic ﬁnite
automata, the same problem was solved in [5]. With the formalism of ﬁrst-order logic
the problem becomes trivial. If a set X ⊆ N is k-recognizable, then using Theorem 4.5

On Cobham’s theorem 927

it is deﬁnable by a formula ϕ(x) in ⟨N, +, Vk⟩ and X is ultimately periodic if and only
if (∃p)(∃N )(∀x)(x ⩾ N ∧ (ϕ(x) ↔ ϕ(x + p))). Since we have a decidable theory, it
is decidable whether this latter sentence is true [29, Prop. 8.2]. The problem can be ex-
tended to Zd and was discussed in [97]. It is solved in polynomial time in [87]. In view of
Theorem 5.1 the question is extended to any abstract numeration system. Let S be an ab-
stract numeration system. Given a DFA accepting an S-recognizable set X ⊆ N, decide
whether or not X is ultimately periodic. Some special cases have been solved positively
in [33, 11]. Using Corollary 5.3, the same question can be asked in terms of morphisms.
Given a morphism σ : A
∗ → A
∗ prolongable on a letter a and a coding τ : A → B,
decide whether or not τ (σ∞(a)) is ultimately periodic. The is the HD0L (ultimate) pe-
riodicity problem. The purely substitutive case was solved independently in [101] and
[71]. The general substitutive case is solved positively in [51] and [95]. Also see [91, 92]
where decidability questions about almost-periodicity are considered. A word is almost
periodic if factors occurring inﬁnitely often have a bounded distance between occurrences
(but some factors may occur only ﬁnitely often).

8 Acknowledgments

We would like to warmly thank Val´erie Berth´e, Alexis B`es, V´eronique Bruy`ere, Christiane
Frougny, Julien Leroy, Narad Rampersad, and Jeffrey Shallit for their useful comments
after reading a preliminary version of this work.

References

[1] B. Adamczewski and J. Bell. Function ﬁelds in positive characteristic: expansions and Cob-
ham’s theorem. J. Algebra, 319:2337–2350, 2008. 920

[2] B. Adamczewski and J. Bell. An analogue of Cobham’s theorem for fractals. Trans. Amer.
Math. Soc., 363:4421–4442, 2011. 921

[3] B. Alexeev. Minimal DFAs for testing divisibility. J. Comput. Syst. Sci., 69:235–243, 2004.
899

[4] J.-P. Allouche. Sur la complexit´e des suites inﬁnies. Bull. Belg. Math. Soc., 1:133–143,
1994. 904

[5] J.-P. Allouche, N. Rampersad, and J. Shallit. Periodicity, repetitions, and orbits of an auto-
matic sequence. Theoret. Comput. Sci., 410(30-32):2795–2803, 2009. 926

[6] J.-P. Allouche and J. Shallit. The ring of k-regular sequences. Theoret. Comput. Sci.,
98(2):163–197, 1992. 920

[7] J.-P. Allouche and J. Shallit. The ring of k-regular sequences. II. Theoret. Comput. Sci.,
307(1):3–29, 2003. 920

[8] J.-P. Allouche and J. O. Shallit. The ubiquitous Prouhet-Thue-Morse sequence. In C. Ding,
T. Helleseth, and H. Niederreiter, editors, Sequences and Their Applications, Proceedings of
SETA ’98, pages 1–16. Springer-Verlag, 1999. 904

928 F. Durand, M. Rigo

[9] J.-P. Allouche and J. O. Shallit. Automatic Sequences, Theory, Applications, Generalizations.
Cambridge University Press, 2003. 902, 903, 904, 912, 920

[10] J. P. Bell. A generalization of Cobham’s theorem for regular sequences. S´em. Lothar. Com-
bin., 54A:Art. B54Ap, 15 pp. (electronic), 2005/07. 920

[11] J. P. Bell, E. Charlier, A. S. Fraenkel, and M. Rigo. A decision problem for ultimately
periodic sets in non-standard numeration systems. Internat. J. Algebra Comput., 19:809–
839, 2009. 927

[12] V. Berth´e and M. Rigo, editors. Combinatorics, automata and number theory, volume 135
of Encyclopedia of Mathematics and Its Applications. Cambridge University Press, 2009.
899, 901, 903, 904, 910, 914

[13] A. Bertrand-Mathis. D´eveloppement en base θ; r´epartition modulo un de la suite (xθn)n⩾0;
langages cod´es et θ-shift. Bull. Soc. Math. France, 114:271–323, 1986. 900, 901

[14] A. Bertrand-Mathis. Comment ´ecrire les nombres entiers dans une base que n’est pas enti`ere.
Acta Math. Hung., 54:237–241, 1989. 901, 902

[15] A. B`es. An extension of the Cobham-Sem¨enov theorem. J. Symbolic Logic, 65(1):201–211,
2000. 907, 908, 913

[16] A. B`es. A survey of arithmetical deﬁnability. Bull. Belg. Math. Soc. Simon Stevin, (suppl.):1–
54, 2001. A tribute to Maurice Boffa. 906

[17] B. Boigelot, L. Bronne, and S. Rassart. An improved reachability analysis method for
strongly linear hybrid systems. In O. Grumberg, editor, Proc. 9th CAV, volume 1254 of
Lecture Notes in Computer Science, pages 167–178. Springer Berlin Heidelberg, 1997. 921

[18] B. Boigelot and J. Brusten. A generalization of Cobham’s theorem to automata over real
numbers. Theoret. Comput. Sci., 410(18):1694–1703, 2009. 921

[19] B. Boigelot, J. Brusten, and V. Bruy`ere. On the sets of real numbers recognized by ﬁnite
automata in multiple bases. In L. Aceto, I. Damg˚ard, L. A. Goldberg, M. M. Halld´orsson,
A. Ing´olfsd´ottir, and I. Walukiewicz, editors, Proc. 35th ICALP (Reykjavik), volume 5126 of
Lecture Notes in Computer Science, pages 112–123. Springer-Verlag, 2008. 921

[20] B. Boigelot, J. Brusten, and J. Leroux. A generalization of Semenov’s theorem to automata
over real numbers. In R. A. Schmidt, editor, Automated Deduction, 22nd International Con-
ference, CADE 2009, McGill University, Montreal, volume 5663 of Lecture Notes in Com-
puter Science, pages 469–484, 2009. 921

[21] B. Boigelot, S. Jodogne, and P. Wolper. An effective decision procedure for linear arithmetic
over the integers and reals. ACM Trans. Comput. Log., 6(3):614–633, 2005. 921

[22] B. Boigelot, S. Rassart, and P. Wolper. On the expressiveness of real and integer arithmetic
automata. In Proc. 25th ICALP (Aalborg), volume 1443 of Lecture Notes in Computer Sci-
ence, pages 152–163. Springer, 1998. 921

[23] S. Brlek. Enumeration of factors in the Thue-Morse word. Discrete Appl. Math., 24:83–96,
1989. 905

[24] J. Brusten. On the sets of real vectors recognized by ﬁnite automata in multiple bases. PhD
thesis, University of Li`ege, Fac. Sciences Appliqu´ees, 2011. 921

[25] V. Bruy`ere. Automata and numeration systems. S´em. Lothar. Combin., 35:Art. B35b, 19 pp.
(electronic), 1995. 898

[26] V. Bruy`ere. On Cobham’s theorem. Thematic term on semigroups, algorithms, automata and
languages, School on automata and languages, Coimbra, Portugal, 2001. 898

On Cobham’s theorem 929

[27] V. Bruy`ere and G. Hansel. Bertrand numeration systems and recognizability. Theoret. Com-
put. Sci., 181(1):17–43, 1997. Latin American Theoretical INformatics (Valpara´ıso, 1995).
900, 908

[28] V. Bruy`ere, G. Hansel, C. Michaux, and R. Villemaire. Correction to: “Logic and p-
recognizable sets of integers”. Bull. Belg. Math. Soc., 1:577, 1994. 898, 906, 907, 908

[29] V. Bruy`ere, G. Hansel, C. Michaux, and R. Villemaire. Logic and p-recognizable sets of
integers. Bull. Belg. Math. Soc., 1:191–238, 1994. 898, 906, 907, 908, 927

[30] J. R. B¨uchi. Weak secord-order arithmetic and ﬁnite automata. Z. Math. Logik Grundlag.
Math., 6:66–92, 1960. Reprinted in S. Mac Lane and D. Siefkes, eds., the collected works of
J. Richard B¨uchi, Springer-Verlag, 1990, pp. 398–424. 907

[31] A. ˇCern´y and J. Gruska. Modular trellises. In G. Rozenberg and A. Salomaa, editors, The
book of L, pages 45–61. Springer-Verlag, 1986. 924

[32] E. Charlier, J. Leroy, and M. Rigo. An analogue of Cobham’s theorem for graph directed
iterated function systems. Adv. Math., 280:86–120, 2015. 921

[33] E. Charlier and M. Rigo. A decision problem for ultimately periodic sets in non-standard
numeration systems. In E. Ochma´nski and J. Tyszkiewicz, editors, Proc. of the 33th Inter-
national Symposium: MFCS (Torun), volume 5162 of Lecture Notes in Computer Science,
pages 241–252. Springer Berlin Heidelberg, 2008. 927

[34] G. Christol. Ensembles presque p´eriodiques k-reconnaissables. Theoret. Comput. Sci.,
9:141–145, 1979. 920

[35] G. Christol, T. Kamae, M. Mend`es France, and G. Rauzy. Suites alg´ebriques, automates et
substitutions. Bull. Soc. Math. France, 108:401–419, 1980. 920

[36] A. Cobham. On the Hartmanis-Stearns problem for a class of tag machines. In IEEE Con-
ference Record of 1968 Ninth Annual Symposium on Switching and Automata Theory, pages
51–60, 1968. Also appeared as IBM Research Technical Report RC-2178, August 23 1968.
912

[37] A. Cobham. On the base-dependence of sets of numbers recognizable by ﬁnite automata.
Math. Systems Theory, 3:186–192, 1969. 898, 902

[38] A. Cobham. Uniform tag sequences. Math. Systems Theory, 6:164–192, 1972. 902, 903,
904

[39] I. P. Cornfeld, S. V. Fomin, and Y. G. Sina˘ı. Ergodic theory, volume 245 of Grundlehren der
Mathematischen Wissenschaften. Springer-Verlag, New York, 1982. 923

[40] M. I. Cortez and F. Durand. Self-similar tiling systems, topological factors and stretching
factors. Discrete Comput. Geom., 40:622–640, 2008. 925

[41] A. de Luca and S. Varricchio. Some combinatorial properties of the Thue-Morse sequence
and a problem in semigroups. Theoret. Comput. Sci., 63(3):333–348, 1989. 905

[42] V. Diekert and D. Krieger. Some remarks about stabilizers. Theoret. Comput. Sci., 410(30-
32):2935–2946, 2009. 919

[43] A. W. M. Dress and F. von Haeseler. A semigroup approach to automaticity. Ann. Comb.,
7(2):171–190, 2003. 920

[44] F. Durand. A characterization of substitutive sequences using return words. Discrete Math.,
179(1-3):89–101, 1998. 913

[45] F. Durand. A generalization of Cobham’s theorem. Theory Comput. Syst., 31(2):169–185,
1998. 913

930 F. Durand, M. Rigo

[46] F. Durand. Sur les ensembles d’entiers reconnaissables. J. Th´eor. Nombres Bordeaux,
10(1):65–84, 1998. 913, 920

[47] F. Durand. Linearly recurrent subshifts have a ﬁnite number of non-periodic subshift factors.
Ergodic Theory Dynam. Systems, 20(4):1061–1078, 2000. 923

[48] F. Durand. A theorem of Cobham for non primitive substitutions. Acta Arith., 104:225–241,
2002. 912

[49] F. Durand. Cobham-Semenov theorem and Nd-subshifts. Theoret. Comput. Sci., 391(1-
2):20–38, 2008. 925

[50] F. Durand. Cobham’s theorem for substitutions. J. Eur. Math. Soc. (JEMS), 13:1799–1814,
2011. 913

[51] F. Durand. Decidability of the HD0L ultimate periodicity problem. RAIRO Theor. Inform.
Appl., 47:201–214, 2013. 927

[52] F. Durand and M. Rigo. Syndeticity and independent substitutions. Adv. in Appl. Math.,
42:1–22, 2009. 912, 915, 916, 919

[53] F. Durand and M. Rigo. Multidimensional extension of the Morse-Hedlund theorem. Europ.
J. Combin., 34:391–409, 2013. 906

[54] H.-D. Ebbinghaus, J. Flum, and W. Thomas. Mathematical logic. Undergraduate Texts in
Mathematics. Springer-Verlag, New York, second edition, 1994. 907

[55] S. Eilenberg. Automata, languages, and machines, volume A. Academic Press, 1974. 902,
904

[56] H. B. Enderton. A mathematical introduction to logic. Academic Press, New York, 1972.
907

[57] S. Fabre. Une g´en´eralisation du th´eor`eme de Cobham. Acta Arith., 67:197–208, 1994. 913

[58] S. Fabre. Substitutions et β-syst`emes de num´eration. Theoret. Comput. Sci., 137(2):219–236,
1995. 913, 919

[59] I. Fagnot. Sur les facteurs des mots automatiques. Theoret. Comput. Sci., 172:67–89, 1997.
913

[60] N. P. Fogg. Substitutions in dynamics, arithmetics and combinatorics, volume 1794 of Lec-
ture Notes in Mathematics. Springer-Verlag, Berlin, 2002. Edited by V. Berth´e, S. Ferenczi,
C. Mauduit and A. Siegel. 904, 912

[61] A. S. Fraenkel. Systems of numeration. Amer. Math. Monthly, 92:105–114, 1985. 899

[62] C. Frougny. Representations of numbers and ﬁnite automata. Math. Systems Theory,
25(1):37–60, 1992. 900, 908

[63] C. Frougny. Non-standard number representation: computer arithmetic, beta-numeration and
quasicrystals. In Physics and theoretical computer science, volume 7 of NATO Secur. Sci.
Ser. D Inf. Commun. Secur., pages 155–169. IOS, Amsterdam, 2007. 897

[64] F. R. Gantmacher. The theory of matrices. Chelsea, 1960. 911

[65] S. Ginsburg and E. H. Spanier. Semigroups, Presburger formulas, and languages. Paciﬁc J.
Math., 16:285–296, 1966. 908

[66] W. H. Gottschalk and G. A. Hedlund. Topological dynamics, volume 36 of AMS Colloquium
Publications. Amer. Math. Soc., 1955. 902

[67] G. Hansel. A propos d’un th´eor`eme de Cobham. In D. Perrin, editor, Actes de la fˆete des
mots, pages 55–59. Greco de Programmation, CNRS, Rouen, 1982. 902

On Cobham’s theorem 931

[68] G. Hansel. Syst`emes de num´eration ind´ependants et synd´eticit´e. Theoret. Comput. Sci.,
204:119–130, 1998. 902

[69] G. Hansel and T. Safer. Vers un th´eor`eme de Cobham pour les entiers de Gauss. Bull. Belg.
Math. Soc. Simon Stevin, 10:723–735, 2003. 925, 926

[70] G. H. Hardy and E. M. Wright. An introduction to the theory of numbers. Oxford University
Press, 5th edition, 1985. 898

[71] T. Harju and M. Linna. On the periodicity of morphisms on free monoids. RAIRO Inform.
Th´eor. App., 20:47–54, 1986. 927

[72] M. Hollander. Greedy numeration systems and regularity. Theory Comput. Systems, 31:111–
133, 1998. 901

[73] C. Holton and L. Q. Zamboni. Directed graphs and substitutions. Theory Comput. Syst.,
34(6):545–564, 2001. 923

[74] J. Honkala. A decision method for the recognizability of sets deﬁned by number systems.
RAIRO Inform. Th´eor. App., 20:395–403, 1986. 926

[75] J. Honkala. On the simpliﬁcation of inﬁnite morphic words. Theoret. Comput. Sci., 410(8-
10):997–1000, 2009. 912

[76] R. A. Horn and C. R. Johnson. Matrix analysis. Cambridge University Press, Cambridge,
1990. Corrected reprint of the 1985 original. 911

[77] I. K´atai and J. Szab´o. Canonical number systems for complex integers. Acta Sci. Math.
(Szeged), 37(3-4):255–260, 1975. 925

[78] K. S. Kedlaya. The algebraic closure of the power series ﬁeld in positive characteristic. Proc.
Amer. Math. Soc., 129(12):3461–3470, 2001. 920

[79] K. S. Kedlaya. Finite automata and algebraic extensions of function ﬁelds. J. Th´eor. Nombres
Bordeaux, 18(2):379–420, 2006. 920

[80] B. P. Kitchens. Symbolic dynamics. Universitext. Springer-Verlag, Berlin, 1998. One-sided,
two-sided and countable state Markov shifts. 923

[81] D. E. Knuth. The art of computer programming. Vol. 2. Addison-Wesley Publishing Co.,
Reading, Mass., second edition, 1981. Seminumerical algorithms, Addison-Wesley Series in
Computer Science and Information Processing. 921

[82] T. J. P. Krebs. A more reasonable proof of Cobham’s theorem. CoRR, abs/1801.06704, 2018.
902

[83] D. Krieger, A. Miller, N. Rampersad, B. Ravikumar, and J. Shallit. Decimations of languages
and state complexity. Theoret. Comput. Sci., 410:2401–2409, 2009. 910

[84] P. K˚urka. Topological and symbolic dynamics, volume 11 of Cours Sp´ecialis´es. Soci´et´e
Math´ematique de France, Paris, 2003. 923

[85] L. Latour. Presburger Arithmetic: from Automata to Formulas. PhD thesis, University of
Li`ege, Fac. Sciences Appliqu´ees, 2006. 907

[86] P. B. A. Lecomte and M. Rigo. Numeration systems on a regular language. Theory Comput.
Systems, 34:27–44, 2001. 909

[87] J. Leroux. A polynomial time Presburger criterion and synthesis for number decision dia-
grams. In IEEE Symposium on Logic in Computer Science (LICS 2005), IEEE Computer
Society, pages 147–156, 2005. 927

[88] D. Lind and B. Marcus. An introduction to symbolic dynamics and coding. Cambridge
University Press, 1995. 911, 922, 923

932 F. Durand, M. Rigo

[89] M. Lothaire. Combinatorics on words, volume 17 of Encyclopedia of Mathematics and Its
Applications. Addison-Wesley, 1983. 903, 904

[90] M. Lothaire. Algebraic combinatorics on words, volume 90 of Encyclopedia of Mathematics
and Its Applications. Cambridge University Press, 2002. 899, 900, 901, 903

[91] A. Maes. Morphisms and almost-periodicity. Discrete Appl. Math., 86(2-3):233–248, 1998.
927

[92] A. Maes. More on morphisms and almost-periodicity. Theoret. Comput. Sci., 231(2):205–
215, 2000. Universal machines and computations (Metz, 1998). 927

[93] C. Michaux and R. Villemaire. Cobham’s theorem seen through B¨uchi’s theorem. In Au-
tomata, languages and programming (Lund, 1993), volume 700 of Lecture Notes in Com-
puter Science, pages 325–334. Springer, Berlin, 1993. 908

[94] C. Michaux and R. Villemaire. Presburger arithmetic and recognizability of sets of natural
numbers by automata: New proofs of Cobham’s and Semenov’s theorems. Ann. Pure Appl.
Logic, 77:251–277, 1996. 908

[95] I. V. Mitrofanov. Periodicity of morphic words. Fundam. Prikl. Mat., 18:107–119, 2013.
927

[96] M. Morse and G. A. Hedlund. Symbolic dynamics. Amer. J. Math., 60:815–866, 1938. 904

[97] A. A. Muchnik. The deﬁnable criterion for deﬁnability in Presburger arithmetic and its
applications. Theoret. Comput. Sci., 290(3):1433–1444, 2003. 908, 924, 927

[98] M. Nivat. invited talk at ICALP, Bologna, 1997. 906

[99] N. Ormes, C. Radin, and L. Sadun. A homeomorphism invariant for substitution tiling
spaces. Geom. Dedicata, 90:153–182, 2002. 925

[100] J.-J. Pansiot. Complexit´e des facteurs des mots inﬁnis engendr´es par morphismes it´er´es. In
Automata, languages and programming (Antwerp, 1984), volume 172 of Lecture Notes in
Computer Science, pages 380–389. Springer, Berlin, 1984. 918

[101] J.-J. Pansiot. Decidability of periodicity for inﬁnite words. RAIRO Inform. Th´eor. App.,
20:43–46, 1986. 927

[102] W. Parry. On the β-expansions of real numbers. Acta Math. Acad. Sci. Hung., 11:401–416,
1960. 900

[103] B. Pascal. Œuvres compl`etes. Seuil, 1963. The treatise De numeris multiplicibus, written
with the other arithmetical treatises before 1654, was published by Guillaume Desprez in
1665. 899

[104] D. Perrin. Finite automata. In J. van Leeuwen, editor, Handbook of theoretical computer
science, Volume B:Formal models and semantics, pages 1–57. Elsevier — MIT Press, 1990.
898, 902

[105] F. Point and V. Bruy`ere. On the Cobham-Semenov theorem. Theory Comput. Syst.,
30(2):197–220, 1997. 908

[106] F. Point, M. Rigo, and L. Waxweiler. Deﬁning multiplication in some additive expansions of
polynomial rings. Comm. in Algebra, 44:2075–2099, 2016. 926

[107] M. Presburger. ¨Uber die Volst¨andigkeit eines gewissen Systems der Arithmetik ganzer
Zahlen, in welchem die Addition als einzige Operation hervortritt. C. R. Premier congr`es
des Math´ematiciens des pays slaves, Varsovie, pages 92–101, 1929. 906, 907

[108] M. Presburger. On the completeness of a certain system of arithmetic of whole numbers in
which addition occurs as the only operation. Hist. Philos. Logic, 12:225–233, 1991. 906,
907
 On Cobham’s theorem 933

[109] A. Quas and L. Zamboni. Periodicity and local complexity. Theoret. Comput. Sci., 319:229–
240, 2004. 906

[110] M. Queff´elec. Substitution dynamical systems—spectral analysis, volume 1294 of Lecture
Notes in Mathematics. Springer-Verlag, Berlin, 1987. 916, 923

[111] A. R´enyi. Representations for real numbers and their ergodic properties. Acta Math. Acad.
Sci. Hung., 8:477–493, 1957. 900

[112] M. Rigo. Generalization of automatic sequences for numeration systems on a regular lan-
guage. Theoret. Comput. Sci., 244:271–281, 2000. 910

[113] M. Rigo. Syntactical and automatic properties of sets of polynomials over ﬁnite ﬁelds. Finite
Fields Appl., 14(1):258–276, 2008. 926

[114] M. Rigo. Formal languages, automata and numeration systems, Applications to recogniz-
ability and decidability, volume 2. ISTE-Wiley, 2014. 906

[115] M. Rigo and A. Maes. More on generalized automatic sequences. J. Automata, Languages,
and Combinatorics, 7:351–376, 2002. 910

[116] M. Rigo and L. Waxweiler. A note on syndeticity, recognizable sets and Cobham’s theorem.
Bull. European Assoc. Theor. Comput. Sci., 88:169–173, February 2006. 902

[117] J. Sakarovitch. ´El´ements de th´eorie des automates. Vuibert, 2003. English corrected edition:
Elements of Automata Theory, Cambridge University Press, 2009. 899

[118] A. Salomaa and M. Soittola. Automata-theoretic aspects of formal power series. Springer-
Verlag, New York, 1978. Texts and Monographs in Computer Science. 914

[119] O. Salon. Suites automatiques `a multi-indices. In S´eminaire de Th´eorie des Nombres de
Bordeaux, pages 4.01–4.27, 1986-1987. 905

[120] O. Salon. Suites automatiques `a multi-indices et alg´ebricit´e. C. R. Acad. Sci. Paris, 305:501–
504, 1987. 905

[121] A. L. Semenov. The Presburger nature of predicates that are regular in two number systems.
Sibirsk. Mat. ˇZ., 18(2):403–418, 479, 1977. In Russian. English translation in Siberian J.
Math. 18 (1977), 289–300. 908, 925

[122] E. Seneta. Non-negative matrices and Markov chains. Springer Series in Statistics. Springer,
New York, 2006. 911

[123] J. O. Shallit. Numeration systems, linear recurrences, and regular sets. Inform. Comput.,
113:331–347, 1994. 900, 909

[124] B. Solomyak. Dynamics of self-similar tilings. Ergodic Theory Dynam. Systems, 17(3):695–
738, 1997. 925

[125] B. Tan and Z.-Y. Wen. Some properties of the Tribonacci sequence. European J. Combin.,
28(6):1703–1719, 2007. 912

[126] R. Villemaire. Joining k- and l-recognizable sets of natural numbers. In STACS 92 (Cachan,
1992), volume 577 of Lecture Notes in Computer Science, pages 83–94. Springer, Berlin,
1992. 908

[127] R. Villemaire. The theory of ⟨N, +, Vk, Vl⟩ is undecidable. Theoret. Comput. Sci.,
106(2):337–349, 1992. 908

[128] M. Waldschmidt. Diophantine approximation on linear algebraic groups, volume 326 of
Grundlehren der Mathematischen Wissenschaften. Springer-Verlag, Berlin, 2000. Transcen-
dence properties of the exponential function in several variables. 926

934 F. Durand, M. Rigo

[129] L. Waxweiler. Caract`ere reconnaissable d’ensembles de polynˆomes `a coefﬁcients dans un
corps ﬁni. PhD thesis, University of Li`ege, 2009. http://hdl.handle.net/2268/11381. 926

[130] P. Wolper and B. Boigelot. Verifying systems with inﬁnite but regular state spaces. In Com-
puter aided veriﬁcation (Vancouver, BC, 1998), volume 1427 of Lecture Notes in Computer
Science, pages 88–97. Springer, Berlin, 1998. 897

[131] E. Zeckendorf. Repr´esentation des nombres naturels par une somme de nombres de Fi-
bonacci ou de nombres Lucas. Bull. Soc. Roy. Li`ege, 41:179–182, 1972. 900
