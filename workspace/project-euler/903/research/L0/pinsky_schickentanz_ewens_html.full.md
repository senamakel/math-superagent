<!-- source: https://arxiv.org/html/2510.20654v2 | converted from HTML -->

Inversions in Random Permutations Under the Ewens Sampling Distribution With and Without a Prescribed Number of Fixed Points

# Inversions in Random Permutations Under the Ewens Sampling Distribution With and Without a Prescribed Number of Fixed Points

Ross G. Pinsky, Dominic T. Schickentanz
November 16, 2025

###### Abstract.

In the first part of the paper, we study the inversion statistic of random permutations under the family ( ℙ θ ( n)) θ ≥ 0 (\mathbb{P}_{\theta}^{(n)})_{\theta\geq 0} of Ewens sampling distributions on S n S_{n}. We obtain a rather simple exact formula for the expected number of inversions under ℙ θ ( n) \mathbb{P}_{\theta}^{(n)}. In particular, we show that this expected number of inversions is decreasing in the tilting parameter θ \theta for any n n and that it is convex in θ \theta for n ∉ { 3, 4 } n\not\in\{3,4\} only. Furthermore, we derive an exact formula for the probability that a specific pair of indices ( i, j) ∈ { 1, …, n } 2 (i,j)\in\{1,\dots,n\}^{2} is inverted and show that this probability is decreasing in θ \theta if and only if | j − i | ≥ 2 |j-i|\geq 2 holds. We also exhibit the asymptotic behavior of these quantities as n → ∞ n\to\infty and θ → ∞ \theta\to\infty.

In the second part of our paper, we analyze the inversion statistic of random permutations under ( ℙ θ ( n)) θ > 0 (\mathbb{P}_{\theta}^{(n)})_{\theta>0} conditioned on having a prescribed number of fixed points. Again, we obtain exact formulas for the expected number of inversions and for the probability that a specific pair of indices is inverted. Since, as expected, the resulting formulas are rather complicated, we focus on the asymptotic behavior of these quantities as n → ∞ n\to\infty, θ → ∞ \theta\to\infty and θ → 0 \theta\to 0.

###### Key words and phrases:

inversion; random permutation; Ewens sampling distribution; derangement; fixed point

###### 2010 Mathematics Subject Classification:

60C05, 05A05

The second named author has been supported in part by a Technion fellowship.

## 1. Introduction and Statement of Results

In this paper, we study the inversion statistic of random permutations under the family of Ewens sampling distributions, the distributions obtained by exponential tilting via the total-number-of-cycles statistic. We consider both the unconditioned Ewens sampling distributions and the Ewens sampling distributions conditioned on the permutation having a prescribed number of fixed points. Surprisingly, it does not seem that the inversion statistic has been studied even under the unconditioned Ewens sampling distributions. Our results in this regard may be thought of as the obverse of the results in [[GP18][1]] concerning cycle statistics under the Mallows distributions, the distributions obtained by exponential tilting via the inversion statistic.

Our results dealing with permutations under Ewens sampling distributions conditioned on having a prescribed number of fixed points generalize recent results of [[Pin25][2]]. In that paper, one of the present authors studied the inversion statistic under uniformly distributed random permutations conditioned on having a prescribed number of fixed points. The proofs in that paper exploited the so-called Chinese restaurant construction of a uniformly distributed random permutation. As is well-known, that construction can be modified to produce a random permutation with a Ewens sampling distribution [[Ald85][3], [Pit06][4]]. We use this construction in our proofs.

Throughout this paper, let n ∈ ℕ n\in\mathbb{N} with n ≥ 3 n\geq 3 (unless explicitly indicated otherwise) and θ ≥ 0 \theta\geq 0. As usual, we denote the set of all permutations of [n]:= { 1, …, n } [n]:=\{1,\dots,n\} by S n S_{n}. Let

 | N ​ ( π):= max ⁡ { | A |: A ⊆ [n], π m ​ ( i) ≠ j ​ for all ​ i, j ∈ A ​ with ​ i ≠ j ​ and all ​ m ∈ ℕ }, π ∈ S n, N(\pi):=\max\{|A|:A\subseteq[n],\,\pi^{m}(i)\neq j\text{ for all }i,j\in A\text{ with }i\neq j\text{ and all }m\in\mathbb{N}\},\quad\pi\in S_{n}, |  |

be the number of cycles in π \pi. Then the Ewens sampling distribution on S n S_{n} with parameter θ \theta is the probability measure ℙ θ ( n) \mathbb{P}_{\theta}^{(n)} on ( S n, 𝒫 ​ ( S n)) (S_{n},\mathcal{P}(S_{n})) defined by

 | ℙ θ ( n) ​ ( { π }):= θ N ​ ( π) θ ( n), π ∈ S n, \mathbb{P}_{\theta}^{(n)}(\{\pi\}):=\frac{\theta^{N(\pi)}}{\theta^{(n)}},\quad\pi\in S_{n}, |  |

where the normalization constant θ ( n) \theta^{(n)} is the rising factorial defined by θ ( n) = ∏ k = 0 n − 1 ( θ + k) \theta^{(n)}=\prod_{k=0}^{n-1}(\theta+k). (In the special case θ = 0 \theta=0, we understand 0 N ​ ( π) 0 ( n) \frac{0^{N(\pi)}}{0^{(n)}} to be 𝟙 N ​ ( π) = 1 ( n − 1)! \frac{\mathbbm{1}_{N(\pi)=1}}{(n-1)!}.)

As θ \theta increases, permutations with more (and hence shorter) cycles become more likely under ℙ θ ( n) \mathbb{P}_{\theta}^{(n)}, interpolating between the uniform distribution on the set of cyclic permutations for θ = 0 \theta=0 and the point measure on the identity permutation id [n] \operatorname{id}_{[n]} as θ → ∞ \theta\to\infty. Of course, ℙ 1 ( n) \mathbb{P}_{1}^{(n)} is the uniform distribution on S n S_{n}. For later use, we recall one well-known property [[ABT03][5], [Pin14][6]]: As n → ∞ n\to\infty, the number of cycles of length m ∈ ℕ m\in\mathbb{N} of a ℙ θ ( n) \mathbb{P}_{\theta}^{(n)} -distributed random permutation converges in distribution to the Poisson distribution with parameter θ m \frac{\theta}{m}. It is convenient to let Σ n: S n → S n \Sigma_{n}:S_{n}\to S_{n} denote the identity in order to have a generic ℙ θ ( n) \mathbb{P}_{\theta}^{(n)} -distributed random variable under ℙ θ ( n) \mathbb{P}_{\theta}^{(n)} at hand.

Originating from population genetics [[Ewe72][7]], Ewens sampling has been applied in several non-mathematical fields, ranging from ecology to physics. For instance, it plays a crucial role in the unified neutral theory of biodiversity. At the same time, it appears in various areas of pure mathematics, ranging from algebra and number theory to probability. We refer to [[JKB97][8]] and [[Cra16][9]] for more insights on the ubiquity of Ewens sampling.

Throughout this paper, let i, j ∈ [n] 2 i,j\in[n]^{2} with i < j i<j. We recall that the pair ( i, j) (i,j) is called an inversion under π ∈ S n \pi\in S_{n} if π − 1 ​ ( i) > π − 1 ​ ( j) \pi^{-1}(i)>\pi^{-1}(j) holds, that is, if i i appears to the right of j j in the one-line notation of π \pi. We denote by

 | Inv ⁡ ( π):= { ( i, j) ∈ [n] 2: i < j, ( i, j) ​ is an inversion }, π ∈ S n, \operatorname{Inv}(\pi):=\{(i,j)\in[n]^{2}:i<j,\ (i,j)\text{ is an inversion}\},\quad\pi\in S_{n}, |  |

the set of all inversions in the permutation π \pi. In the literature, there also is an alternative convention defining inversions through images instead of preimages. Noting Σ n − 1 ∼ Σ n \Sigma_{n}^{-1}\sim\Sigma_{n} under ℙ θ ( n) \mathbb{P}_{\theta}^{(n)}, the difference between the two conventions is irrelevant in our probabilistic framework.

### 1.1. Inversions Under (Unconditioned) Ewens Sampling

By symmetry, under the uniform distribution ℙ 1 ( n) \mathbb{P}_{1}^{(n)}, one has 𝔼 1 ( n) ​ | Inv ⁡ ( Σ n) | = 1 4 ​ n ​ ( n − 1) \mathbb{E}_{1}^{(n)}|\operatorname{Inv}(\Sigma_{n})|=\frac{1}{4}n(n-1). Would one expect 𝔼 θ ( n) ​ | Inv ⁡ ( Σ n) | \mathbb{E}_{\theta}^{(n)}|\operatorname{Inv}(\Sigma_{n})| to be larger or smaller than 𝔼 1 ( n) ​ | Inv ⁡ ( Σ n) | \mathbb{E}_{1}^{(n)}|\operatorname{Inv}(\Sigma_{n})|? Of course, this should depend on the value of θ \theta. On the one hand, recall from above that the number of fixed points in a ℙ θ ( n) \mathbb{P}_{\theta}^{(n)} -distributed permutation converges in distribution to the Poisson distribution with parameter θ \theta, as n → ∞ n\to\infty. The Poisson distributions are stochastically increasing with respect to their parameter θ \theta. Having a lot of fixed points decreases the number of inversions since each pair of fixed points automatically does not form an inversion. For large n n, this suggests that 𝔼 θ ( n) ​ | Inv ⁡ ( Σ n) | \mathbb{E}_{\theta}^{(n)}|\operatorname{Inv}(\Sigma_{n})| should be larger than 𝔼 1 ( n) ​ | Inv ⁡ ( Σ n) | \mathbb{E}_{1}^{(n)}|\operatorname{Inv}(\Sigma_{n})| for θ ∈ ( 0, 1) \theta\in(0,1) and vice versa for θ > 1 \theta>1. On the other hand, recall from above that the number of two-cycles in a ℙ θ ( n) \mathbb{P}_{\theta}^{(n)} -distributed permutation converges in distribution to the Poisson distribution with parameter θ 2 \frac{\theta}{2}, as n → ∞ n\to\infty. Having a lot of two-cycles increases the number of inversions since each pair in a two-cycle automatically forms an inversion. This would suggest the opposite conclusion from the one suggested above.

Here is our main result for unconditioned Ewens sampling distributions.

###### Theorem 1.

1. ( a) (a)

The probability that ( i, j) (i,j) is an inversion is given by

(1.1) |  | ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n)) = \displaystyle\mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}))={} | n ​ ( n − 2 ​ ( j − i) + 1) 2 ​ ( θ + n − 1) − ( n − 1) ​ ( n − 2 ​ ( j − i)) 2 ​ ( θ + n − 2). \displaystyle\frac{n(n-2(j-i)+1)}{2(\theta+n-1)}-\frac{(n-1)(n-2(j-i))}{2(\theta+n-2)}. |  |

As a function of θ ≥ 0 \theta\geq 0, this probability is (strictly) decreasing if and only if j − i ≥ 2 j-i\geq 2 holds.

2. ( b) (b)

The expected number of inversions under ℙ θ ( n) \mathbb{P}_{\theta}^{(n)} is given by

(1.2) |  | 𝔼 θ ( n) ​ | Inv ⁡ ( Σ n) | = \displaystyle\mathbb{E}_{\theta}^{(n)}|\operatorname{Inv}(\Sigma_{n})|={} | ( n + 1) ​ n 2 ​ ( n − 1) 12 ​ ( θ + n − 1) − n ​ ( n − 1) 2 ​ ( n − 2) 12 ​ ( θ + n − 2), \displaystyle\frac{(n+1)n^{2}(n-1)}{12(\theta+n-1)}-\frac{n(n-1)^{2}(n-2)}{12(\theta+n-2)}, |  |

which is strictly decreasing in θ ≥ 0 \theta\geq 0. It is a (strictly) convex function of θ \theta if and only if n ∉ { 3, 4 } n\not\in\{3,4\} holds.

The theorem immediately yields the following asymptotic behavior as n → ∞ n\to\infty for the quantities on the left-hand sides of ( [1.1][10]) and ( [1.2][11]).

###### Corollary 2.

1. ( a) (a)

Let ( i n) n, ( j n) n ⊆ ℕ (i_{n})_{n},(j_{n})_{n}\subseteq\mathbb{N} be sequences with i n < j n ≤ n i_{n}<j_{n}\leq n for all n ∈ ℕ n\in\mathbb{N}. For any fixed θ ≥ 0 \theta\geq 0, we have

 | ℙ θ ( n) ​ ( ( i n, j n) ∈ Inv ⁡ ( Σ n)) \displaystyle\mathbb{P}_{\theta}^{(n)}((i_{n},j_{n})\in\operatorname{Inv}(\Sigma_{n})) |  |

 | = 1 2 − ( θ − 1) ​ ( j n − i n) n 2 − ( θ − 1) ​ ( θ − 2) 2 ​ n 2 + ( 2 ​ θ − 3) ​ ( θ − 1) ​ ( j n − i n) n 3 + O ​ ( 1 n 3), n → ∞. \displaystyle\qquad=\frac{1}{2}-\frac{(\theta-1)(j_{n}-i_{n})}{n^{2}}-\frac{(\theta-1)(\theta-2)}{2n^{2}}+\frac{(2\theta-3)(\theta-1)(j_{n}-i_{n})}{n^{3}}+O\left(\frac{1}{n^{3}}\right),\quad n\to\infty. |  |

2. ( b) (b)

For any fixed θ ≥ 0 \theta\geq 0, we have

(1.3) |  | 𝔼 θ ( n) ​ | Inv ⁡ ( Σ n) | = \displaystyle\mathbb{E}_{\theta}^{(n)}|\operatorname{Inv}(\Sigma_{n})|={} | n ​ ( n − 1) 4 − θ − 1 6 ​ n + θ ​ ( θ − 1) 12 + O ​ ( 1 n 2), n → ∞. \displaystyle\frac{n(n-1)}{4}-\frac{\theta-1}{6}n+\frac{\theta(\theta-1)}{12}+O\left(\frac{1}{n^{2}}\right),\quad n\to\infty. |  |

Note that there is no term of order 1 n \frac{1}{n} in the expansion of the expected number of inversions.

###### Remark 3.

In [[Pin25][2]], it was shown that the expected number of inversions in a random permutation in S n S_{n} distributed according to the uniform distribution conditioned on the permutation having m ∈ ℕ 0 m\in\mathbb{N}_{0} fixed points is given by

 | n ​ ( n − 1) 4 − m − 1 6 ​ n − m 2 − m − 1 12 + O ​ ( 1 ( n − m − 1)!), n → ∞. \frac{n(n-1)}{4}-\frac{m-1}{6}n-\frac{m^{2}-m-1}{12}+O\left(\frac{1}{(n-m-1)!}\right),\quad n\to\infty. |  |

From the Chinese restaurant construction, it follows easily that the expected number of fixed points of Σ n \Sigma_{n} under ℙ θ ( n) \mathbb{P}_{\theta}^{(n)} is equal to θ \theta. Note that if one sets θ = m \theta=m in ( [1.3][12]), one finds that the asymptotic expansions in powers of n n for the expected number of inversions under the two measures coincide up to the O ​ ( 1) O(1) -term, where they differ.

We may also allow θ \theta to depend on n n. Given c > 0 c>0, a simple analysis of ( [1.2][11]) yields

 | 𝔼 c ​ n α ( n) ​ | Inv ⁡ ( Σ n) | ∼ { 1 3 ​ c ​ n 3 − α, α > 1, 4 ​ c + 3 12 ​ ( c + 1) 2 ​ n 2, α = 1, 1 4 ​ n 2, α < 1, n → ∞. \displaystyle\mathbb{E}_{cn^{\alpha}}^{(n)}|\operatorname{Inv}(\Sigma_{n})|\sim\begin{cases}\dfrac{1}{3c}n^{3-\alpha},\quad&\alpha>1,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \dfrac{4c+3}{12(c+1)^{2}}n^{2},\quad&\alpha=1,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \dfrac{1}{4}n^{2},\quad&\alpha<1,\\ \end{cases}\qquad\quad n\to\infty. |  |

In particular, we have lim n → ∞ 𝔼 c ​ n α ( n) ​ | Inv ⁡ ( Σ n) | = 0 \lim_{n\to\infty}\mathbb{E}_{cn^{\alpha}}^{(n)}|\operatorname{Inv}(\Sigma_{n})|=0 if and only if α > 3 \alpha>3. However, one can in fact show that lim n → ∞ ℙ c ​ n α ( n) ​ ( Σ n = id [n]) = 1 \lim_{n\to\infty}\mathbb{P}_{cn^{\alpha}}^{(n)}(\Sigma_{n}=\operatorname{id}_{[n]})=1 is equivalent to α > 2 \alpha>2. This follows from the the definition of the Ewens sampling distribution by taking the logarithm and applying the mean value theorem.

For fixed n n, Theorem [1][13] extends formulas, previously known in the elementary special cases θ ∈ { 0, 1 } \theta\in\{0,1\} only, to the whole parameter range θ ≥ 0 \theta\geq 0. For θ = 1 \theta=1, we recover

 | ℙ 1 ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n)) = 1 2 and 𝔼 1 ( n) ​ | Inv ⁡ ( Σ n) | = n ​ ( n − 1) 4. \mathbb{P}_{1}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}))=\frac{1}{2}\qquad\text{and}\qquad\mathbb{E}_{1}^{(n)}|\operatorname{Inv}(\Sigma_{n})|=\frac{n(n-1)}{4}. |  |

For θ = 0 \theta=0, we recover

 | ℙ 0 ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n)) = 1 2 + j − i − 1 ( n − 1) ​ ( n − 2) and 𝔼 0 ( n) ​ | Inv ⁡ ( Σ n) | = n ​ ( 3 ​ n − 1) 12, \mathbb{P}_{0}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}))=\frac{1}{2}+\frac{j-i-1}{(n-1)(n-2)}\qquad\text{and}\qquad\mathbb{E}_{0}^{(n)}|\operatorname{Inv}(\Sigma_{n})|=\frac{n(3n-1)}{12}, |  |

