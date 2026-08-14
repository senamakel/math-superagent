<!-- source: https://mathworld.wolfram.com/news/2004-10-13/google/ | converted from HTML -->

MathWorld News: Mathematica's Google Aptitude

# **[MathWorld Headline News][1]

---

## Mathematica's Google Aptitude

### By Ed Pegg Jr. and Eric W. Weisstein

#### With additional contributions by Daniel Lichtblau, Adam Strzebonski, Oyvind Tafjord, and Michael Trott

October 13--Many internet denizens have heard of [Sergey Brin][2], President of Technology at google.com. What they may not know is that before cofounding the precursor to Google in 1998 and subsequently becoming a multibillionaire, Brin was an intern at Wolfram Research (makers of [Mathematica][3], as well as sponsors of *MathWorld*).

### The Billboard

So perhaps it's no great surprise that Google utilizes unusually mathematically oriented recruitment techniques. In fact, these practices have received widespread coverage in the last few weeks and months following the erection of a mathematical billboard in Silicon Valley on southbound Highway 101 near Ralston, California in July 2004. The billboard poses the question of finding the first 10-digit [prime number][4] occurring in consecutive digits (i.e., the [decimal expansion][5]) of the mathematical constant known as **[e][6], which is a [transcendental number][7] whose first few digits are 2.7182818284.... The unusal nature of the billboard prompted coverage through numerous mainstream media outlets such as National Public Radio, *The Boston Globe*, and the *Oakland Tribune*, as well as (of course) on the internet.

[8]

Ed mentioned the puzzle on his [MathPuzzle website][9] on July 13, 2004. Minutes after its posting, Wolfram Research CEO and **[A New Kind of Science][10] author Stephen Wolfram sent the solution as a single line of Mathematica code:

Select[FromDigits/@Partition[First[RealDigits[E,10,1000]],10,1],PrimeQ,1] {7427466391}

### The Billboard, Level 2

