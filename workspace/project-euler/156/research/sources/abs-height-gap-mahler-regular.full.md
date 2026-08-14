<!-- source: https://arxiv.org/pdf/2003.03429 | converted from PDF -->

arXiv:2003.03429v2  [math.NT]  11 Oct 2021
A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER
FUNCTIONS

BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

Abstract. We study the asymptotic growth of coeﬃcients of Mahler power series
with algebraic coeﬃcients, as measured by their logarithmic Weil height. We show
that there are ﬁve diﬀerent growth behaviors, all of which being reached. Thus, there
are gaps in the possible growths. In proving this height gap theorem, we obtain that
a k-Mahler function is k-regular if and only if its coeﬃcients have height in O(log n).
Moreover, we deduce that, over an arbitrary ground ﬁeld of characteristic zero, a k-
Mahler function is k-automatic if and only if its coeﬃcients belong to a ﬁnite set. As
a by-product of our results, we also recover a conjecture of Becker which was recently
settled by Bell, Chyzak, Coons, and Dumas.

1. Introduction

The study of power series solutions to linear diﬀerential equations with coeﬃcients
in Q[z] provides a deep interplay between various ﬁelds of mathematics and physics,
including combinatorics and number theory. For instance, the study of generating series
in enumerative combinatorics beneﬁts from the useful dictionary between asymptotics
of coeﬃcients of D-ﬁnite power series and the type of singularities of the corresponding
diﬀerential equation (see [FS09FS09]). More surprisingly, prescribing some kind of arithmetic
behavior for coeﬃcients gives rise to powerful number theoretical consequences, as ﬁrst
perceived by Siegel [Sie29Sie29] when introducing E- and G-functions, and pursued more
recently by André [And00aAnd00a, And00bAnd00b] in his study of arithmetic Gevrey series.
This paper deals with the arithmetic behavior of coeﬃcients of Mahler functions, or
M -functions, which are power series of a very diﬀerent kind. Unless it is rational, an
M -function never satisﬁes a linear or even an algebraic diﬀerential equation [ADH21ADH21].
Instead, M -functions are solutions to linear diﬀerence equations with coeﬃcients in Q[z]
associated with the Mahler operator z ↦→ zk, where k ≥ 2 is a natural number. Precisely,
a power series f (z) ∈ QJzK is a k-Mahler function, or for short k-Mahler, if it satisﬁes
an equation of the form

(1.1) p0(z)f (z) + · · · + pd(z)f (zkd) = 0

with p0(z), . . . , pd(z) ∈ Q[z] and p0(z)pd(z) ̸= 0. A power series is an M -function if it is
a k-Mahler function for some k. The study of M -functions and their values was initiated
at the end of the 1920’s by Mahler [Mah29Mah29, Mah30aMah30a, Mah30bMah30b], who developed a new

This project has received funding from the European Research Council (ERC) under the European
Union’s Horizon 2020 research and innovation program under the Grant Agreement No 648132. Smertnig
was supported by the Austrian Science Fund (FWF) project J4079-N32. Part of the research was
conducted while Smertnig was visiting University of Waterloo; he would like to extend his thanks for
their hospitality. 1

2 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

direction in transcendence theory, nowadays known as Mahler’s method. In fact, Mahler
only considered order one equations, but possibly inhomogeneous and also non-linear
ones. The interest for M -functions of arbitrary order really took on a new signiﬁcance
at the beginning of the 1980s after Mendès France popularized among number theorists
a result of Cobham [Cob68Cob68] stating that automatic power series are M -functions. After
recent results [Phi15Phi15, AF17AF17], the transcendence theory of M -functions mirrors exactly
the one of E-functions. Beyond Mahler’s method and automata theory, it is worth
mentioning that M -functions naturally occur as generating functions in various other
topics such as combinatorics of partitions, numeration, and analysis of algorithms. In
particular, the regular power series introduced by Allouche and Shallit [AS92AS92] form a
distinguished class of M -functions. There is also a mysterious interplay between G-
functions and M -functions that deserves more attention. Indeed, for some G-functions
∑∞
n=0 anzn ∈ QJzK, the power series ∑∞
n=0 vp(an)zn, where vp(an) is the p-adic valuation
of an, turns out to be p-Mahler. This is likely related to the fact that Picard-Fuchs
diﬀerential equations have a strong Frobenius structure for almost all primes. In re-
cent years, there is renewed interest in M -functions, as evidenced by the ﬂourishing
literature on this topic. The latter includes discussions on various perspectives such
as transcendence and algebraic independence, combinatorics and theoretical computer
science, the study of Mahler’s equations and associated Galois theories, and computa-
tional aspects. A number of references can be found in the survey [Ada19Ada19]. See also
[ADH21ADH21, ADHW20ADHW20, AF20AF20, BCCD19BCCD19] for more recent ones.

1.1. The Height Gap Theorem. Let us ﬁrst recall that the coeﬃcients of a k-Mahler
function ∑∞
n=0 anzn ∈ QJzK satisfy some recurrence relation of the form

an =
 s∑

j=1 −αjan−j +
 d∑

i=1
 s∑

j=0 βi,ja n−j
ki ,

where αj and βi,j are algebraic numbers, and n is large enough (see Equation (5.15.1), in
which one can achieve m = 0 using Lemma 3.13.1). It follows that the ﬁeld extension of
Q generated by all coeﬃcients an is a number ﬁeld. In the sequel, we will measure the
coeﬃcients of an M -function by their logarithmic Weil height.

1.1.1. The logarithmic Weil height. For a number ﬁeld, we normalize the non-trivial
absolute values as in [BG06BG06]. Thus, for Q and p a prime we let |p|p = 1/p; for the
archimedean place of Q we use the usual absolute value. For K a number ﬁeld and a
place w of K extending a place v of Q, let

|α|w := |NKw/Qv(α)|
1/[K:Q]
v .

Then the set of places MK on K satisﬁes the product formula. For α ∈ Q the logarithmic
absolute Weil height is deﬁned by

h(α) = log ∏

v∈MK max{1, |α|v},

where K is any number ﬁeld containing α. The value h(α) in this deﬁnition does not
depend on the choice of such a number ﬁeld K. For a/b ∈ Q ∖ {0} with a, b ∈ Z, b ̸= 0,

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 3

and gcd(a, b) = 1, h(a/b) = log max{|a|, |b|}.

For more properties about the logarithmic Weil height, as well as for comparison with
other notions of height, we refer the reader to [Wal00Wal00, Chapter 3].

1.1.2. Landau notation. Let (an)n≥0 be a sequence of non-negative real numbers and
(bn)n≥0 be a sequence of, eventually positive, real numbers. As usual, the notation
an ∈ O(bn) means that there exists a positive number c such that an < cbn for every
suﬃciently large positive integer n, while the notation an ∈ o(bn) means that an/bn tends
to zero as n tends to inﬁnity. Moreover, sticking to the usual practice in number theory,
we write an ∈ Ω(bn) when an ̸∈ o(bn), that is, when there exists a positive number c
such that an > cbn for inﬁnitely many positive integers n. We also write an ∈ O ∩ Ω(bn)
when both an ∈ O(bn) and an ∈ Ω(bn).

We are now ready to state our ﬁrst main result.

Theorem 1.1 (Height Gap Theorem). Let f (z) = ∑∞
n=0 anzn ∈ QJzK be an M -function.
Then one of the following properties holds.
(1) h(an) ∈ O ∩ Ω(n).
(2) h(an) ∈ O ∩ Ω(log2 n).
(3) h(an) ∈ O ∩ Ω(log n).
(4) h(an) ∈ O ∩ Ω(log log n).
(5) h(an) ∈ O(1).

Theorem 1.11.1 implies that the coeﬃcients of an M -function can only exhibit certain
speciﬁc growth behaviors. For instance, as h(an) ∈ o(n) forces h(an) ∈ O(log2 n), there
cannot be such a power series with h(an) ∼ log3 n. Thus, there are gaps in the possible
growths. Let us make few comments on Theorem 1.11.1.
• In Section 22, we provide the reader with examples for each of the ﬁve growth classes,
thereby showing that all of them occur.

• There is no chance in general of replacing lower bounds of the type Ω by stronger
ones. For instance, the 2-Mahler function ∑∞
n=0 2nz2n belongs to class (3), but most
of its coeﬃcients vanish.

• An M -function f (z) can be uniquely speciﬁed by the ﬁnite data consisting of a
k-Mahler equation it satisﬁes and suﬃciently many initial coeﬃcients of the power
series. Assuming the knowledge of such data, we will show that it is decidable
which of the ﬁve growth classes in Theorem 1.11.1 the function f (z) falls into. This is
Theorem 12.112.1.

1.2. Height and structural properties of M -functions. We already alluded to the
fact that inside the ring of k-Mahler functions two subsets are usually distinguished,
leading to the following hierarchy:

{k-automatic functions} ⊊ {k-regular functions} ⊊ {k-Mahler functions} .

We refer the reader to [AS03aAS03a] and Section 33 for precise deﬁnitions and more details
about automatic and regular power series. The following result shows that each of

4 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

these two subsets can be characterized within the k-Mahler functions by their coeﬃcient
growth, using the reﬁned hierarchy provided by Theorem 1.11.1.

Theorem 1.2. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be a k-Mahler function. Then the two
following properties hold.
(a) f (z) is k-automatic if and only if h(an) ∈ O(1), that is, if and only if the sequence
an takes values in a ﬁnite set.
(b) f (z) is k-regular if and only if h(an) ∈ O(log n).

Case (a)(a) of Theorem 1.21.2 extends to arbitrary ground ﬁelds of characteristic zero (see
Theorem 11.111.1). This generalizes the well-known fact that k-regular sequences taking
only ﬁnitely many values are k-automatic [AS03aAS03a, Theorem 16.1.5].
In fact, in proving Theorem 1.11.1, we will show that each of the ﬁve growth classes
corresponds to natural structural properties of the k-Mahler equation, respectively, the
coeﬃcient series. The corresponding results are stated in Theorems 6.16.1, 7.17.1, 8.38.3, and 9.19.1.
Theorem 1.21.2 above provides only a sample. In order to get such structural results, we
reinforce the importance of measuring the size of coeﬃcients by their height and not
only by their modulus. For instance, all the following three Mahler functions

∞∏

n=0
(1 − z2n ) ,
 ∞∑

n=0 2
−nz2n , 1
1 − z/2 ·
 ∞∏

n=0
(1 − z2n)

have bounded rational coeﬃcients, so we cannot distinguish them through the growth
of their coeﬃcients. This is a deﬁciency, for the ﬁrst one is automatic, the second one is
regular but not automatic, and the third one is not regular. However, their coeﬃcients
have diﬀerent height growth behaviors and they can be distinguished by Theorem 1.11.1.
They belong respectively to classes (1), (3), and (5).
The decidability of growth properties of k-regular sequences with respect to the usual
(archimedean) absolute value has recently been considered by Krenn and Shallit [KS20KS20].
In contrast to our results, many of these properties become undecidable. For instance,
it is undecidable whether the sequence of coeﬃcients is bounded [KS20KS20, Theorem D].

Outline. This article is organized as follows. Section 22 provides the reader with a
collection of examples, showing that each of the ﬁve growth classes in the height gap
theorem actually occurs. In Sections 33 and 44, we give some background about Mahler
equations, automatic and regular power series, and Mahler’s method. Sections 55 to 99
are then devoted to the proof of Theorem 1.11.1. In fact, we prove the much more precise
Theorems 6.16.1, 7.17.1, 8.38.3, and 9.19.1. In Section 1010, we discuss how our main results imply
Becker’s conjecture. In Section 1111, we characterize those k-Mahler functions which are
automatic over an arbitrary ground ﬁeld of characteristic zero. In the ﬁnal Section 1212,
we deal with the question of decidability in Theorem 1.11.1.

Notation. Throughout the paper, we use the following notation. We let k ≥ 2 be a
natural number. We let Σk denote the alphabet {0, 1, . . . , k − 1} and Σ∗
k denote the
free monoid generated by Σk, with neutral element ε. Given a positive integer n, we
set ⟨n⟩k := wrwr−1 · · · w0 for the canonical base-k expansion of n (written from most
to least signiﬁcant digit), which means that n = ∑r
i=0 wiki with wi ∈ Σk and wr ̸= 0.
Note that by convention ⟨0⟩k := ε. Conversely, if w := w0 · · · wr is a ﬁnite word over the

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 5

alphabet Σk, we set [w]k := ∑r
i=0 wr−iki. We let U ⊆ Q denote the set of all roots of
unity. For ζ ∈ Q with ζ ̸= 0, observe that there exists j > 0 with ζ kj = ζ if and only
if ζ ∈ U and ζ has order coprime to k. We let Uk ⊆ U denote the set of roots of unity
whose order is not coprime with k.

2. Witnessing Examples

In this section, we provide examples of Mahler functions f (z) = ∑∞
n=0 anzn ∈ QJzK
for each of the ﬁve growth classes occurring in the height gap theorem. We recall that
a rational power series is k-Mahler for all k ≥ 2.

Examples in O∩Ω(n). The upper bound h(an) ∈ O(n) holds for every Mahler function,
by Theorem 1.11.1. To give examples of Mahler functions whose coeﬃcient sequence has
growth in O ∩ Ω(n), it therefore suﬃces to ﬁnd examples whose coeﬃcient series has
growth in Ω(n).

(a) The coeﬃcients of the rational function

1
1 − 2z =
 ∞∑

n=0 2
nzn

have linear growth since h(2n) = n log(2).

(b) Let a, k ≥ 2 be integers and consider the transcendental inﬁnite product

∞∏

n=0
 1
1 − azkn =
 ∞∑

n=0 anzn.

This power series is k-Mahler and an is at least as large as the coeﬃcient of zn in
1/(1 − az), that is an ≥ an. Hence h(an) ≥ n log(a).

(c) The previous example has poles at a−1/kn for all n ≥ 1, but it can be reﬁned to
one that is analytic in the open unit disk of C. Let a, k ≥ 2 be integers and let us
consider the inﬁnite product

∞∏

n=0
 1
1 − a−1zkn =
 ∞∑

n=0 anzn ∈ QJzK.

A partition of n into k-powers is an expression n = j1kn1 + · · · + jrknr with r ∈ Z≥0,
0 ≤ n1 < · · · < nr, and j1, . . . , jr ∈ Z≥0. Expanding the factors in the deﬁnition of
the inﬁnite product as geometric series, we see that

an = ∑

n=j1kn1 +···+jrknr a
−(j1+···+jr),

where the sum is over partitions of n into k-powers. The partition n = 1 + · · · + 1 =
n · k0 gives a summand a−n, and for all other summands j1 + · · · + jr < n. Let p be
a prime divisor of a. Then |an|p ≥ pn, and therefore h(an) ≥ n log p.

6 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

Examples in O ∩ Ω(log2 n). The following example is typical of the Mahler functions
in the class O ∩ Ω(log2 n). It will play a prominent role in Section 77.
(d) Let k ≥ 2 be an integer and consider the inﬁnite product of cyclotomic polynomials

∞∏

n=0
 1
1 − zkn =
 ∞∑

n=0 anzn .

As in (c)(c) above, we see that the integer an is equal to the number of partitions of n
into k-powers. The asymptotics of the coeﬃcient sequence an were ﬁrst studied by
Mahler [Mah40Mah40], who proved that

log an ∼ log2 n
2 log k ·

These results of Mahler have been reﬁned and generalized by de Bruijn [dB48dB48] and
most recently by Dumas and Flajolet [DF96DF96].

(e) Multiplying the inﬁnite product in (d)(d) by any non-zero k-regular power series with
positive coeﬃcients provides a transcendental k-Mahler function with the required
growth behavior. In fact, Theorem 3.83.8 shows that examples in the class O∩Ω(log2 n)
are essentially all of that type.

Examples in O ∩ Ω(log n). For every regular sequence (an)n≥0, the generating series
∑∞
n=0 anzn is an M -function, and examples for which h(an) ∈ O ∩ Ω(log n) abound. We
give some examples and refer the reader to [AS03aAS03a, Chapter 16.5] and [AS92AS92, AS03bAS03b]
for more.
(f) The rational power series
 z
(1 − z)2 =
 ∞∑

n=0 nzn ,

falls into this class, since h(n) = log(n). More generally, if p(z) is a non-constant
polynomial with integer coeﬃcients, then ∑∞
n=0 p(n)zn is a rational function with
the required growth behavior.

(g) Let vp(n) denote the p-adic valuation of the natural number n, where p is a prime
number. The power series ∞∑

n=0 vp(n!)zn,

is p-regular [AS92AS92, Example 8]. Moreover, by Legendre’s formula vp(n!) ∼ n/(p−1).

(h) Let ℓn denote the number of positive integers at most equal to n that can be written
as sum of three squares. The power series ∑∞
n=0 ℓnzn is 2-regular [AS03aAS03a, Example
16.5.2]. Since every integer not of the form 4a(8b + 7) can be written as a sum of
three squares, the sequence has the required growth behavior.

(i) Any linear representation (u, µ, v) on the alphabet Σk gives rise to a k-regular se-
quence (see Deﬁnition 3.43.4). From our results, we will see that whenever there exists
a word w ∈ Σ∗
k such that the matrix µ(w) has an eigenvalue that is neither 0 nor a
root of unity, then the sequence associated with this linear representation has the
required growth behavior.

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 7