the latter being equivalent to OEIS sequence A227404, which counts the total number of inversions in all single cycle permutations of order n n.

At the other end of the parameter range, Theorem [1][13] implies the previously unknown asymptotics

(1.4) |  | lim θ → ∞ θ ​ ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n)) = n − ( j − i) \lim_{\theta\to\infty}\theta\mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}))=n-(j-i) |  |

and

(1.5) |  | lim θ → ∞ θ ​ 𝔼 θ ( n) ​ | Inv ⁡ ( Σ n) | = 1 4 ​ ( 2 ​ n 3). \lim_{\theta\to\infty}\theta\mathbb{E}_{\theta}^{(n)}|\operatorname{Inv}(\Sigma_{n})|=\frac{1}{4}\binom{2n}{3}. |  |

The proofs of the results presented in this subsection can be found in Section [2][14]. At the end of that section, we also provide a rather short and elementary proof of ( [1.4][15]) and ( [1.5][16]), without relying on Theorem [1][13].

### 1.2. Inversions Under Ewens Sampling With Prescribed Number of Fixed Points

We define

 | Fix ⁡ ( π):= { k ∈ [n]: π ​ ( k) = k }, π ∈ S n, \operatorname{Fix}(\pi):=\{k\in[n]:\pi(k)=k\},\quad\pi\in S_{n}, |  |

to be the set of fixed points of π \pi and set

 | D n, m:= { | Fix ⁡ ( Σ n) | = m } = { Σ n ​ has exactly ​ m ​ fixed points }, m ∈ ℤ, n ∈ ℕ. D_{n,m}:=\{|\operatorname{Fix}(\Sigma_{n})|=m\}=\{\Sigma_{n}\text{ has exactly }m\text{ fixed points}\},\quad m\in\mathbb{Z},\,n\in\mathbb{N}. |  |

In addition to our general assumption n ≥ 3 n\geq 3, we henceforth assume θ > 0 \theta>0 and m ∈ { 0, …, n − 2 } m\in\{0,\dots,n-2\} (unless explicitly indicated otherwise) to exclude trivial cases and, in particular, to ensure ℙ θ ( n) ​ ( D n, m) ∈ ( 0, 1) \mathbb{P}_{\theta}^{(n)}(D_{n,m})\in(0,1). Our aim is to analyze the inversion statistic under the conditional law ℙ θ ( n) ( ⋅ | D n, m) \mathbb{P}_{\theta}^{(n)}(\,\cdot\,|D_{n,m}). An important special case is given by m = 0 m=0, with D n, 0 D_{n,0} being the event that Σ n \Sigma_{n} is a derangement.

As a first step, we derive a formula for ℙ θ ( n) ​ ( D n, m) \mathbb{P}_{\theta}^{(n)}(D_{n,m}). While the result seems to be rather well-known for derangements, we did not find a reference for the general case. For convenience, let us set ℙ θ ( 0) ​ ( D 0, 0):= 1 \mathbb{P}_{\theta}^{(0)}(D_{0,0}):=1 (without assigning any meaning to D 0, 0 D_{0,0} or ℙ θ ( 0) \mathbb{P}_{\theta}^{(0)}) and θ ( 0):= 1 \theta^{(0)}:=1.

###### Proposition 4.

We have

 | ℙ θ ( n) ​ ( D n, m) = \displaystyle\mathbb{P}_{\theta}^{(n)}(D_{n,m})={} | ( n m) ​ θ m ​ θ ( n − m) θ ( n) ​ ℙ θ ( n − m) ​ ( D n − m, 0) \displaystyle\binom{n}{m}\frac{\theta^{m}\theta^{(n-m)}}{\theta^{(n)}}\mathbb{P}_{\theta}^{(n-m)}(D_{n-m,0}) |  |

 | = \displaystyle={} | n! ​ θ m m! ​ θ ( n) ​ ∑ k = 0 n − m ( − θ) k ​ θ ( n − m − k) k! ​ ( n − m − k)!, m ∈ { 0, …, n }, n ∈ ℕ. \displaystyle\frac{n!\theta^{m}}{m!\theta^{(n)}}\sum_{k=0}^{n-m}\frac{(-\theta)^{k}\theta^{(n-m-k)}}{k!(n-m-k)!},\qquad m\in\{0,\dots,n\},\,n\in\mathbb{N}. |  |

This proposition is complemented by the trivial observation

(1.6) |  | ℙ θ ( n) ​ ( D n, m) = 0, m ∈ ℤ ∖ { 0, …, n − 2, n }, n ∈ ℕ. \mathbb{P}_{\theta}^{(n)}(D_{n,m})=0,\quad m\in\mathbb{Z}\setminus\{0,\dots,n-2,n\},\,n\in\mathbb{N}. |  |

Under ℙ θ ( n) ( ⋅ | D n, m) \mathbb{P}_{\theta}^{(n)}(\,\cdot\,|D_{n,m}), the probability that the pair ( i, j) (i,j) is inverted and the expected number of inversions, unsurprisingly, are significantly more complicated than their unconditional analogs derived in Theorem [1][13]. For this reason, we postpone the exact formulas for these quantities to Proposition [10][17] in the proof section. Instead, our main results focus on the behavior of these quantities as n → ∞ n\to\infty, θ → ∞ \theta\to\infty or θ → 0 \theta\to 0.

We start with the asymptotics as n → ∞ n\to\infty.

###### Theorem 5.

1. ( a) (a)

Let ( i n) n, ( j n) n ⊆ ℕ (i_{n})_{n},(j_{n})_{n}\subseteq\mathbb{N} be sequences with i n < j n ≤ n i_{n}<j_{n}\leq n for all n ∈ ℕ n\in\mathbb{N}. For any fixed θ > 0 \theta>0 and m ∈ ℕ 0 m\in\mathbb{N}_{0}, we have

 | ℙ θ ( n) ​ ( ( i n, j j) ∈ Inv ⁡ ( Σ n) | D n, m) = 1 2 − \displaystyle\mathbb{P}_{\theta}^{(n)}\big((i_{n},j_{j})\in\operatorname{Inv}(\Sigma_{n})\big|D_{n,m}\big)=\frac{1}{2}- | ( m − 1) ​ ( j n − i n) n 2 − m 2 − 3 ​ m − θ + 2 2 ​ n 2 \displaystyle\frac{(m-1)(j_{n}-i_{n})}{n^{2}}-\frac{m^{2}-3m-\theta+2}{2n^{2}} |  |

 |  | + ( m 2 − 4 ​ m − θ + 3) ​ ( j n − i n) n 3 + O ​ ( 1 n 3), n → ∞. \displaystyle+\frac{(m^{2}-4m-\theta+3)(j_{n}-i_{n})}{n^{3}}+O\left(\frac{1}{n^{3}}\right),\qquad n\to\infty. |  |

2. ( b) (b)

For any fixed θ > 0 \theta>0 and m ∈ ℕ 0 m\in\mathbb{N}_{0}, the expected number of inversions under ℙ θ ( n) ( ⋅ | D n, m) \mathbb{P}_{\theta}^{(n)}(\,\cdot\,|D_{n,m}) satisfies

(1.7) |  | 𝔼 θ ( n) ​ [| Inv ⁡ ( Σ n) | | D n, m] = \displaystyle\mathbb{E}_{\theta}^{(n)}\big[|\operatorname{Inv}(\Sigma_{n})|\big|D_{n,m}\big]={} | n ​ ( n − 1) 4 − m − 1 6 ​ n − m 2 − m − θ 12 + O ​ ( 1 n), n → ∞. \displaystyle\frac{n(n-1)}{4}-\frac{m-1}{6}n-\frac{m^{2}-m-\theta}{12}+O\left(\frac{1}{n}\right),\quad n\to\infty. |  |

We emphasize that the O ​ ( n) O(n) -term in ( [1.7][18]) does not depend on θ \theta and hence is universal for the whole family of Ewens sampling distributions.

###### Remark 6.

Similar to Remark [3][19], a comparison with Corollary [2][20] seems natural. As mentioned in the introduction, we have lim n → ∞ ℙ θ ( n) ​ ( D n, m) = ℙ ​ ( Y θ = m) \lim_{n\to\infty}\mathbb{P}_{\theta}^{(n)}(D_{n,m})=\mathbb{P}(Y_{\theta}=m) for a Poisson random variable Y θ Y_{\theta} with parameter θ \theta. Formally setting m = Y θ m=Y_{\theta} in ( [1.7][18]) and then taking expectations, we observe that the resulting expansion

 | n ​ ( n − 1) 4 − 𝔼 ​ Y θ − 1 6 ​ n − 𝔼 ​ Y θ 2 − 𝔼 ​ Y θ − θ 12 + O ​ ( 1 n) = n ​ ( n − 1) 4 − θ − 1 6 ​ n − θ ​ ( θ − 1) 12 + O ​ ( 1 n) \displaystyle\frac{n(n-1)}{4}-\frac{\mathbb{E}Y_{\theta}-1}{6}n-\frac{\mathbb{E}Y_{\theta}^{2}-\mathbb{E}Y_{\theta}-\theta}{12}+O\left(\frac{1}{n}\right)=\frac{n(n-1)}{4}-\frac{\theta-1}{6}n-\frac{\theta(\theta-1)}{12}+O\left(\frac{1}{n}\right) |  |

coincides with the expansion of

 | 𝔼 θ ( n) ​ | Inv ⁡ ( Σ n) | = ∑ m ∈ ℕ 0 𝔼 θ ( n) ​ [| Inv ⁡ ( Σ n) | | D n, m] ​ ℙ θ ( n) ​ ( D n, m) \displaystyle\mathbb{E}_{\theta}^{(n)}|\operatorname{Inv}(\Sigma_{n})|=\sum_{m\in\mathbb{N}_{0}}\mathbb{E}_{\theta}^{(n)}\big[|\operatorname{Inv}(\Sigma_{n})|\big|D_{n,m}\big]\mathbb{P}_{\theta}^{(n)}(D_{n,m}) |  |

provided in ( [1.3][12]) up to the O ​ ( 1) O(1) -term, where they differ in their sign only.

###### Remark 7.

For θ = 1 \theta=1, corresponding to uniform sampling, ( [1.7][18]) is consistent with the asymptotic expansion derived in [[Pin25][2]]. In that paper, the remainder term O ​ ( 1 n) O\left(\frac{1}{n}\right) was shown to actually be O ​ ( 1 ( n − m − 1)!) O\big(\frac{1}{(n-m-1)!}\big) for θ = 1 \theta=1. We strongly believe that such an improvement is not possible for θ ≠ 1 \theta\neq 1.

Let us now fix n n and consider θ → ∞ \theta\to\infty. Then the probability that the pair ( i, j) (i,j) is inverted and the expected number of inversions converge to strictly positive limits. Notably, these limits depend crucially on the parity of n − m n-m, the number of non-fixed points.

###### Theorem 8.

1. ( a) (a)

We have

 | lim θ → ∞ ℙ θ ( n) \displaystyle\lim_{\theta\to\infty}\mathbb{P}_{\theta}^{(n)} | ( ( i, j) ∈ Inv ⁡ ( Σ n) | D n, m) \displaystyle\big((i,j)\in\operatorname{Inv}(\Sigma_{n})\big|D_{n,m}\big) |  |

 |  | = { n − m n ​ ( n − 1) ​ ( n − m 2 + m ​ ( n − 1 − ( j − i)) n − 2), if ​ n − m ​ is even, 1 n ​ ( n − 1) ​ ( ( n − m + 3) ​ ( n − m − 3) 2 + m ​ ( n − m) ​ ( n − 1 − ( j − i)) + 3 ​ ( n + ( j − i) − 3) n − 2), if ​ n − m ​ is odd. \displaystyle{}=\begin{cases}\frac{n-m}{n(n-1)}\left(\frac{n-m}{2}+\frac{m(n-1-(j-i))}{n-2}\right),\quad&\text{if }n-m\text{ is even},\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \frac{1}{n(n-1)}\left(\frac{(n-m+3)(n-m-3)}{2}+\frac{m(n-m)(n-1-(j-i))+3(n+(j-i)-3)}{n-2}\right),\quad&\text{if }n-m\text{ is odd}.\end{cases} |  |

2. ( b) (b)

The expected number of inversions under ℙ θ ( n) ( ⋅ | D n, m) \mathbb{P}_{\theta}^{(n)}(\,\cdot\,|D_{n,m}) satisfies

 | lim θ → ∞ 𝔼 θ ( n) ​ [| Inv ⁡ ( Σ n) | | D n, m] \displaystyle\lim_{\theta\to\infty}\mathbb{E}_{\theta}^{(n)}\big[|\operatorname{Inv}(\Sigma_{n})|\big|D_{n,m}\big] | = { ( n − m) ​ ( 3 ​ n + m) 12, if ​ n − m ​ is even, ( n − m + 3) ​ ( n − m − 3) 4 + m ​ ( n − m) 3 + 2, if ​ n − m ​ is odd. \displaystyle{}=\begin{cases}\dfrac{(n-m)(3n+m)}{12},\quad&\text{if }n-m\text{ is even},\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \dfrac{(n-m+3)(n-m-3)}{4}+\dfrac{m(n-m)}{3}+2,\quad&\text{if }n-m\text{ is odd}.\end{cases} |  |

Noting lim θ → ∞ ℙ θ ( n) ​ ( D n, n) = 1 \lim_{\theta\to\infty}\mathbb{P}_{\theta}^{(n)}(D_{n,n})=1, the positivity of the above limits does not contradict ( [1.4][15]) and ( [1.5][16]), which state the asymptotics as θ → ∞ \theta\to\infty for the unconditional problem. Rather, Theorem [8][21] and Proposition [4][22] imply

 | 𝔼 θ ( n) ​ | Inv ⁡ ( Σ n) | = \displaystyle\mathbb{E}_{\theta}^{(n)}|\operatorname{Inv}(\Sigma_{n})|={} | ∑ m = 0 n − 2 𝔼 θ ( n) ​ [| Inv ⁡ ( Σ n) | | D n, m] ​ ℙ θ ( n) ​ ( D n, m) \displaystyle\sum_{m=0}^{n-2}\mathbb{E}_{\theta}^{(n)}\big[|\operatorname{Inv}(\Sigma_{n})|\big|D_{n,m}\big]\mathbb{P}_{\theta}^{(n)}(D_{n,m}) |  |

 | ∼ \displaystyle\sim{} | 𝔼 θ ( n) ​ [| Inv ⁡ ( Σ n) | | D n, n − 2] ​ ℙ θ ( n) ​ ( D n, n − 2) ∼ 2 ​ n − 1 3 ⋅ n ​ ( n − 1) 2 ​ θ = 1 4 ​ θ ​ ( 2 ​ n 3), θ → ∞, \displaystyle\mathbb{E}_{\theta}^{(n)}\big[|\operatorname{Inv}(\Sigma_{n})|\big|D_{n,n-2}\big]\mathbb{P}_{\theta}^{(n)}(D_{n,n-2})\sim\frac{2n-1}{3}\cdot\frac{n(n-1)}{2\theta}=\frac{1}{4\theta}\binom{2n}{3},\qquad\theta\to\infty, |  |

recovering ( [1.5][16]). Likewise, ( [1.4][15]) may be recovered as well. In contrast to ( [1.4][15]), various different scenarios in terms of the (modified) Chinese restaurant construction contribute to the limit in Theorem [8][21] ( a) (a), particularly if n − m n-m is odd. Together with the resulting complex dependence on ( n, m) (n,m), this makes the existence of a short elementary proof of the above theorem, resembling the one we provide for ( [1.4][15]) and ( [1.5][16]), seem very unlikely.

The dependence on the parity in Theorem [8][21] can be explained as follows: As θ → ∞ \theta\to\infty, the probability measure ℙ θ ( n) ( ⋅ | D n, m) \mathbb{P}_{\theta}^{(n)}(\,\cdot\,|D_{n,m}) concentrates on those permutations with exactly m m fixed points which have as short and as many cycles as possible. If n − m n-m is even, the ideal setting is given by n − m 2 \frac{n-m}{2} two-cycles in additional to the m m fixed points. If n − m n-m is odd, the ideal setting is given by exactly 1 1 three-cycle and n − m − 3 2 \frac{n-m-3}{2} two-cycles in additional to the m m fixed points.

Our final result deals with the limiting behavior as θ → 0 \theta\to 0. Here the parity of n − m n-m is not relevant. Instead, the cases m = n − 3 m=n-3 and m = n − 2 m=n-2 are distinguished.

###### Proposition 9.

1. ( a) (a)

We have

 | lim θ → 0 ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n) | D n, m) = { n − m n ​ ( n − 1) ​ ( n − m − 3 2 + m ​ ( n − 1 − ( j − i)) + ( n + j − i − 3) ​ 𝟙 m ≠ n − 3 n − 2), m < n − 2, 2 ​ ( n − ( j − i)) n ​ ( n − 1), m = n − 2. \displaystyle\lim_{\theta\to 0}\mathbb{P}_{\theta}^{(n)}\big((i,j)\in\operatorname{Inv}(\Sigma_{n})\big|D_{n,m}\big){}=\begin{cases}\tfrac{n-m}{n(n-1)}\left(\tfrac{n-m-3}{2}+\tfrac{m(n-1-(j-i))+(n+j-i-3)\mathbbm{1}_{m\neq n-3}}{n-2}\right),\quad&m<n-2,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \tfrac{2(n-(j-i))}{n(n-1)},\quad&m=n-2.\end{cases} |  |

2. ( b) (b)

The expected number of inversions under ℙ θ ( n) ( ⋅ | D n, m) \mathbb{P}_{\theta}^{(n)}(\,\cdot\,|D_{n,m}) satisfies

 | lim θ → 0 𝔼 θ ( n) ​ [| Inv ⁡ ( Σ n) | | D n, m] = \displaystyle\lim_{\theta\to 0}\mathbb{E}_{\theta}^{(n)}\big[|\operatorname{Inv}(\Sigma_{n})|\big|D_{n,m}\big]={} | { ( n − m) ​ ( n − m − 3 4 + m + 2 ​ 𝟙 m ≠ n − 3 3), m < n − 2, 2 ​ n − 1 3, m = n − 2. \displaystyle\begin{cases}(n-m)\left(\dfrac{n-m-3}{4}+\dfrac{m+2\mathbbm{1}_{m\neq n-3}}{3}\right),\quad&m<n-2,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \dfrac{2n-1}{3},\quad&m=n-2.\end{cases} |  |

In the special case m = 0 m=0, corresponding to derangements, these limits are consistent with the formulas provided in Subsection [1.1][23]. More precisely, observing ℙ 0 ( n) ​ ( D n, 0) = 1 \mathbb{P}_{0}^{(n)}(D_{n,0})=1, we get

 | lim θ → 0 𝔼 θ ( n) ​ [| Inv ⁡ ( Σ n) | | D n, 0] = n ​ ( 3 ​ n − 1) 12 = 𝔼 0 ( n) ​ | Inv ⁡ ( Σ n) | = 𝔼 0 ( n) ​ [| Inv ⁡ ( Σ n) | | D n, 0], \lim_{\theta\to 0}\mathbb{E}_{\theta}^{(n)}\big[|\operatorname{Inv}(\Sigma_{n})|\big|D_{n,0}\big]=\frac{n(3n-1)}{12}=\mathbb{E}_{0}^{(n)}|\operatorname{Inv}(\Sigma_{n})|=\mathbb{E}_{0}^{(n)}\big[|\operatorname{Inv}(\Sigma_{n})|\big|D_{n,0}\big], |  |

and likewise for the probability that ( i, j) (i,j) is inverted.

The proofs of the results presented in this subsection can be found in Section [3][24].

## 2. Proofs of the Results in Subsection [1.1][23]

The proof of Theorem [1][13] relies upon a version of the Chinese restaurant construction of random permutations. A similar approach was developed recently in [[Pin25][2]] to analyze inversion statistics of uniformly random permutations with a prescribed number of fixed points.

For the reader’s convenience, let us briefly recall the standard Chinese restaurant construction of random permutations generated by Ewens sampling. Consider a restaurant with an unlimited number of round tables, each of which is able to accommodate an unlimited number of people. Arriving persons take their seats according to the following iterative scheme of Markovian type: The first person simply sits at a table. Now suppose that n ∈ ℕ n\in\mathbb{N} persons have already been seated. Then person n + 1 n+1 chooses to sit to the left of any particular already seated person with probability 1 θ + n \frac{1}{\theta+n}, and chooses to sit at an empty table with probability θ θ + n \frac{\theta}{\theta+n}. Once exactly n n persons, numbered from 1 1 to n n, are seated, we define a random permutation Σ n ∈ S n \Sigma_{n}\in S_{n} by Σ n ​ ( i):= j \Sigma_{n}(i):=j, for i, j ∈ [n] i,j\in[n], if person j j is seated to the left of person i i at one of the tables. (Persons sitting alone at a table are considered their own seatmates.) One can easily verify Σ n ∼ ℙ θ ( n) \Sigma_{n}\sim\mathbb{P}_{\theta}^{(n)} under the probability measure corresponding to the n n -step procedure described above [[Ald85][3], [Pit06][4]]. A notable feature of this construction is its consistency: Deleting n n from the cycle representation of Σ n \Sigma_{n} yields the cycle representation of Σ n − 1 \Sigma_{n-1}.

###### Proof of Theorem [1][13].

( a) (a) Let Σ n \Sigma_{n} and Σ n − 1 \Sigma_{n-1} be the (consistent) random permutations of [n] [n] and [n] ∖ { j } [n]\setminus\{j\}, respectively, arising from a Chinese restaurant construction as described above, modified such that the persons (numbered from 1 1 to n n) arrive in the order

 | 1, …, i − 1, i + 1, …, j − 1, j + 1, …, n, i, j. 1,\dots,i-1,i+1,\dots,j-1,j+1,\dots,n,i,j. |  |

We observe Σ n ∼ ℙ θ ( n) \Sigma_{n}\sim\mathbb{P}_{\theta}^{(n)} under the probability measure encoding the random seating choices of the n n persons. Slightly abusing notation, we denote this probability measure by ℙ θ ( n) \mathbb{P}_{\theta}^{(n)} as well. In what follows, we split the event

 | { ( i, j) ∈ Inv ⁡ ( Σ n) } = { Σ n − 1 ​ ( i) > Σ n − 1 ​ ( j) } \{(i,j)\in\operatorname{Inv}(\Sigma_{n})\}=\{\Sigma_{n}^{-1}(i)>\Sigma_{n}^{-1}(j)\} |  |

into several sub-events and analyze them using the modified Chinese restaurant construction.

First assume that person i i chooses to sit to the left of k ∈ [n] ∖ { i, j } k\in[n]\setminus\{i,j\} and that person j j chooses to sit neither at a new table nor to the right of i i. Then i i remains the seatmate to the left of k k after j j is seated (i.e., Σ n − 1 ​ ( i) = k \Sigma_{n}^{-1}(i)=k). Hence ( i, j) (i,j) is an inversion in this scenario if and only if person j j sits down to the left of a person with a label smaller than k k:

 | ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n), Σ n − 1 ​ ( k) = i, Σ n ​ ( j) ∉ { i, j }) \displaystyle\mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}),\Sigma_{n-1}(k)=i,\Sigma_{n}(j)\not\in\{i,j\}) |  |

 | = ℙ θ ( n) ​ ( Σ n − 1 ​ ( j) < k, Σ n − 1 ​ ( j) ≠ j, Σ n − 1 ​ ( k) = i) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}^{-1}(j)<k,\Sigma_{n}^{-1}(j)\neq j,\Sigma_{n-1}(k)=i) |  |

 | = k − 1 − 𝟙 k > j θ + n − 1 ⋅ 1 θ + n − 2. \displaystyle\qquad=\frac{k-1-\mathbbm{1}_{k>j}}{\theta+n-1}\cdot\frac{1}{\theta+n-2}. |  |

