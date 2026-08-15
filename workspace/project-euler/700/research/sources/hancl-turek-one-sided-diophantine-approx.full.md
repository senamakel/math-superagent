<!-- source: https://arxiv.org/pdf/1809.01013 | converted from PDF -->

One–sided Diophantine approximations

Jaroslav Hančl
1, Ondřej Turek1,2,3

1 Department of Mathematics, Faculty of Science, University of Ostrava, 30. dubna
22, 701 03 Ostrava, Czech Republic
2 Department of Theoretical Physics, Nuclear Physics Institute, Czech Academy of
Sciences, 250 68 Řež, Czech Republic
3 Laboratory for Uniﬁed Quantum Devices, Kochi University of Technology, 782-8502
Kochi, Japan

E-mail: jaroslav.hancl@osu.cz, ondrej.turek@osu.cz

September 2018

Abstract. The paper deals with best one–sided (lower or upper) Diophantine
approximations of the ℓ-th kind (ℓ ∈ N). We use the ordinary continued fraction
expansions to formulate explicit criteria for a fraction p
q ∈ Q to be a best lower or
upper Diophantine approximation of the ℓ-th kind to a given α ∈ R. The sets of
best lower and upper approximations are examined in terms of their cardinalities and
metric properties. Applying our results in spectral analysis, we obtain an explanation
for the rarity of so-called Bethe–Sommerfeld quantum graphs.

Keywords: Diophantine approximation, continued fraction, quantum graph, Bethe–
Sommerfeld conjecture

1. Introduction

Diophantine approximations of real numbers is a classical concept in number theory. Its
basic idea consists in ﬁnding rational numbers with the property of being closer to a
given α ∈ R than any other rational number with a smaller denominator, in the sense
of the following deﬁnition.

Deﬁnition 1.1. A number p
q ∈ Q with p ∈ Z, q ∈ N is called a best Diophantine
approximation of the ﬁrst kind to a given α ∈ R if
∣
∣
∣
∣α − p
q
 ∣
∣
∣
∣ < ∣
∣
∣
∣α − p′

q′
 ∣
∣
∣
∣ (1)

holds for all p′

q′ ̸= p
q such that p′ ∈ Z, q′ ∈ N and q′ ≤ q. If the inequality (1) is replaced
with |qα − p| < |q′α − p′|, the corresponding fraction p
q is called a best Diophantine
approximation of the second kind to the number α.arXiv:1809.01013v2  [math.NT]  15 Jan 2019
One–sided Diophantine approximations 2

By their nature, Diophantine approximations are useful as good rational
approximations of irrational numbers (recall ancient estimates 22/7 and 355/113 for
π). They have also various other remarkable applications, for instance in solving
Diophantine equations. Similarly, they are used in the theory of Lagrange numbers
and Markoﬀ chains [4, 10, 11, 14], which plays an important role in computer science.
Recent development in mathematical physics (more speciﬁcally, in spectral analysis
of periodic quantum graphs [8]) led to a need for a mathematical approach that can be
referred to as “best one–sided Diophantine approximations of the ℓ-th kind”, where
ℓ ∈ N. While best Diophantine approximations, introduced in Deﬁnition 1.1, minimize
the quantity ∣
∣
∣α − p
q ∣
∣
∣ with respect to q within the set of all rational numbers p
q , best
“one–sided” Diophantine approximations (of the ﬁrst kind) aim at minimizing that
quantity within the subset of rational numbers with property p
q ≤ α, or p
q ≥ α. Let us
call such fractions best lower Diophantine approximations and best upper Diophantine
approximations, respectively.
The study of best one–sided Diophantine approximations is related to the theory
of asymmetric Diophantine approximations and their precision, which began to develop
in the 20th century. Segre [18] demonstrated that each irrational number has inﬁnitely
many rational approximations lying within certain asymmetric bounds. Robinson [16]
used continued fractions to provide an alternative proof of Segre’s theorem. Another
and very short proof was later published by Eggan and Niven [5]. Then Finkelshtein [9]
studied best upper Diophantine approximations of the 2nd kind. He found their
characterization in terms of so-called reduced regular continued fractions, the formalism
that is described in detail in Perron’s book [15] and a paper by Zurl [22].
It is likely that problems whose solutions rely on the idea of best lower and upper
Diophantine approximations of the ℓ-th kind will re-emerge in physics again in the
future, and probably many times. The aim of this paper is thus to establish a relevant
theory that could be used in future applications. However, our results are interesting
from a purely mathematical point of view as well, as they represent a counterpart to
the classical knowledge of standard Diophantine approximations.
Let us emphasize that the sets of best lower and upper Diophantine approximations
to a given α cannot be obtained in any simple manner from the set of all best Diophantine
approximations given by Deﬁnition 1.1. Indeed, there exist rational numbers that
are best lower or best upper Diophantine approximation to α, but they do not obey
Deﬁnition 1.1 (cf. Example 4.6). Therefore, the sets of best lower and upper Diophantine
approximations need to be constructed anew.
The paper is organized as follows. Sections 2 and 3 recall basic facts about
Diophantine approximations and continued fractions. In particular, we introduce the
notions of best lower and upper Diophantine approximations of the ℓ-th kind, and derive
their elementary properties. Section 4 presents a detailed description of the sets of best
lower and upper Diophantine approximations of the ﬁrst and second kind. In Section 5,
we study best lower and upper aproximations of the third kind. A particular attention
is then paid to quadratic irrational numbers (Section 6). Section 7 is devoted to best

One–sided Diophantine approximations 3

lower and upper approximations of the ℓ-th kind for ℓ ≥ 4. In Section 8 we introduce a
spectral problem in quantum mechanics that motivates and uses the developed theory.
The paper is concluded with a short summary and outlook (Section 9).
Throughout the paper, we use the standard symbols N, Z, Q and R for the sets of
positive integers, integers, rational numbers and real numbers, respectively. The symbol
N0 denotes the set of nonnegative integers.

2. Double–sided and one–sided best Diophantine approximations

Before proceeding to the central notion of this paper (Deﬁnition 2.2), we formulate a
natural extension of Deﬁnition 1.1.

Deﬁnition 2.1. Let α ∈ R, ℓ ∈ N and p
q ∈ Q for p ∈ Z, q ∈ N. We call the number p
q
a best Diophantine approximation of the ℓ-th kind to α if

qℓ−1 ∣
∣
∣
∣α − p
q
 ∣
∣
∣
∣ < (q′)ℓ−1 ∣
∣
∣
∣α − p′

q′
 ∣
∣
∣
∣ (2)

for all p′

q′ ̸= p
q , p′ ∈ Z, q′ ∈ N and q′ ≤ q.

Deﬁnition 2.1 serves as our starting point for introducing one–sided best
Diophantine approximations of the ℓ-th kind. A special case of Deﬁnition 2.2 for ℓ = 3
appeared for the ﬁrst time in [8]; here we consider a general ℓ ∈ N.

Deﬁnition 2.2. Let α ∈ R, ℓ ∈ N and p
q ∈ Q for p ∈ Z, q ∈ N. We say that

• p
q is a best lower Diophantine approximation of the ℓ-th kind to α if

0 ≤ qℓ−1 (
α − p
q
 ) < (q′)
ℓ−1 (
α − p′

q′
 ) (3)

for all p′

q′ ≤ α such that p′

q′ ̸= p
q , p′ ∈ Z, q′ ∈ N and q′ ≤ q.

• p
q is a best upper Diophantine approximation of the ℓ-th kind to α if

0 ≤ qℓ−1 ( p
q − α) < (q′)
ℓ−1 ( p′

q′ − α) (4)

for all p′

q′ ≥ α such that p′

q′ ̸= p
q , p′ ∈ Z, q′ ∈ N and q′ ≤ q.

We immediately have the following observation.

Observation 2.3. If p
q is a best lower Diophantine approximation of the ℓ-th kind to
α, then p = ⌊qα⌋. If p
q is a best upper Diophantine approximation of the ℓ-th kind to α,
then p = ⌈qα⌉.

