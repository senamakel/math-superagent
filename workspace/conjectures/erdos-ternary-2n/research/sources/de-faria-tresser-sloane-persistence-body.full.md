<!-- source: https://ar5iv.labs.arxiv.org/html/1307.1188 | converted from HTML -->

[1307.1188] On Sloane’s persistence problem

# On Sloane’s persistence problem Thanks: This work has been supported by “Projeto Temático Dinâmica em Baixas Dimensões” FAPESP Grant 2011/16265-2, and by FAPESP Grant 2012/19995-0

Edson de Faria Address: Instituto de Matemática e Estatística, Universidade de São Paulo Current address: Rua do Matão 1010, 05508-090, São Paulo SP, Brasil Email address: [edson@ime.usp.br][1] and Charles Tresser Address: IBM, P.O. Box 218 Current address: Yorktown Heights, NY 10598, USA Email address: [charlestresser@yahoo.com][2]

###### Abstract.

We investigate the so-called persistence problem of Sloane, exploiting connections with the dynamics of circle maps and the ergodic theory of ℤ d \mathbb{Z}^{d} actions. We also formulate a conjecture concerning the asymptotic distribution of digits in long products of finitely many primes whose truth would, in particular, solve the persistence problem. The heuristics that we propose to complement our numerical studies can be thought in terms of a simple model in statistical mechanics.

###### Key words and phrases:

Persistence, circle maps, ergodic ℤ d \mathbb{Z}^{d} -actions

###### 2010 Mathematics Subject Classification

Primary 37E10; Secondary 37A45, 37A15, 11K16.

## 1. Introduction

In [S], Sloane proposed the following curious problem. Take a non-negative integer, write down its decimal representation, and multiply its digits together, getting a new non-negative integer. Repeat the process until a single-digit number is obtained. The problem can thus be stated: Is the number of steps taken in this process uniformly bounded?

### 1.1. General formulation

Let us start with a general formulation of Sloane’s problem, while at the same time introducing some of the notation that we will use. Given a natural number n n, and an integer base q > 1 q>1, consider the base- q q expansion of the number n n, say

(1) |  | n = [d 1 d 2 ⋯ d k] q = ∑ j = 1 k d j q k − j, n\;=\;\left[d_{1}d_{2}\cdots d_{k}\right]_{q}\;=\;\sum_{j=1}^{k}d_{j}q^{k-j}\ , |  |

where each digit d j ∈ { 0, 1, …, q − 1 } d_{j}\in\{0,1,\dots,q-1\} (and d 1 ≠ 0 d_{1}\neq 0 when n ≥ 1 n\geq 1). Let S q ​ ( n) S_{q}(n) denote the product of all such digits, i.e.,

 | S q ​ ( n) = ∏ j = 1 k d j. S_{q}(n)\;=\;\prod_{j=1}^{k}d_{j}\ . |  |

Thus n ↦ S q ​ ( n) n\mapsto S_{q}(n) defines a map S q: ℤ + → ℤ + S_{q}:\mathbb{Z}^{+}\to\mathbb{Z}^{+}, which we call the Sloane map in base q q. Clearly, such map can be iterated: write S q ​ ( n) S_{q}(n) in base q q, multiply its digits to obtain S q ​ ( S q ​ ( n)) S_{q}(S_{q}(n)), and so on. In particular, given any n ∈ ℤ + n\in\mathbb{Z}^{+} we can consider its orbit under the Sloane map, namely

 | n, S q ​ ( n), S q 2 ​ ( n), …, S q m ​ ( n), … n\,,\,S_{q}(n)\,,\,S_{q}^{2}(n)\,,\,\ldots\,,\,S_{q}^{m}(n)\,,\,\ldots |  |

The following proposition ensures that this sequence always stabilizes after a finite number of steps.

###### Proposition 1.

We have S q ​ ( n) < n S_{q}(n)<n for all n ≥ q n\geq q (i.e., as long as the base q q expansion of n n has at least two digits).

###### Proof.

Write n n in base q q as in ( 1), and note that k > 1 k>1. Since d j ≤ q − 1 d_{j}\leq q-1 for all j j, it follows that

 | S q ​ ( n) = d 1 ⋅ ∏ j = 2 k d j ≤ d 1 ⋅ ( q − 1) k − 1 < d 1 ​ q k − 1 ≤ n. S_{q}(n)\;=\;d_{1}\cdot\prod_{j=2}^{k}d_{j}\;\leq\;d_{1}\cdot(q-1)^{k-1}\;<\;d_{1}\,q^{k-1}\;\leq\;n\ . |  |

∎

From Proposition 1 we deduce that n n is a fixed point of S q S_{q} if and only if k = 1 k=1. It also follows from Proposition 1 that every orbit of S q S_{q} is finite and converges to some d < q d<q that is a fixed point. In other words, there exists a minimum number ν q ​ ( n) \nu_{q}(n) such that S q i ​ ( n) = S q ν q ​ ( n) ​ ( n) S_{q}^{i}(n)=S_{q}^{\nu_{q}(n)}(n) for all i ≥ ν q ​ ( n) i\geq\nu_{q}(n). Hence ν q ​ ( n) \nu_{q}(n) is the smallest number m m such that S q m ​ ( n) S_{q}^{m}(n) has a single digit. Sloane asked in [S] whether such minimum number of steps until a fixed point is uniformly bounded. The number ν q ​ ( n) \nu_{q}(n) is known as the persistence 1 1 1 What we call persistence in this paper is sometimes referred to as multiplicative persistence elsewhere, to distinguish it from the similarly defined concept of additive persistence, introduced by Hinden [H]. Since we will only consider multiplicative persistence, we will have no use for the adjective. of n n in base q q. Numerical evidence that ν q ​ ( n) \nu_{q}(n) is bounded has been collected for some values of q q. Furthermore, the answer to Sloane’s question is trivially positive for q = 2 q\,=\,2 since for any n ≥ 0 n\geq 0 one has S 2 ​ ( n) ∈ { 0, 1 } S_{2}(n)\in\{0,1\}, and { 0, 1 } \{0,1\} is the fixed-point set of S 2 S_{2}. The problem – known as the persistence problem – can be stated as follows.

###### Problem 1.

For a given q > 2 q>2, is there a positive number B ⁡ ( q) B(q) such that ν q ​ ( n) ≤ B ​ ( q) \nu_{q}(n)\leq B(q) for all n n\/?

A related set of issues goes as follows (considering now B ⁡ ( q) = sup n ν q ​ ( n) B(q)=\sup_{n}\nu_{q}(n) as an element of ℤ + ∪ ∞ \mathbb{Z}^{+}\cup\infty).

###### Problem 2.

What is the behavior of B ⁡ ( q) B(q) seen as a function of q q? More precisely, one can ask:

1. (a)

Is the answer to Problem 1 positive for all, or all but finitely many, or most, or infinitely many, or perhaps only finitely many values of q q?

2. (b)

What is the asymptotic behavior of B ⁡ ( q) B(q) as q → ∞ q\to\infty?

Here are some known facts about the persistence problem in various bases:

1. (1)

In base q = 2 q\,=\,2, the situation is rather trivial: every positive integer has persistence 1 1 in base 2 2.

2. (2)

In base q = 3 q=3, no number with persistence greater than 3 3 has ever been found.

3. (3)

In base q = 10 q=10, the number n = 68889 n=68889 has persistence 7 7, because under the Sloane map S 10 S_{10} we have

 | 68889 ↦ 27648 ↦ 2688 ↦ 768 ↦ 336 ↦ 54 ↦ 20 ↦ 0 68889\mapsto 27648\mapsto 2688\mapsto 768\mapsto 336\mapsto 54\mapsto 20\mapsto 0 |  |

In fact, this is the smallest number with persistence equal to 7 7.

4. (4)

Still in base q = 10 q=10, the number n = 277777788888899 n=277777788888899 has persistence 11 11. It is the smallest number with persistence equal to 11 11.

5. (5)

It is conjectured that ν 10 ​ ( n) ≤ 11 \nu_{10}(n)\leq 11 for all n n. This has been checked for all n n up to 10 233 10^{233}.

### 1.2. Goals and endeavors

In this paper, we have two main goals. The first goal is to examine the persistence problem in the light of some Dynamical Systems considerations. We will show that Sloane’s question (Problem 1) has an affirmative answer in a certain probabilistic sense. Roughly speaking, we will show that for any base q q, the set of natural numbers n n with persistence ≥ 3 \geq 3, i.e. such that S q 2 ​ ( n) ≠ 0 S_{q}^{2}(n)\neq 0, is an extremely rarified subset of ℤ + \mathbb{Z}^{+}. The probabilistic sense in question will be made progressively clear in § 3 and § 4.

We will see in particular that Problem 1 has a positive answer for q = 3 q=3 if a precise orbit that we will fully describe has a “generic” behavior under the ℤ \mathbb{Z} -action determined by a well-defined piecewise affine degree one circle map. Similarly, Problem 1 has a positive answer for q = 4 q=4 if two precise orbits that we will fully describe have a “generic” behavior under the ℤ \mathbb{Z} -action determined by another well-defined piecewise affine degree one circle map. The affine circle maps that we will encounter here are defined by q q and a number p < q p<q, a digit in base q q.

For bases q > 4 q>4, the relevant dynamical systems for the Sloane map are no longer ℤ \mathbb{Z} -actions, but rather ℤ k {\mathbb{Z}}^{k} -actions with k > 1 k>1. More precisely, they are given by certain free abelian groups of piecewise affine degree-one circle maps. We will exploit some simple ergodic properties of such free-abelian actions in order to derive our main probabilistic result on the Sloane map, namely Theorem 2.

Our second goal is to formulate a very general conjecture, namely Conjecture 3, concerning the asymptotic distribution of digits in the base q q expansion of long products whose factors are chosen from a given finite set of primes. This conjecture is conveniently formulated in terms of certain objects that we call multiplication automata, in part because their time evolution produces patterns that resemble those produced by the evolution of (one-dimensional) cellular automata. The most general form of the conjecture, as stated in § 5.2, is too broad to allow thorough numerical tests. Thus, short of a proof, we felt the need to provide an heuristic explanation lending support to this conjecture. Such heuristics is given in the language of inhomeogeneous Markov chains, as a form of convergence to equilibrium for the evolution of our automata. The multiplication automata and the associated convergence to fair distribution may be of interest to the physics of growth processes, and perhaps to other aspects of statistical mechanics.

### 1.3. The Erdös-Sloane map

In order to avoid possible misunderstandings, we warn the reader that another map has been studied, inspired by S q S_{q}: let us call it the Erdös-Sloane map, and denote it by S q ∗ S^{*}_{q}. For each natural number n n, S q ∗ ​ ( n) S^{*}_{q}(n) is the product of the non-zero digits of n n in base q q. According to Guy [G], this map was introduced by Erdös. Since our approach in this paper is based on the conjectured generic property that all digits should become equally probable for (products of) high powers of digits, we have nothing new to say about S q ∗ S^{*}_{q} (although some results we have about S 3 S_{3} can be interpreted in terms of S 3 ∗ S^{*}_{3}).

## 2. Conjectures, remarks, and first simple results

### 2.1. A trivial remark and some conjectures

Let us start by making a trivial but important remark. Choose some base q > 1 q>1. Looking back at the expansion given in ( 1), it is clear that we have the following trivial dichotomy:

1. (1)

Either one of the digits d j d_{j} is equal to zero, in which case S q ​ ( n) = 0 S_{q}(n)=0;

2. (2)

Or else S q ​ ( n) S_{q}(n) is equal to a product of digits in 1, 2, …, q − 1 1,2,\dots,q-1.

This trivial dichotomy, together with first observations of relevant but scarce numerical data, suggest us an obvious strategy. In order to answer Sloane’s question in the affirmative for base q q, it suffices to establish the following.

###### Conjecture 1.

There exists a positive integer k 0 ​ ( q) k_{0}(q) such that, for all k ≥ k 0 ​ ( q) k\geq k_{0}(q), the base q q expansion of any product of k k digits greater than 1 1 for base q q has at least one digit equal to zero.

As soon as a product of digits becomes divisible by q q, a zero appears as its right-most digit when written in base q q, and therefore the next iteration of the Sloane map yields 0 0 as the result. This trivial remark allows us to concentrate only on those products that are not divisible by the base q q. The effect of that will be dramatic when q = 4 q=4. The following two conjectures are implied by Conjecture 1.

In the case of base q = 3 q=3, the only non-zero values assumed by the Sloane map are powers of 2 2. In other words, we only need to investigate the orbit of 1 1 under the doubling map x ↦ 2 ⋅ x x\mapsto 2\cdot x.

###### Conjecture 1a.

There exists a positive integer k 3, 2 k_{3,2} such that, for all k ≥ k 3, 2 k\geq k_{3,2}, the base- 3 3 expansion of 2 k 2^{k} has at least one digit equal to zero.

Such a statement is reminiscent of a conjecture by Erdös to the effect that there is always a 2 among the digits in base 3 of 2 k 2^{k} for all k k sufficiently large. This question has been recently adressed by Lagarias in [L].

In the case of base q = 4 q=4, in principle all products of the form 2 m ⋅ 3 n 2^{m}\cdot 3^{n} would need to be examined. But since the basis 4 divides 2 m ⋅ 3 n 2^{m}\cdot 3^{n} as soon as m ≥ 2 m\geq 2, we only have to consider: (a) powers of 3 or (b) products of the form 2 ⋅ 3 m 2\cdot 3^{m}. In other words, we only need to consider the orbits of 1 and 2 under the tripling map x ↦ 3 ⋅ x x\mapsto 3\cdot x.

###### Conjecture 1b.

There exists a positive integer k 4, 3 k_{4,3} such that, for all k ≥ k 4, 3 k\geq k_{4,3}, the base- 4 4 expansions of 3 k 3^{k} and 2 ⋅ 3 k 2\cdot 3^{k} each have at least one digit equal to zero.

There is considerable computational evidence in favor of these conjectures. Proving these conjectures is certainly sufficient to solve the persistence problem for the corresponding bases.

### 2.2. A weak estimate on ν 3 ​ ( n) \nu_{3}(n)

Let us take the time to establish a weak estimate on ν 3 ​ ( n) \nu_{3}(n), the minimum stability time of n ∈ ℤ + n\in\mathbb{Z}^{+} (in base 3 3) introduced in § 1. This should be compared to a similar estimate proved by Erdös concerning the Erdös-Sloane map. First, a very simple lemma.

###### Lemma 1.

If n > 3 n>3, then at least one of the digits in the base- 3 3 expansion of 2 n 2^{n} is not equal to 2 2.

###### Proof.

Suppose the base- 3 3 expansion of 2 n 2^{n} has exactly k k digits, all equal to 2 2. Then 2 n = 3 k − 1 2^{n}=3^{k}-1, and we have a solution to Catalan’s equation 3 x − 2 y = 1 3^{x}-2^{y}=1 with y = n > 3 y=n>3, which is impossible. 2 2 2 It is not necessary to use the highly non-trivial result about the full Catalan’s conjecture (concerning the Diophantine equation a x − b y = 1 a^{x}-b^{y}=1 –see [M]). The special case needed here (with bases 2 2 and 3 3, which are prime) can be proved by elementary means – see [LeV, p. 85]. ∎

###### Remark 1.

It follows from the proof that S 3 ​ ( 2 n) ≤ 2 k − 1 S_{3}(2^{n})\leq 2^{k-1}.

Let us now present our weak estimate. Recall that if N ∈ ℤ + N\in\mathbb{Z}^{+}, then the number of digits in the base- q q expansion of N N is equal to 1 + ⌊ log q ⁡ N ⌋ 1+\lfloor\log_{q}{N}\rfloor.

###### Proposition 2.

For all n ≥ 3 n\geq 3, we have ν 3 ​ ( n) ≤ 2 ​ ( 1 + log 3 ⁡ log 3 ​ n) \nu_{3}(n)\leq 2(1+\log_{3}\log_{3}{n}).

###### Proof.

