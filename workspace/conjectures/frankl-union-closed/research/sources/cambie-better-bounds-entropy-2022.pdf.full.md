<!-- source: https://arxiv.org/pdf/2212.12500v2 | converted from PDF -->

arXiv:2212.12500v2  [math.CO]  16 Feb 2025
Better bounds for the union-closed sets conjecture using the
entropy approach

Stijn Cambie
∗

February 18, 2025

Abstract

We improve the best known constant 3−√5
2 for which the union-closed conjecture is known
to be true, by using dependent samples as suggested by Sawin and the entropy approach on this
problem initiated by Gilmer. Meanwhile, we focus on the intuition behind this entropy approach
and its boundaries.

1. Introduction

The union-closed conjecture is a challenging conjecture in extremal set theory, see e.g. [11, sec. 32],
which became famous due to its elegance. A union-closed family F is a collection of sets such that
the union of any two sets belongs to F as well. The union-closed conjecture states that if F contains
at least one nonempty set, then there is an element that belongs to at least half of the sets in F . This
can be formally stated as follows, where we recommend the reader who is not familiar with some of
the terminology, notations or deﬁnitions to ﬁrst have a look at Subsection 1.1.

Conjecture 1 (Union-closed conjecture). If F ̸= {∅} is a union-closed family with ground set [n],
then there exists an element i ∈ [n] such that at least half of the sets in F contain i, i.e., |F(i)| ≥ |F |
2 .

This would be tight by taking all subsets of a ﬁxed ground set. Indeed, if F = 2[m], then every
integer i ∈ [m] appears in exactly 2m−1 sets of F . Possibly, these are essentially the only tight examples
(duplicating elements does not change the structure), as also suggested in the blog on the Polymath
project; https://gowers.wordpress.com/2016/01/21/.
According to [2, 3, 11], the union-closed conjecture was already a folklore conjecture since the late
1960s or beginning 1970s, and was made well-known by Frankl, who rediscovered it in the late 1970s
(1979 according to [10]), and Ron Graham. Nonetheless, the ﬁrst formal publication containing it
might be [19]. In the 90s, it was proven in [16, 21] that there is an element that appears in at least
a Ω ( log|F |
|F | ) fraction of all sets. The latter result is also implied by the union-closed size problem by

Reimer [18], which was fully resolved in [3]. In contrast to the union-closed size problem, which was
solved in 10 years, the union-closed conjecture is still open. It has been proven in various speciﬁc
cases, e.g. for certain random generated union-closed families it has been proven to be true with high
probability [2]. More on the history till 2015, with other equivalent formulations of the conjecture, can
be found in the survey [5]. One equivalent formulation by [4] states that every bipartite graph with
at least one edge has at least one vertex in each bipartition class that belongs to at most half of the
maximal independent sets. At the beginning of 2017, Karpas [15] proved the union-closed conjecture
for families that contain roughly at least half of all sets.

∗Extremal Combinatorics and Probability Group (ECOPRO), Institute for Basic Science (IBS), Daejeon, South
Korea, supported by the Institute for Basic Science (IBS-R029-C4), E-mail: stijn.cambie@hotmail.com

1

Very recently, Gilmer [12] proved the ﬁrst linear bound using an elegant entropy-based method.
As such he resolved the ε-Union-Closed Sets Conjecture, as stated in [13]. Gilmer claimed that a tight
version of his method could prove a fraction equal to 3−√
5
2 , which was soon veriﬁed by [1, 7, 20]. The

tight version heavily depends on determining the minimum of a function h(x2)
xh(x) , where h is the binary
entropy function. Chase and Lovett [7] gave a clear, short proof using the minimum determined by [1].
A question and conjecture of Gilmer were soon answered in the negative, by [20, 9]. By working
with approximate union-closed families in [7], 3−√
5
2 seemed possibly the best constant one could aim
for with the idea of Gilmer [12]. Nevertheless, as suggested by Sawin [20], this is not the case. For
this, we address the following question, from which the improved constant can be concluded later.
Note the inequality cannot be strict, since for any {0, 1}-valued random variable equality does hold.

Question 2 (Sawin). What is the maximum value c for which there exists an α ∈ [0, 1] such that the
following is true? For every p, q, r identically distributed [0, 1]-valued random variables with expectation
less than c, where p and q are independent, but p and r are not necessarily independent, we have

(1 − α) E[H(p + q − pq)] + α E [H (max (p, r, min (p + r, 1/2)))] ≥ E[H(p)]. (1)

Yu [22] considered the approach and question of Sawin in larger generality and derived bounds
expressed in general optimisation forms.
Our contribution consists in solving Question 2 exactly and as such improving the constant for
which the union-closed conjecture is true. The core content is written in Section 2. Here, we start
with explaining the entropy approach in general. After that, we give some intuition why the bound
can be improved despite the sharpness of the approximate union-closed conjecture by [7] and why
the direct use of Sawin’s idea cannot improve the constant too much. For this, we provide the upper
bound for c in Question 2, which later will turn out to be sharp. As a last part of this section, in
Subsection 2.4, we summarise the additional steps of the proof for the improved constant.
In the next section, Section 3, we prove the best bound of c in Question 2. In Subsections 3.1
and 3.2, we reduce the possible probability distributions one has to consider and prove that the critical
probability distributions have a support containing at most 3 values. This is as such the technical
core to work out Sawin’s idea and to answer Question 2. After this, we can express the problem
as a minimisation problem of a function in 4 variables and the optimisation problem can be veriﬁed
with a computer-veriﬁcation. In contrast to the detailed work in e.g. [1] for the constant 3−√
5
2 , this
is done slightly less rigorous. We need to take into account that the minimisation problem ﬁnds
a local minimum and there is a ﬁnite computer precision involved. By considering some plots, we
note that there are two regimes to verify. By observing that the extremal probability distribution
is atomic (support has 2 elements) in one regime, we prove it more precisely for that regime and
conclude. In subsection 3.4, we give a precise conﬁrmation by combining our ideas with the strategy
of Yu [22]. As such, we can reduce the veriﬁcation of Question 2 to a minimisation problem in two
variables, which can be solved numerically with graphical conﬁrmation. The graphical conﬁrmation
gives information on the behaviour on local and global minima, which in principle is not the case in
our previous strategy (3 variables), Yu [22] (4 variables) and Liu [17] (9 variables for a slightly further
improved constant). Since the constant is not 1
2 and another core method will be needed for the full
resolution, an even more rigorous analysis than has been done is unnecessary, as it does not contribute
to further understanding the underlying principles. Finally, in Section 4 we summarise the proof for
the improved constant on the union-closed conjecture, based on the answer for Question 2. That is,
for c ∼ 0.3823455 we prove the following theorem.

