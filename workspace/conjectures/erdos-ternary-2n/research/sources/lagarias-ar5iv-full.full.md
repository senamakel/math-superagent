<!-- source: https://ar5iv.labs.arxiv.org/html/math/0512006 | converted from HTML -->

[math/0512006] 1Introduction

Ternary Expansions of Powers of 2 2

Jeffrey C. Lagarias 1 1 1 MSC Classification (2000): 11A63 (Primary), 11K16, 11K41, 26A18, 37A45 (Secondary)

Dept. of Mathematics

University of Michigan

Ann Arbor, MI 48109-1109

(To Mel Nathanson on his 60-th birthday)

(July 11, 2008 )

ABSTRACT

P. Erdős asked how frequently does 2 n 2^{n} have a ternary expansion that omits the digit 2 2. He conjectured that this holds only for finitely many values of n n. We generalize this question to consider iterates of two discrete dynamical systems. The first considers truncated ternary expansions of real sequences x n ​ ( λ) = ⌊ λ ​ 2 n ⌋ x_{n}(\lambda)=\lfloor\lambda 2^{n}\rfloor, where λ > 0 \lambda>0 is a real number, along with its untruncated version, while the second considers 3 3 -adic expansions of sequences y n ​ ( λ) = λ ​ 2 n y_{n}(\lambda)=\lambda 2^{n}, where λ \lambda is a 3 3 -adic integer. We show in both cases that the set of initial values having infinitely many iterates that omit the digit 2 2 is small in a suitable sense. For each nonzero initial value we obtain an asymptotic upper bound as k → ∞ k\to\infty on the the number of the first k k iterates that omit the digit 2 2. We also study auxiliary problems concerning the Hausdorff dimension of intersections of multiplicative translates of 3 3 -adic Cantor sets.

## 1 Introduction

P. Erdős [4] asked the question of when the ternary expansion of 2 n 2^{n} omits the digit 2 2. This happens for 2 0 = ( 1) 3, 2^{0}=(1)_{3}, 2 2 = 4 = ( 11) 3 2^{2}=4=(11)_{3} and 2 8 = 256 = ( 100111) 3 2^{8}=256=(100111)_{3}. He conjectured that it does not happen for all n ≥ 9 n\geq 9, and commented that: “As far as I can see, there is no method at our disposal to attack this conjecture.” This question was initially studied by Gupta [12] who found by a sieving procedure that there are no other solutions for n < 4374 n<4374. In 1980 Narkiewicz [18] showed that the number

 | N 1 ​ ( X):= #⁡ { n ≤ X: the ternary expansion ​ ( 2 n) 3 ​ omits the digit ​ 2 }. N_{1}(X):=\#\{n\leq X:~\mbox{the~ ternary ~expansion}~(2^{n})_{3}~\mbox{omits~the~digit}~2\}. |  |

has N 1 ​ ( X) ≤ 1.62 ​ X α 0 N_{1}(X)\leq 1.62X^{\alpha_{0}} with α 0 = log 3 ⁡ 2 ≈ 0.63092 \alpha_{0}=\log_{3}2\approx 0.63092. The Erdős question remains open and has appeared in several problem lists, e.g. Erdős and Graham [5] and Guy [13, Problem B33]. In this paper we call the ”Conjecture of Erdős” the weaker assertion that there are only finitely many exponents n n such that the ternary expansion ( 2 n) 3 (2^{n})_{3} of 2 n 2^{n} omits the digit 2 2.

This paper considers analogues of the conjecture of Erdős for iterates of two discrete dynamical systems, one acting on the real numbers and the other acting on the 3 3 -adic integers, with an additional degree of freedom given by a parameter λ \lambda specifying the initial condition. In both dynamical systems the parameter value λ = 1 \lambda=1 recovers the original sequence { 2 n: n ≥ 0 } \{2^{n}:n\geq 0\} of Erdős as a forward orbit of the dynamics.

The first dynamical system is y ↦ 2 ​ y y\mapsto 2y acting on the real numbers, which is a homeomorphism of ℝ {\mathbb{R}} that is an expanding map. It produces a sequence of iterates y n = 2 n ​ y 0 y_{n}=2^{n}y_{0} starting from y 0 = λ y_{0}=\lambda. The real dynamical system concerns the iterates y n y_{n}. We also consider an associated dynamical system which gives integers, by applying the floor operator, obtaining the sequence x n = ⌊ y n ⌋ x_{n}=\lfloor y_{n}\rfloor; that is,

 | x n = x n ​ ( λ):= ⌊ λ ​ 2 n ⌋, for ​ n ≥ 0. x_{n}=x_{n}(\lambda):=\lfloor\lambda 2^{n}\rfloor,~~~~~\mbox{for}~~n\geq 0. |  | (1.1) |

We call this the truncated real dynamical system. Strictly speaking the truncated real dynamical system has forward orbits involving two variables O + ​ ( λ):= { ( y n ​ ( λ), x n ​ ( λ)): n ≥ 0 } O^{+}(\lambda):=\{(y_{n}(\lambda),x_{n}(\lambda)):n\geq 0\}, with { y n ​ ( λ) } \{y_{n}(\lambda)\} driving the dynamics. However the expanding nature of the map y ↦ 2 ​ y y\mapsto 2y implies that the integer sequence { x n ​ ( λ): n ≥ 0 } \{x_{n}(\lambda):n\geq 0\} contains enough information to uniquely determine the initial condition λ \lambda of the iteration; here we consider the ternary expansions of the x n ​ ( λ) x_{n}(\lambda).

The second dynamical system is y ↦ 2 ​ y y\mapsto 2y acting on the 3 3 -adic integers ℤ 3 {\mathbb{Z}}_{3}, which is a 3-adic measure-preserving homeomorphism of ℤ 3 {\mathbb{Z}}_{3}. It produces a sequence of iterates y n = 2 n ​ y 0 y_{n}=2^{n}y_{0} starting from the initial condition y 0 = λ y_{0}=\lambda. We write

 | y n = y n ​ ( λ) = λ ​ 2 n, for ​ n ≥ 0, y_{n}=y_{n}(\lambda)=\lambda 2^{n},~~~~~\mbox{for}~~n\geq 0, |  | (1.2) |

In this case we study membership of values y n ​ ( λ) y_{n}(\lambda) in the subset Σ 3, 2 ¯ \Sigma_{3,\bar{2}} of all 3 3 -adic integers whose 3 3 -adic expansion omits the digit 2 2; this is the multiplicative translate 1 2 ​ Σ 3, 1 ¯ \frac{1}{2}\Sigma_{3,\bar{1}} of the 3 3 -adic analogue Σ 3, 1 ¯ \Sigma_{3,\bar{1}} of the classical ”middle-third” Cantor set.

In the real number case dynamical systems of a related nature have been studied by several authors. Flatto, Lagarias and Pollington [8] introduced a parameter λ \lambda in similar questions concering the fractional parts of the sequences { { λ ​ ξ n } } \{\{\lambda\xi^{n}\}\}, for fixed ξ > 1 \xi>1, with the aim of proving results for the parameter value λ = 1 \lambda=1 by proving universal results valid for all parameter values λ > 0 \lambda>0. Recently Dubickas and Novickas [3] considered the prime or compositeness properties of integers occurring in truncated recurrence sequences, including ⌊ λ ​ 2 n ⌋ \lfloor\lambda 2^{n}\rfloor as a particularly simple case. Dubickas [2] further extends both these results to certain λ \lambda that are real algebraic numbers.

The paper contains both results and conjectures;. We now state them in detail.

### 1.1 Truncated Real Dynamical System: Results

For the truncated real dynamical system x n = ⌊ λ ​ 2 n ⌋ x_{n}=\lfloor\lambda 2^{n}\rfloor, we show that there is a uniform asymptotic upper bound valid for all nonzero λ \lambda on the number of n ≤ X n\leq X for which ( ⌊ λ ​ 2 n ⌋) 3 (\lfloor\lambda 2^{n}\rfloor)_{3} omits the digit 2 2. Let ( k) 3 (k)_{3} denote the ternary digit expansion of the integer k k.

###### Theorem 1.1

For each λ > 0 \lambda>0, the upper bound

 | N λ ​ ( X):= #⁡ { n: 1 ≤ n ≤ X ​ and ​ ( ⌊ λ ​ 2 n ⌋) 3 ​ omits the digit 2 } ≤ 25 ​ X 0.9725 N_{\lambda}(X):=\#\{n:~1\leq n\leq X~\mbox{and}~(\lfloor\lambda 2^{n}\rfloor)_{3}~\mbox{omits~the~digit~2}\}\leq 25X^{0.9725} |  | (1.3) |

holds for all all sufficiently large X ≥ n 0 ​ ( λ). X\geq n_{0}(\lambda).

In the complementary direction, the function N λ ​ ( X) N_{\lambda}(X) is not always bounded. The next result shows there exist uncountably many λ > 0 \lambda>0 such that the sequence x n ​ ( λ) x_{n}(\lambda) contains infinitely many integers omitting the digit 2 2 in their ternary expansion.

###### Theorem 1.2

There exists an infinite sequence S = { n k: k ≥ 1 } S=\{n_{k}:k\geq 1\} satisfying n 1 = 2 n_{1}=2 and

 | 2 1 14 ​ ( n k − 1 + 2 ​ k − 7) ≤ n k ≤ 2 27 ​ ( n k − 1 + 2 ​ k + 6), 2^{\frac{1}{14}(n_{k-1}+2k-7)}\leq n_{k}\leq 2^{27(n_{k-1}+2k+6)}, |  | (1.4) |

having the following property: The set of real numbers Σ ⁡ ( S) \Sigma(S) consisting of all λ > 0 \lambda>0 for which all the integers { x n ​ ( λ):= ⌊ λ ​ 2 n ⌋: n ∈ S } \{x_{n}(\lambda):=\lfloor\lambda 2^{n}\rfloor:n\in S\} have ternary expansions omitting the digit 2 2 is an uncountable set.

The set of exponents produced in this theorem forms a very thin infinite set. One can show that ( 1.4) implies that for X ≥ 2 X\geq 2, its cardinality satisfies

 | #⁡ { n k: 1 ≤ n k ≤ X } ≥ log ∗ ⁡ ( X) − 4. \#\{n_{k}:~1\leq n_{k}\leq X\}\geq\log_{\ast}(X)-4. |  | (1.5) |

in which log ∗ ⁡ ( X) \log_{\ast}(X) denotes the number of iterations of the logarithm function starting at X X necessary to get a value of smaller than 1 1. Thus we obtain that for all λ ∈ Σ ⁡ ( S) \lambda\in\Sigma(S),

 | N λ ​ ( X) ≥ log ∗ ⁡ ( X) − 4. N_{\lambda}(X)\geq\log_{\ast}(X)-4. |  | (1.6) |

We next consider properties of the set of λ \lambda that have infinitely such integers. We define the truncated real exceptional set ℰ T ​ ( ℝ +) {\cal E}_{T}({\mathbb{R}}_{+}) by

 | ℰ T ​ ( ℝ +):= { λ > 0: infinitely many ternary expansions ​ ( ⌊ λ ​ 2 n ⌋) 3 ​ omit the digit ​ 2 } {\cal E}_{T}({\mathbb{R}}_{+}):=\{\lambda>0:~\mbox{infinitely~many~ternary~expansions}~(\lfloor\lambda 2^{n}\rfloor)_{3}~\mbox{omit~the~digit}~2\} |  | (1.7) |

We prove the following result.

###### Theorem 1.3

The truncated real exceptional set has Hausdorff dimension

 | dim H ( ℰ T ​ ( ℝ +)) = log 3 ⁡ ( 2) = log ⁡ 2 log ⁡ 3 ≈ 0.63092. \dim_{H}({\cal E}_{T}({\mathbb{R}}_{+}))=\log_{3}(2)=\frac{\log 2}{\log 3}\approx 0.63092. |  |

It has nonzero log 3 ⁡ ( 2) \log_{3}(2) -dimensional Hausdorff measure.

This result gives an indication why it may be a hard problem to tell whether there are infinitely many exceptional powers of 2 2 for any particular λ \lambda, such as λ = 1 \lambda=1. Namely, it is likely to be a hard problem to decide whether any particular real number belongs to this ”small” exceptional set.

### 1.2 Real Dynamical System: Conjecture

Consider the real dynamical system y ↦ 2 ​ y y\mapsto 2y on ℝ +. {\mathbb{R}}_{+}. without truncation, having forward orbits O + ​ ( λ):= { y n = λ ​ 2 n: n ≥ 0 } O^{+}(\lambda):=\{y_{n}=\lambda 2^{n}:n\geq 0\}. We define the real exceptional set ℰ ⁡ ( ℝ +) {\cal E}({\mathbb{R}}_{+}) by

 | ℰ ⁡ ( ℝ +):= { λ > 0: infinitely many ternary expansions ​ ( λ ​ 2 n) 3 ​ omit the digit ​ 2 }. {\cal E}({\mathbb{R}}_{+}):=\{\lambda>0:~\mbox{infinitely~many~ternary~expansions}~(\lambda 2^{n})_{3}~\mbox{~omit~the~digit}~2\}. |  | (1.8) |

This set is much more constrained than the truncated exceptional set ℰ T ​ ( ℝ +) {\cal E}_{T}({\mathbb{R}}_{+}) discussed above. As far as we know it could even be the empty set. The conjecture of Erdős is equivalent to the assertion that 1 ∉ ℰ ⁡ ( ℝ +). 1\not\in{\cal E}({\mathbb{R}}_{+}).

Concerning this exceptional set we make the following conjecture.

#### Conjecture A.

The real exceptional set

 | ℰ ( ℝ):= { λ ∈ ℝ +: infinitely many ternary expansions ( λ 2 n) 3 omit the digit 2 } {\cal E}({\mathbb{R}}):=\{\lambda\in{\mathbb{R}}_{+}:~\mbox{infinitely many ternary expansions}~(\lambda 2^{n})_{3}~\mbox{omit the digit 2}\} |  |

has Hausdorff dimension zero.

A stronger form of this conjecture would be that the exceptional set is countable; even stronger would be the assertion that the real exceptional set is empty. Thus, for the moment, there remains the possibility that the conjecture of Erdős might hold for all initial conditions λ > 0 \lambda>0, for the full ternary expansions ( λ ​ 2 n) 3 (\lambda 2^{n})_{3} as real numbers.

Note that if the real exceptional set is nonempty, it will necessarily be an infinite set, because it is forward invariant under multiplication by 2 2, i.e. 2 ​ ℰ ​ ( ℝ +) ⊂ ℰ ⁡ ( ℝ +). 2{\cal E}({\mathbb{R}}_{+})\subset{\cal E}({\mathbb{R}}_{+}). It is clearly also forward invariant under multiplication by 3 3, i.e. 3 ​ ℰ ​ ( ℝ +) ⊂ ℰ ⁡ ( ℝ +) 3{\cal E}({\mathbb{R}}_{+})\subset{\cal E}({\mathbb{R}}_{+}). Thus it is forward invariant under two commuting semigroup actions. But the real exceptional set is not known to be a (topologically) closed set, so that results on Hausdorff dimension on closed sets invariant under commuting semigroup actions cannot be directly applied.

### 1.3 3 3 -Adic Dynamical System: Results

For a 3 3 -adic integer λ = ∑ j = 0 ∞ d j ​ 3 j \lambda=\sum_{j=0}^{\infty}d_{j}3^{j} with each d j ∈ { 0, 1, 2 } d_{j}\in\{0,1,2\} we write ( λ) 3 = ( ⋯ d 2 d 1 d 0) 3 (\lambda)_{3}=(\cdots d_{2}d_{1}d_{0})_{3} for its 3 3 -adic digital expansion. Our first observation is an upper bound on the number of solutions valid for all nonzero λ ∈ ℤ 3 \lambda\in{\mathbb{Z}}_{3}, which extends the result of Narkiewicz [18] for λ = 1 \lambda=1, using essentially the same proof.

###### Theorem 1.4

For each nonzero λ ∈ ℤ 3 \lambda\in{\mathbb{Z}}_{3}, the 3 3 -adic integers, and each X ≥ 2 X\geq 2,

 | N ~ λ ​ ( X):= #⁡ { n ≤ X: ( λ ​ 2 n) 3 ∈ ℤ 3 ​ omits the digit ​ 2 } ≤ 2 ​ X α 0, \tilde{N}_{\lambda}(X):=\#\{n\leq X:~(\lambda 2^{n})_{3}\in{\mathbb{Z}}_{3}~\mbox{omits~the~digit}~2\}\leq 2X^{\alpha_{0}}, |  | (1.9) |

with α 0 = log 3 ⁡ 2 ≈ 0.63092 \alpha_{0}=\log_{3}2\approx 0.63092.

We next study the 3 3 -adic exceptional set

 | ℰ ⁡ ( ℤ 3):= { λ ∈ ℤ 3: infinitely many 3-adic expansions ​ λ ​ 2 n ​ omit the digit 2 }. {\cal E}({\mathbb{Z}}_{3}):=\{\lambda\in{\mathbb{Z}}_{3}:~\mbox{infinitely~many~ 3-adic~expansions}~\lambda 2^{n}~\mbox{omit~the~digit~2}\}. |  | (1.10) |

This set seems hard to study directly, so as approximations to the 3 3 -adic exceptional set, we define for k ≥ 1 k\geq 1 the sequence of sets

 | ℰ ( k) ​ ( ℤ 3):= { λ ∈ ℤ 3: at least k values of ​ λ ​ 2 n ​ omit the digit 2 }. {\cal E}^{(k)}({\mathbb{Z}}_{3}):=\{\lambda\in{\mathbb{Z}}_{3}:~\mbox{at~least~ $k$~ values~ of}~\lambda 2^{n}~\mbox{omit~the~digit~2}\}. |  | (1.11) |

These sets clearly form a nested family under inclusion,

 | ℰ ( 1) ​ ( ℤ 3) ⊃ ℰ ( 2) ​ ( ℤ 3) ⊃ ℰ ( 3) ​ ( ℤ 3) ⊃ ⋯, {\cal E}^{(1)}({\mathbb{Z}}_{3})\supset{\cal E}^{(2)}({\mathbb{Z}}_{3})\supset{\cal E}^{(3)}({\mathbb{Z}}_{3})\supset\cdots, |  |

and their intersection contains the exceptional set ℰ ⁡ ( ℤ 3). {\cal E}({\mathbb{Z}}_{3}). These sets are somewhat easier to study.

We consider the problem of estimating the Hausdorff dimension of the sets ℰ ( k) ​ ( ℤ 3) {\cal E}^{(k)}({\mathbb{Z}}_{3}) (with respect to the 3 3 -adic metric) and show the following result.

###### Theorem 1.5

(1) The exceptional set 𝑂𝑃𝐸𝑁 ℰ ( 1) ​ ( ℤ 3)) {\cal E}^{(1)}({\mathbb{Z}}_{3})) has Hausdorff dimension

 | dim H ( ℰ ( 1) ​ ( ℤ 3)) = α 0 ≈ 0.63092. \dim_{H}({\cal E}^{(1)}({\mathbb{Z}}_{3}))=\alpha_{0}\approx 0.63092. |  | (1.12) |

(2) The exceptional set ℰ ( 2) ​ ( ℤ 3) {\cal E}^{(2)}({\mathbb{Z}}_{3}) has Hausdorff dimension bounded by

 | 1 2 ​ log 3 ⁡ ( 2) ≤ dim H ( ℰ ( 2) ​ ( ℤ 3)) ≤ 1 2. \frac{1}{2}\log_{3}(2)\leq\dim_{H}({\cal E}^{(2)}({\mathbb{Z}}_{3}))\leq\frac{1}{2}. |  | (1.13) |

