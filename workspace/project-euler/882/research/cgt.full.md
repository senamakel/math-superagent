<!-- source: https://en.wikipedia.org/wiki/Combinatorial_game_theory | converted from HTML -->

Combinatorial game theory - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Branch of game theory about two-player sequential games with perfect information

This article is about the theory of combinatorial games. For the theory that includes games of chance and games of imperfect knowledge, see [Game theory][1].

[2] Mathematicians playing [Kōnane][3] at a combinatorial game theory workshop

**Combinatorial game theory**is a branch of [mathematics][4] and [theoretical computer science][5] that typically studies [sequential games][6] with [perfect information][7]. Research in this field has primarily focused on two-player [games][8] in which a *position*evolves through alternating *moves*, each governed by well-defined rules, with the aim of achieving a specific winning condition. Unlike [economic game theory][1], combinatorial game theory generally avoids the study of [games of chance][9] or games involving [imperfect information][10], preferring instead games in which the current state and the full set of available moves are always known to both players. [1] However, as mathematical techniques develop, the scope of analyzable games expands, and the boundaries of the field continue to evolve. [2] Authors typically define the term "game" at the outset of academic papers, with definitions tailored to the specific game under analysis rather than reflecting the field’s full scope.

[Combinatorial][11] games include well-known examples such as [chess][12], [checkers][13], and [Go][14], which are considered complex and non-trivial, as well as simpler, "solved" games like [tic-tac-toe][15]. Some combinatorial games, such as [infinite chess][16], may feature an [unbounded][17] playing area. In the context of combinatorial game theory, the structure of such games is typically modeled using a [game tree][18]. The field also encompasses single-player puzzles like [Sudoku][19], and zero-player automata such as [Conway's Game of Life][20] —although these are sometimes more accurately categorized as [mathematical puzzles][21] or [automata][22], given that the strictest definitions of "game" imply the involvement of multiple participants. [3]

A key concept in combinatorial game theory is that of the [solved game][23]. For instance, [tic-tac-toe][15] is solved in that optimal play by both participants always results in a draw. Determining such outcomes for more complex games is significantly more difficult. Notably, in 2007, [checkers][24] was announced to be [weakly solved][25], with perfect play by both sides leading to a draw; however, this result required a [computer-assisted proof][26]. [4] Many real-world games remain too complex for complete analysis, though combinatorial methods have shown some success in the study of [Go endgames][27]. In combinatorial game theory, analyzing a *position*means finding the best sequence of moves for both players until the game ends, but this becomes extremely difficult for anything more complex than simple games.

It is useful to distinguish between combinatorial "mathgames"—games of primary interest to mathematicians and scientists for theoretical exploration—and "playgames," which are more widely played for entertainment and competition. [5] Some games, such as [Nim][28], straddle both categories. Nim played a foundational role in the development of combinatorial game theory and was among the earliest games to be programmed on a computer. [6] [Tic-tac-toe][15] continues to be used in teaching fundamental concepts of [game AI][29] design to [computer science][30] students. [7]

## Difference with traditional game theory

[[edit][31]]

Combinatorial game theory contrasts with "traditional" or "economic" [game theory][1], which, although it can address [sequential play][32], often incorporates elements of [probability][33] and [incomplete information][34]. While economic game theory employs [utility theory][35] and equilibrium concepts, combinatorial game theory is primarily concerned with [two-player][36] [perfect-information games][37] and has pioneered novel techniques for analyzing [game trees][18], such as through the use of [surreal numbers][38], which represent a subset of all two-player perfect-information games. The types of games studied in this field are of particular interest in areas such as [artificial intelligence][39], especially for tasks in [automated planning][40] and [scheduling][41]. However, there is a distinction in emphasis: while economic game theory tends to focus on practical algorithms—such as the [alpha–beta pruning][42] strategy commonly taught in AI courses—combinatorial game theory places greater weight on theoretical results, including the analysis of [game complexity][43] and the existence of optimal strategies through methods like the [strategy-stealing argument][44].

## History

[[edit][45]]

Combinatorial game theory arose in relation to the theory of [impartial games][46], in which any play available to one player must be available to the other as well. One such game is [Nim][28], which can be solved completely. Nim is an impartial game for two players, and subject to the *[normal play condition][47]*, which means that a player who cannot move loses. In the 1930s, the [Sprague–Grundy theorem][48] showed that all impartial games are equivalent to heaps in Nim, thus showing that major unifications are possible in games considered at a combinatorial level, in which detailed strategies matter, not just pay-offs.

In the 1960s, [Elwyn R. Berlekamp][49], [John H. Conway][50] and [Richard K. Guy][51] jointly introduced the theory of a [partisan game][52], in which the requirement that a play available to one player be available to both is relaxed. Their results were published in their book *[Winning Ways for your Mathematical Plays][53]*in 1982. However, the first work published on the subject was Conway's 1976 book *[On Numbers and Games][54]*, also known as ONAG, which introduced the concept of [surreal numbers][38] and the generalization to games. *On Numbers and Games*was also a fruit of the collaboration between Berlekamp, Conway, and Guy.

Combinatorial games are generally, by convention, put into a form where one player wins when the other has no moves remaining. It is easy to convert any finite game with only two possible results into an equivalent one where this convention applies. One of the most important concepts in the theory of combinatorial games is that of the [sum][55] of two games, which is a game where each player may choose to move either in one game or the other at any point in the game, and a player wins when his opponent has no move in either game. This way of combining games leads to a rich and powerful mathematical structure.

Conway stated in *On Numbers and Games*that the inspiration for the theory of partisan games was based on his observation of the play in [Go][56] endgames, which can often be decomposed into sums of simpler endgames isolated from each other in different parts of the board.

## Examples

[[edit][57]]

The introductory text *[Winning Ways][58]*introduced a large number of games, but the following were used as motivating examples for the introductory theory:

- Blue–Red [Hackenbush][59] - At the finite level, this partisan combinatorial game allows constructions of games whose values are [dyadic rational numbers][60]. At the infinite level, it allows one to construct all real values, as well as many infinite ones that fall within the class of [surreal numbers][61].
- Blue–Red–Green Hackenbush - Allows for additional game values that are not numbers in the traditional sense, for example, [star][62].
- [Toads and Frogs][63] - Allows various game values. Unlike most other games, a position is easily represented by a short string of characters.
- [Domineering][64] - Various interesting games, such as [hot games][65], appear as positions in Domineering, because there is sometimes an incentive to move, and sometimes not. This allows discussion of a game's [temperature][66].
- [Nim][28] - An [impartial game][46]. This allows for the construction of the [nimbers][67]. (It can also be seen as a green-only special case of Blue-Red-Green Hackenbush.)

The classic game [Go][56] was influential on the early combinatorial game theory, and Berlekamp and Wolfe subsequently developed an endgame and *temperature*theory for it (see references). Armed with this they were able to construct plausible Go endgame positions from which they could give expert Go players a choice of sides and then defeat them either way.

Another game studied in the context of combinatorial game theory is [chess][12]. In 1953 [Alan Turing][68] wrote of the game, "If one can explain quite unambiguously in English, with the aid of mathematical symbols if required, how a calculation is to be done, then it is always possible to programme any digital computer to do that calculation, provided the storage capacity is adequate." [8] In a 1950 paper, [Claude Shannon][69] estimated the lower bound of the [game-tree complexity][43] of chess to be 10 120, and today this is referred to as the [Shannon number][70]. [9] Chess remains unsolved, although extensive study, including work involving the use of supercomputers has created chess endgame [tablebases][71], which shows the result of perfect play for all end-games with seven pieces or less. [Infinite chess][16] has an even greater combinatorial complexity than chess (unless only limited end-games, or composed positions with a small number of pieces are being studied).

## Overview

[[edit][72]]

A game, in its simplest terms, is a list of possible "moves" that two players, called *left*and *right*, can make. The game position resulting from any move can be considered to be another game. This idea of viewing games in terms of their possible moves to other games leads to a [recursive][73] mathematical definition of games that is standard in combinatorial game theory. In this definition, each game has the notation **{L|R}**. L is the [set][74] of game positions that the left player can move to, and R is the set of game positions that the right player can move to; each position in L and R is defined as a game using the same notation.

Using [Domineering][64] as an example, label each of the sixteen boxes of the four-by-four board by A1 for the upper leftmost square, C2 for the third box from the left on the second row from the top, and so on. We use e.g. (D3, D4) to stand for the game position in which a vertical domino has been placed in the bottom right corner. Then, the initial position can be described in combinatorial game theory notation as

{ ( A 1, A 2), ( B 1, B 2), … | ( A 1, B 1), ( A 2, B 2), … }. {\displaystyle \{(\mathrm {A} 1,\mathrm {A} 2),(\mathrm {B} 1,\mathrm {B} 2),\dots |(\mathrm {A} 1,\mathrm {B} 1),(\mathrm {A} 2,\mathrm {B} 2),\dots \}.}[image: {\displaystyle \{(\mathrm {A} 1,\mathrm {A} 2),(\mathrm {B} 1,\mathrm {B} 2),\dots |(\mathrm {A} 1,\mathrm {B} 1),(\mathrm {A} 2,\mathrm {B} 2),\dots \}.}]

In standard Cross-Cram play, the players alternate turns, but this alternation is handled implicitly by the definitions of combinatorial game theory rather than being encoded within the game states.

[75] [75] [75] { ( A 1, A 2) | ( A 1, B 1) } = { { | } | { | } }. {\displaystyle \{(\mathrm {A} 1,\mathrm {A} 2)|(\mathrm {A} 1,\mathrm {B} 1)\}=\{\{|\}|\{|\}\}.}[image: {\displaystyle \{(\mathrm {A} 1,\mathrm {A} 2)|(\mathrm {A} 1,\mathrm {B} 1)\}=\{\{|\}|\{|\}\}.}]

The above game describes a scenario in which there is only one move left for either player, and if either player makes that move, that player wins. (An irrelevant open square at C3 has been omitted from the diagram.) The {|} in each player's move list (corresponding to the single leftover square after the move) is called the [zero game][76], and can actually be abbreviated 0. In the zero game, neither player has any valid moves; thus, the player whose turn it is when the zero game comes up automatically loses.

The type of game in the diagram above also has a simple name; it is called the [star game][62], which can also be abbreviated ∗. In the star game, the only valid move leads to the zero game, which means that whoever's turn comes up during the star game automatically wins.

## Game abbreviations

[[edit][77]]

### Numbers

[[edit][78]]

Numbers represent the number of free moves, or the move advantage of a particular player. By convention positive numbers represent an advantage for Left, while negative numbers represent an advantage for Right. They are defined recursively with 0 being the base case.

0 = {|} 1 = {0|}, 2 = {1|}, 3 = {2|} −1 = {|0}, −2 = {|−1}, −3 = {|−2}

The [zero game][76] is a loss for the first player.

The sum of number games behaves like the integers, for example 3 + −2 = 1.

Any game number is in the class of the [surreal numbers][61].

### Star

[[edit][79]]

Main article: [Star (game theory)][62]

*Star*, written as ∗ or {0|0}, is a first-player win since either player must (if first to move in the game) move to a zero game, and therefore win.

∗ + ∗ = 0, because the first player must turn one copy of ∗ to a 0, and then the other player will have to turn the other copy of ∗ to a 0 as well; at this point, the first player would lose, since 0 + 0 admits no moves.

The game ∗ is neither positive nor negative; it and all other games in which the first player wins (regardless of which side the player is on) are said to be *[fuzzy][80]*or *confused with 0*; symbolically, we write ∗ || 0.

The game ∗n is notation for {0, ∗, …, ∗(n−1)| 0, ∗, …, ∗(n−1)}, which is also representative of normal-play [Nim][28] with a single heap of n objects. (Note that ∗0 = 0 and ∗1 = ∗.)

### Up and down

[[edit][81]]

Main article: [Up (game theory)][82]

*Up*, written as ↑, is a position in combinatorial game theory. [10] In standard notation, ↑ = {0|∗}. Its negative is called *down*.

−↑ = ↓ (*down*)

Up is strictly positive (↑ > 0), and down is strictly negative (↓ < 0), but both are [infinitesimal][83]. Up and down are defined in *[Winning Ways for your Mathematical Plays][53]*.

### "Hot" games

[[edit][84]]

Main article: [Hot game][65]

Consider the game {1|−1}. Both moves in this game are an advantage for the player who makes them; so the game is said to be "hot;" it is greater than any number less than −1, less than any number greater than 1, and fuzzy with any number in between. It is written as ±1. Note that a subclass of hot games, referred to as ±n for some numerical game n is a switch game. Switch games can be added to numbers, or multiplied by positive ones, in the expected fashion; for example, 4 ± 1 = {5|3}.

## Nimbers

[[edit][85]]

An [impartial game][46] is one where, at every position of the game, the same moves are available to both players. For instance, [Nim][28] is impartial, as any set of objects that can be removed by one player can be removed by the other. However, [domineering][64] is not impartial, because one player places horizontal dominoes and the other places vertical ones. Likewise Checkers is not impartial, since the players own different colored pieces. For any [ordinal number][86], one can define an impartial game generalizing Nim in which, on each move, either player may replace the number with any smaller ordinal number; the games defined in this way are known as [nimbers][67]. The [Sprague–Grundy theorem][48] states that every impartial game under the [normal play convention][47] is equivalent to a nimber.

The "smallest" nimbers – the simplest and least under the usual ordering of the ordinals – are 0 and ∗.

## See also

[[edit][87]]

- [Alpha–beta pruning][42], an optimised algorithm for searching the game tree
- [Backward induction][88], reasoning backwards from a final situation
- [Cooling and heating (combinatorial game theory)][89], various transformations of games making them more amenable to the theory
- [Connection game][90], a type of game where players attempt to establish connections
- [Endgame tablebase][71], a database saying how to play endgames
- [Expectiminimax tree][91], an adaptation of a minimax game tree to games with an element of chance
- [Extensive-form game][32], a game tree enriched with payoffs and information available to players
- [Game classification][92], an article discussing ways of classifying games
- [Game complexity][43], an article describing ways of measuring the complexity of games
- [Grundy's game][93], a mathematical game in which heaps of objects are split
- [Multi-agent system][94], a type of computer system for tackling complex problems
- [Positional game][95], a type of game where players claim previously-unclaimed positions
- [Solving chess][96]
- [Sylver coinage][97], a mathematical game of choosing positive integers that are not the sum of non-negative multiples of previously chosen integers
- [Wythoff's game][98], a mathematical game of taking objects from one or two piles
- [Topological game][99], a type of mathematical game played in a topological space
- [Zugzwang][100], being obliged to play when this is disadvantageous

## Notes

[[edit][101]]

1. ↑ Lessons in Play, p. 3
2. ↑ Thomas S. Fergusson's analysis of poker is an example of combinatorial game theory expanding into games that include elements of chance. Research into Three Player Nim is an example of study expanding beyond two player games. Conway, Guy and Berlekamp's analysis of partisan games is perhaps the most famous expansion of the scope of combinatorial game theory, taking the field beyond the study of impartial games.
3. ↑ [Demaine, Erik D.][102]; [Hearn, Robert A.][103] (2009). ["Playing games with algorithms: algorithmic combinatorial game theory"][104]. In Albert, Michael H.; Nowakowski, Richard J. (eds.). *Games of No Chance 3*. Mathematical Sciences Research Institute Publications. Vol. 56. Cambridge University Press. pp. 3– 56. [arXiv][105]: [cs.CC/0106019][106].
4. ↑ Schaeffer, J.; Burch, N.; Bjornsson, Y.; Kishimoto, A.; Muller, M.; Lake, R.; Lu, P.; Sutphen, S. (2007). "Checkers is solved". *[Science][107]*. **317**(5844): 1518– 1522. [Bibcode][108]: [2007Sci...317.1518S][109]. [CiteSeerX][110] [10.1.1.95.5393][111]. [doi][112]: [10.1126/science.1144079][113]. [PMID][114] [17641166][115]. [S2CID][116] [10274228][117].`{{ [cite journal][118] }}`: Cite uses deprecated parameter `| citeseerx=`( [help][119])
5. ↑ Fraenkel, Aviezri (2009). "Combinatorial Games: selected bibliography with a succinct gourmet introduction". *Games of No Chance 3*. **56**: 492.
6. ↑ Grant, Eugene F.; Lardner, Rex (2 August 1952). ["The Talk of the Town - It"][120]. *[The New Yorker][121]*.
7. ↑ [Russell, Stuart][122]; [Norvig, Peter][123] (2021). "Chapter 5: Adversarial search and games". **[Artificial Intelligence: A Modern Approach][124]. Pearson series in artificial intelligence (4th ed.). Pearson Education, Inc. pp. 146– 179. [ISBN][125] [978-0-13-461099-3][126].
8. ↑ Alan Turing. ["Digital computers applied to games"][127]. University of Southampton and King's College Cambridge. p. 2.
9. ↑ [Claude Shannon][69] (1950). ["Programming a Computer for Playing Chess"][128] (PDF). *Philosophical Magazine*. **41**(314): 4. Archived from [the original][129] (PDF) on 2010-07-06.
10. ↑ E. Berlekamp; J. H. Conway; R. Guy (1982). *[Winning Ways for your Mathematical Plays][53]*. Vol. I. Academic Press. [ISBN][125] [0-12-091101-9][130].
E. Berlekamp; J. H. Conway; R. Guy (1982). *Winning Ways for your Mathematical Plays*. Vol. II. Academic Press. [ISBN][125] [0-12-091102-7][131].

## References

[[edit][132]]

- [Albert, Michael H.][133]; Nowakowski, Richard J.; Wolfe, David (2007). *Lessons in Play: An Introduction to Combinatorial Game Theory*. A K Peters Ltd. [ISBN][125] [978-1-56881-277-9][134].
- [Beck, József][135] (2008). **[Combinatorial games: tic-tac-toe theory][136]. Cambridge University Press. [ISBN][125] [978-0-521-46100-9][137].
- [Berlekamp, E.][138]; [Conway, J. H.][139]; [Guy, R.][51] (1982). *[Winning Ways for your Mathematical Plays][53]: Games in general*. Academic Press. [ISBN][125] [0-12-091101-9][130]. 2nd ed., A K Peters Ltd (2001–2004), [ISBN][125] [1-56881-130-6][140], [ISBN][125] [1-56881-142-X][141]
- Berlekamp, E.; Conway, J. H.; [Guy, R.][51] (1982). **[Winning Ways for your Mathematical Plays: Games in particular][142]. Academic Press. [ISBN][125] [0-12-091102-7][131]. 2nd ed., A K Peters Ltd (2001–2004), [ISBN][125] [1-56881-143-8][143], [ISBN][125] [1-56881-144-6][144].
- [Berlekamp, Elwyn][138]; [Wolfe, David][145] (1997). **[Mathematical Go: Chilling Gets the Last Point][146]. A K Peters Ltd. [ISBN][125] [1-56881-032-6][147].
- [Bewersdorff, Jörg][148] (2021). *Luck, Logic and White Lies: The Mathematics of Games*(2nd ed.). A K Peters/CRC Press. [doi][112]: [10.1201/9781003092872][149]. [ISBN][125] [978-1-003-09287-2][150]. See especially sections 21–26.
- [Conway, John Horton][139] (1976). *[On Numbers and Games][54]*. Academic Press. [ISBN][125] [0-12-186350-6][151]. 2nd ed., A K Peters Ltd (2001), [ISBN][125] [1-56881-127-6][152].
- [Robert A. Hearn][103]; Erik D. Demaine (2009). **[Games, Puzzles, and Computation][153]. A K Peters, Ltd. [ISBN][125] [978-1-56881-322-6][154].

## External links

[[edit][155]]

- [List of combinatorial game theory links][156] at the homepage of [David Eppstein][157]
- [An Introduction to Conway's games and numbers][158] by Dierk Schleicher and Michael Stoll
- [Combinational Game Theory terms summary][159] by Bill Spight
- [Combinatorial Game Theory Workshop, Banff International Research Station, June 2005][160]

- [v][161]
- [t][162]
- [e][163]

[Game theory][1]

 |

- [Glossary][164]
- [Game theorists][165]
- [Games][166]

 |

Traditional [game theory][1]

 |

[Definitions][167] |

- [Asynchrony][168]
- [Bayesian regret][169]
- [Best response][170]
- [Bounded rationality][171]
- [Cheap talk][172]
- [Coalition][173]
- [Complete contract][174]
- [Complete information][175]
- [Complete mixing][176]
- [Conjectural variation][177]
- [Contingent cooperator][178]
- [Coopetition][179]
- [Cooperative game theory][180]
- [Dynamic inconsistency][181]
- [Escalation of commitment][182]
- [Farsightedness][183]
- [Game semantics][184]
- [Hierarchy of beliefs][185]
- [Imperfect information][10]
- [Incomplete information][34]
- [Information set][186]
- [Move by nature][187]
- [Mutual knowledge][188]
- [Non-cooperative game theory][189]
- [Non-credible threat][190]
- [Outcome][191]
- [Perfect information][7]
- [Perfect recall][192]
- [Ply][193]
- [Preference][194]
- [Rationality][195]
- [Sequential game][6]
- [Simultaneous action selection][196]
- [Spite][197]
- [Strategic complements][198]
- [Strategic dominance][199]
- [Strategic form][200]
- [Strategic interaction][201]
- [Strategic move][202]
- [Strategy][203]
- [Subgame][204]
- [Succinct game][205]
- [Topological game][99]
- [Tragedy of the commons][206]
- [Uncorrelated asymmetry][207]
- [Win–win game][208]
- [Zero-sum game][209]

 |

[Equilibrium concepts][210] |

- [Backward induction][88]
- [Bayes correlated equilibrium][211]
- [Bayesian efficiency][212]
- [Bayesian game][213]
- [Bayesian Nash equilibrium][214]
- [Berge equilibrium][215]
- [Bertrand–Edgeworth model][216]
- [Coalition-proof Nash equilibrium][217]
- [Core][218]
- [Correlated equilibrium][219]
- [Cursed equilibrium][220]
- [Edgeworth price cycle][221]
- [Epsilon-equilibrium][222]
- [Gibbs equilibrium][223]
- [Incomplete contracts][224]
- [Inequity aversion][225]
- [Individual rationality][226]
- [Iterated elimination of dominated strategies][227]
- [Markov perfect equilibrium][228]
- [Mertens-stable equilibrium][229]
- [Nash equilibrium][230]
- [Open-loop model][231]
- [Pareto efficiency][232]
- [Payoff dominance][233]
- [Perfect Bayesian equilibrium][234]
- [Price of anarchy][235]
- [Program equilibrium][236]
- [Proper equilibrium][237]
- [Quantal response equilibrium][238]
- [Quasi-perfect equilibrium][239]
- [Rational agent][240]
- [Rationalizable strategy][241]
- [Satisfaction equilibrium][242]
- [Self-confirming equilibrium][243]
- [Sequential equilibrium][244]
- [Shapley value][245]
- [Strong Nash equilibrium][246]
- [Subgame perfect equilibrium][247]
- [Trembling hand equilibrium][248]

 |

[Strategies][203] |

- [Appeasement][249]
- [Bid shading][250]
- [Cheap talk][172]
- [Collusion][251]
- [Commitment device][252]
- [De-escalation][253]
- [Deterrence][254]
- [Escalation][255]
- [Fictitious play][256]
- [Focal point][257]
- [Grim trigger][258]
- [Hobbesian trap][259]
- [Markov strategy][260]
- [Max-dominated strategy][261]
- [Mixed strategy][262]
- [Pure strategy][203]
- [Tit for tat][263]
- [Win–stay, lose–switch][264]

 |

[Games][166] |

- [All-pay auction][265]
- [Battle of the sexes][266]
- [Nash bargaining game][267]
- [Bertrand competition][268]
- [Blotto game][269]
- [Centipede game][270]
- [Coordination game][271]
- [Cournot competition][272]
- [Deadlock][273]
- [Dictator game][274]
- [Trust game][275]
- [Diner's dilemma][276]
- [Dollar auction][277]
- [El Farol Bar problem][278]
- [Electronic mail game][279]
- [Gift-exchange game][280]
- [Guess 2/3 of the average][281]
- [Keynesian beauty contest][282]
- [Kuhn poker][283]
- [Lewis signaling game][284]
- [Matching pennies][285]
- [Obligationes][286]
- [Optional prisoner's dilemma][287]
- [Pirate game][288]
- [Prisoner's dilemma][289]
- [Public goods game][290]
- [Rendezvous problem][291]
- [Rock paper scissors][292]
- [Stackelberg competition][293]
- [Stag hunt][294]
- [Traveler's dilemma][295]
- [Ultimatum game][296]
- [Volunteer's dilemma][297]
- [War of attrition][298]

 |

[Theorems][299] |

- [Arrow's impossibility theorem][300]
- [Aumann's agreement theorem][301]
- [Brouwer fixed-point theorem][302]
- [Competitive altruism][303]
- [Folk theorem][304]
- [Gibbard–Satterthwaite theorem][305]
- [Gibbs lemma][306]
- [Glicksberg's theorem][307]
- [Kakutani fixed-point theorem][308]
- [Kuhn's theorem][309]
- [One-shot deviation principle][310]
- [Prim–Read theory][311]
- [Rational ignorance][312]
- [Rational irrationality][313]
- [Sperner's lemma][314]
- [Zermelo's theorem][315]

 |

Subfields |

- [Algorithmic game theory][316]
- [Behavioral game theory][317]
- [Behavioral strategy][318]
- [Compositional game theory][319]
- [Confrontation analysis][320]
- [Contract theory][321]
- [Drama theory][322]
- [Graphical game theory][323]
- [Heresthetic][324]
- [Mean-field game theory][325]
- [Negotiation theory][326]
- [Quantum game theory][327]
- [Social software][328]

 |

Key people |

- [Albert W. Tucker][329]
- [Alvin E. Roth][330]
- [Amos Tversky][331]
- [Antoine Augustin Cournot][332]
- [Ariel Rubinstein][333]
- [David Gale][334]
- [David K. Levine][335]
- [David M. Kreps][336]
- [Donald B. Gillies][337]
- [Drew Fudenberg][338]
- [Eric Maskin][339]
- [Harold W. Kuhn][340]
- [Herbert Simon][341]
- [Herbert Scarf][342]
- [Hervé Moulin][343]
- [Jean Tirole][344]
- [Jean-François Mertens][345]
- [Jennifer Tour Chayes][346]
- [Ken Binmore][347]
- [Kenneth Arrow][348]
- [Leonid Hurwicz][349]
- [Lloyd Shapley][350]
- [Martin Shubik][351]
- [Melvin Dresher][352]
- [Merrill M. Flood][353]
- [Olga Bondareva][354]
- [Oskar Morgenstern][355]
- [Paul Milgrom][356]
- [Peyton Young][357]
- [Reinhard Selten][358]
- [Robert Aumann][359]
- [Robert Axelrod][360]
- [Robert B. Wilson][361]
- [Roger Myerson][362]
- [Samuel Bowles][363]
- [Suzanne Scotchmer][364]
- [Thomas Schelling][365]
- [William Vickrey][366]

 |

 |

 |

[Combinatorial game theory][367]

 |

Core
concepts |

- [Combinatorial explosion][368]
- [Determinacy][369]
- [Disjunctive sum][55]
- [First-player and second-player win][370]
- [Game complexity][43]
- [Game tree][18]
- [Impartial game][46]
- [Misère][371]
- [Partisan game][52]
- [Solved game][23]
- [Sprague–Grundy theorem][48]
- [Strategy-stealing argument][44]
- [Zugzwang][100]

 |

Games |

- [Chess][12]
- [Chomp][372]
- [Clobber][373]
- [Cram][374]
- [Domineering][64]
- [Hackenbush][59]
- [Nim][28]
- [Notakto][375]
- [Subtract a square][376]
- [Sylver coinage][97]
- [Toads and Frogs][63]

 |

Mathematical
tools |

- [Mex][377]
- [Nimber][67]
- [On Numbers and Games][54]
- [Star][62]
- [Surreal number][38]
- [Winning Ways for Your Mathematical Plays][378]

 |

Search
algorithms |

- [Alpha–beta pruning][42]
- [Expectiminimax][379]
- [Minimax][380]
- [Monte Carlo tree search][381]
- [Negamax][382]
- [Paranoid algorithm][383]
- [Principal variation search][384]

 |

Key people |

- [Claude Shannon][69]
- [John Conway][385]
- [John von Neumann][386]

 |

 |

 |

[Evolutionary game theory][387]

 |

Core
concepts |

- [Bishop–Cannings theorem][388]
- [Evolution and the Theory of Games][389]
- [Evolutionarily stable set][390]
- [Evolutionarily stable state][391]
- [Evolutionarily stable strategy][392]
- [Replicator equation][393]
- [Risk dominance][394]
- [Stochastically stable equilibrium][395]
- [Weak evolutionarily stable strategy][396]

 |

Games |

- [Chicken][397]
- [Stag hunt][294]

 |

Applications |

- [Cultural group selection][398]
- [Fisher's principle][399]
- [Mobbing][400]
- [Terminal investment hypothesis][401]

 |

Key people |

- [John Maynard Smith][402]
- [George R. Price][403]
- [William Donald Hamilton][404]
- [Robert Axelrod][360]

 |

 |

 |

[Mechanism design][405]

 |

Core
concepts |

- [Algorithmic mechanism design][406]
- [Bayesian-optimal mechanism][407]
- [Incentive compatibility][408]
- [Market design][409]
- [Myerson ironing][410]
- [Monotonicity][411]
- [Participation constraint][412]
- [Revelation principle][413]
- [Strategyproofness][414]
- [Vickrey–Clarke–Groves mechanism][415]
- [Virtual valuation][416]

 |

Theorems |

- [Myerson–Satterthwaite theorem][417]
- [Revenue equivalence][418]
- [Border's theorem][419]

 |

Applications |

- [Digital goods auction][420]
- [Knapsack auction][421]
- [Truthful cake-cutting][422]

 |

 |

 |

Other topics

 |

- [Bertrand paradox][423]
- [Chainstore paradox][424]
- [Computational complexity of games][425]
- [Helly metric][426]
- [Multi-agent system][94]
- [PPAD-complete][427]

 |

 |

- **[image: icon] [428] [Mathematics portal][429]**
- **[image: Wikimedia Commons logo] [430] [Game theory][431]**
- **[WikiProject][432]**
- **[Game theory][433]**

 |

[Authority control databases][434][image: Edit this at Wikidata] [435] |

- [GND][436]

 |

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Combinatorial_game_theory&oldid=1358173260][437] "

[Category][438]:

- [Combinatorial game theory][439]

Hidden categories:

- [Articles with short description][440]
- [Short description matches Wikidata][441]
- [CS1 errors: deprecated parameters][442]
- [Commons category link is on Wikidata][443]

Search

Combinatorial game theory

16 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Game_theory
[2]: https://en.wikipedia.org/wiki/File:Mathematicians_playing_Konane.jpg
[3]: https://en.wikipedia.org/wiki/Kōnane
[4]: https://en.wikipedia.org/wiki/Mathematics
[5]: https://en.wikipedia.org/wiki/Theoretical_computer_science
[6]: https://en.wikipedia.org/wiki/Sequential_game
[7]: https://en.wikipedia.org/wiki/Perfect_information
[8]: https://en.wikipedia.org/wiki/Game
[9]: https://en.wikipedia.org/wiki/Games_of_chance
[10]: https://en.wikipedia.org/wiki/Imperfect_information
[11]: https://en.wikipedia.org/wiki/Combinatorics
[12]: https://en.wikipedia.org/wiki/Chess
[13]: https://en.wikipedia.org/wiki/Draughts
[14]: https://en.wikipedia.org/wiki/Go_(game)
[15]: https://en.wikipedia.org/wiki/Tic-tac-toe
[16]: https://en.wikipedia.org/wiki/Infinite_chess
[17]: https://en.wikipedia.org/wiki/Unbounded_set
[18]: https://en.wikipedia.org/wiki/Game_tree
[19]: https://en.wikipedia.org/wiki/Sudoku
[20]: https://en.wikipedia.org/wiki/Conway's_Game_of_Life
[21]: https://en.wikipedia.org/wiki/Mathematical_puzzle
[22]: https://en.wikipedia.org/wiki/Cellular_automaton
[23]: https://en.wikipedia.org/wiki/Solved_game
[24]: https://en.wikipedia.org/wiki/Checkers
[25]: https://en.wikipedia.org/wiki/Solved_game#Overview
[26]: https://en.wikipedia.org/wiki/Computer-assisted_proof
[27]: https://en.wikipedia.org/wiki/Go_endgame
[28]: https://en.wikipedia.org/wiki/Nim
[29]: https://en.wikipedia.org/wiki/Game_AI
[30]: https://en.wikipedia.org/wiki/Computer_science
[31]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=1
[32]: https://en.wikipedia.org/wiki/Extensive-form_game
[33]: https://en.wikipedia.org/wiki/Probability
[34]: https://en.wikipedia.org/wiki/Incomplete_information
[35]: https://en.wikipedia.org/wiki/Utility_theory
[36]: https://en.wikipedia.org/wiki/Two-player_game
[37]: https://en.wikipedia.org/wiki/Perfect-information_game
[38]: https://en.wikipedia.org/wiki/Surreal_number
[39]: https://en.wikipedia.org/wiki/Artificial_intelligence
[40]: https://en.wikipedia.org/wiki/Automated_planning
[41]: https://en.wikipedia.org/wiki/Scheduling
[42]: https://en.wikipedia.org/wiki/Alpha–beta_pruning
[43]: https://en.wikipedia.org/wiki/Game_complexity
[44]: https://en.wikipedia.org/wiki/Strategy-stealing_argument
[45]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=2
[46]: https://en.wikipedia.org/wiki/Impartial_game
[47]: https://en.wikipedia.org/wiki/Normal_play_convention
[48]: https://en.wikipedia.org/wiki/Sprague–Grundy_theorem
[49]: https://en.wikipedia.org/wiki/Elwyn_R._Berlekamp
[50]: https://en.wikipedia.org/wiki/John_H._Conway
[51]: https://en.wikipedia.org/wiki/Richard_K._Guy
[52]: https://en.wikipedia.org/wiki/Partisan_game
[53]: https://en.wikipedia.org/wiki/Winning_Ways_for_your_Mathematical_Plays
[54]: https://en.wikipedia.org/wiki/On_Numbers_and_Games
[55]: https://en.wikipedia.org/wiki/Disjunctive_sum
[56]: https://en.wikipedia.org/wiki/Go_(board_game)
[57]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=3
[58]: https://en.wikipedia.org/wiki/Winning_Ways
[59]: https://en.wikipedia.org/wiki/Hackenbush
[60]: https://en.wikipedia.org/wiki/Dyadic_rational
[61]: https://en.wikipedia.org/wiki/Surreal_numbers
[62]: https://en.wikipedia.org/wiki/Star_(game_theory)
[63]: https://en.wikipedia.org/wiki/Toads_and_Frogs
[64]: https://en.wikipedia.org/wiki/Domineering
[65]: https://en.wikipedia.org/wiki/Hot_game
[66]: https://en.wikipedia.org/wiki/Temperature_(game_theory)
[67]: https://en.wikipedia.org/wiki/Nimber
[68]: https://en.wikipedia.org/wiki/Alan_Turing
[69]: https://en.wikipedia.org/wiki/Claude_Shannon
[70]: https://en.wikipedia.org/wiki/Shannon_number
[71]: https://en.wikipedia.org/wiki/Endgame_tablebase
[72]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=4
[73]: https://en.wikipedia.org/wiki/Recursion
[74]: https://en.wikipedia.org/wiki/Set_(mathematics)
[75]: https://en.wikipedia.org/wiki/File:20x20square.png
[76]: https://en.wikipedia.org/wiki/Zero_game
[77]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=5
[78]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=6
[79]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=7
[80]: https://en.wikipedia.org/wiki/Fuzzy_game
[81]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=8
[82]: https://en.wikipedia.org/wiki/Up_(game_theory)
[83]: https://en.wikipedia.org/wiki/Infinitesimal
[84]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=9
[85]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=10
[86]: https://en.wikipedia.org/wiki/Ordinal_number
[87]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=11
[88]: https://en.wikipedia.org/wiki/Backward_induction
[89]: https://en.wikipedia.org/wiki/Cooling_and_heating_(combinatorial_game_theory)
[90]: https://en.wikipedia.org/wiki/Connection_game
[91]: https://en.wikipedia.org/wiki/Expectiminimax_tree
[92]: https://en.wikipedia.org/wiki/Game_classification
[93]: https://en.wikipedia.org/wiki/Grundy's_game
[94]: https://en.wikipedia.org/wiki/Multi-agent_system
[95]: https://en.wikipedia.org/wiki/Positional_game
[96]: https://en.wikipedia.org/wiki/Solving_chess
[97]: https://en.wikipedia.org/wiki/Sylver_coinage
[98]: https://en.wikipedia.org/wiki/Wythoff's_game
[99]: https://en.wikipedia.org/wiki/Topological_game
[100]: https://en.wikipedia.org/wiki/Zugzwang
[101]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=12
[102]: https://en.wikipedia.org/wiki/Erik_Demaine
[103]: https://en.wikipedia.org/wiki/Bob_Hearn
[104]: https://erikdemaine.org/papers/AlgGameTheory_GONC3/
[105]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[106]: https://arxiv.org/abs/cs.CC/0106019
[107]: https://en.wikipedia.org/wiki/Science_(journal)
[108]: https://en.wikipedia.org/wiki/Bibcode_(identifier)
[109]: https://ui.adsabs.harvard.edu/abs/2007Sci...317.1518S
[110]: https://en.wikipedia.org/wiki/CiteSeerX_(identifier)
[111]: https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.95.5393
[112]: https://en.wikipedia.org/wiki/Doi_(identifier)
[113]: https://doi.org/10.1126%2Fscience.1144079
[114]: https://en.wikipedia.org/wiki/PMID_(identifier)
[115]: https://pubmed.ncbi.nlm.nih.gov/17641166
[116]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[117]: https://api.semanticscholar.org/CorpusID:10274228
[118]: https://en.wikipedia.org/wiki/Template:Cite_journal
[119]: https://en.wikipedia.org/wiki/Help:CS1_errors#deprecated_params
[120]: http://www.newyorker.com/archive/1952/08/02/1952_08_02_018_TNY_CARDS_000236053
[121]: https://en.wikipedia.org/wiki/The_New_Yorker
[122]: https://en.wikipedia.org/wiki/Stuart_J._Russell
[123]: https://en.wikipedia.org/wiki/Peter_Norvig
[124]: https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach
[125]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[126]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-13-461099-3
[127]: https://turingarchive.kings.cam.ac.uk/publications-lectures-and-talks-amtb/amt-b-7
[128]: https://web.archive.org/web/20100706211229/http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf
[129]: http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf
[130]: https://en.wikipedia.org/wiki/Special:BookSources/0-12-091101-9
[131]: https://en.wikipedia.org/wiki/Special:BookSources/0-12-091102-7
[132]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=13
[133]: https://en.wikipedia.org/wiki/Michael_H._Albert
[134]: https://en.wikipedia.org/wiki/Special:BookSources/978-1-56881-277-9
[135]: https://en.wikipedia.org/wiki/József_Beck
[136]: https://en.wikipedia.org/wiki/Combinatorial_Games:_Tic-Tac-Toe_Theory
[137]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-46100-9
[138]: https://en.wikipedia.org/wiki/Elwyn_Berlekamp
[139]: https://en.wikipedia.org/wiki/John_Horton_Conway
[140]: https://en.wikipedia.org/wiki/Special:BookSources/1-56881-130-6
[141]: https://en.wikipedia.org/wiki/Special:BookSources/1-56881-142-X
[142]: https://archive.org/details/winningwaysforyo02berl
[143]: https://en.wikipedia.org/wiki/Special:BookSources/1-56881-143-8
[144]: https://en.wikipedia.org/wiki/Special:BookSources/1-56881-144-6
[145]: https://en.wikipedia.org/wiki/David_Wolfe_(mathematician)
[146]: https://archive.org/details/mathematicalgoch0000berl
[147]: https://en.wikipedia.org/wiki/Special:BookSources/1-56881-032-6
[148]: https://en.wikipedia.org/wiki/Jörg_Bewersdorff
[149]: https://doi.org/10.1201%2F9781003092872
[150]: https://en.wikipedia.org/wiki/Special:BookSources/978-1-003-09287-2
[151]: https://en.wikipedia.org/wiki/Special:BookSources/0-12-186350-6
[152]: https://en.wikipedia.org/wiki/Special:BookSources/1-56881-127-6
[153]: https://en.wikipedia.org/wiki/Games,_Puzzles,_and_Computation
[154]: https://en.wikipedia.org/wiki/Special:BookSources/978-1-56881-322-6
[155]: /w/index.php?title=Combinatorial_game_theory&amp;action=edit&amp;section=14
[156]: http://www.ics.uci.edu/~eppstein/cgt/
[157]: https://en.wikipedia.org/wiki/David_Eppstein
[158]: https://arxiv.org/abs/math/0410026
[159]: http://senseis.xmp.net/?CGTPath#toc1
[160]: https://web.archive.org/web/20051217072124/http://www.pims.math.ca/birs/birspages.php?task=displayevent&amp;event_id=05w5048
[161]: https://en.wikipedia.org/wiki/Template:Game_theory
[162]: https://en.wikipedia.org/wiki/Template_talk:Game_theory
[163]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Game_theory
[164]: https://en.wikipedia.org/wiki/Glossary_of_game_theory
[165]: https://en.wikipedia.org/wiki/List_of_game_theorists
[166]: https://en.wikipedia.org/wiki/List_of_games_in_game_theory
[167]: https://en.wikipedia.org/wiki/Game_theory#Basic_concepts
[168]: https://en.wikipedia.org/wiki/Asynchrony_(game_theory)
[169]: https://en.wikipedia.org/wiki/Bayesian_regret
[170]: https://en.wikipedia.org/wiki/Best_response
[171]: https://en.wikipedia.org/wiki/Bounded_rationality
[172]: https://en.wikipedia.org/wiki/Cheap_talk
[173]: https://en.wikipedia.org/wiki/Coalition
[174]: https://en.wikipedia.org/wiki/Complete_contract
[175]: https://en.wikipedia.org/wiki/Complete_information
[176]: https://en.wikipedia.org/wiki/Complete_mixing
[177]: https://en.wikipedia.org/wiki/Conjectural_variation
[178]: https://en.wikipedia.org/wiki/Contingent_cooperator
[179]: https://en.wikipedia.org/wiki/Coopetition
[180]: https://en.wikipedia.org/wiki/Cooperative_game_theory
[181]: https://en.wikipedia.org/wiki/Dynamic_inconsistency
[182]: https://en.wikipedia.org/wiki/Escalation_of_commitment
[183]: https://en.wikipedia.org/wiki/Farsightedness_(game_theory)
[184]: https://en.wikipedia.org/wiki/Game_semantics
[185]: https://en.wikipedia.org/wiki/Hierarchy_of_beliefs
[186]: https://en.wikipedia.org/wiki/Information_set_(game_theory)
[187]: https://en.wikipedia.org/wiki/Move_by_nature
[188]: https://en.wikipedia.org/wiki/Mutual_knowledge
[189]: https://en.wikipedia.org/wiki/Non-cooperative_game_theory
[190]: https://en.wikipedia.org/wiki/Non-credible_threat
[191]: https://en.wikipedia.org/wiki/Outcome_(game_theory)
[192]: https://en.wikipedia.org/wiki/Perfect_recall_(game_theory)
[193]: https://en.wikipedia.org/wiki/Ply_(game_theory)
[194]: https://en.wikipedia.org/wiki/Preference_(economics)
[195]: https://en.wikipedia.org/wiki/Rationality
[196]: https://en.wikipedia.org/wiki/Simultaneous_action_selection
[197]: https://en.wikipedia.org/wiki/Spite_(game_theory)
[198]: https://en.wikipedia.org/wiki/Strategic_complements
[199]: https://en.wikipedia.org/wiki/Strategic_dominance
[200]: https://en.wikipedia.org/wiki/Strategic_form
[201]: https://en.wikipedia.org/wiki/Strategic_interaction
[202]: https://en.wikipedia.org/wiki/Strategic_move
[203]: https://en.wikipedia.org/wiki/Strategy_(game_theory)
[204]: https://en.wikipedia.org/wiki/Subgame
[205]: https://en.wikipedia.org/wiki/Succinct_game
[206]: https://en.wikipedia.org/wiki/Tragedy_of_the_commons
[207]: https://en.wikipedia.org/wiki/Uncorrelated_asymmetry
[208]: https://en.wikipedia.org/wiki/Win–win_game
[209]: https://en.wikipedia.org/wiki/Zero-sum_game
[210]: https://en.wikipedia.org/wiki/Economic_equilibrium
[211]: https://en.wikipedia.org/wiki/Bayes_correlated_equilibrium
[212]: https://en.wikipedia.org/wiki/Bayesian_efficiency
[213]: https://en.wikipedia.org/wiki/Bayesian_game
[214]: https://en.wikipedia.org/wiki/Bayesian_Nash_equilibrium
[215]: https://en.wikipedia.org/wiki/Berge_equilibrium
[216]: https://en.wikipedia.org/wiki/Bertrand–Edgeworth_model
[217]: https://en.wikipedia.org/wiki/Coalition-proof_Nash_equilibrium
[218]: https://en.wikipedia.org/wiki/Core_(game_theory)
[219]: https://en.wikipedia.org/wiki/Correlated_equilibrium
[220]: https://en.wikipedia.org/wiki/Cursed_equilibrium
[221]: https://en.wikipedia.org/wiki/Edgeworth_price_cycle
[222]: https://en.wikipedia.org/wiki/Epsilon-equilibrium
[223]: https://en.wikipedia.org/wiki/Gibbs_measure
[224]: https://en.wikipedia.org/wiki/Incomplete_contracts
[225]: https://en.wikipedia.org/wiki/Inequity_aversion
[226]: https://en.wikipedia.org/wiki/Individual_rationality
[227]: https://en.wikipedia.org/wiki/Iterated_elimination_of_dominated_strategies
[228]: https://en.wikipedia.org/wiki/Markov_perfect_equilibrium
[229]: https://en.wikipedia.org/wiki/Mertens-stable_equilibrium
[230]: https://en.wikipedia.org/wiki/Nash_equilibrium
[231]: https://en.wikipedia.org/wiki/Open-loop_model
[232]: https://en.wikipedia.org/wiki/Pareto_efficiency
[233]: https://en.wikipedia.org/wiki/Payoff_dominance
[234]: https://en.wikipedia.org/wiki/Perfect_Bayesian_equilibrium
[235]: https://en.wikipedia.org/wiki/Price_of_anarchy
[236]: https://en.wikipedia.org/wiki/Program_equilibrium
[237]: https://en.wikipedia.org/wiki/Proper_equilibrium
[238]: https://en.wikipedia.org/wiki/Quantal_response_equilibrium
[239]: https://en.wikipedia.org/wiki/Quasi-perfect_equilibrium
[240]: https://en.wikipedia.org/wiki/Rational_agent
[241]: https://en.wikipedia.org/wiki/Rationalizable_strategy
[242]: https://en.wikipedia.org/wiki/Satisfaction_equilibrium
[243]: https://en.wikipedia.org/wiki/Self-confirming_equilibrium
[244]: https://en.wikipedia.org/wiki/Sequential_equilibrium
[245]: https://en.wikipedia.org/wiki/Shapley_value
[246]: https://en.wikipedia.org/wiki/Strong_Nash_equilibrium
[247]: https://en.wikipedia.org/wiki/Subgame_perfect_equilibrium
[248]: https://en.wikipedia.org/wiki/Trembling_hand_perfect_equilibrium
[249]: https://en.wikipedia.org/wiki/Appeasement
[250]: https://en.wikipedia.org/wiki/Bid_shading
[251]: https://en.wikipedia.org/wiki/Collusion
[252]: https://en.wikipedia.org/wiki/Commitment_device
[253]: https://en.wikipedia.org/wiki/De-escalation
[254]: https://en.wikipedia.org/wiki/Deterrence_theory
[255]: https://en.wikipedia.org/wiki/Conflict_escalation
[256]: https://en.wikipedia.org/wiki/Fictitious_play
[257]: https://en.wikipedia.org/wiki/Focal_point_(game_theory)
[258]: https://en.wikipedia.org/wiki/Grim_trigger
[259]: https://en.wikipedia.org/wiki/Hobbesian_trap
[260]: https://en.wikipedia.org/wiki/Markov_strategy
[261]: https://en.wikipedia.org/wiki/Max-dominated_strategy
[262]: https://en.wikipedia.org/wiki/Strategy_(game_theory)#Mixed_strategy
[263]: https://en.wikipedia.org/wiki/Tit_for_tat
[264]: https://en.wikipedia.org/wiki/Win–stay,_lose–switch
[265]: https://en.wikipedia.org/wiki/All-pay_auction
[266]: https://en.wikipedia.org/wiki/Battle_of_the_sexes_(game_theory)
[267]: https://en.wikipedia.org/wiki/Bargaining_problem
[268]: https://en.wikipedia.org/wiki/Bertrand_competition
[269]: https://en.wikipedia.org/wiki/Blotto_game
[270]: https://en.wikipedia.org/wiki/Centipede_game
[271]: https://en.wikipedia.org/wiki/Coordination_game
[272]: https://en.wikipedia.org/wiki/Cournot_competition
[273]: https://en.wikipedia.org/wiki/Deadlock_(game_theory)
[274]: https://en.wikipedia.org/wiki/Dictator_game
[275]: https://en.wikipedia.org/wiki/Dictator_game#Trust_game
[276]: https://en.wikipedia.org/wiki/Unscrupulous_diner's_dilemma
[277]: https://en.wikipedia.org/wiki/Dollar_auction
[278]: https://en.wikipedia.org/wiki/El_Farol_Bar_problem
[279]: https://en.wikipedia.org/wiki/Electronic_mail_game
[280]: https://en.wikipedia.org/wiki/Gift-exchange_game
[281]: https://en.wikipedia.org/wiki/Guess_2/3_of_the_average
[282]: https://en.wikipedia.org/wiki/Keynesian_beauty_contest
[283]: https://en.wikipedia.org/wiki/Kuhn_poker
[284]: https://en.wikipedia.org/wiki/Lewis_signaling_game
[285]: https://en.wikipedia.org/wiki/Matching_pennies
[286]: https://en.wikipedia.org/wiki/Obligationes
[287]: https://en.wikipedia.org/wiki/Optional_prisoner's_dilemma
[288]: https://en.wikipedia.org/wiki/Pirate_game
[289]: https://en.wikipedia.org/wiki/Prisoner's_dilemma
[290]: https://en.wikipedia.org/wiki/Public_goods_game
[291]: https://en.wikipedia.org/wiki/Rendezvous_problem
[292]: https://en.wikipedia.org/wiki/Rock_paper_scissors
[293]: https://en.wikipedia.org/wiki/Stackelberg_competition
[294]: https://en.wikipedia.org/wiki/Stag_hunt
[295]: https://en.wikipedia.org/wiki/Traveler's_dilemma
[296]: https://en.wikipedia.org/wiki/Ultimatum_game
[297]: https://en.wikipedia.org/wiki/Volunteer's_dilemma
[298]: https://en.wikipedia.org/wiki/War_of_attrition_(game)
[299]: https://en.wikipedia.org/wiki/Game_theory#Theorems
[300]: https://en.wikipedia.org/wiki/Arrow's_impossibility_theorem
[301]: https://en.wikipedia.org/wiki/Aumann's_agreement_theorem
[302]: https://en.wikipedia.org/wiki/Brouwer_fixed-point_theorem
[303]: https://en.wikipedia.org/wiki/Competitive_altruism
[304]: https://en.wikipedia.org/wiki/Folk_theorem_(game_theory)
[305]: https://en.wikipedia.org/wiki/Gibbard–Satterthwaite_theorem
[306]: https://en.wikipedia.org/wiki/Gibbs_lemma
[307]: https://en.wikipedia.org/wiki/Glicksberg's_theorem
[308]: https://en.wikipedia.org/wiki/Kakutani_fixed-point_theorem
[309]: https://en.wikipedia.org/wiki/Kuhn's_theorem
[310]: https://en.wikipedia.org/wiki/One-shot_deviation_principle
[311]: https://en.wikipedia.org/wiki/Prim–Read_theory
[312]: https://en.wikipedia.org/wiki/Rational_ignorance
[313]: https://en.wikipedia.org/wiki/Rational_irrationality
[314]: https://en.wikipedia.org/wiki/Sperner's_lemma
[315]: https://en.wikipedia.org/wiki/Zermelo's_theorem_(game_theory)
[316]: https://en.wikipedia.org/wiki/Algorithmic_game_theory
[317]: https://en.wikipedia.org/wiki/Behavioral_game_theory
[318]: https://en.wikipedia.org/wiki/Behavioral_strategy
[319]: https://en.wikipedia.org/wiki/Compositional_game_theory
[320]: https://en.wikipedia.org/wiki/Confrontation_analysis
[321]: https://en.wikipedia.org/wiki/Contract_theory
[322]: https://en.wikipedia.org/wiki/Drama_theory
[323]: https://en.wikipedia.org/wiki/Graphical_game_theory
[324]: https://en.wikipedia.org/wiki/Heresthetic
[325]: https://en.wikipedia.org/wiki/Mean-field_game_theory
[326]: https://en.wikipedia.org/wiki/Negotiation_theory
[327]: https://en.wikipedia.org/wiki/Quantum_game_theory
[328]: https://en.wikipedia.org/wiki/Social_software_(research_field)
[329]: https://en.wikipedia.org/wiki/Albert_W._Tucker
[330]: https://en.wikipedia.org/wiki/Alvin_E._Roth
[331]: https://en.wikipedia.org/wiki/Amos_Tversky
[332]: https://en.wikipedia.org/wiki/Antoine_Augustin_Cournot
[333]: https://en.wikipedia.org/wiki/Ariel_Rubinstein
[334]: https://en.wikipedia.org/wiki/David_Gale
[335]: https://en.wikipedia.org/wiki/David_K._Levine
[336]: https://en.wikipedia.org/wiki/David_M._Kreps
[337]: https://en.wikipedia.org/wiki/Donald_B._Gillies
[338]: https://en.wikipedia.org/wiki/Drew_Fudenberg
[339]: https://en.wikipedia.org/wiki/Eric_Maskin
[340]: https://en.wikipedia.org/wiki/Harold_W._Kuhn
[341]: https://en.wikipedia.org/wiki/Herbert_A._Simon
[342]: https://en.wikipedia.org/wiki/Herbert_Scarf
[343]: https://en.wikipedia.org/wiki/Hervé_Moulin
[344]: https://en.wikipedia.org/wiki/Jean_Tirole
[345]: https://en.wikipedia.org/wiki/Jean-François_Mertens
[346]: https://en.wikipedia.org/wiki/Jennifer_Tour_Chayes
[347]: https://en.wikipedia.org/wiki/Ken_Binmore
[348]: https://en.wikipedia.org/wiki/Kenneth_Arrow
[349]: https://en.wikipedia.org/wiki/Leonid_Hurwicz
[350]: https://en.wikipedia.org/wiki/Lloyd_Shapley
[351]: https://en.wikipedia.org/wiki/Martin_Shubik
[352]: https://en.wikipedia.org/wiki/Melvin_Dresher
[353]: https://en.wikipedia.org/wiki/Merrill_M._Flood
[354]: https://en.wikipedia.org/wiki/Olga_Bondareva
[355]: https://en.wikipedia.org/wiki/Oskar_Morgenstern
[356]: https://en.wikipedia.org/wiki/Paul_Milgrom
[357]: https://en.wikipedia.org/wiki/Peyton_Young
[358]: https://en.wikipedia.org/wiki/Reinhard_Selten
[359]: https://en.wikipedia.org/wiki/Robert_Aumann
[360]: https://en.wikipedia.org/wiki/Robert_Axelrod_(political_scientist)
[361]: https://en.wikipedia.org/wiki/Robert_B._Wilson
[362]: https://en.wikipedia.org/wiki/Roger_Myerson
[363]: https://en.wikipedia.org/wiki/Samuel_Bowles_(economist)
[364]: https://en.wikipedia.org/wiki/Suzanne_Scotchmer
[365]: https://en.wikipedia.org/wiki/Thomas_Schelling
[366]: https://en.wikipedia.org/wiki/William_Vickrey
[367]: https://en.wikipedia.org/wiki/Combinatorial_game_theory
[368]: https://en.wikipedia.org/wiki/Combinatorial_explosion
[369]: https://en.wikipedia.org/wiki/Determinacy
[370]: https://en.wikipedia.org/wiki/First-player_and_second-player_win
[371]: https://en.wikipedia.org/wiki/Misère
[372]: https://en.wikipedia.org/wiki/Chomp
[373]: https://en.wikipedia.org/wiki/Clobber
[374]: https://en.wikipedia.org/wiki/Cram_(game)
[375]: https://en.wikipedia.org/wiki/Notakto
[376]: https://en.wikipedia.org/wiki/Subtract_a_square
[377]: https://en.wikipedia.org/wiki/Mex_(mathematics)
[378]: https://en.wikipedia.org/wiki/Winning_Ways_for_Your_Mathematical_Plays
[379]: https://en.wikipedia.org/wiki/Expectiminimax
[380]: https://en.wikipedia.org/wiki/Minimax
[381]: https://en.wikipedia.org/wiki/Monte_Carlo_tree_search
[382]: https://en.wikipedia.org/wiki/Negamax
[383]: https://en.wikipedia.org/wiki/Paranoid_algorithm
[384]: https://en.wikipedia.org/wiki/Principal_variation_search
[385]: https://en.wikipedia.org/wiki/John_Conway
[386]: https://en.wikipedia.org/wiki/John_von_Neumann
[387]: https://en.wikipedia.org/wiki/Evolutionary_game_theory
[388]: https://en.wikipedia.org/wiki/Bishop–Cannings_theorem
[389]: https://en.wikipedia.org/wiki/Evolution_and_the_Theory_of_Games
[390]: https://en.wikipedia.org/wiki/Evolutionarily_stable_set
[391]: https://en.wikipedia.org/wiki/Evolutionarily_stable_state
[392]: https://en.wikipedia.org/wiki/Evolutionarily_stable_strategy
[393]: https://en.wikipedia.org/wiki/Replicator_equation
[394]: https://en.wikipedia.org/wiki/Risk_dominance
[395]: https://en.wikipedia.org/wiki/Stochastically_stable_equilibrium
[396]: https://en.wikipedia.org/wiki/Weak_evolutionarily_stable_strategy
[397]: https://en.wikipedia.org/wiki/Chicken_(game)
[398]: https://en.wikipedia.org/wiki/Cultural_group_selection
[399]: https://en.wikipedia.org/wiki/Fisher's_principle
[400]: https://en.wikipedia.org/wiki/Mobbing_(animal_behavior)
[401]: https://en.wikipedia.org/wiki/Terminal_investment_hypothesis
[402]: https://en.wikipedia.org/wiki/John_Maynard_Smith
[403]: https://en.wikipedia.org/wiki/George_R._Price
[404]: https://en.wikipedia.org/wiki/William_Donald_Hamilton
[405]: https://en.wikipedia.org/wiki/Mechanism_design
[406]: https://en.wikipedia.org/wiki/Algorithmic_mechanism_design
[407]: https://en.wikipedia.org/wiki/Bayesian-optimal_mechanism
[408]: https://en.wikipedia.org/wiki/Incentive_compatibility
[409]: https://en.wikipedia.org/wiki/Market_design
[410]: https://en.wikipedia.org/wiki/Myerson_ironing
[411]: https://en.wikipedia.org/wiki/Monotonicity_(mechanism_design)
[412]: https://en.wikipedia.org/wiki/Participation_constraint_(mechanism_design)
[413]: https://en.wikipedia.org/wiki/Revelation_principle
[414]: https://en.wikipedia.org/wiki/Strategyproofness
[415]: https://en.wikipedia.org/wiki/Vickrey–Clarke–Groves_mechanism
[416]: https://en.wikipedia.org/wiki/Virtual_valuation
[417]: https://en.wikipedia.org/wiki/Myerson–Satterthwaite_theorem
[418]: https://en.wikipedia.org/wiki/Revenue_equivalence
[419]: https://en.wikipedia.org/wiki/Border's_theorem
[420]: https://en.wikipedia.org/wiki/Digital_goods_auction
[421]: https://en.wikipedia.org/wiki/Knapsack_auction
[422]: https://en.wikipedia.org/wiki/Truthful_cake-cutting
[423]: https://en.wikipedia.org/wiki/Bertrand_paradox_(economics)
[424]: https://en.wikipedia.org/wiki/Chainstore_paradox
[425]: https://en.wikipedia.org/wiki/Computational_complexity_of_games
[426]: https://en.wikipedia.org/wiki/Helly_metric
[427]: https://en.wikipedia.org/wiki/PPAD_(complexity)
[428]: https://en.wikipedia.org/wiki/File:Square_root_of_x.svg
[429]: https://en.wikipedia.org/wiki/Portal:Mathematics
[430]: https://en.wikipedia.org/wiki/File:Commons-logo.svg
[431]: https://commons.wikimedia.org/wiki/Category:Game%20theory
[432]: https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Game_theory
[433]: https://en.wikipedia.org/wiki/Category:Game_theory
[434]: https://en.wikipedia.org/wiki/Help:Authority_control
[435]: https://www.wikidata.org/wiki/Q1320931#identifiers
[436]: https://d-nb.info/gnd/4164753-1
[437]: https://en.wikipedia.org/w/index.php?title=Combinatorial_game_theory&amp;oldid=1358173260
[438]: /wiki/Help:Category
[439]: /wiki/Category:Combinatorial_game_theory
[440]: /wiki/Category:Articles_with_short_description
[441]: /wiki/Category:Short_description_matches_Wikidata
[442]: /wiki/Category:CS1_errors:_deprecated_parameters
[443]: /wiki/Category:Commons_category_link_is_on_Wikidata
