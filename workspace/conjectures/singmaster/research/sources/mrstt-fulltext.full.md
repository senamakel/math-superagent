<!-- source: https://arxiv.org/html/2106.03335v1 | converted from HTML -->

Singmaster’s conjecture in the interior of Pascal’s triangle

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2106.03335v1 [math.NT] 07 Jun 2021

# Singmaster’s conjecture in the interior of Pascal’s triangle

Kaisa Matomäki Address: Department of Mathematics and Statistics
University of Turku, 20014 Turku
Finland Email address: [ksmato@utu.fi][3], Maksym Radziwiłł Address: Department of Mathematics, Caltech, 1200 E California Blvd, Pasadena, CA, 91125
USA Email address: [maksym.radziwill@gmail.com][4], Xuancheng Shao Address: Department of Mathematics, University of Kentucky
715 Patterson Office Tower
Lexington, KY 40506
USA Email address: [xuancheng.shao@uky.edu][5], Terence Tao Address: Department of Mathematics, UCLA
405 Hilgard Ave
Los Angeles CA 90095
USA Email address: [tao@math.ucla.edu][6] and Joni Teräväinen Address: Mathematical Institute, University of Oxford
Woodstock Road
Oxford OX2 6GG
United Kingdom Email address: [joni.teravainen@maths.ox.ac.uk][7]

###### Abstract.

Singmaster’s conjecture asserts that every natural number greater than one occurs at most a bounded number of times in Pascal’s triangle; that is, for any natural number t ≥ 2 t\geq 2, the number of solutions to the equation ( n m) = t \binom{n}{m}=t for natural numbers 1 ≤ m < n 1\leq m<n is bounded. In this paper we establish this result in the interior region exp ⁡ ( log 2 / 3 + ε ⁡ n) ≤ m ≤ n − exp ⁡ ( log 2 / 3 + ε ⁡ n) \exp(\log^{2/3+\varepsilon}n)\leq m\leq n-\exp(\log^{2/3+\varepsilon}n) for any fixed ε > 0 \varepsilon>0. Indeed, when t t is sufficiently large depending on ε \varepsilon, we show that there are at most four solutions (or at most two in either half of Pascal’s triangle) in this region. We also establish analogous results for the equation ( n) m = t (n)_{m}=t, where ( n) m ≔ n ⁡ ( n − 1) ​ … ​ ( n − m + 1) (n)_{m}\coloneqq n(n-1)\dots(n-m+1) denotes the falling factorial.

## 1. Introduction

In 1971, Singmaster [22] conjectured that any natural number greater than one only appeared in Pascal’s triangle a bounded number of times. In asymptotic notation 1 1 1 Our conventions for asymptotic notation are set out in Section 1.5., we can express this conjecture as

###### Conjecture 1.1 (Singmaster’s conjecture).

For any natural number t ≥ 2 t\geq 2, the number of integer solutions 1 ≤ m < n 1\leq m<n to the equation

(1.1) |  | ( n m) = t \binom{n}{m}=t |  |

is O ⁡ ( 1) O(1).

Note that we can exclude the edges m = 0, m = n m=0,m=n of Pascal’s triangle from consideration since ( n m) = 1 \binom{n}{m}=1 in these cases. Currently the largest known number of solutions to ( 1.1) for a given t t is eight, arising from t = 3003 t=3003 and

(1.2) |  | ( n, m) = ( 3003, 1), ( 78, 2), ( 15, 5), ( 14, 6), ( 14, 8), ( 15, 10), ( 78, 76), ( 3003, 3002). (n,m)=(3003,1),(78,2),(15,5),(14,6),(14,8),(15,10),(78,76),(3003,3002). |  |

For the purposes of attacking this conjecture, we may of course assume t t to be larger than any given absolute constant, which we shall implicitly do in the sequel. In particular we can assume that the iterated logarithms

 | log 2 ⁡ t ≔ log ⁡ log ⁡ t; log 3 ⁡ t ≔ log ⁡ log ⁡ log ⁡ t \log_{2}t\coloneqq\log\log t;\quad\log_{3}t\coloneqq\log\log\log t |  |

are well-defined and positive.

In view of the symmetry

(1.3) |  | ( n m) = ( n n − m) \binom{n}{m}=\binom{n}{n-m} |  |

we may restrict attention to the left half

(1.4) |  | { ( m, n) ∈ ℕ × ℕ: 1 ≤ m ≤ n / 2 } \{(m,n)\in\mathbb{N}\times\mathbb{N}:1\leq m\leq n/2\} |  |

of Pascal’s triangle. For solutions to ( 1.1) in this half ( 1.4) of the triangle, we have

 | t = ( n m) ≥ ( 2 ​ m m) ≍ 4 m / m t=\binom{n}{m}\geq\binom{2m}{m}\asymp 4^{m}/\sqrt{m} |  |

by Stirling’s approximation ( 2.4), and thus we have the upper bound

(1.5) |  | m ≤ 1 log ⁡ 4 ​ log ⁡ t + O ⁡ ( log 2 ⁡ t). m\leq\frac{1}{\log 4}\log t+O(\log_{2}t). |  |

Since n ↦ ( n m) n\mapsto\binom{n}{m} is an increasing function of n n for fixed m ≥ 1 m\geq 1, n n is uniquely determined by m m and t t. Thus by ( 1.5) we have at most O ⁡ ( log ⁡ t) O(\log t) solutions to the equation ( n m) = t \binom{n}{m}=t, a fact already observed in the original paper [22] of Singmaster. This bound was improved to O ⁡ ( log ⁡ t / log 2 ⁡ t) O(\log t/\log_{2}t) by Abbott, Erdős, and Hansen [1], to O ⁡ ( log ⁡ t ​ log 3 ​ t / log 2 2 ​ t) O(\log t\log_{3}t/\log_{2}^{2}t) by Kane [14], and finally to O ⁡ ( log ⁡ t ​ log 3 ​ t / log 2 3 ​ t) O(\log t\log_{3}t/\log_{2}^{3}t) in a followup work of Kane [15]. This remains the best known unconditional bound for the total number of solutions, although it was observed in [1] that the improved bound O ε ​ ( log 2 / 3 + ε ⁡ t) O_{\varepsilon}(\log^{2/3+\varepsilon}t) was available for any ε > 0 \varepsilon>0 assuming the conjecture of Cramér [9].

From the elementary inequalities

 | ( n − m) m m! < ( n m) ≤ n m m! \frac{(n-m)^{m}}{m!}<\binom{n}{m}\leq\frac{n^{m}}{m!} |  |

and some rearranging we see that any solution to ( n m) = t \binom{n}{m}=t obeys the bounds

 | ( t ​ m!) 1 / m ≤ n < ( t ​ m!) 1 / m + m. (tm!)^{1/m}\leq n<(tm!)^{1/m}+m. |  |

Applying Stirling’s approximation ( 2.4) (and also n ≥ m n\geq m) we can thus obtain the order of magnitude of n n as a function of m m and t t:

(1.6) |  | n ≍ m ​ t 1 / m n\asymp mt^{1/m} |  |

or equivalently

(1.7) |  | n m ≍ exp ⁡ ( log ⁡ t m). \frac{n}{m}\asymp\exp\left(\frac{\log t}{m}\right). |  |

In particular we see that n n grows extremely rapidly when the ratio m / log ⁡ t m/\log t becomes small. This makes the difficulty of the problem increase as m / log ⁡ t m/\log t approaches zero, and indeed treating the case of small values of m / log ⁡ t m/\log t is the main obstruction to making further progress on bounding the total number of solutions.

###### Remark 1.2.

In the left half ( 1.4) of Pascal’s triangle, a finer application of Stirling’s approximation in [14, (3.1)] gave the more precise estimate

 | n = ( t m!) 1 / m + m − 1 2 + O ( m t − 1 / m). n=(tm!)^{1/m}+\frac{m-1}{2}+O(mt^{-1/m}). |  |

We will not explicitly use this estimate here.

In this paper we study the opposite regime in which m / log ⁡ t m/\log t is relatively large, or equivalently (by ( 1.7)) n n and m m are somewhat comparable (in the doubly logarithmic sense log 2 ⁡ n ≍ log 2 ⁡ m \log_{2}n\asymp\log_{2}m). More precisely, we have the following result:

###### Theorem 1.3 (Singmaster’s conjecture in the interior of Pascal’s triangle).

Let 0 < ε < 1 0<\varepsilon<1, and assume that t t is sufficiently large depending on ε \varepsilon. Then there are at most two solutions to ( 1.1) in the region exp ⁡ ( log 2 / 3 + ε ⁡ n) ≤ m ≤ n / 2 \exp(\log^{2/3+\varepsilon}n)\leq m\leq n/2. By ( 1.3), we thus have at most four solutions to ( 1.1) in the region exp ⁡ ( log 2 / 3 + ε ⁡ n) ≤ m ≤ n − exp ⁡ ( log 2 / 3 + ε ⁡ n) \exp(\log^{2/3+\varepsilon}n)\leq m\leq n-\exp(\log^{2/3+\varepsilon}n). Furthermore, in the smaller region exp ⁡ ( log 2 / 3 + ε ⁡ n) ≤ m ≤ n / exp ⁡ ( log 1 − ε ′ ⁡ n) \exp(\log^{2/3+\varepsilon}n)\leq m\leq n/\exp(\log^{1-\varepsilon^{\prime}}n) there is at most one solution, whenever 0 < ε ′ < ε 2 / 3 + ε 0<\varepsilon^{\prime}<\frac{\varepsilon}{2/3+\varepsilon} and t t is sufficiently large depending on both ε \varepsilon and ε ′ \varepsilon^{\prime}.

###### Remark 1.4.

The bound of two (or four) solutions is absolutely sharp, in view of the infinite family of solutions observed in [18], [23], [27] to the equation

 | ( n + 1 m + 1) = ( n m + 2) \binom{n+1}{m+1}=\binom{n}{m+2} |  |

given by n = F 2 ​ j + 2 ​ F 2 ​ j + 3 − 1 n=F_{2j+2}F_{2j+3}-1, m = F 2 ​ j ​ F 2 ​ j + 3 − 1 m=F_{2j}F_{2j+3}-1, where F j F_{j} denotes the j t ​ h j^{th} Fibonacci number. See also [13] for further analysis of equations of this type. Besides this infinite family of collisions, and the “trivial” ones generated by ( 1.3), ( n 0) = 1 \binom{n}{0}=1, and ( n m) = ( ( n m) 1) \binom{n}{m}=\binom{\binom{n}{m}}{1}, the only further known collisions between binomial coefficients arise from the identities ( n 2) = ( n ′ m ′) \binom{n}{2}=\binom{n^{\prime}}{m^{\prime}} for

 | ( n, n ′, m ′) = ( 16, 10, 3), ( 21, 2, 4), ( 52, 22, 3), ( 120, 36, 3), ( 153, 19, 5), ( 221, 17, 8) (n,n^{\prime},m^{\prime})=(16,10,3),(21,2,4),(52,22,3),(120,36,3),(153,19,5),(221,17,8) |  |

as well as the example in ( 1.2). It was conjectured by de Weger [11] that these above examples generate all the non-trivial collisions ( n m) = ( n ′ m ′) = t \binom{n}{m}=\binom{n^{\prime}}{m^{\prime}}=t; this would of course imply Singmaster’s conjecture. This conjecture has been verified for ( m, m ′) = ( 2, 3) (m,m^{\prime})=(2,3) [3], for ( m, m ′) = ( 2, 4) (m,m^{\prime})=(2,4) [21], [10], for ( m, m ′) = ( 2, 5) (m,m^{\prime})=(2,5) [8], for ( m, m ′) = ( 3, 4) (m,m^{\prime})=(3,4) [20], [11], and ( m, m ′) = ( 2, 6), ( 2, 8), ( 3, 6), ( 4, 6), ( 4, 8) (m,m^{\prime})=(2,6),(2,8),(3,6),(4,6),(4,8) [26], and for n ≤ 10 6 n\leq 10^{6} or t ≤ 10 60 t\leq 10^{60} in [5].

###### Remark 1.5.

In view of Theorem 1.3, we now see that to prove Conjecture 1.1, we may restrict attention without loss of generality to the region 2 ≤ m ≤ exp ⁡ ( log 2 / 3 + ε ⁡ n) 2\leq m\leq\exp(\log^{2/3+\varepsilon}n) for any fixed ε > 0 \varepsilon>0, or equivalently (by ( 1.7)) to 2 ≤ m ≤ log ⁡ t log 2 3 / 2 − ε ​ t 2\leq m\leq\frac{\log t}{\log^{3/2-\varepsilon}_{2}t} for any fixed ε > 0 \varepsilon>0. It follows from the conjecture of de Weger [11] mentioned in Remark 1.4 that for t t sufficiently large there is only at most one solution in this region, that is to say all but a finite number of binomial coefficients ( n m) \binom{n}{m} for 2 ≤ m ≤ exp ⁡ ( log 2 / 3 + ε ⁡ n) 2\leq m\leq\exp(\log^{2/3+\varepsilon}n) are distinct. In this direction, the number of solutions to the equation ( n m) = ( n ′ m ′) \binom{n}{m}=\binom{n^{\prime}}{m^{\prime}} for fixed 2 ≤ m < m ′ 2\leq m<m^{\prime} has been shown (via Siegel’s theorem on integral points) to be finite in [4] (see also the earlier result [16] treating the case ( m, m ′) = ( 2, p) (m,m^{\prime})=(2,p) for an odd prime p p). This implies that there are no collisions in the regime 2 ≤ m ≤ w ⁡ ( n) 2\leq m\leq w(n) if w w is a function of n n that goes to infinity sufficiently slowly as n → ∞ n\to\infty. Unfortunately, due to the reliance on Siegel’s theorem, the function w w given by these arguments is completely ineffective.

###### Remark 1.6.

For some previous bounds of this type, in [1] it was shown that the number of solutions to ( 1.1) in the range n 5 / 6 ≤ m ≤ n / 2 n^{5/6}\leq m\leq n/2 was O ⁡ ( log 3 / 4 ⁡ t) O(\log^{3/4}t), while the arguments in [14, §7], after some manipulation, show that the number of solutions to ( 1.1) in the range exp ⁡ ( log 1 / 2 + ε ⁡ n) ≤ m ≤ n 5 / 6 \exp(\log^{1/2+\varepsilon}n)\leq m\leq n^{5/6} is O ε ​ ( log ⁡ t / log 2 3 ​ t) O_{\varepsilon}(\log t/\log_{2}^{3}t).

###### Remark 1.7.

The implied quantitative bounds in the hypothesis “ t t is sufficiently large depending on ε \varepsilon ” are effective; however, we have made no attempt whatsoever to optimize them in this paper, and will likely be too large to be of use in numerical verification of Singmaster’s conjecture in their current form.

### 1.1. An analog for falling factorials

The methods used to handle the equation ( 1.1) can be modified to treat the variant equation

(1.8) |  | ( n) m = t (n)_{m}=t |  |

for integers 1 ≤ m < n 1\leq m<n and t ≥ 2 t\geq 2, where ( n) m (n)_{m} denotes the falling factorial

 | ( n) m ≔ n ⁡ ( n − 1) ​ … ​ ( n − m + 1) = m! ​ ( n m). (n)_{m}\coloneqq n(n-1)\dots(n-m+1)=m!\binom{n}{m}. |  |

We exclude the cases m = 0, m = n m=0,m=n since ( n) 0 = 1 (n)_{0}=1 and ( n) n = ( n) n − 1 = n! (n)_{n}=(n)_{n-1}=n!. In [1, Theorem 4] it was shown that for any t ≥ 2 t\geq 2 the number of integer solutions ( m, n) (m,n) to ( 1.8) with 1 ≤ m ≤ n − 1 1\leq m\leq n-1 is O ⁡ ( log ⁡ t) O(\sqrt{\log t}). We do not directly improve upon this bound here, but can obtain an analogue of Theorem 1.3:

###### Theorem 1.8 (Falling factorial multiplicity in the interior).

Let 0 < ε < 1 0<\varepsilon<1, and assume that t t is sufficiently large depending on ε \varepsilon. Then there are at most two integer solutions to ( 1.8) in the region exp ⁡ ( log 2 / 3 + ε ⁡ n) ≤ m < n \exp(\log^{2/3+\varepsilon}n)\leq m<n.

We establish this result in Section 5. Note that the bound of two is best possible, as can be seen from the infinite family of solutions

 | ( a 2 − a) a 2 − 2 ​ a = ( a 2 − a − 1) a 2 − 2 ​ a + 1 (a^{2}-a)_{a^{2}-2a}=(a^{2}-a-1)_{a^{2}-2a+1} |  |

for any integer a > 2 a>2, and more generally

 | ( ( a) b) ( a) b − a = ( ( a) b − 1) ( a) b − a + b − 1 ((a)_{b})_{(a)_{b}-a}=((a)_{b}-1)_{(a)_{b}-a+b-1} |  |

whenever 2 ≤ b < a 2\leq b<a are integers.

### 1.2. Strategy of proof

Theorem 1.3 is a consequence of two Propositions that we now describe. The proof of Theorem 1.8 will follow a similar pattern as described here and we refer the reader to Section 5 for details.

###### Proposition 1.9 (Distance estimate).

Let ε > 0 \varepsilon>0. Suppose we have two solutions ( n, m), ( n ′, m ′) (n,m),(n^{\prime},m^{\prime}) to ( 1.1) in the left half ( 1.4) of Pascal’s triangle. Then one has

 | m ′ − m ≪ ε exp ( log 2 / 3 + ε ( n + n ′)) m^{\prime}-m\ll_{\varepsilon}\exp(\log^{2/3+\varepsilon}(n+n^{\prime})) |  |

for any ε > 0 \varepsilon>0. Furthermore, if

 | m, m ′ ≥ exp ⁡ ( log 2 / 3 + ε ⁡ ( n + n ′)) m,m^{\prime}\geq\exp(\log^{2/3+\varepsilon}(n+n^{\prime})) |  |

then we additionally have

 | n ′ − n ≪ ε exp ( log 2 / 3 + ε ( n + n ′)). n^{\prime}-n\ll_{\varepsilon}\exp(\log^{2/3+\varepsilon}(n+n^{\prime})). |  |

Note how this proposition is consistent with the example in Remark 1.4. We shall discuss the proof of Proposition 1.9 in Section 1.3. For the application to Theorem 1.3, Proposition 1.9 localizes all solutions to ( 1.1) to a region of small diameter. To conclude Theorem 1.3, we can now proceed by adapting the Taylor expansion arguments of Kane [14], [15], in which one views n n as an analytic function of m m (keeping t t fixed) and exploits the non-vanishing of certain derivatives of this function; see Section 2. This is what the proposition below accomplishes. In fact in our analysis only two derivatives of this function are needed (i.e., we only need to exploit the convexity properties of n n as a function of m m).

###### Proposition 1.10 (Kane-type estimate).

Let ε > 0 \varepsilon>0. Suppose that ( n, m) (n,m) is a solution to ( 1.1) in the left-half ( 1.4) of Pascal’s triangle. There there exists at most one other solution ( n ′, m ′) ≠ ( n, m) (n^{\prime},m^{\prime})\neq(n,m) to ( 1.1) with m ′ < m m^{\prime}<m, n ′ > n n^{\prime}>n and

 | | m − m ′ | + | n − n ′ | ≪ exp ⁡ ( ( log 2 ⁡ t) 1 − ε). |m-m^{\prime}|+|n-n^{\prime}|\ll\exp((\log_{2}t)^{1-\varepsilon}). |  |

With these two Propositions at hand it is easy to deduce Theorem 1.3.

###### Deduction of Theorem 1.3.

Let ε > 0 \varepsilon>0, let t t be sufficiently large depending on ε \varepsilon, and let ( n, m) (n,m) be the solution to ( 1.1) in the region

(1.9) |  | { ( n, m): exp ⁡ ( log 2 / 3 + ε ⁡ n) ≤ m ≤ n / 2 } \{(n,m):\exp(\log^{2/3+\varepsilon}n)\leq m\leq n/2\} |  |

with the maximal value of m m (if there are no such solutions then of course Theorem 1.3 is trivial). For brevity we allow all implied constants in the following arguments to depend on ε \varepsilon. If ( n ′, m ′) (n^{\prime},m^{\prime}) is any other solution in this region, then m ′ < m m^{\prime}<m and n ′ > n n^{\prime}>n. From ( 1.7) we have

 | m ≫ log ⁡ t log ⁡ n ≥ log ⁡ t log 1 2 / 3 + ε ⁡ m ≫ log ⁡ t log 2 1 2 / 3 + ε ​ t m\gg\frac{\log t}{\log n}\geq\frac{\log t}{\log^{\frac{1}{2/3+\varepsilon}}m}\gg\frac{\log t}{\log_{2}^{\frac{1}{2/3+\varepsilon}}t} |  |

thanks to ( 1.5). From further application of ( 1.7) we then have

 | n ≪ exp ⁡ ( O ⁡ ( log 2 1 2 / 3 + ε ​ t)). n\ll\exp(O(\log_{2}^{\frac{1}{2/3+\varepsilon}}t)). |  |

Similarly for n ′ n^{\prime}. Applying Proposition 1.9 (with ε \varepsilon replaced by a sufficiently small quantity), we conclude that

(1.10) |  | m − m ′, n ′ − n ≪ ε ′ exp ( O ( log 2 1 − ε ′ t)) m-m^{\prime},n^{\prime}-n\ll_{\varepsilon^{\prime}}\exp(O(\log^{1-\varepsilon^{\prime}}_{2}t)) |  |

whenever 1 − ε ′ > 2 / 3 2 / 3 + ε 1-\varepsilon^{\prime}>\frac{2/3}{2/3+\varepsilon}, or equivalently ε ′ < ε 2 / 3 + ε \varepsilon^{\prime}<\frac{\varepsilon}{2/3+\varepsilon}. The result now follows from Proposition 1.10. ∎

###### Remark 1.11.

The above arguments showed that for t t sufficiently large depending on ε \varepsilon, there were at most four solutions to ( 1.1) in the region exp ⁡ ( log 2 / 3 + ε ⁡ n) ≤ m ≤ n − exp ⁡ ( log 2 / 3 + ε ⁡ n) \exp(\log^{2/3+\varepsilon}n)\leq m\leq n-\exp(\log^{2/3+\varepsilon}n). A modification of the argument also shows that there cannot be exactly *three*such solutions. For if this were the case, we see from ( 1.3) that there must be a solution ( n, m) (n,m) with n = 2 ​ m n=2m, so that m ≍ log ⁡ t m\asymp\log t by Stirling’s approximation. For all other solutions ( n ′, m ′) (n^{\prime},m^{\prime}) to ( 1.1) we have n ′ ≥ n + 1 n^{\prime}\geq n+1, hence

 | ( n n / 2) = t = ( n ′ m ′) ≥ ( n + 1 m ′) \binom{n}{n/2}=t=\binom{n^{\prime}}{m^{\prime}}\geq\binom{n+1}{m^{\prime}} |  |