Let n > 3 n>3 be given, and assume S 3 ​ ( n) ≠ 0 S_{3}(n)\neq 0, otherwise there is nothing to prove. Thus, suppose n 1, n 2, …, n m n_{1},n_{2},\ldots,n_{m} are such that

1. (i)

n j > 3 n_{j}>3 for j = 1, 2, …, m j=1,2,\ldots,m;

2. (ii)

S 3 ​ ( n) = 2 n 1 S_{3}(n)=2^{n_{1}};

3. (iii)

S 3 ​ ( 2 n j) = 2 n j + 1 S_{3}(2^{n_{j}})=2^{n_{j+1}} for j = 1, 2, …, m − 1 j=1,2,\ldots,m-1;

4. (iv)

m m is maximal with the above properties.

From these properties we see that the only possible values for S 3 ​ ( 2 n m) S_{3}(2^{n_{m}}) are 0, 1, 2, 2 2 0,1,2,2^{2} or 2 3 2^{3}. This implies that ν 3 ​ ( n) ≤ 3 + m \nu_{3}(n)\leq 3+m. Hence it suffices to find a suitable bound for the number m m.

Let k j k_{j} denote the number of digits in the base- 3 3 expansion of n j n_{j}, for j = 1, 2, …, m j=1,2,\ldots,m. Since n j > 3 n_{j}>3, we deduce from Lemma 1 and Remark 1 that S 3 ​ ( 2 n j) = 2 n j + 1 ≤ 2 k j − 1 S_{3}(2^{n_{j}})=2^{n_{j+1}}\leq 2^{k_{j}-1}. But we also know that k j = 1 + ⌊ n j ​ log 3 ​ 2 ⌋ k_{j}=1+\lfloor n_{j}\log_{3}{2}\rfloor. Therefore we have

 | n j + 1 ≤ α ​ n j, for j = 1, 2, …, m 1, n_{j+1}\;\leq\;\alpha n_{j}\ ,\ \ \ \textrm{for}\ \ j=1,2,\ldots,m_{1}\ , |  |

where α = log 3 ⁡ 2 \alpha=\log_{3}{2}. From this it follows that

 | 3 < n m ≤ α m − 1 ​ n 1. 3\;<\;n_{m}\;\leq\;\alpha^{m-1}n_{1}\ . |  |

But we also have n 1 ≤ log 3 ⁡ n n_{1}\leq\log_{3}{n}. Hence, extracting the base- 3 3 logarithm of all terms in the above inequality, we see that

 | m < 1 + ( log 3 ⁡ log 3 ​ n) − 1 log 3 ⁡ ( α − 1) < − 1 + 2 ​ log 3 ​ log 3 ​ n. m\;<\;1+\frac{(\log_{3}\log_{3}{n})-1}{\log_{3}{(\alpha^{-1})}}\;<\;-1+2\log_{3}\log_{3}{n}\ . |  |

This shows that ν 3 ​ ( n) < 2 ​ ( 1 + log 3 ⁡ log 3 ​ n) \nu_{3}(n)<2(1+\log_{3}\log_{3}{n}), as claimed. ∎

## 3. Ergodic ℤ \mathbb{Z} -actions and persistence in bases q = 3, 4 q=3,4

In this section, more precisely in § 3.3 below, we introduce a simple dynamical system – generated by a single piecewise affine degree-one circle map – which will turn out to be very useful in the study of the Sloane map for bases q = 3, 4 q=3,4. But first let us present some simple arithmetical facts.

### 3.1. Periodicity of tails

Looking at the base- 3 3 expansions of the successive powers of two (see Figure 2), it is clear that for every k ≥ 1 k\geq 1 the rightmost k k digits of these powers exhibit a periodic behavior. Our goal here is to calculate the minimum period. This periodicity is more general: the last k k digits of the base- q q expansion of p n p^{n} form a periodic sequence, for all 1 < p < q 1<p<q. This fact is a simple consequence of modular arithmetic, and we call it tail periodicity.

First, we need the following simple lemma. Recall that, if q > 1 q>1 is an integer, then the set of all residues r ∈ { 0, 1, 2, …, q − 1 } r\in\{0,1,2,\ldots,q-1\} modulo q q that are relatively prime with q q form a multiplicative group (under multiplication modulo q q), called the group of units modulo q q, denoted U q U_{q}. This group U q U_{q} has order ϕ ⁡ ( q) \phi(q), where ϕ \phi is Euler’s totient function. An integer p p is said to be a primitive root modulo q q if the residue class of p p modulo q q has order ϕ ⁡ ( q) \phi(q) in U q U_{q} (in particular, if such a primitive root exists, then the group U q U_{q} must be cyclic).

###### Lemma 2.

Let p p and q q be integers such that 1 < p < q 1<p<q and p p is a primitive root modulo q q. Then the residues p n ( mod q) p^{n}(\!\!\mod q), n = 0, 1, 2, … n=0,1,2,\ldots, form a periodic sequence with minimum period equal to ϕ ⁡ ( q) \phi(q).

###### Proof.

By hypothesis, p ∈ U q p\in U_{q} is a generator of the cyclic group U q U_{q}. Therefore, by Euler’s theorem, p ϕ ⁡ ( q) ≡ 1 ( mod q) p^{\phi(q)}\equiv 1(\!\!\mod q), and the elements 1, p, p 2, …, p ϕ ⁡ ( q) − 1 1,p,p^{2},\ldots,\penalty p^{\phi(q)-1} exhaust the elements of U q U_{q}. Since p n + ϕ ⁡ ( q) ≡ p n ( mod q) p^{n+\phi(q)}\equiv p^{n}(\!\!\mod q) for all n n, the sequence p n p^{n} is indeed periodic, with minimum period ϕ ⁡ ( q) \phi(q). ∎

As a consequence, we have the following. Given integers k ≥ 1 k\geq 1 and n ≥ 0 n\geq 0, let r n ​ ( k) r_{n}(k) denote the residue of 2 n 2^{n} modulo 3 k 3^{k}.

###### Lemma 3.

For each k ≥ 1 k\geq 1, the sequence r n ​ ( k) r_{n}(k), n = 0, 1, … n=0,1,\ldots, is periodic with minimum period 2 ⋅ 3 k − 1 2\cdot 3^{k-1}.

###### Proof.

It is well-known that 2 2 is a primitive root modulo 3 k 3^{k} for all k ≥ 1 k\geq 1 (see [LeV, p. 81]). Thus, the desired result follows at once from lemma 2 (with p = 2 p=2 and q = 3 k q=3^{k}) and the fact that ϕ ⁡ ( 3 k) = 3 k − 3 k − 1 = 2 ⋅ 3 k − 1 \phi(3^{k})=3^{k}-3^{k-1}=2\cdot 3^{k-1}. ∎

Note that for each k k there are exactly 2 ⋅ 3 k − 1 2\cdot 3^{k-1} strings of length k k in the symbols 0, 1, 2 0,1,2 which do not end in a zero. Call these strings allowable. Combining this counting, the above lemma and the fact that r n ​ ( k) r_{n}(k) also never ends in a zero (otherwise 2 n 2^{n} would be divisible by 3 3), we see that in any full (minimum) period of r n ​ ( k) r_{n}(k) each allowable string appears exactly once. Moreover, since there are exactly 2 k 2^{k} allowable strings of length k k that show only the digits 1 1 and 2 2, the proportion of allowable strings in which at least one zero appears (relative to the total number of allowable sequences of length k k) tends to 1 1 as k → ∞ k\to\infty. From this we deduce that the set A = { n ∈ ℤ +: S 3 ​ ( 2 n) = 0 } A=\{n\in\mathbb{Z}^{+}:\;S_{3}(2^{n})=0\} has asymptotic density 1 1, in the sense of § 3.4 below. This fact can be generalized to other bases (but the counting argument used here becomes a bit more involved). Rather than delve into such arithmetic methods, we shall use a completely different approach to prove a more general density result that holds true for all bases.

### 3.2. Almost-periodicity of heads

If, instead of looking at the final k k digits of the base- 3 3 expansions of powers of two, we look at the first k k digits (for k ≥ 1 k\geq 1 fixed), the behavior of such heads is no longer periodic. It is rather almost periodic, as we will show (see Remark 2).

[image: Refer to caption]

Figure 1. A piecewise linear circle map built out of two linear maps, one expanding with slope p p, the other contracting with slope p q \frac{p}{q}.

### 3.3. An ergodic ℤ \mathbb{Z} -action

In fact, let us present a more general result. We consider two integers 1 < p < q 1<p<q and consider the sequence p n p^{n}, n = 0, 1, 2, … n=0,1,2,\ldots, written in base q q, say

(2) |  | p n = [d 1, n ​ d 2, n ​ … ​ d k n, n] q = ∑ i = 1 k n d i, n ​ q k n − i, p^{n}\;=\;\left[d_{1,n}d_{2,n}\dots d_{k_{n},n}\right]_{q}\;=\;\sum_{i=1}^{k_{n}}d_{i,n}q^{k_{n}-i}\ , |  |

where 0 ≤ d i, n ≤ q − 1 0\leq d_{i,n}\leq q-1 and d 1, n ≠ 0 d_{1,n}\neq 0, and where the number of digits k n k_{n} is given by k n = ⌈ n ​ log q ​ p ⌉ k_{n}=\lceil n\log_{q}{p}\rceil. If we add a “decimal point” in front of the above expansion, we get the number

(3) |  | x n = p n q k n = [0. d 1, n d 2, n ⋯ d k n, n] q ∈ Δ q, x_{n}\;=\;\frac{p^{n}}{q^{k_{n}}}\;=\;\left[0.d_{1,n}d_{2,n}\cdots d_{k_{n},n}\right]_{q}\;\in\;\Delta_{q}\ , |  |

where Δ q = [1 q, 1] ⊂ ℝ \Delta_{q}=[\frac{1}{q},1]\subset\mathbb{R}. Note that x 0 = ( 0.1) q = 1 / q x_{0}=(0.1)_{q}=1/q. Now, the crucial observation is that the sequence ( x n) (x_{n}) just defined is precisely the orbit of x 0 = 1 / q x_{0}=1/q under the piecewise-affine map T p, q: Δ q → Δ q T_{p,q}:\Delta_{q}\to\Delta_{q} given by

