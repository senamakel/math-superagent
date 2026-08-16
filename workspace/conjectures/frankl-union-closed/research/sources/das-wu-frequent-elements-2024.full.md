<!-- source: https://arxiv.org/pdf/2412.03862 | converted from PDF -->

Frequent elements in union-closed set families

Shagnik Das∗ Saintan Wu†

July 15, 2025

Abstract

The Union-Closed Sets Conjecture asks whether every union-closed set family F has
an element contained in half of its sets. In 2022, Nagel posed a generalisation of this
problem, suggesting that the kth-most popular element in a union-closed set family must
be contained in at least 1
2k−1+1 |F| sets.
We combine the entropic method of Gilmer with the combinatorial arguments of Knill
to show that this is indeed the case for all k ≥ 2, and characterise the families that achieve
equality. Furthermore, we show that when |F| → ∞, the kth-most frequent element will
appear in at least ( 3−√5
2 − o(1)
) |F| sets, reflecting the recent progress made for the
Union-Closed Set Conjecture.

1 Introduction

Frankl’s Union-Closed Set Conjecture is arguably one of the most famous (or, according to
some sources, notorious) open problems in extremal set theory. A family F of subsets of a
ground set [n] is said to be union-closed if, for every A, B ∈ F, we have A ∪ B ∈ F. While
union-closed families come in many shapes and sizes, Frankl conjectured in 1979 that they all
must contain a popular element.

Conjecture 1.1. For every union-closed set family F ̸= {∅} over a ground set [n], there is
an element i ∈ [n] belonging to at least half of the sets in F.

Since its formulation, the conjecture has attracted a great deal of attention from the
combinatorial community, even being the focus of a recent PolyMath project [15]. The problem
has stubbornly resisted all attacks, with only partial results having been obtained to date.
In one direction, researchers have proven the conjecture for several special classes of union-
closed set families. For example, Vuˇckovi´c and ˇZivkovi´c [21] established the conjecture for
union-closed set families when n ≤ 12, Roberts and Simpson [18] showed that a minimal
counterexample requires |F| ≥ 4n − 1, and Balla, Bollob´as, and Eccles [4] resolved the case
when |F| ≥ 2
32
n. Various other conditions have also been considered [1, 5, 12, 17, 20], and

∗Department of Mathematics, National Taiwan University, Taipei, Taiwan. Research supported by Taiwan
NSTC grants 111-2115-M-002-009-MY2 and 113-2628-M-002-008-MY4. Email: shagnik@ntu.edu.tw
†Department of Mathematics, National Taiwan University, Taipei, Taiwan. Email: r12221025@ntu.edu.tw

1arXiv:2412.03862v3  [math.CO]  11 Jul 2025
1 INTRODUCTION

we refer the reader to Bruhn and Schaudt’s [6] comprehensive survey detailing progress along
these lines.
Another approach has been to prove weaker results for general union-closed set families,
showing that there must be an element in many sets, if not quite half of them. For instance,
Knill [10] showed that there is always an element contained in at least |F|−1
log2 |F| sets of a union-
closed set family F, with the constant factor later improved by W´ojcik [22]. Other lower bounds

involved the size of the ground set n; Balla [3] proved a lower bound of 1
2 ( log2 n
n )1/2 |F|, while

Reimer [16] gave a bound of log2 |F|
2n |F|, and these were the state-of-the-art until a few years ago.
In 2022, Gilmer [9] made a major breakthrough, introducing novel entropic methods to
come within a constant factor of the conjecture. He proved that if F ̸= {∅} is union-closed, it
contains an element in 1
100|F| sets. This sparked a flurry of activity, and within days several
authors had independently optimised the calculations to push the bound further. Alweiss,
Huang and Sellke [2] and Pebody [14] improved the lower bound to 3−
√5
2 |F|, which Gilmer had
suggested to be the limit of his method. Then Sawin [19], Cambie [7], and Liu [11] made further
progress, increasing the bound from 3−√5
2 |F| ≈ 0.381966|F| to approximately 0.3823455|F|,
which is where things stand today.