and hence (by Stirling’s approximation)

 | ( n + 1 m ′) ≤ ( 1 2 + O ⁡ ( 1 n)) ​ ( n + 1 ( n + 1) / 2). \binom{n+1}{m^{\prime}}\leq\left(\frac{1}{2}+O\left(\frac{1}{n}\right)\right)\binom{n+1}{(n+1)/2}. |  |

By Stirling’s approximation (or the central limit theorem of de Moivre and Laplace) this forces | m ′ − n + 1 2 | ≫ n |m^{\prime}-\frac{n+1}{2}|\gg\sqrt{n}, thus | m ′ − m | ≫ m 1 / 2 |m^{\prime}-m|\gg m^{1/2}. But this contradicts ( 1.10).

### 1.3. Proof methods

We now discuss the method of proof of Proposition 1.9, which is our main new contribution. In contrast to the “Archimedean” arguments of Kane (such as Proposition 1.10) that use real and complex analysis of the binomial coefficients ( n m) \binom{n}{m}, the proof of Proposition 1.9 relies more on “non-Archimedean” arguments, based on evaluating the p p -adic valuations v p ​ ( ( n m)) v_{p}\left(\binom{n}{m}\right) for various primes p p, defined as the number of times p p divides ( n m) \binom{n}{m}. From the classical Legendre formula

(1.11) |  | v p ​ ( n!) = ∑ j = 1 ∞ ⌊ n p j ⌋, v_{p}(n!)=\sum_{j=1}^{\infty}\left\lfloor\frac{n}{p^{j}}\right\rfloor, |  |

where ⌊ x ⌋ \lfloor x\rfloor is the integer part of x x, we see that

(1.12) |  | v p ​ ( ( n m)) = ∑ j = 1 ∞ ( ⌊ n p j ⌋ − ⌊ m p j ⌋ − ⌊ n − m p j ⌋) = ∑ j = 1 ∞ ( { m p j } + { n − m p j } − { n p j }) \begin{split}v_{p}\left(\binom{n}{m}\right)&=\sum_{j=1}^{\infty}\left(\left\lfloor\frac{n}{p^{j}}\right\rfloor-\left\lfloor\frac{m}{p^{j}}\right\rfloor-\left\lfloor\frac{n-m}{p^{j}}\right\rfloor\right)\\ &=\sum_{j=1}^{\infty}\left(\left\{\frac{m}{p^{j}}\right\}+\left\{\frac{n-m}{p^{j}}\right\}-\left\{\frac{n}{p^{j}}\right\}\right)\end{split} |  |

where { x } ≔ x − ⌊ x ⌋ \{x\}\coloneqq x-\lfloor x\rfloor denotes the fractional part of x x. Note that the summands here vanish whenever p j > n p^{j}>n. From this identity we see that if ( n, m), ( n ′, m ′) (n,m),(n^{\prime},m^{\prime}) are two solutions to ( 1.1) then we must have

(1.13) |  | ∑ j = 1 ∞ ( { m p j } + { n − m p j } − { n p j }) = ∑ j = 1 ∞ ( { m ′ p j } + { n ′ − m ′ p j } − { n ′ p j }) \sum_{j=1}^{\infty}\left(\left\{\frac{m}{p^{j}}\right\}+\left\{\frac{n-m}{p^{j}}\right\}-\left\{\frac{n}{p^{j}}\right\}\right)=\sum_{j=1}^{\infty}\left(\left\{\frac{m^{\prime}}{p^{j}}\right\}+\left\{\frac{n^{\prime}-m^{\prime}}{p^{j}}\right\}-\left\{\frac{n^{\prime}}{p^{j}}\right\}\right) |  |

for all primes p p. Our strategy will be to apply this equation with p p set equal to a *random*prime 𝐩 \mathbf{p} drawn uniformly amongst all primes in the interval [P, P + P ​ log − 100 ​ P] [P,P+P\log^{-100}P] where the scale P P is something like exp ⁡ ( log 2 / 3 + ε / 2 ⁡ ( n + n ′)) \exp(\log^{2/3+\varepsilon/2}(n+n^{\prime})), and inspect the distribution of the resulting random variables on the left and right-hand sides of ( 1.13) in order to obtain a contradiction when m, m ′ m,m^{\prime} or n, n ′ n,n^{\prime} are sufficiently well separated. In order to do this we need some information concerning the equidistribution of fractional parts such as { n 𝐩 j } \{\frac{n}{\mathbf{p}^{j}}\}. This will be provided by the following estimate, proven in Section 4. There and later the letter p p always denotes a prime.

###### Proposition 1.12 (Equidistribution estimate).

Let ε > 0 \varepsilon>0 and P ≥ 2 P\geq 2 and let I I be an interval contained in [P, 2 ​ P] [P,2P]. Let M, N M,N be real numbers with M, N = O ⁡ ( exp ⁡ ( log 3 / 2 − ε ⁡ P)) M,N=O(\exp(\log^{3/2-\varepsilon}P)), and let j j be a natural number.

- (i)

For all A > 0 A>0,

 | ∑ p ∈ I e ⁡ ( N p + M p j) = ∫ I e ⁡ ( N t + M t j) ​ d ​ t log ⁡ t + O ε, A ​ ( P ​ log − A ​ P). \sum_{p\in I}e\left(\frac{N}{p}+\frac{M}{p^{j}}\right)=\int_{I}e\left(\frac{N}{t}+\frac{M}{t^{j}}\right)\ \frac{dt}{\log t}+O_{\varepsilon,A}(P\log^{-A}P). |  |

- (ii)

Let W: ℝ 2 → ℂ W\colon\mathbb{R}^{2}\to\mathbb{C} be a smooth ℤ 2 \mathbb{Z}^{2} -periodic function. Then, for all A > 0 A>0,

 | ∑ p ∈ I W ⁡ ( N p, M p j) = ∫ I W ⁡ ( N t, M t j) ​ d ​ t log ⁡ t + O ε, A ​ ( ‖ W ‖ C 3 ​ P ​ log − A ​ P), \sum_{p\in I}W\left(\frac{N}{p},\frac{M}{p^{j}}\right)=\int_{I}W\left(\frac{N}{t},\frac{M}{t^{j}}\right)\ \frac{dt}{\log t}+O_{\varepsilon,A}(\|W\|_{C^{3}}P\log^{-A}P), |  |

where

 | ‖ W ‖ C 3 ≔ ∑ j = 0 3 sup x ∈ ℝ 2 | ∇ j W ​ ( x) |. \|W\|_{C^{3}}\coloneqq\sum_{j=0}^{3}\sup_{x\in\mathbb{R}^{2}}|\nabla^{j}W(x)|. |  |

One can generalize this proposition to control the joint equidistribution of any bounded number of expressions of the form { n p j } \{\frac{n}{p^{j}}\}, but for our applications it will suffice to understand the equidistribution of pairs { N p } \{\frac{N}{p}\}, { M p j } \{\frac{M}{p^{j}}\}.

When it comes to the proof of Proposition 1.12, the first step is to use Fourier expansion to reduce part (ii) of the proposition to part (i). For part (i), the case where | N | P + | M | P j \frac{|N|}{P}+\frac{|M|}{P^{j}} is small (say ≤ log O ⁡ ( A) ⁡ P \leq\log^{O(A)}P) is easily handled using the prime number theorem with classical error term. In the regime where | N | P + | M | P j \frac{|N|}{P}+\frac{|M|}{P^{j}} is large, we use Vaughan’s identity to decompose the sum in (i) into type I and II sums, and assert that these exhibit cancellation; the type I and II bounds are given in ( 4.9) and ( 4.11).

Both type I and type II sums can be handled using Vinogradov’s bound for sums of the form ∑ n ∈ I e ⁡ ( f ⁡ ( n)) \sum_{n\in I}e(f(n)) with f f smooth, although we need to first cut from I I small intervals around zeros of the first log ⁡ P \log P derivatives of N / t + M / t j N/t+M/t^{j}. This way we obtain that the sum in (i) exhibits cancellation. It is here that the restriction N, M = O ⁡ ( exp ⁡ ( log 3 / 2 − ε ⁡ P)) N,M=O(\exp(\log^{3/2-\varepsilon}P)) arises; even under the Riemann hypothesis we do not know how to relax this requirement 2 2 2 Using standard randomness heuristics one could tentatively conjecture that this restriction N, M = O ⁡ ( exp ⁡ ( log 3 / 2 − ε ⁡ P)) N,M=O(\exp(\log^{3/2-\varepsilon}P)) could be relaxed to N, M = O ⁡ ( exp ⁡ ( P c)) N,M=O(\exp(P^{c})) for some constant c > 0 c>0; this would improve the range exp ⁡ ( log 2 / 3 + ε ⁡ n) ≤ m ≤ n / 2 \exp(\log^{2/3+\varepsilon}n)\leq m\leq n/2 in Theorem 1.3 to log C ⁡ n ≤ m ≤ n / 2 \log^{C}n\leq m\leq n/2 for some constant C > 0 C>0..

Once the equidistribution estimate, Proposition 1.12, is established, the analysis of the distribution of both sides of ( 1.13) is relatively straightforward, as long as the scale P P is chosen so that the powers P j P^{j} do not lie close to various integer combinations of m, n, m ′, n ′ m,n,m^{\prime},n^{\prime}. However, there are some delicate cases when two of the numbers n, m, n − m, n ′, m ′, n ′ − m ′ n,m,n-m,n^{\prime},m^{\prime},n^{\prime}-m^{\prime} are “commensurable” in the sense that one of them is close to a rational multiple of the other, where the rational multiplier has small height. Commensurable integers are also known to generate some exceptional examples of integer factorial ratios [6], [7], [25]. Fortunately, we can handle these cases in our context by an analysis of covariances between various fractional parts { n 1 𝐩 }, { n 2 𝐩 } \{\frac{n_{1}}{\mathbf{p}}\},\{\frac{n_{2}}{\mathbf{p}}\}, in particular taking advantage of the fact that these covariances are non-negative up to small errors, and small unless n 1, n 2 n_{1},n_{2} are very highly commensurable.

### 1.4. Acknowledgments

KM was supported by Academy of Finland grant no. 285894. MR acknowledges the support of NSF grant DMS-1902063 and a Sloan Fellowship. XS was supported by NSF grant DMS-1802224. TT was supported by a Simons Investigator grant, the James and Carol Collins Chair, the Mathematical Analysis & Application Research Fund Endowment, and by NSF grant DMS-1764034. JT was supported by a Titchmarsh Fellowship.

### 1.5. Notation

We use X ≪ Y X\ll Y, X = O ⁡ ( Y) X=O(Y), or Y ≫ X Y\gg X to denote the estimate | X | ≤ C ​ Y |X|\leq CY for some constant C C. If we wish to permit this constant to depend on one or more parameters we shall indicate this by appropriate subscripts, thus for instance O ε, A ​ ( Y) O_{\varepsilon,A}(Y) denotes a quantity bounded in magnitude by C ε, A ​ Y C_{\varepsilon,A}Y for some quantity C ε, A C_{\varepsilon,A} depending only on ε, A \varepsilon,A. We write X ≍ Y X\asymp Y for X ≪ Y ≪ X X\ll Y\ll X.

We use 1 E 1_{E} to denote the indicator of an event E E, thus 1 E 1_{E} equals 1 1 when E E is true and 0 0 otherwise.

We let e e denote the standard real character e ⁡ ( x) ≔ e 2 ​ π ​ i ​ x e(x)\coloneqq e^{2\pi ix}.

## 2. Derivative estimates

We generalize the binomial coefficient ( n m) \binom{n}{m} to real 0 ≤ m ≤ n 0\leq m\leq n by the formula

 | ( n m) ≔ Γ ⁡ ( n + 1) Γ ⁡ ( m + 1) ​ Γ ​ ( n − m + 1) \binom{n}{m}\coloneqq\frac{\Gamma(n+1)}{\Gamma(m+1)\Gamma(n-m+1)} |  |

where

 | Γ ⁡ ( x) ≔ e − γ ​ x x ​ ∏ n = 1 ∞ ( 1 + x n) − 1 ​ e x / n \Gamma(x)\coloneqq\frac{e^{-\gamma x}}{x}\prod_{n=1}^{\infty}\left(1+\frac{x}{n}\right)^{-1}e^{x/n} |  |

is the Gamma function (with γ \gamma the Euler–Mascheroni constant). This is of course consistent with the usual definition of the binomial coefficient. Observe that the digamma function

 | ψ ⁡ ( x) ≔ Γ ′ Γ ​ ( x) = − γ + ∑ n = 0 ∞ 1 n + 1 − 1 n + x \psi(x)\coloneqq\frac{\Gamma^{\prime}}{\Gamma}(x)=-\gamma+\sum_{n=0}^{\infty}\frac{1}{n+1}-\frac{1}{n+x} |  |

is a smooth increasing concave function on ( 0, + ∞) (0,+\infty), with

 | ψ ′ ​ ( x) = ∑ n = 0 ∞ 1 ( n + x) 2 \psi^{\prime}(x)=\sum_{n=0}^{\infty}\frac{1}{(n+x)^{2}} |  |

positive and decreasing, and

 | ψ ′′ ( x) = − ∑ n = 0 ∞ 2 ( n + x) 3 \psi^{\prime\prime}(x)=-\sum_{n=0}^{\infty}\frac{2}{(n+x)^{3}} |  |

negative. For future reference we also observe the standard asymptotics

(2.1) |  | ψ ⁡ ( x) \displaystyle\psi(x) | = log ⁡ x + O ⁡ ( 1 x) \displaystyle=\log x+O\left(\frac{1}{x}\right) |  |

(2.2) |  | ψ ′ ​ ( x) \displaystyle\psi^{\prime}(x) | = 1 x + O ⁡ ( 1 x 2) \displaystyle=\frac{1}{x}+O\left(\frac{1}{x^{2}}\right) |  |

(2.3) |  | ψ ′′ ​ ( x) \displaystyle\psi^{\prime\prime}(x) | = − 1 x 2 + O ⁡ ( 1 x 3) \displaystyle=-\frac{1}{x^{2}}+O\left(\frac{1}{x^{3}}\right) |  |

and the Stirling approximation

(2.4) |  | log ⁡ Γ ⁡ ( x) = x ​ log ⁡ x − x − 1 2 ​ log ⁡ x + log ⁡ 2 ​ π + O ⁡ ( 1 x) \log\Gamma(x)=x\log x-x-\frac{1}{2}\log x+\log\sqrt{2\pi}+O\left(\frac{1}{x}\right) |  |

for any x ≥ 1 x\geq 1; see e.g., [2, §6.1, 6.3, 6.4]. One could also extend these functions meromorphically to the entire complex plane, but we will not need to do so here.

From the increasing nature of ψ \psi we see that n ↦ ( n m) n\mapsto\binom{n}{m} is strictly increasing on [m, + ∞) [m,+\infty) for fixed real m > 0 m>0, and from Stirling’s approximation ( 2.4) we see that it goes to infinity as n → ∞ n\to\infty. Thus for given t > 1 t>1, we see from the inverse function theorem that there exists a unique smooth function f t: [0, + ∞) → [0, + ∞) f_{t}\colon[0,+\infty)\to[0,+\infty) with f t ​ ( m) > m f_{t}(m)>m for all m m, such that

(2.5) |  | ( f t ​ ( m) m) = t. \binom{f_{t}(m)}{m}=t. |  |

In particular, the equation ( 1.1) holds for given integers 1 ≤ m ≤ n 1\leq m\leq n and t ≥ 2 t\geq 2 if and only if n = f t ​ ( m) n=f_{t}(m). This function f t f_{t} was analyzed by Kane [14], who among other things was able to extend f t f_{t} holomorphically to a certain sector, which then allowed him to estimate high derivatives of this function. However, for our analysis we will only need to control the first few derivatives of f t f_{t}, which can be estimated by hand:

###### Proposition 2.1 (Estimates on the first few derivatives).

Let t, m t,m be sufficiently large with m ≤ f t ​ ( m) / 2 m\leq f_{t}(m)/2. Then

(2.6) |  | f t ​ ( m) ≍ m ​ t 1 / m f_{t}(m)\asymp mt^{1/m} |  |

and

(2.7) |  | − f t ′ ​ ( m) ≍ ( f t ​ ( m) − 2 ​ m) ​ log ⁡ t m 2 -f^{\prime}_{t}(m)\asymp(f_{t}(m)-2m)\frac{\log t}{m^{2}} |  |

and

(2.8) |  | f t ′′ ​ ( m) ≍ f t ​ ( m) ​ ( log ⁡ t m 2) 2. f^{\prime\prime}_{t}(m)\asymp f_{t}(m)\left(\frac{\log t}{m^{2}}\right)^{2}. |  |

In particular, f t f_{t} is convex and decreasing in this regime.

The bound ( 2.6) can be viewed as a generalization of ( 1.6) to non-integer values of n, m, t n,m,t.

###### Proof.

Taking logarithms in ( 2.5) we have

(2.9) |  | log ⁡ Γ ⁡ ( f t ​ ( m) + 1) − log ⁡ Γ ⁡ ( f t ​ ( m) − m + 1) − log ⁡ Γ ⁡ ( m + 1) = log ⁡ t. \log\Gamma(f_{t}(m)+1)-\log\Gamma(f_{t}(m)-m+1)-\log\Gamma(m+1)=\log t. |  |

Writing n = f t ​ ( m) ≥ 2 ​ m n=f_{t}(m)\geq 2m, we thus see from the mean value theorem that

 | m ​ ψ ​ ( n − θ ​ m + 1) − log ⁡ Γ ⁡ ( m + 1) = log ⁡ t m\psi(n-\theta m+1)-\log\Gamma(m+1)=\log t |  |

for some 0 ≤ θ ≤ 1 0\leq\theta\leq 1 depending on t, m t,m. Applying ( 2.1), we conclude that

 | log ⁡ ( n − θ ​ m) = 1 m ​ ( log ⁡ t + log ⁡ Γ ⁡ ( m + 1)) + O ⁡ ( 1 n) \log(n-\theta m)=\frac{1}{m}(\log t+\log\Gamma(m+1))+O(\frac{1}{n}) |  |

which implies that

 | n ≍ n − θ ​ m ≍ exp ⁡ ( 1 m ​ ( log ⁡ t + log ⁡ Γ ⁡ ( m + 1))) n\asymp n-\theta m\asymp\exp(\frac{1}{m}(\log t+\log\Gamma(m+1))) |  |

and the claim ( 2.6) then follows from Stirling’s approximation ( 2.4).

If we differentiate ( 2.9) we obtain

(2.10) |  | f t ′ ​ ( m) ​ ψ ​ ( f t ​ ( m) + 1) − ( f t ′ ​ ( m) − 1) ​ ψ ​ ( f t ​ ( m) − m + 1) − ψ ⁡ ( m + 1) = 0. f^{\prime}_{t}(m)\psi(f_{t}(m)+1)-(f^{\prime}_{t}(m)-1)\psi(f_{t}(m)-m+1)-\psi(m+1)=0. |  |

In particular we obtain the first derivative formula

(2.11) |  | f t ′ ​ ( m) = ψ ⁡ ( m + 1) − ψ ⁡ ( n − m + 1) ψ ⁡ ( n + 1) − ψ ⁡ ( n − m + 1). f^{\prime}_{t}(m)=\frac{\psi(m+1)-\psi(n-m+1)}{\psi(n+1)-\psi(n-m+1)}. |  |

From ( 2.2) and the mean value theorem we have

(2.12) |  | ψ ⁡ ( n + 1) − ψ ⁡ ( n − m + 1) ≍ m n \psi(n+1)-\psi(n-m+1)\asymp\frac{m}{n} |  |

while from either the mean-value theorem and ( 2.2) (if m ≍ n m\asymp n) or from ( 2.1) (if say m ≤ n / 4 m\leq n/4) we see that

 | ψ ⁡ ( n − m + 1) − ψ ⁡ ( m + 1) ≍ n − 2 ​ m n ​ log ⁡ n m. \psi(n-m+1)-\psi(m+1)\asymp\frac{n-2m}{n}\log\frac{n}{m}. |  |

We conclude that

 | − f t ′ ​ ( m) ≍ n − 2 ​ m m ​ log ⁡ n m -f^{\prime}_{t}(m)\asymp\frac{n-2m}{m}\log\frac{n}{m} |  |

and the claim ( 2.7) follows from ( 2.6).

Differentiating ( 2.10) again, we conclude

 | f t ′′ ​ ( m) ​ ψ ​ ( n + 1) + ( f t ′ ​ ( m)) 2 ​ ψ ′ ​ ( n + 1) − f t ′′ ​ ( m) ​ ψ ​ ( n − m + 1) − ( f t ′ ​ ( m) − 1) 2 ​ ψ ′ ​ ( n − m + 1) − ψ ′ ​ ( m + 1) = 0. f^{\prime\prime}_{t}(m)\psi(n+1)+(f^{\prime}_{t}(m))^{2}\psi^{\prime}(n+1)-f^{\prime\prime}_{t}(m)\psi(n-m+1)-(f^{\prime}_{t}(m)-1)^{2}\psi^{\prime}(n-m+1)-\psi^{\prime}(m+1)=0. |  |

which we can rearrange using ( 2.11) as

 | f t ′′ ​ ( m) ​ ( ψ ⁡ ( n + 1) − ψ ⁡ ( n − m + 1)) 3 \displaystyle f^{\prime\prime}_{t}(m)(\psi(n+1)-\psi(n-m+1))^{3} | = ( ψ ⁡ ( n + 1) − ψ ⁡ ( n − m + 1)) 2 ​ ψ ′ ​ ( m + 1) \displaystyle=(\psi(n+1)-\psi(n-m+1))^{2}\psi^{\prime}(m+1) |  |

 |  | + ( ψ ⁡ ( n + 1) − ψ ⁡ ( m + 1)) 2 ​ ψ ′ ​ ( n − m + 1) \displaystyle\quad+(\psi(n+1)-\psi(m+1))^{2}\psi^{\prime}(n-m+1) |  |

 |  | − ( ψ ⁡ ( n − m + 1) − ψ ⁡ ( m + 1)) 2 ​ ψ ′ ​ ( n + 1). \displaystyle\quad-(\psi(n-m+1)-\psi(m+1))^{2}\psi^{\prime}(n+1). |  |

