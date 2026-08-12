<!-- source: https://oeis.org/wiki/Multiply-perfect_numbers | converted from HTML -->

Multiply-perfect numbers - OeisWiki

This site is supported by donations to [The OEIS Foundation][1].

# Multiply-perfect numbers

From OeisWiki

There are no approved revisions of this page, so it may **not**have been [reviewed][2].

Jump to navigation Jump to search

*Perfect numbers, like perfect men, are very rare.*— [Descartes][3]

The **multiply-perfect numbers**(

**

*k* |

**

**-perfect numbers**) are the [positive integers][4] divisible by their [sum of divisors][5].

## Contents

- 1*k*-perfect numbers

  - 1.1 Table of *k*-perfect numbers
  - 1.2 Smallest *k*-perfect numbers
  - 1.3 1-perfect numbers
  - 1.4 2-perfect numbers (perfect numbers)

    - 1.4.1 Even perfect numbers
    - 1.4.2 Odd perfect numbers

  - 1.5*k*-perfect numbers with *k*≥ 3 (multiperfect numbers)

    - 1.5.1 Even *k*-perfect numbers with *k*≥ 3 (even multiperfect numbers)
    - 1.5.2 Odd *k*-perfect numbers with *k*≥ 3 (odd multiperfect numbers)
    - 1.5.3 Conjectured number of *k*-perfect numbers for each *k*≥ 3

- 2 Almost *k*-perfect numbers

  - 2.1 Almost 1-perfect numbers
  - 2.2 Almost 2-perfect numbers
  - 2.3 Almost *k*-perfect numbers with *k*≥ 3 (almost multiperfect numbers)

- 3 Quasi *k*-perfect numbers

  - 3.1 Quasi 1-perfect numbers
  - 3.2 Quasi 2-perfect numbers
  - 3.3 Quasi *k*-perfect numbers with *k*≥ 3 (quasi multiperfect numbers)

- 4*k*-deficient numbers

  - 4.1 2-deficient numbers (deficient numbers)

- 5*k*-abundant numbers

  - 5.1 2-abundant numbers (abundant numbers)

- 6 Sequences
- 7 See also
- 8 Notes
- 9 References
- 10 External links

## *k*-perfect numbers

[[edit][6]]

A

**

*k* |

**

**-perfect number**is an integer

*n* |

such that its [sum of divisors][5] is

*k**n*, *k*≥ 1, *k*∈ ℕ, |

i.e.

σ 1 ( n): = ∑ i = 1 σ 0 ( n) d ( i) = ∑ i | n i = 1 n i = ∑ i = 1 n [n mod i = 0] ⋅ i = k n, k ≥ 1, k ∈ ℕ,

where

*d*(*i*) |

is the

*i* |

th [divisor][7] of

*n* |

,

*σ*0 (*n*) = *τ*(*n*) |

is the [number of divisors][8] of

*n* |

,

*σ*1 (*n*) = *σ*(*n*) |

is the [sum of divisors][5] of

*n* |

and

[·] |

is the [Iverson bracket][9]. Equivalently, a

**

*k* |

**

**-perfect number**is an integer

*n* |

such that its [harmonic sum of divisors][10] is

*k*, *k*≥ 1, *k*∈ ℕ, |

i.e.

σ − 1 ( n): = ∑ i = 1 σ 0 ( n) 1 d ( i) = ∑ i | n i = 1 n 1 i = ∑ i = 1 n [n mod i = 0] ⋅ ( 1 i) = ∑ i = 1 n [n mod i = 0] ⋅ ( 1 n / i) = ∑ i = 1 n [n mod i = 0] ⋅ ( i n) = σ 1 ( n) n = k,

where

*σ*−1 (*n*) |

is the harmonic sum of divisors of

*n* |

. For example,

672 |

is a [3-perfect number][11], since its divisors add up to

2016 |

, and that is thrice

672 |

.

### Table of *k*-perfect numbers

[[edit][12]]

For

*k*≥ 2 |

, it is not known whether these are finite or infinite sequences (obviously, there is only one

1 |

-perfect number, i.e

1 |

).

**

*k* |

-perfect numbers**

*k* |

 | Sequences

*a**k*(*n*), *n*≥ 1. |

 | [A-number][13] |

