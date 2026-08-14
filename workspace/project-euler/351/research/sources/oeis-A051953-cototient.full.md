<!-- source: https://oeis.org/A051953 | converted from HTML -->

A051953 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A051953 - OEIS] [3]

A051953

Cototient(n) := n - phi(n).

317

0, 1, 1, 2, 1, 4, 1, 4, 3, 6, 1, 8, 1, 8, 7, 8, 1, 12, 1, 12, 9, 12, 1, 16, 5, 14, 9, 16, 1, 22, 1, 16, 13, 18, 11, 24, 1, 20, 15, 24, 1, 30, 1, 24, 21, 24, 1, 32, 7, 30, 19, 28, 1, 36, 15, 32, 21, 30, 1, 44, 1, 32, 27, 32, 17, 46, 1, 36, 25, 46, 1, 48, 1, 38, 35, 40, 17, 54, 1, 48, 27

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,4

COMMENTS

Unlike totients, cototient(n+1) = cototient(n) never holds -- except 2-phi(2) = 3 - phi(3) = 1 -- because cototient(n) is congruent to n modulo 2. - [Labos Elemer][11], Aug 08 2001

Theorem (L. Redei): b^a(n) == b^n (mod n) for every integer b. - [Thomas Ordowski][12] and [Robert Israel][13], Mar 11 2016

Let S be the sum of the cototients of the divisors of n ( [A001065][14]). S < n iff n is deficient, S = n iff n is perfect, and S > n iff n is abundant. - [Ivan N. Ianakiev][15], Oct 06 2023

LINKS

T. D. Noe, [Table of n, a(n) for n = 1..10000][16]

J. Browkin and A. Schinzel, [On integers not of the form n-phi(n)][17], Colloq. Math., 68 (1995), 55-58.

R. E. Jamison, [The Helly bound for singular sums][18], Discrete Math., 249 (2002), 117-133.

Paul Pollack and Carl Pomerance, [Some problems of Erdős on the sum-of-divisors function][19], Trans. Amer. Math. Soc. Ser. B 3 (2016), 1-26. For Richard Guy on his 99th birthday. May his sequence be unbounded.

Carl Pomerance and Hee-Sung Yang, [Variant of a theorem of Erdős on the sum-of-proper-divisors function][20], Math. Comp. 83 (2014), 1903-1913.

N. J. A. Sloane, [Families of Essentially Identical Sequences][21], Mar 24 2021 (Includes this sequence)

Eric Weisstein's World of Mathematics, [Cototient][22]

FORMULA

a(n) = n - [A000010][23] (n).

Equals Mobius transform ( [A054525][24]) of [A001065][14]. - [Gary W. Adamson][25], Jul 11 2008

a( [A006881][26] (n)) = sopf( [A006881][26] (n)) - 1; a( [A000040][27] (n)) = 1. - [Wesley Ivan Hurt][28], May 18 2013

G.f.: sum(n>=1, [A000010][23] (n)*x^(2*n)/(1-x^n) ). - [Mircea Merca][29], Feb 23 2014

From [Ilya Gutkovskiy][30], Apr 13 2017: (Start)

G.f.: -Sum_{k>=2} mu(k)*x^k/(1 - x^k)^2.

Dirichlet g.f.: zeta(s-1)*(1 - 1/zeta(s)). (End)

From [Antti Karttunen][31], Sep 05 2018 & Apr 29 2022: (Start)

Dirichlet convolution square of [A317846][32] / [A046644][33] gives this sequence + [A063524][34].

a(n) = [A003557][35] (n) * [A318305][36] (n).

a(n) = [A000010][23] (n) - [A083254][37] (n).

a(n) = [A318325][38] (n) - [A318326][39] (n).

a(n) = Sum_{d|n} [A062790][40] (d) = Sum_{d|n, d<n} [A007431][41] (d)*( [A000005][42] (n/d)-1).

a(n) = [A048675][43] ( [A318834][44] (n)) = [A276085][45] ( [A353564][46] (n)). [These follow from the formula below]

a(n) = Sum_{d|n, d<n} [A000010][23] (d).

a(n) = [A051612][47] (n) - [A001065][14] (n).

(End)

a(n) = [A243823][48] (n) + [A010846][49] (n) - 1. - [Flávio V. Fernandes][50], Nov 03 2025

EXAMPLE

n = 12, phi(12) = 4 = |{1, 5, 7, 11}|, a(12) = 12 - phi(12) = 8, numbers not exceeding 12 and not coprime to 12: {2, 3, 4, 6, 8, 9, 10, 12}.

MAPLE

with(numtheory): [A051953][51]:= n->n-phi(n): seq( [A051953][51] (n), n=1..81);

MATHEMATICA

Table[n - EulerPhi[n], {n, 1, 80}] (* [Carl Najafi][52], Aug 16 2011 *)

PROG

(PARI) [A051953][51] (n) = n - eulerphi(n); \\ [Michael B. Porter][53], Jan 28 2010

(Haskell)

a051953 n = n - a000010 n -- [Reinhard Zumkeller][54], Jan 21 2014

