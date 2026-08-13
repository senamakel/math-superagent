<!-- source: https://arxiv.org/html/2511.16817v1 | converted from HTML -->

Exceptions to theErdős–Straus–Schinzel conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2511.16817v1 [math.NT] 20 Nov 2025

# Exceptions to the
Erdős–Straus–Schinzel conjecture

Carl Pomerance Address: Department of Mathematics, Dartmouth College
Hanover, NH 03755 Email address: [carlp@math.dartmouth.edu][3] and Andreas Weingartner Address: Department of Mathematics, Southern Utah University
351 University Boulevard
Cedar City, UT 84720 Email address: [weingartner@suu.edu][4]

###### Abstract.

A famous conjecture of Erdős and Straus is that for every integer n ≥ 2 n\geq 2, 4 / n 4/n can be represented as 1 / x + 1 / y + 1 / z 1/x+1/y+1/z, where x, y, z x,y,z are positive integers. This conjecture was generalized to 5 / n 5/n by Sierpiński, and then Schinzel conjectured that for every integer m ≥ 4 m\geq 4 there is a bound n m n_{m} such that the fraction m / n m/n is the sum of 3 unit fractions for all integers n ≥ n m n\geq n_{m}. Leveraging and generalizing work of Elsholtz and Tao, we show that if n m n_{m} exists it must be at least exp ⁡ ( m 1 / 3 + o ⁡ ( 1)) \exp(m^{1/3+o(1)}); that is, there are numbers n n this large for which m / n m/n is not the sum of 3 unit fractions. We prove a weaker, but numerically explicit version of this theorem, showing that for m ≥ 6.52 × 10 9 m\geq 6.52\times 10^{9} there is a prime p ∈ ( m 2, 2 ​ m 2) p\in(m^{2},2m^{2}) with m / p m/p not the sum of 3 unit fractions, and report on some extensive numerical calculations that support this assertion with the much smaller bound m ≥ 19 m\geq 19. In addition we generalize a result of Vaughan to show that for each m m, most n n ’s have m / n m/n representable, and we prove a result generalizing the problem to the sum of j j unit fractions.

###### Key words and phrases:

Egyptian fraction, unit fraction

###### 2010 Mathematics Subject Classification

11D68, 11D72, 11N37

For Krishnaswami Alladi on his 70th birthday

## 1. Introduction

Egyptian fractions have a long and colorful history. According to the Rhind Papyrus (ca. 1550 BCE), ancient Egyptians preferred to write fractions as sums of unit fractions (fractions with numerator 1). We have not seen a compelling argument for why they had this preference, but nevertheless it opened the door to many intriguing problems. For surveys of some of the many problems and results, see [4, Ch. 4], [5, Sec. D11].

The Erdős–Straus conjecture, which dates to around 1948, asserts that 4 / n 4/n is the sum of 3 unit fractions for every integer n ≥ 2 n\geq 2. An early result of Obláth [10] is that n n has this property if n + 1 n+1 is divisible by a prime p ≡ 3 ( mod 4) p\equiv 3\pmod{4}. This implies that asymptotically all n n have the Erdős–Straus property, the number of possible exceptions up to N N being O ⁡ ( N / log ⁡ N) O(N/\sqrt{\log N}). The count of possible exceptions has been strongly improved, though not recently: In 1970, Vaughan [12] gave the upper bound N / exp ⁡ ( c ​ ( log ⁡ N) 2 / 3) N/\exp(c(\log N)^{2/3}) for a positive constant c c.

Sierpiński conjectured that not only 4 / n 4/n, but also 5 / n 5/n, can be written as a sum of 3 unit fractions, and then Schinzel conjectured that for each integer m ≥ 4 m\geq 4, m / n m/n is the sum of 3 unit fractions for all sufficiently large n n, depending on the choice of m m. Clearly a necessary condition for “sufficiently large” is that n ≥ m / 3 n\geq m/3. In this paper we show that “sufficiently large” is indeed big, in fact larger than any fixed power of m m.

###### Theorem 1.1.

For each ϵ > 0 \epsilon>0 there is a bound m ⁡ ( ϵ) m(\epsilon) such that for each m ≥ m ⁡ ( ϵ) m\geq m(\epsilon) there is some n > exp ⁡ ( m 1 / 3 − ϵ) n>\exp(m^{1/3-\epsilon}) with m / n m/n not the sum of 3 3 unit fractions.

For the proof we leverage some of the tools in Elsholtz–Tao [3], which paper was principally concerned with the number of representations of 4 / n 4/n as a sum of 3 unit fractions. We also prove a version of Theorem 1.1 that’s weaker, but numerically explicit, and in particular we obtain the following result.

###### Theorem 1.2.

For each integer m ≥ 6.52 × 10 9 m\geq 6.52\times 10^{9} there is a prime p ∈ ( m 2, 2 ​ m 2) p\in(m^{2},2m^{2}) for which m / p m/p is not the sum of 3 3 unit fractions.

Complementing our lower bounds we prove the following upper bound for the distribution of exceptions to the Erdős–Straus–Schinzel conjecture.

###### Theorem 1.3.

There is an absolute positive constant C C such that for each pair m, N m,N with 4 ≤ m ≤ ( log ⁡ N) 2 4\leq m\leq(\log N)^{2} the number of n ≤ N n\leq N with m / n m/n not the sum of 3 3 unit fractions is at most N / exp ⁡ ( C ​ ( log 2 ⁡ ( N) / φ ⁡ ( m)) 1 / 3) N/\exp(C(\log^{2}(N)/\varphi(m))^{1/3}).

Exploiting the large sieve, the proof is largely derivative of Vaughan’s theorem in [12].

In our proof of Theorem 1.1 we actually show that not only is there one exceptional n > exp ⁡ ( m 1 / 3 − ϵ) n>\exp(m^{1/3-\epsilon}), but that most prime values of n n near this bound are exceptions. This might be contrasted with Theorem 1.3 which implies that when n ≈ exp ⁡ ( m 1 / 2) n\approx\exp(m^{1/2}), most values of n n and in fact most primes are not exceptions. So between exp ⁡ ( m 1 / 3) \exp(m^{1/3}) and exp ⁡ ( m 1 / 2) \exp(m^{1/2}) there is a transition from “usually false” to “usually true”.

The proof of Theorem 1.1 suggests that the average number of solutions for a prime n = p ≥ m n=p\geq m is log 3 ⁡ p m ​ ( log ⁡ log ⁡ p) O ⁡ ( 1) \frac{\log^{3}p}{m}(\log\log p)^{O(1)}. If we ignore the log ⁡ log ⁡ p \log\log p factor and, as in [3, Remark 1.1] with the case m = 4 m=4, model the number of solutions at each prime p p as a Poisson process with intensity log 3 ⁡ p m \frac{\log^{3}p}{m}, we would expect any given prime p p to have “probability” exp ( − ( log p) 3 / m) \exp(-(\log p)^{3}/m) of having no solution. This would suggest that most primes p > exp ⁡ ( m 1 / 3 + ϵ) p>\exp(m^{1/3+\epsilon}) have solutions. It also indicates that there are many exceptional primes p > exp ⁡ ( m 1 / 2 − ϵ) p>\exp(m^{1/2-\epsilon}), while there are no exceptional primes p > exp ⁡ ( m 1 / 2 + ϵ) p>\exp(m^{1/2+\epsilon}), when m m is sufficiently large.

We also consider the more general question of whether m / n m/n can be represented as the sum of j j unit fractions, showing that there are somewhat large exceptional values here as well.

###### Theorem 1.4.

For each pair of positive integers j, k j,k, there is a number m ⁡ ( j, k) m(j,k) such that for each m ≥ m ⁡ ( j, k) m\geq m(j,k), we have m / ( k ​ m + 1) m/(km+1) not the sum of j j unit fractions.

In addition, we examine the Erdős–Straus–Schinzel conjecture numerically for various values of m m.

## 2. Some basic thoughts

For m, n ∈ ℕ m,n\in\mathbb{N}, we consider the equation

(2.1) |  | m n = 1 x + 1 y + 1 z. \frac{m}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}. |  |

We say that a solution ( x, y, z) ∈ ℕ 3 (x,y,z)\in\mathbb{N}^{3} of ( 2.1) is of Type I if n n divides x x but is coprime to y, z y,z, and of Type II if n n divides y, z y,z but is coprime to x x. Note that if n n is prime, n ∤ m n\nmid m and m ≥ 4 m\geq 4 then, up to permuting x, y, z x,y,z, every solution to ( 2.1) must be of Type I or Type II; this is not necessarily the case when n n is composite. For example, 5 / 6 = 1 / 3 + 1 / 4 + 1 / 4 5/6=1/3+1/4+1/4 is not of either type.

The following parametrizations of Type I and Type II solutions, as well as their proofs, follow the ideas in [3, Section 2], where the case m = 4 m=4 is treated. Also, see Aigner [1] and Nakayama [8].

###### Proposition 2.1.

Let n, m ∈ ℕ n,m\in\mathbb{N}. There exists a Type I solution ( x, y, z) ∈ ℕ 3 (x,y,z)\in\mathbb{N}^{3} of ( 2.1) if and only if there exist a, d, f ∈ ℕ a,d,f\in\mathbb{N} with f | m ​ a 2 ​ d + 1 f\mid ma^{2}d+1, m ​ a ​ d | n + f mad\mid n+f, and ( n + f) / m ​ a ​ d (n+f)/mad coprime to n n.

###### Proof.

First assume that there exist a, d, f ∈ ℕ a,d,f\in\mathbb{N} with f | m ​ a 2 ​ d + 1 f\mid ma^{2}d+1, m ​ a ​ d | n + f mad\mid n+f, and ( n + f) / m ​ a ​ d (n+f)/mad coprime to n n. Define e:= m ​ a 2 ​ d + 1 f ∈ ℕ e:=\frac{ma^{2}d+1}{f}\in\mathbb{N}, c:= n + f m ​ a ​ d ∈ ℕ c:=\frac{n+f}{mad}\in\mathbb{N}, so that c c is coprime to n n, and b:= c ​ e − a ∈ ℕ b:=ce-a\in\mathbb{N}, since c ​ e > a ce>a. Then one easily verifies that ( x, y, z):= ( a ​ b ​ d ​ n, a ​ c ​ d, b ​ c ​ d) (x,y,z):=(abdn,acd,bcd) satisfies ( 2.1), and that m ​ a ​ b ​ d = n ​ e + 1 mabd=ne+1, which implies gcd ⁡ ( n, a ​ b ​ d) = 1 \gcd(n,abd)=1. Since c c is also coprime to n n, so are y, z y,z, and the solution ( x, y, z) (x,y,z) is of Type I.

Conversely, assume that ( x, y, z) ∈ ℕ 3 (x,y,z)\in\mathbb{N}^{3} is a Type I solution of ( 2.1). We factor x = n ​ d ​ x ′ x=ndx^{\prime}, y = d ​ y ′ y=dy^{\prime}, z = d ​ z ′ z=dz^{\prime}, where gcd ⁡ ( x ′, y ′, z ′) = 1 \gcd(x^{\prime},y^{\prime},z^{\prime})=1. After multiplying ( 2.1) by n ​ d ​ x ′ ​ y ′ ​ z ′ ndx^{\prime}y^{\prime}z^{\prime}, we get

(2.2) |  | m ​ d ​ x ′ ​ y ′ ​ z ′ = y ′ ​ z ′ + n ​ x ′ ​ y ′ + n ​ x ′ ​ z ′. mdx^{\prime}y^{\prime}z^{\prime}=y^{\prime}z^{\prime}+nx^{\prime}y^{\prime}+nx^{\prime}z^{\prime}. |  |

As y ′, z ′ y^{\prime},z^{\prime} are coprime to n n, we conclude that

(2.3) |  | x ′ ∣ y ′ z ′, y ′ ∣ x ′ z ′, z ′ ∣ x ′ y ′. x^{\prime}\mid y^{\prime}z^{\prime},\quad y^{\prime}\mid x^{\prime}z^{\prime},\quad z^{\prime}\mid x^{\prime}y^{\prime}. |  |

We claim that this implies

(2.4) |  | x ′ = a ​ b, y ′ = a ​ c, z ′ = b ​ c, x^{\prime}=ab,\ y^{\prime}=ac,\ z^{\prime}=bc, |  |

where

 | a = gcd ⁡ ( x ′, y ′), b = gcd ⁡ ( x ′, z ′), c = gcd ⁡ ( y ′, z ′). a=\gcd(x^{\prime},y^{\prime}),\quad b=\gcd(x^{\prime},z^{\prime}),\quad c=\gcd(y^{\prime},z^{\prime}). |  |

Indeed, if a prime p p divides x ′ ​ y ′ ​ z ′ x^{\prime}y^{\prime}z^{\prime}, then gcd ⁡ ( x ′, y ′, z ′) = 1 \gcd(x^{\prime},y^{\prime},z^{\prime})=1 implies that (at least) one of x ′, y ′, z ′ x^{\prime},y^{\prime},z^{\prime} is not divisible by p p, while ( 2.3) implies that the other two, and hence their gcd \gcd, are divisible by the same power of p p. Substituting ( 2.4) into ( 2.2), we obtain

(2.5) |  | m ​ a ​ b ​ c ​ d = n ⁡ ( a + b) + c. mabcd=n(a+b)+c. |  |

As y, z y,z are coprime to n n, a ​ b ​ c ​ d abcd is coprime to n n and ( 2.5) shows that c | a + b c\mid a+b. Writing e:= a + b c ∈ ℕ e:=\frac{a+b}{c}\in\mathbb{N} and dividing ( 2.5) by c c, we have m ​ a ​ b ​ d = n ​ e + 1 mabd=ne+1. Define f:= m ​ a ​ c ​ d − n f:=macd-n, so that m ​ a ​ d | n + f mad\mid n+f. Since ( n + f) / m ​ a ​ d = c (n+f)/mad=c and c c is coprime to n n, so is ( n + f) / m ​ a ​ d (n+f)/mad. We have f | m ​ a 2 ​ d + 1 f\mid ma^{2}d+1, as

 | e ​ f = e ​ m ​ a ​ c ​ d − e ​ n = e ​ m ​ a ​ c ​ d − ( m ​ a ​ b ​ d − 1) = m ​ a ​ d ​ ( e ​ c − b) + 1 = m ​ a 2 ​ d + 1. ef=emacd-en=emacd-(mabd-1)=mad(ec-b)+1=ma^{2}d+1. |  |

