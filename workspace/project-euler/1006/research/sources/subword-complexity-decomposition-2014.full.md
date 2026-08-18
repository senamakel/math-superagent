<!-- source: https://ar5iv.labs.arxiv.org/html/1406.3974 | converted from HTML -->

[1406.3974] Subword complexity and decomposition of the set of factors

# Subword complexity and decomposition of the set of factors

Julien Cassaigne Affiliation: Aix-Marseille Université, France E-mail [cassaigne@iml.univ-mrs.fr, anna.e.frid@gmail.com][1] Anna E. Frid Affiliation: Aix-Marseille Université, France E-mail [cassaigne@iml.univ-mrs.fr, anna.e.frid@gmail.com][1] Affiliation: Sobolev Institute of Mathematics, Russia Svetlana Puzynina Affiliation: Department of Mathematics and Statistics, University of Turku, Finland E-mail [svepuz@utu.fi][2] Affiliation: Sobolev Institute of Mathematics, Russia Luca Q. Zamboni Affiliation: Department of Mathematics and Statistics, University of Turku, Finland E-mail [svepuz@utu.fi][2] Affiliation: Université de Lyon 1, France E-mail [zamboni@math.univ-lyon1.fr][3]

###### Abstract

In this paper we explore a new hierarchy of classes of languages and infinite words and its connection with complexity classes. Namely, we say that a language belongs to the class ℒ k \mathcal{L}_{k} if it is a subset of the catenation of k k languages S 1 ⋯ S k S_{1}\cdots S_{k}, where the number of words of length n n in each of S i S_{i} is bounded by a constant. The class of infinite words whose set of factors is in ℒ k \mathcal{L}_{k} is denoted by 𝒲 k \mathcal{W}_{k}. In this paper we focus on the relations between the classes 𝒲 k \mathcal{W}_{k} and the subword complexity of infinite words, which is as usual defined as the number of factors of the word of length n n. In particular, we prove that the class 𝒲 2 \mathcal{W}_{2} coincides with the class of infinite words of linear complexity. On the other hand, although the class 𝒲 k \mathcal{W}_{k} is included in the class of words of complexity O ⁡ ( n k − 1) O(n^{k-1}), this inclusion is strict for k > 2 k>2.

## 1 Preliminaries

The complexities of infinite words and languages is a widely studied area in formal languages theory. We follow the general approach where the complexity is measured as the number of fragments of a given size. Applied to words, it means that the complexity of a language L L (or an infinite word u u) is the function p L ​ ( n) p_{L}(n) (resp., p u ​ ( n) p_{u}(n)) counting the number of elements of L L (resp., factors of u u) of length n n. This function was introduced by Morse and Hedlund in 1938 [9] under the name *block growth*as a tool to study symbolic dynamical systems. The name *subword complexity*was given by Ehrenfeucht, Lee, and Rozenberg [4]; as the term “factor” replaces “subword”, the term “factor complexity” is more and more popular [3].

An infinite word is ultimately periodic if and only if its complexity is ultimately constant, and it is a classical result that the smallest complexity of aperiodic words is p ⁡ ( n) = n + 1 p(n)=n+1 [9]. The words of this complexity are called Sturmian and form a very interesting and well-explored family (see, e.g., Chapter 2 in [8]). Results on the complexity usually belong to one of the two families: they give either conditions or formulas on the complexity of words from given families (see, e.g., [10]), or conditions on words with given restrictions on the complexity. As an example of a complicated problem of that kind, we mention the S S -adic conjecture on words of linear complexity (see [7] and references therein). For a recent survey and deep results on subword complexity, see [3].

In the paper we relate the subword complexity to local conditions of factorization type. Namely, we are interested in the following question: What is the relation between the complexity of the word and the condition that each its factor can be decomposed into a product of a finite number k k of words belonging to a language of a bounded complexity? In a related paper [5] instead of languages of bounded complexity we considered the language of palindromes. Note that in both cases we need the language of factors to be a subset of the concatenation of these languages and not the concatenation itself. For another family of problems where the equality to the concatenation is needed, see e.g. [1, 6].

## 2 Classes and basic hierarchy

We consider finite and infinite words over a finite alphabet Σ \Sigma, i.e., finite or infinite sequences of elements from the set Σ \Sigma. A *factor*or a *subword*of an infinite word is any sequence of its consecutive letters. The factor u i ⋯ u j u_{i}\cdots u_{j} of an infinite word u = u 1 ⋯ u n ⋯ u=u_{1}\cdots u_{n}\cdots, with u k ∈ Σ u_{k}\in\Sigma, is denoted by u [i.. j] u[i..j]. As usual, the set of factors of a finite or infinite word u u is denoted by Fac ( u) (u). A factor s s of a right infinite word u u is called *right*(resp., *left*) *special*if s ​ a, s ​ b ∈ sa,sb\in Fac ( u) (u) (resp., a ​ s, b ​ s ∈ as,bs\in Fac ( u) (u)) for distinct letters a, b ∈ Σ a,b\in\Sigma. The length of a finite word s s is denoted by | s | |s|, and the number of occurrences of a letter a a in s s is denoted by | s | a |s|_{a}. The empty word is denoted ε \varepsilon and we define | ε | = 0 |\varepsilon|=0. An infinite word u = v w w w w ⋯ = v w ω u=vwwww\cdots=vw^{\omega} for some non-empty word w w is called ultimately ( | w | |w| -)periodic. In the paper we mostly follow the terminology and notation from [8].

Denote by 𝒫 ⁡ ( α) \mathcal{P}(\alpha) the set of infinite words of complexity O ⁡ ( n α) O(n^{\alpha}).

Let us introduce the classes ℒ k \mathcal{L}_{k} of languages and 𝒲 k \mathcal{W}_{k} of infinite words as follows: a language L L (infinite word u u) belongs to the class ℒ k \mathcal{L}_{k} (resp., 𝒲 k \mathcal{W}_{k}) if

 | L ⊆ S 1 ⋯ S k L\subseteq S_{1}\cdots S_{k} |  |

(resp., Fac ( u) ⊆ S 1 ⋯ S k (u)\subseteq S_{1}\cdots S_{k}) for some languages S i S_{i} with p S i ​ ( n) = O ​ ( 1) p_{S_{i}}(n)=O(1). In other words, u ∈ 𝒲 k u\in\mathcal{W}_{k} if and only if Fac ( u) ∈ ℒ k (u)\in\mathcal{L}_{k}, and the condition p S i ​ ( n) = O ​ ( 1) p_{S_{i}}(n)=O(1) means exactly that for some constant C C we have p S i ​ ( n) ≤ C p_{S_{i}}(n)\leq C for all n n. We also have 𝒫 ⁡ ( 0) = 𝒲 1 \mathcal{P}(0)=\mathcal{W}_{1}.

By a simple cardinality argument, we have the following inclusion:

###### Lemma 1

For each integer k > 0 k>0, we have 𝒲 k + 1 ⊆ 𝒫 ⁡ ( k) \mathcal{W}_{k+1}\subseteq\mathcal{P}(k).

