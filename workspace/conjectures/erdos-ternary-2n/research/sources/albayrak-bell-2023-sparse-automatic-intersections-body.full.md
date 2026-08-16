<!-- source: https://ar5iv.labs.arxiv.org/html/2304.09223 | converted from HTML -->

[2304.09223] Quantitative estimates for the size of an intersection of sparse automatic sets

# Quantitative estimates for the size of an intersection of sparse automatic sets Thanks: The first-named author’s postdoctoral appointment at the University of Calgary was partially supported by NSERC grant RGPIN-2018-03770 and CRC tier-2 research stipend 950-231716. Thanks: The second-named author was supported by NSERC grant RGPIN-2022-02951.

Seda Albayrak Address: Department of Mathematics and Statistics, University of Calgary, Calgary, AB Canada T2N 1N4 Email address: [gulizar.albayrak@ucalgary.ca][1] and Jason P. Bell Address: Department of Pure Mathematics, University of Waterloo, Waterloo, ON Canada N2L 3G1 Email address: [jpbell@uwaterloo.ca][2]

###### Abstract.

A theorem of Cobham says that if k k and ℓ \ell are two multiplicatively independent natural numbers then a subset of the natural numbers that is both k k - and ℓ \ell -automatic is eventually periodic. A multidimensional extension was later given by Semenov. In this paper, we give a quantitative version of the Cobham-Semenov theorem for sparse automatic sets, showing that the intersection of a sparse k k -automatic subset of ℕ d \mathbb{N}^{d} and a sparse ℓ \ell -automatic subset of ℕ d \mathbb{N}^{d} is finite with size that can be explicitly bounded in terms of data from the automata that accept these sets.

###### Key words and phrases:

Automatic sets, Cobham’s theorem, sparse sets, independent bases

###### 2020 Mathematics Subject Classification

Primary 68Q45; Secondary 11B85

## 1. Introduction

Let k k be a natural number that is greater than or equal to 2 2. A subset S S of ℕ \mathbb{N} is k k -*automatic*if there is a deterministic finite automaton with input alphabet Σ k = { 0, 1, …, k − 1 } \Sigma_{k}=\{0,1,\ldots,k-1\} with the property that the words over the alphabet Σ k \Sigma_{k} which are accepted by the automaton (where we read words right-to-left) are precisely the words that are base- k k expansions of elements of S S. One can naturally extend this notion of automaticity to subsets of ℕ d \mathbb{N}^{d} with d ≥ 1 d\geq 1, by now working with the input alphabet ( Σ k) d (\Sigma_{k})^{d}. Then, given a d d -tuple ( n 1, …, n d) (n_{1},\ldots,n_{d}) of natural numbers—after possibly padding some words with 0 0 at the beginning—we see there exist words w 1, …, w d w_{1},\ldots,w_{d} of the same length with the additional property that w i w_{i} is a base- k k expansion of n i n_{i} for i = 1, …, d i=1,\ldots,d (base- k k expansions are unique up to some number of leading zeros) and where at least one w i w_{i} has no leading zeros. Then a subset of ℕ d \mathbb{N}^{d} is k k -automatic if there is a finite-state machine with input alphabet ( Σ k) d (\Sigma_{k})^{d} that accepts precisely the words ( w 1, …, w d) (w_{1},\ldots,w_{d}) corresponding to d d -tuples of natural numbers in S S. We refer the reader to the book of Allouche and Shallit [4] for further background on automata and automatic sets, and we assume that the reader has some familiarity with deterministic finite-state automata.

As an example, observe that the deterministic finite-state automaton in Figure 1 with input alphabet Σ 2 = { 0, 1 } \Sigma_{2}=\{0,1\} accepts the set of words corresponding to binary expansions of elements of the 2 2 -automatic set { 3 ⋅ 2 n + 1: n ≥ 1 } \{3\cdot 2^{n}+1\colon n\geq 1\}, where we adopt the usual convention of using doubly circled states to denote accepting states of a finite-state automaton.

q 0 q_{0} start q 1 q_{1} q 2 q_{2} q 3 q_{3} q 4 q_{4} 0 1 0 1 0 1 0,1 0,1 Figure 1. The finite-state machine generating the set { 3 ⋅ 2 n + 1: n ≥ 1 } \{3\cdot 2^{n}+1\colon n\geq 1\}.

A celebrated result of Cobham [10] shows that if k k and ℓ \ell are two multiplicatively independent natural numbers greater than one (i.e., there are no solutions to the equation k a = ℓ b k^{a}=\ell^{b} with nonzero integers a a and b b) and S ⊆ ℕ S\subseteq\mathbb{N} is a set that is both k k - and ℓ \ell -automatic then S S is in fact eventually periodic; i.e., there is some fixed positive integer c c such that for sufficiently large n ∈ ℕ n\in\mathbb{N}, n ∈ S n\in S implies n + c ∈ S n+c\in S. A multidimensional version of Cobham’s theorem was later given by Semenov [30] (see also [25]), who showed that a subset of ℕ d \mathbb{N}^{d} that is both k k - and ℓ \ell -automatic, with k k and ℓ \ell multiplicatively independent, is a semilinear set (equivalently, a set that is definable in Presburger arithmetic or a set that is automatic with respect to all positive integer bases).

In recent years there have been new proofs and extensions of Cobham’s theorem to other settings [1, 2, 6, 12, 13, 20, 24, 28] (see also the survey chapter by Durand and Rigo [14]). One particularly interesting extension is recent work of Hieronymi and Schulz [20], which shows that if one takes Presburger arithmetic and adds a k k -automatic predicate X X and an ℓ \ell -automatic predicate Y Y, with k k and ℓ \ell multiplicatively independent, then the resulting structure has an undecidable first-order theory unless one of the two sets is already Presburger definable. Taking X X equal to Y Y, one immediately deduces Cobham’s theorem. In light of this work, it is a natural question to look at the intersection of a k k -automatic set and an ℓ \ell -automatic set and to ask to what extent the intersection can be described.

In general, this question is intractable and many Diophantine questions that lie beyond the scope of currently available methods in number theory can be encoded within this framework. For example, Erdős [15, p. 67] famously conjectured that the set of powers of two (which is 2 2 -automatic) and the 3 3 -automatic set consisting of numbers whose ternary expansions omit 2 2 has finite intersection, saying “*as far as I can see, there is no method at our disposal to attack this conjecture.*”

Within the theory of automatic sets, however, there is a well-known dichotomy: if S S is an automatic subset of the natural numbers, then either there is some natural number d d such that S S has O ⁡ ( ( log ⁡ n) d) {O}((\log n)^{d}) elements of size at most n n or there is a positive number α \alpha such that S S has at least n α n^{\alpha} elements of size at most n n for all sufficiently large n n (see, for example, [18, §2.3] or [9, Proposition 7.1]). An automatic set for which the polylogarithmic bound holds is called *sparse*, and this notion again naturally extends to the multidimensional setting. Sparse automatic sets have arisen naturally in many unrelated contexts [3, 8, 11, 22, 23, 27] and form an important subclass of the more general collection of automatic sets.

As an example, the set constructed in Figure 1 is a sparse 2 2 -automatic set, as there are O ⁡ ( n) O(n) elements of size less than 2 n 2^{n}. We refer the reader to § 2 for more background on sparse sets.

In this paper, we restrict our focus to the problem of giving a description of the intersection of two sparse automatic subsets of ℕ d \mathbb{N}^{d} that are automatic with respect to two multiplicatively independent bases. This setting—while more restrictive than the general setting in which one studies the possible forms an intersection of two automatic sets can take—still captures many interesting number theoretic questions. Notably, Catalan’s conjecture (now a theorem of Mihăilescu [26]) asserts that the intersection of the sparse 2 2 -automatic set { 2 n + 1: n ≥ 0 } \{2^{n}+1\colon n\geq 0\} with the sparse 3 3 -automatic set { 3 m: m ∈ ℕ } \{3^{m}\colon m\in\mathbb{N}\} consists only of the numbers 3 3 and 9 9. We give the following general finiteness result.

###### Theorem 1.1.

Let k k and ℓ \ell be multiplicatively independent natural numbers greater than or equal to 2 2 and let d d be a positive integer. If X X is a sparse k k -automatic subset of ℕ d \mathbb{N}^{d} and Y Y is a sparse ℓ \ell -automatic set of ℕ d \mathbb{N}^{d}, then X ∩ Y X\cap Y is finite and there is an effectively computable upper bound for the size of the intersection in terms of d, k, ℓ d,k,\ell and data from the minimal automata that accept these sets.

As in the work of Hieronymi and Schulz [20], if we take X = Y X=Y, we see that a subset of ℕ d \mathbb{N}^{d} that is a sparse automatic set with respect to two multiplicatively independent bases is necessarily finite, and so in this sense one can view our main result as a quantitative extension of the sparse case of the Cobham-Semenov theorem.

For Theorem 1.1, we in fact give a closed form for upper bounds in terms of just d d, k k, ℓ \ell, and the number of states in the minimal automata accepting X X and Y Y (see Theorem 4.1 for explicit bounds; we note that our bounds are not optimized but are rather expressed in a clean form). One might ask whether one can decide whether the intersection is empty or even whether one can effectively determine the intersection. Both of these problems are apparently very difficult and connected to highly non-trivial Diophantine questions that are not known to be decidable at this time.

The outline of this paper is as follows. In § 2, we give a brief overview of sparse languages and sparse sets. In § 3, we give a brief overview of S S -unit theory and state the key result we will be using in proving our main theorem. In § 4 we prove a precise version of Theorem 1.1. Finally, we pose a general conjecture about the form of intersections of sparse k k -automatic sets with zero-density ℓ \ell -automatic sets in § 5.

### 1.1. Notation

