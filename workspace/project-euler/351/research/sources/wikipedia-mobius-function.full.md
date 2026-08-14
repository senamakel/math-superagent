<!-- source: https://en.wikipedia.org/wiki/M%C3%B6bius_function | converted from HTML -->

Möbius function - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Multiplicative function in number theory

This article is about the number-theoretic Möbius function. For the combinatorial Möbius function, see [incidence algebra][1]. For the [rational functions][2] defined on the [complex numbers][3], see [Möbius transformation][4].

 |

This article includes a list of [general references][5]**but lacks sufficient corresponding [inline citations][6]**. Please help [improve this article][7] by [introducing][8] more precise citations.*( October 2024)**( [Learn how and when to remove this message][9])*

 |

Möbius function

Named after | [August Ferdinand Möbius][10] |

Publication year | 1832 |

Author of publication | [August Ferdinand Möbius][10] |

Number</span>"}]]}'>No. of known terms | infinite |

First terms | 1, −1, −1, 0, −1, 1, −1, 0, 0, 1 |

[OEIS][11] index |

- [A008683][12]
- Möbius (or Moebius) function mu(n). mu(1) = 1; mu(n) = (-1)^k if n is the product of k different primes; otherwise mu(n) = 0.

 |

The **Möbius function μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}]**is a [multiplicative function][13] in [number theory][14] introduced by the German mathematician [August Ferdinand Möbius][10] (also transliterated *Moebius*) in 1832. \\mu(n)</math> occurs implicitly in the works of Euler as early as 1748, but Möbius, in 1832, was the first to investigate its properties systematically\". {{harv|Hardy|Wright|1980|loc=Notes on ch. XVI}}"}},"i":0}}]}'> [i] \\mod p</math>) is <math>\\mu(p-1)</math>, (see [[#Properties and applications]]) but he didn't make further use of the function. In particular, he didn't use Möbius inversion in the ''Disquisitiones''.{{sfn|Gauss|1986|loc=Art. 81}} The ''[[Disquisitiones Arithmeticae]]'' has been translated from Latin into English and German. The German edition includes all of his papers on number theory: all the proofs of quadratic reciprocity, the determination of the sign of the Gauss sum, the investigations into biquadratic reciprocity, and unpublished notes."}},"i":0}}]}'> [ii] [2] It is ubiquitous in elementary and [analytic number theory][15] and most often appears as part of its namesake the [Möbius inversion formula][16]. Following work of [Gian-Carlo Rota][17] in the 1960s, generalizations of the Möbius function were introduced into combinatorics, and are similarly denoted μ ( x) {\displaystyle \mu (x)}[image: {\displaystyle \mu (x)}].

## Definition

[[edit][18]]

The Möbius function is defined by [3]

1.\n\\end{cases}"}}'> 1.\end{cases}}}"> μ ( n) = { 1 if n = 1 ( − 1) k if n is the product of k distinct primes 0 if n is divisible by a square > 1. {\displaystyle \mu (n)={\begin{cases}1&{\text{if }}n=1\\(-1)^{k}&{\text{if }}n{\text{ is the product of }}k{\text{ distinct primes}}\\0&{\text{if }}n{\text{ is divisible by a square}}>1.\end{cases}}} 1.\end{cases}}}"/>

The Möbius function can alternatively be represented as

μ ( n) = δ ω ( n) Ω ( n) λ ( n), {\displaystyle \mu (n)=\delta _{\omega (n)\Omega (n)}\lambda (n),}[image: {\displaystyle \mu (n)=\delta _{\omega (n)\Omega (n)}\lambda (n),}]

where δ i j {\displaystyle \delta _{ij}}[image: {\displaystyle \delta _{ij}}] is the [Kronecker delta][19], λ ( n) {\displaystyle \lambda (n)}[image: {\displaystyle \lambda (n)}] is the [Liouville function][20], and ω ( n) {\displaystyle \omega (n)}[image: {\displaystyle \omega (n)}] / Ω ( n) {\displaystyle \Omega (n)}[image: {\displaystyle \Omega (n)}] are the [Prime omega functions][21]. ω ( n) {\displaystyle \omega (n)}[image: {\displaystyle \omega (n)}] is the number of distinct prime divisors of n {\displaystyle n}[image: {\displaystyle n}], and Ω ( n) {\displaystyle \Omega (n)}[image: {\displaystyle \Omega (n)}] is the number of prime factors of n {\displaystyle n}[image: {\displaystyle n}], counted with multiplicity.

Another characterization by [Carl Friedrich Gauss][22] is the sum of all [primitive roots][23]. [4]

## Values

[[edit][24]]

The values of μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] for the first 60 positive numbers are

n {\displaystyle n}[image: {\displaystyle n}] | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |

μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] | 1 | −1 | −1 | 0 | −1 | 1 | −1 | 0 | 0 | 1 |

n {\displaystyle n}[image: {\displaystyle n}] | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |

μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] | −1 | 0 | −1 | 1 | 1 | 0 | −1 | 0 | −1 | 0 |

n {\displaystyle n}[image: {\displaystyle n}] | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |

μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] | 1 | 1 | −1 | 0 | 0 | 1 | 0 | 0 | −1 | −1 |

n {\displaystyle n}[image: {\displaystyle n}] | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |

μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] | −1 | 0 | 1 | 1 | 1 | 0 | −1 | 1 | 1 | 0 |

n {\displaystyle n}[image: {\displaystyle n}] | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |

μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] | −1 | −1 | −1 | 0 | 0 | 1 | −1 | 0 | 0 | 0 |

n {\displaystyle n}[image: {\displaystyle n}] | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 |

μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] | 1 | 0 | −1 | 0 | 1 | 0 | 1 | 1 | −1 | 0 |

The first 50 values of the function are plotted below:

[image: The 50 first values of

        μ
        (
        n
        )

    {\displaystyle \mu (n)}] [25] The 50 first values of μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}]

Larger values can be checked in:

- [Wolframalpha][26]
- [the b-file of OEIS][27]

## Applications

[[edit][28]]

### Mathematical series

[[edit][29]]

The [Dirichlet series][30] that [generates][31] the Möbius function is the (multiplicative) inverse of the [Riemann zeta function][32]; if s {\displaystyle s}[image: {\displaystyle s}] is a complex number with real part larger than 1 we have

