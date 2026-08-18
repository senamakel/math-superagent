<!-- source: https://ar5iv.labs.arxiv.org/html/1806.09534 | converted from HTML -->

[1806.09534] The number of valid factorizations of Fibonacci prefixes

# The number of valid factorizations of Fibonacci prefixes Journal: Theoretical Computer Science

Pierre Bonardo Address: Aix Marseille Univ, CNRS, Centrale Marseille, I2M, Marseille, France Anna E. Frid Email: [anna.e.frid@gmail.com][1] URL: [http://iml.univ-mrs.fr/˜frid/][2] Address: Aix Marseille Univ, CNRS, Centrale Marseille, I2M, Marseille, France Jeffrey Shallit Email: [shallit@uwaterloo.ca][3] URL: [https://cs.uwaterloo.ca/˜shallit/][4] Address: School of Computer Science, University of Waterloo, Waterloo, ON N2L 3G1, Canada

###### Abstract

We establish several recurrence relations and an explicit formula for V ⁡ ( n) V(n), the number of factorizations of the length- n n prefix of the Fibonacci word into a (not necessarily strictly) decreasing sequence of standard Fibonacci words. In particular, we show that the sequence V ⁡ ( n) V(n) is the shuffle of the ceilings of two linear functions of n n.

###### Keywords:

numeration systems , Fibonacci numeration system , Fibonacci word

###### 2010 MSC

68R15, 11B39

## 1 Introduction

In the classical Fibonacci, or Zeckendorf, numeration system [6, 11], a positive integer is represented as a sum of Fibonacci numbers:

 | n = F m k + F m k − 1 + ⋯ + F m 0, n=F_{m_{k}}+F_{m_{k-1}}+\cdots+F_{m_{0}}, |  |

where m k > m k − 1 > ⋯ > m 0 ≥ 2 m_{k}>m_{k-1}>\cdots>m_{0}\geq 2 and, as usual, F 0 = 0 F_{0}=0, F 1 = 1 F_{1}=1, and F m + 2 = F m + 1 + F m F_{m+2}=F_{m+1}+F_{m} for all m ≥ 0 m\geq 0. For example, 16 = 13 + 3 = F 7 + F 4 = [100100] F 16=13+3=F_{7}+F_{4}=[100100]_{F}, where a digit in brackets is 1 1 if the respective Fibonacci number appears in the sum, and 0 0 otherwise. Here a representation ends by the digits corresponding to F 4 = 3 F_{4}=3, F 3 = 2 F_{3}=2 and F 2 = 1 F_{2}=1.

Under the condition that m i m_{i} and m i + 1 m_{i+1} are never consecutive, that is, m i + 1 − m i ≥ 2 m_{i+1}-m_{i}\geq 2, or, equivalently, that the Fibonacci numbers F i F_{i} are chosen greedily, such a canonical representation is unique, and the language L V L_{V} of all canonical representations is given by the regular expression ϵ + 1 ​ ( 0 + 01) ∗ \epsilon+1(0+01)^{*}, where the empty word ϵ \epsilon is the representation of 0. At the same time, if consecutive Fibonacci numbers are allowed, but at most once each, the number of such legal representations of n n is the well-known integer sequence [A000119][5] from the Online Encyclopedia of Integer Sequences (OEIS) [8]. Its values oscillate between 1 1 (on numbers of the form F i − 1 F_{i}-1) and n + 1 \sqrt{n+1} (on numbers of the form n = F i 2 − 1 n=F_{i}^{2}-1) [10].

For example, since

 | 16 \displaystyle 16 | = 13 + 3 = 8 + 5 + 3 = 8 + 5 + 2 + 1 = 13 + 2 + 1 \displaystyle=13+3=8+5+3=8+5+2+1=13+2+1 |  |

 |  | = [100100] F = [11100] F = [11011] F = [100011] F, \displaystyle=[100100]_{F}=[11100]_{F}=[11011]_{F}=[100011]_{F}, |  |

the number of legal representations of 16 is 4. Each legal representation of n n can be obtained from a canonical one by a series of replacements

 | ⋯ 100 ⋯ ⟷ ⋯ 011 ⋯, \cdots 100\cdots\longleftrightarrow\cdots 011\cdots, |  |

corresponding to the replacement of a Fibonacci number F m + 2 F_{m+2} by F m + 1 + F m F_{m+1}+F_{m}.

In this paper, we allow even more freedom in Fibonacci representations of n n, allowing the transformations

 | ⋯ k 0 l ⋯ ⟷ ⋯ ( k − 1) 1 ( l + 1) ⋯ \cdots k0l\cdots\longleftrightarrow\cdots(k-1)\;1(l+1)\cdots |  | (1) |

for all k > 0 k>0, l ≥ 0 l\geq 0. Note that the introduced transformation corresponds to passing from a sum of the form k ​ F m + 1 + l ​ F m − 1 kF_{m+1}+lF_{m-1} to the sum ( k − 1) ​ F m + 1 + F m + ( l + 1) ​ F m − 1 (k-1)F_{m+1}+F_{m}+(l+1)F_{m-1}, and, in particular, does not change the represented number.

The representations that can be obtained from the canonical one by a series of transformations as in ( 1) are called valid, and were introduced in [4] in a more general setting because of their link to the Fibonacci word and factorizations of its prefixes, as explained below. Clearly, each legal representation is valid, but the opposite is not true. For example, starting from the legal representation 16 = [11011] F 16=[11011]_{F}, we can find two more valid representations

 | 16 = [10121] F = [1221] F, 16=[10121]_{F}=[1221]_{F}, |  |

and starting from the legal representation 16 = [11100] F 16=[11100]_{F}, we find a new representation

 | 16 = [20000] F, 16=[20000]_{F}, |  |

so that the total number of valid representations of 16 is 7.

Let V ⁡ ( n) V(n) denote the number of valid representations of n n. The goal of this paper is to prove a precise formula for V ⁡ ( n) V(n), given below in Theorem 1. Our formula demonstrates that the values of V ⁡ ( n) V(n) are determined by the shuffle of two straight lines of irrational slope; see Fig. 1.

Figure 1: First 100 values of V ⁡ ( n) V(n)

## 2 Notation and Sturmian representations

We use notation common in combinatorics on words; the reader is referred, for example, to [3] for an introduction. Given a finite word u u, we denote its length by | u | |u|. The power u k u^{k} just means the concatenation u k = u ⋯ u ⏟ k u^{k}=\underbrace{u\cdots u}_{k}. The i i ’th symbol of a finite or infinite word u u is denoted by u ⁡ [i] u[i], so that u = u [1] u [2] ⋯ u=u[1]u[2]\cdots. A factor w [i + 1] w [i + 2] ⋯ w [j] w[i+1]w[i+2]\cdots w[j] of a finite or infinite word w w, or, more precisely, its occurrence starting from position i + 1 i+1 of w w, is denoted by w ( i.. j] w(i..j]. In particular, for j ≥ 0 j\geq 0, the word w ( 0.. j] w(0..j] is the prefix of w w of length j j.

The standard Fibonacci sequence ( f n) (f_{n}) of words over the binary alphabet { a, b } \{a,b\} is defined as follows:

 | f − 1 = b, f 0 = a, f n + 1 = f n ​ f n − 1 ​ for all ​ n ≥ 0. f_{-1}=b,\quad\quad f_{0}=a,\quad\quad f_{n+1}=f_{n}f_{n-1}\mbox{~for all~}n\geq 0. |  | (2) |

The word f n f_{n} is called also the standard word of order n n. In particular, f 1 = a ​ b f_{1}=ab, f 2 = a ​ b ​ a f_{2}=aba, f 3 = a ​ b ​ a ​ a ​ b f_{3}=abaab, f 4 = a ​ b ​ a ​ a ​ b ​ a ​ b ​ a f_{4}=abaababa, and so on. From the definition, we easily see that the length of f n f_{n} is the Fibonacci number F n + 2 F_{n+2}.

The infinite word

 | 𝐟 = lim n → ∞ f n = a b a a b a b a a b a a b a b a a b a b a ⋯ {\bf f}=\lim_{n\to\infty}f_{n}=abaababaabaababaababa\cdots |  |

is called the Fibonacci infinite word. Here we index it starting with 𝐟 ⁡ [1] = a {\bf f}[1]=a.

In the Fibonacci, or Zeckendorf numeration system, a non-negative integer N < F n + 3 N<F_{n+3} is represented as a sum of Fibonacci numbers

 | N = ∑ 0 ≤ i ≤ n k i ​ F i + 2, N=\sum_{0\leq i\leq n}k_{i}F_{i+2}, |  | (3) |

where k i ∈ { 0, 1 } k_{i}\in\{0,1\} for i ≥ 0 i\geq 0. In the canonical version of the definition, the following condition holds:

 | for ​ i ≥ 1, if ​ k i = 1, then ​ k i − 1 = 0. \mbox{for }i\geq 1,\mbox{ if }k_{i}=1,\mbox{ then }k_{i-1}=0. |  | (4) |

Under this nonadjacency condition, the representation of N N is unique up to leading zeros. However, by removing the nonadjacency condition, we can get multiple representations: for example, 14 = F 7 + F 2 = F 6 + F 5 + F 2 = F 6 + F 4 + F 3 + F 2 14=F_{7}+F_{2}=F_{6}+F_{5}+F_{2}=F_{6}+F_{4}+F_{3}+F_{2}. We call such representations legal and denote a representation N = ∑ 0 ≤ i ≤ n k i ​ F i + 2 N=\sum_{0\leq i\leq n}k_{i}F_{i+2} by N = [k n ⋯ k 0] F N=[k_{n}\cdots k_{0}]_{F}. If the condition ( 4) holds, we call the representation canonical.

Let L ⁡ ( n) L(n) denote the number of legal representations of n n. The sequence ( L ⁡ ( n)) (L(n)) is well-studied (see, e.g., [2]) and listed in the OEIS as sequence [A000119][5]. In particular, 1 ≤ L ⁡ ( n) ≤ n + 1 1\leq L(n)\leq\sqrt{n+1}, and both bounds are precise [10].

The following lemma is a particular case of [4, Prop. 2].

###### Lemma 1.

For all k 0, …, k n k_{0},\ldots,k_{n} such that k i ∈ { 0, 1 } k_{i}\in\{0,1\}, the word f n k n f n − 1 k n − 1 ⋯ f 0 k 0 f_{n}^{k_{n}}f_{n-1}^{k_{n-1}}\cdots f_{0}^{k_{0}} is a prefix of the Fibonacci word 𝐟 \bf f.

So L ⁡ ( n) L(n) is also the number of ways to factor the prefix 𝐟 ( 0.. n] {\bf f}(0..n] of the Fibonacci word as a sequence of standard words in strictly decreasing order.

To expand this definition, in this note we consider all factorizations of Fibonacci prefixes 𝐟 ( 0.. n] {\bf f}(0..n] as a concatenation of standard words in (non-strictly) decreasing order. We write N = [k n ⋯ k 0] F N=[k_{n}\cdots k_{0}]_{F} and call this representation of N N valid if k i ≥ 0 k_{i}\geq 0 for all i i and 𝐟 ( 0.. N] = f n k n f n − 1 k n − 1 ⋯ f 0 k 0 {\bf f}(0..N]=f_{n}^{k_{n}}f_{n-1}^{k_{n-1}}\cdots f_{0}^{k_{0}}. Note that according to the previous lemma, every legal representation is valid, but not the other way around. For example, 𝐟 ( 0..14] = ( a b a a b) ( a b a) ( a b a) ( a b a) {\bf f}(0..14]=(abaab)(aba)(aba)(aba), making the representation 14 = [1300] F 14=[1300]_{F} valid. Theorem 1 of [4] says, in particular, that valid representations are exactly those that can be obtained from the canonical one by a series of transformations ( 1).

Note that a digit of a valid representation cannot exceed 3 since the Fibonacci word does not contain a factor of the form u 4 u^{4} for any non-empty word u u [5].

The number of valid representations of N N is denoted by V ⁡ ( N) V(N), and this note is devoted to the study of the sequence ( V ⁡ ( n)) (V(n)), recently listed in the OEIS as sequence [A300066][6]. Clearly, V ⁡ ( n) ≥ L ⁡ ( n) V(n)\geq L(n), and moreover, we prove an explicit formula for V ⁡ ( n) V(n) that implies its linear growth.

## 3 Result

As is well-known, the Fibonacci infinite word

 | 𝐟 = a b a a b a b a ⋯ {\bf f}=abaababa\cdots |  |

is the fixed point of the Fibonacci morphism μ: a → a ​ b, b → a \mu:a\to ab,b\to a; moreover, for each n ≥ 1 n\geq 1, we have f n = μ ⁡ ( f n − 1) f_{n}=\mu(f_{n-1}). Consequently, if N = [k n ⋯ k 0] F N=[k_{n}\cdots k_{0}]_{F}, then Lemma 1 implies that

 | μ ( 𝐟 ( 0.. N]) = μ ( 𝐟 ( 0.. [k n ⋯ k 0] F]) = μ ( f n k n ⋯ f 0 k 0) = f n + 1 k n ⋯ f 1 k 0 = 𝐟 ( 0.. [k n ⋯ k 0 0] F]. \mu({\bf f}(0..N])=\mu({\bf f}(0..[k_{n}\cdots k_{0}]_{F}])=\mu(f_{n}^{k_{n}}\cdots f_{0}^{k_{0}})=f_{n+1}^{k_{n}}\cdots f_{1}^{k_{0}}={\bf f}(0..[k_{n}\cdots k_{0}0]_{F}]. |  |

Let φ \varphi denote the golden ratio: φ = 1 + 5 2 \varphi=\frac{1+\sqrt{5}}{2}. It is important that the Fibonacci word is a Sturmian word of slope 1 / ( φ + 1) = 1 / φ 2 1/(\varphi+1)=1/\varphi^{2} and zero intercept (see Example 2.1.24 of [3]), that is, for all n n, we have

 | 𝐟 ⁡ [n] = { a, if ​ { n / φ 2 } < 1 − 1 / φ 2; b, otherwise. {\bf f}[n]=\begin{cases}a,&\mbox{~if~}\{n/\varphi^{2}\}<1-1/\varphi^{2};\\ b,&\mbox{~otherwise}.\end{cases} |  | (5) |

Here { x } = x − ⌊ x ⌋ \{x\}=x-\lfloor x\rfloor denotes the fractional part of x x.

###### Proposition 1.

If 𝐟 ⁡ [n] = a {\bf f}[n]=a, all valid representations of n n end with an even number of 0s. If 𝐟 ⁡ [n] = b {\bf f}[n]=b, all of them end with an odd number of 0s.

###### Proof.

It suffices to consult the definition of a valid representation and notice that f i f_{i} ends with a a if and only if i i is even. ∎

We now state our main result.

###### Theorem 1.

If 𝐟 ⁡ [n] = a {\bf f}[n]=a, then V ⁡ ( n) = ⌈ n / φ 2 ⌉ V(n)=\lceil n/\varphi^{2}\rceil, or, equivalently, V ⁡ ( n) V(n) is equal to the number of occurrences of b b in 𝐟 ( 0.. n] {\bf f}(0..n], plus one. If 𝐟 ⁡ [n] = b {\bf f}[n]=b, then V ⁡ ( n) = ⌈ n / φ 3 ⌉ V(n)=\lceil n/\varphi^{3}\rceil, or, equivalently, V ⁡ ( n) V(n) is equal to the number of occurrences of a ​ a aa in 𝐟 ( 0.. n] {\bf f}(0..n], plus one.

To prove the theorem, we will need several more propositions.

###### Proposition 2.

- (a)

V ⁡ ( [r ​ 0] F) ≥ V ⁡ ( [r] F) V([r0]_{F})\geq V([r]_{F}) for all r ∈ { 0, 1 } ∗ r\in\{0,1\}^{*}.

- (b)

For all k ≥ 0 k\geq 0 and all r ′ ∈ { 0, 1 } ∗ r^{\prime}\in\{0,1\}^{*}, we have V ⁡ ( [r ′ ​ 10 2 ​ k + 1] F) = V ⁡ ( [r ′ ​ 10 2 ​ k] F) V([r^{\prime}10^{2k+1}]_{F})=V([r^{\prime}10^{2k}]_{F}).

###### Proof.

(a): Consider a factorization 𝐟 ( 0.. [r] F] = f n k n f n − 1 k n − 1 ⋯ f 0 k 0 {\bf f}(0..[r]_{F}]=f_{n}^{k_{n}}f_{n-1}^{k_{n-1}}\cdots f_{0}^{k_{0}}. Applying the Fibonacci morphism μ \mu to both sides, we get the factorization 𝐟 ( 0.. [r 0] F] = f n + 1 k n f n k n − 1 ⋯ f 1 k 0 {\bf f}(0..[r0]_{F}]=f_{n+1}^{k_{n}}f_{n}^{k_{n-1}}\cdots f_{1}^{k_{0}}. So the number of factorizations of 𝐟 ( 0.. [r 0] F] {\bf f}(0..[r0]_{F}] (which is equal to V ⁡ ( [r ​ 0] F) V([r0]_{F})) is at least as large as the number of factorizations of 𝐟 ( 0.. [r] F] {\bf f}(0..[r]_{F}] (which is equal to V ⁡ ( [r] F) V([r]_{F})).

(b) If, in addition r = r ′ ​ 10 2 ​ k r=r^{\prime}10^{2k} for some k ≥ 0 k\geq 0, we see that 𝐟 ( 0.. [r] F] {\bf f}(0..[r]_{F}] ends with f 2 ​ k f_{2k} and 𝐟 ( 0.. [r 0] F] {\bf f}(0..[r0]_{F}] ends with f 2 ​ k + 1 f_{2k+1}, which in turn ends with b b. From Proposition 1, no factorization of 𝐟 ( 0.. [r 0] F] {\bf f}(0..[r0]_{F}] ends with f 0 f_{0}; that is, such a factorization must be of the form 𝐟 ( 0.. [r 0] F] = f n + 1 k n f n k n − 1 ⋯ f 1 k 0 {\bf f}(0..[r0]_{F}]=f_{n+1}^{k_{n}}f_{n}^{k_{n-1}}\cdots f_{1}^{k_{0}}. Taking the μ \mu -preimage, we get the factorization 𝐟 ( 0.. [r] F] = f n k n f n − 1 k n − 1 ⋯ f 0 k 0 {\bf f}(0..[r]_{F}]=f_{n}^{k_{n}}f_{n-1}^{k_{n-1}}\cdots f_{0}^{k_{0}}, thus establishing a bijection and the equality V ⁡ ( [r ′ ​ 10 2 ​ k + 1] F) = V ⁡ ( [r ′ ​ 10 2 ​ k] F) V([r^{\prime}10^{2k+1}]_{F})=V([r^{\prime}10^{2k}]_{F}). ∎

###### Proposition 3.

We have

 | V ⁡ ( [z ​ 10 2 ​ k] F) = V ⁡ ( [z ​ 10 2 ​ k − 2] F) + V ⁡ ( [z ​ ( 01) k] F). V([z10^{2k}]_{F})=V([z10^{2k-2}]_{F})+V([z(01)^{k}]_{F}). |  |

for all z ∈ { 0, 1 } ∗ z\in\{0,1\}^{*} and all k ≥ 1 k\geq 1.

###### Proof.

Proposition 1 tells us that 𝐟 ⁡ [[z ​ 10 2 ​ k] F] = a {\bf f}[[z10^{2k}]_{F}]=a, and moreover, since k > 0 k>0, the prefix of length [z ​ 10 2 ​ k] F [z10^{2k}]_{F} of 𝐟 {\bf f} ends with a ​ b ​ a aba, which is a suffix of f 2 ​ k f_{2k}. Consider a valid factorization 𝐟 ( 0.. [z 10 2 ​ k] F] = f n k n f n − 1 k n − 1 ⋯ f 0 k 0 {\bf f}(0..[z10^{2k}]_{F}]=f_{n}^{k_{n}}f_{n-1}^{k_{n-1}}\cdots f_{0}^{k_{0}}. If k 0 = 0 k_{0}=0, then k 1 = 0 k_{1}=0 since f 1 f_{1} ends with b b, so the factorization is of the form f n k n f n − 1 k n − 1 ⋯ f 2 k 2 f_{n}^{k_{n}}f_{n-1}^{k_{n-1}}\cdots f_{2}^{k_{2}}. Taking the μ 2 \mu^{2} -preimage, we get a factorization f n − 2 k n f n − 3 k n − 1 ⋯ f 0 k 2 f_{n-2}^{k_{n}}f_{n-3}^{k_{n-1}}\cdots f_{0}^{k_{2}} of 𝐟 ( 0.. [z 10 2 ​ k − 2] F] {\bf f}(0..[z10^{2k-2}]_{F}]. Moreover, μ 2 \mu^{2} is a bijection between all the factorizations of 𝐟 ( 0.. [z 10 2 ​ k − 2] F] {\bf f}(0..[z10^{2k-2}]_{F}] and the factorizations of 𝐟 ( 0.. [z 10 2 ​ k] F] {\bf f}(0..[z10^{2k}]_{F}] with k 0 = k 1 = 0 k_{0}=k_{1}=0.

On the other hand, if k 0 ≠ 0 k_{0}\neq 0, then k 0 = 1 k_{0}=1 since the word that we factor ends with a ​ b ​ a aba. Removing this last occurrence of f 0 = a f_{0}=a, we get the prefix of 𝐟 {\bf f} of length [z ​ 10 2 ​ k] F − 1 = [z ​ ( 01) k ​ 0] F [z10^{2k}]_{F}-1=[z(01)^{k}0]_{F}. From Proposition 2, the number of valid factorizations of 𝐟 ( 0.. [z ( 01) k 0] F] {\bf f}(0..[z(01)^{k}0]_{F}] is equal to that of 𝐟 ( 0.. [z ( 01) k] F] {\bf f}(0..[z(01)^{k}]_{F}]. Combining the two possibilities, we get the statement of the proposition. ∎

###### Proposition 4.

For all z ∈ { 0, 1 } ∗ z\in\{0,1\}^{*} and for all k ≥ 1 k\geq 1, we have

 | V ⁡ ( [z ​ 10 k ​ 1] F) = { V ⁡ ( [z ​ 10 k + 1] F), if ​ k ​ is odd; V ⁡ ( [z ​ 10 k] F) + V ⁡ ( [z ​ ( 01) k / 2] F), if ​ k ​ is even. V([z10^{k}1]_{F})=\begin{cases}V([z10^{k+1}]_{F}),&\mbox{~if~}k\mbox{~is odd};\\ V([z10^{k}]_{F})+V([z(01)^{k/2}]_{F}),&\mbox{~if~}k\mbox{~is even.}\end{cases} |  |

###### Proof.

If k k is odd, then [z ​ 10 k ​ 1] F = [z ​ 10 k + 1] F + 1 [z10^{k}1]_{F}=[z10^{k+1}]_{F}+1, and the prefix 𝐟 ( 0.. [z 10 k + 1] F] {\bf f}(0..[z10^{k+1}]_{F}] was considered in the previous proposition. It ends with a ​ b ​ a aba, and the symbol added to get 𝐟 ( 0.. [z 10 k 1] F] {\bf f}(0..[z10^{k}1]_{F}] is also a a. So 𝐟 ( 0.. [z 10 k 1] F] {\bf f}(0..[z10^{k}1]_{F}] ends with a ​ b ​ a ​ a abaa, and all valid factorizations end with f 0 f_{0}. This means that the number of valid factorizations of 𝐟 ( 0.. [z 10 k 1] F] {\bf f}(0..[z10^{k}1]_{F}] is equal to that of 𝐟 [0.. [z 10 k + 1] F] {\bf f}[0..[z10^{k+1}]_{F}]; that is, V ⁡ ( [z ​ 10 k ​ 1] F) = V ⁡ ( [z ​ 10 k + 1] F) V([z10^{k}1]_{F})=V([z10^{k+1}]_{F}).

If k k is even, k > 0 k>0, then 𝐟 ( 0.. [z 10 k 1] F] {\bf f}(0..[z10^{k}1]_{F}] ends with f 3 ​ f 0 = a ​ b ​ a ​ a ​ b ​ a f_{3}f_{0}=abaaba. In particular, the last factor of any valid factorization of 𝐟 ( 0.. [z 10 k 1] F] {\bf f}(0..[z10^{k}1]_{F}] is either f 0 = a f_{0}=a, or f 2 = a ​ b ​ a f_{2}=aba. Indeed, f 4 = a ​ b ​ a ​ a ​ b ​ a ​ b ​ a f_{4}=abaababa and thus for all l > 2 l>2 the f 2 ​ l f_{2l} do not have a common suffix with 𝐟 ( 0.. [z 10 k 1] F] {\bf f}(0..[z10^{k}1]_{F}]. So, letting V 2 ​ ( n) V_{2}(n) denote the number of factorizations of 𝐟 ( 0.. n] {\bf f}(0..n] of the form f n k n f n − 1 k n − 1 ⋯ f 2 k 2 f_{n}^{k_{n}}f_{n-1}^{k_{n-1}}\cdots f_{2}^{k_{2}}, we get

 | V ⁡ ( [z ​ 10 k ​ 1] F) \displaystyle V([z10^{k}1]_{F}) | = V ⁡ ( [z ​ 10 k ​ 1] F − 1) + V 2 ​ ( [z ​ 10 k ​ 1] F − 3) \displaystyle=V([z10^{k}1]_{F}-1)+V_{2}([z10^{k}1]_{F}-3) |  |

 |  | = V ⁡ ( [z ​ 10 k + 1] F) + V 2 ​ ( [z ​ ( 01) k / 2 ​ 00] F) \displaystyle=V([z10^{k+1}]_{F})+V_{2}([z(01)^{k/2}00]_{F}) |  |

 |  | = V ⁡ ( [z ​ 10 k] F) + V ⁡ ( [z ​ ( 01) k / 2] F). \displaystyle=V([z10^{k}]_{F})+V([z(01)^{k/2}]_{F}). |  |

Here the last equality follows from Proposition 2 (for the first addend) and by taking μ − 2 \mu^{-2} of each factorization (for the second one). ∎

Propositions 2 to 4 give a full list of recurrence relations sufficient to compute V ⁡ ( n) V(n) for every n > 1 n>1, starting from V ⁡ ( 1) = 1 V(1)=1. Before using them to prove the main theorem, we consider two particular cases.

###### Corollary 1.

For all k ≥ 1 k\geq 1 we have

 | V ⁡ ( F 2 ​ k + 1 − 1) = V ⁡ ( F 2 ​ k + 1 − 2) = F 2 ​ k − 1 V(F_{2k+1}-1)=V(F_{2k+1}-2)=F_{2k-1} |  |

and

 | V ⁡ ( F 2 ​ k + 2 − 2) = F 2 ​ k V(F_{2k+2}-2)=F_{2k} |  |

###### Proof.

For k = 1 k=1, the equalities can be easily checked: V ⁡ ( F 3 − 1) = V ⁡ ( 1) = V ⁡ ( F 3 − 2) = V ⁡ ( 0) = 1 = F 1 V(F_{3}-1)=V(1)=V(F_{3}-2)=V(0)=1=F_{1}, and V ⁡ ( F 4 − 2) = V ⁡ ( 1) = 1 = F 2 V(F_{4}-2)=V(1)=1=F_{2}. We also observe that F 2 ​ k + 1 − 1 = [( 10) k − 1 ​ 1] F F_{2k+1}-1=[(10)^{k-1}1]_{F}, F 2 ​ k + 1 − 2 = [( 10) k − 1 ​ 0] F F_{2k+1}-2=[(10)^{k-1}0]_{F}, and F 2 ​ k + 2 − 2 = [( 10) k − 1 ​ 01] F F_{2k+2}-2=[(10)^{k-1}01]_{F}. Now we assume that the equalities hold for k k, and use Propositions 3 and 4 to prove they hold for k + 1 k+1:

 | V ⁡ ( F 2 ​ k + 3 − 2) \displaystyle V(F_{2k+3}-2) | = V ⁡ ( [( 10) k ​ 0] F) = V ⁡ ( [( 10) k − 1 ​ 1] F) + V ⁡ ( [( 10) k − 1 ​ 01] F) \displaystyle=V([(10)^{k}0]_{F})=V([(10)^{k-1}1]_{F})+V([(10)^{k-1}01]_{F}) |  |

 |  | = V ⁡ ( F 2 ​ k + 1 − 1) + V ⁡ ( F 2 ​ k + 2 − 2) = F 2 ​ k − 1 + F 2 ​ k = F 2 ​ k + 1, \displaystyle=V(F_{2k+1}-1)+V(F_{2k+2}-2)=F_{2k-1}+F_{2k}=F_{2k+1}, |  |

 | V ⁡ ( F 2 ​ k + 3 − 1) \displaystyle V(F_{2k+3}-1) | = V ⁡ ( [( 10) k ​ 1] F) = V ⁡ ( [( 10) k ​ 0] F) = V ⁡ ( F 2 ​ k + 3 − 2) = F 2 ​ k + 1, \displaystyle=V([(10)^{k}1]_{F})=V([(10)^{k}0]_{F})=V(F_{2k+3}-2)=F_{2k+1}, |  |

 | V ⁡ ( F 2 ​ k + 4 − 2) \displaystyle V(F_{2k+4}-2) | = V ⁡ ( [( 10) k ​ 01] F) = V ⁡ ( [( 10) k ​ 0] F) + V ⁡ ( [( 10) k − 1 ​ 01] F) \displaystyle=V([(10)^{k}01]_{F})=V([(10)^{k}0]_{F})+V([(10)^{k-1}01]_{F}) |  |

 |  | = V ⁡ ( F 2 ​ k + 3 − 2) + V ⁡ ( F 2 ​ k + 2 − 2) = F 2 ​ k + 1 + F 2 ​ k = F 2 ​ k + 2. \displaystyle=V(F_{2k+3}-2)+V(F_{2k+2}-2)=F_{2k+1}+F_{2k}=F_{2k+2}. |  |

∎

###### Corollary 2.

For all k ≥ 1 k\geq 1, we have

 | V ⁡ ( F 2 ​ k) = V ⁡ ( F 2 ​ k + 1) = F 2 ​ k − 2 + 1. V(F_{2k})=V(F_{2k+1})=F_{2k-2}+1. |  |

###### Proof.

For k = 1 k=1, the equalities can be easily checked: V ⁡ ( F 2) = V ⁡ ( 1) = V ⁡ ( F 3) = V ⁡ ( 2) = 1 = F 0 + 1 V(F_{2})=V(1)=V(F_{3})=V(2)=1=F_{0}+1. Suppose the equalities hold for k k; let us prove them for k + 1 k+1. With Proposition 3, we have

 | V ⁡ ( F 2 ​ k + 2) = V ⁡ ( [10 2 ​ k] F) = V ⁡ ( [10 2 ​ k − 2] F) + V ⁡ ( [( 10) k − 1 ​ 1] F) = F 2 ​ k − 2 + 1 + F 2 ​ k − 1 = F 2 ​ k + 1, V(F_{2k+2})=V([10^{2k}]_{F})=V([10^{2k-2}]_{F})+V([(10)^{k-1}1]_{F})=F_{2k-2}+1+F_{2k-1}=F_{2k}+1, |  |

and with Proposition 2, we have

 | V ⁡ ( F 2 ​ k + 3) = V ⁡ ( [10 2 ​ k + 1] F) = V ⁡ ( [10 2 ​ k] F) = V ⁡ ( F 2 ​ k + 2) = F 2 ​ k + 1. V(F_{2k+3})=V([10^{2k+1}]_{F})=V([10^{2k}]_{F})=V(F_{2k+2})=F_{2k}+1. |  |

∎

###### Proposition 5.

Let n = [z] F n=[z]_{F} and n ′ = [z ​ 0] F n^{\prime}=[z0]_{F} be such that 𝐟 ⁡ [n] = a {\bf f}[n]=a. Then ⌈ n / φ 2 ⌉ = ⌈ n ′ / φ 3 ⌉ \lceil n/\varphi^{2}\rceil=\lceil n^{\prime}/\varphi^{3}\rceil.

###### Proof.

Let us write the canonical Fibonacci representation of n n as ∑ 1 ≤ i ≤ l F m i \sum_{1\leq i\leq l}F_{m_{i}}, where 2 ≤ m 1 < m 2 < ⋯ < m l 2\leq m_{1}<m_{2}<\cdots<m_{l}. Since 𝐟 ⁡ [n] = a {\bf f}[n]=a, from Proposition 1 we get that m 1 m_{1} is even.

Now F k = 1 5 ​ ( φ k − ψ k) F_{k}=\frac{1}{\sqrt{5}}(\varphi^{k}-\psi^{k}), where ψ = 1 − 5 2 \psi=\frac{1-\sqrt{5}}{2}, − 1 < ψ < 0 -1<\psi<0. So

 | n = ∑ 1 ≤ i ≤ l F m i = 1 5 ​ ( ∑ 1 ≤ i ≤ l φ m i − ∑ 1 ≤ i ≤ l ψ m i) n=\sum_{1\leq i\leq l}F_{m_{i}}=\frac{1}{\sqrt{5}}\left(\sum_{1\leq i\leq l}\varphi^{m_{i}}-\sum_{1\leq i\leq l}\psi^{m_{i}}\right) |  |

and

 | n ′ = ∑ 1 ≤ i ≤ l F m i + 1 = 1 5 ​ ( ∑ 1 ≤ i ≤ l φ m i + 1 − ∑ 1 ≤ i ≤ l ψ m i + 1), n^{\prime}=\sum_{1\leq i\leq l}F_{m_{i}+1}=\frac{1}{\sqrt{5}}\left(\sum_{1\leq i\leq l}\varphi^{m_{i}+1}-\sum_{1\leq i\leq l}\psi^{m_{i}+1}\right), |  |

implying that

 | n ′ φ = 1 5 ​ ( ∑ 1 ≤ i ≤ l φ m i − 1 φ ​ ∑ 1 ≤ i ≤ l ψ m i + 1). \frac{n^{\prime}}{\varphi}=\frac{1}{\sqrt{5}}\left(\sum_{1\leq i\leq l}\varphi^{m_{i}}-\frac{1}{\varphi}\sum_{1\leq i\leq l}\psi^{m_{i}+1}\right). |  |

The difference between the two values is

 | n ′ φ − n = 1 5 ​ ( 1 − ψ φ) ​ S, \frac{n^{\prime}}{\varphi}-n=\frac{1}{\sqrt{5}}\left(1-\frac{\psi}{\varphi}\right)S, |  |

where

 | S = ∑ 1 ≤ i ≤ l ψ m i = ψ m 1 ​ ∑ 1 ≤ i ≤ l ψ m i − m 1. S=\sum_{1\leq i\leq l}\psi^{m_{i}}=\psi^{m_{1}}\sum_{1\leq i\leq l}\psi^{m_{i}-m_{1}}. |  |

Let us estimate S S. Since m 1 ≥ 2 m_{1}\geq 2, m 1 m_{1} is even and 0 < ψ m 1 < ψ 2 0<\psi^{m_{1}}<\psi^{2}, an upper bound for S S is

 | S < ψ m 1 ​ ∑ k = 0 ∞ ψ 2 ​ k = ψ m 1 1 − ψ 2 ≤ ψ 2 1 − ψ 2, S<\psi^{m_{1}}\sum_{k=0}^{\infty}\psi^{2k}=\frac{\psi^{m_{1}}}{1-\psi^{2}}\leq\frac{\psi^{2}}{1-\psi^{2}}, |  |

whereas a lower bound is

 | S > ψ m 1 ​ ( 1 + ∑ k = 1 ∞ ψ 2 ​ k + 1) > ψ m 1 ​ ( 1 + ∑ k = 0 ∞ ψ 2 ​ k + 1) = ψ m 1 ​ ( 1 + ψ 1 − ψ 2) = 0. S>\psi^{m_{1}}\left(1+\sum_{k=1}^{\infty}\psi^{2k+1}\right)>\psi^{m_{1}}\left(1+\sum_{k=0}^{\infty}\psi^{2k+1}\right)=\psi^{m_{1}}\left(1+\frac{\psi}{1-\psi^{2}}\right)=0. |  |

So

 | 0 < n ′ φ − n < ψ 2 5 ​ ( 1 − ψ φ) ​ 1 1 − ψ 2 = 1 φ 2. 0<\frac{n^{\prime}}{\varphi}-n<\frac{\psi^{2}}{\sqrt{5}}\left(1-\frac{\psi}{\varphi}\right)\frac{1}{1-\psi^{2}}=\frac{1}{\varphi^{2}}. |  |

Dividing by φ 2 \varphi^{2}, we get

 | 0 < n ′ φ 3 − n φ 2 < 1 φ 4 < 1 φ 2. 0<\frac{n^{\prime}}{\varphi^{3}}-\frac{n}{\varphi^{2}}<\frac{1}{\varphi^{4}}<\frac{1}{\varphi^{2}}. |  |

Together with ( 5), meaning that { n / φ 2 } < 1 − 1 / φ 2 \{n/\varphi^{2}\}<1-1/\varphi^{2}, the last inequality implies the statement of the Proposition. ∎

###### Proof of Theorem 1.

Let us start with the case of 𝐟 ⁡ [n] = a {\bf f}[n]=a and proceed by induction starting with V ⁡ ( 1) = 1 V(1)=1. For n > 1 n>1, there are three subcases:

- (a)

n = [z ​ 10 2 ​ k] F n=[z10^{2k}]_{F}, k > 0 k>0;

- (b)

n = [z ​ 10 k ​ 1] F n=[z10^{k}1]_{F}, k k odd;

- (c)

n = [z ​ 10 k ​ 1] F n=[z10^{k}1]_{F}, k k even.

From now on we suppose that the statement of the theorem holds for all n ′, n ′′ < n n^{\prime},n^{\prime\prime}<n.

(a) Since n = [z ​ 10 2 ​ k] F n=[z10^{2k}]_{F} and k > 0 k>0, Proposition 3 gives V ⁡ ( n) = V ⁡ ( [z ​ 10 2 ​ k] F) = V ⁡ ( [z ​ 10 2 ​ k − 2] F) + V ⁡ ( [z ​ ( 01) k] F) V(n)=V([z10^{2k}]_{F})=V([z10^{2k-2}]_{F})+V([z(01)^{k}]_{F}). Write [z ​ 10 2 ​ k − 2] F = n ′ [z10^{2k-2}]_{F}=n^{\prime} and [z ​ ( 01) k] F = n ′′ [z(01)^{k}]_{F}=n^{\prime\prime}. Note that Proposition 1 gives 𝐟 ⁡ [n ′] = 𝐟 ⁡ [n ′′] = a {\bf f}[n^{\prime}]={\bf f}[n^{\prime\prime}]=a. At the same time, n ′′ + 1 = [z ​ 10 2 ​ k − 1] F n^{\prime\prime}+1=[z10^{2k-1}]_{F} and thus 𝐟 ⁡ [n ′′ + 1] = b {\bf f}[n^{\prime\prime}+1]=b. Now ( 5) implies that { n ′ / φ 2 } ∈ ( 0, 1 − 1 / φ 2) \{n^{\prime}/\varphi^{2}\}\in(0,1-1/\varphi^{2}) and { ( n ′′ + 1) / φ 2 } ∈ ( 1 − 1 / φ 2, 1) \{(n^{\prime\prime}+1)/\varphi^{2}\}\in(1-1/\varphi^{2},1). Also, the Fibonacci representation of n ′ n^{\prime} is obtained from that of n ′′ + 1 n^{\prime\prime}+1 by a one-symbol shift to the left. So, summing up n ′ n^{\prime} and n ′′ + 1 n^{\prime\prime}+1, due to the Fibonacci recurrence relation, we get the number with the same representation but shifted to the left yet another position, meaning that n ′ + n ′′ + 1 = n n^{\prime}+n^{\prime\prime}+1=n.

Let us consider the sum t = { n ′ / φ 2 } + { ( n ′′ + 1) / φ 2 } t=\{n^{\prime}/\varphi^{2}\}+\{(n^{\prime\prime}+1)/\varphi^{2}\}. From the inclusions above, we see that t t belongs to the interval ( 1 − 1 / φ 2, 2 − 1 / φ 2) (1-1/\varphi^{2},2-1/\varphi^{2}). But we also know that { n / φ 2 } = { ( n ′ + n ′′ + 1) / φ 2 } ∈ ( 0, 1 − 1 / φ 2) \{n/\varphi^{2}\}=\{(n^{\prime}+n^{\prime\prime}+1)/\varphi^{2}\}\in(0,1-1/\varphi^{2}), since 𝐟 ⁡ [n] = a {\bf f}[n]=a. So

 | { n / φ 2 } = { n ′ / φ 2 } + { ( n ′′ + 1) / φ 2 } − 1, \{n/\varphi^{2}\}=\{n^{\prime}/\varphi^{2}\}+\{(n^{\prime\prime}+1)/\varphi^{2}\}-1, |  |

which is equivalent to ⌊ n / φ 2 ⌋ = ⌊ n ′ / φ 2 ⌋ + ⌊ ( n ′′ + 1) / φ 2 ⌋ + 1 \lfloor n/\varphi^{2}\rfloor=\lfloor n^{\prime}/\varphi^{2}\rfloor+\lfloor(n^{\prime\prime}+1)/\varphi^{2}\rfloor+1 and to ⌊ n / φ 2 ⌋ = ⌊ n ′ / φ 2 ⌋ + ⌊ n ′′ / φ 2 ⌋ + 1 \lfloor n/\varphi^{2}\rfloor=\lfloor n^{\prime}/\varphi^{2}\rfloor+\lfloor n^{\prime\prime}/\varphi^{2}\rfloor+1 (since ⌊ n ′′ / φ 2 ⌋ = ⌊ ( n ′′ + 1) / φ 2 ⌋ \lfloor n^{\prime\prime}/\varphi^{2}\rfloor=\lfloor(n^{\prime\prime}+1)/\varphi^{2}\rfloor). Since all the numbers under consideration are irrational, and thus every ceiling is just the floor plus 1, we get

 | ⌈ n / φ 2 ⌉ = ⌈ n ′ / φ 2 ⌉ + ⌈ n ′′ / φ 2 ⌉. \lceil n/\varphi^{2}\rceil=\lceil n^{\prime}/\varphi^{2}\rceil+\lceil n^{\prime\prime}/\varphi^{2}\rceil. |  |

To establish the statement of the theorem for this subcase, it is sufficient to use Proposition 3 and the induction hypothesis: V ⁡ ( n ′) = ⌈ n ′ / φ 2 ⌉ V(n^{\prime})=\lceil n^{\prime}/\varphi^{2}\rceil and V ⁡ ( n ′′) = ⌈ n ′′ / φ 2 ⌉ V(n^{\prime\prime})=\lceil n^{\prime\prime}/\varphi^{2}\rceil.

(b): Here n = [z ​ 10 2 ​ k − 1 ​ 1] F n=[z10^{2k-1}1]_{F} and k > 0 k>0. It suffices to refer to the previous subcase and to Proposition 4: V ⁡ ( n) = V ⁡ ( n − 1) = V ⁡ ( [z ​ 10 2 ​ k] F) = ⌈ ( n − 1) / φ 2 ⌉ V(n)=V(n-1)=V([z10^{2k}]_{F})=\lceil(n-1)/\varphi^{2}\rceil. It remains to notice that ⌈ ( n − 1) / φ 2 ⌉ = ⌈ n / φ 2 ⌉ \lceil(n-1)/\varphi^{2}\rceil=\lceil n/\varphi^{2}\rceil, since 𝐟 ⁡ [n − 1] = a {\bf f}[n-1]=a.

(c): Here n = [z ​ 10 2 ​ k ​ 1] F n=[z10^{2k}1]_{F} and k > 0 k>0. We use Proposition 4: V ⁡ ( [z ​ 10 2 ​ k ​ 1] F) = V ⁡ ( [z ​ 10 2 ​ k] F) + V ⁡ ( [z ​ ( 01) k] F) V([z10^{2k}1]_{F})=V([z10^{2k}]_{F})+V([z(01)^{k}]_{F}). As above, write n ′ = [z ​ 10 2 ​ k] F n^{\prime}=[z10^{2k}]_{F} and n ′′ = [z ​ ( 01) k] F n^{\prime\prime}=[z(01)^{k}]_{F}; then n = n ′ + n ′′ + 2 n=n^{\prime}+n^{\prime\prime}+2, whereas V ⁡ ( n) = V ⁡ ( n ′) + V ⁡ ( n ′′) V(n)=V(n^{\prime})+V(n^{\prime\prime}). By the induction hypothesis, V ⁡ ( n ′) = ⌈ n ′ / φ 2 ⌉ V(n^{\prime})=\lceil n^{\prime}/\varphi^{2}\rceil and V ⁡ ( n ′′) = ⌈ n ′′ / φ 2 ⌉ V(n^{\prime\prime})=\lceil n^{\prime\prime}/\varphi^{2}\rceil.

We have 𝐟 ⁡ [n] = a {\bf f}[n]=a and 𝐟 ⁡ [n − 1] = b {\bf f}[n-1]=b, implying from ( 5) that { ( n − 1) / φ 2 } ∈ ( 1 − 1 / φ 2, 1) \{(n-1)/\varphi^{2}\}\in(1-1/\varphi^{2},1) and thus { n / φ 2 } ∈ ( 0, 1 / φ 2) \{n/\varphi^{2}\}\in(0,1/\varphi^{2}). At the same time, 𝐟 ⁡ [n ′] = 𝐟 ⁡ [n ′′] = a {\bf f}[n^{\prime}]={\bf f}[n^{\prime\prime}]=a implies { n ′ / φ 2 }, { n ′′ / φ 2 } ∈ ( 0, 1 − 1 / φ 2) \{n^{\prime}/\varphi^{2}\},\{n^{\prime\prime}/\varphi^{2}\}\in(0,1-1/\varphi^{2}) and thus

 | { n ′ / φ 2 } + { n ′′ / φ 2 } + { 2 / φ 2 } ∈ ( 2 / φ 2, 2). \{n^{\prime}/\varphi^{2}\}+\{n^{\prime\prime}/\varphi^{2}\}+\{2/\varphi^{2}\}\in(2/\varphi^{2},2). |  |

Comparing it to { n / φ 2 } = { ( n ′ + n ′′ + 2) / φ 2 } ∈ ( 0, 1 / φ 2) \{n/\varphi^{2}\}=\{(n^{\prime}+n^{\prime\prime}+2)/\varphi^{2}\}\in(0,1/\varphi^{2}), we see that

 | { n / φ 2 } = { n ′ / φ 2 } + { n ′′ / φ 2 } + { 2 / φ 2 } − 1. \{n/\varphi^{2}\}=\{n^{\prime}/\varphi^{2}\}+\{n^{\prime\prime}/\varphi^{2}\}+\{2/\varphi^{2}\}-1. |  |

But since n = n ′ + n ′′ + 2 n=n^{\prime}+n^{\prime\prime}+2 and x = ⌊ x ⌋ + { x } x=\lfloor x\rfloor+\{x\} for every x x, this also means that

 | ⌊ n / φ 2 ⌋ = ⌊ n ′ / φ 2 ⌋ + ⌊ n ′′ / φ 2 ⌋ + 1. \lfloor n/\varphi^{2}\rfloor=\lfloor n^{\prime}/\varphi^{2}\rfloor+\lfloor n^{\prime\prime}/\varphi^{2}\rfloor+1. |  |

Finally, since k / φ 2 k/\varphi^{2} is not an integer for any integer k > 0 k>0, we have ⌈ k / φ 2 ⌉ = ⌊ k / φ 2 ⌋ + 1 \lceil k/\varphi^{2}\rceil=\lfloor k/\varphi^{2}\rfloor+1, so that

 | ⌈ n / φ 2 ⌉ = ⌈ n ′ / φ 2 ⌉ + ⌈ n ′′ / φ 2 ⌉. \lceil n/\varphi^{2}\rceil=\lceil n^{\prime}/\varphi^{2}\rceil+\lceil n^{\prime\prime}/\varphi^{2}\rceil. |  |

It remains to use the induction hypothesis to establish

 | V ⁡ ( n) = V ⁡ ( n ′) + V ⁡ ( n ′′) = ⌈ n ′ / φ 2 ⌉ + ⌈ n ′′ / φ 2 ⌉ = ⌈ n / φ 2 ⌉, V(n)=V(n^{\prime})+V(n^{\prime\prime})=\lceil n^{\prime}/\varphi^{2}\rceil+\lceil n^{\prime\prime}/\varphi^{2}\rceil=\lceil n/\varphi^{2}\rceil, |  |

which was to be proved.

To complete the part of the proof concerning 𝐟 ⁡ [n] = a {\bf f}[n]=a, it remains to notice that ⌈ n / φ 2 ⌉ \lceil n/\varphi^{2}\rceil is equal to the number of b b s in 𝐟 ( 0.. n] {\bf f}(0..n] plus one, due to ( 5).

Now for 𝐟 ⁡ [n] = b {\bf f}[n]=b, it is sufficient to combine Propositions 1, 2 and 5: if 𝐟 ⁡ [n] = b {\bf f}[n]=b, then n = [r ​ 0] F n=[r0]_{F}, where m = [r] F m=[r]_{F} and 𝐟 ⁡ [m] = a {\bf f}[m]=a. Then

 | V ⁡ ( n) = V ⁡ ( m) = ⌈ m / φ 2 ⌉ = ⌈ n / φ 3 ⌉. V(n)=V(m)=\lceil m/\varphi^{2}\rceil=\lceil n/\varphi^{3}\rceil. |  |

Here 𝐟 ( 0.. n] = μ ( 𝐟 ( 0.. m]) {\bf f}(0..n]=\mu({\bf f}(0..m]), and so the occurrences of a ​ a aa in 𝐟 ( 0.. n] {\bf f}(0..n] correspond exactly to occurrences of b b in μ ( 𝐟 ( 0.. m]) \mu({\bf f}(0..m]). The theorem is proved. ∎

The theorem ensures that the sequence ( V ⁡ ( n)) (V(n)) grows as depicted in Fig. 1. The two visible straight lines correspond to the symbols of the Fibonacci word equal to a a (the upper line) or b b (the lower line).

## 4 Fibonacci-regular representation

A sequence ( s ⁡ ( n)) n ≥ 0 (s(n))_{n\geq 0} is said to be Fibonacci-regular if there exist an integer k k, a row vector v v of dimension k k, a column vector w w of dimension k k, and a k × k k\times k matrix-valued morphism ρ \rho on { 0, 1 } ∗ \{0,1\}^{*} such that

 | s ⁡ ( [z] F) = v ​ ρ ​ ( z) ​ w s([z]_{F})=v\rho(z)w |  |

for all canonical Fibonacci representations z ∈ L V z\in L_{V}. The triple ( v, ρ, w) (v,\rho,w) is called a linear representation; see, for example, [7].

Berstel [2] gave the following linear representation for the function L ⁡ ( n) L(n) we mentioned previously in Section 2:

 | v = [1 0 0 0], ρ ⁡ ( 0) = [1 0 0 0 0 0 1 0 1 1 0 0 1 0 0 0], ρ ⁡ ( 1) = [0 1 0 1 0 0 0 0 0 1 0 0 0 0 0 0], w = [1 0 0 1]. v=[1\ 0\ 0\ 0],\quad\rho(0)=\left[\begin{array}[]{cccc}1&0&0&0\\ 0&0&1&0\\ 1&1&0&0\\ 1&0&0&0\end{array}\right],\quad\rho(1)=\left[\begin{array}[]{cccc}0&1&0&1\\ 0&0&0&0\\ 0&1&0&0\\ 0&0&0&0\end{array}\right],\quad w=\left[\begin{array}[]{c}1\\ 0\\ 0\\ 1\end{array}\right]. |  |

Hence L ⁡ ( n) L(n) is Fibonacci-regular.

We can find a similar representation for the function V ⁡ ( n) V(n). For technical reasons it is easier to deal with the reversed Fibonacci representation; one can then obtain the ordinary linear representation by interchanging the roles of the vectors and taking the transposes of the matrices.

###### Theorem 2.

V ⁡ ( n) V(n) has the reversed linear representation ( t, γ, u) (t,\gamma,u), where

 | t \displaystyle t | = [1 0 0 0 0 0 0 0], \displaystyle=[1\ 0\ 0\ 0\ 0\ 0\ 0\ 0],\quad | u \displaystyle u | = [1 1 1 1 1 2 1 4] T \displaystyle=[1\ 1\ 1\ 1\ 1\ 2\ 1\ 4]^{T} |  |

 | γ ⁡ ( 0) \displaystyle\gamma(0) | = [0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 − 1 1 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 − 1 0 0 2 1 0 0 0 1 − 1 0 − 3 3 0 1 0 − 1 − 1 0 2 3 0 1 0], \displaystyle=\left[\begin{array}[]{rrrrrrrr}0&1&0&0&0&0&0&0\\ 0&0&0&1&0&0&0&0\\ -1&1&0&1&0&0&0&0\\ 0&0&0&0&1&0&0&0\\ 0&0&0&0&0&0&1&0\\ -1&0&0&2&1&0&0&0\\ 1&-1&0&-3&3&0&1&0\\ -1&-1&0&2&3&0&1&0\\ \end{array}\right], | γ ⁡ ( 1) \displaystyle\gamma(1) | = [0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0]. \displaystyle=\left[\begin{array}[]{cccccccc}0&0&1&0&0&0&0&0\\ 0&0&1&0&0&0&0&0\\ 0&0&0&0&0&0&0&0\\ 0&0&0&0&0&1&0&0\\ 0&0&0&0&0&1&0&0\\ 0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&1\\ 0&0&0&0&0&0&0&0\\ \end{array}\right]. |  |

###### Proof.

Define g ⁡ ( x) = V ⁡ ( [x] F) g(x)=V([x]_{F}) if x x is a valid canonical representation (that is, containing no leading zeroes, and no two consecutive 1’s), and 0 0 otherwise. It suffices to show, for all x ∈ { 0, 1 } ∗ x\in\{0,1\}^{*} and i ∈ { 0, 1 } i\in\{0,1\}, that

 | [g ⁡ ( x ​ i) g ⁡ ( x ​ i ​ 0) g ⁡ ( x ​ i ​ 1) g ⁡ ( x ​ i ​ 00) g ⁡ ( x ​ i ​ 000) g ⁡ ( x ​ i ​ 100) g ⁡ ( x ​ i ​ 0000) g ⁡ ( x ​ i ​ 10000)] = γ ⁡ ( i) ​ [g ⁡ ( x) g ⁡ ( x ​ 0) g ⁡ ( x ​ 1) g ⁡ ( x ​ 00) g ⁡ ( x ​ 000) g ⁡ ( x ​ 100) g ⁡ ( x ​ 0000) g ⁡ ( x ​ 10000)]. \left[\begin{array}[]{c}g(xi)\\ g(xi0)\\ g(xi1)\\ g(xi00)\\ g(xi000)\\ g(xi100)\\ g(xi0000)\\ g(xi10000)\end{array}\right]=\gamma(i)\left[\begin{array}[]{c}g(x)\\ g(x0)\\ g(x1)\\ g(x00)\\ g(x000)\\ g(x100)\\ g(x0000)\\ g(x10000)\end{array}\right]. |  | (6) |

Once we prove this, it is then easy to see (using induction on | z | |z|) that, if z z is the Fibonacci representation of n n, then t ​ γ ​ ( z R) ​ u = V ⁡ ( n) t\gamma(z^{R})u=V(n), where z R z^{R} is the reversal of z z.

Thus it suffices to verify Eq. ( 6). This is equivalent to proving the following identities for x x.

 | g ⁡ ( x ​ 01) \displaystyle g(x01) | = − g ⁡ ( x) + g ⁡ ( x ​ 0) + g ⁡ ( x ​ 00) \displaystyle=-g(x)+g(x0)+g(x00) |  | (7) |

 | g ⁡ ( x ​ 10) \displaystyle g(x10) | = g ⁡ ( x ​ 1) \displaystyle=g(x1) |  | (8) |

 | g ⁡ ( x ​ 0100) \displaystyle g(x0100) | = − g ⁡ ( x) + 2 ​ g ​ ( x ​ 00) + g ⁡ ( x ​ 000) \displaystyle=-g(x)+2g(x00)+g(x000) |  | (9) |

 | g ⁡ ( x ​ 1000) \displaystyle g(x1000) | = g ⁡ ( x ​ 100) \displaystyle=g(x100) |  | (10) |

 | g ⁡ ( x ​ 010000) \displaystyle g(x010000) | = − g ⁡ ( x) − g ⁡ ( x ​ 0) + 2 ​ g ​ ( x ​ 00) + 3 ​ g ​ ( x ​ 000) + g ⁡ ( x ​ 0000) \displaystyle=-g(x)-g(x0)+2g(x00)+3g(x000)+g(x0000) |  | (11) |

 | g ⁡ ( x ​ 00000) \displaystyle g(x00000) | = g ⁡ ( x) − g ⁡ ( x ​ 0) − 3 ​ g ​ ( x ​ 00) + 3 ​ g ​ ( x ​ 000) + g ⁡ ( x ​ 0000). \displaystyle=g(x)-g(x0)-3g(x00)+3g(x000)+g(x0000). |  | (12) |

Identities ( 8) and ( 10) are particular cases of Proposition 2 (b).

To prove ( 7), consider separately two cases: if x x ends with an even number of zeros, then g ⁡ ( x) = g ⁡ ( x ​ 0) g(x)=g(x0) due to Proposition 2 (b) and g ⁡ ( x ​ 00) = g ⁡ ( x ​ 01) g(x00)=g(x01) due to Proposition 4, so the identity holds. If x x ends with an odd number of zeros, x = z ​ 10 2 ​ k + 1 x=z10^{2k+1}, k ≥ 0 k\geq 0, then due to Proposition 4,

 | g ⁡ ( x ​ 01) = g ⁡ ( z ​ 10 2 ​ k + 2 ​ 1) = g ⁡ ( z ​ 10 2 ​ k + 2) + g ⁡ ( z ​ ( 01) k + 1) = g ⁡ ( x ​ 0) + g ⁡ ( z ​ ( 01) k + 1). g(x01)=g(z10^{2k+2}1)=g(z10^{2k+2})+g(z(01)^{k+1})=g(x0)+g(z(01)^{k+1}). |  |

On the other hand, due to Propositions 2 and 3,

 | g ⁡ ( x ​ 00) = g ⁡ ( x ​ 0) = g ⁡ ( z ​ 10 2 ​ k + 2) = g ⁡ ( z ​ 10 2 ​ k) + g ⁡ ( z ​ ( 01) k + 1) = g ⁡ ( x) + g ⁡ ( z ​ ( 01) k + 1). g(x00)=g(x0)=g(z10^{2k+2})=g(z10^{2k})+g(z(01)^{k+1})=g(x)+g(z(01)^{k+1}). |  |

Comparing these equalities, we get ( 7).

To prove ( 9), it is sufficient to use Proposition 3 to get

 | g ⁡ ( x ​ 0100) = g ⁡ ( x ​ 01) + g ⁡ ( x ​ 001), g(x0100)=g(x01)+g(x001), |  |

and then to use ( 7) twice, for g ⁡ ( x ​ 01) g(x01) and for g ⁡ ( x ​ 001) g(x001).

To prove ( 11), it is sufficient to use Propositions 3 and 2 to get

 | g ⁡ ( x ​ 010000) = g ⁡ ( x ​ 0100) + g ⁡ ( x ​ 00101) = g ⁡ ( x ​ 0100) + g ⁡ ( x ​ 00100). g(x010000)=g(x0100)+g(x00101)=g(x0100)+g(x00100). |  |

Now ( 11) is obtained immediately by summing up ( 9) applied to x x and to x ​ 0 x0.

Finally, to prove ( 12), we again have to consider two cases. If x = z ​ 10 2 ​ k x=z10^{2k}, k ≥ 0 k\geq 0, then due to Proposition 2, g ⁡ ( x ​ 0 5) = g ⁡ ( x ​ 0000) g(x0^{5})=g(x0000), g ⁡ ( x ​ 000) = g ⁡ ( x ​ 00) g(x000)=g(x00), g ⁡ ( x ​ 0) = g ⁡ ( x) g(x0)=g(x), and the equality holds. If now x = z ​ 10 2 ​ k + 1 x=z10^{2k+1}, k ≥ 0 k\geq 0, then ( 12) immediately simplifies with Proposition 2 as

 | g ⁡ ( z ​ 10 2 ​ k + 6) − g ⁡ ( z ​ 10 2 ​ k + 4) = 3 ​ [g ⁡ ( z ​ 10 2 ​ k + 4) − g ⁡ ( z ​ 10 2 ​ k + 2)] − [g ⁡ ( z ​ 10 2 ​ k + 2) − g ⁡ ( z ​ 10 2 ​ k)]. g(z10^{2k+6})-g(z10^{2k+4})=3[g(z10^{2k+4})-g(z10^{2k+2})]-[g(z10^{2k+2})-g(z10^{2k})]. |  |

Applying Proposition 3, we reduce it to

 | g ⁡ ( z ​ ( 01) k + 3) = 3 ​ g ​ ( z ​ ( 01) k + 2) − g ⁡ ( z ​ ( 01) k + 1), g(z(01)^{k+3})=3g(z(01)^{k+2})-g(z(01)^{k+1}), |  |

or, writing y = z ​ ( 01) k + 1 y=z(01)^{k+1} and applying Proposition 4 again,

 | g ⁡ ( y ​ 0100) = 3 ​ g ​ ( y ​ 00) − g ⁡ ( y). g(y0100)=3g(y00)-g(y). |  |

But this is exactly ( 9) since g ⁡ ( y ​ 00) = g ⁡ ( y ​ 000) g(y00)=g(y000).

∎

## References

## References

- [1] J.-P. Allouche and J. Shallit. Automatic Sequences: Theory, Applications, Generalizations. Cambridge University Press, 2003.
- [2] J. Berstel. An exercise on Fibonacci representations. Theor. Inform. Appl. 35 (2001) 491–498.
- [3] J. Berstel and P. Séébold. Sturmian words. In: M. Lothaire, Algebraic Combinatorics on Words. Cambridge University Press, 2002. Chapter 2, pp. 45–110.
- [4] A. E. Frid, Sturmian numeration systems and decompositions to palindromes. European J. Combin. 71 (2018) 202–212.
- [5] J. Karhumäki, On cube-free ω \omega -words generated by binary morphisms. Discr. Appl. Math. 5 (1983), 279–297.
- [6] C. G. Lekkerkerker. Voorstelling van natuurlijke getallen door een som van getallen van Fibonacci. Simon Stevin 29 (1952) 190–195.
- [7] Hamoon Mousavi, Luke Schaeffer, and Jeffrey Shallit. Decision algorithms for Fibonacci-automatic words, I: Basic results. RAIRO Inform. Théorique 51 (2016), 39–66.
- [8] N. J. A. Sloane et al. The On-Line Encyclopedia of Integer Sequences. Available at [https://oeis.org][7].
- [9] A. Ostrowski. Bemerkungen zur Theorie der diophantischen Approximationen. Hamb. Abh. 1 (1921) 77–98.
- [10] P. K. Stockmeyer, A smooth tight upper bound for the Fibonacci representation function R ⁡ ( N) R(N), Fibonacci Quart. 46/47 (2) (2009), 103–106.
- [11] E. Zeckendorf. Représentation des nombres naturels par une somme de nombres de Fibonacci ou de nombres de Lucas. Bull. Soc. Roy. Sci. Liège 41 (1972) 179–182.

[◄][8][image: ar5iv homepage] [9]
[Feeling lucky?][10] [11]
[Conversion report][12]
[Report an issue][13]
[View original on arXiv][14] [►][15]


## Links

[1]: mailto:anna.e.frid@gmail.com
[2]: http://iml.univ-mrs.fr/%CB%9Cfrid/
[3]: mailto:shallit@uwaterloo.ca
[4]: https://cs.uwaterloo.ca/%CB%9Cshallit/
[5]: http://oeis.org/A000119
[6]: http://oeis.org/A300066
[7]: https://oeis.org
[8]: /html/1806.09533
[9]: /
[10]: /feeling_lucky
[11]: /land_of_honey_and_milk
[12]: /log/1806.09534
[13]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1806.09534
[14]: https://arxiv.org/pdf/1806.09534
[15]: /html/1806.09536