Throughout this paper, given an alphabet Σ \Sigma, we let Σ ∗ \Sigma^{*} denote the free monoid consisting of all finite words over the alphabet Σ \Sigma. When Σ = { u } \Sigma=\{u\} is a singleton, we write u ∗ u^{*} rather than { u } ∗ \{u\}^{*} for Σ ∗ \Sigma^{*}. For an integer k ≥ 2 k\geq 2, we take Σ k = { 0, …, k − 1 } \Sigma_{k}=\{0,\ldots,k-1\}, and we let

 | [⋅] k: ( Σ k d) ∗ → ℕ d [\,\cdot\,]_{k}:\left(\Sigma_{k}^{d}\right)^{*}\to\mathbb{N}^{d} |  |

denote the map that takes a d d -tuple of words (here the value of d d depends on the context and for much of the paper we take d = 1 d=1) and outputs the d d -tuple of natural numbers formed by taking the base- k k expansions of these words. So, for example, [( 2110, 0020)] 3 = ( 66, 6) [(2110,0020)]_{3}=(66,6). In general, we assume that at least one of the words in our d d -tuple has no leading zeros so that d d -tuples of natural numbers have unique base- k k expansions.

We also make use of deterministic finite automata (DFAs) throughout this paper. We represent a DFA using a 5 5 -tuple ( Q, Σ, δ, q 0, F) (Q,\Sigma,\delta,q_{0},F), where Q Q is a non-empty finite set of states, Σ \Sigma is a finite input alphabet, δ: Q × Σ → Q \delta:Q\times\Sigma\to Q is the transition function, q 0 ∈ Q q_{0}\in Q is the initial state, and F ⊆ Q F\subseteq Q is the set of accepting states. We note that δ \delta can be extended inductively as a map from Q × Σ ∗ → Q Q\times\Sigma^{*}\to Q by declaring that δ ⁡ ( q, x ​ w) = δ ⁡ ( δ ⁡ ( q, x), w) \delta(q,xw)=\delta(\delta(q,x),w) for all w ∈ Σ ∗ w\in\Sigma^{*} and x ∈ Σ x\in\Sigma.

## 2. Sparse automatic sets

In this section we give a brief summary of sparse languages and sparse sets. Sparse automatic sets and related concepts have been studied by many authors (see, for example, [18] and references therein).

Given a finite alphabet Σ \Sigma and a language ℒ ⊆ Σ ∗ \mathcal{L}\subseteq\Sigma^{*} over Σ \Sigma, we have an associated counting function

 | f ℒ ​ ( n):= | { w ∈ ℒ: length ⁡ ( w) ≤ n } |. f_{\mathcal{L}}(n):=\left|\{w\in\mathcal{L}\colon{\rm length}(w)\leq n\}\right|. |  |

A regular language ℒ \mathcal{L} is *sparse*if f ℒ ​ ( n) = O ⁡ ( n d) f_{\mathcal{L}}(n)=O(n^{d}) for some natural number d d.

There is a precise characterization of sparse regular languages, which has been obtained by several authors and is recorded in [9, Proposition 7.1].

###### Proposition 2.1.

Let ℒ \mathcal{L} be a regular language. The following are equivalent:

1. (1)

ℒ \mathcal{L} is sparse.

2. (2)

ℒ \mathcal{L} is a finite union of languages of the form v 1 ​ w 1 ∗ ​ v 2 ​ w 2 ∗ ​ … ​ v s ​ w s ∗ ​ v s + 1 v_{1}w_{1}^{*}v_{2}w_{2}^{*}\dots v_{s}w_{s}^{*}v_{s+1}, where s ≥ 0 s\geq 0, the v i v_{i} are possibly trivial words, and the w i w_{i} are non-trivial words over the alphabet { 0, 1, …, k − 1 } \{0,1,\ldots,k-1\}.

3. (3)

If Γ = ( Q, Σ, δ, q 0, F) \Gamma=(Q,\Sigma,\delta,q_{0},F) is a minimal finite automaton accepting ℒ \mathcal{L}. Then Γ \Gamma satisfies the following.

  - ( ∗ *)

If q q is a state such that δ ⁡ ( q, v) ∈ F \delta(q,v)\in F for some word v v then there is at most one non-trivial word w w with the property that δ ⁡ ( q, w) = q \delta(q,w)=q and δ ⁡ ( q, w ′) ≠ q \delta(q,w^{\prime})\neq q for every non-trivial proper prefix w ′ w^{\prime} of w w.

A k k -automatic subset S ⊆ ℕ d S\subseteq\mathbb{N}^{d} is then said to be *sparse*if the sublanguage of ( Σ k d) ∗ (\Sigma_{k}^{d})^{*} corresponding to base- k k expansions of elements of S S is a sparse regular language. Translating Proposition 2.1 into the framework of automatic sets, we see that a k k -automatic subset S ⊆ ℕ d S\subseteq\mathbb{N}^{d} is sparse if

(1) |  | π S ​ ( x) = | { ( n 1, …, n d) ∈ S: n 1 + n 2 + ⋯ + n d ≤ x } | = O ⁡ ( ( log ⁡ x) d) \pi_{S}(x)=\left|\{(n_{1},\ldots,n_{d})\in S\colon n_{1}+n_{2}+\cdots+n_{d}\leq x\}\right|={O}((\log\,x)^{d}) |  |

as x x tends to infinity. We note that if S S is not sparse, then there is some α > 0 \alpha>0 such that π S ​ ( x) > x α \pi_{S}(x)>x^{\alpha} for x x large (cf. [18, §2.3]), and so there is a natural gap separating sparse and non-sparse automatic subsets of ℕ d \mathbb{N}^{d}.

We will require the following description of special types of sparse sets, from which every sparse automatic subset of the natural numbers can be built by taking finite unions.

###### Proposition 2.2.

Let k ≥ 2 k\geq 2 be a natural number, let s s be a nonnegative integer and let v 0, v 1, …, v s, w 0, …, w s v_{0},v_{1},\ldots,v_{s},w_{0},\ldots,w_{s} be words in Σ k ∗ \Sigma_{k}^{*}. If

 | S = { [v 0 w 1 ∗ v 1 w 2 ∗ ⋯ v s − 1 w s ∗ v s] k } S=\{[v_{0}w_{1}^{*}v_{1}w_{2}^{*}\cdots v_{s-1}w_{s}^{*}v_{s}]_{k}\} |  |

then there exist c 0, …, c s ∈ ℚ c_{0},\ldots,c_{s}\in\mathbb{Q} and positive integers δ 1, …, δ s \delta_{1},\ldots,\delta_{s} such that

 | S = { c 0 + c 1 k δ s ​ n s + c 2 k δ s ​ n s + δ s − 1 ​ n s − 1 + ⋯ + c s k δ s ​ n s + ⋯ + δ 1 ​ n 1: n 1, …, n s ≥ 0 }. S=\left\{c_{0}+c_{1}k^{\delta_{s}n_{s}}+c_{2}k^{\delta_{s}n_{s}+\delta_{s-1}n_{s-1}}+\cdots+c_{s}k^{\delta_{s}n_{s}+\cdots+\delta_{1}n_{1}}\colon n_{1},\ldots,n_{s}\geq 0\right\}. |  |

###### Proof.

This result is due to Ginsburg and Spanier [19] (see also the proof of [3, Lemma 3.4]). ∎

## 3. Background on S S -unit equations

In this section we give an overview of the theory of S S -unit equations. Specifically, we require a quantitative version of a result due to Evertse, Schlickewei and Schmidt (see [17, Theorem 1.1] and also [16, Theorem 6.1.3]). We recall that for z 1, …, z n z_{1},\ldots,z_{n} in a field K K, the equation z 1 + ⋯ + z n = 1 z_{1}+\cdots+z_{n}=1 is said to be *non-degenerate*if no non-trivial subsum of the left-hand side is equal to zero; that is, whenever I I is a nonempty subset of { 1, …, n } \{1,\ldots,n\}, we have ∑ i ∈ I z i ≠ 0 \sum_{i\in I}z_{i}\neq 0.

The S S -unit theorem (see [16, Theorem 6.1.3]) is a hugely significant result in Diophantine approximation, which we state for the reader’s convenience.

###### Theorem 3.1.

Let K K be a field of characteristic zero, let a 1, …, a n a_{1},\dots,a_{n} be nonzero elements of K K, and let H ⊂ ( K ∗) n H\subset(K^{*})^{n} be a finitely generated multiplicative subgroup. Then there are only finitely many non-degenerate solutions ( x 1, …, x n) ∈ H (x_{1},\dots,x_{n})\in H to the equation

(2) |  | a 1 ​ x 1 + ⋯ + a n ​ x n = 1. a_{1}x_{1}+\cdots+a_{n}x_{n}=1. |  |

We will use a quantitative version of the S S -unit theorem. There are a number of quantitative versions (see for example [5, 16, 17, 29]), but we find the following version, due to Amoroso and Viada [5, Theorem 6.2], most convenient for our purposes. We note that Amoroso and Viada assume their fields are algebraically closed throughout, but for the statement given below this hypothesis is unnecessary since we can embed a field into its algebraic closure. We recall that a finitely generated abelian group is isomorphic to the direct sum of a finite group along with a group isomorphic to ℤ r \mathbb{Z}^{r} for some r ≥ 0 r\geq 0; the quantity r r is uniquely determined by the group and is called the *rank*of the group.

###### Theorem 3.2.

Let K K be a field of characteristic zero, let a 1, …, a n a_{1},\dots,a_{n} be nonzero elements of K K, and let Γ \Gamma be a finitely generated multiplicative subgroup of ( K ∗) n (K^{*})^{n} of rank r < ∞ r<\infty. Then there are at most

 | ( 8 ​ n) 4 ​ n 4 ​ ( n + r + 1) (8n)^{4n^{4}(n+r+1)} |  |

non-degenerate solutions to the equation

 | a 1 ​ x 1 + ⋯ + a n ​ x n = 1 a_{1}x_{1}+\cdots+a_{n}x_{n}=1 |  |

with ( x 1, …, x n) ∈ Γ (x_{1},\dots,x_{n})\in\Gamma.