∑ n = 1 ∞ μ ( n) n s = 1 ζ ( s). {\displaystyle \sum _{n=1}^{\infty }{\frac {\mu (n)}{n^{s}}}={\frac {1}{\zeta (s)}}.}[image: {\displaystyle \sum _{n=1}^{\infty }{\frac {\mu (n)}{n^{s}}}={\frac {1}{\zeta (s)}}.}]

This may be seen from its [Euler product][33]

1 ζ ( s) = ∏ p prime ( 1 − 1 p s) = ( 1 − 1 2 s) ( 1 − 1 3 s) ( 1 − 1 5 s) ⋯ {\displaystyle {\frac {1}{\zeta (s)}}=\prod _{p{\text{ prime}}}{\left(1-{\frac {1}{p^{s}}}\right)}=\left(1-{\frac {1}{2^{s}}}\right)\left(1-{\frac {1}{3^{s}}}\right)\left(1-{\frac {1}{5^{s}}}\right)\cdots }[image: {\displaystyle {\frac {1}{\zeta (s)}}=\prod _{p{\text{ prime}}}{\left(1-{\frac {1}{p^{s}}}\right)}=\left(1-{\frac {1}{2^{s}}}\right)\left(1-{\frac {1}{3^{s}}}\right)\left(1-{\frac {1}{5^{s}}}\right)\cdots }]

Also:

- ∑ n = 1 ∞ | μ ( n) | n s = ζ ( s) ζ ( 2 s); {\displaystyle \sum \limits _{n=1}^{\infty }{\frac {|\mu (n)|}{n^{s}}}={\frac {\zeta (s)}{\zeta (2s)}};}[image: {\displaystyle \sum \limits _{n=1}^{\infty }{\frac {|\mu (n)|}{n^{s}}}={\frac {\zeta (s)}{\zeta (2s)}};}]
- ∑ n = 1 ∞ μ ( n) n = 0; {\displaystyle \sum _{n=1}^{\infty }{\frac {\mu (n)}{n}}=0;}[image: {\displaystyle \sum _{n=1}^{\infty }{\frac {\mu (n)}{n}}=0;}]
- ∑ n = 1 ∞ μ ( n) ln ⁡ n n = − 1; {\displaystyle \sum \limits _{n=1}^{\infty }{\frac {\mu (n)\ln n}{n}}=-1;}[image: {\displaystyle \sum \limits _{n=1}^{\infty }{\frac {\mu (n)\ln n}{n}}=-1;}]
- ∑ n = 1 ∞ μ ( n) ln 2 ⁡ n n = − 2 γ, {\displaystyle \sum \limits _{n=1}^{\infty }{\frac {\mu (n)\ln ^{2}n}{n}}=-2\gamma ,}[image: {\displaystyle \sum \limits _{n=1}^{\infty }{\frac {\mu (n)\ln ^{2}n}{n}}=-2\gamma ,}] where γ {\displaystyle \gamma }[image: {\displaystyle \gamma }] is [Euler's constant][34].

The [Lambert series][35] for the Möbius function is

∑ n = 1 ∞ μ ( n) q n 1 − q n = q, {\displaystyle \sum _{n=1}^{\infty }{\frac {\mu (n)q^{n}}{1-q^{n}}}=q,}[image: {\displaystyle \sum _{n=1}^{\infty }{\frac {\mu (n)q^{n}}{1-q^{n}}}=q,}]

which converges for | q | < 1 {\displaystyle |q|<1}[image: {\displaystyle |q|<1}]. For prime α ≥ 2 {\displaystyle \alpha \geq 2}[image: {\displaystyle \alpha \geq 2}], we also have

∑ n = 1 ∞ μ ( α n) q n q n − 1 = ∑ n ≥ 0 q α n, | q | < 1. {\displaystyle \sum _{n=1}^{\infty }{\frac {\mu (\alpha n)q^{n}}{q^{n}-1}}=\sum _{n\geq 0}q^{\alpha ^{n}},|q|<1.}[image: {\displaystyle \sum _{n=1}^{\infty }{\frac {\mu (\alpha n)q^{n}}{q^{n}-1}}=\sum _{n\geq 0}q^{\alpha ^{n}},|q|<1.}]

### Algebraic number theory

[[edit][36]]

Gauss [1] proved that for a prime number p {\displaystyle p}[image: {\displaystyle p}] the sum of its [primitive roots][37] is congruent to μ ( p − 1) mod p {\displaystyle \mu (p-1)\mod p}[image: {\displaystyle \mu (p-1)\mod p}].

If F q {\displaystyle \mathbb {F} _{q}}[image: {\displaystyle \mathbb {F} _{q}}] denotes the [finite field][38] of order q {\displaystyle q}[image: {\displaystyle q}] (where q {\displaystyle q}[image: {\displaystyle q}] is necessarily a [prime power][39]), then the number N {\displaystyle N}[image: {\displaystyle N}] of monic irreducible polynomials of degree n {\displaystyle n}[image: {\displaystyle n}] over F q {\displaystyle \mathbb {F} _{q}}[image: {\displaystyle \mathbb {F} _{q}}] is given by [5]

N ( q, n) = 1 n ∑ d ∣ n μ ( d) q n d. {\displaystyle N(q,n)={\frac {1}{n}}\sum _{d\mid n}\mu (d)q^{\frac {n}{d}}.}[image: {\displaystyle N(q,n)={\frac {1}{n}}\sum _{d\mid n}\mu (d)q^{\frac {n}{d}}.}]

The Möbius function is used in the [Möbius inversion formula][16].

### Physics

[[edit][40]]

The Möbius function also arises in the [primon gas][41] or [free Riemann gas][42] model of [supersymmetry][43]. In this theory, the fundamental particles or "primons" have energies log ⁡ ( p) {\displaystyle \log(p)}[image: {\displaystyle \log(p)}]. Under [second quantization][44], multiparticle excitations are considered; these are given by log ⁡ ( n) {\displaystyle \log(n)}[image: {\displaystyle \log(n)}] for any [natural number][45] n {\displaystyle n}[image: {\displaystyle n}]. This follows from the fact that the factorization of the natural numbers into primes is unique.

In the free Riemann gas, any natural number can occur, if the [primons][41] are taken as [bosons][46]. If they are taken as [fermions][47], then the [Pauli exclusion principle][48] excludes squares. The operator [image: {\displaystyle (-1)^{F}}] [( − 1) F {\displaystyle (-1)^{F}}][49] that distinguishes fermions and bosons is then none other than the Möbius function μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}].

