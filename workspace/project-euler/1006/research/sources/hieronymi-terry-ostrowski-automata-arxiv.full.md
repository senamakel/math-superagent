<!-- source: https://ar5iv.labs.arxiv.org/html/1407.7000 | converted from HTML -->

[1407.7000] Ostrowski numeration systems, addition and finite automata

# Ostrowski numeration systems, addition and finite automata Thanks: The first author was partially supported by NSF grant DMS-1300402 and by UIUC Campus Research Board award 13086. A version of this paper will appear in the *Notre Dame Journal of Formal Logic.*

Philipp Hieronymi Address: Department of Mathematics
University of Illinois at Urbana-Champaign
1409 West Green Street
Urbana, IL 61801 Email address: [phierony@illinois.edu][1] URL: [http://www.math.uiuc.edu/~phierony][2] and Alonza Terry Jr Address: Department of Mathematics
University of Illinois at Urbana-Champaign
1409 West Green Street
Urbana, IL 61801 Email address: [aterry@illinois.edu][3]

Date: August 9, 2026

###### Abstract.

We present an elementary three pass algorithm for computing addition in Ostrowski numerations systems. When a a is quadratic, addition in the Ostrowski numeration system based on a a is recognizable by a finite automaton. We deduce that a subset of X ⊆ ℕ n X\subseteq\mathbb{N}^{n} is definable in ( ℕ, +, V a) (\mathbb{N},+,V_{a}), where V a V_{a} is the function that maps a natural number x x to the smallest denominator of a convergent of a a that appears in the Ostrowski representation based on a a of x x with a non-zero coefficient, if and only if the set of Ostrowski representations of elements of X X is recognizable by a finite automaton. The decidability of the theory of ( ℕ, +, V a) (\mathbb{N},+,V_{a}) follows.

## 1. Introduction

A continued fraction expansion [a 0; a 1, …, a k, …] [a_{0};a_{1},\dots,a_{k},\dots] is an expression of the form

 | a 0 + 1 a 1 + 1 a 2 + 1 a 3 + 1 ⋱ a_{0}+\frac{1}{a_{1}+\frac{1}{a_{2}+\frac{1}{a_{3}+\frac{1}{\ddots}}}} |  |

For a real number a a, we say [a 0; a 1, …, a k, …] [a_{0};a_{1},\dots,a_{k},\dots] is the continued fraction expansion of a a if a = [a 0; a 1, …, a k, ⋯] a=[a_{0};a_{1},\dots,a_{k},\cdots] and a 0 ∈ ℤ a_{0}\in\mathbb{Z}, a i ∈ ℕ > 0 a_{i}\in\mathbb{N}_{>0} for i > 0 i>0. Let a a be a real number with continued fraction expansion [a 0; a 1, …, a k, …] [a_{0};a_{1},\dots,a_{k},\dots]. In this note we study a numeration system due to Ostrowski [13] based on the continued fraction expansion of a a. Set q − 1:= 0 q_{-1}:=0 and q 0:= 1 q_{0}:=1, and for k ≥ 0 k\geq 0,

(1.1) |  | q k + 1:= a k + 1 ⋅ q k + q k − 1. q_{k+1}:=a_{k+1}\cdot q_{k}+q_{k-1}. |  |

Then every natural number N N can be written uniquely as

 | N = ∑ k = 0 n b k + 1 ​ q k, N=\sum_{k=0}^{n}b_{k+1}q_{k}, |  |

where b k ∈ ℕ b_{k}\in\mathbb{N} such that b 1 < a 1 b_{1}<a_{1}, b k ≤ a k b_{k}\leq a_{k} and, if b k = a k b_{k}=a_{k}, b k − 1 = 0 b_{k-1}=0. We say the word b n ​ … ​ b 1 b_{n}\dots b_{1} is the Ostrowski representation of N N based on a a, and we write ρ a ​ ( N) \rho_{a}(N) for this word. For more details on Ostrowski representations, see for example Allouche and Shallit [2, p.106] or Rockett and Szüsz [14, Chapter II.4]. When a a is the golden ratio ϕ:= 1 + 5 2 \phi:=\frac{1+\sqrt{5}}{2}, the continued fraction expansion of a a is [1; 1, …] [1;1,\dots]. In this special case the sequence ( q k) k ∈ ℕ (q_{k})_{k\in\mathbb{N}} is the sequence of Fibonacci numbers. Thus the Ostrowski representation based on the golden ratio is precisely the better known Zeckendorf representation [17].

In this paper, we will study the following question: given the continued fraction expansion of a a and the Ostrowski representation of two natural numbers based on a a, is there an easy way to compute the Ostrowski representation of their sum? Ahlbach, Usatine, Frougny and Pippenger [1] give an elegant algorithm to calculate the sum of two natural numbers in Zeckendorf representations. In this paper we generalize their work and present an elementary three pass algorithm for computing the sum of two natural numbers given in Ostrowski representation. To be precise, we show that given the continued fraction expansion of a a, addition of two n n -digit numbers in Ostrowski representation based on a a can be computed by three linear passes over the input sequence and hence in time O ⁡ ( n) O(n). If a a is a quadratic number 1 1 1 A real number a a is quadratic if it is a solution to a quadratic equation with rational coefficients, we establish that the graph of addition in the Ostrowski numeration system based on a a can be recognized by a finite automaton (see Theorem B for a precise statement). When a a is the golden ratio, this result is due to Frougny [8] 2 2 2 In private communication Frougny proved that whenever the continued fraction expansion of a has period 1, the stronger statement that addition in the Ostrowski numeration system associated with a a can be obtained by three linear passes, one left-to-right, one right-to-left and one left-to-right, where each of the passes defines a finite sequential transducer..

Ostrowski representations arose in number theory and have strong connections to the combinatorics of words (see for example Berthé [3]). However, our main motivation for studying Ostrowski representations is their application to decidability and definability questions in mathematical logic. The results in this paper (in particular Theorem B below) play a crucial role in the work of the first author [9] on expansions of the real additive group. Here we will present the following application of our work on addition in the Ostrowski numeration system to the study of expansions of Presburger Arithmetic (see Theorem A).

Let a a be quadratic. Since the continued fraction expansion of a a is periodic, there is a natural number c:= max k ∈ ℕ ⁡ a k c:=\max_{k\in\mathbb{N}}a_{k}. Let Σ a = { 0, …, c } \Sigma_{a}=\{0,\dots,c\}. So ρ a ​ ( N) \rho_{a}(N) is a Σ a \Sigma_{a} -word. Let V a: ℕ → ℕ V_{a}:\mathbb{N}\to\mathbb{N} be the function that maps x ≥ 1 x\geq 1 with Ostrowski representation b n ​ … ​ b 1 b_{n}\dots b_{1} to the least q k q_{k} with b k + 1 ≠ 0 b_{k+1}\neq 0, and 0 0 to 1 1.

###### Theorem A.

Let a a be quadratic. A set X ⊆ ℕ n X\subseteq\mathbb{N}^{n} is definable in ( ℕ, +, V a) (\mathbb{N},+,V_{a}) if and only if X X is a a -recognizable. Hence the theory of ( ℕ, +, V a) (\mathbb{N},+,V_{a}) is decidable.

We say a set X ⊆ ℕ X\subseteq\mathbb{N} is a a -recognizable if 0 ∗ ​ ρ a ​ ( X) 0^{*}\rho_{a}(X) is recognizable by a finite automaton, where 0 ∗ ​ ρ a ​ ( X) 0^{*}\rho_{a}(X) is the set of all Σ a \Sigma_{a} -words of the form 0 ​ … ​ 0 ​ ρ a ​ ( N) 0\dots 0\rho_{a}(N) for some N ∈ X N\in X. The definition of a a -recognizability for subsets of ℕ n \mathbb{N}^{n} is slightly more technical and we postpone it to Section 3. The decidability of the theory of ( ℕ, +, V a) (\mathbb{N},+,V_{a}) follows immediately from the first part of the statement of Theorem A and Kleene’s theorem (see Khoussainov and Nerode [11, Theorem 2.7.2]) that the emptiness problem for finite automata is decidable. Bruyère and Hansel [4, Theorem 16] establish Theorem A when a a is the golden ratio. In fact, they show that Theorem A holds for linear numeration systems whose characteristic polynomial is the minimal polynomial of a Pisot number. A similar result for numeration systems based on ( p n) n ∈ ℕ (p^{n})_{n\in\mathbb{N}}, where p > 1 p>1 is an integer, is due to Büchi [6] (for a full proof see Bruyère, Hansel, Michaux and and Villemaire [5]). It is known by Shallit [15] and Loraud [12, Theorem 7] that the set ℕ \mathbb{N} is a a -recognizable if and only if a a is quadratic. So in general the conclusion of Theorem A fails when a a is not quadratic.

A few remarks about the proof of Theorem A are in order. The proof that every definable set is a a -recognizable, is rather straightforward, and we follow a similar argument from Villemaire [16]. For the other direction, by Hodgson [10] it is enough to prove that ℕ \mathbb{N}, the graph of V a V_{a} and the graph of + + are a a -recognizable. While it is easy to check the a a -recognizability of the graph of V a V_{a}, we have to use our algorithm for addition in Ostrowski numeration systems to show that the graph of + + is a a -recognizable. Thus most of the work towards proving Theorem A goes into showing the following result.

###### Theorem B.

Let a a is a quadratic. Then { ( x, y, z) ∈ ℕ 3: x + y = z } \{(x,y,z)\in\mathbb{N}^{3}\ :\ x+y=z\} is a a -recognizable.

We end this introduction with a brief comment about possible applications of Theorem B to the theory of Sturmian words 3 3 3 When preparing this paper, the authors were completely unaware of the connection between Sturmian words and Ostrowski representations. We would like to thank the anonymous referee to point out this connection.. Let a a be a real number in [0, 1] [0,1]. We define

 | f a ​ ( n):= ⌊ ( n + 1) ​ a ⌋ − ⌊ n ​ a ⌋, f_{a}(n):=\lfloor(n+1)a\rfloor-\lfloor na\rfloor, |  |

and we denote the infinite { 0, 1 } \{0,1\} -word f a ​ ( 1) ​ f a ​ ( 2) ​ … f_{a}(1)f_{a}(2)\dots by 𝒇 a \boldsymbol{f}_{a}. This word is called the Sturmian characteristic word with slope a a. If a a is a quadratic irrational, the set { n ∈ ℕ: f a ​ ( n) = 1 } \{n\in\mathbb{N}\ :f_{a}(n)=1\} is a a -recognizable (see [2, Theorem 9.1.15]). Du, Mousavi, Schaeffer and Shallit [7] use this connection and Theorem B in the case of the golden ratio ϕ \phi to prove results about the Fibonacci word (that is the Sturmian characteristic word with slope ϕ − 1 \phi-1). Because of Theorem B the techniques in [7] can be applied to any characteristic Sturmian word whose slope is a quadratic irrational.

### Notation

We denote the set of natural numbers by { 0, 1, 2, … } \{0,1,2,\dots\} by ℕ \mathbb{N}. Definable will always mean definable without parameters. If Σ \Sigma is a finite set, we denote the set of Σ \Sigma -words by Σ ∗ \Sigma^{*}. If a ∈ Σ a\in\Sigma and X ⊆ Σ ∗ X\subseteq\Sigma^{*}, we denote the set { a ​ … ​ a ​ w: w ∈ X } \{a\dots aw\ :\ w\in X\} of Σ \Sigma -words by a ∗ ​ X a^{*}X. If x ∈ X m x\in X^{m} for some set X X, we write x i x_{i} for the i i -th coordinate of x x.

## 2. Ostrowski addition

Fix a real number a a with continued fraction expansion [a 0; a 1, …, a k, …] [a_{0};a_{1},\dots,a_{k},\dots]. In this section we present an algorithm to compute the Ostrowski representations based on a a of the sum of two natural numbers given in Ostrowski representation based on a a. Since we will only consider Ostrowski representation based on a a, we will omit the reference to a a. In the special case that a a is the golden ratio, our algorithm is exactly the one presented in [1]. Although it is not strictly necessary, the reader might find it useful to read [1, Section 2] first.

Let M, N ∈ ℕ M,N\in\mathbb{N} and let x n ​ … ​ x 1, y n ​ … ​ y 1 x_{n}\dots x_{1},y_{n}\dots y_{1} be the Ostrowski representations of M M and N N. We will describe an algorithm that given the continued fraction expansion of a a calculates the Ostrowski representation of M + N M+N. Let s s be the word s n + 1 ​ s n ​ … ​ s 1 s_{n+1}s_{n}\dots s_{1} given by

 | s i:= x i + y i, s_{i}:=x_{i}+y_{i}, |  |

for i = 1, …, n i=1,\dots,n and s n + 1:= 0 s_{n+1}:=0. For ease of notation, we set m:= n + 1 m:=n+1.

The algorithm consists of three linear passes over s s: one left-to-right, one right-to-left and one left-to-right. These three passes will change the word s s into a word that is the Ostrowski representation of M + N M+N. The first pass converts s s into a word whose digit at position k k is smaller or equal to a k a_{k}. The idea how to achieve this, is as follows. We will argue (see Lemma 2.4) that whenever the digit at position k k is larger or equal to a k a_{k}, then the preceding digit has to be less than a k + 1 a_{k+1}. Using ( 2.1) we can then decrease the digit at position k k by a k a_{k}, without increasing the one at position k + 1 k+1 above a k + 1 a_{k+1}, and without changing the value the word represents. The resulting word might not yet be an Ostrowski representation of M + N M+N, because the digit at position k k may be a k a_{k} and not followed by 0 0. With the second and third pass we eliminate all such occurrences.

The first step is an algorithm that makes a left-to-right pass over the sequence s m ​ … ​ s 1 s_{m}\dots s_{1} starting at m m. That means that it starts with the most significant digit, in this case s m s_{m}, and works its way down to the least significant digit s 1 s_{1}. The algorithm can best be described in terms of a moving window of width four. At each step, we only consider the entries in this window. After any possible changes are performed, the window moves one position to the right. When the window reaches the last four digits, the changes are carried out as usual. Afterwards, one final operation is performed on the last three digits. The precise algorithm is as follows. Given s = s m ​ … ​ s 1 s=s_{m}\dots s_{1}, we will recursively define for every k ∈ ℕ k\in\mathbb{N} with 3 ≤ k ≤ m + 1 3\leq k\leq m+1, a word

 | z k:= z k, m ​ z k, m − 1 ​ … ​ z k, 2 ​ z k, 1. z_{k}:=z_{k,m}z_{k,m-1}\dots z_{k,2}z_{k,1}. |  |

###### Algorithm 1.

Let k = m + 1 k=m+1. Then set

 | z m + 1:= s m ​ … ​ s 1. z_{m+1}:=s_{m}\dots s_{1}. |  |

Let k ∈ ℕ k\in\mathbb{N} with 4 ≤ k < m + 1 4\leq k<m+1. We now define z k = z k, m ​ z k, m − 1 ​ … ​ z k, 2 ​ z k 1 z_{k}=z_{k,m}z_{k,m-1}\dots z_{k,2}z_{k_{1}}:

- •

for i ∉ { k, k − 1, k − 2, k − 3 } i\notin\{k,k-1,k-2,k-3\}, we set z k, i = z k + 1, i z_{k,i}=z_{k+1,i},

- •

the subword z k, k ​ z k, k − 1 ​ z k, k − 2 ​ z k, k − 3 z_{k,k}z_{k,k-1}z_{k,k-2}z_{k,k-3} is determined as follows:

  1. (A1)

if z k + 1, k ​ < a k, z k + 1, k − 1 > ​ a k − 1 z_{k+1,k}<a_{k},z_{k+1,k-1}>a_{k-1} and z k + 1, k − 2 = 0 z_{k+1,k-2}=0,

 | z k, k ​ z k, k − 1 ​ z k, k − 2 ​ z k, k − 3 = ( z k + 1, k + 1) ​ ( z k + 1, k − 1 − ( a k − 1 + 1)) ​ ( a k − 2 − 1) ​ ( z k + 1, k − 3 + 1) z_{k,k}z_{k,k-1}z_{k,k-2}z_{k,k-3}=(z_{k+1,k}+1)(z_{k+1,k-1}-(a_{k-1}+1))(a_{k-2}-1)(z_{k+1,k-3}+1) |  |

  2. (A2)

if z k + 1, k < a k, a k − 1 ≤ z k + 1, k − 1 ≤ 2 ​ a k − 1 z_{k+1,k}<a_{k},a_{k-1}\leq z_{k+1,k-1}\leq 2a_{k-1} and z k + 1, k − 2 > 0 z_{k+1,k-2}>0,

 | z k, k ​ z k, k − 1 ​ z k, k − 2 ​ z k, k − 3 = ( z k + 1, k + 1) ​ ( z k + 1, k − 1 − a k − 1) ​ ( z k + 1, k − 2 − 1) ​ ( z k + 1, k − 3) z_{k,k}z_{k,k-1}z_{k,k-2}z_{k,k-3}=(z_{k+1,k}+1)(z_{k+1,k-1}-a_{k-1})(z_{k+1,k-2}-1)(z_{k+1,k-3}) |  |

  3. (A3)

otherwise,

 | z k, k ​ z k, k − 1 ​ z k, k − 2 ​ z k, k − 3 = z k + 1, k ​ z k + 1, k − 1 ​ z k + 1, k − 2 ​ z k + 1, k − 3. z_{k,k}z_{k,k-1}z_{k,k-2}z_{k,k-3}=z_{k+1,k}z_{k+1,k-1}z_{k+1,k-2}z_{k+1,k-3}. |  |

Let k = 3 k=3. We now define z 3 = z 3, m ​ … ​ z 3, 1 z_{3}=z_{3,m}\dots z_{3,1}:

- •

for i ∉ { 1, 2, 3 } i\notin\{1,2,3\}, we set z 3, l = z 4, l z_{3,l}=z_{4,l},

- •

the subword z 3, 3 ​ z 3, 2 ​ z 3, 1 z_{3,3}z_{3,2}z_{3,1} is determined as follows:

  1. (B1)

if z 4, 3 < a 3 z_{4,3}<a_{3}, z 4, 2 > a 2 z_{4,2}>a_{2} and z 4, 1 = 0 z_{4,1}=0,

 | z 3, 3 ​ z 3, 2 ​ z 3, 1 = ( z 4, 3 + 1) ​ ( z 4, 2 − ( a 2 + 1)) ​ ( a 1 − 1), z_{3,3}z_{3,2}z_{3,1}=(z_{4,3}+1)(z_{4,2}-(a_{2}+1))(a_{1}-1), |  |

  2. (B2)

if z 4, 3 < a 3 z_{4,3}<a_{3}, z 4, 2 ≥ a 2 z_{4,2}\geq a_{2} and a 1 ≥ z 4, 1 > 0 a_{1}\geq z_{4,1}>0,

 | z 3, 3 ​ z 3, 2 ​ z 3, 1 = ( z 4, 3 + 1) ​ ( z 4, 2 − a 2) ​ ( z 4, 1 − 1), z_{3,3}z_{3,2}z_{3,1}=(z_{4,3}+1)(z_{4,2}-a_{2})(z_{4,1}-1), |  |

  3. (B3)

if z 4, 3 < a 3 z_{4,3}<a_{3}, z 4, 2 ≥ a 2 z_{4,2}\geq a_{2} and z 4, 1 > a 1 z_{4,1}>a_{1},

 | z 3, 3 ​ z 3, 2 ​ z 3, 1 = ( z 4, 3 + 1) ​ ( z 4, 2 − a 2 + 1) ​ ( z 4, 1 − a 1 − 1), z_{3,3}z_{3,2}z_{3,1}=(z_{4,3}+1)(z_{4,2}-a_{2}+1)(z_{4,1}-a_{1}-1), |  |

  4. (B4)

if z 4, 2 < a 2 z_{4,2}<a_{2} and z 4, 1 ≥ a 1 z_{4,1}\geq a_{1},

 | z 3, 3 ​ z 3, 2 ​ z 3, 1 = z 4, 3 ​ ( z 4, 2 + 1) ​ ( z 4, 1 − a 1). z_{3,3}z_{3,2}z_{3,1}=z_{4,3}(z_{4,2}+1)(z_{4,1}-a_{1}). |  |

  5. (B5)

otherwise,

 | z 3, 3 ​ z 3, 2 ​ z 3, 1 = z 4, 3 ​ z 4, 2 ​ z 4, 1. z_{3,3}z_{3,2}z_{3,1}=z_{4,3}z_{4,2}z_{4,1}. |  |

When we speak of the entry at position l l after step k k, we mean z k, l z_{k,l}. When z k + 1, l ≠ z k, l z_{k+1,l}\neq z_{k,l}, we say that at step k k the entry in position l l was changed. It follows immediately from the algorithm that the only entries changed at step k k, are in position k, k − 1, k − 2 k,k-1,k-2 or k − 3 k-3.

The goal of Algorithm 1 is to produce a word whose entry at position k k is smaller or equal to a k a_{k}, and which represents the same value as s s. The following two Propositions make this statement precise.

###### Proposition 2.1.

Algorithm 1 leaves the value represented unchanged. That is, for every k ∈ ℕ k\in\mathbb{N} with 3 ≤ k ≤ m + 1 3\leq k\leq m+1

 | ∑ i = 0 m z k, i + 1 ​ q i = ∑ i = 0 m s i + 1 ​ q i. \sum_{i=0}^{m}z_{k,i+1}q_{i}=\sum_{i=0}^{m}s_{i+1}q_{i}. |  |

###### Proof.

It follows immediately from the recursive definition of the q i q_{i} ’s (see ( 1.1)) that each rule of Algorithm 1 leaves the value represented unchanged. Induction on k k gives the statement of the Proposition. ∎

###### Proposition 2.2.

For k > 1 k>1, z 3, k ≤ a k z_{3,k}\leq a_{k} and z 3, 1 ≤ a 1 − 1 z_{3,1}\leq a_{1}-1.

We will prove the following two lemmas first.

###### Lemma 2.3.

Let k ∈ ℕ k\in\mathbb{N} and k ≥ 3 k\geq 3. Then

- (i)

If z k + 1, k − 1 = 2 ​ a k − 1 + 1 z_{k+1,k-1}=2a_{k-1}+1, then z k + 1, k − 2 = 0 z_{k+1,k-2}=0.

- (ii)

If z k + 1, k − 1 = 2 ​ a k − 1 z_{k+1,k-1}=2a_{k-1}, then z k + 1, k − 2 ≤ a k − 2 z_{k+1,k-2}\leq a_{k-2}.

###### Proof.

For (i), let z k + 1, k − 1 = 2 ​ a k − 1 + 1 z_{k+1,k-1}=2a_{k-1}+1. It follows immediately from the rules of the algorithm that z k + 2, k − 1 = 2 ​ a k − 1 + 1 z_{k+2,k-1}=2a_{k-1}+1 and z m + 1, k − 1 = 2 ​ a k − 1 z_{m+1,k-1}=2a_{k-1}. So x k − 1 x_{k-1} and y k − 1 y_{k-1} are both equal to a k − 1 a_{k-1}. Hence x k − 2 = 0, y k − 2 = 0 x_{k-2}=0,y_{k-2}=0 and z m + 1, k − 2 = 0 z_{m+1,k-2}=0. The first time that the entry in position k − 2 k-2 can be changed, is at step k + 1 k+1, when rule (A1) is applied. However, since z k + 2, k − 1 = 2 ​ a k − 1 + 1 z_{k+2,k-1}=2a_{k-1}+1, rule (A1) was not applied at step k + 1 k+1. Thus z k + 1, k − 2 = z m + 1, k − 2 = 0 z_{k+1,k-2}=z_{m+1,k-2}=0.

For (ii), let z k + 1, k − 1 = 2 ​ a k − 1 z_{k+1,k-1}=2a_{k-1}. If x k − 1 = y k − 1 = a k − 1 x_{k-1}=y_{k-1}=a_{k-1}, we argue as before to get z k + 1, k − 2 = 0 z_{k+1,k-2}=0. Suppose that either x k − 1 ≠ a k − 1 x_{k-1}\neq a_{k-1} or y k − 1 ≠ a k − 1 y_{k-1}\neq a_{k-1}. Because z k + 1, k − 1 = 2 ​ a k − 1 z_{k+1,k-1}=2a_{k-1}, we get that x k − 1 + y k − 1 = 2 ​ a k − 1 − 1 x_{k-1}+y_{k-1}=2a_{k-1}-1, and that the entry in position k − 1 k-1 had to be increased by 1 1 at step k + 2 k+2. Hence either x k − 1 = a k − 1 x_{k-1}=a_{k-1} or y k − 1 = a k − 1 y_{k-1}=a_{k-1}. By the definition of Ostrowski representations, x k − 2 + y k − 2 ≤ a k − 2 x_{k-2}+y_{k-2}\leq a_{k-2}. Thus z k + 2, k − 2 ≤ a k − 2 z_{k+2,k-2}\leq a_{k-2}. Since the entry in position k − 1 k-1 was increased by 1 1 at step k + 2 k+2, z k + 2, k = a k − 1 z_{k+2,k}=a_{k}-1. Thus no change is made at step k + 1 k+1. It follows that z k + 1, k − 2 = x k − 2 + y k − 2 ≤ a k − 2 z_{k+1,k-2}=x_{k-2}+y_{k-2}\leq a_{k-2}. ∎

###### Lemma 2.4.

Let k ∈ ℕ k\in\mathbb{N} and 3 ≤ k ≤ m 3\leq k\leq m.

- (i OPEN) k)_{k}