∎

The condition that ( n + f) / m ​ a ​ d (n+f)/mad is coprime to n n is not necessary when m ≥ 4 m\geq 4 and n n is prime:

###### Corollary 2.2.

Let m ≥ 4 m\geq 4 and p p be prime. There exists a Type I solution ( x, y, z) ∈ ℕ 3 (x,y,z)\in\mathbb{N}^{3} of ( 2.1) with n = p n=p if and only if there exist a, d, f ∈ ℕ a,d,f\in\mathbb{N} with f | m ​ a 2 ​ d + 1 f\mid ma^{2}d+1 and m ​ a ​ d | p + f mad\mid p+f.

###### Proof.

Assuming there exist a, d, f ∈ ℕ a,d,f\in\mathbb{N} with f | m ​ a 2 ​ d + 1 f\mid ma^{2}d+1 and m ​ a ​ d | n + f mad\mid n+f, the solution ( x, y, z) (x,y,z) is constructed as in the proof of Proposition 2.1, and we find again that gcd ⁡ ( n, a ​ b ​ d) = 1 \gcd(n,abd)=1. Since n n is prime, if n n is not coprime to c c then n | c n\mid c, hence n | y n\mid y and n | z n\mid z, and 1 / x + 1 / y + 1 / z ≤ 3 / n < m / n 1/x+1/y+1/z\leq 3/n<m/n. Thus n n must be coprime to c c, gcd ⁡ ( n, a ​ b ​ c ​ d) = 1 \gcd(n,abcd)=1, and ( x, y, z) (x,y,z) is of Type I.

The converse follows from Proposition 2.1. ∎

###### Proposition 2.3.

Let n, m ∈ ℕ n,m\in\mathbb{N}. There exists a Type II solution ( x, y, z) ∈ ℕ 3 (x,y,z)\in\mathbb{N}^{3} of ( 2.1) if and only if there exist a, b, e ∈ ℕ a,b,e\in\mathbb{N} with e | a + b e\mid a+b, m ​ a ​ b | n + e mab\mid n+e, and ( n + e) / m (n+e)/m coprime to n n.

###### Proof.

First assume that there exist a, b, e ∈ ℕ a,b,e\in\mathbb{N} with e | a + b e\mid a+b and m ​ a ​ b | n + e mab\mid n+e, and ( n + e) / m (n+e)/m coprime to n n. Define c:= a + b e ∈ ℕ c:=\frac{a+b}{e}\in\mathbb{N} and d:= n + e m ​ a ​ b ∈ ℕ d:=\frac{n+e}{mab}\in\mathbb{N}. Then one easily verifies that ( x, y, z):= ( a ​ b ​ d, a ​ c ​ d ​ n, b ​ c ​ d ​ n) (x,y,z):=(abd,acdn,bcdn) satisfies ( 2.1). Since x:= a ​ b ​ d = ( n + e) / m x:=abd=(n+e)/m, x x is coprime to n n and ( x, y, z) (x,y,z) is a Type II solution.

Conversely, assume that ( x, y, z) ∈ ℕ 3 (x,y,z)\in\mathbb{N}^{3} is a Type II solution of ( 2.1). We factor x = d ​ x ′ x=dx^{\prime}, y = n ​ d ​ y ′ y=ndy^{\prime}, z = n ​ d ​ z ′ z=ndz^{\prime}, where gcd ⁡ ( x ′, y ′, z ′) = 1 \gcd(x^{\prime},y^{\prime},z^{\prime})=1. After multiplying ( 2.1) by n ​ d ​ x ′ ​ y ′ ​ z ′ ndx^{\prime}y^{\prime}z^{\prime}, we get

(2.6) |  | m ​ d ​ x ′ ​ y ′ ​ z ′ = n ​ y ′ ​ z ′ + x ′ ​ y ′ + x ′ ​ z ′. mdx^{\prime}y^{\prime}z^{\prime}=ny^{\prime}z^{\prime}+x^{\prime}y^{\prime}+x^{\prime}z^{\prime}. |  |

As x ′ x^{\prime} is coprime to n n, we conclude that x ′ | y ′ ​ z ′ x^{\prime}\mid y^{\prime}z^{\prime}, y ′ | x ′ ​ z ′ y^{\prime}\mid x^{\prime}z^{\prime}, z ′ | x ′ ​ y ′ z^{\prime}\mid x^{\prime}y^{\prime}. As in the proof of Proposition 2.1, this implies ( 2.4). Substituting ( 2.4) into ( 2.6), we obtain

(2.7) |  | m ​ a ​ b ​ c ​ d = a + b + n ​ c, mabcd=a+b+nc, |  |

which shows that c | a + b c\mid a+b. Define e:= a + b c ∈ ℕ e:=\frac{a+b}{c}\in\mathbb{N}, so that e | a + b e\mid a+b. Dividing ( 2.7) by c c, we have m ​ a ​ b ​ d = e + n, mabd=e+n, that is m ​ a ​ b | e + n mab\mid e+n. Since e + n m = a ​ b ​ d = x \frac{e+n}{m}=abd=x and x x is coprime to n n, so is e + n m \frac{e+n}{m}. ∎

The condition that ( n + e) / m (n+e)/m is coprime to n n is not necessary when m ≥ 4 m\geq 4 and n n is prime:

###### Corollary 2.4.

Let m ≥ 4 m\geq 4 and n n be prime. There exists a Type II solution ( x, y, z) ∈ ℕ 3 (x,y,z)\in\mathbb{N}^{3} of ( 2.1) if and only if there exist a, b, e ∈ ℕ a,b,e\in\mathbb{N} with e | a + b e\mid a+b and m ​ a ​ b | n + e mab\mid n+e.

###### Proof.

Assuming there exist a, b, e ∈ ℕ a,b,e\in\mathbb{N} with e | a + b e\mid a+b and m ​ a ​ b | n + e mab\mid n+e, the solution ( x, y, z) (x,y,z) is constructed as in the proof of Proposition 2.3. Since n n is prime, if n n is not coprime to x x then n | x n\mid x and 1 / x + 1 / y + 1 / z ≤ 3 / n < m / n 1/x+1/y+1/z\leq 3/n<m/n. Thus n n must be coprime to x x and ( x, y, z) (x,y,z) is of Type II.

The converse follows from Proposition 2.3. ∎

## 3. A lower bound for the number of exceptional primes

We will make use of the Brun–Titchmarsh inequality, which states that the number of primes up to N N that are congruent to a ( mod q) a\pmod{q} is

 | π ⁡ ( N, q, a) ≪ N φ ⁡ ( q) ​ log ⁡ ( N / q) ( q < N), \pi(N;q,a)\ll\frac{N}{\varphi(q)\log(N/q)}\qquad(q<N), |  |

where φ ⁡ ( q) \varphi(q) is the Euler totient function. We record ( 2.1) in the case that n = p n=p, a prime:

(3.1) |  | m p = 1 x + 1 y + 1 z. \frac{m}{p}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}. |  |

###### Theorem 3.1.

There is a constant c > 0 c>0, such that for every integer m ≥ 8 m\geq 8, there are more than

 | exp ⁡ { c ​ φ ​ ( m) 1 / 3 / ( log ⁡ m) 2 / 3 } \exp\{c\,\varphi(m)^{1/3}/(\log m)^{2/3}\} |  |

primes p p for which ( 3.1) has no solution in natural numbers x, y, z x,y,z.

The proof follows the ideas in [3, Sections 8, 9], generalizing from m = 4 m=4 to general m m.

###### Proof.

Note that ( 3.1) cannot be solved when p = 2, 3 p=2,3 for m = 8 m=8 and m ≥ 10 m\geq 10, nor when p = 2, 5 p=2,5 for m = 9 m=9, so we may assume that m m is large. When p p is prime, then all solutions to ( 3.1) are of Type I or Type II, as discussed above. If ( x, y, z) (x,y,z) is a solution to ( 3.1) of Type I, Corollary 2.2 shows that there are natural numbers a, d, f a,d,f such that

 | p ≡ − f ( mod m ​ a ​ d), f ∣ m a 2 d + 1. p\equiv-f\pmod{mad},\qquad f\mid ma^{2}d+1. |  |

By Lemma 7.4, the modulus satisfies m ​ a ​ d ≤ 3 ​ p ≤ 3 ​ N mad\leq 3p\leq 3N, provided p ≤ N p\leq N. For given m, a, d, f m,a,d,f, the number of primes p ≤ N p\leq N satisfying p ≡ − f ( mod m ​ a ​ d) p\equiv-f\pmod{mad} is

 | ≪ N φ ⁡ ( m ​ a ​ d) ​ log ⁡ ( 2 + N m ​ a ​ d) ≤ N φ ⁡ ( m) ​ φ ​ ( a ​ d) ​ log ⁡ ( 2 + N m ​ a ​ d). \ll\frac{N}{\varphi(mad)\log(2+\frac{N}{mad})}\leq\frac{N}{\varphi(m)\varphi(ad)\log(2+\frac{N}{mad})}. |  |

This follows from Brun–Titchmarsh when m ​ a ​ d ≤ N / 2 mad\leq N/2, while the count is clearly O ⁡ ( 1) O(1) if N / 2 < m ​ a ​ d ≤ 3 ​ N N/2<mad\leq 3N. The number of p ≤ N p\leq N covered by these congruences, by varying the parameters a, d, f a,d,f, is

(3.2) |  | ≪ N φ ⁡ ( m) ∑ a, d: a ​ d ≤ 3 ​ N / m τ ⁡ ( m ​ a 2 ​ d + 1) φ ⁡ ( a ​ d) ​ log ⁡ ( 2 + N m ​ a ​ d). \ll\frac{N}{\varphi(m)}\sum_{a,d:ad\leq 3N/m}\frac{\tau(ma^{2}d+1)}{\varphi(ad)\log(2+\frac{N}{mad})}. |  |

The analogue of the estimate [3, Eq. (8.2)] is

(3.3) |  | ∑ a, d: X / 2 ≤ a ​ d ≤ X τ ⁡ ( m ​ a 2 ​ d + 1) φ ⁡ ( a ​ d) ≪ log 2 X log m ( X, m ≥ 2, m ≪ X O ⁡ ( 1)), \sum_{a,d:X/2\leq ad\leq X}\frac{\tau(ma^{2}d+1)}{\varphi(ad)}\ll\log^{2}X\log m\qquad(X,m\geq 2,\ m\ll X^{O(1)}), |  |

which is proved just like in [3] with m m replacing 4 4. Splitting the sum in ( 3.2) into dyadic intervals 3 ​ N m ​ 2 − j − 1 ≤ a ​ d ≤ 3 ​ N m ​ 2 − j \frac{3N}{m}2^{-j-1}\leq ad\leq\frac{3N}{m}2^{-j}, the contribution to ( 3.2) from j j with m 1 / 6 ≤ 3 ​ N m ​ 2 − j m^{1/6}\leq\frac{3N}{m}2^{-j} is

 | ≪ N φ ⁡ ( m) ​ log 2 ​ N ​ log ⁡ m ​ ∑ j ≪ log ⁡ N 1 j ≪ N φ ⁡ ( m) ​ log 2 ​ N ​ log ⁡ log ⁡ N ​ log ​ m, \ll\frac{N}{\varphi(m)}\log^{2}N\log m\sum_{j\ll\log N}\frac{1}{j}\ll\frac{N}{\varphi(m)}\log^{2}N\log\log N\log m, |  |

by ( 3.3). Since τ ⁡ ( m ​ a 2 ​ d + 1) ≪ ( m ​ a ​ d) 1 / 6 \tau(ma^{2}d+1)\ll(mad)^{1/6}, the contribution to ( 3.2) from j j with m 1 / 6 > 3 ​ N m ​ 2 − j m^{1/6}>\frac{3N}{m}2^{-j}, that is a ​ d < m 1 / 6 ad<m^{1/6}, is

 | ≪ N φ ⁡ ( m) ∑ a, d: a ​ d ≤ m 1 / 6 m 1 / 6 ≪ N φ ⁡ ( m) m 1 / 2. \ll\frac{N}{\varphi(m)}\sum_{a,d:ad\leq m^{1/6}}m^{1/6}\ll\frac{N}{\varphi(m)}m^{1/2}. |  |

Assuming that N N is chosen so that e m 1 / 4 ≪ N < e m e^{m^{1/4}}\ll N<e^{m}, the expression in ( 3.2), and hence the number of primes p ≤ N p\leq N covered by Type I solutions, is

 | ≪ N φ ⁡ ( m) ​ log 2 ​ N ​ log 2 ​ m. \ll\frac{N}{\varphi(m)}\log^{2}N\log^{2}m. |  |

We now specify N = N ⁡ ( m) N=N(m) as the solution to

 | φ ⁡ ( m) / log 2 ⁡ m = C ​ log 3 ​ N, \varphi(m)/\log^{2}m=C\log^{3}N, |  |

for some sufficiently large constant C C, noting that this is consistent with e m 1 / 4 ≪ N < e m e^{m^{1/4}}\ll N<e^{m} when C ≥ 1 C\geq 1. Then most primes p ∈ ( N / 2, N] p\in(N/2,N] are not covered by these congruences, and thus have no Type I solution to ( 3.1).

