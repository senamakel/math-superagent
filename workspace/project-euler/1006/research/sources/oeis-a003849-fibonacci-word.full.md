<!-- source: https://oeis.org/A003849 | converted from HTML -->

A003849 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A003849 - OEIS] [3]

A003849

The infinite Fibonacci word (start with 0, apply 0->01, 1->0, take limit).

228

0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

0,1

COMMENTS

A Sturmian word.

Define strings S(0)=0, S(1)=01, S(n)=S(n-1)S(n-2); iterate; sequence is S(infinity). If the initial 0 is omitted from S(n) for n>0, we obtain [A288582][11] (n+1).

The 0's occur at positions in [A022342][12] (i.e., [A000201][13] - 1), the 1's at positions in [A003622][14].

Replace each run (1;1) with (1;0) in the infinite Fibonacci word [A005614][15] (and add 0 as prefix) [A005614][15] begins: 1,0,1,1,0,1,0,1,1,0,1,1,... changing runs (1,1) with (1,0) produces 1,0,0,1,0,1,0,0,1,0,0,1,... - [Benoit Cloitre][16], Nov 10 2003

Characteristic function of [A003622][14]. - [Philippe Deléham][17], May 03 2004

The fraction of 0's in the first n terms approaches 1/phi (see for example Allouche and Shallit). - [N. J. A. Sloane][18], Sep 24 2007

The limiting mean and variance of the first n terms are 2-phi and 2*phi-3, respectively. - [Clark Kimberling][19], Mar 12 2014, Aug 16 2018

Let S(n) be defined as above. Then this sequence is S(1) + Sum_{n=0..} S(n), where the addition of strings represents concatenation. - [Isaac Saffold][20], May 03 2019

The word is a concatenation of three runs: 0, 1, and 00. The limiting proportions of these are respectively 1 - phi/2, 1/2, and (phi - 1)/2. The mean runlength is (phi + 1)/2. - [Clark Kimberling][19], Dec 26 2010

From [Amiram Eldar][21], Mar 10 2021: (Start)

a(n) is the number of the trailing 0's in the dual Zeckendorf representation of (n+1) ( [A104326][22]).

The asymptotic density of the occurrences of k (0 or 1) is 1/phi^(k+1), where phi is the golden ratio ( [A001622][23]).

The asymptotic mean of this sequence is 1/phi^2 ( [A132338][24]). (End)

REFERENCES

J.-P. Allouche and J. Shallit, Automatic Sequences, Cambridge Univ. Press, 2003.

Jean Berstel, Fibonacci words—a survey, In The book of L, pp. 13-27. Springer Berlin Heidelberg, 1986.

J. C. Lagarias, Number Theory and Dynamical Systems, pp. 35-72 of S. A. Burr, ed., The Unreasonable Effectiveness of Number Theory, Proc. Sympos. Appl. Math., 46 (1992). Amer. Math. Soc. - see p. 64.

Wolfdieter Lang, The Wythoff and the Zeckendorf representations of numbers are equivalent, in G. E. Bergum et al. (edts.) Application of Fibonacci numbers vol. 6, Kluwer, Dordrecht, 1996, pp. 319-337. [See [A317208][25] for a link.]

G. Melançon, Factorizing infinite words using Maple, MapleTech journal, vol. 4, no. 1, 1997, pp. 34-42, esp. p. 36.

Michel Rigo, Formal Languages, Automata and Numeration Systems, 2 vols., Wiley, 2014. Mentions this sequence - see "List of Sequences" in Vol. 2.

LINKS

N. J. A. Sloane, [Table of n, a(n) for n = 0..10945][26]

A. G. M. Ahmed, [AA Weaving][27], in Proceedings of Bridges 2013: Mathematics, Music, Art, Architecture, Culture.

Jean-Paul Allouche, Julien Cassaigne, Jeffrey Shallit, and Luca Q. Zamboni, [A Taxonomy of Morphic Sequences][28], arXiv preprint arXiv:1711.10807 [cs.FL], Nov 29 2017.

J.-P. Allouche and M. Mendes France, [Automata and Automatic Sequences][29], in: Axel F. and Gratias D. (eds), Beyond Quasicrystals. Centre de Physique des Houches, vol 3. Springer, Berlin, Heidelberg, pp. 293-367, 1995; DOI https://doi.org/10.1007/978-3-662-03130-8_11.

