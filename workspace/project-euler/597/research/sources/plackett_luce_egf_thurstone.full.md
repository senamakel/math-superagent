<!-- source: https://en.wikipedia.org/wiki/Plackett%E2%80%93Luce_model | converted from HTML -->

Bradley–Terry model - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

(Redirected from [Plackett–Luce model][1])

Statistical model for pairwise comparisons

The **Bradley–Terry model**is a [probability model][2] for the outcome of pairwise comparisons between items, teams, or objects. Given a pair of items i and j drawn from some [population][3], it estimates the probability that the [pairwise comparison][4] ''j''"}},"i":0}}]}'>*i*> *j*turns out true, as

\\Pr(i > j) = \\frac{p_i}{p_i + p_j},</math>"},"3":{"wt":"{{EquationRef|1}}"}},"i":0}}]}'>

j) = \\frac{p_i}{p_i + p_j},"}}'> j)={\frac {p_{i}}{p_{i}+p_{j}}},}"> Pr ( i > j) = p i p i + p j, {\displaystyle \Pr(i>j)={\frac {p_{i}}{p_{i}+p_{j}}},} j)={\frac {p_{i}}{p_{i}+p_{j}}},}"/> |  | 1 |

where i</sub>"}},"i":0}}]}'>p i is a positive [real-valued][5] score assigned to individual i. The comparison ''j''"}},"i":0}}]}'>*i*> *j*can be read as " i is preferred to j ", " i ranks higher than j ", or " i beats j ", depending on the application.

For example, i</sub>"}},"i":0}}]}'>p i might represent the skill of a team in a sports tournament and j)"}}'> j)}"> Pr ( i > j) {\displaystyle \Pr(i>j)} j)}"/> the probability that i wins a game against j. [1] [2] Or i</sub>"}},"i":0}}]}'>p i might represent the quality or desirability of a commercial product and j)"}}'> j)}"> Pr ( i > j) {\displaystyle \Pr(i>j)} j)}"/> the probability that a consumer will prefer product i over product j.

The Bradley–Terry model can be used in the forward direction to predict outcomes, as described, but is more commonly used in reverse to infer the scores i</sub>"}},"i":0}}]}'>p i given an observed set of outcomes. [2] In this type of application i</sub>"}},"i":0}}]}'>p i represents some measure of the strength or quality of i {\displaystyle i}[image: {\displaystyle i}] and the model lets us estimate the strengths from a series of pairwise comparisons. In a survey of wine preferences, for instance, it might be difficult for respondents to give a complete ranking of a large set of wines, but relatively easy for them to compare sample pairs of wines and say which they feel is better. Based on a set of such pairwise comparisons, the Bradley–Terry model can then be used to derive a full ranking of the wines.

Once the values of the scores i</sub>"}},"i":0}}]}'>p i have been calculated, the model can then also be used in the forward direction, for instance to predict the likely outcome of comparisons that have not yet actually occurred. In the wine survey example, for instance, one could calculate the probability that someone will prefer wine i {\displaystyle i}[image: {\displaystyle i}] over wine j {\displaystyle j}[image: {\displaystyle j}], even if no one in the survey directly compared that particular pair.

## History and applications

[[edit][6]]

The model is named after [Ralph A. Bradley][7] and Milton E. Terry, [3] who presented it in 1952, [4] although it had already been studied by [Ernst Zermelo][8] in the 1920s. [1] [5] [6] Applications of the model include the ranking of competitors in sports, [chess][9], and other competitions, [7] the ranking of products in paired comparison surveys of [consumer choice][10], analysis of [dominance hierarchies][11] within animal and human communities, [8] ranking of [journals][12], ranking of AI models, [9] and is foundational to the field of training reward models in [reinforcement learning from human feedback][13]. [10] It also plays a role in the estimation of the relevance of documents in [machine-learned][14] [search engines][15]. [11]

## Definition

[[edit][16]]

The Bradley–Terry model can be parametrized in various ways. Equation (**1**) is perhaps the most common, but there are a number of others. Bradley and Terry themselves defined exponential score functions p i = e β i {\displaystyle p_{i}=e^{\beta _{i}}}[image: {\displaystyle p_{i}=e^{\beta _{i}}}], so that [2]

j) = \\frac{e^{\\beta_i}}{e^{\\beta_i} + e^{\\beta_j}} = \\frac{1}{1 + e^{\\beta_j-\\beta_i}}."}}'> j)={\frac {e^{\beta _{i}}}{e^{\beta _{i}}+e^{\beta _{j}}}}={\frac {1}{1+e^{\beta _{j}-\beta _{i}}}}.}"> Pr ( i > j) = e β i e β i + e β j = 1 1 + e β j − β i. {\displaystyle \Pr(i>j)={\frac {e^{\beta _{i}}}{e^{\beta _{i}}+e^{\beta _{j}}}}={\frac {1}{1+e^{\beta _{j}-\beta _{i}}}}.} j)={\frac {e^{\beta _{i}}}{e^{\beta _{i}}+e^{\beta _{j}}}}={\frac {1}{1+e^{\beta _{j}-\beta _{i}}}}.}"/>

Alternatively, one can use a [logit][17], such that [1]

j) = \\log \\frac{\\Pr(i > j)}{1 - \\Pr(i > j)} = \\log \\frac{\\Pr(i > j)}{\\Pr(j > i)} = \\beta_i - \\beta_j,"}}'> j)=\log {\frac {\Pr(i>j)}{1-\Pr(i>j)}}=\log {\frac {\Pr(i>j)}{\Pr(j>i)}}=\beta _{i}-\beta _{j},}"> logit ⁡ Pr ( i > j) = log ⁡ Pr ( i > j) 1 − Pr ( i > j) = log ⁡ Pr ( i > j) Pr ( j > i) = β i − β j, {\displaystyle \operatorname {logit} \Pr(i>j)=\log {\frac {\Pr(i>j)}{1-\Pr(i>j)}}=\log {\frac {\Pr(i>j)}{\Pr(j>i)}}=\beta _{i}-\beta _{j},} j)=\log {\frac {\Pr(i>j)}{1-\Pr(i>j)}}=\log {\frac {\Pr(i>j)}{\Pr(j>i)}}=\beta _{i}-\beta _{j},}"/>

