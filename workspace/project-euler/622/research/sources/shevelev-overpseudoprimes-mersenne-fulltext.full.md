<!-- source: https://ar5iv.labs.arxiv.org/html/1206.0606 | converted from HTML -->

[1206.0606] Overpseudoprimes, and Mersenne and Fermat numbers as primover numbers

# Overpseudoprimes, and Mersenne and Fermat numbers as primover numbers

Vladimir Shevelev Address: Vladimir Shevelev, Department of Mathematics, Ben-Gurion University of the Negev, Beer-Sheva 84105, Israel Email address: [shevelev@bgu.ac.il][1], Gilberto García-Pulgarín Address: Gilberto García-Pulgarín, Universidad de Antioquia, Medellín-Colombia Email address: [gigarcia@ciencias.udea.edu.co][2], Juan Miguel Velásquez-Soto Address: Juan Miguel Velásquez-Soto, Departamento de Matemáticas, Universidad del Valle, Cali-Colombia Email address: [jumiveso@univalle.edu.co][3] and John H. Castillo Address: John H. Castillo, Departamento de Matemáticas y Estadística, Universidad de Nariño, San Juan de Pasto-Colombia Email address: [jhcastillo@gmail.com][4]

###### Abstract.

We introduce a new class of pseudoprimes-so called “overpseudoprimes to base b b ”, which is a subclass of strong pseudoprimes to base b b. Denoting via | b | n |b|_{n} the multiplicative order of b b modulo n n, we show that a composite n n is overpseudoprime if and only if | b | d |b|_{d} is invariant for all divisors d > 1 d>1 of n n. In particular, we prove that all composite Mersenne numbers 2 p − 1 2^{p}-1, where p p is prime, are overpseudoprime to base 2 2 and squares of Wieferich primes are overpseudoprimes to base 2 2. Finally, we show that some kinds of well known numbers are overpseudoprime to a base b b.

###### Key words and phrases:

Mersenne numbers, cyclotomic cosets of 2 2 modulo n n, order of 2 2 modulo n n, Poulet pseudoprime, super-Poulet pseudoprime, overpseudoprime, Wieferich prime

###### 2010 Mathematics Subject Classification

Primary 11A51; Secondary 11A41, 11A07.

## 1. Introduction

First and foremost, we recall some definitions and fix some notation. Let b b an integer greater than 1 1 and N N a positive integer relatively prime to b b. Throughout, we denote by | b | N |b|_{N} the multiplicative order of b b modulo N N. For a prime p p, ν p ​ ( N) \nu_{p}(N) means the greatest exponent of p p in the prime factorization of N N.

Fermat’s little theorem implies that 2 p − 1 ≡ 1 ( mod p) 2^{p-1}\equiv 1\pmod{p}, where p p is an odd prime p p. An odd prime p p, is called a Wieferich prime if 2 p − 1 ≡ 1 ( mod p 2) 2^{p-1}\equiv 1\pmod{p^{2}},

We recall that a Poulet number, also known as Fermat pseudoprime to base 2 2, is a composite number n n such that 2 n − 1 ≡ 1 ( mod n) 2^{n-1}\equiv 1\pmod{n}. A Poulet number n n which verifies that d d divides 2 d − 2 2^{d}-2 for each divisor d d of n n, is called a Super-Poulet pseudoprime.

Sometimes the numbers M n = 2 n − 1, n = 1, 2, … M_{n}=2^{n}-1,\enskip n=1,2,\ldots, are called Mersenne numbers, although this name is usually reserved for numbers of the form

(1.1) |  | M p = 2 p − 1 M_{p}=2^{p}-1 |  |

where p p is prime. In this form numbers M p M_{p}, at the first time, were studied by Marin Mersenne (1588-1648) around 1644; see Guy [5, §A3] and a large bibliography there.

In the next section, we introduce a new class of pseudoprimes and we prove that it just contains the odd numbers n n such that | 2 | d |2|_{d} is invariant for all divisors greater than 1 1 of n n. In particular, we show that it contains all composite Mersenne numbers and, at least, squares of all Wieferich primes. In the fourth section, we give a generalization of this concept to arbitrary bases b > 1 b>1 as well. In the final section, we put forward some of its consequences.

We note that, the concept of overpseudoprime to base b b was found in two independent ways. The first one in 2008, by Shevelev [9] and the second one, by Castillo et al. [2], using consequences of the Midy’s property, where overpseudoprimes numbers are denominated Midy pseudoprimes.

The first sections of the present work is a revisited version of Shevelev [9]. In the last section, we present a review of Shevelev [10], using results from Castillo et al. [2].