Proof. Suppose a word u u is in 𝒲 k + 1 \mathcal{W}_{k+1} and consider the factors of length n n of u u. There is ( n + k k) = O ⁡ ( n k) {n+k\choose k}=O(n^{k}) ways to decompose a positive integer n n to k + 1 k+1 non-negative summands in a given order: n = n 1 + n 2 + … + n k + 1 n=n_{1}+n_{2}+\ldots+n_{k+1}. If the summand n i n_{i} is the length of the i i th factor in a decomposition of a word of length n n to k + 1 k+1 factors, and there are at most C C words of length n i n_{i} in the set S i S_{i}, it means that in total, there are not more than C k + 1 C^{k+1} decompositions of words corresponding to a given decomposition of n n. Taking all the factors of u u of length n n together, we see that they are not more than C k + 1 ​ ( n + k k) = O ⁡ ( n k) C^{k+1}{n+k\choose k}=O(n^{k}), which means exactly that u ∈ 𝒫 ⁡ ( k) u\in\mathcal{P}(k). □ \Box

###### Example 1

Now we are going to show that the Thue-Morse word t = 01101001 ⋯ t=01101001\cdots, defined as the fixed point starting with 0 of the morphism φ: 0 → 01, 1 → 10 \varphi:0\to 01,1\to 10, belongs to 𝒲 2 \mathcal{W}_{2}. For each n n the Thue-Morse word consists of words t n = φ n ​ ( 0) t_{n}=\varphi^{n}(0) and t n ¯ = φ n ​ ( 1) \overline{t_{n}}=\varphi^{n}(1), both of them of length 2 n 2^{n}: t = t n t n ¯ t n ¯ t n t n ¯ t n t n t n ¯ ⋯ t=t_{n}\overline{t_{n}}\overline{t_{n}}t_{n}\overline{t_{n}}t_{n}t_{n}\overline{t_{n}}\cdots. Defining S 1 S_{1} to be the set of suffixes of all t n t_{n} and t n ¯ \overline{t_{n}}, and S 2 S_{2} to be the set of their prefixes, we see that S 1 S_{1} and S 2 S_{2} contain exactly two words of length k k each. To cut each factor w w of t t, we just choose any of its occurrences and a position m m in it divided by the maximal power n n of 2 2: w = t [i.. j] = t [i.. m] t [m + 1.. j] w=t[i..j]=t[i..m]t[m+1..j]. By the definition of m m, t [i.. m] t[i..m] is a suffix of t n t_{n} or t n ¯ \overline{t_{n}}, and t [m + 1.. j] t[m+1..j] is a prefix of one of them, and thus, w ∈ S 1 ​ S 2 w\in S_{1}S_{2}. So, t ∈ 𝒲 2 t\in\mathcal{W}_{2}. This construction can be generalized to any fixed point of a primitive morphism but obviously not to fixed points whose complexity is higher than linear (see [10] for examples).

###### Example 2

Sturmian words, which can be defined as infinite words with complexity n + 1 n+1 for each n n, also belong to 𝒲 2 \mathcal{W}_{2}. These words have exactly one right and one left special factor of each length. One of the ways to construct the sets S 1 S_{1} and S 2 S_{2} for a Sturmian word s s is the following:

 | S 1 = { v a | a ∈ { 0, 1 }, v is a right special factor of s } ∪ { ε }, \displaystyle S_{1}=\{va|a\in\{0,1\},v\mbox{ is a right special factor of }s\}\cup\{\varepsilon\}, |  |

 | S 2 = { a v | a ∈ { 0, 1 }, v is a left special factor of s } ∪ { ε }. \displaystyle S_{2}=\{av|a\in\{0,1\},v\mbox{ is a left special factor of }s\}\cup\{\varepsilon\}. |  |

Remark that in fact the set S 2 S_{2} is the set of reversals of factors from S 1 S_{1}, and #​ S 1 ​ ( n) = #​ S 2 ​ ( n) = 2 \#S_{1}(n)=\#S_{2}(n)=2 for each n > 0 n>0. The fact that every factor of s s belongs to S 1 ​ S 2 S_{1}S_{2} follows from the properties of Sturmian words: it can be proved that every factor w w of s s has an occurrence [i.. j] [i..j] with i ≤ 0, j ≥ 0 i\leq 0,j\geq 0 in the biinfinite characteristic Sturmian word u u of s s, where either u = c R ​ 01 ​ c u=c^{R}01c or u = c R ​ 10 ​ c u=c^{R}10c, with c c the right infinite characteristic word (i.e., the infinite left special word).

Now let us introduce the accumulative complexity function g L ​ ( n) g_{L}(n) (resp., g u ​ ( n) g_{u}(n)) of a language L L (resp., a word u u) as

 | g L ​ ( n) = ∑ i = 1 n p L ​ ( n) ( resp., ​ g u ​ ( n) = ∑ i = 1 n p u ​ ( n)). g_{L}(n)=\sum_{i=1}^{n}p_{L}(n)\qquad(\mbox{resp., }g_{u}(n)=\sum_{i=1}^{n}p_{u}(n)). |  |

As above, we introduce the classes ℒ k ′ \mathcal{L}^{\prime}_{k} of languages and 𝒲 k ′ \mathcal{W}^{\prime}_{k} of infinite words as follows: a language L L (resp., infinite word u u) belongs to the class ℒ k ′ \mathcal{L}^{\prime}_{k} (resp., 𝒲 k ′ \mathcal{W}^{\prime}_{k}) if

 | L ⊆ S 1 ⋯ S k L\subseteq S_{1}\cdots S_{k} |  |

(resp., Fac ( u) ⊆ S 1 ⋯ S k (u)\subseteq S_{1}\cdots S_{k}) for some languages S i S_{i} with g S i ​ ( n) = O ​ ( n) g_{S_{i}}(n)=O(n).

As above, u ∈ 𝒲 k ′ u\in\mathcal{W}^{\prime}_{k} if and only if Fac ( u) ∈ ℒ k ′ (u)\in\mathcal{L}^{\prime}_{k}. The condition g S i ​ ( n) = O ​ ( n) g_{S_{i}}(n)=O(n) means exactly that for all n n we have g S i ​ ( n) ≤ K ​ n g_{S_{i}}(n)\leq Kn for some constant K K.

Clearly, ℒ k ⊆ ℒ k ′ \mathcal{L}_{k}\subseteq\mathcal{L}^{\prime}_{k}, since p S i ​ ( n) ≤ C p_{S_{i}}(n)\leq C for all n n implies g S i ​ ( n) ≤ C ​ n g_{S_{i}}(n)\leq Cn. As for an opposite inclusion, we can only can prove the following theorem and its corollary.

###### Theorem 2.1

ℒ 1 ′ ⊆ ℒ 2 \mathcal{L}^{\prime}_{1}\subseteq\mathcal{L}_{2}.

Proof. Consider a language L ∈ ℒ 1 ′ L\in\mathcal{L}^{\prime}_{1}, by definition this means that g L ​ ( n) ≤ K ​ n g_{L}(n)\leq Kn for some K K. We shall construct inductively the sets S S and T T of complexity p S ​ ( n), p T ​ ( n) ≤ 2 ​ K + 1 p_{S}(n),p_{T}(n)\leq 2K+1 such that L ⊆ S ​ T L\subseteq ST.

Let us order the elements of L L according to their length: L = { v 1, …, v n, … } L=\{v_{1},\ldots,v_{n},\ldots\} with | v n | ≤ | v n + 1 | |v_{n}|\leq|v_{n+1}|. The sets S S and T T are constructed inductively: we choose any S 1 = { s 1 } S_{1}=\{s_{1}\} and T 1 = { t 1 } T_{1}=\{t_{1}\} so that v 1 = s 1 ​ t 1 v_{1}=s_{1}t_{1} and then do as follows. Suppose that we constructed the sets S n − 1 S_{n-1} and T n − 1 T_{n-1} of cardinality less than or equal to n − 1 n-1 each so that { v 1, …, v n − 1 } ⊆ S n − 1 ​ T n − 1 \{v_{1},\ldots,v_{n-1}\}\subseteq S_{n-1}T_{n-1} and the number of words of each length l l in each of S n − 1, T n − 1 S_{n-1},T_{n-1} is bounded by 2 ​ K + 1 2K+1.

