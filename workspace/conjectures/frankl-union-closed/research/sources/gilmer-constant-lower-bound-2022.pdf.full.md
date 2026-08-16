<!-- source: https://arxiv.org/pdf/2211.09055v2 | converted from PDF -->

A constant lower bound for the union-closed sets
conjecture

Justin Gilmer∗

Google Research, Brain Team

November 29, 2022

Abstract

We show that for any union-closed family F ⊆ 2[n], F ̸= {∅}, there
exists an i ∈ [n] which is contained in a 0.01 fraction of the sets in F.
This is the ﬁrst known constant lower bound, and improves upon the
Ω(log2(|F|)−1) bounds of Knill and W´ojick. Our result follows from an
information theoretic strengthening of the conjecture. Speciﬁcally, we
show that if A, B are independent samples from a distribution over subsets
of [n] such that P r[i ∈ A] < 0.01 for all i and H(A) > 0, then H(A ∪ B) >
H(A).

1 Introduction

We study families of ﬁnite sets which are union-closed. A family F ⊆ 2
[n] is
said to be union-closed if for every A, B ∈ F the set A ∪ B ∈ F. Frankl in
1979 [8] conjectured that any such family F ̸= {∅} should contain an abundant
element—that is an i ∈ [n] which is contained in at least half of the sets in F.
Due to the simplicity of the problem statement, the union-closed conjecture has
received substantial interest over the past 40 years, with over 50 publications
proving special cases or providing reformulations of the problem [4]. The prob-
lem was also explored in Polymath11 [1], which considered several interesting
strengthenings to the conjecture, some of which were shown to be false. The
best prior bound which does not place additional assumptions on F is due to
Knill [10] (with improvement by W´ojick [12]), who proves that there is an ele-
ment contained in at least Ω( |F |
log2(|F |) ) sets. Some special cases are known which
make strong assumptions on the family F. For example Balla, Bollab´as, and
Eccles [3] show the conjecture holds when |F| ≥ 2
3 2
n. This was later improved
by Karpas [9] under the assumption that |F| ≥ 2n−1. We refer the interested

∗gilmer@google.com
 1arXiv:2211.09055v2  [math.CO]  28 Nov 2022
reader to the survey of Bruhn and Schaudt [4] for an in depth survey of prior
work on the problem.
In this work, we prove the following theorem.

Theorem 1. Let A and B denote independent samples from a distribution
over subsets of [n]. Assume that for all i ∈ [n], P r[i ∈ A] ≤ 0.01. Then
H(A ∪ B) ≥ 1.26H(A).

When H(A) > 0, Theorem 1 implies that H(A ∪ B) > H(A). Note that
if we sample A, B independently and uniformly at random from a union-closed
family F, then H(A ∪ B) ≤ H(A). This follows because A ∪ B is a distribution
over F and the entropy of a distribution over F is maximized when it is the
uniform distribution. We obtain as an immediate corollary

Theorem 2. Let F ⊆ 2
[n] be a union-closed family, F ̸= {∅}. Then there exists
i ∈ [n] that is contained in at least a 0.01 fraction of the sets in F.

We note that Theorem 1 operates in a more general setting than the union-
closed conjecture as we allow A to be sampled from an arbitrary probability
distribution over a family F. Consider the following illustrative examples.
Example 1: Let A = (A1, A2, · · · , An) be a random subset of [n] such that
each Ai are iid Bernoulli random variables with probability p. Then H(A) =
H(p)n and H(A ∪ B) = H(2p − p
2)n.
Example 2: Let A = [n] with probability p and A = ∅ with probability
1 − p. Then H(A) = H(p) and H(A ∪ B) = H(2p − p
2).
In examples 1 and 2 the ratio H(A∪B)
H(A) = H(2p−p2)
H(p) . For these cases, when

p < 3−√5
2 , it follows that H(A ∪ B) > H(A). When p = 3−
√5
2 then H(A ∪ B) =
H(A) and when p > 3−√5
2 we get H(A ∪ B) < H(A). We hypothesize that
these examples are extremal in the following sense: for any distribution A, if
P r[Ai ≤ p] for all i then H(A ∪ B) ≥ H(2p−p2)
H(p) H(A).
The following example was useful in motivating some of the proof techniques
we employ:
Example 3: Sample A ⊆ [n] in the following manner. First sample A1
from a Bernoulli distribution with probability p. Then, conditioned on the event
that A1 = 1, sample each Ai from iid Bernoulli distributions with probability
q = 0.99. Otherwise, if A1 = 0 then each Ai = 0. To calculate H(A), we
apply the chain rule to get H(A) = H(A1, A>1) = H(A1) + H(A>1|A1). The
conditional entropy can be computed as

