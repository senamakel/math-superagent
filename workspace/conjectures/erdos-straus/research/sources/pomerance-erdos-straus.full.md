<!-- source: https://ar5iv.labs.arxiv.org/html/1107.1010 | converted from HTML -->

[1107.1010] Counting the number of solutions to the Erdős-Straus equation on unit fractions

# Counting the number of solutions to the Erdős-Straus equation on unit fractions

Christian Elsholtz Address: Institut für Mathematik A, Steyrergasse 30/II, Technische Universität Graz, A-8010 Graz, Austria Email: [elsholtz@math.tugraz.at][1] and Terence Tao Address: Department of Mathematics, UCLA, Los Angeles CA 90095-1555 Email: [tao@math.ucla.edu][2]

###### Abstract.

For any positive integer n n, let f ⁡ ( n) f(n) denote the number of solutions to the Diophantine equation

 | 4 n = 1 x + 1 y + 1 z \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z} |  |

with x, y, z x,y,z positive integers. The *Erdős-Straus conjecture*asserts that f ⁡ ( n) > 0 f(n)>0 for every n ⩾ 2 n\geqslant 2. In this paper we obtain a number of upper and lower bounds for f ⁡ ( n) f(n) or f ⁡ ( p) f(p) for typical values of natural numbers n n and primes p p. For instance, we establish that

 | N ​ log 2 ​ N ≪ ∑ p ⩽ N f ⁡ ( p) ≪ N ​ log 2 ​ N ​ log ⁡ log ⁡ N. N\log^{2}N\ll\sum_{p\leqslant N}f(p)\ll N\log^{2}N\log\log N. |  |

These upper and lower bounds show that a typical prime has a small number of solutions to the Erdős-Straus Diophantine equation; small, when compared with other additive problems, like Waring’s problem.

###### 1991 Mathematics Subject Classification

11D68, 11N37 secondary: 11D72, 11N56

## 1. Introduction

For any natural number n ∈ ℕ = { 1, 2, … } n\in\mathbb{N}=\{1,2,\ldots\}, let f ⁡ ( n) f(n) denote the number of solutions ( x, y, z) ∈ ℕ 3 (x,y,z)\in\mathbb{N}^{3} to the Diophantine equation

 | 4 n = 1 x + 1 y + 1 z \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z} |  | (1.1) |

(we do not assume x, y, z x,y,z to be distinct or in increasing order). Thus for instance

 | f ( 1) = 0, f ( 2) = 3, f ( 3) = 12, f ( 4) = 10, f ( 5) = 12, f ( 6) = 39, f ( 7) = 36, f ( 8) = 46, … f(1)=0,f(2)=3,f(3)=12,f(4)=10,f(5)=12,f(6)=39,f(7)=36,f(8)=46,\ldots |  |

We plot the values of f ⁡ ( n) f(n) for n ⩽ 1000 n\leqslant 1000, and separately restricting to primes p ⩽ 1000 p\leqslant 1000 in Figures 1, 2.

Figure 1. The value f ⁡ ( n) f(n) for all n ⩽ 1000 n\leqslant 1000. Figure 2. The value f ⁡ ( p) f(p) for all primes p ⩽ 1000 p\leqslant 1000.

From these graphs one might be tempted to draw conclusions, such as “ f ⁡ ( n) ≫ n f(n)\gg n infinitely often”, that we will refute in our investigations below.

The *Erdős-Straus conjecture*(see e.g. [25]) asserts that f ⁡ ( n) > 0 f(n)>0 for all n ⩾ 2 n\geqslant 2; it remains unresolved, although there are a number of partial results. The earliest references to this conjecture are papers by Erdős [18] and Obláth [49], and we draw attention to the fact that the latter paper was submitted in 1948.

Most subsequent approaches list parametric solutions, which solve the conjecture for n n lying in certain residue classes. These soluble classes are either used for analytic approaches via a sieve method, or for computational verifications. For instance, it was shown by Vaughan [82] that the number of n < N n<N for which f ⁡ ( n) = 0 f(n)=0 is at most N ​ exp ⁡ ( − c ​ log 2 / 3 ​ N) N\exp(-c\log^{2/3}N) for some absolute constant c > 0 c>0 and all sufficiently large N N. (Compare also [48, 84, 39, 89] for some weaker results).

The conjecture was verified for all n ⩽ 10 14 n\leqslant 10^{14} in [79]. In Table 1 we list a more complete history of these computations, but there may be further unpublished computations as well.

5000 5000 | ⩽ \leqslant 1950 | Straus, see [18] |

8000 8000 | 1962 | Bernstein [6] |

20000 20000 | ⩽ \leqslant 1969 | Shapiro, see [44] |

106128 106128 | 1948/9 | Oblath [49] |

141648 141648 | 1954 | Rosati [58] |

10 7 10^{7} | 1964 | Yamomoto [88] |

1.1 × 10 7 1.1\times 10^{7} | 1976 | Jollensten [36] |

10 8 10^{8} | 1971 | Terzi [81] |

10 9 10^{9} | 1994 | Elsholtz & Roth (unpublished) |

10 10 10^{10} | 1995 | Elsholtz & Roth (unpublished) |

1.6 × 10 11 1.6\times 10^{11} | 1996 | Elsholtz & Roth (unpublished) |

10 10 10^{10} | 1999 | Kotsireas [37] |

10 14 10^{14} | 1999 | Swett [79] |

2 × 10 14 2\times 10^{14} | 2012 | Bello-Hernández, Benito, Fernández [5] |

10 17 10^{17} | 2014 | Salez [61] |

Table 1. Numerical verifications of the Erdős-Straus conjecture. It appears that Terzi’s set of soluble residue classes is correct, but that the set of checked primes in these classes is incomplete. Another reference to a calculation up to 10 8 10^{8} due to N. Franceschine III (1978) (see [25, 20] and frequently restated elsewhere) only mentions Terzi’s calculation, but is not an independent verification. We are grateful to I. Kotsireas for confirming this (private communication).

Most of these previous approaches concentrated on the question whether f ⁡ ( n) > 0 f(n)>0 or not. In this paper we will instead study the average growth or extremal values of f ⁡ ( n) f(n).

Since we clearly have f ⁡ ( n ​ m) ⩾ f ⁡ ( n) f(nm)\geqslant f(n) for any n, m ∈ ℕ n,m\in\mathbb{N}, we see that to prove the Erdős-Straus conjecture it suffices to do so when n n is equal to a prime p p.

In this paper we investigate the *average*behaviour of f ⁡ ( p) f(p) for p p a prime. More precisely, we consider the asymptotic behaviour of the sum

 | ∑ p ⩽ N f ⁡ ( p) \sum_{p\leqslant N}f(p) |  |

where N N is a large parameter, and p p ranges over all primes up to N N. As we are only interested in asymptotics, we may ignore the case p = 2 p=2, and focus on the odd primes p p.

Let us call a solution ( x, y, z) (x,y,z) to ( 1.1) a *Type I solution*if n n divides x x but is coprime to y, z y,z, and a *Type II solution*if n n divides y, z y,z but is coprime to x x. Let f I ​ ( n), f II ​ ( n) f_{\operatorname{I}}(n),f_{{\operatorname{II}}}(n) denote the number of Type I and Type II solutions respectively. By permuting the x, y, z x,y,z we clearly have

 | f ⁡ ( n) ⩾ 3 ​ f I ​ ( n) + 3 ​ f II ​ ( n) f(n)\geqslant 3f_{\operatorname{I}}(n)+3f_{\operatorname{II}}(n) |  | (1.2) |

for all n > 1 n>1. Conversely, when p p is an odd prime, it is clear from considering the denominators in the Diophantine equation

 | 4 p = 1 x + 1 y + 1 z \frac{4}{p}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z} |  | (1.3) |

that at least one of x, y, z x,y,z must be divisible by p p; also, it is not possible for all three of x, y, z x,y,z to be divisible by p p as this forces the right-hand side of ( 1.3) to be at most 3 / p 3/p. We thus have

 | f ⁡ ( p) = 3 ​ f I ​ ( p) + 3 ​ f II ​ ( p) f(p)=3f_{\operatorname{I}}(p)+3f_{\operatorname{II}}(p) |  | (1.4) |

for all odd primes p p. Thus, to understand the asymptotics of ∑ p ⩽ N f ⁡ ( p) \sum_{p\leqslant N}f(p), it suffices to understand the asymptotics of ∑ p ⩽ N f I ​ ( p) \sum_{p\leqslant N}f_{\operatorname{I}}(p) and ∑ p ⩽ N f II ​ ( p) \sum_{p\leqslant N}f_{\operatorname{II}}(p). As we shall see, Type II solutions are somewhat easier to understand than Type I solutions, but we will nevertheless be able to control both types of solutions in a reasonably satisfactory manner.

We can now state our first main theorem.

###### Theorem 1.1 (Average value of f I, f II f_{\operatorname{I}},f_{\operatorname{II}}).

For all sufficiently large N N, one has the bounds

 | N ​ log 3 ​ N ≪ ∑ n ⩽ N f I ​ ( n) \displaystyle N\log^{3}N\ll\sum_{n\leqslant N}f_{\operatorname{I}}(n) | ≪ N ​ log 3 ​ N \displaystyle\ll N\log^{3}N |  |

 | N ​ log 3 ​ N ≪ ∑ n ⩽ N f II ​ ( n) \displaystyle N\log^{3}N\ll\sum_{n\leqslant N}f_{\operatorname{II}}(n) | ≪ N ​ log 3 ​ N \displaystyle\ll N\log^{3}N |  |

 | N ​ log 2 ​ N ≪ ∑ p ⩽ N f I ​ ( p) \displaystyle N\log^{2}N\ll\sum_{p\leqslant N}f_{\operatorname{I}}(p) | ≪ N ​ log 2 ​ N ​ log ⁡ log ⁡ N \displaystyle\ll N\log^{2}N\log\log N |  |

 | N ​ log 2 ​ N ≪ ∑ p ⩽ N f II ​ ( p) \displaystyle N\log^{2}N\ll\sum_{p\leqslant N}f_{\operatorname{II}}(p) | ≪ N ​ log 2 ​ N. \displaystyle\ll N\log^{2}N. |  |

Here, we use the usual asymptotic notation X ≪ Y X\ll Y or X = O ⁡ ( Y) X=O(Y) to denote the estimate | X | ⩽ C ​ Y |X|\leqslant CY for an absolute constant C C, and use subscripts if we wish to allow dependencies on the implied constant C C, thus for instance X ≪ ε Y X\ll_{\varepsilon}Y or X = O ε ​ ( Y) X=O_{\varepsilon}(Y) denotes the estimate | X | ⩽ C ε ​ Y |X|\leqslant C_{\varepsilon}Y for some C ε C_{\varepsilon} that can depend on ε \varepsilon. We remark that in a previous version of this manuscript, the weaker bound ∑ p ⩽ N f II ​ ( p) ≪ N ​ log 2 ​ N ​ log ⁡ log ⁡ N \sum_{p\leqslant N}f_{\operatorname{II}}(p)\ll N\log^{2}N\log\log N was claimed. As pointed out subsequently by Jia [34], the argument in that previous version in fact only gave ∑ p ⩽ N f II ​ ( p) ≪ N ​ log 2 ​ N ​ log ⁡ log 2 ​ N \sum_{p\leqslant N}f_{\operatorname{II}}(p)\ll N\log^{2}N\log\log^{2}N, but can be repaired to give the originally claimed bound ∑ p ⩽ N f II ​ ( n) ≪ N ​ log 2 ​ N ​ log ⁡ log ⁡ N \sum_{p\leqslant N}f_{\operatorname{II}}(n)\ll N\log^{2}N\log\log N. These bounds are of course superceded by the results in Theorem 1.1.

As a corollary of this and ( 1.4), we see that

 | N ​ log 2 ​ N ≪ ∑ p ⩽ N f ⁡ ( p) ≪ N ​ log 2 ​ N ​ log ⁡ log ⁡ N. N\log^{2}N\ll\sum_{p\leqslant N}f(p)\ll N\log^{2}N\log\log N. |  |

From this, the prime number theorem, and Markov’s inequality, we see that for any ε > 0 \varepsilon>0, we can find a subset A A of primes of relative lower density at least 1 − ε 1-\varepsilon, thus

 | lim inf N → ∞ | { p ∈ A: p ⩽ N } | | { p: p ⩽ N } | ⩾ 1 − ε, \liminf_{N\to\infty}\frac{|\{p\in A:p\leqslant N\}|}{|\{p:p\leqslant N\}|}\geqslant 1-\varepsilon, |  | (1.5) |

such that f ⁡ ( p) = O ε ​ ( log 3 ⁡ p ​ log ⁡ log ⁡ p) f(p)=O_{\varepsilon}(\log^{3}p\log\log p) for all p ∈ A p\in A. Informally, a typical prime has only O ⁡ ( log 3 ⁡ p ​ log ⁡ log ⁡ p) O(\log^{3}p\log\log p) solutions to the Diophantine equation ( 1.3); or alternatively, for any function ξ ⁡ ( p) \xi(p) of p p that goes to infinity as p → ∞ p\to\infty, one has O ⁡ ( ξ ⁡ ( p) ​ log 3 ​ p ​ log ⁡ log ⁡ p) O(\xi(p)\log^{3}p\log\log p) for all p p in a subset of the primes of relative density 1 1. This may provide an explanation as to why analytic methods (such as the circle method) appear to be insufficient to resolve the Erdős-Straus conjecture, as such methods usually only give non-trivial lower bounds on the number of solutions to a Diophantine equation in the case when the number of such solutions grows polynomially with the height parameter N N. (There are however some exceptions to this rule, such as Gallagher’s results [23] on representing integers as the sum of a prime and a bounded number of powers of two, but such results tend to require a large number of summands in order to compensate for possible logarithmic losses in the analysis.)

The double logarithmic factor log ⁡ log ⁡ N \log\log N in the above arguments arises from technical limitations to our method (and specifically, in the inefficient nature of the Brun-Titchmarsh inequality ( A.10) when applied to very short progressions), and we conjecture that it should be eliminated.

###### Remark 1.2.

In view of these results, one can naively model f ⁡ ( p) f(p) as a Poisson process with intensity at least c ​ log 3 ​ p c\log^{3}p for some absolute constant c c. Using this probabilistic model as a heuristic, one expects any given prime to have a “probability” 1 − O ⁡ ( exp ⁡ ( − c ​ log 3 ​ p)) 1-O(\exp(-c\log^{3}p)) of having at least one solution, which by the Borel-Cantelli lemma suggests that the Erdős-Straus conjecture is true for all but finitely many p p. Of course, this is only a heuristic and does not constitute a rigorous argument. (However, one can view the results in [82], [15], based on the large sieve, as a rigorous analogue of this type of reasoning.)

###### Remark 1.3.

From Theorem 1.1 we have the lower bound ∑ n ⩽ N f ⁡ ( n) ≫ N ​ log 3 ​ N \sum_{n\leqslant N}f(n)\gg N\log^{3}N. In fact one has the stronger bound ∑ n ⩽ N f ⁡ ( n) ≫ N ​ log 6 ​ N \sum_{n\leqslant N}f(n)\gg N\log^{6}N (Heath-Brown, private communication) using the methods from [28]; see Remark 2.10 for further discussion. Thus, for composite n n, most solutions are in fact neither of Type I or Type II. It would be of interest to get matching upper bounds for ∑ n ⩽ N f ⁡ ( n) \sum_{n\leqslant N}f(n), but this seems to be beyond the scope of our methods. It would of course also be interesting to control higher moments such as ∑ p ⩽ N f I ​ ( p) k \sum_{p\leqslant N}f_{\operatorname{I}}(p)^{k} or ∑ p ⩽ N f II ​ ( p) k \sum_{p\leqslant N}f_{\operatorname{II}}(p)^{k}, but this also seems to unfortunately lie out of reach of our methods, as the level of the relevant divisor sums becomes too great to handle.

To prove Theorem 1.1, we first use some solvability criteria for Type I and Type II solutions to obtain more tractable expressions for f I ​ ( p) f_{\operatorname{I}}(p) and f II ​ ( p) f_{\operatorname{II}}(p). As we shall see, f I ​ ( p) f_{\operatorname{I}}(p) is essentially (up to a factor of two) the number of quadruples ( a, c, d, f) ∈ ℕ 4 (a,c,d,f)\in\mathbb{N}^{4} with 4 ​ a ​ c ​ d = p + f 4acd=p+f, f f dividing 4 ​ a 2 ​ d + 1 4a^{2}d+1, and a ​ c ​ d ⩽ 3 ​ p / 4 acd\leqslant 3p/4, while f II ​ ( p) f_{\operatorname{II}}(p) is essentially the number of quadruples ( a, c, d, e) ∈ ℕ 4 (a,c,d,e)\in\mathbb{N}^{4} with 4 ​ a ​ c ​ d ​ e = p + 4 ​ a 2 ​ d + e 4acde=p+4a^{2}d+e and a ​ c ​ d ​ e ⩽ 3 ​ p / 2 acde\leqslant 3p/2. (We will systematically review the various known representations of Type I and Type II solutions in Section 2.) This, combined with standard tools from analytic number theory such as the Brun-Titchmarsh inequality and the Bombieri-Vinogradov inequality, already gives most of Theorem 1.1. The most difficult bound is the upper bounds on f I f_{\operatorname{I}}, which eventually require an upper bound for expressions of the form

 | ∑ a ⩽ A ∑ b ⩽ B τ ⁡ ( k ​ a ​ b 2 + 1) \sum_{a\leqslant A}\sum_{b\leqslant B}\tau(kab^{2}+1) |  |

for various A, B, k A,B,k, where τ ⁡ ( n):= ∑ d | n 1 \tau(n):=\sum_{d\mid n}1 is the number of divisors of n n, and d | n d\mid n denotes the assertion that d d divides n n. By using an argument of Erdős [19], we obtain the following bound on this quantity:

###### Proposition 1.4 (Average value of τ ⁡ ( k ​ a ​ b 2 + 1) \tau(kab^{2}+1)).

For any A, B > 1 A,B>1, and any positive integer k ≪ ( A ​ B) O ⁡ ( 1) k\ll(AB)^{O(1)}, one has

 | ∑ a ⩽ A ∑ b ⩽ B τ ⁡ ( k ​ a ​ b 2 + 1) ≪ A ​ B ​ log ⁡ ( A + B) ​ log ⁡ ( 1 + k). \sum_{a\leqslant A}\sum_{b\leqslant B}\tau(kab^{2}+1)\ll AB\log(A+B)\log(1+k). |  |

###### Remark 1.5.

Using the heuristic that τ ⁡ ( n) ∼ log ⁡ n \tau(n)\sim\log n on the average (see ( A.5)), one expects the true bound here to be O ⁡ ( A ​ B ​ log ⁡ ( A + B)) O(AB\log(A+B)). The log ⁡ ( 1 + k) \log(1+k) loss can be reduced (for some ranges of A, B, k A,B,k, at least) by using more tools (such as the Polya-Vinogradov inequality), but this slightly inefficient bound will be sufficient for our applications.

We prove Proposition 1.4 (as well as some variants of this estimate) in Section 7. Our main tool is a more quantitative version of a classical bound of Erdős [19] on the sum ∑ n ⩽ N τ ⁡ ( P ⁡ ( n)) \sum_{n\leqslant N}\tau(P(n)) for various polynomials P P, which may be of independent interest; see Theorem 7.1.

We also collect a number of auxiliary results concerning the quantities f i ​ ( n) f_{i}(n), some of which were in previous literature. Firstly, we have a vanishing property at odd squares:

###### Proposition 1.6 (Vanishing).

For any odd perfect square n n, we have f I ​ ( n) = f II ​ ( n) = 0 f_{\operatorname{I}}(n)=f_{\operatorname{II}}(n)=0.

This observation essentially dates back to Schinzel (see [25], [44], [68]) and Yamomoto (see [88]) and is an easy application of quadratic reciprocity ( A.7): for the convenience of the reader, we give the proof in Section 4. A variant of this proposition was also established in [5]. Note that this does not disprove the Erdős-Straus conjecture, since the inequality ( 1.2) does not hold with equality on perfect squares; but it does indicate a key difficulty in attacking this conjecture, in that when showing that f I ​ ( p) f_{\operatorname{I}}(p) or f II ​ ( p) f_{\operatorname{II}}(p) is non-zero, one can only use methods that *must necessarily fail*when p p is replaced by an odd square such as p 2 p^{2}, which already rules out many strategies (e.g. a finite set of covering congruence strategies, or the circle method).

Next, we establish some upper bounds on f I ​ ( n), f II ​ ( n) f_{\operatorname{I}}(n),f_{\operatorname{II}}(n) for fixed n n:

###### Proposition 1.7 (Upper bounds).

For any n ∈ ℕ n\in\mathbb{N}, one has

 | f I ​ ( n) ≪ n 3 / 5 + O ⁡ ( 1 / log ⁡ log ⁡ n) f_{\operatorname{I}}(n)\ll n^{3/5+O(1/\log\log n)} |  |

and

 | f II ​ ( n) ≪ n 2 / 5 + O ⁡ ( 1 / log ⁡ log ⁡ n). f_{\operatorname{II}}(n)\ll n^{2/5+O(1/\log\log n)}. |  |

In particular, from this and ( 1.4) one can conclude that for any prime p p one has

 | f ⁡ ( p) ≪ p 3 / 5 + O ⁡ ( 1 / log ⁡ log ⁡ p). f(p)\ll p^{3/5+O(1/\log\log p)}. |  |

This should be compared with the recent result in [8], which gives the bound f ( n) ≪ ε n 2 / 3 + ε f(n)\ll_{\varepsilon}n^{2/3+\varepsilon} for all n n and all ε > 0 \varepsilon>0. For composite n n the treatment of parameters dividing n n appears to be more complicated and here we concentrate on those two cases that are motivated by the Erdős-Straus equation for prime denominator.

We prove this proposition in Section 3.

The main tools here are the multiple representations of Type I and Type II solutions available (see Section 2) and the divisor bound ( A.6). The values of f ⁡ ( p) f(p) appear to fluctuate in some respects as the values of the divisor function. The average values of f ⁡ ( p) f(p) behave much more regularly.

Moreover, in view of Theorem 1.1, one might also expect to have f ( n) ≪ ε n ε f(n)\ll_{\varepsilon}n^{\varepsilon} for any ε > 0 \varepsilon>0, but such logarithmic-type bounds on solutions to Diophantine equations seem difficult to obtain in general (Proposition 1.7 appears to be the limit of what one can obtain purely from the divisor bound ( A.6) alone).

In the reverse direction, we have the following lower bounds on f ⁡ ( n) f(n) for various sets of n n:

###### Theorem 1.8 (Lower bounds).

For infinitely many n n, one has

 | f ⁡ ( n) ⩾ exp ⁡ ( ( log ⁡ 3 + o ⁡ ( 1)) ​ log ⁡ n log ⁡ log ⁡ n), f(n)\geqslant\exp((\log 3+o(1))\frac{\log n}{\log\log n}), |  |

where o ⁡ ( 1) o(1) denotes a quantity that goes to zero as n → ∞ n\to\infty.

For any function ξ ⁡ ( n) \xi(n) going to + ∞ +\infty as n → ∞ n\to\infty, one has

 | f ⁡ ( n) ⩾ exp ⁡ ( log ⁡ 3 2 ​ log ⁡ log ⁡ n − O ⁡ ( ξ ⁡ ( n) ​ log ⁡ log ⁡ n)) ≫ ( log ⁡ n) 0.549 f(n)\geqslant\exp\left(\frac{\log 3}{2}\log\log n-O(\xi(n)\sqrt{\log\log n})\right)\gg(\log n)^{0.549} |  |

for all n n in a subset A A of natural numbers of density 1 1 (thus | A ∩ { 1, …, N } | / N → 1 |A\cap\{1,\ldots,N\}|/N\to 1 as N → ∞ N\to\infty).

Finally, one has

 | f ⁡ ( p) ⩾ exp ⁡ ( ( log ⁡ 3 2 − o ⁡ ( 1)) ​ log ⁡ log ⁡ p) ≫ ( log ⁡ p) 0.549 f(p)\geqslant\exp\left((\frac{\log 3}{2}-o(1))\log\log p\right)\gg(\log p)^{0.549} |  |

for all primes p p in a subset B B of primes of relative density 1 1 (thus | { p ∈ B: p ⩽ N } | / | { p: p ⩽ N } | → 1 |\{p\in B:p\leqslant N\}|/{|\{p:p\leqslant N\}|}\to 1 as N → ∞ N\to\infty).

As the proof shows the first two lower bounds are already valid for sums of two unit fractions. The result directly follow from the growth of certain divisor functions. An even better model for f ⁡ ( n) f(n) is a suitable superposition of several divisor functions. The proof will be in Section 6.

Finally, we consider (following [44], [68]) the question of finding polynomial solutions to ( 1.1). Let us call a primitive residue class n = r mod q n=r\mod q*solvable by polynomials*if there exist polynomials P 1 ​ ( n), P 2 ​ ( n), P 3 ​ ( n) P_{1}(n),P_{2}(n),P_{3}(n) which take positive integer values for all sufficiently large n n in this residue class (so in particular, the coefficients of P 1, P 2, P 3 P_{1},P_{2},P_{3} are rational), and such that

 | 4 n = 1 P 1 ​ ( n) + 1 P 2 ​ ( n) + 1 P 3 ​ ( n) \frac{4}{n}=\frac{1}{P_{1}(n)}+\frac{1}{P_{2}(n)}+\frac{1}{P_{3}(n)} |  |

