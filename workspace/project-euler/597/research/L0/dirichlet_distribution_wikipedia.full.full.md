<!-- source: https://en.wikipedia.org/wiki/Dirichlet_distribution | converted from HTML -->

Dirichlet distribution - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Probability distribution

K \\geq 2</math> number of categories ([[integer]])<br /><math>\\boldsymbol\\alpha=(\\alpha_1,\\ldots,\\alpha_K)</math> [[concentration parameter]]s, where <math>\\alpha_i > 0</math>"},"support":{"wt":"<math>x_1, \\ldots, x_K</math> where <math>x_i \\in [0,1]</math> and <math>\\sum_{i=1}^K x_i = 1</math> <br /> (i.e. a <math>K-1</math> [[simplex]])"},"pdf":{"wt":"<math>\\frac{1}{\\mathrm{B}(\\boldsymbol\\alpha)} \\prod_{i=1}^K x_i^{\\alpha_i - 1} </math><br />where <math>\\mathrm{B}(\\boldsymbol\\alpha) = \\frac{\\prod_{i=1}^K \\Gamma(\\alpha_i)}{\\Gamma\\bigl(\\alpha_0\\bigr)}</math><br />where <math>\\alpha_0 = \\sum_{i=1}^K\\alpha_i</math>"},"cdf":{"wt":""},"mean":{"wt":"<math>\\operatorname{E}[X_i] = \\frac{\\alpha_i}{\\alpha_0}</math><br /><math> \\operatorname{E}[\\ln X_i] = \\psi(\\alpha_i)-\\psi(\\alpha_0)</math><br />(where <math>\\psi</math> is the [[digamma function]])"},"median":{"wt":""},"mode":{"wt":"<math>x_i = \\frac{\\alpha_i - 1}{\\alpha_0 - K}, \\quad \\alpha_i > 1. </math>"},"variance":{"wt":"<math>\\operatorname{Var}[X_i] = \\frac{\\tilde{\\alpha}_i(1-\\tilde{\\alpha}_i)}{\\alpha_0+1},</math> <math>\\operatorname{Cov}[X_i,X_j] = \\frac{\\delta_{ij}\\,\\tilde{\\alpha}_i-\\tilde{\\alpha}_i \\tilde{\\alpha}_j}{\\alpha_0+1}</math> <br/>where <math>\\tilde{\\alpha}_i = \\frac{\\alpha_i}{\\alpha_0}</math>, and <math>\\delta_{ij}</math> is the [[Kronecker delta]]"},"skewness":{"wt":""},"kurtosis":{"wt":""},"entropy":{"wt":"<math> H(X) = \\log \\mathrm{B}(\\boldsymbol\\alpha)</math><math> + (\\alpha_0-K)\\psi(\\alpha_0) -</math><math> \\sum_{j=1}^K (\\alpha_j-1)\\psi(\\alpha_j) </math><br/>with <math>\\alpha_0</math> defined as for variance, above; and <math>\\psi</math> is the [[digamma function]]"},"moments":{"wt":"<math> \\alpha_i = E[X_i]\\left(\\frac{E[X_j](1 - E[X_j])}{V[X_j]} - 1 \\right)</math> where {{mvar|j}} is any index, possibly {{mvar|i}} itself"}},"i":0}}]}'>

Dirichlet distribution |

Probability density function

[1] |

[Parameters][2] | K ≥ 2 {\displaystyle K\geq 2}[image: {\displaystyle K\geq 2}] number of categories ( [integer][3])
α = ( α 1, …, α K) {\displaystyle {\boldsymbol {\alpha }}=(\alpha _{1},\ldots ,\alpha _{K})}[image: {\displaystyle {\boldsymbol {\alpha }}=(\alpha _{1},\ldots ,\alpha _{K})}] [concentration parameters][4], where 0"}}'> 0}"> α i > 0 {\displaystyle \alpha _{i}>0} 0}"/> |

[Support][5] | x 1, …, x K {\displaystyle x_{1},\ldots ,x_{K}}[image: {\displaystyle x_{1},\ldots ,x_{K}}] where x i ∈ [0, 1] {\displaystyle x_{i}\in [0,1]}[image: {\displaystyle x_{i}\in [0,1]}] and ∑ i = 1 K x i = 1 {\displaystyle \sum _{i=1}^{K}x_{i}=1}[image: {\displaystyle \sum _{i=1}^{K}x_{i}=1}]
(i.e. a K − 1 {\displaystyle K-1}[image: {\displaystyle K-1}] [simplex][6]) |

[PDF][7] | 1 B ( α) ∏ i = 1 K x i α i − 1 {\displaystyle {\frac {1}{\mathrm {B} ({\boldsymbol {\alpha }})}}\prod _{i=1}^{K}x_{i}^{\alpha _{i}-1}}[image: {\displaystyle {\frac {1}{\mathrm {B} ({\boldsymbol {\alpha }})}}\prod _{i=1}^{K}x_{i}^{\alpha _{i}-1}}]
where B ( α) = ∏ i = 1 K Γ ( α i) Γ ( α 0) {\displaystyle \mathrm {B} ({\boldsymbol {\alpha }})={\frac {\prod _{i=1}^{K}\Gamma (\alpha _{i})}{\Gamma {\bigl (}\alpha _{0}{\bigr )}}}}[image: {\displaystyle \mathrm {B} ({\boldsymbol {\alpha }})={\frac {\prod _{i=1}^{K}\Gamma (\alpha _{i})}{\Gamma {\bigl (}\alpha _{0}{\bigr )}}}}]
where α 0 = ∑ i = 1 K α i {\displaystyle \alpha _{0}=\sum _{i=1}^{K}\alpha _{i}}[image: {\displaystyle \alpha _{0}=\sum _{i=1}^{K}\alpha _{i}}] |

[Mean][8] | E ⁡ [X i] = α i α 0 {\displaystyle \operatorname {E} [X_{i}]={\frac {\alpha _{i}}{\alpha _{0}}}}[image: {\displaystyle \operatorname {E} [X_{i}]={\frac {\alpha _{i}}{\alpha _{0}}}}]
E ⁡ [ln ⁡ X i] = ψ ( α i) − ψ ( α 0) {\displaystyle \operatorname {E} [\ln X_{i}]=\psi (\alpha _{i})-\psi (\alpha _{0})}[image: {\displaystyle \operatorname {E} [\ln X_{i}]=\psi (\alpha _{i})-\psi (\alpha _{0})}]
(where ψ {\displaystyle \psi }[image: {\displaystyle \psi }] is the [digamma function][9]) |

[Mode][10] | 1. "}}'> 1.}"> x i = α i − 1 α 0 − K, α i > 1. {\displaystyle x_{i}={\frac {\alpha _{i}-1}{\alpha _{0}-K}},\quad \alpha _{i}>1.} 1.}"/> |

[Variance][11] | Var ⁡ [X i] = α ~ i ( 1 − α ~ i) α 0 + 1, {\displaystyle \operatorname {Var} [X_{i}]={\frac {{\tilde {\alpha }}_{i}(1-{\tilde {\alpha }}_{i})}{\alpha _{0}+1}},}[image: {\displaystyle \operatorname {Var} [X_{i}]={\frac {{\tilde {\alpha }}_{i}(1-{\tilde {\alpha }}_{i})}{\alpha _{0}+1}},}] Cov ⁡ [X i, X j] = δ i j α ~ i − α ~ i α ~ j α 0 + 1 {\displaystyle \operatorname {Cov} [X_{i},X_{j}]={\frac {\delta _{ij}\,{\tilde {\alpha }}_{i}-{\tilde {\alpha }}_{i}{\tilde {\alpha }}_{j}}{\alpha _{0}+1}}}[image: {\displaystyle \operatorname {Cov} [X_{i},X_{j}]={\frac {\delta _{ij}\,{\tilde {\alpha }}_{i}-{\tilde {\alpha }}_{i}{\tilde {\alpha }}_{j}}{\alpha _{0}+1}}}]
where α ~ i = α i α 0 {\displaystyle {\tilde {\alpha }}_{i}={\frac {\alpha _{i}}{\alpha _{0}}}}[image: {\displaystyle {\tilde {\alpha }}_{i}={\frac {\alpha _{i}}{\alpha _{0}}}}], and δ i j {\displaystyle \delta _{ij}}[image: {\displaystyle \delta _{ij}}] is the [Kronecker delta][12] |

[Entropy][13] | H ( X) = log ⁡ B ( α) {\displaystyle H(X)=\log \mathrm {B} ({\boldsymbol {\alpha }})}[image: {\displaystyle H(X)=\log \mathrm {B} ({\boldsymbol {\alpha }})}] + ( α 0 − K) ψ ( α 0) − {\displaystyle +(\alpha _{0}-K)\psi (\alpha _{0})-}[image: {\displaystyle +(\alpha _{0}-K)\psi (\alpha _{0})-}] ∑ j = 1 K ( α j − 1) ψ ( α j) {\displaystyle \sum _{j=1}^{K}(\alpha _{j}-1)\psi (\alpha _{j})}[image: {\displaystyle \sum _{j=1}^{K}(\alpha _{j}-1)\psi (\alpha _{j})}]
with α 0 {\displaystyle \alpha _{0}}[image: {\displaystyle \alpha _{0}}] defined as for variance, above; and ψ {\displaystyle \psi }[image: {\displaystyle \psi }] is the [digamma function][9] |

[Method of moments][14] | α i = E [X i] ( E [X j] ( 1 − E [X j]) V [X j] − 1) {\displaystyle \alpha _{i}=E[X_{i}]\left({\frac {E[X_{j}](1-E[X_{j}])}{V[X_{j}]}}-1\right)}[image: {\displaystyle \alpha _{i}=E[X_{i}]\left({\frac {E[X_{j}](1-E[X_{j}])}{V[X_{j}]}}-1\right)}] where j is any index, possibly i itself |

In [probability][15] and [statistics][16], the **Dirichlet distribution**(after [Peter Gustav Lejeune Dirichlet][17]), often denoted Dir ⁡ ( α) {\displaystyle \operatorname {Dir} ({\boldsymbol {\alpha }})}[image: {\displaystyle \operatorname {Dir} ({\boldsymbol {\alpha }})}], is a family of [continuous][18] [multivariate][19] [probability distributions][20] parameterized by a vector **α**of positive [reals][21]. It is a multivariate generalization of the [beta distribution][22], [1] hence its alternative name of **multivariate beta distribution**(**MBD**). [2] Dirichlet distributions are commonly used as [prior distributions][23] in [Bayesian statistics][24], and in fact, the Dirichlet distribution is the [conjugate prior][25] of the [categorical distribution][26] and [multinomial distribution][27].

The infinite-dimensional generalization of the Dirichlet distribution is the *[Dirichlet process][28]*.

## Definitions

[[edit][29]]

### Probability density function

[[edit][30]]

[31] Illustrating how the log of the density function changes when K = 3 {\displaystyle K=3}[image: {\displaystyle K=3}] as we change the vector α {\displaystyle {\boldsymbol {\alpha }}}[image: {\displaystyle {\boldsymbol {\alpha }}}] from α = ( 0.3, 0.3, 0.3) {\displaystyle {\boldsymbol {\alpha }}=(0.3,0.3,0.3)}[image: {\displaystyle {\boldsymbol {\alpha }}=(0.3,0.3,0.3)}] to ( 2.0, 2.0, 2.0) {\displaystyle (2.0,2.0,2.0)}[image: {\displaystyle (2.0,2.0,2.0)}], keeping all the individual α i {\displaystyle \alpha _{i}}[image: {\displaystyle \alpha _{i}}] 's equal to each other.

The Dirichlet distribution of order K ≥ 2 {\displaystyle K\geq 2}[image: {\displaystyle K\geq 2}] with parameters 0"}}'> 0}"> α 1, …, α K > 0 {\displaystyle \alpha _{1},\ldots ,\alpha _{K}>0} 0}"/> has a [probability density function][7] given by

f ( x 1, …, x K; α 1, …, α K) = 1 B ( α) ∏ i = 1 K x i α i − 1 {\displaystyle f\left(x_{1},\ldots ,x_{K};\alpha _{1},\ldots ,\alpha _{K}\right)={\frac {1}{\mathrm {B} ({\boldsymbol {\alpha }})}}\prod _{i=1}^{K}x_{i}^{\alpha _{i}-1}}[image: {\displaystyle f\left(x_{1},\ldots ,x_{K};\alpha _{1},\ldots ,\alpha _{K}\right)={\frac {1}{\mathrm {B} ({\boldsymbol {\alpha }})}}\prod _{i=1}^{K}x_{i}^{\alpha _{i}-1}}] where x i ∈ [0, 1] for all i ∈ { 1, …, K } and ∑ i = 1 K x i = 1. {\displaystyle x_{i}\in \left[0,1\right]{\mbox{ for all }}i\in \{1,\dots ,K\}{\mbox{ and }}\sum _{i=1}^{K}x_{i}=1\,.}[image: {\displaystyle x_{i}\in \left[0,1\right]{\mbox{ for all }}i\in \{1,\dots ,K\}{\mbox{ and }}\sum _{i=1}^{K}x_{i}=1\,.}] That is, the probability density function is defined on the standard K − 1 {\displaystyle K-1}[image: {\displaystyle K-1}] [simplex][6] embedded in ⁠ K {\displaystyle K}[image: {\displaystyle K}] ⁠ -dimensional [Euclidean space][32], R K {\displaystyle \mathbb {R} ^{K}}[image: {\displaystyle \mathbb {R} ^{K}}].

The [normalizing constant][33] is the multivariate [beta function][34], which can be expressed in terms of the [gamma function][35]:

B ( α) = ∏ i = 1 K Γ ( α i) Γ ( ∑ i = 1 K α i), α = ( α 1, …, α K). {\displaystyle \mathrm {B} ({\boldsymbol {\alpha }})={\frac {\prod \limits _{i=1}^{K}\Gamma (\alpha _{i})}{\Gamma \left(\sum \limits _{i=1}^{K}\alpha _{i}\right)}},\qquad {\boldsymbol {\alpha }}=(\alpha _{1},\ldots ,\alpha _{K}).}[image: {\displaystyle \mathrm {B} ({\boldsymbol {\alpha }})={\frac {\prod \limits _{i=1}^{K}\Gamma (\alpha _{i})}{\Gamma \left(\sum \limits _{i=1}^{K}\alpha _{i}\right)}},\qquad {\boldsymbol {\alpha }}=(\alpha _{1},\ldots ,\alpha _{K}).}]

### Support

[[edit][36]]

The [support][5] of the Dirichlet distribution is the set of K -dimensional vectors **x**whose entries are real numbers in the interval [0,1] such that ‖ x ‖ 1 = 1 {\displaystyle \|{\boldsymbol {x}}\|_{1}=1}[image: {\displaystyle \|{\boldsymbol {x}}\|_{1}=1}], i.e. the sum of the coordinates is equal to 1. These can be viewed as the probabilities of a K -way [categorical][26] event. Another way to express this is that the domain of the Dirichlet distribution is itself a set of [probability distributions][20], specifically the set of K -dimensional [discrete distributions][37]. The technical term for the set of points in the support of a K -dimensional Dirichlet distribution is the [open][38]**[standard ( K − 1) -simplex][39], [3] which is a generalization of a [triangle][40], embedded in the next-higher dimension. For example, with *K*= 3, the support is an [equilateral triangle][41] embedded in a downward-angle fashion in three-dimensional space, with vertices at (1,0,0), (0,1,0) and (0,0,1), i.e. touching each of the coordinate axes at a point 1 unit away from the origin.

### Symmetric cases

[[edit][42]]

A common special case is the **symmetric Dirichlet distribution**, where all of the elements making up the parameter vector **α**have the same value. The symmetric case might be useful, for example, when a Dirichlet prior over components is called for, but there is no prior knowledge favoring one component over another. Since all elements of the parameter vector have the same value, the symmetric Dirichlet distribution can be parametrized by a single scalar value α, called the [concentration parameter][4]. In terms of α, the density function has the form

f ( x 1, …, x K; α) = Γ ( α K) Γ ( α) K ∏ i = 1 K x i α − 1. {\displaystyle f(x_{1},\dots ,x_{K};\alpha )={\frac {\Gamma (\alpha K)}{\Gamma (\alpha )^{K}}}\prod _{i=1}^{K}x_{i}^{\alpha -1}.}[image: {\displaystyle f(x_{1},\dots ,x_{K};\alpha )={\frac {\Gamma (\alpha K)}{\Gamma (\alpha )^{K}}}\prod _{i=1}^{K}x_{i}^{\alpha -1}.}]

When *α*= 1, [43] the symmetric Dirichlet distribution is equivalent to a uniform distribution over the open **[standard ( K −1) -simplex][39], i.e. it is uniform over all points in its [support][5]. This particular distribution is known as the **flat Dirichlet distribution**. Values of the concentration parameter above 1 prefer [variates][44] that are dense, evenly distributed distributions, i.e. all the values within a single sample are similar to each other. Values of the concentration parameter below 1 prefer sparse distributions, i.e. most of the values within a single sample will be close to 0, and the vast majority of the mass will be concentrated in a few of the values.

When *α*= 1/2, the distribution is the same as would be obtained by choosing a point uniformly at random from the (*K*−1) -dimensional [unit hypersphere][45], which is the surface of a K -dimensional [unit hyperball][46], and squaring each coordinate. The *α*= 1/2 distribution is the [Jeffreys prior][47] for the Dirichlet distribution.

### With specified expectations

[[edit][48]]

