<!-- source: https://oeis.org/A003849/internal | converted from HTML -->

A003849 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A003849 - OEIS] [3]

[A003849][4]

The infinite Fibonacci word (start with 0, apply 0->01, 1->0, take limit).

228

%I #331 Aug 16 2026 16:27:22

%S 0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,

%T 0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,

%U 0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1

%N The infinite Fibonacci word (start with 0, apply 0->01, 1->0, take limit).

%C A Sturmian word.

%C Define strings S(0)=0, S(1)=01, S(n)=S(n-1)S(n-2); iterate; sequence is S(infinity). If the initial 0 is omitted from S(n) for n>0, we obtain A288582(n+1).

%C The 0's occur at positions in A022342 (i.e., A000201 - 1), the 1's at positions in A003622.

%C Replace each run (1;1) with (1;0) in the infinite Fibonacci word A005614 (and add 0 as prefix) A005614 begins: 1,0,1,1,0,1,0,1,1,0,1,1,... changing runs (1,1) with (1,0) produces 1,0,0,1,0,1,0,0,1,0,0,1,... - _Benoit Cloitre_, Nov 10 2003

%C Characteristic function of A003622. - _Philippe Deléham_, May 03 2004

%C The fraction of 0's in the first n terms approaches 1/phi (see for example Allouche and Shallit). - _N. J. A. Sloane_, Sep 24 2007

%C The limiting mean and variance of the first n terms are 2-phi and 2*phi-3, respectively. - _Clark Kimberling_, Mar 12 2014, Aug 16 2018

%C Let S(n) be defined as above. Then this sequence is S(1) + Sum_{n=0..} S(n), where the addition of strings represents concatenation. - _Isaac Saffold_, May 03 2019

%C The word is a concatenation of three runs: 0, 1, and 00. The limiting proportions of these are respectively 1 - phi/2, 1/2, and (phi - 1)/2. The mean runlength is (phi + 1)/2. - _Clark Kimberling_, Dec 26 2010

%C From _Amiram Eldar_, Mar 10 2021: (Start)

%C a(n) is the number of the trailing 0's in the dual Zeckendorf representation of (n+1) (A104326).

%C The asymptotic density of the occurrences of k (0 or 1) is 1/phi^(k+1), where phi is the golden ratio (A001622).

%C The asymptotic mean of this sequence is 1/phi^2 (A132338). (End)

%D J.-P. Allouche and J. Shallit, Automatic Sequences, Cambridge Univ. Press, 2003.

%D Jean Berstel, Fibonacci words—a survey, In The book of L, pp. 13-27. Springer Berlin Heidelberg, 1986.

%D J. C. Lagarias, Number Theory and Dynamical Systems, pp. 35-72 of S. A. Burr, ed., The Unreasonable Effectiveness of Number Theory, Proc. Sympos. Appl. Math., 46 (1992). Amer. Math. Soc. - see p. 64.

%D Wolfdieter Lang, The Wythoff and the Zeckendorf representations of numbers are equivalent, in G. E. Bergum et al. (edts.) Application of Fibonacci numbers vol. 6, Kluwer, Dordrecht, 1996, pp. 319-337. [See A317208 for a link.]

%D G. Melançon, Factorizing infinite words using Maple, MapleTech journal, vol. 4, no. 1, 1997, pp. 34-42, esp. p. 36.

%D Michel Rigo, Formal Languages, Automata and Numeration Systems, 2 vols., Wiley, 2014. Mentions this sequence - see "List of Sequences" in Vol. 2.

%H N. J. A. Sloane, <a href="/A003849/b003849.txt">Table of n, a(n) for n = 0..10945</a>

%H A. G. M. Ahmed, <a href="https://archive.bridgesmathart.org/2013/bridges2013-263.pdf">AA Weaving</a>, in Proceedings of Bridges 2013: Mathematics, Music, Art, Architecture, Culture.

%H Jean-Paul Allouche, Julien Cassaigne, Jeffrey Shallit, and Luca Q. Zamboni, <a href="https://arxiv.org/abs/1711.10807">A Taxonomy of Morphic Sequences</a>, arXiv preprint arXiv:1711.10807 [cs.FL], Nov 29 2017.

%H J.-P. Allouche and M. Mendes France, <a href="https://webusers.imj-prg.fr/~jean-paul.allouche/allmendeshouches.pdf">Automata and Automatic Sequences</a>, in: Axel F. and Gratias D. (eds), Beyond Quasicrystals. Centre de Physique des Houches, vol 3. Springer, Berlin, Heidelberg, pp. 293-367, 1995; DOI https://doi.org/10.1007/978-3-662-03130-8_11.