The sequences [A141232][5], [A141350][6] and [A141390][7] in [11], are result of the earlier work of Shevelev.

## 2. A class of pseudoprimes

Let n > 1 n>1 be an odd number. When we multiply by 2 2 the set of integers modulo n n, we split it in different sets called *cyclotomic cosets*. The cyclotomic coset containing s ≠ 0 s\neq 0 consists of C s = { s, 2 ​ s, 2 2 ​ s, …, 2 m s − 1 ​ s } C_{s}=\{s,2s,2^{2}s,\ldots,2^{m_{s}-1}s\}, where m s m_{s} is the smallest positive number such that 2 m s ⋅ s ≡ s ( mod n) 2^{m_{s}}\cdot s\equiv s\pmod{n}. Actually, it is easy to see that m s = | 2 | n gcd ⁡ ( n, s) m_{s}=|2|_{\frac{n}{\gcd(n,s)}}. For instance the cyclotomic cosets modulo 15 15 are

 | C 1 \displaystyle C_{1} | = { 1, 2, 4, 8 }, \displaystyle=\{1,2,4,8\}, |  |

 | C 3 \displaystyle C_{3} | = { 3, 6, 12, 9 }, \displaystyle=\{3,6,12,9\}, |  |

 | C 5 \displaystyle C_{5} | = { 5, 10 }, and \displaystyle=\{5,10\},\text{ and } |  |

 | C 7 \displaystyle C_{7} | = { 7, 14, 13, 11 }. \displaystyle=\{7,14,13,11\}. |  |

Denote by r = r ⁡ ( n) r=r(n), the number of distinct cyclotomic cosets of 2 2 modulo n n. From the above example, r ⁡ ( 15) = 4 r(15)=4.

Note that, if C 1, …, C r C_{1},\ldots,C_{r} are the different cyclotomic cosets of 2 2 modulo n n, then

(2.1) |  | ⋃ j = 1 r C j = { 1, 2, …, n − 1 } ​ and ​ C j 1 ∩ C j 2 = ∅, j 1 ≠ j 2. \bigcup^{r}_{j=1}C_{j}=\{1,2,\ldots,n-1\}\text{ and }C_{j_{1}}\cap C_{j_{2}}=\varnothing,\;\;j_{1}\neq j_{2}. |  |

We can demonstrate that

(2.2) |  | | 2 | n = lcm ⁡ ( | C 1 |, …, | C r |). |2|_{n}=\lcm(|C_{1}|,\ldots,|C_{r}|). |  |

If p p is an odd prime the cyclotomic cosets have the same number of elements, because for each s ≠ 0 s\neq 0 we have m s = | C s | = | 2 | p gcd ⁡ ( p, s) = | 2 | p m_{s}=|C_{s}|=|2|_{\frac{p}{\gcd(p,s)}}=|2|_{p}. So

(2.3) |  | | C 1 | = ⋯ = | C r |. |C_{1}|=\cdots=|C_{r}|. |  |

Therefore, when p p is an odd prime, we obtain

(2.4) |  | p = r ⁡ ( p) ​ | 2 | p + 1. p=r(p)|2|_{p}+1. |  |

This leave us to study composite numbers such that the equation ( 2.4) holds.

###### Definition 1.

We say that an odd composite number n n is an overpseudoprime to base 2 2, if

(2.5) |  | n = r ⁡ ( n) ​ | 2 | n + 1. n=r(n)|2|_{n}+1. |  |

Note that if n n is an overpseudoprime to base 2 2, then 2 n − 1 = 2 r ⁡ ( n) ​ | 2 | n ≡ 1 ( mod n) 2^{n-1}=2^{r(n)|2|_{n}}\equiv 1\pmod{n}. Thus, the set of overpseudoprimes to base 2 2 is a subset of the set of Poulet pseudoprimes to base 2 2.

###### Theorem 2.

Let n = p 1 l 1 ⋯ p k l k n=p_{1}^{l_{1}}\cdots p_{k}^{l_{k}} be an odd composite number. Then n n is an overpseudoprime to base 2 2 if and only if

(2.6) |  | | 2 | n = | 2 | d, |2|_{n}=|2|_{d}, |  |

for each divisor d > 1 d>1 of n n.

###### Proof.

Let s s, different from zero, be an arbitrary element of ℤ n \mathbb{Z}_{n}. Take u s = gcd ⁡ ( n, s) u_{s}=\gcd(n,s) and v s = n u s v_{s}=\dfrac{n}{u_{s}}. Then s = a ​ u s s=au_{s}, for some integer a a relatively prime with n n. As we said before, | C s | = | 2 | v s \left|C_{s}\right|=\left|2\right|_{v_{s}}.