It remains to count the number of primes p ≤ N p\leq N covered by Type II solutions. If ( x, y, z) (x,y,z) is a solution to ( 3.1) of Type II, Corollary 2.4 shows that there are natural numbers a, b, e a,b,e with

 | p ≡ − e ( mod m ​ a ​ b), e ∣ a + b. p\equiv-e\pmod{mab},\qquad e\mid a+b. |  |

Note that gcd ⁡ ( a, b) = 1 \gcd(a,b)=1 follows from gcd ⁡ ( x ′, y ′, z ′) = 1 \gcd(x^{\prime},y^{\prime},z^{\prime})=1 in the proof of Proposition 2.3. Since e | a + b e\mid a+b, we have e ≤ a + b ≤ 2 ​ a ​ b e\leq a+b\leq 2ab. And m ​ a ​ b | p + e mab\mid p+e implies m ​ a ​ b ≤ p + e ≤ p + 2 ​ a ​ b mab\leq p+e\leq p+2ab, so ( m − 2) ​ a ​ b ≤ p (m-2)ab\leq p and

(3.4) |  | m ​ a ​ b ≤ p ​ m m − 2 ≤ 2 ​ p ≤ 2 ​ N. mab\leq p\frac{m}{m-2}\leq 2p\leq 2N. |  |

For given m, a, b, e m,a,b,e, the number of primes p ≤ N p\leq N satisfying p ≡ − e ( mod m ​ a ​ b) p\equiv-e\pmod{mab} is

 | ≪ N φ ⁡ ( m ​ a ​ b) ​ log ⁡ ( 2 + N m ​ a ​ b) ≤ N φ ⁡ ( m) ​ φ ​ ( a ​ b) ​ log ⁡ ( 2 + N m ​ a ​ b), \ll\frac{N}{\varphi(mab)\log(2+\frac{N}{mab})}\leq\frac{N}{\varphi(m)\varphi(ab)\log(2+\frac{N}{mab})}, |  |

again by Brun–Titchmarsh if m ​ a ​ b ≤ N / 2 mab\leq N/2 and trivially if N / 2 < m ​ a ​ b ≤ 2 ​ N N/2<mab\leq 2N. The number of primes p ≤ N p\leq N that can be covered by these congruences, by varying the parameters a, b, e a,b,e, is

 | ≪ N φ ⁡ ( m) ∑ a, b: a ​ b ≤ 2 ​ N / m ( a, b) = 1 τ ⁡ ( a + b) φ ⁡ ( a ​ b) ​ log ⁡ ( 2 + N m ​ a ​ b). \ll\frac{N}{\varphi(m)}\sum_{a,b:ab\leq 2N/m\atop(a,b)=1}\frac{\tau(a+b)}{\varphi(ab)\log(2+\frac{N}{mab})}. |  |

Splitting this sum into dyadic intervals 2 j − 1 < N m ​ a ​ b ≤ 2 j 2^{j-1}<\frac{N}{mab}\leq 2^{j}, and estimating the resulting sums as in the last paragraph of [3, Section 9], we find that the number of primes p ≤ N p\leq N covered by these congruences is

 | ≪ N φ ⁡ ( m) ​ log 2 ​ N ​ log ⁡ log ⁡ N. \ll\frac{N}{\varphi(m)}\log^{2}N\log\log N. |  |

Thus, most primes p ∈ ( N / 2, N] p\in(N/2,N] are covered neither by Type I nor by Type II congruences if φ ⁡ ( m) / log 2 ⁡ m = C ​ log 3 ​ N \varphi(m)/\log^{2}m=C\log^{3}N and C C is large enough, that is

 | N = exp ⁡ { ( φ ⁡ ( m) / C ​ log 2 ​ m) 1 / 3 }. N=\exp\{(\varphi(m)/C\log^{2}m)^{1/3}\}. |  |

The result now follows with c = 1 / ( 2 ​ C 1 / 3) c=1/(2C^{1/3}), since we have N 4 ​ log ⁡ N > N = exp ⁡ { c ​ ( φ ⁡ ( m) / log 2 ⁡ m) 1 / 3 } \frac{N}{4\log N}>\sqrt{N}=\exp\{c(\varphi(m)/\log^{2}m)^{1/3}\}. ∎

To see Theorem 1.1, since φ ⁡ ( m) ≫ m / log ⁡ log ⁡ m \varphi(m)\gg m/\log\log m, it follows from Theorem 3.1 that for each ϵ > 0 \epsilon>0 and m ≥ m ⁡ ( ϵ) m\geq m(\epsilon), we have more than exp ⁡ ( m 1 / 3 − ϵ) \exp(m^{1/3-\epsilon}) primes p p where ( 3.1) has no solution.

## 4. An upper bound

In this section we prove Theorem 1.3. Our proof largely follows the argument in Vaughan [12].

For m ≥ 4 m\geq 4 and a prime p ≡ − 1 ( mod m) p\equiv-1\pmod{m}, let f ​ ( p) = f m ​ ( p) f(p)=f_{m}(p) denote the greatest integer that is at most

(4.1) |  | 1 2 ​ ∑ t | ( p + 1) / m | μ ⁡ ( t) | ​ τ ​ ( p + 1 t ​ m). \frac{1}{2}\sum_{t\,|\,(p+1)/m}|\mu(t)|\tau\Big(\frac{p+1}{tm}\Big). |  |

For other primes p p we let f ⁡ ( p) = 0 f(p)=0. As shown in [12] for each p p there are at least f ⁡ ( p) f(p) residue classes mod p p such that if n n lies in one of them, then m / n m/n is a sum of 3 unit fractions.

The strategy is to use the large sieve to show that the number of n ≤ N n\leq N lying outside of these f ⁡ ( p) f(p) residue classes mod p p for each p p is bounded above by the bound in Theorem 1.3. To achieve this, we first establish the following lemma.

###### Lemma 4.1.

For m ≤ ( log ⁡ x) O ⁡ ( 1) m\leq(\log x)^{O(1)} we have

 | ∑ p ≤ x f ⁡ ( p) p ≍ 1 φ ⁡ ( m) ​ ( log ⁡ x) 2. \sum_{p\leq x}\frac{f(p)}{p}\asymp\frac{1}{\varphi(m)}(\log x)^{2}. |  |

###### Proof.

Via partial summation it suffices to show that

(4.2) |  | ∑ p ≤ x f ⁡ ( p) ≍ 1 φ ⁡ ( m) ​ x ​ log ⁡ x. \sum_{p\leq x}f(p)\asymp\frac{1}{\varphi(m)}x\log x. |  |

For the upper bound we use the simple inequality

 | τ 3 ​ ( n) ≤ 3 ​ ∑ d | n d ≤ n 2 / 3 τ ⁡ ( d), \tau_{3}(n)\leq 3\sum_{\begin{subarray}{c}d\,|\,n\\ d\leq n^{2/3}\end{subarray}}\tau(d), |  |

where τ 3 ​ ( n) \tau_{3}(n) is the number of triples a, b, c a,b,c of integers with a ​ b ​ c = n abc=n (cf. Koukoulopoulos [6, Ex. 20.2]). Then for a prime p ≡ − 1 ( mod m) p\equiv-1\pmod{m},

 | f ⁡ ( p) < τ 3 ​ ( ( p + 1) / m) ≤ 3 ​ ∑ d | ( p + 1) / m d ≤ p 2 / 3 τ ⁡ ( d). f(p)<\tau_{3}((p+1)/m)\leq 3\sum_{\begin{subarray}{c}d\,|\,(p+1)/m\\ d\leq p^{2/3}\end{subarray}}\tau(d). |  |

Thus, via the Brun–Titchmarsh inequality and our upper bound on m m,

 | ∑ p ≤ x f ⁡ ( p) \displaystyle\sum_{p\leq x}f(p) | ≪ ∑ d ≤ x 2 / 3 τ ⁡ ( d) ​ π ​ ( x, d ​ m, − 1) ≪ ∑ d ≤ x 2 / 3 x ​ τ ​ ( d) φ ⁡ ( d ​ m) ​ log ⁡ x \displaystyle\ll\sum_{d\leq x^{2/3}}\tau(d)\pi(x;dm,-1)\ll\sum_{d\leq x^{2/3}}\frac{x\tau(d)}{\varphi(dm)\log x} |  |

 |  | ≤ x φ ⁡ ( m) ​ log ⁡ x ​ ∑ d ≤ x 2 / 3 τ ⁡ ( d) φ ⁡ ( d) ≪ 1 φ ⁡ ( m) ​ x ​ log ⁡ x. \displaystyle\leq\frac{x}{\varphi(m)\log x}\sum_{d\leq x^{2/3}}\frac{\tau(d)}{\varphi(d)}\ll\frac{1}{\varphi(m)}x\log x. |  |

For the lower bound first note that for an integer n ≥ 2 n\geq 2, one has ⌊ n / 2 ⌋ ≥ n / 3 \lfloor n/2\rfloor\geq n/3. If p ≡ − 1 ( mod m) p\equiv-1\pmod{m} and p + 1 > m p+1>m, then the sum in ( 4.1) is ≥ 2 \geq 2, so that

 | ∑ p ≤ x f ⁡ ( p) \displaystyle\sum_{p\leq x}f(p) | ≥ 1 3 ​ ∑ p ≤ x p ≡ − 1 ( mod m) p + 1 > m ∑ d ​ t | ( p + 1) / m | μ ⁡ ( t) | \displaystyle\geq\frac{1}{3}\sum_{\begin{subarray}{c}p\leq x\\ p\,\equiv\,-1\pmod{m}\\ p+1>m\end{subarray}}\sum_{dt\,|\,(p+1)/m}|\mu(t)| |  |

 |  | ≥ 1 3 ​ ∑ d, t ≤ x 1 / 6 d ​ t > 1 | μ ⁡ ( t) | ​ ∑ p ≤ x p ≡ − 1 ( mod m ​ d ​ t) 1 \displaystyle\geq\frac{1}{3}\sum_{\begin{subarray}{c}d,t\leq x^{1/6}\\ dt>1\end{subarray}}|\mu(t)|\sum_{\begin{subarray}{c}p\leq x\\ p\,\equiv\,-1\kern-5.0pt\pmod{mdt}\end{subarray}}1 |  |

 |  | ≥ 1 3 ​ ∑ d, t ≤ x 1 / 6 1 ≤ Ω ⁡ ( d ​ t) ≤ 3 ​ log ⁡ log ⁡ x | μ ⁡ ( t) | ​ ∑ p ≤ x p ≡ − 1 ( mod m ​ d ​ t) 1, \displaystyle\geq\frac{1}{3}\sum_{\begin{subarray}{c}d,t\leq x^{1/6}\\ 1\leq\Omega(dt)\leq 3\log\log x\end{subarray}}|\mu(t)|\sum_{\begin{subarray}{c}p\leq x\\ p\,\equiv\,-1\kern-5.0pt\pmod{mdt}\end{subarray}}1, |  |

where Ω ⁡ ( n) \Omega(n) is the total number of prime factors of n n with multiplicity. We now use the Bombieri–Vinogradov theorem noting that the number of triples m, d, t m,d,t with given product q q is at most ( log ⁡ x) O ⁡ ( 1) (\log x)^{O(1)}. Thus,

 | ∑ p ≤ x f ⁡ ( p) ≫ ∑ d, t ≤ x 1 / 6 1 ≤ Ω ⁡ ( d ​ t) ≤ 3 ​ log ⁡ log ⁡ x | μ ⁡ ( t) | ​ x φ ⁡ ( m ​ d ​ t) ​ log ⁡ x ≫ 1 φ ⁡ ( m) ​ x ​ log ⁡ x, \sum_{p\leq x}f(p)\gg\sum_{\begin{subarray}{c}d,t\leq x^{1/6}\\ 1\leq\Omega(dt)\leq 3\log\log x\end{subarray}}\frac{|\mu(t)|x}{\varphi(mdt)\log x}\gg\frac{1}{\varphi(m)}x\log x, |  |

completing the proof of ( 4.2) and the lemma. ∎

Let N N be large, let X ≤ N 1 / 2 X\leq N^{1/2} be a quantity specified later, and let P = ∏ p ≤ X p P=\prod_{p\leq X}p. We now employ the large sieve. Let

 | S = ∑ s ≤ N 1 / 2 s | P | μ ⁡ ( s) | ​ ∏ p | s f ⁡ ( p) p − f ⁡ ( p). S=\sum_{\begin{subarray}{c}s\leq N^{1/2}\\ s\,|\,P\end{subarray}}|\mu(s)|\prod_{p\,|\,s}\frac{f(p)}{p-f(p)}. |  |

The number of n ≤ N n\leq N that avoid the f ⁡ ( p) f(p) residue classes mod p p for each p ≤ X p\leq X is bounded above by 4 ​ N / S 4N/S, so our task is to get a lower bound for S S.

Let

 | G = ∑ s | P ∏ p | s f ⁡ ( p) p − f ⁡ ( p). G=\sum_{s\,|\,P}\prod_{p\,|\,s}\frac{f(p)}{p-f(p)}. |  |

For any v ≥ 0 v\geq 0,

 | G − S = ∑ s > N 1 / 2 s | P ∏ p | s f ⁡ ( p) p − f ⁡ ( p) ≤ N − v / 2 ∑ s | P s v ∏ p | s f ⁡ ( p) p − f ⁡ ( p). G-S=\sum_{\begin{subarray}{c}s>N^{1/2}\\ s\,|\,P\end{subarray}}\prod_{p\,|\,s}\frac{f(p)}{p-f(p)}\\ \leq N^{-v/2}\sum_{s\,|\,P}s^{v}\prod_{p\,|\,s}\frac{f(p)}{p-f(p)}. |  |