Theorem 3. Let F ⊂ 2[n] be a nonempty union-closed family. Then there is some element i ∈ [n]
that appears in at least c|F | many sets of F .

So to recap, in this paper, we prove that by taking a linear combination of probability distributions,
not all of them being independent, the bound on the union-closed conjecture derived with the entropy
approach of Gilmer [12] can be improved slightly.
 2

1.1. Terminology and notation

In this subsection, we collect some basic notation and deﬁnitions used in extremal set theory and the
entropy method used in the papers related to the work of Gilmer. For more of this, we refer to [11]
for extremal set theory and [8] for entropy.
The standard ﬁnite set of cardinality n is denoted with [n] = {1, 2, . . . , n}. A subset of [n] is a
set containing some elements from [n] and can possibly be the empty set ∅. A collection of subsets of
[n] is called a set system or family F . The family 2[n] (the power set of [n]) contains all 2n possible
subsets of [n] and in general a family F ⊂ 2[n] is a subset of this power set. A uniform family is a
family whose sets all have the same cardinality k. The largest k-uniform family on the ground set [n]
is ([n]
k ) = {A ⊂ [n] : |A| = k}. Similarly we use ([n]
≥k) to denote {A ⊂ [n] : |A| ≥ k}.
A family F is called union-closed if for every A, B ∈ F also the union A ∪ B ∈ F. Using F ∪ F =
{A∪B : A, B ∈ F }, a family F is union-closed if and only if F ∪F = F . It is approximate union-closed
if the latter is true for almost every choice of A, B ∈ F. The sets containing a ﬁxed element i are
essentially presented by the family F (i) = {A\{i} : i ∈ A ∈ F }. Similarly, F (i) = {A : i ̸∈ A ∈ F }.
We will use some Landau-notation. Given two functions f, g : R → R, we write

• f = o(g) if limx→∞ f (x)/g(x) = 0,

• f ∼ g if limx→∞ f (x)/g(x) = 1.,

• f = O(g) if there is a constant C such that limx→∞|f (x)/g(x)| < C,

• f = Ω(g) if g = O(f ),

• f = Θ(g) if g = O(f ) and f = O(g).

A random variable X can be related with the probability distribution of the outcomes. The entropy
H(X) of a discrete random variable X equals the Shannon entropy of its probability sequence and is
denoted by H(X). The support of a probability distribution or random variable, is the subset of the
possible outcomes which have positive probability (density function). If the support of X is a ﬁnite
set A, and each outcome x ∈ A has a probability px, then

H(X) = − ∑

x∈A px log2 px.

It is a fundamental result, a corollary of Jensen’s inequality, that this is bounded by log2|A|. For a
random variable with only two outcomes, occurring with probabilities p and 1 − p, we denote the
entropy with the binary entropy function h(p) = −(p log2 p + (1 − p) log2(1 − p)).
1 A conditional
entropy of a random variable Y given X can be computed as

H(Y |X) = − ∑

x∈X,y∈Y P(x, y) log2 P(x, y)
P(x) .

Here P(x, y) is the probability on the outcome {X = x, Y = y}. The expectation of a random variable
X is E[X] = ∑
x∈A pxx. We use ∨ for the logical or, that is x∨y implies that x or y has to be satisﬁed.

2. Preliminaries

In this section, we begin by presenting the main idea behind the entropy approach introduced by
Gilmer [12]. We then provide some intuition to explain why the examples from [12, 7], which initially
suggest that the constant 3−√
5
2 cannot be improved using this method, can actually be reﬁned.

1For clarity, the binary entropy function is denoted with h and the entropy function of a variable with H.

3

Additionally, we (try to) demonstrate why the linear combination in Question 2 is somewhat necessary2

and argue that the constant cannot be signiﬁcantly improved by solving this question
3. Finally, we
summarise the key insights behind the proof. More examples and explanations can also be found in
the survey [6].

2.1. Why the entropy approach works for the union-closed conjecture

The contraposition of the union-closed conjecture states that if every element i ∈ [n] appears in strictly
less than half of the sets of a family F ⊂ 2[n], then F is not union-closed and thus |F | < |F ∪ F |. The
idea behind the entropy approach initiated by Gilmer [12] is that if one can ﬁnd a way to sample sets
from F ∪ F such that the entropy is strictly larger than log2|F |, one can conclude that |F | < |F ∪ F |.
The latter since the entropy of a random variable with N possible outcomes is bounded by log2 N.
Proving that H(A ∪ B) > log2|F | where A, B are sampled from F , is hard when lacking information
on F . It is easier to compare H(A ∪ B) with H(A). For the conclusion to hold, A needs to be sampled
uniform random from F . Gilmer [12] did this by taking two uniform independent (iid) random samples
A, B from F and considering the entropy of the union A ∪ B.
For alternatives, one could sample B non-uniform from F , or have two sampled random variables
which are not independent. In that case one tries to do this in such a way that A ∪ B is as uniformly
distributed over F ∪ F as possible. Exactly uniformly distributed seems impossible. If F would be
union-closed and A is uniform random, A ∪ B needs to be equal to A to ensure that A ∪ B is uniformly
distributed as well. As a concrete example, when F = ( [2]
≥1
)
, then P(A = {1}) P(B = {1}) = 1
3 =
P(A = {2}) P(B = {2}) is impossible. Once one is sampling dependent samples, one would need
additional ideas to know more about the conditional probability distributions. Sawin [20] gave the
most natural choice when sampling the sets element-wise.

