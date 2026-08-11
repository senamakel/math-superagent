> **Excerpt only — read this first.** The complete text is beside it at `research/leanos_mth_roots_of_permutations.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, and specific enough that nobody needs the full text.

<!-- source: https://arxiv.org/pdf/1005.1531 | converted from PDF -->

arXiv:1005.1531v4  [math.CO]  12 Sep 2011On the number of mth roots of
permutations

Jes´us Lea˜nos, Rutilo Moreno and Luis M. Rivera-Mart´ınez

Abstract

Let m be a ﬁxed positive integer. It is well-known that a permutation σ of

{1, ..., n} may have one, many, or no mth roots. In this article we provide an

explicit expression and a generating function for the number of mth roots of σ. Let

pm(n) be the probability that a random n-permutation has an mth root. We also

include a proof of the fact that pm(jq) = pm(jq + 1) = · · · = pm(jq + (q − 1)),

j = 0, 1, ..., when m is a power of prime number q.

1 Introduction and main results

Let Sn be the group of all permutations of the ﬁnite set [n] = {1, ..., n}. Let m be a ﬁxed

positive integer. We say that σ ∈ Sn has an mth root or that σ is an mth power if there
exists a permutation τ ∈ Sn with τ m = σ. For ﬁxed m, not all permutations have an

mth root ([15], Theorem 4.8.2), however, L. Glebsky and L. M. Rivera [7] have proved
that for suﬃciently large n, any permutation has an “almost” mth root (in the sense
of the Hamming distance [6]). Now, if we know that a permutation σ has at least one

mth root, how many mth roots can σ have? We can ﬁnd an explicit expression for this
quantity in the paper of A. I. Pavlov [10]. Also, in the article of S. Annin, T. Jansen and

C. Smith [1], appeared a classiﬁcation of the elements in Sn and An that has mth roots,
and they propose some problems related with the roots of permutations. In particular,
our work is about some questions on Problem 1 in Section 4 of [1].

2000 Mathematics Subject Classiﬁcation: 05A05, 05A15.
Key words and phrases: Permutations, mth roots, Enumeration.
Rivera-Mart´ınez was partially supported by PROMEP (SEP), grant UAZ-PTC-103.

1

The main results of this paper are an explicit expression for the number of mth roots
of any n-permutation σ (Theorem 1) and a generating function for this number (Theo-

rem 2). In order to obtain our expression we deﬁne some sets of non-negative integers
that seem interesting by themselves (see Section 2). In particular, such sets provide a
simpler expression than the corresponding expression in [10]. Moreover, this new expres-

sion allows us to compute the number of mth roots of a permutation in an eﬀective way
using a computer algebra system.

Another classical problem consists in estimating the number of permutations in Sn
that admit an mth root. P. Tur´an [14] gave an upper bound when m is a prime number
and Blum [2] gave an asymptotic formula for the case m = 2. Recently, M. B´ona, A.

McLennan and D. White [4] proved that the probability that a random permutation of
length n has an mth root with m prime, is monotonically non-increasing in n. See also

the work of N. Pouyanne [12] for an asymptotic study for any positive integer m and the
work of B. Bollob´as and B. Pittel [3] who continued the work of N. Pouyanne and studied
the limiting distribution of the root degree of a permutation. This problem can be easily

reformulated as the problem about the probability, pm(n), that a n-permutation chosen
uniformly at random has an mth root. For this problem, we give a proof of the fact that
when m is a power of a prime q, for all j ≥ 0, pm(jq) = pm(jq +1) = · · · = pm(jq +(q −1)).

For the case m a prime, see the paper of M. B´ona, et al. [4] that includes a combinatorial
proof of the equivalent equalities. It is also recommended the paper of A. Mar´oti [9] and

the bibliography therein for related results about the proportion of ℓ-regular elements in
the symmetric group Sn. Another interesting article is due to M. R. Pournaki [11], who
worked in the problem of determining the number of even permutations with roots.

Before stating our main results, we shall give some notation and deﬁnitions. As usual,
we denote by N (respectively N0) the set of positive (respectively, non-negative) integers.


*[excerpt ends; 24578 characters not shown — see `research/leanos_mth_roots_of_permutations.full.md`]*