From ( 2.12), ( 2.6) it thus suffices to show that

 | ( ψ ⁡ ( n + 1) − ψ ⁡ ( n − m + 1)) 2 ​ ψ ′ ​ ( m + 1) \displaystyle(\psi(n+1)-\psi(n-m+1))^{2}\psi^{\prime}(m+1)\quad |  |  |

 | + ( ψ ⁡ ( n + 1) − ψ ⁡ ( m + 1)) 2 ​ ψ ′ ​ ( n − m + 1) \displaystyle+(\psi(n+1)-\psi(m+1))^{2}\psi^{\prime}(n-m+1)\quad |  |  |

 | − ( ψ ⁡ ( n − m + 1) − ψ ⁡ ( m + 1)) 2 ​ ψ ′ ​ ( n + 1) \displaystyle-(\psi(n-m+1)-\psi(m+1))^{2}\psi^{\prime}(n+1) | ≍ m n 2 ​ log 2 ⁡ ( n / m). \displaystyle\asymp\frac{m}{n^{2}}\log^{2}(n/m). |  |

The quantity ( ψ ⁡ ( n + 1) − ψ ⁡ ( n − m + 1)) 2 ​ ψ ′ ​ ( m + 1) (\psi(n+1)-\psi(n-m+1))^{2}\psi^{\prime}(m+1) is non-negative and is of size O ⁡ ( m / n 2) O(m/n^{2}) by ( 2.12), ( 2.2). Thus it will suffice to show that

 | ( ψ ⁡ ( n + 1) − ψ ⁡ ( m + 1)) 2 ​ ψ ′ ​ ( n − m + 1) − ( ψ ⁡ ( n − m + 1) − ψ ⁡ ( m + 1)) 2 ​ ψ ′ ​ ( n + 1) ≍ m n 2 ​ log 2 ⁡ ( n / m). (\psi(n+1)-\psi(m+1))^{2}\psi^{\prime}(n-m+1)-(\psi(n-m+1)-\psi(m+1))^{2}\psi^{\prime}(n+1)\asymp\frac{m}{n^{2}}\log^{2}(n/m). |  |

We split the left-hand side as the sum of

 | ( ψ ⁡ ( m + 1) − ψ ⁡ ( n + 1)) 2 ​ ( ψ ′ ​ ( n − m + 1) − ψ ′ ​ ( n + 1)) (\psi(m+1)-\psi(n+1))^{2}(\psi^{\prime}(n-m+1)-\psi^{\prime}(n+1)) |  |

and

 |  | ψ ′ ​ ( n + 1) ​ [( ψ ⁡ ( n + 1) − ψ ⁡ ( m + 1)) 2 − ( ψ ⁡ ( n − m + 1) − ψ ⁡ ( m + 1)) 2] \displaystyle\psi^{\prime}(n+1)[(\psi(n+1)-\psi(m+1))^{2}-(\psi(n-m+1)-\psi(m+1))^{2}] |  |

 |  | = ( ψ ⁡ ( n + 1) − ψ ⁡ ( m + 1) + ψ ⁡ ( n − m + 1) − ψ ⁡ ( m + 1)) ​ ( ψ ⁡ ( n + 1) − ψ ⁡ ( n − m + 1)) ​ ψ ′ ​ ( n + 1). \displaystyle=(\psi(n+1)-\psi(m+1)+\psi(n-m+1)-\psi(m+1))(\psi(n+1)-\psi(n-m+1))\psi^{\prime}(n+1). |  |

From ( 2.1), ( 2.3), and the mean value theorem the first term is positive and comparable to m n 2 ​ log 2 ​ n m \frac{m}{n^{2}}\log^{2}\frac{n}{m}; similarly, from ( 2.1), ( 2.2), and ( 2.12) the second term is positive and bounded above by O ⁡ ( m n 2 ​ log ⁡ n m) O(\frac{m}{n^{2}}\log\frac{n}{m}). The claim follows. ∎

To apply these derivative bounds, we use the following lemma that implicitly appears in [14], [15]:

###### Lemma 2.2 (Small non-zero derivative implies few integer values).

Let k ≥ 1 k\geq 1 be a natural number, and suppose that f: I → ℝ f:I\to\mathbb{R} is a smooth function on an interval I I of some length | I | |I| such that one has the derivative bound

(2.13) |  | 0 < | 1 k! f ( k) ( x) | < | I | − k ( k + 1) / 2 0<\left|\frac{1}{k!}f^{(k)}(x)\right|<|I|^{-k(k+1)/2} |  |

for all x ∈ I x\in I. Then there are at most k k integers m ∈ I m\in I for which f ⁡ ( m) f(m) is also an integer.

###### Proof.

Suppose for contradiction that there are k + 1 k+1 distinct integers m 1, …, m k + 1 ∈ I m_{1},\dots,m_{k+1}\in I with f ⁡ ( m 1), …, f ⁡ ( m k + 1) f(m_{1}),\dots,f(m_{k+1}) an integer. By Lagrange interpolation, the function

(2.14) |  | P ( x) ≔ ∑ i = 1 k + 1 ∏ 1 ≤ j ≤ k + 1: j ≠ i x − m j m i − m j f ( m i) P(x)\coloneqq\sum_{i=1}^{k+1}\prod_{1\leq j\leq k+1:j\neq i}\frac{x-m_{j}}{m_{i}-m_{j}}f(m_{i}) |  |

is a polynomial of degree at most k k such that f ⁡ ( x) − P ⁡ ( x) f(x)-P(x) vanishes at m 1, …, m k + 1 m_{1},\dots,m_{k+1}. By many applications of Rolle’s theorem (see [14, Corollary 2.1]), there must then exist x ∗ ∈ I x_{*}\in I such that f ( k) ​ ( x ∗) − P ( k) ​ ( x ∗) f^{(k)}(x_{*})-P^{(k)}(x_{*}) vanishes. From ( 2.14), 1 k! ​ P ( k) ​ ( x) \frac{1}{k!}P^{(k)}(x) (which is the degree k k coefficient of P ⁡ ( x) P(x)) is an integer multiple of 1 ∏ 1 ≤ i < j ≤ k + 1 | m i − m j | ≥ | I | − k ( k + 1) / 2 \frac{1}{\prod_{1\leq i<j\leq k+1}|m_{i}-m_{j}|}\geq|I|^{-k(k+1)/2}, and thus either vanishes or has magnitude at least | I | − k ( k + 1) / 2 |I|^{-k(k+1)/2}. But this contradicts ( 2.13). ∎

As an application of these bounds, we can locally control the number of solutions ( 1.1) in the region n 1 / 2 + ε ≤ m ≤ n / 2 n^{1/2+\varepsilon}\leq m\leq n/2, thus giving a version of Theorem 1.3 in a small interval:

###### Corollary 2.3.

Let 0 < ε < 1 0<\varepsilon<1, let t t be sufficiently large depending on ε \varepsilon, and suppose that ( n, m) (n,m) is a solution to ( 1.1) in the left half ( 1.4) of Pascal’s triangle with m ≥ n 1 / 2 + ε m\geq n^{1/2+\varepsilon}. Then there is at most one other solution ( n ′, m ′) (n^{\prime},m^{\prime}) to ( 1.1) in the interval m ′ ∈ [m − m ε / 10, m] m^{\prime}\in[m-m^{\varepsilon/10},m].

###### Proof.

From ( 1.7) and the hypothesis n 1 / 2 + ε ≤ m ≤ n / 2 n^{1/2+\varepsilon}\leq m\leq n/2 we have

(2.15) |  | log ⁡ t log 2 ⁡ t ≪ m ≪ log ⁡ t. \frac{\log t}{\log_{2}t}\ll m\ll\log t. |  |

For x x in the interval I ≔ [m − m ε / 10, m] I\coloneqq[m-m^{\varepsilon/10},m], we then have log ⁡ t x = log ⁡ t m + O ⁡ ( m − 2 + ε / 10 ​ log ⁡ t) = log ⁡ t m + O ⁡ ( 1) \frac{\log t}{x}=\frac{\log t}{m}+O(m^{-2+\varepsilon/10}\log t)=\frac{\log t}{m}+O(1), and so we see from Proposition 2.1 and ( 2.15) that f t ​ ( x) ≍ n f_{t}(x)\asymp n and

 | 0 < | f t ′′ ​ ( x) | ≪ n ​ ( log ⁡ t m 2) 2 ≪ n m 2 ​ log 2 2 ​ t ≪ n m 2 ​ log 2 ​ m 0<|f^{\prime\prime}_{t}(x)|\ll n\left(\frac{\log t}{m^{2}}\right)^{2}\ll\frac{n}{m^{2}}\log_{2}^{2}t\ll\frac{n}{m^{2}}\log^{2}m |  |

for all x ∈ I x\in I. Since m ≥ n 1 / 2 + ε m\geq n^{1/2+\varepsilon} and t t is sufficiently large depending on ε \varepsilon, m m is also sufficiently large depending on ε \varepsilon, and we have

 | 0 < | f t ′′ ​ ( x) | < | I | − 3 0<|f^{\prime\prime}_{t}(x)|<|I|^{-3} |  |

for all x ∈ I x\in I. Applying Lemma 2.2, there are at most two integers m ′ ∈ I m^{\prime}\in I with f t ​ ( m ′) f_{t}(m^{\prime}) an integer. Since m m is already one of these integers, the claim follows. ∎

The same method, using higher derivative estimates on f t f_{t}, also gives similar results (with weaker bounds on the number of solutions) for m < n 1 / 2 + ε m<n^{1/2+\varepsilon}; see [14], [15]. However, we will only need to apply this method in the m ≥ n 1 / 2 + ε m\geq n^{1/2+\varepsilon} regime here.

We are now ready to prove Proposition 1.10.

###### Proof of Proposition 1.10.

Let ε > 0 \varepsilon>0, let t t be sufficiently large depending on ε \varepsilon, and let ( n, m) (n,m) be a solution to ( 1.1) in the region

(2.16) |  | { ( n, m): exp ⁡ ( log 2 / 3 + ε ⁡ n) ≤ m ≤ n / 2 } \{(n,m):\exp(\log^{2/3+\varepsilon}n)\leq m\leq n/2\} |  |

For brevity we allow all implied constants in the following arguments to depend on ε \varepsilon. Suppose ( n ′, m ′) (n^{\prime},m^{\prime}) is another solution in this region with m ′ < m m^{\prime}<m, n ′ > n n^{\prime}>n and

 | m − m ′, n ′ − n ≪ ε ′ exp ( O ( log 2 1 − ε ′ t)). m-m^{\prime},n^{\prime}-n\ll_{\varepsilon^{\prime}}\exp(O(\log^{1-\varepsilon^{\prime}}_{2}t)). |  |

From ( 2.7) and convexity (and the bounds m ≪ log ⁡ t m\ll\log t and m − m ′ ≥ 1 m-m^{\prime}\geq 1) we have

 | n ′ − n \displaystyle n^{\prime}-n | = f t ​ ( m ′) − f t ​ ( m) \displaystyle=f_{t}(m^{\prime})-f_{t}(m) |  |

 |  | ≥ f t ′ ​ ( m) ​ ( m ′ − m) \displaystyle\geq f^{\prime}_{t}(m)(m^{\prime}-m) |  |

 |  | ≫ ( n − 2 ​ m) ​ log ⁡ t m 2 ​ ( m − m ′) \displaystyle\gg(n-2m)\frac{\log t}{m^{2}}(m-m^{\prime}) |  |

 |  | ≫ n − 2 ​ m m \displaystyle\gg\frac{n-2m}{m} |  |

 |  | = n m − 2 \displaystyle=\frac{n}{m}-2 |  |

and thus

 | n / m ≪ ε ′ exp ( O ( log 2 1 − ε ′ t)) n/m\ll_{\varepsilon^{\prime}}\exp(O(\log^{1-\varepsilon^{\prime}}_{2}t)) |  |

From ( 1.7) we have n ≫ log ⁡ t n\gg\log t, hence log 2 1 − ε ′ ​ t ≪ log 1 − ε ′ ⁡ n \log^{1-\varepsilon^{\prime}}_{2}t\ll\log^{1-\varepsilon^{\prime}}n, and so for some constant C > 0 C>0, m ≥ n / exp ⁡ ( C ​ log 1 − ε ′ ​ n) ≥ n 9 / 10 m\geq n/\exp(C\log^{1-\varepsilon^{\prime}}n)\geq n^{9/10} (shrinking ε ′ \varepsilon^{\prime} slightly if necessary) if t t is sufficiently large depending on ε ′ \varepsilon^{\prime}. The result now follows from Corollary 2.3.

∎

It remains to establish Proposition 1.9. This will be the objective of the next two sections of the paper.

## 3. The distance bound

In this section we assume Proposition 1.12 and use it to establish Proposition 1.9.

Throughout this section 0 < ε < 1 0<\varepsilon<1 will be fixed; we can assume it to be small. We may assume that t t is sufficiently large depending on ε \varepsilon, as the claim is trivial otherwise. We may assume that m ′ < m m^{\prime}<m, hence also n ′ > n n^{\prime}>n. We assume for sake of contradiction that at least one of the claims

(3.1) |  | m − m ′ ≥ exp ⁡ ( log 2 / 3 + ε ⁡ n ′) m-m^{\prime}\geq\exp(\log^{2/3+\varepsilon}n^{\prime}) |  |

and

(3.2) |  | m, m ′, n ′ − n ≥ exp ⁡ ( log 2 / 3 + ε ⁡ n ′) m,m^{\prime},n^{\prime}-n\geq\exp(\log^{2/3+\varepsilon}n^{\prime}) |  |

is true, as the claim is trivial otherwise. This allows us to select a “good” scale:

###### Lemma 3.1 (Selection of scale).

With the above assumptions, there exists P > 1 P>1 obeying the following axioms:

- (i)

( m, m ′, n, n ′ m,m^{\prime},n,n^{\prime} not too large) We have m, m ′, n, n ′ ≤ exp ⁡ ( log 3 2 − ε 10 ⁡ P) m,m^{\prime},n,n^{\prime}\leq\exp(\log^{\frac{3}{2}-\frac{\varepsilon}{10}}P). (In particular, P P will be sufficiently large depending on ε \varepsilon, since otherwise t = O ε ​ ( 1) t=O_{\varepsilon}(1).)

- (ii)

(Dichotomy) If a, a ′, b, b ′ a,a^{\prime},b,b^{\prime} are integers with | a |, | a ′ |, | b |, | b ′ | ≤ log 1 / 100 ⁡ P |a|,|a^{\prime}|,|b|,|b^{\prime}|\leq\log^{1/100}P, and j j is a natural number, then either

(3.3) |  | | a ​ m + a ′ ​ m ′ + b ​ n + b ′ ​ n ′ | ≤ P j / log 1000 ⁡ P |am+a^{\prime}m^{\prime}+bn+b^{\prime}n^{\prime}|\leq P^{j}/\log^{1000}P |  |

or

 | | a ​ m + a ′ ​ m ′ + b ​ n + b ′ ​ n ′ | ≥ P j ​ log 1000 ​ P. |am+a^{\prime}m^{\prime}+bn+b^{\prime}n^{\prime}|\geq P^{j}\log^{1000}P. |  |

- (iii)

(Separation) At least one of the statements

 | m − m ′ ≥ P ​ log 100 ​ P m-m^{\prime}\geq P\log^{100}P |  |

and

 | m, m ′, n ′ − n ≥ P ​ log 100 ​ P m,m^{\prime},n^{\prime}-n\geq P\log^{100}P |  |

is true.

###### Proof.

We restrict P P to be a power of two in the range

 | exp ⁡ ( log 2 / 3 + ε / 2 ⁡ n ′) ≤ P ≤ exp ⁡ ( 2 ​ log 2 / 3 + ε / 2 ​ n ′); \exp(\log^{2/3+\varepsilon/2}n^{\prime})\leq P\leq\exp(2\log^{2/3+\varepsilon/2}n^{\prime}); |  |

such a choice will automatically obey (i) since n ′ > n > m > m ′ n^{\prime}>n>m>m^{\prime} and (iii) since we assumed that either ( 3.1) or ( 3.2) holds. There are ≫ log 2 / 3 + ε / 2 ⁡ n ′ \gg\log^{2/3+\varepsilon/2}n^{\prime} choices for P P. Some of these will not obey (ii), but we can control the number of exceptions as follows. Firstly, observe that the conclusion ( 3.3) will hold unless j = O ⁡ ( log 1 / 3 ⁡ n ′) j=O(\log^{1/3}n^{\prime}), so we may restrict attention to this range of j j. The number of possible tuples ( a, a ′, b, b ′, j) (a,a^{\prime},b,b^{\prime},j) is then O ⁡ ( log 4 / 100 ⁡ P ​ log 1 / 3 ​ n ′) O(\log^{4/100}P\log^{1/3}n^{\prime}). For each such tuple, we see from the restriction on P P that the number of P P with

 | P j / log 1000 ⁡ P < | a ​ m + a ′ ​ m ′ + b ​ n + b ′ ​ n ′ | < P j ​ log 1000 ​ P P^{j}/\log^{1000}P<|am+a^{\prime}m^{\prime}+bn+b^{\prime}n^{\prime}|<P^{j}\log^{1000}P |  |

is at most O ⁡ ( log 2 ⁡ n ′) O(\log_{2}n^{\prime}) (since a ​ m + a ′ ​ m ′ + b ​ n + b ′ ​ n ′ am+a^{\prime}m^{\prime}+bn+b^{\prime}n^{\prime} is of size O ⁡ ( ( n ′) 2) O((n^{\prime})^{2}), say). Thus we see that the total number of P P which fail to obey (ii) is at most

 | O ⁡ ( log 4 / 100 ⁡ P ​ log 1 / 3 ​ n ′ ​ log 2 ​ n ′) O(\log^{4/100}P\log^{1/3}n^{\prime}\log_{2}n^{\prime}) |  |

which is negligible compared to the total number of choices, which is ≫ log 2 / 3 + ε / 2 ⁡ n ′ \gg\log^{2/3+\varepsilon/2}n^{\prime}. Thus we can find a choice of P P which obeys all of (i), (ii), and (iii), giving the claim. ∎

Henceforth we fix a scale P P obeying the properties in Lemma 3.1. We now introduce a relation ≈ \approx on the reals by declaring x ≈ y x\approx y if | x − y | ≤ P / log 1000 ⁡ P |x-y|\leq P/\log^{1000}P. Thus, by Lemma 3.1 (ii), if a ​ m + a ′ ​ m ′ + b ​ n + b ′ ​ n ′ ≉ 0 am+a^{\prime}m^{\prime}+bn+b^{\prime}n^{\prime}\not\approx 0 for a, a ′, b, b ′ a,a^{\prime},b,b^{\prime} as in Lemma 3.1 (ii) then | a ​ m + a ′ ​ m ′ + b ​ n + b ′ ​ n ′ | ≥ P ​ log 1000 ​ P |am+a^{\prime}m^{\prime}+bn+b^{\prime}n^{\prime}|\geq P\log^{1000}P. Also, from Lemma 3.1 (iii), at least one of the statements

 | m ≉ m ′ m\not\approx m^{\prime} |  |

and

 | m, m ′, n ′ − n ≉ 0 m,m^{\prime},n^{\prime}-n\not\approx 0 |  |

is true.

We introduce a random variable 𝐩 \mathbf{p}, which is drawn uniformly from the primes in the interval I ≔ [P, P + P ​ log − 100 ​ P] I\coloneqq[P,P+P\log^{-100}P] (note that there is at least one such prime thanks to the prime number theorem). From ( 1.13) we surely have

 | ∑ j = 1 ∞ ( { m 𝐩 j } + { n − m 𝐩 j } − { n 𝐩 j }) = ∑ j = 1 ∞ ( { m ′ 𝐩 j } + { n ′ − m ′ 𝐩 j } − { n ′ 𝐩 j }). \sum_{j=1}^{\infty}\left(\left\{\frac{m}{\mathbf{p}^{j}}\right\}+\left\{\frac{n-m}{\mathbf{p}^{j}}\right\}-\left\{\frac{n}{\mathbf{p}^{j}}\right\}\right)=\sum_{j=1}^{\infty}\left(\left\{\frac{m^{\prime}}{\mathbf{p}^{j}}\right\}+\left\{\frac{n^{\prime}-m^{\prime}}{\mathbf{p}^{j}}\right\}-\left\{\frac{n^{\prime}}{\mathbf{p}^{j}}\right\}\right). |  |

We can restrict attention to those j j with j ≤ log 1 / 2 ⁡ P j\leq\log^{1/2}P, since the summands vanish otherwise. For any real number N N, we may take covariances of both sides of this identity with the random variable { N 𝐩 } \{\frac{N}{\mathbf{p}}\} to conclude that

(3.4) |  | ∑ j ≤ log 1 / 2 ⁡ P ( c j ​ ( N, m) + c j ​ ( N, n − m) − c j ​ ( N, n)) = ∑ j ≤ log 1 / 2 ⁡ P ( c j ​ ( N, m ′) + c j ​ ( N, n ′ − m ′) − c j ​ ( N, n ′)) \sum_{j\leq\log^{1/2}P}\left(c_{j}(N,m)+c_{j}(N,n-m)-c_{j}(N,n)\right)=\sum_{j\leq\log^{1/2}P}\left(c_{j}(N,m^{\prime})+c_{j}(N,n^{\prime}-m^{\prime})-c_{j}(N,n^{\prime})\right) |  |

for any real number N N, where the covariances c j ​ ( N, M) c_{j}(N,M) are defined as

 | c j ​ ( N, M) \displaystyle c_{j}(N,M) | ≔ 𝐄 ⁡ { N 𝐩 } ​ { M 𝐩 j } − 𝐄 ⁡ { N 𝐩 } ​ 𝐄 ​ { M 𝐩 j } \displaystyle\coloneqq\mathbf{E}\left\{\frac{N}{\mathbf{p}}\right\}\left\{\frac{M}{\mathbf{p}^{j}}\right\}-\mathbf{E}\left\{\frac{N}{\mathbf{p}}\right\}\mathbf{E}\left\{\frac{M}{\mathbf{p}^{j}}\right\} |  |

 |  | ≔ 𝐄 ⁡ ( 1 2 − { N 𝐩 }) ​ ( 1 2 − { M 𝐩 j }) − 𝐄 ⁡ ( 1 2 − { N 𝐩 }) ​ 𝐄 ​ ( 1 2 − { M 𝐩 j }). \displaystyle\coloneqq\mathbf{E}\left(\frac{1}{2}-\left\{\frac{N}{\mathbf{p}}\right\}\right)\left(\frac{1}{2}-\left\{\frac{M}{\mathbf{p}^{j}}\right\}\right)-\mathbf{E}\left(\frac{1}{2}-\left\{\frac{N}{\mathbf{p}}\right\}\right)\mathbf{E}\left(\frac{1}{2}-\left\{\frac{M}{\mathbf{p}^{j}}\right\}\right). |  |