Note that when s s runs through a set of coset representatives modulo n n, v s v_{s} runs through the set of divisors of n n. So the value of | C s | \left|C_{s}\right| is constant if and only if | 2 | d \left|2\right|_{d} is invariant for each divisor d > 1 d>1 of n n, which proves the theorem. ∎

A direct consequence of the last theorem is the following.

###### Corollary 3.

Two overpseudoprimes to base 2 2, N 1 N_{1} and N 2 N_{2} such that | 2 | N 1 ≠ | 2 | N 2 |2|_{N_{1}}\neq|2|_{N_{2}}, are relatively primes.

###### Corollary 4.

For a prime p p, M p = 2 p − 1 M_{p}=2^{p}-1 is either a prime or an overpseudoprime to base 2 2.

###### Proof.

Assume that M p M_{p} is not prime. Let d > 1 d>1 be any divisor of M p M_{p}. Then | 2 | d |2|_{d} divides p p and thus | 2 | d = p |2|_{d}=p. ∎

###### Corollary 5.

Every overpseudoprime to base 2 2 is a Super-Poulet pseudoprime.

###### Proof.

Let n n be an overpseudoprime to base 2 2 and take d d an arbitrary divisor of n n. By Theorem 2, d d is either prime or overpseudoprime to base 2 2. In any case, we have 2 d − 1 ≡ 1 ( mod d) 2^{d-1}\equiv 1\pmod{d}. ∎

###### Example 6.

Consider the super-Poulet pseudoprime, see [A178997][8] in [11], 96916279 = 167 ⋅ 499 ⋅ 1163 96916279=167\cdot 499\cdot 1163. We know that, cf. [A002326][9] in [11], | 2 | 167 = 83, | 2 | 499 = 166 |2|_{167}=83,\;|2|_{499}=166 and | 2 | 1163 = 166 |2|_{1163}=166. Thus the reciprocal of the above corollary is not true.

Assume that p 1 p_{1} and p 2 p_{2} are primes such that | 2 | p 1 = | 2 | p 2 |2|_{p_{1}}=|2|_{p_{2}}. Then | 2 | p 1 ​ p 2 = lcm ⁡ ( | 2 | p 1, | 2 | p 2) |2|_{p_{1}p_{2}}=\lcm(|2|_{p_{1}},|2|_{p_{2}}). In consequence, n = p 1 ​ p 2 n=p_{1}p_{2} is an overpseudoprime to base 2 2. With the same objective, we get the following.

###### Theorem 7.

Let p 1, …, p k p_{1},\ldots,p_{k} be different primes such that | 2 | p i = | 2 | p j |2|_{p_{i}}=|2|_{p_{j}}, when i ≠ j i\neq j. Assume that p i l i p_{i}^{l_{i}} is an overpseudoprime to base 2 2, where l i l_{i} are positive integers, for each i = 1, …, k i=1,\ldots,k. Then n = p 1 l 1 ⋯ p k l k n=p_{1}^{l_{1}}\cdots p_{k}^{l_{k}} is an overpseudoprime to base 2 2.

## 3. The ( w + 1) (w+1) -th power of Wieferich prime of order w w is overpseudoprime to base 2 2

Knauer and Richstein [6], proved that 1093 1093 and 3511 3511 are the only Wieferich primes less than 1.25 × 10 15 1.25\times 10^{15}. More recently, Dorais and Klyve [3] extend this interval to 6.7 × 10 15 6.7\times 10^{15}.

We say that a prime p p is a Wieferich prime of order w ≥ 1 w\geq 1, if ν p ​ ( 2 p − 1 − 1) = w + 1 \nu_{p}(2^{p-1}-1)=w+1.

The following result, from Nathanson [8, Thm. 3.6], give us a method to calculate | b | p t |b|_{p^{t}} from | b | p |b|_{p}.

###### Theorem 8.