Instead of specifying the vector of concentration parameters α {\displaystyle {\boldsymbol {\alpha }}}[image: {\displaystyle {\boldsymbol {\alpha }}}], one may wish to specify the expected probability distribution E i = α i α 0 where α 0 = ∑ j = 1 K α j {\displaystyle \operatorname {E} _{i}={\frac {\alpha _{i}}{\alpha _{0}}}\;\;{\mbox{ where }}\;\;\alpha _{0}=\sum _{j=1}^{K}\alpha _{j}}[image: {\displaystyle \operatorname {E} _{i}={\frac {\alpha _{i}}{\alpha _{0}}}\;\;{\mbox{ where }}\;\;\alpha _{0}=\sum _{j=1}^{K}\alpha _{j}}] such that the concentration parameters are written as the product α = W E {\displaystyle \,{\boldsymbol {\alpha }}=W\,{\boldsymbol {\operatorname {E} }}\,}[image: {\displaystyle \,{\boldsymbol {\alpha }}=W\,{\boldsymbol {\operatorname {E} }}\,}] of the ( [scalar][49]) concentration weight ⁠ W {\displaystyle W}[image: {\displaystyle W}] ⁠ and the expected probability distribution E {\displaystyle {\boldsymbol {\operatorname {E} }}}[image: {\displaystyle {\boldsymbol {\operatorname {E} }}}] whose components are non-negative and sum up to 1. The concentration weight in this case is larger by a factor of K than the concentration parameter for a symmetric Dirichlet distribution described above. This construction ties in with concept of a base measure when discussing [Dirichlet processes][28] and is often used in the topic modelling literature.

[50] 3D curve plot of the noninformative prior weight, with the convergence constant C W = 2 {\displaystyle C_{W}=2}[image: {\displaystyle C_{W}=2}]

When the dimension of the Dirichlet distribution is large, [Jeffreys prior][47] produces a correspondingly high prior concentration weight. For example when ⁠ K = 100 {\displaystyle K=100}[image: {\displaystyle K=100}] ⁠, the prior concentration weight becomes ⁠ W = K / 2 = 50 {\displaystyle W=K/2=50}[image: {\displaystyle W=K/2=50}] ⁠, which creates a relatively stiff prior probability distribution E ∗ {\displaystyle {\boldsymbol {\operatorname {E} }}^{\ast }}[image: {\displaystyle {\boldsymbol {\operatorname {E} }}^{\ast }}] where initially the posterior probability distribution E {\displaystyle {\boldsymbol {\operatorname {E} }}}[image: {\displaystyle {\boldsymbol {\operatorname {E} }}}] hardly changes in the presence of observed data, even in the case of e.g. 10 observations where all observations indicate the same category X i {\displaystyle X_{i}}[image: {\displaystyle X_{i}}], which naturally and intuitively should produce an expected probability E i {\displaystyle \operatorname {E} _{i}}[image: {\displaystyle \operatorname {E} _{i}}] close to 1. A way to avoid the misbehaviour of the stiff prior is to use the noninformative prior weight W {\displaystyle W}[image: {\displaystyle W}] from [subjective logic][51], where the concentration parameters α i {\displaystyle \alpha _{i}}[image: {\displaystyle \alpha _{i}}] are expressed as a function of the observations r i {\displaystyle r_{i}}[image: {\displaystyle r_{i}}] according to α i = r i + W E i ∗ {\displaystyle \alpha _{i}=r_{i}+W\operatorname {E} _{i}^{\ast }}[image: {\displaystyle \alpha _{i}=r_{i}+W\operatorname {E} _{i}^{\ast }}]. [4] The noninformative prior concentration weight ⁠ W {\displaystyle W}[image: {\displaystyle W}] ⁠ is a function of the number of observations r 0 = ∑ r i {\displaystyle r_{0}=\sum r_{i}}[image: {\displaystyle r_{0}=\sum r_{i}}], expressed as W = K ( 1 + C W r 0) 1 + K r 0 {\displaystyle W={\frac {K(1+C_{W}r_{0})}{1+Kr_{0}}}}[image: {\displaystyle W={\frac {K(1+C_{W}r_{0})}{1+Kr_{0}}}}] where ⁠ C W {\displaystyle C_{W}}[image: {\displaystyle C_{W}}] ⁠ is a convergence constant, normally chosen to be equal to 2. The choice of C W = 2 {\displaystyle C_{W}=2}[image: {\displaystyle C_{W}=2}] ensures that the Dirichlet distribution of any dimension has the same sensitivity to new observations as the Beta distribution with prior concentration parameters α + β = 2 {\displaystyle \alpha +\beta =2}[image: {\displaystyle \alpha +\beta =2}] (or the uniform α = β = 1 {\displaystyle \alpha =\beta =1}[image: {\displaystyle \alpha =\beta =1}]). In the case of a uniform prior probability distribution E ∗ {\displaystyle {\boldsymbol {\operatorname {E} }}^{\ast }}[image: {\displaystyle {\boldsymbol {\operatorname {E} }}^{\ast }}], the noninformative prior weight W {\displaystyle W}[image: {\displaystyle W}] also ensures a uniform prior Dirichlet distribution for any dimension K {\displaystyle K}[image: {\displaystyle K}]. A 3D plot of W {\displaystyle W}[image: {\displaystyle W}] is illustrated in the figure.

## Properties

[[edit][52]]

### Moments

[[edit][53]]

Let X = ( X 1, …, X K) ∼ Dir ⁡ ( α) {\displaystyle X=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} ({\boldsymbol {\alpha }})}[image: {\displaystyle X=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} ({\boldsymbol {\alpha }})}].

Let

α 0 = ∑ i = 1 K α i. {\displaystyle \alpha _{0}=\sum _{i=1}^{K}\alpha _{i}.}[image: {\displaystyle \alpha _{0}=\sum _{i=1}^{K}\alpha _{i}.}]

Then [5] [6]

E ⁡ [X i] = α i α 0, {\displaystyle \operatorname {E} [X_{i}]={\frac {\alpha _{i}}{\alpha _{0}}},}[image: {\displaystyle \operatorname {E} [X_{i}]={\frac {\alpha _{i}}{\alpha _{0}}},}] Var ⁡ [X i] = α i ( α 0 − α i) α 0 2 ( α 0 + 1). {\displaystyle \operatorname {Var} [X_{i}]={\frac {\alpha _{i}(\alpha _{0}-\alpha _{i})}{\alpha _{0}^{2}(\alpha _{0}+1)}}.}[image: {\displaystyle \operatorname {Var} [X_{i}]={\frac {\alpha _{i}(\alpha _{0}-\alpha _{i})}{\alpha _{0}^{2}(\alpha _{0}+1)}}.}]

Furthermore, if i ≠ j {\displaystyle i\neq j}[image: {\displaystyle i\neq j}]

Cov ⁡ [X i, X j] = − α i α j α 0 2 ( α 0 + 1). {\displaystyle \operatorname {Cov} [X_{i},X_{j}]={\frac {-\alpha _{i}\alpha _{j}}{\alpha _{0}^{2}(\alpha _{0}+1)}}.}[image: {\displaystyle \operatorname {Cov} [X_{i},X_{j}]={\frac {-\alpha _{i}\alpha _{j}}{\alpha _{0}^{2}(\alpha _{0}+1)}}.}]

The covariance matrix is [singular][54].

More generally, moments of Dirichlet-distributed random variables can be expressed in the following way. For t = ( t 1, …, t K) ∈ R K {\displaystyle {\boldsymbol {t}}=(t_{1},\dotsc ,t_{K})\in \mathbb {R} ^{K}}[image: {\displaystyle {\boldsymbol {t}}=(t_{1},\dotsc ,t_{K})\in \mathbb {R} ^{K}}], denote by t ∘ i = ( t 1 i, …, t K i) {\displaystyle {\boldsymbol {t}}^{\circ i}=(t_{1}^{i},\dotsc ,t_{K}^{i})}[image: {\displaystyle {\boldsymbol {t}}^{\circ i}=(t_{1}^{i},\dotsc ,t_{K}^{i})}] its i -th [Hadamard power][55]. Then, [7]

E ⁡ [( t ⋅ X) n] = n! Γ ( α 0) Γ ( α 0 + n) ∑ t 1 k 1 ⋯ t K k K k 1! ⋯ k K! ∏ i = 1 K Γ ( α i + k i) Γ ( α i) = n! Γ ( α 0) Γ ( α 0 + n) Z n ( t ∘ 1 ⋅ α, ⋯, t ∘ n ⋅ α), {\displaystyle \operatorname {E} \left[({\boldsymbol {t}}\cdot {\boldsymbol {X}})^{n}\right]={\frac {n!\,\Gamma (\alpha _{0})}{\Gamma (\alpha _{0}+n)}}\sum {\frac {{t_{1}}^{k_{1}}\cdots {t_{K}}^{k_{K}}}{k_{1}!\cdots k_{K}!}}\prod _{i=1}^{K}{\frac {\Gamma (\alpha _{i}+k_{i})}{\Gamma (\alpha _{i})}}={\frac {n!\,\Gamma (\alpha _{0})}{\Gamma (\alpha _{0}+n)}}Z_{n}({\boldsymbol {t}}^{\circ 1}\cdot {\boldsymbol {\alpha }},\cdots ,{\boldsymbol {t}}^{\circ n}\cdot {\boldsymbol {\alpha }}),}[image: {\displaystyle \operatorname {E} \left[({\boldsymbol {t}}\cdot {\boldsymbol {X}})^{n}\right]={\frac {n!\,\Gamma (\alpha _{0})}{\Gamma (\alpha _{0}+n)}}\sum {\frac {{t_{1}}^{k_{1}}\cdots {t_{K}}^{k_{K}}}{k_{1}!\cdots k_{K}!}}\prod _{i=1}^{K}{\frac {\Gamma (\alpha _{i}+k_{i})}{\Gamma (\alpha _{i})}}={\frac {n!\,\Gamma (\alpha _{0})}{\Gamma (\alpha _{0}+n)}}Z_{n}({\boldsymbol {t}}^{\circ 1}\cdot {\boldsymbol {\alpha }},\cdots ,{\boldsymbol {t}}^{\circ n}\cdot {\boldsymbol {\alpha }}),}]

where the sum is over non-negative integers k 1, …, k K {\displaystyle k_{1},\ldots ,k_{K}}[image: {\displaystyle k_{1},\ldots ,k_{K}}] with n = k 1 + ⋯ + k K {\displaystyle n=k_{1}+\cdots +k_{K}}[image: {\displaystyle n=k_{1}+\cdots +k_{K}}], and Z n {\displaystyle Z_{n}}[image: {\displaystyle Z_{n}}] is the [cycle index polynomial][56] of the [Symmetric group][57] of degree n.

We have the special case E ⁡ [t ⋅ X] = t ⋅ α α 0. {\displaystyle \operatorname {E} \left[{\boldsymbol {t}}\cdot {\boldsymbol {X}}\right]={\frac {{\boldsymbol {t}}\cdot {\boldsymbol {\alpha }}}{\alpha _{0}}}.}[image: {\displaystyle \operatorname {E} \left[{\boldsymbol {t}}\cdot {\boldsymbol {X}}\right]={\frac {{\boldsymbol {t}}\cdot {\boldsymbol {\alpha }}}{\alpha _{0}}}.}]

The multivariate analogue E ⁡ [( t 1 ⋅ X) n 1 ⋯ ( t q ⋅ X) n q] {\textstyle \operatorname {E} \left[({\boldsymbol {t}}_{1}\cdot {\boldsymbol {X}})^{n_{1}}\cdots ({\boldsymbol {t}}_{q}\cdot {\boldsymbol {X}})^{n_{q}}\right]}[image: {\textstyle \operatorname {E} \left[({\boldsymbol {t}}_{1}\cdot {\boldsymbol {X}})^{n_{1}}\cdots ({\boldsymbol {t}}_{q}\cdot {\boldsymbol {X}})^{n_{q}}\right]}] for vectors t 1, …, t q ∈ R K {\displaystyle {\boldsymbol {t}}_{1},\dotsc ,{\boldsymbol {t}}_{q}\in \mathbb {R} ^{K}}[image: {\displaystyle {\boldsymbol {t}}_{1},\dotsc ,{\boldsymbol {t}}_{q}\in \mathbb {R} ^{K}}] can be expressed [8] in terms of a color pattern of the exponents n 1, …, n q {\displaystyle n_{1},\dotsc ,n_{q}}[image: {\displaystyle n_{1},\dotsc ,n_{q}}] in the sense of the [Pólya enumeration theorem][58].

Particular cases include the simple computation [9]

E ⁡ [∏ i = 1 K X i β i] = B ( α + β) B ( α) = Γ ( ∑ i = 1 K α i) Γ [∑ i = 1 K ( α i + β i)] × ∏ i = 1 K Γ ( α i + β i) Γ ( α i). {\displaystyle \operatorname {E} \left[\prod _{i=1}^{K}X_{i}^{\beta _{i}}\right]={\frac {B\left({\boldsymbol {\alpha }}+{\boldsymbol {\beta }}\right)}{B\left({\boldsymbol {\alpha }}\right)}}={\frac {\Gamma \left(\sum \limits _{i=1}^{K}\alpha _{i}\right)}{\Gamma \left[\sum \limits _{i=1}^{K}(\alpha _{i}+\beta _{i})\right]}}\times \prod _{i=1}^{K}{\frac {\Gamma (\alpha _{i}+\beta _{i})}{\Gamma (\alpha _{i})}}.}[image: {\displaystyle \operatorname {E} \left[\prod _{i=1}^{K}X_{i}^{\beta _{i}}\right]={\frac {B\left({\boldsymbol {\alpha }}+{\boldsymbol {\beta }}\right)}{B\left({\boldsymbol {\alpha }}\right)}}={\frac {\Gamma \left(\sum \limits _{i=1}^{K}\alpha _{i}\right)}{\Gamma \left[\sum \limits _{i=1}^{K}(\alpha _{i}+\beta _{i})\right]}}\times \prod _{i=1}^{K}{\frac {\Gamma (\alpha _{i}+\beta _{i})}{\Gamma (\alpha _{i})}}.}]

### Mode

[[edit][59]]

The [mode][10] of the distribution is [10] the vector (*x*1, ..., *x K*) with

1. "}}'> 1.}"> x i = α i − 1 α 0 − K, α i > 1. {\displaystyle x_{i}={\frac {\alpha _{i}-1}{\alpha _{0}-K}},\qquad \alpha _{i}>1.} 1.}"/>

### Marginal distributions

[[edit][60]]

The [marginal distributions][61] are [beta distributions][22]: [11]

X i ∼ Beta ⁡ ( α i, α 0 − α i). {\displaystyle X_{i}\sim \operatorname {Beta} (\alpha _{i},\alpha _{0}-\alpha _{i}).}[image: {\displaystyle X_{i}\sim \operatorname {Beta} (\alpha _{i},\alpha _{0}-\alpha _{i}).}]

Also see § Related distributions below.

### Conjugate to categorical or multinomial

[[edit][62]]

The Dirichlet distribution is the [conjugate prior][25] distribution of the [categorical distribution][26] (a generic [discrete probability distribution][63] with a given number of possible outcomes) and [multinomial distribution][27] (the distribution over observed counts of each possible category in a set of categorically distributed observations). This means that if a data point has either a categorical or multinomial distribution, and the [prior distribution][23] of the distribution's parameter (the vector of probabilities that generates the data point) is distributed as a Dirichlet, then the [posterior distribution][64] of the parameter is also a Dirichlet. Intuitively, in such a case, starting from what we know about the parameter prior to observing the data point, we then can update our knowledge based on the data point and end up with a new distribution of the same form as the old one. This means that we can successively update our knowledge of a parameter by incorporating new observations one at a time, without running into mathematical difficulties.

Formally, this can be expressed as follows. Given a model

α = ( α 1, …, α K) = concentration hyperparameter p ∣ α = ( p 1, …, p K) ∼ Dir ⁡ ( K, α) X ∣ p = ( x 1, …, x K) ∼ Cat ⁡ ( K, p) {\displaystyle {\begin{array}{rcccl}{\boldsymbol {\alpha }}&=&\left(\alpha _{1},\ldots ,\alpha _{K}\right)&=&{\text{concentration hyperparameter}}\\\mathbf {p} \mid {\boldsymbol {\alpha }}&=&\left(p_{1},\ldots ,p_{K}\right)&\sim &\operatorname {Dir} (K,{\boldsymbol {\alpha }})\\\mathbb {X} \mid \mathbf {p} &=&\left(\mathbf {x} _{1},\ldots ,\mathbf {x} _{K}\right)&\sim &\operatorname {Cat} (K,\mathbf {p} )\end{array}}}[image: {\displaystyle {\begin{array}{rcccl}{\boldsymbol {\alpha }}&=&\left(\alpha _{1},\ldots ,\alpha _{K}\right)&=&{\text{concentration hyperparameter}}\\\mathbf {p} \mid {\boldsymbol {\alpha }}&=&\left(p_{1},\ldots ,p_{K}\right)&\sim &\operatorname {Dir} (K,{\boldsymbol {\alpha }})\\\mathbb {X} \mid \mathbf {p} &=&\left(\mathbf {x} _{1},\ldots ,\mathbf {x} _{K}\right)&\sim &\operatorname {Cat} (K,\mathbf {p} )\end{array}}}]

then the following holds:

c = ( c 1, …, c K) = number of occurrences of category i p ∣ X, α ∼ Dir ⁡ ( K, c + α) = Dir ⁡ ( K, c 1 + α 1, …, c K + α K) {\displaystyle {\begin{array}{rcccl}\mathbf {c} &=&\left(c_{1},\ldots ,c_{K}\right)&=&{\text{number of occurrences of category }}i\\\mathbf {p} \mid \mathbb {X} ,{\boldsymbol {\alpha }}&\sim &\operatorname {Dir} (K,\mathbf {c} +{\boldsymbol {\alpha }})&=&\operatorname {Dir} \left(K,c_{1}+\alpha _{1},\ldots ,c_{K}+\alpha _{K}\right)\end{array}}}[image: {\displaystyle {\begin{array}{rcccl}\mathbf {c} &=&\left(c_{1},\ldots ,c_{K}\right)&=&{\text{number of occurrences of category }}i\\\mathbf {p} \mid \mathbb {X} ,{\boldsymbol {\alpha }}&\sim &\operatorname {Dir} (K,\mathbf {c} +{\boldsymbol {\alpha }})&=&\operatorname {Dir} \left(K,c_{1}+\alpha _{1},\ldots ,c_{K}+\alpha _{K}\right)\end{array}}}]