2.2. Observations on approximate union-closed set system

Let ψ = 3−√5
2 be the smallest root of 2x − x
2 = 1 − x ⇔ x
2 − 3x + 1 = 0 and g : N → N : n ↦→ g(n)
be a function which is both o(n) and ω(n0.5). In [7], the authors take g(n) ∼ n2/3. The family

F = {A ⊂ [n] : |A| = ψn + g(n) ∨ |A| ≥ (1 − ψ)n} = ( [n]
ψn + g(n)

) ∪ ( [n]
≥ (1 − ψ)n
)

is an approximate union-closed family. That is, the union of two sets (iid, independent identically
distributed, uniform random chosen) in F belongs with high probability to F as well. Nevertheless,
since ψ > 1
3 , one can also observe that F ∪ F = ( [n]
≥ψn+g(n))
. That is, only a small proportion of
F ∪ F belongs to F . As such, this construction, which might suggest that improving the constant ψ
is impossible with the entropy approach, does not necessarily imply this conclusion. If unions of two
sets in F are taken with a non-uniform measure or in a dependent manner such that sets with smaller
unions are more likely to be selected, the initial argument about the sharpness of this construction no
longer holds. The entropy of the union of two random variables, when these variables take values in
F in a dependent way, can indeed be larger. With the dependency proposed by Sawin, the union of
two sets from the approximate union-closed family mentioned above will almost surely have a size of
(0.5 + o(1))n, for example.

2.3. Upper bound for Question 2 and limits on the approach of Sawin

Let h(x) = −x log2(x) − (1 − x) log2(1 − x). Let the roots of the function h(x)(2 − h(x)) − h(2x − x
2)
be 0 < b1 < b2 < 1. Then b1 ∼ 0.139499451909862 and b2 ∼ 0.329454738503037. Choose b = b2 and
a = 1−h(b)
2−h(b) ∼ 0.0788772927059232.

2i.e., variants will not be simpler
3E.g. [17] gave a variant with tiny improvement
 4

Let p, q, r be three identically distributed [0, 1]-valued random variables, where P(p = 1) = a and
P(p = b) = 1 − a, such that p and q are independent and p and r are as negatively correlated as
possible in the sense that P(p = r = 1) = 0. For these choices, we have E[p] = 0.3823455333667034

and (1 − a)
2h(2b − b2) = (1 − 2a) = (1 − a)h(b) which is equivalent with

E[H(p + q − pq)] = E [H (max (p, r, min (p + r, 1/2)))] = E[H(p)].

Hence no linear combination satisﬁes Equation 1 with a strict inequality and local perturbations
(increasing a) will result in counterexamples when c is allowed to be slightly larger.
On a diﬀerent note, we observe that taking a linear combination, as done in Equation 1, will
be necessary to improve the constant 3−√5
2 in the progress on the union-closed conjecture. To see
this, observe that E [H(max(p, r, min(p + r, 1/2)))] < E[H(p)] for p and r identically distributed with
P(p = r = 1) = 0, P(p = b) = 1 − a, and P(p = 1) = a, where b = 1
4 and a = 1−h(b)
2−h(b) + ǫ for some small

ǫ > 0. Since E[p] < 0.37 < 3−√5
2 , considering the single term alone would not lead to an improvement.
From these observations, one can conclude that one cannot aim to prove the result with a constant
better than 0.382345533366703 with the exact suggested approach of Sawin.

2.4. Summary of the proof

The idea from Sawin [20] is to sample sets twice element-wise. Here iteratively, one samples A ∩ [k]
and B ∩ [k] for 0 ≤ k ≤ n based on the probability that a set in F , given the intersection with [k],
would contain the additional element k + 1. The sampling of the element k + 1 for A and B can then
be done in a dependent manner, ensuring that both A and B are uniform samples over F . Once some
elements are sampled, control over the conditional probabilities (the distribution) is lost, so we assume
the worst-case scenario. Since the worst-case scenarios for the two diﬀerent strategies diﬀer, a better
bound is obtained by taking a linear combination of these two diﬀerent ways of sampling in F ∪ F.
As the entropy of the whole sample can be determined by summing (conditional) entropies for every
element k ∈ [n], it is suﬃcient to prove the inequality for these entropies for for a single element. At
this point, the problem reduces to a question that depends purely on the probability distribution of
random variables and their expectations.
To attack that question, we perform local optimisation to ﬁnd properties of an optimal distribution
by redistributing the probability mass function and verifying convexity and concavity. As such, we
reduce the problem to a simpler inequality involving only 4 unknown parameters associated with
a probability distribution whose support contains at most 3 elements. Combining with the work
of Yu [22], this is even further improved to two cases depending on two variables each. The ﬁnal
minimisation problems are veriﬁed numerically with a computer program in two ways, together with
a plot showing that we obtain the global minimum by the proposed atomic probability distribution.

3. Proof for the optimal constant of Question 2

In this section, we prove that the maximum constant c for Question 2 is approximately 0.382345533366
(the value derived in Subsection 2.3). We do so by proving it for the optimal choice of α, α ∼ 0.0356069.
The latter is obtained from comparing derivatives of the atomic solutions with support on {x, 1} and
expectation c around x = b.
That is, the probability p is given by P(p = 1) = c−x
1−x and P(p = x) = 1 − c−x
1−x . Remembering
that p, r are negatively correlated, we let

g1(x) = E[H(p + q − pq)] − E[H(p)] = P(p = x)
2h(2x − x
2) − P(p = x)h(x) and