Upon determining this value and typing the corresponding URL [http://7427466391.com][11] into a web browser, a potential Google employee (or curious *MathWorld*news story reader) is taken to a web page congratulating him (or her) and providing instructions for the second level of the puzzle, which involves finding the next term of the following sequence:

f(1)= 7182818284 f(2)= 8182845904 f(3)= 8747135266 f(4)= 7427466391 f(5)= __________

If the first two terms look familiar, that's because they are 10-digit portions of the decimal expansion of *e*given above. In fact, a little extra analysis shows that they are precisely those 10-digit portions summing to 49. After having determined that, it is easy to find the next number, again using Mathematica:

FromDigits/@Select[Partition[First[RealDigits[E,10,1000]],10,1],Total[#]==49&,5] {7182818284,8182845904,8747135266,7427466391,5966290435}

This is sequence [A095926][12] in Neil Sloane's **[On-Line Encyclopedia of Integer Sequences][13].

While we could likely continue this discussion at least a little further, we prefer at this juncture to leave additional levels of the billboard puzzle to the enterprising reader.

### Son of Billboard: The Google Labs Aptitude Test

On September 30, Google concocted an even more challenging recruitment device: the [Google Labs Aptitude Test][14]. Hardcopies of this test were also distributed to University of Illinois students in the October 12 edition of *The Daily Illini*. While some of the questions on the test relate more to computer knowledge and general creativity, many of them are highly mathematical. And for the these problems, Mathematica clearly shows its extremely high mathematical aptitude by solving them easily, especially when guided by a little research on *MathWorld*and other online resources such as the On-Line Encyclopedia of Integer Sequences.

We thank our former intern for doing his part in bringing fun mathematics problems into the news. A Mathematica version of the test, with answers, is available for download below.

file | format | size |

[AptitudeTest.nb][15] | notebook | 92 K |

### Google Labs Aptitude Test Partially Answered

1. Solve this cryptic equation, realizing of course that values for M and E could be interchanged. No leading zeros are allowed.

WWWDOT - GOOGLE = DOTCOM

This can be solved through systematic application of logic. For example, [image: O] cannot be equal to 0, since [image: O + O +[1 or  0] = W]. That would make [image: W1], but [image: D + GW], which is not possible.

Here is a slow brute-force method of solution that takes a few minutes on a relatively fast machine:

[image: Off[General :: "spell1"] chars = Characters/@ToLowerCase/@{"WWWDOT", "GOOGLE", "DOTCOM"} ; uchars = Union[Flatten[chars]] ; ]

[image: eqn = First[#] - Plus @@ Rest[#] &[FromDigits[#, 10] &/@chars] == 0 ; Timing[soln = Select[Permutations[Range[0, 9]], eqn/.Thread[ucharsMost[#]] &]] ]

[image: {359.3 Second, {{4, 5, 3, 1, 0, 6, 8, 9, 7, 2}, {4, 5, 6, 1, 0, 3, 8, 9, 7, 2}}}]

[image: Thread[ucharsMost[#]] &/@soln]

[image: {{c4, d5, e3, g1, l0, m6, o8, t&#62754 ... , d5, e6, g1, l0, m3, o8, t9, w7}}]

This gives the two solutions

777589 - 188106 == 589483
777589 - 188103 == 589486

Here is another solution using Mathematica 's Reduce command:

[image: eqn = "wwwdot" - "google""dotcom"/.s_StringFromD ... eqs&&#, vars, Integers] &/@eqs, (Unequal @@ vars/.ToRules[#]) =!= False&]//Timing ]

[image: {96.98 Second, c4&&d5&&e3&&g1&&amp ... p;&l0&&m3&&o8&&t9&&w7}]

A faster (but slightly more obscure) piece of code is the following:

[image: cf = Compile[Evaluate[{#, _Integer} &/@{c, d, e, g, l, m, o, t, w, x}], Module[ {& ...  {d, o, t, c, o} . S ; A - B - mC + e&&A - B - eC + m] ] ;]

[image: Transpose[{{c, d, e, g, l, m, o, t, w}, Most[#]}] &/@Module[{perms = Developer`ToPackedArray/@Take[Permutations[Range[0, 9]], All]}, Select[perms, cf @@ #1&]]//Timing]

[image: {49.89 Second, {{{c, 4}, {d, 5}, {e, 3}, {g, 1}, {l, 0}, {m, 6}, {o, 8}, {t, 9}, {w, 7}}, {{c, 4}, {d, 5}, {e, 6}, {g, 1}, {l, 0}, {m, 3}, {o, 8}, {t, 9}, {w, 7}}}}]

Faster still using the same approach (and requiring ~300 MB of memory):

[image: Transpose[{{c, d, e, g, l, m, o, t, w}, Most[#]}] &/@Compile[{}, Module[{perms = Take[Perm ... d, o, t, c, o} . S ; A - B - mC + e&&A - B - eC + m]]]]][]//Timing]

[image: {14.65 Second, {{{c, 4}, {d, 5}, {e, 3}, {g, 1}, {l, 0}, {m, 6}, {o, 8}, {t, 9}, {w, 7}}, {{c, 4}, {d, 5}, {e, 6}, {g, 1}, {l, 0}, {m, 3}, {o, 8}, {t, 9}, {w, 7}}}}]

Even faster using the same approach (that does not exclude leading zeros in the solution, but that can easily be weeded out at the end):

[image: eq = Simplify["wwwdot" - "google" - "dotcom"/.s_StringFr ... ers[s]], 10]] ; Join[CoefficientList[eq, #][[2]] &/@Union[Cases[eq, _Symbol, Infinity]], {0}] ]

[image: {-100, -99900, -1, -100100, -10, -1, -21000, -999, 111000, 0}]

[image: Transpose[{{c, d, e, g, l, m, o, t, w}, Most[#]}] &/@Compile[{}, Select[Permutations[Range ... , 9]], {-100, -99900, -1, -100100, -10, -1, -21000, -999, 111000, 0} . #0&]][]//Timing]

[image: {6.44 Second, {{{c, 4}, {d, 5}, {e, 3}, {g, 1}, {l, 0}, {m, 6}, {o, 8}, {t, 9}, {w, 7}}, {{c, 4}, {d, 5}, {e, 6}, {g, 1}, {l, 0}, {m, 3}, {o, 8}, {t, 9}, {w, 7}}}}]

Here is an independent solution method that uses branch-and-prune techniques:

[image: wwwdot = {w, w, w, d, o, t} ; google = {g, o, o, g, l, e} ; dotcom = {d, o, t, c, o, m} ; vars ... en[{eqn, vareqns, zeroOneConstraints, noLeadingZeros, mustSumToOneConstraints, distinctDigits}] ; ]

[image: Developer`SetSystemOptions["LinearProgrammingOptions" {"InteriorPointSize"1, "Preprocessing"True}] ;]

[image: Off[General :: "spell1"]]

[image: wwwdotgoogledotcom[constraints_, vars_, zeroOneVars_] := Module[{allvars = Join[vars, zeroOneV ...  zeroOneVars[[badpos]] 1], stack} ;] ;] ; Sort/@Map[Reverse, solns, {2}] ]]

[image: wwwdotgoogledotcom[allInfo, vars, Flatten[newvars]]//Timing]

[image: {72.89 Second, {{{c, 4}, {d, 5}, {e, 3}, {g, 1}, {l, 0}, {m, 6}, {o, 8}, {t, 9}, {w, 7}}, {{c, 4}, {d, 5}, {e, 6}, {g, 1}, {l, 0}, {m, 3}, {o, 8}, {t, 9}, {w, 7}}}}]

And the winner for overall fastest:

... &/@Select[dgclotem, dotcom[#, 6] + google[#, 6] wwwdot[#, 6] &])//Timing " width="617" height="511" align="absmiddle" / //>

[image: {2.58 Second, {{c4, d5, e6, g1, l0, m3, o&#627 ...  d5, e3, g1, l0, m6, o8, t9, w7}}}]

2. Write a haiku describing possible methods for predicting search traffic seasonality.

*MathWorld*'s search engine
seemed slowed this May. Undergrads
prepping for finals.

3. 1
1 1
2 1
1 2 1 1
1 1 1 2 2 1

What's the next line?

312211. This is the "look and say" sequence in which each term after the first describes the previous term: one 1 (11); two 1s (21); one 2 and one 1 (1211); one 1, one 2, and two 1's (111221); and so on. See the [look and say sequence][16] entry on MathWorld for a complete write-up and the algebraic form of a fascinating related quantity known as [Conway's constant][17].

[image: RunLengthEncode[x_List] := (Through[{First, Length}[#1]] &)/@Split[x] LookAndSay[n_, d_:1] := NestList[Flatten[Reverse/@RunLengthEncode[#]] &, {d}, n - 1] ]

[image: FromDigits/@LookAndSay[6]]

[image: {1, 11, 21, 1211, 111221, 312211}]

4. You are in a maze of twisty little passages, all alike. There is a dusty laptop here with a weak wireless connection. There are dull, lifeless gnomes strolling around. What dost thou do?

A) Wander aimlessly, bumping into obstacles until you are eaten by a grue.
B) Use the laptop as a digging device to tunnel to the next level.
C) Play MPoRPG until the battery dies along with your hopes.
D) Use the computer to map the nodes of the maze and discover an exit path.
E) Email your resume to Google, tell the lead gnome you quit and find yourself in whole different world [sic].

In general, make a [state diagram][18]. However, this method would not work in certain pathological cases such as, say, a fractal maze. For an example of this and commentary, see Ed Pegg's column [about state diagrams and mazes][19].

5. What's broken with Unix?

Their reproductive capabilities.

How would you fix it?

[This exercise is left to the reader.]

6. On your first day at Google, you discover that your cubicle mate wrote the textbook you used as a primary resource in your first year of graduate school. Do you:

A) Fawn obsequiously and ask if you can have an autograph.
B) Sit perfectly still and use only soft keystrokes to avoid disturbing her concentration
C) Leave her daily offerings of granola and English toffee from the food bins.
D) Quote your favorite formula from the textbook and explain how it's now your mantra.
E) Show her how example 17b could have been solved with 34 fewer lines of code.

[This exercise is left to the reader.]

7. Which of the following expresses Google's over-arching philosophy?

A) "I'm feeling lucky"
B) "Don't be evil"
C) "Oh, I already fixed that"
D) "You should never be more than 50 feet from food"
E) All of the above

[This exercise is left to the reader.]

8. How many different ways can you color an icosahedron with one of three colors on each face?

For an asymmetric 20-sided solid, there are [image: 3^20] possible [3-colorings][20]. For a symmetric 20-sided object, the [P&oacute;lya enumeration theorem][21] can be used to obtain the number of distinct colorings. Here is a concise Mathematica implementation:

[image: Off[General :: "shdw", General :: "spell1"] <<DiscreteMath`Combinato ...  GroupFaces = KSubsetGroup[GroupI, Sort/@f] ; Polya[GroupFaces, colors] ] ]

[image: ColorMySolid[Icosahedron, colors]]

[image: (2 colors^4)/5 + colors^8/3 + colors^10/4 + colors^20/60]

[image: %/.colors 3]

[image: 58130055]

What colors would you choose?

[This exercise is left to the reader.]

9. This space left intentionally blank. Please fill it with something that improves upon emptiness.

For nearly 10,000 images of mathematical functions, see [The Wolfram Functions Site visualization gallery][22].

10. On an infinite, two-dimensional, rectangular lattice of 1-ohm resistors, what is the resistance between two nodes that are a knight's move away?

[image: R[m_, n_] := 1/(2π) Integrate[1/t (1 - ((t - I)/(t + I))^(m + n) ((t - 1)/(t + 1))^Abs[m - n]), {t, 0, ∞}]]

[image: R[1, 2]]

[image: (8 - π)/(2 π)]

This problem is discussed in J. Cserti's 1999 [arXiv preprint][23]. It is also discussed in The Mathematica GuideBook for Symbolics, the forthcoming fourth volume in Michael Trott's **[GuideBook][24] series, the first two of which were published just last week by Springer-Verlag. The contents for all four GuideBooks, including the two not yet published, are available on the DVD distributed with the first two GuideBooks.

11. It's 2PM on a sunny Sunday afternoon in the Bay Area. You're minutes from the Pacific Ocean, redwood forest hiking trails and world class cultural attractions. What do you do?

[This exercise is left to the reader.]

12. In your opinion, what is the most beautiful math equation ever derived?

There are obviously many candidates. The following list gives ten of the authors' favorites:

1. [Archimedes' recurrence formula][25]: [image: a_ (2 n) = (2 a_n b_n)/(a_n + b_n)], [image: b_ (2 n) = (a_ (2 n) b_n)^(1/2)], [image: a_n>π>b_n], [image: a_∞ = b_∞]
2. [Euler formula][26]: [image: ^( π) + 10]
3. [Euler-Mascheroni constant][27]: [image: Underscript[lim, k∞]   (Underoverscript[∑, n = 1, arg3] 1/n - log(k)) ]
4. [Riemann hypothesis][28]: [image: ζ (α + β ) 0] and [image: β≠0] implies [image: α1/2]
5. [Gaussian integral][29]: [image: ∫_ (-∞)^∞^(-x^2) xπ^(1/2)]
6. [Ramanujan's prime product formula][30]: [image: Underoverscript[∏, k = 1, arg3] (p_k^2 + 1)/(p_k^2 - 1) 5/2]
7. [Zeta-regularized product][31]: [image: Underoverscript[∏, k = 1, arg3] k (2 π)^(1/2)]
8. [Mandelbrot set recursion][32]: [image: z_ (n + 1) z_n^2 + C]
9. [BBP formula][33]: [image: πUnderoverscript[∑, n = 0, arg3] (-2/(8 n + 4) - 1/(8 n + 5) - 1/(8 n + 6) + 4/(8 n + 1)) (1/16)^n]
10. [Cauchy integral formula][34]: [image: f(z_0) 1/(2 π ) ∮f(z)/(z - z_0) z]

An excellent paper discussing the most beautiful equations in physics is Daniel Z. Freedman's " [Some beautiful equations of mathematical physics][35]." Note that the physics view on beauty in equations is less uniform than the mathematical one. To quote the not-necessarily-standard view of theoretical physicist P.A.M. Dirac, "It is more important to have beauty in one's equations than to have them fit experiment."

13. Which of the following is NOT an actual interest group formed by Google employees?

A. Women's basketball
B. Buffy fans
C. Cricketeers
D. Nobel winners
E. Wine club

[This exercise is left to the reader.]

14. What will be the next great improvement in search technology?

Semantic searching of mathematical formulas. See [https://functions.wolfram.com/About/ourvision.html][36] for work currently underway at Wolfram Research that will be made available in the near future.

15. What is the optimal size of a project team, above which additional members do not contribute productivity equivalent to the percentage increase in the staff size?

A) 1
B) 3
C) 5
D) 11
E) 24

[This exercise is left to the reader.]

16. Given a triangle ABC, how would you use only a compass and straight edge to find a point P such that triangles ABP, ACP and BCP have equal perimeters? (Assume that ABC is constructed so that a solution does exist.)

This is the [isoperimetric point][37], which is at the center of the larger [Soddy circle][38]. It is related to [Apollonius' problem][39]. The three tangent circles are easy to construct: The circle around [image: C] has diameter [image: a + b - c], which gives the other two circles. A summary of compass and straightedge constructions for the outer Soddy circle can be found in " [Apollonius' Problem: A Study of Solutions and Their Connections][40] " by David Gisch and Jason M. Ribando.

17. Consider a function which, for a given whole number n, returns the number of ones required when writing out all numbers between 0 and n. For example, f(13)=6. Notice that f(1)=1. What is the next largest n such that f(n)=n?

The following Mathematica code computes the difference between [the cumulative number of 1s in the positive integers up to n] and [the value of n itself] as n ranges from 1 to 500,000:

[image: data = MapIndexed[#1 - #2[[1]] &, Rest[FoldList[Plus, 0, Table[DigitCount[n, 10, 1], {n, 500000}]]]] ;]

[image: <<Graphics`Colors` ListPlot[Take[MapIndexed[{#2[[1]], #1} &, data], {1, -1, 1000}], PlotStyleRed] ; ]

[image: [Graphics:HTMLFiles/AptitudeTest_58.gif]]

The solution to the problem is then the first position greater than the first at which data equals 0:

[image: Position[data, 0]//Flatten]

[image: {1, 199981, 199982, 199983, 199984, 199985, 199986, 199987, 199988, 199989, 199990, 200000, 200001}]

which are the first few terms of [sequence A014778][41] in the On-Line Encyclopedia of Integer Sequences.

Checking by hand confirms that the numbers from 1 to 199981 contain a total of 199981 1s:

[image: IntegerDigits/@Range[199981]//Flatten//Count[#, 1] &]

[image: 199981]

18. What is the coolest hack you've ever written?

While there is no "correct" answer, a nice hack for solving the first problem in the SIAM [hundred-dollar, hundred-digit challenge][42] can be achieved by converting the limit into the strongly divergent series:

[image: Sum[(-1)^k (2k)^(2k - 1), {k, ∞}]]

and then using Mathematica 's numerical function SequenceLimit to trivially get the correct answer (to six digits),

[image: Off[SequenceLimit :: "seqlim"] SequenceLimit[FoldList[Plus, 0, N[#, 1000] & @ Table[-(-1)^k (2k)^(2k - 1), {k, 300}]], WynnDegree20] ]

[image: 0.323368]

You must tweak parameters a bit or write your own sequence limit to get all 10 digits.

[Other hacks are left to the reader.]

19. 'Tis known in refined company, that choosing K things out of N can be done in ways as many as choosing N minus K from N: I pick K, you the remaining.

This simply states the [binomial coefficient][43] identity [image: (N)  (N    )   K            N - K].

Find though a cooler bijection, where you show a knack uncanny, of making your choices contain all K of mine. Oh, for pedantry: let K be no more than half N.

'Tis more problematic to disentangle semantic meaning precise from the this paragraph of verbiage peculiar.

20. What number comes next in the sequence: 10, 9, 60, 90, 70, 66, ?

A) 96
B) 1000000000000000000000000000000000\
0000000000000000000000000000000000\
000000000000000000000000000000000
C) Either of the above
D) None of the above

This can be looked up and found to be [sequence A052196][44] in the On-Line Encyclopedia of Integer Sequences, which gives the largest positive integer whose English name has n letters. For example, the first few terms are ten, nine, sixty, ninety, seventy, sixty-six, ninety-six, …. A more correct sequence might be ten, nine, sixty, googol, seventy, sixty-six, ninety-six, googolplex. And also note, incidentally, that the correct spelling of the mathematical term " [googol][45] " differs from the name of the company that made up this aptitude test.

The first few can be computed using the NumberName function in Eric Weisstein's **[MathWorld packages][46]:

[image: <<MathWorld`IntegerSequences`]

[image: pairs = Last/@Split[Sort[{StringLength[StringReplace[NumberName[#], {" "->"", "-"->""}]], #} &/@Range[100]], #1[[1]] == #2[[1]] &]]

[image: {{3, 10}, {4, 9}, {5, 60}, {6, 90}, {7, 70}, {8, 66}, {9, 96}, {10, 100}, {11, 98}, {12, 78}}]

[image: Last/@Take[pairs, 7]]

[image: {10, 9, 60, 90, 70, 66, 96}]

A mathematical solution could also be found by fitting a [Lagrange interpolating polynomial][47] to the six known terms and extrapolating:

[image: pts = {10, 9, 60, 90, 70, 66} ;]

[image: newpts = Function[x, Evaluate[InterpolatingPolynomial[pts, x]]]/@Range[7]]

[image: {10, 9, 60, 90, 70, 66, 290}]

[image: Plot[Evaluate[InterpolatingPolynomial[pts, x]], {x, 0, 7}, PlotStyleRed, Epilog {Red, PointSize[.02], Point/@Transpose[{Range[7], newpts}]}] ;]

[image: [Graphics:HTMLFiles/AptitudeTest_76.gif]]

21. In 29 words or fewer, describe what you would strive to accomplish if you worked at Google Labs.

[This exercise is left to the reader.]

References

Eustace, A. Google Blog. "Pencils Down, People." Sept. 30, 2004. [http://www.google.com/googleblog/2004/09/pencils-down-people.html][14]

Googler, A. Google Blog. "Warning: We Brake for Number Theory." July 12, 2004. [http://www.google.com/googleblog/2004/07/warning-we-brake-for-number-theory.html][8]

Pegg, E. Jr. "Material Added 13 Jul 2004." [http://www.mathpuzzle.com][9]


## Links

[1]: /news/
[2]: http://www.google.com/corporate/execs.html#sergey
[3]: http://www.wolfram.com/mathematica/
[4]: /PrimeNumber.html
[5]: /DecimalExpansion.html
[6]: /e.html
[7]: /TranscendentalNumber.html
[8]: http://www.google.com/googleblog/2004/07/warning-we-brake-for-number-theory.html
[9]: http://www.mathpuzzle.com/
[10]: http://www.wolframscience.com/
[11]: http://7427466391.com/
[12]: http://www.research.att.com/projects/OEIS?Anum=A095926
[13]: http://www.research.att.com/~njas/sequences/
[14]: http://www.google.com/googleblog/2004/09/pencils-down-people.html
[15]: AptitudeTest.nb
[16]: /LookandSaySequence.html
[17]: /ConwaysConstant.html
[18]: /StateDiagram.html
[19]: https://www.maa.org/editorial/mathgames/mathgames_11_24_03.html
[20]: /k-Coloring.html
[21]: /PolyaEnumerationTheorem.html
[22]: https://functions.wolfram.com/visualizations.html
[23]: https://arxiv.org/pdf/cond-mat/9909120
[24]: https://www.mathematicaguidebooks.org/
[25]: /ArchimedesRecurrenceFormula.html
[26]: /EulerFormula.html
[27]: /Euler-MascheroniConstant.html
[28]: /RiemannHypothesis.html
[29]: /GaussianIntegral.html
[30]: /PrimeProducts.html
[31]: /Zeta-RegularizedProduct.html
[32]: /MandelbrotSet.html
[33]: /BBPFormula.html
[34]: /CauchyIntegralFormula.html
[35]: https://arxiv.org/pdf/hep-th/9408175
[36]: https://functions.wolfram.com/About/ourvision.html
[37]: /IsoperimetricPoint.html
[38]: /SoddyCircles.html
[39]: /ApolloniusProblem.html
[40]: https://www.ajur.uni.edu/v3n1/Gisch%20and%20Ribando.pdf
[41]: https://oeis.org/AA014778
[42]: /Hundred-DollarHundred-DigitChallengeProblems.html
[43]: /BinomialCoefficient.html
[44]: https://oeis.org/AA052196
[45]: /Googol.html
[46]: /packages/
[47]: /LagrangeInterpolatingPolynomial.html
