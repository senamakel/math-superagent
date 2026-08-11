<!-- source: https://oeis.org/A000788 | converted from HTML -->

A000788 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A000788 - OEIS] [3]

A000788

Total number of 1's in binary expansions of 0, ..., n.
(Formerly M0964 N0360)

84

0, 1, 2, 4, 5, 7, 9, 12, 13, 15, 17, 20, 22, 25, 28, 32, 33, 35, 37, 40, 42, 45, 48, 52, 54, 57, 60, 64, 67, 71, 75, 80, 81, 83, 85, 88, 90, 93, 96, 100, 102, 105, 108, 112, 115, 119, 123, 128, 130, 133, 136, 140, 143, 147, 151, 156, 159, 163, 167, 172, 176, 181, 186

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

0,3

COMMENTS

Partial sums of [A000120][11].

The graph of this sequence is a version of the Takagi curve: see Lagarias (2012), Section 9, especially Theorem 9.1. - [N. J. A. Sloane][12], Mar 12 2016

a(n-1) is the largest possible number of ordered pairs (a,b) such that a/b is a prime in a subset of the positive integers with n elements. - [Yifan Xie][13], Feb 21 2025

REFERENCES

J.-P. Allouche & J. Shallit, Automatic sequences, Cambridge University Press, 2003, p. 94

R. Bellman and H. N. Shapiro, On a problem in additive number theory, Annals Math., 49 (1948), 333-340. See Eq. 1.9. [From [N. J. A. Sloane][12], Mar 12 2009]

L. E. Bush, An asymptotic formula for the average sums of the digits of integers, Amer. Math. Monthly, 47 (1940), pp. 154-156. [From the bibliography of Stolarsky, 1977]

P. Cheo and S. Yien, A problem on the k-adic representation of positive integers (Chinese; English summary), Acta Math. Sinica, 5 (1955), pp. 433-438. [From the bibliography of Stolarsky, 1977]

M. P. Drazin and J. S. Griffith, On the decimal representation of integers, Proc. Cambridge Philos. Soc., (4), 48 (1952), pp. 555-565. [From the bibliography of Stolarsky, 1977]

E. N. Gilbert, Games of identification or convergence, SIAM Review, 4 (1962), 16-24.

P. J. Grabner, P. Kirschenhofer, H. Prodinger and R. F. Tichy, On the moments of the sum-of-digits function. Applications of Fibonacci numbers, Vol. 5 (St. Andrews, 1992), 263-271, Kluwer Acad. Publ., Dordrecht, 1993.

R. L. Graham, On primitive graphs and optimal vertex assignments, pp. 170-186 of Internat. Conf. Combin. Math. (New York, 1970), Annals of the NY Academy of Sciences, Vol. 175, 1970.

E. Grosswald, Properties of some arithmetic functions, J. Math. Anal. Appl., 28 (1969), pp.405-430.

Donald E. Knuth, The Art of Computer Programming, volume 3 Sorting and Searching, section 5.3.4, subsection Bitonic sorting, with C'(p) = a(p-1).

Hiu-Fai Law, Spanning tree congestion of the hypercube, Discrete Math., 309 (2009), 6644-6648 (see p(m) on page 6647).

Z. Li and E. M. Reingold, Solution of a divide-and-conquer maximin recurrence, SIAM J. Comput., 18 (1989), 1188-1200.

Mauclaire, J.-L.; Murata, Leo; On q-additive functions. I. Proc. Japan Acad. Ser. A Math. Sci. 59 (1983), no. 6, 274-276.

Mauclaire, J.-L.; Murata, Leo; On q-additive functions. II. Proc. Japan Acad. Ser. A Math. Sci. 59 (1983), no. 9, 441-444.

M. D. McIlroy, The number of 1's in binary integers: bounds and extremal properties, SIAM J. Comput., 3 (1974), 255-261.

L. Mirsky, A theorem on representations of integers in the scale of r, Scripta Math., 15 (1949), pp. 11-12.

I. Shiokawa, On a problem in additive number theory, Math. J. Okayama Univ., 16 (1974), pp.167-176. [From the bibliography of Stolarsky, 1977]