Consider the word v n v_{n} and denote its length by m m. It admits m + 1 m+1 factorizations v n = s ​ t v_{n}=st. If for a given factorization we have s ∈ S n − 1 s\in S_{n-1} and t ∈ T n − 1 t\in T_{n-1}, we do not need to add anything to these sets and can take S n = S n − 1 S_{n}=S_{n-1}, T n = T n − 1 T_{n}=T_{n-1}. If for example s ∉ S n − 1 s\notin S_{n-1}, we can construct S n S_{n} by adding s s to S n − 1 S_{n-1}: S n = S n − 1 ∪ { s } S_{n}=S_{n-1}\cup\{s\} if the words of length | s | |s| in S n − 1 S_{n-1} are at most 2 ​ K 2K (and symmetrically for T n − 1 T_{n-1}). But the number N N of lengths l l such that p S n − 1 ​ ( l) > 2 ​ K p_{S_{n-1}}(l)>2K (resp., p T n − 1 ​ ( l) > 2 ​ K p_{T_{n-1}}(l)>2K) and thus no more of words of length l l can be added to S n − 1 S_{n-1} (resp., T n − 1 T_{n-1}) is bounded by N ≤ ( n − 1) / ( 2 ​ K) N\leq(n-1)/(2K), since the total number of words in S n − 1 S_{n-1} (resp., T n − 1 T_{n-1}) is at most ( n − 1) (n-1).

So, to assure that at least one of m + 1 m+1 factorizations is admitted and we (if necessary) can add new words s n s_{n} and t n t_{n}: S n = S n − 1 ∪ { s n } S_{n}=S_{n-1}\cup\{s_{n}\}, T n = T n − 1 ∪ { t n } T_{n}=T_{n-1}\cup\{t_{n}\} such that v n = s n ​ t n v_{n}=s_{n}t_{n}, we should check that m + 1 > 2 ​ ( n − 1) / ( 2 ​ K) m+1>2(n-1)/(2K). But since m m is the length of the word number n n in L L, we have n ≤ g L ​ ( m) ≤ K ​ m n\leq g_{L}(m)\leq Km and thus 2 ​ ( n − 1) / ( 2 ​ K) ≤ ( 2 ​ K ​ m − 2) / ( 2 ​ K) < m + 1 2(n-1)/(2K)\leq(2Km-2)/(2K)<m+1, which was to be proved. □ \Box

###### Corollary 1

For each k > 0 k>0, we have ℒ k ′ ⊆ ℒ 2 ​ k \mathcal{L}^{\prime}_{k}\subseteq\mathcal{L}_{2k}.

Proof. Take a language L ∈ ℒ k ′ L\in\mathcal{L}^{\prime}_{k}: by the definition, L ⊆ S 1 ​ … ​ S k L\subseteq S_{1}\ldots S_{k} with S i ∈ ℒ 1 ′ S_{i}\in\mathcal{L}^{\prime}_{1} for all i i. Due to the theorem above, all S i ∈ ℒ 2 S_{i}\in\mathcal{L}_{2}, that is, S i ⊆ S i ( l) ​ S i ( r) S_{i}\subseteq S_{i}^{(l)}S_{i}^{(r)} where the complexities of S i ( l) S_{i}^{(l)}, S i ( r) S_{i}^{(r)} are bounded. Clearly, we have L ⊆ S 1 ( l) ​ S 1 ( r) ​ … ​ S k ( l) ​ S k ( r) L\subseteq S_{1}^{(l)}S_{1}^{(r)}\ldots S_{k}^{(l)}S_{k}^{(r)}, which proves the corollary. □ \Box

So, for all k > 0 k>0 we have ℒ k ⊆ ℒ k ′ ⊆ ℒ 2 ​ k \mathcal{L}_{k}\subseteq\mathcal{L}^{\prime}_{k}\subseteq\mathcal{L}_{2k} and thus 𝒲 k ⊆ 𝒲 k ′ ⊆ 𝒲 2 ​ k \mathcal{W}_{k}\subseteq\mathcal{W}^{\prime}_{k}\subseteq\mathcal{W}_{2k}.

## 3 Linear complexity and 𝒲 2 \mathcal{W}_{2}

In this section, we prove the main result of this paper, namely,

###### Theorem 3.1

An infinite word is of linear complexity if and only if its language of factors is a subset of the catenation of two languages of bounded complexity: 𝒲 2 = 𝒫 ⁡ ( 1) \mathcal{W}_{2}=\mathcal{P}(1).

The ⊆ \subseteq inclusion has been proven in Lemma 1. Since for periodic words the statement is obvious, it remains to find the languages S, T S,T of bounded complexity for a given infinite word u u of linear complexity p u ​ ( n) ≤ C ​ n p_{u}(n)\leq Cn such that the set of factors of u u is a subset of S ​ T ST.

The construction of the sets S S and T T is based on so-called markers which we define below.

### 3.1 Markers and classification of occurrences

Let u u be an infinite word. Given a length n n, we say that a subset M M of the set of factors of u u of length n n is a set of markers, or, more precisely, of D D -markers for a constant D D, if each factor of u u of length D ​ n Dn contains at least one word m ∈ M m\in M as a factor.

Recall that a factor v v of u u is called right special if v ​ a, v ​ b ∈ va,vb\in Fac ( u) (u) for at least two different symbols a, b a,b.

###### Lemma 2

The set of right special factors of u u of length n n is a set of ( C + 1) (C+1) -markers, where p u ​ ( n) ≤ C ​ n p_{u}(n)\leq Cn.

Proof. Consider a factor v v of u u of length ( C + 1) ​ n (C+1)n and suppose that none of its factors of length n n is right special. It means that each factor of v v of length n n, whenever it occurs in u u, uniquely determines the next factor of length n n, shifted by one letter. But there are C ​ n + 1 Cn+1 occurrences of factors of length n n in v v. So, at least two of them correspond to the same factor, and what happens after its second occurrence repeats what happens after the first one. So, the word u u is ultimately periodic, a contradiction. □ \Box

The number of right special factors of u u of length n n is uniformly bounded by a constant R R which is a polynomial of C C, where p u ​ ( n) ≤ C ​ n p_{u}(n)\leq Cn, due to a result of Cassaigne [2, 3]. Thus, we have the following

###### Corollary 2

For each length n n, there exists a set of cardinality R R of ( C + 1) (C+1) -markers of length n n in u u.

Remark that the set of right special factors is just one the possible ways to build the set of markers. For the proof below it does not matter how the set of markers was constructed, the only thing we use is that the set of markers of each length is bounded.

Consider a factor w = w 1 ⋯ w n w=w_{1}\cdots w_{n} of u u and denote by p ⁡ ( w) p(w) its minimal period, that is, the minimal positive integer such that w i = w i + p ⁡ ( w) w_{i}=w_{i+p(w)} for all i > 0 i>0 and i + p ⁡ ( w) ≤ n i+p(w)\leq n. The word w [1.. p ( w)] w[1..p(w)], also called the minimal period of w w, is denoted by P ⁡ ( w) P(w); each time it will be clear from the context whether the period means the word or the number.

