<!-- source: https://export.arxiv.org/pdf/2308.13657v1.pdf | converted from PDF -->

arXiv:2308.13657v1  [cs.FL]  25 Aug 2023
Transcendence of Sturmian Numbers over an Algebraic Base

Florian Luca
School of Mathematics, University of the Witwatersrand
Private Bag 3, Wits 2050, South Africa
Research Group in Algebraic Structures and Applications
King Abdulaziz University, Jeddah, Saudi Arabia
ﬂorian.luca@wits.ac.za

Jo¨el Ouaknine
Max Planck Institute for Software Systems
Saarland Informatics Campus, Saarbr¨ucken, Germany
joel@mpi-sws.org

James Worrell
Department of Computer Science
University of Oxford, Oxford OX1 3QD, UK
jbw@cs.ox.ac.uk

Abstract
We consider numbers of the form Sβ(u) := ∑∞
n=0 un
βn for u = ⟨un⟩∞
n=0 a Sturmian sequence
over a binary alphabet and β an algebraic number with |β| > 1. We show that every such
number is transcendental. More generally, for a given base β and given irrational number θ we
characterise the Q-linear independence of sets of the form {
1, Sβ(u(1)), . . . , Sβ(u(k))}, where

u(1), . . . , u(k) are Sturmian sequences having slope θ.
We give an application of our main result to the theory of dynamical systems, showing
that for a contracted rotation on the unit circle with algebraic slope, its limit set is either
ﬁnite or consists exclusively of transcendental elements other than its endpoints 0 and 1. This
conﬁrms a conjecture of Bugeaud, Kim, Laurent, and Nogueira [3].

1 Introduction

A famous conjecture of Hartmanis and Stearns asserts that a real number α whose sequence of
digits can be produced by a linear-time Turing machine (in the sense that for all n, given input n in
unary the machine outputs the ﬁrst n digits of α in time O(n)) is either rational or transcendental.
This conjecture remains open and is considered to be very diﬃcult. A weaker version—proposed by
Cobham and eventually proved by Adamczewski, Bugeaud, and Luca [2]—asserts the transcendence
of an irrational automatic real number. The underlying intuition is that the sequence of digits of
an irrational algebraic number cannot be too simple. Indeed, the main technical result of [2] is
that over an integer base every number whose sequence of digits has linear subword complexity
is either rational or transcendental. Cobham’s conjecture is an immediate corollary, given that
automatic sequences have linear subword complexity.
In this paper we prove a transcendence result for numbers whose digit sequences are Sturmian
words (sometimes called mechanical words). Such words have minimal subword complexity among
non-ultimately periodic words and have a natural characterisation in terms of dynamical systems as
codings of rotations on the unit circle. The novelty of this work is that we handle expansions over
an arbitrary algebraic base rather than just an integer base. Here we are motivated by applications
to control theory and dynamical systems.
An inﬁnite sequence u = u0u1u2 . . . over a binary alphabet is said to be Sturmian if the number
p(n) of diﬀerent length-n factors in u satisﬁes p(n) = n + 1 for all n ∈ N, see [11]. Coven and

1

Hedlund [4] show that an inﬁnite word such that p(n) ≤ n for some n is necessarily ultimately
periodic. Thus Sturmian words have minimal subword complexity among non-ultimately periodic
words over a binary alphabet {0, 1}. The letters in a Sturmian word have a limiting frequency—the
limit frequency of the letter 1 is called the slope of the word. Related to this, Sturmian words
have a natural characterisation in terms of dynamical systems, namely as codings of the orbits of
irrational rotations on R/Z. Perhaps the best known example of a Sturmian word is the Fibonacci
word. This is deﬁned as the limit f∞ of the sequence (fn)
∞
n=0 of ﬁnite strings over the binary
alphabet {0, 1}, deﬁned by the recurrence f0 := 0, f1 := 01, and fn = fn−1fn−2 for all n ≥ 2.
The limit is well deﬁned since fn is a preﬁx of fn+1 for all n ∈ N. The Fibonacci word has slope
1/φ, where φ = 1+√5
2 is the golden ratio. It so happens that the Fibonacci word is morphic,
although it is not automatic.
Let u be a Sturmian word over a ﬁnite alphabet Σ ⊆ Q and let β ∈ Q be such that |β| > 1.
Then we call Sβ(u) := ∑∞
n=0 un
βn a Sturmian number with sequence of digits u and base β.1

