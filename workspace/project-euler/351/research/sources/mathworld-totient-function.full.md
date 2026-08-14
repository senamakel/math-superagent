<!-- source: https://mathworld.wolfram.com/TotientFunction.html | converted from HTML -->

Totient Function -- from Wolfram MathWorld

# Totient Function

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

[image: TotientFunction]

The totient function [image: phi(n)], also called Euler's totient function, is defined as the number of [positive integers][2][image: <=n] that are [relatively prime][3] to (i.e., do not contain any factor in common with) [image: n], where 1 is counted as being [relatively prime][3] to all numbers. Since a number less than or equal to and [relatively prime][3] to a given number is called a [totative][4], the totient function [image: phi(n)] can be simply defined as the number of [totatives][4] of [image: n]. For example, there are eight [totatives][4] of 24 (1, 5, 7, 11, 13, 17, 19, and 23), so [image: phi(24)=8].

The totient function is implemented in the [Wolfram Language][5] as [EulerPhi][6] [*n*].

The number [image: n-phi(n)] is called the [cototient][7] of [image: n] and gives the number of positive integers [image: <=n] that have at least one prime factor in common with [image: n].

[image: phi(n)] is always [even][8] for [image: n>=3]. By convention, [image: phi(0)=1], although the [Wolfram Language][5] defines [EulerPhi][6] [0] equal to 0 for consistency with its [FactorInteger][9] [0] command. The first few values of [image: phi(n)] for [image: n=1], 2, ... are 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, ... (OEIS [A000010][10]). The totient function is given by the [M&ouml;bius transform][11] of 1, 2, 3, 4, ... (Sloane and Plouffe 1995, p. 22). [image: phi(n)] is plotted above for small [image: n].

For a [prime][12][image: p],

[image:  phi(p)=p-1, ] |

(1)

 |

since all numbers less than [image: p] are [relatively prime][3] to [image: p]. If [image: m=p^alpha] is a [power][13] of a [prime][12], then the numbers that have a common factor with [image: m] are the multiples of [image: p]: [image: p], [image: 2p], ..., [image: (p^(alpha-1))p]. There are [image: p^(alpha-1)] of these multiples, so the number of factors [relatively prime][3] to [image: p^alpha] is

[image: phi(p^alpha)] | [image: =] | [image: p^alpha-p^(alpha-1)] |

(2)

 |

 | [image: =] | [image: p^(alpha-1)(p-1)] |

(3)

 |

 | [image: =] | [image: p^alpha(1-1/p).] |

(4)

 |

Now take a general [image: m] divisible by [image: p]. Let [image: phi_p(m)] be the number of [positive integers][2][image: <=m] not [divisible][14] by [image: p]. As before, [image: p], [image: 2p], ..., [image: (m/p)p] have common factors, so

[image: phi_p(m)] | [image: =] | [image: m-m/p] |

(5)

 |

 | [image: =] | [image: m(1-1/p).] |

(6)

 |

Now let [image: q] be some other [prime][12] dividing [image: m]. The [integers][15] divisible by [image: q] are [image: q], [image: 2q], ..., [image: (m/q)q]. But these duplicate [image: pq], [image: 2pq], ..., [image: (m/(pq))pq]. So the number of terms that must be subtracted from [image: phi_p] to obtain [image: phi_(pq)] is

[image: Deltaphi_q(m)] | [image: =] | [image: m/q-m/(pq)] |

(7)

 |

 | [image: =] | [image: m/q(1-1/p),] |

(8)

 |

and

[image: phi_(pq)(m)] | [image: =] | [image: phi_p(m)-Deltaphi_q(m)] |

(9)

 |

 | [image: =] | [image: m(1-1/p)-m/q(1-1/p)] |

(10)

 |

 | [image: =] | [image: m(1-1/p)(1-1/q).] |

(11)

 |

By induction, the general case is then

[image: phi(n)] | [image: =] | [image: nproduct_(p|n)(1-1/p)] |

(12)

 |

 | [image: =] | [image: n(1-1/(p_1))(1-1/(p_2))...(1-1/(p_r)),] |

(13)

 |