1.1 Less frequent elements

Aside from attempts to solve Conjecture 1.1 directly, there have also been several equivalent
formulations and variants proposed and studied. In his note on union-closed set families,
Nagel [13] suggested investigating the frequencies of elements beyond the most popular one,
offering the following conjecture.

Conjecture 1.2. For any union-closed set family F with |∪F ∈F F | ≥ k, the kth-most frequent
element lies in at least |F|
2k−1+1 sets in F.

Note that this generalises Conjecture 1.1, which is the case k = 1. Furthermore, the
conjectured bound is best possible, as evidenced by the families we call near-k-cubes, which
are complete boolean lattices of dimension k − 1, together with one additional set; that is,
Fk = 2
[k−1] ∪ {S}, where [k − 1] ⊊ S. This is a union-closed family of size 2
k−1 + 1 in which
the element k features only once. Unlike in Frankl’s Conjecture, though, this is essentially the
only known tight construction; we do not know of any constructions of larger sizes.
Before proceeding to our main result, we observe that Nagel’s conjecture is in fact equiva-
lent to Frankl’s. This extends a remark of Nagel [13], who used the Union-Closed Set Conjecture
to give a weaker lower bound of m
2k .

Observation 1.3. Assuming the Union-Closed Sets Conjecture, Nagel’s conjecture is true for
all k.

Proof. Fix k ∈ N, and let F be a union-closed set family with |F| = m and | ∪F ∈F F | ≥ k.
Without loss of generality, we suppose the (k − 1) most frequent elements in the ground set [n]
are 1, 2, . . . , k − 1, breaking any ties arbitrarily.
 2

1 INTRODUCTION

Consider the 2
k−1-to-1 map πk−1 : 2
[n] → 2
[n]\[k−1] defined by πk−1(F ) = F \[k−1]. Observe
that πk−1(F) is still a union-closed family that contains a nonempty set, since the support of
F is too large to be contained in [k − 1].
By the Union-Closed Sets Conjecture, there exists an element a /∈ [k − 1] contained in
f ≥ 1
2|πk−1(F)| sets in πk−1(F). Tracing sets in πk−1(F) back to their disjoint preimages in F,
we find the following hold:

(i) if F ∈ πk−1(F) contains a, then π−1
k−1(F ) ⊆ F contains at least one set, and they all
contain a, and

(ii) if F ∈ πk−1(F) does not contain a, then π−1
k−1(F ) ⊆ F contains at most 2k−1 sets, none of
which contain a.

It follows that the proportion of sets in F containing a is at least f
f +2k−1(|πk−1(F )|−f ) ≥

1
1+2k−1 , and hence Nagel’s conjecture is true.

1.2 Our results

Nagel [13] himself had proven the conjecture unconditionally in the special cases of the least and
second-least frequent elements. Our main result provides a complete resolution of Conjecture 1.2
for all k ≥ 2.

Theorem 1.4. Let k ≥ 2, and let F be a union-closed set family with | ∪F ∈F F | ≥ k. Then
the kth-most frequent element lies in at least |F|
2k−1+1 sets in F, with equality only if F is a
near-k-cube.

Our proof combines the approaches previously used to attack Conjecture 1.1. For large
set families, we adapt the entropic argument of Gilmer [9] to establish lower bounds on the
frequency of the kth-most frequent element. In fact, as shown in the following theorem, we
can match the Gilmeresque lower bound, suggesting that large union-closed set families do not
exhibit any drop-off in the frequencies of the most popular elements.

Theorem 1.5. For any 0 ≤ α < 3−
√5
2 , there is a constant cα ≥ 0 such that if k ≥ 2 and F is
a union-closed set family with |F| ≥ 2
cα(k−1), then there are at least k elements in the ground
set that each appear in at least α|F| sets in F.

We remark that the proof gives an explicit value for cα, which yields a concrete lower
bound on the size of families for which Theorem 1.5 applies. For smaller families, we instead
use the combinatorial method of Knill [10] to obtain the required lower bound on the frequency
of the kth-most popular element.