(Python)

from sympy.ntheory import totient

print([i - totient(i) for i in range(1, 101)]) # [Indranil Ghosh][55], Mar 17 2017

CROSSREFS

Cf. [A000010][23], [A001065][14] (inverse Möbius transform), [A005278][56], [A001274][57], [A083254][37], [A098006][58], [A049586][59], [A051612][47], [A053579][60], [A054525][24], [A062790][40] (Möbius transform), [A063985][61] (partial sums), [A063986][62], [A290087][63].

Records: [A065385][64], [A065386][65].

Number of zeros in the n-th row of triangle [A054521][66]. - [Omar E. Pol][67], May 13 2016

Cf. [A063740][68] (number of k such that cototient(k) = n). - [M. F. Hasler][69], Jan 11 2018

Cf. [A243823][48], [A010846][49]; [A062830][70].

Sequence in context: [A063717][71] [A024994][72] [A243329][73] * [A079277][74] [A066452][75] [A007104][76]

Adjacent sequences: [A051950][77] [A051951][78] [A051952][79] * [A051954][80] [A051955][81] [A051956][82]

KEYWORD

nonn, easy, nice

AUTHOR

[Labos Elemer][11], Dec 21 1999

STATUS

approved

[Lookup][3] [Welcome][83] [Wiki][84] [Register][85] [Music][86] [Plot 2][87] [Demos][88] [Index][89] [WebCam][90] [Contribute][91] [Format][92] [Style Sheet][93] [Transforms][94] [Superseeker][95] [Recents][96]

[The OEIS Community][97]

Maintained by [The OEIS Foundation Inc.][98]

Last modified August 14 12:19 EDT 2026. Contains 398312 sequences.

[License Agreements, Terms of Use, Privacy Policy][99]


## Links

[1]: /login?redirect=%2fA051953
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A051953/list
[5]: /A051953/graph
[6]: /search?q=A051953+-id:A051953
[7]: /A051953/listen
[8]: /history?seq=A051953
[9]: /search?q=id:A051953&fmt=text
[10]: /A051953/internal
[11]: /wiki/User:Labos_Elemer
[12]: /wiki/User:Thomas_Ordowski
[13]: /wiki/User:Robert_Israel
[14]: /A001065
[15]: /wiki/User:Ivan_N._Ianakiev
[16]: /A051953/b051953.txt
[17]: http://matwbn.icm.edu.pl/ksiazki/cm/cm68/cm6817.pdf
[18]: https://doi.org/10.1016/S0012-365X(01)00240-0
[19]: https://doi.org/10.1090/btran/10
[20]: https://doi.org/10.1090/S0025-5718-2013-02775-5
[21]: /A115004/a115004.txt
[22]: https://mathworld.wolfram.com/Cototient.html
[23]: /A000010
[24]: /A054525
[25]: /wiki/User:Gary_W._Adamson
[26]: /A006881
[27]: /A000040
[28]: /wiki/User:Wesley_Ivan_Hurt
[29]: /wiki/User:Mircea_Merca
[30]: /wiki/User:Ilya_Gutkovskiy
[31]: /wiki/User:Antti_Karttunen
[32]: /A317846
[33]: /A046644
[34]: /A063524
[35]: /A003557
[36]: /A318305
[37]: /A083254
[38]: /A318325
[39]: /A318326
[40]: /A062790
[41]: /A007431
[42]: /A000005
[43]: /A048675
[44]: /A318834
[45]: /A276085
[46]: /A353564
[47]: /A051612
[48]: /A243823
[49]: /A010846
[50]: /wiki/User:Flávio_V._Fernandes
[51]: /A051953
[52]: /wiki/User:Carl_Najafi
[53]: /wiki/User:Michael_B._Porter
[54]: /wiki/User:Reinhard_Zumkeller
[55]: /wiki/User:Indranil_Ghosh
[56]: /A005278
[57]: /A001274
[58]: /A098006
[59]: /A049586
[60]: /A053579
[61]: /A063985
[62]: /A063986
[63]: /A290087
[64]: /A065385
[65]: /A065386
[66]: /A054521
[67]: /wiki/User:Omar_E._Pol
[68]: /A063740
[69]: /wiki/User:M._F._Hasler
[70]: /A062830
[71]: /A063717
[72]: /A024994
[73]: /A243329
[74]: /A079277
[75]: /A066452
[76]: /A007104
[77]: /A051950
[78]: /A051951
[79]: /A051952
[80]: /A051954
[81]: /A051955
[82]: /A051956
[83]: /wiki/Welcome
[84]: /wiki/Main_Page
[85]: /wiki/Special:RequestAccount
[86]: /play.html
[87]: /plot2.html
[88]: /demo1.html
[89]: /wiki/Index_to_OEIS
[90]: /webcam
[91]: /Submit.html
[92]: /eishelp2.html
[93]: /wiki/Style_Sheet
[94]: /transforms.html
[95]: /ol.html
[96]: /recent
[97]: /community.html
[98]: http://oeisf.org
[99]: /wiki/Legal_Documents
