<!-- source: https://arxiv.org/html/2605.04551v1 | converted from HTML -->

A Ceiling Continued Fraction Approach to the Erdős-Straus Conjecture: Heuristic finiteness of counterexamples

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2605.04551v1 [math.NT] 06 May 2026

# A Ceiling Continued Fraction Approach to the Erdős-Straus Conjecture: Heuristic finiteness of counterexamples

Andrés Ventas Email address: [aventas.avp@gmail.com][3]

###### Abstract.

We introduce the Ceiling Continued Fractions (FCT) framework for constructing three-term Egyptian fraction representations in the Erdős–Straus conjecture. The approach exploits divisor structures of shifted integers p + i p+i rather than congruence-based techniques. Computational tests on 10 9 10^{9} primes in ranges around 10 17 10^{17} and 10 52 10^{52}, and 10 7 10^{7} primes around 10 131 10^{131}, show no counterexamples with very small search depth. We derive a super-polynomial upper bound on the failure probability; its convergence, together with the Borel–Cantelli lemma, provides heuristic evidence that counterexamples, if any exist, form a finite set.

###### Key words and phrases:

Erdős-Straus conjecture, Egyptian fractions, Continued Fractions, Borel–Cantelli lemma, Vaughan’s bounds

###### 2020 Mathematics Subject Classification

11D68, 11Y16

## 1. Introduction

The Erdős-Straus conjecture asserts that for every integer n ≥ 2 n\geq 2, the equation 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z admits a solution in positive integers x, y, z x,y,z. While the conjecture has been verified for vast ranges, the most resistant cases remain those where n n is a prime p p satisfying specific quadratic residues. In this work, we focus on Mordell-type primes, p ≡ { 1, 11 2, 13 2, 17 2, 19 2, 23 2 } ( mod 840) p\equiv\{1,11^{2},13^{2},17^{2},19^{2},23^{2}\}\pmod{840} [5].

Although the conjecture has been computationally verified for n ≤ 10 17 n\leq 10^{17}, a formal proof remains elusive [2]. Historical approaches by Mordell and Vaughan [6] focused on identifying specific residues of n n for which solutions are guaranteed. However, these methods overlook the internal divisor structure of external numbers p + i p+i. This paper presents the FCT framework, which shifts the paradigm from a congruence-based search to a targeted identification of relationships between the prime p p and the divisor sets of associated numbers p + i p+i in the orbit of p p.

The index i i of these associated numbers is what we define as the source. The orbit is the search limit relative to p p beyond which the theory indicates that FCT-type solutions cannot exist.

Under the FCT framework, the solution for primes of the form 4 ​ k + 3 4k+3 is immediate and yields a two-term result. This property provides a compelling heuristic: if a two-term representation is guaranteed for any prime of the form 4 ​ k + 3 4k+3, should we not expect a three-term representation for any prime p p of the form 4 ​ k + 1 4k+1 whenever a related external number has a 4 ​ k + 3 4k+3 divisor? Could the problem then be reduced to identifying that 4 ​ k + 3 4k+3 divisor and its associated number? Once a suitable 4 ​ k + 3 4k+3 divisor of these related numbers is identified, the FCT algorithm automatically yields the full three-term solution for p p, eliminating the need for further exhaustive searches.

By computing the success probability associated with the model, we derive a bound for the expected value of failure exhibiting super-polynomial decay,

 | E ⁡ ( F p) ≪ N ​ exp ⁡ ( − 1 12 ​ ( ln ⁡ p) 2), E(F_{p})\ll N\exp\big(-\tfrac{1}{12}(\ln p)^{2}\big), |  |

where N N is the sample size and p p the search range. This decay suggests that failures become extremely rare as p grows. Furthermore, this behavior is consistent with the expectation that only finitely many counterexamples may exist.

## 2. The FCT Framework

A Ceiling Continued Fraction (FCT) is obtained by applying the Euclidean algorithm using the ceiling function. The coefficients ⌈ c 0, c 1, c 2, … ⌉ \lceil c_{0},c_{1},c_{2},\dots\rceil generate convergents through the negative recurrence:

 | p i = c i ​ p i − 1 − p i − 2, q i = c i ​ q i − 1 − q i − 2 p_{i}=c_{i}p_{i-1}-p_{i-2},\quad q_{i}=c_{i}q_{i-1}-q_{i-2} |  | (1) |

where ( p − 1, q − 1) = ( 1, 0) (p_{-1},q_{-1})=(1,0).

###### Theorem 2.1 (Sum by Pairs).

For any x = ⌈ c 0, c 1, c 2, … ⌉ x=\lceil c_{0},c_{1},c_{2},\dots\rceil with convergent numerators p 0, p 1, p 2, … p_{0},p_{1},p_{2},\dots, the reciprocal is given by:

 | 1 x = 1 p 0 + 1 p 0 ​ p 1 + 1 p 1 ​ p 2 + … \frac{1}{x}=\frac{1}{p_{0}}+\frac{1}{p_{0}p_{1}}+\frac{1}{p_{1}p_{2}}+\dots |  | (2) |

###### Proof.