Let p p be an odd prime not divisor of b b, m = ν p ​ ( b | b | p − 1) m=\nu_{p}(b^{\left|b\right|_{p}}-1) and t t a positive integer, then

 | | b | p t = { | b | p, if ​ t ≤ m; p t − m ​ | b | p, if ​ t > m. \left|b\right|_{p^{t}}=\begin{cases}\left|b\right|_{p},&\text{ if }t\leq m;\\ &\\ p^{t-m}\left|b\right|_{p},&\text{ if \ }t>m.\end{cases} |  |

###### Theorem 9.

A prime p p is a Wieferich prime of order greater than or equal to w w if and only if p w + 1 p^{w+1} is an overpseudoprime to base 2 2.

###### Proof.

Suppose that p p is a Wieferich prime of order greater than or equal to w w. Then p w + 1 | 2 p − 1 − 1 p^{w+1}\mid 2^{p-1}-1 and thus | 2 | p w + 1 \left|2\right|_{p^{w+1}} is a divisor of p − 1 p-1.

By Theorem 8, | 2 | p w + 1 = p r \left|2\right|_{p^{w+1}}=p^{r} | 2 | p \left|2\right|_{p} for some non-negative integer r r. So, r = 0 r=0. Therefore, p w + 1 p^{w+1} is an overpseudoprime to base 2 2. The reciprocal is clear.

∎

###### Theorem 10.

Let n n be an overpseudoprime to base 2 2. If n n is not the multiple of the square of a Wieferich prime, then n n is squarefree.

###### Proof.

Let n = p 1 l 1 ​ … ​ p k l k n=p_{1}^{l_{1}}\ldots p_{k}^{l_{k}} and, say, l 1 ≥ 2 l_{1}\geq 2. If p 1 p_{1} is not a Wieferich prime, then | 2 | p 1 2 |2|_{p_{1}^{2}} divides p 1 ​ ( p 1 − 1) p_{1}(p_{1}-1) but does not divide p 1 − 1 p_{1}-1. Thus, | 2 | p 1 2 ≥ p 1 |2|_{p_{1}^{2}}\geq p_{1}. Since | 2 | p 1 ≤ p 1 − 1 |2|_{p_{1}}\leq p_{1}-1, then | 2 | p 1 2 > | 2 | p 1 |2|_{p_{1}^{2}}>|2|_{p_{1}} and by Theorem 2, n n is not an overpseudoprime to base 2 2. ∎

## 4. Overpseudoprime to base b b

Take b b a positive integer greater than 1 1. Denote by r = r b ​ ( n) r=r_{b}(n) the number of cyclotomic cosets of b b modulo n n. If C 1, …, C r C_{1},\ldots,C_{r} are the different cyclotomic cosets of b b modulo n n, then C j 1 ∩ C j 2 = ∅, j 1 ≠ j 2 C_{j_{1}}\cap C_{j_{2}}=\varnothing,\;\;j_{1}\neq j_{2} and ⋃ j = 1 r C j = { 1, 2, …, n − 1 } \bigcup^{r}_{j=1}C_{j}=\{1,2,\ldots,n-1\}.

Let p p be a prime which does not divide b ⁡ ( b − 1) b(b-1). Once again, we get r b ​ ( p) ​ | b | p = p − 1. r_{b}(p)|b|_{p}=p-1.

###### Definition 11.

We say that a composite number n n, relatively prime to b b, is an overpseudoprime to base b b, if it satisfies

(4.1) |  | n = r b ​ ( n) ​ | b | n + 1. n=r_{b}(n)|b|_{n}+1. |  |

The proof of the next theorem follows similarly as in Theorem 2.

###### Theorem 12.

Let n n be a composite number such that gcd ⁡ ( n, b) = 1 \gcd(n,b)=1. Then n n is an overpseudoprime to base b b if and only if | b | n = | b | d |b|_{n}=|b|_{d}, for each divisor d > 1 d>1 of n n.

###### Definition 13.

A prime p p is said a Wieferich prime in base b b if b p − 1 ≡ 1 ( mod p 2) b^{p-1}\equiv 1\pmod{p^{2}}. A Wieferich prime to base b b is of order w ≥ 1 w\geq 1, if ν p ​ ( b p − 1 − 1) = w + 1 \nu_{p}(b^{p-1}-1)=w+1.

With this definition in our hands, we can generalize Theorems 9 and 10. The respective proofs, are similar to that ones.

###### Theorem 14.

A prime p p is a Wieferich prime in base b b of order greater than or equal to w w if and only if p w + 1 p^{w+1} is an overpseudoprime to base b b.

###### Theorem 15.

If n n is overpseudoprime to base b b and is not a multiple of a square of a Wieferich prime to base b b, then n n is squarefree.

Let us remember that an odd composite N N such that N − 1 = 2 r ​ s N-1=2^{r}s with s s an odd integer and ( b, N) = 1 \left(b,\ N\right)=1, is a strong pseudoprime to base b b if either b s ≡ 1 ( mod N) b^{s}\equiv 1\ \pmod{N} or b 2 i ​ s ≡ − 1 ( mod N) b^{2^{i}s}\equiv-1\ \pmod{N}, for some 0 ≤ i < r 0\leq i<r. The following result shows us, that the overpseudoprimes do not appear more frequently than the strong pseudoprimes.

###### Theorem 16.

If n n is an overpseudoprime to base b b, then n n is a strong pseudoprime to the same base.

###### Proof.

Let n n be an overpseudoprime to base b b. Suppose that n − 1 = 2 r ​ s n-1=2^{r}s and | b | n = 2 t ​ s 1 |b|_{n}=2^{t}s_{1}, for some odd integer s s, s 1 s_{1} and nonnegative integers r r, t t. Since n n is an overpseudoprime, then | b | n | ​ n − 1 |b|_{n}|n-1. Thus t ≤ r t\leq r and s 1 s_{1} divides s s. Assume t = 0 t=0. So | b | n |b|_{n} is a divisor of s s and thus

 | b s ≡ 1 ( mod n). b^{s}\equiv 1\pmod{n}. |  |

Then n n is a strong pseudoprime to base b b.

On the other side, assume that t ≥ 1 t\geq 1 and write A = b s 1 = b | b | n 2 t A=b^{s_{1}}=b^{\frac{|b|_{n}}{2^{t}}}. Note that

 | ( A − 1) ( A + 1) ( A 2 + 1) ( A 2 2 + 1) ⋯ ( A 2 t − 1 + 1) = A 2 t − 1 ≡ 0 ( mod n). (A-1)(A+1)(A^{2}+1)(A^{2^{2}}+1)\cdots(A^{2^{t-1}}+1)=A^{2^{t}}-1\equiv 0\pmod{n}. |  |

We claim that for any i < t − 1 i<t-1 the greatest common divisor gcd ⁡ ( n, A 2 i + 1) \gcd(n,\ A^{2^{i}}+1) is 1 1. Indeed, assume that d > 1 d>1 divides both n n and A 2 i + 1 A^{2^{i}}+1. Since n n is an overpseudoprime to base b b, we have | b | d = | b | n |b|_{d}=|b|_{n} and the congruence A 2 i = b 2 i ​ s 1 ≡ − 1 ( mod d) A^{2^{i}}=b^{2^{i}s_{1}}\equiv-1\pmod{d}, leave us to a contradiction with the definition of | b | d |b|_{d}. Thus, gcd ⁡ ( A 2 i + 1, n) = 1 \gcd(A^{2^{i}}+1,n)=1. Similarly gcd ⁡ ( A − 1, n) = 1 \gcd\left(A-1,\ n\right)=1 and we obtain

 | A 2 t − 1 + 1 ≡ 0 ( mod n). A^{2^{t-1}}+1\equiv 0\pmod{n}. |  |

Consequently, b 2 t − 1 ​ s ≡ − 1 ( mod n) b^{2^{t-1}s}\equiv-1\pmod{n}. Therefore, n n is a strong pseudoprime to base b b. ∎

Note that there are strong pseudoprimes to base b b such that | b | n = 2 t ​ s 1 |b|_{n}=2^{t}s_{1} and b 2 i ​ s 1 ≢ − 1 ( mod n) b^{2^{i}s_{1}}\not\equiv-1\pmod{n} for i < t − 1 i<t-1, but n n is not an overpseudoprime to base b b. For example n = 74415361 n=74415361 and b = 13 b=13.

As before, where we have proved that every overpseudoprime to base 2 2 is super-Poulet pseudoprime, using Theorem 12 we can prove the following statement.

###### Theorem 17.

Every overpseudoprime n n to base b b is a superpseudoprime, that is

(4.2) |  | b d − 1 ≡ 1 ( mod d), b^{d-1}\equiv 1\pmod{d}, |  |

for each divisor d > 1 d>1 of n n.

###### Theorem 18.

If n n is an overpseudoprime to base b b, then for every two divisors d 1 < d 2 d_{1}<d_{2} of n n, including 1 1 and n n, we have

(4.3) |  | | b | n | ​ d 2 − d 1. |b|_{n}|d_{2}-d_{1}. |  |

###### Proof.

By the equation ( 4.2), we have | b | d i = | b | n |b|_{d_{i}}=|b|_{n} divides d i − 1 d_{i}-1, for i = 1, 2, i=1,2, and thus ( 4.3) follows. ∎

## 5. Primoverization Process

Note that, if n n is an overpseudoprime to base b b, a divisor of n n is either prime or overpseudoprime to base b b. In this section we study some kinds of numbers which satisfy this property.

In the sequel, we denote by Φ n ​ ( x) \Phi_{n}\left(x\right) the n n -th cyclotomic polynomial. We recall the following theorems from Castillo et al. [2].

###### Theorem 19.

A composite number N N with gcd ⁡ ( N, | b | N) = 1, \gcd\left(N,\left|b\right|_{N}\right)=1, is an overpseudoprime to base b b if and only if Φ | b | N ​ ( b) ≡ 0 ( mod N) \Phi_{\left|b\right|_{N}}\left(b\right)\equiv 0\pmod{N} and | b | N > 1 \left|b\right|_{N}>1.

###### Theorem 20.

Let N > 2 N>2 and P N ​ ( b) = Φ N ​ ( b) gcd ⁡ ( N, Φ N ​ ( b)) P_{N}\left(b\right)=\dfrac{\Phi_{N}\left(b\right)}{\gcd\left(N,\ \Phi_{N}\left(b\right)\right)}. If P N ​ ( b) P_{N}\left(b\right) is composite, then P N ​ ( b) P_{N}\left(b\right) is an overpseudoprime to base b b.

The last theorem leave us to the next definition.

###### Definition 21.

A positive integer is called primover to base b b if it is either prime or an overpseudoprime to base b b.

By Theorem 12, we know that each divisor greater than 1 1, of a overpseudoprime to base b b is primover to the same base b b. By Corollary 2.1, M p M_{p} is primover to base 2 2.

Theorem 20 suggests that we need to know the value of gcd ⁡ ( N, Φ N ​ ( b)) \gcd\left(N,\ \Phi_{N}\left(b\right)\right). To that objective, we recall a result from Motose [7, Th. 2].

###### Theorem 22.

We set n ≥ 2 n\geq 2, a ≥ 2 a\geq 2. Then p p is a prime divisor of Φ n ​ ( b) \Phi_{n}(b) if and only if gcd ⁡ ( b, p) = 1 \gcd(b,p)=1 and n = p γ ​ | b | p n=p^{\gamma}|b|_{p} where γ ≥ 0 \gamma\geq 0. A prime divisor p p of Φ n ​ ( b) \Phi_{n}(b) for n ≥ 3 n\geq 3 has the property such that n = | a | p n=|a|_{p} or ν p ​ ( Φ n ​ ( b)) = 1 \nu_{p}(\Phi_{n}(b))=1 as γ = 0 \gamma=0 or not.

Let p p be the greatest prime divisor of N N. We claim that either gcd ⁡ ( N, Φ N ​ ( b)) = 1 \gcd(N,\Phi_{N}(b))=1 or p p. Indeed, assume that there is a prime q < p q<p divisor of N N and Φ N ​ ( b) \Phi_{N}(b). Thus, Theorem 22 implies that N = q γ ​ | b | q N=q^{\gamma}|b|_{q}. But as p p divides N N, we obtain a contradiction. So gcd ⁡ ( N, Φ N ​ ( b)) \gcd(N,\Phi_{N}(b)), is either 1 1 or a power of p p. If gcd ⁡ ( N, Φ N ​ ( b)) > 1 \gcd(N,\Phi_{N}(b))>1, then N = p l ​ | b | p N=p^{l}|b|_{p}. Since l > 0 l>0, Theorem 22 implies that p 2 p^{2} does not divide Φ N ​ ( b) \Phi_{N}(b). Therefore, we get the following corollary.

###### Corollary 23.

Let N > 1 N>1 and p p the greatest prime divisor of N N. Then gcd ⁡ ( N, Φ N ​ ( b)) = 1 \gcd(N,\Phi_{N}(b))=1 or p p.

In the sequel, we prove that some known kinds of numbers are primovers to some base b b.

###### Theorem 24.

A generalized Fermat number, F n ​ ( b) = b 2 n + 1 F_{n}(b)=b^{2^{n}}+1, with n n a positive integer and b b even; is primover to base b b.

###### Proof.

It is well known that if p p is prime, then Φ p r ​ ( x) = x p r − 1 x p r − 1 − 1 \Phi_{p^{r}}\left(x\right)=\dfrac{x^{p^{r}}-1}{x^{p^{r-1}}-1}, see Bamunoba [1, Thm. 3.4.6] or Gallot [4, Thm. 1.1]. Since gcd ⁡ ( 2 n + 1, Φ 2 n + 1 ​ ( b)) = 1 \gcd\left(2^{n+1},\ \Phi_{2^{n+1}}\left(b\right)\right)=1, we have P 2 n + 1 ​ ( b) = F n ​ ( b) P_{2^{n+1}}(b)=F_{n}\left(b\right) and the result follows from Theorem 20. ∎

###### Theorem 25.

A generalized Mersenne number, M p ​ ( b) = b p − 1 b − 1 M_{p}\left(b\right)=\dfrac{b^{p}-1}{b-1}, with p p a prime such that gcd ⁡ ( p, b − 1) = 1 \gcd(p,b-1)=1, is primover to base b b.

###### Proof.

Note that Φ p ​ ( b) = M p ​ ( b) \Phi_{p}(b)=M_{p}\left(b\right) and gcd ⁡ ( p, Φ p ​ ( b)) = 1 \gcd(p,\Phi_{p}(b))=1. So P p ​ ( b) = M p ​ ( b) P_{p}(b)=M_{p}(b) and the result follows from Theorem 20. ∎

By Theorems 18 and 25, once again, we can prove that the numbers M p ​ ( b) M_{p}{(b)} satisfy a similar property of the Mersenne numbers M p M_{p}.

###### Corollary 26.

If gcd ⁡ ( p, b − 1) = 1 \gcd(p,b-1)=1, then for every pair of divisors d 1 < d 2 d_{1}<d_{2} of M p ​ ( b) M_{p}{(b)}, including trivial divisors 1 1 and M p ​ ( b) M_{p}{(b)}, we have

(5.1) |  | p | d 2 − d 1. p|d_{2}-d_{1}. |  |

The following corollary give us an interesting property of M r ​ ( b) M_{r}(b).

###### Corollary 27.

Let r r be a prime with gcd ⁡ ( r, b − 1) = 1 \gcd(r,b-1)=1. Then M r ​ ( b) M_{r}(b) is prime if and only if the progression ( 1 + r ​ x) x ≥ 0 (1+rx)_{x\geq 0} contains just one prime p p such that | b | p = r |b|_{p}=r.

###### Proof.

Assume that M r ​ ( b) M_{r}(b) is prime. If there exists a prime p p, such that | b | p = r |b|_{p}=r, then p = M r ​ ( b) p=M_{r}(b). Since r | p − 1 r|p-1, i.e., p p is the unique prime in the progression ( 1 + r ​ x) x ≥ 0 (1+rx)_{x\geq 0}.

Conversely, assume that there exists only one prime of the form p = 1 + r ​ x p=1+rx, with x ≥ 0 x\geq 0, such that | b | p = r |b|_{p}=r. So p p divides M r ​ ( b) M_{r}(b). If M r ​ ( b) M_{r}(b) is composite, then it is overpseudoprime to base b b and thus to other prime divisor q q of M r ​ ( b) M_{r}(b) we obtain | b | q = r |b|_{q}=r. This contradicts our assumption. ∎

The next result shows that Fermat numbers to base 2 2 are the only ones, of the form 2 m + 1 2^{m}+1, which are primover to base 2 2.

###### Theorem 28.

The following properties hold.

1. (1)

Assume that b b is even. Then P m ​ ( b) = b m + 1 P_{m}(b)=b^{m}+1 is primover to base b b if and only if m m is a power of 2 2.

2. (2)

Suppose that gcd ⁡ ( n, b − 1) = 1 \gcd(n,b-1)=1. Then M n ​ ( b) = b n − 1 b − 1 M_{n}(b)=\dfrac{b^{n}-1}{b-1} is primover to base b b if and only if n n is prime.

###### Proof.

Sufficient conditions were proved in Theorems 24 and 25.

Now assume that m m has an odd prime divisor. So b + 1 b+1 is a divisor of P m ​ ( b) P_{m}(b) and thereby it is not a prime. Since, | b | b + 1 = 2 \left|b\right|_{b+1}=2 and | b | b m + 1 = 2 ​ m \left|b\right|_{b^{m}+1}=2m; also it is not an overpseudoprime to base b b.

To prove the necessity of the second part, suppose that n n is not prime. Thus for a prime p p divisor of n n, we have M n ​ ( b) M_{n}(b) is composite and b p − 1 b^{p}-1 is one of its proper divisors. As | b | b p − 1 = p \left|b\right|_{b^{p}-1}=p and | b | M n ​ ( b) = n \left|b\right|_{M_{n}(b)}=n, we get that M n ​ ( b) M_{n}(b) is not an overpseudoprime to base b. b. ∎

We note that, for p p and q q primes with q < p q<p, | b | Φ p ​ q ​ ( b) = p ​ q |b|_{\Phi_{pq}(b)}=pq.

###### Theorem 29.

If q < p q<p are primes, then

 | N = ( b − 1) ​ ( b p ​ q − 1) ( b p − 1) ​ ( b q − 1) N=\frac{(b-1)(b^{pq}-1)}{(b^{p}-1)(b^{q}-1)} |  |

is primover to base b b if and only if N N is not multiple of p p.

###### Proof.

It is clear that, N = Φ p ​ q ​ ( b) N=\Phi_{pq}\left(b\right). Assume that N N is not a multiple of p p. Corollary 23 implies that gcd ⁡ ( p ​ q, Φ p ​ q ​ ( b)) = 1 \gcd\left(pq,\ \Phi_{pq}\left(b\right)\right)=1 and the result follows from Theorem 20.

Conversely assume that N N is primover to base b b and p p divides N N. Thereby, | b | p |b|_{p} divides q q and as | b | N = p ​ q |b|_{N}=pq, we get a contradiction. ∎

###### Corollary 30.

With the above notation, if p p divides N N, then N p \dfrac{N}{p} is primover to base b b.

Once again, using Corollary 23 and Theorem 20 we can prove the following theorems.

###### Theorem 31.

If p p is prime, then

 | N = b p n − 1 b p n − 1 − 1 N=\frac{b^{p^{n}}-1}{b^{p^{n-1}}-1} |  |

is primover to base b b if and only if N N is not multiple of p p.

###### Theorem 32.

Let n = p 1 p 2 ⋯ p t n=p_{1}p_{2}\cdots p_{t}, where p 1 < p 2 < ⋯ < p t p_{1}<p_{2}<\cdots<p_{t} are primes and let

 | N = ∏ e | n ( b e − 1) μ ⁡ ( e) ​ μ ​ ( n). N=\prod\nolimits_{e|n}\left(b^{e}-1\right)^{\mu\left(e\right)\mu\left(n\right)}. |  |

If gcd ⁡ ( N, p t) = 1 \gcd(N,p_{t})=1, then N N is primover to base b b. In other case, N p t \dfrac{N}{p_{t}} is primover to base b b.

## References

- [1] A. S. Bamunoba. Cyclotomic polynomials. Thesis master of science in the African Institute for Mathematical Sciences. Stellenbosch University, South Africa, [http://users.aims.ac.za/~bamunoba/bamunoba.pdf][10] (2010).
- [2] J. H. Castillo, G. García-Pulgarín, and J. M. Velásquez-Soto, Pseudoprimes stronger than strong pseudoprimes, preprint, arXiv:1202.3428v2 [math.NT] (2012). (Manuscript submitted for publication)
- [3] F. G. Dorais and D. Klyve, A Wieferich prime search up to 6.7 × 10 15 6.7\times 10^{15}, *J. Integer Seq.*14 (2011), Article 11.9.2.
- [4] Y. Gallot, Cyclotomic polynomials and prime numbers, preprint, [http://yves.gallot.pagesperso-orange.fr/papers/cyclotomic.pdf][11]
- [5] R. K. Guy, *Unsolved Problems in Number Theory*, third ed., Problem Books in Mathematics, Springer-Verlag, 2004.
- [6] J. Knauer and J. Richstein, The continuing search for Wieferich primes, *Math. Comp.*74 (2005), no. 251, 1559–1563 (electronic).
- [7] K. Motose, On values of cyclotomic polynomials. II, *Math. J. Okayama Univ.*37 (1995), 27–36 (1996).
- [8] M. B. Nathanson, *Elementary Methods in Number Theory*, Graduate Texts in Mathematics, vol. 195, Springer-Verlag, 2000.
- [9] V. Shevelev, Overpseudoprimes, Mersenne Numbers and Wieferich primes, preprint, arXiv:0806.3412v7 [math.NT] (2008).
- [10] V. Shevelev, Process of primoverization of numbers of the form a n − 1 a^{n}-1, preprint, arXiv:0807.2332v2 [math.NT] (2008).
- [11] N. J. A. Sloane, The on-line encyclopedia of integer sequences, published electronically at [http://oeis.org][12].

[◄][13][image: ar5iv homepage] [14]
[Feeling lucky?][15] [16]
[Conversion report][17]
[Report an issue][18]
[View original on arXiv][19] [►][20]


## Links

[1]: mailto:shevelev@bgu.ac.il
[2]: mailto:gigarcia@ciencias.udea.edu.co
[3]: mailto:jumiveso@univalle.edu.co
[4]: mailto:jhcastillo@gmail.com
[5]: http://oeis.org/A141232
[6]: http://oeis.org/A141350
[7]: http://oeis.org/A141390
[8]: http://oeis.org/A178997
[9]: http://oeis.org/A002326
[10]: http://users.aims.ac.za/~bamunoba/bamunoba.pdf
[11]: http://yves.gallot.pagesperso-orange.fr/papers/cyclotomic.pdf
[12]: http://oeis.org
[13]: /html/1206.0605
[14]: /
[15]: /feeling_lucky
[16]: /land_of_honey_and_milk
[17]: /log/1206.0606
[18]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1206.0606
[19]: https://arxiv.org/pdf/1206.0606
[20]: /html/1206.0607
