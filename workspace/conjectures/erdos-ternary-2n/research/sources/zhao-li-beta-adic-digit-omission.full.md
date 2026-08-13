<!-- source: https://arxiv.org/html/2405.06220v2 | converted from HTML -->

On β -adic expansions of powers of an algebraic integer omitting a digit

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2405.06220v2 [math.NT] 04 Dec 2025

# On β \beta -adic expansions of powers of an algebraic integer omitting a digit Thanks: ∗ Corresponding author.

Jiuzhou Zhao Address: School of Mathematical Sciences, Key Laboratory of MEA(Ministry of Education) & \& Shanghai Key Laboratory of PMMP, East China Normal University, Shanghai, 200241, China Email address: [zhao9zone@gmail.com][3] and Ruofan Li ∗ Address: Department of Mathematics, Jinan University, Guangzhou, 510632, China Email address: [liruofan@jnu.edu.cn][4]

###### Abstract.

Let α, β \alpha,\beta be two relatively prime algebraic integers in a number field K K and N N be a positive integer. We show that the number of n ∈ { 1, 2, …, N } n\in\{1,2,\dots,N\} such that the β \beta -adic expansion of α n \alpha^{n} omits a given digit is less than C 1 ​ N σ ⁡ ( β) C_{1}N^{\sigma(\beta)}, where σ ⁡ ( β):= log ⁡ ( | N ⁡ ( β) | − 1) log ⁡ | N ⁡ ( β) | \sigma(\beta):=\frac{\log(|N(\beta)|-1)}{\log|N(\beta)|} and C 1 C_{1} is a constant depending only on β \beta, if all prime ideal factors of β \beta are unramified and their norms are integer primes.

###### Key words and phrases:

Radix representation, digital problems, p p -adic interpolation

###### 2020 Mathematics Subject Classification

Primary 11A63; Secondary 11R04.

## 1. Introduction

Consider the ternary expansion

 | ( 2 n) 3:= a k n ​ … ​ a 1 ​ a 0, (2^{n})_{3}:=a_{k_{n}}\dots a_{1}a_{0}, |  |

where a j ∈ { 0, 1, 2 } a_{j}\in\{0,1,2\}, 0 ≤ j ≤ k n 0\leq j\leq k_{n} satisfies 2 n = ∑ j = 0 k n a j ​ 3 j 2^{n}=\sum_{j=0}^{k_{n}}a_{j}3^{j}. It is an interesting phenomenon that ( 2 0) 3 = 1 (2^{0})_{3}=1, ( 2 2) 3 = 11 (2^{2})_{3}=11 and ( 2 8) 3 = 100111 (2^{8})_{3}=100111 omit the digit 2 2. No other value of n n such that ( 2 n) 3 (2^{n})_{3} omits the digit 2 2 is known. Indeed, Erdős [4] proposed the following conjecture, which is still open.

###### Conjecture 1.1.

The ternary expansion of 2 n 2^{n} can not omit the digit 2 2 for all n ≥ 9 n\geq 9.

This conjecture is related to the *persistence*problem (see [1, 2]) which concerns base b b expansion of natural numbers. Given an integer b > 1 b>1 and a natural number n = ∑ j = 1 k d j ​ b k − j n=\sum_{j=1}^{k}d_{j}b^{k-j} with d j ∈ { 0, 1, …, b − 1 } d_{j}\in\{0,1,\dots,b-1\}, define the Sloane map S b: ℕ → ℕ S_{b}:\mathbb{N}\to\mathbb{N} by S b ​ ( n):= ∏ j = 1 k d j S_{b}(n):=\prod_{j=1}^{k}d_{j}. By [2, Proposition 1.1], S b ​ ( n) < n S_{b}(n)<n for all n ≥ b n\geq b. Thus, the orbit under the Sloane map S b m ​ ( n) S^{m}_{b}(n), m ≥ 1 m\geq 1 always stabilizes after a finite number of steps, that is, there exists a minimal number l b ​ ( n) l_{b}(n) such that S b j ​ ( n) = S b l b ​ ( n) ​ ( n) S^{j}_{b}(n)=S^{l_{b}(n)}_{b}(n) for all j ≥ l b ​ ( n) j\geq l_{b}(n). When b = 2 b=2, it is trivial to see that l b ​ ( n) = 1 l_{b}(n)=1 for all n n, the *persistence*problem asks whether a uniform bound of l b ​ ( n) l_{b}(n) exists in general.

###### Problem 1.2 (*Persistence*problem).

For a given b > 2 b>2, is there a positive number B ⁡ ( b) B(b) such that l b ​ ( n) ≤ B ​ ( b) l_{b}(n)\leq B(b) for all n?

In the case of base b = 3 b=3, the only nonzero values assumed by the Sloane map are powers of 2 2. Hence, in order to answer the persistence problem for base 3 3, it suffices to establish the following weaker form of Conjecture 1.1.

###### Conjecture 1.3.

There is a positive integer k 0 k_{0} such that for all k ≥ k 0 k\geq k_{0}, the ternary expansion of 2 k 2^{k} can not omit the digit 0 0.

Another problem related to Conjecture 1.1 is determining *practical binomial coefficients*(see [17, 21]). A positive integer n n is called *practical*if all positive integers less than n n can be written as a sum of distinct divisors of n n. Leonetti and Sanna [17] remarked that, likely, there are only finitely many positive integers n n such that ( 2 ​ n n) \binom{2n}{n} is not a practical number. They proved that if n n is a power of 2 2 whose ternary expansion omits the digit 2 2, then ( 2 ​ n n) \binom{2n}{n} is not a practical number [17, Proposition 2.1].

Progress towards Conjecture 1.1 has been in the form of upper bounds on

 | ℳ ⁡ ( N):= #⁡ { 1 ≤ n ≤ N: ( 2 n) 3 ​ omits the digit 2 }, \mathcal{M}(N):=\#\big\{1\leq n\leq N\colon(2^{n})_{3}\text{ omits the digit $2$}\big\}, |  |

where the symbol #\#denote cardinality. The best known bound on ℳ ⁡ ( N) \mathcal{M}(N) is due to Narkiewicz [19] who proved that

(1.1) |  | ℳ ( N) ≤ 1.62 N σ, where σ:= log 3 ⁡ 2 ≈ 0.63092. \mathcal{M}(N)\leq 1.62N^{\sigma},\quad\text{ where $\sigma:=\log_{3}2\approx 0.63092$. } |  |

We refer the reader to [3, 7, 14, 16] for more results related to Narkiewicz’s result.

In this paper, we are going to generalize Narkiewicz’s result ( 1.1) by describing the above phenomena in general algebraic number fields. Let K K be a number field with ring of integers 𝒪 K \mathcal{O}_{K}. Fix an element β ∈ 𝒪 K \beta\in\mathcal{O}_{K} with norm | N ⁡ ( β) | > 1 |N(\beta)|>1.

###### Definition 1.4.

We call ( β, { 0, 1, …, | N ⁡ ( β) | − 1 }) (\beta,\,\mathcal{\{}0,1,\dots,|N(\beta)|-1\}) a *canonical number system (CNS)*in 𝒪 K \mathcal{O}_{K}, if every α ∈ 𝒪 K \alpha\in\mathcal{O}_{K} can be represented uniquely as

(1.2) |  | α = a 0 + a 1 ​ β + ⋯ + a m ​ β m, a j ∈ { 0, 1, …, | N ⁡ ( β) | − 1 } ​ ( j = 0, 1, …, m), \alpha=a_{0}+a_{1}\beta+\cdots+a_{m}\beta^{m},\quad a_{j}\in\mathcal{\{}0,1,\dots,|N(\beta)|-1\}\;(j=0,1,\dots,m), |  |

which is called the *radix expansion*of α \alpha in base β \beta. For convenience, denote

(1.3) |  | ( α) β:= a m ​ … ​ a 1 ​ a 0, and ​ ( α) β, j:= a j ​ ( j = 0, 1, …, m). (\alpha)_{\beta}:=a_{m}\dots a_{1}a_{0},\text{ and }(\alpha)_{\beta,j}:=a_{j}\;(j=0,1,\dots,m). |  |

For b ∈ { 0, 1, …, | N ⁡ ( β) | − 1 } b\in\{0,1,\dots,|N(\beta)|-1\}, denote

(1.4) |  | ℳ b ​ ( α, β, N):= #⁡ { 1 ≤ n ≤ N: ( α n) β, j ≠ b ​ for all possible j }, \mathcal{M}_{b}(\alpha,\beta,N):=\#\big\{1\leq n\leq N\colon(\alpha^{n})_{\beta,j}\neq b\;\text{for all possible $j$}\big\}, |  |

For the rest of this article, we assume α \alpha is not a root of unity as otherwise α n \alpha^{n} only have finitely many different value as n n changes. Recall that α, β ∈ 𝒪 K \alpha,\,\beta\in\mathcal{O}_{K} are *relatively prime*if the prime ideal decomposition

(1.5) |  | ( β) = 𝔭 1 e 1 ⋯ 𝔭 h e h (\beta)=\mathfrak{p}_{1}^{e_{1}}\cdots\mathfrak{p}_{h}^{e_{h}} |  |

satisfies that 𝔭 j ∤ α \mathfrak{p}_{j}\nmid\alpha (i.e. α ∉ 𝔭 j \alpha\notin\mathfrak{p}_{j}) for all j = 1, 2, …, h j=1,2,\dots,h. Our first result is an upper bound of ℳ b ​ ( α, β, N) \mathcal{M}_{b}(\alpha,\beta,N) (similar to ( 1.1)).

###### Theorem 1.5.

Suppose ( β, { 0, 1, …, | N ⁡ ( β) | − 1 }) (\beta,\,\{0,1,\dots,|N(\beta)|-1\}) is a CNS, β \beta is not divided by ramified primes and α \alpha is relatively prime to β \beta, then

(1.6) |  | ℳ b ​ ( α, β, N) ≤ C 1 ​ N σ ⁡ ( β) \mathcal{M}_{b}(\alpha,\beta,N)\leq C_{1}N^{\sigma(\beta)} |  |