We note that all versions of the S S -unit theorem are ineffective, except in the case when n ≤ 2 n\leq 2.

## 4. Proof of Theorem 1.1

In this section, we prove the following version of Theorem 1.1.

###### Theorem 4.1.

Let k k and ℓ \ell be multiplicatively independent positive integers, let d ≥ 2 d\geq 2, and let Γ = ( Q, Σ k d, δ, q 0, F) \Gamma=(Q,\Sigma_{k}^{d},\delta,q_{0},F) and Γ ′ = ( Q ′, Σ ℓ d, δ ′, q 0 ′, F ′) \Gamma^{\prime}=(Q^{\prime},\Sigma_{\ell}^{d},\delta^{\prime},q_{0}^{\prime},F^{\prime}) be deterministic finite-state automata accepting sparse regular languages ℒ ⊆ ( Σ k d) ∗ \mathcal{L}\subseteq(\Sigma_{k}^{d})^{*} and ℒ ′ ⊆ ( Σ ℓ d) ∗ \mathcal{L}^{\prime}\subseteq(\Sigma_{\ell}^{d})^{*}. If X ⊆ ℕ d X\subseteq\mathbb{N}^{d} is the set of d d -tuples of natural numbers whose base- k k expansions are elements of ℒ \mathcal{L} and Y ⊆ ℕ d Y\subseteq\mathbb{N}^{d} is the set of d d -tuples of natural numbers whose base- ℓ \ell expansions are elements of ℒ ′ \mathcal{L}^{\prime}, then

(3) |  | | X ∩ Y | ≤ k d ​ | Q | ⋅ ℓ d ​ | Q ′ | ⋅ ( 8 ​ ( | Q | + | Q ′ | − 1)) 10 ​ d ​ ( | Q | + | Q ′ |) 5. |X\cap Y|\leq k^{d|Q|}\cdot\ell^{d|Q^{\prime}|}\cdot\left(8(|Q|+|Q^{\prime}|-1)\right)^{10d(|Q|+|Q^{\prime}|)^{5}}. |  |

We note that we have not attempted to optimize the upper bounds, as to do so would lead to unwieldy expressions. Nevertheless, the bounds we obtain cannot be significantly improved using our methods. We begin with a basic estimate.

###### Proposition 4.2.

Let N ≥ 2 N\geq 2, let Σ \Sigma be a finite alphabet of size N N, and let Γ = ( Q, Σ, δ, q 0, F) \Gamma=(Q,\Sigma,\delta,q_{0},F) be a deterministic finite automaton accepting a sparse language ℒ \mathcal{L}. Then ℒ \mathcal{L} is a finite (possibly empty) union of at most

 | ( | Q | − 1)! ​ ( N | Q | − 1 + N | Q | − 2 + ⋯ + 1) (|Q|-1)!(N^{|Q|-1}+N^{|Q|-2}+\cdots+1) |  |

languages of the form

 | { v 0 w 1 ∗ v 1 w 2 ∗ ⋯ v s − 1 w s ∗ v s } \{v_{0}w_{1}^{*}v_{1}w_{2}^{*}\cdots v_{s-1}w_{s}^{*}v_{s}\} |  |

with w 1, …, w s, v 1, …, v s w_{1},\ldots,w_{s},v_{1},\ldots,v_{s} words in Σ ∗ \Sigma^{*} in which the w i w_{i} are non-empty but the v i v_{i} may be empty and with | w 1 | + ⋯ + | w s | ≤ | Q | − 1 |w_{1}|+\cdots+|w_{s}|\leq|Q|-1 and | v 0 | + ⋯ + | v s | ≤ N ⁡ ( | Q | − 1) |v_{0}|+\cdots+|v_{s}|\leq N(|Q|-1).

###### Proof.

Suppose towards a contradiction that this is not the case and pick a DFA ( Q, Σ, δ, q 0, F) (Q,\Sigma,\delta,q_{0},F) for which the conclusion to the statement of the proposition does not hold with | Q | |Q| minimal. We note that the result holds when | Q | = 1 |Q|=1, as the only sparse set accepted by a one-state automaton with input alphabet of size at least two is the empty set. Thus we may assume that | Q | > 1 |Q|>1.

We put a transitive binary relation ⪯ \preceq on Q Q by declaring that q ⪯ q ′ q\preceq q^{\prime} for q, q ′ ∈ Q q,q^{\prime}\in Q if there is a word w ∈ Σ ∗ w\in\Sigma^{*} such that δ ⁡ ( q, w) = q ′ \delta(q,w)=q^{\prime}. We then declare that two states q, q ′ q,q^{\prime} are equivalent if q ⪯ q ′ q\preceq q^{\prime} and q ′ ⪯ q q^{\prime}\preceq q. Then this relation is reflexive as δ ⁡ ( q, ϵ) = q \delta(q,\epsilon)=q, where ϵ \epsilon is the empty word; and it is symmetric and transitive by construction. We let [q] [q] denote the equivalence class of q q. Then ⪯ \preceq induces a partial order on the equivalence classes. We let r r denote the size of the equivalence class [q 0] [q_{0}]. Since ℒ \mathcal{L} is non-empty, there is at least one path from q 0 q_{0} to an accepting state. In particular, by Proposition 2.1 (3), we have that there is at most one cycle based at q 0 q_{0} and since it passes through all states in [q 0] [q_{0}], this cycle, if it exists, is some word w 1 w_{1} of length r r. We note that if r ≥ 2 r\geq 2 then there must be a cycle based at q 0 q_{0}, but if r = 1 r=1 it is possible that δ ⁡ ( q 0, w) = q 0 \delta(q_{0},w)=q_{0} if and only if w w is the empty word. We now consider two cases corresponding to these possibilities. The simpler case is when δ ⁡ ( q 0, w) = q 0 \delta(q_{0},w)=q_{0} only if w w is the empty word. In this case, [q 0] = q 0 [q_{0}]=q_{0} and for each x ∈ Σ x\in\Sigma, we let ℒ x \mathcal{L}_{x} denote the set of all words w ∈ Σ ∗ w\in\Sigma^{*} whose first letter is x x and for which w ∈ ℒ w\in\mathcal{L}. Then δ ⁡ ( q 0, u x) ∈ Q ∖ { q 0 } \delta(q_{0},u_{x})\in Q\setminus\{q_{0}\} for every u x ∈ ℒ x u_{x}\in\mathcal{L}_{x}. Then since q 0 q_{0} is only equivalent to itself, we see that ℒ x = x ​ ℰ x \mathcal{L}_{x}=x\mathcal{E}_{x}, where ℰ x \mathcal{E}_{x} is the regular language accepted by the automaton Γ x:= ( Q ∖ { q 0 }, Σ, δ, δ ⁡ ( q 0, x), F ∖ { q 0 }) \Gamma_{x}:=(Q\setminus\{q_{0}\},\Sigma,\delta,\delta(q_{0},x),F\setminus\{q_{0}\}).

Then by minimality of | Q | |Q|, we have that ℰ x \mathcal{E}_{x} is a union of at most

 | ( | Q | − 2)! ​ ( N | Q | − 2 + ⋯ + 1) (|Q|-2)!(N^{|Q|-2}+\cdots+1) |  |

sets of the form

 | { v 0 w 1 ∗ v 1 w 2 ∗ ⋯ v s − 1 w s ∗ v s } \{v_{0}w_{1}^{*}v_{1}w_{2}^{*}\cdots v_{s-1}w_{s}^{*}v_{s}\} |  |

with w 1, …, w s, v 0, …, v s w_{1},\ldots,w_{s},v_{0},\ldots,v_{s} words in Σ ∗ \Sigma^{*} in which the w i w_{i} are non-empty but the v i v_{i} may be empty and with | w 1 | + ⋯ + | w s | ≤ | Q | − 2 |w_{1}|+\cdots+|w_{s}|\leq|Q|-2 and | v 0 | + ⋯ + | v s | ≤ N ⁡ ( | Q | − 2) |v_{0}|+\cdots+|v_{s}|\leq N(|Q|-2). Then ℒ x \mathcal{L}_{x} is a union of at most ( | Q | − 2)! ​ ( N | Q | − 2 + ⋯ + 1) (|Q|-2)!(N^{|Q|-2}+\cdots+1) sets of the form

 | { ( x v 0) w 1 ∗ ⋯ v s − 1 w s ∗ v s } \{(xv_{0})w_{1}^{*}\cdots v_{s-1}w_{s}^{*}v_{s}\} |  |

with w 1, …, w s, v 0, …, v s w_{1},\ldots,w_{s},v_{0},\ldots,v_{s} words in Σ ∗ \Sigma^{*} in which the w i w_{i} are non-empty but the v i v_{i} may be empty and with | w 1 | + ⋯ + | w s | ≤ | Q | − 1 |w_{1}|+\cdots+|w_{s}|\leq|Q|-1 and | x ​ v 0 | + ⋯ + | v s | ≤ N ⁡ ( | Q | − 1) |xv_{0}|+\cdots+|v_{s}|\leq N(|Q|-1), since N ≥ 1 N\geq 1. Then since ℒ \mathcal{L} is the union of ℒ x \mathcal{L}_{x} for x ∈ Σ x\in\Sigma we see that ℒ \mathcal{L} is a union of at most ( | Q | − 2)! ​ ( N | Q | − 1 + N | Q | − 2 + ⋯ + N) (|Q|-2)!(N^{|Q|-1}+N^{|Q|-2}+\cdots+N) sets of the form

 | { v 0 w 1 ∗ v 1 w 2 ∗ ⋯ v s − 1 w s ∗ v s } \{v_{0}w_{1}^{*}v_{1}w_{2}^{*}\cdots v_{s-1}w_{s}^{*}v_{s}\} |  |