(3) The exceptional set ℰ ( 3) ​ ( ℤ 3) {\cal E}^{(3)}({\mathbb{Z}}_{3}) has positive Hausdorff dimension bounded by

 | 1 6 ​ log 3 ​ 2 ≤ dim H ( ℰ ( 3) ​ ( ℤ 3)) ≤ dim H ( ℰ ( 2) ​ ( ℤ 3)). \frac{1}{6}\log_{3}2\leq\dim_{H}({\cal E}^{(3)}({\mathbb{Z}}_{3}))\leq\dim_{H}({\cal E}^{(2)}({\mathbb{Z}}_{3})). |  | (1.14) |

This result is only a beginning of the study of d ​ i ​ m H ​ ( ℰ ( k)) dim_{H}({\cal E}^{(k)}) for general k k. The (not necessarily closed) set ℰ ( k) ​ ( ℤ 3) {\cal E}^{(k)}({\mathbb{Z}}_{3}) is a countable union of closed sets 𝒞 ⁡ ( 2 m 1, 2 m 2, ⋯, 2 m k) {\cal C}(2^{m_{1}},2^{m_{2}},\cdots,2^{m_{k}}) consisting of those λ \lambda for which { λ ​ 2 m j: 1 ≤ j ≤ k } \{\lambda 2^{m_{j}}:1\leq j\leq k\} all have 3-adic expansions that omit the digit 2 2. One can use this to obtain upper and lower bounds on Hausdorff dimension of these sets by analyzing the Hausdorff dimension of the individual sets 𝒞 ⁡ ( 2 m 1, 2 m 2, ⋯, 2 m k). {\cal C}(2^{m_{1}},2^{m_{2}},\cdots,2^{m_{k}}). These sets are intersections of multiplicative translates of the 3 3 -adic Cantor set, which we discuss in the next subsection. In Theorem 1.5 the upper bound in (2) is deduced using Theorem 1.6 below.

It is not clear whether dim H ( ℰ ( k) ​ ( ℤ 3)) > 0 \dim_{H}({\cal E}^{(k)}({\mathbb{Z}}_{3}))>0 for all k ≥ 1 k\geq 1. Proving or disproving this assertion already seems a subtle question.

Since ℰ ⁡ ( ℤ 3) ⊆ ℰ ( k) ​ ( ℤ 3) {\cal E}({\mathbb{Z}}_{3})\subseteq{\cal E}^{(k)}({\mathbb{Z}}_{3}) for each k ≥ 1 k\geq 1, any upper bound on the Hausdorff dimension of ℰ ( k) ​ ( ℤ 3) {\cal E}^{(k)}({\mathbb{Z}}_{3}) gives an upper bound for the Hausdorff dimension of the 3 3 -adic exceptional set ℰ ⁡ ( ℤ 3). {\cal E}({\mathbb{Z}}_{3}). Each condition λ ​ 2 m j ∈ Σ 3, 2 ¯ \lambda 2^{m_{j}}\in\Sigma_{3,\bar{2}} imposes more constraints, apparantly lowering the Hausdorff dimension. This motivates the following conjecture concerning the 3 3 -adic exceptional set ℰ ⁡ ( ℤ 3). {\cal E}({\mathbb{Z}}_{3}).

#### Conjecture B.

The 3 3 -adic exceptional set

 | ℰ ( ℤ 3):= { λ ∈ ℤ 3: infinitely many 3-adic expansions λ 2 n omit the digit 2 } {\cal E}({\mathbb{Z}}_{3}):=\{\lambda\in{\mathbb{Z}}_{3}:\mbox{infinitely many 3-adic expansions}~\lambda 2^{n}~\mbox{omit the digit 2}\} |  |

has Hausdorff dimension zero.

As in the real dynamical system case, we do not know much about this exceptional set, except that it contains 0 0. Again, the conjecture of Erdős is equivalent to the assertion that 1 ∉ ℰ ⁡ ( ℤ 3) 1\not\in{\cal E}({\mathbb{Z}}_{3}). The 3 3 -adic exceptional set ℰ ⁡ ( ℤ 3) {\cal E}({\mathbb{Z}}_{3}) is forward invariant under multiplication by 2 2 and multiplication by 3 3, but is not known to be a closed set.

### 1.4 Intersection of Multiplicative Translates of Cantor Sets: Results

The study of the exceptional sets ℰ ( k) ​ ( ℤ 3) {\cal E}^{(k)}({\mathbb{Z}}_{3}) leads to auxiliary questions concerning the Hausdoff dimensions of intersections of multiplicative translates of the standard 3 3 -adic Cantor set Σ 3, 2 ¯ \Sigma_{3,\bar{2}}, defined by

 | Σ 3, 2 ¯:= { λ ∈ ℤ 3: the 3-adic expansion ​ ( λ) 3 ​ omits the digit 2 }. \Sigma_{3,\bar{2}}:=\{\lambda\in{\mathbb{Z}}_{3}:~\mbox{the ~3-adic~expansion}~(\lambda)_{3}~\mbox{omits~the~digit~2}\}. |  | (1.15) |

For integers 1 ≤ M 1 < M 2 < ⋯ < M k 1\leq M_{1}<M_{2}<\cdots<M_{k} we study the multiplicative intersection sets

 | 𝒞 ⁡ ( M 1, M 2, ⋯, M k) \displaystyle{\cal C}(M_{1},M_{2},\cdots,M_{k}) | : ⁣ = \displaystyle:= | { λ ∈ ℤ 3: ( M j ​ λ) 3 ​ omits the digit ​ 2 ​ for ​ 1 ≤ j ≤ k } \displaystyle\{\lambda\in{\mathbb{Z}}_{3}:~(M_{j}\lambda)_{3}~~\mbox{omits~the~digit}~2\mbox{ for}~1\leq j\leq k\} |  | (1.16) |

 |  | = \displaystyle= | ⋃ j = 1 k ( 1 M j ​ Σ 3, 2 ¯) \displaystyle\bigcup_{j=1}^{k}\left(\frac{1}{M_{j}}\Sigma_{3,\bar{2}}\right) |  |

These sets are closed sets. The standard ”middle third” Cantor set

 | Σ 3, 1 ¯:= { λ ∈ ℤ 3: the 3-adic digit expansion ​ ( λ) 3 ​ omits the digit 1 }. \Sigma_{3,\bar{1}}:=\{\lambda\in{\mathbb{Z}}_{3}:~\mbox{the~3-adic~digit~expansion}~(\lambda)_{3}~\mbox{omits~the~digit~1}\}. |  | (1.17) |

has Σ 3, 1 ¯ = 2 ​ Σ 3, 2 ¯ \Sigma_{3,\bar{1}}=2\Sigma_{3,\bar{2}}, so that all results given below for Σ 3 ​ 2 ¯ \Sigma_{3\bar{2}} convert to equivalent results for multiplicative translates of Σ 3, 1 ¯. \Sigma_{3,\bar{1}}.

Multiplicative intersection sets arise in studying sets ℰ ( k) ​ ( ℤ 3) {\cal E}^{(k)}({\mathbb{Z}}_{3}), because they are given by countable unions of such sets, namely

 | ℰ ( k) ​ ( ℤ 3) = ⋃ 0 ≤ m 1 < m 2 < … < m k 𝒞 ⁡ ( 2 m 1, 2 m 2, ⋯, 2 m k) {\cal E}^{(k)}({\mathbb{Z}}_{3})=\bigcup_{0\leq m_{1}<m_{2}<...<m_{k}}{\cal C}(2^{m_{1}},2^{m_{2}},\cdots,2^{m_{k}}) |  |

What can be said about the Hausdorff dimension of sets 𝒞 ⁡ ( M 1, M 2, …, M k) {\cal C}(M_{1},M_{2},...,M_{k})? This dimension depends in a complicated manner on the 3 3 -adic expansions of the M i M_{i}, and leads to various problems which seem interesting in their own right.

###### Theorem 1.6

Let M M be a positive integer which is not a power of 3 3. Let Σ 3, 2 ¯ \Sigma_{3,\bar{2}} be the ternary Cantor set. Then the Hausdorff dimension of 𝒞 ⁡ ( 1, M) = Σ 3, 2 ¯ ∩ 1 M ​ Σ 3, 2 ¯ {\cal C}(1,M)=\Sigma_{3,\bar{2}}\cap\frac{1}{M}\Sigma_{3,\bar{2}} satisfies

 | dim H ( 𝒞 ⁡ ( 1, M)) ≤ 1 2. \dim_{H}({\cal C}(1,M))\leq\frac{1}{2}. |  | (1.18) |

We do not know if this bound is sharp. However it is possible to show that

 | dim H ( 𝒞 ⁡ ( 1, 7)) = log 3 ⁡ ( 1 + 5 2) ≈ 0.438. \dim_{H}({\cal C}(1,7))=\log_{3}(\frac{1+\sqrt{5}}{2})\approx 0.438. |  |

For lower bounds on the Hausdorff dimension of such sets, we give the following sufficient condition for positivity of the Hausdorff dimension.

###### Theorem 1.7

Let 1 ≤ M 1 < M 2 < ⋯ < M k 1\leq M_{1}<M_{2}<\cdots<M_{k} be positive integers. Suppose there is a positive integer N N belonging to the 3 3 -adic Cantor set Σ 3, 2 ¯ ∪ ℤ \Sigma_{3,\bar{2}}\cup{\mathbb{Z}} such that all the integers N ​ M i NM_{i} satisfy

 | N ​ M i ∈ Σ 3, 2 ¯ ∩ ℤ, 1 ≤ j ≤ k. NM_{i}\in\Sigma_{3,\bar{2}}\cap{\mathbb{Z}},~~1\leq j\leq k. |  | (1.19) |

Then

 | d ​ i ​ m H ​ ( 𝒞 ⁡ ( M 1, M 2, …, M k)) ≥ log 3 ⁡ ( 2) ⌈ log 3 ⁡ ( N ​ M k) ⌉. dim_{H}({\cal C}(M_{1},M_{2},...,M_{k}))\geq\frac{\log_{3}(2)}{\lceil\log_{3}(NM_{k})\rceil}. |  | (1.20) |

This is proved by direct construction of a Cantor set of positive Hausdorff dimension inside 𝒞 ⁡ ( M 1, M 2, …, M k) {\cal C}(M_{1},M_{2},...,M_{k}).

This result gives a possible approach to obtaining a nonzero lower bound for dim H ( ℰ ( k) ​ ( ℤ 3)) \dim_{H}({\cal E}^{(k)}({\mathbb{Z}}_{3})) for k = 4 k=4 or larger, if suitable M i = 2 n i M_{i}=2^{n_{i}} can be found that fulfill its hypotheses. However it can be shown that the sufficient condition of Theorem 1.7 is not necessary, e.g. N = 1 N=1 and M 1 = 1, M 2 = 52 M_{1}=1,M_{2}=52 does not satisfy the hypothesis of this theorem, but 𝒞 ⁡ ( 1, 52) {\cal C}(1,52) has positive Hausdorff dimension. Thus further strengthenings of this approach may be possible.

Determining the structure and Hausdorff dimension of the sets 𝒞 ⁡ ( M 1, …, M k) {\cal C}(M_{1},...,M_{k}) leads to many open problems.

Problem 1. Let

 | ℳ C:= { M ≥ 1: there exist integers N 1, N 2 ∈ Σ 3, 2 ¯ with N 1 M = N 2 }. {\cal M}_{C}:=\{M\geq 1:~\mbox{there~exist~integers}N_{1},N_{2}\in\Sigma_{3,\bar{2}}~\mbox{with}~N_{1}M=N_{2}\}. |  |

Obtain upper and lower bounds for the number of integers 1 ≤ M ≤ X 1\leq M\leq X in ℳ C {\cal M}_{C}.

