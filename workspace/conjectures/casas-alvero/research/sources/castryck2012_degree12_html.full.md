<!-- source: https://arxiv.org/html/1208.5404v1 | converted from HTML -->

Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree 12

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1208.5404v1 [math.AG] 27 Aug 2012

# Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree 12 12

Wouter Castryck Robert Laterveer Myriam Ounaïes

###### Abstract

In a first (theoretical) part of this paper, we prove a number of constraints on hypothetical counterexamples to the Casas-Alvero conjecture, building on ideas of Graf von Bothmer, Labs, Schicho and van de Woestijne that were recently reinterpreted by Draisma and de Jong in terms of p p -adic valuations. In a second (computational) part, we present ideas improving upon Diaz-Toca and Gonzalez-Vega’s Gröbner basis approach to the Casas-Alvero conjecture. One application is an extension of the proof of Graf von Bothmer et al. to the cases 5 ​ p k 5p^{k}, 6 ​ p k 6p^{k} and 7 ​ p k 7p^{k} (that is, for each of these cases, we elaborate the finite list of primes p p for which their proof is not applicable). Finally, by combining both parts, we settle the Casas-Alvero conjecture in degree 12 12 (the smallest open case).

Files:`CAbadprimes.m``CAbadprimes7test.m``badprimes7.txt``CAdeg12.m`

## 1 Introduction and overview

( 1.1) The subject of this article is the following intriguing conjecture [3]:

###### Conjecture 1 (The Casas-Alvero conjecture, 2001).

Let f ⁡ ( x) ∈ ℂ ⁡ [x] f(x)\in\mathbb{C}[x] be of degree d > 0 d>0 and suppose that for each j = 1, …, d − 1 j=1,\dots,d-1 there exists an a ∈ ℂ a\in\mathbb{C} such that f ⁡ ( a) = f ( j) ​ ( a) = 0 f(a)=f^{(j)}(a)=0, where f ( j) ​ ( x) f^{(j)}(x) denotes the j j th derivative. Then f ⁡ ( x) f(x) is the d d th power of a linear polynomial.

For each given degree d d, proving Conjecture 1 (if true) boils down to a finite Gröbner basis computation. In 2006, this was used by Diaz-Toca and Gonzalez-Vega to verify the conjecture for d ≤ 7 d\leq 7 [5]. Shortly after, Graf von Bothmer, Labs, Schicho and van de Woestijne [7] proved a theoretical result settling the cases d = p k d=p^{k} and d = 2 ​ p k d=2p^{k} (where p p is prime and k ≥ 0 k\geq 0 is an integer). The proof uses reduction-mod- p p arguments in algebraic geometry. It was recently rewritten in the more elementary (and slightly more powerful) language of p p -adic valuations, in a nice overview due to Draisma and de Jong [6].

( 1.2) By lack of a general strategy, beyond the degree, we subdivide the set of hypothetical counterexamples f ⁡ ( x) f(x) to the Casas-Alvero conjecture by

- •

their number of distinct roots #​ roots ​ ( f) \#\text{roots}(f),

- •