H(A>1|A1) = P r[A1 = 0] · 0 + P r[A1 = 1]H(q)(n − 1).

Thus H(A) = H(p) + pH(q)(n − 1). Via a similar calculation we get H(A ∪
B) = H(2p − p2) + 2p(1 − p)H(q)(n − 1) + p2H(2q − q2)(n − 1).
In Example 3, for n large and p small, H(A ∪ B) is dominated by the term
2p(1 − p)H(q)(n − 1). This corresponds to the event that exactly one of A1, B1
is equal to 1. It follows that H(A∪B)
H(A) ≈ 2(1 − p). Note in this case, the entropy

2

H(A ∪ B|A1 = B1 = 1) is small relative to H(A|A1 = 1). We will discuss this
example further in Section 4.
Examples 1 and 2 imply that if P r[Ai = 1] ≥ 3−√5
2 then it is possible that
H(A ∪ B) ≤ H(A). Because 3−
√5
2 < 0.5, any stronger bound for Theorem 1
will not be suﬃcient to resolve the union-closed conjecture. In Section 5 we
discuss a promising direction for additionally leveraging the assumption that A
is chosen uniformly over the family F which might improve the bound to 0.5.

2 Notation and Preliminaries

Throughout the paper we use log(x) to denote the base 2 logarithm of x. If X, X ′

are Bernoulli random variables, we will use X ∪ X ′ to denote max(X, X ′).
We quickly review two properties of conditional entropy that we require to
complete the proofs. We refer the reader to Cover and Thomas [6] for additional
background on information theory.

1. Chain Rule for Entropy: For a sequence of random variables
X1, · · · , Xn, denote X<i = (X1, · · · , Xi−1). Then H(X1, · · · , Xn) =∑

i H(Xi|X<i).

2. For random variables X and Y and a function f (Y ),

H(X|Y ) ≤ H(X|f (Y )).

We quickly prove property (2).

Proof. The sequence X → Y → f (Y ) forms a Markov chain. Thus by the data
processing inequality:
 I(X : f (Y )) ≤ I(X : Y )

H(X) − H(X|f (Y )) ≤ H(X) − H(X|Y )

H(X|Y ) ≤ H(X|f (Y ))

3 Main Result

In this section we prove our main result. We use A<i = (A1, · · · , Ai−1) to
denote the sequence of indicator random variables, where Ai = 1 if and only if
i ∈ A. The proof strategy relies on revealing the bits of A ∪ B and A one at a
time and showing at each step that

H((A ∪ B)i|(A ∪ B)<i) ≥ 1.26H(Ai|A<i). (1)

By applying the chain rule this will imply that H(A ∪ B) ≥ 1.26H(A).
The proof of equation (1) will rely on this key technical lemma, the proof of
which is provided in Section 4.
 3

Lemma 1. Let C denote a random variable over a ﬁnite set S. For each c ∈ S,
let pc be a real number in [0, 1]. Let X be a Bernoulli random variable sampled
according to the following process: ﬁrst sample c ∼ C, then sample X with
P r[X = 1|C = c] = pc. Assume further that E[X] ≤ 0.01. Let C ′ be an iid
copy of C, and sample X ′ conditioned on C ′ according to the same process (so
P r[X ′ = 1|C ′ = c] = pc, and X ′ is independent of X and C). Then

H(X ∪ X ′|C, C ′) ≥ 1.26H(X|C).

We note that Lemma 1 can be restated a bit more succinctly that assuming
{pc}c∈S ⊂ [0, 1] is a ﬁnite sequence of real numbers satisfying Ec[pc] ≤ 0.01,
then:
 Ec,c′ [H(pc + pc′ − pcpc′)] ≥ 1.26Ec [H(pc)] .

Here, X, X ′ correspond to the random bits Ai, Bi respectively, and C, C ′