holds for any digit b ∈ { 1, …, | N ⁡ ( β) | − 1 } b\in\{1,\dots,|N(\beta)|-1\}, where σ ⁡ ( β):= log ⁡ ( | N ⁡ ( β) | − 1) log ⁡ | N ⁡ ( β) | \sigma(\beta):=\frac{\log(|N(\beta)|-1)}{\log|N(\beta)|} and C 1 C_{1} is a constant depending only on β \beta.

Taking 𝒪 K = ℤ \mathcal{O}_{K}=\mathbb{Z}, α = 2 \alpha=2 and β = 3 \beta=3, Theorem 1.5 leads to ( 1.1) up to a constant multiple.

Kátai and Szabó [11] determined all the CNS for Gaussian integers. And the question of determining all CNS in quadratic number fields has been answered by [9, 10]. However, in extensions of higher degree, there is not necessarily a CNS. We say 𝒪 K \mathcal{O}_{K} is *monogenic*if there exists γ ∈ 𝒪 K \gamma\in\mathcal{O}_{K}, such that { 1, γ, …, γ d − 1 } \{1,\gamma,\dots,\gamma^{d-1}\} is an integer basis in 𝒪 K \mathcal{O}_{K}. It is clear from the definition that if ( β, { 0, 1, …, | N ⁡ ( β) | − 1 }) (\beta,\,\{0,1,\dots,|N(\beta)|-1\}) is a CNS in 𝒪 K \mathcal{O}_{K}, then 𝒪 K = ℤ ⁡ [β] \mathcal{O}_{K}=\mathbb{Z}[\beta], hence 𝒪 K \mathcal{O}_{K} must be monogenic. Although 𝒪 K = ℤ ⁡ [β] \mathcal{O}_{K}=\mathbb{Z}[\beta] does not implies ( β, { 0, 1, …, | N ⁡ ( β) | − 1 }) (\beta,\,\{0,1,\dots,|N(\beta)|-1\}) is a CNS in 𝒪 K \mathcal{O}_{K} in general, we do have the following criterion to determine whether the ring of integers has a CNS.

###### Theorem 1.6 (Kovács [15]).

Let K K be a finite extension of ℚ \mathbb{Q} with ring of integers 𝒪 K \mathcal{O}_{K} and [K: ℚ] = d ≥ 3 [K:\mathbb{Q}]=d\geq 3. There exists a CNS ( β, { 0, 1, …, | N ⁡ ( β) | − 1 }) (\beta,\,\{0,1,\dots,|N(\beta)|-1\}) in 𝒪 K \mathcal{O}_{K} if and only if 𝒪 K \mathcal{O}_{K} is monogenic.

However, for number fields with degree at least 3 3, their rings of integers are unlikely to be monogenic, see [8, 18, 22] for some recent results on monogeneity of number fields. In order to study those non-monogenic number fields, we introduce the concept of *β \beta -adic expansion*which is a natural generalization of p p -adic expansion.

###### Definition 1.7.

Given a number field K K and its ring of integers 𝒪 K \mathcal{O}_{K}. Fix β ∈ 𝒪 K \beta\in\mathcal{O}_{K} with norm | N ⁡ ( β) | > 1 |N(\beta)|>1 and a set of representatives 𝒟 β \mathcal{D}_{\beta} of the quotient group 𝒪 K / β ​ 𝒪 K \mathcal{O}_{K}/\beta\mathcal{O}_{K}. For every α ∈ 𝒪 K \alpha\in\mathcal{O}_{K}, the *β \beta -adic expansion*of α \alpha (with respect to 𝒟 β \mathcal{D}_{\beta}) is the unique sequence ( a i) i ∈ ℕ ∈ 𝒟 β ℕ (a_{i})_{i\in\mathbb{N}}\in\mathcal{D}_{\beta}^{\mathbb{N}} such that

(1.7) |  | α = lim i → ∞ a 0 + ⋯ + a i ​ β i \alpha=\lim_{i\rightarrow\infty}a_{0}+\cdots+a_{i}\beta^{i} |  |

with respect to 𝔭 \mathfrak{p} -adic topology for any prime ideal 𝔭 \mathfrak{p} in 𝒪 K \mathcal{O}_{K} dividing β \beta.

For instance, when β = 2 \beta=2 and D β = { 0, 3 } D_{\beta}=\{0,3\}, the 2 2 -adic expansion of 1 1 respect to { 0, 3 } \{0,3\} is

 | 1 = 3 + 3 ⋅ 2 1 + 3 ⋅ 2 3 + 3 ⋅ 2 5 + ⋯. 1=3+3\cdot 2^{1}+3\cdot 2^{3}+3\cdot 2^{5}+\cdots. |  |

It is not hard to see that the sequence ( a i) i ∈ ℕ (a_{i})_{i\in\mathbb{N}} is always ultimately periodic.

We note that some other generalizations of p p -adic expansion exist in the literature. Kátai [12] considered number systems in rings of integers, involving sets of representatives and Pethö [13] introduced number systems based on polynomials g ⁡ ( t) ∈ ℤ ⁡ [t] g(t)\in\mathbb{Z}[t].

When 𝒟 β \mathcal{D}_{\beta} is clear, denote

(1.8) |  | ( α) β:= ( a i) i ∈ ℕ, ( α) β, j:= a j ( j = 0, 1, …). (\alpha)_{\beta}:=(a_{i})_{i\in\mathbb{N}},\text{ $(\alpha)_{\beta,j}:=a_{j}$ ($j=0,1,\dots$).} |  |

and for b ∈ 𝒟 β b\in\mathcal{D}_{\beta} let

(1.9) |  | ℳ b ​ ( α, β, N):= #⁡ { 1 ≤ n ≤ N: ( α n) β, j ≠ b ​ for all possible j }. \mathcal{M}_{b}(\alpha,\beta,N):=\#\{1\leq n\leq N\colon(\alpha^{n})_{\beta,j}\neq b\text{ for all possible $j$}\}. |  |

We will see in Section 2 that β \beta -adic expansion is well-defined and closely related to the radix expansion in base β \beta, so the abuse of notations here should not cause confusion.

An upper bound of this ℳ b ​ ( α, β, N) \mathcal{M}_{b}(\alpha,\beta,N) is also obtained.

###### Theorem 1.8.

Let ( β) = 𝔭 1 e 1 ⋯ 𝔭 h e h (\beta)=\mathfrak{p}_{1}^{e_{1}}\cdots\mathfrak{p}_{h}^{e_{h}} satisfy that 𝔭 i \mathfrak{p}_{i} is unramified and N ⁡ ( 𝔭 i) = q i N(\mathfrak{p}_{i})=q_{i} for all i i, where q i q_{i} is the integer prime lying below 𝔭 i \mathfrak{p}_{i}. If α \alpha is relatively prime to β \beta, then

(1.10) |  | ℳ b ​ ( α, β, N) ≤ C 1 ​ N σ ⁡ ( β) \mathcal{M}_{b}(\alpha,\beta,N)\leq C_{1}N^{\sigma(\beta)} |  |

for any digit b ∈ 𝒟 β b\in\mathcal{D}_{\beta}, where σ ⁡ ( β):= log ⁡ ( | N ⁡ ( β) | − 1) log ⁡ | N ⁡ ( β) | \sigma(\beta):=\frac{\log(|N(\beta)|-1)}{\log|N(\beta)|} and C 1 C_{1} is a constant depending only on β \beta.

As a special case of Theorem 1.8, we obtain the following generalization of Narkiewicz’s result for coprime rational integers p p and q q.

###### Corollary 1.9.

Let p p, q q be two coprime rational integers and b ∈ { 0, 1, …, q − 1 } b\in\{0,1,\ldots,q-1\}. Then

 | ℳ b ​ ( p, q, N) ≤ C ​ N log ⁡ ( q − 1) / log ⁡ ( q) \mathcal{M}_{b}(p,q,N)\leq CN^{\log(q-1)/\log(q)} |  |

for some constant C C that can be effectively computed.

## 2. β \beta -adic expansion

We begin with reviewing basic facts on algebraic number fields and 𝔭 \mathfrak{p} -adic topology. Fix a number field K K and let 𝔭 \mathfrak{p} be a prime ideal of 𝒪 K \mathcal{O}_{K}, we define the 𝔭 \mathfrak{p} -adic valuation and 𝔭 \mathfrak{p} -adic absolute value on the field K K.

###### Definition 2.1.

The *𝔭 \mathfrak{p} -adic valuation*v 𝔭 v_{\mathfrak{p}} on K ∖ { 0 } K\setminus\{0\} is defined as follows:

1. (1)

For each integer a ∈ 𝒪 K ∖ { 0 } a\in\mathcal{O}_{K}\setminus\{0\}, let v 𝔭 ​ ( a) v_{\mathfrak{p}}(a) be the unique non-negative integer satisfying ( a) = 𝔭 v 𝔭 ​ ( a) ​ 𝔟 (a)=\mathfrak{p}^{v_{\mathfrak{p}}(a)}\mathfrak{b} with 𝔭 ∤ 𝔟 \mathfrak{p}\nmid\mathfrak{b}.

2. (2)

For x = a / b ∈ K ∖ { 0 } x=a/b\in K\setminus\{0\} with a, b ∈ 𝒪 K a,b\in\mathcal{O}_{K}, let v 𝔭 ​ ( x):= v 𝔭 ​ ( a) − v 𝔭 ​ ( b) v_{\mathfrak{p}}(x):=v_{\mathfrak{p}}(a)-v_{\mathfrak{p}}(b).

###### Remark 2.2.

(i) It is often convenient to set v 𝔭 ​ ( 0) = + ∞ v_{\mathfrak{p}}(0)=+\infty.
(ii) Note that the valuation v 𝔭 v_{\mathfrak{p}} on K ∖ { 0 } K\setminus\{0\} is well-defined: if a / b = a ′ / b ′ a/b=a^{\prime}/b^{\prime} for nonzero a, b, a ′ a,b,a^{\prime}, and b ′ b^{\prime} in 𝒪 K \mathcal{O}_{K}, then v 𝔭 ​ ( a) − v 𝔭 ​ ( b) = v 𝔭 ​ ( a ′) − v 𝔭 ​ ( b ′) v_{\mathfrak{p}}(a)-v_{\mathfrak{p}}(b)=v_{\mathfrak{p}}(a^{\prime})-v_{\mathfrak{p}}(b^{\prime}).
(iii) One can check that for all x, y ∈ K x,y\in K, v 𝔭 ​ ( x ​ y) = v 𝔭 ​ ( x) + v 𝔭 ​ ( y) v_{\mathfrak{p}}(xy)=v_{\mathfrak{p}}(x)+v_{\mathfrak{p}}(y) and

 | v 𝔭 ​ ( x + y) ≥ min ⁡ { v 𝔭 ​ ( x), v 𝔭 ​ ( y) }. v_{\mathfrak{p}}(x+y)\geq\min\{v_{\mathfrak{p}}(x),v_{\mathfrak{p}}(y)\}. |  |