Organisation and Notation. In Section 2 we prove Theorem 1.5, establishing our bounds
for large set families. We then study smaller set families in Section 3. Finally, we bring the
parts of our proof of Theorem 1.4 together in Section 4, before raising questions about the

3

2 LARGE FAMILIES

true nature of the kth-highest frequency in set families and suggesting directions for further
research.
We shall take [n] = {1, 2, . . . , n} to be the ground set for our set families F, and will
denote their size by m = |F|. For an element i ∈ [n] of the ground set, we denote its (relative)
frequency in F by
 FreqF (i) = |{F ∈ F : i ∈ F }|
|F| ,

and define the kth frequency of F, denoted fk(F), to be the kth-highest frequency among
the elements of the ground set. We shall further assume, without loss of generality, that the
elements are ordered by their frequency in F; that is, FreqF (1) ≥ FreqF (2) ≥ . . . ≥ FreqF (n),
and fk(F) = FreqF (k).
With this notation, Nagel’s conjecture can be reformulated to say that for any union-closed
set family F involving at least k elements, we have fk(F) ≥ 1
2k−1+1. Finally, note that we may,
and will, assume that the empty set is a member of F, since, if it is not, including it preserves
the union-closed property while decreasing the frequency of every element.

2 Large families

In this section we will prove Theorem 1.5, showing that the Gilmeresque bounds on the most
frequent element also apply to the kth-most frequent element when the family is large. In
particular, we will use the method of entropy, and when taking a random set A, it will be
useful to consider events of a given element being contained in A.

Definition 2.1. For any distribution A on 2[n], let Ai be the indicator variable of the event
i ∈ A, and A<i be the joint variable (A1, A2, . . . , Ai−1). Note that A = A<n+1.

2.1 Entropic preliminaries

Entropy is a very useful tool derived from Information Theory. Informally speaking, it quantifies
the amount of information that revealing a random variable yields. Before presenting our proof,
we provide an overview of some basic facts about entropy, focusing on the case of discrete
random variables. We refer the interested reader to [8] for further details.

Definition 2.2 (Entropy). Given random variables X and Y ,

(i) the entropy of a discrete random variable X is given by

H(X) = ∑

x −P(X = x) log2(P(X = x)),

with the convention that 0 log2 0 = 0, and

(ii) the conditional entropy of X given Y is H(X|Y ) = Ey[H(X|Y = y)], the expected value
of the entropy of X given knowledge of Y .

A simple yet important example is the entropy of the Bernoulli distribution.
 4

2 LARGE FAMILIES

Example 2.3 (Binary entropy function). Let X have the Bernoulli distribution with param-
eter p. Then H(X) = −p log2 p − (1 − p) log2(1 − p). Viewed as a function of p, denoted by
H(p), it is called the binary entropy function.

In this paper, we will use the following fundamental properties of entropy, most of which
can be proven by Jensen’s inequality.

Property 2.4. Let X, Y, X0, X1, . . . , Xn be random variables on a finite sample space.

1. Chain rule. H(X, Y ) = H(X|Y ) + H(Y ).
More generally, H(X1, . . . , Xn) = ∑n
i=1 H(Xi|X<i).

2. Range of entropy. If X takes n values, we have 0 ≤ H(X) ≤ log2 n, and equality holds
in the upper bound if and only if X is uniformly distributed.

3. Conditioning lowers entropy. H(X|Y ) ≤ H(X), and equality holds if and only if X
and Y are independent.

4. Data processing. For any function f of Y , we have H(X|f (Y )) ≥ H(X|Y ). Intuitively,
this means that knowing less in advance makes any new information X more informative.

2.2 Size bound of families with low frequencies

We first briefly explain the idea behind Gilmer’s proof. Gilmer [9] proved that if we have a
distribution over 2
[n] where every element in [n] appears with probability at most α, for some
α ≤ 1
100, then, for A and B sampled independently from this distribution, H(A ∪ B) ≥ H(A).
He proved this by using the chain rule to decompose the entropy element-wise, and then showing
that the inequality H((A ∪ B)i|A<i, B<i) ≥ H(Ai|A<i)

