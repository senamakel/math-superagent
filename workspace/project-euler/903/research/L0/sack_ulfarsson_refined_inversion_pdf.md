> **Excerpt only — read this first.** The complete text is one level down at `research/L0/sack_ulfarsson_refined_inversion_pdf.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1106.1995 | converted from PDF -->

arXiv:1106.1995v2  [math.CO]  12 Jan 2012
REFINED INVERSION STATISTICS ON PERMUTATIONS

JOSHUA SACK AND HENNING ´ULFARSSON

Abstract. We introduce and study new reﬁnements of inversion sta-
tistics for permutations, such as k-step inversions, (the number of in-
versions with ﬁxed position diﬀerences) and non-inversion sums (the
sum of the diﬀerences of positions of the non-inversions of a permuta-
tion). We also provide a distribution function for non-inversion sums,
a distribution function for k-step inversions that relates to the Euler-
ian polynomials, and special cases of distribution functions for other
statistics we introduce, such as (≤ k)-step inversions and (k1, k2)-step
inversions (that ﬁx the value separation as well as the position). We
connect our reﬁnements to other work, such as inversion tops that are
0 modulo a ﬁxed integer d, left boundary sums of paths, and marked
meshed patterns. Finally, we use non-inversion sums to show that for
every number n > 34, there is a permutation such that the dot product
of that permutation and the identity permutation (of the same length)
is n.
 Contents

1. Introduction 1
2. Non-inversion sums and the dot product of permutations 3
3. Zone-crossing vectors and the distribution of the non-inversion
sum 9
4. The distribution of k-, (k1, k2)-, and (≤ k)-step inversions 14
5. Future work and connections with other work 20
References 27

1. Introduction

The main object of study in this paper is the set of inversions in a permu-
tation.
1 An inversion in a permutation π, of rank n, is a pair (a, b) satisfying
1 ≤ a < b ≤ n and π(a) > π(b). All other pairs are called non-inversions.
We are particularly interested in permutation statistics related to inversions,
such as the number of inversions of a certain form. The study of permutation
statistics was largely initiated by the seminal MacMahon [6], but has seen

Date: Updated: October 29, 2018.
Sack was partly supported by grant no. 100048021 from the Icelandic Research Fund.
´Ulfarsson was supported by grant no. 090038011 from the Icelandic Research Fund.
1We provide basic deﬁnitions at the end of this introduction.

2 SACK AND ´ULFARSSON

explosive growth in recent decades. In Section 2 we introduce the concept of
the non-inversion sum of a permutation. This is the sum of the diﬀerences
b − a for all non-inversions (a, b) in the permutation. Before studying the
distribution of this statistic we connect these non-inversion sums to another
known statistic on permutations: the dot product with a ﬁxed vector. In
particular, the dot product of the permutation (treated as a vector) with
the identity permutation of the same length is equal to the non-inversion
sum of the permutation plus a function of the rank of the permutation; see
Theorem 2.5.
In Section 3, we deﬁne the distribution function for the non-inversion sum
and prove a recurrence relation for it in Theorem 3.8. We introduce the
concept of a zone-crossing vector, which appears in the recurrence relations.
This is a vector whose kth coordinate is the number of non-inversions (a, b)
such that a ≤ k < b. We relate these vectors to the non-inversion sums
and show that there is a bijective correspondence between permutations
and their zone-crossing vectors. We also prove a theorem showing that the
distribution of the coordinates of these vectors is related to the q-analog of
the binomial coeﬃcients; see Theorem 3.7.
In Section 4 we consider k-step inversions, which are inversions (a, b)
such that b − a = k, and show in Theorem 4.4 that the distribution of these
types of inversions is related to the Eulerian polynomials. We next consider
(k1, k2)-step inversions, which are inversions (a, b), such that b − a = k1 and
π(b) − π(a) = k2, and prove a special case of the distribution function; see
Proposition 4.6. We also consider inversions (a, b) such that b − a ≤ k and

*[excerpt ends; 52553 characters not shown — see `research/L0/sack_ulfarsson_refined_inversion_pdf.full.md`]*