If z k + 1, k − 1 > a k − 1 z_{k+1,k-1}>a_{k-1}, then z k + 1, k < a k z_{k+1,k}<a_{k}.

- (ii OPEN) k)_{k}

If z k + 1, k − 1 = a k − 1 z_{k+1,k-1}=a_{k-1} and z k + 1, k − 2 > 0 z_{k+1,k-2}>0, then z k + 1, k < a k z_{k+1,k}<a_{k}.

###### Proof.

We prove the statements by induction on k k. For k = m k=m, both (i OPEN) m)_{m} and (ii OPEN) m)_{m} hold, because z m + 1, m = 0 z_{m+1,m}=0. For the induction step, suppose that (i OPEN) k + 1)_{k+1} and (ii OPEN) k + 1)_{k+1} hold. We need to establish (i OPEN) k)_{k} and (ii OPEN) k)_{k}.

We first show (i OPEN) k)_{k}. Suppose z k + 1, k − 1 > a k − 1 z_{k+1,k-1}>a_{k-1}. Towards a contradiction, assume that z k + 1, k ≥ a k z_{k+1,k}\geq a_{k}. Since z k + 1, k − 1 > a k − 1 z_{k+1,k-1}>a_{k-1} and the algorithm does not increase the entry in position k − 1 k-1 above a k − 1 a_{k-1} at step k + 1 k+1, we have z k + 2, k − 1 > a k − 1 z_{k+2,k-1}>a_{k-1}. Because z k + 1, k ≥ a k z_{k+1,k}\geq a_{k} and the algorithm either leaves the entry in position k k at step k + 1 k+1 untouched or decreases it by a k a_{k} or a k + 1 a_{k}+1, we get that either z k + 2, k = z k + 1, k z_{k+2,k}=z_{k+1,k} or z k + 2, k ∈ { 2 ​ a k, 2 ​ a k + 1 } z_{k+2,k}\in\{2a_{k},2a_{k}+1\}. We handle these cases separately.