An occurrence w = u [j + 1.. j + n] w=u[j+1..j+n] of w w in u u is called internal if two conditions hold. First, u j + p = u j + p − p ⁡ ( w) u_{j+p}=u_{j+p-p(w)} for all p p such that 1 ≤ p ≤ p ⁡ ( w) 1\leq p\leq p(w) and j + p − p ⁡ ( w) ≥ 1 j+p-p(w)\geq 1; second, symmetrically, u j + p = u j + p + p ⁡ ( w) u_{j+p}=u_{j+p+p(w)} for all p p such that n − p ⁡ ( w) + 1 ≤ p ≤ n n-p(w)+1\leq p\leq n. In other words, due to the definition of p ⁡ ( w) p(w), for an internal occurrence of w w in the infinite word u u we have u [j + p ( w) + 1.. j + p ( w) + n] = w u[j+p(w)+1..j+p(w)+n]=w and, provided that j ≥ p ⁡ ( w) j\geq p(w), u [j − p ( w) + 1.. j − p ( w) + n] = w u[j-p(w)+1..j-p(w)+n]=w.

An occurrence which is not internal is called extreme. More precisely, if u j + i ≠ u j + i − p ⁡ ( w) u_{j+i}\neq u_{j+i-p(w)} for some i i such that max ⁡ ( 1, p ⁡ ( w) − j + 1) ≤ i ≤ p ⁡ ( w) \max(1,p(w)-j+1)\leq i\leq p(w), it is called initial, and if u j + i ≠ u j + i + p ⁡ ( w) u_{j+i}\neq u_{j+i+p(w)} for some i i such that n − p ⁡ ( w) + 1 ≤ i ≤ n n-p(w)+1\leq i\leq n, it is called final. Clearly, an occurrence of a word in u u can be initial and final at the same time.

Since u u is not ultimately periodic, each its factor w w admits a final occurrence, otherwise u u would be ultimately p ⁡ ( w) p(w) -periodic.

### 3.2 Construction and proof

For each k ≥ 1 k\geq 1, consider the set of D D -markers of length 2 k 2^{k} whose cardinality is bounded by R R. Due to Corollary 2, such a set exists and we shall call its elements markers of order k k.

Consider a factor v v of length n ≥ 2 ​ D n\geq 2D of u u. Our goal is to construct two words s ∈ S s\in S and t ∈ T t\in T such that u = s ​ t u=st. By the definition of markers, v v contains a marker of order one; now consider the largest k k such that it contains a marker m m of order k k. Choose an occurrence of v v in u u: v = u [i + 1.. i + n] v=u[i+1..i+n]. If all occurrences of m m in u [i + 1.. i + n] u[i+1..i+n] are internal, take one of them (say, the first one). If not, choose an extreme occurrence of m m in u [i + 1.. i + n] u[i+1..i+n] (again, the first of them if they are several). In both cases, we denote the chosen occurrence m = u [j + 1.. j + 2 k] m=u[j+1..j+2^{k}]; here j ≥ i j\geq i and j + 2 k ≤ i + n j+2^{k}\leq i+n.

Now we define s = s ( v) = u [i + 1.. j + 2 k − 1] s=s(v)=u[i+1..j+2^{k-1}] and t = t ( v) = u [j + 2 k − 1 + 1.. i + n] t=t(v)=u[j+2^{k-1}+1..i+n]. Clearly, v = s ​ t v=st. Note that the marker m m is cut exactly in the middle of an occurrence: m = m l ​ m r m=m_{l}m_{r} with | m l | = | m r | = 2 k − 1 |m_{l}|=|m_{r}|=2^{k-1}. Here s s ends by m l m_{l} and t t starts with m r m_{r}.

At last, let us define

 | S \displaystyle S | = ( Fac ​ ( u) ∩ Σ < 2 ​ D) ∪ { s ⁡ ( v) | v ∈ ( Fac ​ ( u) ∩ Σ ≥ 2 ​ D) }, \displaystyle=(\mbox{Fac}(u)\cap\Sigma^{<2D})\cup\{s(v)|v\in(\mbox{Fac}(u)\cap\Sigma^{\geq 2D})\}, |  |

 | T \displaystyle T | = { ε } ∪ { t ⁡ ( v) | v ∈ ( Fac ​ ( u) ∩ Σ ≥ 2 ​ D) }, \displaystyle=\{\varepsilon\}\cup\{t(v)|v\in(\mbox{Fac}(u)\cap\Sigma^{\geq 2D})\}, |  |

where ε \varepsilon is the empty word, Σ < n = ⋃ k = 0 n − 1 Σ k \Sigma^{<n}=\bigcup_{k=0}^{n-1}\Sigma^{k} and Σ ≥ n = Σ ∗ \ Σ < n \Sigma^{\geq n}=\Sigma^{*}\backslash\Sigma^{<n}.

It follows immediately from the definitions that Fac ( u) ⊆ S ​ T (u)\subseteq ST. It remains to prove that the cardinalities of S ∩ Σ n S\cap\Sigma^{n} and T ∩ Σ n T\cap\Sigma^{n} are uniformly bounded.

Consider a length l ≥ 2 ​ D l\geq 2D. Let us count the words from T ∩ Σ l T\cap\Sigma^{l}.

What can be the length of a marker m m used to construct a word t ∈ T ∩ Σ l t\in T\cap\Sigma^{l}? It is equal to 2 k 2^{k}, where the word m r m_{r} of length 2 k − 1 2^{k-1} is a prefix of t t and thus 2 k − 1 ≤ l 2^{k-1}\leq l. On the other hand, since k k was chosen to be maximal and by the definition of D D, we have l < D ​ 2 k + 1 l<D2^{k+1}. These two inequalities can be rewritten as

 | l 2 ​ D < 2 k ≤ 2 ​ l, \frac{l}{2D}<2^{k}\leq 2l, |  | (1) |

which means that k k can take at most log 2 ⁡ D + 2 \log_{2}D+2 values for a given l l.

Since we use a construction with at most R R markers of each order k k, in total there are at most R ⁡ ( log 2 ⁡ D + 2) R(\log_{2}D+2) markers which are used to construct the words from T ∩ Σ l T\cap\Sigma^{l}. Exactly the same counting works for the words from S ∩ Σ l S\cap\Sigma^{l}. They can be a bit shorter with respect to k k in average, since we choose the first occurrence of a longest marker whenever we have a choice, and since the factor which we decompose can be close to the beginning of u u. However, the same bounds hold, and the same R ⁡ ( log 2 ⁡ D + 2) R(\log_{2}D+2) (or less) markers can be used to construct the words from S ∩ Σ l S\cap\Sigma^{l}.

Now let us consider separately the cases when the occurrence of a marker used for a decomposition is internal, initial or final.

###### Lemma 3

Consider an occurrence of a factor v v of length n ≥ 2 ​ D n\geq 2D in u u and a longest marker m m in it. If all the occurrences of m m to the chosen occurrence of v v are internal, then v v is p ⁡ ( m) p(m) -periodic.

Proof. Follows from the definition of an internal occurrence. □ \Box

Let us fix a length l ≥ 2 ​ D l\geq 2D. Clearly, for a given marker m m of a suitable length 2 k 2^{k}, there is exactly one possible word in Σ l \Sigma^{l} which can belong to T T because of internal occurrences of m m: It is p ⁡ ( m) p(m) -periodic and obtained from the prefix of length l + 2 k − 1 l+2^{k-1} of P ​ ( m) ω P(m)^{\omega} by deleting the first 2 k − 1 2^{k-1} symbols. Symmetrically, there is exactly one possible word in Σ l \Sigma^{l} which can belong to S S because of internal occurrences of m m.