holds for each element appearing infrequently.
Subsequent work [2, 19] showed that this also holds for α as large as 3−√5
2 . Furthermore,
Sawin [19] proved the following optimisation result sharpening this inequality, which will be of
use in our own work.

Lemma 2.5. Let A, B be i.i.d. random sets on the family 2
[n]. Suppose further that E[Ai] ≤
α < 3−
√5
2 . Then H((A ∪ B)i|A<i, B<i) ≥ λαH(Ai|A<i),

where λα = H(2α−α2)
H(α) > 1.1 In particular, H(A ∪ B) ≥ λαH(A).

To obtain lower bounds for the Union-Closed Set Conjecture, Gilmer considered the uni-
form distribution Unif(F) over a union-closed set family. If all elements have low frequency in
F, then, for A and B sampled independently and uniformly from F, we have H(A∪B) ≥ H(A).
However, as F is union-closed, it follows that A ∪ B is also a distribution over F, but is not

1Sawin also showed that this inequality holds when α ≥ 3−√5
2 , but with the constant λα defined to be

1+√5
2 (1 − α) instead of H(2α−α
2)
H(α) .
 5

2 LARGE FAMILIES

uniform — the probability that A ∪ B is the empty set is only 1/|F|2, since we need both A
and B to be empty. This contradicts Property 2.4, which asserts that the uniform distribution
is the unique distribution maximising the entropy.
When dealing with the kth frequency, the condition E[Ai] ≤ α now only applies for i ≥ k.
Thus, to make use of Lemma 2.5, we shall first project F onto [n] \ [k − 1], thereby removing
the k − 1 most frequent elements. Afterwards, we shall perform some estimates to recover
information about the original family.
Specifically, we prove the following.

Theorem 2.6. Let k ≥ 2 and 0 < α < 3−√5
2 . If F is a union-closed family with fk(F) ≤ α,
then log2 |F| ≤ λα
λα−1(k − 1). In fact,

log2 |F| ≤ λα
λα − 1 · 2
k−1(k − 1)
2k−1 − 1 − 1
(λα − 1) log2
 ( λα2
k−1(k − 1)e
(2k−1 − 1) log2 e
 ) .

Proof. Let F be a union-closed family with fk(F) ≤ α. As we do not have information about
the frequencies of the k − 1 most frequent elements, we shall project onto their complement,
using the map πk−1 from the proof of Observation 1.3:

πk−1 : 2
[n] → 2
[n]\[k−1]

F ↦→ F \ [k − 1].

Now let X be a uniformly random set in F, and let A = πk−1(X) be its projection.
Observe that for any i ≥ k, we have E[Ai] = P(i ∈ A) = P(i ∈ X) ≤ α. Hence, if we let B
be independent of and identically distributed as A, Lemma 2.5 gives H(A ∪ B) ≥ λαH(A),
where λα = H(2α−α2)
H(α) . To obtain the desired contradiction, we need provide an upper bound for
H(A ∪ B) and a lower bound for H(A).
For the upper bound, we simply apply the support bound. Since πk−1(F) is still union-
closed, A ∪ B is again a distribution on πk−1(F). Hence, H(A ∪ B) ≤ log2 |πk−1(F)|.
For a lower bound on H(A), observe that, since X is uniformly distributed over F, we
have H(X) = log2 |F|. On the other hand, we have H(X) = H(A, X), since A is determined
by X. Applying the chain rule gives H(A, X) = H(A) + H(X|A). Putting this all together
yields H(A) = log2 |F| − H(X|A).
Combining the upper and lower bounds results in

log2 |πk−1(F)| ≥ λα (log2 |F| − H(X|A)) . (1)

We next evaluate H(X|A). By definition,

H(X|A) = ∑

F ∈πk−1(F ) P(A = F )H(X|A = F ) = ∑

F ∈πk−1(F )
 |π−1