Suppose z k + 2, k ∈ { 2 ​ a k, 2 ​ a k + 1 } z_{k+2,k}\in\{2a_{k},2a_{k}+1\}. By (i OPEN) k + 1)_{k+1}, z k + 2, k + 1 < a k + 1 z_{k+2,k+1}<a_{k+1}. It follows from Lemma 2.3 that, if z k + 2, k = 2 ​ a k z_{k+2,k}=2a_{k}, then z k + 2, k − 1 ≤ a k − 1 z_{k+2,k-1}\leq a_{k-1}, and if z k + 2, k = 2 ​ a k + 1 z_{k+2,k}=2a_{k}+1, then z k + 2, k − 1 = 0 z_{k+2,k-1}=0. Since one of the first two rules is applied at step k + 1 k+1, we have that z k + 1, k − 1 < a k − 1 z_{k+1,k-1}<a_{k-1}. This contradicts our assumption that z k + 1, k − 1 > a k − 1 z_{k+1,k-1}>a_{k-1}.

Now, we suppose that z k + 2, k = z k + 1, k z_{k+2,k}=z_{k+1,k} and z k + 2, k = a k z_{k+2,k}=a_{k}. Because z k + 2, k − 1 > a k − 1 z_{k+2,k-1}>a_{k-1}, we get z k + 2, k + 1 < a k + 1 z_{k+2,k+1}<a_{k+1} by (ii OPEN) k + 1)_{k+1}. Hence z k + 1, k = z k + 2, k − a k z_{k+1,k}=z_{k+2,k}-a_{k} by rule (A2). This contradicts z k + 1, k = z k + 2, k z_{k+1,k}=z_{k+2,k}.

Finally, assume that z k + 2, k = z k + 1, k z_{k+2,k}=z_{k+1,k} and z k + 2, k > a k z_{k+2,k}>a_{k}. By (i OPEN) k + 1)_{k+1}, z k + 2, k + 1 < a k + 1 z_{k+2,k+1}<a_{k+1}. Since z k + 2, k − 1 > a k − 1 z_{k+2,k-1}>a_{k-1}, we have z k + 2, k + 1 < 2 ​ a k + 1 z_{k+2,k+1}<2a_{k+1} by Lemma 2.3. Applying rule (A2) gives z k + 1, k = z k + 2, k − a k z_{k+1,k}=z_{k+2,k}-a_{k}. As before, this is a contradiction.

We now prove (ii OPEN) k)_{k}. Let z k + 1, k − 1 = a k − 1 z_{k+1,k-1}=a_{k-1} and z k + 1, k − 2 > 0 z_{k+1,k-2}>0. Suppose towards a contradiction that z k + 1, k ≥ a k z_{k+1,k}\geq a_{k}. Then z k + 2, k ≥ a k z_{k+2,k}\geq a_{k}, because the algorithm never increases the entry at position k k at step k + 1 k+1. Since z k + 1, k − 1 = a k − 1 z_{k+1,k-1}=a_{k-1}, either z k + 2, k − 1 = a k − 1 + 1 z_{k+2,k-1}=a_{k-1}+1 (in this case rule (A2) was applied) or z k + 2, k − 1 = a k − 1 z_{k+2,k-1}=a_{k-1} (in this case rule (A3) was applied). In both cases, z k + 2, k + 1 < a k + 1 z_{k+2,k+1}<a_{k+1} by (i OPEN) k + 1)_{k+1} and (ii OPEN) k + 1)_{k+1}. Since z k + 2, k − 1 > 0 z_{k+2,k-1}>0, z k + 2, k ≤ 2 ​ a k z_{k+2,k}\leq 2a_{k} by Lemma 2.3 (i). Hence rule (A2) was applied at step k + 1 k+1, and z k + 2, k − 1 = a k − 1 + 1 z_{k+2,k-1}=a_{k-1}+1. By Lemma 2.3 (ii), z k + 2, k < 2 ​ a k z_{k+2,k}<2a_{k}. Thus z k + 1, k = z k + 2, k − a k < a k z_{k+1,k}=z_{k+2,k}-a_{k}<a_{k}, a contradiction. ∎

###### Proof of Proposition 2.2.

Suppose k ≥ 3 k\geq 3. Because the entry at position k k is not changed after step k k, it is enough to show that z k, k ≤ a k z_{k,k}\leq a_{k}. We have to consider four different cases depending on the value of z k + 2, k z_{k+2,k}.

First, consider the case that z k + 2, k < a k z_{k+2,k}<a_{k}. Since the algorithm does not increase the entry in position k k at step k + 1 k+1, z k + 1, k < a k z_{k+1,k}<a_{k}. Thus z k, k ≤ z k + 1, k + 1 ≤ a k z_{k,k}\leq z_{k+1,k}+1\leq a_{k}.

Suppose z k + 2, k = a k z_{k+2,k}=a_{k} and z k + 2, k − 1 > 0 z_{k+2,k-1}>0. By Lemma 2.4 (ii), z k + 2, k + 1 < a k + 1 z_{k+2,k+1}<a_{k+1}. By rule (A2), z k + 1, k = 0 z_{k+1,k}=0. Hence z k, k ≤ 1 ≤ a k z_{k,k}\leq 1\leq a_{k}.

Suppose z k + 2, k = a k z_{k+2,k}=a_{k} and z k + 2, k − 1 = 0 z_{k+2,k-1}=0. Then no change is made at step k + 1 k+1. Thus z k + 1, k = a k z_{k+1,k}=a_{k} and z k + 1, k − 1 = 0 z_{k+1,k-1}=0. Since no change is made at step k k as well, z k, k = a k z_{k,k}=a_{k}.

Finally, consider z k + 2, k > a k z_{k+2,k}>a_{k}. By Lemma 2.4 (i), z k + 2, k + 1 < a k + 1 z_{k+2,k+1}<a_{k+1}. Hence either rule (A1) or rule (A2) is applied. We get that z k + 1, k ≤ a k z_{k+1,k}\leq a_{k}. If z k + 1, k = a k z_{k+1,k}=a_{k}, then z k, k = a k z_{k,k}=a_{k}. If z k + 1, k < a k z_{k+1,k}<a_{k}, then z k, k ≤ z k + 1, k + 1 ≤ a k z_{k,k}\leq z_{k+1,k}+1\leq a_{k}.

Now suppose that k < 3 k<3. We have to show that z 3, k ≤ a k z_{3,k}\leq a_{k}. We do so by considering several different cases depending on the values of z 4, 2 z_{4,2} and z 4, 1 z_{4,1}. By Lemma 2.4, if z 4, 2 > a 2 z_{4,2}>a_{2}, or, if z 4, 2 = a 2 z_{4,2}=a_{2} and z 4, 1 > 0 z_{4,1}>0, then z 4, 3 < a 3 z_{4,3}<a_{3}. If z 4, 2 = a 2 z_{4,2}=a_{2} and z 4, 1 = 0 z_{4,1}=0, then no changes was made.

Suppose that z 4, 2 = 2 ​ a 2 + 1 z_{4,2}=2a_{2}+1. By Lemma 2.3, z 4, 1 = 0 z_{4,1}=0. By rule (B1), z 3, 2 = a 2 z_{3,2}=a_{2}, z 3, 1 = a 1 − 1 z_{3,1}=a_{1}-1 and z 3, 3 = z 4, 3 + 1 ≤ a 3 z_{3,3}=z_{4,3}+1\leq a_{3}.

Now suppose that z 4, 2 = 2 ​ a 2 z_{4,2}=2a_{2}. We get z 4, 1 ≤ a 1 z_{4,1}\leq a_{1} from Lemma 2.3. Then either rule (B1) or rule (B2) was applied. In both cases we get that z 3, 2 = a 2 z_{3,2}=a_{2}, z 3, 1 = z 4, 1 − 1 ≤ a 1 − 1 z_{3,1}=z_{4,1}-1\leq a_{1}-1 and z 3, 3 = z 4, 3 + 1 ≤ a 3 z_{3,3}=z_{4,3}+1\leq a_{3}.

Consider that a 2 ≤ z 4, 2 < 2 ​ a 2 a_{2}\leq z_{4,2}<2a_{2} and z 4, 1 > 0 z_{4,1}>0. Here either rule (B2) or rule (B3) was used. Then z 3, 2 ≤ a 2 z_{3,2}\leq a_{2}, z 3, 1 ≤ a 1 − 1 z_{3,1}\leq a_{1}-1 and z 3, 3 = z 4, 3 + 1 ≤ a 3 z_{3,3}=z_{4,3}+1\leq a_{3}.

The last case we have to consider is z 4, 2 < a 2 z_{4,2}<a_{2}. Depending on whether z 4, 1 ≥ a 1 z_{4,1}\geq a_{1}, we applied either rule (B4) or rule (B5). Since z 4, 1 ≤ 2 ​ a 1 − 1 z_{4,1}\leq 2a_{1}-1, we get z 3, 1 ≤ a 1 − 1 z_{3,1}\leq a_{1}-1 and z 3, 2 ≤ z 3, 2 + 1 ≤ a 2 z_{3,2}\leq z_{3,2}+1\leq a_{2} in both cases. ∎

We will now describe the second step towards determining the Ostrowski representation of M + N M+N. This second algorithm will be a right-to-left pass over z 3 z_{3}. Given the word z 3, m ​ z 3, m − 1 ​ … ​ z 3, 2 ​ z 3, 1 z_{3,m}z_{3,m-1}\dots z_{3,2}z_{3,1}, we will recursively generate a word

 | w k = w k, m + 1 ​ w k, m ​ … ​ w k, 2 ​ w k, 1 w_{k}=w_{k,m+1}w_{k,m}\dots w_{k,2}w_{k,1} |  |

for each k ∈ N k\in N with k ∈ ℕ k\in\mathbb{N} with 2 ≤ k ≤ m + 1 2\leq k\leq m+1. At each step only elements in a moving window of length 3 3 are changed. Because the algorithm moves right to left, we will start by defining w 2 w_{2}, and then recursively define w k w_{k} for k ≥ 2 k\geq 2.

###### Algorithm 2.

Let k = 2 k=2. Then set

 | w 2:= 0 ​ z 3, m ​ z 3, m − 1 ​ … ​ z 3, 2 ​ z 3, 1. w_{2}:=0z_{3,m}z_{3,m-1}\dots z_{3,2}z_{3,1}. |  |

Let k ∈ ℕ k\in\mathbb{N} with 2 < k ≤ m + 1 2<k\leq m+1. We now define w k = w k, m + 1 ​ … ​ w k, 1 w_{k}=w_{k,m+1}\dots w_{k,1}:

- •

for i ∉ { k, k − 1, k − 2 } i\notin\{k,k-1,k-2\}, we set w k, i:= w k − 1, i w_{k,i}:=w_{k-1,i}.

- •

if w k − 1, k < a k w_{k-1,k}<a_{k}, w k − 1, k − 1 = a k − 1 w_{k-1,k-1}=a_{k-1} and w k − 1, k − 2 > 0 w_{k-1,k-2}>0, set

 | w k, k ​ w k, k − 1 ​ w k, k − 2:= ( w k − 1, k + 1) ​ 0 ​ ( w k − 1, k − 2 − 1), w_{k,k}w_{k,k-1}w_{k,k-2}:=(w_{k-1,k}+1)0(w_{k-1,k-2}-1), |  |

otherwise

 | w k, k ​ w k, k − 1 ​ w k, k − 2:= w k − 1, k ​ w k − 1, k − 1 ​ w k − 1, k − 2. w_{k,k}w_{k,k-1}w_{k,k-2}:=w_{k-1,k}w_{k-1,k-1}w_{k-1,k-2}. |  |

Again it follows immediately from Equation ( 1.1) that this algorithm leaves the value represented unchanged:

 | ∑ k = 0 m w m + 1, k + 1 ​ q k = ∑ k = 0 m z 3, k + 1 ​ q k. \sum_{k=0}^{m}w_{m+1,k+1}q_{k}=\sum_{k=0}^{m}z_{3,k+1}q_{k}. |  |

