<!-- source: https://arxiv.org/html/2607.24414 | converted from HTML -->

Entropy methods in combinatorics

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2607.24414v1 [math.CO] 27 Jul 2026

# Entropy methods in combinatorics

Wojciech Samotij Address: School of Mathematical Sciences, Tel Aviv University, Tel Aviv, Israel Email address: [samotij@tauex.tau.ac.il][3]

###### Abstract.

Even though entropy methods have been used in combinatorics for at least five decades, only in recent years has their use really proliferated. There are now tens, if not hundreds, of combinatorial papers that crucially rely on the notion of entropy and exploit the various powerful identities and inequalities relating entropies. In this short survey article, we give a selective overview of these works and discuss several of them in more detail, outlining some of the key ideas.

## 1. Introduction.

The notion of *entropy*was introduced by Claude Shannon in his landmark 1948 paper [96] that laid rigorous foundations for the field of information theory. Shannon’s entropy quantifies the amount of uncertainty that is associated with a discrete random variable. The fundamental property of entropy that makes it relevant to enumeration problems is that the entropy of a random variable that is uniformly distributed on a finite set 𝒳 \mathcal{X} is the logarithm of the cardinality of 𝒳 \mathcal{X}. This fact allows one to turn counting problems into problems of estimating entropy. The advantage of this seemingly circuitous approach is that there are several powerful inequalities involving entropies that do not seem to have any direct counting analogues. The origins of the idea of using entropy in combinatorics are hard to trace, but it has surely been around for at least five decades (see, e.g., [19] or [27, Chapter 2]). Once a niche tool, since the turn of the century entropy has become a widely-applied technique. The aim of this survey is to present some of the most influential applications of entropy methods in combinatorics and highlight the underlying ideas.

### 1.1. Entropy.

There are several different ways to introduce and motivate the notion of entropy, some of which are discussed in detail by Rényi [92]. The author is particularly fond of the following axiomatic approach he first encountered in the excellent lecture notes of Galvin [41]. We would like to define a function I I that measures the information one learns from the occurrence of a certain subset of outcomes of a random experiment; one then defines the entropy of a discrete random variable X X as the average amount of information associated with the outcome of X X. We postulate that I I should: (i) take only nonnegative values and depend only on the probability of the said event; (ii) be decreasing in this probability (less likely events should carry more information); and (iii) assign to the intersection of two independent events the sum of the amounts of information associated with the two events. In other words, we are looking for a function I: ( 0, 1] → [0, ∞) I\colon(0,1]\to[0,\infty) that is decreasing and satisfies I ⁡ ( p ​ q) = I ⁡ ( p) + I ⁡ ( q) I(pq)=I(p)+I(q) for all p, q ∈ ( 0, 1] p,q\in(0,1]. Since one can show that the only functions that meet this specification are logarithmic functions, that is, I ⁡ ( p) = − log b ⁡ p I(p)=-\log_{b}p for some b > 1 b>1, this leads to the following definition.

###### 1.1.

The entropy of a random variable X X taking values in a finite set 𝒳 \mathcal{X} is

 | H ( X) ≔ − ∑ x ∈ 𝒳 ℙ ( X = x) ⋅ log ℙ ( X = x). H(X)\coloneqq-\sum_{x\in\mathcal{X}}\mathbb{P}(X=x)\cdot\log\mathbb{P}(X=x). |  |

The following simple fact is a generalisation of the fundamental property of entropy mentioned in the introduction.

###### 1.2.

If a random variable X X takes values in a finite set 𝒳 \mathcal{X}, then

 | H ⁡ ( X) ≤ log ⁡ | 𝒳 |. H(X)\leq\log|\mathcal{X}|. |  |

Moreover, equality holds if and only if X X is uniform on 𝒳 \mathcal{X}.

### 1.2. Conditional entropy.

A fundamental notion that makes the entropy method so powerful is that of *conditional entropy*. Informally speaking, the conditional entropy of a random variable X X given another random variable Y Y (defined on the same probability space) is the expected amount of information learned from the outcome of X X assuming that the outcome of Y Y is already known. More precisely, for every y y such that ℙ ⁡ ( Y = y) \mathbb{P}(Y=y) is nonzero, define the conditioned random variable X y X^{y} by ℙ ⁡ ( X y = x) ≔ ℙ ⁡ ( X = x ∣ Y = y) \mathbb{P}(X^{y}=x)\coloneqq\mathbb{P}(X=x\mid Y=y). The conditional entropy of X X given Y Y is then the expectation of the (random) entropy H ⁡ ( X y) H(X^{y}), where y y is sampled according to Y Y.

###### 1.3.

Suppose that X X and Y Y are random variables taking values in finite sets 𝒳 \mathcal{X} and 𝒴 \mathcal{Y}, respectively. The conditional entropy of X X given Y Y is

 | H ( X ∣ Y) ≔ − ∑ y ∈ 𝒴 ℙ ( Y = y) ∑ x ∈ 𝒳 ℙ ( X = x ∣ Y = y) log ℙ ( X = x ∣ Y = y). H(X\mid Y)\coloneqq-\sum_{y\in\mathcal{Y}}\mathbb{P}(Y=y)\sum_{x\in\mathcal{X}}\mathbb{P}(X=x\mid Y=y)\log\mathbb{P}(X=x\mid Y=y). |  |

It is easily verified that H ⁡ ( X ∣ Y) = H ⁡ ( X, Y) − H ⁡ ( Y) H(X\mid Y)=H(X,Y)-H(Y), where we wrote H ⁡ ( X, Y) H(X,Y) in place of H ⁡ ( (,,,)) H((X,Y)) to denote the entropy of the random vector ( X, Y) (X,Y). The straightforward generalisation of this identity to n n -dimensional vectors is the so-called *chain rule*for entropies.

###### 1.4 Chain rule.

For every sequence X 1, …, X n X_{1},\dotsc,X_{n} of discrete random variables,

 | H ⁡ ( X 1, …, X n) = ∑ i = 1 n H ⁡ ( X i ∣ X 1, …, X i − 1). H(X_{1},\dotsc,X_{n})=\sum_{i=1}^{n}H(X_{i}\mid X_{1},\dotsc,X_{i-1}). |  |

The next key property formalises the intuitive statement that conditioning on more information can only decrease conditional entropy.

###### 1.5.

For every triple X, Y, Z X,Y,Z of discrete random variables,

 | H ⁡ ( X ∣ Y, Z) ≤ H ⁡ ( X ∣ Y) ≤ H ⁡ ( X). H(X\mid Y,Z)\leq H(X\mid Y)\leq H(X). |  |

Moreover, the second inequality holds with equality if and only if X X and Y Y are independent while the first inequality holds with equality if and only if X X and Z Z are conditionally independent given Y Y. 2 2 2 This means that, for every y y with ℙ ⁡ ( Y = y) > 0 \mathbb{P}(Y=y)>0, the conditioned random variables X y X^{y} and Z y Z^{y} are independent.

An immediate consequence of 1.4 and 1.5 is the following subadditivity property.

###### 1.6 Subadditivity.

For every sequence X 1, …, X n X_{1},\dotsc,X_{n} of discrete random variables,

 | H ⁡ ( X 1, …, X n) ≤ ∑ i = 1 n H ⁡ ( X i). H(X_{1},\dotsc,X_{n})\leq\sum_{i=1}^{n}H(X_{i}). |  |

Moreover, equality holds if and only if X 1, …, X n X_{1},\dotsc,X_{n} are independent.

Similarly, one can derive the following more general, conditional version of the subadditivity property.

###### 1.7.

For every sequence X 1, …, X n, Y X_{1},\dotsc,X_{n},Y of discrete random variables,

 | H ⁡ ( X 1, …, X n ∣ Y) ≤ ∑ i = 1 n H ⁡ ( X i ∣ Y) H(X_{1},\dotsc,X_{n}\mid Y)\leq\sum_{i=1}^{n}H(X_{i}\mid Y) |  |

and equality holds if and only if X 1, …, X n X_{1},\dotsc,X_{n} are conditionally independent given Y Y.

### 1.3. Binary entropy.

In many applications of the entropy method, one often considers the entropy of two-valued random variables. It is therefore customary to introduce the *binary entropy*function, which assigns to a given parameter p ∈ [0, 1] p\in[0,1] the entropy of a random variable that takes only two values, with probabilities p p and 1 − p 1-p, respectively (e.g., the Bernoulli random variable with success probability p p, denoted by Ber ⁡ ( p) \mathrm{Ber}(p)).

###### 1.8.

The binary entropy is the function h: [0, 1] → [0, log ⁡ 2] h\colon[0,1]\to[0,\log 2] defined by

 | h ⁡ ( p) ≔ H ⁡ ( Ber ⁡ ( p)) = − p ​ log ⁡ p − ( 1 − p) ​ log ⁡ ( 1 − p). h(p)\coloneqq H(\mathrm{Ber}(p))=-p\log p-(1-p)\log(1-p). |  |

The binary entropy function arises naturally in the following classical estimate, whose elegant, entropy-based proof is perhaps the archetypal application of the entropy method.

###### 1.9.

For all integers k k and n n satisfying 0 ≤ k ≤ n / 2 0\leq k\leq n/2,

 | ∑ j = 0 k ( n j) ≤ exp ⁡ ( n ⋅ h ⁡ ( k / n)). \sum_{j=0}^{k}\binom{n}{j}\leq\exp(n\cdot h(k/n)). |  |

###### Proof.

Fix integers k k and n n satisfying 0 ≤ k ≤ n 0\leq k\leq n and let Σ \Sigma denote the left-hand side of the asserted inequality. Denote by ( X 1, …, X n) ∈ { 0, 1 } n (X_{1},\dotsc,X_{n})\in\{0,1\}^{n} the characteristic function of the uniformly random subset of ⟦ n ⟧ ≔ { 1, …, n } \llbracket{n}\rrbracket\coloneqq\{1,\dotsc,n\} of cardinality at most k k. By 1.2 and 1.6 and the definition of h h,

 | log ⁡ Σ = H ⁡ ( X 1, …, X n) ≤ ∑ i = 1 n H ⁡ ( X i) = ∑ i = 1 n h ⁡ ( 𝔼 ⁡ [X i]). \log\Sigma=H(X_{1},\dotsc,X_{n})\leq\sum_{i=1}^{n}H(X_{i})=\sum_{i=1}^{n}h(\Ex[X_{i}]). |  |

By symmetry, for each i i,

 | n ⋅ 𝔼 ⁡ [X i] = ∑ j = 1 n 𝔼 ⁡ [X j] = 𝔼 ⁡ [∑ j = 1 n X j] ≤ k, n\cdot\Ex[X_{i}]=\sum_{j=1}^{n}\Ex[X_{j}]=\Ex\left[\sum_{j=1}^{n}X_{j}\right]\leq k, |  |

which implies that

 | h ⁡ ( 𝔼 ⁡ [X i]) ≤ sup { h ⁡ ( p): 0 ≤ p ≤ k / n }. h(\Ex[X_{i}])\leq\sup\{h(p):0\leq p\leq k/n\}. |  |

Assume now that k ≤ n / 2 k\leq n/2. The claimed inequality follows after we observe that h ′ ​ ( p) = log ⁡ ( ( 1 − p) / p) h^{\prime}(p)=\log((1-p)/p) for all p ∈ ( 0, 1) p\in(0,1), which means that h h is increasing on [0, 1 / 2] [0,1/2]. ∎

### 1.4. Relative entropy.

Entropy is a special case of the much more general concept of relative entropy, first introduced by Kullback and Leibler [68]. Given two probability distributions P P and Q Q defined on the same finite set 𝒳 \mathcal{X} and such that Q Q is absolutely continuous 3 3 3 Recall that this means that Q ⁡ ( x) = 0 Q(x)=0 for every x ∈ 𝒳 x\in\mathcal{X} such that P ⁡ ( x) = 0 P(x)=0 with respect to P P (which we will denote from now on by Q ≪ P Q\ll P) we define the *relative entropy*of Q Q from P P (also called the *Kullback–Leibler divergence*of Q Q from P P) by

 | D KL ( Q ∥ P) ≔ ∑ x ∈ 𝒳 Q ( x) log Q ⁡ ( x) P ⁡ ( x). \DKulLei({Q}\,\|\,{P})\coloneqq\sum_{x\in\mathcal{X}}Q(x)\log\frac{Q(x)}{P(x)}. |  |

In the sequel, we shall often identify an 𝒳 \mathcal{X} -valued random variable X X with its probability distribution, denoted by ℒ ⁡ ( X) \mathcal{L}(X). In particular, D KL ( X ∥ Y) \DKulLei({X}\,\|\,{Y}) is nothing else than D KL ( ℒ ( X) ∥ ℒ ( Y)) \DKulLei({\mathcal{L}(X)}\,\|\,{\mathcal{L}(Y)}).

An information-theoretic motivation for the above definition is based on the notion of cross-entropy. One of the main findings of the celebrated work of Shannon [96] is that the ideal lossless coding scheme optimised for outcomes of a discrete random variable X X uses H ⁡ ( X) H(X) units of information on average. The *cross-entropy*of X X relative to another random variable Y Y taking the same set of values, which we will denote here by H ⁡ ( X, Y) H(X;Y), is the expected number of units of information used by the coding scheme optimised for Y Y while encoding outcomes of X X; in other words,

 | H ( X; Y) ≔ − ∑ x ∈ 𝒳 ℙ ( X = x) log ℙ ( Y = x). H(X;Y)\coloneqq-\sum_{x\in\mathcal{X}}\mathbb{P}(X=x)\log\mathbb{P}(Y=x). |  |

Now, the relative entropy of X X from Y Y is the difference between the cross-entropy H ⁡ ( X, Y) H(X;Y) and the real entropy of X X, that is,

(1) |  | D KL ( X ∥ Y) = H ( X; Y) − H ( X). \DKulLei({X}\,\|\,{Y})=H(X;Y)-H(X). |  |

In other words, D KL ( X ∥ Y) \DKulLei({X}\,\|\,{Y}) is the average excess amount of information wasted by using the coding scheme optimised for Y Y in order to encode the outcomes of X X. Finally, let U 𝒳 U_{\mathcal{X}} denote the uniformly chosen random element of a finite set 𝒳 \mathcal{X}. It is easily checked that every 𝒳 \mathcal{X} -valued random variable X X satisfies H ⁡ ( X, U 𝒳) = log ⁡ | 𝒳 | H(X;U_{\mathcal{X}})=\log|\mathcal{X}|, and thus ( 1) implies that

(2) |  | H ( X) = log | 𝒳 | − D KL ( X ∥ U 𝒳), H(X)=\log|\mathcal{X}|-\DKulLei({X}\,\|\,{U_{\mathcal{X}}}), |  |

which explains why relative entropy generalises the notion of entropy.

The key property of relative entropy is that it is always nonnegative.

###### 1.10.

For every pair P, Q P,Q of distributions (on a finite set 𝒳 \mathcal{X}) that satisfy Q ≪ P Q\ll P, we have

 | D KL ( Q ∥ P) ≥ 0. \DKulLei({Q}\,\|\,{P})\geq 0. |  |

Moreover, equality holds if and only if P = Q P=Q.

###### Proof.

Since log ⁡ y ≥ 1 − 1 / y \log y\geq 1-1/y for all y ∈ ( 0, ∞) y\in(0,\infty), and the inequality is strict unless y = 1 y=1, we have

 | D KL ( Q ∥ P) = ∑ x ∈ 𝒳 Q ⁡ ( x) > 0 Q ( x) log Q ⁡ ( x) P ⁡ ( x) ≥ ∑ x ∈ 𝒳 Q ⁡ ( x) > 0 Q ( x) ( 1 − P ⁡ ( x) Q ⁡ ( x)) ≥ ∑ x ∈ 𝒳 Q ( x) − ∑ x ∈ 𝒳 P ( x) = 0 \DKulLei({Q}\,\|\,{P})=\sum_{\begin{subarray}{c}x\in\mathcal{X}\\ Q(x)>0\end{subarray}}Q(x)\log\frac{Q(x)}{P(x)}\geq\sum_{\begin{subarray}{c}x\in\mathcal{X}\\ Q(x)>0\end{subarray}}Q(x)\left(1-\frac{P(x)}{Q(x)}\right)\geq\sum_{x\in\mathcal{X}}Q(x)-\sum_{x\in\mathcal{X}}P(x)=0 |  |

and equality holds throughout if and only if P ⁡ ( x) = Q ⁡ ( x) P(x)=Q(x) for all x ∈ 𝒳 x\in\mathcal{X}. ∎

Observe that 1.10, together with ( 2), implies 1.2. Interestingly, 1.5, 1.6, and 1.7 can also be deduced from nonnegativity of relative entropy between carefully chosen pairs of distributions. For example, 1.6 is an immediate consequence of the following identity, where we write Y ⊗ Z Y\otimes Z for the random vector whose coordinates are independent and have the same distributions as Y Y and Z Z, respectively:

(3) |  | H ( X 1) + ⋯ + H ( X n) − H ( X 1, ⋯, X n) = D KL ( ( X 1, …, X n) ∥ X 1 ⊗ ⋯ ⊗ X n). H(X_{1})+\dotsb+H(X_{n})-H(X_{1},\dotsb,X_{n})=\DKulLei({(X_{1},\dotsc,X_{n})}\,\|\,{X_{1}\otimes\dotsb\otimes X_{n}}). |  |

We state one more useful consequence of 1.10, commonly known as the *data processing inequality*. Roughly speaking, it states that applying the same deterministic transformation to a pair of random variables cannot increase their relative entropy.

###### 1.11.

Suppose that random variables X X and Y Y take values in the same finite set 𝒳 \mathcal{X} and satisfy ℒ ⁡ ( X) ≪ ℒ ⁡ ( Y) \mathcal{L}(X)\ll\mathcal{L}(Y). For every set 𝒯 \mathcal{T} and every function T: 𝒳 → 𝒯 T\colon\mathcal{X}\to\mathcal{T}, we have

 | D KL ( T ( X) ∥ T ( Y)) ≤ D KL ( X ∥ Y). \DKulLei({T(X)}\,\|\,{T(Y)})\leq\DKulLei({X}\,\|\,{Y}). |  |

###### Proof.

The claimed inequality follows as

(4) |  | D KL ( X ∥ Y) − D KL ( T ( X) ∥ T ( Y)) = ∑ x ∈ 𝒳 ℙ ( X = x) log ℙ ⁡ ( X = x) ​ ℙ ​ ( T ⁡ ( Y) = T ⁡ ( x)) ℙ ⁡ ( Y = x) ​ ℙ ​ ( T ⁡ ( X) = T ⁡ ( x)) \DKulLei({X}\,\|\,{Y})-\DKulLei({T(X)}\,\|\,{T(Y)})=\sum_{x\in\mathcal{X}}\mathbb{P}(X=x)\log\frac{\mathbb{P}(X=x)\mathbb{P}(T(Y)=T(x))}{\mathbb{P}(Y=x)\mathbb{P}(T(X)=T(x))} |  |