Thus,

 | G − S G \displaystyle\frac{G-S}{G} | ≤ N − v / 2 ∏ p ≤ X ( 1 + p v f ⁡ ( p) p − f ⁡ ( p)) ( p − f ⁡ ( p) p) \displaystyle\leq N^{-v/2}\prod_{p\leq X}\Big(1+p^{v}\frac{f(p)}{p-f(p)}\Big)\Big(\frac{p-f(p)}{p}\Big) |  |

 |  | = N − v / 2 ∏ p ≤ X ( 1 + ( p v − 1) ​ f ​ ( p) p). \displaystyle=N^{-v/2}\prod_{p\leq X}\Big(1+\frac{(p^{v}-1)f(p)}{p}\Big). |  |

We choose v = 1 / log ⁡ X v=1/\log X, so that

 | G − S G \displaystyle\frac{G-S}{G} | ≤ exp ⁡ ( − log ⁡ N 2 ​ log ⁡ X + ∑ p ≤ X ( e − 1) ​ f ​ ( p) p) \displaystyle\leq\exp\Big(-\frac{\log N}{2\log X}+\sum_{p\leq X}\frac{(e-1)f(p)}{p}\Big) |  |

 |  | ≤ exp ⁡ ( − log ⁡ N 2 ​ log ⁡ X + ( e − 1) ​ C 2 φ ⁡ ( m) ​ log 2 ​ X), \displaystyle\leq\exp\Big(-\frac{\log N}{2\log X}+\frac{(e-1)C_{2}}{\varphi(m)}\log^{2}X\Big), |  |

where C 2 C_{2} is the upper bound constant implied in Lemma 4.1. Let

 | A = 1 2 ​ ( φ ⁡ ( m) ( e − 1) ​ C 2) 1 / 3 A=\frac{1}{2}\Big(\frac{\varphi(m)}{(e-1)C_{2}}\Big)^{1/3} |  |

and choose

 | X = exp ⁡ ( A ​ ( log ⁡ N) 1 / 3). X=\exp\big(A(\log N)^{1/3}\big). |  |

Then

 | G − S G \displaystyle\frac{G-S}{G} | ≤ exp ⁡ ( − 1 2 ​ A ​ ( log ⁡ N) 2 / 3 + 1 8 ​ A ​ ( log ⁡ N) 2 / 3) \displaystyle\leq\exp\Big(-\frac{1}{2A}(\log N)^{2/3}+\frac{1}{8A}(\log N)^{2/3}\Big) |  |

 |  | < exp ⁡ ( − 1 4 ​ A ​ ( log ⁡ N) 2 / 3). \displaystyle<\exp\Big(-\frac{1}{4A}(\log N)^{2/3}\Big). |  |

We may assume this last expression is < 1 / 2 <1/2, else the theorem holds trivially, so S > G / 2 S>G/2. But

 | G ≥ exp ⁡ ( ∑ p ≤ X f ⁡ ( p) p) ≥ exp ⁡ ( C 1 φ ⁡ ( m) ​ ( log ⁡ X) 2), G\geq\exp\Big(\sum_{p\leq X}\frac{f(p)}{p}\Big)\geq\exp\Big(\frac{C_{1}}{\varphi(m)}(\log X)^{2}\Big), |  |

where C 1 C_{1} is the constant in the lower bound implicit in Lemma 4.1. Putting in our choice for X X we have

 | 4 ​ N S ≪ N G ≤ N / exp ⁡ ( C 1 ​ A 2 φ ⁡ ( m) ​ ( log ⁡ N) 2 / 3). \frac{4N}{S}\ll\frac{N}{G}\leq N/\exp\Big(\frac{C_{1}A^{2}}{\varphi(m)}(\log N)^{2/3}\Big). |  |

It remains to note that A 2 / φ ⁡ ( m) ≍ 1 / φ ​ ( m) 1 / 3 A^{2}/\varphi(m)\asymp 1/\varphi(m)^{1/3}, completing our argument for Theorem 1.3.

## 5. The general case

In this section we prove Theorem 1.4.

Let a 1 > a 2 > … a_{1}>a_{2}>\dots be a sequence of real numbers with lim a n = 0 \lim a_{n}=0 and let 𝒜 = { a 1, a 2, … } \mathcal{A}=\{a_{1},a_{2},\dots\}. For each positive integer j j, let V j V_{j} denote the subset of 𝒜 j \mathcal{A}^{j} where the coordinates form a monotone non-increasing sequence. Further let T j T_{j} be the subset of ( 𝒜 ∪ { 0 }) j (\mathcal{A}\cup\{0\})^{j} again with the coordinates non-increasing. For v ∈ T j v\in T_{j}, let s ⁡ ( v) s(v) denote the sum of the coordinates of v v, and let S j = s ⁡ ( V j) S_{j}=s(V_{j}).

###### Lemma 5.1.

For j ≥ 1 j\geq 1, the set of limit points of V j V_{j} is T j ∖ V j T_{j}\setminus V_{j}.

###### Proof.

Suppose ( v n) (v_{n}) is an infinite sequence of distinct members of V j V_{j} with lim v n = w \lim v_{n}=w. Let v n = ( a n, 1, …, a n, j) v_{n}=(a_{n,1},\dots,a_{n,j}). The sequence ( a n, j) n (a_{n,j})_{n} is either eventually constant or has limit 0. The first option cannot occur since otherwise there are only finitely many choices for the vectors v n v_{n}. Next, we consider ( a n, j − 1) n (a_{n,j-1})_{n} and here both options are possible. But if it is eventually constant, then all earlier coordinates of the vectors v ⁡ ( s n) v(s_{n}) likewise become eventually constant. Continuing in this manner, we have that v n v_{n} converges to a vector w ∈ T j w\in T_{j} with last coordinate 0, i.e., w ∈ T j ∖ V j w\in T_{j}\setminus V_{j}.

Conversely, if t ∈ T j t\in T_{j} with last coordinate 0, let t = ( t 1, …, t k, 0, …, 0) t=(t_{1},\dots,t_{k},0,\dots,0), where t 1, …, t k ∈ 𝒜 t_{1},\dots,t_{k}\in\mathcal{A} and k < j k<j. Suppose that t k = a m t_{k}=a_{m}. Replacing each of the 0’s with a m + n a_{m+n}, we then have a sequence of vectors t n ∈ V j t_{n}\in V_{j} that converges to t t. This completes the proof. ∎

###### Lemma 5.2.

For each positive integer j j and each positive real x x there is a positive number ϵ \epsilon, depending on the choice of j j, x x and sequence ( a n) (a_{n}), such that the interval ( x − ϵ, x) (x-\epsilon,x) contains no member of S j S_{j}.

###### Proof.

For each fixed j j there is no infinite strictly increasing sequence made up of members of S j S_{j}. To see this, we suppose such a sequence ( s n) (s_{n}) exists and let s n = s ⁡ ( v n) s_{n}=s(v_{n}). Write v n = ( a n, 1, …, a n, j) v_{n}=(a_{n,1},\dots,a_{n,j}). Each of the sequences ( a n, i) n (a_{n,i})_{n} has 0 as a limit point or it repeats some nonzero number infinitely often, so by passing to an infinite subsequence we may assume that either the sequence of i i th coordinates is constant or has limit 0, and this holds for each i i. These possibilities are incompatible with s ⁡ ( v n) s(v_{n}) strictly increasing, which proves that no infinite strictly increasing sequence can be formed from the elements of S j S_{j}. Thus, the assertion in the lemma holds. ∎

We now specify that the numbers a i a_{i} are unit fractions. To prove Theorem 1.4, we use the lemmas with a i = 1 / i a_{i}=1/i, and note that there is some ϵ > 0 \epsilon>0, depending on the choice of k, j k,j, such that ( 1 / k − ϵ, 1 / k) (1/k-\epsilon,1/k) contains no member of S j S_{j}. However, for m m sufficiently large,

 | m / ( k ​ m + 1) = 1 / ( k + 1 / m) m/(km+1)=1/(k+1/m) |  |

is in this interval, so it must be that that m / ( k ​ m + 1) ∉ S j m/(km+1)\notin S_{j}. This completes the proof of Theorem 1.4.

## 6. Empirical data

The original Erdős–Straus conjecture was verified up to 10 17 10^{17} by Salez [11], and this was recently improved to 10 18 10^{18} by Mihnea–Dumitru [7]. By sifting with the seven congruences in [3, Proposition 1.9], with 4 replaced by m m, we have verified the m = 5 m=5 case up to 10 18 10^{18}, the m = 6, 7, 8 m=6,7,8 cases up to 10 13 10^{13}, and the m = 9, …, 15 m=9,\dots,15 cases up to 10 12 10^{12}, with the noted exceptions found. This sifting was done only with primes, and then composites made up of exceptional primes were checked directly. In all the cases any other exceptional n n, if they exist, must exceed the stated N N. See Table 1.

In addition, with the help of a computer we verified that the claim in Theorem 1.2 also holds for all m ∈ [16, 30000] m\in[16,30000], except m = 19 m=19. Note too that from Table 1 we see that it holds for m = 10 m=10 and m ∈ [12, 15] m\in[12,15]. We conjecture that for every m ≥ 20 m\geq 20 there is a prime p ∈ ( m 2, 2 ​ m 2) p\in(m^{2},2m^{2}) for which m / p m/p is not the sum of 3 unit fractions.

m m | all exceptions n ≤ N n\leq N | Count | N N |

4 4 | 1 1 | 1 | 10 18 10^{18} [7] |

5 5 | 1 1 | 1 | 10 18 10^{18} |

6 6 | 1 1 | 1 | 10 13 10^{13} |

7 7 | 1, 2 1,2 | 2 | 10 13 10^{13} |

8 8 | 1, 2, 3, 11, 17, 131, 241 1,2,3,11,17,131,241 | 7 | 10 13 10^{13} |

9 9 | 1, 2, 5, 11, 19 1,2,5,11,19 | 5 | 10 12 10^{12} |

10 10 | 1, 2, 3, 7, 11, 43, 61, 67, 181 1,2,3,7,11,43,61,67,181 | 9 | 10 12 10^{12} |

11 11 | 1, 2, 3, 4, 37 1,2,3,4,37 | 5 | 10 12 10^{12} |

 | 1, 2, 3, 5, 7, 13, 25, 29, 31, 37, 73, 97, 193, 433, 1,2,3,5,7,13,25,29,31,37,73,97,193,433, |  |  |

12 12 | 577, 1129, 1657, 1873, 2521, 2593, 3433, 10369, 577,1129,1657,1873,2521,2593,3433,10369, | 24 | 10 12 10^{12} |

 | 12049, 12241 12049,12241 |  |  |

13 13 | 1, 2, 3, 4, 5, 7, 14, 53, 61, 67, 79, 211, 281 1,2,3,4,5,7,14,53,61,67,79,211,281 | 13 | 10 12 10^{12} |

14 14 | 1, 2, 3, 4, 5, 17, 19, 29, 59, 257, 353, 841 1,2,3,4,5,17,19,29,59,257,353,841 | 12 | 10 12 10^{12} |

 | 1, 2, 3, 4, 8, 16, 17, 19, 23, 31, 34, 47, 53, 61, 79, 1,2,3,4,8,16,17,19,23,31,34,47,53,61,79, |  |  |

15 15 | 113,122,137,151,197, 226, 233, 271, 541, 1103, 113,122,137,151,197,226,233,271,541,1103, | 32 | 10 12 10^{12} |

 | 1171, 1367, 4201, 6301, 12601, 16831, 20521 1171,1367,4201,6301,12601,16831,20521 |  |  |

Table 1. Values of n ≤ N n\leq N for which ( 3.1) has no solution.

## 7. Numerically explicit estimates: primes with Type I representations

Let τ ⁡ ( n) \tau(n) denote the number of divisors of n n and for j | 6 j\mid 6, let τ j ′ ​ ( n) \tau^{\prime}_{j}(n) denote the number of divisors d d of n n with gcd ⁡ ( d, 6) = j \gcd(d,6)=j. In the proof, we will make use of the following estimates.

###### Lemma 7.1.

For all integers n ≥ 2 n\geq 2 we have

 | τ ⁡ ( n) \displaystyle\tau(n) | ≤ 138.32 ​ ( n − 1) 1 / 6, \displaystyle\leq 138.32(n-1)^{1/6}, |  |

 | τ 1 ′ ​ ( n) \displaystyle\tau^{\prime}_{1}(n) | ≤ 16.2 ​ ( n − 1) 1 / 6, \displaystyle\leq 16.2(n-1)^{1/6}, |  |

 | τ 2 ′ ​ ( n) \displaystyle\tau^{\prime}_{2}(n) | ≤ 51.3 ​ ( n − 1) 1 / 6, \displaystyle\leq 51.3(n-1)^{1/6}, |  |

 | τ 3 ′ ​ ( n) \displaystyle\tau^{\prime}_{3}(n) | ≤ 32.3 ​ ( n − 1) 1 / 6, \displaystyle\leq 32.3(n-1)^{1/6}, |  |

 | τ 6 ′ ​ ( n) \displaystyle\tau^{\prime}_{6}(n) | ≤ 102.7 ​ ( n − 1) 1 / 6. \displaystyle\leq 102.7(n-1)^{1/6}. |  |

###### Proof.

First notice that τ ⁡ ( p a) / p a / 6 = ( a + 1) / p a / 6 ≤ 1 \tau(p^{a})/p^{a/6}=(a+1)/p^{a/6}\leq 1 unless p ≤ 61 p\leq 61. Further, for p ≤ 61 p\leq 61 we compute the integer a p a_{p} that maximizes ( a + 1) / p a / 6 (a+1)/p^{a/6}; these maximizing prime powers being

 | 2 8, 3 4, 5 3, 7 2, 11 2, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61. 2^{8},3^{4},5^{3},7^{2},11^{2},13,17,19,23,29,31,37,41,43,47,53,59,61. |  |

Thus, if u u is the product of these prime powers, then

 | τ ⁡ ( n) / n 1 / 6 ≤ τ ⁡ ( u) / u 1 / 6 < 138.313. \tau(n)/n^{1/6}\leq\tau(u)/u^{1/6}<138.313. |  |