for all n n. Here we recall that a residue class r mod q r\mod q is *primitive*if r r is coprime to q q. One could also consider non-primitive congruences, but these congruences only contain finitely many primes and are thus of less interest to solving the Erdős-Straus conjecture (and if the Erdős-Straus conjecture held for a common factor of r r and q q, then the residue class r mod q r\mod q would trivially be solvable by polynomials.

By Dirichlet’s theorem, the primitive residue class r mod q r\mod q contains arbitrarily large primes p p. For each large prime p p in this class, we either have one or two of the P 1 ​ ( p), P 2 ​ ( p), P 3 ​ ( p) P_{1}(p),P_{2}(p),P_{3}(p) divisible by p p, as observed previously. For p p large enough, note that P i ​ ( p) P_{i}(p) can only be divisible by p p if there is no constant term in P i P_{i}. We thus conclude that either one or two of the P i ​ ( n) P_{i}(n) have no constant term, but not all three. Let us call the congruence *Type I solvable*if one can take exactly one of P 1, P 2, P 3 P_{1},P_{2},P_{3} to have no constant term, and *Type II solvable*if exactly two have no constant term. Thus every solvable primitive residue class r mod q r\mod q is either Type I or Type II solvable.

It is well-known (see [49, 44]) that any primitive residue class n = r mod 840 n=r\mod 840 is solvable by polynomials unless r r is a perfect square. On the other hand, it is also known (see [44], [68]) that a primitive congruence class n = r mod q n=r\mod q which is a perfect square, cannot be solved by polynomials (this also follows from Proposition 1.6). The next proposition essentially classifies all solvable primitive congruences.

###### Proposition 1.9 (Solvable congruences).

Let q mod r q\mod r be a primitive residue class. If this class is Type I solvable by polynomials, then all sufficiently large primes in this residue class lie in one of a finite number of residue classes from one of following families:

- •

{ n = − f mod 4 a d } \{n=-f\mod 4ad\}, where a, d, f ∈ ℕ a,d,f\in\mathbb{N} are such that f | 4 ​ a 2 ​ d + 1 f|4a^{2}d+1. [48]

- •

{ n = − f mod 4 a c } ∩ { n = − c / a mod f } \{n=-f\mod 4ac\}\cap\{n=-c/a\mod f\}, where a, c, f ∈ ℕ a,c,f\in\mathbb{N} are such that ( 4 ​ a ​ c, f) = 1 (4ac,f)=1. [88]

- •

{ n = − f mod 4 c d } ∩ { n 2 = − 4 c 2 d mod f } \{n=-f\mod 4cd\}\cap\{n^{2}=-4c^{2}d\mod f\}, where c, d, f ∈ ℕ c,d,f\in\mathbb{N} are such that ( 4 ​ c ​ d, f) = 1 (4cd,f)=1.

- •

{ n = − 1 / e mod 4 a b } \{n=-1/e\mod 4ab\}, where a, b, e ∈ ℕ a,b,e\in\mathbb{N} are such that e | a + b e\mid a+b and ( e, 4 ​ a ​ b) = 1 (e,4ab)=1. [1], [58]

Conversely, any residue class in one of the above four families is solvable by polynomials.

Similarly, if q mod r q\mod r is Type II solvable by polynomials, then all sufficiently large primes in this residue class lie in one of a finite number of residue classes from one of the following families:

- •

− e mod 4 ​ a ​ b -e\mod 4ab, where a, b, e ∈ ℕ a,b,e\in\mathbb{N} are such that e | a + b e\mid a+b and ( e, 4 ​ a ​ b) = 1 (e,4ab)=1. [1]

- •

− 4 ​ a 2 ​ d mod f -4a^{2}d\mod f, where a, d, f ∈ ℕ a,d,f\in\mathbb{N} are such that 4 ​ a ​ d | f + 1 4ad\mid f+1. [82], [58]

- •

− 4 ​ a 2 ​ d − e mod 4 ​ a ​ d ​ e -4a^{2}d-e\mod 4ade, where a, d, e ∈ ℕ a,d,e\in\mathbb{N} are such that ( 4 ​ a ​ d, e) = 1 (4ad,e)=1. [48]

Conversely, any residue class in one of the above three families is solvable by polynomials.

As indicated by the citations, mpst of these residue classes were observed to be solvable by polynomials in previous literature, but one of the conditions listed here appears to be new, and they form the essentially complete list of all such classes. We prove Proposition 1.9 in Section 10.

###### Remark 1.10.

The results in this paper would also extend (with minor changes) to the more general situation in which the numerator 4 4 in ( 1.3) is replaced by some other fixed positive integer, a situation considered first by Sierpiński and Schinzel (see e.g. [74, 82, 51, 52, 77]).

We will not detail all of these extensions here but in Section 11 we extend our study of the average number of solutions to the more general question on sums of k k unit fractions

 | m n = 1 t 1 + 1 t 2 + ⋯ + 1 t k. \frac{m}{n}=\frac{1}{t_{1}}+\frac{1}{t_{2}}+\cdots+\frac{1}{t_{k}}. |  | (1.6) |

If m ⩽ k m\leqslant k the greedy algorithm (in this case also known as Fibonacci-Sylvester algorithm) shows there is a solution. Indeed, let n = m ​ y + r n=my+r with 0 < r < m 0<r<m, then m n − 1 y + 1 = m − r n ⁡ ( y + 1) \frac{m}{n}-\frac{1}{y+1}=\frac{m-r}{n(y+1)} has a smaller numerator, and inductively a solution with k ⩽ m k\leqslant m is constructed. For an alternative method (especially if m = k = 4 m=k=4) see also Schinzel [67].

If m > k ⩾ 3 m>k\geqslant 3, and the t i t_{i} are positive integers, then it is an open problem if for each sufficiently large n n there is at least one solution. The Erdős-Straus conjecture with m = 4, k = 3 m=4,k=3, discussed above, is the most prominent case. If m m and k k are fixed, one can again establish sets of residue classes, such that ( 1.6) is generally soluble if n n is in any of these residue classes.

The problem of classifying solutions of ( 1.6) has been studied by Rav [57], Sós [76] and Elsholtz [15]. Moreover Viola [83], Shen [72] and Elsholtz [16] have used a suitable subset of these solutions to give (for fixed m > k ⩾ 3 m>k\geqslant 3) quantitive bounds on the number of those integers n ⩽ N n\leqslant N, for which ( 1.6) does not have any solution.

In order to study, whether there is at least one solution, it is again sufficient to concentrate on prime denominators. The average number of solutions is smaller when averaging over the primes only, but we intend to prove that even in the prime case the average number of solutions grows quickly, when k k increases.

We will focus on the case of *Type II solutions*, in which t 2, …, t k t_{2},\ldots,t_{k} are divisible by n n. The classification of solutions that we give below also works for other divisibility patterns, but Type II solutions are the easiest to count, and so we shall restrict our attention to this case. Strictly speaking, the definition of a Type II solution here is slightly different from that discussed previously, because we do not require that t 1 t_{1} is coprime to n n. However, this coprimality is automatic when n n is prime (otherwise the right-hand side of ( 1.6) would only be at most k / n k/n). For composite n n, it is possible to insert this condition and still obtain the lower bound ( 1.7), but this would complicate the argument slightly and we have chosen not to do so here.

For given m, k, n m,k,n, let f m, k, II ​ ( n) f_{m,k,{\operatorname{II}}}(n) denote the number of Type II solutions. Our main result regarding this quantity is the following lower bound on this quantity:

###### Theorem 1.11.

Let m > k ⩾ 3 m>k\geqslant 3 be fixed. Then, for N N sufficiently large, one has

 | ∑ n ⩽ N f m, k, II ( n) ≫ m, k N ( log N) 2 k − 1 − 1 \sum_{n\leqslant N}f_{m,k,{\operatorname{II}}}(n)\gg_{m,k}N(\log N)^{2^{k-1}-1} |  | (1.7) |

and

 | ∑ p ⩽ N f m, k, II ( p) ≫ m, k N ​ ( log ⁡ N) 2 k − 1 − 2 log ⁡ log ⁡ N. \sum_{p\leqslant N}f_{m,k,{\operatorname{II}}}(p)\gg_{m,k}\frac{N(\log N)^{2^{k-1}-2}}{\log\log N}. |  | (1.8) |

Our emphasis here is on the exponential growth of the exponent. In particular, as k k increases by one, the average number of solutions is roughly squared. The denominator of log ⁡ log ⁡ N \log\log N is present for technical reasons (due to use of the crude lower bound ( A.11) on the Euler totient function), and it is likely that it could be eliminated (much as it is in the m = 4, k = 3 m=4,k=3 case) with additional effort.

###### Remark 1.12.

If we let f m, k ​ ( n) f_{m,k}(n) be the total number of solutions to ( 1.6) (not just Type II solutions), then we of course obtain as a corollary that

 | ∑ n ⩽ N f m, k ( n) ≫ k N ( log N) 2 k − 1 − 1. \sum_{n\leqslant N}f_{m,k}(n)\gg_{k}N(\log N)^{2^{k-1}-1}. |  |

We do not expect the power of the logarithm to be sharp in this case (cf. Remark 2.10). For instance, in [31] it is shown that

 | ∑ n ⩽ N f m, 2 ​ ( n) = ( 1 ϕ ⁡ ( m) + o ⁡ ( 1)) ​ N ​ log 2 ​ N \sum_{n\leqslant N}f_{m,2}(n)=\left(\frac{1}{\phi(m)}+o(1)\right)N\log^{2}N |  |

for any fixed m m.

Note that the equation ( 1.6) can be rewritten as

 | 1 m ​ t 1 + ⋯ + 1 m ​ t k + 1 − n = 0, \frac{1}{mt_{1}}+\cdots+\frac{1}{mt_{k}}+\frac{1}{-n}=0, |  |

which is primitive when n n is prime. As a consequence, we obtain a lower bound for the number of integer points on the (generalised) Cayley surface:

###### Corollary 1.13.

Let k ⩾ 3 k\geqslant 3. The number of integer points of the following generalization of Cayley’s cubic surface,

 | 0 = ∑ i = 0 k 1 t i, 0=\sum_{i=0}^{k}\frac{1}{t_{i}}, |  |

with t i t_{i} non-zero integers with min i ⁡ | t i | ⩽ N \min_{i}|t_{i}|\leqslant N, is at least c k ​ N ​ ( log ⁡ N) 2 k − 1 − 2 / log ⁡ log ⁡ N c_{k}N(\log N)^{2^{k-1}-2}/\log\log N for some c k > 0 c_{k}>0 depending only on k k.

Again, the double logarithmic factor should be removable with some additional effort, although the exponent 2 k − 1 − 2 2^{k-1}-2 is not expected to be sharp, and should be improvable also.

Finally, let us mention that there are many other problems on the number of solutions of

 | m n = 1 t 1 + 1 t 2 + ⋯ + 1 t k \frac{m}{n}=\frac{1}{t_{1}}+\frac{1}{t_{2}}+\cdots+\frac{1}{t_{k}} |  |

which we do not study here. Let us point to some further references: [65], [8], [10], [17] study the number of solutions of 1 1 as a sum of unit fractions. [12] and [31] study the case k = 2 k=2, also with varying numerator m m.

Part of the first author’s work on ths project was supported by the German National Merit Foundation. The second author is supported by a grant from the MacArthur Foundation, by NSF grant DMS-0649473, and by the NSF Waterman award. The authors thank Nicolas Templier for many helpful comments and references, and the referee and editor for many useful corrections and suggestions, as well as Serge Salez for pointing out an error in a previous version of the manuscript. The first author is very grateful to Roger Heath-Brown for very generous advice on the subject (dating back as far as 1994). Both authors are particularly indebted to him for several remarks (including Remark 2.10), and also for contributing some of the key arguments here (such as the lower bound on ∑ n ⩽ N f II ​ ( n) \sum_{n\leqslant N}f_{\operatorname{II}}(n) and ∑ p ⩽ N f II ​ ( p) \sum_{p\leqslant N}f_{\operatorname{II}}(p)) which have been reproduced here with permission. The first author also wishes to thank Tim Browning, Ernie Croot and Arnd Roth for discussions on the subject.

## 2. Representation of Type I and Type II solutions

We now discuss the representation of Type I and Type II solutions. There are many such representations in the literature (see e.g. [1], [5], [6], [48], [57], [58], [82], [85]); we will remark how each of these representations can be viewed as a form of the one given here after describing a certain algebraic variety in coordinates.

For any non-zero complex number n n, consider the algebraic surface

 | S n:= { ( x, y, z) ∈ ℂ 3: 4 ​ x ​ y ​ z = n ​ y ​ z + n ​ x ​ z + n ​ x ​ y } ⊂ ℂ 3. S_{n}:=\{(x,y,z)\in\mathbb{C}^{3}:4xyz=nyz+nxz+nxy\}\subset\mathbb{C}^{3}. |  |

Of course, when n n is a natural number, f ⁡ ( n) f(n) is nothing more than the number of ℕ \mathbb{N} -points ( x, y, z) ∈ S n ∩ ℕ 3 (x,y,z)\in S_{n}\cap\mathbb{N}^{3} on this surface.

It is somewhat inconvenient to count ℕ \mathbb{N} -points on S n S_{n} directly, due to the fact that x, y, z x,y,z are likely to share many common factors. To eliminate these common factors, it is convenient to lift S n S_{n} to higher-dimensional varieties Σ n I \Sigma^{\operatorname{I}}_{n}, Σ n II \Sigma^{{\operatorname{II}}}_{n} (and more specifically, to three-dimensional varieties in ℂ 6 \mathbb{C}^{6}), which are adapted to parameterising Type I and Type II solutions respectively. This will replace the three original coordinates x, y, z x,y,z by six coordinates a, b, c, d, e, f a,b,c,d,e,f, any three of which can be used to parameterise Σ n I \Sigma^{I}_{n}. or Σ n II \Sigma^{{\operatorname{II}}}_{n}. This multiplicity of parameterisations will be useful for many of the applications in this paper; rather than pick one parameterisation in advance, it is convenient to be able to pick and choose between them, depending on the situation.

We begin with the description of Type I solutions. More precisely, we define Σ n I \Sigma^{\operatorname{I}}_{n} to be the set of all sextuples ( a, b, c, d, e, f) ∈ ℂ 6 (a,b,c,d,e,f)\in\mathbb{C}^{6} which are non-zero and obey the constraints

 | 4 ​ a ​ b ​ d \displaystyle 4abd | = n ​ e + 1 \displaystyle=ne+1 |  | (2.1) |

 | c ​ e \displaystyle ce | = a + b \displaystyle=a+b |  | (2.2) |

 | 4 ​ a ​ b ​ c ​ d \displaystyle 4abcd | = n ​ a + n ​ b + c \displaystyle=na+nb+c |  | (2.3) |

 | 4 ​ a ​ c ​ d ​ e \displaystyle 4acde | = n ​ e + 4 ​ a 2 ​ d + 1 \displaystyle=ne+4a^{2}d+1 |  | (2.4) |

 | 4 ​ b ​ c ​ d ​ e \displaystyle 4bcde | = n ​ e + 4 ​ b 2 ​ d + 1 \displaystyle=ne+4b^{2}d+1 |  | (2.5) |

 | 4 ​ a ​ c ​ d \displaystyle 4acd | = n + f \displaystyle=n+f |  | (2.6) |

 | e ​ f \displaystyle ef | = 4 ​ a 2 ​ d + 1 \displaystyle=4a^{2}d+1 |  | (2.7) |

 | b ​ f \displaystyle bf | = n ​ a + c \displaystyle=na+c |  | (2.8) |

 | n 2 + 4 ​ c 2 ​ d \displaystyle n^{2}+4c^{2}d | = f ⁡ ( 4 ​ b ​ c ​ d − n). \displaystyle=f(4bcd-n). |  | (2.9) |

###### Remark 2.1.

There are multiple redundancies in these constraints; to take just one example, ( 2.9) follows from ( 2.3) and ( 2.6). One could in fact specify Σ n I \Sigma^{\operatorname{I}}_{n} using just three of these nine constraints if desired. However, this redundancy will be useful in the sequel, as we will be taking full advantage of all nine of these identities.

The identities ( 2.1)-( 2.9) form an algebraic set that can be parameterised (perhaps up to some bounded multiplicity) by fixing three of the six coordinates a, b, c, d, e, f a,b,c,d,e,f and solving for the other three coordinates. For instance, using the coordinates a, c, d a,c,d, one easily verifies that

 | Σ n I = { ( a, n ​ a + c 4 ​ a ​ c ​ d − n, c, d, 4 ​ a 2 ​ d + 1 4 ​ a ​ c ​ d − n, 4 a c d − n): a, c, d ∈ ℂ 3; 4 a c d ≠ n } \Sigma^{\operatorname{I}}_{n}=\left\{(a,\frac{na+c}{4acd-n},c,d,\frac{4a^{2}d+1}{4acd-n},4acd-n):a,c,d\in\mathbb{C}^{3};4acd\neq n\right\} |  |

and similarly for the other ( 6 3) − 1 = 14 \binom{6}{3}-1=14 choices of three coordinates; we omit the elementary but tedious computations. Thus we see that Σ n I \Sigma^{\operatorname{I}}_{n} is a three-dimensional algebraic variety. From ( 2.3) we see that the map

 | π n I: ( a, b, c, d, e, f) ↦ ( a ​ b ​ d ​ n, a ​ c ​ d, b ​ c ​ d) \pi^{\operatorname{I}}_{n}:(a,b,c,d,e,f)\mapsto(abdn,acd,bcd) |  |

maps Σ n I \Sigma^{\operatorname{I}}_{n} to S n S_{n}. After quotienting out by the dilation symmetry

 | ( a, b, c, d, e, f) ↦ ( λ ​ a, λ ​ b, λ ​ c, λ − 2 ​ d, e, f) (a,b,c,d,e,f)\mapsto(\lambda a,\lambda b,\lambda c,\lambda^{-2}d,e,f) |  | (2.10) |

of Σ n I \Sigma^{I}_{n}, this map is injective.

If n n is a natural number, then π n I \pi^{I}_{n} clearly maps ℕ \mathbb{N} -points of Σ n I \Sigma^{I}_{n} to ℕ \mathbb{N} -points of S n S_{n}, and if c c is coprime to n n, gives a Type I solution (note that a ​ b ​ d abd is automatically coprime to n n, thanks to ( 2.1)). In the converse direction, all Type I solutions arise in this manner:

###### Proposition 2.2 (Description of Type I solutions).

Let n ∈ ℕ n\in\mathbb{N}, and let ( x, y, z) (x,y,z) be a Type I solution. Then there exists a unique ( a, b, c, d, e, f) ∈ ℕ 6 ∩ Σ n I (a,b,c,d,e,f)\in\mathbb{N}^{6}\cap\Sigma^{\operatorname{I}}_{n} with a ​ b ​ c ​ d abcd coprime to n n and a, b, c a,b,c having no common factor, such that π n I ​ ( a, b, c, d, e, f) = ( x, y, z) \pi^{\operatorname{I}}_{n}(a,b,c,d,e,f)=(x,y,z).

###### Proof.

The uniqueness follows since π n I \pi^{\operatorname{I}}_{n} is injective after quotienting out by dilations. To show existence, we factor x = n ​ d ​ x ′, y = d ​ y ′, z = d ​ z ′ x=ndx^{\prime},y=dy^{\prime},z=dz^{\prime}, where x ′, y ′, z ′ x^{\prime},y^{\prime},z^{\prime} are coprime, then after multiplying ( 1.1) by n ​ d ​ x ′ ​ y ′ ​ z ′ ndx^{\prime}y^{\prime}z^{\prime} we have

 | 4 ​ d ​ x ′ ​ y ′ ​ z ′ = y ′ ​ z ′ + n ​ x ′ ​ y ′ + n ​ x ′ ​ z ′. 4dx^{\prime}y^{\prime}z^{\prime}=y^{\prime}z^{\prime}+nx^{\prime}y^{\prime}+nx^{\prime}z^{\prime}. |  | (2.11) |

As y ′, z ′ y^{\prime},z^{\prime} are coprime to n n, we conclude that x ′ x^{\prime} divides y ′ ​ z ′ y^{\prime}z^{\prime}, y ′ y^{\prime} divides x ′ ​ z ′ x^{\prime}z^{\prime}, and z ′ z^{\prime} divides x ′ ​ y ′ x^{\prime}y^{\prime}. Splitting into prime factors, we conclude that

 | x ′ = a ​ b, y ′ = a ​ c, z ′ = b ​ c x^{\prime}=ab,y^{\prime}=ac,z^{\prime}=bc |  | (2.12) |

for some natural numbers a, b, c a,b,c; since x ′, y ′, z ′ x^{\prime},y^{\prime},z^{\prime} have no common factor, a, b, c a,b,c have no common factor also. As y, z y,z were coprime to n n, a ​ b ​ c ​ d abcd is coprime to n n also.

Substituting ( 2.12) into ( 2.11) we obtain ( 2.3), which in particular implies (as c c is coprime to n n) that c c divides a + b a+b. If we then set e:= ( a + b) / c e:=(a+b)/c and f:= 4 ​ a ​ c ​ d − n = ( n ​ a + c) / b f:=4acd-n=(na+c)/b, then e, f e,f are natural numbers, and we obtain the other identities ( 2.1)-( 2.9) by routine algebra. By construction we have π n I ​ ( a, b, c, d, e, f) = ( x, y, z) \pi^{\operatorname{I}}_{n}(a,b,c,d,e,f)=(x,y,z), and the claim follows. ∎

In particular, for fixed n n, a Type I solution exists if and only if there is an ℕ \mathbb{N} -point ( a, b, c, d, e, f) (a,b,c,d,e,f) of Σ n I \Sigma^{\operatorname{I}}_{n} with a ​ b ​ c ​ d abcd coprime to n n (the requirement that a, b, c a,b,c have no common factor can be removed using the symmetry ( 2.10)). By parameterising Σ n I \Sigma^{\operatorname{I}}_{n} using three or four of the six coordinates, we recover some of the known characterisations of Type I solvability:

###### Proposition 2.3.

Let n n be a natural number. Then the following are equivalent:

- •

There exists a Type I solution ( x, y, z) (x,y,z).

- •

There exists a, b, e ∈ ℕ a,b,e\in\mathbb{N} with e | a + b e\mid a+b and 4 ​ a ​ b | n ​ e + 1 4ab\mid ne+1. [1]

- •

There exists a, b, c, d ∈ ℕ a,b,c,d\in\mathbb{N} such that 4 ​ a ​ b ​ c ​ d = n ​ a + n ​ b + c 4abcd=na+nb+c with c c coprime to n n. [6]

- •

There exist a, c, d, e ∈ ℕ a,c,d,e\in\mathbb{N} such that n ​ e + 1 = 4 ​ a ​ d ​ ( c ​ e − a) ne+1=4ad(ce-a) with c c coprime to n n. [58, 44]

- •

There exist a, c, d, f ∈ ℕ a,c,d,f\in\mathbb{N} such that n = 4 ​ a ​ c ​ d − f n=4acd-f and f | 4 ​ a 2 ​ d + 1 f\mid 4a^{2}d+1, with c c coprime to n n. [48]

- •

There exist b, c, d, e b,c,d,e with n ​ e = ( 4 ​ b ​ c ​ d ​ e − 1) − 4 ​ b 2 ​ d ne=(4bcde-1)-4b^{2}d and c c coprime to n n. [5]

The proof of this proposition is routine and is omitted.

###### Remark 2.4.

Type I solutions ( x, y, z) (x,y,z) have the obvious reflection symmetry ( x, y, z) ↦ ( x, z, y) (x,y,z)\mapsto(x,z,y). With ( 2.6) and ( 2.9) the corresponding symmetry for Σ n I \Sigma^{\operatorname{I}}_{n} is given by

 | ( a, b, c, d, e, f) ↦ ( b, a, c, d, e, n 2 + 4 ​ c 2 ​ d f). (a,b,c,d,e,f)\mapsto\left(b,a,c,d,e,\frac{n^{2}+4c^{2}d}{f}\right). |  |

We will typically only use the Σ n I \Sigma^{\operatorname{I}}_{n} parameterisation when y ⩽ z y\leqslant z (or equivalently when a ⩽ b a\leqslant b), in order to keep the sizes of various parameters small.

###### Remark 2.5.

If we consider ℕ \mathbb{N} -points ( a, b, c, d, e, f) (a,b,c,d,e,f) of Σ n I \Sigma^{\operatorname{I}}_{n} with a = 1 a=1, they can be explicitly parameterised as

 | ( 1, c ​ e − 1, c, e ​ f − 1 4, e, f) \left(1,ce-1,c,\frac{ef-1}{4},e,f\right) |  |

where e, f e,f are natural numbers with e ​ f = 1 mod 4 ef=1\mod 4 and n = c ​ e ​ f − c − f n=cef-c-f. This shows that any n n of the form c ​ e ​ f − c − f cef-c-f with e ​ f = 1 mod 4 ef=1\mod 4 solves the Erdős-Straus conjecture, an observation made in [5]. However, this is a relatively small set of solutions (corresponding to roughly log 2 ⁡ n \log^{2}n solutions for a given n n on average, rather than log 3 ⁡ n \log^{3}n), due to the restriction a = 1 a=1. Nevertheless, in [5] it was verified that all primes p = 1 mod 4 p=1\mod 4 with p ⩽ 10 14 p\leqslant 10^{14} were representable in this form.

Now we turn to Type II solutions. Here, we replace Σ n I \Sigma^{\operatorname{I}}_{n} by the variety Σ n II \Sigma^{\operatorname{II}}_{n}, as defined the set of all sextuples ( a, b, c, d, e, f) ∈ ℂ 6 (a,b,c,d,e,f)\in\mathbb{C}^{6} which are non-zero and obey the constraints

 | 4 ​ a ​ b ​ d \displaystyle 4abd | = n + e \displaystyle=n+e |  | (2.13) |

 | c ​ e \displaystyle ce | = a + b \displaystyle=a+b |  | (2.14) |

 | 4 ​ a ​ b ​ c ​ d \displaystyle 4abcd | = a + b + n ​ c \displaystyle=a+b+nc |  | (2.15) |

 | 4 ​ a ​ c ​ d ​ e \displaystyle 4acde | = n + 4 ​ a 2 ​ d + e \displaystyle=n+4a^{2}d+e |  | (2.16) |

 | 4 ​ b ​ c ​ d ​ e \displaystyle 4bcde | = n + 4 ​ b 2 ​ d + e \displaystyle=n+4b^{2}d+e |  | (2.17) |

 | 4 ​ a ​ c ​ d \displaystyle 4acd | = f + 1 \displaystyle=f+1 |  | (2.18) |

 | e ​ f \displaystyle ef | = n + 4 ​ a 2 ​ d \displaystyle=n+4a^{2}d |  | (2.19) |

 | b ​ f \displaystyle bf | = n ​ c + a \displaystyle=nc+a |  | (2.20) |

 | 4 ​ c 2 ​ d ​ n + 1 \displaystyle 4c^{2}dn+1 | = f ⁡ ( 4 ​ b ​ c ​ d − 1). \displaystyle=f(4bcd-1). |  | (2.21) |

This is a very similar variety to Σ n I \Sigma^{\operatorname{I}}_{n}; indeed the non-isotropic dilation

 | ( a, b, c, d, e, f) ↦ ( a, b, c / n 2, d ​ n, n 2 ​ e, f / n) (a,b,c,d,e,f)\mapsto(a,b,c/n^{2},dn,n^{2}e,f/n) |  |

is a bijection from Σ n I \Sigma^{\operatorname{I}}_{n} to Σ n II \Sigma^{\operatorname{II}}_{n}. Thus, as with Σ n I \Sigma^{\operatorname{I}}_{n}, Σ n II \Sigma^{\operatorname{II}}_{n} is a three-dimensional algebraic variety in ℂ 6 \mathbb{C}^{6} which can be parameterised by any three of the six coordinates in ( a, b, c, d, e, f) (a,b,c,d,e,f). As before, many of the constraints can be viewed as redundant; for instance, ( 2.21) is a consequence of ( 2.15) and ( 2.18). Note that Σ n II \Sigma^{\operatorname{II}}_{n} enjoys the same dilation symmetry ( 2.10) as Σ n I \Sigma^{\operatorname{I}}_{n}, and also has the reflection symmetry (using ( 2.18) and ( 2.21))

 | ( a, b, c, d, e, f) ↦ ( b, a, c, d, e, 4 ​ c 2 ​ d ​ n + 1 f). (a,b,c,d,e,f)\mapsto\left(b,a,c,d,e,\frac{4c^{2}dn+1}{f}\right). |  |

Analogously to π n I \pi^{\operatorname{I}}_{n}, we have the map π n II: Σ n II → S n \pi^{\operatorname{II}}_{n}:\Sigma^{\operatorname{II}}_{n}\to S_{n} given by

 | π n II: ( a, b, c, d, e, f) ↦ ( a ​ b ​ d, a ​ c ​ d ​ n, b ​ c ​ d ​ n) \pi^{\operatorname{II}}_{n}:(a,b,c,d,e,f)\mapsto(abd,acdn,bcdn) |  | (2.22) |

which is injective up to the dilation symmetry ( 2.10) and which, when n n is a natural number, maps ℕ \mathbb{N} -points of Σ n II \Sigma^{\operatorname{II}}_{n} to ℕ \mathbb{N} -points of S n S_{n}, and when a ​ b ​ d abd is coprime to n n, gives Type II solutions. (Note that this latter condition is automatic when n n is prime, since x, y, z x,y,z cannot all be divisible by n n.)

We have an analogue of Proposition 2.2:

###### Proposition 2.6 (Description of Type II solutions).

Let n ∈ ℕ n\in\mathbb{N}, and let ( x, y, z) (x,y,z) be a Type II solution. Then there exists a unique ( a, b, c, d, e, f) ∈ ℕ 6 ∩ Σ n II (a,b,c,d,e,f)\in\mathbb{N}^{6}\cap\Sigma^{\operatorname{II}}_{n} with a ​ b ​ d abd coprime to n n and a, b, c a,b,c having no common factor, such that π n I ​ ( a, b, c, d, e, f) = ( x, y, z) \pi^{\operatorname{I}}_{n}(a,b,c,d,e,f)=(x,y,z).

###### Proof.

Uniqueness follows from injectivity modulo dilations of π n II \pi^{\operatorname{II}}_{n} as before. To show existence, we factor x = d ​ x ′, y = n ​ d ​ y ′, z = n ​ d ​ z ′ x=dx^{\prime},y=ndy^{\prime},z=ndz^{\prime}, where x ′, y ′, z ′ x^{\prime},y^{\prime},z^{\prime} are coprime, then after multiplying ( 1.1) by n ​ d ​ x ′ ​ y ′ ​ z ′ ndx^{\prime}y^{\prime}z^{\prime} we have

 | 4 ​ d ​ x ′ ​ y ′ ​ z ′ = n ​ y ′ ​ z ′ + x ′ ​ y ′ + x ′ ​ z ′. 4dx^{\prime}y^{\prime}z^{\prime}=ny^{\prime}z^{\prime}+x^{\prime}y^{\prime}+x^{\prime}z^{\prime}. |  | (2.23) |

As x ′ x^{\prime} are coprime to n n, we conclude that x ′ x^{\prime} divides y ′ ​ z ′ y^{\prime}z^{\prime}, y ′ y^{\prime} divides x ′ ​ z ′ x^{\prime}z^{\prime}, and z ′ z^{\prime} divides x ′ ​ y ′ x^{\prime}y^{\prime}. Splitting into prime factors, we again obtain the representation ( 2.12) for some natural numbers a, b, c a,b,c; since x ′, y ′, z ′ x^{\prime},y^{\prime},z^{\prime} have no common factor, a, b, c a,b,c have no common factor also. As x x was coprime to n n, a ​ b ​ d abd is coprime to n n also.

Substituting ( 2.12) into ( 2.23) we obtain ( 2.15), which in particular implies that c c divides a + b a+b. If we then set e:= ( a + b) / c e:=(a+b)/c and f:= 4 ​ a ​ c ​ d − 1 f:=4acd-1, then e, f e,f are natural numbers, and we obtain the other identities ( 2.13)-( 2.21) by routine algebra. By construction we have π n II ​ ( a, b, c, d, e, f) = ( x, y, z) \pi^{\operatorname{II}}_{n}(a,b,c,d,e,f)=(x,y,z), and the claim follows. ∎

Again, we can recover some known characterisations of Type II solvability:

###### Proposition 2.7.

Let n n be a natural number. Then the following are equivalent:

- •

There exists a Type II solution ( x, y, z) (x,y,z).

- •

There exists a, b, e ∈ ℕ a,b,e\in\mathbb{N} with e | a + b e\mid a+b and 4 ​ a ​ b | n + e 4ab\mid n+e, and ( n + e) / 4 (n+e)/4 coprime to n n. [1]

- •

There exists a, b, c, d ∈ ℕ a,b,c,d\in\mathbb{N} such that 4 ​ a ​ b ​ c ​ d = a + b + n ​ c 4abcd=a+b+nc with a ​ b ​ d abd coprime to n n. [6, 44]

- •

There exists a, b, d ∈ ℕ a,b,d\in\mathbb{N} with 4 ​ a ​ b ​ d − 1 | b + n ​ c 4abd-1\mid b+nc with a ​ b ​ d abd coprime to n n. [82]

- •

There exist a, c, d, e ∈ ℕ a,c,d,e\in\mathbb{N} such that n = ( 4 ​ a ​ c ​ d − 1) ​ e − 4 ​ a 2 ​ d n=(4acd-1)e-4a^{2}d with ( n + e) / 4 (n+e)/4 coprime to n n. [58]

- •

There exist a, c, d, f ∈ ℕ a,c,d,f\in\mathbb{N} such that n = 4 ​ a ​ d ​ ( c ​ e − a) − e = e ⁡ ( 4 ​ a ​ c ​ d − 1) − 4 ​ a 2 ​ d n=4ad(ce-a)-e=e(4acd-1)-4a^{2}d with a ​ d ​ ( c ​ e − a) ad(ce-a) coprime to n n. [48]

Next, we record some bounds on the order of magnitude of the parameters a, b, c, d, e, f a,b,c,d,e,f assuming that y ⩽ z y\leqslant z.

###### Lemma 2.8.

Let n ∈ ℕ n\in\mathbb{N}, and suppose that ( x, y, z) = π n I ​ ( a, b, c, d, e, f) (x,y,z)=\pi^{\operatorname{I}}_{n}(a,b,c,d,e,f) is a Type I solution such that y ⩽ z y\leqslant z. Then

 | a \displaystyle a | ⩽ b \displaystyle\leqslant b |  |

 | 1 4 ​ n < a ​ c ​ d \displaystyle\frac{1}{4}n<acd | ⩽ 3 4 ​ n \displaystyle\leqslant\frac{3}{4}n |  |

 | b < c ​ e \displaystyle b<ce | ⩽ 2 ​ b \displaystyle\leqslant 2b |  |

 | a ​ n ⩽ b ​ f \displaystyle an\leqslant bf | ⩽ 5 3 ​ a ​ n. \displaystyle\leqslant\frac{5}{3}an. |  |

If instead ( x, y, z) = π n II ​ ( a, b, c, d, e, f) (x,y,z)=\pi^{\operatorname{II}}_{n}(a,b,c,d,e,f) is a Type II solution such that y ⩽ z y\leqslant z, then

 | a \displaystyle a | ⩽ b \displaystyle\leqslant b |  |

 | 1 4 ​ n < a ​ c ​ d ​ e \displaystyle\frac{1}{4}n<acde | ⩽ n \displaystyle\leqslant n |  |

 | b < c ​ e \displaystyle b<ce | ⩽ 2 ​ b \displaystyle\leqslant 2b |  |

 | 3 ​ a ​ c ​ d ⩽ f \displaystyle 3acd\leqslant f | < 4 ​ a ​ c ​ d \displaystyle<4acd |  |

Informally, the above lemma asserts that the magnitudes of the quantities ( a, b, c, d, e, f) (a,b,c,d,e,f) are controlled entirely by the parameters ( a, c, d, f) (a,c,d,f) (in the Type I case) and ( a, c, d, e) (a,c,d,e) (in the Type II case), with the bounds a ​ c ​ d ∼ n, f ≪ n acd\sim n,f\ll n in the Type I case and a ​ c ​ d ​ e ∼ n acde\sim n in the Type II case. The constants in the bounds here could be improved slightly, but such improvements will not be of importance in our applications.

###### Proof.

First suppose we have a Type I solution. As y ⩽ z y\leqslant z, we have a ⩽ b a\leqslant b. From ( 2.2) we then have b < c ​ e ⩽ 2 ​ b b<ce\leqslant 2b, and thus from ( 2.8) we have

 | a ​ n ⩽ b ​ f ⩽ a ​ n + 2 e ​ f ​ b ​ f. an\leqslant bf\leqslant an+\frac{2}{ef}bf. |  |

Now, from ( 2.7), e ​ f = 1 mod 4 ef=1\mod 4. If e = f = 1 e=f=1, then from ( 2.2) and ( 2.8) we would have b = n ​ a + c = n ​ a + a + b b=na+c=na+a+b, which is absurd, thus e ​ f ⩾ 5 ef\geqslant 5. This gives b ​ f ⩽ 5 ​ a ​ n / 3 bf\leqslant 5an/3 as claimed. From ( 2.8) this implies that c ⩽ 2 ​ a ​ n / 3 c\leqslant 2an/3, which in particular implies that b ​ c ​ d < a ​ b ​ d ​ n bcd<abdn and so y ⩽ z < x y\leqslant z<x. From ( 1.1) we conclude that

 | 4 3 ​ n ⩽ 1 y < 4 n \frac{4}{3n}\leqslant\frac{1}{y}<\frac{4}{n} |  |

which gives the bound n / 4 < a ​ c ​ d ⩽ 3 ​ n / 4 n/4<acd\leqslant 3n/4 as claimed.

Now suppose we have a Type II solution. Again a ⩽ b a\leqslant b and b < c ​ e ⩽ 2 ​ b b<ce\leqslant 2b. From ( 2.15) we have

 | n ​ c < 4 ​ a ​ b ​ c ​ d ⩽ n ​ c + 2 ​ a ​ b ​ c ​ d nc<4abcd\leqslant nc+2abcd |  |

and thus n / 4 < a ​ b ​ d ⩽ n / 2 n/4<abd\leqslant n/2, which by the c ​ e ce bound gives n / 4 < a ​ c ​ d ​ e ⩽ n n/4<acde\leqslant n. Since f = 4 ​ a ​ c ​ d − 1 f=4acd-1, we have 3 ​ a ​ c ​ d ⩽ f < 4 ​ a ​ c ​ d 3acd\leqslant f<4acd, and the claim follows. ∎

###### Remark 2.9.

From the above bounds one can also easily deduce the following observation: if 4 / p = 1 / x + 1 / y + 1 / z 4/p=1/x+1/y+1/z, then the largest denominator max ⁡ ( x, y, z) \max(x,y,z) is always divisible by p p. (This observation also appears in [15].)

###### Remark 2.10.

Propositions 2.2, 2.6 can be viewed as special cases of the classification by Heath-Brown [28] of primitive integer points ( x 1, x 2, x 3, x 4) ∈ ( ℤ \ { 0 }) 4 (x_{1},x_{2},x_{3},x_{4})\in(\mathbb{Z}\backslash\{0\})^{4} on Cayley’s surface

 | { ( x 1, x 2, x 3, x 4): 1 x 1 + 1 x 2 + 1 x 3 + 1 x 4 = 0 }, \left\{(x_{1},x_{2},x_{3},x_{4}):\frac{1}{x_{1}}+\frac{1}{x_{2}}+\frac{1}{x_{3}}+\frac{1}{x_{4}}=0\right\}, |  |

where by “primitive” we mean that x 1, x 2, x 3, x 4 x_{1},x_{2},x_{3},x_{4} have no common factor. Note that if n, x, y, z n,x,y,z solve ( 1.1), then ( − n, 4 ​ x, 4 ​ y, 4 ​ z) (-n,4x,4y,4z) is an integer point on this surface, which will be primitive when n n is prime. In [28, Lemma 1] it is shown that such integer points ( x 1, x 2, x 3, x 4) (x_{1},x_{2},x_{3},x_{4}) take the form

 | x i = ϵ ​ y j ​ y k ​ y l ​ z i ​ j ​ z i ​ k ​ z i ​ l x_{i}=\epsilon y_{j}y_{k}y_{l}z_{ij}z_{ik}z_{il} |  |

for { i, j, k, l } = { 1, 2, 3, 4 } \{i,j,k,l\}=\{1,2,3,4\}, where ϵ ∈ { − 1, + 1 } \epsilon\in\{-1,+1\} is a sign, and the y i, z i ​ j y_{i},z_{ij} are non-zero integers obeying the coprimality constraints

 | ( y i, y j) = ( z i ​ j, z k ​ l) = ( y i, z i ​ j) = 1 (y_{i},y_{j})=(z_{ij},z_{kl})=(y_{i},z_{ij})=1 |  |

for { i, j, k, l } = { 1, 2, 3, 4 } \{i,j,k,l\}=\{1,2,3,4\}, and obeying the equation

 | ∑ { i, j, k, l } = { 1, 2, 3, 4 } y i ​ z j ​ k ​ z k ​ l ​ z l ​ j = 0. \sum_{\{i,j,k,l\}=\{1,2,3,4\}}y_{i}z_{jk}z_{kl}z_{lj}=0. |  | (2.24) |

Conversely, any ϵ, y i, z i ​ j \epsilon,y_{i},z_{ij} obeying the above conditions induces a primitive integer point on Cayley’s surface. The Type I (resp. Type II) solutions correspond, roughly speaking, to the cases when one of the z 1 ​ i z_{1i} (resp. one of the y i y_{i}) in the factorisation

 | n = x 1 = ϵ ​ y 2 ​ y 3 ​ y 4 ​ z 12 ​ z 13 ​ z 14 n=x_{1}=\epsilon y_{2}y_{3}y_{4}z_{12}z_{13}z_{14} |  |

are equal to ± n \pm n. The y i, z i ​ j y_{i},z_{ij} coordinates are closely related to the ( a, b, c, d, e, f) (a,b,c,d,e,f) coordinates used in this section; in [28] it is observed that these coordinates obey a number of algebraic equations in addition to ( 2.24), which essentially describe (the closure of) the universal torsor [11] of Cayley’s surface.

In [28] it was shown that the number of integer points ( x 1, x 2, x 3, x 4) (x_{1},x_{2},x_{3},x_{4}) on Cayley’s surface of maximal height max ⁡ ( | x 1 |, …, | x 4 |) \max(|x_{1}|,\ldots,|x_{4}|) bounded by N N was comparable to N ​ log 6 ​ N N\log^{6}N. This is not quite the situation considered in our paper; a solution to ( 1.1) with n ⩽ N n\leqslant N induces an integer point ( x 1, x 2, x 3, x 4) (x_{1},x_{2},x_{3},x_{4}) whose *minimal*height min ⁡ ( | x 1 |, …, | x 4 |) \min(|x_{1}|,\ldots,|x_{4}|) is bounded by N N. Nevertheless, the results in [28] can be easily modified (by minor adjustments to account for the restriction that three of the x i x_{i} are positive, and restricting n n to be a multiple of 4 4 to eliminate divisibility constraints) to give a *lower bound*∑ n ⩽ N f ⁡ ( n) ≫ N ​ log 6 ​ N \sum_{n\leqslant N}f(n)\gg N\log^{6}N for the number of such points, though it is not immediately obvious whether this lower bound can be matched by a corresponding upper bound. Nevertheless, we see that there are several logarithmic factors separating the general solution count from the Type I and Type II solution count; in particular, for generic n n, the majority of solutions to ( 1.1) will neither be Type I nor Type II. In spite of this, the number of Type I and Type II solutions is the relevant quantity for studying the Erdős-Straus conjecture, as it is naturally to study it for prime denominators only.

We close this section with a small remark on the well known standard classification of solutions in Mordell’s book: His two cases (in his notation)

 | m p = 1 a ​ b ​ d + 1 a ​ c ​ d + 1 b ​ c ​ d ​ p \frac{m}{p}=\frac{1}{abd}+\frac{1}{acd}+\frac{1}{bcdp} |  |

with ( a, b) = ( a, c) = ( b, c) = 1 (a,b)=(a,c)=(b,c)=1 and p ∤ a ​ b ​ c ​ d p\nmid abcd and

 | m p = 1 a ​ b ​ d + 1 a ​ c ​ d ​ p + 1 b ​ c ​ d ​ p \frac{m}{p}=\frac{1}{abd}+\frac{1}{acdp}+\frac{1}{bcdp} |  |

( a, b) = ( a, c) = ( b, c) = 1 (a,b)=(a,c)=(b,c)=1 with p ∤ a ​ b ​ d p\nmid abd suggest that p | c p\mid c might be possible. Here we prove, for m > 3 m>3 and p p coprime to m m, that none of the denominators can be divisible by p 2 p^{2}. In particular p ∤ a ​ b ​ c ​ d p\nmid abcd in both of the cases above.

###### Proposition 2.11.

Let m / p = 1 / x + 1 / y + 1 / z m/p=1/x+1/y+1/z where m > 3 m>3, p p is a prime not dividing m m, and x, y, z x,y,z are natural numbers. Then none of x, y, z x,y,z are divisible by p 2 p^{2}.

Note that there are a small number of counterexamples to this proposition for m ⩽ 3 m\leqslant 3, such as 3 / 2 = 1 / 1 + 1 / 4 + 1 / 4 {3}/{2}={1}/{1}+{1}/{4}+{1}/{4}.

###### Proof.

We may assume that ( x, y, z) (x,y,z) is either a Type I or Type II solution (replacing 4 4 by m m as needed). In the Type I case ( x, y, z) = ( a ​ b ​ d ​ p, a ​ c ​ d, b ​ c ​ d) (x,y,z)=(abdp,acd,bcd), the claim is already clear since a ​ b ​ c ​ d abcd is known to be coprime to p p. In the Type II case ( x, y, z) = ( a ​ b ​ d, a ​ c ​ d ​ p, b ​ c ​ d ​ p) (x,y,z)=(abd,acdp,bcdp) it is known that a ​ b ​ d abd is coprime to p p, so the only remaining task is to establish that c c is coprime to p p also.

Suppose c c is not coprime to p p; then y, z y,z are both divisible by p 2 p^{2}. In particular

 | 1 y + 1 z ⩽ 2 p 2 \frac{1}{y}+\frac{1}{z}\leqslant\frac{2}{p^{2}} |  |

and hence

 | m p > 1 x ⩾ m p − 2 p 2. \frac{m}{p}>\frac{1}{x}\geqslant\frac{m}{p}-\frac{2}{p^{2}}. |  |

Taking reciprocals, we conclude that

 | p < m ​ x ⩽ p ​ ( 1 − 2 m ​ p) − 1. p<mx\leqslant p(1-\frac{2}{mp})^{-1}. |  |

Bounding ( 1 − ε) − 1 < 1 + 2 ​ ε (1-\varepsilon)^{-1}<1+2\varepsilon when 0 < ε < 1 / 2 0<\varepsilon<1/2, we conclude that

 | p < m ​ x < p + 4 m. p<mx<p+\frac{4}{m}. |  |

But if m > 3 m>3, this forces m ​ x mx to be a non-integer, a contradiction. ∎

## 3. Upper bounds for f i ​ ( n) f_{i}(n)

We may now prove Proposition 1.7.

We begin with the bound for f I ​ ( n) f_{\operatorname{I}}(n). By symmetry we may restrict attention to Type I solutions ( x, y, z) (x,y,z) for which y ⩽ z y\leqslant z. By Proposition 2.2 and Lemma 2.8, these solutions arise from sextuples ( a, b, c, d, e, f) ∈ ℕ 6 ∩ Σ n I (a,b,c,d,e,f)\in\mathbb{N}^{6}\cap\Sigma^{\operatorname{I}}_{n} obeying the Type I bounds in Lemma 2.8. In particular we see that

 | e ⋅ f ⋅ ( c ​ d) 2 ⋅ a ​ c = ( a ​ c ​ d) 2 ​ ( c ​ e b) ​ ( b ​ f a) ≪ n 3, e\cdot f\cdot(cd)^{2}\cdot ac=(acd)^{2}(\frac{ce}{b})(\frac{bf}{a})\ll n^{3}, |  |

and hence at least one of e, f, c ​ d, a ​ c e,f,cd,ac is O ⁡ ( n 3 / 5) O(n^{3/5}).

Suppose first that e ≪ n 3 / 5 e\ll n^{3/5}. For fixed e e, we see from ( 2.1) and the divisor bound ( A.6) that there are n O ⁡ ( 1 / log ⁡ log ​ n) n^{O({1}/{\log\log n})} choices for a, b, d a,b,d, giving a net total of n 3 / 5 + O ⁡ ( 1 / log ⁡ log ⁡ n) n^{3/5+O({1}/{\log\log n})} points in Σ n I \Sigma^{\operatorname{I}}_{n} in this case.

Similarly, if f ≪ n 3 / 5 f\ll n^{3/5}, ( 2.6) and the divisor bound gives n O ⁡ ( 1 / log ⁡ log ​ n) n^{O({1}/{\log\log n})} choices for a, c, d a,c,d for each f f, giving n 3 / 5 + O ⁡ ( 1 / log ⁡ log ⁡ n) n^{3/5+O({1}/{\log\log n})} solutions. If c ​ d ≪ n 3 / 5 cd\ll n^{3/5}, one uses ( 2.9) and the divisor bound to get n O ⁡ ( 1 / log ⁡ log ​ n) n^{O({1}/{\log\log n})} choices for b, f, c, d b,f,c,d for each choice of c ​ d cd, and if a ​ c ≪ n 3 / 5 ac\ll n^{3/5}, then ( 2.8) and the divisor bound gives n O ⁡ ( 1 / log ⁡ log ​ n) n^{O({1}/{\log\log n})} choices for a, b, c, f a,b,c,f for each fixed a ​ c ac. Putting all this together (and recalling that any three coordinates in Σ n I \Sigma^{\operatorname{I}}_{n} determine the other three) we obtain the first part of Proposition 1.7.

Now we prove the bound for f II ​ ( n) f_{\operatorname{II}}(n), which is similar. Again we may restrict attention to sextuples ( a, b, c, d, e, f) ∈ ℕ 6 ∩ Σ n II (a,b,c,d,e,f)\in\mathbb{N}^{6}\cap\Sigma^{\operatorname{II}}_{n} obeying the Type II bounds in Lemma 2.8. In particular we have

 | e 2 ⋅ ( a ​ d) ⋅ ( a ​ c) ⋅ ( c ​ d) = ( a ​ c ​ d ​ e) 2 ⩽ n 2 e^{2}\cdot(ad)\cdot(ac)\cdot(cd)=(acde)^{2}\leqslant n^{2} |  |

and so at least one of e, a ​ d, a ​ c, c ​ d e,ad,ac,cd is O ⁡ ( n 2 / 5) O(n^{2/5}).

If e ≪ n 2 / 5 e\ll n^{2/5}, we use ( 2.13) and the divisor bound to get n O ⁡ ( 1 / log ⁡ log ​ n) n^{O({1}/{\log\log n})} choices for a, b, d a,b,d for each e e. If a ​ d ≪ n 2 / 5 ad\ll n^{2/5}, we use ( 2.19) and the divisor bound to get n O ⁡ ( 1 / log ⁡ log ​ n) n^{O({1}/{\log\log n})} choices for a, d, e, f a,d,e,f for each fixed a ​ d ad. If a ​ c ≪ n 2 / 5 ac\ll n^{2/5}, we use ( 2.20) to get n O ⁡ ( 1 / log ⁡ log ​ n) n^{O({1}/{\log\log n})} choices for a, c, b, f a,c,b,f for each fixed a ​ c ac. If c ​ d ≪ n 2 / 5 cd\ll n^{2/5}, we use ( 2.21) and the divisor bound to get n O ⁡ ( 1 / log ⁡ log ​ n) n^{O({1}/{\log\log n})} choices for b, c, d, f b,c,d,f for each fixed c ​ d cd. Putting all this together we obtain the second part of Proposition 1.7.

###### Remark 3.1.

This argument, together with the fact that a large number n n can be factorised in expected O ⁡ ( n o ⁡ ( 1)) O(n^{o(1)}) time (using, say, the quadratic sieve [54]), gives an algorithm to find all Type I solutions for a given n n in expected run time O ⁡ ( n 3 / 5 + o ⁡ ( 1)) O(n^{3/5+o(1)}), and an algorithm to find all the Type II solutions in expected run time O ⁡ ( n 2 / 5 + o ⁡ ( 1)) O(n^{2/5+o(1)}).

## 4. Insolubility for odd squares

We now prove Proposition 1.6. Suppose for contradiction that n n is an odd perfect square (in particular, n = 1 mod 8 n=1\mod 8) with a Type I solution. Then by Proposition 2.2, we can find an ℕ \mathbb{N} -point ( a, b, c, d, e, f) (a,b,c,d,e,f) in Σ n I \Sigma^{\operatorname{I}}_{n}.

Let q q be the largest odd factor of a ​ b ab. From ( 2.1) we have n ​ e + 1 = 0 mod q ne+1=0\mod q. Since n n is a perfect square, we conclude that

 | ( e q) = ( − 1 q) = ( − 1) ( q − 1) / 4 \left(\frac{e}{q}\right)=\left(\frac{-1}{q}\right)=(-1)^{(q-1)/4} |  |

thanks to ( A.8). Since n = 1 mod 8 n=1\mod 8, we see from ( 2.1) that e = 3 mod 4 e=3\mod 4. By quadratic reciprocity ( A.7) we thus have

 | ( q e) = 1. \left(\frac{q}{e}\right)=1. |  |

On the other hand, from ( 2.2) we see that a ​ b = − a 2 mod e ab=-a^{2}\mod e, and thus

 | ( a ​ b e) = ( − 1 e) = − 1 \left(\frac{ab}{e}\right)=\left(\frac{-1}{e}\right)=-1 |  |

by ( A.8). This forces a ​ b ≠ q ab\neq q, and so (by definition of q q) a ​ b ab is even. By ( 2.1), this forces e = 7 mod 8 e=7\mod 8, which by ( A.9) implies that

 | ( 2 e) = 1 \left(\frac{2}{e}\right)=1 |  |

and thus

 | ( q e) = ( a ​ b e), \left(\frac{q}{e}\right)=\left(\frac{ab}{e}\right), |  |

a contradiction.

The proof in the Type II case is almost identical, using ( 2.13), ( 2.14) in place of ( 2.1), ( 2.2); we omit the details.

## 5. Lower bounds I

Now we prove the lower bounds in Theorem 1.1.

We begin with the lower bound

 | ∑ n ⩽ N f II ​ ( n) ≫ N ​ log 3 ​ N. \sum_{n\leqslant N}f_{\operatorname{II}}(n)\gg N\log^{3}N. |  | (5.1) |

Suppose a, c, d, e a,c,d,e are natural numbers with d d square-free, e e coprime to a ​ d ad, e > a e>a, and a ​ c ​ d ​ e ⩽ N / 4 acde\leqslant N/4. Then the quantity

 | n:= 4 ​ a ​ c ​ d ​ e − e − 4 ​ a 2 ​ d n:=4acde-e-4a^{2}d |  | (5.2) |

is a natural number of size at most N N, and ( a, c ​ e − a, c, d, e, 4 ​ a ​ c ​ d − 1) (a,ce-a,c,d,e,4acd-1) is an ℕ \mathbb{N} -point of Σ 𝔫 II \Sigma^{\operatorname{II}}_{\mathfrak{n}}. Applying π n II \pi^{\operatorname{II}}_{n}, we obtain a solution

 | ( x, y, z) = ( a ⁡ ( c ​ e − a) ​ d, a ​ c ​ d ​ n, ( c ​ e − a) ​ c ​ d ​ n) (x,y,z)=(a(ce-a)d,acdn,(ce-a)cdn) |  |

to ( 1.1). We claim that this is a Type II solution, or equivalently that a ⁡ ( c ​ e − a) ​ d a(ce-a)d is coprime to n n. As e e is coprime to a ​ d ad, we see from ( 5.2) that n n is coprime to a ​ d ​ e ade, so it suffices to show that n n is coprime to b:= c ​ e − a b:=ce-a. But if q q is a common factor of both n n and b b, then from the identity ( 2.20) (with f = 4 ​ a ​ c ​ d − 1 f=4acd-1) we see that q q is also a common factor of a a, a contradiction. Thus we have obtained a Type II solution. Also, as d d is square-free, any two quadruples ( a, c, d, e) (a,c,d,e) will generate different solutions, as the associated sextuples ( a, c ​ e − a, c, d, e, 4 ​ a ​ c ​ d − 1) (a,ce-a,c,d,e,4acd-1) cannot be related to each other by the dilation ( 2.10). Thus, it will suffice to show that there are at least δ ​ N ​ log 3 ⁡ N \delta N\log^{3}N quadruples ( a, c, d, e) ∈ ℕ (a,c,d,e)\in\mathbb{N} with d d square-free, e e coprime to a ​ d ad, e > a e>a, and a ​ c ​ d ​ e ⩽ N / 4 acde\leqslant N/4 for some absolute constant δ > 0 \delta>0. Restricting a, c, d a,c,d to be at most N 0.1 N^{0.1} (say), we see that the number of possible choices of e e is at least δ ′ ​ ( N / a ​ c ​ d) ​ ϕ ​ ( a ​ d) / a ​ d \delta^{\prime}({N}/{acd}){\phi(ad)}/{ad}, where ϕ \phi is the Euler totient function and δ ′ > 0 \delta^{\prime}>0 is another absolute constant. It thus suffices to show that

 | ∑ a, c, d ⩽ N 0.1 μ 2 ​ ( d) ​ ϕ ⁡ ( a ​ d) a ​ d ​ 1 a ​ d ​ c ≫ log 3 ⁡ N, \sum_{a,c,d\leqslant N^{0.1}}\mu^{2}(d)\frac{\phi(ad)}{ad}\frac{1}{adc}\gg\log^{3}N, |  |

where μ \mu is the Möbius function (so μ 2 ​ ( d) = 1 \mu^{2}(d)=1 exactly when d d is square-free). Using the elementary estimate ϕ ⁡ ( a ​ d) ⩾ ϕ ⁡ ( a) ​ ϕ ​ ( d) \phi(ad)\geqslant\phi(a)\phi(d) and factorising, we see that it suffices to show that

 | ∑ d ⩽ N 0.1 μ ​ ( d) 2 ​ ϕ ​ ( d) d 2 ≫ log ⁡ N. \sum_{d\leqslant N^{0.1}}\frac{\mu(d)^{2}\phi(d)}{d^{2}}\gg\log N. |  | (5.3) |

But this follows from Lemma A.1.

Now we prove the lower bound

 | ∑ n ⩽ N f I ​ ( n) ≫ N ​ log 3 ​ N, \sum_{n\leqslant N}f_{\operatorname{I}}(n)\gg N\log^{3}N, |  |

which follows by a similar method.

Suppose a, c, d, f a,c,d,f are natural numbers with d d square-free, f f dividing 4 ​ a 2 ​ d + 1 4a^{2}d+1 and coprime to c c, d ⩾ f d\geqslant f, and a ​ c ​ d ⩽ N / 4 acd\leqslant N/4. Then the quantity

 | n:= 4 ​ a ​ c ​ d − f n:=4acd-f |  | (5.4) |

is a natural number which is at most N N, and ( a, b, c, d, 4 ​ a 2 ​ d + 1 / f, f) (a,b,c,d,{4a^{2}d+1}/{f},f) is an ℕ \mathbb{N} -point of Σ n I \Sigma^{\operatorname{I}}_{n}, where

 | b:= c ​ 4 ​ a 2 ​ d + 1 f − e = n ​ a + c f. b:=c\frac{4a^{2}d+1}{f}-e=\frac{na+c}{f}. |  |

Applying π n I \pi^{\operatorname{I}}_{n}, this gives a solution

 | ( x, y, z) = ( a ​ b ​ d ​ n, a ​ c ​ d, b ​ c ​ d) (x,y,z)=(abdn,acd,bcd) |  |

to ( 1.1), and as before the square-free nature of d d ensures that each quadruple ( a, c, d, f) (a,c,d,f) gives a different solution. We claim that this is a Type I solution, i.e. that a ​ b ​ c ​ d abcd is coprime to n n. As f f divides 4 ​ a 2 ​ d + 1 4a^{2}d+1, f f and with ( 5.4) also n n is coprime to a ​ d ad. As f f and c c are coprime by assumption, n n is coprime to a ​ c ​ d acd by ( 5.4). As b = ( n ​ a + c) / f b=(na+c)/f, we conclude that n n is also coprime to b b.

Thus it will suffice to show that there are at least δ ​ N ​ log 3 ⁡ N \delta N\log^{3}N quadruples ( a, c, d, f) ∈ ℕ 4 (a,c,d,f)\in\mathbb{N}^{4} with f f coprime to 2 ​ a ​ c 2ac, and d d square-free with f f dividing 4 ​ a 2 ​ d + 1 4a^{2}d+1, d ⩾ f d\geqslant f, and a ​ c ​ d ⩽ N / 4 acd\leqslant N/4, for some absolute constant δ > 0 \delta>0.

We restrict a, c, f a,c,f to be at most N 0.1 N^{0.1}. If f f is coprime to 2 ​ a ​ c 2ac, then there is a unique primitive residue class of f f such that 4 ​ a 2 ​ d + 1 4a^{2}d+1 is a multiple of f f for all d d in this class. Also, there are at least δ ​ N / a ​ c ​ f \delta{N}/{acf} elements d d of this residue class with d ⩾ f d\geqslant f and a ​ c ​ d ⩽ N / 4 acd\leqslant N/4 for some absolute constant δ > 0 \delta>0; a standard sieving argument shows that a positive proportion of these elements are square-free. Thus, we have a lower bound of

 | ∑ a, c, f ⩽ N 0.1: ( f, 2 ​ a ​ c) = 1 N a ​ c ​ f \sum_{a,c,f\leqslant N^{0.1}:(f,2ac)=1}\frac{N}{acf} |  |

for the number of quadruples. Restricting f f to be odd and then using the crude sieve

 | 1 ( f, 2 ​ a ​ c) = 1 ⩾ 1 − ∑ p 1 p | f ​ 1 p | a − ∑ p 1 p | f ​ 1 p | c 1_{(f,2ac)=1}\geqslant 1-\sum_{p}1_{p\mid f}1_{p\mid a}-\sum_{p}1_{p\mid f}1_{p\mid c} |  | (5.5) |

where p p ranges over odd primes, where 1 E 1_{E} denotes the indicator function of a statement E E (i.e. 1 E = 1 1_{E}=1 if E E holds, and 1 E = 0 1_{E}=0 otherwise), one easily verifies that the above expression is at least δ ​ N ​ log 3 ⁡ N \delta N\log^{3}N for some absolute constant δ > 0 \delta>0, and the claim follows.

Now we establish the lower bound

 | ∑ p ⩽ N f II ​ ( p) ≫ N ​ log 2 ​ N. \sum_{p\leqslant N}f_{\operatorname{II}}(p)\gg N\log^{2}N. |  |

We will repeat the proof of ( 5.1), but because we are now counting primes instead of natural numbers we will need to invoke the Bombieri-Vinogradov inequality at a key juncture.

Suppose a, c, d, e a,c,d,e are natural numbers with d d square-free, a, c, d ⩽ N 0.1 a,c,d\leqslant N^{0.1}, and e e between N 0.6 N^{0.6} and N / 4 ​ a ​ c ​ d N/4acd with

 | p:= 4 ​ a ​ c ​ d ​ e − e − 4 ​ a 2 ​ d p:=4acde-e-4a^{2}d |  | (5.6) |

prime. Then p p is at most N N and at least N 0.6 N^{0.6}, and in particular is automatically coprime to a ​ d ​ e ade (and thus c ​ e − a ce-a, by previous arguments). Thus, as before, each such ( a, c, d, e) (a,c,d,e) gives a Type II solution for a prime p ⩽ N p\leqslant N, with different quadruples giving different solutions. Thus it suffices to show that there are at least δ ​ N ​ log 2 ⁡ N \delta N\log^{2}N quadruples ( a, c, d, e) (a,c,d,e) with the above properties for some absolute constant δ > 0 \delta>0.

Fix a, c, d a,c,d. As e e ranges from N 0.6 N^{0.6} to N / 4 ​ a ​ c ​ d N/4acd, the expression ( 5.6) traces out a primitive residue class modulo 4 ​ a ​ c ​ d − 1 4acd-1, omitting at most O ⁡ ( N 0.6) O(N^{0.6}) members of this class that are less than N N. Thus, the number of primes of the form ( 5.6) for fixed a ​ c ​ d acd is

 | π ⁡ ( N, 4 ​ a ​ c ​ d − 1, − 4 ​ a 2 ​ d) − O ⁡ ( N 0.6), \pi(N;4acd-1,-4a^{2}d)-O(N^{0.6}), |  |

where π ⁡ ( N, q, t) \pi(N;q,t) denotes the number of primes p < N p<N that are congruent to t t mod q q. We replace π ⁡ ( N, 4 ​ a ​ c ​ d − 1, − 4 ​ a 2 ​ d) \pi(N;4acd-1,-4a^{2}d) by a good approximation, and bound the error. If we set

 | D ⁡ ( N, q):= max ( a, q) = 1 ⁡ | π ⁡ ( N, q, a) − li ⁡ ( N) ϕ ⁡ ( q) | D(N;q):=\max_{(a,q)=1}\left|\pi(N;q,a)-\frac{{\rm li}(N)}{\phi(q)}\right| |  |

(as in ( A.13)), where li ⁡ ( x):= ∫ 0 x 𝑑 t / log ⁡ t {\rm li}(x):=\int_{0}^{x}{dt}/{\log t} is the Cauchy principal value of the logarithmic integral, the number of primes of the form ( 5.6) for fixed a ​ c ​ d acd is at least

 | li ⁡ ( N) ϕ ⁡ ( 4 ​ a ​ c ​ d − 1) − D ⁡ ( N, 4 ​ a ​ c ​ d − 1) − O ⁡ ( N 0.6) \frac{{\rm li}(N)}{\phi(4acd-1)}-D(N;4acd-1)-O(N^{0.6}) |  |

The overall contribution of those a ​ c ​ d acd combinations referring to the O ⁡ ( N 0.6) O(N^{0.6}) error term is at most O ⁡ ( ( N 0.1) 3 ​ N 0.6) = o ⁡ ( N ​ log 2 ​ N) O((N^{0.1})^{3}N^{0.6})=o(N\log^{2}N), while li ⁡ ( N) {\rm li}(N) is comparable to N / log ⁡ N N/\log N, so it will suffice to show the lower bound

 | ∑ a, c, d ⩽ N 0.1 μ 2 ​ ( d) ϕ ⁡ ( 4 ​ a ​ c ​ d − 1) ≫ log 3 ⁡ N \sum_{a,c,d\leqslant N^{0.1}}\frac{\mu^{2}(d)}{\phi(4acd-1)}\gg\log^{3}N |  | (5.7) |

and the upper bound

 | ∑ a, c, d ⩽ N 0.1 D ⁡ ( N, 4 ​ a ​ c ​ d − 1) = o ⁡ ( N ​ log 2 ​ N). \sum_{a,c,d\leqslant N^{0.1}}D(N;4acd-1)=o(N\log^{2}N). |  | (5.8) |

We first prove ( 5.7). Using the trivial bound ϕ ⁡ ( 4 ​ a ​ c ​ d − 1) ⩽ 4 ​ a ​ c ​ d \phi(4acd-1)\leqslant 4acd, it suffices to show that

 | ∑ a, c, d ⩽ N 0.1 μ 2 ​ ( d) a ​ c ​ d ≫ log 3 ⁡ N \sum_{a,c,d\leqslant N^{0.1}}\frac{\mu^{2}(d)}{acd}\gg\log^{3}N |  |

which upon factorising reduces to showing

 | ∑ d ⩽ N 0.1 μ 2 ​ ( d) d ≫ log ⁡ N. \sum_{d\leqslant N^{0.1}}\frac{\mu^{2}(d)}{d}\gg\log N. |  |

But this follows from Lemma A.1.

Now we show ( 5.8). Writing q:= 4 ​ a ​ c ​ d − 1 q:=4acd-1, we can upper bound the left-hand side of ( 5.8) somewhat crudely by

 | ∑ q ⩽ N 0.3 D ⁡ ( N, q) ​ τ ​ ( q + 1) 2. \sum_{q\leqslant N^{0.3}}D(N;q)\tau(q+1)^{2}. |  |

From divisor moment estimates (see ( A.4)) we have

 | ∑ q ⩽ N 0.3 τ ​ ( q + 1) 4 q ≪ log O ⁡ ( 1) ⁡ N; \sum_{q\leqslant N^{0.3}}\frac{\tau(q+1)^{4}}{q}\ll\log^{O(1)}N; |  |

hence by Cauchy-Schwarz, we may bound the preceding quantity by

 | ≪ log O ⁡ ( 1) ⁡ N ​ ( ∑ q ⩽ N 0.3 q ​ D ​ ( N, q) 2) 1 / 2. \ll\log^{O(1)}N\left(\sum_{q\leqslant N^{0.3}}qD(N;q)^{2}\right)^{1/2}. |  |

Using the trivial bound D ⁡ ( N, q) ≪ N / q D(N;q)\ll N/q, we bound this in turn by

 | ≪ N 1 / 2 ​ log O ⁡ ( 1) ​ N ​ ( ∑ q ⩽ N 0.3 D ⁡ ( N, q)) 1 / 2. \ll N^{1/2}\log^{O(1)}N\left(\sum_{q\leqslant N^{0.3}}D(N;q)\right)^{1/2}. |  |

But from the Bombieri-Vinogradov inequality ( A.14), we have

 | ∑ q ⩽ N 0.3 D ( N; q) ≪ A N log − A N \sum_{q\leqslant N^{0.3}}D(N;q)\ll_{A}N\log^{-A}N |  |

for any A > 0 A>0, and the claim ( 5.8) follows.

Finally, we establish the lower bound

 | ∑ p ⩽ N f I ​ ( p) ≫ N ​ log 2 ​ N. \sum_{p\leqslant N}f_{\operatorname{I}}(p)\gg N\log^{2}N. |  |

Unsurprisingly, we will repeat many of the arguments from preceding cases. Suppose a, c, d, f a,c,d,f are natural numbers with a, c, f ⩽ N 0.1 a,c,f\leqslant N^{0.1} with ( a, c) = ( 2 ​ a ​ c, f) = 1 (a,c)=(2ac,f)=1, N 0.6 ⩽ d ⩽ N / 4 ​ a ​ c N^{0.6}\leqslant d\leqslant N/4ac, such that f f divides 4 ​ a 2 ​ d + 1 4a^{2}d+1, and the quantity

 | p:= 4 ​ a ​ c ​ d − f p:=4acd-f |  | (5.9) |

is prime. Then p p is at most N N and is at least N 0.4 N^{0.4}, and in particular is coprime to a, c, f a,c,f; from ( 5.9) it is coprime to d d also. This thus yields a Type I solution for p p; by the coprimality of a, c a,c, these solutions are all distinct as no two of the associated sextuples ( a, b, c, d, 4 ​ a 2 ​ d + 1 / f, f) (a,b,c,d,{4a^{2}d+1}/{f},f) can be related by ( 2.10). Thus it suffices to show that there are at least δ ​ N ​ log 2 ⁡ N \delta N\log^{2}N quadruples ( a, c, d, f) (a,c,d,f) with the above properties for some absolute constant δ > 0 \delta>0.

For fixed a, c, f a,c,f, the parameter d d traverses a primitive congruence class modulo f f, and p = 4 ​ a ​ c ​ d − f p=4acd-f traverses a primitive congruence class modulo 4 ​ a ​ c ​ f 4acf, that omits at most O ⁡ ( N 0.6) O(N^{0.6}) of the elements of this class that are less than N N. By ( A.13), the total number of d d that thus give a prime p p for fixed a ​ c ​ f acf is at least

 | li ⁡ ( N) ϕ ⁡ ( 4 ​ a ​ c ​ f) − D ⁡ ( N, 4 ​ a ​ c ​ f) − O ⁡ ( N 0.6) \frac{{\rm li}(N)}{\phi(4acf)}-D(N;4acf)-O(N^{0.6}) |  |

and so by arguing as before it suffices to show the bounds

 | ∑ a, c, f ⩽ N 0.1 1 ( a, c) = ( 2 ​ a ​ c, f) = 1 ​ 1 ϕ ⁡ ( 4 ​ a ​ c ​ f) ≫ log 3 ⁡ N \sum_{a,c,f\leqslant N^{0.1}}1_{(a,c)=(2ac,f)=1}\frac{1}{\phi(4acf)}\gg\log^{3}N |  |

and

 | ∑ a, c, f ⩽ N 0.1 D ⁡ ( N, 4 ​ a ​ c ​ f) = o ⁡ ( N ​ log 2 ​ N). \sum_{a,c,f\leqslant N^{0.1}}D(N;4acf)=o(N\log^{2}N). |  |

But this is proven by a simple modification of the arguments used to establish ( 5.8), ( 5.7) (the constraints ( a, c) = ( 2 ​ a ​ c, f) = 1 (a,c)=(2ac,f)=1 being easily handled by an elementary sieve such as ( 5.5)). This concludes all the lower bounds for Theorem 1.1.

## 6. Lower bounds II

Here we prove Theorem 1.8.

###### Proof.

For any natural numbers m, n m,n, let g 2 ​ ( m, n) g_{2}(m,n) denote the number of solutions ( x, y) ∈ ℕ 2 (x,y)\in\mathbb{N}^{2} to the Diophantine equation m / n = 1 / x + 1 / y {m}/{n}={1}/{x}+{1}/{y}. Since

 | 1 x + 1 y = 1 x + 1 2 ​ y + 1 2 ​ y \frac{1}{x}+\frac{1}{y}=\frac{1}{x}+\frac{1}{2y}+\frac{1}{2y} |  |

we conclude the crude bound f ⁡ ( n) ⩾ g 2 ​ ( 4, n) f(n)\geqslant g_{2}(4,n) for any n n.

In [8, Theorem 1] it was shown that g 2 ​ ( m, n) ≫ 3 s g_{2}(m,n)\gg 3^{s} whenever n n is the product of s s distinct primes congruent to − 1 mod m -1\mod m. Since g 2 ​ ( m, k ​ n) ⩾ g 2 ​ ( m, n) g_{2}(m,kn)\geqslant g_{2}(m,n) for any k k, we conclude that

 | f ⁡ ( n) ⩾ g 2 ​ ( 4, n) ≫ 3 w 4 ​ ( n) f(n)\geqslant g_{2}(4,n)\gg 3^{w_{4}(n)} |  | (6.1) |

for all n n, where w m ​ ( n) w_{m}(n) is the number of distinct prime factors of n n that are congruent to − 1 mod m -1\mod m.

Now we prove the first part of the theorem. Let s s be a large number, and let n n be the product of the first s s primes equal to − 1 mod 4 -1\mod 4, then from the prime number theorem in arithmetic progressions we have log ⁡ n = ( 1 + o ⁡ ( 1)) ​ s ​ log ⁡ s \log n=(1+o(1))s\log s, and thus s = ( 1 + o ⁡ ( 1)) ​ log ⁡ n / log ⁡ log ⁡ n s=(1+o(1)){\log n}/{\log\log n}. From ( 6.1) we then have

 | f ⁡ ( n) ≫ exp ⁡ ( log ⁡ 3 ​ ( 1 + o ⁡ ( 1)) ​ log ⁡ n log ⁡ log ⁡ n). f(n)\gg\exp\left(\log 3(1+o(1))\frac{\log n}{\log\log n}\right). |  |

Letting s → ∞ s\to\infty we obtain the claim.

For the second part of the theorem, we use the Turán-Kubilius inequality (Lemma A.2) to the additive function w 4 w_{4}. This inequality gives that

 | ∑ n ⩽ N | w 4 ​ ( n) − 1 2 ​ log ⁡ log ⁡ N | 2 ≪ N ​ log ⁡ log ⁡ N. \sum_{n\leqslant N}|w_{4}(n)-\frac{1}{2}\log\log N|^{2}\ll N\log\log N. |  |

From this and Chebyshev’s inequality (see also [80, p. 307]), we see that

 | w 4 ​ ( n) ⩾ 1 2 ​ log ⁡ log ⁡ n + O ⁡ ( ξ ⁡ ( n) ​ log ⁡ log ⁡ n) w_{4}(n)\geqslant\frac{1}{2}\log\log n+O(\xi(n)\sqrt{\log\log n}) |  |

for all n n in a density 1 1 subset of ℕ \mathbb{N}. The claim then follows from ( 6.1).

Now we turn to the third part of the theorem. We first deal with the case when p = 4 ​ t − 1 p=4t-1 is prime, then

 | 4 p = 4 p + 1 + 1 t ⁡ ( 4 ​ t − 1) \frac{4}{p}=\frac{4}{p+1}+\frac{1}{t(4t-1)} |  |

which in particular implies that

 | f ⁡ ( p) ⩾ g 2 ​ ( 4, p + 1) f(p)\geqslant g_{2}(4,p+1) |  |

and thus

 | f ⁡ ( p) ≫ 3 w 4 ​ ( p + 1). f(p)\gg 3^{w_{4}(p+1)}. |  |

By Lemma A.2 we know that

 | w 4 ​ ( p + 1) ⩾ ( 1 2 − o ⁡ ( 1)) ​ log ⁡ log ⁡ p w_{4}(p+1)\geqslant\left(\frac{1}{2}-o(1)\right)\log\log p |  | (6.2) |

for all p p in a a set of primes of relative prime density 1 1.

It remains to deal with those primes p p congruent to 1 mod 4 1\mod 4. Writing

 | 4 p = 1 ( p + 3) / 4 + 3 p ⁡ ( p + 3) / 4 \frac{4}{p}=\frac{1}{(p+3)/4}+\frac{3}{p(p+3)/4} |  |

we see that

 | f ⁡ ( p) ⩾ g 2 ​ ( 3, p ⁡ ( p + 3) / 4) ≫ 3 w 3 ​ ( ( p + 3) / 4) ≫ 3 w 3 ​ ( p + 3). f(p)\geqslant g_{2}(3,p(p+3)/4)\gg 3^{w_{3}((p+3)/4)}\gg 3^{w_{3}(p+3)}. |  |

It thus suffices to show that

 | w 3 ​ ( p + 3) ⩾ ( 1 2 − o ⁡ ( 1)) ​ log ⁡ log ⁡ p w_{3}(p+3)\geqslant\left(\frac{1}{2}-o(1)\right)\log\log p |  |

for all p p in a set of primes of relative density 1 1. But this can be established by the same techniques used to establish ( 6.2).

∎

## 7. Sums of divisor functions

Let P: ℤ → ℤ P:\mathbb{Z}\to\mathbb{Z} be a polynomial with integer coefficients, which for simplicity we will assume to be non-negative, and consider the sum

 | ∑ n ⩽ N τ ⁡ ( P ⁡ ( n)). \sum_{n\leqslant N}\tau(P(n)). |  |

In [19], Erdős established the bounds

 | N log N ≪ P ∑ n ⩽ N τ ( P ( n)) ≪ P N log N N\log N\ll_{P}\sum_{n\leqslant N}\tau(P(n))\ll_{P}N\log N |  | (7.1) |

for all N > 1 N>1 and for P P irreducible; note that the implied constants here can depend on both the degree and the coefficients of P P. This is of course consistent with the heuristic τ ⁡ ( n) ∼ log ⁡ n \tau(n)\sim\log n “on average”. Of course, the irreducibility hypothesis is necessary as otherwise P ⁡ ( n) P(n) would be expected to have many more divisors.

In this section we establish a refinement of the Erdős upper bound that gives a more precise description of the dependence of the implied constant on P P (and with irreducibility replaced by a much weaker hypothesis), which may be of some independent interest:

###### Theorem 7.1 (Erdős-type bound).

Let N > 1 N>1, let P P be a polynomial with degree D D and coefficients being non-negative integers of magnitude at most N l N^{l}. For any natural number m m, let ρ ⁡ ( m) \rho(m) be the number of roots of P mod m P\mod m in ℤ / m ​ ℤ \mathbb{Z}/m\mathbb{Z}, and suppose one has the bound

 | ρ ⁡ ( p j) ⩽ C \rho(p^{j})\leqslant C |  | (7.2) |

for all primes p p and all j ⩾ 1 j\geqslant 1. Then

 | N ∑ m ⩽ N ρ ⁡ ( m) m ≪ ∑ n ⩽ N τ ( P ( n)) ≪ D, l, C N ∑ m ⩽ N ρ ⁡ ( m) m. N\sum_{m\leqslant N}\frac{\rho(m)}{m}\ll\sum_{n\leqslant N}\tau(P(n))\ll_{D,l,C}N\sum_{m\leqslant N}\frac{\rho(m)}{m}. |  |

###### Remark 7.2.

For any fixed P P, one has ( 7.2) for some C = C P C=C_{P} (by many applications of Hensel’s lemma, and treating the case of small p p separately), and when P P is irreducible one can use tools such as Landau’s prime ideal theorem to show that ∑ m ⩽ N ρ ( m) / m ≪ P log N \sum_{m\leqslant N}{\rho(m)}/{m}\ll_{P}\log N (indeed, much more precise asymptotics are available here). See [78] for more precise bounds on C C in terms of quantities such as the discriminant Δ ⁡ ( P) \Delta(P) of P P; bounds of this type go back to Nagell [45] and Ore [50] (see also [66], [32]). One should in fact be able to establish a version of Theorem 7.1 in which the implied constant depends explicitly on the Δ ⁡ ( P) \Delta(P) rather than on C C by using the estimates of Henriot [29] (which build upon earlier work of Barban-Vehov [2], Daniel [13], Shiu [73], Nair [46], and Nair-Tenenbaum [47]), but we will not do so here, as we will need to apply this bound in a situation in which the discriminant may be large, but for which the bound C C in ( 7.2) can still be taken to be small. However, the version of Nair’s estimate given in [7, Theorem 2], having no explicit dependence on the discriminant, may be able to give an alternate derivation of Theorem 7.1; we thank the referee for this observation.

Thus we see that Erdős’ original result ( 7.1) is a corollary of Theorem 7.1. For special types of P P (e.g. linear or quadratic polynomials), more precise asymptotics on ∑ n ⩽ N τ ⁡ ( P ⁡ ( n)) \sum_{n\leqslant N}\tau(P(n)) are known (see e.g. [21], [22] for the linear case, and [30], [70], [41], [42], [43] for the quadratic case), but the methods used are less elementary (e.g. Kloosterman sum bounds in the linear case, and class field theory in the quadratic case), and do not cover all ranges of coefficients of P P for the applications to the Erdős-Straus conjecture. See also [55] for another upper bound in the quadratic case which is uniform over large ranges of coefficients but gives weaker bounds (losing some powers of log ⁡ N \log N).

###### Proof.

Our argument will be based on the methods in [19]. In this proof all implied constants will be allowed to depend on D, l D,l and C C.

We begin with the lower bound, which is very easy. Clearly

 | τ ( P ( n)) ⩾ ∑ m ⩽ N: m | P ⁡ ( n) 1 \tau(P(n))\geqslant\sum_{m\leqslant N:m\mid P(n)}1 |  | (7.3) |

and thus

 | ∑ n ⩽ N τ ( P ( n)) ⩾ ∑ m ⩽ N ∑ n ⩽ N: m | P ⁡ ( n) 1. \sum_{n\leqslant N}\tau(P(n))\geqslant\sum_{m\leqslant N}\sum_{n\leqslant N:m\mid P(n)}1. |  |

The expression P ⁡ ( n) mod m P(n)\mod m is periodic in n n with period m m, and thus for m ⩽ N m\leqslant N one has

 | N ρ ⁡ ( m) m ≪ ∑ n ⩽ N: m | P ⁡ ( n) 1 ≪ N ρ ⁡ ( m) m N\frac{\rho(m)}{m}\ll\sum_{n\leqslant N:m\mid P(n)}1\ll N\frac{\rho(m)}{m} |  | (7.4) |

which gives the lower bound on ∑ n ⩽ N τ ⁡ ( P ⁡ ( n)) \sum_{n\leqslant N}\tau(P(n)).

Now we turn to the upper bound, which is more difficult. We first establish a preliminary bound

 | ∑ n ⩽ N τ ​ ( P ⁡ ( n)) 2 ≪ N ​ log O ⁡ ( 1) ​ N \sum_{n\leqslant N}\tau(P(n))^{2}\ll N\log^{O(1)}N |  | (7.5) |

using an argument of Landreau [38]. Let n ⩽ N n\leqslant N. By the coefficient bounds on P P we have

 | P ⁡ ( n) ≪ N O ⁡ ( 1). P(n)\ll N^{O(1)}. |  | (7.6) |

Using the main lemma from [38], we conclude that

 | τ ( P ( n)) 2 ≪ ∑ m ⩽ N: m | P ⁡ ( n) τ ( m) O ⁡ ( 1) \tau(P(n))^{2}\ll\sum_{m\leqslant N:m\mid P(n)}\tau(m)^{O(1)} |  |

and thus

 | ∑ n ⩽ N τ ( P ( n)) 2 ≪ ∑ m ⩽ N τ ( m) O ⁡ ( 1) ∑ n ⩽ N: m | P ⁡ ( n) 1. \sum_{n\leqslant N}\tau(P(n))^{2}\ll\sum_{m\leqslant N}\tau(m)^{O(1)}\sum_{n\leqslant N:m\mid P(n)}1. |  |

Using ( 7.2), we may crudely bound ∑ n ⩽ N: m | P ⁡ ( n) 1 ⩽ τ ( m) O ⁡ ( 1) \sum_{n\leqslant N:m\mid P(n)}1\leqslant\tau(m)^{O(1)}, thus

 | ∑ n ⩽ N τ ​ ( P ⁡ ( n)) 2 ≪ ∑ m ⩽ N τ ​ ( m) O ⁡ ( 1) \sum_{n\leqslant N}\tau(P(n))^{2}\ll\sum_{m\leqslant N}\tau(m)^{O(1)} |  |

and the claim then follows from Lemma A.1.

In view of ( 7.5) and the Cauchy-Schwarz inequality, we may discard from the n n summation any subset of { 1, …, N } \{1,\ldots,N\} of cardinality at most N ​ log − C ′ ​ N N\log^{-C^{\prime}}N for sufficiently large C ′ C^{\prime}. We will take advantage of this freedom in the sequel.

Suppose for the moment that we could reverse ( 7.3) and obtain the bound

 | τ ( P ( n)) ≪ ∑ m ⩽ N: m | P ⁡ ( n) 1. \tau(P(n))\ll\sum_{m\leqslant N:m\mid P(n)}1. |  | (7.7) |

Combining this with ( 7.4), we would obtain

 | ∑ n ⩽ N τ ⁡ ( P ⁡ ( n)) \displaystyle\sum_{n\leqslant N}\tau(P(n)) | ≪ ∑ m ⩽ N ∑ n ⩽ N: m | P ⁡ ( n) 1 \displaystyle\ll\sum_{m\leqslant N}\sum_{n\leqslant N:m\mid P(n)}1 |  |

 |  | ≪ ∑ m ⩽ N N m ​ ρ ​ ( m) \displaystyle\ll\sum_{m\leqslant N}\frac{N}{m}\rho(m) |  |

which would give the theorem. Unfortunately, while ( 7.7) is certainly true when P ⁡ ( n) ⩽ N 2 P(n)\leqslant N^{2}, it can fail for larger values of P ⁡ ( n) P(n), and from the coefficient bounds on P P we only have the weaker upper bound ( 7.6).

Nevertheless, as observed by Erdős, we have the following substitute for ( 7.7):

###### Lemma 7.3.

Let C ′ C^{\prime} be a fixed constant. For all but at most O ⁡ ( N ​ log − C ′ ​ N) O(N\log^{-C^{\prime}}N) values of n n in the range 1 ⩽ n ⩽ N 1\leqslant n\leqslant N, either ( 7.7) holds, or one has

 | τ ( P ( n)) ≪ O ( 1) r ∑ m ∈ S r: m | P ⁡ ( n) 1 \tau(P(n))\ll O(1)^{r}\sum_{m\in S_{r}:m\mid P(n)}1 |  |

for some 2 ⩽ r ≪ ( log ⁡ log ⁡ N) 2 2\leqslant r\ll(\log\log N)^{2}, where S r S_{r} is the set of all m m with the following properties:

- •

m m lies between N 1 / 4 N^{1/4} and N N.

- •

m m is N 1 / r N^{1/r} -smooth (i.e. m m is divisible by any prime larger than N 1 / r N^{1/r}).

- •

m m has at most ( log ⁡ log ⁡ N) 2 (\log\log N)^{2} prime factors.

- •

m m is not divisible by any prime power p k p^{k} with p ⩽ N 1 / 2 p\leqslant N^{1/2}, k > 1 k>1, and p k ⩾ N 1 / 8 ​ ( log ⁡ log ⁡ N) 2 p^{k}\geqslant N^{1/8(\log\log N)^{2}}.

The point here is that the exponential loss in the O ​ ( 1) r O(1)^{r} factor will be more than compensated for by the N 1 / r N^{1/r} -smooth requirement, which as we shall see gains a factor of r − c ​ r r^{-cr} for some absolute constant c > 0 c>0.

###### Proof.

The claim follows from ( 7.7) when P ⁡ ( n) ⩽ N 2 P(n)\leqslant N^{2}, so we may assume that P ⁡ ( n) > N 2 P(n)>N^{2}.

We factorise P ⁡ ( n) P(n) as

 | P ⁡ ( n) = p 1 ​ … ​ p J P(n)=p_{1}\ldots p_{J} |  |

where the primes p 1 ⩽ … ⩽ p J p_{1}\leqslant\ldots\leqslant p_{J} are arranged in non-decreasing order. Let 0 ⩽ j < J 0\leqslant j<J be the largest integer such that p 1 ​ … ​ p j ⩽ N p_{1}\ldots p_{j}\leqslant N. If j = 0 j=0 then all prime factors of P ⁡ ( n) P(n) are greater than N N, and thus by ( 7.6) we have J = O ⁡ ( 1) J=O(1) and thus τ ⁡ ( P ⁡ ( n)) = O ⁡ ( 1) \tau(P(n))=O(1), which makes the claim ( 7.7) trivial. Thus we may assume that j ⩾ 1 j\geqslant 1.

Suppose first that all the primes p j + 1, …, p J p_{j+1},\ldots,p_{J} have size at least N 1 / 2 N^{1/2}. Then from ( 7.6) we in fact have J = j + O ⁡ ( 1) J=j+O(1), and so

 | τ ⁡ ( P ⁡ ( n)) ≪ τ ⁡ ( p 1 ​ … ​ p j). \tau(P(n))\ll\tau(p_{1}\ldots p_{j}). |  |

Note that every factor of p 1 ​ … ​ p j p_{1}\ldots p_{j} divides P ⁡ ( n) P(n) and is at most N N, which gives ( 7.7). Thus we may assume that p j + 1 p_{j+1}, in particular, is less than N 1 / 2 N^{1/2}, which forces

 | N 1 / 2 < p 1 ​ … ​ p j ⩽ N N^{1/2}<p_{1}\ldots p_{j}\leqslant N |  | (7.8) |

and p j < N 1 / 2 p_{j}<N^{1/2}.

Following [19], we eliminate some small exceptional sets of natural numbers n n. First we consider those n n for which P ⁡ ( n) P(n) has at least ( log ⁡ log ⁡ N) 2 (\log\log N)^{2} distinct prime factors. For such P ⁡ ( n) P(n), one has τ ⁡ ( P ⁡ ( n)) ⩾ 2 ( log ⁡ log ⁡ N) 2 \tau(P(n))\geqslant 2^{(\log\log N)^{2}}, which is asymptotically larger than any given power of log ⁡ N \log N; thus by ( 7.5), the set of such n n has size at most O ⁡ ( N ​ log − C ′ ​ N) O(N\log^{-C^{\prime}}N) and can be discarded.

Next, we consider those n n for which P ⁡ ( n) P(n) is divisible by a prime power p k p^{k} with p ⩽ N 1 / 2 p\leqslant N^{1/2}, k > 1 k>1, and p k ⩾ N 1 / 8 ​ ( log ⁡ log ⁡ N) 2 p^{k}\geqslant N^{1/8(\log\log N)^{2}}. By reducing k k if necessary we may assume that p k ⩽ N p^{k}\leqslant N. For each p p and k k, there are at most O ⁡ ( ( N / p k) ​ ρ ​ ( p k)) = O ⁡ ( N / p k) O(({N}/{p^{k}})\rho(p^{k}))=O({N}/{p^{k}}) numbers n n with P ⁡ ( n) P(n) divisible by p k p^{k}, thanks to ( 7.2); thus the total number of such n n is bounded by

 | ≪ N ∑ p ⩽ N 1 / 2 ∑ j ⩾ 2: p j ⩾ N 1 / 8 ​ ( log ⁡ log ⁡ N) 2 1 p j \ll N\sum_{p\leqslant N^{1/2}}\sum_{j\geqslant 2:p^{j}\geqslant N^{1/8(\log\log N)^{2}}}\frac{1}{p^{j}} |  |

which can easily be computed to be O ⁡ ( N ​ log − C ′ ​ N) O(N\log^{-C^{\prime}}N). Thus we may discard all n n of this type.

After removing all such n n, we must have p j > N 1 / 8 ​ ( log ⁡ log ⁡ N) 2 p_{j}>N^{1/8(\log\log N)^{2}}. Indeed, after eliminating the exceptional n n as above, p 1 ​ … ​ p j p_{1}\ldots p_{j} is the product of at most ( log ⁡ log ⁡ N) 2 (\log\log N)^{2} prime powers, each of which is bounded by N 1 / 8 ​ ( log ⁡ log ⁡ N) 2 N^{1/8(\log\log N)^{2}}, or is a single prime larger than N 1 / 8 ​ ( log ⁡ log ⁡ N) 2 N^{1/8(\log\log N)^{2}}. The former possibility thus contributes at most N 1 / 8 N^{1/8} to the final product p 1 ​ … ​ p j p_{1}\ldots p_{j}; from ( 7.8) we conclude that the latter possibility must occur at least once, and the claim follows.

Let r r be the positive integer such that

 | N 1 / ( r + 1) < p j ⩽ N 1 / r, N^{1/(r+1)}<p_{j}\leqslant N^{1/r}, |  |

then 2 ⩽ r ≪ ( log ⁡ log ⁡ N) 2 2\leqslant r\ll(\log\log N)^{2}. The primes p j + 1, …, p J p_{j+1},\ldots,p_{J} have size at least N 1 / ( r + 1) N^{1/(r+1)}, so by ( 7.6) we have J = j + O ⁡ ( r) J=j+O(r), which implies that

 | τ ⁡ ( P ⁡ ( n)) ≪ O ​ ( 1) r ​ τ ​ ( p 1 ​ … ​ p j). \tau(P(n))\ll O(1)^{r}\tau(p_{1}\ldots p_{j}). |  |

As p 1 ​ … ​ p j p_{1}\ldots p_{j} is at least N 1 / 2 N^{1/2}, we have

 | τ ⁡ ( p 1 ​ … ​ p j) ⩽ 2 ​ ∑ m | p 1 ​ … ​ p j; m ⩾ ( p 1 ​ … ​ p j) 1 / 2 1 ⩽ 2 ​ ∑ m | p 1 ​ … ​ p j; m ⩾ N 1 / 4 1. \tau(p_{1}\ldots p_{j})\leqslant 2\sum_{m\mid p_{1}\ldots p_{j};m\geqslant(p_{1}\ldots p_{j})^{1/2}}1\leqslant 2\sum_{m\mid p_{1}\ldots p_{j};m\geqslant N^{1/4}}1. |  |

Note that all m m in the above summand lie in S r S_{r} and divide P ⁡ ( n) P(n). The claim follows. ∎

Invoking the above lemma, it remains to bound

 |  | ∑ m ⩽ N ∑ n ⩽ N: m | P ⁡ ( n) 1 + ∑ r = 2 O ⁡ ( ( log ⁡ log ⁡ N) 2) O ( 1) r ∑ m ∈ S r ∑ n ⩽ N: m | P ⁡ ( n) 1. \displaystyle\sum_{m\leqslant N}\sum_{n\leqslant N:m\mid P(n)}1\quad+\sum_{r=2}^{O((\log\log N)^{2})}O(1)^{r}\sum_{m\in S_{r}}\sum_{n\leqslant N:m\mid P(n)}1. |  |

by O ⁡ ( N ​ ∑ n ⩽ N P ⁡ ( m) / m) O(N\sum_{n\leqslant N}{P(m)}/{m}). The first term was already shown to be acceptable by ( 7.4). For the second sum, we also apply ( 7.4) and bound it by

 | ≪ N ​ ∑ r = 2 O ⁡ ( ( log ⁡ log ⁡ N) 2) O ​ ( 1) r ​ ∑ m ∈ S r ρ ⁡ ( m) m. \ll N\sum_{r=2}^{O((\log\log N)^{2})}O(1)^{r}\sum_{m\in S_{r}}\frac{\rho(m)}{m}. |  | (7.9) |

To estimate this expression, let r, m r,m be as in the above summation, and factor m m into primes. As in the proof of Lemma 7.3, the contribution to m m coming from primes less than N 1 / 8 ​ ( log ⁡ log ⁡ N) 2 N^{1/8(\log\log N)^{2}} is at most N 1 / 8 N^{1/8}, and the primes larger than N 1 / 8 ​ ( log ⁡ log ⁡ N) 2 N^{1/8(\log\log N)^{2}} that divide m m are distinct. Hence, by the pigeonhole principle (as in [19]), there exists t ⩾ 1 t\geqslant 1 with r ​ 2 t ≪ ( log ⁡ log ⁡ N) 2 r2^{t}\ll(\log\log N)^{2} such that the N 1 / r N^{1/r} -smooth number m m has at least ⌊ r ​ t / 100 ⌋ \lfloor{rt}/{100}\rfloor distinct prime factors between N 1 / 2 t + 1 ​ r N^{1/2^{t+1}r} and N 1 / 2 t ​ r N^{1/2^{t}r}, and can thus be factored as m = q 1 ​ … ​ q ⌊ r ​ t / 100 ⌋ ​ u m=q_{1}\ldots q_{\lfloor{rt}/{100}\rfloor}u where q 1 < … < q ⌊ r ​ t / 100 ⌋ q_{1}<\ldots<q_{\lfloor{rt}/{100}\rfloor} are primes between N 1 / 2 t + 1 ​ r N^{1/2^{t+1}r} and N 1 / 2 t ​ r N^{1/2^{t}r}, and u u is an integer of size at most N N. From the Chinese remainder theorem and ( 7.2) we have the crude bound

 | ρ ⁡ ( m) ≪ O ​ ( 1) r ​ t ​ ρ ​ ( u) \rho(m)\ll O(1)^{rt}\rho(u) |  |

and thus

 | ∑ m ∈ S r ρ ⁡ ( m) m ≪ ∑ t = 1 ∞ O ​ ( 1) r ​ t ​ 1 ⌊ r ​ t 100 ⌋! ​ ( ∑ N 1 / 2 t + 1 ​ r ⩽ p ⩽ N 1 / 2 t ​ r 1 p) ⌊ r ​ t / 100 ⌋ ​ ∑ u ⩽ N ρ ⁡ ( u) u. \sum_{m\in S_{r}}\frac{\rho(m)}{m}\ll\sum_{t=1}^{\infty}O(1)^{rt}\frac{1}{\lfloor\frac{rt}{100}\rfloor!}\left(\sum_{N^{1/2^{t+1}r}\leqslant p\leqslant N^{1/2^{t}r}}\frac{1}{p}\right)^{\lfloor{rt}/{100}\rfloor}\sum_{u\leqslant N}\frac{\rho(u)}{u}. |  |

By the standard asymptotic ∑ p < x 1 / p = log ⁡ log ⁡ x + O ⁡ ( 1) \sum_{p<x}{1}/{p}=\log\log x+O(1), we have

 | ∑ N 1 / 2 t + 1 ​ r ⩽ p ⩽ N 1 / 2 t ​ r 1 p = O ⁡ ( 1); \sum_{N^{1/2^{t+1}r}\leqslant p\leqslant N^{1/2^{t}r}}\frac{1}{p}=O(1); |  |

putting this all together, we can bound ( 7.9) by

 | ≪ ( ∑ r = 2 ∞ ∑ t = 1 ∞ O ​ ( 1) r ​ t ⌊ r ​ t 100 ⌋!) ​ ∑ m ⩽ N ρ ⁡ ( m) m \ll\left(\sum_{r=2}^{\infty}\sum_{t=1}^{\infty}\frac{O(1)^{rt}}{\lfloor\frac{rt}{100}\rfloor!}\right)\sum_{m\leqslant N}\frac{\rho(m)}{m} |  |

and the claim follows. ∎

We isolate a simple special case of Theorem 7.1, when the polynomial P P is linear:

###### Corollary 7.4.

If a, b, N a,b,N are natural numbers with a, b ≪ N O ⁡ ( 1) a,b\ll N^{O(1)}, then

 | ∑ n ⩽ N τ ⁡ ( a ​ n + b) ≪ τ ⁡ ( ( a, b)) ​ N ​ log ⁡ N \sum_{n\leqslant N}\tau(an+b)\ll\tau((a,b))N\log N |  |

where ( a, b) (a,b) is the greatest common divisor of a a and b b.

###### Proof.

By the elementary inequality τ ⁡ ( n ​ m) ⩽ τ ⁡ ( n) ​ τ ​ ( m) \tau(nm)\leqslant\tau(n)\tau(m) we may factor out ( a, b) (a,b) and assume without loss of generality that a, b a,b are coprime.

We apply Theorem 7.1 with P ⁡ ( n):= a ​ n + b P(n):=an+b. From the coprimality of a, b a,b and elementary modular arithmetic, we see that ρ ⁡ ( m) ⩽ 1 \rho(m)\leqslant 1 for all m m, and the claim follows. ∎

We may now prove Proposition 1.4 from the introduction.

###### Proof of Proposition 1.4.

We divide into two cases, depending on whether A ⩾ B A\geqslant B or A ⩽ B A\leqslant B.

First suppose that A ⩾ B A\geqslant B. From Corollary 7.4 we have

 | ∑ a ⩽ A τ ⁡ ( k ​ a ​ b 2 + 1) ≪ A ​ ∑ m ⩽ A 1 m ≪ A ​ log ⁡ A, \sum_{a\leqslant A}\tau(kab^{2}+1)\ll A\sum_{m\leqslant A}\frac{1}{m}\ll A\log A, |  |

for each fixed b ⩽ B b\leqslant B, and the claim follows on summing in B B. (Note that this argument in fact works whenever A ⩾ B ε A\geqslant B^{\varepsilon} for any fixed ε > 0 \varepsilon>0.)

Now suppose that A ⩽ B A\leqslant B. For each fixed a ∈ A a\in A, we apply Theorem 7.1 to the polynomial P k ​ a ​ ( b):= k ​ a ​ b 2 + 1 P_{ka}(b):=kab^{2}+1. To do this we first must obtain a bound on ρ k ​ a ​ ( p j) \rho_{ka}(p^{j}), where ρ k ​ a ​ ( m) \rho_{ka}(m) is the number of solutions b mod m b\mod m to k ​ a ​ b 2 + 1 = 0 mod m kab^{2}+1=0\mod m. Clearly ρ k ​ a ​ ( m) \rho_{ka}(m) vanishes whenever m m is not coprime to k ​ a ka, so it suffices to consider ρ k ​ a ​ ( p j) \rho_{ka}(p^{j}) when p p does not divide k ​ a ka. Then P k ​ a P_{ka} is quadratic, and a simple application of Hensel’s lemma reveals that ρ k ​ a ​ ( p j) ⩽ 2 \rho_{ka}(p^{j})\leqslant 2 for all odd prime powers p j p^{j} and ρ k ​ a ​ ( p j) ⩽ 4 \rho_{ka}(p^{j})\leqslant 4 for p = 2 p=2. We may therefore apply Theorem 7.1 and conclude that

 | ∑ b ⩽ B τ ⁡ ( k ​ a ​ b 2 + 1) ≪ B ​ ∑ m ⩽ B ρ k ​ a ​ ( m) m. \sum_{b\leqslant B}\tau(kab^{2}+1)\ll B\sum_{m\leqslant B}\frac{\rho_{ka}(m)}{m}. |  |

It thus suffices to show that

 | ∑ a ⩽ A ∑ m ⩽ B ρ k ​ a ​ ( m) m ≪ A ​ log ⁡ B ​ log ⁡ ( 1 + k). \sum_{a\leqslant A}\sum_{m\leqslant B}\frac{\rho_{ka}(m)}{m}\ll A\log B\log(1+k). |  | (7.10) |

To control ρ k ​ a ​ ( m) \rho_{ka}(m), the obvious tool to use here is the quadratic reciprocity law ( A.7). To apply this law, it is of course convenient to first reduce to the case when a a and m m are odd. If m = 2 j ​ m ′ m=2^{j}m^{\prime} for some odd m ′ m^{\prime}, then ρ k ​ a ​ ( m) ≪ ρ k ​ a ​ ( m ′) \rho_{ka}(m)\ll\rho_{ka}(m^{\prime}), and from this it is easy to see that the bound ( 7.10) follows from the same bound with m m restricted to be odd. Similarly, by splitting a = 2 l ​ a ′ a=2^{l}a^{\prime} and absorbing the 2 l 2^{l} factor into k k (and dividing A A by 2 l 2^{l} to compensate), we may assume without loss of generality that a a is odd.

As previously observed, ρ k ​ a ​ ( m) \rho_{ka}(m) vanishes unless k ​ a ka and m m are coprime, so we may also restrict to the case ( k ​ a, m) = 1 (ka,m)=1, where ( n, m) (n,m) denotes the greatest common divisor of n, m n,m. If p p is an odd prime not dividing k ​ a ka, then from elementary manipulation and Hensel’s lemma we see that

 | ρ k ​ a ​ ( p j) = ρ k ​ a ​ ( p) ⩽ 1 + ( − k ​ a p), \rho_{ka}(p^{j})=\rho_{ka}(p)\leqslant 1+\left(\frac{-ka}{p}\right), |  |

and thus for odd m m coprime to k ​ a ka we have

 | ρ k ​ a ​ ( m) ⩽ ∏ p | m ( 1 + ( − k ​ a p)). \rho_{ka}(m)\leqslant\prod_{p\mid m}\left(1+\left(\frac{-ka}{p}\right)\right). |  |

For odd m m, not necessarily coprime to k ​ a ka, we thus have

 | ρ k ​ a ​ ( m) ⩽ ∏ p | m; ( p, 2 ​ k ​ a) = 1 ( 1 + ( − k ​ a p)). \rho_{ka}(m)\leqslant\prod_{p\mid m;(p,2ka)=1}\left(1+\left(\frac{-ka}{p}\right)\right). |  |

using the multiplicativity properties of the Jacobi symbol, one has

 | 1 + ( − k ​ a p) ⩽ ∑ j: p j | m ( − k ​ a p j) 1+\left(\frac{-ka}{p}\right)\leqslant\sum_{j:p^{j}\mid m}\left(\frac{-ka}{p^{j}}\right) |  |

whenever p | m p\mid m and ( p, 2 ​ k ​ a) = 1 (p,2ka)=1, and thus

 | ρ k ​ a ( m) ⩽ ∏ p | m; ( p, 2 ​ k ​ a) = 1 ∑ j: p j | m ( − k ​ a p j). \rho_{ka}(m)\leqslant\prod_{p\mid m;(p,2ka)=1}\sum_{j:p^{j}\mid m}\left(\frac{-ka}{p^{j}}\right). |  |

The right-hand side can be expanded as

 | ∑ q | m; ( q, 2 ​ k ​ a) = 1 ( − k ​ a q). \sum_{q\mid m;(q,2ka)=1}\left(\frac{-ka}{q}\right). |  |

We can thus bound the left-hand side of ( 7.10) by

 | ∑ q ⩽ B: ( q, 2 ​ k) = 1 ∑ a ⩽ A; ( a, 2 ​ q) = 1 ( − k ​ a q) ∑ m ⩽ B; q | m 1 m. \sum_{q\leqslant B:(q,2k)=1}\sum_{a\leqslant A;(a,2q)=1}\left(\frac{-ka}{q}\right)\sum_{m\leqslant B;q\mid m}\frac{1}{m}. |  |

The final sum is of course ( log ⁡ B q) / q + O ⁡ ( 1 / q) ({\log\frac{B}{q}})/{q}+O({1}/{q}). The contribution of the error term is bounded by

 | O ⁡ ( ∑ q ⩽ B ∑ a ⩽ A 1 q) = O ⁡ ( A ​ log ⁡ B) O(\sum_{q\leqslant B}\sum_{a\leqslant A}\frac{1}{q})=O(A\log B) |  |

which is acceptable, so it suffices to show that

 | | ∑ q ⩽ B: ( q, 2 ​ k) = 1 ∑ a ⩽ A; ( a, 2 ​ q) = 1 ( − k ​ a q) log ⁡ B q q | ≪ A log B log ( 1 + k). \left|\sum_{q\leqslant B:(q,2k)=1}\sum_{a\leqslant A;(a,2q)=1}\left(\frac{-ka}{q}\right)\frac{\log\frac{B}{q}}{q}\right|\ll A\log B\log(1+k). |  | (7.11) |

We first dispose of an easy contribution, when q q is less than A A. The expression

 | a ↦ ( − k ​ a q) ​ 1 ( a, 2 ​ q) = 1 a\mapsto\left(\frac{-ka}{q}\right)1_{(a,2q)=1} |  |

is periodic with period 2 ​ q 2q and sums to zero (being essentially a quadratic character on ℤ / 2 ​ q ​ ℤ \mathbb{Z}/2q\mathbb{Z}), and so in this case we have

 | ∑ a ⩽ A; ( a, 2 ​ q) = 1 ( − k ​ a q) = O ⁡ ( q). \sum_{a\leqslant A;(a,2q)=1}\left(\frac{-ka}{q}\right)=O(q). |  |

One could obtain better estimates and deal with somewhat larger q q here by using tools such as the Pólya-Vinogradov inequality, but we will not need to do so here; similarly for the treatment of the regime A ⩽ q ⩽ k ​ A A\leqslant q\leqslant kA below. In any event, the contribution of the q < A q<A case is bounded by

 | O ⁡ ( ∑ q ⩽ A q ​ log ⁡ B q q) = O ⁡ ( A ​ log ⁡ B) O\left(\sum_{q\leqslant A}q\frac{\log\frac{B}{q}}{q}\right)=O(A\log B) |  |

which is acceptable.

Next, we deal with the contribution when q q is between A A and k ​ A kA. Here we crudely bound the Jacobi symbol in magnitude by 1 1 and obtain a bound of

 | O ⁡ ( ∑ A ⩽ q ⩽ k ​ A ∑ a ⩽ A log ⁡ B q) = O ⁡ ( A ​ log ⁡ B ​ log ⁡ ( 1 + k)) O(\sum_{A\leqslant q\leqslant kA}\sum_{a\leqslant A}\frac{\log B}{q})=O(A\log B\log(1+k)) |  |

which is acceptable.

Finally, we deal with the case when q q exceeds k ​ A kA. We write k = 2 m ​ k ′ k=2^{m}k^{\prime} where k ′ k^{\prime} is odd, then from quadratic reciprocity ( A.7) (and ( A.8), ( A.9)) we have

 | ( − k ​ a q) = c ​ ( q) ​ ( q k ′ ​ a) \left(\frac{-ka}{q}\right)=c(q)\left(\frac{q}{k^{\prime}a}\right) |  |

where c ⁡ ( q):= ( − 1) ( q − 1) / 2 + m ⁡ ( q 2 − 1) / 8 c(q):=(-1)^{(q-1)/2+m(q^{2}-1)/8} is periodic with period 8 8. We can thus rewrite this contribution to ( 7.11) as

 | | ∑ a ⩽ A; ( a, 2) = 1 ∑ k ​ A ⩽ q ⩽ B: ( q, 2 ​ a ​ k) = 1 c ( q) ( q k ′ ​ a) log ⁡ B q q |. \left|\sum_{a\leqslant A;(a,2)=1}\sum_{kA\leqslant q\leqslant B:(q,2ak)=1}c(q)\left(\frac{q}{k^{\prime}a}\right)\frac{\log\frac{B}{q}}{q}\right|. |  |

For any fixed a a in the above sum, the expression

 | q ↦ c ⁡ ( q) ​ ( q k ′ ​ a) ​ 1 ( q, 2 ​ a ​ k) = 1 q\mapsto c(q)\left(\frac{q}{k^{\prime}a}\right)1_{(q,2ak)=1} |  |

is periodic with period 8 ​ k ′ ​ a = O ⁡ ( k ​ A) 8k^{\prime}a=O(kA), is bounded in magnitude by 1 1 and has mean zero. A summation by parts then gives

 | | ∑ k ​ A ⩽ q ⩽ B: ( q, 2 ​ a ​ k) = 1 c ( q) ( q k ′ ​ a) log ⁡ B q q | ≪ log B \left|\sum_{kA\leqslant q\leqslant B:(q,2ak)=1}c(q)\left(\frac{q}{k^{\prime}a}\right)\frac{\log\frac{B}{q}}{q}\right|\ll\log B |  |

and so on summing in A A we see that this contribution is acceptable. This concludes the proof of the proposition. ∎

We now record some variants of Proposition 1.4 that will also be useful in our applications.

###### Proposition 7.5 (Average value of τ 3 ​ ( a ​ b + 1) \tau_{3}(ab+1)).

For any A, B > 1 A,B>1, one has

 | ∑ a ⩽ A ∑ b ⩽ B τ 3 ​ ( a ​ b + 1) ≪ A ​ B ​ log 2 ⁡ ( A + B). \sum_{a\leqslant A}\sum_{b\leqslant B}\tau_{3}(ab+1)\ll AB\log^{2}(A+B). |  | (7.12) |

###### Proof.

By symmetry we may assume that A ⩽ B A\leqslant B, so that a ​ b ≪ B 2 ab\ll B^{2} for all a ⩽ A a\leqslant A and b ⩽ B b\leqslant B. For any n n, τ 3 \tau_{3} is the number of ways to represent n n as the product n = d 1 ​ d 2 ​ d 3 n=d_{1}d_{2}d_{3} of three terms. One of these terms must be at most n 1 / 3 n^{1/3}, and so

 | τ 3 ( n) ≪ ∑ d | n: d ⩽ n 1 / 3 τ ( n d). \tau_{3}(n)\ll\sum_{d\mid n:d\leqslant n^{1/3}}\tau(\frac{n}{d}). |  |

We can thus bound the left-hand side of ( 7.12) by

 | ≪ ∑ d ≪ B 2 / 3 ∑ a ⩽ A ∑ b ⩽ B: d | a ​ b + 1 τ ( a ​ b + 1 d). \ll\sum_{d\ll B^{2/3}}\sum_{a\leqslant A}\sum_{b\leqslant B:d\mid ab+1}\tau(\frac{ab+1}{d}). |  |

Note that for fixed a, d a,d, the constraint d | a ​ b + 1 d\mid ab+1 is only possible if a a is coprime to d d, and restricts b b to some primitive residue class q mod d q\mod d for some q = q a, d q=q_{a,d} between 1 1 and d d. Writing b = c ​ d + q b=cd+q, we can thus bound the above expression by

 | ≪ ∑ d ≪ B 2 / 3 ∑ a ⩽ A ∑ c ≪ B / d τ ⁡ ( a ​ c + r) \ll\sum_{d\ll B^{2/3}}\sum_{a\leqslant A}\sum_{c\ll B/d}\tau(ac+r) |  |

where r = r a, d:= ( a ​ q + 1) / d r=r_{a,d}:=({aq+1})/{d}. Note that r r is clearly coprime to a a. Thus by Corollary 7.4, we may bound the preceding expression by

 | ≪ ∑ d ≪ B 2 / 3 ∑ a ⩽ A B d ​ log ⁡ B \ll\sum_{d\ll B^{2/3}}\sum_{a\leqslant A}\frac{B}{d}\log B |  |

which is O ⁡ ( A ​ B ​ log 2 ⁡ B) O(AB\log^{2}B). The claim follows. ∎

###### Proposition 7.6 (Average value of τ ⁡ ( a ​ b + c ​ d) \tau(ab+cd)).

For any A, B, C, D > 1 A,B,C,D>1, one has

 | ∑ a ⩽ A, b ⩽ B, c ⩽ C, d ⩽ D: ( a, b, c, d) = 1 τ ( a b + c d) ≪ A B C D log ( A + B + C + D). \sum_{\begin{subarray}{c}a\leqslant A,b\leqslant B,c\leqslant C,d\leqslant D:\\ (a,b,c,d)=1\end{subarray}}\tau(ab+cd)\ll ABCD\log(A+B+C+D). |  | (7.13) |

###### Proof.

By symmetry we may assume that A, B, C ⩽ D A,B,C\leqslant D. Then for fixed a, b, c a,b,c coprime, we have

 | ∑ d ⩽ D τ ⁡ ( a ​ b + c ​ d) ≪ D ​ log ⁡ D \sum_{d\leqslant D}\tau(ab+cd)\ll D\log D |  |

by Corollary 7.4, and the claim follows by summing in a, b, c, d a,b,c,d. ∎

###### Remark 7.7.

Informally, one can view the above propositions as asserting that the heuristics τ ⁡ ( n) ≪ log ⁡ n \tau(n)\ll\log n, τ 3 ​ ( n) ≪ log 2 ⁡ n \tau_{3}(n)\ll\log^{2}n are valid on average (in a first moment sense) on the range of various polynomial forms in several variables. A result similar to Proposition 7.6 was established in [28, Lemma 3], but with the coprimality condition ( a, b, c, d) = 1 (a,b,c,d)=1 replaced by ( a ​ b, c ​ d) = 1 (ab,cd)=1, and also the divisor function τ \tau being restricted by forcing one of the divisors to live in a given dyadic range, with the logarithm being removed as a consequence. Also, products of three factors were permitted instead of the terms a ​ b, c ​ d ab,cd. As remarked after [28, Lemma 4], the logarithmic term in ( 7.13) is necessary.

## 8. Upper bound for ∑ n ⩽ N f I ​ ( n) \sum_{n\leqslant N}f_{\operatorname{I}}(n) and ∑ p ⩽ N f I ​ ( p) \sum_{p\leqslant N}f_{\operatorname{I}}(p)

Now that we have established Proposition 1.4, we can obtain upper bounds on sums of f I f_{\operatorname{I}}.

We begin with the bound

 | ∑ n ⩽ N f I ​ ( n) ≪ N ​ log 3 ​ N. \sum_{n\leqslant N}f_{\operatorname{I}}(n)\ll N\log^{3}N. |  |

By Proposition 2.2 and symmetry followed by Lemma 2.8, it suffices to show that there are at most O ⁡ ( N ​ log 3 ​ N) O(N\log^{3}N) septuples ( a, b, c, d, e, f, n) ∈ ℕ 7 (a,b,c,d,e,f,n)\in\mathbb{N}^{7} obeying ( 2.1)-( 2.9) and the Type I estimates from Lemma 2.8. In particular, a ​ c ​ d ≪ N acd\ll N, f f is a factor of 4 ​ a 2 ​ d + 1 4a^{2}d+1, and n = 4 ​ a ​ c ​ d − f n=4acd-f. As a, c, d, f a,c,d,f determine the remaining components of the septuple, we may thus bound the number of such septuples as

 | ∑ a, c, d: a ​ c ​ d ≪ N τ ( 4 a 2 d + 1). \sum_{a,c,d:acd\ll N}\tau(4a^{2}d+1). |  |

Dividing a, c, d a,c,d into dyadic blocks ( A / 2 ⩽ a ⩽ A A/2\leqslant a\leqslant A, etc.) and applying Proposition 1.4 (with k = 4 k=4) to each block, we obtain the desired bound O ⁡ ( N ​ log 3 ​ N) O(N\log^{3}N).

Now we establish the bound

 | ∑ p ⩽ N f I ​ ( p) ≪ N ​ log 2 ​ N ​ log ⁡ log ⁡ N. \sum_{p\leqslant N}f_{\operatorname{I}}(p)\ll N\log^{2}N\log\log N. |  |

As before, it suffices to count quadruples ( a, c, d, f) (a,c,d,f) with a ​ c ​ d ≪ N acd\ll N, and f f a factor of 4 ​ a 2 ​ d + 1 4a^{2}d+1; but now we can restrict p = 4 ​ a ​ c ​ d − f p=4acd-f to be prime. Also, from Proposition 2.2 we may assume that p p is coprime to a ​ c ​ d acd (and hence to 4 ​ a ​ c ​ d 4acd, if we discard the prime p = 2 p=2).

Thus we may assume without loss of generality that − f mod 4 ​ a ​ d -f\mod 4ad is a primitive residue class. From the Brun-Titchmarsh inequality ( A.10), we conclude that for each fixed a, d, f a,d,f, there are O ⁡ ( N / ( ϕ ⁡ ( 4 ​ a ​ d) ​ log ⁡ ( N / 4 ​ a ​ d))) O({N}/({\phi(4ad)\log(N/4ad)})) primes p p in this residue class that are less than N N if a ​ d ⩽ N / 100 ad\leqslant N/100 (say); if instead a ​ d > N / 100 ad>N/100, then we of course only have O ⁡ ( 1) = O ⁡ ( N / ϕ ⁡ ( 4 ​ a ​ d)) O(1)=O({N}/{\phi(4ad)}) primes in this class. Thus, in any event, we can bound the number of such primes as O ⁡ ( N / ( ϕ ⁡ ( 4 ​ a ​ d) ​ log ⁡ ( 2 + N / a ​ d))) O({N}/({\phi(4ad)\log(2+N/ad)})). We therefore have the bound

 | ∑ p ⩽ N f I ( p) ≪ ∑ a, d: a ​ d ≪ N τ ( 4 a 2 d + 1) N ϕ ⁡ ( 4 ​ a ​ d) ​ log ⁡ ( 2 + N / a ​ d). \sum_{p\leqslant N}f_{\operatorname{I}}(p)\ll\sum_{a,d:ad\ll N}\tau(4a^{2}d+1)\frac{N}{\phi(4ad)\log(2+N/ad)}. |  | (8.1) |

By dyadic decomposition (and bounding ϕ ⁡ ( 4 ​ a ​ d) ⩾ ϕ ⁡ ( a ​ d) \phi(4ad)\geqslant\phi(ad)), it thus suffices to show that

 | ∑ a, d: N / 2 ⩽ a ​ d ⩽ N τ ⁡ ( 4 ​ a 2 ​ d + 1) ϕ ⁡ ( a ​ d) ≪ log 2 N. \sum_{a,d:N/2\leqslant ad\leqslant N}\frac{\tau(4a^{2}d+1)}{\phi(ad)}\ll\log^{2}N. |  | (8.2) |

Indeed, assuming this bound for all N N, we can bound the right-hand side of ( 8.1) by

 | ∑ j = 1 O ⁡ ( log ⁡ N) N ​ log 2 ​ N j ≪ N ​ log 2 ​ N ​ log ⁡ log ⁡ N \sum_{j=1}^{O(\log N)}\frac{N\log^{2}N}{j}\ll N\log^{2}N\log\log N |  |

and the claim follows.

To prove ( 8.2), we would like to again apply Proposition 1.4, but we must first deal with the ϕ ⁡ ( a ​ d) \phi(ad) denominator. From ( A.12) one has

 | 1 ϕ ⁡ ( a ​ d) ≪ 1 a ​ d ​ ∑ s | a ∑ t | d 1 s ​ t. \frac{1}{\phi(ad)}\ll\frac{1}{ad}\sum_{s\mid a}\sum_{t\mid d}\frac{1}{st}. |  |

Writing a = s ​ a ′ a=sa^{\prime}, d = t ​ d ′ d=td^{\prime}, we may thus bound the left-hand side of ( 8.2) by

 | ≪ 1 N ∑ s, t: s ​ t ⩽ N 1 s ​ t ∑ a ′, d ′: a ′ ​ d ′ ⩽ N / s ​ t τ ( 4 s 2 t ( a ′) 2 d ′ + 1). \ll\frac{1}{N}\sum_{s,t:st\leqslant N}\frac{1}{st}\sum_{a^{\prime},d^{\prime}:a^{\prime}d^{\prime}\leqslant N/st}\tau(4s^{2}t(a^{\prime})^{2}d^{\prime}+1). |  |

Applying Proposition 1.4 to the inner sum (decomposed into dyadic blocks, and setting k = 4 ​ s 2 ​ t k=4s^{2}t), we see that

 | ∑ a ′, d ′: a ′ ​ d ′ ⩽ N / s ​ t τ ( 4 s 2 t ( a ′) 2 d ′ + 1) ≪ N s ​ t log 2 N s ​ t log ( 1 + s 2 t). \sum_{a^{\prime},d^{\prime}:a^{\prime}d^{\prime}\leqslant N/st}\tau(4s^{2}t(a^{\prime})^{2}d^{\prime}+1)\ll\frac{N}{st}\log^{2}\frac{N}{st}\log(1+s^{2}t). |  |

Inserting this bound and summing in s, t s,t we obtain the claim.

## 9. Upper bound for ∑ n ⩽ N f II ​ ( n) \sum_{n\leqslant N}f_{\operatorname{II}}(n) and ∑ p ⩽ N f II ​ ( p) \sum_{p\leqslant N}f_{\operatorname{II}}(p)

Now we prove the upper bound

 | ∑ n ⩽ N f II ​ ( n) ≪ N ​ log 3 ​ N. \sum_{n\leqslant N}f_{\operatorname{II}}(n)\ll N\log^{3}N. |  |

By Proposition 2.6 followed by Lemma 2.8 (and symmetry), it suffices to show that there are at most O ⁡ ( N ​ log 3 ​ N) O(N\log^{3}N) ℕ \mathbb{N} -points ( a, b, c, d, e, f) (a,b,c,d,e,f) that lie in Σ n II \Sigma_{n}^{\operatorname{II}} for some n ⩽ N n\leqslant N, which also obeys the Type II bound a ​ c ​ d ​ e ⩽ N acde\leqslant N in Lemma 2.8.

Observe from ( 2.13)-( 2.21) that a, c, d, e a,c,d,e determine the other variables b, f, n b,f,n. Thus, it suffices to show that there are O ⁡ ( N ​ log 3 ​ N) O(N\log^{3}N) quadruples ( a, b, d, e) ∈ ℕ 4 (a,b,d,e)\in\mathbb{N}^{4} with a ​ c ​ d ​ e ⩽ N acde\leqslant N. But this follows from ( A.2) with k = 4 k=4.

Finally, we prove the upper bound

 | ∑ p ⩽ N f II ​ ( p) ≪ N ​ log 2 ​ N. \sum_{p\leqslant N}f_{\operatorname{II}}(p)\ll N\log^{2}N. |  |

By dyadic decomposition, it suffices to show that

 | ∑ N / 2 ⩽ p ⩽ N f II ​ ( p) ≪ N ​ log 2 ​ N. \sum_{N/2\leqslant p\leqslant N}f_{\operatorname{II}}(p)\ll N\log^{2}N. |  | (9.1) |

As before, we can bound the left-hand side (up to constants) by the number of quadruples ( a, c, d, e) ∈ ℕ 4 (a,c,d,e)\in\mathbb{N}^{4} with a ​ c ​ d ​ e ≪ N acde\ll N. However, by ( 2.16), we may also add the restriction that 4 ​ a ​ c ​ d ​ e − 4 ​ a 2 ​ d − e 4acde-4a^{2}d-e is a prime between N / 2 N/2 and N N. Also, if we set b:= c ​ e − a b:=ce-a, then by Lemma 2.8 we may also add the restrictions a ⩽ b a\leqslant b and b < c ​ e b<ce, and from Proposition 2.6 we can also require that a, b a,b be coprime. Since

 | ( a ​ d ​ e) ​ ( a ​ c ​ d) ​ ( a ​ b) 1 / 2 \displaystyle(ade)(acd)(ab)^{1/2} | ≪ ( a ​ d ​ e) ​ ( a ​ c ​ d) ​ b \displaystyle\ll(ade)(acd)b |  |

 |  | ≪ ( a ​ d ​ e) ​ ( a ​ c ​ d) ​ ( c ​ e) \displaystyle\ll(ade)(acd)(ce) |  |

 |  | = ( a ​ c ​ d ​ e) 2 \displaystyle=(acde)^{2} |  |

 |  | ≪ N 2 \displaystyle\ll N^{2} |  |

we see that one of the quantities a ​ d ​ e, a ​ c ​ d, a ​ b ade,acd,ab must be at most O ⁡ ( N 4 / 5) O(N^{4/5}) (cf. Section 3). As we shall soon see, the ability to take one of these quantities to be significantly less than N N allows us to avoid the inefficiencies in the Brun-Titchmarsh inequality ( A.10) that led to a double logarithmic loss in the Type I case. (Unfortunately, it does not seem that a similar trick is available in the Type II case.)

Let us first consider those quadruples with a ​ d ​ e ≪ N 4 / 5 ade\ll N^{4/5}, which is the easiest case. For fixed a, d, e a,d,e, 4 ​ a ​ c ​ d ​ e − 4 ​ a 2 ​ d − e 4acde-4a^{2}d-e traverses (a possibly non-primitive) residue class modulo 4 ​ a ​ d ​ e 4ade. As a ​ d ​ e ≪ N 4 / 5 ade\ll N^{4/5}, there are no primes in this class that are at least N / 2 N/2 if the class is not primitive. If it is primitive, we may apply the Brun-Titchmarsh inequality ( A.10) to bound the number of primes between N / 2 N/2 and N N in this class by O ⁡ ( N ϕ ⁡ ( 4 ​ a ​ d ​ e) ​ log ⁡ ( N)) O(\frac{N}{\phi(4ade)\log(N)}), noting that log ⁡ ( N / 4 ​ a ​ d ​ e) \log(N/4ade) is comparable to log ⁡ N \log N. Thus, we can bound this contribution to the left-hand side of ( 9.1) by

 | ≪ N log ⁡ N ∑ a, d, e: a ​ d ​ e ≪ N 4 / 5 1 ϕ ⁡ ( 4 ​ a ​ c ​ d); \ll\frac{N}{\log N}\sum_{a,d,e:ade\ll N^{4/5}}\frac{1}{\phi(4acd)}; |  |

setting m:= a ​ d ​ e m:=ade and bounding ϕ ⁡ ( 4 ​ a ​ d ​ e) ⩾ ϕ ⁡ ( a ​ d ​ e) \phi(4ade)\geqslant\phi(ade), we can bound this in turn by

 | ≪ N log ⁡ N ​ ∑ m ≪ N 4 / 5 τ 3 ​ ( m) ϕ ⁡ ( m) \ll\frac{N}{\log N}\sum_{m\ll N^{4/5}}\frac{\tau_{3}(m)}{\phi(m)} |  |

where τ 3 ( m):= ∑ a, d, e: a ​ d ​ e = m 1 \tau_{3}(m):=\sum_{a,d,e:ade=m}1. Applying Lemma A.1, we have

 | ∑ m ≪ N 4 / 5 τ 3 ​ ( m) ϕ ⁡ ( m) ≪ log 3 ⁡ N, \sum_{m\ll N^{4/5}}\frac{\tau_{3}(m)}{\phi(m)}\ll\log^{3}N, |  | (9.2) |

and so this contribution is acceptable.

Now we consider the case a ​ c ​ d ≪ N 4 / 5 acd\ll N^{4/5}. Here, we rewrite 4 ​ a ​ c ​ d ​ e − 4 ​ a 2 ​ d − e 4acde-4a^{2}d-e as ( 4 ​ a ​ c ​ d − 1) ​ e − 4 ​ a 2 ​ d (4acd-1)e-4a^{2}d, which then traverses a (possibly non-primitive) residue class modulo 4 ​ a ​ c ​ d − 1 4acd-1. Applying the Brun-Titchmarsh inequality as before, we may bound this contribution by

 | ≪ N log ⁡ N ∑ a, c, d: a ​ c ​ d ≪ N 4 / 5 1 ϕ ⁡ ( 4 ​ a ​ c ​ d − 1) \ll\frac{N}{\log N}\sum_{a,c,d:acd\ll N^{4/5}}\frac{1}{\phi(4acd-1)} |  |

and hence (setting m:= 4 ​ a ​ c ​ d − 1 m:=4acd-1) by

 | ≪ N log ⁡ N ​ ∑ m ≪ N 4 / 5 τ 3 ​ ( m + 1) ϕ ⁡ ( m), \ll\frac{N}{\log N}\sum_{m\ll N^{4/5}}\frac{\tau_{3}(m+1)}{\phi(m)}, |  |

so that it suffices to establish the bound

 | ∑ m ≪ N 4 / 5 τ 3 ​ ( m + 1) ϕ ⁡ ( m) ≪ log 3 ⁡ N. \sum_{m\ll N^{4/5}}\frac{\tau_{3}(m+1)}{\phi(m)}\ll\log^{3}N. |  | (9.3) |

This is superficially similar to ( 9.2), but this time the summand is not multiplicative in m m, and we can no longer directly apply Lemma A.1. To deal with this, we apply ( A.12) and bound ( 9.3) by

 | ≪ ∑ m ≪ N 4 / 5 ∑ d | m τ 3 ​ ( m + 1) d ​ m; \ll\sum_{m\ll N^{4/5}}\sum_{d\mid m}\frac{\tau_{3}(m+1)}{dm}; |  |

writing m = d ​ n m=dn, we can rearrange this as

 | ≪ ∑ d ≪ N 4 / 5 1 d 2 ​ ∑ n ≪ N 4 / 5 / d τ 3 ​ ( d ​ n + 1) n. \ll\sum_{d\ll N^{4/5}}\frac{1}{d^{2}}\sum_{n\ll N^{4/5}/d}\frac{\tau_{3}(dn+1)}{n}. |  |

Applying dyadic decomposition of the d, n d,n variables and using Proposition 7.5, we obtain ( 9.3) as required.

Finally, we consider the case a ​ b ≪ N 4 / 5 ab\ll N^{4/5}. Here, we rewrite 4 ​ a ​ c ​ d ​ e − 4 ​ a 2 ​ d − e 4acde-4a^{2}d-e as 4 ​ a ​ b ​ d − e 4abd-e, and note that e e divides a + b = c ​ e a+b=ce. If we fix a, b a,b, there are thus at most τ ⁡ ( a + b) \tau(a+b) choices for e e (which also fixes c c), and once one fixes such a choice, 4 ​ a ​ b ​ d − e 4abd-e traverses a (possibly non-primitive) residue class modulo 4 ​ a ​ b 4ab. Applying the Brun-Titchmarsh inequality again, we may bound this contribution by

 | ≪ N log ⁡ N ∑ a, b: a ​ b ≪ N 4 / 5; ( a, b) = 1 τ ⁡ ( a + b) ϕ ⁡ ( 4 ​ a ​ b). \ll\frac{N}{\log N}\sum_{a,b:ab\ll N^{4/5};(a,b)=1}\frac{\tau(a+b)}{\phi(4ab)}. |  |

Bounding ϕ ⁡ ( 4 ​ a ​ b) ⩾ ϕ ⁡ ( a ​ b) \phi(4ab)\geqslant\phi(ab) and using ( A.12), we can bound this by

 | ≪ N log ⁡ N ∑ a, b: a ​ b ≪ N 4 / 5; ( a, b) = 1 ∑ k | a ∑ l | b τ ⁡ ( a + b) a ​ b ​ k ​ l. \ll\frac{N}{\log N}\sum_{a,b:ab\ll N^{4/5};(a,b)=1}\sum_{k\mid a}\sum_{l\mid b}\frac{\tau(a+b)}{abkl}. |  |

Writing a = k ​ m a=km, b = l ​ n b=ln, we may bound this by

 | ≪ N log ⁡ N ∑ k, l, m, n: k ​ l ​ m ​ n ≪ N 4 / 5; ( k, l, m, n) = 1 1 k 2 ​ l 2 ​ m ​ n τ ( k m + l n). \ll\frac{N}{\log N}\sum_{\begin{subarray}{c}k,l,m,n:klmn\ll N^{4/5};\\ (k,l,m,n)=1\end{subarray}}\frac{1}{k^{2}l^{2}mn}\tau(km+ln). |  |

Dyadically decomposing in k, l, m, n k,l,m,n and using Proposition 7.6, we see that this contribution is also O ⁡ ( N ​ log 2 ​ N) O(N\log^{2}N). The proof of ( 9.1) (and thus Theorem 1.1) is now complete.

## 10. Solutions by polynomials

We now prove Proposition 1.9. We first verify that each of the sets is solvable by polynomials (which of course implies that any residue class contained in such classes are also solvable by polynomials). We first do this for the Type I sets. In view of the π n I \pi^{\operatorname{I}}_{n} map (which clearly preserves polynomiality), it will suffice to find polynomials a = a ⁡ ( n), …, f = f ⁡ ( n) a=a(n),\ldots,f=f(n) of n n that take values in ℕ \mathbb{N} for sufficiently large n n in these sets, and such that ( a ⁡ ( n), …, f ⁡ ( n)) ∈ Σ n I (a(n),\ldots,f(n))\in\Sigma^{\operatorname{I}}_{n} for all n n. This is achieved as follows:

- •

If n = − f mod 4 ​ a ​ d n=-f\mod 4ad, where a, d, f ∈ ℕ a,d,f\in\mathbb{N} are such that f | 4 ​ a 2 ​ d + 1 f\mid 4a^{2}d+1, then we take

 | ( a, b, c, d, e, f):= ( a, n + f 4 ​ a ​ d ​ e − a, n + f 4 ​ a ​ d, d, e, 4 ​ a 2 ​ d + 1 e). (a,b,c,d,e,f):=\left(a,\frac{n+f}{4ad}e-a,\frac{n+f}{4ad},d,e,\frac{4a^{2}d+1}{e}\right). |  |

- •

If n = − f mod 4 ​ a ​ c n=-f\mod 4ac and n = − c / a mod f n=-{c}/{a}\mod f, where a, c, f ∈ ℕ a,c,f\in\mathbb{N} are such that ( 4 ​ a ​ c, f) = 1 (4ac,f)=1, then we take

 | ( a, b, c, d, e, f):= ( a, n ​ a + c f, c, n + f 4 ​ a ​ c, n ​ a + a ​ f + c f ​ c, f); (a,b,c,d,e,f):=\left(a,\frac{na+c}{f},c,\frac{n+f}{4ac},\frac{na+af+c}{fc},f\right); |  |

note from the hypotheses that n ​ a + a ​ f + c na+af+c is divisible by the coprime moduli f f and c c, and is thus also divisible by f ​ c fc.

- •

If n = − f mod 4 ​ c ​ d n=-f\mod 4cd and n 2 = − 4 ​ c 2 ​ d mod f n^{2}=-4c^{2}d\mod f, where c, d, f, q ∈ ℕ c,d,f,q\in\mathbb{N} are such that ( 4 ​ c ​ d, f) = 1 (4cd,f)=1, then we take

 | ( a, b, c, d, e, f):= ( n + f 4 ​ c ​ d, n 2 + 4 ​ c 2 ​ d + n ​ f 4 ​ c ​ d ​ f, c, d, ( n + f) 2 + 4 ​ c 2 ​ d 4 ​ c 2 ​ d ​ f, f); (a,b,c,d,e,f):=\left(\frac{n+f}{4cd},\frac{n^{2}+4c^{2}d+nf}{4cdf},c,d,\frac{(n+f)^{2}+4c^{2}d}{4c^{2}df},f\right); |  |

note from the hypotheses that ( n + f) 2 + 4 ​ c 2 ​ d (n+f)^{2}+4c^{2}d is divisible by the coprime moduli 4 ​ c 2 ​ d 4c^{2}d and f f, and is thus also divisible by 4 ​ c 2 ​ d ​ f 4c^{2}df.

- •

If n = − 1 / e mod 4 a b n=-{1}/{e}\mod 4ab, where a, b, e ∈ ℕ a,b,e\in\mathbb{N} are such that e | a + b e\mid a+b and ( e, 4 ​ a ​ b) = 1 (e,4ab)=1, then we take

 | ( a, b, c, d, e, f):= ( a, b, a + b e, n ​ e + 1 4 ​ a ​ b, e, 4 ​ a ​ a + b e ​ n ​ e + 1 4 ​ a ​ b − n) (a,b,c,d,e,f):=\left(a,b,\frac{a+b}{e},\frac{ne+1}{4ab},e,4a\frac{a+b}{e}\frac{ne+1}{4ab}-n\right) |  |

One easily verifies in each of these cases that one has an ℕ \mathbb{N} -point of Σ n I \Sigma^{\operatorname{I}}_{n} for n n large enough.

Now we turn to the Type II case. We use the same arguments as before, but using Σ n II \Sigma^{\operatorname{II}}_{n} in place of Σ n I \Sigma^{\operatorname{I}}_{n} of course:

- •

If n = − e mod 4 ​ a ​ b n=-e\mod 4ab, where a, b, e ∈ ℕ a,b,e\in\mathbb{N} are such that e | a + b e\mid a+b and ( e, 4 ​ a ​ b) = 1 (e,4ab)=1, then we take

 | ( a, b, c, d, e, f):= ( a, b, a + b e, n + e 4 ​ a ​ b, e, a + b e ​ n + e b − 1). (a,b,c,d,e,f):=\left(a,b,\frac{a+b}{e},\frac{n+e}{4ab},e,\frac{a+b}{e}\frac{n+e}{b}-1\right). |  |

- •

If n = − 4 ​ a 2 ​ d mod f n=-4a^{2}d\mod f, where a, d, f ∈ ℕ a,d,f\in\mathbb{N} are such that 4 ​ a ​ d | f + 1 4ad\mid f+1, then we take

 | ( a, b, c, d, e, f):= ( a, f + 1 4 ​ a ​ d ​ n + 4 ​ a 2 ​ d f − a, f + 1 4 ​ a ​ d, d, n + 4 ​ a 2 ​ d f, f). (a,b,c,d,e,f):=\left(a,\frac{f+1}{4ad}\frac{n+4a^{2}d}{f}-a,\frac{f+1}{4ad},d,\frac{n+4a^{2}d}{f},f\right). |  |

- •

If n = − 4 ​ a 2 ​ d − e mod 4 ​ a ​ d ​ e n=-4a^{2}d-e\mod 4ade, where a, d, e ∈ ℕ a,d,e\in\mathbb{N} are such that ( 4 ​ a ​ d, e) = 1 (4ad,e)=1, then we take

 | ( a, b, c, d, e, f):= ( a, n + e 4 ​ a ​ d, n + 4 ​ a 2 ​ d + e 4 ​ a ​ d ​ e, d, e, n + 4 ​ a 2 ​ d e). (a,b,c,d,e,f):=\left(a,\frac{n+e}{4ad},\frac{n+4a^{2}d+e}{4ade},d,e,\frac{n+4a^{2}d}{e}\right). |  |

Again, one easily verifies in each of these cases that one has an ℕ \mathbb{N} -point of Σ n II \Sigma^{\operatorname{II}}_{n} for n n large enough.

Now we establish the converse claim. Suppose first that we have a primitive residue class q mod r q\mod r that can be solved by polynomials, then we have

 | 4 p = 1 x + 1 y + 1 z \frac{4}{p}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z} |  |