with w 1, …, w s, v 0, …, v s w_{1},\ldots,w_{s},v_{0},\ldots,v_{s} words in Σ ∗ \Sigma^{*} in which the w i w_{i} are non-empty but the v i v_{i} may be empty and with | w 1 | + ⋯ + | w s | ≤ | Q | − 1 |w_{1}|+\cdots+|w_{s}|\leq|Q|-1 and | v 0 | + ⋯ + | v s | ≤ N ⁡ ( | Q | − 1) |v_{0}|+\cdots+|v_{s}|\leq N(|Q|-1). Thus we obtain the result in this case.

We next consider the case when there is a unique cycle w 1 w_{1} of length r ≥ 1 r\geq 1 based at q 0 q_{0}. In particular, [q 0] [q_{0}] has size r r. Then in this case we can write ℒ = ℒ 0 ∪ ℒ 1 \mathcal{L}=\mathcal{L}_{0}\cup\mathcal{L}_{1}, where ℒ 0 \mathcal{L}_{0} is the set of words w w in ℒ \mathcal{L} for which δ ⁡ ( q 0, w) ∈ [q 0] \delta(q_{0},w)\in[q_{0}] and ℒ 1 \mathcal{L}_{1} is the set of words w ∈ ℒ w\in\mathcal{L} for which δ ⁡ ( q 0, w) ∉ [q 0] \delta(q_{0},w)\not\in[q_{0}]. By construction every word in ℒ 0 \mathcal{L}_{0} is of the form w 1 ∗ ​ v w_{1}^{*}v where v v is a proper prefix of w 1 w_{1}. In particular, ℒ 0 \mathcal{L}_{0} is a union of at most r r sets of the desired form. We next consider ℒ 1 \mathcal{L}_{1}. If w ∈ ℒ 1 w\in\mathcal{L}_{1} then w w can be written as u ​ x ​ v uxv with u, v ∈ Σ ∗, x ∈ Σ u,v\in\Sigma^{*},x\in\Sigma such that δ ⁡ ( q 0, u) ∈ [q 0] \delta(q_{0},u)\in[q_{0}] but δ ⁡ ( q 0, u ​ x) ∉ [q 0] \delta(q_{0},ux)\not\in[q_{0}]. Then we may write ℒ 1 \mathcal{L}_{1} as a union of | Q | − r |Q|-r sublanguages ℒ 1, q \mathcal{L}_{1,q} for each q ∈ Q ∖ [q 0] q\in Q\setminus[q_{0}], where ℒ 1 \mathcal{L}_{1} is the set of words in ℒ \mathcal{L} of the form u ​ x ​ v uxv with δ ⁡ ( q 0, u) ∈ [q 0] \delta(q_{0},u)\in[q_{0}], δ ⁡ ( q 0, u ​ x) = q \delta(q_{0},ux)=q.

Then each ℒ 1, q \mathcal{L}_{1,q} is a finite union of languages of the form w 1 ∗ ​ z ​ x ​ ℰ q w_{1}^{*}zx\mathcal{E}_{q} where z z is a proper prefix of w 1 w_{1}, x ∈ Σ x\in\Sigma and δ ⁡ ( q 0, z ​ x) = q \delta(q_{0},zx)=q and ℰ q \mathcal{E}_{q} is a sparse language accepted by an automaton with state set Q ∖ [q 0] Q\setminus[q_{0}]. In particular, by minimality of | Q | |Q|, each ℰ q \mathcal{E}_{q} is a finite union of at most ( | Q | − r − 1)! ​ ( N | Q | − r − 1 + ⋯ + 1) (|Q|-r-1)!(N^{|Q|-r-1}+\cdots+1) sets of the form

 | { v 1 w 2 ∗ v 2 w 3 ∗ ⋯ v s − 1 w s ∗ v s } \{v_{1}w_{2}^{*}v_{2}w_{3}^{*}\cdots v_{s-1}w_{s}^{*}v_{s}\} |  |

with | w 2 | + ⋯ + | w s | ≤ | Q | − r − 1 |w_{2}|+\cdots+|w_{s}|\leq|Q|-r-1 and | v 1 | + ⋯ + | v s | ≤ N ⁡ ( | Q | − r − 1) |v_{1}|+\cdots+|v_{s}|\leq N(|Q|-r-1). Then since w w has at most r r proper prefixes and since there are at most N N choices for x x, we see that ℒ 1, q \mathcal{L}_{1,q} is a union of at most ( r ​ N) ​ ( | Q | − r − 1)! ​ ( N | Q | − r − 1 + ⋯ + N + 1) (rN)(|Q|-r-1)!(N^{|Q|-r-1}+\cdots+N+1) sets of the form

 | { w 1 ∗ ( z x v 1) w 2 ∗ v 2 w 3 ∗ ⋯ v s − 1 w s ∗ v s } \{w_{1}^{*}(zxv_{1})w_{2}^{*}v_{2}w_{3}^{*}\cdots v_{s-1}w_{s}^{*}v_{s}\} |  |

with | w 1 | + ⋯ + | w s | ≤ | Q | − 1 |w_{1}|+\cdots+|w_{s}|\leq|Q|-1 and | z ​ x ​ v 1 | + ⋯ + | v s | ≤ N ⁡ ( | Q | − r − 1) + r ≤ N ⁡ ( | Q | − 1) |zxv_{1}|+\cdots+|v_{s}|\leq N(|Q|-r-1)+r\leq N(|Q|-1). Thus ℒ \mathcal{L} is a union of at most ( | Q | − r) ​ r ​ N ​ ( | Q | − r − 1)! ​ ( N | Q | − r − 1 + ⋯ + N + 1) + r (|Q|-r)rN(|Q|-r-1)!(N^{|Q|-r-1}+\cdots+N+1)+r sets of the desired form, where the contribution of r r comes from considering our decomposition of ℒ 0 \mathcal{L}_{0} and the | Q | − r |Q|-r factor comes from considering the languages ℒ 1, q \mathcal{L}_{1,q} for q ∈ Q ∖ [q 0] q\in Q\setminus[q_{0}]. Finally, since N ≥ 2 N\geq 2 we have r ≤ N r − 1 r\leq N^{r-1} and so

 |  | ( | Q | − r) ​ r ​ N ​ ( | Q | − r − 1)! ​ ( N | Q | − r − 1 + ⋯ + N + 1) + r \displaystyle~(|Q|-r)rN(|Q|-r-1)!(N^{|Q|-r-1}+\cdots+N+1)+r |  |

 |  | ≤ ( | Q | − r) ​ N r − 1 ⋅ N ⁡ ( | Q | − r − 1)! ​ ( N | Q | − r − 1 + ⋯ + N + 1) + N r − 1 \displaystyle\leq(|Q|-r)N^{r-1}\cdot N(|Q|-r-1)!(N^{|Q|-r-1}+\cdots+N+1)+N^{r-1} |  |

 |  | = ( | Q | − r)! ​ ( N | Q | − 1 + ⋯ + N r) + N r − 1 \displaystyle=(|Q|-r)!(N^{|Q|-1}+\cdots+N^{r})+N^{r-1} |  |

 |  | ≤ ( | Q | − 1)! ​ ( N | Q | − 1 + ⋯ + 1). \displaystyle\leq(|Q|-1)!(N^{|Q|-1}+\cdots+1). |  |

The result follows. ∎

We now make use of the estimate in Theorem 3.2.

###### Lemma 4.3.

Let k k and ℓ \ell be multiplicatively independent integers, let m m and n n be positive integers, and let a 1, …, a n, b 1, …, b m a_{1},\ldots,a_{n},b_{1},\ldots,b_{m} be nonzero rational numbers. Then there are at most

 | ( 8 ​ ( n + m − 1)) 10 ​ ( n + m) 5 − 4 ​ ( n + m − 1) 4 \left(8(n+m-1)\right)^{10(n+m)^{5}-4(n+m-1)^{4}} |  |

to the equation

 | a 1 ​ X 1 + ⋯ + a n ​ X n + b 1 ​ Y 1 + ⋯ + b m ​ Y m = 0 a_{1}X_{1}+\cdots+a_{n}X_{n}+b_{1}Y_{1}+\cdots+b_{m}Y_{m}=0 |  |

in which each X i X_{i} is a power of k k, each Y i Y_{i} is a power of ℓ \ell and no proper non-trivial subsum of the left-hand side vanishes.

###### Proof.

We consider the case when n ≤ m n\leq m; the case when m < n m<n is handled similarly. Let H 1:= { k a ℓ b: a, b ∈ ℤ } ≅ ( ℤ, +) 2 H_{1}:=\{k^{a}\ell^{b}:a,b\in\mathbb{Z}\}\cong(\mathbb{Z},+)^{2}, which is an abelian group of rank 2 2, and let H 2:= { ℓ b: b ∈ ℤ } ≅ ( ℤ, +) H_{2}:=\{\ell^{b}:b\in\mathbb{Z}\}\cong(\mathbb{Z},+), which has rank one.

A solution to the equation

 | a 1 ​ X 1 + ⋯ + a n ​ X n + b 1 ​ Y 1 + ⋯ + b m ​ Y m = 0 a_{1}X_{1}+\cdots+a_{n}X_{n}+b_{1}Y_{1}+\cdots+b_{m}Y_{m}=0 |  |

with the desired properties gives rise to a solution to the equation

(4) |  | ∑ i = 1 n ( − a i / b m) Z 1 + ∑ j = 1 m − 1 ( − b j / b m) Z n + j = 1 \sum_{i=1}^{n}(-a_{i}/b_{m})Z_{1}+\sum_{j=1}^{m-1}(-b_{j}/b_{m})Z_{n+j}=1 |  |