g2(x) = E [H (max (p, r, min (p + r, 1/2)))] − E[H(p)]
= (1 − 2 P(p = 1)) − P(p = x)h(x)

4The computation can be found in https://github.com/StijnCambie/UCconjecture/blob/main/Sharpness.sagews

5

Then Eq. (1) is equivalent with (1 − α)g1(x) + αg2(x) ≥ 0 and thus α need to satisfy (1 − α)g′
1(b) +
αg′
2(b) = 0 or equivalently α = g′
1(b)
g′
1(b)−g′
2(b) .
We ﬁrst show that it suﬃces to consider the case where the probability distributions p, q, r are not
supported on (0.5, 1). Next, by performing analytical computations on the behaviour of the functions
in two intervals, similar to what Sawin [20] did, we reduce the problem to ﬁnding the minima of a
continuous function in three variables on a bounded region, and subsequently to two variables. As
such, the remaining problem is a minimisation problem for which the statement can be exactly veriﬁed
with the help of a computer.

3.1. Reduction of support of the probability distribution

First we prove that it is suﬃcient to consider [0, 1]-valued random variables which do not attain values
in (0.5, 1).
For readability and since it is suﬃcient to consider ﬁnite supported measures for the application
on Conjecture 1, we prove the following lemmas only in the case of discrete probability distributions.
The proof of the following lemma can be modiﬁed for general probability distributions by replacing
sums by integrals and probability P by probability distribution µ.

Lemma 4. Assume p, q are independent identically distributed (iid) [0, 1]-valued random variables
with expectation E[p] = c ≤ 0.39 such that P(p = y) > 0 for some 1/2 < y < 1. Then the modiﬁed
common probability distribution p′, q′ of p, q for which P(p′ = 1) = P(p = 1) + (2y − 1) P(p =
y), P(p′ = y) = 0, P(p′ = 0.5) = P(p = 0.5) + (2 − 2y) P(p = y) and P(p′ = y′) = P(p = y′) for every
y′ ∈ [0, 1]\{0.5, y, 1} satisﬁes

• E[p′] = E[p] and

• w E[H(p′)] − E[H(p′ + q′ − p′q′)] > w E[H(p)] − E[H(p + q − pq)] for every w ≤ 1.044, where
p′, q′ are iid.

Proof. The ﬁrst part is immediate since the choice of redistribution is chosen in such a way that the
following two linear combinations are true; (2y − 1) + (2 − 2y)0.5 = y and (2y − 1) + (2 − 2y) = 1. The
latter to ensure that we still have a probability distribution. Hence it remains to prove the second
part. For this, we ﬁrst take a very small value ε = P(p=y)
N by choosing a large positive integer N . Let
I be the support (set with all values x for which P(p = x) > 0) with 1/2 and 1 included as well.
First, we do the redistribution of only an ε-fraction in the probability distribution, that is P(p′ =
1) = P(p = 1) + (2y − 1)ε, P(p′ = y) = P(p = y) − ε, P(p′ = 0.5) = P(p = 0.5) + (2 − 2y)ε. Now
E[H(p′ + q′ − p′q′)] − E[H(p + q − pq)] is equal to ελ + O(ε2), where λ equals

2 ∑

x∈I ((2 − 2y)h(0.5(1 − x)) − h((1 − y)(1 − x))) P(p = x).

Here we have used that h(x + y − xy) = h((1 − x)(1 − y)) (by symmetry of h and 1 − (x + y − yx) =
(1 − x)(1 − y)) and h(0) = 0. Let g(x) = (2 − 2y)h(0.5(1 − x)) − h((1 − y)(1 − x)). Note that

ln 2 d
dx g(x) = (y − 1) ln ( (1 − y)(1 + x)
x + y − xy
 ) > 0 and

ln 2 d
2

dx2 g(x) = − (1 − y)(2y − 1)
(x + 1)(x + y − xy) < 0

since 0 < (1 − y)(1 + x) < x + y − xy for 1 > y > 0.5 and every 1 ≥ x ≥ 0. Due to Jensen’s inequality
for the concave function g, λ = 2 E[g(p)] is upper bounded by 2g(c). This upper bound is independent
of P(p = y). Hence we can do this N times and conclude that for p′, q′ distributed as in the lemma,
we have E[H(p′ + q′ − p′q′)] − E[H(p + q − pq)] ≤ 2g(c) P(p = y) + O(ε). It is also straightforward

6

to compute that E[H(p)] − E[H(p′)] = P(p = y) (h(y) − (2 − 2y)h(0.5)) = −g(0) P(p = y). Finally, it
suﬃces to prove that 2g(c) − g(0) < 0

since then ε can be chosen suﬃciently small such that after adding the O(ε) term, it is still negative.
Since g is an increasing function and g(0) < 0 (due to h being concave), it suﬃces to prove that
2g(0.39) − 1.044g(0) < 0. This is the case for every 1
2 < y < 1.
5

Lemma 5. Let p, r be identically distributed [0, 1]-valued random variables, not necessarily inde-
pendent. Then one can modify the underlying common probability distribution by distributing the
probability mass function on (0.5, 1) over 0.5 and 1 such that E[p] is the same and

E [H (max (p′, r′, min (p′ + r′, 1/2)))] ≤ E [H (max (p, r, min (p + r, 1/2)))] .

Proof. We do the following procedure as long as there is some value in (0, 1) with positive probability.
Let y = max{y | 0.5 < y < 1 ∧ P(p = y) > 0} be the largest value in (0, 1) with positive probability
and y′ the second largest such value, or 0.5 if no other value in (0, 1) has positive probability. We
distribute the probability mass function of y over y′ and 1 (such that we still end with a probability
measure). We let p′ and r′ be dependent as before, with the corresponding distribution taken into
account (made clear below). We claim that the considered quantity E [H (max (p, r, min (p + r, 1/2)))]
did not increase by doing so. If P(p = y, r = y) > 0, we increase P(p = y′, r = y′) and P(p = 1, r = 1)
accordingly and conclude by concavity of h. If P(p = y, r = 1) > 0, then max{p, r, min(p+r, 1/2)} = 1
both before and after the local adaptation of p (similarly when p and r are switched) and so there is
no change by this term. If P(p = y, r = z) > 0, for some z ≤ y′, then we conclude again by concavity
of h. By iterating this process, the probability measure on (0.5, 1) is distributed over 0.5 and 1 and
the condition in the lemma is satisﬁed.