Problem 2. Let

 | ℳ H:= { M ≥ 1: dim H ( 𝒞 ( 1, M) > 0. } {\cal M}_{H}:=\{M\geq 1:~\dim_{H}({\cal C}(1,M)>0.\} |  |

Obtain upper and lower bounds for the number of integers 1 ≤ M ≤ X 1\leq M\leq X in ℳ H {\cal M}_{H}.

These are different problems, because it can be shown that the inclusion ℳ C ⊂ ℳ H {\cal M}_{C}\subset{\cal M}_{H} is strict.

### 1.5 Generalization of the Erdős Conjecture

We formulate the following strengthening of Erdős’s original question, by analogy with a conjecture of Furtstenberg [10, Conjecture 2’], which is reviewed in §5.

#### Conjecture E.

Let p p and q q be multiplicatively independent positive integers, i.e. all { p i q j: i ≥ 0, j ≥ 0 } \{p^{i}q^{j}:i\geq 0,j\geq 0\} are distinct. Then the base q q expansions of the powers { ( p n) q: n ≥ 1 } \{(p^{n})_{q}:n\geq 1\} have the property that any given finite pattern P = a 1 a 2 ⋯ a k P=a_{1}a_{2}\cdots a_{k} of consecutive q q -ary digits occurs in ( p n) q (p^{n})_{q}, for all sufficiently large n ≥ n 0 ​ ( P) n\geq n_{0}(P).

Conjecture E generalizes Erdős’s original problem, which is the special case p = 2 p=2, q = 3 q=3 with the single pattern P = 2 P=2. We note that Furstenberg’s original conjecture concerns d d -ary expansions of { ( p n) d: n ≥ 1 } \{(p^{n})_{d}:n\geq 1\} with d = p ​ q d=pq in which p p and q q are multiplicatively independent, i.e. his conjecture would apply to the 6 6 -adic expansion { ( 2 n) 6: n ≥ 0 } \{(2^{n})_{6}:n\geq 0\}, rather than the 3 3 -adic expansion above.

This conjecture might more properly be formulated as a question, since we present no significant new evidence in its favor. However we think that any mechanism that forces a single pattern to appear from some point on should apply to all patterns.

### 1.6 Summary

First, this paper places the original Erdős problem in a more general dynamical context.

The two dynamical generalizations seem to give restrictions on the original Erdős question of roughly equal strength, as formulated in Theorems 1.1 and 1.4. That is, they each reduce the number of candidate 1 ≤ n ≤ X 1\leq n\leq X to at most X c X^{c} for some 0 < c < 1. 0<c<1. What is interesting is that these arguments use ”independent” information about the ternary expansions of 2 n 2^{n}. The method used for the real dynamical system estimates the omission of 2 2 in the log 3 ⁡ X \log_{3}X most significant ternary digits of 2 n 2^{n}, while for the 3 3 -adic dynamical system the method estimates the omission of 2 2 in the log 3 ⁡ X \log_{3}X least significant ternary digits of 2 n 2^{n}. Heuristically, the most significant digits and least significant digits seem uncorrelated; this is the ”independence” referred to above. Furthermore, since the ternary expansion ( 2 n) 3 (2^{n})_{3} has about α 0 ​ n \alpha_{0}n ternary digits, the vast number of digits in the middle of the expansion are not exploited in either method; only a logarithmically small proportion of the available digits in the ternary expansion ( 2 n) 3 (2^{n})_{3} are considered in the two methods.

It seems a challenging problem to find a method that effectively combines the two approaches to find better upper bounds on N 1 ​ ( X) N_{1}(X) than that given by Narkiewicz. Can one obtain an upper bound of O ⁡ ( X β) O(X^{\beta}) for some β < log 3 ⁡ 2 \beta<\log_{3}2 in this way? Can one show that the high order digits and the low order digits in the ternary expansion ( 2 n) 3 (2^{n})_{3} are ”uncorrelated” in some quantifiable way?

Second, we formulate Conjecture A and Conjecture B , asserting Hausdorff dimension zero of exceptional sets, which seem more approachable questions than the original question of Erdős. A much harder question seems to be to resolve whether the exceptional sets ℰ ⁡ ( ℝ +) {\cal E}({\mathbb{R}}_{+}) and ℰ ⁡ ( ℤ 3) {\cal E}({\mathbb{Z}}_{3}) are countable or finite.

Third, our analysis leads to a variety of interesting auxiliary problems in combinatorial number theory. These concern the Hausdorff dimension of intersections of multiplicative translates of 3 3 -adic Cantor sets. These Hausdorff dimensions depend in an complicated arithmetic way on the values of the integer multipliers. These sets seem worthy of further study.

Finally, we observe analogies with work of Furstenberg [9], [10] on actions of multiplicative semigroups and intersections of Cantor sets. This resulted in formulating Conjecture E.

### 1.7 Contents and Notation

The contents of the rest of the paper are as follows. In §2 we prove results for the truncated real dynamical system. In §3 we prove results for the 3 3 -adic dynamical system. In §4 we establish auxiliary results on the Hausdorff dimensions of intersections of a finite number of multiplicative translates (by positive integers) of the 3 3 -adic Cantor set, and include several examples. These results are used to complete the proofs of one result in §3. In §5 we discuss work of Furstenberg. This includes a conjecure which motivates Conjecture E, and his formuation of a notion transversality of semigroup actions on a compact space and implications for intersections of Cantor sets. In the concluding section §6 we describe history associated to Erdős’s original question.

#### Notation.

Let

 | { { x } }:= x − ⌊ x ⌋ = x ( mod 1) \{\{x\}\}:=x-\lfloor x\rfloor=x~(\bmod~1) |  |

denote the fractional part of a real number x x. Let

 | ⟨ ⟨ x ⟩ ⟩:= { { x + 1 / 2 } } − 1 / 2 \langle\langle x\rangle\rangle:=\{\{x+1/2\}\}-1/2 |  |

denote the (signed) distance of x x to the nearest integer.

#### Acknowledgments.

I am grateful to A. Pollington, K. Soundararajan and H. Furstenberg for helpful comments and references. I thank the reviewer for helpful comments and suggestions. The author was supported by NSF grant DMS-0500555.

## 2 Real Dynamical System: Proofs

We consider the sequence of real numbers x n ∗:= λ ​ 2 n x_{n}^{\ast}:=\lambda 2^{n}, and consider the associated integers

 | x n ​ ( λ) = ⌊ x n ∗ ⌋. x_{n}(\lambda)=\lfloor x_{n}^{\ast}\rfloor. |  |

On taking logarithms to base 3 3 we have

 | log 3 ⁡ x n ∗ = log 3 ⁡ λ + n ​ log 3 ​ 2 = m n + w n, \log_{3}x_{n}^{\ast}=\log_{3}\lambda+n\log_{3}2=m_{n}+w_{n}, |  |

in which m n = ⌊ log 3 ⁡ x n ∗ ⌋ m_{n}=\lfloor\log_{3}x_{n}^{\ast}\rfloor is the integer part and w n:= log 3 ⁡ x n ∗ ( mod 1) w_{n}:=\log_{3}x_{n}^{\ast}~(\bmod~1) is the fractional part, with 0 ≤ w n < 1 0\leq w_{n}<1. Now the digits in the ternary expansion of x n ​ ( λ) x_{n}(\lambda) are completely determined by knowledge of the real number w n w_{n}, since x n ​ ( λ) = 3 m n ​ 3 w n x_{n}(\lambda)=3^{m_{n}}3^{w_{n}}, so they are the first m n m_{n} ternary digits in the ternary expansion of 3 w n 3^{w_{n}}, since multiplication by 3 m n 3^{m_{n}} simply shifts ternary digits to the left without changing them.

On the other hand, the sequence of w n w_{n} form an orbit under iteration of the map T: [0, 1] ↦ [0, 1] T:[0,1]\mapsto[0,1] given by

 | T ⁡ ( w) = w + log 3 ⁡ 2 ( mod 1). T(w)=w+\log_{3}2~(\bmod~1). |  | (2.21) |

on taking initial condition w 0 = log 3 ⁡ λ w_{0}=\log_{3}\lambda, with w n + 1 = T ⁡ ( w n) w_{n+1}=T(w_{n}). Since α 0 = log 3 ⁡ 2 \alpha_{0}=\log_{3}2 is irrational, the map T T is an irrational rotation on the torus ℝ / ℤ {\mathbb{R}}/{\mathbb{Z}}, which is known to be uniquely ergodic. In particular, every forward orbit of iteration of T T is uniformly distributed ( mod 1) (\bmod~1), with the convergence rate to uniform distribution determined by properties of the continued fraction expansion of α 0 \alpha_{0}. We now examine the consequences of this property for the ternary expansions of x n ∗ x_{n}^{\ast}.

First, the leading ternary digits of 3 w n 3^{w_{n}} specify the position of w n w_{n} in the interval [0, 1] [0,1] to a small subinterval. The property of omitting the digit 2 2 in a leading digit of a ternary expansion of x n x_{n} will prohibit w n w_{n} from certain subintervals in [0, 1]; [0,1]; the allowed subintervals will have small measure. Using the fact that the distribution of w n ( mod 1) w_{n}(\bmod~1) approaches the uniform distribution fairly rapidly, one can show that most w n w_{n} have some leading digit that is a 2 2; Theorem 1.1 is deduced using this idea, where the number k k of leading digits used will depend on the interval [1, X] [1,X] considered.

Second, one use a construction selecting a rapidly growing set of values of n = n k n=n_{k}, chosen using the continued fraction expansion of α 0 \alpha_{0}, in such a way as to permit each w n k w_{n_{k}} to fall in a ”good” interval where the initial ternary digits for a large set of short intervals have x n k ​ ( λ) x_{n_{k}}(\lambda) ’s with ternary expansions avoiding any 2 2 ’s. A recursive intervals construction, which modifies λ \lambda slightly at each stage while not disturbing the initial ternary digits already selected, produces the sets in Theorem 1.2. Finally, we use a quantitative version of such an intervals construction producing the set of Hausdorff dimension α 0 \alpha_{0} in Theorem 1.3.

We begin with two preliminary lemmas, the first on the spacings of multiples of an irrational number (modulo one) and the second on Diophantine approximation properties of α 0 = log 3 ⁡ 2 \alpha_{0}=\log_{3}2.

###### Lemma 2.1

Let θ \theta be irrational and consider the N + 1 N+1 numbers

 | { x + j ​ θ ( mod 1): 0 ≤ j ≤ N }, \{x+j\theta~(\bmod~1):0\leq j\leq N\}, |  |

viewed as subdividing the torus ℝ / ℤ {\mathbb{R}}/{\mathbb{Z}} (the interval [0, 1] [0,1] with endpoints identified) into N + 1 N+1 subintervals (”steps”).

(1) These subintervals take at most three distinct lengths. If three different lengths occur, say L 1, L 2, L 3 L_{1},L_{2},L_{3}, then one of them is the sum of the other two, say L 1 + L 2 = L 3 L_{1}+L_{2}=L_{3}.

(2) Let the continued fraction expansion of θ = [a 0, a 1, a 2, ⋯] \theta=[a_{0},a_{1},a_{2},\cdots], have partial quotients a i a_{i} and convergents p n q n \frac{p_{n}}{q_{n}} with denominators satisfying q n + 1 = a n + 1 ​ q n + q n − 1. q_{n+1}=a_{n+1}q_{n}+q_{n-1}. Write uniquely

 | N = ( j + 1) ​ q n + q n − 1 + k, 0 ≤ k ≤ q n − 1 N=(j+1)q_{n}+q_{n-1}+k,~~~0\leq k\leq q_{n}-1 |  | (2.22) |

with 0 ≤ j ≤ a n + 1 − 1. 0\leq j\leq a_{n+1}-1. Then the subintervals have lengths

 | L 1 \displaystyle L_{1} | = \displaystyle= | | ⟨ ⟨ q n ​ θ ⟩ ⟩ | \displaystyle|\langle\langle q_{n}\theta\rangle\rangle| |  |

 | L 2 \displaystyle L_{2} | = \displaystyle= | | ⟨ ⟨ q n − 1 ​ θ ⟩ ⟩ + ( j + 1) ​ ⟨ ⟨ q n ​ θ ⟩ ⟩ | \displaystyle|\langle\langle q_{n-1}\theta\rangle\rangle+(j+1)\langle\langle q_{n}\theta\rangle\rangle| |  |

 | L 3 \displaystyle L_{3} | = \displaystyle= | | ⟨ ⟨ q n − 1 ​ θ ⟩ ⟩ + j ⁡ ⟨ ⟨ q n ​ θ ⟩ ⟩ | \displaystyle|\langle\langle q_{n-1}\theta\rangle\rangle+j\langle\langle q_{n}\theta\rangle\rangle| |  |

and occur with multiplicities j ​ q n + q n − 1 + k + 1, k + 1, jq_{n}+q_{n-1}+k+1,~k+1, and q n − ( k + 1), ~q_{n}-(k+1), respectively. Here L 3 = L 1 + L 2 L_{3}=L_{1}+L_{2}, and L 1 < L 2 L_{1}<L_{2} if 0 ≤ j ≤ a n + 1 − 2 0\leq j\leq a_{n+1}-2, while L 2 < L 1 L_{2}<L_{1} if j = a n + 1 − 1 j=a_{n+1}-1. The intervals of size L 3 L_{3} do not occur if and only if k = q n − 1 k=q_{n}-1.

(3) For N = q n + 1 − 1 N=q_{n+1}-1, there occur intervals of exactly two lengths L 1, L 2 L_{1},L_{2} as above, and these lengths satisfy

 | L 2 < L 1 < 2 ​ L 2. L_{2}<L_{1}<2L_{2}. |  | (2.23) |

#### Proof.

(1), (2) These results have a long history, which is detailed in Slater [23]. In particular, (2) implies (1) and the formulas in (2) appear in Slater [23, eqn. (33), p. 1120]. The ordering of L 1 L_{1} and L 2 L_{2} follows from the fact that the ⟨ ⟨ q n ​ θ ⟩ ⟩ \langle\langle q_{n}\theta\rangle\rangle alternate in sign with successive n n.

(3) Let N = q n + 1 − 1 N=q_{n+1}-1. If a n ≥ 2 a_{n}\geq 2 then the decomposition ( 2.22) is

 | N = ( a n + 1 − 1) ​ q n + q n − 1 + ( q n − 1) N=(a_{n+1}-1)q_{n}+q_{n-1}+(q_{n}-1) |  |

with k = q n − 1 k=q_{n}-1 and j = a n + 1 − 1 j=a_{n+1}-1, Now (2) says there are steps of exactly two lengths L 1 L_{1} and L 2 L_{2} given by

 | L 1 \displaystyle L_{1} | = \displaystyle= | | ⟨ ⟨ q n ​ θ ⟩ ⟩ | \displaystyle|\langle\langle q_{n}\theta\rangle\rangle| |  |

 | L 2 \displaystyle L_{2} | = \displaystyle= | | ⟨ ⟨ q n − 1 ​ θ ⟩ ⟩ + ( a n + 1 − 1) ​ ⟨ ⟨ q n ​ θ ⟩ ⟩ | \displaystyle|\langle\langle q_{n-1}\theta\rangle\rangle+(a_{n+1}-1)\langle\langle q_{n}\theta\rangle\rangle| |  |

and L 2 < L 1 L_{2}<L_{1}. Next we have

 | ⟨ ⟨ q n + 1 ​ θ ⟩ ⟩ = ⟨ ⟨ q n − 1 ​ θ ⟩ ⟩ + a n + 1 ​ ⟨ ⟨ q n ​ θ ⟩ ⟩ = ( ⟨ ⟨ q n − 1 ​ θ ⟩ ⟩ + ( a n + 1 − 1) ​ ⟨ ⟨ q n ​ θ ⟩ ⟩) + ( ⟨ ⟨ q n ​ θ ⟩ ⟩). \langle\langle q_{n+1}\theta\rangle\rangle=\langle\langle q_{n-1}\theta\rangle\rangle+a_{n+1}\langle\langle q_{n}\theta\rangle\rangle=(\langle\langle q_{n-1}\theta\rangle\rangle+(a_{n+1}-1)\langle\langle q_{n}\theta\rangle\rangle)+(\langle\langle q_{n}\theta\rangle\rangle). |  |

Since ⟨ ⟨ q n + 1 ​ θ ⟩ ⟩ \langle\langle q_{n+1}\theta\rangle\rangle and ⟨ ⟨ q n ​ θ ⟩ ⟩ \langle\langle q_{n}\theta\rangle\rangle have opposite signs, and

 | | ⟨ ⟨ q n + 1 ​ θ ⟩ ⟩ | ≤ L 2 |\langle\langle q_{n+1}\theta\rangle\rangle|\leq L_{2} |  |

we must have

 | L 2 < L 1 = L 2 + | ⟨ ⟨ q n + 1 ​ θ ⟩ ⟩ | < 2 ​ L 2. L_{2}<L_{1}=L_{2}+|\langle\langle q_{n+1}\theta\rangle\rangle|<2L_{2}. |  |

(The fact that θ \theta is irrational gives the strict inequality at the last step.)

There remains the case a n + 1 = 1 a_{n+1}=1. Now we find that the decompostion ( 2.22) is

 | N = q n + q n − 1 − 1 = a n ​ q n − 1 + q n − 2 + ( q n − 1 − 1), N=q_{n}+q_{n-1}-1=a_{n}q_{n-1}+q_{n-2}+(q_{n-1}-1), |  |

with k = q n − 1 − 1 k=q_{n-1}-1 and j = a n − 1 − 1 j=a_{n-1}-1. As before, there are intervals of exactly two lengths

 | L 1 \displaystyle L_{1} | = \displaystyle= | | ⟨ ⟨ q n − 1 ​ θ ⟩ ⟩ | \displaystyle|\langle\langle q_{n-1}\theta\rangle\rangle| |  |

 | L 2 \displaystyle L_{2} | = \displaystyle= | | ⟨ ⟨ q n − 2 ​ θ ⟩ ⟩ + ( a n − 1) ​ ⟨ ⟨ q n − 1 ​ θ ⟩ ⟩ |, \displaystyle|\langle\langle q_{n-2}\theta\rangle\rangle+(a_{n}-1)\langle\langle q_{n-1}\theta\rangle\rangle|, |  |

with L 2 < L 1 L_{2}<L_{1}. We deduce as in the case a n + 1 ≥ 2 a_{n+1}\geq 2 that

 | L 2 < L 1 = L 2 + | ⟨ ⟨ q n ​ θ ⟩ ⟩ | < 2 ​ L 2, L_{2}<L_{1}=L_{2}+|\langle\langle q_{n}\theta\rangle\rangle|<2L_{2}, |  |

as required.

The point of Lemma 2.1 is that for the choice N = q n − 1 N=q_{n}-1 the points { x + j ​ θ ( mod 1): 0 ≤ j ≤ N } \{x+j\theta~(\bmod~1):0\leq j\leq N\} are very close to uniformly spaced on the interval [0, 1] [0,1]. The next result obtains information on the convergent denominators q n q_{n} for the irrational number α 0 \alpha_{0}.

###### Lemma 2.2

For the irrational number α 0 = log 3 ⁡ 2 \alpha_{0}=\log_{3}2 the following hold.

(1) For all q ≥ 1 q\geq 1, and all integer p p there holds the Diophantine inequality

 | | α 0 − p q | ≥ 1 1200 ​ 1 q c 0 + 1. |\alpha_{0}-\frac{p}{q}|\geq\frac{1}{1200}\frac{1}{q^{c_{0}+1}}. |  | (2.24) |

with c 0 = 13.3 c_{0}=13.3.

(2) The denominators q n q_{n} of the continued fraction convergents p n q n \frac{p_{n}}{q_{n}} of α 0 \alpha_{0} satisfy

 | q n ≤ 1200 ​ ( q n − 1) c 0. q_{n}\leq 1200(q_{n-1})^{c_{0}}. |  | (2.25) |

#### Proof.

(i) The existence of a bound of this general form, aside from the precise constants, follows from A. Baker’s results on linear forms in logarithms [1, Theorem 3.1], applied to the linear form Λ = k + q ​ log ⁡ 2 − p ​ log ⁡ 3 \Lambda=k+q\log 2-p\log 3, taking k = 0 k=0, noting that its height B:= max ⁡ { | p |, q } ≤ 2 ​ q B:=\max\{|p|,q\}\leq 2q.

The particular bound ( 2.24) is obtained from a result of Simons and de Weger [22, Lemma 12], who show that for k ≥ 1 k\geq 1 and all integers l l,

 | | ( k + l) ​ log ⁡ 2 − k ​ log ⁡ 3 | > exp ⁡ ( − 13.3 ​ ( 0.46057)) ​ k − 13.3 > 1 484 ​ k − 13.3. |(k+l)\log 2-k\log 3|>\exp(-13.3(0.46057))k^{-13.3}>\frac{1}{484}k^{-13.3}. |  |

Their result is proved using a transcendence result of G. Rhin [19, Proposition, p. 160] for linear forms in two logarithms. We may suppose k < k + l < 1.6 ​ k k<k+l<1.6k, and obtain

 | | log 3 ⁡ 2 − k k + l | > 1 log ⁡ 3 ​ exp ⁡ ( − 13.3 ​ ( 0.46057)) ​ ( k + l) − 1 ​ k − 13.3 ≥ 1 1200 ​ ( k + l) − 14.3, |\log_{3}2-\frac{k}{k+l}|>\frac{1}{\log 3}\exp(-13.3(0.46057))(k+l)^{-1}k^{-13.3}\geq\frac{1}{1200}(k+l)^{-14.3}, |  |

which on taking p = k, q = k + l p=k,q=k+l gives the needed bound.

(2) Since α 0 \alpha_{0} lies in the interval between two successive continued fraction convergents p n − 1 q n − 1 \frac{p_{n-1}}{q_{n-1}} and p n q n \frac{p_{n}}{q_{n}}, we obtain using ( 2.24) that

 | 1 q n ​ q n − 1 = | p n q n − p n − 1 q n − 1 | = | α 0 − p n − 1 q n − 1 | + | α 0 − p n q n | ≥ 1 1200 ​ 1 ( q n − 1) c 0 + 1 \frac{1}{q_{n}q_{n-1}}=|\frac{p_{n}}{q_{n}}-\frac{p_{n-1}}{q_{n-1}}|=|\alpha_{0}-\frac{p_{n-1}}{q_{n-1}}|+|{\alpha_{0}}-\frac{p_{n}}{q_{n}}|\geq\frac{1}{1200}\frac{1}{(q_{n-1})^{c_{0}+1}} |  |

Multiplying by 1200 ​ q n ​ q n − 1 c 0 1200q_{n}q_{n-1}^{c_{0}} gives ( 2.25).

#### Proof of Theorem 1.1.

Let λ > 0 \lambda>0. We study for 1 ≤ n ≤ X 1\leq n\leq X the ternary expansion of

 | x n = x n ​ ( λ) = ⌊ λ ​ 2 n ⌋. x_{n}=x_{n}(\lambda)=\lfloor\lambda 2^{n}\rfloor. |  |

We will study the first k k leading ternary digits of the { x n: 1 ≤ n ≤ X } \{x_{n}:1\leq n\leq X\} where we choose k k as follows. If p j q j \frac{p_{j}}{q_{j}} are the convergents of the continued fraction expansion of α 0 = log 3 ⁡ 2 \alpha_{0}=\log_{3}2, pick that l l such that q l − 1 < X ≤ q l q_{l-1}<X\leq q_{l}, and then choose k k to be the number of ternary digits in q l − 1 q_{l-1}, so that 3 k − 1 < q l − 1 ≤ 3 k 3^{k-1}<q_{l-1}\leq 3^{k}. Note that k = ⌈ log 3 ⁡ q l − 1 ⌉ ≤ ⌈ log 3 ⁡ X ⌉. k=\lceil\log_{3}q_{l-1}\rceil\leq\lceil\log_{3}X\rceil.

We now set w n:= log 3 ⁡ ( λ ​ 2 n) ​ ( m ​ o ​ d ​ 1), w_{n}:=\log_{3}(\lambda 2^{n})(mod~1), with 0 ≤ w n < 1, 0\leq w_{n}<1, so that

 | w n = n ​ α 0 + log 3 ⁡ λ ( mod 1). w_{n}=n\alpha_{0}+\log_{3}\lambda~(\bmod~1). |  | (2.26) |

We now observe that where w n w_{n} falls in the interval [0, 1) [0,1) specifies the first k k ternary digits in the ternary expansion of e w n e^{w_{n}}, with 1 ≤ e w n < 3 1\leq e^{w_{n}}<3, we can partition the interval [0, 1) [0,1) into half-open intervals corresponding to each such ternary expansion. Consider a ternary expansion

 | 𝐛 = [b 0 b 1 ⋯ b k − 1] 3, b i ∈ { 0, 1, 2 }, b 0 ≠ 0, {\bf b}=[b_{0}b_{1}\cdots b_{k-1}]_{3},~~~b_{i}\in\{0,1,2\},~b_{0}\neq 0, |  |

of length k k, noting there are 2 ⋅ 3 k − 1 2\cdot 3^{k-1} such expansions. Set

 | β ⁡ ( 𝐛) = ∑ j = 0 k − 1 b j 3 j, \beta({\bf b})=\sum_{j=0}^{k-1}\frac{b_{j}}{3^{j}}, |  | (2.27) |

which has 1 ≤ β ⁡ ( 𝐛) < 3 1\leq\beta({\bf b})<3 and associate the subinterval of [0, 1) [0,1),

 | J ⁡ ( 𝐛):= [log 3 ⁡ β ⁡ ( 𝐛), log 3 ⁡ ( β ⁡ ( 𝐛) + 1 3 k − 1)). J({{\bf b}}):=[\log_{3}\beta({\bf b}),\log_{3}(\beta({\bf b})+\frac{1}{3^{k-1}})). |  | (2.28) |

These 2 ⋅ 3 k − 1 2\cdot 3^{k-1} subintervals partition [0, 1) [0,1), from J ( [10 ⋯ 0] 3) = [log 3 ( 1), log 3 ( 1 + 1 3 k − 1)) J([10\cdots 0]_{3})=[\log_{3}(1),\log_{3}(1+\frac{1}{3^{k-1}})) to J ( [22 ⋯ 2] 3) = [log 3 ( 3 − 1 3 k − 1), log 3 3). J([22\cdots 2]_{3})=[\log_{3}(3-\frac{1}{3^{k-1}}),\log_{3}3).

We claim that the following conditions (C1) and (C2) are equivalent for x n x_{n} with 3 m ≤ x n ≤ 3 m + 1 3^{m}\leq x_{n}\leq 3^{m+1}, with m ≥ k m\geq k.

(C1) x n x_{n} has ternary expansion having the k k leading digits 𝐛 = [b 0 b 1 ⋯ b k − 1] 3 {\bf b}=[b_{0}b_{1}\cdots b_{k-1}]_{3}, i.e x n = ∑ j = 0 m b j ​ 3 m − j x_{n}=\sum_{j=0}^{m}b_{j}3^{m-j}, for some ( b k + 1, …, b m) (b_{k+1},...,b_{m}).

(C2) w n = log 3 ⁡ x n ( mod 1) w_{n}=\log_{3}x_{n}~(\bmod~1) has w n ∈ J ⁡ ( 𝐛) w_{n}\in J({\bf b}).

The claim follows because the definition of J ⁡ ( 𝐛) J({\bf b}) specifies the k leading ternary digits of 3 w n 3^{w_{n}}, while x n = 3 m ​ 3 w n x_{n}=3^{m}3^{w_{n}} and the effect of multiplying by 3 m 3^{m} simply shifts all ternary digits m m places to the left without changing the leading digits.

Next we note that the intervals J ⁡ ( 𝐛) J({\bf b}) all have the same length to within a factor of 3 3, namely

 | 1 3 k ≤ | J ⁡ ( 𝐛) | ≤ 1 3 k − 1. \frac{1}{3^{k}}\leq|J({\bf b})|\leq\frac{1}{3^{k-1}}. |  | (2.29) |

This holds using

 | | J ⁡ ( 𝐛) | = log ⁡ ( β ⁡ ( 𝐛) + 1 3 k − 1) − log ⁡ ( β ⁡ ( 𝐛)) = ∫ β ⁡ ( 𝐛) β ⁡ ( 𝐛) + 1 3 k − 1 d ​ x x, |J({\bf b})|=\log(\beta({\bf b})+\frac{1}{3^{k-1}})-\log(\beta({\bf b}))=\int_{\beta({\bf b})}^{\beta({\bf b})+\frac{1}{3^{k-1}}}\frac{dx}{x}, |  |

and the bounds ( 2.29) follow since 1 3 ≤ 1 x ≤ 1 \frac{1}{3}\leq\frac{1}{x}\leq 1.

Next we examine the w n w_{n} in consecutive blocks of length N = q l − 1 − 1 N=q_{l-1}-1, i.e the set { w n: j ⁡ ( q l − 1 − 1) ≤ n < ( j + 1) ​ ( q l − 1 − 1) }. \{w_{n}:j(q_{l-1}-1)\leq n<(j+1)(q_{l-1}-1)\}. By ( 2.26) we may apply Lemma 2.1 (3) to this sequence of numbers, to infer that the spacings between them are of two lengths L 1 L_{1} and L 2 L_{2} which satisfy L 2 < L 1 < 2 ​ L 2 L_{2}<L_{1}<2L_{2}. In particular since 3 k − 1 ≤ q l − 1 ≤ 3 k 3^{k-1}\leq q_{l-1}\leq 3^{k} these block sizes satisfy

 | 1 2 ⋅ 3 k ≤ 1 2 ​ ( q l − 1 − 1) ≤ L 1 < L 2 ≤ 2 q l − 1 − 1 ≤ 2 3 k − 1. \frac{1}{2\cdot 3^{k}}\leq\frac{1}{2(q_{l-1}-1)}\leq L_{1}<L_{2}\leq\frac{2}{q_{l-1}-1}\leq\frac{2}{3^{k-1}}. |  |

We conclude using ( 2.29) that at each subinterval J ⁡ ( 𝐛) J({\bf b}) contains at most six points w n w_{n} from this block. Thus at most six values of n n in j ⁡ ( q l − 1 − 1) ≤ n < ( j + 1) ​ ( q l − 1 − 1) j(q_{l-1}-1)\leq n<(j+1)(q_{l-1}-1) give an x n x_{n} having given intial k k -digit ternary expansion 𝐛 = [b 0 b 1 ⋯ b k 1] 3 {\bf b}=[b_{0}b_{1}\cdots b_{k_{1}}]_{3}.

We know there are exactly 2 k − 1 2^{k-1} values of 𝐛 = [b 0 b 1 ⋯ b k 1] 3 {\bf b}=[b_{0}b_{1}\cdots b_{k_{1}}]_{3} that omit the ternary digit 2 2, so the above shows there are at most 6 ⋅ 2 k − 1 6\cdot 2^{k-1} values of n n in each such block giving an x n x_{n} whose initial k k ternary digits avoid 2 2. There are ⌊ X q l − 1 − 1 ⌋ + 1 \lfloor\frac{X}{q_{l-1}-1}\rfloor+1 such blocks covering all 1 ≤ n ≤ X 1\leq n\leq X hence we conclude there are at most

 | M:= 6 ⋅ 2 k − 1 ​ ( X q l − 1 − 1 + 1) \displaystyle M:=6\cdot 2^{k-1}\left(\frac{X}{q_{l-1}-1}+1\right) | ≤ \displaystyle\leq | 6 ⋅ 2 k − 1 ​ ( X 3 k − 1 + 1) \displaystyle 6\cdot 2^{k-1}\left(\frac{X}{3^{k-1}}+1\right) |  |

 |  | ≤ \displaystyle\leq | 6 ​ ( ( 2 3) k − 1 ​ X + 2 k − 1) ≤ 12 ​ ( 2 3) k − 1 ​ X, \displaystyle 6\left((\frac{2}{3})^{k-1}X+2^{k-1}\right)\leq 12(\frac{2}{3})^{k-1}X, |  |

values of x n x_{n} whose initial k k ternary digits omit the digit 2 2. (In the last inequality we used X ≥ q l − 1 > 3 k − 1. X\geq q_{l-1}>3^{k-1}.

It remains to upper bound M M as a function of X X. Using Lemma 2.2 (2) we have

 | X ≤ q l ≤ 1200 ​ ( q l − 1) c 0 ≤ 1200 ​ ( 3 k) c 0 X\leq q_{l}\leq 1200(q_{l-1})^{c_{0}}\leq 1200(3^{k})^{c_{0}} |  |

with c 0 = 13.3 c_{0}=13.3. We apply this bound to obtain

 | ( 3 2) k = ( 3 c 0 ​ k) log 3 ⁡ ( 3 / 2) ​ c 0 − 1 ≥ ( 1 1200 ​ X) ( 1 − α 0 c 0), (\frac{3}{2})^{k}=\left(3^{c_{0}k}\right)^{\log_{3}(3/2)c_{0}^{-1}}\geq\left(\frac{1}{1200}X\right)^{(\frac{1-\alpha_{0}}{c_{0}})}, |  |

Here 1 37 < ( log 3 ⁡ ( 3 / 2)) ​ c 0 − 1 = 1 − α 0 c 0 ≤ 1 36 \frac{1}{37}<(\log_{3}(3/2))c_{0}^{-1}=\frac{1-\alpha_{0}}{c_{0}}\leq\frac{1}{36}, so we obtain

 | ( 2 3) k ≤ ( 1200) 1 − α 0 c 0 ​ X − ( 1 − α 0 c 0) (\frac{2}{3})^{k}\leq(1200)^{\frac{1-\alpha_{0}}{c_{0}}}X^{-(\frac{1-\alpha_{0}}{c_{0}})} |  |

Substituting this into the definition of M M we obtain,

 | M ≤ 18 ​ ( 2 3) k ​ X ≤ 18 ⋅ ( 1200) 1 36 ​ X 1 − 1 − α 0 c 0 ≤ 25 ​ X 36 37 ≤ 25 ​ X 0.9725. M\leq 18(\frac{2}{3})^{k}X\leq 18\cdot(1200)^{\frac{1}{36}}X^{1-\frac{1-\alpha_{0}}{c_{0}}}\leq 25X^{\frac{36}{37}}\leq 25X^{0.9725}. |  |

and the result follows. .

#### Proof of Theorem 1.2.

We will construct a rapidly increasing sequence of integers S 0 = { m k: k ≥ 1 } S_{0}=\{m_{k}:k\geq 1\} having the form

 | m k = l 0 + l 1 + … + l k, m_{k}=l_{0}+l_{1}+...+l_{k}, |  | (2.30) |

such that there is an uncountable set of real numbers Σ ~ \tilde{\Sigma} such that all the numbers λ ∈ Σ \lambda\in\Sigma have the property: for each k ≥ 1 k\geq 1, the integer M k:= ⌊ λ ​ 2 m k ⌋ M_{k}:=\lfloor\lambda 2^{m_{k}}\rfloor has a ternary expansion that omits the digit 1 1. We now claim that all the integers N k:= ⌊ λ ​ 2 m k − 1 ⌋ N_{k}:=\lfloor\lambda 2^{m_{k}-1}\rfloor have ternary expansions ( N k) 3 (N_{k})_{3} that omit the digit 2 2. This holds because for each N k N_{k} either M k = 2 ​ N k M_{k}=2N_{k} or M k = 2 ​ N k + 1 M_{k}=2N_{k}+1, but M k M_{k} is necessarily an even integer since all its ternary digits are 0 0 or 2 2, so we must have M k = 2 ​ N k M_{k}=2N_{k}. Thus N k N_{k} has only digits 0 0 and 1 1 in its ternary expansion, so we have for S = { m k − 1: k ≥ 1 } S=\{m_{k}-1:k\geq 1\} that

 | Σ ~ ⊂ Σ ⁡ ( S):= { λ: ( ⌊ λ ​ 2 n k ⌋) 3 ​ omits the digit ​ 2 }, \tilde{\Sigma}\subset\Sigma(S):=\{\lambda:~(\lfloor\lambda 2^{n_{k}}\rfloor)_{3}~\mbox{omits~the~digit}~~2\}, |  |

hence Σ ⁡ ( S) \Sigma(S) is an uncountable set.

We choose the l k l_{k} recursively, taking l 0 = m 0 = 0 l_{0}=m_{0}=0 and l k l_{k} to be the smallest integer satisfying l k ≥ 2 ​ k l_{k}\geq 2k and

 | 0 < { { log 3 ⁡ 2 l k } } = { { l k ​ α 0 } } < 2 − m k − 1 − 2 ​ k − 4. 0<\{\{\log_{3}2^{l_{k}}\}\}=\{\{l_{k}\alpha_{0}\}\}<2^{-m_{k-1}-2k-4}. |  | (2.31) |

Here m k = l 0 + l 1 + ⋯ + l k m_{k}=l_{0}+l_{1}+\cdots+l_{k}. We set

 | r k:= ⌊ l k ​ α 0 ⌋, α 0 = log 3 ⁡ 2. r_{k}:=\lfloor l_{k}\alpha_{0}\rfloor,~~~~~~\alpha_{0}=\log_{3}2. |  |

The condition l k ≥ 2 ​ k l_{k}\geq 2k ensures that r k ≥ k r_{k}\geq k. Then we have

 | 2 l k = 3 l k ​ α 0 = 3 r k + { { l k ​ α 0 } } = 3 r k ​ 3 { { l k ​ α 0 } }. 2^{l_{k}}=3^{l_{k}\alpha_{0}}=3^{r_{k}+\{\{l_{k}\alpha_{0}\}\}}=3^{r_{k}}3^{\{\{l_{k}\alpha_{0}\}\}}. |  |

Using e x ≤ 1 + 2 ​ x e^{x}\leq 1+2x for 0 ≤ x ≤ 1 0\leq x\leq 1 we have

 | 3 { { l k ​ α 0 } } = e { { l k ​ α 0 } } ​ log ⁡ 3 ≤ 1 + 2 ​ log ⁡ 3 ​ { { l k ​ α 0 } } ≤ 1 + 2 ​ log ⁡ 3 2 m k − 1 + 2 ​ k + 4. 3^{\{\{l_{k}\alpha_{0}\}\}}=e^{\{\{l_{k}\alpha_{0}\}\}\log 3}\leq 1+2\log 3\{\{l_{k}\alpha_{0}\}\}\leq 1+\frac{2\log 3}{2^{m_{k-1}+2k+4}}. |  |

Thus we obtain

 | 3 r k < 2 l k < 3 r k ​ ( 1 + 2 ​ ln ⁡ 3 2 m k − 1 + 2 ​ k + 4) ≤ 3 r k ​ ( 1 + 1 3 ( m k − 1 + 2 ​ k + 2) ​ α 0) 3^{r_{k}}<2^{l_{k}}<3^{r_{k}}\left(1+\frac{2\ln 3}{2^{m_{k-1}+2k+4}}\right)\leq 3^{r_{k}}\left(1+\frac{1}{3^{(m_{k-1}+2k+2)\alpha_{0}}}\right) |  | (2.32) |

This says that the ternary expansion of 2 l k 2^{l_{k}} has leading digit 1 1 followed by a string of at least ( m k − 1 + 2 ​ k + 2) ​ α 0 (m_{k-1}+2k+2)\alpha_{0} zeros.

Given this choice of { l k: k ≥ 1 } \{l_{k}:k\geq 1\}, we define the set Σ \Sigma to consist of all real numbers

 | Σ ~:= { λ:= ∑ k = 0 ∞ d k 2 m k: λ ​ is admissible } \tilde{\Sigma}:=\{\lambda:=\sum_{k=0}^{\infty}\frac{d_{k}}{2^{m_{k}}}:\lambda~\mbox{is~ admissible}\} |  | (2.33) |

where λ \lambda is called admissible if, for all k ≥ 1 k\geq 1 it has the two properties

(P1) The digit d k d_{k} satisfies

 | 0 ≤ d k ≤ 3 r k − 3 r k − k. 0\leq d_{k}\leq 3^{r_{k}}-3^{r_{k}-k}. |  | (2.34) |

(P2) Let λ k:= ∑ j = 0 k d j 2 m j \lambda_{k}:=\sum_{j=0}^{k}\frac{d_{j}}{2^{m_{j}}}. Then the integer

 | M k:= λ k ​ 2 m k M_{k}:=\lambda_{k}2^{m_{k}} |  | (2.35) |

has a ternary expansion ( M k) 3 (M_{k})_{3} which omits the digit 1 1.

Claim 1. Any λ = ∑ j = 0 ∞ d j 2 m j \lambda=\sum_{j=0}^{\infty}\frac{d_{j}}{2^{m_{j}}} with all d k d_{k} satisfying (P1) satisfies

 | 1 ≤ λ < 2 1\leq\lambda<2 |  | (2.36) |

and

 | M k = λ k ​ 2 m k = ⌊ λ ​ 2 m k ⌋, for all ​ k ≥ 1. M_{k}=\lambda_{k}2^{m_{k}}=\lfloor\lambda 2^{m_{k}}\rfloor,~\mbox{for~all}~~k\geq 1. |  | (2.37) |

To prove the claim , we observe that (P1) gives

 | 1 ≤ λ \displaystyle~1\leq\lambda | ≤ \displaystyle\leq | 1 + ∑ k = 1 ∞ 1 2 m k − 1 ​ ( 3 r k − 3 r k − k 2 l k) \displaystyle 1+\sum_{k=1}^{\infty}\frac{1}{2^{m_{k-1}}}\left(\frac{3^{r_{k}}-3^{r_{k}-k}}{2^{l_{k}}}\right) |  | (2.38) |

 |  | ≤ \displaystyle\leq | 1 + ∑ k = 1 ∞ 1 2 m k − 1 ​ ( 1 − 3 − k) < 2. \displaystyle 1+\sum_{k=1}^{\infty}\frac{1}{2^{m_{k-1}}}(1-3^{-k})<2. |  |

Next, (P1) gives

 | 0 ≤ λ − λ k \displaystyle 0\leq\lambda-\lambda_{k} | = \displaystyle= | ∑ j = k + 1 ∞ d j 2 m j = 1 2 m k ​ ( ∑ j = k + 1 ∞ d j 2 m j − m k) \displaystyle\sum_{j=k+1}^{\infty}\frac{d_{j}}{2^{m_{j}}}=\frac{1}{2^{m_{k}}}\left(\sum_{j=k+1}^{\infty}\frac{d_{j}}{2^{m_{j}-m_{k}}}\right) |  |

 |  | ≤ \displaystyle\leq | 1 2 m k ​ ( ∑ j = k + 1 ∞ ( 1 − 1 3 j) ​ 1 2 m j − 1 − m k) \displaystyle\frac{1}{2^{m_{k}}}\left(\sum_{j=k+1}^{\infty}(1-\frac{1}{3^{j}})\frac{1}{2^{m_{j-1}-m_{k}}}\right) |  |

 |  | ≤ \displaystyle\leq | 1 2 m k ​ ( ∑ j = k + 1 ∞ ( 1 − 1 3 j) ​ 1 2 ( j − k − 1) ​ ( 2 ​ j)) < 1 2 m k, \displaystyle\frac{1}{2^{m_{k}}}\left(\sum_{j=k+1}^{\infty}(1-\frac{1}{3^{j}})\frac{1}{2^{(j-k-1)(2j)}}\right)<\frac{1}{2^{m_{k}}}, |  |

proving Claim 1.

Claim 2. For any choice of { d j: 1 ≤ j ≤ k − 1 } \{d_{j}:1\leq j\leq k-1\} that satisfy both (P1) and (P2), there are at least 2 r k − 2 r k − k 2^{r_{k}}-2^{r_{k}-k} choices of d k d_{k} that satisfy (P1) and (P2).

To prove this, first note that

 | λ k − 1 ​ 2 m k = M k − 1 ​ 2 m k − m k − 1 = M k − 1 ​ 2 l k = M k − 1 ​ 3 r k + M k − 1 ​ ( 2 l k − 3 r k). \lambda_{k-1}2^{m_{k}}=M_{k-1}2^{m_{k}-m_{k-1}}=M_{k-1}2^{l_{k}}=M_{k-1}3^{r_{k}}+M_{k-1}(2^{l_{k}}-3^{r_{k}}). |  | (2.39) |

We assert that

 | 0 ≤ M k − 1 ​ ( 2 l k − 3 r k) ≤ 3 r k − k. 0\leq M_{k-1}(2^{l_{k}}-3^{r_{k}})\leq 3^{r_{k}-k}. |  | (2.40) |

The left inequality is immediate, and using ( 2.38) we have M k − 1 ≤ λ ​ 2 m k − 1 ≤ 2 m k − 1 + 1 M_{k-1}\leq\lambda 2^{m_{k-1}}\leq 2^{m_{k-1}+1}, while ( 2.32) gives

 | M k − 1 ​ ( 2 l k − 3 r k) \displaystyle M_{k-1}(2^{l_{k}}-3^{r_{k}}) | ≤ \displaystyle\leq | 2 m k − 1 + 1 ​ ( 3 r k ​ ln ⁡ 3 2 m k − 1 + 2 ​ k + 4) \displaystyle 2^{m_{k-1}+1}\left(3^{r_{k}}\frac{\ln 3}{2^{m_{k-1}+2k+4}}\right) |  |

 |  | ≤ \displaystyle\leq | 3 r k ​ 1 2 2 ​ k + 3 ≤ 3 r k − k, \displaystyle 3^{r_{k}}\frac{1}{2^{2k+3}}\leq 3^{r_{k}-k}, |  |

proving ( 2.40).

From ( 2.39) and ( 2.40) we see that the ternary expansion of λ k − 1 ​ 2 m k \lambda_{k-1}2^{m_{k}} repeats that of M k − 1 M_{k-1} shifted r k r_{k} positions to the left, then has a block of at least k k zeros, and following this has the ternary expansion of the integer M k − 1 ​ ( 2 l k − 3 r k) M_{k-1}(2^{l_{k}}-3^{r_{k}}). It follows that choosing from the range of values 0 ≤ d k ≤ 3 r k − 3 r k − k 0\leq d_{k}\leq 3^{r_{k}}-3^{r_{k}-k}, and setting λ k:= ∑ j − 0 k d j 2 m j \lambda_{k}:=\sum_{j-0}^{k}\frac{d_{j}}{2^{m_{j}}}, the integers

 | M k:= λ k ​ 2 m k = λ k − 1 ​ 2 m k + d k M_{k}:=\lambda_{k}2^{m_{k}}=\lambda_{k-1}2^{m_{k}}+d_{k} |  | (2.41) |

can be selected to give all ternary integers which

(i) have the ternary expansion matching M k − 1 M_{k-1} to the left of the r k r_{k} -th position,

(ii) omit the digit 1 1, and

(iii) have at least one 2 2 and at least one 0 0 in positions between r k r_{k} and r k − k r_{k}-k;

call these allowable values. In these k + 1 k+1 positions the largest allowed value is 222 ⋯ 20 222\cdots 20 and the smallest is 000 ⋯ 02 000\cdots 02. These produce exactly 2 r k − 2 r k − k 2^{r_{k}}-2^{r_{k}-k} such ternary integers M k M_{k}, constructed by choice of the same number of allowable values d k d_{k}. This proves Claim 2.

Claim 3. The set Σ ~ \tilde{\Sigma} contains uncountably many admissible λ \lambda, and each of them has the property that every

 | M k = ⌊ λ ​ 2 m k ⌋, k ≥ 1, M_{k}=\lfloor\lambda 2^{m_{k}}\rfloor,~~~k\geq 1, |  | (2.42) |

has a ternary expansion ( M k) 3 (M_{k})_{3} that omits the digit 1 1.

Indeed Claim 2 implies there are uncountably many such λ \lambda, since the construction has a Cantor set form which gives an infinite tree of values with branching at least two at every node at every level k ≥ 2 k\geq 2. The relation ( 2.42) holds by Claim 1, and these M k M_{k} have ternary expansions omitting 2 by (P2). Thus Claim 3 follows.

It remains to verify the upper and lower bounds ( 1.4) on the growth rate of the sequence m k m_{k}. The size of m k m_{k} is determined by the Diophantine condition on l k l_{k} given by equation ( 2.31). (The numbers l k l_{k} grow so rapidly that the side condition l k ≥ 2 ​ k l_{k}\geq 2k is automatically satisfied for k ≥ 2 k\geq 2.) Note that we cannot directly use Dirichlet’s box principle to get an upper bound for the size of the minimal l k l_{k} satisfying ( 2.31) because this is a one-sided approximation condition. Instead we have that the minimal l k l_{k} will be no larger than that even-numbered convergent q 2 ​ l q_{2l} of the continued fraction expansion of α 0 \alpha_{0} satisfying

 | q 2 ​ l − 2 ≤ 2 m k − 1 + 2 ​ k + 4 < q 2 ​ l. q_{2l-2}\leq 2^{m_{k-1}+2k+4}<q_{2l}. |  |

Lemma 2.2 (2) gives the bound

 | q 2 ​ l ≤ 1 C 0 2 ​ ( q 2 ​ l − 2) 2 ​ c 1 = ( 1200) 2 ​ ( q 2 ​ l − 2) 26.6 ≤ 2 27 ​ m k − 1 + 54 ​ k + 132. q_{2l}\leq\frac{1}{C_{0}^{2}}(q_{2l-2})^{2c_{1}}=(1200)^{2}(q_{2l-2})^{26.6}\leq 2^{27m_{k-1}+54k+132}. |  | (2.43) |

Since n k = m k − 1 n_{k}=m_{k}-1 we obtain

 | n k ≤ m k ≤ m k − 1 + q 2 ​ l ≤ m k − 1 + 2 27 ​ m k − 1 + 54 ​ k + 132 ≤ 2 27 ​ ( n k − 1 + 2 ​ k + 6), n_{k}\leq m_{k}\leq m_{k-1}+q_{2l}\leq m_{k-1}+2^{27m_{k-1}+54k+132}\leq 2^{27(n_{k-1}+2k+6)}, |  |

which is the upper bound in ( 1.4).

Lemma 2.2 implies a lower bound on how small l k + 1 l_{k+1} can be to make ( 2.31) hold, namely we must have

 | ( l k + 1) c 0 ≥ 2 m k + 2 ​ j − 7, (l_{k+1})^{c_{0}}\geq 2^{m_{k}+2j-7}, |  | (2.44) |

with c 0 = 13.3, c_{0}=13.3, to avoid contradicting 2.2 (1). This yields the lower bound in ( 1.4), which holds for n k = m k − 1 n_{k}=m_{k}-1 produced in this construction.

#### Proof of Theorem 1.3.

We consider the truncated exceptional set ℰ T ​ ( ℝ +) {\cal E}_{T}({\mathbb{R}}_{+}). We first establish the upper bound d ​ i ​ m H ​ ( ℰ T ​ ( ℝ +)) ≤ α 0 dim_{H}({\cal E}_{T}({\mathbb{R}}_{+}))\leq\alpha_{0}. We have

 | ℰ T ​ ( ℝ +) = ⋃ M = 2 ∞ ( ℰ T ​ ( ℝ +) ∩ [1 M, M]). {\cal E}_{T}({\mathbb{R}}_{+})=\bigcup_{M=2}^{\infty}\left({\cal E}_{T}({\mathbb{R}}_{+})\cap[\frac{1}{M},M]\right). |  |

Since the Hausdorff dimension of a countable union of sets is the supremum of the Hausdorff dimensions of the separate sets, it suffices to show that

 | d ​ i ​ m H ​ ( ℰ T ​ ( ℝ +) ∩ [1 M, M]) ≤ α 0 = log 3 ⁡ 2. dim_{H}({\cal E}_{T}({\mathbb{R}}_{+})\cap[\frac{1}{M},M])\leq\alpha_{0}=\log_{3}2. |  | (2.45) |

To show this we find suitable coverings of these sets. For each n ≥ 1 n\geq 1 we have

 | OPEN ℰ T ​ ( ℝ +) ∩ [1 M, M]) ⊂ S n ​ ( M):= ⋃ j = N ∞ Σ j ​ ( [1 M, M]) {\cal E}_{T}({\mathbb{R}}_{+})\cap[\frac{1}{M},M])\subset S_{n}(M):=\bigcup_{j=N}^{\infty}\Sigma_{j}([\frac{1}{M},M]) |  | (2.46) |

with

 | Σ j ​ ( [1 M, M]):= { λ: − 1 M ≤ λ ≤ M ​ and ​ ( ⌊ λ ​ 2 j ⌋) 3 ​ omits the digit ​ 2 }. \Sigma_{j}([\frac{1}{M},M]):=\{\lambda:-\frac{1}{M}\leq\lambda\leq M~~\mbox{and}~(\lfloor\lambda 2^{j}\rfloor)_{3}~\mbox{omits~the~digit}~2\}. |  |

The set S n ​ ( M) S_{n}(M) thus encodes a ”tail event” that there are arbitrarily large j j for which ( ⌊ λ ​ 2 j ⌋) 3 (\lfloor\lambda 2^{j}\rfloor)_{3} that omit the digit 2 2. We will eventually let n → ∞ n\to\infty so we suppose that n ≥ log 3 ⁡ M + 2 n\geq\log_{3}M+2, so that λ ​ 2 j ≥ 1 \lambda 2^{j}\geq 1, for any j ≥ n j\geq n. Now consider such j j as fixed, and note that ⌊ λ ​ 2 j ⌋ \lfloor\lambda 2^{j}\rfloor takes a fixed integer value on an interval of length 1 2 j \frac{1}{2^{j}}. Letting 𝐛 = ( ⌊ λ ​ 2 j ⌋) 3 {\bf b}=(\lfloor\lambda 2^{j}\rfloor)_{3}, we see that allowable values of 𝐛 {\bf b} satisfy 1 ≤ 𝐛 ≤ M ​ 2 j 1\leq{\bf b}\leq M2^{j}. As λ \lambda varies over [1 M, M] [\frac{1}{M},M] these integers vary over a subset of [1, M ​ 2 j] [1,M2^{j}] and of these, the number of such ternary expansions 𝐛 {\bf b} that omit the digit 2 2 is at most (counting integers over successive blocks [3 k − 1, 3 k) [3^{k-1},3^{k})),

 | 1 + 2 + ⋯ + 2 ⌈ log 3 ⁡ ( 2 j ​ M) ⌉ \displaystyle 1+2+\cdots+2^{\lceil\log_{3}(2^{j}M)\rceil} | ≤ \displaystyle\leq | 2 log 2 ⁡ ( 2 j ​ M) + 2 \displaystyle 2^{\log_{2}(2^{j}M)+2} |  |

 |  | ≤ \displaystyle\leq | 2 j ​ α 0 + log 3 ⁡ M + 2 ≤ 4 ​ M ​ 2 j ​ α 0. \displaystyle 2^{j\alpha_{0}+\log_{3}M+2}\leq 4M2^{j\alpha_{0}}. |  |

Thus we obtain a collection

 | ℐ j ( M):= { I j ( 𝐛): 𝐛 gives an admissible interval for ⌊ λ 2 j ⌋, 1 M ≤ λ ≤ M }. {\cal I}_{j}(M):=\{I_{j}({\bf b}):~{\bf b}~~\mbox{gives~an~admissible~interval~for}~\lfloor\lambda 2^{j}\rfloor,~\frac{1}{M}\leq\lambda\leq M\}. |  |

of at most 4 ​ M ​ 2 j ​ α 0 4M2^{j\alpha_{0}} intervals of length 1 3 j \frac{1}{3^{j}}, and these intervals cover the set Σ j ​ ( [1 M, M]). \Sigma_{j}([\frac{1}{M},M]). Summing over all j ≥ n j\geq n we obtain an infinite collection of intervals

 | ℐ ⁡ ( n, M):= ⋃ j = n ∞ ℐ j ​ ( M), {\cal I}(n,M):=\bigcup_{j=n}^{\infty}{\cal I}_{j}(M), |  |

which cover the set OPEN ℰ T ​ ( ℝ +) ∩ [1 M, M]) {\cal E}_{T}({\mathbb{R}}_{+})\cap[\frac{1}{M},M]) by ( 2.46), and every interval included has length at most 1 2 n. \frac{1}{2^{n}}. Now fix ϵ > 0 \epsilon>0 and observe that

 | ∑ I ∈ ℐ ⁡ ( n, M) | I | α 0 + ϵ \displaystyle\sum_{I\in{\cal I}(n,M)}|I|^{\alpha_{0}+\epsilon} | = \displaystyle= | ∑ j = n ∞ ( ∑ I ∈ ℐ j ​ ( M) ( 1 2 j) α 0 + ϵ) \displaystyle\sum_{j=n}^{\infty}\left(\sum_{I\in{\cal I}_{j}(M)}(\frac{1}{2^{j}})^{\alpha_{0}+\epsilon}\right) |  |

 |  | ≤ \displaystyle\leq | ∑ j = n ∞ 4 ​ M ​ 2 j ​ α 0 ​ ( 1 2 j) α 0 + ϵ \displaystyle\sum_{j=n}^{\infty}4M2^{j\alpha_{0}}(\frac{1}{2^{j}})^{\alpha_{0}+\epsilon} |  |

 |  | = \displaystyle= | 4 ​ M ​ ( ∑ j = n ∞ 2 − j ​ ϵ) = ( 4 ​ M 1 − 2 − ϵ) ​ 2 − n ​ ϵ. \displaystyle 4M\left(\sum_{j=n}^{\infty}2^{-j\epsilon}\right)=(\frac{4M}{1-2^{-\epsilon}})2^{-n\epsilon}. |  |