Ferenczi and Mauduit [5] proved the transcendence of every number Sβ(u) over an integer base
β > 1. Their proof combined combinatorial properties of Sturmian sequences with a p-adic version
of the Thue-Siegel-Roth Theorem, due to Ridout. This result was strengthened by Bugeaud et
al. [3] to show Q-linear independence of sets of the form {1, Sβ(u(1)), Sβ(u(2))
} where u(1), u(2)

are Sturmian words having the same slope and β > 1 is an integer. In the case of an algebraic base
β, Laurent and Nogueria [12] observe that if u is a characteristic Sturmian word (cf. Section 3),
then the transcendence of Sβ(u) follows from a result of Loxton and Van der Poorten [8, Theorem
7] concerning transcendence of Hecke-Mahler series.
In this paper we give a common generalisation of the above three results. For every algebraic
base β and irrational slope θ we give suﬃcient and necessary conditions for Q-linear independence
of a set of Sturmian numbers {1, Sβ(u(1)), . . . , Sβ(u(k))
}, where u(1), . . . , u(k), where are Sturmian
sequences of slope θ. Our characterisation relies on a new combinatorial criterion on a sequence u
that ensures transcendence of Sβ(u) for β an algebraic base. Similar to [3], the Subspace Theorem
plays a major role in our argument. In [7] we give a more elaborate and powerful transcendence
criterion that allows proving Q-linear independence results about Sturmian numbers (again with
a common slope) over diﬀerent algebraic bases.
For a sequence u with linear subword complexity (i.e., such that lim inf n p(n)
n < ∞), it is
shown in [1] that Sβ(u) is transcendental under the condition that β is a Pisot number (i.e., a
real algebraic integer greater than one all of whose Galois conjugates have absolute value less than
one). Compared to the main result of this paper, the class of sequences considered by [1] is more
general (requiring merely linear subword complexity rather than the stronger condition of being
Sturmian), but the condition on the base is more restrictive (being a Pisot number rather than
merely an algebraic number of absolute value strictly greater than one).
In Section 5 we give an application of our main result to the theory of dynamical systems.
We consider the set C of limit points of a contracted rotation f on the unit interval, where f is
assumed to have an algebraic contraction factor. The set C is ﬁnite if f has a periodic orbit and
is otherwise a Cantor set, that is, it is homeomorphic to the Cantor ternary set (equivalently, it is
compact, nowhere dense, and has no isolated points). In the latter case we show that all elements
of C except its endpoints 0 and 1 are transcendental. Our result conﬁrms a conjecture of Bugeaud,
Kim, Laurent, and Nogueira, who proved a special case of this result in [3]. We remark that it is a
longstanding open question whether the actual Cantor ternary set contains any algebraic elements
other than 0 or 1.

2 Preliminaries

Let K be a number ﬁeld of degree d and let M (K) be the set of places of K. We divide M (K)
into the collection of inﬁnite places, which are determined either by an embedding of K in R or a
complex-conjugate pair of embeddings of K in C, and the set of ﬁnite places, which are determined
by prime ideals in the ring OK of integers of K.

1Our notion of Sturmian number is more permissive than that of Morse and Hedland [10] who restricted to the
case of an integer base b > 1 and digit sequence u over alphabet {0, . . . , b − 1}.

2