To see the claimed inequality, note that 138.313 ​ n 1 / 6 < 138.32 ​ ( n − 1) 1 / 6 138.313n^{1/6}<138.32(n-1)^{1/6} for n ≥ 3294 n\geq 3294 and the assertion is easily checked for smaller values of n n. The inequalities for τ j ′ \tau^{\prime}_{j} are proved in a similar manner. ∎

We are aware that the exponent “ 1 / 6 1/6 ” here can be replaced with any fixed ϵ > 0 \epsilon>0 at the expense of larger coefficients, and there are even effective asymptotic estimates for the maximal order (see [9]), but the elementary Lemma 7.1 is optimal for our needs.

###### Lemma 7.2.

Let j | 6 j\,|\,6 and let n n be a positive integer. Among the divisors d d of n n with gcd ⁡ ( d, 6) = j \gcd(d,6)=j at most 1 2 ​ τ j ′ ​ ( n) \frac{1}{2}\tau^{\prime}_{j}(n) of them have d > j ​ n d>\sqrt{jn}.

###### Proof.

Write n = 2 i ​ 3 k ​ v n=2^{i}3^{k}v with gcd ⁡ ( v, 6) = 1 \gcd(v,6)=1 and i, k ≥ 0 i,k\geq 0. In the case j = 1 j=1 the divisors of n n coprime to 6 are precisely the divisors of v v, and among these at most half of them are > v >\sqrt{v}. But n ≥ v \sqrt{n}\geq\sqrt{v}, so the case j = 1 j=1 is proved. If j = 2 j=2 note that the divisors 2 ​ d 2d of n n coprime to 3, correspond to divisors d d of n / 2 n/2 coprime to 3 with at most half of these > 2 i − 1 ​ v >\sqrt{2^{i-1}v}. Note that 2 ​ d > 2 ​ n 2d>\sqrt{2n} implies that d > n / 2 ≥ 2 i − 1 ​ v d>\sqrt{n/2}\geq\sqrt{2^{i-1}v}. The other cases are proved similarly. ∎

###### Lemma 7.3.

For positive integers r ≤ k r\leq k, and for x ≥ r x\geq r, we have

 | ∑ n ≤ x n ≡ r ( mod k) n − α \displaystyle\sum_{\begin{subarray}{c}n\leq x\\ n\,\equiv\,r\kern-5.0pt\pmod{k}\end{subarray}}n^{-\alpha} | ≤ r − α + 1 k ​ ( 1 − α) − 1 ​ ( x 1 − α − r 1 − α), ( 0 ≤ α < 1), \displaystyle\leq r^{-\alpha}+\frac{1}{k}(1-\alpha)^{-1}(x^{1-\alpha}-r^{1-\alpha}),\qquad(0\leq\alpha<1), |  |

 | ∑ n ≤ x n ≡ r ( mod k) n α \displaystyle\sum_{\begin{subarray}{c}n\leq x\\ n\,\equiv\,r\kern-5.0pt\pmod{k}\end{subarray}}n^{\alpha} | < 1 k ⁡ ( 1 + α) ​ ( x + k) 1 + α, ( α > 0). \displaystyle<\frac{1}{k(1+\alpha)}(x+k)^{1+\alpha},\qquad(\alpha>0). |  |

###### Proof.

These inequalities are easy exercises. ∎

As discussed above, when p p is prime, p ∤ m p\,\nmid\,m and m ≥ 4 m\geq 4, then all solutions to ( 3.1) are of Type I or Type II. By Proposition 2.1, if ( x, y, z) (x,y,z) is a solution to ( 3.1) of Type I, there are natural numbers a, d, f a,d,f such that

 | p ≡ − f ( mod m ​ a ​ d), f ∣ m a 2 d + 1. p\equiv-f\pmod{mad},\qquad f\mid ma^{2}d+1. |  |

###### Lemma 7.4.

When p p has a Type I solution to ( 3.1) with m ≥ 4 m\geq 4, then m ​ a ​ d ≤ 2 ​ p + 1 mad\leq 2p+1.

###### Proof.

As in the proof of Proposition 2.1, we define the natural numbers e:= m ​ a 2 ​ d + 1 f e:=\frac{ma^{2}d+1}{f}, c:= p + f m ​ a ​ d c:=\frac{p+f}{mad}, b:= c ​ e − a b:=ce-a, where ( x, y, z) = ( a ​ b ​ d ​ p, a ​ c ​ d, b ​ c ​ d). (x,y,z)=(abdp,acd,bcd). We may assume y ≤ z y\leq z, i.e. a ≤ b a\leq b. Then c ​ e = a + b ≤ 2 ​ b ce=a+b\leq 2b and c ≤ 2 ​ b e = 2 e ​ f ​ b ​ f c\leq\frac{2b}{e}=\frac{2}{ef}bf. The definitions of e, c, b e,c,b imply that b ​ f = p ​ a + c bf=pa+c, so

 | b ​ f = p ​ a + c ≤ p ​ a + 2 e ​ f ​ b ​ f ≤ p ​ a + 2 m + 1 ​ b ​ f, bf=pa+c\leq pa+\frac{2}{ef}bf\leq pa+\frac{2}{m+1}bf, |  |

since e ​ f = m ​ a 2 ​ d + 1 ≥ m + 1 ef=ma^{2}d+1\geq m+1. Thus,

 | b ​ f ≤ p ​ a ​ m + 1 m − 1 bf\leq pa\frac{m+1}{m-1} |  |

and, since b ≥ a b\geq a,

 | f ≤ p ​ m + 1 m − 1. f\leq p\frac{m+1}{m-1}. |  |

Now

 | m ​ a ​ c ​ d = p + f ≤ p ​ 2 ​ m m − 1. macd=p+f\leq p\frac{2m}{m-1}. |  |

If c ≥ 2 c\geq 2, we obtain m ​ a ​ d ≤ p ​ m m − 1 < 2 ​ p mad\leq p\frac{m}{m-1}<2p. If c = 1 c=1, then b ​ f = p ​ a + c = p ​ a + 1 bf=pa+c=pa+1 and f = p ​ a / b + 1 / b ≤ p + 1 f=pa/b+1/b\leq p+1, so m ​ a ​ d = p + f ≤ 2 ​ p + 1 mad=p+f\leq 2p+1. ∎

For given m, a, d, f m,a,d,f, we wish to count the number of primes p ∈ ( N / 2, N] p\in(N/2,N] satisfying p ≡ − f ( mod m ​ a ​ d) p\equiv-f\pmod{mad}. We shall consider 4 cases depending on the value of gcd ⁡ ( f, 6) \gcd(f,6).

### 7.1. The case gcd ⁡ ( f, 6) = 1 \gcd(f,6)=1.

In this case, for given values of m, a, d m,a,d, we let f f run over the divisors of m ​ a 2 ​ d + 1 ma^{2}d+1 coprime to 6. The number of primes p ∈ ( N / 2, N] p\in(N/2,N] with p ≡ − f ( mod m ​ a ​ d) p\equiv-f\pmod{mad} is at most

 | ≤ ⌈ N 2 ​ m ​ a ​ d ⌉ ≤ ⌊ N 2 ​ m ​ a ​ d ⌋ + 1. \leq\left\lceil\frac{N}{2mad}\right\rceil\leq\left\lfloor\frac{N}{2mad}\right\rfloor+1. |  |

Thus, by Lemma 7.1, with κ 1 = 16.2 \kappa_{1}=16.2, the number of primes in this case is at most

 | ∑ m ​ a ​ d ≤ 2 ​ N + 1 \displaystyle\sum_{mad\leq 2N+1} | ( ⌊ N 2 ​ m ​ a ​ d ⌋ + 1) ​ τ 1 ′ ​ ( m ​ a 2 ​ d + 1) \displaystyle\left(\left\lfloor\frac{N}{2mad}\right\rfloor+1\right)\tau^{\prime}_{1}(ma^{2}d+1) |  |

 |  | ≤ κ 1 ​ N 2 ​ m 5 / 6 ∑ m ​ a ​ d ≤ N / 2 a − 2 / 3 d − 5 / 6 + ∑ m ​ a ​ d ≤ 2 ​ N + 1 τ 1 ′ ( m a 2 d + 1) \displaystyle\leq\frac{\kappa_{1}N}{2m^{5/6}}\sum_{mad\leq N/2}a^{-2/3}d^{-5/6}+\sum_{mad\leq 2N+1}\tau^{\prime}_{1}(ma^{2}d+1) |  |

 |  | = S 1, 1 + S 1, 2, \displaystyle=S_{1,1}+S_{1,2}, |  |

say, since ⌊ N / 2 ​ m ​ a ​ d ⌋ \lfloor N/2mad\rfloor vanishes unless m ​ a ​ d ≤ N / 2 mad\leq N/2. Thus, by Lemma 7.3,

 | S 1, 1 ≤ κ 1 ​ N 2 ​ m 5 / 6 ∑ d ≤ N / 2 ​ m 3 ( N 2 ​ m ​ d) 1 / 3 d − 5 / 6 < 3 ​ κ 1 ​ N 4 / 3 2 4 / 3 ​ m 7 / 6 ζ ( 7 / 6) < 127.1 N 4 / 3 m 7 / 6. S_{1,1}\leq\frac{\kappa_{1}N}{2m^{5/6}}\sum_{d\leq N/2m}3\Big(\frac{N}{2md}\Big)^{1/3}d^{-5/6}<\frac{3\kappa_{1}N^{4/3}}{2^{4/3}m^{7/6}}\zeta(7/6)<127.1\frac{N^{4/3}}{m^{7/6}}. |  |

We will work harder for S 1, 2 S_{1,2}. We first consider 2 cases: m ​ a ​ d > 1.01 ​ N mad>1.01N and m ​ a ​ d ≤ 1.01 ​ N mad\leq 1.01N. In the first case, since m ​ a ​ d ​ c − f ≤ N madc-f\leq N, we have f > N / 100 f>N/100. But m ​ a ​ d ≤ 2 ​ N + 1 mad\leq 2N+1, so we have f > m ​ a ​ d / 300 f>mad/300, and so

(7.1) |  | f 2 > m 2 ​ a 2 ​ d 2 10 5 > 10 ​ m ​ a 2 ​ d > 6 ​ ( m ​ a 2 ​ d + 1), f^{2}>\frac{m^{2}a^{2}d^{2}}{10^{5}}>10ma^{2}d>6(ma^{2}d+1), |  |

assuming m ≥ 10 9 m\geq 10^{9}, say. So, we are only considering divisors of m ​ a 2 ​ d + 1 ma^{2}d+1 larger than the square root. Thus, by Lemma 7.2,

(7.2) |  | S 1, 2 ≤ 1 2 ​ ∑ m ​ a ​ d ≤ 1.01 ​ N τ 1 ′ ​ ( m ​ a 2 ​ d + 1) + 1 2 ​ ∑ m ​ a ​ d ≤ 2 ​ N + 1 τ 1 ′ ​ ( m ​ a 2 ​ d + 1). S_{1,2}\leq\frac{1}{2}\sum_{mad\leq 1.01N}\tau^{\prime}_{1}(ma^{2}d+1)+\frac{1}{2}\sum_{mad\leq 2N+1}\tau^{\prime}_{1}(ma^{2}d+1). |  |

The two sums are computed similarly; let X X stand for either 1.01 ​ N 1.01N or 2 ​ N + 1 2N+1.

Considering first the case when a ≤ 100 a\leq 100, we have

 | 1 2 ​ ∑ a ≤ 100 ∑ d ≤ X / m ​ a τ 1 ′ ​ ( m ​ a 2 ​ d + 1) \displaystyle\frac{1}{2}\sum_{a\leq 100}\sum_{d\leq X/ma}\tau^{\prime}_{1}(ma^{2}d+1) | ≤ 1 2 ​ κ 1 ​ m 1 / 6 ​ ∑ a ≤ 100 a 1 / 3 ​ ∑ d ≤ X / m ​ a d 1 / 6 \displaystyle\leq\frac{1}{2}\kappa_{1}m^{1/6}\sum_{a\leq 100}a^{1/3}\sum_{d\leq X/ma}d^{1/6} |  |

 |  | ≤ 3 7 ​ κ 1 ​ m 1 / 6 ​ ∑ a ≤ 100 a 1 / 3 ​ ( X m ​ a + 1) 7 / 6 \displaystyle\leq\frac{3}{7}\kappa_{1}m^{1/6}\sum_{a\leq 100}a^{1/3}\Big(\frac{X}{ma}+1\Big)^{7/6} |  |

 |  | < 3 7 ​ κ 1 ​ m 1 / 6 ​ ∑ a ≤ 100 a 1 / 3 ​ ( 1.01 ​ X m ​ a) 7 / 6 \displaystyle<\frac{3}{7}\kappa_{1}m^{1/6}\sum_{a\leq 100}a^{1/3}\Big(\frac{1.01X}{ma}\Big)^{7/6} |  |

 |  | < 3 7 ​ κ 1 ​ ( 1.01 ​ X) 7 / 6 ​ m − 1 ​ 7.51. \displaystyle<\frac{3}{7}\kappa_{1}(1.01X)^{7/6}m^{-1}7.51. |  |

Here we directly computed the a a -sum and assumed that X > m 2 X>m^{2} and that m ≥ 10 9 m\geq 10^{9}. To this we will add the case a > 100 a>100:

 | 1 2 ​ ∑ a > 100 ∑ m ​ a ​ d ≤ X τ 1 ′ ​ ( m ​ a 2 ​ d + 1) \displaystyle\frac{1}{2}\sum_{a>100}\sum_{mad\leq X}\tau^{\prime}_{1}(ma^{2}d+1) | ≤ 1 2 ​ κ 1 ​ m 1 / 6 ​ ∑ d < X / 100 ​ m d 1 / 6 ​ ∑ 100 < a ≤ X / m ​ d a 1 / 3 \displaystyle\leq\frac{1}{2}\kappa_{1}m^{1/6}\sum_{d<X/100m}d^{1/6}\sum_{100<a\leq X/md}a^{1/3} |  |

 |  | ≤ 3 8 ​ κ 1 ​ m 1 / 6 ​ ∑ d < X / 100 ​ m d 1 / 6 ​ ( X m ​ d + 1) 4 / 3 \displaystyle\leq\frac{3}{8}\kappa_{1}m^{1/6}\sum_{d<X/100m}d^{1/6}\Big(\frac{X}{md}+1\Big)^{4/3} |  |

 |  | < 3 8 κ 1 ( 1.01 X) 4 / 3 m − 7 / 6 ζ ( 7 / 6). \displaystyle<\frac{3}{8}\kappa_{1}(1.01X)^{4/3}m^{-7/6}\zeta(7/6). |  |