where the product runs over all primes [image: p] dividing [image: n]. An interesting identity relating [image: phi(n^k)] to [image: phi(n)] is given by

[image:  phi(n^k)=n^(k-1)phi(n) ] |

(14)

 |

(A. Olofsson, pers. comm., Dec. 30, 2004).

Another identity relates the [divisors][16][image: d] of [image: n] to [image: n] via

[image:  sum_(d|n)phi(d)=n. ] |

(15)

 |

The totient function is connected to the [M&ouml;bius function][17][image: mu(n)] through the sum

[image:  sum_(d)dmu(n/d)=phi(n), ] |

(16)

 |

where the sum is over the divisors of [image: n], which can be proven by induction on [image: n] and the fact that [image: mu(n)] and [image: phi(n)] are multiplicative (Berlekamp 1968, pp. 91-93; van Lint and Nienhuys 1991, p. 123).

The totient function has the [Dirichlet generating function][18]

[image:  sum_(n=1)^infty(phi(n))/(n^s)=(zeta(s-1))/(zeta(s)) ] |

(17)

 |

for [image: s>2] (Hardy and Wright 1979, p. 250).

The totient function satisfies the [inequality][19]

[image:  phi(n)>=sqrt(n) ] |

(18)

 |

for all [image: n] except [image: n=2] and [image: n=6] (Kendall and Osborn 1965; Mitrinović and S&aacute;ndor 1995, p. 9). Therefore, the only values of [image: n] for which [image: phi(n)=2] are [image: n=3], 4, and 6. In addition, for composite [image: n],

[image:  phi(n)<=n-sqrt(n) ] |

(19)

 |

(Sierpiński and Schinzel 1988; Mitrinović and S&aacute;ndor 1995, p. 9).

[image: TotientFunctionInequality]

[image: phi(n)] also satisfies

[image:  liminf_(n->infty)phi(n)(lnlnn)/n=e^(-gamma), ] |

(20)

 |

where [image: gamma] is the [Euler-Mascheroni constant][20]. The values of [image: n] for which [image: phi(n)<e^(-gamma)n/(lnlnn)] are given by 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 22, ... (OEIS [A100966][21]).

The [divisor function][22] satisfies the [congruence][23]

[image: nsigma(n)] | [image: =] | [image: 2 (mod phi(n))] |