Given the Euler sum x = a 0 + a 0 ​ a 1 + a 0 ​ a 1 ​ a 2 + … x=a_{0}+a_{0}a_{1}+a_{0}a_{1}a_{2}+\dots and its continued fraction [3, p.159] x = a 0 − a 1 1 + a 1 ​ − ​ a 2 1 + a 2 ​ − ​ a 3 1 + a 3 ​ − − ⋯ x=a_{0}-\frac{a_{1}}{1+a_{1}}\genfrac{}{}{0.0pt}{}{}{-}\frac{a_{2}}{1+a_{2}}\genfrac{}{}{0.0pt}{}{}{-}\frac{a_{3}}{1+a_{3}}\genfrac{}{}{0.0pt}{}{}{-}\cdots we transform it so that the numerators are 1 1,

 | x \displaystyle x | = 1 1 a 0 − 1 ( 1 + a 1) ​ a 0 a 1 − 1 ( 1 + a 2) ​ a 1 a 2 ​ a 0 − 1 ( 1 + a 3) ​ a 2 ​ a 0 a 3 ​ a 1 − ⋯ \displaystyle=\dfrac{1}{\frac{1}{a_{0}}}\genfrac{}{}{0.0pt}{}{}{-}\frac{1}{\frac{(1+a_{1})a_{0}}{a_{1}}}\genfrac{}{}{0.0pt}{}{}{-}\frac{1}{\frac{(1+a_{2})a_{1}}{a_{2}a_{0}}}\genfrac{}{}{0.0pt}{}{}{-}\frac{1}{\frac{(1+a_{3})a_{2}a_{0}}{a_{3}a_{1}}}\genfrac{}{}{0.0pt}{}{}{-}\cdots |  |

 |  | by definition of F ​ C ​ T \displaystyle\text{by definition of $FCT$} |  |

 | 1 x \displaystyle\dfrac{1}{x} | = ⌈ 1 a 0, ( 1 + a 1) ​ a 0 a 1, ⋯, ( 1 + a i) a i − 1 a i − 3 ⋯ a i a i − 2 a i − 4 ⋯, ⋯ ⌉. \displaystyle=\bigg\lceil\dfrac{1}{a_{0}},\dfrac{(1+a_{1})a_{0}}{a_{1}},\cdots,\dfrac{(1+a_{i})a_{i-1}a_{i-3}\cdots}{a_{i}a_{i-2}a_{i-4}\cdots},\cdots\bigg\rceil. |  |

We denote this continued fraction as 1 x = ⌈ c 0, c 1, ⋯, c i, ⋯ ⌉ \dfrac{1}{x}=\lceil c_{0},c_{1},\cdots,c_{i},\cdots\rceil, we equate the coefficients and solve for the a i a_{i},

 |  | a 0 = 1 c 0, a 1 = a 0 c 1 − a 0, a 2 = a 1 c 2 ​ a 0 − a 1, a 3 = a 2 ​ a 0 c 3 ​ a 1 − a 2 ​ a 0, ⋯ \displaystyle a_{0}=\frac{1}{c_{0}},\ a_{1}=\frac{a_{0}}{c_{1}-a_{0}},\ a_{2}=\frac{a_{1}}{c_{2}a_{0}-a_{1}},\ a_{3}=\frac{a_{2}a_{0}}{c_{3}a_{1}-a_{2}a_{0}},\cdots |  |

 |  | a i = a i − 1 a i − 3 ⋯ c i ​ a i − 2 ​ a i − 4 ​ … − a i − 1 ​ a i − 3 − ⋯. \displaystyle a_{i}=\frac{a_{i-1}a_{i-3}\cdots}{c_{i}a_{i-2}a_{i-4}...-a_{i-1}a_{i-3}\cdots}. |  |

Using the identity of the numerators of the convergents p i = c i ​ p i − 1 − p i − 2 p_{i}=c_{i}p_{i-1}-p_{i-2}, we have

 | a 0 \displaystyle a_{0} | = 1 c 0 = 1 p 0. \displaystyle=\dfrac{1}{c_{0}}=\dfrac{1}{p_{0}}. |  |

 | p 1 \displaystyle p_{1} | = c 1 p 0 − 1, a 1 = a 0 c 1 − a 0 = 1 / c 0 c 1 − ( 1 / c 0) = 1 c 1 ​ c 0 − 1 = 1 c 1 ​ p 0 − 1 = p − 1 p 1. \displaystyle=c_{1}p_{0}-1,\ a_{1}=\frac{a_{0}}{c_{1}-a_{0}}=\dfrac{1/c_{0}}{c_{1}-(1/c_{0})}=\dfrac{1}{c_{1}c_{0}-1}=\frac{1}{c_{1}p_{0}-1}=\dfrac{p_{-1}}{p_{1}}. |  |

 | a i \displaystyle a_{i} | = a i − 1 ​ a i − 3 ​ … c i ​ a i − 2 ​ a i − 4 ​ … − a i − 1 ​ a i − 3 ​ … = p i − 2 p i. \displaystyle=\frac{a_{i-1}a_{i-3}...}{c_{i}a_{i-2}a_{i-4}...-a_{i-1}a_{i-3}...}=\frac{p_{i-2}}{p_{i}}. |  |

Now we substitute in x x and use telescopic sum

 | x \displaystyle x | = a 0 + a 0 ​ a 1 + a 0 ​ a 1 ​ a 2 + a 0 ​ a 1 ​ a 2 ​ a 3 + ⋯ \displaystyle=a_{0}+a_{0}a_{1}+a_{0}a_{1}a_{2}+a_{0}a_{1}a_{2}a_{3}+\cdots |  |

 |  | = 1 p 0 + 1 p 0 ​ 1 p 1 + 1 p 0 ​ 1 p 1 ​ p 0 p 2 + 1 p 0 ​ 1 p 1 ​ p 0 p 2 ​ p 1 p 3 + ⋯ \displaystyle=\dfrac{1}{p_{0}}+\dfrac{1}{p_{0}}\dfrac{1}{p_{1}}+\dfrac{1}{p_{0}}\dfrac{1}{p_{1}}\dfrac{p_{0}}{p_{2}}+\dfrac{1}{p_{0}}\dfrac{1}{p_{1}}\dfrac{p_{0}}{p_{2}}\dfrac{p_{1}}{p_{3}}+\cdots |  |

 |  | = 1 p 0 + 1 p 0 ​ 1 p 1 + 1 p 1 ​ 1 p 2 + 1 p 2 ​ 1 p 3 + ⋯ \displaystyle=\frac{1}{p_{0}}+\frac{1}{p_{0}}\dfrac{1}{p_{1}}+\dfrac{1}{p_{1}}\frac{1}{p_{2}}+\dfrac{1}{p_{2}}\dfrac{1}{p_{3}}+\cdots |  |

 |  | = 1 p 0 + ∑ i = 0 ∞ 1 p i ​ 1 p i + 1. \displaystyle=\dfrac{1}{p_{0}}+\sum_{i=0}^{\infty}\dfrac{1}{p_{i}}\dfrac{1}{p_{i+1}}. |  |

(Proof in [7]). ∎

