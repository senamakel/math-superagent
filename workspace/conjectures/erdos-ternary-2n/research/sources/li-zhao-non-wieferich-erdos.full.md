<!-- source: https://arxiv.org/html/2601.12753 | converted from HTML -->

Non-Wieferich property of prime ideals and a conjecture of Erdös

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2601.12753v1 [math.NT] 19 Jan 2026

# Non-Wieferich property of prime ideals and a conjecture of Erdös Thanks: ∗ Corresponding author.

Ruofan Li Address: Department of Mathematics, Jinan University, Guangzhou, 510632, China Email address: [liruofan@jnu.edu.cn][3] and Jiuzhou Zhao ∗ Address: School of Mathematics and Statistics, Key Laboratory of Engineering Modeling and Statistical Computation of Hainan Province, Hainan University, Haikou 570228, China Email address: [zhao9zone@gmail.com][4]

###### Abstract.

Let K K be a number field with ring of integers 𝒪 \mathcal{O} and α ∈ 𝒪 \alpha\in\mathcal{O}. For any prime ideal 𝔭 \mathfrak{p} of 𝒪 \mathcal{O}, we obtain its higher α \alpha -Wieferich property, which implies a nonexistence theorem for higher Wieferich unramified prime ideals. If β ∈ 𝒪 \beta\in\mathcal{O} is relatively prime to α \alpha and all prime ideal factors of ( β) (\beta) are unramified and have residue degree 1 1, we apply our higher α \alpha -Wieferich property to establish the asymptotic equidistribution of digits in β \beta -adic expansions of α n \alpha^{n}, which is a generalization of the Dupuy-Weirich theorem. When ( β) (\beta) have ramified prime ideal factors, we also obtain a result on the block complexity of β \beta -adic expansions of α n \alpha^{n}.

###### Key words and phrases:

Radix representation, Digital problems, Wieferich primes

###### 2020 Mathematics Subject Classification

11A63,11A41

## 1. Introduction

### 1.1. A conjecture of Erdös and Dupuy-Weirich theorem

For positive integers m m and q q, if

 | m = ∑ i = 0 k a i ​ q i m=\sum_{i=0}^{k}a_{i}q^{i} |  |

for some integers a i a_{i} between 0 0 and q − 1 q-1, then we write ( m) q = a k ⋯ a 0 (m)_{q}=a_{k}\cdots a_{0} and call it the q q -ary expansion of m m. An interesting fact is that, other than ( 2 0) 3 = 1 (2^{0})_{3}=1, ( 2 2) 3 = 11 (2^{2})_{3}=11 and ( 2 8) 3 = 100111 (2^{8})_{3}=100111, no other values of n such that ( 2 n) 3 (2^{n})_{3} omits the digit 2 2 is known. In [4], Erdös proposed the following conjecture:

###### Conjecture 1.1.

There are only finitely many powers of 2 2 whose ternary expansion omits the digit 2 2.

Most progress towards Conjecture 1.1 has been in the form of upper bounds on

 | M ⁡ ( N):= #⁡ { n ∈ ℤ ∩ [1, N]: ( 2 n) 3 ​ omits the digit 2 }, M(N):=\#\{n\in\mathbb{Z}\cap[1,N]\colon(2^{n})_{3}\text{ omits the digit $2$}\}, |  |

where the symbol #\#denote cardinality. The best known bound on M ⁡ ( N) M(N) is due to Narkiewicz [11] who proved that

(1.1) |  | M ( N) ≤ 1.62 N σ, where σ:= log 3 ⁡ 2 ≈ 0.63092. M(N)\leq 1.62N^{\sigma},\quad\text{ where $\sigma:=\log_{3}2\approx 0.63092$. } |  |

We refer the reader to [3, 6, 8, 9, 15] for more results related to Narkiewicz’s result. Recently, Dimitrov and Howe [2, Theorem 1.2] have demonstrated that if n ∉ { 0, 2, 8 } n\notin\{0,2,8\}, then the ternary expansion of 2 n 2^{n} either contains the digit 2 2 or includes at least twenty-six 1 1 ’s.

Based on computer experiments, Dupuy and Weirich [3] believe that a stronger version of Conjecture 1.1 holds.

###### Conjecture 1.2.

Let p p and q q be distinct primes and b ∈ { 0, 1, …, q − 1 } b\in\{0,1,\dots,q-1\}. Denote by d n ​ ( b) d_{n}(b) the number of b b ’s appearing in ( p n) q (p^{n})_{q}. Then

(1.2) |  | lim n → ∞ d n ​ ( b) n ​ log q ​ ( p) = 1 q \lim_{n\to\infty}\frac{d_{n}(b)}{n\log_{q}(p)}=\frac{1}{q} |  |

###### Remark 1.1.

(i) Note that the denominator n ​ log q ​ ( p) n\log_{q}(p) in ( 1.2) is the length of the q q -ary expansion of p n p^{n}, this limit means that the proportion of digits b b ’s in ( p n) q (p^{n})_{q} tends to 1 / q 1/q as n → ∞ n\to\infty.
(ii) Take p = 2 p=2 and q = 3 q=3, ( 1.2) implies that d n ​ ( 2) > 0 d_{n}(2)>0 for n n large enough, which implies Conjecture 1.1.

The following theorem is the first progress on Conjecture 1.2, which considers the average proportion of b b ’s in ( p n) q (p^{n})_{q}. Given the q q -ary expansion

 | p n = a 0 + a 1 ​ q + ⋯ + a N ​ q N, p^{n}=a_{0}+a_{1}q+\cdots+a_{N}q^{N}, |  |

where N = ⌊ log q ⁡ ( p n) ⌋ N=\lfloor\log_{q}(p^{n})\rfloor and a i ∈ { 0, 1, …, q − 1 } a_{i}\in\{0,1,\dots,q-1\}. Let ( p n) q, i:= a i (p^{n})_{q,i}:=a_{i}. Denote

 | f p, n, m ( b):= #⁡ { i ∈ ℤ ∩ [0, m − 1]: ( p n) q, i = b } m, f_{p,n,m}(b):=\frac{\#\{i\in\mathbb{Z}\cap[0,m-1]\colon(p^{n})_{q,i}=b\}}{m}, |  |

for b ∈ { 0, 1, …, q − 1 } b\in\{0,1,\dots,q-1\}. Let L m:= { p n + q m ​ ℤ: n ∈ ℤ } ⊂ ( ℤ / q m ​ ℤ) × L_{m}:=\{p^{n}+q^{m}\mathbb{Z}\colon n\in\mathbb{Z}\}\subset(\mathbb{Z}/q^{m}\mathbb{Z})^{\times} and l m:= #​ L m l_{m}:=\#L_{m}. It is clear that for each m ∈ ℤ ≥ 1 m\in\mathbb{Z}_{\geq 1}, the average proportion of b b ’s in the first m m digits satisfies

(1.3) |  | f p, m ​ ( b):= lim N → ∞ 1 N ​ ∑ n = 1 N f p, n, m ​ ( b) = 1 l m ​ ∑ n = 1 l m f p, n, m ​ ( b). f_{p,m}(b):=\lim_{N\to\infty}\frac{1}{N}\sum_{n=1}^{N}f_{p,n,m}(b)=\frac{1}{l_{m}}\sum_{n=1}^{l_{m}}f_{p,n,m}(b). |  |

###### Theorem (Dupuy and Weirich [3, Theorem 3]).

Let p p and q q be distinct primes and b ∈ { 0, 1, …, q − 1 } b\in\{0,1,\dots,q-1\}, then

 | lim m → ∞ f p, m ​ ( b) = 1 / q. \lim_{m\to\infty}f_{p,m}(b)=1/q. |  |

In this paper, we are going to generalize the above Dupuy-Weirich theorem to general number fields. For this purpose, we also generalize their work [3, Theorem 6] on Wieferich primes. It is worth mentioning that we have observed new phenomena in the setting of general number fields.

### 1.2. Wieferich primes

Let p p be a rational prime. For any k ∈ ℤ ≥ 1 k\in\mathbb{Z}_{\geq 1}, we denote

 | ⟨ 2 ⟩ p k:= { 2 n ( mod p k): n ∈ ℤ ≥ 1 } \langle 2\rangle_{p^{k}}:=\{2^{n}\!\!\pmod{p^{k}}\colon n\in\mathbb{Z}_{\geq 1}\} |  |

