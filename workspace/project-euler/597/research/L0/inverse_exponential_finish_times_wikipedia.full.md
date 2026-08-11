<!-- source: https://en.wikipedia.org/wiki/Inverse_distribution | converted from HTML -->

Inverse distribution - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Probability theory

[image: icon] [1]

 |

This article **needs [more citations][2]**. Please help [improve this article][3] by [adding citations to reliable sources][4]. Unsourced material may be challenged and [removed][5].
*Find sources:*["Inverse distribution"][6] – [news][7]**·**[newspapers][8]**·**[books][9]**·**[scholar][10]**·**[JSTOR][11]*( March 2025)**( [Learn how and when to remove this message][12])*

 |

Not to be confused with [Inverse distribution function][13].

In [probability theory][14] and [statistics][15], an **inverse distribution**is the distribution of the [reciprocal][16] of a random variable. Inverse distributions arise in particular in the [Bayesian][17] context of [prior distributions][18] and [posterior distributions][19] for [scale parameters][20]. In the [algebra of random variables][21], inverse distributions are special cases of the class of [ratio distributions][22], in which the numerator random variable has a [degenerate distribution][23].

## Relation to original distribution

[[edit][24]]

In general, given the [probability distribution][25] of a random variable *X*with strictly positive support, it is possible to find the distribution of the reciprocal, *Y*= 1 / X. If the distribution of *X*is [continuous][26] with [density function][27]*f*(*x*) and [cumulative distribution function][28]*F*(*x*), then the cumulative distribution function, *G*(*y*), of the reciprocal is found by noting that

G ( y) = Pr ( Y ≤ y) = Pr ( X ≥ 1 y) = 1 − Pr ( X < 1 y) = 1 − F ( 1 y). {\displaystyle G(y)=\Pr(Y\leq y)=\Pr \left(X\geq {\frac {1}{y}}\right)=1-\Pr \left(X<{\frac {1}{y}}\right)=1-F\left({\frac {1}{y}}\right).}[image: {\displaystyle G(y)=\Pr(Y\leq y)=\Pr \left(X\geq {\frac {1}{y}}\right)=1-\Pr \left(X<{\frac {1}{y}}\right)=1-F\left({\frac {1}{y}}\right).}]

Then the density function of *Y*is found as the derivative of the cumulative distribution function:

g ( y) = 1 y 2 f ( 1 y). {\displaystyle g(y)={\frac {1}{y^{2}}}f\left({\frac {1}{y}}\right).}[image: {\displaystyle g(y)={\frac {1}{y^{2}}}f\left({\frac {1}{y}}\right).}]

## Examples

[[edit][29]]

### Reciprocal distribution

[[edit][30]]

The [reciprocal distribution][31] has a density function of the form [1]

f ( x) ∝ x − 1 for 0 < a < x < b, {\displaystyle f(x)\propto x^{-1}\quad {\text{ for }}0<a<x<b,}[image: {\displaystyle f(x)\propto x^{-1}\quad {\text{ for }}0<a<x<b,}]

where ∝ {\displaystyle \propto \!\,}[image: {\displaystyle \propto \!\,}] means ["is proportional to"][32]. It follows that the inverse distribution in this case is of the form

g ( y) ∝ y − 1 for 0 ≤ b − 1 < y < a − 1, {\displaystyle g(y)\propto y^{-1}\quad {\text{ for }}0\leq b^{-1}<y<a^{-1},}[image: {\displaystyle g(y)\propto y^{-1}\quad {\text{ for }}0\leq b^{-1}<y<a^{-1},}]

which is again a reciprocal distribution.

### Inverse uniform distribution

[[edit][33]]

0 < a < b, \\quad a, b \\in \\R</math>"},"support":{"wt":"<math> [ b^{-1} , a^{-1} ] </math>"},"pdf":{"wt":"<math> y^{-2} \\frac{ 1 }{ b-a } </math>"},"cdf":{"wt":"<math> \\frac{ b - y^{-1} }{ b - a } </math>"},"mean":{"wt":"<math> \\frac{ \\ln(b) - \\ln(a)}{ b - a } </math>"},"median":{"wt":"<math> \\frac{ 2}{ a+b }</math>"},"variance":{"wt":"<math> \\frac{1}{a \\cdot b} - \\left( \\frac{ \\ln(b) - \\ln(a)}{ b - a } \\right)^2 </math>"},"skewness":{"wt":""},"kurtosis":{"wt":""},"entropy":{"wt":""},"mgf":{"wt":""},"char":{"wt":""},"pgf":{"wt":""},"fisher":{"wt":""}},"i":0}}]}'>