A prime ideal 𝔭 \mathfrak{p} is called *ramified*, if the unique integer prime q ∈ 𝔭 q\in\mathfrak{p} satisfies that v 𝔭 ​ ( q) > 1 v_{\mathfrak{p}}(q)>1. There are only finitely many ramified primes in 𝒪 K \mathcal{O}_{K}.

###### Definition 2.3.

The *𝔭 \mathfrak{p} -adic absolute value*| ⋅ | 𝔭 |\cdot|_{\mathfrak{p}} on the field K K is defined as follows: fix a constant c ∈ ( 0, 1) c\in(0,1), set | α | 𝔭 = c v 𝔭 ​ ( α) |\alpha|_{\mathfrak{p}}=c^{v_{\mathfrak{p}}(\alpha)} for α ∈ K ∖ { 0 } \alpha\in K\setminus\{0\}, and | 0 | 𝔭 = 0 |0|_{\mathfrak{p}}=0. The *𝔭 \mathfrak{p} -adic topology*on K K is the topology induced by | ⋅ | 𝔭 |\cdot|_{\mathfrak{p}}.

For any β ∈ K \beta\in K, let β 1, …, β s \beta_{1},\dots,\beta_{s} be the roots of the minimal polynomial of β \beta, then the norm of β \beta is N ( β):= ( ∏ i = 1 s β i) [K: ℚ ( β)] N(\beta):=\big(\prod_{i=1}^{s}\beta_{i}\big)^{[K:\mathbb{Q}(\beta)]}. For an ideal 𝔞 ⊆ 𝒪 K \mathfrak{a}\subseteq\mathcal{O}_{K}, define its norm by N ⁡ ( 𝔞):= #⁡ ( 𝒪 K / 𝔞) N(\mathfrak{a}):=\#(\mathcal{O}_{K}/\mathfrak{a}). For principal ideals, we have N ⁡ ( β ​ 𝒪 K) = | N ⁡ ( β) | N(\beta\mathcal{O}_{K})=|N(\beta)|; see [6, Theorem 76]. In Theorem 1.8, we consider prime ideals 𝔭 i \mathfrak{p}_{i} whose norms are integer primes, this means they all have inertial degree 1 1.

###### Definition 2.4.

Let G G be an abelian group and H ⊆ G H\subseteq G be a subgroup. We say that a subset S ⊆ G S\subseteq G is a *set of representatives*of the quotient group G / H G/H if the map S → G / H: x ↦ x + H S\rightarrow G/H\colon x\mapsto x+H is a bijection.

###### Remark 2.5.

A set of representatives is usually not unique. In this article, we only consider the case that G / H G/H is finite, so there always exists a set of representatives. In general, if one assumes the axiom of choice, then every quotient group have sets of representatives.

From now on, let 𝒟 β \mathcal{D}_{\beta} denotes a set of representatives of 𝒪 K / β ​ 𝒪 K \mathcal{O}_{K}/\beta\mathcal{O}_{K}, then there is a natural bijection from 𝒟 β i \mathcal{D}_{\beta}^{i} to 𝒪 K / β i ​ 𝒪 K \mathcal{O}_{K}/\beta^{i}\mathcal{O}_{K}.

###### Lemma 2.6.

For any i ≥ 1 i\geq 1, the map

 | 𝒟 β i \displaystyle\mathcal{D}_{\beta}^{i} | → 𝒪 K / β i ​ 𝒪 K \displaystyle\rightarrow\mathcal{O}_{K}/\beta^{i}\mathcal{O}_{K} |  |

 | ( a 0, a 1, …, a i − 1) \displaystyle(a_{0},a_{1},\dots,a_{i-1}) | ↦ a 0 + a 1 ​ β + ⋯ + a i − 1 ​ β i − 1 + β i ​ 𝒪 K \displaystyle\mapsto a_{0}+a_{1}\beta+\cdots+a_{i-1}\beta^{i-1}+\beta^{i}\mathcal{O}_{K} |  |

is a bijection.

###### Proof.

When i = 1 i=1, the statement holds since 𝒟 β \mathcal{D}_{\beta} is a set of representatives of 𝒪 K / β ​ 𝒪 K \mathcal{O}_{K}/\beta\mathcal{O}_{K}. Assume the statement is valid for i i and we are going to prove it for i + 1 i+1. Note that #⁡ ( 𝒟 β i + 1) = | N ⁡ ( β) | i + 1 = | N ⁡ ( β i + 1) | = #⁡ ( 𝒪 K / β i + 1 ​ 𝒪 K) \#(\mathcal{D}_{\beta}^{i+1})=|N(\beta)|^{i+1}=|N(\beta^{i+1})|=\#\big(\mathcal{O}_{K}/\beta^{i+1}\mathcal{O}_{K}\big), so it suffice to prove that the map is injective.

Suppose ( a 0, …, a i) (a_{0},\dots,a_{i}) and ( b 0, …, b i) (b_{0},\dots,b_{i}) have the same image under the map, that is, ∑ j = 0 i a j ​ β j + β i + 1 ​ 𝒪 K = ∑ j = 0 i b j ​ β j + β i + 1 ​ 𝒪 K \sum_{j=0}^{i}a_{j}\beta^{j}+\beta^{i+1}\mathcal{O}_{K}=\sum_{j=0}^{i}b_{j}\beta^{j}+\beta^{i+1}\mathcal{O}_{K}. Then

 | ∑ j = 0 i − 1 ( a j − b j) ​ β j + ( a i − b i) ​ β i ∈ β i + 1 ​ 𝒪 K, \sum_{j=0}^{i-1}(a_{j}-b_{j})\beta^{j}+(a_{i}-b_{i})\beta^{i}\in\beta^{i+1}\mathcal{O}_{K}, |  |

so ∑ j = 0 i − 1 ( a j − b j) ​ β j ∈ β i ​ 𝒪 K \sum_{j=0}^{i-1}(a_{j}-b_{j})\beta^{j}\in\beta^{i}\mathcal{O}_{K}. By the induction hypothesis, we have ( a 0, …, a i − 1) = ( b 0, …, b i − 1) (a_{0},\dots,a_{i-1})=(b_{0},\dots,b_{i-1}). Therefore, we obtain a i ​ β i − b i ​ β i ∈ β i + 1 ​ 𝒪 K a_{i}\beta^{i}-b_{i}\beta^{i}\in\beta^{i+1}\mathcal{O}_{K}, hence a i − b i ∈ β ​ 𝒪 K a_{i}-b_{i}\in\beta\mathcal{O}_{K}. Since a i, b i ∈ 𝒟 β a_{i},b_{i}\in\mathcal{D}_{\beta}, their difference can not lie in β ​ 𝒪 K \beta\mathcal{O}_{K} unless they are the same. ∎

For each i ≥ 1 i\geq 1, we have two natural maps 𝒟 β i + 1 → 𝒟 β i \mathcal{D}_{\beta}^{i+1}\rightarrow\mathcal{D}_{\beta}^{i} and 𝒪 K / β i + 1 ​ 𝒪 K → 𝒪 K / β i ​ 𝒪 K \mathcal{O}_{K}/\beta^{i+1}\mathcal{O}_{K}\rightarrow\mathcal{O}_{K}/\beta^{i}\mathcal{O}_{K}, and it is easy to check that they commute with the map in Lemma 2.6. Taking inverse limits, we have a bijection

 | 𝒟 β ℕ \displaystyle\mathcal{D}_{\beta}^{\mathbb{N}} | ⟷ 𝒪 K, β:= lim ← 𝒪 K / β i ​ 𝒪 K \displaystyle\longleftrightarrow\mathcal{O}_{K,\beta}:=\lim_{\leftarrow}\mathcal{O}_{K}/\beta^{i}\mathcal{O}_{K} |  |

 | ( a i) i ∈ ℕ \displaystyle(a_{i})_{i\in\mathbb{N}} | ⟷ a 0 + a 1 ​ β + ⋯ + a i ​ β i + ⋯ \displaystyle\longleftrightarrow a_{0}+a_{1}\beta+\cdots+a_{i}\beta^{i}+\cdots |  |

Now 𝒪 K \mathcal{O}_{K} can be viewed as a subring of 𝒪 K, β \mathcal{O}_{K,\beta} via natural embedding, so for every α ∈ 𝒪 K \alpha\in\mathcal{O}_{K}, there is a sequence ( a i) i ∈ ℕ ∈ 𝒟 β ℕ (a_{i})_{i\in\mathbb{N}}\in\mathcal{D}_{\beta}^{\mathbb{N}} such that

 | α − ( a 0 + a 1 ​ β + ⋯ + a i ​ β i) ∈ β i + 1 ​ 𝒪 K \alpha-(a_{0}+a_{1}\beta+\cdots+a_{i}\beta^{i})\in\beta^{i+1}\mathcal{O}_{K} |  |

holds for each i ∈ ℕ i\in\mathbb{N}, and we have

(2.1) |  | α = lim i → ∞ a 0 + ⋯ + a i ​ β i \alpha=\lim_{i\rightarrow\infty}a_{0}+\cdots+a_{i}\beta^{i} |  |

with respect to 𝔭 \mathfrak{p} -adic topology for any prime ideal 𝔭 \mathfrak{p} in 𝒪 K \mathcal{O}_{K} dividing β \beta. If there exists another sequence ( b i) i ∈ ℕ ∈ 𝒟 β ℕ (b_{i})_{i\in\mathbb{N}}\in\mathcal{D}_{\beta}^{\mathbb{N}} such that

 | α = lim i → ∞ b 0 + b 1 ​ β + ⋯ + b i ​ β i \alpha=\lim_{i\rightarrow\infty}b_{0}+b_{1}\beta+\cdots+b_{i}\beta^{i} |  |

