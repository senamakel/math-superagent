<!-- source: https://arxiv.org/html/1409.3820v1 | converted from HTML -->

Lucas’ theorem: its generalizations, extensions and applications (1878–2014)

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1409.3820v1 [math.NT] 06 Sep 2014

† † 2010 Mathematics Subject Classification. Primary 11B75, 11A07, 05A10, 11B65; Secondary 11B37, 11B39, 11B50, 11B73. Keywords and phrases: prime, prime power, binomial coefficient, congruence modulo a prime (prime power), p p -adic expansion of an integer, Lucas’ theorem, Lucas’ congruence, Wolstenholme type congruence, Lucas type congruence, variation of Lucas’ theorem modulo prime powers, generalization of Lucas’ theorem, Lucas property, double Lucas property, generalized binomial coefficient, Fibonomial coefficient, Lucas u u -nomial coefficient, Gaussian q q -nomial coefficient, Pascal’s triangle, p p -Lucas property.

# Lucas’ theorem: its generalizations, extensions and applications (1878–2014)

Romeo Meštrović Address: Maritime Faculty, University of Montenegro, Dobrota 36, 85330 Kotor, Montenegro Email address: [romeo@ac.me][3]

###### Abstract.

In 1878 É. Lucas proved a remarkable result which provides a simple way to compute the binomial coefficient ( n m) {n\choose m} modulo a prime p p in terms of the binomial coefficients of the base- p p digits of n n and m m: If p p is a prime, n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} and m = m 0 + m 1 ​ p + ⋯ + m s ​ p s m=m_{0}+m_{1}p+\cdots+m_{s}p^{s} are the p p -adic expansions of nonnegative integers n n and m m, then

 | ( n m) ≡ ∏ i = 0 s ( n i m i) ( mod p). {n\choose m}\equiv\prod_{i=0}^{s}{n_{i}\choose m_{i}}\pmod{p}. |  |

The above congruence, the so-called Lucas’ theorem (or Theorem of Lucas), plays an important role in Number Theory and Combinatorics. In this article, consisting of six sections, we provide a historical survey of Lucas type congruences, generalizations of Lucas’ theorem modulo prime powers, Lucas like theorems for some generalized binomial coefficients, and some their applications.

In Section 1 we present the fundamental congruences modulo a prime including the famous Lucas’ theorem. In Section 2 we mention several known proofs and some consequences of Lucas’ theorem. In Section 3 we present a number of extensions and variations of Lucas’ theorem modulo prime powers. In Section 4 we consider the notions of the Lucas property and the double Lucas property, where we also present numerous integer sequences satisfying one of these properties or a certain Lucas type congruence. In Section 5 we collect several known Lucas type congruences for some generalized binomial coefficients. In particular, this concerns the Fibonomial coefficients, the Lucas u u -nomial coefficients, the Gaussian q q -nomial coefficients and their generalizations. Finally, some applications of Lucas’ theorem in Number Theory and Combinatorics are given in Section 6.

CONTENTS

1 Introduction 3

2 Lucas’ theorem and its variations 5

2.1 Lucas’ theorem . 5
2.2 Some consequences and extensions of Lucas’ theorem . 7

3 Lucas type congruences for prime powers 10

3.1 Wolstenholme type congruences . 10
3.2 Variations of Lucas’ theorem modulo prime powers . 11
3.3 Characterizations of Wolstenholme primes . 17

4 The Lucas property and the p p -Lucas property 18

4.1 The Lucas property and the double Lucas property . 18
4.2 Further Lucas type congruences . 23

5 Lucas type theorems for some generalized binomial coefficients 27

5.1 Generalized binomial coefficients and related Lucas type congruences . 27
5.2 Lucas type congruences for some classes of Lucas u u -nomial coefficients . 32

6 Some applications of Lucas’ theorem 36

6.1 Lucas’ theorem and the Pascal’s triangle . 36
6.2 Another applications of Lucas’s theorem . 40

References 43

Appendix 49

## 1. Introduction

Prime numbers have been studied since the earliest days of mathematics. Congruences modulo primes have been widely investigated since the time of Fermat. There are numerous useful and often remarkable congruences and divisibility results for binomial coefficients; see [36, Ch. XI] for older results and [52] for a modern perspective.

Let p p be a prime. Then by Fermat little theorem, for each integer a a not divisible by p p

 | a p − 1 ≡ 1 ( mod p). a^{p-1}\equiv 1\pmod{p}. |  |

Furthermore, by Wilson theorem, for any prime p p

 | ( p − 1)! + 1 ≡ 0 ( mod p). (p-1)!+1\equiv 0\pmod{p}. |  |

In attempting to discover some analogous expression which should be divisible by n 2 n^{2}, whenever n n is a prime, but not divisible if n n is a composite number, in 1819 Charles Babbage [9] is led to the congruence

 | ( 2 ​ p − 1 p − 1) ≡ 1 ( mod p 2) {2p-1\choose p-1}\equiv 1\pmod{p^{2}} |  |

for all primes p ≥ 3 p\geq 3. In 1862 J. Wolstenholme [142] proved that the above congruence holds modulo p 3 p^{3} for any prime p ≥ 5 p\geq 5.

The study of arithmetic properties of binomial coefficients has a rich history. As noticed in [52], many great mathematicians of the nineteenth century considered problems involving binomial coefficients modulo a prime power (for instance Babbage [9], Cauchy, Cayley, Gauss [45], Hensel, Hermite [57], Kummer [80], Legendre, Lucas [86] and [87], and Stickelberger). They discovered a variety of elegant and surprising theorems which are often easy to prove. For more information on these classical results, their extensions, and new results about this subject, see books of Dickson [36, Chapter IX] and Guy [53], while a more modern treatment of the subject is given by A. Granville [52].

Suppose that a prime p p and pair of integers n ≥ m ≥ 0 n\geq m\geq 0 are given. A beautiful theorem of E. Kummer of 1852 ( [80, pp. 115–116]; also see [36, p. 270]) states that the exact power of the prime p p which divides ( n m) {n\choose m} is given by the number of “carries” when m m and n − m n-m are added in base p p arithmetic. This is a fundamental result in the study of divisibility properties of binomial coefficients.

If n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} and m = m 0 + m 1 ​ p + ⋯ + m s ​ p s m=m_{0}+m_{1}p+\cdots+m_{s}p^{s} are the p p - adic expansions of nonnegative integers n n and m m (so that 0 ≤ m i, n i ≤ p − 1 0\leq m_{i},n_{i}\leq p-1 for each i i), then by Lucas’s theorem established by Édouard Lucas in 1878 [86] (also see [36, p. 271] and [52]),

 | ( n m) ≡ ∏ i = 0 s ( n i m i) ( mod p). {n\choose m}\equiv\prod_{i=0}^{s}{n_{i}\choose m_{i}}\pmod{p}. |  |

The same result is without proof also presented by Lucas in 1878, in Section XXI of his massive journal paper [87, pp. 229–230].

This remarkable result by Lucas provides a simple way to compute the binomial coefficient ( n m) {n\choose m} modulo a prime p p in terms of the binomial coefficients of the base- p p digits of n n and m m. The above congruence, the so-called Lucas’ theorem (or Theorem of Lucas) is a very important congruence in Combinatorial Number Theory and Combinatorics. In particular, this concerns the divisibility of binomial coefficients by primes. In this article, consisting of six sections, we provide a historical survey of Lucas type congruences, generalizations of Lucas’ theorem modulo prime powers and Lucas like theorems for some classes of generalized binomial coefficients. Furthermore, we present some known applications of Lucas’ theorem and certain of its variations in Number Theory and Combinatorics.

This article is organized as follows. In Section 2 we mention several known algebraic and combinatorial proofs of Lucas’ theorem. We also give some consequences and variations of Lucas’ theorem. In Section 3 we present a number of extensions and variations of Lucas’ theorem modulo prime powers. In Section 4 we consider the notions of the Lucas property and the double Lucas property. In this section we also present numerous integer sequences satisfying one of these properties or a certain similar Lucas type congruence. In particular, these properties are closely related to the divisibility properties of certain binomial coefficients, matrices, different binomial sums, Apéry numbers, Delannoy numbers, Stirling numbers of the first and second kind etc. In Section 5 we collect several known Lucas type congruences for some generalized binomial coefficients. In particular, this concerns the Fibonomial coefficients, the Lucas u u -nomial coefficients, the Gaussian q q -nomial coefficients and some their generalizations. Finally, applications of Lucas’ theorem are given in Section 6 of this survey article. Some of these applications are closely related to the determination of number of entries of Pascal’s triangle with a prescribed divisibility property. We also present some known primality criteria whose proofs are based on Lucas’ theorem. Furthermore, we give certain known results concerning the characterizations of the algebraicity of some classes of formal power series in terms of the notion of the p p -Lucas property.

## 2. Lucas’ theorem and its variations

### 2.1. Lucas’ theorem

As noticed above, if n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} and m = m 0 + m 1 ​ p + ⋯ + m s ​ p s m=m_{0}+m_{1}p+\cdots+m_{s}p^{s} are the p p - adic expansions of integers n n and m m such that 0 ≤ m i, n i ≤ p − 1 0\leq m_{i},n_{i}\leq p-1 for each i = 0, 1, …, s i=0,1,\ldots,s, then a beautiful Lucas’s theorem ( [86]; also see [52] ( [86] and [36, p. 271]) states that

(1) |  | ( n m) ≡ ∏ i = 0 s ( n i m i) ( mod p). {n\choose m}\equiv\prod_{i=0}^{s}{n_{i}\choose m_{i}}\pmod{p}. |  |

(with the usual convention that ( 0 0) = 1 {0\choose 0}=1, and ( l r) = 0 {l\choose r}=0 if l < r l<r). The congruence ( 1) was established by Lucas by considering patterns in Pascal’s triangle. Furthermore, ( 1) is equivalent to the following Lucas’ earlier generalization [86, p. 52] of an 1869 result of H. Anton [7, pp. 303–306] (also see [36, p. 271]):

(2) |  | ( n m) ≡ ( n ​ div ​ p m ​ div ​ p) ​ ( n mod p m mod p) ( mod p), {n\choose m}\equiv{n\,{\rm div}\,p\choose m\,{\rm div}\,p}{n\bmod{\,p}\choose m\bmod{p}}\pmod{p}, |  |

where n ​ div ​ p n\,{\rm div}\,p denotes the integer quotient of n n by a prime p p, and n mod p n\bmod{p} its remainder. The congruence ( 2) is in fact the equivalent form of Lucas’ theorem which is often stated in the follwing way:

(3) |  | ( n ​ p + r m ​ p + s) ≡ ( n m) ​ ( r s) ( mod p), {np+r\choose mp+s}\equiv{n\choose m}{r\choose s}\pmod{p}, |  |

where p p is a prime, n, m, r n,m,r and s s are nonnegative integers such that 0 ≤ r, s ≤ p − 1 0\leq r,s\leq p-1.

If a prime p p divides ( n m) {n\choose m} then ( 1) follows easily from Kummer’s theorem. However, if p l p^{l} is the exact power of p p dividing ( n m) {n\choose m}, then we might ask for the value of 1 p l ​ ( n m) ( mod p) \frac{1}{p^{l}}{n\choose m}(\bmod{\,p}). The related result was discovered by H. Anton in 1869 [7] (see also [52], [75, pp. 3–4] and [121]) who proved that if p l p^{l} is the exact power of p p dividing ( n m) {n\choose m}, ( ( l l is by Kummer’s theorem, the number of “carries” when m m and n − m n-m are added in base p p arithmetic)), then

(4) |  | ( − 1) l p l ( n m) ≡ n 0! m 0! ​ r 0! ⋅ n 1! m 1! ​ r 1! ⋯ n s! m s! ​ r s! ( mod p), \frac{(-1)^{l}}{p^{l}}{n\choose m}\equiv\frac{n_{0}!}{m_{0}!r_{0}!}\cdot\frac{n_{1}!}{m_{1}!r_{1}!}\cdots\frac{n_{s}!}{m_{s}!r_{s}!}\pmod{p}, |  |

where n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s}, m = m 0 + m 1 ​ p + ⋯ + m s ​ p s m=m_{0}+m_{1}p+\cdots+m_{s}p^{s}, and r = n − m = r 0 + r 1 ​ p + ⋯ + r s ​ p s r=n-m=r_{0}+r_{1}p+\cdots+r_{s}p^{s} with 0 ≤ m i, n i, r i ≤ p − 1 0\leq m_{i},n_{i},r_{i}\leq p-1 for each i = 0, 1, …, s i=0,1,\ldots,s.

Remark 1. Numerous authors have asked whether there is an analogous congruence modulo p l p^{l} to ( 4), for arbitrary l ≥ 1 l\geq 1. In 1995 A. Granville [52, Theorem 1] gave a positive answer to this question (see the congruence ( 33)) in Subsection 3.2). □ \Box

The several proofs offered for Lucas’ theorem are primarily of to types-algebraic and combinatorial. The well known algebraic proof of Lucas’ theorem due to N.J. Fine [39] in 1947 is based on the binomial theorem for expansion of ( 1 + x) n (1+x)^{n}. This proof runs as follows. Since by Kummer’s theorem, the binomial coefficient ( p k) {p\choose k} is divisible by a prime p p for every k = 1, 2, …, p − 1 k=1,2,\ldots,p-1, by the binomial expansion it follows that

 | ( 1 + X) p ≡ 1 + X p ( mod p). (1+X)^{p}\equiv 1+X^{p}\pmod{p}. |  |

Continuing by induction, we have that for every nonnegative integer i i

 | ( 1 + X) p i ≡ 1 + X p i ( mod p). (1+X)^{p^{i}}\equiv 1+X^{p^{i}}\pmod{p}. |  |

Write n n and m m in base p p, so that n = ∑ i = 1 s n i n=\sum_{i=1}^{s}n_{i} and m = ∑ i = 1 s m i m=\sum_{i=1}^{s}m_{i} for some nonnegative integers s, n 0, …, n s, m 0, …, m s s,n_{0},\ldots,n_{s},m_{0},\ldots,m_{s} with 0 ≤ n i, m i ≤ p − 1 0\leq n_{i},m_{i}\leq p-1 for all i = 0, 1, …, s i=0,1,\ldots,s. Then

 | ∑ m = 0 n ( n m) ​ X m = ( 1 + X) n = ∏ i = 0 s ( ( 1 + X) p i) n i ≡ ∏ i = 0 s ( 1 + X p i) n i = ∏ i = 0 s ( ∑ m i = 0 n i ( n i m i) ​ X m i ​ p i) ( mod p) = ∏ i = 0 s ( ∑ m i = 0 p − 1 ( n i m i) ​ X m i ​ p i) = ∑ m = 0 n ( ∏ i = 0 s ( n i m i)) ​ X m ( mod p). \begin{split}\sum_{m=0}^{n}{n\choose m}X^{m}&=(1+X)^{n}=\prod_{i=0}^{s}\left((1+X)^{p^{i}}\right)^{n_{i}}\\ &\equiv\prod_{i=0}^{s}\left(1+X^{p^{i}}\right)^{n_{i}}=\prod_{i=0}^{s}\left(\sum_{m_{i}=0}^{n_{i}}{n_{i}\choose m_{i}}X^{m_{i}p^{i}}\right)\pmod{p}\\ &=\prod_{i=0}^{s}\left(\sum_{m_{i}=0}^{p-1}{n_{i}\choose m_{i}}X^{m_{i}p^{i}}\right)\\ &=\sum_{m=0}^{n}\left(\prod_{i=0}^{s}{n_{i}\choose m_{i}}\right)X^{m}\pmod{p}.\end{split} |  |

By comparing the coefficients of X m X^{m} on the left hand side and on the right hand side of the above congruence immediately yields Lucas’ theorem given by ( 1).

As an application of a counting technique due to M. Hausner in 1983 [55], in the same paper [55, Example 4] the author established another combinatorial proof of ( 3). Another proof of the congruence ( 3) based on a simple combinatorial lemma is presented in 2005 by P.G. Anderson, A.T. Benjamin and J.A. Rouse in [6, p. 268] (see also [13]). Another two proofs of Lucas’ theorem, based on techniques from Elementary Number Theory were obtained in 2010 by S.-C. Liu and J.C.-C. Yeh [83] and in 2012 by A. Laugier and M.P. Saikia [82].

The congruence ( 3) immediately yields

(5) |  | ( n ​ p m ​ p) ≡ ( n m) ( mod p) {np\choose mp}\equiv{n\choose m}\pmod{p} |  |

since the same products of binomial coefficients are formed on the right side of Lucas’s theorem in both cases, other than an extra ( 0 0) = 1 {0\choose 0}=1.

A direct proof of the congruence ( 5), based on a polynomial method, is given in [133, Solution of Problem A-5, p. 173] as follows. It is well known that ( p i) ≡ 0 ( mod p) {p\choose i}\equiv 0(\bmod{\,p}) for each i = 1, 2, …, p − 1 i=1,2,\ldots,p-1 (see ( 11)) or equivalently that in the ring ℤ p ​ [x] \mathbb{Z}_{p}[x] we have ( 1 + x) p = 1 + x p (1+x)^{p}=1+x^{p}, where ℤ p \mathbb{Z}_{p} is the field of the integers modulo p p. Thus in ℤ p ​ [x] \mathbb{Z}_{p}[x],

 | ∑ k = 0 n ​ p ( n ​ p k) ​ x k = ( 1 + x) n ​ p = ( ( 1 + x) p) n = ( 1 + x p) n = ∑ j = 0 n ( n j) ​ x j ​ p. \sum_{k=0}^{np}{np\choose k}x^{k}=(1+x)^{np}=\left((1+x)^{p}\right)^{n}=(1+x^{p})^{n}=\sum_{j=0}^{n}{n\choose j}x^{jp}. |  |

Since coefficients of like powers must be congruent modulo p p in the equality

 | ∑ k = 0 n ​ p ( n ​ p k) ​ x k = ∑ j = 0 n ( n j) ​ x j ​ p \sum_{k=0}^{np}{np\choose k}x^{k}=\sum_{j=0}^{n}{n\choose j}x^{jp} |  |

in ℤ p ​ [x] \mathbb{Z}_{p}[x], we see that

 | ( n ​ p m ​ p) ≡ ( n m) ( mod p) f ​ o ​ r ​ m = 0, 1, …, n. {np\choose mp}\equiv{n\choose m}\pmod{p}\quad for\,\,m=0,1,\ldots,n. |  |

Further, notice that the Lucas’ congruence ( 3) easily follows by induction on the sum r + s ≥ 0 r+s\geq 0 using the base induction r + s = 0 r+s=0 with r = s = 0 r=s=0 satisfying via the congruence ( 5), and the Pascal formulas:

 | ( n ​ p + ( r + 1) m ​ p + s) = ( n ​ p + r m ​ p + ( s − 1)) + ( n ​ p + r m ​ p + s) {np+(r+1)\choose mp+s}={np+r\choose mp+(s-1)}+{np+r\choose mp+s} |  |

and

 | ( n ​ p + r m ​ p + ( s + 1)) = ( n ​ p + ( r − 1) m ​ p + s) + ( n ​ p + ( r − 1) m ​ p + ( s + 1)). {np+r\choose mp+(s+1)}={np+(r-1)\choose mp+s}+{np+(r-1)\choose mp+(s+1)}. |  |

Remark 2. The Lucas’ congruence ( 3) also can be interpreted as a result about cellular automata (cf. Granville [52, Section 5]). Namely, Lucas’ theorem can be interpreted as a two-dimensional p p -automaton (for a formal definition see [3]). □ \Box

### 2.2. Some consequences and extensions of Lucas’ theorem

Here, as always in the sequel, p p will denote any prime.

As noticed in 2011 by A. Nowicki [103, the congruences 7.3.1–7.33], if n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} is the p p -adic expansion of a positive integer n n, then for each k = 0, 1, …, s k=0,1,\ldots,s

(6) |  | ( n p k) ≡ n k ≡ ⌊ n p k ⌋ ( mod p), {n\choose p^{k}}\equiv n_{k}\equiv\left\lfloor\frac{n}{p^{k}}\right\rfloor\pmod{p}, |  |

holds, and consequently,

(7) |  | ( n p) ≡ ⌊ n p ⌋ ( mod p), {n\choose p}\equiv\left\lfloor\frac{n}{p}\right\rfloor\pmod{p}, |  |

where ⌊ x ⌋ \lfloor x\rfloor is the greatest integer less than or equal to x x.

Remark 3. The congruence ( 7) is proposed by L.E. Clarke [26] in 1956 as a problem which is solved in 1957 by P.A. Piza [108]. □ \Box

Moreover, if 0 ≤ r < p f 0\leq r<p^{f} and 0 ≤ m < p f 0\leq m<p^{f}, then the Lucas’ congruence ( 3) immediately yields ( ( see [103, the congruence 7.3.6]))

(8) |  | ( p f + r m) ≡ ( r m) ( mod p). {p^{f}+r\choose m}\equiv{r\choose m}\pmod{p}. |  |

Furthermore, if 0 ≤ r < p f 0\leq r<p^{f}, 0 ≤ m < p f 0\leq m<p^{f} and a ≥ 0 a\geq 0, then by Lucas’ theorem ( ( see [103, the congruence 7.3.7]),

(9) |  | ( a ​ p f + r m) ≡ ( r m) ( mod p). {ap^{f}+r\choose m}\equiv{r\choose m}\pmod{p}. |  |

Moreover, if 0 ≤ r < p f 0\leq r<p^{f} and p f ≤ m p^{f}\leq m, then by [103, the congruence 7.3.8],

(10) |  | ( p f + r m) ≡ ( r m − p f) ( mod p). {p^{f}+r\choose m}\equiv{r\choose m-p^{f}}\pmod{p}. |  |

Lucas’ theorem immediately yields the following well known congruence:

(11) |  | ( p k) ≡ 0 ( mod p), {p\choose k}\equiv 0\pmod{p}, |  |

where p p is a prime and k k is an integer such that 1 ≤ k ≤ p − 1 1\leq k\leq p-1.

Furthermore, if p p is a prime and f f a positive integer, then by Lucas’ theorem for any f ≥ 1 f\geq 1 and 1 ≤ k ≤ p f − 1 1\leq k\leq p^{f}-1 we have ( ( see, e.g., [13, Theorem 24]))

(12) |  | ( p f k) ≡ 0 ( mod p). {p^{f}\choose k}\equiv 0\pmod{p}. |  |

Further, if p p is a prime and n n, m m and k k are positive integers with m ≤ n m\leq n, then the congruence ( 5) by induction easily yields ( ( see [96, Lemma 2.1]))

(13) |  | ( n ​ p k m ​ p k) ≡ ( n m) ( mod p). {np^{k}\choose mp^{k}}\equiv{n\choose m}\pmod{p}. |  |

An alternative version of Lucas’ theorem was noticed in 1994 by J. M. Holte [60, p. 60] (also see [61, p. 227]) as follows: If

 | B ⁡ ( m, n):= ( m + n m) = ( m + n)! m! ​ n!, B(m,n):={m+n\choose m}=\frac{(m+n)!}{m!n!}, |  |

then

(14) |  | B ⁡ ( m, n) ≡ B ⁡ ( m ​ div ​ p, n ​ div ​ p) ​ B ​ ( m mod p, n mod p) ( mod p), B(m,n)\equiv B(m\,{\rm div}\,p,n\,{\rm div}\,p)B(m\bmod{\,p},n\bmod{\,p})\pmod{p}, |  |

where m ​ div ​ p m\,{\rm div}\,p is the integer quotient of m m by p p and m mod p m\bmod{\,p} is the remainder of m m by division by p p. ( ( similarly, for n n instead of m m)). It follows that if n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} and m = m 0 + m 1 ​ p + ⋯ + m s ​ p s m=m_{0}+m_{1}p+\cdots+m_{s}p^{s}, where 0 ≤ m i, n i ≤ p − 1 0\leq m_{i},n_{i}\leq p-1 for each i = 0, 1, … ​ s i=0,1,\ldots s, then

(15) |  | B ⁡ ( m, n) ≡ ∏ i = 0 s B ⁡ ( m i, n i) ( mod p). B(m,n)\equiv\prod_{i=0}^{s}B(m_{i},n_{i})\pmod{p}. |  |

Consequently, p | B ⁡ ( m, n) p\mid B(m,n) if and only if p | B ⁡ ( m i, n i) p\mid B(m_{i},n_{i}) for some i ∈ { 0, 1, …, s } i\in\{0,1,\ldots,s\}.

Following Granville [52, Section 6], for an integer polynomial f ⁡ ( X) f(X) of degree d d, define the numbers ( m n) f {m\choose n}_{f} with m, n ∈ ℤ m,n\in\mathbb{Z} by the generating function

 | f ​ ( X) m = ∑ n = 0 m ​ d ( m n) f ​ X n, f(X)^{m}=\sum_{n=0}^{md}{m\choose n}_{f}X^{n}, |  |

and let ( m n) f = 0 {m\choose n}_{f}=0 if n < 0 n<0 or n > m ​ d n>md (note that ( m n) f = ( m n) {m\choose n}_{f}={m\choose n} when f ⁡ ( X) = X + 1 f(X)=X+1). Clearly, by Fermat little theorem, f ​ ( X) p ≡ f ⁡ ( X p) ( mod p) f(X)^{p}\equiv f(X^{p})(\bmod{\,p}), and using this in 1995 A. Granville [52, Section 6, the congruence (24)] proved the following generalization of the congruence ( 4): If p p is a prime, m, n m,n nonnegative integers such that m = p ​ l + m 0 m=pl+m_{0}, n = p ​ t + n 0 n=pt+n_{0}, l, t, m 0, n 0 ∈ ℕ l,t,m_{0},n_{0}\in\mathbb{N} and 0 ≤ m 0, n 0 ≤ p − 1 0\leq m_{0},n_{0}\leq p-1, then