their *type*type ​ ( f) \text{type}(f), which is the minimal number of recycled roots minus one

 | min { #S | S ⊂ ℂ and ∀ j: ∃ a ∈ S: f ( a) = f ( j) ( a) = 0 } − 1 \min\left\{\,\#S\,\left|\,S\subset\mathbb{C}\text{ and }\forall j:\exists\,a\in S:f(a)=f^{(j)}(a)=0\right.\,\right\}\,-\,1 |  |

where j j ranges over { 1, …, d − 1 } \{1,\dots,d-1\},

- •

their *scenario*scen ​ ( f) \text{scen}(f), which is

 | min { ( s 1, …, s d − 1) ∈ ℤ ≥ 0 d − 1 | ∃ a i ’s ∈ ℂ: ∀ j: f ( a s j) = f ( j) ( a s j) = 0 } \min\left\{\,\left.(s_{1},\dots,s_{d-1})\in\mathbb{Z}_{\geq 0}^{d-1}\,\right|\,\exists\,\text{$a_{i}$'s}\in\mathbb{C}:\forall j:f(a_{s_{j}})=f^{(j)}(a_{s_{j}})=0\,\right\} |  | (1) |

where the minimum is taken lexicographically and j j ranges over { 1, …, d − 1 } \{1,\dots,d-1\}. Note that type ​ ( f) \text{type}(f) is the maximal entry of scen ​ ( f) \text{scen}(f).

( 1.3) The scenario ( s 1, …, s d − 1) ∈ ℤ ≥ 0 d − 1 (s_{1},\dots,s_{d-1})\in\mathbb{Z}_{\geq 0}^{d-1} of a degree d d counterexample f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] to the Casas-Alvero conjecture always satisfies s 1 = 0 s_{1}=0 and s j ≤ max ⁡ { s i | i < j } + 1 s_{j}\leq\max\{\,s_{i}\,|\,i<j\,\}+1 for all j = 2, …, d − 1 j=2,\dots,d-1. A sequence of this form will therefore be called *a scenario for degree d d*. In view of the above, the *type*of a scenario is defined to be its maximal entry – we denote it by type ​ ( s) \text{type}(s). The number of scenarios for a given degree d d grows quickly with d d. E.g., in our main case of interest d = 12 d=12, we have

 | 1, 1023, 28501, 145750, 246730, 179487, 63987, 11880, 1155, 55, 1 1,1023,28501,145750,246730,179487,63987,11880,1155,55,1 |  |

scenarios of type 0, …, 10 0,\dots,10, respectively, amounting to a total of 678570 678570.

( 1.4) Let s = ( s 1, …, s d − 1) s=(s_{1},\dots,s_{d-1}) be a scenario for degree d d, and let t = type ​ ( s) t=\text{type}(s). Let f ⁡ ( x) ∈ ℂ ⁡ [x] f(x)\in\mathbb{C}[x] be a degree d d counterexample to the Casas-Alvero conjecture. Then we say that f ⁡ ( x) f(x)*matches with s s*if there exist a 0, …, a t ∈ ℂ a_{0},\dots,a_{t}\in\mathbb{C} such that

- •

f ( x) = g ( x) ⋅ ( x − a 0) ( x − a 1) ⋯ ( x − a t) f(x)=g(x)\cdot(x-a_{0})(x-a_{1})\cdots(x-a_{t}) for a degree d − 1 − t d-1-t polynomial g ⁡ ( x) ∈ ℂ ⁡ [x] g(x)\in\mathbb{C}[x],

- •

f ⁡ ( a s j) = f ( j) ​ ( a s j) = 0 f(a_{s_{j}})=f^{(j)}(a_{s_{j}})=0 for all j = 1, …, d − 1 j=1,\dots,d-1.

Clearly f ⁡ ( x) f(x) matches with its own scenario scen ​ ( f) \text{scen}(f), but it may also match with various other scenarios.

*Example.*Since it is conjecturally impossible to give examples over ℂ \mathbb{C}, consider f ⁡ ( x) = x ​ ( x − 1) 4 ​ ( x − 8) ​ ( x − 18) ∈ 𝔽 23 ​ [x] f(x)=x(x-1)^{4}(x-8)(x-18)\in\mathbb{F}_{23}[x]. One checks that the common roots of f f with f ( 1), …, f ( 6) f^{(1)},\dots,f^{(6)} are

 | { 1 }, { 1, 18 }, { 1 }, { 0 }, { 18 }, { 1 }, \{1\},\hskip 10.00002pt\{1,18\},\hskip 10.00002pt\{1\},\hskip 10.00002pt\{0\},\hskip 10.00002pt\{18\},\hskip 10.00002pt\{1\}, |  |

respectively. So type ​ ( f) = 2 \text{type}(f)=2 and scen ​ ( f) = ( 0, 0, 0, 1, 2, 0) \text{scen}(f)=(0,0,0,1,2,0) (take a 0 = 1, a 1 = 0, a 2 = 18 a_{0}=1,a_{1}=0,a_{2}=18). However, f ⁡ ( x) f(x) also matches with ( 0, 1, 0, 2, 1, 0) (0,1,0,2,1,0) (and many more).

( 1.5) In Section 2, we prove a number of general constraints on these attributes. E.g., we find that

- •

#​ roots ​ ( f) ≥ 5 \#\text{roots}(f)\geq 5,

- •

2 ≤ type ​ ( f) ≤ d − 3 2\leq\text{type}(f)\leq d-3 (the first inequality being due to Draisma and Knopper [6, Proposition 6]),

- •

if type ​ ( f) = d − 3 \text{type}(f)=d-3, then no consecutive entries of scen ​ ( f) \text{scen}(f) are equal.

The methods used here are classically flavoured (Gauss–Lucas, Newton, Rolle).

( 1.6) In Section 3, using the p p -adic valuation approach, we prove additional constraints for certain special degrees. Our main results are on degrees of the form p + 1 p+1:

###### Theorem 2.

Let p p be prime and let f ⁡ ( x) f(x) be a degree d = p + 1 d=p+1 counterexample to the Casas-Alvero conjecture. Let c c be the root of f ( d − 1) ​ ( x) f^{(d-1)}(x). Then f ( 1) ​ ( c) ≠ 0 f^{(1)}(c)\neq 0, and there exist at least two indices 2 ≤ j 1 < j 2 ≤ d − 2 2\leq j_{1}<j_{2}\leq d-2 such that f ( j 1) ​ ( c) = f ( j 2) ​ ( c) = 0 f^{(j_{1})}(c)=f^{(j_{2})}(c)=0. In particular, ​ t ​ y ​ p ​ e ​ ( f) ≤ d − 4 \emph{type}(f)\leq d-4. Moreover, if j 1 < ⋯ < j m j_{1}<\dots<j_{m} are the indices between 2 2 and d − 2 d-2 for which f ( d − j 1) ​ ( c) = ⋯ = f ( d − j m) ​ ( c) = 0 f^{(d-j_{1})}(c)=\dots=f^{(d-j_{m})}(c)=0, then the determinant of

 | Δ f = [− 1 j 1 0 0 ⋯ 0 − 1 ( j 2 − 2 j 1 − 2) ​ j 2 j 2 0 ⋯ 0 ⋮ ⋮ ⋮ ⋮ ⋮ − 1 ( j m − 2 j 1 − 2) ​ j m ( j m − 2 j 2 − 2) ​ j m ⋯ j m − 1 ( − 1) j 1 ( − 1) j 2 ⋯ ( − 1) j m] \Delta_{f}=\left[\begin{array}[]{c c c c c c }-1&j_{1}&0&0&\cdots&0\\ -1&\binom{j_{2}-2}{j_{1}-2}j_{2}&j_{2}&0&\cdots&0\\ \vdots&\vdots&\vdots&\vdots&&\vdots\\ -1&\binom{j_{m}-2}{j_{1}-2}j_{m}&\binom{j_{m}-2}{j_{2}-2}j_{m}&&\cdots&j_{m}\\ -1&(-1)^{j_{1}}&(-1)^{j_{2}}&&\cdots&(-1)^{j_{m}}\end{array}\right] |  | (2) |

is a multiple of p p.

Theorem 2 implies that every degree d = p + 1 d=p+1 counterexample to the Casas-Alvero conjecture matches with an element of the strongly reduced list of scenarios s = ( s 1, …, s d − 1) s=(s_{1},\dots,s_{d-1}) for which

- •

s d − 1 ≠ 0 s_{d-1}\neq 0,

- •

the set of indices 2 ≤ j ≤ d − 2 2\leq j\leq d-2 for which s d − j = s d − 1 s_{d-j}=s_{d-1} satisfies the above determinant condition.

For d = 12 d=12 ( p = 11 p=11), the list contains

 | 0, 48, 1668, 8172, 11586, 6298, 1469, 146, 5, 0, 0 0,48,1668,8172,11586,6298,1469,146,5,0,0 |  | (3) |

scenarios of type 0, …, 10 0,\dots,10, respectively, amounting to a total of 29392 29392. In type 8 8, the five scenarios read

 | ( 0, 1, 2, 3, 4, 5, 6, 7, 3, 8, 3), ( 0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 5), ( 0, 1, 2, 3, 4, 3, 5, 6, 7, 8, 3), ( 0, 1, 2, 3, 4, 2, 5, 6, 7, 8, 2), ( 0, 1, 2, 3, 2, 4, 5, 6, 7, 8, 2); \begin{array}[]{l}(0,1,2,3,4,5,6,7,3,8,3),\\ (0,1,2,3,4,5,5,6,7,8,5),\\ (0,1,2,3,4,3,5,6,7,8,3),\\ (0,1,2,3,4,2,5,6,7,8,2),\\ (0,1,2,3,2,4,5,6,7,8,2);\\ \end{array} |  | (4) |

indeed, the only pairs ( j 1, j 2) (j_{1},j_{2}) for which Δ f ≡ 0 mod 11 \Delta_{f}\equiv 0\bmod 11 are ( 3, 8) (3,8), ( 5, 6) (5,6), ( 6, 8) (6,8), ( 6, 9) (6,9), ( 7, 9) (7,9).

( 1.7) For the computational part of our paper, we turn back to the original reduction-mod- p p setting used by Graf von Bothmer et al. Because of the interplay between characteristic 0 0 and characteristic p > 0 p>0, the following general definition is convenient.

###### Definition 1.

Let k k be an algebraically closed field. We say that a degree d d polynomial f ∈ k ⁡ [x] f\in k[x] ( d > 0 d>0) is a *Casas-Alvero polynomial*or *CA-polynomial*(over k k) if f f is not a power of a linear polynomial and if for each j = 1, …, d − 1 j=1,\dots,d-1 there exists an a ∈ k a\in k such that f ⁡ ( a) = f H ( j) ​ ( a) = 0 f(a)=f^{(j)}_{H}(a)=0.

Here, f H ( j) f^{(j)}_{H} denotes the j j th Hasse derivative (using Hasse derivatives turns the Casas-Alvero condition somewhat more restrictive – it makes no difference in characteristic 0 0 or p > d − 1 p>d-1, where f H ( j) = 1 j! ​ f ( j) f^{(j)}_{H}=\frac{1}{j!}f^{(j)}). Then the main theorem of [7] reads:

###### Theorem 3 (Graf von Bothmer, Labs, Schicho, van de Woestijne).

Let d > 0 d>0 be an integer and let p p be a prime number. If no CA-polynomials of degree d d exist over 𝔽 ¯ p \overline{\mathbb{F}}_{p}, then the Casas-Alvero conjecture is true in degree d ​ p k dp^{k} for all integers k ≥ 0 k\geq 0.

Since it is trivial that no CA-polynomials of degree 1 1 or 2 2 can exist (in any characteristic), the cases p k p^{k} and 2 ​ p k 2p^{k} follow. More generally, we call a prime p p a *bad prime for degree d d*if there exist CA-polynomials of degree d d in characteristic p p. Then it is easily verified that p = 2 p=2 is the sole bad prime for degree d = 3 d=3. De Jong and Draisma [6] proved that the bad primes for degree d = 4 d=4 are p = 3, 5, 7 p=3,5,7.

( 1.8) In Section 5 we present an algorithm, the basic version of which takes as input an integer d > 0 d>0 and a prime number p p (or p = 0 p=0), and outputs whether or not CA-polynomials of degree d d exist in characteristic p p. The basic idea is to classify all CA-polynomials by their scenario (the definitions in ( 1.2) straightforwardly generalize to arbitrary k k – this was already used in the example in ( 1.4) there under). We will see that scenarios of moderately low type t t can be ruled out easily (if the Casas-Alvero conjecture is true). In characteristic 0 0, the computation is feasible up to d ⋅ t ≈ 50 d\cdot t\approx 50, say. In moderate characteristic p p, this can be pushed to about twice that value.

( 1.9) By running the algorithm in characteristic 0 0 and analyzing the prime factors appearing in certain resulting Nullstellensatz expansions, we can find the bad primes for d d up to 7 7.

###### Theorem 4.

There are

- •

9 9 bad primes for degree d = 5 d=5, namely,

 | p = 2, 3, 7, 11, 131, 193, 599, 3541, and ​ 8009, p=2,3,7,11,131,193,599,3541,\text{and }8009, |  |

- •

53 53 bad primes for degree d = 6 d=6, namely, the primes listed in Table 1,

- •

366 366 bad primes for degree d = 7 d=7, namely, the primes listed in the file `badprimes7.txt`that accompanies this paper – the smallest non-bad prime (apart from p = 7 p=7) is 127 127 – the largest bad prime is

24984712021698392647916525667237483011737174983678606896870094983849 9096141806825287856933123954724798488422551659890912229726792102063 \begin{array}[]{l}24984712021698392647916525667237483011737174983678606896870094983849\\ 9096141806825287856933123954724798488422551659890912229726792102063\\ \end{array}

(a 135 135 -digit number).

2 | 5 | 7 | 11 |

13 | 19 | 23 | 29 |

37 | 47 | 61 | 67 |

73 | 97 | 257 | 811 |

983 | 1069 | 1087 | 1187 |

1487 | 1499 | 1901 | 2287 |

3209 | 3877 | 3881 | 4019 |

4943 | 5471 | 6983 | 8699 |

9337 | 15131 | 15823 | 20771 |

21379 | 23993 | 150203 | 266587 |

547061 | 685177 | 885061 | 1030951 |

7783207 | 17250187 | 40362599 | 9348983563 |

70016757407 | 2610767527031 | 225833117528659 | 7390044713023799 |

51313000813080529 |  |  |  |

Table 1: Bad primes for degree 6 6 ( 53 53 primes)

We note that the bad primes for d = 5 d=5 have been independently elaborated (by hand) by Chellali and Salinier [4].

( 1.10) Finally in Section 6, we combine our theoretical and computational approaches. Naively running our algorithm in degree 12 12 lies completely out of reach. But in view of Theorem 2 and certain reduction-mod- p p considerations, it suffices to restrict the algorithm to a limited list of scenarios, and to run it in characteristic p p. As such, the computation becomes feasible:

###### Theorem 5.

Conjecture 1 is true for d = 12 d=12.

The margin is tight: each of the five scenarios of ( 4) took approximately three weeks of computation and required about 90 90 GB of RAM. Pushing the analogous computation to d = 20 d=20, the next open case, is utopic.

( 1.11) The main computations have been carried out using Magma [2] version 2.18-2 on a computer called `matrix`, running Ubuntu 11.10 on a 6 6 -core Intel Xeon 2.53 GHz processor with 96 GB RAM. Some additional calculations were executed using Magma version 2.15-12 on `kasparov`, running Debian GNU/Linux 6.0.4 on an 8 8 -core x86-64 2.93 GHz processor with 64 GB RAM.

( 1.12) We would like to thank Filip Cools, Jan Schepers and Fréderik Vercauteren for some helpful discussions. We are also grateful to the Department of Electrical Engineering (KU Leuven), for allowing us to use `kasparov`.

## 2 General constraints on counterexamples

( 2.1) The following easy fact will be used throughout:

###### Lemma 6.

Let f f be a CA-polynomial over k k of degree d > 0 d>0, α 1, α 2 ∈ k ∗ \alpha_{1},\alpha_{2}\in k^{*} and β ∈ k \beta\in k. Then the polynomial g ⁡ ( x) = α 1 ​ f ​ ( α 2 ​ x + β) g(x)=\alpha_{1}f(\alpha_{2}x+\beta) is also CA.

The polynomials f f and g g will be called *equivalent*. Note that the number of distinct roots, the type, the scenario, the matching or not with a given scenario, … are all preserved by equivalence.

( 2.2) We begin with some considerations on the type:

###### Proposition 7.

Let f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] be a CA-polynomial of degree d d and let Γ \Gamma be the convex hull of the roots of f f (when plotted in the complex plane). Let m ≥ 2 m\geq 2 be the maximum of the multiplicities of these roots, and let δ = 1 \delta=1 if this maximum is attained by a non-vertex of Γ \Gamma (let δ = 0 \delta=0 otherwise). Let γ ≥ 2 \gamma\geq 2 be the number of vertices of Γ \Gamma. Then 2 ≤ ​ t ​ y ​ p ​ e ​ ( f) ≤ d + 1 − γ − m − δ ≤ d − 3 2\leq\emph{type}(f)\leq d+1-\gamma-m-\delta\leq d-3.

Proof: For each vertex v v of Γ \Gamma we have:

- •

f ( j) ​ ( v) ≠ 0 f^{(j)}(v)\neq 0 for all j = 1, …, d − 1 j=1,\dots,d-1, or

- •

v v has multiplicity at least 2 2

(by the Gauss–Lucas theorem). This means that among the d d roots of f f, counting multiplicities, at least γ \gamma of them are not needed to find a common root for each derivative. If δ = 1 \delta=1, some non-vertex has multiplicity m m, so another m − 1 m-1 roots are superfluous. Therefore, at most d − γ − ( m − 1) d-\gamma-(m-1) roots are needed. If δ = 0 \delta=0, then the bound reads d − ( γ − 1) − ( m − 1) d-(\gamma-1)-(m-1). In both cases, the upper bound for type ​ ( f) \text{type}(f) follows. The lower bound follows from an observation by Draisma and Knopper [6, Proposition 6]. ■ \blacksquare

Refining to the level of scenarios, we find:

###### Proposition 8.

Let d > 2 d>2 be an integer and let s = ( s 1, s 2, …, s d − 1) s=(s_{1},s_{2},\dots,s_{d-1}) be a scenario for degree d d. If

1. 1.

​ t ​ y ​ p ​ e ​ ( s) ∈ { 0, 1, d − 2 } \emph{type}(s)\in\{0,1,d-2\}, or

2. 2.

​ t ​ y ​ p ​ e ​ ( s) ≤ d − 3 \emph{type}(s)\leq d-3, the first d − 2 − ​ t ​ y ​ p ​ e ​ ( s) d-2-\emph{type}(s) entries of s s are zero, and among s d − 1 − ​ t ​ y ​ p ​ e ​ ( s), …, s d − 1 s_{d-1-\emph{type}(s)},\dots,s_{d-1} there is a zero or two consecutive entries that are equal,

then there are no CA-polynomials f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] for which ​ s ​ c ​ e ​ n ​ ( f) = s \emph{scen}(f)=s.

Proof: The first part is an immediate corollary to Proposition 7. As for the second statement, suppose to the contrary that f f is a CA-polynomial for which scen ​ ( f) = s \text{scen}(f)=s, with t = type ​ ( s) ≤ d − 3 t=\text{type}(s)\leq d-3 and the first d − 2 − type ​ ( s) d-2-\text{type}(s) entries of s s equal to zero. Let a 0, …, a t ∈ ℂ a_{0},\dots,a_{t}\in\mathbb{C} be as in ( 1). Then a 0 a_{0} is a root with multiplicity at least d − 1 − t d-1-t. Let Γ \Gamma be the convex hull of the roots of f f and let γ \gamma be its number of vertices. Using Proposition 7, we conclude that γ = 2 \gamma=2 and that a 0 a_{0} is a vertex. Then if another 0 0 would appear in s = scen ​ ( f) s=\text{scen}(f), by Gauss–Lucas we would conclude that the multiplicity of a 0 a_{0} is strictly bigger than d − 1 − t d-1-t, which would contradict Proposition 7. On the other hand, if two consecutive entries would be equal, some high-order derivative of f ⁡ ( x) f(x) would have a double root. But since γ = 2 \gamma=2, f ⁡ ( x) f(x) is equivalent to a real-root polynomial, so Rolle’s theorem would imply that this double root is actually a root of f ⁡ ( x) f(x) with multiplicity strictly bigger than d − t d-t, again contradicting Proposition 7. ■ \blacksquare

*Remark.*Let s s be as in the énoncé of Proposition 8. Then one cannot merely conclude (without using new arguments, that is) the stronger statement that there are no CA-polynomials f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] that *match*with s s.

( 2.3) As immediate corollaries to the lower bound 2 ≤ type ​ ( f) 2\leq\text{type}(f), we get the following three easy facts: if f f is a CA-polynomial (over ℂ \mathbb{C}) of degree d d, then

1. 1.

f ( 2) ​ ( x) f^{(2)}(x) cannot be the ( d − 2) (d-2) th power of a linear polynomial,

2. 2.

f f cannot have a root of multiplicity at least d − 1 d-1,

3. 3.

f f has at least three distinct roots

(note that these statements can be proved in various other ways, see e.g. [12, Proposition 2.2]). In the next two propositions, we will go a step further in directions 1 and 2. Later on (Proposition 12 and Theorem 13), we will go two steps further in direction 3.

###### Proposition 9.

If f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] is a CA-polynomial of degree d d, then f ( 3) ​ ( x) f^{(3)}(x) cannot be the ( d − 3) (d-3) th power of a linear polynomial.