Adding these 2 estimates, each for X = 1.01 ​ N X=1.01N and X = 2 ​ N + 1 X=2N+1, we get

 | S 1, 2 < 143.4 ​ N 4 / 3 m 7 / 6 + 171.8 ​ N 7 / 6 m. S_{1,2}<143.4\frac{N^{4/3}}{m^{7/6}}+171.8\frac{N^{7/6}}{m}. |  |

So, our estimate in the case that f f is coprime to 6 is

 | S 1, 1 + S 1, 2 \displaystyle S_{1,1}+S_{1,2} | < 270.5 ​ N 4 / 3 m 7 / 6 + 171.8 ​ N 7 / 6 m \displaystyle<270.5\frac{N^{4/3}}{m^{7/6}}+171.8\frac{N^{7/6}}{m} |  |

 |  | = ( 270.5 + 171.8 ( N / m) 1 / 6) ​ N 4 / 3 m 7 / 6 < 276 ​ N 4 / 3 m 7 / 6, \displaystyle=\Big(270.5+\frac{171.8}{(N/m)^{1/6}}\Big)\frac{N^{4/3}}{m^{7/6}}<276\frac{N^{4/3}}{m^{7/6}}, |  |

assuming that N > m 2 N>m^{2} and m ≥ 10 9 m\geq 10^{9}.

### 7.2. The case gcd ⁡ ( f, 6) = 2 \gcd(f,6)=2.

If 6 | m 6\mid m, then we must have f f coprime to 6 (else m ​ a ​ d ​ c − f madc-f is not prime), so this last estimate stands for our bound for Type I solutions. Otherwise we have more work to do. In the current case f f is even, so that we only consider values of m, a, d, c m,a,d,c that are all odd. For given values of m, a, d m,a,d, the number of odd integers c c that place m ​ a ​ d ​ c madc in a half-open interval of length N / 2 N/2 is at most ⌈ N / 4 ​ m ​ a ​ d ⌉ \lceil N/4mad\rceil. Thus, the count for Type I primes in this case is at most

 | ∑ m ​ a ​ d ≤ 2 ​ N + 1 a ​ d ​ odd \displaystyle\sum_{\begin{subarray}{c}mad\leq 2N+1\\ ad~{\rm odd}\end{subarray}} | ⌈ N 4 ​ m ​ a ​ d ⌉ ​ τ 2 ′ ​ ( m ​ a 2 ​ d + 1) \displaystyle\left\lceil\frac{N}{4mad}\right\rceil\tau^{\prime}_{2}(ma^{2}d+1) |  |

 | ≤ \displaystyle\leq | κ 2 ​ ∑ m ​ a ​ d ≤ N / 4 a ​ d ​ odd N 4 ​ m ​ a ​ d ​ m 1 / 6 ​ a 1 / 3 ​ d 1 / 6 + κ 2 ​ ∑ m ​ a ​ d ≤ 2 ​ N + 1 a ​ d ​ odd m 1 / 6 ​ a 1 / 3 ​ d 1 / 6 \displaystyle\kappa_{2}\sum_{\begin{subarray}{c}mad\leq N/4\\ ad~{\rm odd}\end{subarray}}\frac{N}{4mad}m^{1/6}a^{1/3}d^{1/6}+\kappa_{2}\sum_{\begin{subarray}{c}mad\leq 2N+1\\ ad~{\rm odd}\end{subarray}}m^{1/6}a^{1/3}d^{1/6} |  |

 | = \displaystyle= | S 2, 1 + S 2, 2, \displaystyle S_{2,1}+S_{2,2}, |  |

say, where κ 2 = 51.3 \kappa_{2}=51.3 from Lemma 7.1. We follow the same arguments we made for S 1, 1, S 1, 2 S_{1,1},S_{1,2}, now taking into account that a, d a,d are odd numbers. Using Lemma 7.3 with k = 2 k=2, r = 1 r=1, and α = 2 / 3 \alpha=2/3,

 | ∑ n ≤ x n ​ odd n − 2 / 3 < 3 2 x 1 / 3, \sum_{\begin{subarray}{c}n\leq x\\ n~{\rm odd}\end{subarray}}n^{-2/3}<\frac{3}{2}x^{1/3}, |  |

so that

 | S 2, 1 ≤ 3 ​ κ 2 ​ N 4 / 3 2 11 / 3 ​ m 7 / 6 ( 1 − 2 − 7 / 6) ζ ( 7 / 6) < 44.3 N 4 / 3 m 7 / 6. S_{2,1}\leq\frac{3\kappa_{2}N^{4/3}}{2^{11/3}m^{7/6}}(1-2^{-7/6})\zeta(7/6)<44.3\frac{N^{4/3}}{m^{7/6}}. |  |

For S 2, 2 S_{2,2}, the analogue of ( 7.2) has the two sums with τ 2 ′ \tau^{\prime}_{2} and with a, d a,d restricted to odd numbers. Following the argument with X X standing for either 1.01 ​ N 1.01N or 2 ​ N + 1 2N+1 and using Lemmas 7.2, 7.3, and ( 7.1), we have

 | 1 2 ∑ a ≤ 100 a ​ odd ∑ d ≤ X / m ​ a d ​ odd \displaystyle\frac{1}{2}\sum_{\begin{subarray}{c}a\leq 100\\ a~{\rm odd}\end{subarray}}\sum_{\begin{subarray}{c}d\leq X/ma\\ d~{\rm odd}\end{subarray}} | τ 2 ′ ​ ( m ​ a 2 ​ d + 1) ≤ 3 14 ​ κ 2 ​ m 1 / 6 ​ ∑ a ≤ 100 a ​ odd a 1 / 3 ​ ( X m ​ a + 2) 7 / 6 \displaystyle\tau^{\prime}_{2}(ma^{2}d+1)\leq\frac{3}{14}\kappa_{2}m^{1/6}\sum_{\begin{subarray}{c}a\leq 100\\ a~{\rm odd}\end{subarray}}a^{1/3}\Big(\frac{X}{ma}+2\Big)^{7/6} |  |

 |  | ≤ 3 14 κ 2 m − 1 ( 1.01 X) 7 / 6 ∑ a ≤ 100 a ​ odd a − 5 / 6 < 45.36 X 7 / 6 m − 1, \displaystyle\leq\frac{3}{14}\kappa_{2}m^{-1}(1.01X)^{7/6}\sum_{\begin{subarray}{c}a\leq 100\\ a~{\rm odd}\end{subarray}}a^{-5/6}<45.36X^{7/6}m^{-1}, |  |

where we directly computed the a a -sum and we assumed that N > m 2 N>m^{2}, m ≥ 10 9 m\geq 10^{9}. We also have

 | 1 2 ∑ a ​ d ≤ X / m a, d ​ odd a > 100 \displaystyle\frac{1}{2}\sum_{\begin{subarray}{c}ad\leq X/m\\ a,d~{\rm odd}\\ a>100\end{subarray}} | τ 2 ′ ​ ( m ​ a 2 ​ d + 1) ≤ 3 16 ​ κ 2 ​ m 1 / 6 ​ ∑ d ≤ X / 100 ​ m d ​ odd d 1 / 6 ​ ( X m ​ d + 2) 4 / 3 \displaystyle\tau^{\prime}_{2}(ma^{2}d+1)\leq\frac{3}{16}\kappa_{2}m^{1/6}\sum_{\begin{subarray}{c}d\leq X/100m\\ d~{\rm odd}\end{subarray}}d^{1/6}\Big(\frac{X}{md}+2\Big)^{4/3} |  |

 |  | ≤ 3 16 κ 2 ( 1 − 2 − 7 / 6) ζ ( 7 / 6) ( 1.02 X) 4 / 3 / m 7 / 6 < 36.1 X 4 / 3 m − 7 / 6. \displaystyle\leq\frac{3}{16}\kappa_{2}(1-2^{-7/6})\zeta(7/6)(1.02X)^{4/3}/m^{7/6}<36.1X^{4/3}m^{-7/6}. |  |

Adding these two estimates with the two values of X X, we have

 | S 2, 2 < 147.8 N 7 / 6 m − 1 + 127.6 N 4 / 3 m − 7 / 6. S_{2,2}<147.8N^{7/6}m^{-1}+127.6N^{4/3}m^{-7/6}. |  |

Thus, assuming N > m 2 N>m^{2} and m ≥ 10 9 m\geq 10^{9},

 | S 2, 1 + S 2, 2 < ( 171.9 + 147.8 ( N / m) 1 / 6) N 4 / 3 m − 7 / 6 < 177 N 4 / 3 m − 7 / 6. S_{2,1}+S_{2,2}<\Big(171.9+\frac{147.8}{(N/m)^{1/6}}\Big)N^{4/3}m^{-7/6}<177N^{4/3}m^{-7/6}. |  |

### 7.3. The case gcd ⁡ ( f, 6) = 3 \gcd(f,6)=3.

In this case we have m ​ a ​ d ​ c madc not divisible by 3, and m ​ a 2 ​ d ≡ − 1 ( mod 3) ma^{2}d\equiv-1\pmod{3}. Thus, we have d ≡ − m ( mod 3) d\equiv-m\pmod{3}. The number of integers c ≢ 0 ( mod 3) c\not\equiv 0\pmod{3} such that m ​ a ​ d ​ c madc is in an interval of length N / 2 N/2 is ≤ 2 ​ ⌈ N / 6 ​ m ​ a ​ d ⌉ \leq 2\lceil N/6mad\rceil. However, at the top end, namely if m ​ a ​ d > N / 2 mad>N/2, then there is at most 1 value of c c in play, and for m ​ a ​ d > 1.01 ​ N mad>1.01N, we have at most half of τ 3 ′ ​ ( m ​ a 2 ​ d + 1) \tau^{\prime}_{3}(ma^{2}d+1) as the number of possibilities for f f. Using 2 ​ ⌈ N / 6 ​ m ​ a ​ d ⌉ < 2 ​ ⌊ N / 6 ​ m ​ a ​ d ⌋ + 2 2\lceil N/6mad\rceil<2\lfloor N/6mad\rfloor+2, the number of primes in this case is at most

 | S 3, 1 + S 3, 2, S_{3,1}+S_{3,2}, |  |

where

 | S 3, 1:= ∑ m ​ a ​ d ≤ N / 6 d ≡ − m ( mod 3) 3 ∤ a N 3 ​ m ​ a ​ d ​ τ 3 ′ ​ ( m ​ a 2 ​ d + 1) S_{3,1}:=\sum_{\begin{subarray}{c}mad\leq N/6\\ d\,\equiv\,-m\kern-5.0pt\pmod{3}\\ 3\,\nmid\,a\end{subarray}}\frac{N}{3mad}\tau^{\prime}_{3}(ma^{2}d+1) |  |

and

(7.3) |  | S 3, 2:= f ⁡ ( N / 2) + 1 2 ​ f ​ ( 1.01 ​ N) + 1 2 ​ f ​ ( 2 ​ N + 1), S_{3,2}:=f(N/2)+\frac{1}{2}f(1.01N)+\frac{1}{2}f(2N+1), |  |

where

(7.4) |  | f ⁡ ( x):= ∑ m ​ a ​ d ≤ x d ≡ − m ( mod 3) 3 ∤ a τ 3 ′ ​ ( m ​ a 2 ​ d + 1). f(x):=\sum_{\begin{subarray}{c}mad\leq x\\ d\,\equiv\,-m\kern-5.0pt\pmod{3}\\ 3\,\nmid\,a\end{subarray}}\tau^{\prime}_{3}(ma^{2}d+1). |  |

From Lemma 7.1 with κ 3 = 32.3 \kappa_{3}=32.3 we have

 | S 3, 1 \displaystyle S_{3,1} | ≤ κ 3 ​ N 3 ​ m 5 / 6 ∑ a ​ d ≤ N / 6 ​ m d ≡ − m ( mod 3) 3 ∤ a a − 2 / 3 d − 5 / 6 \displaystyle\leq\frac{\kappa_{3}N}{3m^{5/6}}\sum_{\begin{subarray}{c}ad\leq N/6m\\ d\,\equiv\,-m\kern-5.0pt\pmod{3}\\ 3\,\nmid\,a\end{subarray}}a^{-2/3}d^{-5/6} |  |

 |  | < κ 3 ​ N 3 ​ m 5 / 6 ∑ d ≤ N / 6 ​ m d ≡ − m ( mod 3) d − 5 / 6 ⋅ 2 ( N 6 ​ m ​ d) 1 / 3, \displaystyle<\frac{\kappa_{3}N}{3m^{5/6}}\sum_{\begin{subarray}{c}d\leq N/6m\\ d\,\equiv\,-m\kern-5.0pt\pmod{3}\end{subarray}}d^{-5/6}\cdot 2\Big(\frac{N}{6md}\Big)^{1/3}, |  |

using Lemma 7.3 with k = 3 k=3 and r = 1, 2 r=1,2. Summing numerically, we have

 | ∑ d ≡ − m ( mod 3) d − 7 / 6 ≤ ∑ d ≡ 1 ( mod 3) d − 7 / 6 < 2.701, \sum_{d\,\equiv\,-m\kern-5.0pt\pmod{3}}d^{-7/6}\leq\sum_{d\,\equiv\,1\kern-5.0pt\pmod{3}}d^{-7/6}<2.701, |  |