The free Riemann gas has a number of other interesting connections to number theory, including the fact that the [partition function][50] is the [Riemann zeta function][32]. This idea underlies [Alain Connes][51] 's attempted proof of the [Riemann hypothesis][52]. [6]

## Properties

[[edit][53]]

The Möbius function is [multiplicative][13] (i.e., μ ( a b) = μ ( a) μ ( b) {\displaystyle \mu (ab)=\mu (a)\mu (b)}[image: {\displaystyle \mu (ab)=\mu (a)\mu (b)}] whenever a {\displaystyle a}[image: {\displaystyle a}] and b {\displaystyle b}[image: {\displaystyle b}] are [coprime][54]).

**Proof**: Given two coprime numbers m ≥ n {\displaystyle m\geq n}[image: {\displaystyle m\geq n}], we induct on m n {\displaystyle mn}[image: {\displaystyle mn}]. If m n = 1 {\displaystyle mn=1}[image: {\displaystyle mn=1}], then μ ( m n) = 1 = μ ( m) μ ( n) {\displaystyle \mu (mn)=1=\mu (m)\mu (n)}[image: {\displaystyle \mu (mn)=1=\mu (m)\mu (n)}]. Otherwise, n \\geq 1"}}'> n\geq 1}"> m > n ≥ 1 {\displaystyle m>n\geq 1} n\geq 1}"/>, so

0 = ∑ d | m n μ ( d) = μ ( m n) + ∑ d | m n; d < m n μ ( d) = induction μ ( m n) − μ ( m) μ ( n) + ∑ d | m; d ′ | n μ ( d) μ ( d ′) = μ ( m n) − μ ( m) μ ( n) + ∑ d | m μ ( d) ∑ d ′ | n μ ( d ′) = μ ( m n) − μ ( m) μ ( n) + 0 {\displaystyle {\begin{aligned}0&=\sum _{d|mn}\mu (d)\\&=\mu (mn)+\sum _{d|mn;d<mn}\mu (d)\\&{\stackrel {\text{induction}}{=}}\mu (mn)-\mu (m)\mu (n)+\sum _{d|m;d'|n}\mu (d)\mu (d')\\&=\mu (mn)-\mu (m)\mu (n)+\sum _{d|m}\mu (d)\sum _{d'|n}\mu (d')\\&=\mu (mn)-\mu (m)\mu (n)+0\end{aligned}}}[image: {\displaystyle {\begin{aligned}0&=\sum _{d|mn}\mu (d)\\&=\mu (mn)+\sum _{d|mn;d<mn}\mu (d)\\&{\stackrel {\text{induction}}{=}}\mu (mn)-\mu (m)\mu (n)+\sum _{d|m;d'|n}\mu (d)\mu (d')\\&=\mu (mn)-\mu (m)\mu (n)+\sum _{d|m}\mu (d)\sum _{d'|n}\mu (d')\\&=\mu (mn)-\mu (m)\mu (n)+0\end{aligned}}}]

The sum of the Möbius function over all positive divisors of n {\displaystyle n}[image: {\displaystyle n}] (including n {\displaystyle n}[image: {\displaystyle n}] itself and 1) is zero except when n = 1 {\displaystyle n=1}[image: {\displaystyle n=1}]:

1.\n\\end{cases}"}}'> 1.\end{cases}}}"> ∑ d ∣ n μ ( d) = { 1 if n = 1, 0 if n > 1. {\displaystyle \sum _{d\mid n}\mu (d)={\begin{cases}1&{\text{if }}n=1,\\0&{\text{if }}n>1.\end{cases}}} 1.\end{cases}}}"/>

The equality above leads to the important [Möbius inversion formula][16] and is the main reason why μ {\displaystyle \mu }[image: {\displaystyle \mu }] is of relevance in the theory of multiplicative and arithmetic functions.

Other applications of μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] in combinatorics are connected with the use of the [Pólya enumeration theorem][55] in combinatorial groups and combinatorial enumerations.

There is a formula [7] for calculating the Möbius function without directly knowing the factorization of its argument:

μ ( n) = ∑ gcd ( k, n) = 1 1 ≤ k ≤ n e 2 π i k n, {\displaystyle \mu (n)=\sum _{\stackrel {1\leq k\leq n}{\gcd(k,\,n)=1}}e^{2\pi i{\frac {k}{n}}},}[image: {\displaystyle \mu (n)=\sum _{\stackrel {1\leq k\leq n}{\gcd(k,\,n)=1}}e^{2\pi i{\frac {k}{n}}},}]

i.e. μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] is the sum of the primitive n {\displaystyle n}[image: {\displaystyle n}] -th [roots of unity][56]. (However, the computational complexity of this definition is at least the same as that of the Euler product definition.)

Other identities satisfied by the Möbius function include

∑ k ≤ n ⌊ n k ⌋ μ ( k) = 1 {\displaystyle \sum _{k\leq n}\left\lfloor {\frac {n}{k}}\right\rfloor \mu (k)=1}[image: {\displaystyle \sum _{k\leq n}\left\lfloor {\frac {n}{k}}\right\rfloor \mu (k)=1}]

and

∑ j k ≤ n sin ⁡ ( π j k 2) μ ( k) = 1 {\displaystyle \sum _{jk\leq n}\sin \left({\frac {\pi jk}{2}}\right)\mu (k)=1}[image: {\displaystyle \sum _{jk\leq n}\sin \left({\frac {\pi jk}{2}}\right)\mu (k)=1}].

The first of these is a classical result while the second was published in 2020. [8] [9] Similar identities hold for the [Mertens function][57].

### Proof of the formula for the sum of μ {\displaystyle \mu }[image: {\displaystyle \mu }] over divisors

[[edit][58]]

The formula

1\n\\end{cases}"}}'> 1\end{cases}}}"> ∑ d ∣ n μ ( d) = { 1 if n = 1, 0 if n > 1 {\displaystyle \sum _{d\mid n}\mu (d)={\begin{cases}1&{\text{if }}n=1,\\0&{\text{if }}n>1\end{cases}}} 1\end{cases}}}"/>