Substituting l = k − 1 l=k-1 for k < i k<i and l = k − 2 l=k-2 for k > i k>i, separating the additional + 1 +1 from each of the j − i − 1 j-i-1 terms with indices l ∈ { i − 1, …, j − 3 } l\in\{i-1,\dots,j-3\} and inserting the missing summand l = j − 2 l=j-2, we deduce

 | ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n), Σ n − 1 ​ ( i) ≠ i, Σ n ​ ( j) ∉ { i, j }) \displaystyle\mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}),\Sigma_{n-1}(i)\neq i,\Sigma_{n}(j)\not\in\{i,j\}) |  |

 | = ∑ k ∈ [n] ∖ { i, j } ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n), Σ n − 1 ​ ( k) = i, Σ n ​ ( j) ∉ { i, j }) \displaystyle\qquad=\sum_{k\in[n]\setminus\{i,j\}}\mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}),\Sigma_{n-1}(k)=i,\Sigma_{n}(j)\not\in\{i,j\}) |  |

 | = ∑ k = 1 k ≠ i j − 1 k − 1 ( θ + n − 1) ​ ( θ + n − 2) + ∑ k = j + 1 n k − 2 ( θ + n − 1) ​ ( θ + n − 2) \displaystyle\qquad=\sum_{\begin{subarray}{c}k=1\\ k\neq i\end{subarray}}^{j-1}\frac{k-1}{(\theta+n-1)(\theta+n-2)}+\sum_{k=j+1}^{n}\frac{k-2}{(\theta+n-1)(\theta+n-2)} |  |

 | = ∑ l = 0 n − 2 l + ( j − i − 1) − ( j − 2) ( θ + n − 1) ​ ( θ + n − 2) \displaystyle\qquad=\frac{\sum_{l=0}^{n-2}l+(j-i-1)-(j-2)}{(\theta+n-1)(\theta+n-2)} |  |

 | = ( n − 1 2) + ( j − i − 1) − ( j − 2) ( θ + n − 1) ​ ( θ + n − 2). \displaystyle\qquad=\frac{\binom{n-1}{2}+(j-i-1)-(j-2)}{(\theta+n-1)(\theta+n-2)}. |  |

Next consider the case that person i i chooses not to sit at a new table while person j j chooses to sit at a new table. Then the right neighbor of i i remains the same after j j is seated (i.e., Σ n − 1 − 1 ​ ( i) = Σ n − 1 ​ ( i) \Sigma_{n-1}^{-1}(i)=\Sigma_{n}^{-1}(i)) and, recalling our modified version of the Chinese restaurant construction, we get

 | ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n), Σ n − 1 ​ ( i) ≠ i, Σ n ​ ( j) = j) \displaystyle\mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}),\Sigma_{n-1}(i)\neq i,\Sigma_{n}(j)=j) |  |

 | = ℙ θ ( n) ​ ( Σ n − 1 − 1 ​ ( i) > j, Σ n ​ ( j) = j) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n-1}^{-1}(i)>j,\Sigma_{n}(j)=j) |  |

 | = n − j θ + n − 2 ⋅ θ θ + n − 1. \displaystyle\qquad=\frac{n-j}{\theta+n-2}\cdot\frac{\theta}{\theta+n-1}. |  |

Now assume that person i i chooses not to sit at a new table and that person j j chooses to sit to the right of i i. Then the original right neighbor of i i becomes the right neighbor of j j (i.e., Σ n − 1 − 1 ​ ( i) = Σ n − 1 ​ ( j) \Sigma_{n-1}^{-1}(i)=\Sigma_{n}^{-1}(j)) and we obtain

 | ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n), Σ n − 1 ​ ( i) ≠ i, Σ n ​ ( j) = i) \displaystyle\mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}),\Sigma_{n-1}(i)\neq i,\Sigma_{n}(j)=i) |  |

 | = ℙ θ ( n) ​ ( j > Σ n − 1 − 1 ​ ( i), Σ n − 1 − 1 ​ ( i) ≠ i, Σ n ​ ( j) = i) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(j>\Sigma_{n-1}^{-1}(i),\Sigma_{n-1}^{-1}(i)\neq i,\Sigma_{n}(j)=i) |  |

 | = j − 2 θ + n − 2 ⋅ 1 θ + n − 1. \displaystyle\qquad=\frac{j-2}{\theta+n-2}\cdot\frac{1}{\theta+n-1}. |  |

Finally, consider the case that person i i chooses to sit at a new table. Then ( i, j) (i,j) becomes an inversion if and only if person j j sits down at the same table or to the left of a person with a label smaller than i i:

 | ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n), Σ n − 1 ​ ( i) = i) = \displaystyle\mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}),\Sigma_{n-1}(i)=i)={} | ℙ θ ( n) ​ ( Σ n − 1 ​ ( j) ≤ i, Σ n − 1 ​ ( i) = i) = i θ + n − 1 ⋅ θ θ + n − 2. \displaystyle\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}^{-1}(j)\leq i,\Sigma_{n-1}(i)=i)=\frac{i}{\theta+n-1}\cdot\frac{\theta}{\theta+n-2}. |  |

Adding the last four equations, we obtain

(2.1) |  | ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n)) = 1 ( θ + n − 1) ​ ( θ + n − 2) ​ ( θ ​ ( n − ( j − i)) + ( n − 1 2) + j − i − 1). \displaystyle\mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}))=\frac{1}{(\theta+n-1)(\theta+n-2)}\left(\theta(n-(j-i))+\binom{n-1}{2}+j-i-1\right). |  |

By partial fraction decomposition, this is equal to

 | p i, j ​ ( θ):= \displaystyle p_{i,j}(\theta):={} | ( n − 1) ​ ( n − ( j − i)) − ( n − 1 2) − ( j − i − 1) θ + n − 1 + ( n − 1 2) + j − i − 1 − ( n − 2) ​ ( n − ( j − i)) θ + n − 2 \displaystyle\frac{(n-1)(n-(j-i))-\binom{n-1}{2}-(j-i-1)}{\theta+n-1}+\frac{\binom{n-1}{2}+j-i-1-(n-2)(n-(j-i))}{\theta+n-2} |  |

 | = \displaystyle={} | n ​ ( n − 2 ​ ( j − i) + 1) 2 ​ ( θ + n − 1) − ( n − 1) ​ ( n − 2 ​ ( j − i)) 2 ​ ( θ + n − 2), \displaystyle\frac{n(n-2(j-i)+1)}{2(\theta+n-1)}-\frac{(n-1)(n-2(j-i))}{2(\theta+n-2)}, |  |

proving ( [1.1][10]). Setting l:= j − i l:=j-i and differentiating yields

 | p i, j ′ ​ ( θ) = 1 2 ​ ( ( n − 1) ​ ( n − 2 ​ l) ( θ + n − 2) 2 − n ​ ( n − 2 ​ l + 1) ( θ + n − 1) 2). p_{i,j}^{\prime}(\theta)=\frac{1}{2}\left(\frac{(n-1)(n-2l)}{(\theta+n-2)^{2}}-\frac{n(n-2l+1)}{(\theta+n-1)^{2}}\right). |  |

Noting that [0, ∞) → [0, ∞) [0,\infty)\to[0,\infty), θ ↦ θ + n − 1 θ + n − 2 \theta\mapsto\frac{\theta+n-1}{\theta+n-2} is decreasing, we get

 | ( n − 1) ​ ( n − 2 ​ l) ​ ( θ + n − 1) 2 ( θ + n − 2) 2 − n ​ ( n − 2 ​ l + 1) ≤ \displaystyle(n-1)(n-2l)\frac{(\theta+n-1)^{2}}{(\theta+n-2)^{2}}-n(n-2l+1)\leq{} | ( n − 2 ​ l) ​ ( n − 1) 3 ( n − 2) 2 − n ​ ( n − 2 ​ l + 1) \displaystyle(n-2l)\frac{(n-1)^{3}}{(n-2)^{2}}-n(n-2l+1) |  |

 | = \displaystyle={} | 2 ​ l + ( 2 ​ l − 5) ​ n − ( 2 ​ l − 3) ​ n 2 ( n − 2) 2 ​ { < 0, l ≥ 2, > 0, l = 1, \displaystyle\frac{2l+(2l-5)n-(2l-3)n^{2}}{(n-2)^{2}}\begin{cases}<0,\quad&l\geq 2,\\ >0,\quad&l=1,\end{cases} |  |

with equality in the first line for θ = 0 \theta=0. Hence p i, j ​ ( θ) p_{i,j}(\theta) is (strictly) deceasing in θ ≥ 0 \theta\geq 0 if and only if l ≥ 2 l\geq 2 holds.

( b) (b) Using diagonal summation and well-known summation formulas, we get

(2.2) |  | ∑ i, j ∈ [n], i < j ( j − i) = ∑ k = 1 n − 1 ( n − k) ​ k = n ​ n ​ ( n − 1) 2 − ( n − 1) ​ n ​ ( 2 ​ n − 1) 6 = ( n + 1 3). \sum_{i,j\in[n],\,i<j}(j-i)=\sum_{k=1}^{n-1}(n-k)k=n\frac{n(n-1)}{2}-\frac{(n-1)n(2n-1)}{6}=\binom{n+1}{3}. |  |

Combining this with ( [2.1][25]), we deduce

 | 𝔼 θ ( n) ​ | Inv ⁡ ( Σ n) | \displaystyle\mathbb{E}_{\theta}^{(n)}|\operatorname{Inv}(\Sigma_{n})| |  |

 | = ∑ i, j ∈ [n], i < j ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n)) \displaystyle\qquad=\sum_{i,j\in[n],\,i<j}\mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n})) |  |

 | = 1 ( θ + n − 1) ​ ( θ + n − 2) ​ ∑ i, j ∈ [n], i < j ( θ ​ ( n − ( j − i)) + ( n − 1 2) + j − i − 1) \displaystyle\qquad=\frac{1}{(\theta+n-1)(\theta+n-2)}\sum_{i,j\in[n],\,i<j}\left(\theta(n-(j-i))+\binom{n-1}{2}+j-i-1\right) |  |

 | = 1 ( θ + n − 1) ​ ( θ + n − 2) ​ ( θ ​ ( ( n 2) ​ n − ( n + 1 3)) + ( n 2) ​ ( n − 1 2) + ( n + 1 3) − ( n 2)) \displaystyle\qquad=\frac{1}{(\theta+n-1)(\theta+n-2)}\left(\theta\left(\binom{n}{2}n-\binom{n+1}{3}\right)+\binom{n}{2}\binom{n-1}{2}+\binom{n+1}{3}-\binom{n}{2}\right) |  |

 | = 1 ( θ + n − 1) ​ ( θ + n − 2) ​ ( θ 4 ​ ( 2 ​ n 3) + 3 ​ n − 1 2 ​ ( n 3)). \displaystyle\qquad=\frac{1}{(\theta+n-1)(\theta+n-2)}\left(\frac{\theta}{4}\binom{2n}{3}+\frac{3n-1}{2}\binom{n}{3}\right). |  |

By partial fraction decomposition, this equals

 | g ​ ( θ):= n − 1 4 ​ ( 2 ​ n 3) − 3 ​ n − 1 2 ​ ( n 3) θ + n − 1 + 3 ​ n − 1 2 ​ ( n 3) − n − 2 4 ​ ( 2 ​ n 3) θ + n − 2 = \displaystyle g(\theta):=\frac{\frac{n-1}{4}\binom{2n}{3}-\frac{3n-1}{2}\binom{n}{3}}{\theta+n-1}+\frac{\frac{3n-1}{2}\binom{n}{3}-\frac{n-2}{4}\binom{2n}{3}}{\theta+n-2}={} | ( n + 1) ​ n 2 ​ ( n − 1) 12 ​ ( θ + n − 1) − n ​ ( n − 1) 2 ​ ( n − 2) 12 ​ ( θ + n − 2), \displaystyle\frac{(n+1)n^{2}(n-1)}{12(\theta+n-1)}-\frac{n(n-1)^{2}(n-2)}{12(\theta+n-2)}, |  |

proving ( [1.2][11]). Differentiation yields

 | g ( m) ​ ( θ) = ( − 1) m ​ m! 12 ​ n ​ ( n − 1) ​ ( ( n + 1) ​ n ( θ + n − 1) m + 1 − ( n − 1) ​ ( n − 2) ( θ + n − 2) m + 1), m ∈ ℕ. g^{(m)}(\theta)=(-1)^{m}\frac{m!}{12}n(n-1)\left(\frac{(n+1)n}{(\theta+n-1)^{m+1}}-\frac{(n-1)(n-2)}{(\theta+n-2)^{m+1}}\right),\quad m\in\mathbb{N}. |  |

Proceeding as in the proof of part ( a) (a), we get

 | ( n + 1) ​ n − ( n − 1) ​ ( n − 2) ​ ( θ + n − 1) 2 ( θ + n − 2) 2 ≥ \displaystyle(n+1)n-(n-1)(n-2)\frac{(\theta+n-1)^{2}}{(\theta+n-2)^{2}}\geq{} | ( n + 1) ​ n − ( n − 1) 3 n − 2 = n ​ ( 2 ​ n − 5) + 1 n − 2 > 0, \displaystyle(n+1)n-\frac{(n-1)^{3}}{n-2}=\frac{n(2n-5)+1}{n-2}>0, |  |

proving g ′ < 0 g^{\prime}<0. Similarly, we obtain

 | ( n + 1) ​ n − ( n − 1) ​ ( n − 2) ​ ( θ + n − 1) 3 ( θ + n − 2) 3 ≥ \displaystyle(n+1)n-(n-1)(n-2)\frac{(\theta+n-1)^{3}}{(\theta+n-2)^{3}}\geq{} | ( n + 1) ​ n − ( n − 1) 4 ( n − 2) 2 \displaystyle(n+1)n-\frac{(n-1)^{4}}{(n-2)^{2}} |  |

 | = \displaystyle={} | n ​ ( n − 2) ​ ( n − 4) − 1 ( n − 2) 2 ​ { > 0, n ≥ 5, < 0, n ∈ { 3, 4 }, \displaystyle\frac{n(n-2)(n-4)-1}{(n-2)^{2}}\begin{cases}>0,\quad&n\geq 5,\\ <0,\quad&n\in\{3,4\},\end{cases} |  |

with equality in the first line for θ = 0 \theta=0. Hence g ​ ( θ) g(\theta) is (strictly) convex in θ ≥ 0 \theta\geq 0 if and only if we have n ≥ 5 n\geq 5. ∎

###### Proof of Corollary [2][20].

We start by observing

 | 1 θ + n − m = 1 n ⋅ 1 1 − m − θ n = 1 n ​ ∑ k = 0 ∞ ( m − θ) k n k, m ∈ { 1, 2 }, n > θ. \frac{1}{\theta+n-m}=\frac{1}{n}\cdot\frac{1}{1-\frac{m-\theta}{n}}=\frac{1}{n}\sum_{k=0}^{\infty}\frac{(m-\theta)^{k}}{n^{k}},\qquad m\in\{1,2\},\ n>\theta. |  |

( a) (a) Setting ( l n) n:= ( j n − i n) n (l_{n})_{n}:=(j_{n}-i_{n})_{n} and using ( [1.1][10]), we obtain

 | ℙ θ ( n) ​ ( ( i n, j n) ∈ Inv ⁡ ( Σ n)) \displaystyle\mathbb{P}_{\theta}^{(n)}((i_{n},j_{n})\in\operatorname{Inv}(\Sigma_{n})) |  |

 | = n ​ ( n − 2 ​ l n + 1) 2 ​ ( θ + n − 1) − n ​ ( n − 2 ​ l n) 2 ​ ( θ + n − 2) + n − 2 ​ l n 2 ​ ( θ + n − 2) \displaystyle\qquad=\frac{n(n-2l_{n}+1)}{2(\theta+n-1)}-\frac{n(n-2l_{n})}{2(\theta+n-2)}+\frac{n-2l_{n}}{2(\theta+n-2)} |  |

 | = n − 2 ​ l n + 1 2 ​ ∑ k = 0 ∞ ( 1 − θ) k n k − n − 2 ​ l n 2 ​ ∑ k = 0 ∞ ( 2 − θ) k n k + n − 2 ​ l n 2 ​ n ​ ∑ k = 0 ∞ ( 2 − θ) k n k \displaystyle\qquad=\frac{n-2l_{n}+1}{2}\sum_{k=0}^{\infty}\frac{(1-\theta)^{k}}{n^{k}}-\frac{n-2l_{n}}{2}\sum_{k=0}^{\infty}\frac{(2-\theta)^{k}}{n^{k}}+\frac{n-2l_{n}}{2n}\sum_{k=0}^{\infty}\frac{(2-\theta)^{k}}{n^{k}} |  |

 | = 1 2 + ( 1 − θ) ​ l n n 2 − ( θ − 1) ​ ( θ − 2) 2 ​ n 2 + ( 2 ​ θ − 3) ​ ( θ − 1) ​ l n n 3 + O ​ ( 1 n 3), n → ∞, \displaystyle\qquad=\frac{1}{2}+\frac{(1-\theta)l_{n}}{n^{2}}-\frac{(\theta-1)(\theta-2)}{2n^{2}}+\frac{(2\theta-3)(\theta-1)l_{n}}{n^{3}}+O\left(\frac{1}{n^{3}}\right),\qquad n\to\infty, |  |

where the O O -term depends on θ \theta.

( b) (b) Similarly equation ( [1.2][11]) implies

 | 𝔼 θ ( n) ​ | Inv ⁡ ( Σ n) | = \displaystyle\mathbb{E}_{\theta}^{(n)}|\operatorname{Inv}(\Sigma_{n})|={} | ( n + 1) ​ n 2 ​ ( n − 1) 12 ​ ( θ + n − 1) − n ​ ( n − 1) 2 ​ ( n − 2) 12 ​ ( θ + n − 2) \displaystyle\frac{(n+1)n^{2}(n-1)}{12(\theta+n-1)}-\frac{n(n-1)^{2}(n-2)}{12(\theta+n-2)} |  |

 | = \displaystyle={} | n 3 − n 12 ​ ∑ k = 0 ∞ ( 1 − θ) k n k − n 3 − 4 ​ n 2 + 5 ​ n − 2 12 ​ ∑ k = 0 ∞ ( 2 − θ) k n k \displaystyle\frac{n^{3}-n}{12}\sum_{k=0}^{\infty}\frac{(1-\theta)^{k}}{n^{k}}-\frac{n^{3}-4n^{2}+5n-2}{12}\sum_{k=0}^{\infty}\frac{(2-\theta)^{k}}{n^{k}} |  |

 | = \displaystyle={} | n ​ ( n − 1) 4 + 1 − θ 6 ​ n + θ ​ ( θ − 1) 12 + O ​ ( 1 n 2), n → ∞, \displaystyle\frac{n(n-1)}{4}+\frac{1-\theta}{6}n+\frac{\theta(\theta-1)}{12}+O\left(\frac{1}{n^{2}}\right),\qquad n\to\infty, |  |

where the O O -term depends on θ \theta. ∎

###### Elementary proof of ( [1.4][15]) and ( [1.5][16]).

By the definition of the Ewens sampling distribution, we have

 | ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n)) = 1 θ ( n) ​ ∑ k = 1 n a n, k i, j ​ θ k, \mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}))=\frac{1}{\theta^{(n)}}\sum_{k=1}^{n}a^{i,j}_{n,k}\theta^{k}, |  |

with

 | a n, k i, j:= | { π ∈ S n: N ​ ( π) = k, ( i, j) ∈ Inv ⁡ ( π) } |, k ∈ [n], a^{i,j}_{n,k}:=|\{\pi\in S_{n}:N(\pi)=k,\,(i,j)\in\operatorname{Inv}(\pi)\}|,\quad k\in[n], |  |

being the number of permutations in S n S_{n} with k k cycles such that ( i, j) (i,j) is an inversion. Clearly, a n, n i, j = 0 a^{i,j}_{n,n}=0 holds, showing

 | lim θ → ∞ θ ​ ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n)) = a n, n − 1 i, j. \lim_{\theta\to\infty}\theta\mathbb{P}_{\theta}^{(n)}((i,j)\in\operatorname{Inv}(\Sigma_{n}))=a^{i,j}_{n,n-1}. |  |

Further, we observe that π ∈ S n \pi\in S_{n} with N ​ ( π) = n − 1 N(\pi)=n-1 has exactly n − 2 n-2 fixed points and swaps the remaining two elements of [n] [n]. Thus any π ∈ S n \pi\in S_{n} with N ​ ( π) = n − 1 N(\pi)=n-1 satisfies ( i, j) ∈ Inv ⁡ ( π) (i,j)\in\operatorname{Inv}(\pi) if and only if it either swaps i i with some k ∈ { j + 1, …, n } k\in\{j+1,\dots,n\} or it swaps j j with some k ∈ { 1, …, i } k\in\{1,\dots,i\}. We deduce a n, n − 1 i, j = n − j + i a^{i,j}_{n,n-1}=n-j+i, proving ( [1.4][15]). Regarding ( [1.5][16]), we observe

 | 𝔼 θ ( n) ​ | Inv ⁡ ( Σ n) | = 1 θ ( n) ​ ∑ k = 1 n b n, k ​ θ k, \mathbb{E}_{\theta}^{(n)}|\operatorname{Inv}(\Sigma_{n})|=\frac{1}{\theta^{(n)}}\sum_{k=1}^{n}b_{n,k}\theta^{k}, |  |

with b n, k:= ∑ i, j ∈ [n], i < j a n, k i, j b_{n,k}:=\sum_{i,j\in[n],\,i<j}a_{n,k}^{i,j} for any k ∈ [n] k\in[n]. In particular, b n, n = 0 b_{n,n}=0 holds, entailing

 | lim θ → ∞ θ ​ 𝔼 θ ( n) ​ | Inv ⁡ ( Σ n) | = b n, n − 1 = ∑ i, j ∈ [n], i < j ( n − j + i) = 1 4 ​ ( 2 ​ n 3), \lim_{\theta\to\infty}\theta\mathbb{E}_{\theta}^{(n)}|\operatorname{Inv}(\Sigma_{n})|=b_{n,n-1}=\sum_{i,j\in[n],\,i<j}(n-j+i)=\frac{1}{4}\binom{2n}{3}, |  |

where the final equality is derived as in the proof of Theorem [1][13] ( b) (b). ∎

## 3. Proofs of the Results in Subsection [1.2][26]

###### Proof of Proposition [4][22].

Let n ∈ ℕ n\in\mathbb{N} and m ∈ { 0, …, n − 1 } m\in\{0,\dots,n-1\}. By symmetry and a basic Chinese restaurant argument, we have

 | ℙ θ ( n) ​ ( D n, m) = \displaystyle\mathbb{P}_{\theta}^{(n)}(D_{n,m})={} | ( n m) ​ ℙ θ ( n) ​ ( Fix ⁡ ( Σ n) = { n − m + 1, …, n }) \displaystyle\binom{n}{m}\mathbb{P}_{\theta}^{(n)}(\operatorname{Fix}(\Sigma_{n})=\{n-m+1,\dots,n\}) |  |

(3.1) |  | = \displaystyle={} | ( n m) ​ ℙ θ ( n − m) ​ ( D n − m, 0) ​ ∏ l = n − m n − 1 θ θ + l = ( n m) ​ θ m ​ θ ( n − m) θ ( n) ​ ℙ θ ( n − m) ​ ( D n − m, 0), \displaystyle\binom{n}{m}\mathbb{P}_{\theta}^{(n-m)}(D_{n-m,0})\prod_{l=n-m}^{n-1}\frac{\theta}{\theta+l}=\binom{n}{m}\frac{\theta^{m}\theta^{(n-m)}}{\theta^{(n)}}\mathbb{P}_{\theta}^{(n-m)}(D_{n-m,0}), |  |

proving the first claimed equality. For any A ⊆ [n] A\subseteq[n] with k:= | A | k:=|A|, a similar approach yields

 | ℙ θ ( n) ​ ( A ⊆ Fix ⁡ ( Σ n)) = \displaystyle\mathbb{P}_{\theta}^{(n)}(A\subseteq\operatorname{Fix}(\Sigma_{n}))={} | ℙ θ ( n) ​ ( { n − k + 1, …, n } ⊆ Fix ⁡ ( Σ n)) = ∏ l = n − k n − 1 θ θ + l = θ k ​ θ ( n − k) θ ( n). \displaystyle\mathbb{P}_{\theta}^{(n)}(\{n-k+1,\dots,n\}\subseteq\operatorname{Fix}(\Sigma_{n}))=\prod_{l=n-k}^{n-1}\frac{\theta}{\theta+l}=\frac{\theta^{k}\theta^{(n-k)}}{\theta^{(n)}}. |  |

Together with the inclusion-exclusion principle, we deduce

 | ℙ θ ( n) ​ ( D n, 0) = \displaystyle\mathbb{P}_{\theta}^{(n)}(D_{n,0})={} | 1 − ℙ θ ( n) ​ ( Fix ⁡ ( Σ n) ≠ ∅) \displaystyle 1-\mathbb{P}_{\theta}^{(n)}(\operatorname{Fix}(\Sigma_{n})\neq\emptyset) |  |

 | = \displaystyle={} | 1 − ∑ k = 1 n ( − 1) k − 1 ​ ∑ A ⊆ [n], | A | = k ℙ θ ( n) ​ ( A ⊆ Fix ⁡ ( Σ n)) = ∑ k = 0 n ( − 1) k ​ ( n k) ​ θ k ​ θ ( n − k) θ ( n). \displaystyle 1-\sum_{k=1}^{n}(-1)^{k-1}\sum_{A\subseteq[n],|A|=k}\mathbb{P}_{\theta}^{(n)}(A\subseteq\operatorname{Fix}(\Sigma_{n}))=\sum_{k=0}^{n}(-1)^{k}\binom{n}{k}\frac{\theta^{k}\theta^{(n-k)}}{\theta^{(n)}}. |  |

It remains to insert this into ( [3][27]) and simplify the resulting expression to obtain the second claimed equality. The special case m = n m=n is trivial. ∎

The main ingredient towards proving the asymptotic results of Subsection [1.2][26] is the following proposition. In view of Proposition [4][22] and equation ( [1.6][28]), it provides the exact formulas announced in Subsection [1.2][26]:

###### Proposition 10.

1. ( a) (a)

We have

(3.2) |  | ℙ θ ( n) ( ( \displaystyle\mathbb{P}_{\theta}^{(n)}\big(( | i, j) ∈ Inv ( Σ n) | D n, m) \displaystyle i,j)\in\operatorname{Inv}(\Sigma_{n})\big|D_{n,m}\big) |  |

 | = \displaystyle={} | 1 ( θ + n − 1) ​ ( θ + n − 2) ⋅ \displaystyle\frac{1}{(\theta+n-1)(\theta+n-2)}\cdot |  |

 |  | [θ ​ ( n − m − 1) ​ ( n − 1 − ( j − i)) n − 2 ⋅ ℙ θ ( n − 2) ​ ( D n − 2, m − 1) ℙ θ ( n) ​ ( D n, m) \displaystyle\Bigg[\frac{\theta(n-m-1)(n-1-(j-i))}{n-2}\cdot\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m-1})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})} |  |

 |  | + ( θ ​ m ​ ( n − 1 − ( j − i)) n − 2 + θ + ( n − m − 2) ​ ( n − m − 3 2 + n + j − i − 3 n − 2)) ​ ℙ θ ( n − 2) ​ ( D n − 2, m) ℙ θ ( n) ​ ( D n, m) \displaystyle+\left(\frac{\theta m(n-1-(j-i))}{n-2}+\theta+(n-m-2)\left(\frac{n-m-3}{2}+\frac{n+j-i-3}{n-2}\right)\right)\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})} |  |

 |  | + ( m + 1) ​ ( ( n − m − 3) + n + j − i − 3 n − 2) ​ ℙ θ ( n − 2) ​ ( D n − 2, m + 1) ℙ θ ( n) ​ ( D n, m) \displaystyle+(m+1)\left((n-m-3)+\frac{n+j-i-3}{n-2}\right)\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})} |  |

 |  | + ( m + 2) ​ ( m + 1) 2 ⋅ ℙ θ ( n − 2) ​ ( D n − 2, m + 2) ℙ θ ( n) ​ ( D n, m)]. \displaystyle+\frac{(m+2)(m+1)}{2}\cdot\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+2})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})}\Bigg]. |  |

2. ( b) (b)

The expected number of inversions under ℙ θ ( n) ( ⋅ | D n, m) \mathbb{P}_{\theta}^{(n)}(\,\cdot\,|D_{n,m}) is given by

(3.3) |  | 𝔼 θ ( n) ​ [| Inv ⁡ ( Σ n) | | D n, m] = \displaystyle\mathbb{E}_{\theta}^{(n)}\big[|\operatorname{Inv}(\Sigma_{n})|\big|D_{n,m}\big]={} | n ​ ( n − 1) ( θ + n − 1) ​ ( θ + n − 2) ⋅ \displaystyle\frac{n(n-1)}{(\theta+n-1)(\theta+n-2)}\cdot |  |

 |  | [θ ​ ( n − m − 1) 3 ⋅ ℙ θ ( n − 2) ​ ( D n − 2, m − 1) ℙ θ ( n) ​ ( D n, m) \displaystyle\Bigg[\frac{\theta(n-m-1)}{3}\cdot\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m-1})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})} |  |

 |  | + ( θ ​ m 3 + θ 2 + ( n − m − 2) ​ ( n − m − 3 4 + 2 3)) ​ ℙ θ ( n − 2) ​ ( D n − 2, m) ℙ θ ( n) ​ ( D n, m) \displaystyle+\left(\frac{\theta m}{3}+\frac{\theta}{2}+(n-m-2)\left(\frac{n-m-3}{4}+\frac{2}{3}\right)\right)\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})} |  |

 |  | + ( m + 1) ​ ( n − m − 3 2 + 2 3) ​ ℙ θ ( n − 2) ​ ( D n − 2, m + 1) ℙ θ ( n) ​ ( D n, m) \displaystyle+(m+1)\left(\frac{n-m-3}{2}+\frac{2}{3}\right)\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})} |  |

 |  | + ( m + 2) ​ ( m + 1) 4 ⋅ ℙ θ ( n − 2) ​ ( D n − 2, m + 2) ℙ θ ( n) ​ ( D n, m)]. \displaystyle+\frac{(m+2)(m+1)}{4}\cdot\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+2})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})}\Bigg]. |  |

###### Proof.

( a) (a) At the top level, we proceed similar to the proof of Theorem [1][13]. Let Σ n \Sigma_{n}, Σ n − 1 \Sigma_{n-1} and Σ n − 2 \Sigma_{n-2} be the (consistent) random permutations of [n] [n], of [n] ∖ { j } [n]\setminus\{j\} and of [n] ∖ { i, j } [n]\setminus\{i,j\}, respectively, arising from a Chinese restaurant construction, modified such that the persons (numbered from 1 1 to n n) arrive in the order

 | 1, …, i − 1, i + 1, …, j − 1, j + 1, …, n, i, j. 1,\dots,i-1,i+1,\dots,j-1,j+1,\dots,n,i,j. |  |

As above, we observe Σ n ∼ ℙ θ ( n) \Sigma_{n}\sim\mathbb{P}_{\theta}^{(n)} under the probability measure encoding the random seating choices of the n n persons, which we denote by ℙ θ ( n) \mathbb{P}_{\theta}^{(n)} as well. Since we are conditioning on D n, m D_{n,m}, we are permanently dealing with the situation that | Fix ⁡ ( Σ n) | = m |\operatorname{Fix}(\Sigma_{n})|=m persons are sitting alone at tables when all n n people are seated. This, in particular, implies

 | | Fix ⁡ ( Σ n − 2) | ∈ { m − 2, …, m + 2 }. |\operatorname{Fix}(\Sigma_{n-2})|\in\{m-2,\dots,m+2\}. |  |

We consider each of the five options separately, thus splitting

 | A:= { ( i, j) ∈ Inv ⁡ ( Σ n) } ∩ D n, m = { Σ n − 1 ​ ( i) > Σ n − 1 ​ ( j), | Fix ⁡ ( Σ n) | = m } A:=\{(i,j)\in\operatorname{Inv}(\Sigma_{n})\}\cap D_{n,m}=\{\Sigma_{n}^{-1}(i)>\Sigma_{n}^{-1}(j),|\operatorname{Fix}(\Sigma_{n})|=m\} |  |

into five sub-events. We further partition these sub-events into a total of 13 13 sub-sub-events and analyze each of them using the modified Chinese restaurant construction. For convenience, we call a table empty, a singleton or crowded according to whether 0, 1 1 or at least 2 2 persons are seated there.

First consider the situation with m − 2 m-2 singleton tables when n − 2 n-2 persons are seated. Then persons i i and j j both would have to choose empty tables, which, however, implies that ( i, j) (i,j) cannot be an inversion. Hence we have

(3.4) |  |  | ℙ θ ( n) ( A ∩ { | Fix ( Σ n − 2) | = m − 2 } = 0. \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m-2\}=0. |  |

Now consider the situation with m − 1 m-1 singleton tables when n − 2 n-2 persons are seated. We make a case distinction with respect to the seating choice of i i. We start by assuming that i i chooses an empty table. Then j j must choose a crowded table to ensure that we end up with m m singleton tables. By symmetry, the m − 1 m-1 persons sitting at singleton tables when i i arrives (i.e., the fixed points of Σ n − 2 \Sigma_{n-2}) are distributed with equal probability among the n − 2 n-2 seated persons. Using this symmetry property in the fourth equality, we get

 | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m − 1, Σ n − 1 ​ ( i) = i }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m-1,\Sigma_{n-1}(i)=i\}) |  |

 | = ℙ θ ( n) ​ ( Σ n − 1 ​ ( j) ∉ Fix ⁡ ( Σ n − 2), i > Σ n − 1 ​ ( j), Σ n − 1 ​ ( i) = i, | Fix ⁡ ( Σ n − 2) | = m − 1) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}^{-1}(j)\not\in\operatorname{Fix}(\Sigma_{n-2}),i>\Sigma_{n}^{-1}(j),\Sigma_{n-1}(i)=i,|\operatorname{Fix}(\Sigma_{n-2})|=m-1) |  |

 | = ∑ k = 1 i − 1 ℙ θ ( n) ​ ( Σ n − 1 ​ ( j) = k, Σ n − 1 ​ ( i) = i, k ∉ Fix ⁡ ( Σ n − 2), | Fix ⁡ ( Σ n − 2) | = m − 1) \displaystyle\qquad=\sum_{k=1}^{i-1}\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}^{-1}(j)=k,\Sigma_{n-1}(i)=i,k\not\in\operatorname{Fix}(\Sigma_{n-2}),|\operatorname{Fix}(\Sigma_{n-2})|=m-1) |  |

 | = ∑ k = 1 i − 1 1 θ + n − 1 ⋅ θ θ + n − 2 ​ ℙ θ ( n − 2) ​ ( { k ∉ Fix ⁡ ( Σ n − 2) } ∩ D n − 2, m − 1) \displaystyle\qquad=\sum_{k=1}^{i-1}\frac{1}{\theta+n-1}\cdot\frac{\theta}{\theta+n-2}\mathbb{P}_{\theta}^{(n-2)}(\{k\not\in\operatorname{Fix}(\Sigma_{n-2})\}\cap D_{n-2,m-1}) |  |

 | = ∑ k = 1 i − 1 1 θ + n − 1 ⋅ θ θ + n − 2 ⋅ ( n − 2) − ( m − 1) n − 2 ​ ℙ θ ( n − 2) ​ ( D n − 2, m − 1) \displaystyle\qquad=\sum_{k=1}^{i-1}\frac{1}{\theta+n-1}\cdot\frac{\theta}{\theta+n-2}\cdot\frac{(n-2)-(m-1)}{n-2}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m-1}) |  |

 | = i − 1 θ + n − 1 ⋅ n − m − 1 n − 2 ⋅ θ θ + n − 2 ​ ℙ θ ( n − 2) ​ ( D n − 2, m − 1). \displaystyle\qquad=\frac{i-1}{\theta+n-1}\cdot\frac{n-m-1}{n-2}\cdot\frac{\theta}{\theta+n-2}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m-1}). |  |

Throughout the rest of the proof, we make extensive use of symmetry arguments similar to the last four lines without repeating the details. Let us now assume that i i does not choose an empty table. Then necessarily i i must choose a crowded table while j j must choose an empty table. Noting that this implies Σ n − 1 ​ ( i) = Σ n − 1 − 1 ​ ( i) \Sigma_{n}^{-1}(i)=\Sigma_{n-1}^{-1}(i), a similar calculation yields

 | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m − 1, Σ n − 1 ​ ( i) ≠ i }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m-1,\Sigma_{n-1}(i)\neq i\}) |  |

 | = ℙ θ ( n) ​ ( Σ n ​ ( j) = j, Σ n − 1 − 1 ​ ( i) ∉ Fix ⁡ ( Σ n − 2), Σ n − 1 − 1 ​ ( i) > j, | Fix ⁡ ( Σ n − 2) | = m − 1) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}(j)=j,\Sigma_{n-1}^{-1}(i)\not\in\operatorname{Fix}(\Sigma_{n-2}),\Sigma_{n-1}^{-1}(i)>j,|\operatorname{Fix}(\Sigma_{n-2})|=m-1) |  |

 | = θ θ + n − 1 ⋅ n − m − 1 n − 2 ⋅ n − j θ + n − 2 ​ ℙ θ ( n − 2) ​ ( D n − 2, m − 1). \displaystyle\qquad=\frac{\theta}{\theta+n-1}\cdot\frac{n-m-1}{n-2}\cdot\frac{n-j}{\theta+n-2}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m-1}). |  |

We deduce

(3.5) |  | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m − 1 }) = θ ​ ( n − m − 1) ​ ( n − 1 − ( j − i)) ( θ + n − 1) ​ ( θ + n − 2) ​ ( n − 2) ​ ℙ θ ( n − 2) ​ ( D n − 2, m − 1). \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m-1\})=\frac{\theta(n-m-1)(n-1-(j-i))}{(\theta+n-1)(\theta+n-2)(n-2)}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m-1}). |  |

Next consider the situation with m m singleton tables when n − 2 n-2 persons are seated. We make a case distinction with respect to the seating choices of i i and j j. First, assume that i i chooses an empty table and that j j joins i i. Then ( i, j) (i,j) is an inversion and we have

 | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m, Σ n − 1 − 1 ​ ( i) = i, Σ n − 1 ​ ( j) = i }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m,\Sigma_{n-1}^{-1}(i)=i,\Sigma_{n}^{-1}(j)=i\}) |  |

 | = ℙ θ ( n) ​ ( Σ n − 1 ​ ( j) = i, Σ n − 1 − 1 ​ ( i) = i, | Fix ⁡ ( Σ n − 2) | = m) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}^{-1}(j)=i,\Sigma_{n-1}^{-1}(i)=i,|\operatorname{Fix}(\Sigma_{n-2})|=m) |  |

 | = 1 θ + n − 1 ⋅ θ θ + n − 2 ​ ℙ θ ( n − 2) ​ ( D n − 2, m). \displaystyle\qquad=\frac{1}{\theta+n-1}\cdot\frac{\theta}{\theta+n-2}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m}). |  |

Second, assume that i i chooses an empty table and that j j does not join i i. Then j j must sit down at one of the other singleton tables. Noting Σ n − 1 ​ ( i) = i \Sigma_{n}^{-1}(i)=i and using our usual symmetry argument, we get

 | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m, Σ n − 1 − 1 ​ ( i) = i, Σ n − 1 ​ ( j) ≠ i }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m,\Sigma_{n-1}^{-1}(i)=i,\Sigma_{n}^{-1}(j)\neq i\}) |  |

 | = ℙ θ ( n) ​ ( Σ n − 1 ​ ( j) ∈ Fix ⁡ ( Σ n − 2), i > Σ n − 1 ​ ( j), Σ n − 1 − 1 ​ ( i) = i, | Fix ⁡ ( Σ n − 2) | = m) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}^{-1}(j)\in\operatorname{Fix}(\Sigma_{n-2}),i>\Sigma_{n}^{-1}(j),\Sigma_{n-1}^{-1}(i)=i,|\operatorname{Fix}(\Sigma_{n-2})|=m) |  |

 | = m n − 2 ⋅ i − 1 θ + n − 1 ⋅ θ θ + n − 2 ​ ℙ θ ( n − 2) ​ ( D n − 2, m). \displaystyle\qquad=\frac{m}{n-2}\cdot\frac{i-1}{\theta+n-1}\cdot\frac{\theta}{\theta+n-2}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m}). |  |

Third, assume that i i chooses a singleton table. Then j j must choose an empty table and we obtain

 | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m, Σ n − 1 − 1 ​ ( i) ∈ Fix ⁡ ( Σ n − 2) }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m,\Sigma_{n-1}^{-1}(i)\in\operatorname{Fix}(\Sigma_{n-2})\}) |  |

 | = ℙ θ ( n) ​ ( Σ n ​ ( j) = j, Σ n − 1 − 1 ​ ( i) ∈ Fix ⁡ ( Σ n − 2), Σ n − 1 − 1 ​ ( i) > j, | Fix ⁡ ( Σ n − 2) | = m) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}(j)=j,\Sigma_{n-1}^{-1}(i)\in\operatorname{Fix}(\Sigma_{n-2}),\Sigma_{n-1}^{-1}(i)>j,|\operatorname{Fix}(\Sigma_{n-2})|=m) |  |

 | = θ θ + n − 1 ⋅ m n − 2 ⋅ n − j θ + n − 2 ​ ℙ θ ( n − 2) ​ ( D n − 2, m). \displaystyle\qquad=\frac{\theta}{\theta+n-1}\cdot\frac{m}{n-2}\cdot\frac{n-j}{\theta+n-2}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m}). |  |

Fourth, assume that i i chooses a crowded table and that j j sits down to the right of i i. Then the original right neighbor of i i becomes the right neighbor of j j (i.e., Σ n − 1 − 1 ​ ( i) = Σ n − 1 ​ ( j) \Sigma_{n-1}^{-1}(i)=\Sigma_{n}^{-1}(j)). We obtain

 | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m, Σ n − 1 − 1 ​ ( i) ∉ Fix ⁡ ( Σ n − 2) ∪ { i }, Σ n ​ ( j) = i }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m,\Sigma_{n-1}^{-1}(i)\not\in\operatorname{Fix}(\Sigma_{n-2})\cup\{i\},\Sigma_{n}(j)=i\}) |  |

 | = ℙ θ ( n) ( Σ n ( j) = i, Σ n − 1 − 1 ( i) ∉ Fix ( Σ n − 2), j > Σ n − 1 − 1 ( i) ≠ i, | Fix ( Σ n − 2) | = m) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}(j)=i,\Sigma_{n-1}^{-1}(i)\not\in\operatorname{Fix}(\Sigma_{n-2}),j>\Sigma_{n-1}^{-1}(i)\neq i,|\operatorname{Fix}(\Sigma_{n-2})|=m) |  |

 | = 1 θ + n − 1 ⋅ n − 2 − m n − 2 ⋅ j − 2 θ + n − 2 ​ ℙ θ ( n − 2) ​ ( D n − 2, m). \displaystyle\qquad=\frac{1}{\theta+n-1}\cdot\frac{n-2-m}{n-2}\cdot\frac{j-2}{\theta+n-2}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m}). |  |

Fifth, assume that i i chooses a crowded table and that j j sits down to the left of i i. Then the right neighbor of i i remains the same after j j is seated (i.e., Σ n − 1 − 1 ​ ( i) = Σ n − 1 ​ ( i) \Sigma_{n-1}^{-1}(i)=\Sigma_{n}^{-1}(i)). We obtain

 | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m, Σ n − 1 − 1 ​ ( i) ∉ Fix ⁡ ( Σ n − 2) ∪ { i }, Σ n − 1 ​ ( j) = i }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m,\Sigma_{n-1}^{-1}(i)\not\in\operatorname{Fix}(\Sigma_{n-2})\cup\{i\},\Sigma_{n}^{-1}(j)=i\}) |  |

 | = ℙ θ ( n) ​ ( Σ n − 1 ​ ( j) = i, Σ n − 1 − 1 ​ ( i) ∉ Fix ⁡ ( Σ n − 2), Σ n − 1 − 1 ​ ( i) > i, | Fix ⁡ ( Σ n − 2) | = m) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}^{-1}(j)=i,\Sigma_{n-1}^{-1}(i)\not\in\operatorname{Fix}(\Sigma_{n-2}),\Sigma_{n-1}^{-1}(i)>i,|\operatorname{Fix}(\Sigma_{n-2})|=m) |  |

 | = 1 θ + n − 1 ⋅ n − 2 − m n − 2 ⋅ n − i − 1 θ + n − 2 ​ ℙ θ ( n − 2) ​ ( D n − 2, m). \displaystyle\qquad=\frac{1}{\theta+n-1}\cdot\frac{n-2-m}{n-2}\cdot\frac{n-i-1}{\theta+n-2}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m}). |  |

Sixth and lastly, assume that i i chooses a crowded table and that j j does not sit down next to i i. Then j j must have joined a crowded table as well. Further, i i must have chosen to sit to the left of some k i ∈ [n] ∖ { i, j } k_{i}\in[n]\setminus\{i,j\} (i.e., Σ n − 1 − 1 ​ ( i) = k i \Sigma_{n-1}^{-1}(i)=k_{i}). This k i k_{i} remains the right neighbor i i (i.e., Σ n − 1 ​ ( i) = k i \Sigma_{n}^{-1}(i)=k_{i}). Hence ( i, j) (i,j) is an inversion in this scenario if and only if j j sits down to the left of a person k j ∈ [n] ∖ { i, j } k_{j}\in[n]\setminus\{i,j\} with k i > k j k_{i}>k_{j}. For such k i, k j ∈ [n] ∖ { i, j } k_{i},k_{j}\in[n]\setminus\{i,j\} with k i > k j k_{i}>k_{j}, a (slightly more elaborate) symmetry argument yields

 | ℙ θ ( n) ​ ( | Fix ⁡ ( Σ n) | = m, | Fix ⁡ ( Σ n − 2) | = m, Σ n − 1 ​ ( j) = k j, Σ n − 1 − 1 ​ ( i) = k i) \displaystyle\mathbb{P}_{\theta}^{(n)}(|\operatorname{Fix}(\Sigma_{n})|=m,|\operatorname{Fix}(\Sigma_{n-2})|=m,\Sigma_{n}^{-1}(j)=k_{j},\Sigma_{n-1}^{-1}(i)=k_{i}) |  |

 | = ℙ θ ( n) ​ ( Σ n − 1 ​ ( j) = k j, Σ n − 1 − 1 ​ ( i) = k i, k i ∉ Fix ⁡ ( Σ n − 2), k j ∉ Fix ⁡ ( Σ n − 2), | Fix ⁡ ( Σ n − 2) | = m) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}^{-1}(j)=k_{j},\Sigma_{n-1}^{-1}(i)=k_{i},k_{i}\not\in\operatorname{Fix}(\Sigma_{n-2}),k_{j}\not\in\operatorname{Fix}(\Sigma_{n-2}),|\operatorname{Fix}(\Sigma_{n-2})|=m) |  |

 | = 1 θ + n − 1 ⋅ 1 θ + n − 2 ⋅ ( n − 2 − m) ​ ( n − 3 − m) ( n − 2) ​ ( n − 3) ​ 𝟙 n > 3 ​ ℙ θ ( n − 2) ​ ( D n − 2, m + 1). \displaystyle\qquad=\frac{1}{\theta+n-1}\cdot\frac{1}{\theta+n-2}\cdot\frac{(n-2-m)(n-3-m)}{(n-2)(n-3)}\mathbbm{1}_{n>3}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1}). |  |

Noting

(3.6) |  | ∑ k i, k j ∈ [n] ∖ { i, j } 𝟙 k i > k j = ( n − 2) ​ ( n − 3) 2, \sum_{k_{i},k_{j}\in[n]\setminus\{i,j\}}\mathbbm{1}_{k_{i}>k_{j}}=\frac{(n-2)(n-3)}{2}, |  |

we deduce

 | ℙ θ ( n) ( A ∩ { | Fix ( Σ n − 2) | = m, Σ n ( j) ≠ i, Σ n − 1 ( j) ≠ i) }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m,\Sigma_{n}(j)\neq i,\Sigma_{n}^{-1}(j)\neq i)\}) |  |

 | = ∑ k i, k j ∈ [n] ∖ { i, j } 𝟙 k i > k j ​ ℙ θ ( n) ​ ( | Fix ⁡ ( Σ n) | = m, | Fix ⁡ ( Σ n − 2) | = m, Σ n − 1 ​ ( j) = k j, Σ n − 1 − 1 ​ ( i) = k i) \displaystyle\qquad=\sum_{k_{i},k_{j}\in[n]\setminus\{i,j\}}\mathbbm{1}_{k_{i}>k_{j}}\mathbb{P}_{\theta}^{(n)}(|\operatorname{Fix}(\Sigma_{n})|=m,|\operatorname{Fix}(\Sigma_{n-2})|=m,\Sigma_{n}^{-1}(j)=k_{j},\Sigma_{n-1}^{-1}(i)=k_{i}) |  |

 | = ( n − m − 2) ​ ( n − m − 3) 2 ​ ( θ + n − 1) ​ ( θ + n − 2) ​ ℙ θ ( n − 2) ​ ( D n − 2, m). \displaystyle\qquad=\frac{(n-m-2)(n-m-3)}{2(\theta+n-1)(\theta+n-2)}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m}). |  |

(The indicator 𝟙 n > 3 \mathbbm{1}_{n>3} can be omitted since n = 3 n=3 implies ( n − m − 2) ​ ( n − m − 3) = 0 (n-m-2)(n-m-3)=0.) Combining this with the probabilities covering the other five possible seating arrangements treated above, we get

(3.7) |  |  | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m\}) |  |

 | = \displaystyle={} | ℙ θ ( n − 2) ​ ( D n − 2, m) ( θ + n − 1) ​ ( θ + n − 2) ​ ( θ ​ m ​ ( n − 1 − ( j − i)) n − 2 + θ + ( n − 2 − m) ​ ( n + j − i − 3 n − 2 + n − m − 3 2)). \displaystyle\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m})}{(\theta+n-1)(\theta+n-2)}\left(\frac{\theta m(n-1-(j-i))}{n-2}+\theta+(n-2-m)\left(\frac{n+j-i-3}{n-2}+\frac{n-m-3}{2}\right)\right). |  |

Next consider the situation with m + 1 m+1 singleton tables when n − 2 n-2 persons are seated. We make a case distinction with respect to the seating choice of j j. First, assume that j j chooses to sit to the right of i i. Then i i must have joined a singleton table and the original seatmate of i i becomes the right neighbor of j j (i.e., Σ n − 1 − 1 ​ ( i) = Σ n − 1 ​ ( j) \Sigma_{n-1}^{-1}(i)=\Sigma_{n}^{-1}(j)). Noting that i i joining a singleton table implies Σ n − 1 − 1 ​ ( i) ≠ i \Sigma_{n-1}^{-1}(i)\neq i and using our usual symmetry argument, we get

 | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m + 1, Σ n ​ ( j) = i }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m+1,\Sigma_{n}(j)=i\}) |  |

 | = ℙ θ ( n) ( Σ n ( j) = i, Σ n − 1 − 1 ( i) ∈ Fix ( Σ n − 2), j > Σ n − 1 − 1 ( i) ≠ i, | Fix ( Σ n − 2) | = m + 1) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}(j)=i,\Sigma_{n-1}^{-1}(i)\in\operatorname{Fix}(\Sigma_{n-2}),j>\Sigma_{n-1}^{-1}(i)\neq i,|\operatorname{Fix}(\Sigma_{n-2})|=m+1) |  |

 | = 1 θ + n − 1 ⋅ m + 1 n − 2 ⋅ j − 2 θ + n − 2 ​ ℙ θ ( n − 2) ​ ( D n − 2, m + 1). \displaystyle\qquad=\frac{1}{\theta+n-1}\cdot\frac{m+1}{n-2}\cdot\frac{j-2}{\theta+n-2}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1}). |  |

Second, assume that j j chooses to sit to the left of i i. Then, again, i i must have joined a singleton table and the original seatmate of i i remains its right neighbor (i.e., Σ n − 1 − 1 ​ ( i) = Σ n − 1 ​ ( i) \Sigma_{n-1}^{-1}(i)=\Sigma_{n}^{-1}(i)). We obtain

 | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m + 1, Σ n − 1 ​ ( j) = i }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m+1,\Sigma_{n}^{-1}(j)=i\}) |  |

 | = ℙ θ ( n) ​ ( Σ n − 1 ​ ( j) = i, Σ n − 1 − 1 ​ ( i) ∈ Fix ⁡ ( Σ n − 2), Σ n − 1 − 1 ​ ( i) > i, | Fix ⁡ ( Σ n − 2) | = m + 1) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}^{-1}(j)=i,\Sigma_{n-1}^{-1}(i)\in\operatorname{Fix}(\Sigma_{n-2}),\Sigma_{n-1}^{-1}(i)>i,|\operatorname{Fix}(\Sigma_{n-2})|=m+1) |  |

 | = 1 θ + n − 1 ⋅ m + 1 n − 2 ⋅ n − i − 1 θ + n − 2 ​ ℙ θ ( n − 2) ​ ( D n − 2, m + 1). \displaystyle\qquad=\frac{1}{\theta+n-1}\cdot\frac{m+1}{n-2}\cdot\frac{n-i-1}{\theta+n-2}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1}). |  |

Third and lastly, assume that j j chooses not to sit next to i i. We observe that j j cannot choose an empty table. Not being allowed to sit at an empty table either, i i must have chosen to sit to the left of some k i ∈ [n] ∖ { i, j } k_{i}\in[n]\setminus\{i,j\} (i.e., Σ n − 1 − 1 ​ ( i) = k i \Sigma_{n-1}^{-1}(i)=k_{i}). This k i k_{i} remains the right neighbor i i (i.e., Σ n − 1 ​ ( i) = k i \Sigma_{n}^{-1}(i)=k_{i}). Hence ( i, j) (i,j) is an inversion in this scenario if and only if j j sits down to the left of a person k j ∈ [n] ∖ { i, j } k_{j}\in[n]\setminus\{i,j\} with k i > k j k_{i}>k_{j}. For such k i, k j ∈ [n] ∖ { i, j } k_{i},k_{j}\in[n]\setminus\{i,j\}, a symmetry argument yields

 | ℙ θ ( n) ​ ( | Fix ⁡ ( Σ n) | = m, | Fix ⁡ ( Σ n − 2) | = m + 1, Σ n − 1 ​ ( j) = k j, Σ n − 1 − 1 ​ ( i) = k i) \displaystyle\mathbb{P}_{\theta}^{(n)}(|\operatorname{Fix}(\Sigma_{n})|=m,|\operatorname{Fix}(\Sigma_{n-2})|=m+1,\Sigma_{n}^{-1}(j)=k_{j},\Sigma_{n-1}^{-1}(i)=k_{i}) |  |

 | = ℙ θ ( n) ​ ( Σ n − 1 ​ ( j) = k j, Σ n − 1 − 1 ​ ( i) = k i, k i ∈ Fix ⁡ ( Σ n − 2), k j ∉ Fix ⁡ ( Σ n − 2), | Fix ⁡ ( Σ n − 2) | = m + 1) \displaystyle\qquad=\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}^{-1}(j)=k_{j},\Sigma_{n-1}^{-1}(i)=k_{i},k_{i}\in\operatorname{Fix}(\Sigma_{n-2}),k_{j}\not\in\operatorname{Fix}(\Sigma_{n-2}),|\operatorname{Fix}(\Sigma_{n-2})|=m+1) |  |

 | + ℙ θ ( n) ​ ( Σ n − 1 ​ ( j) = k j, Σ n − 1 − 1 ​ ( i) = k i, k i ∉ Fix ⁡ ( Σ n − 2), k j ∈ Fix ⁡ ( Σ n − 2), | Fix ⁡ ( Σ n − 2) | = m + 1) \displaystyle\qquad\quad+\mathbb{P}_{\theta}^{(n)}(\Sigma_{n}^{-1}(j)=k_{j},\Sigma_{n-1}^{-1}(i)=k_{i},k_{i}\not\in\operatorname{Fix}(\Sigma_{n-2}),k_{j}\in\operatorname{Fix}(\Sigma_{n-2}),|\operatorname{Fix}(\Sigma_{n-2})|=m+1) |  |

 | = 2 ⋅ 1 θ + n − 1 ⋅ 1 θ + n − 2 ⋅ ( m + 1) ​ ( ( n − 2) − ( m + 1)) ( n − 2) ​ ( n − 3) ​ 𝟙 n > 3 ​ ℙ θ ( n − 2) ​ ( D n − 2, m + 1). \displaystyle\qquad=2\cdot\frac{1}{\theta+n-1}\cdot\frac{1}{\theta+n-2}\cdot\frac{(m+1)((n-2)-(m+1))}{(n-2)(n-3)}\mathbbm{1}_{n>3}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1}). |  |

Using ( [3.6][29]), we deduce

 | ℙ θ ( n) ( A ∩ { | Fix ( Σ n − 2) | = m + 1, Σ n ( j) ≠ i, Σ n − 1 ( j) ≠ i) }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m+1,\Sigma_{n}(j)\neq i,\Sigma_{n}^{-1}(j)\neq i)\}) |  |

 | = ∑ k i, k j ∈ [n] ∖ { i, j } 𝟙 k i > k j ​ ℙ θ ( n) ​ ( | Fix ⁡ ( Σ n) | = m, | Fix ⁡ ( Σ n − 2) | = m + 1, Σ n − 1 ​ ( j) = k j, Σ n − 1 − 1 ​ ( i) = k i) \displaystyle\qquad=\sum_{k_{i},k_{j}\in[n]\setminus\{i,j\}}\mathbbm{1}_{k_{i}>k_{j}}\mathbb{P}_{\theta}^{(n)}(|\operatorname{Fix}(\Sigma_{n})|=m,|\operatorname{Fix}(\Sigma_{n-2})|=m+1,\Sigma_{n}^{-1}(j)=k_{j},\Sigma_{n-1}^{-1}(i)=k_{i}) |  |

 | = ( m + 1) ​ ( n − m − 3) ( θ + n − 1) ​ ( θ + n − 2) ​ ℙ θ ( n − 2) ​ ( D n − 2, m + 1). \displaystyle\qquad=\frac{(m+1)(n-m-3)}{(\theta+n-1)(\theta+n-2)}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1}). |  |

(The indicator 𝟙 n > 3 \mathbbm{1}_{n>3} can be omitted since n = 3 n=3 implies ( n − m − 3) ​ ℙ θ ( n − 2) ​ ( D n − 2, m + 1) = 0 (n-m-3)\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1})=0.) Combining this with the probabilities covering the other two seating choices of j j treated above, we get

(3.8) |  |  | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m + 1 }) \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m+1\}) |  |

 |  | = m + 1 ( θ + n − 1) ​ ( θ + n − 2) ​ ( n + j − i − 3 n − 2 + ( n − m − 3)) ​ ℙ θ ( n − 2) ​ ( D n − 2, m + 1). \displaystyle\qquad=\frac{m+1}{(\theta+n-1)(\theta+n-2)}\left(\frac{n+j-i-3}{n-2}+(n-m-3)\right)\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1}). |  |

Finally, consider the situation with m + 2 m+2 singleton tables when n − 2 n-2 persons are seated. Then persons i i and j j have to join two distinct such singleton tables. By symmetry, this leads to ( i, j) (i,j) being an inversion with conditional probability 1 2 \frac{1}{2}. Thus we have

(3.9) |  |  | ℙ θ ( n) ​ ( A ∩ { | Fix ⁡ ( Σ n − 2) | = m + 2 }) = 1 2 ⋅ m + 1 θ + n − 1 ⋅ m + 2 θ + n − 2 ​ ℙ θ ( n − 2) ​ ( D n − 2, m + 2). \displaystyle\mathbb{P}_{\theta}^{(n)}(A\cap\{|\operatorname{Fix}(\Sigma_{n-2})|=m+2\})=\frac{1}{2}\cdot\frac{m+1}{\theta+n-1}\cdot\frac{m+2}{\theta+n-2}\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+2}). |  |

Dividing equations ( [3.4][30]), ( [3.5][31]), ( [3.7][32]), ( [3.8][33]) and ( [3.9][34]) by ℙ θ ( n) ​ ( D n, m) \mathbb{P}_{\theta}^{(n)}(D_{n,m}) and adding them up, we obtain ( [3.2][35]).

( b) (b) We start by observing

 | 𝔼 θ ( n) ​ [| Inv ⁡ ( Σ n) | | D n, m] = \displaystyle\mathbb{E}_{\theta}^{(n)}\big[|\operatorname{Inv}(\Sigma_{n})|\big|D_{n,m}\big]={} | ∑ i, j ∈ [n], i < j ℙ θ ( n) ​ ( ( i, j) ∈ Inv ⁡ ( Σ n) | D n, m). \displaystyle\sum_{i,j\in[n],\,i<j}\mathbb{P}_{\theta}^{(n)}\big((i,j)\in\operatorname{Inv}(\Sigma_{n})\big|D_{n,m}\big). |  |

Inserting ( [3.2][35]) into this equation, using ∑ i, j ∈ [n], i < j ( j − i) = ( n + 1 3) \sum_{i,j\in[n],\,i<j}(j-i)=\binom{n+1}{3} (cf. ( [2.2][36])) and simplifying the result, we end up with ( [3.3][37]). ∎

###### Proof of Theorem [5][38].

Unless explicitly indicated otherwise, all asymptotic expansions in this proof are expansions as n → ∞ n\to\infty. Let b ∈ ℕ 0 b\in\mathbb{N}_{0}. We note that θ ( b) = Γ ​ ( θ + b) Γ ​ ( θ) \theta^{(b)}=\frac{\Gamma(\theta+b)}{\Gamma(\theta)}, where Γ \Gamma denotes the Gamma function. In view of Proposition [10][17] and Proposition [4][22], we start by analyzing the asymptotic behavior of

(3.10) |  | G b ​ ( n):= ∑ k = 0 n − b ( − θ) k ​ θ ( n − b − k) k! ​ ( n − b − k)! = 1 Γ ​ ( θ) ​ ∑ k = 0 n − b ( − θ) k ​ Γ ​ ( θ + n − b − k) k! ​ Γ ​ ( 1 + n − b − k). \displaystyle G_{b}(n):=\sum_{k=0}^{n-b}\frac{(-\theta)^{k}\theta^{(n-b-k)}}{k!(n-b-k)!}=\frac{1}{\Gamma(\theta)}\sum_{k=0}^{n-b}\frac{(-\theta)^{k}\Gamma(\theta+n-b-k)}{k!\Gamma(1+n-b-k)}. |  |

Let l n:= ⌊ log ⁡ ( n) ⌋ l_{n}:=\lfloor\log(n)\rfloor. Noting that 1 ( l n + 1)! \frac{1}{(l_{n}+1)!} decays superpolynomially, we get

(3.11) |  | | ∑ k = l n + 1 n − b ( − θ) k ​ θ ( n − b − k) k! ​ ( n − b − k)! | ≤ \displaystyle\left|\sum_{k=l_{n}+1}^{n-b}\frac{(-\theta)^{k}\theta^{(n-b-k)}}{k!(n-b-k)!}\right|\leq{} | ∑ k = l n + 1 n − b θ k ​ ( ⌈ θ ⌉ + n − b − k)! k! ​ ( n − b − k)! \displaystyle\sum_{k=l_{n}+1}^{n-b}\frac{\theta^{k}(\lceil\theta\rceil+n-b-k)!}{k!(n-b-k)!} |  |

 | ≤ \displaystyle\leq{} | ( ⌈ θ ⌉ + n) ⌈ θ ⌉ ​ ∑ k = l n + 1 ∞ θ k k! ≤ ( ⌈ θ ⌉ + n) ⌈ θ ⌉ ​ e θ ( l n + 1)! = O ​ ( 1 n 4). \displaystyle(\lceil\theta\rceil+n)^{\lceil\theta\rceil}\sum_{k=l_{n}+1}^{\infty}\frac{\theta^{k}}{k!}\leq(\lceil\theta\rceil+n)^{\lceil\theta\rceil}\frac{\operatorname{e}^{\theta}}{(l_{n}+1)!}=O\left(\frac{1}{n^{4}}\right). |  |

We now focus on the truncated sum up to k = l n k=l_{n}. For all α, β ∈ ℝ \alpha,\beta\in\mathbb{R} and as z → ∞ z\to\infty, [[TE51][39]] yields

 | Γ ​ ( α + z) Γ ​ ( β + z) = z α − β ​ [1 + ( α − β) ​ ( α + β − 1) 2 ​ z + ( α − β 2) ​ 3 ​ ( α + β − 1) 2 − α + β − 1 12 ​ z 2 + O ​ ( 1 z 3)]. \displaystyle\frac{\Gamma(\alpha+z)}{\Gamma(\beta+z)}=z^{\alpha-\beta}\left[1+\frac{(\alpha-\beta)(\alpha+\beta-1)}{2z}+\binom{\alpha-\beta}{2}\frac{3(\alpha+\beta-1)^{2}-\alpha+\beta-1}{12z^{2}}+O\left(\frac{1}{z^{3}}\right)\right]. |  |