It follows easily from Deﬁnition 2.2 that for any α ∈ R, a fraction p
q is a best
lower Diophantine approximation of the ℓ-th kind to α if and only if −p
q is a best upper
approximation of the ℓ-th kind to −α. Therefore, in the rest of the paper we can assume
α ≥ 0 without loss of generality.
For the sake of convenience, from now on we will usually drop the adjective
“Diophantine” in the term “Diophantine approximation”, and mostly use the following
abbreviations:

One–sided Diophantine approximations 4

• BLDA(ℓ) for “best lower Diophantine approximation of the ℓ-th kind”;

• BUDA(ℓ) for “best upper Diophantine approximation of the ℓ-th kind”.

Since Deﬁnition 2.2 has weaker requirements than Deﬁnition 2.1, we obviously have:

Observation 2.4. If p
q is a best approximation of the ℓ-th kind to α, then p
q is a BLDA(ℓ)
or a BUDA(ℓ) to α.

We emphasize, however, that the converse statement is not true. A BLDA(ℓ) or a
BUDA(ℓ) to α may not obey Deﬁnition 2.1, as we will see in Example 4.6.

Observation 2.5. If p
q is a best lower (upper) approximation of the ℓ-th kind to α, then
p
q is a best lower (respectively, upper) approximation of the ℓ′-th kind to α for all ℓ
′ < ℓ.

Proof. If 0 < q′ ≤ q and

qℓ−1 ∣
∣
∣
∣α − p
q
 ∣
∣
∣
∣ < (q′)ℓ−1 ∣
∣
∣
∣α − p′

q′
 ∣
∣
∣
∣ ,

then obviously

qℓ′−1 ∣
∣
∣
∣α − p
q
 ∣
∣
∣
∣ < (q′)
ℓ′−1 ∣
∣
∣
∣α − p′

q′
 ∣
∣
∣
∣

for all ℓ
′ < ℓ. The inequalities above immediately imply that if p/q obeys deﬁnition of
a best lower (upper) approximation of the ℓ-th kind to α, then it obeys the respective
deﬁnition for ℓ
′ as well.

In some situations one can easily specify a certain subset of Q such that each
BLDA(ℓ) (or BUDA(ℓ)) to a given α is an element of this subset. We will encounter such
situations in subsequent sections. Then the determination of BLDA(ℓ) and BUDA(ℓ)
to α can be simpliﬁed using Proposition 2.6 below.

Proposition 2.6. (i) Let SL ⊂ Q ∩ (−∞, α] contain all BLDA(ℓ) to α. Then p
q ∈ SL
is a BLDA(ℓ) to α if and only if

∀ p′

q′ ∈ SL : q′ ≤ q ⇒ qℓ−1 (
α − p
q
 ) < (q′)
ℓ−1 (
α − p′

q′
 ) . (5)

(ii) Let SU ⊂ Q ∩ [α, ∞) contain all BUDA(ℓ) to α. Then p
q ∈ SU is a BUDA(ℓ)
to α if and only if

∀ p′

q′ ∈ SU : q′ ≤ q ⇒ qℓ−1 ( p
q − α) < (q′)
ℓ−1 ( p′

q′ − α) .

Proof. (i) If p
q is a BLDA(ℓ), then (5) is true due to Deﬁnition 2.2.
Conversely, let p
q ∈ SL be not a BLDA(ℓ); we will show that p
q violates (5). Since

p
q is not a BLDA(ℓ), there exist p′, q′ ∈ Z such that α ≥ p′

q′ ̸= p
q , 0 < q′ ≤ q and (3) is
violated, i.e.,
 qℓ−1 (
α − p
q
 ) ≥ (q′)
ℓ−1 (
α − p′

q′
 ) . (6)

One–sided Diophantine approximations 5

Among the pairs (p′, q′) with this property, choose the pair for which the quantity
(q′)
ℓ−1 (α − p′

q′ ) is minimal. In case that several such pairs exist, let us consider the one

with minimal q′. This construction guarantees that the fraction p′

q′ is a BLDA(ℓ) to α.

Hence p′

q′ ∈ SL, and (5) is violated due to (6).
(ii) The proof is similar to (i).

3. Continued fractions

Any α ∈ R can be expressed in terms of a continued fraction, that is, in the form

α = a0 + 1
a1 + 1
a2+ 1
a3+ 1
···
 , (7)

where a0 ∈ Z and aj ∈ N for all j ∈ N. The fraction on the right hand side of (7) is
commonly represented using the notation [a0; a1, a2, a3, . . .].
It is easy to see that the sequence a0, a1, a2, . . . is ﬁnite if and only if α ∈ Q. For
ﬁnite continued fractions α = [a0; a1, a2, . . . , an] (n ∈ N), we usually assume that the last
term an is diﬀerent from 1 for the sake of uniqueness of the representation (7) (notice
that [a0; a1, a2, . . . , an−1, 1] = [a0; a1, a2, . . . , an−1 + 1]).
For a given continued fraction α = [a0; a1, a2, a3, . . .] and n ∈ N0, the fraction
pn
qn = [a0; a1, a2, . . . , an] is called the n-th convergent of α. If we set

p−1 = 1, p0 = a0 and q−1 = 0, q0 = 1,

the values of pn and qn (n ∈ N) are given by recurrent formulas

pn = anpn−1 + pn−2 and qn = anqn−1 + qn−2 . (8)

Numbers pn and qn obey the following well-known rules [13, eq. (8) and Thm. 6]:

qnpn−1 − pnqn−1 = (−1)n for all n ≥ 0, (9)
qn
qn−1 = [an; an−1, . . . , a1] for all n ≥ 1. (10)

The recurrent formulas (8) remain valid also if the terms an > 0 in (7) are not
integers [17, §3]. This will help us to derive an important identity in Proposition 3.1
below.

Proposition 3.1. For every n ≥ 1, we have

α − pn
qn = (−1)
n

q2
n ([an+1; an+2, . . .] + [0; an, an−1, . . . , a1]) . (11)

Proof. Since

α = [a0; a1, a2, . . . , an, an+1, an+2, . . .] = [a0; a1, a2, . . . , an, [an+1; an+2, . . .]] ,

formula (8) gives

α − pn
qn = pn[an+1; an+2, . . .] + pn−1
qn[an+1; an+2, . . .] + qn−1 − pn
qn . (12)

One–sided Diophantine approximations 6

Applying (9), we transform (12) into

α − pn
qn = (−1)
n

qn (qn[an+1; an+2, . . .] + qn−1) = (−1)
n

q2
n ([an+1; an+2, . . .] + qn−1
qn
 ) . (13)

Finally, (10) and trivial identity [an; an−1, . . . , a1]−1 = [0; an, an−1, . . . , a1] allows us
to rearrange the denominator on the right hand side of (13) into the required form
q2
n ([an+1; an+2, . . .] + [0; an, an−1, . . . , a1]) .

A semiconvergent (or intermediate fraction) of α is a fraction of the form
pnr + pn−1
qnr + qn−1 , where 0 < r < an+1. (14)

Note that if we set r = 0 (except for n = 0) or r = an+1 in (14), we get the convergents
pn−1
qn−1 and pn+1
qn+1 , respectively.
Let us resume well–known facts about values of convergents and semiconvergents:

Proposition 3.2. • [13, Thm. 4 and Thm. 8] The even-order convergents are smaller
or equal to α and form an increasing sequence. The odd-order convergents are
greater or equal to α and form a decreasing sequence. That is,
p0
q0 < p2
q2 < p4
q4 < · · · ≤ α ≤ · · · < p5
q5 < p3
q3 < p1
q1 .

• [13, p. 13–14] The fractions

pn−2
qn−2 = pn−1 · 0 + pn−2
qn−1 · 0 + qn−2 , pn−1 · 1 + pn−2
qn−1 · 1 + qn−2 , · · · , pn−1(an − 1) + pn−2
qn−1(an − 1) + qn−2 , pn−1an + pn−2
qn−1an + qn−2 = pn
qn

form a monotonous sequence that is increasing for even n and decreasing for odd
n.

Continued fractions are compared using the following criterion:

Proposition 3.3. (i) Let α = [a0; a1, a2, a3, . . .], β = [b0; b1, b2, b3, . . .] and n be the
minimal index such that an ̸= bn. Then

α < β ⇔ (n is even and an < bn) or (n is odd and an > bn).