Inverse uniform distribution |

[Parameters][34] | 0 < a < b, a, b ∈ R {\displaystyle 0<a<b,\quad a,b\in \mathbb {R} }[image: {\displaystyle 0<a<b,\quad a,b\in \mathbb {R} }] |

[Support][35] | [b − 1, a − 1] {\displaystyle [b^{-1},a^{-1}]}[image: {\displaystyle [b^{-1},a^{-1}]}] |

[PDF][27] | y − 2 1 b − a {\displaystyle y^{-2}{\frac {1}{b-a}}}[image: {\displaystyle y^{-2}{\frac {1}{b-a}}}] |

[CDF][28] | b − y − 1 b − a {\displaystyle {\frac {b-y^{-1}}{b-a}}}[image: {\displaystyle {\frac {b-y^{-1}}{b-a}}}] |

[Mean][36] | ln ⁡ ( b) − ln ⁡ ( a) b − a {\displaystyle {\frac {\ln(b)-\ln(a)}{b-a}}}[image: {\displaystyle {\frac {\ln(b)-\ln(a)}{b-a}}}] |

[Median][37] | 2 a + b {\displaystyle {\frac {2}{a+b}}}[image: {\displaystyle {\frac {2}{a+b}}}] |

[Variance][38] | 1 a ⋅ b − ( ln ⁡ ( b) − ln ⁡ ( a) b − a) 2 {\displaystyle {\frac {1}{a\cdot b}}-\left({\frac {\ln(b)-\ln(a)}{b-a}}\right)^{2}}[image: {\displaystyle {\frac {1}{a\cdot b}}-\left({\frac {\ln(b)-\ln(a)}{b-a}}\right)^{2}}] |

If the original random variable *X*is [uniformly distributed][39] on the interval (*a*,*b*), where *a*>0, then the reciprocal variable *Y*= 1 / *X*has the reciprocal distribution which takes values in the range (*b*−1,*a*−1), and the probability density function in this range is

g ( y) = y − 2 1 b − a, {\displaystyle g(y)=y^{-2}{\frac {1}{b-a}},}[image: {\displaystyle g(y)=y^{-2}{\frac {1}{b-a}},}]

and is zero elsewhere.

The cumulative distribution function of the reciprocal, within the same range, is

G ( y) = b − y − 1 b − a. {\displaystyle G(y)={\frac {b-y^{-1}}{b-a}}.}[image: {\displaystyle G(y)={\frac {b-y^{-1}}{b-a}}.}]

For example, if *X*is uniformly distributed on the interval (0,1), then *Y*= 1 / *X*has density g ( y) = y − 2 {\displaystyle g(y)=y^{-2}}[image: {\displaystyle g(y)=y^{-2}}] and cumulative distribution function G ( y) = 1 − y − 1 {\displaystyle G(y)={1-y^{-1}}}[image: {\displaystyle G(y)={1-y^{-1}}}] when 1 ."}}'> 1.}"> y > 1. {\displaystyle y>1.} 1.}"/>

### Inverse *t*distribution

[[edit][40]]

Let *X*be a **[t distributed][41] random variate with *k*[degrees of freedom][42]. Then its density function is

f ( x) = 1 k π Γ ( k + 1 2) Γ ( k 2) 1 ( 1 + x 2 k) 1 + k 2. {\displaystyle f(x)={\frac {1}{\sqrt {k\pi }}}{\frac {\Gamma \left({\frac {k+1}{2}}\right)}{\Gamma \left({\frac {k}{2}}\right)}}{\frac {1}{\left(1+{\frac {x^{2}}{k}}\right)^{\frac {1+k}{2}}}}.}[image: {\displaystyle f(x)={\frac {1}{\sqrt {k\pi }}}{\frac {\Gamma \left({\frac {k+1}{2}}\right)}{\Gamma \left({\frac {k}{2}}\right)}}{\frac {1}{\left(1+{\frac {x^{2}}{k}}\right)^{\frac {1+k}{2}}}}.}]