It follows that for each l ≥ 2 ​ D l\geq 2D, each of at most R ⁡ ( log 2 ⁡ D + 2) R(\log_{2}D+2) possible markers for this length, its internal occurrences can give at most one word of length l l in T T and at most one word in S S. Now let us consider words arising from extreme occurrences.

For the sake of convenience, define a new symbol z ∉ Σ z\notin\Sigma and fix u n = z u_{n}=z for n ≤ 0 n\leq 0. So, instead of u u, we can now consider a bi-infinite word u ′ = ⋯ z z z u 1 u 2 u 3 ⋯ u^{\prime}=\cdots zzzu_{1}u_{2}u_{3}\cdots.

Let us fix a marker m m of length 2 k 2^{k} and a length l l satisfying ( 1) and consider the set T f ​ ( m, l) T_{f}(m,l) of words from T T of length l l arising from final occurrences of m m to u u. For any word t ∈ T f ​ ( m, l) t\in T_{f}(m,l) consider a place in u u which gives rise to it, that is, fix a position j ≥ 0 j\geq 0 such that m = u [j + 1.. j + 2 k] m=u[j+1..j+2^{k}] and t = u [j + 2 k − 1 + 1.. j + 2 k − 1 + l] t=u[j+2^{k-1}+1..j+2^{k-1}+l]. Now for each i i such that 0 ≤ i < 2 k − 1 0\leq i<2^{k-1} define the word e f ​ ( m, t, j, i) e_{f}(m,t,j,i) of length l + 2 k l+2^{k} as e f ( m, t, j, i) = u [j + 1 − i.. j + l + 2 k − i] e_{f}(m,t,j,i)=u[j+1-i..j+l+2^{k}-i] (see Fig. 1). Note that if j + 1 < 2 k j+1<2^{k}, the word e f ​ ( m, t, j, i) e_{f}(m,t,j,i) for sufficiently large i i -s starts with one or several (but not more than 2 k − 1 − 1 2^{k-1}-1) symbols z z.

Figure 1: Construction of e f ​ ( m, t, j, i) e_{f}(m,t,j,i)

###### Lemma 4

If e f ​ ( m, t, j, i) = e f ​ ( m, t ′, j ′, i ′) e_{f}(m,t,j,i)=e_{f}(m,t^{\prime},j^{\prime},i^{\prime}) with | t | = | t ′ | = l |t|=|t^{\prime}|=l, then t = t ′ t=t^{\prime} and i = i ′ i=i^{\prime}.

Proof. Denote e f ​ ( m, t, j, i) = e f ​ ( m, t ′, j ′, i ′) = e e_{f}(m,t,j,i)=e_{f}(m,t^{\prime},j^{\prime},i^{\prime})=e. Note also that k k can be uniquely reconstructed from m m.

Suppose that i = i ′ i=i^{\prime}; then t = t ′ = e [i + 2 k − 1 + 1.. i + 2 k − 1 + l] t=t^{\prime}=e[i+2^{k-1}+1..i+2^{k-1}+l].

Suppose that i < i ′ i<i^{\prime}. Then the word e [i + 1.. i ′ + 2 k] e[i+1..i^{\prime}+2^{k}] has m m as a prefix and a suffix and thus is ( i ′ − i) (i^{\prime}-i) -periodic. In particular, m m is ( i ′ − i) (i^{\prime}-i) -periodic. Since p ⁡ ( m) p(m) is the minimal period of m m, we have p ⁡ ( m) ≤ i ′ − i < 2 k − 1 = | m | / 2 p(m)\leq i^{\prime}-i<2^{k-1}=|m|/2. So, for each h = 1, …, 2 k − p ⁡ ( m) + i ′ − i h=1,\ldots,2^{k}-p(m)+i^{\prime}-i both symbols e i + h e_{i+h} and e i + h + p ⁡ ( m) e_{i+h+p(m)} belong to either the prefix copy of m m or to the suffix copy of m m (or to both). So, e i + h = e i + h + p ⁡ ( m) e_{i+h}=e_{i+h+p(m)} for all h h from 1 to 2 k − p ⁡ ( m) + i ′ − i ≥ 2 k 2^{k}-p(m)+i^{\prime}-i\geq 2^{k}, and in particular for all h h such that 2 k − p ⁡ ( m) + 1 ≤ h ≤ 2 k 2^{k}-p(m)+1\leq h\leq 2^{k}. This contradicts to the fact that u [j + 1.. j + 2 k] = e [i + 1.. i + 2 k] u[j+1..j+2^{k}]=e[i+1..i+2^{k}] is a final occurrence of m m to u u. □ \Box

So, the number of possible words e f ​ ( m, t, j, i) e_{f}(m,t,j,i) for a given marker m m and a given length l l of t t is minorized by the number of pairs ( t, i) (t,i); here t t is a word from T ∩ Σ l T\cap\Sigma^{l} arising from a final occurrence of a marker m m, and for each m m, t t and j j, the parameter i i takes exactly 2 k − 1 2^{k-1} values. On the other hand, all e f ​ ( m, t, j, i) e_{f}(m,t,j,i) are words of length l + 2 k l+2^{k}, which are either factors of u u or its prefixes preceded by at most 2 k − 1 2^{k-1} new symbols z z: the number of factors of u u of length l + 2 k l+2^{k} is p u ​ ( l + 2 k) p_{u}(l+2^{k}), the number of words with z z is at most 2 k − 1 2^{k-1}, and the number of words e f ​ ( m, t, j, i) e_{f}(m,t,j,i) is majorized by p u ​ ( l + 2 k) + 2 k − 1 ≤ C ⁡ ( l + 2 k) + 2 k − 1 p_{u}(l+2^{k})+2^{k-1}\leq C(l+2^{k})+2^{k-1}. So, we have

 | 2 k − 1 ​ t f ​ ( m, l) ≤ C ⁡ ( l + 2 k) + 2 k − 1, 2^{k-1}t_{f}(m,l)\leq C(l+2^{k})+2^{k-1}, |  |

where t f ​ ( m, l) t_{f}(m,l) is the contribution to T ∩ Σ l T\cap\Sigma^{l} of all the final occurrences of a marker m m of length 2 k 2^{k}.

Since l < 2 k + 1 ​ D l<2^{k+1}D, the latter inequality can be rewritten as

 | t f ​ ( m, l) < C ⁡ ( 2 ​ D + 1) ​ 2 k + 2 k − 1 2 k − 1 = 2 ​ C ​ ( 2 ​ D + 1) + 1. t_{f}(m,l)<\frac{C(2D+1)2^{k}+2^{k-1}}{2^{k-1}}=2C(2D+1)+1. |  |

In other words,

 | t f ​ ( m, l) ≤ 2 ​ C ​ ( 2 ​ D + 1). t_{f}(m,l)\leq 2C(2D+1). |  |

