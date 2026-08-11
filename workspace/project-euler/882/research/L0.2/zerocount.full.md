<!-- source: https://oeis.org/A059015 | converted from HTML -->

A059015 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A059015 - OEIS] [3]

A059015

Total number of 0's in binary expansions of 0, ..., n.

48

1, 1, 2, 2, 4, 5, 6, 6, 9, 11, 13, 14, 16, 17, 18, 18, 22, 25, 28, 30, 33, 35, 37, 38, 41, 43, 45, 46, 48, 49, 50, 50, 55, 59, 63, 66, 70, 73, 76, 78, 82, 85, 88, 90, 93, 95, 97, 98, 102, 105, 108, 110, 113, 115, 117, 118, 121, 123, 125, 126, 128, 129, 130, 130, 136, 141

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

0,3

COMMENTS

Partial sums of [A023416][11]. - [Reinhard Zumkeller][12], Jul 15 2011

The graph of this sequence is a version of the Takagi curve: see Lagarias (2012), Section 9, especially Theorem 9.1. - [N. J. A. Sloane][13], Mar 12 2016

LINKS

T. D. Noe and Hieronymus Fischer, [Table of n, a(n) for n = 0..10000][14] (terms up to n=1023 by T. D. Noe)

Hsien-Kuei Hwang, S. Janson, and T.-H. Tsai, [Exact and asymptotic solutions of the recurrence f(n) = f(floor(n/2)) + f(ceiling(n/2)) + g(n): theory and applications][15], Preprint 2016.

Hsien-Kuei Hwang, S. Janson, and T.-H. Tsai, [Exact and Asymptotic Solutions of a Divide-and-Conquer Recurrence Dividing at Half: Theory and Applications][16], ACM Transactions on Algorithms, 13:4 (2017), #47; DOI: 10.1145/3127585.

Jeffrey C. Lagarias, [The Takagi function and its properties][17], arXiv:1112.4205 [math.CA], 2011-2012.

Jeffrey C. Lagarias, [The Takagi function and its properties][18], In Functions in number theory and their probabilistic aspects, 153--189, RIMS Kôkyûroku Bessatsu, B34, Res. Inst. Math. Sci. (RIMS), Kyoto, 2012. MR3014845.

Ralf Stephan, [Some divide-and-conquer sequences ...][19]

Ralf Stephan, [Table of generating functions][20]

[Index entries for sequences related to binary expansion of n][21]

FORMULA

a(n) = b(n)+1, with b(2n) = b(n)+b(n-1)+n, b(2n+1) = 2b(n)+n. - [Ralf Stephan][22], Sep 13 2003

From [Hieronymus Fischer][23], Jun 10 2012: (Start)

With m = floor(log_2(n)):

a(n) = 2 + (m+1)*(n+1) - 2^(m+1) + (1/2)*Sum_{j=1..m+1} (floor(n/2^j)*(2*n + 2 - (1 + floor(n/2^j))*2^j) - floor(n/2^j + 1/2)*(2*n + 2 - floor(n/2^j + 1/2)*2^j)).

a(n) = [A083652][24] (n) - (n+1)*[A000120][25] (n) + 2^(m-1) - (1/4) + (1/2)*sum_{j=1..m+1} (floor(n/2^j + 1/2)^2 - (floor(n/2^j) + 1/2)^2)*2^j.

a(2^m-1) = 2 + (m-2)*2^(m-1)

(this is the total number of zero digits occurring in all the numbers with <= m places).

G.f.: 1/(1 - x) + (1/(1 - x)^2)*Sum_{j>=0} x^(2*2^j)/(1 + x^(2^j)); corrected by [Ilya Gutkovskiy][26], Mar 28 2018

General formulas for the number of digits <= d in the base p representations of all integers from 0 to n, where 0 <= d < p.

With m = floor(log_p(n)):

a(n) = 1 + (m+1)*(n+1) - (p^(m+1)-1)/(p-1) + (1/2)*sum_{j=1..m+1} (floor(n/p^j)*(2n + 2 - (1 + floor(n/p^j))*p^j) - floor(n/p^j + (p-d-1)/p)*(2n + 2 + ((p-2*d-2)/p - floor(n/p^j + (p-d-1)/p))*p^j)).

a(n) = H(n,p) - (n+1)*F(n,p,d+1) + (1/2)*sum_{j=1..m+1} ((floor(n/p^j + (p-d-1)/p)^2 - floor(n/p^j)^2)*p^j - (((p - 2*d-2)/p)*floor(n/p^j + (p-d-1)/p) + floor(n/p^j))*p^j), where H(n,p) = sum of number of digits in the base p representations of 0 to n and F(n,p,d) = number of digits >=d in the base p representation of n.

a(p^m-1) = 1 + (d+1)*m*p^(m-1) - (p^m-1)/(p-1).

(this is the total number of digits <= d occurring in all the numbers with <= m places in base p representation).

G.f.: 1/(1-x) + (1/(1-x)^2)*Sum_{j>=0} ((1-x^(d*p^j))*x^p^j + (1-x^p^j)*x^p^(j+1)/(1-x^p^(j+1))). (End)

a(n) = [A083652][24] (n) - [A000788][27] (n). - [Alan Michael Gómez Calderón][28], Sep 25 2025

MAPLE

a:= proc(n) option remember; `if`(n=0, 1, a(n-1)+add(1-i, i=Bits[Split](n))) end:

seq(a(n), n=0..65); # [Alois P. Heinz][29], Nov 11 2024

MATHEMATICA

Accumulate[ Table[ Count[ IntegerDigits[n, 2], 0], {n, 0, 65}]] (* [Jean-François Alcover][30], Oct 03 2012 *)

