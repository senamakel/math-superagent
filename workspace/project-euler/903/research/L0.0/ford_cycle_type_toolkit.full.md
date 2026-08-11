# Ford, "Cycle type of random permutations: A toolkit" (arXiv:2104.12019v3; Discrete Analysis 2022:9)

Full text (ar5iv HTML) of Kevin Ford's toolkit. URL: https://ar5iv.labs.arxiv.org/html/2104.12019. Published: Discrete Analysis 2022:9, DOI 10.19086/da.38090. Summary/queries answered: [[ford_cycle_type_toolkit]] (L1).

## What it establishes (statements)

- Unit of study: cycle counts C_k(σ) of a uniform random σ ∈ S_n; §1-2 develop the Poisson(1/k) heuristic with exact combinatorics.
- Exact factorial moments: E[∏_k (C_k)_{r_k}] = ∏_k k^{−r_k} for Σ_k k·r_k ≤ n (falling-factorial notation). The basis for all exact cycle-type sums.
- Fixed points: C_1 → Poisson(1), explicit error; largest/smallest cycle; cycles with lengths in arbitrary sets I — sieve upper/lower bounds and Poisson/CLT when Σ_{k∈I} 1/k grows.
- Bibliography maps the order-of-permutation distribution literature (Erdős–Turán, Goh–Schmutz, and refs [1,7,10,13,22–28,38,50,57,61–63]).

## Implications for Q(n)

The A_n, B_n sums (fixed-point-count averages of gap-affine pair-inversion probabilities from [[conjugacy_class_statistics_body]] and [[pinsky_schickentanz_ewens_html]]) are cycle-type sums; Ford gives the exact summation identities and the asymptotic replacement scheme at n = 10⁶. Also the literature router for the n!/ord(π) weights used in brute2.

###### Abstract

We provide a standard reference for fundamental distributional results about the cycle type of a random permutation σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n}, emphasizing methods which are combinatorial or probabilistic in nature and adaptable to other situations. Many of our techniques are borrowed from methods used to prove analogous theorems about the prime factorization of random integers. Included here are results about the proportion of permutations σ \sigma having a given number of cycles with lengths from a given set, the distribution of the smallest and largest cycle, and the distribution of the sizes of fixed sets of σ \sigma.

† † daj-author-details: title = Cycle Type of Random Permutations:
a Toolkit, author = Kevin Ford, plaintextauthor = Kevin Ford, keywords = random permutations, cycle type, , † † daj-editor-details: year=2022, number=9, received=10 May 2021, revised=18 February 2022, published=8 September 2022, doi=10.19086/da.38090,

## 1 Introduction

The theory of the cycle type of random permutations of the symmetric group 𝒮 n \mathcal{S}_{n} is very active, with many applications in combinatorics, group theory and number theory. A selection of applications includes

- •

the distribution of orders of permutations (the least common multiple of cycle lengths) [1, 7, 10, 13, 22, 23, 24, 25, 26, 27, 28, 38, 50, 57, 61, 62, 63] and [40, Sec. 6];

- •

invariable generation of the symmetric group [16, 18, 53, 67] and other classical groups [59];

- •

the distribution of fixed sets (divisors) of permutations [14, 17, 18, 19, 33, 53, 73];

- •

permutations contained in transitive subgroups [12, 19, 45];

- •

irreducibility of polynomials over the rationals [8, 9];

- •

permutation groups containing elements with a single cycle that is not a fixed point (Jordan groups) [45, 37] and [69, Ch. 10];

- •

polynomial factorization in finite fields [3, 8, 68].

The main purpose of this paper is provide a standard reference for fundamental distributional results about cycle types, which heretofore have been scattered across many papers with widely varying strength and generality. We showcase methods which are both *general*and *combinatorial*. While many of the results stated here are weaker than existing results in the literature, they are far more general, have significantly shorter proofs and are more adaptable to new situations. This paper is an expanded version of portions of the author’s lecture notes on permutations prepared for the course “Anatomy of integers and random permutations”.

Our methods are borrowed from the theory of numbers, particularly the theory of sieves and the theory of averages of multiplicative functions (see [48, Part 3, Part 4] for uses in number theory). As positive integers factor uniquely into a product of prime numbers, and permutations factor uniquely into a product of cycles, the connection between the distributions of the two objects, prime factors and cycles, is not surprising. The first explicit mention of such a connection, however, is the paper of Knuth and Trabb Pardo [46] in 1976. On the other hand, there are significant differences in the structure of the two objects which explains why there is no simple *transference principle*between statements about prime factorizations and the corresponding statement about the cycle structure of permutations. Deeper inspection, however, reveals that the *distribution*of the two factorizations have many common features, and for much the same underlying reasons.


*[excerpt ends; 111181 characters not shown — see `research/L0/ford_cycle_type_toolkit.full.full.md`]*