k−1(F )|
|F| H(X|A = F ).

Conditioning on A = F , we have that X is uniformly distributed on π−1
k−1(F ), and so

H(X|A) = ∑

F ∈πk−1(F )
 |π−1
k−1(F )|
|F| log2 |π−1
k−1(F )|.
 6

3 SMALL FAMILIES

For a simple bound, observe that |π−1
k−1(F )| ≤ 2
k−1 for all F , and so it follows that
H(X|A) ≤ k − 1. Substituting this into (1), together with the trivial bound |πk−1(F)| ≤ |F|,
we get log2 |F| ≤ λα
λα−1(k − 1), proving the first inequality from the statement of the theorem.
For the more precise estimate, note that the function f (x) = x log2 x is convex, and hence
for any x ∈ [1, 2
k−1], we have f (x) ≤ 2k−1−x
2k−1−1 f (1) + x−1
2k−1−1f (2k−1) = (x − 1) 2k−1(k−1)
2k−1−1 . Thus,

H(X|A) = ∑

F ∈πk−1(F ) f (|π−1
k−1(F )|)
|F| ≤ ∑

F ∈πk−1(F ) |π−1
k−1(F )|−1
|F| · 2k−1(k−1)
2k−1−1 = (1 − |πk−1(F )|
|F| ) 2k−1(k−1)
2k−1−1 .

Letting ρ = |πk−1(F )|
|F| , we can substitute this into (1) to obtain

log2 ρ + log2 |F| ≥ λα
 (
log2 |F| − (1 − ρ)2
k−1(k − 1)
2k−1 − 1
 ) ,

which can be rearranged to give (λα − 1) log2 |F| ≤ log2 ρ + (1 − ρ)λα 2k−1(k−1)
2k−1−1 .

By differentiating, we find the right-hand side is maximised when ρ = (2k−1−1) log2 e
λα2k−1(k−1) , for

which the right-hand side becomes λα2k−1(k−1)
2k−1−1 − log2 ( λα2k−1(k−1)e
(2k−1−1) log2 e ). This gives the desired
upper bound on log2 |F|.

Using this result, we can prove Conjecture 1.2 for large families.

Proposition 2.7. Given k ≥ 2, let F be union-closed with | ∪F ∈F F | ≥ k.

(a) If |F| ≥ 2
2.71(k−1), then fk(F) > 1
17.

(b) If k = 4 and |F| ≥ 14, then f4(F) > 1
9.

(c) If k = 3 and |F| ≥ 6, then f3(F) > 1
5.

(d) If k = 2 and |F| ≥ 4, then f2(F) > 1
3.

Proof. For part (a), we apply Theorem 2.6 with α = 1
17. Note that λ 1
17 ≈ 1.587624, and so

λ 1
17
λ 1
17 −1(k − 1) < 2.71(k − 1). Hence, our claim follows from the first inequality in the theorem.

For the other parts, we use the second inequality in Theorem 2.6. Let B(α, k) denote
the upper bound on log2 |F| it gives. By direct evaluation, we have B( 1
9, 4) ≈ 3.805781,
B( 1
5, 3) ≈ 2.512253, and B( 1
3, 2) ≈ 1.697618, which yield the desired bounds on |F|.

3 Small families

Proposition 2.7 resolves Conjecture 1.2 for families F with |F| = 2Ω(k). In this section we
handle smaller families, starting with those that are very small.

Proposition 3.1. If F is a union-closed set family with |F| ≤ 2
k + 1 and | ∪F ∈F F | ≥ k, then
fk(F) ≥ 1
2k−1+1, with equality if and only if F is a near-k-cube.

Proof. Recall that we order the elements by frequency, so in particular [k − 1] consists of the
k − 1 most frequent elements.
 7

3 SMALL FAMILIES

