<!-- source: https://arxiv.org/pdf/2211.12401 | converted from PDF -->

arXiv:2211.12401v1  [math.CO]  22 Nov 2022Note: a counterexample to a conjecture of Gilmer
which would imply the union-closed conjecture

David Ellis
∗

22nd November 2022

Abstract

In this very short note, we give a counterexample to a recent conjecture
of Gilmer which would have implied the union-closed conjecture.

1 Introduction

We say a family F of sets is union-closed if A ∪ B ∈ F whenever A, B ∈ F .
The celebrated Union-Closed conjecture of Frankl states that if n ∈ N and
F ̸= {∅} is a union-closed family of subsets of {1, 2, . . . , n}, then there exists
i ∈ {1, 2, . . . , n} such that at least half of the sets in F contain i. Gilmer [2]
recently obtained a breakthrough on this conjecture, proving that for any union-
closed family F of subsets of {1, 2, . . . , n} with F ̸= {∅}, there exists an element
i contained in at least 0.01|F | of the sets in F . (We refer the reader to the
survey of Bruhn and Schaudt [1] for survey of work prior to Gilmer’s, on the
problem.)
Gilmer’s proof is an elegant entropy argument. At the end of his paper,
Gilmer makes the following (information-theoretic) conjecture which would im-
mediately imply the union-closed conjecture.

Conjecture 1 (Gilmer). Let A, B be i.i.d. samples from a distribution over a
family of subsets of {1, 2, . . . , n}. Assume that Prob[i ∈ A] < 1
2 for all i, and
that H(A) > 0. Then
 H(A ∪ B) + D(A ∪ B||A) > H(A).

Here, H(A) denotes the entropy of A; recall that for a probability distribu-
tion p = (px)x∈X over a ﬁnite set X, the entropy of p is deﬁned by

H(p) = ∑

x∈X px log2(1/px).

∗School of Mathematics, University of Bristol, UK. Email: david.ellis@bristol.ac.uk

1

Also, D(q||p) denotes the Kullback-Leibler divergence of q from p, for probability
distributions (px)x∈X and (qx)x∈X over a ﬁnite set X; recall that this is deﬁned
by D(q||p) = ∑

x∈X qx log2(qx/px).

The purpose of this very short note is to give a (simple) counterexample to this
conjecture (with n = 2). Another counterexample (for large n) was indepen-
dently and simultaneously obtained by Sawin.

2 The counterexample

As usual, we write [n] := {1, 2, . . . , n}, and for a set S, we write P(S) for
the power-set of S. We ﬁrst note that, writing p for the distribution of A in
Gilmer’s conjecture, and q for the distribution of A ∪ B, the left-hand side of
the conjectured inequality is equal to
∑

x⊂[n] qx log2(1/qx) + ∑

x⊂[n] qx log2(qx/px) = ∑

x⊂[n] qx log2(1/px),

and therefore Gilmer’s conjecture is equivalent to
∑

x⊂[n] qx log2(1/px) − ∑

x⊂[n] px log2(1/px) > 0. (1)

We ﬁrst give a probability distribution p on P([2]) such that, if A and B are
i.i.d. samples from p, then Prob[1 ∈ A] = Prob[2 ∈ A] = 1
2 , but writing q for
the distribution of A ∪ B, the quantity on the left-hand side of (1) satisﬁes
∑

x⊂[n] qx log2(1/px) − ∑

x⊂[n] px log2(1/px) < −0.04. (2)

The distribution p is as follows:

p(∅) = p({1, 2}) = x, p({1}) = p({2}) = 1
2 − x, (3)

where (for concreteness) we take x = 0.3. (We use the variable x to make the
construction more readable.)
It remains to observe that an arbitrarily small perturbation (p′, say) of the
probability distribution p satisﬁes the hypotheses of Gilmer’s conjecture and yet
also has the above quantity (2) being negative; indeed, we may replace p by the
distribution p′ deﬁned by

p′(∅) = x, p′({1, 2}) = x − 2ǫ, p′({1}) = p′({2}) = 1
2 + ǫ − x,

for ǫ a suﬃciently small positive number.
We now check that we do indeed have
∑

x⊂[2] qx log2(1/px) − ∑

x⊂[2] px log2(1/px) < −0.04,

2

for the probability distribution p deﬁned in (3) above. Indeed, we have

q∅ = Prob[A = B = ∅] = x
2,

and

q{1} = Prob[A = ∅ and B = {1}] + Prob[A = {1} and B = ∅] + Prob[A = B = {1}]

= 2x( 1
2 − x) + ( 1
2 − x)
2

= x − 2x
2 + 1
4 − x + x
2

= 1
4 − x
2,

and by symmetry q{2} = q{1} = 1
4 − x
2. Since q is a probability distribution, we
have q{1,2} = 1 − q∅ − q{1} − q{2} = 1 − x
2 − 2( 1
4 − x
2) = 1
2 + x
2.

Substituting in the above values, we have
∑

x⊂[2] qx log2(1/px) − ∑

x⊂[2] px log2(1/px)

= ( 1
2 + 2x
2 − 2x) log2(1/x) + (− 1
2 − 2x
2 + 2x) log2(1/( 1
2 − x)),

which is indeed less than -0.04 when x = 0.3, as claimed.

References

[1] H. Bruhn and O. Schaudt. The journey of the union-closed sets conjecture.
Graphs and Combinatorics, 31(6):2043—2074, 2015.

[2] J. Gilmer. A constant lower bound for the union-closed sets conjecture.
Preprint. arXiv:2211.09055.
 3