J.-P. Allouche and M. Mendes France, [Automata and Automatic Sequences][30], in: Axel F. and Gratias D. (eds), Beyond Quasicrystals. Centre de Physique des Houches, vol 3. Springer, Berlin, Heidelberg, pp. 293-367, 1995; DOI https://doi.org/10.1007/978-3-662-03130-8_11. [Local copy]

P. Arnoux and E. Harriss, [What is a Rauzy Fractal?][31], Notices Amer. Math. Soc., 61 (No. 7, 2014), 768-770, also p. 704 and front cover.

Scott Balchin and Dan Rust, [Computations for Symbolic Substitutions][32], Journal of Integer Sequences, Vol. 20 (2017), Article 17.4.1.

Galyna Barabash, Yaroslav Kholyavka, and Iryna Tytar, [Periodic words connected with the Lucas numbers][33], Visnyk of the Lviv Univ. Series Mech. Math. (2017), Issue 84, 62-66.

Jean Berstel, [Home Page][34]

J. Berstel and J. Karhumaki, [Combinatorics on words - a tutorial][35], Bull. EATCS, #79 (2003), pp. 178-228.

Bryce Emerson Blackham, [Subtraction Games: Range and Strict Periodicity][36], Master's thesis, 2018.

Benoit Cloitre, [The Golden Sieve and its connections to Hiccup sequences and Fraenkel games][37], arXiv:2602.17735 [math.NT], 2026. See p. 30.

Cristian Cobeli and Alexandru Zaharescu, [A bias parity question for Sturmian words][38], arXiv:1811.06509 [math.NT], 2018.

Fabien Durand, Julien Leroy, and Gwenaël Richomme, [Do the Properties of an S-adic Representation Determine Factor Complexity?][39], Journal of Integer Sequences, Vol. 16 (2013), #13.2.6.

J. Endrullis, D. Hendriks and J. W. Klop, [Degrees of streams][40].

S. Ferenczi, [Complexity of sequences and dynamical systems][41], Discrete Math., 206 (1999), 145-154.

L. Goldberg and A. V. Fraenkel, [Patterns in the generalized Fibonacci word, applied to games][42], Discrete Math., 341 2018 1675-1687.

J. Grytczuk, [Infinite semi-similar words][43], Discrete Math. 161 (1996), 133-141.

Andreas M. Hinz and Paul K. Stockmeyer, [Discovering Fibonacci Numbers, Fibonacci Words, and a Fibonacci Fractal in the Tower of Hanoi][44], The Fibonacci Quarterly (2019) Vol. 57, No. 5, 72-83.

A. Hof, O. Knill and B. Simon, [Singular continuous spectrum for palindromic Schroedinger operators][45], Commun. Math. Phys. 174 (1995), 149-159.

Tyler Hoffman and B. Steinhurst, [Hausdorff Dimension of Generalized Fibonacci Word Fractals][46], arXiv preprint arXiv:1601.04786 [math.MG], 2016.

T. Karki, A. Lacroix, and M. Rigo, [On the recognizability of self-generating sets][47], JIS 13 (2010) #10.2.2.

Clark Kimberling, [A Self-Generating Set and the Golden Mean][48], J. Integer Sequences, 3 (2000), #00.2.8.

Clark Kimberling, [Intriguing infinite words composed of zeros and ones][49], Elemente der Mathematik (2021).

Eve Kivivuori, [Implementing, analyzing, and benchmarking the Relative Lempel-Ziv compression algorithm][50], Master's Thesis, Univ. Helsinki (Finland 2023).

M. Lothaire, [Algebraic Combinatorics on Words][51], Cambridge, 2002, see p. 41, etc.

Frédéric Mansuy, ["Palindromic" and "Quasi-crystalline" characteristics of the sequence and Fibonacci words.][52], hal-02082456, 2019.

Douglas M. McKenna, [On a Better Golden Rectangle (That Is Not 61.8033...% Useless!)][53], Proceedings of Bridges (2018), 187-194.

G. Melançon, [Lyndon factorization of sturmian words][54], Discr. Math., 210 (2000), 137-149.