(ii) If α = [a0; a1, a2, . . . , an] and β = [a0; a1, a2, a3, . . .], then α < β if and only if n is
even.

Proof. Proposition 3.3 is an immediate consequence of Proposition 3.1: we write
α − β = α − pn−1
qn−1 − (β − pn−1
qn−1 ) and apply (11) on both expressions α − pn−1
qn−1 and
β − pn−1
qn−1 .

One–sided Diophantine approximations 7

4. Approximations of the ﬁrst and second kind

We provide a complete characterization of best lower Diophantine approximations and
best upper Dipohantine approximations of the ﬁrst and second kind in this section.
We start from a necessary condition for p
q to be a best one–sided approximation of
the ﬁrst kind to a given α.‡

Theorem 4.1. Every best lower or upper approximation of the 1st kind to α is either
a convergent or a semiconvergent of α.

Proof. We will prove that every best lower approximation of the 1-st kind to α is a
convergent or a semiconvergent of α. The case of best upper approximations would be
treated similarly, so we omit it for the sake of brevity.
To prove this, we assume that p
q < α (p ∈ Z, q ∈ N) is neither a convergent nor a
semiconvergent of α, and show that p
q is not a BLDA(1) to α. Proposition 3.2 implies
that the smallest convergent or semiconvergent of α is p0
q0 = a0
1 . The proof thus falls into
2 cases:
• If p
q < a0
1 , we have

α − p
q > α − a0
1 and 0 < 1 ≤ q ;

i.e., p
q contradicts (3) (consider p′ = a0, q′ = 1). So p
q is not a BLDA(1).
• Let p
q < α lie between two adjacent fractions from the set of convergents and
semiconvergents. That is, due to Proposition 3.2, p
q satisﬁes

pnr + pn−1
qnr + qn−1 < p
q < pn(r + 1) + pn−1
qn(r + 1) + qn−1
for some odd n and r ∈ {0, 1, . . . , an+1 − 1}. Furthermore,

p
q − pnr + pn−1
qnr + qn−1 < pn(r + 1) + pn−1
qn(r + 1) + qn−1 − pnr + pn−1
qnr + qn−1 = pnqn−1 − qnpn−1
(qnr + qn−1) (qn(r + 1) + qn−1)

= 1
(qnr + qn−1) (qn(r + 1) + qn−1)
 (15)

(in the last step, we used (9) together with the odd parity of n). At the same time, we
have p
q − pnr + pn−1
qnr + qn−1 = p(qnr + qn−1) − q(pnr + pn−1)
q (qnr + qn−1) ≥ 1
q (qnr + qn−1) . (16)

Combining estimates (15) and (16), we get

qn(r + 1) + qn−1 < q .

Therefore, considering p′ = pn(r + 1) + pn−1 and q′ = qn(r + 1) + qn−1, we conclude that
p
q < α contradicts (3). Hence p
q is not a BLDA(1) to α.

Theorem 4.1 with Observation 2.5 has the following corollary.

‡ A statement equivalent to Theorem 4.1 was recently published independently by S. Bettin in [2].

One–sided Diophantine approximations 8

Corollary 4.2. For all ℓ ≥ 1, every BLDA(ℓ) and BUDA(ℓ) to α is a convergent or a
semiconvergent of α.

In the next step, we ﬁnd a suﬃcient condition for best one–sided approximations
of the second kind.

Theorem 4.3. Every convergent and semiconvergent of α is a best lower or upper
approximation of the 2nd kind to α.

Proof. From Corollary 4.2 we obtain that the only possible candidates for best one–sided
approximations of the second kind to α are the fractions
pnr + pn−1
qnr + qn−1 (17)

where n ∈ N0 and r ∈ {0, 1, . . . , an+1 − 1}. Furthermore, with regard to Proposition 3.2,
number n takes odd values for BLDA(2) and even values for BUDA(2). Let us focus on
odd n; the case of even n is similar.
We will use Proposition 2.6(i) where SL = { pnr+pn−1
qnr+qn−1 : n is odd
}
. Our goal is to
show that all elements of SL are BLDA(2) to α. With regard to condition (5), we will
prove that if we arrange the elements of SL in a sequence with growing denominators,
then the quantities

(qnr + qn−1) (α − pnr + pn−1
qnr + qn−1
 ) (18)

strictly decrease.
For a given n, the denominators qnr + qn−1 obviously grow as r grows from 0 to
an+1 − 1. Furthermore, for the choice r = an+1 we have qnan+1 + qn−1 = qn+1 =
qn+2 · 0 + qn+1. In other words, taking r = an+1 for a given n is equivalent to increasing
n by 2 (i.e., to the next odd value) and taking r = 0. Consequently, if we arrange the
elements of SL according to their denominators, then any two consecutive elements can
be written as pnr + pn−1
qnr + qn−1 and pn(r + 1) + pn−1
qn(r + 1) + qn−1
for some odd n and r ∈ {0, 1, . . . , an+1 − 1}. The monotony of the quantities (18) in
terms of the denominators qnr + qn−1 can be thus veriﬁed by proving the inequality

(qn(r + 1) + qn−1) (
α − pn(r + 1) + pn−1
qn(r + 1) + qn−1
 ) < (qnr + qn−1) (
α − pnr + pn−1
qnr + qn−1
 ) (19)

for every odd n and r ∈ {0, 1, . . . , an+1 − 1}. A straightforward manipulation leads to a
simpliﬁcation of (19) to

αqn − pn < 0 . (20)

Since n is odd, we have pn
qn > α (see Prop. 3.2); thus inequality (20) holds true.

Theorem 4.3 together with Observation 2.5 for ℓ = 2 and ℓ
′ = 1 imply:

One–sided Diophantine approximations 9

Corollary 4.4. Every convergent or a semiconvergent of α is either a BLDA(1) or a
BUDA(1) to α.

Now we are ready to give a complete description of the set of best lower and upper
approximations, both of the ﬁrst and the second kind:

Theorem 4.5. Let α = [a0; a1a2, a3, . . .] ∈ R. For every n ∈ N0, let pn
qn be the n-th
convergent of α.

(i) The set of best lower approximations of the 1st kind to α is equal to the set of best
lower approximations of the 2nd kind to α. Both the sets consist of fractions
pnr + pn−1
qnr + qn−1 (0 ≤ r < an+1) (21)

where n is odd.

(ii) The set of best upper approximations of the 1st kind to α is equal to the set of best
upper approximations of the 2nd kind to α. Both the sets consist of fractions (21)
for an even n, except for the pair (n, r) = (0, 0).

Proof. Let ℓ be 1 or 2. Corollary 4.4 implies that every best lower or upper
approximations of the ℓ-th kind to α has form (21). Conversely, each fraction (21)
is a BLDA(ℓ) or a BUDA(ℓ) to α due to Corollary 4.2. Finally, from Proposition 3.2
we obtain that odd numbers n in (21) correspond to BLDA(ℓ), and even numbers n
correspond to BUDA(ℓ).

Let us compare our results on best one–sided approximations to classical results on
“double–sided” best approximations. It is well known that:

• The set of best approximations of the ﬁrst kind to an α consists of all convergents
of α (except for p0
q0 when α = a0 + 1
2) and some semiconvergents. [13, Thm. 15]

• Fraction p
q is a best approximation of the second kind to the number α if and only
if p
q is a convergent of α, except for p0
q0 when α = a0 + 1
2. [13, Thm. 16 and 17]

By contrast, as we found in Theorem 4.5, the set of all one–sided best approximations
of the ﬁrst kind and the set of all one–sided best approximations of the second kind
both coincide with the set of all convergents and semiconvergents of α. We illustrate
the result with an example.

Example 4.6. If α = π = [3; 7, 15, 1, 292, 1, . . .], fractions (21) for n = 0 and r = 1, . . . , 7
are 4
1 , 7
2 , 10
3 , 13
4 , 16
5 , 19
6 , 22
7 . (22)

Using Deﬁnition 1.1, it is easy to check that among the fractions listed in (22), only
13
4 , 16
5 , 19
6 , 22
7 are best approximations to π of the 1st kind, and only the fraction 22
7 is
a best approximation to π of the second kind. But all the fractions (22)—and no other
with denominator q ≤ 7—are BUDA(1). The same is true for BUDA(2).