This implies

 | Γ ​ ( θ + n − b − k) Γ ​ ( 1 + n − b − k) = ( n − b − k) θ − 1 ​ [1 + ( θ − 1) ​ θ 2 ​ ( n − b − k) + ( θ − 1 2) ​ 3 ​ θ 2 − θ 12 ​ ( n − b − k) 2 + O ​ ( 1 n 3)], \displaystyle\frac{\Gamma(\theta+n-b-k)}{\Gamma(1+n-b-k)}=(n-b-k)^{\theta-1}\left[1+\frac{(\theta-1)\theta}{2(n-b-k)}+\binom{\theta-1}{2}\frac{3\theta^{2}-\theta}{12(n-b-k)^{2}}+O\left(\frac{1}{n^{3}}\right)\right], |  |

uniformly over k ∈ { 0, …, l n } k\in\{0,\dots,l_{n}\}, entailing

 | H b ​ ( n):= \displaystyle H_{b}(n):={} | ∑ k = 0 l n ( − θ) k ​ Γ ​ ( θ + n − b − k) k! ​ Γ ​ ( 1 + n − b − k) \displaystyle\sum_{k=0}^{l_{n}}\frac{(-\theta)^{k}\Gamma(\theta+n-b-k)}{k!\Gamma(1+n-b-k)} |  |

 | = \displaystyle={} | ∑ k = 0 l n ( − θ) k k! ​ ( n − b − k) θ − 1 \displaystyle\sum_{k=0}^{l_{n}}\frac{(-\theta)^{k}}{k!}(n-b-k)^{\theta-1} |  |

 |  | + ∑ k = 0 l n ( − θ) k k! ⋅ θ ​ ( θ − 1) 2 ​ ( n − b − k) θ − 2 \displaystyle+\sum_{k=0}^{l_{n}}\frac{(-\theta)^{k}}{k!}\cdot\frac{\theta(\theta-1)}{2}(n-b-k)^{\theta-2} |  |

 |  | + ∑ k = 0 l n ( − θ) k k! ⋅ ( θ − 1) ​ ( θ − 2) ​ ( 3 ​ θ 2 − θ) 24 ​ ( n − b − k) θ − 3 \displaystyle+\sum_{k=0}^{l_{n}}\frac{(-\theta)^{k}}{k!}\cdot\frac{(\theta-1)(\theta-2)(3\theta^{2}-\theta)}{24}(n-b-k)^{\theta-3} |  |

 |  | + ∑ k = 0 l n ( − θ) k k! ​ O ​ ( n θ − 4). \displaystyle+\sum_{k=0}^{l_{n}}\frac{(-\theta)^{k}}{k!}O(n^{\theta-4}). |  |

Observing

 | ( n − b − k) θ − a = \displaystyle(n-b-k)^{\theta-a}={} | n θ − a ​ ( 1 − b + k n) θ − a \displaystyle n^{\theta-a}\left(1-\frac{b+k}{n}\right)^{\theta-a} |  |

 | = \displaystyle={} | n θ − a ​ [1 − ( θ − a) ​ ( b + k) n + ( θ − a) ​ ( θ − a − 1) ​ ( b + k) 2 2 ​ n 2 + O ​ ( 1 n 3)], \displaystyle n^{\theta-a}\left[1-\frac{(\theta-a)(b+k)}{n}+\frac{(\theta-a)(\theta-a-1)(b+k)^{2}}{2n^{2}}+O\left(\frac{1}{n^{3}}\right)\right], |  |

uniformly over k ∈ { 0, …, l n } k\in\{0,\dots,l_{n}\} and a ∈ { 1, 2, 3 } a\in\{1,2,3\}, we deduce

(3.12) |  | H b ​ ( n) = \displaystyle H_{b}(n)={} | n θ − 1 ​ ∑ k = 0 l n ( − θ) k k! + n θ − 2 ​ ∑ k = 0 l n ( − θ) k k! ​ [θ ​ ( θ − 1) 2 − ( θ − 1) ​ ( b + k)] \displaystyle n^{\theta-1}\sum_{k=0}^{l_{n}}\frac{(-\theta)^{k}}{k!}+n^{\theta-2}\sum_{k=0}^{l_{n}}\frac{(-\theta)^{k}}{k!}\left[\frac{\theta(\theta-1)}{2}-(\theta-1)(b+k)\right] |  |

 |  | + n θ − 3 ​ ∑ k = 0 l n ( − θ) k k! ⋅ ( θ − 1) ​ ( θ − 2) 2 ​ [3 ​ θ 2 − θ 12 − θ ​ ( b + k) + ( b + k) 2] + O ​ ( n θ − 4). \displaystyle+n^{\theta-3}\sum_{k=0}^{l_{n}}\frac{(-\theta)^{k}}{k!}\cdot\frac{(\theta-1)(\theta-2)}{2}\left[\frac{3\theta^{2}-\theta}{12}-\theta(b+k)+(b+k)^{2}\right]+O(n^{\theta-4}). |  |

Similar to ( [3.11][40]), the superpolynomial decay of 1 ( l n + 1)! \frac{1}{(l_{n}+1)!} yields

 | ∑ k = 0 l n ( − θ) k k! = \displaystyle\sum_{k=0}^{l_{n}}\frac{(-\theta)^{k}}{k!}={} | e − θ + O ​ ( 1 n 3), \displaystyle\operatorname{e}^{-\theta}+O\left(\frac{1}{n^{3}}\right), |  |

(3.13) |  | ∑ k = 0 l n ( − θ) k k! ​ k = \displaystyle\sum_{k=0}^{l_{n}}\frac{(-\theta)^{k}}{k!}k={} | − θ ​ ∑ k = 0 l n − 1 ( − θ) k k! = − θ ​ e − θ + O ​ ( 1 n 3), \displaystyle-\theta\sum_{k=0}^{l_{n}-1}\frac{(-\theta)^{k}}{k!}=-\theta\operatorname{e}^{-\theta}+O\left(\frac{1}{n^{3}}\right), |  |

 | ∑ k = 0 l n ( − θ) k k! ​ k 2 = \displaystyle\sum_{k=0}^{l_{n}}\frac{(-\theta)^{k}}{k!}k^{2}={} | θ 2 ​ ∑ k = 0 l n − 2 ( − θ) k k! − θ ​ ∑ k = 0 l n − 1 ( − θ) k k! = θ ​ ( θ − 1) ​ e − θ + O ​ ( 1 n 3). \displaystyle\theta^{2}\sum_{k=0}^{l_{n}-2}\frac{(-\theta)^{k}}{k!}-\theta\sum_{k=0}^{l_{n}-1}\frac{(-\theta)^{k}}{k!}=\theta(\theta-1)\operatorname{e}^{-\theta}+O\left(\frac{1}{n^{3}}\right). |  |

Hence ( [3.10][41])-( [3][42]) imply

(3.14) |  | G b ​ ( n) = \displaystyle G_{b}(n)={} | H b ​ ( n) Γ ​ ( θ) + O ​ ( 1 n 4) = n θ − 1 Γ ​ ( θ) ​ e θ ​ [1 + 1 n ​ A 1 ​ ( b) + 1 n 2 ​ A 2 ​ ( b) + O ​ ( 1 n 3)], \displaystyle\frac{H_{b}(n)}{\Gamma(\theta)}+O\left(\frac{1}{n^{4}}\right)=\frac{n^{\theta-1}}{\Gamma(\theta)\operatorname{e}^{\theta}}\bigg[1+\frac{1}{n}A_{1}(b)+\frac{1}{n^{2}}A_{2}(b)+O\left(\frac{1}{n^{3}}\right)\bigg], |  |

with

(3.15) |  | A 1 ​ ( b):= \displaystyle A_{1}(b):={} | θ ​ ( θ − 1) 2 − ( θ − 1) ​ ( b − θ) = θ − 1 2 ​ ( 3 ​ θ − 2 ​ b) \displaystyle\frac{\theta(\theta-1)}{2}-(\theta-1)(b-\theta)=\frac{\theta-1}{2}(3\theta-2b) |  |

and

(3.16) |  | A 2 ​ ( b):= \displaystyle A_{2}(b):={} | ( θ − 1) ​ ( θ − 2) 2 ​ ( 3 ​ θ 2 − θ 12 − θ ​ ( b − θ) + b 2 − 2 ​ b ​ θ + θ ​ ( θ − 1)) \displaystyle\frac{(\theta-1)(\theta-2)}{2}\left(\frac{3\theta^{2}-\theta}{12}-\theta(b-\theta)+b^{2}-2b\theta+\theta(\theta-1)\right) |  |

 | = \displaystyle={} | ( θ − 1) ​ ( θ − 2) 2 ​ ( b 2 − 3 ​ b ​ θ + θ ​ 27 ​ θ − 13 12). \displaystyle\frac{(\theta-1)(\theta-2)}{2}\left(b^{2}-3b\theta+\theta\frac{27\theta-13}{12}\right). |  |

Now let a ∈ { − 1, 0, 1, 2 } a\in\{-1,0,1,2\}. Using a geometric series expansion to rewrite the denominator, it follows from ( [3.14][43]), ( [3.15][44]) and ( [3.16][45]) that

(3.17) |  | G m + 2 + a ​ ( n) G m ​ ( n) = \displaystyle\frac{G_{m+2+a}(n)}{G_{m}(n)}={} | 1 + 1 n ​ A 1 ​ ( m + 2 + a) + 1 n 2 ​ A 2 ​ ( m + 2 + a) + O ​ ( 1 n 3) 1 + 1 n ​ A 1 ​ ( m) + 1 n 2 ​ A 2 ​ ( m) + O ​ ( 1 n 3) \displaystyle\frac{1+\frac{1}{n}A_{1}(m+2+a)+\frac{1}{n^{2}}A_{2}(m+2+a)+O\left(\frac{1}{n^{3}}\right)}{1+\frac{1}{n}A_{1}(m)+\frac{1}{n^{2}}A_{2}(m)+O\left(\frac{1}{n^{3}}\right)} |  |

 | = \displaystyle={} | [1 + A 1 ​ ( m + 2 + a) n + A 2 ​ ( m + 2 + a) n 2 + O ​ ( 1 n 3)] \displaystyle\left[1+\frac{A_{1}(m+2+a)}{n}+\frac{A_{2}(m+2+a)}{n^{2}}+O\left(\frac{1}{n^{3}}\right)\right] |  |

 |  | ⋅ [1 − A 1 ​ ( m) n − A 2 ​ ( m) n 2 + ( A 1 ​ ( m)) 2 n 2 + O ​ ( 1 n 3)] \displaystyle\cdot\left[1-\frac{A_{1}(m)}{n}-\frac{A_{2}(m)}{n^{2}}+\frac{(A_{1}(m))^{2}}{n^{2}}+O\left(\frac{1}{n^{3}}\right)\right] |  |

 | = \displaystyle={} | 1 + B 1 ​ ( m, a) n + B 2 ​ ( m, a) n 2 + O ​ ( 1 n 3), \displaystyle 1+\frac{B_{1}(m,a)}{n}+\frac{B_{2}(m,a)}{n^{2}}+O\left(\frac{1}{n^{3}}\right), |  |

with

(3.18) |  | B 1 ​ ( m, a):= \displaystyle B_{1}(m,a):={} | A 1 ​ ( m + 2 + a) − A 1 ​ ( m) = − ( 2 + a) ​ ( θ − 1) \displaystyle A_{1}(m+2+a)-A_{1}(m)=-(2+a)(\theta-1) |  |

and

(3.19) |  | B 2 ​ ( m, a):= \displaystyle B_{2}(m,a):={} | A 2 ​ ( m + 2 + a) − A 1 ​ ( m + 2 + a) ​ A 1 ​ ( m) − A 2 ​ ( m) + ( A 1 ​ ( m)) 2 \displaystyle A_{2}(m+2+a)-A_{1}(m+2+a)A_{1}(m)-A_{2}(m)+(A_{1}(m))^{2} |  |

 | = \displaystyle={} | ( 2 + a) ​ ( θ − 1) 2 ​ ( ( 5 + a) ​ θ − 2 ​ ( m + 2 + a)). \displaystyle\frac{(2+a)(\theta-1)}{2}((5+a)\theta-2(m+2+a)). |  |

Combining ( [3.10][41]) and ( [3.17][46]) with Proposition [4][22], we obtain

(3.20) |  |  | 1 ( θ + n − 1) ​ ( θ + n − 2) ⋅ ℙ θ ( n − 2) ​ ( D n − 2, m + a) ℙ θ ( n) ​ ( D n, m) \displaystyle\frac{1}{(\theta+n-1)(\theta+n-2)}\cdot\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+a})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})} |  |

 |  | = m! ​ θ a ( m + a)! ​ n ​ ( n − 1) ⋅ G m + 2 + a ​ ( n) G m ​ ( n) \displaystyle\qquad=\frac{m!\theta^{a}}{(m+a)!n(n-1)}\cdot\frac{G_{m+2+a}(n)}{G_{m}(n)} |  |

 |  | = m! ​ θ a ( m + a)! ​ n ​ ( n − 1) ​ [1 + B 1 ​ ( m, a) n + B 2 ​ ( m, a) n 2 + O ​ ( 1 n 3)]. \displaystyle\qquad=\frac{m!\theta^{a}}{(m+a)!n(n-1)}\left[1+\frac{B_{1}(m,a)}{n}+\frac{B_{2}(m,a)}{n^{2}}+O\left(\frac{1}{n^{3}}\right)\right]. |  |

(In the special case ( m, a) = ( 0, − 1) (m,a)=(0,-1), this trivially holds under the convention 0! ( − 1)!:= 0 \frac{0!}{(-1)!}:=0.) To complete the proof of part ( b) (b), it remains to insert ( [3.20][47]) into ( [3.3][37]), use ( [3.18][48]) and ( [3.19][49]), and simplify the resulting expression.

Regarding part ( a) (a), we additionally observe

 | 1 n − 1 = 1 n + 1 n 2 + 1 n 3 + O ​ ( 1 n 4). \frac{1}{n-1}=\frac{1}{n}+\frac{1}{n^{2}}+\frac{1}{n^{3}}+O\left(\frac{1}{n^{4}}\right). |  |

Thus, using ( [3.18][48]) and ( [3.19][49]), equation ( [3.20][47]) can be rewritten as

 | 1 ( θ + n − 1) ​ ( θ + n − 2) ⋅ ℙ θ ( n − 2) ​ ( D n − 2, m + a) ℙ θ ( n) ​ ( D n, m) \displaystyle\frac{1}{(\theta+n-1)(\theta+n-2)}\cdot\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+a})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})} |  |

 | = m! ​ θ a ( m + a)! ​ [1 n 2 + 1 − ( 2 + a) ​ ( θ − 1) n 3 + 2 + ( 2 + a) ​ ( θ − 1) ​ ( ( 5 + a) ​ θ − 2 ​ ( m + 3 + a)) 2 ​ n 4 + O ​ ( 1 n 5)]. \displaystyle\qquad=\frac{m!\theta^{a}}{(m+a)!}\left[\frac{1}{n^{2}}+\frac{1-(2+a)(\theta-1)}{n^{3}}+\frac{2+(2+a)(\theta-1)((5+a)\theta-2(m+3+a))}{2n^{4}}+O\left(\frac{1}{n^{5}}\right)\right]. |  |

Inserting this (the O ​ ( 1 / n 4) O(1/n^{4}) -term is only needed for a = 0 a=0) together with

 | 1 n − 2 = 1 n + 2 n 2 + O ​ ( 1 n 3) \frac{1}{n-2}=\frac{1}{n}+\frac{2}{n^{2}}+O\left(\frac{1}{n^{3}}\right) |  |

into ( [3.2][35]), it remains to simplify the resulting expression. ∎

###### Proof of Theorem [8][21].

Let l ∈ ℕ l\in\mathbb{N}. By the definition of the Ewens sampling distribution, we have

 | ℙ θ ( l) ​ ( D l, 0) = 1 θ ( l) ​ ∑ k = 1 l a l, k ​ θ k, \mathbb{P}_{\theta}^{(l)}(D_{l,0})=\frac{1}{\theta^{(l)}}\sum_{k=1}^{l}a_{l,k}\theta^{k}, |  |

with

 | a l, k:= | { π ∈ S l: N ​ ( π) = k, Fix ⁡ ( π) = ∅ } |, k ∈ [l], a_{l,k}:=|\{\pi\in S_{l}:N(\pi)=k,\,\operatorname{Fix}(\pi)=\emptyset\}|,\quad k\in[l], |  |

being the number of derangements in S l S_{l} with exactly k k cycles. Observing a l, k = 0 a_{l,k}=0 for all k ∈ [l] k\in[l] with k > l 2 k>\frac{l}{2}, we get

(3.21) |  | lim θ → ∞ θ ⌈ l / 2 ⌉ ​ ℙ θ ( l) ​ ( D l, 0) = a l, ⌊ l / 2 ⌋. \lim_{\theta\to\infty}\theta^{\lceil l/2\rceil}\mathbb{P}_{\theta}^{(l)}(D_{l,0})=a_{l,\lfloor l/2\rfloor}. |  |

If l l is even, π ∈ S l \pi\in S_{l} is a derangement with ⌊ l / 2 ⌋ \lfloor l/2\rfloor cycles if and only if it consists of exactly l / 2 l/2 two-cycles, entailing a l, ⌊ l / 2 ⌋ = ( l − 1)!! a_{l,\lfloor l/2\rfloor}=(l-1)!!. If l ≥ 3 l\geq 3 is odd, π ∈ S l \pi\in S_{l} is a derangement with ⌊ l / 2 ⌋ \lfloor l/2\rfloor cycles if and only if it consists of exactly 1 1 three-cycle and ( l − 3) / 2 (l-3)/2 two-cycles. Thus, for any odd l l, elementary combinatorics implies a l, ⌊ l / 2 ⌋ = 2 ​ ( l 3) ​ ( l − 4)!! a_{l,\lfloor l/2\rfloor}=2\binom{l}{3}(l-4)!!, with the conventions ( − 1)!!:= 1 (-1)!!:=1 and ( 1 3) ​ ( − 3)!!:= 0 \binom{1}{3}(-3)!!:=0.