correspond to the histories A<i, B<i. The constant 0.01 was not optimized
as new ideas will be needed to achieve a tight result. We hypothesize that if
E[X] < 3−√5
2 , then H(X ∪ X ′|C, C ′) ≥ (1 + ϵ)H(X|C) for an ϵ > 0 which
depends on the value of E[X]. We discuss challenges in obtaining a stronger
bound for Lemma 1 along with counter examples to natural strengthenings in
Section 4.
Assuming Lemma 1, we now prove our main result:

Theorem 1. Let A, B be independent samples from a distribution over subsets
of [n] such that P r[i ∈ A] ≤ 0.01 for all i. Then H(A ∪ B) ≥ 1.26H(A).

Proof. We ﬁrst show for all i,

H((A ∪ B)i|(A ∪ B)<i) ≥ 1.26H(Ai|A<i).

By applying property (2) of conditional entropy we get

H((A ∪ B)i|(A ∪ B)<i) ≥ H((A ∪ B)i|A<i, B<i). (2)

We pause here to remark that (2) is the crucial step which takes advantage
of the power of the information theoretic formulation. Because (A ∪ B)<i is
simply a function of A<i, B<i, the entropy in (A ∪ B)i can not increase if we
additionally assume we know the full history of A<i, B<i. Conditioning on
A<i, B<i dramatically simpliﬁes the analysis, as these are iid. Additionally, Ai
and Bi are Bernoulli random variables whose distribution are determined by
the sampled values of A<i and B<i respectively. Thus by Lemma 1 we conclude
that H((A ∪ B)i|A<i, B<i) ≥ 1.26H(Ai|A<i). (3)

To end the proof we repeatedly apply the chain rule to conclude that

H(A ∪ B) ≥ 1.26H(A). (4)

4

4 Proof of Lemma 1

For this section, we can forget all of the structure contained in the random
variables A<i and B<i. Lemma 1 only assumes that they are iid over some
ﬁnite set S. Recall that Lemma 1 can be stated as

Ec,c′ [H(pc + pc′ − pcpc′)] ≥ 1.26Ec [H(pc)] (5)

under the assumption that Ec[pc] ≤ 0.01 = µ.
A natural approach to Lemma 1 is to try to apply Jensen’s inequal-
ity to the function f (pc, pc′) = H(pc + pc′ − pcpc′) − H(pc). However,
this f is not convex in pc′. Additionally, it does not hold in general that
Ec,c′ [H(pc + pc′ − pcpc′) − H(pc)] ≥ H(2µ − µ
2) − H(µ). For example, con-
ditioned on C there may be no entropy left in X, in which case the left hand
side is 0! This is exactly what will happen in Example 2 discussed in the
introduction—after revealing the ﬁrst bit A1, all subsequent bits become deter-
ministic. This example demonstrates that some natural symmetrizations such
as g(pc, pc′) = H(pc + pc′ − pcpc′) − H(pc)+H(pc′ )
2 are not convex.
Another natural approach is to look for a purely information theoretic proof
of Lemma 1. Indeed, one hypothesis is that there is nothing special about
the union function here, but for any function f , H(f (X, X ′)|C, C ′) ≥ H(X|C)
whenever H(f (X, X ′)) ≥ H(X). However, this strengthening turns out to
be false. Consider the case where both X and C are uniform over the set
{0, 1, 2, 3}. Furthermore, let X|C be uniform over {0, 2} when C ∈ {0, 2}, and
X|C be uniform over {1, 3} when C ∈ {1, 3}. Finally, deﬁne f (x, x
′) = (x
mod 2, x
′ mod 2). Then H(f (X, X ′)) = H(X) = log(4), H(X|C) = 1, but
H(f (X, X ′)|C, C ′) = 0. Thus any proof of Lemma 1 will need to make careful
use of properties of the union function.
Having been unable to make the above two proof strategies work, we resort
to a more direct estimation of the terms in inequality (5). Our argument is
quite wasteful and surely is far from tight. First we provide a proof sketch. We
let C0 = {c|pc ≤ 0.1} and let C1 = Cc
0.
Using the assumption that E[X] ≤ 0.01 we apply Markov’s inequality to get
that
 P r[c ∈ C1] = P r[pc > 0.1] ≤ Ec[pc]