so that

 | S 3, 1 < 32.01 N 4 / 3 m − 7 / 6. S_{3,1}<32.01N^{4/3}m^{-7/6}. |  |

For S 3, 2 S_{3,2} we follow the argument for S 2, 2 S_{2,2}, getting

 | ∑ a ≤ 100 3 ∤ a ∑ d ≤ x / m ​ a d ≡ − m ( mod 3) τ 3 ′ ​ ( m ​ a 2 ​ d + 1) ≤ 2 7 ​ κ 3 ​ ( 1.01 ​ x) 7 / 6 m ​ ∑ a ≤ 100 3 ∤ a 1 a 5 / 6 < 50.1 ​ x 7 / 6 m. \sum_{\begin{subarray}{c}a\leq 100\\ 3\,\nmid\,a\end{subarray}}\kern-2.0pt\sum_{\begin{subarray}{c}d\leq x/ma\\ d\,\equiv\,-m\kern-5.0pt\pmod{3}\end{subarray}}\tau^{\prime}_{3}(ma^{2}d+1)\leq\frac{2}{7}\kappa_{3}\frac{(1.01x)^{7/6}}{m}\sum_{\begin{subarray}{c}a\leq 100\\ 3\,\nmid\,a\end{subarray}}\frac{1}{a^{5/6}}<50.1\frac{x^{7/6}}{m}. |  |

Further,

 | ∑ a ​ d ≤ x / m 3 ∤ a a > 100 d ≡ − m ( mod 3) τ 3 ′ ​ ( m ​ a 2 ​ d + 1) ≤ κ 3 2 ​ ( 1.03 ​ x) 4 / 3 m 7 / 6 ​ ∑ d ≡ 1 ( mod 3) d ≤ x / m 1 d 7 / 6 < 45.4 ​ x 4 / 3 m 7 / 6. \sum_{\begin{subarray}{c}ad\leq x/m\\ 3\,\nmid\,a\\ a>100\\ d\,\equiv\,-m\kern-5.0pt\pmod{3}\end{subarray}}\tau^{\prime}_{3}(ma^{2}d+1)\leq\frac{\kappa_{3}}{2}\frac{(1.03x)^{4/3}}{m^{7/6}}\sum_{\begin{subarray}{c}d\,\equiv\,1\kern-5.0pt\pmod{3}\\ d\leq x/m\end{subarray}}\frac{1}{d^{7/6}}<45.4\frac{x^{4/3}}{m^{7/6}}. |  |

Adding these 2 estimates, we have

 | f ⁡ ( x) < ( 45.4 + 50.1 ( x / m) 1 / 6) ​ x 4 / 3 m 7 / 6 < 47 ​ x 4 / 3 m 7 / 6, f(x)<\Big(45.4+\frac{50.1}{(x/m)^{1/6}}\Big)\frac{x^{4/3}}{m^{7/6}}<47\frac{x^{4/3}}{m^{7/6}}, |  |

where we have been assuming that x > m 2 x>m^{2} and m ≥ 10 9 m\geq 10^{9}. Thus, by ( 7.3) and assuming N ≥ 2 ​ m 2 N\geq 2m^{2}, m ≥ 10 9 m\geq 10^{9},

 | S 3, 1 + S 3, 2 < 133.7 ​ N 4 / 3 m 7 / 6. S_{3,1}+S_{3,2}<133.7\frac{N^{4/3}}{m^{7/6}}. |  |

### 7.4. The case ( f, 6) = 6 (f,6)=6.

This case is similar to the preceding one, except that we use κ 6 = 102.7 \kappa_{6}=102.7 in place of κ 3 \kappa_{3}, we assume the variables a, d, c a,d,c are odd (in addition to not being divisible by 3), and we assume that d ≡ − m ( mod 6) d\equiv-m\pmod{6}. The first observation is that the number of integers c c in an interval ( x, x + L] (x,x+L] coprime to 6 is ≤ ⌈ ( L + 1) / 3 ⌉ \leq\lceil(L+1)/3\rceil. So, the number of integers c c coprime to 6 for which m ​ a ​ d ​ c − f madc-f is in ( N / 2, N] (N/2,N] is ≤ ⌈ N / 6 ​ m ​ a ​ d + 1 / 3 ⌉ \leq\lceil N/6mad+1/3\rceil. At the top end, the number of choices for c c when m ​ a ​ d ≥ N / 4 mad\geq N/4 is ≤ 1 \leq 1, and the weight of this possible choice is 1 / 2 1/2 if m ​ a ​ d ≥ 1.01 ​ N mad\geq 1.01N as before. Thus, the count is at most

(7.5) |  | ∑ m ​ a ​ d ≤ N / 4 ( a, 6) = 1 d ≡ − m ( mod 6) N 6 ​ m ​ a ​ d ​ τ 6 ′ ​ ( m ​ a 2 ​ d + 1) + 1 3 ​ g ​ ( N / 4) + 1 2 ​ g ​ ( 1.01 ​ N) + 1 2 ​ g ​ ( 2 ​ N + 1), \sum_{\begin{subarray}{c}mad\leq N/4\\ (a,6)=1\\ d\,\equiv\,-m\kern-5.0pt\pmod{6}\end{subarray}}\frac{N}{6mad}\tau^{\prime}_{6}(ma^{2}d+1)+\frac{1}{3}g(N/4)+\frac{1}{2}g(1.01N)+\frac{1}{2}g(2N+1), |  |

where

 | g ⁡ ( x):= ∑ m ​ a ​ d ≤ x ( a, 6) = 1 d ≡ − m ( mod 6) τ 6 ′ ​ ( m ​ a 2 ​ d + 1). g(x):=\sum_{\begin{subarray}{c}mad\leq x\\ (a,6)=1\\ d\,\equiv\,-m\kern-5.0pt\pmod{6}\end{subarray}}\tau^{\prime}_{6}(ma^{2}d+1). |  |

Using Lemma 7.3,

 | ∑ m ​ a ​ d ≤ N / 4 ( a, 6) = 1 d ≡ − m ( mod 6) \displaystyle\sum_{\begin{subarray}{c}mad\leq N/4\\ (a,6)=1\\ d\,\equiv\,-m\kern-5.0pt\pmod{6}\end{subarray}} | N 6 ​ m ​ a ​ d τ 6 ′ ( m a 2 d + 1) < κ 6 ​ N 6 ​ m 5 / 6 ∑ a ​ d ≤ N / 4 ​ m ( a, 6) = 1 d ≡ − m ( mod 6) a − 2 / 3 d − 5 / 6 \displaystyle\frac{N}{6mad}\tau^{\prime}_{6}(ma^{2}d+1)<\frac{\kappa_{6}N}{6m^{5/6}}\sum_{\begin{subarray}{c}ad\leq N/4m\\ (a,6)=1\\ d\,\equiv\,-m\kern-5.0pt\pmod{6}\end{subarray}}a^{-2/3}d^{-5/6} |  |

 |  | < κ 6 ​ N 6 ​ m 5 / 6 ∑ d ≤ N / 4 ​ m d ≡ − m ( mod 6) ( N 4 ​ m ​ d) 1 / 3 d − 5 / 6 \displaystyle<\frac{\kappa_{6}N}{6m^{5/6}}\sum_{\begin{subarray}{c}d\leq N/4m\\ d\,\equiv\,-m\kern-5.0pt\pmod{6}\end{subarray}}\Big(\frac{N}{4md}\Big)^{1/3}d^{-5/6} |  |

 |  | < κ 6 ​ N 4 / 3 6 ⋅ 4 1 / 3 ​ m 7 / 6 ∑ d ≡ 1 ( mod 6) d − 7 / 6 < 19.23 N 4 / 3 m 7 / 6. \displaystyle<\frac{\kappa_{6}N^{4/3}}{6\cdot 4^{1/3}m^{7/6}}\sum_{d\,\equiv\,1\kern-5.0pt\pmod{6}}d^{-7/6}<19.23\frac{N^{4/3}}{m^{7/6}}. |  |

As with the previous cases, we first sum on a ≤ 100 a\leq 100. We have

 | ∑ a ≤ 100 ( a, 6) = 1 ∑ d ≤ x / m ​ a d ≡ − m ( mod 6) \displaystyle\sum_{\begin{subarray}{c}a\leq 100\\ (a,6)=1\end{subarray}}\sum_{\begin{subarray}{c}d\leq x/ma\\ d\,\equiv\,-m\kern-5.0pt\pmod{6}\end{subarray}} | τ 6 ′ ​ ( m ​ a 2 ​ d + 1) ≤ κ 6 ​ m 1 / 6 ​ ∑ a ≤ 100 ( a, 6) = 1 1 7 ​ a 1 / 3 ​ ( x m ​ a + 6) 7 / 6 \displaystyle\tau^{\prime}_{6}(ma^{2}d+1)\leq\kappa_{6}m^{1/6}\sum_{\begin{subarray}{c}a\leq 100\\ (a,6)=1\end{subarray}}\frac{1}{7}a^{1/3}\Big(\frac{x}{ma}+6\Big)^{7/6} |  |

 |  | ≤ κ 6 ​ ( 1.01 ​ x) 7 / 6 7 ​ m ∑ a ≤ 100 ( a, 6) = 1 a − 5 / 6 < 42.63 x 7 / 6 m. \displaystyle\leq\frac{\kappa_{6}(1.01x)^{7/6}}{7m}\sum_{\begin{subarray}{c}a\leq 100\\ (a,6)=1\end{subarray}}a^{-5/6}<42.63\frac{x^{7/6}}{m}. |  |

Also

 | ∑ a > 100 ( a, 6) = 1 ∑ d ≤ x / m ​ a d ≡ − m ( mod 6) τ 6 ′ ​ ( m ​ a 2 ​ d + 1) \displaystyle\sum_{\begin{subarray}{c}a>100\\ (a,6)=1\end{subarray}}\sum_{\begin{subarray}{c}d\leq x/ma\\ d\,\equiv\,-m\kern-5.0pt\pmod{6}\end{subarray}}\tau^{\prime}_{6}(ma^{2}d+1) | ≤ κ 6 ​ ( 1.06 ​ x) 4 / 3 4 ​ m 7 / 6 ∑ d ≡ − m ( mod 6) d − 7 / 6 \displaystyle\leq\frac{\kappa_{6}(1.06x)^{4/3}}{4m^{7/6}}\sum_{d\,\equiv\,-m\kern-5.0pt\pmod{6}}d^{-7/6} |  |

 |  | < 49.47 ​ x 4 / 3 m 7 / 6. \displaystyle<49.47\frac{x^{4/3}}{m^{7/6}}. |  |

Thus,

 | g ⁡ ( x) < 42.63 ​ x 7 / 6 m + 49.47 ​ x 4 / 3 m 7 / 6. g(x)<42.63\frac{x^{7/6}}{m}+49.47\frac{x^{4/3}}{m^{7/6}}. |  |

We conclude that when m ≥ 10 9 m\geq 10^{9} and N = 2 ​ m 2 N=2m^{2},

 | 1 3 g ( N / 4) + 1 2 g ( 1.01 N) + 1 2 g ( 2 N + 1) < 92.03 N 4 / 3 m − 7 / 6. \frac{1}{3}g(N/4)+\frac{1}{2}g(1.01N)+\frac{1}{2}g(2N+1)<92.03N^{4/3}m^{-7/6}. |  |

With the previous estimate we have from ( 7.5) that the number of primes p ≤ N p\leq N in the case gcd ⁡ ( f, 6) = 6 \gcd(f,6)=6 is ≤ 111.3 ​ N 4 / 3 / m 7 / 6 \leq 111.3N^{4/3}/m^{7/6}. With the estimates for S j, k S_{j,k} for j = 1, 2, 3 j=1,2,3 and k = 1, 2 k=1,2, we have the following result.

###### Proposition 7.5.

When N = 2 ​ m 2 N=2m^{2} and m ≥ 10 9 m\geq 10^{9}, the number of primes p ∈ ( N / 2, N] p\in(N/2,N] which have a Type I representation is less than 698 ​ N 4 / 3 / m 7 / 6 698N^{4/3}/m^{7/6}.

## 8. Numerically explicit estimates: primes with Type II representations

In this section we prove the following statement.

###### Proposition 8.1.

For every natural number m ≥ 6 m\geq 6, there exists a prime p > m 2, p>m^{2}, for which ( 3.1) has no Type II solution.

###### Remark 8.2.

When m = 4 m=4, every prime p < 10 13 p<10^{13} has a Type II solution. When m = 5 m=5, every prime p < 10 13 p<10^{13} except 2 2 and 5 5 has a Type II solution. We conjecture that these statements also hold for p > 10 13 p>10^{13}.

###### Remark 8.3.

The proof actually shows that for all m ≥ 6 m\geq 6, except for m = 7 m=7, there is a prime p ∈ ( m 2, 2 ​ m 2] p\in(m^{2},2m^{2}] with no Type II solution. When m = 7 m=7, the first prime p > 7 2 p>7^{2} without a Type II solution is 127 127.

In the proof of Proposition 8.1, we will make use of the following estimates.

###### Lemma 8.4.

We have

 | ∑ n ≤ x 1 n ≤ 1 + log ⁡ x ( x ≥ 1), \sum_{n\leq x}\frac{1}{n}\leq 1+\log x\qquad(x\geq 1), |  |

 | ∑ n ≤ x τ ⁡ ( n) ≤ x ⁡ ( 1 + log ⁡ x) ( x ≥ 1), \sum_{n\leq x}\tau(n)\leq x(1+\log x)\qquad(x\geq 1), |  |

 | ∑ n ≤ x τ ⁡ ( n) n ≤ 1 2 ​ log 2 ​ x + 2 ​ log ⁡ x + 1:= P ⁡ ( x) ( x ≥ 1), \sum_{n\leq x}\frac{\tau(n)}{n}\leq\frac{1}{2}\log^{2}x+2\log x+1:=P(x)\qquad(x\geq 1), |  |

 | π ⁡ ( x) − π ⁡ ( x / 2) > x 2 ​ log ⁡ x ( x ≥ 3299). \pi(x)-\pi(x/2)>\frac{x}{2\log x}\qquad(x\geq 3299). |  |