for all sufficiently large primes p p in this class, where x = x ⁡ ( p), y = y ⁡ ( p), z = z ⁡ ( p) x=x(p),y=y(p),z=z(p) are polynomials of p p that take natural number values for all large p p in this class. Note that (depending on whether the constant coefficient of x ⁡ ( p) x(p) is nonzero or not) one either has p | x ⁡ ( p) p|x(p) for all p p, or p | x ⁡ ( p) p\not|x(p) for all sufficiently large p p. Similarly for y ⁡ ( p) y(p) and z ⁡ ( p) z(p). Thus, after permuting, we may assume that we are either in the Type I case where p | x ⁡ ( p) p|x(p) and p | y ⁡ ( p), z ⁡ ( p) p\not|y(p),z(p) for all sufficiently large p p in the class, or else in the Type II case where p | x ⁡ ( p) p\not|x(p) and p | y ⁡ ( p), z ⁡ ( p) p|y(p),z(p) for all sufficiently large p p in the class.

Suppose first we are in the Type I case. For all sufficiently large p p, we either have y ⁡ ( p) ⩽ z ⁡ ( p) y(p)\leqslant z(p) for all p p, or y ⁡ ( p) ⩾ z ⁡ ( p) y(p)\geqslant z(p) for all p p; by symmetry we may assume the latter.