One–sided Diophantine approximations 10

Remark 4.7. Best lower and upper Diophantine approximations of the 2nd kind (which
coincide with one–sided approximations of the 1st kind due to Theorem 4.5) have a nice
geometric interpretation, see Figure 1. Consider the graph of linear function f (x) = αx
and a grid of points [x, y] with integer coordinates. For each point [x, y] of the grid,
one can measure its vertical distance to the graph of f (x). Then a fraction p
q for p ∈ Z,
q ∈ N is a BLDA(2) to α if and only if [q, p] lies on or below the graph of f (x) and its
vertical distance to the graph of f (x) is smaller than the vertical distance between the
graph and any other point [q′, p
′] of the grid lying on or below the graph and having
coordinate 0 < q′ ≤ q. In other words, the point [q, p] has smaller vertical distance from
the graph of f (x) than any other point [q′, p
′] ̸= [0, 0] of the grid lying in the triangle
with vertices [0, 0], [q, 0] and [q, f (q)].

(a) (b)

Figure 1. Geometric meaning of best lower (a) and upper (b) approximations of the
2nd kind (plotted for α = √5). Regarding BLDA(2) (Figure (a)), take grid points
[q, p] ∈ N2 that lie immediately below the graph of f (x) = αx, i.e., [1, 2], [2, 4], [3, 6],
[4, 8] and [5, 11]. Their vertical distances to the graph are approximately 0.24, 0.47,
0.71, 0.94 and 0.18, respectively. The minimal distance with respect to 0 < q′ ≤ q
is thus attained for q = 1 and q = 5. Hence 2
1 and 11
5 are the only BLDA(2) to
α = √5 among all fractions having denominators q ≤ 5. For BUDA(2) (Figure (b)),
consider grid points that lie immediately above the graph of f (x) = αx. Their vertical
distances to the graph are approximately 0.76, 0.53, 0.29, 0.06 and 0.82, respectively.
The minimality with respect to 0 < q′ ≤ q is attained for values q = 1, 2, 3, 4 and not
for q = 5; hence 3
1 , 5
2 , 7
3 and 9
4 are BUDA(2) to √5, while 12
5 is not.

Similarly, p
q is a BUDA(2) to α if and only if [q, p] lies on or above the graph of
f (x) and its vertical distance to the graph of f (x) is than the vertical distance between
the graph and any other point [q′, p
′] of the grid lying on or above the graph and having
coordinate 0 < q′ ≤ q.

One–sided Diophantine approximations 11

Remark 4.8. We were notiﬁed by a referee that the results presented in this section
are to some extent known among number theorists in connection with other problems.
This concerns in particular the structure of best one–sided approximations of the second
kind. But it is not simple to ﬁnd them with proofs in the literature.
Furthermore, there exists an alternative characterization of the set of best upper
approximations of the second kind, which was obtained by Y. Y. Finkelshtein within
the context of so-called Klein polygons§. The approximations are expressed in terms of
reduced regular continued fractions, instead of ordinary regular continued fractions that
are used in the present paper. However, the only accessible material on Finkelshtein’s
result regarding BUDA(2) seems to be a short note [9] where no proofs are provided.

5. Approximations of the third kind

Theorem 5.1. We have:

(i) Every best lower approximation of the 3rd kind to α is an even–order convergent of
α.

(ii) Every best upper approximation of the 3rd kind to α is either ⌈α⌉
1 or an odd–order
convergent of α.

Remark 5.2. The ﬁrst version of Theorem 5.1 appeared in [8, Prop. 3.5 and 3.6], but
the proof there turns out to be mistaken∥.

Proof of Theorem 5.1. (i) Let α = [a0; a1, a2, . . .] ∈ R. Due to Theorem 4.5 and
Observation 2.5, each BLDA(3) to α is given as
pnr + pn−1
qnr + qn−1 (23)

for some odd n ∈ N and r satisfying 0 ≤ r < an+1. We shall show that if fraction (23) is
a semiconvergent, i.e., if r satisﬁes 0 < r < an+1, then (23) is not a BLDA(3) to α. To
prove this, we will demonstrate that fraction (23) with 0 < r < an+1 violates (3) with
ℓ = 3 for the choice p′ = pn−1, q′ = qn−1. That is, we shall verify inequality

(qnr + qn−1)
2 (
α − pnr + pn−1
qnr + qn−1
 ) ≥ q2
n−1
 (
α − pn−1
qn−1
 ) (24)

for every r = 1, . . . , an+1 − 1. It is easy to transform (24) into

r ≤ 2qnqn−1α − qnpn−1 − qn−1pn
qn(pn − qnα) for every r = 1, . . . , an+1 − 1,

which is further equivalent to

an+1 − 1 ≤ 2qnqn−1α − qnpn−1 − qn−1pn
qn(pn − qnα) . (25)

§ We thank the referee for pointing our attention to that result.
∥ The argument given in [8, Prop. 3.5] relies on Lemma 3.4 ibidem. However, there is a misprint in
[8, Lemma 3.4], namely, the term an should read as an+1 everywhere in its formulation and proof (4
occurrences). The dependence on a mistaken lemma makes the proof of [8, Prop. 3.5] invalid.

One–sided Diophantine approximations 12

From identity (9) we obtain that the numerator on the right hand side of (25) is equal
to 2qnqn−1α − 2qn−1pn + 1. Therefore, (25) can be rewritten as

an+1 − 1 ≤ −2 qn−1
qn + 1
qn(pn − qnα) . (26)

Now we express the right hand side of (26) in terms of α = [a0; a1, a2, . . .]. Equations (10)
and (11) together with the identity [an; an−1, . . . , a1]−1 = [0; an, an−1, . . . , a1] yield that
we can write the right hand side of (26) as

−2[0; an, an−1, . . . , a1] + [an+1; an+2, . . .] + [0; an, an−1, . . . , a1] .

Hence (26) has the form

an+1 − 1 ≤ −[0; an, an−1, . . . , a1] + an+1 + [0; an+2, an+3, . . .] .

This inequality can be simpliﬁed to

[0; an, an−1, . . . , a1] ≤ [1; an+2, an+3, . . .] ,

which is valid for any α = [a0; a1, a2, . . .].
(ii) We start again from Theorem 4.5 and Observation 2.5, which imply that each
BUDA(3) to α has the form (23) for some even n ∈ N0 and 0 ≤ r < an+1. Our goal is
to prove that the semiconvergents, which correspond to 0 < r < an+1, are either equal
to ⌈α⌉
1 or violate the deﬁnition of BUDA(3). The proof falls into three cases: {n is even
nonzero}; {n = 0 and r > 1}; {n = 0 and r = 1}.
• Let n be even positive integer. We prove that each fraction (23) with 0 < r < an+1
violates (4) with ℓ = 3 and p′ = pn−1, q′ = qn−1. Similarly as in part (i), but this time
for an even n, we verify the inequality

(qnr + qn−1)
2 ( pnr + pn−1
qnr + qn−1 − α) ≥ q2
n−1
 ( pn−1
qn−1 − α) (27)

for every r = 1, . . . , an+1 − 1. We again transform (27) into

an+1 − 1 ≤ −2 qn−1
qn + 1
qn(qnα − pn) (28)

and subsequently rewrite (28) in the form

[0; an, an−1, . . . , a1] ≤ [1; an+2, an+3, . . .] ,

which is valid for any α = [a0; a1, a2, . . .].
• If n = 0 and r > 1, we will show that fraction (23), i.e.,
p0r + p−1
q0r + q−1 = a0r + 1
1 · r + 0 = a0r + 1
r ,

violates condition (4) with ℓ = 3 for the choice p′ = a0 + 1, q′ = 1. To prove this we
shall verify inequality

r2 ( a0r + 1
r − α) ≥ 1
2 ( a0 + 1
1 − α) ,

One–sided Diophantine approximations 13

which is equivalent to

(r − 1) [(r + 1)(a0 − α) + 1] ≥ 0 . (29)

Since 1 < r ≤ a1 − 1 and α ≤ a0 + 1
a1 , we have (r + 1)(a0 − α) + 1 ≥ a1 · −1
a1 + 1 ≥ 0.
So (29) holds.
• Finally, consider (23) for n = 0 and r = 1, i.e.,
p0 · 1 + p−1
q0 · 1 + q−1 = a0r + 1
1 · 1 + 0 = a0 + 1
1 . (30)

