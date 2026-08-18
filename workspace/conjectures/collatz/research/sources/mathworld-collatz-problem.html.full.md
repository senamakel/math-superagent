<!-- source: https://mathworld.wolfram.com/CollatzProblem.html | converted from HTML -->

Collatz Problem -- from Wolfram MathWorld

# Collatz Problem

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

A problem posed by L. Collatz in 1937, also called the [image: 3x+1] mapping, [image: 3n+1] problem, Hasse's algorithm, Kakutani's problem, Syracuse algorithm, Syracuse problem, Thwaites conjecture, and Ulam's problem (Lagarias 1985). Thwaites (1996) has offered a &pound;1000 reward for resolving the [conjecture][2]. Let [image: a_0] be an [integer][3]. Then one form of Collatz problem asks if iterating

[image:  a_n={1/2a_(n-1)   for a_(n-1) even; 3a_(n-1)+1   for a_(n-1) odd ] |

(1)

 |

always returns to 1 for [positive][4][image: a_0]. (If [negative][5] numbers are included, there are four known cycles (excluding the trivial 0 cycle): (4, 2, 1), ([image: -2], [image: -1]), ([image: -5], [image: -14], [image: -7], [image: -20], [image: -10]), and ([image: -17], [image: -50], [image: -25], [image: -74], [image: -37], [image: -110], [image: -55], [image: -164], [image: -82], [image: -41], [image: -122], [image: -61], [image: -182], [image: -91], [image: -272], [image: -136], [image: -68], [image: -34]).)

The members of the [sequence][6] produced by the Collatz are sometimes known as [hailstone numbers][7]. Conway proved that the original Collatz problem has no nontrivial cycles of length [image: <400]. Lagarias (1985) showed that there are no nontrivial cycles with length [image: <275000]. Conway (1972) also proved that Collatz-type problems can be formally [undecidable][8]. Kurtz and Simon (2007) proved that a natural generalization of the Collatz problem is undecidable; unfortunately, this proof cannot be applied to the original Collatz problem.

The Collatz algorithm has been tested and found to always reach 1 for all numbers [image: <=19·2^(58) approx 5.48×10^(18)] (Oliveira e Silva 2008), improving the earlier results of [image: 10^(15)] (Vardi 1991, p. 129) and [image: 5.6×10^(13)] (Leavens and Vermeulen 1992). Because of the difficulty in solving this problem, Erdős commented that "mathematics is not yet ready for such problems" (Lagarias 1985).

The following table gives the sequences obtained for the first few starting values (OEIS [A070165][9]).

[image: a_0] | [image: a_0], [image: a_1], [image: a_2], ... |

1 | 1 |

2 | 2, 1 |

3 | 3, 10, 5, 16, 8, 4, 2, 1 |

4 | 4, 2, 1 |

5 | 5, 16, 8, 4, 2, 1 |

6 | 6, 3, 10, 5, 16, 8, 4, 2, 1 |

[image: CollatzSteps]

The numbers of steps required for the algorithm to reach 1 for [image: a_0=1], 2, ... are 0, 1, 7, 2, 5, 8, 16, 3, 19, 6, 14, 9, 9, 17, 17, 4, 12, 20, 20, 7, ... (OEIS [A006577][10]; illustrated above). Of these, the numbers of tripling steps are 0, 0, 2, 0, 1, 2, 5, 0, 6, ... (OEIS [A006667][11]), and the number of halving steps are 0, 1, 5, 2, 4, 6, 11, 3, 13, ... (OEIS [A006666][12]). The smallest starting values of [image: a_0] that yields a Collatz sequence containing [image: n=1], 2, ... are 1, 2, 3, 3, 3, 6, 7, 3, 9, 3, 7, 12, 7, 9, 15, 3, 7, 18, 19, ... (OEIS [A070167][13]).

The Collatz problem can be implemented as an 8- [register machine][14] (Wolfram 2002, p. 100), quasi- [cellular automaton][15] (Cloney *et al. *1987, Bruschi 2005), or 6-color one-dimensional quasi-cellular automaton with local rules but which wraps first and last digits around (Zeleny). In general, the difficulty in constructing true local-rule cellular automata arises from the necessity of a carry operation when multiplying by 3 which, in the worst case, can extend the entire length of the base-[image: b] representation of digits (and thus require propagating information at faster than the CA's speed of light).

The Collatz problem was modified by Terras (1976, 1979), who asked if iterating

[image:  t_n={1/2t_(n-1)   for t_(n-1) even; 1/2(3t_(n-1)+1)   for t_(n-1) odd ] |

(2)

 |

always returns to 1 for initial integer value [image: t_0] (e.g., Lagarias 1985, Cloney *et al. *1987). This is simply the original statement above but combining the division by two into the addition step if [image: t_(n-1)] is odd, thus compressing the number of steps. The following table gives the sequences for the first few starting values [image: t_0=1], 2, ... (OEIS [A070168][16]).

[image: t_0] | [image: t_1], [image: t_2], ... |

1 | 1 |

2 | 2, 1 |

3 | 3, 5, 8, 4, 2, 1 |

4 | 4, 2, 1 |

5 | 5, 8, 4, 2, 1 |

6 | 6, 3, 5, 8, 4, 2, 1 |

7 | 7, 11, 17, 26, 13, 20, 10, 5, 8, 4, 2, 1 |

If [negative][5] numbers are included, there are 4 known cycles: (1, 2), ([image: -1]), ([image: -5], [image: -7], [image: -10]), and ([image: -17], [image: -25], [image: -37], [image: -55], [image: -82], [image: -41], [image: -61], [image: -91], [image: -136], [image: -68], [image: -34]). It is a special case of the "generalized Collatz problem" with [image: d=2], [image: m_0=1], [image: m_1=3], [image: r_0=0], and [image: r_1=-1]. Terras (1976, 1979) also proved that the set of [integers][3][image: S_k={n:n has stopping time <=k}] has a limiting asymptotic density [image: F(k)], such that if [image: N_x(k)] is the number of [image: n] such that [image: n<=x] and [image: sigma(n)<=k], then the limit

[image:  F(k)=lim_(x->infty)(N_x(k))/x, ] |

(3)

 |

exists. Furthermore, [image: F(k)->1] as [image: k->infty], so almost all [integers][3] have a finite stopping time. Finally, for all [image: k>=1],

[image:  1-F(k)=lim_(x->infty)(N_x(k))/x<=2^(-etak), ] |

(4)

 |

where

[image: H(x)] | [image: =] | [image: -xlgx-(1-x)lg(1-x)] |

(5)

 |

[image: theta] | [image: =] | [image: 1/(lg3)] |

(6)

 |

[image: eta] | [image: =] | [image: 1-H(theta)=0.05004...] |

(7)

 |

(Lagarias 1985).

A generalization of the Collatz problem lets [image: d>=2] be a [positive integer][17] and [image: m_0], ..., [image: m_(d-1)] be [nonzero][18] [integers][3]. Also let [image: r_i in Z] satisfy

[image:  r_i=im_i (mod d). ] |

(8)

 |

Then

[image:  T(x)=(m_ix-r_i)/d ] |

(9)

 |

for [image: x=i (mod d)] defines a generalized Collatz mapping. An equivalent form is

[image:  T(x)=|_(m_ix)/d_|+X_i ] |

(10)

 |

for [image: x=i (mod d)] where [image: X_0], ..., [image: X_(d-1)] are [integers][3] and [image: |_r_|] is the [floor function][19]. The problem is connected with [ergodic theory][20] and [Markov chains][21]. Matthews obtained the following table for the mapping

[image:  T_k(x)={1/2x   for x=0 (mod 2); 1/2(3x+k)   for x=1 (mod 2), ] |

(11)

 |

where [image: k=T_(5^k)].

[image: k] | # cycles | max. cycle length |

0 | 5 | 27 |

1 | 10 | 34 |

2 | 13 | 118 |

3 | 17 | 118 |

4 | 19 | 118 |

5 | 21 | 165 |

6 | 23 | 433 |

Matthews and Watts (1984) proposed the following conjectures.

1. If [image: |m_0...m_(d-1)|<d^d], then all trajectories [image: {T^K(n)}] for [image: n in Z] eventually cycle.

2. If [image: |m_0...m_(d-1)|>d^d], then almost all trajectories [image: {T^K(n)}] for [image: n in Z] are divergent, except for an exceptional set of [integers][3][image: n] satisfying

[image:  #{n in S|-X<=n<X}=o(X). ] |

(12)

 |

3. The number of cycles is finite.

4. If the trajectory [image: {T^K(n)}] for [image: n in Z] is not eventually cyclic, then the iterates are uniformly distribution mod [image: d^alpha] for each [image: alpha>=1], with

[image:  lim_(N->infty)1/(N+1)card{K<=N|T^K(n)=j (mod d^alpha)}
 =d^(-alpha)   ] |

(13)

 |

for [image: 0<=j<=d^alpha-1].

Matthews believes that the map

[image:  T(x)={7x+3   for x=0 (mod 3); 1/3(7x+2)   for x=1 (mod 3); 1/3(x-2)   for x=2 (mod 3) ] |

(14)

 |

will either reach 0 (mod 3) or will enter one of the cycles [image: (-1)] or [image: (-2,-4)], and offers a $100 (Australian?) prize for a proof.

---

## See also

[Hailstone Number][7], [Juggler Sequence][22], [Wolfram Sequences][23]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [collatz problem][24]
- [49 tredecillion][25]
- [circle through (0,0), (1,0), (0,1)][26]

## References

Applegate, D. and Lagarias, J. C. "Density Bounds for the [image: 3x+1] Problem 1. Tree-Search Method." *Math. Comput.***64**, 411-426, 1995. Applegate, D. and Lagarias, J. C. "Density Bounds for the [image: 3x+1] Problem 2. Krasikov Inequalities." *Math. Comput.***64**, 427-438, 1995. Bruschi, M. "Two Cellular Automata for the [image: 3x+1] Map." 26 Feb, 2005. [https://arxiv.org/abs/nlin/0502061][27]. Burckel, S. "Functional Equations Associated with Congruential Functions." *Theor. Comp. Sci.***123**, 397-406, 1994. Cloney, T.; Goles, E.; and Vichniac, G. Y. "The [image: 3x+1] Problem: A Quasi Cellular Automaton." *Complex Sys.***1**, 349-360, 1987. Conway, J. H. "Unpredictable Iterations." *Proc. 1972 Number Th. Conf.*, University of Colorado, Boulder, Colorado, pp. 49-52, 1972. Crandall, R. "On the '[image: 3x+1] ' Problem." *Math. Comput.***32**, 1281-1292, 1978. De Mol, L. "Tag Systems and Collatz-Like Functions." *Theor. Comput. Sci.***390**, 92-101, 2008. Everett, C. "Iteration of the Number Theoretic Function [image: f(2n)=n], [image: f(2n+1)=f(3n+2)]." *Adv. Math.***25**, 42-45, 1977. Guy, R. K. "Collatz's Sequence." &sect;E16 in *[Unsolved Problems in Number Theory, 2nd ed.][28]*New York: Springer-Verlag, pp. 215-218, 1994. Kurtz, S. A. and Simon, J. "The Undecidability of the Generalized Collatz Problem." In *[Theory and Applications of Models of Computation: Proceedings of the 4th International Conference (TAMC 2007) Held in Shanghai, May 22-25, 2007][29]*(Ed. J.-Y. Cai, S. B. Cooper, and H. Zhu). Berlin: Springer, pp. 542-553, 2007. Lagarias, J. C. "The [image: 3x+1] Problem and Its Generalizations." *Amer. Math. Monthly***92**, 3-23, 1985. Leavens, G. T. and Vermeulen, M. "[image: 3x+1] Search Programs." *Comput. Math. Appl.***24**, 79-99, 1992. Margenstern, M. and Matiyasevich, Y. "A Binomial Representation of the [image: 3x+1] Problem." *Acta Arith.***91**, 367-378, 1999. Matthews, K. R. "The Generalized [image: 3x+1] Mapping." [http://www.numbertheory.org/pdfs/survey.pdf][30]. Matthews, K. R. "A Generalized [image: 3x+1] Conjecture." [$100 Reward for a Proof.] [http://www.numbertheory.org/gnubc/challenge][31]. Matthews, K. R. and Watts, A. M. "A Generalization of Hasses's Generalization of the Syracuse Algorithm." *Acta Arith.***43**, 167-175, 1984. Oliveira e Silva, T. "Maximum Excursion and Stopping Time Record-Holders for the [image: 3x+1] Problem: Computational Results." *Math. Comput.***68**, 371-384, 1999. Oliveira e Silva, T. "Computational Verification of the [image: 3x+1] Conjecture." Sep. 19, 2008. [https://sweet.ua.pt/tos/3x+1.html][32]. Schroeppel, R.; Gosper, R. W.; Henneman, W.; and Banks, R. Item 133 in Beeler, M.; Gosper, R. W.; and Schroeppel, R. *HAKMEM.*Cambridge, MA: MIT Artificial Intelligence Laboratory, Memo AIM-239, p. 64, Feb. 1972. [https://www.inwap.com/pdp10/hbaker/hakmem/flows.html#item133][33]. Sloane, N. J. A. Sequences [A006577][10] /M4323, [A006666][12] /M3733, [A006667][11] /M0019, [A070165][9], [A070166][34], [A070167][13], [A070168][16], in "The On-Line Encyclopedia of Integer Sequences." Terras, R. "A Stopping Time Problem on the Positive Integers." *Acta Arith.***30**, 241-252, 1976. Terras, R. "On the Existence of a Density." *Acta Arith.***35**, 101-102, 1979. Thwaites, B. "Two Conjectures, or How to Win &pound;1100." *Math. Gaz.***80**, 35-36, 1996. Vardi, I. "The [image: 3x+1] Problem." Ch. 7 in *[Computational Recreations in Mathematica.][35]*Redwood City, CA: Addison-Wesley, pp. 129-137, 1991. Wirsching, G. J. "&Uuml;ber das [image: 3n+1] Problem." *Elem. Math.***55**, 142-155, 2000. Wolfram, S. *[A New Kind of Science.][36]*Champaign, IL: Wolfram Media, pp. [100][37], [122][38], and [904][39], 2002. Zeleny, E. "Collatz Problem as a Cellular Automaton." 2007. [https://demonstrations.wolfram.com/CollatzProblemAsACellularAutomaton/][40].

## Referenced on Wolfram|Alpha

[Collatz Problem][24]

## Cite this as:

[Weisstein, Eric W.][41] "Collatz Problem." From **[MathWorld][42] --A Wolfram Resource. [https://mathworld.wolfram.com/CollatzProblem.html][43]

## Subject classifications


## Links

[1]: /notebooks/IntegerSequences/CollatzProblem.nb
[2]: /Conjecture.html
[3]: /Integer.html
[4]: /Positive.html
[5]: /Negative.html
[6]: /Sequence.html
[7]: /HailstoneNumber.html
[8]: /Undecidable.html
[9]: http://oeis.org/A070165
[10]: http://oeis.org/A006577
[11]: http://oeis.org/A006667
[12]: http://oeis.org/A006666
[13]: http://oeis.org/A070167
[14]: /RegisterMachine.html
[15]: /CellularAutomaton.html
[16]: http://oeis.org/A070168
[17]: /PositiveInteger.html
[18]: /Nonzero.html
[19]: /FloorFunction.html
[20]: /ErgodicTheory.html
[21]: /MarkovChain.html
[22]: /JugglerSequence.html
[23]: /WolframSequences.html
[24]: https://www.wolframalpha.com/input/?i=collatz+problem
[25]: https://www.wolframalpha.com/input/?i=49+tredecillion
[26]: https://www.wolframalpha.com/input/?i=circle+through+%280%2C0%29%2C+%281%2C0%29%2C+%280%2C1%29
[27]: https://arxiv.org/pdf/nlin/0502061
[28]: http://www.amazon.com/exec/obidos/ASIN/0387208607/ref=nosim/ericstreasuretro
[29]: http://www.amazon.com/exec/obidos/ASIN/3540725032/ref=nosim/ericstreasuretro
[30]: http://www.numbertheory.org/pdfs/survey.pdf
[31]: http://www.numbertheory.org/gnubc/challenge
[32]: https://sweet.ua.pt/tos/3x+1.html
[33]: https://www.inwap.com/pdp10/hbaker/hakmem/flows.html#item133
[34]: http://oeis.org/A070166
[35]: http://www.amazon.com/exec/obidos/ASIN/0685479412/ref=nosim/ericstreasuretro
[36]: http://www.amazon.com/exec/obidos/ASIN/1579550088/ref=nosim/ericstreasuretro
[37]: https://www.wolframscience.com/nks/p100--register-machines/
[38]: https://www.wolframscience.com/nks/p122--elementary-arithmetic/
[39]: https://www.wolframscience.com/nks/p904--elementary-arithmetic/
[40]: https://demonstrations.wolfram.com/CollatzProblemAsACellularAutomaton/
[41]: /about/author.html
[42]: /
[43]: https://mathworld.wolfram.com/CollatzProblem.html