(16) |  | ( m n) f ≡ ∑ k = 0 d − 1 ( ⌊ m / p ⌋ ⌊ n / p ⌋ − k) f ​ ( m 0 n 0 + k ​ p) f ( mod p). {m\choose n}_{f}\equiv\sum_{k=0}^{d-1}{\lfloor m/p\rfloor\choose\lfloor n/p\rfloor-k}_{f}{m_{0}\choose n_{0}+kp}_{f}\pmod{p}. |  |

Notice that when f ⁡ ( X) = X + 1 f(X)=X+1 then the congruence ( 16) becomes

 | ( m n) ≡ ( ⌊ m / p ⌋ ⌊ n / p ⌋) ​ ( m 0 n 0) ( mod p), {m\choose n}\equiv{\lfloor m/p\rfloor\choose\lfloor n/p\rfloor}{m_{0}\choose n_{0}}\pmod{p}, |  |

which is in fact the Lucas’s congruence ( 3).

By using a congruence based on Burnside’s theorem, in 2005, T.J. Evans [38, Theorem 3] proved the following extension of Lucas’ theorem involving Euler’s totient function φ \varphi: If n ≥ 1 n\geq 1, m, M, m 0, r, R m,M,m_{0},r,R and r 0 r_{0} are nonnegative integers such that m = M ​ n + m 0 m=Mn+m_{0}, r = R ​ n + r 0 r=Rn+r_{0}, with 0 ≤ m 0, r 0 < n 0\leq m_{0},r_{0}<n, then

(17) |  | ∑ d | n φ ( n d) ∑ j = − ( d − 1) d − 1 ∑ ∥ a ∥ d = R − ( j / d) ( M a 1) ⋯ ( M a d) ( m 0 r 0 + ( n / d) ​ j) ≡ 0 ( mod n), \sum_{d\mid n}\varphi\left(\frac{n}{d}\right)\sum_{j=-(d-1)}^{d-1}\sum_{\lVert a\rVert_{d}=\atop R-(j/d)}{M\choose a_{1}}\cdots{M\choose a_{d}}{m_{0}\choose r_{0}+(n/d)j}\equiv 0\pmod{n}, |  |

where the summation runs among all positive divisors d d of n n.

Remark 4. It was proved in [38, Corollary 3] that Lucas’ theorem easily follows from the congruence ( 17). □ \Box

## 3. Lucas type congruences for prime powers

### 3.1. Wolstenholme type congruences

Notice that for any prime p p the congruence ( 5) with n = 2 n=2 and m = 1 m=1 becomes

 | ( 2 ​ p p) ≡ 2 ( mod p), {2p\choose p}\equiv 2\pmod{p}, |  |

whence by the identity ( 2 ​ p p) = 2 ​ ( 2 ​ p − 1 p − 1) {2p\choose p}=2{2p-1\choose p-1} it follows that for any prime p p

(18) |  | ( 2 ​ p − 1 p − 1) ≡ 1 ( mod p). {2p-1\choose p-1}\equiv 1\pmod{p}. |  |

As noticed in 1, in 1819 Charles Babbage [9] (also see [52, Introduction] or [36, page 271]) showed that the congruence ( 18) holds modulo p 2 p^{2}, that is, for a prime p ≥ 3 p\geq 3 holds

(19) |  | ( 2 ​ p − 1 p − 1) ≡ 1 ( mod p 2). {2p-1\choose p-1}\equiv 1\pmod{p^{2}}. |  |

Remark 5. A combinatorial proof of the congruence ( 19) can be found in [126, Exercise 14(c) on page 118]. □ \Box

The congruence ( 19) was generalized in 1862 by Joseph Wolstenholme [142] as it is presented in the next section. Namely, Wolstenholme’s theorem asserts that

(20) |  | ( 2 ​ p − 1 p − 1) ≡ 1 ( mod p 3) {2p-1\choose p-1}\equiv 1\pmod{p^{3}} |  |

for all primes p ≥ 5 p\geq 5.

For a survey of Wolstenholme’s theorem see [93] and for its extensions see [146] and [100].

By Glaisher’s congruence [49, p. 323] (also see [93, Section 6]), for any positive integer n n and a prime p ≥ 5 p\geq 5 holds

 | ( n ​ p − 1 p − 1) ≡ 1 ( mod p 3), {np-1\choose p-1}\equiv 1\pmod{p^{3}}, |  |

which by the identity ( n ​ p p) = n ​ ( n ​ p − 1 p − 1) {np\choose p}=n{np-1\choose p-1} yields [103, the congruence 7.1.5]

(21) |  | ( n ​ p p) ≡ n ( mod p 3). {np\choose p}\equiv n\pmod{p^{3}}. |  |

In 1949 W. Ljunggren [19] generalized the congruence ( 21) as follows (also see [10, Theorem 4], [52] and [126, Problem 1.6 (d)], and for a simple proof see [123]): if p ≥ 5 p\geq 5 is a prime, n n and m m are positive integers with m ≤ n m\leq n, then

(22) |  | ( n ​ p m ​ p) ≡ ( n m) ( mod p 3). {np\choose mp}\equiv{n\choose m}\pmod{p^{3}}. |  |

Remark 6. Ljunggren’s congruence ( 22) is refined modulo p 5 p^{5} in 2007 by J. Zhao [145, Theorem 3.5]. □ \Box

Remark 7. Note that the congruence ( 22) with m = 1 m=1 and n = 2 n=2 reduces to the Wolstenholme’s congruence ( 20). □ \Box.

Further, the congruence ( 22) is refined in 1952 by E. Jacobsthal [19] (also see [52]) as follows: if p ≥ 5 p\geq 5 is a prime, n n and m m are positive integers with m ≤ n m\leq n, then

(23) |  | ( n ​ p m ​ p) ≡ ( n m) ( mod p t), {np\choose mp}\equiv{n\choose m}\pmod{p^{t}}, |  |

where t t is the power of p p dividing p 3 ​ n ​ m ​ ( n − m) p^{3}nm(n-m) ( ( this exponent t t can only be increased if p p divides B p − 3 B_{p-3}, the ( p − 3) (p-3) rd Bernoulli number)).

Remark 8. In the literature, the congruence ( 23) is often called Jacobsthal-Kazandzidis congruence (see e.g., [27, Section 11.6, p. 380]). □ \Box

In 2008 C. Helou and G. Terjanian [56, the congruence (1) of Corollary on page 490] refined the Jacobsthal’s result as follows (also see [27, Section 11.6, Corollary 11.6.22, p. 381] for a stronger form)): If p ≥ 5 p\geq 5 is a prime, n n and m m are positive integers with m ≤ n m\leq n, then

(24) |  | ( n ​ p m ​ p) ≡ ( n m) ( mod p t), {np\choose mp}\equiv{n\choose m}\pmod{p^{t}}, |  |

where t t is the power of p p dividing p 3 ​ m ​ ( n − m) ​ ( n m) p^{3}m(n-m){n\choose m}.

By a problem N4 of Short list of 48th IMO 2006 [35], for every integer k ≥ 2 k\geq 2, 2 3 ​ k 2^{3k} divides the number

(25) |  | ( 2 k + 1 2 k) − ( 2 k 2 k − 1) {2^{k+1}\choose 2^{k}}-{2^{k}\choose 2^{k-1}} |  |

but 2 3 ​ k + 1 2^{3k+1} does not.

### 3.2. Variations of Lucas’ theorem modulo prime powers

In 1991 D.F. Bailey [11, Theorem 4] proved that if p p is a prime, n n and r r are nonnegative integers and s s a positive integer less than p p, then

(26) |  | ( n ​ p r ​ p + s) ≡ ( r + 1) ​ ( n r + 1) ​ ( p s) ( mod p 2). {np\choose rp+s}\equiv(r+1){n\choose r+1}{p\choose s}\pmod{p^{2}}. |  |

In the same paper [11, Theorem 5], the author extended the previous congruence as follows: if p ≥ 5 p\geq 5 is a prime, 0 ≤ m ≤ n 0\leq m\leq n, 0 ≤ r < p 0\leq r<p and 1 ≤ s < p 1\leq s<p, then

(27) |  | ( n ​ p 2 m ​ p 2 + r ​ p + s) ≡ ( m + 1) ​ ( n m + 1) ​ ( p 2 r ​ p + s) ( mod p 3). {np^{2}\choose mp^{2}+rp+s}\equiv(m+1){n\choose m+1}{p^{2}\choose rp+s}\pmod{p^{3}}. |  |

Remark 9. Notice that Bailey’s proof of the congruence ( 27) (proof of Theorem 5 in [10]) is deduced applying the Ljunggren’s congruence ( 22) (Theorem 4 in [10]) and a counting technique of M. Hausner from [55]. □ \Box

In 1992 D.F. Bailey [12, Theorem 2.1] generalized his congruence ( 27) modulo any prime power as follows: if p ≥ 5 p\geq 5 is a prime, 0 ≤ m ≤ n 0\leq m\leq n, s ≥ 1 s\geq 1, and a 0, a 1, …, a s − 1 a_{0},a_{1},\ldots,a_{s-1} are nonnegative integers such that 1 ≤ a 0 < p 1\leq a_{0}<p and 0 ≤ a k < p 0\leq a_{k}<p for every k = 1, 2, …, s − 1 k=1,2,\ldots,s-1, then

(28) |  | ( n ​ p s m ​ p s + a s − 1 ​ p s − 1 + ⋯ + a 1 ​ p + a 0) ≡ ( m + 1) ​ ( n m + 1) ​ ( p s a s − 1 ​ p s − 1 + ⋯ + a 1 ​ p + a 0) ( mod p s + 1). \begin{split}&{np^{s}\choose mp^{s}+a_{s-1}p^{s-1}+\cdots+a_{1}p+a_{0}}\\ &\equiv(m+1){n\choose m+1}{p^{s}\choose a_{s-1}p^{s-1}+\cdots+a_{1}p+a_{0}}\pmod{p^{s+1}}.\end{split} |  |

Remark 10. If we put a = a s − 1 ​ p s − 1 + ⋯ + a 1 ​ p + a 0 a=a_{s-1}p^{s-1}+\cdots+a_{1}p+a_{0}, then the congruence ( 28) can be written as

(29) |  | ( n ​ p s m ​ p s + a) ≡ ( m + 1) ​ ( n m + 1) ​ ( p s a) ( mod p s + 1), {np^{s}\choose mp^{s}+a}\equiv(m+1){n\choose m+1}{p^{s}\choose a}\pmod{p^{s+1}}, |  |

where a a is a positive integer less than p s p^{s} which is not divisible by p p. □ \Box.

Using a multiple application of Lucas’ theorem, in 2012 the author of this article [98, Theorem 1.1] proved the following similar congruence to ( 29):

(30) |  | ( n ​ p s m ​ p s + a) ≡ ( − 1) a − 1 ​ a − 1 ​ ( m + 1) ​ ( n m + 1) ​ p s ( mod p s + 1), {np^{s}\choose mp^{s}+a}\equiv(-1)^{a-1}a^{-1}(m+1){n\choose m+1}p^{s}\pmod{p^{s+1}}, |  |

where p p is a prime, n n, m m, s s and a a are nonnegative integers such that n ≥ m n\geq m, s ≥ 1 s\geq 1, 1 ≤ a ≤ p s − 1 1\leq a\leq p^{s}-1, and a a is not divisible by p p.

Remark 11. The congruence ( 29) is an immediate consequence of the congruence ( 30) (see [98, Corollary 1.2 and its proof]). □ \Box

In 1990 D.F. Bailey [10, Theorem 3] (cf. [97, Theorem with k = 2 k=2]) proved the following result: If p p is a prime, n, m, n 0 n,m,n_{0} and m 0 m_{0} are nonnegative integers, and n 0 n_{0} and m 0 m_{0} are both less than p p, then

(31) |  | ( n ​ p 2 + n 0 m ​ p 2 + m 0) ≡ ( n m) ​ ( n 0 m 0) ( mod p 2). {np^{2}+n_{0}\choose mp^{2}+m_{0}}\equiv{n\choose m}{n_{0}\choose m_{0}}\pmod{p^{2}}. |  |

Furthermore, in the same paper Bailey [10, Theorem 5] (cf. [97, Theorem with k = 3 k=3]) extended the above result as follows: If p p is a prime greater than 3 3 and n, m, n 0 n,m,n_{0} and m 0 m_{0} are nonnegative integers such that n 0 n_{0} and m 0 m_{0} are less than p p, then

(32) |  | ( n ​ p 3 + n 0 m ​ p 3 + m 0) ≡ ( n m) ​ ( n 0 m 0) ( mod p 3). {np^{3}+n_{0}\choose mp^{3}+m_{0}}\equiv{n\choose m}{n_{0}\choose m_{0}}\pmod{p^{3}}. |  |

Kummer’s theorem given in Section 1, is useful in situations where the binomial coefficient is divisible by a prime power. However, if the binomial coefficient is not congruent to zero modulo a prime, then the question remains for a way to simplify the expression. In 1995 A. Granville [52, Theorem 1] generalized Anton’s congruence ( 4) modulo prime powers as follows. For a given integer k k define ( k!) p (k!)_{p} to be the product of all integers less than or equal to k k, which are not divisible by p p. Suppose that prime power p f p^{f} and positive integers n n and m m are given with r:= n − m ≥ 0 r:=n-m\geq 0. Write n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} in base p p, and let N j N_{j} be the least positive residue of ⌊ n / p j ⌋ ( mod p f) \lfloor n/p^{j}\rfloor(\bmod{\,p^{f}}) for each j ≥ 0 j\geq 0 ( ( so that N j = n j + n j + 1 ​ p + ⋯ + n j + f − 1 ​ p f − 1 N_{j}=n_{j}+n_{j+1}p+\cdots+n_{j+f-1}p^{f-1});); also make the corresponding definitions for m j, M j, r j, R j m_{j},M_{j},r_{j},R_{j}. Let e j e_{j} be the number of indices i ≥ j i\geq j for which n i < m i n_{i}<m_{i} ( ( that is, the number of “carries” when adding m m and r r in base p p, on or beyond the j j th digit)). Then

(33) |  | 1 p e 0 ( n m) ≡ ( ± 1) e f − 1 ( N 0!) p ( M 0!) p ​ ( R 0!) p ⋅ ( N 1!) p ( M 1!) p ​ ( R 1!) p ⋯ ( N s!) p ( M s!) p ​ ( R s!) p ( mod p f), \frac{1}{p^{e_{0}}}{n\choose m}\equiv(\pm 1)^{e_{f-1}}\frac{(N_{0}!)_{p}}{(M_{0}!)_{p}(R_{0}!)_{p}}\cdot\frac{(N_{1}!)_{p}}{(M_{1}!)_{p}(R_{1}!)_{p}}\cdots\frac{(N_{s}!)_{p}}{(M_{s}!)_{p}(R_{s}!)_{p}}\pmod{p^{f}}, |  |

where ( ± 1) (\pm 1) is ( − 1) (-1) except if p = 2 p=2 and f ≥ 3 f\geq 3.

Here, as usually in the sequel, we will consider the congruence relation modulo a prime power p l p^{l} extended to the ring of rational numbers with denominators not divisible by p p. For such fractions we put m / n ≡ r / s ( mod p l) m/n\equiv r/s\,(\bmod{\,\,p^{l}}) if and only if m ​ s ≡ n ​ r ( mod p l) ms\equiv nr\,(\bmod{\,\,p^{l}}), and the residue class of m / n m/n is the residue class of m ​ n ′ mn^{\prime} where n ′ n^{\prime} is the inverse of n n modulo p l p^{l}.

A result which gives readily an extension of Lucas’ theorem in the form of the congruence to prime power moduli is given in 1992 by A. Granville [51, Proposition 2] as follows: For each positive integer j j, define n j n_{j} to be the least nonnegative residue of an integer n n modulo p j p^{j}. If p p is a prime that does not divide ( n m) {n\choose m}, then

(34) |  | ( n m) ≡ ( ⌊ n / p ⌋ ⌊ m / p ⌋) ​ ( n f m f) / ( ⌊ n f / p ⌋ ⌊ m f / p ⌋) ( mod p f), {n\choose m}\equiv{\lfloor n/p\rfloor\choose\lfloor m/p\rfloor}{n_{f}\choose m_{f}}\Bigg/{\lfloor n_{f}/p\rfloor\choose\lfloor m_{f}/p\rfloor}\pmod{p^{f}}, |  |

for any positive integer f f.

In particular, if ( n m) {n\choose m} is not divisible by p p and m ≡ n ( mod p f) m\equiv n(\bmod{\,p^{f}}), then by ( 34) ( ( also see [103, the congruence 7.1.16]))

(35) |  | ( n m) ≡ ( ⌊ n / p ⌋ ⌊ m / p ⌋) ( mod p f). {n\choose m}\equiv{\left\lfloor n/p\right\rfloor\choose\left\lfloor m/p\right\rfloor}\pmod{p^{f}}. |  |

As observed in 1998 by D. Berend and J.E. Harmse [15, p. 34, congruence (2.2)], if a prime p p does not divide ( n m) {n\choose m} and n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s}, m = m 0 + m 1 ​ p + ⋯ + m s ​ p s m=m_{0}+m_{1}p+\cdots+m_{s}p^{s} are the p p -adic expansions of n n and m m, then iterating the congruence ( 34), we find that

(36) |  | ( n m) ≡ P Q ( mod p f), {n\choose m}\equiv\frac{P}{Q}\pmod{p^{f}}, |  |

where

 | P = ∏ i = 0 k − f + 1 ( n i + n i + 1 ​ p + … + n i + f − 1 ​ p f − 1 m i + m i + 1 ​ p + … + m i + f − 1 ​ p f − 1) P=\prod_{i=0}^{k-f+1}{n_{i}+n_{i+1}p+\ldots+n_{i+f-1}p^{f-1}\choose m_{i}+m_{i+1}p+\ldots+m_{i+f-1}p^{f-1}} |  |

and

 | Q = ∏ i = 1 k − f + 1 ( n i + n i + 1 ​ p + … + n i + f − 2 ​ p f − 2 m i + m i + 1 ​ p + … + m i + f − 2 ​ p f − 2). Q=\prod_{i=1}^{k-f+1}{n_{i}+n_{i+1}p+\ldots+n_{i+f-2}p^{f-2}\choose m_{i}+m_{i+1}p+\ldots+m_{i+f-2}p^{f-2}}. |  |

The congruence ( 36) was established in 1991 independently by K. Davis and W. Webb [29, Theorem 3] (also see [85, p. 88, Theorem 5.1.2]), which is there formulated as follows: If n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s}, m = m 0 + m 1 ​ p + ⋯ + m s ​ p s m=m_{0}+m_{1}p+\cdots+m_{s}p^{s} are the p p -adic expansions of n n and m m, and l < s l<s, then

(37) |  | ( n m) ≡ ( n 0 + n 1 ​ p + ⋯ + n s − 1 ​ p s − 1 + n s ​ p s m 0 + m 1 ​ p + ⋯ + m s − 1 ​ p s − 1 + m s ​ p s) ≡ ( n s − l + ⋯ + n s ​ p s − l m s − l + ⋯ + m s ​ p s − l) ⋯ ( n 0 + ⋯ + n l ​ p s − l m 0 + ⋯ + m l ​ p s − l) ( n s − l + 1 + ⋯ + n s − 1 ​ p s − l − 1 m s − l + 1 + ⋯ + m s − 1 ​ p s − l − 1) ⋯ ( n 0 + ⋯ + n l − 1 ​ p s − l − 1 m 0 + ⋯ + m l − 1 ​ p s − l − 1) ( mod p l). \begin{split}{n\choose m}\equiv&{n_{0}+n_{1}p+\cdots+n_{s-1}p^{s-1}+n_{s}p^{s}\choose m_{0}+m_{1}p+\cdots+m_{s-1}p^{s-1}+m_{s}p^{s}}\\ \equiv&\frac{{n_{s-l}+\cdots+n_{s}p^{s-l}\choose m_{s-l}+\cdots+m_{s}p^{s-l}}\cdots{n_{0}+\cdots+n_{l}p^{s-l}\choose m_{0}+\cdots+m_{l}p^{s-l}}}{{n_{s-l+1}+\cdots+n_{s-1}p^{s-l-1}\choose m_{s-l+1}+\cdots+m_{s-1}p^{s-l-1}}\cdots{n_{0}+\cdots+n_{l-1}p^{s-l-1}\choose m_{0}+\cdots+m_{l-1}p^{s-l-1}}}\pmod{p^{l}}.\end{split} |  |

If a = a 0 + a 1 ​ p + ⋯ + a k − 1 ​ p k − 1 + a k ​ p k a=a_{0}+a_{1}p+\cdots+a_{k-1}p^{k-1}+a_{k}p^{k} and b = b 0 + b 1 ​ p + ⋯ + b k − 1 ​ p k − 1 + b k ​ p k b=b_{0}+b_{1}p+\cdots+b_{k-1}p^{k-1}+b_{k}p^{k} are the p p -adic expansions of a a and b b such that b k > a k b_{k}>a_{k}, then we define

 | ( a 0 + a 1 ​ p + ⋯ + a k − 1 ​ p k − 1 + a k ​ p k b 0 + b 1 ​ p + ⋯ + b k − 1 ​ p k − 1 + b k ​ p k) = p ​ ( a 0 + a 1 ​ p + ⋯ + a k − 1 ​ p k − 1 b 0 + b 1 ​ p + ⋯ + b k − 1 ​ p k − 1). {a_{0}+a_{1}p+\cdots+a_{k-1}p^{k-1}+a_{k}p^{k}\choose b_{0}+b_{1}p+\cdots+b_{k-1}p^{k-1}+b_{k}p^{k}}=p{a_{0}+a_{1}p+\cdots+a_{k-1}p^{k-1}\choose b_{0}+b_{1}p+\cdots+b_{k-1}p^{k-1}}. |  |

Remark 12. For help in understanding the above result concerning the congruence ( 37), we offer the following example [85, p. 88]:

 | ( 386 154) = ( 3 ⋅ 11 2 + 2 ⋅ 11 + 1 11 2 + 3 ⋅ 11) ≡ ( 3 ⋅ 11 + 2 11 + 3) ​ ( 2 ⋅ 11 + 1 3 ⋅ 11) ( 2 3) ( mod 11 2) ≡ ( 3 ⋅ 11 + 2 11 + 3) ​ ( 1 0) ≡ ( 35 14) ( mod 11 2). □ \begin{split}{386\choose 154}&={3\cdot 11^{2}+2\cdot 11+1\choose 11^{2}+3\cdot 11}\equiv\frac{{3\cdot 11+2\choose 11+3}{2\cdot 11+1\choose 3\cdot 11}}{{2\choose 3}}\pmod{11^{2}}\\ \qquad\qquad&\equiv{3\cdot 11+2\choose 11+3}{1\choose 0}\equiv{35\choose 14}\pmod{11^{2}}.\qquad\qquad\qquad\hfill\Box\end{split} |  |

In 2005 A.D. Loveless [85, p. 88] noticed that the above result concerning the congruence ( 37) can be used to simplify general classes of congruences modulo prime powers involving binomial coefficients. In particular, Loveless [85, p. 88, Theorem 5.1.3]) proved that if p p is a prime, s s and n n are positive integers with n ≤ p s n\leq p^{s}, then