and it is easily checked that the function P: 𝒳 → [0, ∞) P\colon\mathcal{X}\to[0,\infty) defined by

 | P ⁡ ( x) ≔ ℙ ⁡ ( T ⁡ ( X) = T ⁡ ( x)) ℙ ⁡ ( T ⁡ ( Y) = T ⁡ ( x)) ⋅ ℙ ⁡ ( Y = x) P(x)\coloneqq\frac{\mathbb{P}(T(X)=T(x))}{\mathbb{P}(T(Y)=T(x))}\cdot\mathbb{P}(Y=x) |  |

is a probability distribution satisfying ℒ ⁡ ( X) ≪ P \mathcal{L}(X)\ll P and thus ( 4) is equal to the nonnegative quantity D KL ( X ∥ P) \DKulLei({X}\,\|\,{P}). ∎

### 1.5. Organisation.

In the remainder of the article, we attempt to survey the many uses of entropy methods in extremal and probabilistic combinatorics. We organise the surveyed papers around common themes and conceptual threads, aiming to maintain a chronological order: the chain rule with randomised order of conditioning ( Section 2), Shearer’s inequality ( Section 3), constructing random graph homomorphisms with large entropy ( Section 4), Pinsker’s inequality and the interplay between entropy and independence ( Section 5), the recent breakthrough on the union-closed sets conjecture ( Section 6), and the very recent entropy-based approach to Turán-type problems ( Section 7).

## 2. Randomised chain rule.

One of the most striking and influential applications of entropy in combinatorics is the beautiful proof of the following conjecture of Minc [83] due to Jaikumar Radhakrishnan [90].

###### 2.1 Minc.

Suppose that M M is an n × n n\times n matrix with all entries in { 0, 1 } \{0,1\} whose row sums are d 1, …, d n d_{1},\dotsc,d_{n}. Then, the permanent of M M is at most ∏ i = 1 n ( d i!) 1 / d i \prod_{i=1}^{n}(d_{i}!)^{1/d_{i}}.

Minc’s conjecture was proved by Brégman [12] and, a few years later, Schrijver [95] found a shorter proof (whose randomised version is presented in [2, Chapter 2]). However, it is the beautiful entropy-based argument due to Radhakrishnan that is considered the ‘book’ proof of this result (see [1, Chapter 37]). The core idea of Radhakrishnan’s argument, which we will term here the *randomised chain rule*, proved to be extremely flexible and it has been adapted by a great number of later works. Notably, Cuckler and Kahn [28] used this method to prove an upper bound on the number of perfect matchings and Hamilton cycles in a graph, which they also matched from below [29]; their results have recently been generalised to hypergraphs [31, 56, 70]. In another notable application of the randomised chain rule, Linial and Luria prove upper bounds on the number of Steiner triple systems [75] and high-dimensional permutations [76]; the former bound was later extended to ( n, q, r, λ) (n,q,r,\lambda) -designs, for arbitrary fixed q q, r r, λ \lambda and large n n, by Keevash [60], whose remarkable work [58] supplies matching lower bounds. Further applications of the randomised chain rule include [11, 18, 30, 71, 80, 99, 101].

Consider the problem of estimating the entropy of a random vector X = ( X i) i ∈ I ∈ A I X=(X_{i})_{i\in I}\in A^{I}, where A A and I I are two finite sets. Given a linear order ≺ \prec on the set of indices I I and writing X ≺ i X_{\prec i} as a shorthand for the vector ( X j) j ≺ i (X_{j})_{j\prec i}, we may use the chain rule ( 1.4) to conclude that

(5) |  | H ⁡ ( X) = ∑ i ∈ I H ⁡ ( X i ∣ X ≺ i). H(X)=\sum_{i\in I}H(X_{i}\mid X_{\prec i}). |  |

Further, given an x ∈ A I x\in A^{I} such that ℙ ⁡ ( X = x) \mathbb{P}(X=x) is nonzero, write X i ≺, x X_{i}^{\prec,x} to denote the variable X i X_{i} conditioned on the event that X ≺ i = x ≺ i X_{\prec i}=x_{\prec i}. By the definition of conditional entropy, we have

(6) |  | H ⁡ ( X i ∣ X ≺ i) = 𝔼 ⁡ [H ⁡ ( X i ≺, x)], H(X_{i}\mid X_{\prec i})=\Ex[H(X_{i}^{\prec,x})], |  |

where the expectation averages over x x that is sampled according to X X. The key realisation that underlies the argument of Radhakrishnan is that both ( 5) and ( 6) hold also for a random ordering ≺ \prec and therefore

(7) |  | H ⁡ ( X) = ∑ i ∈ I 𝔼 ⁡ [H ⁡ ( X i ≺, x)], H(X)=\sum_{i\in I}\Ex[H(X_{i}^{\prec,x})], |  |

where the expectation averages over both x x and the random ordering ≺ \prec. Crucially, even though we obtained ( 7) by first averaging over x x (randomness inherent in the problem) and then over ≺ \prec (external randomness we injected to the argument), we may now attempt to evaluate each term in the right-hand side of ( 7) by switching the order of these two expectations.

In a typical application of this scheme, the random vector X X is a uniformly random element of some 𝒳 ⊆ A I \mathcal{X}\subseteq A^{I}, so that H ⁡ ( X) = log ⁡ | 𝒳 | H(X)=\log|\mathcal{X}|, and the entropy X i ≺, x X_{i}^{\prec,x} is bounded from above by the logarithm of the size of the set A i ≺, x A_{i}^{\prec,x} of all possible values that this variable can assume, that is,

 | A i ≺, x ≔ { y i: y ∈ 𝒳 ​ and ​ y ≺ i = x ≺ i }. A_{i}^{\prec,x}\coloneqq\{y_{i}:y\in\mathcal{X}\text{ and }y_{\prec i}=x_{\prec i}\}. |  |

This leads to the following upper bound on the size of 𝒳 \mathcal{X}, first stated in this general form as [85, Lemma 4].

###### 2.2.

Let A A and I I be finite sets and let ≺ \prec be a random ordering of I I. For every nonempty 𝒳 ⊆ A I \mathcal{X}\subseteq A^{I},

 | log ⁡ | 𝒳 | ≤ ∑ i ∈ I 𝔼 ⁡ [log ⁡ | A i ≺, x |], \log|\mathcal{X}|\leq\sum_{i\in I}\Ex\left[\log|A_{i}^{\prec,x}|\right], |  |

where the expectation averages over both ≺ \prec and a uniformly random x ∈ 𝒳 x\in\mathcal{X}.

As an illustration, we prove the following result, which is implicit in the work of Linial and Luria [75].

###### 2.3 [75, 80].

Suppose that ℋ \mathcal{H} is a k k -uniform, d d -regular, n n -vertex linear hypergraph. The number M ⁡ ( ℋ) M(\mathcal{H}) of perfect matchings in ℋ \mathcal{H} satisfies, as d 1 / ( k − 1) → ∞ d^{1/(k-1)}\to\infty,

 | log ⁡ M ⁡ ( ℋ) ≤ n k ⋅ ( log ⁡ d − ( k − 1) ⋅ ( 1 − o ⁡ ( 1))). \log M(\mathcal{H})\leq\frac{n}{k}\cdot\bigl(\log d-(k-1)\cdot(1-o(1))\bigr). |  |

Since a Steiner triple system on ⟦ n ⟧ \llbracket{n}\rrbracket is nothing else than a perfect matching in the (linear) 3 3 -uniform hypergraph with vertex set E ⁡ ( K n) E(K_{n}) whose hyperedges are the edge sets of triangles of K n K_{n}, Theorem 2.3 implies that there are at most

 | exp ⁡ ( 1 3 ​ ( n 2) ⋅ ( log ⁡ ( n − 2) − 2 + o ⁡ ( 1))) = ( ( 1 + o ⁡ ( 1)) ⋅ n e 2) n 2 / 6 \exp\left(\frac{1}{3}\binom{n}{2}\cdot\bigl(\log(n-2)-2+o(1)\bigr)\right)=\left((1+o(1))\cdot\frac{n}{e^{2}}\right)^{n^{2}/6} |  |

such Steiner triple systems; this estimate is the main result of [75]. Our presentation here will closely follow Luria [80], who proved Theorem 2.3 under the weaker assumption that Δ 2 ​ ( ℋ) = o ​ ( d) \Delta_{2}(\mathcal{H})=o(d). We work with the stronger assumption that Δ 2 ​ ( ℋ) = 1 \Delta_{2}(\mathcal{H})=1 in order to avoid a technical complication in the final part of Luria’s argument.

###### Proof of Theorem 2.3.

Denote the vertex and the edge sets of ℋ \mathcal{H} by V V and E E, respectively. Let 𝒳 \mathcal{X} denote the set of perfect matchings in ℋ \mathcal{H}, each of which can be naturally viewed as a vector in E V E^{V} (whose v v -coordinate is the unique edge of the matching that contains v v). Fix an ordering ≺ \prec of V V, a perfect matching x x, and a vertex v ∈ V v\in V. Clearly, A v ≺, x A_{v}^{\prec,x} always contains the edge x v x_{v}. The key observation, however, is that an edge f ≠ x v f\neq x_{v} can belong to the set A v ≺, x A_{v}^{\prec,x} only if v v belongs to f f and f f is disjoint from ⋃ w ≺ v x w \bigcup_{w\prec v}x_{w}. A moment of thought reveals that the latter holds if and only if v v is the ≺ \prec -smallest element of ⋃ w ∈ f x w \bigcup_{w\in f}x_{w}.

Let ≺ \prec be a uniformly chosen random ordering of V V. An elegant idea of Linial and Luria [75] is to generate ≺ \prec by first assigning to each v ∈ V v\in V a uniformly random τ v ∈ [0, 1] \tau_{v}\in[0,1] and order the vertices according to the resulting function τ: V → [0, 1] \tau\colon V\to[0,1] (which is injective with probability one) by letting v ≺ w v\prec w whenever τ v > τ w \tau_{v}>\tau_{w}. This enables us to apply Jensen’s inequality in the following way. Letting Z v ≺, x Z_{v}^{\prec,x} be the indicator of the event v ⪯ x v v\preceq x_{v}, we have

(8) |  | 𝔼 [log | A v ≺, x |] = 𝔼 [𝔼 [log | A v ≺, x | ∣ τ v, x, Z v ≺, x]] ≤ 𝔼 [log 𝔼 [| A v ≺, x | ∣ τ v, x, Z v ≺, x]]. \Ex[\log|A_{v}^{\prec,x}|]=\Ex[\Ex[\log|A_{v}^{\prec,x}|\mid\tau_{v},x,Z_{v}^{\prec,x}]]\leq\Ex[\log\Ex[|A_{v}^{\prec,x}|\mid\tau_{v},x,Z_{v}^{\prec,x}]]. |  |

As it is easy to check that, for all v ∈ V v\in V and W ⊆ V W\subseteq V,

 | ℙ ⁡ ( v ⪯ W ∣ τ v) = τ v | W ∖ { v } |, \mathbb{P}(v\preceq W\mid\tau_{v})=\tau_{v}^{|W\setminus\{v\}|}, |  |

we have, for every f ∈ E ∖ { x v } f\in E\setminus\{x_{v}\} that contains v v,

 | ℙ ( v ⪯ x v ∣ τ v, x) = τ v k − 1 and ℙ ( v ⪯ ⋃ w ∈ f x w ∣ τ v, x) = τ v | { x w: w ∈ f } | ⋅ k − 1 = τ v k 2 − 1, \mathbb{P}(v\preceq x_{v}\mid\tau_{v},x)=\tau_{v}^{k-1}\qquad\text{and}\qquad\mathbb{P}(v\preceq\bigcup_{w\in f}x_{w}\mid\tau_{v},x)=\tau_{v}^{|\{x_{w}:w\in f\}|\cdot k-1}=\tau_{v}^{k^{2}-1}, |  |

where the final equality holds thanks to our assumption that ℋ \mathcal{H} is linear (and thus every edge f f that is not in the matching x x intersects k k edges of x x). We may conclude that

 | 𝔼 [| A v ≺, x | ∣ τ v, x, Z v ≺, x] ≤ 1 + Z v ≺, x ⋅ d τ v k ⁡ ( k − 1). \Ex[|A_{v}^{\prec,x}|\mid\tau_{v},x,Z_{v}^{\prec,x}]\leq 1+Z_{v}^{\prec,x}\cdot d\tau_{v}^{k(k-1)}. |  |

Substituting this estimate into ( 8), we obtain

 | 𝔼 ⁡ [log ⁡ | A v ≺, x |] ≤ 𝔼 ⁡ [τ v k − 1 ⋅ log ⁡ ( 1 + d ​ τ v k ⁡ ( k − 1))] = ∫ 0 1 t k − 1 ​ log ⁡ ( 1 + dt k ⁡ ( k − 1)) ​ dt = 1 k ⋅ ∫ 0 1 log ⁡ ( 1 + du k − 1) ​ du. \Ex[\log|A_{v}^{\prec,x}|]\leq\Ex[\tau_{v}^{k-1}\cdot\log(1+d\tau_{v}^{k(k-1)})]=\int_{0}^{1}t^{k-1}\log(1+dt^{k(k-1)})\,dt=\frac{1}{k}\cdot\int_{0}^{1}\log(1+du^{k-1})\,du. |  |

Finally, letting δ ≔ d − 1 / ( k − 1) \delta\coloneqq d^{-1/(k-1)}, we have

 | ∫ 0 1 log ⁡ ( 1 + d ​ u k − 1) ​ 𝑑 u = log ⁡ d + ∫ 0 1 log ⁡ ( δ k − 1 + u k − 1) ​ 𝑑 u ≤ log ⁡ d + ( k − 1) ​ ∫ 0 1 log ⁡ ( u + δ) ​ 𝑑 u = log ⁡ d + ( k − 1) ⋅ ( ( 1 + δ) ​ log ⁡ ( 1 + δ) − δ ​ log ⁡ δ − 1). \int_{0}^{1}\log(1+du^{k-1})\,du=\log d+\int_{0}^{1}\log(\delta^{k-1}+u^{k-1})\,du\leq\log d+(k-1)\int_{0}^{1}\log(u+\delta)\,du\\ =\log d+(k-1)\cdot\bigl((1+\delta)\log(1+\delta)-\delta\log\delta-1\bigr). |  |

Since ( 1 + δ) ​ log ⁡ ( 1 + δ) − δ ​ log ⁡ δ → 0 (1+\delta)\log(1+\delta)-\delta\log\delta\to 0 as δ → 0 \delta\to 0, the claimed upper bound on M ⁡ ( ℋ) M(\mathcal{H}) follows from Lemma 2.2. ∎

## 3. Shearer’s inequality.

Consider an arbitrary vector X X of discrete random variables whose coordinates are indexed by the elements of a finite set V V. The subadditivity property of entropy ( 1.6) implies that, for every partition 𝒫 \mathcal{P} of V V, we have

 | H ⁡ ( X) ≤ ∑ W ∈ 𝒫 H ⁡ ( X W), H(X)\leq\sum_{W\in\mathcal{P}}H(X_{W}), |  |

where we write X W ≔ ( X v) v ∈ W X_{W}\coloneqq(X_{v})_{v\in W} for the projection of X X onto the coordinates in W W. The following remarkable generalisation of this inequality was proved in 1978 by Shearer, although it first appeared in print only several years later [19].

###### 3.1 Shearer’s inequality.

Suppose that ℱ \mathcal{F} is a hypergraph on a finite set V V with minimum degree at least t t. Then, for every discrete random vector X X whose coordinates are indexed by V V, we have

 | H ⁡ ( X) ≤ 1 t ​ ∑ W ∈ ℱ H ⁡ ( X W). H(X)\leq\frac{1}{t}\sum_{W\in\mathcal{F}}H(X_{W}). |  |

We remark here that the special case ℱ = { V ∖ { v }: v ∈ V } \mathcal{F}=\{V\setminus\{v\}:v\in V\} and t = | V | − 1 t=|V|-1, which generalises the well-known Loomis–Whitney inequality [79], had been independently obtained by Te Sun Han [45]. The following ‘book’ proof of Shearer’s inequality was discovered by Llewellyn and Radhakrishnan.

###### Proof of Lemma 3.1.

Let ≺ \prec be an arbitrary ordering of the elements of V V. By 1.4 and 1.5, for every W ∈ ℱ W\in\mathcal{F}, we have

 | H ( X W) = ∑ v ∈ W H ( X v ∣ ( X w: w ≺ v, w ∈ W)) ≥ ∑ v ∈ W H ( X v ∣ X ≺ v). H(X_{W})=\sum_{v\in W}H(X_{v}\mid(X_{w}:w\prec v,w\in W))\geq\sum_{v\in W}H(X_{v}\mid X_{\prec v}). |  |

Summing the above inequality over all W ∈ ℱ W\in\mathcal{F} yields

 | ∑ W ∈ ℱ H ⁡ ( X W) ≥ ∑ v ∈ V deg ℱ ⁡ v ⋅ H ⁡ ( X v ∣ X ≺ v) ≥ t ⋅ ∑ v ∈ V H ⁡ ( X v ∣ X ≺ v) = t ⋅ H ⁡ ( X), \sum_{W\in\mathcal{F}}H(X_{W})\geq\sum_{v\in V}\deg_{\mathcal{F}}v\cdot H(X_{v}\mid X_{\prec v})\geq t\cdot\sum_{v\in V}H(X_{v}\mid X_{\prec v})=t\cdot H(X), |  |

where the second inequality holds as entropy is nonnegative and the equality is the chain rule ( 1.4). ∎

The following, purely combinatorial, corollary of the general lemma is already sufficient for many applications.

###### 3.2.

Suppose that ℱ \mathcal{F} is a hypergraph on a finite set V V with minimum degree at least t t. For every finite A A and all 𝒳 ⊆ A V \mathcal{X}\subseteq A^{V},

 | | 𝒳 | t ≤ ∏ W ∈ ℱ | 𝒳 W |, |\mathcal{X}|^{t}\leq\prod_{W\in\mathcal{F}}|\mathcal{X}_{W}|, |  |

where 𝒳 W \mathcal{X}_{W} denotes the projection of 𝒳 \mathcal{X} onto the coordinates in W W.

###### Proof.