For the time being, assume that n − m n-m is even. Using the first equality in Proposition [4][22] along with ( [3.21][50]) and the subsequent formulas, we obtain

 | lim θ → ∞ ℙ θ ( n − 2) ​ ( D n − 2, m) θ ​ ℙ θ ( n) ​ ( D n, m) = \displaystyle\lim_{\theta\to\infty}\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m})}{\theta\mathbb{P}_{\theta}^{(n)}(D_{n,m})}={} | lim θ → ∞ ( n − 2 m) ​ θ ⌈ ( n − m − 2) / 2 ⌉ ​ ℙ θ ( n − m − 2) ​ ( D n − m − 2, 0) ( n m) ​ θ ⌈ ( n − m) / 2 ⌉ ​ ℙ θ ( n − m) ​ ( D n − m, 0) \displaystyle\lim_{\theta\to\infty}\frac{\binom{n-2}{m}\theta^{\lceil(n-m-2)/2\rceil}\mathbb{P}_{\theta}^{(n-m-2)}(D_{n-m-2,0})}{\binom{n}{m}\theta^{\lceil(n-m)/2\rceil}\mathbb{P}_{\theta}^{(n-m)}(D_{n-m,0})} |  |

 | = \displaystyle={} | ( n − 2 m) ​ ( n − m − 3)!! ( n m) ​ ( n − m − 1)!! = n − m n ​ ( n − 1). \displaystyle\frac{\binom{n-2}{m}(n-m-3)!!}{\binom{n}{m}(n-m-1)!!}=\frac{n-m}{n(n-1)}. |  |

(For m = n − 2 m=n-2, this is true on account of our conventions.) Similarly (or trivially for m = n − 2 m=n-2), we get

 | lim θ → ∞ ℙ θ ( n − 2) ​ ( D n − 2, m + 2) θ 2 ​ ℙ θ ( n) ​ ( D n, m) = ( n − m) ​ ( n − m − 2) n ​ ( n − 1) ​ ( m + 2) ​ ( m + 1) \displaystyle\lim_{\theta\to\infty}\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+2})}{\theta^{2}\mathbb{P}_{\theta}^{(n)}(D_{n,m})}=\frac{(n-m)(n-m-2)}{n(n-1)(m+2)(m+1)} |  |

as well as

 | 0 = lim θ → ∞ ℙ θ ( n − 2) ​ ( D n − 2, m − 1) θ ​ ℙ θ ( n) ​ ( D n, m) = lim θ → ∞ ℙ θ ( n − 2) ​ ( D n − 2, m + 1) θ 2 ​ ℙ θ ( n) ​ ( D n, m). \displaystyle 0=\lim_{\theta\to\infty}\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m-1})}{\theta\mathbb{P}_{\theta}^{(n)}(D_{n,m})}=\lim_{\theta\to\infty}\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1})}{\theta^{2}\mathbb{P}_{\theta}^{(n)}(D_{n,m})}. |  |

It remains to combine these four limits with Proposition [10][17] and simplify the resulting expressions.

Now assume that n − m n-m is odd. Then a similar approach yields

 | lim θ → ∞ ℙ θ ( n − 2) ​ ( D n − 2, m − 1) θ ​ ℙ θ ( n) ​ ( D n, m) = \displaystyle\lim_{\theta\to\infty}\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m-1})}{\theta\mathbb{P}_{\theta}^{(n)}(D_{n,m})}={} | ( n − 2 m − 1) ​ θ ⌈ ( n − m − 1) / 2 ⌉ ​ ℙ θ ( n − m − 1) ​ ( D n − m − 1, 0) ( n m) ​ θ ⌈ ( n − m) / 2 ⌉ ​ ℙ θ ( n − m) ​ ( D n − m, 0) \displaystyle\frac{\binom{n-2}{m-1}\theta^{\lceil(n-m-1)/2\rceil}\mathbb{P}_{\theta}^{(n-m-1)}(D_{n-m-1,0})}{\binom{n}{m}\theta^{\lceil(n-m)/2\rceil}\mathbb{P}_{\theta}^{(n-m)}(D_{n-m,0})} |  |

 | = \displaystyle={} | ( n − 2 m − 1) ​ ( n − m − 2)!! ( n m) ​ 2 ​ ( n − m 3) ​ ( n − m − 4)!! = 3 ​ m n ​ ( n − 1) ​ ( n − m − 1) \displaystyle\frac{\binom{n-2}{m-1}(n-m-2)!!}{\binom{n}{m}2\binom{n-m}{3}(n-m-4)!!}=\frac{3m}{n(n-1)(n-m-1)} |  |

(which is trivial for m = 0 m=0) and

 | lim θ → ∞ ℙ θ ( n − 2) ​ ( D n − 2, m + 1) θ 2 ​ ℙ θ ( n) ​ ( D n, m) = 3 n ​ ( n − 1) ​ ( m + 1) \displaystyle\lim_{\theta\to\infty}\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1})}{\theta^{2}\mathbb{P}_{\theta}^{(n)}(D_{n,m})}=\frac{3}{n(n-1)(m+1)} |  |

as well as

 | lim θ → ∞ ℙ θ ( n − 2) ​ ( D n − 2, m) θ ​ ℙ θ ( n) ​ ( D n, m) = \displaystyle\lim_{\theta\to\infty}\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m})}{\theta\mathbb{P}_{\theta}^{(n)}(D_{n,m})}={} | ( n − 2 m) ​ θ ⌈ ( n − m − 2) / 2 ⌉ ​ ℙ θ ( n − m − 2) ​ ( D n − m − 2, 0) ( n m) ​ θ ⌈ ( n − m) / 2 ⌉ ​ ℙ θ ( n − m) ​ ( D n − m, 0) \displaystyle\frac{\binom{n-2}{m}\theta^{\lceil(n-m-2)/2\rceil}\mathbb{P}_{\theta}^{(n-m-2)}(D_{n-m-2,0})}{\binom{n}{m}\theta^{\lceil(n-m)/2\rceil}\mathbb{P}_{\theta}^{(n-m)}(D_{n-m,0})} |  |

 | = \displaystyle={} | ( n − 2 m) ​ 2 ​ ( n − m − 2 3) ​ ( n − m − 6)!! ( n m) ​ 2 ​ ( n − m 3) ​ ( n − m − 4)!! = n − m − 3 n ​ ( n − 1) \displaystyle\frac{\binom{n-2}{m}2\binom{n-m-2}{3}(n-m-6)!!}{\binom{n}{m}2\binom{n-m}{3}(n-m-4)!!}=\frac{n-m-3}{n(n-1)} |  |

and

 | lim θ → ∞ ℙ θ ( n − 2) ​ ( D n − 2, m + 2) θ 2 ​ ℙ θ ( n) ​ ( D n, m) = ( n − m − 3) ​ ( n − m − 5) n ​ ( n − 1) ​ ( m + 2) ​ ( m + 1). \displaystyle\lim_{\theta\to\infty}\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+2})}{\theta^{2}\mathbb{P}_{\theta}^{(n)}(D_{n,m})}=\frac{(n-m-3)(n-m-5)}{n(n-1)(m+2)(m+1)}. |  |

Again, it remains to combine these limits with Proposition [10][17] and to simplify the resulting expressions. ∎

###### Proof of Proposition [9][51].

For the time being, assume m < n − 2 m<n-2. We have

 | lim θ → 0 1 θ ​ ∑ k = 0 l ( − θ) k ​ θ ( l − k) k! ​ ( l − k)! = 1 l ​ 𝟙 l ≠ 1, l ∈ ℕ, \lim_{\theta\to 0}\frac{1}{\theta}\sum_{k=0}^{l}\frac{(-\theta)^{k}\theta^{(l-k)}}{k!(l-k)!}=\frac{1}{l}\mathbbm{1}_{l\neq 1},\quad l\in\mathbb{N}, |  |

because only the summand corresponding to k = 0 k=0 matters asymptotically if l ≠ 1 l\neq 1, while the sum is 0 if l = 1 l=1. Together with Proposition [4][22] (for m = 0 m=0, the calculation is trivial), we get

 | lim θ → 0 θ ​ ℙ θ ( n − 2) ​ ( D n − 2, m − 1) ℙ θ ( n) ​ ( D n, m) = \displaystyle\lim_{\theta\to 0}\theta\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m-1})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})}={} | lim θ → 0 m ​ ( θ + n − 1) ​ ( θ + n − 2) ​ ∑ k = 0 n − m − 1 ( − θ) k ​ θ ( n − m − 1 − k) k! ​ ( n − m − 1 − k)! n ​ ( n − 1) ​ ∑ k = 0 n − m ( − θ) k ​ θ ( n − m − k) k! ​ ( n − m − k)! \displaystyle\lim_{\theta\to 0}\frac{m(\theta+n-1)(\theta+n-2)\sum_{k=0}^{n-m-1}\frac{(-\theta)^{k}\theta^{(n-m-1-k)}}{k!(n-m-1-k)!}}{n(n-1)\sum_{k=0}^{n-m}\frac{(-\theta)^{k}\theta^{(n-m-k)}}{k!(n-m-k)!}} |  |

 | = \displaystyle={} | m ​ ( n − 2) ​ 1 n − m − 1 n ​ 1 n − m. \displaystyle\frac{m(n-2)\frac{1}{n-m-1}}{n\frac{1}{n-m}}. |  |

Similarly, we obtain

 | lim θ → 0 ℙ θ ( n − 2) ​ ( D n − 2, m) ℙ θ ( n) ​ ( D n, m) = \displaystyle\lim_{\theta\to 0}\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})}={} | ( n − 2) ​ 1 n − m − 2 n ​ 1 n − m ​ 𝟙 m ≠ n − 3 \displaystyle\frac{(n-2)\frac{1}{n-m-2}}{n\frac{1}{n-m}}\mathbbm{1}_{m\neq n-3} |  |

as well as

 | lim θ → 0 ℙ θ ( n − 2) ​ ( D n − 2, m + 1) ℙ θ ( n) ​ ( D n, m) = 0 and lim θ → 0 ℙ θ ( n − 2) ​ ( D n − 2, m + 2) ℙ θ ( n) ​ ( D n, m) = 0. \displaystyle\lim_{\theta\to 0}\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+1})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})}=0\quad\text{and}\quad\lim_{\theta\to 0}\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,m+2})}{\mathbb{P}_{\theta}^{(n)}(D_{n,m})}=0. |  |

It remains to combine these limits with Proposition [10][17] and to simplify the resulting expressions.

In the special case m = n − 2 m=n-2, we trivially have

 | ℙ θ ( n − 2) ​ ( D n − 2, ( n − 2) − 1) ℙ θ ( n) ​ ( D n, n − 2) = ℙ θ ( n − 2) ​ ( D n − 2, ( n − 2) + 1) ℙ θ ( n) ​ ( D n, n − 2) = ℙ θ ( n − 2) ​ ( D n − 2, ( n − 2) + 2) ℙ θ ( n) ​ ( D n, n − 2) = 0, θ > 0. \displaystyle\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,(n-2)-1})}{\mathbb{P}_{\theta}^{(n)}(D_{n,n-2})}=\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,(n-2)+1})}{\mathbb{P}_{\theta}^{(n)}(D_{n,n-2})}=\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,(n-2)+2})}{\mathbb{P}_{\theta}^{(n)}(D_{n,n-2})}=0,\quad\theta>0. |  |

Using Proposition [4][22] or elementary combinatorics, we further get

 | lim θ → 0 θ ​ ℙ θ ( n − 2) ​ ( D n − 2, n − 2) ℙ θ ( n) ​ ( D n, n − 2) = \displaystyle\lim_{\theta\to 0}\theta\frac{\mathbb{P}_{\theta}^{(n-2)}(D_{n-2,n-2})}{\mathbb{P}_{\theta}^{(n)}(D_{n,n-2})}={} | lim θ → 0 2 ​ ( θ + n − 1) ​ ( θ + n − 2) n ​ ( n − 1) = 2 ​ ( n − 2) n. \displaystyle\lim_{\theta\to 0}\frac{2(\theta+n-1)(\theta+n-2)}{n(n-1)}=\frac{2(n-2)}{n}. |  |

Together with Proposition [10][17], this yields the claim for m = n − 2 m=n-2. ∎

## References

- [ABT03] Richard Arratia, A. D. Barbour, and Simon Tavaré. Logarithmic combinatorial structures: a probabilistic approach. EMS Monographs in Mathematics. European Mathematical Society (EMS), Zürich, 2003.
- [Ald85] David J. Aldous. Exchangeability and related topics. In École d’été de probabilités de Saint-Flour, XIII—1983, volume 1117 of Lecture Notes in Math., pages 1–198. Springer, Berlin, 1985.
- [Cra16] Harry Crane. The ubiquitous Ewens sampling formula. Statist. Sci., 31(1):1–19, 2016.
- [Ewe72] W. J. Ewens. The sampling theory of selectively neutral alleles. Theoret. Population Biol., 3, 1972.
- [GP18] Alexey Gladkich and Ron Peled. On the cycle structure of Mallows permutations. Ann. Probab., 46(2):1114–1169, 2018.
- [JKB97] Norman L. Johnson, Samuel Kotz, and N. Balakrishnan. Discrete multivariate distributions. Wiley Series in Probability and Statistics: Applied Probability and Statistics. John Wiley & Sons, Inc., New York, 1997. A Wiley-Interscience Publication.
- [Pin14] Ross G. Pinsky. Problems from the discrete to the continuous. Probability, number theory, graph theory, and combinatorics. Universitext. Springer, Cham, 2014.
- [Pin25] Ross G. Pinsky. The inversion statistic in derangements and in other permutations with a prescribed number of fixed points. arXiv:2505.02058 [math.PR], 2025.
- [Pit06] J. Pitman. Combinatorial stochastic processes. volume 1875 of Lecture Notes in Math. Springer, Berlin, 2006.
- [TE51] F. G. Tricomi and A. Erdélyi. The asymptotic expansion of a ratio of gamma functions. Pacific J. Math., 1:133–142, 1951.


## Links

[1]: https://arxiv.org/html/2510.20654v2#bib.bibx5
[2]: https://arxiv.org/html/2510.20654v2#bib.bibx8
[3]: https://arxiv.org/html/2510.20654v2#bib.bibx2
[4]: https://arxiv.org/html/2510.20654v2#bib.bibx9
[5]: https://arxiv.org/html/2510.20654v2#bib.bibx1
[6]: https://arxiv.org/html/2510.20654v2#bib.bibx7
[7]: https://arxiv.org/html/2510.20654v2#bib.bibx4
[8]: https://arxiv.org/html/2510.20654v2#bib.bibx6
[9]: https://arxiv.org/html/2510.20654v2#bib.bibx3
[10]: https://arxiv.org/html/2510.20654v2#S1.E1
[11]: https://arxiv.org/html/2510.20654v2#S1.E2
[12]: https://arxiv.org/html/2510.20654v2#S1.E3
[13]: https://arxiv.org/html/2510.20654v2#Thmthm1
[14]: https://arxiv.org/html/2510.20654v2#S2
[15]: https://arxiv.org/html/2510.20654v2#S1.E4
[16]: https://arxiv.org/html/2510.20654v2#S1.E5
[17]: https://arxiv.org/html/2510.20654v2#Thmthm10
[18]: https://arxiv.org/html/2510.20654v2#S1.E7
[19]: https://arxiv.org/html/2510.20654v2#Thmthm3
[20]: https://arxiv.org/html/2510.20654v2#Thmthm2
[21]: https://arxiv.org/html/2510.20654v2#Thmthm8
[22]: https://arxiv.org/html/2510.20654v2#Thmthm4
[23]: https://arxiv.org/html/2510.20654v2#S1.SS1
[24]: https://arxiv.org/html/2510.20654v2#S3
[25]: https://arxiv.org/html/2510.20654v2#S2.E1
[26]: https://arxiv.org/html/2510.20654v2#S1.SS2
[27]: https://arxiv.org/html/2510.20654v2#S3.Ex1
[28]: https://arxiv.org/html/2510.20654v2#S1.E6
[29]: https://arxiv.org/html/2510.20654v2#S3.E6
[30]: https://arxiv.org/html/2510.20654v2#S3.E4
[31]: https://arxiv.org/html/2510.20654v2#S3.E5
[32]: https://arxiv.org/html/2510.20654v2#S3.E7
[33]: https://arxiv.org/html/2510.20654v2#S3.E8
[34]: https://arxiv.org/html/2510.20654v2#S3.E9
[35]: https://arxiv.org/html/2510.20654v2#S3.E2
[36]: https://arxiv.org/html/2510.20654v2#S2.E2
[37]: https://arxiv.org/html/2510.20654v2#S3.E3
[38]: https://arxiv.org/html/2510.20654v2#Thmthm5
[39]: https://arxiv.org/html/2510.20654v2#bib.bibx10
[40]: https://arxiv.org/html/2510.20654v2#S3.E11
[41]: https://arxiv.org/html/2510.20654v2#S3.E10
[42]: https://arxiv.org/html/2510.20654v2#S3.Ex74
[43]: https://arxiv.org/html/2510.20654v2#S3.E14
[44]: https://arxiv.org/html/2510.20654v2#S3.E15
[45]: https://arxiv.org/html/2510.20654v2#S3.E16
[46]: https://arxiv.org/html/2510.20654v2#S3.E17
[47]: https://arxiv.org/html/2510.20654v2#S3.E20
[48]: https://arxiv.org/html/2510.20654v2#S3.E18
[49]: https://arxiv.org/html/2510.20654v2#S3.E19
[50]: https://arxiv.org/html/2510.20654v2#S3.E21
[51]: https://arxiv.org/html/2510.20654v2#Thmthm9