By Proposition 2.2 and the rules of Algorithm 2, w k, i ≤ a k w_{k,i}\leq a_{k} for every k = 2, …, m + 1 k=2,\dots,m+1 and i = 1, …, m + 2 i=1,\dots,m+2.

###### Lemma 2.5.

There is no k ∈ ℕ k\in\mathbb{N} such that

- •

w m + 1, k = a k w_{m+1,k}=a_{k}

- •

w m + 1, k − 1 < a k − 1 w_{m+1,k-1}<a_{k-1},

- •

w m + 1, k − 2 = a k − 2 w_{m+1,k-2}=a_{k-2}, and

- •

w m + 1, k − 3 > 0 w_{m+1,k-3}>0.

###### Proof.

Towards a contradiction, suppose that there is such an k k. We will first show that w k − 2, k − 3 > 0, w k − 2, k − 2 = a k − 2 w_{k-2,k-3}>0,w_{k-2,k-2}=a_{k-2} and w k − 2, k − 1 = a k − 1 w_{k-2,k-1}=a_{k-1}.

Suppose that w k − 2, k − 3 = 0 w_{k-2,k-3}=0. Then the algorithm would not have made any changes at step k − 2 k-2. Thus w k − 1, k − 3 = 0 w_{k-1,k-3}=0. Because the entry will not be changed later than step k − 1 k-1, w m + 1, k − 3 = 0 w_{m+1,k-3}=0. However, this contradicts w m + 1, k − 3 > 0 w_{m+1,k-3}>0. Thus w k − 2, k − 3 > 0 w_{k-2,k-3}>0.

Suppose that w k − 2, k − 2 < a k − 2 w_{k-2,k-2}<a_{k-2}. Then w k − 1, k − 2 = w k − 2, k − 2 w_{k-1,k-2}=w_{k-2,k-2}. This implies that w k, k − 2 < a k − 2 w_{k,k-2}<a_{k-2} and w m + 1, k − 2 < a k w_{m+1,k-2}<a_{k}. This a contradiction against our assumption w m + 1, k − 2 = a k − 2 w_{m+1,k-2}=a_{k-2}. Hence w k − 2, k − 2 = a k − 2 w_{k-2,k-2}=a_{k-2}.

Now suppose that w k − 2, k − 1 < a k − 1 w_{k-2,k-1}<a_{k-1}. Since w k − 2, k − 2 = a k − 2 w_{k-2,k-2}=a_{k-2} and w k − 2, k − 3 > 0 w_{k-2,k-3}>0, w k − 1, k − 2 = 0 w_{k-1,k-2}=0. Thus w m + 1, k − 2 = 0 w_{m+1,k-2}=0, contradicting w m + 1, k − 2 = a k − 2 w_{m+1,k-2}=a_{k-2}. So w k − 2, k − 1 = a k − 1 w_{k-2,k-1}=a_{k-1}.

It follows that w k − 1, k − 1 = w k − 2, k − 1 = a k − 1 w_{k-1,k-1}=w_{k-2,k-1}=a_{k-1} and w k − 1, k − 2 = w k − 1, k − 2 = a k − 2 w_{k-1,k-2}=w_{k-1,k-2}=a_{k-2}. We will now argue that w k − 1, k < a k w_{k-1,k}<a_{k}.

Suppose towards a contradiction that w k − 1, k = a k w_{k-1,k}=a_{k}. Then w k, k = a k w_{k,k}=a_{k} and w k, k − 1 = a k − 1 w_{k,k-1}=a_{k-1}. Since w m + 1, k − 1 < a k − 1 w_{m+1,k-1}<a_{k-1}, we have w k, k + 1 < a k + 1 w_{k,k+1}<a_{k+1}. Thus w k + 1, k = 0 w_{k+1,k}=0. Hence w m + 1, k = 0 w_{m+1,k}=0, a contradiction. So w k − 1, k < a k w_{k-1,k}<a_{k}.

We conclude that the entry at position k − 2 k-2 is changed at step k k. Therefore, w k, k − 2 = w k − 1, k − 2 − 1 = a k − 2 − 1 w_{k,k-2}=w_{k-1,k-2}-1=a_{k-2}-1. So w m + 1, k − 2 = a k − 2 − 1 w_{m+1,k-2}=a_{k-2}-1. This contradicts our original assumption w m + 1, k − 2 = a k − 2 w_{m+1,k-2}=a_{k-2}. ∎

The third and final step of our algorithm is a left-to-right pass over w m + 1 w_{m+1}. The moving window is again of length 3 3 and we use the same rule as in step 2. Given the word w m + 1, m + 1 ​ … ​ w m + 1, 1 w_{m+1,m+1}\dots w_{m+1,1}, we will recursively generate a word

 | v k:= v k, m + 2 ​ … ​ v k, 1 v_{k}:=v_{k,m+2}\dots v_{k,1} |  |

for each k ∈ N k\in N with k ∈ ℕ k\in\mathbb{N} with 3 ≤ k ≤ m + 3 3\leq k\leq m+3. Because the algorithm moves left to right, we will start by defining w m + 3 w_{m+3} and then recursively define w k w_{k} for k ≤ m + 3 k\leq m+3.

###### Algorithm 3.

Let k = m + 3 k=m+3. Then set

 | v m + 3:= 0 ​ w m + 1, m + 1 ​ … ​ w m + 1, 1. v_{m+3}:=0w_{m+1,m+1}\dots w_{m+1,1}. |  |

Let k ∈ ℕ k\in\mathbb{N} with 3 ≤ k ≤ m + 2 3\leq k\leq m+2. We now define v k = v k, m + 2 ​ … ​ v k, 1 v_{k}=v_{k,m+2}\dots v_{k,1}:

- •

for i ∉ { k, k − 1, k − 2 } i\notin\{k,k-1,k-2\}, we set v k, i:= v k + 1, i v_{k,i}:=v_{k+1,i},

- •

if v k + 1, k < a k v_{k+1,k}<a_{k}, v k + 1, k − 1 = a k − 1 v_{k+1,k-1}=a_{k-1} and v k + 1, k − 2 > 0 v_{k+1,k-2}>0, set

 | v k, k ​ v k, k − 1 ​ v k, k − 2:= ( v k + 1, k + 1) ​ 0 ​ ( v k + 1, k − 2 − 1), v_{k,k}v_{k,k-1}v_{k,k-2}:=(v_{k+1,k}+1)0(v_{k+1,k-2}-1), |  |

otherwise

 | v k, k ​ v k, k − 1 ​ v k, k − 2:= v k + 1, k ​ v k + 1, k − 1 ​ v k + 1, k − 2. v_{k,k}v_{k,k-1}v_{k,k-2}:=v_{k+1,k}v_{k+1,k-1}v_{k+1,k-2}. |  |

As before Equation ( 1.1) implies that this algorithm leaves the value represented unchanged:

 | ∑ k = 0 m w m + 1, k + 1 ​ q k = ∑ k = 0 m v 3, k + 1 ​ q k. \sum_{k=0}^{m}w_{m+1,k+1}q_{k}=\sum_{k=0}^{m}v_{3,k+1}q_{k}. |  |

Moveover, we have v k, i ≤ a k v_{k,i}\leq a_{k} for every k = 3, …, m + 3 k=3,...,m+3 and i = 1, …, m + 2 i=1,\dots,m+2. We will now show v 3 v_{3} is indeed the Ostrowski representation of M + N M+N. It is enough to prove the following Proposition.

###### Proposition 2.6.

Let l ≥ 3 l\geq 3. Then there is no k ≥ l − 1 k\geq l-1 such that v l, k = a k v_{l,k}=a_{k} and v l, k − 1 > 0 v_{l,k-1}>0.

Before we give the proof of Proposition 2.6, we need one more Lemma.

###### Lemma 2.7.

Let l ∈ { 3, …, m + 3 } l\in\{3,\dots,m+3\}. Then there is no k ∈ ℕ k\in\mathbb{N} such that

- •

v l, k = a k v_{l,k}=a_{k}

- •

v l, k − 1 < a k − 1 v_{l,k-1}<a_{k-1},

- •

v l, k − 2 = a k − 2 v_{l,k-2}=a_{k-2}, and

- •

v l, k − 3 > 0 v_{l,k-3}>0.

###### Proof.

We prove the Lemma by induction on l l. By Lemma 2.5, there is no such k k for m + 3 m+3. Suppose that the statement holds for l + 1 l+1. We want to show the statement for l l. Towards a contradiction, suppose that there is a k k such that

(2.1) |  | v l, k = a k, v l, k − 1 < a k − 1, v l, k − 2 = a k − 2 ​ and ​ v l, k − 3 > 0. v_{l,k}=a_{k},v_{l,k-1}<a_{k-1},v_{l,k-2}=a_{k-2}\hbox{ and }v_{l,k-3}>0. |  |

By the induction hypothesis, it is enough to check that no change was made at step l l; that is v l, i = v l + 1, i v_{l,i}=v_{l+1,i} for i ∈ { k, …, k − 3 } i\in\{k,...,k-3\}. Since the algorithm only modifies the entries at position l, l + 1 l,l+1 or l + 2 l+2, we can assume that k ∈ { l − 2, …, l + 3 } k\in\{l-2,\dots,l+3\}. We consider each case separately.

First, suppose k = l − 2 k=l-2. We get that v l, i = v l + 1, i v_{l,i}=v_{l+1,i} for i ∈ { k − 1, k − 2, k − 3 } i\in\{k-1,k-2,k-3\}, because they are not in the moving window at step l l. The only possible change is at position k k. Since v l, l − 2 < v l + 1, l − 2 v_{l,l-2}<v_{l+1,l-2} by induction hypothesis, and v l, l − 2 = a l − 2 v_{l,l-2}=a_{l-2}, we get v l, k = v l + 1, k v_{l,k}=v_{l+1,k}. So no change is made.

Suppose that k = l − 1 k=l-1. If a change is made at step l l, then v l, k = 0 v_{l,k}=0. But this contradicts ( 2.1). Hence no change is made in this case.

Suppose that k = l k=l. If a change is made at step l l, then v l, k − 2 = v l + 1, k − 2 − 1 < a k − 2 v_{l,k-2}=v_{l+1,k-2}-1<a_{k-2}. As before, this contradicts ( 2.1). Thus no change is made.

Suppose k = l + 1 k=l+1. If a change is made at step l l, then v l, k − 2 = 0 v_{l,k-2}=0 contradicting ( 2.1). So no change is made in this case either.

Suppose k = l + 2 k=l+2. If a change is made at step l l, then v l, k − 3 = 0 v_{l,k-3}=0. This again contradicts ( 2.1), and hence no change is made.

Finally suppose k = l + 3 k=l+3. By induction hypothesis, v l + 1, k − 3 = 0 v_{l+1,k-3}=0. Since v l, k − 3 > 0 v_{l,k-3}>0, we have v l + 1, k − 4 = a k − 4 v_{l+1,k-4}=a_{k-4} and v l + 1, k − 5 > 0 v_{l+1,k-5}>0. Then

 | v l + 1, k − 2 = a k − 2, v l + 1, k − 3 = 0, v l + 1, k − 4 = a k − 4 ​ and ​ v l + 1, k − 5 > 0. v_{l+1,k-2}=a_{k-2},v_{l+1,k-3}=0,v_{l+1,k-4}=a_{k-4}\hbox{ and }v_{l+1,k-5}>0. |  |

This contradicts the induction hypothesis. ∎

###### Proof of Propositon 2.6.

We prove this statement by induction on l l. For l = m + 3 l=m+3 the statement holds trivially, because v m + 3, m + 2 = 0 v_{m+3,m+2}=0. Now suppose that the statement holds for l + 1 l+1, but fails for l l. Hence there is k ≥ l − 1 k\geq l-1 such that v l, k = a k v_{l,k}=a_{k} and v l, k − 1 > 0 v_{l,k-1}>0. Since v l + 1, i = v l, i v_{l+1,i}=v_{l,i} for i > l i>l, we have k ≤ l + 1 k\leq l+1. We now consider the three remaining cases k = l + 1 k=l+1, k = l k=l and k = l − 1 k=l-1 individually.

If k = l + 1 k=l+1, then v l + 1, k = a l + 1, k v_{l+1,k}=a_{l+1,k}. By the induction hypothesis, v l + 1, k − 1 = 0 v_{l+1,k-1}=0. But in order for v l, k − 1 > 0 v_{l,k-1}>0 to hold, we must have v l + 1, k − 2 = a k − 2 v_{l+1,k-2}=a_{k-2} and v l + 1, k − 3 > 0 v_{l+1,k-3}>0. This contradicts Lemma 2.7.