Examples in O ∩ Ω(log log n). M -functions whose coeﬃcients have growth in O ∩
Ω(log log n) can again be found by looking at generating functions of suitable k-regular
sequences.
(j) The power series ∞∑

n=1
(1 + ⌊log2 n⌋)zn

is 2-regular [AS92AS92, Example 11], and clearly has the required growth behavior.

(k) Let sn denote the sum of digits in the base-k expansion of n. Then clearly (sn)n≥0
is k-regular, and therefore the power series ∑∞
n=0 snzn is k-Mahler. Since sn ∈
O(log n), it holds that h(sn) ∈ O(log log n). Moreover, for e ≥ 0 and n = ke − 1 we
have sn = (k − 1)e ∼ (k − 1) logk n. Hence sn has he required growth behavior.

Examples in O(1). By Theorem 1.21.2, this class of M -functions corresponds exactly to
generating series of automatic sequences. We refer the reader to the monograph [AS03aAS03a]
for numerous examples, including the generating series of the Thue-Morse sequence, the
Rudin-Shapiro sequence, the Baum-Sweet sequence, and the paperfolding sequence, to
name a few.
 3. Preliminaries

Throughout this section, we let K be a ﬁeld. We will later restrict ourselves to K = Q.
We recall k-Mahler, k-automatic, k-regular, and k-Becker power series and their relation
to each other.

3.1. Mahler functions, equations, and systems. Let us recall that a power series
f (z) ∈ KJzK is a k-Mahler function if it satisﬁes an equation of the form (1.11.1), that is
if there exist a non-negative integer d and polynomials p0(z), . . . , pd(z) ∈ K[z], not all
zero, such that p0(z)f (z) + p1(z)f (zk) + · · · + pd(z)f (zkd) = 0 .
It can be shown that every Mahler function satisﬁes such a functional equation with
p0(z)pd(z) ̸= 0 and p0(z), . . . , pd(z) coprime [AB17AB17, Lemma 4.1]. As we will only be
interested in the asymptotic behavior of the coeﬃcients, the following lemma allows a
further simpliﬁcation of the Mahler equation.

Lemma 3.1. Suppose f (z) = ∑∞
n=0 anzn ∈ KJzK satisﬁes a Mahler equation

(3.1) p0(z)f (z) = p1(z)f (zk) + · · · + pd(z)f (zkd)

with p0(z)pd(z) ̸= 0 and p0(z), . . . , pd(z) coprime. Then there exists n0 ≥ 0 such that
an0 ̸= 0 and f0(z) := ∑∞
n=0 an+n0zn satisﬁes a k-Mahler equation

q0(z)f0(z) = q1(z)f0(zk) + · · · + qd+1(z)f0(zkd+1)

with polynomials q0(z), . . . , qd+1(z) satisfying the following conditions.
(i) One has q0(0) = 1.
(ii) If λ ∈ K ∖ {0}, then p0(λ) = 0 implies q0(λ) = 0.
(iii) If ζ ∈ K ∖ {0} with p0(ζ) = 0 and ζ k = ζ, then qi(ζ) ̸= 0 for some i ∈ {1, . . . , d+ 1}.
Moreover, if f (z) has at least two non-zero coeﬃcients, then f0(z) is non-constant.

8 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

Proof. By [AB17AB17, Lemma 6.1]; the ﬁnal statement requires an inspection of the proof. □

We also need the following fact, a more general version of which is, for instance, proved
in [AB17AB17, Proposition 8.1].

Lemma 3.2. If f (z) ∈ KJzK is k-Mahler and e is a positive integer, then f (z) is also
ke-Mahler.

3.1.1. Linear Mahler systems. A power series f (z) ∈ KJzK is k-Mahler if and only if it
satisﬁes a linear k-Mahler system. That is, there exist f1(z) := f (z), . . . , fd(z) ∈ KJzK
and A(z) ∈ GLd(K(z)) such that

(3.2)
 



f1(z)
...
fd(z)



 = A(z)
 



f1(zk)
...
fd(zk)




 .

Indeed, given f (z) satisfying a k-Mahler equation f (z) = r1(z)f (zk) + · · · + rd(z)f (zkd)
with r1(z), . . . rd(z) ∈ K(z) and rd(z) ̸= 0, the vector
(f (z), . . . , f (zkd−1)
)T

satisﬁes an equation of the form (3.23.2) with A(z) a companion matrix. Conversely,
iterating an equation of the form (3.23.2), and using the invertibility of A(z), it follows
that each fi(zkj ) is contained in the ﬁnite-dimensional K(z)-vector space spanned by
f1(z), . . . , fd(z). Hence the power series f1(zkj ), j ≥ 0, are linearly dependent over K[z].

3.1.2. Analytic properties. Let us assume that K = Q. If f (z) ∈ QJzK is a k-Mahler
function, then there exists a number ﬁeld K with f (z) ∈ KJzK. This is so because
all suﬃciently high coeﬃcients of f (z) are determined recursively by lower ones (see
[Dum93Dum93, Chapitre 3.2.2] or [AF18AF18]). Let v be a place of K and |·|v be an absolute value
associated with v. We let Kv denote the completion of K with respect to the absolute
value |·|v. We also let Cv denote the completion of the algebraic closure of Kv and K the
algebraic closure of K in Cv. Recall that Cv is both algebraically closed and complete.
The power series f (z) is analytic in a neighborhood of 0 in Cv (see, for instance, [Dum93Dum93,
Chapitre 3.3]). The Mahler equation then implies that f (z) is meromorphic in the open
unit disk B|·|v(0, 1) in Cv.

3.2. Automatic and regular power series. We recall the notion of k-automatic and
k-regular sequences. For more background see Allouche and Shallit [AS03aAS03a] or Berstel
and Reutenauer [BR11BR11, Chapter 5].
A sequence (an)n≥0 is k-automatic if there exists a ﬁnite automaton that, given as
input the base k representation of n, reaches an output state labeled by an. Equivalently,
the sequence (an)n≥0 is k-automatic if and only if its k-kernel is a ﬁnite set.

Deﬁnition 3.3. Let a := (an)n≥0 be a sequence with values in a set S. The k-kernel of
a is { (aken+r)n≥0 : e ∈ Z≥0, 0 ≤ r ≤ ke − 1 }.

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 9

Let us now restrict to sequences taking values in the ﬁeld K. Then a sequence (an)n≥0
is said to be k-regular if its k-kernel is contained in a ﬁnite-dimensional vector subspace
of the K-vector space of all K-valued sequences. Obviously k-automatic sequences are
k-regular. A k-regular sequence is k-automatic if and only if it takes only ﬁnitely many
values [AS03aAS03a, Theorem 16.1.5]. There are several other characterizations of k-regular
sequences [AS03aAS03a, Theorems 16.1.3 and 16.2.3]. We recall one characterization that is
relevant for our purpose.

Deﬁnition 3.4. A linear representation on the alphabet Σk is a triple (u, µ, v) where
u ∈ K 1×d, v ∈ K d×1, and µ : Σ∗
k → K d×d is a monoid homomorphism (d ∈ Z≥0). The
linear representation is minimal if the dimension d is minimal amongst all d′ ≥ 0 and
d′-dimensional linear representations (u′, µ′, v′) such that uµ(w)v = u′µ′(w)v′ for all
w ∈ Σ∗
k. Equivalently, uµ(Σ∗
k) spans K 1×d and µ(Σ∗
k)v spans K d×1.

Theorem 3.5. Let (an)n≥0 be a sequence taking values in K. The following statements
are equivalent.

(a) The sequence (an)n≥0 is k-regular.
(b) There exists a (minimal) linear representation (u, µ, v) on the alphabet Σk such that
a[w]k = uµ(w)v for all words w ∈ Σ∗
k.

Proof. The result is proved in [AS03aAS03a, Theorem 16.2.3]. □

A power series f (z) = ∑∞
n=0 anzn ∈ KJzK is said to be k-automatic, respectively
k-regular if the sequence (an)n≥0 is k-automatic, respectively k-regular.

3.3. Becker power series. The connection between k-regular sequences in the sense of
Allouche and Shallit and coeﬃcients of k-Mahler power series was studied by Becker, who
proved that k-regular power series are k-Mahler [Bec94Bec94, Theorem 1]. He also showed
that the converse is false in general: a k-Mahler power series need not be k-regular
[Bec94Bec94, Proposition 1]. However, he did obtain a partial converse. This motivates the
next deﬁnition.

Deﬁnition 3.6. A power series f (z) ∈ KJzK is a k-Becker function (or, in short, k-
Becker) if there exist a positive integer d and polynomials p1(z), . . . , pd(z) ∈ K[z], not
all zero, such that
 f (z) = p1(z)f (zk) + · · · + pd(z)f (zkd) .

Theorem 3.7 ([Bec94Bec94, Theorem 2]). If f (z) = ∑∞
n=0 anzn ∈ QJzK is a k-Becker power
series, then it is k-regular.

In view of these results, one may also ask for a precise characterization of k-regular
power series in terms of k-Becker power series. This gives rise to a conjecture of Becker,
recently settled in [BCCD19BCCD19], and discussed in Section 1010. For Mahler functions, there
exists the following useful decomposition due to Dumas.

Theorem 3.8 ([Dum93Dum93, Théorème 31, p.153]). Let f (z) ∈ KJzK be k-Mahler satisfying
an equation
 p0(z)f (z) + p1(z)f (zk) + · · · + pd(z)f (zkd) = 0

10 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

with p0(z), . . . , pd(z) ∈ K[z] and p0(0) = 1. Then

f (z) = g(z)
∏∞
i=0 p0(zki) ,

where g(z) ∈ KJzK is a k-Becker power series.

3.4. The Mahler denominator. As is already hinted at by Becker’s result, the poly-
nomial p0(z) in a Mahler equation (1.11.1) will play a prominent role in our arguments.
This prompts the following deﬁnition.

Deﬁnition 3.9. Let f (z) ∈ KJzK be a k-Mahler power series, and let

I = { p(z) ∈ K[z] : p(z)f (z) ∈
 ∞∑

i=1 K[z]f (zki) } .

The k-Mahler denominator of f (z) is the unique generator d(z) ∈ K[z] of the ideal I,
with the lowest non-zero coeﬃcient of d(z) being 1.

Since K[z] is a principal ideal domain, there indeed exists such a generator. Observe
that f (z) is k-Becker if and only if d(z) ≡ 1. It is tempting to hope that the k-Mahler
denominator is equal to the polynomial p0(z) in the minimal k-Mahler equation, that is
the equation p0(z)f (z) + p1(z)f (zk) + · · · + pd(z)f (zkd) = 0
with p0(z)pd(z) ̸= 0, minimal d, and coprime p0(z), . . . , pd(z). While this is often the
case, in general this is not so. See Example 3.103.10 for a counterexample. By deﬁnition
d(z) divides p0(z). It is tempting to hope that, to determine the types of roots of d(z),
it suﬃces to consider those of p0(z). Unfortunately, this hope is also thwarted by the
following example.

Example 3.10. The equation

(z − 1/2)f (z) − (z − 1/8)(z3 − 1/2)f (z3) = 0

has only one non-zero solution (up to a scalar) and is minimal with respect to this
solution. However, this solution is k-regular because

f (z) = (z − 1/8)(z2 + 1/2z + 1/4)(z9 − 1/2)f (z9) .

The expected pole at 1/2 disappears after one iteration of the equation.

We will see with Theorems 6.16.1 and 7.17.1 that locating the roots of the k-Mahler denom-
inator provides a characterization of those k-Mahler functions with h(an) ∈ O(log2 n)
and with h(an) ∈ O(log n). However, given a Mahler function with h(an) ∈ O(log n),
its Mahler denominator is irrelevant in determining whether h(an) ∈ O(log log n) or
h(an) ∈ O(1). For instance, all the three following 2-regular functions

∞∏

n=0
(1 − z2n) ,
 ∞∑

n=0 bnzn , ( 1
1 − z
 )2 ,

where we let bn denote the number of 0’s in the binary expansion of n (with b0 = 1), have
a trivial Mahler denominator (i.e., d(z) = 1). However, their coeﬃcients have height in
O(1), O ∩ Ω(log log n), and O ∩ Ω(log n), respectively.

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 11

4. Background about Mahler’s method

Let us consider a linear k-Mahler system:

(4.1)
 



f1(z)
...
fd(z)



 = A(z)
 



f1(zk)
...
fd(zk)





where A(z) is a matrix in GLd(Q(z)) and f1(z), . . . , fd(z) ∈ QJzK. There exists a number
ﬁeld K such that the fi(z)’s belong to KJzK and A(z) ∈ GLd(K(z)). Let v be a place
of K and |·|v be an absolute value associated with v. As before, we let Kv denote the
completion of K with respect to the absolute value |·|v. We also let Cv denote the
completion of the algebraic closure of Kv and K the algebraic closure of K in Cv.

Deﬁnition 4.1. A point α ∈ Cv is called singular with respect to (4.14.1) if there exists
a non-negative integer n such that αkn is a pole of one of the coeﬃcients of the matrix
A(z) or of the matrix A−1(z). We say that α is regular otherwise, that is, α is regular
if both A(αkn) and A−1(αkn) are well-deﬁned for every non-negative integer n.

We recall that the power series f1(z), . . . , fd(z) are meromorphic in the open unit
disc of Cv and analytic in some neighborhood of the origin. Moreover, if α is a regular
point such that |α|v < 1, then the functions f1(z), . . . , fd(z) are well-deﬁned at α. We
also recall that given a ﬁeld K, and elements a1, . . . , am in some ﬁeld extension of K,
the notation tr.degK(a1, . . . , am) stands for the transcendence degree over K of the ﬁeld
extension K(a1, . . . , am).

Theorem 4.2. Let f1(z), . . . , fd(z) ∈ KJzK be related by a Mahler system of the form
(4.14.1). Let α ∈ K, 0 < |α|v < 1 be a regular point with respect to this system. Then

tr. degK (f1(α), . . . , fd(α)) = tr. degK(z)(f1(z), . . . , fd(z)) .

In the case where |·|v is the usual absolute value on C, this classical result is due to
Nishioka [Nis90Nis90]. The proof of Nishioka is based on some techniques from commutative
algebra introduced in the framework of algebraic independence by Nesterenko in the late
Seventies. Recently, Fernandes [Fer18Fer18] observed that Theorem 4.24.2 can also be deduced
from a general algebraic independence criterion due to Philippon [Phi86Phi86, Phi92Phi92]. This
allows her to extend Nishioka’s theorem in the framework of function ﬁelds of positive
characteristic. Using the fact that the criteria obtained by Philippon also apply to any
absolute value associated with a place of a number ﬁeld (see for instance Theorem 2.11
in [Phi86Phi86]), we can argue exactly as in the proof of Theorem 1.3 of [Fer18Fer18] to prove
Theorem 4.24.2.

Theorem 4.3. Let f1(z), . . . , fd(z) ∈ KJzK be related by a Mahler system of the form
(4.14.1). Let α ∈ K, 0 < |α|v < 1 be a regular point for this system. Then for all
homogeneous polynomials P (X1, . . . , Xd) ∈ K[X1, . . . , Xd] such that

P (f1(α), . . . , fd(α)) = 0 ,

there exists Q(z, X1, . . . , Xd) ∈ K[z, X1, . . . , Xd], homogeneous in X1, . . . , Xd, such that

Q(z, f1(z), . . . , fd(z)) = 0

12 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

and
 Q(α, X1, . . . , Xd) = P (X1, . . . , Xi).

Proof. In the case where |·|v is the usual absolute value on C, this result is due to
Adamczewski and Faverjon in [AF17AF17, Theorem 1.4]. It is obtained as a consequence
of the main result of Philippon in [Phi15Phi15], which itself is based on Nishioka’s theorem.
The strategy to deduce this result from Nishioka’s theorem is detailed in [AF17AF17], see
Proposition 3.1. The arguments are based on basic facts from commutative algebra that
also apply to our more general framework. The two main ingredients that we have to
be careful about are the following ones.

(i) A result by Krull saying that if p is a homogeneous ideal in K[z, X0, . . . , Xd] that is
absolutely prime, then for all but ﬁnitely many α ∈ K, the ideal evα(p) is a prime
ideal of K[X0, . . . , Xd]. Here, we let evα : K[z] ↦→ K denote the evaluation map at
z = α. See [Kru48Kru48].
(ii) The fact that the ﬁeld extension L := K(z)(f1(z), . . . , fd(z)) is regular, which means
that an element of L is algebraic over K(z) if and only if it belongs to K(z).

We can use (i) in our framework for Krull proved his result for any base ﬁeld K.
To prove that (ii) also holds true in our framework, we need to know that a k-Mahler
function in KJzK is either rational or transcendental over K(z). There are several proofs
for this result. For instance, Theorem 5.1.7 in [Nis96Nis96] provides a proof in the case where
K is any ﬁeld of characteristic 0. Then we can argue exactly as in the proof of Lemma
3.2 in [AF17AF17] to deduce that the ﬁeld extension K(z)(f1(z), . . . , fd(z)) is regular. □

As a corollary of Theorem 4.34.3, we deduce the following result.

