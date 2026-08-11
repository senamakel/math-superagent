> **Excerpt only — read this first.** The complete text is one level down at `research/L0/dirichlet_distribution_wikipedia.full.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

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

*[excerpt ends; 109127 characters not shown — see `research/L0/dirichlet_distribution_wikipedia.full.full.md`]*