as the multiplicative group generated by 2 2 modulo p k p^{k}. The prime p p is called *(classical) Wieferich*if ⟨ 2 ⟩ p \langle 2\rangle_{p} is isomorphic to ⟨ 2 ⟩ p 2 \langle 2\rangle_{p^{2}}.

Such primes were initially investigated in [14] in relation to the Fermat’s Last Theorem. In that work, the author demonstrated that if x q + y q = z q x^{q}+y^{q}=z^{q} forms a Fermat triple, then q q must be a Wieferich prime. Whether there exist infinitely many Wieferich primes remains an open problem, even assuming the validity of the ABC conjecture. For an extensive discussion of Wieferich primes, we refer the reader to [1, 7, 10, 13].

From now on, fix a number field K K and let 𝒪 \mathcal{O} be its ring of integers.

###### Definition 1.1.

Let 𝔭 \mathfrak{p} be a prime ideal of the ring 𝒪 \mathcal{O}, r ∈ ℤ ≥ 1 r\in\mathbb{Z}_{\geq 1} and α ∈ 𝒪 \ 𝔭 \alpha\in\mathcal{O}\backslash\mathfrak{p}. We say that the prime ideal 𝔭 \mathfrak{p} is *α \alpha -Wieferich*at r r if the multiplicative group generated by α \alpha modulo 𝔭 r \mathfrak{p}^{r} is isomorphic to the multiplicative group generated by α \alpha modulo 𝔭 r − 1 \mathfrak{p}^{r-1}.

We now establish a higher α \alpha -Wieferich property of prime ideals when the integer r r is large enough. Let G k = ⟨ α ⟩ 𝔭 k = { α n ( mod 𝔭 k): n ∈ ℤ ≥ 1 } G_{k}=\langle\alpha\rangle_{\mathfrak{p}^{k}}=\{\alpha^{n}\!\!\pmod{\mathfrak{p}^{k}}\colon n\in\mathbb{Z}_{\geq 1}\} be the multiplicative group generated by α \alpha modulo 𝔭 k \mathfrak{p}^{k}. There is a natural homomorphism from G r G_{r} to G r − 1 G_{r-1}, and we denote the kernel of it by Ker ⁡ ( G r → G r − 1) \ke(G_{r}\to G_{r-1}). It is clear that 𝔭 \mathfrak{p} is α \alpha -Wieferich at r r if and only if #​ Ker ⁡ ( G r → G r − 1) = 1 \#\ke(G_{r}\to G_{r-1})=1.

###### Theorem 1.1.

Let 𝔭 \mathfrak{p} be a prime ideal of the ring 𝒪 \mathcal{O}. Assume that α ∈ 𝒪 \ 𝔭 \alpha\in\mathcal{O}\backslash\mathfrak{p} is not a root of unity, then there is a positive integer v v such that

 | #​ Ker ⁡ ( G r → G r − 1) = { 1, if ​ r − v ≢ 1 ( mod e) p, if ​ r − v ≡ 1 ( mod e) \#\ke(G_{r}\to G_{r-1})=\begin{cases}1,&\quad\text{ if }r-v\not\equiv 1\pmod{e}\\ p,&\quad\text{ if }r-v\equiv 1\pmod{e}\end{cases} |  |

holds for all r > v r>v, where e e is the ramification index of 𝔭 \mathfrak{p} and p p is the rational prime lying below 𝔭 \mathfrak{p}. In particular, if 𝔭 \mathfrak{p} is unramified, then 𝔭 \mathfrak{p} is not α \alpha -Wieferich at r r for all r > v r>v.

###### Remark 1.2.

The condition that α \alpha is not a root of unity is necessary. If α \alpha is a m m -th root of unity, then ⟨ α ⟩ = { α, α 2, …, α m = 1 } ⊆ 𝒪 \langle\alpha\rangle=\{\alpha,\alpha^{2},\dots,\alpha^{m}=1\}\subseteq\mathcal{O} is a finite set. Take

 | N = max { l ∈ ℤ ≥ 1: α i − α j ∈ 𝔭 l \ 𝔭 l + 1 for some i, j ∈ { 1, 2, …, m } }. N=\max\Big\{l\in\mathbb{Z}_{\geq 1}\colon\alpha^{i}-\alpha^{j}\in\mathfrak{p}^{l}\backslash\mathfrak{p}^{l+1}\text{ for some }i,j\in\{1,2,\dots,m\}\Big\}. |  |

For any r > N r>N, the multiplicative group generated by α \alpha modulo 𝔭 r \mathfrak{p}^{r} is isomorphic to { α, α 2, …, α m } \{\alpha,\alpha^{2},\dots,\alpha^{m}\}. Hence 𝔭 \mathfrak{p} is α \alpha -Wieferich at r r for all r > N + 1 r>N+1.

### 1.3. Asymptotic equidistribution of digits

Theorem 1.1 enables us to generalize the Dupuy-Weirich [3] theorem to general number fields.

We first recall the concept of *β \beta -adic expansions*, which is a natural generalization of q q -ary expansions. Denote N ⁡ ( β):= #⁡ ( 𝒪 / β ​ 𝒪) N(\beta):=\#(\mathcal{O}/\beta\mathcal{O}) for every nonzero β ∈ 𝒪 \beta\in\mathcal{O}.

###### Definition 1.2.

Fix β ∈ 𝒪 \beta\in\mathcal{O} with norm N ⁡ ( β) > 1 N(\beta)>1 and a set of representatives 𝒟 \mathcal{D} of the quotient group 𝒪 / β ​ 𝒪 \mathcal{O}/\beta\mathcal{O} with 0 ∈ 𝒟 0\in\mathcal{D}. For every x ∈ 𝒪 x\in\mathcal{O}, the *β \beta -adic expansion*of x x (with respect to 𝒟 \mathcal{D}) is the unique sequence ( b i) i ∈ ℕ ∈ 𝒟 ℕ (b_{i})_{i\in\mathbb{N}}\in\mathcal{D}^{\mathbb{N}} such that

(1.4) |  | x = lim i → ∞ b 0 + b 1 ​ β + ⋯ + b i ​ β i x=\lim_{i\rightarrow\infty}b_{0}+b_{1}\beta+\cdots+b_{i}\beta^{i} |  |

with respect to 𝔭 \mathfrak{p} -adic topology for any prime ideal 𝔭 \mathfrak{p} in 𝒪 \mathcal{O} dividing β \beta.

The existence and uniqueness of β \beta -adic expansions were proved in [15, Section 2].

We define the *i i -th digit function*( x) β, i:= b i (x)_{\beta,i}:=b_{i} for x ∈ 𝒪 x\in\mathcal{O} with x = ∑ i = 0 ∞ b i ​ β i x=\sum_{i=0}^{\infty}b_{i}\beta^{i}. Given an algebraic integer α ∈ 𝒪 \alpha\in\mathcal{O}, we denote the frequency of digit b ∈ 𝒟 b\in\mathcal{D} in the m m -truncated expansion of α n \alpha^{n} by

(1.5) |  | f α, n, m ( b):= #{ i: 0 ≤ i < m, ( α n) β, i = b } m. f_{\alpha,n,m}(b):=\frac{\#\{i\colon 0\leq i<m,\;(\alpha^{n})_{\beta,i}=b\}}{m}. |  |

Consider the Cesàro average 1 N ​ ∑ n = 1 N f α, n, m ​ ( b) \frac{1}{N}\sum_{n=1}^{N}f_{\alpha,n,m}(b), it is clear that

(1.6) |  | f α, m ​ ( b):= lim N → ∞ 1 N ​ ∑ n = 1 N f α, n, m ​ ( b) = 1 h m ​ ∑ n = 1 h m f α, n, m ​ ( b), f_{\alpha,m}(b):=\lim_{N\to\infty}\frac{1}{N}\sum_{n=1}^{N}f_{\alpha,n,m}(b)=\frac{1}{h_{m}}\sum_{n=1}^{h_{m}}f_{\alpha,n,m}(b), |  |

where h m:= #​ H m h_{m}:=\#H_{m} and H m:= ⟨ α + β m ​ 𝒪 ⟩ ⊂ ( 𝒪 / β m ​ 𝒪) × H_{m}:=\langle\alpha+\beta^{m}\mathcal{O}\rangle\subset(\mathcal{O}/\beta^{m}\mathcal{O})^{\times}.