If n = 0, the case r = 1 is possible only when a1 > 1 (see (14)). Hence necessarily
α = [a0; a1, . . .] = a0 + 1
a1+··· /∈ Z. In this case semiconvergent (30) is equal to ⌈α⌉
1 .

It is easy to check that the necessary condition from Theorem 5.1 is not suﬃcient.
We formulate a necessary and suﬃcient condition in Proposition 5.3 below.

Proposition 5.3. Let n be a positive integer and α = [a0; a1, a2, . . .]. Then we have:

(i) A convergent pn
qn is the best lower approximation of the 3rd kind to α if and only if
n is even and

[ak+1; ak+2, . . .] + [0; ak, ak−1, . . . , a1] < [an+1; an+2, . . .] + [0; an, an−1, . . . , a1] (31)

holds for all k = n − 2, n − 4, . . . , 2, 0.

(ii) A convergent pn
qn is the best upper approximation of the 3rd kind to α if and only if
n is odd and (31) holds for all k = n − 2, n − 4, . . . , 3, 1.

Proof. (i) From Theorem 5.1 we obtain that the only possible candidates for BLDA(3)
to α are even–order convergents of α. Therefore, setting SL = { pn
qn : n is even} in
Proposition 2.6(i), we infer that pn
qn for an even n is a BLDA(3) if and only if

q2
n
 (
α − pn
qn
 ) < q2
k
 (
α − pk
qk
 ) for all even k < n.

This and formula (11) imply

1
[an+1; an+2, . . .] + [0; an, an−1, . . . , a1] < 1
[ak+1; ak+2, . . .] + [0; ak, ak−1, . . . , a1]

for all even k < n, and criterion (i) follows immediately.
(ii) From Theorem 5.1 we get the set of candidates for BUDA(3) to α in the form
SU = { pn
qn : n is odd
} ∪ { ⌈α⌉
1 }. Proposition 2.6(ii) then implies that pn
qn with an odd n
is a BUDA(3) if and only if

q2
n
 (
α − pn
qn
 ) < q2
k
 (
α − pk
qk
 ) for all odd k < n (32a)

and q2
n
 (pn
qn − α) < 1
2 ( ⌈α⌉
1 − α) . (32b)

One–sided Diophantine approximations 14

Now we will show that (32a) implies (32b). To prove this, we will demonstrate that

1
2 ( ⌈α⌉
1 − α) ≥ q2
1
 ( p1
q1 − α) . (33)

Since p1
q1 = a0a1+1
a1 , we easily rewrite (33) as

a0 + 1 − α ≥ a1(a0a1 + 1 − a1α) ,

which is equivalent to

(a1 − 1)[(a1 + 1)(α − a0) − 1] ≥ 0 . (34)

In order to prove (34), we estimate

α − a0 = 1
a1 + 1
a2+··· > 1
a1 + 1 , (35)

where the term 1
a2+··· is smaller than 1, because an expansion α = [a0; a1, 1] with the
last term a2 = 1 is excluded, see Section 3. With regard to (35), inequality (34) is
true, so (33) is veriﬁed. We conclude that pn
qn for an odd n is a BUDA(3) if and only if
(32a) holds true. Finally, (32a) corresponds to (31) by virtue of (11); see part (i) of the
proof.

The following proposition will be used in a physical application in Section 8.

Proposition 5.4. Almost all α ∈ R have inﬁnitely many BLDA(3) and inﬁnitely many
BUDA(3).

Proof. We prove that the set M = {α; α has ﬁnitely many BLDA(3)} has zero Lebesgue
measure. Let α = [a0; a1, a2, a3, . . .] ∈ M\Q be ﬁxed. For every even n, let us set

P (n) = [an+1; an+2, . . .] + [0; an, an−1, . . . , a1] (36)

and deﬁne H(n) = max{P (n − 2), P (n − 4), . . . , P (2), P (0)}. We have immediately that
H(n) ≥ H(n − 2) for every even n ∈ N.
If n has property H(n) > H(n − 2), then (31) holds for all k = n − 2, n − 4, . . . , 2, 0;
thus pn
qn is a BLDA(3) to α due to Proposition 5.3. Our assumption α ∈ M implies that
there are only ﬁnitely many such n. Therefore, the sequence {H(2n)}∞
n=1 is eventually
constant.
Consequently, values P (n) for even n are bounded. From (36) we obtain that every
α ∈ M\Q has bounded terms at odd positions of its continued fraction expansion. Hence
M ⊂ Q ∪ ⋃∞
j=1 Mj where for each j ∈ N we have Mj = {α; α = [a0; a1, a2, . . .], a2k <
j for every k ∈ N}. But Theorem 2.1 from [12]—see also Remark 2.1 and paragraph
after Remark 2.1 of [12]—yields that Mj has zero Lebesgue measure for every j ∈ N.
Hence the set M has zero Lebesgue measure.
The proof that almost all α ∈ R have inﬁnitely many BUDA(3) is similar.

One–sided Diophantine approximations 15

6. Approximations of the third kind for quadratic numbers

The criterion derived in Proposition 5.3 is particularly convenient if the continued
fraction of α has some regular structure. A prominent example are eventually periodic
continued fractions,

α = [a0; a1, . . . , am, am+1, . . . , am+h] . (37)

Due to a classical result by Euler and Lagrange, periodic continued fractions correspond
to quadratic irrational numbers, i.e., irrational roots of polynomials x2 + ux + v with
u, v ∈ Q.
In this section, we apply Proposition 5.3 on a general quadratic irrational number
α to ﬁnd bounds on the number of its best upper and lower approximations of the third
kind. In particular, we show that the set of BLDA(3) and the set of BUDA(3) cannot
be both inﬁnite.

Theorem 6.1. Let α be given as (37) for some non-negative integer m and a positive
integer h.
(i) If m = 0; or m is odd and am < am+h; or m is even nonzero and am > am+h,
then the number of best upper approximations of the 3rd kind to α is ﬁnite.
(ii) If m is odd and am > am+h; or m is even nonzero and am < am+h, then the
number of best lower approximations of the 3rd kind to α is ﬁnite.
(iii) A quadratic irrational number cannot have inﬁnitely many BLDA(3) and
inﬁnitely many BUDA(3) at the same time.

Proof. (i) Due to Theorem 5.1, each BUDA(3) to α is either ⌈α⌉
1 or an odd–order
convergent of α. We will show that for any odd n > m + 2h, pn
qn is not a BUDA(3)
to α.
Let us thus consider an arbitrary odd n > m + 2h. According to Proposition 5.3, pn
qn
is a BUDA(3) only if (31) holds for every odd k < n. We take in particular k = n − 2h
(one can take also k = n−h if h is even) and rewrite (31) in terms of (n, k) = (k +2h, k).
We obtain

[ak+1; ak+2, . . .]+[0; ak, ak−1, . . . , a1] < [ak+2h+1; ak+2h+2, . . .]+[0; ak+2h, ak+2h−1, . . . , a1] .(38)

Since k > m (recall that n > m + 2h), we use the periodicity of representation (37)
to conclude that [ak+1; ak+2, . . .] = [ak+2h+1; ak+2h+2, . . .]. This allows us to simplify
condition (38) to

[0; ak, ak−1, . . . , a1] < [0; ak+2h, ak+2h−1, . . . , a1] . (39)

Now we shall demonstrate that (39) is violated in all the three cases from statement (i),
i.e., {m = 0}; {m is odd and am < am+h}; {m is even nonzero and am > am+h}.
• If m = 0, we have [0; ak+2h, ak+2h−1, . . . , a1] = [0; ak, ak−1, . . . , a1, ah, . . . , a1, ah, . . . , a1].
Then condition (39) takes the form

[0; ak, ak−1, . . . , a1] < [0; ak, ak−1, . . . , a1, ah, . . . , a1, ah, . . . , a1] . (40)

One–sided Diophantine approximations 16

Since k is odd, inequality (40) is false in view of Proposition 3.3(ii). Thus pn
qn is not a
BUDA(3) to α.
• Let m > 0. Then we have