where ⁠ logit ⁡ p = log ⁡ p 1 − p {\displaystyle \operatorname {logit} p=\log {\frac {p}{1-p}}}[image: {\displaystyle \operatorname {logit} p=\log {\frac {p}{1-p}}}] ⁠ for ⁠ 0 < p < 1 {\displaystyle 0<p<1}[image: {\displaystyle 0<p<1}] ⁠.

This formulation highlights the similarity between the Bradley–Terry model and [logistic regression][18]. Both employ essentially the same model but in different ways. In [logistic regression][18] one typically knows the parameters β i {\displaystyle \beta _{i}}[image: {\displaystyle \beta _{i}}] and attempts to infer the functional form of j)"}}'> j)}"> Pr ( i > j) {\displaystyle \Pr(i>j)} j)}"/>; in ranking under the Bradley–Terry model one knows the functional form and attempts to infer the parameters.

With a scale factor of 400 and a base of 10, this is equivalent to the [Elo rating system][19] for players with Elo ratings *R**i*and *R**j*. j) = \\frac{10^{R_i/400}}{10^{R_i/400} + 10^{R_j/400}} = \\frac{1}{1 + 10^{(R_j-R_i)/400}}."}}'> j)={\frac {10^{R_{i}/400}}{10^{R_{i}/400}+10^{R_{j}/400}}}={\frac {1}{1+10^{(R_{j}-R_{i})/400}}}.}"> Pr ( i > j) = 10 R i / 400 10 R i / 400 + 10 R j / 400 = 1 1 + 10 ( R j − R i) / 400. {\displaystyle \Pr(i>j)={\frac {10^{R_{i}/400}}{10^{R_{i}/400}+10^{R_{j}/400}}}={\frac {1}{1+10^{(R_{j}-R_{i})/400}}}.} j)={\frac {10^{R_{i}/400}}{10^{R_{i}/400}+10^{R_{j}/400}}}={\frac {1}{1+10^{(R_{j}-R_{i})/400}}}.}"/>

## Plackett–Luce model

[[edit][20]]

A standard generalization of the BT model is the Plackett– [Luce][21] model, [12] [13] which models ranking N {\displaystyle N}[image: {\displaystyle N}] items. In the same notation as BT model: \\cdots > y_N) = \\prod_{i=1}^N \\frac{p_{y_i}}{\\sum_{k=i}^N p_{y_k}} = \\frac{p_{y_1}}{p_{y_1} + \\dots + p_{y_N}}\\frac{p_{y_2}}{p_{y_2} + \\cdots + p_{y_N}} \\cdots \\frac{p_{y_N}}{p_{y_N}}"}}'> \cdots >y_{N})=\prod _{i=1}^{N}{\frac {p_{y_{i}}}{\sum _{k=i}^{N}p_{y_{k}}}}={\frac {p_{y_{1}}}{p_{y_{1}}+\dots +p_{y_{N}}}}{\frac {p_{y_{2}}}{p_{y_{2}}+\cdots +p_{y_{N}}}}\cdots {\frac {p_{y_{N}}}{p_{y_{N}}}}}"> Pr ( y 1 > ⋯ > y N) = ∏ i = 1 N p y i ∑ k = i N p y k = p y 1 p y 1 + ⋯ + p y N p y 2 p y 2 + ⋯ + p y N ⋯ p y N p y N {\displaystyle \Pr(y_{1}>\cdots >y_{N})=\prod _{i=1}^{N}{\frac {p_{y_{i}}}{\sum _{k=i}^{N}p_{y_{k}}}}={\frac {p_{y_{1}}}{p_{y_{1}}+\dots +p_{y_{N}}}}{\frac {p_{y_{2}}}{p_{y_{2}}+\cdots +p_{y_{N}}}}\cdots {\frac {p_{y_{N}}}{p_{y_{N}}}}} \cdots >y_{N})=\prod _{i=1}^{N}{\frac {p_{y_{i}}}{\sum _{k=i}^{N}p_{y_{k}}}}={\frac {p_{y_{1}}}{p_{y_{1}}+\dots +p_{y_{N}}}}{\frac {p_{y_{2}}}{p_{y_{2}}+\cdots +p_{y_{N}}}}\cdots {\frac {p_{y_{N}}}{p_{y_{N}}}}}"/> The factor with i = N {\displaystyle i=N}[image: {\displaystyle i=N}] is always just unity, so for N = 2 {\displaystyle N=2}[image: {\displaystyle N=2}] this reduces to y_2) = p_{y_1}/(p_{y_1} + p_{y_2})"}}'> y_{2})=p_{y_{1}}/(p_{y_{1}}+p_{y_{2}})}"> Pr ( y 1 > y 2) = p y 1 / ( p y 1 + p y 2) {\displaystyle \Pr(y_{1}>y_{2})=p_{y_{1}}/(p_{y_{1}}+p_{y_{2}})} y_{2})=p_{y_{1}}/(p_{y_{1}}+p_{y_{2}})}"/>.

This can be imagined as [drawing from an urn with replacement][22]. The urn contains balls colored in proportion to p 1, p 2, …, p N {\displaystyle p_{1},p_{2},\dots ,p_{N}}[image: {\displaystyle p_{1},p_{2},\dots ,p_{N}}], and one draws from the urn with replacement. If a ball has a new color, then that ball is placed as the next-ranked ball. Otherwise, if the ball has a color already drawn, then it is discarded.