(4) |  | T p, q ( x) = { p ​ x, if ​ 1 q ≤ x < 1 p, p q ​ x, if ​ 1 p ≤ x ≤ 1. T_{p,q}(x)\;=\;\left\{\begin{matrix}px&,&\textrm{if}\ \;\dfrac{1}{q}\leq x<\dfrac{1}{p}\ ,\\ {}&{}&{}\\ \dfrac{p}{q}x&,&\textrm{if}\ \;\dfrac{1}{p}\leq x\leq 1\ .\end{matrix}\right. |  |

This map is built out of two linear maps of the real line: one expanding (multiplication by p > 1 p>1), the other contracting (multiplication by p / q < 1 p/q<1); see Figure 1. Through the identification of the endpoints of Δ q \Delta_{q}, the map T p, q T_{p,q} becomes a (piecewise affine) homeomorphism of the circle. The reader can easily check that x n = T p, q n ​ ( x 0) x_{n}=T_{p,q}^{n}(x_{0}), for all n ≥ 0 n\geq 0. 3 3 3 There are some analogies between Sloane’s question, at least for base 3, and the Collatz conjecture as discussed in Terence Tao’s blog entry [T]. In both cases, one represents the problem by a question about a map on a compact abelian group (here the circle, while one uses the dyadics for the Collatz conjecture). Also, in both cases one can formulate a main aspect of the problem in terms of powers of 2 in base 3: here by expressing that 2 n 2^{n} has at least one zero in its base 3 expansion for all n > 15 n>15, and as explained by Tao in said blog for the Collatz case.

Now we have the following result.

###### Theorem 1.

The map T p, q: Δ q → Δ q T_{p,q}:\Delta_{q}\to\Delta_{q} is topologically conjugate to the rotation by α = log q ⁡ p \alpha=\log_{q}{p}. The conjugacy is Lipschitz, in fact differentiable except at a single point. Moreover, T p, q T_{p,q} has an absolutely continuous invariant measure given by

 | d ​ μ ​ ( x) = d ​ x x ​ log ⁡ q. d\mu(x)\;=\;\frac{dx}{x\log{q}}\ . |  |

###### Proof.

Let us write T = T p, q T=T_{p,q} in this proof. First note that

 | T n ​ ( x 0) \displaystyle T^{n}(x_{0})\; | = p n q ⌈ n ​ α ⌉ = 1 q 1 − { n ​ α } ​ ( p q α) n \displaystyle=\;\frac{p^{n}}{q^{\lceil n\alpha\rceil}}\;=\;\frac{1}{q^{1-\{n\alpha\}}}\left(\frac{p}{q^{\alpha}}\right)^{n} |  |

 |  | = q { n ​ α } − 1, \displaystyle=\;q^{\{n\alpha\}-1}\ , |  |

where we have used that p ​ q − α = 1 pq^{-\alpha}=1. Hence, defining h: [0, 1] → Δ q h:[0,1]\to\Delta_{q} by

(5) |  | h ⁡ ( t) = q t − 1 = 1 q ​ exp ⁡ { t ​ log ⁡ q }, h(t)\;=\;q^{t-1}\;=\;\frac{1}{q}\exp\{t\log{q}\}\ , |  |

we see that h ⁡ ( { n ​ α }) = T n ​ ( x 0) h(\{n\alpha\})=T^{n}(x_{0}). In other words, h h maps the orbit of 0 0 under the rotation R α: t ↦ t + α ( mod 1) R_{\alpha}:t\mapsto t+\alpha\,(\!\!\mod 1) onto the orbit of x 0 x_{0} under T T. This suggests that h h is a conjugacy between R α R_{\alpha} and T T.

To see this, let t ∈ [0, 1] t\in[0,1], and note that there are two possibilities.

1. (i)

We have 0 ≤ t < 1 − α 0\leq t<1-\alpha: in this case, we have R α ​ ( t) = t + α R_{\alpha}(t)=t+\alpha, and therefore

 | h ∘ R α ​ ( t) \displaystyle h\circ R_{\alpha}(t)\; | = q t + α − 1 = q α ​ h ​ ( t) \displaystyle=\;q^{t+\alpha-1}\;=\;q^{\alpha}h(t) |  |

 |  | = q log q ⁡ p ​ h ​ ( t) = p ​ h ​ ( t) = T ∘ h ⁡ ( t). \displaystyle=\;q^{\log_{q}{p}}h(t)\;=\;ph(t)\;=\;T\circ h(t)\ . |  |

2. (ii)

We have 1 − α ≤ t ≤ 1 1-\alpha\leq t\leq 1: in this case, R α ​ ( t) = t + α − 1 R_{\alpha}(t)=t+\alpha-1, and therefore

 | h ∘ R α ​ ( t) \displaystyle h\circ R_{\alpha}(t)\; | = q t + α − 2 = q α − 1 ​ h ​ ( t) \displaystyle=\;q^{t+\alpha-2}\;=\;q^{\alpha-1}h(t) |  |

 |  | = q log q ⁡ p − 1 ​ h ​ ( t) = p q ​ h ​ ( t) = T ∘ h ⁡ ( t). \displaystyle=\;q^{\log_{q}{p}-1}h(t)\;=\;\frac{p}{q}h(t)\;=\;T\circ h(t)\ . |  |

Thus, it follows that h ∘ R α = T ∘ h h\circ R_{\alpha}=T\circ h. The map h h is a homeomorphism, as is clear from ( 5). In fact h h is an analytic diffeomorphism in the open interval ( 0, 1) (0,1). Upon identification of the endpoints 0 0 and 1 1, h h becomes a circle homeomorphism which is differentiable at all points except one, where a break in the derivative occurs.

The absolutely continuous invariant measure μ \mu for T T in Δ q \Delta_{q} can be obtained very simply as the push-forward of Lebesgue measure λ \lambda in [0, 1] [0,1] via h h. To wit, if E ⊆ Δ q E\subseteq\Delta_{q} is Borel measurable, we have

 | μ ⁡ ( E) = λ ⁡ ( h − 1 ​ ( E)) = ∫ h − 1 ​ ( E) 𝑑 t = ∫ E ( h − 1) ′ ​ ( x) ​ 𝑑 x. \mu(E)\;=\;\lambda(h^{-1}(E))\;=\;\int_{h^{-1}(E)}dt\;=\;\int_{E}(h^{-1})^{\prime}(x)\,dx\ . |  |

Since from ( 5) we have

 | h − 1 ​ ( x) = log ⁡ q ​ x log ⁡ q, h^{-1}(x)\;=\;\frac{\log{qx}}{\log{q}}\ , |  |

it follows that

 | d ​ μ ​ ( x) = ( h − 1) ′ ​ ( x) ​ d ​ x = 1 x ​ log ⁡ q ​ d ​ x, d\mu(x)\;=\;(h^{-1})^{\prime}(x)\,dx\;=\;\frac{1}{x\log{q}}\,dx\ , |  |

as was to be proved. ∎

###### Remark 2.

Note that we do not assume that α = log q ⁡ p \alpha=\log_{q}{p} is irrational in the above theorem. When α \alpha is irrational, the orbit of any point under T p, q T_{p,q} is almost periodic. Hence we have the promised almost periodicity of tails. For a more general result concerning piecewise affine homeomorphisms of the circle, see [Li].

###### Remark 3.

The above theorem also holds true when p > q p>q, provided we define T p, q T_{p,q} appropriately in such cases. This can be done as follows. Let k ≥ 1 k\geq 1 be such that q k < p < q k + 1 q^{k}<p<q^{k+1}, and define

(6) |  | T p, q ( x) = { p q k ​ x, if ​ 1 q ≤ x < q k p, p q k + 1 ​ x, if ​ q k p ≤ x ≤ 1. T_{p,q}(x)\;=\;\left\{\begin{matrix}\dfrac{p}{q^{k}}x&,&\textrm{if}\ \;\dfrac{1}{q}\leq x<\dfrac{q^{k}}{p}\ ,\\ {}&{}&{}\\ \dfrac{p}{q^{k+1}}x&,&\textrm{if}\ \;\dfrac{q^{k}}{p}\leq x\leq 1\ .\end{matrix}\right. |  |

Then, just as before, T p, q: Δ q → Δ q T_{p,q}:\Delta_{q}\to\Delta_{q} is a piecewise affine degree-one circle map with rotation number α = { log q ⁡ p } \alpha=\{\log_{q}{p}\}, and this circle map preserves the same measure μ \mu given in Theorem 1 (cf. § 4.5).

###### Remark 4.

In [Bo], Boshernitzan gave an example of a piecewise affine homeomorphism of the unit circle ℝ / ℤ \mathbb{R}/\mathbb{Z} (seen as the interval [0, 1] [0,1] with the endpoints identified) which preserves the rationals and has only dense orbits. We remark that our T p, q T_{p,q} ’s yield a plethora of such examples. Indeed, defining L: [0, 1] → Δ q L:[0,1]\to\Delta_{q} by L ⁡ ( t) = 1 q + ( 1 − 1 q) ​ t L(t)=\frac{1}{q}+\left(1-\frac{1}{q}\right)t, we see that each conjugated map L − 1 ∘ T p, q ∘ L L^{-1}\circ T_{p,q}\circ L is an example of the type devised by Boshernitzan, provided its rotation number α = { log q ⁡ p } \alpha=\{\log_{q}{p}\} is irrational.

Let us now present two corollaries of Theorem 1.

### 3.4. A density result

In order to state and prove the first corollary, we recall that the lower density of a subset A ⊆ ℤ + A\subseteq\mathbb{Z}^{+}, is given by

 | D − ​ ( A) = lim inf n → ∞ 1 n ​ #​ ( A ∩ [1, n]). D^{-}(A)\;=\;\lim\inf_{n\to\infty}\frac{1}{n}\#(A\cap[1,n])\ . |  |

One defines the upper density D + ​ ( A) D^{+}(A) of A A in similar fashion, replacing the lim inf \lim\inf by lim sup \lim\sup. If the upper and lower densities are equal, then we say that A A has asymptotic density D ⁡ ( A) = D + ​ ( A) = D − ​ ( A) D(A)=D^{+}(A)=D^{-}(A). Recall also that a continuous self-map T T of a compact metric space X X is uniquely ergodic, i.e. has a unique invariant Borel probability measure μ \mu, if and only if its Birkhoff time averages 1 n ​ ∑ i = 0 n f ∘ T i \frac{1}{n}\sum_{i=0}^{n}f\circ T^{i} converge uniformly to the space average ∫ X f ​ 𝑑 μ \int_{X}f\,d\mu, for every f ∈ C 0 ​ ( X) f\in C^{0}(X) (see for instance [W, p. 160]).

###### Corollary 1.

If 1 < p < q 1<p<q are such that log q ⁡ p \log_{q}{p} is irrational, then the set A = { n ∈ ℤ +: S q ​ ( p n) = 0 } A=\{n\in\mathbb{Z}^{+}\,:\;S_{q}(p^{n})=0\,\} has asymptotic density equal to 1 1.

###### Proof.

Let T = T p, q T=T_{p,q} and μ \mu be as in Theorem 1, and let x n = T n ​ ( x 0) x_{n}=T^{n}(x_{0}) be our special orbit as before. Since T T is Lipschitz-conjugate to an irrational rotation, it is uniquely ergodic. For each j ≥ 1 j\geq 1, let B j ⊆ Δ q B_{j}\subseteq\Delta_{q} be the set of all points x x whose base- q q expansion has at least one digit 0 0 among its first j j digits. Then B j B_{j} is a finite union of intervals, and its Lebesgue measure is easily seen to be

 | λ ⁡ ( B j) = | Δ q | [1 − ( 1 − 1 q) j − 1] \lambda(B_{j})\;=\;|\Delta_{q}|\left[1-\left(1-\frac{1}{q}\right)^{j-1}\right] |  |

Thus, λ ⁡ ( B j) ↗ | Δ q | \lambda(B_{j})\nearrow|\Delta_{q}|, and therefore μ ⁡ ( B j) ↗ 1 \mu(B_{j})\nearrow 1, as j → ∞ j\to\infty. Note that if x n ∈ B j x_{n}\in B_{j} for some n n with k n ≥ j k_{n}\geq j, then S q ​ ( p n) = 0 S_{q}(p^{n})=0, i.e. n ∈ A n\in A. Since B j B_{j} is a finite union of intervals and μ \mu is a regular Borel measure, we can find a continuous function f j: Δ q → ℝ f_{j}:\Delta_{q}\to\mathbb{R} such that 0 ≤ f j ≤ χ B j 0\leq f_{j}\leq\chi_{B_{j}} everywhere and

(7) |  | ∫ Δ q f j ​ 𝑑 μ ≥ μ ⁡ ( B j) − 1 2 ​ j. \int_{\Delta_{q}}f_{j}\,d\mu\;\geq\;\mu(B_{j})-\frac{1}{2j}\ . |  |

In particular, for all N ≥ 1 N\geq 1 we have

(8) |  | 1 N ​ ∑ n = 0 N − 1 χ B j ∘ T n ​ ( x 0) ≥ 1 N ​ ∑ n = 0 N − 1 f j ∘ T n ​ ( x 0). \frac{1}{N}\sum_{n=0}^{N-1}\chi_{B_{j}}\circ T^{n}(x_{0})\;\geq\;\frac{1}{N}\sum_{n=0}^{N-1}f_{j}\circ T^{n}(x_{0})\ . |  |

Using ( 7) and the fact that T T is uniquely ergodic, we deduce that

(9) |  | 1 N ​ ∑ n = 0 N − 1 f j ∘ T n ​ ( x 0) ≥ ∫ Δ q f j ​ 𝑑 μ − 1 2 ​ j ≥ μ ⁡ ( B j) − 1 j, \frac{1}{N}\sum_{n=0}^{N-1}f_{j}\circ T^{n}(x_{0})\;\geq\;\int_{\Delta_{q}}f_{j}\,d\mu-\frac{1}{2j}\;\geq\;\mu(B_{j})-\frac{1}{j}\ , |  |

provided N N is sufficiently large. Hence, combining ( 8) and ( 9), we get

(10) |  | 1 N ​ ∑ n = 0 N − 1 χ B j ​ ( x n) ≥ μ ⁡ ( B j) − 1 j, \frac{1}{N}\sum_{n=0}^{N-1}\chi_{B_{j}}(x_{n})\;\geq\;\mu(B_{j})-\frac{1}{j}\ , |  |

for all sufficiently large N N. Writing A j = { n ∈ ℤ +: x n ∈ B j } A_{j}=\{n\in\mathbb{Z}^{+}:\,x_{n}\in B_{j}\}, we have just proved that

 | D − ​ ( A j) ≥ μ ⁡ ( B j) − 1 j D^{-}(A_{j})\;\geq\;\mu(B_{j})-\frac{1}{j} |  |

Since all but finitely many elements of A j A_{j} belong to A A, it follows that D − ​ ( A) ≥ μ ⁡ ( B j) − 1 j D^{-}(A)\geq\mu(B_{j})-\frac{1}{j} as well, for every j j. Letting j → ∞ j\to\infty, we deduce that D ⁡ ( A) = D − ​ ( A) = 1 D(A)=D^{-}(A)=1, as desired. ∎

### 3.5. A formula for the digits of p n p^{n} in base q q

Another consequence of Theorem 1 is the following explicit formula for the j j -th digit of p n p^{n} written in base q q.

###### Corollary 2.

If d j, n d_{j,n} denotes, as in ( 2), the j j -th digit from left to right in the base q q expansion of p n p^{n}, then

(11) |  | d j, n = ⌊ q { q j + { n ​ α } − 2 } ⌋, for all j = 1, 2, …, k n, d_{j,n}\;=\;\left\lfloor q\left\{q^{j+\{n\alpha\}-2}\right\}\right\rfloor\ ,\ \textrm{for all}\ j=1,2,\ldots,k_{n}\ , |  |

where, as before, α = log q ⁡ p \alpha=\log_{q}{p} and k n k_{n} is the number of digits in that expansion.

###### Proof.

Again, we let T = T p, q T=T_{p,q}. Since d j, n d_{j,n} is also the j j -th digit of x n = T n ​ ( x 0) x_{n}=T^{n}(x_{0}) after the decimal point, we can certainly write

 | d j, n = ⌊ q ⁡ { q j − 1 ​ x n } ⌋. d_{j,n}\;=\;\left\lfloor q\left\{q^{j-1}x_{n}\right\}\right\rfloor\ . |  |

But by Theorem 1, we have

 | x n = T n ​ ( x 0) = h ∘ R α n ​ ( 0) = h ⁡ ( { n ​ α }) = q { n ​ α } − 1. x_{n}\;=\;T^{n}(x_{0})\;=\;h\circ R_{\alpha}^{n}(0)\;=\;h(\{n\alpha\})\;=\;q^{\{n\alpha\}-1}\ . |  |

This immediately implies formula ( 11). ∎

###### Remark 5.

Although it may seem a bit surprising that we have such an explicit formula for the digits d j, n d_{j,n}, the formula is in practice rather useless for large values of n n: roughly speaking, evaluating d j, n d_{j,n} depends on knowing at least the first n n digits of α = log q ⁡ p \alpha=\log_{q}{p} after the decimal point.

At least for bases 3 3, 4 4, 5 5, and 10 10, we have strong computational evidence suggesting the validity of the following conjecture, which (for base 3 3) is certainly stronger than conjecture 1a.

###### Conjecture 2.

If q q is not a power of p p, then for each d = 0, 1, …, q − 1 d=0,1,\ldots,q-1, we have

 | lim n → ∞ 1 k n ​ #​ { 1 ≤ j ≤ k n: d j, n = d } = 1 q. \lim_{n\to\infty}\frac{1}{k_{n}}\,\#\left\{1\leq j\leq k_{n}:\ d_{j,n}=d\,\right\}\;=\;\frac{1}{q}\ . |  |

(As before, k n = ⌈ n ​ log q ​ p ⌉ k_{n}=\lceil n\log_{q}{p}\rceil is the number of digits of p n p^{n} in base q q.)

For computational evidence and heuristic arguments supporting this conjecture, see § 5. If q = p k q=p^{k} for some k ≥ 1 k\geq 1, then for every n ≥ 1 n\geq 1 the base q q expansion of p n ​ k p^{nk} consists of the digit 1 1 followed by n n zeros. This shows that the hypothesis that q q is not a power of p p is indeed necessary.

## 4. Ergodic ℤ d \mathbb{Z}^{d} -actions and persistence in base q > 4 q>4

We wish to generalize the results presented in § 3 to the cases when the base q q is greater than 4 4. The relevant dynamical system here is no longer the (semi-)group given by a single piecewise affine degree-one circle map, but rather the (semi-)group generated by several such maps.

### 4.1. Abelian actions for the Sloane map

Let 2 = p 1 < p 2 < ⋯ < p m ≤ q − 1 2=p_{1}<p_{2}<\cdots<p_{m}\leq q-1 be the list of all primes smaller than q q. If n ∈ ℤ + n\in\mathbb{Z}^{+} is such that S q ​ ( n) ≠ 0 S_{q}(n)\neq 0, then we can certainly write

(12) |  | S q ​ ( n) = ∏ i = 1 m p i n i, S_{q}(n)\;=\;\prod_{i=1}^{m}p_{i}^{n_{i}}\ , |  |

where ( n 1, n 2, ⋯, n m) ∈ ℤ + m = ( ℤ +) m ⊂ ℤ m (n_{1},n_{2},\cdots,n_{m})\in\mathbb{Z}_{+}^{m}=\left(\mathbb{Z}^{+}\right)^{m}\subset\mathbb{Z}^{m}. We can treat the base- q q expansion of the right-hand side of ( 12) pretty much in the same way as we treated the digits of p n p^{n} in base q q in § 3.3. Keeping the notation introduced in § 3.3, let Δ q = [q − 1, 1] ≡ 𝕊 1 \Delta_{q}=[q^{-1},1]\equiv\mathbb{S}^{1}, and consider the piecewise affine homeomorphisms T p i = T p i, q: Δ q → Δ q T_{p_{i}}=T_{p_{i},q}:\Delta_{q}\to\Delta_{q} ( i = 1, 2, …, m i=1,2,\ldots,m) defined taking p = p i p=p_{i} in ( 4). We denote by P ​ L + ​ ( Δ) PL^{+}(\Delta) the group of all piecewise affine homeomorphisms of the interval Δ ⊆ ℝ \Delta\subseteq\mathbb{R}.

###### Lemma 4.

The group G q ⊂ P ​ L + ​ ( Δ q) G_{q}\subset PL^{+}(\Delta_{q}) generated by { T p i: i = 1, 2, …, m } \{T_{p_{i}}:\,i=1,2,\ldots,m\} is abelian.

###### Proof.

Let h: [0, 1] → Δ q h:[0,1]\to\Delta_{q} be the homeomorphism constructed in the proof of Theorem 1. Then for each i i we have T p i = h ∘ R α i ∘ h − 1 T_{p_{i}}=h\circ R_{\alpha_{i}}\circ h^{-1}, where α i = log q ⁡ p i \alpha_{i}=\log_{q}{p_{i}} and R α i: x ↦ x + α i ( mod 1) R_{\alpha_{i}}:\,x\mapsto x+\alpha_{i}\,({\mod 1}) is the corresponding rotation. Since any two circle rotations commute, we have R α i ∘ R α j = R α j ∘ R α i R_{\alpha_{i}}\circ R_{\alpha_{j}}=R_{\alpha_{j}}\circ R_{\alpha_{i}}, and therefore T p i ∘ T p j = T p j ∘ T p i T_{p_{i}}\circ T_{p_{j}}=T_{p_{j}}\circ T_{p_{i}} as well, so G q G_{q} is abelian. ∎

This lemma tells us in particular that we have a well-defined surjective homomorphism ℤ m → G q \mathbb{Z}^{m}\to G_{q} given by

 | ℤ m ∋ 𝒏 = ( n 1, n 2, …, n m) ↦ T 𝒏 = T p 1 n 1 ∘ T p 2 n 2 ∘ ⋯ ∘ T p m n m ∈ G q. \mathbb{Z}^{m}\ni{\bm{n}}=(n_{1},n_{2},\ldots,n_{m})\;\mapsto\;T^{\bm{n}}\;=\;T_{p_{1}}^{n_{1}}\circ T_{p_{2}}^{n_{2}}\circ\cdots\circ T_{p_{m}}^{n_{m}}\;\in G_{q}\ . |  |

However, this homomorphism is not necessarily one-to-one (but see below). In any case, we see that ℤ m \mathbb{Z}^{m} acts on the circle in a special way as a group of piecewise-affine homeomorphisms of the circle. What is the relevance of this action to the study of the Sloane map in base q q? In order to answer this question, we proceed as in § 3.3. Let x 0 = [0.1] q = 1 q ∈ Δ q x_{0}=[0.1]_{q}=\frac{1}{q}\in\Delta_{q}. Then for each 𝒏 ∈ ℤ + m \bm{n}\in\mathbb{Z}_{+}^{m} we have

(13) |  | T 𝒏 ​ ( x 0) = p 1 n 1 p 2 n 2 ⋯ p m n m q k ⁡ ( 𝒏), T^{\bm{n}}(x_{0})\;=\;\frac{p_{1}^{n_{1}}p_{2}^{n_{2}}\cdots p_{m}^{n_{m}}}{q^{k(\bm{n})}}\ , |  |

where k ⁡ ( 𝒏) k(\bm{n}) is the number of digits of the base- q q expansion of the numerator, given by

 | k ⁡ ( 𝒏) = ⌈ ∑ i = 1 m n i ​ log q ​ p i ⌉ = ⌈ ∑ i = 1 m n i ​ α i ⌉. k(\bm{n})\;=\;\left\lceil\sum_{i=1}^{m}n_{i}\log_{q}{p_{i}}\right\rceil\;=\;\left\lceil\sum_{i=1}^{m}n_{i}\alpha_{i}\right\rceil\ . |  |

Thus, we see that the entire range of values assumed by the Sloane map is contained in a single orbit of the action of the semi-group ℤ + m ⊂ ℤ m \mathbb{Z}_{+}^{m}\subset\mathbb{Z}^{m}.

### 4.2. Detour: ergodic free-abelian actions

We shall need the following facts about free-abelian actions. Let G G be a free abelian group of rank k k, with a fixed set of generators { e 1, e 2, …, e k } \{e_{1},e_{2},\ldots,e_{k}\}. Each g ∈ G g\in G has a unique representation g = ∑ n i ​ e i g=\sum n_{i}e_{i} with n i ∈ ℤ n_{i}\in\mathbb{Z} for all i = 1, 2, …, k i=1,2,\ldots,k. We write ‖ g ‖ = max 1 ≤ i ≤ k ⁡ | n i | \|g\|=\max_{1\leq i\leq k}|n_{i}|, the norm of g g. We denote by G + ⊂ G G^{+}\subset G the semigroup consisting of all elements g g for which n i ≥ 0 n_{i}\geq 0 for all i i. For each N ∈ ℤ + N\in\mathbb{Z}^{+}, let Λ N ​ ( G) = { g ∈ G: ‖ g ‖ ≤ N } \Lambda_{N}(G)=\{g\in G:\|g\|\leq N\}, and let Λ N ​ ( G +) = Λ N ​ ( G) ∩ G + \Lambda_{N}(G^{+})=\Lambda_{N}(G)\cap G^{+}.

Now suppose that the group G G (or the semigroup G + G^{+}) acts on a probability measure space ( X, μ) (X,\mu) as a group (or semigroup) of measure-preserving transformations (m.p.t.’s). In other words, if T g: X → X T^{g}:X\to X denotes the m.p.t. associated to g ∈ G g\in G, then T ∗ g ​ μ = μ T^{g}_{*}\mu=\mu for every g g (where the star denotes push-forward of measures). We say that the G G -action (or G + G^{+} -action) on ( X, μ) (X,\mu) is ergodic if the only measurable subsets E ⊆ X E\subseteq X that are invariant under G G (or G + G^{+}) – i.e. such that ( T g) − 1 ​ E ⊆ E (T^{g})^{-1}E\subseteq E for all g g – are either null-sets or full-measure sets. Just as for rank-one measure-preserving actions, there is a multi-dimensional version of Birkhoff’s ergodic theorem, both in the case of free-abelian groups and free-abelian semigroups. We state the version for semigroups, which is the relevant one here.

###### Theorem A.

If the G + G^{+} -action on ( X, μ) (X,\mu) is ergodic, then for every f ∈ L 1 ​ ( X, μ) f\in L^{1}(X,\mu) and for μ \mu -almost every x ∈ X x\in X we have

(14) |  | lim N → ∞ 1 #​ Λ N ​ ( G +) ​ ∑ g ∈ Λ N ​ ( G +) f ∘ T g ​ ( x) = ∫ X f ​ 𝑑 μ. \lim_{N\to\infty}\frac{1}{\#\Lambda_{N}(G^{+})}\sum_{g\in\Lambda_{N}(G^{+})}f\circ T^{g}(x)\;=\;\int_{X}f\,d\mu\ . |  |

A proof of this theorem can be found in [K, ch. 2].

One can also define unique ergodicity by analogy with the rank-one case. A G G -action (or G + G^{+} -action) on a compact metric space X X through continuous maps is uniquely ergodic if there exists a unique Borel probability measure on X X which is G G -invariant (or G + G^{+} -invariant). As for rank-one actions, we have the following fact (which, once again, we state only for semigroup actions).

###### Theorem B.

If a G + G^{+} -action by continuous maps on a compact metric space X X is uniquely ergodic then for every f ∈ C ⁡ ( X) f\in C(X)

 | 1 #​ Λ N ​ ( G +) ​ ∑ g ∈ Λ N ​ ( G +) f ∘ T g converges uniformly to ∫ X f ​ 𝑑 μ \frac{1}{\#\Lambda_{N}(G^{+})}\sum_{g\in\Lambda_{N}(G^{+})}f\circ T^{g}\ \ \textrm{converges uniformly to}\ \ \ \int_{X}f\,d\mu |  |

as N → ∞ N\to\infty, where μ \mu is the unique G + G^{+} -invariant Borel probability measure.

The proof of the analogous statement for rank-one actions as given in, say, [W, pp.160-161] applies mutatis mutandis to the present case. The converse of Theorem B is also true, but will not be needed here.

### 4.3. First density result

Now we go back to our investigation of the Sloane map. Given a positive integer N N, let Λ N \Lambda_{N} denote the “cube” Λ N = { 𝒏 ∈ ℤ m: | n i | ≤ N, i = 1, 2, …, m } \Lambda_{N}=\{{\bm{n}}\in\mathbb{Z}^{m}:|n_{i}|\leq N,\,i=1,2,\ldots,m\}, and let Λ N + = Λ N ∩ ℤ + m \Lambda_{N}^{+}=\Lambda_{N}\cap\mathbb{Z}_{+}^{m}. The lower asymptotic density of a subset A ⊆ ℤ + m A\subseteq\mathbb{Z}_{+}^{m} is defined to be

 | D − ​ ( A) = lim inf N → ∞ 1 N m ​ #​ ( A ∩ Λ N +). D^{-}(A)\;=\;\lim\inf_{N\to\infty}\frac{1}{N^{m}}\#(A\cap\Lambda_{N}^{+})\ . |  |

The upper asymptotic density of A A, denoted D + ​ ( A) D^{+}(A), is similarly defined (replacing lim inf \lim\inf by lim sup \lim\sup). We always have 0 ≤ D − ​ ( A) ≤ D + ​ ( A) ≤ 1 0\leq D^{-}(A)\leq D^{+}(A)\leq 1. When D − ​ ( A) = D + ​ ( A) D^{-}(A)=D^{+}(A), this common value is called the asymptotic density of A A and it is denoted by D ⁡ ( A) D(A).

###### Proposition 3.

If the base q q is not a prime number, then the set

 | A = { 𝒏 = ( n 1, n 2, …, n m) ∈ ℤ + m: S q ( p 1 n 1 p 2 n 2 ⋯ p m n m) = 0 } A\;=\;\left\{{\bm{n}}=(n_{1},n_{2},\ldots,n_{m})\in\mathbb{Z}_{+}^{m}:\,S_{q}(p_{1}^{n_{1}}p_{2}^{n_{2}}\cdots p_{m}^{n_{m}})=0\,\right\} |  |

has asymptotic density equal to 1 1.

###### Proof.

Since q q is not a prime, we can certainly write q = p 1 a 1 p 2 a 2 ⋯ p m a m q=p_{1}^{a_{1}}p_{2}^{a_{2}}\cdots p_{m}^{a_{m}} where each a i ≥ 0 a_{i}\geq 0. Now, if 𝒏 ∈ ℤ + m \bm{n}\in\mathbb{Z}_{+}^{m} is such that n i ≥ a i n_{i}\geq a_{i} for all i i, then q q divides p 1 n 1 p 2 n 2 ⋯ p m n m p_{1}^{n_{1}}p_{2}^{n_{2}}\cdots p_{m}^{n_{m}}, and therefore S q ( p 1 n 1 p 2 n 2 ⋯ p m n m) = 0 S_{q}(p_{1}^{n_{1}}p_{2}^{n_{2}}\cdots p_{m}^{n_{m}})=0. This shows that A ⊇ { 𝒏 ∈ ℤ + m: n i ≥ a i ​ for all ​ i } A\supseteq\{\bm{n}\in\mathbb{Z}_{+}^{m}:\,n_{i}\geq a_{i}\ \textrm{for all}\;i\}. Hence, for every N N sufficiently large we have

 | #⁡ ( A ∩ Λ N +) ≥ ∏ i = 1 m ( N − a i + 1), \#\left(A\cap\Lambda_{N}^{+}\right)\;\geq\;\prod_{i=1}^{m}(N-a_{i}+1)\ , |  |

and therefore

 | D − ​ ( A) ≥ lim N → ∞ 1 N m ​ ∏ i = 1 m ( N − a i + 1) = 1 D^{-}(A)\;\geq\;\lim_{N\to\infty}\,\frac{1}{N^{m}}\prod_{i=1}^{m}(N-a_{i}+1)\;=\;1 |  |

This proves that D ⁡ ( A) = D − ​ ( A) = 1 D(A)=D^{-}(A)=1. ∎

The set A A in Proposition 3 has asymptotic density 1 1 for trivial reasons: most m m -tuples ( n 1, n 2, …, n m) (n_{1},n_{2},\ldots,n_{m}) are such that n i ≥ a i n_{i}\geq a_{i} for all i i. Note that we did not exploit the abelian action introduced in § 4.1. We will prove in § 4.4 below a more refined version of Proposition 3 using the ergodic properties of such abelian actions.

### 4.4. Second density result

Our second density result makes use of the group G q G_{q} and its action on the circle. In fact, it will make use of certain subgroups of G q G_{q}, which turn out to be free abelian.

We will need the following lemma. Given 1 ≤ i 1 < i 2 < ⋯ < i k ≤ m 1\leq i_{1}<i_{2}<\cdots<i_{k}\leq m, let us denote the subgroup of G q G_{q} generated by { T p i 1, T p i 2, …, T p i k } \{T_{p_{i_{1}}},T_{p_{i_{2}}},\ldots,T_{p_{i_{k}}}\} by G ⁡ ( i 1, i 2, …, i k) G(i_{1},i_{2},\ldots,i_{k}). Recall that α i = log q ⁡ p i \alpha_{i}=\log_{q}{p_{i}} is the rotation number of T p i T_{p_{i}}

###### Lemma 5.

If the numbers 1, α i 1, α i 2, …, α i k 1,\alpha_{i_{1}},\alpha_{i_{2}},\ldots,\alpha_{i_{k}} are rationally independent 4 4 4 In other words, linearly independent over the field of rational numbers, then G ⁡ ( i 1, i 2, …, i k) G(i_{1},i_{2},\ldots,i_{k}) is a free abelian group of rank k k. Moreover, its action on the circle Δ q ≡ 𝕊 1 \Delta_{q}\equiv\mathbb{S}^{1} is uniquely ergodic.

###### Proof.

Suppose ( n 1, n 2, …, n k) ∈ ℤ k (n_{1},n_{2},\ldots,n_{k})\in\mathbb{Z}^{k} is such that

 | T p i 1 n 1 ∘ T p i 2 n 2 ∘ ⋯ ∘ T p i k n k = I d. T_{p_{i_{1}}}^{n_{1}}\circ T_{p_{i_{2}}}^{n_{2}}\circ\cdots\circ T_{p_{i_{k}}}^{n_{k}}\;=\;Id\ . |  |

From this and the fact that each T p i T_{p_{i}} is conjugate to R α i R_{\alpha_{i}} by the same conjugating map, we have

 | R α i 1 n 1 ∘ R α i 2 n 2 ∘ ⋯ ∘ R α i k n k = I d R_{\alpha_{i_{1}}}^{n_{1}}\circ R_{\alpha_{i_{2}}}^{n_{2}}\circ\cdots\circ R_{\alpha_{i_{k}}}^{n_{k}}\;=\;Id |  |

But then n 1 ​ α i 1 + n 2 ​ α i 2 + ⋯ + n k ​ α i k ≡ 0 ( mod 1) n_{1}\alpha_{i_{1}}+n_{2}\alpha_{i_{2}}+\cdots+n_{k}\alpha_{i_{k}}\equiv 0\;(\!\!{\mod 1}). In other words, there exists N ∈ ℤ N\in\mathbb{Z} such that n 1 ​ α i 1 + n 2 ​ α i 2 + ⋯ + n k ​ α i k = N n_{1}\alpha_{i_{1}}+n_{2}\alpha_{i_{2}}+\cdots+n_{k}\alpha_{i_{k}}=N. The hypothesis of rational independence implies that n 1 = n 2 = ⋯ = n k = N = 0 n_{1}=n_{2}=\cdots=n_{k}=N=0. Hence there are no non-trivial relations in G ⁡ ( i 1, i 2, …, i k) G(i_{1},i_{2},\ldots,i_{k}). This shows the group is free abelian as stated. Moreover, at least one of the α i j \alpha_{i_{j}} ’s must be irrational. Say α i 1 \alpha_{i_{1}} is irrational; then T p i 1 T_{p_{i_{1}}}, being conjugate to an irrational rotation, is uniquely ergodic. Therefore, a fortiori, the action of G ⁡ ( i 1, i 2, …, i k) G(i_{1},i_{2},\ldots,i_{k}) on the circle is uniquely ergodic. ∎

We are now in a position to state and prove our second density result. This result refines Proposition 3, and in particular covers the case when the base q q is prime.

###### Theorem 2.

Let 1 ≤ i 1 < i 2 < ⋯ < i k ≤ m 1\leq i_{1}<i_{2}<\cdots<i_{k}\leq m be chosen so that the numbers 1, α i 1, α i 2, …, α i k 1,\alpha_{i_{1}},\alpha_{i_{2}},\ldots,\alpha_{i_{k}} are rationally independent. Then for every divisor d d of q q, the set

 | A = { ( n 1, n 2, …, n k) ∈ ℤ + k: S q ( p i 1 n 1 p i 2 n 2 ⋯ p i k n k ⋅ d) = 0 } A\;=\;\left\{(n_{1},n_{2},\ldots,n_{k})\in\mathbb{Z}_{+}^{k}:\ S_{q}(p_{i_{1}}^{n_{1}}p_{i_{2}}^{n_{2}}\cdots p_{i_{k}}^{n_{k}}\cdot d)=0\,\right\} |  |

has asymptotic density equal to 1 1.

###### Proof.

Things have been set up so that the same argument used in the proof of Corollary 1 can be applied, mutatis mutandis. By Lemma 5, the action of the group G = G ⁡ ( i 1, i 2, …, i k) ≅ ℤ k G=G(i_{1},i_{2},\ldots,i_{k})\cong\mathbb{Z}^{k} on the circle Δ q ≡ 𝕊 1 \Delta_{q}\equiv\mathbb{S}^{1} is uniquely ergodic; the unique invariant measure is the measure μ \mu constructed in Theorem 1. Let us fix the divisor d d of the base q q. We are interested in a particular orbit of the semigroup G + ≅ ℤ + k G^{+}\cong\mathbb{Z}_{+}^{k}, namely that of the point w 0 = d / q ∈ Δ q w_{0}=d/q\in\Delta_{q}. For each 𝒏 ∈ ℤ + k \bm{n}\in\mathbb{Z}_{+}^{k}, let us write w 𝒏 = T 𝒏 ​ ( w 0) w_{\bm{n}}=T^{\bm{n}}(w_{0}). Also, denote by ℓ ⁡ ( 𝒏) \ell(\bm{n}) the number of digits in the base- q q expansion of the number p i 1 n 1 p i 2 n 2 ⋯ p i k n k ⋅ d p_{i_{1}}^{n_{1}}p_{i_{2}}^{n_{2}}\cdots p_{i_{k}}^{n_{k}}\cdot d. Then, just as in ( 13), we have

(15) |  | w 𝒏 = p i 1 n 1 p i 2 n 2 ⋯ p i k n k ⋅ d q ℓ ⁡ ( 𝒏). w_{\bm{n}}\;=\;\frac{p_{i_{1}}^{n_{1}}p_{i_{2}}^{n_{2}}\cdots p_{i_{k}}^{n_{k}}\cdot d}{q^{\ell(\bm{n})}}\ . |  |

As in the proof of Corollary 1, for each j ≥ 1 j\geq 1, let B j ⊆ Δ q B_{j}\subseteq\Delta_{q} be the set of all points x x whose base- q q expansion has at least one digit 0 0 among its first j j digits. As we saw there, μ ⁡ ( B j) ↗ 1 \mu(B_{j})\nearrow 1 as j → ∞ j\to\infty. Let f j: Δ q → ℝ f_{j}:\Delta_{q}\to\mathbb{R} be as in that proof also; thus, each f j f_{j} is continuous and 0 ≤ f j ≤ χ B j 0\leq f_{j}\leq\chi_{B_{j}}, and

(16) |  | ∫ Δ q f j ​ 𝑑 μ ≥ μ ⁡ ( B j) − 1 2 ​ j. \int_{\Delta_{q}}f_{j}\,d\mu\;\geq\;\mu(B_{j})-\frac{1}{2j}\ . |  |

The point now – as is clear from ( 15) – is that

 | S q ( p i 1 n 1 p i 2 n 2 ⋯ p i k n k ⋅ d) = 0 ⇔ T 𝒏 ( w 0) = w 𝒏 ∈ B j for some j ≤ ℓ ( 𝒏). S_{q}(p_{i_{1}}^{n_{1}}p_{i_{2}}^{n_{2}}\cdots p_{i_{k}}^{n_{k}}\cdot d)=0\;\iff\;T^{\bm{n}}(w_{0})=w_{\bm{n}}\in B_{j}\ \textrm{for some}\ j\leq\ell({\bm{n}})\ . |  |

In other words, 𝒏 ∈ A \bm{n}\in A if and only if w 𝒏 ∈ B j w_{\bm{n}}\in B_{j} for some j ≤ k 𝒏 j\leq k_{\bm{n}}. By analogy with what we did in the proof of Corollary 1, for each j ≥ 1 j\geq 1 we define A j = { 𝒏 ∈ ℤ + k: w 𝒏 ∈ B j } A_{j}=\{\bm{n}\in\mathbb{Z}_{+}^{k}:\;w_{\bm{n}}\in B_{j}\}. Note that all but finitely many elements of A j A_{j} belong to A A. Hence, in order to prove that D ⁡ ( A) = 1 D(A)=1, it suffices to show that D − ​ ( A j) ↗ 1 D^{-}(A_{j})\nearrow 1 as j → ∞ j\to\infty. Since the action of G + G^{+} on the circle is uniquely ergodic, combining Theorem B with ( 16) we deduce that, for each fixed j j and all sufficiently large N N,

 | 1 #​ Λ N + ​ ∑ 𝒏 ∈ Λ N + f j ∘ T 𝒏 ​ ( w 0) ≥ ∫ Δ q f j ​ 𝑑 μ − 1 2 ​ j ≥ μ ⁡ ( B j) − 1 j. \frac{1}{\#\Lambda_{N}^{+}}\sum_{\bm{n}\in\Lambda_{N}^{+}}f_{j}\circ T^{\bm{n}}(w_{0})\;\geq\;\int_{\Delta_{q}}f_{j}\,d\mu-\frac{1}{2j}\;\geq\;\mu(B_{j})-\frac{1}{j}\ . |  |

Since f j ≤ χ B j f_{j}\leq\chi_{B_{j}}, it follows that

 | 1 #​ Λ N + ​ ∑ 𝒏 ∈ Λ N + χ B j ​ ( w 𝒏) ≥ μ ⁡ ( B j) − 1 j, \frac{1}{\#\Lambda_{N}^{+}}\sum_{\bm{n}\in\Lambda_{N}^{+}}\chi_{B_{j}}(w_{\bm{n}})\;\geq\;\mu(B_{j})-\frac{1}{j}\ , |  |

for all sufficiently large N N. Letting N → ∞ N\to\infty, this shows that

 | D − ​ ( A j) ≥ μ ⁡ ( B j) − 1 j D^{-}(A_{j})\;\geq\;\mu(B_{j})-\frac{1}{j} |  |

for all j j, and therefore D − ​ ( A j) ↗ 1 D^{-}(A_{j})\nearrow 1 as j → ∞ j\to\infty, as required. ∎

### 4.5. Further generalizations

Since in this paper we are primarily interested in the Sloane map, in all of the above we have focused on products of prime numbers smaller than the base q q. However, most of what we have done goes through when some or all of such primes are greater than q q. Recall from Remark 3 that if p > q p>q we can still define the circle maps T p, q T_{p,q}, and these still commute with each other because they all share a common absolutely continuous invariant measure. Thus, suppose that F F is some non-empty finite set of primes, and that not all the prime divisors of q q are in F F. Then the set { 1 } ∪ { log q ⁡ p: p ∈ F } \{1\}\cup\{\log_{q}{p}:\,p\in F\} is rationally independent. Therefore the maps T p, q T_{p,q} for p ∈ F p\in F generate a free-abelian group G F G_{F} and the action of G F G_{F} on the circle Δ q \Delta_{q} is uniquely ergodic (as in Lemma 5, and the proof is the same). Moreover, the density result given in Theorem 2 also holds true for the list of primes in F F. In particular, the vast majority of products of the form ∏ p ∈ F p n p \prod_{p\in F}p^{n_{p}} (with n p ∈ ℤ + n_{p}\in\mathbb{Z}^{+}) have at least one digit zero in their base- q q expansions. In § 5 we will make a much stronger assertion, in the form of a conjecture, to the effect that the digits in the base- q q expansions of such products become asymptotically equidistributed as max ⁡ { n p: p ∈ F } → ∞ \max\{n_{p}:\,p\in F\}\to\infty.

## 5. Computational evidence and heuristics

### 5.1. Asymptotic distribution of digits in long products of primes

To ease many statements to be made in rest of the paper, we will call Sloane’s conjecture the positive answer to the question about multiplicative persistence raised by Sloane in 1973. Our goal is to place Sloane’s conjecture as a consequence of a much more general conjecture concerning long products of primes (chosen from a given finite set).

As in § 4.5, let us be given a base q > 1 q>1 and a finite set of primes F F with the property that not all prime divisors of q q belong to F F. We call such an F F an allowable set of primes for q q. Suppose we play the following game: starting with any given positive integer a a, we randomly select a sequence π 1, π 2, …, π n, … \pi_{1},\pi_{2},\ldots,\pi_{n},\ldots of primes in F F and we use them to generate the sequence of products N n = a ⋅ π 1 ⋅ π 2 ⋯ π n N_{n}=a\cdot\pi_{1}\cdot\pi_{2}\cdots\pi_{n} with n ∈ ℤ + n\in\mathbb{Z}^{+}. Then it turns out that, regardless of the initial seed a a and of the sequence of primes selected, the frequency of each digit d ∈ { 0, 1, …, q − 1 } d\in\{0,1,\ldots,q-1\} in N n N_{n} always seems to approach 1 q \frac{1}{q} as n → ∞ n\to\infty. More seems to be true, and we formulate the conjecture that was revealed by our numerical computations in the following elementary way.

###### Conjecture 3.

(Elementary formulation).Given an integer q > 1 q>1, an allowable set of primes F F for q q, and a positive integer a a, consider any of the possible sequences of products defined by setting N 0 = a N_{0}=a and then, for each n ≥ 0 n\geq 0, N n + 1 = π n + 1 ⋅ N n N_{n+1}=\pi_{n+1}\cdot N_{n} where each π i \pi_{i} is a element of F F. Then the digits { 0, 1, 2, …, q − 1 } \{0,1,2,\dots,q-1\} are asymptotically equidistributed (their numbers tend to be in equal proportions) when n → ∞ n\to\infty in the base- q q representations of these successive N n N_{n} ’s. Furthermore, the same holds true for blocks of consecutive digits of any length, *i.e.,*the asymptotic proportion of each block of digits of length ℓ > 0 {\ell}>0 is given by 1 q ℓ \frac{1}{q^{\ell}}, the reciprocal of the number of distinct blocs of length ℓ {\ell} in base q q.

We remark that when the restriction of allowability is removed (but F F remains finite) it seems that the non-zero digits remain well distributed while the zeros may be much more abundant, which is more than we need in order to get the Sloane conjecture as a corollary.

### 5.2. Multiplication automata

Let us give a more precise and more general statement of the above conjecture, expressing it in the language of automata. The patterns arising by the multiplication game described above strongly suggest analogy with the dynamics of some simple *cellular automata*(abbreviated CA {\rm CA}) *i.e.,*automorphisms of a shift space that commute with the shift [He]. Successsive multiplications by any p > 1 p>1 (or by any sequence of such p p ’s) do not yield a CA {\rm CA}, because of the carryover effect, but give rise to a close enough object, which we define as follows.

###### Definition 1.

Let q > 1 q>1 and let F F be an allowable set of primes for q q. A multiplication automaton (or MA {\rm MA}), with alphabet 𝒜 q = { 0, 1, …, q − 1 } {\mathcal{A}}_{q}=\{0,1,\ldots,q-1\} consists of a finite sequence of primes π n ∈ F \pi_{n}\in F (with n ≥ 1 n\geq 1) called the multipliers, and two maps, the configuration map x: ℤ + 2 → 𝒜 q x:\mathbb{Z}_{+}^{2}\to{\mathcal{A}}_{q} and the carryover map c: ℤ + 2 → 𝒜 q c:\mathbb{Z}_{+}^{2}\to{\mathcal{A}}_{q} satisfying the following rules for all n ≥ 1 n\geq 1 and all i ≥ 1 i\geq 1:

1. (i)

x i, n = π n ⋅ x i, n − 1 + c i − 1, n mod q x_{i,n}=\pi_{n}\cdot x_{i,n-1}+c_{i-1,n}\mod q;

2. (ii)

c i, n = 1 q ​ ( π n ⋅ x i, n − 1 + c i − 1, n − x i, n) \displaystyle{c_{i,n}=\frac{1}{q}(\pi_{n}\cdot x_{i,n-1}+c_{i-1,n}-x_{i,n})}.

Here, we assume that the initial row ( x i, 0) i ∈ ℤ + (x_{i,0})_{i\in\mathbb{Z}^{+}} of the configuration map is given, as well as the column ( c 0, n) n ∈ ℤ + (c_{0,n})_{n\in\mathbb{Z}^{+}} of initial carryovers. We also assume that x i, 0 = 0 x_{i,0}=0 for all but finitely many values of i i, and we call the number a = ∑ i ≥ 0 x i, 0 ​ q i a=\sum_{i\geq 0}x_{i,0}q^{i} the seed of the MA {\rm MA}. Note that each row of an automaton has only finitely many non-zero elements; in other words, for each n ∈ ℤ + n\in\mathbb{Z}^{+} there exists a smallest k n ≥ 0 k_{n}\geq 0 such that x i, n = 0 x_{i,n}=0 for all i ≥ k n i\geq k_{n}. If the initial seed is non-zero, then k n → ∞ k_{n}\to\infty as n → ∞ n\to\infty.

Despite appearances from the above recursive formulas, it turns out that the values of the configuration map of a MA {\rm MA} are determined purely locally, as the following proposition shows. This further reinforces the similarity of MA {\rm MA} ’s with CA {\rm CA} ’s. 5 5 5 Warning: The word “locally” is used here with a different meaning from the one used when studying, e.g.,cellular automata; in that other context, the carryover is indeed a very non-local effect.

###### Proposition 4.

In every MA {\rm MA}, the configuration value x i, n x_{i,n} depends only on the three values x i, n − 1, x i − 1, n − 1, x i − 1, n x_{i,n-1},\,x_{i-1,n-1},\,x_{i-1,n} and on the multiplier π n \pi_{n}.

###### Proof.

We refer to formulas (i) and (ii) in Definition 1. From (ii) with i − 1 i-1 replacing i i we see that

(17) |  | c i − 1, n = 1 q ​ ( π n ​ x i − 1, n − 1 + c i − 2, n − x i − 1, n). c_{i-1,n}\;=\;\frac{1}{q}(\pi_{n}x_{i-1,n-1}+c_{i-2,n}-x_{i-1,n})\ . |  |

But formula (i) with i − 1 i-1 replacing i i gives us

(18) |  | c i − 2, n = ( x i − 1, n − π n ​ x i − 1, n − 1) mod q c_{i-2,n}\;=\;(x_{i-1,n}-\pi_{n}x_{i-1,n-1})\!\!\!\!\!\mod q |  |

Combining ( 17) and ( 18) with (i) we deduce that

 | x i, n = π n ​ x i, n − 1 + 1 q ​ [π n ​ x i − 1, n − 1 + ( ( x i − 1, n − π n ​ x i − 1, n − 1) mod q) − x i − 1, n], x_{i,n}=\pi_{n}x_{i,n-1}+\frac{1}{q}\left[\pi_{n}x_{i-1,n-1}+((x_{i-1,n}-\pi_{n}x_{i-1,n-1})\!\!\!\!\!\!\mod q)-x_{i-1,n}\right]\,, |  |

which is the desired result. ∎

###### Remark 6.

The way the MA {\rm MA} operates purely locally as told by Proposition 4 is illustrated in part (a) of Figure 5 where in each group of positions, the one framed in black is the value of x i, n x_{i,n}. It is worth pointing out that MA {\rm MA} ’s can be interpreted as examples of *error diffusion*where the input is the previous line, the modified input is the product of the input by π n \pi_{n} added to the carry over, and the new error is the next carry over (see [Tr] and references therein). Incidentally, part (b) of the same figure gives the allowed configuration of another automaton, namely the one that describes the evolution along columns (a simple model of discrete epitaxy). The configurations in part (c) of that figure are the forbidden ones resulting in a solid black square when nothing can be computed.

#### Example 1

The simplest example of a multiplication automaton relevant to Sloane’s conjecture is obtained by taking q = 3 q=3 and F = { 2 } F=\{2\}, choosing a = 1 a=1 as the seed, and setting c 0, n = 0 c_{0,n}=0 for all n n as the initial sequence of carryovers. Note that in this case π n = 2 \pi_{n}=2 for all n n. The configuration map for this automaton yields the list of all powers of 2 2 written in base 3 3. This list corresponds to the orbit of 1 3 = [0.1] 3 \frac{1}{3}=[0.1]_{3} under the map T 2, 3 T_{2,3} introduced in § 3.3. In the notation introduced above, we have 2 n = ∑ i = 0 k n − 1 x i, n ​ q i 2^{n}=\sum_{i=0}^{k_{n}-1}x_{i,n}q^{i} for all n n. Figure 2 exhibits the first 45 rows of this MA {\rm MA}, i.e. the first 45 powers of 2 (out of the about 8000 that we have computed). Some patterns seen there are reminiscent of those appearing in the simplest CA {\rm CA} ’s.

#### Example 2

Another pair of examples is obtained by taking q = 4 q=4 and F = { 3 } F=\{3\}, setting c 0, n = 0 c_{0,n}=0 for all n n as before, and choosing either a = 1 a=1 or a = 2 a=2 as the seed. The resulting pair of MA {\rm MA} yields the two sequences ( 3 n) n ≥ 0 (3^{n})_{n\geq 0} and ( 2 ⋅ 3 n) n ≥ 0 (2\cdot 3^{n})_{n\geq 0} written in base 4 4, which are the relevant ones for Sloane’s conjecture in that base. These sequences correspond to the orbits of 1 4 = [0.1] 4 \frac{1}{4}=[0.1]_{4} and 1 2 = [0.2] 4 \frac{1}{2}=[0.2]_{4} under successive iterations of the map T 3, 4 T_{3,4} introduced in § 3.3. The 23 first rows of these automata are presented side by side in Figure 3.

A MA {\rm MA} as given in Definition 1 can be used as a statistical model for the discrete-time evolution of a mixture of q q species (labeled balls, say, or distinct molecules) with positions at time n n labeled by the integers { 0, 1, …, k n − 1 } \{0,1,\dots,k_{n}-1\}. One is then interested in the asymptotic behavior of the mixture as characterized by the proportions of species populations as n → ∞ n\to\infty. This analogy with statistical mechanics and the observed patterns in the two examples above (see Figures 2 and 3), as well as in several other examples we have investigated, suggest the following conjecture. 6 6 6 This conjecture is indeed more general than its elementary counterpart given earlier: the latter corresponds to the cases when the initial sequence of carryovers in the MA {\rm MA} is identically zero.

###### Conjecture 3.

(General formulation.) The configuration map of every multiplication automaton with non-zero seed converges to an equilibrium in the following sense. For each ℓ > 0 \ell>0 and each ℓ \ell -block b 1 b 2 ⋯ b ℓ ∈ 𝒜 q ℓ b_{1}b_{2}\cdots b_{\ell}\in\mathcal{A}_{q}^{\ell}, we have

 | lim n → ∞ 1 k n #{ 0 ≤ i ≤ k n − ℓ: x i, n = b 1, x i + 1, n = b 2, …, x i + ℓ − 1, n = b ℓ } = 1 q ℓ. \lim_{n\to\infty}\frac{1}{k_{n}}\#\left\{0\leq i\leq k_{n}-\ell:\;x_{i,n}=b_{1},\,x_{i+1,n}=b_{2},\,\ldots,\,x_{i+\ell-1,n}=b_{\ell}\right\}\,=\,\frac{1}{q^{\ell}}\ . |  |

In other words, the populations of the q q species in the mixture become asymptotically perfectly balanced as time evolves. Figure 4 shows clearly that the proportion of zeros in 2 n 2^{n} ( i.e., in row n n of the automaton of Example 1) goes to one third of the digits when n n becomes large enough. Of course there are fluctuations in the proportions but the sizes of these fluctuations go to zero, as one would expect in a model of statistical physics. Similar data have been obtained with bases 4 4, 5 5, and 10 10 and a variety of allowable sets F F of prime multipliers. In many cases, we also checked that the expected asymptotic statistics of blocks behave according to the Conjecture.

Besides potential applications to random number generators, Conjecture 3, if proved true, would yield several interesting corollaries, such as Sloane’s conjecture for all bases (as we have already pointed out), and other conjectures by Erdös, Furstenberg, and Lagarias that are reported in [L].

Here is some space at the top

[image: Refer to caption]

Figure 2. Powers of 2 2 in base 3 3: the multiplication automaton of Example 1. It is conjectured that 2 15 2^{15} is the last power of 2 2 whose base- 3 3 expansion is zero-free.

#### Example 3

Note that in Definition 1 we have assumed that the allowable set of primes F F from which the multipliers are chosen is finite. If this condition is removed, Conjecture 3 becomes false, as the following example shows. We work in base q = 10 q=10 here, but similar examples can be given in other bases. Recall from elementary number theory that a repunit is a positive integer whose (base 10) expansion consists of a string of ones, e.g. 1, 11, 111, 1111, … 1,\,11,\,111,\,1111,\,\ldots, etc. If a repunit R R has n n digits, then of course

 | R = 10 n − 1 9 = 11 ⋯ 11 ( n times). R\;=\;\frac{10^{n}-1}{9}\;=\;11\cdots 11\ \ \ (n\ \textrm{times})\ . |  |

Let k k be any integer greater than 1 1 and consider the infinite sequence of repunits R 1 < R 2 < ⋯ < R n < ⋯ R_{1}<R_{2}<\cdots<R_{n}<\cdots given by

 | R n = 10 2 n − 1 9 R_{n}\;=\;\frac{10^{2^{n}}-1}{9} |  |

Then the identity 10 2 n + 1 − 1 = ( 10 2 n − 1) ​ ( 10 2 n + 1) 10^{2^{n+1}}-1\;=\;\left(10^{2^{n}}-1\right)\left(10^{2^{n}}+1\right) shows that R n R_{n} divides R n + 1 R_{n+1}, for each n ≥ 1 n\geq 1. Moreover, since gcd ⁡ ( 10 2 n − 1, 10 2 n + 1) = 1 \mathrm{gcd}(10^{2^{n}}-1\,,\,10^{2^{n}}+1)=1, we see that R n + 1 R_{n+1} has at least one prime factor which does not divide R n R_{n}. Hence there exist a sequence of primes π 1, π 2, …, π n, … \pi_{1},\pi_{2},\ldots,\pi_{n},\ldots (not necessarily distinct, but ranging over infinitely many values) and a sequence of natural numbers 1 = s 1 < s 2 < ⋯ < s n < ⋯ 1=s_{1}<s_{2}<\cdots<s_{n}<\cdots such that R n = π 1 π 2 ⋯ π s n R_{n}=\pi_{1}\pi_{2}\cdots\pi_{s_{n}} for all n n. But this means that each R n R_{n} appears as a row of the (generalized) MA {\rm MA} with base q = 10 q=10, seed a = 1 a=1 and with F F being the set of all primes appearing as factors of some R n R_{n}, which is infinite as we have shown. In particular, the line-by-line digits for this automaton cannot be asymptotically equidistributed. Therefore Conjecture 3 can fail to hold when F F is infinite. 7 7 7 It is an old unsolved problem to know whether the sequence of repunits 1, 11, 111, 1111, 11111, … 1,\,11,\,111,\,1111,\,11111,\,\ldots written in the decimal system, say, contains infinitely many primes.

### 5.3. Heuristics for convergence to equilibrium

Let us now give an chain of heuristic arguments lending further support in favor of Conjecture 3. The heuristics will be formulated for the most part in the context of Example 1 above ( q = 3 q=3 and F = { 2 } F=\{2\}). The key idea is to model the deterministic behaviour of an MA {\rm MA} by a stochastic process. The irregularities observed in the rows of an MA {\rm MA} are due to the carryover effect, and these will be interpreted as random. This will be our standing assumption. Stated informally: *everything is as if all would be random with appropriate distributions*.

#### 5.3.1. Heuristics I: Inhomogeneous Markov Chains

As pointed out already, we restrict our analysis almost entirely to the MA {\rm MA} of Example 1. We make the further restriction of looking only at the evolution of the populations of the 3 3 species given by the single digits 0, 1, 2 0,1,2. We ignore, of course, all zeros in positions to the left of the last non-zero digit in each row. Although our multiplication automaton is a deterministic object, we will model its evolution – more precisely the row-by-row evolution (or growth) of the population frequencies (or proportions) of the digits 0, 1, 2 0,1,2 – by a stochastic process. Once more, we leave to the reader to see how what we propose here can be extended to the general situation of the conjecture.

In the example at hand, the passage from row n n to row n + 1 n+1 of the multiplication automaton involves only multiplication by 2 2.

The only possible values of the carryovers are 0 0 and 1 1; in the general case of multiplication of π i \pi_{i} in base q q, finding the maximal carryover is indeed the first computation to be done.

Thus, for each i ≥ 0 i\geq 0 and each n ≥ 0 n\geq 0 we have either x i, n + 1 = 2 ​ x i, n mod 2 x_{i,n+1}=2x_{i,n}\mod 2 if there is no carryover at the column position i i, or x i, n + 1 = 2 ​ x i, n + 1 mod 2 x_{i,n+1}=2x_{i,n}+1\mod 2 if there is a carryover at that position. This means that in each position i i, the possible transitions of digits from one row to the next are 0 → 0 0\to 0, 1 → 2 1\to 2 and 2 → 1 2\to 1 without carryover, and 0 → 1 0\to 1, 1 → 0 1\to 0 and 2 → 2 2\to 2 with carryover. These spell out the incidence matrix

(19) |  | 𝑨 = [1 1 0 1 0 1 0 1 1]. \bm{A}\;=\;\begin{bmatrix}1&1&0\\ 1&0&1\\ 0&1&1\end{bmatrix}\ . |  |

This suggests that the evolution of the proportions p 0 ( n), p 1 ( n), p 2 ( n) p_{0}^{(n)},p_{1}^{(n)},p_{2}^{(n)} (with p 0 ( n) + p 1 ( n) + p 2 ( n) = 1 p_{0}^{(n)}+p_{1}^{(n)}+p_{2}^{(n)}=1) of the digits 0, 1, 2 0,1,2 from row to row of the automaton can be modeled by a simple (homogeneous) Markov chain. We refer to the column vectors 𝒑 n = ( p 0 ( n), p 1 ( n), p 2 ( n)) t \bm{p}_{n}=(p_{0}^{(n)},p_{1}^{(n)},p_{2}^{(n)})^{t} as population vectors. Our standing assumption in this context is that *the allowable transitions from each given state have equal probabilities*. Hence this Markov chain has as its transition matrix the doubly stochastic matrix 𝑷 = 1 2 ​ 𝑨 \bm{P}=\frac{1}{2}\bm{A}.

The situation is not quite so simple, however, because this proposed scheme fails to take into account the fact that the total population k n k_{n} occasionally increases as we go from row to row ( k n → ∞ k_{n}\to\infty as n → ∞ n\to\infty) depending on the leading digit, the multiplication factor, and the carryover inherited there.This growth of population size is our only hope to see the asymptotic equidistribution of digits stated above. Indeed, we know from § 3.1 that the tails of size ℓ ≥ 1 \ell\geq 1, namely the blocks x ℓ − 1, n ⋯ x 1, n x 0, n x_{\ell-1,n}\cdots x_{1,n}x_{0,n} (with n = 0, 1, … n=0,1,\ldots) form a periodic sequence. The same is true of the sequence of ℓ \ell -blocks x ℓ − 1 + r, n ⋯ x r + 1, n x r, n x_{\ell-1+r,n}\cdots x_{r+1,n}x_{r,n} for every fixed r r. Hence there is no hope to observe equidistribution of digits along blocks of fixed sizes.

This compels us to change the model slightly, to accommodate the eventual increase in population size. Only two things can happen when we go from row n n to row n + 1 n+1: either k n + 1 = k n k_{n+1}=k_{n}, i.e., the total population size stays the same, or k n + 1 = k n + 1 k_{n+1}=k_{n}+1, i.e., the total population size grows by 1 1. In the first case, the new proportions at time n + 1 n+1 can be obtained from the old proportions at time n n by multiplication with the matrix 𝑷 \bm{P}. In the second case, we can think that the left-most digit at row n n, namely x k n − 1, n x_{k_{n}-1,n} gives rise not to one, but two new digits at row n + 1 n+1, namely x k n − 1, n + 1 x_{k_{n}-1,n+1} and x k n, n + 1 x_{k_{n},n+1}. Of these two, the last one is always equal to 1 1. Since we either have x k n − 1, n = 1 x_{k_{n}-1,n}=1 or x k n − 1, n = 2 x_{k_{n}-1,n}=2, we now either have a non-zero probability of a transition 1 → 1 1\to 1, or the probability of a transition 2 → 1 2\to 1 is now slighty greater than 1 2 \frac{1}{2}. In other words, the new population vector 𝒑 n + 1 \bm{p}_{n+1} is obtained from the old population vector 𝒑 n \bm{p}_{n} by multiplication with one of the two stochastic matrices

(20) |  | 𝑸 n = [1 2 1 2 0 1 2 + ϵ n ϵ n 2 + ϵ n 1 2 + ϵ n 0 1 2 1 2]; 𝑹 n = [1 2 1 2 0 1 2 0 1 2 0 1 + ϵ n 2 + ϵ n 1 2 + ϵ n]. \bm{Q}_{n}\;=\;\begin{bmatrix}\frac{1}{2}&\frac{1}{2}&0\\ \frac{1}{2+\epsilon_{n}}&\frac{\epsilon_{n}}{2+\epsilon_{n}}&\frac{1}{2+\epsilon_{n}}\\ 0&\frac{1}{2}&\frac{1}{2}\end{bmatrix}\ \ \ ;\ \ \bm{R}_{n}\;=\;\begin{bmatrix}\frac{1}{2}&\frac{1}{2}&0\\ \frac{1}{2}&0&\frac{1}{2}\\ 0&\frac{1+\epsilon_{n}}{2+\epsilon_{n}}&\frac{1}{2+\epsilon_{n}}\end{bmatrix}\ . |  |

where ϵ n = 1 k n + 1 \epsilon_{n}=\frac{1}{k_{n}+1} accounts for the increase of the population of 1 1 ’s by one.

Summarizing, the evolution of population proportions in each row of the multiplication automaton in Example 1 can be modelled by an Inhomogeneous Markov Chain (IMC), given by a sequence of stochastic transition matrices ( 𝑷 n) (\bm{P}_{n}) and (column) probability vectors 𝒑 n \bm{p}_{n} such that 𝒑 n + 1 t = 𝒑 n t ​ 𝑷 n \bm{p}_{n+1}^{t}=\bm{p}_{n}^{t}\bm{P}_{n}. Here, each transition matrix 𝑷 n ∈ { 𝑷, 𝑸 n, 𝑹 n } \bm{P}_{n}\in\{\bm{P},\bm{Q}_{n},\bm{R}_{n}\}. There is a well-developed theory of IMC’s; see for instance [B], or [IM].

As it turns out, convergence to equilibrium as expressed in Conjecture 3 is tantamount, in the present example, to strong ergodicity of the IMC. Let us explain this point. For each pair of integers n > m ≥ 0 n>m\geq 0, let 𝑷 ( m, n) = 𝑷 m 𝑷 m + 1 ⋯ 𝑷 n − 1 \bm{P}(m,n)=\bm{P}_{m}\bm{P}_{m+1}\cdots\bm{P}_{n-1}. Following, [B, §6.8.1], we say that the IMC is strongly ergodic if there exists a row probability vector 𝒒 \bm{q} such that

 | lim n → ∞ sup 𝒑 d V ​ ( 𝒑 t ​ 𝑷 ​ ( m, n), 𝒒) = 0, \lim_{n\to\infty}\sup_{\bm{p}}\,d_{V}(\bm{p}^{t}\bm{P}(m,n)\,,\,\bm{q})=0\ , |  |

where the supremum is over all column probability vectors 𝒑 = ( p 0, p 1, p 2) t \bm{p}=(p_{0},p_{1},p_{2})^{t}, and where d V d_{V} is the so-called distance in variation, defined by

 | d V ​ ( 𝜶, 𝜷) = 1 2 ​ ∑ i = 0 2 | α i − β i |, d_{V}(\bm{\alpha},\bm{\beta})\;=\;\frac{1}{2}\sum_{i=0}^{2}|\alpha_{i}-\beta_{i}|\ , |  |

whenever 𝜶 = ( α 0, α 1, α 2) \bm{\alpha}=(\alpha_{0},\alpha_{1},\alpha_{2}) and 𝜷 = ( β 0, β 1, β 2) \bm{\beta}=(\beta_{0},\beta_{1},\beta_{2}) are (row) probability vectors. Recall (see [B, §2.5], or any standard text on Markov chains) that a stationary distribution for a stochastic matrix 𝑸 \bm{Q} is a column probability vector 𝒗 \bm{v} such that 𝒗 t ​ 𝑸 = 𝒗 t \bm{v}^{t}\bm{Q}=\bm{v}^{t}. We have the following sufficient condition for strong ergodicity, as stated in [B, Th. 6.8.5] ( cf. [IM, Th. V.4.5, p. 170]).

###### Theorem C.

If each transition matrix 𝐏 n \bm{P}_{n} has at least one stationary distribution and if there exists a stochastic matrix 𝐏 ∞ \bm{P}_{\infty} such that ‖ 𝐏 n − 𝐏 ∞ ‖ → 0 \|\bm{P}_{n}-\bm{P}_{\infty}\|\to 0 as n → ∞ n\to\infty, then the IMC is strongly ergodic. 8 8 8 Here, ∥ ⋅ ∥ \|\cdot\| is the max-norm: if 𝐀 = ( a i ​ j) \bm{A}=(a_{ij}), then ‖ 𝐀 ‖ = max i, j ⁡ | a i ​ j | \|\bm{A}\|=\max_{i,j}|a_{ij}|.

The hypotheses in this theorem are met in our example. Indeed, here we clearly see from ( 20) that ‖ 𝑸 n − 𝑷 ‖ → 0 \|\bm{Q}_{n}-\bm{P}\|\to 0 and ‖ 𝑹 n − 𝑷 ‖ → 0 \|\bm{R}_{n}-\bm{P}\|\to 0 as n → ∞ n\to\infty; hence we can take 𝑷 ∞ = 𝑷 \bm{P}_{\infty}=\bm{P}. Moreover, an easy computation shows that the probability vectors

(21) |  | 𝒒 n \displaystyle\bm{q}_{n}\; | = ( 2 6 + ϵ n, 2 + ϵ n 6 + ϵ n, 2 6 + ϵ n) t \displaystyle=\;\left(\frac{2}{6+\epsilon_{n}}\,,\,\frac{2+\epsilon_{n}}{6+\epsilon_{n}}\,,\,\frac{2}{6+\epsilon_{n}}\right)^{t} |  |

 | 𝒓 n \displaystyle\bm{r}_{n}\; | = ( 2 + 2 ​ ϵ n 6 + 5 ​ ϵ n, 2 + 2 ​ ϵ n 6 + 5 ​ ϵ n, 2 + ϵ n 6 + 5 ​ ϵ n) t \displaystyle=\;\left(\frac{2+2\epsilon_{n}}{6+5\epsilon_{n}}\,,\,\frac{2+2\epsilon_{n}}{6+5\epsilon_{n}}\,,\,\frac{2+\epsilon_{n}}{6+5\epsilon_{n}}\right)^{t} |  |

are stationary distributions for 𝑸 n \bm{Q}_{n} and 𝑹 𝒏 \bm{R_{n}}, respectively.

The heuristic argument just presented supports the validity of Conjecture 3 in the case of Example 1, as long as one accepts the standing assumption stated in the beginning of this section. The formalism of IMC’s can be similarly used to treat MA {\rm MA} ’s with any other bases q q and allowable sets of multipliers F F. The analysis of the two MA {\rm MA} ’s in Example 2 is completely analogous, because in those two cases F = { 3 } F=\{3\} is still a unitary set. Things become a bit different when F F has two or more elements. For example, take q = 5 q=5 and F = { 2, 3 } F=\{2,3\}. Then instead of a single (unperturbed) stochastic matrix 𝑷 \bm{P} we now have a pair of such matrices, one for each multiplier:

(22) |  | 𝑷 2, 5 = 1 2 ​ [1 1 0 0 0 0 0 1 1 0 1 0 0 0 1 0 1 1 0 0 0 0 0 1 1], 𝑷 3, 5 = 1 3 ​ [1 1 1 0 0 1 0 0 1 1 0 1 1 1 0 1 1 0 0 1 0 0 1 1 1]. \bm{P}_{2,5}=\frac{1}{2}\begin{bmatrix}1&1&0&0&0\\ 0&0&1&1&0\\ 1&0&0&0&1\\ 0&1&1&0&0\\ 0&0&0&1&1\\ \end{bmatrix}\ \ \ ,\ \ \ \bm{P}_{3,5}=\frac{1}{3}\begin{bmatrix}1&1&1&0&0\\ 1&0&0&1&1\\ 0&1&1&1&0\\ 1&1&0&0&1\\ 0&0&1&1&1\\ \end{bmatrix}\,. |  |

In each of these two matrices, the number of non-zero entries in each row equals the number of possible carryovers (upon multiplication by the corresponding prime).

#### 5.3.2. Heuristics II: Block protection

As we have seen in the previous subsection, in the context of Example 1, each digit x ∈ 𝒜 3 = { 0, 1, 2 } x\in\mathcal{A}_{3}=\{0,1,2\} in a given position on row n n of our MA {\rm MA} gives rise to a new digit y ∈ { y 0, y 1 } y\in\{y_{0},y_{1}\} immediately below it on row n + 1 n+1, where either y = y 0 = 2 ​ x mod 3 y=y_{0}=2x\mod 3 or y = y 1 = 2 ​ x + 1 mod 3 y=y_{1}=2x+1\mod 3, depending on whether the carryover at that position is 0 0 or 1 1, respectively. We have stated that, if the carryovers in row n − 1 n-1 are assumed to be randomly placed, then the transition probabilities for the digit transitions x ↦ y x\mapsto y are equal to 1 2 \frac{1}{2} (hence the stochastic matrix 𝑷 \bm{P} introduced earlier). Strictly speaking, this is not correct. But as we will see below, the statement is close to being true provided the digits on row n n are already approximately uniformly distributed in the following (finite) sense. We say that a k k -block B = x 1 x 2 ⋯ x k ∈ 𝒜 3 k B=x_{1}x_{2}\cdots x_{k}\in{\mathcal{A}}_{3}^{k} occurs in an N N -block ω = z 1 z 2 ⋯ z N ∈ 𝒜 3 N \omega=z_{1}z_{2}\cdots z_{N}\in{\mathcal{A}}_{3}^{N} if there exists 0 ≤ j ≤ N − k 0\leq j\leq N-k such that z j + 1 = x 1, z j + 2 = x 2, …, z j + k = x k z_{j+1}=x_{1}\,,\,z_{j+2}=x_{2}\,,\,\ldots\,,\,z_{j+k}=x_{k}.

###### Definition 2.

An N N -block ω ∈ 𝒜 3 N \omega\in\mathcal{A}_{3}^{N} is said to be k k -balanced (for a given k k with 1 ≤ k < N − 3 k 1\leq k<N-3^{k}) if for each k k -block B ∈ 𝒜 3 k B\in\mathcal{A}_{3}^{k} the total number of ocurrences of B B in ω \omega divided by the total number of k k -blocks occurring in ω \omega is equal to 1 / 3 k 1/3^{k}. 9 9 9 Note that the total number of k k -blocks is 3 k 3^{k}.

The rough idea is that if row n n of our MA {\rm MA} is k k -balanced and we count, for a given allowable transition x ↦ y x\mapsto y, how many times this transition occurs when we go from row n n to row n + 1 n+1 and divide that number by the total number of observed transitions which start with the digit x x, then this ratio – which we call an empirical transition probability – is approximately equal to 1 2 \frac{1}{2}, with an error which is exponentially small in k k. We call this phenomenon block protection. The result can be formulated as follows.

###### Proposition 5.

If the n n -th row { x i, n } 1 ≤ i ≤ k n \{x_{i,n}\}_{1\leq i\leq k_{n}} is k k -balanced for some k ≥ 1 k\geq 1, then the empirical probability p x ​ y ​ ( n) p_{xy}(n) of each transition x ↦ y x\mapsto y (computed from the digit transitions x i, n ↦ x i, n + 1 x_{i,n}\mapsto x_{i,n+1}) satisfies | p x ​ y ​ ( n) − 1 2 | ≤ 1 2 ⋅ 3 k \left|p_{xy}(n)-\frac{1}{2}\right|\leq\frac{1}{2\cdot 3^{k}}.

The proof is deferred to Appendix 5.4.

Instead of looking at transitions x ↦ y x\mapsto y between digits, we may consider more generally transitions X ↦ Y X\mapsto Y between blocks X, Y X,Y of a fixed length ℓ \ell. Here X = x i + ℓ − 1, n ⋯ x i + 1, n x i, n X=x_{i+\ell-1,n}\cdots x_{i+1,n}x_{i,n} lies on row n n of our MA {\rm MA} while Y = x i + ℓ − 1, n + 1 ⋯ x i + 1, n + 1 x i, n + 1 Y=x_{i+\ell-1,n+1}\cdots x_{i+1,n+1}x_{i,n+1} lies on row n + 1 n+1 immediately below X X. For each given X X there are two possible values for Y Y (depending on the carryover c i − 1, n ∈ { 0, 1 } c_{i-1,n}\in\{0,1\}). One can talk about block protection of such blocks in the same way we talked about block protection of digits. An exact analogue of Proposition 5 holds true if we simply replace x x by X X and y y by Y Y, and the proof is similar. The end result is that if row n n of our MA {\rm MA} is k k -balanced, then the empirical transition probabilities p X ​ Y ​ ( n) p_{XY}(n) differ from 1 2 \frac{1}{2} by an error smaller than 3 − k 3^{-k} (where k k is the length of the protecting blocks). To be more specific, let 𝑷 ℓ, n 3, 2 \bm{P}_{\ell,n}^{3,2} be the stochastic matrix that gives the actual transitions of ℓ \ell -blocks from row n n to row n + 1 n+1, and assume that row n n is k k -balanced. For ℓ = 2 \ell=2 there are 3 2 = 9 3^{2}=9 blocks. If all allowed transitions were equally likely, we would get the 9 × 9 9\times 9 stochastic matrix

(23) |  | 𝑷 2 3, 2 = 1 2 ​ [1 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 1 1]. \bm{P}_{2}^{3,2}=\frac{1}{2}\begin{bmatrix}1&1&0&0&0&0&0&0&0\\ 0&0&1&1&0&0&0&0&0\\ 0&0&0&0&1&1&0&0&0\\ 0&0&0&0&0&0&1&1&0\\ 1&0&0&0&0&0&0&0&1\\ 0&1&1&0&0&0&0&0&0\\ 0&0&0&1&1&0&0&0&0\\ 0&0&0&0&0&1&1&0&0\\ 0&0&0&0&0&0&0&1&1\\ \end{bmatrix}\,. |  |

The actual stochastic matrices 𝑷 2, n 3, 2 \bm{P}_{2,n}^{3,2} differ from the above matrix only in its non-zero entries, and by less than 3 − k 3^{-k}, provided row n n is k k -balanced. More generally, for arbitrary ℓ \ell, if all allowed transitions X ↦ Y X\mapsto Y were equally likely, the associated stochastic matrix would be

(24) |  | 𝑷 ℓ 3, 2 = 1 2 ​ [δ i, ( 2 ​ i − 1) mod 3 ℓ + δ i, 2 ​ i mod 3 ℓ] 1 ≤ i, j ≤ 3 ℓ, \bm{P}_{\ell}^{3,2}=\frac{1}{2}\left[\delta_{i,(2i-1)\bmod 3^{\ell}}+\delta_{i,2i\bmod 3^{\ell}}\right]_{1\leq i,j\leq 3^{\ell}}\ , |  |

where δ i, j \delta_{i,j} stands for Kronecker’s delta. Once again, the actual stochastic matrices 𝑷 ℓ, n 3, 2 \bm{P}_{\ell,n}^{3,2} differ from the matrix in ( 24) only in its non-zero entries, and by less than 3 − k 3^{-k} if row n n is k k -balanced.

#### 5.3.3. Heuristics III: How to get a good start

Now we come to the last part of the heuristics. Almost all of what was done in parts I and II of the heuristics can be rigorously proved. This is not the case, so far, with the arguments in the present section. The discussion will be more informal.

The IMC formalism as described in § 5.3.1 can only work if the stochastic matrices 𝑷 ℓ, n 3, 2 \bm{P}_{\ell,n}^{3,2} introduced in § 5.3.2 become asymptotically closer and closer to the corresponding matrices 𝑷 ℓ 3, 2 \bm{P}_{\ell}^{3,2} as n → ∞ n\to\infty, for any given ℓ \ell. Thus, we need

(25) |  | lim n → ∞ ‖ 𝑷 ℓ, n 3, 2 − 𝑷 ℓ 3, 2 ‖ = 0, \lim_{n\to\infty}\left\|\bm{P}_{\ell,n}^{3,2}-\bm{P}_{\ell}^{3,2}\right\|\;=\;0\ , |  |

for any block-length ℓ \ell. This is indeed corroborated by our computational evidence. Proposition 5 gives us a much weaker, conditional result: if the n n -th row N n N_{n} of our MA {\rm MA} is k k -balanced, then ‖ 𝑷 ℓ, n 3, 2 − 𝑷 ℓ 3, 2 ‖ ≤ 3 − k \|\bm{P}_{\ell,n}^{3,2}-\bm{P}_{\ell}^{3,2}\|\leq 3^{-k}. It is of course too much to expect that a row of our MA {\rm MA} will be perfectly k k -balanced. But it is not difficult to generalize Proposition 5 so that the expression “ k k -balanced” is replaced by a suitable concept of “almost k k -balanced” (which can be stated in an appropriate quantitative way), so that the estimate in the conclusion is almost the same, with 3 − k 3^{-k} replaced by O ⁡ ( 3 − k) O(3^{-k}), say. Let us agree to say that the matrix 𝑷 ℓ, n 3, 2 \bm{P}_{\ell,n}^{3,2} is k k -reasonable if ‖ 𝑷 ℓ, n 3, 2 − 𝑷 ℓ 3, 2 ‖ = O ⁡ ( 3 − k) \|\bm{P}_{\ell,n}^{3,2}-\bm{P}_{\ell}^{3,2}\|=O(3^{-k}). The stability of the arguments presented so far then tell us that if row n n of our MA {\rm MA} is almost k k -balanced, then the stochastic matrices 𝑷 ℓ, n + j 3, 2 \bm{P}_{\ell,n+j}^{3,2}, j = 0, 1, …, s − 1 j=0,1,\ldots,s-1 remain k k -reasonable for a certain number s s of steps.

Thus, in order to justify the use of the IMC formalism and get a proof of Conjecture 3 (at least for the case of the MA {\rm MA} of Example 1), we need two things:

1. (1)

To guarantee the possibility of a good start, i.e., a row n n of our automaton which is almost k k -balanced, for as large a value of k k as possible.

2. (2)

To make sure that throughout the steps j = 0, 1, …, s − 1 j=0,1,\ldots,s-1 the longer blocks in N n + j N_{n+j} (*i.e.,*those whose evolutions are not protected by the distributions of even longer blocks) are not progressively getting too unevenly distributed, with consequences that would then cascade down to shorter and shorter blocks.

At least at a rough level, point (1) is not difficult to achieve thanks to our results in § 3. Indeed, by what we have seen in that section, adding a decimal point in front of N n N_{n} (the n n -row of our MA {\rm MA}), we get the orbit x n = T 2, 3 n ​ ( x 0) x_{n}=T_{2,3}^{n}(x_{0}) of x 0 = [0.1] 3 x_{0}=[0.1]_{3} under the circle map T 2, 3 T_{2,3}. Since all orbits of T 2, 3 T_{2,3} are dense, given any k k -balanced string Y = y 1 y 2 ⋯ y m ∈ 𝒜 3 m Y=y_{1}y_{2}\cdots y_{m}\in\mathcal{A}_{3}^{m} (with y 1 ≠ 0 y_{1}\neq 0), there exists n ≥ 1 n\geq 1 such that x n x_{n} has the string Y Y as its m m -prefix, or head, which we call good. For each such n n with a good head, the corresponding N n N_{n} has a suffix, or tail, of a certain length r r. Note that we cannot choose r r a-priori: if one uses the density of orbits of T 2, 3 T_{2,3}, one is forced to accept the value of r r imposed by the choice of the good head Y Y.

Now, as we iterate further and consider the successive rows N n, N n + 1, …, N n + j, … N_{n},N_{n+1},\ldots,\penalty N_{n+j},\ldots of the automaton, the tail of length r r generates a periodic sequence of tails lying beneath it (all with the same length r r), whereas the heads increase in size. Clearly, the constant character of r r as j j increases makes the tails irrelevant in the computation of asymptotic proportions of symbols or other blocks. The problem then becomes point (2) above for the heads. This point is experimentally verified but is mathematically beyond our reach at this writing, contrary to point (1) as formulated above.

### 5.4. Appendix: Proof of Proposition 5

As promised, in this section we prove Proposition 5. The proof will require the two lemmas presented below. Let us fix k ≥ 1 k\geq 1. It is an easy consequence of Proposition 4 that, for each i > k i>k and each n ≥ 1 n\geq 1, the element x i, n + 1 x_{i,n+1} of our MA {\rm MA} is completely determined by the following data:

1. (1)

The element x i, n x_{i,n} lying immediately above x i, n + 1 x_{i,n+1};

2. (2)

The k k -block B i, n, k = x i − 1, n x i − 2, n ⋯ x i − k, n ∈ 𝒜 3 k B_{i,n,k}=x_{i-1,n}x_{i-2,n}\cdots x_{i-k,n}\in{\mathcal{A}}_{3}^{k} lying to the right of x i, n x_{i,n};

3. (3)

The carryover c i − k − 1, n c_{i-k-1,n}, i.e. the carryover immediately to the right of B i, n, k B_{i,n,k}.t

In other words, there exists a function Φ k: 𝒜 3 × 𝒜 3 k × { 0, 1 } → 𝒜 3 \Phi_{k}:\,{\mathcal{A}}_{3}\times{\mathcal{A}}_{3}^{k}\times\{0,1\}\to{\mathcal{A}}_{3} such that

(26) |  | x i, n + 1 = Φ k ​ ( x i, n, B i, n, k, c i − k − 1, n). x_{i,n+1}\;=\;\Phi_{k}\left(x_{i,n}\,,\,B_{i,n,k}\,,\,c_{i-k-1,n}\right)\ . |  |

In fact, the function Φ k \Phi_{k} can be explicitly computed. Define the value of a k k -block B = x 1 x 2 ⋯ x k B=x_{1}x_{2}\cdots x_{k} by

(27) |  | v ⁡ ( B) = ∑ j = 1 k x j ​ 3 k − j. v(B)\;=\;\sum_{j=1}^{k}x_{j}3^{k-j}\ . |  |

Note that every block B B is uniquely determined by its value. We now have the following lemma.

###### Lemma 6.

For each digit x ∈ 𝒜 3 x\in{\mathcal{A}}_{3}, each k k -block B = x 1 x 2 ⋯ x k ∈ 𝒜 3 k B=x_{1}x_{2}\cdots x_{k}\in{\mathcal{A}}_{3}^{k} and each carryover c ∈ { 0, 1 } c\in\{0,1\}, we have

(28) |  | Φ k ​ ( x, B, c) = 2 ​ x + ⌊ 2 ​ v ​ ( B) + c 3 k ⌋ mod 3. \Phi_{k}(x,B,c)\;=\;2x+\left\lfloor\frac{2v(B)+c}{3^{k}}\right\rfloor\ \ \mod 3\ . |  |

###### Proof.

The concatenated block x B = x x 1 x 2 ⋯ x k xB=xx_{1}x_{2}\cdots x_{k} has value v ⁡ ( x ​ B) = 3 k ​ x + v ⁡ ( B) v(xB)=3^{k}x+v(B). In order to compute y = Φ k ​ ( x, B, c) y=\Phi_{k}(x,B,c), we multiply this value by 2 2 and add the carryover c c, getting the number w = 2 ​ v ​ ( x ​ B) + c w=2v(xB)+c. This number is written in base 3 3 and the resulting block is placed beneath x ​ B xB. The digit y y (immediately below x x) is precisely the k k -th digit of w w from right to left, i.e., y = ⌊ w / 3 k ⌋ y=\lfloor w/3^{k}\rfloor. Hence we have

 | y \displaystyle y\; | = ⌊ 2 ​ ( 3 k ​ x + v ⁡ ( B)) + c 3 k ⌋ mod 3 \displaystyle=\;\left\lfloor\frac{2(3^{k}x+v(B))+c}{3^{k}}\right\rfloor\ \ \mod 3 |  |

 |  | = 2 x + ⌊ 2 ​ v ​ ( B) + c 3 k ⌋ mod 3, \displaystyle=\;2x+\left\lfloor\frac{2v(B)+c}{3^{k}}\right\rfloor\ \ \mod 3\ , |  |

and this proves ( 28). ∎

Note that the last term in the right-hand side of ( 28) is equal to either 0 0 or 1 1.

Now, it turns out that Φ k \Phi_{k} is “almost” independent of the variable c ∈ { 0, 1 } c\in\{0,1\}. Roughly speaking, the only way the carryover c c to the right of the k k -block B B can influence the value of the digit y y immediately below x x (on the left of B B) is if B B happens to be the block 𝟏 k = 11 ⋯ 1 \mathbf{1}_{k}=11\cdots 1 ( k k times). Every other block will contain in some position a 0 0 or a 2 2; upon multiplication by 2 2 these yield 0 0 and 1 1, respectively, and any carryover effect coming from the right of that position will not go through to the left of it. This is part (i) of the following lemma.

###### Lemma 7.

The function Φ k \Phi_{k} has the following properties.

1. (i)

If x ∈ 𝒜 3 x\in{\mathcal{A}}_{3} and B ∈ 𝒜 3 k B\in{\mathcal{A}}_{3}^{k}, then Φ k ​ ( x, B, 0) ≠ Φ k ​ ( x, B, 1) \Phi_{k}(x,B,0)\neq\Phi_{k}(x,B,1) if and only if B = 𝟏 k B=\mathbf{1}_{k};

2. (ii)

If x ∈ 𝒜 3 x\in{\mathcal{A}}_{3} and y ∈ { y 0, y 1 } y\in\{y_{0},y_{1}\}, then

 | #⁡ { B ∈ 𝒜 3 k ∖ { 𝟏 k }: Φ k ​ ( x, B, c) = y } = 3 k − 1 2 \#\left\{B\in{\mathcal{A}}_{3}^{k}\setminus\{\mathbf{1}_{k}\}\,:\;\Phi_{k}(x,B,c)=y\right\}\;=\;\frac{3^{k}-1}{2} |  |

###### Proof.

First, let B B be a k k -block such that Φ k ​ ( x, B, 0) ≠ Φ k ​ ( x, B, 1) \Phi_{k}(x,B,0)\neq\Phi_{k}(x,B,1). Then from ( 28) we see that

(29) |  | 0 = ⌊ 2 ​ v ​ ( B) 3 k ⌋ ≠ ⌊ 2 ​ v ​ ( B) + 1 3 k ⌋ = 1. 0\;=\;\left\lfloor\frac{2v(B)}{3^{k}}\right\rfloor\;\neq\;\left\lfloor\frac{2v(B)+1}{3^{k}}\right\rfloor\;=\;1\ . |  |

Hence we must have simultaneously

 | 2 ​ v ​ ( B) 3 k < 1 and 2 ​ v ​ ( B) + 1 3 k ≥ 1 \frac{2v(B)}{3^{k}}\;<\;1\ \ \mathrm{and}\ \ \ \frac{2v(B)+1}{3^{k}}\;\geq\;1 |  |

From these two inequalities we deduce that 3 k − 1 ≤ 2 ​ v ​ ( B) < 3 k 3^{k}-1\leq 2v(B)<3^{k}, and therefore v ⁡ ( B) = 1 2 ​ ( 3 k − 1) v(B)=\frac{1}{2}(3^{k}-1). This means that B = 𝟏 k B=\mathbf{1}_{k}. Conversely, if B = 𝟏 k B=\mathbf{1}_{k} then by a simple computation we see that ( 29) holds true. This proves (i).

To prove (ii), there are two cases to consider: y = y 0 y=y_{0} and y = y 1 y=y_{1}. In either case, if B ∈ 𝒜 3 k ∖ { 𝟏 k } B\in{\mathcal{A}}_{3}^{k}\setminus\{\mathbf{1}_{k}\} then by part (i) we have

(30) |  | ⌊ 2 ​ v ​ ( B) 3 k ⌋ = ⌊ 2 ​ v ​ ( B) + 1 3 k ⌋ \left\lfloor\frac{2v(B)}{3^{k}}\right\rfloor\;=\;\left\lfloor\frac{2v(B)+1}{3^{k}}\right\rfloor |  |

If y = y 0 y=y_{0}, then both sides in ( 30) are equal to 0 0, and we get 0 ≤ v ⁡ ( B) < 1 2 ​ ( 3 k − 1) 0\leq v(B)<\frac{1}{2}(3^{k}-1). The number of blocks B B satisfying these inequalities is precisely 1 2 ​ ( 3 k − 1) \frac{1}{2}(3^{k}-1). If y = y 1 y=y_{1}, then both sides in ( 30) are equal to 1 1, and this time we deduce that 1 2 ​ ( 3 k + 1) ≤ v ⁡ ( B) ≤ 3 k − 1 \frac{1}{2}(3^{k}+1)\leq v(B)\leq 3^{k}-1. The number of blocks B B satisfying these last inequalities is also 1 2 ​ ( 3 k − 1) \frac{1}{2}(3^{k}-1). This finishes the proof. ∎

Here is some space at the top

Here is some more space

[image: Refer to caption]

Figure 3. The two multiplication automata of Example 2.

#### Proof of Proposition 5

Consider an allowable transition of digits x ↦ y x\mapsto y from row n n to row n + 1 n+1 of our MA {\rm MA}. We are assuming that row n n is k k -balanced. In order to compute the empirical probability p x ​ y ​ ( n) p_{xy}(n) of such transition, we need to count how many times this transition happens and divide it by the total number of transitions which start with x x on row n n. For this purpose, first we count how many blocks B ∈ 𝒜 3 k ∖ { 𝟏 k } B\in{\mathcal{A}}_{3}^{k}\setminus\{\mathbf{1}_{k}\} are such that Φ k ​ ( x, B, c) = y \Phi_{k}(x,B,c)=y. The answer is given by Lemma 7 (ii): there are 1 2 ​ ( 3 k − 1) \frac{1}{2}(3^{k}-1) such blocks. Since row n n of our MA {\rm MA} is k k -balanced, the proportion of such blocks in that row is therefore the quotient 1 2 ​ ( 3 k − 1) / 3 k \frac{1}{2}(3^{k}-1)/3^{k}. This already tells us that

(31) |  | p x ​ y ​ ( n) ≥ 1 2 − 1 2 ⋅ 3 k p_{xy}(n)\geq\frac{1}{2}-\frac{1}{2\cdot 3^{k}} |  |

We still have to account for the occurences of the block B = 𝟏 k B=\mathbf{1}_{k}. Let c ∈ { 0, 1 } c\in\{0,1\} be such that Φ k ​ ( x, 𝟏 k, c) = y \Phi_{k}(x,\mathbf{1}_{k},c)=y. Each occurrence of B = 𝟏 k B=\mathbf{1}_{k} on row n n for which the carryover immediately to the right of B B equals c c contributes to the desired empirical probability. Since the proportion of such occurrences is at most 1 3 k \frac{1}{3^{k}}, this shows that

(32) |  | p x ​ y ​ ( n) ≤ 1 2 − 1 2 ⋅ 3 k + 1 3 k = 1 2 + 1 2 ⋅ 3 k. p_{xy}(n)\leq\frac{1}{2}-\frac{1}{2\cdot 3^{k}}+\frac{1}{3^{k}}=\frac{1}{2}+\frac{1}{2\cdot 3^{k}}\ . |  |

Combining ( 31) with ( 32) we get the inequality in the statement. ∎

Here is some space at the top

Here is some space at the top

[image: Refer to caption]

Figure 4. This figure plots the proportion of the digit 0 0 in the base- 3 3 expansion of 2 n 2^{n} as a function of n n; note the apparent convergence to 1 3 \frac{1}{3}.

Here is some space at the top

[image: Refer to caption]

Figure 5. Carryover structure for the two automata (horizontal and vertical) associated to Example 1.

## Acknowledgements

The authors are grateful to George Hentchel for bringing this problem to the attention of C.T., and for sharing insights on how asymptotic equidistribution of digits would solve Sloane’s problem in base 3 3.

## References

- [B] P. Brémaud. *Markov Chains: Gibbs Fields, Monte Carlo Simulation and Queues*. Texts in Applied Mathematics 31, Springer-Verlag, 1999.
- [Bo] M. Boshernitzan. *Dense orbits of rationals*. Proc. Amer. Math. Soc. 117 (1993), 1201–1203.
- [G] R. K. Guy, *Unsolved Problems in Number Theory*. 2nd ed., Springer-Verlag, New York, 1994.
- [He] G. Hedlund. *Endomorphisms and automorphisms of the shift dynamical systems*. Mathematical System Theory 3, (1969) 320–375.
- [H] H.J. Hinden. *The additive persistence of a number*. Journal of Recreational Mathematics 7 (1974), 134–135.
- [IM] D.L. Isaacson & R.W. Madsen. *Markov Chains: Theory and Applications*. John Wiley and Sons, New York, 1976.
- [K] G. Keller. *Equilibrium States in Ergodic Theory*. London Mathematical Society Student Texts 42, Cambridge University Press, 1998.
- [L] J.C. Lagarias. *Ternary expansions of powers of 2*. J. London Math. Soc. (2) 79 (2009), 562–588.
- [LeV] W. LeVeque. *Fundamentals of Number Theory*. Addison-Wesley, Reading, Massachusetts, 1977.
- [Li] I. Liousse. *PL Homeomorphisms of the circle that are piecewise C 1 C^{1} conjugate to irrational rotations*. Bull. Braz. Math. Soc. 35 (2004), 269–280.
- [M] P. Mihăilescu. *Primary cyclotomic units and a proof of Catalan’s conjecture*. J. Reine Angew. Math. 572 (2004), 167–195.
- [P] M. Pivato, *Multiplicative cellular automata on nilpotent groups: structure, entropy, and asymptotics*. J. Statist. Phys. 110 (2003), 247–267.
- [S] N. Sloane. *The persistence of a number*. Journal of Recreational Mathematics 6 (1973), 97–98.
- [Tr] C. Tresser, *Bounding the errors for convex dynamics on one or more polytopes*. Chaos 17 (2007), 33–49.
- [W] P. Walters. *An introduction to Ergodic Theory*. Graduate Texts in Mathematics 79, Springer Verlag, New York, 1982.
- [T] T. Tao. *The Collatz conjecture, Littlewood-Offord theory, and powers of 2 and 3*. Blog entry in http://terrytao.wordpress.com, 2011.

[◄][3][image: ar5iv homepage] [4]
[Feeling lucky?][5] [6]
[Conversion report][7]
[Report an issue][8]
[View original on arXiv][9] [►][10]


## Links

[1]: mailto:edson@ime.usp.br
[2]: mailto:charlestresser@yahoo.com
[3]: /html/1307.1187
[4]: /
[5]: /feeling_lucky
[6]: /land_of_honey_and_milk
[7]: /log/1307.1188
[8]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1307.1188
[9]: https://arxiv.org/pdf/1307.1188
[10]: /html/1307.1189