First suppose F contains two sets F1, F2 that are not fully contained in [k − 1]. Without
loss of generality, F2 ̸⊆ F1. Then, setting F3 = F1 ∪ F2, we have F3 ̸= F1, and they contain a
common element outside [k − 1]. This implies fk(F) ≥ 2
|F| ≥ 2
2k+1 > 1
2k−1+1 .
Thus, F can only contain a single set S /∈ 2
[k−1], and so |F| ≤ 2
k−1 + 1 and fk(F) = 1
|F| .
In particular, fk(F) ≥ 1
2k−1+1 , and for equality, we must have |F| = 2
k−1 + 1. This is only
possible if 2
[k−1] ⊆ F and, furthermore, [k − 1] ⊊ S, as otherwise S ∪ [k − 1] would be a second
set in F \ 2
[k−1]. In other words, F is a near-k-cube.

Observe that between Proposition 2.7 and Proposition 3.1, we have already proven Con-
jecture 1.2 when 2 ≤ k ≤ 4. For k ≥ 5, it remains to handle set families F with 2
k + 2 ≤
|F| < 2
2.71(k−1). For these families, we adapt a proof of Knill [10] who, we recall, proved that
f1(F) ≥ 1
log2 |F|+1. In our range of interest, log2 |F| = Θ(k) is much smaller than the denomi-
nator of 2
k−1 + 1 in Conjecture 1.2, and so although Knill’s bound is a considerable weakening
of Frankl’s Conjecture, it will be more than sufficient for our purposes.
Our goal is to show that there is some element in [n] \ [k − 1] with large frequency. To
this end, we denote by F≥k the subfamily of F consisting of sets that contain some element in
[n] \ [k − 1]; that is, F≥k = F \ 2
[k−1]. We are assuming | ∪F ∈F F | ≥ k, which implies F≥k ̸= ∅,
and we shall be particularly interested in vertex covers of this subfamily.

Definition 3.2 (k-good). A set S ⊆ [n] \ [k − 1] is k-good for F if, for every F ∈ F≥k, we have
F ∩ S ̸= ∅. We say S is minimal if none of its proper subsets are k-good.

We emphasise that a k-good set S does not need to be a member of the family F. Fur-
thermore, since [n] \ [k − 1] is k-good, we know that minimal k-good sets always exist. Since,
in some sense, minimal k-good sets cover all the members F≥k efficiently, we might expect that
they contain elements of large frequency, and we show that this is indeed the case.

Proposition 3.3. Let F be a union-closed set family containing m sets. If k ≥ 5 and
2
k + 2 ≤ m ≤ 2
3(k−1), then fk(F) > 1
2k−1+1 .

Proof. Let F be such a union-closed set family, and let S ⊆ [n] \ [k − 1] be minimally k-good
for F. By virtue of k-goodness, S meets every set in F≥k, and hence there are at least |F≥k|
incidences between elements of S and members of F≥k. As there can be at most 2
k−1 members
of F whose support is contained in [k − 1], we have |F≥k| ≥ |F| − 2
k−1 = m − 2
k−1, and then
averaging yields an element of S contained in at least m−2k−1
|S| members of F. In particular,
since S ⊆ [n] \ [k − 1], and thus does not contain any of the k − 1 most frequent elements, we
have
 fk(F) ≥ m − 2
k−1

m|S| .

We thus need to bound the size of S. For this, we use the fact that S is minimally k-good.
Indeed, for every y ∈ S, we know that S \ {y} is not k-good for F, and hence there must be
some set Fy ∈ F≥k that is disjoint from S \ {y}. However, since S is k-good for F, we know
Fy intersects S. Thus, we must have Fy ∩ S = {y}.
Given a subset Y ⊆ S, define FY = ∪y∈Y Fy. Since F is union-closed, we must have
FY ∈ F. Moreover, since FY ∩ S = ∪y∈Y (Fy ∩ S) = Y , these sets are all distinct. This shows

8

4 CONCLUDING REMARKS

|F| ≥ 2
|S|, or |S| ≤ log2 m. Plugging this into our lower bound for fk(F), we obtain

fk(F) ≥ m − 2
k−1

m log2 m .