To solve the Erdős-Straus conjecture for a prime p p, we seek an integer 4 ​ k 4k such that the FCT of p / 4 ​ k p/4k (denoted as F ​ C ​ T ​ ( p, 4 ​ k) FCT(p,4k)) has exactly three terms. Thus, we obtain:

 | 4 ​ k p = 1 p 0 + 1 p 0 ​ p 1 + 1 p 1 ​ p 2 \frac{4k}{p}=\frac{1}{p_{0}}+\frac{1}{p_{0}p_{1}}+\frac{1}{p_{1}p_{2}} |  | (3) |

where p 2 = p p_{2}=p.

For this type of solution, the problem reduces to finding a residue r 0 r_{0} such that:

###### Proposition 2.2 (Inner Congruence).

A three-term unit fraction solution exists if:

 | 4 ​ k + 1 ≡ 0 ( mod r 0), where ​ r 0 = c 0 ⋅ 4 ​ k − p 4k+1\equiv 0\pmod{r_{0}},\quad\text{where }r_{0}=c_{0}\cdot 4k-p |  | (4) |

with c 0 = ⌈ p / 4 ​ k ⌉ c_{0}=\lceil p/4k\rceil.

###### Proof.

Using the ceiling Euclidean algorithm:

p p | 4 ​ k 4k | c 0 c_{0} | r 0 r_{0} |

4 ​ k 4k | r 0 r_{0} | c 1 c_{1} | 1 1 |

r 1 r_{1} | 1 1 | c 2 = r 1 c_{2}=r_{1} | 0 0 |

∎

It is important to maintain the ceiling condition for c 0 c_{0} and c 1 c_{1}. Here, c 0 c_{0} acts as the basis that relates the FCT to the sources.

###### Theorem 2.3 (Divisors of External Sources).

For any prime p ≡ 1 ( mod 4) p\equiv 1\pmod{4}, if p + i p+i has a divisor d ≡ 3 ( mod 4) d\equiv 3\pmod{4} such that 4 ​ i | ( p + d) 4i\mid(p+d), there exists a three-term direct solution given by F ​ C ​ T ​ ( p, ( p + d) / i) FCT(p,(p+d)/i).

###### Proof.

Given p p and its FCT coefficients ⌈ c 0 = i, c 1, c 2 = d ⌉ \lceil c_{0}=i,c_{1},c_{2}=d\rceil, the numerators of the convergents of the continued fraction are p j = { i, i ​ c 1 − 1, p } p_{j}=\{i,ic_{1}-1,p\}, and the denominators are q j = { 1, c 1, 4 ​ k } q_{j}=\{1,c_{1},4k\}. Solving for c 1 c_{1} using the negative recurrence rules of ceiling continued fractions:

 | p + i \displaystyle p+i | = k 0 ⋅ d. ( d divides p + i) \displaystyle=k_{0}\cdot d.\quad\text{($d$ divides $p+i$)} |  | (5) |

 | p \displaystyle p | = ( i ​ c 1 − 1) ​ d − i. (recurrence of the last coefficient for numerators) \displaystyle=(ic_{1}-1)d-i.\quad\text{(recurrence of the last coefficient for numerators)} |  |

 | c 1 \displaystyle c_{1} | = ( p + i d + 1) / i. \displaystyle=\bigg(\dfrac{p+i}{d}+1\bigg)/i. |  |

 | d ⋅ c 1 − 1 \displaystyle d\cdot c_{1}-1 | = 4 ​ k. (recurrence of the last coefficient for denominators) \displaystyle=4k.\quad\text{(recurrence of the last coefficient for denominators)} |  |

 | 4 ​ k \displaystyle 4k | = p + d + i i − 1 = p + d i. \displaystyle=\dfrac{p+d+i}{i}-1=\dfrac{p+d}{i}. |  |

 | k \displaystyle k | = p + d 4 ​ i. \displaystyle=\dfrac{p+d}{4i}. |  |

Since p ≡ 1 ( mod 4) p\equiv 1\pmod{4} and d ≡ 3 ( mod 4) d\equiv 3\pmod{4}, p + d p+d is a multiple of 4 4. The condition 4 ​ i | ( p + d) 4i\mid(p+d) ensures that 4 ​ k 4k is an integer, completing the Egyptian fraction representation via Theorem [2.1] with F ​ C ​ T ​ ( p, 4 ​ k) = F ​ C ​ T ​ ( p, ( p + d) / i) FCT(p,4k)=FCT(p,(p+d)/i). ∎

We obtain as a consequence a useful sufficient condition for p + 1 p+1:

###### Corollary 2.4.

For every prime p = 4 ​ k + 1 p=4k+1 where p + 1 p+1 possesses at least one factor d ≡ 3 ( mod 4) d\equiv 3\pmod{4}, the conjecture holds.

### 2.1. Orbits and Sources

The orbit of p p, denoted as O ⁡ ( p) O(p), is the distance limit for associated numbers p + i p+i beyond which FCT-type solutions are no longer feasible.

From the Euclidean ceiling algorithm, if 4 ​ k > p 4k>p, then c 0 = 1 c_{0}=1 and r 0 = 4 ​ k − p r_{0}=4k-p. Since the subsequent step requires r 0 r_{0} to divide 4 ​ k + 1 4k+1, the maximum 4 ​ k 4k is bounded near 2 ​ p 2p. Beyond this point, r 0 ≈ 2 ​ p + d − p = p + d r_{0}\approx 2p+d-p=p+d, which cannot divide 2 ​ p + 1 2p+1 for d > 1 d>1. Thus, we define the orbit as O ⁡ ( p) = 2 ​ p O(p)=2p.

The sources are the indices i i (or associated numbers p + i p+i) where we search for divisors within O ⁡ ( p) O(p). These sources are determined by c 0 c_{0}, which varies in steps of ⌈ p / 4 ​ k ⌉ \lceil p/4k\rceil. The number of distinct values of i i in this range is given by M ⁡ ( p) = 2 ​ p / 4 = p M(p)=2\sqrt{p/4}=\sqrt{p}.

Sources are clustered at one end of the range and sparsely distributed at the other.