We now compute these covariances:

###### Proposition 3.2 (Covariance estimates).

Let N, M ∈ { m, n, m − n, m ′, n ′, n ′ − m ′ } N,M\in\{m,n,m-n,m^{\prime},n^{\prime},n^{\prime}-m^{\prime}\}, and j j be a natural number with 1 ≤ j ≤ log 1 / 2 ⁡ P 1\leq j\leq\log^{1/2}P.

- (i)

If j ≥ 2 j\geq 2, then c j ​ ( N, M) ≪ log − 10 ⁡ P c_{j}(N,M)\ll\log^{-10}P.

- (ii)

If j = 1 j=1 and N ≈ 0 N\approx 0 or M ≈ 0 M\approx 0, then c j ​ ( N, M) ≪ log − 1000 ⁡ P c_{j}(N,M)\ll\log^{-1000}P.

- (iii)

If j = 1 j=1, N, M ≉ 0 N,M\not\approx 0 and there exist coprime natural numbers 1 ≤ a, b ≤ log 1 / 100 ⁡ P 1\leq a,b\leq\log^{1/100}P such that a ​ N ≈ b ​ M aN\approx bM, then c j ( N, M) = 1 12 ​ a ​ b + O ( log − 1 / 1000 P) c_{j}(N,M)=\frac{1}{12ab}+O(\log^{-1/1000}P).

- (iv)

If j = 1 j=1 and N, M N,M are not of the form in (ii) or (iii), then c j ( N, M) ≪ log − 1 / 1000 P c_{j}(N,M)\ll\log^{-1/1000}P.

###### Remark 3.3.

The term 1 12 ​ a ​ b \frac{1}{12ab} appearing in Proposition 3.2 (iii) is also the covariance between { n ​ 𝐱 } \{n{\bf x}\} and { m ​ 𝐱 } \{m{\bf x}\} for 𝐱 {\bf x} drawn randomly from the unit interval whenever n, m n,m are natural numbers with a ​ n = b ​ m an=bm for some coprime a, b a,b; see [24, Section 2]. Indeed, both assertions are proven by the same Fourier-analytic argument, and Proposition 3.2 endows the linear span of the six functions { N 𝐩 } \{\frac{N}{\mathbf{p}}\} for N ∈ { m, n, m − n, m ′, n ′, n ′ − m ′ } N\in\{m,n,m-n,m^{\prime},n^{\prime},n^{\prime}-m^{\prime}\} with an inner product closely related to the norm N ⁡ () N() studied in [24], the structure of which is the key to obtaining a contradiction from our separation hypotheses on n − n ′, m − m ′ n-n^{\prime},m-m^{\prime}.

###### Proof of Proposition 3.2 assuming Proposition 1.12.

We first dispose of the easy case (ii). If N ≈ 0 N\approx 0, then { N 𝐩 } ≤ log − 1000 ⁡ P \{\frac{N}{\mathbf{p}}\}\leq\log^{-1000}P, and the claim follows from the triangle inequality; similarly if M ≈ 0 M\approx 0 or actually if M ≤ P j / log 1000 ⁡ P M\leq P^{j}/\log^{1000}P. Hence by Lemma 3.1 (ii), we may from now on assume that

 | N ≥ P ​ log 1000 ​ P and M ≥ P j ​ log 1000 ​ P. N\geq P\log^{1000}P\quad\text{and}\quad M\geq P^{j}\log^{1000}P. |  |

To handle the remaining cases we use the truncated Fourier expansion

(3.5) |  | 1 2 − { x } = ∑ 0 < | n | ≤ N 0 e ⁡ ( n ​ x) 2 ​ π ​ i ​ n + O ⁡ ( 1 1 + N 0 ​ dist ​ ( x, ℤ)) = ∑ 0 < | n | ≤ N 0 e ⁡ ( n ​ x) 2 ​ π ​ i ​ n + O ( 1 dist ( x, ℤ) ≤ N 0 − 1 / 2 + 1 N 0 1 / 2) \begin{split}\frac{1}{2}-\{x\}&=\sum_{0<|n|\leq N_{0}}\frac{e(nx)}{2\pi in}+O\left(\frac{1}{1+N_{0}\mathrm{dist}(x,\mathbb{Z})}\right)\\ &=\sum_{0<|n|\leq N_{0}}\frac{e(nx)}{2\pi in}+O\left(1_{\mathrm{dist}(x,\mathbb{Z})\leq N_{0}^{-1/2}}+\frac{1}{N_{0}^{1/2}}\right)\end{split} |  |

that holds for any N 0 ≥ 1 N_{0}\geq 1 (see e.g. [12, Formula (4.18)]).

Our primary tool is Proposition 1.12. Note that, for t ∈ I t\in I, log ⁡ t = log ⁡ P + O ⁡ ( log − 99 ⁡ P) \log t=\log P+O(\log^{-99}P), so that together with the prime number theorem Proposition 1.12 implies that

(3.6) |  | 𝐄 ​ W ​ ( N 𝐩, M 𝐩 j) = 1 | I | ​ ∫ I W ⁡ ( N t, M t j) ​ 𝑑 t + O ε ​ ( ‖ W ‖ C 3 ​ log − 99 ​ P) \mathbf{E}W\left(\frac{N}{\mathbf{p}},\frac{M}{\mathbf{p}^{j}}\right)=\frac{1}{|I|}\int_{I}W\left(\frac{N}{t},\frac{M}{t^{j}}\right)\ dt+O_{\varepsilon}(\|W\|_{C^{3}}\log^{-99}P) |  |

for any smooth ℤ 2 \mathbb{Z}^{2} -periodic W: ℝ 2 → ℂ W\colon\mathbb{R}^{2}\to\mathbb{C} and that, for any M ′, N ′ = O ⁡ ( exp ⁡ ( log 3 / 2 − ε / 2 ⁡ P)) M^{\prime},N^{\prime}=O(\exp(\log^{3/2-\varepsilon/2}P)),

(3.7) |  | 𝐄 ​ e ​ ( N ′ 𝐩 + M ′ 𝐩 j) = 1 | I | ​ ∫ I e ⁡ ( N ′ t + M ′ t j) ​ 𝑑 t + O ε ​ ( log − 99 ⁡ P) \mathbf{E}e\left(\frac{N^{\prime}}{\mathbf{p}}+\frac{M^{\prime}}{\mathbf{p}^{j}}\right)=\frac{1}{|I|}\int_{I}e\left(\frac{N^{\prime}}{t}+\frac{M^{\prime}}{t^{j}}\right)\ dt+O_{\varepsilon}(\log^{-99}P) |  |

Applying ( 3.6) with W W a suitable cutoff localized to the region { ( x, y): dist ( x, ℤ) ≤ 2 N 0 − 1 / 2 } \{(x,y):\mathrm{dist}(x,\mathbb{Z})\leq 2N_{0}^{-1/2}\} that equals one on { ( x, y): dist ( x, ℤ) ≤ N 0 − 1 / 2 } \{(x,y):\mathrm{dist}(x,\mathbb{Z})\leq N_{0}^{-1/2}\} chosen so that ‖ W ‖ C 3 ≪ N 0 3 / 2 \|W\|_{C^{3}}\ll N_{0}^{3/2}, we see that, for any N 0 ∈ [1, log 20 ⁡ P] N_{0}\in[1,\log^{20}P] we have

 | 𝐏 ( dist ( N 𝐩, ℤ) ≤ N 0 − 1 / 2) ≪ 1 | I | ∫ I 1 dist ( N t, ℤ) ≤ 2 N 0 − 1 / 2 d t + N 0 − 1 / 2. \mathbf{P}\left(\mathrm{dist}\left(\frac{N}{\mathbf{p}},\mathbb{Z}\right)\leq N_{0}^{-1/2}\right)\ll\frac{1}{|I|}\int_{I}1_{\mathrm{dist}(\frac{N}{t},\mathbb{Z})\leq 2N_{0}^{-1/2}}\ dt+N_{0}^{-1/2}. |  |

Since N ≥ P ​ log 1000 ​ P N\geq P\log^{1000}P, the first term on the right-hand side can be computed to be O ( N 0 − 1 / 2) O(N_{0}^{-1/2}). Thus

(3.8) |  | 𝐏 ( dist ( N 𝐩, ℤ) ≤ N 0 − 1 / 2) ≪ N 0 − 1 / 2 \mathbf{P}\left(\mathrm{dist}\left(\frac{N}{\mathbf{p}},\mathbb{Z}\right)\leq N_{0}^{-1/2}\right)\ll N_{0}^{-1/2} |  |

and a similar argument gives

(3.9) |  | 𝐏 ( dist ( M 𝐩 j, ℤ) ≤ N 0 − 1 / 2) ≪ N 0 − 1 / 2. \mathbf{P}\left(\mathrm{dist}\left(\frac{M}{\mathbf{p}^{j}},\mathbb{Z}\right)\leq N_{0}^{-1/2}\right)\ll N_{0}^{-1/2}. |  |

To prepare for the proofs of parts (i), (iii) and (iv), let us first show that, for 1 ≤ j ≤ log 1 / 2 ⁡ P 1\leq j\leq\log^{1/2}P, we have

(3.10) |  | 𝐄 ⁡ ( 1 2 − { M 𝐩 j }) ≪ log − 10 ⁡ P. \mathbf{E}\left(\frac{1}{2}-\left\{\frac{M}{\mathbf{p}^{j}}\right\}\right)\ll\log^{-10}P. |  |

We use the Fourier expansion ( 3.5) with N 0 = log 20 ⁡ P N_{0}=\log^{20}P. Averaging over p ∈ I p\in I and applying ( 3.9) to handle the first error term, we see that

 | 𝐄 ⁡ ( 1 2 − { M 𝐩 j }) = ∑ 0 < | m | ≤ log 20 ⁡ P 1 2 ​ π ​ i ​ m ​ 𝐄 ​ e ​ ( m ​ M 𝐩 j) + O ⁡ ( log − 10 ⁡ P). \mathbf{E}\left(\frac{1}{2}-\left\{\frac{M}{\mathbf{p}^{j}}\right\}\right)=\sum_{0<|m|\leq\log^{20}P}\frac{1}{2\pi im}\mathbf{E}e\left(m\frac{M}{\mathbf{p}^{j}}\right)+O(\log^{-10}P). |  |

By the triangle inequality and ( 3.7), it suffices to show that, for every non-zero integer m = O ⁡ ( log 20 ⁡ P) m=O(\log^{20}P),

 | 1 | I | ​ ∫ I e ⁡ ( m ​ M t j) ​ 𝑑 t ≪ log − 11 ⁡ P. \frac{1}{|I|}\int_{I}e\left(m\frac{M}{t^{j}}\right)\ dt\ll\log^{-11}P. |  |

Recalling that M ≥ P j ​ log 1000 ​ P M\geq P^{j}\log^{1000}P, this estimate follows from a standard integration by parts (see e.g. [12, Lemma 8.9]). Similarly

(3.11) |  | 𝐄 ⁡ ( 1 2 − { N 𝐩 }) ≪ log − 10 ⁡ P. \mathbf{E}\left(\frac{1}{2}-\left\{\frac{N}{\mathbf{p}}\right\}\right)\ll\log^{-10}P. |  |

Furthermore, using similarly ( 3.5), ( 3.8), ( 3.9) and ( 3.7), we see that, whenever 1 ≤ N 0 ≤ log 20 ⁡ P 1\leq N_{0}\leq\log^{20}P,

(3.12) |  | 𝐄 ( 1 2 − { N 𝐩 }) ( 1 2 − { M 𝐩 j }) = − ∑ 0 < | m |, | n | < N 0 1 4 ​ π 2 ​ m ​ n 1 | I | ∫ I e ( n N t + m M t j) d t + O ( 1 N 0 1 / 2). \mathbf{E}\left(\frac{1}{2}-\left\{\frac{N}{\mathbf{p}}\right\}\right)\left(\frac{1}{2}-\left\{\frac{M}{\mathbf{p}^{j}}\right\}\right)=-\sum_{0<|m|,|n|<N_{0}}\frac{1}{4\pi^{2}mn}\frac{1}{|I|}\int_{I}e\left(n\frac{N}{t}+m\frac{M}{t^{j}}\right)\ dt+O\left(\frac{1}{N_{0}^{1/2}}\right). |  |

Now we are ready to prove (i), (iii), and (iv). Let us start with (i). In light of ( 3.10), ( 3.11) and ( 3.12) with N 0 = log 20 ⁡ P N_{0}=\log^{20}P, it suffices to show that

 | 1 | I | ​ ∫ I e ⁡ ( n ​ N t + m ​ M t j) ​ 𝑑 t ≪ log − 11 ⁡ P. \frac{1}{|I|}\int_{I}e\left(n\frac{N}{t}+m\frac{M}{t^{j}}\right)\ dt\ll\log^{-11}P. |  |

whenever n, m = O ⁡ ( log 20 ⁡ P) n,m=O(\log^{20}P) are non-zero integers. Applying a change of variables t = P / s t=P/s, we reduce to showing that

(3.13) |  | ∫ 1 / ( 1 + log − 100 ⁡ P) 1 e ⁡ ( a ​ s + b ​ s j) ​ 𝑑 s ≪ log − 200 ⁡ P \int_{1/(1+\log^{-100}P)}^{1}e(as+bs^{j})\ ds\ll\log^{-200}P |  |

(say), where a ≔ n ​ N / P a\coloneqq nN/P and b ≔ m ​ M / P j b\coloneqq mM/P^{j}. By hypothesis, we have | a |, | b | ≥ log 1000 ⁡ P |a|,|b|\geq\log^{1000}P. Since 2 ≤ j ≤ log 1 / 2 ⁡ P 2\leq j\leq\log^{1/2}P, the derivative a + j ​ b ​ s j − 1 a+jbs^{j-1} of the phase a ​ s + b ​ s j as+bs^{j} is at least log 200 ⁡ P \log^{200}P outside of an interval of length at most O ⁡ ( log − 200 ⁡ P) O(\log^{-200}P), and ( 3.13) now follows from a standard integration by parts (see e.g. [12, Lemma 8.9]). This concludes the proof of (i).

Let us now turn to (iv). In light of ( 3.10), ( 3.11) and ( 3.12) with N 0 = log 1 / 500 ⁡ P N_{0}=\log^{1/500}P, it suffices to show that

 | 1 | I | ∫ I e ( n ​ N + m ​ M t) d t ≪ log − 1 / 500 P \frac{1}{|I|}\int_{I}e\left(\frac{nN+mM}{t}\right)\ dt\ll\log^{-1/500}P |  |

whenever n, m = O ⁡ ( log 1 / 500 ⁡ P) n,m=O(\log^{1/500}P) are non-zero integers. From the hypothesis (iv) and Lemma 3.1 (ii) (after factoring out any common multiple of n n and m m), we have | n ​ N + m ​ M | ≥ P ​ log 1000 ​ P |nN+mM|\geq P\log^{1000}P. The claim (iv) now follows from integration by parts.

Finally we show (iii). In light of ( 3.10), ( 3.11) and ( 3.12) with N 0 = log 1 / 500 ⁡ P N_{0}=\log^{1/500}P, it suffices to show that

 | − ∑ 0 < | n |, | m | ≤ log 1 / 500 ⁡ P 1 4 ​ π 2 ​ m ​ n 1 | I | ∫ I e ( n ​ N + m ​ M t) d t = 1 12 ​ a ​ b + O ( log − 1 / 1000 P). -\sum_{0<|n|,|m|\leq\log^{1/500}P}\frac{1}{4\pi^{2}mn}\frac{1}{|I|}\int_{I}e\left(\frac{nN+mM}{t}\right)\ dt=\frac{1}{12ab}+O(\log^{-1/1000}P). |  |

Let us first consider those n, m = O ⁡ ( log 1 / 500 ⁡ P) n,m=O(\log^{1/500}P) for which n ​ N + m ​ M ≉ 0 nN+mM\not\approx 0. By Lemma 3.1 (ii) | n ​ N + m ​ M | ≥ P ​ log 1000 ​ P |nN+mM|\geq P\log^{1000}P and similarly to case (iv), the contribution of such pairs ( n, m) (n,m) is acceptable.

Consider now the case n ​ N ≈ − m ​ M nN\approx-mM for some non-zero integers n, m = O ⁡ ( log 1 / 500 ⁡ P) n,m=O(\log^{1/500}P). By assumption also a ​ N ≈ b ​ M aN\approx bM for some co-prime positive integers a, b ≤ log 1 / 100 ⁡ P a,b\leq\log^{1/100}P. and hence by Lemma 3.1 (ii) − a ​ m ​ M ≈ b ​ n ​ M -amM\approx bnM which contradicts the assumption M ≉ 0 M\not\approx 0 unless ( n, m) (n,m) is a multiple of ( a, − b) (a,-b). On the other hand if ( n, m) (n,m) is a multiple of ( a, − b) (a,-b), then n ​ N ≈ − m ​ M nN\approx-mM by Lemma 3.1 (ii).

Thus it remains to show that

 | ∑ 0 < | k | ≤ log 1 / 500 ⁡ P max ⁡ { a, b } 1 4 ​ π 2 ​ k 2 ​ a ​ b 1 | I | ∫ I e ( k ​ a ​ N − k ​ b ​ M t) d t = 1 12 ​ a ​ b + O ( log − 1 / 1000 P). \sum_{0<|k|\leq\frac{\log^{1/500}P}{\max\{a,b\}}}\frac{1}{4\pi^{2}k^{2}ab}\frac{1}{|I|}\int_{I}e\left(\frac{kaN-kbM}{t}\right)\ dt=\frac{1}{12ab}+O(\log^{-1/1000}P). |  |

Since a ​ N ≈ b ​ M aN\approx bM we have, for every k ≤ log 1 / 500 ⁡ P k\leq\log^{1/500}P,

 | 1 | I | ​ ∫ I e ⁡ ( k ​ a ​ N − k ​ b ​ M t) ​ 𝑑 t = 1 − O ⁡ ( log − 100 ⁡ P) \frac{1}{|I|}\int_{I}e\left(\frac{kaN-kbM}{t}\right)\ dt=1-O(\log^{-100}P) |  |

and so it suffices to show that

 | ∑ 0 < | k | ≤ log 1 / 500 ⁡ P max ⁡ { a, b } 1 4 ​ π 2 ​ k 2 ​ a ​ b = 1 12 ​ a ​ b + O ( log − 1 / 1000 P) \sum_{0<|k|\leq\frac{\log^{1/500}P}{\max\{a,b\}}}\frac{1}{4\pi^{2}k^{2}ab}=\frac{1}{12ab}+O(\log^{-1/1000}P) |  |

This is trivial for a ​ b ≥ log 1 / 1000 ⁡ P ab\geq\log^{1/1000}P. For a ​ b ≤ log 1 / 1000 ⁡ P ab\leq\log^{1/1000}P the claim follows from the Basel identity

 | ∑ k = 1 ∞ 1 k 2 = π 2 6 \sum_{k=1}^{\infty}\frac{1}{k^{2}}=\frac{\pi^{2}}{6} |  |

and the tail bound

 | ∑ k ≥ log 1 / 1000 ⁡ P 1 k 2 ≪ log − 1 / 1000 P. \sum_{k\geq\log^{1/1000}P}\frac{1}{k^{2}}\ll\log^{-1/1000}P. |  |

∎

Now we can get back to proving Proposition 1.9 assuming Proposition 1.12. From Proposition 3.2 (i) and ( 3.4) we see that

(3.14) |  | c 1 ​ ( N, m) + c 1 ​ ( N, n − m) − c 1 ​ ( N, n) = c 1 ​ ( N, m ′) + c 1 ​ ( N, n ′ − m ′) − c 1 ​ ( N, n ′) + O ⁡ ( δ) c_{1}(N,m)+c_{1}(N,n-m)-c_{1}(N,n)=c_{1}(N,m^{\prime})+c_{1}(N,n^{\prime}-m^{\prime})-c_{1}(N,n^{\prime})+O(\delta) |  |

for N ∈ { m, n, n − m, m ′, n ′, m ′ − n ′ } N\in\{m,n,n-m,m^{\prime},n^{\prime},m^{\prime}-n^{\prime}\}, where for brevity we introduce the error tolerance

 | δ ≔ log − 1 / 1000 P. \delta\coloneqq\log^{-1/1000}P. |  |

We can now arrive at the desired contradiction by some case analysis (reminiscent of that in [24, 25]) using the remaining portions of Proposition 3.2, as follows.

### Case m ′ ≈ 0 m^{\prime}\approx 0

Applying ( 3.14) with N = m N=m, we conclude from Proposition 3.2 (ii) that

(3.15) |  | c 1 ​ ( m, m) + c 1 ​ ( m, n − m) − c 1 ​ ( m, n) = c 1 ​ ( m, n ′ − m ′) − c 1 ​ ( m, n ′) + O ⁡ ( δ). c_{1}(m,m)+c_{1}(m,n-m)-c_{1}(m,n)=c_{1}(m,n^{\prime}-m^{\prime})-c_{1}(m,n^{\prime})+O(\delta). |  |

From Lemma 3.1 (iii) we have m ≉ 0 m\not\approx 0 (and hence also n − m, n ′ − m ′, n ′ ≉ 0 n-m,n^{\prime}-m^{\prime},n^{\prime}\not\approx 0, since these quantities are greater than or equal to m m), hence by Proposition 3.2 (iii) we have c 1 ​ ( m, m) = 1 12 + O ⁡ ( δ) c_{1}(m,m)=\frac{1}{12}+O(\delta). Furthermore, since m ′ ≈ 0 m^{\prime}\approx 0, we see from Lemma 3.1 (ii) that, for 1 ≤ a, b ≤ log 1 / 100 ⁡ P 1\leq a,b\leq\log^{1/100}P, a ​ m ≈ b ⁡ ( n ′ − m ′) am\approx b(n^{\prime}-m^{\prime}) if and only if a ​ m ≈ b ​ n ′ am\approx bn^{\prime}. Hence Proposition 3.2 (iii) (iv) implies that

 | c 1 ​ ( m, n ′ − m ′) = c 1 ​ ( m, n ′) + O ⁡ ( δ). c_{1}(m,n^{\prime}-m^{\prime})=c_{1}(m,n^{\prime})+O(\delta). |  |