Applying Proposition 2.2, we see that

 | ( x, y, z) = ( a ​ b ​ d ​ p, a ​ c ​ d, b ​ c ​ d) (x,y,z)=(abdp,acd,bcd) |  |

for some ℕ \mathbb{N} -point ( a, …, f) = ( a ⁡ ( p), …, f ⁡ ( p)) (a,\ldots,f)=(a(p),\ldots,f(p)) in Σ p I \Sigma^{\operatorname{I}}_{p} with a ⁡ ( p), b ⁡ ( p), c ⁡ ( p) a(p),b(p),c(p) having no common factor. In particular, d = d ⁡ ( p) d=d(p) is the greatest common divisor of x ⁡ ( p), y ⁡ ( p), z ⁡ ( p) x(p),y(p),z(p). On the other hand, if we let d ~ ∈ ℚ ⁡ [t] \tilde{d}\in\mathbb{Q}[t] be the monic greatest common divisor of x, y, z x,y,z, then there are natural numbers C 1, C 2 C_{1},C_{2} such that C 1 ​ d ~ ​ ( p) C_{1}\tilde{d}(p) is always an integer and C 1 ​ d ~ ​ ( p) C_{1}\tilde{d}(p) divides C 2 ​ x ​ ( p), C 2 ​ y ​ ( p), C 2 ​ z ​ ( p) C_{2}x(p),C_{2}y(p),C_{2}z(p), and by the Euclidean algorithm we know that there is also a natural number C 3 C_{3} such that C 1 ​ C 3 ​ d ~ ​ ( p) C_{1}C_{3}\tilde{d}(p) is an integer combination of x ⁡ ( p), y ⁡ ( p), z ⁡ ( p) x(p),y(p),z(p). From this we see that d ⁡ ( p) d(p) is of the form q ⁡ ( p) ​ d ~ ​ ( p) q(p)\tilde{d}(p) where q ⁡ ( p) q(p) is a rational number that takes on only finitely many values as p p varies. For any given rational q q, the question of whether q ​ d ~ ​ ( p) q\tilde{d}(p) is an integer, and whether q ​ d ~ ​ ( p) q\tilde{d}(p) divides x ⁡ ( p), y ⁡ ( p), z ⁡ ( p) x(p),y(p),z(p), can be determined in terms of finitely many residue classes p ​ mod ⁡ r p\operatorname{mod}r of p p (note that x ⁡ ( p) q ​ d ~ ​ ( p), y ⁡ ( p) q ​ d ~ ​ ( p), z ⁡ ( p) q ​ d ~ ​ ( p) \frac{x(p)}{q\tilde{d}(p)},\frac{y(p)}{q\tilde{d}(p)},\frac{z(p)}{q\tilde{d}(p)} are polynomials in p p with rational coefficients). Thus, one can partition the original residue class of p p into finitely many subclasses, such that on each such class, q ⁡ ( p) = q q(p)=q is independent of p p. We now pass to an arbitrary such subclass (eliminating the non-primitive classes, as these only contain at most one prime), so that d ⁡ ( p) d(p) is now a polynomial function of p p. Dividing out by d d and repeating these arguments, we conclude (after passing to further subclasses if necessary) that a = a ⁡ ( p) a=a(p), b = b ⁡ ( p) b=b(p), and c = c ⁡ ( p) c=c(p) are also polynomials in p p for sufficiently large p p in the subclass. Applying the identities ( 2.1)-( 2.9) we also see that e = e ⁡ ( p) e=e(p) and f = f ⁡ ( p) f=f(p) are polynomials in p p for sufficiently large p p. It will then suffice to show that all subclasses obtained in this fashion lie in a residue class from one of the Type I families in Proposition 1.9.