Given the proportions p 1, p 2, …, p N {\displaystyle p_{1},p_{2},\dots ,p_{N}}[image: {\displaystyle p_{1},p_{2},\dots ,p_{N}}], the PL model can be sampled by the "exponential race" method. One samples " [radioactive decay][23] times" from N {\displaystyle N}[image: {\displaystyle N}] " [exponential][24] clocks", that is, t 1 ∼ E x p ( p 1), …, t N ∼ E x p ( p N) {\displaystyle t_{1}\sim \mathrm {Exp} (p_{1}),\dots ,t_{N}\sim \mathrm {Exp} (p_{N})}[image: {\displaystyle t_{1}\sim \mathrm {Exp} (p_{1}),\dots ,t_{N}\sim \mathrm {Exp} (p_{N})}]. Then one ranks the items according to the order in which they decayed. In this interpretation, it is immediately clear that the PL model satisfies [Luce's choice axiom][25] (from the same Luce). Therefore, for any two y, z {\displaystyle y,z}[image: {\displaystyle y,z}], z) = \\frac{p_y}{p_y + p_z}"}}'> z)={\frac {p_{y}}{p_{y}+p_{z}}}}"> Pr ( y > z) = p y p y + p z {\displaystyle \Pr(y>z)={\frac {p_{y}}{p_{y}+p_{z}}}} z)={\frac {p_{y}}{p_{y}+p_{z}}}}"/> reduces to the BT model, and in general, for any subset y 1, …, y M {\displaystyle y_{1},\dots ,y_{M}}[image: {\displaystyle y_{1},\dots ,y_{M}}] of the choices, \\cdots > y_N) = \\frac{p_{y_1}}{p_{y_1} + \\cdots + p_{y_M}}\\frac{p_{y_2}}{p_{y_2} + \\cdots + p_{y_M}} \\cdots \\frac{p_{y_M}}{p_{y_M}}"}}'> \cdots >y_{N})={\frac {p_{y_{1}}}{p_{y_{1}}+\cdots +p_{y_{M}}}}{\frac {p_{y_{2}}}{p_{y_{2}}+\cdots +p_{y_{M}}}}\cdots {\frac {p_{y_{M}}}{p_{y_{M}}}}}"> Pr ( y 1 > ⋯ > y N) = p y 1 p y 1 + ⋯ + p y M p y 2 p y 2 + ⋯ + p y M ⋯ p y M p y M {\displaystyle \Pr(y_{1}>\cdots >y_{N})={\frac {p_{y_{1}}}{p_{y_{1}}+\cdots +p_{y_{M}}}}{\frac {p_{y_{2}}}{p_{y_{2}}+\cdots +p_{y_{M}}}}\cdots {\frac {p_{y_{M}}}{p_{y_{M}}}}} \cdots >y_{N})={\frac {p_{y_{1}}}{p_{y_{1}}+\cdots +p_{y_{M}}}}{\frac {p_{y_{2}}}{p_{y_{2}}+\cdots +p_{y_{M}}}}\cdots {\frac {p_{y_{M}}}{p_{y_{M}}}}}"/> reduces to a smaller PL model with the same parameters.

## Inference

[[edit][26]]

The most common application of the Bradley–Terry model is to infer the values of the parameters p i {\displaystyle p_{i}}[image: {\displaystyle p_{i}}] given an observed set of outcomes j"}}'> j}"> i > j {\displaystyle i>j} j}"/>, such as wins and losses in a competition. The simplest way to estimate the parameters is by [maximum likelihood estimation][27], i.e., by maximizing the [likelihood][28] of the observed outcomes given the model and parameter values.

Suppose we know the outcomes of a set of pairwise competitions between a certain group of individuals, and let ij</sub>"}},"i":0}}]}'>w ij be the number of times individual i beats individual j. Then the likelihood of this set of outcomes within the Bradley–Terry model is j)]^{w_{ij}}"}}'> j)]^{w_{ij}}}"> ∏ i j [Pr ( i > j)] w i j {\displaystyle \prod _{ij}[\Pr(i>j)]^{w_{ij}}} j)]^{w_{ij}}}"/> and the [log-likelihood][29] of the parameter vector 1</sub>, ..., ''p<sub>n</sub>'']"}},"i":0}}]}'>**p**= [*p*1, ..., *p n*] is [1]