with Z i = X i / Y m ∈ H 1 Z_{i}=X_{i}/Y_{m}\in H_{1} for 1 ≤ i ≤ n 1\leq i\leq n and Z i = Y i − n / Y m ∈ H 2 Z_{i}=Y_{i-n}/Y_{m}\in H_{2} for n + 1 ≤ i < n + m n+1\leq i<n+m, and with Equation ( 4) non-degenerate. Then ( Z 1, …, Z n + m − 1) ∈ Γ ⊆ ( ℚ ∗) n + m − 1 (Z_{1},\ldots,Z_{n+m-1})\in\Gamma\subseteq(\mathbb{Q}^{*})^{n+m-1}, where Γ = H 1 n × H 2 m − 1 \Gamma=H_{1}^{n}\times H_{2}^{m-1}, which is a group of rank 2 ​ n + m − 1 2n+m-1. Thus we can take r = 2 ​ n + m − 1 r=2n+m-1 in Theorem 3.2, and this gives that Equation ( 4) has at most

(5) |  | ( 8 ​ ( n + m − 1)) 4 ​ ( n + m − 1) 4 ​ ( 3 ​ n + 2 ​ m − 1) (8(n+m-1))^{4(n+m-1)^{4}(3n+2m-1)} |  |

non-degenerate solutions. Since n ≤ m n\leq m, we have 3 ​ n + 2 ​ m ≤ 5 ​ ( n + m) / 2 3n+2m\leq 5(n+m)/2, and so 4 ​ ( n + m − 1) 4 ​ ( 3 ​ n + 2 ​ m − 1) ≤ 10 ​ ( n + m) 5 − 4 ​ ( n + m − 1) 4 4(n+m-1)^{4}(3n+2m-1)\leq 10(n+m)^{5}-4(n+m-1)^{4}. Thus the quantity in Equation ( 5) is bounded above by

 | ( 8 ​ ( n + m − 1)) 10 ​ ( n + m) 5 − 4 ​ ( n + m − 1) 4. (8(n+m-1))^{10(n+m)^{5}-4(n+m-1)^{4}}. |  |

Finally, we can uniquely recover the original X i X_{i} ’s and Y i Y_{i} ’s from Z 1, …, Z m + n − 1 Z_{1},\ldots,Z_{m+n-1}. To see this, observe that for i = 1, …, n i=1,\ldots,n we must have Z i = k a / ℓ b Z_{i}=k^{a}/\ell^{b} for some integers a a and b b. Since k k and ℓ \ell are multiplicatively independent, a a and b b are uniquely determined. So we can recover X 1, …, X n X_{1},\ldots,X_{n} and Y m Y_{m} from Z 1, …, Z n Z_{1},\dots,Z_{n}. But we can then recover Y 1, …, Y m − 1 Y_{1},\dots,Y_{m-1} from the remaining Z j Z_{j}. The result follows.

∎

We now use the preceding lemma to give estimates in the case where some degeneracy is allowed.

###### Lemma 4.4.

Let k k and ℓ \ell be multiplicatively independent integers and let m, n ≥ 1 m,n\geq 1 be integers and let a 1, …, a n, b 1, …, b m a_{1},\ldots,a_{n},b_{1},\ldots,b_{m} be nonzero rational numbers. Then there are at most

 | 2 − ( n + m) ⋅ ( 8 ​ ( n + m − 1)) 10 ​ ( n + m) 5 − ( n + m) 2^{-(n+m)}\cdot\left(8(n+m-1)\right)^{10(n+m)^{5}-(n+m)} |  |

solutions to the equation

 | a 1 ​ X 1 + ⋯ + a n ​ X n + b 1 ​ Y 1 + ⋯ + b m ​ Y m = 0 a_{1}X_{1}+\cdots+a_{n}X_{n}+b_{1}Y_{1}+\cdots+b_{m}Y_{m}=0 |  |

in which each X i X_{i} is a power of k k, each Y i Y_{i} is a power of ℓ \ell, and no non-trivial subsum of either a 1 ​ X 1 + ⋯ + a n ​ X n a_{1}X_{1}+\cdots+a_{n}X_{n} or b 1 ​ Y 1 + ⋯ + b m ​ Y m b_{1}Y_{1}+\cdots+b_{m}Y_{m} vanishes.

###### Proof.

For each solution to

 | a 1 ​ X 1 + ⋯ + a n ​ X n + b 1 ​ Y 1 + ⋯ + b m ​ Y m = 0 a_{1}X_{1}+\cdots+a_{n}X_{n}+b_{1}Y_{1}+\cdots+b_{m}Y_{m}=0 |  |

such that no subsum of either a 1 ​ X 1 + ⋯ + a n ​ X n a_{1}X_{1}+\cdots+a_{n}X_{n} or b 1 ​ Y 1 + ⋯ + b m ​ Y m b_{1}Y_{1}+\cdots+b_{m}Y_{m} vanishes, we can associate a set partition π \pi of the set V:= { X 1, …, X n, Y 1, …, Y m } V:=\{X_{1},\ldots,X_{n},Y_{1},\ldots,Y_{m}\} into disjoint non-empty subsets U 1, …, U r U_{1},\ldots,U_{r} such that the subsum corresponding to the variables in each U i U_{i} vanishes and no proper subsum vanishes. Let c i:= | U i | c_{i}:=|U_{i}|. Then U i U_{i} intersects both { X 1, …, X n } \{X_{1},\ldots,X_{n}\} and { Y 1, …, Y m } \{Y_{1},\ldots,Y_{m}\} non-trivially and so by Lemma 4.3, for i = 1, …, r i=1,\ldots,r, there are at most ( 8 ​ ( c i − 1)) 10 ​ c i 5 − 4 ​ ( c i − 1) 4 \left(8(c_{i}-1)\right)^{10c_{i}^{5}-4(c_{i}-1)^{4}} non-degenerate solutions to the subsum

 | ∑ X j ∈ U i a j ​ X j + ∑ Y j ∈ U i b j ​ Y j = 0 \sum_{X_{j}\in U_{i}}a_{j}X_{j}+\sum_{Y_{j}\in U_{i}}b_{j}Y_{j}=0 |  |

with each X j X_{j} a power of k k and each Y j Y_{j} a power of ℓ \ell. Thus for the set partition π \pi we have at most

 | ∏ i = 1 r ( 8 ​ ( c i − 1)) 10 ​ c i 5 − 4 ​ ( c i − 1) 4 \displaystyle\prod_{i=1}^{r}\left(8(c_{i}-1)\right)^{10c_{i}^{5}-4(c_{i}-1)^{4}} | ≤ ( 8 ​ ( n + m − 1)) ∑ i = 1 r ( 10 ​ c i 5 − 4 ​ ( c i − 1) 4) \displaystyle\leq\left(8(n+m-1)\right)^{\sum_{i=1}^{r}(10c_{i}^{5}-4(c_{i}-1)^{4})} |  |

 |  | ≤ ( 8 ​ ( n + m − 1)) 10 ​ ( ∑ i = 1 r c i) 5 − 4 ​ ∑ i = 1 r ( c i − 1) \displaystyle\leq\left(8(n+m-1)\right)^{10\left(\sum_{i=1}^{r}c_{i}\right)^{5}-4\sum_{i=1}^{r}(c_{i}-1)} |  |

 |  | = ( 8 ​ ( n + m − 1)) 10 ​ ( n + m) 5 − 4 ​ ( n + m − r) \displaystyle=\left(8(n+m-1)\right)^{10(n+m)^{5}-4(n+m-r)} |  |

 |  | ≤ ( 8 ​ ( n + m − 1)) 10 ​ ( n + m) 5 − 2 ​ ( n + m) \displaystyle\leq\left(8(n+m-1)\right)^{10(n+m)^{5}-2(n+m)} |  |

solutions, where the last step follows from the fact that

(6) |  | r ≤ ( n + m) / 2, r\leq(n+m)/2, |  |

which is a consequence of the fact that each U i U_{i} intersects both { X 1, …, X n } \{X_{1},\ldots,X_{n}\} and { Y 1, …, Y m } \{Y_{1},\ldots,Y_{m}\} non-trivially.

Finally, observe that collection of set partitions of a finite set W W having exactly e e parts embeds in the collection of surjective maps from W W to { 1, …, e } \{1,\ldots,e\}, by first assigning the labels 1, …, e 1,\ldots,e to the sets making up a set partition and then associating the map which sends w ∈ W w\in W to the label of the set it is in. Since the number of parts in our set partitions is bounded by ( n + m) / 2 (n+m)/2, we see that the number of possible set partitions we have to consider is at most ( ( n + m) / 2) n + m \left((n+m)/2\right)^{n+m}, since it embeds in the set of maps from V V into { 1, …, ⌊ ( n + m) / 2 ⌋ } \{1,\ldots,\lfloor(n+m)/2\rfloor\}. Since we get at most

 | ( 8 ​ ( n + m − 1)) 10 ​ ( n + m) 5 − 2 ​ ( n + m) \left(8(n+m-1)\right)^{10(n+m)^{5}-2(n+m)} |  |

solutions of the desired form corresponding to each associated set partition of V V, and since there are at most ( ( n + m) / 2) n + m ((n+m)/2)^{n+m} possible set partitions that can occur, we get an upper bound of

 |  | ( ( n + m) / 2) n + m ⋅ ( 8 ​ ( n + m − 1)) 10 ​ ( n + m) 5 − 2 ​ ( n + m) \displaystyle~((n+m)/2)^{n+m}\cdot\left(8(n+m-1)\right)^{10(n+m)^{5}-2(n+m)} |  |

 |  | ≤ 2 − ( n + m) ⋅ ( 8 ​ ( n + m − 1)) n + m ​ ( 8 ​ ( n + m − 1)) 10 ​ ( n + m) 5 − 2 ​ ( n + m) \displaystyle\leq 2^{-(n+m)}\cdot\left(8(n+m-1)\right)^{n+m}(8(n+m-1))^{10(n+m)^{5}-2(n+m)} |  |

 |  | = 2 − ( n + m) ⋅ ( 8 ​ ( n + m − 1)) 10 ​ ( n + m) 5 − ( n + m). \displaystyle=2^{-(n+m)}\cdot(8(n+m-1))^{10(n+m)^{5}-(n+m)}. |  |

The result follows. ∎