N. J. A. Sloane, A Handbook of Integer Sequences, Academic Press, 1973 (includes this sequence).

N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

K. B. Stolarsky, Power and exponential sums of digital sums related to binomial coefficient parity, SIAM J. Appl. Math., 32 (1977), 717-730.

J. R. Trollope, An explicit expression for binary digital sums. Math. Mag. 41 1968 21-25.

LINKS

T. D. Noe and Hieronymus Fischer, [Table of n, a(n) for n = 0..10000][14] (terms up to n=1000 by T. D. Noe).

Geir Agnarsson, [On the number of hypercubic bipartitions of an integer][15], arXiv preprint arXiv:1106.4997 [math.CO], 2011.

Geir Agnarsson, [Induced subgraphs of hypercubes][16], arXiv preprint arXiv:1112.3015 [math.CO], 2011.

Geir Agnarsson and Kshitij Lauria, [Extremal subgraphs of the d-dimensional grid graph][17], arXiv preprint arXiv:1302.6517 [math.CO], 2013.

Jean-Paul Allouche, [On an Inequality in a 1970 Paper of R. L. Graham][18], INTEGERS 21A (2021), #A2.

Mathias Hauan Arbo, Esten Ingar Grøtli, and Jan Tommy Gravdahl, [CASCLIK: CasADi-Based Closed-Loop Inverse Kinematics][19], arXiv:1901.06713 [cs.RO], 2019.

Venkata Sai Narayana Bavisetty, Matthew Wheeler, Reinhard Laubenbacher, and Claus Kadelka, [Upper bound for the stability of Boolean networks][20], arXiv:2506.12310 [q-bio.MN], 2025. See p. 8.

Johann Cigler, [A curious class of Hankel determinants][21], arXiv:1803.05164 [math.CO], 2018.

G. F. Clements and B. Lindström, [A sequence of (+-1) determinants with large values][22], Proc. Amer. Math. Soc., 16 (1965), pp. 548-550. [From the bibliography of Stolarsky, 1977]

Jean Coquet, [Power sums of digital sums][23], J. Number Theory 22 (1986), no. 2, 161-176.

Hubert Delange, [Sur la fonction sommatoire de la fonction "somme des chiffres"][24], Enseignement Math., (2), 21 (1975), pp. 31-47. [From the bibliography of Stolarsky, 1977]

Laurent Feuilloley, [Brief Announcement: Average Complexity for the LOCAL Model][25], arXiv preprint arXiv:1505.05072 [cs.DC], 2015.