Exactly the same upper bound can be symmetrically proved for the contribution to T ∩ Σ l T\cap\Sigma^{l} of initial occurrences of a marker m m: t i ​ ( m, l) ≤ 2 ​ C ​ ( 2 ​ D + 1) t_{i}(m,l)\leq 2C(2D+1). So, each of R ⁡ ( log 2 ⁡ D + 2) R(\log_{2}D+2) possible markers for the length l l can contribute at most for the following number of words to T ∩ Σ l T\cap\Sigma^{l}: one word arising from its internal occurrences, plus 2 ​ C ​ ( 2 ​ D + 1) 2C(2D+1) words arising from final occurrences, plus 2 ​ C ​ ( 2 ​ D + 1) 2C(2D+1) words arising from initial occurrences. This gives the desired upper bound: the total number of words in the set T ∩ Σ l T\cap\Sigma^{l} is bounded by the constant

 | R ⁡ ( log 2 ⁡ D + 2) ​ [1 + 4 ​ C ​ ( 2 ​ D + 1)]. R(\log_{2}D+2)[1+4C(2D+1)]. |  |

The proof for S ∩ Σ l S\cap\Sigma^{l} is similar and gives the same constant as the upper bound. □ \Box

Note that the analogous fact for general languages is not true: there exists a language of linear complexity not belonging to any ℒ k \mathcal{L}_{k}. However, this language (which we do not describe here because of the lack of space) is not closed under taking a factor.

## 4 Word of quadratic complexity

Lemma 1 and Theorem 3.1 imply that 𝒲 2 = 𝒫 ⁡ ( 1) \mathcal{W}_{2}=\mathcal{P}(1), and in general 𝒲 k + 1 ⊆ 𝒫 ⁡ ( k) \mathcal{W}_{k+1}\subseteq\mathcal{P}(k) for all k k. So, the following natural question arises: is it true that 𝒲 k + 1 = 𝒫 ⁡ ( k) \mathcal{W}_{k+1}=\mathcal{P}(k) for all k k?

The answer is negative, and, since 𝒲 k ⊆ 𝒲 k ′ \mathcal{W}_{k}\subseteq\mathcal{W}^{\prime}_{k}, to show it we just point an example of a word of quadratic complexity which does not belong to 𝒲 3 ′ \mathcal{W}^{\prime}_{3}.

Consider the word u = a b a b b a b b b ⋯ = ∏ i = 1 ∞ a b k u=ababbabbb\cdots=\prod_{i=1}^{\infty}ab^{k}. Its complexity p u ​ ( n) = Θ ⁡ ( n 2) p_{u}(n)=\Theta(n^{2}): this can be either proved directly or derived from the famous paper by Pansiot [10], since u u is obtained by erasing the first letter c c from the fixed point starting with c c of the morphism c ↦ c ​ a ​ b, a ↦ a ​ b, b ↦ b c\mapsto cab,a\mapsto ab,b\mapsto b.

###### Lemma 5

The word u u does not belong to 𝒲 3 ′ \mathcal{W}^{\prime}_{3}.

Proof. Suppose the opposite: Fac ( u) ⊆ X ​ Y ​ Z (u)\subseteq XYZ with g X ​ ( n), g Y ​ ( n), g Z ​ ( n) = O ⁡ ( n) g_{X}(n),g_{Y}(n),g_{Z}(n)=O(n). Now for each word v ∈ v\in Fac ( u) (u) of length at most n n fix some its decomposition v = x ⁡ ( v) ​ y ​ ( v) ​ z ​ ( v) = x ​ y ​ z v=x(v)y(v)z(v)=xyz with x ∈ X x\in X, y ∈ Y y\in Y, z ∈ Z z\in Z. We shall estimate the number of words v v which can be decomposed like that.

Now for each k, l > 0 k,l>0 define the word w k, l = a b l a b l + 1 ⋯ a b l + k − 1 a w_{k,l}=ab^{l}ab^{l+1}\cdots ab^{l+k-1}a. Clearly, w k, l w_{k,l} is a factor of u u of length k ⁡ ( l + ( k + 1) / 2) + 1 k(l+(k+1)/2)+1.

###### Claim

Let E ⁡ ( n) E(n) be the set of pairs ( k, l) (k,l) such that | w k, l | ≤ n |w_{k,l}|\leq n, k ≥ 3 k\geq 3 and l ≥ n l\geq\sqrt{n}. Then #​ E ​ ( n) = Θ ⁡ ( n ​ log ⁡ n) \#E(n)=\Theta(n\log n).

Proof. Note that the condition | w k, l | = k ⁡ ( l + ( k + 1) / 2) + 1 ≤ n |w_{k,l}|=k(l+(k+1)/2)+1\leq n implies the inequality l ≤ n − 1 k − k + 1 2 \displaystyle l\leq\frac{n-1}{k}-\frac{k+1}{2}. So,

 | #​ E ​ ( n) = ∑ k = 3 ∞ #⁡ { l ∈ ℕ: n ≤ l ≤ n − 1 k − k + 1 2 }. \#E(n)=\sum_{k=3}^{\infty}\#\left\{l\in\mathbb{N}:\sqrt{n}\leq l\leq\frac{n-1}{k}-\frac{k+1}{2}\right\}. |  |

Observe that this set is empty for k ≥ 2 ​ n k\geq\sqrt{2n}: indeed, if k ≥ 2 ​ n k\geq\sqrt{2n}, then n − 1 k − k + 1 2 ≤ n 2 ​ n − 2 ​ n + 1 2 < 0 \displaystyle\frac{n-1}{k}-\frac{k+1}{2}\leq\frac{n}{\sqrt{2n}}-\frac{\sqrt{2n}+1}{2}<0. So,

 | #​ E ​ ( n) = ∑ k = 3 ⌊ 2 ​ n ⌋ ( n − 1 k − k + 1 2 − n + 1). \#E(n)=\sum_{k=3}^{\lfloor\sqrt{2n}\rfloor}\left(\frac{n-1}{k}-\frac{k+1}{2}-\sqrt{n}+1\right). |  |

Here

 | ∑ k = 3 ⌊ 2 ​ n ⌋ n − 1 k = ( n − 1) ​ ∑ k = 3 ⌊ 2 ​ n ⌋ 1 k = Θ ⁡ ( n ​ ln ⁡ n) \sum_{k=3}^{\lfloor\sqrt{2n}\rfloor}\frac{n-1}{k}=(n-1)\sum_{k=3}^{\lfloor\sqrt{2n}\rfloor}\frac{1}{k}=\Theta\left(n\ln n\right) |  |

and

 | ∑ k = 3 ⌊ 2 ​ n ⌋ ( k + 1 2 + n − 1) = Θ ⁡ ( n). \sum_{k=3}^{\lfloor\sqrt{2n}\rfloor}\left(\frac{k+1}{2}+\sqrt{n}-1\right)=\Theta(n). |  |

The claim follows. □ \Box

Let us say that a factor v v of u u is of type ( k, l) (k,l) if v = b i ​ w k, l ​ b j v=b^{i}w_{k,l}b^{j} for some i i and j j. Clearly, each factor of u u either is of some type ( k, l) (k,l), or contains at most one letter a a.