For example, let p = 73 p=73; the set of indices i = ⌈ 73 / 4 ​ k ⌉ i=\lceil 73/4k\rceil yields the sequence:

 | { 19, 10, 7, 5, 4, 4, 3, 3, 3, …, 2, 2, 2 ​ …, 1, 1, 1, … }. \{19,10,7,5,4,4,3,3,3,\dots,2,2,2\dots,1,1,1,\dots\}. |  |

The set of distinct values is { 19, 10, 7, 5, 4, 3, 2, 1 } \{19,10,7,5,4,3,2,1\}, resulting in M ⁡ ( p) = 8 ≈ 73 M(p)=8\approx\sqrt{73} unique sources.

### 2.2. Computational Acceleration

While the following properties generates solutions that intersect with the source analysis above, it provides a computationally trivial sieve that resolves the vast majority of cases in O ⁡ ( ln ⁡ p) O(\ln p) time, thereby explaining the empirical speed of the algorithm.

###### Theorem 2.5 (Grid of Congruences).

For any pair c 1 = 4 ​ k 1 + 3 c_{1}=4k_{1}+3, c 2 = 4 ​ k 2 + 3 c_{2}=4k_{2}+3, the product minus one, m = c 1 ​ c 2 − 1 m=c_{1}c_{2}-1, forms an infinite system of congruences p ≡ − c 1 ( mod m) p\equiv-c_{1}\pmod{m} and p ≡ − c 2 ( mod m) p\equiv-c_{2}\pmod{m} yielding solutions for p = 4 ​ k + 1 p=4k+1.

###### Proof.

Using the denominators of the convergents, c 1 ​ c 2 − 1 = 4 ​ k c_{1}c_{2}-1=4k, so c 1 ​ c 2 = 4 ​ k + 1 c_{1}c_{2}=4k+1. From the numerators:

 | p \displaystyle p | = ( c 1 ​ c 0 − 1) ​ c 2 − c 0 = ( c 1 ​ c 2 − 1) ​ c 0 − c 2. \displaystyle=(c_{1}c_{0}-1)c_{2}-c_{0}=(c_{1}c_{2}-1)c_{0}-c_{2}. |  | (6) |

 | p \displaystyle p | ≡ − c 2 ( mod c 1 ​ c 2 − 1). \displaystyle\equiv-c_{2}\pmod{c_{1}c_{2}-1}. |  |

The interchanging of c 1 c_{1} and c 2 c_{2} yields the second congruence. ∎

The structure mirrors that of the primes: each new progression, associated with a larger 4 ​ k + 3 4k+3 factor of a solution, covers additional elements without achieving full coverage.

Setting c 0 = 1 c_{0}=1 and c 1 ​ c 2 = 4 ​ k + 1 c_{1}c_{2}=4k+1 generates two arithmetic progressions: ( 4 ​ k − c 1) + 4 ​ k (4k-c_{1})+4k and ( 4 ​ k − c 2) + 4 ​ k (4k-c_{2})+4k, forming an extensive grid:

− 3 ( mod 8, 20, 32, 44, …) -3\pmod{8,20,32,44,\ldots}

− 7 ( mod 20, 48, 76, 104, 132, …) -7\pmod{20,48,76,104,132,\ldots}

− 11 ( mod 32, 76, 120, 164, 208, 252, …) -11\pmod{32,76,120,164,208,252,\ldots}

⋯ \cdots

The FCT framework provides a direct three-step solution once 4 ​ k 4k is identified (Theorem [2.1]).

We also have another significant sufficient condition for solutions,

###### Theorem 2.6 (Factors of External Sources).

For any prime p ≡ 1 ( mod 4) p\equiv 1\pmod{4}, if p + 4 ​ k i + 3 p+4k_{i}+3 has a factor f ≡ 2 ( mod 3 ​ k i) f\equiv 2\pmod{3k_{i}}, a three-term direct solution exists with F ​ C ​ T ​ ( p, 4 ​ f) FCT(p,4f).

###### Proof.

Given p p and its FCT coefficients ⌈ c 0, c 1, c 2 = 4 k i + 3 ⌉ \lceil c_{0},c_{1},c_{2}=4k_{i}+3\rceil, the numerators of the convergents are p i = { c 0, c 0 ​ c 1 − 1, p } p_{i}=\{c_{0},c_{0}c_{1}-1,p\}, and the denominators are q i = { 1, c 1, 4 ​ f } q_{i}=\{1,c_{1},4f\}, with f = ( p + 4 ​ k i + 3) / ( 3 ​ k i + 2) f=(p+4k_{i}+3)/(3k_{i}+2). Using the recurrences of the convergents:

 | p \displaystyle p | = c 2 ​ c 1 ​ c 0 − c 2 − c 0 \displaystyle=c_{2}c_{1}c_{0}-c_{2}-c_{0} |  | (7) |

 |  | = ( c 2 ​ c 1 − 1) ​ c 0 − c 2 \displaystyle=(c_{2}c_{1}-1)c_{0}-c_{2} |  |

 |  | = 4 ​ f ​ c 0 − ( 4 ​ k i + 3) \displaystyle=4fc_{0}-(4k_{i}+3) |  |

 | p + 4 ​ k i + 3 \displaystyle p+4k_{i}+3 | = 4 ​ f ​ c 0 \displaystyle=4fc_{0} |  |

 | c 0 \displaystyle c_{0} | = p + 4 ​ k i + 3 4 ​ f \displaystyle=\dfrac{p+4k_{i}+3}{4f} |  |

fulfilling the condition of the theorem. We obtain the solution by F ​ C ​ T ​ ( p, 4 ​ f) FCT(p,4f) through Theorem [2.1]. ∎

## 3. Expected Value of failure for Mordell-type Primes

This study focuses exclusively on primes of Mordell type

p ≡ { 1, 11 2, 13 2, 17 2, 19 2, 23 2 } ( mod 840) p\equiv\{1,11^{2},13^{2},17^{2},19^{2},23^{2}\}\pmod{840} [5].

### 3.1. Independence of the sources