F. Mignosi, A. Restivo, and M. Sciortino, [Words and forbidden factors][55], WORDS (Rouen, 1999). Theoret. Comput. Sci. 273 (2002), no. 1-2, 99--117. MR1872445 (2002m:68096) - From [N. J. A. Sloane][18], Jul 10 2012

Kerry Mitchell, [Spirolateral-Type Images from Integer Sequences][56], Bridges 2013.

Kerry Mitchell, [Spirolateral image for this sequence][57] [taken, with permission, from the Spirolateral-Type Images from Integer Sequences article]

T. D. Noe, [The first 1652 subwords, including leading zeros.][58]

Saúl Pilatowsky-Cameo, Soonwon Choi, and Wen Wei Ho, [Critically slow Hilbert-space ergodicity in quantum morphic drives][59], arXiv:2502.06936 [quant-ph], 2025. See p. 15.

Giuseppe Pirillo, [Fibonacci numbers and words][60], Discrete Math. 173 (1997), no. 1-3, 197--207. MR1468849 (98g:68135)

Aayush Rajasekaran, [Using Automata Theory to Solve Problems in Additive Number Theory][61], MS thesis, University of Waterloo, 2018.

Aayush Rajasekaran, Narad Rampersad, and Jeffrey Shallit, [Overpals, Underlaps, and Underpals][62], In: Brlek S., Dolce F., Reutenauer C., Vandomme É. (eds) Combinatorics on Words, WORDS 2017, Lecture Notes in Computer Science, vol 10432.

J. L. Ramírez and G. N. Rubiano, [Properties and Generalizations of the Fibonacci Word Fractal][63], The Mathematica Journal, Vol. 16 (2014).

José L. Ramírez, Gustavo N. Rubiano, and Rodrigo de Castro, [A Generalization of the Fibonacci Word Fractal and the Fibonacci Snowflake][64], arXiv preprint arXiv:1212.1368 [cs.DM], 2012.

M. Rigo, P. Salimov, and E. Vandomme, [Some Properties of Abelian Return Words][65], Journal of Integer Sequences, Vol. 16 (2013), #13.2.5.

Luke Schaeffer and Jeffrey Shallit, [Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences][66], Electronic Journal of Combinatorics 23(1) (2016), #P1.25.

N. J. A. Sloane, [Families of Essentially Identical Sequences][67], Mar 24 2021 (Includes this sequence)

Eric Weisstein's World of Mathematics, [Golden Ratio][68]

Jiemeng Zhang, Zhixiong Wen, and Wen Wu, [Some Properties of the Fibonacci Sequence on an Infinite Alphabet][69], Electronic Journal of Combinatorics, 24(2) (2017), #P2.52.

[Index entries for sequences that are fixed points of mappings][70]

[Index entries for characteristic functions][71]

FORMULA

a(n) = floor((n+2)*r) - floor((n+1)*r) where r=phi/(1+2*phi) and phi is the Golden Ratio. - [Benoit Cloitre][16], Nov 10 2003

a(n) = [A003714][72] (n) mod 2 = [A014417][73] (n) mod 2. - [Philippe Deléham][17], Jan 04 2004

The first formula by Cloitre is just one of an infinite family of formulas. Using phi^2=1+phi, it follows that r=phi/(1+2*phi)=2-phi. Then from floor(-x)=-floor(x)-1 for non-integer x, it follows that a(n)=2- [A014675][74] (n)=2-(floor((n+2)* phi)-floor((n+1)*phi)). - [Michel Dekking][75], Aug 27 2016

a(n) = 1 - [A096270][76] (n+1), i.e., [A096270][76] is the complement of this sequence. - [A.H.M. Smeets][77], Mar 31 2024

a(n)=1 if the fractional part of n/phi^2 is between sqrt(5)-2=.23606... and 1/phi=.61803.... Otherwise, a(n)=0. - [Geoffrey Caveney][78], Aug 14 2026

EXAMPLE

The word is 010010100100101001010010010100...

Over the alphabet {a,b} this is a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, ...

MAPLE

z := proc(m) option remember; if m=0 then [0] elif m=1 then [0, 1] else [op(z(m-1)), op(z(m-2))]; fi; end; z(12);

M:=19; S[0]:=`0`; S[1]:=`01`; for n from 2 to M do S[n]:=cat(S[n-1], S[n-2]); od:

t0:=S[M]: l:=length(t0); for i from 1 to l do lprint(i-1, substring(t0, i..i)); od: # [N. J. A. Sloane][18], Nov 01 2006

MATHEMATICA

Nest[ Flatten[ # /. {0 -> {0, 1}, 1 -> {0}}] &, {0}, 10] (* [Robert G. Wilson v][79], Mar 05 2005 *)

(* Alternative: *)

Flatten[Nest[{#, #[[1]]} &, {0, 1}, 9]] (* [IWABUCHI Yu(u)ki][80], Oct 23 2013 *)

(* Alternative: *)

Table[Floor[(n + 2) #] - Floor[(n + 1) #], {n, 0, 120}] &[2 - GoldenRatio] (* [Michael De Vlieger][81], Aug 15 2016 *)

(* Alternative: *)

SubstitutionSystem[{0->{0, 1}, 1->{0}}, {0}, {10}][[1]] (* [Harvey P. Dale][82], Dec 20 2021 *)

PROG

(Magma) t1:=[ n le 2 select ["0", "0, 1"][n] else Self(n-1) cat ", " cat Self(n-2) : n in [1..12]]; t1[12];

(Haskell)

a003849 n = a003849_list !! n

a003849_list = tail $ concat fws where

fws = [1] : [0] : (zipWith (++) fws $ tail fws)

-- [Reinhard Zumkeller][83], Nov 01 2013, Apr 07 2012

(PARI) a(n)=my(k=2); while(fibonacci(k)<=n, k++); while(n>1, while(fibonacci(k--)>n, ); n-=fibonacci(k)); n==1 \\ [Charles R Greathouse IV][84], Feb 03 2014

(PARI) M3849=[2, 2, 1, 0]/*L(k), S(k), L(k-1), S(k-1)*/; [A003849][85] (n)={while(n>M3849[1], M3849=vecextract(M3849, [1, 2, 1, 2])+[M3849[3], M3849[4]<<M3849[1], 0, 0]); bittest(M3849[2], n)} \\ Much faster at the expense of using ~ Nmax/5 bytes of memory (~ 250 KB for n <= 1.3e6). - [M. F. Hasler][86], Apr 07 2021

(PARI) a(n)= my(phi=quadgen(5)); 2 + (n+1)*phi\1 - (n+2)*phi\1; \\ [Ruud H.G. van Tol][87], Jan 15 2026

(Python)

def fib(n):

"""Return the concatenation of [A003849][85] (0..F-1) where F is the smallest

Fibonacci number > n, so that the result contains a(n) at index n."""

a, b = '10'

while len(b)<=n:

a, b = b, b + a

return b # [Robert FERREOL][88], Apr 15 2016, edited by [M. F. Hasler][86], Apr 07 2021

(Python)

from math import isqrt

def [A003849][85] (n): return 2-(n+2+isqrt(m:=5*(n+2)**2)>>1)+(n+1+isqrt(m-10*n-15)>>1) # [Chai Wah Wu][89], Aug 25 2022

CROSSREFS

There are several versions of this sequence in the OEIS. This one and [A003842][90] are probably the most important. See also [A008352][91], [A076662][92], [A288581][93], [A288582][11].

Binary complement of [A005614][15]. Cf. [A014675][74], [A036299][94], [A003714][72], [A014417][73], [A096268][95], [A096270][76], [A133235][96], [A182028][97], [A213975][98].

Positions of 1's gives [A003622][14].

Sequences mentioned in the Allouche et al. "Taxonomy" paper, listed by example number: 1: [A003849][85], 2: [A010060][99], 3: [A010056][100], 4: [A020985][101] and [A020987][102], 5: [A191818][103], 6: [A316340][104] and [A273129][105], 18: [A316341][106], 19: [A030302][107], 20: [A063438][108], 21: [A316342][109], 22: [A316343][110], 23: [A003849][85] minus its first term, 24: [A316344][111], 25: [A316345][112] and [A316824][113], 26: [A020985][101] and [A020987][102], 27: [A316825][114], 28: [A159689][115], 29: [A049320][116], 30: [A003849][85], 31: [A316826][117], 32: [A316827][118], 33: [A316828][119], 34: [A316344][111], 35: [A043529][120], 36: [A316829][121], 37: [A010060][99].

Cf. [A001622][23], [A104326][22], [A132338][24].

The following sequences are all essentially the same, in the sense that they are simple transformations of each other, with [A000201][13] as the parent: [A000201][13], [A001030][122], [A001468][123], [A001950][124], [A003622][14], [A003842][90], [A003849][85], [A004641][125], [A005614][15], [A014675][74], [A022342][12], [A088462][126], [A096270][76], [A114986][127], [A124841][128]. - [N. J. A. Sloane][18], Mar 11 2021

Sequence in context: [A267371][129] [A285205][130] [A286654][131] * [A188034][132] [A115199][133] [A085242][134]

Adjacent sequences: [A003846][135] [A003847][136] [A003848][137] * [A003850][138] [A003851][139] [A003852][140]

KEYWORD

nonn, easy, nice, changed

AUTHOR

[N. J. A. Sloane][18]

EXTENSIONS

Revised by [N. J. A. Sloane][18], Jul 03 2012

STATUS

approved

[Lookup][3] [Welcome][141] [Wiki][142] [Register][143] [Music][144] [Plot 2][145] [Demos][146] [Index][147] [WebCam][148] [Contribute][149] [Format][150] [Style Sheet][151] [Transforms][152] [Superseeker][153] [Recents][154]

[The OEIS Community][155]

Maintained by [The OEIS Foundation Inc.][156]

Last modified August 17 10:12 EDT 2026. Contains 398383 sequences.

[License Agreements, Terms of Use, Privacy Policy][157]


## Links

[1]: /login?redirect=%2fA003849
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A003849/list
[5]: /A003849/graph
[6]: /search?q=A003849+-id:A003849
[7]: /A003849/listen
[8]: /history?seq=A003849
[9]: /search?q=id:A003849&fmt=text
[10]: /A003849/internal
[11]: /A288582
[12]: /A022342
[13]: /A000201
[14]: /A003622
[15]: /A005614
[16]: /wiki/User:Benoit_Cloitre
[17]: /wiki/User:Philippe_Deléham
[18]: /wiki/User:N._J._A._Sloane
[19]: /wiki/User:Clark_Kimberling
[20]: /wiki/User:Isaac_Saffold
[21]: /wiki/User:Amiram_Eldar
[22]: /A104326
[23]: /A001622
[24]: /A132338
[25]: /A317208
[26]: /A003849/b003849.txt
[27]: https://archive.bridgesmathart.org/2013/bridges2013-263.pdf
[28]: https://arxiv.org/pdf/1711.10807
[29]: https://webusers.imj-prg.fr/~jean-paul.allouche/allmendeshouches.pdf
[30]: /A003842/a003842.pdf
[31]: https://www.ams.org/notices/201407/rnoti-p768.pdf
[32]: https://cs.uwaterloo.ca/journals/JIS/VOL20/Rust/rust3.html
[33]: http://prima.lnu.edu.ua/faculty/mechmat/Departments/MathVisnykLU/VLUsMath-84/VisnM-84-062.pdf
[34]: http://www-igm.univ-mlv.fr/~berstel/
[35]: http://www-igm.univ-mlv.fr/~berstel/Articles/2003TutorialCoWdec03.pdf
[36]: https://scholarsarchive.byu.edu/etd/6735
[37]: https://arxiv.org/pdf/2602.17735
[38]: https://arxiv.org/pdf/1811.06509
[39]: https://cs.uwaterloo.ca/journals/JIS/VOL16/Durand/durand2.html
[40]: https://joerg.endrullis.de/assets/papers/streams-degrees-2011.pdf
[41]: https://doi.org/10.1016/S0012-365X(98)00400-2
[42]: https://www.wisdom.weizmann.ac.il/~fraenkel/Papers/Patterns.pdf
[43]: https://doi.org/10.1016/0012-365X(95)00297-A
[44]: https://www.fq.math.ca/Papers1/57-5/Hinz-Stockmeyer.pdf
[45]: https://projecteuclid.org/euclid.cmp/1104275098
[46]: https://arxiv.org/pdf/1601.04786
[47]: https://cs.uwaterloo.ca/journals/JIS/VOL13/Rigo/rigo6.html
[48]: https://cs.uwaterloo.ca/journals/JIS/VOL3/goldentext.html
[49]: https://doi.org/10.4171/EM/468
[50]: https://hdl.handle.net/10138/562976
[51]: http://www-igm.univ-mlv.fr/~berstel/Lothaire/
[52]: https://hal.science/hal-02082456
[53]: https://archive.bridgesmathart.org/2018/bridges2018-187.html
[54]: https://doi.org/10.1016/S0012-365X(99)00123-5
[55]: https://doi.org/10.1016/S0304-3975(00)00436-9
[56]: https://archive.bridgesmathart.org/2013/bridges2013-403.pdf
[57]: /A003849/a003849.jpg
[58]: /A003849/a003849.txt
[59]: https://arxiv.org/pdf/2502.06936
[60]: https://doi.org/10.1016/S0012-365X(94)00236-C
[61]: https://uwspace.uwaterloo.ca/bitstream/handle/10012/13202/Rajasekaran_Aaayush.pdf?sequence=3
[62]: https://doi.org/10.1007/978-3-319-66396-8_3
[63]: https://www.mathematica-journal.com/2014/02/19/properties-and-generalizations-of-the-fibonacci-word-fractal/
[64]: https://arxiv.org/pdf/1212.1368
[65]: https://cs.uwaterloo.ca/journals/JIS/VOL16/Rigo/rigo3.html
[66]: https://doi.org/10.37236/5752
[67]: /A115004/a115004.txt
[68]: https://mathworld.wolfram.com/GoldenRatio.html
[69]: https://doi.org/10.37236/6745
[70]: /index/Fi#FIXEDPOINTS
[71]: /index/Ch#char_fns
[72]: /A003714
[73]: /A014417
[74]: /A014675
[75]: /wiki/User:Michel_Dekking
[76]: /A096270
[77]: /wiki/User:A.H.M._Smeets
[78]: /wiki/User:Geoffrey_Caveney
[79]: /wiki/User:Robert_G._Wilson_v
[80]: /wiki/User:IWABUCHI_Yu(u)ki
[81]: /wiki/User:Michael_De_Vlieger
[82]: /wiki/User:Harvey_P._Dale
[83]: /wiki/User:Reinhard_Zumkeller
[84]: /wiki/User:Charles_R_Greathouse_IV
[85]: /A003849
[86]: /wiki/User:M._F._Hasler
[87]: /wiki/User:Ruud_H.G._van_Tol
[88]: /wiki/User:Robert_FERREOL
[89]: /wiki/User:Chai_Wah_Wu
[90]: /A003842
[91]: /A008352
[92]: /A076662
[93]: /A288581
[94]: /A036299
[95]: /A096268
[96]: /A133235
[97]: /A182028
[98]: /A213975
[99]: /A010060
[100]: /A010056
[101]: /A020985
[102]: /A020987
[103]: /A191818
[104]: /A316340
[105]: /A273129
[106]: /A316341
[107]: /A030302
[108]: /A063438
[109]: /A316342
[110]: /A316343
[111]: /A316344
[112]: /A316345
[113]: /A316824
[114]: /A316825
[115]: /A159689
[116]: /A049320
[117]: /A316826
[118]: /A316827
[119]: /A316828
[120]: /A043529
[121]: /A316829
[122]: /A001030
[123]: /A001468
[124]: /A001950
[125]: /A004641
[126]: /A088462
[127]: /A114986
[128]: /A124841
[129]: /A267371
[130]: /A285205
[131]: /A286654
[132]: /A188034
[133]: /A115199
[134]: /A085242
[135]: /A003846
[136]: /A003847
[137]: /A003848
[138]: /A003850
[139]: /A003851
[140]: /A003852
[141]: /wiki/Welcome
[142]: /wiki/Main_Page
[143]: /wiki/Special:RequestAccount
[144]: /play.html
[145]: /plot2.html
[146]: /demo1.html
[147]: /wiki/Index_to_OEIS
[148]: /webcam
[149]: /Submit.html
[150]: /eishelp2.html
[151]: /wiki/Style_Sheet
[152]: /transforms.html
[153]: /ol.html
[154]: /recent
[155]: /community.html
[156]: http://oeisf.org
[157]: /wiki/Legal_Documents