Let X X be a uniformly chosen random vector in 𝒳 \mathcal{X}. By 1.2 and 3.1,

 | log ⁡ | 𝒳 | = H ⁡ ( X) ≤ 1 t ⋅ ∑ W ∈ ℱ H ⁡ ( X W) ≤ 1 t ⋅ ∑ W ∈ ℱ log ⁡ | 𝒳 W |, \log|\mathcal{X}|=H(X)\leq\frac{1}{t}\cdot\sum_{W\in\mathcal{F}}H(X_{W})\leq\frac{1}{t}\cdot\sum_{W\in\mathcal{F}}\log|\mathcal{X}_{W}|, |  |

as claimed. ∎

It is worth mentioning that both Lemmas 3.1 and 3.2 remain true when we allow the edges of the hypergraph ℱ \mathcal{F} to have nonnegative integer multiplicities (in which case, degrees count edges with their multiplicities); the proofs remain unchanged. A further generalisation of Corollary 3.2 to weighted hypergraphs was considered by Friedgut [39].

One particularly elegant application of Corollary 3.2, due to Friedgut and Kahn [38], gives an upper bound on the number of copies of a uniform hypergraph F F in another hypergraph with a given number of edges. Their bound generalises the earlier work of Alon [3], who obtained the same bound in the case where F F is a graph, and is best-possible up to a multiplicative constant that depends only on F F. The method of [38] was later used in [49] to prove strong bounds on the number of copies of a given graph in another graph with given numbers of edges and vertices (see also [46]). Finally, we refer the interested reader to the recent [20] for a streamlined version of the proof of the main results of [38, 49] that avoids the use of Shearer’s inequality and linear programming duality.

As an illustration of Corollary 3.2, we present here the argument of [38] in one special case, obtaining an ‘asymptotic’ version of the famous Kruskal–Katona Theorem. The *shadow*of a family ℋ \mathcal{H} of sets is the family

 | ∂ ℋ ≔ { E ∖ { v }: v ∈ E ∈ ℋ }. \partial\mathcal{H}\coloneqq\{E\setminus\{v\}:v\in E\in\mathcal{H}\}. |  |

###### 3.3.

Suppose that ℋ \mathcal{H} is a family of k k -element sets. If | ℋ | ≥ x k / k! |\mathcal{H}|\geq x^{k}/k! for some real x > 0 x>0, then | ∂ ℋ | ≥ x k − 1 / ( k − 1)! |\partial\mathcal{H}|\geq x^{k-1}/(k-1)!.

###### Proof.

Let A ≔ ⋃ ℋ A\coloneqq\bigcup\mathcal{H} and let 𝒳 ⊆ A ⟦ k ⟧ \mathcal{X}\subseteq A^{\llbracket{k}\rrbracket} be the family of all ordered sets from ℋ \mathcal{H}, so that | 𝒳 | = k! ⋅ | ℋ | ≥ x k |\mathcal{X}|=k!\cdot|\mathcal{H}|\geq x^{k}. Note that, for every i ∈ ⟦ k ⟧ i\in\llbracket{k}\rrbracket, the projection 𝒳 ⟦ k ⟧ ∖ { i } \mathcal{X}_{\llbracket{k}\rrbracket\setminus\{i\}} comprises only ordered members of ∂ ℋ \partial\mathcal{H} and thus its cardinality cannot exceed ( k − 1)! ⋅ | ∂ ℋ | (k-1)!\cdot|\partial\mathcal{H}|. Consequently, by Corollary 3.2,

 | x k ⁡ ( k − 1) ≤ | 𝒳 | k − 1 ≤ ∏ i ∈ ⟦ k ⟧ | 𝒳 ⟦ k ⟧ ∖ { i } | ≤ ( ( k − 1)! ⋅ | ∂ ℋ |) k, x^{k(k-1)}\leq|\mathcal{X}|^{k-1}\leq\prod_{i\in\llbracket{k}\rrbracket}|\mathcal{X}_{\llbracket{k}\rrbracket\setminus\{i\}}|\leq((k-1)!\cdot|\partial\mathcal{H}|)^{k}, |  |

as claimed. ∎

The recent work of Chao and Yu [15] presents another entropy-based argument that proves a strengthening of Proposition 3.3, known as Lovász’s formulation of the Kruskal–Katona Theorem, where x k / k! x^{k}/k! and x k − 1 / ( k − 1)! x^{k-1}/(k-1)! are replaced by ( x k) \binom{x}{k} and ( x k − 1) \binom{x}{k-1}, respectively. The same authors used entropy methods to prove sharp upper bounds on the number of rainbow triangles in a graph with specified numbers of red, green, and blue edges [14, 15], improving a ‘vanilla’ application of Shearer’s inequality by a constant factor.

Another extremely influential application of Shearer’s inequality drives the proof of the following upper bound on the number of homomorphisms from a regular bipartite graph to an arbitrary graph (with loops allowed).

###### 3.4 [40, 54].

For every d d -regular, N N -vertex, bipartite graph G G and every graph F F,

 | | Hom ⁡ ( G, F) | 1 / N ≤ | Hom ⁡ ( K d, d, F) | 1 / ( 2 ​ d). |\Hom(G,F)|^{1/N}\leq|\Hom(K_{d,d},F)|^{1/(2d)}. |  |

Theorem 3.4 is a result of Galvin and Tetali [40], but its proof is an adaptation of the method of Kahn [54], who obtained an upper bound on the number of independent sets in a bipartite regular graph. (The method has its roots in Kahn’s earlier work with Lawrenz [52], which studies the number of so-called rank functions on the hypercube, which are in one-to-one correspondence with homomorphisms from the hypercube to ℤ \mathbb{Z}.) In fact, Kahn’s result is a special case of the above theorem, as there is a well-known bijection between independent sets of G G and the set Hom ⁡ ( G,) \Hom(G,\hbox to24.19pt{\vbox to8.54pt{\pgfpicture\makeatletter\hbox{\hskip 1.42271pt\lower-4.26773pt\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin} \lxSVG@begingroup@{stroke} \lxSVG@begingroup@{fill} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width} \lx@inpgf@ignorespaces\nullfont\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin} {}{{}}{} {}{{}}{}{}{}{}{{}}{}\lxSVG@discardpath\lxSVG@discardpath@clipped{M -1.97 -5.91 M -1.97 -5.91 L -1.97 5.91 L 31.5 5.91 L 31.5 -5.91 Z M 31.5 5.91} \lx@inpgf@ignorespaces{{}}\lx@inpgf@ignorespaces\hbox{\hbox{{\lxSVG@begingroup@{_scopebegin} \lxSVG@begingroup@{fill} {{}{{{}}}{{}}{}{}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}{}{}{}{}{}{\lxSVG@begingroup@{_scopebegin} \lxSVG@begingroup@{fill} \lxSVG@fill\lxSVG@drawpath@unclipped{M 2.35 0 C 2.35 1.3 1.3 2.35 0 2.35 C -1.3 2.35 -2.35 1.3 -2.35 0 C -2.35 -1.3 -1.3 -2.35 0 -2.35 C 1.3 -2.35 2.35 -1.3 2.35 0 Z M 0 0}{stroke:none} \lx@inpgf@ignorespaces \lxSVG@closescope }{{{{\lx@inpgf@ignorespaces}}\lxSVG@begingroup@{_scopebegin} \lxSVG@transformcm{1.0}{0.0}{0.0}{1.0}{0.0pt}{0.0pt}\lxSVG@begingroup@{transform} \pgfsys@hbox{58}\lxSVG@closescope }}} \lxSVG@closescope }}} {{}}\lx@inpgf@ignorespaces\hbox{\hbox{{\lxSVG@begingroup@{_scopebegin} \lxSVG@begingroup@{fill} {{}{{{}}}{{}}{}{}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}{}{}{}{}{}{\lxSVG@begingroup@{_scopebegin} \lxSVG@begingroup@{fill} \lxSVG@fill\lxSVG@drawpath@unclipped{M 22.03 0 C 22.03 1.3 20.98 2.35 19.69 2.35 C 18.39 2.35 17.34 1.3 17.34 0 C 17.34 -1.3 18.39 -2.35 19.69 -2.35 C 20.98 -2.35 22.03 -1.3 22.03 0 Z M 19.69 0}{stroke:none} \lx@inpgf@ignorespaces \lxSVG@closescope }{{{{\lx@inpgf@ignorespaces}}\lxSVG@begingroup@{_scopebegin} \lxSVG@transformcm{1.0}{0.0}{0.0}{1.0}{14.22638pt}{0.0pt}\lxSVG@begingroup@{transform} \pgfsys@hbox{58}\lxSVG@closescope }}} \lxSVG@closescope }}} {{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}\lxSVG@begingroup@{_scopebegin} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width} \lx@inpgf@ignorespaces{}\lxSVG@stroke\lxSVG@drawpath@unclipped{M 2.62 0 L 17.06 0}{fill:none} \lx@inpgf@ignorespaces \lxSVG@closescope {{}}{}\lxSVG@begingroup@{_scopebegin} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width} \lx@inpgf@ignorespaces\lx@inpgf@ignorespaces\hbox{\hbox{{\lxSVG@begingroup@{_scopebegin} {{}}{} {\lx@inpgf@ignorespaces{}{}{{}}{}}{\lx@inpgf@ignorespaces{}{}{{}}{}}{{}{}\lx@inpgf@ignorespaces}{{}} {\lx@inpgf@ignorespaces{}{}{{}}{}}{{{}}{{}}}{{}}{\lx@inpgf@ignorespaces{}{}{{}}{}}{{{}}{{}}}{{}}{}{{}}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{{{{{{}}{}{}{}{}{{}}}}}{}{}{}{}}{}\lxSVG@stroke\lxSVG@drawpath@unclipped{M 21.54 -1.86 C 33.28 -13.6 33.28 13.6 21.54 1.86}{fill:none} \lx@inpgf@ignorespaces \lxSVG@closescope }}} \lxSVG@closescope \lxSVG@closescope {}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}\hss}\lxSVG@discardpath\lxSVG@closescope \hss}}\lxSVG@closescope\endpgfpicture}}). The strongest result proved in [40] is a generalisation of Theorem 3.4 to the setting of weighted graph homomorphisms, where the vertices of F F are assigned positive real weights via some λ: V ⁡ ( F) → ( 0, ∞) \lambda\colon V(F)\to(0,\infty) and the weight of a homomorphism f ∈ Hom ⁡ ( G, F) f\in\Hom(G,F) is ∏ v ∈ V ⁡ ( G) λ f ⁡ ( v) \prod_{v\in V(G)}\lambda_{f(v)}; this more general result is deduced from Theorem 3.4 by relating the sum of weights of all homomorphisms to the number of homomorphisms to an appropriate blowup of F F.

Various extensions and variations of the entropy-based method of proof Theorem 3.4 were used by many authors not only to give tighter bounds on the number of homomorphisms from G G to F F under further assumptions on G G, but also to describe the typical structure of randomly chosen such homomorphism. Some highlights include: the works of Kahn on the typical structure of a random independent set in the hypercube [54] and a random homomorphism from the hypercube to ℤ \mathbb{Z} [51], further sharpened by Galvin [42], and the number of antichains in the Boolean lattice [55]; and the works of Engbers and Galvin that give a rough description of the typical structure of a random homomorphism from an arbitrary regular bipartite graph [35] as well as a finer description in the case where this graph is a high-dimensional torus [34]. Several more recent works combine entropy arguments with the method of graph containers to prove extremely precise results on the typical structure of random graph homomorphisms from the hypercube [53, 74], high-dimensional tori [50], the nearest-neighbour graph on ℤ d \mathbb{Z}^{d} [87, 88], and bipartite expanders [67]. Finally, we mention that the recent work [5] uses the method of proof of Theorem 3.4 to give sharp upper bounds on the number of independent sets in certain regular hypergraphs.

###### Proof of Theorem 3.4.

Let f: V ⁡ ( G) → V ⁡ ( F) f\colon V(G)\to V(F) be a uniformly chosen random homomorphism from G G to F F, so that H ⁡ ( f) = log ⁡ | Hom ⁡ ( G, F) | H(f)=\log|\Hom(G,F)|, and let V ⁡ ( G) = V 0 ∪ V 1 V(G)=V_{0}\cup V_{1} be an arbitrary bipartition of G G. Writing f W f_{W} for the restriction of f f to a subset W ⊆ V ⁡ ( G) W\subseteq V(G), we may use the chain rule ( 1.4) to obtain

(9) |  | H ⁡ ( f) = H ⁡ ( f V 0) + H ⁡ ( f V 1 ∣ f V 0). H(f)=H(f_{V_{0}})+H(f_{V_{1}}\mid f_{V_{0}}). |  |

Since every vertex in V 0 V_{0} is a neighbour of exactly d d vertices in V 1 V_{1}, we may use Shearer’s inequality to bound the first term in the right-hand side of ( 9) as follows:

 | H ⁡ ( f V 0) ≤ 1 d ⋅ ∑ v ∈ V 1 H ⁡ ( f N v). H(f_{V_{0}})\leq\frac{1}{d}\cdot\sum_{v\in V_{1}}H(f_{N_{v}}). |  |

Further, using 1.5 and 1.7, we bound the second term in the right-hand side of ( 9) as follows:

 | H ⁡ ( f V 1 ∣ f V 0) ≤ ∑ v ∈ V 1 H ⁡ ( f v ∣ f V 0) ≤ ∑ v ∈ V 1 H ⁡ ( f v ∣ f N v), H(f_{V_{1}}\mid f_{V_{0}})\leq\sum_{v\in V_{1}}H(f_{v}\mid f_{V_{0}})\leq\sum_{v\in V_{1}}H(f_{v}\mid f_{N_{v}}), |  |

where N v N_{v} denotes the neighbourhood of v v in G G. Substituting these two upper bounds back into ( 9), we obtain the key inequality

 | d ⋅ H ⁡ ( f) ≤ ∑ v ∈ V 1 ( H ⁡ ( f N v) + d ⋅ H ⁡ ( f v ∣ f N v)). d\cdot H(f)\leq\sum_{v\in V_{1}}\bigl(H(f_{N_{v}})+d\cdot H(f_{v}\mid f_{N_{v}})\bigr). |  |

The crux of the argument is to realise that each term in the above sum is the entropy of a random homomorphism from the complete bipartite graph K d, d K_{d,d} to F F. Indeed, one may define such random g v ∈ Hom ⁡ ( K d, d, F) g^{v}\in\Hom(K_{d,d},F) as follows. Denote the two partite sets of K d, d K_{d,d} by A A and B B, let φ v: A → N v \varphi^{v}\colon A\to N_{v} be an arbitrary bijection, and let g A v = f φ v ​ ( A) g_{A}^{v}=f_{\varphi^{v}(A)}. Further, conditioned on g A v g_{A}^{v}, the vector g B v g_{B}^{v} comprises d d independent copies of f v f_{v} conditioned on f N v f_{N_{v}}. Since f f is a homomorphism and B B is an independent set, the resulting function g v g^{v} is also a homomorphism. Most importantly, by construction and 1.7,

 | H ⁡ ( g v) = H ⁡ ( g A v) + H ⁡ ( g B v ∣ g A v) = H ⁡ ( g A v) + ∑ b ∈ B H ⁡ ( g b v ∣ g A v) = H ⁡ ( f N v) + d ⋅ H ⁡ ( f v ∣ f N v). H(g^{v})=H(g^{v}_{A})+H(g^{v}_{B}\mid g^{v}_{A})=H(g^{v}_{A})+\sum_{b\in B}H(g_{b}^{v}\mid g_{A}^{v})=H(f_{N_{v}})+d\cdot H(f_{v}\mid f_{N_{v}}). |  |

Since H ⁡ ( g v) ≤ log ⁡ | Hom ⁡ ( K d, d, F) | H(g^{v})\leq\log|\Hom(K_{d,d},F)| for each v v, by 1.2, we obtain

 | d ⋅ log ⁡ | Hom ⁡ ( G, F) | = d ⋅ H ⁡ ( f) ≤ | V 1 | ⋅ log ⁡ | Hom ⁡ ( K d, d, F) | = N / 2 ⋅ log ⁡ | Hom ⁡ ( K d, d, F) |, d\cdot\log|\Hom(G,F)|=d\cdot H(f)\leq|V_{1}|\cdot\log|\Hom(K_{d,d},F)|=N/2\cdot\log|\Hom(K_{d,d},F)|, |  |

which is equivalent to the claimed inequality. ∎

As a final illustration of the usefulness of Shearer’s inequality, we present a generalisation of a beautiful entropy-based proof of the edge-isoperimetric inequality for the hypercube discovered by Boucheron, Lugosi, and Massart [10]. Our presentation here closely follows [32], where optimal edge-isoperimetric inequalities are proved for a much broader class of graphs. Given positive integers m m and n n, we denote by K m n K_{m}^{n} the Cartesian product of n n complete graphs K m K_{m}, that is, the graph with vertex set ⟦ m ⟧ n \llbracket{m}\rrbracket^{n} whose edges are pairs of vectors that differ in exactly one coordinate, so that K 2 n K_{2}^{n} is the n n -dimensional hypercube graph.

###### 3.5.

For all integers m ≥ 2 m\geq 2 and n ≥ 1 n\geq 1 and every nonempty A ⊆ ⟦ m ⟧ n A\subseteq\llbracket{m}\rrbracket^{n}, we have

 | e K m n ​ ( A, A c) ≥ | A | ⋅ ( m − 1) ​ ( n − log m ⁡ | A |). e_{K_{m}^{n}}(A,A^{c})\geq|A|\cdot(m-1)(n-\log_{m}|A|). |  |

###### Proof.

Let X = ( X 1, …, X n) X=(X_{1},\dotsc,X_{n}) be a uniformly chosen random vertex of A A. For every v ∈ ⟦ m ⟧ n v\in\llbracket{m}\rrbracket^{n} and each i ∈ ⟦ n ⟧ i\in\llbracket{n}\rrbracket, denote by v ( i) v_{(i)} the projection of v v along the i i th coordinate, that is, v ( i) = ( v 1, …, v i − 1, v i + 1, …, v n) v_{(i)}=(v_{1},\dotsc,v_{i-1},v_{i+1},\dotsc,v_{n}). Further, given an x ∈ A x\in A, let A i ​ ( x) ⊆ ⟦ m ⟧ A_{i}(x)\subseteq\llbracket{m}\rrbracket denote the support of X i X_{i} conditioned on X ( i) = x ( i) X_{(i)}=x_{(i)}. Our first observation is that

 | e K m n ​ ( A, A c) = ∑ x ∈ A ∑ i = 1 n ( m − | A i ​ ( x) |). e_{K_{m}^{n}}(A,A^{c})=\sum_{x\in A}\sum_{i=1}^{n}(m-|A_{i}(x)|). |  |