As demonstrated in the Divisor Sources Theorem [2.3], finding a solution requires identifying a divisor d ≡ 3 ( mod 4) d\equiv 3\pmod{4} within an appropriate source i i by examining the divisors of p + i p+i.

Since the space of potential successes is restricted to divisors within p + i p+i, we have as an average in each source approximately ln ⁡ p \ln p opportunities to identify a favorable divisor.

To estimate the probability of potential failures, we adopt the standard heuristic of Cramér’s model [1], treating the divisibility of shifted primes p + i p+i by distinct integers as asymptotically independent events.

Note that restricting the analysis to Mordell-type primes the correlation in the divisors of p + i p+i are expected to behave more closely to the independent random model.

The non-intersection between solutions from different sources is ensured as they provide solutions with different c 0 c_{0} coefficients.

### 3.2. Divisors of External Sources (fd: f0, f1, f2)

Section 2.1 established that the number of distinct available sources in the orbit of p p is M ⁡ ( p) = p M(p)=\sqrt{p}. There are three main categories of divisor sources, each with complementary characteristics.

The probability that a prime p p fails to find a solution across its p \sqrt{p} independent sources is the joint probability of failure across these three types.

Therefore, failure is defined as the inability to find a suitable divisor among the ln ⁡ p \ln{p} candidates across all p \sqrt{p} independent sources.

#### 3.2.1. Source 1 (f1)

For source f 1 f_{1} to yield a solution, it must contain at least one divisor d ≡ 3 ( mod 4) d\equiv 3\pmod{4}. The probability that a random integer lacks prime factors of this form is governed by the Landau-Ramanujan constant K ≈ 0.764 K\approx 0.764 [4].

Because source f 1 f_{1} is computed over all 4 ​ k + 3 4k+3 residues, its failure probability is fundamentally limited by the Landau-Ramanujan bound:

 | P f ​ 1 ​ ( F) ∼ K ln ⁡ p. P_{f1}(F)\sim\frac{K}{\sqrt{\ln p}}. |  | (8) |

In this case, the expectation does not depend on M M (the number of sources) as f ​ 1 f1 is a single, fixed source.

#### 3.2.2. Consecutive Sources 𝐢 ≥ 𝟐 \mathbf{i\geq 2} (f2)

The source c 0 = i c_{0}=i corresponds to solutions derived from the divisors of p + i p+i, obtained with consecutive i i.

By Theorem [2.3], source i i requires exact division by 4 ​ i 4i; thus, the probability of success for a given divisor d ≡ 4 ​ k + 3 d\equiv 4k+3 of p + i p+i is 1 / i 1/i.

For a source i i, the residues progress in steps of 4 ​ i 4i, skipping i − 1 i-1 residues of the form 4 ​ k + 3 4k+3.

For i ≥ 2 i\geq 2, we evaluate consecutive sources across the range i = [2, p / 2] i=[2,\sqrt{p}/2]. We seek divisors of the form 4 ​ k + 3 4k+3 in a given source, which comprise approximately half of the odd divisors of ( p + c 0) (p+c_{0}). This equates to 1 / 4 1/4 of total divisors, augmented by the contribution of even ( p + c 0) (p+c_{0}) sources, ensuring the usable fraction exceeds 1 / 3 1/3.

 | P f ​ 2 ​ ( F) \displaystyle P_{f2}(F) | ≪ ∏ i = 2 ⌊ p / 2 ⌋ ( 1 − 1 i) 1 3 ​ ln ⁡ p \displaystyle\ll\prod_{i=2}^{\lfloor\sqrt{p}/2\rfloor}\bigg(1-\dfrac{1}{i}\bigg)^{\frac{1}{3}\ln{p}} |  |

 |  | = ( 1 ⌊ p / 2 ⌋) 1 3 ​ ln ⁡ p (telescoping product). \displaystyle=\bigg(\dfrac{1}{\lfloor\sqrt{p}/2\rfloor}\bigg)^{\frac{1}{3}\ln{p}}\quad\text{(telescoping product).} |  |

 |  | ≪ ( 2 p) 1 3 ​ ln ⁡ p \displaystyle\ll\bigg(\dfrac{2}{\sqrt{p}}\bigg)^{\frac{1}{3}\ln{p}} |  |

Restricting the search to the first M M sources within a sample of size N N yields:

 | P f ​ 2 ​ ( F ( M, N)) ≪ ( 1 M) 1 3 ​ ln ⁡ N. P_{f2}(F_{(M,N)})\ll\bigg(\dfrac{1}{M}\bigg)^{\frac{1}{3}\ln{N}}. |  |

#### 3.2.3. Sources of 𝐟𝟎 \mathbf{f0}

We group the dispersed sources under the name f 0 f_{0}. We explore up to M M variations of the ceiling coefficient c 0 c_{0} obtained as ⌈ p / 4 ​ k ⌉ \lceil p/4k\rceil (with a maximum of M = p / 2 M=\sqrt{p}/2). For each source, we have slightly more than 1 3 ​ ln ⁡ p \frac{1}{3}\ln{p} candidate divisors of the form 4 ​ k + 3 4k+3. The probability that none of these combinations satisfies the required congruence 4 ​ i | ( p + d) 4i\mid(p+d) is the product of their individual failure probabilities, resulting in the product of an arithmetic progression:

 | P f ​ 0 ​ ( F M) \displaystyle P_{f0}(F_{M}) | ≪ ∏ i = 1 M ( 1 − 4 ​ i p) 1 3 ​ ln ⁡ p = ∏ i = 1 M ( p − 4 ​ i p) 1 3 ​ ln ⁡ p \displaystyle\ll\prod_{i=1}^{M}\left(1-\frac{4i}{p}\right)^{\frac{1}{3}\ln{p}}=\prod_{i=1}^{M}\left(\frac{p-4i}{p}\right)^{\frac{1}{3}\ln p} |  | (9) |

 |  | = [1 p M ​ Γ ⁡ ( p 4 + 1) Γ ⁡ ( p 4 − M + 1) ⋅ 4 M] 1 3 ​ ln ⁡ p. \displaystyle=\bigg[\dfrac{1}{p^{M}}\dfrac{\Gamma\left(\frac{p}{4}+1\right)}{\Gamma\left(\frac{p}{4}-M+1\right)}\cdot 4^{M}\bigg]^{\frac{1}{3}\ln p}. |  |

