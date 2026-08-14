<!-- source: https://oeis.org/A002321 | converted from HTML -->

A002321 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A002321 - OEIS] [3]

A002321

Mertens's function: Sum_{k=1..n} mu(k), where mu is the Moebius function [A008683][4].
(Formerly M0102 N0038)

156

1, 0, -1, -1, -2, -1, -2, -2, -2, -1, -2, -2, -3, -2, -1, -1, -2, -2, -3, -3, -2, -1, -2, -2, -2, -1, -1, -1, -2, -3, -4, -4, -3, -2, -1, -1, -2, -1, 0, 0, -1, -2, -3, -3, -3, -2, -3, -3, -3, -3, -2, -2, -3, -3, -2, -2, -1, 0, -1, -1, -2, -1, -1, -1, 0, -1, -2, -2, -1, -2, -3, -3, -4, -3, -3, -3, -2, -3, -4, -4, -4

( [list][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

1,5

COMMENTS

Partial sums of the Moebius function [A008683][4].

Also determinant of n X n (0,1) matrix defined by A(i,j)=1 if j=1 or i divides j.

The first positive value of Mertens's function for n > 1 is for n = 94. The graph seems to show a negative bias for the Mertens function which is eerily similar to the Chebyshev bias (described in [A156749][12] and [A156709][13]). The purported bias seems to be empirically approximated to - (6 / Pi^2) * (sqrt(n) / 4) (by looking at the graph) (see MathOverflow link, May 28 2012) where 6 / Pi^2 = 1 / zeta(2) is the asymptotic density of squarefree numbers (the squareful numbers having Moebius mu of 0). This would be a growth pattern akin to the Chebyshev bias. - [Daniel Forgues][14], Jan 23 2011

All integers appear infinitely often in this sequence. - [Charles R Greathouse IV][15], Aug 06 2012

Soundararajan proves that, on the Riemann Hypothesis, a(n) << sqrt(n) exp(sqrt(log n)*(log log n)^14), sharpening the well-known equivalence. - [Charles R Greathouse IV][15], Jul 17 2015

Balazard & De Roton improve this (on the Riemann Hypothesis) to a(n) << sqrt(n) exp(sqrt(log n)*(log log n)^k) for any k > 5/2, where the implied constant in the Vinogradov symbol depends on k. Saha & Sankaranarayanan reduce the exponent to 5/4 on additional hypotheses. - [Charles R Greathouse IV][15], Feb 02 2023

REFERENCES

E. Landau, Vorlesungen über Zahlentheorie, Chelsea, NY, Vol. 2, p. 157.

D. H. Lehmer, Guide to Tables in the Theory of Numbers. Bulletin No. 105, National Research Council, Washington, DC, 1941, pp. 7-10.

F. Mertens, "Über eine zahlentheoretische Funktion", Akademie Wissenschaftlicher Wien Mathematik-Naturlich Kleine Sitzungsber, IIa 106, (1897), p. 761-830.

D. S. Mitrinovic et al., Handbook of Number Theory, Kluwer, Section VI.1.

Biswajyoti Saha and Ayyadurai Sankaranarayanan, On estimates of the Mertens function, International Journal of Number Theory, Vol. 15, No. 02 (2019), pp. 327-337.

N. J. A. Sloane, A Handbook of Integer Sequences, Academic Press, 1973 (includes this sequence).

N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

J. von zur Gathen and J. Gerhard, Modern Computer Algebra, Cambridge, 1999, see p. 482.

LINKS

T. D. Noe, [Table of n, a(n) for n = 1..10000][16]

Michel Balazard and Anne De Roton, [Sur un critère de Baez-Duarte pour l'hypothèse de Riemann][17], Int'l J. Number Theory 6(4) (2010), 883-903. arXiv preprint arXiv:0812.1689 [math.NT], 2008.

B. Boncompagni, [Selected values of the Mertens function][18].

Olivier Bordellès, [Some Explicit Estimates for the Mobius Function][19], J. Int. Seq. 18 (2015), Article 15.11.1.

G. J. Chaitin, [Thoughts on the Riemann hypothesis][20], arXiv:math/0306042 [math.HO], 2003.

J. Brian Conrey, [The Riemann Hypothesis][21], Notices Amer. Math. Soc., 50 (No. 3, March 2003), 341-353. See p. 347.

Marc Deléglise and Joël Rivat, [Computing the summation of the Mobius function][22], Experiment. Math. 5(4) (1996), 291-295.

François Dress, [Fonction sommatoire de la fonction de Moebius. 1. Majorations expérimentales][23], Experiment. Math. 2(2) (1993), 89-98.

François Dress and Mohamed El Marraki, [Fonction sommatoire de la fonction de Moebius. 2. Majorations asymptotiques élémentaires][24], Experiment. Math. 2(2) (1993), 99-112.

Mohamed El-Marraki, [Fonction sommatoire de la fonction mu de Möbius, 3. Majorations asymptotiques effectives fortes][25], Journal de théorie des nombres de Bordeaux 7(2) (1995), 407-433.

Brady Haran, Holly Krieger, and Pete McPartlan, [A Prime Surprise (Mertens Conjecture)][26], Numberphile video (2019).

Harald A. Helfgott and Lola Thompson, [Summing mu(n): a faster elementary algorithm][27], arXiv:2101.08773 [math.NT], 2021.

Greg Hurst, [Computations of the Mertens function and improved bounds on the Mertens conjecture][28], arXiv:1610.08551 [math.NT], 2016-2017.

MathOverflow, [Is Mertens function negatively biased?][29], posted May 28, 2012.

MathOverflow, [Approximations to the Mertens function][30], posted Jul 08 2015.

Nathan Ng, [The distribution of the summatory function of the Möbius function][31], Proc. London Math. Soc. (3) 89 (2004), no. 2, 361-389; arXiv:math/0310381 [math.NT], 2003.

Andrew M. Odlyzko and H. J. J. te Riele, [Disproof of the Mertens conjecture][32], J. reine angew. Math., 357 (1985), 138-160.

Maxie Dion Schmidt, [Picking up the partial sums of the Möbius function problem with probabilistic number theory][33], arXiv:2604.23517 [math.NT], 2026. See p. 1 (Def. 1.2).

Lowell Schoenfeld, [An improved estimate for the summatory function of the Möbius function][34], Acta Arithmetica 15(3) (1969), 221-233.

Kannan Soundararajan, [Partial sums of the Möbius function][35], Journal für die reine und angewandte Mathematik, Vol. 631 (2009), 141-152. arXiv:0705.0723 [math.NT], 2007-2008.

Robert Daublebsky von Sterneck, [Empirische Untersuchung ueber den Verlauf der zahlentheoretischer Function sigma(n) = Sum_{x=1..n} mu(x) im Intervalle von 0 bis 150 000][36], Sitzungsbericht der Kaiserlichen Akademie der Wissenschaften Wien, Mathematisch-Naturwissenschaftlichen Klasse, 2a, v. 106 (1897), 835-1024.

Robert Daublebsky von Sterneck, [Bemerkung über die Summierung einiger zahlen-theoretischen Functionen][37], Monatshefte für Mathematik und Physik 9(1) (1898), 43-45. [He proves the inequality |a(n)| <= (n/9) + 8.]

Paul Tarau, [Towards a generic view of primality through multiset decompositions of natural numbers][38], Theor. Comp. Sci. 537 (Jun 05 2014), 105-124.

Paul Tarau, [Emulating Primality with Multiset Representations of Natural Numbers][39], in Theor. Aspects Comput., (ICTAC 2011) Lect. Notes Comp. Sci. 6916/2011, 218-238.

Gerard Villemin's Almanac of Numbers, [Nombres de Moebius et de Mertens][40].

Eric Weisstein's World of Mathematics, [Mertens Function][41].

Eric Weisstein's World of Mathematics, [Redheffer Matrix][42].

Wikipedia, [Mertens function][43].

H. S. Wilf, [A Greeting; and a view of Riemann's Hypothesis][44], Amer. Math. Monthly, 94:1 (1987), 3-6.

FORMULA

Assuming the Riemann hypothesis, a(n) = O(x^(1/2 + eps)) for every eps > 0 (Littlewood - see Landau p. 161).

Lambert series: Sum_{n >= 1} a(n)*(x^n/(1-x^n)-x^(n+1)/(1-x^(n+1))) = x and -1/x. - [Mats Granvik][45], Sep 09 2010 and Sep 23 2010

a(n)+2 = [A192763][46] (n,1) for n>1, and [A192763][46] (1,k) for k>1 (conjecture). - [Mats Granvik][45], Jul 10 2011

Sum_{k = 1..n} a(floor(n/k)) = 1. - [David W. Wilson][47], Feb 27 2012

a(n) = Sum_{k = 1..n} tau_{-2}(k) * floor(n/k), where tau_{-2} is [A007427][48]. - [Enrique Pérez Herrero][49], Jan 23 2013

a(n) = Sum_{k=1.. [A002088][50] (n)} exp(2*Pi*i*[A038566][51] (k)/ [A038567][52] (k-1)) where i is the imaginary unit. - [Eric Desbiaux][53], Jul 31 2014

Schoenfeld proves that |a(n)| < 5.3*n/(log n)^(10/9) for n > 1. - [Charles R Greathouse IV][15], Jan 17 2018

G.f. A(x) satisfies: A(x) = (1/(1 - x)) * (x - Sum_{k>=2} (1 - x^k) * A(x^k)). - [Ilya Gutkovskiy][54], Aug 11 2021

EXAMPLE

G.f. = x - x^3 - x^4 - 2*x^5 - x^6 - 2*x^7 - 2*x^8 - 2*x^9 - x^10 - 2*x^11 - 2*x^12 - ...

MAPLE

with(numtheory); [A002321][55]:= n->add(mobius(k), k=1..n);

MATHEMATICA

Rest[ FoldList[ #1+#2&, 0, Array[ MoebiusMu, 100 ] ] ]

(* Alternative: *)

Accumulate[Array[MoebiusMu, 100]] (* [Harvey P. Dale][56], May 11 2011 *)

PROG

(PARI) a(n) = sum( k=1, n, moebius(k))

(PARI) a(n) = if( n<1, 0, matdet( matrix(n, n, i, j, j==1 || 0==j%i)))

(PARI) a(n)=my(s); forsquarefree(k=1, n, s+=moebius(k)); s \\ [Charles R Greathouse IV][15], Jan 08 2018

(Haskell)

import Data.List (genericIndex)

a002321 n = genericIndex a002321_list (n-1)

a002321_list = scanl1 (+) a008683_list

-- [Reinhard Zumkeller][57], Jul 14 2014, Dec 26 2012

(Python)

from sympy import mobius

def M(n): return sum(mobius(k) for k in range(1, n + 1))

print([M(n) for n in range(1, 151)]) # [Indranil Ghosh][58], Mar 18 2017

(Python)

from functools import lru_cache

@lru_cache(maxsize=None)

def [A002321][55] (n):

if n == 0:

return 0

c, j = n, 2

k1 = n//j

while k1 > 1:

j2 = n//k1 + 1

c += (j2-j)*[A002321][55] (k1)

j, k1 = j2, n//j2

return j-c # [Chai Wah Wu][59], Mar 30 2021

(Magma) [&+[MoebiusMu(k): k in [1..n]]: n in [1..81]]; // [Bruno Berselli][60], Jul 12 2021

CROSSREFS

Cf. [A008683][4], [A059571][61], [A084237][62], [A209802][63].

First column of [A134541][64].

First column of [A179287][65].

Sequence in context: [A145866][66] [A103318][67] [A197775][68] * [A043530][69] [A297771][70] [A164995][71]

Adjacent sequences: [A002318][72] [A002319][73] [A002320][74] * [A002322][75] [A002323][76] [A002324][77]

KEYWORD

sign, easy, nice

AUTHOR

[N. J. A. Sloane][78]

STATUS

approved

[Lookup][3] [Welcome][79] [Wiki][80] [Register][81] [Music][82] [Plot 2][83] [Demos][84] [Index][85] [WebCam][86] [Contribute][87] [Format][88] [Style Sheet][89] [Transforms][90] [Superseeker][91] [Recents][92]

[The OEIS Community][93]

Maintained by [The OEIS Foundation Inc.][94]

Last modified August 14 12:19 EDT 2026. Contains 398312 sequences.

[License Agreements, Terms of Use, Privacy Policy][95]


## Links

[1]: /login?redirect=%2fA002321
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A008683
[5]: /A002321/list
[6]: /A002321/graph
[7]: /search?q=A002321+-id:A002321
[8]: /A002321/listen
[9]: /history?seq=A002321
[10]: /search?q=id:A002321&fmt=text
[11]: /A002321/internal
[12]: /A156749
[13]: /A156709
[14]: /wiki/User:Daniel_Forgues
[15]: /wiki/User:Charles_R_Greathouse_IV
[16]: /A002321/b002321.txt
[17]: https://arxiv.org/pdf/0812.1689
[18]: https://web.archive.org/web/20110810105334/http://mertens.redgolpe.com/
[19]: https://cs.uwaterloo.ca/journals/JIS/VOL18/Bordelles2/bordelles21.html
[20]: https://arxiv.org/pdf/math/0306042
[21]: https://www.ams.org/notices/200303/fea-conrey-web.pdf
[22]: http://projecteuclid.org/euclid.em/1047565447
[23]: https://projecteuclid.org/euclid.em/1048516214
[24]: https://projecteuclid.org/euclid.em/1048516215
[25]: https://www.numdam.org/item/JTNB_1995__7_2_407_0/
[26]: https://www.youtube.com/watch?v=uvMGZb0Suyc
[27]: https://arxiv.org/pdf/2101.08773
[28]: https://arxiv.org/pdf/1610.08551
[29]: http://mathoverflow.net/questions/98174
[30]: http://mathoverflow.net/questions/211095
[31]: https://arxiv.org/pdf/math/0310381
[32]: https://www-users.cse.umn.edu/~odlyzko/doc/zeta.html
[33]: https://arxiv.org/pdf/2604.23517
[34]: https://eudml.org/doc/204893
[35]: https://arxiv.org/pdf/0705.0723
[36]: https://www.zobodat.at/pdf/SBAWW_106_2a_0835-1024.pdf
[37]: https://doi.org/10.1007/BF01707854
[38]: https://doi.org/10.1016/j.tcs.2014.04.025
[39]: https://doi.org/10.1007/978-3-642-23283-1_15
[40]: https://web.archive.org/web/20250214012221/http://villemin.gerard.free.fr/TABLES/aaaFArit/MobiusMe.htm
[41]: https://mathworld.wolfram.com/MertensFunction.html
[42]: https://mathworld.wolfram.com/RedhefferMatrix.html
[43]: https://en.wikipedia.org/wiki/Mertens_function
[44]: https://www.jstor.org/stable/2323497
[45]: /wiki/User:Mats_Granvik
[46]: /A192763
[47]: /wiki/User:David_W._Wilson
[48]: /A007427
[49]: /wiki/User:Enrique_Pérez_Herrero
[50]: /A002088
[51]: /A038566
[52]: /A038567
[53]: /wiki/User:Eric_Desbiaux
[54]: /wiki/User:Ilya_Gutkovskiy
[55]: /A002321
[56]: /wiki/User:Harvey_P._Dale
[57]: /wiki/User:Reinhard_Zumkeller
[58]: /wiki/User:Indranil_Ghosh
[59]: /wiki/User:Chai_Wah_Wu
[60]: /wiki/User:Bruno_Berselli
[61]: /A059571
[62]: /A084237
[63]: /A209802
[64]: /A134541
[65]: /A179287
[66]: /A145866
[67]: /A103318
[68]: /A197775
[69]: /A043530
[70]: /A297771
[71]: /A164995
[72]: /A002318
[73]: /A002319
[74]: /A002320
[75]: /A002322
[76]: /A002323
[77]: /A002324
[78]: /wiki/User:N._J._A._Sloane
[79]: /wiki/Welcome
[80]: /wiki/Main_Page
[81]: /wiki/Special:RequestAccount
[82]: /play.html
[83]: /plot2.html
[84]: /demo1.html
[85]: /wiki/Index_to_OEIS
[86]: /webcam
[87]: /Submit.html
[88]: /eishelp2.html
[89]: /wiki/Style_Sheet
[90]: /transforms.html
[91]: /ol.html
[92]: /recent
[93]: /community.html
[94]: http://oeisf.org
[95]: /wiki/Legal_Documents