0.1 ≤ 0.1 (6)

This implies that P r[C0] ≥ 0.9. In what follows we will sometimes write C0
as shorthand for the event that C ∈ C0. Similarly C′
0 refers to the event that
C ′ ∈ C0. For example, the conditional entropy H(X|C) can be written as

H(X|C) = P r[C0]H(X|C0) + P r[C1]H(X|C1).

We ﬁrst note that conditioned on the event that both C, C ′ ∈ C0, the entropy
H(X ∪ X ′) will be a constant factor larger than H(X)+H(X ′)
2 . This can be
leveraged to prove that

P r[C0]
2H(X ∪ X ′|C0, C′
0) ≥ 1.26P r[C0]H(X|C0). (7)

5

Then, in the event that exactly one of c, c
′ ∈ C0 we can show that H(X ∪
X ′) ≥ 0.9H(X). Using this property, we will show that

2P r[C0]P r[C1]H(X ∪ X ′|C0, C′
1) ≥ 1.62P r[C1]H(X|C1). (8)

Example 3 discussed in the introduction helped to motivate the decompo-
sition considered in equations (7) and (8). In this example, most of the en-
tropy in H(X|C) comes from the event that A1 = 1 (this corresponds to the
event C1). This entropy is dominated by the corresponding event that exactly
one of A1 and B1 are equal to 1, which is exactly the conclusion of equa-
tion (8). This example also demonstrates that entropy coming from the term
P r[C1]
2H(X, X ′|C, C ′ ∈ C1) may be small relative to P r[C1]H(X|C1). In this
work we throw this term away, it is non-negative and the sum of the left hand
side of (7) and (8) are already larger than H(X|C). However, a tight version of
Lemma 1 will require a more careful analysis.
We now make the above proof sketch rigorous with the following sequence
of lemmas.

Lemma 2. Assume p, p
′ ≤ 0.1. Then H(p + p
′ − pp′) ≥ 1.4 ( H(p)+H(p′)
2 ).

Proof. Note the lemma holds when p = p
′ = 0. We let D = [0, 0.1] × [0, 0.1] −
{(0, 0)}. Figure 1 plots the function f (p, p
′) = 2H(p+p′−pp′)
H(p)+H(p′) for (p, p
′) ∈ D
where the lemma can be checked visually. More formally, by concavity of H,
H(p)+H(p′)
2 ≤ H ( p+p′

2 ). Additionally, when 0 ≤ p, p
′ ≤ 0.1, we have p + p
′ −

pp′ ≥ 0.9(p+p′). Thus in the given domain, f (p, p
′) ≥ H(0.9(p+p′))
H(0.5(p+p′)) . The function

g(p) = H(0.9p)
H(0.5p) for p ∈ (0, 0.2] is minimized at p = 0.2. This implies that over
the domain, f (p, p
′) > g(0.2) = 1.45.

Lemma 3. For any p, p
′ ∈ [0, 1], H(p + p
′ − pp′) ≥ (1 − p)H(p
′).

Proof. By concavity of H,

H(p · 1 + (1 − p)p
′) ≥ pH(1) + (1 − p)H(p′) = (1 − p)H(p
′).

For the next lemmas, we use q to denote the distribution of C, that is
q(c) = P r[C = c]. Additionally q0 denotes the distribution of C conditioned on
the event that C ∈ C0. So for c ∈ C0, q0(c) = q(c)
P r[C∈C0] .

Lemma 4. Under the assumption that E[X] ≤ 0.01,

P r[C0]
2H(X ∪ X ′|C0, C′
0) ≥ 1.26P r[C0]H(X|C ∈ C0)

