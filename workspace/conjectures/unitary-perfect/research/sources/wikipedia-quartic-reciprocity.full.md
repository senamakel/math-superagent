<!-- source: https://en.wikipedia.org/wiki/Quartic_reciprocity | converted from HTML -->

Quartic reciprocity - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Conditions in number theory

**Quartic**or **biquadratic reciprocity**is a collection of theorems in [elementary][1] and [algebraic][2] [number theory][3] that state conditions under which the [congruence][4]*x*4 ≡*p*(mod *q*) is solvable; the word "reciprocity" comes from the form of some of these theorems, in that they relate the solvability of the congruence *x*4 ≡*p*(mod *q*) to that of *x*4 ≡*q*(mod *p*).

## History

[[edit][5]]

[Euler][6] made the first conjectures about biquadratic reciprocity. [1] [Gauss][7] published two monographs on biquadratic reciprocity. In the first one (1828) he proved Euler's conjecture about the biquadratic character of 2. In the second one (1832) he stated the biquadratic reciprocity law for the Gaussian integers and proved the supplementary formulas. He said [2] that a third monograph would be forthcoming with the proof of the general theorem, but it never appeared. Jacobi presented proofs in his Königsberg lectures of 1836–37. [3] The first published proofs were by Eisenstein. [4] [5] [6] [7]

Since then a number of other proofs of the classical (Gaussian) version have been found, [8] as well as alternate statements. Lemmermeyer states that there has been an explosion of interest in the [rational reciprocity laws][8] since the 1970s. [A] [9]

## Integers

[[edit][9]]

A **quartic**or **biquadratic residue**(mod *p*) is any number congruent to the [fourth power][10] of an integer (mod *p*). If *x*4 ≡*a*(mod *p*) does not have an integer solution, *a*is a **quartic**or **biquadratic nonresidue**(mod *p*). [10]

As is often the case in number theory, it is easiest to work modulo prime numbers, so in this section all moduli *p*, *q*, etc., are assumed to positive, odd primes. [10]

### Gauss

[[edit][11]]

The first thing to notice when working within the ring **Z**of integers is that if the prime number *q*is ≡ 3 (mod 4) then a residue *r*is a [quadratic residue][12] (mod *q*) [if and only if][13] it is a biquadratic residue (mod *q*). Indeed, the first supplement of [quadratic reciprocity][14] states that − 1 is a quadratic nonresidue (mod *q*), so that for any integer *x*, one of *x*and −*x*is a quadratic residue and the other one is a nonresidue. Thus, if *r*≡*a*2 (mod *q*) is a quadratic residue, then if *a*≡*b*2 is a residue, *r*≡*a*2 ≡*b*4 (mod *q*) is a biquadratic residue, and if *a*is a nonresidue, −*a*is a residue, −*a*≡*b*2, and again, *r*≡ ( −*a*) 2 ≡*b*4 (mod *q*) is a biquadratic residue. [11]

Therefore, the only interesting case is when the modulus *p*≡ 1 (mod 4).

Gauss proved [12] that if *p*≡ 1 (mod 4) then the nonzero residue classes (mod *p*) can be divided into four sets, each containing (*p*− 1)/4 numbers. Let *e*be a quadratic nonresidue. The first set is the quartic residues; the second one is *e*times the numbers in the first set, the third is *e*2 times the numbers in the first set, and the fourth one is *e*3 times the numbers in the first set. Another way to describe this division is to let *g*be a [primitive root][15] (mod *p*); then the first set is all the numbers whose indices with respect to this root are ≡ 0 (mod 4), the second set is all those whose indices are ≡ 1 (mod 4), etc. [13] In the vocabulary of [group theory][16], the first set is a subgroup of [index][17] 4 (of the multiplicative group **Z**/p**Z**×), and the other three are its cosets.

The first set is the biquadratic residues, the third set is the quadratic residues that are not quartic residues, and the second and fourth sets are the quadratic nonresidues. Gauss proved that − 1 is a biquadratic residue if *p*≡ 1 (mod 8) and a quadratic, but not biquadratic, residue, when *p*≡ 5 (mod 8). [14]

2 is a quadratic residue mod *p*if and only if *p*≡ ±1 (mod 8). Since *p*is also ≡ 1 (mod 4), this means *p*≡ 1 (mod 8). Every such prime is the sum of a square and twice a square. [15]

Gauss proved [14]

**Let *q*= *a*2 + 2*b*2 ≡ 1 (mod 8) be a prime number. Then **

**2 is a biquadratic residue (mod *q*) if and only if *a*≡ ±1 (mod 8), and****2 is a quadratic, but not a biquadratic, residue (mod *q*) if and only if *a*≡ ±3 (mod 8).**

Every prime *p*≡ 1 (mod 4) is the sum of two squares. [16] If *p*= *a*2 + *b*2 where *a*is odd and *b*is even, Gauss proved [17] that

2 belongs to the first (respectively second, third, or fourth) class defined above if and only if *b*≡ 0 (resp. 2, 4, or 6) (mod 8). The first case of this is one of Euler's conjectures:

**2 is a biquadratic residue of a prime *p*≡ 1 (mod 4) if and only if *p*= *a*2 + 64*b*2.**

### Dirichlet

[[edit][18]]