From Lemma 2.8 we have a ⁡ ( p) ​ c ​ ( p) ​ d ​ ( p) = O ⁡ ( p) a(p)c(p)d(p)=O(p) and f ⁡ ( p) = O ⁡ ( p) f(p)=O(p) for all p p, which implies that at least two of the polynomials a ⁡ ( p), c ⁡ ( p), d ⁡ ( p) a(p),c(p),d(p) must be constant in p p, and that f ⁡ ( p) f(p) has degree at most 1 1 in p p. We now divide into several cases.

First suppose that a, d a,d are independent of p p. By ( 2.7) this forces e, f e,f to be independent of p p as well, and f f divides 4 ​ a 2 ​ d + 1 4a^{2}d+1. By ( 2.6) we have

 | p = − f mod 4 ​ a ​ d p=-f\mod 4ad |  |

for all sufficiently large primes p p in the given subclass, and the claim follows in this case.

Now suppose that a, c a,c are independent of p p, and f f has degree 0 0 (i.e. is also independent of p p). Then from ( 2.6) we have p = − f mod 4 ​ a ​ c p=-f\mod 4ac, and from ( 2.8) we have p = − c / a mod f p=-{c}/{a}\mod f; since p p is a large prime this also forces ( 4 ​ a ​ c, f) = 1 (4ac,f)=1, and the claim follows.