with respect to 𝔭 \mathfrak{p} -adic topology for some prime ideal 𝔭 \mathfrak{p} in 𝒪 K \mathcal{O}_{K} dividing β \beta, then bijectivity implies ( a i) i ∈ ℕ = ( b i) i ∈ ℕ (a_{i})_{i\in\mathbb{N}}=(b_{i})_{i\in\mathbb{N}}. Therefore we conclude that β \beta -adic expansion is well-defined.

Next we investigate the relation between β \beta -adic expansion and the radix expansion of base β \beta. When 𝒟 β = { 0, 1, …, | N ⁡ ( β) | − 1 } \mathcal{D}_{\beta}=\{0,1,\dots,|N(\beta)|-1\} and ( β, 𝒟 β) (\beta,\,\mathcal{D}_{\beta}) is a CNS, for any α ∈ 𝒪 K \alpha\in\mathcal{O}_{K}, we have α = a 0 + a 1 ​ β + ⋯ + a m ​ β m \alpha=a_{0}+a_{1}\beta+\cdots+a_{m}\beta^{m} for some a 0, …, a m ∈ 𝒟 a_{0},\ldots,a_{m}\in\mathcal{D}. Therefore if 𝒟 β \mathcal{D}_{\beta} is a set of representatives, then the β \beta -adic expansion of α \alpha with respect to is ( a 0, …, a m, 0, 0, 0, …) (a_{0},\ldots,a_{m},0,0,0,\ldots).

###### Lemma 2.7.

Let ( β) = 𝔭 1 e 1 ⋯ 𝔭 h e h (\beta)=\mathfrak{p}_{1}^{e_{1}}\cdots\mathfrak{p}_{h}^{e_{h}}. If ( β, { 0, 1, …, | N ⁡ ( β) | − 1 }) (\beta,\,\{0,1,\dots,|N(\beta)|-1\}) is a CNS in 𝒪 K \mathcal{O}_{K}, then | N ⁡ ( 𝔭 i) | = q i |N(\mathfrak{p}_{i})|=q_{i} for all i i, where q i q_{i} is the integer prime that lies below 𝔭 i \mathfrak{p}_{i}.

###### Proof.

Assume | N ⁡ ( 𝔭 i) | > q i |N(\mathfrak{p}_{i})|>q_{i} for some i. Then

 | | N ⁡ ( β) | = ∏ 1 ≤ i ≤ h | N ⁡ ( 𝔭 i) | e i > ∏ 1 ≤ i ≤ h q i e i, |N(\beta)|=\prod_{1\leq i\leq h}\Big|N(\mathfrak{p}_{i})\Big|^{e_{i}}>\prod_{1\leq i\leq h}q_{i}^{e_{i}}, |  |

hence ∏ 1 ≤ i ≤ h q i e i ∈ { 0, 1, …, | N ⁡ ( β) | − 1 } \prod_{1\leq i\leq h}q_{i}^{e_{i}}\in\mathcal{\{}0,1,\dots,|N(\beta)|-1\}. Since 𝔭 i | q i \mathfrak{p}_{i}\mid q_{i} for all i i, we have β | ∏ 1 ≤ i ≤ h q i e i \beta\mid\prod_{1\leq i\leq h}q_{i}^{e_{i}}, thus the map

 | { 0, 1, …, | N ⁡ ( β) | − 1 } \displaystyle\{0,1,\dots,|N(\beta)|-1\} | → 𝒪 K / β ​ 𝒪 K \displaystyle\rightarrow\mathcal{O}_{K}/\beta\mathcal{O}_{K} |  |

 | x \displaystyle x | ↦ x + β ​ 𝒪 K \displaystyle\mapsto x+\beta\mathcal{O}_{K} |  |

is not injective. Note that #​ 𝒟 β = | N ⁡ ( β) | = #⁡ ( 𝒪 K / β ​ 𝒪 K) \#\mathcal{D}_{\beta}=|N(\beta)|=\#(\mathcal{O}_{K}/\beta\mathcal{O}_{K}), so the above map is also not surjective. Therefore we can choose an element α ∈ 𝒪 K \alpha\in\mathcal{O}_{K} such that α ≢ x ⁡ ( mod ⁡ 1 ​ β) \alpha\not\equiv x\;(\mo 1\beta) for any x ∈ 𝒟 β x\in\mathcal{D}_{\beta}. However, since ( β, { 0, 1, …, | N ⁡ ( β) | − 1 }) (\beta,\,\{0,1,\dots,|N(\beta)|-1\}) is a CNS in 𝒪 K \mathcal{O}_{K}, we have α = c 0 + c 1 ​ β + ⋯ + c m ​ β m \alpha=c_{0}+c_{1}\beta+\cdots+c_{m}\beta^{m} for some c 0, …, c m ∈ 𝒟 β c_{0},\dots,c_{m}\in\mathcal{D}_{\beta}, which implies α ≡ c 0 ​ ( mod ⁡ 1 ​ β) \alpha\equiv c_{0}\;(\mo 1\beta), a contradiction. ∎

###### Lemma 2.8.

Let ( β) = 𝔭 1 e 1 ⋯ 𝔭 h e h (\beta)=\mathfrak{p}_{1}^{e_{1}}\cdots\mathfrak{p}_{h}^{e_{h}} and 𝒟 β = { 0, 1, …, | N ⁡ ( β) | − 1 } \mathcal{D}_{\beta}=\{0,1,\dots,|N(\beta)|-1\}. If ( β, 𝒟 β) (\beta,\,\mathcal{D}_{\beta}) is a CNS in 𝒪 K \mathcal{O}_{K}, and 𝔭 j \mathfrak{p}_{j} is unramified for all j j, then 𝒟 β \mathcal{D}_{\beta} is a set of representatives of 𝒪 K / β ​ 𝒪 K \mathcal{O}_{K}/\beta\mathcal{O}_{K}.

###### Proof.

Note that #⁡ ( 𝒪 K / β ​ 𝒪 K) = N ⁡ ( β ​ 𝒪 K) = | N ⁡ ( β) | = #​ 𝒟 β \#(\mathcal{O}_{K}/\beta\mathcal{O}_{K})=N(\beta\mathcal{O}_{K})=|N(\beta)|=\#\mathcal{D}_{\beta}, so we only need to show x − y ∉ β ​ 𝒪 K x-y\notin\beta\mathcal{O}_{K} for all distinct x, y ∈ 𝒟 β x,y\in\mathcal{D}_{\beta}. Assume that β | x − y \beta\mid x-y for some distinct x, y ∈ 𝒟 β x,y\in\mathcal{D}_{\beta}, then 𝔭 1 e 1 ⋯ 𝔭 h e h ∣ x − y \mathfrak{p}_{1}^{e_{1}}\cdots\mathfrak{p}_{h}^{e_{h}}\mid x-y. Since 𝔭 j \mathfrak{p}_{j} is unramified for all j j, this implies q 1 e 1 ⋯ q h e h ∣ x − y q_{1}^{e_{1}}\cdots q_{h}^{e_{h}}\mid x-y. Hence, combined with Lemma 2.7,

 | | N ( β) | = N ( 𝔭 1 e 1 ⋯ 𝔭 h e h) = N ( 𝔭 1) e 1 ⋯ N ( 𝔭 h) e h = q 1 e 1 ⋯ q h e h ∣ x − y, |N(\beta)|=N(\mathfrak{p}_{1}^{e_{1}}\cdots\mathfrak{p}_{h}^{e_{h}})=N(\mathfrak{p}_{1})^{e_{1}}\cdots N(\mathfrak{p}_{h})^{e_{h}}=q_{1}^{e_{1}}\cdots q_{h}^{e_{h}}\mid x-y, |  |

a contradiction. ∎

###### Corollary 2.9 (=Theorem 1.5).

Take 𝒟 β = { 0, 1, …, | N ⁡ ( β) | − 1 } \mathcal{D}_{\beta}=\{0,1,\dots,|N(\beta)|-1\}. If ( β, 𝒟 β) (\beta,\,\mathcal{D}_{\beta}) is a CNS, β \beta is not divided by ramified primes and α \alpha is relatively prime to β \beta, then ( 1.10) holds for any digit b ∈ { 1, …, | N ⁡ ( β) | − 1 } b\in\{1,\dots,|N(\beta)|-1\}.

###### Proof.

Note that if the radix expansion of α n \alpha^{n} in base β \beta is

 | α n = a 0 + a 1 ​ β + ⋯ + a m ​ β m, a j ∈ D β ​ ( j = 0, 1, …, m), \alpha^{n}=a_{0}+a_{1}\beta+\cdots+a_{m}\beta^{m},\quad a_{j}\in D_{\beta}\;(j=0,1,\dots,m), |  |

then we may add infinitely many zeroes to obtain its β \beta -adic expansion

 | ( a 0, a 1, …, a m, 0, 0, …). (a_{0},a_{1},\ldots,a_{m},0,0,\ldots). |  |

Therefore this corollary follows from Theorem 1.8, Lemma 2.7 and Lemma 2.8. ∎

###### Remark 2.10.

When b = 0 b=0, if the length of the radix expansion of α n \alpha^{n} is long enough, the we may use a similar inequality as ( 4) and follow the proof of Theorem 1.8 to deduce the desired bound.

## 3. 𝔭 \mathfrak{p} -adic interpolation of the sequence ( α n) n ∈ ℕ (\alpha^{n})_{n\in\mathbb{N}}

Let ( β) = 𝔭 1 e 1 ⋯ 𝔭 h e h (\beta)=\mathfrak{p}_{1}^{e_{1}}\cdots\mathfrak{p}_{h}^{e_{h}} be the prime ideal decomposition of ( β) (\beta) and α ∈ 𝒪 K \alpha\in\mathcal{O}_{K} be relatively prime to β \beta. Fix a prime ideal 𝔭 ∈ { 𝔭 1, …, 𝔭 h } \mathfrak{p}\in\{\mathfrak{p}_{1},\dots,\mathfrak{p}_{h}\}. In order to analyze the β \beta -adic expansion of α n \alpha^{n}, we need to introduce a powerful method called 𝔭 \mathfrak{p} -adic interpolation.

Recall that ( K, | ⋅ | 𝔭) (K,|\cdot|_{\mathfrak{p}}) is a valued field and the distance of x, y ∈ K x,y\in K is defined as | x − y | 𝔭 |x-y|_{\mathfrak{p}}. A valued field is said to be *complete*when every Cauchy sequence has a limit.

###### Proposition 3.1 ( [20, Chapter 1, (M)]).

Every valued field has a completion.

We denote the completion of K K with respect to the 𝔭 \mathfrak{p} -adic absolute value | ⋅ | 𝔭 |\cdot|_{\mathfrak{p}} by K 𝔭 K_{\mathfrak{p}}, and denote the extended absolute value again by | ⋅ | 𝔭 |\cdot|_{\mathfrak{p}}. Let

 | B ¯ ​ ( 0, 1) = { x ∈ K 𝔭: | x | 𝔭 ≤ 1 } \bar{B}(0,1)=\{x\in K_{\mathfrak{p}}\colon|x|_{\mathfrak{p}}\leq 1\} |  |

denote the closed unit ball of K 𝔭 K_{\mathfrak{p}}. It is clear that 𝒪 K ⊂ B ¯ ​ ( 0, 1) \mathcal{O}_{K}\subset\bar{B}(0,1).

Let ( α n) n ∈ ℕ (\alpha_{n})_{n\in\mathbb{N}} be a sequence of integers in 𝒪 K \mathcal{O}_{K}. A *𝔭 \mathfrak{p} -adic interpolation*of the sequence ( α n) n ∈ ℕ (\alpha_{n})_{n\in\mathbb{N}} is a continuous function G ⁡ ( x) G(x), defined in the unit ball B ¯ ​ ( 0, 1) \bar{B}(0,1), with G ⁡ ( n) = α n G(n)=\alpha_{n} for all n ∈ ℕ n\in\mathbb{N}.

###### Lemma 3.2.

If α ∈ 𝒪 K \alpha\in\mathcal{O}_{K} satisfies that 𝔭 ∤ α \mathfrak{p}\nmid\alpha, then there is a rational integer u 𝔭 u_{\mathfrak{p}} such that the sequence ( α n) n ∈ ℕ (\alpha^{n})_{n\in\mathbb{N}} can be divided into subsequences

 | ( α l ​ ( α u 𝔭) n) n ∈ ℕ, l = 0, 1, …, u 𝔭 − 1, (\alpha^{l}(\alpha^{u_{\mathfrak{p}}})^{n})_{n\in\mathbb{N}},\quad l=0,1,\dots,u_{\mathfrak{p}}-1, |  |

and for each l l, the sequence ( α l ​ ( α u 𝔭) n) n ∈ ℕ (\alpha^{l}(\alpha^{u_{\mathfrak{p}}})^{n})_{n\in\mathbb{N}} has an analytic 𝔭 \mathfrak{p} -adic interpolation G l G_{l}.

###### Proof.

Define the formal series

 | log ⁡ ( 1 + X):= ∑ n = 1 ∞ ( − 1) n + 1 ​ X n n \log(1+X):=\sum_{n=1}^{\infty}(-1)^{n+1}\frac{X^{n}}{n} |  |

Recall that for a power series f ⁡ ( X) = ∑ n = 0 ∞ a n ​ X n f(X)=\sum_{n=0}^{\infty}a_{n}X^{n} with coefficients in K 𝔭 K_{\mathfrak{p}}, the radius of convergence is defined as

(3.1) |  | r = 1 / ( lim sup n → + ∞ | a n | 𝔭), r=1/(\limsup_{n\rightarrow+\infty}|a_{n}|_{\mathfrak{p}}), |  |

then f ⁡ ( x) f(x) converges for every x ∈ K 𝔭 x\in K_{\mathfrak{p}} with | x | 𝔭 < r |x|_{\mathfrak{p}}<r, see [5, Proposition 5.4.1] for details.

Let a n = ( − 1) n + 1 / n a_{n}=(-1)^{n+1}/n, we claim that | a n | 𝔭 1 / n = c − v 𝔭 ( n) / n → 1 |a_{n}|_{\mathfrak{p}}^{1/n}=c^{-v_{\mathfrak{p}}(n)/n}\rightarrow 1 as n → ∞ n\rightarrow\infty, where c c is the constant fixed in Definition 2.3. To see this, let q q be the unique integer prime lying below 𝔭 \mathfrak{p} and n = q v q ​ ( n) ​ a n=q^{v_{q}(n)}a with q ∤ a q\nmid a, then v q ​ ( n) ≤ log ⁡ n v_{q}(n)\leq\log n; on the other hand,

(3.2) |  | ( n) = ( q) v q ​ ( n) ​ ( a) = ( 𝔭 v 𝔭 ​ ( q) ​ 𝔟) v q ​ ( n) ​ ( a), (n)=(q)^{v_{q}(n)}(a)=(\mathfrak{p}^{v_{\mathfrak{p}}(q)}\mathfrak{b})^{v_{q}(n)}(a), |  |

with 𝔭 ∤ 𝔟 \mathfrak{p}\nmid\mathfrak{b}, thus

(3.3) |  | v 𝔭 ​ ( n) = v 𝔭 ​ ( q) ​ v q ​ ( n) ≤ v 𝔭 ​ ( q) ​ log ⁡ n, v_{\mathfrak{p}}(n)=v_{\mathfrak{p}}(q)v_{q}(n)\leq v_{\mathfrak{p}}(q)\log n, |  |

which completes the proof of the claim. Hence, applying ( 3.1), we can define the 𝔭 \mathfrak{p} -adic logarithm of x ∈ B ⁡ ( 1, 1):= { x ∈ K 𝔭: | x − 1 | 𝔭 < 1 } x\in B(1,1):=\{x\in K_{\mathfrak{p}}\colon|x-1|_{\mathfrak{p}}<1\} as

 | log 𝔭 ⁡ ( x) = log 𝔭 ⁡ ( 1 + ( x − 1)) = ∑ n = 1 ∞ ( − 1) n + 1 ​ ( x − 1) n n. \log_{\mathfrak{p}}(x)=\log_{\mathfrak{p}}(1+(x-1))=\sum_{n=1}^{\infty}(-1)^{n+1}\frac{(x-1)^{n}}{n}. |  |

Define the formal series exp ⁡ ( X):= ∑ n = 0 ∞ X n / n! \bexp(X):=\sum_{n=0}^{\infty}X^{n}/n!. To calculate the radius of convergence ( 3.1), let a n = 1 / ( n!) a_{n}=1/(n!). Similar to ( 3.2) and ( 3.3), we have

(3.4) |  | v 𝔭 ​ ( n!) = v 𝔭 ​ ( q) ​ v q ​ ( n!) < v 𝔭 ​ ( q) ​ n q − 1, v_{\mathfrak{p}}(n!)=v_{\mathfrak{p}}(q)v_{q}(n!)<\frac{v_{\mathfrak{p}}(q)n}{q-1}, |  |

where we use v q ​ ( n!) ≤ n / ( q − 1) v_{q}(n!)\leq n/(q-1) in the last inequality (see [5, Lemma 5.7.4]). Hence,

 | | 1 / n! | 𝔭 1 / n = c − v 𝔭 ( n!) / n < c − v 𝔭 ( q) / ( q − 1), |1/n!|_{\mathfrak{p}}^{1/n}=c^{-v_{\mathfrak{p}}(n!)/n}<c^{-v_{\mathfrak{p}}(q)/(q-1)}, |  |

this implies that the radius of convergence r ≥ c v 𝔭 ​ ( q) / ( q − 1) r\geq c^{v_{\mathfrak{p}}(q)/(q-1)}. Therefore, we can define the 𝔭 \mathfrak{p} -adic exponential function as

(3.5) |  | exp 𝔭 ⁡ ( x):= ∑ n = 0 ∞ x n n!, x ∈ B ⁡ ( 0, c v 𝔭 ​ ( q) / ( q − 1)) \bexp_{\mathfrak{p}}(x):=\sum_{n=0}^{\infty}\frac{x^{n}}{n!},\quad x\in B(0,c^{v_{\mathfrak{p}}(q)/(q-1)}) |  |

Observe that for all x ∈ B ⁡ ( 1, c v 𝔭 ​ ( q)) x\in B(1,c^{v_{\mathfrak{p}}(q)}) and N ∈ ℕ N\in\mathbb{N},

(3.6) |  | | ∑ n = 1 N ( − 1) n + 1 ​ ( x − 1) n n | 𝔭 \displaystyle\Big|\sum_{n=1}^{N}(-1)^{n+1}\frac{(x-1)^{n}}{n}\Big|_{\mathfrak{p}} | ≤ max 1 ≤ n ≤ N ⁡ | x − 1 | 𝔭 n | n | 𝔭 \displaystyle\leq\max_{1\leq n\leq N}\frac{|x-1|_{\mathfrak{p}}^{n}}{|n|_{\mathfrak{p}}} |  |

 |  | = max 1 ≤ n ≤ N ⁡ ( c n ​ v 𝔭 ​ ( x − 1) / c v 𝔭 ​ ( n)) \displaystyle=\max_{1\leq n\leq N}\Big(c^{nv_{\mathfrak{p}}(x-1)}/c^{v_{\mathfrak{p}}(n)}\Big) |  |

 |  | ≤ max 1 ≤ n ≤ N ⁡ ( c n ​ v 𝔭 ​ ( x − 1) / c v 𝔭 ​ ( q) ​ log ⁡ n) ≤ | x − 1 | 𝔭, \displaystyle\leq\max_{1\leq n\leq N}\Big(c^{nv_{\mathfrak{p}}(x-1)}/c^{v_{\mathfrak{p}}(q)\log n}\Big)\leq|x-1|_{\mathfrak{p}}, |  |

where we use ( 3.3) in the third step. Hence, for each x ∈ B ⁡ ( 1, c v 𝔭 ​ ( q)) x\in B(1,c^{v_{\mathfrak{p}}(q)}), we have

(3.7) |  | | log 𝔭 ⁡ ( x) | 𝔭 ≤ | x − 1 | 𝔭. |\log_{\mathfrak{p}}(x)|_{\mathfrak{p}}\leq|x-1|_{\mathfrak{p}}. |  |

Thus, by ( 3.5) and ( 3.7), log 𝔭 ⁡ ( x) \log_{\mathfrak{p}}(x) is in the domain of exp 𝔭 \bexp_{\mathfrak{p}} when x ∈ B ¯ ​ ( 1, c v 𝔭 ​ ( q) + 1) x\in\bar{B}(1,c^{v_{\mathfrak{p}}(q)+1}).

Note that 𝒪 K / 𝔭 v 𝔭 ​ ( q) + 1 \mathcal{O}_{K}/\mathfrak{p}^{v_{\mathfrak{p}}(q)+1} is a finite additive group, the sequence α, α 2, …, α n, … \alpha,\alpha^{2},\dots,\alpha^{n},\dots must satisfy that there exist two integers n, m n,m with 0 ≤ n < m 0\leq n<m such that

 | α m + 𝒪 K / 𝔭 v 𝔭 ​ ( q) + 1 = α n + 𝒪 K / 𝔭 v 𝔭 ​ ( q) + 1, \alpha^{m}+\mathcal{O}_{K}/\mathfrak{p}^{v_{\mathfrak{p}}(q)+1}=\alpha^{n}+\mathcal{O}_{K}/\mathfrak{p}^{v_{\mathfrak{p}}(q)+1}, |  |

thus α n ​ ( α m − n − 1) ∈ 𝔭 v 𝔭 ​ ( q) + 1 \alpha^{n}(\alpha^{m-n}-1)\in\mathfrak{p}^{v_{\mathfrak{p}}(q)+1}. By the condition 𝔭 ∤ α \mathfrak{p}\nmid\alpha, we have α m − n − 1 ∈ 𝔭 v 𝔭 ​ ( q) + 1 \alpha^{m-n}-1\in\mathfrak{p}^{v_{\mathfrak{p}}(q)+1}. Therefore, there is an integer u 𝔭 u_{\mathfrak{p}} such that | α u 𝔭 − 1 | 𝔭 ≤ c v 𝔭 ​ ( q) + 1 |\alpha^{u_{\mathfrak{p}}}-1|_{\mathfrak{p}}\leq c^{v_{\mathfrak{p}}(q)+1}.

By ( 3.7), for | x | 𝔭 ≤ 1 |x|_{\mathfrak{p}}\leq 1,

(3.8) |  | | x ​ log 𝔭 ⁡ ( α u 𝔭) | 𝔭 = | x | 𝔭 | ​ log 𝔭 ⁡ ( α u 𝔭) | 𝔭 ≤ 1 ⋅ | α u 𝔭 − 1 | 𝔭 ≤ c v 𝔭 ​ ( q) + 1. |x\log_{\mathfrak{p}}(\alpha^{u_{\mathfrak{p}}})|_{\mathfrak{p}}=|x|_{\mathfrak{p}}|\log_{\mathfrak{p}}(\alpha^{u_{\mathfrak{p}}})|_{\mathfrak{p}}\leq 1\cdot|\alpha^{u_{\mathfrak{p}}}-1|_{\mathfrak{p}}\leq c^{v_{\mathfrak{p}}(q)+1}. |  |

Combined with ( 3.5), we obtain that exp 𝔭 ⁡ ( x ​ log 𝔭 ⁡ ( α u 𝔭)) \bexp_{\mathfrak{p}}(x\log_{\mathfrak{p}}(\alpha^{u_{\mathfrak{p}}})) is well-defined on the closed ball B ¯ ​ ( 0, 1) \bar{B}(0,1). This expression will serve as the definition of ( α u 𝔭) x (\alpha^{u_{\mathfrak{p}}})^{x}, x ∈ B ¯ ​ ( 0, 1) x\in\bar{B}(0,1).

Now take G l ​ ( x) = α l ​ ( α u 𝔭) x G_{l}(x)=\alpha^{l}(\alpha^{u_{\mathfrak{p}}})^{x}, x ∈ B ¯ ​ ( 0, 1) x\in\bar{B}(0,1), for l ∈ { 0, 1, …, u 𝔭 − 1 } l\in\{0,1,\dots,u_{\mathfrak{p}}-1\}, which is the analytic 𝔭 \mathfrak{p} -adic interpolation that we want. ∎

###### Corollary 3.3.

Let ( β) = 𝔭 1 e 1 ⋯ 𝔭 h e h (\beta)=\mathfrak{p}_{1}^{e_{1}}\cdots\mathfrak{p}_{h}^{e_{h}} and α ∈ 𝒪 K \alpha\in\mathcal{O}_{K} be relatively prime to β \beta. Let u 𝔭 i u_{\mathfrak{p}_{i}} ( i = 1, 2, …, h i=1,2,\dots,h) be as in Lemma 3.2 and u = ∏ i = 1 h u 𝔭 i u=\prod_{i=1}^{h}u_{\mathfrak{p}_{i}}. Then G l ​ ( x):= α l ​ ( α u) x G_{l}(x):=\alpha^{l}(\alpha^{u})^{x} is an analytic 𝔭 i \mathfrak{p}_{i} -adic interpolation of ( α l ​ ( α u) n) n ∈ ℕ (\alpha^{l}(\alpha^{u})^{n})_{n\in\mathbb{N}} for all i = 1, 2, …, h i=1,2,\dots,h and l = 0, 1, …, u − 1 l=0,1,\dots,u-1.

###### Proof.

Let q i q_{i} be the unique integer prime lying below 𝔭 i \mathfrak{p}_{i} for i = 1, 2, …, h i=1,2,\dots,h. By the definition of u 𝔭 i u_{\mathfrak{p}_{i}}, we have

 | α u 𝔭 i + 𝒪 K / 𝔭 i v 𝔭 i ​ ( q i) + 1 = 1 + 𝒪 K / 𝔭 i v 𝔭 i ​ ( q i) + 1. \alpha^{u_{\mathfrak{p}_{i}}}+\mathcal{O}_{K}/\mathfrak{p}_{i}^{v_{\mathfrak{p}_{i}}(q_{i})+1}=1+\mathcal{O}_{K}/\mathfrak{p}_{i}^{v_{\mathfrak{p}_{i}}(q_{i})+1}. |  |

Hence, for all i ∈ { 1, 2, …, h } i\in\{1,2,\dots,h\}, α u + 𝒪 K / 𝔭 i v 𝔭 i ​ ( q i) + 1 = 1 + 𝒪 K / 𝔭 i v 𝔭 i ​ ( q i) + 1 \alpha^{u}+\mathcal{O}_{K}/\mathfrak{p}_{i}^{v_{\mathfrak{p}_{i}}(q_{i})+1}=1+\mathcal{O}_{K}/\mathfrak{p}_{i}^{v_{\mathfrak{p}_{i}}(q_{i})+1}, that is,

(3.9) |  | | α u − 1 | 𝔭 i ≤ c v 𝔭 i ​ ( q i) + 1. |\alpha^{u}-1|_{\mathfrak{p}_{i}}\leq c^{v_{\mathfrak{p}_{i}}(q_{i})+1}. |  |

Therefore, exp 𝔭 i ⁡ ( x ​ log 𝔭 i ⁡ ( α u)) \bexp_{\mathfrak{p}_{i}}(x\log_{\mathfrak{p}_{i}}(\alpha^{u})) is well-defined for | x | 𝔭 i ≤ 1 |x|_{\mathfrak{p}_{i}}\leq 1 (the discussion is similar to the one in the proof of Lemma 3.2), and this expression will serve as the definition of ( α u) x (\alpha^{u})^{x}, | x | 𝔭 i ≤ 1 |x|_{\mathfrak{p}_{i}}\leq 1. ∎

###### Remark 3.4.

One can think of G l ​ ( x) = α l ​ ( α u) x G_{l}(x)=\alpha^{l}(\alpha^{u})^{x} as a formal function, which is well-defined on the closed ball B ¯ ​ ( 0, 1) \bar{B}(0,1) in K 𝔭 K_{\mathfrak{p}} for all 𝔭 ∈ { 𝔭 1, …, 𝔭 h } \mathfrak{p}\in\{\mathfrak{p}_{1},\dots,\mathfrak{p}_{h}\}.

## 4. Proof of Theorem 1.8

We begin with a simple lemma.

###### Lemma 4.1.

Let G l ​ ( x) = α l ​ ( α u) x G_{l}(x)=\alpha^{l}(\alpha^{u})^{x} and { 𝔭 1, …, 𝔭 h } \{\mathfrak{p}_{1},\dots,\mathfrak{p}_{h}\} be as in Corollary 3.3. Then there exist integers n 0, m 0 n_{0},m_{0} such that

(4.1) |  | | G l ​ ( x) − G l ​ ( y) | 𝔭 ≥ c n 0 ​ | x − y | 𝔭, |G_{l}(x)-G_{l}(y)|_{\mathfrak{p}}\geq c^{n_{0}}|x-y|_{\mathfrak{p}}, |  |

for all x, y x,y with | x − y | 𝔭 ≤ c m 0 |x-y|_{\mathfrak{p}}\leq c^{m_{0}} and 𝔭 ∈ { 𝔭 1, …, 𝔭 h } \mathfrak{p}\in\{\mathfrak{p}_{1},\dots,\mathfrak{p}_{h}\}.

###### Proof.

Fix a 𝔭 ∈ { 𝔭 1, …, 𝔭 h } \mathfrak{p}\in\{\mathfrak{p}_{1},\dots,\mathfrak{p}_{h}\}, we claim that there exist integers n 𝔭, m 𝔭 > 0 n_{\mathfrak{p}},m_{\mathfrak{p}}>0 such that for every pair of distinct x, y ∈ ¯ ​ B ​ ( 0, 1) x,y\in\bm{\bar{}}B(0,1),

(4.2) |  | if | x − y | 𝔭 ≤ c m 𝔭, then ​ | G l ​ ( x) − G l ​ ( y) | 𝔭 ≥ c n 𝔭 ​ | x − y | 𝔭. \text{if $|x-y|_{\mathfrak{p}}\leq c^{m_{\mathfrak{p}}}$, then }|G_{l}(x)-G_{l}(y)|_{\mathfrak{p}}\geq c^{n_{\mathfrak{p}}}|x-y|_{\mathfrak{p}}. |  |

Assume that for every n n, there is a pair of distinct points x n x_{n}, y n y_{n} satisfying

(4.3) |  | | x n − y n | 𝔭 ≤ 1 n, | G l ​ ( x n) − G l ​ ( y n) | 𝔭 < 1 n ​ | x n − y n | 𝔭. |x_{n}-y_{n}|_{\mathfrak{p}}\leq\frac{1}{n},\quad|G_{l}(x_{n})-G_{l}(y_{n})|_{\mathfrak{p}}<\frac{1}{n}|x_{n}-y_{n}|_{\mathfrak{p}}. |  |

Since ¯ ​ B ​ ( 0, 1) \bm{\bar{}}B(0,1) is compact (similar to [5, Corollary 4.2.7]), ( x n) n ≥ 1 (x_{n})_{n\geq 1} has a convergent subsequence ( x n j) j ≥ 1 (x_{n_{j}})_{j\geq 1}, we assume that x n j → x 0 x_{n_{j}}\rightarrow x_{0}. We must have y n j → x 0 y_{n_{j}}\rightarrow x_{0} as well. Suppose that G l ​ ( z) = ∑ n = 0 ∞ c n ​ z n G_{l}(z)=\sum_{n=0}^{\infty}c_{n}z^{n} since G l G_{l} is analytic, then

(4.4) |  |  | G l ​ ( x n j) − G l ​ ( y n j) x n j − y n j = ∑ n = 0 ∞ c n ​ ( x n j n − y n j n) x n j − y n j \displaystyle\frac{G_{l}(x_{n_{j}})-G_{l}(y_{n_{j}})}{x_{n_{j}}-y_{n_{j}}}=\frac{\sum_{n=0}^{\infty}c_{n}(x_{n_{j}}^{n}-y_{n_{j}}^{n})}{x_{n_{j}}-y_{n_{j}}} |  |

 | = \displaystyle= | ∑ n = 0 ∞ c n ​ ( x n j n − 1 + x n j n − 2 ​ y n j + ⋯ + y n j n − 1) → ∑ n = 0 ∞ c n ​ n ​ x 0 n − 1 = G l ′ ​ ( x 0), \displaystyle\sum_{n=0}^{\infty}c_{n}(x_{n_{j}}^{n-1}+x_{n_{j}}^{n-2}y_{n_{j}}+\cdots+y_{n_{j}}^{n-1})\rightarrow\sum_{n=0}^{\infty}c_{n}nx_{0}^{n-1}=G_{l}^{\prime}(x_{0}), |  |

as j → + ∞ j\rightarrow+\infty. But, by ( 4.3),

 | | G l ​ ( x n) − G l ​ ( y n) x n − y n | p < 1 n, \Big|\frac{G_{l}(x_{n})-G_{l}(y_{n})}{x_{n}-y_{n}}\Big|_{p}<\frac{1}{n}, |  |

combined with ( 4.4), we have G l ′ ​ ( x 0) = 0 G_{l}^{\prime}(x_{0})=0. However, this is impossible, one can check that:

 | G l ′ ​ ( x) \displaystyle G_{l}^{\prime}(x) | = α l ​ ( ∑ n = 0 ∞ ( x ​ log 𝔭 ⁡ ( α u)) n n!) ′ \displaystyle=\alpha^{l}\Big(\sum_{n=0}^{\infty}\frac{\big(x\log_{\mathfrak{p}}(\alpha^{u})\big)^{n}}{n!}\Big)^{\prime} |  |

 |  | = α l ​ ∑ n = 1 ∞ ( log 𝔭 ⁡ ( α u)) n ​ x n − 1 ( n − 1)! \displaystyle=\alpha^{l}\sum_{n=1}^{\infty}\frac{\big(\log_{\mathfrak{p}}(\alpha^{u})\big)^{n}x^{n-1}}{(n-1)!} |  |

(4.5) |  |  | = ( α l ​ log 𝔭 ⁡ ( α u)) ​ ( α u) x ≠ 0, \displaystyle=\big(\alpha^{l}\log_{\mathfrak{p}}(\alpha^{u})\big)(\alpha^{u})^{x}\neq 0, |  |

for all x ∈ ¯ ​ B ​ ( 0, 1) x\in\bm{\bar{}}B(0,1). This completes the proof of the claim.

Let m 0 = max ⁡ { m 𝔭: 𝔭 ∈ { 𝔭 1, …, 𝔭 h } } m_{0}=\max\big\{m_{\mathfrak{p}}\colon\mathfrak{p}\in\{\mathfrak{p}_{1},\dots,\mathfrak{p}_{h}\}\big\} and n 0 = max ⁡ { n 𝔭: 𝔭 ∈ { 𝔭 1, …, 𝔭 h } } n_{0}=\max\big\{n_{\mathfrak{p}}\colon\mathfrak{p}\in\{\mathfrak{p}_{1},\dots,\mathfrak{p}_{h}\}\big\}. This completes the proof of the lemma. ∎

Fix a digit b ∈ 𝒟 β b\in\mathcal{D}_{\beta}, for a word ( a j) j = 0 k − 1 ∈ ( 𝒟 β ∖ { b }) k (a_{j})_{j=0}^{k-1}\in(\mathcal{D}_{\beta}\setminus\{b\})^{k}, denote

 | [( a j) j = 0 k − 1] ( l):= { 0 ≤ n ≤ | N ( β) | k − 1: ( α l ( α u) n) β, j = a j for j = 0, …, k − 1 }, \big[(a_{j})_{j=0}^{k-1}\big]^{(l)}:=\big\{0\leq n\leq|N(\beta)|^{k}-1\colon\big(\alpha^{l}(\alpha^{u})^{n}\big)_{\beta,j}=a_{j}\text{ for }j=0,\dots,k-1\big\}, |  |

where u u is as in Corollary 3.3, l = 0, 1, …, u − 1 l=0,1,\dots,u-1 and the definition of ( ⋅) β, j (\cdot)_{\beta,j} is as in ( 1.8). By the definition of ℳ b ​ ( α, β, u ​ | N ⁡ ( β) | k) \mathcal{M}_{b}\big(\alpha,\beta,u|N(\beta)|^{k}\big) (see ( 1.9)), we have

 | ℳ b ​ ( α, β, u ​ | N ⁡ ( β) | k) ≤ \displaystyle\mathcal{M}_{b}\big(\alpha,\beta,u|N(\beta)|^{k}\big)\leq | #{ 1 ≤ n ≤ u | N ( β) | k: ( α n) β, j ≠ b for j = 0, …, k − 1 } \displaystyle\#\big\{1\leq n\leq u|N(\beta)|^{k}\colon(\alpha^{n})_{\beta,j}\neq b\text{ for }j=0,\dots,k-1\big\} |  |

(4.6) |  | ≤ \displaystyle\leq | ∑ l = 1 u ∑ ( a i) i = 0 k − 1 ∈ ( 𝒟 β ∖ { b }) k #​ [( a j) j = 0 k − 1] ( l). \displaystyle\sum_{l=1}^{u}\sum_{(a_{i})_{i=0}^{k-1}\in\big(\mathcal{D}_{\beta}\setminus\{b\}\big)^{k}}\#\big[(a_{j})_{j=0}^{k-1}\big]^{(l)}. |  |

We are now going to estimate #​ [( a j) j = 0 k − 1] ( l) \#\big[(a_{j})_{j=0}^{k-1}\big]^{(l)}. Let q j q_{j} be the unique integer prime lying below 𝔭 j \mathfrak{p}_{j} for j = 1, 2, …, h j=1,2,\dots,h. By the condition N ⁡ ( 𝔭 j) = q j N(\mathfrak{p}_{j})=q_{j}, we have

(4.7) |  | | N ⁡ ( β) | = ∏ j = 1 h N ​ ( 𝔭 j) e j = ∏ j = 1 h q j e j. |N(\beta)|=\prod_{j=1}^{h}N(\mathfrak{p}_{j})^{e_{j}}=\prod_{j=1}^{h}q_{j}^{e_{j}}. |  |

Consider the partition

(4.8) |  | [( a j) j = 0 k − 1] ( l) = ⋃ i = 0 | N ⁡ ( β) | m 0 − 1 [( a j) j = 0 k − 1] i ( l) \big[(a_{j})_{j=0}^{k-1}\big]^{(l)}=\bigcup_{i=0}^{|N(\beta)|^{m_{0}}-1}\big[(a_{j})_{j=0}^{k-1}\big]^{(l)}_{i} |  |

where

 | [( a j) j = 0 k − 1] ( l) i:= { 0 ≤ n ≤ | N ( β) | k − 1: n ∈ [( a j) j = 0 k − 1] ( l) and n ≡ i ( mod 1 | N ( β) | m 0) }, \begin{split}\big[(a_{j})_{j=0}^{k-1}\big]^{(l)}_{i}:=\Big\{0\leq n\leq|N(\beta)|^{k}-1\colon&n\in\big[(a_{j})_{j=0}^{k-1}\big]^{(l)}\\ &\text{ and }n\equiv i\,(\mo 1|N(\beta)|^{m_{0}})\Big\},\end{split} |  |

and m 0 m_{0} is defined as in Lemma 4.1. Suppose that n, m n,m are in [( a j) j = 0 k − 1] i ( l) \big[(a_{j})_{j=0}^{k-1}\big]^{(l)}_{i}, then

 | α l ​ ( α u) n + β k ​ 𝒪 K = ∑ i = 0 k − 1 a i ​ β i + β k ​ 𝒪 K = α l ​ ( α u) m + β k ​ 𝒪 K, \alpha^{l}(\alpha^{u})^{n}+\beta^{k}\mathcal{O}_{K}=\sum_{i=0}^{k-1}a_{i}\beta^{i}+\beta^{k}\mathcal{O}_{K}=\alpha^{l}(\alpha^{u})^{m}+\beta^{k}\mathcal{O}_{K}, |  |

that is, β k | ( α l ​ ( α u) n − α l ​ ( α u) m) \beta^{k}\mid\big(\alpha^{l}(\alpha^{u})^{n}-\alpha^{l}(\alpha^{u})^{m}\big). Recall that ( β) = 𝔭 1 e 1 ⋯ 𝔭 h e h (\beta)=\mathfrak{p}_{1}^{e_{1}}\cdots\mathfrak{p}_{h}^{e_{h}}, we have

(4.9) |  | | α l ​ ( α u) n − α l ​ ( α u) m | 𝔭 j ≤ c k ​ e j, \Big|\alpha^{l}(\alpha^{u})^{n}-\alpha^{l}(\alpha^{u})^{m}\Big|_{\mathfrak{p}_{j}}\leq c^{ke_{j}}, |  |

for all j ∈ { 0, 1, …, h } j\in\{0,1,\dots,h\}. Moreover, n, m ∈ [( a j) j = 0 k − 1] i ( l) n,m\in\big[(a_{j})_{j=0}^{k-1}\big]^{(l)}_{i} also implies that

 | n ≡ m ⁡ ( mod ⁡ 1 ​ | N ⁡ ( β) | m 0), n\equiv m\,(\mo 1|N(\beta)|^{m_{0}}), |  |

that is, | N ⁡ ( β) | m 0 | n − m |N(\beta)|^{m_{0}}\mid n-m. Combined this with ( 4.7), we have

 | | n − m | 𝔭 j ≤ c m 0, |n-m|_{\mathfrak{p}_{j}}\leq c^{m_{0}}, |  |

for all j ∈ { 0, 1, …, h } j\in\{0,1,\dots,h\}. Hence, by Lemma 4.1 and ( 4.1), we have

 | | n − m | 𝔭 j ≤ c − n 0 ​ c k ​ e j, |n-m|_{\mathfrak{p}_{j}}\leq c^{-n_{0}}c^{ke_{j}}, |  |

for all j ∈ { 0, 1, …, h } j\in\{0,1,\dots,h\}. This implies that ∏ j = 1 h 𝔭 j k ​ e j − n 0 | ( n − m) \prod_{j=1}^{h}\mathfrak{p}_{j}^{ke_{j}-n_{0}}|(n-m). Recall the condition that 𝔭 j \mathfrak{p}_{j} is unramified for all j j, this implies that

 | ∏ j = 1 h q j k ​ e j − n 0 | ( n − m), \prod_{j=1}^{h}q_{j}^{ke_{j}-n_{0}}\mid(n-m), |  |

where q i q_{i} is the integer prime that lies in 𝔭 i \mathfrak{p}_{i}. Hence, the distance

 | | n − m | ≥ ∏ j = 1 h q j k ​ e j − n 0, |n-m|\geq\prod_{j=1}^{h}q_{j}^{ke_{j}-n_{0}}, |  |

which holds for each pair of distinct n, m ∈ [( a j) j = 0 k − 1] i ( l) n,m\in\big[(a_{j})_{j=0}^{k-1}\big]_{i}^{(l)}. Therefore,

(4.10) |  | #​ [( a j) j = 0 k − 1] i ( l) ≤ | N ⁡ ( β) | k / ( ∏ j = 1 h q j k ​ e j − n 0). \#\big[(a_{j})_{j=0}^{k-1}\big]_{i}^{(l)}\leq|N(\beta)|^{k}/\Big(\prod_{j=1}^{h}q_{j}^{ke_{j}-n_{0}}\Big). |  |

On the other hand, by ( 4.7),

(4.11) |  | | N ⁡ ( β) | k = ∏ j = 1 h q j k ​ e j. |N(\beta)|^{k}=\prod_{j=1}^{h}q_{j}^{ke_{j}}. |  |

Applying ( 4.11) to ( 4.10), we have

(4.12) |  | #​ [( a j) j = 0 k − 1] i ( l) ≤ C ~ 0, \#\big[(a_{j})_{j=0}^{k-1}\big]_{i}^{(l)}\leq\widetilde{C}_{0}, |  |

where C ~ 0:= ( ∏ j = 1 h q j) n 0 \widetilde{C}_{0}:=\big(\prod_{j=1}^{h}q_{j}\big)^{n_{0}}. Applying ( 4.12), ( 4.8) to ( 4), we obtain

(4.13) |  | ℳ b ​ ( α, β, u ​ | N ⁡ ( β) | k) ≤ C 0 ⋅ | N ⁡ ( β) | k ​ σ ​ ( β) \mathcal{M}_{b}\big(\alpha,\beta,u|N(\beta)|^{k}\big)\leq C_{0}\cdot\big|N(\beta)\big|^{k\sigma(\beta)} |  |

where σ ⁡ ( β):= log ⁡ ( | N ⁡ ( β) | − 1) log ⁡ | N ⁡ ( β) | \sigma(\beta):=\frac{\log(|N(\beta)|-1)}{\log|N(\beta)|} and C 0:= u ​ | N ⁡ ( β) | m 0 ​ C ~ 0 C_{0}:=u|N(\beta)|^{m_{0}}\widetilde{C}_{0}. For an integer N ∈ ℕ N\in\mathbb{N}, there is an integer k ∈ ℕ k\in\mathbb{N} such that | N ⁡ ( β) | k − 1 ≤ N ≤ | N ⁡ ( β) | k |N(\beta)|^{k-1}\leq N\leq|N(\beta)|^{k}; then, by ( 4.13), we have

 | ℳ b ​ ( α, β, N) ≤ ℳ b ​ ( α, β, u ​ | N ⁡ ( β) | k) ≤ C 1 ​ N σ ⁡ ( β), \begin{split}\mathcal{M}_{b}\big(\alpha,\beta,N\big)\leq\mathcal{M}_{b}\big(\alpha,\beta,u|N(\beta)|^{k}\big)\leq C_{1}N^{\sigma(\beta)},\end{split} |  |

where C 1:= C 0 ​ | N ⁡ ( β) | σ ⁡ ( β) C_{1}:=C_{0}|N(\beta)|^{\sigma(\beta)}. This completes the proof.

## Acknowledgements

We thank Wladyslaw Narkiewicz for pointing out errors in the previous version of this article. We thank the referee for helpful suggestions. This work was supported in part by NSFC No. 12471085, Science and Technology Commission of Shanghai Municipality (STCSM) No. 22DZ2229014, NSFC No. 12401006, and Guangdong Basic and Applied Basic Research Foundation No. 2023A1515110272.

## Declaration of interests

There are no relevant financial or non-financial competing interests to report.

## References

- [1] G. Bonuccelli, L. Colucci, and E. de Faria. On the Erdös-Sloane and shifted Sloane persistence problems. J. Integer Seq., 23(10):Art. 20.10.7, 30, 2020.
- [2] E. de Faria and C. Tresser. On Sloane’s persistence problem. Exp. Math., 23(4):363–382, 2014.
- [3] T. Dupuy and D. E. Weirich. Bits of 3 n 3^{n} in binary, Wieferich primes and a conjecture of Erdös. J. Number Theory, 158:268–280, 2016.
- [4] P. Erdős. Some unconventional problems in number theory. Number 61, pages 73–82. 1979. Luminy Conference on Arithmetic.
- [5] F. Q. Gouvêa. p p -adic numbers. Universitext. Springer, Cham, third edition, [2020] ©2020.
- [6] E. Hecke. Lectures on the theory of algebraic numbers, volume 77 of Graduate Texts in Mathematics. Springer-Verlag, New York-Berlin, 1981. Translated from the German by George U. Brauer, Jay R. Goldman and R. Kotzen.
- [7] S. T. Holdum, F. R. Klausen, and P. M. Reichstein Rasmussen. Powers in prime bases and a problem on central binomial coefficients. Integers, 15:Paper No. A43, 13, 2015.
- [8] B. Jhorar, and S. K. Khanduja. On the index theorem of Ore. Manuscripta Math., 153(1-2):299–313, 2017.
- [9] I. Kátai and B. Kovács. Kanonische Zahlensysteme in der Theorie der quadratischen algebraischen Zahlen. Acta Sci. Math. (Szeged), 42(1-2):99–107, 1980.
- [10] I. Kátai and B. Kovács. Canonical number systems in imaginary quadratic fields. Acta Math. Acad. Sci. Hungar., 37(1-3):159–164, 1981.
- [11] I. Kátai and J. Szabó. Canonical number systems for complex integers. Acta Sci. Math. (Szeged), 37(3-4):255–260, 1975.
- [12] I. Kátai. Construction of number systems in algebraic number fields. Ann. Univ. Sci. Budapest. Sect. Comput., 18(3-4):103–107, 1999.
- [13] A. Pethö. On a polynomial transformation and its application to the construction of a public key cryptosystem. Computational number theory (Debrecen), 31–43, 1989.
- [14] R. E. Kennedy and C. Cooper. A generalization of a result by Narkiewicz concerning large digits of powers. Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat., 11:36–40, 2000.
- [15] B. Kovács. Canonical number systems in algebraic number fields. Acta Math. Acad. Sci. Hungar., 37(4):405–407, 1981.
- [16] J. C. Lagarias. Ternary expansions of powers of 2. J. Lond. Math. Soc. (2), 79(3):562–588, 2009.
- [17] P. Leonetti and C. Sanna. Practical numbers among the binomial coefficients. J. Number Theory, 207:145–155, 2020.
- [18] R. Li. On number fields towers defined by iteration of polynomials. Arch. Math. (Basel), 119(4):371–379, 2022.
- [19] W. Narkiewicz. A note on a paper of H. Gupta concerning powers of two and three: “Powers of 2 2 and sums of distinct powers of 3 3 ” [Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat. Fiz. No. 602-633 (1978), 151–158 (1979); MR 81g:10016]. Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat. Fiz., (678-715):173–174, 1980.
- [20] P. Ribenboim. The theory of classical valuations. Springer Monographs in Mathematics. Springer-Verlag, New York, 1999.
- [21] C. Sanna. Practical central binomial coefficients. Quaest. Math., 44(9):1141–1144, 2021.
- [22] H. Smith. The monogeneity of radical extensions. Acta Arith., 198(3):313–327, 2021.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:zhao9zone@gmail.com
[4]: mailto:liruofan@jnu.edu.cn