**1** |

{1} |

 |  |

**2** |

{6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 2658455991569831744654692615953842176, ...} |

 | [A000396][14] |

**3** |

{120, 672, 523776, 459818240, 1476304896, 51001180160, ...} |

 | [A005820][15] |

**4** |

{30240, 32760, 2178540, 23569920, 45532800, 142990848, 1379454720, 43861478400, 66433720320, ...} |

 | [A027687][16] |

**5** |

{14182439040, 31998395520, 518666803200, 13661860101120, 30823866178560, 740344994887680, 796928461056000, 212517062615531520, 69357059049509038080, ...} |

 | [A046060][17] |

**6** |

{154345556085770649600, 9186050031556349952000, 680489641226538823680000, 6205958672455589512937472000, 13297004660164711617331200000, ...} |

 | [A046061][18] |

**7** |

{141310897947438348259849402738485523264343544818565120000, ...} |

 |  |

**8** |

{2 62 × 3 15 × 5 9 × 7 7 × 11 3 × 13 3 × 17 2 × 19 × 23 × 29 × 31 × 37 × 41 × 43 × 53 × 61 × 71 × 97 2 × 521 2 × 6118243316177221840497066178204572112368770107012542227185747, ...} |

 |  |

### Smallest *k*-perfect numbers

[[edit][19]]

Smallest

*k* |

-perfect number for each

*k*≥ 1 |

.
[A007539][20] First

*n* |

-fold perfect number,

*n*≥ 1 |

.

{1, 6, 120, 30240, 14182439040, 154345556085770649600, 141310897947438348259849402738485523264343544818565120000,
8268099687077761372899241948635962893501943883292455548843932421413884476391773708366277840568053624227289196057256213348352000000000, ...} |

### 1-perfect numbers

[[edit][21]]

There is only one

1 |

-perfect number, i.e.

1 |

.

### 2-perfect numbers (perfect numbers)

[[edit][22]]

When

*k* |

is not specified, it is generally understood to mean

*k*= 2 |

, i.e. [perfect numbers][23]. These numbers have been studied since [Euclid][24] 's time.

