> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/sudakov-verstraete-cycles-sparse-graphs-II.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1010.5309 | converted from PDF -->

## What it claims

The independence ratio of a graph G is deﬁned by

ι(G) := sup
X⊂V (G)
 |X|
α(X) ,

where α(X) is the independence number of the subgraph of G induced by X. The independence
ratio is a relaxation of the chromatic number χ(G) in the sense that χ(G) ≥ ι(G) for every graph G,
while for many natural classes of graphs these quantities are almost equal. In this paper, we address
two old conjectures of Erd˝os on cycles in graphs with large chromatic number and a conjecture of
Erd˝os and Hajnal on graphs with inﬁnite chromatic number.

1 Introduction

Let G be a graph and let α(X) be the size of a largest independent set in the subgraph of G induced
by X. The independence ratio of a graph G is deﬁned by

ι(G) := sup
X⊂V (G)
 |X|
α(X) .

The independence ratio of a graph G is a relaxation of the chromatic number χ(G), since χ(G) ≥ ι(G)
for all graphs G. For many interesting classes of graphs, including random and pseudorandom graphs,
the chromatic number and independence ratio are equal or almost equal. On the other hand, so-called
Kneser graphs are examples of graphs on n vertices with…

1.1…

## Statements it makes

Theorem 1 Every triangle-free graph with independence ratio at least k ≥ 3 has cycles of Ω(k2 log k)
consecutive lengths.

Theorem 1 is part of a more general theorem on hereditary properties – families of graphs closed under
taking induced subgraphs. To describe the general theorem, let P be a hereditary property and let
f : [1, ∞) → [1, ∞) be an increasing bijection. Then we say that P has speed at most f if for every
n ∈ N and every n-vertex graph G ∈ P , we have ι(G) ≤ f (n). Since the identity function f (x) = x
for x ∈ [1, ∞) serves as an upper bound for the speed of every hereditary property, the speed of each
hereditary property is well-deﬁned. We shall prove the following theorem:

Theorem 2 Let f : [1, ∞) → [1, ∞) be an increasing bijection. If P is a hereditary property with
speed at most f , then any graph G ∈ P with ι(G) > 18k + 4 has cycles of at least 1
2 f −1(k) consecutive
lengths.

Theorem 3 Let G be a Ks+1-free graph and suppose ι(G) > 18k + 4. Then G contains cycles of at
least 1
2 (k/s)s/(s−1) consecutive lengths.

Theorem 4 Let σ be an inﬁnite increasing sequence of positive integers satisfying σ1 ≥ 3 and log σr ≤
σr−1 for all r ≥ 2. If G is an n-vertex graph and

Theorem 4 is proved in Section 3. We claimed that an n-vertex graph G with ι(G) ≥ 3 exp(8 log∗n)
contains a cycle of length a prime. Let pr denote the rth prime number. Then Bertrand’s Postulate
gives pr+1 ≤ 2pr for all r ∈ N, and so log pr+1 ≤ log pr + 1 ≤ pr for all r ∈ N. Applying Theorem 4 to
this sequence, we see that a graph G with ι(G) > 3 exp(8 log∗n) contains a cycle of length a prime, as
claimed. Theorem 4 gives a similar upper bound for much sparser sequences, such as powers of three,
or 2 + 1, 22 + 1, 222 + 1, . . . and so on.

Theorem 5 For any graph G on n vertices,

Lemma 1 Let k ≥ 1. Then every n-vertex graph G with α(G) < n/(k + 1) has an induced subgraph
that is k-expanding on independent sets and a 2-connected subgraph that is weakly k-expanding on
independent sets.

Lemma 2 For n ≥ e15, every n-vertex triangle-free graph G has

Lemma 3 If G is an n-vertex triangle-free graph with α(G) < n/(3k + 1) and k ≥ e15, then G
contains a 2-connected subgraph H that is weakly 2-expanding on sets of size at most k2 log k and
weakly 3k-expanding on independent sets.
 5

Proposition 1 Let T ≥ 1, and let G be a graph that is 2-expanding on sets of size at most T . Then
for any longest path P ⊂ G there is a cycle C ⊂ H of length at least 3T containing S(P ) ∪ ∂S(P ).

Proposition 2 Let T ≥ 1, and let G be a graph that is weakly 2-expanding on sets of size at most
T . Then there exists a longest path P ⊂ G and a cycle C ⊂ H of length at least 3T containing
S(P ) ∪ ∂S(P ).

Theorem 6 Let G be a triangle-free graph with ι(G) > 3k + 1 where k ≥ e15. Then G has a cycle of
length at least 3k2 log k.

Proposition 3 Let k ≥ e15 and let G be an n-vertex triangle-free…

Pr…


*[further statements in the full text]*

*[digest of a 38816 character source; every section, statement, and proof in full at `research/sources/sudakov-verstraete-cycles-sparse-graphs-II.full.md`]*