We establish the asymptotic equidistribution of digits. Denote N ⁡ ( 𝔞):= #⁡ ( 𝒪 / 𝔞) N(\mathfrak{a}):=\#(\mathcal{O}/\mathfrak{a}) for any ideal 𝔞 ⊆ 𝒪 \mathfrak{a}\subseteq\mathcal{O}.

###### Theorem 1.2.

Let ( β) = 𝔭 1 g 1 ⋯ 𝔭 h g h (\beta)=\mathfrak{p}_{1}^{g_{1}}\cdots\mathfrak{p}_{h}^{g_{h}} satisfy that 𝔭 i \mathfrak{p}_{i} is unramified and N ⁡ ( 𝔭 i) = p i N(\mathfrak{p}_{i})=p_{i} for all i i, where p i p_{i} is the rational prime lying below 𝔭 i \mathfrak{p}_{i}. If α \alpha is relatively prime to β \beta and is not a root of unity, then

(1.7) |  | lim m → ∞ f α, m ​ ( b) = 1 / #​ 𝒟 \lim_{m\to\infty}f_{\alpha,m}(b)=1/\#\mathcal{D} |  |

holds for all b ∈ 𝒟 b\in\mathcal{D}.

When the prime ideal factorization of ( β) (\beta) contains a ramified prime ideal 𝔭 \mathfrak{p}, despite that its α \alpha -Wieferich property (as in Theorem 1.1) is not sufficient for the proof of the asymptotic equidistribution of digits, we are still able to obtain a result on the block complexity of β \beta -adic expansions of α n \alpha^{n}.

Denote the number of m m -truncated blocks by

 | 𝒞 m ( α):= #{ ( b 0, …, b m − 1) ∈ 𝒟 m: α n ≡ ∑ i = 0 m − 1 b i β i ( mod β m ​ 𝒪) for some n }, \mathcal{C}_{m}(\alpha):=\#\Big\{(b_{0},\dots,b_{m-1})\in\mathcal{D}^{m}\colon\alpha^{n}\equiv\sum_{i=0}^{m-1}b_{i}\beta^{i}\!\!\pmod{\beta^{m}\mathcal{O}}\;\;\text{for some $n$}\Big\}, |  |

we define the block complexity as

 | 𝒞 ⁡ ( α):= lim m → ∞ log ⁡ 𝒞 m ​ ( α) m ​ log ⁡ N ​ ( β), if the limit exists. \mathcal{C}(\alpha):=\lim_{m\to\infty}\frac{\log\mathcal{C}_{m}(\alpha)}{m\log N(\beta)},\quad\text{if the limit exists}. |  |

###### Theorem 1.3.

Let ( β) = 𝔭 1 g 1 ⋯ 𝔭 h g h (\beta)=\mathfrak{p}_{1}^{g_{1}}\cdots\mathfrak{p}_{h}^{g_{h}}. If α \alpha is not a root of unity and relatively prime to β \beta, then

(1.8) |  | 𝒞 ⁡ ( α) = ∑ j = 1 h g j ​ e j − 1 ​ log ⁡ p j ∑ j = 1 h g j ​ f j ​ log ⁡ p j, \mathcal{C}(\alpha)=\frac{\sum_{j=1}^{h}g_{j}e_{j}^{-1}\log p_{j}}{\sum_{j=1}^{h}g_{j}f_{j}\log p_{j}}, |  |

where p j p_{j} is the rational prime lying below 𝔭 j \mathfrak{p}_{j}, e j e_{j} is the ramification index of 𝔭 j \mathfrak{p}_{j} and f j f_{j} is the residue degree of 𝔭 j \mathfrak{p}_{j}.

## 2. The valuation ring and Teichmuller map

Note that Theorem 1.1 concerns only a single prime ideal 𝔭 \mathfrak{p}, so it is convenient to consider the localization of 𝒪 \mathcal{O} at 𝔭 \mathfrak{p}. Let K 𝔭 K_{\mathfrak{p}} be the completion of the number field K K with respect to the 𝔭 \mathfrak{p} -adic valuation v 𝔭 v_{\mathfrak{p}}. The *𝔭 \mathfrak{p} -adic integer ring*

 | 𝒪 𝔭:= { x ∈ K 𝔭: v 𝔭 ​ ( x) ≥ 0 } \mathcal{O}_{\mathfrak{p}}:=\{x\in K_{\mathfrak{p}}:v_{\mathfrak{p}}(x)\geq 0\} |  |

contains the *group of units*

 | 𝒪 𝔭 ×:= { x ∈ K 𝔭: v 𝔭 ​ ( x) = 0 } \mathcal{O}_{\mathfrak{p}}^{\times}:=\{x\in K_{\mathfrak{p}}:v_{\mathfrak{p}}(x)=0\} |  |

and the *unique maximal ideal*

 | 𝒫:= { x ∈ K 𝔭: v 𝔭 ​ ( x) > 0 }. \mathcal{P}:=\{x\in K_{\mathfrak{p}}:v_{\mathfrak{p}}(x)>0\}. |  |

Note that 𝒪 / 𝔭 k ≅ 𝒪 𝔭 / 𝒫 k \mathcal{O}/\mathfrak{p}^{k}\cong\mathcal{O}_{\mathfrak{p}}/\mathcal{P}^{k} holds for any k ∈ ℤ ≥ 1 k\in\mathbb{Z}_{\geq 1}. For convenience, we still denote the cyclic subgroup ⟨ α + 𝒫 k ⟩ ⊆ ( 𝒪 𝔭 / 𝒫 k) × \langle\alpha+\mathcal{P}^{k}\rangle\subseteq(\mathcal{O}_{\mathfrak{p}}/\mathcal{P}^{k})^{\times} as G k G_{k}.

Before studying Ker ⁡ ( G k → G k − 1) \ke(G_{k}\to G_{k-1}), we need to recall some basic facts about 𝒪 𝔭 \mathcal{O}_{\mathfrak{p}}. Fix a prime element π ∈ 𝒪 𝔭 \pi\in\mathcal{O}_{\mathfrak{p}}, i.e. an element satisfying v 𝔭 ​ ( π) = 1 v_{\mathfrak{p}}(\pi)=1, we have the following properties (see [12, Chapter II, Section 3 and 4] for details).

###### Proposition 2.1.

(i) Any x ∈ 𝒪 𝔭 x\in\mathcal{O}_{\mathfrak{p}} has a prime factorization

 | x = ε ​ π i, x=\varepsilon\pi^{i}, |  |

where ε ∈ 𝒪 𝔭 × \varepsilon\in\mathcal{O}_{\mathfrak{p}}^{\times} is a unit and i = v 𝔭 ​ ( x) i=v_{\mathfrak{p}}(x).

(ii) The nonzero proper ideals in 𝒪 𝔭 \mathcal{O}_{\mathfrak{p}} are the following principal ideals:

 | 𝒫 = ( π), 𝒫 2 = ( π 2), …, 𝒫 k = ( π k), … \mathcal{P}=(\pi),\;\mathcal{P}^{2}=(\pi^{2}),\;\ldots,\;\mathcal{P}^{k}=(\pi^{k}),\;\ldots |  |

(iii) Fix a set of representatives R R for 𝒪 𝔭 / 𝒫 \mathcal{O}_{\mathfrak{p}}/\mathcal{P}, containing 0 0. Then any x ∈ 𝒪 𝔭 x\in\mathcal{O}_{\mathfrak{p}} has a 𝔭 \mathfrak{p} -adic expansion

 | x = a 0 + a 1 ​ π + a 2 ​ π 2 + ⋯ + a k ​ π k + ⋯ x=a_{0}+a_{1}\pi+a_{2}\pi^{2}+\cdots+a_{k}\pi^{k}+\cdots |  |

where a k ∈ R a_{k}\in R for all k ∈ ℤ ≥ 0 k\in\mathbb{Z}_{\geq 0}.

The following lemma is rather elementary but plays a key role in our proof. Recall that p p is the rational prime lying below 𝔭 \mathfrak{p}, and e e is the ramification index of 𝔭 \mathfrak{p}.

###### Lemma 2.1.

