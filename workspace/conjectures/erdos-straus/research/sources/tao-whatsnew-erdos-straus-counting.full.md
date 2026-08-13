<!-- source: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/ | converted from HTML -->

Counting the number of solutions to the Erdös-Straus equation on unit fractions | What's new

[1]

[What's new][1]

Updates on my research and expository papers, discussion of open problems, and other maths-related topics. By Terence Tao

- [Home][1]
- [About][2]
- [Career advice][3]
- [On writing][4]
- [Books][5]
- [Mastodon+][6]
- [Applets][7]

- [Subscribe to feed][8]

# Counting the number of solutions to the Erdös-Straus equation on unit fractions

31 July, 2011 in [math.NT][9], [update][10] | Tags: [Christian Elsholtz][11], [Erdos divisor bound][12], [Erdos-Straus conjecture][13], [Paul Erdos][14] | by [Terence Tao][15]

[Christian Elsholtz][16] and I have recently finished our joint paper “ [Counting the number of solutions to the Erd&ouml;s-Straus equation on unit fractions][17] “, submitted to the [Journal of the Australian Mathematical Society][18]. This supercedes my [previous paper on the subject][19], by obtaining stronger and more general results. (The paper is currently in the process of being resubmitted to the arXiv, and should appear at [this link][20] within a few days.)

As with the previous paper, the main object of study is the number [image: {f(n)}] of solutions to the Diophantine equation

[image: \displaystyle  \frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z} \ \ \ \ \ (1)]

with [image: {x,y,z}] positive integers. The [Erd&ouml;s-Straus conjecture][21] asserts that [image: {f(n)>0}] for all [image: {n>1}]. Since [image: {f(nm) \geq f(n)}] for all positive integers [image: {n,m}], it suffices to show that [image: {f(p)>0}] for all primes [image: {p}].

We single out two special types of solutions: *Type I*solutions, in which [image: {x}] is divisible by [image: {n}] and [image: {y,z}] are coprime to [image: {n}], and *Type II*solutions, in which [image: {x}] is coprime to [image: {n}] and [image: {y,z}] are divisible by [image: {n}]. Let [image: {f_I(n), f_{II}(n)}] denote the number of Type I and Type II solutions respectively. For any [image: {n}], one has

[image: \displaystyle  f(n) \geq 3 f_I(n) + 3 f_{II}(n),]

with equality when [image: {n}] is an odd primes [image: {p}]. Thus, to prove the Erd&ouml;s-Strauss conjecture, it suffices to show that at least one of [image: {f_I(p)}], [image: {f_{II}(p)}] is positive whenever [image: {p}] is an odd prime.

Our first main results are the asymptotics

[image: \displaystyle  N \log^3 N \ll \sum_{n \leq N} f_I(n) \ll N \log^3 N]

[image: \displaystyle  N \log^3 N \ll \sum_{n \leq N} f_{II}(n) \ll N \log^3 N]

[image: \displaystyle  N \log^2 N \ll \sum_{p \leq N} f_I(p) \ll N \log^2 N \log\log N]

[image: \displaystyle  N \log^2 N \ll \sum_{p \leq N} f_{II}(p) \ll N \log^2 N.]

This improves upon the results in the previous paper, which only established

[image: \displaystyle  N \log^2 N \ll \sum_{p \leq N} f_I(p) \ll N \exp(O( \frac{\log x}{\log\log x} ))]

and

[image: \displaystyle  N \log^2 N \ll \sum_{p \leq N} f_{II}(p) \ll N \log^2 N \log \log N.]

The double logarithmic factor in the upper bound for [image: {\sum_{p \leq N} f_I(p)}] is artificial (arising from the inefficiency in the [Brun-Titchmarsh inequality][22] on very short progressions) but we do not know how to remove it.

The methods are similar to those in the previous paper (which were also independently discovered in unpublished work of Elsholtz and Heath-Brown), but with the additional input of the Erd&ouml;s divisor bound on expressions of the form [image: {\sum_{n \leq N} \tau(P(n))}] for polynomials [image: {P}], discussed in [this recent blog post][23]. (Actually, we need to tighten Erd&ouml;s’ bound somewhat, to obtain some uniformity in the bounds even as the coefficients of [image: {P}] become large, but this turns out to be achievable by going through the original arguments of Erd&ouml;s more carefully.)

We also note an [observation of Heath-Brown][24], that in our notation gives the lower bound

[image: \displaystyle  N \log^6 N \ll \sum_{n \leq N} f(n);]

thus, we see that for typical [image: {n}], that most solutions to the Erd&ouml;s-Straus equation are not of Type I or Type II, in contrast to the case when [image: {n}] is prime.

We also have a number other new results. We find a way to systematically unify all the previously known parameterisations of solutions to the Erd&ouml;s-Straus equation, by lifting the Cayley-type surface [image: {\{ (x,y,z): \frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z} \}}] to a certain three-dimensional variety in six-dimensional affine space, in such a way that integer points in the former arise from integer points in the latter. Each of the previously known characterisations of solutions then corresponds to a different choice of coordinates on this variety. (This point of view was also adopted in a [paper of Heath-Brown][24], who interprets this lifted variety as the *universal torsor*of the Cayley surface.) By optimising between these parameterisations and exploiting the [divisor bound][25], we obtain some bounds on the worst-case behaviour of [image: {f_I(n)}] and [image: {f_{II}(n)}], namely

[image: \displaystyle  f_I(n) \ll n^{3/5 + O(1/\log \log n)}]

and

[image: \displaystyle  f_{II}(n) \ll n^{2/5 + O(1/\log \log n)},]

which should be compared to a recent previous bound [image: {f(n) \ll n^{2/3 + O(1/\log \log n)}}] [of Browning and Elsholtz][26]. In the other direction, we show that [image: {f(n) \gg n^{(3+o(1))/\log\log n}}] for infinitely many [image: {n}], and [image: {f(p) \gg \log^{\frac{\log 3}{2}-o(1)} p}] for almost all primes [image: {p}]. Here, the main tools are some bounds for the representation of a rational as a sum of two unit fractions in the above-mentioned work of Browning and Elsholtz, and also the [Tur&aacute;n-Kubilius inequality][27].

We also completely classify all the congruence classes that can be solved by polynomials, completing the partial list discussed in the [previous post][19]. Specifically, the Erd&ouml;s-Straus conjecture is true for [image: {n}] whenever one of the following congruence-type conditions is satisfied:

1. [image: {n = -f \mod 4ad}], where [image: {a,d,f \in {\bf N}}] are such that [image: {f|4a^2 d+1}].
2. [image: {n = -f \mod 4ac}] and [image: {n = -\frac{c}{a} \mod f}], where [image: {a,c,f \in {\bf N}}] are such that [image: {(4ac,f)=1}].
3. [image: {n = -f \mod 4cd}] and [image: {n^2 = -4c^2d \mod f}], where [image: {c,d,f \in {\bf N}}] are such that [image: {(4cd,f)=1}].
4. [image: {n = -\frac{1}{e} \mod 4ab}] or [image: {n = -e \mod 4ab}], where [image: {a,b,e \in {\bf N}}] are such that [image: {e|a+b}] and [image: {(e,4ab)=1}].
5. [image: {n = -4a^2d \mod f}], where [image: {a,d,f \in {\bf N}}] are such that [image: {4ad|f+1}].
6. [image: {n = -4a^2d-e \mod 4ade}], where [image: {a,d,e \in {\bf N}}] are such that [image: {(4ad,e)=1}].

In principle, this suggests a way to extend the existing verification of the Erd&ouml;s-Straus conjecture beyond the current range of [image: {10^{14}}] by collecting all congruences to small moduli (e.g. up to [image: {10^6}]), and then using this to sieve out the primes up to a given size.

Finally, we begin a study of the more general equation

[image: \displaystyle  \frac{m}{n} = \frac{1}{n_1}+\ldots+\frac{1}{n_k} \ \ \ \ \ (2)]