The density of *Y*= 1 / *X*is

g ( y) = 1 k π Γ ( k + 1 2) Γ ( k 2) 1 y 2 ( 1 + 1 y 2 k) 1 + k 2. {\displaystyle g(y)={\frac {1}{\sqrt {k\pi }}}{\frac {\Gamma \left({\frac {k+1}{2}}\right)}{\Gamma \left({\frac {k}{2}}\right)}}{\frac {1}{y^{2}\left(1+{\frac {1}{y^{2}k}}\right)^{\frac {1+k}{2}}}}.}[image: {\displaystyle g(y)={\frac {1}{\sqrt {k\pi }}}{\frac {\Gamma \left({\frac {k+1}{2}}\right)}{\Gamma \left({\frac {k}{2}}\right)}}{\frac {1}{y^{2}\left(1+{\frac {1}{y^{2}k}}\right)^{\frac {1+k}{2}}}}.}]

With *k*= 1, the distributions of *X*and 1 /*X*are identical (*X*is then [Cauchy distributed][43] (0,1)). If *k*> 1 then the distribution of 1 /*X*is [bimodal][44]. [*[citation needed][45]*]

### Reciprocal normal distribution

[[edit][46]]

See also: [Propagation of uncertainty § Reciprocal and shifted reciprocal][47]

If variable X {\displaystyle X}[image: {\displaystyle X}] follows a [normal distribution][48] N ( μ, σ 2) {\displaystyle {\mathcal {N}}(\mu ,\sigma ^{2})}[image: {\displaystyle {\mathcal {N}}(\mu ,\sigma ^{2})}], then the inverse or reciprocal Y = 1 X {\displaystyle Y={\frac {1}{X}}}[image: {\displaystyle Y={\frac {1}{X}}}] follows a reciprocal normal distribution: [2]

f ( y) = 1 2 π σ y 2 e − 1 2 ( 1 / y − μ σ) 2. {\displaystyle f(y)={\frac {1}{{\sqrt {2\pi }}\sigma y^{2}}}e^{-{\frac {1}{2}}\left({\frac {1/y-\mu }{\sigma }}\right)^{2}}.}[image: {\displaystyle f(y)={\frac {1}{{\sqrt {2\pi }}\sigma y^{2}}}e^{-{\frac {1}{2}}\left({\frac {1/y-\mu }{\sigma }}\right)^{2}}.}] [49] Graph of the density of the inverse of the standard normal distribution

If variable *X*follows a [standard normal distribution][50] N ( 0, 1) {\displaystyle {\mathcal {N}}(0,1)}[image: {\displaystyle {\mathcal {N}}(0,1)}], then *Y*= 1/*X*follows a *reciprocal standard normal distribution*, [heavy-tailed][51] and [bimodal][52], [2] with modes at ± 1 2 {\displaystyle \pm {\tfrac {1}{\sqrt {2}}}}[image: {\displaystyle \pm {\tfrac {1}{\sqrt {2}}}}] and density

f ( y) = e − 1 2 y 2 2 π y 2 {\displaystyle f(y)={\frac {e^{-{\frac {1}{2y^{2}}}}}{{\sqrt {2\pi }}y^{2}}}}[image: {\displaystyle f(y)={\frac {e^{-{\frac {1}{2y^{2}}}}}{{\sqrt {2\pi }}y^{2}}}}]

and the first and higher-order moments do not exist. [2] For such inverse distributions and for [ratio distributions][22], there can still be defined probabilities for intervals, which can be computed either by [Monte Carlo simulation][53] or, in some cases, by using the Geary–Hinkley transformation. [3]

However, in the more general case of a shifted reciprocal function 1 / ( p − B) {\displaystyle 1/(p-B)}[image: {\displaystyle 1/(p-B)}], for B = N ( μ, σ) {\displaystyle B=N(\mu ,\sigma )}[image: {\displaystyle B=N(\mu ,\sigma )}] following a general normal distribution, then mean and variance statistics do exist in a [principal value][54] sense, if the difference between the pole p {\displaystyle p}[image: {\displaystyle p}] and the mean μ {\displaystyle \mu }[image: {\displaystyle \mu }] is real valued. The mean of this transformed random variable (*reciprocal shifted normal distribution*) is then indeed the scaled [Dawson's function][55]: [4]

2 σ F ( p − μ 2 σ). {\displaystyle {\frac {\sqrt {2}}{\sigma }}F\left({\frac {p-\mu }{{\sqrt {2}}\sigma }}\right).}[image: {\displaystyle {\frac {\sqrt {2}}{\sigma }}F\left({\frac {p-\mu }{{\sqrt {2}}\sigma }}\right).}]

In contrast, if the shift p − μ {\displaystyle p-\mu }[image: {\displaystyle p-\mu }] is purely complex, the mean exists and is a scaled [Faddeeva function][56], whose exact expression depends on the sign of the imaginary part, Im ⁡ ( p − μ) {\displaystyle \operatorname {Im} (p-\mu )}[image: {\displaystyle \operatorname {Im} (p-\mu )}]. In both cases, the variance is a simple function of the mean. [5] Therefore, the variance has to be considered in a principal value sense if p − μ {\displaystyle p-\mu }[image: {\displaystyle p-\mu }] is real, while it exists if the imaginary part of p − μ {\displaystyle p-\mu }[image: {\displaystyle p-\mu }] is non-zero. Note that these means and variances are exact, as they do not recur to linearisation of the ratio. The exact covariance of two ratios with a pair of different poles p 1 {\displaystyle p_{1}}[image: {\displaystyle p_{1}}] and p 2 {\displaystyle p_{2}}[image: {\displaystyle p_{2}}] is similarly available. [6] The case of the inverse of a [complex normal variable][57] B {\displaystyle B}[image: {\displaystyle B}], shifted or not, exhibits different characteristics. [4]

### Inverse exponential distribution

[[edit][58]]

If X {\displaystyle X}[image: {\displaystyle X}] is an exponentially distributed random variable with rate parameter λ {\displaystyle \lambda }[image: {\displaystyle \lambda }], then Y = 1 / X {\displaystyle Y=1/X}[image: {\displaystyle Y=1/X}] has the following cumulative distribution function: F Y ( y) = e − λ / y {\displaystyle F_{Y}(y)=e^{-\lambda /y}}[image: {\displaystyle F_{Y}(y)=e^{-\lambda /y}}] for 0"}}'> 0}"> y > 0 {\displaystyle y>0} 0}"/>. Note that the expected value of this random variable does not exist. The reciprocal exponential distribution finds use in the analysis of fading wireless communication systems.

### Inverse Cauchy distribution

[[edit][59]]

If *X*is a [Cauchy distributed][43] (*μ*, *σ*) random variable, then 1 / X is a Cauchy ( *μ*/ *C*, *σ*/ *C*) random variable where *C*= *μ*2 + *σ*2.