Let a, b ∈ 𝒪 𝔭 × a,b\in\mathcal{O}_{\mathfrak{p}}^{\times}, if a ≡ b ( mod 𝒫 v) a\equiv b\!\!\pmod{\mathcal{P}^{v}} but a ≢ b ( mod 𝒫 v + 1) a\not\equiv b\!\!\pmod{\mathcal{P}^{v+1}} for some v ∈ ℤ ≥ 1 v\in\mathbb{Z}_{\geq 1}, then

(2.1) |  | a p ≡ b p ( mod 𝒫 min ⁡ { e + v, p ​ v }). a^{p}\equiv b^{p}\!\!\pmod{\mathcal{P}^{\min\{e+v,pv\}}}. |  |

Moreover, if p ​ v > e + v pv>e+v, then

(2.2) |  | a p ≡ b p ( mod 𝒫 e + v) but a p ≢ b p ( mod 𝒫 e + v + 1). a^{p}\equiv b^{p}\!\!\pmod{\mathcal{P}^{e+v}}\;\;\text{but }\;a^{p}\not\equiv b^{p}\!\!\pmod{\mathcal{P}^{e+v+1}}. |  |

###### Proof.

Since a ≡ b ( mod 𝒫 v) a\equiv b\!\!\pmod{\mathcal{P}^{v}} but a ≢ b ( mod 𝒫 v + 1) a\not\equiv b\!\!\pmod{\mathcal{P}^{v+1}}, we have a = b + ε ​ π v a=b+\varepsilon\pi^{v} for some ε ∈ 𝒪 𝔭 × \varepsilon\in\mathcal{O}_{\mathfrak{p}}^{\times}. Raise both sides to the p p -th power, we obtain that

(2.3) |  | a p − b p = ( b + ε ​ π v) p − b p = ( p 1) ​ b p − 1 ​ ε ​ π v + ( p 2) ​ b p − 2 ​ ε 2 ​ π 2 ​ v + ⋯ + ε p ​ π p ​ v. \begin{split}a^{p}-b^{p}&=(b+\varepsilon\pi^{v})^{p}-b^{p}\\ &=\binom{p}{1}b^{p-1}\varepsilon\pi^{v}+\binom{p}{2}b^{p-2}\varepsilon^{2}\pi^{2v}+\cdots+\varepsilon^{p}\pi^{pv}.\end{split} |  |

Note that ( p j) \binom{p}{j} is divisible by p p but not p 2 p^{2} for all 1 ≤ j ≤ p − 1 1\leq j\leq p-1, so

 | v 𝔭 ​ ( ( p j) ​ b p − j ​ ε j ​ π j ​ v) = e + j ​ v, for j ≠ p. v_{\mathfrak{p}}\left(\binom{p}{j}b^{p-j}\varepsilon^{j}\pi^{jv}\right)=e+jv,\quad\text{for $j\neq p$}. |  |

Hence v 𝔭 ​ ( a p − b p) ≥ min ⁡ { e + v, p ​ v } v_{\mathfrak{p}}(a^{p}-b^{p})\geq\min\{e+v,pv\}, which implies ( 2.1).

Moreover, if p ​ v > e + v pv>e+v, v 𝔭 ​ ( ( p j) ​ b p − j ​ ε j ​ π j ​ v) = e + v v_{\mathfrak{p}}\left(\binom{p}{j}b^{p-j}\varepsilon^{j}\pi^{jv}\right)=e+v only when j = 1 j=1, thus ( 2.2) holds. ∎

We conclude this section by defining the Teichmuller map in the standard way.

###### Definition 2.1.

The Teichmuller map τ: 𝒪 𝔭 × → 𝒪 𝔭 × \tau\colon\mathcal{O}_{\mathfrak{p}}^{\times}\to\mathcal{O}_{\mathfrak{p}}^{\times} is defined by

(2.4) |  | τ ⁡ ( x) = lim n → ∞ x p f ​ n, \tau(x)=\lim_{n\to\infty}x^{p^{fn}}, |  |

where f f is the residual degree of 𝔭 \mathfrak{p} and p p is the rational prime lying below 𝔭 \mathfrak{p}.

Recall that the 𝔭 \mathfrak{p} -adic absolute value is defined as | x | 𝔭:= c − v 𝔭 ​ ( x) |x|_{\mathfrak{p}}:=c^{-v_{\mathfrak{p}}(x)} for x ∈ K 𝔭 x\in K_{\mathfrak{p}}, where c c is some constant strictly greater than 1 1.

###### Lemma 2.2.

For any x ∈ 𝒪 𝔭 × x\in\mathcal{O}_{\mathfrak{p}}^{\times}, τ ⁡ ( x) \tau(x) is well-defined and we have

1. (i)

τ ⁡ ( x) \tau(x) satisfies the equation ( τ ⁡ ( x)) p f = τ ⁡ ( x) \big(\tau(x)\big)^{p^{f}}=\tau(x);

2. (ii)

we have τ ⁡ ( x) ≡ x ( mod 𝒫) \tau(x)\equiv x\pmod{\mathcal{P}}.

###### Proof.

We first show that the sequence ( x p f ​ n) n ≥ 1 (x^{p^{fn}})_{n\geq 1} is a Cauchy sequence with respect to the 𝔭 \mathfrak{p} -adic metric, hence the limit ( 2.4) exists.

For each x ∈ 𝒪 𝔭 × x\in\mathcal{O}_{\mathfrak{p}}^{\times}, since #​ ( 𝒪 𝔭 / 𝒫) × = p f − 1 \#(\mathcal{O}_{\mathfrak{p}}/\mathcal{P})^{\times}=p^{f}-1, we have x p f − 1 ≡ 1 ( mod 𝒫) x^{p^{f}-1}\equiv 1\pmod{\mathcal{P}}. Apply Lemma 2.1 with a = x p f − 1 a=x^{p^{f}-1} and b = 1 b=1, we have x ( p f − 1) ​ p ≡ 1 ( mod 𝒫 2) x^{(p^{f}-1)p}\equiv 1\pmod{\mathcal{P}^{2}}. Apply Lemma 2.1 repeatedly, we obtain that

(2.5) |  | x ( p f − 1) ​ p f ​ m ≡ ( mod 𝒫 1 + f ​ m) for all m ∈ ℤ ≥ 0. x^{(p^{f}-1)p^{fm}}\equiv 1\!\!\pmod{\mathcal{P}^{1+fm}}\quad\text{for all $m\in\mathbb{Z}_{\geq 0}$}. |  |

Thus | x p f ⁡ ( m + 1) − x p f ​ m | 𝔭 = | x p f ​ m | 𝔭 ⋅ | x ( p f − 1) ​ p f ​ m − 1 | 𝔭 ≤ c − 1 − f ​ m \big|x^{p^{f(m+1)}}-x^{p^{fm}}\big|_{\mathfrak{p}}=\big|x^{p^{fm}}\big|_{\mathfrak{p}}\cdot\big|x^{(p^{f}-1)p^{fm}}-1\big|_{\mathfrak{p}}\leq c^{-1-fm} for all m ∈ ℤ ≥ 0 m\in\mathbb{Z}_{\geq 0}, where | ⋅ | 𝔭:= c − v 𝔭 ​ ( ⋅) |\cdot|_{\mathfrak{p}}:=c^{-v_{\mathfrak{p}}(\cdot)} for some constant c > 1 c>1. Using this inequality, we obtain that for any integers n > m ≥ 1 n>m\geq 1,

 | | x p f ​ n − x p f ​ m | 𝔭 ≤ max ⁡ { | x p f ​ n − x p f ⁡ ( n − 1) | 𝔭, …, | x p f ⁡ ( m + 1) − x p f ​ m | 𝔭 } ≤ c − 1 − f ​ m → 0 ​ ( as ​ m → ∞), \begin{split}|x^{p^{fn}}-x^{p^{fm}}|_{\mathfrak{p}}&\leq\max\big\{|x^{p^{fn}}-x^{p^{f(n-1)}}|_{\mathfrak{p}},\dots,|x^{p^{f(m+1)}}-x^{p^{fm}}|_{\mathfrak{p}}\big\}\\ &\leq c^{-1-fm}\to 0\;\;(\text{as }m\to\infty),\end{split} |  |