can be written using [Dirichlet convolution][59] as: 1 ∗ μ = ε {\displaystyle 1*\mu =\varepsilon }[image: {\displaystyle 1*\mu =\varepsilon }] where ε {\displaystyle \varepsilon }[image: {\displaystyle \varepsilon }] is the [identity under the convolution][60].

One way of proving this formula is by noting that the Dirichlet convolution of two [multiplicative functions][61] is again multiplicative. Thus it suffices to prove the formula for powers of primes. Indeed, for any prime p {\displaystyle p}[image: {\displaystyle p}] and for any 0"}}'> 0}"> k > 0 {\displaystyle k>0} 0}"/>

1 ∗ μ ( p k) = ∑ d ∣ p k μ ( d) = μ ( 1) + μ ( p) + ∑ 1 < m <= k μ ( p m) = 1 − 1 + ∑ 0 = 0 = ε ( p k) {\displaystyle 1*\mu (p^{k})=\sum _{d\mid p^{k}}\mu (d)=\mu (1)+\mu (p)+\sum _{1<m<=k}\mu (p^{m})=1-1+\sum 0=0=\varepsilon (p^{k})}[image: {\displaystyle 1*\mu (p^{k})=\sum _{d\mid p^{k}}\mu (d)=\mu (1)+\mu (p)+\sum _{1<m<=k}\mu (p^{m})=1-1+\sum 0=0=\varepsilon (p^{k})}],

while for n = 1 {\displaystyle n=1}[image: {\displaystyle n=1}]

1 ∗ μ ( 1) = ∑ d ∣ 1 μ ( d) = μ ( 1) = 1 = ε ( 1) {\displaystyle 1*\mu (1)=\sum _{d\mid 1}\mu (d)=\mu (1)=1=\varepsilon (1)}[image: {\displaystyle 1*\mu (1)=\sum _{d\mid 1}\mu (d)=\mu (1)=1=\varepsilon (1)}].

#### Other proofs

[[edit][62]]

Another way of proving this formula is by using the identity

μ ( n) = ∑ gcd ( k, n) = 1 1 ≤ k ≤ n e 2 π i k n, {\displaystyle \mu (n)=\sum _{\stackrel {1\leq k\leq n}{\gcd(k,\,n)=1}}e^{2\pi i{\frac {k}{n}}},}[image: {\displaystyle \mu (n)=\sum _{\stackrel {1\leq k\leq n}{\gcd(k,\,n)=1}}e^{2\pi i{\frac {k}{n}}},}]

The formula above is then a consequence of the fact that the n {\displaystyle n}[image: {\displaystyle n}] th roots of unity sum to 0, since each n {\displaystyle n}[image: {\displaystyle n}] th root of unity is a primitive d {\displaystyle d}[image: {\displaystyle d}] th root of unity for exactly one divisor d {\displaystyle d}[image: {\displaystyle d}] of n {\displaystyle n}[image: {\displaystyle n}].

However it is also possible to prove this identity from first principles. First note that it is trivially true when n = 1 {\displaystyle n=1}[image: {\displaystyle n=1}]. Suppose then that 1"}}'> 1}"> n > 1 {\displaystyle n>1} 1}"/>. Then there is a [bijection][63] between the factors d {\displaystyle d}[image: {\displaystyle d}] of n {\displaystyle n}[image: {\displaystyle n}] for which μ ( d) ≠ 0 {\displaystyle \mu (d)\neq 0}[image: {\displaystyle \mu (d)\neq 0}] and the subsets of the set of all prime factors of n {\displaystyle n}[image: {\displaystyle n}]. The asserted result follows from the fact that every non-empty [finite set][64] has an equal number of odd- and even-cardinality subsets.

This last fact can be shown easily by induction on the cardinality | S | {\displaystyle |S|}[image: {\displaystyle |S|}] of a non-empty finite set S {\displaystyle S}[image: {\displaystyle S}]. First, if | S | = 1 {\displaystyle |S|=1}[image: {\displaystyle |S|=1}], there is exactly one odd-cardinality subset of S {\displaystyle S}[image: {\displaystyle S}], namely S {\displaystyle S}[image: {\displaystyle S}] itself, and exactly one even-cardinality subset, namely ∅ {\displaystyle \emptyset }[image: {\displaystyle \emptyset }]. Next, if 1"}}'> 1}"> | S | > 1 {\displaystyle |S|>1} 1}"/>, then divide the subsets of S {\displaystyle S}[image: {\displaystyle S}] into two subclasses depending on whether they contain or not some fixed element x {\displaystyle x}[image: {\displaystyle x}] in S {\displaystyle S}[image: {\displaystyle S}]. There is an obvious bijection between these two subclasses, pairing those subsets that have the same complement relative to the subset { x } {\displaystyle \{x\}}[image: {\displaystyle \{x\}}]. Also, one of these two subclasses consists of all the subsets of the set S ∖ { x } {\displaystyle S\setminus \{x\}}[image: {\displaystyle S\setminus \{x\}}], and therefore, by the induction hypothesis, has an equal number of odd- and even-cardinality subsets. These subsets in turn correspond bijectively to the even- and odd-cardinality { x } {\displaystyle \{x\}}[image: {\displaystyle \{x\}}] -containing subsets of S {\displaystyle S}[image: {\displaystyle S}]. The inductive step follows directly from these two bijections.

A related result is that the binomial coefficients exhibit alternating entries of odd and even power which sum symmetrically.

### Average order

[[edit][65]]

The [mean value (in the sense of average orders)][66] of the Möbius function is zero. This statement is, in fact, equivalent to the [prime number theorem][67]. [10]

### μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] sections

[[edit][68]]

μ ( n) = 0 {\displaystyle \mu (n)=0}[image: {\displaystyle \mu (n)=0}] [if and only if][69] n {\displaystyle n}[image: {\displaystyle n}] is divisible by the square of a prime. The first numbers with this property are

4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28, 32, 36, 40, 44, 45, 48, 49, 50, 52, 54, 56, 60, 63, ... (sequence [A013929][70] in the [OEIS][11]).