j) \\bigr]}^{w_{ij}} = \\sum_{i=1}^n \\sum_{j=1}^n \\ln \\biggl[ \\left(\\frac{p_i}{p_i+p_j}\\right)^{w_{ij}} \\biggr] \\\\[6pt]\n& = \\sum_{ij} w_{ij} \\ln \\biggl( \\frac{p_i}{p_i+p_j} \\biggr) = \\sum_{ij} \\bigl[ w_{ij} \\ln(p_i) - w_{ij} \\ln(p_i + p_j) \\bigr].\n\\end{align}"}}'> j){\bigr ]}}^{w_{ij}}=\sum _{i=1}^{n}\sum _{j=1}^{n}\ln {\biggl [}\left({\frac {p_{i}}{p_{i}+p_{j}}}\right)^{w_{ij}}{\biggr ]}\\[6pt]&=\sum _{ij}w_{ij}\ln {\biggl (}{\frac {p_{i}}{p_{i}+p_{j}}}{\biggr )}=\sum _{ij}{\bigl [}w_{ij}\ln(p_{i})-w_{ij}\ln(p_{i}+p_{j}){\bigr ]}.\end{aligned}}}"> l ( p) = ln ⁡ ∏ i j [Pr ( i > j)] w i j = ∑ i = 1 n ∑ j = 1 n ln ⁡ [( p i p i + p j) w i j] = ∑ i j w i j ln ⁡ ( p i p i + p j) = ∑ i j [w i j ln ⁡ ( p i) − w i j ln ⁡ ( p i + p j)]. {\displaystyle {\begin{aligned}{\mathcal {l}}(\mathbf {p} )&=\ln \prod _{ij}{{\bigl [}\Pr(i>j){\bigr ]}}^{w_{ij}}=\sum _{i=1}^{n}\sum _{j=1}^{n}\ln {\biggl [}\left({\frac {p_{i}}{p_{i}+p_{j}}}\right)^{w_{ij}}{\biggr ]}\\[6pt]&=\sum _{ij}w_{ij}\ln {\biggl (}{\frac {p_{i}}{p_{i}+p_{j}}}{\biggr )}=\sum _{ij}{\bigl [}w_{ij}\ln(p_{i})-w_{ij}\ln(p_{i}+p_{j}){\bigr ]}.\end{aligned}}} j){\bigr ]}}^{w_{ij}}=\sum _{i=1}^{n}\sum _{j=1}^{n}\ln {\biggl [}\left({\frac {p_{i}}{p_{i}+p_{j}}}\right)^{w_{ij}}{\biggr ]}\\[6pt]&=\sum _{ij}w_{ij}\ln {\biggl (}{\frac {p_{i}}{p_{i}+p_{j}}}{\biggr )}=\sum _{ij}{\bigl [}w_{ij}\ln(p_{i})-w_{ij}\ln(p_{i}+p_{j}){\bigr ]}.\end{aligned}}}"/>

Zermelo [5] showed that this expression has only a single maximum, which can be found by differentiating with respect to p i {\displaystyle p_{i}}[image: {\displaystyle p_{i}}] and setting the result to zero, which leads to

p_i = \\frac{\\sum_{j} w_{ij}}{\\sum_{j} (w_{ij}+w_{ji})/ (p_i+p_j)}.</math>"},"3":{"wt":"{{EquationRef|2}}"}},"i":0}}]}'>

p i = ∑ j w i j ∑ j ( w i j + w j i) / ( p i + p j). {\displaystyle p_{i}={\frac {\sum _{j}w_{ij}}{\sum _{j}(w_{ij}+w_{ji})/(p_{i}+p_{j})}}.}[image: {\displaystyle p_{i}={\frac {\sum _{j}w_{ij}}{\sum _{j}(w_{ij}+w_{ji})/(p_{i}+p_{j})}}.}] |  | 2 |

This equation has no known closed-form solution, but Zermelo suggested solving it by simple iteration. Starting from any convenient set of (positive) initial values for the p i {\displaystyle p_{i}}[image: {\displaystyle p_{i}}], one iteratively performs the update

p_i' = \\frac{\\sum_{j} w_{ij}}{\\sum_{j} (w_{ij}+w_{ji})/ (p_i+p_j)}</math>"},"3":{"wt":"{{EquationRef|3}}"}},"i":0}}]}'>

p i ′ = ∑ j w i j ∑ j ( w i j + w j i) / ( p i + p j) {\displaystyle p_{i}'={\frac {\sum _{j}w_{ij}}{\sum _{j}(w_{ij}+w_{ji})/(p_{i}+p_{j})}}}[image: {\displaystyle p_{i}'={\frac {\sum _{j}w_{ij}}{\sum _{j}(w_{ij}+w_{ji})/(p_{i}+p_{j})}}}] |  | 3 |

for all i in turn. The resulting parameters are arbitrary up to an overall multiplicative constant, so after computing all of the new values they should be normalized by dividing by their [geometric mean][30] thus:

p_i \\leftarrow \\frac{p'_i}{\\left(\\prod_{j=1}^n p'_j\\right)^{1/n}}.</math>"},"3":{"wt":"{{EquationRef|4}}"}},"i":0}}]}'>

p i ← p i ′ ( ∏ j = 1 n p j ′) 1 / n. {\displaystyle p_{i}\leftarrow {\frac {p'_{i}}{\left(\prod _{j=1}^{n}p'_{j}\right)^{1/n}}}.}[image: {\displaystyle p_{i}\leftarrow {\frac {p'_{i}}{\left(\prod _{j=1}^{n}p'_{j}\right)^{1/n}}}.}] |  | 4 |

This estimation procedure improves the log-likelihood on every iteration, and is guaranteed to eventually reach the unique maximum. [5] [14] It is, however, slow to converge. [1] [15] More recently it has been pointed out [16] that equation (**2**) can also be rearranged as

p i = ∑ j w i j p j / ( p i + p j) ∑ j w j i / ( p i + p j), {\displaystyle p_{i}={\frac {\sum _{j}w_{ij}p_{j}/(p_{i}+p_{j})}{\sum _{j}w_{ji}/(p_{i}+p_{j})}},}[image: {\displaystyle p_{i}={\frac {\sum _{j}w_{ij}p_{j}/(p_{i}+p_{j})}{\sum _{j}w_{ji}/(p_{i}+p_{j})}},}]

which can be solved by iterating

p_i' = \\frac{\\sum_{j} w_{ij} p_j/(p_i+p_j)}{\\sum_j w_{ji}/(p_i+p_j)},</math>"},"3":{"wt":"{{EquationRef|5}}"}},"i":0}}]}'>

p i ′ = ∑ j w i j p j / ( p i + p j) ∑ j w j i / ( p i + p j), {\displaystyle p_{i}'={\frac {\sum _{j}w_{ij}p_{j}/(p_{i}+p_{j})}{\sum _{j}w_{ji}/(p_{i}+p_{j})}},}[image: {\displaystyle p_{i}'={\frac {\sum _{j}w_{ij}p_{j}/(p_{i}+p_{j})}{\sum _{j}w_{ji}/(p_{i}+p_{j})}},}] |  | 5 |