Plugging these facts into ( 3.15) and rearranging, we obtain

 | 1 12 + c 1 ​ ( m, n − m) = c 1 ​ ( m, n) + O ⁡ ( δ). \frac{1}{12}+c_{1}(m,n-m)=c_{1}(m,n)+O(\delta). |  |

But by Proposition 3.2 (iii), (iv) we know that c 1 ​ ( m, n − m) ≥ − O ⁡ ( δ) c_{1}(m,n-m)\geq-O(\delta), so that

 | c 1 ​ ( m, n) ≥ 1 12 + O ⁡ ( δ) c_{1}(m,n)\geq\frac{1}{12}+O(\delta) |  |

But since m ≉ n m\not\approx n (because m ≤ n / 2 m\leq n/2 and m ≉ 0 m\not\approx 0), another application of Proposition 3.2 (iii), (iv) gives

 | c 1 ​ ( m, n) ≤ 1 2 ​ 1 12 + O ⁡ ( δ), c_{1}(m,n)\leq\frac{1}{2}\frac{1}{12}+O(\delta), |  |

which is a contradiction.

Since m ′ m^{\prime} was the smallest element of { m, n, n − m, m ′, n ′, m ′ − n ′ } \{m,n,n-m,m^{\prime},n^{\prime},m^{\prime}-n^{\prime}\}, we now thus have N ≉ 0 N\not\approx 0 for all N ∈ { m, n, n − m, m ′, n ′, m ′ − n ′ } N\in\{m,n,n-m,m^{\prime},n^{\prime},m^{\prime}-n^{\prime}\}, and case (ii) of Proposition 3.2 no longer applies.

### Case m ≉ m ′ m\not\approx m^{\prime} and m ′ ≉ 0 m^{\prime}\not\approx 0

We apply ( 3.14) with N = m ′ N=m^{\prime} to conclude that

(3.16) |  | c 1 ​ ( m ′, m) + c 1 ​ ( m ′, n − m) − c 1 ​ ( m ′, n) = c 1 ​ ( m ′, m ′) + c 1 ​ ( m ′, n ′ − m ′) − c 1 ​ ( m ′, n ′) + O ⁡ ( δ). c_{1}(m^{\prime},m)+c_{1}(m^{\prime},n-m)-c_{1}(m^{\prime},n)=c_{1}(m^{\prime},m^{\prime})+c_{1}(m^{\prime},n^{\prime}-m^{\prime})-c_{1}(m^{\prime},n^{\prime})+O(\delta). |  |

Now if there are no co-prime positive integers a, b ≤ log 1 / 100 ⁡ P a,b\leq\log^{1/100}P such that a ​ m ′ ≈ b ​ n ′ am^{\prime}\approx bn^{\prime} or a ​ m ′ ≈ b ⁡ ( n ′ − m ′) am^{\prime}\approx b(n^{\prime}-m^{\prime}), then by Proposition 3.2 (iv) we have

 | c 1 ​ ( m ′, n ′ − m ′) − c 1 ​ ( m ′, n ′) = O ⁡ ( δ) c_{1}(m^{\prime},n^{\prime}-m^{\prime})-c_{1}(m^{\prime},n^{\prime})=O(\delta) |  |

On the other hand, if such co-prime integers exist, then a ​ m ′ ≈ b ​ n ′ am^{\prime}\approx bn^{\prime} if and only if ( a − b) ​ m ′ ≈ b ⁡ ( n ′ − m ′) (a-b)m^{\prime}\approx b(n^{\prime}-m^{\prime}) and necessarily a > b a>b, so that by Proposition 3.2 (iii) we have in this case

(3.17) |  | c 1 ​ ( m ′, n ′ − m ′) − c 1 ​ ( m ′, n ′) = 1 12 ​ ( a − b) ​ b − 1 12 ​ a ​ b − O ⁡ ( δ) ≥ − O ⁡ ( δ). c_{1}(m^{\prime},n^{\prime}-m^{\prime})-c_{1}(m^{\prime},n^{\prime})=\frac{1}{12(a-b)b}-\frac{1}{12ab}-O(\delta)\geq-O(\delta). |  |

Since Proposition 3.2 (iii) also gives c 1 ​ ( m ′, m ′) ≥ 1 / 12 + O ⁡ ( δ) c_{1}(m^{\prime},m^{\prime})\geq 1/12+O(\delta), combining with ( 3.16) we obtain that

(3.18) |  | c 1 ​ ( m ′, m) + c 1 ​ ( m ′, n − m) − c 1 ​ ( m ′, n) ≥ 1 12 − O ⁡ ( δ). c_{1}(m^{\prime},m)+c_{1}(m^{\prime},n-m)-c_{1}(m^{\prime},n)\geq\frac{1}{12}-O(\delta). |  |

On the other hand, since m ′ ≉ m m^{\prime}\not\approx m, we also have m ′ ≉ n − m m^{\prime}\not\approx n-m since n − m ≥ m > m ′ n-m\geq m>m^{\prime}. By Proposition 3.2 (iii), (iv), we have

 | c 1 ​ ( m ′, m) + c 1 ​ ( m ′, n − m) ≤ 1 12 ⋅ 1 2 + 1 12 ⋅ 1 2 + O ⁡ ( δ), c_{1}(m^{\prime},m)+c_{1}(m^{\prime},n-m)\leq\frac{1}{12}\cdot\frac{1}{2}+\frac{1}{12}\cdot\frac{1}{2}+O(\delta), |  |

which can be improved to

(3.19) |  | c 1 ​ ( m ′, m) + c 1 ​ ( m ′, n − m) ≤ 1 12 ⋅ 1 3 + 1 12 ⋅ 1 2 + O ⁡ ( δ), c_{1}(m^{\prime},m)+c_{1}(m^{\prime},n-m)\leq\frac{1}{12}\cdot\frac{1}{3}+\frac{1}{12}\cdot\frac{1}{2}+O(\delta), |  |

unless both m ≈ 2 ​ m ′ m\approx 2m^{\prime} and n − m ≈ 2 ​ m ′ n-m\approx 2m^{\prime}. Since by Proposition 3.2 (iii), (iv) we have c 1 ​ ( m ′, n) ≥ − O ⁡ ( δ) c_{1}(m^{\prime},n)\geq-O(\delta), the estimate ( 3.19) contradicts ( 3.18).

Hence we must have both m ≈ 2 ​ m ′ m\approx 2m^{\prime} and n − m ≈ 2 ​ m ′ n-m\approx 2m^{\prime}. But then Lemma 3.1 (ii) forces n ≈ 4 ​ m ′ n\approx 4m^{\prime}, hence by Proposition 3.2 (iii)

 | c 1 ​ ( m ′, m) + c 1 ​ ( m ′, n − m) − c 1 ​ ( m ′, n) = 1 12 ⋅ 1 2 + 1 12 ⋅ 1 2 − 1 12 ⋅ 1 4 + O ⁡ ( δ), c_{1}(m^{\prime},m)+c_{1}(m^{\prime},n-m)-c_{1}(m^{\prime},n)=\frac{1}{12}\cdot\frac{1}{2}+\frac{1}{12}\cdot\frac{1}{2}-\frac{1}{12}\cdot\frac{1}{4}+O(\delta), |  |

and we again contradict ( 3.18).

### Case m ≈ m ′ m\approx m^{\prime} and m ′ ≉ 0 m^{\prime}\not\approx 0

By Lemma 3.1 (iii), we must have n ≉ n ′ n\not\approx n^{\prime}. We apply ( 3.14) for N = n N=n to obtain

(3.20) |  | c 1 ​ ( n, m) + c 1 ​ ( n, n − m) − c 1 ​ ( n, n) = c 1 ​ ( n, m ′) + c 1 ​ ( n, n ′ − m ′) − c 1 ​ ( n, n ′) + O ⁡ ( δ). c_{1}(n,m)+c_{1}(n,n-m)-c_{1}(n,n)=c_{1}(n,m^{\prime})+c_{1}(n,n^{\prime}-m^{\prime})-c_{1}(n,n^{\prime})+O(\delta). |  |

Since m ≈ m ′ m\approx m^{\prime}, we have by Proposition 3.2 (iii), (iv) (using also Lemma 3.1 (ii)) that c 1 ​ ( n, m) = c 1 ​ ( n, m ′) + O ⁡ ( δ) c_{1}(n,m)=c_{1}(n,m^{\prime})+O(\delta). Proposition 3.2 (iii) also gives c 1 ​ ( n, n) = 1 / 12 + O ⁡ ( δ) c_{1}(n,n)=1/12+O(\delta). Plugging these into ( 3.20) and rearranging, we obtain

(3.21) |  | c 1 ​ ( n, n − m) + c 1 ​ ( n, n ′) = 1 12 + c 1 ​ ( n, n ′ − m ′) + O ⁡ ( δ). c_{1}(n,n-m)+c_{1}(n,n^{\prime})=\frac{1}{12}+c_{1}(n,n^{\prime}-m^{\prime})+O(\delta). |  |

Since n ≉ n ′ n\not\approx n^{\prime} and m ≉ 0 m\not\approx 0, we see from Proposition 3.2 (iii), (iv) that

(3.22) |  | c 1 ​ ( n, n − m) + c 1 ​ ( n, n ′) ≤ 1 12 ⋅ 1 2 + 1 12 ⋅ 1 2 + O ⁡ ( δ) c_{1}(n,n-m)+c_{1}(n,n^{\prime})\leq\frac{1}{12}\cdot\frac{1}{2}+\frac{1}{12}\cdot\frac{1}{2}+O(\delta) |  |

which can be improved to

(3.23) |  | c 1 ​ ( n, n − m) + c 1 ​ ( n, n ′) ≤ 1 12 ⋅ 1 3 + 1 12 ⋅ 1 2 + O ⁡ ( δ) c_{1}(n,n-m)+c_{1}(n,n^{\prime})\leq\frac{1}{12}\cdot\frac{1}{3}+\frac{1}{12}\cdot\frac{1}{2}+O(\delta) |  |

unless 2 ​ ( n − m) ≈ n 2(n-m)\approx n and n ′ ≈ 2 ​ n n^{\prime}\approx 2n. Now ( 3.23) contradicts ( 3.21) since by Proposition 3.2 (iii), (iv) c 1 ​ ( n, n ′ − m ′) ≥ − O ⁡ ( δ) c_{1}(n,n^{\prime}-m^{\prime})\geq-O(\delta).

Hence we can assume that 2 ​ ( n − m) ≈ n 2(n-m)\approx n and n ′ ≈ 2 ​ n n^{\prime}\approx 2n. But using m ≈ m ′ m\approx m^{\prime} and Lemma 3.1 (ii) this implies that 2 ​ ( n ′ − m ′) ≈ 3 ​ n 2(n^{\prime}-m^{\prime})\approx 3n, so that by ( 3.21) and Proposition 3.2 (iii) we obtain

 | c 1 ​ ( n, n − m) + c 1 ​ ( n, n ′) = 1 12 + c 1 ​ ( n, n ′ − m ′) + O ⁡ ( δ) = 1 12 + 1 12 ⋅ 1 2 ⋅ 3 + O ⁡ ( δ). c_{1}(n,n-m)+c_{1}(n,n^{\prime})=\frac{1}{12}+c_{1}(n,n^{\prime}-m^{\prime})+O(\delta)=\frac{1}{12}+\frac{1}{12}\cdot\frac{1}{2\cdot 3}+O(\delta). |  |

contradicting ( 3.22).

###### Remark 3.4.

Morally speaking, the ability to obtain a contradiction here reflects the fact that one cannot have an identity of the form

(3.24) |  | { m ​ x } + { ( n − m) ​ x } − { n ​ x } = { m ′ ​ x } + { ( n ′ − m ′) ​ x } − { n ′ ​ x } \{mx\}+\{(n-m)x\}-\{nx\}=\{m^{\prime}x\}+\{(n^{\prime}-m^{\prime})x\}-\{n^{\prime}x\} |  |

for almost all real numbers x x and some integers 1 ≤ m ≤ n / 2 1\leq m\leq n/2, 1 ≤ m ′ ≤ n ′ / 2 1\leq m^{\prime}\leq n^{\prime}/2 unless one has both m = m ′ m=m^{\prime} and n = n ′ n=n^{\prime} (this type of connection goes back to Landau [17, p. 116]). This latter fact is easily established by inspecting the jump discontinuities of both sides of ( 3.24), but it is also possible to establish it by computing the covariances of both sides of ( 3.24) with { N ​ x } \{Nx\} for various choices of N N, and the arguments above can be viewed as an adaptation of this latter method.

It remains to establish Proposition 1.12. This will be established in the next section.

## 4. Equidistribution

In this section we prove Proposition 1.12. Fix ε, A \varepsilon,A. We may assume that P P is sufficiently large depending on ε, A \varepsilon,A, as the claim is trivial otherwise. If we have P j ≥ M ​ log A ​ P P^{j}\geq M\log^{A}P then we can replace in both parts of the proposition M P j \frac{M}{P^{j}} by 0 0 with negligible error, so we may assume that either M = 0 M=0 or P j < M ​ log A ​ P P^{j}<M\log^{A}P. In either event we may thus assume that j ≤ log 1 / 2 ⁡ P j\leq\log^{1/2}P. Next, by partitioning I I into at most log 100 ⁡ P \log^{100}P intervals of length at most P ​ log − 100 ​ P P\log^{-100}P and using the triangle inequality, it suffices (after suitable adjustment of P P, A A) to assume that I ⊂ [P, P + P ​ log − 100 ​ P] I\subset[P,P+P\log^{-100}P]. In particular we have

(4.1) |  | P j − 1 ≤ t j − 1 ≤ 2 ​ P j − 1 P^{j-1}\leq t^{j-1}\leq 2P^{j-1} |  |

for all t ∈ I t\in I.

Let us first reduce Proposition 1.12 (ii) to Proposition 1.12 (i). We perform a Fourier expansion

 | W ⁡ ( x, y) = ∑ n, m ∈ ℤ c n, m ​ e ​ ( n ​ x + m ​ y) W(x,y)=\sum_{n,m\in\mathbb{Z}}c_{n,m}e(nx+my) |  |

where by integration by parts the Fourier coefficients

 | c n, m = ∫ ℝ 2 / ℤ 2 W ⁡ ( x, y) ​ e ​ ( − n ​ x − m ​ y) ​ 𝑑 x ​ 𝑑 y c_{n,m}=\int_{\mathbb{R}^{2}/\mathbb{Z}^{2}}W(x,y)e(-nx-my)\ dxdy |  |

obey the bounds

 | | c n, m | ≪ ‖ W ‖ C 3 ​ ( 1 + | n | + | m |) − 3. |c_{n,m}|\ll\|W\|_{C^{3}}(1+|n|+|m|)^{-3}. |  |

By the triangle inequality, the contributions of those frequencies n, m n,m with | n | + | m | ≥ log 2 ​ A ⁡ P |n|+|m|\geq\log^{2A}P is then acceptable. By a further application of the triangle inequality, Proposition 1.12 (ii) follows from showing that

 | ∑ p ∈ I e ⁡ ( n ​ N p + m ​ M p j) = ∫ I e ⁡ ( n ​ N t + m ​ M t j) ​ d ​ t log ⁡ t + O ε, A ​ ( P ​ log − 10 ​ A ​ P) \sum_{p\in I}e\left(n\frac{N}{p}+m\frac{M}{p^{j}}\right)=\int_{I}e\left(n\frac{N}{t}+m\frac{M}{t^{j}}\right)\ \frac{dt}{\log t}+O_{\varepsilon,A}(P\log^{-10A}P) |  |

whenever n, m n,m are integers with | n | + | m | ≤ log 2 ​ A ⁡ P |n|+|m|\leq\log^{2A}P. But this follows from Proposition 1.12 (i) by adjusting the values of ε, A, M, N \varepsilon,A,M,N suitably.

The proof of part (i) will use the standard tools of Vaughan’s identity and Vinogradov’s exponential sum estimates. We state a suitable form of the latter tool here:

###### Lemma 4.1 (Vinogradov’s exponential sum estimate).

Let X ≥ 2 X\geq 2, F ≥ X 4 F\geq X^{4}, and α ≥ 1 \alpha\geq 1. Let I ⊂ [X, 2 ​ X] I\subset[X,2X] be an interval. Let f ⁡ ( x) f(x) be a smooth function on I I satisfying for all t ∈ I t\in I

(4.2) |  | α − r 3 ​ F ≤ t r r! ​ | f ( r) ​ ( t) | ≤ α r 3 ​ F \displaystyle\alpha^{-r^{3}}F\leq\frac{t^{r}}{r!}|f^{(r)}(t)|\leq\alpha^{r^{3}}F |  |

for all integers 1 ≤ r ≤ 10 ​ ⌈ log ⁡ F / ( log ⁡ X) ⌉ + 1. 1\leq r\leq 10\lceil\log F/(\log X)\rceil+1. Assume further that

(4.3) |  | ( log ⁡ α) ​ ( log ⁡ F) 2 ( log ⁡ X) 3 < 10 − 3. \displaystyle(\log\alpha)\frac{(\log F)^{2}}{(\log X)^{3}}<10^{-3}. |  |

Then we have

(4.4) |  | ∑ n ∈ I e ( f ( n)) ≪ α X exp ( − 2 − 18 ( log X) 3 / ( log F) 2), \displaystyle\sum_{n\in I}e(f(n))\ll\alpha X\exp(-2^{-18}(\log X)^{3}/(\log F)^{2}), |  |

where the implied constant is absolute.

###### Proof.

This is essentially [12, Theorem 8.25] with minor modifications (the modification needed is that we only assume ( 4.2) for r r in a certain range, not all integers r ≥ 1 r\geq 1.).

Let R:= 10 ​ ⌈ log ⁡ F / ( log ⁡ X) ⌉ R:=10\lceil\log F/(\log X)\rceil, and as in [12, p. 217], let

 | F n ​ ( q):= ∑ 0 ≤ r ≤ R α r ​ ( n) ​ q r, α r ​ ( n) ≔ f ( r) ​ ( n) r!. \displaystyle F_{n}(q):=\sum_{0\leq r\leq R}\alpha_{r}(n)q^{r},\quad\alpha_{r}(n)\coloneqq\frac{f^{(r)}(n)}{r!}. |  |

Let S f ​ ( I) S_{f}(I) denote the sum in ( 4.4). By Taylor’s formula, for any q ≥ 1 q\geq 1 we have

 | S f ​ ( I) = ∑ n ∈ I e ⁡ ( F n ​ ( q)) + O ⁡ ( q + X ​ q R + 1 ​ max t ∈ I ⁡ | f ( R + 1) ​ ( t) | ( R + 1)!). \displaystyle S_{f}(I)=\sum_{n\in I}e(F_{n}(q))+O\left(q+Xq^{R+1}\frac{\max_{t\in I}|f^{(R+1)}(t)|}{(R+1)!}\right). |  |

Let 𝒬:= { x y: 1 ≤ x ≤ V, 1 ≤ y ≤ V } ∩ ℕ \mathcal{Q}:=\{xy:1\leq x\leq V,1\leq y\leq V\}\cap\mathbb{N}, where 𝒬 \mathcal{Q} is interpreted as a multiset. Also let Q = | 𝒬 | = V 2 Q=|\mathcal{Q}|=V^{2}. Then

 | S f ​ ( I) = ∑ n ∈ I | 𝒬 | − 1 ​ ∑ q ∈ 𝒬 e ⁡ ( F n ​ ( q)) + O ⁡ ( Q + X ​ Q R + 1 ​ max t ∈ I ⁡ | f ( R + 1) ​ ( t) | ( R + 1)!). \displaystyle S_{f}(I)=\sum_{n\in I}|\mathcal{Q}|^{-1}\sum_{q\in\mathcal{Q}}e(F_{n}(q))+O\left(Q+XQ^{R+1}\frac{\max_{t\in I}|f^{(R+1)}(t)|}{(R+1)!}\right). |  |

We take V = X 1 / 4 V=X^{1/4} in which case by ( 4.2) the error term is

(4.5) |  | ≪ X 1 / 2 + X ⋅ X ( R + 1) / 2 ​ α ( R + 1) 3 ​ F / X R + 1 ≪ X 1 / 2 + X − ( R + 1) / 4 α ( R + 1) 3 ⋅ ( F X 1 − ( R + 1) / 4). \begin{split}&\ll X^{1/2}+X\cdot X^{(R+1)/2}\alpha^{(R+1)^{3}}F/X^{R+1}\\ &\ll X^{1/2}+X^{-(R+1)/4}\alpha^{(R+1)^{3}}\cdot(FX^{1-(R+1)/4}).\end{split} |  |

The term in the parenthesis is ≤ F X 3 / 4 F − 10 / 4 ≤ 1 \leq FX^{3/4}F^{-10/4}\leq 1. Using also ( 4.3) we see that ( 4.5) is ≪ X 1 / 2 \ll X^{1/2} which is in particular smaller than the right-hand side of ( 4.4). The sum ∑ q ∈ 𝒬 e ⁡ ( F n ​ ( q)) \sum_{q\in\mathcal{Q}}e(F_{n}(q)) is precisely the one estimated in [12, pp. 217–225]. The only assumption needed of f f in that argument is ( 4.2), and the only restriction on F F and X X there is F ≥ X 4 F\geq X^{4}. Hence, we conclude that the lemma holds by following the analysis there verbatim. ∎

We now apply this estimate to obtain an estimate for an exponential sum over integers.

###### Proposition 4.2 (Exponential sums over integers).

Let ε > 0 \varepsilon>0, A ≥ 1 A\geq 1, X ≥ 2 X\geq 2, 2 ≤ j ≪ log 1 / 2 ⁡ X 2\leq j\ll\log^{1/2}X, and let N, M N,M be real numbers with N, M ≪ exp ⁡ ( O ⁡ ( log 3 / 2 − ε ⁡ X)) N,M\ll\exp(O(\log^{3/2-\varepsilon}X)). Let I I be an interval in [X, X + X ​ log − 100 ​ X] [X,X+X\log^{-100}X]. Then

(4.6) |  | ∑ n ∈ I e ( N n + M n j) ≪ ε, A X ( 1 + F) − c log O ⁡ ( A) X + X log − A X \sum_{n\in I}e\left(\frac{N}{n}+\frac{M}{n^{j}}\right)\ll_{\varepsilon,A}X(1+F)^{-c}\log^{O(A)}X+X\log^{-A}X |  |

for some absolute constant c > 0 c>0, where

 | F ≔ | N | X + | M | X j. F\coloneqq\frac{|N|}{X}+\frac{|M|}{X^{j}}. |  |