%H J.-P. Allouche and M. Mendes France, <a href="/A003842/a003842.pdf">Automata and Automatic Sequences</a>, in: Axel F. and Gratias D. (eds), Beyond Quasicrystals. Centre de Physique des Houches, vol 3. Springer, Berlin, Heidelberg, pp. 293-367, 1995; DOI https://doi.org/10.1007/978-3-662-03130-8_11. [Local copy]

%H P. Arnoux and E. Harriss, <a href="https://www.ams.org/notices/201407/rnoti-p768.pdf">What is a Rauzy Fractal?</a>, Notices Amer. Math. Soc., 61 (No. 7, 2014), 768-770, also p. 704 and front cover.

%H Scott Balchin and Dan Rust, <a href="https://cs.uwaterloo.ca/journals/JIS/VOL20/Rust/rust3.html">Computations for Symbolic Substitutions</a>, Journal of Integer Sequences, Vol. 20 (2017), Article 17.4.1.

%H Galyna Barabash, Yaroslav Kholyavka, and Iryna Tytar, <a href="http://prima.lnu.edu.ua/faculty/mechmat/Departments/MathVisnykLU/VLUsMath-84/VisnM-84-062.pdf">Periodic words connected with the Lucas numbers</a>, Visnyk of the Lviv Univ. Series Mech. Math. (2017), Issue 84, 62-66.

%H Jean Berstel, <a href="http://www-igm.univ-mlv.fr/~berstel/">Home Page</a>

%H J. Berstel and J. Karhumaki, <a href="http://www-igm.univ-mlv.fr/~berstel/Articles/2003TutorialCoWdec03.pdf">Combinatorics on words - a tutorial</a>, Bull. EATCS, #79 (2003), pp. 178-228.

%H Bryce Emerson Blackham, <a href="https://scholarsarchive.byu.edu/etd/6735">Subtraction Games: Range and Strict Periodicity</a>, Master's thesis, 2018.

%H Benoit Cloitre, <a href="https://arxiv.org/abs/2602.17735">The Golden Sieve and its connections to Hiccup sequences and Fraenkel games</a>, arXiv:2602.17735 [math.NT], 2026. See p. 30.

%H Cristian Cobeli and Alexandru Zaharescu, <a href="https://arxiv.org/abs/1811.06509">A bias parity question for Sturmian words</a>, arXiv:1811.06509 [math.NT], 2018.

%H Fabien Durand, Julien Leroy, and Gwenaël Richomme, <a href="https://cs.uwaterloo.ca/journals/JIS/VOL16/Durand/durand2.html">Do the Properties of an S-adic Representation Determine Factor Complexity?</a>, Journal of Integer Sequences, Vol. 16 (2013), #13.2.6.

%H J. Endrullis, D. Hendriks and J. W. Klop, <a href="https://joerg.endrullis.de/assets/papers/streams-degrees-2011.pdf">Degrees of streams</a>.

%H S. Ferenczi, <a href="https://doi.org/10.1016/S0012-365X(98)00400-2">Complexity of sequences and dynamical systems</a>, Discrete Math., 206 (1999), 145-154.

%H L. Goldberg and A. V. Fraenkel, <a href="https://www.wisdom.weizmann.ac.il/~fraenkel/Papers/Patterns.pdf">Patterns in the generalized Fibonacci word, applied to games</a>, Discrete Math., 341 2018 1675-1687.

%H J. Grytczuk, <a href="https://doi.org/10.1016/0012-365X(95)00297-A">Infinite semi-similar words</a>, Discrete Math. 161 (1996), 133-141.

%H Andreas M. Hinz and Paul K. Stockmeyer, <a href="https://www.fq.math.ca/Papers1/57-5/Hinz-Stockmeyer.pdf">Discovering Fibonacci Numbers, Fibonacci Words, and a Fibonacci Fractal in the Tower of Hanoi</a>, The Fibonacci Quarterly (2019) Vol. 57, No. 5, 72-83.

%H A. Hof, O. Knill and B. Simon, <a href="https://projecteuclid.org/euclid.cmp/1104275098">Singular continuous spectrum for palindromic Schroedinger operators</a>, Commun. Math. Phys. 174 (1995), 149-159.