Steven Finch, Pascal Sebah, and Zai-Qiao Bai, [Odd Entries in Pascal's Trinomial Triangle][26], arXiv:0802.2654 [math.NT], 2008.

Oscar E. González, [An observation of Rankin on Hankel determinants][27], Department of Mathematics, University of Illinois at Urbana-Champaign, 2018.

P. J. Grabner and H.-K. Hwang, [Digital sums and divide-and-conquer recurrences: Fourier expansions and absolute convergence][28]

Milton W. Green, [Letter to N. J. A. Sloane, 1973][29] (note "A360" refers to N0360 which is the present sequence).

Hsien-Kuei Hwang, S. Janson, and T.-H. Tsai, [Exact and asymptotic solutions of the recurrence f(n) = f(floor(n/2)) + f(ceiling(n/2)) + g(n): theory and applications][30], Preprint 2016.

Hsien-Kuei Hwang, S. Janson, and T.-H. Tsai, [Exact and Asymptotic Solutions of a Divide-and-Conquer Recurrence Dividing at Half: Theory and Applications][31], ACM Transactions on Algorithms, 13:4 (2017), #47; DOI: 10.1145/3127585.

Hsien-Kuei Hwang, Svante Janson, and Tsung-Hsi Tsai, [Identities and periodic oscillations of divide-and-conquer recurrences splitting at half][32], arXiv:2210.10968 [cs.DS], 2022, p. 36 and 44.

Linda Knüver and Mareike Fischer, [Revealing the building blocks of tree balance: fundamental units of the Sackin and Colless Indices][33], arXiv:2509.04995 [q-bio.PE], 2025. See p. 25.

Jeffrey C. Lagarias, [The Takagi function and its properties][34], arXiv:1112.4205 [math.CA], 2011-2012.

Jeffrey C. Lagarias, [The Takagi function and its properties][35], In Functions in number theory and their probabilistic aspects, 153--189, RIMS Kôkyûroku Bessatsu, B34, Res. Inst. Math. Sci. (RIMS), Kyoto, 2012. MR3014845.

Julien Leroy, Michel Rigo, and Manon Stipulanti, [Behavior of Digital Sequences Through Exotic Numeration Systems][36], Electronic Journal of Combinatorics 24(1) (2017), #P1.44.

B. Lindström, [On a combinatorial problem in number theory][37], Canad. Math. Bull., 8 (1965), 477-490.

Raoul Nakhmanson-Kulish, [Graphic representation of K(n)=a(n)/(n log2(n)/2) from n=63 to 131071][38]

D. J. Newman, [On the number of binary digits in a multiple of three][39], Proc. Amer. Math. Soc., 21 (1969), pp. 719-721. [From the bibliography of Stolarsky, 1977]

Ralf Stephan, [Some divide-and-conquer sequences ...][40]

Ralf Stephan, [Table of generating functions][41]

S. C. Tang, [An improvement and generalization of Bellman-Shapiro's theorem on a problem in additive number theory][42], Proc. Amer. Math. Soc., 14 (1963), pp. 199-204. [From the bibliography of Stolarsky, 1977]

Eric Weisstein's World of Mathematics, [Binary][43]

David W. Wilson, [Fast C++ function for computing a(n)][44]

[Index entries for sequences related to binary expansion of n][45]

FORMULA

McIlroy (1974) gives bounds and recurrences. - [N. J. A. Sloane][12], Mar 24 2014

Stolarsky (1977) studies the asymptotics, and gives at least nine references to earlier work on the problem. I have added all the references that were not here already. - [N. J. A. Sloane][12], Apr 06 2014

a(n) = Sum_{k=1..n} [A000120][11] (k). - [Benoit Cloitre][46], Dec 19 2002

a(0) = 0, a(2n) = a(n)+a(n-1)+n, a(2n+1) = 2a(n)+n+1. - [Ralf Stephan][47], Sep 13 2003

a(n) = n*log_2(n)/2 + O(n); a(2^n)=n*2^(n-1)+1. - [Benoit Cloitre][46], Sep 25 2003 (The first result is due to Bellman and Shapiro, - [N. J. A. Sloane][12], Mar 24 2014)

a(n) = n*log_2(n)/2+n*F(log_2(n)) where F is a nowhere differentiable continuous function of period 1 (see Allouche & Shallit). - [Benoit Cloitre][46], Jun 08 2004

G.f.: (1/(1-x)^2) * Sum_{k>=0} x^2^k/(1+x^2^k). - [Ralf Stephan][47], Apr 19 2003

a(2^n-1) = [A001787][48] (n) = n*2^(n-1). - [M. F. Hasler][49], Nov 22 2009

a(4^n-2) = n(4^n-2).

For real n, let f(n) = [n]/2 if [n] even, n-[n+1]/2 otherwise. Then a(n) = Sum_{k>=0} 2^k*f((n+1)/2^k).

a( [A000225][50] (n)) = [A173921][51] ( [A000225][50] (n)) = [A001787][48] (n); a( [A000079][52] (n)) = [A005183][53] (n). - [Reinhard Zumkeller][54], Mar 04 2010

From [Hieronymus Fischer][55], Jun 10 2012: (Start)

a(n) = (1/2)*Sum_{j=1..m+1} (floor(n/2^j + 1/2)*(2n + 2 - floor(n/2^j + 1/2))*2^j - floor(n/2^j)*(2n + 2 - (1 + floor(n/2^j)) * 2^j)), where m=floor(log_2(n)).

a(n) = (n+1)*[A000120][11] (n) - 2^(m-1) + 1/4 + (1/2)*Sum_{j=1..m+1} ((floor(n/2^j) + 1/2)^2 - floor(n/2^j + 1/2)^2)*2^j, where m=floor(log_2(n)).

a(2^m-1) = m*2^(m-1).

(This is the total number of '1' digits occurring in all the numbers with <= m bits.)

Generic formulas for the number of digits >= d in the base p representations of all integers from 0 to n, where 1<= d < p.

a(n) = (1/2)*Sum_{j=1..m+1} (floor(n/p^j + (p-d)/p)*(2n + 2 + ((p-2*d)/p - floor(n/p^j + (p-d)/p))*p^j) - floor(n/p^j)*(2n + 2 - (1+floor(n/p^j)) * p^j)), where m=floor(log_p(n)).

a(n) = (n+1)*F(n,p,d) + (1/2)*Sum_{j=1..m+1} ((((p-2*d)/p)*floor(n/p^j+(p-d)/p) + floor(n/p^j))*p^j - (floor(n/p^j+(p-d)/p)^2 - floor(n/p^j)^2)*p^j), where m=floor(log_p(n)) and F(n,p,d) = number of digits >= d in the base p representation of n.

a(p^m-1) = (p-d)*m*p^(m-1).

(This is the total number of digits >= d occurring in all the numbers with <= m digits in base p representation.)

G.f.: g(x) = (1/(1-x)^2)*Sum_{j>=0} (x^(d*p^j) - x^(p*p^j))/(1-x^(p*p^j)). (End)

a(n) = Sum_{k=1..n} [A000120][11] ( [A240857][56] (n,k)). - [Reinhard Zumkeller][54], Apr 14 2014

For n > 0, if n is written as 2^m + r with 0 <= r < 2^m, then a(n) = m*2^(m-1) + r + 1 + a(r). - [Shreevatsa R][57], Mar 20 2018

a(n) = n*(n+1)/2 + Sum_{k=1..floor(n/2)} ((2k-1)((g(n,k)-1)*2^(g(n,k) + 1) + 2) - (n+1)*(g(n,k)+1)*g(n,k)/2), where g(n,k) = floor(log_2(n/(2k-1))). - [Fabio Visonà][58], Mar 17 2020

From [Jeffrey Shallit][59], Aug 07 2021: (Start)

A 2-regular sequence, satisfying the identities

a(4n+1) = -a(2n) + a(2n+1) + a(4n)

a(4n+2) = -2a(2n) + 2a(2n+1) + a(4n)

a(4n+3) = -4a(n) + 4a(2n+1)

a(8n) = 4a(n) - 8a(2n) + 5a(4n)

a(8n+4) = -9a(2n) + 5a(2n+1) + 4a(4n)

for n>=0. (End)

a(n) = Sum_{k=0..floor(log_2(n+1))} k * [A360189][60] (n,k). - [Alois P. Heinz][61], Mar 06 2023

a(n) = [A083741][62] (n+1) + [A136013][63] (n+1). - [Alan Michael Gómez Calderón][64], Sep 23 2025

MAPLE

a:= proc(n) option remember; `if`(n=0, 0, a(n-1)+add(i, i=Bits[Split](n))) end:

seq(a(n), n=0..62); # [Alois P. Heinz][61], Nov 11 2024

MATHEMATICA

a[n_] := Count[ Table[ IntegerDigits[k, 2], {k, 0, n}], 1, 2]; Table[a[n], {n, 0, 62}] (* [Jean-François Alcover][65], Dec 16 2011 *)

(* Alternative: *)

Table[Plus@@Flatten[IntegerDigits[Range[n], 2]], {n, 0, 62}] (* [Alonso del Arte][66], Dec 16 2011 *)

(* Alternative: *)

Accumulate[DigitCount[Range[0, 70], 2, 1]] (* [Harvey P. Dale][67], Jun 08 2013 *)

PROG

(PARI) [A000788][68] (n)={ n<3 && return(n); if( bittest(n, 0) \\

, n+1 == 1<<valuation(n+1, 2) && return(valuation(n+1, 2)*(n+1)/2) \\

; [A000788][68] (n>>1)*2+n>>1+1 \\

, n == 1<<valuation(n, 2) && return(valuation(n, 2)*n/2+1) \\

; [A000788][68] (n>>=1)+ [A000788][68] (n-1)+n )} \\ [M. F. Hasler][49], Nov 22 2009

(PARI) a(n)=sum(k=1, n, hammingweight(k)) \\ [Charles R Greathouse IV][69], Oct 04 2013

(PARI) a(n) = if (n==0, 0, m = logint(n, 2); r = n % 2^m; m*2^(m-1) + r + 1 + a(r)); \\ [Michel Marcus][70], Mar 27 2018

(PARI) a(n)={n++; my(t, i, s); c=n; while(c!=0, i++; c\=2); for(j=1, i, d=(n\2^(i-j))%2; t+=(2^(i-j)*(s*d+d*(i-j)/2)); s+=d); t} \\ [David A. Corneth][71], Nov 26 2024

(C++) /* See [David W. Wilson][72] link. */

(Haskell) a000788_list = scanl1 (+) [A000120][11] _list

-- [Walt Rorie-Baety][73], Jun 30 2012

(Haskell) {a000788 0 = 0; a00788 n = a000788 n2 + a000788 (n-n2-1) + (n-n2) where n2 = n `div` 2}

-- [Walt Rorie-Baety][73], Jul 15 2012

(Python)

def [A000788][68] (n): return sum(i.bit_count() for i in range(1, n+1)) # [Chai Wah Wu][74], Mar 01 2023

(Python)

def [A000788][68] (n): return (n+1)*n.bit_count()+(sum((m:=1<<j)*((k:=n>>j)-(r if n<<1>=m*(r:=k<<1|1) else 0)) for j in range(1, n.bit_length()+1))>>1) # [Chai Wah Wu][74], Nov 11 2024

CROSSREFS

For number of 0's in binary expansion of 0, ..., n see [A059015][75].

The basic sequences concerning the binary expansion of n are [A000120][11], [A000788][68], [A000069][76], [A001969][77], [A023416][78], [A059015][75], [A070939][79], [A083652][80].

Cf. [A005183][53], [A083741][62], [A136013][63], [A360189][60].

Cf. [A027868][81], [A037123][82], [A054899][83], [A055640][84], [A055641][85], [A102669][86] - [A102685][87], [A117804][88], [A122840][89], [A122841][90], [A160093][91], [A160094][92], [A196563][93], [A196564][94] (for base 10).

Sequence in context: [A140206][95] [A007818][96] [A158618][97] * [A053039][98] [A286753][99] [A325543][100]

Adjacent sequences: [A000785][101] [A000786][102] [A000787][103] * [A000789][104] [A000790][105] [A000791][106]

KEYWORD

nonn, nice, base, easy

AUTHOR

[N. J. A. Sloane][12]

EXTENSIONS

More terms from Larry Reeves (larryr(AT)acm.org), Jan 15 2001

STATUS

approved

[Lookup][3] [Welcome][107] [Wiki][108] [Register][109] [Music][110] [Plot 2][111] [Demos][112] [Index][113] [WebCam][114] [Contribute][115] [Format][116] [Style Sheet][117] [Transforms][118] [Superseeker][119] [Recents][120]

[The OEIS Community][121]

Maintained by [The OEIS Foundation Inc.][122]

Last modified August 11 09:33 EDT 2026. Contains 398211 sequences.

[License Agreements, Terms of Use, Privacy Policy][123]


## Links

[1]: /login?redirect=%2fA000788
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A000788/list
[5]: /A000788/graph
[6]: /search?q=A000788+-id:A000788
[7]: /A000788/listen
[8]: /history?seq=A000788
[9]: /search?q=id:A000788&fmt=text
[10]: /A000788/internal
[11]: /A000120
[12]: /wiki/User:N._J._A._Sloane
[13]: /wiki/User:Yifan_Xie
[14]: /A000788/b000788.txt
[15]: https://arxiv.org/abs/1106.4997
[16]: https://arxiv.org/abs/1112.3015
[17]: https://arxiv.org/abs/1302.6517
[18]: http://math.colgate.edu/~integers/graham2/graham2.Abstract.html
[19]: https://arxiv.org/abs/1901.06713
[20]: https://arxiv.org/abs/2506.12310
[21]: https://arxiv.org/abs/1803.05164
[22]: https://doi.org/10.1090/S0002-9939-1965-0178001-X
[23]: https://doi.org/10.1016/0022-314X(86)90067-3
[24]: https://doi.org/10.5169/seals-47328
[25]: https://arxiv.org/abs/1505.05072
[26]: https://arxiv.org/abs/0802.2654
[27]: https://faculty.math.illinois.edu/~oscareg2/resources/publications/rankinDeterminantsV11.pdf
[28]: http://algo.stat.sinica.edu.tw/
[29]: /A003075/a003075.pdf
[30]: https://algo.stat.sinica.edu.tw/hk/files/2016/12/aat-hhrr-1.pdf
[31]: https://doi.org/10.1145/3127585
[32]: https://arxiv.org/abs/2210.10968
[33]: https://arxiv.org/abs/2509.04995
[34]: https://arxiv.org/abs/1112.4205
[35]: http://hdl.handle.net/2433/198081
[36]: https://doi.org/10.37236/6581
[37]: https://doi.org/10.4153/CMB-1965-034-2
[38]: /A000788/a000788.jpg
[39]: https://doi.org/10.1090/S0002-9939-1969-0244149-8
[40]: /somedcgf.html
[41]: /A079944/a079944.ps
[42]: https://doi.org/10.1090/S0002-9939-1963-0150082-7
[43]: https://mathworld.wolfram.com/Binary.html
[44]: /A000788/a000788.txt
[45]: /index/Bi#binary
[46]: /wiki/User:Benoit_Cloitre
[47]: /wiki/User:Ralf_Stephan
[48]: /A001787
[49]: /wiki/User:M._F._Hasler
[50]: /A000225
[51]: /A173921
[52]: /A000079
[53]: /A005183
[54]: /wiki/User:Reinhard_Zumkeller
[55]: /wiki/User:Hieronymus_Fischer
[56]: /A240857
[57]: /wiki/User:Shreevatsa_R
[58]: /wiki/User:Fabio_Visonà
[59]: /wiki/User:Jeffrey_Shallit
[60]: /A360189
[61]: /wiki/User:Alois_P._Heinz
[62]: /A083741
[63]: /A136013
[64]: /wiki/User:Alan_Michael_Gómez_Calderón
[65]: /wiki/User:Jean-François_Alcover
[66]: /wiki/User:Alonso_del_Arte
[67]: /wiki/User:Harvey_P._Dale
[68]: /A000788
[69]: /wiki/User:Charles_R_Greathouse_IV
[70]: /wiki/User:Michel_Marcus
[71]: /wiki/User:David_A._Corneth
[72]: /wiki/User:David_W._Wilson
[73]: /wiki/User:Walt_Rorie-Baety
[74]: /wiki/User:Chai_Wah_Wu
[75]: /A059015
[76]: /A000069
[77]: /A001969
[78]: /A023416
[79]: /A070939
[80]: /A083652
[81]: /A027868
[82]: /A037123
[83]: /A054899
[84]: /A055640
[85]: /A055641
[86]: /A102669
[87]: /A102685
[88]: /A117804
[89]: /A122840
[90]: /A122841
[91]: /A160093
[92]: /A160094
[93]: /A196563
[94]: /A196564
[95]: /A140206
[96]: /A007818
[97]: /A158618
[98]: /A053039
[99]: /A286753
[100]: /A325543
[101]: /A000785
[102]: /A000786
[103]: /A000787
[104]: /A000789
[105]: /A000790
[106]: /A000791
[107]: /wiki/Welcome
[108]: /wiki/Main_Page
[109]: /wiki/Special:RequestAccount
[110]: /play.html
[111]: /plot2.html
[112]: /demo1.html
[113]: /wiki/Index_to_OEIS
[114]: /webcam
[115]: /Submit.html
[116]: /eishelp2.html
[117]: /wiki/Style_Sheet
[118]: /transforms.html
[119]: /ol.html
[120]: /recent
[121]: /community.html
[122]: http://oeisf.org
[123]: /wiki/Legal_Documents