###### Proof.

We may assume without loss of generality that A A is sufficiently large, and X X is sufficiently large depending on ε, A \varepsilon,A. By hypothesis we have F ≪ exp ⁡ ( O ⁡ ( log 3 / 2 − ε ⁡ X)) F\ll\exp(O(\log^{3/2-\varepsilon}X)). We may assume that F ≥ log C ​ A ⁡ X F\geq\log^{CA}X for a large absolute constant C C, since the claim is trivial otherwise.

Let f: I → ℝ f\colon I\to\mathbb{R} denote the phase function

 | f ⁡ ( t) ≔ N t + M t j. f(t)\coloneqq\frac{N}{t}+\frac{M}{t^{j}}. |  |

Then for any r ≥ 1 r\geq 1 and t ∈ I t\in I we have

(4.7) |  | t r r! ​ | f ( r) ​ ( t) | = | N t + M r t j | ≍ X − 1 ​ | N + M r / t j − 1 | \frac{t^{r}}{r!}|f^{(r)}(t)|=\left|\frac{N}{t}+\frac{M_{r}}{t^{j}}\right|\asymp X^{-1}|N+M_{r}/t^{j-1}| |  |

where

 | M r ≔ ( r + j − 1 j − 1) ​ M. M_{r}\coloneqq\binom{r+j-1}{j-1}M. |  |

Since

 | 1 ≤ ( r + j − 1 j − 1) ≤ ( r + j) r = exp ⁡ ( r ​ log ⁡ ( r + j)) = exp ⁡ ( O ⁡ ( r 2 ​ log 2 ​ X)) 1\leq\binom{r+j-1}{j-1}\leq(r+j)^{r}=\exp(r\log(r+j))=\exp(O(r^{2}\log_{2}X)) |  |

we conclude that

 | M r = exp ⁡ ( O ⁡ ( r 2 ​ log 2 ​ X)) ​ M M_{r}=\exp(O(r^{2}\log_{2}X))M |  |

and

 | | N | X + | M r | X j = exp ⁡ ( O ⁡ ( r 2 ​ log 2 ​ X)) ​ F. \frac{|N|}{X}+\frac{|M_{r}|}{X^{j}}=\exp(O(r^{2}\log_{2}X))F. |  |

If | M r | ≤ | N | ​ X j − 1 / 4 |M_{r}|\leq|N|X^{j-1}/4 then from the triangle inequality and ( 4.1) we have

 | X − 1 ​ | N + M r / t j − 1 | ≍ X − 1 | N | = exp ⁡ ( O ⁡ ( r 2 ​ log 2 ​ X)) ​ F. X^{-1}|N+M_{r}/t^{j-1}|\asymp X^{-1}|N|=\exp(O(r^{2}\log_{2}X))F. |  |

Consider then the case | M r | > | N | ​ X j − 1 / 4 |M_{r}|>|N|X^{j-1}/4. We have the upper bound

 | X − 1 ​ | N + M r / t j − 1 | ≪ | M r | X j ≪ exp ⁡ ( O ⁡ ( r 2 ​ log 2 ​ X)) ​ F X^{-1}|N+M_{r}/t^{j-1}|\ll\frac{|M_{r}|}{X^{j}}\ll\exp(O(r^{2}\log_{2}X))F |  |

for all t ∈ I t\in I from the triangle inequality. Furthermore, since the function t ↦ − 1 / t j − 1 t\mapsto-1/t^{j-1} has derivative ≍ j / X j \asymp j/X^{j} on I I, we also have, for all t t outside of an interval of length O ⁡ ( X ​ log − 2 ​ A ​ X) O(X\log^{-2A}X), the lower bound

 | X − 1 ​ | N + M r / t j − 1 | ≫ | M r | X j ​ log − 3 ​ A ​ X ≫ exp ⁡ ( O ⁡ ( r 2 ​ log 2 ​ X)) ​ F ​ log − 3 ​ A ​ X. X^{-1}|N+M_{r}/t^{j-1}|\gg\frac{|M_{r}|}{X^{j}}\log^{-3A}X\gg\exp(O(r^{2}\log_{2}X))F\log^{-3A}X. |  |

If we set α ≔ log 4 ​ A ⁡ X \alpha\coloneqq\log^{4A}X and A A is sufficiently large, then we conclude from ( 4.7) and the bounds above that the estimate ( 4.2) holds for all 1 ≤ r ≤ log ⁡ X 1\leq r\leq\log X and all t ∈ I t\in I outside the union of O ⁡ ( log ⁡ X) O(\log X) intervals of length O ⁡ ( X ​ log − 2 ​ A ​ X) O(X\log^{-2A}X). The contribution of these exceptional intervals to ( 4.6) is negligible, and removing them splits I I up into at most O ⁡ ( log ⁡ X) O(\log X) subintervals, so by the triangle inequality it suffices to show that

 | ∑ n ∈ I ′ e ( N n + M n j) ≪ ε, A X log − 2 ​ A X \sum_{n\in I^{\prime}}e\left(\frac{N}{n}+\frac{M}{n^{j}}\right)\ll_{\varepsilon,A}X\log^{-2A}X |  |

for any subinterval I ′ I^{\prime} with the property that ( 4.2) holds for all t ∈ I ′ t\in I^{\prime} and 1 ≤ r ≤ log ⁡ X 1\leq r\leq\log X. If F ≥ X 4 F\geq X^{4}, we may apply Lemma 4.1 to conclude that

 | ∑ n ∈ I ′ e ⁡ ( N n + M n j) ≪ X ​ log 4 ​ A ​ X ​ exp ⁡ ( − c ​ log 2 ​ ε ​ X) \sum_{n\in I^{\prime}}e\left(\frac{N}{n}+\frac{M}{n^{j}}\right)\ll X\log^{4A}X\exp(-c\log^{2\varepsilon}X) |  |

for some absolute constant c > 0 c>0, and the claim follows. If instead F < X 4 F<X^{4}, we can apply the Weyl inequality [12, Theorem 8.4] with k = 5 k=5 to conclude that

 | ∑ n ∈ I ′ e ⁡ ( N n + M n j) ≪ α O ⁡ ( 1) ​ ( F / X 5 + 1 / F) c ​ X ​ log ⁡ X \sum_{n\in I^{\prime}}e\left(\frac{N}{n}+\frac{M}{n^{j}}\right)\ll\alpha^{O(1)}(F/X^{5}+1/F)^{c}X\log X |  |

for some absolute constant c > 0 c>0; since F ≥ log C ​ A ⁡ X F\geq\log^{CA}X, we obtain the claim by taking C C large enough. ∎

Now we prove Proposition 1.12 (i). We may assume without loss of generality that j ≥ 2 j\geq 2, since for j = 1 j=1 we can absorb the M M terms into the N N term (and add a dummy term with M = 0 M=0 and j = 2 j=2, say). By summation by parts (see e.g. [19, Lemma 2.2]), and adjusting A A as necessary, it suffices to show that

 | ∑ p ∈ I e ⁡ ( N p + M p j) ​ log ⁡ p = ∫ I e ⁡ ( N t + M t j) ​ 𝑑 t + O ε, A ​ ( P ​ log − 10 ​ A ​ P) \sum_{p\in I}e\left(\frac{N}{p}+\frac{M}{p^{j}}\right)\log p=\int_{I}e\left(\frac{N}{t}+\frac{M}{t^{j}}\right)\ dt+O_{\varepsilon,A}(P\log^{-10A}P) |  |

for all intervals I ⊂ [P, P + P ​ log − 100 ​ P] I\subset[P,P+P\log^{-100}P]. This is equivalent to

 | ∑ n ∈ I e ⁡ ( N n + M n j) ​ Λ ​ ( n) = ∫ I e ⁡ ( N t + M t j) ​ 𝑑 t + O ε, A ​ ( P ​ log − 10 ​ A ​ P), \sum_{n\in I}e\left(\frac{N}{n}+\frac{M}{n^{j}}\right)\Lambda(n)=\int_{I}e\left(\frac{N}{t}+\frac{M}{t^{j}}\right)\ dt+O_{\varepsilon,A}(P\log^{-10A}P), |  |

where Λ \Lambda is the von Mangoldt function, since the contribution of the prime powers is negligible. We introduce the quantity

 | F ≔ | N | P + | M | P j. F\coloneqq\frac{|N|}{P}+\frac{|M|}{P^{j}}. |  |

If F ≤ log C ​ A ⁡ P F\leq\log^{CA}P for some large absolute constant C > 0 C>0, then the total variation of the phase t ↦ N t + M t j t\mapsto\frac{N}{t}+\frac{M}{t^{j}} is O ⁡ ( log C ​ A ⁡ P) O(\log^{CA}P), and the claim readily follows from a further summation by parts (see e.g. [19, Lemma 2.2]) and the prime number theorem (with classical error term). Thus we may assume that

(4.8) |  | F > log C ​ A ⁡ P. F>\log^{CA}P. |  |

In this case, a change of variables t = P / s t=P/s gives

 | ∫ I e ( N t + M t j) d t = − P ∫ P / I e ( N P s + M P j s j) d ​ s s 2. \int_{I}e\left(\frac{N}{t}+\frac{M}{t^{j}}\right)\ dt=-P\int_{P/I}e\left(\frac{N}{P}s+\frac{M}{P^{j}}s^{j}\right)\ \frac{ds}{s^{2}}. |  |

The derivative of the phase here is N / P + j ​ s j − 1 ​ M / P j N/P+js^{j-1}M/P^{j} which, once C C is large enough, is ≥ log 10 ​ A ⁡ P \geq\log^{10A}P for all s ∈ P / I s\in P/I apart from an interval of length at most O ⁡ ( log − 10 ​ A ⁡ P) O(\log^{-10A}P). Hence by partial integration we get that

 | ∫ I e ⁡ ( N t + M t j) ​ 𝑑 t ≪ P ​ log − 10 ​ A ​ P \int_{I}e\left(\frac{N}{t}+\frac{M}{t^{j}}\right)\ dt\ll P\log^{-10A}P |  |

if C C is large enough, so it remains to establish the bound

 | ∑ n ∈ I e ⁡ ( N n + M n j) ​ Λ ​ ( n) ≪ P ​ log − 10 ​ A ​ P \sum_{n\in I}e\left(\frac{N}{n}+\frac{M}{n^{j}}\right)\Lambda(n)\ll P\log^{-10A}P |  |

under the hypothesis ( 4.8).

By Vaughan’s identity in the form of [12, Proposition 13.4] (with y = z = P 1 / 3 y=z=P^{1/3}), followed by a shorter-than-dyadic decomposition, we can write

 | Λ ⁡ ( n) = ∑ r ≤ R ( α r ∗ 1 ​ ( n) + α r ′ ∗ log ⁡ ( n) + β r ∗ γ r ​ ( n)) \displaystyle\Lambda(n)=\sum_{r\leq R}(\alpha_{r}*1(n)+\alpha_{r}^{\prime}*\log(n)+\beta_{r}*\gamma_{r}(n)) |  |

for n ∈ [P, 2 ​ P] n\in[P,2P], where ∗ *denotes Dirichlet convolution, and

 | R \displaystyle R | ≪ log O ⁡ ( 1) ⁡ P, \displaystyle\ll\log^{O(1)}P, |  |

 | | α r ​ ( n) |, | α r ′ ​ ( n) |, | β r ​ ( n) |, | γ r ​ ( n) | \displaystyle|\alpha_{r}(n)|,|\alpha^{\prime}_{r}(n)|,|\beta_{r}(n)|,|\gamma_{r}(n)| | ≪ log ⁡ P, \displaystyle\ll\log P, |  |

 | supp ⁡ ( α r), supp ⁡ ( α r ′) \displaystyle\mathrm{supp}(\alpha_{r}),\mathrm{supp}(\alpha^{\prime}_{r}) | ⊂ [M r, ( 1 + log − 100 ⁡ P) ​ M r], \displaystyle\subset[M_{r},(1+\log^{-100}P)M_{r}], |  |

 | supp ⁡ ( β r) \displaystyle\mathrm{supp}(\beta_{r}) | ⊂ [K r, ( 1 + log − 100 ⁡ P) ​ K r], \displaystyle\subset[K_{r},(1+\log^{-100}P)K_{r}], |  |

 | supp ⁡ ( γ r) \displaystyle\mathrm{supp}(\gamma_{r}) | ⊂ [N r, ( 1 + log − 100 ⁡ P) ​ N r], \displaystyle\subset[N_{r},(1+\log^{-100}P)N_{r}], |  |

 | 1 ≤ M r \displaystyle 1\leq M_{r} | ≪ P 2 / 3; \displaystyle\ll P^{2/3}; |  |

 | P 1 / 3 ≪ K r, N r \displaystyle P^{1/3}\ll K_{r},N_{r} | ≪ P 2 / 3 \displaystyle\ll P^{2/3} |  |

(the bound for the coefficients arising from Vaughan’s identiy is ≪ log ⁡ P \ll\log P since 1 ∗ Λ = log 1\ast\Lambda=\log). By the triangle inequality, it thus suffices to establish the Type I estimates

(4.9) |  | ∑ n ∈ I e ( N n + M n j) ( α r ∗ 1) ( n) ≪ ε, A P log − 11 ​ A P \sum_{n\in I}e\left(\frac{N}{n}+\frac{M}{n^{j}}\right)(\alpha_{r}*1)(n)\ll_{\varepsilon,A}P\log^{-11A}P |  |

and

(4.10) |  | ∑ n ∈ I e ( N n + M n j) ( α r ′ ∗ log) ( n) ≪ ε, A P log − 11 ​ A + 1 P \sum_{n\in I}e\left(\frac{N}{n}+\frac{M}{n^{j}}\right)(\alpha^{\prime}_{r}*\log)(n)\ll_{\varepsilon,A}P\log^{-11A+1}P |  |

as well as the Type II estimates

(4.11) |  | ∑ n ∈ I e ( N n + M n j) ( β r ∗ γ r) ( n) ≪ ε, A P log − 11 ​ A P \sum_{n\in I}e\left(\frac{N}{n}+\frac{M}{n^{j}}\right)(\beta_{r}*\gamma_{r})(n)\ll_{\varepsilon,A}P\log^{-11A}P |  |

for all 1 ≤ r ≤ R 1\leq r\leq R and I ⊂ [P, P + P ​ log − 100 ​ P] I\subset[P,P+P\log^{-100}P]. The second Type I estimate ( 4.10) follows from the first Type I estimate ( 4.9) (replacing α r \alpha_{r} with α r ′ \alpha^{\prime}_{r}) and a summation by parts (see e.g. [19, Lemma 2.2]), so it suffices to establish ( 4.9) and ( 4.11).

We begin with ( 4.9). By the triangle inequality, the left-hand side is bounded by

 | ≪ log ⁡ P ​ ∑ m ∈ [M r, ( 1 + log − 100 ⁡ P) ​ M r] | ∑ n ∈ 1 m ⋅ I e ⁡ ( N m ​ n + M m j ​ n j) |. \ll\log P\sum_{m\in[M_{r},(1+\log^{-100}P)M_{r}]}\left|\sum_{n\in\frac{1}{m}\cdot I}e\left(\frac{N}{mn}+\frac{M}{m^{j}n^{j}}\right)\right|. |  |

Applying Proposition 4.2 with X = P / m X=P/m and N / m N/m and M / m j M/m^{j} in place of N N and M M, we can bound this by

 | ≪ ε, A P log P ( ( 1 + F) c log O ⁡ ( A) P + log − 20 ​ A P) \ll_{\varepsilon,A}P\log P\left((1+F)^{c}\log^{O(A)}P+\log^{-20A}P\right) |  |

for some constant c > 0 c>0, and the claim now follows from ( 4.8).

Now we establish ( 4.11). We can assume that K r ​ N r ≍ P K_{r}N_{r}\asymp P, as the sum vanishes otherwise. By the triangle inequality, the left-hand side is bounded by

 | ≪ log ⁡ P ​ ∑ m ∈ [K r, ( 1 + log − 100 ⁡ P) ​ K r] | ∑ n ∈ 1 m ⋅ I γ r ​ ( n) ​ e ​ ( N m ​ n + M m j ​ n j) |. \ll\log P\sum_{m\in[K_{r},(1+\log^{-100}P)K_{r}]}\left|\sum_{n\in\frac{1}{m}\cdot I}\gamma_{r}(n)e\left(\frac{N}{mn}+\frac{M}{m^{j}n^{j}}\right)\right|. |  |

By Cauchy–Schwarz it suffices to show that

 | ∑ m ∈ [K r, ( 1 + log − 100 ⁡ P) ​ K r] | ∑ n ∈ 1 m ⋅ I γ r ​ ( n) ​ e ​ ( N m ​ n + M m j ​ n j) | 2 ≪ K r ​ N r 2 ​ log − 30 ​ A ​ P \sum_{m\in[K_{r},(1+\log^{-100}P)K_{r}]}\left|\sum_{n\in\frac{1}{m}\cdot I}\gamma_{r}(n)e\left(\frac{N}{mn}+\frac{M}{m^{j}n^{j}}\right)\right|^{2}\ll K_{r}N^{2}_{r}\log^{-30A}P |  |

(say). Rearranging, it suffices to show that

(4.12) |  | ∑ n, n ′ ∈ [N r, ( 1 + log − 100 ⁡ P) ​ N r] γ r ​ ( n) ​ γ r ​ ( n ′) ¯ ​ X n, n ′ ≪ K r ​ N r 2 ​ log − 30 ​ A ​ P \sum_{n,n^{\prime}\in[N_{r},(1+\log^{-100}P)N_{r}]}\gamma_{r}(n)\overline{\gamma_{r}(n^{\prime})}X_{n,n^{\prime}}\ll K_{r}N^{2}_{r}\log^{-30A}P |  |

where

 | X n, n ′ ≔ ∑ m ∈ [K r, ( 1 + log − 100 ⁡ P) ​ K r] ∩ 1 n ⋅ I ∩ 1 n ′ ⋅ I e ⁡ ( N ⁡ ( n ′ − n) n ​ n ′ ​ m + M ⁡ ( ( n ′) j − n j) n j ​ ( n ′) j ​ m j). X_{n,n^{\prime}}\coloneqq\sum_{m\in[K_{r},(1+\log^{-100}P)K_{r}]\cap\frac{1}{n}\cdot I\cap\frac{1}{n^{\prime}}\cdot I}e\left(\frac{N(n^{\prime}-n)}{nn^{\prime}m}+\frac{M((n^{\prime})^{j}-n^{j})}{n^{j}(n^{\prime})^{j}m^{j}}\right). |  |

By Proposition 4.2, we have

 | X n, n ′ ≪ ε, A K r ( ( 1 + | n ′ − n | N r F) − c log O ⁡ ( A) P + log − 40 ​ A P) X_{n,n^{\prime}}\ll_{\varepsilon,A}K_{r}\left(\left(1+\frac{|n^{\prime}-n|}{N_{r}}F\right)^{-c}\log^{O(A)}P+\log^{-40A}P\right) |  |

for some absolute constant 0 < c < 1 0<c<1. Bounding γ r ​ ( n) ​ γ r ​ ( n ′) ¯ ≪ log 2 ⁡ P \gamma_{r}(n)\overline{\gamma_{r}(n^{\prime})}\ll\log^{2}P and noting that

 | ∑ n ∈ [N r, ( 1 + log − 100 ⁡ P) ​ N r] ( 1 + | n ′ − n | N r ​ F) − c ≪ N r ​ F − c \sum_{n\in[N_{r},(1+\log^{-100}P)N_{r}]}\left(1+\frac{|n^{\prime}-n|}{N_{r}}F\right)^{-c}\ll N_{r}F^{-c} |  |

for all n ′ ∈ [N r, ( 1 + log − 100 ⁡ P) ​ N r] n^{\prime}\in[N_{r},(1+\log^{-100}P)N_{r}], we obtain the claim ( 4.12) from ( 4.8). This completes the proof of Proposition 1.12.

## 5. Multiplicity of the falling factorial

In this section we establish Theorem 1.8. We first observe that if 1 ≤ m ≤ n 1\leq m\leq n solves ( 1.8) for some sufficiently large t t, then

 | t = ( n) m ≥ ( m) m = m! ≫ ( m / e) m t=(n)_{m}\geq(m)_{m}=m!\gg(m/e)^{m} |  |

by Stirling’s formula. Hence we have an analogue of ( 1.5):

(5.1) |  | m ≪ log ⁡ t log 2 ⁡ t m\ll\frac{\log t}{\log_{2}t} |  |

Next, since

 | ( n − m) m < ( n) m ≤ n m (n-m)^{m}<(n)_{m}\leq n^{m} |  |

we have

(5.2) |  | t 1 / m ≤ n < t 1 / m + m t^{1/m}\leq n<t^{1/m}+m |  |

and we obtain an analogue

(5.3) |  | n ≍ t 1 / m = exp ⁡ ( log ⁡ t m) n\asymp t^{1/m}=\exp\left(\frac{\log t}{m}\right) |  |

of ( 1.6), ( 1.7).

Next, we obtain the following analogue of Proposition 1.9.

###### Proposition 5.1 (Distance estimate).

Suppose we have two solutions ( n, m), ( n ′, m ′) (n,m),(n^{\prime},m^{\prime}) to ( 1.8) in region { ( m, n) ∈ ℕ 2: 1 ≤ m ≤ n } \{(m,n)\in\mathbb{N}^{2}:1\leq m\leq n\}. Then one has

(5.4) |  | m ′ − m ≪ log ⁡ ( n + n ′). m^{\prime}-m\ll\log(n+n^{\prime}). |  |

Furthermore, if

(5.5) |  | exp ⁡ ( log 2 / 3 + ε ⁡ ( n + n ′)) ≤ m, m ′ ≤ ( n + n ′) 2 / 3 \exp(\log^{2/3+\varepsilon}(n+n^{\prime}))\leq m,m^{\prime}\leq(n+n^{\prime})^{2/3} |  |

for some ε > 0 \varepsilon>0, then we additionally have

(5.6) |  | n ′ − n ≪ A, ε m + m ′ log A ⁡ ( m + m ′) n^{\prime}-n\ll_{A,\varepsilon}\frac{m+m^{\prime}}{\log^{A}(m+m^{\prime})} |  |

for any A > 0 A>0.

###### Proof.