(38) |  | ( p s n) ≡ { 0 ( mod p s) i ​ f ​ n ≢ 0 ( mod p) ( p s − 1 n / p) ( mod p s) i ​ f ​ p | n. {p^{s}\choose n}\equiv\left\{\begin{array}[]{ll}0&(\bmod{\,p^{s}})\quad if\,\,n\not\equiv 0\,(\bmod{\,p})\\ {p^{s-1}\choose n/p}&(\bmod{\,p^{s}})\quad if\,\,p\mid n.\end{array}\right. |  |

A similar result was earlier directly proved in 1980 by P.W. Haggard and J.O. Kiltinen [54, p. 398, Theorem]. This result asserts that if p p is a prime, l l and f f are positive integers with f ≥ l − 1 f\geq l-1 and 0 ≤ n ≤ p f 0\leq n\leq p^{f}, then

(39) |  | ( p f n) ≡ { 0 ( mod p l) i ​ f ​ n ≢ 0 ( mod p f − l + 1) ( p l − 1 i) ( mod p l) i ​ f ​ n = i ⋅ p f − l + 1. {p^{f}\choose n}\equiv\left\{\begin{array}[]{ll}0&(\bmod{\,p^{l}})\quad if\,\,n\not\equiv 0\,(\bmod{\,p^{f-l+1}})\\ {p^{l-1}\choose i}&(\bmod{\,p^{l}})\quad if\,\,n=i\cdot p^{f-l+1}.\end{array}\right. |  |

Using the congruence ( 37), in 1993 K. Davis and W. Webb [30] generalized Bailey’s results concerning the congruences ( 31) and ( 32) for any modulus p k p^{k} with p ≥ 5 p\geq 5 and k ≥ 1 k\geq 1. They proved [30, Theorem 3] that if p p is any prime, k, n, m, a, b k,n,m,a,b and s s are positive integers such that 0 < a, b < p s 0<a,b<p^{s}, then

(40) |  | ( n ​ p k + s + a m ​ p k + s + b) ≡ ( n ​ p k m ​ p k) ​ ( a b) ( mod p k + 1). {np^{k+s}+a\choose mp^{k+s}+b}\equiv{np^{k}\choose mp^{k}}{a\choose b}\pmod{p^{k+1}}. |  |

Remark 13. Notice that under the same assumption preceding the congruence ( 40), and if ( n ​ p k + s + a m ​ p k + s) ≢ 0 ( mod p) {np^{k+s}+a\choose mp^{k+s}}\not\equiv 0(\bmod{\,p}), then the congruence ( 40) can be obtained by iterating s s times the Granville’s congruence ( 34). Notice also that the condition ( n ​ p k + s + a m ​ p k + s) ≢ 0 ( mod p) {np^{k+s}+a\choose mp^{k+s}}\not\equiv 0(\bmod{\,p}) is by Lucas’ theorem equivalent to the following two conditions: ( n m) ≢ 0 ( mod p) {n\choose m}\not\equiv 0(\bmod{\,p}) and ( a b) ≢ 0 ( mod p) {a\choose b}\not\equiv 0(\bmod{\,p}). □ \Box

Further, by repeated application of the congruence ( 40), and using Ljunggren’s congruence ( 22), we find that under the same assumptions preceding the congruence ( 40) [30, Corollary 1] for any prime p > 3 p>3,

(41) |  | ( n ​ p k + s + a m ​ p k + s + b) ≡ ( n ​ p ⌊ k / 3 ⌋ m ​ p ⌊ k / 3 ⌋) ​ ( a b) ( mod p k + 1). {np^{k+s}+a\choose mp^{k+s}+b}\equiv{np^{\lfloor k/3\rfloor}\choose mp^{\lfloor k/3\rfloor}}{a\choose b}\pmod{p^{k+1}}. |  |

In particular, the congruence ( 41) with s = 1 s=1 and k − 1 ≥ 0 k-1\geq 0 instead of k k implies that for each prime p ≥ 5 p\geq 5 and for all integers k ≥ 1 k\geq 1, n ≥ 0 n\geq 0, a a and b b with 0 ≤ a, b < p 0\leq a,b<p

(42) |  | ( n ​ p k + a m ​ p k + b) ≡ ( n ​ p ⌊ ( k − 1) / 3 ⌋ m ​ p ⌊ ( k − 1) / 3 ⌋) ​ ( a b) ( mod p k). {np^{k}+a\choose mp^{k}+b}\equiv{np^{\lfloor(k-1)/3\rfloor}\choose mp^{\lfloor(k-1)/3\rfloor}}{a\choose b}\pmod{p^{k}}. |  |

Furthermore, the congruence ( 42) with ⌊ k / 2 ⌋ \lfloor k/2\rfloor instead of ⌊ ( k − 1) / 3 ⌋ \lfloor(k-1)/3\rfloor is satisfied for p = 2 p=2, and the congruence ( 42) with ⌊ ( k − 1) / 2 ⌋ \lfloor(k-1)/2\rfloor instead of ⌊ ( k − 1) / 3 ⌋ \lfloor(k-1)/3\rfloor is also satisfied for p = 3 p=3.

Remark 14. As noticed above, a proof of the congruence ( 41) given by Davis and Webb is based on their earlier result from [29] given by the congruence ( 41). However, this result together with related proof is slightly more complicated. In 2012 the author of this article [97, Theorem] gave a simple induction proof of the congruence ( 42) which uses only the usual properties of binomial coefficients. □ \Box

Adapting Fine’s method [39], in 1988 R.A. Macleod [88, Theorem 2] proved the following variation of Lucas’ theorem: Let p p be a prime, let r r be a positive integer, and let

 | M = ∑ i = 0 k M i ​ p i ​ r, w ​ i ​ t ​ h 0 ≤ M i < p r f ​ o ​ r ​ a ​ l ​ l ​ i = 0, 1, …, k. M=\sum_{i=0}^{k}M_{i}p^{ir},\quad with\quad 0\leq M_{i}<p^{r}\quad for\,\,all\,\,i=0,1,\ldots,k. |  |

Then for every nonnegative integer N N such that 0 ≤ N ≤ M 0\leq N\leq M

(43) |  | ( M N) ≡ ∑ ( p r − 1 ​ M 0 N 0) ( p r − 1 ​ M 1 N 1) ⋯ ( p r − 1 ​ M k N k) ( mod p r), {M\choose N}\equiv\sum{p^{r-1}M_{0}\choose N_{0}}{p^{r-1}M_{1}\choose N_{1}}\cdots{p^{r-1}M_{k}\choose N_{k}}\pmod{p^{r}}, |  |

where the summation ranges over all k + 1 k+1 -tuples ( N 0, N 1, …, N k) (N_{0},N_{1},\ldots,N_{k}) such that

 | p r − 1 ​ N = ∑ i = 0 k N i ​ p i ​ r, w ​ i ​ t ​ h 0 ≤ N i < p r − 1 ​ M i f ​ o ​ r ​ a ​ l ​ l ​ i = 0, 1, …, k. p^{r-1}N=\sum_{i=0}^{k}N_{i}p^{ir},\quad with\quad 0\leq N_{i}<p^{r-1}M_{i}\quad for\,\,all\,\,i=0,1,\ldots,k. |  |

Quite recently, in 2014 E. Rowland and R. Yassawi [115, Section 5, Theorem 5.3] established a new generalization of Lucas’ theorem to prime powers as follows: Let p p be a prime, let f f be a positive integer and let D = { 0, 1, …, p f − p f − 1 } D=\{0,1,\ldots,p^{f}-p^{f-1}\}. If n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} and m = m 0 + m 1 ​ p + ⋯ + m s ​ p s m=m_{0}+m_{1}p+\cdots+m_{s}p^{s} are the p p -adic expansions of nonnegative integers n n and m m, then

(44) |  | ( n m) ≡ ∑ ( i 0, …, i l) ∈ D l + 1 ( j 0, …, j l) ∈ D l + 1 ( − 1) n − i + ∑ h = 0 l i h ​ ( p f − 1 − 1 n − i) ​ ( n − i m − j) × ∏ h = 0 l ( p f − p f − 1 i h) ​ ( i h j h) ( mod p f), \begin{split}{n\choose m}\equiv&\sum_{(i_{0},\ldots,i_{l})\in D^{l+1}\atop(j_{0},\ldots,j_{l})\in D^{l+1}}(-1)^{n-i+\sum_{h=0}^{l}i_{h}}{p^{f-1}-1\choose n-i}{n-i\choose m-j}\\ &\times\prod_{h=0}^{l}{p^{f}-p^{f-1}\choose i_{h}}{i_{h}\choose j_{h}}\pmod{p^{f}},\end{split} |  |

where i = ∑ h = 0 l i h ​ p h i=\sum_{h=0}^{l}i_{h}p^{h} and j = ∑ h = 0 l j h ​ p h j=\sum_{h=0}^{l}j_{h}p^{h}.

Remark 15. Note that i = ∑ h = 0 l i h ​ p h i=\sum_{h=0}^{l}i_{h}p^{h} and j = ∑ h = 0 l j h ​ p h j=\sum_{h=0}^{l}j_{h}p^{h} are representations of integers i i and j j in base p p with an enlarged digit set D D rather than the standard digit set { 0, 1, …, p − 1 } \{0,1,\ldots,p-1\}. □ \Box

Remark 16. E. Rowland and R. Yassawi [115, Section 5] showed that a broad range of multidimensional sequences possess “Lucas products” modulo a prime p p. Furthermore, in 2009 K. Samol and D. van Straten [117, Proposition 4.1] established the Lucas type congruence for a sequence whose terms are constant terms of P ​ ( x) n P(x)^{n} for certain Laurent polynomials P ⁡ ( x) P(x). □ \Box

### 3.3. Characterizations of Wolstenholme primes

A prime p p is said to be a Wolstenholme prime if it satisfies the congruence

 | ( 2 ​ p − 1 p − 1) ≡ 1 ( mod p 4), {2p-1\choose p-1}\equiv 1\,(\bmod{\,p^{4}}), |  |

or equivalently,

(45) |  | ( 2 ​ p p) ≡ 2 ( mod p 4). {2p\choose p}\equiv 2\pmod{p^{4}}. |  |

The two known such primes are 16843 and 2124679, and R.J. McIntosh and E.L. Roettger reported in [91] that these primes are only two Wolstenholme primes less than 10 9 10^{9}. However, McIntosh in [90] conjectured that there are infinitely many Wolstenholme primes (for more information see [94]). By the well known result of J.W.L. Glaisher in 1900 [49, p. 323] (also see [95, the congruence (1.2)]),

(46) |  | ( 2 ​ p − 1 p − 1) ≡ 1 − 2 3 ​ p 3 ​ B p − 3 ( mod p 4), {2p-1\choose p-1}\equiv 1-\frac{2}{3}p^{3}B_{p-3}\pmod{p^{4}}, |  |

where B k B_{k} ( k = 0, 1, 2, … k=0,1,2,\ldots) are Bernoulli numbers defined by the generating function [71]

 | ∑ k = 0 ∞ B k ​ x k k! = x e x − 1. \sum_{k=0}^{\infty}B_{k}\frac{x^{k}}{k!}=\frac{x}{e^{x}-1}\,. |  |

The congruence ( 46) shows that a prime p p is a Wolstenholme prime if and only if p p divides the numerator of B p − 3 B_{p-3}, the ( p − 3) (p-3) rd Bernoulli number.

As an application of the congruences ( 42) with k = 4 k=4 and Jacobsthal’s congruence ( 23), we can obtain the following characterization of Wolstenholme primes given in 2012 by the author of this article [97, Proposition]: The following statements about a prime p ≥ 5 p\geq 5 are equivalent.

- (i)

p p is a Wolstenholme prime;

- (ii)

for all nonnegative integers n n and m m the congruence

(47) |  | ( n ​ p m ​ p) ≡ ( n m) ( mod p 4) {np\choose mp}\equiv{n\choose m}\pmod{p^{4}} |  |

holds;

- (iii)

for all nonnegative integers n, m, n 0 n,m,n_{0} and m 0 m_{0} such that n 0 n_{0} and m 0 m_{0} are less than p p,

(48) |  | ( n ​ p 4 + n 0 m ​ p 4 + m 0) ≡ ( n m) ​ ( n 0 m 0) ( mod p 4). {np^{4}+n_{0}\choose mp^{4}+m_{0}}\equiv{n\choose m}{n_{0}\choose m_{0}}\pmod{p^{4}}. |  |

## 4. The Lucas property and the p p -Lucas property

### 4.1. The Lucas property and the double Lucas property

In 1992 R.J. McIntosh [89] proposed the following definition:

Definition. The integer sequence ( a n) n ≥ 0 (a_{n})_{n\geq 0} has the Lucas property if a 0 = 1 a_{0}=1, and for every prime p p, every n ≥ 0 n\geq 0, and every j ∈ { 0, 1, …, p − 1 } j\in\{0,1,\ldots,p-1\} the congruence

(49) |  | a p ​ n + j ≡ a n ​ a j ( mod p) a_{pn+j}\equiv a_{n}a_{j}\pmod{p} |  |

holds. □ \Box

Remark 17. (cf. [1, p. 152, Remark 6.1]). Taking n = j = 0 n=j=0 in the congruence ( 49) gives a 0 ≡ a 0 2 ( mod p) a_{0}\equiv a_{0}^{2}(\bmod{\,p}). This yields that either a 0 ≡ 0 ( mod p) a_{0}\equiv 0(\bmod{\,p}) or a 0 ≡ 1 ( mod p) a_{0}\equiv 1(\bmod{\,p}). In the first case, taking n = 0 n=0 and j ∈ { 0, 1, …, p − 1 } j\in\{0,1,\ldots,p-1\} gives a j ≡ 0 ( mod p) a_{j}\equiv 0(\bmod{\,p}); hence a p ​ n + j ≡ a n ​ a j ≡ 0 ( mod p) a_{pn+j}\equiv a_{n}a_{j}\equiv 0(\bmod{\,p}) for all n n ’s and j j ’s. This means that a n a_{n} is a zero sequence modulo p p. What precedes implies that such a sequence either satisfies a n = 0 a_{n}=0 for all n ≥ 0 n\geq 0 or a 0 = 1 a_{0}=1. □ \Box

An analogous definition of double Lucas property is given also by McIntosh [89] as follows:

Definition. The function L: ℕ × ℕ → ℤ L:\mathbb{N}\times\mathbb{N}\rightarrow\mathbb{Z} has the double Lucas property if L ⁡ ( n, m) = 0 L(n,m)=0 for all n < m n<m, and for every prime p p, every n, m ≥ 0 n,m\geq 0, and every r, s r,s with 0 ≤ r, s ≤ p − 1 0\leq r,s\leq p-1 the congruence

(50) |  | L ⁡ ( n ​ p + r, m ​ p + s) ≡ L ⁡ ( n, m) ​ L ​ ( r, s) ( mod p) L(np+r,mp+s)\equiv L(n,m)L(r,s)\pmod{p} |  |

holds. □ \Box

Notice that Lucas’ theorem (the congruence ( 3)) and the congruence ( 14) show that both functions C ⁡ ( n, m), B ⁡ ( n, m): ℕ × ℕ → ℤ C(n,m),B(n,m):\mathbb{N}\times\mathbb{N}\rightarrow\mathbb{Z} defined as C ⁡ ( n, m) = ( n m) C(n,m)={n\choose m} and B ⁡ ( n, m) = ( n + m m) B(n,m)={n+m\choose m} have the double Lucas property. McIntosh [89] presents various properties of the function L ⁡ ( n, k) L(n,k) and their connection with tre Lucas property. A typical result is as follows: If L ⁡ ( n, m) L(n,m) has the double Lucas property, then the function F ⁡ ( n) = ∑ m = 0 n L ⁡ ( n, m) F(n)=\sum_{m=0}^{n}L(n,m) has the Lucas property.

In 1999 J.-P. Allouche [1, Proposition 7.1] proved the following result: Let m m be a positive integer, let e 1 = 2, e 2, …, e m e_{1}=2,e_{2},\ldots,e_{m} be integers such that e j ≤ e j + 1 ≤ 2 ​ e j e_{j}\leq e_{j+1}\leq 2e_{j} for j = 1, 2, …, m − 1 j=1,2,\ldots,m-1, and let r 1, r 2, …, r m r_{1},r_{2},\ldots,r_{m} be positive integers. Then the sequence ( u n) n ≥ 0 (u_{n})_{n\geq 0} defined by

(51) |  | u n = ( 2 ​ n n) r 1 ( e 2 ​ n 2 ​ n) r 2 ( e 3 ​ n e 2 ​ n) r 3 ⋯ ( e m ​ n e m − 1 ​ n) r m u_{n}={2n\choose n}^{r_{1}}{e_{2}n\choose 2n}^{r_{2}}{e_{3}n\choose e_{2}n}^{r_{3}}\cdots{e_{m}n\choose e_{m-1}n}^{r_{m}} |  |

has the Lucas property.

In particular, if e j + 1 − e j = 1 e_{j+1}-e_{j}=1 for all j = 1, 2, …, m − 1 j=1,2,\ldots,m-1, and r 1, r 2, …, r m r_{1},r_{2},\ldots,r_{m} are positive integers, then the above result implies that the sequence ( u n) n ≥ 0 (u_{n})_{n\geq 0} defined as

 | u n = ( 2 ​ n n) r 1 ( 3 ​ n n) r 2 ⋯ ( ( m + 1) ​ n n) r m u_{n}={2n\choose n}^{r_{1}}{3n\choose n}^{r_{2}}\cdots{(m+1)n\choose n}^{r_{m}} |  |

has the Lucas property ( ( see [89])).

The Apéry numbers A 1 ​ ( n) A_{1}(n) and A 2 ​ ( n) A_{2}(n) defined as

 | A 1 ( n) = ∑ k = 0 n ( n k) 2 ( n + k k) 2, A 2 ( n) = ∑ k = 0 n ( n k) 2 ( n + k k), n = 0, 1, …, A_{1}(n)=\sum_{k=0}^{n}{n\choose k}^{2}{n+k\choose k}^{2},A_{2}(n)=\sum_{k=0}^{n}{n\choose k}^{2}{n+k\choose k},\,\,n=0,1,\ldots, |  |

arose in Apéry’s proof in 1979 of the irrationality of ζ ⁡ ( 3) \zeta(3) [8]. ( A 1 ​ ( n)) n ≥ 0 (A_{1}(n))_{n\geq 0} and ( A 1 ​ ( n)) n ≥ 0 (A_{1}(n))_{n\geq 0} are Sloane’s sequences A005259 and A005258 in [124], respectively.

The Apéry numbers modulo a prime were studied in 1982 by I. Gessel who proved [47, Theorem 1] the following result: If n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} is the p p -adic expansion of n n, then

(52) |  | A 1 ​ ( n) ≡ ∏ i = 0 s A 1 ​ ( n i) ( mod p). A_{1}(n)\equiv\prod_{i=0}^{s}A_{1}(n_{i})\pmod{p}. |  |

In other words, the sequence ( A 1 ​ ( n)) n ≥ 1 (A_{1}(n))_{n\geq 1} has the Lucas property.

Similarly, the sequence ( A 2 ​ ( n)) n ≥ 0 (A_{2}(n))_{n\geq 0} satisfies the Lucas property ( ( see [31])).

In 2008 Y. Jin, Z-J. Lu and A.L. Schmidt [72, (ii) of Lemma 2] proved that the sums of powers of binomial coefficients have the Lucas property, that is: For a positive integer s s, let ( a n ( s)) n ≥ 0 (a_{n}^{(s)})_{n\geq 0} be a sequence defined as

 | a n ( s) = ∑ k = 0 n ( n k) s, n = 0, 1, 2, …. a_{n}^{(s)}=\sum_{k=0}^{n}{n\choose k}^{s},\quad n=0,1,2,\ldots. |  |

Then for every prime p p, every n ≥ 0 n\geq 0, and every j ∈ { 0, 1, …, p − 1 } j\in\{0,1,\ldots,p-1\} the congruence

(53) |  | a p ​ n + j ( s) ≡ a n ( s) ​ a j ( s) ( mod p) a_{pn+j}^{(s)}\equiv a_{n}^{(s)}a_{j}^{(s)}\pmod{p} |  |

holds.

Remark 18. The above result implies that the residues of Pascal’s triangle modulo p p have a self-similar structure (see, e.g., [42], [52, Section 5] and [141]). □ \Box

For a prime p p and a positive integer k k, in 1994 M. Razpet [111] considered the p k × p k p^{k}\times p^{k} matrix A ⁡ ( k, p) = [a i, j ​ ( k, p)] 0 ≤ i ≤ p k − 1 0 ≤ j ≤ p k − 1 A(k,p)=[a_{i,j}(k,p)]_{0\leq i\leq p^{k}-1}^{0\leq j\leq p^{k}-1}, whose the entry a i, j ​ ( k, p) a_{i,j}(k,p) is defined as the remainder of the division of ( i j) {i\choose j} by p p. In particular, for k = 1 k=1 we write A ⁡ ( p) = A ⁡ ( 1, p) = [a i, j ​ ( p)] 0 ≤ i ≤ p − 1 0 ≤ j ≤ p − 1 A(p)=A(1,p)=[a_{i,j}(p)]_{0\leq i\leq p-1}^{0\leq j\leq p-1}. M. Razpet [111] noticed that for every k ≥ 1 k\geq 1 and every prime p p, the matrix A ⁡ ( k, p) A(k,p) is the k k -fold tensor (or Kronecker) product of the matrix A ⁡ ( p) A(p) by itself in the field ℤ p \mathbb{Z}_{p}, that is, A ⁡ ( k, p) = A ⁡ ( p) ⊗ A ⁡ ( p) ⊗ ⋯ ⊗ A ⁡ ( p) ⏟ k = A ​ ( p) ⊗ k A(k,p)=\underbrace{A(p)\otimes A(p)\cdots\otimes A(p)}_{k}=A(p)^{\otimes{k}}. Note that matrix indices start at index pair ( 0, 0) (0,0). This is an algebraic and “square” representation of the oft-noted self-similarity structure of Pascal’s triangle (see, e.g., [58] and [141]).

Furthermore, as noticed in [111, p. 378], by Lucas’ theorem we have

(54) |  | a i, j ( k, p) ≡ a i 0, j 0 ( p) a i 1, j 1 ( p) ⋯ a i k − 1, j k − 1 ( p) ( mod p), a_{i,j}(k,p)\equiv a_{i_{0},j_{0}}(p)a_{i_{1},j_{1}}(p)\cdots a_{i_{k-1},j_{k-1}}(p)\pmod{p}, |  |

where 0 ≤ i, j ≤ p k − 1 0\leq i,j\leq p^{k}-1, i = i 0 + i 1 ​ p + ⋯ + i k − 1 ​ p k − 1 i=i_{0}+i_{1}p+\cdots+i_{k-1}p^{k-1} and j = j 0 + j 1 ​ p + ⋯ + j k − 1 ​ p k − 1 j=j_{0}+j_{1}p+\cdots+j_{k-1}p^{k-1} with 0 ≤ i l, j l ≤ p − 1 0\leq i_{l},j_{l}\leq p-1 for all l = 0, 1, …, k − 1 l=0,1,\ldots,k-1.

Remark 19. In [109] M. Prunescu pointed out that Pascal’s triangle modulo p k p^{k} is not a limit of tensor powers of matrices if k ≥ 2 k\geq 2. However, Pascal’s triangle modulo p k p^{k} are p p -automatic, and consequently can be produced by matrix substitution and are projections of double sequences produced by two-dimensional morphisms (see [4]). □ \Box

In 2003 D. Berend and N. Kriger [14, Theorem 5] proved that there exist uncountably many infinite matrices A = [a i, j] m, n = 0 ∞ A=[a_{i,j}]_{m,n=0}^{\infty} satisfying the double Lucas property, that is the congruences

(55) |  | a m, n ≡ ∏ i = 0 k a m i, n i ( mod p) a_{m,n}\equiv\prod_{i=0}^{k}a_{m_{i},n_{i}}\pmod{p} |  |

are satisfied for every prime p p and all nonnegative integers m m and n n with p p -adic expansions m = ∑ i = 0 k m i ​ p i m=\sum_{i=0}^{k}m_{i}p^{i} and n = ∑ i = 0 k n i ​ p i n=\sum_{i=0}^{k}n_{i}p^{i}.

In 1998 N.J. Calkin [21] investigated divisibility properties for sums of powers of binomial coefficients f n, a f_{n,a} defined as

 | f n, a = ∑ k = 0 n ( n k) a, f_{n,a}=\sum_{k=0}^{n}{n\choose k}^{a}, |  |

where n n and a a are nonnegative integers. Then f n, 0 = n + 1 f_{n,0}=n+1, f n, 1 = 2 n f_{n,1}=2^{n} and f n, 2 = ( 2 ​ n n) f_{n,2}={2n\choose n}. The sequences ( f n, a) n ≥ 0 (f_{n,a})_{n\geq 0} for a = 3, 4, 5, 6 a=3,4,5,6 are Sloane’s sequences A000172 (Franel numbers), A005260, A005261, A069865 in [124], respectively. Calkin [21, Lemma 4] proved that for every positive integer a a, the sequence ( f n, a) n ≥ 0 (f_{n,a})_{n\geq 0} has the Lucas property. This means that if p p is a prime and if n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} is the p p -adic expansion of n n, then

(56) |  | f n, a ≡ ∏ i = 0 s f n i, a ( mod p). f_{n,a}\equiv\prod_{i=0}^{s}f_{n_{i},a}\pmod{p}. |  |

Calkin [21, p. 21] also noticed that for any a ∈ { 1, 2, … } a\in\{1,2,\ldots\} the sequence ( h n, a) n ≥ 0 (h_{n,a})_{n\geq 0} defined as

 | h n, a = ∑ k = 0 n ( − 1) k ​ ( 2 ​ n k) a, h_{n,a}=\sum_{k=0}^{n}(-1)^{k}{2n\choose k}^{a}, |  |

also has the Lucas property.

For a positive integer n n the central trinomial coefficient T n T_{n} is the largest coefficient in the expansion ( 1 + x + x 2) n (1+x+x^{2})^{n} (Sloane’s sequence A002426 in [124]). It is easy to express T n T_{n} in terms of trinomial coefficients as

 | T n = ∑ k ≥ 0 ( n k, k, n − 2 ​ k), T_{n}=\sum_{k\geq 0}{n\choose k,k,n-2k}, |  |

where we use the convention that if any multinomial coefficient has a negative number on the bottom then the coefficient is zero. In 2006 E. Deutsch and B.E. Sagan [33] proved that the sequence ( T n) n ≥ 0 (T_{n})_{n\geq 0} has the Lucas property. Namely, by [33, Theorem 4.7] if p p is a prime and n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} is a positive integer with 0 ≤ n i ≤ p − 1 0\leq n_{i}\leq p-1 for all i = 0, 1, …, s i=0,1,\ldots,s, then

(57) |  | T n ≡ ∏ i = 0 s T n i ( mod p). T_{n}\equiv\prod_{i=0}^{s}T_{n_{i}}\pmod{p}. |  |

Furthermore, E. Deutsch and B.E. Sagan [33, Theorem 4.4] proved the following result for central binomial coefficients ( 2 ​ n n) {2n\choose n} (Sloane’s sequence A000984 in [124]): Let p p be a prime and let n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} be a positive integer with 0 ≤ n i ≤ p − 1 0\leq n_{i}\leq p-1 for all i = 0, 1, …, s i=0,1,\ldots,s. For every j ∈ { 0, 1, …, p − 1 } j\in\{0,1,\ldots,p-1\} let δ p, j ​ ( n) \delta_{p,j}(n) be the number of elements of the set { n 0, n 1, …, n s } \{n_{0},n_{1},\ldots,n_{s}\} equal to j j. Then