If k = l k=l, then either v l + 1, k = a k v_{l+1,k}=a_{k} or v l + 1, k = a k − 1 v_{l+1,k}=a_{k}-1. Suppose that v l + 1, k = a k − 1 v_{l+1,k}=a_{k}-1. Then v l + 1, k − 1 = a k v_{l+1,k-1}=a_{k} and v l + 1, k − 2 > 0 v_{l+1,k-2}>0. This implies v l, k − 1 = 0 v_{l,k-1}=0, which contradicts v l, k − 1 > 0 v_{l,k-1}>0. Suppose that v l + 1, k = a k v_{l+1,k}=a_{k}. By induction hypothesis, v l + 1, k − 1 = 0 v_{l+1,k-1}=0. But then no change is made at step l l, and hence v l, k − 1 = 0 v_{l,k-1}=0. A contradiction against v l, k − 1 > 0 v_{l,k-1}>0.

If k = l − 1 k=l-1, then no change is made at step l l, since v l, l − 1 = a l − 1 v_{l,l-1}=a_{l-1}. Hence v l + 1, l − 1 = v l, l − 1 = a l − 1 v_{l+1,l-1}=v_{l,l-1}=a_{l-1} and v l + 1, l − 2 = v l, l − 2 > 0 v_{l+1,l-2}=v_{l,l-2}>0. Since no change was made at step l l, we get that v l + 1, l = a l v_{l+1,l}=a_{l}. This contradicts the induction hypothesis. ∎

###### Corollary 2.8.

The word v 3, m + 2 ​ … ​ v 3, 1 v_{3,m+2}\dots v_{3,1} is the Ostrowski representation of M + N M+N.

## 3. Proof of Theorem A

In this section we will prove Theorem A. Let a a be a quadratic irrational number. Let [a 0; a 1, …, a n, …] [a_{0};a_{1},\dots,a_{n},\dots] be its continued fraction expansion. Since the continued fraction expansion of a a is periodic, it is of the form

 | [a 0; a 1, …, a ξ − 1, a ξ, …, a ν ¯], [a_{0};a_{1},\dots,a_{\xi-1},\overline{a_{\xi},\dots,a_{\nu}}], |  |

where ν − ξ \nu-\xi is the length of the repeating block and the repeating block starts at ξ \xi. We can choose ξ \xi and ν \nu such that ξ > 4 \xi>4 and ν − ξ ≥ 3 \nu-\xi\geq 3. 4 4 4 It might be the case that neither ξ \xi nor ν \nu are minimal, but this will be irrelevant here. Set μ:= max i ⁡ a i \mu:=\max_{i}a_{i}. Set m:= 2 ​ μ + 1 m:=2\mu+1. Set Σ a:= { 0, …, m }. \Sigma_{a}:=\{0,\dots,m\}.

We first remind the reader of the definitions of finite automata and recognizability. For more details, we refer the reader to [11]. Let Σ \Sigma be a finite set. We denote by Σ ∗ \Sigma^{*} the set of words of finite length on Σ \Sigma.

###### Definition 3.1.

A nondeterministic finite automaton 𝒜 \mathcal{A} over Σ \Sigma is a quadruple ( S, I, T, F) (S,I,T,F), where S S is a finite non-empty set, called the set of states of 𝒜 \mathcal{A}, I I is a subset of S S, called the set of initial states, T ⊆ S × Σ × S T\subseteq S\times\Sigma\times S is a non-empty set, called the transition table of 𝒜 \mathcal{A} and F F is a subset of S S, called the set of final states of 𝒜 \mathcal{A}. An automaton 𝒜 = ( S, I, T, F) \mathcal{A}=(S,I,T,F) is deterministic if I I contains exactly one element, and for every s ∈ S s\in S and w ∈ Σ ∗ w\in\Sigma^{*} there is exactly one s ′ ∈ S s^{\prime}\in S such that ( s, w, s ′) ∈ T (s,w,s^{\prime})\in T. We say that an automaton 𝒜 \mathcal{A} on Σ \Sigma accepts a word w = w n ​ … ​ w 1 ∈ Σ ∗ w=w_{n}\dots w_{1}\in\Sigma^{*} if there is a sequence s n, …, s 1, s 0 ∈ S s_{n},\dots,s_{1},s_{0}\in S such that s n ∈ I s_{n}\in I, s 0 ∈ F s_{0}\in F and for i = 1, …, n i=1,\dots,n, ( s i, w i, s i − 1) ∈ T (s_{i},w_{i},s_{i-1})\in T. A subset L ⊆ Σ ∗ L\subseteq\Sigma^{*} is recognized by 𝒜 \mathcal{A} if L L is the set of Σ \Sigma -words that are accepted by 𝒜 \mathcal{A}. We say that L ⊆ Σ ∗ L\subseteq\Sigma^{*} is recognizable if L L is recognized by some deterministic finite automaton.

It is well known (see [11, Theorem 2.3.3]) that a set is recognizable if it is recognized by some *nondeterministic*finite automaton.

Let Σ \Sigma be a set containing 0 0. Let z = ( z 1, …, z n) ∈ ( Σ ∗) n z=(z_{1},\dots,z_{n})\in(\Sigma^{*})^{n} and let m m be the maximal length of z 1, …, z n z_{1},\dots,z_{n}. We add to each z i z_{i} the necessary number of 0 0 ’s to get a word z i ′ z_{i}^{\prime} of length m m. The convolution 5 5 5 Here we followed the presentation in [16]. For a general definition of convolution see [11]. of z z is defined as the word z 1 ∗ ⋯ ∗ z n ∈ ( Σ n) ∗ z_{1}*\dots*z_{n}\in(\Sigma^{n})^{*} whose i i -th letter is the element of Σ n \Sigma^{n} consisting of the i i -th letters of z 1 ′, …, z n ′ z_{1}^{\prime},\dots,z_{n}^{\prime}.

###### Definition 3.2.

A subset X ⊂ ( Σ ∗) n X\subset(\Sigma^{*})^{n} is Σ \Sigma -recognizable if the set

 | { z 1 ∗ ⋯ ∗ z n: ( z 1, …, z n) ∈ X } \{z_{1}*\dots*z_{n}\ :\ (z_{1},\dots,z_{n})\in X\} |  |

is Σ n \Sigma^{n} -recognizable.

We remind the reader that every natural number N N can be written as N = ∑ k = 0 n b k + 1 ​ q k N=\sum_{k=0}^{n}b_{k+1}q_{k}, where b k ∈ ℕ b_{k}\in\mathbb{N} such that b 1 < a 1 b_{1}<a_{1}, b k ≤ a k b_{k}\leq a_{k} and, if b k = a k b_{k}=a_{k}, b k − 1 = 0 b_{k-1}=0, and that we denoted the Σ a \Sigma_{a} -word b n ​ … ​ b 1 b_{n}\dots b_{1} by ρ a ​ ( N) \rho_{a}(N).

###### Definition 3.3.

Let X ⊆ ℕ n X\subseteq\mathbb{N}^{n}. We say that X X is a a -recognizable if the set

 | { ( 0 l 1 ρ a ( N 1), …, 0 l n ρ a ( N n)): ( N 1, …, N n) ∈ X, l 1, …, l n ∈ ℕ } \{(0^{l_{1}}\rho_{a}(N_{1}),\dots,0^{l_{n}}\rho_{a}(N_{n}))\ :\ (N_{1},\dots,N_{n})\in X,l_{1},\dots,l_{n}\in\mathbb{N}\} |  |

is Σ a \Sigma_{a} -recognizable.

In this section we will prove that a subset X ⊆ ℕ n X\subseteq\mathbb{N}^{n} is a a -recognizable if and only if X X is definable in ( ℕ, +, V a) (\mathbb{N},+,V_{a}).

### Recognizability implies definability

We will first show that whenever a set X ⊆ ℕ n X\subseteq\mathbb{N}^{n} is a a -recognizable, then X X is definable in ( ℕ, +, V a) (\mathbb{N},+,V_{a}). The proof here is an adjusted version of the proofs in Villemaire [16] and [4].

First note that < < is definable in ( ℕ, +, V a) (\mathbb{N},+,V_{a}) and so is V a ​ ( ℕ) = { q k: k ∈ ℕ } V_{a}(\mathbb{N})=\{q_{k}\ :\ k\in\mathbb{N}\}. For convenience, we write I I for V a ​ ( ℕ) V_{a}(\mathbb{N}). We denote the successor function on I I by s I s_{I}.

###### Definition 3.4.

For j ∈ { 1, …, m } j\in\{1,\dots,m\}, let ϵ j ⊆ I × ℕ \epsilon_{j}\subseteq I\times\mathbb{N} be the set of ( x, y) ∈ I × ℕ (x,y)\in I\times\mathbb{N} with

 | ∃ z \displaystyle\exists z | ∈ ℕ ​ ∃ t ∈ ℕ ⁡ ( z < x ∧ z + j ​ x < s I ​ ( x) ∧ V a ​ ( t) > x ∧ V a ​ ( x + t) = x ∧ y = z + j ​ x + t) \displaystyle\in\mathbb{N}\exists t\in\mathbb{N}(z<x\wedge z+jx<s_{I}(x)\wedge V_{a}(t)>x\wedge V_{a}(x+t)=x\wedge y=z+jx+t) |  |

 |  | ∨ ∃ z ∈ ℕ ( z < x ∧ y < s I ( x) ∧ y = z + j x). \displaystyle\vee\exists z\in\mathbb{N}(z<x\wedge y<s_{I}(x)\wedge y=z+jx). |  |

Let ϵ 0 ⊆ I × ℕ \epsilon_{0}\subseteq I\times\mathbb{N} be the set of ( x, y) ∈ I × ℕ (x,y)\in I\times\mathbb{N} with ⋀ j = 1 m ¬ ϵ j ​ ( x, y) \bigwedge_{j=1}^{m}\neg\epsilon_{j}(x,y).

This definition is inspired by [16, Lemma 2.3]. Obviously, ϵ j \epsilon_{j} is definable in ( ℕ, +, V a) (\mathbb{N},+,V_{a}). Because of the greediness of the Ostrowski representation, ϵ j ​ ( x, y) \epsilon_{j}(x,y) holds iff x = q k x=q_{k} for some k ∈ ℕ k\in\mathbb{N} and the coefficient of q k q_{k} in the Ostrowski representation of y y is j j. We directly get the following Lemma.

###### Lemma 3.5.

Let l, n ∈ ℕ l,n\in\mathbb{N} and let ∑ k b k + 1 ​ q k \sum_{k}b_{k+1}q_{k} be the Ostrowski representation of n n. Then b l + 1 = j b_{l+1}=j iff ϵ j ​ ( q l, n) \epsilon_{j}(q_{l},n).

###### Definition 3.6.

Let I e I_{e} be the set of all y ∈ I y\in I with

 | ∃ z ∈ ℕ ​ ϵ 1 ​ ( 1, z) ∧ ϵ 1 ​ ( y, z) ∧ ∀ x ∈ I ⁡ ( ϵ 1 ​ ( x, z) ↔ ¬ ϵ 1 ​ ( s I ​ ( x), z)), \exists z\in\mathbb{N}\ \epsilon_{1}(1,z)\wedge\epsilon_{1}(y,z)\wedge\forall x\in I\big(\epsilon_{1}(x,z)\leftrightarrow\neg\epsilon_{1}(s_{I}(x),z)\big), |  |

and let I o I_{o} be the set of all y ∈ I y\in I with

 | ∃ z ∈ ℕ ⁡ ( ¬ ϵ 1 ​ ( 1, z)) ∧ ϵ 1 ​ ( y, z) ∧ ∀ x ∈ I ⁡ ( ϵ 1 ​ ( x, z) ↔ ¬ ϵ 1 ​ ( s I ​ ( x), z)). \exists z\in\mathbb{N}\ (\neg\epsilon_{1}(1,z))\wedge\epsilon_{1}(y,z)\wedge\forall x\in I\big(\epsilon_{1}(x,z)\leftrightarrow\neg\epsilon_{1}(s_{I}(x),z)\big). |  |

Obviously both I e I_{e} and I o I_{o} are definable in ( ℕ, +, V a) (\mathbb{N},+,V_{a}), I = I e ∪ I o I=I_{e}\cup I_{o}, and since q 0 = 1 q_{0}=1,

 | I e = { q k: k ​ even } ​ and ​ I o = { q k: k ​ odd }. I_{e}=\{q_{k}\ :\ k\hbox{ even }\}\hbox{ and }I_{o}=\{q_{k}\ :\ k\hbox{ odd }\}. |  |

###### Definition 3.7.

Let U e ⊆ ℕ U_{e}\subseteq\mathbb{N} be the set of all y ∈ ℕ y\in\mathbb{N} with

 | ∀ z ∈ I o ​ ϵ 0 ​ ( z, y) ∧ ∀ z ∈ I e ​ ( ϵ 0 ​ ( z, y) ∨ ϵ 1 ​ ( z, y)), \forall z\in I_{o}\ \epsilon_{0}(z,y)\wedge\forall z\in I_{e}\ (\epsilon_{0}(z,y)\vee\epsilon_{1}(z,y)), |  |

and U o ⊆ ℕ U_{o}\subseteq\mathbb{N} be the set of all y ∈ ℕ y\in\mathbb{N} with

 | ∀ z ∈ I e ​ ϵ 0 ​ ( z, y) ∧ ∀ z ∈ I o ​ ( ϵ 0 ​ ( z, y) ∨ ϵ 1 ​ ( z, y)). \forall z\in I_{e}\ \epsilon_{0}(z,y)\wedge\forall z\in I_{o}\ (\epsilon_{0}(z,y)\vee\epsilon_{1}(z,y)). |  |