If n {\displaystyle n}[image: {\displaystyle n}] is prime, then μ ( n) = − 1 {\displaystyle \mu (n)=-1}[image: {\displaystyle \mu (n)=-1}], but the converse is not true. The first non prime n {\displaystyle n}[image: {\displaystyle n}] for which μ ( n) = − 1 {\displaystyle \mu (n)=-1}[image: {\displaystyle \mu (n)=-1}] is 30 = 2 × 3 × 5 {\displaystyle 30=2\times 3\times 5}[image: {\displaystyle 30=2\times 3\times 5}]. The first such numbers with three distinct prime factors ( [sphenic numbers][71]) are

30, 42, 66, 70, 78, 102, 105, 110, 114, 130, 138, 154, 165, 170, 174, 182, 186, 190, 195, 222, ... (sequence [A007304][72] in the [OEIS][11]).

and the first such numbers with 5 distinct prime factors are

2310, 2730, 3570, 3990, 4290, 4830, 5610, 6006, 6090, 6270, 6510, 6630, 7410, 7590, 7770, 7854, 8610, 8778, 8970, 9030, 9282, 9570, 9690, ... (sequence [A046387][73] in the [OEIS][11]).

## Mertens function

[[edit][74]]

In number theory another [arithmetic function][75] closely related to the Möbius function is the [Mertens function][57], defined by

M ( n) = ∑ k = 1 n μ ( k) {\displaystyle M(n)=\sum _{k=1}^{n}\mu (k)}[image: {\displaystyle M(n)=\sum _{k=1}^{n}\mu (k)}]

for every natural number n. This function is closely linked with the positions of zeroes of the [Riemann zeta function][32]. See the article on the [Mertens conjecture][76] for more information about the connection between M ( n) {\displaystyle M(n)}[image: {\displaystyle M(n)}] and the [Riemann hypothesis][52].

From the formula

μ ( n) = ∑ gcd ( k, n) = 1 1 ≤ k ≤ n e 2 π i k n, {\displaystyle \mu (n)=\sum _{\stackrel {1\leq k\leq n}{\gcd(k,n)=1}}e^{2\pi i{\frac {k}{n}}},}[image: {\displaystyle \mu (n)=\sum _{\stackrel {1\leq k\leq n}{\gcd(k,n)=1}}e^{2\pi i{\frac {k}{n}}},}]

it follows that the Mertens function is given by

M ( n) = − 1 + ∑ a ∈ F n e 2 π i a, {\displaystyle M(n)=-1+\sum _{a\in {\mathcal {F}}_{n}}e^{2\pi ia},}[image: {\displaystyle M(n)=-1+\sum _{a\in {\mathcal {F}}_{n}}e^{2\pi ia},}]

where F n {\displaystyle {\mathcal {F}}_{n}}[image: {\displaystyle {\mathcal {F}}_{n}}] is the [Farey sequence][77] of order n {\displaystyle n}[image: {\displaystyle n}].

This formula is used in the proof of the [Franel–Landau theorem][78]. [11]

## Generalizations

[[edit][79]]

### Incidence algebras

[[edit][80]]

In [combinatorics][81], every locally finite [partially ordered set][82] (poset) is assigned an [incidence algebra][1]. One distinguished member of this algebra is that poset's "Möbius function". The classical Möbius function treated in this article is essentially equal to the Möbius function of the set of all positive integers partially ordered by [divisibility][83]. See the article on [incidence algebras][1] for the precise definition and several examples of these general Möbius functions.

Because the Möbius function is multipliciative, so is its (iterated) [Dirichlet convolution][59] μ k = μ ∗ ⋯ ∗ μ {\displaystyle \mu _{k}=\mu *\cdots *\mu }[image: {\displaystyle \mu _{k}=\mu *\cdots *\mu }] to be the k {\displaystyle k}[image: {\displaystyle k}] -fold [Dirichlet convolution][59] of the Möbius function with itself. We then have μ k ( p a) = ( − 1) a ( k a) {\displaystyle \mu _{k}\left(p^{a}\right)=(-1)^{a}{\binom {k}{a}}}[image: {\displaystyle \mu _{k}\left(p^{a}\right)=(-1)^{a}{\binom {k}{a}}}] where the [binomial coefficient][84] is taken to be zero if k"}}'> k}"> a > k {\displaystyle a>k} k}"/>. [12] The definition may be extended to complex k {\displaystyle k}[image: {\displaystyle k}] by reading the binomial as a polynomial in k {\displaystyle k}[image: {\displaystyle k}]. [13]

## Implementations

[[edit][85]]

- [Mathematica][86]
- [Maxima][87]
- [geeksforgeeks][88] C++, Python3, Java, C#, PHP, JavaScript
- [Rosetta Code][89]
- [Sage][90]

## See also

[[edit][91]]