Letting n → ∞ n\to\infty, the diameter of the covering ℐ ⁡ ( n, M) {\cal I}(n,M) goes to zero, and the scaled length goes to zero as well, which establishes

 | d ​ i ​ m H ​ ( ℰ T ​ ( ℝ +) ∩ [1 M, M]) ≤ α 0 + ϵ. dim_{H}\left({\cal E}_{T}({\mathbb{R}}_{+})\cap[\frac{1}{M},M]\right)\leq\alpha_{0}+\epsilon. |  |

Now we can let ϵ → 0 \epsilon\to 0 to obtain ( 2.45), and the upper bound d ​ i ​ m H ​ ( ℰ T ​ ( ℝ +)) ≤ α 0 dim_{H}({\cal E}_{T}({\mathbb{R}}_{+}))\leq\alpha_{0} follows.

To establish the lower bound d ​ i ​ m H ​ ( ℰ T ​ ( ℝ)) ≥ α 0 dim_{H}({\cal E}_{T}({\mathbb{R}}))\geq\alpha_{0} is more difficult, as it requires controlling all coverings of the set. We will actually establish the stronger result that

 | m ​ e ​ a ​ s α 0 ​ ( Σ ~) > 1 16, meas_{\alpha_{0}}(\tilde{\Sigma})>\frac{1}{16}, |  | (2.47) |