Now, denoting by k i k_{i} the (random) size of A i ​ ( X) A_{i}(X), we may rewrite the above identity as

 | e K m n ​ ( A, A c) = | A | ⋅ ∑ i = 1 n 𝔼 ⁡ [m − k i]. e_{K_{m}^{n}}(A,A^{c})=|A|\cdot\sum_{i=1}^{n}\Ex[m-k_{i}]. |  |

The key idea is to define the affine function ψ: [0, log ⁡ m] → ℝ \psi\colon[0,\log m]\to\mathbb{R} by ψ ⁡ ( x) ≔ ( m − 1) ​ ( 1 − x / log ⁡ m) \psi(x)\coloneqq(m-1)(1-x/\log m) and observe that ψ ⁡ ( log ⁡ k) ≤ m − k \psi(\log k)\leq m-k for every k ∈ ⟦ m ⟧ k\in\llbracket{m}\rrbracket. Consequently,

 | e K m n ​ ( A, A c) ≥ | A | ⋅ ∑ i = 1 n 𝔼 ⁡ [ψ ⁡ ( log ⁡ k i)] = | A | ⋅ ∑ i = 1 n ψ ⁡ ( 𝔼 ⁡ [log ⁡ k i]) = | A | ⋅ n ⋅ ψ ⁡ ( 1 n ​ ∑ i = 1 n 𝔼 ⁡ [log ⁡ k i]). e_{K_{m}^{n}}(A,A^{c})\geq|A|\cdot\sum_{i=1}^{n}\Ex[\psi(\log k_{i})]=|A|\cdot\sum_{i=1}^{n}\psi\bigl(\Ex[\log k_{i}]\bigr)=|A|\cdot n\cdot\psi\left(\frac{1}{n}\sum_{i=1}^{n}\Ex[\log k_{i}]\right). |  |

Since 𝔼 ⁡ [log ⁡ k i] \Ex[\log k_{i}] is precisely the conditional entropy H ⁡ ( X i ∣ X ( i)) H(X_{i}\mid X_{(i)}), Shearer’s inequality (or even the weaker Han’s inequality) implies that

 | ∑ i = 1 n 𝔼 ⁡ [log ⁡ k i] = ∑ i = 1 n H ⁡ ( X i ∣ X ( i)) = n ⋅ H ⁡ ( X) − ∑ i = 1 n H ⁡ ( X ( i)) ≤ H ⁡ ( X) = log ⁡ | A |. \sum_{i=1}^{n}\Ex[\log k_{i}]=\sum_{i=1}^{n}H(X_{i}\mid X_{(i)})=n\cdot H(X)-\sum_{i=1}^{n}H(X_{(i)})\leq H(X)=\log|A|. |  |

Since ψ \psi is decreasing, we may conclude that

 | e K m n ​ ( A, A c) ≥ | A | ⋅ n ⋅ ψ ⁡ ( ( log ⁡ | A |) / n) = | A | ⋅ ( m − 1) ​ ( n − log m ⁡ | A |), e_{K_{m}^{n}}(A,A^{c})\geq|A|\cdot n\cdot\psi\bigl((\log|A|)/n\bigr)=|A|\cdot(m-1)(n-\log_{m}|A|), |  |

as claimed. ∎

## 4. Random homomorphisms with large entropy.

In the previous section, we showed how entropy methods can be used to prove upper bounds on the number of homomorphisms from a regular bipartite graph G G to an arbitrary graph F F. The reason why this is possible is that log ⁡ | Hom ⁡ ( G, F) | \log|\Hom(G,F)| may be viewed as the entropy of a uniformly chosen random f ∈ Hom ⁡ ( G, F) f\in\Hom(G,F) and, as the proof of Theorem 3.4 shows, H ⁡ ( f) H(f) can be bounded from above using Shearer’s inequality ( Lemma 3.1). In principle, we could also prove a lower bound on the number of homomorphisms by supplying a lower bound on the entropy of a uniformly random f ∈ Hom ⁡ ( G, F) f\in\Hom(G,F). However, since the distribution of f f can be difficult to analyse, this approach seems intractable. Kopparty and Rossman [63] pioneered the following striking alternative to this idea: Since the logarithm of | Hom ⁡ ( G, F) | |\Hom(G,F)| is bounded from below by the entropy of *any*probability distribution on Hom ⁡ ( G, F) \Hom(G,F) (by 1.2), one may obtain lower bounds on | Hom ⁡ ( G, F) | |\Hom(G,F)| by constructing distributions that still have large entropies but exhibit more independence, which makes them easier to analyse.

The basic method of Kopparty and Rossman has been adapted and generalised by multitude of subsequent works, mostly in the context of the notorious conjecture of Erdős and Simonovits [36] and Sidorenko [98, 97]. Given graphs F F and G G, we define

 | t ⁡ ( F, G) ≔ | Hom ⁡ ( F, G) | ⋅ v G − v F; t(F,G)\coloneqq|\Hom(F,G)|\cdot v_{G}^{-v_{F}}; |  |

in other words, t ⁡ ( F, G) t(F,G) is the probability that a random function f: V ⁡ ( F) → V ⁡ ( G) f\colon V(F)\to V(G) is a homomorphism.

###### 4.1 Sidorenko and Erdős–Simonovits.

For every bipartite graph F F and all G G,

 | t ⁡ ( F, G) ≥ t ​ ( K 2, G) e F. t(F,G)\geq t(K_{2},G)^{e_{F}}. |  |

Although Conjecture 4.1 remains open, it has been shown to be true for many special families of F F. What makes it relevant to us is that most of the recent progress on the conjecture has relied on generalisations of the entropy-based method of Kopparty and Rossman. The first to explore these ideas were Li and Szegedy [73], closely followed by Kim, Lee, and Lee [62]; in both of these works, entropy appears only implicitly. Having said that, the following later works [24, 25, 100] explicitly follow the general scheme outlined above. Several other works used similar approaches to study a number of related problems. In particular: Kamčev, Liebanau, and Morrison [57] study analogues of Conjecture 4.1 in the context of systems of linear equations; Lee [72] gives lower bounds on t ⁡ ( F, G) t(F,G) for a class of nonbipartite F F under the assumption that G G is ‘locally dense’; and the papers [7, 44, 66] use similar entropy-based arguments in the closely-related context of commonality of graphs. Finally, given a pair F, F ′ F,F^{\prime} of graphs, one can consider generalising the inequality appearing in Conjecture 4.1 to t ​ ( F, G) 1 / e F ≥ t ​ ( F ′, G) 1 / e F ′ t(F,G)^{1/e_{F}}\geq t(F^{\prime},G)^{1/e_{F^{\prime}}} and ask when it is valid for all G G. For example, Erdős and Simonovits conjectured that it holds when F F and F ′ F^{\prime} are both paths of odd lengths and e F ≥ e F ′ e_{F}\geq e_{F}^{\prime}, which was proved by Sağlam [93]; an entropy-based proof of this conjecture was given in [8]. The case where both F F and F ′ F^{\prime} are trees is studied, using entropy techniques, in [6].

In order to add some substance to the above discussion, we use an adaptation of the method of Kopparty and Rossman [63] to show that 4.1 is true for every connected bipartite graph F F that contains a ‘dominating’ vertex, which was originally proved by Conlon, Fox, and Sudakov [23] using the technique of dependent random choice (see the excellent survey of Fox and Sudakov [37]).

###### 4.2.

Suppose that F F is a connected bipartite graph with bipartition V ⁡ ( F) = A ∪ B V(F)=A\cup B such that some α ∈ A \alpha\in A is adjacent to all of B B. Then, for every nonempty graph G G,

 | t ⁡ ( F, G) ≥ t ​ ( K 2, G) e F. t(F,G)\geq t(K_{2},G)^{e_{F}}. |  |

###### Proof.

Let α \alpha be a vertex in A A with N α = B N_{\alpha}=B and let β \beta be an arbitrary vertex in B B. We construct a random homomorphism f ∈ Hom ⁡ ( F, G) f\in\Hom(F,G) as follows:

1. (i)

Let ( f α, f β) (f_{\alpha},f_{\beta}) be a uniformly random pair of adjacent vertices of G G.

2. (ii)

Let ( f b) b ∈ B ∖ { β } (f_{b})_{b\in B\setminus\{\beta\}} be | B | − 1 |B|-1 conditionally independent copies of f β f_{\beta} given f α f_{\alpha}.

3. (iii)

Having defined f B f_{B}, generate the variables ( f a) a ∈ A ∖ { α } (f_{a})_{a\in A\setminus\{\alpha\}} independently, conditional on f B f_{B}, so that, for each a a, the conditional distribution of f a f_{a} given f B f_{B} matches the conditional distribution of f α f_{\alpha} given f N a f_{N_{a}}.

By definition, f f is a homomorphism from F F to G G. Crucially, for every nonempty C ⊆ B C\subseteq B,

(10) |  | H ⁡ ( f α, f C) = H ⁡ ( f α) + H ⁡ ( f C ∣ f α) = H ⁡ ( f α) + | C | ⋅ H ⁡ ( f β ∣ f α) = | C | ⋅ H ⁡ ( f α, f β) − ( | C | − 1) ⋅ H ⁡ ( f α), H(f_{\alpha},f_{C})=H(f_{\alpha})+H(f_{C}\mid f_{\alpha})=H(f_{\alpha})+|C|\cdot H(f_{\beta}\mid f_{\alpha})=|C|\cdot H(f_{\alpha},f_{\beta})-(|C|-1)\cdot H(f_{\alpha}), |  |

where the key (second) equality is a consequence of (ii) and 1.7. Further, by (iii) and 1.5, for every a ∈ A ∖ { α } a\in A\setminus\{\alpha\} and all sets W W satisfying N a ⊆ W ⊆ V ⁡ ( F) ∖ { a } N_{a}\subseteq W\subseteq V(F)\setminus\{a\},

(11) |  | H ⁡ ( f a ∣ f W) = H ⁡ ( f a ∣ f B) = H ⁡ ( f α ∣ f N a) = H ⁡ ( f α, f N a) − H ⁡ ( f N a) = | N a | ⋅ H ⁡ ( f α, f β) − ( | N a | − 1) ⋅ H ⁡ ( f α) − H ⁡ ( f N a), \begin{split}H(f_{a}\mid f_{W})&=H(f_{a}\mid f_{B})=H(f_{\alpha}\mid f_{N_{a}})=H(f_{\alpha},f_{N_{a}})-H(f_{N_{a}})\\ &=|N_{a}|\cdot H(f_{\alpha},f_{\beta})-(|N_{a}|-1)\cdot H(f_{\alpha})-H(f_{N_{a}}),\end{split} |  |

where the last equality holds by ( 10). Let ≺ \prec be an arbitrary ordering of A ∖ { α } A\setminus\{\alpha\}. By the chain rule,

 | H ⁡ ( f) = H ⁡ ( f α, f B) + ∑ a ∈ A ∖ { α } H ⁡ ( f a ∣ f B, f α, f ≺ a), H(f)=H(f_{\alpha},f_{B})+\sum_{a\in A\setminus\{\alpha\}}H(f_{a}\mid f_{B},f_{\alpha},f_{\prec a}), |  |

where f ≺ a f_{\prec a} stands for ( f a ′) a ′ ∈ A ∖ { α }, a ′ ≺ a (f_{a^{\prime}})_{a^{\prime}\in A\setminus\{\alpha\},a^{\prime}\prec a}. Using ( 10), ( 11), and the identity e F = ∑ a ∈ A | N a | e_{F}=\sum_{a\in A}|N_{a}|, we may rewrite the above identity as

 | H ⁡ ( f) = e F ⋅ H ⁡ ( f α, f β) − ( e F − | A |) ⋅ H ⁡ ( f α) − ∑ a ∈ A ∖ { α } H ⁡ ( f N a). H(f)=e_{F}\cdot H(f_{\alpha},f_{\beta})-(e_{F}-|A|)\cdot H(f_{\alpha})-\sum_{a\in A\setminus\{\alpha\}}H(f_{N_{a}}). |  |

Finally, using the facts that H ⁡ ( f α, f β) = log ⁡ ( 2 ​ e G) H(f_{\alpha},f_{\beta})=\log(2e_{G}), that H ⁡ ( f w) ≤ log ⁡ v G H(f_{w})\leq\log v_{G} and H ⁡ ( f N w) ≤ | N w | ⋅ log ⁡ v G H(f_{N_{w}})\leq|N_{w}|\cdot\log v_{G} for every w ∈ V ⁡ ( F) w\in V(F), which all follow from 1.2, we conclude that

 | H ⁡ ( f) ≥ e F ⋅ log ⁡ ( 2 ​ e G) − ( e F − | A |) ⋅ log ⁡ v G − ( e F − | N α |) ⋅ log ⁡ v G = e F ⋅ log ⁡ ( 2 ​ e G) + ( v F − 2 ​ e F) ⋅ log ⁡ v G. H(f)\geq e_{F}\cdot\log(2e_{G})-(e_{F}-|A|)\cdot\log v_{G}-(e_{F}-|N_{\alpha}|)\cdot\log v_{G}=e_{F}\cdot\log(2e_{G})+(v_{F}-2e_{F})\cdot\log v_{G}. |  |

Since log ⁡ | Hom ⁡ ( F, G) | ≥ H ⁡ ( f) \log|\Hom(F,G)|\geq H(f), again by 1.2, we conclude that

 | log ⁡ t ⁡ ( F, G) = log ⁡ | Hom ⁡ ( F, G) | − v F ⋅ log ⁡ v G ≥ e F ⋅ ( log ⁡ ( 2 ​ e G) − 2 ​ log ​ v G) = e F ⋅ log ⁡ t ⁡ ( K 2, G). \log t(F,G)=\log|\Hom(F,G)|-v_{F}\cdot\log v_{G}\geq e_{F}\cdot\bigl(\log(2e_{G})-2\log v_{G}\bigr)=e_{F}\cdot\log t(K_{2},G). |  |

∎

## 5. Entropy and independence.

Suppose that X X and Y Y are two discrete random variables. Recall 1.6, which states that H ⁡ ( X, Y) ≤ H ⁡ ( X) + H ⁡ ( Y) H(X,Y)\leq H(X)+H(Y) and that equality holds if and only if X X and Y Y are independent. What can be said about the distribution of the vector ( X, Y) (X,Y) when we assume that H ⁡ ( X, Y) H(X,Y) is not much smaller than H ⁡ ( X) + H ⁡ ( Y) H(X)+H(Y)? One answer to this question is provided by the following beautiful inequality due to Pinsker [89]. Recall that the *total variation distance*between two distributions P P and Q Q on the same finite set 𝒳 \mathcal{X} is the quantity

 | d TV ​ ( Q, P) ≔ max ⁡ { Q ⁡ ( A) − P ⁡ ( A): A ⊆ 𝒳 }. d_{\mathrm{TV}}(Q,P)\coloneqq\max\{Q(A)-P(A):A\subseteq\mathcal{X}\}. |  |

###### 5.1 Pinsker’s inequality.

For every pair X X, Y Y of discrete random variables,

 | d TV ​ ( ( X, Y), X ⊗ Y) ≤ H ⁡ ( X) + H ⁡ ( Y) − H ⁡ ( X, Y) 2. d_{\mathrm{TV}}\bigl((X,Y),X\otimes Y\bigr)\leq\sqrt{\frac{H(X)+H(Y)-H(X,Y)}{2}}. |  |

Roughly speaking, Pinsker’s inequality says that if H ⁡ ( X, Y) H(X,Y) is ‘close’ to H ⁡ ( X) + H ⁡ ( Y) H(X)+H(Y), then X X and Y Y are ‘almost independent’. We remark that Pinsker first proved the above inequality with a greater constant; the version stated above was obtained independently by Csiszár [26], Kemperman [61], and Kullback [69]. The heart of the proof of Proposition 5.1 is the following folklore estimate. Given p ∈ ( 0, 1) p\in(0,1) and q ∈ [0, 1] q\in[0,1], define

 | d KL ( q, p) ≔ D KL ( Ber ( q) ∥ Ber ( p)) = q log q p + ( 1 − q) log 1 − q 1 − p. d_{\mathrm{KL}}(q,p)\coloneqq\DKulLei({\mathrm{Ber}(q)}\,\|\,{\mathrm{Ber}(p)})=q\log\frac{q}{p}+(1-q)\log\frac{1-q}{1-p}. |  |

###### 5.2.

For all p ∈ ( 0, 1) p\in(0,1) and q ∈ [0, 1] q\in[0,1],

 | d KL ( q, p) ≥ ( p − q) 2 2 ​ max ​ { r ⁡ ( 1 − r): min ⁡ { p, q } ≤ r ≤ max ⁡ { p, q } } ≥ 2 ( p − q) 2. d_{\mathrm{KL}}(q,p)\geq\frac{(p-q)^{2}}{2\max\{r(1-r):\min\{p,q\}\leq r\leq\max\{p,q\}\}}\geq 2(p-q)^{2}. |  |

###### Proof of Proposition 5.1.

Consider an arbitrary event A A and let T T be its indicator, so that both T ⁡ ( X, Y) T(X,Y) and T ⁡ ( X ⊗ Y) T(X\otimes Y) are Bernoulli random variables with success probabilities q ≔ ℙ ⁡ ( ( X, Y) ∈ A) q\coloneqq\mathbb{P}((X,Y)\in A) and p ≔ ℙ ⁡ ( X ⊗ Y ∈ A) p\coloneqq\mathbb{P}(X\otimes Y\in A), respectively. By ( 3) and the data processing inequality ( 1.11),

 | H ( X) + H ( Y) − H ( X, Y) = D KL ( ( X, Y) ∥ X ⊗ Y) ≥ D KL ( T ( X, Y) ∥ T ( X ⊗ Y)) = d KL ( q, p). H(X)+H(Y)-H(X,Y)=\DKulLei({(X,Y)}\,\|\,{X\otimes Y})\geq\DKulLei({T(X,Y)}\,\|\,{T(X\otimes Y)})=d_{\mathrm{KL}}(q,p). |  |

The claimed inequality follows from Lemma 5.2. ∎

Pinsker’s inequality, and its analogues, has recently proved to be a powerful tool in extremal and probabilistic combinatorics. Ellis, Friedgut, Kindler, and Yehudayoff [33] used a version of Proposition 5.1 to obtain a structural characterisation of sets for which the Loomis–Whitney inequality [79] is nearly tight. Kozma, Meyerovitch, Peled, and the author [64] used entropy methods to obtain a structural characterisation of random finite metric spaces; a version of Proposition 5.1 played a central role in the argument. Finally, a strengthening of Proposition 5.1 lies at the heart of the solution to the lower-tail problem for subgraph counts in the binomial random graph found by Kozma and the author [65]. Several other authors have independently explored the interplay between entropy and independence [22, 21, 48, 82, 84, 91].