Corollary 4.4. Let f1(z), . . . , fd(z) ∈ KJzK be related by a Mahler system of the form
(4.14.1). Let us assume that f1(z), . . . , fd(z) are linearly independent over K(z). Then
there exists a real number r, 0 < r < 1, such that for every α ∈ K with 0 < |α|v < r,
the numbers f1(α), . . . , fd(α) are well-deﬁned and linearly independent over K.

Proof. We ﬁrst observe that if r is small enough, then α is a regular point with respect
to (4.14.1) and the numbers f1(α), . . . , fd(α) are thus well-deﬁned. Then the result follows
directly from Theorem 4.34.3. □

5. Generic upper bound

To prove (1)(1) of Theorem 1.11.1, giving a general upper bound on h(an) for a Mahler
function f (z) = ∑∞
n=0 anzn ∈ QJzK, we use a classical recursion for the sequence (an)n≥0
that is deduced from the Mahler equation. Since this is somewhat lengthy and the proof
of the upper bound for h(an) in case (2)(2) of Theorem 1.11.1, where we assume h(an) ∈ o(n),
works similarly, we establish both these bounds at the same time.
We need the following lemma. For archimedean absolute values, a more general result
for ﬁnitely generated semigroups of matrices can be found in [Bel05Bel05].

Lemma 5.1. Let d be a positive integer. Let |·| be an absolute value on Q, and let ∥·∥
be an operator norm on Qd×d with respect to |·|. Let A ∈ Qd×d be a matrix such that

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 13

|λ| ≤ 1 for every eigenvalue λ of A. Then