We can now deduce our result. Indeed, since m > 2
k, we have m − 2
k−1 > 1
2m, and thus
fk(F) > 1
2 log2 m ≥ 1
6(k−1), where in the final inequality we use the upper bound m ≤ 2
3(k−1).
For all k ≥ 6, we have 6(k − 1) ≤ 2
k−1 + 1, and hence we have the desired bound.
When k = 5, we have 1
2 log2 m ≥ 1
17 for m ≤ 2
17/2, proving the conjecture in this case. On
the other hand, if m ≥ 2
17/2, then we actually have m − 2
k−1 > 15
16m, and thus our lower bound
becomes f5(F) ≥ 15
16 log2 m ≥ 5
64 > 1
17, which again gives the required result.

4 Concluding remarks

In this paper, we studied a conjecture of Nagel regarding the frequency of the kth-most popular
element in union closed set families. We used entropic methods to handle large families, while
resorting to combinatorial arguments for smaller families. In this final section, we combine
these results to establish our main result, and then address some outstanding open questions.

4.1 Piecing it all together

We proved three results — Propositions 2.7, 3.1 and 3.3 — that established the conjecture for
union-closed set families F of various sizes m = |F|. Table 1 summarises the different ranges
in which these results apply.
 k = 2 k = 3 k = 4 k ≥ 5
Conjectured bound fk(F) ≥ 1
3 fk(F) ≥ 1
5 fk(F) ≥ 1
9 fk(F) ≥ 1
2k−1+1
Proposition 3.1 m ≤ 5 m ≤ 9 m ≤ 17 m ≤ 2
k + 1
Proposition 3.3 2
k + 2 ≤ m ≤ 2
3(k−1)

Proposition 2.7 m ≥ 4 m ≥ 6 m ≥ 14 m ≥ 2
2.71(k−1)

Table 1: Effective range of three propositions, with |F| = m

We see that between them, the propositions settle all cases. Note that Proposition 2.7
and Proposition 3.3 establish strict lower bounds for the conjectured bound on fk(F), while
Proposition 3.1 shows that the only case achieving equality is the near-k-cube. Thus, putting
these results together yields a complete resolution of Conjecture 1.2 for k ≥ 2.

4.2 Frequencies in large families

In fact, for large union-closed set families F, we did not just show that fk(F) > 1
2k−1+1, but
proved quite a bit more. Theorem 1.5 indicates the following:

Corollary 4.1. For any fixed k, fk(F) ≥ 3−√5
2 − o(1) as |F| → ∞.
 9

REFERENCES

Note that the value 3−√5
2 is the constant obtained from the proof of Gilmer [9], with the
calculations as optimised by Alweiss, Huang and Sellke [2] and Pebody [14]. That is, there does
not appear to be any discernible difference in the behaviour of the most frequent element and
the kth-most frequent element. This leads one to wonder whether a direct analogue of Frankl’s
Conjecture (Conjecture 1.1) might hold in large families for the kth-most frequent element;
namely, that it should lie in half the sets. Our attempts to construct families whose kth
frequency is significantly smaller have not borne fruit, and so we pose the following conjecture.

Conjecture 4.2. For any k ∈ N, fk(F) = 1
2 − o(1) when |F| → ∞.

We note that, in contrast to Conjecture 1.1, this bound can only hold asymptotically.
Indeed, the following example shows that fk(F) cannot approach 1
2 too quickly when k ≥ 2.

Example 4.3. Let {Si : 1 ≤ i ≤ k − 1} be a collection of pairwise-disjoint ground sets, each
of size n + 1. For each i, let s∗
i ∈ Si be a distinguished element.
Define Fi = ∅ ∪ {F ⊆ Si : s∗
i ∈ F }, and take the set family F to be the direct sum of these
families, given by F = ⊎Fi = {∪
k−1
i=1 Fi : Fi ∈ Fi}.

It is straightforward to verify that F is a union-closed set family of m = (2
n + 1)k−1 sets, in
which the kth-most frequent element appears in just 2
n−1(2
n + 1)k−2 sets. Hence, we have