Again it is easy to see that U e U_{e} and U o U_{o} are definable in ( ℕ, +, V a) (\mathbb{N},+,V_{a}). We get the following Lemma from Lemma 3.5.

###### Lemma 3.8.

Let n ∈ ℕ n\in\mathbb{N} and let ∑ k b k + 1 ​ q k \sum_{k}b_{k+1}q_{k} be the Ostrowski representation of n n. Then

- (i)

n ∈ U e n\in U_{e} if and only if for all even k k b k + 1 ≤ 1 b_{k+1}\leq 1, and for all odd k k b k + 1 = 0 b_{k+1}=0,

- (ii)

n ∈ U o n\in U_{o} if and only if for all odd k k b k + 1 ≤ 1 b_{k+1}\leq 1, and for all even k k b k + 1 = 0 b_{k+1}=0.

###### Definition 3.9.

Let ϵ ⊆ I × ( U e × U o) \epsilon\subseteq I\times(U_{e}\times U_{o}) be the set of all ( x, ( y 1, y 2)) (x,(y_{1},y_{2})) with

 | ( x ∈ I e → ϵ 1 ​ ( x, y 1)) ∧ ( x ∈ I o → ϵ 1 ​ ( x, y 2)). (x\in I_{e}\rightarrow\epsilon_{1}(x,y_{1}))\wedge(x\in I_{o}\rightarrow\epsilon_{1}(x,y_{2})). |  |

###### Theorem 3.10.

Let X ⊆ ℕ n X\subseteq\mathbb{N}^{n} be a a -recognizable. Then X X is definable in ( ℕ, +, V a) (\mathbb{N},+,V_{a}).

###### Proof.

Let X ⊆ ℕ n X\subseteq\mathbb{N}^{n} be a a -recognizable by a finite automaton 𝒜 = ( S, I, T, F) \mathcal{A}=(S,I,T,F). Without loss generality we can assume that the set of states S S is { 1, …, t } \{1,\dots,t\} for some t ∈ ℕ t\in\mathbb{N}, and I = { 1 } I=\{1\}. Let φ \varphi be the formula defining the following subset Z Z of U t U^{t}:

 | { ( u 1, …, u t) ∈ U t: ∀ q ∈ I ​ ⋀ i = 1 t ( ϵ ⁡ ( q, u i) → ⋀ j = 1, j ≠ i t ¬ ϵ ⁡ ( q, u j)) }. \{(u_{1},\dots,u_{t})\in U^{t}\ :\forall q\in I\ \bigwedge_{i=1}^{t}\big(\epsilon(q,u_{i})\rightarrow\bigwedge_{j=1,j\neq i}^{t}\neg\epsilon(q,u_{j})\big)\}. |  |

So Z Z is the set of tuples ( u 1, …, u t) ∈ U t (u_{1},\dots,u_{t})\in U^{t} such that for q ∈ I q\in I there is at most one i ∈ { 1, …, t } i\in\{1,\dots,t\} such that ϵ ⁡ ( q, u i) \epsilon(q,u_{i}). Note that x ∈ X x\in X if there is a run s 1 ​ … ​ s m s_{1}\dots s_{m} of 𝒜 \mathcal{A} on the word given by the Ostrowski representation of the coordinates of x x such that s 1 = 1 s_{1}=1 and s m ∈ F s_{m}\in F. The idea now is to code such a run as an element of Z Z. To be precise, a tuple ( u 1, …, u t) ∈ Z (u_{1},\dots,u_{t})\in Z will code a run s 1 ​ … ​ s m s_{1}\dots s_{m} if for each q i ∈ I q_{i}\in I, s i s_{i} is the unique element k k of { 1, …, t } \{1,\dots,t\} such that ϵ ⁡ ( q i, u k) \epsilon(q_{i},u_{k}). Thus x = ( x 1, …, x n) ∈ X x=(x_{1},\dots,x_{n})\in X if and only if x x satisfies the following formula in ( ℕ, +, V a) (\mathbb{N},+,V_{a}):

 | ∃ u 1, …, u t ∈ U ​ ∃ q ∈ I ​ φ ​ ( u 1, …, u t) ∧ ϵ ⁡ ( 1, u 1) ∧ ⋁ l ∈ F ϵ ⁡ ( q, u l) \displaystyle\exists u_{1},\dots,u_{t}\in U\ \exists q\in I\ \varphi(u_{1},\dots,u_{t})\wedge\epsilon(1,u_{1})\wedge\bigvee_{l\in F}\epsilon(q,u_{l}) |  |

 | ∧ ⋀ ( l, ( ρ 1, …, ρ n), k) ∈ T ∀ z ∈ I ( ( z > q) → ⋀ i = 1 n ⋀ j = 1 m ¬ ϵ j ( z, x i)) \displaystyle\wedge\bigwedge_{(l,(\rho_{1},\dots,\rho_{n}),k)\in T}\forall z\in I\Big((z>q)\rightarrow\bigwedge_{i=1}^{n}\bigwedge_{j=1}^{m}\neg\epsilon_{j}(z,x_{i})\Big) |  |

 | ∧ [( z ≤ q ∧ ϵ ( z, u l) ∧ ⋀ i = 1 n ϵ ρ i ( z, x i)) → ϵ ( s I ( z), u k)]. \displaystyle\wedge\Big[\big(z\leq q\wedge\epsilon(z,u_{l})\wedge\bigwedge_{i=1}^{n}\epsilon_{\rho_{i}}(z,x_{i})\big)\rightarrow\epsilon(s_{I}(z),u_{k})\Big]. |  |

∎

### Definability implies recognizability

We will prove that if a subset X ⊆ ℕ n X\subseteq\mathbb{N}^{n} is definable in ( ℕ, +, V a) (\mathbb{N},+,V_{a}), then it is a a -recognizable. By [10] it is suffices to show that the set ℕ \mathbb{N} and the relations { ( x, y) ∈ ℕ 2: x = y } \{(x,y)\in\mathbb{N}^{2}\ :\ x=y\}, { ( x, y, z) ∈ ℕ 3: x + y = z } \{(x,y,z)\in\mathbb{N}^{3}\ :\ x+y=z\} and { ( x, y) ∈ ℕ 2: V a ​ ( x) = y } \{(x,y)\in\mathbb{N}^{2}\ :\ V_{a}(x)=y\} are all a a -recognizable. It is well known that ℕ \mathbb{N} is a a -recognizable (see for example [15, Theorem 8]), and using that knowledge it is easy to check that { ( x, y) ∈ ℕ 2: x = y } \{(x,y)\in\mathbb{N}^{2}\ :\ x=y\} and { ( x, y) ∈ ℕ 2: V a ​ ( x) = y } \{(x,y)\in\mathbb{N}^{2}\ :\ V_{a}(x)=y\} are a a -recognizable. We are now going to show that { ( x, y, z) ∈ ℕ 3: x + y = z } \{(x,y,z)\in\mathbb{N}^{3}\ :\ x+y=z\} is a a -recognizable.

By the work in the previous section, we have an algorithm to compute addition in Ostrowski representation based on a a. This algorithm consists of four steps, and we will now show that each of the four steps can be recognized by a finite automaton. Given two words z = z n ​ … ​ z 1, z ′ = z n ′ ​ … ​ z 1 ′ ∈ ρ a ​ ( ℕ) z=z_{n}\dots z_{1},z^{\prime}=z_{n}^{\prime}\dots z_{1}^{\prime}\in\rho_{a}(\mathbb{N}), the first step is to compute the Σ a \Sigma_{a} -word ( z n + z n ′) ​ … ​ ( z 1 + z 1 ′) (z_{n}+z_{n}^{\prime})\dots(z_{1}+z_{1}^{\prime}), which we will denote by z + z ′ z+z^{\prime}. It is straightforward to verify that the set { z ∗ z ′ ∗ ( z + z ′): z, z ′ ∈ ρ a ( ℕ) } \{z*z^{\prime}*(z+z^{\prime})\ :\ z,z^{\prime}\in\rho_{a}(\mathbb{N})\} is recognizable by a finite automaton. For z, z ′ ∈ Σ a ∗ z,z^{\prime}\in\Sigma_{a}^{*}, we will write z ↝ i z ′ z\rightsquigarrow_{i}z^{\prime} if Algorithm i i produces z ′ z^{\prime} on input z z. In the following, we will prove that the set { z ∗ z ′: z, z ′ ∈ Σ a ∗, z ↝ i z ′ } \{z*z^{\prime}\ :\ z,z^{\prime}\in\Sigma_{a}^{*},z\rightsquigarrow_{i}z^{\prime}\} is recognizable by a finite automaton for i = 1, 2, 3 i=1,2,3. From these results it is immediate that

 | { z ∗ z ′ ∗ z ′′ ∗ u 0 ∗ u 1 ∗ u 2 \displaystyle\{z*z^{\prime}*z^{\prime\prime}*u_{0}*u_{1}*u_{2}\  | : z, z ′, z ′′ ∈ ρ a ​ ( ℕ), u 0, u 1, u 2 ∈ Σ a ∗, \displaystyle:\ z,z^{\prime},z^{\prime\prime}\in\rho_{a}(\mathbb{N}),u_{0},u_{1},u_{2}\in\Sigma_{a}^{*}, |  |

 |  | u 0 = z + z ′, u 0 ↝ 1 u 1 ↝ 2 u 2 ↝ 3 z ′′ } \displaystyle\ u_{0}=z+z^{\prime},u_{0}\rightsquigarrow_{1}u_{1}\rightsquigarrow_{2}u_{2}\rightsquigarrow_{3}z^{\prime\prime}\} |  |

is recognizable by a finite automaton. Since recognizability is preserved under projections (see [11, Theorem 2.3.9]), { ( x, y, z) ∈ ℕ 3: x + y = z } \{(x,y,z)\in\mathbb{N}^{3}\ :\ x+y=z\} is a a -recognizable by Corollary 2.8. Thus every set X ⊆ ℕ n X\subseteq\mathbb{N}^{n} definable in ( ℕ, +, V a) (\mathbb{N},+,V_{a}) is a a -recognizable.

### An automaton for Algorithm 1