again normalizing after every round of updates using equation (**4**). This iteration gives identical results to the one in (**3**) but converges much faster and hence is normally preferred over (**3**). [16]

### Worked example of solution procedure

[[edit][31]]

Consider a sporting competition between four teams, who play a total of 22 games among themselves. Each team's wins are given in the rows of the table below and the opponents are given as the columns:

Results

 | A | B | C | D |

**A** | – | 2 | 0 | 1 |

**B** | 3 | – | 5 | 0 |

**C** | 0 | 3 | – | 1 |

**D** | 4 | 0 | 3 | – |

For example, Team A has beat Team B twice and lost to team B three times; not played team C at all; won once and lost four times against team D.

We would like to estimate the relative strengths of the teams, which we do by calculating the parameters p i {\displaystyle p_{i}}[image: {\displaystyle p_{i}}], with higher parameters indicating greater prowess. To do this, we initialize the four entries in the parameter vector **p**arbitrarily, for example assigning the value 1 to each team: [1, 1, 1, 1]. Then we apply equation (**5**) to update p 1 {\displaystyle p_{1}}[image: {\displaystyle p_{1}}], which gives

p 1 = ∑ j ( ≠ 1) w 1 j p j / ( p 1 + p j) ∑ j ( ≠ 1) w j 1 / ( p 1 + p j) = 2 1 1 + 1 + 0 1 1 + 1 + 1 1 1 + 1 3 1 1 + 1 + 0 1 1 + 1 + 4 1 1 + 1 = 0.429. {\displaystyle p_{1}={\frac {\sum _{j(\neq 1)}w_{1j}p_{j}/(p_{1}+p_{j})}{\sum _{j(\neq 1)}w_{j1}/(p_{1}+p_{j})}}={\frac {2{\frac {1}{1+1}}+0{\frac {1}{1+1}}+1{\frac {1}{1+1}}}{3{\frac {1}{1+1}}+0{\frac {1}{1+1}}+4{\frac {1}{1+1}}}}=0.429.}[image: {\displaystyle p_{1}={\frac {\sum _{j(\neq 1)}w_{1j}p_{j}/(p_{1}+p_{j})}{\sum _{j(\neq 1)}w_{j1}/(p_{1}+p_{j})}}={\frac {2{\frac {1}{1+1}}+0{\frac {1}{1+1}}+1{\frac {1}{1+1}}}{3{\frac {1}{1+1}}+0{\frac {1}{1+1}}+4{\frac {1}{1+1}}}}=0.429.}]

Now, we apply (**5**) again to update p 2 {\displaystyle p_{2}}[image: {\displaystyle p_{2}}], making sure to use the new value of p 1 {\displaystyle p_{1}}[image: {\displaystyle p_{1}}] that we just calculated:

p 2 = ∑ j ( ≠ 2) w 2 j p j / ( p 2 + p j) ∑ j ( ≠ 2) w j 2 / ( p 2 + p j) = 3 0.429 1 + 0.429 + 5 1 1 + 1 + 0 1 1 + 1 2 1 1 + 0.429 + 3 1 1 + 1 + 0 1 1 + 1 = 1.172 {\displaystyle p_{2}={\frac {\sum _{j(\neq 2)}w_{2j}p_{j}/(p_{2}+p_{j})}{\sum _{j(\neq 2)}w_{j2}/(p_{2}+p_{j})}}={\frac {3{\frac {0.429}{1+0.429}}+5{\frac {1}{1+1}}+0{\frac {1}{1+1}}}{2{\frac {1}{1+0.429}}+3{\frac {1}{1+1}}+0{\frac {1}{1+1}}}}=1.172}[image: {\displaystyle p_{2}={\frac {\sum _{j(\neq 2)}w_{2j}p_{j}/(p_{2}+p_{j})}{\sum _{j(\neq 2)}w_{j2}/(p_{2}+p_{j})}}={\frac {3{\frac {0.429}{1+0.429}}+5{\frac {1}{1+1}}+0{\frac {1}{1+1}}}{2{\frac {1}{1+0.429}}+3{\frac {1}{1+1}}+0{\frac {1}{1+1}}}}=1.172}]

Similarly for p 3 {\displaystyle p_{3}}[image: {\displaystyle p_{3}}] and p 4 {\displaystyle p_{4}}[image: {\displaystyle p_{4}}] we get

p 3 = ∑ j ( ≠ 3) w 3 j p j / ( p 3 + p j) ∑ j ( ≠ 3) w j 3 / ( p 3 + p j) = 0 0.429 1 + 0.429 + 3 1.172 1 + 1.172 + 1 1 1 + 1 0 1 1 + 0.429 + 5 1 1 + 1.172 + 3 1 1 + 1 = 0.557 {\displaystyle p_{3}={\frac {\sum _{j(\neq 3)}w_{3j}p_{j}/(p_{3}+p_{j})}{\sum _{j(\neq 3)}w_{j3}/(p_{3}+p_{j})}}={\frac {0{\frac {0.429}{1+0.429}}+3{\frac {1.172}{1+1.172}}+1{\frac {1}{1+1}}}{0{\frac {1}{1+0.429}}+5{\frac {1}{1+1.172}}+3{\frac {1}{1+1}}}}=0.557}[image: {\displaystyle p_{3}={\frac {\sum _{j(\neq 3)}w_{3j}p_{j}/(p_{3}+p_{j})}{\sum _{j(\neq 3)}w_{j3}/(p_{3}+p_{j})}}={\frac {0{\frac {0.429}{1+0.429}}+3{\frac {1.172}{1+1.172}}+1{\frac {1}{1+1}}}{0{\frac {1}{1+0.429}}+5{\frac {1}{1+1.172}}+3{\frac {1}{1+1}}}}=0.557}]