The ancient Christian scholar Augustine explained that God could have created the world in an instant but chose to do it in a perfect number of days, 6. Early Jewish commentators felt that the perfection of the universe was shown by the Moon's period of 28 days. The next in line are 496, 8128, and 33550336. All end in 6 or 8, though what seems to be an alternating pattern of 6's and 8's for the first few perfect numbers doesn't continue. In a 1638 letter to [Mersenne][25], Descartes proposed that every [even perfect number][26] is of [Euclid][24] 's form, and stated that he saw no reason why an [odd perfect number][27] could not exist (Dickson 2005, p. 12). As [René Descartes][3] pointed out: "Perfect numbers like perfect men are very rare." It isn't known if there are infinitely many perfect numbers (for each [Mersenne prime][28] we have a corresponding [even perfect number][26], but it isn't known if there are infinitely many [Mersenne primes][28].) It is also not known if there are any [odd perfect numbers][27].

#### Even perfect numbers

[[edit][29]]

The **even perfect numbers**are of the form

n = 2 m ( 2 m + 1 − 1) = 2 m σ ( 2 m), m ≥ 1,

where

2*m*+1 − 1 |

must be [prime][30] (called a [Mersenne prime][28], see [A000668][31]).

σ ( n) = σ ( 2 m) σ ( σ ( 2 m)) = σ ( 2 m) σ ( 2 m + 1 − 1) = σ ( 2 m) 2 m + 1 = ( 2 m + 1 − 1) 2 m + 1 = 2 m + 1 ( 2 m + 1 − 1) = 2 n, m ≥ 1,

since powers of

2 |

, with positive exponent, are [almost-perfect][32].

**Theorem.***( [Euclid][24])*

If

2*m*− 1 |

is a prime number (called a Mersenne prime), then

*n*= (2*m*− 1) (2*m*− 1) |

is a [perfect number][23] (see [A000396][14]).

*Proof.*Labelling for our convenience the Mersenne prime as

*p*= 2*m*− 1 |

, the divisors of

*n* |

are the powers of

2 |

from

1 |

to

2*m*− 1 |

and each of those powers multiplied by

*p* |

. Since

∑ |

*m*− 1

 |

*i*= 0

 |

 |

2*i*= 2*m*− 1 |

, the sum of the divisors of

*n* |

is

(2*m*− 1) + (2*m*− 1) *p* |

. Further rewriting, we get

*σ*(*n*) = (2*m*− 1) (1 + *p*) = (2*m*− 1) (1 + 2*m*− 1) = 2*m*(2*m*− 1) = 2 ⋅ (2*m*− 1) (2*m*− 1) = 2*n* |

, as predicted. [1] □

It wasn't until [Leonhard Euler][33] came along that the converse was proven.

**Theorem.***(Euler)*

If

*n* |

is an [even perfect number][26], it must be the product of a Mersenne prime

*p*= 2*m*− 1 |

and the power of two

2*m*− 1 |

. (See [A000079][34] for the powers of 2.)

*Proof.*PROOF GOES HERE. □ (Provide proof: PROOF GOES HERE. □) [2]

Between Euclid and Euler, medieval mathematicians made some conjectures about perfect numbers that have since been proven false, such as that there is a perfect number between each consecutive power of 10 (there are no perfect numbers between 10000 and 100000, or for that matter between 10000 and 10000000), and that the least significant base 10 digit of each successive perfect number alternates between 6 and 8 (supported by reference only to the first five perfect numbers). [3]

Every even [perfect number][23] is a [triangular number][35], since they are a subset of

2 n − 1 ⋅ ( 2 n − 1) = ( 2 n − 1) 2 n 2 = t 2 n − 1,

where

2*n*− 1 |

is prime.

Every even [perfect number][23] is also an [hexagonal number][36], since they are a subset of

2 n − 1 ⋅ ( 2 n − 1) = 2 n − 1 ⋅ ( 2 ⋅ 2 n − 1 − 1) = h 2 n − 1,

where

2*n*− 1 |

is prime.

#### Odd perfect numbers

[[edit][37]]

*Main article page: [Odd perfect numbers][27]*

*It is not known whether **odd perfect numbers**exist or not!*Mathematicians have been able to prove all sorts of necessary (but not sufficient) requirements for the existence of such numbers without being able to prove either that they do exist or that they don't exist.

### *k*-perfect numbers with *k*≥ 3 (multiperfect numbers)

[[edit][38]]

When

*k*≥ 3 |

, these are considered [multiperfect numbers][39].

#### Even *k*-perfect numbers with *k*≥ 3 (even multiperfect numbers)

[[edit][40]]

(...)

#### Odd *k*-perfect numbers with *k*≥ 3 (odd multiperfect numbers)

[[edit][41]]

(...)

#### Conjectured number of *k*-perfect numbers for each *k*≥ 3

[[edit][42]]

[A134639][43] Conjectured count of numbers

*k* |

such that

*σ*(*k*) |

*k* |

= *n*, *n*≥ 3 |

.

{6, 36, 65, 245, 516, ...} |

Follow the thread relating to the following SeqFan post on [http://list.seqfan.eu/pipermail/seqfan/2012-July/thread.html#9825][44]

```
---------- Forwarded message ----------
From: Georgi Guninski < [[email protected]][45]>
To: Sequence Fanatics Discussion list < [[email protected]][45]>
Cc:
Date: Mon, 16 Jul 2012 13:14:33 +0300
Subject: [seqfan] Re: Reference that " [A027687][16] 4-perfect numbers" is finite
Thank you.

Asked because an odd perfect number and infinitely mersenne primes implies
4-perfect numbers are infinite (and a lot of other 2k-perfect numbers) -
take the product of the OPN and coprime to it EPN.

On the other hand 4-perfect being finite and infinitely mersenne primes
implies no OPN.

What is the reason to believe all 4-perfect are discovered (even if they
are finite)?
```

## Almost *k*-perfect numbers

[[edit][46]]

An

**almost

*k* |

**

**-perfect number**is an integer

*n* |

such that its [sum of divisors][5] is

*k**n*− 1, *k*≥ 1, *k*∈ ℕ, |

i.e.

σ 1 ( n): = ∑ i = 1 σ 0 ( n) d ( i) = ∑ i | n i = 1 n i = ∑ i = 1 n [n mod i = 0] ⋅ i = k n − 1, k ≥ 1, k ∈ ℕ,

where

*d*(*i*) |

is the

*i* |

th [divisor][7] of

*n* |

,

*σ*0 (*n*) = *τ*(*n*) |

is the [number of divisors][8] of

*n* |

,

*σ*1 (*n*) = *σ*(*n*) |

is the [sum of divisors][5] of

*n* |

and

[·] |

is the [Iverson bracket][9].

### Almost 1-perfect numbers

[[edit][47]]

(...)

### Almost 2-perfect numbers

[[edit][48]]

The powers of two are

**almost

2 |

**

**-perfect numbers**(**almost-perfect numbers**), since

σ ( 2 m) = 2 m + 1 − 1 = 2 ⋅ 2 m − 1, m ≥ 1..

### Almost *k*-perfect numbers with *k*≥ 3 (almost multiperfect numbers)

[[edit][49]]

(...)

## Quasi *k*-perfect numbers

[[edit][50]]

A

**quasi

*k* |

**

**-perfect number**is an integer

*n* |

such that its [sum of divisors][5] is

*k**n*+ 1, *k*≥ 1, *k*∈ ℕ, |

i.e.

σ 1 ( n): = ∑ i = 1 σ 0 ( n) d ( i) = ∑ i | n i = 1 n i = ∑ i = 1 n [n mod i = 0] ⋅ i = k n + 1, k ≥ 1, k ∈ ℕ,

where

*d*(*i*) |

is the

*i* |

th [divisor][7] of

*n* |

,

*σ*0 (*n*) = *τ*(*n*) |

is the [number of divisors][8] of

*n* |

,

*σ*1 (*n*) = *σ*(*n*) |

is the [sum of divisors][5] of

*n* |

and

[·] |

is the [Iverson bracket][9].

### Quasi 1-perfect numbers

[[edit][51]]

The primes

*p* |

are [[quasi

1 |

-perfect numbers]] since

*σ*(*p*) = *p*+ 1 |

.

### Quasi 2-perfect numbers

[[edit][52]]

(...)

### Quasi *k*-perfect numbers with *k*≥ 3 (quasi multiperfect numbers)

[[edit][53]]

(...)

## *k*-deficient numbers

[[edit][54]]

A

**

*k* |

**

**-deficient number**is an integer

*n* |

such that its [sum of divisors][5] is less than

*k**n*, *k*≥ 1, *k*∈ ℕ, |

i.e.

σ 1 ( n): = ∑ i = 1 σ 0 ( n) d ( i) = ∑ i | n i = 1 n i = ∑ i = 1 n [n mod i = 0] ⋅ i < k n, k ≥ 1, k ∈ ℕ,

where

*d*(*i*) |

is the

*i* |

th [divisor][7] of

*n* |

,

*σ*0 (*n*) = *τ*(*n*) |

is the [number of divisors][8] of

*n* |

,

*σ*1 (*n*) = *σ*(*n*) |

is the [sum of divisors][5] of

*n* |

and

[·] |

is the [Iverson bracket][9].

### 2-deficient numbers (deficient numbers)

[[edit][55]]

*Main article page: [Deficient numbers][56]*

(1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 22, 23, 25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 41, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 55, 57, 58, 59, 61, 62, 63, 64, 65, 67, 68, 69, 71, 73, 74, 75, 76, 77, 79, 81, 82, 83, 85, 86, 87, 89, 91, 92, 93, 94, 95, 97, 98, 99…)

## *k*-abundant numbers

[[edit][57]]

A

**

*k* |

**

**-abundant number**is an integer

*n* |

such that its [sum of divisors][5] is more than

*k**n*, *k*≥ 1, *k*∈ ℕ, |

i.e.

σ 1 ( n): = ∑ i = 1 σ 0 ( n) d ( i) = ∑ i | n i = 1 n i = ∑ i = 1 n [n mod i = 0] ⋅ i > k n, k ≥ 1, k ∈ ℕ,

where

*d*(*i*) |

is the

*i* |

th [divisor][7] of

*n* |

,

*σ*0 (*n*) = *τ*(*n*) |

is the [number of divisors][8] of

*n* |

,

*σ*1 (*n*) = *σ*(*n*) |

is the [sum of divisors][5] of

*n* |

and

[·] |

is the [Iverson bracket][9].

### 2-abundant numbers (abundant numbers)

[[edit][58]]

*Main article page: [Abundant numbers][59]*

(12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100...)

## Sequences

[[edit][60]]

[A007691][61] Multiply-perfect numbers:

*n* |

divides

*σ*(*n*) |

.

{1, 6, 28, 120, 496, 672, 8128, 30240, 32760, 523776, 2178540, 23569920, 33550336, 45532800, 142990848, 459818240, 1379454720, 1476304896, 8589869056, 14182439040, 31998395520, 43861478400, ...} |

[A054030][62]

*σ*(*n*) |

*n* |

 |

for

*n* |

such that

*σ*(*n*) |

is divisible by

*n* |

.

{1, 2, 2, 3, 2, 3, 2, 4, 4, 3, 4, 4, 2, 4, 4, 3, 4, 3, 2, 5, 5, 4, 3, 4, 2, 4, 4, 5, 4, 5, 5, 4, 5, 5, 4, 4, 4, 5, 4, 4, 2, 5, 4, 5, 6, 5, 5, 5, 5, 5, 5, 6, 5, 5, 4, 5, 6, 5, 4, 4, 5, 4, 5, 4, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 5, 6, 5, 6, 6, 5, 4, 4, ...} |

## See also

[[edit][63]]

- [Category:Multiperfect numbers][64]
- [A007539][20] lists the smallest

*k* |

-perfect number.

- [Perfect numbers][23] (singles) (

*σ*(*n*) − *n*= *n* |

)
- [Amicable numbers][65] (pairs) (

*σ*(*m*) − *m*= *n* |

and

*σ*(*n*) − *n*= *m* |

)
- [Sociable numbers][66] (

*k* |

-tuples) (

*σ*(*n**i*) − *n**i*= *n*(*i*+1) mod *k*, *i*= 0 .. *k*− 1, *k*≥ 3 |

)

## Notes

[[edit][67]]

1. ↑ James A. Anderson & James M. Bell, *Number Theory with Applications,*Upper Saddle River, New Jersey: Prentice Hall (1997): p. 124, Theorem 2.21.
2. ↑ Needs proof.
3. ↑ Thomas Koshy, *Elementary Number Theory with Applications,*Elsevier Academic Press (2007): 375.

## References

[[edit][68]]

- Dickson, L. E., *History of the Theory of Numbers,*Vol. 1: Divisibility and Primality. New York: Dover, pp. 3-33, 2005.

## External links

[[edit][69]]

- [The Multiply Perfect Numbers Page][70].
- [Weisstein, Eric W.][71], [Multiperfect Number][72], from MathWorld—A Wolfram Web Resource.
- PlanetMath, [Table of small multiply perfect numbers][73].
- [OddPerfect.org][74]

Retrieved from " [https://oeis.org/wiki/Multiply-perfect_numbers][75] "

[Category][76]:

- [Multiply-perfect numbers][77]

Hidden categories:

- [Pages using the math template without the tex argument][78]
- [Articles containing theorems][79]
- [Prove][80]
- [To do][81]

## Navigation menu

### Page actions

- [Page][82]
- [Discussion][83]
- [Read][82]
- [View source][84]
- [History][85]

### Page actions

- [Page][82]
- [Discussion][83]
- More
- Tools

### Personal tools

- [Request account][86]
- [Log in][87]

[88]

### Navigation

- [OEIS][89]
- [Wiki Main Page][88]
- [Community portal][90]
- [System Status][91]
- [Recent changes][92]
- [Random page][93]
- [Help][94]
- [Special pages][95]

### Search

### Tools

- [What links here][96]
- [Related changes][97]
- Printable version
- [Page information][98]

[image: Powered by MediaWiki] [99]

- Content is available under [The OEIS End-User License Agreement][100] unless otherwise noted.
- [License Agreements, Terms of Use, Privacy Policy][101]
- [About OeisWiki][102]
- [Disclaimers][103]


## Links

[1]: http://oeisf.org/
[2]: /wiki/Help:Page_validation
[3]: /wiki/Ren%C3%A9_Descartes
[4]: /wiki/Positive_integers
[5]: /wiki/Sum_of_divisors
[6]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=1
[7]: /wiki/Divisors
[8]: /wiki/Number_of_divisors
[9]: /wiki/Iverson_bracket
[10]: /wiki/Harmonic_sum_of_divisors
[11]: /w/index.php?title=3-perfect_numbers&amp;action=edit&amp;redlink=1
[12]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=2
[13]: /wiki/A-number
[14]: https://oeis.org/A000396
[15]: https://oeis.org/A005820
[16]: https://oeis.org/A027687
[17]: https://oeis.org/A046060
[18]: https://oeis.org/A046061
[19]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=3
[20]: https://oeis.org/A007539
[21]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=4
[22]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=5
[23]: /wiki/Perfect_numbers
[24]: /wiki/Euclid
[25]: /wiki/Marin_Mersenne
[26]: /wiki/Even_perfect_numbers
[27]: /wiki/Odd_perfect_numbers
[28]: /wiki/Mersenne_primes
[29]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=6
[30]: /wiki/Prime_numbers
[31]: https://oeis.org/A000668
[32]: /wiki/Almost-perfect_numbers
[33]: /wiki/Leonhard_Euler
[34]: https://oeis.org/A000079
[35]: /wiki/Triangular_numbers
[36]: /wiki/Hexagonal_numbers
[37]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=7
[38]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=8
[39]: /wiki/Multiperfect_numbers
[40]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=9
[41]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=10
[42]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=11
[43]: https://oeis.org/A134639
[44]: http://list.seqfan.eu/pipermail/seqfan/2012-July/thread.html#9825
[45]: /cdn-cgi/l/email-protection
[46]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=12
[47]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=13
[48]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=14
[49]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=15
[50]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=16
[51]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=17
[52]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=18
[53]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=19
[54]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=20
[55]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=21
[56]: /wiki/Deficient_numbers
[57]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=22
[58]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=23
[59]: /wiki/Abundant_numbers
[60]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=24
[61]: https://oeis.org/A007691
[62]: https://oeis.org/A054030
[63]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=25
[64]: /wiki/Category:Multiperfect_numbers
[65]: /wiki/Amicable_numbers
[66]: /wiki/Sociable_numbers
[67]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=26
[68]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=27
[69]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit&amp;section=28
[70]: http://wwwhomes.uni-bielefeld.de/achim/mpn.html
[71]: http://mathworld.wolfram.com/about/author.html
[72]: http://mathworld.wolfram.com/MultiperfectNumber.html
[73]: https://planetmath.org/?op=getobj&amp;from=objects&amp;id=10268
[74]: http://oddperfect.org/
[75]: https://oeis.org/wiki/Multiply-perfect_numbers
[76]: /wiki/Special:Categories
[77]: /wiki/Category:Multiply-perfect_numbers
[78]: /wiki/Category:Pages_using_the_math_template_without_the_tex_argument
[79]: /wiki/Category:Articles_containing_theorems
[80]: /wiki/Category:Prove
[81]: /wiki/Category:To_do
[82]: /wiki/Multiply-perfect_numbers
[83]: /wiki/Talk:Multiply-perfect_numbers
[84]: /w/index.php?title=Multiply-perfect_numbers&amp;action=edit
[85]: /w/index.php?title=Multiply-perfect_numbers&amp;action=history
[86]: /wiki/Special:RequestAccount
[87]: /w/index.php?title=Special:UserLogin&amp;returnto=Multiply-perfect+numbers
[88]: /wiki/Main_Page
[89]: https://oeis.org/
[90]: /wiki/OeisWiki:Community_portal
[91]: /wiki/OeisWiki:System_Status
[92]: /wiki/Special:RecentChanges
[93]: /wiki/Special:Random
[94]: https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Contents
[95]: /wiki/Special:SpecialPages
[96]: /wiki/Special:WhatLinksHere/Multiply-perfect_numbers
[97]: /wiki/Special:RecentChangesLinked/Multiply-perfect_numbers
[98]: /w/index.php?title=Multiply-perfect_numbers&amp;action=info
[99]: https://www.mediawiki.org/
[100]: /wiki/The_OEIS_End-User_License_Agreement
[101]: /wiki/OeisWiki:Privacy_policy
[102]: /wiki/OeisWiki:About
[103]: /wiki/OeisWiki:General_disclaimer
