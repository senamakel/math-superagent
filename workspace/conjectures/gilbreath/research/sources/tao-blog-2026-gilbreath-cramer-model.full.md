<!-- source: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/ | converted from HTML -->

Gilbreath’s conjecture: a Cramér random model and a deterministic analysis | What's new

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

# Gilbreath’s conjecture: a Cramér random model and a deterministic analysis

11 July, 2026 in [math.CO][9], [math.NT][10], [math.PR][11] | Tags: [Cramer's random model][12], [Gilbreath's conjecture][13], [Zach Hunter][14], [Zachary Chase][15] | by [Terence Tao][16]

[Zachary Chase][17], [Zach Hunter][18] and I have uploaded to the arXiv our preprint [Gilbreath’s conjecture: a Cramér random model and a deterministic analysis][19]. This paper is motivated by a [notorious conjecture of Gilbreath][20] (also proposed eighty years prior by Proth), which one can state as follows: if one starts with the sequence of primes and repeatedly takes absolute differences of consecutive terms, then the first term of each subsequent row is always [image: {1}]:

[image: \displaystyle  \begin{array}{ccccccccccc} 2 & & 3 & & 5 & & 7 & & 11 & & 13 \\ & 1 & & 2 & & 2 & & 4 & & 2 & \\ & & 1 & & 0 & & 2 & & 2 & \\ & & & 1 & & 2 & & 0 & & \\ & & & & 1 & & 2 & & & \\ & & & & & 1 & & & & \end{array}. ]

Coming from a PDE background, I like to think of this conjecture as a (discrete) nonlinear “wave equation” problem, where the primes are the “initial data”, the downward direction in the above pyramid is the arrow of “time”, and the “equation of motion” is that the value of the “scalar field” at any given point in “spacetime” is the absolute difference of the values of the two points directly above it. We will informally refer to solutions to such an “equation” as “Gilbreath arrays”.

Numerically, the conjecture has been verified for the first [image: {3.34 \times 10^{11}}] rows [by Odlyzko][21]. Asymptotically, the conjecture can be heuristically justified as follows. Firstly, because all primes other than [image: {2}] are odd, it is easy to see that the first term of each row is odd, while all other terms are even. Next, if one starts with the first [image: {n}] primes for some large [image: {n}] and takes initial differences, then the prime number theorem tells us that the average size of the next row is about [image: {\log n}], and [Cram&eacute;r’s conjecture][22] predicts that the maximum size should be [image: {O(\log^2 n)}]. With each new row, the maximum size can only decrease (since [image: {|a-b| \leq \max(a, b)}] for any natural numbers [image: {a,b}]), and so one would expect it likely on each row that the maximum size should drop by at least [image: {1}] (unless it has already reached [image: {2}]). Since there are [image: {n-1}] rows to go before one reaches the end, it seems extremely likely that the maximum size should drop down to at most [image: {2}] by then, at which point the result is forced from parity reasons.

However, it seems well beyond current technology to try to make these heuristics rigorous; even the first step of proving Cram&eacute;r’s conjecture is far out of reach. In our paper, we consider two more feasible directions:

- What is a realistic probabilistic model of the primes, and can one confirm the (asymptotic version of the) conjecture almost surely for such a model?
- Can one use deterministic arguments to reduce the (asymptotic) Gilbreath conjecture to more tractable looking (and heuristically plausible) statements about iterated differences of primes?

Let us first discuss the question of analyzing probabilistic models. One can strip away the first row and initialize using prime gaps [image: {p_{n+1}-p_n}] rather than primes; it is convenient to also strip away the aforementioned parity structure, by eliminating the initial gap [image: {3-2=1}], and dividing all remaining gaps by [image: {2}], so that one now works with an initial sequence [image: {\frac{p_{n+1}-p_n}{2}, n \geq 2}] with no parity bias. The conjecture is now equivalent to the first row always being [image: {\{0,1\}}] -valued:

[image: \displaystyle  \begin{array}{ccccccccccccccccc} 0 & & 0 & & 1 & & 0 & & 1 & & 0 && 1 && 2 && 0\\ & 0 & & 1 & & 1 & & 1 & & 1 && 1 && 1 && 2\\ & & 1 & & 0 & & 0 & & 0 && 0 && 0 && 1\\ & & & 1 & & 0 & & 0 & & 0 && 0 && 1\\ & & & & 1 & & 0 & & 0 && 0 && 1\\ & & & & & 1 & & 0 & & 0 && 1\\ & & & & & & 1 & & 0 && 1\\ & & & & & & & 1 && 1 \\ & & & & & & & & 0 \end{array}. ]

The Cram&eacute;r model suggests that the first [image: {n}] normalized prime gaps should behave like geometric random variables of mean about [image: {\frac{\log n}{2}}]. My co-author, [Zachary Chase][23], established an analogue of the Gilbreath conjecture for a more slowly growing model. Here is a special case of his main theorem:

**Theorem 1**Suppose the initial row entries [image: {a_n}] of a Gilbreath array are drawn independently from a uniform distribution on [image: {\{0,\dots,f(n)-1\}}] for some [image: {2 \leq f(n) \leq \frac{1}{10} \frac{\log\log n}{\log \log \log n}}]. Then almost surely, all but finitely many of the rows have a [image: {\{0,1\}}] -valued first entry.

The Cram&eacute;r model morally corresponds to a value of [image: {f(n)}] comparable to [image: {\log n}], which is too large for the above theorem to apply. However, we were able to improve the argument, basically allowing [image: {f(n)}] to be anything of size [image: {o(n)}]. Furthermore, it was not necessary that the distribution be uniform: the important hypothesis was that the distribution not be concentrated in any [image: {2}] -separated set, such as the even numbers, the odd numbers, or the multiples of [image: {3}]. (See the paper for the precise formulation of “non-concentrated”.) Such a hypothesis is needed since if for instance all initial entries were divisible by [image: {3}], then this property would propagate down the array, and it would become extremely unlikely that the initial values would remain [image: {\{0,1\}}] -valued. Our hypotheses are obeyed by the Cram&eacute;r random model, and so we obtain a heuristic confirmation of the original Gilbreath conjecture for the primes.