This was obtained by reversing the direction of the arithmetic progression (from p − M + 4 ​ i p-M+4i up to p p). Now applying Stirling’s approximation ( Γ ⁡ ( x + M) Γ ⁡ ( x) ≈ x M \frac{\Gamma{(x+M)}}{\Gamma(x)}\approx x^{M}),

 | P f ​ 0 ​ ( F M) \displaystyle P_{f0}(F_{M}) | ≪ [( 1 p) M ⋅ 4 M ⋅ ( p − M 4) M] 1 3 ​ ln ⁡ p \displaystyle\ll\bigg[\bigg(\dfrac{1}{p}\bigg)^{M}\cdot 4^{M}\cdot\left(\frac{p-M}{4}\right)^{M}\bigg]^{\frac{1}{3}\ln p} |  | (10) |

 |  | = [( p − M p)] M 3 ​ ln ⁡ p. \displaystyle=\bigg[\bigg(\dfrac{p-M}{p}\bigg)\bigg]^{\frac{M}{3}\ln p}. |  |

We see that a significantly large M M is required to force this probability of failure away from 1 1.

### 3.3. Expected Value of failure cases

###### Heuristic 3.1 (Expected number of failures under the FCT framework).

Under the Cramér-type heuristic probabilistic model described in Section 3.1, the expected number of failures among N N consecutive primes of magnitude p p satisfying Mordell-type congruence conditions is given by

 | E ⁡ ( N) ≪ N ​ exp ⁡ ( − 1 12 ​ ( ln ⁡ p) 2). E(N)\ll N\exp\Big(-\frac{1}{12}(\ln p)^{2}\Big). |  | (11) |

One could derive the expectation by combining the three previous cases covering all sources in the orbit of p p. However, the dominant contribution arises from the f ​ 2 f2 sources. Therefore,

 | P Total Failure ≪ ( 2 p) 1 3 ​ ln ⁡ p = exp ⁡ ( − 1 6 ​ ( ln ⁡ p) 2 + ln ⁡ 2 3 ​ ( ln ⁡ p)). \displaystyle P_{\text{Total Failure}}\ll\bigg(\dfrac{2}{\sqrt{p}}\bigg)^{\frac{1}{3}\ln{p}}=\exp\bigg(-\frac{1}{6}(\ln p)^{2}+\frac{\ln 2}{3}(\ln p)\bigg). |  |

Operating on the exponent term,

 |  | − 1 6 ​ ( ln ⁡ p) 2 + ln ⁡ 2 3 ​ ( ln ⁡ p) = − 1 6 ​ ( ln ⁡ p) 2 ​ ( 1 − 2 ​ ln ⁡ 2 ln ⁡ p). \displaystyle-\frac{1}{6}(\ln p)^{2}+\frac{\ln 2}{3}(\ln p)=-\frac{1}{6}(\ln p)^{2}\bigg(1-\frac{2\ln 2}{\ln p}\bigg). |  |

 |  | For sufficiently large ​ p, ( 1 − 2 ​ ln ⁡ 2 ln ⁡ p) > 0.5. \displaystyle\text{For sufficiently large }p,\bigg(1-\frac{2\ln 2}{\ln p}\bigg)>0.5. |  |

Therefore, we have

 | P Total Failure ≪ exp ⁡ ( − 1 12 ​ ( ln ⁡ p) 2). P_{\text{Total Failure}}\ll\exp\Big(-\frac{1}{12}(\ln p)^{2}\Big). |  |

Multiplying this by the sample size N N yields the expectation shown previously.

For a search restricted to M M sources applied to a set of N N primes of magnitude p p, the expected value satisfies the following asymptotic bound:

 | E ⁡ ( N) ≪ N ​ ( 1 M) 1 3 ​ ln ⁡ p. E(N)\ll N\left(\frac{1}{M}\right)^{\frac{1}{3}\ln p}. |  |

This suggests that the expected number of failures can be made smaller than 1 1 even for relatively small values of M M, which are computationally accessible. The expected number of failures decays at a super-polynomial rate. While existing theories establish global probability bounds [2], the FCT algorithm demonstrates the existence of solutions across a wide range of local configurations, yielding a super-polynomially decaying upper bound.

### 3.4. Algorithm Complexity and Empirical Acceleration

The algorithmic implementation of the FCT framework consists of two distinct phases for a given prime p p:

1. (1)

Initial Sieve (Grid): Check small prime congruences based on Theorem 2.5.

2. (2)

Source Scanning: Iterate through M M distinct sources i ≤ M ⁡ ( p) i\leq M(p), computing the divisors of p + i p+i and verifying the condition 4 ​ i | ( p + d) 4i\mid(p+d).

#### 3.4.1. Theoretical Worst-Case Complexity

As established in Section 2.1, the number of distinct sources in the full orbit O ⁡ ( p) O(p) is bounded by M ⁡ ( p) = ⌊ p ⌋ M(p)=\lfloor\sqrt{p}\rfloor. For each source, the average number of divisors to test is O ⁡ ( ln ⁡ p) O(\ln p). Consequently, a naive scan of the entire theoretical search space yields a worst-case time complexity per prime of:

 | 𝒯 theoretical ​ ( p) = O ⁡ ( p ⋅ ln ⁡ p ⋅ ℱ ⁡ ( p)), \mathcal{T}_{\text{theoretical}}(p)=O\big(\sqrt{p}\cdot\ln p\cdot\mathcal{F}(p)\big), |  | (12) |

where ℱ ⁡ ( p) \mathcal{F}(p) represents the cost of factoring p + i p+i.

#### 3.4.2. Empirical Complexity and the Truncation Constant

While the bound M ⁡ ( p) = p M(p)=\sqrt{p} dictates the theoretical maximum, empirical evidence demonstrates a dramatic *early termination*phenomenon. In computational stress tests across 10 9 10^{9} Mordell-type primes (magnitudes 10 17 10^{17} and 10 52 10^{52}), and 10 7 10^{7} Mordell-type primes at 10 131 10^{131}, a solution was always located within the first M = 40 M=40 sources.