(58) |  | ( 2 ​ n n) ≡ { ∏ j ( 2 ​ j j) δ p, j ​ ( n) ( mod p) i f n i ≤ p / 2 f o r a l l i = 0, 1, … s, 0 ( mod p) o t h e r w i s e,, {2n\choose n}\equiv\left\{\begin{array}[]{ll}\prod_{j}{2j\choose j}^{\delta_{p,j}(n)}&\pmod{p}\quad if\,\,n_{i}\leq p/2\,\ for\,\,all\,\,i=0,1,\ldots s,\\ 0&\pmod{p}\quad otherwise,\end{array}\right., |  |

where the summation ranges over all j ∈ { 0, 1, …, p − 1 } j\in\{0,1,\ldots,p-1\} such that δ p, j ​ ( n) > 0 \delta_{p,j}(n)>0.

In 2009 M. Chamberland and K. Dilcher [25] studied the divisibility properties of the sums u ⁡ ( n) u(n) defined as

 | u ( n) = ∑ k = 0 n ( − 1) k ( n k) ( 2 ​ n k), n = 0, 1, 2, …. u(n)=\sum_{k=0}^{n}(-1)^{k}{n\choose k}{2n\choose k},\quad n=0,1,2,\ldots. |  |

Under this notation, the authors proved [25, Theorem 2.2] that for every prime p ≥ 3 p\geq 3 and all integers m ≥ 0 m\geq 0 and r r such that 0 ≤ r ≤ ( p − 1) / 2 0\leq r\leq(p-1)/2 we have

(59) |  | u ⁡ ( m ​ p + r) ≡ u ⁡ ( m) ​ u ​ ( r) ( mod p). u(mp+r)\equiv u(m)u(r)\pmod{p}. |  |

As an application, the authors proved [25, Corollary 2.1] that for every prime p ≥ 3 p\geq 3 and every integer n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} with 0 ≤ n i ≤ ( p − 1) / 2 0\leq n_{i}\leq(p-1)/2 for each i = 0, 1, …, s i=0,1,\ldots,s, we have

(60) |  | u ( n) ≡ u ( n 0) u ( n 1) ⋯ u ( n s) ( mod p). u(n)\equiv u(n_{0})u(n_{1})\cdots u(n_{s})\pmod{p}. |  |

Similarly, if the sums w ⁡ ( n) w(n) are defined as

 | w ( n) = ∑ k = 0 n − 1 ( − 1) k ( 2 ​ n − 1 k) ( n − 1 k), n = 0, 1, 2, …, w(n)=\sum_{k=0}^{n-1}(-1)^{k}{2n-1\choose k}{n-1\choose k},\quad n=0,1,2,\ldots, |  |

then by [25, Corollary 2.2], for all primes p ≥ 3 p\geq 3 and positive integers m m and r r with ( p + 1) / 2 ≤ r ≤ p − 1 (p+1)/2\leq r\leq p-1

(61) |  | u ⁡ ( m ​ p + r) ≡ w ⁡ ( m + 1) ​ u ​ ( r) ( mod p). u(mp+r)\equiv w(m+1)u(r)\pmod{p}. |  |

Remark 20. We point out that the Lucas property holds for a general family of sequences considered in 2006 by T.D. Noe [102]. □ \Box

For all nonnegative integers i i and j j let w ( i, j | a, b, c) w(i,j|a,b,c) denote the number of all paths in the plane from ( 0, 0) (0,0) to ( i, j) (i,j) with steps ( 1, 0) (1,0), ( 0, 1) (0,1), ( 1, 1) (1,1), and with positive integer weights a a, b b, c c, respectively. The explicit formula for w ( i, j | a, b, c) w(i,j|a,b,c) was obtained by several authors by using combinatorial arguments (see, e.g., [43]):

 | w ( i, j | a, b, c) = ∑ k ≥ 0 ( k i) ( i k − j) a k − j b k − i c i + j − k. w(i,j|a,b,c)=\sum_{k\geq 0}{k\choose i}{i\choose k-j}a^{k-j}b^{k-i}c^{i+j-k}. |  |

Actually, k k in the above sum runs from max ⁡ { i, j } \max\{i,j\} to i + j i+j. In the case a = b = c = 1 a=b=c=1, we have even the Delannoy numbers which count the usual, unweighted lattice paths from the point ( 0, 0) (0,0) to the point ( i, j) (i,j) with steps along the vectors ( 1, 0) (1,0), ( 0, 1) (0,1) and ( 1, 1) (1,1). If i = j = n i=j=n, then the numbers w ( n, n | 1, 1, 1) w(n,n|1,1,1), n = 0, 1, 2, … n=0,1,2,\ldots are called the central Delannoy numbers (Sloane’s sequence A001850 in [124]).

In 2002 M. Razpet [112, Theorem 1] proved the following double Lucas property of w ( i, j | a, b, c) w(i,j|a,b,c): Let p p be a prime and let α, β, γ, δ \alpha,\beta,\gamma,\delta be nonnegative integers where 0 ≤ β < p 0\leq\beta<p and 0 ≤ δ < p 0\leq\delta<p. Then the congruence

(62) |  | w ( α p + β, γ p + δ | a, b, c) ≡ w ( α, γ | a, b, c) w ( β, δ | a, b, c) ( mod p) w(\alpha p+\beta,\gamma p+\delta|a,b,c)\equiv w(\alpha,\gamma|a,b,c)w(\beta,\delta|a,b,c)\pmod{p} |  |

holds for all positive integers a, b, c a,b,c.

Remark 21. Razpet [112] notice that the congruence ( 62) is particularly true for the Delannoy numbers D ( i, j):= w ( i, j | 1, 1, 1) D(i,j):=w(i,j|1,1,1) as proven in another way in 1990 by M. Razpet [110] and by M. Sved and R.J. Clarke [132] (see also [33] and [37]). □ \Box

In 2004 H. Pan [106, Theorem 1] proved the following result: Suppose λ ⁡ ( x 1, …, x n) = ∑ Φ ≠ I ⊆ { 1, …, n } α I ​ ∏ i ∈ I X i \lambda(x_{1},\ldots,x_{n})=\sum_{\Phi\not=I\subseteq\{1,\ldots,n\}}\alpha_{I}\prod_{i\in I}X_{i}, α I ∈ 𝔽 \alpha_{I}\in\mathbb{F}, is a polynomial over the finite field 𝔽 \mathbb{F} with q q elements. Let w λ ​ ( k 1, …, k n) w_{\lambda}(k_{1},\ldots,k_{n}) be the coefficient of ∏ i = 1 n X i k i \prod_{i=1}^{n}X_{i}^{k_{i}} in the formal power series 1 1 − λ ⁡ ( x 1, …, x n) \frac{1}{1-\lambda(x_{1},\ldots,x_{n})}. Then w λ w_{\lambda} satisfies the double Lucas property, i.e., for any nonnegative integers a 1, …, a n a_{1},\ldots,a_{n} and 0 ≤ b 1, …, b n < q 0\leq b_{1},\ldots,b_{n}<q,

(63) |  | w λ ​ ( a 1 ​ q + b 1, …, a n ​ q + b n) = w λ ​ ( a 1, …, a n) ​ w λ ​ ( b 1, …, b n). w_{\lambda}(a_{1}q+b_{1},\ldots,a_{n}q+b_{n})=w_{\lambda}(a_{1},\ldots,a_{n})w_{\lambda}(b_{1},\ldots,b_{n}). |  |

Remark 22. If p p is a prime and 𝔽 \mathbb{F} is the field ℤ p = { 0, 1, …, p − 1 } \mathbb{Z}_{p}=\{0,1,\ldots,p-1\}, then the equality “ = = ” in ( 63) becomes ≡ 0 ( mod p) \equiv 0(\bmod{\,p}). □ \Box

### 4.2. Further Lucas type congruences

For nonnegative integers n n and k k Stirling numbers of the second kind { n k } {n\brace k} (Sloane’s sequence A008277 in [124]) are recursively defined as:

 | { n k } = { 1 if n = 0, k = 0, 0 if n > 0, k = 0, 0 if n = 0, k > 0, k ​ { n − 1 k } + { n − 1 k − 1 } if n > 0, k > 0. {n\brace k}=\left\{\begin{array}[]{ll}1&{\rm if}\,\,n=0,k=0,\\ 0&{\rm if}\,\,n>0,k=0,\\ 0&{\rm if}\,\,n=0,k>0,\\ k{n-1\brace k}+{n-1\brace k-1}&{\rm if}\,\,n>0,k>0.\end{array}\right. |  |

{ n k } {n\brace k} presents the number of ways of partitioning a set of n n elements into k k nonempty sets (i.e., k k set blocks). They (as well as Stirling numbers of the first kind defined below) are named after James Stirling, who introduced them in 1730 [127].

In 1988 M. Sved [131, p. 61, Theorem] showed the following result: Let n n and m m be nonnegative integers, and let p p be a an odd prime such that p p does not divide m m. Put

 | n ′ = ⌊ p ​ n − p ​ ⌊ m / p ⌋ − 1 p − 1 ⌋, n^{\prime}=\left\lfloor\frac{pn-p\lfloor m/p\rfloor-1}{p-1}\right\rfloor, |  |

and let n ′ = ∑ i = 0 h n i ′ ​ p i n^{\prime}=\sum_{i=0}^{h}n_{i}^{\prime}p^{i} and m = ∑ i = 0 h m i ​ p i m=\sum_{i=0}^{h}m_{i}p^{i} be the expansions of n ′ n^{\prime} and m m to base p p. Then

(64) |  | { n m } ≡ { n 0 ′ m 0 } ​ ∏ j = 1 h ( n j ′ m j). {n\brace m}\equiv{n_{0}^{\prime}\brace m_{0}}\prod_{j=1}^{h}{n_{j}^{\prime}\choose m_{j}}. |  |

In 2000 R. Sánchez-Peregrino [118, Proposition 3.1] proved that if n, m, r n,m,r and s s are nonnegative integers such that 0 ≤ s ≤ r ≤ p − 1 0\leq s\leq r\leq p-1 and m ≤ n ≤ p − 1 m\leq n\leq p-1, then

(65) |  | { n ​ p + r m ​ p + s } ≡ { n − m + r s } ​ ( n m) + { n − m + r + 1 s + p } ​ ( n m − 1) ( mod p). {np+r\brace mp+s}\equiv{n-m+r\brace s}{n\choose m}+{n-m+r+1\brace s+p}{n\choose m-1}\pmod{p}. |  |

Notice also that under the hypothesis that r + n − m + 1 < s + p r+n-m+1<s+p, the congruence ( 65) reduces to

(66) |  | { n ​ p + r m ​ p + s } ≡ { n − m + r s } ​ ( n m) ( mod p). {np+r\brace mp+s}\equiv{n-m+r\brace s}{n\choose m}\pmod{p}. |  |

Furthermore, by [118, Proposition 4.1], if r, s, a r,s,a and f f are nonnegative inegers, then

(67) |  | { a ​ p f + r s } ≡ ∑ i 0 + i 1 + ⋯ + i f ( a i 0, i 1, …, i f) ​ { r + i 0 s − ∑ l = 1 f i l ​ p f } ( mod p). {ap^{f}+r\brace s}\equiv\sum_{i_{0}+i_{1}+\cdots+i_{f}}{a\choose i_{0},i_{1},\ldots,i_{f}}{r+i_{0}\brace s-\sum_{l=1}^{f}i_{l}p^{f}}\pmod{p}. |  |

Remark 23. As noticed in [118, Remark 3.1], in the case r < p r<p the congruence ( 65) gives the formulas (4.17) and (4.18) of F.T. Howard [67] from 1990. □ \Box

For nonnegative integers n n and k k Stirling numbers of the first kind [n k] {n\brack k} (Sloane’s sequence A008275 in [124]) are defined by the recurrence relation

 | [n k] = { 1 if n = 0, k = 0, 0 if n > 0, k = 0, 0 if n = 0, k > 0, ( n − 1) ​ [n − 1 k] + [n − 1 k − 1] if n > 0, k > 0. {n\brack k}=\left\{\begin{array}[]{ll}1&{\rm if}\,\,n=0,k=0,\\ 0&{\rm if}\,\,n>0,k=0,\\ 0&{\rm if}\,\,n=0,k>0,\\ (n-1){n-1\brack k}+{n-1\brack k-1}&{\rm if}\,\,n>0,k>0.\end{array}\right. |  |

The absolute value of [n k] {n\brack k} (Sloane’s sequence A094638 in [124]) denotes, as usual, the number of permutations of n n elements which contain exactly k k permutation cycles.

In 1993 R. Peele, A.J. Radcliffe and H.S. Wilf [107, Proposition 2.1] proved the following analogue of Lucas’ theorem for the numbers [n k] {n\brack k}: Let p p be a prime and let n n and k k be integers with 1 ≤ k ≤ n 1\leq k\leq n. Let n ′ = ⌊ n / p ⌋ n^{\prime}=\lfloor n/p\rfloor and n 0 = n − n ′ ​ p n_{0}=n-n^{\prime}p. Further, define integers i i and j j as follows:

 | k − n ′ = j ⁡ ( p − 1) + i w ​ i ​ t ​ h ​ 0 ≤ i < p − 1 ​ i ​ f ​ n 0 = 0; 0 < i ≤ p − 1 ​ i ​ f ​ n 0 > 0. k-n^{\prime}=j(p-1)+i\quad with\,\,0\leq i<p-1\,\,if\,\,n_{0}=0;\,\,0<i\leq p-1\,\,if\,\,n_{0}>0. |  |

Then

(68) |  | [n k] ≡ ( − 1) n ′ − j ​ ( n ′ j) ​ [n 0 i] ( mod p). {n\brack k}\equiv(-1)^{n^{\prime}-j}{n^{\prime}\choose j}{n_{0}\brack i}\pmod{p}. |  |

For a nonnegative integer k k let J k ​ ( z) J_{k}(z) be the —it Bessel function of the first kind. Put

 | f k ​ ( z) = J k ​ ( 2 ​ z) z k / 2 = ∑ i = 0 ∞ ( − 1) i ​ z i i! ​ ( i + k)!. f_{k}(z)=\frac{J_{k}(2\sqrt{z})}{z^{k/2}}=\sum_{i=0}^{\infty}\frac{(-1)^{i}z^{i}}{i!(i+k)!}. |  |

Furthermore, define the polynomial u i ​ ( k, x) u_{i}(k;x) by means of

 | k! ​ f k ​ ( x ​ z) f k ​ ( z) = ∑ i = 0 ∞ u i ​ ( k, x) ​ z i i! ​ ( i + k)!. \frac{k!f_{k}(xz)}{f_{k}(z)}=\sum_{i=0}^{\infty}u_{i}(k;x)\frac{z^{i}}{i!(i+k)!}. |  |

Certain Lucas type congruences for w i ​ ( x) = u i ​ ( 0, x) w_{i}(x)=u_{i}(0;x) and the integers w i = w i ​ ( 0) w_{i}=w_{i}(0) with i = 0, 1, 2 ​ …, i=0,1,2\ldots, were derived by L. Carlitz [22] in 1955, and an interesting application was presented ( ( w n) n ≥ 0 (w_{n})_{n\geq 0} is Sloane’s sequence A000275). In 1987 F.T. Howard [66, Theorem 1] proved a more general result as follows: Let k k, n n and s s be nonnegative integers, and let p p be a prime such that p ≥ 2 ​ k p\geq 2k and s < p − 2 ​ k s<p-2k. Then the numbers u i ​ ( k):= u i ​ ( k, 0) u_{i}(k):=u_{i}(k;0) are integral ( mod p) (\bmod{\,p}) for all i = 0, 1, 2 ​ …; i=0,1,2\ldots; in particular, u n ​ ( 0) u_{n}(0) and u n ​ ( 1) u_{n}(1) are positive integers for all n = 0, 1, 2 ​ … n=0,1,2\ldots. Furthermore, for any fixed k ≥ 0 k\geq 0 and every prime p p the congruence

(69) |  | u n ​ p + s ​ ( k) ≡ u s ​ ( k) ⋅ w n ( mod p) u_{np+s}(k)\equiv u_{s}(k)\cdot w_{n}\pmod{p} |  |

holds for all n ≥ 0 n\geq 0 and 0 ≤ s ≤ n − 1 0\leq s\leq n-1.

With the assumptions of the above statement, if m m is a nonnegative integer with the expansion m = ∑ i = 0 s m i ​ p i m=\sum_{i=0}^{s}m_{i}p^{i} to base p p satisfying m 0 < p − 2 ​ k m_{0}<p-2k, then the congruence ( 70) with k = 0 k=0 implies Carlitz’s result [22] from 1955 which asserts that the sequence ( w n) n ≥ 0 (w_{n})_{n\geq 0} has the Lucas property, i.e.,

(70) |  | w m ≡ ∏ i = 0 s w m i ( mod p), w_{m}\equiv\prod_{i=0}^{s}w_{m_{i}}\pmod{p}, |  |

Furthermore, the following two congruences are satisfied [66, p. 306, Corollary and Theorem 2]:

(71) |  | u m ​ ( k) ≡ u m 0 ​ ( k) ​ ∏ i = 1 s w m i ​ ( 0) ( mod p), u_{m}(k)\equiv u_{m_{0}}(k)\prod_{i=1}^{s}w_{m_{i}}(0)\pmod{p}, |  |

and

(72) |  | u n ​ p − k ​ ( k) ≡ ( − 1) k ​ u 0 ​ ( k) ⋅ w n ​ ( 0) ( mod p). u_{np-k}(k)\equiv(-1)^{k}u_{0}(k)\cdot w_{n}(0)\pmod{p}. |  |

Let p p be a prime and let n, r, l n,r,l and a a be positive integers. Following Z.-W. Sun and D. Wan [130], the normalized cyclotomic ψ \psi -coefficient is defined as

(73) |  | { n r } l, p a:= p − { ⌊ n − p a − 1 − l ​ p a φ ⁡ ( p a) { ⌋ ∑ k ≡ r ( mod p a) ( − 1) k ( n k) ( ( k − r) / p a l). {n\brace r}_{l,p^{a}}:=p^{-\left\{\lfloor\frac{n-p^{a-1}-lp^{a}}{\varphi(p^{a})}\right\{\rfloor}\sum_{k\equiv r\,(\bmod{\,p^{a}})}(-1)^{k}{n\choose k}{(k-r)/p^{a}\choose l}. |  |

In 2008 Z.-W. Sun and D. Wan [130, Theorem 1.1] proved that if p p is any prime, r r is an integer and a, l, n, s, t a,l,n,s,t are positive integers with a ≥ 2 a\geq 2 and s, t < p s,t<p, then

(74) |  | { p ​ n + s p ​ r + t } l, p a + 1 ≡ ( − 1) t ​ ( s t) ​ { n r } l, p a ( mod p). {pn+s\brace pr+t}_{l,p^{a+1}}\equiv(-1)^{t}{s\choose t}{n\brace r}_{l,p^{a}}\pmod{p}. |  |

It is noticed in [130, Remark 1.1] that in the case l = 0 l=0 the congruence ( 74) is equivalent to Theorem 1.7 in [129] due to Z.-W. Sun and D.M. Davis in 2007. Under the same conditions preceeding the congruence ( 74), Sun and Davis [129, Theorem 1.7] proved the following congruence of Lucas’ type:

(75) |  | 1 ⌊ n / p a − 1 ⌋! ​ ∑ k ≡ r ( mod p a) ( − 1) p ​ k ​ ( p ​ n + s p ​ k + t) ​ ( k − r p a − 1) l ≡ 1 ⌊ n / p a − 1 ⌋! ​ ∑ k ≡ r ( mod p a) ( − 1) k ​ ( n k) ​ ( s t) ​ ( k − r p a − 1) l ( mod p). \begin{split}&\frac{1}{\lfloor n/p^{a-1}\rfloor!}\sum_{k\equiv r\,(\bmod{\,p^{a}})}(-1)^{pk}{pn+s\choose pk+t}\left(\frac{k-r}{p^{a-1}}\right)^{l}\\ \equiv&\frac{1}{\lfloor n/p^{a-1}\rfloor!}\sum_{k\equiv r\,(\bmod{\,p^{a}})}(-1)^{k}{n\choose k}{s\choose t}\left(\frac{k-r}{p^{a-1}}\right)^{l}\pmod{p}.\end{split} |  |

J. Boulanger and J.-L. Chabert [18] have extended Lucas’ theorem to Linear Algebra and Even Topology. Their result can be briefly exposed as follows. Let V V be a discrete valuation domain with finite residue field. Denote by K K the quotient field of V V, by v v the corresponding valuation of K K, by 𝔪 \mathfrak{m} the maximal ideal of V V, and by q q the cardinality of the residue field V / 𝔪 V/\mathfrak{m}. We denote by K ^ \widehat{K}, V ^ \widehat{V} and 𝔪 ^ \widehat{\mathfrak{m}} the completions of K K, V V and 𝔪 \mathfrak{m}, respectively, with respect to the 𝔪 \mathfrak{m} -adic topology and we still denote by v v the extension of v v to K ^ \widehat{K}. Consider the ring Int ⁡ ( V) {\rm Int}(V) of integer-valued polynomials on V V, that is,

 | Int ⁡ ( V) = { f ∈ K ⁡ [X]: f ⁡ ( V) ⊆ V }. {\rm Int}(V)=\{f\in K[X]:\,f(V)\subseteq V\}. |  |

A basis C n ​ ( X) C_{n}(X) of the V V -module Int ⁡ ( V) {\rm Int}(V) can be constructed as follows [20, Chapter II, §2 ]. We choose a generator t t of 𝔪 \mathfrak{m} and a set U = { u 0 = 0, u 1, …, u q − 1 } U=\{u_{0}=0,u_{1},\ldots,u_{q-1}\} of representatives of V V modulo 𝔪 \mathfrak{m}. It is known that each element x x of V ^ \widehat{V} has a unique t t -adic expansion

 | x = ∑ j = 0 ∞ x j ​ t j with ​ x j ∈ U ​ for ​ each ​ j ∈ ℕ. x=\sum_{j=0}^{\infty}x_{j}t^{j}\quad{\rm with}\,\,x_{j}\in U\,\,{\rm for\,\,each}\,\,j\in\mathbb{N}. |  |

We now construct a sequence ( u n) n ≥ 0 (u_{n})_{n\geq 0} of elements of V V which will replace the sequence of nonnegative integers. Taking q q as the basis of the numeration, that is, writing every positive integer n n in the form n = ∑ i = 0 k n i ​ q i n=\sum_{i=0}^{k}n_{i}q^{i} with 0 ≤ n i < q 0\leq n_{i}<q for each i = 0, 1, …, k i=0,1,\ldots,k, we extend the sequence ( u j) 0 ≤ j < k (u_{j})_{0\leq j<k} in the following way:

 | u n = u n 0 + u n 1 ​ t + u n 2 ​ t 2 + ⋯ + u n k ​ t k. u_{n}=u_{n_{0}}+u_{n_{1}}t+u_{n_{2}}t^{2}+\cdots+u_{n_{k}}t^{k}. |  |

We then replace the binomial polynomials

 | ( X n) = X ( X − 1) ( X − 2) ⋯ ( X − n + 1)) n! {X\choose n}=\frac{X(X-1)(X-2)\cdots(X-n+1))}{n!} |  |

( ( which form a basis of the ℤ \mathbb{Z} -module Int ⁡ ( ℤ) = { f ∈ ℚ ⁡ [X]: f ⁡ ( ℤ) ⊆ ℤ } {\rm Int}(\mathbb{Z})=\{f\in\mathbb{Q}[X]:\,f(\mathbb{Z})\subseteq\mathbb{Z}\} of integer-valued polynomials on ℤ \mathbb{Z})) by the polynomials defined as

 | C n ( X) = ∏ k = 0 n − 1 X − u k u n − u k, n = 1, 2, …, and C 0 = 1. C_{n}(X)=\prod_{k=0}^{n-1}\frac{X-u_{k}}{u_{n}-u_{k}},\,\,n=1,2,\ldots,\,\,{\rm and}\,\,C_{0}=1. |  |

Then by [20, Theorem II.2.7], the sequence of polynomials ( C n ​ ( X)) n ≥ 0 (C_{n}(X))_{n\geq 0} form a basis of the V V -module Int ⁡ ( V) {\rm Int}(V). In 2001 J. Boulanger and J.-L. Chabert [18, Theorem 2.2] proved the following “generalized Lucas’ theorem”: If

 | n = n 0 + n 1 ​ q + … + n k ​ q k n=n_{0}+n_{1}q+\ldots+n_{k}q^{k} |  |

is the q q -adic expansion of a positive integer n n, and if

 | x = x 0 + x 1 ​ t + … + x j ​ t j + … x=x_{0}+x_{1}t+\ldots+x_{j}t^{j}+\ldots |  |

is the t t -adic expansion of an element x x of V ^ \widehat{V}, then

(76) |  | C n ( x) ≡ C n 0 ( x 0) C n 1 ( x 1) ⋯ C n k ( x k) ( mod 𝔪 ^). C_{n}(x)\equiv C_{n_{0}}(x_{0})C_{n_{1}}(x_{1})\cdots C_{n_{k}}(x_{k})\pmod{\widehat{\mathfrak{m}}}. |  |

Remark 24. Notice also that in 1993 N. Zaheer [144] generalized Lucas’ theorem to vector-valued abstract polynomials in vector spaces. □ \Box

## 5. Lucas type theorems for some generalized binomial coefficients

### 5.1. Generalized binomial coefficients and related Lucas type congruences

Let A A and B B be nonzero integers. The Lucas sequence u 0, u 1, u 2, … u_{0},u_{1},u_{2},\ldots is defined recursively as

(77) |  | u 0 = 0, u 1 = 1 and u n + 1 = A u n − B u n − 1 for n = 1, 2, 3, …. u_{0}=0,u_{1}=1\quad{\rm and}\quad u_{n+1}=Au_{n}-Bu_{n-1}\quad{\rm for}\,\,n=1,2,3,\ldots. |  |

The companion sequence of Lucas sequence ( u n) n ≥ 0 (u_{n})_{n\geq 0} is the sequence ( v n) n ≥ 0 (v_{n})_{n\geq 0} recursively defined as

(78) |  | v 0 = 2, v 1 = A and v n + 1 = A v n − B v n − 1 for n = 1, 2, 3, …. v_{0}=2,v_{1}=A\quad{\rm and}\quad v_{n+1}=Av_{n}-Bv_{n-1}\quad{\rm for}\,\,n=1,2,3,\ldots. |  |

It is well known that for all n = 0, 1, 2, … n=0,1,2,\ldots

 | u n = α n − β n α − β and v n = α n + β n, u_{n}=\frac{\alpha^{n}-\beta^{n}}{\alpha-\beta}\quad{\rm and}\quad v_{n}=\alpha^{n}+\beta^{n}, |  |

where

 | α = A + Δ 2, β = A − Δ 2 and Δ = A 2 − 4 B. \alpha=\frac{A+\sqrt{\Delta}}{2},\beta=\frac{A-\sqrt{\Delta}}{2}\quad{\rm and}\quad\Delta=A^{2}-4B. |  |

In fact, α \alpha and β \beta are roots of the characteristic equation x 2 − A ​ x + B = 0 x^{2}-Ax+B=0. Note that for A = 1, B = − 1 A=1,B=-1 the terms of the sequence ( u n) n ≥ 0 (u_{n})_{n\geq 0} defined by ( 77) are the well-known Fibonacci numbers F n F_{n} defined recursively as F 0 = 0 F_{0}=0, F 1 = 1 F_{1}=1 and

 | F n + 1 = F n + F n − 1 for ​ n ≥ 1. F_{n+1}=F_{n}+F_{n-1}\quad{\rm for}\,\,n\geq 1. |  |

Fibonacci numbers are in fact the Lucas sequence ( u n) n ≥ 0 (u_{n})_{n\geq 0} given by ( 77) with u 0 = 0 u_{0}=0 and u 1 = 1 u_{1}=1.

Similarly, the Lucas numbers L n L_{n} are defined by L 0 = 2 L_{0}=2, L 1 = 1 L_{1}=1 and

 | L n + 1 = L n + L n − 1 for ​ n ≥ 1. L_{n+1}=L_{n}+L_{n-1}\quad{\rm for}\,\,n\geq 1. |  |

Fibonacci numbers F n F_{n} and Lucas numbers L n L_{n} are given as Sloane’s sequences A000045 and A000032 in [124], respectively.

Let a:= ( a n) n ≥ 0 a:=(a_{n})_{n\geq 0} be a sequence of real or complex numbers such that a n ≠ 0 a_{n}\not=0 for all n ≥ 1 n\geq 1. The a a - nomial coefficients (or the generalized binomial coefficients) (associated to the sequence a a) are defined by

 | [n k] a = a n a n − 1 ⋯ a 1 ( a k a k − 1 ⋯ a 1) ( a n − k a n − k − 1 ⋯ a 1) for ​ n ≥ 2 ​ and ​ 1 ≤ k ≤ n − 1, {n\brack k}_{a}=\frac{a_{n}a_{n-1}\cdots a_{1}}{(a_{k}a_{k-1}\cdots a_{1})(a_{n-k}a_{n-k-1}\cdots a_{1})}\quad{\rm for}\,\,n\geq 2\,\,{\rm and}\,\,1\leq k\leq n-1, |  |

and

 | [n 0] a = [n n] a = 1 for ​ n ≥ 0. {n\brack 0}_{a}={n\brack n}_{a}=1\quad{\rm for}\,\,n\geq 0. |  |

This definition was suggested in 1915 by Georges Fontené in his one-page note [41]. A number of authors have considered different classes of generalized binomial coefficients [n k] a {n\brack k}_{a} (usually, when a:= ( a n) n ≥ 0 a:=(a_{n})_{n\geq 0} is an integer sequence). Related investigations were done in 1913 by R.D. Carmichael [24], in 1936 by M. Ward, [136], in 1967 by R.D. Fray [42] and V.E. Hoggatt [59], in 1969 by H.W. Gould [50], and later by several authors ( [61], [62], [77], [79], [102], [134] and [135]). For example, in 1989 D.E. Knuth and H.S. Wilf [79, Proposition 3] generalized Kummer’s theorem for the a a -nomial coefficients [m + k m] a {m+k\brack m}_{a}, where a = ( a n) n ≥ 1 a=(a_{n})_{n\geq 1} is a sequence of positive integers. Consequently, they obtained [79, Theorems 1 and 2] Kummer’s theorem for the Gaussian q q -nomial coefficients [m + k m] q {m+k\brack m}_{q} where q > 1 q>1 is an integer and for the Fibonomial coefficients [m + k m] ℱ {m+k\brack m}_{\mathcal{F}} defined below, respectively.

In general, even if the all terms of a sequence a = ( a n) n ≥ 0 a=(a_{n})_{n\geq 0} are integers, [n k] a {n\brack k}_{a} may not be integers. In 1913 R.D. Carmichael [24, page 40] proved that if the sequence a:= ( a n) n ≥ 1 a:=(a_{n})_{n\geq 1} of positive integers is defined recursively as

 | a 1 = a 2 = 1, and a n + 1 = c ​ a n + d ​ a n − 1 for ​ n = 2, 3, 4, …, a_{1}=a_{2}=1,\quad{\rm and}\quad a_{n+1}=ca_{n}+da_{n-1}\quad{\rm for}\,\,n=2,3,4,\ldots, |  |

where c c and d d are integers, then the all a a -nomial coefficients are integers. For a more general result see Remark 28.

If u:= ( u n) n ≥ 0 u:=(u_{n})_{n\geq 0} is the Lucas sequence defined by ( 77), and if A ≠ ± 1 A\not=\pm 1 or B ≠ 1 B\not=1, then u 1, u 2, … u_{1},u_{2},\ldots are nonzero (see, e.g., [69]), and so are v 1 = u 2 / u 1 v_{1}=u_{2}/u_{1}, v 2 = u 4 / u 2, … v_{2}=u_{4}/u_{2},\ldots, where v:= ( v n) n ≥ 0 v:=(v_{n})_{n\geq 0} is the companion sequence of the sequence ( u n) n ≥ 0 (u_{n})_{n\geq 0} given by ( 78). In the case when A 2 = B = 1 A^{2}=B=1, then as noticed in [69] u n = 0 u_{n}=0 if and only if 3 | n 3\mid n. If v n = 0 v_{n}=0, then u 2 ​ n = u n ​ v n = 0 u_{2n}=u_{n}v_{n}=0; hence 3 | n 3\mid n and u n = 0 u_{n}=0, which is impossible since v n 2 − Δ ​ u n 2 = 4 ​ B n v_{n}^{2}-\Delta u_{n}^{2}=4B^{n} (cf. [68]). Thus v 0, v 1, v 2, … v_{0},v_{1},v_{2},\ldots are all nonzero.

If f A ≠ ± 1 A\not=\pm 1 or B ≠ 1 B\not=1 the Lucas u u -nomial coefficient [n k] u {n\brack k}_{u} with 1 ≤ k ≤ n 1\leq k\leq n is the generalized binomial coefficient associated to the Lucas sequence u:= ( u n) n ≥ 0 u:=(u_{n})_{n\geq 0} defined by ( 77), that is,

 | [n k] u = u n u n − 1 ⋯ u 1 ( u k u k − 1 ⋯ u 1) ( u n − k u n − k − 1 ⋯ u 1) for ​ n ≥ 2 ​ and ​ 1 ≤ k ≤ n − 1, {n\brack k}_{u}=\frac{u_{n}u_{n-1}\cdots u_{1}}{(u_{k}u_{k-1}\cdots u_{1})(u_{n-k}u_{n-k-1}\cdots u_{1})}\quad{\rm for}\,\,n\geq 2\,\,{\rm and}\,\,1\leq k\leq n-1, |  |

and [n 0] u = [n n] u = 1 {n\brack 0}_{u}={n\brack n}_{u}=1 for all n ≥ 0 n\geq 0.

In the sam way we define the v v - nomial generalized binomial coefficient [n k] v {n\brack k}_{v}, where v:= ( v n) n ≥ 0 v:=(v_{n})_{n\geq 0} is the companion sequence of the Lucas sequence ( u n) n ≥ 0 (u_{n})_{n\geq 0} defined by ( 78).

Remark 25. In the case A = 2 A=2 and B = 1 B=1, ( 77) yields u n = n u_{n}=n for all n = 0, 1, 2, … n=0,1,2,\ldots, and hence [n k] u {n\brack k}_{u} is exactly the binomial coefficient ( n k) {n\choose k}. □ \Box

Similarly, the Fibonomial coefficients (or Fibonacci coefficients) are defined as the generalized binomial coefficients associated to the sequence ( F n) n ≥ (F_{n})_{n\geq} of Fibonacci numbers, that is,

 | [n k] ℱ = F n F n − 1 ⋯ F 1 ( F k F k − 1 ⋯ F 1) ( F n − k F n − k − 1 ⋯ F 1) for ​ n ≥ 2 ​ and ​ 1 ≤ k ≤ n − 1, {n\brack k}_{\mathcal{F}}=\frac{F_{n}F_{n-1}\cdots F_{1}}{(F_{k}F_{k-1}\cdots F_{1})(F_{n-k}F_{n-k-1}\cdots F_{1})}\quad{\rm for}\,\,n\geq 2\,\,{\rm and}\,\,1\leq k\leq n-1, |  |

and [n 0] ℱ = [n n] ℱ = 1 {n\brack 0}_{\mathcal{F}}={n\brack n}_{\mathcal{F}}=1 for all n ≥ 0 n\geq 0.

The Fibonomial coefficients and the Lucas u u -nomial coefficients were introduced in 1878 by É. Lucas [87, §9], and later they have been studied by several authors (see [50], [59], [60], [139], [69] and [68]).

The triangle of Fibonomial coefficients is given as Sloane’s sequence A010048 in [124]. It is known (see, e.g., [59, the equality (D), page 386]) that

 | [n k] ℱ = F k + 1 ​ [n − 1 k] ℱ + F n − k − 1 ​ [n − 1 k − 1] ℱ, for ​ 0 ≤ k ≤ n − 1, {n\brack k}_{\mathcal{F}}=F_{k+1}{n-1\brack k}_{\mathcal{F}}+F_{n-k-1}{n-1\brack k-1}_{\mathcal{F}},\,\,{\rm for\,\,}0\leq k\leq n-1, |  |

whence by induction immediately follows that the all Fibonomial coefficients are integers.

When A = q + 1 A=q+1 and B = q B=q related to the sequence defined by ( 77), where q q is an integer such that | q | > 1 |q|>1, [n k] u {n\brack k}_{u}, then it coincides with the Gaussian q q -nomial coefficient [n k] q {n\brack k}_{q} because u j = ( q j − 1) / ( q − 1) u_{j}=(q^{j}-1)/(q-1) for j = 1, 2, … j=1,2,\ldots, and hence,

 | [n k] q = ( q n − 1) ( q n − 1 − 1) ⋯ ( q n − k + 1 − 1) ( q k − 1) ( q k − 1 − 1) ⋯ ( q − 1). {n\brack k}_{q}=\frac{(q^{n}-1)(q^{n-1}-1)\cdots(q^{n-k+1}-1)}{(q^{k}-1)(q^{k-1}-1)\cdots(q-1)}. |  |

The numbers [n k] q {n\brack k}_{q} were introduced in 1808 by Gauss [46, §5]. It is well known that these numbers satisfy the recursion formula

 | [n k] q = q k ​ [n − 1 k] q + [n − 1 k − 1] q, for ​ 0 ≤ k ≤ n − 1. {n\brack k}_{q}=q^{k}{n-1\brack k}_{q}+{n-1\brack k-1}_{q},\,\,{\rm for}\,\,0\leq k\leq n-1. |  |

The triangles of Gaussian q q -nomial coefficients for q = − 2, 2, 3, 4, 5, 6, 7, 8, 9 q=-2,2,3,4,5,6,7,8,9 are given as Sloane’s sequences A015109, A022166, A022167, A022168, A022169, A022170, A022171, A022172 and A022173 in [124], respectively.

It is easy to see that if 0 ≤ m ≤ n 0\leq m\leq n, then

 | lim q → 1 [n m] q = ( n m), \lim_{q\to 1}{n\brack m}_{q}={n\choose m}, |  |

 | [n m] q = [n n − m] q ( symmetry) {n\brack m}_{q}={n\brack n-m}_{q}\quad({\rm symmetry}) |  |

and

 | [n m] q = [n − 1 m − 1] q + q m ​ [n − 1 m] q, {n\brack m}_{q}={n-1\brack m-1}_{q}+q^{m}{n-1\brack m}_{q}, |  |

whence easily follows by induction that if q q is any positive integer, then [n m] q {n\brack m}_{q} are also integers for all n n and m m. □ \Box

Remark 26. An analogy to the Lucas u u -nomial coefficients [n k] u {n\brack k}_{u} was obtained in 1995 by W.A. Kimball and W.A. Webb [77] and in 1998 by B. Wilson [140] in some special cases, and in 2001 by H. Hu and Z.-W. Sun [69] for the general case (see Subsection 5.2). □ \Box

It is known (see, e.g., [84], [139]) that the generalized base for the Fibonacci sequence is

 | 𝒫 = { r 0, r 1, r 2, r 3, r 4, …, } = { 1, 3, 6, 6, 12, …, } \mathcal{P}=\{r_{0},r_{1},r_{2},r_{3},r_{4},\ldots,\}=\{1,3,6,6,12,\ldots,\} |  |

in the sense that any positive integer n n can be uniquely expressed as

 | n = ( n s ​ n s − 1 ​ … ​ n 1 ​ n 0) 𝒫:= n 0 + n 1 ​ r 1 + ⋯ + n s − 1 ​ r s − 1 + n s ​ r s, n=(n_{s}n_{s-1}\ldots n_{1}n_{0})_{\mathcal{P}}:=n_{0}+n_{1}r_{1}+\cdots+n_{s-1}r_{s-1}+n_{s}r_{s}, |  |

where 0 ≤ n i < r i + 1 / r i 0\leq n_{i}<r_{i+1}/r_{i} for each i = 0, 1, …, s − 1 i=0,1,\ldots,s-1.

Under the above notations, in 1994 D.L. Wells [139, Theorem 2] proved that

(79) |  | [n k] ℱ ≡ [n 0 k 0] ℱ ⋅ ∏ i ≥ 1 ( n i k i) ( mod 2). {n\brack k}_{\mathcal{F}}\equiv{n_{0}\brack k_{0}}_{\mathcal{F}}\cdot\prod_{i\geq 1}{n_{i}\choose k_{i}}\pmod{2}. |  |

In 1988 M. Sved [131] establihed that the geometry of the binomial arrays of Pascal’s triangle modulo p p gives a simple interpretation of Lucas’ theorem. Moreover, as noticed in [131, p. 58], this interpretation can be extended to arrays of other combinatorial functions; in particular, Lucas’ theorem can be generalized to the Gaussian q q -nomial coefficients as follows. Let p p be a prime, q > 1 q>1 a positive integer not divisible by p p, and let a ≠ 1 a\not=1 be the minimal exponent for which q a ≡ 1 ( mod p) q^{a}\equiv 1\,(\bmod{\,p}); then by Fermat little theorem it follows that a | ( p − 1) a\mid(p-1). Further, if n = N ​ a + n 0 n=Na+n_{0}, m = M ​ a + m 0 m=Ma+m_{0} with 0 ≤ n 0 < a 0\leq n_{0}<a and 0 ≤ m 0 < a 0\leq m_{0}<a, then [131, p. 60]

(80) |  | [n m] q ≡ ( N M) ​ [n 0 m 0] q ( mod p). {n\brack m}_{q}\equiv{N\choose M}{n_{0}\brack m_{0}}_{q}\pmod{p}. |  |

Remark 27. In the same area of research A. Bès [16] generalized Lucas’ theorem. This accomplishment obviously serves to improve the security of cryptographic applications modulo prime powers [16]. □ \Box

Definition. For a positive integer d d, the rank of apparition r = r ⁡ ( d) r=r(d) with respect to the integer sequence ( a n) n ≥ 0 (a_{n})_{n\geq 0} is the least index n n for which d d divides a n a_{n}, that is, r ( d) = min { n ∈ ℕ: d ∣ a n } r(d)=\min\{n\in\mathbb{N}:\,d\mid a_{n}\} (if d d does not divide any a n a_{n}, then r ⁡ ( d) = ∞ r(d)=\infty). □ \Box

Remark 28. Let a = ( a n) n ≥ 0 a=(a_{n})_{n\geq 0} be an integer sequence. In order to guarantee that the all a a -nomial coefficients [n k] a = 0 {n\brack k}_{a}=0 are integers, it is usually required that the sequence a = ( a n) n ≥ 0 a=(a_{n})_{n\geq 0} be regularly divisible, that is, p i | a j p^{i}\mid a_{j} if and only if r ⁡ ( p i) | j r(p^{i})\mid j for all i ≥ 1 i\geq 1, j ≥ 1 j\geq 1, and all primes p p. Here r ⁡ ( p i) r(p^{i}) denotes the rank of apparition og p i p^{i} as defined above. The principal class of sequences which are known to be regularly divisible are the Lucas sequences given by ( 77) for which gcd ⁡ ( A, B) = 1 \gcd(A,B)=1 (see [63]). □ \Box

In 2000 J.M. Holte [61, Theorem 1] proved the following result: Let p p be a prime and let m m and n n be nonnegative integers. Let r r be the rank of apparition of p p with respect to the Lucas sequence u = ( u n) u=(u_{n}), let τ \tau be the period of ( u n) (u_{n}) modulo p p, and let t = τ / r t=\tau/r ( ( t t is necessarily a positive integer)). Furthermore, for i, j ≥ 0 i,j\geq 0 and for 0 ≤ k, l < r 0\leq k,l<r, let A i, j ​ ( k, l) A_{i,j}(k,l) denote the solution of the modulo p p recurrence relation

 | A i, j ​ ( k, l) ≡ u i ​ r + k + 1 ​ A i, j ​ ( k, l − 1) + b ​ u j ​ r + l − 1 ​ A i, j ​ ( k − 1, l) ( mod p), A_{i,j}(k,l)\equiv u_{ir+k+1}A_{i,j}(k,l-1)+bu_{jr+l-1}A_{i,j}(k-1,l)\pmod{p}, |  |

and let H i, j ​ ( k, l) = u r + 1 r ​ i ​ j ​ A i, j ​ ( k, l) H_{i,j}(k,l)=u_{r+1}^{rij}A_{i,j}(k,l). Set n 0 = n ( mod r) n_{0}=n(\bmod{\,r}), m 0 = m ( mod r) m_{0}=m(\bmod{\,r}), n ′ = n + r n^{\prime}=n+r, m ′ = m + r m^{\prime}=m+r, n ′′ = n ′ ( mod t) n^{\prime\prime}=n^{\prime}(\bmod{\,t}), and m ′′ = m ′ ( mod t) m^{\prime\prime}=m^{\prime}(\bmod{\,t}). Then

(81) |  | [m + n n] u ≡ ( m ′ + n ′ n ′) ​ H m ′′, n ′′ ​ ( m 0, n 0) ( mod p). {m+n\brack n}_{u}\equiv{m^{\prime}+n^{\prime}\choose n^{\prime}}H_{m^{\prime\prime},n^{\prime\prime}}(m_{0},n_{0})\pmod{p}. |  |

Using the above result, with the same notations as above, Holte [61, Theorem 3] also proved the following result: Let ( u n) (u_{n}) be the Lucas sequence defined by ( 77), let p p be a prime such that B B is not divisible by p p. Set λ = max ⁡ { 0, m ′′ + n ′′ − ( p − 1) } \lambda=\max\{0,m^{\prime\prime}+n^{\prime\prime}-(p-1)\}, n ∗ = n ( mod t) n^{*}=n(\bmod{\,t}) and m ∗ = m ( mod t) m^{*}=m(\bmod{\,t}). Then

(82) |  | [m + n n] u ≡ ( m ′ + n ′ n ′) ​ ( m ′′ + n ′′ + λ ​ t, n ′′ + λ ​ t) − 1 ​ [m ∗ n ∗ + λ ​ τ] u ( mod p). {m+n\brack n}_{u}\equiv{m^{\prime}+n^{\prime}\choose n^{\prime}}{m^{\prime\prime}+n^{\prime\prime}+\lambda t,\choose n^{\prime\prime}+\lambda t}^{-1}{m^{*}\brack n^{*}+\lambda\tau}_{u}\pmod{p}. |  |

Thus, except when s = p − 1 s=p-1 and m ′′ + n ′′ ≥ p m^{\prime\prime}+n^{\prime\prime}\geq p, then

(83) |  | [m + n n] u ≡ ( m ′ + n ′ n ′) ​ ( m ′′ + n ′′ + λ ​ t, n ′′) − 1 ​ [m ∗ n ∗] u ( mod p). {m+n\brack n}_{u}\equiv{m^{\prime}+n^{\prime}\choose n^{\prime}}{m^{\prime\prime}+n^{\prime\prime}+\lambda t,\choose n^{\prime\prime}}^{-1}{m^{*}\brack n^{*}}_{u}\pmod{p}. |  |

Holte [61, Section 7] noticed that by means of a bit of translation, the congruence ( 82) may be transformed into the following result obtained in 1992 by D. Wells [137] (also see [138]): Let N = n + m N=n+m, and correspondingly, N 0 = N ( mod r) N_{0}=N(\bmod{\,r}), N ′ = ⌊ N / r ⌋ N^{\prime}=\lfloor N/r\rfloor, and N ′′ = N ′ ( mod s) N^{\prime\prime}=N^{\prime}(\bmod{\,s}). Let N ′ = ∑ j = 0 l N j ​ p j N^{\prime}=\sum_{j=0}^{l}N_{j}p^{j} and m ′ = ∑ j = 0 l m j ​ p j m^{\prime}=\sum_{j=0}^{l}m_{j}p^{j} be the p p -adic expansions of N ′ N^{\prime} and m ′ m^{\prime}. If p p is a prime such that B B is not divisible by p p, then under the same definitions of B B and t t as above, for N ′′ ≥ m ′′ N^{\prime\prime}\geq m^{\prime\prime},

(84) |  | [N m] u ≡ ( N ′′ m ′′) − 1 ​ ∏ j = 0 l ( N j m j) ​ [N ​ r + N 0 m ′′ ​ r + m 0] u ( mod p), {N\brack m}_{u}\equiv{N^{\prime\prime}\choose m^{\prime\prime}}^{-1}\prod_{j=0}^{l}{N_{j}\choose m_{j}}{Nr+N_{0}\brack m^{\prime\prime}r+m_{0}}_{u}\pmod{p}, |  |

and for N ′′ < m ′′ N^{\prime\prime}<m^{\prime\prime},

(85) |  | [N m] u ≡ { ( s + N ′′ m ′′) − 1 ​ ∏ j = 0 l ( N j m j) ​ [t + N ′′ ​ r + N 0 m ′′ ​ r + m 0] u ( mod p) i ​ f ​ s < p − 1 ( s m ′′) − 1 ​ ∏ j = 0 l ( N j m j) ​ [( N ′′ + 1) ​ t + N ′′ ​ r + N 0 m ′′ ​ r + m 0] u ( mod p) i ​ f ​ s = p − 1. {N\brack m}_{u}\equiv\left\{\begin{array}[]{ll}{s+N^{\prime\prime}\choose m^{\prime\prime}}^{-1}\prod_{j=0}^{l}{N_{j}\choose m_{j}}{t+N^{\prime\prime}r+N_{0}\brack m^{\prime\prime}r+m_{0}}_{u}\pmod{p}&if\,\,s<p-1\\ {s\choose m^{\prime\prime}}^{-1}\prod_{j=0}^{l}{N_{j}\choose m_{j}}{(N^{\prime\prime}+1)t+N^{\prime\prime}r+N_{0}\brack m^{\prime\prime}r+m_{0}}_{u}\pmod{p}&if\,\,s=p-1.\end{array}\right. |  |

Remark 29. In 2002 E.R. Tou [135, Theorem 4] generalized the congruence ( 82) modulo product of a finite number of distinct primes. □ \Box

### 5.2. Lucas type congruences for some classes of Lucas u u -nomial coefficients

In 2001 H. Hu and Z.-W. Sun [69, Theorem] proved the following result for the Lucas u u -nomial coefficients: Let u = ( u n) n ≥ 0 u=(u_{n})_{n\geq 0} be a Lucas sequence defined by ( 77). Suppose that gcd ⁡ ( A, B) = 1 \gcd(A,B)=1, and A ≠ ± 1 A\not=\pm 1 or B ≠ ± 1 B\not=\pm 1. Then u k ≠ 0 u_{k}\not=0 for every k ≥ 1 k\geq 1. Let q q be a positive integer, let m m and n n be nonnegative integers, and let R ⁡ ( q) = { 0, 1, …, q − 1 } R(q)=\{0,1,\ldots,q-1\}. If s, t ∈ R ⁡ ( q) s,t\in R(q) then

(86) |  | [m ​ q + s n ​ q + t] u ≡ ( m n) ​ [s t] u ​ u q + 1 ( n ​ q + t) ​ ( m − n) + n ⁡ ( s − t) ( mod w q), {mq+s\brack nq+t}_{u}\equiv{m\choose n}{s\brack t}_{u}u_{q+1}^{(nq+t)(m-n)+n(s-t)}\pmod{w_{q}}, |  |

where w q w_{q} is the largest divisor of u q u_{q} relatively prime to u 1, …, u q − 1 u_{1},\ldots,u_{q-1}. If q q or m ⁡ ( n + t) + n ⁡ ( s + 1) m(n+t)+n(s+1) is even, then

(87) |  | [m ​ q + s n ​ q + t] u ≡ ( m n) ​ [s t] u ​ ( − 1) ( m ​ t − n ​ s) ​ ( q − 1) ​ B q 2 ​ ( ( n ​ q + t) ​ ( m − n) + n ⁡ ( s − t)) ( mod w q). {mq+s\brack nq+t}_{u}\equiv{m\choose n}{s\brack t}_{u}(-1)^{(mt-ns)(q-1)}B^{\frac{q}{2}((nq+t)(m-n)+n(s-t))}\pmod{w_{q}}. |  |

Remark 30. ( [69, Remark 1]) When A = 2 A=2 and B = 1 B=1, we have u k = k u_{k}=k for each nonnegative integer k k, and if in addition we assume that q = p q=p is a prime, then w p = p w_{p}=p, and hence the congruence ( 86) becomes

 | ( m ​ p + s n ​ p + t) ≡ ( m n) ​ ( s t) ( mod p), {mp+s\choose np+t}\equiv{m\choose n}{s\choose t}\pmod{p}, |  |

which is in fact, Lucas’ theorem. □ \Box

In 2002 H. Hu [68, p. 291, Theorem] proved the following result: Let q q be a positive integer, and let m m and n n be even nonnegative integers with n ≤ m n\leq m. Let s s and t t be nonnegative integers such that t ≤ s < q t\leq s<q, and let v q ∗ v_{q}^{*} be the largest divisor of v q v_{q} relatively prime to v 0, …, v q − 1 v_{0},\ldots,v_{q-1}. Then

(88) |  | ( m / 2 n / 2) ​ [m ​ q + s n ​ q + t] u ≡ ( m n) ​ [s t] u ​ ( − B q) m − n 2 ​ ( n ​ q + t) + n 2 ​ ( s − t) ( mod v q ∗). {m/2\choose n/2}{mq+s\brack nq+t}_{u}\equiv{m\choose n}{s\brack t}_{u}(-B^{q})^{\frac{m-n}{2}(nq+t)+\frac{n}{2}(s-t)}\pmod{v_{q}^{*}}. |  |

Lucas type congruences modulo p 2 p^{2} and p 3 p^{3} ( p p is a prime > 3 >3) for Lucas u u -nomial coefficients and Fibonomial coefficients are established in [76], [77] and [120]. Namely, in 1993 W.A. Kimball and W.A. Webb [76] (also see [120, p. 1029]) proved the following two results: Let p p be an odd prime and let m m and n n be nonnegative integers. Suppose that τ \tau is the period of the Fibonacci sequence ( F n) n ≥ 0 (F_{n})_{n\geq 0} modulo p p, r r is the rank of apparition of p p ( ( that is, r r is the least index k k for which p p divides F k F_{k})), and t = τ / r t=\tau/r is an integer. In [134] it is shown that t ∈ { 1, 2, 4 } t\in\{1,2,4\}. The number ε \varepsilon is defined as follows: ε = 1 \varepsilon=1 if τ = r \tau=r; ε = − 1 \varepsilon=-1 if τ = 2 ​ r \tau=2r; and ε 2 ≡ − 1 ( mod p 2) \varepsilon^{2}\equiv-1(\bmod{\,p^{2}}) if τ = 4 ​ r \tau=4r; in this case p ≡ 1 ( mod 4) p\equiv 1(\bmod{\,4}). Then

(89) |  | [m ​ τ n ​ τ] ℱ ≡ ( m ​ t n ​ t) ( mod p 2) {m\tau\brack n\tau}_{\mathcal{F}}\equiv{mt\choose nt}\pmod{p^{2}} |  |

and

(90) |  | [m ​ r n ​ r] ℱ ≡ ε ( m − n) ​ n ​ r ​ [m n] ℱ ( mod p 2). {mr\brack nr}_{\mathcal{F}}\equiv\varepsilon^{(m-n)nr}{m\brack n}_{\mathcal{F}}\pmod{p^{2}}. |  |

In 1995 Kimball and Webb [77, Theorems 1 and 3] proved the following results: Let ( u n) n ≥ 0 (u_{n})_{n\geq 0} and ( v n) n ≥ 0 (v_{n})_{n\geq 0} be the sequences defined by ( 77) and ( 78), respectively, where A A and B B are nonzero integers such that gcd ⁡ ( A, B) = 1 \gcd(A,B)=1. Let p p be an odd prime, let τ \tau be the period of the sequence ( u n) n ≥ 0 (u_{n})_{n\geq 0} modulo p p, and let r r be the rank of apparition of p p. Then for all nonnegative integers m m and n n such that n ≤ m n\leq m there holds

(91) |  | [m ​ r n ​ r] u ≡ ( v r 2) ( m − n) ​ n ​ r ​ ( m n) ( mod p 2) {mr\brack nr}_{u}\equiv\left(\frac{v_{r}}{2}\right)^{(m-n)nr}{m\choose n}\pmod{p^{2}} |  |

and

(92) |  | [m ​ τ n ​ τ] u ≡ ( 1 + 1 2 ​ τ ​ ( m − n) ​ n ​ ( ( − B) τ − 1)) ​ ( m ​ t n ​ t) ( mod p 2). {m\tau\brack n\tau}_{u}\equiv\left(1+\frac{1}{2}\tau(m-n)n((-B)^{\tau}-1)\right){mt\choose nt}\pmod{p^{2}}. |  |

As a consequence of the congruence ( 91), it is proved in [77, Corollary 2] that

(93) |  | [m ​ τ n ​ τ] u ≡ ( 1 + τ ⁡ ( m − n) ​ n ​ ( ( v r 2) t − 1)) ​ ( m ​ t n ​ t) ( mod p 2). {m\tau\brack n\tau}_{u}\equiv\left(1+\tau(m-n)n\left(\left(\frac{v_{r}}{2}\right)^{t}-1\right)\right){mt\choose nt}\pmod{p^{2}}. |  |

Moreover, the congruence ( 92) immediately implies [77, Corollary 4] that if B = ± 1 B=\pm 1, then

(94) |  | [m ​ τ n ​ τ] u ≡ ( m ​ t n ​ t) ( mod p 2). {m\tau\brack n\tau}_{u}\equiv{mt\choose nt}\pmod{p^{2}}. |  |

Kimball and Webb [77, Theorem 5] also proved the following congruences for the Gaussian q q -nomial coefficients:

(95) |  | [m ​ r n ​ r] q ≡ ( q r + 1 2) ( m − n) ​ n ​ r ​ ( m n) ( mod p 2) ≡ ( 1 + 1 2 ​ r ​ ( m − n) ​ n ​ ( q r − 1)) ​ ( m n) ( mod p 2), \begin{split}{mr\brack nr}_{q}&\equiv\left(\frac{q^{r}+1}{2}\right)^{(m-n)nr}{m\choose n}\pmod{p^{2}}\\ &\equiv\left(1+\frac{1}{2}r(m-n)n(q^{r}-1)\right){m\choose n}\pmod{p^{2}},\end{split} |  |

where p p is a prime, q q is any p p -integral rational number such that q 2 − q q^{2}-q is not divisible by p p, and r r is the rank of apparition of p p.

In 1998 B. Wilson [140] proved the following result: Let p p be a prime such that p ≠ 2, 5 p\not=2,5, and let r r be the rank of apparition of p p with respect to the Fibonacci sequence ( F n) n ≥ 0 (F_{n})_{n\geq 0}. Then for any nonnegative integers m, n, s m,n,s and l l such that 0 ≤ s, l < r 0\leq s,l<r

(96) |  | [m ​ r n ​ r] ℱ ≡ [m n] ℱ ​ F r + 1 ( m − n) ​ n ​ r ( mod p) {mr\brack nr}_{\mathcal{F}}\equiv{m\brack n}_{\mathcal{F}}F_{r+1}^{(m-n)nr}\pmod{p} |  |

and

(97) |  | [m ​ r + s n ​ r + l] ℱ ≡ ( m n) ​ [s l] ℱ ​ F r + 1 ( n ​ r + l) ​ ( m − n) + n ⁡ ( s − l) ( mod p). {mr+s\brack nr+l}_{\mathcal{F}}\equiv{m\choose n}{s\brack l}_{\mathcal{F}}F_{r+1}^{(nr+l)(m-n)+n(s-l)}\pmod{p}. |  |

In 2007 L.-L. Shi [120] proved another congruence modulo p 2 p^{2} (where p > 3 p>3 is a prime) for the Lucas u u -nomial coefficients. Namely, in [120, Theorem 2] it is proved the following result: Let ( u n) n ≥ 0 (u_{n})_{n\geq 0} be the Lucas sequence defined by ( 77), where A A and B B are nonzero integers such that gcd ⁡ ( A, B) = 1 \gcd(A,B)=1, and A ≠ ± 1 A\not=\pm 1 or B ≠ 1 B\not=1. Let p > 3 p>3 be a prime not dividing B B. If r r is the rank of apparition of p p with respect to ( u n) n ≥ 0 (u_{n})_{n\geq 0}, then for any nonnegative integers m, n, s m,n,s and t t such that 0 ≤ s, l < r 0\leq s,l<r, we have

(98) |  | [m ​ r + s n ​ r + l] u ≡ { ( − 1) l − s − 1 ​ B − ( l − s 2) ​ u ( m − n) ​ r ​ u l − s − 1 × u r + 1 ( m − n) ​ ( l − 1) − n ⁡ ( l − s) ​ [m ​ r n ​ r] u ​ ( [l s] u) − 1 ( mod p 2) if s < l u r + 1 m ​ l + n ​ s − 2 ​ n ​ l ​ S m, s S n, l ​ S m − n, s − l ​ [m ​ r n ​ r] u ​ [s l] u ( mod p 2) if s ≥ l, {mr+s\brack nr+l}_{u}\equiv\left\{\begin{array}[]{ll}(-1)^{l-s-1}B^{-{l-s\choose 2}}u_{(m-n)r}u_{l-s}^{-1}&\\ \times u_{r+1}^{(m-n)(l-1)-n(l-s)}{mr\brack nr}_{u}\left({l\brack s}_{u}\right)^{-1}\pmod{p^{2}}&{\rm if}\quad s<l\\ u_{r+1}^{ml+ns-2nl}\frac{S_{m,s}}{S_{n,l}S_{m-n,s-l}}{mr\brack nr}_{u}{s\brack l}_{u}\pmod{p^{2}}&{\rm if}\quad s\geq l,\end{array}\right. |  |

where S k, i = 1 − ( k B u r) / u r + 1 ∑ j = 1 i ( u j − 1 / u j) S_{k,i}=1-(kBu_{r})/u_{r+1}\sum_{j=1}^{i}(u_{j-1}/u_{j}).

If Δ:= A 2 − 4 ​ B \Delta:=A^{2}-4B is not divisible by p p, then [m ​ r n ​ r] u {mr\brack nr}_{u} in ( 98) can be replaced by ( v r / 2) ( m − n) ​ n ​ r ​ ( m n) (v_{r}/2)^{(m-n)nr}{m\choose n}.

In 1995 Kimball and Webb [78, Theorem] and in 2007 L.-L. Shi [120] considered the generalized Lucas u u -nomial coefficients and the generalized Fibonomial coefficients defined as follows. If ( u n) n ≥ 0 (u_{n})_{n\geq 0} is the Lucas sequence defined by ( 77) such that A ≠ ± 1 A\not=\pm 1 or B ≠ 1 B\not=1, and let ( F n) n ≥ 0 (F_{n})_{n\geq 0} be the Fibonacci sequence. For any positive integer j j we set

 | [n] u j = ∏ k = 1 n u k ​ j and [n] ℱ j = ∏ k = 1 n F k ​ j, [n]_{u}^{j}=\prod_{k=1}^{n}u_{kj}\quad{\rm and}\quad[n]_{\mathcal{F}}^{j}=\prod_{k=1}^{n}F_{kj}, |  |

for n = 0, 1, 2, … n=0,1,2,\ldots, and regard an empty product as value 1.

Then for n, k = 0, 1, 2, … n,k=0,1,2,\ldots the generalized Lucas u u -nomial coefficient [n k] u j {n\brack k}_{u}^{j} and the generalized Fibonomial coefficient [n k] ℱ j {n\brack k}_{\mathcal{F}}^{j} are defined as follows:

 | [n k] u j = { [n] u j [k] u j ​ [n − k] u j if 0 ≤ k ≤ n 0 otherwise, {n\brack k}_{u}^{j}=\left\{\begin{array}[]{ll}\frac{[n]_{u}^{j}}{[k]_{u}^{j}[n-k]_{u}^{j}}&{\rm if}\quad 0\leq k\leq n\\ 0&{\rm otherwise},\end{array}\right. |  |

 | [n k] ℱ j = { [n] ℱ j [k] ℱ j ​ [n − k] u j if 0 ≤ k ≤ n 0 otherwise. {n\brack k}_{\mathcal{F}}^{j}=\left\{\begin{array}[]{ll}\frac{[n]_{\mathcal{F}}^{j}}{[k]_{\mathcal{F}}^{j}[n-k]_{u}^{j}}&{\rm if}\quad 0\leq k\leq n\\ 0&{\rm otherwise}.\end{array}\right. |  |

where ( u i ​ j / u j) i ≥ 0 (u_{ij}/u_{j})_{i\geq 0} is also a Lucas sequence.

In 1995 Kimball and Webb [78, Theorem] extended the congruence ( 90) by showing that if the rank r r of apparition of p p is p + 1 p+1 or p − 1 p-1, then for any prime p > 3 p>3 and any m ≥ n ≥ 0 m\geq n\geq 0,

(99) |  | [m ​ r n ​ r] ℱ ≡ ( ∓) ( m − n) ​ n ​ [m n] ℱ r ( mod p 3), r ​ e ​ s ​ p ​ e ​ c ​ t ​ i ​ v ​ e ​ l ​ y. {mr\brack nr}_{\mathcal{F}}\equiv(\mp)^{(m-n)n}{m\brack n}_{\mathcal{F}}^{r}\pmod{p^{3}},\quad respectively. |  |

In 2007 Shi [120] proved the congruence modulo p 3 p^{3} (where p > 3 p>3 is a prime) for the generalized Lucas u u -nomial coefficients. Namely, in [120, Theorem 1] it is proved the following result: Let A A and B B be nonzero integers such that gcd ⁡ ( A, B) = 1 \gcd(A,B)=1, and A ≠ ± 1 A\not=\pm 1 or B ≠ 1 B\not=1. Let p > 3 p>3 be a prime not dividing B B. If the rank r r of apparition of p p is p + 1 p+1 or p − 1 p-1 ( ( and hence r = p − ( A 2 − 4 ​ B p) r=p-\left(\frac{A^{2}-4B}{p}\right))), where ( ⋅ p) \left(\frac{\cdot}{p}\right) denotes the Legendre symobol, then for any nonnegative integers m m and n n we have

(100) |  | [m ​ r n ​ r] u ≡ ( − 1) ( m − n) ​ n ​ B ( m − n) ​ n ​ ( r 2) ​ [m n] u r ( mod p 3). {mr\brack nr}_{u}\equiv(-1)^{(m-n)n}B^{(m-n)n{r\choose 2}}{m\brack n}_{u}^{r}\pmod{p^{3}}. |  |

Remark 31. In the case A = − B = 1 A=-B=1 the congruence ( 100) yields the congruence ( 99) of Kimball and Webb [78]. □ \Box

In 1965 G. Olive [104] (also see [105, Lemma 2.1]) proved the following result: Suppose that d d is a positive integer and a, b, h, l a,b,h,l are integers such that 0 ≤ b, l ≤ d − 1 0\leq b,l\leq d-1. Then

(101) |  | [a ​ d + b h ​ d + l] q ≡ ( a h) ​ [b l] q ( mod Φ d ​ ( q)), {ad+b\brack hd+l}_{q}\equiv{a\choose h}{b\brack l}_{q}\pmod{\Phi_{d}(q)}, |  |

where Φ d ​ ( q) \Phi_{d}(q) is the d d th cyclotomic polynomial.

Remark 32. As noticed in [119, Chapter 5, p. 506], the congruence ( 101) perhaps was known to Gauss and it is rediscovered in 1982 by J. Désarménien [32] and V. Strehl [128] whose proof uses combinatorial arguments. □ \Box

Remark 33. Another different q q -analogue of the congruence ( 101) was established in 1967 by R.D. Fray [42]. □ \Box

Remark 34. Applying Lucas’ theorem, in 2006 S.-P. Eu, S.-C. Liu and Y.-N. Yeh [37] established the congruences of several combinatorial numbers, including Delannoy numbers and a class of Apéry-like numbers, the numbers of noncrossing connected graphs (Sloane’s sequence A007297), the numbers of total edges of all noncrossing connected graphs on n n vertices (Sloane’s sequence A045741), etc. □ \Box

## 6. Some applications of Lucas’ theorem

Even today, Lucas’ theorem is being studied widely, and has both extended and generalized, particularly in the area of divisibility of binomial coefficients. Numerous results on divisibility of binomial and multinomial coefficients by primes and prime powers and related historical notes are given in 1980 by D. Singmaster [122]. Furthermore, Lucas’ theorem has numerous applications in Number Theory, Combinatorics, Cryptography and Probability. We also point out that this theorem has become ubiquitous in the Theory of cellular automata.

### 6.1. Lucas’ theorem and the Pascal’s triangle

Let a k ​ ( n) a_{k}(n) be the number of integers 0 ≤ m ≤ n 0\leq m\leq n such that ( n m) ≢ 0 ( mod k) {n\choose m}\not\equiv 0(\bmod{\,k}), that is, a k ​ ( n) a_{k}(n) is the number of nonzero entries on row n n of Pascal’s triangle modulo k k. Let | n | w |n|_{w} be the number of occurrences of the word w w in n s n s − 1 ⋯ n 0 n_{s}n_{s-1}\cdots n_{0}, where n = ∑ i = 0 s n i ​ k i n=\sum_{i=0}^{s}n_{i}k^{i} is the base- k k representation of n n. In 1899 J.W.L. Glaisher [48, §14] initiated the study of counting entries on row n n of Pascal’s triangle modulo k k by using Lucas’ theorem to determine a 2 ​ ( n) = 2 | n | 1 a_{2}(n)=2^{|n|_{1}}. The proof is simple (cf. [114, p. 1]): In order that ( n m) {n\choose m} be odd, each term ( n i m i) {n_{i}\choose m_{i}} in the product must be 1, so if n i = 0 n_{i}=0 then m i = 0 m_{i}=0 and if n i = 1 n_{i}=1 then m i m_{i} can be either 0 or 1. It was the first result on a thorny path of solution of this difficult problem. However, this topic was forgotten for almost a half-century.

In 1947 N.J. Fine [39] generalized Glaisher’s result to an arbitrary prime. Fine’s result follows from Lucas’ theorem in the same way: Let p p be a prime, and let n n be a nonnegative integer. The number of nonzero entries on row n = ∑ i = 0 s n i ​ p i n=\sum_{i=0}^{s}n_{i}p^{i} of Pascal’s triangle modulo p p is ( ( cf. [114, p. 2]))

(102) |  | a p ​ ( n) = ∏ i = 0 s ( n i + 1). a_{p}(n)=\prod_{i=0}^{s}(n_{i}+1). |  |

Namely, the formula ( 102) immediately follows from the fact that by Lucas’ theorem, the binomial coefficient ( n m) {n\choose m} with m = ∑ i = 0 s m i ​ p i m=\sum_{i=0}^{s}m_{i}p^{i} is not divisible by a prime p p if and only if 0 ≤ m i ≤ n i 0\leq m_{i}\leq n_{i} for all i = 0, 1, …, s i=0,1,\ldots,s.

Remark. 35. If p = 2 p=2, then the formula ( 102) presents the number of odd entries on row n = ∑ i = 0 s n i ​ 2 i n=\sum_{i=0}^{s}n_{i}2^{i} of Pascal’s triangle. Notice that the parity of binomial coefficients has played an important role in a paper from 1984 of J.P. Jones and Y.V. Matijasevič [73] in connection with Hilbert’s tenth problem, Gödel’s undecidability proposition and computational complexity. They base their Lemma on the Lucas’ theorem given by the congruence ( 1) with p = 2 p=2 (cf. [74, Lemmas 3.9 and 3.10]). □ \Box

As noticed in [114], one may generalize Glaisher’s result in a different direction, namely to ask for the number a k, r a_{k,r} of integers 0 ≤ m ≤ n 0\leq m\leq n such that ( n m) ≡ r ( mod k) {n\choose m}\equiv r(\bmod{\,k}). In 2011 E. Rowland [114, Section 2, Theorem 1] generalized Fine’s result to prime powers, obtaining a formula for the sum a p α ​ ( n) = ∑ r = 1 p α − 1, r ( n) a_{p^{\alpha}}(n)=\sum_{r=1}^{p^{\alpha}-1,r}(n). Notice that in 1978 E. Hexel and H. Sachs [58, §5] determined a formula for a p, r i ​ ( n) a_{p,r^{i}}(n) in terms of ( p − 1) (p-1) th roots of unity, where r r is a primitive root modulo p p. For some related results see also [5], [28], [44], [51] and [114, Theorem 2]).

The previous considerations can be genearlized as follows. Let p p be a prime. For nonnegative integers n n and k k consider the set

 | A n, k ( p) = { j ∈ { 0, 1, …, n }: p k ∥ ( n j) }, A_{n,k}^{(p)}=\{j\in\{0,1,\ldots,n\}:p^{k}\|{n\choose j}\}, |  |

where p k | ( n j) p^{k}\|{n\choose j} denotes that p k | ( n j) p^{k}\mid{n\choose j} and ( n j) ≢ 0 ( mod p k + 1) {n\choose j}\not\equiv 0(\bmod{\,p^{k+1}}). In particular, A n, 0 ( p) A_{n,0}^{(p)} is a set of nonzero entries on row n n of Pascal’s triangle modulo k k. Therefore, under the previous notation, for a prime p p we have a p ​ ( n) = | A n, 0 ( p) | a_{p}(n)=|A_{n,0}^{(p)}| ( | S | |S| denotes the cardinality of a set S S), Notice that | A n, 0 ( p) | |A_{n,0}^{(p)}| can be evaluated by Fine’s formula ( 102). In 1967 L. Carlitz [23] solved a difficult problem for evaluation of | A n, 1 ( p) | |A_{n,1}^{(p)}|. In 1971 F.T. Howard [64], discovered the formula for | A n, k ( 2) | |A_{n,k}^{(2)}| for arbitrary k k. In 1973 F.T. Howard [65] found a solution for | A n, 2 ( p) | |A_{n,2}^{(p)}|.

Further related results are given in [52], and in 1997 by J.G. Huard, B.K. Spearman and K.S. Williams [70]. Let n n be a nonnegative integer. The n n th row of Pascal’s triangle consists of the following n + 1 n+1 binomial coefficients:

 | ( n 0), ( n 1), ( n 2), …, ( n n). {n\choose 0},{n\choose 1},{n\choose 2},\ldots,{n\choose n}. |  |

We denote by N n ​ ( t, m) N_{n}(t,m) the number of those binomial coefficients which are congruent to t t modulo m m, where t t and m ≥ 1 m\geq 1 are integers such that 0 ≤ t ≤ m − 1 0\leq t\leq m-1. Let p p be a prime, and let n n be a positive integer with the p p -adic expansion n = ∑ i = 0 k n i ​ p i n=\sum_{i=0}^{k}n_{i}p^{i}. We denote the number of r r ’s occuring among n 0, n 1, …, n k n_{0},n_{1},\ldots,n_{k} by l r l_{r} ( r = 0, 1, …, p − 1 r=0,1,\ldots,p-1). Set ω = e 2 ​ π ​ i / ( p − 1) \omega=e^{2\pi i/(p-1)} and let g g denote a primitive root modulo p p. Denote by ind g ​ t {\rm ind}_{g}t the index of the integer t ≢ 0 ( mod p) t\not\equiv 0(\bmod{\,p}) with respect to g g; that is, ind g ​ t {\rm ind}_{g}t is the unique integer j j such that t ≡ g j ( mod p) t\equiv g^{j}(\bmod{\,p}). In 1978 E. Hexel and H. Sachs [58, Theorem 3] have shown that for t = 1, 2, …, p − 1 t=1,2,\ldots,p-1,

(103) |  | N n ​ ( t, p) = 1 p − 1 ​ ∑ s = 0 p − 2 ω − s ​ ind g ​ t ​ ∏ r = 1 p − 1 B ​ ( r, s) l r, N_{n}(t,p)=\frac{1}{p-1}\sum_{s=0}^{p-2}\omega^{-s{\rm ind}_{g}t}\prod_{r=1}^{p-1}B(r,s)^{l_{r}}, |  |

where

 | B ⁡ ( r, s) = ∑ j = 0 r ω s ​ ind g ​ ( r j). B(r,s)=\sum_{j=0}^{r}\omega^{s{\rm ind}_{g}{r\choose j}}. |  |

By using the formula ( 103), in 1997 J.G. Huard, B.K. Spearman and K.S. Williams proved the analogous formula for N n ​ ( t ​ p, p 2) N_{n}(tp,p^{2}) with t = 1, 2, …, p − 1 t=1,2,\ldots,p-1 [70, Theorem 1.1]. They proved that for t = 1, 2, …, p − 1 t=1,2,\ldots,p-1,

(104) |  | N n ​ ( t ​ p, p 2) = 1 p − 1 ​ ∑ i = 0 p − 2 ∑ j = 1 p − 1 l i ​ j ​ ∑ s = 0 p − 2 ω − s ⁡ ( ind g ​ t + ind g ​ ( i + 1) − ind g ​ j) × B ⁡ ( p − 2 − i, − s) ​ B ​ ( j − 1, s) ​ ∏ r = 1 p − 1 B ​ ( r, s) l r − δ ⁡ ( r − i) − δ ⁡ ( r − j), \begin{split}N_{n}(tp,p^{2})=&\frac{1}{p-1}\sum_{i=0}^{p-2}\sum_{j=1}^{p-1}l_{ij}\sum_{s=0}^{p-2}\omega^{-s({\rm ind}_{g}t+{\rm ind}_{g}(i+1)-{\rm ind}_{g}j)}\\ \times&B(p-2-i,-s)B(j-1,s)\prod_{r=1}^{p-1}B(r,s)^{l_{r}-\delta(r-i)-\delta(r-j)},\end{split} |  |

where

 | δ ⁡ ( x) = { 1 i ​ f ​ x = 0 0 i ​ f ​ x ≠ 0, \delta(x)=\left\{\begin{array}[]{ll}1&if\,\,x=0\\ 0&if\,\,x\not=0,\end{array}\right. |  |

and l i ​ j l_{ij} denotes the number of occurences of the pair i ​ j ij in the string n 0 ​ n 1 ​ … ​ n k n_{0}n_{1}\ldots n_{k}.

Let p p be a prime, and let k k be a positive integer. Let A ⁡ ( k, p) A(k,p) be the matrix with entries ( i j) p:= ( i j) ( mod p) {i\choose j}_{p}:={i\choose j}(\bmod{\,p}), 0 ≤ i < p k 0\leq i<p^{k}, 0 ≤ j < p k 0\leq j<p^{k} (actually, ( i j) p {i\choose j}_{p} is the remainder of the division of ( i j) {i\choose j} by p p). By using the Lucas property of the matrix A ⁡ ( k, p) A(k,p) given by ( 54), in 1994 M. Razpet [111, p. 378] proved that the number of all zero entries of the matrix A ⁡ ( k, p) A(k,p) is equal to p 2 ​ n − ( p + 1 2) k p^{2n}-{p+1\choose 2}^{k}, and hence, the number of all nonzero entries of the matrix A ⁡ ( k, p) A(k,p) is equal to ( p + 1 2) k {p+1\choose 2}^{k}.

Let p p be a prime, and let n n be a positive integer. For an integer r r such that 0 ≤ r ≤ p − 1 0\leq r\leq p-1, let b r ​ ( n) b_{r}(n) be the number of binomial coefficients ( i j) {i\choose j} with 0 ≤ j ≤ i < n 0\leq j\leq i<n such that ( i j) ≡ r ( mod p) {i\choose j}\equiv r(\bmod{\,p}). In 1957 J.B. Roberts [113] established systems of simultaneous linear difference equations with constant coefficients whose solutions would yield the quantities b r ​ ( n) b_{r}(n) explicitly. Namely, if 0 ≤ c ≤ p − 1 0\leq c\leq p-1, 1 ≤ t ≤ p k 1\leq t\leq p^{k}, k > 0 k>0, and if q ¯ \bar{q} is the reciprocal of q ∈ { 1, 3, …, p − 1 } q\in\{1,3,\ldots,p-1\} modulo p p ( ( i.e., q ​ q ¯ ≡ 1 ( mod p) q\bar{q}\equiv 1(\bmod{\,p}))), then by [113, Theorem 1],

(105) |  | b r ​ ( c ​ p k + t) = b r ​ ( c ​ p k) + ∑ q = 1 p − 1 ( b r ​ q ¯ ​ ( c + 1) − b r ​ q ¯ ​ ( c)) ​ b q ​ ( t). b_{r}(cp^{k}+t)=b_{r}(cp^{k})+\sum_{q=1}^{p-1}(b_{r\bar{q}}(c+1)-b_{r\bar{q}}(c))b_{q}(t). |  |

Furthermore, if b ⁡ ( n) = ∑ r = 1 p − 1 b r ​ ( n) b(n)=\sum_{r=1}^{p-1}b_{r}(n) and n = ∑ i = 0 k n i ​ p i n=\sum_{i=0}^{k}n_{i}p^{i} with 0 ≤ n i ≤ p − 1 0\leq n_{i}\leq p-1 for all i = 0, 1, …, k i=0,1,\ldots,k, then by [113, Corollary 4],

(106) |  | b ( n) = 1 2 ∑ i = 0 k n i ( ( n i + 1) ⋯ ( n k + 1)) ( 1 2 p ( p + 1)) i. b(n)=\frac{1}{2}\sum_{i=0}^{k}n_{i}((n_{i}+1)\cdots(n_{k}+1))\left(\frac{1}{2}p(p+1)\right)^{i}. |  |

By using Lucas’ theorem, in 1992 R. Garfield and H.S. Wilf [44, Theorem] proved the following result: Let p p be a prime, let a a be a primitive root modulo p p, and let n n be a nonnegative integer with the p p -adic expansion n = ∑ i = 0 s n i ​ p i n=\sum_{i=0}^{s}n_{i}p^{i}. Denote by l j ​ ( n) l_{j}(n) the number of j j ’s occuring among n 0, n 1, …, n s n_{0},n_{1},\ldots,n_{s} ( ( j = 0, 1, …, p − 1 j=0,1,\ldots,p-1)). Further, for each i ∈ { 0, 1, …, p − 2 } i\in\{0,1,\ldots,p-2\} let r i ​ ( n) r_{i}(n) be the number of integers k k with 0 ≤ k ≤ n 0\leq k\leq n, for which ( n k) ≡ a i ( mod p) {n\choose k}\equiv a^{i}(\bmod\,p), and let R n ​ ( X) = ∑ i = 0 p − 2 r i ​ ( n) ​ X i R_{n}(X)=\sum_{i=0}^{p-2}r_{i}(n)X^{i} be their generating function. Then

(107) |  | R n ​ ( X) ≡ ∏ j = 1 p − 1 R j ​ ( X) l j ​ ( n) ( mod X p − 1 − 1). R_{n}(X)\equiv\prod_{j=1}^{p-1}R_{j}(X)^{l_{j}(n)}\pmod{X^{p-1}-1}. |  |

In 1990 R. Bollinger and C. Burchard [17] considered the extended pascal’s triangles which arise, by analogy with the ordinary Pascal’s triangle as the (left-justified) arrays of the coefficients in the expansion ( 1 + x + x 2 + ⋯ + x k − 1) n (1+x+x^{2}+\cdots+x^{k-1})^{n}. That is, the array T k T_{k} has in row n n, column m m, the number C k ​ ( n, m) C_{k}(n,m) defined for k, n, m ≥ 0 k,n,m\geq 0 by the expansion

 | ( 1 + x + x 2 + ⋯ + x k − 1) n = ∑ m = 0 ( k − 1) ​ n C k ​ ( n, m) ​ x m, (1+x+x^{2}+\cdots+x^{k-1})^{n}=\sum_{m=0}^{(k-1)n}C_{k}(n,m)x^{m}, |  |

It is nociced in [17, the property d) on page 199] that

 | C k ​ ( n, m) = ∑ j ( − 1) j ​ ( n j) ​ ( n − 1 + m − k ​ j n − 1), C_{k}(n,m)=\sum_{j}(-1)^{j}{n\choose j}{n-1+m-kj\choose n-1}, |  |

and hence, C 2 ​ ( n, m) = ( n m) C_{2}(n,m)={n\choose m}. Accordingly, T 2 T_{2} is the Pascal’s triangle.

R. Bollinger and C. Burchard [17, Theorem 1] applied Lucas’ theorem to the Pascal’s triangle, proving that if p p is a prime, and if n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} and m = m 0 + m 1 ​ p + ⋯ + m s ​ p l m=m_{0}+m_{1}p+\cdots+m_{s}p^{l} are the p p -adic expansions of n n and m m, then

(108) |  | C k ​ ( n, m) ≡ ∑ r 0, …, r s ∏ i = 0 s C k ​ ( n i, r i) ( mod p), C_{k}(n,m)\equiv\sum_{r_{0},\ldots,r_{s}}\prod_{i=0}^{s}C_{k}(n_{i},r_{i})\pmod{p}, |  |

where the sum is taken over all ( s + 1) (s+1) -tuples ( r 0, r 1, …, r s) (r_{0},r_{1},\ldots,r_{s}) such that 𝑂𝑃𝐸𝑁 i) i) m = r 0 + r 1 ​ p + ⋯ + r s ​ p s m=r_{0}+r_{1}p+\cdots+r_{s}p^{s} and 𝑂𝑃𝐸𝑁 i ​ i) ii) 0 ≤ r i ≤ ( k − 1) ​ n i 0\leq r_{i}\leq(k-1)n_{i} for each i = 0, 1, …, s i=0,1,\ldots,s; if m m is not representable in this form, then certainly C k ​ ( n, m) ≡ 0 ( mod p) C_{k}(n,m)\equiv 0\,(\bmod{\,p}).

### 6.2. Another applications of Lucas’s theorem

By using Kummer’s theorem and Lucas’ theorem, in 2007 K. Dilcher [34, Theorem 2] derived an alternating sum analog to a special case to an 1876 congruence of Hermite [57] (also see [36, Chapter IX, p. 271]) as follows. Let p p be an odd prime and let q q be a positive integer. Then

(109) |  | ∑ j = 0 ⌊ q / 2 ⌋ ( q ⁡ ( p − 1) 2 ​ j ​ ( p − 1)) ≡ { 1 ( mod p) i ​ f ​ q ​ i ​ s ​ o ​ d ​ d; 2 ( mod p) i ​ f ​ q ​ i ​ s ​ e ​ v ​ e ​ n ​ a ​ n ​ d ​ q ≢ 0 ( mod p + 1); 3 2 ( mod p) i ​ f ​ p + 1 | q. \sum_{j=0}^{\lfloor q/2\rfloor}{q(p-1)\choose 2j(p-1)}\equiv\left\{\begin{array}[]{ll}1\pmod{p}&if\,\,q\,\,is\,\,odd;\\ 2\pmod{p}&if\,\,q\,\,is\,\,even\,\,and\,\,q\not\equiv 0(\bmod\,p+1);\\ \frac{3}{2}\pmod{p}&if\,\,p+1\mid q.\end{array}\right. |  |

By using Lucas’ theorem, in 2009 the author of this article proved the following result [92, Theorem]. If d, q > 1 d,q>1 are integers such that

(110) |  | ( n ​ d m ​ d) ≡ ( n m) ( mod q) {nd\choose md}\equiv{n\choose m}\pmod{q} |  |

for every pair of integers n ≥ m ≥ 0 n\geq m\geq 0, then d d and q q are powers of the same prime p p.

Remark 36. Observe that the above result may be considered as a partial converse theorem of the congruence ( 5) of Subsection 2.1. □ \Box

In 2010 M.P. Saikia and J. Vogrinc [116, Theorem 2.1] (see also [81, Theorem 1.2 and its proof]) proved that a positive integer p > 1 p>1 is a prime if and only if

(111) |  | ( n p) ≡ ⌊ n p ⌋ ( mod p) {n\choose p}\equiv\left\lfloor\frac{n}{p}\right\rfloor\pmod{p} |  |

for every nonnegative integer n n.

By using Lucas’ theorem, in 2013 the author of this article [99, Theorem 1.1] generalized Babbage’s criterion for primality given in 1819 by Babbage [9] (also see [52, Section 4]). Lucas’ theorem is also applied in a recent author’s note [101, Theorem 1] in order to prove the following result: If n > 1 n>1 and q > 1 q>1 are integers such that

 | ( n − 1 k) ≡ ( − 1) k ( mod q) {n-1\choose k}\equiv(-1)^{k}\pmod{q} |  |

for every integer k ∈ { 0, 1, …, n − 1 } k\in\{0,1,\ldots,n-1\}, then q q is a prime and n n is a power of q q.

Definition (see, e.g., [2]). Let p p be a prime. We say that the sequence of rational numbers ( a n) n ≥ 0 (a_{n})_{n\geq 0} ( a n) n ≥ 0 (a_{n})_{n\geq 0} has the p p - Lucas property (or that the sequence ( a n) n ≥ 0 (a_{n})_{n\geq 0} is p p - Lucas) if the denominators of all the a n a_{n} ’s are not divisible by p p, and if for all n ≥ 0 n\geq 0 and for all j ∈ { 0, 1, …, p − 1 } j\in\{0,1,\ldots,p-1\} it holds

(112) |  | a p ​ n + j ≡ a n ​ a j ( mod p). □ \qquad\qquad\qquad a_{pn+j}\equiv a_{n}a_{j}\pmod{p}.\qquad\qquad\qquad\qquad\hfill\Box |  |

Clearly, the sequence of rational numbers ( a n) n ≥ 0 (a_{n})_{n\geq 0} has the p p -Lucas property if and only if

(113) |  | a n ≡ ∏ i = 0 s a n i ( mod p), a_{n}\equiv\prod_{i=0}^{s}a_{n_{i}}\pmod{p}, |  |

for every positive integer n n with the p p -adic expansion n = n 0 + n 1 ​ p + ⋯ + n s ​ p s n=n_{0}+n_{1}p+\cdots+n_{s}p^{s} such that 0 ≤ n i ≤ p − 1 0\leq n_{i}\leq p-1 for all i = 0, 1, …, s i=0,1,\ldots,s. Furthermore, the integer sequence ( a n) n ≥ 0 (a_{n})_{n\geq 0} has the Lucas property if and only if ( a n) n ≥ 0 (a_{n})_{n\geq 0} has the p p -Lucas property for every prime p p.

In what follows, we will consider sequences ( a n) n ≥ 0 (a_{n})_{n\geq 0} having the p p -Lucas property for infinitely many primes p p. As noticed in [2, Remarks 1], such a sequence is either 0 or it satisfies a 0 = 1 a_{0}=1. □ \Box

For a positive integer t t consider the formal power series

 | ∑ n = 0 ∞ ( 2 ​ n n) t ​ X n. \sum_{n=0}^{\infty}{2n\choose n}^{t}X^{n}. |  |

It is known that the above formal power series is transendental over ℚ ⁡ ( X) \mathbb{Q}(X) when t ≥ 2 t\geq 2. This is due in 1980 to Stanley [125], and independently in 1987 to Flajolet [40] and in 1989 to C.F. Woodcock and H. Sharif [143]. While Stanley and Flajolet used analytic methods and studied the asymptotics of the coefficients of this series, Woodcock and Sharif gave a purely algebraic proof. Their basic idea is to reduce this series modulo a prime p p, and to use the p p -Lucas property for central binomial coefficients: if n = ∑ i = 0 s n i n=\sum_{i=0}^{s}n_{i} is the base p p expansion of a positive integer n n, then ( [89]; cf. ( 58) of Subsection 4.1)

(114) |  | ( 2 ​ n n) ≡ ∏ i = 0 s ( 2 ​ n i n i) ( mod p). {2n\choose n}\equiv\prod_{i=0}^{s}{2n_{i}\choose n_{i}}\pmod{p}. |  |

Namely, a proof of Woodcock and Sharif [143] is based on the following congruence which follows from Lucas’ theorem:

 | F t p − 1 ​ ( X) ≡ ( ∑ i = 0 ( p − 1) / 2 ( 2 ​ i i) ​ X i) − 1 ( mod p). F_{t}^{p-1}(X)\equiv\left(\sum_{i=0}^{(p-1)/2}{2i\choose i}X^{i}\right)^{-1}\pmod{p}. |  |

In 1998 J.-P. Allouche, D. Gouyou-Beauchamps and G. Skordev [2] generalized the method of Woodcock and Sharif to characterize all formal power series that have the p p -Lucas property for “many” primes p p, and that are furthermore algebraic over ℚ ⁡ ( X) \mathbb{Q}(X). Namely, they proved the following result [2, Theorem 1]: Let s s be an integer ≥ 2 \geq 2. Define s ′ = s s^{\prime}=s if s s is even, and s ′ = 2 ​ s s^{\prime}=2s if s s is odd. Let F ⁡ ( X) = ∑ n = 0 ∞ a n ​ X n F(X)=\sum_{n=0}^{\infty}a_{n}X^{n} be a nonzero formal power series with coefficients in ℚ \mathbb{Q}. Then the following conditions are equivalent:

- (i)

The sequence ( a n) n ≥ 0 (a_{n})_{n\geq 0} has the p p -Lucas property for all large primes p p such that p ≡ 1 ( mod s) p\equiv 1(\bmod{\,s}), and the formal power series F ⁡ ( X) F(X) is algebraic over ℚ ⁡ ( X) \mathbb{Q}(X).

- (ii)

There exists a polynomial P ⁡ ( X) P(X) in ℚ ⁡ [X] \mathbb{Q}[X] of degree at most s ′ s^{\prime}, with P ⁡ ( 0) = 1 P(0)=1, such that F ( X) = ( P ( X)) − 1 / s ′ F(X)=(P(X))^{-1/s^{\prime}}.

If s s is odd, and if the number s ′ s^{\prime} is replaced by s s in the statement ( i ​ i) (ii), we still have ( i ​ i) (ii) implies ( i) (i), but the converse is not necessarily true.

Furthermore, when the number s s is equal to 2, in 1999 Allouche [1, Theorem 6.4] proved the following result (cf. [2, Theorem 2]): Let ( a n) n ≥ 0 (a_{n})_{n\geq 0} be a nonzero sequence of rational numbers. Then the following assertions are equivalent.

- (i)

The sequence ( a n) n ≥ 0 (a_{n})_{n\geq 0} has the p p -Lucas property for all large primes p p, and the series F ⁡ ( X) = ∑ n = 0 ∞ a n ​ X n F(X)=\sum_{n=0}^{\infty}a_{n}X^{n} is algebraic over ℚ ⁡ ( X) \mathbb{Q}(X).

- (ii)

For all large primes p p the sequence ( a n) n ≥ 0 (a_{n})_{n\geq 0} has the p p -Lucas property, and the degree d p d_{p} of the series ∑ n = 0 ∞ ( a n ( mod p)) ​ X n \sum_{n=0}^{\infty}(a_{n}(\bmod{\,p}))X^{n} ( ( that is necessarily algebraic over 𝔽 p ​ ( X) \mathbb{F}_{p}(X) from the p p -Lucas property)) is bounded independently of p p.

- (iii)

There exists a polynomial P ⁡ ( X) P(X) in ℚ ⁡ [X] \mathbb{Q}[X] of degree at most 2 2, with P ⁡ ( 0) = 1 P(0)=1, such that F ( X) = ∑ n = 0 ∞ a n X n = ( P ( X)) − 1 / 2 F(X)=\sum_{n=0}^{\infty}a_{n}X^{n}=(P(X))^{-1/2}.

Remark 37. In 2013 É. Delaygue [31, Subsection 1.2] considered the notion of p p -Lucas property to a ℤ p \mathbb{Z}_{p} - valued family A = ( A ⁡ ( 𝐧)) 𝐧 ∈ ℕ d A=\left(A(\mathbf{n})\right)_{\mathbf{n}\in\mathbb{N}^{d}}, where p p is a prime, ℤ p \mathbb{Z}_{p} is the ring of p p -adic integers and d d is a positive integer. We say that A A satisfies the p p -Lucas property if and only if, for all v ∈ { 0, 1, …, p − 1 } d \mathrm{v}\in\{0,1,\ldots,p-1\}^{d} and all n ∈ ℕ d \mathrm{n}\in\mathbb{N}^{d}, we have

 | A ⁡ ( v + n ​ p) ≡ A ⁡ ( v) ​ A ​ ( n) ( mod p ​ ℤ p). A(\mathrm{v}+\mathrm{n}p)\equiv A(\mathrm{v})A(\mathrm{n})\pmod{p\mathbb{Z}_{p}}. |  |

Delaygue [31, Theorem 3] established an effective criterion for a sequence of factorial ratios to satisfy the p p -Lucas property for almost all primes p p. □ \Box

## References

- [1] J.-P. Allouche, Transcendence of formal power series with rational coefficients, Theoret. Comput. Sci. 218 (1999), 143–160.
- [2] J.-P. Allouche, D. Gouyou-Beauchamps and G. Skordev, Transcendence of binomial and Lucas’ formal power power series, J. Algebra 210 (1998), 577–592.
- [3] J.-P. Allouche, F. von Haeseler, H.-O. Peitgen and G. Skordev, Discrete Appl. Math. 66 (1996), 1–22.
- [4] J.-P. Allouche and J. Shallit, Automatic Sequences: Theory, Applications, Generalizations, Cambridge University Press, New York/Cambridge, 2003.
- [5] T. Amdeberhan and R. Stanley, Polynomial coefficient enumeration, http://arXiv.org/abs/0811.3652v1, 2008.
- [6] P.G. Anderson, A.T. Benjamin and J A. Rouse, Combinatorial proofs of Fermat’s, Lucas’s, and Wilson’s theorems, Amer. Math. Monthly 112 (2005), 266–268.
- [7] H. Anton, Die Elferprobe und die Proben für die Modul Neun, 9, 13 and 101, Dreizehn und Hunderteins. Für Volksund Mittelschulen, Archiv Math. Physik 49 (1869), 241–308.
- [8] R. Apéry, Irrationalité de ζ ⁡ ( 2) \zeta(2) and ζ ⁡ ( 3) \zeta(3), Astérisque 61 (1979), 11–13.
- [9] C. Babbage, Demonstration of a theorem relating to prime numbers, Edinburgh Philosophical J. 1 (1819), 46–49.
- [10] D.F. Bailey, Two p 3 p^{3} variations of Lucas’ theorem, J. Number Theory 35 (1990), 208–215.
- [11] D.F. Bailey, Some binomial coefficient congruences, Appl. Math. Letters 4, No. 4 (1991), 1–5.
- [12] D.F. Bailey, More binomial coefficent congruences, Fibonacci Quart. 30, No. 2 (1992), 121–125.
- [13] A.T. Benjamin and J.J. Quinn, Proofs That Really Coubt, The Art of Combinatorial proofs, Mathematical Association of America, Providence, 2003.
- [14] D. Berend and N. Kriger, On some questions of Razpet regarding binomial coefficients, Discrete Math. 260 (2003), 177–182.
- [15] D. Berend and J.E. Harmse, On some arithmetical properties of middle binomial coefficients, Acta Arith. 84 (1998), 31–41.
- [16] A. Bès, On Pascal triangles modulo a prime power, Ann. Pure Appl. Logic 89 (1997), 17–35.
- [17] R.C. Bollinger and C.L. Burchard, Lucas’ theorem and some related results for extended Pascal triangles, Amer. Math. Monthly 97 (1990), 198–204.
- [18] J. Boulanger and J.-L. Chabert, An extension of the Lucas theorem, Acta Arith. 96 (2001), 303–312.
- [19] V. Brun, J.O. Stubban, J.E. Fjeldstad, R. Tambs Lyche, K.E. Aubert, W. Ljunggren and E. Jacobsthal, On the divisibility of the difference between two binomial coefficients. Den 11te Skandinaviske Matematikerkongress, Trondheim, 1949, 42–54. Johan Grundt Tanums Forlag, Oslo, 1952.
- [20] P.-J. Cahen and J.-L. Chabert, Integer-Valued Polynomials, Amer. Math. Soc. Surveys Monogr. 48, Providence, 1997.
- [21] N.J. Calkin, Factors sums of powers of binomial coefficients, Acta Arithmetica 86 (1998), 17–26.
- [22] L. Carlitz, The coefficients of the reciprocal of J 0 ​ ( x) J_{0}(x), Arch. Math. 6 (1955), 121–127.
- [23] L. Carlitz, The number of binomial coefficients divisible by a fixed power of a prime, Rend. Circ. Mat. Palermo 16, no. 2 (1967), 299–320.
- [24] R.D. Carmichael, On the numerical factors of the arithmetic forms α n ± β n \alpha^{n}\pm\beta^{n}, Ann. of Math. 15 (1913–1914), 30–70.
- [25] M. Chamberland and K. Dilcher, A binomial sum related to Wolstenholme’s theorem, J. Number Theory 129 (2009), 2659–2672.
- [26] L.E. Clarke, Problem 4704, Amer. Math. Monthly 63 (1956), p. 584; Solution, ibid 64 (1957), 597–598.
- [27] H. Cohen, Number Theory. Volume II: Analytic and Modern Tools, Springer, 2007.
- [28] K.S. Davis and W.A. Webb, Pascal’s triangle modulo 4, Fibonacci Quart. 29, no. 1 (1991), 79–83.
- [29] K.S. Davis and W.A. Webb, Lucas’ theorem for prime powers, European J. Combin. 11 (1990), 229–233.
- [30] K.S. Davis and W.A. Webb, A binomial coefficient congruence modulo prime powers, J. Number Theory 43 (1993), 20–23.
- [31] É. Delaygue, Arithmetic properties of Apéry-like numbers, arXiv:1310.4131v1 [math.NT], 2013.
- [32] J. Désarménien, Un analogue des congruences de Kummer pour les q q -nombres d’Euler, European J. Combin. 3 (1982), 19–28.
- [33] E. Deutsch and B.E. Sagan, Congruences for Catalan and Motzkin numbers and related sequences, J. Number Theory 117 (2006), 191–215.
- [34] K. Dilcher, Congruences for a class of alternating lacunary sums of binomial coefficients, J. Integer Sequences 10 (2007), Article 07.10.1.
- [35] D. Djukić, V. Janković, I. Matić and N. Petrović, The IMO compendium: A Collection of Problems Suggested for the International Mathemacical Olympiads: 1959–2009, Second edition, Springer-Verlag, New York, 2009.
- [36] L.E. Dickson, The History of the Theory of Numbers, Vol. I, Chelsea, New York, 1966.
- [37] S.-P. Eu, S.-C. Liu and Y.-N. Yeh, On the congruences of some combinatorial numbers, Stud. Appl. Math. 116 (2006), 135–144.
- [38] T.J. Evans, On some generalizations of Fermat’s, Lucas’s and Wilson’s theorem, Ars Combinatoria 79 (2005), 189–194.
- [39] N.J. Fine, Binomial coefficients modulo a prime, Amer. Math. Monthly 54 (1947), 589–592.
- [40] P. Flajolet, Analytic models and ambiguity of context-free languages, Theoret. Comput. Sci. 49 (1987), 283–309.
- [41] G. Fontené, Généralisation d’une formule connue, Nouvelles Annales de Mathématiques 15, no. 4 (1915), p. 112.
- [42] R.D. Fray, Congruence properties of ordinary and q q -binomial coefficients, Duke Math. J. 34 (1967), 467–480.
- [43] R.D. Fray, D.P. Roselle, Weighted lattice paths, Pacific J. Math. 37, no. 1 (1971), 85–96.
- [44] R. Garfield and H. Wilf, The distribution of the binomial coefficients modulo p p, J. Number Theory 41 (1992), 1–5.
- [45] C.F. Gauss, Disquisitiones Arithmeticae, Fleischer, Leipzig, 1801.
- [46] C.F. Gauss, Summatio quarumdam serierum singularium, Commentationes societatis regiae scientiarum Gottingensis recentiores 1 (1808), 147–186. Reprinted in Gauss’s Werke 2 (1863), 9–45.
- [47] I. Gessel, Some congruences for Apéry numbers, J. Number Theory 14 (1982), 362–368.
- [48] J.W.L. Glaisher, On the residues of a binomial-theorem coefficients, Q. J. Pure Appl. Math. 30 (1899), 150–156.
- [49] J.W.L. Glaisher, On the residues of the sums of products of the first p − 1 p-1 numbers, and their powers, to modulus p 2 p^{2} or p 3 p^{3}, Q. J. Math. 31 (1900), 321–353.
- [50] H.W. Gould, The Bracket function and Fonténe-Ward generalized binomial coefficients with applications to Fibonomial coefficients, Fibonacci Quart. 7, no. 1 (1969), 23–40.
- [51] A. Granville, Zaphod Beeblebrox’s brain and the fifty-ninth row of Pascal’s triangle, Amer. Math. Monthly 99 (1992), 318–331.
- [52] A. Granville, Arithmetic properties of binomial coefficients. I I. Binomial coefficients modulo prime powers, in Organic Mathematics (Burnaby, BC, 1995), CMS Conf. Proc., vol. 20, American Mathematical Society, Providence, RI, 1997, 253–275.
- [53] R.K. Guy, Unsolved problems in Number Theory, Third edition, Springer-Verlag, New York, 2004.
- [54] P.W. Haggard and J.O. Kiltinen, Binomial expansions modulo prime powers, Internat. J. Math. & Math. Sci. 3, No. 2 (1980), 397–400.
- [55] M. Hausner, Applications of a simple of counting technique, Amer. Math. Monthly 90 (1983), 127–129.
- [56] C. Helou and G. Terjanian, On Wolstenholme’s theorem and its converse, J. Number Theory 128 (2008), 475–499.
- [57] Ch. Hermite, Extrait d’une lettre à M. Borchardt, J. Reine Angew. Math. 81 (1876), 93–95.
- [58] E. Hexel and H. Sachs, Counting residues modulo a prime in Pascal’s triangle, Indian J. Math. 20 (1978), 91–105.
- [59] V.E. Hoggatt, Fibonacci numbers and generalized binomial coefficients, Fibonacci Quart. 5, no. 4 (1967), 383–400.
- [60] J.M. Holte, A Lucas-type theorem for Fibonomial-coefficient residues, Fibonacci Quart. 32, no. 1 (1994), 60–68.
- [61] J.M. Holte, Residues of generalized binomial coefficients modulo a prime, Fibonacci Quart. 38, no. 3 (2000), 227–238.
- [62] J.M. Holte, Fractal dimension of arithmetical structures of generalized binomial coefficients modulo a prime, Fibonacci Quart. 44, no. 1 (2006), 46–58.
- [63] P. Horak and L. Skula, A characterization of the second-order strong divisibility sequences, Fibonacci Quart. 23, no. 2 (1985), 126–132.
- [64] F.T. Howard, The number of binomial coefficients divisible by a fixed power of 2, Proc. Amer. Math. Soc. 29 (1971), 236–242.
- [65] F.T. Howard, The number of binomial coefficients divisible by a fixed power of a prime, Proc. Amer. Math. Soc. 37 (1973), 358–362.
- [66] F.T. Howard, The reciprocal of the Bessel function J k ​ ( z) J_{k}(z), Fibonacci Quart. 25, no. 4 (1987), 304–311.
- [67] F.T. Howard, Congruences for the Stirling numbers and associated Stirling numbers, Acta Arith. 55 (1990), 29–41.
- [68] H. Hu, On Lucas v v -triangles, Fibonacci Quart. 40, no. 4 (2002), 290–294.
- [69] H. Hu and Z.-W. Sun, An extension of Lucas’ theorem Proc. Amer. Math. Soc. 129 (2001), 3471–3478.
- [70] J.G. Huard, B.K. Spearman and K.S. Williams, On Pascal’s triangle modulo p 2 p^{2}, Colloq. Mathem. 74, no. 1 (1997), 157–165.
- [71] K. Ireland and M. Rosen, A Classical Introduction to Modern Number Theory, Springer-Verlag, New York, 1982.
- [72] Y. Jin, Z-J. Lu and A.L. Schmidt, On recurrences for sums of powers of binomial coefficients, J. Number Theory 128 (2008), 2784–2794.
- [73] J.P. Jones and Y.V. Matijasevič, Register machine proof of the theorem on exponential diophantine representation of enumerable sets, J. Symbolic Logic 49 (1984), 818–829.
- [74] J.P. Jones and Y.V. Matijasevič, Proof of recursive unsolvability of Hilbert’s tenth problem, Amer. Math. Monthly 98, no. 8 (1991), 689–709.
- [75] G.S. Kazandzidis, Congruences on the binomial coefficients, Bull. Soc. Math. Grèce ( ( N.S.)) 9 (fasc. 1) (1968), 1–12.
- [76] W.A. Kimball and W.A. Webb, Congruence properties of Fibonacci numbers and Fibonacci coefficients, in Applications of Fibonacci numbers, vol. 5, Kluwer, Dordrecht, 1993.
- [77] W.A. Kimball and W.A. Webb, Some congruences for generalized binomial coefficients, Rocky Mountain J. Math. 25 (1995), 1079–1085.
- [78] W.A. Kimball and W.A. Webb, A congruence for Fibonacci coefficients modulo p 3 p^{3}, Fibonacci Quart. 33, no. 4 (1995), 290–297.
- [79] D.E. Knuth and H.S. Wilf, The power of a prime that divides a generalized binomial coefficient, J. Reine Angew. Math. 396 (1989), 212–219.
- [80] E.E. Kummer, Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen, J. Reine Angew. Math. 44 (1852), 93–146.
- [81] A. Laugier and M.P. Saikia, A characterization of a prime p p from the binomial coefficient ( n p) {n\choose p} with n > p + 1 n>p+1 a natural number,
- [82] A. Laugier and M.P. Saikia, A new proof of Lucas’ Theorem, Notes on Number Theory and Discrete Mathematics 18, no. 4 (2012), 1–6; also available at arXiv:1301.4250v1 [math.NT], 2013.
- [83] S.-C. Liu and J.C.-C. Yeh, Catalan numbers modulo 2 k 2^{k}, J. Integer Sequences 13 (2010), Article 10.5.4.
- [84] C.T. Long and N. Woo, On bases for the set of integers, Duke Math. J. 38 (1971), 583–590.
- [85] A.D. Loveless, Extensions in the Theory of Lucas and Lehmer Pseudoprimes, Ph.D. Thesis, Washington State University, 2005, available at http://www.dissertations.wsu.edu.
- [86] É. Lucas, Sur les congruences des nombres eulériens et les coefficients différentiels des fonctions trigonométriques, suivant un module premier, Bull. Soc. Math. France 6 (1877–1878), 49–54.
- [87] É, Lucas, Théorie des fonctions numérique simplement périodiques, Amer. J. Math. 1 (1878), 184–240.
- [88] R.A. Macleod, Generalization of a result of E. Lucas, Canad. Math. Bull. 31, no. 1, 1988, 95–98.
- [89] R.J. McIntosh, A generalization of a congruential property of Lucas, Amer. Math. Monthly 99, No.3 (1992), 231–238.
- [90] R.J. McIntosh, On the converse of Wolstenholme’s Theorem, Acta Arith. 71 (1995), 381–389.
- [91] R.J. McIntosh and E.L. Roettger, A search for Fibonacci-Wieferich and Wolstenholme primes, Math. Comp. 76 (2007), 2087–2094.
- [92] R. Meštrović, A Note on the Congruence ( n ​ d m ​ d) ≡ ( n m) ( mod q) {nd\choose md}\equiv{n\choose m}(\bmod{\,q}), Amer. Math. Monthly 116 (2009), 75–77.
- [93] R. Meštrović, Wolstenholme’s theorem: its generalizations and extensions in the last hundred and fifty years (1862–2012); preprint arXiv:1111.3057v2 [math.NT], 2011.
- [94] R. Meštrović, Congruences for Wolstenholme primes, accepted for publication in Czechoslovak Math. J.; preprint arXiv:1108.4178v1 [math.NT], 2011.
- [95] R. Meštrović, On the mod p 7 p^{7} determination of ( 2 ​ p − 1 p − 1) {2p-1\choose p-1}, Rocky Mount. J. Math. 44 (2014), 633–548; preprint arXiv:1108.1174v1 [math.NT], 2011.
- [96] R. Meštrović, A note on the congruence ( n ​ p k m ​ p k) ≡ ( n m) ( mod p r) {np^{k}\choose mp^{k}}\equiv{n\choose m}(\bmod{\,p^{r}}), Czechoslovak Math. J. 62 (2012), No. 1, 59–65.
- [97] R. Meštrović, Variations of Lucas’ theorem modulo prime powers, 11 pages; preprint arXiv:1301.0252 [math.NT], 2012.
- [98] R. Meštrović, A Lucas’ type theorem modulo prime powers, Fibonacci Quart. 51, no. 2 (2013), 142–146; preprint arXiv:1301.0251 [math.NT], 2012.
- [99] R. Meštrović, An extension of Babbage’s criterion for primality, Math. Slovaca 63, no. 6 (2013), 1179–1182.
- [100] R. Meštrović, Some Wolstenholme type congruences, Math. Appl. 2 (2013), 35–42.
- [101] R. Meštrović, A primality criterion based on a Lucas’ congruence, arXiv:1407.7894v1 [math.NT], 2014.
- [102] T.D. Noe, On the divisibility of generalized central trinomial coefficients, J. Integer Sequences 9 (2006), Article 06.2.7.
- [103] A. Nowicki, Podróże po Imperium Liczb. Czȩść 11. Silnie i Symbole Newtona (Rozdziałl 7), University of Torun, Poland, 2011; also available at http://www.mat.uni.torun.pl/ ~ \widetilde{} anow.
- [104] G. Olive, Generalized powers, Amer. Math. Monthly 72 (1965), 619–627.
- [105] H. Pan, On divisibility of sums of Apéry polynomials; preprint arXiv:1108.1546v1 [math.NT], 2011.
- [106] H. Pan, A congruence of Lucas’ type Discrete Math. 288 (2004), 173–175.
- [107] R. Peele, A.J. Radcliffe and H.S. Wilf, Congruence problems involving Stirling numbers of the first kind, Fibonacci Quart. 31, no. 1 (1993), 27–34.
- [108] P.A. Piza, Solution of Problem 4704, Amer. Math. Monthly 64, No. 8 (1957), 597–598.
- [109] M. Prunescu, Sign-reductions, p p -adic valuations, binomial coefficients modulo p k p^{k} and triangular symmetries, available at http://home.mathematik.uni-freiburg.de.
- [110] M. Razpet, Divisibility properties of some number arrays, Ars Combin. 30 (1990), 308–318.
- [111] M. Razpet, On divisibility of binomial cefficients, Discrete Math. 135 (1994), 377–379.
- [112] M. Razpet, The Lucas property of a number array, Discrete Math. 248 (2002), 157–168.
- [113] J.B. Roberts, On binomial coefficient residues, Canad. J. Math. 9 (1957), 363–370.
- [114] E. Rowland, The number of nonzero binomial coefficients modulo p α p^{\alpha}; preprint arXiv:1001.1783v3 [math.NT], 2011.
- [115] E. Rowland and R. Yassawi, Automatic congruences for diagonals of rational functions; preprint arXiv:1310.8635v2 [math.NT], 2014.
- [116] M.P. Saikia and J. Vogrinc, A simple number theoretic result, J. Assam Academy of Math. 3 (2010), 91–96.
- [117] K. Samol and D. van Straten, Dwork congruences and reflexive polytopes; preprint arXiv:0911.0797 [math.NT], 2009.
- [118] R. Sánchez-Peregrino, The Lucas congruences for Stirling numbers of the second kind, Acta Arith. 94 (2000), 41–52.
- [119] J. Sándor and B. Crstici, Handbook of Number Theory II, Kluwer Academic Publisher, vol. 198, Dordrecht/Boston/London, 2004.
- [120] L.-L. Shi, Congruences for Lucas u u -nomial coefficients modulo p 3 p^{3}, Rocky Mountain J. Math. 37 (2007), 1027–1042.
- [121] D. Singmaster, Notes on binomial coefficients I- a generalization of Lucas’ congruence J. London Math. Soc. 8, no. 2 (1974), 545–548.
- [122] D. Singmaster, Divisibility of binomial and multinomial coefficients by primes and prime powers, 18th Anniversary Volume of the Fibonacci Association, pp. 98–113, 1980.
- [123] C.C. Siong, A simple proof of Ljunggren’s binomial congruence, Amer. Math. Monthly 121, No. 2 (2014), 162–164.
- [124] N.J.A. Sloane, The On-Line Encyclopedia of Integer Sequences, http://www.research.att.com/ njas/sequences/seis.html.
- [125] R.P. Stanley, Differentiability finite power series, European J. Combin. 1 (1980), 175–188.
- [126] R.P. Stanley, Enumerative Combinatorics, Vol. I, Cambbridge University Press, 1997.
- [127] J. Stirling, Methodus differentialis, sive tractatus de summatione et interpolazione serierum infinitarum, Londini, 1730.
- [128] V. Strehl, Zum q q -Analogon der Kongruenz von Lucas, in Séminaire Lotharingen de Combin., 5ème Session, 102–104, Strasbourg, 1982.
- [129] Z.W. Sun and D.M. Davis, Combinatorial congruences modulo prime powers, Trans. Amer. Math. Soc. 359 (2007), 5525–5553.
- [130] Z.-W. Sun and D. Wan, Lucas type congruences for cyclotomic ψ \psi -coefficients, Int. J. Number Theory 4 (2008), no. 2, 155–170.
- [131] M. Sved, Divisibility-with visibility, Math. Intelligencer 10, No. 2 (1988), 56–64.
- [132] M. Sved and R.J. Clarke, King’s walk on the infinite chessboard, Australasian J. Math. 2 (1990), 191–215.
- [133] The William Lowell Putnam Mathematical Competition, Problem A-5, Amer. Math. Monthly 86 (1979), 171–173.
- [134] R.F. Torretto and J.A. Fuchs, Generalized binomial coefficients, Fibonacci Quart. 2 (1964), 296–302.
- [135] E.R. Tou, Residues of generalized binomial coefficients modulo a product of primes, senior thesis, Spring (2002), Department of Mathematics and Computer Science, Gustavus Adolphus College, St. Peter, MN; available at http://sites.google.com/site/erikrtou/home.
- [136] M. Ward, A Calculus of Sequences, American J. Math. 58 (1936), 255–266.
- [137] D.L. Wells, Lucas theorem for generalized binomial coefficients, Ph.D. Thesis, Washington State University, 1992.
- [138] D.L. Wells, Lucas’ theorem for generalized binomial coefficients, AMS Abstracts 14 (1993), p. 32.
- [139] D.L. Wells, The Fibonacci and Lucas triangles modulo 2, Fibonacci Quart. 32, no. 2 (1994), 111–123.
- [140] B. Wilson, Fibonacci triangles modulo p p, Fibonacci Quart. 36, no. 3 (1998), 194–203.
- [141] S. Wolfram, Geometry of binomial coefficients, Amer. Math. Monthly 91 (1984), 566–571.
- [142] J. Wolstenholme, On certain properties of prime numbers, Quart. J. Pure Appl. Math. 5 (1862), 35–39.
- [143] C.F. Woodcock and H. Sharif, On the transcendence of certain series, J. Algebra 121 (1989), 364–369.
- [144] N. Zaheer [144] A generalization of Lucas’ theorem to vector spaces, Int. J. Math. and Math. Sci. 16 (1993), 267–276.
- [145] J. Zhao, Bernoulli Numbers, Wolstenholme’s theorem, and p 5 p^{5} variations of Lucas’ theorem, J. Number Theory 123 (2007), 18–26.
- [146] J. Zhao, Wolstenholme type theorem for multiple harmonic sum, Int. J. of Number Theory 4 (2008), 73–106.

## Appendix

List of references and related Lucas type congruences

from this article (arranged by year of publication)

[9, 1819] Charles Babbage (also see [52, Introduction] or [36, page 271]) - ( 19), p. 10.

[142, 1862] Joseph Wolstenholme - ( 20), p. 10.

[7, 1869] H. Anton (also see [36, p. 271]) - ( 2), p. 5)

[86, 1878], [87, 1878; Section XXI, pp. 229–230], É. Lucas (Lucas’ theorem) - the congruences ( 1) and ( 3), p. 5.

[49, 1900; p. 323] J.W.L. Glaisher (also see [103, the congruence 7.1.5] and [93, Section 6]) - ( 21), p. 10.

[19, 1949] W. Ljunggren (also see [10, Theorem 4], [52], [126, Problem 1.6 (d)] and [123]) - ( 22), p. 11.

[19, 1952] E. Jacobsthal (also see [52]) - ( 23), p. 11.

[22, 1955] L. Carlitz - ( 70), p. 25.

[26, 1956] L.E. Clarke and [108, 1957], P.A. Piza - ( 7), p. 8.

[104, 1965] G. Olive (also see [119, Chapter 5, p. 506], [32], [128] [105, Lemma 2.1]) - ( 101), p. 36.

[47, 1982; Theorem 1] I. Gessel - ( 52), p. 19.

[66, 1987; Theorem 1] F.T. Howard - ( 69), p. 25.

[66, 1987; p. 306, Corollary and Theorem 2] F.T. Howard - ( 71) and ( 72), p. 25.

[88, 1988; Theorem 2], R.A. Macleod - ( 43), p. 16.

[131, 1988; p. 61, Theorem] M. Sved - ( 64), p. 23.

[131, 1988; p. 60, Theorem] M. Sved - ( 80), p. 31.

[10, 1990; Theorem 3] D.F. Bailey - ( 31), p. 12.

[10, 1990; Theorem 5] D.F. Bailey - ( 32), p. 13.

[17, 1990; Theorem 1] R. Bollinger and C. Burchard - ( 108), p. 40.

[11, 1991; Theorem 4] D.F. Bailey - ( 26), p. 11.

[11, 1991; Theorem 5] D.F. Bailey - ( 27), p. 12.

[29, 1991; Theorem 3] K. Davis and W. Webb (also see [85, p. 88, Theorem 5.1.2] and [15, p. 34, congruence (2.2)]) - ( 37), p. 14.

[12, 1992; Theorem 5] D.F. Bailey (also see [98, Corollary 1.2]) - ( 28) and ( 29), p. 12.

[51, 1992; Proposition 2] A. Granville - ( 34), p. 13.

[89, 1992] R.J. McIntosh - ( 114), p. 42.

[137, 1992; Theorem 2] (also see [138] and [61, Section 7]) D.L. Wells - ( 84) and ( 85), p. 32.

[30, 1993; Theorem 3] K. Davis and W. Webb (also see [51, Proposition 2]) - ( 40), p. 15.

[30, 1993; Corollary 1] K. Davis and W. Webb - ( 41), p. 15.

[30, 1993; Corollary 1] K. Davis and W. Webb (also see [97, Theorem]) - ( 42), p. 15.

[76, 1993] W.A. Kimball and W.A. Webb (also see [120, p. 1029]) - ( 89) and ( 90), p. 33.

[107, 1993; Proposition 2.1] R. Peele, A.J. Radcliffe and H.S. Wilf - ( 68), p. 24.

[60, 1994; p. 60] J.M. Holte (also see [61, 1994; p. 227]) - ( 14) and ( 15), p. 9.

[111, 1994; p. 378] M. Razpet - ( 54), p. 20.

[139, 1994; Theorem 2] D.L. Wells - ( 79), p. 30.

[52, 1995; Section 6, the congruence (24)] A. Granville - ( 16), p. 9.

[52, 1995; Theorem 1] A. Granville - ( 33), p. 13.

[77, 1995; Theorems 1 and 3] W.A. Kimball and W.A. Webb - ( 91) and ( 92), p. 34.

[77, 1995; Corollaries 2 and 4] W.A. Kimball and W.A. Webb - ( 93) and ( 94), p. 34.

[77, 1995; Theorem 5] W.A. Kimball and W.A. Webb - ( 95), p. 34.

[78, 1995; Theorem] W.A. Kimball and W.A. Webb - ( 99), p. 35.

[21, 1998; Lemma 4] N.J. Calkin - ( 56), p. 20.

[140, 1998] B. Wilson - ( 96) and ( 97), p. 34.

[1, 1999; Proposition 7.1] J.-P. Allouche - ( 51), p. 18.

[61, 2000; Theorem 1] J.M. Holte - ( 81), p. 31.

[61, 2000; Theorem 3] J.M. Holte - ( 82) and ( 83), p. 32.

[118, 2000; Proposition 3.1] R. Sánchez-Peregrino - ( 65) and ( 66), pp. 23–24.

[118, 2000; Proposition 4.1] R. Sánchez-Peregrino - ( 67), p. 24.

[18, 2001; Theorem 2.2] J. Boulanger and J.-L. Chabert - ( 76), p. 27.

[69, 2001; Theorem] H. Hu and Z.-W. Sun - ( 86) and ( 87), pp. 32–33.

[68, 2002; p. 291, Theorem] H. Hu - ( 88), p. 33.

[112, 2002; Theorem 1] M. Razpet - ( 62), p. 22.

[14, 2003; Theorem 5] D. Berend and N. Kriger - ( 55), p. 20.

[106, 2004; Theorem 1] H. Pan - ( 63), p. 23.

[38, 2005; Theorem 3] T.J. Evans - ( 17), p. 9.

[33, 2006; Theorem 4.7] E. Deutsch and B.E. Sagan - ( 57), p. 21.

[33, 2006; Theorem 4.4] E. Deutsch and B.E. Sagan - ( 58), p. 21.

[120, 2007; Theorem 2] L.-L. Shi - ( 98), p. 35.

[120, 2007; Theorem 1] L.-L. Shi - ( 100), p. 36.

[129, 2007; Theorem 1.7] Z.-W. Sun and D.M. Davis - ( 75), p. 26.

[56, 2008; the congruence (1) of Corollary on page 490] C. Helou and G. Terjanian (also see [27, Section 11.6, Corollary 11.6.22, p. 381]) - ( 24), p. 11.

[72, 2008; (ii) of Lemma 2] Y. Jin, Z-J. Lu and A.L. Schmidt - ( 53), p. 19.

[130, 2008; Theorem 1.1] Z.-W. Sun and D. Wan - ( 74), p. 26.

[25, 2009; Theorem 2.2] M. Chamberland and K. Dilcher - ( 59), p. 22.

[25, 2009; Corollaries 2.1 and 2.2] M. Chamberland and K. Dilcher - ( 60) and ( 61), p. 22.

[103, 2011; the congruences 7.3.1–7.33] A. Nowicki - ( 6), p. 7.

[98, 2012; Theorem 1.1] R. Meštrović - ( 30), p. 12.

[97, 2012; Theorem] R. Meštrović (also see [30, Corollary 1]) - ( 42), p. 15.

[97, 2012; Proposition] R. Meštrović - ( 47) and ( 48), p. 17.

[115, 2014; Section 5, Theorem 5.3] E. Rowland and R. Yassawi - ( 44), p. 16.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:romeo@ac.me
