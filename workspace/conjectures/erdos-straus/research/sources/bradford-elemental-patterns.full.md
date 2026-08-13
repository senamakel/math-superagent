<!-- source: https://arxiv.org/html/2403.16047v1 | converted from HTML -->

Elemental Patterns from the Erdős Straus Conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2403.16047v1 [math.NT] 24 Mar 2024

# Elemental Patterns from the Erdős Straus Conjecture

Kyle Bradford

###### Abstract.

This paper makes the following conjecture: For every prime p p there exists a positive integer x x with ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and a positive divisor d | x 2 d|x^{2} so that either

(1) d mod ( 4 ​ x − p) ≡ − p ​ x d\bmod\left(4x-p\right)\equiv-px

or

(2) d ≤ x d\leq x and d mod ( 4 ​ x − p) ≡ − x d\bmod\left(4x-p\right)\equiv-x.

Furthermore this paper proves that the solutions to these modular equations are in one-to-one correspondence with the solutions of the diophantine equation used in the Erdős Straus conjecture.

## 1. Introductory Material

The Erdős Straus conjecture suggests for any integer n ≥ 2 n\geq 2 there exists positive integers x, y x,y and z z so that the following diophantine equation holds.

(1) |  | 4 n = 1 x + 1 y + 1 z \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z} |  |

Introduced by Paul Erdős and Ernst Straus in the late 1940s [7], the problem was quickly picked up by other notable mathematicians such as Richard Obláth [13], Luigi Rosati [15], Koichi Yamamoto [26] and Louis Mordell [12]. Richard Guy included this problem in his book on Unsolved Problems in Number Theory along with many other results on Egyptian fractions [8]. Notable papers use analytic number theory, abstractions or computational methods to analyze this problem [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], but this paper introduces an insight that will govern how this problem will be resolved. My earlier work described how it suffices to show the conjecture holds for any prime p p [3]. In this previous work I insisted that x ≤ y ≤ z x\leq y\leq z and I continue this convention. It was shown that p ∤ x p\nmid x, p | z p|z and p p sometimes divides y y. It was also shown that p 2 p^{2} does not divide x, y x,y or z z. Using the common nomenclature, a solution is of type I if p ∤ y p\nmid y and is of type II if p | y p|y. This paper discusses new results and then motivates further research in the following sections. All proofs are shown in the final section.

## 2. New Results

The results in this paper are very subtle but quite illuminating. Ultimately, for each prime p p, I build both necessary and sufficient conditions to describe the solutions of ( 1) solely through its smallest solution value, x x. The following proposition and corollary derive a sufficient condition for finding type I solutions to ( 1).

###### Proposition 1.

Suppose for a prime p p there exists a positive integer x x with ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and a positive divisor d | x 2 d|x^{2} so that d mod ( 4 ​ x − p) ≡ − p ​ x d\bmod\left(4x-p\right)\equiv-px.

Then letting

 | y \displaystyle y | = p ​ x + d 4 ​ x − p \displaystyle=\frac{px+d}{4x-p} |  |

 | z \displaystyle z | = p ⁡ ( x + p ⁡ ( x 2 d)) 4 ​ x − p \displaystyle=\frac{p\left(x+p\left(\frac{x^{2}}{d}\right)\right)}{4x-p} |  |

we see that x, y x,y and z z are positive integers with x ≤ y ≤ z x\leq y\leq z and p ∤ y p\nmid y.

###### Corollary 1.

Suppose for a prime p p there exists a positive integer x x with ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and a positive divisor d | x 2 d|x^{2} so that d mod ( 4 ​ x − p) ≡ − p ​ x d\bmod\left(4x-p\right)\equiv-px.

Then we have met a sufficient condition to find a type I solution to ( 1).

The following proposition and corollary derive a sufficient condition for finding type II solutions to ( 1).

###### Proposition 2.

Suppose for a prime p p there exists a positive integer x x with ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and a positive divisor d | x 2 d|x^{2} so that d ≤ x d\leq x and d mod ( 4 ​ x − p) ≡ − x d\bmod\left(4x-p\right)\equiv-x.

Then letting

 | y \displaystyle y | = p ⁡ ( x + d) 4 ​ x − p \displaystyle=\frac{p(x+d)}{4x-p} |  |

 | z \displaystyle z | = p ⁡ ( x + x 2 d) 4 ​ x − p \displaystyle=\frac{p\left(x+\frac{x^{2}}{d}\right)}{4x-p} |  |

we see that x, y x,y and z z are positive integers with x ≤ y ≤ z x\leq y\leq z and p | y p|y.

###### Corollary 2.

Suppose for a prime p p there exists a positive integer x x with ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and a positive divisor d | x 2 d|x^{2} so that d ≤ x d\leq x and d mod ( 4 ​ x − p) ≡ − x d\bmod\left(4x-p\right)\equiv-x.

Then we have met a sufficient condition to find a type II solution to ( 1).

The following two propositions derive the necessary conditions for finding type I and type II solutions to ( 1) respectively.

###### Proposition 3.

Suppose for a prime p p there exist positive integers x ≤ y ≤ z x\leq y\leq z that satisfy ( 1) and p ∤ y p\nmid y.

Then it is necessarily true that ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and a positive divisor d | x 2 d|x^{2} exists so that

 | ( 1) \displaystyle(1) | d mod ( 4 ​ x − p) ≡ − p ​ x \displaystyle\quad d\bmod\left(4x-p\right)\equiv-px |  |

 | ( 2) \displaystyle(2) | y = p ​ x + d 4 ​ x − p \displaystyle\quad y=\frac{px+d}{4x-p} |  |

 | ( 3) \displaystyle(3) | z = p ⁡ ( x + p ⁡ ( x 2 d)) 4 ​ x − p. \displaystyle\quad z=\frac{p\left(x+p\left(\frac{x^{2}}{d}\right)\right)}{4x-p}. |  |

###### Proposition 4.