This relationship is used in [Bayesian statistics][24] to estimate the underlying parameter **p**of a [categorical distribution][26] given a collection of N samples. Intuitively, we can view the [hyperprior][65] vector **α**as [pseudocounts][66], i.e. as representing the number of observations in each category that we have already seen. Then we simply add in the counts for all the new observations (the vector **c**) in order to derive the posterior distribution.

In Bayesian [mixture models][67] and other [hierarchical Bayesian models][68] with mixture components, Dirichlet distributions are commonly used as the prior distributions for the [categorical variables][26] appearing in the models. See the section on applications below for more information.

### Relation to Dirichlet-multinomial distribution

[[edit][69]]

In a model where a Dirichlet prior distribution is placed over a set of [categorical-valued][26] observations, the [marginal][61] [joint distribution][70] of the observations (i.e. the joint distribution of the observations, with the prior parameter [marginalized out][71]) is a [Dirichlet-multinomial distribution][72]. This distribution plays an important role in [hierarchical Bayesian models][68], because when doing [inference][73] over such models using methods such as [Gibbs sampling][74] or [variational Bayes][75], Dirichlet prior distributions are often marginalized out. See the [article on this distribution][72] for more details.

### Entropy

[[edit][76]]

If X is a Dir ⁡ ( α) {\displaystyle \operatorname {Dir} ({\boldsymbol {\alpha }})}[image: {\displaystyle \operatorname {Dir} ({\boldsymbol {\alpha }})}] random variable, the [differential entropy][77] of X (in [nat units][78]) is [12]

h ( X) = E ⁡ [− ln ⁡ f ( X)] = ln ⁡ B ⁡ ( α) + ( α 0 − K) ψ ( α 0) − ∑ j = 1 K ( α j − 1) ψ ( α j) {\displaystyle h({\boldsymbol {X}})=\operatorname {E} [-\ln f({\boldsymbol {X}})]=\ln \operatorname {B} ({\boldsymbol {\alpha }})+(\alpha _{0}-K)\psi (\alpha _{0})-\sum _{j=1}^{K}(\alpha _{j}-1)\psi (\alpha _{j})}[image: {\displaystyle h({\boldsymbol {X}})=\operatorname {E} [-\ln f({\boldsymbol {X}})]=\ln \operatorname {B} ({\boldsymbol {\alpha }})+(\alpha _{0}-K)\psi (\alpha _{0})-\sum _{j=1}^{K}(\alpha _{j}-1)\psi (\alpha _{j})}]

where ψ {\displaystyle \psi }[image: {\displaystyle \psi }] is the [digamma function][9].

The following formula for E ⁡ [ln ⁡ ( X i)] {\displaystyle \operatorname {E} [\ln(X_{i})]}[image: {\displaystyle \operatorname {E} [\ln(X_{i})]}] can be used to derive the differential [entropy][13] above. Since the functions ln ⁡ ( X i) {\displaystyle \ln(X_{i})}[image: {\displaystyle \ln(X_{i})}] are the sufficient statistics of the Dirichlet distribution, the [exponential family differential identities][79] can be used to get an analytic expression for the expectation of ln ⁡ ( X i) {\displaystyle \ln(X_{i})}[image: {\displaystyle \ln(X_{i})}] (see equation (2.62) in [13]) and its associated covariance matrix:

E ⁡ [ln ⁡ ( X i)] = ψ ( α i) − ψ ( α 0) {\displaystyle \operatorname {E} [\ln(X_{i})]=\psi (\alpha _{i})-\psi (\alpha _{0})}[image: {\displaystyle \operatorname {E} [\ln(X_{i})]=\psi (\alpha _{i})-\psi (\alpha _{0})}]

and

Cov ⁡ [ln ⁡ ( X i), ln ⁡ ( X j)] = ψ ′ ( α i) δ i j − ψ ′ ( α 0) {\displaystyle \operatorname {Cov} [\ln(X_{i}),\ln(X_{j})]=\psi '(\alpha _{i})\delta _{ij}-\psi '(\alpha _{0})}[image: {\displaystyle \operatorname {Cov} [\ln(X_{i}),\ln(X_{j})]=\psi '(\alpha _{i})\delta _{ij}-\psi '(\alpha _{0})}]

where ψ {\displaystyle \psi }[image: {\displaystyle \psi }] is the [digamma function][9], ψ ′ {\displaystyle \psi '}[image: {\displaystyle \psi '}] is the [trigamma function][80], and δ i j {\displaystyle \delta _{ij}}[image: {\displaystyle \delta _{ij}}] is the [Kronecker delta][12].

The spectrum of [Rényi information][81] for values other than λ = 1 {\displaystyle \lambda =1}[image: {\displaystyle \lambda =1}] is given by [14]

F R ( λ) = ( 1 − λ) − 1 ( − λ log ⁡ B ( α) + ∑ i = 1 K log ⁡ Γ ( λ ( α i − 1) + 1) − log ⁡ Γ ( λ ( α 0 − K) + K)) {\displaystyle F_{R}(\lambda )=(1-\lambda )^{-1}\left(-\lambda \log \mathrm {B} ({\boldsymbol {\alpha }})+\sum _{i=1}^{K}\log \Gamma (\lambda (\alpha _{i}-1)+1)-\log \Gamma (\lambda (\alpha _{0}-K)+K)\right)}[image: {\displaystyle F_{R}(\lambda )=(1-\lambda )^{-1}\left(-\lambda \log \mathrm {B} ({\boldsymbol {\alpha }})+\sum _{i=1}^{K}\log \Gamma (\lambda (\alpha _{i}-1)+1)-\log \Gamma (\lambda (\alpha _{0}-K)+K)\right)}]

and the information entropy is the limit as λ {\displaystyle \lambda }[image: {\displaystyle \lambda }] goes to 1.

Another related interesting measure is the entropy of a discrete categorical (one-of-K binary) vector **Z**with probability-mass distribution **X**, i.e., P ( Z i = 1, Z j ≠ i = 0 | X) = X i {\displaystyle P(Z_{i}=1,Z_{j\neq i}=0|{\boldsymbol {X}})=X_{i}}[image: {\displaystyle P(Z_{i}=1,Z_{j\neq i}=0|{\boldsymbol {X}})=X_{i}}]. The conditional [information entropy][13] of **Z**, given **X**is

S ( X) = H ( Z | X) = E Z ⁡ [− log ⁡ P ( Z | X)] = ∑ i = 1 K − X i log ⁡ X i {\displaystyle S({\boldsymbol {X}})=H({\boldsymbol {Z}}|{\boldsymbol {X}})=\operatorname {E} _{\boldsymbol {Z}}[-\log P({\boldsymbol {Z}}|{\boldsymbol {X}})]=\sum _{i=1}^{K}-X_{i}\log X_{i}}[image: {\displaystyle S({\boldsymbol {X}})=H({\boldsymbol {Z}}|{\boldsymbol {X}})=\operatorname {E} _{\boldsymbol {Z}}[-\log P({\boldsymbol {Z}}|{\boldsymbol {X}})]=\sum _{i=1}^{K}-X_{i}\log X_{i}}]

This function of **X**is a scalar random variable. If **X**has a symmetric Dirichlet distribution with all α i = α {\displaystyle \alpha _{i}=\alpha }[image: {\displaystyle \alpha _{i}=\alpha }], the expected value of the entropy (in [nat units][78]) is [15]

E ⁡ [S ( X)] = ∑ i = 1 K E ⁡ [− X i ln ⁡ X i] = ψ ( K α + 1) − ψ ( α + 1) {\displaystyle \operatorname {E} [S({\boldsymbol {X}})]=\sum _{i=1}^{K}\operatorname {E} [-X_{i}\ln X_{i}]=\psi (K\alpha +1)-\psi (\alpha +1)}[image: {\displaystyle \operatorname {E} [S({\boldsymbol {X}})]=\sum _{i=1}^{K}\operatorname {E} [-X_{i}\ln X_{i}]=\psi (K\alpha +1)-\psi (\alpha +1)}]

### Kullback–Leibler divergence

[[edit][82]]

The [Kullback–Leibler (KL) divergence][83] between two Dirichlet distributions, Dir ( α) {\displaystyle {\text{Dir}}({\boldsymbol {\alpha }})}[image: {\displaystyle {\text{Dir}}({\boldsymbol {\alpha }})}] and Dir ( β) {\displaystyle {\text{Dir}}({\boldsymbol {\beta }})}[image: {\displaystyle {\text{Dir}}({\boldsymbol {\beta }})}], over the same simplex is: [16]

D K L ( D i r ( α) ‖ D i r ( β)) = log ⁡ Γ ( ∑ i = 1 K α i) Γ ( ∑ i = 1 K β i) + ∑ i = 1 K [log ⁡ Γ ( β i) Γ ( α i) + ( α i − β i) ( ψ ( α i) − ψ ( ∑ j = 1 K α j))] {\displaystyle {\begin{aligned}D_{\mathrm {KL} }{\big (}\mathrm {Dir} ({\boldsymbol {\alpha }})\,\|\,\mathrm {Dir} ({\boldsymbol {\beta }}){\big )}&=\log {\frac {\Gamma \left(\sum _{i=1}^{K}\alpha _{i}\right)}{\Gamma \left(\sum _{i=1}^{K}\beta _{i}\right)}}+\sum _{i=1}^{K}\left[\log {\frac {\Gamma (\beta _{i})}{\Gamma (\alpha _{i})}}+(\alpha _{i}-\beta _{i})\left(\psi (\alpha _{i})-\psi \left(\sum _{j=1}^{K}\alpha _{j}\right)\right)\right]\end{aligned}}}[image: {\displaystyle {\begin{aligned}D_{\mathrm {KL} }{\big (}\mathrm {Dir} ({\boldsymbol {\alpha }})\,\|\,\mathrm {Dir} ({\boldsymbol {\beta }}){\big )}&=\log {\frac {\Gamma \left(\sum _{i=1}^{K}\alpha _{i}\right)}{\Gamma \left(\sum _{i=1}^{K}\beta _{i}\right)}}+\sum _{i=1}^{K}\left[\log {\frac {\Gamma (\beta _{i})}{\Gamma (\alpha _{i})}}+(\alpha _{i}-\beta _{i})\left(\psi (\alpha _{i})-\psi \left(\sum _{j=1}^{K}\alpha _{j}\right)\right)\right]\end{aligned}}}]

### Aggregation

[[edit][84]]

If

X = ( X 1, …, X K) ∼ Dir ⁡ ( α 1, …, α K) {\displaystyle X=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} (\alpha _{1},\ldots ,\alpha _{K})}[image: {\displaystyle X=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} (\alpha _{1},\ldots ,\alpha _{K})}]

then, if the random variables with subscripts i and j are dropped from the vector and replaced by their sum,

X ′ = ( X 1, …, X i + X j, …, X K) ∼ Dir ⁡ ( α 1, …, α i + α j, …, α K). {\displaystyle X'=(X_{1},\ldots ,X_{i}+X_{j},\ldots ,X_{K})\sim \operatorname {Dir} (\alpha _{1},\ldots ,\alpha _{i}+\alpha _{j},\ldots ,\alpha _{K}).}[image: {\displaystyle X'=(X_{1},\ldots ,X_{i}+X_{j},\ldots ,X_{K})\sim \operatorname {Dir} (\alpha _{1},\ldots ,\alpha _{i}+\alpha _{j},\ldots ,\alpha _{K}).}]

This aggregation property may be used to derive the marginal distribution of X i {\displaystyle X_{i}}[image: {\displaystyle X_{i}}] mentioned above.

### Neutrality

[[edit][85]]

Main article: [Neutral vector][86]

If X = ( X 1, …, X K) ∼ Dir ⁡ ( α) {\displaystyle X=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} ({\boldsymbol {\alpha }})}[image: {\displaystyle X=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} ({\boldsymbol {\alpha }})}], then the vector X is said to be *neutral*[17] in the sense that *X K*is independent of X ( − K) {\displaystyle X^{(-K)}}[image: {\displaystyle X^{(-K)}}] [3] where

X ( − K) = ( X 1 1 − X K, X 2 1 − X K, …, X K − 1 1 − X K), {\displaystyle X^{(-K)}=\left({\frac {X_{1}}{1-X_{K}}},{\frac {X_{2}}{1-X_{K}}},\ldots ,{\frac {X_{K-1}}{1-X_{K}}}\right),}[image: {\displaystyle X^{(-K)}=\left({\frac {X_{1}}{1-X_{K}}},{\frac {X_{2}}{1-X_{K}}},\ldots ,{\frac {X_{K-1}}{1-X_{K}}}\right),}]

and similarly for removing any of X 2, …, X K − 1 {\displaystyle X_{2},\ldots ,X_{K-1}}[image: {\displaystyle X_{2},\ldots ,X_{K-1}}]. Observe that any permutation of X is also neutral (a property not possessed by samples drawn from a [generalized Dirichlet distribution][87]). [18]

Combining this with the property of aggregation it follows that *X**j*+ ... + *X**K*is independent of ( X 1 X 1 + ⋯ + X j − 1, X 2 X 1 + ⋯ + X j − 1, …, X j − 1 X 1 + ⋯ + X j − 1) {\displaystyle \left({\frac {X_{1}}{X_{1}+\cdots +X_{j-1}}},{\frac {X_{2}}{X_{1}+\cdots +X_{j-1}}},\ldots ,{\frac {X_{j-1}}{X_{1}+\cdots +X_{j-1}}}\right)}[image: {\displaystyle \left({\frac {X_{1}}{X_{1}+\cdots +X_{j-1}}},{\frac {X_{2}}{X_{1}+\cdots +X_{j-1}}},\ldots ,{\frac {X_{j-1}}{X_{1}+\cdots +X_{j-1}}}\right)}]. In fact it is true, further, for the Dirichlet distribution, that for 3 ≤ j ≤ K − 1 {\displaystyle 3\leq j\leq K-1}[image: {\displaystyle 3\leq j\leq K-1}], the pair ( X 1 + ⋯ + X j − 1, X j + ⋯ + X K) {\displaystyle \left(X_{1}+\cdots +X_{j-1},X_{j}+\cdots +X_{K}\right)}[image: {\displaystyle \left(X_{1}+\cdots +X_{j-1},X_{j}+\cdots +X_{K}\right)}], and the two vectors ( X 1 X 1 + ⋯ + X j − 1, X 2 X 1 + ⋯ + X j − 1, …, X j − 1 X 1 + ⋯ + X j − 1) {\displaystyle \left({\frac {X_{1}}{X_{1}+\cdots +X_{j-1}}},{\frac {X_{2}}{X_{1}+\cdots +X_{j-1}}},\ldots ,{\frac {X_{j-1}}{X_{1}+\cdots +X_{j-1}}}\right)}[image: {\displaystyle \left({\frac {X_{1}}{X_{1}+\cdots +X_{j-1}}},{\frac {X_{2}}{X_{1}+\cdots +X_{j-1}}},\ldots ,{\frac {X_{j-1}}{X_{1}+\cdots +X_{j-1}}}\right)}] and ( X j X j + ⋯ + X K, X j + 1 X j + ⋯ + X K, …, X K X j + ⋯ + X K) {\displaystyle \left({\frac {X_{j}}{X_{j}+\cdots +X_{K}}},{\frac {X_{j+1}}{X_{j}+\cdots +X_{K}}},\ldots ,{\frac {X_{K}}{X_{j}+\cdots +X_{K}}}\right)}[image: {\displaystyle \left({\frac {X_{j}}{X_{j}+\cdots +X_{K}}},{\frac {X_{j+1}}{X_{j}+\cdots +X_{K}}},\ldots ,{\frac {X_{K}}{X_{j}+\cdots +X_{K}}}\right)}], viewed as triple of normalised random vectors, are [mutually independent][88]. The analogous result is true for partition of the indices {1, 2, ..., *K*} into any other pair of non-singleton subsets.

### Characteristic function

[[edit][89]]

The characteristic function of the Dirichlet distribution is a [confluent][90] form of the [Lauricella hypergeometric series][91]. It is given by [Phillips][92] as [19]

C F ( s 1, …, s K − 1) = E ⁡ ( e i ( s 1 X 1 + ⋯ + s K − 1 X K − 1)) = Ψ [K − 1] ( α 1, …, α K − 1; α 0; i s 1, …, i s K − 1) {\displaystyle CF\left(s_{1},\ldots ,s_{K-1}\right)=\operatorname {E} \left(e^{i\left(s_{1}X_{1}+\cdots +s_{K-1}X_{K-1}\right)}\right)=\Psi ^{\left[K-1\right]}(\alpha _{1},\ldots ,\alpha _{K-1};\alpha _{0};is_{1},\ldots ,is_{K-1})}[image: {\displaystyle CF\left(s_{1},\ldots ,s_{K-1}\right)=\operatorname {E} \left(e^{i\left(s_{1}X_{1}+\cdots +s_{K-1}X_{K-1}\right)}\right)=\Psi ^{\left[K-1\right]}(\alpha _{1},\ldots ,\alpha _{K-1};\alpha _{0};is_{1},\ldots ,is_{K-1})}]

where

Ψ [m] ( a 1, …, a m; c; z 1, … z m) = ∑ ( a 1) k 1 ⋯ ( a m) k m z 1 k 1 ⋯ z m k m ( c) k k 1! ⋯ k m!. {\displaystyle \Psi ^{[m]}(a_{1},\ldots ,a_{m};c;z_{1},\ldots z_{m})=\sum {\frac {(a_{1})_{k_{1}}\cdots (a_{m})_{k_{m}}\,z_{1}^{k_{1}}\cdots z_{m}^{k_{m}}}{(c)_{k}\,k_{1}!\cdots k_{m}!}}.}[image: {\displaystyle \Psi ^{[m]}(a_{1},\ldots ,a_{m};c;z_{1},\ldots z_{m})=\sum {\frac {(a_{1})_{k_{1}}\cdots (a_{m})_{k_{m}}\,z_{1}^{k_{1}}\cdots z_{m}^{k_{m}}}{(c)_{k}\,k_{1}!\cdots k_{m}!}}.}]