This behavior is consistent with the super-polynomial decay of the expected failure probability derived in Section 3.2. Specifically, the probability of failure when truncated to a constant number of sources M 0 M_{0} is bounded by:

 | P ⁡ ( F M 0) ≪ ( 1 M 0) 1 3 ​ ln ⁡ p. P(F_{M_{0}})\ll\left(\frac{1}{M_{0}}\right)^{\frac{1}{3}\ln p}. |  |

For M 0 = 40 M_{0}=40 and p ≈ 10 17 p\approx 10^{17}, this theoretical estimate is vanishingly small ( ≈ 10 − 10 \approx 10^{-10}), explaining why the algorithm never requires iterating up to p \sqrt{p}.

Therefore, for all practical purposes, the observed runtime is governed not by p p, but by the *fixed*truncation limit M max = 40 M_{\text{max}}=40 (or a slightly higher chosen constant). The empirical complexity per prime is effectively:

 | 𝒯 empirical ​ ( p) ≈ O ⁡ ( M max ⋅ ℱ ⁡ ( p)) ≈ O ⁡ ( ℱ ⁡ ( p)), \mathcal{T}_{\text{empirical}}(p)\approx O\big(M_{\text{max}}\cdot\mathcal{F}(p)\big)\approx O(\mathcal{F}(p)), |  | (13) |

with an additional O ⁡ ( ln ⁡ p) O(\ln p) cost for the initial sieve.

#### 3.4.3. Performance Justification

The exceptional throughput reported in Table 2 ( 0.00055 0.00055 ms/p at p ≈ 10 17 p\approx 10^{17}, 0.0015 0.0015 ms/p at p ≈ 10 52 p\approx 10^{52}, and 0.0019 0.0019 ms/p at p ≈ 10 131 p\approx 10^{131}) is a direct consequence of this truncation. Since M max M_{\text{max}} is constant, the runtime scales primarily with the cost of integer factorization ℱ ⁡ ( p) \mathcal{F}(p) rather than with the square root of p p.

### 3.5. Theoretical Comparisons

Table 1 illustrates how the FCT framework reduces expected failures compared to classical bounds. We consider two theoretical sample sizes: one of 10 7 10^{7} Mordell-type primes, and another of 10 17 10^{17} or 10 52 10^{52}, matching the magnitude of the respective ranges.

For the Vaughan column, we evaluate the bound E Vaughan ( N) ≈ N exp ( − ( ( log N) 2 / 3) / c) E_{\text{Vaughan}}(N)\approx N\exp\big(-((\log N)^{2/3})/c\big), with c = 1 c=1, [6], using the sample size N N of primes in the given range. Note that Vaughan’s bound applies to the full set of numbers, whereas the FCT model is restricted to the harder Mordell subclass; therefore, the comparison is intended to illustrate the relative decay rates rather than provide a direct like-for-like estimate.

Sources | Range | Sam. Size | E[Fail.] (FCT) | E[Fail.] (Vaughan) |

M = 20 M=20 | 10 17 10^{17} | N = 10 7 N=10^{7} | 1.1 × 10 − 10 1.1\times 10^{-10} | 4.64 × 10 − 5 4.64\times 10^{-5} |

M = 20 M=20 | 10 17 10^{17} | N = 10 17 N=10^{17} | 1 1 | 4.64 × 10 5 4.64\times 10^{5} |

M = 40 M=40 | 10 17 10^{17} | N = 10 17 N=10^{17} | 1.2 × 10 − 4 1.2\times 10^{-4} | 4.64 × 10 5 4.64\times 10^{5} |

M = 20 M=20 | 10 52 10^{52} | N = 10 7 N=10^{7} | 8.27 × 10 − 45 8.27\times 10^{-45} | 2.15 × 10 − 28 2.15\times 10^{-28} |

M = 20 M=20 | 10 52 10^{52} | N = 10 52 N=10^{52} | 1.18 1.18 | 2.15 × 10 17 2.15\times 10^{17} |

M = 40 M=40 | 10 52 10^{52} | N = 10 52 N=10^{52} | 1.2 × 10 − 12 1.2\times 10^{-12} | 2.15 × 10 17 2.15\times 10^{17} |

Table 1. Theoretical estimation of unresolved cases ( p ≈ 10 17 p\approx 10^{17} and p ≈ 10 52 p\approx 10^{52}): FCT vs. Vaughan’s bound.

The expected value of failure in the FCT model decreases as the number of sources M M increases. It also decreases as the magnitude p p grows, due to the larger quantity of available divisors.

## 4. Probabilistic Interpretation and Borel–Cantelli Lemma

We emphasize that the probabilistic quantities introduced in this section should be interpreted in a heuristic sense.

The model assumes approximate independence between sources and divisor events, as explained in section 3.1.

We model the failure events F p F_{p} as random events within a heuristic probabilistic framework. In this framework, P ⁡ ( F p) P(F_{p}) represents the modeled probability that a Mordell-type prime p p fails to admit an FCT solution.

### 4.1. Heuristic finiteness of failure events

Let F p F_{p} denote the event that a Mordell-type prime p p does not admit an FCT solution. As established in Heuristic 3.1, the failure probability satisfies:

 | P ⁡ ( F p) ≪ exp ⁡ ( − 1 12 ​ ( ln ⁡ p) 2) = p − 1 12 ​ ln ⁡ p. P(F_{p})\ll\exp\!\Big(-\frac{1}{12}(\ln p)^{2}\Big)=p^{-\frac{1}{12}\ln p}. |  |

We consider the cumulative expected number of failures up to a bound X X:

 | ∑ p ≤ X P ⁡ ( F p) \displaystyle\sum_{p\leq X}P(F_{p}) | = ∑ p ≤ X exp ⁡ ( − 1 12 ​ ( ln ⁡ p) 2) \displaystyle=\sum_{p\leq X}\exp\!\Big(-\frac{1}{12}(\ln p)^{2}\Big) |  |

 |  | = ∑ p ≤ X p − 1 12 ​ ln ⁡ p. \displaystyle=\sum_{p\leq X}p^{-\frac{1}{12}\ln p}. |  |