%H Tyler Hoffman and B. Steinhurst, <a href="https://arxiv.org/abs/1601.04786">Hausdorff Dimension of Generalized Fibonacci Word Fractals</a>, arXiv preprint arXiv:1601.04786 [math.MG], 2016.

%H T. Karki, A. Lacroix, and M. Rigo, <a href="https://cs.uwaterloo.ca/journals/JIS/VOL13/Rigo/rigo6.html">On the recognizability of self-generating sets</a>, JIS 13 (2010) #10.2.2.

%H Clark Kimberling, <a href="https://cs.uwaterloo.ca/journals/JIS/VOL3/goldentext.html">A Self-Generating Set and the Golden Mean</a>, J. Integer Sequences, 3 (2000), #00.2.8.

%H Clark Kimberling, <a href="https://doi.org/10.4171/EM/468">Intriguing infinite words composed of zeros and ones</a>, Elemente der Mathematik (2021).

%H Eve Kivivuori, <a href="https://hdl.handle.net/10138/562976">Implementing, analyzing, and benchmarking the Relative Lempel-Ziv compression algorithm</a>, Master's Thesis, Univ. Helsinki (Finland 2023).

%H M. Lothaire, <a href="http://www-igm.univ-mlv.fr/~berstel/Lothaire/">Algebraic Combinatorics on Words</a>, Cambridge, 2002, see p. 41, etc.

%H Frédéric Mansuy, <a href="https://hal.science/hal-02082456">"Palindromic" and "Quasi-crystalline" characteristics of the sequence and Fibonacci words.</a>, hal-02082456, 2019.

%H Douglas M. McKenna, <a href="https://archive.bridgesmathart.org/2018/bridges2018-187.html">On a Better Golden Rectangle (That Is Not 61.8033...% Useless!)</a>, Proceedings of Bridges (2018), 187-194.

%H G. Melançon, <a href="https://doi.org/10.1016/S0012-365X(99)00123-5">Lyndon factorization of sturmian words</a>, Discr. Math., 210 (2000), 137-149.

%H F. Mignosi, A. Restivo, and M. Sciortino, <a href="https://doi.org/10.1016/S0304-3975(00)00436-9">Words and forbidden factors</a>, WORDS (Rouen, 1999). Theoret. Comput. Sci. 273 (2002), no. 1-2, 99--117. MR1872445 (2002m:68096) - From _N. J. A. Sloane_, Jul 10 2012

%H Kerry Mitchell, <a href="https://archive.bridgesmathart.org/2013/bridges2013-403.pdf">Spirolateral-Type Images from Integer Sequences</a>, Bridges 2013.

%H Kerry Mitchell, <a href="/A003849/a003849.jpg">Spirolateral image for this sequence</a> [taken, with permission, from the Spirolateral-Type Images from Integer Sequences article]

%H T. D. Noe, <a href="/A003849/a003849.txt">The first 1652 subwords, including leading zeros.</a>

%H Saúl Pilatowsky-Cameo, Soonwon Choi, and Wen Wei Ho, <a href="https://arxiv.org/abs/2502.06936">Critically slow Hilbert-space ergodicity in quantum morphic drives</a>, arXiv:2502.06936 [quant-ph], 2025. See p. 15.

%H Giuseppe Pirillo, <a href="https://doi.org/10.1016/S0012-365X(94)00236-C">Fibonacci numbers and words</a>, Discrete Math. 173 (1997), no. 1-3, 197--207. MR1468849 (98g:68135)

%H Aayush Rajasekaran, <a href="https://uwspace.uwaterloo.ca/bitstream/handle/10012/13202/Rajasekaran_Aaayush.pdf?sequence=3">Using Automata Theory to Solve Problems in Additive Number Theory</a>, MS thesis, University of Waterloo, 2018.

%H Aayush Rajasekaran, Narad Rampersad, and Jeffrey Shallit, <a href="https://doi.org/10.1007/978-3-319-66396-8_3">Overpals, Underlaps, and Underpals</a>, In: Brlek S., Dolce F., Reutenauer C., Vandomme É. (eds) Combinatorics on Words, WORDS 2017, Lecture Notes in Computer Science, vol 10432.

%H J. L. Ramírez and G. N. Rubiano, <a href="https://www.mathematica-journal.com/2014/02/19/properties-and-generalizations-of-the-fibonacci-word-fractal/">Properties and Generalizations of the Fibonacci Word Fractal</a>, The Mathematica Journal, Vol. 16 (2014).