where Σ ~ ⊂ [1, 2] \tilde{\Sigma}\subset[1,2] is the set constructed in Theorem 1.2 in ( 2.33). The set Σ ~ \tilde{\Sigma} had a construction resembling a Cantor set, with two differences. The first difference is that the dissection at each layer k k depended on the previous layers, and the second difference is that the layer at level k k involved denominators 2 m k 2^{m_{k}} with

 | m k = l 0 + l 1 + … + l k, m_{k}=l_{0}+l_{1}+...+l_{k}, |  |

with the l k l_{k} growing extremely rapidly. We can however adapt an argument given in Falconer [7, Example 2.7, p. 31] for the Cantor set to show ( 2.47).

We claim that Σ ~ \tilde{\Sigma} has a representation as

 | Σ ~ = ⋂ s = 1 ∞ X s, \tilde{\Sigma}=\bigcap_{s=1}^{\infty}X_{s}, |  | (2.48) |

in which X s X_{s} consists of a union of a collection 𝒥 s {\cal J}_{s} of disjoint intervals of size proportional to 3 − s 3^{-s}, and the sets are nested:

 | ⋯ X 3 ⊂ X 2 ⊂ X 1. \cdots X_{3}\subset X_{2}\subset X_{1}. |  |

Here the intervals in 𝒥 s {\cal J}_{s} will play the role of the Cantor set dissection into intervals at level s s, for each power of 3 s 3^{s}.

We first define the collection 𝒥 s {\cal J}_{s} for those levels s = s k s=s_{k} with

 | s j:= ⌊ m j ​ α 0 ⌋, s_{j}:=\lfloor m_{j}\alpha_{0}\rfloor, |  | (2.49) |

which are directly given in the construction of Theorem 1.2. Then we show one can fill in all the intermediate layers s k ≤ s < s k + 1 s_{k}\leq s<s_{k+1}.

We have 3 s k < 2 m k < 3 s k + 1 3^{s_{k}}<2^{m_{k}}<3^{s_{k}+1}, and the set 𝒥 s k {\cal J}_{s_{k}} is the union of all closed intervals

 | 𝒥 s k:= { [M 2 m k, M + 1 2 m k]: M = λ k 2 m k with λ k = ∑ j = 0 k d j 2 m j admissible. } {\cal J}_{s_{k}}:=\{\left[\frac{M}{2^{m_{k}}},\frac{M+1}{2^{m_{k}}}\right]:~M=\lambda_{k}2^{m_{k}}~\mbox{with}~\lambda_{k}=\sum_{j=0}^{k}\frac{d_{j}}{2^{m_{j}}}~\mbox{admissible}.\} |  |

with admissibility in the construction in Theorem 1.2. Here we have

 | 2 m k = 2 l 1 + … + l k = 3 l 1 ​ α 0 + … + l k ​ α 0 = 3 r 1 + r 2 + … + r k ⋅ 3 { { l 1 ​ α 0 } } + … + { { l k ​ α 0 } } ≤ 2 ⋅ 3 r + 1 + … + r k, 2^{m_{k}}=2^{l_{1}+...+l_{k}}=3^{l_{1}\alpha_{0}+...+l_{k}\alpha_{0}}=3^{r_{1}+r_{2}+...+r_{k}}\cdot 3^{\{\{l_{1}\alpha_{0}\}\}+...+\{\{l_{k}\alpha_{0}\}\}}\leq 2\cdot 3^{r+1+...+r_{k}}, |  |

using the fact that

 | ∑ k = 1 ∞ { { l k ​ α 0 } } ≤ ∑ k = 1 ∞ 2 − m k − 1 − 2 ​ k − 2 ≤ 1 2, \sum_{k=1}^{\infty}\{\{l_{k}\alpha_{0}\}\}\leq\sum_{k=1}^{\infty}2^{-m_{k-1}-2k-2}\leq\frac{1}{2}, |  |

using ( 2.31). This also establishes that

 | s k = r 1 + r 2 + … + r k. s_{k}=r_{1}+r_{2}+...+r_{k}. |  | (2.50) |

Inside each interval at level s = s k − 1 s=s_{k-1} there fit exactly 2 r k − 2 r k − k 2^{r_{k}}-2^{r_{k}-k} subintervals at ternary level s = s k s=s_{k}, each of length 2 − m k 2^{-m_{k}}, and we now know that 1 2 ​ 3 − s k ≤ 2 − m k ≤ 3 − s k. \frac{1}{2}3^{-s_{k}}\leq 2^{-m_{k}}\leq 3^{-s_{k}}. This dissection of an interval at ternary level s k − 1 s_{k-1} into subintervals at ternary level s k s_{k} is exactly that of the Cantor set, except that the two ends of the interval are trimmed off a small amount, to a relative distance 3 − k 3^{-k} from each end of the interval.

We now fill in the intermediate levels X s X_{s} for s k − 1 < s < s k s_{k-1}<s<s_{k} by gluing together all intervals in 𝒥 s k {\cal J}_{s_{k}} that have matching initial ternary expansions [M] 3 [M]_{3} of M = λ k ​ 2 m k M=\lambda_{k}2^{m_{k}}, disregarding the last s k − s s_{k}-s ternary digits of [M] 3 [M]_{3}, and filling in the space between them. The resulting intervals of 𝒥 s {\cal J}_{s} all have size exactly 3 s k − s ​ 2 − m k 3^{s_{k}-s}2^{-m_{k}} (except possibly for two subintervals adjacent to the truncated ends); their size lies between 1 2 ​ 3 − s \frac{1}{2}3^{-s} and 3 − s 3^{-s}. Also, the gaps between any two adjacent intervals at ternary level s s are of size at least as large as

 | G s = 3 s k − s ​ 2 − m k ≥ 1 2 ​ 3 − s. G_{s}=3^{s_{k}-s}2^{-m_{k}}\geq\frac{1}{2}3^{-s}. |  | (2.51) |

This fact holds because this construction uses ternary integers omitting the digit 1 1; the set of ternary integers omitting the digit 2 2 has some intervals of this kind that are adjacent, so the gap size would be zero in that case.

The above construction defines the intervals in 𝒥 s {\cal J}_{s} at level s s for all s s. This dissection imitates the Cantor set in that each interval at level s s, contains at most 2 s ′ − s 2^{s^{\prime}-s} subintervals at any deeper ternary level s ′ ≥ s s^{\prime}\geq s. It may contain fewer subintervals, due to the trimming at ends of the subinterval, but it always contains at least 2 s ′ − s − 1 2^{s^{\prime}-s-1} such subintervals.

The set Σ ~ \tilde{\Sigma} is a compact set contained in the interval [1, 2] [1,2]. To bound its α 0 \alpha_{0} -dimensional Hausdorff measure from below, we must show that in every covering { U i } \{U_{i}\} by closed intervals there holds

 | ∑ i | U i | α 0 ≥ 1 16. \sum_{i}|U_{i}|^{\alpha_{0}}\geq\frac{1}{16}. |  | (2.52) |

By enlarging the intervals slightly (by 1 + ϵ 1+\epsilon) and observing that their interiors give an open cover of Σ ~ \tilde{\Sigma}, we can extract a finite subcover. Since we can extract a finite subcover for any ϵ > 0 \epsilon>0, it suffices to verify ( 2.52) holds for every finite cover { U i } \{U_{i}\} of Σ ~ \tilde{\Sigma} by intervals.

Given an interval U i U_{i} in a covering, define s s by

 | 3 − s ≤ | U i | < 3 − s + 1. 3^{-s}\leq|U_{i}|<3^{-s+1}. |  | (2.53) |

Then U i U_{i} can touch at most two subintervals at level s s because all subintervals in 𝒥 s {\cal J}_{s} are sepated by gaps of size at least 1 2 ​ 3 − s. \frac{1}{2}3^{-s}. If s ′ ≥ s s^{\prime}\geq s then U i U_{i} intersects at most 2 ⋅ 2 s ′ − s 2\cdot 2^{s^{\prime}-s} subintervals at level s ′ − s s^{\prime}-s; by ( 2.53) this number is bounded above by

 | OPEN 2 ⋅ 2 s ′ − s ≤ 2 s ′ ​ 3 − α 0 ​ s ≤ 2 ⋅ 2 s ′ ​ ( 3 α 0 ​ | U i | α 0) = 4 ⋅ 2 s ′ ​ | U i | α 0). 2\cdot 2^{s^{\prime}-s}\leq 2^{s^{\prime}}3^{-\alpha_{0}s}\leq 2\cdot 2^{s^{\prime}}(3^{\alpha_{0}}|U_{i}|^{\alpha_{0}})=4\cdot 2^{s^{\prime}}|U_{i}|^{\alpha_{0}}). |  | (2.54) |

Given a finite cover, choose s ′ = s k s^{\prime}=s_{k} large enough so that | U i | ≥ 3 − s ′ |U_{i}|\geq 3^{-s^{\prime}} for all i i. Then the collection { U i } \{U_{i}\} necessarily covers all subintervals at level s ′ = s k s^{\prime}=s_{k}. By construction ℐ s k {\cal I}_{s_{k}} contains at least

 | ∏ i = 1 k ( 2 r i − 2 r i − i) = 2 r 1 + … + r k ​ ∏ i = 1 n ( 1 − 2 − i) ≥ 1 4 ​ 2 s k \prod_{i=1}^{k}(2^{r_{i}}-2^{r_{i}-i})=2^{r_{1}+...+r_{k}}\prod_{i=1}^{n}(1-2^{-i})\geq\frac{1}{4}2^{s_{k}} |  | (2.55) |

intervals, since where ∏ i = 1 k ( 1 − 2 − i) ≥ ∏ i = 1 ∞ ( 1 − 2 − i) ≥ 1 4 \prod_{i=1}^{k}(1-2^{-i})\geq\prod_{i=1}^{\infty}(1-2^{-i})\geq\frac{1}{4}. Now we count how many intervals at level s k s_{k} are covered. Since U i U_{i} intersects at most 4 ⋅ 2 s k ​ | U i | α 0 4\cdot 2^{s_{k}}|U_{i}|^{\alpha_{0}} such intervals we must have

 | ∑ i 4 ⋅ 2 s k ​ | U i | α 0 ≥ | 𝒥 s k | ≥ 1 4 ​ 2 − s k. \sum_{i}4\cdot 2^{s_{k}}|U_{i}|^{\alpha_{0}}\geq|{\cal J}_{s_{k}}|\geq\frac{1}{4}2^{-s_{k}}. |  |

This yields

 | ∑ i | U i | α 0 ≥ 1 16, \sum_{i}|U_{i}|^{\alpha_{0}}\geq\frac{1}{16}, |  |

which establishes ( 2.47).

#### Remark.

More generally we may consider the real dynamical system y → β ​ y y\to\beta y, where β > 1 \beta>1, and consider the truncated ternary expansions { ( ⌊ λ ​ β n ⌋) 3: n ≥ 0 } \{(\lfloor\lambda\beta^{n}\rfloor)_{3}:n\geq 0\}. The methods above should extend to those β \beta such that α:= log 3 ⁡ β \alpha:=\log_{3}\beta satisfies a Diophantine condition

 | | α − p q | ≥ c 2 ​ 1 q c 1 + 1, for all ​ p, q ​ with ​ q ≥ 1, |\alpha-\frac{p}{q}|\geq c_{2}\frac{1}{q^{c_{1}+1}},~~\mbox{for~all}~p,q~\mbox{with}~q\geq 1, |  | (2.56) |

for constants c 1 > 1 c_{1}>1 and c 2 > 0 c_{2}>0. The conclusions of the results require appropriate modification, with constants depending on the Diophantine condition.

## 3 3 3 -adic Integer Dynamical System: Proofs

We consider the 3 3 -adic integers ℤ 3 {\mathbb{Z}}_{3} and write the 3 3 -adic expansion of λ ∈ ℤ 3 \lambda\in{\mathbb{Z}}_{3} as

 | λ = ∑ j = 0 ∞ d j ​ 3 j ​ with each ​ d j ∈ { 0, 1, 2 }. \lambda=\sum_{j=0}^{\infty}d_{j}3^{j}~~~\mbox{with~each}~d_{j}\in\{0,1,2\}. |  | (3.57) |

We write the 3 3 -adic digit expansion as ( λ) 3 = ( ⋯ d 2 d 1 d 0) 3. (\lambda)_{3}=(\cdots d_{2}d_{1}d_{0})_{3}.

This dynamical system consider the sequence of 3 3 -adic integers, y n = λ ​ 2 n, y_{n}=\lambda 2^{n}, where λ \lambda is a given nonzero 3 3 -adic integer. Here y n y_{n} form the forward orbit of the first order linear recurrence y n = 2 ​ y n − 1 y_{n}=2y_{n-1}, with initial condition y 0 = λ y_{0}=\lambda. The map T: x → 2 ​ x T:x\to 2x is an automorphism of the 3 3 -adic integers ℤ 3 {\mathbb{Z}}_{3}, which leaves each of the sets Σ j:= 3 j ​ ℤ 3 ∗ \Sigma_{j}:=3^{j}{\mathbb{Z}}_{3}^{\ast} for j ≥ 0 j\geq 0 invariant. (Here ℤ 3 ∗ {\mathbb{Z}}_{3}^{\ast} are the 3 3 -adic units.) These sets partition ℤ 3 {\mathbb{Z}}_{3} and this map acts ergodically on each component Σ j \Sigma_{j}.

We are interested in the possible ways that the orbit { y n: n ≥ 0 } \{y_{n}:n\geq 0\} can intersect the set Σ 3, 2 ¯:= { w: w = ∑ j = 0 ∞ a j 3 j ∈ ℤ 3, with each a j = 0 or 1 }. \Sigma_{3,\bar{2}}:=\{w:w=\sum_{j=0}^{\infty}a_{j}3^{j}\in{\mathbb{Z}}_{3},~\mbox{with~each}~a_{j}=0~\mbox{or}~1\}. We now upper bound the number of n ≤ X n\leq X that can fall in the set Σ 3, 2 ¯ \Sigma_{3,\bar{2}}.

#### Proof of Theorem 1.4.

Let λ ∈ ℤ 3 \lambda\in{\mathbb{Z}}_{3} with λ ≠ 0 \lambda\neq 0. We study the set

 | N ~ λ ​ ( X):= #⁡ { 1 ≤ n ≤ X: ( λ ​ 2 n) 3 ​ omits the digit ​ 2 }. \tilde{N}_{\lambda}(X):=\#\{1\leq n\leq X:~(\lambda 2^{n})_{3}~~\mbox{omits~the~digit}~2\}. |  | (3.58) |

Write λ = 3 j ​ λ ∗ \lambda=3^{j}\lambda^{\ast} with λ ∗ ∈ ℤ 3 ×:= { λ ∈ ℤ 3: λ ≢ 0 ( mod 3) }. \lambda^{\ast}\in{\mathbb{Z}}_{3}^{\times}:=\{\lambda\in{\mathbb{Z}}_{3}:~\lambda\not\equiv 0~(\bmod~3)\}. Then we have N ~ λ ​ ( X) = N ~ λ ∗ ​ ( X) \tilde{N}_{\lambda}(X)=\tilde{N}_{\lambda^{\ast}}(X), since multiplication by 3 j 3^{j} simply shifts 3 3 -adic digits to the left. Thus to prove the desired inequality there is no loss of generality to require λ ≠ 0 ( mod 3) \lambda\neq 0~(\bmod~3), by replacing λ \lambda with λ ∗ \lambda^{\ast}.

The proof is based on the fact that 2 2 is a primitive root ( mod 3 k) (\bmod~3^{k}) for each k ≥ 1 k\geq 1. Thus, for each k ≥ 1 k\geq 1

 | { λ ​ 2 n ( mod 3): 1 ≤ n ≤ ϕ ⁡ ( 3 k) = 2 ⋅ 3 k − 1 } \{\lambda 2^{n}~(\bmod~3):1\leq n\leq\phi(3^{k})=2\cdot 3^{k-1}\} |  | (3.59) |

runs over all 2 ⋅ 3 k − 1 2\cdot 3^{k-1} invertible residue classes ( mod 3 k) (\bmod~3^{k}). Of these, exactly 2 k − 1 2^{k-1} residue classes have a 3 3 -adic expansion that omits the digit 2 2. Now, given X X, pick that k k such that

 | 2 ⋅ 3 k − 2 < X ≤ 2 ⋅ 3 k − 1. 2\cdot 3^{k-2}<X\leq 2\cdot 3^{k-1}. |  |

Then applying ( 3.59) over 1 ≤ n ≤ 2 ⋅ 3 k − 1 1\leq n\leq 2\cdot 3^{k-1} we have exactly 2 k − 1 2^{k-1} values of n n with ( λ ​ 2 n) 3 (\lambda 2^{n})_{3} omitting the digit 2 2 in its first k k 3 3 -adic digits ( d k − 1 ⋯ d 1 d 0) 3. (d_{k-1}\cdots d_{1}d_{0})_{3}. Thus

 | N ~ λ ​ ( X) \displaystyle\tilde{N}_{\lambda}(X) | ≤ \displaystyle\leq | 2 k − 1 = 2 ⋅ 2 k − 2 = 2 ⋅ 3 α 0 ​ ( k − 2) \displaystyle 2^{k-1}=2\cdot 2^{k-2}=2\cdot 3^{\alpha_{0}(k-2)} |  |

 |  | = \displaystyle= | 2 1 − α 0 ​ ( 2 ⋅ 3 k − 2) α 0 ≤ 2 ​ X α 0, \displaystyle 2^{1-\alpha_{0}}\left(2\cdot 3^{k-2}\right)^{\alpha_{0}}\leq 2X^{\alpha_{0}}, |  |

which is the desired upper bound.

The object of Theorem 1.5 is to establish upper bounds on the Hausdorff dimension of the 3-adic exceptional set ℰ ⁡ ( ℤ 3) {\cal E}({\mathbb{Z}}_{3}) through upper bounds on various ℰ ( j) ​ ( ℤ 3) {\cal E}^{(j)}({\mathbb{Z}}_{3}) which contain it.

We note that Hausdorff dimension is a metric notion (cf. Rogers [20]), and its version for 3 3 -adic integers uses the 3 3 -adic metric is quite similar to Hausdorff dimension for real numbers on the interval [0, 1] [0,1]. In fact we have a continuous (and almost one-to-one) mapping ι: ℤ 3 → [0, 1] \iota:{\mathbb{Z}}_{3}\to[0,1] which sends a 3 3 -adic number λ = ( ⋯ d 2 d 1 d 0) 3 \lambda=(\cdots d_{2}d_{1}d_{0})_{3} to the real number with ternary expansion . d 0 d 1 d 2 ⋯.d_{0}d_{1}d_{2}\cdots. One can show that this mapping preserves Hausdorff dimension of sets, i.e a 3 3 -adic set X X and its image ι ⁡ ( X) \iota(X) have the same Hausdorff dimension. This holds because one can expand each set in a 3 3 -adic covering of a set X X to a closed-open disk
B ⁡ ( m, 3 j) = { x ∈ ℤ 3: x ≡ m ( mod 3 j) } B(m,3^{j})=\{x\in{\mathbb{Z}}_{3}:~x\equiv m~(\bmod~3^{j})\}, with at most a factor of 3 3 increase in diameter, and similarly one can inflate any real covering to a covering with ternary intervals [m 3 j, m + 1 3 j] [\frac{m}{3^{j}},\frac{m+1}{3^{j}}] with at most a factor of 3 increase in diameter. But these special intervals are assigned the same diameter under their respective metrics, and this can be used to show the Hausdorff dimensions of X X and ι ⁡ ( X) \iota(X) coincide. In particular the standard 3 3 -adic Cantor set Σ 3, 1 ¯ \Sigma_{3,\bar{1}} maps under ι \iota to the usual Cantor set in [0, 1] [0,1] hence it has Hausdorff dimension d H ​ ( Σ 3, 1 ¯) = log 3 ⁡ ( 2) ≈ 0.63092 d_{H}(\Sigma_{3,\bar{1}})=\log_{3}(2)\approx 0.63092. Now OPEN Σ 3, 1 ¯ = 2 ​ Σ 3, 2 ¯) \Sigma_{3,\bar{1}}=2\Sigma_{3,\bar{2}}) hence dim H ( Σ 3, 2 ¯) = log 3 ⁡ ( 2) \dim_{H}(\Sigma_{3,\bar{2}})=\log_{3}(2) as well.

#### Proof of Theorem 1.5.

This proof assumes that Theorem 1.6 is proved in order to deduce the upper bound in (2).

(1) We have

 | ℰ ( 1) ​ ( ℤ 3) = ⋃ m = 0 ∞ 𝒞 ⁡ ( 2 m), {\cal E}^{(1)}({\mathbb{Z}}_{3})=\bigcup_{m=0}^{\infty}{\cal C}(2^{m}), |  |

with 𝒞 ⁡ ( 2 m):= { λ: ( λ ​ 2 n) 3 ​ omits the digit ​ 2 }. {\cal C}(2^{m}):=\{\lambda:~(\lambda 2^{n})_{3}~\mbox{omits~the~digit}~~2\}. Then

 | 𝒞 ⁡ ( 2 m) = 1 2 m ​ 𝒞 ​ ( 1) = 1 2 m ​ ( Σ 3, 2 ¯) = 1 2 m + 1 ​ ( Σ 3, 1 ¯). {\cal C}(2^{m})=\frac{1}{2^{m}}{\cal C}(1)=\frac{1}{2^{m}}(\Sigma_{3,\bar{2}})=\frac{1}{2^{m+1}}(\Sigma_{3,\bar{1}}). |  |

Each 𝒞 ⁡ ( 2 m) {\cal C}(2^{m}) is a linearly rescaled version of the Cantor set Σ 3, 1 ¯ \Sigma_{3,\bar{1}} so has Hausdorff dimension log 3 ⁡ 2 \log_{3}2. Thus

 | log 3 ⁡ 2 = dim H ( 𝒞 ⁡ ( 1)) ≤ dim H ( ℰ ( 1) ​ ( ℤ 3)) ≤ sup m ≥ 0 dim H ( 𝒞 ⁡ ( 2 m)) = log 3 ⁡ 2, \log_{3}2=\dim_{H}({\cal C}(1))\leq\dim_{H}({\cal E}^{(1)}({\mathbb{Z}}_{3}))\leq\sup_{m\geq 0}\dim_{H}({\cal C}(2^{m}))=\log_{3}2, |  |

as required.

(2) We have

 | ℰ ( 2) ​ ( ℤ 3) = ⋃ 0 ≤ m 1 < m 2 𝒞 ⁡ ( 2 m 1, 2 m 2). {\cal E}^{(2)}({\mathbb{Z}}_{3})=\bigcup_{0\leq m_{1}<m_{2}}{\cal C}(2^{m_{1}},2^{m_{2}}). |  |

with 𝒞 ⁡ ( 2 m 1, 2 m 2):= { λ: ( λ ​ 2 m i) 3 ​ omits the digit ​ 2 }. {\cal C}(2^{m_{1}},2^{m_{2}}):=\{\lambda:~(\lambda 2^{m_{i}})_{3}~\mbox{omits~the~digit}~~2\}. Now

 | 𝒞 ⁡ ( 2 m 1, 2 m 2) = 1 2 m 1 ​ 𝒞 ​ ( 1, 2 m 2 − m 1), {\cal C}(2^{m_{1}},2^{m_{2}})=\frac{1}{2^{m_{1}}}{\cal C}(1,2^{m_{2}-m_{1}}), |  |

which gives dim H ( 𝒞 ⁡ ( 2 m 1, 2 m 2)) = dim H ( 𝒞 ⁡ ( 1, 2 m 2 − m 1)). \dim_{H}({\cal C}(2^{m_{1}},2^{m_{2}}))=\dim_{H}({\cal C}(1,2^{m_{2}-m_{1}})). Since m 2 − m 1 ≥ 1 m_{2}-m_{1}\geq 1, Theorem 1.6 applies to give

 | dim H ( 𝒞 ⁡ ( 1, 2 m 2 − m 1)) ≤ 1 2, for all ​ m 2 > m 1 ≥ 0. \dim_{H}({\cal C}(1,2^{m_{2}-m_{1}}))\leq\frac{1}{2},~~\mbox{for~all}~m_{2}>m_{1}\geq 0. |  |

This yields the upper bound

 | dim H ( ℰ ( 2) ​ ( ℤ 3)) = sup 0 ≤ m 1 < m 2 dim H ( 𝒞 ⁡ ( 2 m 1, 2 m 2)) ≤ 1 2. \dim_{H}({\cal E}^{(2)}({\mathbb{Z}}_{3}))=\sup_{0\leq m_{1}<m_{2}}\dim_{H}({\cal C}(2^{m_{1}},2^{m_{2}}))\leq\frac{1}{2}. |  |

To establish the lower bound, we use the fact that 4 = ( 11) 3 4=(11)_{3}. Then the set

 | Σ A:= { λ = ( ⋯ d 2 d 1 d 0) 3: all blocks d 2 ​ n + 1 d 2 ​ n ∈ { 00, 01 } } ⊂ Σ 3, 2 ¯, \Sigma_{A}:=\{\lambda=(\cdots d_{2}d_{1}d_{0})_{3}:~\mbox{all~blocks}~d_{2n+1}d_{2n}\in\{00,01\}~\}\subset\Sigma_{3,\bar{2}}, |  |

satisfies

 | 4 Σ A = { λ = ( ⋯ d 2 d 1 d 0) 3: all blocks d 2 ​ n + 1 d 2 ​ n ∈ { 00, 11 } } ⊂ Σ 3, 2 ¯, 4\Sigma_{A}=\{\lambda=(\cdots d_{2}d_{1}d_{0})_{3}:~\mbox{all~blocks}~d_{2n+1}d_{2n}\in\{00,11\}~\}\subset\Sigma_{3,\bar{2}}, |  |

which shows that Σ A ⊂ 𝒞 ⁡ ( 1, 4). \Sigma_{A}\subset{\cal C}(1,4). Now Σ A \Sigma_{A} is given by a Cantor set construction, which permits its Hausdorff dimension to be computed in a standard way. We obtain

 | dim H ( ℰ ( 2) ​ ( ℤ 3)) ≥ dim H ( 𝒞 ⁡ ( 1, 2 2)) ≥ dim H ( Σ A) = log 3 ⁡ ( 2) log 3 ⁡ ( 9) = 1 2 ​ log 3 ⁡ ( 2) ≈ 0.31596. \dim_{H}({\cal E}^{(2)}({\mathbb{Z}}_{3}))\geq\dim_{H}({\cal C}(1,2^{2}))\geq\dim_{H}(\Sigma_{A})=\frac{\log_{3}(2)}{\log_{3}(9)}=\frac{1}{2}\log_{3}(2)\approx 0.31596. |  |

(3) We have

 | ℰ ( 2) ​ ( ℤ 3) = ⋃ 0 ≤ m 1 < m 2 < m 3 𝒞 ⁡ ( 2 m 1, 2 m 2, 2 m 3). {\cal E}^{(2)}({\mathbb{Z}}_{3})=\bigcup_{0\leq m_{1}<m_{2}<m_{3}}{\cal C}(2^{m_{1}},2^{m_{2}},2^{m_{3}}). |  |

The upper bound dim H ( ℰ ( 3) ​ ( ℤ 3) ≤ dim H ( ℰ ( 2) ​ ( ℤ 3) CLOSE CLOSE \dim_{H}({\cal E}^{(3)}({\mathbb{Z}}_{3})\leq\dim_{H}({\cal E}^{(2)}({\mathbb{Z}}_{3}) is immediate. To establish the lower bound, we use the facts that 4 = ( 11) 3 4=(11)_{3} and 256 = ( 100111) 3 256=(100111)_{3}. Then

 | Σ B:= { λ = ( ⋯ d 2 d 1 d 0) 3: all d 6 ​ n + 5 d 6 ​ n + 4 d 6 ​ n + 3 d 6 ​ n + 2 d 6 ​ n + 1 d 6 ​ n ∈ { 000000, 000001 } } ⊂ Σ 3, 2 ¯. \Sigma_{B}:=\{\lambda=(\cdots d_{2}d_{1}d_{0})_{3}:~\mbox{all}~d_{6n+5}d_{6n+4}d_{6n+3}d_{6n+2}d_{6n+1}d_{6n}\in\{000000,000001\}~\}\subset\Sigma_{3,\bar{2}}. |  |

has

 | 4 Σ B = { λ = ( ⋯ d 2 d 1 d 0) 3: all d 6 ​ n + 5 d 6 ​ n + 4 d 6 ​ n + 3 d 6 ​ n + 2 d 6 ​ n + 1 d 6 ​ n ∈ { 000000, 000011 } } ⊂ Σ 3, 2 ¯. 4\Sigma_{B}=\{\lambda=(\cdots d_{2}d_{1}d_{0})_{3}:~\mbox{all}~d_{6n+5}d_{6n+4}d_{6n+3}d_{6n+2}d_{6n+1}d_{6n}\in\{000000,~000011\}~\}\subset\Sigma_{3,\bar{2}}. |  |

 | 256 Σ B = { λ = ( ⋯ d 2 d 1 d 0) 3: all d 6 ​ n + 5 d 6 ​ n + 4 d 6 ​ n + 3 d 6 ​ n + 2 d 6 ​ n + 1 d 6 ​ n ∈ { 000000, 100111 } } ⊂ Σ 3, 2 ¯. 256\Sigma_{B}=\{\lambda=(\cdots d_{2}d_{1}d_{0})_{3}:\mbox{all}~d_{6n+5}d_{6n+4}d_{6n+3}d_{6n+2}d_{6n+1}d_{6n}\in\{000000,100111\}~\}\subset\Sigma_{3,\bar{2}}. |  |

Thus Σ B ⊂ 𝒞 ⁡ ( 1, 4, 256) ⊂ ℰ ( 3) ​ ( ℤ 3) \Sigma_{B}\subset{\cal C}(1,4,256)\subset{\cal E}^{(3)}({\mathbb{Z}}_{3}). Now Σ B \Sigma_{B} has a Cantor set construction showing that

 | dim H ( Σ B) = log 3 ⁡ ( 2) log 3 ⁡ ( 3 6) = 1 6 ​ log 3 ⁡ ( 2) ≈ 0.10515, \dim_{H}(\Sigma_{B})=\frac{\log_{3}(2)}{\log_{3}(3^{6})}=\frac{1}{6}\log_{3}(2)\approx 0.10515, |  |

which gives the asserted lower bound.

#### Remark.

The proof of Theorem 1.5 exploited the known solutions to Erdős’s problem. Consequently this approach does not extend to give a nonzero lower bound for dim H ( ℰ ( k) ​ ( ℤ 3)) \dim_{H}({\cal E}^{(k)}({\mathbb{Z}}_{3})), for any k ≥ 4 k\geq 4. Theorem 1.7 offers more flexibility in finding ternary expansion identities for integers that could potentially yield nonzero lower bounds in these cases.

## 4 Intersections of Multiplicative Translates of the 3 3 -Adic Cantor Set: Proofs

We study the 3 3 -adic Cantor set Σ 3, 1 ¯ \Sigma_{3,\bar{1}}, defined by

 | Σ 3, 2 ¯:= { λ ∈ ℤ 3: the 3-adic digit expansion ​ ( λ) 3 ​ omits the digit 2 }. \Sigma_{3,\bar{2}}:=\{\lambda\in{\mathbb{Z}}_{3}:~\mbox{the~3-adic~digit~expansion}~(\lambda)_{3}~\mbox{omits~the~digit~2}\}. |  | (4.60) |

For integers 1 ≤ M 1 < M 2 < ⋯ < M k 1\leq M_{1}<M_{2}<\cdots<M_{k} we define the intersection set

 | 𝒞 ⁡ ( M 1, M 2, ⋯, M k) \displaystyle{\cal C}(M_{1},M_{2},\cdots,M_{k}) | : ⁣ = \displaystyle:= | { λ ∈ ℤ 3: ( M i ​ λ) 3 ​ omits the digit ​ 2 } \displaystyle\{\lambda\in{\mathbb{Z}}_{3}:~(M_{i}\lambda)_{3}~\mbox{omits~the~digit}~~2\} |  | (4.61) |

 |  | = \displaystyle= | ⋂ i = 1 k 1 M i ​ Σ 3, 1 ¯ \displaystyle\bigcap_{i=1}^{k}\frac{1}{M_{i}}\Sigma_{3,\bar{1}} |  | (4.62) |

In §3 we used integers M i = 2 m i M_{i}=2^{m_{i}} but here we allow arbitrary positive integers M i M_{i}. We study 𝒞 ⁡ ( 1, M) {\cal C}(1,M) for general M M and note first that 𝒞 ⁡ ( 1, 3 j ​ M) = 𝒞 ⁡ ( 1, M). {\cal C}(1,3^{j}M)={\cal C}(1,M).. Thus without loss of generality we may reduce to the case g ​ c ​ d ​ ( M, 3) = 1 gcd(M,3)=1. Another simple fact is the following.

###### Lemma 4.1

Let M M be a positive integer.

(1) If M ≡ 2 ( mod 3) M\equiv 2(\bmod~3) then 𝒞 ⁡ ( 1, M) = { 0 } {\cal C}(1,M)=\{0\}.

(2) If M ≡ 1 ( mod 3) M\equiv 1(\bmod~3) then 𝒞 ⁡ ( 1, M) {\cal C}(1,M) is an infinite set.

#### Proof.

(1) Suppose M ≡ 2 ( mod 3) M\equiv 2(\bmod~3). If 𝒞 ⁡ ( 1, M) ≠ { 0 } {\cal C}(1,M)\neq\{0\}, then it necessarily contains some λ \lambda with λ ≠ 0 ( mod 3) \lambda\neq 0(\bmod~3), since we may divide out any powers of 3 3, and multiplication by 3 j 3^{j} simply shifts digits to the left. Then λ ∈ Σ 3, 2 ¯ \lambda\in\Sigma_{3,\bar{2}} implies λ ≡ 1 ( mod 3) \lambda\equiv 1~(\bmod~3). Then M ​ λ ≡ 2 ( mod 3) M\lambda\equiv 2(\bmod~3) so M ​ λ ∉ Σ 3, 2 ¯ M\lambda\not\in\Sigma_{3,\bar{2}}, a contradicting membership in ( 1, M) \sc(1,M). Hence no such λ \lambda exist, and 𝒞 ⁡ ( 1, M) = { 0 } {\cal C}(1,M)=\{0\}.

(2) Suppose M ≡ 1 ( mod 3). M\equiv 1(\bmod~3). To show 𝒞 ⁡ ( 1, M) {\cal C}(1,M) is an infinite set it suffices to exhibit one nonzero element λ ∈ 𝒞 ∗ ​ ( 1, M) \lambda\in{\cal C}^{\ast}(1,M), because 3 j ​ λ ∈ 𝒞 ∗ ​ ( 1, M) 3^{j}\lambda\in{\cal C}^{\ast}(1,M) for all j ≥ 0 j\geq 0. We may construct such an element λ = ( ⋯ d 2 d 1 d 0) 3 \lambda=(\cdots d_{2}d_{1}d_{0})_{3} recursively, starting with the choice d 0 = 1 d_{0}=1. Write M = ∑ j = 0 n a j ​ 3 j M=\sum_{j=0}^{n}a_{j}3^{j}, with a 0 = 1 a_{0}=1. Let M ​ λ = ∑ j = 0 ∞ c j ​ 3 j M\lambda=\sum_{j=0}^{\infty}c_{j}3^{j}. Then the k k -th digit satisfies

 | c k ≡ d k + ( ∑ j = 1 n a j ​ d n − j) + e k − 1 ( mod 3) c_{k}\equiv d_{k}+\left(\sum_{j=1}^{n}a_{j}d_{n-j}\right)+e_{k-1}~(\bmod~3) |  |

(with the convention d − 1 = d − 2 = ⋯ = d − n = 0 d_{-1}=d_{-2}=\cdots=d_{-n}=0), and with e k − 1 e_{k-1} encoding the ”carry digit” information, from the previous terms, which is completely determined by ( d 0, d 1, …, d k − 1.) (d_{0},d_{1},...,d_{k-1}.) Since we have two choices 0 0, 1 1 for d k d_{k}, at least one of them will foce c k ≠ 2 ( mod 3). c_{k}\neq 2~(\bmod~3). Thus we can recursively construct an admissible λ \lambda by induction on k k. .

It is possible to make a detailed analysis of the structure of 𝒞 ⁡ ( 1, M) {\cal C}(1,M) with M ≡ 1 ( mod 3) M\equiv 1~(\bmod~3), and determine their Hausdorff dimensions, which we consider elsewhere. One can show that infinite set 𝒞 ⁡ ( 1, M) {\cal C}(1,M) can be either countable or uncountable, e.g. 𝒞 ⁡ ( 1, 49) {\cal C}(1,49) is countably infinite, while 𝒞 ⁡ ( 1, 7) {\cal C}(1,7) is uncountable.

Now we upper bound the Hausdorff dimension of 𝒞 ⁡ ( 1, M) {\cal C}(1,M). For M = 3 j, ( j ≥ 0) M=3^{j},~(j\geq 0) we have 𝒞 ⁡ ( 1, 3 j) = Σ 3, 2 ¯ {\cal C}(1,3^{j})=\Sigma_{3,\bar{2}}, whence dim H ( 𝒞 ⁡ ( 1, 3 j)) = log 3 ⁡ ( 2) ≈ 0.63 \dim_{H}({\cal C}(1,3^{j}))=\log_{3}(2)\approx 0.63. The following result treats all other M ≥ 1 M\geq 1.

#### Proof of Theorem 1.6.

We suppose that M > 1 M>1 is an integer that is not a power of 3 3, i.e. its ternary expansion ( M) 3 (M)_{3} contains at least two nonzero ternary digits. Our object is to upper bound the Hausdorff dimension of

 | 𝒞 ⁡ ( 1, M):= Σ 3, 2 ¯ ∩ M ​ Σ 3, 2 ¯, {\cal C}(1,M):=\Sigma_{3,\bar{2}}\cap M\Sigma_{3,\bar{2}}, |  |

by 1 2 \frac{1}{2}. By the discussion above we may reduce to the case that g ​ c ​ d ​ ( M, 3) = 1 gcd(M,3)=1, and by Lemma 4.1 we may suppose M ≡ 1 ( mod 3), M\equiv 1~(\bmod~3), since the Hausdorff dimension is 0 0 if M ≡ 2 ( mod 3). M\equiv 2(\bmod~3). Thus we can write

 | ( M) 3 = b 0 + b m ​ 3 m + ∑ j = m + 1 n b j ​ 3 j, b j ∈ { 0, 1, 2 }, with ​ b 0 ​ b m ≠ 0. (M)_{3}=b_{0}+b_{m}3^{m}+\sum_{j=m+1}^{n}b_{j}3^{j},~~~b_{j}\in\{0,1,2\},~\mbox{with}~~b_{0}b_{m}\neq 0. |  | (4.63) |

and b 0 = 1 b_{0}=1, where the m m -th digit is the first nonzero ternary digit after the 0 0 -th digit.

We will study the minimal covers of 𝒞 ⁡ ( 1, M) {\cal C}(1,M) with 3 3 -adic open sets of measure 3 − r − 1 3^{-r-1} that specify the first r + 1 r+1 digits of the 3 3 -adic expansion of a number λ ∈ 𝒞 ⁡ ( 1, M) \lambda\in{\cal C}(1,M). These sets are congruence classes ( mod 3 r + 1) (\bmod~3^{r+1}) and they have diameter 3 − ( r + 1). 3^{-(r+1)}. We call a congruence class λ ( mod 3 r + 1) \lambda~(\bmod~3^{r+1}) admissible if 𝒞 ∗ ​ ( 1, M) {\cal C}^{\ast}(1,M) contains at least one element in this congruence class. Our object is to bound above the number of admissible congruence classes λ ( mod 3 r + 1) \lambda~(\bmod~3^{r+1})

Set λ = ∑ j = 0 ∞ d j ​ 3 j ∈ Σ 3, 2 ¯ \lambda=\sum_{j=0}^{\infty}d_{j}3^{j}\in\Sigma_{3,\bar{2}}, so that each d j = 0 d_{j}=0 or 1 1. Now define the digits a j a_{j} by

 | M ​ λ = ∑ j = 0 ∞ a j ​ 3 j, a j ∈ { 0, 1, 2 }. M\lambda=\sum_{j=0}^{\infty}a_{j}3^{j},~~~a_{j}\in\{0,1,2\}. |  |

The condition that M ​ λ ∈ Σ 3, 2 ¯ M\lambda\in\Sigma_{3,\bar{2}} means each a j = 0 a_{j}=0 or 1 1 which imposes extra constraints on the d j d_{j} ’s.

Claim 1. Suppose that ( d 0, d 1, …, d 2 ​ l ​ m + k − 1) (d_{0},d_{1},...,d_{2lm+k-1}) with 0 ≤ k < m 0\leq k<m of λ ∈ 𝒞 ⁡ ( 1, M) \lambda\in{\cal C}(1,M) are fixed. Then at least one of the following conditions holds:

(i) There is at most one admissible value for d 2 ​ l ​ m + k d_{2lm+k} in λ ( mod 3 2 ​ l ​ m + k + 1) \lambda~(\bmod~3^{2lm+k+1}).

(ii) There are two admissible values for d 2 ​ l ​ m + k d_{2lm+k} for λ ( mod 3 2 ​ l ​ m + k + 1) \lambda~(\bmod~3^{2lm+k+1}) and for any fixed choices of ( d 2 ​ l ​ m + k + 1, d 2 ​ l ​ m + k + 2, …, d ( 2 ​ l + 1) ​ m + k − 1) (d_{2lm+k+1},d_{2lm+k+2},...,d_{(2l+1)m+k-1}) at most three of the four possible values of ( d 2 ​ l ​ m + k, d ( 2 ​ l + 1) ​ m + k) (d_{2lm+k},d_{(2l+1)m+k}) give admissible sequences for λ ( mod 3 ( 2 ​ l + 1) ​ m + k). \lambda~(\bmod~3^{(2l+1)m+k}).

To prove the claim, suppose that condition (i) doesn’t hold. We then examine the digit a ( 2 ​ l + 1) ​ m + k a_{(2l+1)m+k} using

 | M ​ λ \displaystyle M\lambda | ≡ \displaystyle\equiv | b 0 ​ d ( 2 ​ l + 1) ​ m + k ​ 3 ( 2 ​ l + 1) ​ m + k + b m ​ d ( 2 ​ l + m) + k ​ 3 ( 2 ​ l + 1) ​ m + k \displaystyle b_{0}d_{(2l+1)m+k}3^{(2l+1)m+k}+b_{m}d_{(2l+m)+k}3^{(2l+1)m+k} |  | (4.64) |

 |  |  | + M ⁡ ( ∑ j = 0 2 ​ l ​ m + k − 1 d j ​ 3 j) + b 0 ​ d 2 ​ l ​ m + k ​ 3 2 ​ l ​ m + k ( mod 3 ( 2 ​ l + 1) ​ m + k + 1). \displaystyle~~~~~+M(\sum_{j=0}^{2lm+k-1}d_{j}3^{j})+b_{0}d_{2lm+k}3^{2lm+k}~(\bmod~3^{(2l+1)m+k+1}). |  |

Define the digits r j r_{j} by

 | M ⁡ ( ∑ j = 0 2 ​ l ​ m + k − 1 d j ​ 3 j) = ∑ j = 0 ∞ r j ​ 3 j, r j ∈ { 0, 1, 2 }. M(\sum_{j=0}^{2lm+k-1}d_{j}3^{j})=\sum_{j=0}^{\infty}r_{j}3^{j},~~~r_{j}\in\{0,1,2\}. |  |

We assert that ( 4.64) then gives the congruence

 | a ( 2 ​ l + 1) ​ m + k ≡ b 0 ​ d ( 2 ​ l + 1) ​ m + k + b m ​ d 2 ​ l ​ m + k + r ( 2 ​ l + l) ​ m + k ( mod 3). a_{(2l+1)m+k}\equiv b_{0}d_{(2l+1)m+k}+b_{m}d_{2lm+k}+r_{(2l+l)m+k}~(\bmod~3). |  | (4.65) |

That is, we assert there cannot be any extra ”carry digit” from lower order terms that affects the ( 2 ​ l + 1) ​ m + k (2l+1)m+k -th 3 3 -adic digit, coming from the addition of b 0 ​ d 2 ​ l ​ m + k ​ 3 2 ​ m + k b_{0}d_{2lm+k}3^{2m+k} in ( 4.64). Namely, the extra term b 0 ​ d 2 ​ l ​ m + k ​ 3 k b_{0}d_{2lm+k}3^{k}, where d 2 ​ l ​ m + k = 0 d_{2lm+k}=0 or 1 1 contributes nothing if d 2 ​ l ​ m + k = 0 d_{2lm+k}=0, while if d 2 ​ l ​ m + k = 1 d_{2lm+k}=1 By our assumption that (i) doesn’t hold, both values d 2 ​ l ​ m + k = 0, 1 d_{2lm+k}=0,1 occur for admissible λ ( mod 3 2 ​ l ​ m + k) \lambda(\bmod~3^{2lm+k}) for these digits. Since b 0 = 1 b_{0}=1 and the 3 3 -adic digit of M ​ λ M\lambda in the ( 2 ​ l ​ m + k + 1) (2lm+k+1) -st place is 0 0 or 1 1, this digit must have been 0 0 when d 2 ​ l ​ m + k = 0 d_{2lm+k}=0, and 1 1 when d 2 ​ l ​ m + k = 1 d_{2lm+k}=1, so there can be no ”carry digit” in the addition of b 0 ​ d 2 ​ l ​ m + k ​ 3 k b_{0}d_{2lm+k}3^{k}, as asserted.

Now consider the pairs ( d 2 ​ l ​ m + k, d ( 2 ​ l + 1) ​ m + k) (d_{2lm+k},d_{(2l+1)m+k}). Of the four values ( 00), ( 01), ( 10), ( 11) (00),(01),(10),(11) that these may take, the quantities b 0 ​ d ( 2 ​ l + 1) ​ m + k + b m ​ d 2 ​ l ​ m + k b_{0}d_{(2l+1)m+k}+b_{m}d_{2lm+k} with b 0 = 1 b_{0}=1 and b m = 1 b_{m}=1 or 2 2 will cover all residue classes ( mod 3). (\bmod~3). In particular, at least one choice will result in a ( 2 ​ l + 1) ​ m + k ≡ 2 ( mod 3) a_{(2l+1)m+k}\equiv 2~(\bmod~3) in ( 4.65), and so give a non-admissible set of digits ( mod 3 ( 2 ​ l + 1) ​ m + k) (\bmod~3^{(2l+1)m+k}). This proves (ii), and the claim.

Claim 2. For M M having the ternary expansion ( 4.63) and a given r ≥ 2 ​ m r\geq 2m there are are at most 3 1 2 ​ r + 2 ​ m 3^{\frac{1}{2}r+2m} admissible congruence classes in 𝒞 ⁡ ( 1, M) {\cal C}(1,M) ( mod 3 r) (\bmod~3^{r}).

To prove the claim, we group the 3 3 -adic digits in pairs ( d 2 ​ j ​ m + k, d OPEN ( 2 ​ j + 1) ​ m + k)) (d_{2jm+k},d_{(2j+1)m+k)}), 0 ≤ k < m 0\leq k<m, for all pairs with ( 2 ​ j + 1) ​ m + k ≤ r (2j+1)m+k\leq r. There are at most 2 ​ m − 1 2m-1 unpaired digits. Claim 1 1 establishes that, conditional on the choice of all other allowed digits, there are at most three permitted choices for the set of paired digits. For each unpaired digit there are at most two choices for its value. Since the number of paired digits is at most 1 2 ​ ( r + 1) \frac{1}{2}(r+1) the total number of admissible sequences ( mod 3 r + 1) (\bmod~3^{r+1}) is at most 3 1 2 ​ ( r + 1) ​ 2 2 ​ m − 1 3^{\frac{1}{2}(r+1)}2^{2m-1}, which implies Claim 2.

To conclude the proof, Claim 2 implies that we have a covering ℐ r {\cal I}_{r} of 𝒞 ⁡ ( 1, M) {\cal C}(1,M) with a set of at most 3 ( 1 2 ​ r + 2 ​ m CLOSE 3^{(\frac{1}{2}r+2m} sets, each of diameter 3 − ( r + 1). 3^{-(r+1)}. For each ϵ > 0 \epsilon>0 this covering satisfies

 | ∑ I ∈ ℐ r | I | 1 2 + ϵ ≤ 3 ( 1 2 ​ r + 2 ​ m CLOSE ​ ( 3 − ( r + 1)) 1 2 + ϵ ≤ 3 − ( r + 1) ​ ϵ. \sum_{I\in{\cal I}_{r}}|I|^{\frac{1}{2}+\epsilon}\leq 3^{(\frac{1}{2}r+2m}(3^{-(r+1)})^{\frac{1}{2}+\epsilon}\leq 3^{-(r+1)\epsilon}. |  |

Letting r → ∞ r\to\infty, this bound implies dim H ( 𝒞 ⁡ ( 1, M)) ≤ 1 2 + ϵ. \dim_{H}({\cal C}(1,M))\leq\frac{1}{2}+\epsilon. Letting ϵ → 0 \epsilon\to 0 gives the result.

We do not know whether the bound in Theorem 1.5 is sharp. However it is possible to show that 𝒞 ⁡ ( 1, 7) {\cal C}(1,7) has dim H 𝒞 ⁡ ( 1, 7) = log 3 ⁡ ( 1 + 5 2) ≈ 0.43 \dim_{H}{\cal C}(1,7)=\log_{3}(\frac{1+\sqrt{5}}{2})\approx 0.43.

#### Proof of Theorem 1.7.

We suppose are given N N a positive integer with N ∈ Σ 3, 2 ¯ ​ ∫ ℤ N\in\Sigma_{3,\bar{2}}\int{\mathbb{Z}} and 1 ≤ M 1 < M 2 < ⋯ < M k 1\leq M_{1}<M_{2}<\cdots<M_{k} with all N ​ M i ∈ Σ 3, 2 ¯. NM_{i}\in\Sigma_{3,\bar{2}}. Our object is to obtain an explicit nonzero lower bound on the Hausdorff dimension dim H ( 𝒞 ⁡ ( M 1, M 2, ⋯, M k)) \dim_{H}({\cal C}(M_{1},M_{2},\cdots,M_{k})). We set n n equal to the number of ternary digits in N ​ M k NM_{k}, so that n = ⌈ log 3 ⁡ N ​ M k ⌉. n=\lceil\log_{3}NM_{k}\rceil. Now we consider the set

 | Σ C:= { λ = ( ⋯ d 2 d 1 d 0) 3: all blocks d ( k + 1) ​ n − 1 ⋯ d k ​ n + 1 d k ​ n ∈ { 0 n, ( N) 3 } } ⊂ Σ 3, 2 ¯. \Sigma_{C}:=\{\lambda=(\cdots d_{2}d_{1}d_{0})_{3}:~\mbox{all~blocks}~~d_{(k+1)n-1}\cdots d_{kn+1}d_{kn}\in\{0^{n},~(N)_{3}\}~\}\subset\Sigma_{3,\overline{2}}. |  |

Since each N ​ M j ∈ Σ 3, 2 ¯ NM_{j}\in\Sigma_{3,\bar{2}} is an integer with at most n n ternary digits, we have

 | M j Σ C:= { λ = ( ⋯ d 2 d 1 d 0) 3: all blocks d ( k + 1) ​ n − 1 ⋯ d k ​ n + 1 d k ​ n ∈ { 0 n, ( N M j) 3 } } ⊂ Σ 3, 2 ¯. M_{j}\Sigma_{C}:=\{\lambda=(\cdots d_{2}d_{1}d_{0})_{3}:~\mbox{all~blocks}~d_{(k+1)n-1}\cdots d_{kn+1}d_{kn}\in\{0^{n},~(NM_{j})_{3}\}~\}\subset\Sigma_{3,\bar{2}}. |  |

Thus Σ C ⊂ 𝒞 ⁡ ( M 1, M 2, ⋯, M k) \Sigma_{C}\subset{\cal C}(M_{1},M_{2},\cdots,M_{k}). By inspection Σ C \Sigma_{C} is a Cantor set which has Hausdorff dimension

 | dim H Σ C = log 3 ⁡ ( 2) log 3 ⁡ ( 3 n) = log 3 ⁡ ( 2) ⌈ log 3 ⁡ ( N ​ M k) ⌉, \dim_{H}\Sigma_{C}=\frac{\log_{3}(2)}{\log_{3}(3^{n})}=\frac{\log_{3}(2)}{\lceil\log_{3}(NM_{k})\rceil}, |  |

and the result follows. .

## 5 Furstenberg Conjecture and Transversality of Semigroup Actions

In 1970 Furstenberg [10, p. 43] formulated the following conjecture which is in the same direction as Erdős’s question.

#### Conjecture 𝟐 ′ {\bf 2}^{{}^{\prime}}.

(Furstenberg) Suppose p p and q q are not powers of the same integer. Then the expansions to the base B = p ​ q B=pq of the powers { ( p n) p ​ q: n ≥ 1 } \{(p^{n})_{pq}:n\geq 1\} have the property that any given finite pattern of consecutive base B B digits occurs in ( p n) p ​ q (p^{n})_{pq} for all sufficiently large n n.

For example, for p = 2 p=2 and q = 3 q=3, this conjecture asserts that any given pattern of base B = 6 B=6 digits will occur as consecutive digits in the base 6 6 expansion of ( 2 n) 6 (2^{n})_{6}, for all sufficiently large n n. The restriction to products B = p ​ q B=pq of two (or more) multiplicatively independent elements was motivated by results in Furstenberg’s seminal work [9]. There he showed that for any irrational number θ \theta the set { p m q n θ ( m o d 1): m, n ≥ 0 } \{p^{m}q_{n}\theta(mod~1):m,n\geq 0\} is dense on the torus ℝ / ℤ {\mathbb{R}}/{\mathbb{Z}}. However it is well known that there is an uncountable set of irrational numbers θ \theta for which { p m ​ θ: m ≥ 0 } \{p^{m}\theta:m\geq 0\} is not dense on the torus.

Conjecture E in the introduction proposes nevertheless that Furstenberg’s conjecture continues to hold when the base B = q B=q is a prime (in the special case p = 2 p=2, q = 3 q=3). More generally one can ask whether Furstenberg’s conjecture might be valid more generally for base B B expansions for arbitrary B B with g ​ c ​ d ​ ( B, p) = 1 gcd(B,p)=1.

A main object of Furstenberg [10] was to introduce a notion of transversality of two semigroups of transformations 𝒮 1 {\cal S}_{1} and 𝒮 2 {\cal S}_{2} acting on a compact metric space X X with respect to a (suitable) dimension function d ​ i ​ m ​ ( A) dim(A) defined on all closed sets A A.

###### Definition 5.1

Two closed sets A A and B B in a compact metric space X X are transverse (for a given dimension function) if

 | d ​ i ​ m ​ ( A ∩ B) ≤ max ⁡ ( d ​ i ​ m ​ ( A) + d ​ i ​ m ​ ( B) − d ​ i ​ m ​ ( X), 0). dim(A\cap B)\leq\max(dim(A)+dim(B)-dim(X),0). |  |

###### Definition 5.2

Two semigroups 𝒮 1 {\cal S}_{1} and 𝒮 2 {\cal S}_{2} acting on a compact metric space X X are transverse (for a given dimension function) if any closed 𝒮 1 {\cal S}_{1} -invariant set A A and any closed 𝒮 2 {\cal S}_{2} -invariant set B B are themselves transverse, for that dimension function.

He obtained as an immediate consequence of this definition the following result concerning simultaneous invariant sets ( [10, p. 42]), which draws on earlier work ( [9]).

###### Proposition 5.1

(Furstenberg) Suppose that 𝒮 1 {\cal S}_{1} and 𝒮 2 {\cal S}_{2} are transverse semigroups acting on a compact metric space X X, and that 𝒮 1 {\cal S}_{1} has the additional property:

(*) If A A is a closed 𝒮 1 {\cal S}_{1} -invariant set with d ​ i ​ m ​ ( A) = d ​ i ​ m ​ ( X) dim(A)=dim(X), then A = X A=X.

Then any proper closed subset of X X invariant under both 𝒮 1 {\cal S}_{1} and 𝒮 2 {\cal S}_{2} has d ​ i ​ m ​ ( A) = 0 dim(A)=0.

Furstenberg does not construct any transverse semigroups, but as evidence for their existence shows for the following pair of tranformation semigroups that their (nontrivial) simultaneously invariant closed sets satisfy this property ( [10, Theorem 3]).

###### Proposition 5.2

(Furstenberg) Let ℤ r {\mathbb{Z}}_{r} be the ring of r r -adic integers, and suppose that r = p ​ q r=pq with p > 1 p>1 and q > 1 q>1 not both powers of the same integer. Define transformations D s ​ ( x) = ⌊ x s ⌋ D_{s}(x)=\lfloor\frac{x}{s}\rfloor, for s = p, q, s=p,q, and p ​ q pq, and note that D p ​ q = D p ​ D q = D q ​ D p D_{pq}=D_{p}D_{q}=D_{q}D_{p}. Let 𝒮 p {\cal S}_{p} and 𝒮 q {\cal S}_{q} denote the semigroups generated by D p D_{p} and D q D_{q}, respectively. If A A is a simultaneously 𝒮 p {\cal S}_{p} and 𝒮 q {\cal S}_{q} invariant proper closed subset of ℤ r {\mathbb{Z}}_{r}, then A A has Hausdorff dimension zero.

The proof of this result draws on his earlier work ( [9]). Furstenberg [10, p. 45] goes on to conjecture that 𝒮 p {\cal S}_{p} and 𝒮 q {\cal S}_{q} are transverse semigroups acting on ℤ r {\mathbb{Z}}_{r}.

Conjectures A and B in the introduction are partially motivated by Furstenberg’s framework but fall outside it. One could approach Conjecture A by considering only the ternary expansions of fractional parts { { λ ​ 2 n } } \{\{\lambda 2^{n}\}\}, and thus iterating x → 2 ​ x x\to 2x on the compact space X = ℝ / ℤ X={\mathbb{R}}/{\mathbb{Z}}. This defines a larger exceptional set ℰ ⁡ ( ℝ / ℤ) {\cal E}({\mathbb{R}}/{\mathbb{Z}}), which contains ℰ ⁡ ( ℝ) {\cal E}({\mathbb{R}}). Does ℰ ⁡ ( ℝ / ℤ) {\cal E}({\mathbb{R}}/{\mathbb{Z}}) have Hausdorff dimension zero? This set includes all dyadic rationals (thus λ = 1 \lambda=1), which is a dense set in ℝ / ℤ {\mathbb{R}}/{\mathbb{Z}}, so its closure is the whole space X X, and is not covered by Furstenberg’s results.

Furstenberg’s formulation does not apply to semigroups of transformations on the real numbers because ℝ {\mathbb{R}} is not compact. One may ask: Can Furstenberg’s framework be generalized to apply to semigroups of operators acting on the real numbers, or the integers?

## 6 Concluding Remarks

We conclude by reviewing some history related to Erdős’s question. Erdős [4] raised his question on ternary expansions of 2 n 2^{n} in connection with his conjecture that the binomial coefficient ( 2 ​ n n) {{2n}\choose{n}} is not squarefree for all n ≥ 5 n\geq 5. This binomial coefficient is divisible by 4 4 except for n = 2 k n=2^{k}, so it is natural to examine when larger primes divide ( 2 k + 1 2 k) {{2^{k+1}}\choose{2^{k}}}. Here one has

 | 3 ​ does not divide ​ ( 2 k + 1 2 k) ⟺ The ternary expansion of ​ 2 n ​ omits the digit ​ 2, 3~\mbox{does~not~divide}~{{2^{k+1}}\choose{2^{k}}}\Longleftrightarrow\mbox{The~ternary~ expansion ~of}~2^{n}~\mbox{omits the digit}~2, |  |

as follows from Lucas’s theorem (Lucas [16], see Graham et al. [14, Exercise 5.61]). This led Erdős to raise his ternary expansion question, since a positive answer to it would establish his binomial coefficient conjecture.

As it turned out, Erdős’s binomial coefficient conjecture was later resolved affirmatively, without answering the ternary expansion question. In 1985 Sarkozy [21] proved that ( 2 ​ n n) {{2n}\choose{n}} is not squarefree for all sufficiently large n n. About 1995, Granville and Ramaré [11] and, independently, Velammal [24] proved it for all n ≥ 5 n\geq 5.

The theme of this paper is that Erdős’s unconventional question retains interest for its own sake, even though the problem that originally motivated its study has been solved.

## References

- [1] A. Baker, Transcendental Number Theory, Cambridge University Press: Cambridge 1975
- [2] A. Dubickas, Arithmetical properties of powers of algebraic integers, Bull. Lond. Math. Soc. 38 (2006), 70–80.
- [3] A. Dubickas and A. Novikas, Integer parts of powers of rational numbers, Math. Z. 251 (2005), 635–648.
- [4] P. Erdős, Some unconventional problems in number theory, Math. Mag. 52, No. 2 (1979), 67–70.
- [5] P. Erdős and R. L. Graham, Old and New Problems and Results in Combinatorial Number Theory, Monograph No. 28 de L’Enseign. Math., Univ. of Geneva 1980.
- [6] K. Falconer, The geometry of fractal sets, Cambridge Tracts in Mathematics No. 85, Cambridge Univ. Press: Cambridge 1985.
- [7] K. Falconer, Fractal Geometry: Mathematical Foundations and Applications, John Wiley & Sons: Chichester 1990.
- [8] L. Flatto, J. C. Lagarias and A. Pollington, On the range of fractional parts { ξ ​ ( p q) n } \{\xi(\frac{p}{q})^{n}\}, Acta Arith. 70 (1995), 125–147.
- [9] H. Furstenberg, Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation, Math. Systems Theory 1 (1967) 1–49.
- [10] H. Furstenberg, Intersections of Cantor sets and transversality of semigroups, in: Problems in Analysis: (Symposium Salomon Bochner, Princeton Univ. 1969), pp. 41–59, Princeton Univ. Press; Princeton 1970.
- [11] A. Granville and O. Ramaré, Explicit bounds on exponential sums and the scarcity of sqarefree binomial coefficients, Mathematika 43 (1996), 73–107.
- [12] H. Gupta, Powers of 2 2 and sums of distinct powers of 3 3, Univ. Beograd Publ. Elecktrotehn. Fak. Ser. Mat. Fiz. No. 602–633 (1978), 151–158. (MR 0580438)
- [13] R. K. Guy, Unsolved Problems in Number Theory, Second Edition, Springer-Verlag: New York 1994.
- [14] R. L. Graham, D. Knuth and O. Patashnik, Concrete Mathematics, Second Edition. Addison-Wesley: Reading, Mass. 1994.
- [15] D. Lind and B. Marcus, An Introduction to Symbolic Dynamics and Coding, Cambridge Univ. Press: Cambridge 1995.
- [16] E. Lucas, Sur les congruences des nombres eulériens et des coefficients différentials des fonctions trigonométriques, suivant un module premier, Bull. Soc. Math. France 6 (1878), 49–54.
- [17] R. D. Mauldin and S. C. Williams, Hausdorff dimension in graph directed constructions, Trans. Amer. Math. Soc. 309 (1988), 811–829.
- [18] W. Narkiewicz, A note on a paper of H. Gupta concerning powers of 2 2 and 3 3, Univ. Beograd Publ. Elecktrotehn. Fak. Ser. Mat. Fiz. No. 678–715 (1980), 173–174. (MR 0623247)
- [19] G. Rhin, Approximants de Padé et mesures effectives d’irrationalité, Progress in Mathematics, 71 (1987), 155–164.
- [20] C. A. Rogers, Hausdorff Measures, Cambridge University Press: Cambridge 1970. (Reprint: 1998).
- [21] A. Sárközy, On divisors of binomial coefficients I, J. Number Theory 20 (1985) , 70–80.
- [22] J. Simons and B. M. M. de Weger, Theoretical and computational bounds for m m -cycles of the 3 ​ n + 1 3n+1 problem, Acta Arith. 117 (2005), 51–70.
- [23] N. E. Slater, Gaps and steps for the sequence n ​ θ ( mod 1) n\theta~(\bmod~1), Math. Proc. Camb. Phil. Soc. 63 (1967), 1115–1123.
- [24] G. Velammal, Is the binomial coefficient ( 2 ​ n n) {{2n}\choose{n}} squarefree?, Hardy-Ramanujan J. 18 (1995), 23–45.

Jeffrey C. Lagarias
Dept. of Mathematics
The University of Michigan
Ann Arbor, MI 48109-1043
email: lagarias@umich.edu

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/math/0512005
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/math/0512006
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+math/0512006
[7]: https://arxiv.org/abs/math/0512006
[8]: /html/math/0512007