Proof: Suppose to the contrary that f ( 3) ​ ( x) f^{(3)}(x) is the ( d − 3) (d-3) th power of a linear polynomial. Thanks to Lemma 6, we may assume f ( 3) ​ ( x) = d! ( d − 3)! ​ x d − 3 f^{(3)}(x)=\frac{d!}{(d-3)!}x^{d-3}. Assume that f ( 1) ​ ( 0) ≠ 0 f^{(1)}(0)\not=0, then f f has a root of multiplicity at least 2 2 which is different from 0 0 and again by Lemma 6, we may assume f ⁡ ( 1) = f ( 1) ​ ( 1) = 0 f(1)=f^{(1)}(1)=0. Thus

 | f ⁡ ( x) = x d − ( d − 1) ​ x 2 + ( d − 2) ​ x; f ( 2) ​ ( x) = ( d − 1) ​ ( d ​ x d − 2 − 2). f(x)=x^{d}-(d-1)x^{2}+(d-2)x;\ \ f^{(2)}(x)=(d-1)\left(dx^{d-2}-2\right). |  |

Solving f ⁡ ( x) = f ( 2) ​ ( x) = 0 f(x)=f^{(2)}(x)=0, we get x = d d + 1 x=\frac{d}{d+1} and ( d + 1 d) d − 2 = d 2 (\frac{d+1}{d})^{d-2}=\frac{d}{2}. We easily see that the function ϕ ⁡ ( t) = ( t − 2) ​ ln ⁡ t + 1 t − ln ⁡ t 2 \phi(t)=(t-2)\ln\frac{t+1}{t}-\ln\frac{t}{2} is strictly decreasing for t ≥ 4 t\geq 4 and that ϕ ⁡ ( 4) < 0 \phi(4)<0. Thus the equality ϕ ⁡ ( d) = 0 \phi(d)=0 is never reached for d ≥ 4 d\geq 4. We conclude that we necessarily have f ( 1) ​ ( 0) = 0 f^{(1)}(0)=0. Then, for some constant c c, f ( 2) ​ ( x) = d ⁡ ( d − 1) ​ x d − 2 + 2 ​ c f^{(2)}(x)=d(d-1)x^{d-2}+2c and f ⁡ ( x) = x d + c ​ x 2 f(x)=x^{d}+cx^{2}. Solving f ⁡ ( x) = f ( 2) ​ ( x) = 0 f(x)=f^{(2)}(x)=0, we get that c = 0 c=0. ■ \blacksquare

###### Proposition 10.

Let f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] be a CA-polynomial of degree d d, then f f cannot have a root of multiplicity at least d − 2 d-2.

Proof: Suppose that 0 0 is such a root. If f ( d − 1) ​ ( 0) ≠ 0 f^{(d-1)}(0)\not=0, then we may assume that f ⁡ ( 1) = f ( d − 1) ​ ( 1) = 0 f(1)=f^{(d-1)}(1)=0 and

 | f ⁡ ( x) = x d − 2 ​ ( x 2 − d ​ x + d − 1), f ( d − 2) ​ ( x) = ( d − 1)! 2 ​ ( d ​ x 2 − 2 ​ d ​ x + 2). f(x)=x^{d-2}(x^{2}-dx+d-1),\ \ f^{(d-2)}(x)=\frac{(d-1)!}{2}(dx^{2}-2dx+2). |  |

Solving f ⁡ ( x) = f ( d − 2) ​ ( x) = 0 f(x)=f^{(d-2)}(x)=0, we get x 2 = 2 x^{2}=2 and x = d + 1 d x=\frac{d+1}{d}. Thus ( d + 1) 2 = 2 ​ d 2 (d+1)^{2}=2d^{2} which is impossible. We conclude that we necessarily have f ( d − 1) ​ ( 0) = 0 f^{(d-1)}(0)=0. Then, for some constant c c, f ⁡ ( x) = x d + c ​ x d − 2 f(x)=x^{d}+cx^{d-2} and f ( d − 2) ​ ( x) = d! 2 ​ x 2 + c f^{(d-2)}(x)=\frac{d!}{2}x^{2}+c. Solving f ⁡ ( x) = f ( d − 2) ​ ( x) = 0 f(x)=f^{(d-2)}(x)=0, we get c = 0 c=0. ■ \blacksquare

We have chosen to present an elementary proof of Proposition 10, though we also can see it as a direct consequence of the forthcoming Proposition 12.

( 2.4) Let us recall some basic properties of the elementary symmetric polynomials. Let a polynomial f f and its derivatives be of the form

 | f ( j) ​ ( x) = d! ( d − j)! ​ ( x d − j + ( d − j 1) ​ a 1 ​ x d − j − 1 + ( d − j 2) ​ a 2 ​ x d − j − 2 + ⋯ + a d − j) f^{(j)}(x)=\frac{d!}{(d-j)!}(x^{d-j}+{{d-j}\choose 1}a_{1}x^{d-j-1}+{{d-j}\choose 2}a_{2}x^{d-j-2}+\cdots+a_{d-j}) |  |

(here by convention f = f ( 0) f=f^{(0)}). Let σ m ​ ( j) \sigma_{m}(j) be the sum of the m m th powers of the roots of f ( j) f^{(j)}, for j = 0, ⋯, d − 1 j=0,\cdots,d-1. Then Newton’s formulas applied to each f ( j) f^{(j)} give the following relations (see for example [10] for more details on Newton formulas):

###### Lemma 11.

 | ∑ k = 1 r σ k ​ ( j) ​ ( d − j r − k) ​ a r − k = − r ​ ( d − j r) ​ a r \sum_{k=1}^{r}\sigma_{k}(j){{d-j}\choose{r-k}}a_{r-k}=-r{{d-j}\choose r}a_{r} |  |

for 0 ≤ j ≤ d − 1 0\leq j\leq d-1, 1 ≤ r ≤ d − j 1\leq r\leq d-j. (It is understood that a 0 = 1 a_{0}=1.)

In particular, for r = 1 r=1, we have that

 | σ 1 ​ ( j) d − j = σ 1 ​ ( 0) d \displaystyle\frac{\sigma_{1}(j)}{d-j}=\frac{\sigma_{1}(0)}{d} |  |

for j = 0, …, d − 1 j=0,\dots,d-1, which means that the center of mass of the roots of the derivatives is fixed. As obviously

 | σ 1 ​ ( d − 1) = σ 1 ​ ( 0) d = − a 1 \displaystyle\sigma_{1}(d-1)=\frac{\sigma_{1}(0)}{d}=-a_{1} |  |

is the only root of f ( d − 1) f^{(d-1)}, we see that whenever f f is a CA-polynomial over ℂ \mathbb{C}, the center of mass of its roots σ 1 ​ ( 0) d \displaystyle\frac{\sigma_{1}(0)}{d} is itself a root of f f. As a direct consequence, the number of distinct roots of a CA-polynomial cannot be two. Actually, we can say more: if f f has more than two distinct roots, then at least one of them (the center of mass) has to be in the interior of the convex hull of the roots. This fact also follows immediately from the Gauss–Lucas theorem, and can be pushed further:

###### Proposition 12.

Let f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] be a CA-polynomial. Then f f has at least two distinct roots in the interior of the convex hull of the roots, when plotted in the complex plane. In particular, f f has at least four distinct roots.

Proof: Assume that f f has exactly one root, say 0 0, in the interior. Let ζ \zeta be among the roots of f f located on the boundary with maximal multiplicity m m. Then by Gauss–Lucas, f ( m) ​ ( 0) = f ( m + 1) ​ ( 0) = ⋯ = f ( d − 1) ​ ( 0) = 0 f^{(m)}(0)=f^{(m+1)}(0)=\cdots=f^{(d-1)}(0)=0 which means that for j = m, …, d − 1 j=m,\ldots,d-1:

 | f ( j) ​ ( x) = d! ( d − j)! ​ x d − j. \displaystyle f^{(j)}(x)=\frac{d!}{(d-j)!}x^{d-j}. |  |

Taylor expansion gives

 | f ⁡ ( 0) = ∑ j = m d f ( j) ​ ( ζ) j! ​ ( − ζ) j = ζ d ​ ∑ j = m d ( − 1) j ​ ( d j) = ζ d ​ ( − 1) m ​ ( d − 1 m − 1). f(0)=\sum_{j=m}^{d}\frac{f^{(j)}(\zeta)}{j!}(-\zeta)^{j}=\zeta^{d}\sum_{j=m}^{d}(-1)^{j}{d\choose j}=\zeta^{d}(-1)^{m}{{d-1}\choose{m-1}}. |  |

As f ⁡ ( 0) = 0 f(0)=0, we get ζ = 0 \zeta=0, which is a contradiction. ■ \blacksquare

Note that Proposition 12 can also be deduced directly from 2 ≤ type ​ ( f) 2\leq\text{type}(f).

( 2.5) We now prove the main result of this section:

###### Theorem 13.

Let f f be a CA-polynomial over ℂ \mathbb{C}, then f f has at least five distinct roots.

Proof: Assume that f f has four distinct roots. Then by the previous proposition, it has at least two distinct roots in the interior of its Gauss–Lucas hull. This implies that the four roots are on a line. By Lemma 6, we may assume that this is the real line. We denote by m m the maximal multiplicity of the roots of f f. By Proposition 10, we know that 2 ≤ m ≤ d − 3 2\leq m\leq d-3.

- •

First case: m ≤ d − 5 m\leq d-5. Again using Lemma 6, we may assume without loss of generality that the roots of f f are as follows : a < 0 < 1 < b a<0<1<b and f ( d − 1) ​ ( 0) = 0 f^{(d-1)}(0)=0. Then a a and b b cannot be zeros of f ( j) f^{(j)} for d − 5 ≤ j ≤ d − 1 d-5\leq j\leq d-1. Moreover, by Rolle’s theorem, each zero of f ( j) f^{(j)} is simple. Then we necessarily have f ( d − 2) ​ ( 1) = 0, f ( d − 3) ​ ( 0) = 0, f ( d − 4) ​ ( 1) = 0, f ( d − 5) ​ ( 0) = 0 f^{(d-2)}(1)=0,\ f^{(d-3)}(0)=0,\ f^{(d-4)}(1)=0,\ f^{(d-5)}(0)=0. Integrating five times the expression f ( d − 1) ​ ( x) = d! ​ x f^{(d-1)}(x)=d!x and taking into account these constraints, we get f ( d − 5) ​ ( x) = d! 5! ​ x ​ ( x 2 − 5) 2 \displaystyle f^{(d-5)}(x)=\frac{d!}{5!}x(x^{2}-5)^{2}. But this contradicts the fact that the roots are simple.

- •

Second case: m = d − 4 m=d-4. In view of Lemma 6, we arrange the roots as follows : a < 0 < b < 1 a<0<b<1 and we assume that f ( d − 1) ​ ( 0) = 0 f^{(d-1)}(0)=0. Denote by m a, m 0, m b, m 1 m_{a},\ m_{0},\ m_{b},\ m_{1} their respective multiplicities. Then again we must have f ( d − 2) ​ ( b) = 0 f^{(d-2)}(b)=0, f ( d − 3) ​ ( 0) = 0 f^{(d-3)}(0)=0, f ( d − 4) ​ ( b) = 0 f^{(d-4)}(b)=0. Like in the first case, computing the last derivatives, we get

 | f ( d − 1) ( x) = d! x, 2! f ( d − 2) ( x) = d! ( x 2 − b 2), 3! f ( d − 3) ( x) = d! x ( x 2 − 3 b 2), 4! f ( d − 4) ( x) = d! ( x 2 − 5 b 2) ( x 2 − b 2). \begin{split}&f^{(d-1)}(x)=d!x,\ \ \ 2!f^{(d-2)}(x)=d!(x^{2}-b^{2}),\\ &3!f^{(d-3)}(x)=d!x(x^{2}-3b^{2}),\ \ 4!f^{(d-4)}(x)=d!(x^{2}-5b^{2})(x^{2}-b^{2}).\end{split} |  |

Obviously, as f ( d − 4) ​ ( b) = 0 f^{(d-4)}(b)=0, we have m b ≤ d − 5 m_{b}\leq d-5. From the Gauss–Lucas theorem, we deduce that a < − 5 ​ b a<-\sqrt{5}b. Now we apply Lemma 11 with j = 0 j=0, r = 1 r=1 and with j = 0 j=0, r = 3 r=3 to obtain

 | m a ​ a + m b ​ b + m 1 = m a ​ a 3 + m b ​ b 3 + m 1 = 0. m_{a}a+m_{b}b+m_{1}=m_{a}a^{3}+m_{b}b^{3}+m_{1}=0. |  | (5) |

