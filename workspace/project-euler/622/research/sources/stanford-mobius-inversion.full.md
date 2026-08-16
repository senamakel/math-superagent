<!-- source: https://crypto.stanford.edu/pbc/notes/numbertheory/mobius.html | converted from HTML -->

Number Theory - Möbius Inversion

-

[Number Theory][1]

-

[Modular Arithmetic][2]

-

[Euclid’s Algorithm][3]

-

[Division][4]

-

[Chinese Remainder][5]

-

[Polynomial Roots][6]

-

[Units & Totients][7]

-

[Exponentiation][8]

-

[Order of a Unit][9]

-

[Miller-Rabin Test][10]

-

[Generators][11]

-

[Cyclic Groups][12]

-

[Quadratic Residues][13]

-

[Gauss' Lemma][14]

-

[Quadratic Recip.][15]

-

[Carmichael][16]

-

[Multiplicative][17]

-

[Möbius Inversion][18]

-

[Generators II][19]

-

[Cyclotomic][20]

-

[Heptadecagon][21]

-

[Eisenstein][22]

-

[Gaussian Periods][23]

-

[Roots of Unity][24]

-

[Quadratic Forms][25]

---

-

[Notes][26]

-

[Ben Lynn][27]

[⏴ Multiplicative][17] [Generators II ⏵][19]

Contents

# Möbius Inversion

Suppose for some (not necessarily multiplicative) [number-theoretic function][17] \(f\) \[ F(n) = \sum_{d|n} f(d) .\] Can we make \(f(n)\) the subject of this equation?

We’ll see that we can find a function \(\mu\) such that \[ f(n) = \sum_{d|n} \mu(n/d) F(d) = \sum_{d|n} \mu(d) F(n/d) .\] and we call this process *Möbius inversion*.

We have \[ \begin{aligned} \sum_{d|n} \mu(d) F(n/d) &=& \sum_{d|n}\mu(d) \sum_{r|\frac{n}{d}} f(r) \\ &=& \sum_{d r |n} \mu(d)f(r) \\ &=& \sum_{r |n} f(r) \sum_{d|(n/r)} \mu(d) \end{aligned} \] If we want this equal to \(f(n)\) we need \(\mu\) to satisfy \[ \sum_{d|m}\mu(d) = \begin{cases} 0, & m > 1 \\ 1, & m = 1 \end{cases} \]

A little thought leads to this unique solution, known as the *Möbius function*: \[ \mu(n) = \begin{cases} 1 & n = 1 \\ 0 & p^2 | n \textrm{ for some prime }p \\ (-1)^r & n = p_1…​p_r \textrm{ for distinct primes }p_i \end{cases} \] Notice \(\mu\) is multiplicative, which implies \(f(n)\) is multiplicative if \(F(n)\) is. In summary,

**Theorem**: \[ F(n) = \sum_{d|n} f(d) \] if and only if \[ f(n) = \sum_{d|n} \mu(n/d) F(d) \] and \(f(n)\) is multiplicative if and only if \(F(n)\) is multiplicative.

**Example**: From before \(n = \sum_{d|n} \phi(n) \). Write \(n = p_1^{k_1}...p_m^{k_m}.\) Then \[ \begin{aligned} \phi(n) &=& \sum_{d|n} \mu(d) \frac{n}{d} \\ &=& n \sum_{d|n} \mu(d) \frac{1}{d} \\ &=& n \left(1 - \sum_i \frac{1}{p_i} + \sum_{i\ne j} \frac{1}{p_i p_j} - …​\right) \\ &=& n \left(1 - \frac{1}{p_1}\right)…​\left(1 - \frac{1}{p_m}\right) \end{aligned} \] which is another way to derive the [formula for \(\phi\)][7].

Gauss encountered the Möbius function over 30 years before Möbius when he showed that the sum of the [generators][11] of \(\mathbb{Z}_p^*\) is \(\mu(p-1)\). More generally, if \(\mathbb{Z}_n^*\) has a generator, then the sum of all the generators of \(\mathbb{Z}_n^*\) is \(\mu(\phi(n))\). This can be seen by considering the sums of the roots of polynomials of the form \(x^d - 1\) where \(d | \phi(n)\).

[⏴ Multiplicative][17] [Generators II ⏵][19]

Contents

---

## Contents

-

[Number Theory][1]

-

[Modular Arithmetic][2]

-

[Euclid’s Algorithm][3]

-

[Division][4]

-

[Chinese Remainder][5]

-

[Polynomial Roots][6]

-

[Units & Totients][7]

-

[Exponentiation][8]

-

[Order of a Unit][9]

-

[Miller-Rabin Test][10]

-

[Generators][11]

-

[Cyclic Groups][12]

-

[Quadratic Residues][13]

-

[Gauss' Lemma][14]

-

[Quadratic Recip.][15]

-

[Carmichael][16]

-

[Multiplicative][17]

-

[Möbius Inversion][18]

-

[Generators II][19]

-

[Cyclotomic][20]

-

[Heptadecagon][21]

-

[Eisenstein][22]

-

[Gaussian Periods][23]

-

[Roots of Unity][24]

-

[Quadratic Forms][25]

---

-

[Notes][26]

-

[Ben Lynn][27]

[back to top]

[Ben Lynn][28]*blynn@cs.stanford.edu*💡


## Links

[1]: .
[2]: arith.html
[3]: euclid.html
[4]: division.html
[5]: crt.html
[6]: poly.html
[7]: units.html
[8]: exp.html
[9]: order.html
[10]: millerrabin.html
[11]: gen.html
[12]: cyclic.html
[13]: qr.html
[14]: gausslemma.html
[15]: quadrecip.html
[16]: carmichael.html
[17]: mult.html
[18]: mobius.html
[19]: gengen.html
[20]: cyclo.html
[21]: 17gon.html
[22]: eisenstein.html
[23]: gaussperiod.html
[24]: rootsunity.html
[25]: form.html
[26]: ../
[27]: https://crypto.stanford.edu/~blynn/
[28]: /~blynn/