Denote by F ⁡ ( n) F(n) the set of pairs ( k, l) (k,l) with k ≥ 3 k\geq 3 and l ≥ n l\geq\sqrt{n} such that there exists a factor v v of u u of length at most n n and of type ( k, l) (k,l) whose decomposition is x ​ y ​ z xyz with | x | a ≤ 1 |x|_{a}\leq 1, | z | a ≤ 1 |z|_{a}\leq 1. There were k + 1 ≥ 4 k+1\geq 4 letters a a in v v, and at least k − 1 ≥ 2 k-1\geq 2 of them stay in the word y y. The type of y y is thus one of the four following: ( k, l) (k,l), ( k − 1, l + 1) (k-1,l+1), ( k − 1, l) (k-1,l), ( k − 2, l + 1) (k-2,l+1). But the total number of words in Y Y of length at most n n is g Y ​ ( n) = O ​ ( n) g_{Y}(n)=O(n), and each word y y can give rise to at most four types from F ⁡ ( n) F(n). So, #​ F ​ ( n) ≤ 4 ​ g Y ​ ( n) = O ⁡ ( n) \#F(n)\leq 4g_{Y}(n)=O(n), and due to the previous claim, there are still #​ E ​ ( n) \ F ⁡ ( n) = Θ ⁡ ( n ​ log ⁡ n) \#E(n)\backslash F(n)=\Theta(n\log n) pairs ( k, l) (k,l) with k ≥ 3 k\geq 3 and l ≥ n l\geq\sqrt{n} such that each word v v of type ( k, l) (k,l) and of length at most n n is decomposed so that its middle part y ⁡ ( v) y(v) contains at most one letter a a. Since there are k + 1 ≥ 4 k+1\geq 4 letters a a in v v, we see that either x ⁡ ( v) x(v) or z ⁡ ( v) z(v) contains at least two letters a a.

We denote this set of pairs by H ⁡ ( n) = E ⁡ ( n) \ F ⁡ ( n) H(n)=E(n)\backslash F(n). The number of all factors v v of u u whose types are in H ⁡ ( n) H(n) is denoted by s ⁡ ( n) s(n).

Consider a factor v v of u u of length at most n n whose type is in H ⁡ ( n) H(n). Suppose first that the word x ⁡ ( v) x(v) contains more than one letter a a. Then the word v v is uniquely determined by x ⁡ ( v) x(v) and the length | v | ≤ n |v|\leq n. So, the number of words v v of length ≤ n \leq n admitting such a decomposition is bounded by n ​ g X ​ ( n) = O ⁡ ( n 2) ng_{X}(n)=O(n^{2}).

Symmetrically, the number of words v v such that z ⁡ ( v) z(v) contains more than one letter a a is bounded by n ​ g Z ​ ( n) = O ⁡ ( n 2) ng_{Z}(n)=O(n^{2}).

So, the number s ⁡ ( n) s(n) of words whose types are in H ⁡ ( n) H(n) is O ⁡ ( n 2) O(n^{2}). But on the other hand, the number of types in H ⁡ ( n) H(n) is Θ ⁡ ( n ​ log ⁡ n) \Theta(n\log n), and for each type ( k, l) (k,l), the number of words of this type is l ⁡ ( l + k + 1) l(l+k+1): indeed, such a word is of the form b i ​ w k, l ​ b j b^{i}w_{k,l}b^{j}, where i i can take l l values from 0 to l − 1 l-1 and j j can take l + k + 1 l+k+1 values from 0 to l + k l+k. Since we restricted ourselves to the case of l ≥ n l\geq\sqrt{n}, the number of words of each type is l ⁡ ( l + k + 1) > n l(l+k+1)>n. In total, we have that s ⁡ ( n) ≥ n ​ Θ ​ ( n ​ log ⁡ n) s(n)\geq n\Theta(n\log n), that is,

 | s ⁡ ( n) = Ω ⁡ ( n 2 ​ log ⁡ n). s(n)=\Omega(n^{2}\log n). |  |

A contradiction to the previous condition s ⁡ ( n) = O ⁡ ( n 2) s(n)=O(n^{2}). □ \Box

Since 𝒲 3 ⊆ 𝒲 3 ′ \mathcal{W}_{3}\subseteq\mathcal{W}^{\prime}_{3}, we get also the following

###### Corollary 3

There exists a word of quadratic complexity which does not belong to 𝒲 3 \mathcal{W}_{3}.

## 5 Belonging to some 𝒲 k \mathcal{W}_{k}

The word u u of quadratic complexity considered in the previous section does not belong to 𝒲 3 ′ \mathcal{W}^{\prime}_{3}, but it can be proved that it belongs to 𝒲 4 ′ \mathcal{W}^{\prime}_{4}. We omit this proof here since it does not add much to the theory. However, this result suggests the following question: given a word of complexity majorated by a polynomial, is it true that it belongs to 𝒲 k \mathcal{W}_{k} for some k k?

As we show in the next proposition, the answer to this question is negative.

###### Proposition 1

For any growing integer function f ⁡ ( n) f(n) such that f ⁡ ( 1) ≥ 1 f(1)\geq 1, f ⁡ ( n) ≤ n f(n)\leq n and f ⁡ ( n) → ∞ f(n)\to\infty, there exists an infinite word w w of complexity O ⁡ ( n 2 ​ f ​ ( n)) O(n^{2}f(n)) which does not belong to 𝒲 k \mathcal{W}_{k} for any k k.

Proof. First we describe the construction of the word w w, then we prove that w w does not belong to 𝒲 k \mathcal{W}_{k} for any k k, and after that we prove that the word has complexity O ⁡ ( n 2 ​ f ​ ( n)) O(n^{2}f(n)).

Define the infinite word w w as follows:

 | w = ∏ p = 1 ∞ ∏ q = 1 f ⁡ ( p) ( a p ​ b q) k ⁡ ( p, q), w=\prod_{p=1}^{\infty}\prod_{q=1}^{f(p)}(a^{p}b^{q})^{k(p,q)}, |  |

where k ⁡ ( p, q) k(p,q) is a growing function: k ⁡ ( p, q) ≤ k ⁡ ( p, q + 1) k(p,q)\leq k(p,q+1) and k ⁡ ( p, f ⁡ ( p)) ≤ k ⁡ ( p + 1, 1) k(p,f(p))\leq k(p+1,1) for all p p and q q.

Let us prove that w ∉ 𝒲 k w\notin\mathcal{W}_{k} for any k k. Suppose by contrary that w ∈ 𝒲 k w\in\mathcal{W}_{k}: Fac ( w) ⊆ S 1 ⋯ S k (w)\subseteq S_{1}\cdots S_{k} with p S i ​ ( n) ≤ M i p_{S_{i}}(n)\leq M_{i} for all i i. Define S = ∪ i S i S=\cup_{i}S_{i}; then p S ​ ( n) ≤ ∑ i p S i ​ ( n) ≤ ∑ i M i = M p_{S}(n)\leq\sum_{i}p_{S_{i}}(n)\leq\sum_{i}M_{i}=M for an appropriate constant M M. Consequently, g S ​ ( n) ≤ M ​ n g_{S}(n)\leq Mn for all n n.

###### Claim

For every pair of integers ( p, q) (p,q), such that p + q < n − 2 2 ​ k − 1 p+q<\frac{n-2}{2k-1}, q ≤ f ⁡ ( p) q\leq f(p) and k ⁡ ( p, q) ≥ 2 ​ k − 1 k(p,q)\geq 2k-1, there exists a word s p, q ∈ S s_{p,q}\in S, | s p, q | ≤ n |s_{p,q}|\leq n, such that s p, q s_{p,q} contains b ​ a p ​ b q ​ a ba^{p}b^{q}a as a factor, and all those words s p, q s_{p,q} are distinct.