For x ∈ K and v ∈ M (K), deﬁne the absolute value |x|v as follows: |x|v := |σ(x)|1/d in case v
corresponds to a real embedding σ : K → R; |x|v := |σ(x)|2/d in case v corresponds to a complex-
conjugate pair of embeddings σ, σ : K → C; ﬁnally, |x|v := N (p)
−ordp(x)/d if v corresponds to a
prime ideal p in O and ordp(x) is the order of p as a divisor of the ideal xO. With the above
deﬁnitions we have the product formula: ∏v∈M(K) |x|v = 1 for all x ∈ K ∗. Given a set of places
S ⊆ M (K), the ring OS of S-integers is the subring comprising all x ∈ K such |x|v ≤ 1 for all
ﬁnite places v ∈ S.
For m ≥ 2 the absolute Weil height of x = (x1, . . . , xm) ∈ K m is deﬁned to be

H(x) := ∏

v∈M(K) max(|x1|v, . . . , |xm|v) .

This deﬁnition is independent of the choice of ﬁeld K containing x1, . . . , xm. Note the restriction
m ≥ 2 in the above deﬁnition. For x ∈ K we deﬁne its height H(x) to be H(1, x). For a non-zero
polynomial f = ∑s
i=0 aiX i ∈ K[X], where s ≥ 1, we deﬁne its height H(f ) to be the height of its
coeﬃcient vector (a0, . . . , as).
The following classical result of Schlickewei will be instrumental in our approach.

Theorem 1 (Subspace Theorem). Let S ⊆ M (K) be a ﬁnite set of places, containing all inﬁnite
places and let m ≥ 2. For every v ∈ S let L1,v, . . . , Lm,v be linearly independent linear forms in m
variables with algebraic coeﬃcients. Then for any ε > 0 the solutions x ∈ Om
S of the inequality

∏

v∈S
 m∏

i=1 |Li,v(x)|v ≤ H(x)
−ε

are contained in ﬁnitely many proper subspaces of K m.

We will also need the following more elementary proposition.

Proposition 2. [6, Proposition 2.3] Let f ∈ K[X] be a polynomial with at most k + 1 terms.
Assume that f can be written as the sum of two polynomials g and h, where every monomial of g
has degree at most d0 and every monomial of h has degree at least d1. Let β be a root of f that is
not a root of unity. If d1 − d0 > log(k H(f ))
log H(β) then β is a common root of g and h.

3 Stuttering Sequences

Let A ⊆ Q be a ﬁnite alphabet. An inﬁnite sequence u = u0u1u2 . . . ∈ A
ω is said to be stuttering
if for all w > 0 there exist sequences ⟨rn⟩
∞
n=0 and ⟨sn⟩
∞
n=0 of positive integers and d ≥ 2 such that:

S1 ⟨rn⟩
∞
n=0 is unbounded and sn ≥ wrn for all n ∈ N;

S2 for all n ∈ N there exist integers 0 ≤ i1(n) < . . . < id(n) ≤ sn such that the strings u0 . . . usn
and urn . . . urn+sn diﬀer at the set of indices ⋃d
j=1{ij(n), ij(n) + 1};

S3 we have id(n) − i1(n) = ω(log rn) and, writing i0(n) := 0 and id+1(n) := sn for all n, we have
ij+1(n) − ij(n) = ω(1) for all j ∈ {0, 1, . . . , d};

S4 for all n ∈ N and j ∈ {1, 2 . . . , d} we have uij (n) + uij (n)+1 = uij (n)+rn + uij (n)+rn+1.

The notion of a stuttering sequence is reminiscent of the transcendence conditions of [1, 3, 5]
in that it concerns periodicity in an inﬁnite word. Roughly speaking, a sequence u is stuttering if
for all w > 0 there are arbitrarily long preﬁxes of u that, modulo a ﬁxed number of mismatches,
comprise w repetitions of some ﬁnite word. The fact that the number w of repetitions is arbitrary
is key to our being able to prove transcendence results over an arbitrary algebraic base β. In
compensation, our condition allows repetitions with a certain number of discrepancies. This should
be contrasted with the notion of stammering sequence in [1, Section 4], where there is no allowance
for such discrepancies and in which the quantity corresponding to w is ﬁxed.

3