which shows that the sequence ( x p f ​ n) n ≥ 1 (x^{p^{fn}})_{n\geq 1} is a Cauchy sequence.

For all m ∈ ℤ ≥ 0 m\in\mathbb{Z}_{\geq 0}, multiply both sides of ( 2.5) by x p f ​ m x^{p^{fm}}, we have

 | x p f ⁡ ( m + 1) ≡ x p f ​ m ( mod 𝒫 1 + f ​ m). x^{p^{f(m+1)}}\equiv x^{p^{fm}}\pmod{\mathcal{P}^{1+fm}}. |  |

Hence

 | x p f ​ m ≡ x p f ⁡ ( m − 1) ≡ ⋯ ≡ x ( mod 𝒫) x^{p^{fm}}\equiv x^{p^{f(m-1)}}\equiv\cdots\equiv x\pmod{\mathcal{P}} |  |

for all m ∈ ℤ ≥ 1 m\in\mathbb{Z}_{\geq 1}. Letting m → ∞ m\to\infty, we obtain Lemma 2.2 ( ii).

To see Lemma 2.2 ( i), we note that y ↦ y p f y\mapsto y^{p^{f}} is a continuous map on K 𝔭 K_{\mathfrak{p}}, so

 | ( τ ⁡ ( x)) p f = ( lim n → ∞ x p f ​ n) p f = lim n → ∞ x p f ⁡ ( n + 1) = τ ⁡ ( x). ∎ (\tau(x))^{p^{f}}=\big(\lim_{n\to\infty}x^{p^{fn}}\big)^{p^{f}}=\lim_{n\to\infty}x^{p^{f(n+1)}}=\tau(x).\qed |  |

## 3. Proof of Theorem 1.1

Let us start with the direct product decomposition of ( 𝒪 𝔭 / 𝒫 k) × (\mathcal{O}_{\mathfrak{p}}/\mathcal{P}^{k})^{\times} for each k ∈ ℤ ≥ 1 k\in\mathbb{Z}_{\geq 1}. Denote the multiplicative group of principal units modulo 𝒫 k \mathcal{P}^{k}

 | { x + 𝒫 k: x ≡ ( mod 𝒫) } \{x+\mathcal{P}^{k}:x\equiv 1\!\!\pmod{\mathcal{P}}\} |  |

as U 1 ( k) U_{1}^{(k)}. Consider the following short exact sequence

 | 1 ⟶ U 1 ( k) ⟶ ( 𝒪 𝔭 / 𝒫 k) × → φ k ( 𝒪 𝔭 / 𝒫) × ⟶ 1, 1\longrightarrow U_{1}^{(k)}\longrightarrow(\mathcal{O}_{\mathfrak{p}}/\mathcal{P}^{k})^{\times}\xrightarrow[\hskip 8.19447pt\;\;]{\varphi_{k}}(\mathcal{O}_{\mathfrak{p}}/\mathcal{P})^{\times}\longrightarrow 1, |  |

where φ k: x mod 𝒫 k ↦ x mod 𝒫 \varphi_{k}:x\bmod\mathcal{P}^{k}\mapsto x\bmod\mathcal{P}. Note that this short exact sequence splits, because there exists a homomorphism

 | ψ k: ( 𝒪 𝔭 / 𝒫) × ⟶ ( 𝒪 𝔭 / 𝒫 k) × a + 𝒫 ⟼ τ ⁡ ( a) + 𝒫 k, \begin{split}\psi_{k}:(\mathcal{O}_{\mathfrak{p}}/\mathcal{P})^{\times}&\longrightarrow\;\;(\mathcal{O}_{\mathfrak{p}}/\mathcal{P}^{k})^{\times}\\ a+\mathcal{P}\quad&\longmapsto\;\;\tau(a)+\mathcal{P}^{k},\end{split} |  |

where a ∈ R a\in R (the set of representatives as in Proposition 2.1 (iii)) and τ \tau is the Teichmüller map; and one can check that

 | φ k ∘ ψ k = id ( 𝒪 𝔭 / 𝒫) ×. \varphi_{k}\circ\psi_{k}=\operatorname{id}_{(\mathcal{O}_{\mathfrak{p}}/\mathcal{P})^{\times}}. |  |

Hence

(3.1) |  | ( 𝒪 𝔭 / 𝒫 k) × ≅ ( 𝒪 𝔭 / 𝒫) × × U 1 ( k). (\mathcal{O}_{\mathfrak{p}}/\mathcal{P}^{k})^{\times}\cong(\mathcal{O}_{\mathfrak{p}}/\mathcal{P})^{\times}\times U_{1}^{(k)}. |  |

Suppose α ∈ ( 𝒪 𝔭) × \alpha\in(\mathcal{O}_{\mathfrak{p}})^{\times} is not a root of unity and its 𝔭 \mathfrak{p} -adic expansion is

 | α = a 0 + a 1 ​ π + a 2 ​ π 2 + ⋯ + a k ​ π k + ⋯. \alpha=a_{0}+a_{1}\pi+a_{2}\pi^{2}+\cdots+a_{k}\pi^{k}+\cdots. |  |

Note that

 | φ k ​ ( α ​ ( τ ⁡ ( a 0)) − 1 + 𝒫 k) = φ k ​ ( α + 𝒫 k) ⋅ φ k ​ ( τ ​ ( a 0) − 1 + 𝒫 k) = ( a 0 + 𝒫) ⋅ ( a 0 + 𝒫) − 1 = 1 + 𝒫, \begin{split}\varphi_{k}\bigl(\alpha\big(\tau(a_{0})\big)^{-1}+\mathcal{P}^{k}\bigr)&=\varphi_{k}(\alpha+\mathcal{P}^{k})\cdot\varphi_{k}\big(\,\tau(a_{0})^{-1}+\mathcal{P}^{k}\big)\\ &=(a_{0}+\mathcal{P})\cdot(a_{0}+\mathcal{P})^{-1}\\ &=1+\mathcal{P},\end{split} |  |

thus α ​ ( τ ⁡ ( a 0)) − 1 + 𝒫 k ∈ U 1 ( k) \alpha(\tau(a_{0}))^{-1}+\mathcal{P}^{k}\in U_{1}^{(k)}. Therefore, the isomorphism in ( 3.1) applies to α \alpha as:

 | α + 𝒫 k = ( τ ⁡ ( a 0) + 𝒫 k) ​ ( α ​ ( τ ⁡ ( a 0)) − 1 + 𝒫 k) ⟼ ( a 0 + 𝒫) × ( α ​ ( τ ⁡ ( a 0)) − 1 + 𝒫 k). \alpha+\mathcal{P}^{k}=(\tau(a_{0})+\mathcal{P}^{k})\bigl(\alpha(\tau(a_{0}))^{-1}+\mathcal{P}^{k}\bigr)\longmapsto(a_{0}+\mathcal{P})\times\big(\alpha(\tau(a_{0}))^{-1}+\mathcal{P}^{k}\big). |  |

Hence we obtain the isomorphism

(3.2) |  | G k = ⟨ α + 𝒫 k ⟩ ≅ ⟨ a 0 + 𝒫 ⟩ × ⟨ α ​ ( τ ⁡ ( a 0)) − 1 + 𝒫 k ⟩. G_{k}=\langle\alpha+\mathcal{P}^{k}\rangle\cong\langle a_{0}+\mathcal{P}\rangle\times\langle\alpha(\tau(a_{0}))^{-1}+\mathcal{P}^{k}\rangle. |  |

Let η = α ​ ( τ ⁡ ( a 0)) − 1 \eta=\alpha(\tau(a_{0}))^{-1}, by ( 3.2), we have

(3.3) |  | #​ Ker ⁡ ( G k → G k − 1) = #​ Ker ⁡ ( ⟨ η + 𝒫 k ⟩ → ⟨ η + 𝒫 k − 1 ⟩). \#\ke(G_{k}\to G_{k-1})=\#\ke\big(\langle\eta+\mathcal{P}^{k}\rangle\to\langle\eta+\mathcal{P}^{k-1}\rangle\big). |  |