fk(F) = 2
n−1(2
n + 1)k−2

(2n + 1)k−1 = 1
2 − 1
2m1/(k−1) < 1
2.

As a first step towards Conjecture 4.2, one could see if the improved bounds of Sawin [19],
Cambie [7], and Liu [11] for the Union-Closed Sets Conjecture can also be employed in this
setting to show a lower bound of fk(F) ≥ 3−
√5
2 + δ, for some δ > 0, provided F is sufficiently
large.

Acknowledgements

We are grateful to Kuo-Han Ku for some initial discussions, and to Hung-Hsun Hans Yu and
Ting-Wei Chao for their comments on an early manuscript.

References

[1] James Aaronson, David Ellis, and Imre Leader, A note on transitive union-closed families,
Electron. J. Combin. 28 (2021), no. 2, Paper No. 2.3, 4.

[2] Ryan Alweiss, Brice Huang, and Mark Sellke, Improved lower bound for Frankl’s union-
closed sets conjecture, Electron. J. Combin. 31 (2024), no. 3, Paper No. 3.35, 11.

[3] Igor Balla, Minimum density of union-closed families, 2011, arXiv:1106.0369.
 10

REFERENCES

[4] Igor Balla, B´ela Bollob´as, and Tom Eccles, Union-closed families of sets, J. Combin.
Theory Ser. A 120 (2013), no. 3, 531–544.

[5] Henning Bruhn, Pierre Charbit, Oliver Schaudt, and Jan Arne Telle, The graph formulation
of the union-closed sets conjecture, European J. Combin. 43 (2015), 210–219.

[6] Henning Bruhn and Oliver Schaudt, The journey of the union-closed sets conjecture,
Graphs Combin. 31 (2015), no. 6, 2043–2074.

[7] Stijn Cambie, Better bounds for the union-closed sets conjecture using the entropy ap-
proach, 2022, arXiv:2212.12500.

[8] Thomas M Cover, Elements of information theory, John Wiley & Sons, 1999.

[9] Justin Gilmer, A constant lower bound for the union-closed sets conjecture, 2022,
arXiv:2211.09055.

[10] Emanuel Knill, Graph generated union-closed families of sets, 1994, arXiv:math/9409215.

[11] Jingbo Liu, Improving the lower bound for the union-closed sets conjecture via conditionally
iid coupling, 2024 58th Annual Conference on Information Sciences and Systems (CISS)
(2023), 1–6.

[12] Robert Morris, FC-families and improved bounds for Frankl’s conjecture, European J.
Combin. 27 (2006), no. 2, 269–282.

[13] Nicolas Nagel, Notes on the union closed sets conjecture, 2023, arXiv:2208.03803.

[14] Luke Pebody, Extension of a method of Gilmer, 2022, arXiv:2211.13139.

[15] PolyMath, Frankl’s union-closed conjecture, https://www.michaelnielsen.org/
polymath/index.php?title=Frankl%27s_union-closed_conjecture, 2016.

[16] David Reimer, An average set size theorem, Combin. Probab. Comput. 12 (2003), no. 1,
89–93.

[17] J¨urgen Reinhold, Frankl’s conjecture is true for lower semimodular lattices, Graphs Com-
bin. 16 (2000), no. 1, 115–116.

[18] Ian Roberts and Jamie Simpson, A note on the union-closed sets conjecture, Australas. J.
Combin. 47 (2010), 265–267.

[19] Will Sawin, An improved lower bound for the union-closed set conjecture, 2023,
arXiv:2211.11504.

[20] Theresa P. Vaughan, Families implying the Frankl conjecture, European J. Combin. 23
(2002), no. 7, 851–860.

[21] Bojan Vuˇckovi´c and Miodrag ˇZivkovi´c, The 12-element case of Frankl’s Conjecture, IPSI
BgD Transactions on Internet Research 13 (2017), 65–71.
 11

REFERENCES

[22] Piotr W´ojcik, Union-closed families of sets, Discrete Math. 199 (1999), no. 1-3, 173–182.

12