We now use these estimates to obtain upper bounds on the size of an intersection of sparse subsets of ℕ \mathbb{N}.

###### Proposition 4.5.

Let k k and ℓ \ell be multiplicatively independent positive integers, let s ≥ 1, t ≥ 1 s\geq 1,t\geq 1, and let v 0, …, v s, w 1, …, w s ∈ Σ k ∗ v_{0},\ldots,v_{s},w_{1},\ldots,w_{s}\in\Sigma_{k}^{*} and u 0, …, u t, y 1, …, y t ∈ Σ ℓ ∗ u_{0},\ldots,u_{t},y_{1},\ldots,y_{t}\in\Sigma_{\ell}^{*}. If

 | X = { [v 0 w 1 ∗ v 1 w 2 ∗ ⋯ v s − 1 w s ∗ v s] k } X=\{[v_{0}w_{1}^{*}v_{1}w_{2}^{*}\cdots v_{s-1}w_{s}^{*}v_{s}]_{k}\} |  |

and

 | Y = { [u 0 y 1 ∗ u 1 y 2 ∗ ⋯ u t − 1 y t ∗ u t] ℓ }, Y=\{[u_{0}y_{1}^{*}u_{1}y_{2}^{*}\cdots u_{t-1}y_{t}^{*}u_{t}]_{\ell}\}, |  |

then

 | | X ∩ Y | ≤ ( 8 ​ ( s + t + 1)) 10 ​ ( s + t + 2) 5 − ( s + t + 2). \left|X\cap Y\right|\leq\left(8(s+t+1)\right)^{10(s+t+2)^{5}-(s+t+2)}. |  |

###### Proof.

By Proposition 2.2 we have that X X is of the form

 | { c 0 + c 1 k δ s ​ n s + c 2 k δ s ​ n s + δ s − 1 ​ n s − 1 + ⋯ + c s k δ s ​ n s + ⋯ + δ 1 ​ n 1: n 1, …, n s ≥ 0 }, \left\{c_{0}+c_{1}k^{\delta_{s}n_{s}}+c_{2}k^{\delta_{s}n_{s}+\delta_{s-1}n_{s-1}}+\cdots+c_{s}k^{\delta_{s}n_{s}+\cdots+\delta_{1}n_{1}}\colon n_{1},\ldots,n_{s}\geq 0\right\}, |  |

where c 0, …, c s c_{0},\ldots,c_{s} are rational numbers. Similarly, Y Y is of the form

 | { d 0 + d 1 ℓ δ t ′ ​ m t + d 2 ℓ δ t ′ ​ m s + δ t − 1 ′ ​ m t − 1 + ⋯ + d t ℓ δ t ′ ​ m t + ⋯ + δ 1 ′ ​ m 1: m 1, …, m t ≥ 0 }, \left\{d_{0}+d_{1}\ell^{\delta_{t}^{\prime}m_{t}}+d_{2}\ell^{\delta_{t}^{\prime}m_{s}+\delta_{t-1}^{\prime}m_{t-1}}+\cdots+d_{t}\ell^{\delta_{t}^{\prime}m_{t}+\cdots+\delta_{1}^{\prime}m_{1}}\colon m_{1},\ldots,m_{t}\geq 0\right\}, |  |

where d 0, …, d t d_{0},\ldots,d_{t} are rational numbers.

Then an element in X ∩ Y X\cap Y corresponds to a solution to the equation

 | d 0 ​ X 0 + ⋯ + d t ​ X t − c 0 ​ Y 0 − ⋯ − c s ​ Y s = 0, d_{0}X_{0}+\cdots+d_{t}X_{t}-c_{0}Y_{0}-\cdots-c_{s}Y_{s}=0, |  |

where

 | X 0 = 1, X 1 = ℓ δ t ′ ​ m t, …, X t = ℓ δ t ′ ​ m t + ⋯ + δ 1 ′ ​ m 1 X_{0}=1,X_{1}=\ell^{\delta_{t}^{\prime}m_{t}},\ldots,X_{t}=\ell^{\delta_{t}^{\prime}m_{t}+\cdots+\delta_{1}^{\prime}m_{1}} |  |

and

 | Y 0 = 1, …, Y s = k δ s ​ n s + ⋯ + δ 1 ​ n 1, Y_{0}=1,\ldots,Y_{s}=k^{\delta_{s}n_{s}+\cdots+\delta_{1}n_{1}}, |  |

with the corresponding element in the intersection given by

 | A:= d 0 ​ X 0 + ⋯ + d t ​ X t = c 0 ​ Y 0 + ⋯ + c s ​ Y s. A:=d_{0}X_{0}+\cdots+d_{t}X_{t}=c_{0}Y_{0}+\cdots+c_{s}Y_{s}. |  |

Since we are only concerned about the quantity A A in determining X ∩ Y X\cap Y, after removing a maximal vanishing subsum 1 1 1 For nonzero A A, this will be necessarily a proper subset, but when A = 0 A=0 this will be the entire set. The estimates we give account for this possibility. we may assume that no non-trivial subsum of the terms involving powers of ℓ \ell vanishes and that there are at most t + 1 t+1 such terms. Similarly, we may remove a maximal vanishing subsum from X t + 1 + ⋯ + X t + s + 1 X_{t+1}+\cdots+X_{t+s+1}.

By Lemma 4.4, taking n n to be the number of terms from our first sum, we have n ≤ t + 1 n\leq t+1; similarly, we can take m m to be the number of terms from our second subsum and we have m ≤ s + 1 m\leq s+1. Using the fact that there are at most 2 s + 1 ⋅ 2 t + 1 2^{s+1}\cdot 2^{t+1} possible pairs of maximal vanishing subsums that we can remove and the fact that the function

 | F ⁡ ( a, b) = 2 − a − b − 2 ​ ( 8 ​ ( a + b + 1)) 10 ​ ( a + b + 2) 5 − ( a + b + 2) F(a,b)=2^{-a-b-2}\left(8(a+b+1)\right)^{10(a+b+2)^{5}-(a+b+2)} |  |

is increasing in both a a and b b for a, b ≥ 0 a,b\geq 0, we then see there are at most

 | 2 s + t + 2 ⋅ 2 − ( s + t + 2) ​ ( 8 ​ ( s + t + 1)) 10 ​ ( s + t + 2) 5 − ( s + t + 2) 2^{s+t+2}\cdot 2^{-(s+t+2)}\left(8(s+t+1)\right)^{10(s+t+2)^{5}-(s+t+2)} |  |

elements in X ∩ Y X\cap Y. The result follows.

∎

We are now ready to prove Theorem 4.1.

###### Proof of Theorem 4.1.

By Proposition 4.2 X X is a union of sets W 1, …, W A 1 W_{1},\ldots,W_{A_{1}} of the form

(7) |  | { [v 0 w 1 ∗ v 1 w 2 ∗ ⋯ v s − 1 w s ∗ v s] k } \{[v_{0}w_{1}^{*}v_{1}w_{2}^{*}\cdots v_{s-1}w_{s}^{*}v_{s}]_{k}\} |  |

with w 1, …, w s, v 0, …, v s w_{1},\ldots,w_{s},v_{0},\ldots,v_{s} words in ( Σ k d) ∗ (\Sigma_{k}^{d})^{*} in which the w i w_{i} are non-empty but the v i v_{i} may be empty and with | w 1 | + ⋯ + | w s | ≤ | Q | − 1 |w_{1}|+\cdots+|w_{s}|\leq|Q|-1 and | v 0 | + ⋯ + | v s | ≤ k d ​ ( | Q | − 1) |v_{0}|+\cdots+|v_{s}|\leq k^{d}(|Q|-1). Moreover, since our input alphabet has size k d k^{d}, Proposition 4.2 also says we can take

 | A 1 ≤ ( | Q | − 1)! ​ ( k d ⁡ ( | Q | − 1) + k d ⁡ ( | Q | − 2) + ⋯ + 1). A_{1}\leq(|Q|-1)!(k^{d(|Q|-1)}+k^{d(|Q|-2)}+\cdots+1). |  |

Similarly, Y Y is the union of sets Z 1, …, Z A 2 Z_{1},\ldots,Z_{A_{2}} with

 | A 2 ≤ ( | Q ′ | − 1)! ​ ( ℓ d ⁡ ( | Q ′ | − 1) + ℓ d ⁡ ( | Q ′ | − 2) + ⋯ + 1) A_{2}\leq(|Q^{\prime}|-1)!(\ell^{d(|Q^{\prime}|-1)}+\ell^{d(|Q^{\prime}|-2)}+\cdots+1) |  |

and each Z j Z_{j} of the form

(8) |  | { [u 0 y 1 ∗ u 1 y 2 ∗ ⋯ u t − 1 y t ∗ u t + 1] ℓ } \{[u_{0}y_{1}^{*}u_{1}y_{2}^{*}\cdots u_{t-1}y_{t}^{*}u_{t+1}]_{\ell}\} |  |

with u 0, …, u t + 1, y 1, …, y t u_{0},\ldots,u_{t+1},y_{1},\ldots,y_{t} words in ( Σ ℓ d) ∗ (\Sigma_{\ell}^{d})^{*} in which the y i y_{i} are non-empty but the u i u_{i} may be empty and with | y 1 | + ⋯ + | y t | ≤ | Q ′ | − 1 |y_{1}|+\cdots+|y_{t}|\leq|Q^{\prime}|-1 and | u 0 | + ⋯ + | u t | ≤ ℓ ⁡ ( | Q ′ | − 1) |u_{0}|+\cdots+|u_{t}|\leq\ell(|Q^{\prime}|-1). In particular, t ≤ | Q ′ | − 1 t\leq|Q^{\prime}|-1 for each such set.