∥A
n∥ ∈
 {O(nd−1) if |·| is archimedean,
O(1) if |·| is non-archimedean.

Proof. It suﬃces to show the claim for a Jordan block λ + N ∈ Q
s×s where s ≤ d, where
|λ| ≤ 1, and where N is the s × s-matrix with ones on the superdiagonal and zeroes
everywhere else. Then N i is the matrix that has ones on the ith superdiagonal and
zeroes everywhere else, with N i = 0 for i ≥ s. Thus

(λ + N )
n =
 s−1∑

i=0
 (n
i
 )
λ
n−iN i for n ≥ s.

Now ∥(λ + N )n∥ ≤ C∣
∣
( n
s−1
)∣
∣ for some constant C, and the claim follows. □

Proposition 5.2. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be a k-Mahler function. Then the
following properties hold.

(1) One has h(an) ∈ O(n).
(2) Suppose in addition that all roots of the k-Mahler denominator of f (z) are contained
in {0} ∪ U. Then h(an) ∈ O(log2 n).

Proof. We may assume f (z) ̸= 0. The series f (z) satisﬁes a k-Mahler equation

p0(z)f (z) = p1(z)f (zk) + · · · + pd(z)f (zkd)

with p0(z) = d(z) the k-Mahler denominator and d ≥ 1. Extend the sequence an to
rational indices by setting ar = 0 for all r ∈ Q ∖ Z≥0. Let s = max{ deg pi(z) : i ∈
0, . . . , d }. Let p0(z) = zm(1 + α1z + · · · + αs−mzs−m) with α1, . . . , αs−m ∈ Q, and,
for i ∈ {1, . . . , d}, let pi(z) = ∑s
j=0 βi,jzj with βi,j ∈ Q. Comparing coeﬃcients in the
Mahler equation, we have

an−m +
 s−m∑

j=1 αjan−m−j =
 d∑

i=1
 s∑

j=0 βi,ja n−j
ki for n ∈ Z.

Shifting the indices by m, we obtain

(5.1) an =
 s−m∑

j=1 −αjan−j +
 d∑

i=1
 s∑

j=0 βi,ja n+m−j
ki for n ∈ Z.

If n > m, then n > (n + m)/2 ≥ (n + m − j)/ki for i ≥ 1 and j ≥ 0. Thus, Equation (5.15.1)
allows the recursive computation of an for n > m from a0, . . . , am. We now write this
as a matrix equation. For i ∈ {0, . . . , d}, let

(5.2) ai(n) :=
 






 an/ki
a(n−1)/ki
...
a(n−s)/ki
 





 .

14 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

Let A, B1, . . . , Bd ∈ Q(s+1)×(s+1) be given by

Bi =
 






βi,0 βi,1 . . . βi,s
0 0 . . . 0
... ... . . . ...
0 0 . . . 0
 




 and A = ( −α 0
Is×s 0s×1
) ,

where α = (α1, . . . , αs−m, 0, . . . , 0) ∈ Q1×s, where Is×s is the s × s identity matrix,
and 0s×1 is the s × 1 matrix containing zeroes. The characteristic polynomial of A is
zs+1 + α1zs + · · · + αs−mzm+1 = zm+s+1p0(1/z) ∈ Q[z].
Now
 a0(n) = Aa0(n − 1) +
 d∑

i=1 Biai(n + m) for n > m.

Fix n0 > m. Recursively substituting for a0(n − j), for n ≥ n0, we get

a0(n) = A
n−n0a0(n0) +
 n−n0−1∑

j=0
 d∑

i=1 A
jBiai(n + m − j).

The recursion formula for (an)n≥0 implies that there is a number ﬁeld K containing
all αi, βi,j and an for n ≥ 0. For each place v of K, let |·|v be the corresponding
absolute value and let ∥·∥v be the induced maximum norm. We also write ∥·∥v for the
operator norm on K (s+1)×(s+1). Let εv(n) = n if v is archimedean, and εv(n) = 1 if v is
non-archimedean. Then

(5.3) ∥a0(n)∥v ≤ εv(dn) · max {
∥A
n−n0∥v · ∥a0(n0)∥v, ∥A
j∥v · ∥Bi∥v · ∥ai(n + m − j)∥v }

where i ∈ {1, . . . , d} and j ∈ {0, . . . , n − n0 − 1}. Let S be the ﬁnite set consisting
of all places v that are archimedean or for which ∥A∥v > 1, or |an|v > 1 for some
n ∈ {0, . . . , n0}, or ∥Bi∥v > 1 for some i ∈ {1, . . . , d}. Note that, for v ̸∈ S, also
∥An∥v ≤ ∥A∥n
v ≤ 1 for all n ≥ 1. If v ̸∈ S, then, by induction, the bound in (5.35.3) implies
|an|v ≤ ∥a0(n)∥v ≤ 1 for all n ≥ n0. Therefore

h(an) = log ∏

v∈S max{1, |an|v}.

To show the claims, it suﬃces to obtain suitable bounds on |an|v for v ∈ S. We ﬁrst
prove the bound in (1).
Let v ∈ S. We show |an|v ≤ cn for some c ∈ R≥1 and all n ≥ 1. First enlarge n0 > m
and pick c0 ∈ R≥1 so that dnc1+m/2 ≤ cn/6 for all c ∈ R≥c0 and n ≥ n0. Let c ∈ R≥c0
be suﬃciently large so that |an|v ≤ c for all n ∈ {1, . . . , n0} and so that ∥Bi∥v ≤ c for
all i ∈ {1, . . . , d}. Enlarging c further, also suppose ∥A∥v ≤ c1/3, so that ∥An∥v ≤ cn/3.
We proceed by induction on n. For 1 ≤ n ≤ n0 the claim is true by choice of c. For
n > n0, the inequality (5.35.3) gives

∥a0(n)∥v ≤ εv(dn) · c
(n−n0)/3 · max {∥a0(n0)∥v, ∥Bi∥v · ∥ai(n + m − j)∥v},

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 15

where i ∈ {1, . . . , d} and j ∈ {0, . . . , n − n0 − 1}. By induction hypothesis, we can use
(5.25.2) to estimate ∥ai(n + m − j)∥v ≤ c(n+m)/k ≤ c(n+m)/2, and therefore

∥a0(n)∥v ≤ dn · c
(n−n0)/3 · c · c
(n+m)/2 = dnc
1+m/2 · c
−n0/3 · c
5n/6 ≤ c
n.

Thus |an|v ≤ cn, as claimed.
To show (2), we now assume in addition that all roots of p0(z) are contained in {0}∪U.
Let v ∈ S. We show that there exists c ∈ R≥1 such that |an|v ≤ nc log n for all suﬃciently
large n. To this end, ﬁrst note that we may choose c0 ∈ R≥1 and enlarge n0 > m so
that dc3ns+1 ≤ nc log(n) for all n ≥ n0 and c ≥ c0. Now let c ∈ R≥c0 be suﬃciently large
so that |an|v ≤ c for all n ∈ {1, . . . , n0} and ∥Bi∥v ≤ c for all i ∈ {1, . . . , d}. By our
assumption on the roots of p0(z), all the eigenvalues of A are contained in {0} ∪ U. Thus
∥An∥v ∈ O(ns) by Lemma 5.15.1, and we can also assume ∥An∥v ≤ cns for n ≥ 1, enlarging
c if necessary.
Since k ≥ 2 > 1 + m/n0, enlarging c further, we may also assume

c(log k − log(1 + m/n0)) > s + 1

and even dc2 ≤ nc(log k−log(1+m/n0))−(s+1)
0 . Then dc2 ≤ nc(log k−log(1+m/n))−(s+1) for all
n ≥ n0.
We show ∥a0(n)∥v ≤ nc log n for all n ≥ n0 by induction. Let n ≥ n0. The bound (5.35.3)
gives
 ∥a0(n)∥v ≤ εv(dn)cns · max {
∥a0(n0)∥v, ∥Bi∥v · ∥ai(n + m − j)∥v}
,

where i ∈ {1, . . . , d} and j ∈ {0, . . . , n − n0 − 1}. By induction hypothesis, we can use
(5.25.2) to estimate
 ∥ai(n + m − j)∥v ≤ max {c, ( n + m
k
 )c log ( n+m
k )}
.

With the latter bound of the maximum,

∥a0(n)∥v ≤ dcns+1 · c · ( n + m
k
 )c log ( n+m
k )
 ≤ dc
2ns+1+c log ( n+m
k )

≤ dc
2ns+1+c log(n)+c log (1+ m
n )
−c log(k) ≤ nc log(n);

in case ∥ai(n + m − j)∥v ≤ c we have

∥a0(n)∥v ≤ dc
3ns+1 ≤ nc log(n). □

We have thus established the general growth bound for the coeﬃcients of a Mahler
function: the height of the nth coeﬃcient is at most linear in n.

6. First gap: characterization of totally analytic Mahler functions

In this section, we characterize k-Mahler functions f (z) = ∑∞
n=0 anzn ∈ QJzK with
h(an) ∈ o(n). Let f (z) ∈ QJzK be an M -function. There exists a number ﬁeld K such
that f (z) ∈ KJzK, and for every place v of K, we may consider f (z) as a power series
over the algebraic closure Cv of the completion Kv. Then f (z) has a positive radius of
convergence, and it is meromorphic in the open unit disk of Cv. Moreover, for all but
ﬁnitely many places of K, the radius of convergence of f (z) is equal to 1. Hence, an

16 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

M -function is globally analytic. We say that f (z) is totally analytic if, for every place v
of K, f (z) is analytic in the open unit disk of Cv.

Theorem 6.1. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be a k-Mahler function. The following
statements are equivalent.
(a) We have h(an) ∈ o(n).
(b) Every non-zero root of the k-Mahler denominator of f (z) belongs to U (i.e., is a
root of unity).
(c) The power series f (z) is totally analytic.
(d) We have h(an) ∈ O(log2 n).

The crucial step here lies in showing that all roots of the k-Mahler denominator are
contained in {0} ∪ U. This relies on the deep results on Mahler’s method by Nishioka,
Philippon, Fernandes, as well as by Adamczewski and Faverjon that were recalled in
Section 44. But ﬁrst we need the following easy lemma.

Lemma 6.2. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be a power series that is not a polynomial.
If h(an) ∈ o(n), then f (z) has radius of convergence 1 for every absolute value of Q.

Proof. Fix an absolute value |·| on Q, and let

ρ = ( lim sup
n→∞
 n
√
|an|)−1 ∈ R≥0 ∪ {∞}

be the radius of convergence of f (z).
We show ρ = 1 by contradiction. Suppose ﬁrst ρ > 1. Choose ρ′ ∈ R>0 with with
1 < ρ′ < ρ. Since lim supn→∞ n√
|an| = 1/ρ < 1/ρ′, we have |an| ≤ (1/ρ′)n for all
suﬃciently large n. Since f is not a polynomial, there exist inﬁnitely many such n with
an ̸= 0, and for these |a−1
n | ≥ (ρ′)n. One has h(an) = h(a−1
n ) as a consequence of the
product formula. It follows that h(an) = h(a−1
n ) ≥ log|a−1
n | ≥ n log(ρ′), in contradiction
to our assumption.
Suppose now ρ < 1, and choose ρ < ρ′ < 1. Then, for all n0 ≥ 0, there exists an
n ≥ n0 such that |an| ≥ (1/ρ′)n. Hence h(an) ≥ log|an| ≥ n log(1/ρ′) again yields a
contradiction. □

We also require the notion of Cartier operators in the next proof.

Deﬁnition 6.3. For every r ∈ Σk, we deﬁne a Cartier operator ∆r : QJzK → QJzK by

∆r( ∞∑

n=0 anzn) =
 ∞∑

n=0 akn+rzn .

Note that, if p(z) ∈ Q[z], then deg(∆r(p(z))) ≤ (deg p)/k. Moreover, if j ≥ 1, then a
short computation yields

∆r(
p(z)f (zkj )
) = ∆r(p(z)) · f (zkj−1).

Proposition 6.4. Let f (z) ∈ QJzK be k-Mahler and let d(z) ∈ Q[z] be its k-Mahler
denominator. If λ ∈ Q is a root of d(z), and |·| is an absolute value on Q with 0 < |λ| < 1,
then the radius of convergence of f (z) with respect to this absolute value is strictly less
than 1.

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 17

Proof. Let us ﬁrst consider a minimal homogeneous equation associated with f (z):

(6.1) p0(z)f (z) + p1(z)f (zk) + · · · + pd(z)f (zkd) = 0 .

By minimal, we mean that p0(z)pd(z) ̸= 0, that d is minimal, and that p0(z), . . . , pd(z) ∈
Q[z] are relatively prime. If f (z) = 0, then we can take d = 0 and p0(z) = 1. Thus also
d(z) = 1 and the claim is trivially true. We may assume f (z) ̸= 0, so that d ≥ 1.
As in Section 44, we can assume that there exists a number ﬁeld K containing λ and
all coeﬃcients of f (z) as well as the coeﬃcients of the polynomials p0(z), . . . , pd(z).
Further, |·| on K arises from a place v of K, and Cv is the algebraic closure of the
completion Kv, with K denoting the algebraic closure of K inside Cv.
We claim that f (z), . . . , f (zkd−1) are linearly independent over K(z). By way of
contradiction, suppose that this is not the case. Then there exist q0(z), . . . , qd−1(z) ∈
K[z], not all zero, such that

q0(z)f (z) + · · · + qd−1(z)f (zkd−1) = 0.

Since the coeﬃcients of q0(z), . . . , qd(z) are all algebraic over Q, we can assume q0(z),
. . . , qd(z) ∈ Q[z]. Let t ∈ {0, . . . , d−1} be minimal with qt(z) ̸= 0, say qt(z) = ∑M
j=m bjzj

with bm, bM ̸= 0. Let m = ∑∞
ν=0 kν mν with mν ∈ Σk be the base-k expansion of m (with
all but ﬁnitely many mν being zero). Setting ∆ = ∆mt ◦ · · · ◦ ∆m0, we see ∆(qt(z)) ̸= 0.
Then ∆(qt(z))f (z) + · · · + ∆(qd−1(z))f (zkd−1−t ) = 0

is a k-Mahler equation for f (z), contradicting the minimality of d. Therefore f (z),
. . . , f (zkd−1) must be linearly independent over K(z), as claimed.
Now 




 f (z)
...
f (zkd−1)





 = A(z)
 




 f (zk)
...
f (zkd)







with
 A(z) =
 









− p1(z)
p0(z) − p2(z)
p0(z) · · · − pd−1(z)
p0(z) − pd(z)
p0(z)
1 0 · · · 0 0

0 1 . . . ... ...
... . . . . . . 0 ...
0 · · · 0 1 0
 









 ∈ GLd(K(z)).

By Corollary 4.44.4, we have that

f (λ
kn), f (λkn+1), . . . , f (λkn+d−1)

are linearly independent over K, as soon as n is large enough, say n ≥ n0.
Now, iterating Equation (6.16.1), we obtain an equation of the form

(6.2) r0(z)f (z) + r1(z)f (zkn0 ) + · · · + rd(z)f (zkn0 +d−1) = 0 ,

where we assume without any loss of generality that r0(z), . . . , rd(z) ∈ K[z] are relatively
prime. We claim that f (z) has a pole at λ. Let us assume by contradiction that f (z) is

18 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

well-deﬁned at λ. Since d(λ) = 0, it follows that r0(λ) = 0 and we get that

r1(λ)f (λ
kn0 ) + · · · + rd(λ)f (λkn0+d−1) = 0 .

Since f (λkn0 ), . . . , f (λkn0+d−1) are linearly independent over K, all the ri(z) should
vanish at λ, contradicting the fact that they are relatively prime. Hence, f (z) has a pole
at λ and its radius of convergence is therefore less than 1. □

We now have the ingredients to characterize Mahler functions with h(an) ∈ o(n).

Proof of Theorem 6.16.1. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be k-Mahler.
(a)(a) ⇒ (c)(c) Suppose h(an) ∈ o(n). By Lemma 6.26.2 the series f (z) has radius of conver-
gence at least 1 with respect to every absolute value |·| on Q.
(c)(c) ⇒ (b)(b) Suppose now f (z) has radius of convergence at least 1 with respect to every
absolute value |·| on Q. Let d(z) ∈ Q[z] be the k-Mahler denominator of f (z). Suppose
there exists λ ∈ Q ∖ {0} with d(λ) = 0 such that λ is not a root of unity. By Kronecker’s
Theorem there exists an absolute value |·| on Q for which |λ| < 1. By Proposition 6.46.4,
the series f (z) has radius of convergence strictly less than 1 for this absolute value, a
contradiction.
(b)(b) ⇒ (d)(d) Suppose all roots of the k-Mahler denominator d(z) ∈ Q[z] of f (z) are
contained in {0} ∪ U. Then h(an) ∈ O(log2 n) by (2)(2) of Proposition 5.25.2.
(d)(d) ⇒ (a)(a) Clearly h(an) ∈ O(log2 n) implies h(an) ∈ o(n). □

7. Second gap: characterization of regular Mahler functions

In this section, we characterize Mahler functions f (z) = ∑∞
n=0 anzn ∈ QJzK with
h(an) ∈ o(log2 n). The following result also proves Case (b)(b) of Theorem 1.21.2.

Theorem 7.1. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be a k-Mahler function. The following
statements are equivalent.
(a) We have h(an) ∈ o(log2 n).
(b) Every non-zero root of the k-Mahler denominator of f (z) belongs to Uk.
(c) The power series f (z) is k-regular.
(d) We have h(an) ∈ O(log n).

We already know that, if h(an) ∈ o(log2 n), then every root ζ of the k-Mahler denom-
inator d(z) of f (z) is contained in {0} ∪ U. The brunt of the work in this section lies in
showing ζ ∈ {0} ∪ Uk, that is, if ζ ̸= 0, then ζ kj ̸= ζ for all j > 0. This requires a careful
analysis of the asymptotics of f (z) at such a hypothetical root of d(z) to establish a
contradiction.
We start with some estimates.

Lemma 7.2. Let f (z) = ∑∞
n=0 anzn ∈ RJzK be a power series with non-negative coef-
ﬁcients. Suppose there exists c ∈ R>0 with an ≤ nc log n for all suﬃciently large n. Let
c′, ε ∈ R>0 with c′ > 2c. Then there exists t0 ∈ [0, 1) such that

∞∑

n=⌈m log2 m⌉ antn < ε for all t ∈ [t0, 1) and m ≥ c′

1 − t ·

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 19

Proof. By assumption, for large n,

antn ≤ exp(c log2 n + n log t).

We will show that, for suﬃciently large m (ensured by choice of t0) and n ≥ m log2 m,

(7.1) c log2 n + n log t ≤ 1
2 n log t.

We ﬁrst show how to conclude the proof using Equation (7.17.1). Then antn ≤ tn/2 and

∞∑

n=⌈m log2 m⌉ antn ≤ t⌈m log2 m⌉/2

1 − √t = (1 + √t)t⌈m log
2 m⌉/2

1 − t < 2t⌈m log2 m⌉/2

1 − t ·

We need to bound the right side by a constant. Using m ≥ c′/(1 − t) and t ∈ [0, 1), we
have

(7.2) log
 ( 2t⌈m log2 m⌉/2

1 − t
 )
 ≤ log 2 + c′ log t
2(1 − t) log2 ( c′

1 − t
 ) − log(1 − t).

Recall limt→1 log t/(1 − t) = −1 and log2(c′/(1 − t)) ∼ log2(1 − t) for t → 1−. Hence
the right side of Equation (7.27.2) tends to −∞ as t → 1−. Choosing t0 ∈ [0, 1) suﬃciently
close to 1, therefore
∞∑

n=⌈m log2 m⌉ antn ≤ ε for t ∈ [t0, 1) and m ≥ c
′/(1 − t).

It remains to show the bound in Equation (7.17.1). The latter is equivalent to c log2 n +
1
2 n log t ≤ 0. Since log t ≤ t − 1 ≤ −c′/m, it suﬃces to show

(7.3) c log2 n − n c′

2m ≤ 0 for n ≥ m log2 m.

We ﬁrst show this for n = m log2 m. Now

c log2(m log2 m) − m(log2 m) c′

2m ∼ (c − c
′/2) log2 m

as a function in m for m → ∞, and c − c′/2 is negative by choice of c′. Thus, for
suﬃciently large m, we have c log2(m log2 m) − m(log2 m) c′
2m ≤ 0. We can ensure a large
enough m by choosing t0 ∈ [0, 1) suﬃciently close to 1.
Now, set g(n) := c log2 n and h(n) := n c′
2m . Then g′(n) = 2c log n
n , and hence

g′(m log2 m) = 2c log m + 2c log(log2 m)
m log2 m ∼ 2c
m log m ·

Thus, choosing m suﬃciently large, we may also ensure

g′(m log2 m) ≤ h
′(m log2 m) = c′

2m ·

Since g(n) is concave for n ≥ exp(1), this ensures g(n) ≤ h(n) for n ≥ m log2 m. This
proves Equation (7.17.1) and ends the proof of the lemma. □

20 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

Lemma 7.3. Let f (z) = ∑∞
n=0 anzn ∈ RJzK be a power series with non-negative coeﬃ-
cients. Let a ∈ R≥0 and b, c ∈ R>0. Assume that there exist a sequence (tj)j≥0 → 1 in
[0, 1) and m0 ∈ Z≥0 such that

f (tj) ≥ (1 − tj)
a exp(c log2 m)tmb
j for all j ≥ 0 and m ≥ m0.

Then there exist c′ ∈ R>0 and inﬁnitely many n ≥ 1 with an > exp(c′ log2 n).

Proof. Without any loss of generality we can assume that there exists a constant c′ > 2c
such that an ≤ exp(c′ log(n)2) for all suﬃciently large n. Indeed, otherwise the result
holds trivially. By the previous lemma, for all suﬃciently large j and m ≥ 3c′/(1 − tj),
we have ∞∑

n=⌈m log2 m⌉ antn
j ≤ 1 .

Let mj = ⌈3c′/(1 − tj)⌉ and

Aj = log (
(1 − tj)
a exp(c log2 mj)tmj b
j )

= a log(1 − tj) + c log2 mj + mjb log tj .

Then, for suﬃciently large j,

⌊mj log2 mj ⌋∑

n=0 antn
j ≥ exp(Aj) − 1 .

Since ( 3c′

(1 − tj) + 1
)b log tj ≤ mjb log tj ≤ 3c′

(1 − tj) b log tj ,

and ((log tj)/(1−tj))j≥0 → −1, we ﬁnd (mjb log tj)j≥0 → −3c′b. Since log2(1/(1−tj )) =
log2(1 − tj) and therefore log2 mj ∼ log2(1 − tj), we see that Aj ∼ c log2 mj. Choosing
j suﬃciently large, we may assume
 Aj ≥ c
2 log2 mj .

Therefore, again restricting to large enough j for the last inequality,

⌊mj log
2 mj ⌋∑

n=0 antn
j ≥ exp(Aj) − 1 ≥ exp ( c
4 log2 mj ) .

By the pigeonhole principle, there exists 0 ≤ nj ≤ mj log2 mj such that

anj ≥ exp ( c
4 log2 mj)/(1 + mj log2 mj) .

Thus log anj ≥ c
4 log2 mj − log(mj log2 mj + 1) ∼ c
4 log2 mj .

We may assume log anj ≥ c
8 log2 mj. To ﬁnish, since nj ≤ mj log2 mj, we have

log2 nj ≤ log2(mj log2 mj) ∼ log2 mj .

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 21

We may take log2 nj ≤ 2 log2 mj, so that log anj ≥ c
16 log2 nj. Since log anj ≥ c
8 log2 mj
and (mj)j≥0 → ∞, also (nj)j≥0 → ∞. Thus there are in fact inﬁnitely many distinct
such nj. □

Lemma 7.4. Let ζ ∈ C with ζ k = ζ. Let p(z) ∈ C[z] with p(0) = 1 and p(ζ) ̸= 0. Then
there exists c ∈ R>0 such that, for all t ∈ [0, 1) with p(ζtkn) ̸= 0 for all n ≥ 0,

∣
∣
∣
∣
( ∞∏

n=0 p(ζtkn)

)−1∣
∣
∣
∣ > |1 − t|
c .

Proof. The proof is the same as the one of the lower bound in [AB17AB17, Lemma 9.5 and
Proposition 9.2]. Let α1, . . . , αs denote the roots of p(z) (with multiplicity). Then

p(z) = (1 − α
−1
1 z) · · · (1 − α
−1
s z) .

It suﬃces to show the claim for 1 − α
−1
1 z. Suppose t ∈ [0, 1] is such that ζtkn ̸= α1 for
all n ≥ 0. Then the inﬁnite product ∏∞
n=0(1 − α
−1
1 tkn)−1 converges, and
∣
∣
∣
∣
 ∞∏

n=0
 1
1 − α
−1
1 ζtkn
 ∣
∣
∣
∣ ≥
 ∞∏

n=0
 1
1 + |α
−1
1 |tkn ≥
 ∞∏

n=0 exp(−|α
−1
1 |tkn) .

Then, by [AB17AB17, Lemma 9.4],

∞∏

n=0 exp(−|α
−1
1 |tkn) ≥ exp ( − |α
−1
1 |(1 − 1/k)
−1 ∞∑

n=1
 tn

n
 ) = (1 − t)
 |α−1
1 |k

k−1 . □

Let B(λ, r) ⊆ C, respectively B(λ, r) ⊆ C, denote the open, respectively closed, disc
of radius r ∈ R≥0 with center λ ∈ C.

Lemma 7.5 (Special case of [AB17AB17, Lemma 10.2]). Let d ∈ Z>0, let ζ ∈ C ∖ {0} such
that ζ k = ζ, and let A : B(0, 1) → Cd×d be a continuous, matrix-valued function. Assume
that w(z) ∈ CJzKd satisﬁes the equation

w(λ) = A(λ)w(λk) for all λ ∈ B(0, 1) .

Assume also that the following properties hold.
(i) The coordinates of w(z) are analytic in B(0, 1).
(ii) The matrix A(ζ) is not nilpotent.
(iii) The set { w(λ) : λ ∈ B(0, 1) } is not contained in a proper vector subspace of Cd.
Then there exist c ∈ R>0 and a sequence (tj)j≥0 → 1 in [0, 1) such that

∥w(tj ζ)∥ > |1 − tj|
c for all j ≥ 0 .

Proof. This is [AB17AB17, Lemma 10.2] in the special case θ = 0. We do not assume w(z) to
be continuous in B(0, 1), but this assumption is never used in the proof and is therefore
superﬂuous. □

Lemma 7.6. Let b ∈ Z>0 and a, a′ ∈ R with a′ > a > 0. Then there exists t0 ∈ [0, 1)
such that (1 − t1/b)
a > (1 − t)
a′ for all t ∈ [t0, 1).

22 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

Proof. For t ∈ [0, 1) we have

1 − t = (1 − t1/b)
 b−1∑

i=0 ti/b ≤ b(1 − t1/b).

Moreover (1 − t)a′−a < 1/ba for t suﬃciently close to 1. Then

(1 − t1/b)
a ≥ (1 − t)a′

(1 − t)a′−aba > (1 − t)
a′ . □

Armed with these estimates, we can ﬁnally prove a further restriction on the roots of
the k-Mahler denominator. This is the key step in the current section. The arguments
are in many aspects very similar to those used by Adamczewski and Bell in [AB17AB17, §11].

Proposition 7.7. Let f (z) = ∑∞
n=0 anzn ∈ CJzK be a k-Mahler series that is analytic
in B(0, 1). Let ζ ∈ U with ζ kj0 = ζ for some j0 ≥ 1, and let l = kj0. Suppose there
exists an l-Mahler equation

p0(z)f (z) = p1(z)f (zl) + · · · + pd(z)f (zld),

with p0(z), . . . , pd(z) ∈ C[z] coprime, with p0(z)pd(z) ̸= 0, and such that p0(ζ) = 0.
Then there exist a, b, c ∈ R>0, m0, n0 ∈ Z≥0, and a sequence (tj)j≥0 → 1 in [0, 1)
such that
∣
∣
∣
∣
∣
 ∞∑

n=0 an+n0(ζtj)
n∣
∣
∣
∣
∣ ≥ (1 − tj)
a exp(b log2 m)tmc
j for all j ≥ 0 and m ≥ m0 .

Proof. Applying Lemma 3.13.1, there exist n0 ≥ 0 and q0(z), . . . , qd+1(z) ∈ C[z] such that
an0 ̸= 0 and
 f0(z) =
 ∞∑

n=0 an+n0zn

satisﬁes q0(z)f0(z) = q1(z)f0(zl) + · · · + qd+1f0(zld+1) ,

with q0(0) = 1, with q0(ζ) = 0, and with qi(ζ) ̸= 0 for some i ∈ {1, . . . , d + 1}.
Let νi ∈ Z≥0 be the order of vanishing of qi(z) at ζ. Deﬁne

r := min { νi + (i − 1)ν0
i : i ∈ 1, . . . , d + 1 } ∈ Q≥0 .

Since ν0 > 0 and νi = 0 for some i ∈ {1, . . . , d + 1}, we have r < ν0. Deﬁning

g(z) := f0(ζz)
 ∞∏

n=0
 q0(ζzln)
(1 − zln)r

we obtain

g(z) =
 d+1∑

i=1 ri(z)g(zli ) with ri(z) = qi(ζz) 1
(1 − z)r
 i−1∏

n=1
 q0(ζzln)
(1 − zln)r ∈ C(z) .

In the expression for ri(z), the denominator has roots at every ω ∈ C for which ωli−1 = 1.
If ω ̸= 1, then r < ν0 guarantees that ri(z) does not actually have a pole at ω. For ω = 1,

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 23

this is ensured by ir ≤ νi + (i − 1)ν0. Thus, all ri(z) are in fact polynomials. Moreover,
by choice of r, there exists an i0 ∈ {1, . . . , d + 1} such that ri0(1) ̸= 0.

Claim: There exist a ∈ R>0 and a sequence (tj)j≥0 → 1 in [0, 1) with

|g(tj)| ≥ (1 − tj)
a.

Proof of Claim. First we deal with the degenerate case in which g(z) is constant. Then
g(z) = g(0) and from the deﬁnition of g we see g(0) ̸= 0 since f0(0) ̸= 0 and q0(0) = 1.
Choosing a = 1, any sequence (tj)j≥0 → 1 in [0, 1) satisﬁes |g(tj )| > 1 − tj for suﬃciently
large j. From now on we may assume that g(z) is not constant.
We are going to apply Lemma 7.57.5. Denote by ∥·∥ the maximum norm with respect

to |·|. Let w(z) = (g(z), g(zl), . . . , g(zld )
)T and

A(z) =
 











r1(z) r2(z) . . . rd−1(z) rd(z) rd+1(z)
1 0 . . . 0 0 0
0 1 . . . 0 0 0
... 0 . . . ... ... ...
... ... . . . 1 0 0
0 0 . . . 0 1 0
 











 ∈ C(z)
(d+1)×(d+1).

Then w(z) = A(z)w(zl). The coordinates of A(z) are polynomials and hence of course
continuous. We verify the conditions of Lemma 7.57.5.
(i)(i) The coordinates of w(z) are analytic in B(0, 1) since g(z) is analytic in B(0, 1).
(ii)(ii) The characteristic polynomial of A(z) is yd+1 − r1(z)yd − · · · − rd+1(z) ∈ C(z)[y].
Since ri0(1) ̸= 0, the matrix A(1) is not nilpotent.
(iii)(iii) Suppose that S = { w(λ) : λ ∈ B(0, 1) } is contained in a proper subspace of Cd.
Then there exist α0, . . . , αd ∈ C, not all zero, such that α0g(λ) + · · · + αdg(λld) = 0 for
all λ ∈ B(0, 1). Since g(z) is analytic in B(0, 1) this forces α0g(z) + · · · + αdg(zld) = 0.
But then g(z) is constant by [AB17AB17, Lemma 7.9], a contradiction. Hence the set S is
not contained in a proper subspace of Cd.
Applying Lemma 7.57.5, there exist a ∈ R>0 and a sequence (tj)j≥0 → 1 in [0, 1) such
that ∥w(tj )∥ > (1 − tj)
a for all j ≥ 0 .
Restricting to a subsequence and making a substitution, we may assume that there exists
i ∈ [0, d] and b = li such that |g(tj )| > (1 − t1/b
j )a for j ≥ 0. Applying Lemma 7.67.6 and
replacing a by a slightly larger constant, we may actually take |g(tj )| > (1 − tj)a for all
j ≥ 0. □ (Claim)
By the result of Mahler, see Example (d)(d) in Section 22, there exists a constant c ∈ R>0
such that, for some m0 ≥ 0,

∞∏

n=0
(1 − tln
j )
−1 ≥
 ∞∑

n=m0 exp(c log2 n)tn
j .

Thus ∞∏

n=0
(1 − tln
j )
−1 ≥ exp(c log2 m)tm
j for all m ≥ m0 .

24 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

The lower bound for g(z) together with the fact that f0(z) is analytic in B(0, 1) implies
q0(ζtln
j ) ̸= 0 for all n ≥ 0. By Lemma 7.47.4, there exists a′ ∈ R>0 such that
∣
∣
∣
∣
 ∞∏

n=0
 (1 − tln
j )ν0

q0(ζtln
j )
 ∣
∣
∣
∣ > (1 − tj)
a′ for j large enough.

With b = ν0 − r > 0, we conclude, for m ≥ m0, that

|f0(tjζ)| = |g(tj)| · ∣
∣
∣
∣
 ∞∏

n=0
 (1 − tln
j )r

q0(ζtln
j )
 ∣
∣
∣
∣ > (1 − tj)
a+a′ exp(cb log2 m)tmb
j . □

Proposition 7.8. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be k-Mahler and suppose that h(an) ∈
o(log2 n). Then the roots of the k-Mahler denominator of f (z) are contained in {0} ∪ Uk.

Proof. Let d(z) be the k-Mahler denominator of f (z). Suppose that ζ ∈ Q ∖ {0} is such
that d(ζ) = 0. Then ζ ∈ U by Theorem 6.16.1. We have to show ζ kj ̸= ζ for all j ≥ 1.
Suppose to the contrary that ζ kj0 = ζ for some j0 ≥ 1. Let l = kj0. Then f (z) is also
l-Mahler by Lemma 3.23.2. Let p0(z), . . . , pd(z) ∈ Q[z] be coprime, with p0(z)pd(z) ̸= 0,
such that p0(z)f (z) = p1(z)f (zl) + · · · + pd(z)f (zld) .
Since this is also a k-Mahler equation for f (z), the k-Mahler denominator d(z) divides
p0(z), hence p0(ζ) = 0. Fix any embedding Q ֒→ C, and thereby an archimedean
absolute value on Q. We apply Proposition 7.77.7 to conclude that there exist a, b, c ∈ R>0,
m0, n0 ∈ Z≥0, and a sequence (tj)j≥0 → 1 in [0, 1) such that

|f0(ζtj)| ≥ (1 − tj)
a exp(b log2 m)tmc
j for all j ≥ 0 and m ≥ m0 ,

where f0(z) = ∑∞
n=0 an+n0zn. Since ∑∞
n=0|an+n0|tn ≥ |f0(ζt)| for t ∈ [0, 1), the condi-
tions of Lemma 7.37.3 are satisﬁed for ∑∞
n=0|an+n0|zn. Thus there exist c′ ∈ R>0 such that
|an| ≥ exp(c′ log2 n) inﬁnitely often. Thus h(an) ̸∈ o(log2 n); a contradiction. □

Once we know that all roots of the k-Mahler denominator of f (z) are contained in
{0}∪Uk it is not hard to show that f (z) is k-regular. This was shown by Dumas [Dum93Dum93,
Théorème 30]; see also [BCCD19BCCD19, Proposition 2]. We recall the proof.
Keep in mind that Uk consists of all roots of unity ζ for which ζ kj ̸= ζ for all j ≥ 1.
In particular, 1 ̸∈ Uk. By [AB17AB17, Proposition 7.8], the inﬁnite product

∞∏

n=0
(1 − ζ −1zkn)
−1

is k-regular for ζ ∈ Uk.

Proposition 7.9. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be a k-Mahler series and suppose that
h(an) ∈ o(log2 n). Then f (z) is a k-regular power series.

Proof. Since every polynomial is k-regular, and sums of k-regular sequences are k-regular,
it suﬃces to show the claim for ∑∞
n=0 an+n0zn for some n0 ≥ 0. By Lemma 3.13.1 we may
therefore assume d(0) = 1 for the k-Mahler denominator d(z) of f (z). By Proposition 7.87.8,
all roots of d(z) are contained in Uk. By Theorem 3.83.8 we can write

f (z) = g(z)
∏∞
n=0 d(zkn)

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 25

with a k-Becker series g(z). By Theorem 3.73.7, the series g(z) is k-regular. Because

∞∏

n=0
(1 − ζ −1zkn)
−1

is k-regular for ζ ∈ Uk, and products of k-regular series are k-regular, also f (z) is k-
regular. □

Allouche and Shallit [AS92AS92, Theorem 2.10] show |an| ∈ O(nc) for a C-valued k-regular
sequence. A similar argument bounds the height of the coeﬃcients.

Lemma 7.10. If f (z) = ∑∞
n=0 anzn ∈ QJzK is k-regular, then h(an) ∈ O(log n).

Proof. For n ∈ Z≥0, we recall that ⟨n⟩k ∈ Σ∗
k is the canonical base-k expansion of n. By
Theorem 3.53.5 there exists a linear representation (u, µ, v) (of some dimension d ∈ Z≥0)
such that an = uµ(⟨n⟩k)v for all n ∈ Z≥0. Moreover, using basic properties of the
logarithmic Weil height (see [Wal00Wal00, Chapter 3]), we deduce that h(uµ(w)v) ∈ O(|w|)
for w ∈ Σ∗
k. Noting that |⟨n⟩k| ∈ O(log n), we obtain h(an) ∈ O(log n). □

At this point, we are ready to prove Theorem 7.17.1.

Proof of Theorem 7.17.1. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be a k-Mahler function.
(a)(a) ⇒ (b)(b) Suppose h(an) ∈ o(log2 n). By Proposition 7.87.8 all roots of the k-Mahler
denominator of f (z) are contained in {0} ∪ Uk.
(b)(b) ⇒ (c)(c) Suppose that all roots of the k-Mahler denominator are contained in {0}∪Uk.
Then f (z) is k-regular by Proposition 7.97.9.
(c)(c) ⇒ (d)(d) Suppose f (z) is k-regular. Then h(an) ∈ O(log n) by Lemma 7.107.10.
(d)(d) ⇒ (a)(a) Clearly h(an) ∈ O(log n) implies h(an) ∈ o(log2 n). □

8. Third gap: word-convolution products of automatic sequences

In this section, we characterize Mahler functions f (z) = ∑∞
n=0 anzn ∈ QJzK with
h(an) ∈ o(log n). The arguments are similar to the ones used in [Bel05Bel05] and [BCH16BCH16].
As before, we actually prove a more extensive characterization involving a structural
property.
Before stating the main result of this section, we ﬁrst recall the deﬁnition of the
word-convolution product following [BCH16BCH16].

Deﬁnition 8.1. Given two sequences of complex numbers (a(n))n≥0 and (b(n))n≥0,
their word-convolution product is the sequence a ⋆w b deﬁned by

a ⋆w b(n) =
 s∑

j=0 a([i1 · · · ij]k)b([ij+1 · · · is]k) ,

where ⟨n⟩k = i1i2 · · · is ∈ Σ∗
k.

We also need the notion of tame semi-group of matrices.

Deﬁnition 8.2. Let d be a positive integer. A semigroup of matrices S ⊆ K d×d is tame,
if all eigenvalues of all matrices A ∈ S are contained in {0} ∪ U.

26 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

We are now ready to state the main result of this section. We already know that
a k-Mahler function with h(an) ∈ O(log n) is k-regular. The sequence of coeﬃcients
(an)n≥0 therefore has a minimal linear representation (u, µ, v) by Theorem 3.53.5.

Theorem 8.3. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be a k-Mahler function. The following
statements are equivalent.

(a) We have h(an) ∈ o(log n).
(b) For every minimal linear representation (u, µ, v) of (an)n≥0, the matrix semigroup
µ(Σ∗
k) is tame.
(c) The sequence (an)n≥0 is a Q-linear combination of word-convolution products of
k-automatic sequences.
(d) We have h(an) ∈ O(log log n).

Our ﬁrst goal is to use the additional restriction h(an) ∈ o(log n) to obtain a restriction
on the possible eigenvalues of the matrices µ(w). The following lemma is similar to
[Bel05Bel05, Lemma 2.3].

Lemma 8.4. Let (an)n≥0 be a k-regular sequence in Q, with a minimal linear represen-
tation (u, µ, v). Suppose h(an) ∈ o(log n). Then the ﬁnitely generated matrix semigroup
µ(Σ∗
k) is tame.

Proof. By deﬁnition of the linear representation, we have a[w]k = uµ(w)v for all w ∈ Σ∗
k.
Since [w]k ∈ O(k|w|) for all w ∈ Σ∗
k, our assumption on the sequence translates into
h(uµ(w)v) ∈ o(|w|).
Write d for the dimension of (u, µ, v). If d = 0, the claim is trivially true. Let
d > 0. Suppose there exist a word w ∈ Σ∗
k and λ ∈ Q ∖ {0} not a root of unity such
that λ is an eigenvalue of µ(w). Then there exists a non-zero vector v0 ∈ Qd×1 with
µ(w)v0 = λv0. By minimality of the linear representation, there exist w1, . . . , wd ∈ Σ∗
k
such that µ(w1)v, . . . , µ(wd)v form a basis of Q
d×1. Let α1, . . . , αd ∈ Q be such that
v0 = α1µ(w1)v + · · · + αdµ(wd)v. Again by minimality, the set { uµ(w′) : w′ ∈ Σ∗
k } spans
Q1×d. Therefore there exists w′ ∈ Σ∗
k such that uµ(w′)v0 ̸= 0.
Now d∑

i=1 αiuµ(w′wnwi)v = uµ(w′)µ(wn)v0 = λnuµ(w′)v0 ̸= 0.

Since λ is not a root of unity, there exists an absolute value |·| on Q with |λ| > 1. We
conclude that there exists an i ∈ {1, . . . d} with

|αiuµ(w′wnwi)v| ≥ |λ|
n · |uµ(w′)v0|
d

for inﬁnitely many n ≥ 0. Hence there exists c′ ∈ R>0 such that, for these n ≥ 0,

h(uµ(w′wnwi)v) ≥ log|uµ(w′wnwi)v| ≥ nc
′.

This is a contradiction. □

Tame semigroups aﬀord a particular block diagonal decomposition.

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 27

Lemma 8.5. Let S ⊆ Qd×d be a ﬁnitely generated tame semigroup. Then there exist
d1, . . ., dr ∈ Z≥0 with d = d1 + · · · + dr, ﬁnite semigroups Si ∈ Q
di×di for i ∈ {1, . . . , r},
and a matrix T ∈ GLd(Q) such that

T −1ST ⊆
 









S1 Qd1×d2 Qd1×d3 . . . Qd1×dr

0 S2 Qd2×d3 . . . Qd2×dr

0 0 S3 . . . Qd3×dr
... ... ... . . . ...
0 0 0 . . . Sr
 









 .

Proof. If S spans Qd×d, then µ(Σ∗
k) is ﬁnite [BCH16BCH16, Lemma 4] and we are done. Oth-
erwise, we iterate Lemma 5 of [BCH16BCH16] to get a block-upper-triangular decomposition
with ﬁnite semigroup diagonals. □

The arguments in the following proof are similar to [Bel05Bel05, Theorem 2.6].

Proof of Theorem 8.38.3. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be k-Mahler.
(a)(a) ⇒ (b)(b) Suppose h(an) ∈ o(log n). Then (an)n≥0 is k-regular by Theorem 7.17.1.
Lemma 8.48.4 implies that µ(Σ∗
k) is tame.
(b)(b) ⇒ (d)(d) Let (u, µ, v) be a minimal linear representation of the k-regular sequence
(an)n≥0. Suppose µ(Σ∗
k) is tame. We have to show h(an) ∈ O(log log n). For this,
it suﬃces to show h(uµ(w)v) ∈ O(log|w|) for non-empty words w ∈ Σ∗
k. We can apply
Lemma 8.58.5. Thus, there exists a ﬁnite semigroup S of block-diagonal matrices such that,
after a change of basis, for every w ∈ Σ∗
k the matrix µ(w) is of the form D + N with
D ∈ S and N strictly upper triangular. We may assume that S contains the identity
matrix. Since Σk is ﬁnite, there exists a ﬁnite set N of strictly upper triangular matrices
such that µ(Σk) ⊆ S + N .
Let w = a1 · · · al ∈ Σ∗
k with a1, . . . , al ∈ Σk, and let µ(ai) = Di + Ni with Di ∈ S and
Ni ∈ N . For J ⊆ {1, . . . , l} with J = {j1 < j2 < · · · < jr} deﬁne

bJ = uD1 · · · Dj1−1Nj1Dj1+1 · · · Dj2−1Nj2Dj2+1 · · · Djr−1Njr Djr+1 · · · Dlv .

Then uµ(w)v = uµ(a1 · · · al)v = u(D1 + N1) · · · (Dl + Nl)v = ∑

J⊆{1,...,l} bJ .

Any product that includes d or more of the Ni’s is 0, and hence bJ = 0 whenever #J ≥ d.
Thus, the previous sum reduces to

uµ(w)v = ∑

J⊆{1,...,l}
#J<d
 bJ .

This sum has at most ( l
d−1)+· · ·+(l
0
) ≤ Cld−1 non-zero terms for some constant C ∈ R>1.
As S is a semigroup, each product Dji+1 · · · Dji+1−1 is again contained in the ﬁnite set
S. Hence #{ bJ : J ⊆ {1, . . . , l} } ≤ d #S d #N d−1 < ∞ .
Let K be the number ﬁeld generated by the ﬁnitely many coordinates of u, v, and
µ(a) for a ∈ Σk. Then bJ ∈ K for each J ⊆ {1, . . . , l}. Since there are only ﬁnitely

28 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

many of these elements, for every place v of K, there exists a constant cv ∈ R>0 such
that |bJ |v ≤ cv for all J ⊆ {1, . . . , l}, and we can take cv = 1 for all but ﬁnitely many
places. For m ∈ Z≥0, let

εv(m) =
 {m if v is archimedean,
1 if v is non-archimedean.

Note ∏
v∈MK εv(m) ≤ m[K:Q]. With this deﬁnition |uµ(w)v|v ≤ εv(Cld−1)cv and

h(uµ(w)v) = log ∏

v∈MK max{1, |uµ(w)v|v}

≤ log ∏

v∈MK max{1, εv(Cld−1)cv}

≤ log (
(Cld−1)
[K:Q]) + log ( ∏

v∈MK max{1, cv}
) ∈ O(log l).

Since l = |w| this proves the claim.
(d)(d) ⇒ (a)(a) Clearly h(an) ∈ O(log log n) implies h(an) ∈ o(log n).
Finally, the equivalence (b)(b) ⇔ (c)(c) is precisely the equivalence (i) ⇔ (ii) proved by Bell,
Coons, and Hare in [BCH16BCH16, Theorem 13] (which does not require the sequences to be
Z-valued). □

9. Fourth gap: characterization of automatic Mahler functions

In this section, we characterize Mahler functions f (z) = ∑∞
n=0 anzn ∈ QJzK with
h(an) ∈ o(log log n), extending [BCH14BCH14, Theorem 1.1].

Theorem 9.1. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be a k-Mahler function. The following
statements are equivalent.
(a) We have h(an) ∈ o(log log n).
(b) For every minimal linear representation of (an)n≥0, the matrix semigroup µ(Σ∗
k) is
ﬁnite.
(c) The power series f (z) is k-automatic.
(d) We have h(an) ∈ O(1). Equivalently, the set { an : n ≥ 0 } is ﬁnite.

The following lemma closely follows [BCH14BCH14, Lemma 2.1]

Lemma 9.2. Let (an)n≥0 be a k-regular sequence in Q, with a minimal linear represen-
tation (u, µ, v). If h(an) ∈ o(log log n), then the semigroup µ(Σ∗
k) is ﬁnite.

Proof. Again a[w]k = uµ(w)v for all w ∈ Σ∗
k. By our assumption

h(uµ(w)v) ∈ o(log|w|) .

Now suppose to the contrary that µ(Σ∗
k) is inﬁnite. A theorem of McNaughton and
Zalcstein [MZ75MZ75] gives a positive answer to the strong Burnside problem for semigroups
of matrices over a ﬁeld. Since µ(Σ∗
k) is a ﬁnitely generated semigroup of matrices, but
not ﬁnite, this theorem implies that there exists w ∈ Σ∗
k such that µ(wm) ̸= µ(wn) for
all m, n ∈ Z≥0 with m ̸= n. Fix such a word w.

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 29

Set A := µ(w). By Lemma 8.48.4 every eigenvalue of A is either 0 or a root of unity. Our
choice of w ensures that there exists at least one non-zero eigenvalue ζ with a non-trivial
Jordan block. Let B ∈ Qd×d be an invertible matrix such that B−1AB is in Jordan
normal form. Without restriction we may assume

B−1AB =
 








ζ 1 0 . . . 0
0 ζ ∗ . . . 0
0 0 ∗ . . . 0
... ... ... . . . ...
0 0 . . . . . . ∗








 .

The (1, 2) entry of B−1AnB is nζ n−1. Hence h(eT
1 B−1AnBe2) = h(nζ n−1) ≥ log n.
Using the minimality of the linear representation, we can write eT
1 B−1 = ∑d
i=1 λiuµ(wi)
and Be2 = ∑d
i=1 τiµ(w′
i)v with suitable λi, τi ∈ Q and wi, w′
i ∈ Σ∗
k. It follows that

h
( d∑

i,j=1 λiτjuµ(wiwnw′
j)v) ≥ log n .

Hence there exist i, j ∈ {1, . . . , d} and c ∈ R>0 such that

h(uµ(wiwnw′
j)v) > c log n for inﬁnitely many n.

This is a contradiction to h(uµ(wiwnw′
j)v) ∈ o(log n). □

Proof of Theorem 9.19.1. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be a k-Mahler function.
(a)(a) ⇒ (b)(b) Let h(an) ∈ o(log log n). Then (an)n≥0 is k-regular by Theorem 7.17.1, with a
minimal linear representation (u, µ, v). By Lemma 9.29.2 the semigroup µ(Σ∗
k) is ﬁnite.
(b)(b) ⇒ (c)(c) Let (u, µ, v) be a minimal linear representation of the regular sequence
(an)n≥0. Suppose µ(Σ∗
k) is ﬁnite. Then (an)n≥0 takes only ﬁnitely many values, and
k-regular sequences taking ﬁnitely many values are automatic ([AS03aAS03a, Theorem 16.1.5]
or [BR11BR11, Proposition 5.3.3]).
(c)(c) ⇒ (d)(d) Let (an)n≥0 be k-automatic. Then the sequence only takes ﬁnitely many
values by deﬁnition.
(d)(d) ⇒ (a)(a) Clearly, if { an : n ≥ 0 } is ﬁnite, then h(an) ∈ o(log log n). □

10. Comments on Becker’s conjecture

Every k-regular power series is k-Mahler, and as a partial converse Becker showed that
a k-Becker power series is k-regular. He also conjectured a full description of k-regular
power series in terms of k-Becker power series. This conjecture was recently proven
by Bell, Chyzak, Coons, and Dumas, as the main result in [BCCD19BCCD19]. The proof in
[BCCD19BCCD19] is stated for K = C, but the same arguments apply equally well to arbitrary
ﬁelds of characteristic zero.

Theorem 10.1 ([BCCD19BCCD19, Theorem 1]). Let K be a ﬁeld of characteristic 0. If f (z) ∈
KJzK is k-regular, there exist a polynomial q(z) ∈ K[z] with q(0) = 1 such that 1/q(z) is
k-regular and a non-negative integer γ such f (z)/zγq(z) is a k-Becker Laurent series.

30 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

By a k-Becker Laurent series, we of course mean a Laurent series satisfying a func-
tional equation as in Deﬁnition 3.63.6. We stress that it is not always possible to obtain
a k-Becker power series of the form f (z)r(z) with r(z) a rational function [BCCD19BCCD19,
Theorem 14].
The proof of Bell, Chyzak, Coons, and Dumas breaks down into two steps:
(I) First they show that a k-regular power series f (z) ∈ KJzK satisﬁes a k-Mahler
equation p0(z)f (z) + p1(z)f (zk) + · · · + pd(z)f (zkd) = 0 ,

where all roots of p0(z) belong to {0} ∪ Uk. Equivalently, the k-denominator d(z) of
f (z) has all its roots in {0} ∪ Uk.
(II) They show that any such series has the required decomposition.
We now give alternative arguments for both of these steps using our results. In
particular, for K = Q, step I is immediate from Theorem 7.17.1 and our argument for step
II is somewhat shorter. We also recover Proposition 2 and Corollary 3 of [BCCD19BCCD19]
(Corollary 3 follows as in the proof of Proposition 7.97.9).

10.1. Step I. For K = Q, Theorem 7.17.1 immediately establishes step I. We now show
how to extend the relevant part of Theorem 7.17.1 to arbitrary ﬁelds of characteristic 0.
Let K be a ﬁeld of characteristic 0 and let f (z) = ∑∞
n=0 anzn ∈ KJzK be k-regular.
Let d(z) denote the Mahler denominator of f (z) over K. We also have that the k-kernel
of f (z) generates a ﬁnite-dimensional K-vector space. In particular, there is some ﬁxed
M > 0 such that for every j ∈ {0, 1, . . . , kM − 1}, we have

akM n+j = ∑

e<M
 ke−1∑

i=0 cj,i,eaken+i for n ≥ 0.

We have that for some s ≥ 0, the power series f (z), f (zk), . . . , f (zks) satisfy a Mahler
system of the form Equation (3.23.2) with some invertible matrix A(z) with entries in K(z).
Let R be a ﬁnitely generated Z-algebra that contains:
(1) a0, . . . , akM −1;
(2) the roots of d(z) and the reciprocals of all non-zero roots of d(z);
(3) the structure constants ci,j,e.
(4) the non-zero coeﬃcients and their inverses of each polynomial appearing in either
the numerator or denominator of an entry of A(z).
Then by construction, f (z) ∈ RJzK. If p is a prime ideal of R and g(z) ∈ RJzK, then we
let g|p(z) denote the power series in R/pJzK obtained by reducing the coeﬃcients of g(z)
modulo p. Then by construction, f|p(z) is a regular power series in (Rp/pp)JzK.

Lemma 10.2. Let λ ∈ R be a non-zero root of d(z). Then λ is a root of unity.

Proof. Suppose that λ is not root of unity. Then, since the coeﬃcients of A(z) have only
ﬁnitely many poles, there is some n such that λkn is a regular point with respect to this
Mahler system. We now take a k-Mahler equation

(10.1) q0(z)f (z) =
 L∑

i=1 qi(z)f (zki), q0(z), q1(z), . . . , qL(z) ∈ K[z],

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 31

with q0(z) ̸= 0 and L minimal. Iterating Equation (10.110.1) we ﬁnd an equation

(10.2) r0(z)f (z) =
 L+n−1∑

i=n ri(z)f (zki),

where we may assume that the polynomials r0(z), rn(z), . . . , rL+n+1(z) ∈ K[z] are co-
prime. The Mahler denominator d(z) divides r0(z) and so r0(λ) = 0. By coprimality of
the coeﬃcients, in particular there is some i0 such that ri0(λ) ̸= 0. Now we adjoin the
coeﬃcients of r0(z) and rn(z), . . . , rn+L−1(z) to R.
By Noether normalization, there is a positive integer N and x1, . . . , xd ∈ R such that
x1, . . . , xd are algebraically independent over Q and such that R[1/N ] is a ﬁnite integral
extension of Z[1/N ][x1, . . . , xd]. Let S denote the set of prime ideals p of R[1/N ] with
the property that p ∩ Z[1/N ][x1, . . . , xd] = (x1 − b1, . . . , xd − bd) with b1, . . . , bd integers.
By integrality, there is at least one such prime for each d-tuple (b1, . . . , bd) of integers.
Moreover, R/p is a ﬁnite extension of Z[1/N ], generated by at most κ elements for some
κ that is independent of p (indeed, we may take κ to be the cardinality of the set of
generators of R[1/N ] as a Z[1/N ][x1, . . . , xd]-module). Hence Rp/pp is a number ﬁeld of
degree at most κ for each p ∈ S.
Moreover, the intersection of the prime ideals in S is (0). For p ∈ S, we let λp =
λ + p ∈ R/p. Then we reduce Equation (10.210.2) modulo p and plug in z = λp to obtain

(10.3) 0 =
 L+n−1∑

i=n ri|p(λp)f|p(λ
ki
p ),

where the left side follows from the fact that d(z) divides r0(z). It is straightfor-
ward to see that λkn
p ∈ (R/p)p is a regular point of the reduced Mahler system for
f|p(z), f|p(zk), . . . , f|p(zkL−1) for p in a Zariski dense subset T of S. Moreover, there is a
Zariski dense subset T ′ of T such that ri0|p(λp) ̸= 0 for p ∈ T ′. We remark that there is
a Zariski dense subset T ′′ such that λp is not a root of unity. To see this, observe that if
p ∈ T ′ is such that λp is a root of unity, then Q(λp) is an extension of degree at most κ
and hence there is some ﬁxed M = M (κ) such that λM
p = 1. Since T ′ is Zariski dense,
this gives that λ is a root of unity, which is a contradiction.
Now for p ∈ T ′′, we have λp ∈ Kp := (R/p)p. Then there is some place v on the
number ﬁeld Kp such that |λp|v < 1. Equation (10.310.3) combined with Theorem 4.34.3 yields

0 =
 L+n−1∑

i=n ri|p(z)f|p(zki).

By Zariski density of T ′′, also 0 = ∑L+n−1
i=n ri(z)f (zki) ∈ RJzK ∩ KJzK, in contradiction
to the minimality of L. The result follows. □

By looking at the asymptotic behavior on the unit circle we may once again strengthen
the previous lemma.

Lemma 10.3. Let λ ∈ R be a non-zero root of d(z). Then λ ∈ Uk.

Proof. Let λ be a non-zero root of d(z). By the previous lemma λ ∈ U. Therefore it
suﬃces to show λkj ̸= λ for all j ≥ 1.

32 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

Suppose to the contrary that λkj = λ for some j ≥ 1. Since R is ﬁnitely generated, it
embeds into C. Let |·| denote the induced absolute value on R. We may now conclude
as in the proof of Proposition 7.87.8: from Proposition 7.77.7 we obtain log|an| ≥ c log2 n
inﬁnitely often. However, using the linear representation of a k-regular sequence, we
easily obtain log|an| ∈ O(log n) as in Lemma 7.107.10 (or [AS92AS92, Theorem 2.10]), a contra-
diction. □

We thus have the following theorem, extending a part of Theorem 7.17.1 to ﬁelds of
characteristic 0 and also generalizing [BCCD19BCCD19, Proposition 2].

Theorem 10.4. Let K be a ﬁeld of characteristic 0, let f (z) ∈ KJzK be k-Mahler,
and let d(z) be the Mahler denominator of f (z). Then f (z) is k-regular if and only if
every non-zero root of d(z) (in the algebraic closure K) is a root of unity with order not
coprime to k.

Proof. If f (z) is k-regular, the claim follows from the previous lemma. The converse
direction follows exactly as in the proof of Proposition 7.97.9. □

10.2. Step II. We now provide a somewhat shorter argument for the second step of
[BCCD19BCCD19]. First recall the following easy lemma.

Lemma 10.5. Let K be a ﬁeld and let f (z) ∈ KJzK be a k-Mahler power series solution
to the equation

(10.4) p0(z)f (z) + p1(z)f (zk) + · · · + pd(z)f (zkd) = 0 .

If there exists a polynomial q(z) such that p0(z)q(z) divides q(zkj ) for all j, 1 ≤ j ≤ d,
then f (z)/q(z) ∈ K((z)) is a k-Becker Laurent series.

Proof. Set g(z) := f (z)/q(z), then (10.410.4) gives

p0(z)q(z)g(z) + p1(z)q(zk)g(zk) + · · · + pd(z)q(zkd)g(zkd ) = 0 .

Thus, g(z) = − ∑d
i=1 ri(z)g(zki ), where ri(z) = pi(z)q(zki)/(p0(z)q(z)) ∈ K[z]. □

Proof of Becker’s conjecture (Theorem 10.110.1). Since f (z) is k-regular, we know, by the
ﬁrst step, that f (z) satisﬁes an equation of the form

p0(z)f (z) + p1(z)f (zk) + · · · + pd(z)f (zkd) = 0 ,

where all roots of p0(z) belong to {0} ∪ Uk. Thus, every non-zero root is a primitive
ℓ-root of unity for some ℓ not coprime with k. For such a natural number ℓ, there exist
a positive integer r and a non-negative integer s such that gcd(ℓ, kj ) = r for all j > s.
Let s be minimal with this property. Let A denote the set of non-zero roots of p0(z),
and, for ξ ∈ A, set a(ξ) := ℓ(ξ)/r(ξ). Let φn(z) denote the nth cyclotomic polynomial.
Then φℓ(ξ)(z)φa(ξ)(zks) divides φa(ξ)(zks+j ) for all j ≥ 1. In particular, (z − ξ)φa(ξ)(zks)
divides φa(ξ)(zks+j ) for all j, 1 ≤ j ≤ m. Setting

q(z) := ∏

ξ∈A φa(ξ)(zks) ,

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 33

and applying Lemma 10.510.5, we obtain that f (z)/zγq(z) is a k-Becker Laurent series,
where γ is the valuation of p0(z). Moreover, 1/q(z) is a k-Becker power series for

q(z)
−1 = q(zk)
q(z) · q(zk)
−1

and by construction q(z) divides q(zk). In particular, 1/q(z) is k-regular. □

11. Automatic Mahler power series over arbitrary fields

We ﬁrst show how to extend our characterization of k-automatic Mahler functions to
arbitrary ground ﬁelds of characteristic zero.

Theorem 11.1. Let K be a ﬁeld of characteristic 0 and let f (z) = ∑∞
n=0 anzn ∈ KJzK
be a k-Mahler power series. Then (an)n≥0 is k-automatic if and only if { an : n ≥ 0 } is
ﬁnite.

In order to prove Theorem 11.111.1, we use a standard specialization argument.

Lemma 11.2. Let K be a ﬁeld of characteristic zero containing Q, and let u1, . . . , ud ∈
K. Then there exists a ring homomorphism ϕ : Q[u1, . . . , ud] → Q leaving Q invariant.

Proof. This is an easy consequence of the weak Nullstellensatz. A proof can be found in
[EG15EG15, Lemma 6.3.3]. □

Proof of Theorem 11.111.1. Let f (z) = ∑∞
n=0 anzn ∈ KJzK be a k-Mahler power series with
ﬁnite set of coeﬃcients. Replacing K by its algebraic closure, we may assume Q ⊆ K.
Let p0(z), . . . , pd(z) ∈ K[z] be such that

p0(z)f (z) + p1(z)f (zk) + · · · + pd(z)f (zkd) = 0 .

Let C be the ﬁnite set consisting of all coeﬃcients of f (z) and p0(z), . . . , pd(z). We apply
Lemma 11.211.2 with the set {u1, . . . , ud} consisting of all c ∈ C, all c − d with c, d ∈ C, as
well as the inverses of all these elements that are non-zero. Thus ϕ(c) ̸= 0 for c ̸= 0 and
ϕ(c) ̸= ϕ(d) for c ̸= d. The resulting homomorphism extends to ϕ : Q[u1, . . . , um]JzK →
QJzK, and

ϕ(p0)(z) · ϕ(f )(z) + ϕ(p1)(z) · ϕ(f )(zk) + · · · + ϕ(pd)(z) · ϕ(f )(zkd) = 0

is a k-Mahler equation for ϕ(f )(z). Thus Theorem 9.19.1 implies that the sequence
(ϕ(an))n≥0 is k-automatic. Since ϕ : C → Q is injective, the same is true for (an)n≥0. □

11.1. The case of a base ﬁeld of positive characteristic. Theorem 11.111.1 strongly
depends on the characteristic of the ﬁeld being zero. If K is a ﬁeld of characteristic
p > 0, we still have a similar result for p-Mahler power series (see Proposition 11.311.3), but
if k is coprime to p this is no longer true. Indeed, the series

∞∏

i=0
(1 − zki)
−1 ∈ KJzK

is not k-automatic by [Bec94Bec94, Proposition 1], despite being k-Mahler with coeﬃcients
taking only ﬁnitely many values (because they belong to the prime ﬁeld).

34 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

Proposition 11.3. Let K be a ﬁeld of characteristic p and let f (z) = ∑∞
n=0 anzn ∈ KJzK
be a k-Mahler power series where k is a power of p. Then the sequence (an)n≥0 is k-
automatic if and only if { an : n ≥ 0 } is ﬁnite.

Proof. Let f (z) = ∑∞
n=0 anzn ∈ KJzK be pm-Mahler for some positive integer m. Let us
assume that { an : n ≥ 0 } is ﬁnite. Let us consider a non-trivial equation

p0(z)f (z) + p1(z)f (zpm) + · · · + pd(z)f (zpmd) = 0 .

We let R denote the ﬁnitely generated Fp-algebra generated by the coeﬃcients an, the
inverses of all non-zero diﬀerences ai − aj, and the coeﬃcients of the polynomials pi(z),
as well as the inverses of their non-zero coeﬃcients.
Let M be some maximal ideal of R. Then R/M = Fq with q a power of p, say
q = pℓ. Let f|M(z) := ∑∞
n=0(an mod M)zn denote the reduction of f (z) modulo M.
Then f|M(z) is pm-Mahler and hence it is also pmℓ-Mahler by Lemma 3.23.2. Thus, we
deduce that f|M(z) is algebraic over Fq(z). By Christol’s theorem (see [AS03aAS03a, Chapter
12]), the sequence (an mod M)n≥0 is p-automatic. But by deﬁnition of R, if ai ̸= aj
then ai mod M ̸= aj mod M. Thus the sequence (an)n≥0 is also p-automatic, and hence
pm-automatic. □

12. Decidability

A k-Mahler function can be uniquely speciﬁed by the ﬁnite data consisting of a k-
Mahler equation it satisﬁes and suﬃciently many initial coeﬃcients of the power series.
Therefore it is reasonable to ask whether, for a given k-Mahler function, it can be decided
which of the ﬁve cases of Theorem 1.11.1 it falls into. However, we neither try to describe
an eﬃcient algorithm to perform this task, nor do we provide an upper bound for the
complexity of the algorithm that could be extracted from what follows.

Theorem 12.1. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be a k-Mahler function (speciﬁed by a
k-Mahler equation and suﬃciently many initial coeﬃcients). Then it is decidable which
of the ﬁve growth classes in Theorem 1.11.1 the function f falls into.

Let f (z) = ∑∞
n=0 anzn ∈ QJzK be k-Mahler. As Theorems 6.16.1 and 7.17.1 show, the
minimal denominator d(z) ∈ Q[z] of f (z) plays a crucial role in determining the growth
class that f (z) falls into: the growth depends on whether d(z) has roots outside {0} ∪ U,
respectively outside {0} ∪ Uk. This raises the question whether there is an eﬀective way
of deciding which of the three cases occurs. Along similar lines, if f (z) is k-regular, the
question arises whether it is decidable into which of the three cases (k-regular, Q-linear
combination of word-convolution products of k-automatic sequences, and k-automatic)
the coeﬃcients of f (z) falls. In this section, we establish that all these properties are
decidable.
Suppose f (z) is speciﬁed by a k-Mahler equation and suﬃciently many initial coef-
ﬁcients to determine the solution uniquely. Then we can compute any ﬁnite number
of initial coeﬃcients by recursion. By work of Adamczewski and Faverjon [AF18AF18] it
is possible to ﬁnd a minimal (homogeneous) k-Mahler equation, that is, polynomials
p0(z), p1(z), . . . , pd(z) ∈ K[z], where K is a number ﬁeld,

(12.1) p0(z)f (z) + p1(z)f (zk) + · · · + pd(z)f (zkd) = 0 ,

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 35

where d is minimal and p0(z), . . . , pd(z) are coprime.
By deﬁnition d(z) divides p0(z). It is tempting to hope that, to determine the types of
roots of d(z), it suﬃces to consider those of p0(z). Unfortunately, this hope is thwarted
by Example 3.103.10. We can however still determine the types of roots of d(z).

Proposition 12.2. There exists an algorithm to determine whether the k-Mahler de-
nominator d(z) of a k-Mahler function f (z) has a root outside {0} ∪ U.
Moreover, if all roots of d(z) are contained in {0} ∪ U, then we can ﬁnd an explicit
k-Mahler equation
 q0(z)f (z) = q1(z)f (zkn0 ) + · · · + qd(z)f (zkn0 +d−1)

with n0 ≥ 1, with q0(z), . . . , qd(z) ∈ Q[z] and all roots of q0(z) contained in {0} ∪ U.

Proof. Let us consider the minimal equation (12.112.1). By [AF18AF18], this equation can be
explicitly determined (this is a variation of Algorithm 1.3 in [AF18AF18]). We may assume
that the number ﬁeld K contains all coeﬃcients and roots of p0(z), . . . , pd(z). Set

S := { λ : p0(λ)pd(λ) = 0 }

and ρ = min
v∈MK{ min{ |λ|v : p0(λ)pd(λ) = 0 } } .

Now, let n0 be the minimal positive integer such that |λkn0 |v < ρ for all λ in S and all
places v such that |λ|v < 1 (there are only a ﬁnite number of such places). The integer
n0 can be explicitly determined. By repeated substitution, we can explicitly determine
an equation

(12.2) q0(z)f (z) = q1(z)f (zkn0 ) + · · · + qd(z)f (zkn0 +d−1) ,

for f (z). Suppose ﬁrst that q0(z) does not have a non-zero root λ that is not a root of
unity. Then neither does d(z), because d(z) divides q0(z).
Suppose now q0(z) has a non-zero root λ that is not a root of unity. By Kronecker’s
theorem, there exists a place v such that 0 < |λ|v < 1. Arguing exactly as in the proof
of Proposition 6.46.4, we see that λ is a pole of f (z). Thus f (z) has a radius of convergence
strictly less than 1 with respect to |·|v. By Theorem 6.16.1 also d(z) must have a non-zero
root that is not a root of unity. □

Assuming d(z) does not have a root outside of {0} ∪ U, we now want to determine if
it has a root in U ∖ Uk.

Lemma 12.3. Let d ∈ Z>0, let ζ ∈ C ∖ {0} such that ζ k = ζ, and let A(z) ∈ Q(z)d×d.
Assume that w(z) ∈ CJzKd satisﬁes the equation

w(z) = A(z)w(zk) .

Assume also that the following properties hold.
(i) The coordinates of A(z) have no poles at ζ and no poles in B(0, 1).
(ii) The coordinates of w(z) are continuous in B(0, 1).
Then, there exists c ∈ R>0 such that

∥w(tζ)∥ < |1 − t|
−c for all t ∈ (0, 1).

36 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

Proof. Since the map [0, 1] → Cd×d, t ↦→ A(tζ) is continuous, there exists c0 ≥ 1 such
that ∥A(tζ)∥ ≤ c0 for all t ∈ [0, 1]. Let ε ∈ (0, 1) and c1 = max{ ∥w(tζ)∥ : t ∈ [0, ε] }.
Let t ∈ [0, 1), and let n ∈ Z≥0 be minimal such that tkn ≤ ε. We can obtain an upper
bound on n as follows. The inequality tkn ≤ ε is equivalent to kn log t ≤ log ε, which
is equivalent to kn(− log t) ≥ − log ε. In turn, this is equivalent to n + logk(− log t) ≥
logk(− log ε). So n = ⌈logk(− log ε) − logk(− log t)⌉ .
Thus n ≤ c2 − logk(− log t) with c2 = 1 + logk(− log ε) .
Now kn ≤ kc2k− logk(− log t) ≤ kc2 1
− log t ≤ kc2 1
1 − t ,

where we used log t ≤ t − 1 for the last inequality. We have

w(tζ) = A(tζ)A(tkζ) · · · A(tkn−1ζ)w(tknζ) ,

and thus ∥w(tζ)∥ ≤ cn
0 c1. Now

c
n
0 c1 = c1kn logk c0 ≤ c1kc2 logk c0(1 − t)
− logk c0.

The constant may be absorbed by replacing the exponent by a bigger one. □

Proposition 12.4. Let f (z) ∈ QJzK be k-Mahler with k-Mahler denominator d(z).
Suppose all roots of d(z) are contained in {0} ∪ U. There exists an algorithm to decide
whether d(z) has a root in U ∖ Uk.
Moreover, if all roots of d(z) are contained in {0} ∪ Uk, then we can ﬁnd an explicit
k-Mahler equation
 s0(z)f (z) = s1(z)f (zk) + · · · + sd(z)f (zkd)

with s0(z), . . . , sd(z) ∈ Q[z] and all roots of s0(z) contained in {0} ∪ Uk.

Proof. Let d(z)f (z) = p1(z)f (zk) + · · · + pd(z)f (zkd) with p1(z), . . . , pd(z) ∈ Q[z]. Using
the condition on d(z) together with the fact that f (z) converges in a neighborhood of 0,
this equation implies that f (z) is analytic in B|·|(0, 1) for every absolute value |·| on Q.
Now let q0(z)f (z) = q1(z)f (zk) + · · · + qd(z)f (zkd) with q0(z), . . . , qd(z) ∈ Q[z] and
q0(z)qd(z) ̸= 0 be an explicit k-Mahler equation for f (z). Since d(z) divides q0(z), we
only have to check if any of the ﬁnitely many roots of q0(z) in U ∖ Uk are roots of d(z).
Suppose ζ is such a root of q0(z). Then there exists an, explicitly determinable, integer
j0 ≥ 1 such that ζ kj0 = ζ. Let ℓ = kj0. Again using [AF18AF18] we can ﬁnd an ℓ-Mahler
equation for f (z), say

(12.3) r0(z)f (z) = r1(z)f (zℓ) + · · · + re(z)f (zℓe)

with r0(z), . . . , re(z) ∈ Q[z] coprime and r0(z)re(z) ̸= 0. If r0(ζ) ̸= 0, then d(ζ) ̸= 0.
Suppose now r0(ζ) = 0. We will show d(ζ) = 0. Fix any embedding Q ֒→ C, and
thereby an archimedean absolute value |·| on Q. Proposition 7.77.7 implies that there exist
a, b, c ∈ R>0, m0, n0 ∈ Z≥0, and a sequence (tj)j≥0 → 1 in [0, 1) such that

∣
∣ ∞∑

n=0 an+n0(ζtj)
n∣
∣ ≥ (1 − tj)
a exp(b log2 m)tmc
j for all j ≥ 0 and m ≥ m0.

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 37

Deﬁne f0(z) = ∑∞
n=0 an+n0zn and mj = ⌈1/(1 − tj)⌉. Then

log|f0(ζtj)| ≥ a log(1 − tj) + b log2⌈1/(1 − tj)⌉ + ⌈1/(1 − tj)⌉c log tj .

As in the proof of Lemma 7.37.3 we see that the right side is asymptotically equivalent
to b log2(1 − tj). Now, if we had d(ζ) ̸= 0, then Lemma 12.312.3 would give log|f0(ζtj)| ≤
−c log(1 − tj) for some c ∈ R>0, a contradiction.
To explicitly ﬁnd an equation with s0(z) as desired, note that for each ζ ∈ U ∖ Uk
that is a root of q0(z), we have found some k-Mahler equation, Equation (12.312.3), for f (z)
with r0(ζ) ̸= 0. Taking the greatest common divisor of q0(z) and all these r0(z) as ζ
varies over the roots, we obtain the desired equation. □

We have now shown that it is possible to decide algorithmically which of Cases (1)(1)
and (2)(2) of Theorem 1.11.1 a given Mahler function f (z) = ∑∞
n=0 anzn ∈ QJzK falls into.
Suppose now that f (z) is k-regular. In this case, we wish to also decide whether f (z)
belongs to class (3)(3), (4)(4), or (5)(5) of Theorem 1.11.1.

12.1. From k-Mahler equations to linear representations. We have represented
an arbitrary k-Mahler function f (z) by a k-Mahler equation and suﬃciently many initial
coeﬃcients. If f (z) is k-regular, it is more natural to represent the sequence of coeﬃcients
by a linear representation. We show that such a linear representation is computable from
a k-Mahler equation satisﬁed by f (z). Recall that ∆r with r ∈ Σk denotes the Cartier
operators (Deﬁnition 6.36.3).

Lemma 12.5. Let f1(z), . . . , fd(z) ∈ QJzK with fi(z) = ∑∞
n=0 ai,nzn. Suppose that, for
every r ∈ Σk and every 1 ≤ i ≤ d, there are explicitly known coeﬃcients λr,1, . . . , λr,d ∈ Q
such that
 ∆r(fi(z)) = λr,1,if1(z) + · · · + λr,d,ifd(z) .

Then we get an explicit linear representation for the k-regular sequence (a1,n)n≥0.

Proof. Let µ : Σ∗
k → Qd×d be deﬁned by

µ(r) :=
 



λr,1,1 . . . λr,1,d
... . . . ...
λr,d,1 . . . λr,d,d



 and let a(n) := (a1,n, . . . , ad,n).

Since ∆r(fi(z)) = ∑∞
n=0 ai,kn+rzn, we obtain a(kn + r) = a(n)µ(r) for r ∈ Σk. Finally
let e1 = (1, 0, . . . , 0)T ∈ Qd×1. Then a1,[w]k = a([w]k)e1 = a(0)µ(w)e1 for all words
w ∈ Σ∗
k. □

Lemma 12.6. Let p1(z), . . . , pd(z) ∈ Q[z] with e = max{deg p1(z), . . . , deg pd(z)}. If
f (z) = ∑∞
n=0 anzn ∈ QJzK satisﬁes the k-Becker equation

f (z) = p1(z)f (zk) + · · · + pd(z)f (zkd) ,

then a linear representation for the k-regular sequence (an)n≥0 is computable from a0
and p1(z), . . . , pd(z).

38 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

Proof. Following Becker [Bec94Bec94, Theorem 2], we see that the Q-vector space V spanned
by { zif (zkj ) : 0 ≤ i ≤ e, 0 ≤ j ≤ d } is closed under all Cartier operators. Explicitly, if
r ∈ Σk, 0 ≤ i ≤ e, and j ≥ 1, then

∆r(zif (zkj )) = ∆r(zi)f (zkj−1) ∈ V,

since ∆r(zi) = z(i−r)/k if i ≡ r mod k and ∆r(zi) = 0 otherwise. If j = 0, then
deg(∆r(zipj(z))) ≤ 2e/k ≤ e, and thus

∆r(zif (z)) = ∆r( d∑

j=1 zipj(z)f (zkj )
) =
 d∑

j=1 ∆r(zipj(z))f (zkj−1 ) ∈ V .

Since ∆r(zipj(z)) can be explicitly computed, we may apply Lemma 12.512.5 to ﬁnd a linear
representation of (an)n≥0. Since 0if (0kj ) ∈ {0, a0}, the resulting linear representation
only depends on p1(z), . . . , pd(z) and a0. □

It is rather non-trivial that the convolution product of k-regular sequences is again
k-regular. The standard way to show this uses the module-theoretic characterization of k-
regularity; see [AS03aAS03a, Theorem 16.4.1] or [BR11BR11, Proposition 5.2.7]. To see that a linear
representation of the convolution product is computable from linear representations, we
need to revisit this proof.

Remark 12.7. Using the growth-based characterization of k-regular sequences in The-
orem 6.16.1, it is easy to show that the convolution product of k-regular sequences is
k-regular. However, since this characterization already makes use of this fact that con-
volution products of k-regular sequences are k-regular (in Proposition 7.97.9), this does not
actually give a new, independent proof.

Lemma 12.8. Let (a(n))n≥0 and (b(n))n≥0 be two k-regular sequences in Q, each being
given by a linear representation. Then a linear representation of the convolution product
(a ⋆ b(n))n≥0 is computable.

Let us recall that by deﬁnition a ⋆ b(n) = ∑n
i=0 a(i)b(n − i).

Proof. For r ∈ Σk, let (∆r(a)(n))n≥0 be the sequence deﬁned by ∆r(a)(n) := a(kn + r).
The key step in the proof of Allouche and Shallit [AS03aAS03a, Theorem 16.4.1] is the reduction
(with r ∈ Σk)

(12.4) ∆r(a ⋆ b)(n) = ∑

0≤s≤r ∆s(a) ⋆ ∆r−s(b)(n) + ∑

r<s≤k−1 ∆s(a) ⋆ ∆k+r−s(b)(n − 1) .

We will adapt this proof to the case where a and b are given by linear representations.
Without restriction we can assume that the linear representations of a and b both have
the same dimension d ≥ 0. After a change of basis, we may take the linear representation
of a to be (a(0), κ, e1), where a(0) = (a1(0), . . . , ad(0)) with a1(0) = a(0), where e1 =
(1, 0, . . . , 0)T , and where κ : Σ∗
k → Qd×d is a monoid homomorphism. Deﬁne a(n) :=
a(0)κ(⟨n⟩k), where ⟨n⟩k ∈ Σ∗
k is the canonical base-k expansion of n. Then, in particular,

(a1(kn + r), . . . , ad(kn + r)) = (a1(n), . . . , ad(n)) κ(r) for r ∈ Σk.

For b we have a linear representation (b(0), λ, e1) with analogous deﬁnitions.

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 39

We construct a linear representation for a ⋆ b of dimension 2d2. For this, we index
the ﬁrst set of d2 coordinates by (i, j) in lexicographic order, and the second by (i′, j′),
where 1 ≤ i, j ≤ d. That is, the coordinates are indexed by (1, 1), (1, 2), . . . , (d, d),
(1′, 1′), (1′, 2′), . . . , (d′, d′). We use subscripts to indicate the corresponding entry of a
matrix, e.g., κ(r)i,j is the entry in the ith row and jth column of κ(r). For 1 ≤ i, j ≤ d
and r, s ∈ Σk, we get

∆r(ai) ⋆ ∆s(bj) = ( d∑

ℓ=1 aℓκ(r)ℓ,i) ⋆ ( d∑

m=1 bmλ(s)m,j ) =
 d∑

ℓ,m=1 κ(r)ℓ,iλ(s)m,j(aℓ ⋆ bm) .

Using Equation (12.412.4),

∆r(ai ⋆ bj)(n) = ∑

0≤s≤r
 d∑

ℓ,m=1 κ(s)ℓ,iλ(r − s)m,j (aℓ ⋆ bm)(n)

+ ∑

r<s≤k−1
 d∑

ℓ,m=1 κ(s)ℓ,iλ(k + r − s)m,j (aℓ ⋆ bm)(n − 1)

=
 d∑

ℓ,m=1
 ( ∑

0≤s≤r κ(s)ℓ,iλ(r − s)m,j )
(aℓ ⋆ bm)(n)

+
 d∑

ℓ,m=1
 ( ∑

r<s≤k−1 κ(s)ℓ,iλ(k + r − s)m,j)(aℓ ⋆ bm)(n − 1) .

Further note if r ≥ 1, then ai ⋆ bj(kn + r − 1) = ∆r−1(ai ⋆ bj)(n). For r = 0 we have
ai ⋆ bj(kn − 1) = ai ⋆ bj(k(n − 1) + (k − 1)) = ∆k−1(ai ⋆ bj)(n − 1). In this case, in
Equation (12.412.4), the second sum vanishes, and we again obtain ai ⋆ bj(kn − 1) as a linear
combination of the aℓ ⋆ bm(n − 1), namely,

∆k−1(ai ⋆ bj)(n − 1) =
 d∑

ℓ,m
 ( ∑

0≤s≤k−1 κ(s)ℓ,iλ(k − 1 − s)m,j )
(aℓ ⋆ bm)(n − 1).

For two d×d-matrices A, B, the Kronecker product A⊗B is the d2 ×d2-matrix deﬁned
by (A ⊗ B)(i,j),(ℓ,m) = Ai,ℓBj,m. For r ∈ Σk with r ̸= 0, we deﬁne the 2d2 × 2d2-matrix
µ(r) by the block structure

µ(r) := ( ∑
0≤s≤r κ(s) ⊗ λ(r − s) ∑
0≤s≤r κ(s) ⊗ λ(r − 1 − s)
∑r<s≤k−1 κ(s) ⊗ λ(k + r − s) ∑r<s≤k−1 κ(s) ⊗ λ(k + r − 1 − s)

) .

Similarly
 µ(0) :=
 ( κ(0) ⊗ λ(0) 0
∑k−1
s=1 κ(s) ⊗ λ(k − s) ∑k−1
s=0 κ(s) ⊗ λ(k − 1 − s)

)
 .

Deﬁne for each n ≥ 0 the 2d2 row vector v(n) by v(n)(ℓ,m) = aℓ ⋆ bm(n) and v(n)(ℓ′,m′) =
aℓ ⋆ bm(n − 1). Then
 v(kn + r) = v(n)µ(r).

40 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

Now v(1,1)(n) = a1 ⋆ b1(n) = a ⋆ b(n). Thus, the triple (v(0), µ, e(1,1)), where e(1,1) is the
2d2 column vector with 1 in the coordinate (1, 1) and zeroes everywhere else, is a linear
representation for a ⋆ b. □

Proposition 12.9. Let f (z) = ∑∞
n=0 anzn ∈ QJzK be k-regular, given by a k-Mahler
equation, the minimal n0 ≥ 0 with an0 ̸= 0, and the value an0. Then a linear represen-
tation for the k-regular sequence (an)n≥0 is computable.

Proof. From a linear representation of (an)n≥n0 it is easy to ﬁnd one for (an)n≥0. We
may therefore without restriction assume n0 = 0. (An explicit k-Mahler equation for
this power series can be found using [AB17AB17, Lemma 6.1].)
Using Propositions 12.212.2 and 12.412.4, we can further ﬁnd a k-Mahler equation

p0(z)f (z) = p1(z)f (zk) + · · · + pdf (zkd) ,

with p0(z), . . . pd(z) ∈ Q[z], with p0(z) and pd(z) coprime, and with the property that
all roots of p0(z) are contained in Uk. In particular, we may assume p0(0) = 1.
Now Theorem 3.83.8 gives a decomposition

f (z) = g(z)
( ∞∏

i=0 p0(zki)
)−1 ,

where g(z) is k-Becker, and a k-Becker equation for g(z) can be computed. Lemma 12.612.6
yields a linear representation for the coeﬃcient sequence of g(z). Factoring p0(z) into
linear factors of the form 1 − zζ −1 with ζ ∈ Uk, we recall that ∏∞
i=0(1 − zkiζ −1)−1 is
k-regular. Indeed, by [AB17AB17, Proposition 7.8], this inﬁnite product factors as a polyno-
mial and a k-Becker function (both computable). Using Lemma 12.812.8 we ﬁnd a linear
representation for ∏∞
i=0(1 − zkiζ −1)−1. Finally, Lemma 12.812.8 allows us to ﬁnd a linear
representation for f (z) itself. □

12.2. Tame and ﬁnite semigroups. From a linear representation, a minimal linear
representation is computable, and we may now assume that the k-regular sequence
(an)n≥0 is given by such a minimal linear representation (u, µ, v). To decide which of
Cases (3)(3)–(5)(5) of Theorem 1.11.1 the sequence belongs to, it now suﬃces to decide whether
or not the ﬁnitely generated matrix semigroup µ(Σ∗
k) is ﬁnite, respectively, tame.
For this, we ﬁrst need the following two lemmas.

Lemma 12.10. Let A1, . . . , At ∈ Qd×d. It is possible to decide whether or not the
matrices A1, . . . , At have a proper non-zero common invariant subspace, and if so, to
compute one.

Proof. This can be done using exterior powers and Gröbner bases, see Arapura and
Peterson [AP04AP04]. A model-theoretic approach is given by Pastuszak in [Pas17Pas17]. Both
papers discuss the history of this problem. □

Lemma 12.11. Let K be a number ﬁeld and d ≥ 0. For every r ≥ 0, there exists a
computable n = n(r, K) with the following property: if S ⊆ K d×d is a ﬁnite semigroup
generated by r matrices, then #S ≤ n.

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 41

Proof. By a result of Mandel and Simon [MS78MS78, Theorem 1.2] there exists such a bound
n(r, K, g), that however also depends on the maximal size g of a subgroup of S. Over a
number ﬁeld, Schur [Sch05Sch05] proved that there exists an explicit bound on the size of a
ﬁnite subgroup of GLd(K), so we can bound g independently of S. (See also the, largely
expository, article [GL06GL06] for this and later results.) □

Proposition 12.12. Let S ⊆ Qd×d be a ﬁnitely generated matrix semigroup, given by a
ﬁnite set of generators. It is decidable whether or not S is

(1) ﬁnite,
(2) tame.

Proof. Let A1, . . . , Al be the given set of generators for S, and let K be the number
ﬁeld generated by all the coeﬃcients of the matrices Ai. Then S ⊆ K d×d and it suﬃces
to consider the problem over the ﬁeld K.
(1) With the bound from Lemma 12.1112.11, one can decide whether or not S is ﬁnite.
(2) This problem can be reduced to the ﬁniteness problem using Lemma 8.58.5. Indeed,
by iterated application of Lemma 12.1012.10, we may decompose K d×1 = V1 ⊕ · · · ⊕ Vs with
each Vi a S-invariant subspace that contains no proper, non-zero S-invariant subspace.
Then Lemma 8.58.5 implies that S is tame if and only if S|Vi is ﬁnite for each 1 ≤ i ≤ s.
This can be decided using (1). □

References

[AB17] B. Adamczewski and J. P. Bell. A problem about Mahler functions. Ann. Sc. Norm. Super.
Pisa Cl. Sci. (5), 17(4):1301–1355, 2017.
[Ada19] B. Adamczewski. Mahler’s method. Doc. Math. (Extra Volume Mahler Selecta), pages 95–
122, 2019.
[ADH21] B. Adamczewski, T. Dreyfus, and C. Hardouin. Hypertranscendence and linear diﬀerence
equations. J. Amer. Math. Soc., 34(2):475–503, 2021. doi:10.1090/jams/960doi:10.1090/jams/960.
[ADHW20] B. Adamczewski, T. Dreyfus, C. Hardouin, and M. Wibmer. Algebraic independence and
linear diﬀerence equations. 2020. To appear in J. Eur. Math. Soc. arXiv:2010.09266arXiv:2010.09266.
[AF17] B. Adamczewski and C. Faverjon. Méthode de Mahler: relations linéaires, transcendance
et applications aux nombres automatiques. Proc. Lond. Math. Soc. (3), 115(1):55–90, 2017.
doi:10.1112/plms.12038doi:10.1112/plms.12038.
[AF18] B. Adamczewski and C. Faverjon. Méthode de Mahler, transcendance et relations linéaires:
aspects eﬀectifs. J. Théor. Nombres Bordeaux, 30(2):557–573, 2018.
[AF20] B. Adamczewski and C. Faverjon. Mahler’s method in several variables and ﬁnite automata.
2020. Preprint. arXiv:2012.08283arXiv:2012.08283.
[And00a] Y. André. Séries Gevrey de type arithmétique. I. Théorèmes de pureté et de dualité. Ann.
of Math. (2), 151(2):705–740, 2000. doi:10.2307/121045doi:10.2307/121045.
[And00b] Y. André. Séries Gevrey de type arithmétique. II. Transcendance sans transcendance. Ann.
of Math. (2), 151(2):741–756, 2000. doi:10.2307/121046doi:10.2307/121046.
[AP04] D. Arapura and C. Peterson. The common invariant subspace problem: an approach via
Gröbner bases. Linear Algebra Appl., 384:1–7, 2004. doi:10.1016/j.laa.2003.03.001doi:10.1016/j.laa.2003.03.001.
[AS92] J.-P. Allouche and J. Shallit. The ring of k-regular sequences. Theoret. Comput. Sci.,
98(2):163–197, 1992. doi:10.1016/0304-3975(92)90001-Vdoi:10.1016/0304-3975(92)90001-V.
[AS03a] J.-P. Allouche and J. Shallit. Automatic sequences. Cambridge University Press, Cambridge,
2003. Theory, applications, generalizations. doi:10.1017/CBO9780511546563doi:10.1017/CBO9780511546563.
[AS03b] J.-P. Allouche and J. Shallit. The ring of k-regular sequences. II. Theoret. Comput. Sci.,
307(1):3–29, 2003. Words. doi:10.1016/S0304-3975(03)00090-2doi:10.1016/S0304-3975(03)00090-2.

42 BORIS ADAMCZEWSKI, JASON BELL, AND DANIEL SMERTNIG

[BCCD19] J. P. Bell, F. Chyzak, M. Coons, and P. Dumas. Becker’s conjecture on Mahler functions.
Trans. Amer. Math. Soc., 372(5):3405–3423, 2019. doi:10.1090/tran/7762doi:10.1090/tran/7762.
[BCH14] J. P. Bell, M. Coons, and K. G. Hare. The minimal growth of a k-regular sequence. Bull.
Aust. Math. Soc., 90(2):195–203, 2014. doi:10.1017/S0004972714000197doi:10.1017/S0004972714000197.
[BCH16] J. P. Bell, M. Coons, and K. G. Hare. Growth degree classiﬁcation for ﬁnitely
generated semigroups of integer matrices. Semigroup Forum, 92(1):23–44, 2016.
doi:10.1007/s00233-015-9725-1doi:10.1007/s00233-015-9725-1.
[Bec94] P.-G. Becker. k-Regular Power Series and Mahler-Type Functional Equations. J. Number
Theory, 49(3):269–286, 1994. doi:10.1006/jnth.1994.1093doi:10.1006/jnth.1994.1093.
[Bel05] J. P. Bell. A gap result for the norms of semigroups of matrices. Linear Algebra Appl.,
402:101–110, 2005. doi:10.1016/j.laa.2004.12.007doi:10.1016/j.laa.2004.12.007.
[BG06] E. Bombieri and W. Gubler. Heights in Diophantine geometry, volume 4 of
New Mathematical Monographs. Cambridge University Press, Cambridge, 2006.
doi:10.1017/CBO9780511542879doi:10.1017/CBO9780511542879.
[BR11] J. Berstel and C. Reutenauer. Noncommutative rational series with applications, volume 137
of Encyclopedia of Mathematics and its Applications. Cambridge University Press, Cam-
bridge, 2011.
[Cob68] A. Cobham. On the hartmanis-stearns problem for a class of tag machines. In Conference
Record of 1968 Ninth Annual Symposium on Switching and Automata Theory, Schenectady,
New York, pages 51–60, 1968.
[dB48] N. G. de Bruijn. On Mahler’s partition problem. Nederl. Akad. Wetensch., Proc., 51:659–669
= Indagationes Math. 10, 210–220 (1948), 1948.
[DF96] P. Dumas and P. Flajolet. Asymptotique des récurrences mahlériennes: le cas cyclotomique.
J. Théor. Nombres Bordeaux, 8(1):1–30, 1996.
[Dum93] P. Dumas. Récurrences mahlériennes, suites automatiques, études asymptotiques. Institut
National de Recherche en Informatique et en Automatique (INRIA), Rocquencourt, 1993.
Thèse, Université de Bordeaux I, Talence, 1993.
[EG15] J.-H. Evertse and K. Győry. Unit equations in Diophantine number theory, volume 146
of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge,
2015. doi:10.1017/CBO9781316160749doi:10.1017/CBO9781316160749.
[Fer18] G. Fernandes. Méthode de Mahler en caractéristique non nulle: un analogue du théorème
de Ku. Nishioka. Ann. Inst. Fourier (Grenoble), 68(6):2553–2580, 2018.
[FS09] P. Flajolet and R. Sedgewick. Analytic combinatorics. Cambridge University Press, Cam-
bridge, 2009. doi:10.1017/CBO9780511801655doi:10.1017/CBO9780511801655.
[GL06] R. M. Guralnick and M. Lorenz. Orders of ﬁnite groups of matrices. In Groups, rings and
algebras, volume 420 of Contemp. Math., pages 141–161. Amer. Math. Soc., Providence, RI,
2006. doi:10.1090/conm/420/07974doi:10.1090/conm/420/07974.
[Kru48] W. Krull. Parameterspezialisierung in Polynomringen. II. Das Grundpolynom. Arch. Math.
(Basel), 1:129–137, 1948. doi:10.1007/BF02039524doi:10.1007/BF02039524.
[KS20] D. Krenn and J. Shallit. Decidability and k-Regular Sequences. 2020. arXiv:2005.09507arXiv:2005.09507.
[Mah29] K. Mahler. Arithmetische Eigenschaften der Lösungen einer Klasse von Funktionalgleichun-
gen. Math. Ann., 101(1):342–366, 1929. doi:10.1007/BF01454845doi:10.1007/BF01454845.
[Mah30a] K. Mahler. Arithmetische Eigenschaften einer Klasse transzendental-transzendenter Funk-
tionen. Math. Z., 32(1):545–585, 1930. doi:10.1007/BF01194652doi:10.1007/BF01194652.
[Mah30b] K. Mahler. Uber das Verschwinden von Potenzreihen mehrerer Veränderlichen in speziellen
Punktfolgen. Math. Ann., 103(1):573–587, 1930. doi:10.1007/BF01455711doi:10.1007/BF01455711.
[Mah40] K. Mahler. On a special functional equation. J. London Math. Soc., 15:115–123, 1940.
doi:10.1112/jlms/s1-15.2.115doi:10.1112/jlms/s1-15.2.115.
[MS78] A. Mandel and I. Simon. On ﬁnite semigroups of matrices. Theoret. Comput. Sci., 5(2):101–
111, 1977/78. doi:10.1016/0304-3975(77)90001-9doi:10.1016/0304-3975(77)90001-9.
[MZ75] R. McNaughton and Y. Zalcstein. The Burnside problem for semigroups. J. Algebra, 34:292–
299, 1975. doi:10.1016/0021-8693(75)90184-2doi:10.1016/0021-8693(75)90184-2.

A HEIGHT GAP THEOREM FOR COEFFICIENTS OF MAHLER FUNCTIONS 43

[Nis90] K. Nishioka. New approach in Mahler’s method. J. Reine Angew. Math., 407:202–219, 1990.
doi:10.1515/crll.1990.407.202doi:10.1515/crll.1990.407.202.
[Nis96] K. Nishioka. Mahler functions and transcendence, volume 1631 of Lecture Notes in Mathe-
matics. Springer-Verlag, Berlin, 1996. doi:10.1007/BFb0093672doi:10.1007/BFb0093672.
[Pas17] G. Pastuszak. The common invariant subspace problem and Tarski’s theorem. Electron. J.
Linear Algebra, 32:343–356, 2017. doi:10.13001/1081-3810.3439doi:10.13001/1081-3810.3439.
[Phi86] P. Philippon. Critères pour l’indépendance algébrique. Inst. Hautes Études Sci. Publ. Math.,
(64):5–52, 1986.
[Phi92] P. Philippon. Critères pour l’indépendance algébrique dans les anneaux diophantiens. C. R.
Acad. Sci. Paris Sér. I Math., 315(5):511–515, 1992.
[Phi15] P. Philippon. Groupes de Galois et nombres automatiques. J. Lond. Math. Soc. (2),
92(3):596–614, 2015. doi:10.1112/jlms/jdv056doi:10.1112/jlms/jdv056.
[Sch05] I. Schur. Über eine Klasse von endlichen Gruppen linearer Substitutionen. Berl. Ber.,
1905:77–91, 1905.
[Sie29] C. L. Siegel. Über einige Anwendungen diophantischer Approximationen. Abh. Preuss. Akad.
Wiss., Phys. Math. Kl., pages 41–69, 1929.
[Wal00] M. Waldschmidt. Diophantine approximation on linear algebraic groups, volume 326 of
Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathemati-
cal Sciences]. Springer-Verlag, Berlin, 2000. Transcendence properties of the exponential
function in several variables. doi:10.1007/978-3-662-11569-5doi:10.1007/978-3-662-11569-5.

Univ Lyon, Université Claude Bernard Lyon 1, CNRS UMR 5208, Institut Camille Jor-
dan, 43 blvd. du 11 novembre 1918, F-69622 Villeurbanne cedex, France
Email address: boris.adamczewski@math.cnrs.fr

Department of Pure Mathematics, University of Waterloo, Waterloo, ON, Canada N2L
3G1
Email address: jpbell@uwaterloo.ca

University of Graz, Institute for Mathematics and Scientific Computing, NAWI Graz,
Heinrichstrasse 36, 8010 Graz, Austria
Email address: daniel.smertnig@uni-graz.at