We proceed to calculate the order of η + 𝒫 k \eta+\mathcal{P}^{k} in U 1 ( k) U_{1}^{(k)}, which is denoted by Ord k ⁡ ( η) \operatorname{Ord}_{k}(\eta). By [5, Theorem 80], we obtain that

 | #​ ( 𝒪 𝔭 / 𝒫 k) × = N ​ ( 𝔭 k) ​ ( 1 − 1 N ⁡ ( 𝔭)) = p f ⁡ ( k − 1) ​ ( p f − 1), and #​ ( 𝒪 𝔭 / 𝒫) × = p f − 1, \begin{split}\#(\mathcal{O}_{\mathfrak{p}}/\mathcal{P}^{k})^{\times}&=N(\mathfrak{p}^{k})\left(1-\frac{1}{N(\mathfrak{p})}\right)\\ &=p^{f(k-1)}(p^{f}-1),\quad\text{and}\\ \#(\mathcal{O}_{\mathfrak{p}}/\mathcal{P})^{\times}&=p^{f}-1,\end{split} |  |

Combining this with ( 3.1), we have #​ U 1 ( k) = p f ⁡ ( k − 1) \#U_{1}^{(k)}=p^{f(k-1)}, hence Ord k ⁡ ( η) \operatorname{Ord}_{k}(\eta) must be a power of p p.

Denote v ⁡ ( j) = v 𝔭 ​ ( η p j − 1) v(j)=v_{\mathfrak{p}}(\eta^{p^{j}}-1) for each j ∈ ℤ ≥ 0 j\in\mathbb{Z}_{\geq 0}. Since η p j ≡ ( mod 𝒫 v ⁡ ( j)) \eta^{p^{j}}\equiv 1\!\!\pmod{\mathcal{P}^{v(j)}} but η p j ≢ ( mod 𝒫 v ⁡ ( j) + 1) \eta^{p^{j}}\not\equiv 1\!\!\pmod{\mathcal{P}^{v(j)+1}}, we can apply Lemma 2.1 with a = η p j a=\eta^{p^{j}} and b = 1 b=1, and obtain

 | v ⁡ ( j + 1) ≥ min ⁡ { e + v ⁡ ( j), p ​ v ​ ( j) } > v ⁡ ( j). v(j+1)\geq\min\{e+v(j),pv(j)\}>v(j). |  |

Since ( v ⁡ ( j)) j ≥ 1 \big(v(j)\big)_{j\geq 1} is strictly increasing, there exists l ∈ ℤ ≥ 0 l\in\mathbb{Z}_{\geq 0} such that v ⁡ ( l) > e v(l)>e. When j ≥ l j\geq l, since p ​ v ​ ( j) > e + v ⁡ ( j) pv(j)>e+v(j), we can apply ( 2.2) in Lemma 2.1 with a = η p j a=\eta^{p^{j}} and b = 1 b=1 to deduce

(3.4) |  | v ⁡ ( j + 1) = v ⁡ ( j) + e. v(j+1)=v(j)+e. |  |

For each k > v ⁡ ( l) k>v(l), let k ~ = ⌈ ( k − v ⁡ ( l)) ​ e − 1 ⌉ \widetilde{k}=\left\lceil(k-v(l))e^{-1}\right\rceil, where ⌈ x ⌉ \lceil x\rceil is the smallest integer not less than x x. Using ( 3.4) repeatedly, we have

 | v ⁡ ( l + k ~) = v ⁡ ( l) + e ​ k ~ ≥ v ⁡ ( l) + ( k − v ⁡ ( l)) = k. \begin{split}v(l+\tilde{k})&=v(l)+e\widetilde{k}\\ &\geq v(l)+(k-v(l))=k.\end{split} |  |

Hence η p l + k ~ ≡ 1 ( mod 𝒫 k) \eta^{p^{l+\widetilde{k}}}\equiv 1\pmod{\mathcal{P}^{k}}. Moreover, by using ( 3.4) k ~ − 1 \widetilde{k}-1 times, we have

 | v ⁡ ( l + k ~ − 1) = v ⁡ ( l) + e ⁡ ( k ~ − 1) < v ⁡ ( l) + k − v ⁡ ( l) = k, \begin{split}v(l+\widetilde{k}-1)&=v(l)+e(\widetilde{k}-1)\\ &<v(l)+k-v(l)=k,\end{split} |  |

thus η p l + k ~ − 1 ≢ 1 ( mod 𝒫 k) \eta^{p^{l+\widetilde{k}-1}}\not\equiv 1\pmod{\mathcal{P}^{k}}. Therefore

(3.5) |  | Ord k ⁡ ( η) = p l + k ~. \operatorname{Ord}_{k}(\eta)=p^{l+\widetilde{k}}. |  |

- •

If k − v ⁡ ( l) ≡ 1 ( mod e) k-v(l)\equiv 1\pmod{e}, we can write k − v ⁡ ( l) = h ​ e + 1 k-v(l)=he+1, then

 | Ord k ⁡ ( η) = p l + ⌈ h ​ e + 1 e ⌉ = p l + h + 1, Ord k − 1 ⁡ ( η) = p l + ⌈ h ​ e e ⌉ = p l + h. \begin{split}\operatorname{Ord}_{k}(\eta)&=p^{l+\left\lceil\frac{he+1}{e}\right\rceil}=p^{l+h+1},\\ \operatorname{Ord}_{k-1}(\eta)&=p^{l+\left\lceil\frac{he}{e}\right\rceil}=p^{l+h}.\end{split} |  |

- •

If k − v ⁡ ( l) ≢ 1 ( mod e) k-v(l)\not\equiv 1\pmod{e}, we can write k − v ⁡ ( l) = h ​ e + r k-v(l)=he+r with r ∈ { 2, 3, …, e } r\in\{2,3,\dots,e\}, then

 | Ord k ⁡ ( η) = p l + ⌈ h ​ e + r e ⌉ = p l + h + 1, Ord k − 1 ⁡ ( η) = p l + ⌈ h ​ e + r − 1 e ⌉ = p l + h + 1. \begin{split}\operatorname{Ord}_{k}(\eta)&=p^{l+\left\lceil\frac{he+r}{e}\right\rceil}=p^{l+h+1},\\ \operatorname{Ord}_{k-1}(\eta)&=p^{l+\left\lceil\frac{he+r-1}{e}\right\rceil}=p^{l+h+1}.\end{split} |  |

Combining this with ( 3.3),

 | #​ Ker ⁡ ( G k → G k − 1) = #​ Ker ⁡ ( ⟨ η + 𝒫 k ⟩ → ⟨ η + 𝒫 k − 1 ⟩) = #​ ⟨ η + 𝒫 k ⟩ #​ ⟨ η + 𝒫 k − 1 ⟩ = { p, if k − v ⁡ ( l) ≡ 1 ( mod e), 1, if k − v ⁡ ( l) ≢ 1 ( mod e), \begin{split}&\#\ke(G_{k}\to G_{k-1})=\#\ke\bigl(\langle\eta+\mathcal{P}^{k}\rangle\to\langle\eta+\mathcal{P}^{k-1}\rangle\bigr)\\ =&\frac{\#\langle\eta+\mathcal{P}^{k}\rangle}{\#\langle\eta+\mathcal{P}^{k-1}\rangle}=\begin{cases}p,&\quad\text{if $k-v(l)\equiv 1\pmod{e}$},\\ 1,&\quad\text{if $k-v(l)\not\equiv 1\pmod{e}$},\end{cases}\end{split} |  |

which completes the proof of Theorem 1.1.

## 4. Proof of Theorem 1.2 and Theorem 1.3

Let α, β ∈ 𝒪 \alpha,\beta\in\mathcal{O} be as in Theorem 1.2 and recall that

 | H m = ⟨ α + β m ​ 𝒪 ⟩ ⊆ ( 𝒪 / β m ​ 𝒪) ×, H_{m}=\langle\alpha+\beta^{m}\mathcal{O}\ \rangle\subseteq(\mathcal{O}/\beta^{m}\mathcal{O})^{\times}, |  |

is the multiplicative subgroup generated by α \alpha modulo β m ​ 𝒪 \beta^{m}\mathcal{O}.

Since ( β) = 𝔭 1 g 1 ⋯ 𝔭 h g h (\beta)=\mathfrak{p}_{1}^{g_{1}}\cdots\mathfrak{p}_{h}^{g_{h}}, by the Chinese remainder theorem, there exists an isomorphism

 | α n ( mod β m) ↦ ( α n ( mod 𝔭 1 g 1 ​ m), …, α n ( mod 𝔭 h g h ​ m)) \alpha^{n}\!\!\!\!\pmod{\beta^{m}}\mapsto\left(\alpha^{n}\!\!\!\!\pmod{\mathfrak{p}_{1}^{g_{1}m}},\ldots,\alpha^{n}\!\!\!\!\pmod{\mathfrak{p}_{h}^{g_{h}m}}\right) |  |