[0; ak, ak−1, . . . , a1] = [0; ak, ak−1, . . . , am+1, am, am−1, . . . , a1]

and

[0; ak+2h, ak+2h−1, . . . , a1] = [0; ak, ak−1, . . . , am+1, am+h, . . . , am+1, am+h, . . . , am+1, am, . . . , a1] .

Hence (39) has the form

[0; ak, ak−1, . . . , am+1, am, am−1, . . . , a1]

< [0; ak, ak−1, . . . , am+1, am+h, . . . , am+1, am+h, . . . , am+1, am, . . . , a1] . (41)

Now if m is odd and am < am+h, we have that k − m + 1 is odd and am < am+h, thus
(41) is false by Proposition 3.3(i). Similarly, if m is even and am > am+h, we have that
k − m + 1 is even and am > am+h, so (41) is again false. Therefore, in either case pn
qn is
not a BUDA(3) to α.
(ii) The proof is similar to (i), with the main diﬀerence that we examine even
n > m − 2h, thus k = n − 2h is even. One proves that no convergent pn
qn with n > m + 2h
is a BLDA(3) to α.
(iii) A quadratic irrational number has an eventually periodic continued fraction
of form (37), so statements (i) and (ii) apply. The conditions listed in (i) and (ii) are
complementary. As one of them is always satisﬁed, either the number of BLDA(3) to α
or the number of BUDA(3) to α must be ﬁnite.

Proposition 6.2. Let α = [a0; a1, . . . , am, am+1, . . . , am+h] for m ∈ N0 and h ∈ N.
(i) If α has inﬁnitely many BLDA(3), then α has at most (1+⌈m/2⌉+h) BUDA(3).
(ii) If α has inﬁnitely many BUDA(3), then α has at most (⌊m/2⌋ + h) BLDA(3).

Proof. (i) We will apply Theorem 6.1. The case of inﬁnitely many BLDA(3) to α
corresponds to case (i) of Theorem 6.1. The proof of Theorem 6.1(i) then implies
that every BUDA(3) to α is either ⌈α⌉
1 or a convergent pn
qn of α for an odd n ≤ m + 2h.
In total there are at most 1 + ⌈ m+2h
2 ⌉ possibilities.
(ii) Inﬁnitely many BUDA(3) to α correspond to case (ii) of Theorem 6.1. So each
BLDA(3) to α must be a convergent pn
qn of α for an even n ≤ m + 2h. Hence we get at
most ⌊ m+2h
2 ⌋ possibilities.

Remark 6.3. The bounds on the number of BLDA(3) and BUDA(3) to α given in
Proposition 6.2 can be improved, but we will not go into detail for the sake of simplicity
of the proof.

One–sided Diophantine approximations 17

7. Approximations of the ℓ-th kind for ℓ ≥ 4

Theorem 5.1 together with Observation 2.5 imply that every best lower or upper
approximation of the ℓ-th kind to α for ℓ ≥ 4 is either a convergent of α or ⌈α⌉
1 . Note
at ﬁrst that the sets of BLDA(ℓ) and BUDA(ℓ) to α are always nonempty:

Observation 7.1. For every ℓ ∈ N and α ∈ R, p0
q0 = ⌊α⌋
1 is a BLDA(ℓ) to α and ⌈α⌉
1 is
a BUDA(ℓ) to α.

However, as ℓ grows beyond 3, the structure of the sets of BLDA(ℓ) and BUDA(ℓ)
to a given α = [a0; a1, a2, a3, . . .] becomes increasingly dependent on the values of aj.
Consider the following proposition:

Proposition 7.2. Let ℓ ≥ 4. For a given α = [a0; a1, a2, a3, . . .], set

Cn(ℓ) = qℓ−3
n
[an+1; an+2, . . .] + [0; an, an−1, . . . , a1] , (42)

where pn
qn is the n-th convergent of α. Then pn
qn is a best lower approximation of the ℓ-th
kind to α if and only if n is even and Cn(ℓ) < Ck(ℓ) for all k = 0, 2, 4, 6, . . . , n − 2.

Proof. The proof is similar to the proof of Proposition 5.3(i). We use Theorem 5.1
together with Observation 2.5 to infer that every BLDA(ℓ) to α is an even–order
convergent of α. Then we apply Proposition 2.6(i) with SL = { pn
qn : n is even}
, whence
we obtain that pn
qn for an even n is a BLDA(ℓ) if and only if

qℓ−1
n
 (
α − pn
qn
 ) < qℓ−1
k
 (
α − pk
qk
 ) for all even k < n. (43)

Finally, we use (11) to rewrite condition (43) in the form

qℓ−3
n
[an+1; an+2, . . .] + [0; an, an−1, . . . , a1] < qℓ−3
k
[ak+1; ak+2, . . .] + [0; ak, ak−1, . . . , a1]

for all even k < n.

Let us comment on Proposition 7.2. Recall that qn depends solely on terms aj for
j ≤ n; cf. (8). So does the numerator of Cn(ℓ) in expression (42), while the denominator
has an+1 as its dominant term. Therefore, pn
qn is a best lower approximation to α if and

only if an+1 is large enough compared to the quantity qn ∈ [∏n
j=1 aj, ∏n
j=1(aj + 1)).
Hence we conclude that the number of BLDA(ℓ) to a given α can in general attain any
value from 1 to inﬁnity depending on the arrangement of large terms at odd positions
in the continued fraction expansion of α. Similar results can be derived for best upper
approximations of the ℓ-th kind.
In particular, since the numerators of Cn(ℓ) in (42) grow to inﬁnity (if ℓ ≥ 4),
Proposition 7.2 and the considerations above have a straightforward consequence:

One–sided Diophantine approximations 18

Observation 7.3. If ℓ ≥ 4 and the terms an with odd indices n in α = [a0; a1, a2, a3, . . .]
are bounded, then α has only ﬁnitely many best lower approximations of the ℓ-th kind.
Similarly, if the terms an with even indices n are bounded, there are only ﬁnitely many
BUDA(ℓ).

We can even say more:

Proposition 7.4. (i) Let ℓ be a positive integer such that ℓ ≥ 4 and let {an}
∞
n=1 be a
sequence of positive integers such that

lim sup
n→∞ log a2n+1
2n + 1 < (ℓ − 3) log ϕ , (44)

where ϕ = 1+
√5
2 is the golden ratio. Then the number α = [a0; a1, a2, a3, . . .] has only
ﬁnitely many best lower approximations of the ℓ-th kind.
(ii) Similarly, if we have

lim sup
n→∞ log a2n
2n < (ℓ − 3) log ϕ , (45)

then α = [a0; a1, a2, a3, . . .] has only ﬁnitely many best upper approximations of the ℓ-th
kind.

Proof. We will prove the part (i); the proof of (ii) is similar. In view of Proposition 7.2,
let us examine the quantity Cn(ℓ) for even numbers n. First of all, we have trivially

Cn(ℓ) ≥ qℓ−3
n
an+1 + 1
an+2 + 1
an ≥ qℓ−3
n
an+1 + 2 . (46)

Now we will estimate the numerator and denominator of (46). From (44) we obtain that
there exists an x and a k0 such that 1 < x < ϕ and log ak < (ℓ − 3)k log x for all odd
k > k0. Taking in particular the odd integer k = n + 1 (recall that n is even), we have

an+1 < x
(ℓ−3)(n+1) for all even n ≥ k0. (47)

Using the recurrent relation (8), we get qn ≥ Fn for all n, where Fn = 1√5(ϕ
n − ϕ
−n) is
the n-th Fibonacci number; note that the equality qn = Fn holds iﬀ 1 = a1 = . . . = an.
When we plug the estimate qn ≥ Fn and (47) into (46), we get

Cn(ℓ) ≥ 1
(
√5)ℓ−3 · (ϕ
n − ϕ−n)ℓ−3

x(ℓ−3)(n+1) + 2 for all even n ≥ k0. (48)

Now inequality 1 < x < ϕ yields

lim
n→∞ (ϕn − ϕ
−n)
ℓ−3

x(ℓ−3)(n+1) + 2 = ∞.

As a particular consequence of this and (48), there exists n0 such that for all even
n > n0, we have Cn(ℓ) ≮ C0(ℓ). Then Proposition 7.2 implies that a convergent pn
qn is
a best lower approximations of the ℓ-th kind to α only if n ≤ n0. Consequently, the
number of BLDA(ℓ) to α is ﬁnite.