Proof. Consider the word b ​ ( a p ​ b q) 2 ​ k − 1 ​ a b(a^{p}b^{q})^{2k-1}a. Since k ⁡ ( p, q) ≥ 2 ​ k − 1 k(p,q)\geq 2k-1 and q ≤ f ⁡ ( p) q\leq f(p), it is a factor of w w, and since p + q < n − 2 2 ​ k − 1 p+q<\frac{n-2}{2k-1}, its length is at most n n. However we cut the word b ​ ( a p ​ b q) 2 ​ k − 1 ​ a b(a^{p}b^{q})^{2k-1}a into at most k k pieces, at least one piece will contain b ​ a p ​ b q ​ a ba^{p}b^{q}a as a factor. The claim follows. □ \Box

Let us estimate the number of words b ​ a p ​ b q ​ a ba^{p}b^{q}a for p + q < n − 2 2 ​ k − 1 p+q<\frac{n-2}{2k-1}, q ≤ f ⁡ ( p) q\leq f(p) and k ⁡ ( p, q) ≥ 2 ​ k − 1 k(p,q)\geq 2k-1. Since the function k ⁡ ( p, q) k(p,q) is growing, there exists a constant p k p_{k} such that k ⁡ ( p, q) ≥ 2 ​ k − 1 k(p,q)\geq 2k-1 for all p ≥ p k p\geq p_{k} and all q ≤ f ⁡ ( p) q\leq f(p). Since f ⁡ ( p) ≤ p f(p)\leq p for all p p, we have p + q ≤ p + f ⁡ ( p) ≤ 2 ​ p p+q\leq p+f(p)\leq 2p, and thus the number of pairs ( p, q) (p,q) is bounded from below by the sum ∑ p = p k n − 2 2 ​ ( 2 ​ k − 1) f ⁡ ( p) \displaystyle\sum_{p=p_{k}}^{\frac{n-2}{2(2k-1)}}f(p). Since f ⁡ ( p) → ∞ f(p)\to\infty with p p, and since g S ​ ( n) g_{S}(n) is bounded from below by the number of pairs ( p, q) (p,q) due to Claim Claim, we have

 | g S ​ ( n) ≥ ∑ p = p k n − 2 2 ​ ( 2 ​ k − 1) f ⁡ ( p) > M ​ n g_{S}(n)\geq\sum_{p=p_{k}}^{\frac{n-2}{2(2k-1)}}f(p)>Mn |  |

for some sufficiently large n n. A contradiction to the fact that g S ​ ( n) ≤ M ​ n g_{S}(n)\leq Mn.

Now let us check that the complexity of the word w w is O ⁡ ( n 2 ​ f ​ ( n)) O(n^{2}f(n)). The word w w contains factors of the following types:

1. 1.

Factors of a block ( a p ​ b q) k (a^{p}b^{q})^{k} for some p p, q q and k k.

2. 2.

Factors of a concatenation of blocks ( a p ​ b q) k 1 ​ ( a p ​ b q + 1) k 2 (a^{p}b^{q})^{k_{1}}(a^{p}b^{q+1})^{k_{2}}.

3. 3.

Factors of a concatenation of blocks ( a p ​ b f ⁡ ( p)) k 1 ​ ( a p + 1 ​ b) k 2 (a^{p}b^{f(p)})^{k_{1}}(a^{p+1}b)^{k_{2}}.

4. 4.

Factors containing some complete block ( a p ​ b q) k p, q (a^{p}b^{q})^{k_{p,q}} as a factor.

Remark that some of these families intersect, but this is not a problem since we only need a bound. So, let us estimate the number of words of length n n in each family.

In the family 1, we have O ⁡ ( n) O(n) words of the form a i ​ b n − i a^{i}b^{n-i} or b i ​ a n − i b^{i}a^{n-i}, plus O ⁡ ( n 2) O(n^{2}) words of the form a i ​ b q ​ a n − q − i a^{i}b^{q}a^{n-q-i} (uniquely determined by 0 < i, q < n 0<i,q<n) or b i ​ a p ​ b n − p − i b^{i}a^{p}b^{n-p-i} (uniquely determined by 0 < i, p < n 0<i,p<n), plus words containing a factor b ​ a p ​ b q ​ a ba^{p}b^{q}a or a ​ b q ​ a p ​ b ab^{q}a^{p}b. The latter words are uniquely determined by p < n p<n, q ≤ f ⁡ ( p) q\leq f(p) and the position of the first occurrence of a p a^{p}, which takes values from 0 to p + q < n p+q<n. So, the number of such words (and thus of all the words in family 1) is O ⁡ ( n 2 ​ f ​ ( n)) O(n^{2}f(n)).

Treating the other three families analogously, we see that the complexity of each of them is at most O ⁡ ( n 2 ​ f ​ ( n)) O(n^{2}f(n)) too. So, the complexity p w ​ ( n) = O ⁡ ( n 2 ​ f ​ ( n)) p_{w}(n)=O(n^{2}f(n)), which completes the proof. □ \Box

## 6 Conclusion

We finalize this paper by suggesting the following open problem: What is the minimal possible complexity of a word which does not belong to any 𝒲 k \mathcal{W}_{k}?

Remark that Theorem 3.1 and Proposition 1 imply that this complexity is strictly bigger than linear and is at most quadratic.

Supported in part by RFBR grants 12-01-00089 and 12-01-00448, as well as by the Academy of Finland grant 251371.

## References

- [1] S. V. Avgustinovich, A. E. Frid. A unique decomposition theorem for factorial languages. Int. J. Alg. Comput. 15 (2005) 149–160.
- [2] J. Cassaigne. Special factors of sequences with linear subword complexity. DLT 1995, 25–34, World Sci. Publishing, Singapore, 1996.
- [3] J. Cassaigne, F. Nicolas. Factor complexity. Combinatorics, automata and number theory, 163–247, Encyclopedia Math. Appl., 135, Cambridge Univ. Press, 2010.
- [4] A. Ehrenfeucht, K.P. Lee, G. Rozenberg. Subword complexities of various deterministic developmental languages without interactions. Theoret. Comput. Sci. 1 (1975) 59-76.
- [5] A. Frid, S. Puzynina, L. Q. Zamboni. On palindromic factorization of words. Advances in Applied Mathematics 50 (2013) 737–748.
- [6] Y.-S. Han, K. Salomaa, D. Wood. Prime Decompositions of Regular Languages. Proc. DLT 2006, LNCS 4036 (2006) 145–155.
- [7] Leroy, J. Some improvements of the S -adic conjecture. Adv. in Appl. Math. 48 (2012), no. 1, 79–98.
- [8] Lothaire, M.: Algebraic combinatorics on words. Cambridge University Press, 2002.
- [9] M. Morse and G. Hedlund, Symbolic dynamics, Amer. J. Math. 60 (1938), 815–866.
- [10] Pansiot, J.J.: Complexité des facteurs des mots infinis engendrés par morphismes itérés. In: Paredaens, J. (ed.) ICALP 1984. LNCS, vol. 172, pp. 380–389. Springer, Heidelberg (1984)

[◄][4][image: ar5iv homepage] [5]
[Feeling lucky?][6] [7]
[Conversion report][8]
[Report an issue][9]
[View original on arXiv][10] [►][11]


## Links

[1]: mailto:cassaigne@iml.univ-mrs.fr,%20anna.e.frid@gmail.com
[2]: mailto:svepuz@utu.fi
[3]: mailto:zamboni@math.univ-lyon1.fr
[4]: /html/1406.3973
[5]: /
[6]: /feeling_lucky
[7]: /land_of_honey_and_milk
[8]: /log/1406.3974
[9]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1406.3974
[10]: https://arxiv.org/pdf/1406.3974
[11]: /html/1406.3975