%H José L. Ramírez, Gustavo N. Rubiano, and Rodrigo de Castro, <a href="https://arxiv.org/abs/1212.1368">A Generalization of the Fibonacci Word Fractal and the Fibonacci Snowflake</a>, arXiv preprint arXiv:1212.1368 [cs.DM], 2012.

%H M. Rigo, P. Salimov, and E. Vandomme, <a href="https://cs.uwaterloo.ca/journals/JIS/VOL16/Rigo/rigo3.html">Some Properties of Abelian Return Words</a>, Journal of Integer Sequences, Vol. 16 (2013), #13.2.5.

%H Luke Schaeffer and Jeffrey Shallit, <a href="https://doi.org/10.37236/5752">Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences</a>, Electronic Journal of Combinatorics 23(1) (2016), #P1.25.

%H N. J. A. Sloane, <a href="/A115004/a115004.txt">Families of Essentially Identical Sequences</a>, Mar 24 2021 (Includes this sequence)

%H Eric Weisstein's World of Mathematics, <a href="https://mathworld.wolfram.com/GoldenRatio.html">Golden Ratio</a>

%H Jiemeng Zhang, Zhixiong Wen, and Wen Wu, <a href="https://doi.org/10.37236/6745">Some Properties of the Fibonacci Sequence on an Infinite Alphabet</a>, Electronic Journal of Combinatorics, 24(2) (2017), #P2.52.

%H <a href="/index/Fi#FIXEDPOINTS">Index entries for sequences that are fixed points of mappings</a>

%H <a href="/index/Ch#char_fns">Index entries for characteristic functions</a>

%F a(n) = floor((n+2)*r) - floor((n+1)*r) where r=phi/(1+2*phi) and phi is the Golden Ratio. - _Benoit Cloitre_, Nov 10 2003

%F a(n) = A003714(n) mod 2 = A014417(n) mod 2. - _Philippe Deléham_, Jan 04 2004

%F The first formula by Cloitre is just one of an infinite family of formulas. Using phi^2=1+phi, it follows that r=phi/(1+2*phi)=2-phi. Then from floor(-x)=-floor(x)-1 for non-integer x, it follows that a(n)=2-A014675(n)=2-(floor((n+2)* phi)-floor((n+1)*phi)). - _Michel Dekking_, Aug 27 2016

%F a(n) = 1 - A096270(n+1), i.e., A096270 is the complement of this sequence. - _A.H.M. Smeets_, Mar 31 2024

%F a(n)=1 if the fractional part of n/phi^2 is between sqrt(5)-2=.23606... and 1/phi=.61803.... Otherwise, a(n)=0. - _Geoffrey Caveney_, Aug 14 2026

%e The word is 010010100100101001010010010100...

%e Over the alphabet {a,b} this is a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, a, b, a, b, a, a, b, a, a, b, a, b, a, ...

%p z := proc(m) option remember; if m=0 then [0] elif m=1 then [0,1] else [op(z(m-1)),op(z(m-2))]; fi; end; z(12);

%p M:=19; S[0]:=`0`; S[1]:=`01`; for n from 2 to M do S[n]:=cat(S[n-1], S[n-2]); od:

%p t0:=S[M]: l:=length(t0); for i from 1 to l do lprint(i-1,substring(t0,i..i)); od: # _N. J. A. Sloane_, Nov 01 2006

