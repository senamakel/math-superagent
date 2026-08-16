<!-- source: https://ar5iv.labs.arxiv.org/html/2306.08824 | converted from HTML -->

[2306.08824] Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling

# Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling

Jingbo Liu Affiliation: Department of Statistics, University of Illinois, Urbana-Champaign
Email: jingbol@illinois.edu

May 2023

###### Abstract

Recently, Gilmer proved the first constant lower bound for the union-closed sets conjecture via an information-theoretic argument. The heart of the argument is an entropic inequality involving the OR function of two i.i.d. binary vectors, and the best constant obtainable through the i.i.d. coupling is 3 − 5 2 ≈ 0.38197 \frac{3-\sqrt{5}}{2}\approx 0.38197. Sawin demonstrated that the bound can be strictly improved by considering a convex combination of the i.i.d. coupling and the max-entropy coupling, and the best constant obtainable through this approach is around 0.38234, as evaluated by Yu and Cambie. In this work we show analytically that the bound can be further strictly improved by considering another class of coupling under which the two binary sequences are i.i.d. conditioned on an auxiliary random variable. We also provide a new class of bounds in terms of finite-dimensional optimization. For a basic instance from this class, analysis assisted with numerically solved 9-dimensional optimization suggests that the optimizer assumes a certain structure. Under numerically verified hypotheses, the lower bound for the union-closed sets conjecture can be improved to approximately 0.38271, a number that can be defined as the solution to an analytic equation.

## I Introduction

The union-closed sets conjecture, usually credited to Frankl, is a well-known open problem in combinatorics which has a simple statement: for any nonempty union-closed family of subsets of [n]:= { 1, 2, …, n } [n]:=\{1,2,\dots,n\}, there exists i ∈ [n] i\in[n] that belongs to at least half of these subsets [BS15]. Combinatorial arguments of Knill [Kni94] and Wójick [Wój99] proved weaker versions of the conjecture where the proportion one half is replaced by a lower bound depending on the size of the family. The first constant lower bound was achieved recently by Gilmer [Gil22] through an information theoretic argument. Let s ¯:= 1 − s \bar{s}:=1-s for any s ∈ [0, 1] s\in[0,1], and let h ⁡ ( s):= s ​ log 2 ​ 1 s + s ¯ ​ log 2 ​ 1 s ¯ h(s):=s\log_{2}\frac{1}{s}+\bar{s}\log_{2}\frac{1}{\bar{s}} denote the binary entropy function. The crux of argument is the following information-theoretic inequality:

###### Proposition 1.