Example 3. To illustrate the notion of stuttering sequence, we recall the example of the Fi-
bonacci word. That this sequence is stuttering is a consequence of Theorem 4. Here in fact the
sequence of shifts ⟨rn⟩
∞
n=0 witnessing that the Fibonacci word is stuttering is the Fibonacci sequence
⟨1, 1, 2, 3, 5, . . .⟩. Below we align the Fibonacci word f∞ with its shift f (5)
∞ by r5 = 5, underlining
the mismatches which arise in consecutive pairs that satisfy Condition S4.

f∞ := 010010100100101001010010010100100101001 . . .

f (5)
∞ := 010010010100101001001010010010100101001 . . .

In what follows, we use the following representation of Sturmian words. Write I := [0, 1) for
the unit interval and given x ∈ R denote the integer part of x by ⌊x⌋ and the fractional part of
x by {x} := x − ⌊x⌋ ∈ I. Let 0 < θ < 1 be an irrational number and deﬁne the rotation map
T = Tθ : I → I by T (y) = {y + θ}. Given x ∈ I, the θ-coding of x is the inﬁnite sequence
u = u1u2u3 . . . deﬁned by un := 1 if T n(x) ∈ [0, θ) and un := 0 otherwise. As shown by Morse
and Hedlund, u is a Sturmian word and, up to changing at most two letters, all Sturmian words
over a binary alphabet arise as codings of the above type for some choice of θ and x. In particular,
for the purposes of establishing our transcendence results we may work exclusively with codings as
deﬁned above. The number θ is equal to the slope of the Sturmian word, as deﬁned in Section 1.
The θ-coding of 0 is in particular called the characteristic Sturmian word of slope θ.
The main result of this section is as follows:

Theorem 4. Let θ ∈ (0, 1) be irrational. Given a positive integer k, let c0, . . . , ck ∈ C and
x1, . . . , xk ∈ I. Suppose that xi − xj ̸∈ Zθ + Z for all i ̸= j. Writing ⟨u(i)
n ⟩
∞
n=0 for the θ-coding of
xi, for i = 1, . . . , k, deﬁne un := c0 + ∑k
i=1 ciu(i)
n for all n ∈ N. Then u = ⟨un⟩
∞
n=0 is stuttering.

Proof. We start by recalling some basic facts about the continued-fractions. Write [a0, a1, a2, a3, . . .]
for the simple continued-fraction expansion of θ. Given n ∈ N, we write pn
qn := [a0, a1, . . . , an] for
the n-th convergent. Then ⟨qn⟩
∞
n=0 is a strictly increasing sequence of positive integers such that
∥qnθ∥ = |qnθ − pn|, where ∥α∥ denotes the distance of a given number α ∈ R to the nearest integer.
We moreover have that qnθ − pn and qn+1θ − pn+1 have opposite signs for all n. Finally we have
the law of best approximation: q ∈ N occurs as one of the qn just in case ∥qθ∥ < ∥q′θ∥ for all q′

with 0 < q′ < q.
To establish that u is stuttering, given w > 0 we deﬁne ⟨rn⟩
∞
n=0 to be the subsequence of ⟨qn⟩
∞
n=0
comprising all terms qn such that ∥qnθ∥ = qnθ − pn > 0. Note that we either have rn = q2n for all
n or rn = q2n+1 for all n, so ⟨rn⟩
∞
n=0 is an inﬁnite sequence that diverges to inﬁnity. Next, write
d = (k + 1)w and for all n ∈ N deﬁne sn be the greatest number such that the words u0 . . . usn
and urn · · · urn+sn have Hamming distance at most 2d. Since u is not ultimately periodic, sn is
thereby well-deﬁned.
Condition S2. Denote the set of positions at which u0 . . . usn and urn . . . usn+rn diﬀer by

∆n := {
m ∈ {0, . . . , sn} : um ̸= um+rn} . (1)

We claim that for n suﬃciently large, m ∈ ∆n if and only if there exists ℓ ∈ {1, . . . , k} such that
one of the following two conditions holds:

(i) T m(xℓ) ∈ [1 − ∥rnθ∥, 1),

(ii) T m(xℓ) ∈ [θ − ∥rnθ∥, θ).