One–sided Diophantine approximations 19

Both sets of BLDA(ℓ) and BUDA(ℓ) are ﬁnite also in the case when α is an irrational
algebraic number, i.e., an irrational root of a polynomial with integer coeﬃcients:

Proposition 7.5. For all ℓ ≥ 4, every irrational algebraic number α has a ﬁnite number
of best upper and best lower approximations of the ℓ-th kind.

Proof. Let us prove that the number of BLDA(ℓ) is ﬁnite. The case of BUDA(ℓ) is
similar. Let α be an irrational algebraic number. Roth’s theorem states that for each
ε > 0 there are ﬁnitely many coprime integers p, q such that
∣
∣
∣
∣α − p
q
 ∣
∣
∣
∣ < 1
q2+ε .

Setting in particular ε = ℓ − 3, we obtain that for any ℓ > 3 there exist only ﬁnitely
many integers p, q such that

qℓ−1 ∣
∣
∣
∣α − p
q
 ∣
∣
∣
∣ < 1. (49)

At the same time, the choice p′ = ⌊α⌋, q′ = 1 gives

(q′)
ℓ−1 (
α − p′

q′
 ) = 1
ℓ−1 (
α − ⌊α⌋
1
 ) = α − ⌊α⌋ < 1 . (50)

From (49) and (50), we obtain that there are only ﬁnitely many rational numbers p
q < α
such that
 0 ≤ qℓ−1 (
α − p
q
 ) < 1
ℓ−1 (α − ⌊α⌋
1
 ) .

In other words, only ﬁnitely many rational numbers p
q can satisfy the deﬁnition of a best
lower approximation to α (Deﬁnition 2.2).

Let us conclude this section with describing metric properties of the sets of numbers
having inﬁnitely many best one–sided approximations of the ℓ-th kind.

Proposition 7.6. For every ℓ ≥ 4 the set of numbers α which have inﬁnitely many best
upper or lower approximations of the ℓ-th kind has zero Lebesgue measure.

Proof. To obtain the statement, we use the fact that for every positive real ε the set

S = {
α ; ∣
∣
∣
∣α − p
q
 ∣
∣
∣
∣ < 1
q2+ε has inﬁnitely many solutions (p, q) ∈ (Z, Z)} (51)

has zero Lebesgue measure [3, p. 103]. Then we put ε = ℓ − 3 and follow the steps in
the proof of Proposition 7.5.

Proposition 7.7. For every ℓ ≥ 4 the set of numbers α which have inﬁnitely many best
upper or lower approximations of the ℓ-th kind has Hausdorﬀ dimension at most 2
ℓ−1.

Proof. We again proceed similarly as in the proof of Proposition 7.5, starting from the
fact that for every positive real ε the set S, given by (51), has Hausdorﬀ dimension 2
2+ε ,
which can be found in [3, p. 104].

One–sided Diophantine approximations 20

8. Application in mathematical physics

We have seen in Remark 4.7 that best one–sided approximations of the 2nd kind have a
simple geometric interpretation. In this section we will present an advanced application
of best one–sided Diophantine approximations of the 3rd kind by demonstrating their
use in quantum mechanics on graphs.
The motivation for the problem arises in spectral analysis. When studying a
quantum system consisting of a particle conﬁned to an inﬁnite periodic rectangular
network with δ-type potentials in the vertices (see Figure 2), one ﬁnds that the system

r r r r

r r r r

r r r r

r r r r

Figure 2. A periodic rectangular lattice graph with δ potentials (represented by solid
circles) in the vertices. A particle is conﬁned to the edges of the graph.

has gaps in its energy spectrum. In other words, there are intervals of energies that the
particle cannot attain. If we denote the lengths of the edges of the rectangle by a and
b and consider a repulsive δ potential of strength u > 0, it can be proved that every
gap is adjacent to some of the points (mπ/a)
2 and (mπ/b)2, where m ∈ N is a positive
integer [6]. The presence or absence of a gap at a given position (mπ/a)2 or (mπ/b)
2

depends on the parameter u. A calculation shows [7] that a gap adjacent to (mπ/a)
2 is
present if and only if the integer m ∈ N satisﬁes