We will now construct a non-deterministic automaton 𝒜 1 \mathcal{A}_{1} that recognizes the set { z ∗ z ′: z, z ′ ∈ Σ a ∗, z ↝ 1 z ′ } \{z*z^{\prime}\ :\ z,z^{\prime}\in\Sigma_{a}^{*},z\rightsquigarrow_{1}z^{\prime}\}. Before giving the definition of 𝒜 1 \mathcal{A}_{1}, we need to introduce some notation. Let A ⊆ ℕ ≤ m 4 × ℕ ≤ m 4 × ℕ ≤ m 4 A\subseteq\mathbb{N}_{\leq m}^{4}\times\mathbb{N}_{\leq m}^{4}\times\mathbb{N}_{\leq m}^{4} be the set of tuples ( u, v, w) (u,v,w) with

 | w = { ( v 1 + 1, v 2 − ( u 2 + 1), u 3 − 1, v 4 + 1), if v 1 ​ < u 1, v 2 > ​ u 2 and v 3 = 0, ( v 1 + 1, v 2 − u 2, v 3 − 1, v 4, if v 1 < u 1, u 2 ≤ v 2 ≤ 2 ​ u 2 and v 3 > 0, ( v 1, v 2, v 3, v 4), otherwise. w=\left\{\begin{array}[]{ll}(v_{1}+1,v_{2}-(u_{2}+1),u_{3}-1,v_{4}+1),&\hbox{ if $v_{1}<u_{1},v_{2}>u_{2}$ and $v_{3}=0$,}\\ (v_{1}+1,v_{2}-u_{2},v_{3}-1,v_{4},&\hbox{ if $v_{1}<u_{1},u_{2}\leq v_{2}\leq 2u_{2}$ and $v_{3}>0$,}\\ (v_{1},v_{2},v_{3},v_{4}),&\hbox{otherwise.}\end{array}\right. |  |

Let B ⊆ ℕ ≤ m 3 × ℕ ≤ m 3 × ℕ ≤ m 3 B\subseteq\mathbb{N}_{\leq m}^{3}\times\mathbb{N}_{\leq m}^{3}\times\mathbb{N}_{\leq m}^{3} be the set of tuples ( u, v, w) (u,v,w) with

 | w = { ( v 1 + 1, v 2 − ( u 2 + 1), u 3 − 1), v 1 < u 1, v 2 > u 2 and v 3 = 0; ( v 1 + 1, v 2 − u 2, v 3 − 1), v 1 < u 1, v 2 ≥ u 2 and u 1 ≥ v 1 > 0,; ( v 1 + 1, v 2 − u 2 + 1, v 1 − u 1 − 1), v 1 < u 1, v 2 ≥ u 2 and v 1 > u 1; ( v 1, v 2 + 1, v 1 − u 1), if v 2 < u 2 and v 1 ≥ u 1; ( v 1, v 2, v 3), otherwise. w=\left\{\begin{array}[]{ll}(v_{1}+1,v_{2}-(u_{2}+1),u_{3}-1),&\hbox{$v_{1}<u_{1}$, $v_{2}>u_{2}$ and $v_{3}=0$;}\\ (v_{1}+1,v_{2}-u_{2},v_{3}-1),&\hbox{$v_{1}<u_{1}$, $v_{2}\geq u_{2}$ and $u_{1}\geq v_{1}>0$,;}\\ (v_{1}+1,v_{2}-u_{2}+1,v_{1}-u_{1}-1),&\hbox{$v_{1}<u_{1}$, $v_{2}\geq u_{2}$ and $v_{1}>u_{1}$;}\\ (v_{1},v_{2}+1,v_{1}-u_{1}),&\hbox{if $v_{2}<u_{2}$ and $v_{1}\geq u_{1}$;}\\ (v_{1},v_{2},v_{3}),&\hbox{otherwise.}\end{array}\right. |  |

Note that A A corresponds to the rules (A1),(A2) and (A3) of Algorithm 1, while B B corresponds to the rules (B1)-(B5) of Algorithm 1. The values of the variable u u represent the relevant part of the continued fraction, the values of the variable v v are used to code the entries in the moving window before any changes are carried out, and the values of the variable w w correspond to the entries in the moving window after the changes are carried out. For i ∈ { 4, …, ν } i\in\{4,\dots,\nu\} and l ∈ { 0, 1 } l\in\{0,1\},

 | P ⁡ ( i, l):= { ( a i, a i − 1, a i − 2, a ν), i = ξ + 2 and l = 1; ( a i, a i − 1, a ν, a ν − 1), i = ξ + 1 and l = 1; ( a i, a ν, a ν − 1, a ν − 2), i = ξ and l = 1; ( a i, a i − 1, a i − 2, a i − 3), otherwise. P(i,l):=\left\{\begin{array}[]{ll}(a_{i},a_{i-1},a_{i-2},a_{\nu}),&\hbox{$i=\xi+2$ and $l=1$;}\\ (a_{i},a_{i-1},a_{\nu},a_{\nu-1}),&\hbox{$i=\xi+1$ and $l=1$;}\\ (a_{i},a_{\nu},a_{\nu-1},a_{\nu-2}),&\hbox{$i=\xi$ and $l=1$;}\\ (a_{i},a_{i-1},a_{i-2},a_{i-3}),&\hbox{otherwise.}\\ \end{array}\right. |  |

We first explain informally the construction of 𝒜 1 \mathcal{A}_{1}. Suppose we take z = z l ​ … ​ z 1 ∈ Σ a ∗ z=z_{l}\dots z_{1}\in\Sigma_{a}^{*}. Now perform Algorithm 1 on z z, and let the word z ′ = z l ′ ​ … ​ z 1 ′ z^{\prime}=z_{l}^{\prime}\dots z_{1}^{\prime} be the output. In order to carry out the operations at step k k in Algorithm 1, we needed to know the values of a k, a k − 1, a k − 2, a k − 3 a_{k},a_{k-1},a_{k-2},a_{k-3}. Because of the periodicity of the continued fraction expansion of a a, there is i ≤ ν i\leq\nu such a k = a i a_{k}=a_{i}. Let l l be 1 1 if k > ν k>\nu and 0 0 otherwise. Then P ⁡ ( i, l) = ( a k, a k − 1, a k − 2, a k − 3) P(i,l)=(a_{k},a_{k-1},a_{k-2},a_{k-3}). Hence in order to reconstruct ( a k, a k − 1, a k − 2, a k − 3), (a_{k},a_{k-1},a_{k-2},a_{k-3}), it is enough to save i i and whether or not k ≤ ν k\leq\nu. Moreover, to perform the operations at step k k in Algorithm 1, we also used the values of the last three entries in the moving window after the changes in the previous step are carried out, but before the window moves to the right. Let us denote the triple consisting of these entries by v = ( v 1, v 2, v 3) ∈ Σ a 3 v=(v_{1},v_{2},v_{3})\in\Sigma_{a}^{3}. So before the operations at step k k are performed, the values in the moving window are ( v 1, v 2, v 3, z k − 3) (v_{1},v_{2},v_{3},z_{k-3}). Note that at step k k in the algorithm, we are reading in z k − 3 z_{k-3}, and not z k z_{k}. However, the value of z k ′ z_{k}^{\prime} is determined at the same step. Indeed, at step k k with k ≥ 4 k\geq 4, the entries in the moving window are changed as follows:

 | ( v 1, v 2, v 3, z k − 3) ↦ ( z k ′, v 1 ′, v 2 ′, v 3 ′), (v_{1},v_{2},v_{3},z_{k-3})\mapsto(z_{k}^{\prime},v_{1}^{\prime},v_{2}^{\prime},v_{3}^{\prime}), |  |

for a certain triple ( v 1 ′, v 2 ′, v 3 ′) ∈ Σ a 3 (v_{1}^{\prime},v_{2}^{\prime},v_{3}^{\prime})\in\Sigma_{a}^{3} with A ⁡ ( P ⁡ ( i, l), v 1, v 2, v 3, z k − 3, z k ′, v 1 ′, v 2 ′, v 3 ′) A(P(i,l),v_{1},v_{2},v_{3},z_{k-3},z_{k}^{\prime},v_{1}^{\prime},v_{2}^{\prime},v_{3}^{\prime}). The values in the moving window for step k − 1 k-1 will be ( v 1 ′, v 2 ′, v 3 ′, z k − 4) (v^{\prime}_{1},v_{2}^{\prime},v_{3}^{\prime},z_{k-4}). Because the value of z k ′ z_{k}^{\prime} is only determined at step k k, and thus at the same time z k − 3 ′ z_{k-3}^{\prime} is being read, we are required to store the value of z k ′ z_{k}^{\prime} for three steps. In order to save this information when moving from state to state, we introduce another triple ( w 1, w 2, w 3) ∈ Σ a 3 (w_{1},w_{2},w_{3})\in\Sigma_{a}^{3}. This triple will always contain the last three digits of z ′ z^{\prime}. That means that before step k k, ( w 1, w 2, w 3) = ( z k ′, z k − 1 ′, z k − 2 ′) (w_{1},w_{2},w_{3})=(z^{\prime}_{k},z^{\prime}_{k-1},z^{\prime}_{k-2}). We now define the set of states of 𝒜 1 \mathcal{A}_{1} as the set of quadruples ( i, l, v, w) (i,l,v,w), where i ≤ ν i\leq\nu, l ∈ { 0, 1 } l\in\{0,1\}, v, w ∈ Σ a 3 v,w\in\Sigma_{a}^{3}. The idea is that in each state of the automaton the pair ( i, l) (i,l) codes the relevant part of the continued fraction expansion, v v contains the entries of the moving window, and w ∈ Σ a 3 w\in\Sigma_{a}^{3} the values of z k ′ z_{k}^{\prime} that we needed to save. The automaton moves from one of these states to another according to the rules described in Algorithm 1.

Here is the definition of the automaton 𝒜 1 = ( S 1, I 1, T 1, F 1) \mathcal{A}_{1}=(S_{1},I_{1},T_{1},F_{1}).

- 1.

The set S 1 S_{1} of states of 𝒜 1 \mathcal{A}_{1} is

 | { ( i, 1, v, w): ξ ≤ i \displaystyle\{(i,1,v,w)\ :\ \xi\leq i | ≤ ν, v, w ∈ Σ a 3 } \displaystyle\leq\nu,v,w\in\Sigma_{a}^{3}\} |  |

 |  | ∪ { ( i, 0, v, w): 3 ≤ i ≤ ν, v, w ∈ Σ a 3 }, \displaystyle\cup\{(i,0,v,w)\ :\ 3\leq i\leq\nu,v,w\in\Sigma_{a}^{3}\}, |  |

- 2.

the set I 1 I_{1} of initial states is

 | { ( i, l, ( 0, 0, 0), ( 0, 0, 0)) ∈ S: i ≥ 4 }, \{(i,l,(0,0,0),(0,0,0))\in S\ :\ i\geq 4\}, |  |

- 3.

the transition table T 1 T_{1} contains the tuples ( s, ( x, y), t) ∈ S 1 × Σ a 2 × S 1 (s,(x,y),t)\in S_{1}\times\Sigma_{a}^{2}\times S_{1} that satisfy w ′ = ( w 2, w 3, y) w^{\prime}=(w_{2},w_{3},y) and one of the following conditions:

  - a.

i ≠ ξ, ( j, l ′) = ( i − 1, l), A ( P ( i, l), v, x, w 1, v ′), i\neq\xi,(j,l^{\prime})=(i-1,l),A(P(i,l),v,x,w_{1},v^{\prime}),

  - b.

i = ξ, l = 1, ( j, l ′) = ( ν, l), A ( P ( i, l), v, x, w 1, v ′) i=\xi,l=1,(j,l^{\prime})=(\nu,l),A(P(i,l),v,x,w_{1},v^{\prime}),

  - c.

i = ξ, l = 0, ( j, l ′) = ( i − 1, l), A ( P ( i, l), v, x, w 1, v ′) i=\xi,l=0,(j,l^{\prime})=(i-1,l),A(P(i,l),v,x,w_{1},v^{\prime})

  - d.

i = 4, j = 3 i=4,j=3, A ⁡ ( P ⁡ ( 4, l), v, x, w 1, v ′), B ⁡ ( a 3, a 2, a 1, v ′, w 2, w 3, y) A(P(4,l),v,x,w_{1},v^{\prime}),B(a_{3},a_{2},a_{1},v^{\prime},w_{2},w_{3},y),

where s = ( i, l, v, w) s=(i,l,v,w), w = ( w 1, w 2, w 3) w=(w_{1},w_{2},w_{3}) and t = ( j, k, v ′, w ′) t=(j,k,v^{\prime},w^{\prime}),

- 4.

the set F 1 F_{1} of final states is { ( i, l, w, y) ∈ S 1: i = 3 } \{(i,l,w,y)\in S_{1}\ :\ i=3\}.

We leave it to the reader to check the details that 𝒜 \mathcal{A} indeed recognizes the set { z ∗ z ′: z, z ′ ∈ Σ a ∗, z ↝ 1 z ′ } \{z*z^{\prime}\ :\ z,z^{\prime}\in\Sigma_{a}^{*},z\rightsquigarrow_{1}z^{\prime}\}. The automata we constructed is non-deterministic, but as mentioned above there is deterministic finite automaton that recognizes the same set.

### Automata for Algorithm 2 and 3

We now describe the non-deterministic automata 𝒜 2 \mathcal{A}_{2} and 𝒜 3 \mathcal{A}_{3} recognizing the sets { z ∗ z ′: z, z ′ ∈ Σ a ∗, z ↝ 2 z ′ } \{z*z^{\prime}\ :\ z,z^{\prime}\in\Sigma_{a}^{*},z\rightsquigarrow_{2}z^{\prime}\} and { z ∗ z ′: z, z ′ ∈ Σ a ∗, z ↝ 3 z ′ } \{z*z^{\prime}\ :\ z,z^{\prime}\in\Sigma_{a}^{*},z\rightsquigarrow_{3}z^{\prime}\}. Again, we have to fix some notation first. Let C ⊆ ℕ ≤ m 3 × ℕ ≤ m 3 × ℕ ≤ m 3 C\subseteq\mathbb{N}_{\leq m}^{3}\times\mathbb{N}_{\leq m}^{3}\times\mathbb{N}_{\leq m}^{3} be the set of triples ( u, v, w) ∈ C (u,v,w)\in C such that

 | w = { ( v 1 + 1, 0, v 3 − 1), if v 1 < u 1, v 2 = u 2 and v 3 > 0; ( v 1, v 2, v 3), otherwise. w=\left\{\begin{array}[]{ll}(v_{1}+1,0,v_{3}-1),&\hbox{if $v_{1}<u_{1}$, $v_{2}=u_{2}$ and $v_{3}>0$;}\\ (v_{1},v_{2},v_{3}),&\hbox{otherwise.}\end{array}\right. |  |

The relation C C represents the operation performed in both Algorithm 2 and 3. As for A A and B B above, the values of the variable u u correspond to the relevant part of the continued fraction, while the values of the variables v v and w w represent the entries in the moving window, before and after any changes are carried out. For i ∈ { 3, …, ν } i\in\{3,\dots,\nu\} and l ∈ { 0, 1 } l\in\{0,1\},

 | Q ⁡ ( i, l):= { ( a i, a i − 1, a ν), i = ξ + 1 and l = 1; ( a i, a ν, a ν − 1), i = ξ and l = 1; ( a i, a i − 1, a i − 2), otherwise. Q(i,l):=\left\{\begin{array}[]{ll}(a_{i},a_{i-1},a_{\nu}),&\hbox{$i=\xi+1$ and $l=1$;}\\ (a_{i},a_{\nu},a_{\nu-1}),&\hbox{$i=\xi$ and $l=1$;}\\ (a_{i},a_{i-1},a_{i-2}),&\hbox{otherwise.}\\ \end{array}\right. |  |

We start with an informal description of the automaton 𝒜 2 \mathcal{A}_{2}. Let z = z l ​ … ​ z 1 ∈ Σ a ∗ z=z_{l}\dots z_{1}\in\Sigma_{a}^{*} and suppose that z ′ = z l ′ ​ … ​ z 1 ′ z^{\prime}=z_{l}^{\prime}\dots z_{1}^{\prime} is the output of Algorithm 2 on input z z. To perform the operations at step k k in Algorithm 2, we again need to know a certain part of the continued fraction expansion of a a; in this case ( a k, a k − 1, a k − 2) (a_{k},a_{k-1},a_{k-2}). As before it is enough to know the natural numbers i ≤ ν i\leq\nu with a k = a i a_{k}=a_{i}, and whether k < ν k<\nu. Set l l to be 1 1 if k > ν k>\nu and 0 0 otherwise. Then Q ⁡ ( i, l) = ( a k, a k − 1, a k − 2) Q(i,l)=(a_{k},a_{k-1},a_{k-2}). When constructing 𝒜 2 \mathcal{A}_{2}, we have to be careful: the Algorithm 2 runs from the right to the left, but the automaton reads the input from the left to the right. Let ( v 1 ′, v 2 ′) ∈ Σ a 2 (v_{1}^{\prime},v_{2}^{\prime})\in\Sigma_{a}^{2} be such that ( z k, v 1 ′, v 2 ′) (z_{k},v_{1}^{\prime},v_{2}^{\prime}) are the entries in the moving window before the changes at step k k are made. Then at step k k, the entries change as follows:

 | ( z k, v 1 ′, v 2 ′) ↦ ( v 1, v 2, z k − 2 ′), (z_{k},v_{1}^{\prime},v_{2}^{\prime})\mapsto(v_{1},v_{2},z_{k-2}^{\prime}), |  |

for some pair ( v 1, v 2) ∈ Σ a 2 (v_{1},v_{2})\in\Sigma_{a}^{2} with C ⁡ ( Q ⁡ ( i, l), z k, v 1 ′, v 2 ′, v 1, v 2, z k − 2 ′) C(Q(i,l),z_{k},v_{1}^{\prime},v_{2}^{\prime},v_{1},v_{2},z_{k-2}^{\prime}). So when the automaton reads in ( z k − 2, z k − 2 ′) (z_{k-2},z_{k-2}^{\prime}), the value of z k z_{k} is used to determine z k − 2 ′ z_{k-2}^{\prime}. Hence in contrast to 𝒜 1 \mathcal{A}_{1}, the automaton 𝒜 2 \mathcal{A}_{2} has to remember the value of z k z_{k}, and not the value of z k ′ z_{k}^{\prime}. We define the states of 𝒜 2 \mathcal{A}_{2} to be tuples ( i, l, v, w) ∈ { 0, …, m } × { 0, 1 } × Σ a 2 × Σ a 2 (i,l,v,w)\in\{0,\dots,m\}\times\{0,1\}\times\Sigma_{a}^{2}\times\Sigma_{a}^{2}. The pair v v is again used to save the entries of the moving window, and w w is needed to remember the previously read entries of z z. The automaton moves from one of these states to another according to the rules described in Algorithm 2. However, since the automaton reads the input backwards, the automaton will go from a state ( i, l, v, w) (i,l,v,w) to a state ( i ′, l ′, v ′, w ′) (i^{\prime},l^{\prime},v^{\prime},w^{\prime}) if Q ⁡ ( i, l) Q(i,l) and Q ⁡ ( i ′, l ′) Q(i^{\prime},l^{\prime}) are the correct parts of the continued fraction expansion of a a and the algorithm transforms ( z k, v 1 ′, v 2 ′) (z_{k},v_{1}^{\prime},v_{2}^{\prime}) to ( v 1, v 2, z k − 2 ′) (v_{1},v_{2},z_{k-2}^{\prime}).

Here is the definition of the automaton 𝒜 2 = ( S 2, I 2, T 2, F 2) \mathcal{A}_{2}=(S_{2},I_{2},T_{2},F_{2}).

- 1.

The set S 2 S_{2} of states of 𝒜 2 \mathcal{A}_{2} is

 | { ( i, 1, v, w): ξ ≤ i \displaystyle\{(i,1,v,w)\ :\ \xi\leq i | ≤ ν, v, w ∈ Σ a 2 } \displaystyle\leq\nu,v,w\in\Sigma_{a}^{2}\} |  |

 |  | ∪ { ( i, 0, v, w): 2 ≤ i ≤ ξ, v, w ∈ Σ a 2 }, \displaystyle\cup\{(i,0,v,w)\ :\ 2\leq i\leq\xi,v,w\in\Sigma_{a}^{2}\}, |  |

- 2.

the set I 2 I_{2} of initial states is

 | { ( i, l, ( 0, 0, 0), ( 0, 0, 0)) ∈ S: i ≥ 3 }, \{(i,l,(0,0,0),(0,0,0))\in S\ :\ i\geq 3\}, |  |

- 3.

the transition table T 2 T_{2} contains the tuples ( s, ( x, y), t) ∈ S 2 × Σ a 2 × S 2 (s,(x,y),t)\in S_{2}\times\Sigma_{a}^{2}\times S_{2} that satisfy w ′ = ( w 2, x) w^{\prime}=(w_{2},x) and one of the following conditions:

  - a.

i ≠ ξ, ( j, l ′) = ( i − 1, l), C ( Q ( i, l), w 1, v ′, v, y), i\neq\xi,(j,l^{\prime})=(i-1,l),C(Q(i,l),w_{1},v^{\prime},v,y),

  - b.

i = ξ, l = 1, ( j, l ′) = ( ν, l), C ( Q ( i, l), w 1, v ′, v, y) i=\xi,l=1,(j,l^{\prime})=(\nu,l),C(Q(i,l),w_{1},v^{\prime},v,y),

  - c.

i = ξ, l = 0, ( j, l ′) = ( i − 1, l), C ( Q ( i, l), w 1, v ′, v, y) i=\xi,l=0,(j,l^{\prime})=(i-1,l),C(Q(i,l),w_{1},v^{\prime},v,y)

  - d.

i = 3, j = 2 i=3,j=2, C ⁡ ( Q ⁡ ( i, 0), w, x, v, y) C(Q(i,0),w,x,v,y),

where s = ( i, l, v, w) s=(i,l,v,w), w = ( w 1, w 2) w=(w_{1},w_{2}) and t = ( j, k, v ′, w ′) t=(j,k,v^{\prime},w^{\prime}),

- 4.

the set F 2 F_{2} of final states is { ( i, l, w, y) ∈ S 2: i = 3 } \{(i,l,w,y)\in S_{2}\ :\ i=3\}.

As in the case of Algorithm 1, we leave it to the reader to verify that 𝒜 2 \mathcal{A}_{2} recognizes the set { z ∗ z ′: z, z ′ ∈ Σ a ∗, z ↝ 2 z ′ } \{z*z^{\prime}\ :\ z,z^{\prime}\in\Sigma_{a}^{*},z\rightsquigarrow_{2}z^{\prime}\}. As before, while 𝒜 2 \mathcal{A}_{2} is non-deterministic, there is a deterministic automata recognizing the same set as 𝒜 2 \mathcal{A}_{2}.

It is left to construct the automaton for Algorithm 3. The only difference between Algorithm 2 and 3 is the direction in which the algorithm runs over the input. Hence the only adjustment we need to make to 𝒜 2 \mathcal{A}_{2}, is to address the change in direction. Let 𝒜 3 = ( S 2, I 2, T 3, F 2) \mathcal{A}_{3}=(S_{2},I_{2},T_{3},F_{2}) be the automaton that has the same states as 𝒜 2 \mathcal{A}_{2}, but whose transition table T 3 T_{3} contains the tuples ( s, ( x, y), t) ∈ S 2 × Σ a 2 × S 2 (s,(x,y),t)\in S_{2}\times\Sigma_{a}^{2}\times S_{2} that satisfy w ′ = ( w 2, y) w^{\prime}=(w_{2},y) and one of the following conditions:

- a.

i ≠ ξ, ( j, l ′) = ( i − 1, l), C ( Q ( i, l), v, x, w 1, v ′), i\neq\xi,(j,l^{\prime})=(i-1,l),C(Q(i,l),v,x,w_{1},v^{\prime}),

- b.

i = ξ, l = 1, ( j, l ′) = ( ν, l), C ( Q ( i, l), v, x, w 1, v ′) i=\xi,l=1,(j,l^{\prime})=(\nu,l),C(Q(i,l),v,x,w_{1},v^{\prime}),

- c.

i = ξ, l = 0, ( j, l ′) = ( i − 1, l), C ( Q ( i, l), v, x, w 1, v ′) i=\xi,l=0,(j,l^{\prime})=(i-1,l),C(Q(i,l),v,x,w_{1},v^{\prime})

- d.

i = 3, j = 2 i=3,j=2, C ⁡ ( Q ⁡ ( i, 0), v, x, w, y) C(Q(i,0),v,x,w,y),

where s = ( i, l, v, w) s=(i,l,v,w), w = ( w 1, w 2) w=(w_{1},w_{2}) and t = ( j, k, v ′, w ′) t=(j,k,v^{\prime},w^{\prime}).

The set { z ∗ z ′: z, z ′ ∈ Σ a ∗, z ↝ 3 z ′ } \{z*z^{\prime}\ :\ z,z^{\prime}\in\Sigma_{a}^{*},z\rightsquigarrow_{3}z^{\prime}\} is recognized by 𝒜 3 \mathcal{A}_{3}. So there is also a deterministic automaton recognizes this set. This completes the proof of Theorem A.

## References

- [1] Connor Ahlbach, Jeremy Usatine, Christiane Frougny, and Nicholas Pippenger. Efficient algorithms for Zeckendorf arithmetic. Fibonacci Quart., 51(3):249–255, 2013.
- [2] Jean-Paul Allouche and Jeffrey Shallit. Automatic sequences. Cambridge University Press, Cambridge, 2003. Theory, applications, generalizations.
- [3] Valérie Berthé. Autour du système de numération d’Ostrowski. Bull. Belg. Math. Soc. Simon Stevin, 8(2):209–239, 2001. Journées Montoises d’Informatique Théorique (Marne-la-Vallée, 2000).
- [4] Véronique Bruyère and Georges Hansel. Bertrand numeration systems and recognizability. Theoret. Comput. Sci., 181(1):17–43, 1997. Latin American Theoretical INformatics (Valparaíso, 1995).
- [5] Véronique Bruyère, Georges Hansel, Christian Michaux, and Roger Villemaire. Logic and p p -recognizable sets of integers. Bull. Belg. Math. Soc. Simon Stevin, 1(2):191–238, 1994. Journées Montoises (Mons, 1992).
- [6] J. Richard Büchi. Weak second-order arithmetic and finite automata. Z. Math. Logik Grundlagen Math., 6:66–92, 1960.
- [7] C. F. Du, H. Mousavi, L. Schaeffer, and J. Shallit. Decision algorithms for fibonacci-automatic words, with applications to pattern avoidance. ArXiv 1406.0670, 2014.
- [8] Christiane Frougny. Representations of numbers and finite automata. Math. Systems Theory, 25(1):37–60, 1992.
- [9] Philipp Hieronymi. Expansions of the ordered additive group of real numbers by two discrete subgroups. J. Symbolic Logic, to appear, arXiv:1407.7002, 2015.
- [10] Bernard R. Hodgson. Décidabilité par automate fini. Ann. Sci. Math. Québec, 7(1):39–57, 1983.
- [11] Bakhadyr Khoussainov and Anil Nerode. Automata theory and its applications, volume 21 of Progress in Computer Science and Applied Logic. Birkhäuser Boston, Inc., Boston, MA, 2001.
- [12] Nathalie Loraud. β \beta -shift, systèmes de numération et automates. J. Théor. Nombres Bordeaux, 7(2):473–498, 1995.
- [13] Alexander Ostrowski. Bemerkungen zur Theorie der Diophantischen Approximationen. Abh. Math. Sem. Univ. Hamburg, 1(1):77–98, 1922.
- [14] Andrew M. Rockett and Peter Szüsz. Continued fractions. World Scientific Publishing Co., Inc., River Edge, NJ, 1992.
- [15] Jeffrey Shallit. Numeration systems, linear recurrences, and regular sets. Inform. and Comput., 113(2):331–347, 1994.
- [16] Roger Villemaire. The theory of ⟨ 𝐍, +, V k, V l ⟩ \langle{\bf N},+,V_{k},V_{l}\rangle is undecidable. Theoret. Comput. Sci., 106(2):337–349, 1992.
- [17] E. Zeckendorf. Représentation des nombres naturels par une somme de nombres de Fibonacci ou de nombres de Lucas. Bull. Soc. Roy. Sci. Liège, 41:179–182, 1972.

[◄][4][image: ar5iv homepage] [5]
[Feeling lucky?][6] [7]
[Conversion report][8]
[Report an issue][9]
[View original on arXiv][10] [►][11]


## Links

[1]: mailto:phierony@illinois.edu
[2]: http://www.math.uiuc.edu/~phierony
[3]: mailto:aterry@illinois.edu
[4]: /html/1407.6999
[5]: /
[6]: /feeling_lucky
[7]: /land_of_honey_and_milk
[8]: /log/1407.7000
[9]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1407.7000
[10]: https://arxiv.org/pdf/1407.7000
[11]: /html/1407.7001