We claim furthermore that for all m there is most ℓ such that one of above conditions holds.
Assuming the claim, since T m(xℓ) ∈ [1 − ∥rnθ∥, 1) if and only if T m+1(xℓ) ∈ [θ − ∥rnθ∥, θ), it
follows that the elements of ∆n come in consecutive pairs, i.e., we can write

∆n =
 d⋃

j=1
{ij(n), ij(n) + 1} ,

where i1(n) < . . . < id(n) are the elements m ∈ ∆n that satisfy Condition (i) above for some ℓ.

4

It remains to prove the claim. To this end note that for a ﬁxed ℓ ∈ {1, . . . , k} we have u(ℓ)
m ̸=
u(ℓ)
m+rn iﬀ exactly one of T m(xℓ) and T m+rn(xℓ) lies in the interval [0, θ) iﬀ either Condition (i) or
Condition (ii) holds. Moreover, since xℓ − xℓ′ ̸= θ (mod 1) for ℓ ̸= ℓ′, we see that for n suﬃciently
large there is at most one ℓ ∈ {1, . . . , k} such that one of these two conditions holds. Equivalently,
for all m there is at most one ℓ such that u(ℓ)
m ̸= u(ℓ)
m+rn. We deduce that um ̸= um+rn if and only
if u(ℓ)
m ̸= u(ℓ)
m+rn for some ℓ ∈ {1, . . . , k}. This concludes the proof of the claim.
Condition S1. Our objective is to show that sn ≥ wrn for all n ∈ N. We have already
established that there are d = (k + 1)w distinct m ∈ ∆n that satisfy Condition (i), above, for some
ℓ ∈ {1, . . . , k}. Thus there exists ℓ0 ∈ {1, . . . , k} and ∆
′
n ⊆ ∆n such that |∆
′
n| ≥ w and all m ∈ ∆
′
n
satisfy Condition (i) for ℓ = ℓ0. In this case we have ∥(m1 − m2)θ∥ < ∥rnθ∥ for all m1, m2 ∈ ∆
′
n.
By the law of best approximation it follows that every two distinct elements of ∆
′
n have diﬀerence
strictly greater than rn. But this contradicts |∆
′
n| = w given that ∆
′
n ⊆ {0, 1, . . . , wrn}.
Condition S3. By deﬁnition of i1(n), . . . , id(n), for all j ∈ {1, . . . , d} there exists ℓj(n) ∈
{1, . . . , k} with T ij (n)(xℓj (n)) ∈ [1 − ∥rnθ∥, 1). Now, for all n ∈ N and 1 ≤ j1 < j2 ≤ d we have

∥(ij2 (n) − ij1 (n))θ + xℓj2 (n) − xℓj1 (n)∥ ≤ ∥rnθ∥ . (2)

We claim that the left-hand side of (2) is non-zero. Indeed, the claim holds if ℓj2 (n) = ℓj1 (n)
because θ is irrational, while the claim also holds in case ℓj2 (n) ̸= ℓj1 (n) since in this case we have
xℓj2 (n) − xℓj1 (n) ̸∈ Zθ + Z by assumption. Since moreover the right-hand side of (2) tends to zero
as n tends to inﬁnity, we have that ij2 (n) − ij1(n) = ω(1). On the other hand, if ℓj2(n) = ℓj1 (n)
then we even have ij2(n) − ij1(n) ≥ rn = ω(log rn) by the law of best approximation. Hence we
certainly have id(n) − i1(n) = ω(log rn).
Finally, deﬁning i0(n) := 0 we have i1(n)−i0(n) = ω(1) by the requirement that T i1(n)(xℓ1(n)) ∈
[1 − ∥rnθ∥, 1) and the fact that ∥rnθ∥ converges to 0. Setting id+1(n) := sn for all n, we also have
id+1(n) − id(n) = ω(1) by the maximality condition in the deﬁnition of sn.
Condition S4. Consider m ∈ ∆n satisfying Condition (i) above, i.e., such that T m(xℓ) ∈
[1 − ∥rnθ∥, 1) for some ℓ ∈ {1, . . . , k}. Then we have

u(ℓ)
m = 0, u(ℓ)
m+1 = 1 and u(ℓ)
m+rn = 1, u(ℓ)
m+rn+1 = 0 .