Now, assume there are random variables p, q, r satisfying the conditions of Question 2 for which
E[H(p)] ≤ c and (1 − α) E[H(p + q − pq)] + α E [H (max (p, r, min (p + r, 1/2)))] ≤ E[H(p)] for some
α ∈ [0, 1]. Next, we consider the modiﬁed random variables p′, q′, r′, where the probability distri-
bution is iteratively adapted by distributing the probability P(p = y) for some 0.5 < y < 1 over
P(p = 0.5) and P(p = 1). Since 1.044 > 1
1−α , Lemma 4 implies that E[H(p′)] − (1 − α) E[H(p′ +
q′ − p′q′)] > E[H(p)] − (1 − α) E[H(p + q − pq)]. Also E [H (max (p′, r′, min (p′ + r′, 1/2)))] ≤
E [H (max (p, r, min (p + r, 1/2)))] for the natural choice of the adapted dependency of p and r by
Lemma 5. Thus, if there are probability distributions p, q and r for which Equation 1 is not satisﬁed
for some value of c, then these distributions must have support disjoint from (0.5, 1).

3.2. Reduction to small support of the probability distribution

In the previous subsection, we established that for Question 2, it is suﬃcient to consider probability
distributions whose support does not include values in (0.5, 1), and we now further restrict the support
to at most three elements.
First, we observe that the quantity E [H (max (p, r, min (p + r, 1/2)))] is minimised (under the
condition that p and r have the same ﬁxed distribution) when P(p = r = 1) = 0. If P(p = r = 1) and
P(p = x, r = y) > ǫ > 0 for some values 0 < max x, y < 1, we modify the probability distribution by
increasing P(p = x, r = 1) and P(p = 1, r = y) by ǫ, and decreasing P(p = r = 1) and P(p = x, r = y)
by ǫ. This decreases the expectation of the entropy function E [H (max (p, r, min (p + r, 1/2)))]. Note
that in the remaining case P(p = r = 0) would be the only other positive probability and so the
whole expectation E [H (max (p, r, min (p + r, 1/2)))] = P(p = r = 0)h(0) + P(p = r = 1)h(1) is
zero. Similarly, we can make analogous modiﬁcations, decreasing P(p = r = 1) and P(p = 0, r = 0)
with ε = P(p = r = 1) and increasing P(p = 0, r = 1) and P(p = 1, r = 0) with ε. The latter

5Veriﬁcation at https://github.com/StijnCambie/UCconjecture/blob/main/reduction_UC.sagews

7

is possible since we assumed P(p = 1) ≤ 1
2 . Thus, without loss of generality, we may assume that
P(p = r = 1) = 0.
Now, by the result of the previous subsection, subsection 3.1, whenever p, r < 1, we have p, r ≤ 1
2
and hence max (p, r, min (p + r, 1/2)) = min (p + r, 1/2) .
For the remainder of this subsection, let P(p = 1) = a. Deﬁne x0 as the (1 − 2a)-quantile of p,
i.e., the smallest value satisfying P(p ≤ x0) ≥ 1 − 2a.

Lemma 6. We can assume that P(p = r) = 1−2a and this happens exactly for the (1−2a)-quantile x0,
that is, for every x < x0, we have P(p = r = x) = P(p = x) and P(p = r = x0) = 1 − 2a − P(p < x0).

Proof. To prove the statement, we show that probability mass can be redistributed without increasing
the studied expectation.
Since h is an increasing function on [0, 1/2], we can assume that the values x, y ∈ [0, 1/2] for which
P(p = x, r = y) > 0 satisfy x, y ≤ x0. In particular, for x0 < x ≤ 1/2 and y0 < y ≤ 1/2, we have
the following condition: if P(p = x, r = z) > 0 or P(p = z, r = y) > 0, then z = 1. This cancels the
largest values in [0, 1/2], as their combination with 1 results in a contribution of 0 due to h(1) = 0.
If P(p = x, r = y), P(p = x
′, r = y′) ≥ ε > 0, where x < x
′ < x0 ≤ 1/2 and 1/2 ≥ x0 ≥ y > y′,
we can decrease P(p = x, r = y) and P(p = x
′, r = y′) with ε and increase P(p = x, r = y′), P(p =
x
′, r = y) with ε. The studied expectation does not increase, by the follow claim.

Claim 7. The function g : [0, 1] → [0, 1] : x ↦→ h(min(x, 1/2)) is a concave function. For all x, x
′, y, y′ ∈
[0, 1/2] such that x < x
′ and y > y′, we have g(x + y) + g(x
′ + y′) ≥ g(x + y′) + g(x
′ + y).

Proof. The second derivative of g equals that one of h on [0, 1/2) and is therefore strictly negative on
this interval. The second derivative of g is zero for x ≥ 1/2.
Since (x+y)+(x
′ +y′) = (x+y′)+(x
′ +y) and x+y′ < min{x+y, x
′ +y′} and max{x+y, x
′ +y′} <
x
′ + y, the pair {x
′ + y, x + y′} majorises {x + y, x
′ + y′}. The claim now follows from Karamata’s
inequality [14]. ♦

We conclude that we can assume that P(p = r) = 1 − 2a and this happens exactly for the (1 − 2a)-
quantile, that is, for every x < x0, we have P(p = r = x) = P(p = x) and P(p = r = x0) =
1 − 2a − P(p < x0).

Next, we use the same approach as Sawin. Let µ be a probability distribution which minimises