### Inverse F distribution

[[edit][60]]

If *X*is an ******[F ( ν 1, ν 2) distributed][61] random variable then 1 / *X*is an *F*(*ν*2, *ν*1) random variable.

### Reciprocal of binomial distribution

[[edit][62]]

If X {\displaystyle X}[image: {\displaystyle X}] is distributed according to a Binomial distribution with n {\displaystyle n}[image: {\displaystyle n}] number of trials and a probability of success p {\displaystyle p}[image: {\displaystyle p}] then no closed form for the reciprocal distribution is known. However, we can calculate the mean of this distribution.

E [1 ( 1 + X)] = 1 p ( n + 1) ( 1 − ( 1 − p) n + 1) {\displaystyle E\left[{\frac {1}{(1+X)}}\right]={\frac {1}{p(n+1)}}\left(1-(1-p)^{n+1}\right)}[image: {\displaystyle E\left[{\frac {1}{(1+X)}}\right]={\frac {1}{p(n+1)}}\left(1-(1-p)^{n+1}\right)}]

An asymptotic approximation for the non-central moments of the reciprocal distribution is known. [7]

E [( 1 + X) a] = O ( ( n p) − a) + o ( n − a) {\displaystyle E[(1+X)^{a}]=O((np)^{-a})+o(n^{-a})}[image: {\displaystyle E[(1+X)^{a}]=O((np)^{-a})+o(n^{-a})}]