such that

(4.1) |  | H m ≅ G g 1 ​ m ( 1) × G g 2 ​ m ( 2) × ⋯ × G g h ​ m ( h), H_{m}\cong G_{g_{1}m}^{(1)}\times G_{g_{2}m}^{(2)}\times\cdots\times G_{g_{h}m}^{(h)}, |  |

where G k ( j):= ⟨ α + 𝔭 j k ⟩ ⊆ ( 𝒪 / 𝔭 j k) × G_{k}^{(j)}:=\langle\alpha+\mathfrak{p}_{j}^{k}\rangle\subseteq(\mathcal{O}/\mathfrak{p}_{j}^{k})^{\times} for all j ∈ { 1, 2, …, h } j\in\{1,2,\dots,h\}.

### 4.1. Proof of Theorem 1.2

Since 𝔭 j \mathfrak{p}_{j} is unramified for all j ∈ { 1, 2, …, h } j\in\{1,2,\dots,h\}, by Theorem 1.1, there exists an positive integer M M such that

 | #​ G k ( j) = #​ Ker ⁡ ( G k ( j) → G k − 1 ( j)) ⋅ #​ G k − 1 ( j) = p j ⋅ #​ G k − 1 ( j), \#G_{k}^{(j)}=\#\ke(G_{k}^{(j)}\to G_{k-1}^{(j)})\cdot\#G_{k-1}^{(j)}=p_{j}\cdot\#G_{k-1}^{(j)}, |  |

for all k ≥ M k\geq M and j ∈ { 1, 2, …, h } j\in\{1,2,\dots,h\}, where p j p_{j} is the rational prime lying below 𝔭 j \mathfrak{p}_{j}. Combining this with ( 4.1), we have

(4.2) |  | h m: = #​ H m = ∏ j = 1 h #​ G g j ​ m ( j) = ∏ j = 1 h ( p j g j ​ #​ G g j ​ ( m − 1) ( j)) = ∏ j = 1 h N ​ ( 𝔭 j) g j ⋅ ∏ j = 1 h #​ G g j ​ ( m − 1) ( j) = N ⁡ ( β) ⋅ #​ H m − 1 = N ⁡ ( β) ​ h m − 1, \begin{split}h_{m}&:=\#H_{m}=\prod_{j=1}^{h}\#G_{g_{j}m}^{(j)}=\prod_{j=1}^{h}\left(p_{j}^{g_{j}}\#G_{g_{j}(m-1)}^{(j)}\right)\\ &=\prod_{j=1}^{h}N(\mathfrak{p}_{j})^{g_{j}}\cdot\prod_{j=1}^{h}\#G_{g_{j}(m-1)}^{(j)}=N(\beta)\cdot\#H_{m-1}=N(\beta)h_{m-1},\end{split} |  |

for all m ≥ M + 1 m\geq M+1.

Recall that ( α n) β, i (\alpha^{n})_{\beta,i} is the i i -th digit in the β \beta -adic expansion of α n \alpha^{n}, we define

 | D n, m ​ ( b):= #⁡ { 0 ≤ i < m: ( α n) β, i = b }, D_{n,m}(b):=\#\{0\leq i<m:(\alpha^{n})_{\beta,i}=b\}, |  |

and

 | D m ​ ( b):= ∑ n = 1 h m D n, m ​ ( b), D_{m}(b):=\sum_{n=1}^{h_{m}}D_{n,m}(b), |  |

for each digit b ∈ 𝒟 b\in\mathcal{D}.

Denote ( a 0, a 1, ⋯, a m − 1) β:= ∑ j = 0 m − 1 a j ​ β j (a_{0},a_{1},\cdots,a_{m-1})_{\beta}:=\sum_{j=0}^{m-1}a_{j}\beta^{j} for ( a 0, a 1, ⋯, a m − 1) ∈ 𝒟 m (a_{0},a_{1},\cdots,a_{m-1})\in\mathcal{D}^{m}, we have

 | D m ​ ( b) = ∑ n = 1 h m #⁡ { 0 ≤ i < m: ( α n) β, i = b } = ∑ ( a 0, a 1, ⋯, a m − 1) β ∈ H m #⁡ { 0 ≤ i < m: a i = b } = ∑ ( a 0, a 1, ⋯, a m − 2) β ∈ H m − 1 ∑ a m − 1 ∈ 𝒟 #⁡ { 0 ≤ i < m: a i = b }, \begin{split}D_{m}(b)&=\sum_{n=1}^{h_{m}}\#\{0\leq i<m:(\alpha^{n})_{\beta,i}=b\}\\ &=\sum_{(a_{0},a_{1},\cdots,a_{m-1})_{\beta}\in H_{m}}\#\{0\leq i<m:a_{i}=b\}\\ &=\sum_{(a_{0},a_{1},\cdots,a_{m-2})_{\beta}\in H_{m-1}}\;\sum_{a_{m-1}\in\mathcal{D}}\#\{0\leq i<m:a_{i}=b\},\end{split} |  |

where we use ( 4.2) in the last equality. Note that if a m − 1 = b a_{m-1}=b, then

 | #⁡ { 0 ≤ i < m: a i = b } = 1 + #⁡ { 0 ≤ i < m − 1: a i = b }, \#\{0\leq i<m:a_{i}=b\}=1+\#\{0\leq i<m-1:a_{i}=b\}, |  |

otherwise,

 | #⁡ { 0 ≤ i < m: a i = b } = #⁡ { 0 ≤ i < m − 1: a i = b }. \#\{0\leq i<m:a_{i}=b\}=\#\{0\leq i<m-1:a_{i}=b\}. |  |