As an illustration of the power of Proposition 5.1, we present an entropy-based proof of the following stability version of the Kruskal–Katona theorem ( Proposition 3.3), originally proved by Keevash [59]. We refer the interested reader to [65, Section 3] for another simple application of Proposition 5.1 in the context of counting triangle-free graphs.

###### 5.3.

Suppose that ℋ \mathcal{H} is a family of k k -element sets with cardinality x k / k! x^{k}/k!, for some real x > 0 x>0. If | ∂ ℋ | ≤ ( 1 + ε) ​ x k − 1 / ( k − 1)! |\partial\mathcal{H}|\leq(1+\varepsilon)x^{k-1}/(k-1)!, then there is an ⌈ x ⌉ \lceil x\rceil -element subset of V ≔ ⋃ ℋ V\coloneqq\bigcup\mathcal{H} that contains all but at most C k ​ ε 1 / 2 ​ x k − 1 / ( k − 1)! C_{k}\varepsilon^{1/2}x^{k-1}/(k-1)! members of ∂ ℋ \partial\mathcal{H}, where C k C_{k} is a constant that depends only on k k.

###### Proof.

Let U U be the uniformly chosen random ordered set in ∂ ℋ \partial\mathcal{H} and denote by π: V k − 1 → V \pi\colon V^{k-1}\to V the projection on the last coordinate. Further, for a family 𝒢 \mathcal{G} of subsets of V V and a v ∈ V v\in V, let ∂ v 𝒢 ≔ { E ∖ { v }: v ∈ E ∈ 𝒢 } \partial_{v}\mathcal{G}\coloneqq\{E\setminus\{v\}:v\in E\in\mathcal{G}\} be the link of v v in 𝒢 \mathcal{G}, cf. the definition of the shadow of 𝒢 \mathcal{G}. Given a δ ∈ [0, 1] \delta\in[0,1], define

 | V δ ≔ { v ∈ V: | ∂ v ∂ ℋ | ≤ ( 1 − δ) ​ x k − 2 / ( k − 2)! } V_{\delta}\coloneqq\{v\in V:|\partial_{v}\partial\mathcal{H}|\leq(1-\delta)x^{k-2}/(k-2)!\} |  |

and observe that

 | ( 1 − δ) ​ x k − 2 ( k − 2)! ⋅ | V ∖ V δ | ≤ ∑ v ∈ V | ∂ v ∂ ℋ | = ( k − 1) ⋅ | ∂ ℋ | ≤ ( 1 + ε) ​ x k − 1 ( k − 2)!, \frac{(1-\delta)x^{k-2}}{(k-2)!}\cdot|V\setminus V_{\delta}|\leq\sum_{v\in V}|\partial_{v}\partial\mathcal{H}|=(k-1)\cdot|\partial\mathcal{H}|\leq\frac{(1+\varepsilon)x^{k-1}}{(k-2)!}, |  |

which means that | V ∖ V δ | ≤ ( 1 + ε) / ( 1 − δ) ⋅ x |V\setminus V_{\delta}|\leq(1+\varepsilon)/(1-\delta)\cdot x. In particular, if we let R R be a randomly chosen set of min ⁡ { ⌈ x ⌉, | V ∖ V δ | } \min\{\lceil x\rceil,|V\setminus V_{\delta}|\} vertices of V ∖ V δ V\setminus V_{\delta}, every v ∈ V ∖ V δ v\in V\setminus V_{\delta} satisfies

 | ℙ ⁡ ( v ∈ R) ≥ min ⁡ { 1, x | V ∖ V δ | } ≥ 1 − δ 1 + ε ≥ 1 − δ − ε. \mathbb{P}(v\in R)\geq\min\left\{1,\frac{x}{|V\setminus V_{\delta}|}\right\}\geq\frac{1-\delta}{1+\varepsilon}\geq 1-\delta-\varepsilon. |  |

Consequently,

 | ℙ ⁡ ( U ⊈ R) ≤ ℙ ⁡ ( U ∩ V δ ≠ ∅) + ℙ ⁡ ( U ⊈ R ∣ U ⊆ V ∖ V δ) ≤ ( k − 1) ⋅ ℙ ⁡ ( π ⁡ ( U) ∈ V δ) + ( k − 1) ⋅ ( δ + ε). \mathbb{P}(U\nsubseteq R)\leq\mathbb{P}(U\cap V_{\delta}\neq\varnothing)+\mathbb{P}(U\nsubseteq R\mid U\subseteq V\setminus V_{\delta})\leq(k-1)\cdot\mathbb{P}(\pi(U)\in V_{\delta})+(k-1)\cdot(\delta+\varepsilon). |  |

It thus suffices to show that ℙ ⁡ ( π ⁡ ( U) ∈ V δ) = O ⁡ ( ε 1 / 2) \mathbb{P}(\pi(U)\in V_{\delta})=O(\varepsilon^{1/2}) for some δ = O ⁡ ( ε 1 / 2) \delta=O(\varepsilon^{1/2}).

Let X = ( X 1, …, X k) X=(X_{1},\dotsc,X_{k}) be a uniformly chosen random ordered set of ℋ \mathcal{H}, so that H ⁡ ( X) = log ⁡ ( k! ⋅ | ℋ |) = k ​ log ⁡ x H(X)=\log(k!\cdot|\mathcal{H}|)=k\log x. Writing X ( i) X_{(i)} for the projection of X X along the i i th coordinate, Shearer’s inequality ( Lemma 3.1) implies that

 | k ⁡ ( k − 1) ⋅ log ⁡ x = ( k − 1) ⋅ H ⁡ ( X) ≤ ∑ i = 1 k H ⁡ ( X ( i)) = k ⋅ H ⁡ ( X ( 1)), k(k-1)\cdot\log x=(k-1)\cdot H(X)\leq\sum_{i=1}^{k}H(X_{(i)})=k\cdot H(X_{(1)}), |  |

which, by ( 2), means that

 | D KL ( X ( 1) ∥ U) = log ( ( k − 1)! ⋅ | ∂ ℋ |) − H ( X ( 1)) ≤ log ( 1 + ε) ≤ ε. \DKulLei({X_{(1)}}\,\|\,{U})=\log\bigl((k-1)!\cdot|\partial\mathcal{H}|\bigr)-H(X_{(1)})\leq\log(1+\varepsilon)\leq\varepsilon. |  |

Further, by the data processing inequality ( 1.11), we have

 | D KL ( X 1 ∥ π ( U)) = D KL ( X k ∥ π ( U)) = D KL ( π ( X ( 1)) ∥ π ( U)) ≤ D KL ( X ( 1) ∥ U) ≤ ε. \DKulLei({X_{1}}\,\|\,{\pi(U)})=\DKulLei({X_{k}}\,\|\,{\pi(U)})=\DKulLei({\pi(X_{(1)})}\,\|\,{\pi(U)})\leq\DKulLei({X_{(1)}}\,\|\,{U})\leq\varepsilon. |  |

We conclude that

(12) |  | D KL ( X 1 ⊗ X ( 1) ∥ π ( U) ⊗ U) = D KL ( X 1 ∥ π ( U)) + D KL ( X ( 1) ∥ U) ≤ 2 ε. \DKulLei({X_{1}\otimes X_{(1)}}\,\|\,{\pi(U)\otimes U})=\DKulLei({X_{1}}\,\|\,{\pi(U)})+\DKulLei({X_{(1)}}\,\|\,{U})\leq 2\varepsilon. |  |

We will now bound the left-hand side of ( 12) from below.

To this end, note first that

 | ∑ i = 1 k H ⁡ ( X ( i)) − ( k − 1) ⋅ H ⁡ ( X) ≤ k ⋅ log ⁡ ( ( k − 1)! ⋅ | ∂ ℋ |) − k ⁡ ( k − 1) ​ log ⁡ x ≤ k ​ log ⁡ ( 1 + ε), \sum_{i=1}^{k}H(X_{(i)})-(k-1)\cdot H(X)\leq k\cdot\log\bigl((k-1)!\cdot|\partial\mathcal{H}|\bigr)-k(k-1)\log x\leq k\log(1+\varepsilon), |  |

where the first inequality follows from 1.2. On the other hand, by the chain rule ( 1.4),

(13) |  | ( k − 1) ⋅ H ⁡ ( X) = ∑ i = 1 k ∑ j ≠ i H ⁡ ( X j ∣ X < j), (k-1)\cdot H(X)=\sum_{i=1}^{k}\sum_{j\neq i}H(X_{j}\mid X_{<j}), |  |

while the chain rule plus monotonicity of conditional entropy ( 1.5) yield

(14) |  | ∑ i = 1 k H ⁡ ( X ( i)) ≥ H ⁡ ( X ( 1)) + ∑ i = 2 k ∑ j ≠ i H ⁡ ( X j ∣ X < j). \sum_{i=1}^{k}H(X_{(i)})\geq H(X_{(1)})+\sum_{i=2}^{k}\sum_{j\neq i}H(X_{j}\mid X_{<j}). |  |

Combining ( 13) and ( 14) and using the chain rule once more, we obtain

 | ∑ i = 1 k H ⁡ ( X ( i)) − ( k − 1) ⋅ H ⁡ ( X) ≥ H ⁡ ( X ( 1)) − ∑ j = 2 k H ⁡ ( X j ∣ X < j) = H ⁡ ( X ( 1)) + H ⁡ ( X 1) − H ⁡ ( X). \sum_{i=1}^{k}H(X_{(i)})-(k-1)\cdot H(X)\geq H(X_{(1)})-\sum_{j=2}^{k}H(X_{j}\mid X_{<j})=H(X_{(1)})+H(X_{1})-H(X). |  |

Recalling identity Eq. 3, we conclude that

(15) |  | D KL ( X ∥ X 1 ⊗ X ( 1)) = H ( X ( 1)) + H ( X 1) − H ( X) ≤ k log ( 1 + ε). \DKulLei({X}\,\|\,{X_{1}\otimes X_{(1)}})=H(X_{(1)})+H(X_{1})-H(X)\leq k\log(1+\varepsilon). |  |

Finally, let T: V k → { 0, 1 } T\colon V^{k}\to\{0,1\} be the indicator of (ordered sets of) ℋ \mathcal{H} and consider the two probabilities

 | q X ≔ ℙ ⁡ ( T ⁡ ( X 1 ⊗ X ( 1)) = 0) and q U ≔ ℙ ⁡ ( T ⁡ ( π ⁡ ( U) ⊗ U) = 0). q_{X}\coloneqq\mathbb{P}\bigl(T(X_{1}\otimes X_{(1)})=0\bigr)\qquad\text{and}\qquad q_{U}\coloneqq\mathbb{P}\bigl(T(\pi(U)\otimes U)=0\bigr). |  |

By the data processing inequality ( 1.11), by ( 15), and since T ⁡ ( X) = 1 T(X)=1 with probability one,

 | − log ( 1 − q X) = d KL ( 1, 1 − q X) = D KL ( T ( X) ∥ T ( X 1 ⊗ X ( 1))) ≤ D KL ( X ∥ X 1 ⊗ X ( 1)) ≤ k log ( 1 + ε), -\log(1-q_{X})=d_{\mathrm{KL}}(1,1-q_{X})=\DKulLei({T(X)}\,\|\,{T(X_{1}\otimes X_{(1)})})\leq\DKulLei({X}\,\|\,{X_{1}\otimes X_{(1)}})\leq k\log(1+\varepsilon), |  |

which yields q X ≤ 1 − ( 1 + ε) − k ≤ k ​ ε q_{X}\leq 1-(1+\varepsilon)^{-k}\leq k\varepsilon. We claim that q U ≤ 3 ​ k ​ ε q_{U}\leq 3k\varepsilon. Indeed, either q U ≤ q X ≤ k ​ ε q_{U}\leq q_{X}\leq k\varepsilon or q U > q X q_{U}>q_{X}. In the latter case, by the data processing inequality ( 1.11),

 | D KL ( X 1 ⊗ X ( 1) ∥ π ( U) ⊗ U) ≥ D KL ( T ( X 1 ⊗ X ( 1)) ∥ T ( π ( U) ⊗ U)) = d KL ( q X, q U), \DKulLei({X_{1}\otimes X_{(1)}}\,\|\,{\pi(U)\otimes U})\geq\DKulLei({T(X_{1}\otimes X_{(1)})}\,\|\,{T(\pi(U)\otimes U)})=d_{\mathrm{KL}}(q_{X},q_{U}), |  |

and thus, by Lemma 5.2 and ( 12),

 | ( q U − k ​ ε) 2 2 ​ q U ≤ ( q U − q X) 2 2 ​ q U ≤ d KL ​ ( q X, q U) ≤ 2 ​ ε, \frac{(q_{U}-k\varepsilon)^{2}}{2q_{U}}\leq\frac{(q_{U}-q_{X})^{2}}{2q_{U}}\leq d_{\mathrm{KL}}(q_{X},q_{U})\leq 2\varepsilon, |  |

which implies that q U ≤ 3 ​ k ​ ε q_{U}\leq 3k\varepsilon.

Finally, for every v ∈ V v\in V,

 | ℙ ⁡ ( T ⁡ ( v ⊗ U) = 0) = | ∂ ℋ | − | ∂ v ℋ | | ∂ ℋ | ≥ 1 − ( k − 1)! x k − 1 ⋅ | ∂ v ℋ |, \mathbb{P}\bigl(T(v\otimes U)=0\bigr)=\frac{|\partial\mathcal{H}|-|\partial_{v}\mathcal{H}|}{|\partial\mathcal{H}|}\geq 1-\frac{(k-1)!}{x^{k-1}}\cdot|\partial_{v}\mathcal{H}|, |  |

where the last inequality holds as | ∂ ℋ | ≥ x k − 1 / ( k − 1)! |\partial\mathcal{H}|\geq x^{k-1}/(k-1)!, by the Kruskal–Katona Theorem ( Proposition 3.3). Since | ∂ v ℋ | ≤ ( 1 − δ) ​ x k − 1 / ( k − 1)! |\partial_{v}\mathcal{H}|\leq(1-\delta)x^{k-1}/(k-1)! for each v ∈ V δ v\in V_{\delta}, again by Proposition 3.3 and the fact that ∂ ∂ v ℋ = ∂ v ∂ ℋ \partial\partial_{v}\mathcal{H}=\partial_{v}\partial\mathcal{H} for every v ∈ V v\in V, we have

 | 3 ​ k ​ ε ≥ q U ≥ δ ⋅ ℙ ⁡ ( π ⁡ ( U) ∈ V δ). 3k\varepsilon\geq q_{U}\geq\delta\cdot\mathbb{P}(\pi(U)\in V_{\delta}). |  |

We may now complete the proof by taking δ ≔ 3 ​ k ​ ε \delta\coloneqq\sqrt{3k\varepsilon}. ∎

## 6. The union-closed sets conjecture.

The so-called union-closed sets conjecture, posed by Peter Frankl in 1979, is one of the most notorious conjectures in extremal set theory. It states that, for every nonempty finite family ℱ \mathcal{F} of sets that is closed under union (that is, A ∪ B ∈ ℱ A\cup B\in\mathcal{F} for every pair A, B ∈ ℱ A,B\in\mathcal{F}), there is an element x ∈ ⋃ ℱ x\in\bigcup\mathcal{F} that belongs to at least half of all the sets in ℱ \mathcal{F}. Despite its innocuous formulation, the conjecture remains open to this day. Relatively little progress towards its solution had been made until Justin Gilmer [43] found a beautiful and surprising entropy-based argument showing that every union-closed family ℱ \mathcal{F} admits an element x ∈ ⋃ ℱ x\in\bigcup\mathcal{F} that belongs to at least one percent of all sets in ℱ \mathcal{F}. Gilmer predicted that the key technical lemma in his argument could be improved to yield a stronger version of his result with one percent replaced by ( 3 − 5) / 2 ≈ 38 % (3-\sqrt{5})/2\approx 38\%. Soon afterwards, this feat was independently achieved by four groups of authors [4, 17, 86, 94]. Finally, we mention that two subsequent works [13, 102] used a modification of Gilmer’s approach (already suggested by Sawin [94]) to obtain a slightly improved bound on the maximum frequency of an element in a union-closed family.

In the remainder of this section, we present a sketch of Gilmer’s lovely argument, leaving out a key technical inequality whose proof requires some nontrivial calculus. The heart of the matter is the following beautiful theorem.

###### 6.1.

Let A A and B B be two independent samples from a distribution over subsets of ⟦ n ⟧ \llbracket{n}\rrbracket. If H ⁡ ( A) > 0 H(A)>0 and max i ⁡ ℙ ⁡ ( i ∈ A) < ( 3 − 5) / 2 \max_{i}\mathbb{P}(i\in A)<(3-\sqrt{5})/2, then H ⁡ ( A ∪ B) > H ⁡ ( A) H(A\cup B)>H(A).

Before we sketch the proof of Theorem 6.1, we explain how it implies the statement about union-closed families. Let ℱ \mathcal{F} be a finite collection of sets that is closed under union and let A A and B B be two independent uniformly random members of ℱ \mathcal{F}. If no element x ∈ ⋃ ℱ x\in\bigcup\mathcal{F} belonged to at least ( 3 − 5) / 2 (3-\sqrt{5})/2 -proportion of all sets in ℱ \mathcal{F}, then Theorem 6.1 would imply that H ⁡ ( A ∪ B) > H ⁡ ( A) = log ⁡ | ℱ | H(A\cup B)>H(A)=\log|\mathcal{F}|. However, since ℱ \mathcal{F} is union-closed, A ∪ B A\cup B is an element of ℱ \mathcal{F} and thus H ⁡ ( A ∪ B) ≤ log ⁡ | ℱ | H(A\cup B)\leq\log|\mathcal{F}| by 1.2, a contradiction.

###### Proof of Theorem 6.1 (sketch).

Let X, Y ∈ { 0, 1 } n X,Y\in\{0,1\}^{n} be the characteristic vectors of A A and B B, respectively. Write ∨ \vee for the coordinate-wise maximum operator. By the chain rule ( 1.4),

 | H ⁡ ( A ∪ B) − H ⁡ ( A) = H ⁡ ( X ∨ Y) − H ⁡ ( X) = ∑ i = 1 n ( H ⁡ ( X i ∨ Y i ∣ X < i ∨ Y < i) − H ⁡ ( X i ∣ X < i)). H(A\cup B)-H(A)=H(X\vee Y)-H(X)=\sum_{i=1}^{n}\bigl(H(X_{i}\vee Y_{i}\mid X_{<i}\vee Y_{<i})-H(X_{i}\mid X_{<i})\bigr). |  |