where O() and o() are the big and little [o order functions][63] and a {\displaystyle a}[image: {\displaystyle a}] is a real number.

### Reciprocal of triangular distribution

[[edit][64]]

For a [triangular distribution][65] with lower limit *a*, upper limit *b*and mode *c*, where *a*<*b*and *a*≤*c*≤*b*, the mean of the reciprocal is given by

μ = 2 ( a l n ( a c) a − c + b l n ( c b) b − c) a − b {\displaystyle \mu ={\frac {2\left({\frac {a\,\mathrm {ln} \left({\frac {a}{c}}\right)}{a-c}}+{\frac {b\,\mathrm {ln} \left({\frac {c}{b}}\right)}{b-c}}\right)}{a-b}}}[image: {\displaystyle \mu ={\frac {2\left({\frac {a\,\mathrm {ln} \left({\frac {a}{c}}\right)}{a-c}}+{\frac {b\,\mathrm {ln} \left({\frac {c}{b}}\right)}{b-c}}\right)}{a-b}}}]

and the variance by

σ 2 = 2 ( l n ( c a) a − c + l n ( b c) b − c) a − b − μ 2 {\displaystyle \sigma ^{2}={\frac {2\left({\frac {\mathrm {ln} \left({\frac {c}{a}}\right)}{a-c}}+{\frac {\mathrm {ln} \left({\frac {b}{c}}\right)}{b-c}}\right)}{a-b}}-\mu ^{2}}[image: {\displaystyle \sigma ^{2}={\frac {2\left({\frac {\mathrm {ln} \left({\frac {c}{a}}\right)}{a-c}}+{\frac {\mathrm {ln} \left({\frac {b}{c}}\right)}{b-c}}\right)}{a-b}}-\mu ^{2}}].

Both moments of the reciprocal are only defined when the triangle does not cross zero, i.e. when *a*, *b*, and *c*are either all positive or all negative.

### Other inverse distributions

[[edit][66]]

Other inverse distributions include

[inverse-chi-squared distribution][67] [inverse-gamma distribution][68] [inverse-Wishart distribution][69] [inverse matrix gamma distribution][70]

## Applications

[[edit][71]]

[image: icon] [1]

 |

This section **does not [cite][72] any [sources][2]**. Please help [improve this section][3] by [adding citations to reliable sources][4]. Unsourced material may be challenged and [removed][5].*( March 2025)**( [Learn how and when to remove this message][12])*

 |

Inverse distributions are widely used as prior distributions in Bayesian inference for scale parameters.

## See also

[[edit][73]]

- [Harmonic mean][74]
- [Ratio distribution][22]
- [Self-reciprocal distributions][75]

## References

[[edit][76]]

1. ↑ [Hamming R. W.][77] (1970) ["On the distribution of numbers"][78] [Archived][79] 2013-10-29 at the [Wayback Machine][80], *The Bell System Technical Journal*49(8) 1609–1625
2. 1 2 3 Johnson, Norman L.; Kotz, Samuel; Balakrishnan, Narayanaswamy (1994). *Continuous Univariate Distributions, Volume 1*. Wiley. p. 171. [ISBN][81] [0-471-58495-9][82].
3. ↑ [Hayya, Jack][83]; Armstrong, Donald; Gressis, Nicolas (July 1975). "A Note on the Ratio of Two Normally Distributed Variables". *[Management Science][84]*. **21**(11): 1338– 1341. [doi][85]: [10.1287/mnsc.21.11.1338][86]. [JSTOR][87] [2629897][88].
4. 1 2 Lecomte, Christophe (May 2013). "Exact statistics of systems with uncertainties: an analytical theory of rank-one stochastic dynamic systems". *Journal of Sound and Vibration*. **332**(11): 2750– 2776. [doi][85]: [10.1016/j.jsv.2012.12.009][89].
5. ↑ Lecomte, Christophe (May 2013). "Exact statistics of systems with uncertainties: an analytical theory of rank-one stochastic dynamic systems". *Journal of Sound and Vibration*. **332**(11). Section (4.1.1). [doi][85]: [10.1016/j.jsv.2012.12.009][89].
6. ↑ Lecomte, Christophe (May 2013). "Exact statistics of systems with uncertainties: an analytical theory of rank-one stochastic dynamic systems". *Journal of Sound and Vibration*. **332**(11). Eq.(39)-(40). [doi][85]: [10.1016/j.jsv.2012.12.009][89].
7. ↑ Cribari-Neto F, Lopes Garcia N, Vasconcellos KLP (2000) A note on inverse moments of binomial variates. Brazilian Review of Econometrics 20 (2)

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Inverse_distribution&oldid=1317936750][90] "

