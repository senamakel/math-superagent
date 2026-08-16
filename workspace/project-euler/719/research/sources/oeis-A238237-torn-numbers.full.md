A238237 - OEIS

<!-- source: https://oeis.org/A238237 | converted from HTML -->

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A238237 - OEIS] [3]

**A238237** — Numbers which when chopped into two parts with equal length, added and squared result in the same number.

Terms: 81, 2025, 3025, 9801, 494209, 998001, 24502500, 25502500, 52881984, 60481729, 99980001, 6049417284, 6832014336, 9048004641, 9999800001, 101558217124, 108878221089, 123448227904, 127194229449, 152344237969, 213018248521, 217930248900, 249500250000, 250500250000

COMMENTS

Yet another variant of the Kaprekar numbers [A006886][11]. - N. J. A. Sloane, Aug 06 2017

From Bernard Schott, Jan 21 2022: (Start)

Three subsequences:

-> {(10^m-1)^2, m >= 1} = [A059988] \ {0}; see example 9801.

-> {(10^m-1)^2 * 10^(2*m) / 4, m >= 1} = [A350869] \ {0}; see example 2025.

-> {(10^m+1)^2 * 10^(2*m) / 4, m >= 1} = [A038544] \ {1}, see example 3025. (End)

LINKS

Rémy Sigrist, Table of n, a(n) for n = 1..25000

Mohammad Javaheri, [On 2025 and Other Torn Numbers][18], Amer. Math. Monthly (2025).

Iva Kodrnja, [On Remarkable Properties of Number 2025][19], KoG, 29 (29), 74-80, 2025. See pp. 74-75, 79.

FORMULA

a(n) = [A290449](n)^2. - Bernard Schott, Jan 20 2022

EXAMPLE

2025 = (20 + 25)^2, so 2025 is in the sequence.
3025 = (30 + 25)^2, so 3025 is in the sequence.
9801 = (98 + 01)^2, so 9801 is in the sequence.

MATHEMATICA

Select[Range[600000]^2, EvenQ[len=IntegerLength[#]] && # == (Mod[#, 10^(len/2)] + Floor[#/10^(len/2)])^2 &]  (* Stefano Spezia, Jan 01 2025 *)

PROG

(PARI) forstep(m=1, 7, 2, p=10^((m+1)/2); for(n=10^m, 10^(m+1)-1, d=lift(Mod(n, p)); if(((n-d)/p+d)^2==n, print1(n, ", "))));

CROSSREFS

Subsequence of [A102766]. Subsequence: [A350870]. Cf. [A006886], [A038544], [A059988], [A350869]. For square roots see [A290449].

KEYWORD nonn, base

AUTHOR Arkadiusz Wesolowski, Feb 20 2014

## Links
[2]: http://oeisf.org/#DONATE
[3]: /
[11]: /A006886
[18]: https://doi.org/10.1080/00029890.2025.2561491
[19]: https://doi.org/10.31896/k.29.8