- [Liouville function][20]
- [Mertens function][57]
- [Ramanujan's sum][92]
- [Sphenic number][71]

## Notes

[[edit][93]]

1. ↑ Hardy & Wright, Notes on ch. XVI: "... μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] occurs implicitly in the works of Euler as early as 1748, but Möbius, in 1832, was the first to investigate its properties systematically". ( Hardy & Wright 1980, Notes on ch. XVI)
2. ↑ In the *[Disquisitiones Arithmeticae][94]*(1801) [Carl Friedrich Gauss][22] showed that the sum of the primitive roots ( mod p {\displaystyle \mod p}[image: {\displaystyle \mod p}]) is μ ( p − 1) {\displaystyle \mu (p-1)}[image: {\displaystyle \mu (p-1)}], (see #Properties and applications) but he didn't make further use of the function. In particular, he didn't use Möbius inversion in the *Disquisitiones*. [1] The *[Disquisitiones Arithmeticae][94]*has been translated from Latin into English and German. The German edition includes all of his papers on number theory: all the proofs of quadratic reciprocity, the determination of the sign of the Gauss sum, the investigations into biquadratic reciprocity, and unpublished notes.

### Citations

[[edit][95]]

1. 1 2 Gauss 1986, Art. 81.
2. ↑ Möbius 1832, pp. 105–123.
3. ↑ Abramowitz & Stegun 1972, p. 826.
4. ↑ Weisstein, Eric W. ["Möbius Function"][96]. *mathworld.wolfram.com*. Retrieved 1 October 2024.
5. ↑ Jacobson 2009, §4.13.
6. ↑ Bost & Connes 1995, pp. 411–457.
7. ↑ Hardy & Wright 1980, (16.6.4), p. 239.
8. ↑ Apostol 1976.
9. ↑ Kline 2020.
10. ↑ Apostol 1976, §3.9.
11. ↑ Edwards 1974, Ch. 12.2.
12. ↑ Popovici 1963, pp. 493–499.
13. ↑ Sándor & Crstici 2004, p. 107.

## Sources

[[edit][97]]

"}},"i":8}},"\n*",{"template":{"target":{"wt":"Cite journal ","href":"./Template:Cite_journal"},"params":{"last":{"wt":"Kline"},"first":{"wt":"Jeffery"},"year":{"wt":"2020"},"title":{"wt":"Unital Sums of the Möbius and Mertens Functions"},"url":{"wt":"https://cs.uwaterloo.ca/journals/JIS/VOL23/Kline/kline4.pdf"},"journal":{"wt":"Journal of Integer Sequences"},"volume":{"wt":"23"},"issue":{"wt":"8"},"pages":{"wt":"1–17"}},"i":9}},"\n*",{"template":{"target":{"wt":"Cite book ","href":"./Template:Cite_book"},"params":{"last":{"wt":"Jacobson"},"first":{"wt":"Nathan"},"author-link":{"wt":"Nathan Jacobson"},"title":{"wt":"Basic algebra I"},"publisher":{"wt":"Dover Publications"},"year":{"wt":"2009"},"isbn":{"wt":"978-0-486-47189-1"},"edition":{"wt":"2nd"},"orig-year":{"wt":"First published 1985"}},"i":10}},"\n* ",{"template":{"target":{"wt":"springer","href":"./Template:Springer"},"params":{"title":{"wt":"Möbius function"},"last":{"wt":"Klimov"},"first":{"wt":"N. I."},"id":{"wt":"m/m064280"}},"i":11}},"\n*",{"template":{"target":{"wt":"Cite journal ","href":"./Template:Cite_journal"},"params":{"last":{"wt":"Möbius"},"first":{"wt":"A. F."},"author-link":{"wt":"August Ferdinand Möbius"},"year":{"wt":"1832"},"title":{"wt":"Über eine besondere Art von Umkehrung der Reihen"},"url":{"wt":"https://www.digizeitschriften.de/en/dms/img/?PID=GDZPPN002138654"},"journal":{"wt":"[[Crelle's Journal|Journal für die reine und angewandte Mathematik]]"},"volume":{"wt":"9"},"pages":{"wt":"105–123"}},"i":12}},"\n*",{"template":{"target":{"wt":"Cite web ","href":"./Template:Cite_web"},"params":{"last":{"wt":"Pegg"},"first":{"wt":"Ed Jr"},"author-link":{"wt":"Ed Pegg Jr."},"date":{"wt":"2003"},"title":{"wt":"The Möbius function (and squarefree numbers)"},"url":{"wt":"http://www.mathpuzzle.com/MAA/02-Mobius%20Function/mathgames_11_03_03.html"},"website":{"wt":"Ed Pegg's Math Games"},"mode":{"wt":"cs2"}},"i":13}},"\n*",{"template":{"target":{"wt":"Cite journal ","href":"./Template:Cite_journal"},"params":{"last":{"wt":"Popovici"},"first":{"wt":"Constantin P."},"year":{"wt":"1963"},"title":{"wt":"A generalization of the Möbius function"},"journal":{"wt":"Studii şi Cercetări Matematice"},"volume":{"wt":"14"},"pages":{"wt":"493–499"},"mr":{"wt":"0181602"}},"i":14}},"\n*",{"template":{"target":{"wt":"Cite book ","href":"./Template:Cite_book"},"params":{"last1":{"wt":"Sándor"},"first1":{"wt":"Jozsef"},"title":{"wt":"Handbook of number theory II"},"last2":{"wt":"Crstici"},"first2":{"wt":"Borislav"},"publisher":{"wt":"Kluwer Academic"},"year":{"wt":"2004"},"isbn":{"wt":"1-4020-2546-7"},"location":{"wt":"Dordrecht"},"zbl":{"wt":"1079.11001"}},"i":15}},"\n*",{"template":{"target":{"wt":"Cite book ","href":"./Template:Cite_book"},"params":{"title":{"wt":"Handbook of number theory I"},"publisher":{"wt":"[[Springer-Verlag]]"},"year":{"wt":"2006"},"isbn":{"wt":"1-4020-4215-9"},"editor-last":{"wt":"Sándor"},"editor-first":{"wt":"József"},"location":{"wt":"Dordrecht"},"pages":{"wt":"187–226"},"zbl":{"wt":"1151.11300"},"editor-last2":{"wt":"Mitrinović"},"editor-first2":{"wt":"Dragoslav S."},"editor-last3":{"wt":"Crstici"},"editor-first3":{"wt":"Borislav"}},"i":16}},"\n",{"template":{"target":{"wt":"refend","href":"./Template:Refend"},"params":{},"i":17}}]}'>

- Abramowitz, Milton; Stegun, Irene A. (1972) [1964]. *Handbook of mathematical functions: with formulas, graphs and mathematical tables [conference under the auspices of the National science foundation and the Massachusetts institute of technology]*. Dover books on advanced mathematics. New York: Dover. [ISBN][98] [978-0-486-61272-0][99].
- [Apostol, Tom M.][100] (1976). *Introduction to analytic number theory*. Undergraduate Texts in Mathematics. New York; Heidelberg: Springer-Verlag. [ISBN][98] [978-0-387-90163-3][101]. [MR][102] [0434929][103]. [Zbl][104] [0335.10001][105].
- Bost, J.-B.; Connes, Alain (1995). ["Hecke Algebras, Type III factors and phase transitions with spontaneous symmetry breaking in number theory"][106]. *Selecta Mathematica*. New Series. **1**(3): 411– 457. [doi][107]: [10.1007/BF01589495][108]. [S2CID][109] [116418599][110].
- Deléglise, Marc; Rivat, Joël (1996). ["Computing the summation of the Möbius function"][111]. *Experimental Mathematics*. **5**(4): 291– 295. [doi][107]: [10.1080/10586458.1996.10504594][112]. [S2CID][109] [574146][113].
- [Edwards, Harold][114] (1974). *Riemann's Zeta Function*. Mineola, New York: Dover Publications. [ISBN][98] [0-486-41740-9][115].
- [Gauss, Carl Friedrich][22] (1965). *Untersuchungen uber hohere Arithmetik (Disquisitiones Arithemeticae & other papers on number theory)*. Translated by Maser, H. (2nd ed.). New York: Chelsea. [ISBN][98] [0-8284-0191-8][116].
- [Gauss, Carl Friedrich][22] (1986). *Disquisitiones Arithemeticae*. Translated by Clarke, Arthur A. (corrected 2nd ed.). New York: [Springer][117]. [ISBN][98] [0-387-96254-9][118].
- [Hardy, G. H.][119]; [Wright, E. M.][120] (1980) [First edition published 1938]. **[An Introduction to the Theory of Numbers][121] (5th ed.). Oxford: [Oxford University Press][122]. [ISBN][98] [978-0-19-853171-5][123] – via [Internet Archive][124].
- Kline, Jeffery (2020). ["Unital Sums of the Möbius and Mertens Functions"][125] (PDF). *Journal of Integer Sequences*. **23**(8): 1– 17.
- [Jacobson, Nathan][126] (2009) [First published 1985]. *Basic algebra I*(2nd ed.). Dover Publications. [ISBN][98] [978-0-486-47189-1][127].
- Klimov, N. I. (2001) [1994], ["Möbius function"][128], *[Encyclopedia of Mathematics][129]*, EMS Press
- [Möbius, A. F.][10] (1832). ["Über eine besondere Art von Umkehrung der Reihen"][130]. *[Journal für die reine und angewandte Mathematik][131]*. **9**: 105– 123.
- [Pegg, Ed Jr][132] (2003), ["The Möbius function (and squarefree numbers)"][133], *Ed Pegg's Math Games*
- Popovici, Constantin P. (1963). "A generalization of the Möbius function". *Studii şi Cercetări Matematice*. **14**: 493– 499. [MR][102] [0181602][134].
- Sándor, Jozsef; Crstici, Borislav (2004). *Handbook of number theory II*. Dordrecht: Kluwer Academic. [ISBN][98] [1-4020-2546-7][135]. [Zbl][104] [1079.11001][136].
- Sándor, József; Mitrinović, Dragoslav S.; Crstici, Borislav, eds. (2006). *Handbook of number theory I*. Dordrecht: [Springer-Verlag][137]. pp. 187– 226. [ISBN][98] [1-4020-4215-9][138]. [Zbl][104] [1151.11300][139].

## External links

[[edit][140]]

- [Weisstein, Eric W.][141] ["Möbius function"][96]. *[MathWorld][142]*.

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Möbius_function&oldid=1363371224][143] "

[Category][144]:

- [Multiplicative functions][145]

Hidden categories:

- [Articles with short description][146]
- [Short description matches Wikidata][147]
- [Use dmy dates from October 2024][148]
- [Articles lacking in-text citations from October 2024][149]
- [All articles lacking in-text citations][150]

Search

Möbius function

33 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Incidence_algebra
[2]: https://en.wikipedia.org/wiki/Rational_function
[3]: https://en.wikipedia.org/wiki/Complex_number
[4]: https://en.wikipedia.org/wiki/Möbius_transformation
[5]: https://en.wikipedia.org/wiki/Wikipedia:Citing_sources#General_references
[6]: https://en.wikipedia.org/wiki/Wikipedia:Citing_sources#Inline_citations
[7]: https://en.wikipedia.org/w/index.php?title=M%C3%B6bius_function&amp;action=edit
[8]: https://en.wikipedia.org/wiki/Wikipedia:When_to_cite
[9]: https://en.wikipedia.org/wiki/Help:Maintenance_template_removal
[10]: https://en.wikipedia.org/wiki/August_Ferdinand_Möbius
[11]: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
[12]: //oeis.org/A008683
[13]: https://en.wikipedia.org/wiki/Multiplicative_function
[14]: https://en.wikipedia.org/wiki/Number_theory
[15]: https://en.wikipedia.org/wiki/Analytic_number_theory
[16]: https://en.wikipedia.org/wiki/Möbius_inversion_formula
[17]: https://en.wikipedia.org/wiki/Gian-Carlo_Rota
[18]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=1
[19]: https://en.wikipedia.org/wiki/Kronecker_delta
[20]: https://en.wikipedia.org/wiki/Liouville_function
[21]: https://en.wikipedia.org/wiki/Prime_omega_function
[22]: https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss
[23]: https://en.wikipedia.org/wiki/Primitive_root_modulo_n
[24]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=2
[25]: https://en.wikipedia.org/wiki/File:Moebius_mu.svg
[26]: https://www.wolframalpha.com/input/?i=MoebiusMu+123
[27]: https://oeis.org/A008683/b008683.txt
[28]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=3
[29]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=4
[30]: https://en.wikipedia.org/wiki/Dirichlet_series
[31]: https://en.wikipedia.org/wiki/Generating_function
[32]: https://en.wikipedia.org/wiki/Riemann_zeta_function
[33]: https://en.wikipedia.org/wiki/Euler_product
[34]: https://en.wikipedia.org/wiki/Euler's_constant
[35]: https://en.wikipedia.org/wiki/Lambert_series
[36]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=5
[37]: https://en.wikipedia.org/wiki/Primitive_root_modulo_n#Arithmetic_facts
[38]: https://en.wikipedia.org/wiki/Finite_field
[39]: https://en.wikipedia.org/wiki/Prime_power
[40]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=6
[41]: https://en.wikipedia.org/wiki/Primon_gas
[42]: https://en.wikipedia.org/wiki/Free_Riemann_gas
[43]: https://en.wikipedia.org/wiki/Supersymmetry
[44]: https://en.wikipedia.org/wiki/Second_quantization
[45]: https://en.wikipedia.org/wiki/Natural_number
[46]: https://en.wikipedia.org/wiki/Boson
[47]: https://en.wikipedia.org/wiki/Fermion
[48]: https://en.wikipedia.org/wiki/Pauli_exclusion_principle
[49]: https://en.wikipedia.org/wiki/(-1)^F
[50]: https://en.wikipedia.org/wiki/Partition_function_(statistical_mechanics)
[51]: https://en.wikipedia.org/wiki/Alain_Connes
[52]: https://en.wikipedia.org/wiki/Riemann_hypothesis
[53]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=7
[54]: https://en.wikipedia.org/wiki/Coprime
[55]: https://en.wikipedia.org/wiki/Pólya_enumeration_theorem
[56]: https://en.wikipedia.org/wiki/Roots_of_unity
[57]: https://en.wikipedia.org/wiki/Mertens_function
[58]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=8
[59]: https://en.wikipedia.org/wiki/Dirichlet_convolution
[60]: https://en.wikipedia.org/wiki/Dirichlet_convolution#Properties
[61]: https://en.wikipedia.org/wiki/Multiplicative_functions
[62]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=9
[63]: https://en.wikipedia.org/wiki/Bijection
[64]: https://en.wikipedia.org/wiki/Finite_set
[65]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=10
[66]: https://en.wikipedia.org/wiki/Average_order_of_an_arithmetic_function
[67]: https://en.wikipedia.org/wiki/Prime_number_theorem
[68]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=11
[69]: https://en.wikipedia.org/wiki/If_and_only_if
[70]: //oeis.org/A013929
[71]: https://en.wikipedia.org/wiki/Sphenic_number
[72]: //oeis.org/A007304
[73]: //oeis.org/A046387
[74]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=12
[75]: https://en.wikipedia.org/wiki/Arithmetic_function
[76]: https://en.wikipedia.org/wiki/Mertens_conjecture
[77]: https://en.wikipedia.org/wiki/Farey_sequence
[78]: https://en.wikipedia.org/wiki/Farey_sequence#Riemann_hypothesis
[79]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=13
[80]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=14
[81]: https://en.wikipedia.org/wiki/Combinatorics
[82]: https://en.wikipedia.org/wiki/Partially_ordered_set
[83]: https://en.wikipedia.org/wiki/Divisor
[84]: https://en.wikipedia.org/wiki/Binomial_coefficient
[85]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=15
[86]: https://functions.wolfram.com/NumberTheoryFunctions/MoebiusMu/
[87]: https://maxima.sourceforge.io/docs/manual/maxima_singlepage.html#index-moebius
[88]: https://www.geeksforgeeks.org/program-mobius-function/
[89]: https://rosettacode.org/wiki/M%C3%B6bius_function
[90]: https://doc.sagemath.org/html/en/reference/rings%20standard/sage/arith/misc.html?highlight=moebius
[91]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=16
[92]: https://en.wikipedia.org/wiki/Ramanujan's_sum
[93]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=17
[94]: https://en.wikipedia.org/wiki/Disquisitiones_Arithmeticae
[95]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=18
[96]: https://mathworld.wolfram.com/MoebiusFunction.html
[97]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=19
[98]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[99]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-61272-0
[100]: https://en.wikipedia.org/wiki/Tom_M._Apostol
[101]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-90163-3
[102]: https://en.wikipedia.org/wiki/MR_(identifier)
[103]: https://mathscinet.ams.org/mathscinet-getitem?mr=0434929
[104]: https://en.wikipedia.org/wiki/Zbl_(identifier)
[105]: https://zbmath.org/?format=complete&amp;q=an:0335.10001
[106]: https://cds.cern.ch/record/283504
[107]: https://en.wikipedia.org/wiki/Doi_(identifier)
[108]: https://doi.org/10.1007%2FBF01589495
[109]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[110]: https://api.semanticscholar.org/CorpusID:116418599
[111]: https://projecteuclid.org/euclid.em/1047565447
[112]: https://doi.org/10.1080%2F10586458.1996.10504594
[113]: https://api.semanticscholar.org/CorpusID:574146
[114]: https://en.wikipedia.org/wiki/Harold_Edwards_(mathematician)
[115]: https://en.wikipedia.org/wiki/Special:BookSources/0-486-41740-9
[116]: https://en.wikipedia.org/wiki/Special:BookSources/0-8284-0191-8
[117]: https://en.wikipedia.org/wiki/Springer_Science+Business_Media
[118]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-96254-9
[119]: https://en.wikipedia.org/wiki/G._H._Hardy
[120]: https://en.wikipedia.org/wiki/E._M._Wright
[121]: https://archive.org/details/introductiontoth00hard
[122]: https://en.wikipedia.org/wiki/Oxford_University_Press
[123]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-853171-5
[124]: https://en.wikipedia.org/wiki/Internet_Archive
[125]: https://cs.uwaterloo.ca/journals/JIS/VOL23/Kline/kline4.pdf
[126]: https://en.wikipedia.org/wiki/Nathan_Jacobson
[127]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-47189-1
[128]: https://www.encyclopediaofmath.org/index.php?title=Möbius_function
[129]: https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics
[130]: https://www.digizeitschriften.de/en/dms/img/?PID=GDZPPN002138654
[131]: https://en.wikipedia.org/wiki/Crelle's_Journal
[132]: https://en.wikipedia.org/wiki/Ed_Pegg_Jr.
[133]: http://www.mathpuzzle.com/MAA/02-Mobius%20Function/mathgames_11_03_03.html
[134]: https://mathscinet.ams.org/mathscinet-getitem?mr=0181602
[135]: https://en.wikipedia.org/wiki/Special:BookSources/1-4020-2546-7
[136]: https://zbmath.org/?format=complete&amp;q=an:1079.11001
[137]: https://en.wikipedia.org/wiki/Springer-Verlag
[138]: https://en.wikipedia.org/wiki/Special:BookSources/1-4020-4215-9
[139]: https://zbmath.org/?format=complete&amp;q=an:1151.11300
[140]: /w/index.php?title=M%C3%B6bius_function&amp;action=edit&amp;section=20
[141]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[142]: https://en.wikipedia.org/wiki/MathWorld
[143]: https://en.wikipedia.org/w/index.php?title=Möbius_function&amp;oldid=1363371224
[144]: /wiki/Help:Category
[145]: /wiki/Category:Multiplicative_functions
[146]: /wiki/Category:Articles_with_short_description
[147]: /wiki/Category:Short_description_matches_Wikidata
[148]: /wiki/Category:Use_dmy_dates_from_October_2024
[149]: /wiki/Category:Articles_lacking_in-text_citations_from_October_2024
[150]: /wiki/Category:All_articles_lacking_in-text_citations