p 4 = ∑ j ( ≠ 4) w 4 j p j / ( p 4 + p j) ∑ j ( ≠ 4) w j 4 / ( p 4 + p j) = 4 0.429 1 + 0.429 + 0 1.172 1 + 1.172 + 3 0.557 1 + 0.557 1 1 1 + 0.429 + 0 1 1 + 1.172 + 1 1 1 + 0.557 = 1.694 {\displaystyle p_{4}={\frac {\sum _{j(\neq 4)}w_{4j}p_{j}/(p_{4}+p_{j})}{\sum _{j(\neq 4)}w_{j4}/(p_{4}+p_{j})}}={\frac {4{\frac {0.429}{1+0.429}}+0{\frac {1.172}{1+1.172}}+3{\frac {0.557}{1+0.557}}}{1{\frac {1}{1+0.429}}+0{\frac {1}{1+1.172}}+1{\frac {1}{1+0.557}}}}=1.694}[image: {\displaystyle p_{4}={\frac {\sum _{j(\neq 4)}w_{4j}p_{j}/(p_{4}+p_{j})}{\sum _{j(\neq 4)}w_{j4}/(p_{4}+p_{j})}}={\frac {4{\frac {0.429}{1+0.429}}+0{\frac {1.172}{1+1.172}}+3{\frac {0.557}{1+0.557}}}{1{\frac {1}{1+0.429}}+0{\frac {1}{1+1.172}}+1{\frac {1}{1+0.557}}}}=1.694}]

Then we normalize all the parameters by dividing by their geometric mean ( 0.429 × 1.172 × 0.557 × 1.694) 1 / 4 = 0.830 {\displaystyle (0.429\times 1.172\times 0.557\times 1.694)^{1/4}=0.830}[image: {\displaystyle (0.429\times 1.172\times 0.557\times 1.694)^{1/4}=0.830}] to get the estimated parameters **p**= [0.516, 1.413, 0.672, 2.041].

To improve the estimates further, we repeat the process, using the new **p**values. For example,

p 1 = 2 ⋅ 1.413 0.516 + 1.413 + 0 ⋅ 0.672 0.516 + 0.672 + 1 ⋅ 2.041 0.516 + 2.041 3 ⋅ 1 0.516 + 1.413 + 0 ⋅ 1 0.516 + 0.672 + 4 ⋅ 1 0.516 + 2.041 = 0.725. {\displaystyle p_{1}={\frac {2\cdot {\frac {1.413}{0.516+1.413}}+0\cdot {\frac {0.672}{0.516+0.672}}+1\cdot {\frac {2.041}{0.516+2.041}}}{3\cdot {\frac {1}{0.516+1.413}}+0\cdot {\frac {1}{0.516+0.672}}+4\cdot {\frac {1}{0.516+2.041}}}}=0.725.}[image: {\displaystyle p_{1}={\frac {2\cdot {\frac {1.413}{0.516+1.413}}+0\cdot {\frac {0.672}{0.516+0.672}}+1\cdot {\frac {2.041}{0.516+2.041}}}{3\cdot {\frac {1}{0.516+1.413}}+0\cdot {\frac {1}{0.516+0.672}}+4\cdot {\frac {1}{0.516+2.041}}}}=0.725.}]

Repeating this process for the remaining parameters and normalizing, we get **p**= [0.677, 1.034, 0.624, 2.287]. Repeating a further 10 times gives rapid convergence toward a final solution of **p**= [0.640, 1.043, 0.660, 2.270]. This indicates that Team D is the strongest and Team B the second strongest, while Teams A and C are nearly equal in strength but below Teams B and D. In this way the Bradley–Terry model lets us infer the relationship between all four teams, even though not all teams have played each other.

## Variations

[[edit][32]]

### Crowd-BT

[[edit][33]]

The Crowd-BT model, developed in 2013 by Chen et al, [17] attempts to extend the standard Bradley–Terry model for [crowdsourced][34] settings while reducing the number of comparisons needed by taking into account the reliability of each judge. In particular, it identifies and excludes judges presumed to be spammers (selecting choices at random) or malicious (selecting always the wrong choice). In a crowdsourced task of ranking documents by reading difficulty with 624 judges contributing up to 40 pairwise comparisons each, Crowd-BT was shown to outperform both standard Bradley–Terry as well as ranking system [TrueSkill][35]. It has been recommended for use when quality results are valued over efficiency and the number of comparisons is high. [18]

## See also

[[edit][36]]

- [Elo rating system][19]
- [Ordinal regression][37]
- [Rasch model][38]
- [Scale (social sciences)][39]
- [Softmax function][40]
- [Thurstonian model][41]

## References

[[edit][42]]