Thus

 | D m ​ ( b) = ∑ ( a 0, a 1, ⋯, a m − 2) β ∈ H m − 1 ( N ⁡ ( β) ⋅ #⁡ { 0 ≤ i < m − 1: a i = b } + 1) = N ⁡ ( β) ​ D m − 1 ​ ( b) + h m − 1. \begin{split}D_{m}(b)&=\sum_{(a_{0},a_{1},\cdots,a_{m-2})_{\beta}\in H_{m-1}}(N(\beta)\cdot\#\{0\leq i<m-1:a_{i}=b\}+1)\\ &=N(\beta)D_{m-1}(b)+h_{m-1}.\end{split} |  |

Repeating the process above, we have

(4.3) |  | D m ​ ( b) = ( N ⁡ ( β)) 2 ​ D m − 2 ​ ( b) + N ⁡ ( β) ​ h m − 2 + h m − 1 = ( N ⁡ ( β)) m − M ​ D M ​ ( b) + ( N ⁡ ( β)) m − M − 1 ​ h M + ⋯ + h m − 1 = ( N ⁡ ( β)) m − M ​ D M ​ ( b) + ( m − M) ​ ( N ⁡ ( β)) m − M − 1 ​ h M, \begin{split}D_{m}(b)&=\big(N(\beta)\big)^{2}D_{m-2}(b)+N(\beta)h_{m-2}+h_{m-1}\\ &\vdots\\ &=(N(\beta))^{m-M}D_{M}(b)+(N(\beta))^{m-M-1}h_{M}+\cdots+h_{m-1}\\ &=(N(\beta))^{m-M}D_{M}(b)+(m-M)(N(\beta))^{m-M-1}h_{M},\end{split} |  |

where we use ( 4.2) in the last equality. Therefore, by ( 1.5), ( 1.6), ( 4.3) and

 | h m = ( N ⁡ ( β)) m − M ​ h M, h_{m}=(N(\beta))^{m-M}h_{M}, |  |

we have

 | f α, m ​ ( b) = 1 h m ​ ∑ n = 1 h m f α, n, m ​ ( b) = D m ​ ( b) m ​ h m = D M ​ ( b) m ​ h M + m − M m ​ ( N ⁡ ( β)) − 1. \begin{split}f_{\alpha,m}(b)&=\frac{1}{h_{m}}\sum_{n=1}^{h_{m}}f_{\alpha,n,m}(b)\\ &=\frac{D_{m}(b)}{mh_{m}}=\frac{D_{M}(b)}{mh_{M}}+\frac{m-M}{m}(N(\beta))^{-1}.\end{split} |  |

Letting m → ∞ m\to\infty, we obtain

 | lim m → ∞ f m ​ ( b) = ( N ⁡ ( β)) − 1 = 1 / #​ 𝒟, \lim_{m\to\infty}f_{m}(b)=(N(\beta))^{-1}=1/\#\mathcal{D}, |  |

which completes the proof of Theorem 1.2.

### 4.2. Proof of Theorem 1.3

Since the ramification index of 𝔭 j \mathfrak{p}_{j} is e j e_{j}, by Theorem 1.1, there exists an positive integer M M such that for all k ≥ M k\geq M and j ∈ { 1, 2, …, h } j\in\{1,2,\dots,h\},

 | #​ G k ( j) \displaystyle\#G_{k}^{(j)} | = #​ Ker ⁡ ( G k ( j) → G k − 1 ( j)) ⋅ #​ G k − 1 ( j) \displaystyle=\#\ke(G_{k}^{(j)}\to G_{k-1}^{(j)})\cdot\#G_{k-1}^{(j)} |  |

 |  | = #​ Ker ⁡ ( G k ( j) → G k − 1 ( j)) ⋅ #​ Ker ⁡ ( G k − 1 ( j) → G k − 2 ( j)) ⋅ #​ G k − 2 ( j) \displaystyle=\#\ke(G_{k}^{(j)}\to G_{k-1}^{(j)})\cdot\#\ke(G_{k-1}^{(j)}\to G_{k-2}^{(j)})\cdot\#G_{k-2}^{(j)} |  |

(4.4) |  |  | = ⋯ = p j ⋅ #​ G k − e j ( j), \displaystyle=\cdots=p_{j}\cdot\#G_{k-e_{j}}^{(j)}, |  |

where p j p_{j} is the rational prime lying below 𝔭 j \mathfrak{p}_{j}. Applying ( 4.4) repeatedly, we have

(4.5) |  | p j [k − M e j] ​ #​ G M ( j) ≤ #​ G k ( j) ≤ p j [k − M e j] + 1 ​ #​ G M ( j). p_{j}^{\big[\frac{k-M}{e_{j}}\big]}\#G_{M}^{(j)}\leq\#G_{k}^{(j)}\leq p_{j}^{\big[\frac{k-M}{e_{j}}\big]+1}\#G_{M}^{(j)}. |  |

Combining this with ( 4.1), we have

(4.6) |  | 𝒞 m ​ ( α) = #​ H m = ∏ j = 1 h #​ G g j ​ m ( j) ≤ ∏ j = 1 h ( p j [g j ​ m − M e j] + 1 ​ #​ G M ( j)), and 𝒞 m ​ ( α) ≥ ∏ j = 1 h ( p j [g j ​ m − M e j] ​ #​ G M ( j)), \begin{split}\mathcal{C}_{m}(\alpha)&=\#H_{m}=\prod_{j=1}^{h}\#G_{g_{j}m}^{(j)}\leq\prod_{j=1}^{h}\Big(p_{j}^{\big[\frac{g_{j}m-M}{e_{j}}\big]+1}\#G_{M}^{(j)}\Big),\;\;\text{ and }\\ \mathcal{C}_{m}(\alpha)&\geq\prod_{j=1}^{h}\Big(p_{j}^{\big[\frac{g_{j}m-M}{e_{j}}\big]}\#G_{M}^{(j)}\Big),\end{split} |  |

for all m ≥ M m\geq M. Hence, setting C M:= log ⁡ ( ∏ j = 1 h #​ G M ( j)) C_{M}:=\log(\prod_{j=1}^{h}\#G_{M}^{(j)}),

 | C M + ∑ j = 1 h ( g j ​ m − M e j − 1) ​ log ⁡ p j m ​ ∑ j = 1 h f j ​ g j ​ log ⁡ p j ≤ log ⁡ 𝒞 m ​ ( α) m ​ log ⁡ N ​ ( β) ≤ C M + ∑ j = 1 h ( g j ​ m − M e j + 1) ​ log ⁡ p j m ​ ∑ j = 1 h f j ​ g j ​ log ⁡ p j, \begin{split}&\frac{C_{M}+\sum_{j=1}^{h}(\frac{g_{j}m-M}{e_{j}}-1)\log p_{j}}{m\sum_{j=1}^{h}f_{j}g_{j}\log p_{j}}\leq\frac{\log\mathcal{C}_{m}(\alpha)}{m\log N(\beta)}\\ \leq&\;\frac{C_{M}+\sum_{j=1}^{h}(\frac{g_{j}m-M}{e_{j}}+1)\log p_{j}}{m\sum_{j=1}^{h}f_{j}g_{j}\log p_{j}},\end{split} |  |

where we use N ⁡ ( β) = ∏ j = 1 h N ​ ( 𝔭) g j = ∏ j = 1 h p j f j ​ g j N(\beta)=\prod_{j=1}^{h}N(\mathfrak{p})^{g_{j}}=\prod_{j=1}^{h}p_{j}^{f_{j}g_{j}}. Letting m → ∞ m\to\infty, we obtain ( 1.8), which completes the proof of Theorem 1.3.

## Acknowledgements

R. Li was supported by NSFC No. 12401006 and Guangdong Basic and Applied Basic Research Foundation No. 2023A1515110272. J. Zhao was supported by NSFC No. 12471085 and Science and Technology Commission of Shanghai Municipality (STCSM) No. 22DZ2229014.

## References

- [1] R. Crandall, K. Dilcher and C. Pomerance. A search for Wieferich and Wilson primes. Math. Comp., 66(217):433–449, 1997.
- [2] V. S. Dimitrov and E. W. Howe. Powers of 3 with few nonzero bits and a conjecture of Erdős. Rocky Mountain J. Math., 55(1):45–61, 2025.
- [3] T. Dupuy and D. E. Weirich. Bits of 3 n 3^{n} in binary, Wieferich primes and a conjecture of Erdös. J. Number Theory, 158:268–280, 2016.
- [4] P. Erdös. Some unconventional problems in number theory. Math. Mag. 52(2):67–70, 1979.
- [5] E. Hecke. Lectures on the theory of algebraic numbers. Springer-Verlag, New York-Berlin, Graduate Texts in Mathematics 77, 1981.
- [6] S. T. Holdum, F. R. Klausen, and P. M. Reichstein Rasmussen. Powers in prime bases and a problem on central binomial coefficients. Integers, 15:Paper No. A43, 13, 2015.
- [7] N. M. Katz. Wieferich past and future. Topics in finite fields. Amer. Math. Soc., Providence, RI., Contemp. Math. 632:253–270, 2015.
- [8] R. E. Kennedy and C. Cooper. A generalization of a result by Narkiewicz concerning large digits of powers. Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat., 11:36–40, 2000.
- [9] J. C. Lagarias. Ternary expansions of powers of 2. J. Lond. Math. Soc. (2), 79(3):562–588, 2009.
- [10] S. Lang. Old and new conjectured Diophantine inequalities. Bull. Amer. Math. Soc. (N.S.), 23(1):37–75, 1990.
- [11] W. Narkiewicz. A note on a paper of H. Gupta concerning powers of two and three: “Powers of 2 2 and sums of distinct powers of 3 3 ” [Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat. Fiz. No. 602-633 (1978), 151–158 (1979); MR 81g:10016]. Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat. Fiz., (678-715):173–174, 1980.
- [12] J. Neukirch. Algebraic number theory. Springer-Verlag, Berlin. Grundlehren der mathematischen Wissenschaften 322, 1999.
- [13] J. H. Silverman. Wieferich’s criterion and the a ​ b ​ c abc -conjecture. J. Number Theory., 30(2):226–237, 1988.
- [14] A. P. Wieferich. Zum letzten Fermatschen Theorem. J. Reine Angew. Math., 136(1909):293–302.
- [15] J. Zhao, and R. Li. On β \beta -adic expansions of powers of an algebraic integer ommitting a digit. Quaest. Math., 48(8):1247–1260, 2025.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:liruofan@jnu.edu.cn
[4]: mailto:zhao9zone@gmail.com