2m
π tan ( π
2 (m ( b
a − ⌊m b
a
 ⌋)) < ua
π2 . (52)

Similarly, a gap adjacent to (mπ/b)
2 is present if and only if

2m
π tan (π
2 (m ( a
b − ⌊ma
b
 ⌋)) < ub
π2 . (53)

Conditions (52) and (53) have a slightly diﬀerent form in the case of attractive δ
potentials (see [8]), but we will not go into details here.
We will demonstrate in Theorem 8.2 below that a certain information about the set
of best lower Diophantine approximations of the third kind to b/a and to a/b allows to
formulate general statements regarding the gaps in the energy spectrum of the system.
For proving the theorem, we will need the following lemma.

Lemma 8.1. Let {yn}∞
n=1 be a strictly increasing sequence of positive numbers and
xn ∈ [
0, π
2 ) for all n ∈ N. If the sequence {ynxn}
∞
n=1 is strictly decreasing, then the
sequence {yn tan xn}
∞
n=1 is strictly decreasing.

One–sided Diophantine approximations 21

Proof. The assumptions on {ynxn}
∞
n=1 and {yn}∞
n=1 give

xn+1 < ynxn
yn+1 < xn for all n ∈ N; (54)

thus the sequence {xn}∞
n=1 is strictly decreasing as well.
Since tan 0 = 0 and tangent is a strictly convex function on the interval [0, π/2),
we have
 x′ < x ⇒ tan x′ < x′

x tan x for all x, x
′ ∈ [
0; π
2 ) . (55)

A particular choice x = xn and x′ = xn+1 in (55) together with (54) gives

tan xn+1 < xn+1
xn tan xn < yn
yn+1 tan xn .

Hence we obtain yn+1 tan xn+1 < yn tan xn for all n ∈ N.

Theorem 8.2. Let a, b > 0. If both a/b and b/a have inﬁnitely many best lower
approximations of the 3rd kind, then the number of gaps in the energy spectrum of
a periodic rectangular lattice quantum graph with repulsive δ potentials in the vertices
and edge lengths a and b is either inﬁnite or zero.

Proof. We have to analyze the number of integers m ∈ N that satisfy condition (52) or
condition (53). At ﬁrst we will examine (52).
Let θ = b/a and { kn
mn : n ∈ N0} be the set of all BLDA(3) to θ. By assumption,
this set has inﬁnitely many elements. Observation 2.3 gives kn = ⌊mnθ⌋. Without
loss of generality, we can assume that the denominators form an increasing sequence,
m0 < m1 < m2 < · · ·. Then the sequence {mn(mnθ − ⌊mnθ⌋)}∞
n=1 is strictly decreasing
by Deﬁnition 2.2. Moreover, the sequence has nonnegative terms; therefore

lim
n→∞ mn(mnθ − ⌊mnθ⌋) = L ∈ [0, ∞) . (56)

As a particular consequence of (56), we have

lim
n→∞(mnθ − ⌊mnθ⌋) = 0 . (57)

If we set in Lemma 8.1

xn = π
2 (mn (θ − ⌊mnθ⌋) and yn = 2mn
π ,

we obtain that the sequence
{ 2mn
π tan (π
2 (mnθ − ⌊mnθ⌋)
)}∞

n=1
is strictly decreasing. Using (56) and (57), we ﬁnd that

lim
n→∞ 2mn
π tan (π
2 (mnθ − ⌊mnθ⌋)
)

= lim
n→∞ mn(mnθ − ⌊mnθ⌋) · tan ( π
2 (mnθ − ⌊mnθ⌋)
)

π
2 (mnθ − ⌊mnθ⌋) = L · 1 = L . (58)

One–sided Diophantine approximations 22

Now we are ready to analyze the number of integers m ∈ N that satisfy (52). We have
two cases.
1. If ua
π2 > L, then (58) implies the existence of an n0 such that

2mn
π tan ( π
2 (mnθ − ⌊mnθ⌋)) < ua
π2 (59)

for all n > n0. Consequently, there are inﬁnitely many integers mn satisfying (52).
2. Assume that ua
π2 ≤ L. Then for every m ∈ N, we have

2m
π tan (π
2 (mθ − ⌊mθ⌋)) ≥ 2m
π · π
2 (mθ − ⌊mθ⌋) = m(mθ − ⌊mθ⌋) . (60)

If we take an arbitrary BLDA(3) of the form ⌊mnθ⌋ /mn with property mn ≥ m, then
Deﬁnition 2.2 gives

mn(mnθ − ⌊mnθ⌋) ≤ m(mθ − ⌊mθ⌋) . (61)

From (60), (61) and from the fact that sequence {mn(mnθ − ⌊mnθ⌋)}∞
n=1 strictly
decreases to L we get
2m
π tan (π
2 (mθ − ⌊mθ⌋)) > L for all m ∈ N.

In other words, there exists no m ∈ N obeying (52).
In the same way one would analyze condition (53). The assumption that a/b has
inﬁnitely many BLDA(3) leads to the conclusion that the number of solutions of (53) is
either inﬁnite or zero.
To sum up, the number of integers m that satisfy at least one of the conditions (52),
(53) is either inﬁnite or zero.

This result is closely related to the existence of so-called Bethe–Sommerfeld
quantum graphs. Let us ﬁnish this section with an important comment on this
interesting problem.
The Bethe–Sommerfeld conjecture of 1933 [20] states that any quantum system that
is periodic in two or more directions has ﬁnitely many gaps in its energy spectrum. The
conjecture was proved for several classes of systems (see e.g. [19]), but turned out to be
invalid for quantum graphs [1]. All examples of periodic quantum graphs studied in the
literature until 2017 led to energy spectra with either inﬁnitely many gaps, or no gaps
at all. The ﬁrst examples of quantum graphs that obey the conjecture in a nontrivial
manner, i.e., that have a ﬁnite nonzero number of gaps in their energy spectra, appeared
in [8] and [21]. In accord with [8] let us call a quantum graph having a ﬁnite nonzero
number of gaps in its energy spectrum to be of the Bethe–Sommerfeld type. In view of
Theorem 8.2, we conclude that if the ratios of edge lengths b/a and a/b have inﬁnitely
many best lower approximations, then the periodic rectangular lattice graph in question
cannot be of the Bethe–Sommerfeld type, regardless of the strength of the repulsive δ
potential in the vertices.
Now let us recall Proposition 5.4, which says that the set of numbers α having
inﬁnitely many BLDA(3) has full Lebesgue measure. Hence we obtain immediately that

One–sided Diophantine approximations 23

the set of numbers α such that both α and 1/α have inﬁnitely many BLDA(3) has full
Lebesgue measure as well. When we restrict our attention to the family of periodic
rectangular graphs with repulsive δ-type potentials in the vertices, we can say in view of
Theorem 8.2 that the Bethe–Sommerfeld graphs form a subset of zero Lebesgue measure.
For almost all ratios a/b of edge lengths, the quantum graph in question does not belong
to the Bethe–Sommerfeld class. This explains why it was so diﬃcult and longstanding
problem to prove the existence of Bethe–Sommerfeld graphs and, in particular, to ﬁnd
an explicit example.

9. Conclusions

Let us compare the theory of the best one–sided (lower or upper) Diophantine
approximations of the ℓ-th kind (ℓ ∈ N) with the theory of the classical best Diophantine
approximation of the ℓ-th kind. They have several diﬀerences and also some common
features. The common property is that the both theories make use of convergents and
semiconvergents as a main tool. Also metric properties are very similar. On the other
hand, the structure of the sets of best lower and upper Diophantine approximations
diﬀers from the sets known in the classical theory. A surprising result was found
for approximations of the ﬁrst and second kind, which form mutually diﬀerent sets
in the classical theory, but in the theory of one–sided approximations they coincide
(Theorem 4.5).
An important aspect concerns applications and history. Classical “double–sided”
best approximations have been developed and widely used in practical problems for
centuries. Best lower and upper approximations, by contrast, do not have many known
applications so far. In this paper, we demonstrated their immediate connection to
quantum mechanics on graphs (Section 8), which originally served as a main motivation
for our research. Our results help to understand the intricacy of Bethe–Sommerfeld
graphs, the existence of which posed an open problem in mathematical physics for
decades. We are certain that other applications of best one–sided approximations in
physics and mathematics will arise in the future.
The research opens many interesting new questions. For instance, what will be the
analog of the Lagrange or Markoﬀ sequences? Will it be possible to obtain a one–sided
version of Markoﬀ chains? And if one constructs an analog of functions which substitute
Lagrange numbers and which are described in [10] or [11], what form will they have?
All of this could give rise to a nice theory.

Acknowledgments

The authors thank Štěpán Starosta (Czech Technical University in Prague) for valuable
comments and discussions. The research was supported by the Czech Science Foundation
(GAČR) within the project 17-01706S.

One–sided Diophantine approximations 24

References

[1] G. Berkolaiko, P. Kuchment: Introduction to Quantum Graphs, Amer. Math. Soc., Providence,
R.I., 2013.
[2] S. Bettin: A congruence sum and rational approximations, Rend. Circ. Mat. Palermo (2) 66
(2017), 477–483.
[3] Y. Bugeaud: Approximation by algebraic numbers, Cambridge Tracts in Mathematics 160,
Cambridge University Press, 2004.
[4] T.W. Cusick, M. E. Flahive: The Markoﬀ and Lagrange spectra, Mathematical surveys and
Monographs 30, American Mathematical Society, Providence, RI, 1989.
[5] L.C. Eggan, I. Niven: A remark on one–sided approximation, Proc. Amer. Math. Soc. 12 (1961),
538–540.
[6] P. Exner: Lattice Kronig–Penney models, Phys. Rev. Lett. 74 (1995), 3503–3506.
[7] P. Exner: Contact interactions on graph superlattices, J. Phys. A: Math. Gen. 29 (1996), 87–102.
[8] P. Exner, O. Turek: Periodic quantum graphs from the Bethe–Sommerfeld perspective, J. Phys.
A: Math. Theor. 50 (2017), 455201.
[9] Y.Y. Finkelshtein: Klein polygons and reduced regular continued fractions, Russ. Math. Surv. 48
(1993), 198–200.
[10] J. Hančl: Sharpening of theorems of Vahlen and Hurwitz and approximation properties of the
golden ratio, Arch. Math. (Basel) 105, no. 2, (2015), 129–137.
[11] J. Hančl: Second basic theorem of Hurwitz, Lith. Math. J. 56 (2016), 72–76.
[12] J. Hančl, A. Jaššová and J. Šustek: Lebesgue measure and Hausdorﬀ dimension of special sets of
real numbers from (0, 1), Ramanujan J. 28 (2012), 15–23.
[13] A.Ya. Khinchin: Continued Fractions, University of Chicago Press, 1964.
[14] E. Pelantová, Š. Starosta, M. Znojil: Markov constant and quantum instabilities, J. Phys. A:
Math. Theor. 49 (2016), 155201.
[15] O. Perron: Die Lehre von den Kettenbrüchen, B. G. Teubner, Leipzig, 1913.
[16] R.M. Robinson: Unsymmetrical approximation of irrational numbers, Bull. Amer. Math. Soc. 53
(1947), 351–361.
[17] W.M. Schmidt: Diophantine Approximation, Lecture Notes in Mathematics, vol. 785, Springer
Verlag, Berlin 1980.
[18] B. Segre: Lattice points in inﬁnite domains, and asymmetric Diophantine approximations, Duke
Math. J. 12 (1945), 337–365.
[19] M.M. Skriganov: Proof of the Bethe-Sommerfeld conjecture in dimension two, Soviet Math. Dokl.
20 (1979), 956–959.
[20] A. Sommerfeld, H. Bethe: Electronentheorie der Metalle. 2nd edition, Handbuch der Physik,
Springer Verlag 1933.
[21] O. Turek: Gaps in the spectrum of a cuboidal periodic lattice graph, Rep. Math. Phys., to appear
(arXiv:1801.02572).
[22] E. Zurl: Theorie der reduziert-regelmäßigen Kettenbrüche, Math. Ann. 110 (1935), 679–717.