[Categories][91]:

- [Algebra of random variables][92]
- [Types of probability distributions][93]

Hidden categories:

- [Articles with short description][94]
- [Short description matches Wikidata][95]
- [Articles needing additional references from March 2025][96]
- [All articles needing additional references][97]
- [Webarchive template wayback links][98]
- [All articles with unsourced statements][99]
- [Articles with unsourced statements from April 2013][100]

Search

Inverse distribution

2 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/File:Question_book-new.svg
[2]: https://en.wikipedia.org/wiki/Wikipedia:Verifiability
[3]: https://en.wikipedia.org/wiki/Special:EditPage/Inverse_distribution
[4]: https://en.wikipedia.org/wiki/Help:Referencing_for_beginners
[5]: https://en.wikipedia.org/wiki/Wikipedia:Verifiability#Burden_of_evidence
[6]: https://www.google.com/search?as_eq=wikipedia&amp;q=%22Inverse+distribution%22
[7]: https://www.google.com/search?tbm=nws&amp;q=%22Inverse+distribution%22+-wikipedia&amp;tbs=ar:1
[8]: https://www.google.com/search?amp;q=%22Inverse+distribution%22&amp;tbs=bkt:s&amp;tbm=bks
[9]: https://www.google.com/search?tbs=bks:1&amp;q=%22Inverse+distribution%22+-wikipedia
[10]: https://scholar.google.com/scholar?q=%22Inverse+distribution%22
[11]: https://www.jstor.org/action/doBasicSearch?Query=%22Inverse+distribution%22&amp;acc=on&amp;wc=on
[12]: https://en.wikipedia.org/wiki/Help:Maintenance_template_removal
[13]: https://en.wikipedia.org/wiki/Inverse_distribution_function
[14]: https://en.wikipedia.org/wiki/Probability_theory
[15]: https://en.wikipedia.org/wiki/Statistics
[16]: https://en.wikipedia.org/wiki/Multiplicative_inverse
[17]: https://en.wikipedia.org/wiki/Bayesian_inference
[18]: https://en.wikipedia.org/wiki/Prior_distribution
[19]: https://en.wikipedia.org/wiki/Posterior_distribution
[20]: https://en.wikipedia.org/wiki/Scale_parameter
[21]: https://en.wikipedia.org/wiki/Algebra_of_random_variables
[22]: https://en.wikipedia.org/wiki/Ratio_distribution
[23]: https://en.wikipedia.org/wiki/Degenerate_distribution
[24]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=1
[25]: https://en.wikipedia.org/wiki/Probability_distribution
[26]: https://en.wikipedia.org/wiki/Continuous_probability_distribution
[27]: https://en.wikipedia.org/wiki/Probability_density_function
[28]: https://en.wikipedia.org/wiki/Cumulative_distribution_function
[29]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=2
[30]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=3
[31]: https://en.wikipedia.org/wiki/Reciprocal_distribution
[32]: https://en.wikipedia.org/wiki/Proportionality_(mathematics)
[33]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=4
[34]: https://en.wikipedia.org/wiki/Statistical_parameter
[35]: https://en.wikipedia.org/wiki/Support_(mathematics)
[36]: https://en.wikipedia.org/wiki/Expected_value
[37]: https://en.wikipedia.org/wiki/Median
[38]: https://en.wikipedia.org/wiki/Variance
[39]: https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)
[40]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=5
[41]: https://en.wikipedia.org/wiki/Student's_t-distribution
[42]: https://en.wikipedia.org/wiki/Degrees_of_freedom
[43]: https://en.wikipedia.org/wiki/Cauchy_distribution
[44]: https://en.wikipedia.org/wiki/Bimodal
[45]: https://en.wikipedia.org/wiki/Wikipedia:Citation_needed
[46]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=6
[47]: https://en.wikipedia.org/wiki/Propagation_of_uncertainty#Reciprocal_and_shifted_reciprocal
[48]: https://en.wikipedia.org/wiki/Normal_distribution
[49]: https://en.wikipedia.org/wiki/File:Graph_of_inverse_of_the_normal_distribution.png
[50]: https://en.wikipedia.org/wiki/Standard_normal_distribution
[51]: https://en.wikipedia.org/wiki/Heavy-tailed_distribution
[52]: https://en.wikipedia.org/wiki/Bimodal_distribution
[53]: https://en.wikipedia.org/wiki/Monte_Carlo_simulation
[54]: https://en.wikipedia.org/wiki/Principal_value
[55]: https://en.wikipedia.org/wiki/Dawson's_function
[56]: https://en.wikipedia.org/wiki/Faddeeva_function
[57]: https://en.wikipedia.org/wiki/Complex_normal_variable
[58]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=7
[59]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=8
[60]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=9
[61]: https://en.wikipedia.org/wiki/F_distribution
[62]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=10
[63]: https://en.wikipedia.org/wiki/Big_O_notation
[64]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=11
[65]: https://en.wikipedia.org/wiki/Triangular_distribution
[66]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=12
[67]: https://en.wikipedia.org/wiki/Inverse-chi-squared_distribution
[68]: https://en.wikipedia.org/wiki/Inverse-gamma_distribution
[69]: https://en.wikipedia.org/wiki/Inverse-Wishart_distribution
[70]: https://en.wikipedia.org/wiki/Inverse_matrix_gamma_distribution
[71]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=13
[72]: https://en.wikipedia.org/wiki/Wikipedia:Citing_sources
[73]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=14
[74]: https://en.wikipedia.org/wiki/Harmonic_mean
[75]: https://en.wikipedia.org/wiki/Relationships_among_probability_distributions#Reciprocal_of_a_random_variable
[76]: /w/index.php?title=Inverse_distribution&amp;action=edit&amp;section=15
[77]: https://en.wikipedia.org/wiki/Richard_Hamming
[78]: http://lucent.com/bstj/vol49-1970/articles/bstj49-8-1609.pdf
[79]: https://web.archive.org/web/20131029201817/http://lucent.com/bstj/vol49-1970/articles/bstj49-8-1609.pdf
[80]: https://en.wikipedia.org/wiki/Wayback_Machine
[81]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[82]: https://en.wikipedia.org/wiki/Special:BookSources/0-471-58495-9
[83]: https://en.wikipedia.org/wiki/Jack_Hayya
[84]: https://en.wikipedia.org/wiki/Management_Science_(journal)
[85]: https://en.wikipedia.org/wiki/Doi_(identifier)
[86]: https://doi.org/10.1287%2Fmnsc.21.11.1338
[87]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[88]: https://www.jstor.org/stable/2629897
[89]: https://doi.org/10.1016%2Fj.jsv.2012.12.009
[90]: https://en.wikipedia.org/w/index.php?title=Inverse_distribution&amp;oldid=1317936750
[91]: /wiki/Help:Category
[92]: /wiki/Category:Algebra_of_random_variables
[93]: /wiki/Category:Types_of_probability_distributions
[94]: /wiki/Category:Articles_with_short_description
[95]: /wiki/Category:Short_description_matches_Wikidata
[96]: /wiki/Category:Articles_needing_additional_references_from_March_2025
[97]: /wiki/Category:All_articles_needing_additional_references
[98]: /wiki/Category:Webarchive_template_wayback_links
[99]: /wiki/Category:All_articles_with_unsourced_statements
[100]: /wiki/Category:Articles_with_unsourced_statements_from_April_2013