We deduce that m a ​ a ​ ( a 2 − 1) = − m b ​ b ​ ( b 2 − 1) m_{a}a(a^{2}-1)=-m_{b}b(b^{2}-1) and looking at the sign, we see that − a < 1 -a<1. Then m a > − a ​ m a = m b ​ b + m 1 > m 1 m_{a}>-am_{a}=m_{b}b+m_{1}>m_{1} which implies that m a ≥ 2 m_{a}\geq 2 and m 1 ≤ d − 5 m_{1}\leq d-5. Now in the case where m a = 2, m 1 = m b = 1 m_{a}=2,m_{1}=m_{b}=1, equations ( 5) give a ​ ( a + 1) 2 = 0 a(a+1)^{2}=0. Thus this case cannot occur. We can readily deduce that m 0 ≤ d − 5 m_{0}\leq d-5. The only possibility left is m a = m = d − 4 m_{a}=m=d-4.

From the relation − ( d − 4) ​ a ​ ( 1 − a 2) = m b ​ b ​ ( 1 − b 2) -(d-4)a(1-a^{2})=m_{b}b(1-b^{2}), we deduce that ϕ ⁡ ( − a) ≤ ϕ ⁡ ( b) \phi(-a)\leq\phi(b) where we put ϕ ⁡ ( t) = t ⁡ ( 1 − t 2) \phi(t)=t(1-t^{2}). But ϕ \phi is increasing on [0, 1 / 3] [0,1/\sqrt{3}] and we know that − a > b > 0 -a>b>0. Thus we have − a > 1 / 3 -a>1/\sqrt{3}. Now we get back to the linear equation in ( 5):

 | d − 4 = m b ​ b − a + m 1 ​ 1 − a < m b 5 + m 1 ​ 3 < 4. d-4=m_{b}\frac{b}{-a}+m_{1}\frac{1}{-a}<\frac{m_{b}}{\sqrt{5}}+m_{1}\sqrt{3}<4. |  |

Since the Casas-Alvero conjecture is true for d ≤ 7 d\leq 7, this is a contradiction.

- •

Third case: m = d − 3 m=d-3. We proceed as in the previous case. We have

 | f ( d − 1) ​ ( x) = d! ​ x, 2! ​ f ( d − 2) ​ ( x) = d! ​ ( x 2 − b 2), 3! ​ f ( d − 3) ​ ( x) = d! ​ x ​ ( x 2 − 3 ​ b 2). f^{(d-1)}(x)=d!x,\ \ \ 2!f^{(d-2)}(x)=d!(x^{2}-b^{2}),3!f^{(d-3)}(x)=d!x(x^{2}-3b^{2}). |  |

From Gauss–Lucas we deduce that a < − 3 ​ b a<-\sqrt{3}b. Again, we obtain that m a ≥ 2 m_{a}\geq 2. Thus we necessarily have: m a = m m_{a}=m, m 0 = m 1 = m b = 1 m_{0}=m_{1}=m_{b}=1. The linear equation in ( 5) gives

 | d − 3 = b − a + 1 − a < 1 3 + 3 < 3, d-3=\frac{b}{-a}+\frac{1}{-a}<\frac{1}{\sqrt{3}}+\sqrt{3}<3, |  |

again a contradiction. ■ \blacksquare

## 3 Additional constraints for special degrees

( 3.1) We now turn our attention to certain special instances of d d, in each case involving a prime number p p. Inspired by Draisma and de Jong’s take [6], we use p p -adic valuations. Most of the proofs below have straightforward analogs in the original reduction-mod- p p setting of Graf von Bothmer et al. But at some points, the valuation language does seem slightly more powerful. Our starting point is the existence of a map

 | v p: ℂ → ℚ ∪ { + ∞ } v_{p}\,:\,\mathbb{C}\,\rightarrow\,\mathbb{Q}\cup\{+\infty\} |  |

satisfying

- •

v p ​ ( a) = + ∞ v_{p}(a)=+\infty if and only if a = 0 a=0,

- •

v p ​ ( a ​ b) = v p ​ ( a) + v p ​ ( b) v_{p}(ab)=v_{p}(a)+v_{p}(b) for all a, b ∈ ℂ a,b\in\mathbb{C},

- •

v p ​ ( a + b) ≥ min ⁡ { v p ​ ( a), v p ​ ( b) } v_{p}(a+b)\geq\min\{v_{p}(a),v_{p}(b)\} for all a, b ∈ ℂ a,b\in\mathbb{C},

and extending the usual p p -adic valuation on ℤ \mathbb{Z} (i.e. if n = p r ⋅ n ′ n=p^{r}\cdot n^{\prime} with n ′ n^{\prime} prime to p p, then v p ​ ( n) = r v_{p}(n)=r). See e.g. [11, Chapter 4, Theorem 1]. It is important to note that the last property implies v p ​ ( a + b) = min ⁡ { v p ​ ( a), v p ​ ( b) } v_{p}(a+b)=\min\{v_{p}(a),v_{p}(b)\} if v p ​ ( a) ≠ v p ​ ( b) v_{p}(a)\not=v_{p}(b). We will make a frequent use of this fact.

( 3.2) The p p -adic valuations of binomial coefficients are well-understood. A formula due to Legendre [9] states that for any n ∈ ℤ > 0 n\in\mathbb{Z}_{>0} and any j ∈ { 0, …, n } j\in\{0,\dots,n\} one has

 | v p ​ ( n j) = s p ​ ( j) + s p ​ ( n − j) − s p ​ ( n) p − 1, v_{p}{n\choose j}=\frac{s_{p}(j)+s_{p}(n-j)-s_{p}(n)}{p-1}, |  |

where s p ​ ( ⋅) s_{p}(\cdot) denotes the sum of the p p -adic digits. Note that s p ​ ( j) + s p ​ ( n − j) − s p ​ ( n) s_{p}(j)+s_{p}(n-j)-s_{p}(n) is a measure for the number of carries when adding n − j n-j to j j in base p p. In particular,

 | v p ​ ( n j) = 0 iff there are no carries. v_{p}{n\choose j}=0\hskip 10.00002pt\text{iff}\hskip 10.00002pt\text{there are no carries}. |  |

It follows that:

###### Lemma 14.

Let n ∈ ℤ > 0 n\in\mathbb{Z}_{>0} and k ∈ ℤ ≥ 0 k\in\mathbb{Z}_{\geq 0}. If j ∈ { 0, 1, 2, …, n ​ p k } j\in\{0,1,2,\dots,np^{k}\} is not a multiple of p k p^{k}, then

 | v p ​ ( n ​ p k j) > 0. v_{p}{np^{k}\choose j}>0. |  |

If moreover n = p r + 1 n=p^{r}+1 for some r ∈ ℤ ≥ 0 r\in\mathbb{Z}_{\geq 0}, it is sufficient to assume that j ∉ { 0, p k, ( n − 1) ​ p k, n ​ p k } j\not\in\{0,p^{k},(n-1)p^{k},np^{k}\}.

Proof: According to Legendre’s formula

 | v p ​ ( n ​ p k j) = s p ​ ( j) + s p ​ ( n ​ p k − j) − s p ​ ( n ​ p k) p − 1. v_{p}{np^{k}\choose j}=\frac{s_{p}(j)+s_{p}(np^{k}-j)-s_{p}(np^{k})}{p-1}. |  |

Let q q and ρ ≠ 0 \rho\neq 0 be the quotient and remainder of j j when divided by p k p^{k}. Then s p ​ ( n ​ p k) = s p ​ ( n) s_{p}(np^{k})=s_{p}(n), s p ​ ( j) = s p ​ ( q) + s p ​ ( ρ) s_{p}(j)=s_{p}(q)+s_{p}(\rho), and

 | s p ​ ( n ​ p k − j) = s p ​ ( ( n − q − 1) ​ p k + ( p k − ρ)) ≥ s p ​ ( n − q) − 1 + 1, s_{p}(np^{k}-j)=s_{p}((n-q-1)p^{k}+(p^{k}-\rho))\geq s_{p}(n-q)-1+1, |  |

from which

 | v p ​ ( n ​ p k j) ≥ v p ​ ( n q) + s p ​ ( ρ) p − 1 > 0. v_{p}{np^{k}\choose j}\geq v_{p}{n\choose q}+\frac{s_{p}(\rho)}{p-1}>0. |  |

A similar argument proves the second statement. ■ \blacksquare

( 3.3) We use this to prove:

###### Proposition 15.

Let n ∈ ℤ > 0 n\in\mathbb{Z}_{>0} and k ∈ ℤ ≥ 0 k\in\mathbb{Z}_{\geq 0} be integers, and let f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] be a CA-polynomial of degree d = n ​ p k d=np^{k}. Then

 | f, f ( p k), f ( 2 ​ p k), …, f ( d − p k) f,f^{(p^{k})},f^{(2p^{k})},\dots,f^{(d-p^{k})} |  |

do not share a common root. If n = p r + 1 n=p^{r}+1 for some integer r ≥ 0 r\geq 0, one even has that

 | f, f ( p k), f ( d − p k) f,f^{(p^{k})},f^{(d-p^{k})} |  |

do not share a common root. As a consequence, if s = ( s 1, …, s d − 1) s=(s_{1},\dots,s_{d-1}) is a scenario for degree d d and s p k = s 2 ​ p k = ⋯ = s d − p k s_{p^{k}}=s_{2p^{k}}=\dots=s_{d-p^{k}} (resp. s p k = s d − p k s_{p^{k}}=s_{d-p^{k}}), then there are no CA-polynomials that match with s s.

Proof: We only prove the first statement (the second assertion follows entirely similarly). Suppose to the contrary that f f is a CA-polynomial such that f, f ( p k), …, f ( d − p k) f,f^{(p^{k})},\dots,f^{(d-p^{k})} do have a common root. We may assume without loss of generality, using Lemma 6, that f f is of the form

 | f ⁡ ( x) = x d + ( d 1) ​ a 1 ​ x d − 1 + ( d 2) ​ a 2 ​ x d − 2 + ⋯ + ( d d − 1) ​ a d − 1 ​ x, f(x)=x^{d}+{d\choose 1}a_{1}x^{d-1}+{d\choose 2}a_{2}x^{d-2}+\cdots+{d\choose d-1}a_{d-1}x, |  | (6) |

that the assumed common root of f, f ( p k), …, f ( d − p k) f,f^{(p^{k})},\dots,f^{(d-p^{k})} is 0 0, and that

 | min { v p ( x i) | i = 1, …, d } = 0, \min\{v_{p}(x_{i})\,|\,i=1,\dots,d\}=0, |  |

where we have denoted by x 1, x 2, …, x d x_{1},x_{2},\dots,x_{d} the zeros of f f.

For j = 1, …, d − 1 j=1,\dots,d-1, we have:

 | j! d! ​ f ( d − j) ​ ( x) = x j + ( j 1) ​ a 1 ​ x j − 1 + ( j 2) ​ a 2 ​ x j − 2 + ⋯ + ( j j − 1) ​ a j − 1 ​ x + a j. \frac{j!}{d!}f^{(d-j)}(x)=x^{j}+{j\choose 1}a_{1}x^{j-1}+{j\choose 2}a_{2}x^{j-2}+\cdots+{j\choose{j-1}}a_{j-1}x+a_{j}. |  | (7) |

