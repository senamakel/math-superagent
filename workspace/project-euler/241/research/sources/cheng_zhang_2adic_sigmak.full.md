<!-- source: https://arxiv.org/html/2603.11979v1 | converted from HTML -->

On the 2 -adic valuation of ⁢ σ k ( n )

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2603.11979v1 [math.NT] 12 Mar 2026

# On the 2 2 -adic valuation of σ k ​ ( n) \sigma_{k}(n)

Kaimin Cheng Address: School of Mathematical Sciences, China West Normal University, Nanchong 637002, P. R. China Email address: [ckm20@126.com][3] and Ke Zhang Address: School of Mathematical Sciences, China West Normal University, Nanchong 637002, P. R. China Email address: [2745808109@qq.com][4]

###### Abstract.

For a positive integer k k, let

 | σ k ​ ( n) = ∑ d | n d k \sigma_{k}(n)=\sum_{d\mid n}d^{k} |  |

be the divisor function of order k k, and let ν p ​ ( m) \nu_{p}(m) denote the p p -adic valuation of an integer m m. Motivated by recent work on the p p -adic valuation of σ k ​ ( n) \sigma_{k}(n), we study ν 2 ​ ( σ k ​ ( n)) \nu_{2}(\sigma_{k}(n)) in detail. We prove that, for every integer n ≥ 2 n\geq 2,

 | ν 2 ​ ( σ k ​ ( n)) ≤ { ⌈ log 2 ⁡ n ⌉, if k is odd, ⌊ log 2 ⁡ n ⌋, if k is even. \nu_{2}(\sigma_{k}(n))\leq\begin{cases}\lceil\log_{2}n\rceil,&\text{if $k$ is odd},\\[2.84526pt] \lfloor\log_{2}n\rfloor,&\text{if $k$ is even}.\end{cases} |  |

These bounds are best possible. More precisely, if k k is odd, then equality holds if and only if n n is a product of distinct Mersenne primes; if k k is even, then equality holds if and only if n = 3 n=3. We also obtain an explicit formula for ν 2 ​ ( σ k ​ ( n)) \nu_{2}(\sigma_{k}(n)) in terms of the prime factorization of n n.

###### Key words and phrases:

divisor function, 2 2 -adic valuation, upper bound

###### 2020 Mathematics Subject Classification

Primary 11A25, 11D61

## 1. Introduction

For a positive integer n n, the classical sum-of-divisors function

 | σ ⁡ ( n) = ∑ d | n d \sigma(n)=\sum_{d\mid n}d |  |

is one of the most fundamental arithmetic functions in number theory. It appears naturally in many problems, ranging from multiplicative number theory to the theory of perfect numbers. A celebrated theorem of Robin [7] states that the Riemann hypothesis is equivalent to the inequality

 | σ ⁡ ( n) < e γ ​ n ​ log ⁡ log ⁡ n ( n > 5041), \sigma(n)<e^{\gamma}n\log\log n\qquad(n>5041), |  |

where γ \gamma denotes Euler’s constant.

Another classical topic related to σ ⁡ ( n) \sigma(n) is the theory of perfect numbers. A positive integer n n is called *perfect*if σ ⁡ ( n) = 2 ​ n \sigma(n)=2n. Euler proved that an even integer n n is perfect if and only if

 | n = 2 m ​ ( 2 m + 1 − 1) n=2^{m}(2^{m+1}-1) |  |

for some positive integer m m such that 2 m + 1 − 1 2^{m+1}-1 is prime, that is, a Mersenne prime. Whether there exist infinitely many even perfect numbers remains open, as does the existence of odd perfect numbers. For the latter problem, Ochem and Rao [5] proved that an odd perfect number must exceed 10 1500 10^{1500}, while Nielsen [4] showed that an odd perfect number must have at least 10 10 distinct prime factors.

Let p p be a prime. For a nonzero integer m m, write ν p ​ ( m) \nu_{p}(m) for the p p -adic valuation of m m, namely the largest integer α \alpha such that p α | m p^{\alpha}\mid m. In recent years, increasing attention has been paid to the p p -adic valuation of divisor sums. In particular, Amdeberhan, Moll, Sharma, and Villamizar [1] studied ν p ​ ( σ ​ ( n)) \nu_{p}(\sigma(n)) and proved that

 | ν 2 ​ ( σ ⁡ ( n)) ≤ ⌈ log 2 ⁡ n ⌉ \nu_{2}(\sigma(n))\leq\lceil\log_{2}n\rceil |  |

for every integer n ≥ 2 n\geq 2, with equality if and only if n n is a product of distinct Mersenne primes. For odd primes p p, they also obtained conditional upper bounds for ν p ​ ( σ ​ ( n)) \nu_{p}(\sigma(n)). These conditions were later removed by Zhao and Chen [8], who proved that

 | ν p ​ ( σ ⁡ ( n)) ≤ ⌈ log p ⁡ n ⌉ \nu_{p}(\sigma(n))\leq\lceil\log_{p}n\rceil |  | (1.1) |

for every odd prime p p and every integer n ≥ 2 n\geq 2. They also determined all integers n ≥ 2 n\geq 2 satisfying equality in ( 1.1) for every odd prime p < 10 5 p<10^{5}. Related investigations for other arithmetic functions may be found, for instance, in [3, 6].

For a positive integer k k, define the divisor function of order k k by

 | σ k ​ ( n) = ∑ d | n d k. \sigma_{k}(n)=\sum_{d\mid n}d^{k}. |  |

Very recently, Zhao [9] proved that

 | ν p ​ ( σ k ​ ( n)) ≤ ⌈ k ​ log p ​ n ⌉ \nu_{p}(\sigma_{k}(n))\leq\lceil k\log_{p}n\rceil |  |

for every integer n ≥ 2 n\geq 2, every prime p p, and every integer k ≥ 1 k\geq 1.

The purpose of this paper is to sharpen Zhao’s bound in the case p = 2 p=2. Our main result is the following.

###### Theorem 1.1.

Let k ≥ 1 k\geq 1 and n ≥ 2 n\geq 2. Write

 | n = 2 a ​ ∏ i = 1 r p i α i, n=2^{a}\prod_{i=1}^{r}p_{i}^{\alpha_{i}}, |  |

where p 1, …, p r p_{1},\dots,p_{r} are distinct odd primes. Then

 | ν 2 ​ ( σ k ​ ( n)) = ∑ 1 ≤ i ≤ r α i ​ odd ( ν 2 ​ ( α i + 1) + ν 2 ​ ( p i k + 1) − 1). \nu_{2}(\sigma_{k}(n))=\sum_{\begin{subarray}{c}1\leq i\leq r\\ \alpha_{i}\ \mathrm{odd}\end{subarray}}\bigl(\nu_{2}(\alpha_{i}+1)+\nu_{2}(p_{i}^{k}+1)-1\bigr). |  |

In particular:

1. (a)

If k k is odd, then

 | ν 2 ​ ( σ k ​ ( n)) = ∑ 1 ≤ i ≤ r α i ​ odd ( ν 2 ​ ( α i + 1) + ν 2 ​ ( p i + 1) − 1), \nu_{2}(\sigma_{k}(n))=\sum_{\begin{subarray}{c}1\leq i\leq r\\ \alpha_{i}\ \mathrm{odd}\end{subarray}}\bigl(\nu_{2}(\alpha_{i}+1)+\nu_{2}(p_{i}+1)-1\bigr), |  |

and

 | ν 2 ​ ( σ k ​ ( n)) ≤ ⌈ log 2 ⁡ n ⌉. \nu_{2}(\sigma_{k}(n))\leq\lceil\log_{2}n\rceil. |  |

Equality holds if and only if n n is a product of distinct Mersenne primes.

2. (b)

If k k is even, then

 | ν 2 ​ ( σ k ​ ( n)) = ∑ 1 ≤ i ≤ r α i ​ odd ν 2 ​ ( α i + 1), \nu_{2}(\sigma_{k}(n))=\sum_{\begin{subarray}{c}1\leq i\leq r\\ \alpha_{i}\ \mathrm{odd}\end{subarray}}\nu_{2}(\alpha_{i}+1), |  |

and

 | ν 2 ​ ( σ k ​ ( n)) ≤ ⌊ log 2 ⁡ n ⌋. \nu_{2}(\sigma_{k}(n))\leq\lfloor\log_{2}n\rfloor. |  |

Equality holds if and only if n = 3 n=3.

## 2. Prime powers

We begin with the multiplicativity of σ k \sigma_{k}. If gcd ⁡ ( m, n) = 1 \gcd(m,n)=1, then

 | σ k ​ ( m ​ n) = σ k ​ ( m) ​ σ k ​ ( n). \sigma_{k}(mn)=\sigma_{k}(m)\sigma_{k}(n). |  |

Indeed, every positive divisor d d of m ​ n mn can be written uniquely in the form d = a ​ b d=ab with a | m a\mid m and b | n b\mid n. Hence

 | σ k ​ ( m ​ n) = ∑ d | m ​ n d k = ∑ a | m b | n ( a ​ b) k = ( ∑ a | m a k) ​ ( ∑ b | n b k) = σ k ​ ( m) ​ σ k ​ ( n). \sigma_{k}(mn)=\sum_{d\mid mn}d^{k}=\sum_{\begin{subarray}{c}a\mid m\\ b\mid n\end{subarray}}(ab)^{k}=\left(\sum_{a\mid m}a^{k}\right)\left(\sum_{b\mid n}b^{k}\right)=\sigma_{k}(m)\sigma_{k}(n). |  |

Therefore, if

 | n = 2 a ​ ∏ i = 1 r p i α i, n=2^{a}\prod_{i=1}^{r}p_{i}^{\alpha_{i}}, |  |

where the p i p_{i} are distinct odd primes and a, α i ≥ 0 a,\alpha_{i}\geq 0, then

 | σ k ​ ( n) = σ k ​ ( 2 a) ​ ∏ i = 1 r σ k ​ ( p i α i), \sigma_{k}(n)=\sigma_{k}(2^{a})\prod_{i=1}^{r}\sigma_{k}(p_{i}^{\alpha_{i}}), |  |

and so

 | ν 2 ​ ( σ k ​ ( n)) = ν 2 ​ ( σ k ​ ( 2 a)) + ∑ i = 1 r ν 2 ​ ( σ k ​ ( p i α i)). \nu_{2}(\sigma_{k}(n))=\nu_{2}(\sigma_{k}(2^{a}))+\sum_{i=1}^{r}\nu_{2}(\sigma_{k}(p_{i}^{\alpha_{i}})). |  |

Thus the problem reduces to prime powers.

We first consider powers of 2 2.

###### Lemma 2.1.

For every a ≥ 0 a\geq 0,

 | ν 2 ​ ( σ k ​ ( 2 a)) = 0. \nu_{2}(\sigma_{k}(2^{a}))=0. |  |

###### Proof.

Since

 | σ k ​ ( 2 a) = 1 + 2 k + 2 2 ​ k + ⋯ + 2 a ​ k, \sigma_{k}(2^{a})=1+2^{k}+2^{2k}+\cdots+2^{ak}, |  |

all terms except the first are even. Hence the sum is odd, and therefore

 | ν 2 ​ ( σ k ​ ( 2 a)) = 0. \nu_{2}(\sigma_{k}(2^{a}))=0. |  |

∎

Thus the 2 2 -adic valuation of σ k ​ ( n) \sigma_{k}(n) depends only on the odd part of n n.

###### Lemma 2.2.

If n = 2 a ​ m n=2^{a}m with m m odd, then

 | ν 2 ​ ( σ k ​ ( n)) = ν 2 ​ ( σ k ​ ( m)). \nu_{2}(\sigma_{k}(n))=\nu_{2}(\sigma_{k}(m)). |  |

###### Proof.

This follows immediately from multiplicativity and Lemma 2.1. ∎

The following standard valuation formula is a special case of the lifting-the-exponent lemma.

###### Lemma 2.3.

[2, Proposition 1] Let p p be a prime and let A ≥ 2 A\geq 2 be an integer. Then for every positive integer m m:

1. (a)

If p p is odd and p | ( A − 1) p\mid(A-1), then

 | ν p ​ ( A m − 1) = ν p ​ ( A − 1) + ν p ​ ( m). \nu_{p}(A^{m}-1)=\nu_{p}(A-1)+\nu_{p}(m). |  |

2. (b)

If p = 2 p=2 and A A is odd, then

 | ν 2 ​ ( A m − 1) = { ν 2 ​ ( A − 1), if m is odd, ν 2 ​ ( A 2 − 1) + ν 2 ​ ( m) − 1, if m is even. \nu_{2}(A^{m}-1)=\begin{cases}\nu_{2}(A-1),&\text{if $m$ is odd},\\[2.84526pt] \nu_{2}(A^{2}-1)+\nu_{2}(m)-1,&\text{if $m$ is even}.\end{cases} |  |

We now deal with odd prime powers.

###### Theorem 2.4.

Let p p be an odd prime and α ≥ 0 \alpha\geq 0. Then

 | ν 2 ​ ( σ k ​ ( p α)) = { 0, if ​ α ​ is even, ν 2 ​ ( α + 1) + ν 2 ​ ( p k + 1) − 1, if ​ α ​ is odd. \nu_{2}(\sigma_{k}(p^{\alpha}))=\begin{cases}0,&\text{if }\alpha\text{ is even},\\[2.84526pt] \nu_{2}(\alpha+1)+\nu_{2}(p^{k}+1)-1,&\text{if }\alpha\text{ is odd}.\end{cases} |  |

###### Proof.

We have

 | σ k ​ ( p α) = 1 + p k + p 2 ​ k + ⋯ + p α ​ k = p k ⁡ ( α + 1) − 1 p k − 1. \sigma_{k}(p^{\alpha})=1+p^{k}+p^{2k}+\cdots+p^{\alpha k}=\frac{p^{k(\alpha+1)}-1}{p^{k}-1}. |  |

If α \alpha is even, then α + 1 \alpha+1 is odd. Since p p is odd, each term p j ​ k p^{jk} is odd, and hence the sum of the α + 1 \alpha+1 terms is odd. Therefore

 | ν 2 ​ ( σ k ​ ( p α)) = 0. \nu_{2}(\sigma_{k}(p^{\alpha}))=0. |  |

Now assume that α \alpha is odd, so that α + 1 \alpha+1 is even. Put A = p k A=p^{k}. Then A A is odd and

 | σ k ​ ( p α) = A α + 1 − 1 A − 1. \sigma_{k}(p^{\alpha})=\frac{A^{\alpha+1}-1}{A-1}. |  |

By Lemma 2.3,

 | ν 2 ​ ( A α + 1 − 1) = ν 2 ​ ( A − 1) + ν 2 ​ ( A + 1) + ν 2 ​ ( α + 1) − 1. \nu_{2}(A^{\alpha+1}-1)=\nu_{2}(A-1)+\nu_{2}(A+1)+\nu_{2}(\alpha+1)-1. |  |

Subtracting ν 2 ​ ( A − 1) \nu_{2}(A-1) from both sides yields

 | ν 2 ​ ( A α + 1 − 1 A − 1) = ν 2 ​ ( A + 1) + ν 2 ​ ( α + 1) − 1. \nu_{2}\!\left(\frac{A^{\alpha+1}-1}{A-1}\right)=\nu_{2}(A+1)+\nu_{2}(\alpha+1)-1. |  |

Since A = p k A=p^{k}, this becomes

 | ν 2 ​ ( σ k ​ ( p α)) = ν 2 ​ ( p k + 1) + ν 2 ​ ( α + 1) − 1. \nu_{2}(\sigma_{k}(p^{\alpha}))=\nu_{2}(p^{k}+1)+\nu_{2}(\alpha+1)-1. |  |

This completes the proof. ∎

The parity of k k leads to two especially simple formulas.

###### Corollary 2.5.

Assume that k k is odd. Then for every odd prime p p,

 | ν 2 ​ ( p k + 1) = ν 2 ​ ( p + 1). \nu_{2}(p^{k}+1)=\nu_{2}(p+1). |  |

Consequently,

 | ν 2 ​ ( σ k ​ ( p α)) = { 0, α ​ even, ν 2 ​ ( α + 1) + ν 2 ​ ( p + 1) − 1, α ​ odd. \nu_{2}(\sigma_{k}(p^{\alpha}))=\begin{cases}0,&\alpha\ \text{even},\\[2.84526pt] \nu_{2}(\alpha+1)+\nu_{2}(p+1)-1,&\alpha\ \text{odd}.\end{cases} |  |

###### Proof.

Since k k is odd,

 | p k + 1 = ( p + 1) ​ ( p k − 1 − p k − 2 + ⋯ − p + 1). p^{k}+1=(p+1)(p^{k-1}-p^{k-2}+\cdots-p+1). |  |

The second factor is a sum of k k odd integers, hence is itself odd. Therefore

 | ν 2 ​ ( p k + 1) = ν 2 ​ ( p + 1), \nu_{2}(p^{k}+1)=\nu_{2}(p+1), |  |

and the desired formula follows from Theorem 2.4. ∎

###### Corollary 2.6.

Assume that k k is even. Then for every odd prime p p,

 | ν 2 ​ ( p k + 1) = 1. \nu_{2}(p^{k}+1)=1. |  |

Consequently,

 | ν 2 ​ ( σ k ​ ( p α)) = { 0, α ​ even, ν 2 ​ ( α + 1), α ​ odd. \nu_{2}(\sigma_{k}(p^{\alpha}))=\begin{cases}0,&\alpha\ \text{even},\\[2.84526pt] \nu_{2}(\alpha+1),&\alpha\ \text{odd}.\end{cases} |  |

###### Proof.

If k k is even and p p is odd, then p 2 ≡ 1 ( mod 8) p^{2}\equiv 1\pmod{8}, so p k ≡ 1 ( mod 8) p^{k}\equiv 1\pmod{8}. Hence

 | p k + 1 ≡ 2 ( mod 8), p^{k}+1\equiv 2\pmod{8}, |  |

which implies ν 2 ​ ( p k + 1) = 1 \nu_{2}(p^{k}+1)=1. The formula now follows from Theorem 2.4. ∎

###### Theorem 2.7.

Let

 | n = 2 a ​ ∏ i = 1 r p i α i, n=2^{a}\prod_{i=1}^{r}p_{i}^{\alpha_{i}}, |  |

where p 1, …, p r p_{1},\dots,p_{r} are distinct odd primes. Then

 | ν 2 ​ ( σ k ​ ( n)) = ∑ 1 ≤ i ≤ r α i ​ odd ( ν 2 ​ ( α i + 1) + ν 2 ​ ( p i k + 1) − 1). \nu_{2}(\sigma_{k}(n))=\sum_{\begin{subarray}{c}1\leq i\leq r\\ \alpha_{i}\ \mathrm{odd}\end{subarray}}\bigl(\nu_{2}(\alpha_{i}+1)+\nu_{2}(p_{i}^{k}+1)-1\bigr). |  |

In particular,

 | ν 2 ​ ( σ k ​ ( n)) = ∑ 1 ≤ i ≤ r α i ​ odd ( ν 2 ​ ( α i + 1) + ν 2 ​ ( p i + 1) − 1) if ​ k ​ is odd, \nu_{2}(\sigma_{k}(n))=\sum_{\begin{subarray}{c}1\leq i\leq r\\ \alpha_{i}\ \mathrm{odd}\end{subarray}}\bigl(\nu_{2}(\alpha_{i}+1)+\nu_{2}(p_{i}+1)-1\bigr)\qquad\text{if }k\text{ is odd}, |  |

and

 | ν 2 ​ ( σ k ​ ( n)) = ∑ 1 ≤ i ≤ r α i ​ odd ν 2 ​ ( α i + 1) if ​ k ​ is even. \nu_{2}(\sigma_{k}(n))=\sum_{\begin{subarray}{c}1\leq i\leq r\\ \alpha_{i}\ \mathrm{odd}\end{subarray}}\nu_{2}(\alpha_{i}+1)\qquad\text{if }k\text{ is even}. |  |

###### Proof.

By multiplicativity,

 | ν 2 ​ ( σ k ​ ( n)) = ν 2 ​ ( σ k ​ ( 2 a)) + ∑ i = 1 r ν 2 ​ ( σ k ​ ( p i α i)). \nu_{2}(\sigma_{k}(n))=\nu_{2}(\sigma_{k}(2^{a}))+\sum_{i=1}^{r}\nu_{2}(\sigma_{k}(p_{i}^{\alpha_{i}})). |  |

Now apply Lemma 2.1 and Theorem 2.4. The two specialized formulas follow from Corollaries 2.5 and 2.6. ∎

## 3. Proof of the main theorem

We first treat the case where k k is odd.

###### Proposition 3.1.

Assume that k k is odd. Then for every n ≥ 2 n\geq 2,

 | ν 2 ​ ( σ k ​ ( n)) = ν 2 ​ ( σ ⁡ ( n)). \nu_{2}(\sigma_{k}(n))=\nu_{2}(\sigma(n)). |  |

###### Proof.

By Corollary 2.5, for each odd prime power p α p^{\alpha},

 | ν 2 ​ ( σ k ​ ( p α)) = { 0, α ​ even, ν 2 ​ ( α + 1) + ν 2 ​ ( p + 1) − 1, α ​ odd. \nu_{2}(\sigma_{k}(p^{\alpha}))=\begin{cases}0,&\alpha\text{ even},\\[2.84526pt] \nu_{2}(\alpha+1)+\nu_{2}(p+1)-1,&\alpha\text{ odd}.\end{cases} |  |

This is exactly the same formula as for k = 1 k=1; see [1, Theorem 3.2]. Moreover, Lemma 2.1 gives

 | ν 2 ​ ( σ k ​ ( 2 α)) = ν 2 ​ ( σ ⁡ ( 2 α)) = 0. \nu_{2}(\sigma_{k}(2^{\alpha}))=\nu_{2}(\sigma(2^{\alpha}))=0. |  |

The claim therefore follows from multiplicativity. ∎

As an immediate consequence of Proposition 3.1 and [1, Theorem 1.3], we obtain the following result.

###### Theorem 3.2.

Assume that k k is odd. Then for every n ≥ 2 n\geq 2,

 | ν 2 ​ ( σ k ​ ( n)) ≤ ⌈ log 2 ⁡ n ⌉. \nu_{2}(\sigma_{k}(n))\leq\lceil\log_{2}n\rceil. |  |

Moreover, equality holds if and only if n n is a product of distinct Mersenne primes.

We now turn to the case where k k is even.

###### Lemma 3.3.

Assume that k k is even, and let

 | n = ∏ i = 1 r p i α i n=\prod_{i=1}^{r}p_{i}^{\alpha_{i}} |  |

be odd. Then

 | ν 2 ​ ( σ k ​ ( n)) ≤ ∑ i = 1 r α i. \nu_{2}(\sigma_{k}(n))\leq\sum_{i=1}^{r}\alpha_{i}. |  |

###### Proof.

By Theorem 2.7,

 | ν 2 ​ ( σ k ​ ( n)) = ∑ α i ​ odd ν 2 ​ ( α i + 1). \nu_{2}(\sigma_{k}(n))=\sum_{\alpha_{i}\ \mathrm{odd}}\nu_{2}(\alpha_{i}+1). |  |

If α i \alpha_{i} is odd, then

 | 2 ν 2 ​ ( α i + 1) ≤ α i + 1, 2^{\nu_{2}(\alpha_{i}+1)}\leq\alpha_{i}+1, |  |

and therefore

 | ν 2 ​ ( α i + 1) ≤ log 2 ⁡ ( α i + 1) ≤ α i. \nu_{2}(\alpha_{i}+1)\leq\log_{2}(\alpha_{i}+1)\leq\alpha_{i}. |  |

It follows that

 | ν 2 ​ ( σ k ​ ( n)) ≤ ∑ α i ​ odd α i ≤ ∑ i = 1 r α i. \nu_{2}(\sigma_{k}(n))\leq\sum_{\alpha_{i}\ \mathrm{odd}}\alpha_{i}\leq\sum_{i=1}^{r}\alpha_{i}. |  |

∎

The next estimate will be used to isolate the equality case.

###### Lemma 3.4.

Let

 | n = ∏ i = 1 r p i α i n=\prod_{i=1}^{r}p_{i}^{\alpha_{i}} |  |

be an odd integer greater than 3 3, and put

 | Ω ⁡ ( n) = ∑ i = 1 r α i. \Omega(n)=\sum_{i=1}^{r}\alpha_{i}. |  |

Then

 | ⌊ log 2 ⁡ n ⌋ ≥ Ω ⁡ ( n) + 1. \lfloor\log_{2}n\rfloor\geq\Omega(n)+1. |  |

###### Proof.

We distinguish two cases.

*Case 1: Ω ⁡ ( n) = 1 \Omega(n)=1.*Then n = p n=p is an odd prime. Since n > 3 n>3, we have p ≥ 5 p\geq 5, and hence

 | ⌊ log 2 ⁡ n ⌋ ≥ ⌊ log 2 ⁡ 5 ⌋ = 2 = Ω ⁡ ( n) + 1. \lfloor\log_{2}n\rfloor\geq\lfloor\log_{2}5\rfloor=2=\Omega(n)+1. |  |

*Case 2: Ω ⁡ ( n) ≥ 2 \Omega(n)\geq 2.*Since every odd prime factor of n n is at least 3 3, we have

 | n ≥ 3 Ω ⁡ ( n). n\geq 3^{\Omega(n)}. |  |

Thus

 | log 2 ⁡ n ≥ Ω ⁡ ( n) ​ log 2 ​ 3. \log_{2}n\geq\Omega(n)\log_{2}3. |  |

Since log 2 ⁡ 3 > 3 / 2 \log_{2}3>3/2, it follows that

 | log 2 ⁡ n > 3 2 ​ Ω ​ ( n). \log_{2}n>\frac{3}{2}\,\Omega(n). |  |

Because Ω ⁡ ( n) ≥ 2 \Omega(n)\geq 2, we have

 | 3 2 ​ Ω ​ ( n) ≥ Ω ⁡ ( n) + 1. \frac{3}{2}\,\Omega(n)\geq\Omega(n)+1. |  |

Therefore

 | log 2 ⁡ n > Ω ⁡ ( n) + 1. \log_{2}n>\Omega(n)+1. |  |

As Ω ⁡ ( n) + 1 \Omega(n)+1 is an integer, this implies

 | ⌊ log 2 ⁡ n ⌋ ≥ Ω ⁡ ( n) + 1. \lfloor\log_{2}n\rfloor\geq\Omega(n)+1. |  |

∎

We are now ready to prove the even- k k case of Theorem 1.1.

###### Theorem 3.5.

Assume that k k is even. Then for every n ≥ 2 n\geq 2,

 | ν 2 ​ ( σ k ​ ( n)) ≤ ⌊ log 2 ⁡ n ⌋. \nu_{2}(\sigma_{k}(n))\leq\lfloor\log_{2}n\rfloor. |  |

Moreover, equality holds if and only if n = 3 n=3.

###### Proof.

Write

 | n = 2 a ​ m, n=2^{a}m, |  |

where m m is odd. By Lemma 2.2,

 | ν 2 ​ ( σ k ​ ( n)) = ν 2 ​ ( σ k ​ ( m)). \nu_{2}(\sigma_{k}(n))=\nu_{2}(\sigma_{k}(m)). |  |

We first prove the upper bound. If m = 1 m=1, then n = 2 a n=2^{a}, and Lemma 2.1 gives ν 2 ​ ( σ k ​ ( n)) = 0 \nu_{2}(\sigma_{k}(n))=0, so the assertion is clear. Thus we may assume that m > 1 m>1, and write

 | m = ∏ i = 1 r p i α i. m=\prod_{i=1}^{r}p_{i}^{\alpha_{i}}. |  |

By Lemma 3.3,

 | ν 2 ​ ( σ k ​ ( n)) = ν 2 ​ ( σ k ​ ( m)) ≤ ∑ i = 1 r α i. \nu_{2}(\sigma_{k}(n))=\nu_{2}(\sigma_{k}(m))\leq\sum_{i=1}^{r}\alpha_{i}. |  |

On the other hand,

 | log 2 ⁡ n ≥ log 2 ⁡ m = ∑ i = 1 r α i ​ log 2 ​ p i ≥ ∑ i = 1 r α i, \log_{2}n\geq\log_{2}m=\sum_{i=1}^{r}\alpha_{i}\log_{2}p_{i}\geq\sum_{i=1}^{r}\alpha_{i}, |  |

since each odd prime p i ≥ 3 p_{i}\geq 3 satisfies log 2 ⁡ p i > 1 \log_{2}p_{i}>1. Hence

 | ν 2 ​ ( σ k ​ ( n)) ≤ log 2 ⁡ n. \nu_{2}(\sigma_{k}(n))\leq\log_{2}n. |  |

Since the left-hand side is an integer, it follows that

 | ν 2 ​ ( σ k ​ ( n)) ≤ ⌊ log 2 ⁡ n ⌋. \nu_{2}(\sigma_{k}(n))\leq\lfloor\log_{2}n\rfloor. |  |

We now consider the equality case. Suppose that

 | ν 2 ​ ( σ k ​ ( n)) = ⌊ log 2 ⁡ n ⌋. \nu_{2}(\sigma_{k}(n))=\lfloor\log_{2}n\rfloor. |  |

We first show that a = 0 a=0, so that n n must be odd. Indeed, if a ≥ 1 a\geq 1, then

 | log 2 ⁡ n = log 2 ⁡ m + a, \log_{2}n=\log_{2}m+a, |  |

and therefore

 | ⌊ log 2 ⁡ n ⌋ ≥ ⌊ log 2 ⁡ m ⌋ + 1. \lfloor\log_{2}n\rfloor\geq\lfloor\log_{2}m\rfloor+1. |  |

But

 | ν 2 ​ ( σ k ​ ( n)) = ν 2 ​ ( σ k ​ ( m)), \nu_{2}(\sigma_{k}(n))=\nu_{2}(\sigma_{k}(m)), |  |

so equality for n n would imply

 | ν 2 ​ ( σ k ​ ( m)) ≥ ⌊ log 2 ⁡ m ⌋ + 1, \nu_{2}(\sigma_{k}(m))\geq\lfloor\log_{2}m\rfloor+1, |  |

contrary to the bound already established for m m. Hence a = 0 a=0.

Thus n n is odd. If n > 3 n>3, then Lemma 3.4 yields

 | ⌊ log 2 ⁡ n ⌋ ≥ Ω ⁡ ( n) + 1, \lfloor\log_{2}n\rfloor\geq\Omega(n)+1, |  |

where Ω ⁡ ( n) = ∑ i α i \Omega(n)=\sum_{i}\alpha_{i}, while Lemma 3.3 gives

 | ν 2 ​ ( σ k ​ ( n)) ≤ Ω ⁡ ( n). \nu_{2}(\sigma_{k}(n))\leq\Omega(n). |  |

Therefore

 | ν 2 ​ ( σ k ​ ( n)) < ⌊ log 2 ⁡ n ⌋, \nu_{2}(\sigma_{k}(n))<\lfloor\log_{2}n\rfloor, |  |

so equality is impossible for odd n > 3 n>3. It remains only to consider n = 3 n=3.

For n = 3 n=3, we have

 | σ k ​ ( 3) = 1 + 3 k. \sigma_{k}(3)=1+3^{k}. |  |

Since k k is even, 3 k ≡ 1 ( mod 8) 3^{k}\equiv 1\pmod{8}, and hence

 | 1 + 3 k ≡ 2 ( mod 8). 1+3^{k}\equiv 2\pmod{8}. |  |

Thus

 | ν 2 ​ ( σ k ​ ( 3)) = 1 = ⌊ log 2 ⁡ 3 ⌋. \nu_{2}(\sigma_{k}(3))=1=\lfloor\log_{2}3\rfloor. |  |

This proves that equality holds if and only if n = 3 n=3. ∎

Theorem 1.1 follows immediately from Theorems 3.2 and 3.5.

## References

- [1] T. Amdeberhan, V. H. Moll, V. Sharma, and D. Villamizar, Arithmetic properties of the sum of divisors, J. Number Theory 223 (2021), 325–349.
- [2] F. R. Beyl, Cyclic subgroups of the prime residue group, Amer. Math. Monthly 84 (1977), 46–48.
- [3] S. Hong, J. Zhao, and W. Zhao, The 2-adic valuations of Stirling numbers of the second kind, Int. J. Number Theory 8 (2012), 1057–1066.
- [4] P. P. Nielsen, Odd perfect numbers, Diophantine equations, and upper bounds, Math. Comp. 84 (2015), 2549–2567.
- [5] P. Ochem and M. Rao, Odd perfect numbers are greater than 10 1500 10^{1500}, Math. Comp. 81 (2012), 1869–1877.
- [6] M. Qiu and S. Hong, 2-adic valuations of Stirling numbers of the first kind, Int. J. Number Theory 15 (2019), 1827–1855.
- [7] G. Robin, Large values of the sum-of-divisors function and the Riemann hypothesis, J. Math. Pures Appl. (9) 63 (1984), 187–213.
- [8] J. Zhao and Y. Chen, p p -adic valuation of the sum of divisors, Front. Math. 20 (2025), 795–827.
- [9] J. Zhao, p p -adic valuation of σ k ​ ( n) \sigma_{k}(n), Bull. Aust. Math. Soc. (2026), doi:10.1017/S000497272510083X.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:ckm20@126.com
[4]: mailto:2745808109@qq.com