Moreover for all ℓ′ ̸= ℓ and n suﬃciently large we have

u(ℓ′)
m = u(ℓ′)
m+rn and u(ℓ′)
m+1 = u(ℓ′)
m+rn+1 .

We conclude that um + um+1 = um+rm + um+rn+1, establishing Condition S4.

4 A Transcendence Result

Theorem 5. Let A be a ﬁnite set of algebraic numbers and suppose that u ∈ A
ω is a stuttering
sequence. Then for any algebraic number β with |β| > 1, the sum α := ∑∞
n=0 un
βn is transcendental.

Proof. Suppose for a contradiction that α is algebraic. By scaling we can assume without loss of
generality that A consists solely of algebraic integers. Let K = Q(β) be the ﬁeld generated over Q
by β and write S ⊆ M (K) for the set comprising all inﬁnite places of K and all ﬁnite places of K
corresponding to prime-ideal divisors of the ideal βOK.
Applying the stuttering condition (for a value of w to be determined later), we obtain d ≥ 2 such
that for all n ∈ N there are positive integers rn, sn, i1(n), . . . , id(n) satisfying conditions S1–S4. By
condition S2, for all n if we deﬁne

cj(n) := (uij (n)+rn − uij (n)) + (uij (n)+rn+1 − uij (n)+1)β−1, j ∈ {1, 2, . . . , d}

and αn := ∑rn
j=0 ujβrn−j then we have
∣
∣
∣βrn α − α − αn − c1(n)β−i1(n) − · · · − cd(n)β−id(n)∣
∣
∣ < |β|−sn , (3)

5

Note that c1(n), . . . , cd(n) are non-zero by Condition S4. By passing to a subsequence we can
furthermore assume without loss of generality that c1 = c1(n), . . . , cd = cd(n) are constant, inde-
pendent of n.
To set up the application of the Subspace Theorem, deﬁne a family of linear forms Li,v, for
1 ≤ i ≤ 3 + d and v ∈ S, by

Li,v(x1, . . . , x3+d) := xi for all (i, v) ̸= (3, v0), and
L3,v0(x1, . . . , x3+d) := αx1 − αx2 − x3 − ∑d
j=1 cjx3+j .

Write bn := (
βrn , 1, αn, β−i1(n), . . . , β−id(n)) and let M ≥ 2 be an upper bound of the set of real
numbers {|γ|v : γ ∈ {β} ∪ A, v ∈ S} .

Then for all v ̸= v0 we have
|L3,v(bn)|v = |αn|v ≤
 rn∑

j=0 M j+1 ≤ M rn+2 ,

while |L3,v0(bn)|v0 ≤ |β|−sn/deg(β) by (3). Furthermore, for i ̸= 3, by the product formula we have∏
v∈S |Li,v(bn)|v = 1. Altogether we have

∏

v∈S
 d+3∏

i=1 |Li,v(bn)|v ≤ M (rn+2)|S| · |β|−sn/deg(β) . (4)