6
 (0(.(0(0(0 (0(.(0(2(5 (0(.(0(5(0 (0(.(0(7(5 (0(.(1(0(0
(0(.(0(0(0

(0(.(0(2(5

(0(.(0(5(0

(0(.(0(7(5

(0(.(1(0(0
f((p(,p0()(=(2H((p (+p0 [pp0()(/((H((p()(+H((p0()()
 (1(.(5

(1(.(6

(1(.(7

(1(.(8

(1(.(9

Figure 1: Plotting the function f (p, p
′) = 2H(p+p′−pp′)
H(p)+H(p′) over 0 ≤ p, p
′ ≤ 0.1. The
minimum value of 1.496 is achieved at p = p′ = 0.1.

Proof.
 P r[C0]H(X|C ∈ C0) = P r[C0]Ec∼q0 H(pc)

= P r[C0]
2 Ec∼q0 [H(pc) + Ec′∼q0H(pc′)]

= P r[C0]Ec,c′∼q0
 [ H(pc) + H(pc′)
2
 ]

(By Lemma 2) ≤ P r[C0]
1.4 [Ec,c′∼q0 H(pc + pc′ − pcpc′)]

(P r[C0] ≥ 0.9) ≤ P r[C0]2

1.26 H(X ∪ X ′|C, C ′ ∈ C0)

Multiplying both sides by 1.26 yields the desired result.

Lemma 5. Under the assumption that E[X] ≤ 0.01,

2P r[C0, C′
1]H(X ∪ X ′|C0, C′
1) ≥ 1.62P r[C1]H(X|C ∈ C1)

7

Proof.

2P r[C0, C′
1]H(X ∪ X ′|C0, C′
1) = 2 ∑

c∈C0,c′∈C1 q(c)q(c′)H(pc + pc′ − pcpc′)

(by Lemma 3) ≥ 2 ∑

c∈C0,c′∈C1 q(c)q(c′)(1 − pc)H(pc′)

= 2 ∑

c∈C0 q(c)(1 − pc)
 [ ∑

c′∈C1 q(c′)H(pc′)

]

= 2P r[C′
1]H(X ′|C′
1) ∑

c∈C0 q(c)(1 − pc)

(using pc ≤ 0.1) ≥ 2P r[C′
1]H(X|C′
1) ∑

c∈C0 q(c)0.9

= 1.8P r[C0]P r[C′
1]H(X ′|C′
1)

(using P r[C0] ≥ 0.9) ≥ 1.62P r[C′
1]H(X ′|C′
1)

We can now quickly ﬁnish the proof of Lemma 1.

Proof. To show that H(X ∪X ′|C, C ′) ≥ 1.26H(X|C), we write H(X ∪X ′|C, C ′)
as a sum of three disjoint events:

1. P r[C, C ′ ∈ C0]H(X ∪ X ′|C, C ′ ∈ C0)

2. 2P r[C ∈ C0]P r[C ′ ∈ C1]H(X ∪ X ′|C ∈ C0, C ′ ∈ C1)

3. P r[C, C ′ ∈ C1]H(X ∪ X ′|C, C ′ ∈ C1)

By Lemma 4, event (1) has higher entropy than 1.26P r[C ∈ C0]H(X|C ∈
C0). By Lemma 5, event (2) has higher entropy than 1.62P r[C ∈ C1]H(X|C ∈
C1). Finally, event (3) has non-negative entropy. Thus H(X ∪ X ′|C, C ′) ≥
1.26H(X|C).

5 A possible path towards resolving the conjec-
ture

It is clear that there is more ground to be covered with the information theoretic
approach we have initiated in this work. A tight version of Lemma 1 would
imply a 3−
√5
2 lower bound on the maximum element frequency for union-closed
families. Because 3−√5
2 < 1
2 , additional ideas will be needed to resolve union-
closed conjecture. In this section we discuss a potential direction towards this
strengthening.
 8

In cases where p is close to 1
2 , the distribution of A ∪ B seems to be far from
uniform. Thus it may still hold that |F ∪ F| > |F|1 even though H(A ∪ B) ≤
H(A). To quantify how far from uniform the distribution A ∪ B is, it is useful to
consider the KL-divergence D(A ∪ B||A). When A is the uniform distribution
over a union-closed family F, it holds that
2

D(A ∪ B||A) + H(A ∪ B) = H(A) = log(|F|). (9)

We can study the quantity D(A ∪ B||A) + H(A ∪ B) for more general distri-
butions A—say if A is not the uniform distribution, or F is not union-closed.
For example, if A denotes a single bit with probability p of being 1, then when
p = 0.5 it holds exactly that D(A ∪ B||A) + H(A ∪ B) = H(A) = 1.0. However,
if p < 0.5 it holds that

D(A ∪ B||A) + H(A ∪ B) > H(A). (10)

If equation (10) ever holds for a distribution A, we can conclude that either A
is not the uniform distribution over F or the distribution A ∪ B has support
outside of F.
Thus the union-closed sets conjecture would follow from showing the follow-
ing:

Conjecture 1. Let A, B be iid samples from a distribution over a family of
subsets of [n]. Assume that P r[i ∈ A] < 0.5 for all i, and H(A) > 0. Then
H(A ∪ B) + D(A ∪ B||A) > H(A).

6 Conclusion

We have established the ﬁrst constant lower bound for the union-closed con-
jecture by studying the entropy of the union of two iid samples from a fam-
ily F. The methods presented are strong enough to derive the stronger con-
clusion that H(A ∪ B) ≥ CpH(a) for a constant Cp > 0 which depends on
p = max
i P r[Ai = 1]. However, we certainly have not derived the strongest pos-

sible bound Cp. We are hopeful that the approach initiated in this work will
lead to a proof of the conjecture. Beyond proving the union-closed conjecture,
the following questions could be interesting to consider

1. Does it hold for any distribution A with P r[Ai = 1] ≤ p for all i that
H(A ∪ B) ≥ H(2p−p2)
H(p) H(A)?

2. Does Conjecture 1 hold?

3. Under what other assumptions on the distributions A, B does it hold that
H(A ∪ B) > H(A)? Suppose for example that for ﬁxed k it holds that for
every X ∈ ([n]
k ), P r[X ⊆ A] < p. How small does p need to be to conclude
that H(A ∪ B) > H(A)?

1We use F ∪ F to denote {A ∪ B|A, B ∈ F}.
2See [6] Theorem 2.6.4.
 9

Update (11/27/2022) Shortly after publication of this preprint, three
publications appeared which all prove tight versions of our Lemma 1 [5, 11, 2].
These results improve the resulting bound on Frankl’s conjecture to 3−√5
2 ≈ .38.
Sawin [11] conﬁrm Question 1 when p ≤ 3−
√5
2 . However, when p > 3−√5
2 it
only holds that H(A ∪ B) ≥ (1 − p) 2√
5−1 . Sawin [11] and Ellis [7] provide
constructions refuting Conjecture 1. It is noteworthy that Sawin’s construction
demonstrates that, without placing additional assumptions on the distribution
A, incorporating the KL term cannot improve the resulting bound on Frankl’s
conjecture.

Acknowledgement

The author is grateful to Michael Saks and Swastik Kopparty for enlightening
discussions and for reviewing initial versions of this work. Additionally, the
author thanks Phil Long for his careful reading and feedback on the manuscript.

References

[1] Polymath11. https://gowers.wordpress.com/2016/01/21/
frankls-union-closed-conjecture-a-possible-polymath-project/.

[2] Ryan Alweiss, Brice Huang, and Mark Sellke. Improved lower bound for
the union-closed sets conjecture. arXiv preprint arXiv:2211.11731, 2022.

[3] Igor Balla, B´ela Bollob´as, and Tom Eccles. Union-closed families of sets.
Journal of Combinatorial Theory, Series A, 120(3):531–544, 2013.

[4] Henning Bruhn and Oliver Schaudt. The journey of the union-closed sets
conjecture. Graphs and Combinatorics, 31(6):2043–2074, 2015.

[5] Zachary Chase and Shachar Lovett. Approximate union closed conjecture.
arXiv preprint arXiv:2211.11689, 2022.

[6] Thomas M Cover and A Thomas Joy. Elements of information theory.
John Wiley & Sons, 1999.

[7] David Ellis. Note: a counterexample to a conjecture of gilmer which would
imply the union-closed conjecture. arXiv preprint arXiv:2211.12401, 2022.

[8] P Frankl. Extremal set systems. Handbook of combinatorics, 2:1293–1329,
1995.

[9] Ilan Karpas. Two results on union-closed families. arXiv preprint
arXiv:1708.01434, 2017.

[10] Emanuel Knill. Graph generated union-closed families of sets. arXiv
preprint math/9409215, 1994.
 10

[11] Will Sawin. An improved lower bound for the union-closed set conjecture.
arXiv preprint arXiv:2211.11504, 2022.

[12] Piotr W´ojcik. Union-closed families of sets. Discrete Mathematics, 199(1-
3):173–182, 1999.
 11