Now for ( p, q) ∈ { 1, …, A 1 } × { 1, …, A 2 } (p,q)\in\{1,\ldots,A_{1}\}\times\{1,\ldots,A_{2}\} and each i = 1, …, d i=1,\ldots,d, we let W p, i ⊆ ℕ W_{p,i}\subseteq\mathbb{N} and Z q, i ⊆ ℕ Z_{q,i}\subseteq\mathbb{N} be respectively the images of W p W_{p} and Z q Z_{q} under the projection map from ℕ d \mathbb{N}^{d} onto its i i -th coordinate. For i ∈ { 1, …, d } i\in\{1,\ldots,d\} we have

 | proj i ( v 1 w 1 ∗ v 2 w 2 ∗ ⋯ v s w s ∗ v s + 1) = proj i ( v 1) proj i ( w 1) ∗ ⋯ proj i ( w s) ∗ proj i ( v s + 1), \proj_{i}(v_{1}w_{1}^{*}v_{2}w_{2}^{*}\cdots v_{s}w_{s}^{*}v_{s+1})=\proj_{i}(v_{1})\proj_{i}(w_{1})^{*}\cdots\proj_{i}(w_{s})^{*}\proj_{i}(v_{s+1}), |  |

where proj i {\rm proj}_{i} is the projection map ( Σ k d) ∗ → Σ k ∗ (\Sigma_{k}^{d})^{*}\to\Sigma_{k}^{*} obtained by taking the i i -th coordinate. It follows that each W p, i W_{p,i} is a set of the form given in Equation ( 7) but where we now use words over Σ k \Sigma_{k} instead of ( Σ k) d (\Sigma_{k})^{d}. Similarly, each Z q, i Z_{q,i} is a set of the form given in Equation ( 8), but where we now use words over Σ ℓ \Sigma_{\ell} instead.

By Proposition 4.5, each W p, i ∩ Z q, i W_{p,i}\cap Z_{q,i} has cardinality at most

 | ( 8 ​ ( s + t + 1)) 10 ​ ( s + t + 2) 5 − ( s + t + 2) \left(8(s+t+1)\right)^{10(s+t+2)^{5}-(s+t+2)} |  |

in the intersection. In particular, since s ≤ | Q | − 1 s\leq|Q|-1 and t ≤ | Q ′ | − 1 t\leq|Q^{\prime}|-1, we have

 | | W p, i ∩ Z q, i | ≤ ( 8 ​ ( | Q | + | Q ′ | − 1)) 10 ​ ( | Q | + | Q ′ |) 5 − ( | Q | + | Q ′ |). |W_{p,i}\cap Z_{q,i}|\leq\left(8(|Q|+|Q^{\prime}|-1)\right)^{10(|Q|+|Q^{\prime}|)^{5}-(|Q|+|Q^{\prime}|)}. |  |

Now since

 | W p ∩ Z q ⊆ ( W p, 1 ∩ Z q, 1) × ⋯ × ( W p, d ∩ Z q, d), W_{p}\cap Z_{q}\subseteq(W_{p,1}\cap Z_{q,1})\times\cdots\times(W_{p,d}\cap Z_{q,d}), |  |

we then see each intersection W p ∩ Z q W_{p}\cap Z_{q} has size at most

 | ( 8 ​ ( | Q | + | Q ′ | − 1)) 10 ​ d ​ ( | Q | + | Q ′ |) 5 − d ⁡ ( | Q | + | Q ′ |). \left(8(|Q|+|Q^{\prime}|-1)\right)^{10d(|Q|+|Q^{\prime}|)^{5}-d(|Q|+|Q^{\prime}|)}. |  |

Finally, since

 | X ∩ Y = ⋃ p ≤ A 1 ⋃ q ≤ A 2 ( W p ∩ Z q), X\cap Y=\bigcup_{p\leq A_{1}}\bigcup_{q\leq A_{2}}(W_{p}\cap Z_{q}), |  |

we see that

 | | X ∩ Y | ≤ A 1 ⋅ A 2 ⋅ ( 8 ​ ( | Q | + | Q ′ | − 1)) 10 ​ d ​ ( | Q | + | Q ′ |) 5 − d ⁡ ( | Q | + | Q ′ |). |X\cap Y|\leq A_{1}\cdot A_{2}\cdot\left(8(|Q|+|Q^{\prime}|-1)\right)^{10d(|Q|+|Q^{\prime}|)^{5}-d(|Q|+|Q^{\prime}|)}. |  |

Finally, observe that A 1 ≤ | Q | | Q | ⋅ k d ​ | Q | A_{1}\leq|Q|^{|Q|}\cdot k^{d|Q|} and A 2 ≤ | Q ′ | | Q ′ | ⋅ ℓ d ​ | Q ′ | A_{2}\leq|Q^{\prime}|^{|Q^{\prime}|}\cdot\ell^{d|Q^{\prime}|}, so we get

 | | X ∩ Y | ≤ k d ​ | Q | ⋅ ℓ d ​ | Q ′ | ⋅ | Q | | Q | ⋅ | Q ′ | | Q ′ | ⋅ ( 8 ​ ( | Q | + | Q ′ | − 1)) 10 ​ d ​ ( | Q | + | Q ′ |) 5 − d ⁡ ( | Q | + | Q ′ |), |X\cap Y|\leq k^{d|Q|}\cdot\ell^{d|Q^{\prime}|}\cdot|Q|^{|Q|}\cdot|Q^{\prime}|^{|Q^{\prime}|}\cdot\left(8(|Q|+|Q^{\prime}|-1)\right)^{10d(|Q|+|Q^{\prime}|)^{5}-d(|Q|+|Q^{\prime}|)}, |  |

which is easily seen to be less than

 | k d ​ | Q | ⋅ ℓ d ​ | Q ′ | ⋅ ( 8 ​ ( | Q | + | Q ′ | − 1)) 10 ​ d ​ ( | Q | + | Q ′ |) 5. k^{d|Q|}\cdot\ell^{d|Q^{\prime}|}\cdot\left(8(|Q|+|Q^{\prime}|-1)\right)^{10d(|Q|+|Q^{\prime}|)^{5}}. |  |

The result follows. ∎

###### Remark 4.6.

We note that the strategy employed in the proof of Theorem 4.1 involves giving a description of the complexity of the sublanguages of ( Σ k d) ∗ (\Sigma_{k}^{d})^{*} and ( Σ ℓ d) ∗ (\Sigma_{\ell}^{d})^{*} accepted by our automata, then using this to bound the complexity of their projections, and finally using S S -unit theory to get a bound on the sizes of the projections. An alternative approach would be to first find the automata that accept the projections of the languages and work with those bounds. The projection of a regular language accepted by an automaton with n n states can be accepted by an automaton with 2 n 2^{n} states. 2 2 2 There are improvements to this bound (see, for example, [21] and references therein), but in general the number of states required to accept a projected language is exponential in the number of states of the minimal automaton accepting the original language. If one uses this approach one gets an alternative bound that is typically much worse.

## 5. A general intersection question

We now consider the general question of what the intersection of a sparse automatic set with a zero-density automatic set can look like. We recall that for a subset S S of ℕ \mathbb{N}, the *density*of S S is just the limit

(9) |  | lim n → ∞ π S ​ ( n) n, \lim_{n\to\infty}\frac{\pi_{S}(n)}{n}, |  |

if it exists. In general, a set of natural numbers always has a lower density and an upper density given respectively by

(10) |  | lim inf n → ∞ π S ​ ( n) n ​ and ​ lim sup n → ∞ π S ​ ( n) n, \liminf_{n\to\infty}\frac{\pi_{S}(n)}{n}\text{ and }\limsup_{n\to\infty}\frac{\pi_{S}(n)}{n}, |  |

and so the density exists precisely when these two values coincide.

We make the remark that since sparse automatic sets are polylogarithmically bounded, they necessarily have density zero.

The following result is due to the second-named author [7, Prop. 2.1].

###### Proposition 5.1.

Let k ≥ 2 k\geq 2 be a natural number, let h: ℕ → ℚ ≥ 0 h:\mathbb{N}\to\mathbb{Q}_{\geq 0} be a k k -automatic sequence, and let s ⁡ ( n) = ∑ j < n h ⁡ ( j) s(n)=\sum_{j<n}h(j). Then there exist β ∈ ( 0, k) \beta\in(0,k), C > 0 C>0, a ≥ 1 a\geq 1, and nonnegative rational numbers c j c_{j} for j ∈ { 0, 1, …, a − 1 } j\in\{0,1,\ldots,a-1\} such that

 | | s ⁡ ( k a ​ n + j) − c j ​ k a ​ n + j | < C ​ β a ​ n |s(k^{an+j})-c_{j}k^{an+j}|<C\beta^{an} |  |

for every n ≥ 0 n\geq 0. Moreover, a a and the rational numbers c 0, …, c a − 1 c_{0},\ldots,c_{a-1} are recursively computable and β \beta can be effectively determined.

As a consequence of this, we can prove that either a k k -automatic set S S has positive lower density (i.e., lim inf π S ​ ( x) / x > 0 \liminf\pi_{S}(x)/x>0) or there is some positive ϵ > 0 \epsilon>0 such that π S ​ ( x) = O ⁡ ( x 1 − ϵ) \pi_{S}(x)={O}(x^{1-\epsilon}).

###### Proposition 5.2.

Let k ≥ 2 k\geq 2 be a natural number and let S S be a k k -automatic subset of the natural numbers. Then either S S has positive lower density or there is some ϵ > 0 \epsilon>0 such that π S ​ ( x) = O ⁡ ( x 1 − ϵ). \pi_{S}(x)={O}(x^{1-\epsilon}).

###### Proof.

Taking h: ℕ → { 0, 1 } h:\mathbb{N}\to\{0,1\} to be the characteristic function of S S and then applying Proposition 5.1, we see that either S S has positive lower density or π S ​ ( k n) = O ⁡ ( β n) \pi_{S}(k^{n})={O}(\beta^{n}) for some β ∈ ( 0, k) \beta\in(0,k). We henceforth assume that we are in the second case. Then there is some ϵ > 0 \epsilon>0 such that

 | π S ​ ( k n) = O ⁡ ( k ( 1 − ϵ) ​ n). \pi_{S}(k^{n})={O}(k^{(1-\epsilon)n}). |  |