Since sn ≥ wrn we have that for w suﬃciently large the right-hand side of (4) is less than
|β|−sn/2 deg(β). On the other hand there exists a constant c such that the height of bn satisﬁes the
bound H(bn) ≤ |β|csn for all n. Thus there exists ε > 0 such that the right-hand side of (4) is
at most H(bn)
−ε for all n. Since bn is a vector of S-units we can apply the Subspace Theorem
to obtain a non-zero linear form L(x1, . . . , x3+d) with coeﬃcients in K such that L(bn) = 0 for
inﬁnitely many n ∈ N.
Denote by vars(L) ⊆ {x1, . . . , x3+d} the set of variables that appear in L with non-zero coeﬃ-
cient. We claim that x3 ∈ vars(L). Indeed, suppose for a contradiction that x3 ̸∈ vars(L). Then
for all n, L(bn) is a ﬁxed linear combination of the numbers βrn , 1, β−i1(n), . . . , β−id(n). By Item S3
the gaps beween successive exponents in these powers of β tend to inﬁnity with n and hence a
ﬁxed linear combination of such powers cannot vanish for arbitrarily large n.
We have that L(bn) is a linear combination of a most rn + d + 1 powers of β, whose re-
spective exponents lie in the set {0, 1, . . . , rn} ∪ {−i1(n), . . . , −id(n)}. From Item S3 there exists
j0 ∈ {1, . . . , d − 1} such that ij0+1(n) − ij0(n) = ω(log rn). By Proposition 2 the condition
L(bn) = 0 entails, for n suﬃciently large, that vars(L) is contained either in {x1, . . . , xj0+3} or in
{xj0+4, . . . , xd}. Since we know that x3 ∈ vars(L) the former inclusion applies.
We have established that x3 ∈ vars(L) ⊆ {x1, . . . , xj0+3}. Thus by a suitable linear combination
of the forms L3,v0 and L, so as to eliminate the variable x3, we obtain a non-zero linear form
L′(x1, . . . , x3+d) with algebraic coeﬃcients that does not mention x3 and such that |L′(bn)| <
|β|−sn for inﬁnitely many n. Note that L′(bn) is a ﬁxed linear combination of at most d + 2 powers
of β, with respective exponents in the set {rn, 0, −i1(n), . . . , −id(n)}. Moreover by Item S3 the gaps
between consecutive elements of this set tend to inﬁnity with n. It follows that |L′(bn)| ≫ |β|−id(n).
But since sn − id(n) = ω(1), this contradicts |L′(bn)| < |β|−sn .

We have the following immediate corollary of Theorem 4 and Theorem 5.

Theorem 6. Let β be an algebraic number with |β| > 1. Let 0 < θ < 1 be irrational and let

x1, . . . , xk ∈ I be such that xi − xj ̸∈ Zθ + Z for i ̸= j. For i = 1, . . . , k, deﬁne αi := ∑∞
n=0 u
(i)
n
βn ,

where ⟨u(i)
n ⟩
∞
n=0 is the θ-coding of xi. Then the set {1, α1, . . . , αk} is linearly independent over the
ﬁeld Q of algebraic numbers.
 6

1

δ

δ + λ − 1

0 1−δ
λ 1

Figure 1: A plot of fλ,δ : I → I

5 Application to Limit Sets of Contracted Rotations

Let 0 < λ, δ < 1 be real numbers such that λ + δ > 1. We call the map f = fλ,δ : I → I given
by f (x) := {λx + δ} a contracted rotation with slope λ and oﬀset δ. Associated with f we have
the map F = Fλ,δ : R → R, given by F (x) = λ{x} + δ + ⌊x⌋. We call F a lifting of f : it is
characterised by the properties that F (x + 1) = F (x) + 1 and {F (x)} = f ({x}) for all x ∈ R. The
rotation number θ = θλ,δ of f is deﬁned by

θ := lim
n→∞ F n(x0)
n ,

where the limit exists and is independent of the initial point x0 ∈ R.
If the rotation number θ is irrational then the restriction of f to the limit set ⋂
n≥0 f n(I) is
topologically conjugated to the rotation map T = Tθ : I → I with T (y) = {y + θ}. The closure of
the limit set is a Cantor set C = Cλ,δ, that is, C is compact, nowhere dense, and has no isolated
points. On the other hand, if θ is rational then the limit set C is the unique periodic orbit of f .
For each choice of slope 0 < λ < 1 and irrational rotation number 0 < θ < 1, there exists a unique
oﬀset δ such that δ + λ > 1 and the map f has rotation number θ. It is known that such δ must
be transcendental if λ is algebraic [12].
The main result of this section is as follows:

Theorem 7. Let 0 < λ, θ < 1 be such that λ is algebraic and θ is irrational. Let δ be the unique
oﬀset such that the contracted rotation fλ,δ has rotation number θ. Then every element of the limit
set Cλ,δ other than 0 and 1 is transcendental.