Suppose for a prime p p there exist positive integers x ≤ y ≤ z x\leq y\leq z that satisfy ( 1) and p | y p|y.

Then it is necessarily true that ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and a positive divisor d | x 2 d|x^{2} exists so that

 | ( 1) \displaystyle(1) | d ≤ x \displaystyle\quad d\leq x |  |

 | ( 2) \displaystyle(2) | d mod ( 4 ​ x − p) ≡ − x \displaystyle\quad d\bmod\left(4x-p\right)\equiv-x |  |

 | ( 3) \displaystyle(3) | y = p ⁡ ( x + d) 4 ​ x − p \displaystyle\quad y=\frac{p(x+d)}{4x-p} |  |

 | ( 4) \displaystyle(4) | z = p ⁡ ( x + x 2 d) 4 ​ x − p. \displaystyle\quad z=\frac{p\left(x+\frac{x^{2}}{d}\right)}{4x-p}. |  |

Indeed I have now developed both the necessary and sufficient conditions for solving the Erdős Straus conjecture. The solutions are in one-to-one correspondence with the modular identities in propositions 1 and 2. This is a key result because it reduces the conjecture to one dimension. That is to say, for every prime p p we need to find at least one pair, x x and d d, meeting the appropriate conditions as functions of p p to prove the Erdős Straus conjecture. I summarize this in the following conjecture.

###### Conjecture 1.

For every prime p p there exists a positive integer x x with ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and a positive divisor d | x 2 d|x^{2} so that either

(1) d mod ( 4 ​ x − p) ≡ − p ​ x d\bmod\left(4x-p\right)\equiv-px

or

(2) d ≤ x d\leq x and d mod ( 4 ​ x − p) ≡ − x d\bmod\left(4x-p\right)\equiv-x.

## 3. Computation motivation toward a solution

The strength of this approach is that I have yet to employ different methodologies for different modular classes of prime numbers. At this point you can use my conjecture to derive Mordell’s identities for all primes p p except possibly for primes p p such that p mod 840 ∈ { 1,121,169,289,361, 529 } p\bmod 840\in\{1,121,169,289,361,529\}. It has been suggested that this problem can be solved through quadratic residues, and it may be no coincidence that my results suggest d | x 2 d|x^{2}. My approach begs for x x to depend on a divisor of ⌈ p 4 ⌉ \left\lceil\frac{p}{4}\right\rceil, but this is clearly not the case for all primes. Figure 1 may motivate you to find a similar pattern, although I only graphed primes less than 100 for clarity.

Figure 1. This graphs primes less than 100 against the possible solution values x in the Erdős Straus conjecture

To make this more clear I include the following two tables. In table 1 I consider type I solutions for p < 100 p<100 and I consider writing x = ⌈ p 4 ⌉ + k x=\left\lceil\frac{p}{4}\right\rceil+k. Notice now that 0 ≤ k ≤ ⌈ p 4 ⌉ 0\leq k\leq\left\lceil\frac{p}{4}\right\rceil. The table provides for each prime p p every possible value k k that appears for type I solutions. Notice that for prime p ≠ 2 p\neq 2 so that 1 mod 24 ≢ p mod 24 1\bmod 24\not\equiv p\bmod 24 we are guaranteed to have a type I solution when k = 0 k=0. Also notice for primes p p so that 3 mod 4 ≡ p 3\bmod 4\equiv p we are guaranteed to have type I solutions when k k is a divisor of ⌈ p 4 ⌉ \left\lceil\frac{p}{4}\right\rceil.

2 |  |  |  |  |  |  |  |  |  |  |  |

3 | 0 | 1 |  |  |  |  |  |  |  |  |  |

5 | 0 |  |  |  |  |  |  |  |  |  |  |

7 | 0 | 1 | 2 |  |  |  |  |  |  |  |  |

11 | 0 | 1 | 3 |  |  |  |  |  |  |  |  |

13 | 0 | 1 |  |  |  |  |  |  |  |  |  |

17 | 0 | 1 |  |  |  |  |  |  |  |  |  |

19 | 0 | 1 | 3 | 5 |  |  |  |  |  |  |  |

23 | 0 | 1 | 2 | 3 | 4 | 6 |  |  |  |  |  |

29 | 0 | 3 |  |  |  |  |  |  |  |  |  |

31 | 0 | 1 | 2 | 4 | 8 |  |  |  |  |  |  |

37 | 0 | 2 | 4 | 6 |  |  |  |  |  |  |  |

41 | 0 | 1 | 7 |  |  |  |  |  |  |  |  |

43 | 0 | 1 | 4 | 7 | 11 |  |  |  |  |  |  |

47 | 0 | 1 | 2 | 3 | 4 | 5 | 9 | 12 |  |  |  |

53 | 0 | 1 | 2 | 6 | 7 | 10 |  |  |  |  |  |

59 | 0 | 1 | 3 | 4 | 5 | 9 | 10 | 15 |  |  |  |

61 | 0 | 2 | 5 | 7 | 8 |  |  |  |  |  |  |

67 | 0 | 1 | 3 | 4 | 7 | 11 | 13 | 17 |  |  |  |

71 | 0 | 1 | 2 | 3 | 4 | 6 | 8 | 9 | 12 | 14 | 18 |

73 | 1 | 2 | 3 |  |  |  |  |  |  |  |  |

79 | 0 | 1 | 2 | 4 | 5 | 8 | 10 | 16 | 20 |  |  |

83 | 0 | 1 | 3 | 5 | 6 | 7 | 9 | 15 | 21 |  |  |

89 | 0 | 1 | 3 | 16 |  |  |  |  |  |  |  |

97 | 0 | 1 | 3 | 9 |  |  |  |  |  |  |  |

Table 1. This table provides for each prime less than 100 all of the possible k values for type I solutions.

In table 2 I consider type II solutions for primes p < 100 p<100. I again consider writing x = ⌈ p 4 ⌉ + k x=\left\lceil\frac{p}{4}\right\rceil+k so that 0 ≤ k ≤ ⌈ p 4 ⌉ 0\leq k\leq\left\lceil\frac{p}{4}\right\rceil. For a given prime p p, notice that there are some type II solutions that have x x values that have no type I solutions. For example, see that p = 41 p=41 has k = 3 k=3, which corresponds to x = 14 x=14. There are no type I solutions when p = 41 p=41 and x = 14 x=14.

2 | 0 |  |  |  |

3 | 0 |  |  |  |

5 | 0 |  |  |  |

7 | 0 |  |  |  |

11 | 0 | 1 |  |  |

13 | 0 |  |  |  |

17 | 0 | 1 |  |  |

19 | 0 | 1 |  |  |

23 | 0 | 2 |  |  |

29 | 0 | 2 |  |  |

31 | 0 | 1 |  |  |

37 | 0 |  |  |  |

41 | 0 | 1 | 3 |  |

43 | 0 | 1 |  |  |

47 | 0 | 2 | 4 |  |

53 | 0 | 4 |  |  |

59 | 0 | 1 | 2 | 5 |

61 | 0 | 2 |  |  |

67 | 0 | 1 |  |  |

71 | 0 | 1 | 2 | 6 |

73 | 1 | 2 |  |  |

79 | 0 | 1 |  |  |

83 | 0 | 3 | 7 |  |

89 | 0 | 1 | 3 | 7 |

97 | 0 | 1 | 3 |  |

Table 2. This table provides for each prime less than 100 all of the possible k values for type II solutions.

There are other patterns to consider. My colleagues and I have considered tables like these for up to five digit primes, but this paper should outline a motivation for finding a pattern and proving the conjecture.

## 4. Proofs

###### Proof.

Proposition 1

Let p p be a prime, x x be a positive integer with ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and d d be a positive divisor d | x 2 d|x^{2} so that d mod ( 4 ​ x − p) ≡ − p ​ x d\bmod\left(4x-p\right)\equiv-px.

It should be clear that p ≠ 2 p\neq 2 because if p = 2 p=2, then both x x and d d must be 1 1 by definition and we cannot have 1 mod 2 ≡ 0 1\bmod 2\equiv 0.

First, note that x x is a positive integer by definition.

Next, note that if d mod ( 4 ​ x − p) ≡ − p ​ x d\bmod\left(4x-p\right)\equiv-px, then ( p ​ x + d) mod ( 4 ​ x − p) ≡ 0 (px+d)\bmod\left(4x-p\right)\equiv 0. This implies that ( 4 ​ x − p) | ( p ​ x + d) (4x-p)|(px+d). By definition, p, x p,x and d d are all positive, so p ​ x + d px+d is positive. Because ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil, it should be clear that 4 ​ x − p 4x-p is also positive. Letting

 | y = p ​ x + d 4 ​ x − p y=\frac{px+d}{4x-p} |  |

we see that y y is a positive integer. We also see that p ∤ y p\nmid y. To show this we assume, for the sake of contradiction, that p | y p|y. This implies that p | ( p ​ x + d) p|(px+d) which further implies that p | d p|d. If p | d p|d, then p | x 2 p|x^{2}; however, from the definition of x x, we see that x < p x<p. p p cannot divide x x or x 2 x^{2}. This creates a contradiction, implying that p ∤ y p\nmid y.

Finally, note that ( p 2 ​ x 2 d) ​ d = p 2 ​ x 2 = ( − p ​ x) 2 \left(\frac{p^{2}x^{2}}{d}\right)d=p^{2}x^{2}=(-px)^{2} in ℤ \mathbb{Z}, so we get the following modular equation:

(2) |  | ( p 2 ​ x 2 d) mod ( 4 ​ x − p) ⋅ d mod ( 4 ​ x − p) ≡ ( − p ​ x) mod ( 4 ​ x − p) ⋅ ( − p ​ x) mod ( 4 ​ x − p) \left(\frac{p^{2}x^{2}}{d}\right)\bmod(4x-p)\cdot d\bmod(4x-p)\equiv(-px)\bmod(4x-p)\cdot(-px)\bmod(4x-p) |  |

Recall that d mod ( 4 ​ x − p) ≡ − p ​ x d\bmod(4x-p)\equiv-px, so this equation becomes:

(3) |  | ( p 2 ​ x 2 d) mod ( 4 ​ x − p) ⋅ ( − p ​ x) mod ( 4 ​ x − p) ≡ ( − p ​ x) mod ( 4 ​ x − p) ⋅ ( − p ​ x) mod ( 4 ​ x − p) \left(\frac{p^{2}x^{2}}{d}\right)\bmod(4x-p)\cdot(-px)\bmod(4x-p)\equiv(-px)\bmod(4x-p)\cdot(-px)\bmod(4x-p) |  |

When p ≠ 2 p\neq 2, we see that − p ​ x -px and 4 ​ x − p 4x-p are coprime. To show this let m m be a positive integer so that m | ( − p ​ x) m|(-px) and m | ( 4 ​ x − p) m|(4x-p). We necessarily see that m m must divide ( − 4) ​ ( − p ​ x) + ( − p) ​ ( 4 ​ x − p) = p 2 (-4)(-px)+(-p)(4x-p)=p^{2}. This makes m = 1, p m=1,p or p 2 p^{2}. For sake of contradiction, assume that m = p m=p. This implies that p | ( 4 ​ x − p) p|(4x-p), which further implies that p | x p|x, but this is impossible as x ≤ ⌈ p 2 ⌉ x\leq\left\lceil\frac{p}{2}\right\rceil. Next, for the sake of contradiction, assume that m = p 2 m=p^{2}. This implies that p 2 | ( − p ​ x) p^{2}|(-px), which further implies that p | x p|x. Again, this is impossible. We conclude that m = 1 m=1, so we have that − p ​ x -px and 4 ​ x − p 4x-p are indeed coprime. We see that ( − p ​ x) mod ( 4 ​ x − p) (-px)\bmod(4x-p) is a unit, with an inverse element in the group ( ℤ / ( 4 ​ x − p) ​ ℤ) × \left(\mathbb{Z}/\penalty(4x-p)\mathbb{Z}\right)^{\times}. Applying this inverse element on the right to either side of ( 3), we have that ( p 2 ​ x 2 d) mod ( 4 ​ x − p) ≡ − p ​ x \left(\frac{p^{2}x^{2}}{d}\right)\bmod(4x-p)\equiv-px. We see then that ( p ​ x + ( p 2 ​ x 2 d)) mod ( 4 ​ x − p) ≡ 0 \left(px+\left(\frac{p^{2}x^{2}}{d}\right)\right)\bmod(4x-p)\equiv 0. This implies that ( 4 ​ x − p) | ( p ​ x + ( p 2 ​ x 2 d)) (4x-p)|\left(px+\left(\frac{p^{2}x^{2}}{d}\right)\right). Note that p, x, d p,x,d and 4 ​ x − p 4x-p are positive integers. Letting

 | z = p ⁡ ( x + p ⁡ ( x 2 d)) 4 ​ x − p z=\frac{p\left(x+p\left(\frac{x^{2}}{d}\right)\right)}{4x-p} |  |

we see that z z is a positive integer.

To finish this proof we show that x ≤ y ≤ z x\leq y\leq z.

First consider when x < ⌈ p 2 ⌉ x<\left\lceil\frac{p}{2}\right\rceil. We see that

 | x ≤ p 2 + d 4 ​ x x\leq\frac{p}{2}+\frac{d}{4x} |  |

This implies that 4 ​ x 2 < 2 ​ p ​ x + d 4x^{2}<2px+d, x ⁡ ( 4 ​ x − p) < p ​ x + d x(4x-p)<px+d and

 | x < p ​ x + d 4 ​ x − p ≤ y x<\frac{px+d}{4x-p}\leq y |  |

Next consider when x = ⌈ p 2 ⌉ x=\left\lceil\frac{p}{2}\right\rceil. Because p ≠ 2 p\neq 2, we have that x = p + 1 2 x=\frac{p+1}{2}. We see that

 | y \displaystyle y | = p ⁡ ( p + 1 2) + d 4 ​ ( p + 1 2) − p \displaystyle=\frac{p\left(\frac{p+1}{2}\right)+d}{4\left(\frac{p+1}{2}\right)-p} |  |

 |  | = p ⁡ ( p + 1) + 2 ​ d 2 ​ ( p + 2) \displaystyle=\frac{p(p+1)+2d}{2(p+2)} |  |

 |  | = p + 1 2 + d − ( p + 1) p + 2 \displaystyle=\frac{p+1}{2}+\frac{d-(p+1)}{p+2} |  |

Because y y is an integer, we see that ( p + 2) | ( d − ( p + 1)) (p+2)|(d-(p+1)). For 0 < d < ( p + 1) 0<d<(p+1), we see that

 | − 1 < d − ( p + 1) p + 2 < 0 -1<\frac{d-(p+1)}{p+2}<0 |  |

This implies that d ≥ ( p + 1) d\geq(p+1) and x = p + 1 2 ≤ y x=\frac{p+1}{2}\leq y.

In either scenario we are guaranteed to have x ≤ y x\leq y.

Because d | x 2 d|x^{2}, we see that d ≤ x 2 ≤ p ​ x d\leq x^{2}\leq px. This implies that d 2 ≤ p 2 ​ x 2 d^{2}\leq p^{2}x^{2}. We see then that

 | d ≤ ( p 2 ​ x 2 d) d\leq\left(\frac{p^{2}x^{2}}{d}\right) |  |

We see then that

 | p ​ x + d 4 ​ x − p ≤ p ​ x + ( p 2 ​ x 2 d) 4 ​ x − p \frac{px+d}{4x-p}\leq\frac{px+\left(\frac{p^{2}x^{2}}{d}\right)}{4x-p} |  |

We see that y ≤ z y\leq z. ∎

###### Proof.

Corollary 1

Let p p be prime.

Suppose that a positive integer x x exists with ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and a positive divisor d | x 2 d|x^{2} exists so that d mod ( 4 ​ x − p) ≡ − p ​ x d\bmod\left(4x-p\right)\equiv-px.

Under these conditions, we see from Proposition 1 that positive integers x, y x,y and z z exist with x ≤ y ≤ z x\leq y\leq z and p ∤ y p\nmid y so that

 | 1 x + 1 y + 1 z \displaystyle\frac{1}{x}+\frac{1}{y}+\frac{1}{z} | = 1 x + 4 ​ x − p p ​ x + d + 4 ​ x − p p ⁡ ( x + p ⁡ ( x 2 d)) \displaystyle=\frac{1}{x}+\frac{4x-p}{px+d}+\frac{4x-p}{p\left(x+p\left(\frac{x^{2}}{d}\right)\right)} |  |

 |  | = p ⁡ ( p ​ x + d) ​ ( x + p ⁡ ( x 2 d)) + p ​ x ​ ( 4 ​ x − p) ​ ( x + p ⁡ ( x 2 d)) + x ⁡ ( p ​ x + d) ​ ( 4 ​ x − p) p ​ x ​ ( p ​ x + d) ​ ( x + p ⁡ ( x 2 d)) \displaystyle=\frac{p\left(px+d\right)\left(x+p\left(\frac{x^{2}}{d}\right)\right)+px\left(4x-p\right)\left(x+p\left(\frac{x^{2}}{d}\right)\right)+x\left(px+d\right)\left(4x-p\right)}{px\left(px+d\right)\left(x+p\left(\frac{x^{2}}{d}\right)\right)} |  |

 |  | = 2 ​ p 2 ​ x 2 + p 3 ​ x 3 d + d ​ p ​ x + 4 ​ p ​ x 3 + 4 ​ p 2 ​ x 4 d − p 2 ​ x 2 − p 3 ​ x 3 d + 4 ​ p ​ x 3 + 4 ​ d ​ x 2 − p 2 ​ x 2 − d ​ p ​ x p ⁡ ( 2 ​ p ​ x 3 + p 2 ​ x 4 d + d ​ x 2) \displaystyle=\frac{2p^{2}x^{2}+\frac{p^{3}x^{3}}{d}+dpx+4px^{3}+\frac{4p^{2}x^{4}}{d}-p^{2}x^{2}-\frac{p^{3}x^{3}}{d}+4px^{3}+4dx^{2}-p^{2}x^{2}-dpx}{p\left(2px^{3}+\frac{p^{2}x^{4}}{d}+dx^{2}\right)} |  |

 |  | = 4 ​ ( 2 ​ p ​ x 3 + p 2 ​ x 4 d + d ​ x 2) p ⁡ ( 2 ​ p ​ x 3 + p 2 ​ x 4 d + d ​ x 2) \displaystyle=\frac{4\left(2px^{3}+\frac{p^{2}x^{4}}{d}+dx^{2}\right)}{p\left(2px^{3}+\frac{p^{2}x^{4}}{d}+dx^{2}\right)} |  |

 |  | = 4 p \displaystyle=\frac{4}{p} |  |

This is a type I solution to ( 1). ∎

###### Proof.

Proposition 2

Let p p be a prime, x x be a positive integer with ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and d d be a positive divisor d | x 2 d|x^{2} so that d ≤ x d\leq x and d mod ( 4 ​ x − p) ≡ − x d\bmod\left(4x-p\right)\equiv-x.

First, note that x x is a positive integer by definition.

Next, note that if d mod ( 4 ​ x − p) ≡ − x d\bmod\left(4x-p\right)\equiv-x, then ( x + d) mod ( 4 ​ x − p) ≡ 0 (x+d)\bmod\left(4x-p\right)\equiv 0. This implies that ( 4 ​ x − p) | ( x + d) (4x-p)|(x+d). By definition, p, x, d p,x,d and 4 ​ x − p 4x-p are all positive, so p ⁡ ( x + d) p(x+d) is positive. Letting

 | y = p ⁡ ( x + d) 4 ​ x − p y=\frac{p(x+d)}{4x-p} |  |

we see that y y is a positive integer. Because ( 4 ​ x − p) | ( x + d) (4x-p)|(x+d), we see that p | y p|y in that scenario.

Finally, note that ( x 2 d) ​ d = x 2 = ( − x) 2 \left(\frac{x^{2}}{d}\right)d=x^{2}=(-x)^{2} in ℤ \mathbb{Z}, so we get the following modular equation:

(4) |  | ( x 2 d) mod ( 4 ​ x − p) ⋅ d mod ( 4 ​ x − p) ≡ ( − x) mod ( 4 ​ x − p) ⋅ ( − x) mod ( 4 ​ x − p) \left(\frac{x^{2}}{d}\right)\bmod(4x-p)\cdot d\bmod(4x-p)\equiv(-x)\bmod(4x-p)\cdot(-x)\bmod(4x-p) |  |

Recall that d mod ( 4 ​ x − p) ≡ − x d\bmod(4x-p)\equiv-x, so this equation becomes:

(5) |  | ( x 2 d) mod ( 4 ​ x − p) ⋅ ( − x) mod ( 4 ​ x − p) ≡ ( − x) mod ( 4 ​ x − p) ⋅ ( − x) mod ( 4 ​ x − p) \left(\frac{x^{2}}{d}\right)\bmod(4x-p)\cdot(-x)\bmod(4x-p)\equiv(-x)\bmod(4x-p)\cdot(-x)\bmod(4x-p) |  |

We see that − x -x and 4 ​ x − p 4x-p are coprime. To show this let m m be a positive integer so that m | ( − x) m|(-x) and m | ( 4 ​ x − p) m|(4x-p). We necessarily see that m m must divide ( − 4) ​ ( − x) + ( − 1) ​ ( 4 ​ x − p) = p (-4)(-x)+(-1)(4x-p)=p. This makes m = 1 m=1 or p p. For sake of contradiction assume that m = p m=p. This implies that p | ( − x) p|(-x), which further implies that p | x p|x. We have shown this to be impossible. We conclude that m = 1 m=1, so we have that − x -x and 4 ​ x − p 4x-p are indeed coprime. We see that ( − x) mod ( 4 ​ x − p) (-x)\bmod(4x-p) is a unit, with an inverse element in the group ( ℤ / ( 4 ​ x − p) ​ ℤ) × \left(\mathbb{Z}/\penalty(4x-p)\mathbb{Z}\right)^{\times}. Applying this inverse element on the right to either side of ( 5), we have that ( x 2 d) mod ( 4 ​ x − p) ≡ − x \left(\frac{x^{2}}{d}\right)\bmod(4x-p)\equiv-x. We see then that ( x + ( x 2 d)) mod ( 4 ​ x − p) ≡ 0 \left(x+\left(\frac{x^{2}}{d}\right)\right)\bmod(4x-p)\equiv 0. This implies that ( 4 ​ x − p) | ( x + ( x 2 d)) (4x-p)|\left(x+\left(\frac{x^{2}}{d}\right)\right). Note that p, x, d p,x,d and 4 ​ x − p 4x-p are positive integers. Letting

 | z = p ⁡ ( x + ( x 2 d)) 4 ​ x − p z=\frac{p\left(x+\left(\frac{x^{2}}{d}\right)\right)}{4x-p} |  |

we see that z z is a positive integer.

To finish this proof we show that x ≤ y ≤ z x\leq y\leq z.

Because p | y p|y, we see that p ≤ y p\leq y. By definition we see that x ≤ p x\leq p. This implies that x ≤ y x\leq y.

Because d ≤ x d\leq x, we have d 2 ≤ x 2 d^{2}\leq x^{2}. We see that

 | d ≤ ( x 2 d) d\leq\left(\frac{x^{2}}{d}\right) |  |

which implies that

 | p ⁡ ( x + d) 4 ​ x − p ≤ p ⁡ ( x + ( x 2 d)) 4 ​ x − p \frac{p(x+d)}{4x-p}\leq\frac{p\left(x+\left(\frac{x^{2}}{d}\right)\right)}{4x-p} |  |

We see that y ≤ z y\leq z. ∎

###### Proof.

Corollary 2

Let p p be prime.

Suppose that positive integer x x with ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil and a positive divisor d | x 2 d|x^{2} so that d ≤ x d\leq x and d mod ( 4 ​ x − p) ≡ − x d\bmod\left(4x-p\right)\equiv-x.

Under these conditions, we see that positive integers x, y x,y and z z exist with x ≤ y ≤ z x\leq y\leq z and p | y p|y so that

 | 1 x + 1 y + 1 z \displaystyle\frac{1}{x}+\frac{1}{y}+\frac{1}{z} | = 1 x + 4 ​ x − p p ⁡ ( x + d) + 4 ​ x − p p ⁡ ( x + x 2 d) \displaystyle=\frac{1}{x}+\frac{4x-p}{p(x+d)}+\frac{4x-p}{p\left(x+\frac{x^{2}}{d}\right)} |  |

 |  | = p ⁡ ( x + d) ​ ( x + x 2 d) + x ⁡ ( 4 ​ x − p) ​ ( x + x 2 d) + x ⁡ ( x + d) ​ ( 4 ​ x − p) p ​ x ​ ( x + d) ​ ( x + x 2 d) \displaystyle=\frac{p(x+d)\left(x+\frac{x^{2}}{d}\right)+x(4x-p)\left(x+\frac{x^{2}}{d}\right)+x(x+d)(4x-p)}{px(x+d)\left(x+\frac{x^{2}}{d}\right)} |  |

 |  | = 2 ​ p ​ x 2 + p ​ x 3 d + d ​ p ​ x + 4 ​ x 3 + 4 ​ x 4 d − p ​ x 2 − p ​ x 3 d + 4 ​ x 3 + 4 ​ d ​ x 2 − p ​ x 2 − d ​ p ​ x p ⁡ ( 2 ​ x 3 + x 4 d + d ​ x 2) \displaystyle=\frac{2px^{2}+\frac{px^{3}}{d}+dpx+4x^{3}+\frac{4x^{4}}{d}-px^{2}-\frac{px^{3}}{d}+4x^{3}+4dx^{2}-px^{2}-dpx}{p\left(2x^{3}+\frac{x^{4}}{d}+dx^{2}\right)} |  |

 |  | = 4 ​ ( 2 ​ x 3 + x 4 d + d ​ x 2) p ⁡ ( 2 ​ x 3 + x 4 d + d ​ x 2) \displaystyle=\frac{4\left(2x^{3}+\frac{x^{4}}{d}+dx^{2}\right)}{p\left(2x^{3}+\frac{x^{4}}{d}+dx^{2}\right)} |  |

 |  | = 4 p \displaystyle=\frac{4}{p} |  |

∎

###### Proof.

Proposition 3

Let p p be prime and let x ≤ y ≤ z x\leq y\leq z be positive integers that satisfy ( 1) with p ∤ y p\nmid y.

First, it was shown in [3] that a necessary condition for type I solutions is that ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil.

Next, slightly changing the notation in [3], we let m = gcd ⁡ ( x, y, z), a = gcd ⁡ ( x, y) / m, b = gcd ⁡ ( x, z) / m m=\gcd(x,y,z),a=\gcd(x,y)/m,b=\gcd(x,z)/m and c = gcd ⁡ ( y, z) / m c=\gcd(y,z)/m. Using this new notation, it was shown in [3] that x = a ​ b ​ m x=abm, y = a ​ c ​ m y=acm and z = b ​ c ​ m z=bcm.

For this type I solution, let d = ( 4 ​ x − p) ​ y − p ​ x d=(4x-p)y-px. We need to show that d | x 2 d|x^{2}.

In [3] it was shown for type I solutions that

 | p = 4 ​ a ​ b ​ c ​ m − a b + c. p=\frac{4abcm-a}{b+c}. |  |

This makes

 | d \displaystyle d | = ( 4 ​ x − p) ​ y − p ​ x \displaystyle=(4x-p)y-px |  |

 |  | = 4 ​ x ​ y − ( x + y) ​ p \displaystyle=4xy-(x+y)p |  |

 |  | = 4 ​ a 2 ​ b ​ c ​ m 2 − ( a ​ b ​ m + a ​ c ​ m) ​ ( 4 ​ a ​ b ​ c ​ m − a b + c) \displaystyle=4a^{2}bcm^{2}-(abm+acm)\left(\frac{4abcm-a}{b+c}\right) |  |

 |  | = 4 ​ a 2 ​ b ​ c ​ m 2 − 4 ​ a 2 ​ b ​ c ​ m 2 + a 2 ​ m \displaystyle=4a^{2}bcm^{2}-4a^{2}bcm^{2}+a^{2}m |  |

 |  | = a 2 ​ m. \displaystyle=a^{2}m. |  |

Because a 2 ​ m | a 2 ​ b 2 ​ m 2 a^{2}m|a^{2}b^{2}m^{2}, we see that d | x 2 d|x^{2}.

From the definition of d = ( 4 ​ x − p) ​ y − p ​ x d=(4x-p)y-px, it should be clear that d mod ( 4 ​ x − p) ≡ − p ​ x d\bmod(4x-p)\equiv-px.