Fix some i ∈ ⟦ n ⟧ i\in\llbracket{n}\rrbracket. Since conditioning on more information only reduces entropy ( 1.5),

 | H ⁡ ( X i ∨ Y i ∣ X < i ∨ Y < i) − H ⁡ ( X i ∣ X < i) ≥ H ⁡ ( X i ∨ Y i ∣ X < i, Y < i) − H ⁡ ( X i ∣ X < i) ≕ Δ i. H(X_{i}\vee Y_{i}\mid X_{<i}\vee Y_{<i})-H(X_{i}\mid X_{<i})\geq H(X_{i}\vee Y_{i}\mid X_{<i},Y_{<i})-H(X_{i}\mid X_{<i})\eqqcolon\Delta_{i}. |  |

Writing p i ≔ 𝔼 ⁡ [X i ∣ X < i] p_{i}\coloneqq\Ex[X_{i}\mid X_{<i}] and q i ≔ 𝔼 ⁡ [Y i ∣ Y < i] q_{i}\coloneqq\Ex[Y_{i}\mid Y_{<i}] and recalling the definition of conditional entropy, one quickly realises that the assumption that X X and Y Y are independent means that

(16) |  | Δ i = 𝔼 ⁡ [h ⁡ ( p i + q i − p i ​ q i) − h ⁡ ( p i)], \Delta_{i}=\Ex[h(p_{i}+q_{i}-p_{i}q_{i})-h(p_{i})], |  |

where h h is the binary entropy function defined in Section 1.3. It clearly suffices to argue that Δ i ≥ 0 \Delta_{i}\geq 0 for every i i and that Δ i > 0 \Delta_{i}>0 unless p i = q i = 0 p_{i}=q_{i}=0 with probability one. It turns out that this follows from our main assumption that 𝔼 ⁡ [p i] = 𝔼 ⁡ [q i] = ℙ ⁡ ( i ∈ A) < ( 3 − 5) / 2 \Ex[p_{i}]=\Ex[q_{i}]=\mathbb{P}(i\in A)<(3-\sqrt{5})/2. If both p i p_{i} and q i q_{i} were constant (which is always true when i = 1 i=1), verifying that Δ i ≥ 0 \Delta_{i}\geq 0 (and that Δ i > 0 \Delta_{i}>0 unless p i = q i = 0 p_{i}=q_{i}=0) would be a fairly routine calculus exercise. In the case where p i p_{i} and q i q_{i} are random, this requires substantial technical work, see [4, 17, 86, 94]. We just remark that the significance of ( 3 − 5) / 2 (3-\sqrt{5})/2 is that it is the only nontrivial solution to the equation h ⁡ ( 2 ​ p − p 2) = h ⁡ ( p) h(2p-p^{2})=h(p) and that the heart of the matter seems to lie in proving that h ⁡ ( p 2) ≥ ( 5 + 1) / 2 ⋅ p ​ h ​ ( p) h(p^{2})\geq(\sqrt{5}+1)/2\cdot ph(p) for all p ∈ [0, 1] p\in[0,1], which had been proved by Boppana in the 1980s, see [9]. ∎

## 7. Entropy-based approach to the Turán problem.

The recent work of Chao and Yu [16] makes an interesting connection between entropy and the classical Turán problem for hypergraphs that has already been used to prove new bounds on Turán densities of several families of hypergraphs [47, 77, 78, 81]. Given a family ℱ \mathcal{F} of k k -uniform hypergraphs, we say that a hypergraph G G is *ℱ \mathcal{F} -free*if G G does not contain any member of ℱ \mathcal{F} as a subgraph. Define the *Turán number*ex ⁡ ( n, ℱ) \ex(n,\mathcal{F}) as the largest number of edges in an ℱ \mathcal{F} -free hypergraph with n n vertices and let

 | π ⁡ ( ℱ) ≔ lim n → ∞ ex ⁡ ( n, ℱ) ⋅ ( n k) − 1. \pi(\mathcal{F})\coloneqq\lim_{n\to\infty}\ex(n,\mathcal{F})\cdot\binom{n}{k}^{-1}. |  |

The *blowup density*of a k k -uniform hypergraph G G is the quantity

 | b ( G) ≔ k! ⋅ sup { ∑ A ∈ G ∏ v ∈ A x v: x ∈ [0, 1] V ⁡ ( G), ∑ v ∈ V ⁡ ( G) x v = 1 }, b(G)\coloneqq k!\cdot\sup\left\{\sum_{A\in G}\prod_{v\in A}x_{v}:x\in[0,1]^{V(G)},\,\sum_{v\in V(G)}x_{v}=1\right\}, |  |

which is naturally interpreted as the largest edge density of a blowup of G G. A hypergraph G G is called *ℱ \mathcal{F} -hom-free*if G G does not contain a homomorphic copy of any member of ℱ \mathcal{F}, that is, if Hom ⁡ ( F, G) = ∅ \Hom(F,G)=\varnothing for every F ∈ ℱ F\in\mathcal{F}. It is well-known that, for every family ℱ \mathcal{F},

(17) |  | π ⁡ ( ℱ) = sup { b ⁡ ( G): G is ℱ -hom-free } = sup { k! ⋅ e G ⋅ v G − k: G is ℱ -hom-free }. \pi(\mathcal{F})=\sup\{b(G):\text{$G$ is $\mathcal{F}$-hom-free}\}=\sup\left\{k!\cdot e_{G}\cdot v_{G}^{-k}:\text{$G$ is $\mathcal{F}$-hom-free}\right\}. |  |

Chao and Yu [16] provide the following alternative description of π ⁡ ( ℱ) \pi(\mathcal{F}).

###### 7.1 [16].

For any family ℱ \mathcal{F} of k k -uniform hypergraphs, log ⁡ π ⁡ ( ℱ) \log\pi(\mathcal{F}) is the supremum of H ⁡ ( X 1, …, X k) − k ​ H ​ ( X 1) H(X_{1},\dotsc,X_{k})-kH(X_{1}) over uniform orderings ( X 1, …, X k) (X_{1},\dotsc,X_{k}) of a random edge of some nonempty ℱ \mathcal{F} -hom-free k k -uniform hypergraph G G.

###### Proof.

Denote the supremum by S S. Given an arbitrary nonempty ℱ \mathcal{F} -hom-free hypergraph G G, we may let ( X 1, …, X k) (X_{1},\dotsc,X_{k}) be the uniformly chosen random ordered edge of G G to obtain

 | S ≥ H ⁡ ( X 1, …, X k) − k ​ H ​ ( X 1) = log ⁡ ( k! ⋅ e G) − k ​ H ​ ( X 1) ≥ log ⁡ ( k! ⋅ e G) − k ​ log ​ v G. S\geq H(X_{1},\dotsc,X_{k})-kH(X_{1})=\log(k!\cdot e_{G})-kH(X_{1})\geq\log(k!\cdot e_{G})-k\log v_{G}. |  |

Taking the supremum over all ℱ \mathcal{F} -hom-free G G yields S ≥ log ⁡ π ⁡ ( ℱ) S\geq\log\pi(\mathcal{F}). For the reverse inequality, suppose that ( X 1, …, X k) (X_{1},\dotsc,X_{k}) is the uniform ordering of a random edge of some ℱ \mathcal{F} -hom-free hypergraph G G and let T: V ​ ( G) k → { 0, 1 } T\colon V(G)^{k}\to\{0,1\} be the indicator of (ordered) edges of G G. Write X 1 ⊗ k X_{1}^{\otimes k} for the k k -dimensional vector X 1 ⊗ ⋯ ⊗ X 1 X_{1}\otimes\dotsb\otimes X_{1}. By 1.6, identity Eq. 3, and the data processing inequality ( 1.11),

 | k H ( X 1) − H ( X 1, …, X k) = H ( X 1 ⊗ k) − H ( X 1, …, X k) = D KL ( ( X 1, …, X k) ∥ X 1 ⊗ k) ≥ D KL ( T ( X 1, …, X k) ∥ T ( X 1 ⊗ k)) = d KL ( 1, ℙ ( T ( X 1 ⊗ k) = 1)) = − log ℙ ( T ( X 1 ⊗ k) = 1). kH(X_{1})-H(X_{1},\dotsc,X_{k})=H(X_{1}^{\otimes k})-H(X_{1},\dotsc,X_{k})=\DKulLei({(X_{1},\dotsc,X_{k})}\,\|\,{X_{1}^{\otimes k}})\\ \geq\DKulLei({T(X_{1},\dotsc,X_{k})}\,\|\,{T(X_{1}^{\otimes k})})=d_{\mathrm{KL}}(1,\mathbb{P}(T(X_{1}^{\otimes k})=1))=-\log\mathbb{P}(T(X_{1}^{\otimes k})=1). |  |

Finally, a moment’s thought reveals that the supremum of ℙ ⁡ ( T ⁡ ( X 1 ⊗ k) = 1) \mathbb{P}(T(X_{1}^{\otimes k})=1) over all random X 1 ∈ V ⁡ ( G) X_{1}\in V(G) is nothing else but b ⁡ ( G) b(G), which implies that S ≤ log ⁡ b ⁡ ( G) ≤ log ⁡ π ⁡ ( ℱ) S\leq\log b(G)\leq\log\pi(\mathcal{F}). ∎

To illustrate Proposition 7.1, Chao and Yu [16] provided an entropy-based proof of Turán’s theorem that is based on the ideas described in Section 4, which we present in the remainder of this section. A key role is played by the following lemma.

###### 7.2 [16].

Let X 1, …, X n X_{1},\dotsc,X_{n} be 𝒳 \mathcal{X} -valued random variables and let

 | s ≔ max x ∈ 𝒳 ⁡ | { i ∈ ⟦ n ⟧: ℙ ⁡ ( X i = x) > 0 } |. s\coloneqq\max_{x\in\mathcal{X}}|\{i\in\llbracket{n}\rrbracket:\mathbb{P}(X_{i}=x)>0\}|. |  |

There exists a random variable I ∈ ⟦ n ⟧ I\in\llbracket{n}\rrbracket that is independent of X 1, …, X n X_{1},\dotsc,X_{n} and satisfies

 | s ⋅ exp ⁡ ( H ⁡ ( X I)) ≥ ∑ i = 1 n exp ⁡ ( H ⁡ ( X i)). s\cdot\exp(H(X_{I}))\geq\sum_{i=1}^{n}\exp(H(X_{i})). |  |

###### Proof.

Denote by Σ \Sigma the sum appearing in the statement of the lemma and, for each i ∈ ⟦ n ⟧ i\in\llbracket{n}\rrbracket, let p i ≔ exp ⁡ ( H ⁡ ( X i)) / Σ p_{i}\coloneqq\exp(H(X_{i}))/\Sigma. Let I ∈ ⟦ n ⟧ I\in\llbracket{n}\rrbracket be the random index satisfying ℙ ⁡ ( I = i) = p i \mathbb{P}(I=i)=p_{i} for all i i. It follows from the chain rule ( 1.4) that

 | H ⁡ ( X I) + H ⁡ ( I ∣ X I) = H ⁡ ( X I, I) = H ⁡ ( I) + H ⁡ ( X I ∣ I) = ∑ i = 1 n p i ⋅ ( − log ⁡ p i + H ⁡ ( X i)) = log ⁡ Σ. H(X_{I})+H(I\mid X_{I})=H(X_{I},I)=H(I)+H(X_{I}\mid I)=\sum_{i=1}^{n}p_{i}\cdot\left(-\log p_{i}+H(X_{i})\right)=\log\Sigma. |  |

Further, since knowing X I X_{I} leaves at most s s options for I I, we have H ⁡ ( I ∣ X I) ≤ log ⁡ s H(I\mid X_{I})\leq\log s. Substituting this inequality into the above identity yields the assertion of the lemma. ∎

Fix an integer r ≥ 2 r\geq 2. The inequality π ⁡ ( K r + 1) ≥ 1 − 1 / r \pi(K_{r+1})\geq 1-1/r is easy to prove. For example, one may deduce it from Proposition 7.1 by considering a uniformly random ordered edge ( X 1, X 2) (X_{1},X_{2}) of K r K_{r}, which satisfies H ⁡ ( X 1, X 2) − 2 ​ H ​ ( X 1) = log ⁡ ( r ⁡ ( r − 1)) − 2 ​ log ⁡ r = log ⁡ ( 1 − 1 / r) H(X_{1},X_{2})-2H(X_{1})=\log(r(r-1))-2\log r=\log(1-1/r). For the reverse inequality, suppose that ( X 1, X 2) (X_{1},X_{2}) is a uniformly ordered random edge of some K r + 1 K_{r+1} -free graph G G. Our goal is to prove that

 | q ≔ exp ⁡ ( H ⁡ ( X 1, X 2) − 2 ​ H ​ ( X 1)) ≤ 1 − 1 / r. q\coloneqq\exp(H(X_{1},X_{2})-2H(X_{1}))\leq 1-1/r. |  |

The heart of the argument is the following statement.

###### 7.3.

For every positive integer N N, there exist random vectors T 1, …, T N ∈ V ​ ( G) N T_{1},\dotsc,T_{N}\in V(G)^{N} such that, for all i, j ∈ ⟦ N ⟧ i,j\in\llbracket{N}\rrbracket,

1. (i)

T i, i T_{i,i} is adjacent to each of T i, 1, …, T i, i − 1 T_{i,1},\dotsc,T_{i,i-1},

2. (ii)

H ⁡ ( T i) = ( N − i + 1) ⋅ H ⁡ ( X 1) + ( i − 1) ⋅ H ⁡ ( X 2 ∣ X 1) = N ⋅ H ⁡ ( X 1) + ( i − 1) ⋅ log ⁡ q H(T_{i})=(N-i+1)\cdot H(X_{1})+(i-1)\cdot H(X_{2}\mid X_{1})=N\cdot H(X_{1})+(i-1)\cdot\log q, and

3. (iii)

T i, j T_{i,j} has the same distribution as X 1 X_{1}.

###### Proof (sketch).

For each i ∈ ⟦ N ⟧ i\in\llbracket{N}\rrbracket, we construct T i T_{i} as follows (cf. the proof of Theorem 4.2). First, let T i, i, …, T i, N T_{i,i},\dotsc,T_{i,N} be independent random samples from the distribution of X 1 X_{1}. Second, given T i, i T_{i,i}, let T i, 1, …, T i, i − 1 T_{i,1},\dotsc,T_{i,i-1} be conditionally independent copies of X 2 X_{2} conditioned on X 1 = T i, i X_{1}=T_{i,i}. ∎

It follows from (i) that if, for some sequence t ∈ V ​ ( G) N t\in V(G)^{N}, we have ℙ ⁡ ( T i = t) > 0 \mathbb{P}(T_{i}=t)>0 for every i ∈ C ⊆ ⟦ N ⟧ i\in C\subseteq\llbracket{N}\rrbracket, then the vertices ( t i) i ∈ C (t_{i})_{i\in C} are pairwise adjacent. Since G G is K r + 1 K_{r+1} -free, no such t t can belong to the support of more than r r among the T 1, …, T N T_{1},\dotsc,T_{N}. Using Lemma 7.2 and (ii), we can define a random variable I ∈ ⟦ N ⟧ I\in\llbracket{N}\rrbracket satisfying

 | r ⋅ exp ⁡ ( H ⁡ ( T I)) ≥ ∑ i = 1 N exp ⁡ ( H ⁡ ( T i)) = ∑ i = 1 N q i − 1 ⋅ exp ⁡ ( N ⋅ H ⁡ ( X 1)). r\cdot\exp(H(T_{I}))\geq\sum_{i=1}^{N}\exp(H(T_{i}))=\sum_{i=1}^{N}q^{i-1}\cdot\exp(N\cdot H(X_{1})). |  |

On the other hand, since each of the N N coordinates of T I T_{I} has the same distribution as X 1 X_{1}, by (iii), we have H ⁡ ( T I) ≤ N ⋅ H ⁡ ( X 1) H(T_{I})\leq N\cdot H(X_{1}). Substituting this estimate into the above inequality and letting N N tend to infinity, we obtain the inequality r ≥ 1 / ( 1 − q) r\geq 1/(1-q), which is equivalent to the desired estimate q ≤ 1 − 1 / r q\leq 1-1/r.

## Acknowledgements.

I would like to thank Asaf Cohen Antonir, Shira Ben Dor, Marcelo Campos, David Conlon, Sahar Diskin, Ehud Friedgut, Matan Harel, Ilay Hoshen, Vishesh Jain, Matthew Jenssen, Gady Kozma, Eden Kuperwasser, Tom Meyerovitch, Frank Mousset, Rajko Nenadov, Jinyoung Park, Ron Peled, Yinon Spinka, and Adam (Zsolt) Wagner for many interesting and enriching conversations on the topic of entropy. These discussions have greatly influenced the content of this paper. Having said that, all errors and omissions are entirely my own. Finally, special thanks to David Conlon, Eden Kuperwasser, Joonkyung Lee, and Hung-Hsun Yu for their comments on an earlier version of this paper.

## References