We begin with ( 5.4). We follow the arguments from [1, Proof of Theorem 4]. Taking 2 2 -valuations v 2 v_{2} of both sides of ( 1.8) and using ( 1.11) we have

 | ∑ j = 1 ∞ ( ⌊ n 2 j ⌋ − ⌊ n − m 2 j ⌋) = ∑ j = 1 ∞ ( ⌊ n ′ 2 j ⌋ − ⌊ n ′ − m ′ 2 j ⌋). \sum_{j=1}^{\infty}\left(\left\lfloor\frac{n}{2^{j}}\right\rfloor-\left\lfloor\frac{n-m}{2^{j}}\right\rfloor\right)=\sum_{j=1}^{\infty}\left(\left\lfloor\frac{n^{\prime}}{2^{j}}\right\rfloor-\left\lfloor\frac{n^{\prime}-m^{\prime}}{2^{j}}\right\rfloor\right). |  |

The summands here vanish unless j ≤ log ⁡ ( n + n ′) j\leq\log(n+n^{\prime}). Writing ⌊ x ⌋ = x + O ⁡ ( 1) \lfloor x\rfloor=x+O(1), we conclude that

 | ∑ 1 ≤ j ≤ log ⁡ ( n + n ′) m 2 j + O ⁡ ( log ⁡ ( n + n ′)) = ∑ 1 ≤ j ≤ log ⁡ ( n + n ′) m ′ 2 j + O ⁡ ( log ⁡ ( n + n ′)) \sum_{1\leq j\leq\log(n+n^{\prime})}\frac{m}{2^{j}}+O(\log(n+n^{\prime}))=\sum_{1\leq j\leq\log(n+n^{\prime})}\frac{m^{\prime}}{2^{j}}+O(\log(n+n^{\prime})) |  |

and ( 5.4) follows.

Now we prove ( 5.6). Fix A, ε > 0 A,\varepsilon>0. We may assume without loss of generality that m ′ < m m^{\prime}<m, so that n ′ > n n^{\prime}>n by ( 1.8). We may also assume t t is sufficiently large depending on A, ε A,\varepsilon, as the claim is trivial otherwise; from ( 5.5) this also implies that m, m ′, n, n ′ m,m^{\prime},n,n^{\prime} are sufficiently large depending on A, ε A,\varepsilon. Henceforth all implied constants are permitted to depend on A, ε A,\varepsilon. By ( 5.5) we have

 | log 2 / 3 + ε ⁡ n ≤ log ⁡ m \log^{2/3+\varepsilon}n\leq\log m |  |

while from ( 5.3) we have log ⁡ n ≍ log ⁡ t m \log n\asymp\frac{\log t}{m}. From this and ( 5.1) we have

(5.7) |  | m ≍ log ⁡ t log 2 ⁡ t m\asymp\frac{\log t}{\log_{2}t} |  |

and then

 | log ⁡ n ≪ log 2 1 2 / 3 + ε ​ t. \log n\ll\log^{\frac{1}{2/3+\varepsilon}}_{2}t. |  |

Similarly for m ′, n ′ m^{\prime},n^{\prime}. From ( 5.4) we conclude that

(5.8) |  | m − m ′ ≪ log 2 1 2 / 3 + ε ​ t ≪ log 1 2 / 3 + ε ⁡ m. m-m^{\prime}\ll\log^{\frac{1}{2/3+\varepsilon}}_{2}t\ll\log^{\frac{1}{2/3+\varepsilon}}m. |  |

In particular m ≍ m ′ m\asymp m^{\prime} and, combining ( 5.3) with ( 5.8) and ( 5.7), also n ≍ n ′ ​ t 1 / m − 1 / m ′ ≍ n ′ n\asymp n^{\prime}t^{1/m-1/m^{\prime}}\asymp n^{\prime}. Hence from ( 5.5) we see that

(5.9) |  | n, n ′ ≫ m 3 / 2. n,n^{\prime}\gg m^{3/2}. |  |

Also we have

 | log ⁡ t m ′ = log ⁡ t m + O ( log ⁡ t ​ log 1 2 / 3 + ε ​ m m 2) = log ⁡ t m + O ( m − 1 / 2) \frac{\log t}{m^{\prime}}=\frac{\log t}{m}+O\left(\frac{\log t\log^{\frac{1}{2/3+\varepsilon}}m}{m^{2}}\right)=\frac{\log t}{m}+O(m^{-1/2}) |  |

(say), hence on exponentiating and using ( 5.2), ( 5.9)

(5.10) |  | n ′ = exp ( log ⁡ t m ′) + O ( m) = n + O ( m − 1 / 2 n). n^{\prime}=\exp\left(\frac{\log t}{m^{\prime}}\right)+O(m)=n+O(m^{-1/2}n). |  |

Suppose that we could find a prime p > m p>m obeying the inequalities

(5.11) |  | max ⁡ ( 1 − { n ′ − n p }, 1 − m p) < { n − m p } < 1; { n ′ − n p } < 1 − m p. \max\left(1-\left\{\frac{n^{\prime}-n}{p}\right\},1-\frac{m}{p}\right)<\left\{\frac{n-m}{p}\right\}<1;\quad\left\{\frac{n^{\prime}-n}{p}\right\}<1-\frac{m}{p}. |  |

These inequalities imply in particular that

 | { n − m p } − 1 + m p ∈ [0, 1) ​ and ​ { n − m p } + { n ′ − n p } − 1 + m p ∈ [0, 1), \left\{\frac{n-m}{p}\right\}-1+\frac{m}{p}\in[0,1)\text{ and }\left\{\frac{n-m}{p}\right\}+\left\{\frac{n^{\prime}-n}{p}\right\}-1+\frac{m}{p}\in[0,1), |  |

so that these quantities respectively equal { n p } \{\frac{n}{p}\} and { n ′ p } \{\frac{n^{\prime}}{p}\}. Consequently, if ( 5.11) hold, then we would have

(5.12) |  | { n p } = { n − m p } − 1 + m p < m p \left\{\frac{n}{p}\right\}=\left\{\frac{n-m}{p}\right\}-1+\frac{m}{p}<\frac{m}{p} |  |

and (since m ′ < m m^{\prime}<m)

(5.13) |  | { n ′ p } = { n − m p } + { n ′ − n p } − 1 + m p ≥ m p ≥ m ′ p. \left\{\frac{n^{\prime}}{p}\right\}=\left\{\frac{n-m}{p}\right\}+\left\{\frac{n^{\prime}-n}{p}\right\}-1+\frac{m}{p}\geq\frac{m}{p}\geq\frac{m^{\prime}}{p}. |  |

Now ( 5.12) implies that p p divides ( n) m (n)_{m}, while ( 5.13) implies that p p does not divide ( n ′) m ′ (n^{\prime})_{m^{\prime}}. This contradicts the assumption ( n) m = t = ( n ′) m ′ (n)_{m}=t=(n^{\prime})_{m^{\prime}}. Thus there cannot be any prime p ≥ 2 ​ m p\geq 2m obeying ( 5.11).

Let w 1: ℝ → [0, 1] w_{1}\colon\mathbb{R}\to[0,1] be a suitable smooth ℤ \mathbb{Z} -periodic function supported on the region

 | { x ∈ ℝ: { x } ∈ ( 1 − log − 2 ​ A ⁡ m, 1) } \{x\in\mathbb{R}:\{x\}\in(1-\log^{-2A}m,1)\} |  |

chosen so that ∫ 0 1 w 1 ≫ log − 2 ​ A ⁡ m \int_{0}^{1}w_{1}\gg\log^{-2A}m and ‖ w 1 ‖ C 3 ≪ log 6 ​ A ⁡ m \|w_{1}\|_{C^{3}}\ll\log^{6A}m, and let w 2: ℝ → [0, 1] w_{2}\colon\mathbb{R}\to[0,1] similarly be a smooth ℤ \mathbb{Z} -periodic function supported on the region

 | { y ∈ ℝ: { y } ∈ ( log − 2 ​ A ⁡ m, 1 / 2) } \{y\in\mathbb{R}:\{y\}\in(\log^{-2A}m,1/2)\} |  |

chosen so that w 2 ​ ( y) = 1 w_{2}(y)=1 when { y } ∈ [2 ​ log − 2 ​ A ​ m, 1 / 4] \{y\}\in[2\log^{-2A}m,1/4] and ‖ w 2 ‖ C 3 ≪ log 6 ​ A ⁡ m \|w_{2}\|_{C^{3}}\ll\log^{6A}m. Let 𝐩 \mathbf{p} be a prime drawn uniformly from all the primes in [2 ​ m, 100 ​ m] [2m,100m]. As 𝐩 \mathbf{p} does not obey ( 5.11), we have

 | 𝐄 ​ w 1 ​ ( n − m 𝐩) ​ w 2 ​ ( n ′ − n 𝐩) = 0 \mathbf{E}w_{1}\left(\frac{n-m}{\mathbf{p}}\right)w_{2}\left(\frac{n^{\prime}-n}{\mathbf{p}}\right)=0 |  |

and hence by Proposition 1.12 (and dyadic decomposition)

 | ∫ 2 100 w 1 ​ ( n − m t ​ m) ​ w 2 ​ ( n ′ − n t ​ m) ​ 𝑑 t ≪ log − 100 ​ A ⁡ m, \int_{2}^{100}w_{1}\left(\frac{n-m}{tm}\right)w_{2}\left(\frac{n^{\prime}-n}{tm}\right)\ dt\ll\log^{-100A}m, |  |

or on changing variables t = 1 / s t=1/s

(5.14) |  | ∫ 1 / 100 1 / 2 w 1 ​ ( n − m m ​ s) ​ w 2 ​ ( n ′ − n m ​ s) ​ 𝑑 s ≪ log − 100 ​ A ⁡ m. \int_{1/100}^{1/2}w_{1}\left(\frac{n-m}{m}s\right)w_{2}\left(\frac{n^{\prime}-n}{m}s\right)\ ds\ll\log^{-100A}m. |  |

On the other hand, by ( 5.10), ( 5.9) we have

(5.15) |  | n − m m ≫ n m ≫ m 1 / 2 ​ n ′ − n m + m 1 / 2. \frac{n-m}{m}\gg\frac{n}{m}\gg m^{1/2}\frac{n^{\prime}-n}{m}+m^{1/2}. |  |

We perform a Fourier expansion

 | w 1 ​ ( x) = ∑ ℓ ∈ ℤ c ℓ ​ e ​ ( ℓ ​ x), w_{1}(x)=\sum_{\ell\in\mathbb{Z}}c_{\ell}e(\ell x), |  |

where by integration by parts the Fourier coefficients obey the bounds

 | | c ℓ | ≪ ( 1 + | ℓ |) − 3 ​ log 6 ​ A ​ m. |c_{\ell}|\ll(1+|\ell|)^{-3}\log^{6A}m. |  |

Thus ( 5.14) can then be rewritten as

(5.16) |  | ∑ ℓ ∈ ℤ c ℓ ​ ∫ 1 / 100 1 / 2 w 2 ​ ( n ′ − n m ​ s) ​ e ​ ( n − m m ​ ℓ ​ s) ​ 𝑑 s ≪ log − 100 ​ A ⁡ m. \sum_{\ell\in\mathbb{Z}}c_{\ell}\int_{1/100}^{1/2}w_{2}\left(\frac{n^{\prime}-n}{m}s\right)e\left(\frac{n-m}{m}\ell s\right)\ ds\ll\log^{-100A}m. |  |

By ( 5.15) and integration by parts, one readily establishes the bound

 | ∫ 1 / 100 1 / 2 w 2 ​ ( n ′ − n m ​ s) ​ e ​ ( n − m m ​ ℓ ​ s) ​ 𝑑 s ≪ log 6 ​ A ⁡ m | ℓ | ​ m 1 / 2 \int_{1/100}^{1/2}w_{2}\left(\frac{n^{\prime}-n}{m}s\right)e\left(\frac{n-m}{m}\ell s\right)\ ds\ll\frac{\log^{6A}m}{|\ell|m^{1/2}} |  |

for ℓ ≠ 0 \ell\neq 0. Thus the total contribution to the left-hand side of ( 5.16) from the terms with ℓ ≠ 0 \ell\neq 0 is negligible, and hence

 | c 0 ​ ∫ 1 / 100 1 / 2 w 2 ​ ( n ′ − n m ​ s) ​ 𝑑 s ≪ log − 100 ​ A ⁡ m. c_{0}\int_{1/100}^{1/2}w_{2}\left(\frac{n^{\prime}-n}{m}s\right)\ ds\ll\log^{-100A}m. |  |

Since c 0 = ∫ 0 1 w 1 ≫ log − 2 ​ A ⁡ m c_{0}=\int_{0}^{1}w_{1}\gg\log^{-2A}m and w 2 w_{2} equals 1 1 on [2 ​ log − 2 ​ A ​ m, 1 / 4] [2\log^{-2A}m,1/4], we have

(5.17) |  | f ⁡ ( n ′ − n m) ≪ log − 98 ​ A ⁡ m f\left(\frac{n^{\prime}-n}{m}\right)\ll\log^{-98A}m |  |

where

 | f ⁡ ( θ) ≔ ∫ 1 / 100 1 / 2 1 2 ​ log − 2 ​ A ​ m ≤ { θ ​ s } ≤ 1 / 4 ​ 𝑑 s. f(\theta)\coloneqq\int_{1/100}^{1/2}1_{2\log^{-2A}m\leq\{\theta s\}\leq 1/4}\ ds. |  |

However, direct calculation shows that when θ ≥ 3 \theta\geq 3, we have

 | f ⁡ ( θ) ≥ ∑ θ 16 ≤ n ≤ θ 2 − 1 4 ∫ ℝ 1 n + 1 / 100 ≤ θ ​ s ≤ n + 1 / 4 ​ 𝑑 s ≫ θ ⋅ θ − 1 = 1, f(\theta)\geq\sum_{\frac{\theta}{16}\leq n\leq\frac{\theta}{2}-\frac{1}{4}}\int_{\mathbb{R}}1_{n+1/100\leq\theta s\leq n+1/4}\ ds\gg\theta\cdot\theta^{-1}=1, |  |

when 1 / 2 < θ < 3 1/2<\theta<3, we have

 | f ⁡ ( θ) ≥ ∫ 1 30 ​ θ 1 20 ​ θ 𝑑 s ≍ 1, f(\theta)\geq\int_{\frac{1}{30\theta}}^{\frac{1}{20\theta}}\ ds\asymp 1, |  |

and, when 8 ​ log − A ​ m ≤ θ ≤ 1 / 2 8\log^{-A}m\leq\theta\leq 1/2, we have

 | f ⁡ ( θ) ≥ ∫ 1 / 4 1 / 2 𝑑 s ≍ 1. f(\theta)\geq\int_{1/4}^{1/2}\ ds\asymp 1. |  |

Hence ( 5.17) can only hold if

 | n ′ − n m ≪ log − A ⁡ m, \frac{n^{\prime}-n}{m}\ll\log^{-A}m, |  |

giving the claim ( 5.6). ∎

Now we adapt the analysis from Section 2. We extend the falling factorial ( n) m (n)_{m} to real n ≥ m ≥ 0 n\geq m\geq 0 by the formula

 | ( n) m ≔ Γ ⁡ ( n + 1) Γ ⁡ ( n − m + 1). (n)_{m}\coloneqq\frac{\Gamma(n+1)}{\Gamma(n-m+1)}. |  |

From the increasing nature of the digamma function ψ \psi we see that for fixed m m, ( n) m (n)_{m} increases from Γ ⁡ ( m + 2) \Gamma(m+2) when n n goes from m + 1 m+1 to infinity. Applying the inverse function theorem, we conclude that for any sufficiently large t t there is a unique smooth function g t: { m > 0: Γ ⁡ ( m + 2) ≤ t } → ℝ g_{t}\colon\{m>0:\Gamma(m+2)\leq t\}\to\mathbb{R} such that for any m > 0 m>0 with Γ ⁡ ( m + 2) ≤ t \Gamma(m+2)\leq t, one has g t ​ ( m) ≥ m g_{t}(m)\geq m and

(5.18) |  | ( g t ​ ( m)) m = t. (g_{t}(m))_{m}=t. |  |

Indeed, one could simply set g t ​ ( m) ≔ f t / Γ ⁡ ( m + 1) ​ ( m) g_{t}(m)\coloneqq f_{t/\Gamma(m+1)}(m), where f t f_{t} is the function studied in Section 2.

We have an analogue of Proposition 2.1:

###### Proposition 5.2 (Estimates on the first few derivatives).

Let C > 1 C>1, and let t, m t,m be sufficiently large depending on C C with Γ ⁡ ( m + 2) ≤ t \Gamma(m+2)\leq t. Then

(5.19) |  | g t ​ ( m) ≍ t 1 / m. g_{t}(m)\asymp t^{1/m}. |  |

In the range m ≤ g t ​ ( m) / 2 m\leq g_{t}(m)/2, we have

(5.20) |  | − g t ′ ​ ( m) ≍ g t ​ ( m) ​ log ⁡ t m 2 -g^{\prime}_{t}(m)\asymp g_{t}(m)\frac{\log t}{m^{2}} |  |

and in the range m ≤ g t ​ ( m) − C ​ log 2 ​ g t ​ ( m) m\leq g_{t}(m)-C\log^{2}g_{t}(m), one has

(5.21) |  | 0 < g t ′′ ​ ( m) ≪ g t ​ ( m) ​ ( log ⁡ t m 2) 2 + C − 1 ​ log − 3 ​ m. 0<g^{\prime\prime}_{t}(m)\ll g_{t}(m)\left(\frac{\log t}{m^{2}}\right)^{2}+C^{-1}\log^{-3}m. |  |

###### Proof.

Write n = g t ​ ( m) ≥ m n=g_{t}(m)\geq m. First note that ( 5.19) is simply ( 5.3). Taking logarithms in ( 5.18) we have

(5.22) |  | log ⁡ Γ ⁡ ( g t ​ ( m) + 1) − log ⁡ Γ ⁡ ( g t ​ ( m) − m + 1) = log ⁡ t. \log\Gamma(g_{t}(m)+1)-\log\Gamma(g_{t}(m)-m+1)=\log t. |  |

If we differentiate ( 5.22) we obtain

(5.23) |  | g t ′ ​ ( m) ​ ψ ​ ( g t ​ ( m) + 1) − ( g t ′ ​ ( m) − 1) ​ ψ ​ ( g t ​ ( m) − m + 1) = 0. g^{\prime}_{t}(m)\psi(g_{t}(m)+1)-(g^{\prime}_{t}(m)-1)\psi(g_{t}(m)-m+1)=0. |  |

In particular we obtain the first derivative formula

(5.24) |  | g t ′ ​ ( m) = − ψ ⁡ ( n − m + 1) ψ ⁡ ( n + 1) − ψ ⁡ ( n − m + 1). g^{\prime}_{t}(m)=\frac{-\psi(n-m+1)}{\psi(n+1)-\psi(n-m+1)}. |  |

In the regime m ≤ n / 2 m\leq n/2 we can then obtain ( 5.20) from ( 2.12), ( 2.1), ( 5.19).

Differentiating ( 5.23) again, we conclude

 | g t ′′ ​ ( m) ​ ψ ​ ( n + 1) + ( g t ′ ​ ( m)) 2 ​ ψ ′ ​ ( n + 1) − g t ′′ ​ ( m) ​ ψ ​ ( n − m + 1) − ( g t ′ ​ ( m) − 1) 2 ​ ψ ′ ​ ( n − m + 1) = 0 g^{\prime\prime}_{t}(m)\psi(n+1)+(g^{\prime}_{t}(m))^{2}\psi^{\prime}(n+1)-g^{\prime\prime}_{t}(m)\psi(n-m+1)-(g^{\prime}_{t}(m)-1)^{2}\psi^{\prime}(n-m+1)=0 |  |

which we can rearrange using ( 5.24) as

(5.25) |  | g t ′′ ​ ( m) ​ ( ψ ⁡ ( n + 1) − ψ ⁡ ( n − m + 1)) 3 = ψ ​ ( n + 1) 2 ​ ψ ′ ​ ( n − m + 1) − ψ ​ ( n − m + 1) 2 ​ ψ ′ ​ ( n + 1). \begin{split}g^{\prime\prime}_{t}(m)(\psi(n+1)-\psi(n-m+1))^{3}&=\psi(n+1)^{2}\psi^{\prime}(n-m+1)\\ &\quad-\psi(n-m+1)^{2}\psi^{\prime}(n+1).\end{split} |  |

Suppose first that m ≤ n / 2 m\leq n/2. Then ( 2.12) applies, and it suffices to show that

 | ψ ​ ( n + 1) 2 ​ ψ ′ ​ ( n − m + 1) − ψ ​ ( n − m + 1) 2 ​ ψ ′ ​ ( n + 1) ≍ ( m n) 3 ​ n ​ ( log ⁡ t m 2) 2. \psi(n+1)^{2}\psi^{\prime}(n-m+1)-\psi(n-m+1)^{2}\psi^{\prime}(n+1)\asymp\left(\frac{m}{n}\right)^{3}n\left(\frac{\log t}{m^{2}}\right)^{2}. |  |

By ( 5.19) the right-hand side is ≍ m ​ log 2 ​ n n 2 \asymp\frac{m\log^{2}n}{n^{2}}. On the other hand, from the mean value theorem and ( 2.1), ( 2.2), ( 2.3) we have

 | 0 < ψ ​ ( n + 1) 2 ​ ( ψ ′ ​ ( n − m + 1) − ψ ′ ​ ( n + 1)) ≍ m ​ log 2 ​ n n 2 0<\psi(n+1)^{2}(\psi^{\prime}(n-m+1)-\psi^{\prime}(n+1))\asymp\frac{m\log^{2}n}{n^{2}} |  |

and

 | 0 < ( ψ ​ ( n + 1) 2 − ψ ​ ( n − m + 1) 2) ​ ψ ′ ​ ( n + 1) ≪ m ​ log ⁡ n n 2 0<(\psi(n+1)^{2}-\psi(n-m+1)^{2})\psi^{\prime}(n+1)\ll\frac{m\log n}{n^{2}} |  |

giving the claim.

Now suppose that n / 2 ≤ m ≤ n − C ​ log 2 ​ n n/2\leq m\leq n-C\log^{2}n. From ( 2.1), ( 2.2) we have

 | ψ ⁡ ( n + 1) − ψ ⁡ ( n − m + 1) \displaystyle\psi(n+1)-\psi(n-m+1) | ≍ log ⁡ n n − m \displaystyle\asymp\log\frac{n}{n-m} |  |

 | ψ ​ ( n + 1) 2 ​ ( ψ ′ ​ ( n − m + 1) − ψ ′ ​ ( n + 1)) \displaystyle\psi(n+1)^{2}(\psi^{\prime}(n-m+1)-\psi^{\prime}(n+1)) | ≍ log 2 ⁡ n n − m \displaystyle\asymp\frac{\log^{2}n}{n-m} |  |

 | 0 < ( ψ ​ ( n + 1) 2 − ψ ​ ( n − m + 1) 2) ​ ψ ′ ​ ( n + 1) \displaystyle 0<(\psi(n+1)^{2}-\psi(n-m+1)^{2})\psi^{\prime}(n+1) | ≪ log 2 ⁡ n n \displaystyle\ll\frac{\log^{2}n}{n} |  |