Hµ = (1 − α) E(p,q)∼µ×µ[H(p + q − pq)] + α E
′
p∼µ [H (min (2p, 1/2))] − Ep∼µ[H(p)] (2)

among all probability distributions with expectation bounded by c; Ep∼µ[H(p)] ≤ c. Let Pp∼µ(p =
1) = a and let the (1 − 2a)-quantile of µ be x0. Such a distribution exists, as explained in the proof
of Sawin’s Lemma 3. Here E
′ has to be interpreted as the expectation over the (1 − 2a)-quantile (due
to Lemma 6).

Lemma 8. The probability distribution µ also minimises

2(1 − α) E(p,q)∼µ×ν [H(p + q − pq)] − Ep∼νH[p] + α E
′
p∼ν [H (min (2p, 1/2))]

= Eq∼ν (2(1 − α) Ep∼µ[H(p + q − pq)] − H(q)) + E
′
q∼ν [H (min (2q, 1/2))]

among all probability measures ν for which the (1 − 2a)-quantile is x0, Ep∼ν H[p] ≤ c and Pp∼ν (p =
1) = a.

Proof. Consider the combination µ
′ = (1−ε)µ+εν, which has the same values for x0 and a = P(p = 1).
By deﬁnition of µ being a minimiser, Hµ′ − Hµ ≥ 0. Now Hµ′ −Hµ
ε equals, up to a O(ε) function,

2(1 − α) (( E(p,q)∼µ×ν − E(p,q)∼µ×µ) [H(p + q − pq)]
) − ( Ep∼ν − Ep∼µ)[H(p)]

+ α (
( E
′
p∼ν − E
′
p∼µ) [H (min (2p, 1/2))]
) .

So by taking ε suﬃciently small, we conclude.
 8

Now for every ﬁxed constant 0 ≤ q ≤ 1, the function Fµ(q) = Ep∼µ[2(1 − α)H(p + q − pq) − h(q)]

satisﬁes d
dq (q(1 − q) d2
dq2 Fµ(q)
) < 0, as veriﬁed in the proof of [20, Lem. 3]. By direct computation,

we verify that ln 2 d2
dq2 h (2q) = −2(1−q)
(1−2q) and d
dq (q(1 − q) ln 2 d2
dq2 h (2q)
) = d
dq ( −2
(1−2q)q ) = −2
(1−2q)2 <

