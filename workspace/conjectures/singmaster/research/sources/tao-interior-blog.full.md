<!-- source: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/ | converted from HTML -->

Singmaster’s conjecture in the interior of Pascal’s triangle | What's new

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

# Singmaster’s conjecture in the interior of Pascal’s triangle

7 June, 2021 in [math.NT][9], [paper][10] | Tags: [binomial coefficients][11], [exponential sums][12], [Joni Teravainen][13], [Kaisa Matomaki][14], [Maksym Radziwill][15], [Singmaster's conjecture][16], [Xuancheng Shao][17] | by [Terence Tao][18]

[Kaisa Matomäki][19], [Maksym Radziwill][20], [Xuancheng Shao][21], [Joni Teräväinen][22], and myself have just uploaded to the arXiv our preprint “ [Singmaster’s conjecture in the interior of Pascal’s triangle][23] “. This paper leverages the theory of exponential sums over primes to make progress on a [well known conjecture of Singmaster][24] which asserts that any natural number larger than [image: {1}] appears at most a bounded number of times in Pascal’s triangle. That is to say, for any integer [image: {t \geq 2}], there are at most [image: {O(1)}] solutions to the equation

[image: \displaystyle  \binom{n}{m} = t \ \ \ \ \ (1)]

with [image: {1 \leq m < n}]. Currently, the largest number of solutions that is known to be attainable is eight, with [image: {t}] equal to

[image: \displaystyle  3003 = \binom{3003}{1} = \binom{78}{2} = \binom{15}{5} = \binom{14}{6} = \binom{14}{8} = \binom{15}{10} ]

[image: \displaystyle = \binom{78}{76} = \binom{3003}{3002}.]

Because of the symmetry [image: {\binom{n}{m} = \binom{n}{n-m}}] of Pascal’s triangle it is natural to restrict attention to the left half [image: {1 \leq m \leq n/2}] of the triangle.

Our main result settles this conjecture in the “interior” region of the triangle:

**Theorem 1 (Singmaster’s conjecture in the interior of the triangle)**If [image: {0 < \varepsilon < 1}] and [image: {t}] is sufficiently large depending on [image: {\varepsilon}], there are at most two solutions to (1) in the region

[image: \displaystyle  \exp( \log^{2/3+\varepsilon} n ) \leq m \leq n/2 \ \ \ \ \ (2)]

and hence at most four in the region

[image: \displaystyle  \exp( \log^{2/3+\varepsilon} n ) \leq m \leq n - \exp( \log^{2/3+\varepsilon} n ).]

Also, there is at most one solution in the region

[image: \displaystyle  \exp( \log^{2/3+\varepsilon} n ) \leq m \leq n/\exp(\log^{1-\varepsilon} n ).]

To verify Singmaster’s conjecture in full, it thus suffices in view of this result to verify the conjecture in the boundary region

[image: \displaystyle  2 \leq m < \exp(\log^{2/3+\varepsilon} n) \ \ \ \ \ (3)]

(or equivalently [image: {n - \exp(\log^{2/3+\varepsilon} n) < m \leq n}]); we have deleted the [image: {m=1}] case as it of course automatically supplies exactly one solution to (1). It is in fact possible that for [image: {t}] sufficiently large there are no further collisions [image: {\binom{n}{m} = \binom{n'}{m'}=t}] for [image: {(n,m), (n',m')}] in the region (3), in which case there would never be more than eight solutions to (1) for sufficiently large [image: {t}]. This is latter claim known for bounded values of [image: {m,m'}] [by Beukers, Shorey, and Tildeman][25], with the main tool used being [Siegel’s theorem on integral points][26].

The upper bound of two here for the number of solutions in the region (2) is best possible, due to the infinite family of solutions to the equation

[image: \displaystyle  \binom{n+1}{m+1} = \binom{n}{m+2} \ \ \ \ \ (4)]

coming from [image: {n = F_{2j+2} F_{2j+3}-1}], [image: {m = F_{2j} F_{2j+3}-1}] and [image: {F_j}] is the [image: {j^{th}}] Fibonacci number.

The appearance of the quantity [image: {\exp( \log^{2/3+\varepsilon} n )}] in Theorem 1 may be familiar to readers that are acquainted with Vinogradov’s bounds on exponential sums, which ends up being the main new ingredient in our arguments. In principle this threshold could be lowered if we had stronger bounds on exponential sums.

To try to control solutions to (1) we use a combination of “ [Archimedean][27] ” and “non-Archimedean” approaches. In the “Archimedean” approach (following earlier [work of Kane][28] on this problem) we view [image: {n,m}] primarily as real numbers rather than integers, and express (1) in terms of the Gamma function as

[image: \displaystyle  \frac{\Gamma(n+1)}{\Gamma(m+1) \Gamma(n-m+1)} = t.]

One can use this equation to solve for [image: {n}] in terms of [image: {m,t}] as

[image: \displaystyle  n = f_t(m)]

for a certain real analytic function [image: {f_t}] whose asymptotics are easily computable (for instance one has the asymptotic [image: {f_t(m) \asymp m t^{1/m}}]). One can then view the problem as one of trying to control the number of lattice points on the graph [image: {\{ (m,f_t(m)): m \in {\bf R} \}}]. Here we can take advantage of the fact that in the regime [image: {m \leq f_t(m)/2}] (which corresponds to working in the left half [image: {m \leq n/2}] of Pascal’s triangle), the function [image: {f_t}] can be shown to be convex, but not too convex, in the sense that one has both upper and lower bounds on the second derivative of [image: {f_t}] (in fact one can show that [image: {f''_t(m) \asymp f_t(m) (\log t/m^2)^2}]). This can be used to preclude the possibility of having a cluster of three or more nearby lattice points on the graph [image: {\{ (m,f_t(m)): m \in {\bf R} \}}], basically because the area subtended by the triangle connecting three of these points would lie between [image: {0}] and [image: {1/2}], contradicting [Pick’s theorem][29]. Developing these ideas, we were able to show

**Proposition 2**Let [image: {\varepsilon>0}], and suppose [image: {t}] is sufficiently large depending on [image: {\varepsilon}]. If [image: {(m,n)}] is a solution to (1) in the left half [image: {m \leq n/2}] of Pascal’s triangle, then there is at most one other solution [image: {(m',n')}] to this equation in the left half with

[image: \displaystyle  |m-m'| + |n-n'| \ll \exp( (\log\log t)^{1-\varepsilon} ).]

Again, the example of (4) shows that a cluster of two solutions is certainly possible; the convexity argument only kicks in once one has a cluster of three or more solutions.

To finish the proof of Theorem 1, one has to show that any two solutions [image: {(m,n), (m',n')}] to (1) in the region of interest must be close enough for the above proposition to apply. Here we switch to the “non-Archimedean” approach, in which we look at the [image: {p}] [-adic valuations][30][image: {\nu_p( \binom{n}{m} )}] of the binomial coefficients, defined as the number of times a prime [image: {p}] divides [image: {\binom{n}{m}}]. From the fundamental theorem of arithmetic, a collision

[image: \displaystyle  \binom{n}{m} = \binom{n'}{m'}]

between binomial coefficients occurs if and only if one has agreement of valuations

[image: \displaystyle  \nu_p( \binom{n}{m} ) = \nu_p( \binom{n'}{m'} ). \ \ \ \ \ (5)]

From the [Legendre formula][31]

[image: \displaystyle  \nu_p(n!) = \sum_{j=1}^\infty \lfloor \frac{n}{p^j} \rfloor]

we can rewrite this latter identity (5) as

[image: \displaystyle  \sum_{j=1}^\infty \{ \frac{m}{p^j} \} + \{ \frac{n-m}{p^j} \} - \{ \frac{n}{p^j} \} = \sum_{j=1}^\infty \{ \frac{m'}{p^j} \} + \{ \frac{n'-m'}{p^j} \} - \{ \frac{n'}{p^j} \}, \ \ \ \ \ (6)]

where [image: {\{x\} := x - \lfloor x\rfloor}] denotes the fractional part of [image: {x}]. (These sums are not truly infinite, because the summands vanish once [image: {p^j}] is larger than [image: {\max(n,n')}].)

A key idea in our approach is to view this condition (6)*statistically*, for instance by viewing [image: {p}] as a prime drawn randomly from an interval such as [image: {[P, P + P \log^{-100} P]}] for some suitably chosen scale parameter [image: {P}], so that the two sides of (6) now become random variables. It then becomes advantageous to compare correlations between these two random variables and some additional test random variable. For instance, if [image: {n}] and [image: {n'}] are far apart from each other, then one would expect the left-hand side of (6) to have a higher correlation with the fractional part [image: {\{ \frac{n}{p}\}}], since this term shows up in the summation on the left-hand side but not the right. Similarly if [image: {m}] and [image: {m'}] are far apart from each other (although there are some annoying cases one has to treat separately when there is some “unexpected commensurability”, for instance if [image: {n'-m'}] is a rational multiple of [image: {m}] where the rational has bounded numerator and denominator). In order to execute this strategy, it turns out (after some standard Fourier expansion) that one needs to get good control on exponential sums such as

[image: \displaystyle  \sum_{P \leq p \leq P + P\log^{-100} P} e( \frac{N}{p} + \frac{M}{p^j} )]

for various choices of parameters [image: {P, N, M, j}], where [image: {e(\theta) := e^{2\pi i \theta}}]. Fortunately, the methods of Vinogradov (which more generally can handle sums such as [image: {\sum_{n \in I} e(f(n))}] and [image: {\sum_{p \in I} e(f(p))}] for various analytic functions [image: {f}]) can give useful bounds on such sums as long as [image: {N}] and [image: {M}] are not too large compared to [image: {P}]; more specifically, Vinogradov’s estimates are non-trivial in the regime [image: {N,M \ll \exp( \log^{3/2-\varepsilon} P )}], and this ultimately leads to a distance bound

[image: \displaystyle  m' - m \ll_\varepsilon \exp( \log^{2/3 +\varepsilon}(n+n') )]

between any colliding pair [image: {(n,m), (n',m')}] in the left half of Pascal’s triangle, as well as the variant bound

[image: \displaystyle  n' - n \ll_\varepsilon \exp( \log^{2/3 +\varepsilon}(n+n') )]

under the additional assumption

[image: \displaystyle  m', m \geq \exp( \log^{2/3 +\varepsilon}(n+n') ).]

Comparing these bounds with Proposition 2 and using some basic estimates about the function [image: {f_t}], we can conclude Theorem 1.

A modification of the arguments also gives similar results for the equation

[image: \displaystyle  (n)_m = t \ \ \ \ \ (7)]

where [image: {(n)_m := n (n-1) \dots (n-m+1)}] is the [falling factorial][32]:

**Theorem 3**If [image: {0 < \varepsilon < 1}] and [image: {t}] is sufficiently large depending on [image: {\varepsilon}], there are at most two solutions to (7) in the region

[image: \displaystyle  \exp( \log^{2/3+\varepsilon} n ) \leq m < n. \ \ \ \ \ (8)]

Again the upper bound of two is best possible, thanks to identities such as

[image: \displaystyle  (a^2-a)_{a^2-2a} = (a^2-a-1)_{a^2-2a+1}.]

### Share this:

- [Print (Opens in new window) Print][33]
- [Email a link to a friend (Opens in new window) Email][34]
- More
-

- [Share on X (Opens in new window) X][35]
- [Share on Facebook (Opens in new window) Facebook][36]
- [Share on Reddit (Opens in new window) Reddit][37]
- [Share on Pinterest (Opens in new window) Pinterest][38]
-

Like Loading...

### Recent Comments

[image: Unknown's avatar] | Anonymous on [A digestion of the proof of Se…][39] |

[image: Unknown's avatar] [40] | [A digestion of the p…][40] on [Sendov’s conjecture for…][41] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][42] |

[image: Terence Tao's avatar] [43] | [Terence Tao][43] on [246A, Notes 5: conformal …][44] |

[image: Unknown's avatar] | Anonymous on [246A, Notes 5: conformal …][45] |

[image: Unknown's avatar] | Anonymous on [Analysis I][46] |

[image: Unknown's avatar] | Anonymous on [The spectral proof of the Szem…][47] |

[image: Unknown's avatar] | Anonymous on [Analysis I][48] |

[image: Unknown's avatar] | Anonymous on [245A, Notes 6: Outer measures,…][49] |

[image: Terence Tao's avatar] [43] | [Terence Tao][43] on [245A, Notes 6: Outer measures,…][50] |

[image: Terence Tao's avatar] [43] | [Terence Tao][43] on [245A, Notes 5: Differentiation…][51] |

[image: Terence Tao's avatar] [43] | [Terence Tao][43] on [246A, Notes 5: conformal …][52] |

[image: Tim Ktitarev's avatar] [53] | [Tim Ktitarev][53] on [A partial digestion of the HRT…][54] |

[image: Unknown's avatar] | Anonymous on [A partial digestion of the HRT…][55] |

[image: Michael M. Ross's avatar] | Michael M. Ross on [A digestion of the Jacobian co…][56] |

### Top Posts

- [A digestion of the proof of Sendov's conjecture][40]
- [A digestion of the Jacobian conjecture counterexample][57]
- [A partial digestion of the HRT counterexample][58]
- [Career advice][3]
- [Third SAIR competition: inverse Galois challenge][59]
- [Work hard][60]
- [Analysis I][61]
- [About][2]
- [On writing][4]
- [The three-dimensional Kakeya conjecture, after Wang and Zahl][62]

### Archives

- [August 2026][63] (2)
- [July 2026][64] (9)
- [June 2026][65] (3)
- [May 2026][66] (1)
- [March 2026][67] (4)
- [February 2026][68] (3)
- [January 2026][69] (4)
- [December 2025][70] (5)
- [November 2025][71] (5)
- [September 2025][72] (1)
- [August 2025][73] (3)
- [July 2025][74] (1)
- [June 2025][75] (2)
- [May 2025][76] (5)
- [April 2025][77] (2)
- [March 2025][78] (1)
- [February 2025][79] (3)
- [January 2025][80] (1)
- [December 2024][81] (3)
- [November 2024][82] (4)
- [October 2024][83] (1)
- [September 2024][84] (4)
- [August 2024][85] (3)
- [July 2024][86] (3)
- [June 2024][87] (1)
- [May 2024][88] (1)
- [April 2024][89] (5)
- [March 2024][90] (1)
- [December 2023][91] (2)
- [November 2023][92] (2)
- [October 2023][93] (1)
- [September 2023][94] (3)
- [August 2023][95] (3)
- [June 2023][96] (8)
- [May 2023][97] (1)
- [April 2023][98] (1)
- [March 2023][99] (2)
- [February 2023][100] (1)
- [January 2023][101] (2)
- [December 2022][102] (3)
- [November 2022][103] (3)
- [October 2022][104] (3)
- [September 2022][105] (1)
- [July 2022][106] (3)
- [June 2022][107] (1)
- [May 2022][108] (2)
- [April 2022][109] (2)
- [March 2022][110] (5)
- [February 2022][111] (3)
- [January 2022][112] (1)
- [December 2021][113] (2)
- [November 2021][114] (2)
- [October 2021][115] (1)
- [September 2021][116] (2)
- [August 2021][117] (1)
- [July 2021][118] (3)
- [June 2021][119] (1)
- [May 2021][120] (2)
- [February 2021][121] (6)
- [January 2021][122] (2)
- [December 2020][123] (4)
- [November 2020][124] (2)
- [October 2020][125] (4)
- [September 2020][126] (5)
- [August 2020][127] (2)
- [July 2020][128] (2)
- [June 2020][129] (1)
- [May 2020][130] (2)
- [April 2020][131] (3)
- [March 2020][132] (9)
- [February 2020][133] (1)
- [January 2020][134] (3)
- [December 2019][135] (4)
- [November 2019][136] (2)
- [September 2019][137] (2)
- [August 2019][138] (3)
- [July 2019][139] (2)
- [June 2019][140] (4)
- [May 2019][141] (6)
- [April 2019][142] (4)
- [March 2019][143] (2)
- [February 2019][144] (5)
- [January 2019][145] (1)
- [December 2018][146] (6)
- [November 2018][147] (2)
- [October 2018][148] (2)
- [September 2018][149] (5)
- [August 2018][150] (3)
- [July 2018][151] (3)
- [June 2018][152] (1)
- [May 2018][153] (4)
- [April 2018][154] (4)
- [March 2018][155] (5)
- [February 2018][156] (4)
- [January 2018][157] (5)
- [December 2017][158] (5)
- [November 2017][159] (3)
- [October 2017][160] (4)
- [September 2017][161] (4)
- [August 2017][162] (5)
- [July 2017][163] (5)
- [June 2017][164] (1)
- [May 2017][165] (3)
- [April 2017][166] (2)
- [March 2017][167] (3)
- [February 2017][168] (1)
- [January 2017][169] (2)
- [December 2016][170] (2)
- [November 2016][171] (2)
- [October 2016][172] (5)
- [September 2016][173] (4)
- [August 2016][174] (4)
- [July 2016][175] (1)
- [June 2016][176] (3)
- [May 2016][177] (5)
- [April 2016][178] (2)
- [March 2016][179] (6)
- [February 2016][180] (2)
- [January 2016][181] (1)
- [December 2015][182] (4)
- [November 2015][183] (6)
- [October 2015][184] (5)
- [September 2015][185] (5)
- [August 2015][186] (4)
- [July 2015][187] (7)
- [June 2015][188] (1)
- [May 2015][189] (5)
- [April 2015][190] (4)
- [March 2015][191] (3)
- [February 2015][192] (4)
- [January 2015][193] (4)
- [December 2014][194] (6)
- [November 2014][195] (5)
- [October 2014][196] (4)
- [September 2014][197] (3)
- [August 2014][198] (4)
- [July 2014][199] (5)
- [June 2014][200] (5)
- [May 2014][201] (5)
- [April 2014][202] (2)
- [March 2014][203] (4)
- [February 2014][204] (5)
- [January 2014][205] (4)
- [December 2013][206] (4)
- [November 2013][207] (5)
- [October 2013][208] (4)
- [September 2013][209] (5)
- [August 2013][210] (1)
- [July 2013][211] (7)
- [June 2013][212] (12)
- [May 2013][213] (4)
- [April 2013][214] (2)
- [March 2013][215] (2)
- [February 2013][216] (6)
- [January 2013][217] (1)
- [December 2012][218] (4)
- [November 2012][219] (7)
- [October 2012][220] (6)
- [September 2012][221] (4)
- [August 2012][222] (3)
- [July 2012][223] (4)
- [June 2012][224] (3)
- [May 2012][225] (3)
- [April 2012][226] (4)
- [March 2012][227] (5)
- [February 2012][228] (5)
- [January 2012][229] (4)
- [December 2011][230] (8)
- [November 2011][231] (8)
- [October 2011][232] (7)
- [September 2011][233] (6)
- [August 2011][234] (8)
- [July 2011][235] (9)
- [June 2011][236] (8)
- [May 2011][237] (11)
- [April 2011][238] (3)
- [March 2011][239] (10)
- [February 2011][240] (3)
- [January 2011][241] (5)
- [December 2010][242] (5)
- [November 2010][243] (6)
- [October 2010][244] (9)
- [September 2010][245] (9)
- [August 2010][246] (3)
- [July 2010][247] (4)
- [June 2010][248] (8)
- [May 2010][249] (8)
- [April 2010][250] (8)
- [March 2010][251] (8)
- [February 2010][252] (10)
- [January 2010][253] (12)
- [December 2009][254] (11)
- [November 2009][255] (8)
- [October 2009][256] (15)
- [September 2009][257] (6)
- [August 2009][258] (13)
- [July 2009][259] (10)
- [June 2009][260] (11)
- [May 2009][261] (9)
- [April 2009][262] (11)
- [March 2009][263] (14)
- [February 2009][264] (13)
- [January 2009][265] (18)
- [December 2008][266] (8)
- [November 2008][267] (9)
- [October 2008][268] (10)
- [September 2008][269] (5)
- [August 2008][270] (6)
- [July 2008][271] (7)
- [June 2008][272] (8)
- [May 2008][273] (11)
- [April 2008][274] (12)
- [March 2008][275] (12)
- [February 2008][276] (13)
- [January 2008][277] (17)
- [December 2007][278] (10)
- [November 2007][279] (9)
- [October 2007][280] (9)
- [September 2007][281] (7)
- [August 2007][282] (9)
- [July 2007][283] (9)
- [June 2007][284] (6)
- [May 2007][285] (10)
- [April 2007][286] (11)
- [March 2007][287] (9)
- [February 2007][288] (4)

### Categories

- [expository][289] (325)

  - [tricks][290] (13)

- [guest blog][291] (10)
- [Mathematics][292] (924)

  - [math.AC][293] (9)
  - [math.AG][294] (43)
  - [math.AP][295] (115)
  - [math.AT][296] (17)
  - [math.CA][297] (197)
  - [math.CO][298] (207)
  - [math.CT][299] (9)
  - [math.CV][300] (40)
  - [math.DG][301] (37)
  - [math.DS][302] (90)
  - [math.FA][303] (24)
  - [math.GM][304] (16)
  - [math.GN][305] (21)
  - [math.GR][306] (90)
  - [math.GT][307] (17)
  - [math.HO][308] (14)
  - [math.IT][309] (13)
  - [math.LO][310] (54)
  - [math.MG][311] (48)
  - [math.MP][312] (31)
  - [math.NA][313] (26)
  - [math.NT][9] (213)
  - [math.OA][314] (22)
  - [math.PR][315] (114)
  - [math.QA][316] (6)
  - [math.RA][317] (49)
  - [math.RT][318] (21)
  - [math.SG][319] (4)
  - [math.SP][320] (48)
  - [math.ST][321] (11)

- [non-technical][322] (212)

  - [admin][323] (48)
  - [advertising][324] (81)
  - [diversions][325] (7)
  - [media][326] (14)

    - [journals][327] (3)

  - [obituary][328] (15)

- [opinion][329] (37)
- [paper][10] (272)

  - [book][330] (23)
  - [Companion][331] (13)
  - [update][332] (26)

- [question][333] (128)

  - [polymath][334] (87)

- [talk][335] (69)

  - [DLS][336] (20)

- [teaching][337] (190)

  - [245A – Real analysis][338] (11)
  - [245B – Real analysis][339] (22)
  - [245C – Real analysis][340] (6)
  - [246A – complex analysis][341] (11)
  - [246B – complex analysis][342] (5)
  - [246C – complex analysis][343] (5)
  - [247B – Classical Fourier Analysis][344] (5)
  - [254A – analytic prime number theory][345] (19)
  - [254A – ergodic theory][346] (18)
  - [254A – Hilbert's fifth problem][347] (12)
  - [254A – Incompressible fluid equations][348] (5)
  - [254A – random matrices][349] (14)
  - [254B – expansion in groups][350] (8)
  - [254B – Higher order Fourier analysis][351] (9)
  - [255B – incompressible Euler equations][352] (2)
  - [275A – probability theory][353] (6)
  - [285G – poincare conjecture][354] (20)
  - [Logic reading seminar][355] (8)

- [The sciences][356] (1)
- [travel][357] (26)

###

[additive combinatorics][358] [approximate groups][359] [arithmetic progressions][360] [Artificial Intelligence][361] [Ben Green][362] [Cauchy-Schwarz][363] [Cayley graphs][364] [central limit theorem][365] [Chowla conjecture][366] [compressed sensing][367] [correspondence principle][368] [cosmic distance ladder][369] [distributions][370] [divisor function][371] [eigenvalues][372] [Elias Stein][373] [Emmanuel Breuillard][374] [entropy][375] [equidistribution][376] [Erdos][377] [ergodic theory][378] [Euler equations][379] [exponential sums][12] [finite fields][380] [Fourier transform][381] [Freiman's theorem][382] [Gowers uniformity norm][383] [Gowers uniformity norms][384] [graph theory][385] [Gromov's theorem][386] [GUE][387] [Hilbert's fifth problem][388] [ICM][389] [incompressible Euler equations][390] [inverse conjecture][391] [Joni Teravainen][13] [Kaisa Matomaki][14] [Kakeya conjecture][392] [Lie algebras][393] [Lie groups][394] [Liouville function][395] [Littlewood-Offord problem][396] [Maksym Radziwill][15] [Mobius function][397] [Navier-Stokes equations][398] [nilpotent groups][399] [nilsequences][400] [nonstandard analysis][401] [Paul Erdos][402] [politics][403] [polymath1][404] [polymath8][405] [Polymath15][406] [polynomial method][407] [polynomials][408] [prime gaps][409] [prime numbers][410] [prime number theorem][411] [random matrices][412] [randomness][413] [Ratner's theorem][414] [regularity lemma][415] [Ricci flow][416] [Riemann zeta function][417] [Schrodinger equation][418] [Shannon entropy][419] [sieve theory][420] [structure][421] [Szemeredi's theorem][422] [Tamar Ziegler][423] [ultrafilters][424] [universality][425] [Van Vu][426] [wave maps][427] [Yitang Zhang][428]

### [image: RSS] [429] [The Polymath Blog][430]

- [Polymath News and AI][431]
- [Polymath projects 2021][432]
- [A sort of Polymath on a famous MathOverflow problem][433]
- [Ten Years of Polymath][434]
- [Updates and Pictures][435]
- [Polymath proposal: finding simpler unit distance graphs of chromatic number 5][436]
- [A new polymath proposal (related to the Riemann Hypothesis) over Tao’s blog][437]
- [Spontaneous Polymath 14 – A success!][438]
- [Polymath 13 – a success!][439]
- [Non-transitive Dice over Gowers’s Blog][440]

## 31 comments

[Comments feed for this article][441]

[7 June, 2021 at 6:48 pm][442]

**William Verreault**

[image: William Verreault's avatar]

What a coincidence, I was a coauthor on a paper that only recently appeared in Integers on Singmaster’s conjecture, called ”Repetitions of Multinomial Coefficients and a Generalization of Singmaster’s Conjecture”.

It is #A34 on Integers 2021 page: [http://math.colgate.edu/~integers/current.html][443]

It’d be interesting to see how these ideas hold up in higher dimensions!

[Reply][444]

[8 June, 2021 at 7:41 am][445]

**[Terence Tao][43]**

[image: Terence Tao's avatar]

Thanks for the reference! It does seem plausible that the methods will extend to multinomial equations such as [image: \binom{n}{m_1,m_2,m_3} = t] in the interior of the simplex [image: \{ (m_1,m_2,m_3,n): n = m_1 + m_2 + m_3 \}]. It is tempting for instance to work in the region [image: m_1 \leq m_2 \leq m_3] and express [image: n] as an analytic function [image: n = f_t(m_1,m_2)] of [image: m_1, m_2] for a given [image: t]. If one can establish some convexity bounds on this function [image: f_t] then the Archimedean arguments should largely go through (though now clusters can have three solutions instead of two). The types of correlations we compute in the non-Archimedean arguments would also be computable in the multinomial case, but the case analysis is likely to be more complicated. Still one should be able to get some partial results at least in this case (optimistically one could hope for an upper bound of three solutions in the interior of the simplex when [image: m_1 \leq m_2 \leq m_3], and thus at most [image: 3 \times 3! = 18] solutions without the order restriction, but there may be technical issues preventing one from getting this far).

[Reply][446]

[15 June, 2021 at 12:24 pm][447]

**William Verreault**

[image: William Verreault's avatar]

That sounds good, I’ll have to try to work it out!

Have you looked at whether one can improve these results (and possibly prove Singmaster’s conjecture) conditionally on other various conjectures (e.g. GRH to get better exponential sum estimates, bounds on gaps between primes to modify the regions where you work, possibly abc conjecture, etc.)?

[Reply][448]

[16 June, 2021 at 10:01 am][449]

**[Terence Tao][43]**

[image: Terence Tao's avatar]

This is briefly discussed in the footnote on page 2. The main thing that is needed in our arguments are estimates of the form

[image: \displaystyle \sum_{P \leq p \leq 2P} e( N/p ) = o( \frac{P}{\log P} )]

for various large [image: P,N] (this is roughly the same as asking that the fractional parts [image: \{N/p\}] for prime [image: p \asymp P] are uniformly distributed). [Actually for technical reasons (involving the need to also control prime powers [image: p^j]) we work with a slightly shorter interval than [image: [P,2P]] and need a slightly more general phase and slightly stronger error terms, but never mind these complications for now.] The estimates of Vinogradov basically let us get something like this as long as [image: N \ll \exp( \log^{3/2-\varepsilon} P )], but pseudorandomness heuristics predict a much larger range of [image: N] such as [image: N \ll \exp(P^c)] for some [image: c>0] (perhaps even [image: c] arbitrarily close to 1), which would lead to widening the applicability of our results to something like [image: \log^C n \leq m \leq n - \log^C n]. In comparison, the Riemann hypothesis would (morally, at least) give results of the form

[image: \displaystyle \sum_{P \leq p \leq 2P} e( N \log p ) = o( \frac{P}{\log P} )]

for such a wide range of [image: N], which certainly looks similar, but we could not obtain a direct connection between the two types of estimates.

[Reply][450]

[22 August, 2021 at 5:55 am][451]

**思**

[image: 思's avatar]

Hello,professor. I am a Chinese student about to enter freshman year. These days, I think about the “3N + 1” conjecture. I think I should prove it. I wonder if you could have a look. If you can, please reply me! esteem it a favor!

[8 June, 2021 at 2:21 am][452]

**Anonymous**

[image: Unknown's avatar]

Typo in the formula after (5): the sum should be over $P \le p \le P + P \log^{-100} P$.

*[Corrected, thanks – T.]*

[Reply][453]

[8 June, 2021 at 4:44 am][454]

**[Simple unsolved math problem, 5 | Yet Another Mathblog][455]**

[…] Xuancheng Shao, Joni Teräväinen, and Terrance Tao solved the conjecture below recently (see T. Tao’s blog post with the link to the paper and a […]

[Reply][456]

[8 June, 2021 at 5:20 pm][457]

**Anonymous**

[image: Unknown's avatar]

Is it possible to extend these results (beyond binomial coefficients) for a larger class of functions [image: f(m, n)] (having certain regularity properties and sufficiently fast growth rate)?

[Reply][458]

[9 June, 2021 at 9:12 am][459]

**[Terence Tao][43]**

[image: Terence Tao's avatar]

Such hypotheses would suffice for the “Archimedean” parts of the argument, but for the “non-Archimedean” parts one needs to know information about the prime factorisation of [image: f(m,n)]. For instance, a basic property about the prime factorisation of [image: \binom{n}{m}] for [image: 1 \leq m \leq n/2] is that this binomial coefficient is divisible by every prime between [image: n-m+1] and [image: n], but not by any prime larger than [image: n]. This fact alone is already enough to establish non-collision [image: \binom{n}{m} \neq \binom{n'}{m'}] for a reasonable number of pairs [image: (n,m), (n',m')]; the argument we employ evolved from various attempts to try to generalise this type of argument (which already appears in an early work on this problem by Abbott, Erdos, and Hansen).

[Reply][460]

[12 June, 2021 at 7:11 pm][461]

**Anonymous**

[image: Unknown's avatar]

Non twin prime

After adding 1 and 3 to each natural number in the natural number set n, a pair of new numbers with 1 and 3 bits can be formed. If the pair of numbers are twin primes, the corresponding elements in the n set are put into the a set, otherwise they are put into the B set. For example, after adding the numbers 1 and 3 to the number “4” in the n set, two new numbers 41 and 43 are formed, which are a pair of twin prime numbers, then “4” is put into the a set.

For example, natural numbers within 10 can be divided into two categories as follows:

Class 1: there are four numbers, specifically 1, 4, 7 and 10. According to this rule, they should be put into a set,

Class 2: there are six numbers: 2, 3, 5, 6, 8, 9. According to this rule, they should be put into b set.

Obviously, a and B sets complement each other and refer to four pairs of twin primes, twin primes and six pairs of non twin primes with 1 and 3 in natural number 109 respectively.

Can we say that the elements in B set are “non twin primes” and complement of twin primes?

Here, we only study the twin prime numbers 11-13 and 41-43, which are 1 and 3.

[Reply][462]

[8 June, 2021 at 11:19 pm][463]

**Anonymous**

[image: Unknown's avatar]

How can I read the inequalities if e.g. [image: \epsilon=\frac{1}{3}]? For Eq. (2) one gets [image: n \leq m \leq \frac{n}{2}] which is…weird.

[Reply][464]

[9 June, 2021 at 6:39 am][465]

**Aunonymous**

[image: Unknown's avatar]

I mean, what he said is true. The interval is just empty.

[Reply][466]

[9 June, 2021 at 11:43 am][467]

**Anonymous**

[image: Unknown's avatar]

Maksym’s webpage is mis-linked.

*[Corrected, thanks – T.]*

[Reply][468]

[9 June, 2021 at 3:01 pm][469]

**[Singmaster and Pascal – The nth Root][470]**

[…] Kaisa Matomäki, Maksym Radziwill, Xuancheng Shao, Joni Teräväinen, and myself have just uploaded to the arXiv our preprint “Singmaster’s conjecture in the interior of Pascal’s triangle“. This paper leverages the theory of exponential sums over primes to make progress on a well known conjecture of Singmaster which asserts that any natural number larger than {1} appears at most a bounded number of times in Pascal’s triangle. … (Terry Tao) […]

[Reply][471]

[10 June, 2021 at 1:07 am][472]

**[Singmaster’s conjecture – SPP 2026][473]**

[…] learned about this conjecture by a blog post of Terence Tao on his own blog. There he reported on recent progress on this conjecture […]

[Reply][474]

[10 June, 2021 at 7:52 am][475]

**[Antoine Deleforge][476]**

[image: Unknown's avatar]

Really nice work! I noticed one small inconsistency between the elementary examples in your paper and the ones given on the Wikipedia page on Singmaster’s conjecture ( [https://en.wikipedia.org/wiki/Singmaster%27s_conjecture][24]): you give (52, 22, 3) while the wikipedia page seems to give (56, 22, 3). Do you know which one is correct?

*[Thanks for locating this typo; it will be corrected in the next version of the ms. -T]*

[Reply][477]

[11 June, 2021 at 10:42 am][478]

**Anonymous**

[image: Unknown's avatar]

It is not clear from the statement of the conjecture (both here and in the arXiv paper) if the number of solutions to (1) is dependent on [image: t] (i.e. [image: O_t(1)]) or is uniformly bounded wrt [image: t].

*[Uniformly bounded in [image: t], otherwise we would have used [image: O_t(1)] as in Section 1.5 of the paper. -T]*

[Reply][479]

[13 June, 2021 at 1:44 am][480]

**Anonymous**

[image: Unknown's avatar]

The upper bound of two here for the number of solutions in the region (8)
should be changed to
The upper bound of two here for the number of solutions in the region (2)
perhaps?

*[Corrected, thanks – T.]*

[Reply][481]

[13 June, 2021 at 4:31 am][482]

**Anonymous**

[image: Unknown's avatar]

I don’t believe any random ways,

[Reply][483]

[15 June, 2021 at 5:02 pm][484]

**[JSE][485]**

[image: JSE's avatar]

The part of the argument where a set of integer points on a real-analytic subvariety (in this case three points on a curve) can’t cluster together too closely because the area of the simplex they determine would be too small (but also nonzero) feels reminiscent of the work of Bombieri and Pila, which also gives bounds for the number of integer points on a curve with bounded coordinates, those bounds being uniform in the curve in the same way your bounds are uniform in t. Did you have this stuff in mind and do you think there’s any relation?

[Reply][486]

[16 June, 2021 at 10:06 am][487]

**[Terence Tao][43]**

[image: Terence Tao's avatar]

Nice observation! We were not directly inspired by the Bombieri–Pila determinant method (the argument we use comes instead from a paper of Kane) but now that you mention it, there is definitely a similarity that we will mention in the next revision of the ms.

This does raise the possibility though that it might be possible to use the determinant method (in either the Archimedean or non-Archimedean form) to improve the upper bound for the total number of solutions to [image: \binom{n}{m} = t]; the best bound currently is [image: O( \log t \log\log\log t / (\log\log t)^3)], [due to Kane][28], and relying primarily on derivative estimates for this real-analytic curve. There the problem comes more from the edge of Pascal’s triangle than the interior, and I don’t think the rest of the methods in our paper are directly useful for this problem, but perhaps it is something for an expert in the determinant method to take a look at. (The key difficulty would be to get good quantitative estimates on the number of intersection points between the solution set [image: \{ (n,m) \in {\bf N}: \binom{n}{m} = t \}] and an algebraic curve of a given degree.)

[Reply][488]

[15 June, 2021 at 5:12 pm][489]

**[Aditya Guha Roy][490]**

[image: Aditya Guha Roy's avatar]

Reblogged this on [Aditya Guha Roy's weblog][491].

[Reply][492]

[17 June, 2021 at 3:35 pm][493]

**[duck_master][494]**

[image: duck_master's avatar]

In retrospect, the idea of comparing the valuations for a *random* prime number is extremely clever. (I had thought about comparing valuations before; however, I initially tried studying [image: p = 2, 3, 5], but I gave up because this has to do with base-2, base-3, base-5, etc. expansions, and these don’t generally relate simply to each other.)

Also, to simplify the proof: you could sample your choice of [image: p] for the application of valuation-comparison with probability [image: \propto\Lambda(p)]. On the “back-end” (the actual computation of the correlations), this gets rid of the now-unnecessary summation-by-parts on (in the latest version as of the time of writing) the top of page 22, which serves as the transition from naïve uniform sampling to my proposed version of sampling; on the “front-end” (the application of the correlations to restricting solutions of [image: \binom{n}{m} = \binom{n'}{m'} = t]), this is perfectly okay because the failure probability of the identity is at most [image: \approx\frac{\log P}{P}] and the difference of the two sides in cases of failure is at most [image: \approx\log P] anyways, which introduces a perfectly-manageable error term of [image: \approx\frac{\log^2 P}{P}] for the correlation equation.

[Reply][495]

[19 June, 2021 at 10:20 am][496]

**[Terence Tao][43]**

[image: Terence Tao's avatar]

Yes, these two sampling methods are basically equivalent and which one to use is mostly a matter of personal preference. The weighting [image: \Lambda] is often more convenient in proving the estimates, but the naive weighting involving primes drawn at random is conceptually simpler and is often the formulation used in describing many theorems or conjectures about the primes.

[Reply][497]

[18 June, 2021 at 12:00 pm][498]

**William Verreault**

[image: William Verreault's avatar]

I would like to know where your motivation to work on Singmaster’s conjecture came from since it is not as well-known as other conjectures. Did it come from your co-authors? If so, what was their motivation to look at Singmaster’s conjecture? Were you motivated by something else first?

I know you said in another comment that these arguments evolved from trying to generalize arguments that use the prime factorization of [image: \binom{n}{m}], but did you find Kane’s ”archimedean” approach first and then figured out a way to improve the proof with non-archimedean arguments?

[Reply][499]

[19 June, 2021 at 10:49 am][500]

**[Terence Tao][43]**

[image: Terence Tao's avatar]

The five of us are working on a related project involving exponential sums over primes that we hope to finalise soon. At one point in that project, one of us realised a possible connection of our work to Singmaster’s conjecture, although it turned out in the end that we were able to get our results using just the standard Vinogradov estimates on exponential sums on primes rather than the ones we have been working on.

The connection between equidistribution properties over primes (or equivalently, exponential sums over primes) and Singmaster started with the basic observation that when [image: 1 \leq m \leq n/2], the binomial coefficient [image: \binom{n}{m}] is divisible by every prime between [image: n-m+1] and [image: n], but not divisible by any prime larger than [image: n]. This is already enough to get decent results in the regime [image: \varepsilon n \leq m \leq n/2] (and was already exploited in an old paper of Abbott, Erdos, and Hansen), though for much smaller values of [image: m] this is less useful as the interval [image: [n-m+1,n]] is too short to provably contain primes. Our starting point was then the heuristic variant of the above observation (say in the region [image: n^{1/2+\varepsilon} \leq m \leq n/2] to avoid dealing with contributions of powers of primes) that [image: \binom{n}{m}] tended to be divisible by most primes in [image: [m,(1+\varepsilon) m]] but very few primes in [image: [(1-\varepsilon) m,m]], and this could be used to separate [image: \binom{n}{m}] from [image: \binom{n'}{m'}], for instance if [image: (1+\varepsilon/2)m \leq m' \leq (1+\varepsilon)m]. This idea then went through several iterations and refinements (for instance we mostly started with first moment estimates on fractional parts [image: \{ \frac{n}{p}\}, \{ \frac{m}{p}\}] and only later realised the utility of second moment estimates, i.e., correlation estimates) until reaching the current form.

[Reply][501]

[19 June, 2021 at 6:29 pm][502]

**Richard**

[image: Richard's avatar]

Thanks for both this comment and your reponse. It’s so interesting to glimpse insights into these (partial? Partial? PARTIAL? More than I could ever dream of!) results are realised, and how collaborations alight on them.

[Reply][503]

[21 June, 2021 at 11:28 am][504]

**William Verreault**

[image: William Verreault's avatar]

Thank you for the very detailed answer. It is always nice to have insight into where these new ideas come from!

This basic observation on the divisibility of [image: \binom{n}{m}] makes me think that these new techniques can’t help when considering the similar question on solutions to n!m!=t (as studied by Kane using the same Archimedean arguments in ”On the number of ways of writing t as a product of factorials”). Is that right?

To be more precise, he proved that the [image: \limsup_{t\to\infty}] of the number of solutions to the previous equation is 6, but conjectured it is the maximum, and I would find it interesting to see if this can be improved using your ideas (whether by obtaining effective bounds on ”large values of t” that could help numerically verify this conjecture or by obtaining similar results for n_1!…n_k!=t).

[Reply][505]

[21 June, 2021 at 5:48 pm][506]

**[Terence Tao][43]**

[image: Terence Tao's avatar]

For the equation [image: n! m! = t] studied by Kane, as well as the similar equation [image: n!/m! = t] studied in the last section of our paper, it seems the [image: 2] -valuation [image: \nu_2] already gives quite a lot of information; for [image: n!/m! = t] we experimented with working with more general [image: p] -valuations [image: \nu_p] as we did for [image: \binom{n}{m} = t], but the information we could extract from the other valuations was not as strong as what one could already get using [image: \nu_2]. Similarly, in Kane’s paper it seems the [image: 2] -valuation already pinpoints [image: n+m] to an accuracy of [image: O(\log\log t)], which looks much better than what one could hope to accomplish through other valuations.

[Reply][507]

[27 June, 2021 at 8:24 am][508]

**[Healthy Social Media, Secrets of Pascal’s Triangle and Venus’ Tectonics – Phil Beaudoin][509]**

[image: Unknown's avatar]

[…] “ I have no idea which number it is, but it probably appears infinitely many times. ” Well, thanks to Terrence Tao and Waverly, I learned this week about the Singmaster’s conjecture which says that no number […]

[Reply][510]

[30 June, 2021 at 7:15 am][511]

**Glenn Wouda**

[image: Glenn Wouda's avatar]

Dear professor Tao, I am trying to get to the errata for your book “Analysis I (third edition)” but the page [https://terrytao.wordpress.com/books/analysis-i/][61] freezes and there is a pop-up saying that the the page is waiting to load.

I have tried on several occasions and also with several different browsers but the problem persists.

Having the errata available would help me a lot while reading and studying your book.

Thanks in advance

*[I have changed the comment settings to only display the most recent 50 comments, which seems to alleviate this loading issue -T.]*

[Reply][512]

### Leave a comment [Cancel reply][513]

### For commenters

To enter in LaTeX in comments, use $latex *<Your LaTeX code>*$ (without the < and > signs, of course; in fact, these signs should be avoided as they can cause formatting errors). Also, backslashes \ need to be doubled as \\. See the [about page][2] for details and for other commenting policy.

[&laquo; Goursat and Furstenberg-Weiss type lemmas][514]

[Quantitative bounds for Gowers uniformity of the Mobius and von Mangoldt functions &raquo;][515]

[Blog at WordPress.com.][516] Ben Eastaugh and Chris Sternal-Johnson.

[Subscribe to feed.][8]

- [Comment][517]
- [Reblog][518]
- [Subscribe][518] [Subscribed][518]

  - [What's new][519]

  -

Already have a WordPress.com account? [Log in now.][520]

-

  - [What's new][519]
  - [Subscribe][518] [Subscribed][518]
  - [Sign up][521]
  - [Log in][520]
  - [Copy shortlink][522]
  - [Report this content][523]
  - [View post in Reader][524]
  - [Manage subscriptions][525]
  - [Collapse this bar][518]

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
[10]: https://terrytao.wordpress.com/category/paper/
[11]: https://terrytao.wordpress.com/tag/binomial-coefficients/
[12]: https://terrytao.wordpress.com/tag/exponential-sums/
[13]: https://terrytao.wordpress.com/tag/joni-teravainen/
[14]: https://terrytao.wordpress.com/tag/kaisa-matomaki/
[15]: https://terrytao.wordpress.com/tag/maksym-radziwill/
[16]: https://terrytao.wordpress.com/tag/singmasters-conjecture/
[17]: https://terrytao.wordpress.com/tag/xuancheng-shao/
[18]: https://terrytao.wordpress.com/author/teorth/
[19]: https://users.utu.fi/ksmato/
[20]: http://www.its.caltech.edu/~maksym/
[21]: https://math.as.uky.edu/users/xsh228
[22]: https://sites.google.com/view/joniteravainen/
[23]: https://arxiv.org/abs/2106.03335
[24]: https://en.wikipedia.org/wiki/Singmaster%27s_conjecture
[25]: https://mathscinet.ams.org/mathscinet-getitem?mr=1689495
[26]: https://en.wikipedia.org/wiki/Siegel%27s_theorem_on_integral_points
[27]: https://en.wikipedia.org/wiki/Archimedean_property
[28]: https://mathscinet.ams.org/mathscinet-getitem?mr=2373115
[29]: https://en.wikipedia.org/wiki/Pick%27s_theorem
[30]: https://en.wikipedia.org/wiki/P-adic_order
[31]: https://en.wikipedia.org/wiki/Legendre%27s_formula
[32]: https://en.wikipedia.org/wiki/Falling_and_rising_factorials
[33]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#print?share=print
[34]: mailto:?subject=%5BShared%20Post%5D%20Singmaster%27s%20conjecture%20in%20the%20interior%20of%20Pascal%27s%20triangle#038;body=https%3A%2F%2Fterrytao.wordpress.com%2F2021%2F06%2F07%2Fsingmasters-conjecture-in-the-interior-of-pascals-triangle%2F&#038;share=email
[35]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?share=twitter
[36]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?share=facebook
[37]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?share=reddit
[38]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?share=pinterest
[39]: https://terrytao.wordpress.com/2026/08/12/a-digestion-of-the-proof-of-sendovs-conjecture/comment-page-1/#comment-693888
[40]: https://terrytao.wordpress.com/2026/08/12/a-digestion-of-the-proof-of-sendovs-conjecture/
[41]: https://terrytao.wordpress.com/2020/12/08/sendovs-conjecture-for-sufficiently-high-degree-polynomials/comment-page-1/#comment-693886
[42]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693885
[43]: http://www.math.ucla.edu/~tao
[44]: https://terrytao.wordpress.com/2016/10/18/246a-notes-5-conformal-mapping/comment-page-1/#comment-693883
[45]: https://terrytao.wordpress.com/2016/10/18/246a-notes-5-conformal-mapping/comment-page-1/#comment-693882
[46]: https://terrytao.wordpress.com/books/analysis-i/comment-page-17/#comment-693880
[47]: https://terrytao.wordpress.com/2012/12/03/the-spectral-proof-of-the-szemeredi-regularity-lemma/comment-page-1/#comment-693879
[48]: https://terrytao.wordpress.com/books/analysis-i/comment-page-17/#comment-693878
[49]: https://terrytao.wordpress.com/2010/10/30/245a-notes-6-outer-measures-pre-measures-and-product-measures/comment-page-3/#comment-693877
[50]: https://terrytao.wordpress.com/2010/10/30/245a-notes-6-outer-measures-pre-measures-and-product-measures/comment-page-3/#comment-693875
[51]: https://terrytao.wordpress.com/2010/10/16/245a-notes-5-differentiation-theorems/comment-page-4/#comment-693874
[52]: https://terrytao.wordpress.com/2016/10/18/246a-notes-5-conformal-mapping/comment-page-1/#comment-693873
[53]: http://timktitarev.wordpress.com
[54]: https://terrytao.wordpress.com/2026/08/06/a-partial-digestion-of-the-hrt-counterexample/comment-page-1/#comment-693872
[55]: https://terrytao.wordpress.com/2026/08/06/a-partial-digestion-of-the-hrt-counterexample/comment-page-1/#comment-693871
[56]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693870
[57]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/
[58]: https://terrytao.wordpress.com/2026/08/06/a-partial-digestion-of-the-hrt-counterexample/
[59]: https://terrytao.wordpress.com/2026/06/16/third-sair-competition-inverse-galois-challenge/
[60]: https://terrytao.wordpress.com/career-advice/work-hard/
[61]: https://terrytao.wordpress.com/books/analysis-i/
[62]: https://terrytao.wordpress.com/2025/02/25/the-three-dimensional-kakeya-conjecture-after-wang-and-zahl/
[63]: https://terrytao.wordpress.com/2026/08/
[64]: https://terrytao.wordpress.com/2026/07/
[65]: https://terrytao.wordpress.com/2026/06/
[66]: https://terrytao.wordpress.com/2026/05/
[67]: https://terrytao.wordpress.com/2026/03/
[68]: https://terrytao.wordpress.com/2026/02/
[69]: https://terrytao.wordpress.com/2026/01/
[70]: https://terrytao.wordpress.com/2025/12/
[71]: https://terrytao.wordpress.com/2025/11/
[72]: https://terrytao.wordpress.com/2025/09/
[73]: https://terrytao.wordpress.com/2025/08/
[74]: https://terrytao.wordpress.com/2025/07/
[75]: https://terrytao.wordpress.com/2025/06/
[76]: https://terrytao.wordpress.com/2025/05/
[77]: https://terrytao.wordpress.com/2025/04/
[78]: https://terrytao.wordpress.com/2025/03/
[79]: https://terrytao.wordpress.com/2025/02/
[80]: https://terrytao.wordpress.com/2025/01/
[81]: https://terrytao.wordpress.com/2024/12/
[82]: https://terrytao.wordpress.com/2024/11/
[83]: https://terrytao.wordpress.com/2024/10/
[84]: https://terrytao.wordpress.com/2024/09/
[85]: https://terrytao.wordpress.com/2024/08/
[86]: https://terrytao.wordpress.com/2024/07/
[87]: https://terrytao.wordpress.com/2024/06/
[88]: https://terrytao.wordpress.com/2024/05/
[89]: https://terrytao.wordpress.com/2024/04/
[90]: https://terrytao.wordpress.com/2024/03/
[91]: https://terrytao.wordpress.com/2023/12/
[92]: https://terrytao.wordpress.com/2023/11/
[93]: https://terrytao.wordpress.com/2023/10/
[94]: https://terrytao.wordpress.com/2023/09/
[95]: https://terrytao.wordpress.com/2023/08/
[96]: https://terrytao.wordpress.com/2023/06/
[97]: https://terrytao.wordpress.com/2023/05/
[98]: https://terrytao.wordpress.com/2023/04/
[99]: https://terrytao.wordpress.com/2023/03/
[100]: https://terrytao.wordpress.com/2023/02/
[101]: https://terrytao.wordpress.com/2023/01/
[102]: https://terrytao.wordpress.com/2022/12/
[103]: https://terrytao.wordpress.com/2022/11/
[104]: https://terrytao.wordpress.com/2022/10/
[105]: https://terrytao.wordpress.com/2022/09/
[106]: https://terrytao.wordpress.com/2022/07/
[107]: https://terrytao.wordpress.com/2022/06/
[108]: https://terrytao.wordpress.com/2022/05/
[109]: https://terrytao.wordpress.com/2022/04/
[110]: https://terrytao.wordpress.com/2022/03/
[111]: https://terrytao.wordpress.com/2022/02/
[112]: https://terrytao.wordpress.com/2022/01/
[113]: https://terrytao.wordpress.com/2021/12/
[114]: https://terrytao.wordpress.com/2021/11/
[115]: https://terrytao.wordpress.com/2021/10/
[116]: https://terrytao.wordpress.com/2021/09/
[117]: https://terrytao.wordpress.com/2021/08/
[118]: https://terrytao.wordpress.com/2021/07/
[119]: https://terrytao.wordpress.com/2021/06/
[120]: https://terrytao.wordpress.com/2021/05/
[121]: https://terrytao.wordpress.com/2021/02/
[122]: https://terrytao.wordpress.com/2021/01/
[123]: https://terrytao.wordpress.com/2020/12/
[124]: https://terrytao.wordpress.com/2020/11/
[125]: https://terrytao.wordpress.com/2020/10/
[126]: https://terrytao.wordpress.com/2020/09/
[127]: https://terrytao.wordpress.com/2020/08/
[128]: https://terrytao.wordpress.com/2020/07/
[129]: https://terrytao.wordpress.com/2020/06/
[130]: https://terrytao.wordpress.com/2020/05/
[131]: https://terrytao.wordpress.com/2020/04/
[132]: https://terrytao.wordpress.com/2020/03/
[133]: https://terrytao.wordpress.com/2020/02/
[134]: https://terrytao.wordpress.com/2020/01/
[135]: https://terrytao.wordpress.com/2019/12/
[136]: https://terrytao.wordpress.com/2019/11/
[137]: https://terrytao.wordpress.com/2019/09/
[138]: https://terrytao.wordpress.com/2019/08/
[139]: https://terrytao.wordpress.com/2019/07/
[140]: https://terrytao.wordpress.com/2019/06/
[141]: https://terrytao.wordpress.com/2019/05/
[142]: https://terrytao.wordpress.com/2019/04/
[143]: https://terrytao.wordpress.com/2019/03/
[144]: https://terrytao.wordpress.com/2019/02/
[145]: https://terrytao.wordpress.com/2019/01/
[146]: https://terrytao.wordpress.com/2018/12/
[147]: https://terrytao.wordpress.com/2018/11/
[148]: https://terrytao.wordpress.com/2018/10/
[149]: https://terrytao.wordpress.com/2018/09/
[150]: https://terrytao.wordpress.com/2018/08/
[151]: https://terrytao.wordpress.com/2018/07/
[152]: https://terrytao.wordpress.com/2018/06/
[153]: https://terrytao.wordpress.com/2018/05/
[154]: https://terrytao.wordpress.com/2018/04/
[155]: https://terrytao.wordpress.com/2018/03/
[156]: https://terrytao.wordpress.com/2018/02/
[157]: https://terrytao.wordpress.com/2018/01/
[158]: https://terrytao.wordpress.com/2017/12/
[159]: https://terrytao.wordpress.com/2017/11/
[160]: https://terrytao.wordpress.com/2017/10/
[161]: https://terrytao.wordpress.com/2017/09/
[162]: https://terrytao.wordpress.com/2017/08/
[163]: https://terrytao.wordpress.com/2017/07/
[164]: https://terrytao.wordpress.com/2017/06/
[165]: https://terrytao.wordpress.com/2017/05/
[166]: https://terrytao.wordpress.com/2017/04/
[167]: https://terrytao.wordpress.com/2017/03/
[168]: https://terrytao.wordpress.com/2017/02/
[169]: https://terrytao.wordpress.com/2017/01/
[170]: https://terrytao.wordpress.com/2016/12/
[171]: https://terrytao.wordpress.com/2016/11/
[172]: https://terrytao.wordpress.com/2016/10/
[173]: https://terrytao.wordpress.com/2016/09/
[174]: https://terrytao.wordpress.com/2016/08/
[175]: https://terrytao.wordpress.com/2016/07/
[176]: https://terrytao.wordpress.com/2016/06/
[177]: https://terrytao.wordpress.com/2016/05/
[178]: https://terrytao.wordpress.com/2016/04/
[179]: https://terrytao.wordpress.com/2016/03/
[180]: https://terrytao.wordpress.com/2016/02/
[181]: https://terrytao.wordpress.com/2016/01/
[182]: https://terrytao.wordpress.com/2015/12/
[183]: https://terrytao.wordpress.com/2015/11/
[184]: https://terrytao.wordpress.com/2015/10/
[185]: https://terrytao.wordpress.com/2015/09/
[186]: https://terrytao.wordpress.com/2015/08/
[187]: https://terrytao.wordpress.com/2015/07/
[188]: https://terrytao.wordpress.com/2015/06/
[189]: https://terrytao.wordpress.com/2015/05/
[190]: https://terrytao.wordpress.com/2015/04/
[191]: https://terrytao.wordpress.com/2015/03/
[192]: https://terrytao.wordpress.com/2015/02/
[193]: https://terrytao.wordpress.com/2015/01/
[194]: https://terrytao.wordpress.com/2014/12/
[195]: https://terrytao.wordpress.com/2014/11/
[196]: https://terrytao.wordpress.com/2014/10/
[197]: https://terrytao.wordpress.com/2014/09/
[198]: https://terrytao.wordpress.com/2014/08/
[199]: https://terrytao.wordpress.com/2014/07/
[200]: https://terrytao.wordpress.com/2014/06/
[201]: https://terrytao.wordpress.com/2014/05/
[202]: https://terrytao.wordpress.com/2014/04/
[203]: https://terrytao.wordpress.com/2014/03/
[204]: https://terrytao.wordpress.com/2014/02/
[205]: https://terrytao.wordpress.com/2014/01/
[206]: https://terrytao.wordpress.com/2013/12/
[207]: https://terrytao.wordpress.com/2013/11/
[208]: https://terrytao.wordpress.com/2013/10/
[209]: https://terrytao.wordpress.com/2013/09/
[210]: https://terrytao.wordpress.com/2013/08/
[211]: https://terrytao.wordpress.com/2013/07/
[212]: https://terrytao.wordpress.com/2013/06/
[213]: https://terrytao.wordpress.com/2013/05/
[214]: https://terrytao.wordpress.com/2013/04/
[215]: https://terrytao.wordpress.com/2013/03/
[216]: https://terrytao.wordpress.com/2013/02/
[217]: https://terrytao.wordpress.com/2013/01/
[218]: https://terrytao.wordpress.com/2012/12/
[219]: https://terrytao.wordpress.com/2012/11/
[220]: https://terrytao.wordpress.com/2012/10/
[221]: https://terrytao.wordpress.com/2012/09/
[222]: https://terrytao.wordpress.com/2012/08/
[223]: https://terrytao.wordpress.com/2012/07/
[224]: https://terrytao.wordpress.com/2012/06/
[225]: https://terrytao.wordpress.com/2012/05/
[226]: https://terrytao.wordpress.com/2012/04/
[227]: https://terrytao.wordpress.com/2012/03/
[228]: https://terrytao.wordpress.com/2012/02/
[229]: https://terrytao.wordpress.com/2012/01/
[230]: https://terrytao.wordpress.com/2011/12/
[231]: https://terrytao.wordpress.com/2011/11/
[232]: https://terrytao.wordpress.com/2011/10/
[233]: https://terrytao.wordpress.com/2011/09/
[234]: https://terrytao.wordpress.com/2011/08/
[235]: https://terrytao.wordpress.com/2011/07/
[236]: https://terrytao.wordpress.com/2011/06/
[237]: https://terrytao.wordpress.com/2011/05/
[238]: https://terrytao.wordpress.com/2011/04/
[239]: https://terrytao.wordpress.com/2011/03/
[240]: https://terrytao.wordpress.com/2011/02/
[241]: https://terrytao.wordpress.com/2011/01/
[242]: https://terrytao.wordpress.com/2010/12/
[243]: https://terrytao.wordpress.com/2010/11/
[244]: https://terrytao.wordpress.com/2010/10/
[245]: https://terrytao.wordpress.com/2010/09/
[246]: https://terrytao.wordpress.com/2010/08/
[247]: https://terrytao.wordpress.com/2010/07/
[248]: https://terrytao.wordpress.com/2010/06/
[249]: https://terrytao.wordpress.com/2010/05/
[250]: https://terrytao.wordpress.com/2010/04/
[251]: https://terrytao.wordpress.com/2010/03/
[252]: https://terrytao.wordpress.com/2010/02/
[253]: https://terrytao.wordpress.com/2010/01/
[254]: https://terrytao.wordpress.com/2009/12/
[255]: https://terrytao.wordpress.com/2009/11/
[256]: https://terrytao.wordpress.com/2009/10/
[257]: https://terrytao.wordpress.com/2009/09/
[258]: https://terrytao.wordpress.com/2009/08/
[259]: https://terrytao.wordpress.com/2009/07/
[260]: https://terrytao.wordpress.com/2009/06/
[261]: https://terrytao.wordpress.com/2009/05/
[262]: https://terrytao.wordpress.com/2009/04/
[263]: https://terrytao.wordpress.com/2009/03/
[264]: https://terrytao.wordpress.com/2009/02/
[265]: https://terrytao.wordpress.com/2009/01/
[266]: https://terrytao.wordpress.com/2008/12/
[267]: https://terrytao.wordpress.com/2008/11/
[268]: https://terrytao.wordpress.com/2008/10/
[269]: https://terrytao.wordpress.com/2008/09/
[270]: https://terrytao.wordpress.com/2008/08/
[271]: https://terrytao.wordpress.com/2008/07/
[272]: https://terrytao.wordpress.com/2008/06/
[273]: https://terrytao.wordpress.com/2008/05/
[274]: https://terrytao.wordpress.com/2008/04/
[275]: https://terrytao.wordpress.com/2008/03/
[276]: https://terrytao.wordpress.com/2008/02/
[277]: https://terrytao.wordpress.com/2008/01/
[278]: https://terrytao.wordpress.com/2007/12/
[279]: https://terrytao.wordpress.com/2007/11/
[280]: https://terrytao.wordpress.com/2007/10/
[281]: https://terrytao.wordpress.com/2007/09/
[282]: https://terrytao.wordpress.com/2007/08/
[283]: https://terrytao.wordpress.com/2007/07/
[284]: https://terrytao.wordpress.com/2007/06/
[285]: https://terrytao.wordpress.com/2007/05/
[286]: https://terrytao.wordpress.com/2007/04/
[287]: https://terrytao.wordpress.com/2007/03/
[288]: https://terrytao.wordpress.com/2007/02/
[289]: https://terrytao.wordpress.com/category/expository/
[290]: https://terrytao.wordpress.com/category/expository/tricks/
[291]: https://terrytao.wordpress.com/category/guest-blog/
[292]: https://terrytao.wordpress.com/category/mathematics/
[293]: https://terrytao.wordpress.com/category/mathematics/mathac/
[294]: https://terrytao.wordpress.com/category/mathematics/mathag/
[295]: https://terrytao.wordpress.com/category/mathematics/mathap/
[296]: https://terrytao.wordpress.com/category/mathematics/mathat/
[297]: https://terrytao.wordpress.com/category/mathematics/mathca/
[298]: https://terrytao.wordpress.com/category/mathematics/mathco/
[299]: https://terrytao.wordpress.com/category/mathematics/mathct/
[300]: https://terrytao.wordpress.com/category/mathematics/mathcv/
[301]: https://terrytao.wordpress.com/category/mathematics/mathdg/
[302]: https://terrytao.wordpress.com/category/mathematics/mathds/
[303]: https://terrytao.wordpress.com/category/mathematics/mathfa/
[304]: https://terrytao.wordpress.com/category/mathematics/mathgm/
[305]: https://terrytao.wordpress.com/category/mathematics/mathgn/
[306]: https://terrytao.wordpress.com/category/mathematics/mathgr/
[307]: https://terrytao.wordpress.com/category/mathematics/mathgt/
[308]: https://terrytao.wordpress.com/category/mathematics/mathho/
[309]: https://terrytao.wordpress.com/category/mathematics/mathit/
[310]: https://terrytao.wordpress.com/category/mathematics/mathlo/
[311]: https://terrytao.wordpress.com/category/mathematics/mathmg/
[312]: https://terrytao.wordpress.com/category/mathematics/mathmp/
[313]: https://terrytao.wordpress.com/category/mathematics/mathna/
[314]: https://terrytao.wordpress.com/category/mathematics/mathoa/
[315]: https://terrytao.wordpress.com/category/mathematics/mathpr/
[316]: https://terrytao.wordpress.com/category/mathematics/mathqa/
[317]: https://terrytao.wordpress.com/category/mathematics/mathra/
[318]: https://terrytao.wordpress.com/category/mathematics/mathrt/
[319]: https://terrytao.wordpress.com/category/mathematics/mathsg/
[320]: https://terrytao.wordpress.com/category/mathematics/mathsp/
[321]: https://terrytao.wordpress.com/category/mathematics/mathst/
[322]: https://terrytao.wordpress.com/category/non-technical/
[323]: https://terrytao.wordpress.com/category/non-technical/admin/
[324]: https://terrytao.wordpress.com/category/non-technical/advertising/
[325]: https://terrytao.wordpress.com/category/non-technical/diversions-non-technical/
[326]: https://terrytao.wordpress.com/category/non-technical/media/
[327]: https://terrytao.wordpress.com/category/non-technical/media/journals/
[328]: https://terrytao.wordpress.com/category/non-technical/obituary/
[329]: https://terrytao.wordpress.com/category/opinion/
[330]: https://terrytao.wordpress.com/category/paper/book/
[331]: https://terrytao.wordpress.com/category/paper/companion/
[332]: https://terrytao.wordpress.com/category/paper/update/
[333]: https://terrytao.wordpress.com/category/question/
[334]: https://terrytao.wordpress.com/category/question/polymath/
[335]: https://terrytao.wordpress.com/category/talk/
[336]: https://terrytao.wordpress.com/category/talk/dls/
[337]: https://terrytao.wordpress.com/category/teaching/
[338]: https://terrytao.wordpress.com/category/teaching/245a-real-analysis/
[339]: https://terrytao.wordpress.com/category/teaching/245b-real-analysis/
[340]: https://terrytao.wordpress.com/category/teaching/245c-real-analysis/
[341]: https://terrytao.wordpress.com/category/teaching/246a-complex-analysis/
[342]: https://terrytao.wordpress.com/category/teaching/246b-complex-analysis/
[343]: https://terrytao.wordpress.com/category/teaching/246c-complex-analysis/
[344]: https://terrytao.wordpress.com/category/teaching/247b-classical-fourier-analysis/
[345]: https://terrytao.wordpress.com/category/teaching/254a-analytic-prime-number-theory/
[346]: https://terrytao.wordpress.com/category/teaching/254a-ergodic-theory/
[347]: https://terrytao.wordpress.com/category/teaching/254a-hilberts-fifth-problem/
[348]: https://terrytao.wordpress.com/category/teaching/254a-incompressible-fluid-equations/
[349]: https://terrytao.wordpress.com/category/teaching/254a-random-matrices/
[350]: https://terrytao.wordpress.com/category/teaching/254b-expansion-in-groups/
[351]: https://terrytao.wordpress.com/category/teaching/254b-higher-order-fourier-analysis/
[352]: https://terrytao.wordpress.com/category/teaching/255b-incompressible-euler-equations/
[353]: https://terrytao.wordpress.com/category/teaching/275a-probability-theory/
[354]: https://terrytao.wordpress.com/category/teaching/285g-poincare-conjecture/
[355]: https://terrytao.wordpress.com/category/teaching/logic-reading-seminar/
[356]: https://terrytao.wordpress.com/category/the-sciences/
[357]: https://terrytao.wordpress.com/category/travel/
[358]: https://terrytao.wordpress.com/tag/additive-combinatorics/
[359]: https://terrytao.wordpress.com/tag/approximate-groups/
[360]: https://terrytao.wordpress.com/tag/arithmetic-progressions/
[361]: https://terrytao.wordpress.com/tag/artificial-intelligence/
[362]: https://terrytao.wordpress.com/tag/ben-green/
[363]: https://terrytao.wordpress.com/tag/cauchy-schwarz/
[364]: https://terrytao.wordpress.com/tag/cayley-graphs/
[365]: https://terrytao.wordpress.com/tag/central-limit-theorem/
[366]: https://terrytao.wordpress.com/tag/chowla-conjecture/
[367]: https://terrytao.wordpress.com/tag/compressed-sensing/
[368]: https://terrytao.wordpress.com/tag/correspondence-principle/
[369]: https://terrytao.wordpress.com/tag/cosmic-distance-ladder/
[370]: https://terrytao.wordpress.com/tag/distributions/
[371]: https://terrytao.wordpress.com/tag/divisor-function/
[372]: https://terrytao.wordpress.com/tag/eigenvalues/
[373]: https://terrytao.wordpress.com/tag/elias-stein/
[374]: https://terrytao.wordpress.com/tag/emmanuel-breuillard/
[375]: https://terrytao.wordpress.com/tag/entropy/
[376]: https://terrytao.wordpress.com/tag/equidistribution/
[377]: https://terrytao.wordpress.com/tag/erdos/
[378]: https://terrytao.wordpress.com/tag/ergodic-theory/
[379]: https://terrytao.wordpress.com/tag/euler-equations/
[380]: https://terrytao.wordpress.com/tag/finite-fields/
[381]: https://terrytao.wordpress.com/tag/fourier-transform/
[382]: https://terrytao.wordpress.com/tag/freimans-theorem/
[383]: https://terrytao.wordpress.com/tag/gowers-uniformity-norm/
[384]: https://terrytao.wordpress.com/tag/gowers-uniformity-norms/
[385]: https://terrytao.wordpress.com/tag/graph-theory/
[386]: https://terrytao.wordpress.com/tag/gromovs-theorem/
[387]: https://terrytao.wordpress.com/tag/gue/
[388]: https://terrytao.wordpress.com/tag/hilberts-fifth-problem/
[389]: https://terrytao.wordpress.com/tag/icm/
[390]: https://terrytao.wordpress.com/tag/incompressible-euler-equations/
[391]: https://terrytao.wordpress.com/tag/inverse-conjecture/
[392]: https://terrytao.wordpress.com/tag/kakeya-conjecture/
[393]: https://terrytao.wordpress.com/tag/lie-algebras/
[394]: https://terrytao.wordpress.com/tag/lie-groups/
[395]: https://terrytao.wordpress.com/tag/liouville-function/
[396]: https://terrytao.wordpress.com/tag/littlewood-offord-problem/
[397]: https://terrytao.wordpress.com/tag/mobius-function/
[398]: https://terrytao.wordpress.com/tag/navier-stokes-equations/
[399]: https://terrytao.wordpress.com/tag/nilpotent-groups/
[400]: https://terrytao.wordpress.com/tag/nilsequences/
[401]: https://terrytao.wordpress.com/tag/nonstandard-analysis/
[402]: https://terrytao.wordpress.com/tag/paul-erdos/
[403]: https://terrytao.wordpress.com/tag/politics/
[404]: https://terrytao.wordpress.com/tag/polymath1/
[405]: https://terrytao.wordpress.com/tag/polymath8/
[406]: https://terrytao.wordpress.com/tag/polymath15/
[407]: https://terrytao.wordpress.com/tag/polynomial-method/
[408]: https://terrytao.wordpress.com/tag/polynomials/
[409]: https://terrytao.wordpress.com/tag/prime-gaps/
[410]: https://terrytao.wordpress.com/tag/prime-numbers/
[411]: https://terrytao.wordpress.com/tag/prime-number-theorem/
[412]: https://terrytao.wordpress.com/tag/random-matrices/
[413]: https://terrytao.wordpress.com/tag/randomness/
[414]: https://terrytao.wordpress.com/tag/ratners-theorem/
[415]: https://terrytao.wordpress.com/tag/regularity-lemma/
[416]: https://terrytao.wordpress.com/tag/ricci-flow/
[417]: https://terrytao.wordpress.com/tag/riemann-zeta-function/
[418]: https://terrytao.wordpress.com/tag/schrodinger-equation/
[419]: https://terrytao.wordpress.com/tag/shannon-entropy/
[420]: https://terrytao.wordpress.com/tag/sieve-theory/
[421]: https://terrytao.wordpress.com/tag/structure/
[422]: https://terrytao.wordpress.com/tag/szemeredis-theorem/
[423]: https://terrytao.wordpress.com/tag/tamar-ziegler/
[424]: https://terrytao.wordpress.com/tag/ultrafilters/
[425]: https://terrytao.wordpress.com/tag/universality/
[426]: https://terrytao.wordpress.com/tag/van-vu/
[427]: https://terrytao.wordpress.com/tag/wave-maps/
[428]: https://terrytao.wordpress.com/tag/yitang-zhang/
[429]: https://polymathprojects.org/feed/
[430]: https://polymathprojects.org
[431]: https://polymathprojects.org/2026/04/03/polymath-news-and-ai/
[432]: https://polymathprojects.org/2021/02/20/polymath-projects-2021/
[433]: https://polymathprojects.org/2019/06/09/a-sort-of-polymath-on-a-famous-mathoverflow-problem/
[434]: https://polymathprojects.org/2019/02/03/ten-years-of-polymath/
[435]: https://polymathprojects.org/2018/10/19/updates-and-pictures/
[436]: https://polymathprojects.org/2018/04/10/polymath-proposal-finding-simpler-unit-distance-graphs-of-chromatic-number-5/
[437]: https://polymathprojects.org/2018/01/26/a-new-polymath-proposal-related-to-the-riemann-hypothesis-over-taos-blog/
[438]: https://polymathprojects.org/2018/01/26/spontaneous-polymath-14-a-success/
[439]: https://polymathprojects.org/2017/08/22/polymath-13-a-success/
[440]: https://polymathprojects.org/2017/05/15/non-transitive-dice-over-gowerss-blog/
[441]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/feed/
[442]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629583
[443]: http://math.colgate.edu/~integers/current.html
[444]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629583#respond
[445]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629612
[446]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629612#respond
[447]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629914
[448]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629914#respond
[449]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629945
[450]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629945#respond
[451]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-633131
[452]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629605
[453]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629605#respond
[454]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629608
[455]: http://yetanothermathblog.com/2016/11/26/simple-unsolved-math-problem-5/
[456]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629608#respond
[457]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629620
[458]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629620#respond
[459]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629663
[460]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629663#respond
[461]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629819
[462]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629819#respond
[463]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629633
[464]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629633#respond
[465]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629659
[466]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629659#respond
[467]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629670
[468]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629670#respond
[469]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629679
[470]: https://math.koppernigk.net/singmaster-and-pascal/
[471]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629679#respond
[472]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629695
[473]: https://blog.spp2026.de/singmasters-conjecture/
[474]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629695#respond
[475]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629707
[476]: https://members.loria.fr/ADeleforge/
[477]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629707#respond
[478]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629769
[479]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629769#respond
[480]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629835
[481]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629835#respond
[482]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629840
[483]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629840#respond
[484]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629921
[485]: http://quomodocumque.wordpress.com
[486]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629921#respond
[487]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629946
[488]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629946#respond
[489]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-629922
[490]: https://scoutmathematics.wordpress.com/
[491]: https://scoutmathematics.wordpress.com/2021/06/16/singmasters-conjecture-in-the-interior-of-pascals-triangle/
[492]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=629922#respond
[493]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-630036
[494]: https://duck-master.github.io
[495]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=630036#respond
[496]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-630323
[497]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=630323#respond
[498]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-630251
[499]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=630251#respond
[500]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-630326
[501]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=630326#respond
[502]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-630348
[503]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=630348#respond
[504]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-630508
[505]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=630508#respond
[506]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-630521
[507]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=630521#respond
[508]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-630751
[509]: http://philbeaudoin.com/2021/06/27/healthy-social-media-secrets-of-pascals-triangle-and-venus-tectonics/
[510]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=630751#respond
[511]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comment-630869
[512]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/?replytocom=630869#respond
[513]: /2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#respond
[514]: https://terrytao.wordpress.com/2021/05/07/goursat-and-furstenberg-weiss-type-lemmas/
[515]: https://terrytao.wordpress.com/2021/07/05/quantitative-bounds-for-gowers-uniformity-of-the-mobius-and-von-mangoldt-functions/
[516]: https://wordpress.com/?ref=footer_blog
[517]: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/#comments
[518]: 
[519]: https://terrytao.wordpress.com
[520]: https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fterrytao.wordpress.com%2F2021%2F06%2F07%2Fsingmasters-conjecture-in-the-interior-of-pascals-triangle%2F#038;signup_flow=account
[521]: https://wordpress.com/start/
[522]: https://wp.me/p3qzP-3f3
[523]: https://wordpress.com/abuse/?report_url=https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/
[524]: https://wordpress.com/reader/blogs/817149/posts/12465
[525]: https://subscribe.wordpress.com/