where [image: {m > k \geq 3}] are fixed. We can obtain a partial analogue of our main bounds for the [image: {m=4,k=3}] case, namely that

[image: \displaystyle  \sum_{n \leq N} f_{m,k,II}(n) \gg N \log^{2^{k-1}-1} N]

and

[image: \displaystyle  \sum_{p \leq N} f_{m,k,II}(p) \gg N \log^{2^{k-1}-2} N / \log\log N]

were [image: {f_{m,k,II}(n)}] denotes the number of solutions to (2) which are of “Type II” in the sense that [image: {n_2,\ldots,n_k}] are all divisible by [image: {n}]. However, we do not believe our bounds to be sharp in the large [image: {k}] regime, though it does show that the expected number of solutions to (2) should grow rapidly in [image: {k}].

### Share this:

- [Print (Opens in new window) Print][28]
- [Email a link to a friend (Opens in new window) Email][29]
- More
-

- [Share on X (Opens in new window) X][30]
- [Share on Facebook (Opens in new window) Facebook][31]
- [Share on Reddit (Opens in new window) Reddit][32]
- [Share on Pinterest (Opens in new window) Pinterest][33]
-

Like Loading...

### Recent Comments

[image: Unknown's avatar] | Anonymous on [A digestion of the proof of Se…][34] |

[image: Unknown's avatar] [35] | [A digestion of the p…][35] on [Sendov’s conjecture for…][36] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][37] |

[image: Terence Tao's avatar] [38] | [Terence Tao][38] on [246A, Notes 5: conformal …][39] |

[image: Unknown's avatar] | Anonymous on [246A, Notes 5: conformal …][40] |

[image: Unknown's avatar] | Anonymous on [Analysis I][41] |

[image: Unknown's avatar] | Anonymous on [The spectral proof of the Szem…][42] |

[image: Unknown's avatar] | Anonymous on [Analysis I][43] |

[image: Unknown's avatar] | Anonymous on [245A, Notes 6: Outer measures,…][44] |

[image: Terence Tao's avatar] [38] | [Terence Tao][38] on [245A, Notes 6: Outer measures,…][45] |

[image: Terence Tao's avatar] [38] | [Terence Tao][38] on [245A, Notes 5: Differentiation…][46] |

[image: Terence Tao's avatar] [38] | [Terence Tao][38] on [246A, Notes 5: conformal …][47] |

[image: Tim Ktitarev's avatar] [48] | [Tim Ktitarev][48] on [A partial digestion of the HRT…][49] |

[image: Unknown's avatar] | Anonymous on [A partial digestion of the HRT…][50] |

[image: Michael M. Ross's avatar] | Michael M. Ross on [A digestion of the Jacobian co…][51] |

### Top Posts

- [A digestion of the proof of Sendov's conjecture][35]
- [A digestion of the Jacobian conjecture counterexample][52]
- [A partial digestion of the HRT counterexample][53]
- [Career advice][3]
- [Third SAIR competition: inverse Galois challenge][54]
- [Work hard][55]
- [Analysis I][56]
- [About][2]
- [On writing][4]
- [The three-dimensional Kakeya conjecture, after Wang and Zahl][57]

### Archives

- [August 2026][58] (2)
- [July 2026][59] (9)
- [June 2026][60] (3)
- [May 2026][61] (1)
- [March 2026][62] (4)
- [February 2026][63] (3)
- [January 2026][64] (4)
- [December 2025][65] (5)
- [November 2025][66] (5)
- [September 2025][67] (1)
- [August 2025][68] (3)
- [July 2025][69] (1)
- [June 2025][70] (2)
- [May 2025][71] (5)
- [April 2025][72] (2)
- [March 2025][73] (1)
- [February 2025][74] (3)
- [January 2025][75] (1)
- [December 2024][76] (3)
- [November 2024][77] (4)
- [October 2024][78] (1)
- [September 2024][79] (4)
- [August 2024][80] (3)
- [July 2024][81] (3)
- [June 2024][82] (1)
- [May 2024][83] (1)
- [April 2024][84] (5)
- [March 2024][85] (1)
- [December 2023][86] (2)
- [November 2023][87] (2)
- [October 2023][88] (1)
- [September 2023][89] (3)
- [August 2023][90] (3)
- [June 2023][91] (8)
- [May 2023][92] (1)
- [April 2023][93] (1)
- [March 2023][94] (2)
- [February 2023][95] (1)
- [January 2023][96] (2)
- [December 2022][97] (3)
- [November 2022][98] (3)
- [October 2022][99] (3)
- [September 2022][100] (1)
- [July 2022][101] (3)
- [June 2022][102] (1)
- [May 2022][103] (2)
- [April 2022][104] (2)
- [March 2022][105] (5)
- [February 2022][106] (3)
- [January 2022][107] (1)
- [December 2021][108] (2)
- [November 2021][109] (2)
- [October 2021][110] (1)
- [September 2021][111] (2)
- [August 2021][112] (1)
- [July 2021][113] (3)
- [June 2021][114] (1)
- [May 2021][115] (2)
- [February 2021][116] (6)
- [January 2021][117] (2)
- [December 2020][118] (4)
- [November 2020][119] (2)
- [October 2020][120] (4)
- [September 2020][121] (5)
- [August 2020][122] (2)
- [July 2020][123] (2)
- [June 2020][124] (1)
- [May 2020][125] (2)
- [April 2020][126] (3)
- [March 2020][127] (9)
- [February 2020][128] (1)
- [January 2020][129] (3)
- [December 2019][130] (4)
- [November 2019][131] (2)
- [September 2019][132] (2)
- [August 2019][133] (3)
- [July 2019][134] (2)
- [June 2019][135] (4)
- [May 2019][136] (6)
- [April 2019][137] (4)
- [March 2019][138] (2)
- [February 2019][139] (5)
- [January 2019][140] (1)
- [December 2018][141] (6)
- [November 2018][142] (2)
- [October 2018][143] (2)
- [September 2018][144] (5)
- [August 2018][145] (3)
- [July 2018][146] (3)
- [June 2018][147] (1)
- [May 2018][148] (4)
- [April 2018][149] (4)
- [March 2018][150] (5)
- [February 2018][151] (4)
- [January 2018][152] (5)
- [December 2017][153] (5)
- [November 2017][154] (3)
- [October 2017][155] (4)
- [September 2017][156] (4)
- [August 2017][157] (5)
- [July 2017][158] (5)
- [June 2017][159] (1)
- [May 2017][160] (3)
- [April 2017][161] (2)
- [March 2017][162] (3)
- [February 2017][163] (1)
- [January 2017][164] (2)
- [December 2016][165] (2)
- [November 2016][166] (2)
- [October 2016][167] (5)
- [September 2016][168] (4)
- [August 2016][169] (4)
- [July 2016][170] (1)
- [June 2016][171] (3)
- [May 2016][172] (5)
- [April 2016][173] (2)
- [March 2016][174] (6)
- [February 2016][175] (2)
- [January 2016][176] (1)
- [December 2015][177] (4)
- [November 2015][178] (6)
- [October 2015][179] (5)
- [September 2015][180] (5)
- [August 2015][181] (4)
- [July 2015][182] (7)
- [June 2015][183] (1)
- [May 2015][184] (5)
- [April 2015][185] (4)
- [March 2015][186] (3)
- [February 2015][187] (4)
- [January 2015][188] (4)
- [December 2014][189] (6)
- [November 2014][190] (5)
- [October 2014][191] (4)
- [September 2014][192] (3)
- [August 2014][193] (4)
- [July 2014][194] (5)
- [June 2014][195] (5)
- [May 2014][196] (5)
- [April 2014][197] (2)
- [March 2014][198] (4)
- [February 2014][199] (5)
- [January 2014][200] (4)
- [December 2013][201] (4)
- [November 2013][202] (5)
- [October 2013][203] (4)
- [September 2013][204] (5)
- [August 2013][205] (1)
- [July 2013][206] (7)
- [June 2013][207] (12)
- [May 2013][208] (4)
- [April 2013][209] (2)
- [March 2013][210] (2)
- [February 2013][211] (6)
- [January 2013][212] (1)
- [December 2012][213] (4)
- [November 2012][214] (7)
- [October 2012][215] (6)
- [September 2012][216] (4)
- [August 2012][217] (3)
- [July 2012][218] (4)
- [June 2012][219] (3)
- [May 2012][220] (3)
- [April 2012][221] (4)
- [March 2012][222] (5)
- [February 2012][223] (5)
- [January 2012][224] (4)
- [December 2011][225] (8)
- [November 2011][226] (8)
- [October 2011][227] (7)
- [September 2011][228] (6)
- [August 2011][229] (8)
- [July 2011][230] (9)
- [June 2011][231] (8)
- [May 2011][232] (11)
- [April 2011][233] (3)
- [March 2011][234] (10)
- [February 2011][235] (3)
- [January 2011][236] (5)
- [December 2010][237] (5)
- [November 2010][238] (6)
- [October 2010][239] (9)
- [September 2010][240] (9)
- [August 2010][241] (3)
- [July 2010][242] (4)
- [June 2010][243] (8)
- [May 2010][244] (8)
- [April 2010][245] (8)
- [March 2010][246] (8)
- [February 2010][247] (10)
- [January 2010][248] (12)
- [December 2009][249] (11)
- [November 2009][250] (8)
- [October 2009][251] (15)
- [September 2009][252] (6)
- [August 2009][253] (13)
- [July 2009][254] (10)
- [June 2009][255] (11)
- [May 2009][256] (9)
- [April 2009][257] (11)
- [March 2009][258] (14)
- [February 2009][259] (13)
- [January 2009][260] (18)
- [December 2008][261] (8)
- [November 2008][262] (9)
- [October 2008][263] (10)
- [September 2008][264] (5)
- [August 2008][265] (6)
- [July 2008][266] (7)
- [June 2008][267] (8)
- [May 2008][268] (11)
- [April 2008][269] (12)
- [March 2008][270] (12)
- [February 2008][271] (13)
- [January 2008][272] (17)
- [December 2007][273] (10)
- [November 2007][274] (9)
- [October 2007][275] (9)
- [September 2007][276] (7)
- [August 2007][277] (9)
- [July 2007][278] (9)
- [June 2007][279] (6)
- [May 2007][280] (10)
- [April 2007][281] (11)
- [March 2007][282] (9)
- [February 2007][283] (4)

### Categories

- [expository][284] (325)

  - [tricks][285] (13)

- [guest blog][286] (10)
- [Mathematics][287] (924)

  - [math.AC][288] (9)
  - [math.AG][289] (43)
  - [math.AP][290] (115)
  - [math.AT][291] (17)
  - [math.CA][292] (197)
  - [math.CO][293] (207)
  - [math.CT][294] (9)
  - [math.CV][295] (40)
  - [math.DG][296] (37)
  - [math.DS][297] (90)
  - [math.FA][298] (24)
  - [math.GM][299] (16)
  - [math.GN][300] (21)
  - [math.GR][301] (90)
  - [math.GT][302] (17)
  - [math.HO][303] (14)
  - [math.IT][304] (13)
  - [math.LO][305] (54)
  - [math.MG][306] (48)
  - [math.MP][307] (31)
  - [math.NA][308] (26)
  - [math.NT][9] (213)
  - [math.OA][309] (22)
  - [math.PR][310] (114)
  - [math.QA][311] (6)
  - [math.RA][312] (49)
  - [math.RT][313] (21)
  - [math.SG][314] (4)
  - [math.SP][315] (48)
  - [math.ST][316] (11)

- [non-technical][317] (212)

  - [admin][318] (48)
  - [advertising][319] (81)
  - [diversions][320] (7)
  - [media][321] (14)

    - [journals][322] (3)

  - [obituary][323] (15)

- [opinion][324] (37)
- [paper][325] (272)

  - [book][326] (23)
  - [Companion][327] (13)
  - [update][10] (26)

- [question][328] (128)

  - [polymath][329] (87)

- [talk][330] (69)

  - [DLS][331] (20)

- [teaching][332] (190)

  - [245A – Real analysis][333] (11)
  - [245B – Real analysis][334] (22)
  - [245C – Real analysis][335] (6)
  - [246A – complex analysis][336] (11)
  - [246B – complex analysis][337] (5)
  - [246C – complex analysis][338] (5)
  - [247B – Classical Fourier Analysis][339] (5)
  - [254A – analytic prime number theory][340] (19)
  - [254A – ergodic theory][341] (18)
  - [254A – Hilbert's fifth problem][342] (12)
  - [254A – Incompressible fluid equations][343] (5)
  - [254A – random matrices][344] (14)
  - [254B – expansion in groups][345] (8)
  - [254B – Higher order Fourier analysis][346] (9)
  - [255B – incompressible Euler equations][347] (2)
  - [275A – probability theory][348] (6)
  - [285G – poincare conjecture][349] (20)
  - [Logic reading seminar][350] (8)

- [The sciences][351] (1)
- [travel][352] (26)

###

[additive combinatorics][353] [approximate groups][354] [arithmetic progressions][355] [Artificial Intelligence][356] [Ben Green][357] [Cauchy-Schwarz][358] [Cayley graphs][359] [central limit theorem][360] [Chowla conjecture][361] [compressed sensing][362] [correspondence principle][363] [cosmic distance ladder][364] [distributions][365] [divisor function][366] [eigenvalues][367] [Elias Stein][368] [Emmanuel Breuillard][369] [entropy][370] [equidistribution][371] [Erdos][372] [ergodic theory][373] [Euler equations][374] [exponential sums][375] [finite fields][376] [Fourier transform][377] [Freiman's theorem][378] [Gowers uniformity norm][379] [Gowers uniformity norms][380] [graph theory][381] [Gromov's theorem][382] [GUE][383] [Hilbert's fifth problem][384] [ICM][385] [incompressible Euler equations][386] [inverse conjecture][387] [Joni Teravainen][388] [Kaisa Matomaki][389] [Kakeya conjecture][390] [Lie algebras][391] [Lie groups][392] [Liouville function][393] [Littlewood-Offord problem][394] [Maksym Radziwill][395] [Mobius function][396] [Navier-Stokes equations][397] [nilpotent groups][398] [nilsequences][399] [nonstandard analysis][400] [Paul Erdos][14] [politics][401] [polymath1][402] [polymath8][403] [Polymath15][404] [polynomial method][405] [polynomials][406] [prime gaps][407] [prime numbers][408] [prime number theorem][409] [random matrices][410] [randomness][411] [Ratner's theorem][412] [regularity lemma][413] [Ricci flow][414] [Riemann zeta function][415] [Schrodinger equation][416] [Shannon entropy][417] [sieve theory][418] [structure][419] [Szemeredi's theorem][420] [Tamar Ziegler][421] [ultrafilters][422] [universality][423] [Van Vu][424] [wave maps][425] [Yitang Zhang][426]

### [image: RSS] [427] [The Polymath Blog][428]

- [Polymath News and AI][429]
- [Polymath projects 2021][430]
- [A sort of Polymath on a famous MathOverflow problem][431]
- [Ten Years of Polymath][432]
- [Updates and Pictures][433]
- [Polymath proposal: finding simpler unit distance graphs of chromatic number 5][434]
- [A new polymath proposal (related to the Riemann Hypothesis) over Tao’s blog][435]
- [Spontaneous Polymath 14 – A success!][436]
- [Polymath 13 – a success!][437]
- [Non-transitive Dice over Gowers’s Blog][438]

## 11 comments

[Comments feed for this article][439]

[20 August, 2011 at 10:17 pm][440]

**[mixedmath][441]**

[image: mixedmath's avatar]

Is there anything known about the (perhaps easier) case when we look for solutions to [image: \frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z} + \frac{1}{w}]? I am trying to think whether this makes the idea easier or not.

[Reply][442]

[21 August, 2011 at 8:50 am][443]

**[Terence Tao][38]**

[image: Terence Tao's avatar]

In our paper we have some lower bounds on the average number of solutions in this case (which we call the k=4 case), but we were unable to match them with good upper bounds. There are of course more solutions in the k=4 case than the k=3 case (and in particular, there is obviously at least one solution for each n) but by the same token, they are harder to parameterise efficiently.

[Reply][444]

[13 September, 2011 at 10:34 pm][445]

**peteg**

[image: peteg's avatar]

In Lemma 2.7 of the paper and its proof, bounds are given for some of the parameters of Type I and II solutions. In particular, it is proved that, for Type I solutions, [image: {\frac{n}{4} < y < \frac{3n}{4}}], where [image: {y}] is the smallest value among [image: {x}], [image: {y}], and [image: {z}]. It is then stated that “The constants in the bounds here could be improved slightly, but such improvements will not be of importance in our applications.”

I believe I can show that the upper bound on [image: {y}] in the Type I solution case can be improved to [image: {y < \frac{n}{2}}], unless [image: {n=3 \mod{4}}], in which [image: {y \leq \frac{n+1}{2}}]. I’m not sure, maybe this is what the authors had in mind when it was said that the bounds could be improved slightly. Anyway, for what it’s worth, here is my argument. I use the notation from the paper, Lemma 2.7.

First, observe that [image: {c < n}], since [image: {c | y}] and [image: {y < \frac{3n}{4}}]. Next, observe that [image: { na + c = b (4y - n) }]. This follows by starting from (2.3) in the paper, [image: {4abcd = na + nb + c}], and, since [image: {y=acd}], it follows that [image: {(4y-n)b = na+c}]. Next, observe that [image: { z = \frac{y}{a} b }]. This follows from [image: {z= bcd}], by substituting [image: {cd = \frac{y}{a}}]. Next, observe that [image: { x = n \frac{y}{c} b }]. This follows from [image: {x= nabd}], by substituting [image: {ad = \frac{y}{c}}]. Thus the solution [image: {(x,y,z) = (n \frac{yb}{c}, y, \frac{yb}{a} )}].

Assume now that [image: {y \geq \frac{n}{2}}]. Then [image: {4y-n \geq n}], say [image: {4y-n = n+t}] where [image: {t \geq 0}]. So [image: {na+c = b(4y-n)= b(n+t)}].

But since [image: {c < n}], [image: {b \leq a}]. If [image: {b < a}], then since [image: {z=\frac{y}{a} b }], [image: {z < y}], a contradiction. So assume [image: {b=a}]. Then [image: {na + c = a(n+t)}], so [image: {c=at}]. But [image: {(c,a) = 1}], so this means [image: {a = b = 1}]. This means [image: {4y-n = n+c}]. But since [image: {c|y}], this means that [image: {c|2n}], and, since [image: {(c,n) =1}], it must be that [image: {c|2}], so [image: {c}] = 1 or 2. If [image: {c=1}], then [image: {n+1=4y-n}], which is clearly impossible. If [image: {c=2}], then [image: {2|y}] and [image: {4y-n = n+2}], so [image: {4y =2n+2}], and [image: {y = \frac{n+1}{2}}]. Since [image: {2 | y}], this case can only happen when [image: {n = 3 \mod{4}}].

[Reply][446]

[20 September, 2011 at 2:48 am][447]

**[Diophantine sets and the integers | cartesian product][448]**

[image: Unknown's avatar]

[…] Counting the number of solutions to the Erdös-Straus equation on unit fractions (terrytao.wordpress.com) […]

[Reply][449]

[20 January, 2012 at 7:04 pm][450]

**[davie][451]**

[image: davie's avatar]

can i have the list of erdos-straus conjecture expressing rational number 4/n a sum of three unit fractions 1/x+1/y+1/z???email me at my account [atillodavid@yahoo.com][452] …tnx a lot

[Reply][453]

[23 August, 2014 at 9:11 am][454]

**[ibrahimaeygue][455]**

[image: ibrahimaeygue's avatar]

Dear all
RSA numbers linked to the pythagorean triples associated with Erdös-Straus decompositions…. N = 2099999959 is factorised in less than 10 / 100th of a second almost “instantly” The general characterization is given by :
– p = s*N*r/((2*a*s – r*N)*( s+r+t))
– q = ((2*a*s – r*N)*( s+r+t))/(s*r)
and/or
– p = s*N*r/((2*a*s – r*N)*( s-r+t))
– q = ((2*a*s – r*N)*( s-r+t))/(s*r)
Best regards

[Reply][456]

[17 October, 2016 at 9:02 am][457]

**Ben thurston**

[image: Ben thurston's avatar]

I found these I hadn’t seen anywhere else: [http://imgur.com/a/mAlIR][458]

[Reply][459]

[17 October, 2016 at 9:17 am][460]

**Ben thurston**

[image: Ben thurston's avatar]

they make a little more sense factoring a term I was leaving expanded… [http://imgur.com/a/nDuao][461]

[Reply][462]

[18 October, 2016 at 12:54 am][463]

**[wlod][464]**

[image: wlod's avatar]

Perhaps, in the old days, many people got the result for all $n$ but for $12\cdot m+1$ case. This follows from the three simplest cases: $4\cdot m-1$, and $3\cdot m-1$, and $8\cdot m-3$.

[Reply][465]

[28 August, 2019 at 1:59 am][466]

**siplebrice**

[image: siplebrice's avatar]

I was toying with Integer Partitions of 4n into exactly 3 parts restricted to the divisors of pn. I’m not sure how to address that restriction combinatorially, but if a+b+c=4n and a, b, & c each divide pn, it’s done.

[Reply][467]

[2 December, 2025 at 4:17 am][468]

**Anonymous**

[image: Unknown's avatar]

For the Erdős–Straus equation
( frac{4}{n} = frac{1}{x} + frac{1}{y} + frac{1}{z} ),
one can package the usual heuristics as

[
f(n)
= A_1(n) (log n)^2

- A_2(n) log n
- O!big((log n)^alphabig),
]

with, for instance,

[
A_1(n) = prod_{p mid n} left(1 + frac{2}{p}right), qquad
A_2(n) = sum_{p mid n} frac{log p}{p},
]

for some fixed (alpha < 2). This is only meant as a compact way to
encode the standard “local factors × (log^2 n)” heuristics, not as
a new result.

[Reply][469]

### Leave a comment [Cancel reply][470]

### For commenters

To enter in LaTeX in comments, use $latex *<Your LaTeX code>*$ (without the < and > signs, of course; in fact, these signs should be avoided as they can cause formatting errors). Also, backslashes \ need to be doubled as \\. See the [about page][2] for details and for other commenting policy.

[&laquo; Erdos’ divisor bound][23]

[Localisation and compactness properties of the Navier-Stokes global regularity problem &raquo;][471]

[Blog at WordPress.com.][472] Ben Eastaugh and Chris Sternal-Johnson.

[Subscribe to feed.][8]

- [Comment][473]
- [Reblog][474]
- [Subscribe][474] [Subscribed][474]

  - [What's new][475]

  -

Already have a WordPress.com account? [Log in now.][476]

-

  - [What's new][475]
  - [Subscribe][474] [Subscribed][474]
  - [Sign up][477]
  - [Log in][476]
  - [Copy shortlink][478]
  - [Report this content][479]
  - [View post in Reader][480]
  - [Manage subscriptions][481]
  - [Collapse this bar][474]

%d


## Links

[1]: https://terrytao.wordpress.com/
[2]: https://terrytao.wordpress.com/about/
[3]: https://terrytao.wordpress.com/career-advice/
[4]: https://terrytao.wordpress.com/advice-on-writing-papers/
[5]: https://terrytao.wordpress.com/books/
[6]: https://terrytao.wordpress.com/mastodon-posts/
[7]: https://terrytao.wordpress.com/applets/
[8]: https://terrytao.wordpress.com/feed/
[9]: https://terrytao.wordpress.com/category/mathematics/mathnt/
[10]: https://terrytao.wordpress.com/category/paper/update/
[11]: https://terrytao.wordpress.com/tag/christian-elsholtz/
[12]: https://terrytao.wordpress.com/tag/erdos-divisor-bound/
[13]: https://terrytao.wordpress.com/tag/erdos-straus-conjecture/
[14]: https://terrytao.wordpress.com/tag/paul-erdos/
[15]: https://terrytao.wordpress.com/author/teorth/
[16]: http://www.math.tugraz.at/~elsholtz/
[17]: https://terrytao.wordpress.com/wp-content/uploads/2011/07/egyptian-count13.pdf
[18]: http://www.austms.org.au/Journal+of+the+Australian+Mathematical+Society
[19]: https://terrytao.wordpress.com/2011/07/07/on-the-number-of-solutions-to-4p-1n_1-1n_2-1n_3/
[20]: http://arxiv.org/abs/1107.1010
[21]: http://en.wikipedia.org/wiki/Erd&#037;C5&#037;91s&#037;E2&#037;80&#037;93Straus_conjecture
[22]: http://en.wikipedia.org/wiki/Brun&#037;E2&#037;80&#037;93Titchmarsh_theorem
[23]: https://terrytao.wordpress.com/2011/07/23/erdos-divisor-bound/
[24]: http://www.ams.org/mathscinet-getitem?mr=2075628
[25]: https://terrytao.wordpress.com/2008/09/23/the-divisor-bound/
[26]: http://www.maths.bris.ac.uk/~matdb/preprints/es.pdf
[27]: http://en.wikipedia.org/wiki/Tur&#037;C3&#037;A1n&#037;E2&#037;80&#037;93Kubilius_inequality
[28]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#print?share=print
[29]: mailto:?subject=%5BShared%20Post%5D%20Counting%20the%20number%20of%20solutions%20to%20the%20Erd%C3%B6s-Straus%20equation%20on%20unit%20fractions#038;body=https%3A%2F%2Fterrytao.wordpress.com%2F2011%2F07%2F31%2Fcounting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions%2F&#038;share=email
[30]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?share=twitter
[31]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?share=facebook
[32]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?share=reddit
[33]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?share=pinterest
[34]: https://terrytao.wordpress.com/2026/08/12/a-digestion-of-the-proof-of-sendovs-conjecture/comment-page-1/#comment-693888
[35]: https://terrytao.wordpress.com/2026/08/12/a-digestion-of-the-proof-of-sendovs-conjecture/
[36]: https://terrytao.wordpress.com/2020/12/08/sendovs-conjecture-for-sufficiently-high-degree-polynomials/comment-page-1/#comment-693886
[37]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693885
[38]: http://www.math.ucla.edu/~tao
[39]: https://terrytao.wordpress.com/2016/10/18/246a-notes-5-conformal-mapping/comment-page-1/#comment-693883
[40]: https://terrytao.wordpress.com/2016/10/18/246a-notes-5-conformal-mapping/comment-page-1/#comment-693882
[41]: https://terrytao.wordpress.com/books/analysis-i/comment-page-17/#comment-693880
[42]: https://terrytao.wordpress.com/2012/12/03/the-spectral-proof-of-the-szemeredi-regularity-lemma/comment-page-1/#comment-693879
[43]: https://terrytao.wordpress.com/books/analysis-i/comment-page-17/#comment-693878
[44]: https://terrytao.wordpress.com/2010/10/30/245a-notes-6-outer-measures-pre-measures-and-product-measures/comment-page-3/#comment-693877
[45]: https://terrytao.wordpress.com/2010/10/30/245a-notes-6-outer-measures-pre-measures-and-product-measures/comment-page-3/#comment-693875
[46]: https://terrytao.wordpress.com/2010/10/16/245a-notes-5-differentiation-theorems/comment-page-4/#comment-693874
[47]: https://terrytao.wordpress.com/2016/10/18/246a-notes-5-conformal-mapping/comment-page-1/#comment-693873
[48]: http://timktitarev.wordpress.com
[49]: https://terrytao.wordpress.com/2026/08/06/a-partial-digestion-of-the-hrt-counterexample/comment-page-1/#comment-693872
[50]: https://terrytao.wordpress.com/2026/08/06/a-partial-digestion-of-the-hrt-counterexample/comment-page-1/#comment-693871
[51]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693870
[52]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/
[53]: https://terrytao.wordpress.com/2026/08/06/a-partial-digestion-of-the-hrt-counterexample/
[54]: https://terrytao.wordpress.com/2026/06/16/third-sair-competition-inverse-galois-challenge/
[55]: https://terrytao.wordpress.com/career-advice/work-hard/
[56]: https://terrytao.wordpress.com/books/analysis-i/
[57]: https://terrytao.wordpress.com/2025/02/25/the-three-dimensional-kakeya-conjecture-after-wang-and-zahl/
[58]: https://terrytao.wordpress.com/2026/08/
[59]: https://terrytao.wordpress.com/2026/07/
[60]: https://terrytao.wordpress.com/2026/06/
[61]: https://terrytao.wordpress.com/2026/05/
[62]: https://terrytao.wordpress.com/2026/03/
[63]: https://terrytao.wordpress.com/2026/02/
[64]: https://terrytao.wordpress.com/2026/01/
[65]: https://terrytao.wordpress.com/2025/12/
[66]: https://terrytao.wordpress.com/2025/11/
[67]: https://terrytao.wordpress.com/2025/09/
[68]: https://terrytao.wordpress.com/2025/08/
[69]: https://terrytao.wordpress.com/2025/07/
[70]: https://terrytao.wordpress.com/2025/06/
[71]: https://terrytao.wordpress.com/2025/05/
[72]: https://terrytao.wordpress.com/2025/04/
[73]: https://terrytao.wordpress.com/2025/03/
[74]: https://terrytao.wordpress.com/2025/02/
[75]: https://terrytao.wordpress.com/2025/01/
[76]: https://terrytao.wordpress.com/2024/12/
[77]: https://terrytao.wordpress.com/2024/11/
[78]: https://terrytao.wordpress.com/2024/10/
[79]: https://terrytao.wordpress.com/2024/09/
[80]: https://terrytao.wordpress.com/2024/08/
[81]: https://terrytao.wordpress.com/2024/07/
[82]: https://terrytao.wordpress.com/2024/06/
[83]: https://terrytao.wordpress.com/2024/05/
[84]: https://terrytao.wordpress.com/2024/04/
[85]: https://terrytao.wordpress.com/2024/03/
[86]: https://terrytao.wordpress.com/2023/12/
[87]: https://terrytao.wordpress.com/2023/11/
[88]: https://terrytao.wordpress.com/2023/10/
[89]: https://terrytao.wordpress.com/2023/09/
[90]: https://terrytao.wordpress.com/2023/08/
[91]: https://terrytao.wordpress.com/2023/06/
[92]: https://terrytao.wordpress.com/2023/05/
[93]: https://terrytao.wordpress.com/2023/04/
[94]: https://terrytao.wordpress.com/2023/03/
[95]: https://terrytao.wordpress.com/2023/02/
[96]: https://terrytao.wordpress.com/2023/01/
[97]: https://terrytao.wordpress.com/2022/12/
[98]: https://terrytao.wordpress.com/2022/11/
[99]: https://terrytao.wordpress.com/2022/10/
[100]: https://terrytao.wordpress.com/2022/09/
[101]: https://terrytao.wordpress.com/2022/07/
[102]: https://terrytao.wordpress.com/2022/06/
[103]: https://terrytao.wordpress.com/2022/05/
[104]: https://terrytao.wordpress.com/2022/04/
[105]: https://terrytao.wordpress.com/2022/03/
[106]: https://terrytao.wordpress.com/2022/02/
[107]: https://terrytao.wordpress.com/2022/01/
[108]: https://terrytao.wordpress.com/2021/12/
[109]: https://terrytao.wordpress.com/2021/11/
[110]: https://terrytao.wordpress.com/2021/10/
[111]: https://terrytao.wordpress.com/2021/09/
[112]: https://terrytao.wordpress.com/2021/08/
[113]: https://terrytao.wordpress.com/2021/07/
[114]: https://terrytao.wordpress.com/2021/06/
[115]: https://terrytao.wordpress.com/2021/05/
[116]: https://terrytao.wordpress.com/2021/02/
[117]: https://terrytao.wordpress.com/2021/01/
[118]: https://terrytao.wordpress.com/2020/12/
[119]: https://terrytao.wordpress.com/2020/11/
[120]: https://terrytao.wordpress.com/2020/10/
[121]: https://terrytao.wordpress.com/2020/09/
[122]: https://terrytao.wordpress.com/2020/08/
[123]: https://terrytao.wordpress.com/2020/07/
[124]: https://terrytao.wordpress.com/2020/06/
[125]: https://terrytao.wordpress.com/2020/05/
[126]: https://terrytao.wordpress.com/2020/04/
[127]: https://terrytao.wordpress.com/2020/03/
[128]: https://terrytao.wordpress.com/2020/02/
[129]: https://terrytao.wordpress.com/2020/01/
[130]: https://terrytao.wordpress.com/2019/12/
[131]: https://terrytao.wordpress.com/2019/11/
[132]: https://terrytao.wordpress.com/2019/09/
[133]: https://terrytao.wordpress.com/2019/08/
[134]: https://terrytao.wordpress.com/2019/07/
[135]: https://terrytao.wordpress.com/2019/06/
[136]: https://terrytao.wordpress.com/2019/05/
[137]: https://terrytao.wordpress.com/2019/04/
[138]: https://terrytao.wordpress.com/2019/03/
[139]: https://terrytao.wordpress.com/2019/02/
[140]: https://terrytao.wordpress.com/2019/01/
[141]: https://terrytao.wordpress.com/2018/12/
[142]: https://terrytao.wordpress.com/2018/11/
[143]: https://terrytao.wordpress.com/2018/10/
[144]: https://terrytao.wordpress.com/2018/09/
[145]: https://terrytao.wordpress.com/2018/08/
[146]: https://terrytao.wordpress.com/2018/07/
[147]: https://terrytao.wordpress.com/2018/06/
[148]: https://terrytao.wordpress.com/2018/05/
[149]: https://terrytao.wordpress.com/2018/04/
[150]: https://terrytao.wordpress.com/2018/03/
[151]: https://terrytao.wordpress.com/2018/02/
[152]: https://terrytao.wordpress.com/2018/01/
[153]: https://terrytao.wordpress.com/2017/12/
[154]: https://terrytao.wordpress.com/2017/11/
[155]: https://terrytao.wordpress.com/2017/10/
[156]: https://terrytao.wordpress.com/2017/09/
[157]: https://terrytao.wordpress.com/2017/08/
[158]: https://terrytao.wordpress.com/2017/07/
[159]: https://terrytao.wordpress.com/2017/06/
[160]: https://terrytao.wordpress.com/2017/05/
[161]: https://terrytao.wordpress.com/2017/04/
[162]: https://terrytao.wordpress.com/2017/03/
[163]: https://terrytao.wordpress.com/2017/02/
[164]: https://terrytao.wordpress.com/2017/01/
[165]: https://terrytao.wordpress.com/2016/12/
[166]: https://terrytao.wordpress.com/2016/11/
[167]: https://terrytao.wordpress.com/2016/10/
[168]: https://terrytao.wordpress.com/2016/09/
[169]: https://terrytao.wordpress.com/2016/08/
[170]: https://terrytao.wordpress.com/2016/07/
[171]: https://terrytao.wordpress.com/2016/06/
[172]: https://terrytao.wordpress.com/2016/05/
[173]: https://terrytao.wordpress.com/2016/04/
[174]: https://terrytao.wordpress.com/2016/03/
[175]: https://terrytao.wordpress.com/2016/02/
[176]: https://terrytao.wordpress.com/2016/01/
[177]: https://terrytao.wordpress.com/2015/12/
[178]: https://terrytao.wordpress.com/2015/11/
[179]: https://terrytao.wordpress.com/2015/10/
[180]: https://terrytao.wordpress.com/2015/09/
[181]: https://terrytao.wordpress.com/2015/08/
[182]: https://terrytao.wordpress.com/2015/07/
[183]: https://terrytao.wordpress.com/2015/06/
[184]: https://terrytao.wordpress.com/2015/05/
[185]: https://terrytao.wordpress.com/2015/04/
[186]: https://terrytao.wordpress.com/2015/03/
[187]: https://terrytao.wordpress.com/2015/02/
[188]: https://terrytao.wordpress.com/2015/01/
[189]: https://terrytao.wordpress.com/2014/12/
[190]: https://terrytao.wordpress.com/2014/11/
[191]: https://terrytao.wordpress.com/2014/10/
[192]: https://terrytao.wordpress.com/2014/09/
[193]: https://terrytao.wordpress.com/2014/08/
[194]: https://terrytao.wordpress.com/2014/07/
[195]: https://terrytao.wordpress.com/2014/06/
[196]: https://terrytao.wordpress.com/2014/05/
[197]: https://terrytao.wordpress.com/2014/04/
[198]: https://terrytao.wordpress.com/2014/03/
[199]: https://terrytao.wordpress.com/2014/02/
[200]: https://terrytao.wordpress.com/2014/01/
[201]: https://terrytao.wordpress.com/2013/12/
[202]: https://terrytao.wordpress.com/2013/11/
[203]: https://terrytao.wordpress.com/2013/10/
[204]: https://terrytao.wordpress.com/2013/09/
[205]: https://terrytao.wordpress.com/2013/08/
[206]: https://terrytao.wordpress.com/2013/07/
[207]: https://terrytao.wordpress.com/2013/06/
[208]: https://terrytao.wordpress.com/2013/05/
[209]: https://terrytao.wordpress.com/2013/04/
[210]: https://terrytao.wordpress.com/2013/03/
[211]: https://terrytao.wordpress.com/2013/02/
[212]: https://terrytao.wordpress.com/2013/01/
[213]: https://terrytao.wordpress.com/2012/12/
[214]: https://terrytao.wordpress.com/2012/11/
[215]: https://terrytao.wordpress.com/2012/10/
[216]: https://terrytao.wordpress.com/2012/09/
[217]: https://terrytao.wordpress.com/2012/08/
[218]: https://terrytao.wordpress.com/2012/07/
[219]: https://terrytao.wordpress.com/2012/06/
[220]: https://terrytao.wordpress.com/2012/05/
[221]: https://terrytao.wordpress.com/2012/04/
[222]: https://terrytao.wordpress.com/2012/03/
[223]: https://terrytao.wordpress.com/2012/02/
[224]: https://terrytao.wordpress.com/2012/01/
[225]: https://terrytao.wordpress.com/2011/12/
[226]: https://terrytao.wordpress.com/2011/11/
[227]: https://terrytao.wordpress.com/2011/10/
[228]: https://terrytao.wordpress.com/2011/09/
[229]: https://terrytao.wordpress.com/2011/08/
[230]: https://terrytao.wordpress.com/2011/07/
[231]: https://terrytao.wordpress.com/2011/06/
[232]: https://terrytao.wordpress.com/2011/05/
[233]: https://terrytao.wordpress.com/2011/04/
[234]: https://terrytao.wordpress.com/2011/03/
[235]: https://terrytao.wordpress.com/2011/02/
[236]: https://terrytao.wordpress.com/2011/01/
[237]: https://terrytao.wordpress.com/2010/12/
[238]: https://terrytao.wordpress.com/2010/11/
[239]: https://terrytao.wordpress.com/2010/10/
[240]: https://terrytao.wordpress.com/2010/09/
[241]: https://terrytao.wordpress.com/2010/08/
[242]: https://terrytao.wordpress.com/2010/07/
[243]: https://terrytao.wordpress.com/2010/06/
[244]: https://terrytao.wordpress.com/2010/05/
[245]: https://terrytao.wordpress.com/2010/04/
[246]: https://terrytao.wordpress.com/2010/03/
[247]: https://terrytao.wordpress.com/2010/02/
[248]: https://terrytao.wordpress.com/2010/01/
[249]: https://terrytao.wordpress.com/2009/12/
[250]: https://terrytao.wordpress.com/2009/11/
[251]: https://terrytao.wordpress.com/2009/10/
[252]: https://terrytao.wordpress.com/2009/09/
[253]: https://terrytao.wordpress.com/2009/08/
[254]: https://terrytao.wordpress.com/2009/07/
[255]: https://terrytao.wordpress.com/2009/06/
[256]: https://terrytao.wordpress.com/2009/05/
[257]: https://terrytao.wordpress.com/2009/04/
[258]: https://terrytao.wordpress.com/2009/03/
[259]: https://terrytao.wordpress.com/2009/02/
[260]: https://terrytao.wordpress.com/2009/01/
[261]: https://terrytao.wordpress.com/2008/12/
[262]: https://terrytao.wordpress.com/2008/11/
[263]: https://terrytao.wordpress.com/2008/10/
[264]: https://terrytao.wordpress.com/2008/09/
[265]: https://terrytao.wordpress.com/2008/08/
[266]: https://terrytao.wordpress.com/2008/07/
[267]: https://terrytao.wordpress.com/2008/06/
[268]: https://terrytao.wordpress.com/2008/05/
[269]: https://terrytao.wordpress.com/2008/04/
[270]: https://terrytao.wordpress.com/2008/03/
[271]: https://terrytao.wordpress.com/2008/02/
[272]: https://terrytao.wordpress.com/2008/01/
[273]: https://terrytao.wordpress.com/2007/12/
[274]: https://terrytao.wordpress.com/2007/11/
[275]: https://terrytao.wordpress.com/2007/10/
[276]: https://terrytao.wordpress.com/2007/09/
[277]: https://terrytao.wordpress.com/2007/08/
[278]: https://terrytao.wordpress.com/2007/07/
[279]: https://terrytao.wordpress.com/2007/06/
[280]: https://terrytao.wordpress.com/2007/05/
[281]: https://terrytao.wordpress.com/2007/04/
[282]: https://terrytao.wordpress.com/2007/03/
[283]: https://terrytao.wordpress.com/2007/02/
[284]: https://terrytao.wordpress.com/category/expository/
[285]: https://terrytao.wordpress.com/category/expository/tricks/
[286]: https://terrytao.wordpress.com/category/guest-blog/
[287]: https://terrytao.wordpress.com/category/mathematics/
[288]: https://terrytao.wordpress.com/category/mathematics/mathac/
[289]: https://terrytao.wordpress.com/category/mathematics/mathag/
[290]: https://terrytao.wordpress.com/category/mathematics/mathap/
[291]: https://terrytao.wordpress.com/category/mathematics/mathat/
[292]: https://terrytao.wordpress.com/category/mathematics/mathca/
[293]: https://terrytao.wordpress.com/category/mathematics/mathco/
[294]: https://terrytao.wordpress.com/category/mathematics/mathct/
[295]: https://terrytao.wordpress.com/category/mathematics/mathcv/
[296]: https://terrytao.wordpress.com/category/mathematics/mathdg/
[297]: https://terrytao.wordpress.com/category/mathematics/mathds/
[298]: https://terrytao.wordpress.com/category/mathematics/mathfa/
[299]: https://terrytao.wordpress.com/category/mathematics/mathgm/
[300]: https://terrytao.wordpress.com/category/mathematics/mathgn/
[301]: https://terrytao.wordpress.com/category/mathematics/mathgr/
[302]: https://terrytao.wordpress.com/category/mathematics/mathgt/
[303]: https://terrytao.wordpress.com/category/mathematics/mathho/
[304]: https://terrytao.wordpress.com/category/mathematics/mathit/
[305]: https://terrytao.wordpress.com/category/mathematics/mathlo/
[306]: https://terrytao.wordpress.com/category/mathematics/mathmg/
[307]: https://terrytao.wordpress.com/category/mathematics/mathmp/
[308]: https://terrytao.wordpress.com/category/mathematics/mathna/
[309]: https://terrytao.wordpress.com/category/mathematics/mathoa/
[310]: https://terrytao.wordpress.com/category/mathematics/mathpr/
[311]: https://terrytao.wordpress.com/category/mathematics/mathqa/
[312]: https://terrytao.wordpress.com/category/mathematics/mathra/
[313]: https://terrytao.wordpress.com/category/mathematics/mathrt/
[314]: https://terrytao.wordpress.com/category/mathematics/mathsg/
[315]: https://terrytao.wordpress.com/category/mathematics/mathsp/
[316]: https://terrytao.wordpress.com/category/mathematics/mathst/
[317]: https://terrytao.wordpress.com/category/non-technical/
[318]: https://terrytao.wordpress.com/category/non-technical/admin/
[319]: https://terrytao.wordpress.com/category/non-technical/advertising/
[320]: https://terrytao.wordpress.com/category/non-technical/diversions-non-technical/
[321]: https://terrytao.wordpress.com/category/non-technical/media/
[322]: https://terrytao.wordpress.com/category/non-technical/media/journals/
[323]: https://terrytao.wordpress.com/category/non-technical/obituary/
[324]: https://terrytao.wordpress.com/category/opinion/
[325]: https://terrytao.wordpress.com/category/paper/
[326]: https://terrytao.wordpress.com/category/paper/book/
[327]: https://terrytao.wordpress.com/category/paper/companion/
[328]: https://terrytao.wordpress.com/category/question/
[329]: https://terrytao.wordpress.com/category/question/polymath/
[330]: https://terrytao.wordpress.com/category/talk/
[331]: https://terrytao.wordpress.com/category/talk/dls/
[332]: https://terrytao.wordpress.com/category/teaching/
[333]: https://terrytao.wordpress.com/category/teaching/245a-real-analysis/
[334]: https://terrytao.wordpress.com/category/teaching/245b-real-analysis/
[335]: https://terrytao.wordpress.com/category/teaching/245c-real-analysis/
[336]: https://terrytao.wordpress.com/category/teaching/246a-complex-analysis/
[337]: https://terrytao.wordpress.com/category/teaching/246b-complex-analysis/
[338]: https://terrytao.wordpress.com/category/teaching/246c-complex-analysis/
[339]: https://terrytao.wordpress.com/category/teaching/247b-classical-fourier-analysis/
[340]: https://terrytao.wordpress.com/category/teaching/254a-analytic-prime-number-theory/
[341]: https://terrytao.wordpress.com/category/teaching/254a-ergodic-theory/
[342]: https://terrytao.wordpress.com/category/teaching/254a-hilberts-fifth-problem/
[343]: https://terrytao.wordpress.com/category/teaching/254a-incompressible-fluid-equations/
[344]: https://terrytao.wordpress.com/category/teaching/254a-random-matrices/
[345]: https://terrytao.wordpress.com/category/teaching/254b-expansion-in-groups/
[346]: https://terrytao.wordpress.com/category/teaching/254b-higher-order-fourier-analysis/
[347]: https://terrytao.wordpress.com/category/teaching/255b-incompressible-euler-equations/
[348]: https://terrytao.wordpress.com/category/teaching/275a-probability-theory/
[349]: https://terrytao.wordpress.com/category/teaching/285g-poincare-conjecture/
[350]: https://terrytao.wordpress.com/category/teaching/logic-reading-seminar/
[351]: https://terrytao.wordpress.com/category/the-sciences/
[352]: https://terrytao.wordpress.com/category/travel/
[353]: https://terrytao.wordpress.com/tag/additive-combinatorics/
[354]: https://terrytao.wordpress.com/tag/approximate-groups/
[355]: https://terrytao.wordpress.com/tag/arithmetic-progressions/
[356]: https://terrytao.wordpress.com/tag/artificial-intelligence/
[357]: https://terrytao.wordpress.com/tag/ben-green/
[358]: https://terrytao.wordpress.com/tag/cauchy-schwarz/
[359]: https://terrytao.wordpress.com/tag/cayley-graphs/
[360]: https://terrytao.wordpress.com/tag/central-limit-theorem/
[361]: https://terrytao.wordpress.com/tag/chowla-conjecture/
[362]: https://terrytao.wordpress.com/tag/compressed-sensing/
[363]: https://terrytao.wordpress.com/tag/correspondence-principle/
[364]: https://terrytao.wordpress.com/tag/cosmic-distance-ladder/
[365]: https://terrytao.wordpress.com/tag/distributions/
[366]: https://terrytao.wordpress.com/tag/divisor-function/
[367]: https://terrytao.wordpress.com/tag/eigenvalues/
[368]: https://terrytao.wordpress.com/tag/elias-stein/
[369]: https://terrytao.wordpress.com/tag/emmanuel-breuillard/
[370]: https://terrytao.wordpress.com/tag/entropy/
[371]: https://terrytao.wordpress.com/tag/equidistribution/
[372]: https://terrytao.wordpress.com/tag/erdos/
[373]: https://terrytao.wordpress.com/tag/ergodic-theory/
[374]: https://terrytao.wordpress.com/tag/euler-equations/
[375]: https://terrytao.wordpress.com/tag/exponential-sums/
[376]: https://terrytao.wordpress.com/tag/finite-fields/
[377]: https://terrytao.wordpress.com/tag/fourier-transform/
[378]: https://terrytao.wordpress.com/tag/freimans-theorem/
[379]: https://terrytao.wordpress.com/tag/gowers-uniformity-norm/
[380]: https://terrytao.wordpress.com/tag/gowers-uniformity-norms/
[381]: https://terrytao.wordpress.com/tag/graph-theory/
[382]: https://terrytao.wordpress.com/tag/gromovs-theorem/
[383]: https://terrytao.wordpress.com/tag/gue/
[384]: https://terrytao.wordpress.com/tag/hilberts-fifth-problem/
[385]: https://terrytao.wordpress.com/tag/icm/
[386]: https://terrytao.wordpress.com/tag/incompressible-euler-equations/
[387]: https://terrytao.wordpress.com/tag/inverse-conjecture/
[388]: https://terrytao.wordpress.com/tag/joni-teravainen/
[389]: https://terrytao.wordpress.com/tag/kaisa-matomaki/
[390]: https://terrytao.wordpress.com/tag/kakeya-conjecture/
[391]: https://terrytao.wordpress.com/tag/lie-algebras/
[392]: https://terrytao.wordpress.com/tag/lie-groups/
[393]: https://terrytao.wordpress.com/tag/liouville-function/
[394]: https://terrytao.wordpress.com/tag/littlewood-offord-problem/
[395]: https://terrytao.wordpress.com/tag/maksym-radziwill/
[396]: https://terrytao.wordpress.com/tag/mobius-function/
[397]: https://terrytao.wordpress.com/tag/navier-stokes-equations/
[398]: https://terrytao.wordpress.com/tag/nilpotent-groups/
[399]: https://terrytao.wordpress.com/tag/nilsequences/
[400]: https://terrytao.wordpress.com/tag/nonstandard-analysis/
[401]: https://terrytao.wordpress.com/tag/politics/
[402]: https://terrytao.wordpress.com/tag/polymath1/
[403]: https://terrytao.wordpress.com/tag/polymath8/
[404]: https://terrytao.wordpress.com/tag/polymath15/
[405]: https://terrytao.wordpress.com/tag/polynomial-method/
[406]: https://terrytao.wordpress.com/tag/polynomials/
[407]: https://terrytao.wordpress.com/tag/prime-gaps/
[408]: https://terrytao.wordpress.com/tag/prime-numbers/
[409]: https://terrytao.wordpress.com/tag/prime-number-theorem/
[410]: https://terrytao.wordpress.com/tag/random-matrices/
[411]: https://terrytao.wordpress.com/tag/randomness/
[412]: https://terrytao.wordpress.com/tag/ratners-theorem/
[413]: https://terrytao.wordpress.com/tag/regularity-lemma/
[414]: https://terrytao.wordpress.com/tag/ricci-flow/
[415]: https://terrytao.wordpress.com/tag/riemann-zeta-function/
[416]: https://terrytao.wordpress.com/tag/schrodinger-equation/
[417]: https://terrytao.wordpress.com/tag/shannon-entropy/
[418]: https://terrytao.wordpress.com/tag/sieve-theory/
[419]: https://terrytao.wordpress.com/tag/structure/
[420]: https://terrytao.wordpress.com/tag/szemeredis-theorem/
[421]: https://terrytao.wordpress.com/tag/tamar-ziegler/
[422]: https://terrytao.wordpress.com/tag/ultrafilters/
[423]: https://terrytao.wordpress.com/tag/universality/
[424]: https://terrytao.wordpress.com/tag/van-vu/
[425]: https://terrytao.wordpress.com/tag/wave-maps/
[426]: https://terrytao.wordpress.com/tag/yitang-zhang/
[427]: https://polymathprojects.org/feed/
[428]: https://polymathprojects.org
[429]: https://polymathprojects.org/2026/04/03/polymath-news-and-ai/
[430]: https://polymathprojects.org/2021/02/20/polymath-projects-2021/
[431]: https://polymathprojects.org/2019/06/09/a-sort-of-polymath-on-a-famous-mathoverflow-problem/
[432]: https://polymathprojects.org/2019/02/03/ten-years-of-polymath/
[433]: https://polymathprojects.org/2018/10/19/updates-and-pictures/
[434]: https://polymathprojects.org/2018/04/10/polymath-proposal-finding-simpler-unit-distance-graphs-of-chromatic-number-5/
[435]: https://polymathprojects.org/2018/01/26/a-new-polymath-proposal-related-to-the-riemann-hypothesis-over-taos-blog/
[436]: https://polymathprojects.org/2018/01/26/spontaneous-polymath-14-a-success/
[437]: https://polymathprojects.org/2017/08/22/polymath-13-a-success/
[438]: https://polymathprojects.org/2017/05/15/non-transitive-dice-over-gowerss-blog/
[439]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/feed/
[440]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comment-69173
[441]: http://mixedmath.wordpress.com
[442]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?replytocom=69173#respond
[443]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comment-69250
[444]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?replytocom=69250#respond
[445]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comment-78824
[446]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?replytocom=78824#respond
[447]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comment-82097
[448]: http://cartesianproduct.wordpress.com/2011/09/20/diophantine-sets-and-the-integers/
[449]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?replytocom=82097#respond
[450]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comment-123836
[451]: http://yahoomail.com
[452]: mailto:atillodavid@yahoo.com
[453]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?replytocom=123836#respond
[454]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comment-408519
[455]: http://gravatar.com/ibrahimaeygue
[456]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?replytocom=408519#respond
[457]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comment-473389
[458]: http://imgur.com/a/mAlIR
[459]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?replytocom=473389#respond
[460]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comment-473391
[461]: http://imgur.com/a/nDuao
[462]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?replytocom=473391#respond
[463]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comment-473410
[464]: http://wlod.wordpress.com/
[465]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?replytocom=473410#respond
[466]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comment-520574
[467]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?replytocom=520574#respond
[468]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comment-689204
[469]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/?replytocom=689204#respond
[470]: /2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#respond
[471]: https://terrytao.wordpress.com/2011/08/04/localisation-and-compactness-properties-of-the-navier-stokes-global-regularity-problem/
[472]: https://wordpress.com/?ref=footer_blog
[473]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/#comments
[474]: 
[475]: https://terrytao.wordpress.com
[476]: https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fterrytao.wordpress.com%2F2011%2F07%2F31%2Fcounting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions%2F#038;signup_flow=account
[477]: https://wordpress.com/start/
[478]: https://wp.me/p3qzP-1ld
[479]: https://wordpress.com/abuse/?report_url=https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/
[480]: https://wordpress.com/reader/blogs/817149/posts/5159
[481]: https://subscribe.wordpress.com/