A special case of Theorem 7, in which λ is assumed to be the reciprocal of an integer, was
proven in [3, Theorem 1.2]. In their discussion of the latter result the authors conjecture the truth
of Theorem 7, i.e., the more general case in which λ may be algebraic. As noted in [3], while
Cλ,δ is homeomorphic to the Cantor ternary set, it is a longstanding open problem, formulated by
Mahler [9], whether the Cantor ternary set contains irrational algebraic elements.

Proof of Theorem 7. For a real number 0 < x < 1 deﬁne

ξx := ∑

n≥1 (⌈x + (n + 1)θ⌉ − ⌈x + nθ⌉) λ
n

ξ′
x := ∑

n≥1 (⌊x + (n + 1)θ⌋ − ⌊x + nθ⌋) λ
n .

Note that for all x the binary sequence ⟨ ⌈x + (n + 1)θ⌉ − ⌈x + nθ⌉ : n ∈ N ⟩ is the coding of −x − θ
by 1 − θ (as deﬁned in Section 3) and hence is Sturmian of slope 1 − θ. Similarly, the binary

7

sequence ⟨ ⌊x + (n + 1)θ⌋ − ⌊x + nθ⌋ : n ∈ N ⟩ is the coding of x + θ by θ and hence is Sturmian of
slope θ. Thus for all x, both ξx and ξ′
x are Sturmian numbers.
It is shown in [3, Lemma 4.2]2 that for every element of y ∈ Cλ,δ \ {0, 1}, either there exists
z ∈ Z and 0 < x < 1 with x ̸∈ Zθ + Z such that

y = z + ξ0 − ξ−x

or else there exists a strictly positive integer m and γ ∈ Q(β) such that

y = γ + (1 − β−m) ξ′
0 .

In either case, transcendence of y follows from Theorem 6.

Acknowledgements. The authors would like to thank Pavol Kebis and Andrew Scoones for
helpful feedback and corrections.

References

[1] B. Adamczewski and Y. Bugeaud, “On the complexity of algebraic numbers I, Expansions
in integer bases”, Ann. Math. 165, (2007), pp. 547–566.

[2] B. Adamczewski, Y. Bugeaud and F. Luca, “Sur la complexit´e des nombres alg´ebriques”,
C. R. Acad. Sci. Paris 339, (2004), pp. 11–14.

[3] Y. Bugeaud, D. H. Kim, M. Laurent and A. Nogueira. “On the Diophantine nature of
the elements of Cantor sets arising in the dynamics of contracted rotations”, Ann. Scuola
Normale Superiore di Pisa 5, Vol. XXII, (2021), pp. 1691–1704.

[4] E. M. Coven and G. A. Hedlund. “Sequences with minimal block growth”, Math Systems
Theory 7, (1973), pp. 138–153.

[5] S. Ferenczi and C. Mauduit, “Transcendence of Numbers with a Low Complexity Expan-
sion”, Journal of Number Theory 67 (1997), pp. 146–161.

[6] H W. Lenstra, “Finding small degree factors of lacunary polynomials”, Number Theory in
Progress: Diophantine Problems and Polynomials, Proceedings of the International Confer-
ence on Number Theory, (1997).

[7] F. Luca, J. Ouaknine and J. Worrell, “On the transcendence of a series related to Sturmian
words”, arXiv:2204.08268 (2022).

[8] J. H. Loxton and A. J. van der Poortrn, “Arithmetic properties of certain functions in
several variables III”, Bull. Austral. Math. Soc. 16, (1977), pp. 15–47.

[9] K. Mahler. “Some suggestions for further research.”, Bull. Austral. Math. Soc. 29 (1984),
pp. 101–108.

[10] M. Morse and G. A. Hedlund. “Symbolic dynamics”, Amer. J. Math 60, (1938), pp. 815–
866.

[11] M. Morse and G. A. Hedlund. “Symbolic dynamics II: Sturmian Trajectories.”, Amer. J.
Math 62(1), (1940), pp. 1–4.

[12] M. Laurent and A. Noguiera. “Rotation number of contracted rotations”, J. Modern Dy-
namics 12, (2018), pp. 175–191.

2The proof of the lemma is stated for β an integer but carries over without change for β algebraic.

8