(21)

 |

 | [image: =] | [image: {0 (mod phi(n)) if phi(n)=2; 2 (mod phi(n)) otherwise] |

(22)

 |

for all [primes][12][image: p>=5] and no [composite][24] with the exception of 4, 6, and 22, where [image: sigma(n)] is the [divisor function][22]. This fact was proved by Subbarao (1974), despite the implication to the contrary, "is it true for infinitely many composite [image: n]?," stated in Guy (1994, p. 92), a query subsequently removed from Guy (2004, p. 142). No [composite][24] solution is currently known to

[image:  n-1=0 (mod phi(n)) ] |

(23)

 |

(Honsberger 1976, p. 35).

A corollary of the [Zsigmondy theorem][25] leads to the following congruence,

[image:  phi(a^n+b^n)=0 (mod n) ] |

(24)

 |

(Zsigmondy 1882, Moree 2004, Ruiz 2004ab).

The first few [image: n] for which

[image:  phi(n)=phi(n+1) ] |

(25)

 |

are given by 1, 3, 15, 104, 164, 194, 255, 495, 584, 975, ... (OEIS [A001274][26]), which have common values [image: phi(n)=1], 2, 8, 48, 80, 96, 128, 240, 288, 480, ... (OEIS [A003275][27]).

The only [image: n<10^(10)] for which

[image:  phi(n)=phi(n+1)=phi(n+2) ] |

(26)

 |

is [image: n=5186], giving

[image:  phi(5186)=phi(5187)=phi(5188)=2^53^4 ] |

(27)

 |

(Guy 2004, p. 139).

Values of [image: phi(n)] shared among [image: n] that are close together include

[image: phi(25930)] | [image: =] | [image: phi(25935)=phi(25940)=phi(25942)] |

(28)

 |

 | [image: =] | [image: 2^73^4] |

(29)

 |

[image: phi(404471)] | [image: =] | [image: phi(404473)=phi(404477)] |

(30)

 |

 | [image: =] | [image: 2^83^25^27] |

(31)

 |

(Guy 2004, p. 139). McCranie found an arithmetic progression of six numbers with equal totient functions,

[image:  phi(583200)=phi(583230)=phi(583260)=phi(583290)
 =phi(583320)=phi(583350)=155520,   ] |

(32)

 |

as well as other progressions of six numbers starting at 1166400, 1749600, ... (OEIS [A050518][28]).

If the [Goldbach conjecture][29] is true, then for every positive integer [image: m], there are [primes][12][image: p] and [image: q] such that

[image:  phi(p)+phi(q)=2m ] |

(33)

 |

(Guy 2004, p. 160). Erdős asked if this holds for [image: p] and [image: q] not necessarily prime, but this relaxed form remains unproven (Guy 2004, p. 160).

Guy (2004, p. 150) discussed solutions to

[image:  phi(sigma(n))=n, ] |

(34)

 |

where [image: sigma(n)] is the [divisor function][22]. F. Helenius has found 365 such solutions, the first of which are 2, 8, 12, 128, 240, 720, 6912, 32768, 142560, 712800, ... (OEIS [A001229][30]).

---

## See also

[Cototient][7], [Dedekind Function][31], [Euler's Totient Rule][32], [Fermat's Little Theorem][33], [Lehmer's Totient Problem][34], [Leudesdorf Theorem][35], [Noncototient][36], [Nontotient][37], [Silverman Constant][38], [Totative][4], [Totient Summatory Function][39], [Totient Valence Function][40] [Explore this topic in the MathWorld classroom][41]

## Related Wolfram sites

[https://functions.wolfram.com/NumberTheoryFunctions/EulerPhi/][42]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [Mandelbrot set][43]
- [euler totient function of 30][44]
- [euler's totient function of 10][45]

## References

Abramowitz, M. and Stegun, I. A. (Eds.). "The Euler Totient Function." &sect;24.3.2 in *[Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables, 9th printing.][46]*New York: Dover, p. 826, 1972. Beiler, A. H. Ch. 12 in *[Recreations in the Theory of Numbers: The Queen of Mathematics Entertains.][47]*New York: Dover, 1966. Berlekamp, E. R. *Algorithmic Coding Theory.*New York: McGraw-Hill, 1968. Cohen, G. L. and Segal, S. L. "A Note concerning Those [image: n] for Which [image: phi(n)+1] Divides [image: n]." *Fib. Quart.***27**, 285-286, 1989. Conway, J. H. and Guy, R. K. "Euler's Totient Numbers." *[The Book of Numbers.][48]*New York: Springer-Verlag, pp. 154-156, 1996. Courant, R. and Robbins, H. "Euler's [image: phi] Function. Fermat's Theorem Again." &sect;2.4.3 in Supplement to Ch. 1 in *[What Is Mathematics?: An Elementary Approach to Ideas and Methods, 2nd ed.][49]*Oxford, England: Oxford University Press, pp. 48-49, 1996. Guy, R. K. *[Unsolved Problems in Number Theory, 2nd ed.][50]*New York: Springer-Verlag, 1994. Guy, R. K. "Euler's Totient Function," "Does [image: phi(n)] Properly Divide [image: n-1]," "Solutions of [image: phi(m)=sigma(n)]," "Carmichael's Conjecture," "Gaps Between Totatives," "Iterations of [image: phi] and [image: sigma]," "Behavior of [image: phi(sigma(n))] and [image: sigma(phi(n))]." &sect;B36-B42 in *[Unsolved Problems in Number Theory, 3rd ed.][50]*New York: Springer-Verlag, pp. 138-151, 2004. Hardy, G. H. and Wright, E. M. *[An Introduction to the Theory of Numbers, 5th ed.][51]*Oxford, England: Clarendon Press, 1979. Havil, J. *[Gamma: Exploring Euler's Constant.][52]*Princeton, NJ: Princeton University Press, pp. 115-116, 2003. Helenius, F. Untitled. [http://pweb.netcom.com/~fredh/phisigma/pslist.html][53]. Honsberger, R. *[Mathematical Gems II.][54]*Washington, DC: Math. Assoc. Amer., p. 35, 1976. Jones, G. A. and Jones, J. M. "Euler's Function." Ch. 5 in *[Elementary Number Theory.][55]*Berlin: Springer-Verlag, pp. 83-96, 1998. Kendall, R. P. and Osborn, R. "Two Simple Lower Bounds for the Euler Phi-Function." *Texas J. Sci.***17**, 324-328, 1965. Mitrinović, D. S. and S&aacute;ndor, J. *[Handbook of Number Theory.][56]*Dordrecht, Netherlands: Kluwer, 1995. Moree, P. "Phi Function Congruence." 13 Oct 2004. [https://listserv.nodak.edu/cgi-bin/wa.exe?A2=ind0410&L=nmbrthry&T=0&F=&S=&P=1222][57]. Nagell, T. "Relatively Prime Numbers. Euler's [image: phi] -Function." &sect;8 in *[Introduction to Number Theory.][58]*New York: Wiley, pp. 23-26, 1951. Niven, I. M.; Zuckerman, H. S.; and Montgomery, H. L. *[An Introduction to the Theory of Numbers, 5th ed.][59]*New York: Wiley, p. 51, 1991. Perrot, J. 1811. Quoted in Dickson, L. E. *[History of the Theory of Numbers, Vol. 1: Divisibility and Primality.][60]*New York: Dover, p. 126, 2005. Ruiz, S. "A Congruence with the Euler Totient Function." 11 Oct 2004a. [https://arxiv.org/abs/math/0410241][61]. Ruiz, S. "Phi Function Congruence." 12 Oct 2004b. [https://listserv.nodak.edu/cgi-bin/wa.exe?A2=ind0410&L=nmbrthry&T=0&F=&S=&P=834][62]. S&eacute;roul, R. "The Euler Phi Function." &sect;2.7 in *[Programming for Mathematicians.][63]*Berlin: Springer-Verlag, pp. 14-15, 2000. Shanks, D. "Euler's [image: phi] Function." &sect;2.27 in *[Solved and Unsolved Problems in Number Theory, 4th ed.][64]*New York: Chelsea, pp. 68-71, 1993. Sierpiński, W. and Schinzel, A. *[Elementary Theory of Numbers, 2nd Eng. ed.][65]*Amsterdam, Netherlands: North-Holland, 1988. Sloane, N. J. A. Sequences [A000010][10] /M0299, [A001229][30], [A001274][26] /M2999, [A002088][66] /M1008, [A003275][27] /M1874, [A050518][28], and [A100966][21] in "The On-Line Encyclopedia of Integer Sequences." Sloane, N. J. A. and Plouffe, S. *[The Encyclopedia of Integer Sequences.][67]*San Diego, CA: Academic Press, 1995. Subbarao, M. V. "On Two Congruences for Primality." *Pacific J. Math.***52**, 261-268, 1974. van Lint, J. H. and Nienhuys, J. W. *Discrete Wiskunde.*9062333680 Academic Service, 1991. Zsigmondy, K. "Zur Theorie der Potenzreste." *Monatshefte f&uuml;r Math. u. Phys.***3**, 265-284, 1882.

## Referenced on Wolfram|Alpha

[Totient Function][68]

## Cite this as:

[Weisstein, Eric W.][69] "Totient Function." From **[MathWorld][70] --A Wolfram Resource. [https://mathworld.wolfram.com/TotientFunction.html][71]

## Subject classifications


## Links

[1]: /notebooks/NumberTheoreticFunctions/TotientFunction.nb
[2]: /PositiveInteger.html
[3]: /RelativelyPrime.html
[4]: /Totative.html
[5]: http://www.wolfram.com/language/
[6]: http://reference.wolfram.com/language/ref/EulerPhi.html
[7]: /Cototient.html
[8]: /EvenNumber.html
[9]: http://reference.wolfram.com/language/ref/FactorInteger.html
[10]: http://oeis.org/A000010
[11]: /MoebiusTransform.html
[12]: /PrimeNumber.html
[13]: /Power.html
[14]: /Divisible.html
[15]: /Integer.html
[16]: /Divisor.html
[17]: /MoebiusFunction.html
[18]: /DirichletGeneratingFunction.html
[19]: /Inequality.html
[20]: /Euler-MascheroniConstant.html
[21]: http://oeis.org/A100966
[22]: /DivisorFunction.html
[23]: /Congruence.html
[24]: /CompositeNumber.html
[25]: /ZsigmondyTheorem.html
[26]: http://oeis.org/A001274
[27]: http://oeis.org/A003275
[28]: http://oeis.org/A050518
[29]: /GoldbachConjecture.html
[30]: http://oeis.org/A001229
[31]: /DedekindFunction.html
[32]: /EulersTotientRule.html
[33]: /FermatsLittleTheorem.html
[34]: /LehmersTotientProblem.html
[35]: /LeudesdorfTheorem.html
[36]: /Noncototient.html
[37]: /Nontotient.html
[38]: /SilvermanConstant.html
[39]: /TotientSummatoryFunction.html
[40]: /TotientValenceFunction.html
[41]: /classroom/TotientFunction.html
[42]: https://functions.wolfram.com/NumberTheoryFunctions/EulerPhi/
[43]: https://www.wolframalpha.com/input/?i=Mandelbrot+set
[44]: https://www.wolframalpha.com/input/?i=euler+totient+function+of+30
[45]: https://www.wolframalpha.com/input/?i=euler%27s+totient+function+of+10
[46]: http://www.amazon.com/exec/obidos/ASIN/0486612724/ref=nosim/ericstreasuretro
[47]: http://www.amazon.com/exec/obidos/ASIN/0486210960/ref=nosim/ericstreasuretro
[48]: http://www.amazon.com/exec/obidos/ASIN/038797993X/ref=nosim/ericstreasuretro
[49]: http://www.amazon.com/exec/obidos/ASIN/0195105192/ref=nosim/ericstreasuretro
[50]: http://www.amazon.com/exec/obidos/ASIN/0387208607/ref=nosim/ericstreasuretro
[51]: http://www.amazon.com/exec/obidos/ASIN/0198531710/ref=nosim/ericstreasuretro
[52]: http://www.amazon.com/exec/obidos/ASIN/0691099839/ref=nosim/ericstreasuretro
[53]: http://pweb.netcom.com/~fredh/phisigma/pslist.html
[54]: http://www.amazon.com/exec/obidos/ASIN/0883853027/ref=nosim/ericstreasuretro
[55]: http://www.amazon.com/exec/obidos/ASIN/3540761977/ref=nosim/ericstreasuretro
[56]: http://www.amazon.com/exec/obidos/ASIN/0792338235/ref=nosim/ericstreasuretro
[57]: https://listserv.nodak.edu/cgi-bin/wa.exe?A2=ind0410&amp;L=nmbrthry&amp;T=0&amp;F=&amp;S=&amp;P=1222
[58]: http://www.amazon.com/exec/obidos/ASIN/0828401632/ref=nosim/ericstreasuretro
[59]: http://www.amazon.com/exec/obidos/ASIN/0471625469/ref=nosim/ericstreasuretro
[60]: http://www.amazon.com/exec/obidos/ASIN/0486442322/ref=nosim/ericstreasuretro
[61]: https://arxiv.org/pdf/math/0410241
[62]: https://listserv.nodak.edu/cgi-bin/wa.exe?A2=ind0410&amp;L=nmbrthry&amp;T=0&amp;F=&amp;S=&amp;P=834
[63]: http://www.amazon.com/exec/obidos/ASIN/354066422X/ref=nosim/ericstreasuretro
[64]: http://www.amazon.com/exec/obidos/ASIN/0828412979/ref=nosim/ericstreasuretro
[65]: http://www.amazon.com/exec/obidos/ASIN/0444866620/ref=nosim/ericstreasuretro
[66]: http://oeis.org/A002088
[67]: http://www.amazon.com/exec/obidos/ASIN/0125586302/ref=nosim/ericstreasuretro
[68]: https://www.wolframalpha.com/input/?i=totient+function
[69]: /about/author.html
[70]: /
[71]: https://mathworld.wolfram.com/TotientFunction.html