0. Hence q(1 − q) ln 2 d2
dq2 (Fµ(q) + h (2q)) is a strictly decreasing function. This implies that if we
consider the function Fµ(q) + h (2q) on the interval I1 = [0, min{x0, 1/4}] and Fµ(q) on the interval
I2 = [min{x0, 1/4}, 1/2] separately, we observe that the second derivative of each function behaves in
one of three ways: it is either strictly positive, strictly negative, or changes sign at a critical point z1
or z2.
I.e., Fµ(q) + H (2q) is either strictly convex on one part of I1 (which is of the form [0, z1] and
strictly concave at the other part ([z1, min{x0, 1/4}]), convex on the whole interval, or concave on
all of I1. Similarly Fµ(q) is either strictly convex on one part of I2, [min{x0, 1/4}, z2], and strictly
concave at the remaining part, [z2, 1], convex on all of I2, or concave on the whole interval I2.
On each interval (so for both I1 and I2), the minimum is attained by a probability distribution
that either has only one value with positive probability (if the studied function is convex), or two,
one of them being the maximum of the interval. When the latter occurs on I2, one can extend I2
to [min{x0, 1/4}, 1] and redistribute the mass from 1/2 over 1 and the inﬂection point z2 of I2 and
repeat as before. Increasing the probability mass of 1 even further decreases E
′
p∼µ[H(min(2p, 1/2))],
so the latter distribution was not a minimising probability distribution in Lemma 8.
This results into candidate probability distributions with at most 4 diﬀerent values with positive
mass.
In total there are 32 = 9 combinations (which one can double based on x0 < 1/4 and x0 ≥ 1/4,
but each such pair works by the same ideas) to consider for the behaviour on the two intervals. The
3 combinations where the considered function on I1 is convex are almost immediate. In the other
situations we can modify the probability measure even further in steps and conclude at the end that
a probability distribution that is a solution in Lemma 8 has at most 3 values with positive mass.
If min{x0, 1/4} = x0 has positive probability on the ﬁrst interval and this is diﬀerent from the
(smallest) value y0 on the second interval that got positive probability, one can repeat the argument by
replacing x0 by min{y0, 1/4}. This implies that in case there are 4 values with positive probability, the
values 1 and 1
4 are among them. But when we would have x0 ≥ 1
4 , we know that E
′[H(min{2p, 1/2})
does not depend on the distribution on the interval [1/4, 1] and as such, we can repeat the argument
about the extremum for Fµ(q). At the end, we conclude that the support has no more than 3
elements with positive probability. Furthermore, if the support contains exactly 3 elements with
positive probability, at least one of them is at most 1/4.
We illustrate this for an example where the function Fµ(q) + H (2q) on I1 ⊊ [0, 1/4] is both
convex and concave (there is an inﬂection point z1 ∈ I1), y0 > 1/4 and Fµ(q) is convex (convex and
concave works similar) on [x0, 1/2], in Fig. 1. Here the red dots represent the values (q, f (q)), where
f (q) = Fµ(q) + H (2q) 1q≤min{x0,1/4}, for those q that have a positive probability under the candidate
probability measure µ.
First we extend I1 = [0, x0] to [0, min{y0, 1/4}] and redistribute the mass. We redeﬁne I1 and I2
and redistribute the mass on [1/4, 1] (here it is within [1/4, 1/2]), to end with a candidate probability
distribution for Lemma 8 which has less than 4 values with positive probability.

3.3. Veriﬁcation for distributions with support of size at most 3

Once the support is reduced to 3 elements, {a1, a2, 1}, by knowing the associated probabilities
p1, p2, 1 − p1 − p2 of each element, the inequality in Question 2 can be checked. As such, we ﬁnd
an optimisation problem in 4 variables. Using Maple, it has been checked in multiple ways; by solving
a minimisation problem in multiple regimes, and by plotting an implicit plot, as well as plots with a
ﬁxed choice for a1 assuming E[p] = c. From these, we note that there are two local regions where

9

x

y
 11/21/4 x

y
 11/21/4

x

y
 11/21/4 x

y
 11/21/4

Figure 1: An example of improving the distribution

the minima occur; around a1 = 0 and around p1 = 06, corresponding with the cases where p is
{0, 1}-valued and the atomic one used to show sharpness in Subsection 2.3.
Finally, we also give a more rigorous proof for the case where the distribution is atomic, i.e.,
P(p = b) = 1 − a and P(p = 1) = a and E[p] = a + (1 − a)b ≤ c, where c ∼ 0.3823455 is
the claimed optimum. Then E[H(p + q − pq)] = (1 − a)
2h(2b − b2), E[H(p)] = (1 − a)h(b) and
E [H (max (p, r, min (p + r, 1/2)))] ≥ (1 − 2a)h(min(2b, 1/2)). Since the case where P(p = r = 1) = 0
is the worst case, we need to show that

(1 − α)(1 − a)
2h(2b − b2) + α(1 − 2a)h(min(2b, 1/2)) − (1 − a)h(b) ≥ 0, or equivalently

(1 − α)h(2b − b2)a2 + (−2(1 − α)h(2b − b2) − 2αh(min(2b, 1/2)) + h(b)
) a + Ob,α(1) ≥ 0

For ﬁxed (non-zero) b, this is a quadratic function in a with positive leading coeﬃcient, which attains
its minimum at a = 1 + 2αh(min(2b,1/2))−h(b)
2(1−α)h(2b−b2) > c−b
1−b and thus it is suﬃcient to prove this in the case
where a = c−b
1−b .
7

3.4. Precise veriﬁcation

If we combine our conclusions from Subsections 3.2 and 3.1 with the one from [22], we obtain that
there are two possible forms for the joint distribution of (p, r). Either p = r and the support of p has
size bounded by 2 (the elements being bounded by 1/2), or the support has 3 elements {a1, a2, 1} and
p1 = 1 − 2p2, where P(p = a2, r = 1) = P(p = 1, r = a2) = p2. Equivalently, with the notation of [22],
the distribution Ppr is of the form (1 − β)Qa,a + βQb,b or (1 − β)Qa,a + βQ1,b (where a ≤ b).
Hereby for a ﬁxed choice of c, β is a function of a and b. In the ﬁrst case, a < c < b and β = c−a
b−a .

In the second case, β = 2(c−a)
1+b−2a .
As such, the ﬁnal veriﬁcation for Question 2 can be deduced from an inequality involving only two
variables. This ﬁnal veriﬁcation has been done in https://github.com/StijnCambie/UCconjecture,
documents FinalComputation24
8, If p = r, the inequality is strict. In the case with the support
containing 1, we deduce that the atomic distribution from subsection 2.3 is the (unique) minimiser,
and the inequality is true and tight.

4. Proof of bound for sharper union-closed conjecture

Having established the answer to Question 2 in the previous section, we now present the formal proof
of Theorem 3, as sketched in [20], to complete the exposition Let α ∼ 0.0356069 and c ∼ 0.3823455

6See https://github.com/StijnCambie/UCconjecture , documents FinalComputation23
7See https://github.com/StijnCambie/UCconjecture/blob/main/Sharpness.sagews
8For some reason, minus is replaced by K in the PDF.
10

be the previously determined optimal constants for Question 2.

Proof of Theorem 3. Assume there is a (nonempty) union-closed family F ⊂ 2[n] for which every
element i ∈ [n] appears in at most a c-fraction of the sets in F . Without loss of generality, we can
assume that 1 appears in at least one set in F . We consider random variables A, B, C, which are three
uniform samples from F , deﬁned as follows. The uniform sampling of B happens independently of the
sampling of A and C. The latter two are sampled element-wise and in a dependent way. We denote
Ai = 1 if i ∈ A and otherwise Ai = 0, i.e., it is the indicator function 1i∈A, and A<i = (A1, . . . , Ai−1)
is the sequence of the ﬁrst i − 1 indicator random variables. Analogously Ci and C<i are deﬁned.
For every i ∈ [n] and given (ﬁxed) realisations a<i = (a1, . . . , ai−1) and c<i = (c1, . . . , ci−1), we
consider the fractions

fa = |{S ∈ F : i ∈ S, S<i = a<i}|
|{S ∈ F : S<i = a<i}| and fc = |{S ∈ F : i ∈ S, S<i = c<i}|
|{S ∈ F : S<i = c<i}| .

If max{fa, fc} > 0.5, we take x ∈ U ([0, 1]), a uniformly random element from [0, 1], and take ai =
[x < fa] and ci = [x < fc]. That is, ai = 1 if x < fa and otherwise ai = 0. Similarly, if fa, fc ≤ 1/2,
we take ai = [x < fa] and ci = [0.5 − fc < x < 0.5] for the uniform random generated x ∈ [0, 1].
If we do the previous steps for every i ∈ [n], there are up to 2i−1 diﬀerent realisations and fractions.
Let pi = P(A<i+1 | A<i) be the conditional probability distribution, associated with the probabil-
ity (fraction) for a<i+1 given any realisation of a<i. Deﬁne ri = P(C<i+1 | C<i) completely analogous.
Then with the above steps for concrete realisations, for the random variable A ∪ C, we have

P[(A ∪ C)i | A<i, C<i] = max{pi, ri, min(pi + ri, 1/2)}.

By the product rule applied to the conditional probabilities pi, we have that A (and similarly C) will
be uniformly distributed over F , that is for a particular set T ∈ F, we have

P(A = T ) = ∏

i∈T
 |{S ∈ F : i ∈ S, S<i = T<i}|
|{S ∈ F : S<i = T<i}| · ∏

i̸∈T
 |{S ∈ F : i ̸∈ S, S<i = T<i}|
|{S ∈ F : S<i = T<i}| = 1
|F | .

Hence A, B, C all have the (same) uniform probability distribution. Let qi = P(i ∈ B | B<i) be a con-
ditional probability distribution. Now pi, qi and ri are identically distributed conditional probability
distributions, where qi is independent from the other two, but pi and qi are dependent.
The chain rule and data processing inequality respectively yield

H((A∪B)<i+1) = H((A∪B)<i)+H((A∪B)<i+1 | (A∪B)<i) ≥ H((A∪B)<i)+H((A∪B)<i+1 | A<i, B<i),

while H(A<i+1) = H(A<i) + H(A<i+1 | A<i). As such to prove that

(1 − α)H(A ∪ B) + αH(A ∪ C) > H(A),

it is suﬃcient to prove that (1 − α)H((A ∪ B)1) + αH((A ∪ C)1) > H(A1) and (1 − α)H((A ∪ B)<i+1 |
A<i, B<i) + αH((A ∪ C)<i+1 | A<i, C<i) ≥ H(A<i+1 | A<i) for every i ≥ 2. But with the conditional
probability distribution of (A∪B)i, with which we refer to P((A∪B)<i+1 | (A∪B)<i), being pi+qi−piqi
(by the principle of inclusion-exclusion) and of (A ∪ C)i being max{pi, ri, min(pi + ri, 0.5)} (by the
choice of the samples), where pi, qi, ri all have expectation less than c, this follows from the answer
to Question 2. Since equality cannot appear for i = 1, the inequality is strict. We conclude that
max{H(A ∪ C), H(A ∪ B)} > H(A) = log2|F |, which is a contradiction. So no such family F as
initially assumed exists.

Acknowledgement

We thank an anonymous referee for their careful reading and valuable suggestions, including critical
remarks on readability that helped improve the presentation of the paper. Their recommendation to
consider connections with the work of Yu [22] led to the addition of Subsection 3.4, strengthening the
resolution of Question 2.
 11

Open access statement. For the purpose of open access, a CC BY public copyright license is
applied to any Author Accepted Manuscript (AAM) arising from this submission.

References

[1] R. Alweiss, B. Huang, and M. Sellke, Improved Lower Bound for the Union-Closed Sets Conjecture, arXiv e-prints
(2022), arXiv:2211.11731.

[2] P. Balister and B. Bollobás, Random union-closed families, in Number theory, analysis, and combinatorics, De
Gruyter Proc. Math., De Gruyter, Berlin, 2014, pp. 1–9.

[3] I. Balla, B. Bollobás, and T. Eccles, Union-closed families of sets, J. Combin. Theory Ser. A 120 (2013)(3),
531–544, URL https://doi.org/10.1016/j.jcta.2012.10.005.

[4] H. Bruhn, P. Charbit, O. Schaudt, and J. A. Telle, The graph formulation of the union-closed sets conjecture,
European J. Combin. 43 (2015), 210–219, URL https://doi.org/10.1016/j.ejc.2014.08.030.

[5] H. Bruhn and O. Schaudt, The journey of the union-closed sets conjecture, Graphs Combin. 31 (2015)(6), 2043–
2074, URL https://doi.org/10.1007/s00373-014-1515-0.

[6] S. Cambie, Progress on the union-closed conjecture and oﬀsprings in winter 2022-2023, arXiv e-prints (2023),
arXiv:2306.12351.

[7] Z. Chase and S. Lovett, Approximate union closed conjecture, arXiv e-prints (2022), arXiv:2211.11689.

[8] T. M. Cover and J. A. Thomas, Elements of information theory, Wiley-Interscience [John Wiley & Sons], Hoboken,
NJ, second edn., 2006.

[9] D. Ellis, Note: a counterexample to a conjecture of Gilmer which would imply the union-closed conjecture, arXiv
e-prints (2022), arXiv:2211.12401.

[10] P. Frankl, Extremal set systems, in Handbook of combinatorics, Vol. 1, 2, Elsevier Sci. B. V., Amsterdam, 1995,
pp. 1293–1329.

[11] P. Frankl and N. Tokushige, Extremal problems for ﬁnite sets, vol. 86, American Mathematical Soc., 2018.

[12] J. Gilmer, A constant lower bound for the union-closed sets conjecture, arXiv e-prints (2022), arXiv:2211.09055.

[13] Y. Hu, On the Union-Closed Sets Conjecture, arXiv e-prints (2017), arXiv:1706.06167.

[14] J. Karamata, Sur une inégalité rélative aux fonctions convexes., Publ. Math. Univ. Belgrade 1 (1932), 145–148.

[15] I. Karpas, Two Results on Union-Closed Families, arXiv e-prints (2017), arXiv:1708.01434.

[16] E. Knill, Graph generated union-closed families of sets, arXiv preprint math/9409215 (1994).

[17] J. Liu, Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling, arXiv
e-prints (2023), arXiv:2306.08824.

[18] D. Reimer, An average set size theorem, Combin. Probab. Comput. 12 (2003)(1), 89–93, URL
https://doi.org/10.1017/S0963548302005230.

[19] I. Rival, Graphs and order, nato asi series, vol. 147, 1985.

[20] W. Sawin, An improved lower bound for the union-closed set conjecture, arXiv e-prints (2022), arXiv:2211.11504.

[21] P. Wójcik, Union-closed families of sets, Discrete Math. 199 (1999)(1-3), 173–182, URL
https://doi.org/10.1016/S0012-365X(98)00208-8 .

[22] L. Yu, Dimension-free bounds for the union-closed sets conjecture, Entropy 25 (2023)(5), URL
https://www.mdpi.com/1099-4300/25/5/767.
 12