and hence by ( 5.25)

 | g t ′′ ​ ( m) ≍ log 2 ⁡ n ( n − m) ​ log 3 ​ n n − m. g_{t}^{\prime\prime}(m)\asymp\frac{\log^{2}n}{(n-m)\log^{3}\frac{n}{n-m}}. |  |

Since n 2 ≥ n − m ≥ C ​ log 2 ​ n \frac{n}{2}\geq n-m\geq C\log^{2}n, we have

 | ( n − m) ​ log 3 ​ n n − m ≫ C ​ log 5 ​ n (n-m)\log^{3}\frac{n}{n-m}\gg C\log^{5}n |  |

(as can be seen by checking the cases n − m ≤ n n-m\leq\sqrt{n} and n − m > n n-m>\sqrt{n} separately), and the claim follows. ∎

Now we can establish Theorem 1.8. Let C > 0 C>0 be a large absolute constant, let ε > 0 \varepsilon>0, and suppose that t t is sufficiently large depending on ε, C \varepsilon,C. Let ( n, m) (n,m) be the integer solution to ( 1.8) in the region exp ⁡ ( log 2 / 3 + ε ⁡ n) ≤ m ≤ n − 1 \exp(\log^{2/3+\varepsilon}n)\leq m\leq n-1 with a maximal value of m m; we may assume that such a solution exists, since we are done otherwise. If ( n ′, m ′) (n^{\prime},m^{\prime}) is any other solution in this region, then m ′ < m m^{\prime}<m and n < n ′ n<n^{\prime}. Note that n, n ′, m, m ′ n,n^{\prime},m,m^{\prime} are sufficiently large depending on ε, C \varepsilon,C. From Proposition 5.1 and ( 5.3) we have

 | m − m ′ ≪ log ⁡ n ′ ≪ log ⁡ t m ′ m-m^{\prime}\ll\log n^{\prime}\ll\frac{\log t}{m^{\prime}} |  |

and from ( 5.3) and ( 5.1)

 | m ′ ≍ log ⁡ t log ⁡ n ′ ≥ log ⁡ t log 1 2 / 3 + ε ⁡ m ′ ≫ log ⁡ t log 2 1 2 / 3 + ε ​ t m^{\prime}\asymp\frac{\log t}{\log n^{\prime}}\geq\frac{\log t}{\log^{\frac{1}{2/3+\varepsilon}}m^{\prime}}\gg\frac{\log t}{\log^{\frac{1}{2/3+\varepsilon}}_{2}t} |  |

and thus m ′ ≍ m m^{\prime}\asymp m and log ⁡ t m = log ⁡ t m ′ + O ⁡ ( 1) \frac{\log t}{m}=\frac{\log t}{m^{\prime}}+O(1). Hence n ≍ n ′ n\asymp n^{\prime} and

(5.26) |  | m − m ′ ≪ log ⁡ n. m-m^{\prime}\ll\log n. |  |

First suppose that m ≤ n 1 / 2 ​ log 10 ​ n m\leq n^{1/2}\log^{10}n. Here we will exploit the fact that n n grows rapidly as m m decreases. From Proposition 5.1 we have

 | n ′ − n ≪ ε m log 200 ⁡ m ≪ m log 100 ⁡ n. n^{\prime}-n\ll_{\varepsilon}\frac{m}{\log^{200}m}\ll\frac{m}{\log^{100}n}. |  |

On the other hand, from ( 5.20) and the mean value theorem we have

 | n ′ − n = g t ​ ( m ′) − g t ​ ( m) ≫ n ​ log ⁡ t m 2 ​ ( m − m ′) ≥ n m n^{\prime}-n=g_{t}(m^{\prime})-g_{t}(m)\gg\frac{n\log t}{m^{2}}(m-m^{\prime})\geq\frac{n}{m} |  |

thanks to ( 5.1) and the trivial bound m − m ′ ≥ 1 m-m^{\prime}\geq 1. Thus we have

 | n m ≪ m log 100 ⁡ n \frac{n}{m}\ll\frac{m}{\log^{100}n} |  |

but this contradicts the hypothesis m ≤ n 1 / 2 ​ log 10 ​ n m\leq n^{1/2}\log^{10}n.

Now suppose we are in the regime

 | n 1 / 2 ​ log 10 ​ n < m ≤ n − C ​ log 2 ​ n. n^{1/2}\log^{10}n<m\leq n-C\log^{2}n. |  |

Here we will take advantage of the convexity properties of g t g_{t}. From ( 5.26), m ′ m^{\prime} lies in the interval [m − O ⁡ ( log ⁡ n), m] [m-O(\log n),m]. By ( 5.19), for all x x in this interval, we have

 | g t ​ ( x) ≍ t 1 / x ≍ t 1 / m ≍ n g_{t}(x)\asymp t^{1/x}\asymp t^{1/m}\asymp n |  |

and by ( 5.21), we have

 | 0 < g t ′′ ​ ( x) \displaystyle 0<g^{\prime\prime}_{t}(x) | ≪ g t ​ ( x) ​ ( log ⁡ t x 2) 2 + C − 1 ​ log − 3 ​ x \displaystyle\ll g_{t}(x)\left(\frac{\log t}{x^{2}}\right)^{2}+C^{-1}\log^{-3}x |  |

 |  | ≪ n ​ ( log ⁡ t m 2) 2 + C − 1 ​ log − 3 ​ m \displaystyle\ll n\left(\frac{\log t}{m^{2}}\right)^{2}+C^{-1}\log^{-3}m |  |

 |  | ≪ n ​ ( log ⁡ n m) 2 + C − 1 ​ log − 3 ​ n \displaystyle\ll n\left(\frac{\log n}{m}\right)^{2}+C^{-1}\log^{-3}n |  |

 |  | ≪ C − 1 ​ log − 3 ​ n \displaystyle\ll C^{-1}\log^{-3}n |  |

since m > n 1 / 2 ​ log 10 ​ n m>n^{1/2}\log^{10}n. Applying Lemma 2.2 with k = 2 k=2, we see (for C C large enough) that there are at most two integers m ′ m^{\prime} in this interval with g t ​ ( m ′) g_{t}(m^{\prime}) an integer, giving Theorem 1.8 follows in this case.

It remains to handle the case

(5.27) |  | n − C ​ log 2 ​ n < m ≤ n − 1. n-C\log^{2}n<m\leq n-1. |  |

Recall from ( 5.26) that m ′ m^{\prime} lies in the interval [m − O ⁡ ( log ⁡ n), m] [m-O(\log n),m]. From ( 5.3), ( 5.27) we have

 | m ≍ n ≍ log ⁡ t log 2 ⁡ t m\asymp n\asymp\frac{\log t}{\log_{2}t} |  |

so m ′ = m − O ⁡ ( log 2 ⁡ t) m^{\prime}=m-O(\log_{2}t). From ( 5.3) again we thus also have

 | m ′ ≍ n ′ ≍ log ⁡ t log 2 ⁡ t. m^{\prime}\asymp n^{\prime}\asymp\frac{\log t}{\log_{2}t}. |  |

From ( 1.8) we have

 | n ′ n ′ − m ′ ​ n ′ − 1 n ′ − 1 − m ′ ​ … ​ n + 1 n + 1 − m ′ = ( n − m ′) ​ … ​ ( n − m + 1). \frac{n^{\prime}}{n^{\prime}-m^{\prime}}\frac{n^{\prime}-1}{n^{\prime}-1-m^{\prime}}\dots\frac{n+1}{n+1-m^{\prime}}=(n-m^{\prime})\dots(n-m+1). |  |

The right-hand side is at most exp ⁡ ( O ⁡ ( log 2 ⁡ t ​ log 3 ​ t)) \exp(O(\log_{2}t\log_{3}t)). This implies that n ′ − n ≪ log 3 ⁡ t n^{\prime}-n\ll\log_{3}t, since otherwise the left hand side would be, for any C ≥ 1 C\geq 1,

 | ≫ ( n n − m ′ + 1 + C ​ log 3 ​ t) C ​ log 3 ​ t ≫ exp ⁡ ( C 2 ​ log 3 ​ t ​ log 2 ​ t) \gg\left(\frac{n}{n-m^{\prime}+1+C\log_{3}t}\right)^{C\log_{3}t}\gg\exp\left(\frac{C}{2}\log_{3}t\log_{2}t\right) |  |

which contradicts the bound for the right hand side when C C is sufficiently large.

In particular we have from the triangle inequality that

 | n − m, n ′ − m ′ ≪ C ​ log 2 2 ​ t. n-m,n^{\prime}-m^{\prime}\ll C\log^{2}_{2}t. |  |

Making the change of variables ℓ:= n − m \ell:=n-m, it now suffices to show that there are at most two integer solutions to the equation

(5.28) |  | ( n) n − ℓ = t (n)_{n-\ell}=t |  |

in the regime 1 ≤ ℓ ≪ C ​ log 2 2 ​ t 1\leq\ell\ll C\log^{2}_{2}t. We write this equation ( 5.28) as

 | n! = t ​ ℓ! n!=t\ell! |  |

or equivalently

 | n = h t ​ ( ℓ) n=h_{t}(\ell) |  |

where h t ​ ( x) ≔ Γ − 1 ​ ( t ​ Γ ​ ( x + 1)) − 1 h_{t}(x)\coloneqq\Gamma^{-1}(t\Gamma(x+1))-1, and Γ − 1: [1, + ∞) → [2, + ∞) \Gamma^{-1}\colon[1,+\infty)\to[2,+\infty) is the inverse of the gamma function. Here we will exploit the very slowly varying nature of h t h_{t}. From Stirling’s formula we have

 | h t ​ ( x) ≍ log ⁡ t log 2 ⁡ t h_{t}(x)\asymp\frac{\log t}{\log_{2}t} |  |

whenever 1 ≤ x ≪ C ​ log 2 2 ​ t 1\leq x\ll C\log^{2}_{2}t. Taking the logarithmic derivative of the equation

 | Γ ⁡ ( h t ​ ( x) + 1) = t ​ Γ ​ ( x + 1) \Gamma(h_{t}(x)+1)=t\Gamma(x+1) |  |

we have

 | h t ′ ​ ( x) ​ ψ ​ ( h t ​ ( x) + 1) = ψ ⁡ ( x + 1). h^{\prime}_{t}(x)\psi(h_{t}(x)+1)=\psi(x+1). |  |

Hence by ( 2.1)

 | h t ′ ​ ( x) ≍ log ⁡ x log ⁡ h t ​ ( x) ≪ log 3 ⁡ t log 2 ⁡ t h^{\prime}_{t}(x)\asymp\frac{\log x}{\log h_{t}(x)}\ll\frac{\log_{3}t}{\log_{2}t} |  |

in the regime 1 ≤ x ≪ C ​ log 2 2 ​ t 1\leq x\ll C\log^{2}_{2}t. In particular, for two solutions ( n, ℓ), ( n ′, ℓ ′) (n,\ell),(n^{\prime},\ell^{\prime}) to ( 5.28) in this regime we have

(5.29) |  | n − n ′ ≪ log 3 ⁡ t log 2 ⁡ t ​ | ℓ − ℓ ′ |. n-n^{\prime}\ll\frac{\log_{3}t}{\log_{2}t}|\ell-\ell^{\prime}|. |  |

For fixed n n there is at most one ℓ ≥ 1 \ell\geq 1 solving ( 5.28). We conclude that for two distinct solutions ( n, ℓ), ( n ′, ℓ ′) (n,\ell),(n^{\prime},\ell^{\prime}) to ( 5.28) in this regime, we have | n − n ′ | ≥ 1 |n-n^{\prime}|\geq 1, and hence the separation

 | | ℓ − ℓ ′ | ≫ log 2 ⁡ t log 3 ⁡ t. |\ell-\ell^{\prime}|\gg\frac{\log_{2}t}{\log_{3}t}. |  |

Now suppose we have three solutions ( n 1, ℓ 1), ( n 2, ℓ 2), ( n 3, ℓ 3) (n_{1},\ell_{1}),(n_{2},\ell_{2}),(n_{3},\ell_{3}) to ( 5.28) in this regime. We can order ℓ 1 < ℓ 2 < ℓ 3 \ell_{1}<\ell_{2}<\ell_{3}, so that n 1 < n 2 < n 3 n_{1}<n_{2}<n_{3}. From the preceding discussion we have

 | log 2 ⁡ t log 3 ⁡ t ≪ ℓ 2 − ℓ 1, ℓ 3 − ℓ 2 ≪ C ​ log 2 2 ​ t \frac{\log_{2}t}{\log_{3}t}\ll\ell_{2}-\ell_{1},\ell_{3}-\ell_{2}\ll C\log^{2}_{2}t |  |

and

 | 1 ≤ n 2 − n 1, n 3 − n 2 ≪ C ​ log 2 ​ t ​ log 3 ​ t. 1\leq n_{2}-n_{1},n_{3}-n_{2}\ll C\log_{2}t\log_{3}t. |  |

If 2 j 2^{j} is a power of 2 2 that divides an integer in ( n 1, n 2] (n_{1},n_{2}] as well as an integer in ( n 2, n 3] (n_{2},n_{3}], then we must therefore have 2 j ≪ C ​ log 2 ​ t ​ log 3 ​ t 2^{j}\ll C\log_{2}t\log_{3}t, so that j ≪ log 3 ⁡ t j\ll\log_{3}t. Thus, there must exist i = 1, 2 i=1,2 such that the interval ( n i, n i + 1] (n_{i},n_{i+1}] only contains multiples of 2 j 2^{j} when j ≪ log 3 ⁡ t j\ll\log_{3}t. Fix this i i. Taking 2 2 -adic valuations of ( 5.28) using ( 1.11) we have

 | ∑ j = 1 ∞ ⌊ n i 2 j ⌋ = v 2 ​ ( t) + ∑ j = 1 ∞ ⌊ ℓ i 2 j ⌋ \sum_{j=1}^{\infty}\left\lfloor\frac{n_{i}}{2^{j}}\right\rfloor=v_{2}(t)+\sum_{j=1}^{\infty}\left\lfloor\frac{\ell_{i}}{2^{j}}\right\rfloor |  |

and

 | ∑ j = 1 ∞ ⌊ n i + 1 2 j ⌋ = v 2 ​ ( t) + ∑ j = 1 ∞ ⌊ ℓ i + 1 2 j ⌋ \sum_{j=1}^{\infty}\left\lfloor\frac{n_{i+1}}{2^{j}}\right\rfloor=v_{2}(t)+\sum_{j=1}^{\infty}\left\lfloor\frac{\ell_{i+1}}{2^{j}}\right\rfloor |  |

and thus

(5.30) |  | ∑ j = 1 ∞ ( ⌊ n i + 1 2 j ⌋ − ⌊ n i 2 j ⌋) = ∑ j = 1 ∞ ( ⌊ ℓ i + 1 2 j ⌋ − ⌊ ℓ i 2 j ⌋). \sum_{j=1}^{\infty}\left(\left\lfloor\frac{n_{i+1}}{2^{j}}\right\rfloor-\left\lfloor\frac{n_{i}}{2^{j}}\right\rfloor\right)=\sum_{j=1}^{\infty}\left(\left\lfloor\frac{\ell_{i+1}}{2^{j}}\right\rfloor-\left\lfloor\frac{\ell_{i}}{2^{j}}\right\rfloor\right). |  |

Since

(5.31) |  | ℓ i + 1 − ℓ i ≫ log 2 ⁡ t log 3 ⁡ t, \ell_{i+1}-\ell_{i}\gg\frac{\log_{2}t}{\log_{3}t}, |  |

we certainly have ℓ i + 1 − ℓ i ≥ 2 \ell_{i+1}-\ell_{i}\geq 2, and the right-hand side of ( 5.30) is at least

 | ⌊ ℓ i + 1 2 ⌋ − ⌊ ℓ i 2 ⌋ ≫ ℓ i + 1 − ℓ i. \left\lfloor\frac{\ell_{i+1}}{2}\right\rfloor-\left\lfloor\frac{\ell_{i}}{2}\right\rfloor\gg\ell_{i+1}-\ell_{i}. |  |

By construction, the terms on the left-hand side of ( 5.30) vanish unless j ≪ log 3 ⁡ t j\ll\log_{3}t, in which case they are equal to n i + 1 − n i 2 j + O ⁡ ( 1) \frac{n_{i+1}-n_{i}}{2^{j}}+O(1). Thus the left-hand side of ( 5.30) is at most O ⁡ ( n i + 1 − n i + log 3 ⁡ t) O(n_{i+1}-n_{i}+\log_{3}t). Thus

 | ℓ i + 1 − ℓ i ≪ n i + 1 − n i + log 3 ⁡ t. \ell_{i+1}-\ell_{i}\ll n_{i+1}-n_{i}+\log_{3}t. |  |

But from ( 5.29) one has n i + 1 − n i ≪ log 3 ⁡ t log 2 ⁡ t ​ ( ℓ i + 1 − ℓ i) n_{i+1}-n_{i}\ll\frac{\log_{3}t}{\log_{2}t}(\ell_{i+1}-\ell_{i}). Hence ℓ i + 1 − ℓ i ≪ log 3 ⁡ t \ell_{i+1}-\ell_{i}\ll\log_{3}t. But this contradicts ( 5.31). This concludes the proof of Theorem 1.8.

## References

- [1] H. L. Abbott, P. Erdős, and D. Hanson. On the number of times an integer occurs as a binomial coefficient. Amer. Math. Monthly, 81:256–261, 1974.
- [2] Milton Abramowitz and Irene A. Stegun. Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables. Dover, New York City, ninth Dover printing, tenth GPO printing edition, 1964.
- [3] È. T. Avanesov. Solution of a problem on figurate numbers. Acta Arith., 12:409–420, 1966/67.
- [4] F. Beukers, T. N. Shorey, and R. Tijdeman. Irreducibility of polynomials and arithmetic progressions with equal products of terms. In Number theory in progress, Vol. 1 (Zakopane-Kościelisko, 1997), pages 11–26. de Gruyter, Berlin, 1999.
- [5] Aart Blokhuis, Andries Brouwer, and Benne de Weger. Binomial collisions and near collisions. Integers, 17:Paper No. A64, 8, 2017.
- [6] J. W. Bober. Factorial ratios, hypergeometric series, and a family of step functions. J. Lond. Math. Soc. (2), 79(2):422–444, 2009.
- [7] J. William Bober. Integer ratios of factorials, hypergeometric functions, and related step functions. ProQuest LLC, Ann Arbor, MI, 2009. Thesis (Ph.D.)–University of Michigan.
- [8] Yann Bugeaud, Maurice Mignotte, Samir Siksek, Michael Stoll, and Szabolcs Tengely. Integral points on hyperelliptic curves. Algebra Number Theory, 2(8):859–885, 2008.
- [9] Harald Cramér. On the order of magnitude of the difference between consecutive prime numbers. Acta Arith., 2:23–46, 1936.
- [10] B. M. M. de Weger. A binomial Diophantine equation. Quart. J. Math. Oxford Ser. (2), 47(186):221–231, 1996.
- [11] Benjamin M. M. de Weger. Equal binomial coefficients: some elementary considerations. J. Number Theory, 63(2):373–386, 1997.
- [12] H. Iwaniec and E. Kowalski. Analytic number theory, volume 53 of American Mathematical Society Colloquium Publications. American Mathematical Society, Providence, RI, 2004.
- [13] H. Jenkins. Repeated binomial coefficients and high-degree curves. Integers, 16:Paper No. A69, 14, 2016.
- [14] Daniel Kane. New bounds on the number of representations of T T as a binomial coefficient. Integers, 4:A7, 10, 2004.
- [15] Daniel M. Kane. Improved bounds on the number of ways of expressing t t as a binomial coefficient. Integers, 7:A53, 7, 2007.
- [16] P. Kiss. On the number of solutions of the Diophantine equation ( x p) = ( y 2) \binom{x}{p}=\binom{y}{2}. Fibonacci Quart., 26(2):127–130, 1988.
- [17] Edmund Landau. Collected works. Vol. 1. Thales-Verlag, Essen, 1985. With a contribution in English by G. H. Hardy and H. Heilbronn, Edited and with a preface in English by L. Mirsky, I. J. Schoenberg, W. Schwarz and H. Wefelscheid.
- [18] D. A. Lind. The quadratic field Q ⁡ ( 5) Q(\surd 5) and a certain Diophantine equation. Fibonacci Quart., 6(3):86–93, 1968.
- [19] Kaisa Matomäki, Maksym Radziwiłł, and Terence Tao. Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges. Proc. Lond. Math. Soc. (3), 118(2):284–350, 2019.
- [20] L. J. Mordell. On the integer solutions of y ⁡ ( y + 1) = x ⁡ ( x + 1) ​ ( x + 2) y(y+1)=x(x+1)(x+2). Pacific J. Math., 13:1347–1351, 1963.
- [21] Ákos Pintér. A note on the Diophantine equation ( x 4) = ( y 2) \binom{x}{4}=\binom{y}{2}. Publ. Math. Debrecen, 47(3-4):411–415, 1995.
- [22] David Singmaster. Research Problems: How Often Does an Integer Occur as a Binomial Coefficient? Amer. Math. Monthly, 78(4):385–386, 1971.
- [23] David Singmaster. Repeated binomial coefficients and Fibonacci numbers. Fibonacci Quart., 13(4):295–298, 1975.
- [24] K. Soundararajan. Integral Factorial Ratios. arXiv e-prints, page arXiv:1901.05133, January 2019.
- [25] K. Soundararajan. Integral factorial ratios: irreducible examples with height larger than 1. Philos. Trans. Roy. Soc. A, 378(2163):20180444, 13, 2020.
- [26] Roelof J. Stroeker and Benjamin M. M. de Weger. Elliptic binomial Diophantine equations. Math. Comp., 68(227):1257–1281, 1999.
- [27] Craig A. Tovey. Multiple occurrences of binomial coefficients. Fibonacci Quart., 23(4):356–358, 1985.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:ksmato@utu.fi
[4]: mailto:maksym.radziwill@gmail.com
[5]: mailto:xuancheng.shao@uky.edu
[6]: mailto:tao@math.ucla.edu
[7]: mailto:joni.teravainen@maths.ox.ac.uk