1. 1 2 3 4 5 Hunter, David R. (2004). ["MM algorithms for generalized Bradley–Terry models"][43]. *The Annals of Statistics*. **32**(1): 384– 406. [CiteSeerX][44] [10.1.1.110.7878][45]. [doi][46]: [10.1214/aos/1079120141][47]. [JSTOR][48] [3448514][49]. [Archived][50] from the original on 2021-02-09. Retrieved 2015-08-29.`{{ [cite journal][51] }}`: Cite uses deprecated parameter `| citeseerx=`( [help][52])
2. 1 2 3 Agresti, Alan (2014). *Categorical Data Analysis*. John Wiley & Sons. pp. 436– 439.
3. ↑ E.E.M. van Berkum. ["Bradley-Terry model"][53]. *Encyclopedia of Mathematics*. Retrieved 18 November 2014.
4. ↑ Bradley, Ralph Allan; Terry, Milton E. (1952). "Rank Analysis of Incomplete Block Designs: I. The Method of Paired Comparisons". *Biometrika*. **39**(3/4): 324– 345. [doi][46]: [10.2307/2334029][54]. [JSTOR][48] [2334029][55].
5. 1 2 3 Zermelo, Ernst (1929). "Die Berechnung der Turnier-Ergebnisse als ein Maximumproblem der Wahrscheinlichkeitsrechnung". *[Mathematische Zeitschrift][56]*. **29**(1): 436– 460. [doi][46]: [10.1007/BF01180541][57]. [S2CID][58] [122877703][59].
6. ↑ Heinz-Dieter Ebbinghaus (2007), *Ernst Zermelo: An Approach to His Life and Work*, Springer, pp. 268– 269, [ISBN][60] [978-3-540-49553-6][61]
7. ↑ Shev, A.; Fujii, K.; Hsieh, F.; McCowan, B. (2014). ["Systemic testing on Bradley-Terry model against nonlinear ranking hierarchy"][62]. *[PLOS One][63]*. **9**(12) e115367. [Bibcode][64]: [2014PLoSO...9k5367S][65]. [doi][46]: [10.1371/journal.pone.0115367][66]. [PMC][67] [4274013][62]. [PMID][68] [25531899][69].
8. ↑ Boyd, Robert; [Silk, Joan B.][70] (1983). "A method for assigning cardinal dominance ranks". *[Animal Behaviour][71]*. **31**(1): 45– 58. [doi][46]: [10.1016/S0003-3472(83)80172-9][72]. [S2CID][58] [53178779][73].
9. ↑ ["Chatbot Arena: New models & Elo system update | LMSYS Org"][74]. *lmsys.org*. Retrieved 2024-01-30.
10. ↑ von Csefalvay, Chris (2026). *Post-Training: A Practical Guide for AI Engineers and Developers*. No Starch Press. p. 115. [ISBN][60] [978-1-7185-0520-9][75].
11. ↑ Szummer, Martin; Yilmaz, Emine (2011). **[Semi-supervised learning to rank with preference regularization][76] (PDF). CIKM.
12. ↑ Plackett, R. L. (1975). "The Analysis of Permutations". *Applied Statistics*. **24**(2): 193– 202. [doi][46]: [10.2307/2346567][77]. [JSTOR][48] [2346567][78].
13. ↑ Luce, R. D. (1959). *Individual Choice Behavior: A Theoretical Analysis*. Wiley.
14. ↑ Ford, Jr., L. R. (1957). "Solution of a ranking problem from binary comparisons". *[American Mathematical Monthly][79]*. **64**(8): 28– 33. [doi][46]: [10.1080/00029890.1957.11989117][80].
15. ↑ Dykstra, Jr., Otto (1956). "A note on the rank analysis of incomplete block designs". *[Biometrics][81]*. **12**: 301– 306. [doi][46]: [10.2307/2334029][54]. [JSTOR][48] [2334029][55].
16. 1 2 Newman, M. E. J. (2023). ["Efficient computation of rankings from pairwise comparisons"][82]. *[Journal of Machine Learning Research][83]*. **24**(238): 1– 25. [Archived][84] from the original on 2024-10-06. Retrieved 2023-08-15.
17. ↑ Chen, Xi; Bennett, Paul N.; Collins-Thompson, Kevyn; Horvitz, Eric (4 February 2013). "Pairwise ranking aggregation in a crowdsourced setting". *Proceedings of the sixth ACM international conference on Web search and data mining*. pp. 193– 202. [doi][46]: [10.1145/2433396.2433420][85]. [ISBN][60] [978-1-4503-1869-3][86].
18. ↑ Zhang, Xiaohang; Li, Guoliang; Feng, Jianhua (April 2016). "Crowdsourced top-k algorithms: an experimental evaluation". *Proceedings of the VLDB Endowment*. **9**(8): 612– 623. [doi][46]: [10.14778/2921558.2921559][87].

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Bradley–Terry_model&oldid=1363947235#Plackett–Luce_model][88] "

[Categories][89]:

- [Machine learning][90]
- [Statistical models][91]
- [Logistic regression][92]
- [Regression models][93]

Hidden categories:

- [Articles with short description][94]
- [Short description matches Wikidata][95]
- [CS1 errors: deprecated parameters][96]

Search

Bradley–Terry model

3 languages Add topic


## Links