For an odd prime number *p*and a quadratic residue *a*(mod *p*), [Euler's criterion][19] states that a p − 1 2 ≡ 1 ( mod p), {\displaystyle a^{\frac {p-1}{2}}\equiv 1{\pmod {p}},}[image: {\displaystyle a^{\frac {p-1}{2}}\equiv 1{\pmod {p}},}] so if *p*≡ 1 (mod 4), a p − 1 4 ≡ ± 1 ( mod p). {\displaystyle a^{\frac {p-1}{4}}\equiv \pm 1{\pmod {p}}.}[image: {\displaystyle a^{\frac {p-1}{4}}\equiv \pm 1{\pmod {p}}.}]

Define the **rational quartic residue symbol**for prime *p*≡ 1 (mod 4) and quadratic residue *a*(mod *p*) as ( a p) 4 = ± 1 ≡ a p − 1 4 ( mod p). {\displaystyle {\Bigg (}{\frac {a}{p}}{\Bigg )}_{4}=\pm 1\equiv a^{\frac {p-1}{4}}{\pmod {p}}.}[image: {\displaystyle {\Bigg (}{\frac {a}{p}}{\Bigg )}_{4}=\pm 1\equiv a^{\frac {p-1}{4}}{\pmod {p}}.}] It is easy to prove that *a*is a biquadratic residue (mod *p*) if and only if ( a p) 4 = 1. {\displaystyle {\Bigg (}{\frac {a}{p}}{\Bigg )}_{4}=1.}[image: {\displaystyle {\Bigg (}{\frac {a}{p}}{\Bigg )}_{4}=1.}]

Dirichlet [18] simplified Gauss's proof of the biquadratic character of 2 (his proof only requires quadratic reciprocity for the integers) and put the result in the following form:

Let *p*= *a*2 + *b*2 ≡ 1 (mod 4) be prime, and let *i*≡*b*/*a*(mod *p*). Then

( 2 p) 4 ≡ i a b 2 ( mod p). {\displaystyle {\Bigg (}{\frac {2}{p}}{\Bigg )}_{4}\equiv i^{\frac {ab}{2}}{\pmod {p}}.}[image: {\displaystyle {\Bigg (}{\frac {2}{p}}{\Bigg )}_{4}\equiv i^{\frac {ab}{2}}{\pmod {p}}.}] (Note that *i*2 ≡ − 1 (mod *p*).)

In fact, [19] let *p*= *a*2 + *b*2 = *c*2 + 2*d*2 = *e*2 − 2*f*2 ≡ 1 (mod 8) be prime, and assume *a*is odd. Then

( 2 p) 4 = ( − 1) b 4 = ( 2 c) = ( − 1) n + d 2 = ( − 2 e), {\displaystyle {\Bigg (}{\frac {2}{p}}{\Bigg )}_{4}=\left(-1\right)^{\frac {b}{4}}={\Bigg (}{\frac {2}{c}}{\Bigg )}=\left(-1\right)^{n+{\frac {d}{2}}}={\Bigg (}{\frac {-2}{e}}{\Bigg )},}[image: {\displaystyle {\Bigg (}{\frac {2}{p}}{\Bigg )}_{4}=\left(-1\right)^{\frac {b}{4}}={\Bigg (}{\frac {2}{c}}{\Bigg )}=\left(-1\right)^{n+{\frac {d}{2}}}={\Bigg (}{\frac {-2}{e}}{\Bigg )},}] where ( x q) {\displaystyle ({\tfrac {x}{q}})}[image: {\displaystyle ({\tfrac {x}{q}})}] is the ordinary [Legendre symbol][20].

Going beyond the character of 2, let the prime *p*= *a*2 + *b*2 where *b*is even, and let *q*be a prime such that ( p q) = 1. {\displaystyle ({\tfrac {p}{q}})=1.}[image: {\displaystyle ({\tfrac {p}{q}})=1.}] Quadratic reciprocity says that ( q ∗ p) = 1, {\displaystyle ({\tfrac {q^{*}}{p}})=1,}[image: {\displaystyle ({\tfrac {q^{*}}{p}})=1,}] where q ∗ = ( − 1) q − 1 2 q. {\displaystyle q^{*}=(-1)^{\frac {q-1}{2}}q.}[image: {\displaystyle q^{*}=(-1)^{\frac {q-1}{2}}q.}] Let σ 2 ≡*p*(mod *q*). Then [20]

( q ∗ p) 4 = ( σ ( b + σ) q). {\displaystyle {\Bigg (}{\frac {q^{*}}{p}}{\Bigg )}_{4}={\Bigg (}{\frac {\sigma (b+\sigma )}{q}}{\Bigg )}.}[image: {\displaystyle {\Bigg (}{\frac {q^{*}}{p}}{\Bigg )}_{4}={\Bigg (}{\frac {\sigma (b+\sigma )}{q}}{\Bigg )}.}] This implies [21] that ( q ∗ p) 4 = 1 if and only if { b ≡ 0 ( mod q); or a ≡ 0 ( mod q) and ( 2 q) = 1; or a ≡ μ b, μ 2 + 1 ≡ λ 2 ( mod q), and ( λ ( λ + 1) q) = 1. {\displaystyle {\Bigg (}{\frac {q^{*}}{p}}{\Bigg )}_{4}=1{\mbox{ if and only if }}{\begin{cases}b\equiv 0{\pmod {q}};&{\mbox{ or }}\\a\equiv 0{\pmod {q}}{\mbox{ and }}\left({\frac {2}{q}}\right)=1;&{\mbox{ or }}\\a\equiv \mu b,\;\;\mu ^{2}+1\equiv \lambda ^{2}{\pmod {q}}{\mbox{, and }}\left({\frac {\lambda (\lambda +1)}{q}}\right)=1.\end{cases}}}[image: {\displaystyle {\Bigg (}{\frac {q^{*}}{p}}{\Bigg )}_{4}=1{\mbox{ if and only if }}{\begin{cases}b\equiv 0{\pmod {q}};&{\mbox{ or }}\\a\equiv 0{\pmod {q}}{\mbox{ and }}\left({\frac {2}{q}}\right)=1;&{\mbox{ or }}\\a\equiv \mu b,\;\;\mu ^{2}+1\equiv \lambda ^{2}{\pmod {q}}{\mbox{, and }}\left({\frac {\lambda (\lambda +1)}{q}}\right)=1.\end{cases}}}]

The first few examples are: [22]

( − 3 p) 4 = 1 if and only if b ≡ 0 ( mod 3) ( 5 p) 4 = 1 if and only if b ≡ 0 ( mod 5) ( − 7 p) 4 = 1 if and only if a b ≡ 0 ( mod 7) ( − 11 p) 4 = 1 if and only if b ( b 2 − 3 a 2) ≡ 0 ( mod 11) ( 13 p) 4 = 1 if and only if b ( b 2 − 3 a 2) ≡ 0 ( mod 13) ( 17 p) 4 = 1 if and only if a b ( b 2 − a 2) ≡ 0 ( mod 17). {\displaystyle {\begin{aligned}\left({\frac {-3}{p}}\right)_{4}=1&{\mbox{ if and only if }}&b&\equiv 0{\pmod {3}}\\\left({\frac {5}{p}}\right)_{4}=1&{\mbox{ if and only if }}&b&\equiv 0{\pmod {5}}\\\left({\frac {-7}{p}}\right)_{4}=1&{\mbox{ if and only if }}&ab&\equiv 0{\pmod {7}}\\\left({\frac {-11}{p}}\right)_{4}=1&{\mbox{ if and only if }}&b(b^{2}-3a^{2})&\equiv 0{\pmod {11}}\\\left({\frac {13}{p}}\right)_{4}=1&{\mbox{ if and only if }}&b(b^{2}-3a^{2})&\equiv 0{\pmod {13}}\\\left({\frac {17}{p}}\right)_{4}=1&{\mbox{ if and only if }}\;\;\;\;&ab(b^{2}-a^{2})&\equiv 0{\pmod {17}}.\\\end{aligned}}}[image: {\displaystyle {\begin{aligned}\left({\frac {-3}{p}}\right)_{4}=1&{\mbox{ if and only if }}&b&\equiv 0{\pmod {3}}\\\left({\frac {5}{p}}\right)_{4}=1&{\mbox{ if and only if }}&b&\equiv 0{\pmod {5}}\\\left({\frac {-7}{p}}\right)_{4}=1&{\mbox{ if and only if }}&ab&\equiv 0{\pmod {7}}\\\left({\frac {-11}{p}}\right)_{4}=1&{\mbox{ if and only if }}&b(b^{2}-3a^{2})&\equiv 0{\pmod {11}}\\\left({\frac {13}{p}}\right)_{4}=1&{\mbox{ if and only if }}&b(b^{2}-3a^{2})&\equiv 0{\pmod {13}}\\\left({\frac {17}{p}}\right)_{4}=1&{\mbox{ if and only if }}\;\;\;\;&ab(b^{2}-a^{2})&\equiv 0{\pmod {17}}.\\\end{aligned}}}]

Euler had conjectured the rules for 2, − 3 and 5, but did not prove any of them.

Dirichlet [23] also proved that if *p*≡ 1 (mod 4) is prime and ( 17 p) = 1 {\displaystyle ({\tfrac {17}{p}})=1}[image: {\displaystyle ({\tfrac {17}{p}})=1}] then

( 17 p) 4 ( p 17) 4 = { + 1 if and only if p = x 2 + 17 y 2 − 1 if and only if 2 p = x 2 + 17 y 2 {\displaystyle {\Bigg (}{\frac {17}{p}}{\Bigg )}_{4}{\Bigg (}{\frac {p}{17}}{\Bigg )}_{4}={\begin{cases}+1{\mbox{ if and only if }}\;\;p=x^{2}+17y^{2}\\-1{\mbox{ if and only if }}2p=x^{2}+17y^{2}\end{cases}}}[image: {\displaystyle {\Bigg (}{\frac {17}{p}}{\Bigg )}_{4}{\Bigg (}{\frac {p}{17}}{\Bigg )}_{4}={\begin{cases}+1{\mbox{ if and only if }}\;\;p=x^{2}+17y^{2}\\-1{\mbox{ if and only if }}2p=x^{2}+17y^{2}\end{cases}}}]

This has been extended from 17 to 17, 73, 97, and 193 by Brown and Lehmer. [24]

### Burde

[[edit][21]]

There are a number of equivalent ways of stating Burde's rational biquadratic reciprocity law.

They all assume that *p*= *a*2 + *b*2 and *q*= *c*2 + *d*2 are primes where *b*and *d*are even, and that ( p q) = 1. {\displaystyle ({\tfrac {p}{q}})=1.}[image: {\displaystyle ({\tfrac {p}{q}})=1.}]

Gosset's version is [9]

( q p) 4 ≡ ( a / b − c / d a / b + c / d) q − 1 4 ( mod q). {\displaystyle {\Bigg (}{\frac {q}{p}}{\Bigg )}_{4}\equiv {\Bigg (}{\frac {a/b-c/d}{a/b+c/d}}{\Bigg )}^{\frac {q-1}{4}}{\pmod {q}}.}[image: {\displaystyle {\Bigg (}{\frac {q}{p}}{\Bigg )}_{4}\equiv {\Bigg (}{\frac {a/b-c/d}{a/b+c/d}}{\Bigg )}^{\frac {q-1}{4}}{\pmod {q}}.}]

Letting *i*2 ≡ − 1 (mod *p*) and *j*2 ≡ − 1 (mod *q*), Frölich's law is [25]

( q p) 4 ( p q) 4 = ( a + b j q) = ( c + d i p). {\displaystyle {\Bigg (}{\frac {q}{p}}{\Bigg )}_{4}{\Bigg (}{\frac {p}{q}}{\Bigg )}_{4}={\Bigg (}{\frac {a+bj}{q}}{\Bigg )}={\Bigg (}{\frac {c+di}{p}}{\Bigg )}.}[image: {\displaystyle {\Bigg (}{\frac {q}{p}}{\Bigg )}_{4}{\Bigg (}{\frac {p}{q}}{\Bigg )}_{4}={\Bigg (}{\frac {a+bj}{q}}{\Bigg )}={\Bigg (}{\frac {c+di}{p}}{\Bigg )}.}]

Burde stated his in the form: [26] [27] [28]

( q p) 4 ( p q) 4 = ( a c − b d q). {\displaystyle {\Bigg (}{\frac {q}{p}}{\Bigg )}_{4}{\Bigg (}{\frac {p}{q}}{\Bigg )}_{4}={\Bigg (}{\frac {ac-bd}{q}}{\Bigg )}.}[image: {\displaystyle {\Bigg (}{\frac {q}{p}}{\Bigg )}_{4}{\Bigg (}{\frac {p}{q}}{\Bigg )}_{4}={\Bigg (}{\frac {ac-bd}{q}}{\Bigg )}.}]

Note that [29]

( a c + b d p) = ( p q) ( a c − b d p). {\displaystyle {\Bigg (}{\frac {ac+bd}{p}}{\Bigg )}={\Bigg (}{\frac {p}{q}}{\Bigg )}{\Bigg (}{\frac {ac-bd}{p}}{\Bigg )}.}[image: {\displaystyle {\Bigg (}{\frac {ac+bd}{p}}{\Bigg )}={\Bigg (}{\frac {p}{q}}{\Bigg )}{\Bigg (}{\frac {ac-bd}{p}}{\Bigg )}.}]

### Miscellany

[[edit][22]]

Let *p*≡*q*≡ 1 (mod 4) be primes and assume ( p q) = 1 {\displaystyle ({\tfrac {p}{q}})=1}[image: {\displaystyle ({\tfrac {p}{q}})=1}]. Then *e*2 = *p f*2 + *q g*2 has non-trivial integer solutions, and [30]

( p q) 4 ( q p) 4 = ( − 1) f g 2 ( − 1 e). {\displaystyle {\Bigg (}{\frac {p}{q}}{\Bigg )}_{4}{\Bigg (}{\frac {q}{p}}{\Bigg )}_{4}=\left(-1\right)^{\frac {fg}{2}}\left({\frac {-1}{e}}\right).}[image: {\displaystyle {\Bigg (}{\frac {p}{q}}{\Bigg )}_{4}{\Bigg (}{\frac {q}{p}}{\Bigg )}_{4}=\left(-1\right)^{\frac {fg}{2}}\left({\frac {-1}{e}}\right).}]

Let *p*≡*q*≡ 1 (mod 4) be primes and assume *p*= *r*2 + *q s*2. Then [31]

( p q) 4 ( q p) 4 = ( 2 q) s. {\displaystyle {\Bigg (}{\frac {p}{q}}{\Bigg )}_{4}{\Bigg (}{\frac {q}{p}}{\Bigg )}_{4}=\left({\frac {2}{q}}\right)^{s}.}[image: {\displaystyle {\Bigg (}{\frac {p}{q}}{\Bigg )}_{4}{\Bigg (}{\frac {q}{p}}{\Bigg )}_{4}=\left({\frac {2}{q}}\right)^{s}.}]

Let *p*= 1 + 4*x*2 be prime, let *a*be any odd number that divides *x*, and let a ∗ = ( − 1) a − 1 2 a. {\displaystyle a^{*}=\left(-1\right)^{\frac {a-1}{2}}a.}[image: {\displaystyle a^{*}=\left(-1\right)^{\frac {a-1}{2}}a.}] Then [32]*a**is a biquadratic residue (mod *p*).

Let *p*= *a*2 + 4*b*2 = *c*2 + 2*d*2 ≡ 1 (mod 8) be prime. Then [33] all the divisors of *c*4 −*p a*2 are biquadratic residues (mod *p*). The same is true for all the divisors of *d*4 −*p b*2.

## Gaussian integers

[[edit][23]]

### Background

[[edit][24]]

In his second monograph on biquadratic reciprocity Gauss displays some examples and makes conjectures that imply the theorems listed above for the biquadratic character of small primes. He makes some general remarks, and admits there is no obvious general rule at work. He goes on to say

The theorems on biquadratic residues gleam with the greatest simplicity and genuine beauty only when the field of arithmetic is extended to **imaginary**numbers, so that without restriction, the numbers of the form *a*+ *bi*constitute the object of study ... we call such numbers **integral complex numbers**. [34] [bold in the original]

These numbers are now called the [ring][25] of [Gaussian integers][26], denoted by **Z**[*i*]. Note that *i*is a fourth root of 1.

In a footnote he adds

The theory of cubic residues must be based in a similar way on a consideration of numbers of the form *a*+ *bh*where *h*is an imaginary root of the equation *h*3 = 1 ... and similarly the theory of residues of higher powers leads to the introduction of other imaginary quantities. [35]

The numbers built up from a cube [root of unity][27] are now called the ring of [Eisenstein integers][28]. The "other imaginary quantities" needed for the "theory of residues of higher powers" are the [rings of integers][29] of the [cyclotomic number fields][30]; the Gaussian and Eisenstein integers are the simplest examples of these.

### Facts and terminology

[[edit][31]]

Gauss develops the arithmetic theory of the "integral complex numbers" and shows that it is quite similar to the arithmetic of ordinary integers. [36] This is where the terms unit, associate, norm, and primary were introduced into mathematics.

The **units**are the numbers that divide 1. [37] They are 1, *i*, − 1, and −*i*. They are similar to 1 and − 1 in the ordinary integers, in that they divide every number. The units are the powers of *i*.

Given a number λ = *a*+ *bi*, its **conjugate**is *a*−*bi*and its **associates**are the four numbers [37]

λ = +*a*+ *bi**i*λ = −*b*+ *ai*− λ = −*a*−*bi*−*i*λ = +*b*−*ai*

If λ = *a*+ *bi*, the **norm**of λ, written N λ, is the number *a*2 + *b*2. If λ and μ are two Gaussian integers, N λ μ = N λ N μ; in other words, the norm is multiplicative. [37] The norm of zero is zero, the norm of any other number is a [positive integer][32]. ε is a unit if and only if N ε = 1. The square root of the norm of λ, a nonnegative [real number][33] which may not be a Gaussian integer, is the absolute value of lambda.

Gauss proves that **Z**[*i*] is a [unique factorization domain][34] and shows that the primes fall into three classes: [38]

- 2 is a special case: 2 = *i*3 (1 + *i*) 2. It is the only prime in **Z**divisible by the square of a prime in **Z**[*i*]. In algebraic number theory, 2 is said to ramify in **Z**[*i*].
- Positive primes in **Z**≡ 3 (mod 4) are also primes in **Z**[*i*]. In algebraic number theory, these primes are said to remain inert in **Z**[*i*].
- Positive primes in **Z**≡ 1 (mod 4) are the product of two conjugate primes in **Z**[*i*]. In algebraic number theory, these primes are said to split in **Z**[*i*].

Thus, inert primes are 3, 7, 11, 19, ... and a factorization of the split primes is

5 = (2 + *i*) × (2 −*i*), 13 = (2 + 3*i*) × (2 − 3*i*), 17 = (4 + *i*) × (4 −*i*), 29 = (2 + 5*i*) × (2 − 5*i*), ...

The associates and conjugate of a prime are also primes.

Note that the norm of an inert prime *q*is N*q*= *q*2 ≡ 1 (mod 4); thus the norm of all primes other than 1 + *i*and its associates is ≡ 1 (mod 4).

Gauss calls a number in **Z**[*i*] **odd**if its norm is an odd integer. [39] Thus all primes except 1 + *i*and its associates are odd. The product of two odd numbers is odd and the conjugate and associates of an odd number are odd.

In order to state the unique factorization theorem, it is necessary to have a way of distinguishing one of the associates of a number. Gauss defines [40] an odd number to be **primary**if it is ≡ 1 (mod (1 + *i*) 3). It is straightforward to show that every odd number has exactly one primary associate. An odd number λ = *a*+ *bi*is primary if *a*+ *b*≡*a*−*b*≡ 1 (mod 4); i.e., *a*≡ 1 and *b*≡ 0, or *a*≡ 3 and *b*≡ 2 (mod 4). [41] The product of two primary numbers is primary and the conjugate of a primary number is also primary.

The unique factorization theorem [42] for **Z**[*i*] is: if λ ≠ 0, then

λ = i μ ( 1 + i) ν π 1 α 1 π 2 α 2 π 3 α 3 … {\displaystyle \lambda =i^{\mu }(1+i)^{\nu }\pi _{1}^{\alpha _{1}}\pi _{2}^{\alpha _{2}}\pi _{3}^{\alpha _{3}}\dots }[image: {\displaystyle \lambda =i^{\mu }(1+i)^{\nu }\pi _{1}^{\alpha _{1}}\pi _{2}^{\alpha _{2}}\pi _{3}^{\alpha _{3}}\dots }]

where 0 ≤ μ ≤ 3, ν ≥ 0, the π*i*s are primary primes and the α*i*s ≥ 1, and this representation is unique, up to the order of the factors.

The notions of [congruence][4] [43] and [greatest common divisor][35] [44] are defined the same way in **Z**[*i*] as they are for the ordinary integers **Z**. Because the units divide all numbers, a congruence (mod λ) is also true modulo any associate of λ, and any associate of a GCD is also a GCD.

### Quartic residue character

[[edit][36]]

Gauss proves the analogue of [Fermat's theorem][37]: if α is not divisible by an odd prime π, then [45]

α N π − 1 ≡ 1 ( mod π) {\displaystyle \alpha ^{N\pi -1}\equiv 1{\pmod {\pi }}}[image: {\displaystyle \alpha ^{N\pi -1}\equiv 1{\pmod {\pi }}}]

Since N π ≡ 1 (mod 4), α N π − 1 4 {\displaystyle \alpha ^{\frac {N\pi -1}{4}}}[image: {\displaystyle \alpha ^{\frac {N\pi -1}{4}}}] makes sense, and α N π − 1 4 ≡ i k ( mod π) {\displaystyle \alpha ^{\frac {N\pi -1}{4}}\equiv i^{k}{\pmod {\pi }}}[image: {\displaystyle \alpha ^{\frac {N\pi -1}{4}}\equiv i^{k}{\pmod {\pi }}}] for a unique unit *i**k*.

This unit is called the **quartic**or **biquadratic residue character**of α (mod π) and is denoted by [46] [47]

[α π] = i k ≡ α N π − 1 4 ( mod π). {\displaystyle \left[{\frac {\alpha }{\pi }}\right]=i^{k}\equiv \alpha ^{\frac {N\pi -1}{4}}{\pmod {\pi }}.}[image: {\displaystyle \left[{\frac {\alpha }{\pi }}\right]=i^{k}\equiv \alpha ^{\frac {N\pi -1}{4}}{\pmod {\pi }}.}]

It has formal properties similar to those of the [Legendre symbol][20]. [48]

The congruence x 4 ≡ α ( mod π) {\displaystyle x^{4}\equiv \alpha {\pmod {\pi }}}[image: {\displaystyle x^{4}\equiv \alpha {\pmod {\pi }}}] is solvable in **Z**[*i*] if and only if [α π] = 1. {\displaystyle \left[{\frac {\alpha }{\pi }}\right]=1.}[image: {\displaystyle \left[{\frac {\alpha }{\pi }}\right]=1.}] [49] [α β π] = [α π] [β π] {\displaystyle {\Bigg [}{\frac {\alpha \beta }{\pi }}{\Bigg ]}={\Bigg [}{\frac {\alpha }{\pi }}{\Bigg ]}{\Bigg [}{\frac {\beta }{\pi }}{\Bigg ]}}[image: {\displaystyle {\Bigg [}{\frac {\alpha \beta }{\pi }}{\Bigg ]}={\Bigg [}{\frac {\alpha }{\pi }}{\Bigg ]}{\Bigg [}{\frac {\beta }{\pi }}{\Bigg ]}}] [α π] ¯ = [α ¯ π ¯] {\displaystyle {\overline {{\Bigg [}{\frac {\alpha }{\pi }}{\Bigg ]}}}={\Bigg [}{\frac {\overline {\alpha }}{\overline {\pi }}}{\Bigg ]}}[image: {\displaystyle {\overline {{\Bigg [}{\frac {\alpha }{\pi }}{\Bigg ]}}}={\Bigg [}{\frac {\overline {\alpha }}{\overline {\pi }}}{\Bigg ]}}] where the bar denotes [complex conjugation][38]. if π and θ are associates, [α π] = [α θ] {\displaystyle {\Bigg [}{\frac {\alpha }{\pi }}{\Bigg ]}={\Bigg [}{\frac {\alpha }{\theta }}{\Bigg ]}}[image: {\displaystyle {\Bigg [}{\frac {\alpha }{\pi }}{\Bigg ]}={\Bigg [}{\frac {\alpha }{\theta }}{\Bigg ]}}] if α ≡ β (mod π), [α π] = [β π] {\displaystyle {\Bigg [}{\frac {\alpha }{\pi }}{\Bigg ]}={\Bigg [}{\frac {\beta }{\pi }}{\Bigg ]}}[image: {\displaystyle {\Bigg [}{\frac {\alpha }{\pi }}{\Bigg ]}={\Bigg [}{\frac {\beta }{\pi }}{\Bigg ]}}]

The biquadratic character can be extended to odd composite numbers in the "denominator" in the same way the Legendre symbol is generalized into the [Jacobi symbol][39]. As in that case, if the "denominator" is composite, the symbol can equal one without the congruence being solvable:

[α λ] = [α π 1] α 1 [α π 2] α 2 … {\displaystyle \left[{\frac {\alpha }{\lambda }}\right]=\left[{\frac {\alpha }{\pi _{1}}}\right]^{\alpha _{1}}\left[{\frac {\alpha }{\pi _{2}}}\right]^{\alpha _{2}}\dots }[image: {\displaystyle \left[{\frac {\alpha }{\lambda }}\right]=\left[{\frac {\alpha }{\pi _{1}}}\right]^{\alpha _{1}}\left[{\frac {\alpha }{\pi _{2}}}\right]^{\alpha _{2}}\dots }] where λ = π 1 α 1 π 2 α 2 π 3 α 3 … {\displaystyle \lambda =\pi _{1}^{\alpha _{1}}\pi _{2}^{\alpha _{2}}\pi _{3}^{\alpha _{3}}\dots }[image: {\displaystyle \lambda =\pi _{1}^{\alpha _{1}}\pi _{2}^{\alpha _{2}}\pi _{3}^{\alpha _{3}}\dots }] If *a*and *b*are ordinary integers, *a*≠ 0, |*b*| > 1, gcd(*a*, *b*) = 1, then [50] [a b] = 1. {\displaystyle \left[{\frac {a}{b}}\right]=1.}[image: {\displaystyle \left[{\frac {a}{b}}\right]=1.}]

### Statements of the theorem

[[edit][40]]

Gauss stated the law of biquadratic reciprocity in this form: [2] [51]

Let π and θ be distinct primary primes of **Z**[*i*]. Then

if either π or θ or both are ≡ 1 (mod 4), then [π θ] = [θ π], {\displaystyle {\Bigg [}{\frac {\pi }{\theta }}{\Bigg ]}=\left[{\frac {\theta }{\pi }}\right],}[image: {\displaystyle {\Bigg [}{\frac {\pi }{\theta }}{\Bigg ]}=\left[{\frac {\theta }{\pi }}\right],}] but if both π and θ are ≡ 3 + 2*i*(mod 4), then [π θ] = − [θ π]. {\displaystyle {\Bigg [}{\frac {\pi }{\theta }}{\Bigg ]}=-\left[{\frac {\theta }{\pi }}\right].}[image: {\displaystyle {\Bigg [}{\frac {\pi }{\theta }}{\Bigg ]}=-\left[{\frac {\theta }{\pi }}\right].}]

Just as the quadratic reciprocity law for the Legendre symbol is also true for the Jacobi symbol, the requirement that the numbers be prime is not needed; it suffices that they be odd [relatively prime][41] nonunits. [52] Probably the most well-known statement is:

Let π and θ be primary relatively prime nonunits. Then [53]

[π θ] [θ π] − 1 = ( − 1) N π − 1 4 N θ − 1 4. {\displaystyle {\Bigg [}{\frac {\pi }{\theta }}{\Bigg ]}\left[{\frac {\theta }{\pi }}\right]^{-1}=(-1)^{{\frac {N\pi -1}{4}}{\frac {N\theta -1}{4}}}.}[image: {\displaystyle {\Bigg [}{\frac {\pi }{\theta }}{\Bigg ]}\left[{\frac {\theta }{\pi }}\right]^{-1}=(-1)^{{\frac {N\pi -1}{4}}{\frac {N\theta -1}{4}}}.}]

There are supplementary theorems [54] [55] for the units and the half-even prime 1 + *i*.

if π = *a*+ *bi*is a primary prime, then

[i π] = i − a − 1 2, [1 + i π] = i a − b − 1 − b 2 4, {\displaystyle {\Bigg [}{\frac {i}{\pi }}{\Bigg ]}=i^{-{\frac {a-1}{2}}},\;\;\;{\Bigg [}{\frac {1+i}{\pi }}{\Bigg ]}=i^{\frac {a-b-1-b^{2}}{4}},}[image: {\displaystyle {\Bigg [}{\frac {i}{\pi }}{\Bigg ]}=i^{-{\frac {a-1}{2}}},\;\;\;{\Bigg [}{\frac {1+i}{\pi }}{\Bigg ]}=i^{\frac {a-b-1-b^{2}}{4}},}]

and thus

[− 1 π] = ( − 1) a − 1 2, [2 π] = i − b 2. {\displaystyle {\Bigg [}{\frac {-1}{\pi }}{\Bigg ]}=(-1)^{\frac {a-1}{2}},\;\;\;{\Bigg [}{\frac {2}{\pi }}{\Bigg ]}=i^{-{\frac {b}{2}}}.}[image: {\displaystyle {\Bigg [}{\frac {-1}{\pi }}{\Bigg ]}=(-1)^{\frac {a-1}{2}},\;\;\;{\Bigg [}{\frac {2}{\pi }}{\Bigg ]}=i^{-{\frac {b}{2}}}.}]

Also, if π = *a*+ *bi*is a primary prime, and *b*≠ 0 then [56]

[π ¯ π] = [− 2 π] ( − 1) a 2 − 1 8 {\displaystyle {\Bigg [}{\frac {\overline {\pi }}{\pi }}{\Bigg ]}={\Bigg [}{\frac {-2}{\pi }}{\Bigg ]}(-1)^{\frac {a^{2}-1}{8}}}[image: {\displaystyle {\Bigg [}{\frac {\overline {\pi }}{\pi }}{\Bigg ]}={\Bigg [}{\frac {-2}{\pi }}{\Bigg ]}(-1)^{\frac {a^{2}-1}{8}}}] (if *b*= 0 the symbol is 0).

Jacobi defined π = *a*+ *bi*to be primary if *a*≡ 1 (mod 4). With this normalization, the law takes the form [57]

Let α = *a*+ *bi*and β = *c*+ *di*where *a*≡*c*≡ 1 (mod 4) and *b*and *d*are even be relatively prime nonunits. Then

[α β] [β α] − 1 = ( − 1) b d 4 {\displaystyle \left[{\frac {\alpha }{\beta }}\right]\left[{\frac {\beta }{\alpha }}\right]^{-1}=(-1)^{\frac {bd}{4}}}[image: {\displaystyle \left[{\frac {\alpha }{\beta }}\right]\left[{\frac {\beta }{\alpha }}\right]^{-1}=(-1)^{\frac {bd}{4}}}]

The following version was found in Gauss's unpublished manuscripts. [58]

Let α = *a*+ 2*bi*and β = *c*+ 2*di*where *a*and *c*are odd be relatively prime nonunits. Then

[α β] [β α] − 1 = ( − 1) b d + a − 1 2 d + c − 1 2 b, [1 + i α] = i b ( a − 3 b) 2 − a 2 − 1 8 {\displaystyle \left[{\frac {\alpha }{\beta }}\right]\left[{\frac {\beta }{\alpha }}\right]^{-1}=(-1)^{bd+{\frac {a-1}{2}}d+{\frac {c-1}{2}}b},\;\;\;\;\left[{\frac {1+i}{\alpha }}\right]=i^{{\frac {b(a-3b)}{2}}-{\frac {a^{2}-1}{8}}}}[image: {\displaystyle \left[{\frac {\alpha }{\beta }}\right]\left[{\frac {\beta }{\alpha }}\right]^{-1}=(-1)^{bd+{\frac {a-1}{2}}d+{\frac {c-1}{2}}b},\;\;\;\;\left[{\frac {1+i}{\alpha }}\right]=i^{{\frac {b(a-3b)}{2}}-{\frac {a^{2}-1}{8}}}}]

The law can be stated without using the concept of primary:

If λ is odd, let ε ( λ) be the unique unit congruent to λ (mod (1 + *i*) 3); i.e., ε ( λ) = *i**k*≡ λ (mod 2 + 2*i*), where 0 ≤*k*≤ 3. Then [59] for odd and relatively prime α and β, neither one a unit,

[α β] [β α] − 1 = ( − 1) N α − 1 4 N β − 1 4 ϵ ( α) N β − 1 4 ϵ ( β) N α − 1 4 {\displaystyle \left[{\frac {\alpha }{\beta }}\right]\left[{\frac {\beta }{\alpha }}\right]^{-1}=(-1)^{{\frac {N\alpha -1}{4}}{\frac {N\beta -1}{4}}}\epsilon (\alpha )^{\frac {N\beta -1}{4}}\epsilon (\beta )^{\frac {N\alpha -1}{4}}}[image: {\displaystyle \left[{\frac {\alpha }{\beta }}\right]\left[{\frac {\beta }{\alpha }}\right]^{-1}=(-1)^{{\frac {N\alpha -1}{4}}{\frac {N\beta -1}{4}}}\epsilon (\alpha )^{\frac {N\beta -1}{4}}\epsilon (\beta )^{\frac {N\alpha -1}{4}}}]

For odd λ, let λ ∗ = ( − 1) N λ − 1 4 λ. {\displaystyle \lambda ^{*}=(-1)^{\frac {N\lambda -1}{4}}\lambda .}[image: {\displaystyle \lambda ^{*}=(-1)^{\frac {N\lambda -1}{4}}\lambda .}] Then if λ and μ are relatively prime nonunits, Eisenstein proved [60]

[λ μ] = [μ ∗ λ]. {\displaystyle \left[{\frac {\lambda }{\mu }}\right]={\Bigg [}{\frac {\mu ^{*}}{\lambda }}{\Bigg ]}.}[image: {\displaystyle \left[{\frac {\lambda }{\mu }}\right]={\Bigg [}{\frac {\mu ^{*}}{\lambda }}{\Bigg ]}.}]

## See also

[[edit][42]]

- [Quadratic reciprocity][14]
- [Cubic reciprocity][43]
- [Octic reciprocity][44]
- [Eisenstein reciprocity][45]
- [Artin reciprocity][46]

## Notes

[[edit][47]]

- **A.****^**Here, "rational" means laws that are stated in terms of ordinary [integers][48] rather than in terms of the integers of some [algebraic number field][49].

## References

[[edit][50]]

1. ↑ Euler, *Tractatus*, § 456
2. 1 2 Gauss, BQ, § 67
3. ↑ Lemmermeyer, p. 200
4. ↑ Eisenstein, *Lois de reciprocite*
5. ↑ Eisenstein, *Einfacher Beweis ...*
6. ↑ Eisenstein, *Application de l'algebre ...*
7. ↑ Eisenstein, *Beitrage zur Theorie der elliptischen ...*
8. ↑ Lemmermeyer, pp. 199–202
9. 1 2 Lemmermeyer, p. 172
10. 1 2 Gauss, BQ § 2
11. ↑ Gauss, BQ § 3
12. ↑ Gauss, BQ §§ 4–7
13. ↑ Gauss, BQ § 8
14. 1 2 Gauss, BQ § 10
15. ↑ Gauss, DA Art. 182
16. ↑ Gauss, DA, Art. 182
17. ↑ Gauss BQ §§ 14–21
18. ↑ Dirichlet, *Demonstration ...*
19. ↑ Lemmermeyer, Prop. 5.4
20. ↑ Lemmermeyer, Prop. 5.5
21. ↑ Lemmermeyer, Ex. 5.6
22. ↑ Lemmmermeyer, pp.159, 190
23. ↑ Dirichlet, *Untersuchungen ...*
24. ↑ Lemmermeyer, Ex. 5.19
25. ↑ Lemmermeyer, p. 173
26. ↑ Lemmermeyer, p. 167
27. ↑ Ireland & Rosen pp.128–130
28. ↑ Burde, K. (1969). "Ein rationales biquadratisches Reziprozitätsgesetz". *J. Reine Angew. Math.*(in German). **235**: 175– 184. [Zbl][51] [0169.36902][52].
29. ↑ Lemmermeyer, Ex. 5.13
30. ↑ Lemmermeyer, Ex. 5.5
31. ↑ Lemmermeyer, Ex. 5.6, credited to Brown
32. ↑ Lemmermeyer, Ex. 6.5, credited to Sharifi
33. ↑ Lemmermeyer, Ex. 6.11, credited to E. Lehmer
34. ↑ Gauss, BQ, § 30, translation in Cox, p. 83
35. ↑ Gauss, BQ, § 30, translation in Cox, p. 84
36. ↑ Gauss, BQ, §§ 30–55
37. 1 2 3 Gauss, BQ, § 31
38. ↑ Gauss, BQ, §§ 33–34
39. ↑ Gauss, BQ, § 35. He defines "halfeven" numbers as those divisible by 1 + *i*but not by 2, and "even" numbers as those divisible by 2.
40. ↑ Gauss, BQ, § 36
41. ↑ Ireland & Rosen, Ch. 9.7
42. ↑ Gauss, BQ, § 37
43. ↑ Gauss, BQ, §§ 38–45
44. ↑ Gauss, BQ, §§ 46–47
45. ↑ Gauss, BQ, § 51
46. ↑ Gauss defined the character as the exponent *k*rather than the unit *i**k*; also, he had no symbol for the character.
47. ↑ There is no standard notation for higher residue characters in different domains (see Lemmermeyer, p. xiv); this article follows Lemmermeyer, chs. 5–6
48. ↑ Ireland & Rosen, Prop 9.8.3
49. ↑ Gauss, BQ, § 61
50. ↑ Ireland & Rosen, Prop. 9.8.3, Lemmermeyer, Prop 6.8
51. ↑ proofs are in Lemmermeyer, chs. 6 and 8, Ireland & Rosen, ch. 9.7–9.10
52. ↑ Lemmermeyer, Th. 69.
53. ↑ Lemmermeyer, ch. 6, Ireland & Rosen ch. 9.7–9.10
54. ↑ Lemmermeyer, Th. 6.9; Ireland & Rosen, Ex. 9.32–9.37
55. ↑ Gauss proves the law for 1 + *i*in BQ, §§ 68–76
56. ↑ Ireland & Rosen, Ex. 9.30; Lemmermeyer, Ex. 6.6, where Jacobi is credited
57. ↑ Lemmermeyer, Th. 6.9
58. ↑ Lemmermeyer, Ex. 6.17
59. ↑ Lemmermeyer, Ex. 6.18 and p. 275
60. ↑ Lemmermeyer, Ch. 8.4, Ex. 8.19

## Literature

[[edit][53]]

The references to the original papers of Euler, Dirichlet, and Eisenstein were copied from the bibliographies in Lemmermeyer and Cox, and were not used in the preparation of this article.

### Euler

[[edit][54]]

- Euler, Leonhard (1849), *Tractatus de numeroroum doctrina capita sedecim quae supersunt*, Comment. Arithmet. 2

This was actually written 1748–1750, but was only published posthumously; It is in Vol V, pp. 182–283 of

- Euler, Leonhard (1911–1944), *Opera Omnia, Series prima, Vols I–V*, Leipzig & Berlin: Teubner

### Gauss

[[edit][55]]

The two monographs Gauss published on biquadratic reciprocity have consecutively numbered sections: the first contains §§ 1–23 and the second §§ 24–76. Footnotes referencing these are of the form "Gauss, BQ, § *n*". Footnotes referencing the *Disquisitiones Arithmeticae*are of the form "Gauss, DA, Art. *n*".

- Gauss, Carl Friedrich (1828), *Theoria residuorum biquadraticorum, Commentatio prima*, Göttingen: Comment. Soc. regiae sci, Göttingen 6

- Gauss, Carl Friedrich (1832), *Theoria residuorum biquadraticorum, Commentatio secunda*, Göttingen: Comment. Soc. regiae sci, Göttingen 7

These are in Gauss's *Werke*, Vol II, pp. 65–92 and 93–148

German translations are in pp. 511–533 and 534–586 of the following, which also has the [Disquisitiones Arithmeticae][56] and Gauss's other papers on number theory.

- Gauss, Carl Friedrich (1965), *Untersuchungen uber hohere Arithmetik (Disquisitiones Arithmeticae & other papers on number theory) (Second edition)*, translated by Maser, H., New York: Chelsea, [ISBN][57] [0-8284-0191-8][58]

### Eisenstein

[[edit][59]]

- Eisenstein, Ferdinand Gotthold (1844), ["Lois de réciprocité"][60], *Journal für die reine und angewandte Mathematik (Crelle's Journal)*, **1844**(28), J. Reine Angew. Math. 28, pp. 53–67 (Crelle's Journal): 53– 67, [doi][61]: [10.1515/crll.1844.28.53][62], [S2CID][63] [120713971][64]

- Eisenstein, Ferdinand Gotthold (1844), *Einfacher Beweis und Verallgemeinerung des Fundamentaltheorems für die biquadratischen Reste*, J. Reine Angew. Math. 28 pp. 223–245 (Crelle's Journal)

- Eisenstein, Ferdinand Gotthold (1845), *Application de l'algèbre à l'arithmétique transcendante*, J. Reine Angew. Math. 29 pp. 177–184 (Crelle's Journal)

- Eisenstein, Ferdinand Gotthold (1846), *Beiträge zur Theorie der elliptischen Funktionen I: Ableitung des biquadratischen Fundalmentaltheorems aus der Theorie der Lemniskatenfunctionen, nebst Bemerkungen zu den Multiplications- und Transformationsformeln*, J. Reine Angew. Math. 30 pp. 185–210 (Crelle's Journal)

These papers are all in Vol I of his *Werke*.

### Dirichlet

[[edit][65]]

- Dirichlet, Pierre Gustave LeJeune (1832), *Démonstration d'une propriété analogue à la loi de Réciprocité qui existe entre deux nombres premiers quelconques*, J. Reine Angew. Math. 9 pp. 379–389 (Crelle's Journal)

- Dirichlet, Pierre Gustave LeJeune (1833), *Untersuchungen über die Theorie der quadratischen Formen*, Abh. Königl. Preuss. Akad. Wiss. pp. 101–121

both of these are in Vol I of his *Werke*.

### Modern authors

[[edit][66]]

- 2</sup> + n y<sup>2</sup>"},"publisher":{"wt":"Wiley"},"location":{"wt":"New York"},"year":{"wt":"1989"},"isbn":{"wt":"0-471-50654-0"}},"i":0}}]}'/> Cox, David A. (1989), *Primes of the form x 2 + n y 2*, New York: Wiley, [ISBN][57] [0-471-50654-0][67]

- Ireland, Kenneth; Rosen, Michael (1990), *A Classical Introduction to Modern Number Theory (Second edition)*, New York: [Springer][68], [ISBN][57] [0-387-97329-X][69]

- Lemmermeyer, Franz (2000), *Reciprocity Laws: from Euler to Eisenstein*, Springer Monographs in Mathematics, Berlin: Springer, [doi][61]: [10.1007/978-3-662-12893-0][70], [ISBN][57] [3-540-66957-4][71]

## External links

[[edit][72]]

- [Weisstein, Eric W.][73] ["Biquadratic Reciprocity Theorem"][74]. *[MathWorld][75]*.

These two papers by Franz Lemmermeyer contain proofs of Burde's law and related results:

- [Rational Quartic Reciprocity][76]
- [Rational Quartic Reciprocity II][77]

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Quartic_reciprocity&oldid=1343496542][78] "

[Categories][79]:

- [Algebraic number theory][80]
- [Modular arithmetic][81]
- [Theorems in number theory][82]

Hidden categories:

- [Articles with short description][83]
- [Short description is different from Wikidata][84]
- [CS1 German-language sources (de)][85]

Search

Quartic reciprocity

2 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Number_theory#Elementary_number_theory
[2]: https://en.wikipedia.org/wiki/Algebraic_number_theory
[3]: https://en.wikipedia.org/wiki/Number_theory
[4]: https://en.wikipedia.org/wiki/Congruence_relation
[5]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=1
[6]: https://en.wikipedia.org/wiki/Leonhard_Euler
[7]: https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss
[8]: https://en.wikipedia.org/wiki/Rational_reciprocity_law
[9]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=2
[10]: https://en.wikipedia.org/wiki/Fourth_power
[11]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=3
[12]: https://en.wikipedia.org/wiki/Quadratic_residue
[13]: https://en.wikipedia.org/wiki/If_and_only_if
[14]: https://en.wikipedia.org/wiki/Quadratic_reciprocity
[15]: https://en.wikipedia.org/wiki/Primitive_root_modulo_n
[16]: https://en.wikipedia.org/wiki/Group_theory
[17]: https://en.wikipedia.org/wiki/Index_of_a_subgroup
[18]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=4
[19]: https://en.wikipedia.org/wiki/Euler's_criterion
[20]: https://en.wikipedia.org/wiki/Legendre_symbol
[21]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=5
[22]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=6
[23]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=7
[24]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=8
[25]: https://en.wikipedia.org/wiki/Ring_(mathematics)
[26]: https://en.wikipedia.org/wiki/Gaussian_integers
[27]: https://en.wikipedia.org/wiki/Root_of_unity
[28]: https://en.wikipedia.org/wiki/Eisenstein_integers
[29]: https://en.wikipedia.org/wiki/Ring_of_integers
[30]: https://en.wikipedia.org/wiki/Cyclotomic_field
[31]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=9
[32]: https://en.wikipedia.org/wiki/Natural_number
[33]: https://en.wikipedia.org/wiki/Real_number
[34]: https://en.wikipedia.org/wiki/Unique_factorization_domain
[35]: https://en.wikipedia.org/wiki/Greatest_common_divisor
[36]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=10
[37]: https://en.wikipedia.org/wiki/Fermat's_little_theorem
[38]: https://en.wikipedia.org/wiki/Complex_conjugation
[39]: https://en.wikipedia.org/wiki/Jacobi_symbol
[40]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=11
[41]: https://en.wikipedia.org/wiki/Coprime_integers
[42]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=12
[43]: https://en.wikipedia.org/wiki/Cubic_reciprocity
[44]: https://en.wikipedia.org/wiki/Octic_reciprocity
[45]: https://en.wikipedia.org/wiki/Eisenstein_reciprocity
[46]: https://en.wikipedia.org/wiki/Artin_reciprocity
[47]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=13
[48]: https://en.wikipedia.org/wiki/Integers
[49]: https://en.wikipedia.org/wiki/Algebraic_number_field
[50]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=14
[51]: https://en.wikipedia.org/wiki/Zbl_(identifier)
[52]: https://zbmath.org/?format=complete&amp;q=an:0169.36902
[53]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=15
[54]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=16
[55]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=17
[56]: https://en.wikipedia.org/wiki/Disquisitiones_Arithmeticae
[57]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[58]: https://en.wikipedia.org/wiki/Special:BookSources/0-8284-0191-8
[59]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=18
[60]: https://zenodo.org/record/1709626
[61]: https://en.wikipedia.org/wiki/Doi_(identifier)
[62]: https://doi.org/10.1515%2Fcrll.1844.28.53
[63]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[64]: https://api.semanticscholar.org/CorpusID:120713971
[65]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=19
[66]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=20
[67]: https://en.wikipedia.org/wiki/Special:BookSources/0-471-50654-0
[68]: https://en.wikipedia.org/wiki/Springer_Science+Business_Media
[69]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-97329-X
[70]: https://doi.org/10.1007%2F978-3-662-12893-0
[71]: https://en.wikipedia.org/wiki/Special:BookSources/3-540-66957-4
[72]: /w/index.php?title=Quartic_reciprocity&amp;action=edit&amp;section=21
[73]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[74]: https://mathworld.wolfram.com/BiquadraticReciprocityTheorem.html
[75]: https://en.wikipedia.org/wiki/MathWorld
[76]: http://matwbn.icm.edu.pl/ksiazki/aa/aa67/aa6747.pdf
[77]: http://www.fen.bilkent.edu.tr/~franz/publ/aar2.pdf
[78]: https://en.wikipedia.org/w/index.php?title=Quartic_reciprocity&amp;oldid=1343496542
[79]: /wiki/Help:Category
[80]: /wiki/Category:Algebraic_number_theory
[81]: /wiki/Category:Modular_arithmetic
[82]: /wiki/Category:Theorems_in_number_theory
[83]: /wiki/Category:Articles_with_short_description
[84]: /wiki/Category:Short_description_is_different_from_Wikidata
[85]: /wiki/Category:CS1_German-language_sources_(de)
