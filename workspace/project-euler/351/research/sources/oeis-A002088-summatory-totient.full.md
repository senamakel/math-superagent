<!-- source: https://oeis.org/A002088 | converted from HTML -->

A002088 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A002088 - OEIS] [3]

A002088

Sum of totient function: a(n) = Sum_{k=1..n} phi(k), cf. [A000010][4].
(Formerly M1008 N0376)

154

0, 1, 2, 4, 6, 10, 12, 18, 22, 28, 32, 42, 46, 58, 64, 72, 80, 96, 102, 120, 128, 140, 150, 172, 180, 200, 212, 230, 242, 270, 278, 308, 324, 344, 360, 384, 396, 432, 450, 474, 490, 530, 542, 584, 604, 628, 650, 696, 712, 754, 774, 806, 830, 882, 900, 940, 964

( [list][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

0,3

COMMENTS

Number of elements in the set {(x,y): 1 <= x <= y <= n, 1=gcd(x,y)}. - [Michael Somos][12], Jun 13 1999

Sum_{k=1..n} phi(k) gives the number of distinct arithmetic progressions which contain an infinite number of primes and whose difference does not exceed n. E.g., {1k+1}, {2k+1}, {3k+1, 3k+2}, {4k+1, 4k+3}, {5k+1, ..5k+4} means 10 sequences. - [Labos Elemer][13], May 02 2001

The quotient [A024916][14] (n)/a(n) = SummatorySigma/SummatoryTotient as n increases seems to approach Pi^4/36 = zeta(2)^2 = [A098198][15] = 2.705808084277845... . - [Labos Elemer][13], Sep 20 2004 (corrected by Peter Pein, Apr 28 2009)

Also the number of rationals p/q in (0,1] with denominators q<=n. - [Franz Vrabec][16], Jan 29 2005

a(n) is the number of initial segments of Beatty sequences for real numbers > 1, cut off when the next term in the sequence would be >= n. For example, the sequence 1,2 is included for n=3 and n=4, but not for n >= 5 because the next term of the Beatty sequence must be 3 or 4. Problem suggested by [David W. Wilson][17]. - [Franklin T. Adams-Watters][18], Oct 19 2006

Number of complex numbers satisfying any one of {x^1=1, x^2=1, x^3=1, x^4=1, x^5=1, ..., x^n=1}. - Paul Smith (math.idiot(AT)gmail.com), Mar 19 2007

a(n+2) equals the number of Sturmian words of length n which are 'special', prefix of two Sturmian words of length n+1. - [Fred Lunnon][19], Sep 05 2010

For n > 1: [A020652][20] (a(n)) = 1 and [A038567][21] (a(n)) = n; for n > 0: [A214803][22] (a(n)) = 1. - [Reinhard Zumkeller][23], Jul 29 2012

Also number of elements in the set {(x,y): 1 <= x + y <= n, x >= 0, y > 0, with x and y relatively prime integers}. Thus, the number of reduced rational numbers x/y with x nonnegative, y positive, and x + y <= n. (For n >= 1, 0 <= x/y <= n - 1, clearly including each integer in this interval.) - [Rick L. Shepherd][24], Apr 08 2014

This function, the partial sums of phi = [A000010][4], is sometimes denoted by (uppercase) Phi. - [M. F. Hasler][25], Apr 18 2015

From [Roger Ford][26], Jan 16 2016: (Start)

For n >= 1: a(n) is the number of perfect arched semi-meander solutions with n arches. To be perfect the number of arch groupings must equal the number of arches with a length of 1 in the current generation and every preceding generation.

Example: p is the number of arches with length 1 (/\), g is the number of arch groups (-), n is number of arches in the top half of a semi-meander solution

/\

/\ //\\

//\\-/\-///\\\- n=6 p=3 g=3 Each preceding arch configuration

/\ /\ is formed by attaching the arch

/\-//\\-//\\- n=5 p=3 g=3 end in the first position and the

/\ arch end in the last position.

//\\

///\\\-/\- n=4 p=2 g=2

/\

//\\-/\- n=3 p=2 g=2

/\-/\- n=2 p=2 g=2

/\- n=1 p=1 g=1. (End)

a(n) is the number of distinct lists of binary words of length n that are balanced (Sturmian). - [Dan Rockwell][27], Will Wodrich, Aaliyah Fiala, and Bob Burton, May 30 2019

2013 IMO Problem 6 shows that a(n) is the number of ways to arrange the numbers 0, 1, ..., n on a circle such that for any numbers 0 <= a < b < c < d <= n, the chord joining a and d does not intersect with the chord intersecting b and c, with rotation counted as same. - [Yifan Xie][28], Aug 26 2025

REFERENCES

Albert H. Beiler, Recreations in the Theory of Numbers, Dover Publications, 1966, Chap. XVI.

Steven R. Finch, Mathematical Constants, Cambridge, 2003, pp. 115-119.

Ronald L. Graham, Donald E. Knuth, and Oren Patashnik, Concrete Mathematics. Addison-Wesley, Reading, MA, 1990, p. 138.

M. N. Huxley, The Distribution of Prime Numbers, Oxford Univ. Press, 1972, p. 6.

D. H. Lehmer, Guide to Tables in the Theory of Numbers. Bulletin No. 105, National Research Council, Washington, DC, 1941, pp. 7-10.

Ivan Niven and Herbert S. Zuckerman, An Introduction to the Theory of Numbers. 2nd ed., Wiley, NY, 1966, p. 94, Problem 11.

József Sándor, Dragoslav S. Mitrinovic, and Borislav Crstici, Handbook of Number Theory I, Springer Science & Business Media, 2005, Chapter I, section 21, pp. 24-25.

N. J. A. Sloane, A Handbook of Integer Sequences, Academic Press, 1973 (includes this sequence).

N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

J. V. Uspensky and M. A. Heaslet, Elementary Number Theory, McGraw-Hill, NY, 1939, p. 111.

LINKS

Al Zimmermann, [Table of n, a(n) for n = 0..50000][29] (Terms 0 to 1000 by T. D. Noe)

Dorin Andrica and Ovidiu Bagdasar, [On some results concerning the polygonal polynomials][30], Carpathian Journal of Mathematics, Vol. 35, No. 1 (2019), 1-11.

Art of Problem Solving, [2013 IMO Problem 6][31].

Sarah Bockting-Conrad, Yevgenia Kashina, T. Kyle Petersen, and Bridget Eileen Tenner, [Sós permutations][32], arXiv:2007.01132 [math.CO], 2020.

Rayan Chikhi, Vladan Jovicic, Stefan Kratsch, Paul Medvedev, Martin Milanic, Sofya Raskhodnikova, and Nithin Varma, [Bipartite Graphs of Small Readability][33], arXiv:1805.04765 [cs.DM], 2018.

Steven R. Finch, [Euler Totient Function Asymptotic Constants][34]. [Broken link]

Steven R. Finch, [Euler Totient Function Asymptotic Constants][35]. [From the Wayback machine]

Paul Loomis, Michael Plytage and John Polhill, [Summing up the Euler phi function][36], The College Mathematics Journal, Vol. 39, No. 1 (Jan. 2008), pp. 34-42.

József Sándor, Dragoslav S. Mitrinovic, and Borislav Crstici, [Handbook of Number Theory I][37], Volume 1, Springer, 2005, p. 24.

Mehtaab Sawhney, [Problem H-807][38], Advanced Problems and Solutions, The Fibonacci Quarterly, Vol. 55, No. 2 (2017), p. 184; [Identities with sums of Euler and number of squarefree divisors functions][39], Solution to Problem H-807 by the proposer, ibid., Vol. 57, No. 2 (2019), pp. 186-187.

N. J. A. Sloane, [Families of Essentially Identical Sequences][40], Mar 24 2021 (Includes this sequence).

James J. Sylvester, [On the number of fractions contained in any Farey series of which the limiting number is given][41], in: London, Edinburgh and Dublin Philosophical Magazine (5th series) 15 (1883), p. 251 = Collected Mathematical Papers, Vols. 1-4, Cambridge Univ. Press, 1904-1912, Vol. 4, p. 103 (see below).

J. J. Sylvester, The collected mathematical papers of James Joseph Sylvester, [vol. 2][42], [vol. 3][43], [vol. 4][44].

A. Walfisz, [Weylsche Exponentialsummen in der neueren Zahlentheorie][45], VEB Deutscher Verlag der Wissenschaften, Berlin 1963.

Eric Weisstein's World of Mathematics, [Beatty Sequence][46].

Eric Weisstein's World of Mathematics, [Totient Function][47].

Eric Weisstein's World of Mathematics, [Totient Summatory Function][48].

R. G. Wilson, v, [Letter to N. J. A. Sloane, Jan 24 1989][49].

FORMULA

a(n) = (3*n^2)/(Pi^2) + O(n log n).

More precisely, a(n) = (3/Pi^2)*n^2 + O(n*(log(n))^(2/3)*(log(log(n)))^(4/3)), (A. Walfisz 1963). - [Benoit Cloitre][50], Feb 02 2003

a(n) = (1/2)*Sum_{k>=1} mu(k)*floor(n/k)*floor(1+n/k). - [Benoit Cloitre][50], Apr 11 2003

a(n) = [A000217][51] (n) - [A063985][52] (n) = [A018805][53] (n) - [A015614][54] (n). - [Reinhard Zumkeller][23], Jan 21 2013

A slightly simpler version of Cloitre's formula is a(n) = 1/2 + Sum_{k=1..oo} floor(n/k)^2*mu(k)/2. - [Bill Gosper][55], Jul 25 2020

The quotient [A024916][14] (n)/a(n) = SummatorySigma/SummatoryTotient as n increases seems to approach (Pi^4)/36 = Zeta(2)^2 = 2.705808084277845. See also [A067282][56]. - [Labos Elemer][13], Sep 21 2004

[A024916][14] (n)/a(n) = zeta(2)^2 + O(log(n)/n). This follows from asymptotic formulas for the sequences. - [Franklin T. Adams-Watters][18], Oct 19 2006

Row sums of triangle [A134542][57]. - [Gary W. Adamson][58], Oct 31 2007

G.f.: (Sum_{n>=1} mu(n)*x^n/(1-x^n)^2)/(1-x), where mu(n) = [A008683][59] (n). - [Mamuka Jibladze][60], Apr 06 2015

a(n) = [A005728][61] (n) - 1, for n >= 0. - [Wolfdieter Lang][62], Nov 22 2016

a(n) = (Sum_{k=1..floor(sqrt(n))} k*(k+1) * (M(floor(n/k)) - M(floor(n/(k+1)))) + Sum_{k=1..floor(n/(1+floor(sqrt(n))))} mu(k) * floor(n/k) * floor(1+n/k))/2, where M(k) is the Mertens function ( [A002321][63]) and mu(k) is the Moebius function ( [A008683][59]). - [Daniel Suteu][64], Nov 23 2018

a(n) = [A015614][54] (n)+1. - [R. J. Mathar][65], Apr 26 2023

a(n) = [A000217][51] (n) - Sum{k=2..n} a(floor(n/k)). From summing over Id = 1 (Dirichlet convolution) phi. - [Jason Xu][66], Jul 31 2024

a(n) = Sum_{k=1..n} k*[A002321][63] (floor(n/k)). - [Ridouane Oudra][67], Jul 03 2025

a(n) = Sum_{i=1..n} floor(n/i) * Sum_{j=1..i} mu(gcd(i, j)), where mu is the Moebius function ( [A008683][59]) (Sawhney, 2017). - [Amiram Eldar][68], Dec 29 2025

EXAMPLE

G.f. = x + 2*x^2 + 4*x^3 + 6*x^4 + 10*x^5 + 12*x^6 + 18*x^7 + 22*x^8 + 28*x^9 + ...

MAPLE

with(numtheory): [A002088][69]:=n->add(phi(i), i=1..n): seq( [A002088][69] (n), n=0..70);

MATHEMATICA

Table[Plus @@ EulerPhi[Range[n]], {n, 0, 57}] (* [Alonso del Arte][70], May 30 2006 *)

(* Alternative: *)

Accumulate[EulerPhi[Range[0, 60]]] (* [Harvey P. Dale][71], Aug 27 2011 *)

PROG

(PARI) a(n)=sum(k=1, n, eulerphi(k)) \\ [Charles R Greathouse IV][72], Jun 16 2011

(PARI) a(n)=if(n>0, my(s=1); forsquarefree(k=1, n, s+=(n\k[1])^2*moebius(k)); s/2, 0); \\ [Charles R Greathouse IV][72], Oct 15 2021

(PARI) first(n)=my(v=vector(n), s); forfactored(k=1, n, v[k[1]]=s+=eulerphi(k)); v \\ [Charles R Greathouse IV][72], Oct 15 2021

(Haskell)

a002088 n = a002088_list !! n

a002088_list = scanl (+) 0 a000010_list -- [Reinhard Zumkeller][23], Jul 29 2012

(GAP) List([1..60], n->Sum([1..n], i->Phi(i))); # [Muniru A Asiru][73], Jul 31 2018

(Magma) [&+[EulerPhi(i): i in [1..n]]: n in [1..60]]; // [Vincenzo Librandi][74], Aug 01 2018

(SageMath) [sum(euler_phi(k) for k in (1..n)) for n in (0..60)] # [G. C. Greubel][75], Nov 25 2018

(Python)

from functools import lru_cache

@lru_cache(maxsize=None)

def [A002088][69] (n): # based on second formula in [A018805][53]

if n == 0:

return 0

c, j = 0, 2

k1 = n//j

while k1 > 1:

j2 = n//k1 + 1

c += (j2-j)*(2*[A002088][69] (k1)-1)

j, k1 = j2, n//j2

return (n*(n-1)-c+j)//2 # [Chai Wah Wu][76], Mar 24 2021

CROSSREFS

Cf. [A000010][4], [A000217][51], [A001088][77], [A002321][63], [A005728][61], [A008683][59], [A015614][54], [A018805][53], [A020652][20], [A214803][22], [A024916][14], [A038567][21], [A063985][52], [A067282][56], [A098198][15], [A134542][57].

Sequence in context: [A162578][78] [A152919][79] [A306564][80] * [A092249][81] [A019332][82] [A002491][83]

Adjacent sequences: [A002085][84] [A002086][85] [A002087][86] * [A002089][87] [A002090][88] [A002091][89]

KEYWORD

nonn, easy, nice

AUTHOR

[N. J. A. Sloane][90]

EXTENSIONS

Additional comments from [Len Smiley][91]

STATUS

approved

[Lookup][3] [Welcome][92] [Wiki][93] [Register][94] [Music][95] [Plot 2][96] [Demos][97] [Index][98] [WebCam][99] [Contribute][100] [Format][101] [Style Sheet][102] [Transforms][103] [Superseeker][104] [Recents][105]

[The OEIS Community][106]

Maintained by [The OEIS Foundation Inc.][107]

Last modified August 14 12:19 EDT 2026. Contains 398312 sequences.

[License Agreements, Terms of Use, Privacy Policy][108]


## Links

[1]: /login?redirect=%2fA002088
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A000010
[5]: /A002088/list
[6]: /A002088/graph
[7]: /search?q=A002088+-id:A002088
[8]: /A002088/listen
[9]: /history?seq=A002088
[10]: /search?q=id:A002088&fmt=text
[11]: /A002088/internal
[12]: /wiki/User:Michael_Somos
[13]: /wiki/User:Labos_Elemer
[14]: /A024916
[15]: /A098198
[16]: /wiki/User:Franz_Vrabec
[17]: /wiki/User:David_W._Wilson
[18]: /wiki/User:Franklin_T._Adams-Watters
[19]: /wiki/User:Fred_Lunnon
[20]: /A020652
[21]: /A038567
[22]: /A214803
[23]: /wiki/User:Reinhard_Zumkeller
[24]: /wiki/User:Rick_L._Shepherd
[25]: /wiki/User:M._F._Hasler
[26]: /wiki/User:Roger_Ford
[27]: /wiki/User:Dan_Rockwell
[28]: /wiki/User:Yifan_Xie
[29]: /A002088/b002088.txt
[30]: https://doi.org/10.37193/CJM.2019.01.01
[31]: https://artofproblemsolving.com/community/c6h1181543p5720264
[32]: https://arxiv.org/pdf/2007.01132
[33]: https://arxiv.org/pdf/1805.04765
[34]: http://www.people.fas.harvard.edu/~sfinch/constant/totient/totient.html
[35]: http://web.archive.org/web/20010603070928/http://www.mathsoft.com/asolve/constant/totient/totient.html
[36]: https://www.jstor.org/stable/27646564
[37]: https://doi.org/10.1007/1-4020-3658-2
[38]: https://www.fq.math.ca/Problems/May2017advanced.pdf
[39]: https://www.fq.math.ca/Problems/AdvProbMay2019.pdf
[40]: /A115004/a115004.txt
[41]: https://doi.org/10.1080/14786448308627346
[42]: http://www.hti.umich.edu/cgi/t/text/text-idx?sid=b88432273f115fb346725f1a42422e19;c=umhistmath;idno=AAS8085.0002.001
[43]: http://www.hti.umich.edu/cgi/t/text/text-idx?sid=b88432273f115fb346725f1a42422e19;c=umhistmath;idno=AAS8085.0003.001
[44]: http://www.hti.umich.edu/cgi/t/text/text-idx?sid=b88432273f115fb346725f1a42422e19;c=umhistmath;idno=AAS8085.0004.001
[45]: https://doi.org/10.1002/zamm.19640441217
[46]: https://mathworld.wolfram.com/BeattySequence.html
[47]: https://mathworld.wolfram.com/TotientFunction.html
[48]: https://mathworld.wolfram.com/TotientSummatoryFunction.html
[49]: /A002088/a002088.pdf
[50]: /wiki/User:Benoit_Cloitre
[51]: /A000217
[52]: /A063985
[53]: /A018805
[54]: /A015614
[55]: /wiki/User:Bill_Gosper
[56]: /A067282
[57]: /A134542
[58]: /wiki/User:Gary_W._Adamson
[59]: /A008683
[60]: /wiki/User:Mamuka_Jibladze
[61]: /A005728
[62]: /wiki/User:Wolfdieter_Lang
[63]: /A002321
[64]: /wiki/User:Daniel_Suteu
[65]: /wiki/User:R._J._Mathar
[66]: /wiki/User:Jason_Xu
[67]: /wiki/User:Ridouane_Oudra
[68]: /wiki/User:Amiram_Eldar
[69]: /A002088
[70]: /wiki/User:Alonso_del_Arte
[71]: /wiki/User:Harvey_P._Dale
[72]: /wiki/User:Charles_R_Greathouse_IV
[73]: /wiki/User:Muniru_A_Asiru
[74]: /wiki/User:Vincenzo_Librandi
[75]: /wiki/User:G._C._Greubel
[76]: /wiki/User:Chai_Wah_Wu
[77]: /A001088
[78]: /A162578
[79]: /A152919
[80]: /A306564
[81]: /A092249
[82]: /A019332
[83]: /A002491
[84]: /A002085
[85]: /A002086
[86]: /A002087
[87]: /A002089
[88]: /A002090
[89]: /A002091
[90]: /wiki/User:N._J._A._Sloane
[91]: /wiki/User:Len_Smiley
[92]: /wiki/Welcome
[93]: /wiki/Main_Page
[94]: /wiki/Special:RequestAccount
[95]: /play.html
[96]: /plot2.html
[97]: /demo1.html
[98]: /wiki/Index_to_OEIS
[99]: /webcam
[100]: /Submit.html
[101]: /eishelp2.html
[102]: /wiki/Style_Sheet
[103]: /transforms.html
[104]: /ol.html
[105]: /recent
[106]: /community.html
[107]: http://oeisf.org
[108]: /wiki/Legal_Documents