- [1] M. Aigner and G. M. Ziegler (2018) Proofs from The Book. Sixth edition, Springer, Berlin. Note: See corrected reprint of the 1998 original [ MR1723092], Including illustrations by Karl H. Hofmann External Links: ISBN 978-3-662-57264-1; 978-3-662-57265-8, [Document][4], [MathReview Entry][5] Cited by: §2.
- [2] N. Alon and J. H. Spencer (2016) The probabilistic method. Fourth edition, Wiley Series in Discrete Mathematics and Optimization, John Wiley & Sons, Inc., Hoboken, NJ. External Links: ISBN 978-1-119-06195-3, [MathReview Entry][6] Cited by: §2.
- [3] N. Alon (1981) On the number of subgraphs of prescribed type of graphs with a given number of edges. Israel J. Math. 38 ( 1-2), pp. 116–130. External Links: ISSN 0021-2172, [Document][7], [MathReview (David E. Daykin)][8] Cited by: §3.
- [4] R. Alweiss, B. Huang, and M. Sellke (2024) Improved lower bound for Frankl’s union-closed sets conjecture. Electron. J. Combin. 31 ( 3), pp. Paper No. 3.35, 11. External Links: [Document][9], [Link][10], [MathReview Entry][11] Cited by: §6, §6.
- [5] J. Balogh, B. Bollobás, and B. Narayanan (2021) Counting independent sets in regular hypergraphs. J. Combin. Theory Ser. A 180, pp. Paper No. 105405, 5. External Links: ISSN 0097-3165, [Document][12], [MathReview (Mark Rowland Budden)][13] Cited by: §3.
- [6] N. Behague, G. Crudele, J. A. Noel, and L. M. Simbaqueba (2025) Sidorenko-type inequalities for pairs of trees. Random Structures Algorithms 67 ( 1), pp. Paper No. e70026, 51. External Links: ISSN 1042-9832, [Document][14], [Link][15], [MathReview Entry][16] Cited by: §4.
- [7] N. Behague, N. Morrison, and J. A. Noel (2024) Off-diagonal commonality of graphs via entropy. SIAM J. Discrete Math. 38 ( 3), pp. 2335–2360. External Links: ISSN 0895-4801, [Document][17], [Link][18], [MathReview (Kiyoshi Yoshimoto)][19] Cited by: §4.
- [8] G. Blekherman and A. Raymond (2023) A new proof of the Erdős-Simonovits conjecture on walks. Graphs Combin. 39 ( 3), pp. Paper No. 53, 8. External Links: ISSN 0911-0119, [Document][20], [Link][21], [MathReview (Serge A. Lawrence)][22] Cited by: §4.
- [9] R. B. Boppana A Useful Inequality for the Binary Entropy Function. Note: arXiv:2301.09664 Cited by: §6.
- [10] S. Boucheron, G. Lugosi, and P. Massart (2013) Concentration inequalities. Oxford University Press, Oxford. Note: A nonasymptotic theory of independence, With a foreword by Michel Ledoux External Links: ISBN 978-0-19-953525-5, [Document][23], [MathReview (Sreenivasan Ravi)][24] Cited by: §3.
- [11] S. Boyadzhiyska, S. Das, and T. Szabó (2020) Enumerating extensions of mutually orthogonal Latin squares. Des. Codes Cryptogr. 88 ( 10), pp. 2187–2206. External Links: ISSN 0925-1022, [Document][25], [MathReview (R. M. Falcón)][26] Cited by: §2.
- [12] L. M. Brègman (1973) Certain properties of nonnegative matrices and their permanents. Dokl. Akad. Nauk SSSR 211, pp. 27–30. External Links: ISSN 0002-3264, [MathReview (E. Seneta)][27] Cited by: §2.
- [13] S. Cambie Better bounds for the union-closed sets conjecture using the entropy approach. Note: arXiv:2212.12500 Cited by: §6.
- [14] T. Chao and H. H. Yu A Purely Entropic Approach to the Rainbow Triangle Problem. Note: arXiv:2407.14084 Cited by: §3.
- [15] T. Chao and H. H. Yu (2024) Kruskal-Katona-type problems via the entropy method. J. Combin. Theory Ser. B 169, pp. 480–506. External Links: ISSN 0095-8956, [Document][28], [MathReview (Grace McCourt)][29] Cited by: §3.
- [16] T. Chao and H. H. Yu (2026) When entropy meets Turán: new proofs and hypergraph Turán results. J. Lond. Math. Soc. (2) 113 ( 3), pp. Paper No. e70473, 40. External Links: ISSN 0024-6107,1469-7750, [Document][30], [Link][31], [MathReview Entry][32] Cited by: 7.1, 7.2, §7, §7, §7.
- [17] Z. Chase and S. Lovett Approximate union closed conjecture. Note: arXiv:2211.11689 Cited by: §6, §6.
- [18] M. Christoph, N. Draganić, A. Girão, E. Hurley, L. Michel, and A. Müyesser Cycle-factors of regular graphs via entropy. Note: arXiv:2507.19417 Cited by: §2.
- [19] F. R. K. Chung, R. L. Graham, P. Frankl, and J. B. Shearer (1986) Some intersection theorems for ordered sets and graphs. J. Combin. Theory Ser. A 43 ( 1), pp. 23–37. External Links: ISSN 0097-3165, [Document][33], [MathReview (Zoltán Füredi)][34] Cited by: §1, §3.
- [20] A. Cohen Antonir, M. Harel, F. Mousset, and W. Samotij Upper tails for irregular graphs beyond the mean-field regime. Note: arXiv:2606.14564 Cited by: §3.
- [21] A. Coja-Oghlan and M. Hahn-Klimroth (2021) The cut metric for probability distributions. SIAM J. Discrete Math. 35 ( 2), pp. 1096–1135. External Links: ISSN 0895-4801,1095-7146, [Document][35], [Link][36], [MathReview (Tatyana S. Turova)][37] Cited by: §5.
- [22] A. Coja-Oghlan, F. Krzakala, W. Perkins, and L. Zdeborová (2018) Information-theoretic thresholds from the cavity method. Adv. Math. 333, pp. 694–795. External Links: ISSN 0001-8708,1090-2082, [Document][38], [Link][39], [MathReview (Wenyi Zhang)][40] Cited by: §5.
- [23] D. Conlon, J. Fox, and B. Sudakov (2010) An approximate version of Sidorenko’s conjecture. Geom. Funct. Anal. 20 ( 6), pp. 1354–1366. External Links: ISSN 1016-443X, [Document][41], [Link][42], [MathReview (József Balogh)][43] Cited by: §4.
- [24] D. Conlon, J. H. Kim, C. Lee, and J. Lee (2018) Some advances on Sidorenko’s conjecture. J. Lond. Math. Soc. (2) 98 ( 3), pp. 593–608. External Links: ISSN 0024-6107, [Document][44], [Link][45], [MathReview (József Balogh)][46] Cited by: §4.
- [25] D. Conlon and J. Lee (2017) Finite reflection groups and graph norms. Adv. Math. 315, pp. 130–165. External Links: ISSN 0001-8708, [Document][47], [Link][48], [MathReview (Juanjo Rué)][49] Cited by: §4.
- [26] I. Csiszár (1966) A note on Jensen’s inequality. Studia Sci. Math. Hungar. 1, pp. 185–188. External Links: ISSN 0081-6906, [MathReview (H. Kesten)][50] Cited by: §5.
- [27] I. Csiszár and J. Körner (2011) Information theory. Second edition, Cambridge University Press, Cambridge. Note: Coding theorems for discrete memoryless systems External Links: ISBN 978-0-521-19681-9, [Document][51], [MathReview Entry][52] Cited by: §1.
- [28] B. Cuckler and J. Kahn (2009) Entropy bounds for perfect matchings and Hamiltonian cycles. Combinatorica 29 ( 3), pp. 327–335. External Links: ISSN 0209-9683, [Document][53], [MathReview (Shaohui Zhai)][54] Cited by: §2.
- [29] B. Cuckler and J. Kahn (2009) Hamiltonian cycles in Dirac graphs. Combinatorica 29 ( 3), pp. 299–326. External Links: ISSN 0209-9683, [Document][55], [MathReview (Shaohui Zhai)][56] Cited by: §2.
- [30] J. Cutler and A. J. Radcliffe (2011) An entropy proof of the Kahn-Lovász theorem. Electron. J. Combin. 18 ( 1), pp. Paper 10, 9. External Links: [Document][57], [MathReview (Shaohui Zhai)][58] Cited by: §2.
- [31] T. Dai, A. Divoux, and T. Kelly (2026) Entropy bounds for perfect matchings in bipartite hypergraphs. Electron. J. Combin. 33 ( 2), pp. Paper No. 2.20, 13. External Links: ISSN 1077-8926, [Document][59], [Link][60], [MathReview Entry][61] Cited by: §2.
- [32] S. Diskin and W. Samotij (2025) Isoperimetry in Product Graphs. Electron. J. Combin. 32 ( 3), pp. P3.12. External Links: [Document][62], [MathReview Entry][63] Cited by: §3.
- [33] D. Ellis, E. Friedgut, G. Kindler, and A. Yehudayoff (2016) Geometric stability via information theory. Discrete Anal., pp. Paper No. 10, 29. External Links: [Document][64], [Link][65], [MathReview (Mohammad Soufi)][66] Cited by: §5.
- [34] J. Engbers and D. Galvin (2012) H H -coloring tori. J. Combin. Theory Ser. B 102 ( 5), pp. 1110–1133. External Links: ISSN 0095-8956, [Document][67], [MathReview (Anne C. Sinko)][68] Cited by: §3.
- [35] J. Engbers and D. Galvin (2012) H H -colouring bipartite graphs. J. Combin. Theory Ser. B 102 ( 3), pp. 726–742. External Links: ISSN 0095-8956, [Document][69], [MathReview (Anne C. Sinko)][70] Cited by: §3.
- [36] P. Erdős and M. Simonovits (1984) Cube-supersaturated graphs and related problems. In Progress in graph theory (Waterloo, Ont., 1982), pp. 203–218. External Links: [MathReview (Ralph Faudree)][71] Cited by: §4.
- [37] J. Fox and B. Sudakov (2011) Dependent random choice. Random Structures Algorithms 38 ( 1-2), pp. 68–99. External Links: ISSN 1042-9832, [Document][72], [Link][73], [MathReview (Hamed Hatami)][74] Cited by: §4.
- [38] E. Friedgut and J. Kahn (1998) On the number of copies of one hypergraph in another. Israel J. Math. 105, pp. 251–256. External Links: ISSN 0021-2172, [Document][75], [MathReview (Nigel Martin)][76] Cited by: §3, §3.
- [39] E. Friedgut (2004) Hypergraphs, entropy, and inequalities. Amer. Math. Monthly 111 ( 9), pp. 749–760. External Links: ISSN 0002-9890, [Document][77], [Link][78], [MathReview Entry][79] Cited by: §3.
- [40] D. Galvin and P. Tetali (2004) On weighted graph homomorphisms. In Graphs, morphisms and statistical physics, DIMACS Ser. Discrete Math. Theoret. Comput. Sci., Vol. 63, pp. 97–104. External Links: [Document][80], [MathReview (Valery A. Liskovets)][81] Cited by: 3.4, §3.
- [41] D. Galvin Three tutorial lectures on entropy and counting. Note: arXiv:1406.7872 Cited by: §1.1.
- [42] D. Galvin (2003) On homomorphisms from the Hamming cube to 𝐙 {\bf Z}. Israel J. Math. 138, pp. 189–213. External Links: ISSN 0021-2172, [Document][82], [MathReview (Heinrich Niederhausen)][83] Cited by: §3.
- [43] J. Gilmer A constant lower bound for the union-closed sets conjecture. Note: arXiv:2211.09055 Cited by: §6.
- [44] A. Grzesik, J. Lee, B. Lidický, and J. Volec (2022) On tripartite common graphs. Combin. Probab. Comput. 31 ( 5), pp. 907–923. External Links: ISSN 0963-5483, [Document][84], [Link][85], [MathReview (Kiyoshi Yoshimoto)][86] Cited by: §4.
- [45] T. S. Han (1978) Nonnegative entropy measures of multivariate symmetric correlations. Information and Control 36 ( 2), pp. 133–156. External Links: ISSN 0019-9958, [MathReview (Gordon Cook)][87] Cited by: §3.
- [46] M. Harel, F. Mousset, and W. Samotij (2022) Upper tails via high moments and entropic stability. Duke Math. J. 171 ( 10), pp. 2089–2192. External Links: ISSN 0012-7094, [Document][88], [MathReview Entry][89] Cited by: §3.
- [47] D. Iľkovič and J. Yan An improved hypergraph Mantel’s Theorem. Note: arXiv:2503.14474 Cited by: §7.
- [48] V. Jain, F. Koehler, and A. Risteski (2019) Mean-field approximation, convex hierarchies, and the optimality of correlation rounding: a unified perspective. In STOC’19—Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing, pp. 1226–1236. Cited by: §5.
- [49] S. Janson, K. Oleszkiewicz, and A. Ruciński (2004) Upper tails for subgraph counts in random graphs. Israel J. Math. 142, pp. 61–92. External Links: ISSN 0021-2172, [Document][90], [MathReview (David B. Penman)][91] Cited by: §3.
- [50] M. Jenssen and P. Keevash (2023) Homomorphisms from the torus. Adv. Math. 430, pp. Paper No. 109212, 89. External Links: ISSN 0001-8708, [Document][92], [MathReview (Ioan Tomescu)][93] Cited by: §3.
- [51] J. Kahn (2001) Range of cube-indexed random walk. Israel J. Math. 124, pp. 189–201. External Links: ISSN 0021-2172, [Document][94], [MathReview (Heinrich Niederhausen)][95] Cited by: §3.
- [52] J. Kahn and A. Lawrenz (1999) Generalized rank functions and an entropy argument. J. Combin. Theory Ser. A 87 ( 2), pp. 398–403. External Links: ISSN 0097-3165, [Document][96], [MathReview (A. N. Philippou)][97] Cited by: §3.
- [53] J. Kahn and J. Park (2020) The number of 4-colorings of the Hamming cube. Israel J. Math. 236 ( 2), pp. 629–649. External Links: ISSN 0021-2172, [Document][98], [MathReview (Vernold Vivin. J)][99] Cited by: §3.
- [54] J. Kahn (2001) An entropy approach to the hard-core model on bipartite graphs. Combin. Probab. Comput. 10 ( 3), pp. 219–237. External Links: ISSN 0963-5483, [Document][100], [MathReview Entry][101] Cited by: 3.4, §3, §3.
- [55] J. Kahn (2002) Entropy, independent sets and antichains: a new approach to Dedekind’s problem. Proc. Amer. Math. Soc. 130 ( 2), pp. 371–378. External Links: ISSN 0002-9939, [Document][102], [Link][103], [MathReview (Valery A. Liskovets)][104] Cited by: §3.
- [56] J. Kahn (2023) Asymptotics for Shamir’s problem. Adv. Math. 422, pp. Paper No. 109019, 39. External Links: ISSN 0001-8708, [Document][105], [MathReview (Tatyana S. Turova)][106] Cited by: §2.
- [57] N. Kamčev, A. Liebenau, and N. Morrison (2023) Towards a characterization of Sidorenko systems. Q. J. Math. 74 ( 3), pp. 957–974. External Links: ISSN 0033-5606, [Document][107], [Link][108], [MathReview (Jonathan Chapman)][109] Cited by: §4.
- [58] P. Keevash The existence of designs. Note: arXiv:1401.3665 Cited by: §2.
- [59] P. Keevash (2008) Shadows and intersections: stability and new proofs. Adv. Math. 218 ( 5), pp. 1685–1703. External Links: ISSN 0001-8708, [Document][110], [Link][111], [MathReview (David J. Grynkiewicz)][112] Cited by: §5.
- [60] P. Keevash (2018) Counting designs. J. Eur. Math. Soc. (JEMS) 20 ( 4), pp. 903–927. External Links: ISSN 1435-9855, [Document][113], [MathReview (Luc Teirlinck)][114] Cited by: §2.
- [61] J. H. B. Kemperman (1969) On the optimum rate of transmitting information. Ann. Math. Statist. 40, pp. 2156–2177. External Links: ISSN 0003-4851, [Document][115], [Link][116], [MathReview (N. Zierler)][117] Cited by: §5.
- [62] J. H. Kim, C. Lee, and J. Lee (2016) Two approaches to Sidorenko’s conjecture. Trans. Amer. Math. Soc. 368 ( 7), pp. 5057–5074. External Links: ISSN 0002-9947, [Document][118], [Link][119], [MathReview (Dmitry A. Shabanov)][120] Cited by: §4.
- [63] S. Kopparty and B. Rossman (2011) The homomorphism domination exponent. European J. Combin. 32 ( 7), pp. 1097–1114. External Links: ISSN 0195-6698, [Document][121], [Link][122], [MathReview Entry][123] Cited by: §4, §4.
- [64] G. Kozma, T. Meyerovitch, R. Peled, and W. Samotij (2024) What does a typical metric space look like?. Ann. Inst. Henri Poincaré Probab. Stat. 60 ( 1), pp. 11–53. External Links: ISSN 0246-0203, [Document][124], [Link][125], [MathReview (Michel Bonnefont)][126] Cited by: §5.
- [65] G. Kozma and W. Samotij (2023) Lower tails via relative entropy. Ann. Probab. 51 ( 2), pp. 665–698. External Links: ISSN 0091-1798, [Document][127], [Link][128], [MathReview (Christoph Thäle)][129] Cited by: §5, §5.
- [66] D. Král̆, J. Volec, and F. Wei (2025) Common graphs with arbitrary chromatic number. Compos. Math. 161 ( 3), pp. 594–634. External Links: ISSN 0010-437X, [Document][130], [Link][131], [MathReview Entry][132] Cited by: §4.
- [67] R. A. Krueger, L. Li, and J. Park Lipschitz functions on weak expanders. Note: arXiv:2408.14702 Cited by: §3.
- [68] S. Kullback and R. A. Leibler (1951) On information and sufficiency. Ann. Math. Statistics 22, pp. 79–86. External Links: ISSN 0003-4851, [Document][133], [MathReview (L. J. Savage)][134] Cited by: §1.4.
- [69] S. Kullback (1967) A lower bound for discrimination information in terms of variation. IEEE Transactions on Information Theory 13, pp. 126–127. Cited by: §5.
- [70] M. Kwan, R. Safavi, and Y. Wang (2026) Counting perfect matchings in Dirac hypergraphs. Combinatorica 46 ( 1), pp. Paper No. 5, 32. External Links: ISSN 0209-9683,1439-6912, [Document][135], [Link][136], [MathReview (Ioan Tomescu)][137] Cited by: §2.
- [71] M. Kwan (2020) Almost all Steiner triple systems have perfect matchings. Proc. Lond. Math. Soc. (3) 121 ( 6), pp. 1468–1495. External Links: ISSN 0024-6115, [Document][138], [MathReview (Peter Horák)][139] Cited by: §2.
- [72] J. Lee (2021) On some graph densities in locally dense graphs. Random Structures Algorithms 58 ( 2), pp. 322–344. External Links: ISSN 1042-9832, [Document][140], [Link][141], [MathReview Entry][142] Cited by: §4.
- [73] J. L. X. Li and B. Szegedy On the logarithmic calculus and Sidorenko’s conjecture. Note: arXiv:1107.1153 Cited by: §4.
- [74] L. Li, G. McKinley, and J. Park (2025) The number of colorings of the middle layers of the Hamming cube. Combinatorica 45 ( 1), pp. Paper No. 7, 47. External Links: ISSN 0209-9683, [Document][143], [Link][144], [MathReview (Martin Klazar)][145] Cited by: §3.
- [75] N. Linial and Z. Luria (2013) An upper bound on the number of Steiner triple systems. Random Structures Algorithms 43 ( 4), pp. 399–406. External Links: ISSN 1042-9832, [Document][146], [MathReview (Yeh-Jong Pan)][147] Cited by: 2.3, §2, §2, §2, §2.
- [76] N. Linial and Z. Luria (2014) An upper bound on the number of high-dimensional permutations. Combinatorica 34 ( 4), pp. 471–486. External Links: ISSN 0209-9683, [Document][148], [MathReview (Arnold Knopfmacher)][149] Cited by: §2.
- [77] X. Liu On a hypergraph Mantel theorem. Note: arXiv:2501.19229 Cited by: §7.
- [78] X. Liu Spectral generalized Turán problems. Note: arXiv:2507.21689 Cited by: §7.
- [79] L. H. Loomis and H. Whitney (1949) An inequality related to the isoperimetric inequality. Bull. Amer. Math. Soc. 55, pp. 961–962. External Links: ISSN 0002-9904, [Document][150], [MathReview (L. C. Young)][151] Cited by: §3, §5.
- [80] Z. Luria New bounds on the number of n-queens configurations. Note: arXiv:1705.05225 Cited by: 2.3, §2, §2.
- [81] J. Ma and T. Zhu A note on hypergraph extensions of Mantel’s theorem. Note: arXiv:2505.11373 Cited by: §7.
- [82] P. Manurangsi and P. Raghavendra (2017) A birthday repetition theorem and complexity of approximating dense CSPs. In 44th International Colloquium on Automata, Languages, and Programming, LIPIcs. Leibniz Int. Proc. Inform., Vol. 80, pp. 78:1–78:15. Cited by: §5.
- [83] H. Minc (1963) Upper bounds for permanents of ( 0, 1) (0,\,1) -matrices. Bull. Amer. Math. Soc. 69, pp. 789–791. External Links: ISSN 0002-9904, [Document][152], [MathReview (H. J. Ryser)][153] Cited by: §2.
- [84] A. Montanari (2008) Estimating random variables from random sparse observations. European Transactions on Telecommunications 19 ( 4), pp. 385–403. Cited by: §5.
- [85] C. Palmer and D. Pálvölgyi (2022) At most 3.55 n 3.55^{n} stable matchings. In 2021 IEEE 62nd Annual Symposium on Foundations of Computer Science—FOCS 2021, pp. 217–227. External Links: [Document][154], [MathReview Entry][155] Cited by: §2.
- [86] L. Pebody Extension of a Method of Gilmer. Note: arXiv:2211.13139 Cited by: §6, §6.
- [87] R. Peled and Y. Spinka Long-range order in discrete spin systems. Note: arXiv:2010.03177 Cited by: §3.
- [88] R. Peled and Y. Spinka (2023) Rigidity of proper colorings of ℤ d \mathbb{Z}^{d}. Invent. Math. 232 ( 1), pp. 79–162. External Links: ISSN 0020-9910, [Document][156], [MathReview Entry][157] Cited by: §3.
- [89] M. S. Pinsker (1964) Information and information stability of random variables and processes. Holden-Day, Inc., San Francisco, Calif.-London-Amsterdam. Note: Translated and edited by Amiel Feinstein External Links: [MathReview Entry][158] Cited by: §5.
- [90] J. Radhakrishnan (1997) An entropy proof of Bregman’s theorem. J. Combin. Theory Ser. A 77 ( 1), pp. 161–164. External Links: ISSN 0097-3165, [Document][159], [MathReview Entry][160] Cited by: §2.
- [91] P. Raghavendra and N. Tan (2012) Approximating CSPs with global cardinality constraints using SDP hierarchies. In Proceedings of the Twenty-Third Annual ACM-SIAM Symposium on Discrete Algorithms, pp. 373–387. Cited by: §5.
- [92] A. Rényi (1965) On the foundations of information theory. Rev. Inst. Internat. Statist. 33, pp. 1–14. External Links: ISSN 0373-1138, [Document][161], [MathReview (J. Wolfowitz)][162] Cited by: §1.1.
- [93] M. Sağlam (2018) Near log-convexity of measured heat in (discrete) time and consequences. In 59th Annual IEEE Symposium on Foundations of Computer Science—FOCS 2018, pp. 967–978. External Links: [Document][163], [Link][164], [MathReview Entry][165] Cited by: §4.
- [94] W. Sawin An improved lower bound for the union-closed set conjecture. Note: arXiv:2211.11504 Cited by: §6, §6.
- [95] A. Schrijver (1978) A short proof of Minc’s conjecture. J. Combinatorial Theory Ser. A 25 ( 1), pp. 80–83. External Links: ISSN 0097-3165, [Document][166], [MathReview (J. H. van Lint)][167] Cited by: §2.
- [96] C. E. Shannon (1948) A mathematical theory of communication. Bell System Tech. J. 27, pp. 379–423, 623–656. External Links: ISSN 0005-8580, [Document][168], [MathReview (J. L. Doob)][169] Cited by: §1.4, §1.
- [97] A. F. Sidorenko (1991) Inequalities for functionals generated by bipartite graphs. Diskret. Mat. 3 ( 3), pp. 50–65. External Links: ISSN 0234-0860, [Document][170], [Link][171], [MathReview (B. Zelinka)][172] Cited by: §4.
- [98] A. Sidorenko (1993) A correlation inequality for bipartite graphs. Graphs Combin. 9 ( 2), pp. 201–204. External Links: ISSN 0911-0119, [Document][173], [Link][174], [MathReview Entry][175] Cited by: §4.
- [99] M. Simkin (2023) The number of n n -queens configurations. Adv. Math. 427, pp. Paper No. 109127, 83. External Links: ISSN 0001-8708, [Document][176], [MathReview (Eugenijus Manstavičius)][177] Cited by: §2.
- [100] B. Szegedy An information theoretic approach to Sidorenko’s conjecture. Note: arXiv:1406.6738 Cited by: §4.
- [101] R. van der Hofstad, R. Pendavingh, and J. van der Pol (2022) The number of partial Steiner systems and d d -partitions. Adv. Comb., pp. Paper No. 2, 23. External Links: [Document][178], [MathReview (Martin Kochol)][179] Cited by: §2.
- [102] L. Yu (2023) Dimension-free bounds for the union-closed sets conjecture. Entropy 25 ( 5), pp. Paper No. 767, 10. External Links: [Document][180], [Link][181], [MathReview Entry][182] Cited by: §6.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:samotij@tauex.tau.ac.il
[4]: https://dx.doi.org/10.1007/978-3-662-57265-8
[5]: https://www.ams.org/mathscinet-getitem?mr=3823190
[6]: https://www.ams.org/mathscinet-getitem?mr=3524748
[7]: https://dx.doi.org/10.1007/BF02761855
[8]: https://www.ams.org/mathscinet-getitem?mr=599482
[9]: https://dx.doi.org/10.37236/12232
[10]: https://doi.org/10.37236/12232
[11]: https://www.ams.org/mathscinet-getitem?mr=4798522
[12]: https://dx.doi.org/10.1016/j.jcta.2021.105405
[13]: https://www.ams.org/mathscinet-getitem?mr=4200745
[14]: https://dx.doi.org/10.1002/rsa.70026
[15]: https://doi.org/10.1002/rsa.70026
[16]: https://www.ams.org/mathscinet-getitem?mr=4946485
[17]: https://dx.doi.org/10.1137/23M1625342
[18]: https://doi.org/10.1137/23M1625342
[19]: https://www.ams.org/mathscinet-getitem?mr=4790926
[20]: https://dx.doi.org/10.1007/s00373-023-02646-8
[21]: https://doi.org/10.1007/s00373-023-02646-8
[22]: https://www.ams.org/mathscinet-getitem?mr=4578445
[23]: https://dx.doi.org/10.1093/acprof%3Aoso/9780199535255.001.0001
[24]: https://www.ams.org/mathscinet-getitem?mr=3185193
[25]: https://dx.doi.org/10.1007/s10623-020-00771-6
[26]: https://www.ams.org/mathscinet-getitem?mr=4156232
[27]: https://www.ams.org/mathscinet-getitem?mr=327788
[28]: https://dx.doi.org/10.1016/j.jctb.2024.08.003
[29]: https://www.ams.org/mathscinet-getitem?mr=4789260
[30]: https://dx.doi.org/10.1112/jlms.70473
[31]: https://doi.org/10.1112/jlms.70473
[32]: https://www.ams.org/mathscinet-getitem?mr=5041301
[33]: https://dx.doi.org/10.1016/0097-3165%2886%2990019-1
[34]: https://www.ams.org/mathscinet-getitem?mr=859293
[35]: https://dx.doi.org/10.1137/19M126548X
[36]: https://doi.org/10.1137/19M126548X
[37]: https://www.ams.org/mathscinet-getitem?mr=4266221
[38]: https://dx.doi.org/10.1016/j.aim.2018.05.029
[39]: https://doi.org/10.1016/j.aim.2018.05.029
[40]: https://www.ams.org/mathscinet-getitem?mr=3818090
[41]: https://dx.doi.org/10.1007/s00039-010-0097-0
[42]: https://doi.org/10.1007/s00039-010-0097-0
[43]: https://www.ams.org/mathscinet-getitem?mr=2738996
[44]: https://dx.doi.org/10.1112/jlms.12142
[45]: https://doi.org/10.1112/jlms.12142
[46]: https://www.ams.org/mathscinet-getitem?mr=3893193
[47]: https://dx.doi.org/10.1016/j.aim.2017.05.009
[48]: https://doi.org/10.1016/j.aim.2017.05.009
[49]: https://www.ams.org/mathscinet-getitem?mr=3667583
[50]: https://www.ams.org/mathscinet-getitem?mr=214714
[51]: https://dx.doi.org/10.1017/CBO9780511921889
[52]: https://www.ams.org/mathscinet-getitem?mr=2839250
[53]: https://dx.doi.org/10.1007/s00493-009-2366-9
[54]: https://www.ams.org/mathscinet-getitem?mr=2520275
[55]: https://dx.doi.org/10.1007/s00493-009-2360-2
[56]: https://www.ams.org/mathscinet-getitem?mr=2520274
[57]: https://dx.doi.org/10.37236/497
[58]: https://www.ams.org/mathscinet-getitem?mr=2770115
[59]: https://dx.doi.org/10.37236/14339
[60]: https://doi.org/10.37236/14339
[61]: https://www.ams.org/mathscinet-getitem?mr=5063621
[62]: https://dx.doi.org/10.37236/13585
[63]: https://www.ams.org/mathscinet-getitem?mr=4960378
[64]: https://dx.doi.org/10.19086/da.784
[65]: https://doi.org/10.19086/da.784
[66]: https://www.ams.org/mathscinet-getitem?mr=3555193
[67]: https://dx.doi.org/10.1016/j.jctb.2012.05.003
[68]: https://www.ams.org/mathscinet-getitem?mr=2959393
[69]: https://dx.doi.org/10.1016/j.jctb.2011.12.004
[70]: https://www.ams.org/mathscinet-getitem?mr=2900814
[71]: https://www.ams.org/mathscinet-getitem?mr=776802
[72]: https://dx.doi.org/10.1002/rsa.20344
[73]: https://doi.org/10.1002/rsa.20344
[74]: https://www.ams.org/mathscinet-getitem?mr=2768884
[75]: https://dx.doi.org/10.1007/BF02780332
[76]: https://www.ams.org/mathscinet-getitem?mr=1639767
[77]: https://dx.doi.org/10.2307/4145187
[78]: https://doi.org/10.2307/4145187
[79]: https://www.ams.org/mathscinet-getitem?mr=2104047
[80]: https://dx.doi.org/10.1090/dimacs/063/07
[81]: https://www.ams.org/mathscinet-getitem?mr=2056231
[82]: https://dx.doi.org/10.1007/BF02783426
[83]: https://www.ams.org/mathscinet-getitem?mr=2031957
[84]: https://dx.doi.org/10.1017/s0963548322000074
[85]: https://doi.org/10.1017/s0963548322000074
[86]: https://www.ams.org/mathscinet-getitem?mr=4472294
[87]: https://www.ams.org/mathscinet-getitem?mr=464499
[88]: https://dx.doi.org/10.1215/00127094-2021-0067
[89]: https://www.ams.org/mathscinet-getitem?mr=4484206
[90]: https://dx.doi.org/10.1007/BF02771528
[91]: https://www.ams.org/mathscinet-getitem?mr=2085711
[92]: https://dx.doi.org/10.1016/j.aim.2023.109212
[93]: https://www.ams.org/mathscinet-getitem?mr=4619447
[94]: https://dx.doi.org/10.1007/BF02772616
[95]: https://www.ams.org/mathscinet-getitem?mr=1856513
[96]: https://dx.doi.org/10.1006/jcta.1999.2965
[97]: https://www.ams.org/mathscinet-getitem?mr=1704270
[98]: https://dx.doi.org/10.1007/s11856-020-1984-1
[99]: https://www.ams.org/mathscinet-getitem?mr=4093899
[100]: https://dx.doi.org/10.1017/S0963548301004631
[101]: https://www.ams.org/mathscinet-getitem?mr=1841642
[102]: https://dx.doi.org/10.1090/S0002-9939-01-06058-0
[103]: https://doi.org/10.1090/S0002-9939-01-06058-0
[104]: https://www.ams.org/mathscinet-getitem?mr=1862115
[105]: https://dx.doi.org/10.1016/j.aim.2023.109019
[106]: https://www.ams.org/mathscinet-getitem?mr=4575035
[107]: https://dx.doi.org/10.1093/qmath/haad013
[108]: https://doi.org/10.1093/qmath/haad013
[109]: https://www.ams.org/mathscinet-getitem?mr=4642245
[110]: https://dx.doi.org/10.1016/j.aim.2008.03.023
[111]: https://doi.org/10.1016/j.aim.2008.03.023
[112]: https://www.ams.org/mathscinet-getitem?mr=2419936
[113]: https://dx.doi.org/10.4171/JEMS/779
[114]: https://www.ams.org/mathscinet-getitem?mr=3779688
[115]: https://dx.doi.org/10.1214/aoms/1177697293
[116]: https://doi.org/10.1214/aoms/1177697293
[117]: https://www.ams.org/mathscinet-getitem?mr=252112
[118]: https://dx.doi.org/10.1090/tran/6487
[119]: https://doi.org/10.1090/tran/6487
[120]: https://www.ams.org/mathscinet-getitem?mr=3456171
[121]: https://dx.doi.org/10.1016/j.ejc.2011.03.009
[122]: https://doi.org/10.1016/j.ejc.2011.03.009
[123]: https://www.ams.org/mathscinet-getitem?mr=2825537
[124]: https://dx.doi.org/10.1214/22-aihp1262
[125]: https://doi.org/10.1214/22-aihp1262
[126]: https://www.ams.org/mathscinet-getitem?mr=4718373
[127]: https://dx.doi.org/10.1214/22-aop1610
[128]: https://doi.org/10.1214/22-aop1610
[129]: https://www.ams.org/mathscinet-getitem?mr=4546629
[130]: https://dx.doi.org/10.1112/S0010437X24007681
[131]: https://doi.org/10.1112/S0010437X24007681
[132]: https://www.ams.org/mathscinet-getitem?mr=4927388
[133]: https://dx.doi.org/10.1214/aoms/1177729694
[134]: https://www.ams.org/mathscinet-getitem?mr=39968
[135]: https://dx.doi.org/10.1007/s00493-025-00194-8
[136]: https://doi.org/10.1007/s00493-025-00194-8
[137]: https://www.ams.org/mathscinet-getitem?mr=5023062
[138]: https://dx.doi.org/10.1112/plms.12373
[139]: https://www.ams.org/mathscinet-getitem?mr=4144368
[140]: https://dx.doi.org/10.1002/rsa.20974
[141]: https://doi.org/10.1002/rsa.20974
[142]: https://www.ams.org/mathscinet-getitem?mr=4201799
[143]: https://dx.doi.org/10.1007/s00493-024-00128-w
[144]: https://doi.org/10.1007/s00493-024-00128-w
[145]: https://www.ams.org/mathscinet-getitem?mr=4846297
[146]: https://dx.doi.org/10.1002/rsa.20487
[147]: https://www.ams.org/mathscinet-getitem?mr=3124689
[148]: https://dx.doi.org/10.1007/s00493-011-2842-8
[149]: https://www.ams.org/mathscinet-getitem?mr=3259813
[150]: https://dx.doi.org/10.1090/S0002-9904-1949-09320-5
[151]: https://www.ams.org/mathscinet-getitem?mr=31538
[152]: https://dx.doi.org/10.1090/S0002-9904-1963-11031-9
[153]: https://www.ams.org/mathscinet-getitem?mr=155843
[154]: https://dx.doi.org/10.1109/FOCS52979.2021.00029
[155]: https://www.ams.org/mathscinet-getitem?mr=4399683
[156]: https://dx.doi.org/10.1007/s00222-022-01164-3
[157]: https://www.ams.org/mathscinet-getitem?mr=4557400
[158]: https://www.ams.org/mathscinet-getitem?mr=213190
[159]: https://dx.doi.org/10.1006/jcta.1996.2727
[160]: https://www.ams.org/mathscinet-getitem?mr=1426744
[161]: https://dx.doi.org/10.1002/num.22095
[162]: https://www.ams.org/mathscinet-getitem?mr=181483
[163]: https://dx.doi.org/10.1109/FOCS.2018.00095
[164]: https://doi.org/10.1109/FOCS.2018.00095
[165]: https://www.ams.org/mathscinet-getitem?mr=3899657
[166]: https://dx.doi.org/10.1016/0097-3165%2878%2990036-5
[167]: https://www.ams.org/mathscinet-getitem?mr=491216
[168]: https://dx.doi.org/10.1002/j.1538-7305.1948.tb01338.x
[169]: https://www.ams.org/mathscinet-getitem?mr=26286
[170]: https://dx.doi.org/10.1515/dma.1992.2.5.489
[171]: https://doi.org/10.1515/dma.1992.2.5.489
[172]: https://www.ams.org/mathscinet-getitem?mr=1138091
[173]: https://dx.doi.org/10.1007/BF02988307
[174]: https://doi.org/10.1007/BF02988307
[175]: https://www.ams.org/mathscinet-getitem?mr=1225933
[176]: https://dx.doi.org/10.1016/j.aim.2023.109127
[177]: https://www.ams.org/mathscinet-getitem?mr=4597952
[178]: https://dx.doi.org/10.19086/aic.32563
[179]: https://www.ams.org/mathscinet-getitem?mr=4406039
[180]: https://dx.doi.org/10.3390/e25050767
[181]: https://doi.org/10.3390/e25050767
[182]: https://www.ams.org/mathscinet-getitem?mr=4601918