Accumulate[DigitCount[Range[0, 70], 2, 0]] (* [Harvey P. Dale][31], Jun 24 2017 *)

PROG

(Haskell)

a059015 n = a059015_list !! n

a059015_list = scanl1 (+) $ map a023416 [0..]

-- [Reinhard Zumkeller][12], Jul 15 2011

(PARI) v=vector(100, i, 1); for(i=1, #v-1, v[i+1] = v[i] + #binary(i) - hammingweight(i)); v \\ [Charles R Greathouse IV][32], Nov 20 2012

(PARI) a(n)=if(n, my(m=logint(n, 2)); 2 + (m+1)*(n+1) - 2^(m+1) + sum(j=1, m+1, my(t=floor(n/2^j + 1/2)); (n>>j)*(2*n + 2 - (1 + (n>>j))<<j) - (2*n + 2 - t<<j)*t)/2, 1) \\ [Charles R Greathouse IV][32], Dec 14 2015

(Python)

def [A059015][33] (n): return 2+(n+1)*(m:=(n+1).bit_length())-(1<<m)-sum(i.bit_count() for i in range(1, n+1)) # [Chai Wah Wu][34], Mar 01 2023

(Python)

def [A059015][33] (n): return 2+(n+1)*((t:=(n+1).bit_length())-n.bit_count())-(1<<t)-(sum((m:=1<<j)*((k:=n>>j)-(r if n<<1>=m*(r:=k<<1|1) else 0)) for j in range(1, n.bit_length()+1))>>1) # [Chai Wah Wu][34], Nov 11 2024

CROSSREFS

The basic sequences concerning the binary expansion of n are [A000120][25], [A000788][27], [A000069][35], [A001969][36], [A023416][11], [A059015][33], [A070939][37], [A083652][24].

Cf. [A055640][38], [A055641][39], [A102669][40] - [A102685][41], [A117804][42], [A122840][43], [A122841][44], [A160093][45], [A160094][46], [A196563][47], [A196564][48] (for base 10).

Sequence in context: [A338228][49] [A351782][50] [A064574][51] * [A325108][52] [A329474][53] [A260295][54]

Adjacent sequences: [A059012][55] [A059013][56] [A059014][57] * [A059016][58] [A059017][59] [A059018][60]

KEYWORD

nonn, easy, nice

AUTHOR

[Patrick De Geest][61], Dec 15 2000

STATUS

approved

[Lookup][3] [Welcome][62] [Wiki][63] [Register][64] [Music][65] [Plot 2][66] [Demos][67] [Index][68] [WebCam][69] [Contribute][70] [Format][71] [Style Sheet][72] [Transforms][73] [Superseeker][74] [Recents][75]

[The OEIS Community][76]

Maintained by [The OEIS Foundation Inc.][77]

Last modified August 11 09:33 EDT 2026. Contains 398211 sequences.

[License Agreements, Terms of Use, Privacy Policy][78]


## Links

[1]: /login?redirect=%2fA059015
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A059015/list
[5]: /A059015/graph
[6]: /search?q=A059015+-id:A059015
[7]: /A059015/listen
[8]: /history?seq=A059015
[9]: /search?q=id:A059015&fmt=text
[10]: /A059015/internal
[11]: /A023416
[12]: /wiki/User:Reinhard_Zumkeller
[13]: /wiki/User:N._J._A._Sloane
[14]: /A059015/b059015.txt
[15]: https://algo.stat.sinica.edu.tw/hk/files/2016/12/aat-hhrr-1.pdf
[16]: https://doi.org/10.1145/3127585
[17]: https://arxiv.org/abs/1112.4205
[18]: http://hdl.handle.net/2433/198081
[19]: /somedcgf.html
[20]: /A079944/a079944.ps
[21]: /index/Bi#binary
[22]: /wiki/User:Ralf_Stephan
[23]: /wiki/User:Hieronymus_Fischer
[24]: /A083652
[25]: /A000120
[26]: /wiki/User:Ilya_Gutkovskiy
[27]: /A000788
[28]: /wiki/User:Alan_Michael_Gómez_Calderón
[29]: /wiki/User:Alois_P._Heinz
[30]: /wiki/User:Jean-François_Alcover
[31]: /wiki/User:Harvey_P._Dale
[32]: /wiki/User:Charles_R_Greathouse_IV
[33]: /A059015
[34]: /wiki/User:Chai_Wah_Wu
[35]: /A000069
[36]: /A001969
[37]: /A070939
[38]: /A055640
[39]: /A055641
[40]: /A102669
[41]: /A102685
[42]: /A117804
[43]: /A122840
[44]: /A122841
[45]: /A160093
[46]: /A160094
[47]: /A196563
[48]: /A196564
[49]: /A338228
[50]: /A351782
[51]: /A064574
[52]: /A325108
[53]: /A329474
[54]: /A260295
[55]: /A059012
[56]: /A059013
[57]: /A059014
[58]: /A059016
[59]: /A059017
[60]: /A059018
[61]: /wiki/User:Patrick_De_Geest
[62]: /wiki/Welcome
[63]: /wiki/Main_Page
[64]: /wiki/Special:RequestAccount
[65]: /play.html
[66]: /plot2.html
[67]: /demo1.html
[68]: /wiki/Index_to_OEIS
[69]: /webcam
[70]: /Submit.html
[71]: /eishelp2.html
[72]: /wiki/Style_Sheet
[73]: /transforms.html
[74]: /ol.html
[75]: /recent
[76]: /community.html
[77]: http://oeisf.org
[78]: /wiki/Legal_Documents