Since p − 1 12 ​ ln ⁡ p < p − 2 p^{-\frac{1}{12}\ln p}<p^{-2} for sufficiently large p p, and since the series ∑ p p − 2 \sum_{p}p^{-2} converges, it follows that the above series converges.

###### Corollary 4.1.

Under Heuristic 3.1, the convergence of the series ∑ P ⁡ ( F p) \sum P(F_{p}), together with the Borel–Cantelli lemma, suggests that the set of Mordell-type primes failing to admit an FCT solution is finite.

## 5. Experimental Results and Empirical Probabilities

The FCT algorithm was stress-tested against 10 9 10^{9} Mordell-type primes at 10 17 10^{17}, 10 52 10^{52}, and 10 9 10^{9} primes at 10 131 10^{131} using PARI/GP (v2.17.3) compiled with ”gp2c” on a 3.0 GHz processor with 10 10 cores.

The optional parameters used were:

A search depth of sources M = 96 M=96.

Factor limit 2 24 2^{24}.

Size of congruences list for the initial sieve L ​ 4 ​ k = 1026 L4k=1026.

In the ranges of 10 52 10^{52} and 10 131 10^{131} an increase in the factorization limit significantly penalizes performance. Divisors are obtained through the factors contained within this limit.

Range | Sample size | Total time | Time per prime | ms/p out of sieve |

10 17 10^{17} | 10 9 10^{9} | 9.1 9.1 min | 0.00055 0.00055 ms | 0.97 0.97 ms |

10 52 10^{52} | 10 9 10^{9} | 24.98 24.98 min | 0.0015 0.0015 ms | 202 202 ms |

10 131 10^{131} | 10 7 10^{7} | 0.32 0.32 min | 0.0019 0.0019 ms | 211 211 ms |

Table 2. Empirical results on 10 17 10^{17}, 10 52 10^{52}, and 10 131 10^{131} ranges

###### Example 5.1.

Consider the solution triple ( p, 4 ​ k, source) (p,4k,\text{source}) for a large prime p p:

 | p \displaystyle p | = 11756638905368616011414050501310355554617941987811609 \displaystyle=11756638905368616011414050501310355554617941987811609 |  |

 | 4 ​ k \displaystyle 4k | = 1960490455533318809410064185473201382030123301988960 \displaystyle=1960490455533318809410064185473201382030123301988960 |  |

 | source \displaystyle\text{source} | = f ​ 2.6 \displaystyle=f2.6 |  |

Following Theorem 2.3, the value 4 ​ k 4k is derived from a divisor of p + 6 p+6, specifically:

 | d = 6303827831296845046334611528852737562797824122151. d=6303827831296845046334611528852737562797824122151. |  |

By applying the FCT algorithm to the expression p / 4 ​ k p/4k, we obtain:

 | F ​ C ​ T ​ ( p / 4 ​ k) = [6,311, 6303827831296845046334611528852737562797824122151]. FCT(p/4k)=[6,311,6303827831296845046334611528852737562797824122151]. |  |

Finally, by invoking Theorem 2.1 and scaling the denominators of the solution by k k, we yield the three-term representation [x, y, z] [x,y,z]:

 | x \displaystyle x | = 2940735683299978214115096278209802073045184952983440. \displaystyle=2940735683299978214115096278209802073045184952983440. |  |

 | y \displaystyle y | = 5484472049354459369324654558861280866229269937314115600. \displaystyle=5484472049354459369324654558861280866229269937314115600. |  |

 | z \displaystyle z | = 10746492911807896894698146950272337341766761173665849 \displaystyle=10746492911807896894698146950272337341766761173665849 |  |

 |  | 238916016046288627773111370797373460663594211541333400. \displaystyle\quad 238916016046288627773111370797373460663594211541333400. |  |

where z z is a 108-digit integer.

One can verify directly that 4 / p = 1 / x + 1 / y + 1 / z. 4/p=1/x+1/y+1/z.

## 6. Conclusion

The FCT framework presents an interesting paradox: by restricting analysis to a smaller subset of potential solutions, it derives formulas that substantially improve upon classical probability bounds. This efficiency stems from exploiting specific algebraic properties that multiply strategic solution locations.

We highlight three important consequences:

- •

A solution exists whenever p + 1 p+1 has a divisor of the form 4 ​ k + 3 4k+3.

- •

The probability of failure decays super-polynomially, suggesting statistical certainty as M → ∞ M\to\infty

- •

The probabilistic model suggests that infinitely many failure events should not occur.

Acknowledgements. The author acknowledges the “Sementeira” group at the University of Santiago de Compostela for sustaining the spirit of mathematical problem solving.

## References

- [1] H. Cramér, On the order of magnitude of the difference between consecutive prime numbers, Acta Arithmetica 2 (1936), no. 1, 23–46.
- [2] C. Elsholtz and T. Tao, The number of solutions of 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z, Math. Comp. 82 (2013), 1737–1773. https://arxiv.org/abs/1201.3173 arXiv:1201.3173
- [3] S. Khrushchev, Orthogonal Polynomials and Continued Fractions, Encyclopedia of Mathematics and its Applications, vol. 122, Cambridge University Press, 2008, p. 159.
- [4] P. Moree and J. Cazaran, On a claim of Ramanujan in his first letter to Hardy, Expositiones Mathematicae 17 (1999), 289–311.
- [5] N. J. A. Sloane, The On-Line Encyclopedia of Integer Sequences, Primes of the form x 2 + 840 ​ y 2 x^{2}+840y^{2}, Sequence A139665. https://oeis.org/A139665
- [6] R. C. Vaughan, On a problem of Erdős, Straus and Schinzel, Mathematika 17 (1970), 193–198.
- [7] A. Ventas, Relación entre series infinitas, fraccións continuas teito e constantes. Aplicacións (Parte I), 2025. https://retallosdematematicas.blogspot.com/2025/04/relacion-entre-series-infinitas.html

Email addres:


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:
