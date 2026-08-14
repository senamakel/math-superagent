<!-- source: https://arxiv.org/html/2506.07386v1 | converted from HTML -->

Computation of the Totient Summatory Function

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2506.07386v1 [math.NT] 09 Jun 2025

# Computation of the Totient Summatory Function

Lucas Augustus Brown [3]

2026– \twodigit 8– \twodigit 11

###### Abstract

An algorithm is devised for computing Φ ⁡ ( n) = ϕ ⁡ ( 1) + ϕ ⁡ ( 2) + ⋯ + ϕ ⁡ ( n) \Phi(n)=\phi(1)+\phi(2)+\cdots+\phi(n) in time Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) and space Θ ~ ​ ( n 1 / 3) \widetilde{\Theta}(n^{1/3}). The starting point is an existing algorithm based on the Dirichlet hyperbola method and the Mertens function. The algorithm is then used to compute Φ ⁡ ( 10 19) = 30396355092701331435065976498046398788 \Phi(10^{19})=30396355092701331435065976498046398788.

## 1 Introduction

The totient-summatory function,

 | Φ ⁡ ( n) = ∑ k = 1 n ϕ ⁡ ( n), \Phi(n)=\sum_{k=1}^{n}\phi(n), |  |

has been computed out to Φ ⁡ ( 10 18) = 303963550927013314319686824781290348 \Phi(10^{18})=303963550927013314319686824781290348 ( [A064018][4]) with the aid of algorithms that take Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time [6, 5]; the implied constants and logarithmic factors are small enough that replicating this computation takes less than a day on a recent computer running a single-threaded program. Unfortunately, these algorithms all require the simultaneous storage of at least Θ ⁡ ( n 1 / 2) \Theta(n^{1/2}) integers, which is pushing the limits of what the typical desktop computer can handle.

The contribution of this paper is to modify one such algorithm [6, totientSummatoryFast1] to use Θ ~ ​ ( n 1 / 3) \widetilde{\Theta}(n^{1/3}) space, enabling the computation of

 | Φ ⁡ ( 10 19) = 30396355092701331435065976498046398788 \Phi(10^{19})=30396355092701331435065976498046398788 |  |

in less than 9 days and 7 gigabytes.

### 1.1 Conventions

The Dirichlet convolution of f f and g g is denoted by f ∗ g f*g.

The letter μ \mu is used for both the Möbius function and an array such that μ k = μ ⁡ ( k) \mu_{k}=\mu(k).

The letter M M is used for both the Mertens function and an array such that M k = M ⁡ ( k) M_{k}=M(k).

The letter δ \delta denotes the identity function for Dirichlet convolution: δ ⁡ ( 1) = 1 \delta(1)=1, and δ ⁡ ( x) = 0 \delta(x)=0 for all other x x.

The reported time and space complexities count the arithmetic operations used and the integers stored, not bit operations and bits stored.

### 1.2 Overview of the paper

- •

In Section 2, we review some existing algorithms.

- •

In Section 3, we modify one such algorithm to reduce its space complexity from Θ ⁡ ( n 1 / 2) \Theta(n^{1/2}) to Θ ~ ​ ( n 1 / 3) \widetilde{\Theta}(n^{1/3}), culminating in Algorithm 13.

- •

In Section 4, we analyze Algorithm 13, concluding in Theorem 7 that, with its optimal parameter selection, it takes Θ ⁡ ( n 2 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 1 / 3) \Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}\right) time and Θ ⁡ ( n 1 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 2 / 3) \Theta\left(n^{1/3}\cdot(\ln(\ln(n)))^{2/3}\right) space.

- •

In Section 5, we present the results of running Algorithm 13 on various inputs.

- •

Finally, Section 6 contains some supporting lemmas.

## 2 Existing algorithms

A recent paper by Hirsch, Kessler, and Mendlovic [4, §5.6] outlines an algorithm for computing Φ ⁡ ( n) \Phi(n) in O ~ ​ ( n 1 / 2) \widetilde{O}(n^{1/2}) time and space; furthermore, this algorithm has the same space-time tradeoffs as that paper’s prime-counting algorithm [3], which means that it has a variant that achieves O ⁡ ( n 5 / 9 + ε) O(n^{5/9+\varepsilon}) time and O ⁡ ( n 2 / 9 + ε) O(n^{2/9+\varepsilon}) space for any ε > 0 \varepsilon>0. However, this algorithm and its variants have never been implemented, and the hidden factors are expected to be large enough to make using it noncompetitive for practical n n.

### 2.1 The Mertens-first algorithm

By applying the Dirichlet hyperbola method to the convolution ϕ = μ ∗ I \phi=\mu*I, where I ⁡ ( x) = x I(x)=x, and letting a ​ b = n ab=n, we obtain the formula

 | Φ ⁡ ( n) = ∑ x = 1 a ∑ y = 1 n / x μ ⁡ ( x) ​ I ​ ( y) + ∑ y = 1 b ∑ x = 1 n / y μ ⁡ ( x) ​ I ​ ( y) − ∑ x = 1 a ∑ y = 1 b μ ⁡ ( x) ​ I ​ ( y) \Phi(n)=\sum_{x=1}^{a}\sum_{y=1}^{n/x}\mu(x)\,I(y)+\sum_{y=1}^{b}\sum_{x=1}^{n/y}\mu(x)\,I(y)-\sum_{x=1}^{a}\sum_{y=1}^{b}\mu(x)\,I(y) |  |

 | = ∑ x = 1 a ∑ y = 1 n / x y ⋅ μ ⁡ ( x) + ∑ y = 1 b ∑ x = 1 n / y y ⋅ μ ⁡ ( x) − ∑ x = 1 a ∑ y = 1 b y ⋅ μ ⁡ ( x) =\sum_{x=1}^{a}\sum_{y=1}^{n/x}y\cdot\mu(x)+\sum_{y=1}^{b}\sum_{x=1}^{n/y}y\cdot\mu(x)-\sum_{x=1}^{a}\sum_{y=1}^{b}y\cdot\mu(x) |  |

 | Φ ⁡ ( n) = ∑ x = 1 a μ ⁡ ( x) ⋅ ⌊ n x ⌋ ⋅ ( ⌊ n x ⌋ + 1) 2 ⏟ X + ∑ y = 1 b y ⋅ M ⁡ ( n / y) ⏟ Y − b ⋅ ( b + 1) 2 ⋅ M ⁡ ( a) ⏟ Z. \Phi(n)=\underbrace{\sum_{x=1}^{a}\mu(x)\cdot\frac{{\left\lfloor\frac{n}{x}\right\rfloor}\cdot\left({\left\lfloor\frac{n}{x}\right\rfloor}+1\right)}{2}}_{X}+\underbrace{\sum_{y=1}^{b}y\cdot M(n/y)}_{Y}-\underbrace{\frac{b\cdot(b+1)}{2}\cdot M(a)}_{Z}. |  | (1) |

The labels X X, Y Y, and Z Z will be used later.

Suppose that we have an algorithm that can compute an individual value of M ⁡ ( x) M(x) in time O ~ ​ ( x c) \widetilde{O}(x^{c}), and note that c < 1 c<1 is available [1]. Using a sieve to compute the necessary Möbius values, but otherwise evaluating this formula naïvely, takes time

 | O ~ ​ ( a + ∑ x = 1 b ( n x) c + a c) \widetilde{O}\left(a+\sum_{x=1}^{b}\left(\frac{n}{x}\right)^{c}+a^{c}\right) |  |

 | = O ~ ​ ( a + n c ​ ∫ 1 b x − c ​ 𝑑 x + a c) =\widetilde{O}\left(a+n^{c}\displaystyle\int_{1}^{b}\!x^{-c}\,dx+a^{c}\right) |  |

 | = O ~ ​ ( a + n c ​ b 1 − c 1 − c − n c ​ 1 1 − c 1 − c + a c) =\widetilde{O}\left(a+n^{c}\frac{b^{1-c}}{1-c}-n^{c}\frac{1^{1-c}}{1-c}+a^{c}\right) |  |

 | = O ~ ​ ( a + n c ​ b 1 − c − n c + a c) =\widetilde{O}\left(a+n^{c}b^{1-c}-n^{c}+a^{c}\right) |  |

 | = O ~ ​ ( a + n ​ a c − 1 − n c + a c). =\widetilde{O}\left(a+na^{c-1}-n^{c}+a^{c}\right). |  |

The third term is always dominated by the second, and the fourth is always dominated by the first.

 | = O ~ ​ ( a + n ​ a c − 1) =\widetilde{O}\left(a+na^{c-1}\right) |  |

To balance the contributions of the two terms, we take a = O ~ ​ ( n 1 / ( 2 − c)) a=\widetilde{O}(n^{1/(2-c)}).

The Deléglise-Rivat algorithm [1] allows c = 2 / 3 c=2/3, and so using it in this algorithm results in a time complexity of O ~ ​ ( n 3 / 4) \widetilde{O}(n^{3/4}). The Mertens function can also be computed with the Helfgott-Thompson algorithm [2], which takes O ~ ​ ( n 3 / 5) \widetilde{O}(n^{3/5}) time. Evaluating ( 1) as described then takes O ~ ​ ( n 5 / 7) \widetilde{O}(n^{5/7}) time.

This algorithm suffers from the fact that all those Mertens values are computed one-at-a-time and are not given a chance to contribute to each other. This can be ameliorated by another application of the Dirichlet hyperbola method. This time, we use δ = μ ∗ 1 \delta=\mu*1 and set α ​ β = n \alpha\beta=n to obtain

 | ∑ k = 1 n δ ⁡ ( k) = ∑ x = 1 α ∑ y = 1 n / x μ ⁡ ( x) ⋅ 1 + ∑ y = 1 β ∑ x = 1 n / y μ ⁡ ( x) ⋅ 1 − ∑ x = 1 α ∑ y = 1 β μ ⁡ ( x) ⋅ 1 \sum_{k=1}^{n}\delta(k)=\sum_{x=1}^{\alpha}\sum_{y=1}^{n/x}\mu(x)\cdot 1+\sum_{y=1}^{\beta}\sum_{x=1}^{n/y}\mu(x)\cdot 1-\sum_{x=1}^{\alpha}\sum_{y=1}^{\beta}\mu(x)\cdot 1 |  |

 | 1 = ∑ x = 1 α μ ⁡ ( x) ​ ⌊ n x ⌋ + ∑ y = 1 β M ⁡ ( n / y) − M ⁡ ( α) ​ ⌊ β ⌋ 1=\sum_{x=1}^{\alpha}\mu(x){\left\lfloor\frac{n}{x}\right\rfloor}+\sum_{y=1}^{\beta}M(n/y)-M(\alpha){\left\lfloor\beta\right\rfloor} |  |

 | M ⁡ ( n) = 1 + ⌊ β ⌋ ​ M ​ ( α) − ∑ x = 1 α μ ⁡ ( x) ​ ⌊ n x ⌋ − ∑ y = 2 β M ⁡ ( n / y). M(n)=1+{\left\lfloor\beta\right\rfloor}M(\alpha)-\sum_{x=1}^{\alpha}\mu(x){\left\lfloor\frac{n}{x}\right\rfloor}-\sum_{y=2}^{\beta}M(n/y). |  | (2) |

When evaluating ( 1), we need to find μ ⁡ ( k) \mu(k) for 1 ≤ k ≤ a 1\leq k\leq a, M ⁡ ( n / k) M(n/k) for 1 ≤ k ≤ b 1\leq k\leq b, and M ⁡ ( a) M(a).

When evaluating ( 2), we need to find μ ⁡ ( k) \mu(k) for 1 ≤ k ≤ α 1\leq k\leq\alpha, M ⁡ ( n / k) M(n/k) for 2 ≤ k ≤ β 2\leq k\leq\beta, and M ⁡ ( α) M(\alpha).

Clearly, these work well together: we can sieve μ \mu up to a a, accumulate the values along the way to compute M M up to a a, use ( 2) to compute the remaining Mertens values, and then feed all that data into ( 1) to compute Φ ⁡ ( n) \Phi(n). This results in Algorithm 1, which I call the *Mertens-first algorithm*. Note that we do *not*take α = a \alpha=a: instead, we use a = Θ ~ ​ ( n 2 / 3) a=\widetilde{\Theta}(n^{2/3}) and α = n \alpha=\sqrt{n}.

Data: n ≥ 1 n\geq 1

Result: Φ ⁡ ( n) \Phi(n)

a ← ⌊ Θ ~ ​ ( n 2 / 3) ⌋ a\leftarrow{\left\lfloor\widetilde{\Theta}(n^{2/3})\right\rfloor}; b ← ⌊ n / a ⌋ b\leftarrow{\left\lfloor n/a\right\rfloor}; X ← 0 X\leftarrow 0; Y ← 0 Y\leftarrow 0; Z ← 0 Z\leftarrow 0; m ← 0 m\leftarrow 0; s ← ⌊ n ⌋ s\leftarrow{\left\lfloor\sqrt{n}\right\rfloor} 0.1

if*⌊ n ⌋ = ⌊ n / ⌊ n ⌋ ⌋ {\left\lfloor\sqrt{n}\right\rfloor}={\left\lfloor n/{\left\lfloor\sqrt{n}\right\rfloor}\right\rfloor}*then s ← s − 1 s\leftarrow s-1 0.2

0.3

χ ← ⌊ n / s ⌋ \chi\leftarrow{\left\lfloor n/s\right\rfloor} 0.4

Prepare a segmented sieve to compute μ ⁡ ( k) \mu(k) for 1 ≤ k ≤ a 1\leq k\leq a. 0.5

Let μ \mu and M M be arrays indexed from 1 1 through ⌊ n ⌋ {\left\lfloor\sqrt{n}\right\rfloor}, inclusive. 0.6

Let M ′ M^{\prime} be an array indexed from 1 1 to ⌊ n / ⌊ n ⌋ ⌋ {\left\lfloor n/{\left\lfloor\sqrt{n}\right\rfloor}\right\rfloor}, inclusive, initialized to all zeros.

0.7

2 for*x = 1 x=1 to a a*do 0.8

v ← ⌊ n / x ⌋ v\leftarrow{\left\lfloor n/x\right\rfloor} 0.9

m ← m + μ ⁡ ( x) m\leftarrow m+\mu(x) 0.10

X ← X + μ ⁡ ( x) ⋅ v ⋅ ( v + 1) 2 X\leftarrow X+\mu(x)\cdot\dfrac{v\cdot(v+1)}{2} 0.11

if*x ≤ ⌊ n ⌋ x\leq{\left\lfloor\sqrt{n}\right\rfloor}*then 0.12

M x ← m M_{x}\leftarrow m 0.13

μ x ← μ ⁡ ( x) \mu_{x}\leftarrow\mu(x) 0.14

0.30

else if*x = χ x=\chi*then 0.31

0.32

if*v ≠ b v\neq b*then M v ′ ← m M^{\prime}_{v}\leftarrow m 0.33

0.34

0.37

s ← s − 1 s\leftarrow s-1 0.38

χ ← ⌊ n / s ⌋ \chi\leftarrow{\left\lfloor n/s\right\rfloor} 0.39

0.45

if*x = a x=a*then Z ← m ⋅ b ⋅ ( b + 1) 2 Z\leftarrow m\cdot\dfrac{b\cdot(b+1)}{2} 0.46

0.47

0.48

*lines 1 – 1 here*0.49

0.50

0.51

for*y = b y=b to 1 1*do 0.52

v ← ⌊ n / y ⌋ v\leftarrow{\left\lfloor n/y\right\rfloor} 0.53

m ← 1 − v + ⌊ v ⌋ ⋅ M ⌊ v ⌋ m\leftarrow 1-v+{\left\lfloor\sqrt{v}\right\rfloor}\cdot M_{{\left\lfloor\sqrt{v}\right\rfloor}} 0.54

for*x = 2 x=2 to ⌊ v ⌋ {\left\lfloor\sqrt{v}\right\rfloor}*do 0.55

m ← m − μ x ⋅ ⌊ v / x ⌋ m\leftarrow m-\mu_{x}\cdot{\left\lfloor v/x\right\rfloor} 0.56

if*⌊ v / x ⌋ ≤ ⌊ n ⌋ {\left\lfloor v/x\right\rfloor}\leq{\left\lfloor\sqrt{n}\right\rfloor}*then 0.57

m ← m − M ⌊ v / x ⌋ m\leftarrow m-M_{{\left\lfloor v/x\right\rfloor}} else 0.58

m ← m − M ⌊ n / ⌊ v / x ⌋ ⌋ ′ m\leftarrow m-M^{\prime}_{{\left\lfloor n/{\left\lfloor v/x\right\rfloor}\right\rfloor}} M y ′ ← M y ′ + m M^{\prime}_{y}\leftarrow M^{\prime}_{y}+m 0.59

Y ← Y + y ⋅ M y ′ Y\leftarrow Y+y\cdot M^{\prime}_{y}

0.60

return X + Y − Z X+Y-Z

Algorithm 1 Compute Φ ⁡ ( n) \Phi(n) in Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time and Θ ~ ​ ( n 1 / 2) \widetilde{\Theta}(n^{1/2}) space [6].

The purpose of the non-consecutivity of the line numbering is to coordinate line numbers between Algorithms 1, 7, 10, 12, and 13. The variables X X, Y Y, and Z Z correspond to the labels X X, Y Y, and Z Z in ( 1).

Algorithm 1 has four phases:

1. 0.

In the zeroth phase, lines 1 – 1 initialize the computation.

2. 1.

In the first phase, covered in lines 1 – 1, we sieve the Möbius function up to ⌊ n ⌋ {\left\lfloor\sqrt{n}\right\rfloor}, accumulate its values to compute the Mertens function, save both μ \mu and M M, and accumulate terms into X X.

3. 2.

In the second phase, covered in lines 1 – 1 and 1 – 1, we continue the sieve up to a a. We continue to accumulate Möbius values to compute Mertens values, and we continue to accumulate terms into X X, but we do not save any μ \mu, and only some Mertens values are saved. As the final act of phase 2, we compute Z Z. At this point, X X and Z Z are fully evaluated, and nothing has been done about Y Y.

4. 3.

In the third phase, lines 1 – 1 feed the stored Möbius and Mertens values into ( 2) to compute the remaining Mertens values in order of increasing argument—that is, we first compute M ⁡ ( n / b) M(n/b), then M ⁡ ( n / ( b − 1)) M(n/(b-1)), then …, and finally M ⁡ ( n) M(n). As each Mertens value is computed, a term from Y Y becomes available, and we evaluate it accordingly.

Once the third phase is done, Φ ⁡ ( n) \Phi(n) is computed as X + Y − Z X+Y-Z.

Line 1 is gatekept by the condition v ≠ b v\neq b. This is needed to mitigate an overlap in the phases that occurs for some ( a, n) (a,n) pairs. In such cases, without the gatekeeping, line 1 would set M b ′ M^{\prime}_{b} to M ⁡ ( a) M(a), which should be its final value, but it then gets modifed in the first iteration through phase 3, which throws things off. With the condition v ≠ b v\neq b in place, M b ′ M^{\prime}_{b} is not touched until phase 3.

Algorithm 1 takes Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time: phases 0–2 combined clearly take Θ ~ ​ ( a) \widetilde{\Theta}(a) time, and phase 3 takes time

 | Θ ~ ​ ( ∑ y = 1 b ( ⌊ n y ⌋ − 1)) \widetilde{\Theta}\left(\sum_{y=1}^{b}\left({\left\lfloor\sqrt{\frac{n}{y}}\right\rfloor}-1\right)\right) |  |

 | = Θ ~ ​ ( ∫ 1 b n y ​ 𝑑 y − b) =\widetilde{\Theta}\left(\displaystyle\int_{1}^{b}\!\sqrt{\frac{n}{y}}\,dy-b\right) |  |

 | = Θ ~ ​ ( 2 ​ n ​ ( b − 1) − b) =\widetilde{\Theta}\left(2\sqrt{n}\left(\sqrt{b}-1\right)-b\right) |  |

 | = Θ ~ ​ ( n a). =\widetilde{\Theta}\left(\frac{n}{\sqrt{a}}\right). |  |

Algorithm 1 takes Θ ~ ​ ( n) \widetilde{\Theta}(\sqrt{n}) space: we use three arrays of Θ ⁡ ( n) \Theta(\sqrt{n}) elements each to store the Möbius and Mertens values, the Möbius sieving consumes O ~ ​ ( a) \widetilde{O}(\sqrt{a}) space, and everything else fits in O ⁡ ( 1) O(1) space.

## 3 The Mertens-first algorithm in less space

We now reduce Algorithm 1 ’s memory usage from Θ ~ ​ ( n) \widetilde{\Theta}(\sqrt{n}) to Θ ~ ​ ( n 3) \widetilde{\Theta}(\sqrt[3]{n}). The first step is to observe that we can move line 1 into phase 1. The work done in that line is essentially as follows:

for*y = b y=b to 1 1*do 0.1

for*x = 2 x=2 to ⌊ n / y ⌋ {\left\lfloor\sqrt{n/y}\right\rfloor}*do 0.2

M y ′ ← M y ′ − μ x ⋅ ⌊ n y ​ x ⌋ M^{\prime}_{y}\leftarrow M^{\prime}_{y}-\mu_{x}\cdot{\left\lfloor\dfrac{n}{yx}\right\rfloor}

Algorithm 2 An extract from Algorithm 1

If we can swap the order of the loops, then we will be able to integrate this line into phase 1 and not have to store the Möbius array.

This extract iterates over all pairs ( y, x) (y,x) such that 1 ≤ y ≤ b 1\leq y\leq b and 2 ≤ x ≤ n / y 2\leq x\leq\sqrt{n/y}. The range accessed by x x is therefore 2 ≤ x ≤ n 2\leq x\leq\sqrt{n}, and for each x x, y y ranges over 1 ≤ y ≤ min ⁡ ( b, n / x 2) 1\leq y\leq\min(b,n/x^{2}). This extract is therefore essentially equivalent to

for*x = 2 x=2 to ⌊ n ⌋ {\left\lfloor\sqrt{n}\right\rfloor}*do 0.1

for*y = 1 y=1 to min ⁡ ( b, ⌊ n / x 2 ⌋) \min(b,{\left\lfloor n/x^{2}\right\rfloor})*do 0.2

M y ′ ← M y ′ − μ ⁡ ( x) ⋅ ⌊ n y ​ x ⌋ M^{\prime}_{y}\leftarrow M^{\prime}_{y}-\mu(x)\cdot{\left\lfloor\dfrac{n}{yx}\right\rfloor}

Algorithm 3 Algorithm 2, reordered

It is also easy to move line 1 into phase 1. The work this line does is essentially

for*y = b y=b to 1 1*do 0.1

M y ′ ← M y ′ + 1 − ⌊ n / y ⌋ + ⌊ n / y ⌋ ⋅ M ⌊ n / y ⌋ M^{\prime}_{y}\leftarrow M^{\prime}_{y}+1-{\left\lfloor n/y\right\rfloor}+{\left\lfloor\sqrt{n/y}\right\rfloor}\cdot M_{{\left\lfloor\sqrt{n/y}\right\rfloor}}

Algorithm 4 An extract from Algorithm 1

This is essentially equivalent to

for*x = 1 x=1 to a a*do 0.1

if*∃ y ∋ 1 ≤ y ≤ b & x = ⌊ n / y ⌋ \exists y\;\ni\;1\leq y\leq b\;\;\&\;\;x={\left\lfloor\sqrt{n/y}\right\rfloor}*then 0.2

forall*such y y*do 0.3

M y ′ ← M y ′ + 1 − ⌊ n / y ⌋ + x ⋅ M x M^{\prime}_{y}\leftarrow M^{\prime}_{y}+1-{\left\lfloor n/y\right\rfloor}+x\cdot M_{x}

Algorithm 5 Algorithm 4, redone

which we make more precise as

d ← b d\leftarrow b 0.1

γ ← ⌊ n / d ⌋ \gamma\leftarrow{\left\lfloor\sqrt{n/d}\right\rfloor} 0.2

for*x = 1 x=1 to a a*do 0.3

0.4

while*x = γ x=\gamma*do 0.5

M d ′ ← M d ′ + 1 − ⌊ n / d ⌋ + x ⋅ M x M^{\prime}_{d}\leftarrow M^{\prime}_{d}+1-{\left\lfloor n/d\right\rfloor}+x\cdot M_{x} 0.6

d ← d − 1 d\leftarrow d-1 0.7

γ ← ⌊ n / d ⌋ \gamma\leftarrow{\left\lfloor\sqrt{n/d}\right\rfloor}

Algorithm 6 Algorithm 4, redone again

Applying these edits to Algorithm 1 yields Algorithm 7:

- •

Lines 1 and 1 have had actions added to them.

- •

Line 1 no longer calls for the existence of the array μ \mu.

- •

Line 1 has been deleted.

- •

Lines 7 – 7 have been inserted.

- •

Line 1 has been modified.

- •

Line 1 has been deleted.

Data: n ≥ 1 n\geq 1

Result: Φ ⁡ ( n) \Phi(n)

a ← ⌊ Θ ~ ​ ( n 2 / 3) ⌋ a\leftarrow{\left\lfloor\widetilde{\Theta}(n^{2/3})\right\rfloor}; b ← ⌊ n / a ⌋ b\leftarrow{\left\lfloor n/a\right\rfloor}; X ← 0 X\leftarrow 0; Y ← 0 Y\leftarrow 0; Z ← 0 Z\leftarrow 0; m ← 0 m\leftarrow 0; s ← ⌊ n ⌋ s\leftarrow{\left\lfloor\sqrt{n}\right\rfloor}; d ← b d\leftarrow b 0.1

if*⌊ n ⌋ = ⌊ n / ⌊ n ⌋ ⌋ {\left\lfloor\sqrt{n}\right\rfloor}={\left\lfloor n/{\left\lfloor\sqrt{n}\right\rfloor}\right\rfloor}*then s ← s − 1 s\leftarrow s-1 0.2

0.3

χ ← ⌊ n / s ⌋ \chi\leftarrow{\left\lfloor n/s\right\rfloor}; γ ← ⌊ n / d ⌋ \gamma\leftarrow{\left\lfloor\sqrt{n/d}\right\rfloor} 0.4

Prepare a segmented sieve to compute μ ⁡ ( x) \mu(x) for 1 ≤ x ≤ a 1\leq x\leq a. 0.5

Let M M be an array indexed from 1 1 through ⌊ n ⌋ {\left\lfloor\sqrt{n}\right\rfloor}, inclusive. 0.6

Let M ′ M^{\prime} be an array indexed from 1 1 to ⌊ n / ⌊ n ⌋ ⌋ {\left\lfloor n/{\left\lfloor\sqrt{n}\right\rfloor}\right\rfloor}, inclusive, initialized to all zeros.

0.7

2 for*x = 1 x=1 to a a*do 0.8

v ← ⌊ n / x ⌋ v\leftarrow{\left\lfloor n/x\right\rfloor} 0.9

m ← m + μ ⁡ ( x) m\leftarrow m+\mu(x) 0.10

X ← X + μ ⁡ ( x) ⋅ v ⋅ ( v + 1) 2 X\leftarrow X+\mu(x)\cdot\dfrac{v\cdot(v+1)}{2} 0.11

if*x ≤ ⌊ n ⌋ x\leq{\left\lfloor\sqrt{n}\right\rfloor}*then 0.12

M x ← m M_{x}\leftarrow m 0.13

0.15

if*x > 1 x>1*then 0.16

for*y = 1 y=1 to min ⁡ ( b, ⌊ v / x ⌋) \min(b,{\left\lfloor v/x\right\rfloor})*do 0.17

M y ′ ← M y ′ − μ ⁡ ( x) ⋅ ⌊ v y ⌋ M^{\prime}_{y}\leftarrow M^{\prime}_{y}-\mu(x)\cdot{\left\lfloor\dfrac{v}{y}\right\rfloor} while*x = γ x=\gamma*do 0.18

M d ′ ← M d ′ + 1 − ⌊ n / d ⌋ + m ​ x M^{\prime}_{d}\leftarrow M^{\prime}_{d}+1-{\left\lfloor n/d\right\rfloor}+mx 0.19

d ← d − 1 d\leftarrow d-1 0.20

γ ← ⌊ n / d ⌋ \gamma\leftarrow{\left\lfloor\sqrt{n/d}\right\rfloor} 0.21

0.30

else if*x = χ x=\chi*then 0.31

0.32

if*v ≠ b v\neq b*then M v ′ ← m M^{\prime}_{v}\leftarrow m 0.33

0.34

0.37

s ← s − 1 s\leftarrow s-1 0.38

χ ← ⌊ n / s ⌋ \chi\leftarrow{\left\lfloor n/s\right\rfloor} 0.39

0.45

if*x = a x=a*then Z ← m ⋅ b ⋅ ( b + 1) 2 Z\leftarrow m\cdot\dfrac{b\cdot(b+1)}{2} 0.46

0.47

*lines 7 – 7 here*0.48

0.49

0.50

for*y = b y=b to 1 1*do 0.51

v ← ⌊ n / y ⌋ v\leftarrow{\left\lfloor n/y\right\rfloor} 0.52

m ← 0 m\leftarrow 0 0.53

for*x = 2 x=2 to ⌊ v ⌋ {\left\lfloor\sqrt{v}\right\rfloor}*do 0.54

0.56

if*⌊ v / x ⌋ ≤ ⌊ n ⌋ {\left\lfloor v/x\right\rfloor}\leq{\left\lfloor\sqrt{n}\right\rfloor}*then 0.57

m ← m − M ⌊ v / x ⌋ m\leftarrow m-M_{{\left\lfloor v/x\right\rfloor}} else 0.58

m ← m − M ⌊ n / ⌊ v / x ⌋ ⌋ ′ m\leftarrow m-M^{\prime}_{{\left\lfloor n/{\left\lfloor v/x\right\rfloor}\right\rfloor}} M y ′ ← M y ′ + m M^{\prime}_{y}\leftarrow M^{\prime}_{y}+m 0.59

Y ← Y + y ⋅ M y ′ Y\leftarrow Y+y\cdot M^{\prime}_{y} 0.60

0.61

return X + Y − Z X+Y-Z

Algorithm 7 Compute Φ ⁡ ( n) \Phi(n) in Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time and Θ ~ ​ ( n 1 / 2) \widetilde{\Theta}(n^{1/2}) space.

The next step is to move line 7 into phase 1. The work this line does is essentially

for*y = b y=b to 1 1*do 0.1

v ← ⌊ n / y ⌋ v\leftarrow{\left\lfloor n/y\right\rfloor} 0.2

m ← 0 m\leftarrow 0 0.3

for*x = 2 x=2 to ⌊ v ⌋ {\left\lfloor\sqrt{v}\right\rfloor}*do 0.4

if*⌊ v / x ⌋ ≤ ⌊ n ⌋ {\left\lfloor v/x\right\rfloor}\leq{\left\lfloor\sqrt{n}\right\rfloor}*then 0.5

m ← m − M ⌊ v / x ⌋ m\leftarrow m-M_{{\left\lfloor v/x\right\rfloor}} M y ′ ← M y ′ + m M^{\prime}_{y}\leftarrow M^{\prime}_{y}+m

Algorithm 8 An extract from Algorithm 7

This extract iterates over all pairs ( x, y) (x,y) with

 | 1 ≤ y ≤ b and 2 ≤ x ≤ ⌊ n / y ⌋ and ⌊ n x ​ y ⌋ ≤ ⌊ n ⌋ 1\leq y\leq b\qquad\text{and}\qquad 2\leq x\leq{\left\lfloor\sqrt{n/y}\right\rfloor}\qquad\text{and}\qquad{\left\lfloor\frac{n}{xy}\right\rfloor}\leq{\left\lfloor\sqrt{n}\right\rfloor} |  | (3) |

and, for each such pair, subtracts M ⌊ n / ( x ​ y) ⌋ M_{{\left\lfloor n/(xy)\right\rfloor}} from M y ′ M^{\prime}_{y}. Note that the third inequality is equivalent to this action all happening during phase 1. Let k = ⌊ n / ( x ​ y) ⌋ k={\left\lfloor n/(xy)\right\rfloor}. Then for each Mertens value M ⁡ ( k) M(k) that we compute, we must find all pairs of integers ( x, y) (x,y) subject to the above bounds and

 | k ≤ n x ​ y < k + 1, k\leq\frac{n}{xy}<k+1, |  |

or equivalently,

 | n k + 1 < x ​ y ≤ n k. \frac{n}{k+1}<xy\leq\frac{n}{k}. |  |

Handling a single k k at a time is awfully close to factoring ⌊ n / k ⌋ {\left\lfloor n/k\right\rfloor}. To avoid breaking the clock, we will instead gather a block of consecutive Mertens values and handle them all at once. When this algorithm is fully developed, the memory usage will be O ~ ​ ( n 3) \widetilde{O}(\sqrt[3]{n}) due to the array M ′ M^{\prime} and storage inside the Möbius siever; we will therefore gather Mertens batches of size b b. The high index of each batch will be x x, and the low index will be A ​ = def ​ 1 + b ⋅ ⌊ x / b ⌋ A\overset{\mathrm{def}}{=}1+b\cdot{\left\lfloor x/b\right\rfloor}. The result is that, when processing each batch, we will be looking for all pairs ( t, ℓ) (t,\ell) such that

 | 1 ≤ t ≤ b and 2 ≤ ℓ ≤ n / t and A = b ⋅ ⌊ x b ⌋ + 1 and A ≤ ⌊ n ℓ ​ t ⌋ ≤ x. 1\leq t\leq b\qquad\text{and}\qquad 2\leq\ell\leq\sqrt{n/t}\qquad\text{and}\qquad A=b\cdot{\left\lfloor\frac{x}{b}\right\rfloor}+1\qquad\text{and}\qquad A\leq{\left\lfloor\frac{n}{\ell t}\right\rfloor}\leq x. |  |

Since A A and x x are integers, the rightmost condition is equivalent to

 | A ≤ n ℓ ​ t < x + 1, A\leq\frac{n}{\ell t}<x+1, |  |

or equivalently,

 | n t ⋅ ( x + 1) < ℓ ≤ n A ​ t. \frac{n}{t\cdot(x+1)}<\ell\leq\frac{n}{At}. |  |

Furthermore, since t ≤ b t\leq b and the relevant x x -values are ≤ ⌊ n ⌋ \leq{\left\lfloor\sqrt{n}\right\rfloor}, the lesser side of this inequality is at least Θ ~ ​ ( n 1 / 6) \widetilde{\Theta}(n^{1/6}); therefore, the restriction 2 ≤ ℓ 2\leq\ell above is superfluous.

Algorithm 8 is therefore essentially equivalent to

for*x = 1 x=1 to a a*do 0.1

if*x ≤ n x\leq\sqrt{n}*then 0.2

ℳ x ← M ⁡ ( x) \mathcal{M}_{x}\leftarrow M(x) 0.3

if*b | x b\mid x, or x = ⌊ n ⌋ x={\left\lfloor\sqrt{n}\right\rfloor},*then 0.4

Let A A be the least index in ℳ \mathcal{M}. 0.5

for*t = 1 t=1 to b b*do 0.6

ℓ m ​ i ​ n ← 1 + ⌊ n t ⋅ ( x + 1) ⌋ \ell_{min}\leftarrow 1+{\left\lfloor\dfrac{n}{t\cdot(x+1)}\right\rfloor} 0.7

ℓ m ​ a ​ x ← min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ A ⌋) \ell_{max}\leftarrow\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\dfrac{n}{t\cdot A}\right\rfloor}\right) 0.8

for*ℓ = ℓ m ​ i ​ n \ell=\ell_{min} to ℓ m ​ a ​ x \ell_{max}*do 0.9

M t ′ ← M t ′ − ℳ ⌊ n / ( ℓ ​ t) ⌋ M^{\prime}_{t}\leftarrow M^{\prime}_{t}-\mathcal{M}_{{\left\lfloor n/(\ell t)\right\rfloor}} 0.10

Forget the contents of ℳ \mathcal{M}.

Algorithm 9 Algorithm 8, redone

Applying this edit to Algorithm 7 yields Algorithm 10:

- •

Line 7 has been modified.

- •

Lines 10 – 10 have been inserted.

- •

Lines 7 and 7 have been deleted.

- •

Line 7 has been modified.

Data: n ≥ 1 n\geq 1

Result: Φ ⁡ ( n) \Phi(n)

a ← ⌊ Θ ~ ​ ( n 2 / 3) ⌋ a\leftarrow{\left\lfloor\widetilde{\Theta}(n^{2/3})\right\rfloor}; b ← ⌊ n / a ⌋ b\leftarrow{\left\lfloor n/a\right\rfloor}; X ← 0 X\leftarrow 0; Y ← 0 Y\leftarrow 0; Z ← 0 Z\leftarrow 0; m ← 0 m\leftarrow 0; s ← ⌊ n ⌋ s\leftarrow{\left\lfloor\sqrt{n}\right\rfloor}; d ← b d\leftarrow b 0.1

if*⌊ n ⌋ = ⌊ n / ⌊ n ⌋ ⌋ {\left\lfloor\sqrt{n}\right\rfloor}={\left\lfloor n/{\left\lfloor\sqrt{n}\right\rfloor}\right\rfloor}*then s ← s − 1 s\leftarrow s-1 0.2

0.3

χ ← ⌊ n / s ⌋ \chi\leftarrow{\left\lfloor n/s\right\rfloor}; γ ← ⌊ n / d ⌋ \gamma\leftarrow{\left\lfloor\sqrt{n/d}\right\rfloor} 0.4

Prepare a segmented sieve to compute μ ⁡ ( x) \mu(x) for 1 ≤ x ≤ a 1\leq x\leq a. 0.5

Let ℳ \mathcal{M} be an array of size b b. Its indexing will vary as the algorithm executes. 0.6

Let M ′ M^{\prime} be an array indexed from 1 1 to ⌊ n / ⌊ n ⌋ ⌋ {\left\lfloor n/{\left\lfloor\sqrt{n}\right\rfloor}\right\rfloor}, inclusive, initialized to all zeros. 0.7

0.8

2 for*x = 1 x=1 to a a*do 0.9

v ← ⌊ n / x ⌋ v\leftarrow{\left\lfloor n/x\right\rfloor} 0.10

m ← m + μ ⁡ ( x) m\leftarrow m+\mu(x) 0.11

X ← X + μ ⁡ ( x) ⋅ v ⋅ ( v + 1) / 2 X\leftarrow X+\mu(x)\cdot v\cdot(v+1)/2 0.12

if*x ≤ ⌊ n ⌋ x\leq{\left\lfloor\sqrt{n}\right\rfloor}*then 0.13

ℳ x ← m \mathcal{M}_{x}\leftarrow m 0.14

0.16

if*x > 1 x>1*then 0.17

for*y = 1 y=1 to min ⁡ ( b, ⌊ v / x ⌋) \min(b,{\left\lfloor v/x\right\rfloor})*do 0.18

M y ′ ← M y ′ − μ ⁡ ( x) ⋅ ⌊ v / y ⌋ M^{\prime}_{y}\leftarrow M^{\prime}_{y}-\mu(x)\cdot{\left\lfloor v/y\right\rfloor} while*x = γ x=\gamma*do 0.19

M d ′ ← M d ′ + 1 − ⌊ n / d ⌋ + m ​ x M^{\prime}_{d}\leftarrow M^{\prime}_{d}+1-{\left\lfloor n/d\right\rfloor}+mx 0.20

d ← d − 1 d\leftarrow d-1 0.21

γ ← ⌊ n / d ⌋ \gamma\leftarrow{\left\lfloor\sqrt{n/d}\right\rfloor} if*b | x b\mid x, or x = ⌊ n ⌋ x={\left\lfloor\sqrt{n}\right\rfloor},*then 0.22

Let A A be the least index in ℳ \mathcal{M}. 0.23

for*t = 1 t=1 to b b*do 0.24

ℓ m ​ i ​ n ← 1 + ⌊ n / ( t ⋅ ( x + 1)) ⌋ \ell_{min}\leftarrow 1+{\left\lfloor n/(t\cdot(x+1))\right\rfloor} 0.25

ℓ m ​ a ​ x ← min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ A ⌋) \ell_{max}\leftarrow\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\dfrac{n}{t\cdot A}\right\rfloor}\right) 0.26

for*ℓ = ℓ m ​ i ​ n \ell=\ell_{min} to ℓ m ​ a ​ x \ell_{max}*do 0.27

M t ′ ← M t ′ − ℳ ⌊ n / ( ℓ ​ t) ⌋ M^{\prime}_{t}\leftarrow M^{\prime}_{t}-\mathcal{M}_{{\left\lfloor n/(\ell t)\right\rfloor}} 0.28

Forget the contents of ℳ \mathcal{M}. else if*x = χ x=\chi*then 0.29

0.30

if*v ≠ b v\neq b*then M v ′ ← m M^{\prime}_{v}\leftarrow m 0.31

0.32

0.35

s ← s − 1 s\leftarrow s-1 0.36

χ ← ⌊ n / s ⌋ \chi\leftarrow{\left\lfloor n/s\right\rfloor} 0.37

0.43

if*x = a x=a*then Z ← m ⋅ b ⋅ ( b + 1) / 2 Z\leftarrow m\cdot b\cdot(b+1)/2 0.44

0.45

*lines 10 – 10 here*0.46

0.47

0.48

for*y = b y=b to 1 1*do 0.49

v ← ⌊ n / y ⌋ v\leftarrow{\left\lfloor n/y\right\rfloor} 0.50

m ← 0 m\leftarrow 0 0.51

for*t = 2 t=2 to ⌊ v ⌋ {\left\lfloor\sqrt{v}\right\rfloor}*do 0.52

0.56

if*⌊ v t ⌋ > ⌊ n ⌋ {\left\lfloor\dfrac{v}{t}\right\rfloor}>{\left\lfloor\sqrt{n}\right\rfloor}*then 0.57

m ← m − M ⌊ n / ⌊ v / t ⌋ ⌋ ′ m\leftarrow m-M^{\prime}_{{\left\lfloor n/{\left\lfloor v/t\right\rfloor}\right\rfloor}} M y ′ ← M y ′ + m M^{\prime}_{y}\leftarrow M^{\prime}_{y}+m 0.58

Y ← Y + y ⋅ M y ′ Y\leftarrow Y+y\cdot M^{\prime}_{y} 0.59

0.60

return X + Y − Z X+Y-Z

Algorithm 10 Compute Φ ⁡ ( n) \Phi(n) in Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time and Θ ~ ​ ( n 1 / 2) \widetilde{\Theta}(n^{1/2}) space.

The only thing left to do is remove the need to store M k ′ M^{\prime}_{k} for k > b k>b. This entails moving the action of line 10 into phase 2. The work done by this line is essentially

for*y = b y=b to 1 1*do 0.1

v ← ⌊ n / y ⌋ v\leftarrow{\left\lfloor n/y\right\rfloor} 0.2

m ← 0 m\leftarrow 0 0.3

for*t = 2 t=2 to ⌊ v ⌋ {\left\lfloor\sqrt{v}\right\rfloor}*do 0.4

if*⌊ v / t ⌋ > ⌊ n ⌋ {\left\lfloor v/t\right\rfloor}>{\left\lfloor\sqrt{n}\right\rfloor}*then 0.5

m ← m − M ⌊ n / ⌊ v / t ⌋ ⌋ ′ m\leftarrow m-M^{\prime}_{{\left\lfloor n/{\left\lfloor v/t\right\rfloor}\right\rfloor}} M y ′ ← M y ′ + m M^{\prime}_{y}\leftarrow M^{\prime}_{y}+m

Algorithm 11 An extract from Algorithm 10

Let x x be the index of a Mertens value that gets saved during phase 2 (so that ⌊ n ⌋ < x ≤ a {\left\lfloor\sqrt{n}\right\rfloor}<x\leq a). It gets stored as M ⌊ n / x ⌋ ′ M^{\prime}_{\left\lfloor n/x\right\rfloor}, and the t t - and y y -values of this loop that touch it are exactly those that satisfy

 | 1 ≤ y ≤ b and 2 ≤ t ≤ ⌊ n / y ⌋ and ⌊ n ⌋ < ⌊ n t ​ y ⌋ and ⌊ n x ⌋ = ⌊ n ⌊ n / ( t ​ y) ⌋ ⌋. 1\leq y\leq b\quad\text{and}\quad 2\leq t\leq{\left\lfloor\sqrt{n/y}\right\rfloor}\quad\text{and}\quad{\left\lfloor\sqrt{n}\right\rfloor}<{\left\lfloor\frac{n}{ty}\right\rfloor}\quad\text{and}\quad{\left\lfloor\frac{n}{x}\right\rfloor}={\left\lfloor\frac{n}{{\left\lfloor n/(ty)\right\rfloor}}\right\rfloor}. |  |

As with the transition from Algorithm 7 to Algorithm 10, we need to assemble a batch of Mertens values and process them all at once to avoid breaking the clock. To accommodate this, for each x x -value such that M ⁡ ( x) M(x) gets assembled into the batch, let w = ⌊ n / x ⌋ w={\left\lfloor n/x\right\rfloor}. Let A A be the greatest w w -value in the batch and let B B be the least. Then the restrictions on t t and y y become

 | 1 ≤ y ≤ b and 2 ≤ t ≤ ⌊ n / y ⌋ and ⌊ n ⌋ < ⌊ n t ​ y ⌋ and B ≤ ⌊ n ⌊ n / ( t ​ y) ⌋ ⌋ ≤ A. 1\leq y\leq b\quad\text{and}\quad 2\leq t\leq{\left\lfloor\sqrt{n/y}\right\rfloor}\quad\text{and}\quad{\left\lfloor\sqrt{n}\right\rfloor}<{\left\lfloor\frac{n}{ty}\right\rfloor}\quad\text{and}\quad B\leq{\left\lfloor\frac{n}{{\left\lfloor n/(ty)\right\rfloor}}\right\rfloor}\leq A. |  | (4) |

Applying this edit to Algorithm 10 yields Algorithm 12:

- •

Line 10 has been modified.

- •

Line 10 has been modified.

- •

Lines 12 and 12 have been inserted.

- •

Lines 12 – 12 have been inserted.

- •

Line 10 has been modified.

Data: n ≥ 1 n\geq 1

Result: Φ ⁡ ( n) \Phi(n)

a ← ⌊ Θ ~ ​ ( n 2 / 3) ⌋ a\leftarrow{\left\lfloor\widetilde{\Theta}(n^{2/3})\right\rfloor}; b ← ⌊ n / a ⌋ b\leftarrow{\left\lfloor n/a\right\rfloor}; X ← 0 X\leftarrow 0; Y ← 0 Y\leftarrow 0; Z ← 0 Z\leftarrow 0; m ← 0 m\leftarrow 0; s ← ⌊ n ⌋ s\leftarrow{\left\lfloor\sqrt{n}\right\rfloor}; d ← b d\leftarrow b 0.1

if*⌊ n ⌋ = ⌊ n / ⌊ n ⌋ ⌋ {\left\lfloor\sqrt{n}\right\rfloor}={\left\lfloor n/{\left\lfloor\sqrt{n}\right\rfloor}\right\rfloor}*then s ← s − 1 s\leftarrow s-1 0.2

0.3

χ ← ⌊ n / s ⌋ \chi\leftarrow{\left\lfloor n/s\right\rfloor}; γ ← ⌊ n / d ⌋ \gamma\leftarrow{\left\lfloor\sqrt{n/d}\right\rfloor} 0.4

Prepare a segmented sieve to compute μ ⁡ ( x) \mu(x) for 1 ≤ x ≤ a 1\leq x\leq a. 0.5

Let ℳ \mathcal{M} be an array of size b b. Its indexing will vary as the algorithm executes. 0.6

Let M ′ M^{\prime} be an array indexed from 1 1 to b b, inclusive, initialized to all zeros. 0.7

0.8

2 for*x = 1 x=1 to a a*do 0.9

v ← ⌊ n / x ⌋ v\leftarrow{\left\lfloor n/x\right\rfloor} 0.10

m ← m + μ ⁡ ( x) m\leftarrow m+\mu(x) 0.11

X ← X + μ ⁡ ( x) ⋅ v ⋅ ( v + 1) / 2 X\leftarrow X+\mu(x)\cdot v\cdot(v+1)/2 0.12

if*x ≤ ⌊ n ⌋ x\leq{\left\lfloor\sqrt{n}\right\rfloor}*then 0.13

ℳ x ← m \mathcal{M}_{x}\leftarrow m 0.14

0.16

if*x > 1 x>1*then 0.17

for*y = 1 y=1 to min ⁡ ( b, ⌊ v / x ⌋) \min(b,{\left\lfloor v/x\right\rfloor})*do 0.18

M y ′ ← M y ′ − μ ⁡ ( x) ⋅ ⌊ v / y ⌋ M^{\prime}_{y}\leftarrow M^{\prime}_{y}-\mu(x)\cdot{\left\lfloor v/y\right\rfloor} while*x = γ x=\gamma*do 0.19

M d ′ ← M d ′ + 1 − ⌊ n / d ⌋ + m ​ x M^{\prime}_{d}\leftarrow M^{\prime}_{d}+1-{\left\lfloor n/d\right\rfloor}+mx 0.20

d ← d − 1 d\leftarrow d-1 0.21

γ ← ⌊ n / d ⌋ \gamma\leftarrow{\left\lfloor\sqrt{n/d}\right\rfloor} if*b | x b\mid x, or x = ⌊ n ⌋ x={\left\lfloor\sqrt{n}\right\rfloor},*then 0.22

Let A A be the least index in ℳ \mathcal{M}. 0.23

for*t = 1 t=1 to b b*do 0.24

ℓ m ​ i ​ n ← 1 + ⌊ n / ( t ⋅ ( x + 1)) ⌋ \ell_{min}\leftarrow 1+{\left\lfloor n/(t\cdot(x+1))\right\rfloor} 0.25

ℓ m ​ a ​ x ← min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ A ⌋) \ell_{max}\leftarrow\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\dfrac{n}{t\cdot A}\right\rfloor}\right) 0.26

for*ℓ = ℓ m ​ i ​ n \ell=\ell_{min} to ℓ m ​ a ​ x \ell_{max}*do 0.27

M t ′ ← M t ′ − ℳ ⌊ n / ( ℓ ​ t) ⌋ M^{\prime}_{t}\leftarrow M^{\prime}_{t}-\mathcal{M}_{{\left\lfloor n/(\ell t)\right\rfloor}} 0.28

Forget the contents of ℳ \mathcal{M}. else if*x = χ x=\chi*then 0.29

0.30

if*v ≠ b v\neq b*then 0.31

0.32

if*ℳ \mathcal{M} is empty*then A ← v A\leftarrow v 0.33

0.34

ℳ v ← m \mathcal{M}_{v}\leftarrow m; B ← v B\leftarrow v 0.35

s ← s − 1 s\leftarrow s-1 0.36

χ ← ⌊ n / s ⌋ \chi\leftarrow{\left\lfloor n/s\right\rfloor} if*x = a x=a or ( x > ⌊ n ⌋ x>{\left\lfloor\sqrt{n}\right\rfloor} and ℳ \mathcal{M} is full)*then 0.37

for*y = 1 y=1 to b b*do 0.38

forall*t t satisfying ( 4)*do 0.39

M y ′ ← M y ′ − ℳ t ​ y M^{\prime}_{y}\leftarrow M^{\prime}_{y}-\mathcal{M}_{ty} Forget the contents of ℳ \mathcal{M}. if*x = a x=a*then Z ← m ⋅ b ⋅ ( b + 1) / 2 Z\leftarrow m\cdot b\cdot(b+1)/2 0.40

0.41

*lines 12 – 12 here*0.42

0.43

0.44

for*y = b y=b to 1 1*do 0.45

v ← ⌊ n / y ⌋ v\leftarrow{\left\lfloor n/y\right\rfloor} 0.46

m ← 0 m\leftarrow 0 0.47

for*t = 2 t=2 to ⌊ v ⌋ {\left\lfloor\sqrt{v}\right\rfloor}*do 0.48

0.52

if*⌊ v t ⌋ > ⌊ n ⌋ {\left\lfloor\dfrac{v}{t}\right\rfloor}>{\left\lfloor\sqrt{n}\right\rfloor} and ⌊ n ⌊ v / t ⌋ ⌋ ≤ b {\left\lfloor\dfrac{n}{{\left\lfloor v/t\right\rfloor}}\right\rfloor}\leq b*then 0.53

m ← m − M ⌊ n / ⌊ v / t ⌋ ⌋ ′ m\leftarrow m-M^{\prime}_{{\left\lfloor n/{\left\lfloor v/t\right\rfloor}\right\rfloor}} M y ′ ← M y ′ + m M^{\prime}_{y}\leftarrow M^{\prime}_{y}+m 0.54

Y ← Y + y ⋅ M y ′ Y\leftarrow Y+y\cdot M^{\prime}_{y} 0.55

0.56

return X + Y − Z X+Y-Z

Algorithm 12 Compute Φ ⁡ ( n) \Phi(n) in Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time and Θ ~ ​ ( n 1 / 3) \widetilde{\Theta}(n^{1/3}) space.

We have now hit our target time- and space-complexities, but some further optimization can be done. In particular, the iteration over t t in phase 3—lines 12 – 12 —can be made more efficient. The conditions on t t are

 | 2 ≤ t ≤ ⌊ n / y ⌋ and ⌊ n ⌋ < ⌊ ⌊ n / y ⌋ t ⌋ and ⌊ n ⌊ ⌊ n / y ⌋ / t ⌋ ⌋ ≤ b, 2\leq t\leq{\left\lfloor\sqrt{n/y}\right\rfloor}\qquad\text{and}\qquad{\left\lfloor\sqrt{n}\right\rfloor}<{\left\lfloor\frac{{\left\lfloor n/y\right\rfloor}}{t}\right\rfloor}\qquad\text{and}\qquad{\left\lfloor\frac{n}{{\left\lfloor{\left\lfloor n/y\right\rfloor}/t\right\rfloor}}\right\rfloor}\leq b, |  |

which is equivalent to

 | 2 ≤ t ≤ ⌊ n / y ⌋ and ⌊ n ⌋ + 1 ≤ ⌊ n / y ⌋ t and n ⌊ ⌊ n / y ⌋ / t ⌋ < b + 1. 2\leq t\leq{\left\lfloor\sqrt{n/y}\right\rfloor}\qquad\text{and}\qquad{\left\lfloor\sqrt{n}\right\rfloor}+1\leq\frac{{\left\lfloor n/y\right\rfloor}}{t}\qquad\text{and}\qquad\frac{n}{{\left\lfloor{\left\lfloor n/y\right\rfloor}/t\right\rfloor}}<b+1. |  |

Since t t is an integer, we can drop the floor function from the first inequality.

 | 2 ≤ t ≤ n / y and t ≤ ⌊ n / y ⌋ ⌊ n ⌋ + 1 and n b + 1 < ⌊ ⌊ n / y ⌋ t ⌋. 2\leq t\leq\sqrt{n/y}\qquad\text{and}\qquad t\leq\frac{{\left\lfloor n/y\right\rfloor}}{{\left\lfloor\sqrt{n}\right\rfloor}+1}\qquad\text{and}\qquad\frac{n}{b+1}<{\left\lfloor\frac{{\left\lfloor n/y\right\rfloor}}{t}\right\rfloor}. |  |

By Lemmas 8 and 9, we can drop the t ≤ n / y t\leq\sqrt{n/y} condition and the middle inequality, leaving us with

 | 2 ≤ t and n b + 1 < ⌊ ⌊ n / y ⌋ t ⌋. 2\leq t\qquad\text{and}\qquad\frac{n}{b+1}<{\left\lfloor\frac{{\left\lfloor n/y\right\rfloor}}{t}\right\rfloor}. |  |

A further improvement can be had by inserting “and μ ⁡ ( x) ≠ 0 \mu(x)\neq 0 ” into line 12.

Making the corresponding edits modifies lines 12, 12, and 12 to yield Algorithm 13.

Data: n ≥ 1 n\geq 1

Result: Φ ⁡ ( n) \Phi(n)

a ← ⌊ Θ ~ ​ ( n 2 / 3) ⌋ a\leftarrow{\left\lfloor\widetilde{\Theta}(n^{2/3})\right\rfloor}; b ← ⌊ n / a ⌋ b\leftarrow{\left\lfloor n/a\right\rfloor}; X ← 0 X\leftarrow 0; Y ← 0 Y\leftarrow 0; Z ← 0 Z\leftarrow 0; m ← 0 m\leftarrow 0; s ← ⌊ n ⌋ s\leftarrow{\left\lfloor\sqrt{n}\right\rfloor}; d ← b d\leftarrow b 0.1

if*⌊ n ⌋ = ⌊ n / ⌊ n ⌋ ⌋ {\left\lfloor\sqrt{n}\right\rfloor}={\left\lfloor n/{\left\lfloor\sqrt{n}\right\rfloor}\right\rfloor}*then s ← s − 1 s\leftarrow s-1 0.2

0.3

χ ← ⌊ n / s ⌋ \chi\leftarrow{\left\lfloor n/s\right\rfloor}; γ ← ⌊ n / d ⌋ \gamma\leftarrow{\left\lfloor\sqrt{n/d}\right\rfloor} 0.4

Prepare a segmented sieve to compute μ ⁡ ( x) \mu(x) for 1 ≤ x ≤ a 1\leq x\leq a. 0.5

Let ℳ \mathcal{M} be an array of size b b. Its indexing will vary as the algorithm executes. 0.6

Let M ′ M^{\prime} be an array indexed from 1 1 to b b, inclusive, initialized to all zeros. 0.7

0.8

2 for*x = 1 x=1 to a a*do 0.9

v ← ⌊ n / x ⌋ v\leftarrow{\left\lfloor n/x\right\rfloor} 0.10

m ← m + μ ⁡ ( x) m\leftarrow m+\mu(x) 0.11

X ← X + μ ⁡ ( x) ⋅ v ⋅ ( v + 1) / 2 X\leftarrow X+\mu(x)\cdot v\cdot(v+1)/2 0.12

if*x ≤ ⌊ n ⌋ x\leq{\left\lfloor\sqrt{n}\right\rfloor}*then 0.13

ℳ x ← m \mathcal{M}_{x}\leftarrow m 0.14

0.16

if*x > 1 x>1 and μ ⁡ ( x) ≠ 0 \mu(x)\neq 0*then 0.17

for*y = 1 y=1 to min ⁡ ( b, ⌊ v / x ⌋) \min(b,{\left\lfloor v/x\right\rfloor})*do 0.18

M y ′ ← M y ′ − μ ⁡ ( x) ⋅ ⌊ v / y ⌋ M^{\prime}_{y}\leftarrow M^{\prime}_{y}-\mu(x)\cdot{\left\lfloor v/y\right\rfloor} while*x = γ x=\gamma*do 0.19

M d ′ ← M d ′ + 1 − ⌊ n / d ⌋ + m ​ x M^{\prime}_{d}\leftarrow M^{\prime}_{d}+1-{\left\lfloor n/d\right\rfloor}+mx 0.20

d ← d − 1 d\leftarrow d-1 0.21

γ ← ⌊ n / d ⌋ \gamma\leftarrow{\left\lfloor\sqrt{n/d}\right\rfloor} if*b | x b\mid x, or x = ⌊ n ⌋ x={\left\lfloor\sqrt{n}\right\rfloor},*then 0.22

Let A A be the least index in ℳ \mathcal{M}. 0.23

for*t = 1 t=1 to b b*do 0.24

ℓ m ​ i ​ n ← 1 + ⌊ n / ( t ⋅ ( x + 1)) ⌋ \ell_{min}\leftarrow 1+{\left\lfloor n/(t\cdot(x+1))\right\rfloor} 0.25

ℓ m ​ a ​ x ← min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ A ⌋) \ell_{max}\leftarrow\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\dfrac{n}{t\cdot A}\right\rfloor}\right) 0.26

for*ℓ = ℓ m ​ i ​ n \ell=\ell_{min} to ℓ m ​ a ​ x \ell_{max}*do 0.27

M t ′ ← M t ′ − ℳ ⌊ n / ( ℓ ​ t) ⌋ M^{\prime}_{t}\leftarrow M^{\prime}_{t}-\mathcal{M}_{{\left\lfloor n/(\ell t)\right\rfloor}} 0.28

Forget the contents of ℳ \mathcal{M}. else if*x = χ x=\chi*then 0.29

0.30

if*v ≠ b v\neq b*then 0.31

0.32

if*ℳ \mathcal{M} is empty*then A ← v A\leftarrow v 0.33

0.34

ℳ v ← m \mathcal{M}_{v}\leftarrow m; B ← v B\leftarrow v 0.35

s ← s − 1 s\leftarrow s-1 0.36

χ ← ⌊ n / s ⌋ \chi\leftarrow{\left\lfloor n/s\right\rfloor} if*x = a x=a or ( x > ⌊ n ⌋ x>{\left\lfloor\sqrt{n}\right\rfloor} and ℳ \mathcal{M} is full)*then 0.37

for*y = 1 y=1 to b b*do 0.38

forall*t t satisfying ( 4)*do 0.39

M y ′ ← M y ′ − ℳ t ​ y M^{\prime}_{y}\leftarrow M^{\prime}_{y}-\mathcal{M}_{ty} Forget the contents of ℳ \mathcal{M}. if*x = a x=a*then Z ← m ⋅ b ⋅ ( b + 1) / 2 Z\leftarrow m\cdot b\cdot(b+1)/2 0.40

0.41

*lines 13 – 13 here*0.42

0.43

0.44

for*y = b y=b to 1 1*do 0.45

v ← ⌊ n / y ⌋ v\leftarrow{\left\lfloor n/y\right\rfloor} 0.46

m ← 0 m\leftarrow 0 0.47

for*t ∈ { 2, 3, 4, … } t\in{\left\{2,3,4,...\right\}}*do 0.48

0.52

if*n b + 1 ≥ ⌊ v t ⌋ \displaystyle\frac{n}{b+1}\geq{\left\lfloor\frac{v}{t}\right\rfloor}*then break 0.53

0.54

m ← m − M ⌊ n / ⌊ v / t ⌋ ⌋ ′ m\leftarrow m-M^{\prime}_{{\left\lfloor n/{\left\lfloor v/t\right\rfloor}\right\rfloor}} M y ′ ← M y ′ + m M^{\prime}_{y}\leftarrow M^{\prime}_{y}+m 0.55

Y ← Y + y ⋅ M y ′ Y\leftarrow Y+y\cdot M^{\prime}_{y} 0.56

0.57

return X + Y − Z X+Y-Z

Algorithm 13 Compute Φ ⁡ ( n) \Phi(n) in Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time and Θ ~ ​ ( n 1 / 3) \widetilde{\Theta}(n^{1/3}) space.

## 4 Analysis of Algorithm 13

The inner loops of Algorithm 13 are inside the Möbius siever and lines 13, 13 – 13, 13, 13, and 13 – 13.

###### 1.

The Möbius sieving consumes Θ ⁡ ( a ​ ln ⁡ ( ln ⁡ ( a))) \Theta(a\ln(\ln(a))) time.

The Möbius function is sieved up to a a; the rest is a standard result. ∎

###### 2.

Line 13 consumes Θ ⁡ ( n / a) \Theta(n/\sqrt{a}) time.

Line 13 is hit

 | ∑ 2 ≤ x ≤ ⌊ n ⌋ μ ⁡ ( x) ≠ 0 min ⁡ ( ⌊ n a ⌋, ⌊ n x 2 ⌋) \sum_{\begin{subarray}{c}2\leq x\leq{\left\lfloor\sqrt{n}\right\rfloor}\\ \mu(x)\neq 0\end{subarray}}\min\left({\left\lfloor\frac{n}{a}\right\rfloor},{\left\lfloor\frac{n}{x^{2}}\right\rfloor}\right) |  |

times. Since the squarefree integers have a natural density of 6 / π 2 6/\pi^{2}, this is

 | = Θ ⁡ ( ∑ x = 2 ⌊ n ⌋ min ⁡ ( ⌊ n a ⌋, ⌊ n x 2 ⌋)) =\Theta\left(\sum_{x=2}^{{\left\lfloor\sqrt{n}\right\rfloor}}\min\left({\left\lfloor\frac{n}{a}\right\rfloor},{\left\lfloor\frac{n}{x^{2}}\right\rfloor}\right)\right) |  |

 | = Θ ⁡ ( ∑ x = 2 ⌊ a ⌋ ⌊ n a ⌋ + ∑ x = ⌊ a ⌋ + 1 ⌊ n ⌋ ⌊ n x 2 ⌋) =\Theta\left(\sum_{x=2}^{{\left\lfloor\sqrt{a}\right\rfloor}}{\left\lfloor\frac{n}{a}\right\rfloor}+\sum_{x={\left\lfloor\sqrt{a}\right\rfloor}+1}^{{\left\lfloor\sqrt{n}\right\rfloor}}{\left\lfloor\frac{n}{x^{2}}\right\rfloor}\right) |  |

 | = Θ ⁡ ( ⌊ n a ⌋ ⋅ ( ⌊ a ⌋ − 1) + ∫ ⌊ a ⌋ + 1 ⌊ n ⌋ n x 2 ​ 𝑑 x) =\Theta\left({\left\lfloor\frac{n}{a}\right\rfloor}\cdot\left({\left\lfloor\sqrt{a}\right\rfloor}-1\right)+\displaystyle\int_{{\left\lfloor\sqrt{a}\right\rfloor}+1}^{{\left\lfloor\sqrt{n}\right\rfloor}}\!\;\frac{n}{x^{2}}\,dx\right) |  |

 | = Θ ⁡ ( ⌊ n a ⌋ ⋅ ( ⌊ a ⌋ − 1) + n ⌊ a ⌋ + 1 − n ⌊ n ⌋) =\Theta\left({\left\lfloor\frac{n}{a}\right\rfloor}\cdot\left({\left\lfloor\sqrt{a}\right\rfloor}-1\right)+\frac{n}{{\left\lfloor\sqrt{a}\right\rfloor}+1}-\frac{n}{{\left\lfloor\sqrt{n}\right\rfloor}}\right) |  |

 | = Θ ⁡ ( n a), =\Theta\left(\frac{n}{\sqrt{a}}\right), |  |

as desired. ∎

###### 3.

The runtime of Algorithm 13 is at least Θ ⁡ ( n 2 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 1 / 3) \Theta(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}).

By Lemmas 1 and 2, the combined runtime of of the Möbius sieving and line 13 is

 | Θ ⁡ ( a ​ ln ⁡ ( ln ⁡ ( a))) + Θ ⁡ ( n a), \Theta(a\ln(\ln(a)))+\Theta\left(\frac{n}{\sqrt{a}}\right), |  |

which is minimized by choosing

 | a = Θ ⁡ ( ( n ln ⁡ ( ln ⁡ ( n))) 2 / 3); a=\Theta\left(\left(\frac{n}{\ln(\ln(n))}\right)^{2/3}\right); |  |

the runtime of those parts is then Θ ⁡ ( n 2 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 1 / 3) \Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}\right) each. ∎

Lines 13 – 13 can be neglected: they get hit at most b b times.

###### 4.

With a = Θ ⁡ ( ( n / ln ⁡ ( ln ⁡ ( n))) 2 / 3) a=\Theta((n/\ln(\ln(n)))^{2/3}), line 13 consumes Θ ⁡ ( n 2 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 1 / 3) \Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}\right) time.

Line 13 gets hit at least

 | ∑ 1 ≤ x ≤ n b | x ∑ t = 1 b ( 1 + max ⁡ ( ℓ m ​ a ​ x ​ ( x, t) − ℓ m ​ i ​ n ​ ( x, t), 0)) \sum_{\begin{subarray}{c}1\leq x\leq\sqrt{n}\\ b\mid x\end{subarray}}\sum_{t=1}^{b}\left(1+\max\left(\ell_{max}(x,t)-\ell_{min}(x,t),0\right)\right) |  |

times. If b | ⌊ n ⌋ b\mid{\left\lfloor\sqrt{n}\right\rfloor}, then this is exactly the number of hits; otherwise, there will be a final phase-1 batch that is not included in the above sum.

The first batch ( x = b x=b) and that possible last batch ( x = ⌊ n ⌋ ≢ 0 ( mod b)) (x={\left\lfloor\sqrt{n}\right\rfloor}\not\equiv 0\pmod{b}) need special handling. For the first batch, when x = b x=b, the relevant section of the algorithm amounts to

begin 0.1

for*t = 1 t=1 to b b*do 0.2

ℓ m ​ i ​ n ← 1 + ⌊ n t ⋅ ( b + 1) ⌋ \ell_{min}\leftarrow 1+{\left\lfloor\dfrac{n}{t\cdot(b+1)}\right\rfloor} 0.3

ℓ m ​ a ​ x ← min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⌋) \ell_{max}\leftarrow\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\dfrac{n}{t}\right\rfloor}\right) 0.4

for*ℓ = ℓ m ​ i ​ n \ell=\ell_{min} to ℓ m ​ a ​ x \ell_{max}*do 0.5

M t ′ ← M t ′ − ℳ ⌊ n / ( ℓ ​ t) ⌋ M^{\prime}_{t}\leftarrow M^{\prime}_{t}-\mathcal{M}_{{\left\lfloor n/(\ell t)\right\rfloor}} 0.6

Algorithm 14 An extract from Algorithm 13, with x = b x=b

The time consumed by this extract is

 | ∑ t = 1 b ( 1 + max ⁡ ( ℓ m ​ a ​ x − ℓ m ​ i ​ n, 0)) \sum_{t=1}^{b}\left(1+\max\left(\ell_{max}-\ell_{min},0\right)\right) |  |

 | = ∑ t = 1 b ( 1 + max ⁡ ( min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⌋) − 1 − ⌊ n t ⋅ ( b + 1) ⌋, 0)) =\sum_{t=1}^{b}\left(1+\max\left(\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\frac{n}{t}\right\rfloor}\right)-1-{\left\lfloor\frac{n}{t\cdot(b+1)}\right\rfloor},0\right)\right) |  |

 | = b + ∑ t = 1 b max ⁡ ( min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⌋) − 1 − ⌊ n t ⋅ ( b + 1) ⌋, 0). =b+\sum_{t=1}^{b}\max\left(\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\frac{n}{t}\right\rfloor}\right)-1-{\left\lfloor\frac{n}{t\cdot(b+1)}\right\rfloor},0\right). |  |

We have 0 < t < n 0<t<n, so n / t ≤ n / t \sqrt{n/t}\leq n/t.

 | = b + ∑ t = 1 b max ⁡ ( ⌊ n / t ⌋ − 1 − ⌊ n t ⋅ ( b + 1) ⌋, 0) =b+\sum_{t=1}^{b}\max\left({\left\lfloor\sqrt{n/t}\right\rfloor}-1-{\left\lfloor\frac{n}{t\cdot(b+1)}\right\rfloor},0\right) |  |

For b ≤ n 1 / 3 b\leq n^{1/3}, Lemma 10 establishes that the first argument of the max \max function is negative, so the time consumed by the extract is O ⁡ ( b) O(b). The case b > n 1 / 3 b>n^{1/3} is a bit more complicated: in this case, the max \max function’s first argument prevails for

 | t > t 0 ​ = def ​ n ⋅ ( 1 2 − 1 b + 1 − 1 4 − 1 b + 1), t>t_{0}\overset{\mathrm{def}}{=}n\cdot\left(\frac{1}{2}-\frac{1}{b+1}-\sqrt{\frac{1}{4}-\frac{1}{b+1}}\right), |  |

so the time consumed by the extract is

 | b + ∑ t = t 0 b ( ⌊ n / t ⌋ − 1 − ⌊ n t ⋅ ( b + 1) ⌋). b+\sum_{t=t_{0}}^{b}\left({\left\lfloor\sqrt{n/t}\right\rfloor}-1-{\left\lfloor\frac{n}{t\cdot(b+1)}\right\rfloor}\right). |  |

The sum will turn out to be Θ ~ ​ ( a) \widetilde{\Theta}(a), so the b b is neglectably small.

 | = Θ ⁡ ( ∫ t 0 b ( n t − 1 − n t ⋅ ( b + 1)) ​ 𝑑 t) =\Theta\left(\int_{t_{0}}^{b}\left(\sqrt{\frac{n}{t}}-1-\frac{n}{t\cdot(b+1)}\right)dt\right) |  |

 | = Θ ⁡ ( 2 ​ b ​ n − 2 ​ n ​ t 0 − b + t 0 + n b + 1 ⋅ ln ⁡ ( t 0 b)) =\Theta\left(2\sqrt{bn}-2\sqrt{nt_{0}}-b+t_{0}+\frac{n}{b+1}\cdot\ln\left(\frac{t_{0}}{b}\right)\right) |  |

From Lemma 11, we have that t 0 = n ⋅ ( b − 2 + O ⁡ ( b − 3)) t_{0}=n\cdot(b^{-2}+O(b^{-3})). Therefore,

 | = Θ ⁡ ( 2 ​ b ​ n − 2 ​ n 2 ⋅ ( b − 2 + O ⁡ ( b − 3)) − b + n ⋅ ( b − 2 + O ⁡ ( b − 3)) + n b + 1 ⋅ ln ⁡ ( n ⋅ ( b − 2 + O ⁡ ( b − 3)) b)) =\Theta\left(2\sqrt{bn}-2\sqrt{n^{2}\cdot(b^{-2}+O(b^{-3}))}-b+n\cdot(b^{-2}+O(b^{-3}))+\frac{n}{b+1}\cdot\ln\left(\frac{n\cdot(b^{-2}+O(b^{-3}))}{b}\right)\right) |  |

 | = Θ ⁡ ( 2 ​ b ​ n − 2 ​ a ​ 1 + O ⁡ ( b − 1) − b + n b 2 ⋅ ( 1 + O ⁡ ( b − 1)) + a 1 + 1 / b ⋅ ln ⁡ ( n b 3 ⋅ ( 1 + O ⁡ ( b − 1)))). =\Theta\left(2\sqrt{bn}-2a\sqrt{1+O(b^{-1})}-b+\frac{n}{b^{2}}\cdot(1+O(b^{-1}))+\frac{a}{1+1/b}\cdot\ln\left(\frac{n}{b^{3}}\cdot(1+O(b^{-1}))\right)\right). |  |

Recall that we are working with a = Θ ⁡ ( ( n / ln ⁡ ( ln ⁡ ( n))) 2 / 3) a=\Theta\left((n/\ln(\ln(n)))^{2/3}\right), so b = Θ ⁡ ( n 1 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 2 / 3) b=\Theta\left(n^{1/3}\cdot(\ln(\ln(n)))^{2/3}\right). Therefore the first term dominates the rest, yielding

 | = Θ ⁡ ( n 2 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 1 / 3). =\Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}\right). |  |

In the last batch, when x = ⌊ n ⌋ ≢ 0 ( mod b) x={\left\lfloor\sqrt{n}\right\rfloor}\not\equiv 0\pmod{b}, the relevant section of the algorithm amounts to

begin 0.1

x ← ⌊ n ⌋ x\leftarrow{\left\lfloor\sqrt{n}\right\rfloor} 0.2

A ← 1 + b ⋅ ⌊ x / b ⌋ A\leftarrow 1+b\cdot{\left\lfloor x/b\right\rfloor} 0.3

for*t = 1 t=1 to b b*do 0.4

ℓ m ​ i ​ n ← 1 + ⌊ n t ⋅ ( x + 1) ⌋ \ell_{min}\leftarrow 1+{\left\lfloor\dfrac{n}{t\cdot(x+1)}\right\rfloor} 0.5

ℓ m ​ a ​ x ← min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ A ⌋) \ell_{max}\leftarrow\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\dfrac{n}{t\cdot A}\right\rfloor}\right) 0.6

for*ℓ = ℓ m ​ i ​ n \ell=\ell_{min} to ℓ m ​ a ​ x \ell_{max}*do 0.7

M t ′ ← M t ′ − ℳ ⌊ n / ( ℓ ​ t) ⌋ M^{\prime}_{t}\leftarrow M^{\prime}_{t}-\mathcal{M}_{{\left\lfloor n/(\ell t)\right\rfloor}} 0.8

Algorithm 15 An extract from Algorithm 13, with x = ⌊ n ⌋ ≢ 0 ( mod b) x={\left\lfloor\sqrt{n}\right\rfloor}\not\equiv 0\pmod{b}

The time consumed by this extract is

 | ∑ t = 1 b ( 1 + max ⁡ ( ℓ m ​ a ​ x − ℓ m ​ i ​ n, 0)) \sum_{t=1}^{b}\left(1+\max\left(\ell_{max}-\ell_{min},0\right)\right) |  |

 | = b + ∑ t = 1 b max ⁡ ( min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ A ⌋) − 1 − ⌊ n t ⋅ ( x + 1) ⌋, 0) =b+\sum_{t=1}^{b}\max\left(\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\dfrac{n}{t\cdot A}\right\rfloor}\right)-1-{\left\lfloor\dfrac{n}{t\cdot(x+1)}\right\rfloor},0\right) |  |

 | = b + ∑ t = 1 b max ⁡ ( min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ ( 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋) ⌋) − 1 − ⌊ n t ⋅ ( ⌊ n ⌋ + 1) ⌋, 0). =b+\sum_{t=1}^{b}\max\left(\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\dfrac{n}{t\cdot\left(1+b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}\right)}\right\rfloor}\right)-1-{\left\lfloor\dfrac{n}{t\cdot({\left\lfloor\sqrt{n}\right\rfloor}+1)}\right\rfloor},0\right). |  | (5) |

We split off the t = 1 t=1 term for special treatment: this is

 | max ⁡ ( min ⁡ ( ⌊ n ⌋, ⌊ n 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋ ⌋) − 1 − ⌊ n ⌊ n ⌋ + 1 ⌋, 0). \max\left(\min\left({\left\lfloor\sqrt{n}\right\rfloor},{\left\lfloor\dfrac{n}{1+b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}}\right\rfloor}\right)-1-{\left\lfloor\dfrac{n}{{\left\lfloor\sqrt{n}\right\rfloor}+1}\right\rfloor},0\right). |  |

By hypothesis, we are working with ⌊ n ⌋ ≢ 0 ( mod b) {\left\lfloor\sqrt{n}\right\rfloor}\not\equiv 0\pmod{b}, so 1 + b ⋅ ⌊ ⌊ n ⌋ / b ⌋ ≤ ⌊ n ⌋ 1+b\cdot{\left\lfloor{\left\lfloor\sqrt{n}\right\rfloor}/b\right\rfloor}\leq{\left\lfloor\sqrt{n}\right\rfloor}. Therefore, in the min \min function, the first argument prevails.

 | = max ⁡ ( ⌊ n ⌋ − 1 − ⌊ n ⌊ n ⌋ + 1 ⌋, 0) =\max\left({\left\lfloor\sqrt{n}\right\rfloor}-1-{\left\lfloor\dfrac{n}{{\left\lfloor\sqrt{n}\right\rfloor}+1}\right\rfloor},0\right) |  |

 | = 0 =0 |  |

Therefore ( 5) becomes

 | = b + ∑ t = 2 b max ⁡ ( min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ ( 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋) ⌋) − 1 − ⌊ n t ⋅ ( ⌊ n ⌋ + 1) ⌋, 0). =b+\sum_{t=2}^{b}\max\left(\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\dfrac{n}{t\cdot\left(1+b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}\right)}\right\rfloor}\right)-1-{\left\lfloor\dfrac{n}{t\cdot({\left\lfloor\sqrt{n}\right\rfloor}+1)}\right\rfloor},0\right). |  |

By Lemma 12, in the min \min function, the second argument prevails.

 | = b + ∑ t = 2 b max ⁡ ( ⌊ n t ⋅ ( 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋) ⌋ − 1 − ⌊ n t ⋅ ( ⌊ n ⌋ + 1) ⌋, 0) =b+\sum_{t=2}^{b}\max\left({\left\lfloor\frac{n}{t\cdot\left(1+b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}\right)}\right\rfloor}-1-{\left\lfloor\frac{n}{t\cdot({\left\lfloor\sqrt{n}\right\rfloor}+1)}\right\rfloor},0\right) |  |

 | = Θ ⁡ ( b + ∫ 2 b max ⁡ ( n t ⋅ ( 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋) − 1 − n t ⋅ ( ⌊ n ⌋ + 1), 0) ​ 𝑑 t) =\Theta\left(b+\int_{2}^{b}\max\left(\frac{n}{t\cdot\left(1+b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}\right)}-1-\frac{n}{t\cdot({\left\lfloor\sqrt{n}\right\rfloor}+1)},0\right)dt\right) |  |

Let

 | U ​ = def ​ n ⋅ ⌊ n ⌋ − b ⋅ ⌊ ⌊ n ⌋ b ⌋ ( 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋) ​ ( ⌊ n ⌋ + 1). U\overset{\mathrm{def}}{=}n\cdot\frac{{\left\lfloor\sqrt{n}\right\rfloor}-b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}}{\left(1+b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}\right)\left({\left\lfloor\sqrt{n}\right\rfloor}+1\right)}. |  |

Then

 | = Θ ⁡ ( b + ∫ 2 b max ⁡ ( U t − 1, 0) ​ 𝑑 t) =\Theta\left(b+\int_{2}^{b}\max\left(\frac{U}{t}-1,0\right)dt\right) |  |

 | < Θ ⁡ ( b + ∫ 2 b max ⁡ ( U t, 0) ​ 𝑑 t) <\Theta\left(b+\int_{2}^{b}\max\left(\frac{U}{t},0\right)dt\right) |  |

 | < Θ ⁡ ( b + U ​ ln ⁡ ( U)). <\Theta\left(b+U\ln(U)\right). |  |

By Lemma 13, this can be weakened to

 | = O ⁡ ( b + n ​ ln ⁡ ( n)). =O(b+\sqrt{n}\ln(n)). |  |

Recall that we are in the process of estimating the time devoted to line 13. We have separated out the first and last batches for special treatment, and found them to consume

 | Θ ⁡ ( n 2 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 1 / 3) + O ⁡ ( b + n ​ ln ⁡ ( n)) \Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}\right)+O(b+\sqrt{n}\ln(n)) |  |

 | = Θ ⁡ ( n 2 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 1 / 3) =\Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}\right) |  | (6) |

time. We now turn our attention to those batches in which b | x b\mid x and x ≠ b x\neq b. For those batches, we have A = 1 + x − b A=1+x-b, so the time devoted to those batches is

 | ∑ 2 ​ b ≤ x ≤ n b | x ∑ t = 1 b ( 1 + max ⁡ ( min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ ( 1 + x − b) ⌋) − ( 1 + ⌊ n t ⋅ ( x + 1) ⌋), 0)). \sum_{\begin{subarray}{c}2b\leq x\leq\sqrt{n}\\ b\mid x\end{subarray}}\;\sum_{t=1}^{b}\left(1+\max\left(\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\frac{n}{t\cdot(1+x-b)}\right\rfloor}\right)-\left(1+{\left\lfloor\frac{n}{t\cdot(x+1)}\right\rfloor}\right),0\right)\right). |  |

By Lemma 14, this is

 | = Θ ⁡ ( a ⋅ ln ⁡ ( n 2 ​ a − 3)). =\Theta\left(a\cdot\ln(n^{2}a^{-3})\right). |  |

With a = Θ ⁡ ( ( n / ln ⁡ ( ln ⁡ ( n))) 2 / 3) a=\Theta\left((n/\ln(\ln(n)))^{2/3}\right), this works out to

 | = Θ ⁡ ( a ⋅ ln ⁡ ( ln ⁡ ( ln ⁡ ( n)))) =\Theta\left(a\cdot\ln(\ln(\ln(n)))\right) |  |

 | = Θ ( n 2 / 3 ⋅ ( ln ( ln ( n))) − 2 / 3 ⋅ ln ( ln ( ln ( n)))). =\Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{-2/3}\cdot\ln(\ln(\ln(n)))\right). |  | (7) |

From ( 6) and ( 7), we see that, with a = Θ ⁡ ( ( n / ln ⁡ ( ln ⁡ ( n))) 2 / 3) a=\Theta((n/\ln(\ln(n)))^{2/3}), the total time consumed in handling line 13 is

 | Θ ( n 2 / 3 ⋅ ( ln ( ln ( n))) 1 / 3) + Θ ( n 2 / 3 ⋅ ( ln ( ln ( n))) − 2 / 3 ⋅ ln ( ln ( ln ( n)))) \Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}\right)+\Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{-2/3}\cdot\ln(\ln(\ln(n)))\right) |  |

 | = Θ ⁡ ( n 2 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 1 / 3), =\Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}\right), |  |

as desired. ∎

###### 5.

Line 13 consumes Θ ⁡ ( n ​ ln ⁡ ( b)) \Theta\left(\sqrt{n}\ln(b)\right) time.

On each iteration through phase 2 in which line 13 gets hit, it gets hit

 | ∑ y = 1 b f ⁡ ( t, y) \sum_{y=1}^{b}f(t,y) |  |

times, where f ⁡ ( t, y) f(t,y) is the number of integers t t that satisfy ( 4).

We need to determine which values of A A and B B happen. The k k th value of x x such that M ⁡ ( x) M(x) gets saved during phase 2 is approximately

 | n n − k. \frac{n}{\sqrt{n}-k}. |  |

We accumulate batches of size b b, so a batch will be processed when k | b k\mid b; the first batch has k = b k=b and the last batch will have k ≈ n − n 3 k\approx\sqrt{n}-\sqrt[3]{n}. The j j th batch will then have

 | A ≈ n − b ⋅ ( j − 1) and B ≈ n − b ​ j. A\approx\sqrt{n}-b\cdot(j-1)\qquad\text{and}\qquad B\approx\sqrt{n}-bj. |  |

When processing the j j th batch, the bounds on t t are therefore approximately

 | 2 ≤ t ≤ n / y and n < n t ​ y and n − b ​ j ≤ t ​ y ≤ n − b ⋅ ( j − 1) 2\leq t\leq\sqrt{n/y}\quad\text{and}\quad\sqrt{n}<\frac{n}{ty}\quad\text{and}\quad\sqrt{n}-bj\leq ty\leq\sqrt{n}-b\cdot(j-1) |  |

 | 2 ≤ t ≤ n y and t < n y and n − b ​ j y ≤ t ≤ n − b ​ j y + b y. 2\leq t\leq\sqrt{\frac{n}{y}}\quad\text{and}\quad t<\frac{\sqrt{n}}{y}\quad\text{and}\quad\frac{\sqrt{n}-bj}{y}\leq t\leq\frac{\sqrt{n}-bj}{y}+\frac{b}{y}. |  |

The second condition and the upper side of the first condition are both weaker than the upper side of the third condition.

 | 2 ≤ t and n − b ​ j y ≤ t ≤ n − b ​ j y + b y 2\leq t\quad\text{and}\quad\frac{\sqrt{n}-bj}{y}\leq t\leq\frac{\sqrt{n}-bj}{y}+\frac{b}{y} |  |

Therefore

 | f ⁡ ( t, y) ≈ n − b ​ j y + b y − max ⁡ ( 2, n − b ​ j y), f(t,y)\approx\frac{\sqrt{n}-bj}{y}+\frac{b}{y}-\max\left(2,\frac{\sqrt{n}-bj}{y}\right), |  |

so on an iteration through phase 2 in which line 13 gets hit, it gets hit

 | Θ ⁡ ( ∑ y = 1 b ( n − b ​ j y + b y − max ⁡ ( 2, n − b ​ j y))) = Θ ⁡ ( ∑ y = 1 b b y) = Θ ⁡ ( b ​ ln ⁡ ( b)) \Theta\left(\sum_{y=1}^{b}\left(\frac{\sqrt{n}-bj}{y}+\frac{b}{y}-\max\left(2,\frac{\sqrt{n}-bj}{y}\right)\right)\right)=\Theta\left(\sum_{y=1}^{b}\frac{b}{y}\right)=\Theta\left(b\ln(b)\right) |  |

times. There are Θ ⁡ ( n − n 3) \Theta(\sqrt{n}-\sqrt[3]{n}) values of x x such that M ⁡ ( x) M(x) gets saved during phase 2; since each batch has size b b, there are

 | Θ ⁡ ( n − n 3 b) \Theta\left(\frac{\sqrt{n}-\sqrt[3]{n}}{b}\right) |  |

batches. The total time devoted to line 13 across all iterations through phase 2 is therefore

 | Θ ⁡ ( b ​ ln ⁡ ( b)) ⋅ Θ ⁡ ( n − n 3 b) \Theta\left(b\ln(b)\right)\cdot\Theta\left(\frac{\sqrt{n}-\sqrt[3]{n}}{b}\right) |  |

 | = Θ ⁡ ( n ​ ln ⁡ ( b)), =\Theta\left(\sqrt{n}\ln(b)\right), |  |

as desired. ∎

###### 6.

Lines 13 – 13 consume Θ ⁡ ( b ​ ln ⁡ ( b)) \Theta(b\ln(b)) time.

These lines get hit

 | Θ ⁡ ( ∑ y = 1 b n / y n / ( b + 1)) = Θ ⁡ ( ∑ y = 1 b b + 1 y) = Θ ⁡ ( b ​ ln ⁡ ( b)) \Theta\left(\sum_{y=1}^{b}\frac{n/y}{n/(b+1)}\right)=\Theta\left(\sum_{y=1}^{b}\frac{b+1}{y}\right)=\Theta\left(b\ln(b)\right) |  |

times. ∎

###### 7.

With an optimal parameter selection of

 | a = Θ ⁡ ( ( n ln ⁡ ( ln ⁡ ( n))) 2 / 3), a=\Theta\left(\left(\frac{n}{\ln(\ln(n))}\right)^{2/3}\right), |  |

Algorithm 13 computes Φ ⁡ ( n) \Phi(n) in Θ ⁡ ( n 1 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 2 / 3) \Theta\left(n^{1/3}\cdot(\ln(\ln(n)))^{2/3}\right) space and Θ ⁡ ( n 2 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 1 / 3) \Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}\right) time.

The correctness of the algorithm is evident by its development, and the space complexity follows by inspection.

For the time complexity, Lemmas 1, 2, and 3 prove that the minimum possible time for a subsection of the algorithm is Θ ⁡ ( n 2 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 1 / 3) \Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}\right) and that this is obtained by selecting a = Θ ⁡ ( ( n / ln ⁡ ( ln ⁡ ( n))) 2 / 3) a=\Theta\left((n/\ln(\ln(n)))^{2/3}\right), while Lemmas 4, 5, and 6 establish that, with this parmeter selection, the rest of the algorithm does not exceed this time complexity. ∎

## 5 Computational results

The data in Table 1 was procured by running totientsum.py under PyPy3 on a computer with an AMD Ryzen 9 7950X CPU and 128 GB of RAM. The times are wall-clock times; the space requirements are maximum resident-set sizes reported by the command /usr/bin/time -v.

n n | Φ ⁡ ( 10 n) \Phi(10^{n}) [A064018][4] ( n n) | Time (s) | Memory |

Phase 1 | Phase 2 | Total | (kb) |

13 | 30396355092702898919527444 | 5 | 8 | 13 | 95612 |

14 | 3039635509270144893910357854 | 22 | 33 | 56 | 122480 |

15 | 303963550927013509478708835152 | 96 | 154 | 250 | 193868 |

16 | 30396355092701332166351822199504 | 459 | 754 | 1214 | 331492 |

17 | 3039635509270133156701800820366346 | 2114 | 3803 | 5916 | 712492 |

18 | 303963550927013314319686824781290348 | 10135 | 18691 | 28826 | 1695468 |

19 | 30396355092701331435065976498046398788 | 614160 | 162208 | 776388 | 6586924 |

Table 1: Computation of some values of Φ \Phi.

The values of Φ ⁡ ( 10 n) \Phi(10^{n}) for n ∈ { 13, …, 18 } n\in{\left\{13,\ldots,18\right\}} were already known; the values computed here match those at [https://oeis.org/A064018/b064018.txt][5].

The computation of Φ ⁡ ( 10 19) \Phi(10^{19}) is new. Based on the algorithm’s space- and time-complexities, one would expect the computation of Φ ⁡ ( 10 19) \Phi(10^{19}) to take about 160,000 seconds and occupy about 3.6 GB. The reason for the deviation from this expectation is presumably that 10 18 10^{18} fits in a single 64-bit machine word while 10 19 10^{19} does not. To guard against computer glitches, the computation was run twice; the results matched.

## 6 Supporting lemmas

###### 8.

Let n n and y y be integers such that 1 ≤ y ≤ n 1\leq y\leq\sqrt{n}. Then

 | n y ≥ ⌊ n / y ⌋ ⌊ n ⌋ + 1. \sqrt{\frac{n}{y}}\geq\frac{{\left\lfloor n/y\right\rfloor}}{{\left\lfloor\sqrt{n}\right\rfloor}+1}. |  |

We begin with ⌊ n ⌋ + 1 ≥ n {\left\lfloor\sqrt{n}\right\rfloor}+1\geq\sqrt{n}. We can then weaken this to

 | ⌊ n ⌋ + 1 ≥ n y. {\left\lfloor\sqrt{n}\right\rfloor}+1\geq\sqrt{\frac{n}{y}}. |  |

Multiplying by n / y / ( ⌊ n ⌋ + 1) \sqrt{n/y}/({\left\lfloor\sqrt{n}\right\rfloor}+1) yields

 | n y ≥ n / y ⌊ n ⌋ + 1, \sqrt{\frac{n}{y}}\geq\frac{n/y}{{\left\lfloor\sqrt{n}\right\rfloor}+1}, |  |

which we can weaken to

 | n y ≥ ⌊ n / y ⌋ ⌊ n ⌋ + 1, \sqrt{\frac{n}{y}}\geq\frac{{\left\lfloor n/y\right\rfloor}}{{\left\lfloor\sqrt{n}\right\rfloor}+1}, |  |

as desired. ∎

###### 9.

With b b, n n, x x, and y y as in lines 12 – 12,

 | n b + 1 < ⌊ ⌊ n / y ⌋ x ⌋ ⟹ x ≤ ⌊ n / y ⌋ ⌊ n ⌋ + 1. \frac{n}{b+1}<{\left\lfloor\frac{{\left\lfloor n/y\right\rfloor}}{x}\right\rfloor}\implies x\leq\frac{{\left\lfloor n/y\right\rfloor}}{{\left\lfloor\sqrt{n}\right\rfloor}+1}. |  |

The hypothesis can be weakened by dropping the outer floor function, yielding

 | n b + 1 < ⌊ n / y ⌋ x \frac{n}{b+1}<\frac{{\left\lfloor n/y\right\rfloor}}{x} |  |

and therefore

 | x ≤ ⌊ n / y ⌋ n / ( b + 1). x\leq\frac{{\left\lfloor n/y\right\rfloor}}{n/(b+1)}. |  |

Since b = Θ ~ ​ ( n 1 / 3) b=\widetilde{\Theta}(n^{1/3}), we have n / ( b + 1) > ⌊ n ⌋ + 1 n/(b+1)>{\left\lfloor\sqrt{n}\right\rfloor}+1, and the conclusion follows immediately. ∎

###### 10.

Suppose that 1 ≤ t ≤ b ≤ n 1 / 3 1\leq t\leq b\leq n^{1/3}. Then for sufficiently large b b and n n,

 | ⌊ n / t ⌋ ≤ 1 + ⌊ n t ⋅ ( b + 1) ⌋. {\left\lfloor\sqrt{n/t}\right\rfloor}\leq 1+{\left\lfloor\frac{n}{t\cdot(b+1)}\right\rfloor}. |  |

Consider the function

 | f ⁡ ( z) = ( 1 + z b + 1) 2 − z. f(z)=\left(1+\frac{z}{b+1}\right)^{2}-z. |  |

Observe that f ⁡ ( b 2) f(b^{2}), f ′ ​ ( b 2) f^{\prime}(b^{2}), and f ′′ f^{\prime\prime} are all positive. Therefore, if z ≥ b 2 z\geq b^{2}, then f ⁡ ( z) ≥ 0 f(z)\geq 0.

Now consider f ⁡ ( n / t) f(n/t). From the hypotheses of this lemma, we have n / t ≥ b 2 n/t\geq b^{2}. Therefore,

 | 0 ≤ f ⁡ ( n / t) = ( 1 + n / t b + 1) 2 − n t 0\leq f(n/t)=\left(1+\frac{n/t}{b+1}\right)^{2}-\frac{n}{t} |  |

 | n t ≤ ( 1 + n t ⋅ ( b + 1)) 2 \frac{n}{t}\leq\left(1+\frac{n}{t\cdot(b+1)}\right)^{2} |  |

 | n / t ≤ 1 + n t ⋅ ( b + 1). \sqrt{n/t}\leq 1+\frac{n}{t\cdot(b+1)}. |  |

Applying the floor function to both sides then yields the desired result. ∎

###### 11.

lim u → ∞ u 3 ⋅ ( 1 2 − 1 u − 1 4 − 1 u − 1 u 2) = 2 \displaystyle\lim_{u\rightarrow\infty}u^{3}\cdot\left(\frac{1}{2}-\frac{1}{u}-\sqrt{\frac{1}{4}-\frac{1}{u}}-\frac{1}{u^{2}}\right)=2.

Make the substitution u = 1 / x u=1/x to obtain

 | lim x → 0 + x − 3 ⋅ ( 1 2 − x − 1 4 − x − x 2) \lim_{x\rightarrow 0^{+}}x^{-3}\cdot\left(\frac{1}{2}-x-\sqrt{\frac{1}{4}-x}-x^{2}\right) |  |

 | = lim x → 0 + 1 − 2 ​ x − ( 1 − 4 ​ x) 1 / 2 − 2 ​ x 2 2 ​ x 3. =\lim_{x\rightarrow 0^{+}}\frac{1-2x-(1-4x)^{1/2}-2x^{2}}{2x^{3}}. |  |

L’Hôpital’s rule yields

 | = lim x → 0 + 0 − 2 − ( 1 / 2) ( 1 − 4 x) − 1 / 2 ( − 4) − 4 x 6 ​ x 2 =\lim_{x\rightarrow 0^{+}}\frac{0-2-(1/2)(1-4x)^{-1/2}(-4)-4x}{6x^{2}} |  |

 | = lim x → 0 + − 2 + 2 ( 1 − 4 x) − 1 / 2 − 4 x 6 ​ x 2. =\lim_{x\rightarrow 0^{+}}\frac{-2+2(1-4x)^{-1/2}-4x}{6x^{2}}. |  |

L’Hôpital’s rule yields

 | = lim x → 0 + 0 + 2 ( − 1 / 2) ( 1 − 4 x) − 3 / 2 ( − 4) − 4 12 ​ x =\lim_{x\rightarrow 0^{+}}\frac{0+2(-1/2)(1-4x)^{-3/2}(-4)-4}{12x} |  |

 | = lim x → 0 + 4 ( 1 − 4 x) − 3 / 2 − 4 12 ​ x. =\lim_{x\rightarrow 0^{+}}\frac{4(1-4x)^{-3/2}-4}{12x}. |  |

L’Hôpital’s rule yields

 | = lim x → 0 + 4 ( − 3 / 2) ( 1 − 4 x) − 5 / 2 ( − 4) − 0 12 =\lim_{x\rightarrow 0^{+}}\frac{4(-3/2)(1-4x)^{-5/2}(-4)-0}{12} |  |

 | = lim x → 0 + 24 ( 1 − 4 x) − 5 / 2 12 =\lim_{x\rightarrow 0^{+}}\frac{24(1-4x)^{-5/2}}{12} |  |

 | = 2, =2, |  |

as desired. ∎

###### 12.

Suppose that 2 ≤ t 2\leq t and b = o ⁡ ( n) b=o(\sqrt{n}). Then for sufficiently large n n,

 | ⌊ n t ⋅ ( 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋) ⌋ ≤ ⌊ n / t ⌋. {\left\lfloor\frac{n}{t\cdot\left(1+b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}\right)}\right\rfloor}\leq{\left\lfloor\sqrt{n/t}\right\rfloor}. |  |

We begin with

 | n 2 < ⌊ n ⌋ − b + 1 < ⌊ n ⌋ − ( ⌊ n ⌋ mod b) + 1 = b ⋅ ⌊ ⌊ n ⌋ b ⌋ + 1. \sqrt{\frac{n}{2}}<{\left\lfloor\sqrt{n}\right\rfloor}-b+1<{\left\lfloor\sqrt{n}\right\rfloor}-({\left\lfloor\sqrt{n}\right\rfloor}\bmod b)+1=b\cdot{\left\lfloor\frac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}+1. |  |

The first inequality is true for sufficiently large n n because b = o ⁡ ( n 1 / 2) b=o(n^{1/2}); the rest is arithmetic. By hypothesis, t ≥ 2 t\geq 2, so we can weaken this to

 | n t < 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋ \sqrt{\frac{n}{t}}<1+b\cdot{\left\lfloor\frac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor} |  |

and therefore

 | n / t 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋ < n / t. \frac{n/t}{1+b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}}<\sqrt{n/t}. |  |

Applying the floor function to both sides then yields the desired result. ∎

###### 13.

U ≤ 2 ​ n U\leq 2\sqrt{n}.

Since b = o ⁡ ( n) b=o(\sqrt{n}), we have for sufficiently large n n

 | n ≤ 2 ⋅ ( 1 + ⌊ n ⌋) 2 − 2 ​ b ⋅ ( ⌊ n ⌋ + 1) n\leq 2\cdot\left(1+{\left\lfloor\sqrt{n}\right\rfloor}\right)^{2}-2b\cdot\left({\left\lfloor\sqrt{n}\right\rfloor}+1\right) |  |

 | = 2 ⋅ ( 1 + ⌊ n ⌋ − b) ​ ( ⌊ n ⌋ + 1) =2\cdot\left(1+{\left\lfloor\sqrt{n}\right\rfloor}-b\right)\left({\left\lfloor\sqrt{n}\right\rfloor}+1\right) |  |

 | ≤ 2 ⋅ ( 1 + ⌊ n ⌋ − ( ⌊ n ⌋ mod b)) ​ ( ⌊ n ⌋ + 1) \leq 2\cdot\left(1+{\left\lfloor\sqrt{n}\right\rfloor}-({\left\lfloor\sqrt{n}\right\rfloor}\bmod b)\right)\left({\left\lfloor\sqrt{n}\right\rfloor}+1\right) |  |

 | = 2 ⋅ ( 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋) ​ ( ⌊ n ⌋ + 1), =2\cdot\left(1+b\cdot{\left\lfloor\frac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}\right)\left({\left\lfloor\sqrt{n}\right\rfloor}+1\right), |  |

which is equivalent to

 | 2 ​ n ≥ n ⋅ n ( 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋) ​ ( ⌊ n ⌋ + 1) 2\sqrt{n}\geq n\cdot\frac{\sqrt{n}}{\left(1+b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}\right)\left({\left\lfloor\sqrt{n}\right\rfloor}+1\right)} |  |

 | ≥ n ⋅ ⌊ n ⌋ ( 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋) ​ ( ⌊ n ⌋ + 1) \geq n\cdot\frac{{\left\lfloor\sqrt{n}\right\rfloor}}{\left(1+b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}\right)\left({\left\lfloor\sqrt{n}\right\rfloor}+1\right)} |  |

 | ≥ n ⋅ ⌊ n ⌋ − b ⋅ ⌊ ⌊ n ⌋ b ⌋ ( 1 + b ⋅ ⌊ ⌊ n ⌋ b ⌋) ​ ( ⌊ n ⌋ + 1), \geq n\cdot\frac{{\left\lfloor\sqrt{n}\right\rfloor}-b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}}{\left(1+b\cdot{\left\lfloor\dfrac{{\left\lfloor\sqrt{n}\right\rfloor}}{b}\right\rfloor}\right)\left({\left\lfloor\sqrt{n}\right\rfloor}+1\right)}, |  |

which is the desired result. ∎

###### 14.

 | ∑ 2 ​ b ≤ x ≤ n b | x ∑ t = 1 b ( 1 + max ⁡ ( min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ ( 1 + x − b) ⌋) − ( 1 + ⌊ n t ⋅ ( x + 1) ⌋), 0)) \sum_{\begin{subarray}{c}2b\leq x\leq\sqrt{n}\\ b\mid x\end{subarray}}\;\sum_{t=1}^{b}\left(1+\max\left(\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\frac{n}{t\cdot(1+x-b)}\right\rfloor}\right)-\left(1+{\left\lfloor\frac{n}{t\cdot(x+1)}\right\rfloor}\right),0\right)\right) |  |

 | = Θ ⁡ ( a ⋅ ln ⁡ ( n 2 ​ a − 3)). =\Theta\left(a\cdot\ln(n^{2}a^{-3})\right). |  |

Reindexing the outer sum yields

 | ∑ χ = 2 n / b ∑ t = 1 b ( 1 + max ⁡ ( min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ ( 1 + b ​ χ − b) ⌋) − 1 − ⌊ n t ⋅ ( b ​ χ + 1) ⌋, 0)) \sum_{\chi=2}^{\sqrt{n}/b}\sum_{t=1}^{b}\left(1+\max\left(\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\frac{n}{t\cdot(1+b\chi-b)}\right\rfloor}\right)-1-{\left\lfloor\frac{n}{t\cdot(b\chi+1)}\right\rfloor},0\right)\right) |  |

 | = n − 1 + ∑ χ = 2 n / b ∑ t = 1 b max ⁡ ( min ⁡ ( ⌊ n / t ⌋, ⌊ n t ⋅ ( 1 + b ​ χ − b) ⌋) − 1 − ⌊ n t ⋅ ( b ​ χ + 1) ⌋, 0). =\sqrt{n}-1+\sum_{\chi=2}^{\sqrt{n}/b}\sum_{t=1}^{b}\max\left(\min\left({\left\lfloor\sqrt{n/t}\right\rfloor},{\left\lfloor\frac{n}{t\cdot(1+b\chi-b)}\right\rfloor}\right)-1-{\left\lfloor\frac{n}{t\cdot(b\chi+1)}\right\rfloor},0\right). |  |

The sum will turn out to be Θ ~ ​ ( a) \widetilde{\Theta}(a), so the n − 1 \sqrt{n}-1 is neglectably small.

 | = Θ ⁡ ( ∫ 2 n / b ∫ 1 b max ⁡ ( min ⁡ ( n / t, n t ⋅ ( 1 + b ​ χ − b)) − 1 − n t ⋅ ( b ​ χ + 1), 0) ​ 𝑑 t ​ 𝑑 χ) =\Theta\left(\int_{2}^{\sqrt{n}/b}\int_{1}^{b}\max\left(\min\left(\sqrt{n/t},\frac{n}{t\cdot(1+b\chi-b)}\right)-1-\frac{n}{t\cdot(b\chi+1)},0\right)dt\;d\chi\right) |  |

Let u = b ​ χ + 1 u=b\chi+1.

 | = Θ ⁡ ( 1 b ⋅ ∫ 1 + 2 ​ b 1 + n ∫ 1 b max ⁡ ( min ⁡ ( n / t, n t ⋅ ( u − b)) − 1 − n t ​ u, 0) ​ 𝑑 t ​ 𝑑 u) =\Theta\left(\frac{1}{b}\cdot\int_{1+2b}^{1+\sqrt{n}}\int_{1}^{b}\max\left(\min\left(\sqrt{n/t},\frac{n}{t\cdot(u-b)}\right)-1-\frac{n}{tu},0\right)dt\;du\right) |  |

Let T ​ = def ​ n ⋅ ( u − b) − 2 T\overset{\mathrm{def}}{=}n\cdot(u-b)^{-2}. This is the crossover point in the min \min function. For lesser t t, the first argument prevails, and the integral becomes

 | = Θ ⁡ ( 1 b ⋅ ∫ 1 + 2 ​ b 1 + n ( ∫ T b max ⁡ ( b ​ n t ​ u ⋅ ( u − b) − 1, 0) ​ 𝑑 t + ∫ 1 T max ⁡ ( n / t − 1 − n t ​ u, 0) ​ 𝑑 t) ​ 𝑑 u). =\Theta\left(\frac{1}{b}\cdot\int_{1+2b}^{1+\sqrt{n}}\left(\int_{T}^{b}\max\left(\frac{bn}{tu\cdot(u-b)}-1,0\right)dt+\int_{1}^{T}\max\left(\sqrt{n/t}-1-\frac{n}{tu},0\right)dt\right)du\right). |  |

By Lemma 15, in the first inner integral, max \max function’s first argument prevails throughout the interval of integration.

 | = Θ ⁡ ( 1 b ⋅ ∫ 1 + 2 ​ b 1 + n ( ∫ T b ( b ​ n t ​ u ⋅ ( u − b) − 1) ​ 𝑑 t + ∫ 1 T max ⁡ ( n / t − 1 − n t ​ u, 0) ​ 𝑑 t) ​ 𝑑 u) =\Theta\left(\frac{1}{b}\cdot\int_{1+2b}^{1+\sqrt{n}}\left(\int_{T}^{b}\left(\frac{bn}{tu\cdot(u-b)}-1\right)dt+\int_{1}^{T}\max\left(\sqrt{n/t}-1-\frac{n}{tu},0\right)dt\right)du\right) |  |

Let S ​ = def ​ n 2 − n u − ( n 2) 2 − n 2 u \displaystyle S\overset{\mathrm{def}}{=}\frac{n}{2}-\frac{n}{u}-\sqrt{\left(\frac{n}{2}\right)^{2}-\frac{n^{2}}{u}}. This is the crossover point in the remaining max \max function; the first argument prevails for t > S t>S.

 | = Θ ⁡ ( 1 b ⋅ ∫ 1 + 2 ​ b 1 + n ( ∫ T b ( b ​ n t ​ u ⋅ ( u − b) − 1) ​ 𝑑 t + ∫ S T ( n / t − 1 − n t ​ u) ​ 𝑑 t) ​ 𝑑 u) =\Theta\left(\frac{1}{b}\cdot\int_{1+2b}^{1+\sqrt{n}}\left(\int_{T}^{b}\left(\frac{bn}{tu\cdot(u-b)}-1\right)dt+\int_{S}^{T}\left(\sqrt{n/t}-1-\frac{n}{tu}\right)dt\right)du\right) |  |

 | = Θ ⁡ ( 1 b ⋅ ∫ 1 + 2 ​ b 1 + n ( b ​ n ​ ln ⁡ ( b / T) u ⋅ ( u − b) − ( b − T) + 2 ​ n ​ ( T 1 / 2 − S 1 / 2) − ( T − S) − n ​ ln ⁡ ( T / S) u) ​ 𝑑 u) =\Theta\left(\frac{1}{b}\cdot\int_{1+2b}^{1+\sqrt{n}}\left(\frac{bn\ln(b/T)}{u\cdot(u-b)}-(b-T)+2\sqrt{n}(T^{1/2}-S^{1/2})-(T-S)-\frac{n\ln(T/S)}{u}\right)du\right) |  |

Cancelling and substituting out the T T s, and factoring out an n n, yields

 | = Θ ⁡ ( n b ⋅ ∫ 1 + 2 ​ b 1 + n ( b ​ ln ⁡ ( b n ​ ( u − b) 2) ( u − b) ⋅ u − b n + 2 u − b − 2 ​ S n + S n + ln ⁡ ( S n ​ ( u − b) 2) u) ​ 𝑑 u). =\Theta\left(\frac{n}{b}\cdot\int_{1+2b}^{1+\sqrt{n}}\left(\frac{b\ln\left(\dfrac{b}{n}(u-b)^{2}\right)}{(u-b)\cdot u}-\frac{b}{n}+\frac{2}{u-b}-2\sqrt{\frac{S}{n}}+\frac{S}{n}+\frac{\ln\left(\dfrac{S}{n}(u-b)^{2}\right)}{u}\right)du\right). |  |

We now pull the b / n b/n term out, and also substitute a = n / b a=n/b.

 | = Θ ⁡ ( 2 ​ b − n + a ⋅ ∫ 1 + 2 ​ b 1 + n ( b ​ ln ⁡ ( ( u − b) 2 a) ( u − b) ⋅ u + 2 u − b − 2 ​ S n + S n + ln ⁡ ( S n ​ ( u − b) 2) u) ​ 𝑑 u) =\Theta\left(2b-\sqrt{n}+a\cdot\int_{1+2b}^{1+\sqrt{n}}\left(\frac{b\ln\left(\dfrac{(u-b)^{2}}{a}\right)}{(u-b)\cdot u}+\frac{2}{u-b}-2\sqrt{\frac{S}{n}}+\frac{S}{n}+\frac{\ln\left(\dfrac{S}{n}(u-b)^{2}\right)}{u}\right)du\right) |  |

The expression will turn out to be Θ ~ ​ ( a) \widetilde{\Theta}(a), so the 2 ​ b − n 2b-\sqrt{n} is neglectably small.

 | = a ⋅ Θ ⁡ ( ∫ 1 + 2 ​ b 1 + n ( b ​ ln ⁡ ( ( u − b) 2 a) ( u − b) ⋅ u + 2 u − b − 2 ​ S n + S n + ln ⁡ ( S n ​ ( u − b) 2) u) ​ 𝑑 u) =a\cdot\Theta\left(\int_{1+2b}^{1+\sqrt{n}}\left(\frac{b\ln\left(\dfrac{(u-b)^{2}}{a}\right)}{(u-b)\cdot u}+\frac{2}{u-b}-2\sqrt{\frac{S}{n}}+\frac{S}{n}+\frac{\ln\left(\dfrac{S}{n}(u-b)^{2}\right)}{u}\right)du\right) |  |

Observe that S n = S n + 1 u \displaystyle\sqrt{\frac{S}{n}}=\frac{S}{n}+\frac{1}{u}.

 | = a ⋅ Θ ⁡ ( ∫ 1 + 2 ​ b 1 + n ( b ​ ln ⁡ ( ( u − b) 2 a) ( u − b) ⋅ u + 2 u − b − 2 u − S n + ln ⁡ ( S n ​ ( u − b) 2) u) ​ 𝑑 u) =a\cdot\Theta\left(\int_{1+2b}^{1+\sqrt{n}}\left(\frac{b\ln\left(\dfrac{(u-b)^{2}}{a}\right)}{(u-b)\cdot u}+\frac{2}{u-b}-\frac{2}{u}-\frac{S}{n}+\frac{\ln\left(\dfrac{S}{n}(u-b)^{2}\right)}{u}\right)du\right) |  |

 | = a ⋅ Θ ⁡ ( ∫ 1 + 2 ​ b 1 + n ( b ​ ln ⁡ ( ( u − b) 2 a) ( u − b) ⋅ u + 2 ​ b u ⋅ ( u − b) − S n + ln ⁡ ( ( u − b) 2 u 2) u + ln ⁡ ( S ​ u 2 n) u) ​ 𝑑 u) =a\cdot\Theta\left(\int_{1+2b}^{1+\sqrt{n}}\left(\frac{b\ln\left(\dfrac{(u-b)^{2}}{a}\right)}{(u-b)\cdot u}+\frac{2b}{u\cdot(u-b)}-\frac{S}{n}+\frac{\ln\left(\dfrac{(u-b)^{2}}{u^{2}}\right)}{u}+\frac{\ln\left(\dfrac{Su^{2}}{n}\right)}{u}\right)du\right) |  |

We now invoke Lemmas 16 and 17 to approximately integrate the S S -terms, yielding

 | = a ⋅ Θ ⁡ ( ∫ 1 + 2 ​ b 1 + n ( b ​ ln ⁡ ( ( u − b) 2 a) ( u − b) ⋅ u + 2 ​ b u ⋅ ( u − b) + ln ⁡ ( ( u − b) 2 u 2) u) ​ 𝑑 u + O ⁡ ( 1 / b)). =a\cdot\Theta\left(\int_{1+2b}^{1+\sqrt{n}}\left(\frac{b\ln\left(\dfrac{(u-b)^{2}}{a}\right)}{(u-b)\cdot u}+\frac{2b}{u\cdot(u-b)}+\frac{\ln\left(\dfrac{(u-b)^{2}}{u^{2}}\right)}{u}\right)du+O(1/b)\right). |  |

The integral will turn out to be Θ ~ ​ ( 1) \widetilde{\Theta}(1), so the O ⁡ ( 1 / b) O(1/b) is neglectably small.

 | = a ⋅ Θ ⁡ ( ∫ 1 + 2 ​ b 1 + n ( b ​ ln ⁡ ( ( u − b) 2 a) ( u − b) ⋅ u + 2 ​ b u ⋅ ( u − b) + ln ⁡ ( ( u − b) 2 u 2) u) ​ 𝑑 u) =a\cdot\Theta\left(\int_{1+2b}^{1+\sqrt{n}}\left(\frac{b\ln\left(\dfrac{(u-b)^{2}}{a}\right)}{(u-b)\cdot u}+\frac{2b}{u\cdot(u-b)}+\frac{\ln\left(\dfrac{(u-b)^{2}}{u^{2}}\right)}{u}\right)du\right) |  |

Now we put the integrand on a common denominator and use the logarithm’s quotient rule to obtain

 | = a ⋅ Θ ⁡ ( ∫ 1 + 2 ​ b 1 + n ( 2 ​ b ​ ln ⁡ ( u − b) − b ​ ln ⁡ ( a) + 2 ​ b + 2 ​ ( u − b) ​ ln ⁡ ( u − b) − 2 ​ ( u − b) ​ ln ⁡ ( u) ( u − b) ⋅ u) ​ 𝑑 u). =a\cdot\Theta\left(\int_{1+2b}^{1+\sqrt{n}}\left(\frac{2b\ln(u-b)-b\ln(a)+2b+2(u-b)\ln(u-b)-2(u-b)\ln(u)}{(u-b)\cdot u}\right)du\right). |  |

Some terms in the numerator cancel.

 | = a ⋅ Θ ⁡ ( ∫ 1 + 2 ​ b 1 + n ( − b ​ ln ⁡ ( a) + 2 ​ b + 2 ​ u ​ ln ⁡ ( u − b) − 2 ​ ( u − b) ​ ln ⁡ ( u) ( u − b) ⋅ u) ​ 𝑑 u) =a\cdot\Theta\left(\int_{1+2b}^{1+\sqrt{n}}\left(\frac{-b\ln(a)+2b+2u\ln(u-b)-2(u-b)\ln(u)}{(u-b)\cdot u}\right)du\right) |  |

We now undo the common denominator to find that the integral has become elementary.

 | = a ⋅ Θ ⁡ ( ∫ 1 + 2 ​ b 1 + n ( ( 2 − ln ⁡ ( a)) ​ ( 1 u − b − 1 u) + 2 ​ ln ⁡ ( u − b) u − b − 2 ​ ln ⁡ ( u) u) ​ 𝑑 u) =a\cdot\Theta\left(\int_{1+2b}^{1+\sqrt{n}}\left((2-\ln(a))\left(\frac{1}{u-b}-\frac{1}{u}\right)+\frac{2\ln(u-b)}{u-b}-\frac{2\ln(u)}{u}\right)du\right) |  |

 | = a ⋅ Θ ⁡ ( ( ( 2 − ln ⁡ ( a)) ​ ( ln ⁡ ( | u − b |) − ln ⁡ ( | u |)) + ( ln ⁡ ( u − b)) 2 − ( ln ⁡ ( u)) 2) | u = 1 + 2 ​ b 1 + n) =a\cdot\Theta\left(\left.\left((2-\ln(a))\left(\ln(\left|u-b\right|)-\ln(\left|u\right|)\right)+(\ln(u-b))^{2}-(\ln(u))^{2}\right)\right|_{u=1+2b}^{1+\sqrt{n}}\right) |  |

 | = a ⋅ Θ ⁡ ( ( ln ⁡ ( e 2 ​ a − 1) ​ ln ⁡ ( 1 − b u) + ln ⁡ ( u 2 − b ​ u) ​ ln ⁡ ( 1 − b u)) | u = 1 + 2 ​ b 1 + n) =a\cdot\Theta\left(\left.\left(\ln(e^{2}a^{-1})\ln\left(1-\frac{b}{u}\right)+\ln(u^{2}-bu)\ln\left(1-\frac{b}{u}\right)\right)\right|_{u=1+2b}^{1+\sqrt{n}}\right) |  |

 | = a ⋅ Θ ⁡ ( ( ln ⁡ ( e 2 ​ a − 1 ​ ( u 2 − b ​ u)) ⋅ ln ⁡ ( 1 − b u)) | u = 1 + 2 ​ b 1 + n) =a\cdot\Theta\left(\left.\left(\ln\left(e^{2}a^{-1}(u^{2}-bu)\right)\cdot\ln\left(1-\frac{b}{u}\right)\right)\right|_{u=1+2b}^{1+\sqrt{n}}\right) |  |

 | = a ⋅ Θ ⁡ ( ln ⁡ ( e 2 a ​ ( 1 + n) ​ ( 1 + n − b)) ​ ln ⁡ ( 1 − b 1 + n) − ln ⁡ ( e 2 a ​ ( 2 ​ b 2 + 3 ​ b + 1)) ​ ln ⁡ ( 1 + b 1 + 2 ​ b)) =a\cdot\Theta\left(\ln\left(\frac{e^{2}}{a}(1+\sqrt{n})(1+\sqrt{n}-b)\right)\ln\left(1-\frac{b}{1+\sqrt{n}}\right)-\ln\left(\frac{e^{2}}{a}(2b^{2}+3b+1)\right)\ln\left(\frac{1+b}{1+2b}\right)\right) |  |

 | = a ⋅ Θ ⁡ ( ln ⁡ ( e 2 ​ a − 1 ⋅ Θ ⁡ ( n)) ⋅ ln ⁡ ( 1 − Θ ⁡ ( b n)) + ln ⁡ ( e 2 ​ a − 1 ⋅ Θ ⁡ ( b 2)) ⋅ Θ ⁡ ( ln ⁡ ( 2))) =a\cdot\Theta\left(\ln\left(e^{2}a^{-1}\cdot\Theta(n)\right)\cdot\ln\left(1-\Theta\left(\frac{b}{\sqrt{n}}\right)\right)+\ln\left(e^{2}a^{-1}\cdot\Theta(b^{2})\right)\cdot\Theta(\ln(2))\right) |  |

Since we are working with a = Θ ~ ​ ( n 2 / 3) a=\widetilde{\Theta}(n^{2/3}) and b = Θ ~ ​ ( n 1 / 3) b=\widetilde{\Theta}(n^{1/3}), this becomes

 | = a ⋅ Θ ( ln ( e 2 ⋅ Θ ~ ( n − 2 / 3) ⋅ Θ ( n)) ⋅ ln ( 1 − Θ ~ ( n − 1 / 6)) + ln ( a − 1 ⋅ Θ ( b 2)) ⋅ Θ ( 1)) =a\cdot\Theta\left(\ln\left(e^{2}\cdot\widetilde{\Theta}(n^{-2/3})\cdot\Theta(n)\right)\cdot\ln\left(1-\widetilde{\Theta}(n^{-1/6})\right)+\ln\left(a^{-1}\cdot\Theta(b^{2})\right)\cdot\Theta(1)\right) |  |

 | = a ⋅ Θ ( ln ( e 2 ⋅ Θ ~ ( n 1 / 3)) ⋅ ( − Θ ~ ( n − 1 / 6)) + ln ( a − 1 ⋅ Θ ( b 2)) ⋅ Θ ( 1)) =a\cdot\Theta\left(\ln\left(e^{2}\cdot\widetilde{\Theta}(n^{1/3})\right)\cdot(-\widetilde{\Theta}(n^{-1/6}))+\ln\left(a^{-1}\cdot\Theta(b^{2})\right)\cdot\Theta(1)\right) |  |

 | = a ⋅ Θ ⁡ ( o ⁡ ( 1) + ln ⁡ ( Θ ⁡ ( 1) ⋅ b 2 / a) ⋅ Θ ⁡ ( 1)) =a\cdot\Theta\left(o(1)+\ln\left(\Theta(1)\cdot b^{2}/a\right)\cdot\Theta(1)\right) |  |

 | = a ⋅ Θ ⁡ ( o ⁡ ( 1) + ln ⁡ ( Θ ⁡ ( 1)) ⋅ Θ ⁡ ( 1) + ln ⁡ ( b 2 / a) ⋅ Θ ⁡ ( 1)). =a\cdot\Theta\left(o(1)+\ln(\Theta(1))\cdot\Theta(1)+\ln(b^{2}/a)\cdot\Theta(1)\right). |  |

Since we are working with a = ( n / ln ⁡ ( ln ⁡ ( n))) 2 / 3 a=(n/\ln(\ln(n)))^{2/3} and b = n 1 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 2 / 3 b=n^{1/3}\cdot(\ln(\ln(n)))^{2/3}, ln ⁡ ( b 2 / a) \ln(b^{2}/a) increases without bound. Therefore,

 | = a ⋅ Θ ⁡ ( ln ⁡ ( b 2 / a) ⋅ Θ ⁡ ( 1)) =a\cdot\Theta\left(\ln(b^{2}/a)\cdot\Theta(1)\right) |  |

 | = Θ ⁡ ( a ⋅ ln ⁡ ( n 2 ​ a − 3)), =\Theta\left(a\cdot\ln\left(n^{2}a^{-3}\right)\right), |  |

as desired. ∎

###### 15.

For 1 + b ≤ u ≤ 1 + n 1+b\leq u\leq 1+\sqrt{n} and large n n, b ​ n ( u − b) ⋅ u > b \dfrac{bn}{(u-b)\cdot u}>b.

Since n > u − 1 \sqrt{n}>u-1, we have

 | n > ( u − 1) 2. n>(u-1)^{2}. |  |

For all but the smallest n n, we will have b > 2 b>2; since we are working in the limit of large n n, we can weaken this to

 | n > ( u − 1) 2 − ( b ​ u − 2 ​ u + 1) = u 2 − b ​ u, n>(u-1)^{2}-(bu-2u+1)=u^{2}-bu, |  |

from which the conclusion follows immediately. ∎

###### 16.

∫ 1 + 2 ​ b 1 + n ( 1 u ⋅ ln ⁡ ( u 2 ⋅ S n)) ​ 𝑑 u = O ⁡ ( b − 1) \displaystyle\int_{1+2b}^{1+\sqrt{n}}\left(\frac{1}{u}\cdot\ln\left(u^{2}\cdot\frac{S}{n}\right)\right)du=O(b^{-1}).

Let C k C_{k} be the k k th Catalan number ( [A000108][6]). Observe that

 | S n = ∑ k = 2 ∞ C k − 1 u k, \frac{S}{n}=\sum_{k=2}^{\infty}\frac{C_{k-1}}{u^{k}}, |  |

and therefore S / n > u − 2 S/n>u^{-2}. Then

 | 0 < ∫ 1 + 2 ​ b 1 + n ( 1 u ⋅ ln ⁡ ( u 2 ⋅ S n)) ​ 𝑑 u. 0<\int_{1+2b}^{1+\sqrt{n}}\left(\frac{1}{u}\cdot\ln\left(u^{2}\cdot\frac{S}{n}\right)\right)du. |  |

By Lemma 11, we have u 2 ⋅ S / n = 1 + O ⁡ ( u − 1) u^{2}\cdot S/n=1+O(u^{-1}), so

 | = ∫ 1 + 2 ​ b 1 + n ( 1 u ⋅ ln ⁡ ( 1 + O ⁡ ( u − 1))) ​ 𝑑 u =\int_{1+2b}^{1+\sqrt{n}}\left(\frac{1}{u}\cdot\ln\left(1+O(u^{-1})\right)\right)du |  |

 | = ∫ 1 + 2 ​ b 1 + n ( 1 u ⋅ O ⁡ ( u − 1)) ​ 𝑑 u =\int_{1+2b}^{1+\sqrt{n}}\left(\frac{1}{u}\cdot O(u^{-1})\right)du |  |

 | = ∫ 1 + 2 ​ b 1 + n O ⁡ ( u − 2) ​ 𝑑 u =\int_{1+2b}^{1+\sqrt{n}}O(u^{-2})\;du |  |

 | = − O ⁡ ( u − 1) | u = 1 + 2 ​ b 1 + n =\left.-O(u^{-1})\right|_{u=1+2b}^{1+\sqrt{n}} |  |

 | = O ⁡ ( 1 1 + 2 ​ b) − O ⁡ ( 1 1 + n) =O\left(\frac{1}{1+2b}\right)-O\left(\frac{1}{1+\sqrt{n}}\right) |  |

 | = O ⁡ ( b − 1), =O(b^{-1}), |  |

as desired. ∎

###### 17.

∫ 1 + 2 ​ b 1 + n S n ​ 𝑑 u = O ⁡ ( b − 1) \displaystyle\int_{1+2b}^{1+\sqrt{n}}\frac{S}{n}\;du=O(b^{-1}).

For u > 5 u>5, we have

 | 16 u 2 + 16 u < 4 \frac{16}{u^{2}}+\frac{16}{u}<4 |  |

 | u 2 + 4 + 16 u 2 − 4 ​ u − 8 + 16 u < u 2 − 4 ​ u u^{2}+4+\frac{16}{u^{2}}-4u-8+\frac{16}{u}<u^{2}-4u |  |

 | u − 2 − 4 u < u 2 − 4 ​ u u-2-\frac{4}{u}<\sqrt{u^{2}-4u} |  |

 | u − 2 − u 2 − 4 ​ u < 4 u u-2-\sqrt{u^{2}-4u}<\frac{4}{u} |  |

 | 0 < u − 2 − u 2 − 4 ​ u < 4 u 0<u-2-\sqrt{u^{2}-4u}<\frac{4}{u} |  |

 | 0 < 1 2 − 1 u − 1 4 − 1 u < 2 u 2 0<\frac{1}{2}-\frac{1}{u}-\sqrt{\frac{1}{4}-\frac{1}{u}}<\frac{2}{u^{2}} |  |

 | 0 < S n < 2 u 2. 0<\frac{S}{n}<\frac{2}{u^{2}}. |  |

Integrating then gives the desired result. ∎

## References

- [1] Marc Deléglise and Joöl Rivat “Computing the summation of the Möbius function” In *Experimental Mathematics*5.4, 1996, pp. 291–295 DOI: [10.1080/10586458.1996.10504594][7]
- [2] Haraldés Helfgott and Lola Thompson “Summing μ ⁡ ( n) \mu(n): a faster elementary algorithm” In *Research in Number Theory*9.6, 2023 DOI: [10.1007/s40993-022-00408-8][8]
- [3] Dean Hirsch, Ido Kessler and Uri Mendlovic, Personal communication, 2025
- [4] Dean Hirsch, Ido Kessler and Uri Mendlovic “Computing π ⁡ ( N) \pi(N): An elementary approach in O ~ ​ ( N) \tilde{O}(\sqrt{N}) time” In *Mathematics of Computation*, 2022 DOI: [10.1090/mcom/4039][9]
- [5] Oleksandr Kulkov “Dirichlet convolution. Part 1: Fast prefix sum computations”, 2023 URL: [https://codeforces.com/blog/entry/117635][10]
- [6] Griffin Macris “Summing Multiplicative Functions (Pt. 1)”, 2023 URL: [https://gbroxey.github.io/blog/2023/04/30/mult-sum-1.html][11]

2020 *Mathematics Subject Classification*: Primary 11Y16; Secondary 11-04, 11A25, 11Y55, 11Y70.

*Keywords*: totient, totient summatory function, Dirichlet hyperbola method, computation.

(Concerned with sequences [A002088][12] and [A064018][4].)


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://orcid.org/0000-0002-6000-3735
[4]: https://oeis.org/A064018
[5]: https://oeis.org/A064018/b064018.txt
[6]: https://oeis.org/A000108
[7]: https://dx.doi.org/10.1080/10586458.1996.10504594
[8]: https://dx.doi.org/10.1007/s40993-022-00408-8
[9]: https://dx.doi.org/10.1090/mcom/4039
[10]: https://codeforces.com/blog/entry/117635
[11]: https://gbroxey.github.io/blog/2023/04/30/mult-sum-1.html
[12]: https://oeis.org/A002088