The sum is over non-negative integers k 1, …, k m {\displaystyle k_{1},\ldots ,k_{m}}[image: {\displaystyle k_{1},\ldots ,k_{m}}] and k = k 1 + ⋯ + k m {\displaystyle k=k_{1}+\cdots +k_{m}}[image: {\displaystyle k=k_{1}+\cdots +k_{m}}]. Phillips goes on to state that this form is "inconvenient for numerical calculation" and gives an alternative in terms of a [complex path integral][93]:

Ψ [m] = Γ ( c) 2 π i ∫ L e t t a 1 + ⋯ + a m − c ∏ j = 1 m ( t − z j) − a j d t {\displaystyle \Psi ^{[m]}={\frac {\Gamma (c)}{2\pi i}}\int _{L}e^{t}\,t^{a_{1}+\cdots +a_{m}-c}\,\prod _{j=1}^{m}(t-z_{j})^{-a_{j}}\,dt}[image: {\displaystyle \Psi ^{[m]}={\frac {\Gamma (c)}{2\pi i}}\int _{L}e^{t}\,t^{a_{1}+\cdots +a_{m}-c}\,\prod _{j=1}^{m}(t-z_{j})^{-a_{j}}\,dt}]

where L denotes any path in the complex plane originating at − ∞ {\displaystyle -\infty }[image: {\displaystyle -\infty }], encircling in the positive direction all the singularities of the integrand and returning to − ∞ {\displaystyle -\infty }[image: {\displaystyle -\infty }].

### Inequality

[[edit][94]]

Probability density function f ( x 1, …, x K − 1; α 1, …, α K) {\displaystyle f\left(x_{1},\ldots ,x_{K-1};\alpha _{1},\ldots ,\alpha _{K}\right)}[image: {\displaystyle f\left(x_{1},\ldots ,x_{K-1};\alpha _{1},\ldots ,\alpha _{K}\right)}] plays a key role in a multifunctional inequality which implies various bounds for the Dirichlet distribution. [20]

Another inequality relates the moment-generating function of the Dirichlet distribution to the convex conjugate of the scaled reversed Kullback-Leibler divergence: [21]

log ⁡ E ⁡ ( exp ⁡ ∑ i = 1 K s i X i) ≤ sup p ∑ i = 1 K ( p i s i − α i log ⁡ ( α i α 0 p i)), {\displaystyle \log \operatorname {E} \left(\exp {\sum _{i=1}^{K}s_{i}X_{i}}\right)\leq \sup _{p}\sum _{i=1}^{K}\left(p_{i}s_{i}-\alpha _{i}\log \left({\frac {\alpha _{i}}{\alpha _{0}p_{i}}}\right)\right),}[image: {\displaystyle \log \operatorname {E} \left(\exp {\sum _{i=1}^{K}s_{i}X_{i}}\right)\leq \sup _{p}\sum _{i=1}^{K}\left(p_{i}s_{i}-\alpha _{i}\log \left({\frac {\alpha _{i}}{\alpha _{0}p_{i}}}\right)\right),}] where the supremum is taken over p spanning the (*K*− 1) -simplex.

## Related distributions

[[edit][95]]

When X = ( X 1, …, X K) ∼ Dir ⁡ ( α 1, …, α K) {\displaystyle {\boldsymbol {X}}=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} \left(\alpha _{1},\ldots ,\alpha _{K}\right)}[image: {\displaystyle {\boldsymbol {X}}=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} \left(\alpha _{1},\ldots ,\alpha _{K}\right)}], the marginal distribution of each component X i ∼ Beta ⁡ ( α i, α 0 − α i) {\displaystyle X_{i}\sim \operatorname {Beta} (\alpha _{i},\alpha _{0}-\alpha _{i})}[image: {\displaystyle X_{i}\sim \operatorname {Beta} (\alpha _{i},\alpha _{0}-\alpha _{i})}], a [Beta distribution][22]. In particular, if *K*= 2 then X 1 ∼ Beta ⁡ ( α 1, α 2) {\displaystyle X_{1}\sim \operatorname {Beta} (\alpha _{1},\alpha _{2})}[image: {\displaystyle X_{1}\sim \operatorname {Beta} (\alpha _{1},\alpha _{2})}] is equivalent to X = ( X 1, 1 − X 1) ∼ Dir ⁡ ( α 1, α 2) {\displaystyle {\boldsymbol {X}}=(X_{1},1-X_{1})\sim \operatorname {Dir} \left(\alpha _{1},\alpha _{2}\right)}[image: {\displaystyle {\boldsymbol {X}}=(X_{1},1-X_{1})\sim \operatorname {Dir} \left(\alpha _{1},\alpha _{2}\right)}].

For K independently distributed [Gamma distributions][96]:

Y 1 ∼ Gamma ⁡ ( α 1, 1), …, Y K ∼ Gamma ⁡ ( α K, 1) {\displaystyle Y_{1}\sim \operatorname {Gamma} (\alpha _{1},1),\ldots ,Y_{K}\sim \operatorname {Gamma} (\alpha _{K},1)}[image: {\displaystyle Y_{1}\sim \operatorname {Gamma} (\alpha _{1},1),\ldots ,Y_{K}\sim \operatorname {Gamma} (\alpha _{K},1)}]

we have writing α 0:= ∑ i = 1 K α i {\displaystyle \alpha _{0}:=\sum _{i=1}^{K}\limits \alpha _{i}}[image: {\displaystyle \alpha _{0}:=\sum _{i=1}^{K}\limits \alpha _{i}}]: [22]: 402

V = ∑ i = 1 K Y i ∼ Gamma ⁡ ( α 0, 1), {\displaystyle V=\sum _{i=1}^{K}Y_{i}\sim \operatorname {Gamma} \left(\alpha _{0},1\right),}[image: {\displaystyle V=\sum _{i=1}^{K}Y_{i}\sim \operatorname {Gamma} \left(\alpha _{0},1\right),}] X = ( X 1, …, X K) = ( Y 1 V, …, Y K V) ∼ Dir ⁡ ( α 1, …, α K). {\displaystyle X=(X_{1},\ldots ,X_{K})=\left({\frac {Y_{1}}{V}},\ldots ,{\frac {Y_{K}}{V}}\right)\sim \operatorname {Dir} \left(\alpha _{1},\ldots ,\alpha _{K}\right).}[image: {\displaystyle X=(X_{1},\ldots ,X_{K})=\left({\frac {Y_{1}}{V}},\ldots ,{\frac {Y_{K}}{V}}\right)\sim \operatorname {Dir} \left(\alpha _{1},\ldots ,\alpha _{K}\right).}]

Although the *X i*s are not independent from one another, they can be seen to be generated from a set of K independent [gamma][96] random variables. [22]: 594 Unfortunately, since the sum V is lost in forming X (in fact it can be shown that V is stochastically independent of X), it is not possible to recover the original gamma random variables from these values alone. Nevertheless, because independent random variables are simpler to work with, this reparametrization can still be useful for proofs about properties of the Dirichlet distribution.

### Conjugate prior of the Dirichlet distribution

[[edit][97]]

Because the Dirichlet distribution is an [exponential family distribution][98] it has a conjugate prior. The conjugate prior is of the form: [23]

CD ⁡ ( α ∣ v, η) ∝ ( 1 B ⁡ ( α)) η exp ⁡ ( − ∑ k v k α k). {\displaystyle \operatorname {CD} ({\boldsymbol {\alpha }}\mid {\boldsymbol {v}},\eta )\propto \left({\frac {1}{\operatorname {B} ({\boldsymbol {\alpha }})}}\right)^{\eta }\exp \left(-\sum _{k}v_{k}\alpha _{k}\right).}[image: {\displaystyle \operatorname {CD} ({\boldsymbol {\alpha }}\mid {\boldsymbol {v}},\eta )\propto \left({\frac {1}{\operatorname {B} ({\boldsymbol {\alpha }})}}\right)^{\eta }\exp \left(-\sum _{k}v_{k}\alpha _{k}\right).}]

Here v {\displaystyle {\boldsymbol {v}}}[image: {\displaystyle {\boldsymbol {v}}}] is a K -dimensional real vector and η {\displaystyle \eta }[image: {\displaystyle \eta }] is a scalar parameter. The domain of ( v, η) {\displaystyle ({\boldsymbol {v}},\eta )}[image: {\displaystyle ({\boldsymbol {v}},\eta )}] is restricted to the set of parameters for which the above unnormalized density function can be normalized. The (necessary and sufficient) condition is: [24]

0\\;\\;\\;\\;\\text{ and } \\;\\;\\;\\;\\eta>-1 \\;\\;\\;\\;\\text{ and } \\;\\;\\;\\;(\\eta\\leq0\\;\\;\\;\\;\\text{ or }\\;\\;\\;\\;\\sum_k \\exp-\\frac{v_k} \\eta < 1)\n"}}'> 0\;\;\;\;{\text{ and }}\;\;\;\;\eta >-1\;\;\;\;{\text{ and }}\;\;\;\;(\eta \leq 0\;\;\;\;{\text{ or }}\;\;\;\;\sum _{k}\exp -{\frac {v_{k}}{\eta }}<1)}"> ∀ k v k > 0 and η > − 1 and ( η ≤ 0 or ∑ k exp − v k η < 1) {\displaystyle \forall k\;\;v_{k}>0\;\;\;\;{\text{ and }}\;\;\;\;\eta >-1\;\;\;\;{\text{ and }}\;\;\;\;(\eta \leq 0\;\;\;\;{\text{ or }}\;\;\;\;\sum _{k}\exp -{\frac {v_{k}}{\eta }}<1)} 0\;\;\;\;{\text{ and }}\;\;\;\;\eta >-1\;\;\;\;{\text{ and }}\;\;\;\;(\eta \leq 0\;\;\;\;{\text{ or }}\;\;\;\;\sum _{k}\exp -{\frac {v_{k}}{\eta }}<1)}"/>

The conjugation property can be expressed as

if [*prior*: α ∼ CD ⁡ ( ⋅ ∣ v, η) {\displaystyle {\boldsymbol {\alpha }}\sim \operatorname {CD} (\cdot \mid {\boldsymbol {v}},\eta )}[image: {\displaystyle {\boldsymbol {\alpha }}\sim \operatorname {CD} (\cdot \mid {\boldsymbol {v}},\eta )}]] and [*observation*: x ∣ α ∼ Dirichlet ⁡ ( ⋅ ∣ α) {\displaystyle {\boldsymbol {x}}\mid {\boldsymbol {\alpha }}\sim \operatorname {Dirichlet} (\cdot \mid {\boldsymbol {\alpha }})}[image: {\displaystyle {\boldsymbol {x}}\mid {\boldsymbol {\alpha }}\sim \operatorname {Dirichlet} (\cdot \mid {\boldsymbol {\alpha }})}]] then [*posterior*: α ∣ x ∼ CD ⁡ ( ⋅ ∣ v − log ⁡ x, η + 1) {\displaystyle {\boldsymbol {\alpha }}\mid {\boldsymbol {x}}\sim \operatorname {CD} (\cdot \mid {\boldsymbol {v}}-\log {\boldsymbol {x}},\eta +1)}[image: {\displaystyle {\boldsymbol {\alpha }}\mid {\boldsymbol {x}}\sim \operatorname {CD} (\cdot \mid {\boldsymbol {v}}-\log {\boldsymbol {x}},\eta +1)}]].

In the published literature there is no practical algorithm to efficiently generate samples from CD ⁡ ( α ∣ v, η) {\displaystyle \operatorname {CD} ({\boldsymbol {\alpha }}\mid {\boldsymbol {v}},\eta )}[image: {\displaystyle \operatorname {CD} ({\boldsymbol {\alpha }}\mid {\boldsymbol {v}},\eta )}].

### Generalization by scaling and translation of log-probabilities

[[edit][99]]

As noted above, Dirichlet variates can be generated by normalizing independent [gamma][96] variates. If instead one normalizes [generalized gamma][100] variates, one obtains variates from the simplicial generalized beta distribution (SGB). [25] On the other hand, SGB variates can also be obtained by applying the [softmax function][101] to scaled and translated logarithms of Dirichlet variates. Specifically, let x = ( x 1, …, x K) ∼ Dir ⁡ ( α) {\displaystyle \mathbf {x} =(x_{1},\ldots ,x_{K})\sim \operatorname {Dir} ({\boldsymbol {\alpha }})}[image: {\displaystyle \mathbf {x} =(x_{1},\ldots ,x_{K})\sim \operatorname {Dir} ({\boldsymbol {\alpha }})}] and let y = ( y 1, …, y K) {\displaystyle \mathbf {y} =(y_{1},\ldots ,y_{K})}[image: {\displaystyle \mathbf {y} =(y_{1},\ldots ,y_{K})}], where applying the logarithm elementwise: y = softmax ⁡ ( a − 1 log ⁡ x + log ⁡ b) ⟺ x = softmax ⁡ ( a log ⁡ y − a log ⁡ b) {\displaystyle \mathbf {y} =\operatorname {softmax} (a^{-1}\log \mathbf {x} +\log \mathbf {b} )\;\iff \;\mathbf {x} =\operatorname {softmax} (a\log \mathbf {y} -a\log \mathbf {b} )}[image: {\displaystyle \mathbf {y} =\operatorname {softmax} (a^{-1}\log \mathbf {x} +\log \mathbf {b} )\;\iff \;\mathbf {x} =\operatorname {softmax} (a\log \mathbf {y} -a\log \mathbf {b} )}] or y k = b k x k 1 / a ∑ i = 1 K b i x i 1 / a ⟺ x k = ( y k / b k) a ∑ i = 1 K ( y i / b i) a {\displaystyle y_{k}={\frac {b_{k}x_{k}^{1/a}}{\sum _{i=1}^{K}b_{i}x_{i}^{1/a}}}\;\iff \;x_{k}={\frac {(y_{k}/b_{k})^{a}}{\sum _{i=1}^{K}(y_{i}/b_{i})^{a}}}}[image: {\displaystyle y_{k}={\frac {b_{k}x_{k}^{1/a}}{\sum _{i=1}^{K}b_{i}x_{i}^{1/a}}}\;\iff \;x_{k}={\frac {(y_{k}/b_{k})^{a}}{\sum _{i=1}^{K}(y_{i}/b_{i})^{a}}}}] where 0"}}'> 0}"> a > 0 {\displaystyle a>0} 0}"/> and b = ( b 1, …, b K) {\displaystyle \mathbf {b} =(b_{1},\ldots ,b_{K})}[image: {\displaystyle \mathbf {b} =(b_{1},\ldots ,b_{K})}], with all 0"}}'> 0}"> b k > 0 {\displaystyle b_{k}>0} 0}"/>, then y ∼ SGB ⁡ ( a, b, α) {\displaystyle \mathbf {y} \sim \operatorname {SGB} (a,\mathbf {b} ,{\boldsymbol {\alpha }})}[image: {\displaystyle \mathbf {y} \sim \operatorname {SGB} (a,\mathbf {b} ,{\boldsymbol {\alpha }})}]. The SGB density function can be derived by noting that the transformation x ↦ y {\displaystyle \mathbf {x} \mapsto \mathbf {y} }[image: {\displaystyle \mathbf {x} \mapsto \mathbf {y} }], which is a [bijection][102] from the simplex to itself, induces a [differential volume change factor][103] [26] of: R ( y, a, b) = a 1 − K ∏ k = 1 K y k x k {\displaystyle R(\mathbf {y} ,a,\mathbf {b} )=a^{1-K}\prod _{k=1}^{K}{\frac {y_{k}}{x_{k}}}}[image: {\displaystyle R(\mathbf {y} ,a,\mathbf {b} )=a^{1-K}\prod _{k=1}^{K}{\frac {y_{k}}{x_{k}}}}] where it is understood that x {\displaystyle \mathbf {x} }[image: {\displaystyle \mathbf {x} }] is recovered as a function of y {\displaystyle \mathbf {y} }[image: {\displaystyle \mathbf {y} }], as shown above. This facilitates writing the SGB density in terms of the Dirichlet density, as: f SGB ( y ∣ a, b, α) = f Dir ( x ∣ α) R ( y, a, b) {\displaystyle f_{\text{SGB}}(\mathbf {y} \mid a,\mathbf {b} ,{\boldsymbol {\alpha }})={\frac {f_{\text{Dir}}(\mathbf {x} \mid {\boldsymbol {\alpha }})}{R(\mathbf {y} ,a,\mathbf {b} )}}}[image: {\displaystyle f_{\text{SGB}}(\mathbf {y} \mid a,\mathbf {b} ,{\boldsymbol {\alpha }})={\frac {f_{\text{Dir}}(\mathbf {x} \mid {\boldsymbol {\alpha }})}{R(\mathbf {y} ,a,\mathbf {b} )}}}] This generalization of the Dirichlet density, via a [change of variables][104], is closely related to a [normalizing flow][105], while the differential volume change is not given by the [Jacobian determinant][106] of x ↦ y: R K → R K {\displaystyle \mathbf {x} \mapsto \mathbf {y}:\mathbb {R} ^{K}\to \mathbb {R} ^{K}} [image: {\displaystyle \mathbf {x} \mapsto \mathbf {y} :\mathbb {R} ^{K}\to \mathbb {R} ^{K}}] which is zero, but by the Jacobian determinant of ( x 1, …, x K − 1) ↦ ( y 1, …, y K − 1) {\displaystyle (x_{1},\ldots ,x_{K-1})\mapsto \mathbf {(} y_{1},\ldots ,y_{K-1})}[image: {\displaystyle (x_{1},\ldots ,x_{K-1})\mapsto \mathbf {(} y_{1},\ldots ,y_{K-1})}], as explained in more detail at [Normalizing flow § Simplex flow][107].

For further insight into the interaction between the Dirichlet shape parameters α {\displaystyle {\boldsymbol {\alpha }}}[image: {\displaystyle {\boldsymbol {\alpha }}}], and the transformation parameters a, b {\displaystyle a,\mathbf {b} }[image: {\displaystyle a,\mathbf {b} }], it may be helpful to consider the logarithmic marginals, log ⁡ x k 1 − x k {\displaystyle \log {\frac {x_{k}}{1-x_{k}}}}[image: {\displaystyle \log {\frac {x_{k}}{1-x_{k}}}}], which follow the [logistic-beta distribution][108], B σ ( α k, ∑ i ≠ k α i) {\displaystyle B_{\sigma }(\alpha _{k},\sum _{i\neq k}\alpha _{i})}[image: {\displaystyle B_{\sigma }(\alpha _{k},\sum _{i\neq k}\alpha _{i})}]. See in particular the sections on [tail behaviour][109] and [generalization with location and scale parameters][110].

#### Application

[[edit][111]]

When b 1 = b 2 = ⋯ = b K {\displaystyle b_{1}=b_{2}=\cdots =b_{K}}[image: {\displaystyle b_{1}=b_{2}=\cdots =b_{K}}], then the transformation simplifies to x ↦ softmax ⁡ ( a − 1 log ⁡ x) {\displaystyle \mathbf {x} \mapsto \operatorname {softmax} (a^{-1}\log \mathbf {x} )}[image: {\displaystyle \mathbf {x} \mapsto \operatorname {softmax} (a^{-1}\log \mathbf {x} )}], which is known as [temperature scaling][112] in [machine learning][113], where it is used as a calibration transform for multiclass probabilistic classifiers. [27] Traditionally the temperature parameter ( a {\displaystyle a}[image: {\displaystyle a}] here) is learnt [discriminatively][114] by minimizing multiclass [cross-entropy][115] over a supervised calibration data set with known class labels. But the above PDF transformation mechanism can be used to facilitate also the design of [generatively trained][116] calibration models with a temperature scaling component.

## Occurrence and applications

[[edit][117]]

### Bayesian models

[[edit][118]]

Dirichlet distributions are most commonly used as the [prior distribution][23] of [categorical variables][26] or [multinomial variables][27] in Bayesian [mixture models][67] and other [hierarchical Bayesian models][68]. (In many fields, such as in [natural language processing][119], categorical variables are often imprecisely called "multinomial variables". Such a usage is unlikely to cause confusion, just as when [Bernoulli distributions][120] and [binomial distributions][121] are commonly conflated.)

Inference over hierarchical Bayesian models is often done using [Gibbs sampling][74], and in such a case, instances of the Dirichlet distribution are typically [marginalized out][61] of the model by integrating out the Dirichlet [random variable][122]. This causes the various categorical variables drawn from the same Dirichlet random variable to become correlated, and the joint distribution over them assumes a [Dirichlet-multinomial distribution][72], conditioned on the hyperparameters of the Dirichlet distribution (the [concentration parameters][4]). One of the reasons for doing this is that Gibbs sampling of the [Dirichlet-multinomial distribution][72] is extremely easy; see that article for more information.

### Intuitive interpretations of the parameters

[[edit][123]]

#### The concentration parameter

[[edit][124]]

Dirichlet distributions are very often used as [prior distributions][23] in [Bayesian inference][125]. The simplest and perhaps most common type of Dirichlet prior is the symmetric Dirichlet distribution, where all parameters are equal. This corresponds to the case where you have no prior information to favor one component over any other. As described above, the single value α to which all parameters are set is called the [concentration parameter][4]. If the sample space of the Dirichlet distribution is interpreted as a [discrete probability distribution][63], then intuitively the concentration parameter can be thought of as determining how "concentrated" the probability mass of the Dirichlet distribution to its center, leading to samples with mass dispersed almost equally among all components, i.e., with a value much less than 1, the mass will be highly concentrated in a few components, and all the rest will have almost no mass, and with a value much greater than 1, the mass will be dispersed almost equally among all the components. See the article on the [concentration parameter][4] for further discussion.

#### String cutting

[[edit][126]]

One example use of the Dirichlet distribution is if one wanted to cut strings (each of initial length 1.0) into K pieces with different lengths, where each piece had a designated average length, but allowing some variation in the relative sizes of the pieces. Recall that α 0 = ∑ i = 1 K α i. {\displaystyle \alpha _{0}=\sum _{i=1}^{K}\alpha _{i}.}[image: {\displaystyle \alpha _{0}=\sum _{i=1}^{K}\alpha _{i}.}] The α i / α 0 {\displaystyle \alpha _{i}/\alpha _{0}}[image: {\displaystyle \alpha _{i}/\alpha _{0}}] values specify the mean lengths of the cut pieces of string resulting from the distribution. The variance around this mean varies inversely with α 0 {\displaystyle \alpha _{0}}[image: {\displaystyle \alpha _{0}}].

[image: Example of Dirichlet(1/2,1/3,1/6) distribution] [127] Example of Dirichlet(1/2,1/3,1/6) distribution

#### [Pólya's urn][128]

[[edit][129]]

Consider an urn containing balls of K different colors. Initially, the urn contains *α*1 balls of color 1, *α*2 balls of color 2, and so on. Now perform N draws from the urn, where after each draw, the ball is placed back into the urn with an additional ball of the same color. In the limit as N approaches infinity, the proportions of different colored balls in the urn will be distributed as Dir(*α*1, ..., *α K*). [28]

For a formal proof, note that the proportions of the different colored balls form a bounded [0,1]*K*-valued [martingale][130], hence by the [martingale convergence theorem][131], these proportions converge [almost surely][132] and [in mean][133] to a limiting random vector. To see that this limiting vector has the above Dirichlet distribution, check that all mixed [moments][134] agree.

Each draw from the urn modifies the probability of drawing a ball of any one color from the urn in the future. This modification diminishes with the number of draws, since the relative effect of adding a new ball to the urn diminishes as the urn accumulates increasing numbers of balls.

## Random variate generation

[[edit][135]]

Further information: [Non-uniform random variate generation][136]

### From gamma distribution

[[edit][137]]

With a source of Gamma-distributed random variates, one can easily sample a random vector x = ( x 1, …, x K) {\displaystyle x=(x_{1},\ldots ,x_{K})}[image: {\displaystyle x=(x_{1},\ldots ,x_{K})}] from the K -dimensional Dirichlet distribution with parameters ( α 1, …, α K) {\displaystyle (\alpha _{1},\ldots ,\alpha _{K})}[image: {\displaystyle (\alpha _{1},\ldots ,\alpha _{K})}]. First, draw K independent random samples y 1, …, y K {\displaystyle y_{1},\ldots ,y_{K}}[image: {\displaystyle y_{1},\ldots ,y_{K}}] from [Gamma distributions][96] each with density

Gamma ⁡ ( α i, 1) = y i α i − 1 e − y i Γ ( α i), {\displaystyle \operatorname {Gamma} (\alpha _{i},1)={\frac {y_{i}^{\alpha _{i}-1}\;e^{-y_{i}}}{\Gamma (\alpha _{i})}},\!}[image: {\displaystyle \operatorname {Gamma} (\alpha _{i},1)={\frac {y_{i}^{\alpha _{i}-1}\;e^{-y_{i}}}{\Gamma (\alpha _{i})}},\!}]

and then set

x i = y i ∑ j = 1 K y j. {\displaystyle x_{i}={\frac {y_{i}}{\sum _{j=1}^{K}y_{j}}}.}[image: {\displaystyle x_{i}={\frac {y_{i}}{\sum _{j=1}^{K}y_{j}}}.}]

\\{y_{i}\\}</math>, is given by the product:\n\n<math display=block>e^{-\\sum_{i}y_{i}} \\prod _{i=1}^{K} \\frac{y_{i}^{\\alpha _{i}-1}}{\\Gamma (\\alpha _{i})} </math>\n\nNext, one uses a change of variables, parametrising <math> \\{y_{i}\\}</math> in terms of <math> y_{1}, y_{2}, \\ldots , y_{K-1} </math> and <math> \\sum _{i=1}^{K}y_{i}</math> , and performs a change of variables from <math> y \\to x </math> such that <math>\\bar x = \\textstyle\\sum_{i=1}^{K}y_{i}, x_{1} = \\frac{y_{1}}{\\bar x}, x_{2} = \\frac{y_{2}}{\\bar x}, \\ldots , x_{K-1} = \\frac{y_{K-1}}{\\bar x}</math>. Each of the variables <math>0 \\leq x_{1}, x_{2}, \\ldots , x_{k-1} \\leq 1 </math> and likewise <math>0 \\leq \\textstyle\\sum _{i=1}^{K-1}x_{i} \\leq 1 </math>. One must then use the change of variables formula, <math> P(x) = P(y(x))\\bigg|\\frac{\\partial y}{\\partial x}\\bigg| </math> in which <math>\\bigg|\\frac{\\partial y}{\\partial x}\\bigg|</math> is the transformation Jacobian. Writing y explicitly as a function of x, one obtains \n<math>y_{1} = \\bar xx_{1}, y_{2} = \\bar xx_{2} \\ldots y_{K-1} = \\bar xx_{K-1}, y_{K} = \\bar x(1-\\textstyle\\sum_{i=1}^{K-1}x_{i}) </math>\nThe Jacobian now looks like\n<math display=block>\\begin{vmatrix}\\bar x & 0 & \\ldots & x_{1} \\\\ 0 & \\bar x & \\ldots & x_{2} \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ -\\bar x & -\\bar x & \\ldots & 1-\\sum_{i=1}^{K-1}x_{i} \\end{vmatrix}</math>\n\nThe determinant can be evaluated by noting that it remains unchanged if multiples of a row are added to another row, and adding each of the first K-1 rows to the bottom row to obtain\n\n<math display=block>\\begin{vmatrix}\\bar x & 0 & \\ldots & x_{1} \\\\ 0 & \\bar x & \\ldots & x_{2} \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ 0 & 0 & \\ldots & 1 \\end{vmatrix} </math>\n\nwhich can be expanded about the bottom row to obtain the determinant value <math>\\bar x^{K-1}</math>. Substituting for x in the joint pdf and including the Jacobian determinant, one obtains:\n\n<math display=block>\n\\begin{align}\n&\\frac{\\left[\\prod _{i=1}^{K-1}(\\bar xx_{i})^{\\alpha _{i}-1} \\right] \\left[\\bar x(1-\\sum_{i=1}^{K-1}x_{i})\\right]^{\\alpha_{K}-1}}{\\prod _{i=1}^{K}\\Gamma (\\alpha _{i})}\\bar x^{K-1}e^{-\\bar x} \\\\\n=&\\frac{\\Gamma(\\bar\\alpha)\\left[\\prod _{i=1}^{K-1}(x_{i})^{\\alpha _{i}-1} \\right] \\left[1-\\sum_{i=1}^{K-1}x_{i}\\right]^{\\alpha_{K}-1}}{\\prod _{i=1}^{K}\\Gamma (\\alpha _{i})}\\times\\frac{\\bar x^{\\bar\\alpha-1}e^{-\\bar x}}{\\Gamma(\\bar\\alpha)}\n\\end{align}\n</math>\nwhere <math>\\bar\\alpha=\\textstyle\\sum_{i=1}^K\\alpha_i</math>. The right-hand side can be recognized as the product of a Dirichlet pdf for the <math>x_i</math> and a gamma pdf for <math>\\bar x</math>. The product form shows the Dirichlet and gamma variables are independent, so the latter can be integrated out by simply omitting it, to obtain:\n<math display=block>x_{1}, x_{2}, \\ldots, x_{K-1} \\sim \\frac{(1-\\sum_{i=1}^{K-1}x_{i})^{\\alpha _{K}-1}\\prod _{i=1}^{K-1}x_{i}^{\\alpha _{i} -1}}{B(\\boldsymbol{\\alpha})} </math>\n\nWhich is equivalent to\n\n<math display=block>\\frac{\\prod _{i=1}^{K} x_{i}^{\\alpha_{i}-1}}{B(\\boldsymbol{\\alpha})} </math> with support <math> \\sum_{i=1}^{K}x_{i}=1 </math>\n\n",{"template":{"target":{"wt":"hidden end","href":"./Template:Hidden_end"},"params":{},"i":1}}]}'>

[Proof]

The joint distribution of the independently sampled gamma variates, { y i } {\displaystyle \{y_{i}\}}[image: {\displaystyle \{y_{i}\}}], is given by the product:

e − ∑ i y i ∏ i = 1 K y i α i − 1 Γ ( α i) {\displaystyle e^{-\sum _{i}y_{i}}\prod _{i=1}^{K}{\frac {y_{i}^{\alpha _{i}-1}}{\Gamma (\alpha _{i})}}}[image: {\displaystyle e^{-\sum _{i}y_{i}}\prod _{i=1}^{K}{\frac {y_{i}^{\alpha _{i}-1}}{\Gamma (\alpha _{i})}}}]

Next, one uses a change of variables, parametrising { y i } {\displaystyle \{y_{i}\}}[image: {\displaystyle \{y_{i}\}}] in terms of y 1, y 2, …, y K − 1 {\displaystyle y_{1},y_{2},\ldots ,y_{K-1}}[image: {\displaystyle y_{1},y_{2},\ldots ,y_{K-1}}] and ∑ i = 1 K y i {\displaystyle \sum _{i=1}^{K}y_{i}}[image: {\displaystyle \sum _{i=1}^{K}y_{i}}], and performs a change of variables from y → x {\displaystyle y\to x}[image: {\displaystyle y\to x}] such that x ¯ = ∑ i = 1 K y i, x 1 = y 1 x ¯, x 2 = y 2 x ¯, …, x K − 1 = y K − 1 x ¯ {\displaystyle {\bar {x}}=\textstyle \sum _{i=1}^{K}y_{i},x_{1}={\frac {y_{1}}{\bar {x}}},x_{2}={\frac {y_{2}}{\bar {x}}},\ldots ,x_{K-1}={\frac {y_{K-1}}{\bar {x}}}}[image: {\displaystyle {\bar {x}}=\textstyle \sum _{i=1}^{K}y_{i},x_{1}={\frac {y_{1}}{\bar {x}}},x_{2}={\frac {y_{2}}{\bar {x}}},\ldots ,x_{K-1}={\frac {y_{K-1}}{\bar {x}}}}]. Each of the variables 0 ≤ x 1, x 2, …, x k − 1 ≤ 1 {\displaystyle 0\leq x_{1},x_{2},\ldots ,x_{k-1}\leq 1}[image: {\displaystyle 0\leq x_{1},x_{2},\ldots ,x_{k-1}\leq 1}] and likewise 0 ≤ ∑ i = 1 K − 1 x i ≤ 1 {\displaystyle 0\leq \textstyle \sum _{i=1}^{K-1}x_{i}\leq 1}[image: {\displaystyle 0\leq \textstyle \sum _{i=1}^{K-1}x_{i}\leq 1}]. One must then use the change of variables formula, P ( x) = P ( y ( x)) | ∂ y ∂ x | {\displaystyle P(x)=P(y(x)){\bigg |}{\frac {\partial y}{\partial x}}{\bigg |}}[image: {\displaystyle P(x)=P(y(x)){\bigg |}{\frac {\partial y}{\partial x}}{\bigg |}}] in which | ∂ y ∂ x | {\displaystyle {\bigg |}{\frac {\partial y}{\partial x}}{\bigg |}}[image: {\displaystyle {\bigg |}{\frac {\partial y}{\partial x}}{\bigg |}}] is the transformation Jacobian. Writing y explicitly as a function of x, one obtains y 1 = x ¯ x 1, y 2 = x ¯ x 2 … y K − 1 = x ¯ x K − 1, y K = x ¯ ( 1 − ∑ i = 1 K − 1 x i) {\displaystyle y_{1}={\bar {x}}x_{1},y_{2}={\bar {x}}x_{2}\ldots y_{K-1}={\bar {x}}x_{K-1},y_{K}={\bar {x}}(1-\textstyle \sum _{i=1}^{K-1}x_{i})}[image: {\displaystyle y_{1}={\bar {x}}x_{1},y_{2}={\bar {x}}x_{2}\ldots y_{K-1}={\bar {x}}x_{K-1},y_{K}={\bar {x}}(1-\textstyle \sum _{i=1}^{K-1}x_{i})}] The Jacobian now looks like | x ¯ 0 … x 1 0 x ¯ … x 2 ⋮ ⋮ ⋱ ⋮ − x ¯ − x ¯ … 1 − ∑ i = 1 K − 1 x i | {\displaystyle {\begin{vmatrix}{\bar {x}}&0&\ldots &x_{1}\\0&{\bar {x}}&\ldots &x_{2}\\\vdots &\vdots &\ddots &\vdots \\-{\bar {x}}&-{\bar {x}}&\ldots &1-\sum _{i=1}^{K-1}x_{i}\end{vmatrix}}}[image: {\displaystyle {\begin{vmatrix}{\bar {x}}&0&\ldots &x_{1}\\0&{\bar {x}}&\ldots &x_{2}\\\vdots &\vdots &\ddots &\vdots \\-{\bar {x}}&-{\bar {x}}&\ldots &1-\sum _{i=1}^{K-1}x_{i}\end{vmatrix}}}]

The determinant can be evaluated by noting that it remains unchanged if multiples of a row are added to another row, and adding each of the first K-1 rows to the bottom row to obtain

| x ¯ 0 … x 1 0 x ¯ … x 2 ⋮ ⋮ ⋱ ⋮ 0 0 … 1 | {\displaystyle {\begin{vmatrix}{\bar {x}}&0&\ldots &x_{1}\\0&{\bar {x}}&\ldots &x_{2}\\\vdots &\vdots &\ddots &\vdots \\0&0&\ldots &1\end{vmatrix}}}[image: {\displaystyle {\begin{vmatrix}{\bar {x}}&0&\ldots &x_{1}\\0&{\bar {x}}&\ldots &x_{2}\\\vdots &\vdots &\ddots &\vdots \\0&0&\ldots &1\end{vmatrix}}}]

which can be expanded about the bottom row to obtain the determinant value x ¯ K − 1 {\displaystyle {\bar {x}}^{K-1}}[image: {\displaystyle {\bar {x}}^{K-1}}]. Substituting for x in the joint pdf and including the Jacobian determinant, one obtains:

[∏ i = 1 K − 1 ( x ¯ x i) α i − 1] [x ¯ ( 1 − ∑ i = 1 K − 1 x i)] α K − 1 ∏ i = 1 K Γ ( α i) x ¯ K − 1 e − x ¯ = Γ ( α ¯) [∏ i = 1 K − 1 ( x i) α i − 1] [1 − ∑ i = 1 K − 1 x i] α K − 1 ∏ i = 1 K Γ ( α i) × x ¯ α ¯ − 1 e − x ¯ Γ ( α ¯) {\displaystyle {\begin{aligned}&{\frac {\left[\prod _{i=1}^{K-1}({\bar {x}}x_{i})^{\alpha _{i}-1}\right]\left[{\bar {x}}(1-\sum _{i=1}^{K-1}x_{i})\right]^{\alpha _{K}-1}}{\prod _{i=1}^{K}\Gamma (\alpha _{i})}}{\bar {x}}^{K-1}e^{-{\bar {x}}}\\=&{\frac {\Gamma ({\bar {\alpha }})\left[\prod _{i=1}^{K-1}(x_{i})^{\alpha _{i}-1}\right]\left[1-\sum _{i=1}^{K-1}x_{i}\right]^{\alpha _{K}-1}}{\prod _{i=1}^{K}\Gamma (\alpha _{i})}}\times {\frac {{\bar {x}}^{{\bar {\alpha }}-1}e^{-{\bar {x}}}}{\Gamma ({\bar {\alpha }})}}\end{aligned}}}[image: {\displaystyle {\begin{aligned}&{\frac {\left[\prod _{i=1}^{K-1}({\bar {x}}x_{i})^{\alpha _{i}-1}\right]\left[{\bar {x}}(1-\sum _{i=1}^{K-1}x_{i})\right]^{\alpha _{K}-1}}{\prod _{i=1}^{K}\Gamma (\alpha _{i})}}{\bar {x}}^{K-1}e^{-{\bar {x}}}\\=&{\frac {\Gamma ({\bar {\alpha }})\left[\prod _{i=1}^{K-1}(x_{i})^{\alpha _{i}-1}\right]\left[1-\sum _{i=1}^{K-1}x_{i}\right]^{\alpha _{K}-1}}{\prod _{i=1}^{K}\Gamma (\alpha _{i})}}\times {\frac {{\bar {x}}^{{\bar {\alpha }}-1}e^{-{\bar {x}}}}{\Gamma ({\bar {\alpha }})}}\end{aligned}}}] where α ¯ = ∑ i = 1 K α i {\displaystyle {\bar {\alpha }}=\textstyle \sum _{i=1}^{K}\alpha _{i}}[image: {\displaystyle {\bar {\alpha }}=\textstyle \sum _{i=1}^{K}\alpha _{i}}]. The right-hand side can be recognized as the product of a Dirichlet pdf for the x i {\displaystyle x_{i}}[image: {\displaystyle x_{i}}] and a gamma pdf for x ¯ {\displaystyle {\bar {x}}}[image: {\displaystyle {\bar {x}}}]. The product form shows the Dirichlet and gamma variables are independent, so the latter can be integrated out by simply omitting it, to obtain: x 1, x 2, …, x K − 1 ∼ ( 1 − ∑ i = 1 K − 1 x i) α K − 1 ∏ i = 1 K − 1 x i α i − 1 B ( α) {\displaystyle x_{1},x_{2},\ldots ,x_{K-1}\sim {\frac {(1-\sum _{i=1}^{K-1}x_{i})^{\alpha _{K}-1}\prod _{i=1}^{K-1}x_{i}^{\alpha _{i}-1}}{B({\boldsymbol {\alpha }})}}}[image: {\displaystyle x_{1},x_{2},\ldots ,x_{K-1}\sim {\frac {(1-\sum _{i=1}^{K-1}x_{i})^{\alpha _{K}-1}\prod _{i=1}^{K-1}x_{i}^{\alpha _{i}-1}}{B({\boldsymbol {\alpha }})}}}]

Which is equivalent to

∏ i = 1 K x i α i − 1 B ( α) {\displaystyle {\frac {\prod _{i=1}^{K}x_{i}^{\alpha _{i}-1}}{B({\boldsymbol {\alpha }})}}}[image: {\displaystyle {\frac {\prod _{i=1}^{K}x_{i}^{\alpha _{i}-1}}{B({\boldsymbol {\alpha }})}}}] with support ∑ i = 1 K x i = 1 {\displaystyle \sum _{i=1}^{K}x_{i}=1}[image: {\displaystyle \sum _{i=1}^{K}x_{i}=1}]

Below is example Python code to draw the sample:

```
params = [a1, a2, ..., ak]
sample = [random.gammavariate(a, 1) for a in params]
sample = [v / sum(sample) for v in sample]
```

This formulation is correct regardless of how the Gamma distributions are parameterized (shape/scale vs. shape/rate) because they are equivalent when scale and rate equal 1.0.

### From marginal beta distributions

[[edit][138]]

A less efficient algorithm [29] relies on the univariate marginal and conditional distributions being beta and proceeds as follows. Simulate x 1 {\displaystyle x_{1}}[image: {\displaystyle x_{1}}] from

Beta ( α 1, ∑ i = 2 K α i) {\displaystyle {\textrm {Beta}}\left(\alpha _{1},\sum _{i=2}^{K}\alpha _{i}\right)}[image: {\displaystyle {\textrm {Beta}}\left(\alpha _{1},\sum _{i=2}^{K}\alpha _{i}\right)}]

Then simulate x 2, …, x K − 1 {\displaystyle x_{2},\ldots ,x_{K-1}}[image: {\displaystyle x_{2},\ldots ,x_{K-1}}] in order, as follows. For j = 2, …, K − 1 {\displaystyle j=2,\ldots ,K-1}[image: {\displaystyle j=2,\ldots ,K-1}], simulate ϕ j {\displaystyle \phi _{j}}[image: {\displaystyle \phi _{j}}] from

Beta ( α j, ∑ i = j + 1 K α i), {\displaystyle {\textrm {Beta}}\left(\alpha _{j},\sum _{i=j+1}^{K}\alpha _{i}\right),}[image: {\displaystyle {\textrm {Beta}}\left(\alpha _{j},\sum _{i=j+1}^{K}\alpha _{i}\right),}]

and let

x j = ( 1 − ∑ i = 1 j − 1 x i) ϕ j. {\displaystyle x_{j}=\left(1-\sum _{i=1}^{j-1}x_{i}\right)\phi _{j}.}[image: {\displaystyle x_{j}=\left(1-\sum _{i=1}^{j-1}x_{i}\right)\phi _{j}.}]

Finally, set

x K = 1 − ∑ i = 1 K − 1 x i. {\displaystyle x_{K}=1-\sum _{i=1}^{K-1}x_{i}.}[image: {\displaystyle x_{K}=1-\sum _{i=1}^{K-1}x_{i}.}]

This iterative procedure corresponds closely to the "string cutting" intuition described above.

Below is example Python code to draw the sample:

```
params = [a1, a2, ..., ak]
xs = [random.betavariate(params[0], sum(params[1:]))]
for j in range(1, len(params) - 1):
    phi = random.betavariate(params[j], sum(params[j + 1 :]))
    xs.append((1 - sum(xs)) * phi)
xs.append(1 - sum(xs))
```

### When each alpha is 1

[[edit][139]]

When *α*1 = ... = *α**K*= 1, a sample from the distribution can be found by randomly drawing a set of *K*− 1 values independently and uniformly from the interval [0, 1], adding the values 0 and 1 to the set to make it have *K*+ 1 values, sorting the set, and computing the difference between each pair of order-adjacent values, to give *x*1, ..., *x**K*.

### When each alpha is 1/2 and relationship to the hypersphere

[[edit][140]]

When *α*1 = ... = *α**K*= 1/2, a sample from the distribution can be found by randomly drawing K values independently from the standard normal distribution, squaring these values, and normalizing them by dividing by their sum, to give *x*1, ..., *x**K*.

A point (*x*1, ..., *x**K*) can be drawn uniformly at random from the (*K*−1)-dimensional unit hypersphere (which is the surface of a K -dimensional [hyperball][46]) via a similar procedure. Randomly draw K values independently from the standard normal distribution and normalize these coordinate values by dividing each by the constant that is the square root of the sum of their squares.

## See also

[[edit][141]]

- [Generalized Dirichlet distribution][87]
- [Grouped Dirichlet distribution][142]
- [Inverted Dirichlet distribution][143]
- [Latent Dirichlet allocation][144]
- [Dirichlet process][28]
- [Matrix variate Dirichlet distribution][145]

## References

[[edit][146]]

1. ↑ S. Kotz; N. Balakrishnan; N. L. Johnson (2000). *Continuous Multivariate Distributions. Volume 1: Models and Applications*. New York: Wiley. [ISBN][147] [978-0-471-18387-7][148]. (Chapter 49: Dirichlet and Inverted Dirichlet Distributions)
2. ↑ Olkin, Ingram; [Rubin, Herman][149] (1964). ["Multivariate Beta Distributions and Independence Properties of the Wishart Distribution"][150]. *The Annals of Mathematical Statistics*. **35**(1): 261– 269. [doi][151]: [10.1214/aoms/1177703748][150]. [JSTOR][152] [2238036][153].
3. 1 2 Bela A. Frigyik; Amol Kapila; Maya R. Gupta (2010). ["Introduction to the Dirichlet Distribution and Related Processes"][154] (PDF). University of Washington Department of Electrical Engineering. Archived from [the original][155] (Technical Report UWEETR-2010-006) on 2015-02-19.
4. ↑ A. Jøsang, J.H. Cho, and F. Chen. Noninformative Prior Weights for Dirichlet PDFs. *Proceedings of the 2022 IEEE International Conference on Multisensor Fusion and Integration (MFI 2022)*, Cranfield, UK, September 2022. [PDF][156]
5. ↑ Eq. (49.9) on page 488 of [Kotz, Balakrishnan & Johnson (2000). Continuous Multivariate Distributions. Volume 1: Models and Applications. New York: Wiley.][157]
6. ↑ BalakrishV. B. (2005). [" "Chapter 27. Dirichlet Distribution" "][158]. *A Primer on Statistical Distributions*. Hoboken, NJ: John Wiley & Sons, Inc. p. [274][158]. [ISBN][147] [978-0-471-42798-8][159].
7. ↑ Dello Schiavo, Lorenzo (2019). ["Characteristic functionals of Dirichlet measures"][160]. *Electron. J. Probab*. **24**: 1– 38. [arXiv][161]: [1810.09790][162]. [doi][151]: [10.1214/19-EJP371][160].
8. ↑ Dello Schiavo, Lorenzo; Quattrocchi, Filippo (2023). "Multivariate Dirichlet Moments and a Polychromatic Ewens Sampling Formula". [arXiv][161]: [2309.11292][163] [[math.PR][164]].
9. ↑ Hoffmann, Till. ["Moments of the Dirichlet distribution"][165]. Archived from [the original][166] on 2016-02-14. Retrieved 14 February 2016.
10. ↑ Christopher M. Bishop (17 August 2006). **[Pattern Recognition and Machine Learning][167]. Springer. [ISBN][147] [978-0-387-31073-2][168].
11. ↑ Farrow, Malcolm. ["MAS3301 Bayesian Statistics"][169] (PDF). *Newcastle University*. Retrieved 10 April 2013.
12. ↑ Lin, Jiayu (2016). **[On The Dirichlet Distribution][170] (PDF). Kingston, Canada: Queen's University. pp. § 2.4.9.
13. ↑ Nguyen, Duy (15 August 2023). ["AN IN DEPTH INTRODUCTION TO VARIATIONAL BAYES NOTE"][171]. [SSRN][172] [4541076][171]. Retrieved 15 August 2023.
14. ↑ Song, Kai-Sheng (2001). "Rényi information, loglikelihood, and an intrinsic distribution measure". *Journal of Statistical Planning and Inference*. **93**(325). Elsevier: 51– 69. [doi][151]: [10.1016/S0378-3758(00)00169-5][173].
15. ↑ Nemenman, Ilya; Shafee, Fariel; Bialek, William (2002). **[Entropy and Inference, revisited][174] (PDF). NIPS 14., eq. 8
16. ↑ Joram Soch (2020-05-10). ["Kullback–Leibler divergence for the Dirichlet distribution"][175]. *The Book of Statistical Proofs*. StatProofBook. Retrieved 2025-06-23.
17. ↑ Connor, Robert J.; Mosimann, James E (1969). "Concepts of Independence for Proportions with a Generalization of the Dirichlet Distribution". *Journal of the American Statistical Association*. **64**(325). American Statistical Association: 194– 206. [doi][151]: [10.2307/2283728][176]. [JSTOR][152] [2283728][177].
18. ↑ See Kotz, Balakrishnan & Johnson (2000), Section 8.5, "Connor and Mosimann's Generalization", pp. 519–521.
19. ↑ Phillips, P. C. B. (1988). ["The characteristic function of the Dirichlet and multivariate F distribution"][178] (PDF). *Cowles Foundation Discussion Paper 865*.
20. ↑ Grinshpan, A. Z. (2017). ["An inequality for multiple convolutions with respect to Dirichlet probability measure"][179]. *Advances in Applied Mathematics*. **82**(1): 102– 119. [doi][151]: [10.1016/j.aam.2016.08.001][179].
21. ↑ Perrault, P. (2024). "A New Bound on the Cumulant Generating Function of Dirichlet Processes". [arXiv][161]: [2409.18621][180] [[math.PR][164]]. Theorem 3.3
22. 1 2 Devroye, Luc (1986). **[Non-Uniform Random Variate Generation][181]. Springer-Verlag. [ISBN][147] [0-387-96305-7][182].
23. ↑ Lefkimmiatis, Stamatios; Maragos, Petros; Papandreou, George (2009). ["Bayesian Inference on Multiscale Models for Poisson Intensity Estimation: Applications to Photon-Limited Image Denoising"][183]. *IEEE Transactions on Image Processing*. **18**(8): 1724– 1741. [Bibcode][184]: [2009ITIP...18.1724L][185]. [doi][151]: [10.1109/TIP.2009.2022008][183]. [PMID][186] [19414285][187]. [S2CID][188] [859561][189].
24. ↑ Andreoli, Jean-Marc (2018). "A conjugate prior for the Dirichlet distribution". [arXiv][161]: [1811.05266][190] [[cs.LG][191]].
25. ↑ Graf, Monique (2019). ["The Simplicial Generalized Beta distribution - R-package SGB and applications"][192]. *Libra*. Retrieved 26 May 2025.`{{ [cite web][193] }}`: CS1 maint: numeric names: authors list ( [link][194])
26. ↑ Sorrenson, Peter; et al. (2024) (2023). "Learning Distributions on Manifolds with Free-Form Flows". [arXiv][161]: [2312.09852][195] [[cs.LG][191]].`{{ [cite arXiv][196] }}`: CS1 maint: numeric names: authors list ( [link][194])
27. ↑ Ferrer, Luciana; Ramos, Daniel (2025). ["Evaluating Posterior Probabilities: Decision Theory, Proper Scoring Rules, and Calibration"][197]. *Transactions on Machine Learning Research*.
28. ↑ Blackwell, David; MacQueen, James B. (1973). ["Ferguson distributions via Polya urn schemes"][198]. *Ann. Stat*. **1**(2): 353– 355. [doi][151]: [10.1214/aos/1176342372][198].
29. ↑ A. Gelman; J. B. Carlin; H. S. Stern; D. B. Rubin (2003). **[Bayesian Data Analysis][199] (2nd ed.). Chapman & Hall/CRC. pp. [582][200]. [ISBN][147] [1-58488-388-X][201].

## External links

[[edit][202]]

- ["Dirichlet distribution"][203], *[Encyclopedia of Mathematics][204]*, EMS Press, 2001 [1994]
- [Dirichlet Distribution][205]
- [How to estimate the parameters of the compound Dirichlet distribution (Pólya distribution) using expectation-maximization (EM)][206]
- Luc Devroye. ["Non-Uniform Random Variate Generation"][181]. Retrieved 19 October 2019.
- [Dirichlet Random Measures, Method of Construction via Compound Poisson Random Variables, and Exchangeability Properties of the resulting Gamma Distribution][207]
- [SciencesPo][208]: R package that contains functions for simulating parameters of the Dirichlet distribution.

- [v][209]
- [t][210]
- [e][211]

[Probability distributions][20] ( [list][212])

 |

Discrete
univariate |

with finite
support |

- [Benford][213]
- [Bernoulli][120]
- [Beta-binomial][214]
- [Binomial][121]
- [Categorical][26]
- [Hypergeometric][215]

  - [Negative][216]

- [Poisson binomial][217]
- [Rademacher][218]
- [Soliton][219]
- [Discrete uniform][220]
- [Zipf][221]
- [Zipf–Mandelbrot][222]

 |

with infinite
support |

- [Beta negative binomial][223]
- [Borel][224]
- [Conway–Maxwell–Poisson][225]
- [Discrete phase-type][226]
- [Delaporte][227]
- [Extended negative binomial][228]
- [Flory–Schulz][229]
- [Gauss–Kuzmin][230]
- [Geometric][231]
- [Logarithmic][232]
- [Mixed Poisson][233]
- [Negative binomial][234]
- [Panjer][235]
- [Parabolic fractal][236]
- [Poisson][237]
- [Skellam][238]
- [Yule–Simon][239]
- [Zeta][240]

 |

 |

Continuous
univariate |

supported on a
bounded interval |

- [Arcsine][241]
- [ARGUS][242]
- [Balding–Nichols][243]
- [Bates][244]
- [Beta][22]

  - [Generalized][245]

- [Beta rectangular][246]
- [Continuous Bernoulli][247]
- [Continuous binomial][248]
- [Irwin–Hall][249]
- [Kumaraswamy][250]
- [Logit-normal][251]
- [Noncentral beta][252]
- [PERT][253]
- [Power function][254]
- [Raised cosine][255]
- [Reciprocal][256]
- [Triangular][257]
- [U-quadratic][258]
- [Uniform][259]
- [Wigner semicircle][260]

 |

supported on a
semi-infinite
interval |

- [Benini][261]
- [Benktander 1st kind][262]
- [Benktander 2nd kind][263]
- [Beta prime][264]
- [Burr][265]
- [Chi][266]
- [Chi-squared][267]

  - [Noncentral][268]
  - [Inverse][269]

    - [Scaled][270]

- [Dagum][271]
- [Davis][272]
- [Erlang][273]

  - [Hyper][274]

- [Exponential][275]

  - [Hyperexponential][276]
  - [Hypoexponential][277]
  - [Logarithmic][278]

- **[F][279]

  - [Noncentral][280]

- [Folded normal][281]
- [Fréchet][282]
- [Gamma][96]

  - [Generalized][100]
  - [Inverse][283]

- [gamma/Gompertz][284]
- [Gompertz][285]

  - [Shifted][286]

- [Half-logistic][287]
- [Half-normal][288]
- **[Hotelling's T -squared][289]
- [Hartman–Watson][290]
- [Inverse Gaussian][291]

  - [Generalized][292]

- [Kolmogorov][293]
- [Lévy][294]
- [Log-Cauchy][295]
- [Log-Laplace][296]
- [Log-logistic][297]
- [Log-normal][298]
- [Log-t][299]
- [Lomax][300]
- [Matrix-exponential][301]
- [Maxwell–Boltzmann][302]
- [Maxwell–Jüttner][303]
- [Mittag-Leffler][304]
- [Nakagami][305]
- [Pareto][306]
- [Phase-type][307]
- [Poly-Weibull][308]
- [Rayleigh][309]
- [Relativistic Breit–Wigner][310]
- [Rice][311]
- [Truncated normal][312]
- [type-2 Gumbel][313]
- [Weibull][314]

  - [Discrete][315]

- [Wilks's lambda][316]

 |

supported
on the whole
real line |

- [Cauchy][317]
- [Exponential power][318]
- **[Fisher's z][319]
- [Kaniadakis κ-Gaussian][320]
- **[Gaussian q][321]
- [Generalized hyperbolic][322]
- [Generalized logistic (logistic-beta)][323]
- [Generalized normal][324]
- [Geometric stable][325]
- [Gumbel][326]
- [Holtsmark][327]
- [Hyperbolic secant][328]
- **[Johnson's S U][329]
- [Landau][330]
- [Laplace][331]

  - [Asymmetric][332]

- [Logistic][333]
- **[Noncentral t][334]
- [Normal (Gaussian)][335]
- [Normal-inverse Gaussian][336]
- [Skew normal][337]
- [Slash][338]
- [Stable][339]
- **[Student's t][340]
- [Tracy–Widom][341]
- [Variance-gamma][342]
- [Voigt][343]

 |

with support
whose type varies |

- [Generalized chi-squared][344]
- [Generalized extreme value][345]
- [Generalized Pareto][346]
- [Marchenko–Pastur][347]
- **[Kaniadakis κ -exponential][348]
- **[Kaniadakis κ -Gamma][349]
- **[Kaniadakis κ -Weibull][350]
- **[Kaniadakis κ -Logistic][351]
- **[Kaniadakis κ -Erlang][352]
- **[q -exponential][353]
- **[q -Gaussian][354]
- **[q -Weibull][355]
- [Shifted log-logistic][356]
- [Tukey lambda][357]

 |

 |

Mixed
univariate |

continuous-
discrete |

- [Rectified Gaussian][358]

 |

 |

[Multivariate (joint)][359] |

- *Discrete: *
- [Ewens][360]
- [Multinomial][27]

  - [Dirichlet][72]
  - [Negative][361]

- *Continuous: *
- [Dirichlet][362]

  - [Generalized][87]

- [Multivariate Laplace][363]
- [Multivariate normal][364]
- [Multivariate stable][365]
- **[Multivariate t][366]
- [Normal-gamma][367]

  - [Inverse][368]

- *[Matrix-valued:][369]*
- [LKJ][370]
- [Matrix beta][371]
- **[Matrix F][372]
- [Matrix normal][373]
- **[Matrix t][374]
- [Matrix gamma][375]

  - [Inverse][376]

- [Wishart][377]

  - [Normal][378]
  - [Inverse][379]
  - [Normal-inverse][380]
  - [Complex][381]

- [Uniform distribution on a Stiefel manifold][382]

 |

[Directional][383] |

*Univariate (circular) [directional][383]*[Circular uniform][384] [Univariate von Mises][385] [Wrapped normal][386] [Wrapped Cauchy][387] [Wrapped exponential][388] [Wrapped asymmetric Laplace][389] [Wrapped Lévy][390]*Bivariate (spherical)*[Kent][391]*Bivariate (toroidal)*[Bivariate von Mises][392]*Multivariate*[von Mises–Fisher][393] [Bingham][394]

 |

[Degenerate][395]
and [singular][396] |

*Degenerate*[Dirac delta function][397]*Singular*[Cantor][398]

 |

Families |

- [Circular][399]
- [Compound Poisson][400]
- [Elliptical][401]
- [Exponential][98]
- [Natural exponential][402]
- [Location–scale][403]
- [Maximum entropy][404]
- [Mixture][405]
- [Pearson][406]
- [Tweedie][407]
- [Wrapped][408]

 |

- [Category][409]
- [410] [Commons][411]

 |

- [v][412]
- [t][413]
- [e][414]

[Peter Gustav Lejeune Dirichlet][17]

 |

- [Dirichlet distribution][362]
- [Dirichlet character][415]
- [Dirichlet process][28]
- [Dirichlet-multinomial distribution][72]
- [Dirichlet series][416]
- [Dirichlet's theorem on arithmetic progressions][417]
- [Dirichlet convolution][418]
- [Dirichlet problem][419]
- [Dirichlet integral][420]

 |

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Dirichlet_distribution&oldid=1341278815][421] "

[Categories][422]:

- [Multivariate continuous distributions][423]
- [Conjugate prior distributions][424]
- [Exponential family distributions][425]
- [Continuous distributions][426]

Hidden categories:

- [Articles with short description][427]
- [Short description matches Wikidata][428]
- [CS1 maint: numeric names: authors list][429]

Search

Dirichlet distribution

16 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/File:Dirichlet.pdf
[2]: https://en.wikipedia.org/wiki/Statistical_parameter
[3]: https://en.wikipedia.org/wiki/Integer
[4]: https://en.wikipedia.org/wiki/Concentration_parameter
[5]: https://en.wikipedia.org/wiki/Support_(mathematics)
[6]: https://en.wikipedia.org/wiki/Simplex
[7]: https://en.wikipedia.org/wiki/Probability_density_function
[8]: https://en.wikipedia.org/wiki/Expected_value
[9]: https://en.wikipedia.org/wiki/Digamma_function
[10]: https://en.wikipedia.org/wiki/Mode_(statistics)
[11]: https://en.wikipedia.org/wiki/Variance
[12]: https://en.wikipedia.org/wiki/Kronecker_delta
[13]: https://en.wikipedia.org/wiki/Information_entropy
[14]: https://en.wikipedia.org/wiki/Method_of_moments_(statistics)
[15]: https://en.wikipedia.org/wiki/Probability
[16]: https://en.wikipedia.org/wiki/Statistics
[17]: https://en.wikipedia.org/wiki/Peter_Gustav_Lejeune_Dirichlet
[18]: https://en.wikipedia.org/wiki/Continuous_probability_distribution
[19]: https://en.wikipedia.org/wiki/Multivariate_random_variable
[20]: https://en.wikipedia.org/wiki/Probability_distribution
[21]: https://en.wikipedia.org/wiki/Real_number
[22]: https://en.wikipedia.org/wiki/Beta_distribution
[23]: https://en.wikipedia.org/wiki/Prior_distribution
[24]: https://en.wikipedia.org/wiki/Bayesian_statistics
[25]: https://en.wikipedia.org/wiki/Conjugate_prior
[26]: https://en.wikipedia.org/wiki/Categorical_distribution
[27]: https://en.wikipedia.org/wiki/Multinomial_distribution
[28]: https://en.wikipedia.org/wiki/Dirichlet_process
[29]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=1
[30]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=2
[31]: https://en.wikipedia.org/wiki/File:LogDirichletDensity-alpha_0.3_to_alpha_2.0.gif
[32]: https://en.wikipedia.org/wiki/Euclidean_space
[33]: https://en.wikipedia.org/wiki/Normalizing_constant
[34]: https://en.wikipedia.org/wiki/Beta_function
[35]: https://en.wikipedia.org/wiki/Gamma_function
[36]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=3
[37]: https://en.wikipedia.org/wiki/Discrete_distribution
[38]: https://en.wikipedia.org/wiki/Open_set
[39]: https://en.wikipedia.org/wiki/Standard_simplex
[40]: https://en.wikipedia.org/wiki/Triangle
[41]: https://en.wikipedia.org/wiki/Equilateral_triangle
[42]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=4
[43]: https://en.wikipedia.org/wiki/Dirichlet_distribution#endnote_concentration-parameter-disambiguation
[44]: https://en.wikipedia.org/wiki/Random_variate
[45]: https://en.wikipedia.org/wiki/Unit_hypersphere
[46]: https://en.wikipedia.org/wiki/Ball_(mathematics)
[47]: https://en.wikipedia.org/wiki/Jeffreys_prior
[48]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=5
[49]: https://en.wikipedia.org/wiki/Scalar_(mathematics)
[50]: https://en.wikipedia.org/wiki/File:Plot-noninformative-prior-weight.jpg
[51]: https://en.wikipedia.org/wiki/Subjective_logic
[52]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=6
[53]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=7
[54]: https://en.wikipedia.org/wiki/Invertible_matrix
[55]: https://en.wikipedia.org/wiki/Hadamard_product_(matrices)#Analogous_operations
[56]: https://en.wikipedia.org/wiki/Cycle_index#Symmetric_group_Sn
[57]: https://en.wikipedia.org/wiki/Symmetric_group
[58]: https://en.wikipedia.org/wiki/Pólya_enumeration_theorem
[59]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=8
[60]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=9
[61]: https://en.wikipedia.org/wiki/Marginal_distribution
[62]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=10
[63]: https://en.wikipedia.org/wiki/Discrete_probability_distribution
[64]: https://en.wikipedia.org/wiki/Posterior_distribution
[65]: https://en.wikipedia.org/wiki/Hyperprior
[66]: https://en.wikipedia.org/wiki/Pseudocount
[67]: https://en.wikipedia.org/wiki/Mixture_model
[68]: https://en.wikipedia.org/wiki/Hierarchical_Bayesian_model
[69]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=11
[70]: https://en.wikipedia.org/wiki/Joint_distribution
[71]: https://en.wikipedia.org/wiki/Marginalized_out
[72]: https://en.wikipedia.org/wiki/Dirichlet-multinomial_distribution
[73]: https://en.wikipedia.org/wiki/Statistical_inference
[74]: https://en.wikipedia.org/wiki/Gibbs_sampling
[75]: https://en.wikipedia.org/wiki/Variational_Bayes
[76]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=12
[77]: https://en.wikipedia.org/wiki/Differential_entropy
[78]: https://en.wikipedia.org/wiki/Nat_(unit)
[79]: https://en.wikipedia.org/wiki/Exponential_family#Moments_and_cumulants_of_the_sufficient_statistic
[80]: https://en.wikipedia.org/wiki/Trigamma_function
[81]: https://en.wikipedia.org/wiki/Rényi_entropy
[82]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=13
[83]: https://en.wikipedia.org/wiki/KL_divergence
[84]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=14
[85]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=15
[86]: https://en.wikipedia.org/wiki/Neutral_vector
[87]: https://en.wikipedia.org/wiki/Generalized_Dirichlet_distribution
[88]: https://en.wikipedia.org/wiki/Independence_(probability_theory)#More_than_two_random_variables
[89]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=16
[90]: https://en.wikipedia.org/wiki/Confluent_hypergeometric_function
[91]: https://en.wikipedia.org/wiki/Lauricella_hypergeometric_series
[92]: https://en.wikipedia.org/wiki/Peter_C._B._Phillips
[93]: https://en.wikipedia.org/wiki/Methods_of_contour_integration
[94]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=17
[95]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=18
[96]: https://en.wikipedia.org/wiki/Gamma_distribution
[97]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=19
[98]: https://en.wikipedia.org/wiki/Exponential_family
[99]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=20
[100]: https://en.wikipedia.org/wiki/Generalized_gamma_distribution
[101]: https://en.wikipedia.org/wiki/Softmax_function
[102]: https://en.wikipedia.org/wiki/Bijection
[103]: https://en.wikipedia.org/wiki/Flow-based_generative_model#Differential_volume_ratio
[104]: https://en.wikipedia.org/wiki/Change_of_variables
[105]: https://en.wikipedia.org/wiki/Normalizing_flow
[106]: https://en.wikipedia.org/wiki/Jacobian_determinant
[107]: https://en.wikipedia.org/wiki/Flow-based_generative_model#Simplex_flow
[108]: https://en.wikipedia.org/wiki/Logistic-beta_distribution
[109]: https://en.wikipedia.org/wiki/Generalized_logistic_distribution#Tail_behaviour
[110]: https://en.wikipedia.org/wiki/Generalized_logistic_distribution#Generalization_with_location_and_scale_parameters
[111]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=21
[112]: https://en.wikipedia.org/wiki/Platt_scaling#Analysis
[113]: https://en.wikipedia.org/wiki/Machine_learning
[114]: https://en.wikipedia.org/wiki/Discriminative_model
[115]: https://en.wikipedia.org/wiki/Cross-entropy
[116]: https://en.wikipedia.org/wiki/Generative_model
[117]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=22
[118]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=23
[119]: https://en.wikipedia.org/wiki/Natural_language_processing
[120]: https://en.wikipedia.org/wiki/Bernoulli_distribution
[121]: https://en.wikipedia.org/wiki/Binomial_distribution
[122]: https://en.wikipedia.org/wiki/Random_variable
[123]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=24
[124]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=25
[125]: https://en.wikipedia.org/wiki/Bayesian_inference
[126]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=26
[127]: https://en.wikipedia.org/wiki/File:Dirichlet_example.png
[128]: https://en.wikipedia.org/wiki/Pólya_urn_model
[129]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=27
[130]: https://en.wikipedia.org/wiki/Martingale_(probability_theory)
[131]: https://en.wikipedia.org/wiki/Martingale_convergence_theorem
[132]: https://en.wikipedia.org/wiki/Almost_sure_convergence
[133]: https://en.wikipedia.org/wiki/Convergence_in_mean
[134]: https://en.wikipedia.org/wiki/Moment_(mathematics)
[135]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=28
[136]: https://en.wikipedia.org/wiki/Non-uniform_random_variate_generation
[137]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=29
[138]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=30
[139]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=31
[140]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=32
[141]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=33
[142]: https://en.wikipedia.org/wiki/Grouped_Dirichlet_distribution
[143]: https://en.wikipedia.org/wiki/Inverted_Dirichlet_distribution
[144]: https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation
[145]: https://en.wikipedia.org/wiki/Matrix_variate_Dirichlet_distribution
[146]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=34
[147]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[148]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-471-18387-7
[149]: https://en.wikipedia.org/wiki/Herman_Rubin
[150]: https://doi.org/10.1214%2Faoms%2F1177703748
[151]: https://en.wikipedia.org/wiki/Doi_(identifier)
[152]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[153]: https://www.jstor.org/stable/2238036
[154]: https://web.archive.org/web/20150219021331/https://www.ee.washington.edu/techsite/papers/documents/UWEETR-2010-0006.pdf
[155]: https://www.ee.washington.edu/techsite/papers/documents/UWEETR-2010-0006.pdf
[156]: https://www.mn.uio.no/ifi/english/people/aca/josang/publications/jcc2022-mfi.pdf
[157]: http://www.wiley.com/WileyCDA/WileyTitle/productCd-0471183873.html
[158]: https://archive.org/details/primeronstatisti0000bala/page/274
[159]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-471-42798-8
[160]: https://doi.org/10.1214%2F19-EJP371
[161]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[162]: https://arxiv.org/abs/1810.09790
[163]: https://arxiv.org/abs/2309.11292
[164]: https://arxiv.org/archive/math.PR
[165]: https://web.archive.org/web/20160214015422/https://tillahoffmann.github.io/Moments-of-the-Dirichlet-distribution/
[166]: https://tillahoffmann.github.io/Moments-of-the-Dirichlet-distribution/
[167]: https://books.google.com/books?id=kTNoQgAACAAJ
[168]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-31073-2
[169]: http://www.mas.ncl.ac.uk/~nmf16/teaching/mas3301/week6.pdf
[170]: https://mast.queensu.ca/~communications/Papers/msc-jiayu-lin.pdf
[171]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4541076
[172]: https://en.wikipedia.org/wiki/SSRN_(identifier)
[173]: https://doi.org/10.1016%2FS0378-3758%2800%2900169-5
[174]: http://papers.nips.cc/paper/1965-entropy-and-inference-revisited.pdf
[175]: https://statproofbook.github.io/P/dir-kl.html
[176]: https://doi.org/10.2307%2F2283728
[177]: https://www.jstor.org/stable/2283728
[178]: https://cowles.yale.edu/sites/default/files/files/pub/d08/d0865.pdf
[179]: https://doi.org/10.1016%2Fj.aam.2016.08.001
[180]: https://arxiv.org/abs/2409.18621
[181]: http://luc.devroye.org/rnbookindex.html
[182]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-96305-7
[183]: https://doi.org/10.1109%2FTIP.2009.2022008
[184]: https://en.wikipedia.org/wiki/Bibcode_(identifier)
[185]: https://ui.adsabs.harvard.edu/abs/2009ITIP...18.1724L
[186]: https://en.wikipedia.org/wiki/PMID_(identifier)
[187]: https://pubmed.ncbi.nlm.nih.gov/19414285
[188]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[189]: https://api.semanticscholar.org/CorpusID:859561
[190]: https://arxiv.org/abs/1811.05266
[191]: https://arxiv.org/archive/cs.LG
[192]: https://libra.unine.ch/server/api/core/bitstreams/dd593778-b1fd-4856-855b-7b21e005ee77/content
[193]: https://en.wikipedia.org/wiki/Template:Cite_web
[194]: https://en.wikipedia.org/wiki/Category:CS1_maint:_numeric_names:_authors_list
[195]: https://arxiv.org/abs/2312.09852
[196]: https://en.wikipedia.org/wiki/Template:Cite_arXiv
[197]: https://openreview.net/forum?id=qbrE0LR7fF
[198]: https://doi.org/10.1214%2Faos%2F1176342372
[199]: https://archive.org/details/bayesiandataanal00gelm
[200]: https://archive.org/details/bayesiandataanal00gelm/page/n607
[201]: https://en.wikipedia.org/wiki/Special:BookSources/1-58488-388-X
[202]: /w/index.php?title=Dirichlet_distribution&amp;action=edit&amp;section=35
[203]: https://www.encyclopediaofmath.org/index.php?title=Dirichlet_distribution
[204]: https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics
[205]: http://users.ics.aalto.fi/ahonkela/dippa/node95.html
[206]: http://mayagupta.org/publications/EMbookGuptaChen2010.pdf
[207]: http://www.cs.princeton.edu/courses/archive/fall07/cos597C/scribe/20071130.pdf
[208]: https://cran.r-project.org/web/packages/SciencesPo/index.html
[209]: https://en.wikipedia.org/wiki/Template:Probability_distributions
[210]: https://en.wikipedia.org/wiki/Template_talk:Probability_distributions
[211]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Probability_distributions
[212]: https://en.wikipedia.org/wiki/List_of_probability_distributions
[213]: https://en.wikipedia.org/wiki/Benford's_law
[214]: https://en.wikipedia.org/wiki/Beta-binomial_distribution
[215]: https://en.wikipedia.org/wiki/Hypergeometric_distribution
[216]: https://en.wikipedia.org/wiki/Negative_hypergeometric_distribution
[217]: https://en.wikipedia.org/wiki/Poisson_binomial_distribution
[218]: https://en.wikipedia.org/wiki/Rademacher_distribution
[219]: https://en.wikipedia.org/wiki/Soliton_distribution
[220]: https://en.wikipedia.org/wiki/Discrete_uniform_distribution
[221]: https://en.wikipedia.org/wiki/Zipf's_law
[222]: https://en.wikipedia.org/wiki/Zipf–Mandelbrot_law
[223]: https://en.wikipedia.org/wiki/Beta_negative_binomial_distribution
[224]: https://en.wikipedia.org/wiki/Borel_distribution
[225]: https://en.wikipedia.org/wiki/Conway–Maxwell–Poisson_distribution
[226]: https://en.wikipedia.org/wiki/Discrete_phase-type_distribution
[227]: https://en.wikipedia.org/wiki/Delaporte_distribution
[228]: https://en.wikipedia.org/wiki/Extended_negative_binomial_distribution
[229]: https://en.wikipedia.org/wiki/Flory–Schulz_distribution
[230]: https://en.wikipedia.org/wiki/Gauss–Kuzmin_distribution
[231]: https://en.wikipedia.org/wiki/Geometric_distribution
[232]: https://en.wikipedia.org/wiki/Logarithmic_distribution
[233]: https://en.wikipedia.org/wiki/Mixed_Poisson_distribution
[234]: https://en.wikipedia.org/wiki/Negative_binomial_distribution
[235]: https://en.wikipedia.org/wiki/(a,b,0)_class_of_distributions
[236]: https://en.wikipedia.org/wiki/Parabolic_fractal_distribution
[237]: https://en.wikipedia.org/wiki/Poisson_distribution
[238]: https://en.wikipedia.org/wiki/Skellam_distribution
[239]: https://en.wikipedia.org/wiki/Yule–Simon_distribution
[240]: https://en.wikipedia.org/wiki/Zeta_distribution
[241]: https://en.wikipedia.org/wiki/Arcsine_distribution
[242]: https://en.wikipedia.org/wiki/ARGUS_distribution
[243]: https://en.wikipedia.org/wiki/Balding–Nichols_model
[244]: https://en.wikipedia.org/wiki/Bates_distribution
[245]: https://en.wikipedia.org/wiki/Generalized_beta_distribution
[246]: https://en.wikipedia.org/wiki/Beta_rectangular_distribution
[247]: https://en.wikipedia.org/wiki/Continuous_Bernoulli_distribution
[248]: https://en.wikipedia.org/wiki/Continuous_binomial_distribution
[249]: https://en.wikipedia.org/wiki/Irwin–Hall_distribution
[250]: https://en.wikipedia.org/wiki/Kumaraswamy_distribution
[251]: https://en.wikipedia.org/wiki/Logit-normal_distribution
[252]: https://en.wikipedia.org/wiki/Noncentral_beta_distribution
[253]: https://en.wikipedia.org/wiki/PERT_distribution
[254]: https://en.wikipedia.org/wiki/Power_function_distribution?action=edit&amp;redlink=1
[255]: https://en.wikipedia.org/wiki/Raised_cosine_distribution
[256]: https://en.wikipedia.org/wiki/Reciprocal_distribution
[257]: https://en.wikipedia.org/wiki/Triangular_distribution
[258]: https://en.wikipedia.org/wiki/U-quadratic_distribution
[259]: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
[260]: https://en.wikipedia.org/wiki/Wigner_semicircle_distribution
[261]: https://en.wikipedia.org/wiki/Benini_distribution
[262]: https://en.wikipedia.org/wiki/Benktander_type_I_distribution
[263]: https://en.wikipedia.org/wiki/Benktander_type_II_distribution
[264]: https://en.wikipedia.org/wiki/Beta_prime_distribution
[265]: https://en.wikipedia.org/wiki/Burr_distribution
[266]: https://en.wikipedia.org/wiki/Chi_distribution
[267]: https://en.wikipedia.org/wiki/Chi-squared_distribution
[268]: https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution
[269]: https://en.wikipedia.org/wiki/Inverse-chi-squared_distribution
[270]: https://en.wikipedia.org/wiki/Scaled_inverse_chi-squared_distribution
[271]: https://en.wikipedia.org/wiki/Dagum_distribution
[272]: https://en.wikipedia.org/wiki/Davis_distribution
[273]: https://en.wikipedia.org/wiki/Erlang_distribution
[274]: https://en.wikipedia.org/wiki/Hyper-Erlang_distribution
[275]: https://en.wikipedia.org/wiki/Exponential_distribution
[276]: https://en.wikipedia.org/wiki/Hyperexponential_distribution
[277]: https://en.wikipedia.org/wiki/Hypoexponential_distribution
[278]: https://en.wikipedia.org/wiki/Exponential-logarithmic_distribution
[279]: https://en.wikipedia.org/wiki/F-distribution
[280]: https://en.wikipedia.org/wiki/Noncentral_F-distribution
[281]: https://en.wikipedia.org/wiki/Folded_normal_distribution
[282]: https://en.wikipedia.org/wiki/Fréchet_distribution
[283]: https://en.wikipedia.org/wiki/Inverse-gamma_distribution
[284]: https://en.wikipedia.org/wiki/Gamma/Gompertz_distribution
[285]: https://en.wikipedia.org/wiki/Gompertz_distribution
[286]: https://en.wikipedia.org/wiki/Shifted_Gompertz_distribution
[287]: https://en.wikipedia.org/wiki/Half-logistic_distribution
[288]: https://en.wikipedia.org/wiki/Half-normal_distribution
[289]: https://en.wikipedia.org/wiki/Hotelling's_T-squared_distribution
[290]: https://en.wikipedia.org/wiki/Hartman–Watson_distribution
[291]: https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution
[292]: https://en.wikipedia.org/wiki/Generalized_inverse_Gaussian_distribution
[293]: https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test
[294]: https://en.wikipedia.org/wiki/Lévy_distribution
[295]: https://en.wikipedia.org/wiki/Log-Cauchy_distribution
[296]: https://en.wikipedia.org/wiki/Log-Laplace_distribution
[297]: https://en.wikipedia.org/wiki/Log-logistic_distribution
[298]: https://en.wikipedia.org/wiki/Log-normal_distribution
[299]: https://en.wikipedia.org/wiki/Log-t_distribution
[300]: https://en.wikipedia.org/wiki/Lomax_distribution
[301]: https://en.wikipedia.org/wiki/Matrix-exponential_distribution
[302]: https://en.wikipedia.org/wiki/Maxwell–Boltzmann_distribution
[303]: https://en.wikipedia.org/wiki/Maxwell–Jüttner_distribution
[304]: https://en.wikipedia.org/wiki/Mittag-Leffler_distribution
[305]: https://en.wikipedia.org/wiki/Nakagami_distribution
[306]: https://en.wikipedia.org/wiki/Pareto_distribution
[307]: https://en.wikipedia.org/wiki/Phase-type_distribution
[308]: https://en.wikipedia.org/wiki/Poly-Weibull_distribution
[309]: https://en.wikipedia.org/wiki/Rayleigh_distribution
[310]: https://en.wikipedia.org/wiki/Relativistic_Breit–Wigner_distribution
[311]: https://en.wikipedia.org/wiki/Rice_distribution
[312]: https://en.wikipedia.org/wiki/Truncated_normal_distribution
[313]: https://en.wikipedia.org/wiki/Type-2_Gumbel_distribution
[314]: https://en.wikipedia.org/wiki/Weibull_distribution
[315]: https://en.wikipedia.org/wiki/Discrete_Weibull_distribution
[316]: https://en.wikipedia.org/wiki/Wilks's_lambda_distribution
[317]: https://en.wikipedia.org/wiki/Cauchy_distribution
[318]: https://en.wikipedia.org/wiki/Generalized_normal_distribution#Version_1
[319]: https://en.wikipedia.org/wiki/Fisher's_z-distribution
[320]: https://en.wikipedia.org/wiki/Kaniadakis_Gaussian_distribution
[321]: https://en.wikipedia.org/wiki/Gaussian_q-distribution
[322]: https://en.wikipedia.org/wiki/Generalised_hyperbolic_distribution
[323]: https://en.wikipedia.org/wiki/Generalized_logistic_distribution
[324]: https://en.wikipedia.org/wiki/Generalized_normal_distribution
[325]: https://en.wikipedia.org/wiki/Geometric_stable_distribution
[326]: https://en.wikipedia.org/wiki/Gumbel_distribution
[327]: https://en.wikipedia.org/wiki/Holtsmark_distribution
[328]: https://en.wikipedia.org/wiki/Hyperbolic_secant_distribution
[329]: https://en.wikipedia.org/wiki/Johnson's_SU-distribution
[330]: https://en.wikipedia.org/wiki/Landau_distribution
[331]: https://en.wikipedia.org/wiki/Laplace_distribution
[332]: https://en.wikipedia.org/wiki/Asymmetric_Laplace_distribution
[333]: https://en.wikipedia.org/wiki/Logistic_distribution
[334]: https://en.wikipedia.org/wiki/Noncentral_t-distribution
[335]: https://en.wikipedia.org/wiki/Normal_distribution
[336]: https://en.wikipedia.org/wiki/Normal-inverse_Gaussian_distribution
[337]: https://en.wikipedia.org/wiki/Skew_normal_distribution
[338]: https://en.wikipedia.org/wiki/Slash_distribution
[339]: https://en.wikipedia.org/wiki/Stable_distribution
[340]: https://en.wikipedia.org/wiki/Student's_t-distribution
[341]: https://en.wikipedia.org/wiki/Tracy–Widom_distribution
[342]: https://en.wikipedia.org/wiki/Variance-gamma_distribution
[343]: https://en.wikipedia.org/wiki/Voigt_profile
[344]: https://en.wikipedia.org/wiki/Generalized_chi-squared_distribution
[345]: https://en.wikipedia.org/wiki/Generalized_extreme_value_distribution
[346]: https://en.wikipedia.org/wiki/Generalized_Pareto_distribution
[347]: https://en.wikipedia.org/wiki/Marchenko–Pastur_distribution
[348]: https://en.wikipedia.org/wiki/Kaniadakis_Exponential_distribution
[349]: https://en.wikipedia.org/wiki/Kaniadakis_Gamma_distribution
[350]: https://en.wikipedia.org/wiki/Kaniadakis_Weibull_distribution
[351]: https://en.wikipedia.org/wiki/Kaniadakis_Logistic_distribution
[352]: https://en.wikipedia.org/wiki/Kaniadakis_Erlang_distribution
[353]: https://en.wikipedia.org/wiki/Q-exponential_distribution
[354]: https://en.wikipedia.org/wiki/Q-Gaussian_distribution
[355]: https://en.wikipedia.org/wiki/Q-Weibull_distribution
[356]: https://en.wikipedia.org/wiki/Shifted_log-logistic_distribution
[357]: https://en.wikipedia.org/wiki/Tukey_lambda_distribution
[358]: https://en.wikipedia.org/wiki/Rectified_Gaussian_distribution
[359]: https://en.wikipedia.org/wiki/Joint_probability_distribution
[360]: https://en.wikipedia.org/wiki/Ewens's_sampling_formula
[361]: https://en.wikipedia.org/wiki/Negative_multinomial_distribution
[362]: https://en.wikipedia.org/wiki/Dirichlet_distribution
[363]: https://en.wikipedia.org/wiki/Multivariate_Laplace_distribution
[364]: https://en.wikipedia.org/wiki/Multivariate_normal_distribution
[365]: https://en.wikipedia.org/wiki/Multivariate_stable_distribution
[366]: https://en.wikipedia.org/wiki/Multivariate_t-distribution
[367]: https://en.wikipedia.org/wiki/Normal-gamma_distribution
[368]: https://en.wikipedia.org/wiki/Normal-inverse-gamma_distribution
[369]: https://en.wikipedia.org/wiki/Random_matrix
[370]: https://en.wikipedia.org/wiki/Lewandowski-Kurowicka-Joe_distribution
[371]: https://en.wikipedia.org/wiki/Matrix_variate_beta_distribution
[372]: https://en.wikipedia.org/wiki/Matrix_F-distribution
[373]: https://en.wikipedia.org/wiki/Matrix_normal_distribution
[374]: https://en.wikipedia.org/wiki/Matrix_t-distribution
[375]: https://en.wikipedia.org/wiki/Matrix_gamma_distribution
[376]: https://en.wikipedia.org/wiki/Inverse_matrix_gamma_distribution
[377]: https://en.wikipedia.org/wiki/Wishart_distribution
[378]: https://en.wikipedia.org/wiki/Normal-Wishart_distribution
[379]: https://en.wikipedia.org/wiki/Inverse-Wishart_distribution
[380]: https://en.wikipedia.org/wiki/Normal-inverse-Wishart_distribution
[381]: https://en.wikipedia.org/wiki/Complex_Wishart_distribution
[382]: https://en.wikipedia.org/wiki/Uniform_distribution_on_a_Stiefel_manifold
[383]: https://en.wikipedia.org/wiki/Directional_statistics
[384]: https://en.wikipedia.org/wiki/Circular_uniform_distribution
[385]: https://en.wikipedia.org/wiki/Von_Mises_distribution
[386]: https://en.wikipedia.org/wiki/Wrapped_normal_distribution
[387]: https://en.wikipedia.org/wiki/Wrapped_Cauchy_distribution
[388]: https://en.wikipedia.org/wiki/Wrapped_exponential_distribution
[389]: https://en.wikipedia.org/wiki/Wrapped_asymmetric_Laplace_distribution
[390]: https://en.wikipedia.org/wiki/Wrapped_Lévy_distribution
[391]: https://en.wikipedia.org/wiki/Kent_distribution
[392]: https://en.wikipedia.org/wiki/Bivariate_von_Mises_distribution
[393]: https://en.wikipedia.org/wiki/Von_Mises–Fisher_distribution
[394]: https://en.wikipedia.org/wiki/Bingham_distribution
[395]: https://en.wikipedia.org/wiki/Degenerate_distribution
[396]: https://en.wikipedia.org/wiki/Singular_distribution
[397]: https://en.wikipedia.org/wiki/Dirac_delta_function
[398]: https://en.wikipedia.org/wiki/Cantor_distribution
[399]: https://en.wikipedia.org/wiki/Circular_distribution
[400]: https://en.wikipedia.org/wiki/Compound_Poisson_distribution
[401]: https://en.wikipedia.org/wiki/Elliptical_distribution
[402]: https://en.wikipedia.org/wiki/Natural_exponential_family
[403]: https://en.wikipedia.org/wiki/Location–scale_family
[404]: https://en.wikipedia.org/wiki/Maximum_entropy_probability_distribution
[405]: https://en.wikipedia.org/wiki/Mixture_distribution
[406]: https://en.wikipedia.org/wiki/Pearson_distribution
[407]: https://en.wikipedia.org/wiki/Tweedie_distribution
[408]: https://en.wikipedia.org/wiki/Wrapped_distribution
[409]: https://en.wikipedia.org/wiki/Category:Probability_distributions
[410]: https://en.wikipedia.org/wiki/File:Commons-logo.svg
[411]: https://commons.wikimedia.org/wiki/Category:Probability%20distributions
[412]: https://en.wikipedia.org/wiki/Template:Peter_Gustav_Lejeune_Dirichlet
[413]: https://en.wikipedia.org/wiki/Template_talk:Peter_Gustav_Lejeune_Dirichlet?action=edit&amp;redlink=1
[414]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Peter_Gustav_Lejeune_Dirichlet
[415]: https://en.wikipedia.org/wiki/Dirichlet_character
[416]: https://en.wikipedia.org/wiki/Dirichlet_series
[417]: https://en.wikipedia.org/wiki/Dirichlet's_theorem_on_arithmetic_progressions
[418]: https://en.wikipedia.org/wiki/Dirichlet_convolution
[419]: https://en.wikipedia.org/wiki/Dirichlet_problem
[420]: https://en.wikipedia.org/wiki/Dirichlet_integral
[421]: https://en.wikipedia.org/w/index.php?title=Dirichlet_distribution&amp;oldid=1341278815
[422]: /wiki/Help:Category
[423]: /wiki/Category:Multivariate_continuous_distributions
[424]: /wiki/Category:Conjugate_prior_distributions
[425]: /wiki/Category:Exponential_family_distributions
[426]: /wiki/Category:Continuous_distributions
[427]: /wiki/Category:Articles_with_short_description
[428]: /wiki/Category:Short_description_matches_Wikidata
[429]: /wiki/Category:CS1_maint:_numeric_names:_authors_list