We see that

 | p ​ x + d 4 ​ x − p \displaystyle\frac{px+d}{4x-p} | = p ​ x + ( 4 ​ x − p) ​ y − p ​ x 4 ​ x − p \displaystyle=\frac{px+(4x-p)y-px}{4x-p} |  |

 |  | = ( 4 ​ x − p) ​ y 4 ​ x − p \displaystyle=\frac{(4x-p)y}{4x-p} |  |

 |  | = y. \displaystyle=y. |  |

We also see that

 | p ⁡ ( x + p ⁡ ( x 2 d)) 4 ​ x − p \displaystyle\frac{p\left(x+p\left(\frac{x^{2}}{d}\right)\right)}{4x-p} | = p ​ x + p 2 ​ x 2 ( 4 ​ x − p) ​ y − p ​ x 4 ​ x − p \displaystyle=\frac{px+\frac{p^{2}x^{2}}{(4x-p)y-px}}{4x-p} |  |

 |  | = ( 4 ​ x − p) ​ x ​ y ​ p − p 2 ​ x 2 + p 2 ​ x 2 ( 4 ​ x − p) ​ ( 4 ​ x ​ y − ( x + y) ​ p) \displaystyle=\frac{(4x-p)xyp-p^{2}x^{2}+p^{2}x^{2}}{(4x-p)(4xy-(x+y)p)} |  |

 |  | = ( 4 ​ x − p) ​ x ​ y ​ p ( 4 ​ x − p) ​ ( 4 ​ x ​ y − ( x + y) ​ p) \displaystyle=\frac{(4x-p)xyp}{(4x-p)(4xy-(x+y)p)} |  |

 |  | = x ​ y ​ p 4 ​ x ​ y − ( x + y) ​ p \displaystyle=\frac{xyp}{4xy-(x+y)p} |  |

 |  | = 1 4 p − 1 x − 1 y \displaystyle=\frac{1}{\frac{4}{p}-\frac{1}{x}-\frac{1}{y}} |  |

 |  | = z. \displaystyle=z. |  |

∎

###### Proof.

Proposition 4

Let p p be prime and let x ≤ y ≤ z x\leq y\leq z be positive integers that satisfy ( 1) with p | y p|y.

It was shown in [3] that a necessary condition for type II solutions is that ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \left\lceil\frac{p}{4}\right\rceil\leq x\leq\left\lceil\frac{p}{2}\right\rceil.

For this type II solution, let d = ( 4 ​ x − p) ​ ( y / p) − x d=(4x-p)(y/\penalty p)-x. We need to show that d | x 2 d|x^{2}.

Recall, using the slightly different notation, that p | y p|y and p | z p|z, so p | c p|c. In [3] it was shown for type II solutions that if c = c ∗ ​ p c=c^{*}p, then

 | p = 4 ​ a ​ b ​ m − a + b c ∗. p=4abm-\frac{a+b}{c^{*}}. |  |

This makes

 | d \displaystyle d | = ( 4 ​ x − p) ​ ( y / p) − x \displaystyle=(4x-p)(y/\penalty p)-x |  |

 |  | = 4 ​ x ​ ( y / p) − ( x + y) \displaystyle=4x(y/\penalty p)-(x+y) |  |

 |  | = 4 ​ a 2 ​ b ​ c ∗ ​ m 2 − a ​ b ​ m − a ​ c ∗ ​ m ​ ( 4 ​ a ​ b ​ m − a + b c ∗) \displaystyle=4a^{2}bc^{*}m^{2}-abm-ac^{*}m\left(4abm-\frac{a+b}{c^{*}}\right) |  |

 |  | = 4 ​ a 2 ​ b ​ c ∗ ​ m 2 − a ​ b ​ m − 4 ​ a 2 ​ b ​ c ∗ ​ m 2 + a 2 ​ m + a ​ b ​ m \displaystyle=4a^{2}bc^{*}m^{2}-abm-4a^{2}bc^{*}m^{2}+a^{2}m+abm |  |

 |  | = a 2 ​ m. \displaystyle=a^{2}m. |  |

Because a 2 ​ m | a 2 ​ b 2 ​ m 2 a^{2}m|a^{2}b^{2}m^{2}, we see that d | x 2 d|x^{2}.

We have that y ≤ z y\leq z implies that a ​ c ​ m ≤ b ​ c ​ m acm\leq bcm or a ≤ b a\leq b. This implies that a 2 ​ m ≤ a ​ b ​ m a^{2}m\leq abm, so d ≤ x d\leq x.

From the definition of d = ( 4 ​ x − p) ​ ( y / p) − x d=(4x-p)(y/\penalty p)-x, it should be clear that d mod ( 4 ​ x − p) ≡ − x d\bmod(4x-p)\equiv-x.

We see that

 | p ⁡ ( x + d) 4 ​ x − p \displaystyle\frac{p(x+d)}{4x-p} | = p ⁡ ( x + ( 4 ​ x − p) ​ ( y / p) − x) 4 ​ x − p \displaystyle=\frac{p(x+(4x-p)(y/\penalty p)-x)}{4x-p} |  |

 |  | = ( 4 ​ x − p) ​ y 4 ​ x − p \displaystyle=\frac{(4x-p)y}{4x-p} |  |

 |  | = y. \displaystyle=y. |  |