Now suppose instead that a, c a,c are independent of p p, and f f has degree 1 1 (and thus grows linearly in p p). By Lemma 2.8, b, e b,e are then bounded and thus constant in p p. From ( 2.2) we have e | a + b e\mid a+b, and from ( 2.1) we have p = − 1 / e mod 4 a b p=-{1}/{e}\mod 4ab. As p p is an arbitrarily large prime, this forces ( 4 ​ a ​ b, e) = 1 (4ab,e)=1, and the claim follows.

Next, suppose that c, d c,d are independent of p p, and f f has degree 0 0. Then from ( 2.6) one has p = − f mod 4 ​ c ​ d p=-f\mod 4cd, which in particular forces ( 4 ​ c ​ d, f) = 1 (4cd,f)=1. From ( 2.9) one has p 2 = − 4 ​ c 2 ​ d mod f p^{2}=-4c^{2}d\mod f, and the claim follows.

Finally, suppose that c, d c,d are independent of p p, and f f has degree 1 1. By ( 2.9), f ⁡ ( p) f(p) divides p 2 + 4 ​ c 2 ​ d p^{2}+4c^{2}d for all large primes p p in the primitive residue subclass. Applying the Euclidean algorithm, we conclude that f f in fact divides p 2 + 4 ​ c 2 ​ d p^{2}+4c^{2}d*as a polynomial*in p p. But as c, d c,d are positive, p 2 + 4 ​ c 2 ​ d p^{2}+4c^{2}d is irreducible over the reals, a contradiction. This concludes the treatment of the Type I case.

Now suppose we are in the Type II case. Arguing as in the Type I case, we obtain an ℕ \mathbb{N} -point ( a, …, f) = ( a ⁡ ( p), …, f ⁡ ( p)) (a,\ldots,f)=(a(p),\ldots,f(p)) in Σ p II \Sigma^{\operatorname{II}}_{p} for all sufficiently large primes p p in this class, and obeying the bounds in Lemma 2.8, and after partitioning the set of such large primes p p into a finite number of primitive subclasses, one has a ⁡ ( p), …, f ⁡ ( p) a(p),\ldots,f(p) all depending in a polynomial fashion on p p in each subclass.

We now work with an individual subclass and show that all sufficiently large primes p p in this subclass lie in a residue class in one of the Type II families in Proposition 1.9. From Lemma 2.8 we have a ⁡ ( p) ​ c ​ ( p) ​ d ​ ( p) ​ e ​ ( p) = O ⁡ ( p) a(p)c(p)d(p)e(p)=O(p), and so three of these polynomials a ⁡ ( p), c ⁡ ( p), d ⁡ ( p), e ⁡ ( p) a(p),c(p),d(p),e(p) must be independent of p p.

Suppose first that a, c, e a,c,e are independent of p p. By ( 2.2), b b is independent of p p also, and e | a + b e\mid a+b. By ( 2.13), p = − e mod 4 ​ a ​ b p=-e\mod 4ab, and thus ( e, 4 ​ a ​ b) = 1 (e,4ab)=1, and the claim then follows from Dirichlet’s theorem.

Now suppose that a, c, d a,c,d are independent of p p. By ( 2.18), f f is independent of p p also, and 4 ​ a ​ d | f + 1 4ad\mid f+1. From ( 2.19) one has p = − 4 ​ a 2 ​ d mod f p=-4a^{2}d\mod f, and the claim follows.

Next, suppose a, d, e a,d,e are independent of p p. By ( 2.16) one has p = − 4 ​ a 2 ​ d − e mod 4 ​ a ​ d ​ e p=-4a^{2}d-e\mod 4ade, which implies ( 4 ​ a ​ d, e) = 1 (4ad,e)=1, and the claim follows.

Finally, suppose c, d, e c,d,e are independent of p p. By ( 2.14) this forces a, b a,b to be bounded, and hence also independent of p p; and so this case is subsumed by the preceding cases.

## 11. Lower bounds III

### 11.1. Generation of solutions

We begin the proof of Theorem 1.11; the method of proof will be a generalisation of that in Section 5. For the rest of this section, m m and k k are fixed, and all implied constants in asymptotic notation are allowed to depend on m, k m,k. We assume that N N is sufficiently large depending on m, k m,k.

In the m = 4, k = 3 m=4,k=3 case, Type II solutions were generated by the ansatz

 | ( t 1, t 2, t 3) = ( a ​ b ​ d, a ​ c ​ d ​ n, b ​ c ​ d ​ n) (t_{1},t_{2},t_{3})=(abd,acdn,bcdn) |  |

for various quadruples ( a, b, c, d) (a,b,c,d) (or equivalently, quadruples ( a, c, d, e) (a,c,d,e), setting b:= c ​ e − a b:=ce-a); see ( 2.22). We will use a generalisation of this ansatz for higher k k; for instance, when k = 4 k=4 we will construct solutions of the form

 | ( t 1, t 2, t 3, t 4) = ( b ​ x 12 ​ x 123 ​ x 124 ​ x 1234, x 12 ​ x 23 ​ x 24 ​ x 123 ​ x 124 ​ x 234 ​ x 1234 ​ n, b ​ x 23 ​ x 123 ​ x 234 ​ x 1234 ​ n, b ​ x 24 ​ x 124 ​ x 234 ​ x 1234 ​ n) (t_{1},t_{2},t_{3},t_{4})=(bx_{12}x_{123}x_{124}x_{1234},x_{12}x_{23}x_{24}x_{123}x_{124}x_{234}x_{1234}n,bx_{23}x_{123}x_{234}x_{1234}n,bx_{24}x_{124}x_{234}x_{1234}n) |  |

for various octuples ( b, x 12, x 23, x 24, x 123, x 124, x 234, x 1234) (b,x_{12},x_{23},x_{24},x_{123},x_{124},x_{234},x_{1234}), or equivalently, using octuples

 | ( x 12, x 23, x 24, x 123, x 124, x 234, x 1234, e), (x_{12},x_{23},x_{24},x_{123},x_{124},x_{234},x_{1234},e), |  |

and setting

 | b = e ​ x 23 ​ x 24 ​ x 234 − x 12 ​ x 24 ​ x 124 − x 12 ​ x 23 ​ x 123. b=ex_{23}x_{24}x_{234}-x_{12}x_{24}x_{124}-x_{12}x_{23}x_{123}. |  |

More generally, we will generate Type II solutions via the following lemma.

###### Lemma 11.2 (Generation of Type II solutions).

Let 𝒫 {\mathcal{P}} denote the set 2 k − 1 − 1 2^{k-1}-1 -element set

 | 𝒫:= { I ⊂ { 1, …, k }: 2 ∈ I; I ≠ { 2 } }. {\mathcal{P}}:=\{I\subset\{1,\ldots,k\}:2\in I;I\neq\{2\}\}. |  |

Let ( x I) I ∈ 𝒫 (x_{I})_{I\in{\mathcal{P}}} be a tuple of natural numbers, and let e e be another natural number, obeying the inequalities

 | 1 2 ​ m ​ N ⩽ e ​ ∏ I ∈ 𝒫 x I \displaystyle\frac{1}{2m}N\leqslant e\prod_{I\in{\mathcal{P}}}x_{I} | ⩽ 1 m ​ N \displaystyle\leqslant\frac{1}{m}N |  | (11.1) |

and

 | 1 < x I ⩽ N 1 / 2 k + 2 1<x_{I}\leqslant N^{1/2^{k+2}} |  | (11.2) |

whenever I ∈ 𝒫 I\in{\mathcal{P}}. Suppose also that the quantity

 | w:= ∏ I ∈ 𝒫: I ≠ { 1, 2 } x I w:=\prod_{I\in{\mathcal{P}}:I\neq\{1,2\}}x_{I} |  | (11.3) |

is square-free. Set

 | b \displaystyle b | : = e ∏ I ∈ 𝒫: 1 ∉ I x I − ∑ j = 3 k ∏ I ∈ 𝒫: j ∉ I x I \displaystyle:=e\prod_{I\in{\mathcal{P}}:1\not\in I}x_{I}-\sum_{j=3}^{k}\prod_{I\in{\mathcal{P}}:j\not\in I}x_{I} |  | (11.4) |

 | t 1 \displaystyle t_{1} | : = b ∏ I ∈ 𝒫: 1 ∈ I x I \displaystyle:=b\prod_{I\in{\mathcal{P}}:1\in I}x_{I} |  | (11.5) |

 | n \displaystyle n | : = m ​ t 1 − e \displaystyle:=mt_{1}-e |  | (11.6) |

 | t 2 \displaystyle t_{2} | : = n ​ ∏ I ∈ 𝒫 x I \displaystyle:=n\prod_{I\in{\mathcal{P}}}x_{I} |  | (11.7) |

and

 | t j:= b n ∏ I ∈ 𝒫: j ∈ I x I. t_{j}:=b\,n\prod_{I\in{\mathcal{P}}:j\in I}x_{I}. |  | (11.8) |

Then n n is a natural number with n ⩽ N n\leqslant N, and ( t 1, …, t k) (t_{1},\ldots,t_{k}) is a Type II solution for this value of n n. Furthermore, each choice of ( x I) I ∈ 𝒫 (x_{I})_{I\in{\mathcal{P}}} and e e generates a distinct Type II solution.

###### Remark 11.3.

In the m = 4, k = 3 m=4,k=3 case, the parameters x I x_{I} are related to the coordinates ( a, b, c, d, e, f) (a,b,c,d,e,f) appearing in Proposition 2.6 by the formula

 | ( a, b, c, d, e, f) = ( x 12, b, x 23, x 123, e, 4 ​ x 12 ​ x 23 ​ x 123 − 1); (a,b,c,d,e,f)=(x_{12},b,x_{23},x_{123},e,4x_{12}x_{23}x_{123}-1); |  |

however, the constraint that a, b, c a,b,c have no common factor and a ​ b ​ d abd is coprime to n n has been replaced by the slightly different criterion that d d is squarefree, which turns out to be more convenient for obtaining lower bounds (note that the same trick was also used to prove ( 5.1)). Parameterisations of this type have appeared numerous times in the previous literature (see [24, 27, 60, 15], or indeed Propositions 2.2, 2.6), though because most of these parameterisations were focused on dealing with *all*solutions of a given type, as opposed to an easily countable subset of solutions, there were more parameters x I x_{I} (indexed by all non-empty subsets of { 1, …, k } \{1,\ldots,k\}, not just the ones in 𝒫 {\mathcal{P}}), and there were some coprimality conditions on the x I x_{I} rather than square-free conditions.

###### Proof.

Let the notation be as in the lemma. Then from ( 11.2) one has

 | ∑ j = 3 k ∏ I ∈ 𝒫: j ∉ I x I ⩽ ( k − 2) N 2 k − 2 / 2 k + 2 ≪ N 1 / 16 \sum_{j=3}^{k}\prod_{I\in{\mathcal{P}}:j\not\in I}x_{I}\leqslant(k-2)N^{2^{k-2}/2^{k+2}}\ll N^{1/16} |  |

while since

 | ∏ I ∈ 𝒫 x I ≪ N 2 k − 1 / 2 k + 2 ≪ N 1 / 8 \prod_{I\in{\mathcal{P}}}x_{I}\ll N^{2^{k-1}/2^{k+2}}\ll N^{1/8} |  |

we see from ( 11.1) that

 | e ≫ N 7 / 8. e\gg N^{7/8}. |  |

From ( 11.4) we then have that

 | 1 2 e ∏ I ∈ 𝒫: 1 ∉ I x I ⩽ b ⩽ e ∏ I ∈ 𝒫: 1 ∉ I x I \frac{1}{2}e\prod_{I\in{\mathcal{P}}:1\not\in I}x_{I}\leqslant b\leqslant e\prod_{I\in{\mathcal{P}}:1\not\in I}x_{I} |  |

and thus by ( 11.5)

 | 1 2 ​ e ​ ∏ I ∈ 𝒫 x I ⩽ t 1 ⩽ e ​ ∏ I ∈ 𝒫 x I \frac{1}{2}e\prod_{I\in{\mathcal{P}}}x_{I}\leqslant t_{1}\leqslant e\prod_{I\in{\mathcal{P}}}x_{I} |  |

and thus by ( 11.6) (noting that m ⩾ 4 m\geqslant 4)

 | 1 4 ​ m ​ e ​ ∏ I ∈ 𝒫 x I ⩽ n ⩽ m ​ e ​ ∏ I ∈ 𝒫 x I. \frac{1}{4}me\prod_{I\in{\mathcal{P}}}x_{I}\leqslant n\leqslant me\prod_{I\in{\mathcal{P}}}x_{I}. |  |

These bounds ensure that b, n, t 1, …, t k b,n,t_{1},\ldots,t_{k} are natural numbers with n ⩽ N n\leqslant N, and with t 2, …, t k t_{2},\ldots,t_{k} divisible by n n. Dividing ( 11.4) by b ​ n ​ ∏ I ∈ 𝒫 x I b\,n\prod_{I\in{\mathcal{P}}}x_{I} and using ( 11.5), ( 11.7), ( 11.8), we conclude that

 | 1 t 2 = e n ​ t 1 − ∑ j = 3 k 1 t j; \frac{1}{t_{2}}=\frac{e}{nt_{1}}-\sum_{j=3}^{k}\frac{1}{t_{j}}; |  |

applying ( 11.6) one concludes that ( t 1, …, t k) (t_{1},\ldots,t_{k}) is a Type II solution.

It remains to demonstrate that each choice of ( x I) I ∈ 𝒫 (x_{I})_{I\in{\mathcal{P}}} and e e generates a distinct Type II solution, or equivalently that the Type II solution ( t 1, …, t k) (t_{1},\ldots,t_{k}) uniquely determines ( x I) I ∈ 𝒫 (x_{I})_{I\in{\mathcal{P}}} and e e. To do this, first observe from ( 1.6) that ( t 1, …, t k) (t_{1},\ldots,t_{k}) determines n n, and from ( 11.6) we see that e e is determined also. Next, observe from ( 11.5), ( 11.7), ( 11.8) that for any 3 ⩽ j ⩽ k 3\leqslant j\leqslant k, one has

 | t 2 ​ t j n 2 ​ t 1 = ( ∏ I ∈ 𝒫: j ∈ I; 1 ∉ I x I) 2 ( ∏ I ∈ 𝒫: j ∈ I ​ XOR ​ 1 ∉ I x I) \frac{t_{2}t_{j}}{n^{2}t_{1}}=\left(\prod_{I\in{\mathcal{P}}:j\in I;1\not\in I}x_{I}\right)^{2}\left(\prod_{I\in{\mathcal{P}}:j\in I\hbox{ XOR }1\not\in I}x_{I}\right) |  | (11.9) |

where XOR denotes the exclusive or operator; in particular, the left-hand side is necessarily a natural number. Note that all the factors x I x_{I} appearing on the right-hand side are components of the square-free quantity w w given by ( 11.3). We conclude that ( ∏ I ∈ 𝒫: j ∈ I; 1 ∉ I x I) 2 (\prod_{I\in{\mathcal{P}}:j\in I;1\not\in I}x_{I})^{2} is the largest perfect square dividing t 2 ​ t j n 2 ​ t 1 \frac{t_{2}t_{j}}{n^{2}t_{1}}. We conclude that the Type II solution ( t 1, …, t k) (t_{1},\ldots,t_{k}) determines all the products

 | ∏ I ∈ 𝒫: j ∈ I; 1 ∉ I x I \prod_{I\in{\mathcal{P}}:j\in I;1\not\in I}x_{I} |  | (11.10) |

for 3 ⩽ j ⩽ k 3\leqslant j\leqslant k. Note (from the square-free nature of w w) that the x I x_{I} with 1 ∉ I 1\not\in I are all coprime. Taking the greatest common divisor of the ( 11.10) for all 3 ⩽ j ⩽ k 3\leqslant j\leqslant k, we see that the Type II solution determines x { 2, 3, …, k } x_{\{2,3,\ldots,k\}}. Dividing this quantity out from all the expressions ( 11.10), and then taking the greatest common divisor of the resulting quotients for 4 ⩽ j ⩽ k 4\leqslant j\leqslant k, one recovers x { 2, 4, …, k } x_{\{2,4,\ldots,k\}}; a similar argument gives x I x_{I} for any I ∈ 𝒫 I\in{\mathcal{P}} with 1 ∉ I 1\not\in I of cardinality k − 3 k-3. Dividing out these quantities and taking greatest common divisors again, one can then recover x I x_{I} for any I ∈ 𝒫 I\in{\mathcal{P}} with 1 ∉ I 1\not\in I of cardinality k − 4 k-4; continuing in this fashion we can recover all the x I x_{I} with I ∈ 𝒫 I\in{\mathcal{P}} and 1 ∉ I 1\not\in I.

Returning to ( 11.9), we can then recover the products ∏ I ∈ 𝒫: 1, j ∈ I x I \prod_{I\in{\mathcal{P}}:1,j\in I}x_{I} for all 3 ⩽ j ⩽ k 3\leqslant j\leqslant k. Taking greatest common divisors iteratively as before, we can then recover all the x I x_{I} with I ∈ 𝒫 I\in{\mathcal{P}} and 1 ∈ I 1\in I, thus reconstructing all of the data ( x I) I ∈ 𝒫 (x_{I})_{I\in{\mathcal{P}}} and e e, as claimed. ∎

In view of this above lemma, we see that to prove ( 1.7), it suffices to show that the number of tuples ( ( x I) I ∈ 𝒫, e) ((x_{I})_{I\in{\mathcal{P}}},e) obeying the hypotheses of the lemma is at least c ​ N ​ ( log ⁡ N) 2 k − 1 − 1 cN(\log N)^{2^{k-1}-1} for an absolute constant c > 0 c>0.

Observe that if we fix x I x_{I} with I ∈ 𝒫 I\in{\mathcal{P}} obeying ( 11.2) and with the quantity w w defined by ( 11.3), then there are

 | ≫ N ∏ I ∈ 𝒫 x I \gg\frac{N}{\prod_{I\in{\mathcal{P}}}x_{I}} |  |

choices of e e that obey ( 11.1). Thus, noting that μ 2 ​ ( w) ⩾ μ 2 ​ ( ∏ I ∈ 𝒫 x I) \mu^{2}(w)\geqslant\mu^{2}(\prod_{I\in{\mathcal{P}}}x_{I}), the number of tuples obeying the hypotheses of the lemma is

 | ≫ N ​ ∑ ∗ μ 2 ​ ( ∏ I ∈ 𝒫 x I) ∏ I ∈ 𝒫 x I, \gg N\sum_{*}\frac{\mu^{2}(\prod_{I\in{\mathcal{P}}}x_{I})}{\prod_{I\in{\mathcal{P}}}x_{I}}, |  | (11.11) |

where the sum ∑ ∗ \sum_{*} ranges over all choices of ( x I) I ∈ 𝒫 (x_{I})_{I\in{\mathcal{P}}} obeying the bounds ( 11.2). To estimate ( 11.11), we make use of [16, Theorem 6.4], which we restate as a lemma:

###### Lemma 11.4.

Let l ⩾ 1 l\geqslant 1, and for each 1 ⩽ i ⩽ l 1\leqslant i\leqslant l, let α i < β i \alpha_{i}<\beta_{i} be positive real numbers. Then

 | ∑ N α i ⩽ n i ⩽ N β i ​ for all ​ 1 ⩽ i ⩽ l μ 2 ( n 1 ⋯ n l) n 1 ⋯ n l ≫ l ( log N) l ∏ i = 1 l ( β i − α i), \sum_{N^{\alpha_{i}}\leqslant n_{i}\leqslant N^{\beta_{i}}\hbox{ for all }1\leqslant i\leqslant l}\frac{\mu^{2}(n_{1}\cdots n_{l})}{n_{1}\cdots n_{l}}\gg_{l}(\log N)^{l}\prod_{i=1}^{l}(\beta_{i}-\alpha_{i}), |  | (11.12) |

for N N sufficiently large depending on l l and the α 1, …, α l, β 1, …, β l \alpha_{1},\ldots,\alpha_{l},\beta_{1},\ldots,\beta_{l}.

From this lemma (and noting that there are 2 k − 1 − 1 2^{k-1}-1 parameters x I x_{I} in the sum ∑ ∗ \sum_{*}) we see that

 | ∑ ∗ μ 2 ​ ( ∏ I ∈ 𝒫 x I) ∏ I ∈ 𝒫 x I ≫ log 2 k − 1 − 1 ⁡ N; \sum_{*}\frac{\mu^{2}(\prod_{I\in{\mathcal{P}}}x_{I})}{\prod_{I\in{\mathcal{P}}}x_{I}}\gg\log^{2^{k-1}-1}N; |  | (11.13) |

inserting this into ( 11.11) we obtain the claim.

Now we prove ( 1.8). As in Section 5, the arguments are similar to those used to prove ( 1.7), but with the additional input of the Bombieri-Vinogradov inequality.

As in the proof of ( 1.7), it suffices to obtain a lower bound (in this case, c ​ N ​ ( log ⁡ N) 2 k − 1 − 2 / log ⁡ log ⁡ N c{N(\log N)^{2^{k-1}-2}}/{\log\log N} for some c > 0 c>0) on the number of tuples ( ( x I) I ∈ 𝒫, e) ((x_{I})_{I\in{\mathcal{P}}},e), but now with the additional constraint that the quantity

 | p:= m t 1 − e = m b ∏ I ∈ 𝒫: 1 ∈ I x I − e \displaystyle p:=mt_{1}-e=mb\prod_{I\in{\mathcal{P}}:1\in I}x_{I}-e |  |

is prime.

Suppose we fix ( x I) I ∈ 𝒫 (x_{I})_{I\in{\mathcal{P}}} obeying ( 11.2) with w w squarefree. We may write

 | p = q ​ e + r p=qe+r |  |

where

 | q:= m ​ ∏ I ∈ 𝒫 x I − 1 q:=m\prod_{I\in{\mathcal{P}}}x_{I}-1 |  | (11.14) |

and

 | r:= − m ∏ I ∈ 𝒫: 1 ∈ I x I ∑ j = 3 k ∏ I ∈ 𝒫: j ∉ I x I. r:=-m\prod_{I\in{\mathcal{P}}:1\in I}x_{I}\sum_{j=3}^{k}\prod_{I\in{\mathcal{P}}:j\not\in I}x_{I}. |  |

Thus as e e varies in the range given by ( 11.1), q ​ e + r qe+r traces out an arithmetic progression of spacing q q whose convex hull contains [0.6 ​ N, 0.9 ​ N] [0.6N,0.9N] (say). Thus, every prime p p in this interval [0.6 ​ N, 0.9 ​ N] [0.6N,0.9N] that is congruent to r mod q r\mod q will provide an e e that will give a Type II solution with n = p n=p prime, and different choices of ( x I) I ∈ 𝒫 (x_{I})_{I\in{\mathcal{P}}} and p p will give different Type II solutions.

For fixed ( x I) I ∈ 𝒫 (x_{I})_{I\in{\mathcal{P}}}, if r r is coprime to q q, then we see from ( A.13) (and estimating li ⁡ ( x) = ( 1 + o ⁡ ( 1)) ​ x / log ⁡ x {\rm li}(x)=(1+o(1)){x}/{\log x}) that the number of such p p is at least

 | ⩾ c ​ N log ⁡ N ​ ϕ ​ ( q) − D ⁡ ( 0.6 ​ N, q) − D ⁡ ( 0.9 ​ N, q) \geqslant c\frac{N}{\log N\phi(q)}-D(0.6N;q)-D(0.9N;q) |  |

for some absolute constant c > 0 c>0. It thus suffices to show that

 | ∑ ∗ μ 2 ​ ( w) ​ 1 ( r, q) = 1 ​ N log ⁡ N ​ ϕ ​ ( q) ≫ N ​ ( log ⁡ N) 2 k − 1 − 2 log ⁡ log ⁡ N \sum_{*}\mu^{2}(w)1_{(r,q)=1}\frac{N}{\log N\phi(q)}\gg\frac{N(\log N)^{2^{k-1}-2}}{\log\log N} |  | (11.15) |

and

 | ∑ ∗ D ⁡ ( c ​ N, q) = o ⁡ ( N ​ ( log ⁡ N) 2 k − 1 − 2 log ⁡ log ⁡ N) \sum_{*}D(cN;q)=o\left(\frac{N(\log N)^{2^{k-1}-2}}{\log\log N}\right) |  | (11.16) |

for c = 0.6, 0.9 c=0.6,0.9.

We first show ( 11.15). Since li ⁡ ( N / 100) {\rm li}(N/100) is comparable to N / log ⁡ N N/\log N, and ϕ ⁡ ( q) ⩽ q ≪ w \phi(q)\leqslant q\ll w, we may simplify ( 11.15) as

 | ∑ ∗ μ 2 ​ ( w) ∏ I ∈ 𝒫 x I ​ 1 ( r, q) = 1 ≫ ( log ⁡ N) 2 k − 1 − 1 log ⁡ log ⁡ N. \sum_{*}\frac{\mu^{2}(w)}{\prod_{I\in{\mathcal{P}}}x_{I}}1_{(r,q)=1}\gg\frac{(\log N)^{2^{k-1}-1}}{\log\log N}. |  | (11.17) |

The expression on the left-hand side is similar to ( 11.11), but now one also has the additional constraint 1 ( r, q) = 1 1_{(r,q)=1}. To deal with this constraint, we restrict the ranges of the x I x_{I} parameters somewhat to perform an averaging in the x { 1, 2 } x_{\{1,2\}} parameter (taking advantage of the fact that this parameter does not appear in the μ 2 ​ ( w) \mu^{2}(w) term). More precisely, we restrict to the ranges where

 | x I ⩽ N 1 / 2 100 ​ k x_{I}\leqslant N^{1/2^{100k}} |  | (11.18) |

(say) for I ≠ { 1, 2 } I\neq\{1,2\}, and

 | x { 1, 2 } ⩽ N 1 / 2 k + 2. x_{\{1,2\}}\leqslant N^{1/2^{k+2}}. |  | (11.19) |

We now analyse the constraint that r r and q q are coprime. We can factor

 | r = − m ​ x { 1, 2 } 2 ​ s r=-mx_{\{1,2\}}^{2}s |  |

where

 | s:= ( ∏ I ∈ 𝒫: 1 ∈ I; I ≠ { 1, 2 } x I) ∑ j = 3 k ∏ I ∈ 𝒫: j ∉ I; I ≠ { 1, 2 } x I; s:=\left(\prod_{I\in{\mathcal{P}}:1\in I;I\neq\{1,2\}}x_{I}\right)\sum_{j=3}^{k}\prod_{I\in{\mathcal{P}}:j\not\in I;I\neq\{1,2\}}x_{I}; |  |

the point is that s s does not depend on x { 1, 2 } x_{\{1,2\}}. Since q + 1 q+1 is divisible by m ​ x { 1, 2 } mx_{\{1,2\}}, we see that m ​ x { 1, 2 } 2 mx_{\{1,2\}}^{2} is coprime to q q, and thus ( q, r) = 1 (q,r)=1 iff ( q, s) = 1 (q,s)=1. We can write q = u ​ x { 1, 2 } − 1 q=ux_{\{1,2\}}-1, where u:= m ∏ I ∈ 𝒫: I ≠ { 1, 2 } x I u:=m\prod_{I\in{\mathcal{P}}:I\neq\{1,2\}}x_{I}, and so ( q, r) = 1 (q,r)=1 iff ( u ​ x { 1, 2 } − 1, s) = 1 (ux_{\{1,2\}}-1,s)=1.

We may replace s s here by the largest square-free factor s ′ s^{\prime} of s s. If we then factor s ′ = v ​ y s^{\prime}=vy, where v:= ( s ′, u) v:=(s^{\prime},u) and y:= s ′ / v y:=s^{\prime}/v, then u ​ x { 1, 2 } − 1 ux_{\{1,2\}}-1 is already coprime to v v, and so we conclude that ( q, r) = 1 (q,r)=1 iff ( u ​ x { 1, 2 } − 1, y) = 1 (ux_{\{1,2\}}-1,y)=1.

Fix x I x_{I} for I ≠ { 1, 2 } I\neq\{1,2\}. By construction, u u and y y are coprime, and so the constraint ( u ​ x { 1, 2 } − 1, y) = 1 (ux_{\{1,2\}}-1,y)=1 restricts x { 1, 2 } x_{\{1,2\}} to ϕ ⁡ ( y) \phi(y) distinct residue classes modulo y y. Since

 | y ⩽ s ≪ N 1 / 2 90 ​ k y\leqslant s\ll N^{1/2^{90k}} |  |

(say) thanks to ( 11.18), we conclude that

 | ∑ x { 1, 2 } ⩽ N 1 / 2 k + 2 1 ( q, r) = 1 x { 1, 2 } ≫ ϕ ⁡ ( y) y ​ log ⁡ N. \sum_{x_{\{1,2\}}\leqslant N^{1/2^{k+2}}}\frac{1_{(q,r)=1}}{x_{\{1,2\}}}\gg\frac{\phi(y)}{y}\log N. |  |

Using the crude bound ( A.11), we may lower bound ϕ ⁡ ( y) / y ≫ 1 / log ⁡ log ⁡ N {\phi(y)}/{y}\gg{1}/{\log\log N}. (It is quite likely that by a finer analysis of the generic divisibility properties of y y, one can remove this double logarithmic loss, but we will not attempt to do so here.) We may thus lower bound the left-hand side of ( 11.17) by

 | log ⁡ N log ⁡ log ⁡ N ​ ∑ ∗ ⁣ ∗ μ 2 ​ ( w) w, \frac{\log N}{\log\log N}\sum_{**}\frac{\mu^{2}(w)}{w}, |  |

where ∑ ∗ ⁣ ∗ \sum_{**} sums over all x I x_{I} for I ≠ { 1, 2 } I\neq\{1,2\} obeying ( 11.18). But by Lemma 11.4 we have

 | ∑ ∗ ⁣ ∗ μ 2 ​ ( w) w ≫ ( log ⁡ N) 2 k − 1 − 2, \sum_{**}\frac{\mu^{2}(w)}{w}\gg(\log N)^{2^{k-1}-2}, |  |

and the claim ( 11.17) follows.

Finally, we show ( 11.16). Observe that each q q can be represented in the form ( 11.14) in at most τ 2 k − 1 − 1 ​ ( q + 1) \tau_{2^{k-1}-1}(q+1) different ways; also, from ( 11.2) we have q ≪ N 2 k − 1 / 2 k + 2 = N 1 / 8 q\ll N^{2^{k-1}/2^{k+2}}=N^{1/8}. We may thus bound the left-hand side of ( 11.16) by

 | ∑ q ≪ N 1 / 8 D ⁡ ( c ​ N, q) ​ τ 2 k − 1 − 1 ​ ( q + 1). \sum_{q\ll N^{1/8}}D(cN;q)\tau_{2^{k-1}-1}(q+1). |  |

From the Bombieri-Vinogradov inequality ( A.14) and the trivial bound D ⁡ ( c ​ N, q) ≪ N / q D(cN;q)\ll N/q one has

 | ∑ q ≪ N 1 / 8 q D ( c N; q) 2 ≪ A N log − A N \sum_{q\ll N^{1/8}}qD(cN;q)^{2}\ll_{A}N\log^{-A}N |  |

for any A > 0 A>0, while from Lemma A.1 (and shifting q q by 1 1) one has

 | ∑ q ≪ N 1 / 8 τ 2 k − 1 − 1 ​ ( q + 1) 2 q ≪ log O ⁡ ( 1) ⁡ N. \sum_{q\ll N^{1/8}}\frac{\tau_{2^{k-1}-1}(q+1)^{2}}{q}\ll\log^{O(1)}N. |  |

The claim then follows from the Cauchy-Schwarz inequality (taking A A large enough). The proof of Theorem 1.11 is now complete.

## Appendix A Some results from number theory

In this section we record some well-known facts from number theory that we will need throughout the paper. We begin with a crude estimate for averages of multiplicative functions.

Now we record some asymptotic formulae for the divisor function τ \tau. From the Dirichlet hyperbola method we have the asymptotic

 | ∑ n ⩽ N τ ⁡ ( n) = N ​ log ⁡ N + O ⁡ ( N) \sum_{n\leqslant N}\tau(n)=N\log N+O(N) |  | (A.1) |

(see e.g. [33, §1.5]). More generally, we have

 | ∑ n ⩽ N τ k ​ ( n) = N ​ log k − 1 ​ N + O k ​ ( N ​ log k − 2 ​ N) \sum_{n\leqslant N}\tau_{k}(n)=N\log^{k-1}N+O_{k}(N\log^{k-2}N) |  | (A.2) |

for all k ⩾ 1 k\geqslant 1, where τ k ( n):= ∑ d 1, …, d k: d 1 ​ … ​ d k = n 1 \tau_{k}(n):=\sum_{d_{1},\ldots,d_{k}:d_{1}\ldots d_{k}=n}1. Indeed, the left-hand side of ( A.2) can be rearranged as

 | ∑ d 1 ⩽ N ∑ d 2 ⩽ N / d 1 … ​ ∑ d k ⩽ N / d 1 ​ … ​ d k − 1 1 \sum_{d_{1}\leqslant N}\sum_{d_{2}\leqslant N/d_{1}}\ldots\sum_{d_{k}\leqslant N/d_{1}\ldots d_{k-1}}1 |  |

and the claim follows by evaluating each of the summations in turn.

We can perturb this asymptotic:

###### Lemma A.1 (Crude bounds on sums of multiplicative functions).

Let f ⁡ ( n) f(n) be a multiplicative function obeying the bounds

 | f ⁡ ( p) = m + O ⁡ ( 1 p) f(p)=m+O(\frac{1}{p}) |  |

for all primes p p and some integer m ⩾ 1 m\geqslant 1, and

 | | f ⁡ ( p j) | ≪ j O ⁡ ( 1) |f(p^{j})|\ll j^{O(1)} |  |

for all primes p p and j > 1 j>1. Then one has

 | ∑ n ⩽ N f ( n) ≪ m N log m − 1 N \sum_{n\leqslant N}f(n)\ll_{m}N\log^{m-1}N |  |

for N N sufficiently large depending on m m; from this and summation by parts we have in particular that

 | ∑ n ⩽ N f ⁡ ( n) n ≪ m log m N \sum_{n\leqslant N}\frac{f(n)}{n}\ll_{m}\log^{m}N |  |

If f f is non-negative, we also have the corresponding lower bound

 | ∑ n ⩽ N f ( n) ≫ m N log m − 1 N \sum_{n\leqslant N}f(n)\gg_{m}N\log^{m-1}N |  |

and hence

 | ∑ n ⩽ N f ⁡ ( n) n ≫ m log m N \sum_{n\leqslant N}\frac{f(n)}{n}\gg_{m}\log^{m}N |  |

One can of course get much better estimates by contour integration methods (and these estimates also follow without much difficulty from the more general results in [26]), but the above crude bounds will suffice for our purposes.

###### Proof.

We allow all implied constants to depend on m m. By Möbius inversion, we can write

 | f ⁡ ( n) = ∑ d | n τ m ​ ( d) ​ g ​ ( n d) f(n)=\sum_{d\mid n}\tau_{m}(d)g(\frac{n}{d}) |  |

where g g is a multiplicative function obeying the bounds

 | g ⁡ ( p) = O ⁡ ( 1 p) g(p)=O(\frac{1}{p}) |  |

and

 | | g ⁡ ( p j) | ≪ j O ⁡ ( 1) |g(p^{j})|\ll j^{O(1)} |  |

for all j > 1 j>1. In particular, the Euler product

 | ∑ n = 1 ∞ | g ⁡ ( n) | n = ∏ p ( 1 + | g ⁡ ( p) | p + ∑ j = 2 ∞ | g ⁡ ( p j) | p j) = ∏ p ( 1 + O ⁡ ( 1 p 2)) \sum_{n=1}^{\infty}\frac{|g(n)|}{n}=\prod_{p}\left(1+\frac{|g(p)|}{p}+\sum_{j=2}^{\infty}\frac{|g(p^{j})|}{p^{j}}\right)=\prod_{p}\left(1+O\left(\frac{1}{p^{2}}\right)\right) |  |

is absolutely convergent.

We may therefore write ∑ n ⩽ N f ⁡ ( n) \sum_{n\leqslant N}f(n) as

 | ∑ k ⩽ N g ⁡ ( k) ​ ∑ d ⩽ N / k τ m ​ ( d). \sum_{k\leqslant N}g(k)\sum_{d\leqslant N/k}\tau_{m}(d). |  | (A.3) |

Applying ( A.2), we conclude

 | | ∑ n ⩽ N f ⁡ ( n) | ≪ ∑ k ⩽ N | g ⁡ ( k) | k ​ N ​ log m − 1 ​ N |\sum_{n\leqslant N}f(n)|\ll\sum_{k\leqslant N}\frac{|g(k)|}{k}N\log^{m-1}N |  |

and the upper bound follows from the absolute convergence of ∑ n = 1 ∞ | g ⁡ ( n) | / n \sum_{n=1}^{\infty}{|g(n)|}/{n}.

Now we establish the lower bound. By zeroing out f f at various small primes p p (and all their multiples), we may assume that f ⁡ ( p j) = g ⁡ ( p j) = 0 f(p^{j})=g(p^{j})=0 for all p ⩽ w p\leqslant w for any fixed threshold w w. By making w w large enough, we may ensure that

 | 1 − ∑ n = 2 ∞ | g ⁡ ( n) | n > 0. 1-\sum_{n=2}^{\infty}\frac{|g(n)|}{n}>0. |  |

If we then insert the bound ( A.2) into ( A.3) we obtain the claim. ∎

As a typical application of Lemma A.1 we have

 | ∑ n ⩽ N τ k ( n) ≪ k N log 2 k − 1 N \sum_{n\leqslant N}\tau^{k}(n)\ll_{k}N\log^{2^{k}-1}N |  | (A.4) |

for any N > 1 N>1 and k ⩾ 1 k\geqslant 1, (see also [40]).

To study some more detailed distribution of divisors and prime divisors we recall the *Turán-Kubilius inequality*for additive functions. A function w w is called additive, if w ⁡ ( n 1 ​ n 2) = w ⁡ ( n 1) + w ⁡ ( n 2) w(n_{1}n_{2})=w(n_{1})+w(n_{2}), whenever gcd ⁡ ( n 1, n 2) = 1 \gcd(n_{1},n_{2})=1.

###### Lemma A.2 (Turán-Kubilius inequality (see [69], page 20)).

Let w: ℕ → ℝ w:\mathbb{N}\rightarrow\mathbb{R} denote an arithmetic function which is additive (thus w ⁡ ( n ​ m) = w ⁡ ( n) + w ⁡ ( m) w(nm)=w(n)+w(m) whenever n, m n,m are coprime). Let A ⁡ ( N):= ∑ p k ⩽ N w ⁡ ( p k) / p k A(N):=\sum_{p^{k}\leqslant N}{w(p^{k})}/{p^{k}} and D 2 ​ ( N):= ∑ p k ⩽ N | w ⁡ ( p k) | 2 / p k D^{2}(N):=\sum_{p^{k}\leqslant N}{|w(p^{k})|^{2}}/{p^{k}}. For every N ⩾ 2 N\geqslant 2 and for any additive function w w the following inequality holds:

 | ∑ n ⩽ N | w ⁡ ( n) − A ⁡ ( N) | 2 ⩽ 30 ​ N ​ D 2 ​ ( N). \sum_{n\leqslant N}|w(n)-A(N)|^{2}\leqslant 30ND^{2}(N). |  |

(Here ∑ p k \sum_{p^{k}} denotes the sum over all prime powers.)

###### Example A.1.

Let ω ⁡ ( n) \omega(n) denote the number of distinct prime factors of n n, then A ⁡ ( N) = ∑ p k ⩽ N ω ⁡ ( p k) / p k = log ⁡ log ⁡ N + O ⁡ ( 1) A(N)=\sum_{p^{k}\leqslant N}{\omega(p^{k})}/{p^{k}}=\log\log N+O(1) and D 2 ​ ( N) = ∑ p k ⩽ N ω ​ ( p k) 2 / p k = A ⁡ ( N) = log ⁡ log ⁡ N + O ⁡ ( 1) D^{2}(N)=\sum_{p^{k}\leqslant N}{\omega(p^{k})^{2}}/{p^{k}}=A(N)=\log\log N+O(1). The Turán-Kubilius inequality then gives

 | ∑ n ⩽ N | ω ⁡ ( n) − log ⁡ log ⁡ N | 2 ⩽ 30 ​ N ​ log ⁡ log ⁡ N + O ⁡ ( N). \sum_{n\leqslant N}|\omega(n)-\log\log N|^{2}\leqslant 30N\log\log N+O(N). |  |

In particular, if ξ ⁡ ( n) → ∞ \xi(n)\to\infty as n → ∞ n\to\infty, then one has | ω ⁡ ( n) − log ⁡ log ⁡ n | ⩽ ξ ⁡ ( n) ​ log ⁡ log ⁡ n |\omega(n)-\log\log n|\leqslant\xi(n)\sqrt{\log\log n} for all n n in a set of integers of density 1 1. For more details see [80].

From ( A.1) one might guess the heuristic

 | τ ⁡ ( n) ≈ log ⁡ n \tau(n)\approx\log n |  | (A.5) |

*on average*. But it follows from the Turán-Kubilius inequality that for “typical” n n, the number of divsors is about 2 log ⁡ log ⁡ n = ( log ⁡ n) log ⁡ 2 2^{\log\log n}=(\log n)^{\log 2}, which is considerably smaller, and that a small number of integers with an exceptionally large number of divisors heavily influences this average. The influence of these integers with a very large number of divsiors dominates even more for higher moments. The extremal cases heuristically consist of many small prime factors, and the following “divisor bound” holds

 | τ ⁡ ( n) ⩽ 2 ( 1 + o ⁡ ( 1)) ​ log ⁡ n log ⁡ log ⁡ n = O ⁡ ( n 1 log ⁡ log ⁡ n) \tau(n)\leqslant 2^{(1+o(1))\frac{\log n}{\log\log n}}=O(n^{\frac{1}{\log\log n}}) |  | (A.6) |

for any n ⩾ 1 n\geqslant 1; see [56].

The Turán-Kubilius type inequalities have been studied for shifted primes as well. We make use of the following result of Barban (see Elliott [14], Theorem 12.10).

###### Lemma A.2.

A function w: ℕ → ℝ + w:\mathbb{N}\rightarrow\mathbb{R}^{+} is said to be strongly additive if it is additive and w ⁡ ( p k) = w ⁡ ( p) w(p^{k})=w(p) holds, for every prime power p k p^{k}, k ⩾ 1 k\geqslant 1. Let w w denote a real nonnegative strongly additive function. Define S ⁡ ( N):= ∑ p ⩽ N w ⁡ ( p) / ( p − 1) S(N):=\sum_{p\leqslant N}{w(p)}/{(p-1)} and Λ ⁡ ( N):= max p ⩽ N ⁡ w ⁡ ( p) \Lambda(N):=\max_{p\leqslant N}w(p). Suppose that Λ ⁡ ( N) = o ⁡ ( S ⁡ ( N)) \Lambda(N)=o(S(N)), as N → ∞ N\rightarrow\infty. Then for any fixed ε > 0 \varepsilon>0, the prime density

 | ν N ​ ( p, | w ⁡ ( p + 1) − S ⁡ ( N) | > ε ​ S ​ ( N)) → 0 ​ as ​ N → ∞. \nu_{N}(p;|w(p+1)-S(N)|>\varepsilon S(N))\rightarrow 0\text{ as }N\rightarrow\infty. |  |

The same holds for other shifts p + a p+a, where a ≠ 0 a\neq 0.

The function ω ⁡ ( n) \omega(n) is strongly additive. This lemma implies that for primes with relative prime density 1, p + 1 p+1 contains about 1 2 ​ log ⁡ log ​ p \frac{1}{2}\log\log p primes of the form 1 mod 4 1\bmod 4. To see this one chooses w ⁡ ( p) = 1 w(p)=1 if p ≡ 1 mod 4 p\equiv 1\bmod 4, and 0 0 otherwise. In this example one has S ⁡ ( N) ∼ 1 2 ​ log ⁡ log ​ N S(N)\sim\frac{1}{2}\log\log N and Λ ⁡ ( N) = 1 \Lambda(N)=1.

We recall the quadratic reciprocity law

 | ( m n) ​ ( n m) = ( − 1) ( n − 1) ​ ( m − 1) / 4 \left(\frac{m}{n}\right)\left(\frac{n}{m}\right)=(-1)^{(n-1)(m-1)/4} |  | (A.7) |

for all odd m, n m,n, where ( m n) \left(\frac{m}{n}\right) is the Jacobi symbol, as well as the companion laws

 | ( − 1 n) = ( − 1) ( n − 1) / 4 \left(\frac{-1}{n}\right)=(-1)^{(n-1)/4} |  | (A.8) |

and

 | ( 2 n) = ( − 1) ( n 2 − 1) / 8 \left(\frac{2}{n}\right)=(-1)^{(n^{2}-1)/8} |  | (A.9) |

for odd n n.

For any primitive residue class a mod q a\mod q and any N > 0 N>0, let π ⁡ ( N, q, a) \pi(N;q,a) denote the number of primes p < N p<N that are congruent to a a mod q q. We recall the *Brun-Titchmarsh inequality*(see e.g. [33, Theorem 6.6])

 | π ⁡ ( N, q, a) ≪ N ϕ ⁡ ( q) ​ log ⁡ N q \pi(N;q,a)\ll\frac{N}{\phi(q)\log\frac{N}{q}} |  | (A.10) |

for any such class with N ⩾ q N\geqslant q. This bound suffices for upper bound estimates on primes in residue classes. Due to the q q in the denominator of log ⁡ ( N / q) \log({N}/{q}), it will only be efficient to apply this inequality when q q is much smaller than N N, e.g. q ⩽ N c q\leqslant N^{c} for some c < 1 c<1.

The Euler totient function ϕ ⁡ ( q) \phi(q) in the denominator is also inconvenient; it would be preferable if one could replace it with q q. Unfortunately, this is not possible; the best bound on 1 / ϕ ⁡ ( q) {1}/{\phi(q)} in terms of q q that one has in general is

 | 1 ϕ ⁡ ( q) ≪ log ⁡ log ⁡ q q \frac{1}{\phi(q)}\ll\frac{\log\log q}{q} |  | (A.11) |

(see e.g. [59]). Using this bound would simplify our arguments, but one would lose an additional factor of log ⁡ log ⁡ N \log\log N or so in the final estimates. To avoid this loss, we observe the related estimate

 | 1 ϕ ⁡ ( q) ≪ 1 q ​ ∑ d | q 1 d. \frac{1}{\phi(q)}\ll\frac{1}{q}\sum_{d\mid q}\frac{1}{d}. |  | (A.12) |

Indeed, we have

 | q ϕ ⁡ ( q) \displaystyle\frac{q}{\phi(q)} | = ∏ p | q p p − 1 \displaystyle=\prod_{p\mid q}\frac{p}{p-1} |  |

 |  | = ∏ p | q ( 1 + 1 p) ​ ( 1 + O ⁡ ( 1 p 2)) \displaystyle=\prod_{p\mid q}(1+\frac{1}{p})(1+O(\frac{1}{p^{2}})) |  |

 |  | ≪ ∏ p | q ( 1 + 1 p) \displaystyle\ll\prod_{p\mid q}(1+\frac{1}{p}) |  |

 |  | ⩽ ∑ d | q 1 d, \displaystyle\leqslant\sum_{d\mid q}\frac{1}{d}, |  |

and ( A.12) follows. (One could restrict d d to be square-free here if desired, but we will not need to do so in this paper.)

The Brun-Titchmarsh inequality only gives upper bounds for the number of primes in an arithmetic progression. To get lower bounds, we let D ⁡ ( N, q) D(N;q) denote the quantity

 | D ⁡ ( N, q):= max ( a, q) = 1 ⁡ | π ⁡ ( N, q, a) − li ⁡ ( N) ϕ ⁡ ( q) |. D(N;q):=\max_{(a,q)=1}\left|\pi(N;q,a)-\frac{{\rm li}(N)}{\phi(q)}\right|. |  | (A.13) |

where li ⁡ ( x):= ∫ 0 x 𝑑 t / log ⁡ t {\rm li}(x):=\int_{0}^{x}{dt}/{\log t} is the Cauchy principal value of the logarithmic integral. The Bombieri-Vinogradov inequality (see e.g. [33, Theorem 17.1]) implies in particular that

 | ∑ q ⩽ N θ D ( N; q) ≪ θ, A N log − A N. \sum_{q\leqslant N^{\theta}}D(N;q)\ll_{\theta,A}N\log^{-A}N. |  | (A.14) |

We remark that the above inequality is usually phrased using the summatory von Mangoldt function ψ ⁡ ( N, q, a) = ∑ n ⩽ N; n = a mod q Λ ⁡ ( n) \psi(N;q,a)=\sum_{n\leqslant N;n=a\mod q}\Lambda(n). A summation by parts converts it to an estimate using the prime counting function; see [9] for details.

for all 0 < θ < 1 / 2 0<\theta<1/2 and A > 0 A>0. Informally, this gives lower bounds on π ⁡ ( N, q, a) \pi(N;q,a) on the average for q q much smaller than N 1 / 2 N^{1/2}.

## References

- [1] A. Aigner, ‘Brüche als Summe von Stammbrüchen’, *J. Reine Angew. Math.*214/215 (1964), 174–179.
- [2] M. B. Barban, P. P. Vehov, ‘Summation of multiplicative functions of polynomials’, *Mat. Zametki*5 (1969), 669–680.
- [3] P. Bartoš, ‘K Riešitel’nosti Diofantickej Rovnice ∑ j = 1 n 1 / x j = a / b \sum_{j=1}^{n}{1}/{x_{j}}={a}/{b} ’, *Časopis pro pěstování matematiky*, 98 (1973), 261–264.
- [4] P. Bartoš and K. Pehatzová-Bošanká. ‘K Riešeniu Diofantickej Rovnice 1 / x + 1 / y + 1 / z = a / b {1}/{x}+{1}/{y}+{1}/{z}={a}/{b} ’, *Časopis pro pěstování matematiky*, 96 (1971), 294–299.
- [5] M. Bello-Hernández, M. Benito, E. Fernández, ‘On egyptian fractions’, preprint, arXiv:1010.2035, version 2, 30. April 2012.
- [6] L. Bernstein, ‘Zur Lösung der diophantischen Gleichung m n = 1 x + 1 y + 1 z \frac{m}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}, insbesondere im Fall m = 4 m=4 ’, *J. Reine Angew. Math.*211, 1962, 1–10.
- [7] R. de la Bretéche, T. Browning, ‘Sums of arithmetic functions over values of binary forms’, *Acta Arith.*125 (2006), 291–304.
- [8] T. Browning, C. Elsholtz, ‘The number of representations of rationals as a sum of unit fractions’, to appear in Illinois Journal of Mathematics.
- [9] J. Brüdern. ‘Einführung in die analytische Zahlentheorie’. Springer, Berlin, Heidelberg, 1995.
- [10] Yong-Gao Chen, C. Elsholtz, Li-Li Jiang, ‘Egyptian fractions with restrictions’, *Acta Arith.*154 (2012), 109–123.
- [11] J-L. Colliot-Théelène, J-J. Sansuc, ‘Torseurs sous des groupes de type multiplicatif; applications á l’étude des points rationnels de certaines variétés algébriques’, *C. R. Acad. Sci. Paris Sér. A-B*282 (1976), no. 18, Aii, A1113–A1116.
- [12] E.S. Croot, D.E. Dobbs, J.B. Friedlander, A.J Hetzel, F. Pappalardi, ‘Binary Egyptian fractions’. *J. Number Theory*84 (2000), no. 1, 63–79.
- [13] S. Daniel, ‘Uniform bounds for short sums of certain arithmetic functions of polynomial arguments’, Unpublished manuscript.
- [14] P. D. T. A. Elliott, ‘Probabilistic number theory. II.’ Central limit theorems. Grundlehren der Mathematischen Wissenschaften, 240. Springer-Verlag, Berlin-New York, 1980.
- [15] C. Elsholtz, ‘Sums of k k unit fractions’, PhD thesis, Technische Universität Darmstadt, 1998.
- [16] C. Elsholtz, ‘Sums of k k unit fractions’ *Trans. Amer. Math. Soc.*353 (2001), 3209–3227.
- [17] C Elsholtz, C. Heuberger, H. Prodinger, ‘The number of Huffman codes, compact trees, and sums of unit fractions’, to appear in IEEE Trans. Inform. Theory.
- [18] P. Erdős, ‘Az 1 / x 1 + 1 / x 2 + … + 1 / x n = a / b {1}/{x_{1}}+{1}/{x_{2}}+\ldots+{1}/{x_{n}}={a}/{b} egyenlet egész számú megoldásairól’, *Mat. Lapok*1 (1950), 192–210.
- [19] P. Erdős, ‘On the sum ∑ k = 1 x d ⁡ ( f ⁡ ( k)) \sum_{k=1}^{x}d(f(k)) ’, *J. London Math. Soc.*27 (1952), 7–15.
- [20] P. Erdős, P.; R.L. Graham, ‘Old and new problems and results in combinatorial number theory’ *Monographies de L’Enseignement Mathématique*, 28. L’Enseignement Mathématique, Geneva, 1980. 128 pp.
- [21] É. Fouvry, ‘Sur le probléme des diviseurs de Titchmarsh’, *J. Reine Angew. Math.*357 (1985), 51–76.
- [22] É. Fouvry, H. Iwaniec, ‘The divisor function over arithmetic progressions’, With an appendix by Nicholas Katz. *Acta Arith.*61 (1992), no. 3, 271–287.
- [23] P. X. Gallagher, ‘Primes and Powers of two’, *Inventiones Math.*29 (1975), 125–142.
- [24] H. Gupta, ‘Selected topics in number theory.’ Abacus Press, Tunbridge Wells, 1980. 394 pp.
- [25] R. Guy, ‘Unsolved Problems in Number Theory’, 2nd ed. New York: Springer-Verlag, pp. 158-166, 1994.
- [26] H. Halberstam, H.-E. Richert, ‘On a result of R. R. Hall.’, *J. Number Theory*11 (1979), no. 1, 76–89.
- [27] R.R. Hall, ’Sets of Multiples’, Cambridge University Press, Cambridge, 1996.
- [28] D. R. Heath-Brown, ‘The density of rational points on Cayley’s cubic surface’, Proceedings of the Session in Analytic Number Theory and Diophantine Equations, 33 pp., Bonner Math. Schriften, 360, Univ. Bonn, Bonn, 2003.
- [29] K. Henriot, ‘Nair-Tenenbaum bounds uniform with respect to the discriminant’, Math. Proc. Camb. Phil. Soc. 152 (2012), no. 3, 405–424.
- [30] C. Hooley, ‘On the number of divisors of quadratic polynomials’, *Acta Math.*110 (1963), 97–114.
- [31] J. Huang, R. C. Vaughan, ‘Mean value theorems for binary Egyptian fractions’, *J. Number Theory*131 (2011), 1641–1656.
- [32] M. N. Huxley, ‘A note on polynomial congruences’, Recent Progress in Analytic Number Theory, Vol. I (H. Halberstam and C. Hooley, eds.), Academic Press, London, 1981, pp. 193-196.
- [33] H. Iwaniec, E. Kowalski, ‘Analytic number theory’, American Mathematical Society Colloquium Publications, 53. American Mathematical Society, Providence, RI, 2004.
- [34] C. Jia, ‘A Note on Terence Tao’s Paper “On the Number of Solutions to 4 / p = 1 / n 1 + 1 / n 2 + 1 / n 3 4/p=1/n_{1}+1/n_{2}+1/n_{3} ”’, preprint.
- [35] C. Jia, ‘ The estimate for mean values on prime numbers relative to 4 / p = 1 / n 1 + 1 / n 2 + 1 / n 3 4/p=1/n_{1}+1/n_{2}+1/n_{3} ’ *Science China Mathematics*55 (2012), no. 3, 465–474.
- [36] R.W. Jollenstein, ‘A note on the Egyptian problem’, *Congressus Numerantium, 17, Utilitas Math., Winnipeg, Man.*In Proceedings of the Seventh Southeastern Conference on Combinatorics, Graph Theory, and Computing, 351–364, Louisiana State Univ., Baton Rouge, La., 1976.
- [37] I. Kotsireas, ‘The Erdős-Straus conjecture on Egyptian fractions’, Paul Erdős and his mathematics (Budapest, 1999), 140–144, János Bolyai Math. Soc., Budapest, 1999.
- [38] B. Landreau, ‘A new proof of a theorem of van der Corput’, *Bull. London Math. Soc.*21 (1989), no. 4, 366–368.
- [39] Delang Li, ‘On the Equation 4 / n = 1 / x + 1 / y + 1 / z {4}/{n}={1}/{x}+{1}/{y}+{1}/{z} ’, *Journal of Number Theory*13 (1981), 485–494, 1981.
- [40] C. Mardjanichvili, ‘Estimation d’une somme arithmetique.’ *Comptes Rendus (Doklady) de l’Académie des Sciences de l’URSS*22 (1939), 387–389.
- [41] J. McKee, ‘On the average number of divisors of quadratic polynomials’, *Math. Proc. Cambridge Philos. Soc.*117 (1995), no. 3, 389–392.
- [42] J. McKee, ‘A note on the number of divisors of quadratic polynomials. Sieve methods, exponential sums, and their applications in number theory’ (Cardiff, 1995), 275–281, *London Math. Soc. Lecture Note Ser.*, 237, Cambridge Univ. Press, Cambridge, 1997.
- [43] J. McKee, ‘The average number of divisors of an irreducible quadratic polynomial’, *Math. Proc. Cambridge Philos. Soc.*126 (1999), no. 1, 17–22.
- [44] L. J. Mordell, ‘Diophantine Equations’, volume 30 of Pure and Applied Mathematics. Academic Press, 1969.
- [45] T. Nagell, ‘Généralisation d’un theórème de Tchebicheff’, *J. Math.*8 (1921), 343–356.
- [46] M. Nair, ‘Multiplicative functions of polynomial values in short intervals’, *Acta Arith.*62 (1992), no. 3, 257–269.
- [47] M. Nair, G. Tenenbaum, ‘Short sums of certain arithmetic functions’, *Acta Math.*180 (1998), 119–144.
- [48] M. Nakayama, ‘On the decomposition of a rational number into “Stammbrüche.”’, *Tôhoku Math. J.*46, (1939). 1–21.
- [49] M.R. Obláth, ‘Sur l’ équation diophantienne 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 {4}/{n}={1}/{x_{1}}+{1}/{x_{2}}+{1}/{x_{3}} ’, *Mathesis*59 (1950), 308–316.
- [50] O. Ore, ‘Anzahl der Wurzeln höherer Kongruenzen’, *Norsk Matematisk Tidsskrift*, 3 Aagang, Kristiana (1921), 343–356.
- [51] G. Palamà, ‘Su di una congettura di Sierpiński relativa alla possibilità in numeri naturali della 5 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 {5}/{n}={1}/{x_{1}}+{1}/{x_{2}}+{1}/{x_{3}} ’, *Bollettino della Unione Matematica Italiana (3)*, 13 (1958), 65–72.
- [52] G. Palamà, Su di una congettura di Schinzel, *Bollettino della Unione Matematica Italiana (3)*, 14 (1959), 82–94.
- [53] C. P. Popovici, ‘On the diophantine equation a / b = 1 / x 1 + 1 / x 2 + 1 / x 3 {a}/{b}={1}/{x_{1}}+{1}/{x_{2}}+{1}/{x_{3}} ’, *Analele Universitătii Bucureṣti. Seria Ṣtiinṭele Naturii. Matematică-Fizikă*10 (1961), 29–44, 1961.
- [54] C. Pomerance, ‘Analysis and Comparison of Some Integer Factoring Algorithms’, in *Computational Methods in Number Theory, Part I*, H.W. Lenstra, Jr. and R. Tijdeman, eds., Math. Centre Tract 154, Amsterdam, 1982, pp 89–139.
- [55] C. Pomerance, ‘Ruth-Aaron numbers revisited’, *Paul Erdős and his Mathematics*, I (Budapest, 1999), Bolyai Soc. Math. Stud. 11, János Bolyai Math. Soc., Budapest, 2002, pp. 567–579.
- [56] S. Ramanujan, ‘Highly composite numbers’, *Proc. London Math. Soc.*14 (1915), 347–409.
- [57] Y. Rav, ‘On the representation of rational numbers as a sum of a fixed number of unit fractions’, *J. Reine Angew. Math.*222 (1966), 207–213.
- [58] L. Rosati, ‘Sull’equazione diofantea 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 4/n=1/x_{1}+1/x_{2}+1/x_{3} ’, *Boll. Un. Mat. Ital.*(3) 9, (1954), 59–63.
- [59] J. Rosser, L. Schoenfeld, ‘Approximate formulas for some functions of prime numbers’, *Illinois J. Math.*6 (1962), 64–94.
- [60] I.Z. Ruzsa, ‘On an additive property of squares and primes’, *Acta Arithmetica*49 (1988), 281–289.
- [61] S. Salez, *The Erdős-Straus conjecture: New modular equations and checking up to N = 10 17 N=10^{17}*, preprint. arXiv:1406.6307
- [62] J.W. Sander, ‘On 4 / n = 1 / x + 1 / y + 1 / z {4}/{n}={1}/{x}+{1}/{y}+{1}/{z} and Rosser’s sieve’, Acta Arithmetica 59 (1991), 183–204.
- [63] J.W. Sander, ‘On 4 / n = 1 / x + 1 / y + 1 / z {4}/{n}={1}/{x}+{1}/{y}+{1}/{z} and Iwaniec’ Half Dimensional Sieve’, Journal of Number Theory 46 (1994), 123–136.
- [64] J.W. Sander, ‘Egyptian Fractions and the Erdős-Straus Conjecture.’ Nieuw Archief voor Wiskunde (4) 15 (1997), 43–50.
- [65] C. Sándor, ‘On the number of solutions of the Diophantine equation ∑ i = 1 n 1 x i = 1 \sum_{i=1}^{n}\frac{1}{x_{i}}=1 ’. *Period. Math. Hungar.*47 (2003), no. 1-2, 215–219.
- [66] G. Sándor, ‘Über die Anzahl der Lösungen einer Kongruenz’, *Acta. Math.*87 (1952), 13–17.
- [67] A. Schinzel, ‘Sur quelques propriétés des nombres 3 / n 3/n et 4 / n 4/n ’, où n n est un nombre impair. *Mathesis*65 (1956), 219–222.
- [68] A. Schinzel, ‘On sums of three unit fractions with polynomial denominators’, *Funct. Approx. Comment. Math.*28 (2000), 187–194.
- [69] W. Schwarz, J. Spilker, ‘Arithmetical functions’, *London Mathematical Society Lecture Note Series*, 184. Cambridge University Press, Cambridge, 1994.
- [70] E.J. Scourfield, ‘The divisors of a quadratic polynomial’, *Proc. Glasgow Math. Assoc.*5 (1961) 8–20.
- [71] A. Selberg, ‘Harmonic analysis and discontinuous groups in weakly symmetric Riemannian spaces with applications to Dirichlet series’, *J. Indian Math. Soc. (N.S.)*20 (1956), 47–87.
- [72] Shen Zun, ‘On the diophantine equation ∑ i = 0 k 1 / x i = a / n \sum_{i=0}^{k}{1}/{x_{i}}={a}/{n} ’, *Chinese Ann. Math. Ser. B*, 7 (1986), 213–220.
- [73] P. Shiu, ‘A Brun-Titchmarsh theorem for multiplicative functions’, *J. Reine Angew. Math.*313 (1980), 161–170.
- [74] W. Sierpiński, ‘Sur les décompositions de nombres rationnels en fractions primaires’, *Mathesis*65 (1956), 16–32.
- [75] W. Sierpiński. ‘On the Decomposition of Rational Numbers into Unit Fractions’, *Pánstwowe Wydawnictwo Naukowe*, Warsaw, 1957.
- [76] E. Sós. ‘Die diophantische Gleichung 1 / x = 1 / x 1 + 1 / x 2 + … + 1 / x n {1}/{x}={1}/{x_{1}}+{1}/{x_{2}}+\ldots+{1}/{x_{n}} ’, Zeitschrift für mathematischen und naturwissenschaftlichen Unterricht, 36 (1905), 97–102.
- [77] B.M. Stewart. Theory of Numbers. *2nd ed. New York: The Macmillan Company; London: Collier-Macmillan*, 1964.
- [78] C. L. Stewart, ‘On the number of solutions of polynomial congruences and Thue equations’, *J. Amer. Math. Soc.*4 (1991), no. 4, 793–835.
- [79] A. Swett, http://math.uindy.edu/swett/esc.htm accessed on 27 July 2011.
- [80] G. Tenenbaum, ‘Introduction to analytic and probabilistic number theory’, Cambridge Studies in Advanced Mathematics, 46. Cambridge University Press, Cambridge, 1995.
- [81] D.G. Terzi. ‘On a conjecture by Erdős-Straus’, Nordisk Tidskr. Informations-Behandling (BIT) 11 (1971), 212–216.
- [82] R. Vaughan, ‘On a problem of Erdős, Straus and Schinzel’, *Mathematika*17 (1970), 193–198.
- [83] C. Viola, ‘On the diophantine equations ∏ 0 k x i − ∑ 0 k x i = n \prod_{0}^{k}x_{i}-\sum_{0}^{k}x_{i}=n and ∑ 0 k 1 / x i = a / n \sum_{0}^{k}{1}/{x_{i}}={a}/{n} ’, *Acta Arith.*22 (1973), 339–352.
- [84] W. Webb, ‘On 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z ’, *Proc. Amer. Math. Soc.*25 (1970), 578–584.
- [85] W. Webb, ‘On a theorem of Rav concerning Egyptian fractions’, Canad. Math. Bull. 18 (1975), no. 1, 155–156.
- [86] W. Webb, ‘On the Diophantine equation k / n = a 1 / x 1 + a 2 / x 2 + a 3 / x 3 {k}/{n}={a_{1}}/{x_{1}}+{a_{2}}/{x_{2}}+{a_{3}}/{x_{3}} ’, *Časopis pro pěstováni matematiy, roč*, 101 (1976), 360–365.
- [87] A. Wintner, ‘Eratosthenian Averages’, Waverly Press, Baltimore, Md., 1943. v+81 pp.
- [88] K. Yamamoto, ‘On the Diophantine Equation 4 / n = 1 / x + 1 / y + 1 / z {4}/{n}={1}/{x}+{1}/{y}+{1}/{z} ’, *Mem Fac. Sci. Kyushu Univ. Ser. A, V.*19 (1965), 37–47.
- [89] Xun Qian Yang, ‘A note on 4 / n = 1 / x + 1 / y + 1 / z {4}/{n}={1}/{x}+{1}/{y}+{1}/{z} ’ Proceedings of the American Mathematical Society, 85 (1982), 496–498.

[◄][3][image: ar5iv homepage] [4]
[Feeling lucky?][5] [6]
[Conversion report][7]
[Report an issue][8]
[View original on arXiv][9] [►][10]


## Links

[1]: mailto:elsholtz@math.tugraz.at
[2]: mailto:tao@math.ucla.edu
[3]: /html/1107.1009
[4]: /
[5]: /feeling_lucky
[6]: /land_of_honey_and_milk
[7]: /log/1107.1010
[8]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1107.1010
[9]: https://arxiv.org/abs/1107.1010
[10]: /html/1107.1011