[1]: /w/index.php?title=Plackett%E2%80%93Luce_model&amp;redirect=no
[2]: https://en.wikipedia.org/wiki/Probability_theory
[3]: https://en.wikipedia.org/wiki/Population_(statistics)
[4]: https://en.wikipedia.org/wiki/Pairwise_comparison_(psychology)
[5]: https://en.wikipedia.org/wiki/Real_number
[6]: /w/index.php?title=Bradley%E2%80%93Terry_model&amp;action=edit&amp;section=1
[7]: https://en.wikipedia.org/wiki/Ralph_A._Bradley
[8]: https://en.wikipedia.org/wiki/Ernst_Zermelo
[9]: https://en.wikipedia.org/wiki/Chess_rating_system
[10]: https://en.wikipedia.org/wiki/Choice_modeling
[11]: https://en.wikipedia.org/wiki/Dominance_hierarchy
[12]: https://en.wikipedia.org/wiki/Scientific_journal
[13]: https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback
[14]: https://en.wikipedia.org/wiki/Learning_to_rank
[15]: https://en.wikipedia.org/wiki/Search_engine
[16]: /w/index.php?title=Bradley%E2%80%93Terry_model&amp;action=edit&amp;section=2
[17]: https://en.wikipedia.org/wiki/Logit
[18]: https://en.wikipedia.org/wiki/Logistic_regression
[19]: https://en.wikipedia.org/wiki/Elo_rating_system
[20]: /w/index.php?title=Bradley%E2%80%93Terry_model&amp;action=edit&amp;section=3
[21]: https://en.wikipedia.org/wiki/R._Duncan_Luce
[22]: https://en.wikipedia.org/wiki/Sampling_with_replacement
[23]: https://en.wikipedia.org/wiki/Radioactive_decay
[24]: https://en.wikipedia.org/wiki/Exponential_distribution
[25]: https://en.wikipedia.org/wiki/Luce's_choice_axiom
[26]: /w/index.php?title=Bradley%E2%80%93Terry_model&amp;action=edit&amp;section=4
[27]: https://en.wikipedia.org/wiki/Maximum_likelihood
[28]: https://en.wikipedia.org/wiki/Likelihood
[29]: https://en.wikipedia.org/wiki/Log-likelihood
[30]: https://en.wikipedia.org/wiki/Geometric_mean
[31]: /w/index.php?title=Bradley%E2%80%93Terry_model&amp;action=edit&amp;section=5
[32]: /w/index.php?title=Bradley%E2%80%93Terry_model&amp;action=edit&amp;section=6
[33]: /w/index.php?title=Bradley%E2%80%93Terry_model&amp;action=edit&amp;section=7
[34]: https://en.wikipedia.org/wiki/Crowdsourcing
[35]: https://en.wikipedia.org/wiki/TrueSkill
[36]: /w/index.php?title=Bradley%E2%80%93Terry_model&amp;action=edit&amp;section=8
[37]: https://en.wikipedia.org/wiki/Ordinal_regression
[38]: https://en.wikipedia.org/wiki/Rasch_model
[39]: https://en.wikipedia.org/wiki/Scale_(social_sciences)
[40]: https://en.wikipedia.org/wiki/Softmax_function
[41]: https://en.wikipedia.org/wiki/Thurstonian_model
[42]: /w/index.php?title=Bradley%E2%80%93Terry_model&amp;action=edit&amp;section=9
[43]: http://projecteuclid.org/euclid.aos/1079120141
[44]: https://en.wikipedia.org/wiki/CiteSeerX_(identifier)
[45]: https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.110.7878
[46]: https://en.wikipedia.org/wiki/Doi_(identifier)
[47]: https://doi.org/10.1214%2Faos%2F1079120141
[48]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[49]: https://www.jstor.org/stable/3448514
[50]: https://web.archive.org/web/20210209224246/https://projecteuclid.org/euclid.aos/1079120141
[51]: https://en.wikipedia.org/wiki/Template:Cite_journal
[52]: https://en.wikipedia.org/wiki/Help:CS1_errors#deprecated_params
[53]: http://www.encyclopediaofmath.org/index.php?title=Bradley-Terry_model&amp;oldid=22181
[54]: https://doi.org/10.2307%2F2334029
[55]: https://www.jstor.org/stable/2334029
[56]: https://en.wikipedia.org/wiki/Mathematische_Zeitschrift
[57]: https://doi.org/10.1007%2FBF01180541
[58]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[59]: https://api.semanticscholar.org/CorpusID:122877703
[60]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[61]: https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-49553-6
[62]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4274013
[63]: https://en.wikipedia.org/wiki/PLOS_One
[64]: https://en.wikipedia.org/wiki/Bibcode_(identifier)
[65]: https://ui.adsabs.harvard.edu/abs/2014PLoSO...9k5367S
[66]: https://doi.org/10.1371%2Fjournal.pone.0115367
[67]: https://en.wikipedia.org/wiki/PMC_(identifier)
[68]: https://en.wikipedia.org/wiki/PMID_(identifier)
[69]: https://pubmed.ncbi.nlm.nih.gov/25531899
[70]: https://en.wikipedia.org/wiki/Joan_Silk
[71]: https://en.wikipedia.org/wiki/Animal_Behaviour
[72]: https://doi.org/10.1016%2FS0003-3472%2883%2980172-9
[73]: https://api.semanticscholar.org/CorpusID:53178779
[74]: https://lmsys.org/blog/2023-12-07-leaderboard
[75]: https://en.wikipedia.org/wiki/Special:BookSources/978-1-7185-0520-9
[76]: http://research.microsoft.com/pubs/154323/SzummerYilmaz-semisupervised-ranking-cikm11.pdf
[77]: https://doi.org/10.2307%2F2346567
[78]: https://www.jstor.org/stable/2346567
[79]: https://en.wikipedia.org/wiki/American_Mathematical_Monthly
[80]: https://doi.org/10.1080%2F00029890.1957.11989117
[81]: https://en.wikipedia.org/wiki/Biometrics
[82]: https://jmlr.org/papers/v24/22-1086.html
[83]: https://en.wikipedia.org/wiki/Journal_of_Machine_Learning_Research
[84]: https://web.archive.org/web/20241006153025/https://jmlr.org/papers/v24/22-1086.html
[85]: https://doi.org/10.1145%2F2433396.2433420
[86]: https://en.wikipedia.org/wiki/Special:BookSources/978-1-4503-1869-3
[87]: https://doi.org/10.14778%2F2921558.2921559
[88]: https://en.wikipedia.org/w/index.php?title=Bradley–Terry_model&amp;oldid=1363947235#Plackett–Luce_model
[89]: /wiki/Help:Category
[90]: /wiki/Category:Machine_learning
[91]: /wiki/Category:Statistical_models
[92]: /wiki/Category:Logistic_regression
[93]: /wiki/Category:Regression_models
[94]: /wiki/Category:Articles_with_short_description
[95]: /wiki/Category:Short_description_matches_Wikidata
[96]: /wiki/Category:CS1_errors:_deprecated_parameters