We also see that

 | p ⁡ ( x + x 2 d) 4 ​ x − p \displaystyle\frac{p\left(x+\frac{x^{2}}{d}\right)}{4x-p} | = p ⁡ ( x + x 2 ( 4 ​ x − p) ​ ( y / p) − x) 4 ​ x − p \displaystyle=\frac{p\left(x+\frac{x^{2}}{(4x-p)(y/\penalty p)-x}\right)}{4x-p} |  |

 |  | = ( 4 ​ x − p) ​ x ​ y − p ​ x 2 + p ​ x 2 ( 4 ​ x − p) ​ ( 4 ​ x ​ ( y / p) − ( x + y)) \displaystyle=\frac{(4x-p)xy-px^{2}+px^{2}}{(4x-p)(4x(y/\penalty p)-(x+y))} |  |

 |  | = ( 4 ​ x − p) ​ x ​ y ( 4 ​ x − p) ​ ( 4 ​ x ​ ( y / p) − ( x + y)) \displaystyle=\frac{(4x-p)xy}{(4x-p)(4x(y/\penalty p)-(x+y))} |  |

 |  | = x ​ y 4 ​ x ​ ( y / p) − ( x + y) \displaystyle=\frac{xy}{4x(y/\penalty p)-(x+y)} |  |

 |  | = 1 4 p − 1 x − 1 y \displaystyle=\frac{1}{\frac{4}{p}-\frac{1}{x}-\frac{1}{y}} |  |

 |  | = z. \displaystyle=z. |  |

∎

## References

- [1] Abdulrahman A. Abdulaziz, On the Egyptian method of decomposing 2 n \frac{2}{n} into unit fractions, Historia Math. 35 (2008), 1-18.
- [2] M. Bello-Hernández, M. Benito and E. Fernández, On Egyptian fractions, arXiv: 1010.2035v2, (2012) .
- [3] K. Bradford, A Note On The Erdős-Straus Conjecture, Integers, 21 (2021), A24.
- [4] K. Bradford and E. Ionascu, A geometric reduction of the Erdős-Straus conjecture, Adv. Mod. and Optim. 1 (2015), vol. 17, 41-54.
- [5] E. S. Croot III, Egyptian Fractions, Ph. D. Thesis, (1994).
- [6] C. Elsholtz and T. Tao, Counting the number of solutions to the Erdős-Straus equation on unit fractions, J. Aust. Math. Soc. 94 (2013), vol. 1, 50-105.
- [7] P. Erdős, Az 1 / x 1 + ⋯ + 1 / x n = a / b 1/\penalty x_{1}+\cdots+1/\penalty x_{n}=a/\penalty b egyenlet egész számú megoldásairól, Mat. Lapok 1 (1950).
- [8] R. Guy, Unsolved Problems in Number Theory, Springer, New York, 2004.
- [9] E. J. Ionascu and A. Wilson, On the Erdős-Straus conjecture, Rev. Roumaine Math. Pures Appl., 56 (1) (2011), 21-30.
- [10] D. Li On the equation 4 /n = 1 /x + 1 /y + 1 /z, J. Number Theory, 13 (1981), 485-494.
- [11] G. G. Martin, The distribution of prime primitive roots and dense egyptian fractions, Ph. D. Thesis, (1997).
- [12] L. G. Mordell, Diophantine equations, Academic Press, London, (1969).
- [13] M.R. Obláth, Sur l’ équation diophantienne 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 4/\penalty n=1/\penalty x_{1}+1/\penalty x_{2}+1/\penalty x_{3}, Mathesis 59 (1950), 308-316.
- [14] Y. Rav, On the representation of rational numbers as a sum of a fixed number of unit fractions, J. Reine Angew. Math. 222 (1966), 207-213.
- [15] L. A. Rosati, Sull’equazione diofantea 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 4/n=1/x_{1}+1/x_{2}+1/x_{3}, Boll. Unione Mat. Ital., serie III, Anno IX, (1954), No. 1.
- [16] J.W. Sander, On 4 / n = 1 / x + 1 / y + 1 / z 4/\penalty n=1/\penalty x+1/\penalty y+1/\penalty z and Rosser’s sieve, Acta Arith. 49 (1988), 281-289.
- [17] J.W. Sander, On 4 / n = 1 / x + 1 / y + 1 / z 4/\penalty n=1/\penalty x+1/\penalty y+1/\penalty z and Iwaniec’ Half Dimensional Sieve, Acta Arith. 59 (1991), 183-204.
- [18] J.W. Sander, Egyptian fractions and the Erdős-Straus Conjecture, Nieuw Arch. Wiskd. (4) 15 (1997), 43-50.
- [19] A. Schinzel, On sums of three unit fractions with polynomial denominators, Funct. Approx. Comment. Math. 28 (2000), 187-194.
- [20] A. Swett, The Erdős Straus conjecture, Current Research on ESC, rev.10/28/99. http://math.uindy.edu/swett.esc.htm (1999).
- [21] D. G. Terzi, On a conjecture by Erdős-Straus, Nordisk Tidskr. Info. (BIT) 11 (1971), 212-216.
- [22] R.C. Vaughan, On a problem of Erdos, Straus and Schinzel, Mathematika, 17 (1970), 193-198.
- [23] W. Webb, On 4 / n = 1 / x + 1 / y + 1 / z 4/\penalty n=1/\penalty x+1/\penalty y+1/\penalty z, Proc. Amer. Math. Soc. 25 (1970), 578-584.
- [24] W. Webb, On a theorem of Rav concerning Egyptian fractions, Canad. Math. Bull. 18 (1975), no. 1, 155-156.
- [25] W. Webb, On the diophantine equation k / n = a 1 / x 1 + a 2 / x 2 + a 3 / x 3 k/\penalty n=a_{1}/\penalty x_{1}+a_{2}/\penalty x_{2}+a_{3}/\penalty x_{3}, C ˘ \breve{C} asopis pro p e ˘ \breve{e} stováni matematiy, ro c ˘ \breve{c} 10 (1976), 360-365.
- [26] K. Yamamoto, On the diophantine equation 4 / n = 1 / x + 1 / y + 1 / z 4/\penalty n=1/\penalty x+1/\penalty y+1/\penalty z, Memoirs of the Faculty of Science, Kyushu University, Ser. A, Vol. 19 (1965), No. 1, 37-47.
- [27] X.Q. Yang, A note on 4 / n = 1 / x + 1 / y + 1 / z 4/\penalty n=1/\penalty x+1/\penalty y+1/\penalty z, Proc. Amer. Math. Soc., 85 (1982), 496-498.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
