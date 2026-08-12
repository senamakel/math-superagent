<!-- source: https://arxiv.org/html/2601.17832v1 | converted from HTML -->

Computing bounded solutions to linear Diophantine equations with the sum of divisors

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2601.17832v1 [math.NT] 25 Jan 2026

# Computing bounded solutions to linear Diophantine equations with the sum of divisors

Max A. Alekseyev Address: The George Washington University
Washington, DC, USA Email address: [maxal@gwu.edu][3]

###### Abstract.

We propose an efficient computational method for finding all solutions n ≤ U n\leq U to the Diophantine equation a ​ σ ​ ( n) = b ​ n + c a\sigma(n)=bn+c, where integer coefficient a, b, c a,b,c and an upper bound U U are given. Our method is implemented in SageMath computer algebra system within the framework of recursively enumerated sets and natively benefits from MapReduce parallelization. We used it to discover new solutions to many published equations and close gaps in between the known large solutions, including but not limited to hyperperfect and f f -perfect numbers, as well as to significantly lift the existence bounds in open questions about quasiperfect and almost-perfect numbers.

## 1. Introduction

The *sum of divisors*function, commonly denoted by σ \sigma, has fascinated people for centuries. In particular, it provides elegant characterizations for several important classes of integers, such as the *prime numbers*, which are precisely the solutions to σ ⁡ ( n) = n + 1 \sigma(n)=n+1, and the *perfect numbers*, defined by the equation σ ⁡ ( n) = 2 ​ n \sigma(n)=2n, among others discussed later in the present paper. While the solutions to the former equation are completely understood, the latter remains solved only partially as the existence of an odd perfect number is one of the oldest open questions in number theory. This question is representative of the rich collection of unresolved problems concerning equations involving σ \sigma [6, Section B2].

The aforementioned equations can be seen as partial cases of the Diophantine equation:

(1) |  | a ​ σ ​ ( n) = b ​ n + c, a\sigma(n)=bn+c, |  |

where a > 0, b, c a>0,b,c are fixed integer coefficients with gcd ⁡ ( a, b, c) = 1 \gcd(a,b,c)=1 and n n is an integer indeterminate. In the present study, we develop an efficient computational method for finding all solutions to a given equation ( 1) below a given upper bound U U.

Note that the case a = 1 a=1 and c = 0 c=0 corresponds to *multiperfect numbers*, more specifically *b b -perfect numbers*or just perfect numbers when b = 2 b=2. This case has been the subject of extensive theoretical study (see, for example, references in [6, Section B1]) as well as large-scale computational searches [5]. Although we do not exclude the case c = 0 c=0 from consideration, it is rather special as it admits additional optimization techniques that are not available for nonzero values of c c. Another special case b = 0 b=0 corresponds to inverting the sum of divisors function, a problem we addressed in [1], and thus we delegate this case to the corresponding software. Accordingly, in the present paper we focus on the general case, without discussion of any special treatments for b = 0 b=0 or c = 0 c=0.

We apply our method to many equations of the form ( 1), particularly those that are present in the Online Encyclopedia of Integer Sequences (OEIS) [14], and advance the knowledge about their ”small” solutions by discovering new solutions and putting both newly discovered and already known solutions in order below significantly larger search bounds than previously reported. Similarly, for equations with no known solutions (such as quasiperfect and almost-perfect numbers [6, Section B2]), our method can significantly lift the known lower bounds for potential solutions.

The paper is organized as follows. We introduce the needed notation in Section 2, describe the proposed method in Section 3 and its implementation in Section 4, and then present some practical results in Section 5. We conclude the paper with discussion in Section 6.

## 2. Notation

We start by introducing the notation, which we use throughout the paper:

- •

spf ⁡ ( n) \mathrm{spf}(n) and lpf ⁡ ( n) \mathrm{lpf}(n) denote the smallest and largest prime factor of an integer n > 1 n>1, respectively;

- •

ν p ​ ( n) \nu_{p}(n) denotes the p p -adic valuation of n n, i.e. the largest exponent k k such that p k | n p^{k}\mid n;

- •

Ω ⁡ ( n) \Omega(n) and ω ⁡ ( n) \omega(n) denote the number of prime factors of n n with and without multiplicities, respectively;

- •

τ ⁡ ( n) \tau(n) denotes the number of divisors of an integer n n;

- •

𝔭 1 = 2 \mathfrak{p}_{1}=2, 𝔭 2 = 3 \mathfrak{p}_{2}=3, 𝔭 3 = 5 \mathfrak{p}_{3}=5, … \dots denote the prime numbers in their natural order.

## 3. Method outline

At its core, our approach to solving ( 1) for n ≤ U n\leq U is based on representing the positive integers not exceeding U U as the nodes of a tree T U T_{U} rooted at 1 1, where each node n > 1 n>1 has the parent n / p ν p ​ ( n) n/p^{\nu_{p}(n)} with p:= lpf ⁡ ( n) p:=\mathrm{lpf}(n) (Fig. 1). To search for the solutions, we perform the (restricted) depth-first traversal of T U T_{U} with a few important optimization techniques making it efficient, which we describe in the follow-up subsections. We therefore refer to the nodes of T U T_{U} as the *search space*and to U U as the *search bound*.

Figure 1. The tree T U T_{U} for U = 60 U=60, where some nodes 1 ⋅ p 1\cdot p, 2 ⋅ p 2\cdot p, and 3 ⋅ p 3\cdot p with prime p p are hidden under ellipses.

Note that the descendants of node m m have form m ​ n ′ mn^{\prime}, where spf ⁡ ( n ′) > lpf ⁡ ( m) \mathrm{spf}(n^{\prime})>\mathrm{lpf}(m) (thus gcd ⁡ ( m, n ′) = 1 \gcd(m,n^{\prime})=1) and n ′ ≤ U ′:= U / m n^{\prime}\leq U^{\prime}:=U/m satisfies the equation a ′ ​ σ ​ ( n ′) = b ′ ​ n ′ + c ′ a^{\prime}\sigma(n^{\prime})=b^{\prime}n^{\prime}+c^{\prime} with the coefficients ( a ′, b ′, c ′) (a^{\prime},b^{\prime},c^{\prime}) obtained from ( a ​ σ ​ ( m), b ​ m, c) (a\sigma(m),bm,c) by canceling their common factor (see also Section 4.2). That is, at node m m, we are essentially solving the equation ( 1) with ( a, b, c, U) = ( a ′, b ′, c ′, U ′) (a,b,c,U)=(a^{\prime},b^{\prime},c^{\prime},U^{\prime}) for n = n ′ n=n^{\prime} with an additional constraint spf ⁡ ( n ′) > lpf ⁡ ( m) \mathrm{spf}(n^{\prime})>\mathrm{lpf}(m).

### 3.1. Shortcuts

Under a *shortcut*we understand a way to determine the solutions n = m ​ n ′ n=mn^{\prime} with Ω ⁡ ( n ′) ≤ 2 \Omega(n^{\prime})\leq 2 or ω ⁡ ( n ′) = 1 \omega(n^{\prime})=1 among the descendants of a node m m in T U T_{U}, without traversing all those descendants. There are two cases to consider.

Case n ′ = p k n^{\prime}=p^{k} with k ≥ 1 k\geq 1 and prime p ∈ ( lpf ⁡ ( m), U ′ 1 / k] p\in(\mathrm{lpf}(m),U^{\prime 1/k}]. The equation ( 1) here takes the form a ′ ​ p k + 1 − 1 p − 1 = b ′ ​ p k + c ′ a^{\prime}\frac{p^{k+1}-1}{p-1}=b^{\prime}p^{k}+c^{\prime}, implying that prime p p divides a ′ − c ′ a^{\prime}-c^{\prime}. If a ′ ≠ c ′ a^{\prime}\neq c^{\prime}, we factor a ′ − c ′ a^{\prime}-c^{\prime} and try its prime factors as candidate values for p p, for each of which we then determine suitable values of the exponent k k. Otherwise, if a ′ = c ′ a^{\prime}=c^{\prime}, then gcd ⁡ ( a ′, b ′) = 1 \gcd(a^{\prime},b^{\prime})=1 and ( ( a ′ − b ′) p + b ′) p ( k − 1) = a ′ ((a^{\prime}-b^{\prime})p+b^{\prime})p^{(}k-1)=a^{\prime}, implying that

- •

for k = 1 k=1 and a ′ ≠ b ′ a^{\prime}\neq b^{\prime}, there are no solutions;

- •

for k = 1 k=1 and a ′ = b ′ a^{\prime}=b^{\prime} (thus a ′ = b ′ = c ′ a^{\prime}=b^{\prime}=c^{\prime}), any prime p > lpf ⁡ ( m) p>\mathrm{lpf}(m) gives a solution m ​ p mp (in our implementation, the case a ′ = b ′ = c ′ a^{\prime}=b^{\prime}=c^{\prime} does not appear as it is addressed in pre-processing as explained in Section 4.2);

- •

for k ≥ 2 k\geq 2, we have that p k − 1 | a ′ p^{k-1}\mid a^{\prime} and furthermore k − 1 = ν p ​ ( a ′) k-1=\nu_{p}(a^{\prime}), that is, the candidate values for ( p, k) (p,k) are derived from the prime power factors of a ′ a^{\prime}.

Among the identified solutions we may or may not discard those with p > U ′ 1 / k p>U^{\prime 1/k}, a choice we discuss in Section 4.5.

An explicit partial case of this shortcut for ( a, b, c) = ( 1, 2, d) (a,b,c)=(1,2,d) is given by the following easily verifiable claim, which was discovered and stated by multiple people in the corresponding OEIS sequences (see Section 5.1):

###### Theorem 3.1 (OEIS [14]).

For integers d d and ℓ > 0 \ell>0, the number n = 2 ℓ − 1 ​ ( 2 ℓ − d − 1) n=2^{\ell-1}(2^{\ell}-d-1) is a solution to σ ⁡ ( n) = 2 ​ n + d \sigma(n)=2n+d whenever 2 ℓ − d − 1 2^{\ell}-d-1 is prime.

Indeed, here we have m = 2 ℓ − 1 m=2^{\ell-1}, giving ( a ′, b ′, c ′) = ( σ ⁡ ( m), 2 ​ m, d) = ( 2 ℓ − 1, 2 ℓ, d) (a^{\prime},b^{\prime},c^{\prime})=(\sigma(m),2m,d)=(2^{\ell}-1,2^{\ell},d), and if p:= a ′ − c ′ = 2 ℓ − 1 − d p:=a^{\prime}-c^{\prime}=2^{\ell}-1-d is prime, then the shortcut produces a solution m ​ p = 2 ℓ − 1 ​ ( 2 ℓ − d − 1) mp=2^{\ell-1}(2^{\ell}-d-1) stated in Theorem 3.1.

Case n ′ = p ​ q n^{\prime}=pq with distinct primes p, q p,q, both greater than lpf ⁡ ( m) \mathrm{lpf}(m), and p ​ q ≤ U ′ pq\leq U^{\prime}. Here the equation ( 1) takes the form a ′ ​ ( p + 1) ​ ( q + 1) = b ′ ​ p ​ q + c a^{\prime}(p+1)(q+1)=b^{\prime}pq+c, which we rewrite as A ​ p ​ q + B ​ p + B ​ q + C = 0 Apq+Bp+Bq+C=0 with coefficients A:= a ′ − b ′ A:=a^{\prime}-b^{\prime}, B:= a ′ B:=a^{\prime}, and C:= a ′ − c ′ C:=a^{\prime}-c^{\prime} (in practice, we also cancel their common factor to have gcd ⁡ ( A, B, C) = 1 \gcd(A,B,C)=1). If A = 0 A=0, we check if B | C B\mid C, in which case we obtain the suitable ( p, q) (p,q) by iterating p p over the primes in the interval ( lpf ⁡ ( m), min ⁡ ( D / 2, U ′) CLOSE (\mathrm{lpf}(m),\min(D/2,\sqrt{U^{\prime}}) with D:= − C / B D:=-C/B, and testing q:= D − p q:=D-p for primality. Otherwise, when A ≠ 0 A\neq 0, we *complete the rectangle*(the technique that was known to Brahmagupta born 598 AD [3, Chapter XIII]), i.e. rewrite the equation as

 | ( A ​ p + B) ​ ( A ​ q + B) = B 2 − A ​ C, (Ap+B)(Aq+B)=B^{2}-AC, |  |

which allows us to quickly obtain suitable prime pairs ( p, q) (p,q) by factoring and iterating over the divisors of B 2 − A ​ C B^{2}-AC. In the exceptional case B 2 − A ​ C = 0 B^{2}-AC=0, solutions exist only if p:= − B / A p:=-B/A is a prime satisfying p > lpf ⁡ ( m) p>\mathrm{lpf}(m), and then we report that any prime q > lpf ⁡ ( m) q>\mathrm{lpf}(m) different from p p gives a solution m ​ p ​ q mpq.

Again, here we may obtain some solutions greater than U U, and decide whether or not to report them.

### 3.2. Pruning with prime wheel

At each node m m of T U T_{U}, the shortcuts described in the previous section provide us with the solutions n = m ​ n ′ n=mn^{\prime} satisfying Ω ⁡ ( n ′) ≤ 2 \Omega(n^{\prime})\leq 2 or ω ⁡ ( n ′) = 1 \omega(n^{\prime})=1, and so it remains to focus on finding those with Ω ⁡ ( n ′) ≥ 3 \Omega(n^{\prime})\geq 3 and ω ⁡ ( n ′) ≥ 2 \omega(n^{\prime})\geq 2. It immediately follows that spf ⁡ ( n ′) ≤ U ′ 1 / 3 \mathrm{spf}(n^{\prime})\leq U^{\prime 1/3}, however, we do not need this bound as our approach relies on more accurate dynamic bounds as described below.

Our goal is to generate a set Q Q containing all *feasible*prime powers, that is, for any solution n ′ n^{\prime} of interest and p:= spf ⁡ ( n ′) p:=\mathrm{spf}(n^{\prime}), we should have p ν p ​ ( n ′) ∈ Q p^{\nu_{p}(n^{\prime})}\in Q. Since Q Q defines the set of children { m ​ q: q ∈ Q } \{mq\ :\ q\in Q\} of the node m m to visit, we want Q Q to be as small as possible. We will need the following theorem, which can be seen as a refinement of Lemma 1 in [7]:

###### Theorem 3.2.

Let n n, U U, and S S be positive integers such that n ≤ U n\leq U, σ ⁡ ( n) ≥ S \sigma(n)\geq S, and spf ⁡ ( n) = 𝔭 k \mathrm{spf}(n)=\mathfrak{p}_{k} for some index k k. Then for a positive integer ℓ \ell:

- •

if ℓ ≤ ω ⁡ ( n) \ell\leq\omega(n), then

 | ∏ i = 1 ℓ 𝔭 k + i − 1 ≤ U; \prod_{i=1}^{\ell}\mathfrak{p}_{k+i-1}\leq U; |  |

- •

if ℓ ≥ ω ⁡ ( n) \ell\geq\omega(n), then

 | ∏ i = 1 ℓ 𝔭 k + i − 1 𝔭 k + i − 1 − 1 ≥ S U. \prod_{i=1}^{\ell}\frac{\mathfrak{p}_{k+i-1}}{\mathfrak{p}_{k+i-1}-1}\geq\frac{S}{U}. |  |

###### Proof.

Let’s start with the case ℓ = ω ⁡ ( n) \ell=\omega(n). Since spf ⁡ ( n) = 𝔭 k \mathrm{spf}(n)=\mathfrak{p}_{k}, the ℓ \ell distinct prime factors of n n in increasing order are bounded from below by 𝔭 k, 𝔭 k + 1, …, 𝔭 k + ℓ − 1 \mathfrak{p}_{k},\mathfrak{p}_{k+1},\dots,\mathfrak{p}_{k+\ell-1}, respectively, and therefore

(2) |  | ∏ i = 1 ℓ 𝔭 k + i − 1 ≤ n ≤ U. \prod_{i=1}^{\ell}\mathfrak{p}_{k+i-1}\leq n\leq U. |  |

For the fraction σ ⁡ ( n) n \frac{\sigma(n)}{n}, we have the following upper bound:

 | σ ⁡ ( n) n = ∏ prime ​ p | n ( 1 + p + ⋯ + p − ν p ​ ( n)) ≤ ∏ prime ​ p | n p p − 1. \frac{\sigma(n)}{n}=\prod_{\text{prime }p|n}(1+p+\dots+p^{-\nu_{p}(n)})\leq\prod_{\text{prime }p|n}\frac{p}{p-1}. |  |

Since p p − 1 \frac{p}{p-1} is a decreasing function of p p, the following inequality holds:

(3) |  | ∏ i = 1 ℓ 𝔭 k + i − 1 𝔭 k + i − 1 − 1 ≥ σ ⁡ ( n) n ≥ S U. \prod_{i=1}^{\ell}\frac{\mathfrak{p}_{k+i-1}}{\mathfrak{p}_{k+i-1}-1}\geq\frac{\sigma(n)}{n}\geq\frac{S}{U}. |  |

The theorem statement now follows from the observation that for a fixed k k, the left-hand sides of the inequalities ( 2) and ( 3) represent increasing functions of ℓ \ell. ∎

We construct the set Q Q by keeping track of an accurate lower bound ℓ ≤ ω ⁡ ( n ′) \ell\leq\omega(n^{\prime}) (initially ℓ = 2 \ell=2) and an ℓ \ell -tuple of consecutive primes W:= ( 𝔭 k, 𝔭 k + 1, …, 𝔭 k + ℓ − 1) W:=(\mathfrak{p}_{k},\mathfrak{p}_{k+1},\dots,\mathfrak{p}_{k+\ell-1}), starting with W 1 = 𝔭 k W_{1}=\mathfrak{p}_{k} (initially 𝔭 k \mathfrak{p}_{k} is the next prime after lpf ⁡ ( m) \mathrm{lpf}(m)). 1 1 1 We do not track the actual value of index k k, and we use indices just to underline the relationship between primes in W W. We refer to W W as the *prime wheel*of length | W | = ℓ |W|=\ell. It supports two operations: 2 2 2 In practice, both operations on the wheel are done by using a single generator of consecutive primes.

rolling:

corresponds to incrementing k k, when the tuple W W changes by removing the first element and appending the next prime ( = 𝔭 k + ℓ =\mathfrak{p}_{k+\ell}) after the last element of W W;

length increment:

is done by appending the next prime ( = 𝔭 k + ℓ =\mathfrak{p}_{k+\ell}) after the last element of W W.

Along with the wheel W W, we keep track of the products

 | P κ ​ ( W):= ∏ p ∈ W ( p − κ), κ ∈ { 0, 1 }. P_{\kappa}(W):=\prod_{p\in W}(p-\kappa),\qquad\kappa\in\{0,1\}. |  |

From | W | ≤ ω ⁡ ( n ′) |W|\leq\omega(n^{\prime}) and W 1 ≤ spf ⁡ ( n ′) W_{1}\leq\mathrm{spf}(n^{\prime}), it follows that P 0 ​ ( W) ≤ n ′ ≤ U ′ P_{0}(W)\leq n^{\prime}\leq U^{\prime}, and thus a ′ ​ σ ⁡ ( n ′) n ′ = b ′ + c ′ n ′ a^{\prime}\frac{\sigma(n^{\prime})}{n^{\prime}}=b^{\prime}+\frac{c^{\prime}}{n^{\prime}} is bounded from below by

 | L ⁡ ( W):= { b ′ + c ′ U ′ if ​ c ′ ≥ 0; b ′ + c ′ P 0 ​ ( W) if ​ c ′ < 0. L(W):=\begin{cases}b^{\prime}+\frac{c^{\prime}}{U^{\prime}}&\text{if }c^{\prime}\geq 0;\\ b^{\prime}+\frac{c^{\prime}}{P_{0}(W)}&\text{if }c^{\prime}<0.\end{cases} |  |

For each state of the wheel W W, we test the following conditions:

- •

if P 0 ​ ( W) > U ′ P_{0}(W)>U^{\prime}, then by Theorem 3.2 no solutions with spf ⁡ ( n ′) ≥ W 1 \mathrm{spf}(n^{\prime})\geq W_{1} exist, and we stop the wheel;

- •

if a ′ ​ P 0 ​ ( W) P 1 ​ ( W) < L ⁡ ( W) a^{\prime}\frac{P_{0}(W)}{P_{1}(W)}<L(W), then by Theorem 3.2 there are no solutions with ω ⁡ ( n ′) = | W | \omega(n^{\prime})=|W|, and we increment the wheel length.

If neither of the two conditions holds, then we consider p:= W 1 p:=W_{1} as a candidate for spf ⁡ ( n ′) \mathrm{spf}(n^{\prime}). Since ω ⁡ ( n ′) ≥ | W | \omega(n^{\prime})\geq|W|, the power p t p^{t} in n ′ n^{\prime} must satisfy the inequality p t ​ P 0 ​ ( W) p ≤ U ′ p^{t}\frac{P_{0}(W)}{p}\leq U^{\prime}, and so we add to Q Q the powers p t p^{t} for t t in the interval [1, 1 + ⌊ log p ⁡ U ′ P 0 ​ ( W) ⌋] [1,1+\lfloor\log_{p}\frac{U^{\prime}}{P_{0}(W)}\rfloor]. Then we continue with rolling the wheel.

Since P 0 ​ ( W) P_{0}(W) grows as the wheel W W rolls or grows in length, and sooner or later the wheel stops. By that time, the set Q Q captures all feasible prime powers as we prove in the following theorem:

###### Theorem 3.3.

Let a ′, b ′, c ′, U ′ a^{\prime},b^{\prime},c^{\prime},U^{\prime} be defined as above. Suppose n ′ ≤ U ′ n^{\prime}\leq U^{\prime} is a solution to a ′ ​ σ ​ ( n ′) = b ′ ​ n ′ + c ′ a^{\prime}\sigma(n^{\prime})=b^{\prime}n^{\prime}+c^{\prime} with ω ⁡ ( n ′) ≥ 2 \omega(n^{\prime})\geq 2 and spf ⁡ ( n ′) = 𝔭 t > lpf ⁡ ( m) \mathrm{spf}(n^{\prime})=\mathfrak{p}_{t}>\mathrm{lpf}(m) for some index t t. Then at a certain point the prime wheel reaches the state with | W | ≤ ω ⁡ ( n ′) |W|\leq\omega(n^{\prime}) and W 1 = 𝔭 t W_{1}=\mathfrak{p}_{t}.

###### Proof.

The wheel W W starts at length | W | = 2 |W|=2 and W 1 W_{1} being the next prime after lpf ⁡ ( m) \mathrm{lpf}(m). Hence, at the beginning we have W 1 ≤ 𝔭 t W_{1}\leq\mathfrak{p}_{t} and | W | ≤ ω ⁡ ( n ′) |W|\leq\omega(n^{\prime}). Let W ′:= ( 𝔭 t, 𝔭 t + 1, …, 𝔭 t + ω ⁡ ( n ′) − 1) W^{\prime}:=(\mathfrak{p}_{t},\mathfrak{p}_{t+1},\dots,\mathfrak{p}_{t+\omega(n^{\prime})-1}). Suppose that W 1 ≤ 𝔭 t W_{1}\leq\mathfrak{p}_{t}. We have:

- •

if | W | ≤ ω ⁡ ( n ′) |W|\leq\omega(n^{\prime}), then

 | P 0 ​ ( W) ≤ P 0 ​ ( W ′) ≤ n ′ ≤ U ′; P_{0}(W)\leq P_{0}(W^{\prime})\leq n^{\prime}\leq U^{\prime}; |  |

- •

if | W | = ω ⁡ ( n ′) |W|=\omega(n^{\prime}), then again P 0 ​ ( W) ≤ P 0 ​ ( W ′) P_{0}(W)\leq P_{0}(W^{\prime}), which together with Theorem 3.2 further implies

 | L ⁡ ( W) ≤ L ⁡ ( W ′) ≤ a ′ ​ σ ⁡ ( n ′) n ′ ≤ a ′ ​ P 0 ​ ( W ′) P 1 ​ ( W ′) ≤ a ′ ​ P 0 ​ ( W) P 1 ​ ( W). L(W)\leq L(W^{\prime})\leq a^{\prime}\frac{\sigma(n^{\prime})}{n^{\prime}}\leq a^{\prime}\frac{P_{0}(W^{\prime})}{P_{1}(W^{\prime})}\leq a^{\prime}\frac{P_{0}(W)}{P_{1}(W)}. |  |

By induction on W 1 W_{1}, it now follows that while W 1 ≤ 𝔭 t W_{1}\leq\mathfrak{p}_{t}, the wheel W W does not stop (since P 0 ​ ( W) ≤ U ′ P_{0}(W)\leq U^{\prime}) and cannot grow in length above ω ⁡ ( n ′) \omega(n^{\prime}) (since L ⁡ ( W) ≤ a ′ ​ P 0 ​ ( W) P 1 ​ ( W) L(W)\leq a^{\prime}\frac{P_{0}(W)}{P_{1}(W)}). That is, eventually W W reaches the state with | W | ≤ ω ⁡ ( n ′) |W|\leq\omega(n^{\prime}) and W 1 = 𝔭 t W_{1}=\mathfrak{p}_{t}. ∎

For the sake of simplicity, we did not include the lower bound for Ω ⁡ ( n ′) \Omega(n^{\prime}) in the wheel description and analysis above. In fact, knowing that Ω ⁡ ( n ′) ≥ ℓ Ω \Omega(n^{\prime})\geq\ell_{\Omega} for some ℓ Ω ≥ 3 \ell_{\Omega}\geq 3 provides us with a better lower bound for n ′ n^{\prime}, which is n ′ ≥ W 1 ℓ Ω − | W | ​ P 0 ​ ( W) n^{\prime}\geq W_{1}^{\ell_{\Omega}-|W|}P_{0}(W) instead of just P 0 ​ ( W) P_{0}(W), and thus P 0 ​ ( W) P_{0}(W) should be replaced with W 1 ℓ Ω − | W | ​ P 0 ​ ( W) W_{1}^{\ell_{\Omega}-|W|}P_{0}(W) in the wheel exit condition and the definition of L ⁡ ( W) L(W).

### 3.3. Case of odd σ \sigma

We recognize the case when both a ′ a^{\prime} and b ′ + c ′ b^{\prime}+c^{\prime} are odd. In this case, for any *odd*solution n ′ n^{\prime}, we have

 | σ ⁡ ( n ′) ≡ a ′ ​ σ ​ ( n ′) = b ′ ​ n ′ + c ′ ≡ b ′ + c ′ ≡ 1 ( mod 2), \sigma(n^{\prime})\equiv a^{\prime}\sigma(n^{\prime})=b^{\prime}n^{\prime}+c^{\prime}\equiv b^{\prime}+c^{\prime}\equiv 1\pmod{2}, |  |

implying that n ′ n^{\prime} is an odd square. We take this observation into an account by adjusting the pruning and construction of the set Q Q described above. In particular, when p:= spf ⁡ ( n ′) > 2 p:=\mathrm{spf}(n^{\prime})>2 and hence n ′ n^{\prime} is an odd square, the wheel stop condition W 1 ℓ Ω − | W | ​ P 0 ​ ( W) > U ′ W_{1}^{\ell_{\Omega}-|W|}P_{0}(W)>U^{\prime} changes to W 1 ℓ Ω − 2 ​ | W | ​ P 0 ​ ( W) 2 > U ′ W_{1}^{\ell_{\Omega}-2|W|}P_{0}(W)^{2}>U^{\prime}, and we restrict our attention only to even exponents t t while adding powers p t p^{t} to Q Q. Additionally, from a ′ ​ σ ​ ( p t) ​ σ ​ ( n ′ / p t) = b ′ ​ n ′ + c a^{\prime}\sigma(p^{t})\sigma(n^{\prime}/p^{t})=b^{\prime}n^{\prime}+c, it follows that for any prime q | σ ⁡ ( p t) q\mid\sigma(p^{t}), − b ′ ​ c ′ ≡ ( b ′) 2 ​ n ′ ( mod q) -b^{\prime}c^{\prime}\equiv(b^{\prime})^{2}n^{\prime}\pmod{q}, i.e., − b ′ ​ c ′ -b^{\prime}c^{\prime} is a square residue modulo q q. We test this condition by comparing Legendre symbol ( − b ′ ​ c ′ q) \left(\frac{-b^{\prime}c^{\prime}}{q}\right) to − 1 -1, and discard t t if the equality holds for any such q q.

Similarly, sometimes we can recognize the oddness of σ ⁡ ( n ′) \sigma(n^{\prime}) irrespectively of the parity of n ′ n^{\prime}, e.g., when a ′ a^{\prime} and c ′ c^{\prime} are odd while b ′ b^{\prime} is even. In this case, n ′ n^{\prime} can be a square or twice a square. Correspondingly, we extend the test described above to p = 2 p=2 by computing Legendre symbol ( − 2 t ​ b ′ ​ c ′ q) = ( − 2 t mod 2 ​ b ′ ​ c ′ q) \left(\frac{-2^{t}b^{\prime}c^{\prime}}{q}\right)=\left(\frac{-2^{t\bmod 2}b^{\prime}c^{\prime}}{q}\right). In particular, this test automatically eliminates the possibility of even solutions for the quasiperfect numbers satisfying σ ⁡ ( n) = 2 ​ n + 1 \sigma(n)=2n+1 (see Section 5.1) since for any exponent t ≥ 1 t\geq 1, σ ⁡ ( 2 t) = 2 t + 1 − 1 \sigma(2^{t})=2^{t+1}-1 has a prime factor q q congruent to 3 modulo 4, giving Legendre symbol ( − 2 t ​ b ′ ​ c ′ q) = ( − 2 t + 1 q) = ( − 1 q) = − 1 \left(\frac{-2^{t}b^{\prime}c^{\prime}}{q}\right)=\left(\frac{-2^{t+1}}{q}\right)=\left(\frac{-1}{q}\right)=-1.

We also recognize the squareness of n ′ n^{\prime} when we additionally know the value of τ ⁡ ( n ′) \tau(n^{\prime}) (see Section 4.4) and this value is odd.

### 3.4. Case of gcd ⁡ ( a ′, c ′) > 1 \gcd(a^{\prime},c^{\prime})>1

From gcd ⁡ ( a ′, b ′, c ′) = 1 \gcd(a^{\prime},b^{\prime},c^{\prime})=1, it follows that g:= gcd ⁡ ( a ′, c ′) g:=\gcd(a^{\prime},c^{\prime}) divides any solution n ′ n^{\prime}. Suppose that g > 1 g>1. If gcd ⁡ ( g, m) > 1 \gcd(g,m)>1, then there are no solutions as n ′ n^{\prime} is coprime to m m. However, if gcd ⁡ ( g, m) = 1 \gcd(g,m)=1, the prime factors of g g give valid prime factors of n ′ n^{\prime}. In this case, instead of rolling the wheel in search for spf ⁡ ( n ′) \mathrm{spf}(n^{\prime}), we pick the largest prime power p e p^{e} from the prime factorization of g g and define Q = { p t: t = e, e + 1, …, e + ⌊ log p U ′ g ⌋ } Q=\{p^{t}\ :\ t=e,e+1,\dots,e+\lfloor\log_{p}\frac{U^{\prime}}{g}\rfloor\}. Jumping from m m to a node m ′:= m ​ q m^{\prime}:=mq for q ∈ Q q\in Q facilitates a more narrowed search for n ′ n^{\prime}.

Since solutions of the form n = m ′ ​ n ′′ n=m^{\prime}n^{\prime\prime} do not have to satisfy the restriction spf ⁡ ( n ′′) > lpf ⁡ ( m ′) \mathrm{spf}(n^{\prime\prime})>\mathrm{lpf}(m^{\prime}) anymore, to properly incorporate such jumps into the search, we introduce and maintain a lower bound l p l_{p} for spf ⁡ ( n ′) \mathrm{spf}(n^{\prime}) independent of lpf ⁡ ( m) \mathrm{lpf}(m) (e.g., l p l_{p} does not change when we jump from m m to m ′ m^{\prime}). Also, to guarantee that gcd ⁡ ( m, n ′) = 1 \gcd(m,n^{\prime})=1, we make the prime wheel roll over the set primes exluding the prime factors of m m.

## 4. SageMath implementation

### 4.1. RES framework

The described traversal of T U T_{U} fits nicely the framework of *recursively enumerated set*(RES) in SageMath computer algebra system [12]. It allows efficient traversal the nodes of a forest (tree T U T_{U} in our case) by specifying seeds (i.e., the root of T U T_{U}) and defining a function succ( t t) that computes the set of successors of a given node t t. To simplify computations, we define t t as a tuple ( a ′, b ′, c ′, m, l p, aux) (a^{\prime},b^{\prime},c^{\prime},m,l_{p},\mathrm{aux}), where the first five elements have the same meaning as in the previous section, and aux \mathrm{aux} is a dictionary with additional constraints (see Section 4.4 below). So, the tuple t t may be viewed as the *configuration*of node m m in T U T_{U}.

### 4.2. Configurations reduction

In order to better handle configurations, we define a local function reduce_abc( t t), which reduces the given configuration t t (e.g., by canceling the common factor of a ′, b ′, c ′ a^{\prime},b^{\prime},c^{\prime}) and returns the resulting reduced configuration. It recognizes some cases when the given t t has no solutions and returns None, indicating that traversal of the subtree rooted at t t should be avoided. For example, gcd ⁡ ( a ′, b ′, c ′) = 1 \gcd(a^{\prime},b^{\prime},c^{\prime})=1 but gcd ⁡ ( a ′, c ′) \gcd(a^{\prime},c^{\prime}) having a prime factor (which has to divide n ′ n^{\prime}) below l p l_{p} is such a case.

Another special case recognized by reduce_abc is a ′ = b ′ = c ′ a^{\prime}=b^{\prime}=c^{\prime}, where any prime p p would be a solution. However, in view of the given m m and l p l_{p}, primes p p in the solution must be restricted to p ≥ l p p\geq l_{p} and p ∤ m p\nmid m. Function reduce_abc( t t) prints a message describing the corresponding infinite series of solutions, and avoids solving this equation by returning None as above. We show an example of an equation with an infinite series of solutions in Section 5.1 below.

As certain equations of the form ( 1) have already received significant effort in computing their solutions, our implementation supports optional referencing to those ”core” equations (parameter refs) and the corresponding OEIS sequences. When refs=True, once a configuration t t is identified as corresponding to a core equation, a message with a reference to the corresponding OEIS sequence is printed and no processing of t t takes place. In particular, equations ( a ′, b ′) = ( 1, 2) (a^{\prime},b^{\prime})=(1,2) and small even c ′ c^{\prime} (discussed in Section 5.1) can be referenced this way as their solutions below 10 20 10^{20} can be queried from the OEIS.

### 4.3. MapReduce parallelization

The primary benefit of the RES framework is a readily-available parallelization via the MapReduce mechanism [8] present in SageMath. Besides the parallelized traversal, it supports parallel processing of each visited node t t via a user-defined function proc( t t), which computes the result (e.g., set of solutions) for node t t, and those results then can be combined over all visited nodes. In our case, while the prime wheel (that computes successors) is implemented inside succ( t t) function, computing the shortcuts (that produces actual solutions) are conveniently implemented inside proc( t t).

### 4.4. Additional constraints

It is possible to further narrow the traversal by enforcing additional constraints. Our implementation supports the following constraints via optional parameters:

- •

squarefreeness of n n (parameter squarefree);

- •

evenness of n n (parameter even_only);

- •

coprimality to a given integer (parameter coprime_to);

- •

bounds for ω ⁡ ( n) \omega(n) and Ω ⁡ ( n) \Omega(n) (parameters omega and bigomega, respectively);

- •

a prescribed value for τ ⁡ ( n) \tau(n) (parameter numdiv).

Nontrivial constraints, whether they are derived from the given parameters or obtained while rolling the prime wheel in succ() function, are passed (in aux dictionary) from a parent node to its children to propagate a narrowed search. Also, such constraints can save time while computing shortcuts in proc() function: for example, a bound like ω ⁡ ( n ′) ≥ 2 \omega(n^{\prime})\geq 2 implies that the case n ′ = p k n^{\prime}=p^{k} is impossible and can be skipped, and similarly a bound like Ω ⁡ ( n ′) ≥ 3 \Omega(n^{\prime})\geq 3 implies that the case n = p ​ q n=pq is impossible.

### 4.5. Solutions above U U

As we already noted, the shortcuts described in Section 3.1 can potentially produce some solutions above U U. In our implementation, we have control over whether to ignore or report such large solutions (parameter strict). In our computational experiments, some of which are described in the next section, large solutions—whether previously known or newly discovered—happen to inspire us to increase the search bound and thus eventually place those solutions in order. Unfortunately, some of the discovered solutions, such as the greater of two 2772 2772 -hyperperfect numbers reported in Section 5.2, are too large and remain inaccessible as a search bound.

### 4.6. Availability

Our implementation is available from the following GitHub repository:

[https://github.com/maxale/multiplicative_functions][4]

Our method is accessible via function res_solve_sigma_abc() in the code file sigma_linear_eq.sage. It expects from a caller the required arguments a a, b b, c c, and U U, and also supports optional parameters, some of which are described above. A full list of supported parameters and their format can be seen directly in the code.

## 5. Applications

In this section, we present some practical results obtained with our method for various equations of interest.

### 5.1. Numbers with a small abundance

The *abundance*of a number n n is defined as σ ⁡ ( n) − 2 ​ n \sigma(n)-2n. The perfect numbers have abundance 0 0, so the abundance of n n can be viewed as the ”distance” from n n to being a perfect number.

The next two famous cases are the numbers with abundance 1 1 called *quasiperfect numbers*, and the numbers with abundance − 1 -1 called *almost-perfect numbers*. Existence of quasiperfect numbers is an open question. It is known that quasiperfect numbers must be odd squares greater than 10 35 10^{35} [7]. With our method, we lift this bound to 10 45 10^{45}, which was established in about 440 core-hours (specifically, about 11 hours on a 40-core machine). 3 3 3 We define *core-hours*as the wall-clock time in hours taken by the computation times the number of used cores. Most experiments were run on Intel Xeon 2.40GHz or AMD EPYC 2.2GHz CPUs. As we explained in Section 3.3, the squareness and oddness of the possible solutions is automatically detected and taken into account by our method.

The only known almost-perfect numbers are the powers of 2 2. The existing literature on almost-perfect numbers does not seem to give an explicit lower bound on almost-perfect non-powers of 2 2, but focuses on the possible structure of such numbers (e.g., see [9]). With our method, we establish that no other almost-perfect numbers exist below 10 33 10^{33}, which took about 6540 6540 core-hours. For the odd almost-perfect number other than 1 1, we establish that none exist below 10 47 10^{47}, which took about 1272 1272 core-hours.

In general, numbers with an odd abundance are much sparser than those of even abundance, since an odd abundance of n n implies the oddness of σ ⁡ ( n) \sigma(n), and thus n n must be a square or twice a square. The Online Encyclopedia of Integer Sequences [14] contains sequences for each even abundance in the interval [− 32, 32] [-32,32] as well as for abundances in { − 42, − 54, ± 64, ± 90,128 } \{-42,-54,\pm 64,\pm 90,128\}. With our method, we have routinely completed these sequences with all terms below 10 20 10^{20}. For some of them we actually reached a larger bound, typically chosen to match some term discovered by the shortcuts (e.g., a term produced by Theorem 3.1). In Table 1, we list some of largest bounds we achieved and the corresponding running time in core-hours.

Abundance | OEIS | Search bound | Core-hours |

-2 | A191363 | 10 24 10^{24} | 42 |

2 | A088831 | 10 24 10^{24} | 46 |

6 | A087167 | 1.5 ⋅ 10 23 1.5\cdot 10^{23} | 1720 |

10 | A223609 | 9.6 ⋅ 10 24 9.6\cdot 10^{24} | 340 |

14 | A141546 | 10 24 10^{24} | 40 |

18 | A223610 | 1.5 ⋅ 10 23 1.5\cdot 10^{23} | 1440 |

-22 | A223606 | 1.5 ⋅ 10 26 1.5\cdot 10^{26} | 436 |

-24 | A385255 | 1.5 ⋅ 10 23 1.5\cdot 10^{23} | 246 |

90 | A389703 | 1.5 ⋅ 10 23 1.5\cdot 10^{23} | 1805 |

Table 1. Selected fixed-abundance sequences in the OEIS, along with the achieved search bounds and the approximate running time taken by the search.

We remark that the numbers of abundance 12 12 contain an infinite subsequence ( 6 ​ 𝔭 k) k ≥ 3 (6\mathfrak{p}_{k})_{k\geq 3} and thus the corresponding OEIS sequence A141545 is mostly composed of small terms from this subsequence. Our method correctly identifies this infinite subsequence (by printing a message about it) and focuses on searching *sporadic*solutions outside it. Those sporadic solutions can seen as a subsequence of the OEIS sequence A234238, which lists sporadic solutions to a more general congruence σ ⁡ ( n) ≡ 6 ( mod n) \sigma(n)\equiv 6\pmod{n} and which we solved below 10 24 10^{24}.

### 5.2. Hyperperfect numbers

Hyperperfect numbers represent another generalization of perfect numbers [6, Section B2]. A positive integer n n is called k k -hyperperfect for some integer k k if n = 1 + k ⁡ ( σ ⁡ ( n) − n − 1) n=1+k(\sigma(n)-n-1), where σ ⁡ ( n) − n − 1 \sigma(n)-n-1 can be seen as the sum of divisors of n n other than 1 1 and n n. The 1 1 -hyperperfect numbers are exactly the perfect ones. McCranie [10] tabulated hyperperfect numbers below 10 11 10^{11} and identified a few values of k k of particular interest. Besides the perfect numbers, the OEIS contains sequences of k k -hyperperfect numbers listed in Table 2.

k | 2 | 4 | 6 | 12 | 18 | 2772 | 31752 |

OEIS | A007593 | A220290 | A028499 | A028500 | A028501 | A028502 | A034916 |

Table 2. The sequences of k k -hyperperfect numbers (other than perfect ones) that are present in the OEIS.

Noting that the defining equation for k k -hyperperfect numbers has the form ( 1) with ( a, b, c) = ( k, k + 1, k − 1) (a,b,c)=(k,k+1,k-1), we apply our method for determining all terms in the cited sequences below bounds of at least 10 20 10^{20}. Besides pushing the search bounds and putting known terms in order, we discovered some previously unknown hyperperfect numbers, such as the following two 2772 2772 -hyperperfect numbers composed of 3 and 4 primes, respectively:

 | 47268697363953913 = 2791 ⋅ 411409 ⋅ 41166127 47268697363953913=2791\cdot 411409\cdot 41166127 |  |

and

 | 186690534609915040044368953 = 5237 ⋅ 6173 ⋅ 128669 ⋅ 44881723181837. 186690534609915040044368953=5237\cdot 6173\cdot 128669\cdot 44881723181837. |  |

While the former number is below our search bound and is proved to be the fifth 2772 2772 -hyperperfect number in order, the latter one currently remains out of reach and thus its order number is unknown.

While 2 2 -hyperperfect numbers satisfy the equation 2 ​ σ ​ ( n) = 3 ​ n + 1 2\sigma(n)=3n+1, the OEIS sequence A063906 lists solutions to a similar equation 2 ​ σ ​ ( n) = 3 ​ n + 3 2\sigma(n)=3n+3, which can be also written as σ ​ ( n) = 3 2 ​ ( n + 1) \sigma(n)=\frac{3}{2}(n+1) to somewhat resemble perfect numbers. We determined all solutions to this equation below 3.7 ⋅ 10 23 3.7\cdot 10^{23}, which took us 6336 core-hours, as well as discovered some previously unknown terms above that bound.

### 5.3. f f -perfect numbers

For a given arithmetic function f f, f f -perfect numbers are defined [11] as integers n n satisfying 2 ​ f ​ ( n) = ∑ d | n f ⁡ ( d) 2f(n)=\sum_{d\mid n}f(d). For the identity function f f, they are exactly the perfect numbers, and thus f f -perfect numbers represent yet another generalization of the perfect numbers. The OEIS contains a few sequences listing f f -perfect numbers, including f ⁡ ( x) = x + 1 f(x)=x+1 (sequence A066229) and f ⁡ ( x) = x − 1 f(x)=x-1 (sequence A066230).

Note that when f f is a linear function, say f ⁡ ( n) = u ​ n + v f(n)=un+v with integer coefficients u, v u,v, then the defining equation of f f -perfect numbers becomes 2 ​ ( u ​ n + v) = u ​ σ ​ ( n) + v ​ τ ​ ( n) 2(un+v)=u\sigma(n)+v\tau(n). For a fixed value of τ ⁡ ( n) = d \tau(n)=d it takes the form ( 1) with ( a, b, c) = ( u, 2 ​ u, v ⁡ ( 2 − d)) (a,b,c)=(u,2u,v(2-d)), for which we can run our method with the additional constraint τ ⁡ ( n) = d \tau(n)=d (see Section 4.4). We identify the feasible values of τ ⁡ ( n) \tau(n) as follows.

The bound n ≤ U n\leq U implies an upper bound for τ ⁡ ( n) \tau(n). For U < 10 480 U<10^{480}, an accurate bound can be obtained from data present in the OEIS sequence A002182 of *highly composite numbers*, which are the numbers k k such that τ ⁡ ( k) > τ ⁡ ( ℓ) \tau(k)>\tau(\ell) for all ℓ < k \ell<k. Namely, if k k is the largest such number with D:= τ ⁡ ( k) ≤ U D:=\tau(k)\leq U, then for any n ≤ U n\leq U, we have τ ⁡ ( n) ≤ D \tau(n)\leq D. We can further quickly identify feasible values of d d in the interval [1, D] [1,D] by checking if the smallest number m m with τ ⁡ ( m) = d \tau(m)=d (OEIS sequence A005179) does not exceed U U.

Following this route, we determined all ( x + 1) (x+1) -perfect numbers below 1.5 ⋅ 10 23 1.5\cdot 10^{23}, including the following newly discovered term with a rich prime factorization:

 | 20055918935605248255 = 3 ⋅ 5 ⋅ 7 3 ⋅ 17 ⋅ 101 ⋅ 719 ⋅ 991 ⋅ 3186283. 20055918935605248255=3\cdot 5\cdot 7^{3}\cdot 17\cdot 101\cdot 719\cdot 991\cdot 3186283. |  |

Similarly, we determined all ( x − 1) (x-1) -perfect numbers below 5.9 ⋅ 10 20 5.9\cdot 10^{20}.

## 6. Concluding remarks

It is hard to come up with an accurate complexity analysis for the proposed algorithm, but our computational experiments show that it is very efficient in practice and can reach much larger search bounds than the previously reported in the literature. They also show (e.g., in Table 1) that its running time is sensitive to the given coefficients as it may vary significantly for the coefficients the same magnitude and the same upper bound U U.

Empirically, within the explored search bounds, the running time as a function of U U for many equations seems to grow as Θ ⁡ ( r log 10 ⁡ U) \Theta(r^{\log_{10}U}) with a constant r r (depending on the equation coefficients) in the interval [2, 4] [2,4], although there exist outliers with smaller and larger values of r r. Also, our computations tend to scale up well with the number of cores (e.g., using 80 cores reduces the running time by a factor close to 2 as compared to 40 cores). Unfortunately, the performance of the current MapReduce functionality in SageMath may drastically degrade as the number of cores gets close or exceeds a hundred, 4 4 4 See SageMath ’s issue #41115: [https://github.com/sagemath/sage/issues/41115][5] and to be on a safe side in our computational experiments we used at most 80 cores.

We took a great care about crafting our algorithm at the high level (minimizing the number of nodes of T U T_{U} to visit) and fitting it into the RES/ MapReduce framework, but we did not do much about optimization at the lower level. Since SageMath is Python -based, it does not provide the best performance out of the box. We expect that *cythonization*of our implementation or re-implementing it in a parallelization-aware mid-level programming language (such as Cilk extension of C++) can bring some- or even many-fold speedup. This is something we plan to explore in future.

Another possibility for scaling up our method is using parallelization not only within the cores of a single computer, but also across multiple computers. We believe it is well amenable to distributing across multiple nodes of a computational cluster as well as across a variety of computers in a crowd-computing project, although we did not pursue that in practice.

An obvious drawback of our method is its inability to extend the search from an already achieved search bound to a larger one. In order to increase the search bound, the whole computation should be started from scratch.

Recently we used Theorem 1 and a similar computational approach within the collaborative effort [13] proving that the largest n n such that L n:= lcm ⁡ ( 1, 2, …, n) L_{n}:=\mathrm{lcm}(1,2,\dots,n) is highly abundant is n = 169 n=169. In practice, our approach is able to determine if L n L_{n} is highly abundant for n n up to a few hundred (surely including all n ≤ 169 n\leq 169).

The tree structure on the positive integers (described in Section 3) is somewhat similar to the one used by Fang [4], although they use multiplication by single primes rather than prime powers while going down along the tree. Both our and their search algorithms can be seen as instances of the reverse search [2]. While their target is not the equation ( 1) and thus direct comparison of the two approaches is not possible, they claim that their algorithm and pruning strategy *”can be adapted to search for … odd almost-perfect numbers”*. However, since their approach was designed for a different problem, it understandably misses some techniques (e.g., what we refer to as shortcuts) that we found essential to the efficient search for odd almost-perfect numbers.

With a suitable adjustment of the shortcut and pruning techniques, our method can be used for linear equations with other multiplicative functions. In particular, we already have an efficient solver for linear equations with Euler’s totient function; the manuscript describing it is currently in preparation.

## References

- [1] M. A. Alekseyev. Computing the inverses, their power sums, and extrema for Euler’s totient and other multiplicative functions. Journal of Integer Sequences, 19(5):Article 16.5.2, 2016.
- [2] D. Avis and K. Fukuda. Reverse search for enumeration. Discrete Applied Mathematics, 65(1):21–46, 1996. First International Colloquium on Graphs and Optimization. [doi:10.1016/0166-218X(95)00026-N][6].
- [3] L. E. Dickson. History of the Theory of Numbers. Volume II: Diophantine Analysis. Carnegie Institution of Washington, Washington, DC, 1920.
- [4] W. Fang. Searching on the boundary of abundance for odd weird numbers. Preprint arXiv:2207.12906 [math.NT], 2022. [doi:10.48550/arXiv.2207.12906][7].
- [5] A. Flammenkamp. The multiply perfect numbers page. [https://wwwhomes.uni-bielefeld.de/achim/mpn.html][8], 2023.
- [6] R. K. Guy. Unsolved problems in number theory. Problem Books in Mathematics. Springer, New York, NY, 3rd edition, 2004. [doi:10.1007/978-0-387-26677-0][9].
- [7] P. Hagis and G. L. Cohen. Some results concerning quasiperfect numbers. Journal of the Australian Mathematical Society. Series A. Pure Mathematics and Statistics, 33(2):275–286, 1982. [doi:10.1017/S1446788700018401][10].
- [8] F. Hivert. High performance computing experiments in enumerative and algebraic combinatorics. In Proceedings of the International Workshop on Parallel Symbolic Computation, PASCO 2017, New York, NY, USA, 2017. Association for Computing Machinery. [doi:10.1145/3115936.3115938][11].
- [9] M. Kishore. On odd perfect, quasiperfect, and odd almost perfect numbers. Mathematics of Computation, 36(154):583–586, 1981. [doi:10.2307/2007662][12].
- [10] J. S. McCranie. A study of hyperperfect numbers. J. Int. Seqs., 3:Article 00.1.3, 2000.
- [11] J. L. Pe. On a generalization of perfect numbers. J. Rec. Math., 31(3):168–172, 2002.
- [12] SageMath. version 10.8, 2025. [https://www.sagemath.org][13].
- [13] T. Tao et al. Is the least common multiple sequence lcm ​ ( 1, 2, …, n) \text{lcm}(1,2,\dots,n) a subset of the highly abundant numbers? MathOverflow. [https://mathoverflow.net/q/501203][14] (version: 2025-10-10).
- [14] The OEIS Foundation. The On-Line Encyclopedia of Integer Sequences. [http://oeis.org][15], 2026.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:maxal@gwu.edu
[4]: https://github.com/maxale/multiplicative_functions
[5]: https://github.com/sagemath/sage/issues/41115
[6]: https://doi.org/10.1016/0166-218X(95)00026-N
[7]: https://doi.org/10.48550/arXiv.2207.12906
[8]: https://wwwhomes.uni-bielefeld.de/achim/mpn.html
[9]: https://doi.org/10.1007/978-0-387-26677-0
[10]: https://doi.org/10.1017/S1446788700018401
[11]: https://doi.org/10.1145/3115936.3115938
[12]: https://doi.org/10.2307/2007662
[13]: https://www.sagemath.org
[14]: https://mathoverflow.net/q/501203
[15]: http://oeis.org