Then for a given x > 1 x>1, we have k n ≤ x < k n + 1 k^{n}\leq x<k^{n+1} for some n n and so

 | π S ​ ( x) ≤ π S ​ ( k n + 1) = O ⁡ ( ( k n + 1) 1 − ϵ). \pi_{S}(x)\leq\pi_{S}(k^{n+1})={O}((k^{n+1})^{1-\epsilon}). |  |

Since k ​ x ≥ k n + 1 kx\geq k^{n+1} we then see

 | π S ​ ( x) = O ⁡ ( x 1 − ϵ), \pi_{S}(x)={O}(x^{1-\epsilon}), |  |

and so we obtain the desired result. ∎

In general, if k k and ℓ \ell are multiplicatively independent, then a sparse k k -automatic set can have infinite intersection with an ℓ \ell -automatic set, but in the case when X X is a sparse k k -automatic set and Y Y is an ℓ \ell -automatic set of zero density, we expect X ∩ Y X\cap Y to be finite. Heuristically, one can see why this should be the case as follows. Since Y Y has zero density, we have shown that there is some ϵ > 0 \epsilon>0 such that π Y ​ ( x) = O ⁡ ( x 1 − ϵ) \pi_{Y}(x)=O(x^{1-\epsilon}), and since X X is sparse there are positive constants c c and d d such that π X ​ ( x) ≤ c ​ ( log ⁡ x) d \pi_{X}(x)\leq c(\log\,x)^{d} for x x large. Thus there is some C > 0 C>0 such that, for x x large, if we take a natural number in [0, x] [0,x], the probability that it lies in Y Y is at most C ​ x − ϵ Cx^{-\epsilon}. In particular, if i 1 < i 2 < i 3 < ⋯ i_{1}<i_{2}<i_{3}<\cdots is an enumeration of the elements of our sparse k k -automatic set S S, then since the bases k k and ℓ \ell are multiplicatively independent, we expect that the probability that i j i_{j} is in Y Y to be at most C ​ i j − ϵ Ci_{j}^{-\epsilon}, and so the expected number of elements in X ∩ Y X\cap Y should be bounded by the size of the sum

 | ∑ j ≥ 1 C i j ϵ. \sum_{j\geq 1}\frac{C}{i_{j}^{\epsilon}}. |  |

Notice that the above series converges when X X is sparse. To see this, recall that π X ​ ( x) ≤ c ​ ( log ⁡ x) d \pi_{X}(x)\leq c(\log\,x)^{d} for some c, d > 0 c,d>0 and for x x large. Since π X ​ ( i N) = N \pi_{X}(i_{N})=N, we then have N ≤ c ​ ( log ⁡ i N) d N\leq c(\log\,i_{N})^{d} for N N large, which gives i N ≥ exp ⁡ ( ( N / c) 1 / d) i_{N}\geq\exp((N/c)^{1/d}) for N N sufficiently large. In particular, i N i_{N} grows faster than any polynomial in N N and so for every ϵ > 0 \epsilon>0 we have that ∑ 1 / i j ϵ \sum 1/i_{j}^{\epsilon} converges.

Using this heuristic as a guide, we make the following conjecture, although this problem appears to be well beyond what current methods in number theory can handle.

###### Conjecture 5.3.

Let k, ℓ k,\ell be multiplicatively independent positive integers. If X X is a sparse k k -automatic subset of ℕ \mathbb{N} and Y Y is a zero-density ℓ \ell -automatic subset of ℕ \mathbb{N}, then X ∩ Y X\cap Y is finite.

We note that if we take k = 2, ℓ = 3 k=2,\ell=3 and X = { 2 i: i ≥ 0 } X=\{2^{i}\colon i\geq 0\} and Y Y to be the set of numbers whose ternary expansions have no occurrences of 2 2, then Y Y has zero density and X X is sparse and so the conjecture of Erdős [15, p. 67] mentioned in the introduction is a special case of Conjecture 5.3.

## References

- [1] B. Adamczewski and J. P. Bell, Function fields in positive characteristic: expansions and Cobham’s theorem. *J. Algebra*319 (2008), no. 6, 2337–2350.
- [2] B. Adamczewski and J. P. Bell, A problem about Mahler functions. *Ann. Sc. Norm. Super. Pisa Cl. Sci.*(5) 17 (2017), no. 4, 1301–1355.
- [3] S. Albayrak and J. P. Bell, A refinement of Christol’s theorem for algebraic power series. *Math. Z.*300 (2022), no. 3, 2265–2288.
- [4] J.-P. Allouche and J. Shallit, *Automatic Sequences. Theory, applications, generalizations.*Cambridge University Press, Cambridge, 2003.
- [5] F. Amoroso and E. Viada, Small points on subvarieties of a torus. *Duke Math. J.*150 (2009), no. 3, 407–442.
- [6] J. P. Bell, A generalization of Cobham’s theorem for regular sequences. *Sém. Lothar. Combin.*54A (2005/07), Art. B54Ap. 15 pp.
- [7] J. P. Bell, The upper density of an automatic set is rational. *J. Théor. Nombres Bordeaux*32 (2020), no. 2, 585–604.
- [8] J. P. Bell, D. Ghioca, and R. Moosa, *Effective isotrivial Mordell-Lang in positive characteristic*. Preprint available at arXiv:2010.08579.
- [9] J. P. Bell and R. Moosa, F F -sets and finite automata. *J. Théor. Nombres Bordeaux*31 (2019), no. 1, 101–130.
- [10] A. Cobham, On the base-dependence of sets of numbers recognizable by finite automata. *Math. Systems Theory*3 (1969), 186–192.
- [11] H. Derksen, A Skolem-Mahler-Lech theorem in positive characteristic and finite automata. *Invent. Math.*168 (2007), no. 1. 175–224.
- [12] F. Durand, A generalization of Cobham’s Theorem. *Theory Comput. Syst.*31 (1998), no. 2, 169–185.
- [13] F. Durand, Cobham’s theorem for substitutions. *J. Eur. Math. Soc. (JEMS)*13 (2011), no. 6, 1799–1814.
- [14] F. Durand and M. Rigo, On Cobham’s theorem. *Handbook of automata theory. Vol. II. Automata in mathematics and selected applications*, 947–986, EMS Press, Berlin, 2021.
- [15] P. Erdős, Some unconventional problems in number theory. *Math. Mag.*52, No. 2 (1979), 67–70.
- [16] J.-H. Evertse and K. Győry, *Unit equations in Diophantine number theory.*Cambridge Studies in Advanced Mathematics, 146. Cambridge University Press, Cambridge, 2015.
- [17] J.-H. Evertse, H. P. Schlickewei, and W. M. Schmidt, Linear equations in variables which lie in a multiplicative group. *Ann. of Math. (2)*155 (2002), no. 3, 807–836.
- [18] P. Gawrychowski, D. Krieger, N. Rampersad, and J. Shallit, Finding the growth rate of a regular or context-free language in polynomial time. *Internat. J. Found. Comput. Sci.*21 (2010), no. 4, 597–618.
- [19] S. Ginsburg and E. Spanier, Bounded regular sets. *Proc. Amer. Math. Soc.*17 (1966), 1043–1049.
- [20] P. Hieronymi, and C. Schulz, A strong version of Cobham’s theorem. *STOC ’22—Proceedings of the 54th Annual ACM SIGACT Symposium on Theory of Computing*, 1172–1179, ACM, New York, 2022.
- [21] G. Jirásková and T. Masopust, State complexity of projected languages. Descriptional complexity of formal systems, 198–211, *Lecture Notes in Comput. Sci.*, 6808, Springer, Heidelberg, 2011.
- [22] K. S. Kedlaya, Finite automata and algebraic extensions of function fields. *J. Théor. Nombres Bordeaux*18 (2006), no. 2, 379–420.
- [23] K. S. Kedlaya, On the algebraicity of generalized power series. *Beitr. Algebra Geom.*58 (2017), no. 3, 499–527.
- [24] T. J. P. Krebs, A more reasonable proof of Cobham’s theorem. *Internat. J. Found. Comput. Sci.*32 (2021), no. 2. 203–207.
- [25] C. Michaux and R. Villemaire, Presburger arithmetic and recognizability of sets of natural numbers by automata: new proofs of Cobham’s and Semenov’s theorems, *Ann. Pure Appl. Logic*77 (1996), no. 3, 251–277.
- [26] P. Mihăilescu, Primary cyclotomic units and a proof of Catalan’s conjecture. *J. Reine Angew. Math.*572 (2004), 167–195.
- [27] R. Moosa and T. Scanlon, F F -structures and integral points on semiabelian varieties over finite fields. *Amer. J. Math.*126 (2004), no. 3, 473–522.
- [28] R. Schäfke and M. Singer, Consistent systems of linear differential and difference equations. *J. Eur. Math. Soc. (JEMS)*21 (2019), no. 9, 2751–2792.
- [29] H. P. Schlickewei, S S -unit equations over number fields. *Invent. Math.*102 (1990), no. 1, 95–107.
- [30] A. L. Semenov, The Presburger nature of predicates that are regular in two number systems, *Sibirsk. Mat. Z̆.*18 (1977), no. 2, 403–418, 479.

[◄][3][image: ar5iv homepage] [4]
[Feeling lucky?][5] [6]
[Conversion report][7]
[Report an issue][8]
[View original on arXiv][9] [►][10]


## Links

[1]: mailto:gulizar.albayrak@ucalgary.ca
[2]: mailto:jpbell@uwaterloo.ca
[3]: /html/2304.09222
[4]: /
[5]: /feeling_lucky
[6]: /land_of_honey_and_milk
[7]: /log/2304.09223
[8]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2304.09223
[9]: https://arxiv.org/pdf/2304.09223
[10]: /html/2304.09224