%t Nest[ Flatten[ # /. {0 -> {0, 1}, 1 -> {0}}] &, {0}, 10] (* _Robert G. Wilson v_, Mar 05 2005 *)

%t (* Alternative: *)

%t Flatten[Nest[{#, #[[1]]} &, {0, 1}, 9]] (* _IWABUCHI Yu(u)ki_, Oct 23 2013 *)

%t (* Alternative: *)

%t Table[Floor[(n + 2) #] - Floor[(n + 1) #], {n, 0, 120}] &[2 - GoldenRatio] (* _Michael De Vlieger_, Aug 15 2016 *)

%t (* Alternative: *)

%t SubstitutionSystem[{0->{0,1},1->{0}},{0},{10}][[1]] (* _Harvey P. Dale_, Dec 20 2021 *)

%o (Magma) t1:=[ n le 2 select ["0","0,1"][n] else Self(n-1) cat "," cat Self(n-2) : n in [1..12]]; t1[12];

%o (Haskell)

%o a003849 n = a003849_list !! n

%o a003849_list = tail $ concat fws where

%o fws = [1] : [0] : (zipWith (++) fws $ tail fws)

%o -- _Reinhard Zumkeller_, Nov 01 2013, Apr 07 2012

%o (PARI) a(n)=my(k=2);while(fibonacci(k)<=n,k++);while(n>1,while(fibonacci(k--)>n,); n-=fibonacci(k)); n==1 \\ _Charles R Greathouse IV_, Feb 03 2014

%o (PARI) M3849=[2,2,1,0]/*L(k),S(k),L(k-1),S(k-1)*/; A003849(n)={while(n>M3849[1],M3849=vecextract(M3849,[1,2,1,2])+[M3849[3],M3849[4]<<M3849[1],0,0]);bittest(M3849[2],n)} \\ Much faster at the expense of using ~ Nmax/5 bytes of memory (~ 250 KB for n <= 1.3e6). - _M. F. Hasler_, Apr 07 2021

%o (PARI) a(n)= my(phi=quadgen(5)); 2 + (n+1)*phi\1 - (n+2)*phi\1; \\ _Ruud H.G. van Tol_, Jan 15 2026

%o (Python)

%o def fib(n):

%o """Return the concatenation of A003849(0..F-1) where F is the smallest

%o Fibonacci number > n, so that the result contains a(n) at index n."""

%o a, b = '10'

%o while len(b)<=n:

%o a, b = b, b + a

%o return b # _Robert FERREOL_, Apr 15 2016, edited by _M. F. Hasler_, Apr 07 2021

%o (Python)

%o from math import isqrt

%o def A003849(n): return 2-(n+2+isqrt(m:=5*(n+2)**2)>>1)+(n+1+isqrt(m-10*n-15)>>1) # _Chai Wah Wu_, Aug 25 2022

%Y There are several versions of this sequence in the OEIS. This one and A003842 are probably the most important. See also A008352, A076662, A288581, A288582.

%Y Binary complement of A005614. Cf. A014675, A036299, A003714, A014417, A096268, A096270, A133235, A182028, A213975.

%Y Positions of 1's gives A003622.

%Y Sequences mentioned in the Allouche et al. "Taxonomy" paper, listed by example number: 1: A003849, 2: A010060, 3: A010056, 4: A020985 and A020987, 5: A191818, 6: A316340 and A273129, 18: A316341, 19: A030302, 20: A063438, 21: A316342, 22: A316343, 23: A003849 minus its first term, 24: A316344, 25: A316345 and A316824, 26: A020985 and A020987, 27: A316825, 28: A159689, 29: A049320, 30: A003849, 31: A316826, 32: A316827, 33: A316828, 34: A316344, 35: A043529, 36: A316829, 37: A010060.

%Y Cf. A001622, A104326, A132338.

%Y The following sequences are all essentially the same, in the sense that they are simple transformations of each other, with A000201 as the parent: A000201, A001030, A001468, A001950, A003622, A003842, A003849, A004641, A005614, A014675, A022342, A088462, A096270, A114986, A124841. - _N. J. A. Sloane_, Mar 11 2021

%K nonn,easy,nice,changed

%O 0,1

%A _N. J. A. Sloane_

%E Revised by _N. J. A. Sloane_, Jul 03 2012

[Lookup][3] [Welcome][5] [Wiki][6] [Register][7] [Music][8] [Plot 2][9] [Demos][10] [Index][11] [WebCam][12] [Contribute][13] [Format][14] [Style Sheet][15] [Transforms][16] [Superseeker][17] [Recents][18]

[The OEIS Community][19]

Maintained by [The OEIS Foundation Inc.][20]

Last modified August 17 10:12 EDT 2026. Contains 398383 sequences.

[License Agreements, Terms of Use, Privacy Policy][21]


## Links

[1]: /login?redirect=%2fA003849%2finternal
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A003849
[5]: /wiki/Welcome
[6]: /wiki/Main_Page
[7]: /wiki/Special:RequestAccount
[8]: /play.html
[9]: /plot2.html
[10]: /demo1.html
[11]: /wiki/Index_to_OEIS
[12]: /webcam
[13]: /Submit.html
[14]: /eishelp2.html
[15]: /wiki/Style_Sheet
[16]: /transforms.html
[17]: /ol.html
[18]: /recent
[19]: /community.html
[20]: http://oeisf.org
[21]: /wiki/Legal_Documents