Using equality ( 7) with j = 1, ⋯, d − 1 j=1,\cdots,d-1, each time plugging in a common root of f ( d − j) f^{(d-j)} and f f (taking 0 0 if j j is a multiple of p k p^{k}), one proves by induction on j j that

 | { v p ​ ( a j) ≥ 0 for all ​ j = 1, …, d − 1, a j = 0 as soon as ​ p k | j. \left\{\begin{array}[]{ll}v_{p}(a_{j})\geq 0&\hbox{ for all\ }\ j=1,\dots,d-1,\\ a_{j}=0&\hbox{ as soon as\ }\ p^{k}\mid j.\\ \end{array}\right. |  | (8) |

Now let x j x_{j} be such that v p ​ ( x j) = 0 v_{p}(x_{j})=0. Then taking valuations of both sides of the equality

 | x j d = − ( d 1) ​ a 1 ​ x j d − 1 − ( d 2) ​ a 2 ​ x j d − 2 − ⋯ − ( d d − 2) ​ a d − 2 ​ x j 2 − ( d d − 1) ​ a d − 1 ​ x j x_{j}^{d}=-{d\choose 1}a_{1}x_{j}^{d-1}-{d\choose 2}a_{2}x_{j}^{d-2}-\cdots-{d\choose{d-2}}a_{d-2}x_{j}^{2}-{d\choose d-1}a_{d-1}x_{j} |  |

yields a contradiction with ( 8) and Lemma 14. ■ \blacksquare

Note that the cases p k p^{k} and 2 ​ p k 2p^{k} tautologically follow from the above proposition. If d = p r + 1 d=p^{r}+1, it implies that the root of f ( d − 1) ​ ( x) f^{(d-1)}(x) must be a simple root of f ⁡ ( x) f(x). If p ≥ 3 p\geq 3, this in turn can be seen as a limit case of the following statement:

###### Proposition 16.

If d = p r + 1 d=p^{r}+1, then the root of f ( d − 1) ​ ( x) f^{(d-1)}(x) cannot be the mean of two distinct roots of f ⁡ ( x) f(x).

Proof: Using Lemma 6 we can assume that f ⁡ ( x) f(x) is of the form ( 6) with a 1 = 0 a_{1}=0 (i.e. the root of f ( d − 1) ​ ( x) f^{(d-1)}(x) is 0 0), and that again all roots x 1, …, x d x_{1},\dots,x_{d} have non-negative valuation, with minimum 0 0. Let x j x_{j} be such that v p ​ ( x j) = 0 v_{p}(x_{j})=0. Then the equality

 | d ​ a d − 1 ​ x j = − x j d − ( d 2) ​ a 2 ​ x j d − 2 − ⋯ − ( d d − 2) ​ a d − 2 ​ x j 2 da_{d-1}x_{j}=-x_{j}^{d}-{d\choose 2}a_{2}x_{j}^{d-2}-\cdots-{d\choose d-2}a_{d-2}x_{j}^{2} |  |

implies that v p ​ ( a d − 1) = 0 v_{p}(a_{d-1})=0. Now let w ∈ ℂ ∗ w\in\mathbb{C}^{\ast} be such that f ⁡ ( w) = f ⁡ ( − w) = 0 f(w)=f(-w)=0. Then 0 = f ⁡ ( w) − f ⁡ ( − w) 0=f(w)-f(-w) gives

 | d ​ a d − 1 ​ w = − ( d 3) ​ a 3 ​ w d − 3 − ( d 5) ​ a 5 ​ w d − 5 − ⋯ − ( d d − 3) ​ a d − 3 ​ w 3. da_{d-1}w=-{d\choose 3}a_{3}w^{d-3}-{d\choose 5}a_{5}w^{d-5}-\cdots-{d\choose d-3}a_{d-3}w^{3}. |  |

Taking valuations yields a contradiction. ■ \blacksquare

The same argument can be used to show that the root of f ( d − 1) ​ ( x) f^{(d-1)}(x) cannot be the mean of two distinct roots of f ( 1) ​ ( x) f^{(1)}(x).

( 3.4) From now on, we focus on the special case d = p + 1 d=p+1. Using once again Lemma 6, we may assume that

 | { f ⁡ ( x) = x d + d ​ a 1 ​ x d − 1 + ( d 2) ​ a 2 ​ x d − 2 + ⋯ + ( d d − 2) ​ a d − 2 ​ x 2, min { v p ( x j) | j = 1, …, d } = 0, \left\{\begin{array}[]{ll}&f(x)=x^{d}+da_{1}x^{d-1}+{d\choose 2}a_{2}x^{d-2}+\cdots+{d\choose{d-2}}a_{d-2}x^{2},\\ &\\ &\min\{v_{p}(x_{j})\,|\,j=1,\dots,d\}=0,\end{array}\right. |  | (9) |

where we have denoted by x 1, …, x d − 3, x d − 2 = x d − 1 = 0, x d = − a 1 x_{1},\dots,x_{d-3},x_{d-2}=x_{d-1}=0,x_{d}=-a_{1} the roots of f f. For j = 1, …, d − 2 j=1,\dots,d-2, we then again have that expression ( 7) holds. Observe that v p ​ ( a 1) ≥ 0 v_{p}(a_{1})\geq 0 because − a 1 -a_{1} is one of the roots of f f. As before, using equality ( 7) with j = 2, …, d − 2 j=2,\dots,d-2, each time plugging in a common root of f ( d − j) f^{(d-j)} and f f, we prove by induction on j j that

 | v p ​ ( a j) ≥ 0 for all ​ j = 1, …, d − 2. v_{p}(a_{j})\geq 0\ \ \ \hbox{ for all\ }\ j=1,\dots,d-2. |  | (10) |

Let x j x_{j} be such that v p ​ ( x j) = 0 v_{p}(x_{j})=0. The equality

 | − d ​ a 1 ​ x j d − 1 = x j d + ( d 2) ​ a 2 ​ x j d − 2 + ⋯ + ( d d − 2) ​ a d − 2 ​ x j 2 -da_{1}x_{j}^{d-1}=x_{j}^{d}+{d\choose 2}a_{2}x_{j}^{d-2}+\cdots+{d\choose{d-2}}a_{d-2}x_{j}^{2} |  |

shows that v p ​ ( a 1) = 0 v_{p}(a_{1})=0. Therefore, we may assume without loss of generality that a 1 = − 1 a_{1}=-1. Then we can write f ⁡ ( x) = ( x − 1) ​ g ​ ( x) f(x)=(x-1)g(x) where

 | g ⁡ ( x) = x d − 1 − ( d − 1) ​ x d − 2 + ( ( d 2) ​ a 2 − ( d − 1)) ​ x d − 3 + ( ( d 3) ​ a 3 + ( d 2) ​ a 2 − ( d − 1)) ​ x d − 4 + ⋯ + ( ( d d − 3) ​ a d − 3 + ⋯ + ( d 2) ​ a 2 − ( d − 1)) ​ x 2. \begin{split}g(x)&=x^{d-1}-(d-1)x^{d-2}+\left({d\choose 2}a_{2}-(d-1)\right)x^{d-3}+\\ &\left({d\choose 3}a_{3}+{d\choose 2}a_{2}-(d-1)\right)x^{d-4}+\cdots+\\ &\left({d\choose d-3}a_{d-3}+\cdots+{d\choose{2}}a_{2}-(d-1)\right)x^{2}.\end{split} |  |

In view of ( 10) and Lemma 14, all roots of g g have strictly positive valuations (actually greater than 1 / ( d − 3) 1/(d-3)). As a consequence, we see that 1 1 is a simple root of f f (a fact already implied by Proposition 15) and that v p ​ ( x j) > 0 v_{p}(x_{j})>0 for j = 1, …, d − 3 j=1,\dots,d-3. Now whenever f ( d − j) ​ ( 1) ≠ 0 f^{(d-j)}(1)\not=0, the Casas-Alvero property implies that f ( d − j) ​ ( x j) = 0 f^{(d-j)}(x_{j})=0 with v p ​ ( x j) > 0 v_{p}(x_{j})>0 and from equality ( 7) we get v p ​ ( a j) > 0 v_{p}(a_{j})>0. But as

 | f ⁡ ( 1) = 1 − d + ( d 2) ​ a 2 + ⋯ + ( d d − 2) ​ a d − 2 = 0, f(1)=1-d+{d\choose 2}a_{2}+\cdots+{d\choose{d-2}}a_{d-2}=0, |  |

there is at least one index 2 ≤ j ≤ d − 2 2\leq j\leq d-2 such that v p ​ ( a j) = 0 v_{p}(a_{j})=0. In other words, at least one of the derivatives f ( d − j) ​ ( 1) = 0 f^{(d-j)}(1)=0. If we put this together with Proposition 10 and the observations following Lemma 11, we get:

###### Lemma 17.

Let f f be a CA-polynomial over ℂ \mathbb{C} of degree d = p + 1 d=p+1, where p p is prime. Let c c be the center of mass of the roots of f f. Then the following conditions are satisfied:

- •

f ( 1) ​ ( c) ≠ 0, f ( d − 1) ​ ( c) = 0 f^{(1)}(c)\neq 0,f^{(d-1)}(c)=0,

- •

f ( j) ​ ( c) ≠ 0 f^{(j)}(c)\not=0 for at least one j ∈ { 2, …, d − 2 } j\in\{2,\dots,d-2\},

- •

f ( j) ​ ( c) = 0 f^{(j)}(c)=0 for at least one j ∈ { 2, …, d − 2 } j\in\{2,\dots,d-2\}.

( 3.5) Let us now go further into the investigation of the orders of the derivatives having the center of mass as a root, thereby proving Theorem 2. We may again assume that f f is of the form ( 9) and that a 1 = − 1 a_{1}=-1. We will use the notation x ≡ y x\equiv y if v p ​ ( x − y) > 0 v_{p}(x-y)>0. In view of Lemma 17, let j 1 < j 2 < ⋯ < j m j_{1}<j_{2}<\cdots<j_{m}\ be the indices between 2 2 and d − 2 d-2 such that f ( d − j i) ​ ( 1) = 0 f^{(d-j_{i})}(1)=0 for i = 1, …, m i=1,\dots,m. As observed previously, for all j ∈ { 2, ⋯, d − 2 } j\in\{2,\cdots,d-2\}, we have v p ​ ( a j) ≥ 0 v_{p}(a_{j})\geq 0. Moreover, if j ∉ { j 1, ⋯, j m } j\notin\{j_{1},\cdots,j_{m}\} then a j ≡ 0 a_{j}\equiv 0. From equality ( 7) with x = 1 x=1 and j = j 1, j 2, …, j m j=j_{1},j_{2},\dots,j_{m}, we get

 | { 1 − j 1 + a j 1 ≡ 0 1 − j 2 + ( j 2 j 1) ​ a j 1 + a j 2 ≡ 0 ⋮ 1 − j m + ( j m j 1) ​ a j 1 + ( j m j 2) ​ a j 2 + ⋯ + a j m ≡ 0 \left\{\begin{array}[]{ll}1-j_{1}+a_{j_{1}}&\equiv 0\\ 1-j_{2}+\binom{j_{2}}{j_{1}}a_{j_{1}}+a_{j_{2}}&\equiv 0\\ \ \ \ \ \ \vdots\\ 1-j_{m}+\binom{j_{m}}{j_{1}}a_{j_{1}}+\binom{j_{m}}{j_{2}}a_{j_{2}}+\cdots+a_{j_{m}}&\equiv 0\\ \end{array}\right. |  | (11) |

Now, using that f ⁡ ( 1) p = 0 \frac{f(1)}{p}=0 and that v p ​ ( d j) ≥ 1 v_{p}\binom{d}{j}\geq 1 for j = 2, …, d − 2 j=2,\dots,d-2, we obtain

 | − 1 + ( d j 1) p ​ a j 1 + ⋯ + ( d j m) p ​ a j m ≡ 0. -1+\frac{\binom{d}{j_{1}}}{p}a_{j_{1}}+\cdots+\frac{\binom{d}{j_{m}}}{p}a_{j_{m}}\equiv 0. |  | (12) |

Observe that for all 2 ≤ j ≤ d − 2 2\leq j\leq d-2 we have:

 | ( d j) p = d ( d − 2) ( d − 3) ⋯ ( d − ( j − 1)) j! = ( p + 1) ( p − 1) ( p − 2) ⋯ ( p − ( j − 2)) j! = 1 j! ​ ( p j − 1 + α j − 2 ​ p j − 2 + ⋯ + α 1 ​ p) + ( − 1) j − 2 ​ ( j − 2)! j! \begin{split}\frac{{d\choose j}}{p}&=\frac{d(d-2)(d-3)\cdots(d-(j-1))}{j!}\\ &=\frac{(p+1)(p-1)(p-2)\cdots(p-(j-2))}{j!}\\ &=\frac{1}{j!}(p^{j-1}+\alpha_{j-2}p^{j-2}+\cdots+\alpha_{1}p)+\frac{(-1)^{j-2}(j-2)!}{j!}\end{split} |  |

where α 1, …, α j − 2 \alpha_{1},\dots,\alpha_{j-2} are integers. Therefore:

 | ( d j) p ≡ ( − 1) j j ⁡ ( j − 1). \frac{\binom{d}{j}}{p}\equiv\frac{(-1)^{j}}{j(j-1)}. |  |

Putting equations ( 11) and ( 12) together and putting a ~ j i = a j i j i ​ ( j i − 1) \tilde{a}_{j_{i}}=\frac{a_{j_{i}}}{j_{i}(j_{i}-1)}, we obtain:

 | { − 1 + j 1 ​ a ~ j 1 ≡ 0 − 1 + ( j 2 − 2 j 1 − 2) ​ j 2 ​ a ~ j 1 + j 2 ​ a ~ j 2 ≡ 0 ⋮ − 1 + ( j m − 2 j 1 − 2) ​ j m ​ a ~ j 1 + ( j m − 2 j 2 − 2) ​ j m ​ a ~ j 2 + ⋯ + j m ​ a ~ j m ≡ 0 − 1 + ( − 1) j 1 a ~ j 1 + ( − 1) j 2 a ~ j 2 + ⋯ + ( − 1) j m a ~ m ≡ 0. \left\{\begin{array}[]{ll}-1+j_{1}\tilde{a}_{j_{1}}&\equiv 0\\ -1+\binom{j_{2}-2}{j_{1}-2}j_{2}\tilde{a}_{j_{1}}+j_{2}\tilde{a}_{j_{2}}&\equiv 0\\ \ \ \ \ \ \vdots\\ -1+\binom{j_{m}-2}{j_{1}-2}j_{m}\tilde{a}_{j_{1}}+\binom{j_{m}-2}{j_{2}-2}j_{m}\tilde{a}_{j_{2}}+\cdots+j_{m}\tilde{a}_{j_{m}}&\equiv 0\\ -1+(-1)^{j_{1}}\tilde{a}_{j_{1}}+(-1)^{j_{2}}\tilde{a}_{j_{2}}+\cdots+(-1)^{j_{m}}\tilde{a}_{{}_{m}}&\equiv 0.\end{array}\right. |  | (13) |

With Δ f \Delta_{f} as in the énoncé of Theorem 2, we see that necessarily det Δ f ≡ 0 \det\Delta_{f}\equiv 0: otherwise inverting ( 13) we would get that 1 ≡ 0 1\equiv 0. To conclude the proof of Theorem 2 we show:

###### Lemma 18.

Let f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] be a CA-polynomial of degree d = p + 1 d=p+1 and let c c be the center of mass of its roots. Then there are at least two indices 2 ≤ j 1 < j 2 ≤ d − 2 2\leq j_{1}<j_{2}\leq d-2 such that f ( j 1) ​ ( c) = f ( j 2) ​ ( c) = 0 f^{(j_{1})}(c)=f^{(j_{2})}(c)=0.

Proof: If not, in virtue of Lemma 17, there exists a unique index 2 ≤ j ≤ d − 2 2\leq j\leq d-2 such that f ( d − j) ​ ( c) = 0 f^{(d-j)}(c)=0. We can assume without loss of generality that f f is of the form ( 9) with a 1 = − 1 a_{1}=-1 and apply the above. Then m = 1 m=1 and

 | Δ f = [− 1 j − 1 ( − 1) j] = j − ( − 1) j. \Delta_{f}=\left[\begin{array}[]{l l }-1&j\\ -1&(-1)^{j}\end{array}\right]=j-(-1)^{j}. |  | (14) |

Observe that 1 ≤ j − ( − 1) j ≤ j + 1 ≤ d − 2 1\leq j-(-1)^{j}\leq j+1\leq d-2 for j ∈ 2, …, d − 3 j\in{2,\dots,d-3}. Besides, d − 2 − ( − 1) d − 2 = d − 3 d-2-(-1)^{d-2}=d-3 because d d is even (indeed, p ≠ 2 p\neq 2 since the Casas-Alvero conjecture is true for degree 3 3). Thus there is no way for p p to divide det Δ f \det\Delta_{f}. ■ \blacksquare

( 3.6) Theorem 2 implies that every CA-polynomial of degree d = p + 1 d=p+1 matches with a scenario s = ( s 1, …, s d − 1) s=(s_{1},\dots,s_{d-1}) for which s d − 1 ≠ 0 s_{d-1}\neq 0 and the index set

 | ind ​ ( s) = { j | 2 ≤ j ≤ d − 2 ​ and ​ s d − j = s d − 1 } \text{ind}(s)=\{\,j\ |\ 2\leq j\leq d-2\text{ and }s_{d-j}=s_{d-1}\,\} |  |

satisfies the according determinant condition. We remark however that this does not necessarily imply that *the*scenario of a CA-polynomial satisfies these conditions. Indeed, imagine a CA-polynomial f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] of degree 12 12 for which

 | scen ​ ( f) = s = ( 0, 1, 2, 3, 4, 2, 5, 6, 4, 7, 4), \text{scen}(f)=s=(0,1,2,3,4,2,5,6,4,7,4), |  |

i.e. there exist a 1, …, a 7 ∈ ℂ a_{1},\dots,a_{7}\in\mathbb{C} such that f ⁡ ( a s j) = f ( j) ​ ( a s j) = 0 f(a_{s_{j}})=f^{(j)}(a_{s_{j}})=0 for j = 1, …, d − 1 j=1,\dots,d-1. Then ind ​ ( s) = { 3, 7 } \text{ind}(s)=\{3,7\} does not satisfy the determinant condition. However, it might a priori be that f ( 6) ​ ( x) f^{(6)}(x) has both a 2 a_{2} and a 4 a_{4} as a root. Then f ⁡ ( x) f(x) also matches with the scenario ( 0, 1, 2, 3, 4, 4, 5, 6, 4, 7, 4) ≠ scen ​ ( f) (0,1,2,3,4,4,5,6,4,7,4)\neq\text{scen}(f). Here, the index set reads { 3, 6, 7 } \{3,6,7\}, for which the determinant condition *is*satisfied.

( 3.7) We end our study of the degree p + 1 p+1 case with the following observation.

###### Proposition 19.

Let p p be a prime number. Then there is no CA-polynomial of degree d = p + 1 d=p+1 all of whose roots are rational.

Proof: Using the notations and the results found in the proof of Lemma 17, we may assume that f f is of the form

 | f ⁡ ( x) = x d − d ​ x d − 1 + ( d 2) ​ x d − 2 + ⋯ + ( − 1) k − 1 ( d k − 1) x d − k + 1 + ( d k) a k x d − k + ⋯ + ( d d − 2) a d − 2 x 2, \begin{split}f(x)=&x^{d}-dx^{d-1}+{d\choose 2}x^{d-2}\\ &+\cdots+(-1)^{k-1}{d\choose{k-1}}x^{d-k+1}+{d\choose k}a_{k}x^{d-k}+\cdots+{d\choose d-2}a_{d-2}x^{2},\end{split} |  |

with v p ​ ( x j) ≥ 1 v_{p}(x_{j})\geq 1 for j = 1, …, d − 3 j=1,\dots,d-3. Here, we have denoted by k k the smallest index between 2 2 and d − 2 d-2 such that f ( d − k) ​ ( 1) ≠ 0 f^{(d-k)}(1)\not=0 (we know from Lemma 17 that such a k k exists). We introduce the notation

 | S m = ∑ j = 1 d − 3 x j m. S_{m}=\sum_{j=1}^{d-3}x_{j}^{m}. |  |

Then we have: v p ​ ( S 1) = v p ​ ( d − 1) = 1 v_{p}(S_{1})=v_{p}(d-1)=1, and v p ​ ( S j) ≥ 2 v_{p}(S_{j})\geq 2 for j = 2, …, d − 2 j=2,\dots,d-2. Using Newton’s formulas (see Lemma 11 applied to j = 0 j=0), we obtain

 | − k ​ ( d k) ​ a k = ∑ j = 0 k − 1 ( − 1) j ​ ( 1 + S k − j) ​ ( d j) = ∑ j = 0 k − 1 ( − 1) j ​ ( d j) + ∑ j = 0 k − 1 ( − 1) j ​ S k − j ​ ( d j) = ( − 1) k − 1 ​ ( d − 1 k − 1) + ∑ j = 0 k − 1 ( − 1) j ​ S k − j ​ ( d j). \begin{split}-k{d\choose k}a_{k}&=\sum_{j=0}^{k-1}(-1)^{j}(1+S_{k-j}){d\choose j}\\ &=\sum_{j=0}^{k-1}(-1)^{j}{d\choose j}+\sum_{j=0}^{k-1}(-1)^{j}S_{k-j}{d\choose j}\\ &=(-1)^{k-1}{{d-1}\choose{k-1}}+\sum_{j=0}^{k-1}(-1)^{j}S_{k-j}{d\choose j}.\\ \end{split} |  |

Note that v p ​ ( ( d k) ​ a k) > 1 v_{p}({d\choose k}a_{k})>1 which will lead to a contradiction:

- •

If k = 2 k=2, then the last equality becomes

 | − 2 ​ ( d 2) ​ a 2 = − ( d − 1) + S 2 − d ​ S 1 = − ( d − 1) + S 2 − d ⁡ ( d − 1) = − ( d + 1) ​ ( d − 1) + S 2. -2{d\choose 2}a_{2}=-(d-1)+S_{2}-dS_{1}=-(d-1)+S_{2}-d(d-1)=-(d+1)(d-1)+S_{2}. |  |

The valuation of the right-hand term is 1 1.

- •

If 3 ≤ k ≤ d − 2 3\leq k\leq d-2, then the right-hand term is

 | ( − 1) k − 1 ​ ( d − 1 k − 1) + ∑ j = 0 k − 2 ( − 1) j ​ S k − j ​ ( d j) + ( − 1) k − 1 ​ S 1 ​ ( d k − 1). (-1)^{k-1}{{d-1}\choose{k-1}}+\sum_{j=0}^{k-2}(-1)^{j}S_{k-j}{d\choose j}+(-1)^{k-1}S_{1}{d\choose{k-1}}. |  |

But v p ​ ( S k − j) ≥ 2 v_{p}(S_{k-j})\geq 2 for j = 0, …, k − 2 j=0,\dots,k-2, and v p ​ ( S 1 ​ ( d k − 1)) = 2 v_{p}(S_{1}{d\choose{k-1}})=2, so the valuation of the right-hand term is v p ​ ( ( d − 1 k − 1)) = 1 v_{p}({{d-1}\choose{k-1}})=1. ■ \blacksquare

Remark that the proof of Proposition 19 in fact implies that there are no CA-polynomials of degree p + 1 p+1 all of whose roots are contained in a number field in which p p does not ramify. Indeed, this ensures that the valuations of the x j x_{j} are integers, hence we can still conclude that v p ​ ( x j) ≥ 1 v_{p}(x_{j})\geq 1.

## 4 Algebraic varieties of counterexamples

( 4.1) Let k k be an algebraically closed field and let d > 0 d>0 be an integer. The set of equivalence classes (in the sense of Lemma 6) of CA-polynomials of degree d d will be denoted by CA k ​ ( d) \text{CA}_{k}(d).

( 4.2) We have a surjective map

 | Φ k ( d, d − 2): V k ( d, d − 2) → CA k ( d): ( p 1, …, p d − 2) ↦ x 2 ( x − p 1) ⋯ ( x − p d − 2), \Phi_{k}(d,d-2):V_{k}(d,d-2)\rightarrow\text{CA}_{k}(d):(p_{1},\dots,p_{d-2})\mapsto x^{2}(x-p_{1})\cdots(x-p_{d-2}), |  |

where V k ​ ( d, d − 2) ⊂ ℙ k d − 3 V_{k}(d,d-2)\subset\mathbb{P}_{k}^{d-3} is the projective variety defined by the ideal

 | I k ( d, d − 2) = ( Res x ( F, F H ( j)) | j = 2, …, d − 1) I_{k}(d,d-2)=\left(\,\left.\text{Res}_{x}(F,F_{H}^{(j)})\,\right|\,j=2,\dots,d-1\,\right) |  |

with F = x 2 ​ ( x − P 1) ​ … ​ ( x − P d − 2) ∈ k ⁡ [P 1, …, P d − 2] ​ [x] F=x^{2}(x-P_{1})\dots(x-P_{d-2})\in k[P_{1},\dots,P_{d-2}][x]. Therefore, in order to prove that no CA-polynomials exist in degree d d, it suffices to show that V k ​ ( d, d − 2) = ∅ V_{k}(d,d-2)=\emptyset. Note that V k ​ ( d, d − 2) V_{k}(d,d-2) is invariant under coordinate permutations, so it is sufficient to show that V k ​ ( d, d − 2) V_{k}(d,d-2) does not contain any points of the form ( p 1, …, p d − 3, 1) (p_{1},\dots,p_{d-3},1). Setting P d − 2 = 1 P_{d-2}=1 in I k ​ ( d, d − 2) I_{k}(d,d-2), we obtain an ideal of k ⁡ [P 1, …, P d − 3] k[P_{1},\dots,P_{d-3}] that is equal to the unit ideal if and only if V k ​ ( d, d − 2) = ∅ V_{k}(d,d-2)=\emptyset. This can be checked using a finite Gröbner basis computation, which is exactly the approach of [5].

( 4.3) Somehow dually, we also have a surjective map

 | Φ k ​ ( d, 0): V k ​ ( d, 0) → CA k ​ ( d): \Phi_{k}(d,0):V_{k}(d,0)\rightarrow\text{CA}_{k}(d):\hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt |  |

 | ( a 1, …, a d − 2) ↦ x 2 ​ ( x d − 2 + a 1 ​ x d − 3 + ⋯ + a d − 2), \hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt(a_{1},\dots,a_{d-2})\mapsto x^{2}(x^{d-2}+a_{1}x^{d-3}+\dots+a_{d-2}), |  |

where now V k ​ ( d, 0) ⊂ ℙ k ​ ( d − 2, d − 1, …, 2, 1) V_{k}(d,0)\subset\mathbb{P}_{k}(d-2;d-1;\dots;2;1) is the weighted projective variety defined by the ideal

 | I k ( d, 0) = ( Res x ( F, F H ( j)) | j = 2, …, d − 1) I_{k}(d,0)=\left(\,\left.\text{Res}_{x}(F,F_{H}^{(j)})\,\right|\,j=2,\dots,d-1\,\right) |  |

with F = x 2 ​ ( x d − 2 + A 1 ​ x d − 3 + ⋯ + A d − 2) ∈ k ⁡ [A 1, …, A d − 2] ​ [x] F=x^{2}(x^{d-2}+A_{1}x^{d-3}+\dots+A_{d-2})\in k[A_{1},\dots,A_{d-2}][x]. Again, in order to show that no Casas-Alvero polynomials can exist in degree d d, it is sufficient to prove that V k ​ ( d, 0) = ∅ V_{k}(d,0)=\emptyset. This was used in the theoretical approach of [7].

( 4.4) We will make use of a hybrid version of the above maps. Namely, for each t ∈ { 0, …, d − 2 } t\in\{0,\dots,d-2\} we have a surjective map

 | Φ k ​ ( d, t): V k ​ ( d, t) → CA k ​ ( d): \Phi_{k}(d,t):V_{k}(d,t)\rightarrow\text{CA}_{k}(d):\hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt |  |

 | ( p 1, …, p t, a 1, …, a d − 2 − t) ↦ x 2 ( x − p 1) ⋯ ( x − p t) ( x d − 2 − t + a 1 x d − 3 − t + ⋯ + a d − 2 − t), (p_{1},\dots,p_{t},a_{1},\dots,a_{d-2-t})\mapsto x^{2}(x-p_{1})\cdots(x-p_{t})(x^{d-2-t}+a_{1}x^{d-3-t}+\dots+a_{d-2-t}), |  |

where V k ​ ( d, t) ⊂ ℙ k ​ ( 1, …, 1, d − 2 − t, d − 3 − t, …, 2, 1) V_{k}(d,t)\subset\mathbb{P}_{k}(1;\dots;1;d-2-t;d-3-t;\dots;2;1) is the weighted projective variety defined by the ideal

 | I k ( d, t) = ( Res x ( F, F H ( j)) | j = 2, …, d − 1) I_{k}(d,t)=\left(\,\left.\text{Res}_{x}(F,F_{H}^{(j)})\,\right|\,j=2,\dots,d-1\,\right) |  |

with

 | F = x 2 ( x − P 1) ⋯ ( x − P t) ( x d − 2 − t + A 1 x d − 3 − t + ⋯ + A d − 2 − t) F=x^{2}(x-P_{1})\cdots(x-P_{t})(x^{d-2-t}+A_{1}x^{d-3-t}+\dots+A_{d-2-t}) |  |

in k ⁡ [P 1, …, P t, A 1, …, A d − 2 − t] ​ [x] k[P_{1},\dots,P_{t},A_{1},\dots,A_{d-2-t}][x]. Once more it is sufficient to show that V k ​ ( d, t) = ∅ V_{k}(d,t)=\emptyset (for any value of t t) in order to prove that no Casas-Alvero polynomials of degree d d exist over k k.

( 4.5) Now to each scenario s s for degree d d of type t t, we associate the variety

 | V k ​ ( s) ⊂ V k ​ ( d, t) V_{k}(s)\subset V_{k}(d,t) |  |

defined by the ideal

 | I k ( s) = ( F H ( j) ( P s j) | j = 2, …, d − 1) ⊂ k [P 1, …, P t, A 1, …, A d − 2 − t] I_{k}(s)=\left(\,\left.F_{H}^{(j)}(P_{s_{j}})\,\right|\,j=2,\dots,d-1\,\right)\subset k[P_{1},\dots,P_{t},A_{1},\dots,A_{d-2-t}] |  |

where

 | F = x 2 ( x − P 1) ⋯ ( x − P t) ( x d − 2 − t + A 1 x d − 3 − t + ⋯ + A d − 2 − t) F=x^{2}(x-P_{1})\cdots(x-P_{t})(x^{d-2-t}+A_{1}x^{d-3-t}+\dots+A_{d-2-t}) |  |

and P 0 = 0 P_{0}=0. Then it is clear that V k ​ ( s) V_{k}(s) parameterizes the CA-polynomials that match with s s. Recall that every CA-polynomial matches with at least one scenario (e.g., its own scenario scen ​ ( f) \text{scen}(f)). Thus, if one wants to show that no CA-polynomials of degree d d exist over k k, it suffices to show that V k ​ ( s) = ∅ V_{k}(s)=\emptyset for each scenario s s for degree d d. This is essentially the ‘primary decomposition’ that was mentioned in [7, Section ?], but in Section 5 below we will see that there is a significant amount of computational gain to be expected from viewing the set of CA-polynomials that match with s s as a subvariety of V k ​ ( d, t) V_{k}(d,t) rather than V k ​ ( d, d − 2) V_{k}(d,d-2). Moreover, if k = ℂ k=\mathbb{C}, in view of the theoretical results obtained in Sections 2 and 3, it is actually sufficient to check whether V ℂ ​ ( s) = ∅ V_{\mathbb{C}}(s)=\emptyset for a restricted set of scenarios. We will elaborate the details of this for d = 12 d=12 in Section 6.

## 5 Revisiting the computational approach

( 5.1) We now describe the basic version of our algorithm, discarding the theoretical results of Sections 2 and 3. The input is a field characteristic p p (either 0 0 or a prime number) along with an integer d > 2 d>2. The output is `yes`or `no`, depending on whether Casas-Alvero polynomials exist in degree d d and characteristic p p or not.

*Step 1.*Create a list L L (of length d − 1 d-1) of lists, such that L ⁡ [t] L[t] contains all scenarios for type t t (for t = 0, …, d − 2 t=0,\dots,d-2). This can be done easily using d − 2 d-2 nested for-loops. Let k k be the field of rational numbers if p = 0 p=0, and let k k be the field with p p elements otherwise. Set `answer := no`.

*Step 2.*For t t going from 1 1 to d − 2 d-2 do:

- -

Initiate the following variables/structures:

  - *

R = k ⁡ [P 1, …, P t − 1, A 1, …, A d − 2 − t] R=k[P_{1},\dots,P_{t-1},A_{1},\dots,A_{d-2-t}]

  - *

S = R ⁡ [x] S=R[x]

  - *

P 0 = 0 P_{0}=0 and P t = 1 P_{t}=1

  - *

F ( x) = x 2 ( x − P 1) ⋯ ( x − P t) ( x d − 2 − t + A 1 x d − 3 − t + ⋯ + A d − 2 − t) F(x)=x^{2}(x-P_{1})\cdots(x-P_{t})(x^{d-2-t}+A_{1}x^{d-3-t}+\dots+A_{d-2-t})

  - *

≺ \prec = = a monomial ordering that first eliminates A 1, …, A d − 2 − t A_{1},\dots,A_{d-2-t} and that behaves like `grevlex`on the remaining variables P 1, …, P t − 1 P_{1},\dots,P_{t-1}

- -

For s s in L ⁡ [t] L[t] do:

  - *

Let I k aff ​ ( s) ⊂ R I_{k}^{\text{aff}}(s)\subset R be the ideal generated by F H ( j) ​ ( P s j) F_{H}^{(j)}(P_{s_{j}}) for j = 2, …, d − 1 j=2,\dots,d-1. Check whether or not I k aff ​ ( s) = R I_{k}^{\text{aff}}(s)=R by checking if the reduced Gröbner basis (w.r.t. ≺ \prec) of I k aff ​ ( s) I_{k}^{\text{aff}}(s) equals { 1 } \{1\}. If it does not, set `answer := yes`and quit the loops.

*Step 3.*Output `answer`.

( 5.2) Modulo a base change to the algebraic closure of k k, I k aff ​ ( s) I_{k}^{\text{aff}}(s) is obtained from I k ​ ( s) I_{k}(s) (as described in ( 4.5)) by setting P t = 1 P_{t}=1, so it only describes an affine part of V k ​ ( s) V_{k}(s). However, it suffices to verify that this affine part is empty. Indeed, the type of a CA-polynomial corresponding to a point ( p 1, …, p t, a 1, …, a d − 2 − t) ∈ V k ​ ( s) (p_{1},\dots,p_{t},a_{1},\dots,a_{d-2-t})\in V_{k}(s) with p t = 0 p_{t}=0 is strictly smaller than t t, so we would have encountered it already.

( 5.3) The variables A 1, …, A d − 2 − t A_{1},\dots,A_{d-2-t} appear linearly in the defining polynomials F H ( j) ​ ( P s j) F_{H}^{(j)}(P_{s_{j}}). Therefore, they can be eliminated easily. (In fact, the corresponding linear system is in echelon form, so the A i A_{i} ’s can be eliminated bottom-up by hand.) The lower the type, the more variables can be eliminated and the easier the Gröbner basis computation becomes (in the extreme case t = 1 t=1 one obtains a linear system in d − 3 d-3 variables). This is the main reason for our usage of the hybrid varieties V k ​ ( d, t) V_{k}(d,t).

( 5.4) It is theoretically possible to avoid Gröbner basis computations and use linear algebra instead. Indeed, I k aff ​ ( s) = R I_{k}^{\text{aff}}(s)=R is equivalent to the solvability of

 | 1 = g 1 ⋅ F H ( 2) ​ ( P s 2) + … + g d − 2 ⋅ F H ( d − 1) ​ ( P s d − 1) 1=g_{1}\cdot F_{H}^{(2)}(P_{s_{2}})\,+\,\dots\,+\,g_{d-2}\cdot F_{H}^{(d-1)}(P_{s_{d-1}}) |  | (15) |

in terms of polynomials g i ∈ R g_{i}\in R. If such polynomials exist, by the effective Nullstellensatz they can be chosen such that their degree is bounded by d d d^{d} (e.g., see [8]). So in principle, one could use indetermined coefficients to translate the solvability of ( 15) to the solvability of some linear system of equations. But this system is so huge that no gain is to be expected (although maybe this deserves a deeper analysis).

( 5.5) One can speed up the algorithm slightly by noting the following. If s 2 = 0 s_{2}=0, then the first defining polynomial is

 | F H ( 2) ( 0) = ( − 1) t ⋅ P 1 ⋯ P t − 1 ⋅ A d − 2 − t F_{H}^{(2)}(0)=(-1)^{t}\cdot P_{1}\cdots P_{t-1}\cdot A_{d-2-t} |  |

But Casas-Alvero polynomials corresponding to P 1 ⋯ P t − 1 = 0 P_{1}\cdots P_{t-1}=0 are of strictly lower type than t t, so they would have been encountered already. Therefore, our defining polynomial can be replaced by A d − 2 − t A_{d-2-t}. If in addition s 3 = 0 s_{3}=0, then similarly the second defining polynomial can be replaced by A d − 3 − t A_{d-3-t}, and so on. Suppose that the first nonzero entry of s s appears at position j j. Then after substituting A d − 2 − t = ⋯ = A d − j + 1 − t = 0 A_{d-2-t}=\dots=A_{d-j+1-t}=0 (no substitutions if j = 2 j=2), one finds that

 | F H ( j) ​ ( P s j) = F H ( j) ​ ( P 1) F_{H}^{(j)}(P_{s_{j}})=F_{H}^{(j)}(P_{1}) |  |

is a multiple of P 1 P_{1}. For the same reason, this factor can be removed.

( 5.6) The above algorithm can be used straightforwardly to find all bad primes for a given degree d d (given that we know that the Casas-Alvero conjecture is true in degree d d):

1. 1.

Initialize a set of candidate bad primes C = { } C=\{\,\}.

2. 2.

First run the basic algorithm with p = 0 p=0, but instead of just checking whether the reduced Gröbner basis of I ℚ aff ​ ( s) I_{\mathbb{Q}}^{\text{aff}}(s) equals { 1 } \{1\}, compute polynomials g 1, …, g d − 2 ∈ R g_{1},\dots,g_{d-2}\in R for which ( 15) holds. Then add every prime factor appearing in the denominators of the g j g_{j} to C C.

3. 3.

Now if a prime p p is not in C C, it cannot be a bad prime because each of the expansions ( 15) can be reduced mod p p. To find which candidate bad primes are actually bad primes, we run the basic algorithm for each p ∈ C p\in C.

An implementation of this method can be found in `CAbadprimes.m`.

( 5.7) The hardest part is step 2 2, because of the computing in characteristic 0 0. Note that it is possible to give an upper bound for the elements of C C purely in terms of d d, so that step 2 2 could in principle be avoided. Indeed, see the discussion following ( 15) – the denominators of the solutions of the linear system can be bounded using Cramer’s rule. But the bound one obtains is too large to be of any practical use.

( 5.8) We have executed the algorithm for d = 5 d=5, d = 6 d=6 and d = 7 d=7. In case of d = 5 d=5, the total time needed was less than 0.03 0.03 seconds. For d = 6 d=6, the computer needed less than 3 3 seconds. A naive run of the algorithm for d = 7 d=7 is not expected to end in a reasonable amount of time, because the denominators become very hard to factor. But by using several monomial orders and computing greatest common divisors, one can make the case d = 7 d=7 feasible in Magma (apart from the factorization of one composite 119 119 -digit number, for which we used the `CADO-NFS`package [1]). The file `CAbadprimes7test.m`contains Magma code proving the correctness of our output. The case d = 8 d=8 lies out of reach. Of course, exhaustive lists of bad primes for increasing degrees become less and less interesting. But it would be good to have an idea on the growth of the largest bad prime, or on the number of bad primes. Such lists can also be helpful in detecting patterns (we could not observe any). By just repeating our basic algorithm for increasing values of p p, it is feasible to find the smallest non-bad prime (that does not divide d d), for d d up to 10 10. We have put the outcomes in Table 2.

d d | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |

p p | - | - | 11 | 13 | 17 | 127 | 419 | 941 | 3803 |

Table 2: The smallest non-bad prime p p that does not divide d d

## 6 The Casas-Alvero conjecture in degree 12 12

( 6.1) Naively applying the basic algorithm to d = 12 d=12 and characteristic p = 0 p=0 is unrealistic. Two observations lead to a crucial speed-up:

- •

as remarked in ( 4.5), in view of the theoretical results obtained in Sections 2 and 3, it suffices to show that V ℂ ​ ( s) = ∅ V_{\mathbb{C}}(s)=\emptyset for a restricted set of scenarios s s,

- •

for each such s s, it actually suffices to show that V 𝔽 ¯ p ​ ( s) = ∅ V_{\overline{\mathbb{F}}_{p}}(s)=\emptyset for a single prime p p, because the varieties are projective and take equations over ℤ \mathbb{Z}.

( 6.2) As for the first speed-up, by Theorem 2 and Proposition 15 it suffices to prove that V ℂ ​ ( s) = ∅ V_{\mathbb{C}}(s)=\emptyset for all scenarios s = ( s 1, …, s 11) s=(s_{1},\dots,s_{11}) for which

- •

s 1 = 0 ≠ s 11 s_{1}=0\neq s_{11},

- •

s 3 ≠ s 9 s_{3}\neq s_{9},

- •

s 4 ≠ s 8 s_{4}\neq s_{8},

- •

ind ​ ( s) \text{ind}(s) satisfies the determinant condition mentioned in the énoncé of Theorem 2

(we omit the contribution of Proposition 8 to this discussion, because the arguments involved are rather subtle, whereas the computational gain is limited). Let L res L_{\text{res}} be obtained from L L (as introduced in ( 5.1)) by restricting to these scenarios. Then L res \text{L}_{\text{res}} contains

 | 0, 6, 718, 5210, 8918, 5404, 1352, 141, 5, 0, 0 0,6,718,5210,8918,5404,1352,141,5,0,0 |  |

scenarios of type 0, …, 10 0,\dots,10, respectively (this is less than was mentioned in ( 3), where only the determinant condition was taken into account). However, for the algorithm to work rigorously, the list L res L_{\text{res}} should be slightly enlarged again, so that it becomes closed under taking *descendants*, in the following sense.

###### Definition 2.

Let d > 0 d>0 be an integer and let s = ( s 1, …, s d − 1) s=(s_{1},\dots,s_{d-1}) be a scenario for degree d d. Let t = type ​ ( s) t=\text{type}(s). Then we say that s ′ = ( s 1 ′, …, s d − 1 ′) s^{\prime}=(s^{\prime}_{1},\dots,s^{\prime}_{d-1}) is a *descendant*of s s if there exists a 1 ≤ j ≤ t 1\leq j\leq t such that for all i = 1, …, d − 1 i=1,\dots,d-1

- •

s i ′ = s i s^{\prime}_{i}=s_{i} if s i < j s_{i}<j,

- •

s i ′ = 0 s^{\prime}_{i}=0 if s i = j s_{i}=j,

- •

s i ′ = s i − 1 s^{\prime}_{i}=s_{i}-1 if s i > j s_{i}>j.

This ensures that working in the affine subvariety P t = 1 P_{t}=1 (see ( 5.2)) and speeding up the algorithm (as in ( 5.5)) are still justified. Note that if s ′ s^{\prime} is a descendant of s s, then type ​ ( s ′) = type ​ ( s) − 1 \text{type}(s^{\prime})=\text{type}(s)-1. By closing L res L_{\text{res}} under taking descendants, one obtains a list L res cl L_{\text{res}}^{\text{cl}} containing

 | 1,279, 3892, 12073, 13661, 6685, 1491, 146, 5, 0, 0 1,279,3892,12073,13661,6685,1491,146,5,0,0 |  |

scenarios of type 0, …, 10 0,\dots,10, respectively. This may seem a big increase, but note that scenarios of low type can be eliminated very easily.

( 6.3) As for the second speed-up, based on the experimentally observed distribution of bad primes in degrees d ≤ 7 d\leq 7, any prime p p which is ‘not too small’ is most likely to work. If nevertheless the computation breaks down and a `yes`is printed, one can redo the computation using a different value of p p. (In principle, it is possible to give a lower bound on p p so that it is guaranteed to work, but this bound is much too large to be of any practical use – recall from Theorem 4 that the largest bad prime for d = 7 d=7 had already 135 135 decimal digits). Our first try was p = 10 7 + 17 p=10^{7}+17 and immediately worked. It is convenient to use the same p p for all scenarios listed in L res cl L_{\text{res}}^{\text{cl}}. At least, if a scenario s s is treated modulo some p p, then all of its subsequent descendants should be treated modulo the same p p. Indeed, this enables us to conclude that the *projective*variety V 𝔽 ¯ p ​ ( s) V_{\overline{\mathbb{F}}_{p}}(s) is empty, and hence that V ℂ ​ ( s) = ∅ V_{\mathbb{C}}(s)=\emptyset.

( 6.4) Magma code implementing the above method can be found in the file `CAdeg12.m`. We have executed the algorithm and the outcome was affirmative (i.e. the Casas-Alvero conjecture is true in degree 12 12, thereby proving Theorem 5). Approximate time and memory requirements can be found in Table 3.

type | # scenarios | time | memory |

1 1 | 279 279 | 0.1 0.1 secs | ≪ 0.1 \ll 0.1 GB |

2 2 | 3892 3892 | 43 43 secs | ≪ 0.1 \ll 0.1 GB |

3 3 | 12073 12073 | 2 2 mins | < 0.1 <0.1 GB |

4 4 | 13661 13661 | 40 40 mins | 0.1 0.1 GB |

5 5 | 6685 6685 | 20 20 hours | 0.2 0.2 GB |

6 6 | 1491 1491 | 2 2 weeks | 1.3 1.3 GB |

7 7 | 146 146 | 16 16 weeks | 10 10 GB |

8 8 | 5 5 | 15 15 weeks | 90 90 GB |

Table 3: Approximate time and memory requirements for settling d = 12 d=12, as if the algorithm were executed on a single core. In practice, types 6 6 and 7 7 were spread among multiple cores. In case of type 8 8, this was not possible due to memory limitations.

( 6.5) The computation fills in the smallest open entry in the list of degrees for which the Casas-Alvero conjecture is known to hold. Up to our knowledge, the list of degrees d ≤ 100 d\leq 100 for which the conjecture is still open is

20, 24, 28, 30, 35, 36, 40, 42, 45, 48, 55, 56, 60, 63, 66, 70, 72, 77, 78, 80, 84, 88, 90, 91, 98, 99, 100 20,24,28,30,35,36,40,42,45,48,55,56,60,63,66,70,72,77,78,80,84,88,90,91,98,99,100.

Our algorithm can in principle be generalized to higher degrees (note in particular that the two next open cases d = 20 d=20 and d = 24 d=24 are also of the form p + 1 p+1). But without new theoretical ingredients, an implementation of this is expected to demand astronomical amounts of time and memory.

## References

- [1] Shi Bai, Pierrick Gaudry, Alexander Kruppa, François Morain, Emmanuel Thomé and Paul Zimmerman, *CADO-NFS 1.1*, available at `http://cado-nfs.gforge.inria.fr/`
- [2] Wieb Bosma, John Cannon and Catherine Playoust, *The Magma algebra system. I. The user language*, Journal of Symbolic Computation 24(3-4), pp. 235–265 (1997)
- [3] Eduardo Casas-Alvero, *Higher order polar germs*, Journal of Algebra 240(1), pp. 326-337 (2001)
- [4] Mustapha Chellali and Alain Salinier, *La conjecture de Casas-Alvero pour les degrés 5 ​ p e 5p^{e}*, preprint
- [5] Gema M. Diaz-Toca and Laureano Gonzalez-Vega, *On analyzing a conjecture about univariate polynomials and their roots by using maple*, Proceedings of the Maple Conference 2006, Waterloo (Canada), July 23-26, 2006, pp. 81-98 (2006)
- [6] Jan Draisma and Johan P. de Jong, *On the Casas-Alvero conjecture*, EMS Newsletter June 2011, pp. 29-33 (2011) + erratum available at `http://www.win.tue.nl/~jdraisma/`
- [7] Hans-Christian Graf von Bothmer, Oliver Labs, Josef Schicho and Christiaan van de Woestijne, *The Casas-Alvero conjecture for infinitely many degrees*, Journal of Algebra 316(1), pp. 224-230 (2007)
- [8] János Kollár, *Sharp effective Nullstellensatz*, Journal of the American Mathematical Society 1(4), pp. 963-975 (1988)
- [9] A. M. Legendre, *Théorie des nombres*, Firmin Didot Frères, Paris (1830)
- [10] V. V. Prasolov, *Polynomials*, Algorithms and Computation in Mathematics 11, Springer (2009)
- [11] P. Ribenboim, *The theory of classical valuations*, Monographs in Mathematics, Springer (1999)
- [12] H. Verhoek, *Some remarks about a polynomial conjecture of Casas-Alvero*, Séminaire Bourbakettes, Paris (2009)

Departement Wiskunde, KU Leuven
Celestijnenlaan 200B, 3001 Leuven (Heverlee), Belgium
*E-mail address:*`wouter.castryck@wis.kuleuven.be`

Institut de Recherche Mathématique Avancée, Université de Strasbourg
7 Rue René Descartes, 67084 Strasbourg CEDEX, France
*E-mail address:*`robert.laterveer@math.unistra.fr`

Institut de Recherche Mathématique Avancée, Université de Strasbourg
7 Rue René Descartes, 67084 Strasbourg CEDEX, France
*E-mail address:*`myriam.ounaies@unistra.fr`


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