###### Proof.

The first two inequalities are standard exercises. The third one follows from the second one and partial summation. The last one follows from Dusart [2, Eq. (5.5)] when x ≥ 10600 x\geq 10600, and from direct computation otherwise. ∎

###### Proof of Proposition 8.1.

We count the number of primes in the interval ( N / 2, N] (N/2,N] covered by Type II solutions. By Proposition 2.4, if ( x, y, z) (x,y,z) is a solution to ( 3.1) of Type II, there are natural numbers a, b, e a,b,e with a ≤ b a\leq b and

 | p ≡ − e mod m a b, e ∣ a + b. p\equiv-e\mod mab,\qquad e\mid a+b. |  |

By ( 3.4),

 | m ​ a ​ b ≤ p ​ m m − 2 ≤ N ​ m m − 2 = Q ​ m, mab\leq p\frac{m}{m-2}\leq N\frac{m}{m-2}=Qm, |  |

where Q:= N / ( m − 2) Q:=N/(m-2). For given m, a, b, e m,a,b,e, the number of primes p p in ( N / 2, N] (N/2,N] satisfying p ≡ − e mod m ​ a ​ b p\equiv-e\mod mab is

 | ≤ ⌊ N 2 ​ m ​ a ​ b ⌋ + 1. \leq\left\lfloor\frac{N}{2mab}\right\rfloor+1. |  |

The number of primes in ( N / 2, N] (N/2,N] that can be covered by these congruences, by varying the parameters a, b, e a,b,e, is

(8.1) |  | ≤ T:= ∑ a ≤ b: a ​ b ≤ Q τ ( a + b) ( ⌊ N 2 ​ m ​ a ​ b ⌋ + 1) = T 1 + T 2, \leq T:=\sum_{a\leq b:ab\leq Q}\tau(a+b)\left(\left\lfloor\frac{N}{2mab}\right\rfloor+1\right)=T_{1}+T_{2}, |  |

say. For T 1 T_{1} we may assume m ​ a ​ b ≤ N / 2 mab\leq N/2, so that

 | T 1 ≤ N 2 ​ m ​ ∑ a ≤ N / 2 ​ m 1 a ​ ∑ a ≤ b ≤ N / 2 ​ a ​ m τ ⁡ ( a + b) b. T_{1}\leq\frac{N}{2m}\sum_{a\leq\sqrt{N/2m}}\frac{1}{a}\sum_{a\leq b\leq N/2am}\frac{\tau(a+b)}{b}. |  |

Writing n = a + b n=a+b, the innermost sum is

 | ≤ ∑ a ≤ b ≤ N / 2 ​ a ​ m 2 ​ τ ​ ( a + b) a + b ≤ 2 ​ ∑ 2 ​ a ≤ n ≤ N / a ​ m τ ⁡ ( n) n ≤ 2 ​ P ​ ( N / a ​ m), \leq\sum_{a\leq b\leq N/2am}\frac{2\tau(a+b)}{a+b}\leq 2\sum_{2a\leq n\leq N/am}\frac{\tau(n)}{n}\leq 2P(N/am), |  |

by Lemma 8.4. We obtain

 | T 1 ≤ N m ​ ∑ a ≤ N / 2 ​ m P ⁡ ( N / a ​ m) a ≤ N m ​ P ​ ( N / m) ​ ( 1 + log ⁡ N / 2 ​ m). T_{1}\leq\frac{N}{m}\sum_{a\leq\sqrt{N/2m}}\frac{P(N/am)}{a}\leq\frac{N}{m}P(N/m)(1+\log\sqrt{N/2m}). |  |

We let N = 2 ​ m 2 N=2m^{2}. Since P ⁡ ( x) ≤ 1 2 ​ ( 2 + log ⁡ x) 2 P(x)\leq\frac{1}{2}(2+\log x)^{2}, we get

 | T 1 ≤ m 2 ​ ( 3 + log ⁡ m) 3 ( m ≥ 4). T_{1}\leq\frac{m}{2}(3+\log m)^{3}\qquad(m\geq 4). |  |

Similarly,

 | T 2 ≤ ∑ a ≤ Q ∑ b ≤ Q / a τ ⁡ ( a + b) ≤ ∑ a ≤ Q ∑ n ≤ 2 ​ Q / a τ ⁡ ( n). T_{2}\leq\sum_{a\leq\sqrt{Q}}\sum_{b\leq Q/a}\tau(a+b)\leq\sum_{a\leq\sqrt{Q}}\sum_{n\leq 2Q/a}\tau(n). |  |

By Lemma 8.4,

 | T 2 ≤ ∑ a ≤ Q 2 ​ Q a ​ ( 1 + log ⁡ 2 ​ Q / a) ≤ 2 ​ Q ​ ( 1 + log ⁡ 2 ​ Q) ​ ( 1 + log ⁡ Q). T_{2}\leq\sum_{a\leq\sqrt{Q}}\frac{2Q}{a}(1+\log 2Q/a)\leq 2Q(1+\log 2Q)(1+\log\sqrt{Q}). |  |

With N = 2 ​ m 2 N=2m^{2}, we obtain

 | T 2 ≤ 2 ​ m ​ ( 3 + log ⁡ m) 2 ( m ≥ 18). T_{2}\leq 2m(3+\log m)^{2}\qquad(m\geq 18). |  |

The number of primes in ( N / 2, N] = ( m 2, 2 ​ m 2] (N/2,N]=(m^{2},2m^{2}] is,

 | π ⁡ ( N) − π ⁡ ( N / 2) > N 2 ​ log ⁡ N ( N ≥ 3299), \pi(N)-\pi(N/2)>\frac{N}{2\log N}\qquad(N\geq 3299), |  |

by Lemma 8.4. If T 1 + T 2 T_{1}+T_{2} is less than the number of primes in ( N / 2, N] (N/2,N], then there are primes in ( N / 2, N] (N/2,N] with no Type II solution. From the above bounds for T 1 T_{1} and T 2 T_{2}, it follows that T 1 + T 2 < N 2 ​ log ⁡ N T_{1}+T_{2}<\frac{N}{2\log N} for m ≥ 34000 m\geq 34000. When 16000 ≤ m ≤ 34000 16000\leq m\leq 34000, we evaluate with a computer the more precise upper bounds

 | T 1 ≤ N m ​ ∑ a ≤ N / 2 ​ m P ⁡ ( n / a ​ m) a, T 2 ≤ 2 ​ Q ​ ∑ a ≤ Q 1 + log ⁡ ( 2 ​ Q / a) a, T_{1}\leq\frac{N}{m}\sum_{a\leq\sqrt{N/2m}}\frac{P(n/am)}{a},\quad T_{2}\leq 2Q\sum_{a\leq\sqrt{Q}}\frac{1+\log(2Q/a)}{a}, |  |

which we also established above, to confirm that T 1 + T 2 < N 2 ​ log ⁡ N T_{1}+T_{2}<\frac{N}{2\log N}. When 3000 ≤ m ≤ 16000 3000\leq m\leq 16000, we evaluate with a computer the original sum T T in ( 8.1) to confirm that T < N 2 ​ log ⁡ N T<\frac{N}{2\log N} also holds in this range. When 20 ≤ m ≤ 6000 20\leq m\leq 6000, a brute force algorithm shows that there is a prime p p in ( m 2, 2 ​ m 2] (m^{2},2m^{2}] that has no solution at all to ( 3.1), and hence no solution of Type II. Finally, for 6 ≤ m ≤ 19 6\leq m\leq 19, we verify that there is a prime p > m 2 p>m^{2} that has no Type II solution. ∎

## 9. Proof of Theorem 1.2

We begin with the following corollary of the work in Section 8.

###### Corollary 9.1.

If N = 2 ​ m 2 N=2m^{2} and m ≥ 10 9 m\geq 10^{9}, then the number of primes in ( N / 2, N] (N/2,N] with a Type II solution is < 1 10 N 4 / 3 m − 7 / 6 <\frac{1}{10}N^{4/3}m^{-7/6}.

###### Proof.

From the proof of Proposition 8.1, the number in question is

 | ≤ T 1 + T 2 ≤ m 2 ​ ( 3 + log ⁡ m) 3 + 2 ​ m ​ ( 3 + log ⁡ m) 2. \leq T_{1}+T_{2}\leq\frac{m}{2}(3+\log m)^{3}+2m(3+\log m)^{2}. |  |

This is < 1 10 N 4 / 3 m − 7 / 6 = 2 4 / 3 10 m 3 / 2 <\frac{1}{10}N^{4/3}m^{-7/6}=\frac{2^{4/3}}{10}m^{3/2} for m ≥ 10 9 m\geq 10^{9}. ∎

With Proposition 7.5 and Corollary 9.1 we have that when m ≥ 10 9 m\geq 10^{9} and N = 2 ​ m 2 N=2m^{2}, the number of primes p ∈ ( N / 2, N] p\in(N/2,N] for which m / p m/p is the sum of 3 unit fractions is < 698.1 ​ N 4 / 3 / m 7 / 6 <698.1N^{4/3}/m^{7/6}. We contrast this upper bound with the lower bound in Lemma 8.4 for the number of primes in ( N / 2, N] (N/2,N]. And we find that when m ≥ 6.52 × 10 9 m\geq 6.52\times 10^{9} and N = 2 ​ m 2 N=2m^{2}, we have

 | N 2 ​ log ⁡ N > 698.1 ​ N 4 / 3 m 7 / 6. \frac{N}{2\log N}>698.1\frac{N^{4/3}}{m^{7/6}}. |  |

Hence, Theorem 1.2 follows.

## 10. Some final thoughts

In Theorem 1.2 we show that the dyadic interval ( m 2, 2 ​ m 2) (m^{2},2m^{2}) has a prime p p for which m / p m/p is not the sum of 3 unit fractions, for m m beyond a numerically explicit bound. One could ask the question for the smaller interval ( m, 2 ​ m) (m,2m). Here it is a simple exercise to show that m / ( m + 1) m/(m+1) is not the sum of 3 unit fractions once m ≥ 42 m\geq 42. How about for prime n n? Here we have that if p p is a prime in ( m, ( 6 / 5) ​ ( m − 1)) (m,(6/5)(m-1)), then m / p m/p is not the sum of 3 unit fractions. To see this, note that, as we have seen, if m / p m/p is the sum of 3 unit fractions, then the representation is either Type I or Type II, so that at least one summand is ≤ 1 / p \leq 1/p. The other two summands have sum ≤ 5 / 6 \leq 5/6, so m / p ≤ 5 / 6 + 1 / p m/p\leq 5/6+1/p, which implies p ≥ ( 6 / 5) ​ ( m − 1) p\geq(6/5)(m-1), a contradiction. Using explicit prime estimates as in [2] and a calculation, one can show the interval ( m, ( 6 / 5) ​ ( m − 1)) (m,(6/5)(m-1)) contains a prime for every m ≥ 32 m\geq 32. In fact, it is not hard to check smaller m m ’s to see that for each m ≥ 14 m\geq 14 there is a prime p ∈ ( m, 2 ​ m) p\in(m,2m) with m / p m/p not the sum of 3 unit fractions.

A simple corollary of Theorem 1.4 is that for each ϵ > 0 \epsilon>0 and each positive integer j j, there are infinitely many positive rationals r < ϵ r<\epsilon which are not the sum of j j unit fractions. Perhaps this statement has a more direct proof?

Talking about j j summands, perhaps the natural generalization of the Erdős–Straus conjecture is that for each m ≥ 4 m\geq 4 there are at most finitely many n n for which m / n m/n is not the sum of m − 1 m-1 unit fractions. Might this be provable for some m m?

## References

- [1] A. Aigner, Brüche als Summe von Stammbrüchen, J. Reine Angew. Math. 214/215 (1964), 174–179.
- [2] P. Dusart, Explicit estimates of some functions over primes. Ramanujan J. 45 (2018), 227–251.
- [3] C. Elsholtz and T. Tao, Counting the number of solutions to the Erdős–Straus equation on unit fractions, J. Aust. Math. Soc. 94 (2013), 50–105.
- [4] P. Erdős and R. L. Graham, Old and new problems and results in combinatorial number theory, L’Enseignement Math. #28 (1980), 128 pp.
- [5] R. K. Guy, Unsolved problems in number theory, Third Ed., Springer, New York, 2004.
- [6] D. Koukoulopoulos, The distribution of prime numbers, Graduate Studies in Math. 203, Amer. Math. Soc., Providence, RI, 2019.
- [7] S. Mihnea and B. C. Dumitru, Further verification and empirical evidence for the Erdős–Straus conjecture, arXiv:2509.00128
- [8] M. Nakayama, On the decomposition of a rational number into “Stammbrüche.”, Tôhoku Math. J. 46 (1939), 1–21.
- [9] J.-L. Nicolas and G. Robin, Majorations explicites pour le nombre de diviseurs de N N, Canad. Math. Bull. 26 (1983), 485–492.
- [10] R. Obláth, Sur l’équation diophantienne 4 n = 1 x 1 + 1 x 2 + 1 x 3 \frac{4}{n}=\frac{1}{x_{1}}+\frac{1}{x_{2}}+\frac{1}{x_{3}}, Mathesis 59 (1950), 308–316.
- [11] S. E. Salez, The Erdős–Straus conjecture; New modular equations and checking up to n = 10 17 n=10^{17}, arXiv:1406.6307.
- [12] R. C. Vaughan, On a problem of Erdős, Straus and Schinzel, Mathematika 17 (1970), 193–198.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:carlp@math.dartmouth.edu
[4]: mailto:weingartner@suu.edu