Let S S be a random variable in [0, 1] [0,1] satisfying 𝔼 ⁡ [S] = u \mathbb{E}[S]=u, and let T T be an i.i.d. copy of S S. Then

 | 𝔼 ⁡ [h ⁡ ( S ¯ ​ T ¯)] ≥ 𝔼 ⁡ [h ⁡ ( S)] ⋅ { h ⁡ ( 2 ​ u − u 2) h ⁡ ( u), u ≤ 3 − 5 2 ( 1 − u) ​ 2 5 − 1, u ≥ 3 − 5 2. \displaystyle\mathbb{E}[h(\bar{S}\bar{T})]\geq\mathbb{E}[h(S)]\cdot\left\{\begin{array}[]{cc}\frac{h(2u-u^{2})}{h(u)},\quad u\leq\frac{3-\sqrt{5}}{2}\\ (1-u)\frac{2}{\sqrt{5}-1},\quad u\geq\frac{3-\sqrt{5}}{2}\end{array}\right.. |  |

Gilmer’s original paper [Gil22] established a similar bound with a suboptimal constant; the sharp bound ( 1) was established by [CL22] [AHS22] [Saw22]. Using Proposition 1, a weak form of the union-closed sets conjecture follows with constant 3 − 5 2 \frac{3-\sqrt{5}}{2}: Indeed, as in [Gil22], one may consider X n:= { X 1, …, X n } X^{n}:=\{X_{1},\dots,X_{n}\} and Y n Y^{n} two independent and identically distributed (i.i.d.) binary vectors, such that { i ∈ [n]: X i = 1 } \{i\in[n]\colon X_{i}=1\} is equiprobably distributed on the union-closed family of of sets. Then, denoting by H ( ⋅ | ⋅) H(\cdot|\cdot) the conditional Shannon entropy in bits, we have

 | H ⁡ ( X n ∨ Y n) \displaystyle H(X^{n}\vee Y^{n}) | = ∑ i = 1 n H ⁡ ( X i ∨ Y i | X i − 1 ∨ Y i − 1) \displaystyle=\sum_{i=1}^{n}H(X_{i}\vee Y_{i}|X^{i-1}\vee Y^{i-1}) |  | (3) |

 |  | ≥ ∑ i = 1 n H ⁡ ( X i ∨ Y i | X i − 1, Y i − 1), \displaystyle\geq\sum_{i=1}^{n}H(X_{i}\vee Y_{i}|X^{i-1},Y^{i-1}), |  | (4) |

where ∨ \vee denotes the elementwise max, whereas

 | H ⁡ ( X n) \displaystyle H(X^{n}) | = ∑ i = 1 n H ⁡ ( X i | X n − 1) \displaystyle=\sum_{i=1}^{n}H(X_{i}|X^{n-1}) |  | (5) |

 |  | = ∑ i = 1 n H ⁡ ( X i | X i − 1, Y i − 1). \displaystyle=\sum_{i=1}^{n}H(X_{i}|X^{i-1},Y^{i-1}). |  | (6) |

Thus, if 𝔼 ⁡ [X i] < 3 − 5 2 \mathbb{E}[X_{i}]<\frac{3-\sqrt{5}}{2} for all i i, then setting S = 𝔼 ⁡ [X i | X i − 1] S=\mathbb{E}[X_{i}|X^{i-1}] and T = 𝔼 ⁡ [Y i | Y i − 1] T=\mathbb{E}[Y_{i}|Y^{i-1}], we obtain from Proposition 1 that H ⁡ ( X n ∨ Y n) > H ⁡ ( X n) H(X^{n}\vee Y^{n})>H(X^{n}), so that the family cannot be union-closed as the equiprobable distribution maximizes the entropy for a given support.

Clearly, for this argument to work we only used the fact that max P X n ​ Y n ⁡ H ⁡ ( X n ∨ Y n) − H ⁡ ( X n) > 0 \max_{P_{X^{n}Y^{n}}}H(X^{n}\vee Y^{n})-H(X^{n})>0, where the max is over P X n ​ Y n P_{X^{n}Y^{n}} under which P X n = P Y n P_{X^{n}}=P_{Y^{n}}. This inequality appears very similar to the entropic formulation of a general version of the reverse Brascamp-Lieb inequality, for which a tensorization property is known (see [LCCV17] [LCCV18] for the max entropy version and [AJN22] for the independent coupling case); the reason why we cannot apply tensorization of Brascamp-Lieb here (and hence proving the union-closed sets conjecture by solving a simple n = 1 n=1 case) is that P X n = P Y n P_{X^{n}}=P_{Y^{n}} plays an essential role.

It is tempting to strengthen Gilmer’s lower bound by considering other coupling of X i X_{i} and Y i Y_{i} so that P X i | X i − 1 ​ Y i − 1 = P X i | X i − 1 P_{X_{i}|X^{i-1}Y^{i-1}}=P_{X_{i}|X^{i-1}}, P Y i | X i − 1 ​ Y i − 1 = P Y i | Y i − 1 P_{Y_{i}|X^{i-1}Y^{i-1}}=P_{Y_{i}|Y^{i-1}} is still true, yet H ⁡ ( X i ∨ Y i | X i − 1, Y i − 1) H(X_{i}\vee Y_{i}|X^{i-1},Y^{i-1}) becomes larger. The main challenge, however, is that S:= 𝔼 ⁡ [X i | X i − 1] S:=\mathbb{E}[X_{i}|X^{i-1}] and T:= 𝔼 ⁡ [Y i | Y i − 1] T:=\mathbb{E}[Y_{i}|Y^{i-1}] will then have more complicated dependence structure, whereas the validity of ( 1) relies strongly on the independence of S S and T T. Sawin [Saw22] proved that by taking a convex combination of the i.i.d. coupling and a coupling that maximizes H ⁡ ( X i ∨ Y i | X i − 1, Y i − 1) H(X_{i}\vee Y_{i}|X^{i-1},Y^{i-1}), one can strictly improve the best lower bound 3 − 5 2 \frac{3-\sqrt{5}}{2} obtained by the i.i.d. coupling. The best lower bound obtained by this approach was evaluated by Yu [Yu23] and Cambie [Cam22], the heart of which is the following:

###### Proposition 2.

For c ∗ c^{*} and α ∗ \alpha^{*} that can be analytically defined (see below this proposition), the following is true: For any c < c ∗ c<c^{*}, there exists C > 1 C>1 such that

 | α ¯ ∗ ​ 𝔼 ​ [h ⁡ ( S ¯ ​ T ¯)] + α ∗ ​ 𝔼 ​ [h ⁡ ( S ∨ R ∨ min ⁡ ( S + R, 1 / 2))] ≥ C ​ 𝔼 ​ [h ⁡ ( S)] \displaystyle\bar{\alpha}^{*}\mathbb{E}[h(\bar{S}\bar{T})]+\alpha^{*}\mathbb{E}[h(S\vee R\vee\min(S+R,1/2))]\geq C\mathbb{E}[h(S)] |  | (7) |

whenever P S ​ R P_{SR} is a symmetric distribution, P S ​ T = P S ​ P T P_{ST}=P_{S}P_{T}, P S = P T P_{S}=P_{T}, and 𝔼 ⁡ [S] ≤ c \mathbb{E}[S]\leq c.

Note that h ⁡ ( S ∨ R ∨ min ⁡ ( S + R, 1 / 2)) h(S\vee R\vee\min(S+R,1/2)) is the maximum H ⁡ ( X i ∨ Y i | X i − 1, Y i − 1) H(X_{i}\vee Y_{i}|X^{i-1},Y^{i-1}) for given S S and T T. Intuitively, ( 7) can hold for some c ∗ > 3 − 5 2 c^{*}>\frac{3-\sqrt{5}}{2} because the optimizer of the ratio of expected entropies in ( 1) is close to a point mass at 3 − 5 2 \frac{3-\sqrt{5}}{2} when u u is close to 3 − 5 2 \frac{3-\sqrt{5}}{2}, so when α ∗ \alpha^{*} is small the optimizer for ( 7) must be close to that point mass (in the sense of weak convergence), but the max entropy coupling produces strictly larger 𝔼 ⁡ [h ⁡ ( S ∨ R ∨ min ⁡ ( S + R, 1 / 2))] \mathbb{E}[h(S\vee R\vee\min(S+R,1/2))] in that case.

To find the best values of c ∗ c^{*} and α ∗ \alpha^{*} in Proposition 2, one can first use Krein-Milman to reduce the optimization to a finite (five) dimensional one [Yu23]. Further cardinality reduction with mass moving arguments were given in [Cam22]. Then the independent numerical optimization by Yu and Cambie confirmed that the optimizer is

 | P S ​ R ​ ( 1, b) \displaystyle P_{SR}(1,b) | = P S ​ R ​ ( b, 1) = a; \displaystyle=P_{SR}(b,1)=a; |  | (8) |

 | P S ​ R ​ ( b, b) \displaystyle P_{SR}(b,b) | = 1 − 2 ​ a, \displaystyle=1-2a, |  | (9) |

with b, a ∈ [0, 1] b,a\in[0,1] solving the set of equations

 | ( 1 − 2 ​ a) ​ h ​ ( 1 2) \displaystyle(1-2a)h(\tfrac{1}{2}) | = ( 1 − a) ​ h ​ ( b); \displaystyle=(1-a)h(b); |  | (10) |

 | ( 1 − a) 2 ​ h ​ ( b ¯ 2) \displaystyle(1-a)^{2}h(\bar{b}^{2}) | = ( 1 − a) ​ h ​ ( b). \displaystyle=(1-a)h(b). |  | (11) |

Hence h ⁡ ( b) ​ ( 2 − h ⁡ ( b)) = h ⁡ ( b ¯ 2) h(b)(2-h(b))=h(\bar{b}^{2}), which has two roots in ( 0, 1) (0,1), and we set b ∗ ≈ 0.329454738503037 b^{*}\approx 0.329454738503037 as the larger root. Let a ∗ ≈ 0.0788772927059232 a^{*}\approx 0.0788772927059232 be the corresponding solution for a a. These solutions led to

 | c ∗ ≈ 0.3823455 \displaystyle c^{*}\approx 0.3823455 |  | (12) |

which is the optimal value for the inequality in ( 7) and hence the best constant for the union-closed sets conjecture obtainable from Sawin’s approach. Define

 | f α ​ ( a, b):= α ¯ ​ 𝔼 ​ [h ⁡ ( S ¯ ​ T ¯)] + α ​ 𝔼 ​ [h ⁡ ( S ∨ R ∨ min ⁡ ( S + R, 1 / 2))] − 𝔼 ⁡ [h ⁡ ( S)]. \displaystyle f_{\alpha}(a,b):=\bar{\alpha}\mathbb{E}[h(\bar{S}\bar{T})]+\alpha\mathbb{E}[h(S\vee R\vee\min(S+R,1/2))]-\mathbb{E}[h(S)]. |  | (13) |

Then from the equations

 | ∂ a f α ​ ( a, b) ​ d ​ a + ∂ b f α ​ ( a, b) ​ d ​ b \displaystyle\partial_{a}f_{\alpha}(a,b)\,da+\partial_{b}f_{\alpha}(a,b)\,db | = 0; \displaystyle=0; |  | (14) |

 | d ​ 𝔼 ​ [S] = b ¯ ​ d ​ a + a ¯ ​ d ​ b \displaystyle d\mathbb{E}[S]=\bar{b}\,da+\bar{a}\,db | = 0, \displaystyle=0, |  | (15) |

we obtain

 | α ∗ = − a ¯ ​ [2 ​ a ¯ ​ h ​ ( b ¯ 2) − h ⁡ ( b)] + b ¯ ​ [2 ​ a ¯ 2 ​ b ¯ ​ log ⁡ 1 − b ¯ 2 b ¯ 2 + a ¯ ​ log ⁡ b ¯ b] − 2 ​ a ¯ ​ [a ¯ ​ h ​ ( b ¯ 2) − 1] + 2 ​ a ¯ 2 ​ b ¯ 2 ​ log ⁡ 1 − b ¯ 2 b ¯ 2. \displaystyle\alpha^{*}=\frac{-\bar{a}[2\bar{a}h(\bar{b}^{2})-h(b)]+\bar{b}[2\bar{a}^{2}\bar{b}\log\frac{1-\bar{b}^{2}}{\bar{b}^{2}}+\bar{a}\log\frac{\bar{b}}{b}]}{-2\bar{a}[\bar{a}h(\bar{b}^{2})-1]+2\bar{a}^{2}\bar{b}^{2}\log\frac{1-\bar{b}^{2}}{\bar{b}^{2}}}. |  | (16) |

Plugging in the values of a ∗ a^{*} and b ∗ b^{*} we obtain α ∗ ≈ 0.0356069 \alpha^{*}\approx 0.0356069.

Contribution. In this paper we improve the previous best lower bound c ∗ c^{*} in ( 12) for the union-closed sets conjecture by considering a new class of couplings of X n X^{n} and Y n Y^{n} that ensures P S ​ T P_{ST} is a mixture of i.i.d. distribution. In other words, our coupling ensures the existence of some random variable U U such that S S and T T are i.i.d. conditioned on U U. The main observation is that the equality case of ( 7), excluding the trivial case of P S P_{S} supported on { 0, 1 } \{0,1\}, is given by ( 8)-( 9), which is a symmetric distribution but [P S ​ T ​ ( s, t)] s, t ∈ { b, 1 } [P_{ST}(s,t)]_{s,t\in\{b,1\}} is not positive semidefinite and hence not a mixture of i.i.d. distributions.

By taking a convex combination of the left side of ( 13) and H ⁡ ( X i ∨ Y i | X i − 1, Y i − 1) H(X_{i}\vee Y_{i}|X^{i-1},Y^{i-1}) under the new coupling scheme, we can show analytically that c ∗ c^{*} can be strictly improved (Section III). This argument is analogous to that of Sawin [Saw22] which proves strict improvement over the (unconditional) i.i.d. coupling by considering the limit of small convex combination weight, without numerical evaluation. Note that c ∗ c^{*} was previously the best lower bound; in Remark 1 we show that if we apply a similar convex combination argument (in the regime of small combination weight) to Yu’s general bound based on maximal correlation [Yu23], there is no improvement over c ∗ c^{*}.

In order to further numerically evaluate bounds obtainable from this new class of coupling, we then consider a convex combination of just Gilmer’s original i.i.d. coupling and the conditionally i.i.d. coupling, without Sawin’s max entropy coupling in the second term in ( 7). This allows us to show that considering two-mixture P S ​ T P_{ST} is sufficient. Under addition assumptions on the class of conditionally i.i.d. coupling employed, we further reduce the computation of the lower bound to a 9 dimensional optimization problem (Section V). For a basic instance from this class, numerical results using Matlab optimization package (interior point, sqp, active-set algorithms) with at least 10 5 10^{5} random initializations suggests that the best local optimizer has a certain structure. Under this structural assumption, the global optimizer can be expressed as the solution to a set of analytic equations, which in turns shows that the lower bound for the union-closed sets conjecture can be improved to approximately 0.382709 (Section V).

## II Conditionally IID Coupling

In this section we explain the main idea for improvement based on conditionally i.i.d. coupling. First, we formalize a method of sampling X i X_{i} and Y i Y_{i} given ( X i − 1, Y i − 1) (X^{i-1},Y^{i-1}) as follows:

###### Definition 1.

We say Π \Pi is a *protocol*if for any ( s, t) ∈ [0, 1] 2 (s,t)\in[0,1]^{2}, Π s, t \Pi_{s,t} is a distribution on { 0, 1 } 2 \{0,1\}^{2} satisfying: For any ( s, t) ∈ [0, 1] 2 (s,t)\in[0,1]^{2}, we have 𝔼 ⁡ [X] = s \mathbb{E}[X]=s and 𝔼 ⁡ [Y] = t \mathbb{E}[Y]=t, where ( X, Y) ∼ Π s, t (X,Y)\sim\Pi_{s,t}.

Given any P X n P_{X^{n}}, a protocol Π \Pi defines a method of randomly and sequentially generating X n X^{n} and Y n Y^{n}: for each i = 1, …, n i=1,\dots,n and given ( X i − 1, Y i − 1) (X^{i-1},Y^{i-1}), we generate X i X_{i} and Y i Y_{i} according to Π s, t \Pi_{s,t}, where s:= P X i | X i − 1 ​ ( 1 | X i − 1) s:=P_{X_{i}|X^{i-1}}(1|X^{i-1}) and t:= P X i | X i − 1 ​ ( 1 | Y i − 1) t:=P_{X_{i}|X^{i-1}}(1|Y^{i-1}), and P X i | X i − 1 P_{X_{i}|X^{i-1}} is the conditional distribution induced by P X n P_{X^{n}}. This is a broad class of couplings that includes Gilmer’s i.i.d. coupling [Gil22], Sawin’s max-entropy coupling [Saw22], Yu’s maximal correlation based coupling [Yu23], and also the conditionally i.i.d. coupling that we will soon introduce.

The idea of taking convex combination of protocols in Proposition 2 can now be explained in larger generality: Suppose that there are protocols Π ( 1) \Pi^{(1)}, …, Π ( K) \Pi^{(K)} such that for all distribution μ \mu on [0, 1] [0,1] with mean not exceeding c c, we have

 | ∑ k = 1 K w k ​ inf P S ​ T ∈ 𝒞 k ​ ( μ) 𝔼 ⁡ [h ⁡ ( Π S, T ( k) ​ ( 0, 0))] ≥ C ​ 𝔼 ​ [h ⁡ ( S)] \displaystyle\sum_{k=1}^{K}w_{k}\inf_{P_{ST}\in\mathcal{C}_{k}(\mu)}\mathbb{E}[h(\Pi_{S,T}^{(k)}(0,0))]\geq C\mathbb{E}[h(S)] |  | (17) |

where w 1, …, w K ≥ 0 w_{1},\dots,w_{K}\geq 0, ∑ k = 1 K w k = 1 \sum_{k=1}^{K}w_{k}=1, C > 1 C>1 are fixed, and 𝒞 k ​ ( μ) \mathcal{C}_{k}(\mu) is a set large enough to contain all the couplings of μ \mu and μ \mu that can possibly be induced by the k k -protocol. For example, in Gilmer’s approach, K = 1 K=1, Π s, t ( 1) = Bern ⁡ ( s) × Bern ⁡ ( t) \Pi_{s,t}^{(1)}={\rm Bern}(s)\times{\rm Bern}(t), and 𝒞 1 \mathcal{C}_{1} is the singleton set containing μ × μ \mu\times\mu. Sawin’s improvement can be interpreted as the case of K = 2 K=2, and Π s, t ( 2) \Pi_{s,t}^{(2)} is the most greedy coupling of Bern ⁡ ( s) {\rm Bern}(s) and Bern ⁡ ( t) {\rm Bern}(t) that maximizes the entropy of the OR function. Correspondingly, 𝒞 2 ​ ( μ) \mathcal{C}_{2}(\mu) is a rather large set – probably no better choice than taking all symmetric couplings of μ \mu and μ \mu. In Yu’s maximal correlation based formulation, Π s, t \Pi_{s,t} satisfies a maximal correlation upper bound, and so by tensorization 𝒞 ⁡ ( μ) \mathcal{C}(\mu) is the set of distributions satisfying the same maximal correlation upper bound.

###### Proposition 3.

If ( 17) holds with constant c > 0 c>0, then c c is a lower bound for the constant in the union-closed sets conjecture.

###### Proof.

We can identify the given family of subsets with binary sequences where a coordinate 1 indicates inclusion of the corresponding element. Let P X n P_{X^{n}} be the equiprobable distribution on the resulting set of binary sequences. Let ( X ( k) ​ n, Y ( k) ​ n) (X^{(k)n},Y^{(k)n}) be induced by protocol Π ( k) \Pi^{(k)}. Assuming P X i ​ ( 1) < c P_{X_{i}}(1)<c for all i i, then analogous to ( 4), we obtain from ( 17) that

 | ∑ k = 1 K w k ​ H ​ ( X ( k) ​ n ∨ Y ( k) ​ n) ≥ C ​ H ​ ( X n). \displaystyle\sum_{k=1}^{K}w_{k}H(X^{(k)n}\vee Y^{(k)n})\geq CH(X^{n}). |  | (18) |

Since the equiprobable distribution maximizes entropy among distributions supported on the a given set, this would imply that the given family is not union-closed. ∎

We next define a new class of Π ( 3) \Pi^{(3)} for which h ⁡ ( Π s, t ( 3) ​ ( 0, 0)) h(\Pi_{s,t}^{(3)}(0,0)) is larger than Gilmer’s independent coupling, yet 𝒞 3 ​ ( μ) \mathcal{C}_{3}(\mu) is strictly smaller than the set of symmetric couplings 𝒞 2 \mathcal{C}_{2} as in Sawin’s improvement.

###### Definition 2.

A protocol Π \Pi is *conditionally IID*if it can represented as

 | Π s, t ​ ( x, y) = ∫ Q u, s ​ ( x) ​ Q u, t ​ ( y) ​ P U ​ ( 𝑑 u) \displaystyle\Pi_{s,t}(x,y)=\int Q_{u,s}(x)Q_{u,t}(y)P_{U}(du) |  | (19) |

where Q u, s Q_{u,s} is a Bernoulli distribution whose mean is a function of ( u, s) (u,s), and P U P_{U} is an arbitrary probability measure. By the isomorphism theorem of standard probability spaces, we can assume that P U P_{U} is the uniform probability distribution on [0, 1] [0,1].

The max-entropy protocol of Sawin, which uses Π s, t ( 2) ​ ( 0, 0) = 1 − s ∨ t ∨ min ⁡ ( s + t, 1 / 2) \Pi^{(2)}_{s,t}(0,0)=1-s\vee t\vee\min(s+t,1/2), is not conditionally IID. Indeed, for s = t < 1 / 4 s=t<1/4 we see [Π s, t ( 2) ​ ( x, y)] x, y ∈ { 0, 1 } [\Pi_{s,t}^{(2)}(x,y)]_{x,y\in\{0,1\}} is matrix with diagonals equal 0, 1 − 2 ​ s 1-2s and off-diagonals equal s s, so it is not positive semidefinite, and hence cannot be the form ( 19).

###### Example 4.

Let 𝒳 \mathcal{X} and 𝒴 \mathcal{Y} be two players with their local randomness, and let the common randomness be U U a random variable uniformly distributed on [0, 1] [0,1]. Let a ⁡ ( ⋅) a(\cdot) be a measurable function on [0, 1] [0,1]. Given U = u U=u and s s in [0, 1] [0,1], let X ∼ Q u, s X\sim Q_{u,s} be simulated this way: use the local randomness of 𝒳 \mathcal{X} (which is not known to 𝒴 \mathcal{Y}) to simulate B ∼ Ber ⁡ ( a ⁡ ( s)) B\sim{\rm Ber}(a(s)). If B = 0 B=0, then X X is generated as a Ber ⁡ ( s) {\rm Ber}(s) random variable using the local randomness of 𝒳 \mathcal{X}; if B = 1 B=1, we set X = 1 U < s X=1_{U<s}. Then X ∼ Ber ⁡ ( s) X\sim{\rm Ber}(s) (conditioned on s s). Generate Y Y similarly using u u and t t. We have

 |  | ℙ ⁡ [X = Y = 0 | U] \displaystyle\quad\mathbb{P}[X=Y=0|U] |  |

 |  | = a ⁡ ( s) ​ a ​ ( t) ​ 1 U ≥ s ∨ t + a ⁡ ( s) ​ ( 1 − a ⁡ ( t)) ​ 1 U ≥ s ​ t ¯ \displaystyle=a(s)a(t)1_{U\geq s\vee t}+a(s)(1-a(t))1_{U\geq s}\bar{t} |  |

 |  | + ( 1 − a ⁡ ( s)) ​ a ​ ( t) ​ s ¯ ​ 1 U ≥ t + ( 1 − a ⁡ ( s)) ​ ( 1 − a ⁡ ( t)) ​ s ¯ ​ t ¯ \displaystyle\quad+(1-a(s))a(t)\bar{s}1_{U\geq t}+(1-a(s))(1-a(t))\bar{s}\bar{t} |  | (20) |

and hence

 | Π s, t ​ ( 0, 0) \displaystyle\Pi_{s,t}(0,0) | = a ⁡ ( s) ​ a ​ ( t) ​ ( 1 − s ∨ t) + ( 1 − a ⁡ ( s)) ​ a ​ ( t) ​ s ¯ ​ t ¯ \displaystyle=a(s)a(t)(1-s\vee t)+(1-a(s))a(t)\bar{s}\bar{t} |  |

 |  | + a ⁡ ( s) ​ ( 1 − a ⁡ ( t)) ​ s ¯ ​ t ¯ + ( 1 − a ⁡ ( s)) ​ ( 1 − a ⁡ ( t)) ​ s ¯ ​ t ¯ \displaystyle\quad+a(s)(1-a(t))\bar{s}\bar{t}+(1-a(s))(1-a(t))\bar{s}\bar{t} |  | (21) |

 |  | = s ¯ ​ t ¯ + a ⁡ ( s) ​ a ​ ( t) ​ ( s ¯ ∧ t ¯ − s ¯ ​ t ¯). \displaystyle=\bar{s}\bar{t}+a(s)a(t)(\bar{s}\wedge\bar{t}-\bar{s}\bar{t}). |  | (22) |

If we choose a ⁡ () a() to maximize h ⁡ ( Π s, t ​ ( 0, 0)) = h ⁡ ( t ¯ 2 + a ​ ( t) 2 ​ t ​ t ¯) h(\Pi_{s,t}(0,0))=h(\bar{t}^{2}+a(t)^{2}t\bar{t}) for any given t t, we are led to

 | a ⁡ ( t) = { 0 t ≤ 1 − 1 2 1 − 2 ​ t ¯ 2 2 ​ t ​ t ¯ 1 − 1 2 < t ≤ 1 2 1 t > 1 2. \displaystyle a(t)=\left\{\begin{array}[]{cc}0&t\leq 1-\frac{1}{\sqrt{2}}\\ \sqrt{\frac{1-2\bar{t}^{2}}{2t\bar{t}}}&1-\frac{1}{\sqrt{2}}<t\leq\frac{1}{2}\\ 1&t>\frac{1}{2}\end{array}\right.. |  |

###### Example 5.

Let P U P_{U} be the uniform distribution on [0, 1] [0,1], and let f ⁡ () f() be a measurable function on [0, 1] [0,1] satisfying 0 ≤ f ⁡ ( s ¯) ≤ s ∧ s ¯ 0\leq f(\bar{s})\leq s\wedge\bar{s}. Given u, s ∈ [0, 1] u,s\in[0,1], let X ∼ Q u, s X\sim Q_{u,s} be simulated this way: set X = 0 X=0 with probability s ¯ + f ⁡ ( s ¯) ​ ( 1 u > 1 2 − 1 u ≤ 1 2) \bar{s}+f(\bar{s})(1_{u>\frac{1}{2}}-1_{u\leq\frac{1}{2}}), and X = 1 X=1 with the remaining probability. Then Π s, t ​ ( 0, 0) = s ¯ ​ t ¯ + f ⁡ ( s ¯) ​ f ​ ( t ¯). \Pi_{s,t}(0,0)=\bar{s}\bar{t}+f(\bar{s})f(\bar{t}).

The coupling induced by a conditional IID protocol can be interpreted as simulating each X i X_{i} by looking only at X i − 1 X^{i-1} and U i − 1 U^{i-1}, without referencing the Y Y -sequence, and similarly for each Y i Y_{i}. Therefore, X i X^{i} and Y i Y^{i} are conditionally i.i.d. given U i U^{i} for all n n. Hence 𝔼 ⁡ [X i | X i − 1] \mathbb{E}[X_{i}|X^{i-1}] and 𝔼 ⁡ [Y i | Y i − 1] \mathbb{E}[Y_{i}|Y^{i-1}], which are functions of X i − 1 X^{i-1} and Y i − 1 Y^{i-1}, are conditionally i.i.d. We can therefore take

 | 𝒞 3 ​ ( μ):= { couplings of μ and μ } ∩ cl ​ conv ​ { symmetric rank-1 measures } \displaystyle\mathcal{C}_{3}(\mu):=\{\textrm{couplings of $\mu$ and $\mu$}\}\cap{\rm cl}\,{\rm conv}\{\textrm{symmetric rank-1 measures}\} |  | (26) |

where conv {\rm conv} denotes the convex hull, and the closure cl {\rm cl} is with respect to weak convergence (ensuring that we can invoke Krein-Milman later).

## III Analytic Proof of Strict Improvement

Recall that c ∗ ≈ 0.3823455 c^{*}\approx 0.3823455, defined around ( 11) as solution to analytic equations, was the previous best lower bound for the union-closed sets conjecture. The main result of the section is the following:

###### Theorem 6.

The union-closed sets conjecture holds with a constant strictly larger than c ∗ c^{*}.

The idea is to use ( 17) and perturb the previous best scheme with a conditionally IID protocol. First, we prove the following result which allows us to not worry about the case of P S P_{S} supported on { 0, 1 } \{0,1\}, a trivial equality case for ( 17). This observation was briefly mentioned (without quantitative bound) in Sawin’s paper [Saw22].

###### Lemma 7.

Let c ∈ ( 0, 1) c\in(0,1). Suppose that μ n \mu_{n} is a sequence of probability measures with mean equal to c c and converging weakly to μ ∗ \mu^{*}, where μ ∗ \mu^{*} is the (unique) probability measure supported on { 0, 1 } \{0,1\} and with mean equal to c c. Then

 | lim inf n → ∞ ∫ h ⁡ ( s ¯ ​ t ¯) ​ μ n ​ ( 𝑑 s) ​ μ n ​ ( 𝑑 t) ∫ h ⁡ ( s) ​ μ n ​ ( 𝑑 s) ≥ 2 ​ c ¯. \displaystyle\liminf_{n\to\infty}\frac{\int h(\bar{s}\bar{t})\mu_{n}(ds)\mu_{n}(dt)}{\int h(s)\mu_{n}(ds)}\geq 2\bar{c}. |  | (27) |

###### Proof.

By the assumption of weak convergence, we can pick a sequence ϵ n ↓ 0 \epsilon_{n}\downarrow 0 such that

 | μ n ​ ( [ϵ n, 1 − ϵ n]) ≤ ϵ n. \displaystyle\mu_{n}([\epsilon_{n},1-\epsilon_{n}])\leq\epsilon_{n}. |  | (28) |

Let 𝒜 n:= [0, ϵ n) \mathcal{A}_{n}:=[0,\epsilon_{n}) and ℬ n:= [ϵ n, 1] \mathcal{B}_{n}:=[\epsilon_{n},1]. Using h ⁡ ( x) ∼ x ​ ln ⁡ 1 x h(x)\sim x\ln\frac{1}{x} as x → 0 x\to 0, we see

 | lim n → ∞ inf s ∈ 𝒜 n, t ∈ ℬ n h ⁡ ( s ¯ ​ t ¯) h ⁡ ( t ¯) = 1. \displaystyle\lim_{n\to\infty}\inf_{s\in\mathcal{A}_{n},t\in\mathcal{B}_{n}}\frac{h(\bar{s}\bar{t})}{h(\bar{t})}=1. |  | (29) |

Therefore we have

 | lim inf n → ∞ ∫ 𝒜 n × ℬ n h ⁡ ( s ¯ ​ t ¯) ​ μ n ​ ( 𝑑 s) ​ μ n ​ ( 𝑑 t) ∫ ℬ n h ⁡ ( s) ​ μ n ​ ( 𝑑 s) ≥ lim n → ∞ μ n ​ ( 𝒜 n) = c ¯. \displaystyle\liminf_{n\to\infty}\frac{\int_{\mathcal{A}_{n}\times\mathcal{B}_{n}}h(\bar{s}\bar{t})\mu_{n}(ds)\mu_{n}(dt)}{\int_{\mathcal{B}_{n}}{h(s)\mu_{n}(ds)}}\geq\lim_{n\to\infty}\mu_{n}(\mathcal{A}_{n})=\bar{c}. |  | (30) |

Moreover, applying Proposition 1 to the probability measure (conditional probability) 1 μ n ​ ( 𝒜 n) ​ μ n | 𝒜 n \frac{1}{\mu_{n}(\mathcal{A}_{n})}\mu_{n}|_{\mathcal{A}_{n}}, whose mean is smaller than ϵ n \epsilon_{n}, we obtain

 | lim inf n → ∞ ∫ 𝒜 n × 𝒜 n h ⁡ ( s ¯ ​ t ¯) ​ μ n ​ ( 𝑑 s) ​ μ n ​ ( 𝑑 t) ∫ 𝒜 n h ⁡ ( s) ​ μ n ​ ( 𝑑 t) ≥ 2 ​ lim n → ∞ μ n ​ ( 𝒜 n) = 2 ​ c ¯. \displaystyle\liminf_{n\to\infty}\frac{\int_{\mathcal{A}_{n}\times\mathcal{A}_{n}}h(\bar{s}\bar{t})\mu_{n}(ds)\mu_{n}(dt)}{\int_{\mathcal{A}_{n}}h(s)\mu_{n}(dt)}\geq 2\lim_{n\to\infty}\mu_{n}(\mathcal{A}_{n})=2\bar{c}. |  | (31) |

The lemma then follows by ( 30)-( 31) and ∫ 𝒜 n × ℬ n h ⁡ ( s ¯ ​ t ¯) ​ μ n ​ ( 𝑑 s) ​ μ n ​ ( 𝑑 t) = ∫ ℬ n × 𝒜 n h ⁡ ( s ¯ ​ t ¯) ​ μ n ​ ( 𝑑 s) ​ μ n ​ ( 𝑑 t) \int_{\mathcal{A}_{n}\times\mathcal{B}_{n}}h(\bar{s}\bar{t})\mu_{n}(ds)\mu_{n}(dt)=\int_{\mathcal{B}_{n}\times\mathcal{A}_{n}}h(\bar{s}\bar{t})\mu_{n}(ds)\mu_{n}(dt). ∎

Theorem 6 now follows by Proposition 3 and the following observation:

###### Lemma 8.

Let a ⁡ ( ⋅) a(\cdot) be as in ( II) and let Π ( 3) \Pi^{(3)} be the corresponding conditionally i.i.d. protocol. There exists β ∈ ( 0, 1) \beta\in(0,1), c ′ > c ∗ c^{\prime}>c^{*}, and C > 1 C>1 such that

 | α ¯ ∗ ​ β ¯ ​ 𝔼 ​ [h ⁡ ( S ¯ ​ T ¯)] + α ∗ ​ β ¯ ​ 𝔼 ​ [h ⁡ ( S ∨ R 1 ∨ min ⁡ ( S + R 1, 1 / 2))] \displaystyle\bar{\alpha}^{*}\bar{\beta}\mathbb{E}[h(\bar{S}\bar{T})]+\alpha^{*}\bar{\beta}\mathbb{E}[h(S\vee R_{1}\vee\min(S+R_{1},1/2))] |  |

 | + β ​ 𝔼 ​ [h ⁡ ( S ¯ ​ R ¯ 2 + a ⁡ ( S) ​ a ​ ( R 2) ​ ( S ¯ ∧ R ¯ 2 − S ¯ ​ R ¯ 2))] ≥ C ​ 𝔼 ​ [h ⁡ ( S)] \displaystyle+\beta\mathbb{E}[h(\bar{S}\bar{R}_{2}+a(S)a(R_{2})(\bar{S}\wedge\bar{R}_{2}-\bar{S}\bar{R}_{2}))]\geq C\mathbb{E}[h(S)] |  | (32) |

whenever 𝔼 ⁡ [S] ≤ c ′ \mathbb{E}[S]\leq c^{\prime}, P S ​ T ∈ 𝒞 1 ​ ( P S) P_{ST}\in\mathcal{C}_{1}(P_{S}) P S ​ R 1 ∈ 𝒞 2 ​ ( P S) P_{SR_{1}}\in\mathcal{C}_{2}(P_{S}), P S ​ R 2 ∈ 𝒞 3 ​ ( P S) P_{SR_{2}}\in\mathcal{C}_{3}(P_{S}).

###### Proof.

Let P S ∗ P_{S}^{*} be the two-point distribution where ℙ [S = b ∗] = 1 − a ∗ \mathbb{P}[S=b^{*}]=1-a^{*} and ℙ [S = 1] = a ∗ \mathbb{P}[S=1]=a^{*}, with a ∗ a^{*} and b ∗ b^{*} defined around ( 12). Note that

 | inf P S ​ R 2 ∈ 𝒞 3 ​ ( P S ∗) 𝔼 ⁡ [h ⁡ ( Π S, R 2 ( 3) ​ ( 0, 0))] 𝔼 ⁡ [h ⁡ ( S)] > 1. \displaystyle\inf_{P_{SR_{2}}\in\mathcal{C}_{3}(P_{S}^{*})}\frac{\mathbb{E}[h(\Pi_{S,R_{2}}^{(3)}(0,0))]}{\mathbb{E}[h(S)]}>1. |  | (33) |

Indeed, if the infimum on the left side of ( 37) is over P S ​ R 2 ∈ 𝒞 2 ​ ( P S ∗) P_{SR_{2}}\in\mathcal{C}_{2}(P_{S}^{*}) instead, then the infimum equals 1, achieved at P S ​ R 2 ∗ P_{SR_{2}}^{*} defined as

 | P S ​ R 2 ∗ ​ ( 1, 1) \displaystyle P_{SR_{2}}^{*}(1,1) | = 0; \displaystyle=0; |  | (34) |

 | P S ​ R 2 ∗ ​ ( b ∗, 1) \displaystyle P_{SR_{2}}^{*}(b^{*},1) | = P S ​ R 2 ∗ ​ ( 1, b ∗) = a ∗; \displaystyle=P_{SR_{2}}^{*}(1,b^{*})=a^{*}; |  | (35) |

 | P S ​ R 2 ∗ ​ ( b ∗, b ∗) \displaystyle P_{SR_{2}}^{*}(b^{*},b^{*}) | = 1 − 2 ​ a ∗. \displaystyle=1-2a^{*}. |  | (36) |

Since P S ​ R 2 ∗ ∈ P S ​ R 2 P_{SR_{2}}^{*}\in P_{SR_{2}} belongs to 𝒞 2 ​ ( P S ∗) \mathcal{C}_{2}(P_{S}^{*}) but not 𝒞 3 ​ ( P S ∗) \mathcal{C}_{3}(P_{S}^{*}), and 𝒞 3 ​ ( P S ∗) ⊆ 𝒞 2 ​ ( P S ∗) \mathcal{C}_{3}(P_{S}^{*})\subseteq\mathcal{C}_{2}(P_{S}^{*}), we see ( 37) holds.

Next, we claim that there exists some δ > 0 \delta>0 such that

 | inf P S: W 1 ​ ( P S, P S ∗) < δ inf P S ​ R 2 ∈ 𝒞 3 ​ ( P S) 𝔼 ⁡ [h ⁡ ( Π S, R 2 ( 3) ​ ( 0, 0))] 𝔼 ⁡ [h ⁡ ( S)] > 1, \displaystyle\inf_{P_{S}:\,W_{1}(P_{S},P_{S}^{*})<\delta}\,\inf_{P_{SR_{2}}\in\mathcal{C}_{3}(P_{S})}\frac{\mathbb{E}[h(\Pi_{S,R_{2}}^{(3)}(0,0))]}{\mathbb{E}[h(S)]}>1, |  | (37) |

where W 1 W_{1} denotes the Wasserstein-1 distance. Indeed, for any such P S P_{S} in ( 37) and for P S ​ R 2 ∈ 𝒞 3 ​ ( P S) P_{SR_{2}}\in\mathcal{C}_{3}(P_{S}), we can construct a P S ​ R 2 ∗ ⁣ ∗ ∈ 𝒞 3 ​ ( P S ∗) P_{SR_{2}}^{**}\in\mathcal{C}_{3}(P_{S}^{*}) such that W 1 ​ ( P S ​ R 2, P S ​ R 2 ∗ ⁣ ∗) ≤ 2 ​ δ W_{1}(P_{SR_{2}},P_{SR_{2}}^{**})\leq 2\delta, by using the optimal transport (stochastic) map in the definition of the Wasserstein distance. By choosing δ > 0 \delta>0 small enough we can also assume that P S P_{S} is bounded away from measures supported on { 0, 1 } \{0,1\}, so that the denominator in ( 37) is bounded away from 0. Then the claim follows by the continuity of the numerator and denominator in ( 37) with respect to weak convergence (equivalently, with respect to W 1 W_{1}).

Now define

 | g ⁡ ( P S):= inf P S ​ R 2 α ¯ ∗ ​ 𝔼 ​ [h ⁡ ( Π S, T ( 1) ​ ( 0, 0))] + α ∗ ​ 𝔼 ​ [h ⁡ ( Π S, R 1 ( 2) ​ ( 0, 0))] 𝔼 ⁡ [h ⁡ ( S)] \displaystyle g(P_{S}):=\inf_{P_{SR_{2}}}\frac{\bar{\alpha}^{*}\mathbb{E}[h(\Pi_{S,T}^{(1)}(0,0))]+\alpha^{*}\mathbb{E}[h(\Pi_{S,R_{1}}^{(2)}(0,0))]}{\mathbb{E}[h(S)]} |  | (38) |

where T T is an i.i.d. copy of S S. Set

 | C δ:= inf P S: W 1 ​ ( P S, P S ∗) ≥ δ, 𝔼 ⁡ [S] ≤ c ∗ g ( P S). \displaystyle C_{\delta}:=\inf_{P_{S}:\,W_{1}(P_{S},\,P_{S}^{*})\geq\delta,\,\mathbb{E}[S]\leq c^{*}}g(P_{S}). |  | (39) |

Then C δ > 1 C_{\delta}>1 for any δ > 0 \delta>0. Indeed, suppose that P S n P_{S}^{n} is a weakly convergent sequence satisfying W 1 ​ ( P S n, P S ∗) ≥ δ W_{1}(P_{S}^{n},P_{S}^{*})\geq\delta, 𝔼 P S n ​ [S] ≤ c ∗ \mathbb{E}_{P_{S}^{n}}[S]\leq c^{*}, and lim n → ∞ g ⁡ ( P S n) = C δ \lim_{n\to\infty}g(P_{S}^{n})=C_{\delta}. If P S ′:= lim n → ∞ P S n P_{S}^{\prime}:=\lim_{n\to\infty}P_{S}^{n} is supported on { 0, 1 } \{0,1\}, then by Lemma 7 we have C δ ≥ 2 ​ c ¯ ∗ ​ α ¯ ∗ > 1 C_{\delta}\geq 2\bar{c}^{*}\bar{\alpha}^{*}>1; otherwise, C δ = g ⁡ ( P S ′) C_{\delta}=g(P_{S}^{\prime}) and 𝔼 P S ′ ​ [h ​ ( S)] > 0 \mathbb{E}_{P_{S}^{\prime}}[h(S)]>0, and we conclude from the condition of strict inequality in Proposition 2 that C δ > 1 C_{\delta}>1.

Now we can set β ∈ ( 0, 1) \beta\in(0,1) as any number satisfying β ¯ ​ C δ > 1 \bar{\beta}C_{\delta}>1. Since Proposition 2 showed

 | inf P S: 𝔼 ⁡ [S] ≤ c ∗ g ( P S) ≥ 1, \displaystyle\inf_{P_{S}:\,\mathbb{E}[S]\leq c^{*}}g(P_{S})\geq 1, |  | (40) |

together with ( 37) we have established

 | inf P S: W 1 ​ ( P S, P S ∗) < δ, 𝔼 ⁡ [S] ≤ c ∗ f ( β, P S) > 1 \displaystyle\inf_{P_{S}:\,W_{1}(P_{S},P_{S}^{*})<\delta,\,\mathbb{E}[S]\leq c^{*}}f(\beta,P_{S})>1 |  | (41) |

where

 |  | f ⁡ ( β, P S):= \displaystyle f(\beta,P_{S}):= |  |

 |  | inf P S ​ R 1 ∈ 𝒞 2 ​ ( P S), P S ​ R 2 ∈ 𝒞 3 ​ ( P S) α ¯ ∗ ​ β ¯ ​ 𝔼 ​ [h ⁡ ( Π S, T ( 1) ​ ( 0, 0))] + α ∗ ​ β ¯ ​ 𝔼 ​ [h ⁡ ( Π S, R 1 ( 2) ​ ( 0, 0))] + β ​ 𝔼 ​ [h ⁡ ( Π S, R 2 ( 3) ​ ( 0, 0))] 𝔼 ⁡ [h ⁡ ( S)]. \displaystyle\inf_{P_{SR_{1}}\in\mathcal{C}_{2}(P_{S}),P_{SR_{2}}\in\mathcal{C}_{3}(P_{S})}\tfrac{\bar{\alpha}^{*}\bar{\beta}\mathbb{E}[h(\Pi_{S,T}^{(1)}(0,0))]+\alpha^{*}\bar{\beta}\mathbb{E}[h(\Pi_{S,R_{1}}^{(2)}(0,0))]+\beta\mathbb{E}[h(\Pi_{S,R_{2}}^{(3)}(0,0))]}{\mathbb{E}[h(S)]}. |  | (42) |

Combining ( 42) with β ¯ ​ C δ > 1 \bar{\beta}C_{\delta}>1, we actually have

 | inf P S: 𝔼 ⁡ [S] ≤ c ∗ f ( β, P S) > 1. \displaystyle\inf_{P_{S}:\,\mathbb{E}[S]\leq c^{*}}f(\beta,P_{S})>1. |  | (43) |

Finally, suppose that P S n P_{S}^{n} is a weakly convergent sequence that such that 𝔼 P S n ​ [S] = c ∗ + 1 n \mathbb{E}_{P_{S}^{n}}[S]=c^{*}+\frac{1}{n} and

 | lim n → ∞ f ( β, P S n) ≤ lim n → ∞ inf P S: 𝔼 ⁡ [S] ≤ c ∗ + 1 n f ( β, P S). \displaystyle\lim_{n\to\infty}f(\beta,P_{S}^{n})\leq\lim_{n\to\infty}\inf_{P_{S}:\,\mathbb{E}[S]\leq c^{*}+\frac{1}{n}}f(\beta,P_{S}). |  | (44) |

If P S n P_{S}^{n} converges to a probability measure supported on { 0, 1 } \{0,1\}, we conclude from Lemma 7 that lim n → ∞ f ⁡ ( β, P S n) ≥ 2 ​ c ¯ ∗ \lim_{n\to\infty}f(\beta,P_{S}^{n})\geq 2\bar{c}^{*}; otherwise, lim n → ∞ f ⁡ ( β, P S n) = f ⁡ ( β, lim n → ∞ P S n) > 1 \lim_{n\to\infty}f(\beta,P_{S}^{n})=f(\beta,\lim_{n\to\infty}P_{S}^{n})>1 by ( 43). We therefore established that the right side of ( 44) is strictly larger than 1, which is the claim of the lemma. ∎

###### Remark 1.

Yu [Yu23] considered Π \Pi that ensures the maximal correlation coefficient of the binary pair distribution Π s, t \Pi_{s,t} is upper bounded by a given ρ ∈ [0, 1] \rho\in[0,1] for any ( s, t) (s,t). Then by a tensorization property, it follows that 𝒞 \mathcal{C} can be taken to be the set of distributions on [0, 1] 2 [0,1]^{2} with maximal correlation upper bounded by ρ \rho. The cases of ρ = 0 \rho=0 and ρ = 1 \rho=1 reduces to the i.i.d. coupling and the max-entropy coupling, respectively. A natural question is whether we can pick some ρ ∈ ( 0, 1) \rho\in(0,1) and apply a similar argument as Lemma 8 to show strict improvement on c ∗ c^{*}. The answer is positive only if for some ρ ∈ ( 0, 1) \rho\in(0,1),

 | P S ​ T ​ ( b ∗, b ∗) ​ h ​ ( Π b ∗ ​ b ∗ ​ ( 0, 0)) − ( 1 − a ∗) ​ h ​ ( b ∗) > 0, \displaystyle P_{ST}(b^{*},b^{*})h(\Pi_{b^{*}b^{*}}(0,0))-(1-a^{*})h(b^{*})>0, |  | (45) |

where P S ​ T P_{ST} is the coupling of P S = P T P_{S}=P_{T} defined by P S ​ ( b ∗) = 1 − a ∗ P_{S}(b^{*})=1-a^{*} and P S ​ ( 1) = a ∗ P_{S}(1)=a^{*} with maximal correlation upper-bounded by ρ \rho such that P S ​ T ​ ( b ∗, b ∗) P_{ST}(b^{*},b^{*}) is minimized, and Π b ∗ ​ b ∗ \Pi_{b^{*}b^{*}} is the coupling of two Bernoulli b ∗ b^{*} distributions with maximal correlation upper-bounded by ρ \rho such that h ​ ( Π b ∗ ​ b ∗ ​ ( 0, 0)) h(\Pi_{b^{*}b^{*}}(0,0)) is maximized. Since the maximal correlation of discrete distributions can be computed as the second singular value of a matrix, we have Π b ∗ ​ b ∗ ​ ( 0, 0) = min ⁡ { b ¯ ∗ 2 + b ∗ ​ b ¯ ∗ ​ ρ, 0.5 } \Pi_{b^{*}b^{*}}(0,0)=\min\{\bar{b}^{*2}+b^{*}\bar{b}^{*}\rho,0.5\} and P S ​ T ​ ( b ∗, b ∗) = max ⁡ { a ¯ ∗ 2 − a ∗ ​ a ¯ ∗ ​ ρ, 1 − 2 ​ a ¯ ∗ } P_{ST}(b^{*},b^{*})=\max\{\bar{a}^{*2}-a^{*}\bar{a}^{*}\rho,1-2\bar{a}^{*}\} [Yu23]. Then we can verify that the left side of ( 45) is, in fact, negative for all ρ ∈ ( 0, 1) \rho\in(0,1).

## IV Cardinality Reduction

In this section we remove the max-entropy coupling term in ( 32), and simplify ( 46) to a finite-dimension optimization under certain assumptions (Theorem 12 ahead), which enables numerical evaluation of the bound. As before, let 𝒞 1 \mathcal{C}_{1} be the set of measures P S ​ R P_{SR} on [0, 1] 2 [0,1]^{2} under which S S and R R are i.i.d., and let 𝒞 3 \mathcal{C}_{3} be the closure of the convex hull of 𝒞 1 \mathcal{C}_{1}. We focus on the following optimization:

 | inf P S ​ R 2 ∈ 𝒞 3, 𝔼 ⁡ [S] ≤ c { β ¯ ​ 𝔼 ​ [h ⁡ ( S ¯ ​ T ¯)] + β ​ 𝔼 ​ [h ⁡ ( Π S, R 2 ​ ( 0, 0))] − 𝔼 ⁡ [h ⁡ ( S)] } \displaystyle\inf_{P_{SR_{2}}\in\mathcal{C}_{3},\,\mathbb{E}[S]\leq c}\left\{\bar{\beta}\mathbb{E}[h(\bar{S}\bar{T})]+\beta\mathbb{E}[h(\Pi_{S,R_{2}}(0,0))]-\mathbb{E}[h(S)]\right\} |  | (46) |

where c > 0 c>0, and S S and T T are i.i.d.

###### Theorem 9.

For any conditionally IID protocol Π \Pi as in Definition 2, the infimum in ( 46) is achieved by some P S ​ R 2 P_{SR_{2}} which is a mixture of two i.i.d. distributions, i.e.,

 | P S ​ R 2 ​ ( s, r) = 𝔼 ⁡ [P S | W ​ ( s | W) ​ P S | W ​ ( r | W)] \displaystyle P_{SR_{2}}(s,r)=\mathbb{E}[P_{S|W}(s|W)P_{S|W}(r|W)] |  | (47) |

for some binary random variable W W and conditional distribution P S | W P_{S|W}.

###### Proof.

The fact that the infimum is achievable follows from the weak compactness of measures (Prokhorov theorem). For any c ′ > 0 c^{\prime}>0, the map from 𝒞 3 ∩ { P S ​ R 2: 𝔼 ⁡ [S] = c ′ } \mathcal{C}_{3}\cap\{P_{SR_{2}}\colon\mathbb{E}[S]=c^{\prime}\} to 𝔼 ⁡ [h ⁡ ( S ¯ ​ T ¯)] \mathbb{E}[h(\bar{S}\bar{T})] is concave, as shown in [AHS22], so is its composition with the linear map from P S ​ R 2 P_{SR_{2}} to P S P_{S}. The last two summands in ( 46) are linear in P S ​ R 2 P_{SR_{2}}. Therefore ( 46) is achieved at the extreme points of 𝒞 3 ∩ { P S ​ R 2: 𝔼 ⁡ [S] = c ′ } \mathcal{C}_{3}\cap\{P_{SR_{2}}\colon\mathbb{E}[S]=c^{\prime}\} for some c ′ > 0 c^{\prime}>0.

It remains to show that the extreme points are mixtures of two i.i.d. distributions, from which the theorem follows by Krein-Milman. For any P S ​ R 2 ∈ 𝒞 3 P_{SR_{2}}\in\mathcal{C}_{3} we can write P S ​ R 2 P_{SR_{2}} by ( 47) for some (not necessarily binary) random variable W W. We can assume that W W has finite support, as the general case will then follow by a limiting argument. Then 𝔼 ⁡ [S | W] \mathbb{E}[S|W] is a random variable on ℝ \mathbb{R} with mean equal to c ′ c^{\prime}. The extreme points in the set of probability measures on ℝ \mathbb{R} with mean equal to c ′ c^{\prime} are mixtures of two delta measures with mean equal to c ′ c^{\prime}, Therefore we can express the distribution of 𝔼 ⁡ [S | W] \mathbb{E}[S|W] as a convex combination of mixture of two delta measures, and hence express P S ​ R 2 P_{SR_{2}} as a convex combination of mixtures of two i.i.d. measures with mean equal to c ′ c^{\prime}. This establishes the claim about extreme points and hence the theorem statement. ∎

Theorem 9 implies that it is sufficient to consider

 | P S ​ R 2 ​ ( s, r) = q ​ P 1 ​ ( s) ​ P 1 ​ ( r) + q ¯ ​ P 0 ​ ( s) ​ P 0 ​ ( r) \displaystyle P_{SR_{2}}(s,r)=qP_{1}(s)P_{1}(r)+\bar{q}P_{0}(s)P_{0}(r) |  | (48) |

where q ∈ [0, 1] q\in[0,1] and P 0 P_{0} and P 1 P_{1} are probability measures on [0, 1] [0,1]. Further simplification is possible in some settings. The idea is to use convexity of certain functionals, which in turn relies on the positive semidefiniteness of certain quadratic forms. First, we observe the following about some matrices generated by polynomials.

###### Lemma 10.

Let p ⁡ ( ⋅) p(\cdot) and p 1 ​ ( ⋅, ⋅) p_{1}(\cdot,\cdot) be given polynomials. For positive integer k k, let B k B_{k} be the matrix where the ( i, j) (i,j) -th entry equals the coefficient of the monomial x i ​ y j x^{i}y^{j} in the expansion of p 1 ​ ( x, y) ​ p k ​ ( x) ​ p k ​ ( y) p_{1}(x,y)p^{k}(x)p^{k}(y). Then there exists C > 0 C>0 such that the operator norm of B k B_{k} is upper bounded by C k C^{k} for all k k.

###### Proof.

Suppose that p ⁡ ( x) = ∑ m = 0 D a m ​ x m p(x)=\sum_{m=0}^{D}a_{m}x^{m}, and p k ​ ( x) = ∑ m = 0 D ​ k a m ( k) ​ x m p^{k}(x)=\sum_{m=0}^{Dk}a^{(k)}_{m}x^{m}. Let us focus on the case of p 1 ​ ( ⋅, ⋅) = 1 p_{1}(\cdot,\cdot)=1, as the case of monomial p 1 p_{1} will then follow with exactly the same spectral norm, and then the general p 1 p_{1} case will follow by subadditivity. Then B k B_{k} is a symmetric rank-one matrix, and from the large deviation analysis, the square of its operator norm is

 | ∑ m = 1 D ​ k ( a m ( k)) 2 = exp ⁡ ( 2 ​ k ​ sup P M { 𝔼 ⁡ [log ⁡ ( a M)] + H ⁡ ( P M) } + o ⁡ ( k)) \displaystyle\sum_{m=1}^{Dk}(a^{(k)}_{m})^{2}=\exp\left(2k\sup_{P_{M}}\left\{\mathbb{E}[\log(a_{M})]+H(P_{M})\right\}+o(k)\right) |  | (49) |

where the supremum is over P M P_{M} a distribution on { 0, 1, …, D } \{0,1,\dots,D\}. Therefore the operator norm grows at most exponentially in k k. ∎

Note that if p 1 ​ ( x, y) ​ p k ​ ( x) ​ p k ​ ( y) p_{1}(x,y)p^{k}(x)p^{k}(y) is a symmetric polynomial whose max degree in x x is L L, then Lemma 10 implies that

 | ∫ p 1 ​ ( x, y) ​ p k ​ ( x) ​ p k ​ ( y) ​ γ ​ ( x) ​ γ ​ ( y) ​ 𝑑 x ​ 𝑑 y ≤ C k ​ ( ∑ i = 0 L ∫ x i ​ γ ​ ( x)) 2 \displaystyle\int p_{1}(x,y)p^{k}(x)p^{k}(y)\gamma(x)\gamma(y)dxdy\leq C^{k}(\sum_{i=0}^{L}\int x^{i}\gamma(x))^{2} |  | (50) |

for any γ ⁡ ( ⋅) \gamma(\cdot). We can use this fact to establish the following:

###### Lemma 11.

Fix p ⁡ ( ⋅) p(\cdot) a polynomial satisfying p ⁡ ( 1) = 0 p(1)=0. Consider Π \Pi in Example 5, with f ⁡ ( x) = l ​ x ​ p ​ ( x) f(x)=lxp(x). For sufficiently small l > 0 l>0, the following holds: For any c, d ∈ [0, 1] c,d\in[0,1], the map μ ↦ ∫ h ⁡ ( Π s, r ​ ( 0, 0)) ​ μ ​ ( 𝑑 s) ​ μ ​ ( 𝑑 t) \mu\mapsto\int h(\Pi_{s,r}(0,0))\mu(ds)\mu(dt) restricted to the set of probability measures satisfying

 | 𝔼 μ ​ ( S) \displaystyle\mathbb{E}_{\mu}(S) | = c; \displaystyle=c; |  | (51) |

 | 𝔼 μ ​ [f ​ ( S ¯)] \displaystyle\mathbb{E}_{\mu}[f(\bar{S})] | = d, \displaystyle=d, |  | (52) |

is concave.

###### Proof.

Note that for sufficiently small l l, 0 ≤ f ⁡ ( s ¯) ≤ s ∧ s ¯ 0\leq f(\bar{s})\leq s\wedge\bar{s} is satisfied and so Π \Pi is a well-defined protocol. For notation simplicity, we write x:= s ¯ x:=\bar{s} and y:= t ¯ y:=\bar{t}, and I:= Π s, r ​ ( 0, 0) = x ​ y + f ⁡ ( x) ​ f ​ ( y) I:=\Pi_{s,r}(0,0)=xy+f(x)f(y). The goal can be rephrased as showing − ∫ h ( I) μ ( d x) μ ( d y) ≥ 0 -\int h(I)\mu(dx)\mu(dy)\geq 0 for measures μ \mu on [0, 1] [0,1] satisfying ∫ 𝑑 μ = 0 \int d\mu=0, ∫ x ​ μ ​ ( 𝑑 x) = 0 \int x\mu(dx)=0 and ∫ f ⁡ ( x) ​ μ ​ ( 𝑑 x) = 0 \int f(x)\mu(dx)=0.

Similar to [AHS22], we apply integration by parts twice to obtain

 | − ∫ h ( I) μ ( d x) μ ( d y) \displaystyle-\int h(I)\mu(dx)\mu(dy) | = − ∫ ∂ x ∂ y h ( I) γ ( x) γ ( y) d x d y \displaystyle=-\int\partial_{x}\partial_{y}h(I)\gamma(x)\gamma(y)dxdy |  | (53) |

 |  | = ∫ ( I x ​ y ​ log ⁡ I 1 − I + I x ​ I y I ⁡ ( 1 − I)) ​ γ ​ ( x) ​ γ ​ ( y) ​ 𝑑 x ​ 𝑑 y \displaystyle=\int\left(I_{xy}\log\frac{I}{1-I}+\frac{I_{x}I_{y}}{I(1-I)}\right)\gamma(x)\gamma(y)dxdy |  | (54) |

where γ ⁡ ( x):= μ ⁡ ( [0, x]) \gamma(x):=\mu([0,x]) and I x I_{x} denotes the derivative of I I in x x. We then analyze the terms in ( 54) separately to show the nonnegativity of ( 54).

First,

 | A 1 \displaystyle A_{1} | : = ∫ I x ​ y ​ ( log ⁡ I) ​ γ ​ ( x) ​ γ ​ ( y) \displaystyle:=\int I_{xy}(\log I)\gamma(x)\gamma(y) |  | (55) |

 |  | = ∫ ( 1 + f ′ ​ ( x) ​ f ′ ​ ( y)) ​ log ⁡ ( x ​ y + f ⁡ ( x) ​ f ​ ( y)) ​ γ ​ ( x) ​ γ ​ ( y) \displaystyle=\int(1+f^{\prime}(x)f^{\prime}(y))\log(xy+f(x)f(y))\gamma(x)\gamma(y) |  | (56) |

 |  | = ∫ log ⁡ ( x ​ y) ​ γ ​ ( x) ​ γ ​ ( y) + ∫ f ′ ​ ( x) ​ f ′ ​ ( y) ​ log ⁡ ( x ​ y) ​ γ ​ ( x) ​ γ ​ ( y) \displaystyle=\int\log(xy)\gamma(x)\gamma(y)+\int f^{\prime}(x)f^{\prime}(y)\log(xy)\gamma(x)\gamma(y) |  |

 |  | + ∫ ( 1 + f ′ ( x) f ′ ( y)) log ( 1 + f ⁡ ( x) ​ f ​ ( y) x ​ y) γ ( x) γ ( y). \displaystyle\quad+\int(1+f^{\prime}(x)f^{\prime}(y))\log\left(1+\frac{f(x)f(y)}{xy}\right)\gamma(x)\gamma(y). |  | (57) |

Now ∫ log ( y) γ ( x) γ ( y) = − ∫ log ( y) γ ( y) ∫ d μ = 0 \int\log(y)\gamma(x)\gamma(y)=-\int\log(y)\gamma(y)\int d\mu=0 by integration by parts. Similarly, ∫ f ′ ( x) f ′ ( y) log ( y) γ ( x) γ ( y) = − ∫ f ′ ( y) log ( y) γ ( y) ∫ f ( x) μ ( d x) = 0 \int f^{\prime}(x)f^{\prime}(y)\log(y)\gamma(x)\gamma(y)=-\int f^{\prime}(y)\log(y)\gamma(y)\int f(x)\mu(dx)=0. The third term in ( 57) can be Taylor expanded as

 | ∫ ( 1 + l 2 ​ ( x ​ p ​ ( x)) ′ ​ ( y ​ p ​ ( y)) ′) ​ ∑ k = 1 ∞ ( − 1) k + 1 k ​ l 2 ​ k ​ p k ​ ( x) ​ p k ​ ( y) ​ γ ​ ( x) ​ γ ​ ( y), \displaystyle\int(1+l^{2}(xp(x))^{\prime}(yp(y))^{\prime})\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k}l^{2k}p^{k}(x)p^{k}(y)\gamma(x)\gamma(y), |  | (58) |

which, by Lemma 10, is lower bounded by

 |  | − ∑ k = 1 ∞ l 2 ​ k ∑ m = 0 ( k + 1) ​ D C k ( ∫ x m γ ( x)) 2 \displaystyle\quad-\sum_{k=1}^{\infty}l^{2k}\sum_{m=0}^{(k+1)D}C^{k}\left(\int x^{m}\gamma(x)\right)^{2} |  |

 |  | ≥ − ∑ m = 0 ∞ l 2 ​ C 1 − l 2 ​ C ( ∫ x m γ ( x)) 2 \displaystyle\geq-\sum_{m=0}^{\infty}\frac{l^{2}C}{1-l^{2}C}\left(\int x^{m}\gamma(x)\right)^{2} |  | (59) |

 |  | ≥ − 2 C l 2 ∑ m = 0 ∞ ( ∫ x m γ ( x)) 2 \displaystyle\geq-2Cl^{2}\sum_{m=0}^{\infty}\left(\int x^{m}\gamma(x)\right)^{2} |  | (60) |

for sufficiently small l > 0 l>0 (by which we mean l l is smaller than some positive threshold depending on p ⁡ ( ⋅) p(\cdot)), where D D denotes the degree of p ⁡ ( ⋅) p(\cdot), and C > 0 C>0 depends only on p ⁡ ( ⋅) p(\cdot).

Second,

 | A 2 \displaystyle A_{2} | : = ∫ I x ​ y ​ log ⁡ 1 1 − I ​ γ ​ ( x) ​ γ ​ ( y) \displaystyle:=\int I_{xy}\log\frac{1}{1-I}\gamma(x)\gamma(y) |  | (61) |

 |  | = ∫ ( 1 + l 2 ​ ( x ​ p ​ ( x)) ′ ​ ( y ​ p ​ ( y)) ′) ​ ∑ k = 1 ∞ 1 k ​ ( x ​ y + f ⁡ ( x) ​ f ​ ( y)) k ​ γ ​ ( x) ​ γ ​ ( y) \displaystyle=\int(1+l^{2}(xp(x))^{\prime}(yp(y))^{\prime})\sum_{k=1}^{\infty}\frac{1}{k}(xy+f(x)f(y))^{k}\gamma(x)\gamma(y) |  | (62) |

 |  | = ∑ k = 1 ∞ ∫ F k ​ ( x) ​ F k ​ ( y) ​ γ ​ ( x) ​ γ ​ ( y) ≥ 0 \displaystyle=\sum_{k=1}^{\infty}\int F_{k}(x)F_{k}(y)\gamma(x)\gamma(y)\geq 0 |  | (63) |

where F k ​ ( ⋅) F_{k}(\cdot) are certain polynomials arising from applying binomial expansion to ( 62).

Third,

 | A 3 \displaystyle A_{3} | : = ∫ I x ​ I y I ⁡ ( 1 − I) ​ γ ​ ( x) ​ γ ​ ( y) \displaystyle:=\int\frac{I_{x}I_{y}}{I(1-I)}\gamma(x)\gamma(y) |  |

 |  | = ∫ I x ​ I y I ​ γ ​ ( x) ​ γ ​ ( y) + ∫ I x ​ I y ​ ∑ k = 0 ∞ I k ​ γ ​ ( x) ​ γ ​ ( y). \displaystyle=\int\frac{I_{x}I_{y}}{I}\gamma(x)\gamma(y)+\int I_{x}I_{y}\sum_{k=0}^{\infty}I^{k}\gamma(x)\gamma(y). |  | (64) |

Denote by A 31 A_{31} and A 32 A_{32} the two integrals in ( 64), and define q ⁡ ( x):= ( x ​ p ​ ( x)) ′ q(x):=(xp(x))^{\prime}. We have

 | A 31 \displaystyle A_{31} | = ∫ ( 1 + l 2 ​ q ​ ( x) ​ p ​ ( y)) ​ ( 1 + l 2 ​ p ​ ( x) ​ q ​ ( y)) 1 + l 2 ​ p ​ ( x) ​ p ​ ( y) ​ γ ​ ( x) ​ γ ​ ( y) \displaystyle=\int\frac{(1+l^{2}q(x)p(y))(1+l^{2}p(x)q(y))}{1+l^{2}p(x)p(y)}\gamma(x)\gamma(y) |  | (65) |

 |  | = ∫ γ ⁡ ( x) ​ γ ​ ( y) \displaystyle=\int\gamma(x)\gamma(y) |  |

 |  | + ∫ ( l 2 q ( x) p ( y) + l 2 p ( x) q ( y) + l 4 q ( x) q ( y) p ( x) p ( y)) γ ( x) γ ( y) \displaystyle+\int(l^{2}q(x)p(y)+l^{2}p(x)q(y)+l^{4}q(x)q(y)p(x)p(y))\gamma(x)\gamma(y) |  |

 |  | + ∫ ( 1 + l 2 q ( x) p ( y)) ( 1 + l 2 p ( x) q ( y)) ∑ k = 1 ∞ ( − 1) k l 2 ​ k p k ( x) p k ( y) γ ( x) γ ( y) \displaystyle+\int(1+l^{2}q(x)p(y))(1+l^{2}p(x)q(y))\sum_{k=1}^{\infty}(-1)^{k}l^{2k}p^{k}(x)p^{k}(y)\gamma(x)\gamma(y) |  | (66) |

Denote the 3 integrals in ( 66) by A 311 A_{311}, A 312 A_{312} and A 313 A_{313}, respectively. We have

 | A 312 ≥ − l 2 C ∑ m = 0 2 ​ D + 1 ( ∫ x m γ ( x)) 2 \displaystyle A_{312}\geq-l^{2}C\sum_{m=0}^{2D+1}(\int x^{m}\gamma(x))^{2} |  | (67) |

and similarly to ( 62),

 | A 313 ≥ − 2 l 2 C ∑ m = 0 ∞ ( ∫ x m γ ( x)) 2 \displaystyle A_{313}\geq-2l^{2}C\sum_{m=0}^{\infty}\left(\int x^{m}\gamma(x)\right)^{2} |  | (68) |

for some C > 0 C>0 depending on p ⁡ ( ⋅) p(\cdot). Next,

 | A 32 \displaystyle A_{32} | = ∫ x ​ y ​ ( 1 + l 2 ​ q ​ ( x) ​ p ​ ( y)) ​ ( 1 + l 2 ​ p ​ ( x) ​ q ​ ( y)) \displaystyle=\int xy(1+l^{2}q(x)p(y))(1+l^{2}p(x)q(y)) |  |

 |  | ⋅ ∑ k = 0 ∞ x k ​ y k ​ ( 1 + l 2 ​ p ​ ( x) ​ p ​ ( y)) k ​ γ ​ ( x) ​ γ ​ ( y) \displaystyle\cdot\sum_{k=0}^{\infty}x^{k}y^{k}(1+l^{2}p(x)p(y))^{k}\gamma(x)\gamma(y) |  | (69) |

 |  | = ∫ ∑ k = 0 ∞ x k + 1 ​ y k + 1 ​ ( 1 + l 2 ​ p ​ ( x) ​ p ​ ( y)) k ​ γ ​ ( x) ​ γ ​ ( y) \displaystyle=\int\sum_{k=0}^{\infty}x^{k+1}y^{k+1}(1+l^{2}p(x)p(y))^{k}\gamma(x)\gamma(y) |  |

 |  | + ∫ ( l 2 p 1 ( x, y) + l 4 p 2 ( x, y)) ∑ k = 0 ∞ x k + 1 y k + 1 ( 1 + l 2 p ( x) p ( y)) k γ ( x) γ ( y) \displaystyle+\int(l^{2}p_{1}(x,y)+l^{4}p_{2}(x,y))\sum_{k=0}^{\infty}x^{k+1}y^{k+1}(1+l^{2}p(x)p(y))^{k}\gamma(x)\gamma(y) |  | (70) |

where p 1 p_{1} and p 2 p_{2} are symmetric polynomials whose definitions can be seen from the expansion of terms. The degree in x x of p 1 p_{1} and p 2 p_{2} are D D and 2 ​ D 2D respectively. Let A 321 A_{321} and A 322 A_{322} be the two integrals in ( 70). There exists a 0, …, a 2 ​ D > 0 a_{0},\dots,a_{2D}>0 such that

 | − ∫ ( p 1 ( x, y) + l 2 p 2 ( x, y)) γ ( x) γ ( y) ≤ ∑ m = 0 2 ​ D a m ( ∫ x m γ ( x)) 2 \displaystyle-\int(p_{1}(x,y)+l^{2}p_{2}(x,y))\gamma(x)\gamma(y)\leq\sum_{m=0}^{2D}a_{m}(\int x^{m}\gamma(x))^{2} |  | (71) |

whenever l < 1 l<1. Recall the Schur product theorem about the positive semidefiniteness of the elementwise product of PSD matrices; it follows that

 | − A 322 ≤ l 2 ​ ∫ ∑ m = 0 2 ​ D a m ​ x m ​ y m ​ ∑ k = 0 ∞ x k + 1 ​ y k + 1 ​ ( 1 + l 2 ​ p ​ ( x) ​ p ​ ( y)) k ​ γ ​ ( x) ​ γ ​ ( y). \displaystyle-A_{322}\leq l^{2}\int\sum_{m=0}^{2D}a_{m}x^{m}y^{m}\sum_{k=0}^{\infty}x^{k+1}y^{k+1}(1+l^{2}p(x)p(y))^{k}\gamma(x)\gamma(y). |  | (72) |

We can expand ( 1 + l 2 ​ p ​ ( x) ​ p ​ ( y)) k (1+l^{2}p(x)p(y))^{k} in ( 72); for each m ∈ { 0, …, 2 ​ D } m\in\{0,\dots,2D\}, k ≥ 0 k\geq 0, and n ∈ { 0, …, k } n\in\{0,\dots,k\}, the coefficient for ∫ x m + k + 1 ​ y m + k + 1 ​ p n ​ ( x) ​ p n ​ ( y) ​ γ ​ ( x) ​ γ ​ ( y) \int x^{m+k+1}y^{m+k+1}p^{n}(x)p^{n}(y)\gamma(x)\gamma(y) in ( 72) is l 2 ​ n + 2 ​ a m ​ ( k n) l^{2n+2}a_{m}{{k}\choose{n}}. On the other hand, the coefficient for the same term in A 321 A_{321} is l 2 ​ n ​ ( m + k n) ≥ l 2 ​ n ​ ( k n) l^{2n}{{m+k}\choose{n}}\geq l^{2n}{k\choose{n}}. This shows that − A 322 ≤ l 2 ​ max ⁡ { a 1, …, a 2 ​ D } ​ A 321 -A_{322}\leq l^{2}\max\{a_{1},\dots,a_{2D}\}A_{321} and hence

 | A 32 ≥ 1 2 ​ A 321 ≥ 1 2 ​ ∫ ∑ k = 0 ∞ x k + 1 ​ y k + 1 ​ γ ​ ( x) ​ γ ​ ( y) \displaystyle A_{32}\geq\frac{1}{2}A_{321}\geq\frac{1}{2}\int\sum_{k=0}^{\infty}x^{k+1}y^{k+1}\gamma(x)\gamma(y) |  | (73) |

for l l sufficiently small. Returning to ( 66), we have

 | A 3 \displaystyle A_{3} | = A 31 + A 32 \displaystyle=A_{31}+A_{32} |  | (74) |

 |  | ≥ 1 2 ​ ( 1 − C ′ ​ l 2) ​ ∑ k = 0 ∞ ( ∫ x k ​ γ ​ ( x)) 2 \displaystyle\geq\frac{1}{2}(1-C^{\prime}l^{2})\sum_{k=0}^{\infty}(\int x^{k}\gamma(x))^{2} |  | (75) |

 |  | ≥ 1 4 ​ ∑ k = 0 ∞ ( ∫ x k ​ γ ​ ( x)) 2 \displaystyle\geq\frac{1}{4}\sum_{k=0}^{\infty}(\int x^{k}\gamma(x))^{2} |  | (76) |

for l l sufficiently small and where C ′ > 0 C^{\prime}>0 is some constant. And so A 1 + A 2 + A 3 ≥ 1 8 ​ ∑ k = 0 ∞ ( ∫ x k ​ γ ​ ( x)) 2 A_{1}+A_{2}+A_{3}\geq\frac{1}{8}\sum_{k=0}^{\infty}(\int x^{k}\gamma(x))^{2} for l l sufficiently small, establishing the desired nonnegativity of ( 54). ∎

Now we can state the main result of this section:

###### Theorem 12.

Fix p ⁡ ( ⋅) p(\cdot) a polynomial satisfying p ⁡ ( 1) = 0 p(1)=0. Consider Π \Pi in Example 5, with f ⁡ ( x) = l ​ x ​ p ​ ( x) f(x)=lxp(x). Let c, β, q c,\beta,q be fixed, and consider the optimization of ( 46) over P 0 P_{0} and P 1 P_{1} in ( 48). For sufficiently small l > 0 l>0, the optimal value can be achieved by ( P 0, P 1) (P_{0},P_{1}) of the form

 | P 0 \displaystyle P_{0} | = a 1 ​ δ b 0 + a 2 ​ δ b 2 + a 3 ​ δ b 4; \displaystyle=a_{1}\delta_{b_{0}}+a_{2}\delta_{b_{2}}+a_{3}\delta_{b_{4}}; |  | (77) |

 | P 1 \displaystyle P_{1} | = a 1 ​ δ b 1 + a 2 ​ δ b 3 + a 3 ​ δ b 5, \displaystyle=a_{1}\delta_{b_{1}}+a_{2}\delta_{b_{3}}+a_{3}\delta_{b_{5}}, |  | (78) |

where b 0, …, b 5 ∈ [0, 1] b_{0},\dots,b_{5}\in[0,1], and ( a 1, a 2, a 3) (a_{1},a_{2},a_{3}) is on the probability simplex.

###### Proof.

Pick arbitrary c ′ ∈ [0, c] c^{\prime}\in[0,c] and d ∈ [0, 1] d\in[0,1], and consider the map from ( P 0, P 1) (P_{0},P_{1}) to the objective function in ( 46), restricted to the ( P 0, P 1) (P_{0},P_{1}) satisfying

 | q ​ ∫ x ​ P 1 ​ ( 𝑑 x) + q ¯ ​ ∫ x ​ P 0 ​ ( 𝑑 x) \displaystyle q\int xP_{1}(dx)+\bar{q}\int xP_{0}(dx) | = 1 − c ′; \displaystyle=1-c^{\prime}; |  | (79) |

 | q ​ ∫ f ⁡ ( x) ​ P 1 ​ ( 𝑑 x) + q ¯ ​ ∫ f ⁡ ( x) ​ P 0 ​ ( 𝑑 x) \displaystyle q\int f(x)P_{1}(dx)+\bar{q}\int f(x)P_{0}(dx) | = d. \displaystyle=d. |  | (80) |

From Lemma 11, we see that this is a is a concave functional on a convex set, hence the infimum is achieved at extremal points (Krein-Milman theorem). For the set of ( P 0, P 1) (P_{0},P_{1}) where P 0 P_{0} and P 1 P_{1} are from the set of probability measures, the extremal points are of the form ( δ b 0, δ b 1) (\delta_{b_{0}},\delta_{b_{1}}). If we add the two linear constraints in ( 79)-( 80), the extremal points in this restricted convex set are convex combinations of three such delta measure pairs (using an argument similar to the proof of ( 9)), which is the claim of the theorem.

An alternative argument for the last part is as follows: for any ( P 0, P 1) = ∑ k = 1 K a k ​ ( δ b k, δ b k ′) (P_{0},P_{1})=\sum_{k=1}^{K}a_{k}(\delta_{b_{k}},\delta_{b^{\prime}_{k}}), a k > 0 a_{k}>0, ∑ k K a k = 1 \sum_{k}^{K}a_{k}=1 with K ≥ 4 K\geq 4, we consider variations of a 1, …, a 4 a_{1},\dots,a_{4} while retaining ∑ k = 1 4 a k \sum_{k=1}^{4}a_{k}, ∑ k = 1 4 a k ​ ( q ¯ ​ b k + q ​ b k ′) \sum_{k=1}^{4}a_{k}(\bar{q}b_{k}+qb^{\prime}_{k}), and the values of a 5, …, a K a_{5},\dots,a_{K}. This yields a 2-dimensional polygon. Lemma 11 implies that the quadratic form ∫ h ⁡ ( Π s, r ​ ( 0, 0)) ​ μ ​ ( 𝑑 s) ​ μ ​ ( 𝑑 t) \int h(\Pi_{s,r}(0,0))\mu(ds)\mu(dt) restricted to ∫ μ = 0 \int\mu=0 and ∫ s ​ μ ​ ( 𝑑 s) = 0 \int s\mu(ds)=0 has positive signature at most 1, so on this 2-dimensional polygon there must be a line along which we can move q 1, …, q 4 q_{1},\dots,q_{4} so that ∫ h ⁡ ( Π s, r ​ ( 0, 0)) ​ μ ​ ( 𝑑 s) ​ μ ​ ( 𝑑 t) \int h(\Pi_{s,r}(0,0))\mu(ds)\mu(dt) is a quadratic function with nonpositive leading coefficient, where we set μ = q ¯ ​ P 0 + q ​ P 1 \mu=\bar{q}P_{0}+qP_{1}. Thus we can move along this line until hitting the boundary of the polygon without increasing the objective value, hence showing K K can be reduced if K ≥ 4 K\geq 4. For ( P 0, P 1) (P_{0},P_{1}) not finitely supported, we can use approximation argument and the fact that the weak limit of K K -supported distributions is also K K supported; see similar argument in [AHS22, Lemma 6]. ∎

## V Numerical Evaluation

In this section we focus on a basic instance of Example 5, f ⁡ ( x) = x ​ x ¯ f(x)=x\bar{x}, numerically evaluate the largest c c for ( 46) to be nonnegative, and discuss its implication for the union-closed sets conjecture (Theorem 13).

### V-A Positive-Semidefiniteness

Recall that Theorem 12 reduces the optimization to a 9-dimensional one involving ( a 1, a 2, q, b 0, b 2, b 4, b 1, b 3, b 5) (a_{1},a_{2},q,b_{0},b_{2},b_{4},b_{1},b_{3},b_{5}), where q q denotes the weight for the P 1 P_{1} component of the mixture. Theorem 12 is based on Lemma 11, which states that the quadratic form μ ↦ − ∫ h ( Π s, r ( 0, 0)) μ ( d s) μ ( d t) \mu\mapsto-\int h(\Pi_{s,r}(0,0))\mu(ds)\mu(dt) is positive semidefinite in the codimension-2 subspace specified by ( 51)-( 52), if f ⁡ ( x) = l ​ x ​ p ​ ( x) f(x)=lxp(x), l l is sufficiently small, and p p is a polynomial with p ⁡ ( 1) = 0 p(1)=0. For l = 1 l=1, we verify the positive semidefiniteness of this quadratic form by numerically computing the eigenvalues of the matrix [− h ⁡ ( Π s, r ​ ( 0, 0))] s, t ∈ 𝒢 [-h(\Pi_{s,r}(0,0))]_{s,t\in\mathcal{G}} on the codimension-2 subspace, where 𝒢 \mathcal{G} is a grid on [0, 1] [0,1] with separation 0.0004. Our Matlab code can be found in [https://jingbol.web.illinois.edu/frankl3.m][1]. The min eigenvalue is − 2.3685 × 10 − 14 -2.3685\times 10^{-14}, which is negligible considering the numerical errors for computation of large matrices. For comparison, the numerical precision of Matlab is 2.22 × 10 − 16 2.22\times 10^{-16}; for the case of i.i.d. coupling where Π s, t ​ ( 0.0) = s ¯ ​ t ¯ \Pi_{s,t}(0.0)=\bar{s}\bar{t}, the positive-semidefiniteness was rigorously shown in [AHS22], and the numerically evaluated minimum eigenvalue is − 2.4206 × 10 − 14 -2.4206\times 10^{-14}.

As another approach of verifying positive semidefiniteness, consider x = s ¯ x=\bar{s}, y = t ¯ y=\bar{t} and I:= Π s, t ​ ( 0, 0) = x ​ y ​ ( 1 + x ¯ ​ y ¯) I:=\Pi_{s,t}(0,0)=xy(1+\bar{x}\bar{y}). For measures μ \mu on [0, 1] [0,1] satisfying ∫ μ ⁡ ( 𝑑 x) = 0 \int\mu(dx)=0, ∫ x ​ μ ​ ( 𝑑 x) = 0 \int x\mu(dx)=0, ∫ x 2 ​ μ ​ ( 𝑑 x) = 0 \int x^{2}\mu(dx)=0, we have

 | − ∫ h ( I) μ ( d x) μ ( d y) \displaystyle-\int h(I)\mu(dx)\mu(dy) | = ∫ x ​ y ​ ( 1 + x ¯ ​ y ¯) ​ log ⁡ ( 1 − x + y − x ​ y 2) ​ μ ​ ( 𝑑 x) ​ μ ​ ( 𝑑 y) \displaystyle=\int xy(1+\bar{x}\bar{y})\log\left(1-\frac{x+y-xy}{2}\right)\mu(dx)\mu(dy) |  |

 |  | + ∫ ( 1 − I) log ( 1 − I) μ ( d x) μ ( d y) \displaystyle+\int(1-I)\log(1-I)\mu(dx)\mu(dy) |  | (81) |

where we used ∫ x ​ y ​ ( 1 + x ¯ ​ y ¯) ​ log ⁡ ( 2 ​ x ​ y) ​ μ ​ ( 𝑑 x) ​ μ ​ ( 𝑑 y) = 0 \int xy(1+\bar{x}\bar{y})\log(2xy)\mu(dx)\mu(dy)=0 which follows from the assumptions on μ \mu. Now if the integrand in ( 81) can be expanded as ∑ m, n ∈ { 0, 1, … } O m ​ n ​ x m ​ y n \sum_{m,n\in\{0,1,\dots\}}O_{mn}x^{m}y^{n} then the required condition is that [O m ​ n] m, n ≥ 3 [O_{mn}]_{m,n\geq 3} is a positive semidefinite matrix. We can calculate that the coefficient of x m ​ y n x^{m}y^{n} in log ⁡ ( 1 − x + y − x ​ y 2) \log\left(1-\frac{x+y-xy}{2}\right) is

 | − ∑ k = m ∨ n m + n 1 k ​ 2 k ( − 1) m + n − k ( k k − n) ( n k − m) \displaystyle-\sum_{k=m\vee n}^{m+n}\frac{1}{k2^{k}}(-1)^{m+n-k}{k\choose k-n}{n\choose k-m} |  | (82) |

and in log ⁡ ( 1 − I) \log(1-I) is

 | ( − 1) m + n + 1 ​ ∑ k = ⌈ m ∨ n 2 ⌉ m ∧ n 1 k ​ ∑ d = ( m + n − 3 ​ k) ∨ 0 m ∧ n − k ( k d + 3 ​ k − m − n) ​ ( m + n − d − 2 ​ k m − k − d) ​ ( n − k d), \displaystyle(-1)^{m+n+1}\sum_{k=\lceil\frac{m\vee n}{2}\rceil}^{m\wedge n}\frac{1}{k}\sum_{d=(m+n-3k)\vee 0}^{m\wedge n-k}{k\choose d+3k-m-n}{m+n-d-2k\choose m-k-d}{n-k\choose d}, |  | (83) |

from which we easily obtain the expression of O O. We numerically verified that [O] 2 ≤ m, n ≤ L [O]_{2\leq m,n\leq L} is positive semidefinite for L = 29 L=29. For L ≥ 30 L\geq 30, the combinatorial numbers are not computed exactly (keeping only 15 digits), but we checked the numerical value of the minimum eigenvalue for up to L = 90 L=90, all confirming the positive semidefinite hypothesis. (Code can be found in [https://jingbol.web.illinois.edu/frankl7.m][2])

### V-B 9-Dimensional Optimization

Under the positive semidefiniteness hypothesis (Section V-A), it is sufficient to consider distribution of the form ( 77)-( 78). We can certify that c > 0 c>0 is a lower bound for the union-closed sets conjecture if for some β ∈ ( 0, 1) \beta\in(0,1) the following 9-dimensional optimization has optimal value no less than 1:

 | minimize β ¯ ​ 𝔼 ( q ¯ ​ P 0 + q ​ P 1) ⊗ 2 ​ [h ⁡ ( X ​ Y)] + β ​ 𝔼 q ¯ ​ P 0 ⊗ 2 + q ​ P 1 ⊗ 2 ​ [h ⁡ ( X ​ Y + X ​ Y ​ X ¯ ​ Y ¯)] 𝔼 q ¯ ​ P 0 + q ​ P 1 ​ [h ​ ( X)] \displaystyle\textrm{minimize }\quad\frac{\bar{\beta}\mathbb{E}_{(\bar{q}P_{0}+qP_{1})^{\otimes 2}}[h(XY)]+\beta\mathbb{E}_{\bar{q}P_{0}^{\otimes 2}+qP_{1}^{\otimes 2}}[h(XY+XY\bar{X}\bar{Y})]}{\mathbb{E}_{\bar{q}P_{0}+qP_{1}}[h(X)]} |  | (84) |

 | subject to: q ¯ ( a 1 b 0 + a 2 b 2 + a 3 b 4) + q ( a 1 b 1 + a 2 b 3 + a 3 b 5) \displaystyle\textrm{ subject to: }\quad\bar{q}(a_{1}b_{0}+a_{2}b_{2}+a_{3}b_{4})+q(a_{1}b_{1}+a_{2}b_{3}+a_{3}b_{5}) | ≥ 1 − c; \displaystyle\geq 1-c; |  | (85) |

 | 0 ≤ a 1, a 2, q, b 0, b 1, …, b 5 \displaystyle 0\leq a_{1},a_{2},q,b_{0},b_{1},\dots,b_{5} | ≤ 1; \displaystyle\leq 1; |  | (86) |

 | a 1 + a 2 \displaystyle a_{1}+a_{2} | ≤ 1. \displaystyle\leq 1. |  | (87) |

We used various algorithms (interior-point, sqp, active-set) from Matlab optimization package to solve constrained optimization with about 10 5 10^{5} different random initializations (code can be found in [https://jingbol.web.illinois.edu/frankl5.m][3]). The percentage of different local optimizers found changes with the choice of solvers. One common local minimum found was simply a one-point mass, but the best local minimum found, which we conjecture to be global, is the following (up to symmetries):

 | q \displaystyle q | = 0; \displaystyle=0; |  | (88) |

 | P 0 \displaystyle P_{0} | = p ∗ ​ δ x ∗ + p ¯ ∗ ​ δ 0, \displaystyle=p^{*}\delta_{x^{*}}+\bar{p}^{*}\delta_{0}, |  | (89) |

where p ∗ p^{*} and x ∗ x^{*} are defined by

 | x ∗ 2 + x ∗ 2 ​ ( 1 + x ¯ ∗ 2) \displaystyle x^{*2}+x^{*2}(1+\bar{x}^{*2}) | = 1; \displaystyle=1; |  | (90) |

 | p ∗ 2 h ( x 2 ∗) − p ∗ h ( x ∗) \displaystyle p^{*2}h(x^{2*})-p^{*}h(x^{*}) | = 0. \displaystyle=0. |  | (91) |

Define c ′:= 1 − p ∗ ​ x ∗ c^{\prime}:=1-p^{*}x^{*}. The optimal value of β \beta should satisfy

 | d ⁡ ( β ¯ ​ p 2 ​ h ​ ( x 2) + β ​ h ​ ( p 2 ​ ( 1 + p ¯ 2)) − p ​ h ​ ( x)) | p = p ∗, x = x ∗ \displaystyle d(\bar{\beta}p^{2}h(x^{2})+\beta h(p^{2}(1+\bar{p}^{2}))-ph(x))|_{p=p^{*},x=x^{*}} | = 0; \displaystyle=0; |  | (92) |

 | d ⁡ ( p ​ x) | p = p ∗, x = x ∗ \displaystyle d(px)|_{p=p^{*},x=x^{*}} | = 0, \displaystyle=0, |  | (93) |

where the differentials are in x x and p p, and we can solve d ​ p d ​ x \frac{dp}{dx} and β \beta from the two equations to obtain expression of the optimal β ∗ \beta^{*} in terms of x ∗ x^{*} and p ∗ p^{*} (omitted here). The numerical values are

 | p ∗ \displaystyle p^{*} | ≈ 0.893604513905457; \displaystyle\approx 0.893604513905457; |  | (94) |

 | x ∗ \displaystyle x^{*} | ≈ 0.690787593924988; \displaystyle\approx 0.690787593924988; |  | (95) |

 | c ′ \displaystyle c^{\prime} | ≈ 0.382709087918741; \displaystyle\approx 0.382709087918741; |  | (96) |

 | β ∗ \displaystyle\beta^{*} | ≈ 0.100052559862974. \displaystyle\approx 0.100052559862974. |  | (97) |

Our conclusion is the following:

###### Theorem 13.

Under the positive-semidefiniteness hypothesis in Section V-A and the hypothesis of the global minimizer structure in Section V-B, the constant in the union-closed sets conjecture can be improved to c ′ c^{\prime} in ( 96).

## References

- [AHS22] Ryan Alweiss, Brice Huang, and Mark Sellke. Improved lower bound for the union-closed sets conjecture. arXiv preprint arXiv:2211.11731, 2022.
- [AJN22] Venkat Anantharam, Varun Jog, and Chandra Nair. Unifying the brascamp-lieb inequality and the entropy power inequality. IEEE Transactions on Information Theory, 68(12):7665–7684, 2022.
- [BS15] Henning Bruhn and Oliver Schaudt. The journey of the union-closed sets conjecture. Graphs and Combinatorics, 31:2043–2074, 2015.
- [Cam22] Stijn Cambie. Better bounds for the union-closed sets conjecture using the entropy approach. arXiv preprint arXiv:2212.12500, 2022.
- [CL22] Zachary Chase and Shachar Lovett. Approximate union closed conjecture. arXiv preprint arXiv:2211.11689, 2022.
- [Gil22] Justin Gilmer. A constant lower bound for the union-closed sets conjecture. arXiv preprint arXiv:2211.09055, 2022.
- [Kni94] Emanuel Knill. Graph generated union-closed families of sets. arXiv preprint math/9409215, 1994.
- [LCCV17] Jingbo Liu, Thomas A Courtade, Paul Cuff, and Sergio Verdu. Information-theoretic perspectives on Brascamp-Lieb inequality and its reverse. arXiv preprint arXiv:1702.06260, 2017.
- [LCCV18] Jingbo Liu, Thomas A Courtade, Paul W Cuff, and Sergio Verdú. A forward-reverse Brascamp-Lieb inequality: Entropic duality and Gaussian optimality. Entropy, 20(6):418, 2018.
- [Saw22] Will Sawin. An improved lower bound for the union-closed set conjecture. arXiv preprint arXiv:2211.11504, 2022.
- [Wój99] Piotr Wójcik. Union-closed families of sets. Discrete Mathematics, 199(1-3):173–182, 1999.
- [Yu23] Lei Yu. Dimension-free bounds for the union-closed sets conjecture. Entropy, 25(5):767, 2023.

[◄][4][image: ar5iv homepage] [5]
[Feeling lucky?][6] [7]
[Conversion report][8]
[Report an issue][9]
[View original on arXiv][10] [►][11]


## Links

[1]: https://jingbol.web.illinois.edu/frankl3.m
[2]: https://jingbol.web.illinois.edu/frankl7.m
[3]: https://jingbol.web.illinois.edu/frankl5.m
[4]: /html/2306.08823
[5]: /
[6]: /feeling_lucky
[7]: /land_of_honey_and_milk
[8]: /log/2306.08824
[9]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2306.08824
[10]: https://arxiv.org/pdf/2306.08824
[11]: /html/2306.08826