One can informally explain our proof of the above result as follows. We consider the portion of the array generated by the first [image: {n}] values [image: {a_1,\dots,a_n}] for some large [image: {n}]. Suppose that at some point [image: {P}] deep in this portion of the array, a value [image: {d}] that is larger than [image: {1}] is attained. Then the two values [image: {a,b}] above [image: {P}] must satisfy the equation [image: {|a-b|=d}]. So, either one of these values is at least [image: {d+1}], or one of them is [image: {d}] and the other is [image: {0}]. If one iterates this observation, one sees that [image: {P}] is the base of an upside-down triangle of [image: {\{0,d\}}] values, topped off by at least one location [image: {P'}] where the value is at least [image: {d+1}]. If one iterates that observation in turn, we see that [image: {P}] forms the base of a “tower” of upside-down triangles stacked atop each other, with the number of such triangles bounded by the maximum size of the initial data (in the “backwards light cone” of [image: {P}]). In the [image: {f(n)=o(n)}] regime, it turns out that the number (or “entropy”) of such towers is subexponential in [image: {n}]. So if we can show that each tower only can be created with an exponentially small probability, we can conclude by the standard techniques of the union bound and the Borel–Cantelli lemma.

At this point we use the following elementary observation. Suppose that some finite Gilbreath array coming from say initial data [image: {a_1,\dots,a_n}] has been generated, and consider the effect of adding a new value [image: {a_{n+1}}] to the initial data, which then triggers [image: {n}] iterations of the absolute value difference operation [image: {a \mapsto |a-c|}] for various values of [image: {c}] until one reaches the new bottom vertex of the array. This difference operation [image: {a \mapsto |a-c|}] has the property that the preimage of any [image: {2}] -separated set is still [image: {2}] -separated. Iterating this, we see that the set of values that make [image: {a_{n+1}}] iterate to a [image: {\{0,d\}}] -valued bottom vertex is also [image: {2}] -separated. So as long as the distribution of [image: {a_{n+1}}] avoids [image: {2}] -separated sets, one can iterate this observation in [image: {n}] to show that it is exponentially rare that large triangles of [image: {\{0,d\}}] -valued vertices can be created.

We also consider an asymptotic continuous random model, in which the initial data [image: {a_n}] are not natural numbers, but instead independently random non-negative real numbers with an exponential distribution, which we can normalize to have mean [image: {1}]; this heuristically is an approximate model for the Gilbreath array generated by the first [image: {n}] normalized prime gaps, after dividing by the mean [image: {\log n/2}]. In this normalized model, each entry of the [image: {k^{th}}] row ends up having the same mean [image: {c_k}]. The first few values of [image: {c_k}] can be computed explicitly

[image: \displaystyle  c_0 = 1; c_1 = 1; c_2 = \frac{7}{9}; c_3 = \frac{227}{288}.]

However, the asymptotic behavior of [image: {c_n}] remains unclear to us. We were able to show an inequality [image: {c_0 + \dots + c_n \geq \log(n+e)}] for any [image: {n}], indicating that [image: {c_k}] cannot decay faster than [image: {1/k}], but we do not know whether this is the true decay rate. In any case a decay rate of [image: {1/k}] (which is very weakly supported by numerical evidence) is consistent with the Gilbreath conjecture, as it would indicate that the Gilbreath array from the first [image: {n}] prime gaps should end up being almost entirely [image: {\{0,1\}}] -valued by merely [image: {O(\log n)}] steps, well before the [image: {n}] steps needed to reach the bottom of the array.

Now we turn to deterministic analysis of Gilbreath arrays. Suppose we found some initial data [image: {a_1,\dots,a_N}] that did not grow too quickly (e.g., one had a Cram&eacute;r-type bound [image: {a_N = O(\log^2 N)}]), but still iterated to a final value that was not [image: {\{0,1\}}]. What features of the initial data could generate such a failure of a Gilbreath-type conjecture? One way in which the conjecture could fail is if the Gilbreath iteration somehow produced a reasonably long consecutive string of zeroes (say, longer than [image: {\log^{10} N}]), as then the next few iterations would not act to decrease the magnitude of the non-zero entries bordering this string of zeroes. Such a scenario would be heuristically rate, as the parity of each element of the array can be worked out explicitly using the parity identity [image: {|a-b| = a + b \hbox{ mod } 2}], and so constant-parity sequences of length say [image: {\log^{10} N}] should be almost surely non-existent asymptotically by standard probabilistic heuristics.

Another bad scenario is if the Gilbreath iteration, after some medium number [image: {i}] of iterations, produced an extremely long consecutive block (say of length [image: {\exp(\log^{1/10} N) i}]) which was entirely [image: {\{0,d\}}] -valued for some [image: {d \geq 2}]. This block would then persist as a [image: {\{0,d\}}] -block for a large number of iterations (equal to the length of the block), thus potentially delaying for a significant time the drop-down of the maximal value to below [image: {d}]. For odd [image: {d}], one can use the parity analysis alluded to earlier to argue that the formation of such a block is extremely unlikely; but for even [image: {d}], we can only use such heuristics if we make strong assumptions of joint independence, as we did in the probabilistic analysis in our paper.

In any event, we were able to use purely elementary methods to establish an “inverse theorem” that states, roughly speaking, that the above two scenarios are the *only*ways in which a Gilbreath array can fail to have a [image: {\{0,1\}}] -valued first entry. This basically arises from a more careful analysis of the towers of triangles alluded to earlier. (A previous argument involved considering ways to pack a large triangle by smaller triangles, leading to a [MathOverflow question][24] which was nicely answered by Fedja Nazarov and Anders Martinsson, but we later managed to optimize the argument to the point where the answer to this packing question was no longer needed.) So this in principle reduces the (deterministic) Gilbreath conjecture to several more tractable-looking (though complicated to state) assertions, though proving those latter statements seems well out of reach at the moment.

### Share this:

- [Print (Opens in new window) Print][25]
- [Email a link to a friend (Opens in new window) Email][26]
- More
-

- [Share on X (Opens in new window) X][27]
- [Share on Facebook (Opens in new window) Facebook][28]
- [Share on Reddit (Opens in new window) Reddit][29]
- [Share on Pinterest (Opens in new window) Pinterest][30]
-

Like Loading...

### Recent Comments

[image: Terence Tao's avatar] [31] | [Terence Tao][31] on [245A, Notes 5: Differentiation…][32] |

[image: Unknown's avatar] | Anonymous on [245A, Notes 5: Differentiation…][33] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][34] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][35] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][36] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][37] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][38] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][39] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][40] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][41] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][42] |

[image: Unknown's avatar] | Anonymous on [A digestion of the Jacobian co…][43] |

[image: Terence Tao's avatar] [31] | [Terence Tao][31] on [245A, Notes 1: Lebesgue m…][44] |

[image: Terence Tao's avatar] [31] | [Terence Tao][31] on [245A, Notes 5: Differentiation…][45] |

[image: RobertJDicks1's avatar] [46] | [RobertJDicks1][46] on [The subspace theorem approach…][47] |

### Top Posts

- [A digestion of the Jacobian conjecture counterexample][48]
- [Career advice][3]
- [The three-dimensional Kakeya conjecture, after Wang and Zahl][49]
- [About][2]
- [Work hard][50]
- [245A, Notes 5: Differentiation theorems][51]
- [On writing][4]
- [Books][5]
- [Does one have to be a genius to do maths?][52]
- [Mastodon+][6]

### Archives

- [July 2026][53] (9)
- [June 2026][54] (3)
- [May 2026][55] (1)
- [March 2026][56] (4)
- [February 2026][57] (3)
- [January 2026][58] (4)
- [December 2025][59] (5)
- [November 2025][60] (5)
- [September 2025][61] (1)
- [August 2025][62] (3)
- [July 2025][63] (1)
- [June 2025][64] (2)
- [May 2025][65] (5)
- [April 2025][66] (2)
- [March 2025][67] (1)
- [February 2025][68] (3)
- [January 2025][69] (1)
- [December 2024][70] (3)
- [November 2024][71] (4)
- [October 2024][72] (1)
- [September 2024][73] (4)
- [August 2024][74] (3)
- [July 2024][75] (3)
- [June 2024][76] (1)
- [May 2024][77] (1)
- [April 2024][78] (5)
- [March 2024][79] (1)
- [December 2023][80] (2)
- [November 2023][81] (2)
- [October 2023][82] (1)
- [September 2023][83] (3)
- [August 2023][84] (3)
- [June 2023][85] (8)
- [May 2023][86] (1)
- [April 2023][87] (1)
- [March 2023][88] (2)
- [February 2023][89] (1)
- [January 2023][90] (2)
- [December 2022][91] (3)
- [November 2022][92] (3)
- [October 2022][93] (3)
- [September 2022][94] (1)
- [July 2022][95] (3)
- [June 2022][96] (1)
- [May 2022][97] (2)
- [April 2022][98] (2)
- [March 2022][99] (5)
- [February 2022][100] (3)
- [January 2022][101] (1)
- [December 2021][102] (2)
- [November 2021][103] (2)
- [October 2021][104] (1)
- [September 2021][105] (2)
- [August 2021][106] (1)
- [July 2021][107] (3)
- [June 2021][108] (1)
- [May 2021][109] (2)
- [February 2021][110] (6)
- [January 2021][111] (2)
- [December 2020][112] (4)
- [November 2020][113] (2)
- [October 2020][114] (4)
- [September 2020][115] (5)
- [August 2020][116] (2)
- [July 2020][117] (2)
- [June 2020][118] (1)
- [May 2020][119] (2)
- [April 2020][120] (3)
- [March 2020][121] (9)
- [February 2020][122] (1)
- [January 2020][123] (3)
- [December 2019][124] (4)
- [November 2019][125] (2)
- [September 2019][126] (2)
- [August 2019][127] (3)
- [July 2019][128] (2)
- [June 2019][129] (4)
- [May 2019][130] (6)
- [April 2019][131] (4)
- [March 2019][132] (2)
- [February 2019][133] (5)
- [January 2019][134] (1)
- [December 2018][135] (6)
- [November 2018][136] (2)
- [October 2018][137] (2)
- [September 2018][138] (5)
- [August 2018][139] (3)
- [July 2018][140] (3)
- [June 2018][141] (1)
- [May 2018][142] (4)
- [April 2018][143] (4)
- [March 2018][144] (5)
- [February 2018][145] (4)
- [January 2018][146] (5)
- [December 2017][147] (5)
- [November 2017][148] (3)
- [October 2017][149] (4)
- [September 2017][150] (4)
- [August 2017][151] (5)
- [July 2017][152] (5)
- [June 2017][153] (1)
- [May 2017][154] (3)
- [April 2017][155] (2)
- [March 2017][156] (3)
- [February 2017][157] (1)
- [January 2017][158] (2)
- [December 2016][159] (2)
- [November 2016][160] (2)
- [October 2016][161] (5)
- [September 2016][162] (4)
- [August 2016][163] (4)
- [July 2016][164] (1)
- [June 2016][165] (3)
- [May 2016][166] (5)
- [April 2016][167] (2)
- [March 2016][168] (6)
- [February 2016][169] (2)
- [January 2016][170] (1)
- [December 2015][171] (4)
- [November 2015][172] (6)
- [October 2015][173] (5)
- [September 2015][174] (5)
- [August 2015][175] (4)
- [July 2015][176] (7)
- [June 2015][177] (1)
- [May 2015][178] (5)
- [April 2015][179] (4)
- [March 2015][180] (3)
- [February 2015][181] (4)
- [January 2015][182] (4)
- [December 2014][183] (6)
- [November 2014][184] (5)
- [October 2014][185] (4)
- [September 2014][186] (3)
- [August 2014][187] (4)
- [July 2014][188] (5)
- [June 2014][189] (5)
- [May 2014][190] (5)
- [April 2014][191] (2)
- [March 2014][192] (4)
- [February 2014][193] (5)
- [January 2014][194] (4)
- [December 2013][195] (4)
- [November 2013][196] (5)
- [October 2013][197] (4)
- [September 2013][198] (5)
- [August 2013][199] (1)
- [July 2013][200] (7)
- [June 2013][201] (12)
- [May 2013][202] (4)
- [April 2013][203] (2)
- [March 2013][204] (2)
- [February 2013][205] (6)
- [January 2013][206] (1)
- [December 2012][207] (4)
- [November 2012][208] (7)
- [October 2012][209] (6)
- [September 2012][210] (4)
- [August 2012][211] (3)
- [July 2012][212] (4)
- [June 2012][213] (3)
- [May 2012][214] (3)
- [April 2012][215] (4)
- [March 2012][216] (5)
- [February 2012][217] (5)
- [January 2012][218] (4)
- [December 2011][219] (8)
- [November 2011][220] (8)
- [October 2011][221] (7)
- [September 2011][222] (6)
- [August 2011][223] (8)
- [July 2011][224] (9)
- [June 2011][225] (8)
- [May 2011][226] (11)
- [April 2011][227] (3)
- [March 2011][228] (10)
- [February 2011][229] (3)
- [January 2011][230] (5)
- [December 2010][231] (5)
- [November 2010][232] (6)
- [October 2010][233] (9)
- [September 2010][234] (9)
- [August 2010][235] (3)
- [July 2010][236] (4)
- [June 2010][237] (8)
- [May 2010][238] (8)
- [April 2010][239] (8)
- [March 2010][240] (8)
- [February 2010][241] (10)
- [January 2010][242] (12)
- [December 2009][243] (11)
- [November 2009][244] (8)
- [October 2009][245] (15)
- [September 2009][246] (6)
- [August 2009][247] (13)
- [July 2009][248] (10)
- [June 2009][249] (11)
- [May 2009][250] (9)
- [April 2009][251] (11)
- [March 2009][252] (14)
- [February 2009][253] (13)
- [January 2009][254] (18)
- [December 2008][255] (8)
- [November 2008][256] (9)
- [October 2008][257] (10)
- [September 2008][258] (5)
- [August 2008][259] (6)
- [July 2008][260] (7)
- [June 2008][261] (8)
- [May 2008][262] (11)
- [April 2008][263] (12)
- [March 2008][264] (12)
- [February 2008][265] (13)
- [January 2008][266] (17)
- [December 2007][267] (10)
- [November 2007][268] (9)
- [October 2007][269] (9)
- [September 2007][270] (7)
- [August 2007][271] (9)
- [July 2007][272] (9)
- [June 2007][273] (6)
- [May 2007][274] (10)
- [April 2007][275] (11)
- [March 2007][276] (9)
- [February 2007][277] (4)

### Categories

- [expository][278] (323)

  - [tricks][279] (13)

- [guest blog][280] (10)
- [Mathematics][281] (922)

  - [math.AC][282] (9)
  - [math.AG][283] (43)
  - [math.AP][284] (115)
  - [math.AT][285] (17)
  - [math.CA][286] (196)
  - [math.CO][9] (207)
  - [math.CT][287] (9)
  - [math.CV][288] (39)
  - [math.DG][289] (37)
  - [math.DS][290] (90)
  - [math.FA][291] (24)
  - [math.GM][292] (16)
  - [math.GN][293] (21)
  - [math.GR][294] (90)
  - [math.GT][295] (17)
  - [math.HO][296] (14)
  - [math.IT][297] (13)
  - [math.LO][298] (54)
  - [math.MG][299] (48)
  - [math.MP][300] (31)
  - [math.NA][301] (26)
  - [math.NT][10] (213)
  - [math.OA][302] (22)
  - [math.PR][11] (114)
  - [math.QA][303] (6)
  - [math.RA][304] (49)
  - [math.RT][305] (21)
  - [math.SG][306] (4)
  - [math.SP][307] (48)
  - [math.ST][308] (11)

- [non-technical][309] (212)

  - [admin][310] (48)
  - [advertising][311] (81)
  - [diversions][312] (7)
  - [media][313] (14)

    - [journals][314] (3)

  - [obituary][315] (15)

- [opinion][316] (37)
- [paper][317] (272)

  - [book][318] (23)
  - [Companion][319] (13)
  - [update][320] (26)

- [question][321] (128)

  - [polymath][322] (87)

- [talk][323] (69)

  - [DLS][324] (20)

- [teaching][325] (190)

  - [245A – Real analysis][326] (11)
  - [245B – Real analysis][327] (22)
  - [245C – Real analysis][328] (6)
  - [246A – complex analysis][329] (11)
  - [246B – complex analysis][330] (5)
  - [246C – complex analysis][331] (5)
  - [247B – Classical Fourier Analysis][332] (5)
  - [254A – analytic prime number theory][333] (19)
  - [254A – ergodic theory][334] (18)
  - [254A – Hilbert's fifth problem][335] (12)
  - [254A – Incompressible fluid equations][336] (5)
  - [254A – random matrices][337] (14)
  - [254B – expansion in groups][338] (8)
  - [254B – Higher order Fourier analysis][339] (9)
  - [255B – incompressible Euler equations][340] (2)
  - [275A – probability theory][341] (6)
  - [285G – poincare conjecture][342] (20)
  - [Logic reading seminar][343] (8)

- [The sciences][344] (1)
- [travel][345] (26)

###

[additive combinatorics][346] [approximate groups][347] [arithmetic progressions][348] [Artificial Intelligence][349] [Ben Green][350] [Cauchy-Schwarz][351] [Cayley graphs][352] [central limit theorem][353] [Chowla conjecture][354] [compressed sensing][355] [correspondence principle][356] [cosmic distance ladder][357] [distributions][358] [divisor function][359] [eigenvalues][360] [Elias Stein][361] [Emmanuel Breuillard][362] [entropy][363] [equidistribution][364] [Erdos][365] [ergodic theory][366] [Euler equations][367] [exponential sums][368] [finite fields][369] [Fourier transform][370] [Freiman's theorem][371] [Gowers uniformity norm][372] [Gowers uniformity norms][373] [graph theory][374] [Gromov's theorem][375] [GUE][376] [Hilbert's fifth problem][377] [ICM][378] [incompressible Euler equations][379] [inverse conjecture][380] [Joni Teravainen][381] [Kaisa Matomaki][382] [Kakeya conjecture][383] [Lie algebras][384] [Lie groups][385] [Liouville function][386] [Littlewood-Offord problem][387] [Maksym Radziwill][388] [Mobius function][389] [Navier-Stokes equations][390] [nilpotent groups][391] [nilsequences][392] [nonstandard analysis][393] [Paul Erdos][394] [politics][395] [polymath1][396] [polymath8][397] [Polymath15][398] [polynomial method][399] [polynomials][400] [prime gaps][401] [prime numbers][402] [prime number theorem][403] [random matrices][404] [randomness][405] [Ratner's theorem][406] [regularity lemma][407] [Ricci flow][408] [Riemann zeta function][409] [Schrodinger equation][410] [Shannon entropy][411] [sieve theory][412] [structure][413] [Szemeredi's theorem][414] [Tamar Ziegler][415] [ultrafilters][416] [universality][417] [Van Vu][418] [wave maps][419] [Yitang Zhang][420]

### [image: RSS] [421] [The Polymath Blog][422]

- [Polymath News and AI][423]
- [Polymath projects 2021][424]
- [A sort of Polymath on a famous MathOverflow problem][425]
- [Ten Years of Polymath][426]
- [Updates and Pictures][427]
- [Polymath proposal: finding simpler unit distance graphs of chromatic number 5][428]
- [A new polymath proposal (related to the Riemann Hypothesis) over Tao’s blog][429]
- [Spontaneous Polymath 14 – A success!][430]
- [Polymath 13 – a success!][431]
- [Non-transitive Dice over Gowers’s Blog][432]

## 9 comments

[Comments feed for this article][433]

[13 July, 2026 at 7:31 am][434]

**Anonymous**

[image: Unknown's avatar]

Please forgive me for asking a silly question: Why can we model number theory using probability theory? Take the prime number theorem as an example. If expressed in the language of probability, it would be stated as: if we randomly pick a large number n, the probability that n is prime is approximately 1/log n. But a number can only be either prime or not, so why isn’t the probability 1/2?

[Reply][435]

[13 July, 2026 at 9:11 am][436]

**[Terence Tao][31]**

[image: Terence Tao's avatar]

The more precise claim is that while number-theoretic objects such as the set of primes are deterministic rather than random, they (at least conjecturally) exhibit strong signs of being [pseudorandom][437] in various senses. See [https://terrytao.wordpress.com/2015/01/04/254a-supplement-4-probabilistic-models-and-heuristics-for-the-primes-optional/][438] for more discussion.

[Reply][439]

[13 July, 2026 at 9:56 am][440]

**Anonymous**

[image: Unknown's avatar]

I extended the explicit computation of the constants c_i in Section 1.3 by three further values (c_4, c_5, c_6), using a sign-cone decomposition of your simplex representation with exact rational arithmetic throughout: [https://github.com/michaelmross/Gilbreath][441] (data/exact_values.json)

[Reply][442]

[13 July, 2026 at 10:53 am][443]

**[Terence Tao][31]**

[image: Terence Tao's avatar]

Thanks! We will note these extended values in the next revision of the manuscript. A quick check against our Monte Carlo calculation reveals an excellent fit.

A quick check of the OEIS indicates that neither the numerators nor denominators of this sequence are currently in that database. You might consider submitting both of these (I assume they are in lowest terms) there.

[Reply][444]

[29 July, 2026 at 6:27 pm][445]

**Michael M. Ross**

[image: Michael M. Ross's avatar]

Just published today: A397880 and A395556

[Reply][446]

[13 July, 2026 at 12:10 pm][447]

**Michael M. Ross**

[image: Michael M. Ross's avatar]

Yes, lowest terms: gcd(numerator, denominator) = 1.
OEIS submission underway.

[Reply][448]

[14 July, 2026 at 9:16 am][449]

**[Visualizing the Gilbreath expectation sequence | What's new][450]**

[image: Unknown's avatar]

[…] can illustrate this with Figure 1 from my recent paper on the Gilbreath conjecture with Chase and Hunter, reproduced […]

[Reply][451]

[24 July, 2026 at 6:21 am][452]

**Emmanuel Audigé**

[image: Emmanuel Audigé's avatar]

Subject: An exact cutoff-parity law and quantitative bound for the Cramér–Gilbreath model

Dear Professor Tao,

After reading and working carefully through your paper with Zachary Chase and Zach Hunter, I found that the two-separated concentration parameter appearing in Proposition 4.1 can be evaluated exactly for the geometric model.

More importantly, the tail replacement used in the proof has an exact parity oscillation. Substituting this exact coefficient into Proposition 4.1 yields an explicit finite-[image: n] failure bound and a computable threshold.

**Exact two-separated concentration in the geometric model**

Let [image: X] have the geometric distribution

[image: \displaystyle \mathbb P(X=k)=pq^k, \qquad q=1-p, \qquad 0 < p < 1, \qquad k\geq0,]

and define

[image: \displaystyle \Lambda_2(X) := \sup_{\substack{A\subseteq\mathbb Z_{\geq0}\\ |a-a'|\geq2\ \text{for }a\neq a'}} \mathbb P(X\in A).]

**1. Exact extremizer**

One has

[image: \displaystyle \boxed{\Lambda_2(X) = \sum_{m\geq0}pq^{2m} = \frac{1}{1+q} = \frac{1}{2-p}.}]

The unique maximizing set is

[image: \displaystyle \boxed{A=2\mathbb Z_{\geq0}.}]

Indeed, every 2-separated set contains at most one element of each pair

[image: \displaystyle \{2m,2m+1\},]

and

[image: \displaystyle pq^{2m}>pq^{2m+1}.]

Hence

[image: \displaystyle \mathbb P(X\in A) \leq \sum_{m\geq0}pq^{2m} = \frac{1}{2-p},]

with equality precisely for [image: A=2\mathbb Z_{\geq0}].

**2. Exact stability identity**

For every 2-separated set [image: A\subseteq\mathbb Z_{\geq0}],

[image: \displaystyle \boxed{\frac{1}{2-p}-\mathbb P(X\in A) = \sum_{m\geq0} pq^{2m}\left(\mathbf 1_{A\cap\{2m,2m+1\}=\varnothing} + p\,\mathbf 1_{2m+1\in A}\right).}]

Indeed, the contribution of the pair [image: \{2m,2m+1\}] to the deficit from the extremizer is

[image: \displaystyle \begin{cases} 0, & 2m\in A,\\[1mm] pq^{2m}-pq^{2m+1}=p^2q^{2m}, & 2m+1\in A,\\[1mm] pq^{2m}, & A\cap\{2m,2m+1\}=\varnothing. \end{cases}]

Thus every departure from the even extremizer has an exact probabilistic cost.

**3. Exact cutoff-parity law**

Let [image: D\geq1], and define the modified variable

[image: \displaystyle X_D = \begin{cases} X, & X\leq D,\\ \varepsilon, & X>D, \end{cases}]

where [image: \varepsilon] is independent of [image: X] and

[image: \displaystyle \mathbb P(\varepsilon=0) = \mathbb P(\varepsilon=1) = \frac12.]

Then

[image: \displaystyle \boxed{\Lambda_2(X_D) = \frac{1}{2-p}\left(1+\frac{(-1)^D}{2}pq^{D+1}\right).}]

The maximizing pattern on the support of [image: X_D] is uniquely the even pattern.

Indeed,

[image: \displaystyle \Lambda_2(X_D) = \sum_{\substack{0\leq k\leq D\\ k\ \mathrm{even}}} pq^k + \frac{q^{D+1}}2.]

Consequently,

[image: \displaystyle \boxed{\Lambda_2(X_D)-\Lambda_2(X) = \frac{(-1)^D}{2(2-p)}pq^{D+1}.}]

Thus the truncation used in the proof exhibits the exact parity oscillation

[image: \displaystyle \begin{aligned} D\ \mathrm{even} &\Longrightarrow \Lambda_2(X_D) > \Lambda_2(X),\\ D\ \mathrm{odd} &\Longrightarrow \Lambda_2(X_D) < \Lambda_2(X). \end{aligned}]

**4. Exact coefficient in the Cramér model**

For the geometric variables in the paper, let

[image: \displaystyle p_j=\frac{2}{2+\log j}, \qquad q_j=\frac{\log j}{2+\log j}.]

Then, for [image: j\geq2],

[image: \displaystyle \boxed{\rho_j = \Lambda_2(X_j) = \frac{\log j+2}{2(\log j+1)} = \frac12+\frac{1}{2(\log j+1)}.}]

Also [image: \rho_1=1]. Hence

[image: \displaystyle \boxed{\prod_{j=1}^{n}\rho_j = 2^{-(n-1)} \exp\left(\frac{n}{\log n} - \frac{n}{2\log^2 n} + O\left(\frac{n}{\log^3 n}\right)\right).}]

Indeed,

[image: \displaystyle 2\rho_j = 1+\frac{1}{1+\log j},]

and therefore

[image: \displaystyle \log(2\rho_j) = \log\left(1+\frac{1}{1+\log j}\right) = \frac{1}{\log j} - \frac{3}{2\log^2 j} + O\left(\frac{1}{\log^3j}\right).]

Using

[image: \displaystyle \sum_{j\leq n}\frac{1}{\log j} = \frac{n}{\log n} + \frac{n}{\log^2n} + O\left(\frac{n}{\log^3n}\right)]

and

[image: \displaystyle \sum_{j\leq n}\frac{1}{\log^2j} = \frac{n}{\log^2n} + O\left(\frac{n}{\log^3n}\right),]

one obtains the displayed product asymptotic.

In particular,

[image: \displaystyle \boxed{\left(\prod_{j=1}^{n}\rho_j\right)^{1/2} = 2^{-(n-1)/2} \exp\left(\frac{n}{2\log n} - \frac{n}{4\log^2n} + O\left(\frac{n}{\log^3n}\right)\right).}]

**5. Explicit finite-[image: n] Cramér–Gilbreath bound**

Let [image: a_1,\ldots,a_n] be the independent geometric variables of the Cramér model, and let

[image: \displaystyle F_n := \left\{a^{(n-1,1)}>1\right\}.]

For [image: D\geq1], replace each [image: a_j>D] independently by a fair value in [image: \{0,1\}], and leave [image: a_j] unchanged when [image: a_j\leq D]. Denote the resulting variable by [image: a_{j,D}].

Its exact two-separated concentration coefficient is

[image: \displaystyle \boxed{\rho_{j,D} = \frac{1}{2-p_j}\left(1+\frac{(-1)^D}{2}p_jq_j^{D+1}\right).}]

The original and modified Gilbreath arrays coincide whenever

[image: \displaystyle \max_{1\leq j\leq n}a_j\leq D.]

Therefore

[image: \displaystyle \mathbb P(F_n) \leq \mathbb P\left(\max_{j\leq n}a_j>D\right) + \mathbb P\left(a_D^{(n-1,1)}>1\right).]

Since

[image: \displaystyle \mathbb P(a_j>D)=q_j^{D+1}]

and [image: q_j\leq q_n] for [image: j\leq n],

[image: \displaystyle \mathbb P\left(\max_{j\leq n}a_j>D\right) \leq \sum_{j=1}^{n}q_j^{D+1} \leq nq_n^{D+1}.]

Applying Proposition 4.1 to the modified variables gives

[image: \displaystyle \boxed{\begin{aligned} \mathbb P(F_n) \leq {}& \sum_{j=1}^{n}q_j^{D+1}\\ &+ 2^D\left(\frac{en}{D}+e\right)^{2D} \left(\prod_{j=1}^{n}\rho_{j,D}\right)^{1/2}. \end{aligned}}]

In particular,

[image: \displaystyle \boxed{\mathbb P(F_n) \leq nq_n^{D+1} + 2^D\left(\frac{en}{D}+e\right)^{2D} \left[\prod_{j=1}^{n} \frac{1}{2-p_j}\left(1+\frac{(-1)^D}{2}p_jq_j^{D+1}\right)\right]^{1/2}.}]

Now take

[image: \displaystyle D=\lfloor\delta n\rfloor, \qquad 0 < \delta < 1.]

Since

[image: \displaystyle q_n = 1-\frac{2}{2+\log n},]

one has

[image: \displaystyle nq_n^{D+1} \leq n\exp\left(-\frac{2(D+1)}{2+\log n}\right) = n\exp\left(-(2\delta+o(1))\frac{n}{\log n}\right).]

Furthermore,

[image: \displaystyle \sum_{j=1}^{n} p_jq_j^{D+1} = o(1),]

so the cutoff-parity correction contributes only [image: o(1)] to the logarithm of the product. Hence

[image: \displaystyle \frac12\sum_{j=1}^{n}\log\rho_{j,D} = -\frac{n}{2}\log2 + \frac{n}{2\log n} + O\left(\frac{n}{\log^2n}\right).]

Also,

[image: \displaystyle \frac{1}{n}\log\left[2^D\left(\frac{en}{D}+e\right)^{2D}\right] = \delta\log2 + 2\delta\log\left(\frac{e(1+\delta)}{\delta}\right) + o(1).]

It follows that

[image: \displaystyle \boxed{\mathbb P(F_n) \leq n\exp\left(-(2\delta+o(1))\frac{n}{\log n}\right) + \exp\left((\Phi(\delta)+o(1))n\right),}]

where

[image: \displaystyle \boxed{\Phi(\delta) = \delta\log2 + 2\delta\log\left(\frac{e(1+\delta)}{\delta}\right) - \frac{\log2}{2}.}]

The function [image: \Phi] has a unique positive zero

[image: \displaystyle \boxed{\delta_* = 0.0370366917265559\ldots.}]

Thus, for every fixed

[image: \displaystyle \boxed{0 < \delta < \delta_*,}]

the failure probabilities satisfy the explicit summable estimate

[image: \displaystyle \boxed{\mathbb P\left(a^{(n-1,1)} > 1\right) \leq n\exp\left(-(2\delta+o(1))\frac{n}{\log n}\right) + \exp\left(-(c_\delta+o(1))n\right),}]

where

[image: \displaystyle c_\delta=-\Phi(\delta)>0.]

For example, taking

[image: \displaystyle \delta=0.03]

gives

[image: \displaystyle \Phi(0.03) = -0.0536121728894\ldots,]

and hence

[image: \displaystyle \boxed{\mathbb P\left(a^{(n-1,1)}>1\right) \leq n\exp\left(-(0.06+o(1))\frac{n}{\log n}\right) + \exp\left(-(0.0536121728\ldots+o(1))n\right).}]

The exact chain is therefore

[image: \displaystyle \boxed{\text{unique two-separated extremizer} \Longrightarrow \text{exact stability defect} \Longrightarrow \text{cutoff-parity law} \Longrightarrow \text{explicit finite-}n\text{ failure rate}.}]

This turns the qualitative two-separated estimate in the proof into an exact concentration law and gives a quantitative strengthening of the almost-sure Cramér–Gilbreath conclusion.

Best regards,
Emmanuel Audigé

[Reply][453]

[29 July, 2026 at 1:07 pm][454]

**Wen Huang**

[image: Wen Huang's avatar]

Regarding the length L appearing in Theorem 1.6 of your paper on the Gilbreath conjecture, I have attempted to substitute the pairing condition from the strong Goldbach conjecture for preliminary calculations. Could you check whether my understanding outlined below is correct? At the first level: the pairing gap satisfies D = N – 2p = \sum g_i. This implies that covering all even integers in the Goldbach problem is equivalent to requiring sufficient flexibility for the consecutive sums of prime gaps. Fundamentally, the two-valued obstacle segments described in your theorem undermine this flexibility. At the second level, the critical divide lies between finiteness and infiniteness. If any \{0,d\} two-valued segment remains finite (regardless of whether its length exceeds your defined L), pairings can seemingly be constructed by searching outside this segment. However, once such a segment extends to infinity, the consecutive sums can only take values from discrete linear combinations. As N\to\infty, D=N-2p varies continuously, which inevitably causes massive mismatches and directly invalidates the full coverage requirement of the strong Goldbach conjecture. At the third level: Is it therefore reasonable to interpret the matter as follows? The validity of the strong Goldbach conjecture inherently enforces the exclusion of infinitely long obstacle segments. Meanwhile, the explicit constant L proven in your theorem (beyond which a counterexample to the Gilbreath conjecture emerges) precisely quantifies the finite tolerance threshold. For the Goldbach conjecture, there is no need to further shrink L; it suffices merely to guarantee that L remains finite. Does this simplified viewpoint overlook essential sieve-theoretic error terms?

[Reply][455]

### Leave a comment [Cancel reply][456]

### For commenters

To enter in LaTeX in comments, use $latex *<Your LaTeX code>*$ (without the < and > signs, of course; in fact, these signs should be avoided as they can cause formatting errors). Also, backslashes \ need to be doubled as \\. See the [about page][2] for details and for other commenting policy.

[&laquo; A digestion of unit distance constructions][457]

[Old and new apps, via modern coding agents &raquo;][458]

[Blog at WordPress.com.][459] Ben Eastaugh and Chris Sternal-Johnson.

[Subscribe to feed.][8]

- [Comment][460]
- [Reblog][461]
- [Subscribe][461] [Subscribed][461]

  - [What's new][462]

  -

Already have a WordPress.com account? [Log in now.][463]

-

  - [What's new][462]
  - [Subscribe][461] [Subscribed][461]
  - [Sign up][464]
  - [Log in][463]
  - [Copy shortlink][465]
  - [Report this content][466]
  - [View post in Reader][467]
  - [Manage subscriptions][468]
  - [Collapse this bar][461]

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
[9]: https://terrytao.wordpress.com/category/mathematics/mathco/
[10]: https://terrytao.wordpress.com/category/mathematics/mathnt/
[11]: https://terrytao.wordpress.com/category/mathematics/mathpr/
[12]: https://terrytao.wordpress.com/tag/cramers-random-model/
[13]: https://terrytao.wordpress.com/tag/gilbreaths-conjecture/
[14]: https://terrytao.wordpress.com/tag/zach-hunter/
[15]: https://terrytao.wordpress.com/tag/zachary-chase/
[16]: https://terrytao.wordpress.com/author/teorth/
[17]: https://www.math.kent.edu/~zchase/
[18]: https://zachhunter.xyz/
[19]: https://arxiv.org/abs/2607.08712
[20]: https://en.wikipedia.org/wiki/Gilbreath&#037;27s_conjecture
[21]: https://www.jstor.org/stable/2152962
[22]: https://en.wikipedia.org/wiki/Cram&#037;C3&#037;A9r&#037;27s_conjecture
[23]: https://link.springer.com/article/10.1007/s00208-023-02579-w
[24]: https://mathoverflow.net/questions/468056/packing-an-upwards-equilateral-triangle-efficiently-by-downwards-equilateral-tri
[25]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#print?share=print
[26]: mailto:?subject=%5BShared%20Post%5D%20Gilbreath%27s%20conjecture%3A%20a%20Cram%C3%A9r%20random%20model%20and%20a%20deterministic%20analysis#038;body=https%3A%2F%2Fterrytao.wordpress.com%2F2026%2F07%2F11%2Fgilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis%2F&#038;share=email
[27]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?share=twitter
[28]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?share=facebook
[29]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?share=reddit
[30]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?share=pinterest
[31]: http://www.math.ucla.edu/~tao
[32]: https://terrytao.wordpress.com/2010/10/16/245a-notes-5-differentiation-theorems/comment-page-4/#comment-693781
[33]: https://terrytao.wordpress.com/2010/10/16/245a-notes-5-differentiation-theorems/comment-page-4/#comment-693780
[34]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693779
[35]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693777
[36]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693774
[37]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693773
[38]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693772
[39]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693771
[40]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693770
[41]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693769
[42]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693768
[43]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693766
[44]: https://terrytao.wordpress.com/2010/09/09/245a-notes-1-lebesgue-measure/comment-page-2/#comment-693765
[45]: https://terrytao.wordpress.com/2010/10/16/245a-notes-5-differentiation-theorems/comment-page-4/#comment-693763
[46]: http://robertjdicks1.wordpress.com
[47]: https://terrytao.wordpress.com/2014/07/07/the-subspace-theorem-approach-to-siegels-theorem-on-integral-points-on-curves-via-nonstandard-analysis/comment-page-1/#comment-693762
[48]: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/
[49]: https://terrytao.wordpress.com/2025/02/25/the-three-dimensional-kakeya-conjecture-after-wang-and-zahl/
[50]: https://terrytao.wordpress.com/career-advice/work-hard/
[51]: https://terrytao.wordpress.com/2010/10/16/245a-notes-5-differentiation-theorems/
[52]: https://terrytao.wordpress.com/career-advice/does-one-have-to-be-a-genius-to-do-maths/
[53]: https://terrytao.wordpress.com/2026/07/
[54]: https://terrytao.wordpress.com/2026/06/
[55]: https://terrytao.wordpress.com/2026/05/
[56]: https://terrytao.wordpress.com/2026/03/
[57]: https://terrytao.wordpress.com/2026/02/
[58]: https://terrytao.wordpress.com/2026/01/
[59]: https://terrytao.wordpress.com/2025/12/
[60]: https://terrytao.wordpress.com/2025/11/
[61]: https://terrytao.wordpress.com/2025/09/
[62]: https://terrytao.wordpress.com/2025/08/
[63]: https://terrytao.wordpress.com/2025/07/
[64]: https://terrytao.wordpress.com/2025/06/
[65]: https://terrytao.wordpress.com/2025/05/
[66]: https://terrytao.wordpress.com/2025/04/
[67]: https://terrytao.wordpress.com/2025/03/
[68]: https://terrytao.wordpress.com/2025/02/
[69]: https://terrytao.wordpress.com/2025/01/
[70]: https://terrytao.wordpress.com/2024/12/
[71]: https://terrytao.wordpress.com/2024/11/
[72]: https://terrytao.wordpress.com/2024/10/
[73]: https://terrytao.wordpress.com/2024/09/
[74]: https://terrytao.wordpress.com/2024/08/
[75]: https://terrytao.wordpress.com/2024/07/
[76]: https://terrytao.wordpress.com/2024/06/
[77]: https://terrytao.wordpress.com/2024/05/
[78]: https://terrytao.wordpress.com/2024/04/
[79]: https://terrytao.wordpress.com/2024/03/
[80]: https://terrytao.wordpress.com/2023/12/
[81]: https://terrytao.wordpress.com/2023/11/
[82]: https://terrytao.wordpress.com/2023/10/
[83]: https://terrytao.wordpress.com/2023/09/
[84]: https://terrytao.wordpress.com/2023/08/
[85]: https://terrytao.wordpress.com/2023/06/
[86]: https://terrytao.wordpress.com/2023/05/
[87]: https://terrytao.wordpress.com/2023/04/
[88]: https://terrytao.wordpress.com/2023/03/
[89]: https://terrytao.wordpress.com/2023/02/
[90]: https://terrytao.wordpress.com/2023/01/
[91]: https://terrytao.wordpress.com/2022/12/
[92]: https://terrytao.wordpress.com/2022/11/
[93]: https://terrytao.wordpress.com/2022/10/
[94]: https://terrytao.wordpress.com/2022/09/
[95]: https://terrytao.wordpress.com/2022/07/
[96]: https://terrytao.wordpress.com/2022/06/
[97]: https://terrytao.wordpress.com/2022/05/
[98]: https://terrytao.wordpress.com/2022/04/
[99]: https://terrytao.wordpress.com/2022/03/
[100]: https://terrytao.wordpress.com/2022/02/
[101]: https://terrytao.wordpress.com/2022/01/
[102]: https://terrytao.wordpress.com/2021/12/
[103]: https://terrytao.wordpress.com/2021/11/
[104]: https://terrytao.wordpress.com/2021/10/
[105]: https://terrytao.wordpress.com/2021/09/
[106]: https://terrytao.wordpress.com/2021/08/
[107]: https://terrytao.wordpress.com/2021/07/
[108]: https://terrytao.wordpress.com/2021/06/
[109]: https://terrytao.wordpress.com/2021/05/
[110]: https://terrytao.wordpress.com/2021/02/
[111]: https://terrytao.wordpress.com/2021/01/
[112]: https://terrytao.wordpress.com/2020/12/
[113]: https://terrytao.wordpress.com/2020/11/
[114]: https://terrytao.wordpress.com/2020/10/
[115]: https://terrytao.wordpress.com/2020/09/
[116]: https://terrytao.wordpress.com/2020/08/
[117]: https://terrytao.wordpress.com/2020/07/
[118]: https://terrytao.wordpress.com/2020/06/
[119]: https://terrytao.wordpress.com/2020/05/
[120]: https://terrytao.wordpress.com/2020/04/
[121]: https://terrytao.wordpress.com/2020/03/
[122]: https://terrytao.wordpress.com/2020/02/
[123]: https://terrytao.wordpress.com/2020/01/
[124]: https://terrytao.wordpress.com/2019/12/
[125]: https://terrytao.wordpress.com/2019/11/
[126]: https://terrytao.wordpress.com/2019/09/
[127]: https://terrytao.wordpress.com/2019/08/
[128]: https://terrytao.wordpress.com/2019/07/
[129]: https://terrytao.wordpress.com/2019/06/
[130]: https://terrytao.wordpress.com/2019/05/
[131]: https://terrytao.wordpress.com/2019/04/
[132]: https://terrytao.wordpress.com/2019/03/
[133]: https://terrytao.wordpress.com/2019/02/
[134]: https://terrytao.wordpress.com/2019/01/
[135]: https://terrytao.wordpress.com/2018/12/
[136]: https://terrytao.wordpress.com/2018/11/
[137]: https://terrytao.wordpress.com/2018/10/
[138]: https://terrytao.wordpress.com/2018/09/
[139]: https://terrytao.wordpress.com/2018/08/
[140]: https://terrytao.wordpress.com/2018/07/
[141]: https://terrytao.wordpress.com/2018/06/
[142]: https://terrytao.wordpress.com/2018/05/
[143]: https://terrytao.wordpress.com/2018/04/
[144]: https://terrytao.wordpress.com/2018/03/
[145]: https://terrytao.wordpress.com/2018/02/
[146]: https://terrytao.wordpress.com/2018/01/
[147]: https://terrytao.wordpress.com/2017/12/
[148]: https://terrytao.wordpress.com/2017/11/
[149]: https://terrytao.wordpress.com/2017/10/
[150]: https://terrytao.wordpress.com/2017/09/
[151]: https://terrytao.wordpress.com/2017/08/
[152]: https://terrytao.wordpress.com/2017/07/
[153]: https://terrytao.wordpress.com/2017/06/
[154]: https://terrytao.wordpress.com/2017/05/
[155]: https://terrytao.wordpress.com/2017/04/
[156]: https://terrytao.wordpress.com/2017/03/
[157]: https://terrytao.wordpress.com/2017/02/
[158]: https://terrytao.wordpress.com/2017/01/
[159]: https://terrytao.wordpress.com/2016/12/
[160]: https://terrytao.wordpress.com/2016/11/
[161]: https://terrytao.wordpress.com/2016/10/
[162]: https://terrytao.wordpress.com/2016/09/
[163]: https://terrytao.wordpress.com/2016/08/
[164]: https://terrytao.wordpress.com/2016/07/
[165]: https://terrytao.wordpress.com/2016/06/
[166]: https://terrytao.wordpress.com/2016/05/
[167]: https://terrytao.wordpress.com/2016/04/
[168]: https://terrytao.wordpress.com/2016/03/
[169]: https://terrytao.wordpress.com/2016/02/
[170]: https://terrytao.wordpress.com/2016/01/
[171]: https://terrytao.wordpress.com/2015/12/
[172]: https://terrytao.wordpress.com/2015/11/
[173]: https://terrytao.wordpress.com/2015/10/
[174]: https://terrytao.wordpress.com/2015/09/
[175]: https://terrytao.wordpress.com/2015/08/
[176]: https://terrytao.wordpress.com/2015/07/
[177]: https://terrytao.wordpress.com/2015/06/
[178]: https://terrytao.wordpress.com/2015/05/
[179]: https://terrytao.wordpress.com/2015/04/
[180]: https://terrytao.wordpress.com/2015/03/
[181]: https://terrytao.wordpress.com/2015/02/
[182]: https://terrytao.wordpress.com/2015/01/
[183]: https://terrytao.wordpress.com/2014/12/
[184]: https://terrytao.wordpress.com/2014/11/
[185]: https://terrytao.wordpress.com/2014/10/
[186]: https://terrytao.wordpress.com/2014/09/
[187]: https://terrytao.wordpress.com/2014/08/
[188]: https://terrytao.wordpress.com/2014/07/
[189]: https://terrytao.wordpress.com/2014/06/
[190]: https://terrytao.wordpress.com/2014/05/
[191]: https://terrytao.wordpress.com/2014/04/
[192]: https://terrytao.wordpress.com/2014/03/
[193]: https://terrytao.wordpress.com/2014/02/
[194]: https://terrytao.wordpress.com/2014/01/
[195]: https://terrytao.wordpress.com/2013/12/
[196]: https://terrytao.wordpress.com/2013/11/
[197]: https://terrytao.wordpress.com/2013/10/
[198]: https://terrytao.wordpress.com/2013/09/
[199]: https://terrytao.wordpress.com/2013/08/
[200]: https://terrytao.wordpress.com/2013/07/
[201]: https://terrytao.wordpress.com/2013/06/
[202]: https://terrytao.wordpress.com/2013/05/
[203]: https://terrytao.wordpress.com/2013/04/
[204]: https://terrytao.wordpress.com/2013/03/
[205]: https://terrytao.wordpress.com/2013/02/
[206]: https://terrytao.wordpress.com/2013/01/
[207]: https://terrytao.wordpress.com/2012/12/
[208]: https://terrytao.wordpress.com/2012/11/
[209]: https://terrytao.wordpress.com/2012/10/
[210]: https://terrytao.wordpress.com/2012/09/
[211]: https://terrytao.wordpress.com/2012/08/
[212]: https://terrytao.wordpress.com/2012/07/
[213]: https://terrytao.wordpress.com/2012/06/
[214]: https://terrytao.wordpress.com/2012/05/
[215]: https://terrytao.wordpress.com/2012/04/
[216]: https://terrytao.wordpress.com/2012/03/
[217]: https://terrytao.wordpress.com/2012/02/
[218]: https://terrytao.wordpress.com/2012/01/
[219]: https://terrytao.wordpress.com/2011/12/
[220]: https://terrytao.wordpress.com/2011/11/
[221]: https://terrytao.wordpress.com/2011/10/
[222]: https://terrytao.wordpress.com/2011/09/
[223]: https://terrytao.wordpress.com/2011/08/
[224]: https://terrytao.wordpress.com/2011/07/
[225]: https://terrytao.wordpress.com/2011/06/
[226]: https://terrytao.wordpress.com/2011/05/
[227]: https://terrytao.wordpress.com/2011/04/
[228]: https://terrytao.wordpress.com/2011/03/
[229]: https://terrytao.wordpress.com/2011/02/
[230]: https://terrytao.wordpress.com/2011/01/
[231]: https://terrytao.wordpress.com/2010/12/
[232]: https://terrytao.wordpress.com/2010/11/
[233]: https://terrytao.wordpress.com/2010/10/
[234]: https://terrytao.wordpress.com/2010/09/
[235]: https://terrytao.wordpress.com/2010/08/
[236]: https://terrytao.wordpress.com/2010/07/
[237]: https://terrytao.wordpress.com/2010/06/
[238]: https://terrytao.wordpress.com/2010/05/
[239]: https://terrytao.wordpress.com/2010/04/
[240]: https://terrytao.wordpress.com/2010/03/
[241]: https://terrytao.wordpress.com/2010/02/
[242]: https://terrytao.wordpress.com/2010/01/
[243]: https://terrytao.wordpress.com/2009/12/
[244]: https://terrytao.wordpress.com/2009/11/
[245]: https://terrytao.wordpress.com/2009/10/
[246]: https://terrytao.wordpress.com/2009/09/
[247]: https://terrytao.wordpress.com/2009/08/
[248]: https://terrytao.wordpress.com/2009/07/
[249]: https://terrytao.wordpress.com/2009/06/
[250]: https://terrytao.wordpress.com/2009/05/
[251]: https://terrytao.wordpress.com/2009/04/
[252]: https://terrytao.wordpress.com/2009/03/
[253]: https://terrytao.wordpress.com/2009/02/
[254]: https://terrytao.wordpress.com/2009/01/
[255]: https://terrytao.wordpress.com/2008/12/
[256]: https://terrytao.wordpress.com/2008/11/
[257]: https://terrytao.wordpress.com/2008/10/
[258]: https://terrytao.wordpress.com/2008/09/
[259]: https://terrytao.wordpress.com/2008/08/
[260]: https://terrytao.wordpress.com/2008/07/
[261]: https://terrytao.wordpress.com/2008/06/
[262]: https://terrytao.wordpress.com/2008/05/
[263]: https://terrytao.wordpress.com/2008/04/
[264]: https://terrytao.wordpress.com/2008/03/
[265]: https://terrytao.wordpress.com/2008/02/
[266]: https://terrytao.wordpress.com/2008/01/
[267]: https://terrytao.wordpress.com/2007/12/
[268]: https://terrytao.wordpress.com/2007/11/
[269]: https://terrytao.wordpress.com/2007/10/
[270]: https://terrytao.wordpress.com/2007/09/
[271]: https://terrytao.wordpress.com/2007/08/
[272]: https://terrytao.wordpress.com/2007/07/
[273]: https://terrytao.wordpress.com/2007/06/
[274]: https://terrytao.wordpress.com/2007/05/
[275]: https://terrytao.wordpress.com/2007/04/
[276]: https://terrytao.wordpress.com/2007/03/
[277]: https://terrytao.wordpress.com/2007/02/
[278]: https://terrytao.wordpress.com/category/expository/
[279]: https://terrytao.wordpress.com/category/expository/tricks/
[280]: https://terrytao.wordpress.com/category/guest-blog/
[281]: https://terrytao.wordpress.com/category/mathematics/
[282]: https://terrytao.wordpress.com/category/mathematics/mathac/
[283]: https://terrytao.wordpress.com/category/mathematics/mathag/
[284]: https://terrytao.wordpress.com/category/mathematics/mathap/
[285]: https://terrytao.wordpress.com/category/mathematics/mathat/
[286]: https://terrytao.wordpress.com/category/mathematics/mathca/
[287]: https://terrytao.wordpress.com/category/mathematics/mathct/
[288]: https://terrytao.wordpress.com/category/mathematics/mathcv/
[289]: https://terrytao.wordpress.com/category/mathematics/mathdg/
[290]: https://terrytao.wordpress.com/category/mathematics/mathds/
[291]: https://terrytao.wordpress.com/category/mathematics/mathfa/
[292]: https://terrytao.wordpress.com/category/mathematics/mathgm/
[293]: https://terrytao.wordpress.com/category/mathematics/mathgn/
[294]: https://terrytao.wordpress.com/category/mathematics/mathgr/
[295]: https://terrytao.wordpress.com/category/mathematics/mathgt/
[296]: https://terrytao.wordpress.com/category/mathematics/mathho/
[297]: https://terrytao.wordpress.com/category/mathematics/mathit/
[298]: https://terrytao.wordpress.com/category/mathematics/mathlo/
[299]: https://terrytao.wordpress.com/category/mathematics/mathmg/
[300]: https://terrytao.wordpress.com/category/mathematics/mathmp/
[301]: https://terrytao.wordpress.com/category/mathematics/mathna/
[302]: https://terrytao.wordpress.com/category/mathematics/mathoa/
[303]: https://terrytao.wordpress.com/category/mathematics/mathqa/
[304]: https://terrytao.wordpress.com/category/mathematics/mathra/
[305]: https://terrytao.wordpress.com/category/mathematics/mathrt/
[306]: https://terrytao.wordpress.com/category/mathematics/mathsg/
[307]: https://terrytao.wordpress.com/category/mathematics/mathsp/
[308]: https://terrytao.wordpress.com/category/mathematics/mathst/
[309]: https://terrytao.wordpress.com/category/non-technical/
[310]: https://terrytao.wordpress.com/category/non-technical/admin/
[311]: https://terrytao.wordpress.com/category/non-technical/advertising/
[312]: https://terrytao.wordpress.com/category/non-technical/diversions-non-technical/
[313]: https://terrytao.wordpress.com/category/non-technical/media/
[314]: https://terrytao.wordpress.com/category/non-technical/media/journals/
[315]: https://terrytao.wordpress.com/category/non-technical/obituary/
[316]: https://terrytao.wordpress.com/category/opinion/
[317]: https://terrytao.wordpress.com/category/paper/
[318]: https://terrytao.wordpress.com/category/paper/book/
[319]: https://terrytao.wordpress.com/category/paper/companion/
[320]: https://terrytao.wordpress.com/category/paper/update/
[321]: https://terrytao.wordpress.com/category/question/
[322]: https://terrytao.wordpress.com/category/question/polymath/
[323]: https://terrytao.wordpress.com/category/talk/
[324]: https://terrytao.wordpress.com/category/talk/dls/
[325]: https://terrytao.wordpress.com/category/teaching/
[326]: https://terrytao.wordpress.com/category/teaching/245a-real-analysis/
[327]: https://terrytao.wordpress.com/category/teaching/245b-real-analysis/
[328]: https://terrytao.wordpress.com/category/teaching/245c-real-analysis/
[329]: https://terrytao.wordpress.com/category/teaching/246a-complex-analysis/
[330]: https://terrytao.wordpress.com/category/teaching/246b-complex-analysis/
[331]: https://terrytao.wordpress.com/category/teaching/246c-complex-analysis/
[332]: https://terrytao.wordpress.com/category/teaching/247b-classical-fourier-analysis/
[333]: https://terrytao.wordpress.com/category/teaching/254a-analytic-prime-number-theory/
[334]: https://terrytao.wordpress.com/category/teaching/254a-ergodic-theory/
[335]: https://terrytao.wordpress.com/category/teaching/254a-hilberts-fifth-problem/
[336]: https://terrytao.wordpress.com/category/teaching/254a-incompressible-fluid-equations/
[337]: https://terrytao.wordpress.com/category/teaching/254a-random-matrices/
[338]: https://terrytao.wordpress.com/category/teaching/254b-expansion-in-groups/
[339]: https://terrytao.wordpress.com/category/teaching/254b-higher-order-fourier-analysis/
[340]: https://terrytao.wordpress.com/category/teaching/255b-incompressible-euler-equations/
[341]: https://terrytao.wordpress.com/category/teaching/275a-probability-theory/
[342]: https://terrytao.wordpress.com/category/teaching/285g-poincare-conjecture/
[343]: https://terrytao.wordpress.com/category/teaching/logic-reading-seminar/
[344]: https://terrytao.wordpress.com/category/the-sciences/
[345]: https://terrytao.wordpress.com/category/travel/
[346]: https://terrytao.wordpress.com/tag/additive-combinatorics/
[347]: https://terrytao.wordpress.com/tag/approximate-groups/
[348]: https://terrytao.wordpress.com/tag/arithmetic-progressions/
[349]: https://terrytao.wordpress.com/tag/artificial-intelligence/
[350]: https://terrytao.wordpress.com/tag/ben-green/
[351]: https://terrytao.wordpress.com/tag/cauchy-schwarz/
[352]: https://terrytao.wordpress.com/tag/cayley-graphs/
[353]: https://terrytao.wordpress.com/tag/central-limit-theorem/
[354]: https://terrytao.wordpress.com/tag/chowla-conjecture/
[355]: https://terrytao.wordpress.com/tag/compressed-sensing/
[356]: https://terrytao.wordpress.com/tag/correspondence-principle/
[357]: https://terrytao.wordpress.com/tag/cosmic-distance-ladder/
[358]: https://terrytao.wordpress.com/tag/distributions/
[359]: https://terrytao.wordpress.com/tag/divisor-function/
[360]: https://terrytao.wordpress.com/tag/eigenvalues/
[361]: https://terrytao.wordpress.com/tag/elias-stein/
[362]: https://terrytao.wordpress.com/tag/emmanuel-breuillard/
[363]: https://terrytao.wordpress.com/tag/entropy/
[364]: https://terrytao.wordpress.com/tag/equidistribution/
[365]: https://terrytao.wordpress.com/tag/erdos/
[366]: https://terrytao.wordpress.com/tag/ergodic-theory/
[367]: https://terrytao.wordpress.com/tag/euler-equations/
[368]: https://terrytao.wordpress.com/tag/exponential-sums/
[369]: https://terrytao.wordpress.com/tag/finite-fields/
[370]: https://terrytao.wordpress.com/tag/fourier-transform/
[371]: https://terrytao.wordpress.com/tag/freimans-theorem/
[372]: https://terrytao.wordpress.com/tag/gowers-uniformity-norm/
[373]: https://terrytao.wordpress.com/tag/gowers-uniformity-norms/
[374]: https://terrytao.wordpress.com/tag/graph-theory/
[375]: https://terrytao.wordpress.com/tag/gromovs-theorem/
[376]: https://terrytao.wordpress.com/tag/gue/
[377]: https://terrytao.wordpress.com/tag/hilberts-fifth-problem/
[378]: https://terrytao.wordpress.com/tag/icm/
[379]: https://terrytao.wordpress.com/tag/incompressible-euler-equations/
[380]: https://terrytao.wordpress.com/tag/inverse-conjecture/
[381]: https://terrytao.wordpress.com/tag/joni-teravainen/
[382]: https://terrytao.wordpress.com/tag/kaisa-matomaki/
[383]: https://terrytao.wordpress.com/tag/kakeya-conjecture/
[384]: https://terrytao.wordpress.com/tag/lie-algebras/
[385]: https://terrytao.wordpress.com/tag/lie-groups/
[386]: https://terrytao.wordpress.com/tag/liouville-function/
[387]: https://terrytao.wordpress.com/tag/littlewood-offord-problem/
[388]: https://terrytao.wordpress.com/tag/maksym-radziwill/
[389]: https://terrytao.wordpress.com/tag/mobius-function/
[390]: https://terrytao.wordpress.com/tag/navier-stokes-equations/
[391]: https://terrytao.wordpress.com/tag/nilpotent-groups/
[392]: https://terrytao.wordpress.com/tag/nilsequences/
[393]: https://terrytao.wordpress.com/tag/nonstandard-analysis/
[394]: https://terrytao.wordpress.com/tag/paul-erdos/
[395]: https://terrytao.wordpress.com/tag/politics/
[396]: https://terrytao.wordpress.com/tag/polymath1/
[397]: https://terrytao.wordpress.com/tag/polymath8/
[398]: https://terrytao.wordpress.com/tag/polymath15/
[399]: https://terrytao.wordpress.com/tag/polynomial-method/
[400]: https://terrytao.wordpress.com/tag/polynomials/
[401]: https://terrytao.wordpress.com/tag/prime-gaps/
[402]: https://terrytao.wordpress.com/tag/prime-numbers/
[403]: https://terrytao.wordpress.com/tag/prime-number-theorem/
[404]: https://terrytao.wordpress.com/tag/random-matrices/
[405]: https://terrytao.wordpress.com/tag/randomness/
[406]: https://terrytao.wordpress.com/tag/ratners-theorem/
[407]: https://terrytao.wordpress.com/tag/regularity-lemma/
[408]: https://terrytao.wordpress.com/tag/ricci-flow/
[409]: https://terrytao.wordpress.com/tag/riemann-zeta-function/
[410]: https://terrytao.wordpress.com/tag/schrodinger-equation/
[411]: https://terrytao.wordpress.com/tag/shannon-entropy/
[412]: https://terrytao.wordpress.com/tag/sieve-theory/
[413]: https://terrytao.wordpress.com/tag/structure/
[414]: https://terrytao.wordpress.com/tag/szemeredis-theorem/
[415]: https://terrytao.wordpress.com/tag/tamar-ziegler/
[416]: https://terrytao.wordpress.com/tag/ultrafilters/
[417]: https://terrytao.wordpress.com/tag/universality/
[418]: https://terrytao.wordpress.com/tag/van-vu/
[419]: https://terrytao.wordpress.com/tag/wave-maps/
[420]: https://terrytao.wordpress.com/tag/yitang-zhang/
[421]: https://polymathprojects.org/feed/
[422]: https://polymathprojects.org
[423]: https://polymathprojects.org/2026/04/03/polymath-news-and-ai/
[424]: https://polymathprojects.org/2021/02/20/polymath-projects-2021/
[425]: https://polymathprojects.org/2019/06/09/a-sort-of-polymath-on-a-famous-mathoverflow-problem/
[426]: https://polymathprojects.org/2019/02/03/ten-years-of-polymath/
[427]: https://polymathprojects.org/2018/10/19/updates-and-pictures/
[428]: https://polymathprojects.org/2018/04/10/polymath-proposal-finding-simpler-unit-distance-graphs-of-chromatic-number-5/
[429]: https://polymathprojects.org/2018/01/26/a-new-polymath-proposal-related-to-the-riemann-hypothesis-over-taos-blog/
[430]: https://polymathprojects.org/2018/01/26/spontaneous-polymath-14-a-success/
[431]: https://polymathprojects.org/2017/08/22/polymath-13-a-success/
[432]: https://polymathprojects.org/2017/05/15/non-transitive-dice-over-gowerss-blog/
[433]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/feed/
[434]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#comment-693359
[435]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?replytocom=693359#respond
[436]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#comment-693362
[437]: https://en.wikipedia.org/wiki/Pseudorandomness
[438]: https://terrytao.wordpress.com/2015/01/04/254a-supplement-4-probabilistic-models-and-heuristics-for-the-primes-optional/
[439]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?replytocom=693362#respond
[440]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#comment-693364
[441]: https://github.com/michaelmross/Gilbreath
[442]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?replytocom=693364#respond
[443]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#comment-693365
[444]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?replytocom=693365#respond
[445]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#comment-693709
[446]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?replytocom=693709#respond
[447]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#comment-693366
[448]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?replytocom=693366#respond
[449]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#comment-693407
[450]: https://terrytao.wordpress.com/2026/07/14/visualizing-the-gilbreath-expectation-sequence/
[451]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?replytocom=693407#respond
[452]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#comment-693627
[453]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?replytocom=693627#respond
[454]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#comment-693708
[455]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/?replytocom=693708#respond
[456]: /2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#respond
[457]: https://terrytao.wordpress.com/2026/07/03/a-digestion-of-unit-distance-constructions/
[458]: https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/
[459]: https://wordpress.com/?ref=footer_blog
[460]: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/#comments
[461]: 
[462]: https://terrytao.wordpress.com
[463]: https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fterrytao.wordpress.com%2F2026%2F07%2F11%2Fgilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis%2F#038;signup_flow=account
[464]: https://wordpress.com/start/
[465]: https://wp.me/p3qzP-4E8
[466]: https://wordpress.com/abuse/?report_url=https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/
[467]: https://wordpress.com/reader/blogs/817149/posts/17864
[468]: https://subscribe.wordpress.com/
