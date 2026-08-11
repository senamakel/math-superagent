> **Excerpt only.** The full converted text is archived at `raw/goswick_0806.3943.md` and is not loaded into any agent's context. Replace this file with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, and specific enough that nobody needs the original.

<!-- source: https://arxiv.org/pdf/0806.3943 | converted from PDF -->

arXiv:0806.3943v2  [math.NT]  10 Aug 2011
SUMS OF SQUARES AND ORTHOGONAL INTEGRAL VECTORS

LEE M. GOSWICK, EMIL W. KISS, G ´ABOR MOUSSONG, N ´ANDOR SIM ´ANYI

Abstract. Two vectors in Z
3 are called twins if they are orthogonal and have
the same length. The paper describes twin pairs using cubic lattices, and counts
the number of twin pairs with a given length. Integers M with the property that
each integral vector with length √
M has a twin are called twin-complete. They are
completely characterized modulo a famous conjecture in number theory. The main
tool is the decomposition theory of Hurwitz integral quaternions. Throughout the
paper we made a concerted eﬀort to keep the exposition as elementary as possible.

1. Introduction and main results

An icube in Z
n of dimension k is a sequence (v1, . . . , vk) of k nonzero vectors in Zn

that are pairwise orthogonal and have the same length. The subgroup generated
by v1, . . . , vk is called the corresponding cubic lattice. The common length of the
vectors vi is denoted by ∥vi∥, and is called the edge length of the icube. By the norm
of vi we shall mean N(vi) = ∥vi∥2 (a similar convention is used also for Gaussian
integers and quaternions). A twin pair is a 2-dimensional icube in Z
3.
In this paper we investigate how icubes can be constructed, counted, and extended.
We shall consider the case n = 3. The main results are the following.
• Theorem 5.10 counts all twin pairs with a given edge length.
• Proposition 1.3 and Corollary 5.11 show that a twin pair can be extended to
a 3-dimensional icube if and only if its edge length is an integer.
• Theorem 1.5 and Corollary 1.6 investigate the existence and uniqueness of
3-dimensional cubic lattices containing a single integral vector and the exten-
sion of single vectors to twins.
• Theorem 1.8 and Corollary 1.10 characterize twin-complete numbers.
• The above results are based on the following representation theorems:
k = 1 : Theorem 4.2 and Theorem 4.6;
k = 2 : Theorem 5.4;
k = 3 : Theorem 3.3 and Corollary 3.9.

1991 Mathematics Subject Classiﬁcation. 11R52, 52C07.
Key words and phrases. Cubic lattice, Euler rotation matrix, Hurwitz integral quaternion.
Second author supported by Hungarian Nat. Sci. Found. (OTKA) Grant No. NK72523, third
author supported by Hungarian Nat. Sci. Found. (OTKA) Grant No. T047102, fourth author sup-
ported by the National Science Foundation, grants DMS-0457168 and DMS-0800538.
1

2 LEE M. GOSWICK, EMIL W. KISS, G ´ABOR MOUSSONG, N ´ANDOR SIM ´ANYI

In the rest of the Introduction, we put these results into context.
The problem of construction and counting for 3-dimensional icubes in Z
3 has been
solved by A. S´ark¨ozy [Sar61]. To formulate his main result, we use a construction
discovered by Euler. The following well-known facts show how to obtain rotations
in R3. Throughout the paper we identify v = (v1, v2, v3) ∈ R3 with the pure quater-
nion V (v) = v1i + v2j + v3k.

Theorem 1.1 (see [CS03], Section 3). Let H∗ = H \{0} denote the set of nonzero
quaternions, and V the space of all quaternions with zero real part. For α ∈ H
∗,
let M(α) denote the matrix of the transformation α( · )α−1 : V → V expressed
in the standard basis (i, j, k). Then there exists a surjective linear representation
ρ : H
∗ → SO(3, R) such that
(1) ker(ρ) = R∗.
(2) The matrix of ρ(α) in the standard basis (i, j, k) is

M(α) = 1
d
 


m
2 + n
2 − p2 − q2 −2mq + 2np 2mp + 2nq
2mq + 2np m
2 − n
2 + p2 − q2 −2mn + 2pq
−2mp + 2nq 2mn + 2pq m
2 − n
2 − p2 + q2


 ,

where α = m + ni + pj + qk and d = m
2 + n
2 + p2 + q2. We note that the restriction
of the representation ρ to the unit sphere S3 of H is the adjoint representation of S3

with the kernel {1, −1}, being also the universal covering of the real projective space
SO(3, R).

In what follows, we shall concern ourselves with the Euler matrix E(α) = dM(α).

*[excerpt ends; 56532 characters not shown]*
