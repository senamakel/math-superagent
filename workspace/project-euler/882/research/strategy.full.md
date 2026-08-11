<!-- source: https://en.wikipedia.org/wiki/Strategy_(game_theory) | converted from HTML -->

Strategy (game theory) - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Complete plan on how a game player will behave in every possible game situation

For other uses of "Strategy", see [Strategy (disambiguation)][1].

In [game theory][2], a **move**, **action**, or **play**is any one of the options which a player can choose in a setting where the optimal outcome depends *not only*on their own actions *but also*on the actions of others. [1] The discipline mainly concerns the action of a player in a game affecting the behavior or actions of other players. Some examples of "games" include chess, bridge, poker, monopoly, diplomacy or battleship. [2]

The term **strategy**is typically used to mean a complete [algorithm][3] for playing a game, telling a player what to do for every possible situation. A player's strategy determines the action the player will take at any stage of the game. However, the idea of a strategy is often confused or [conflated][4] with that of a move or action, because of the correspondence between moves and [pure strategies][5] in [most games][6]: for any move *X*, "always play move *X*" is an example of a valid strategy, and as a result every move can also be considered to be a strategy. Other authors treat strategies as being a different type of thing from actions, and therefore distinct.

It is helpful to think about a "strategy" as a list of directions, and a "move" as a single turn on the list of directions itself. This strategy is based on the payoff or outcome of each action. The goal of each agent is to consider their payoff based on a competitors action. For example, competitor A can assume competitor B enters the market. From there, Competitor A compares the payoffs they receive by entering and not entering. The next step is to assume Competitor B does not enter and then consider which payoff is better based on if Competitor A chooses to enter or not enter. This technique can identify dominant strategies where a player can identify an action that they can take no matter what the competitor does to try to maximize the payoff.

A **strategy profile**(sometimes called a **strategy combination**) is a set of strategies for all players which fully specifies all actions in a game. A strategy profile must include one and only one strategy for every player.

## Strategy set

[[edit][7]]

A player's **strategy set**defines what strategies are available for them to play.

A player has a **finite**strategy set if they have a number of discrete strategies available to them. For instance, a game of [rock paper scissors][8] comprises a single move by each player — and each player's move is made without knowledge of the other's, not as a response — so each player has the finite strategy set {rock paper scissors}.

A strategy set is infinite otherwise. For instance the [cake cutting game][9] has a bounded continuum of strategies in the strategy set {Cut anywhere between zero percent and 100 percent of the cake}.

In a [dynamic game][10], games that are played over a series of time, the strategy set consists of the possible rules a player could give to a [robot][11] or [agent][12] on how to play the game. For instance, in the [ultimatum game][13], the strategy set for the second player would consist of every possible rule for which offers to accept and which to reject.

In a [Bayesian game][14], or games in which players have incomplete information about one another, the strategy set is similar to that in a dynamic game. It consists of rules for what action to take for any possible private information.

### Choosing a strategy set

[[edit][15]]

In applied game theory, the definition of the strategy sets is an important part of the art of making a game simultaneously solvable and meaningful. The game theorist can use knowledge of the overall problem, that is the friction between two or more players, to limit the strategy spaces, and ease the solution.

For instance, strictly speaking in the Ultimatum game a player can have strategies such as: *Reject offers of ($1, $3, $5, ..., $19), accept offers of ($0, $2, $4, ..., $20)*. Including all such strategies makes for a very large strategy space and a somewhat difficult problem. A game theorist might instead believe they can limit the strategy set to: {Reject any offer ≤ *x*, accept any offer > *x*; for *x*in ($0, $1, $2, ..., $20)}.

## Pure and mixed strategies

[[edit][16]]

A **pure strategy**provides a complete and deterministic plan for how a player will act in every possible situation in a game. It specifies exactly what action the player will take at each decision point, given any information they may have. A player's **strategy set**consists of all the pure strategies available to them.

A **mixed strategy**is a probability distribution over the set of pure strategies. Rather than committing to a single course of action, the player randomizes among pure strategies according to specified probabilities. Mixed strategies are particularly useful in games where no pure strategy constitutes a best response, allowing players to avoid being predictable. Since the outcomes depend on probabilities, the resulting payoffs are referred to as **expected payoffs**.

A pure strategy can be viewed as a special case of a mixed strategy—one in which a single pure strategy is chosen with probability 1, and all others with probability 0.

A **totally mixed strategy**is a mixed strategy in which *every*pure strategy in the player's strategy set is assigned a strictly positive probability—that is, no pure strategy is excluded or played with zero probability. This means the player randomizes across *all*of their options, never fully ruling any one out. Totally mixed strategies are important in some advanced game theory concepts like [trembling hand perfect equilibrium][17], where the idea is to model players as occasionally making small mistakes. In that context, assigning positive probability to every strategy—even suboptimal ones—helps capture how players might still end up choosing them due to small "trembles" in decision-making.

## Mixed strategy

[[edit][18]]

### Illustration

[[edit][19]]

In a soccer penalty kick, the kicker must choose whether to kick to the right or left side of the goal, and simultaneously the goalie must decide which way to block it. Also, the kicker has a direction they are best at shooting, which is left if they are right-footed. The matrix for the soccer game illustrates this situation, a simplified form of the game studied by Chiappori, Levitt, and Groseclose (2002). [3] It assumes that if the goalie guesses correctly, the kick is blocked, which is set to the base payoff of 0 for both players. If the goalie guesses wrong, the kick is more likely to go in if it is to the left (payoffs of +2 for the kicker and -2 for the goalie) than if it is to the right (the lower payoff of +1 to kicker and -1 to goalie).

 | Goalie |

Lean Left | Lean Right |

Kicker | Kick Left | 0, 0 | +2, -2 |

Kick Right | +1, -1 | 0, 0 |

 |

 |

Payoff for the Soccer Game (Kicker, Goalie) |

This game has no pure-strategy equilibrium, because one player or the other would deviate from any profile of strategies—for example, (Left, Left) is not an equilibrium because the Kicker would deviate to Right and increase his payoff from 0 to 1.

The kicker's mixed-strategy equilibrium is found from the fact that they will deviate from randomizing unless their payoffs from Left Kick and Right Kick are exactly equal. If the goalie leans left with probability g, the kicker's expected payoff from Kick Left is g(0) + (1-g)(2), and from Kick Right is g(1) + (1-g)(0). Equating these yields g= 2/3. Similarly, the goalie is willing to randomize only if the kicker chooses mixed strategy probability k such that Lean Left's payoff of k(0) + (1-k)(-1) equals Lean Right's payoff of k(-2) + (1-k)(0), so k = 1/3. Thus, the mixed-strategy equilibrium is (Prob(Kick Left) = 1/3, Prob(Lean Left) = 2/3).

In equilibrium, the kicker kicks to their best side only 1/3 of the time. That is because the goalie is guarding that side more. Also, in equilibrium, the kicker is indifferent which way they kick, but for it to be an equilibrium they must choose exactly 1/3 probability.

Chiappori, Levitt, and Groseclose try to measure how important it is for the kicker to kick to their favored side, add center kicks, etc., and look at how professional players actually behave. They find that they do randomize, and that kickers kick to their favored side 45% of the time and goalies lean to that side 57% of the time. Their article is well-known as an example of how people in real life use mixed strategies.

### Significance

[[edit][20]]

In his famous paper, [John Forbes Nash][21] proved that there is an [equilibrium][22] for every finite game. One can divide Nash equilibria into two types. *Pure strategy Nash equilibria*are Nash equilibria where all players are playing pure strategies. *Mixed strategy Nash equilibria*are equilibria where at least one player is playing a mixed strategy. While Nash proved that every finite game has a Nash equilibrium, not all have pure strategy Nash equilibria. For an example of a game that does not have a Nash equilibrium in pure strategies, see [Matching pennies][23]. However, many games do have pure strategy Nash equilibria (e.g., the [Coordination game][24], the [Prisoner's dilemma][25], the [Stag hunt][26]). Further, games can have both pure strategy and mixed strategy equilibria. An easy example is the pure coordination game, where in addition to the pure strategies (A,A) and (B,B) a mixed equilibrium exists in which both players play either strategy with probability 1/2.

### Interpretations of mixed strategies

[[edit][27]]

During the 1980s, the concept of mixed strategies came under heavy fire for being "intuitively problematic", since they are weak Nash equilibria, and a player is indifferent about whether to follow their equilibrium strategy probability or deviate to some other probability. [4] [5] Game theorist [Ariel Rubinstein][28] describes alternative ways of understanding the concept. The first, due to Harsanyi (1973), [6] is called *[purification][29]*, and supposes that the mixed strategies interpretation merely reflects our lack of knowledge of the players' information and decision-making process. Apparently random choices are then seen as consequences of non-specified, payoff-irrelevant exogenous factors. [5] A second interpretation imagines the game players standing for a large population of agents. Each of the agents chooses a pure strategy, and the payoff depends on the fraction of agents choosing each strategy. The mixed strategy hence represents the distribution of pure strategies chosen by each population. However, this does not provide any justification for the case when players are individual agents.

Later, Aumann and Brandenburger (1995), [7] re-interpreted Nash equilibrium as an equilibrium in *beliefs*, rather than actions. For instance, in [rock paper scissors][8] an equilibrium in beliefs would have each player *believing*the other was equally likely to play each strategy. This interpretation weakens the descriptive power of Nash equilibrium, however, since it is possible in such an equilibrium for each player to *actually*play a pure strategy of Rock in each play of the game, even though over time the probabilities are those of the mixed strategy.

## Behavior strategy

[[edit][30]]

While a mixed strategy assigns a probability distribution over pure strategies, a **behavior strategy**(or **behavioral strategy**) assigns at each [information set][31] a probability distribution over the set of possible actions. While the two concepts are very closely related in the context of normal form games, they have very different implications for extensive form games. Roughly, a mixed strategy randomly chooses a deterministic path through the [game tree][32], while a behavior strategy can be seen as a stochastic path. The relationship between mixed and behavior strategies is the subject of [Kuhn's theorem][33], a behavioral outlook on traditional game-theoretic hypotheses. The result establishes that in any finite extensive-form game with perfect recall, for any player and any mixed strategy, there exists a behavior strategy that, against all profiles of strategies (of other players), induces the same distribution over terminal nodes as the mixed strategy does. The converse is also true.

A famous example of why perfect recall is required for the equivalence is given by Piccione and Rubinstein (1997) [*[full citation needed][34]*] with their *Absent-Minded Driver*game.

### Outcome equivalence

[[edit][35]]

Outcome equivalence combines the mixed and behavioral strategy of Player i in relation to the pure strategy of Player i’s opponent. Outcome equivalence is defined as the situation in which, for any mixed and behavioral strategy that Player i takes, in response to any pure strategy that Player I’s opponent plays, the outcome distribution of the mixed and behavioral strategy must be equal. This equivalence can be described by the following formula: (Q^(U(i), S(-i)))(z) = (Q^(β(i), S(-i)))(z), where U(i) describes Player i's mixed strategy, β(i) describes Player i's behavioral strategy, and S(-i) is the opponent's strategy. [8]

### Strategy with perfect recall

[[edit][36]]

Main article: [Perfect recall (game theory)][37]

Perfect recall is defined as the ability of every player who is playing the game to remember and recall all past actions within the game. Perfect recall is required for equivalence as, in finite games with imperfect recall, there will be existing mixed strategies of Player I in which there is no equivalent behavior strategy. This is fully described in the *Absent-Minded Driver*game formulated by Piccione and Rubinstein. In short, this game is based on the decision-making of a driver with imperfect recall, who needs to take the second exit off the highway to reach home but does not remember which intersection they are at when they reach it. Figure [2] describes this game.

Without perfect information (i.e., imperfect information), players make a choice at each decision node without knowledge of the decisions that have preceded it. Therefore, a player’s mixed strategy can produce outcomes that their behavioral strategy cannot, and vice versa. This is demonstrated in the *Absent-minded Driver*game. With perfect recall and information, the driver has a single pure strategy, which is [continue, exit], as the driver is aware of what intersection (or decision node) they are at when they arrive to it. On the other hand, looking at the planning-optimal stage only, the maximum payoff is achieved by continuing at both intersections, maximized at p=2/3 (reference). This simple one player game demonstrates the importance of perfect recall for outcome equivalence, and its impact on normal and extended form games. [9]

## See also

[[edit][38]]

- [Nash equilibrium][22]
- [Haven (graph theory)][39]
- [Evolutionarily stable strategy][40]

## References

[[edit][41]]

1. ↑ [Ben Polak][42]*Game Theory: Lecture 1 Transcript*ECON 159, 5 September 2007, [Open Yale Courses][43].
2. ↑ [Aumann, R.][44] (22 March 2017). *Game Theory. In: Palgrave Macmillan*. London: Palgrave Macmillan. [ISBN][45] [978-1-349-95121-5][46].
3. ↑ Chiappori, P. -A.; Levitt, S.; Groseclose, T. (2002). ["Testing Mixed-Strategy Equilibria when Players Are Heterogeneous: The Case of Penalty Kicks in Soccer"][47] (PDF). *American Economic Review*. **92**(4): 1138. [CiteSeerX][48] [10.1.1.178.1646][49]. [doi][50]: [10.1257/00028280260344678][51].`{{ [cite journal][52] }}`: Cite uses deprecated parameter `| citeseerx=`( [help][53])
4. ↑ [Aumann, R.][44] (1985). ["What is Game Theory Trying to accomplish?"][54] (PDF). In Arrow, K.; Honkapohja, S. (eds.). *Frontiers of Economics*. Oxford: Basil Blackwell. pp. 909– 924.
5. 1 2 [Rubinstein, A.][28] (1991). "Comments on the interpretation of Game Theory". *[Econometrica][55]*. **59**(4): 909– 924. [doi][50]: [10.2307/2938166][56]. [JSTOR][57] [2938166][58].
6. ↑ [Harsanyi, John][59] (1973). "Games with randomly disturbed payoffs: a new rationale for mixed-strategy equilibrium points". *Int. J. Game Theory*. **2**: 1– 23. [doi][50]: [10.1007/BF01737554][60]. [S2CID][61] [154484458][62].
7. ↑ [Aumann, Robert][44]; [Brandenburger, Adam][63] (1995). "Epistemic Conditions for Nash Equilibrium". *Econometrica*. **63**(5): 1161– 1180. [CiteSeerX][48] [10.1.1.122.5816][64]. [doi][50]: [10.2307/2171725][65]. [JSTOR][57] [2171725][66].`{{ [cite journal][52] }}`: Cite uses deprecated parameter `| citeseerx=`( [help][53])
8. ↑ Shimoji, Makoto (2012-05-01). ["Outcome-equivalence of self-confirming equilibrium and Nash equilibrium"][67]. *Games and Economic Behavior*. **75**(1): 441– 447. [doi][50]: [10.1016/j.geb.2011.09.010][68]. [ISSN][69] [0899-8256][70].
9. ↑ Kak, Subhash (2017). "The Absent-Minded Driver Problem Redux". [arXiv][71]: [1702.05778][72] [[cs.AI][73]].

- [v][74]
- [t][75]
- [e][76]

[Game theory][2]

 |

- [Glossary][77]
- [Game theorists][78]
- [Games][79]

 |

Traditional [game theory][2]

 |

[Definitions][80] |

- [Asynchrony][81]
- [Bayesian regret][82]
- [Best response][83]
- [Bounded rationality][84]
- [Cheap talk][85]
- [Coalition][86]
- [Complete contract][87]
- [Complete information][88]
- [Complete mixing][89]
- [Conjectural variation][90]
- [Contingent cooperator][91]
- [Coopetition][92]
- [Cooperative game theory][93]
- [Dynamic inconsistency][94]
- [Escalation of commitment][95]
- [Farsightedness][96]
- [Game semantics][97]
- [Hierarchy of beliefs][98]
- [Imperfect information][99]
- [Incomplete information][100]
- [Information set][31]
- [Move by nature][101]
- [Mutual knowledge][102]
- [Non-cooperative game theory][103]
- [Non-credible threat][104]
- [Outcome][105]
- [Perfect information][106]
- [Perfect recall][37]
- [Ply][107]
- [Preference][108]
- [Rationality][109]
- [Sequential game][110]
- [Simultaneous action selection][111]
- [Spite][112]
- [Strategic complements][113]
- [Strategic dominance][114]
- [Strategic form][115]
- [Strategic interaction][116]
- [Strategic move][117]
- [Strategy][118]
- [Subgame][119]
- [Succinct game][120]
- [Topological game][121]
- [Tragedy of the commons][122]
- [Uncorrelated asymmetry][123]
- [Win–win game][124]
- [Zero-sum game][125]

 |

[Equilibrium concepts][126] |

- [Backward induction][127]
- [Bayes correlated equilibrium][128]
- [Bayesian efficiency][129]
- [Bayesian game][14]
- [Bayesian Nash equilibrium][130]
- [Berge equilibrium][131]
- [Bertrand–Edgeworth model][132]
- [Coalition-proof Nash equilibrium][133]
- [Core][134]
- [Correlated equilibrium][135]
- [Cursed equilibrium][136]
- [Edgeworth price cycle][137]
- [Epsilon-equilibrium][138]
- [Gibbs equilibrium][139]
- [Incomplete contracts][140]
- [Inequity aversion][141]
- [Individual rationality][142]
- [Iterated elimination of dominated strategies][143]
- [Markov perfect equilibrium][144]
- [Mertens-stable equilibrium][145]
- [Nash equilibrium][22]
- [Open-loop model][146]
- [Pareto efficiency][147]
- [Payoff dominance][148]
- [Perfect Bayesian equilibrium][149]
- [Price of anarchy][150]
- [Program equilibrium][151]
- [Proper equilibrium][152]
- [Quantal response equilibrium][153]
- [Quasi-perfect equilibrium][154]
- [Rational agent][155]
- [Rationalizable strategy][156]
- [Satisfaction equilibrium][157]
- [Self-confirming equilibrium][158]
- [Sequential equilibrium][159]
- [Shapley value][160]
- [Strong Nash equilibrium][161]
- [Subgame perfect equilibrium][162]
- [Trembling hand equilibrium][17]

 |

[Strategies][118] |

- [Appeasement][163]
- [Bid shading][164]
- [Cheap talk][85]
- [Collusion][165]
- [Commitment device][166]
- [De-escalation][167]
- [Deterrence][168]
- [Escalation][169]
- [Fictitious play][170]
- [Focal point][171]
- [Grim trigger][172]
- [Hobbesian trap][173]
- [Markov strategy][174]
- [Max-dominated strategy][175]
- Mixed strategy
- [Pure strategy][118]
- [Tit for tat][176]
- [Win–stay, lose–switch][177]

 |

[Games][79] |

- [All-pay auction][178]
- [Battle of the sexes][179]
- [Nash bargaining game][180]
- [Bertrand competition][181]
- [Blotto game][182]
- [Centipede game][183]
- [Coordination game][24]
- [Cournot competition][184]
- [Deadlock][185]
- [Dictator game][186]
- [Trust game][187]
- [Diner's dilemma][188]
- [Dollar auction][189]
- [El Farol Bar problem][190]
- [Electronic mail game][191]
- [Gift-exchange game][192]
- [Guess 2/3 of the average][193]
- [Keynesian beauty contest][194]
- [Kuhn poker][195]
- [Lewis signaling game][196]
- [Matching pennies][23]
- [Obligationes][197]
- [Optional prisoner's dilemma][198]
- [Pirate game][199]
- [Prisoner's dilemma][25]
- [Public goods game][200]
- [Rendezvous problem][201]
- [Rock paper scissors][8]
- [Stackelberg competition][202]
- [Stag hunt][26]
- [Traveler's dilemma][203]
- [Ultimatum game][13]
- [Volunteer's dilemma][204]
- [War of attrition][205]

 |

[Theorems][206] |

- [Arrow's impossibility theorem][207]
- [Aumann's agreement theorem][208]
- [Brouwer fixed-point theorem][209]
- [Competitive altruism][210]
- [Folk theorem][211]
- [Gibbard–Satterthwaite theorem][212]
- [Gibbs lemma][213]
- [Glicksberg's theorem][214]
- [Kakutani fixed-point theorem][215]
- [Kuhn's theorem][33]
- [One-shot deviation principle][216]
- [Prim–Read theory][217]
- [Rational ignorance][218]
- [Rational irrationality][219]
- [Sperner's lemma][220]
- [Zermelo's theorem][221]

 |

Subfields |

- [Algorithmic game theory][222]
- [Behavioral game theory][223]
- [Behavioral strategy][224]
- [Compositional game theory][225]
- [Confrontation analysis][226]
- [Contract theory][227]
- [Drama theory][228]
- [Graphical game theory][229]
- [Heresthetic][230]
- [Mean-field game theory][231]
- [Negotiation theory][232]
- [Quantum game theory][233]
- [Social software][234]

 |

Key people |

- [Albert W. Tucker][235]
- [Alvin E. Roth][236]
- [Amos Tversky][237]
- [Antoine Augustin Cournot][238]
- [Ariel Rubinstein][28]
- [David Gale][239]
- [David K. Levine][240]
- [David M. Kreps][241]
- [Donald B. Gillies][242]
- [Drew Fudenberg][243]
- [Eric Maskin][244]
- [Harold W. Kuhn][245]
- [Herbert Simon][246]
- [Herbert Scarf][247]
- [Hervé Moulin][248]
- [Jean Tirole][249]
- [Jean-François Mertens][250]
- [Jennifer Tour Chayes][251]
- [Ken Binmore][252]
- [Kenneth Arrow][253]
- [Leonid Hurwicz][254]
- [Lloyd Shapley][255]
- [Martin Shubik][256]
- [Melvin Dresher][257]
- [Merrill M. Flood][258]
- [Olga Bondareva][259]
- [Oskar Morgenstern][260]
- [Paul Milgrom][261]
- [Peyton Young][262]
- [Reinhard Selten][263]
- [Robert Aumann][44]
- [Robert Axelrod][264]
- [Robert B. Wilson][265]
- [Roger Myerson][266]
- [Samuel Bowles][267]
- [Suzanne Scotchmer][268]
- [Thomas Schelling][269]
- [William Vickrey][270]

 |

 |

 |

[Combinatorial game theory][271]

 |

Core
concepts |

- [Combinatorial explosion][272]
- [Determinacy][273]
- [Disjunctive sum][274]
- [First-player and second-player win][275]
- [Game complexity][276]
- [Game tree][32]
- [Impartial game][277]
- [Misère][278]
- [Partisan game][279]
- [Solved game][280]
- [Sprague–Grundy theorem][281]
- [Strategy-stealing argument][282]
- [Zugzwang][283]

 |

Games |

- [Chess][284]
- [Chomp][285]
- [Clobber][286]
- [Cram][287]
- [Domineering][288]
- [Hackenbush][289]
- [Nim][290]
- [Notakto][291]
- [Subtract a square][292]
- [Sylver coinage][293]
- [Toads and Frogs][294]

 |

Mathematical
tools |

- [Mex][295]
- [Nimber][296]
- [On Numbers and Games][297]
- [Star][298]
- [Surreal number][299]
- [Winning Ways for Your Mathematical Plays][300]

 |

Search
algorithms |

- [Alpha–beta pruning][301]
- [Expectiminimax][302]
- [Minimax][303]
- [Monte Carlo tree search][304]
- [Negamax][305]
- [Paranoid algorithm][306]
- [Principal variation search][307]

 |

Key people |

- [Claude Shannon][308]
- [John Conway][309]
- [John von Neumann][310]

 |

 |

 |

[Evolutionary game theory][311]

 |

Core
concepts |

- [Bishop–Cannings theorem][312]
- [Evolution and the Theory of Games][313]
- [Evolutionarily stable set][314]
- [Evolutionarily stable state][315]
- [Evolutionarily stable strategy][40]
- [Replicator equation][316]
- [Risk dominance][317]
- [Stochastically stable equilibrium][318]
- [Weak evolutionarily stable strategy][319]

 |

Games |

- [Chicken][320]
- [Stag hunt][26]

 |

Applications |

- [Cultural group selection][321]
- [Fisher's principle][322]
- [Mobbing][323]
- [Terminal investment hypothesis][324]

 |

Key people |

- [John Maynard Smith][325]
- [George R. Price][326]
- [William Donald Hamilton][327]
- [Robert Axelrod][264]

 |

 |

 |

[Mechanism design][328]

 |

Core
concepts |

- [Algorithmic mechanism design][329]
- [Bayesian-optimal mechanism][330]
- [Incentive compatibility][331]
- [Market design][332]
- [Myerson ironing][333]
- [Monotonicity][334]
- [Participation constraint][335]
- [Revelation principle][336]
- [Strategyproofness][337]
- [Vickrey–Clarke–Groves mechanism][338]
- [Virtual valuation][339]

 |

Theorems |

- [Myerson–Satterthwaite theorem][340]
- [Revenue equivalence][341]
- [Border's theorem][342]

 |

Applications |

- [Digital goods auction][343]
- [Knapsack auction][344]
- [Truthful cake-cutting][345]

 |

 |

 |

Other topics

 |

- [Bertrand paradox][346]
- [Chainstore paradox][347]
- [Computational complexity of games][348]
- [Helly metric][349]
- [Multi-agent system][350]
- [PPAD-complete][351]

 |

 |

- **[image: icon] [352] [Mathematics portal][353]**
- **[image: Wikimedia Commons logo] [354] [Game theory][355]**
- **[WikiProject][356]**
- **[Game theory][357]**

 |

[Authority control databases][358][image: Edit this at Wikidata] [359]

 |

International |

- [GND][360]

 |

National |

- strategie her</span>"}]]}'> [Czech Republic][361]

 |

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Strategy_(game_theory)&oldid=1347054546][362] "

[Category][363]:

- [Strategy (game theory)][364]

Hidden categories:

- [Articles with short description][365]
- [Short description matches Wikidata][366]
- [CS1 errors: deprecated parameters][367]
- [All articles with incomplete citations][368]
- [Articles with incomplete citations from September 2018][369]
- [Commons category link is locally defined][370]

Search

Strategy (game theory)

16 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Strategy_(disambiguation)
[2]: https://en.wikipedia.org/wiki/Game_theory
[3]: https://en.wikipedia.org/wiki/Algorithm
[4]: https://en.wikipedia.org/wiki/Conflate
[5]: https://en.wikipedia.org/wiki/Pure_strategies
[6]: https://en.wikipedia.org/wiki/Normal-form_game
[7]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=1
[8]: https://en.wikipedia.org/wiki/Rock_paper_scissors
[9]: https://en.wikipedia.org/wiki/Fair_division
[10]: https://en.wikipedia.org/wiki/Dynamic_game
[11]: https://en.wikipedia.org/wiki/Robot
[12]: https://en.wikipedia.org/wiki/Software_agent
[13]: https://en.wikipedia.org/wiki/Ultimatum_game
[14]: https://en.wikipedia.org/wiki/Bayesian_game
[15]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=2
[16]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=3
[17]: https://en.wikipedia.org/wiki/Trembling_hand_perfect_equilibrium
[18]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=4
[19]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=5
[20]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=6
[21]: https://en.wikipedia.org/wiki/John_Forbes_Nash
[22]: https://en.wikipedia.org/wiki/Nash_equilibrium
[23]: https://en.wikipedia.org/wiki/Matching_pennies
[24]: https://en.wikipedia.org/wiki/Coordination_game
[25]: https://en.wikipedia.org/wiki/Prisoner's_dilemma
[26]: https://en.wikipedia.org/wiki/Stag_hunt
[27]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=7
[28]: https://en.wikipedia.org/wiki/Ariel_Rubinstein
[29]: https://en.wikipedia.org/wiki/Purification_theorem
[30]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=8
[31]: https://en.wikipedia.org/wiki/Information_set_(game_theory)
[32]: https://en.wikipedia.org/wiki/Game_tree
[33]: https://en.wikipedia.org/wiki/Kuhn's_theorem
[34]: https://en.wikipedia.org/wiki/Wikipedia:Citing_sources#What_information_to_include
[35]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=9
[36]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=10
[37]: https://en.wikipedia.org/wiki/Perfect_recall_(game_theory)
[38]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=11
[39]: https://en.wikipedia.org/wiki/Haven_(graph_theory)
[40]: https://en.wikipedia.org/wiki/Evolutionarily_stable_strategy
[41]: /w/index.php?title=Strategy_(game_theory)&amp;action=edit&amp;section=12
[42]: https://en.wikipedia.org/wiki/Ben_Polak
[43]: https://en.wikipedia.org/wiki/Open_Yale_Courses
[44]: https://en.wikipedia.org/wiki/Robert_Aumann
[45]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[46]: https://en.wikipedia.org/wiki/Special:BookSources/978-1-349-95121-5
[47]: http://pricetheory.uchicago.edu/levitt/Papers/ChiapporiGrosecloseLevitt2002.pdf
[48]: https://en.wikipedia.org/wiki/CiteSeerX_(identifier)
[49]: https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.178.1646
[50]: https://en.wikipedia.org/wiki/Doi_(identifier)
[51]: https://doi.org/10.1257%2F00028280260344678
[52]: https://en.wikipedia.org/wiki/Template:Cite_journal
[53]: https://en.wikipedia.org/wiki/Help:CS1_errors#deprecated_params
[54]: http://www.ma.huji.ac.il/raumann/pdf/what%20is%20game%20theory.pdf
[55]: https://en.wikipedia.org/wiki/Econometrica
[56]: https://doi.org/10.2307%2F2938166
[57]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[58]: https://www.jstor.org/stable/2938166
[59]: https://en.wikipedia.org/wiki/John_Harsanyi
[60]: https://doi.org/10.1007%2FBF01737554
[61]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[62]: https://api.semanticscholar.org/CorpusID:154484458
[63]: https://en.wikipedia.org/wiki/Adam_Brandenburger?action=edit&amp;redlink=1
[64]: https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.122.5816
[65]: https://doi.org/10.2307%2F2171725
[66]: https://www.jstor.org/stable/2171725
[67]: https://www.sciencedirect.com/science/article/abs/pii/S0899825611001746
[68]: https://doi.org/10.1016%2Fj.geb.2011.09.010
[69]: https://en.wikipedia.org/wiki/ISSN_(identifier)
[70]: https://search.worldcat.org/issn/0899-8256
[71]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[72]: https://arxiv.org/abs/1702.05778
[73]: https://arxiv.org/archive/cs.AI
[74]: https://en.wikipedia.org/wiki/Template:Game_theory
[75]: https://en.wikipedia.org/wiki/Template_talk:Game_theory
[76]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Game_theory
[77]: https://en.wikipedia.org/wiki/Glossary_of_game_theory
[78]: https://en.wikipedia.org/wiki/List_of_game_theorists
[79]: https://en.wikipedia.org/wiki/List_of_games_in_game_theory
[80]: https://en.wikipedia.org/wiki/Game_theory#Basic_concepts
[81]: https://en.wikipedia.org/wiki/Asynchrony_(game_theory)
[82]: https://en.wikipedia.org/wiki/Bayesian_regret
[83]: https://en.wikipedia.org/wiki/Best_response
[84]: https://en.wikipedia.org/wiki/Bounded_rationality
[85]: https://en.wikipedia.org/wiki/Cheap_talk
[86]: https://en.wikipedia.org/wiki/Coalition
[87]: https://en.wikipedia.org/wiki/Complete_contract
[88]: https://en.wikipedia.org/wiki/Complete_information
[89]: https://en.wikipedia.org/wiki/Complete_mixing
[90]: https://en.wikipedia.org/wiki/Conjectural_variation
[91]: https://en.wikipedia.org/wiki/Contingent_cooperator
[92]: https://en.wikipedia.org/wiki/Coopetition
[93]: https://en.wikipedia.org/wiki/Cooperative_game_theory
[94]: https://en.wikipedia.org/wiki/Dynamic_inconsistency
[95]: https://en.wikipedia.org/wiki/Escalation_of_commitment
[96]: https://en.wikipedia.org/wiki/Farsightedness_(game_theory)
[97]: https://en.wikipedia.org/wiki/Game_semantics
[98]: https://en.wikipedia.org/wiki/Hierarchy_of_beliefs
[99]: https://en.wikipedia.org/wiki/Imperfect_information
[100]: https://en.wikipedia.org/wiki/Incomplete_information
[101]: https://en.wikipedia.org/wiki/Move_by_nature
[102]: https://en.wikipedia.org/wiki/Mutual_knowledge
[103]: https://en.wikipedia.org/wiki/Non-cooperative_game_theory
[104]: https://en.wikipedia.org/wiki/Non-credible_threat
[105]: https://en.wikipedia.org/wiki/Outcome_(game_theory)
[106]: https://en.wikipedia.org/wiki/Perfect_information
[107]: https://en.wikipedia.org/wiki/Ply_(game_theory)
[108]: https://en.wikipedia.org/wiki/Preference_(economics)
[109]: https://en.wikipedia.org/wiki/Rationality
[110]: https://en.wikipedia.org/wiki/Sequential_game
[111]: https://en.wikipedia.org/wiki/Simultaneous_action_selection
[112]: https://en.wikipedia.org/wiki/Spite_(game_theory)
[113]: https://en.wikipedia.org/wiki/Strategic_complements
[114]: https://en.wikipedia.org/wiki/Strategic_dominance
[115]: https://en.wikipedia.org/wiki/Strategic_form
[116]: https://en.wikipedia.org/wiki/Strategic_interaction
[117]: https://en.wikipedia.org/wiki/Strategic_move
[118]: https://en.wikipedia.org/wiki/Strategy_(game_theory)
[119]: https://en.wikipedia.org/wiki/Subgame
[120]: https://en.wikipedia.org/wiki/Succinct_game
[121]: https://en.wikipedia.org/wiki/Topological_game
[122]: https://en.wikipedia.org/wiki/Tragedy_of_the_commons
[123]: https://en.wikipedia.org/wiki/Uncorrelated_asymmetry
[124]: https://en.wikipedia.org/wiki/Win–win_game
[125]: https://en.wikipedia.org/wiki/Zero-sum_game
[126]: https://en.wikipedia.org/wiki/Economic_equilibrium
[127]: https://en.wikipedia.org/wiki/Backward_induction
[128]: https://en.wikipedia.org/wiki/Bayes_correlated_equilibrium
[129]: https://en.wikipedia.org/wiki/Bayesian_efficiency
[130]: https://en.wikipedia.org/wiki/Bayesian_Nash_equilibrium
[131]: https://en.wikipedia.org/wiki/Berge_equilibrium
[132]: https://en.wikipedia.org/wiki/Bertrand–Edgeworth_model
[133]: https://en.wikipedia.org/wiki/Coalition-proof_Nash_equilibrium
[134]: https://en.wikipedia.org/wiki/Core_(game_theory)
[135]: https://en.wikipedia.org/wiki/Correlated_equilibrium
[136]: https://en.wikipedia.org/wiki/Cursed_equilibrium
[137]: https://en.wikipedia.org/wiki/Edgeworth_price_cycle
[138]: https://en.wikipedia.org/wiki/Epsilon-equilibrium
[139]: https://en.wikipedia.org/wiki/Gibbs_measure
[140]: https://en.wikipedia.org/wiki/Incomplete_contracts
[141]: https://en.wikipedia.org/wiki/Inequity_aversion
[142]: https://en.wikipedia.org/wiki/Individual_rationality
[143]: https://en.wikipedia.org/wiki/Iterated_elimination_of_dominated_strategies
[144]: https://en.wikipedia.org/wiki/Markov_perfect_equilibrium
[145]: https://en.wikipedia.org/wiki/Mertens-stable_equilibrium
[146]: https://en.wikipedia.org/wiki/Open-loop_model
[147]: https://en.wikipedia.org/wiki/Pareto_efficiency
[148]: https://en.wikipedia.org/wiki/Payoff_dominance
[149]: https://en.wikipedia.org/wiki/Perfect_Bayesian_equilibrium
[150]: https://en.wikipedia.org/wiki/Price_of_anarchy
[151]: https://en.wikipedia.org/wiki/Program_equilibrium
[152]: https://en.wikipedia.org/wiki/Proper_equilibrium
[153]: https://en.wikipedia.org/wiki/Quantal_response_equilibrium
[154]: https://en.wikipedia.org/wiki/Quasi-perfect_equilibrium
[155]: https://en.wikipedia.org/wiki/Rational_agent
[156]: https://en.wikipedia.org/wiki/Rationalizable_strategy
[157]: https://en.wikipedia.org/wiki/Satisfaction_equilibrium
[158]: https://en.wikipedia.org/wiki/Self-confirming_equilibrium
[159]: https://en.wikipedia.org/wiki/Sequential_equilibrium
[160]: https://en.wikipedia.org/wiki/Shapley_value
[161]: https://en.wikipedia.org/wiki/Strong_Nash_equilibrium
[162]: https://en.wikipedia.org/wiki/Subgame_perfect_equilibrium
[163]: https://en.wikipedia.org/wiki/Appeasement
[164]: https://en.wikipedia.org/wiki/Bid_shading
[165]: https://en.wikipedia.org/wiki/Collusion
[166]: https://en.wikipedia.org/wiki/Commitment_device
[167]: https://en.wikipedia.org/wiki/De-escalation
[168]: https://en.wikipedia.org/wiki/Deterrence_theory
[169]: https://en.wikipedia.org/wiki/Conflict_escalation
[170]: https://en.wikipedia.org/wiki/Fictitious_play
[171]: https://en.wikipedia.org/wiki/Focal_point_(game_theory)
[172]: https://en.wikipedia.org/wiki/Grim_trigger
[173]: https://en.wikipedia.org/wiki/Hobbesian_trap
[174]: https://en.wikipedia.org/wiki/Markov_strategy
[175]: https://en.wikipedia.org/wiki/Max-dominated_strategy
[176]: https://en.wikipedia.org/wiki/Tit_for_tat
[177]: https://en.wikipedia.org/wiki/Win–stay,_lose–switch
[178]: https://en.wikipedia.org/wiki/All-pay_auction
[179]: https://en.wikipedia.org/wiki/Battle_of_the_sexes_(game_theory)
[180]: https://en.wikipedia.org/wiki/Bargaining_problem
[181]: https://en.wikipedia.org/wiki/Bertrand_competition
[182]: https://en.wikipedia.org/wiki/Blotto_game
[183]: https://en.wikipedia.org/wiki/Centipede_game
[184]: https://en.wikipedia.org/wiki/Cournot_competition
[185]: https://en.wikipedia.org/wiki/Deadlock_(game_theory)
[186]: https://en.wikipedia.org/wiki/Dictator_game
[187]: https://en.wikipedia.org/wiki/Dictator_game#Trust_game
[188]: https://en.wikipedia.org/wiki/Unscrupulous_diner's_dilemma
[189]: https://en.wikipedia.org/wiki/Dollar_auction
[190]: https://en.wikipedia.org/wiki/El_Farol_Bar_problem
[191]: https://en.wikipedia.org/wiki/Electronic_mail_game
[192]: https://en.wikipedia.org/wiki/Gift-exchange_game
[193]: https://en.wikipedia.org/wiki/Guess_2/3_of_the_average
[194]: https://en.wikipedia.org/wiki/Keynesian_beauty_contest
[195]: https://en.wikipedia.org/wiki/Kuhn_poker
[196]: https://en.wikipedia.org/wiki/Lewis_signaling_game
[197]: https://en.wikipedia.org/wiki/Obligationes
[198]: https://en.wikipedia.org/wiki/Optional_prisoner's_dilemma
[199]: https://en.wikipedia.org/wiki/Pirate_game
[200]: https://en.wikipedia.org/wiki/Public_goods_game
[201]: https://en.wikipedia.org/wiki/Rendezvous_problem
[202]: https://en.wikipedia.org/wiki/Stackelberg_competition
[203]: https://en.wikipedia.org/wiki/Traveler's_dilemma
[204]: https://en.wikipedia.org/wiki/Volunteer's_dilemma
[205]: https://en.wikipedia.org/wiki/War_of_attrition_(game)
[206]: https://en.wikipedia.org/wiki/Game_theory#Theorems
[207]: https://en.wikipedia.org/wiki/Arrow's_impossibility_theorem
[208]: https://en.wikipedia.org/wiki/Aumann's_agreement_theorem
[209]: https://en.wikipedia.org/wiki/Brouwer_fixed-point_theorem
[210]: https://en.wikipedia.org/wiki/Competitive_altruism
[211]: https://en.wikipedia.org/wiki/Folk_theorem_(game_theory)
[212]: https://en.wikipedia.org/wiki/Gibbard–Satterthwaite_theorem
[213]: https://en.wikipedia.org/wiki/Gibbs_lemma
[214]: https://en.wikipedia.org/wiki/Glicksberg's_theorem
[215]: https://en.wikipedia.org/wiki/Kakutani_fixed-point_theorem
[216]: https://en.wikipedia.org/wiki/One-shot_deviation_principle
[217]: https://en.wikipedia.org/wiki/Prim–Read_theory
[218]: https://en.wikipedia.org/wiki/Rational_ignorance
[219]: https://en.wikipedia.org/wiki/Rational_irrationality
[220]: https://en.wikipedia.org/wiki/Sperner's_lemma
[221]: https://en.wikipedia.org/wiki/Zermelo's_theorem_(game_theory)
[222]: https://en.wikipedia.org/wiki/Algorithmic_game_theory
[223]: https://en.wikipedia.org/wiki/Behavioral_game_theory
[224]: https://en.wikipedia.org/wiki/Behavioral_strategy
[225]: https://en.wikipedia.org/wiki/Compositional_game_theory
[226]: https://en.wikipedia.org/wiki/Confrontation_analysis
[227]: https://en.wikipedia.org/wiki/Contract_theory
[228]: https://en.wikipedia.org/wiki/Drama_theory
[229]: https://en.wikipedia.org/wiki/Graphical_game_theory
[230]: https://en.wikipedia.org/wiki/Heresthetic
[231]: https://en.wikipedia.org/wiki/Mean-field_game_theory
[232]: https://en.wikipedia.org/wiki/Negotiation_theory
[233]: https://en.wikipedia.org/wiki/Quantum_game_theory
[234]: https://en.wikipedia.org/wiki/Social_software_(research_field)
[235]: https://en.wikipedia.org/wiki/Albert_W._Tucker
[236]: https://en.wikipedia.org/wiki/Alvin_E._Roth
[237]: https://en.wikipedia.org/wiki/Amos_Tversky
[238]: https://en.wikipedia.org/wiki/Antoine_Augustin_Cournot
[239]: https://en.wikipedia.org/wiki/David_Gale
[240]: https://en.wikipedia.org/wiki/David_K._Levine
[241]: https://en.wikipedia.org/wiki/David_M._Kreps
[242]: https://en.wikipedia.org/wiki/Donald_B._Gillies
[243]: https://en.wikipedia.org/wiki/Drew_Fudenberg
[244]: https://en.wikipedia.org/wiki/Eric_Maskin
[245]: https://en.wikipedia.org/wiki/Harold_W._Kuhn
[246]: https://en.wikipedia.org/wiki/Herbert_A._Simon
[247]: https://en.wikipedia.org/wiki/Herbert_Scarf
[248]: https://en.wikipedia.org/wiki/Hervé_Moulin
[249]: https://en.wikipedia.org/wiki/Jean_Tirole
[250]: https://en.wikipedia.org/wiki/Jean-François_Mertens
[251]: https://en.wikipedia.org/wiki/Jennifer_Tour_Chayes
[252]: https://en.wikipedia.org/wiki/Ken_Binmore
[253]: https://en.wikipedia.org/wiki/Kenneth_Arrow
[254]: https://en.wikipedia.org/wiki/Leonid_Hurwicz
[255]: https://en.wikipedia.org/wiki/Lloyd_Shapley
[256]: https://en.wikipedia.org/wiki/Martin_Shubik
[257]: https://en.wikipedia.org/wiki/Melvin_Dresher
[258]: https://en.wikipedia.org/wiki/Merrill_M._Flood
[259]: https://en.wikipedia.org/wiki/Olga_Bondareva
[260]: https://en.wikipedia.org/wiki/Oskar_Morgenstern
[261]: https://en.wikipedia.org/wiki/Paul_Milgrom
[262]: https://en.wikipedia.org/wiki/Peyton_Young
[263]: https://en.wikipedia.org/wiki/Reinhard_Selten
[264]: https://en.wikipedia.org/wiki/Robert_Axelrod_(political_scientist)
[265]: https://en.wikipedia.org/wiki/Robert_B._Wilson
[266]: https://en.wikipedia.org/wiki/Roger_Myerson
[267]: https://en.wikipedia.org/wiki/Samuel_Bowles_(economist)
[268]: https://en.wikipedia.org/wiki/Suzanne_Scotchmer
[269]: https://en.wikipedia.org/wiki/Thomas_Schelling
[270]: https://en.wikipedia.org/wiki/William_Vickrey
[271]: https://en.wikipedia.org/wiki/Combinatorial_game_theory
[272]: https://en.wikipedia.org/wiki/Combinatorial_explosion
[273]: https://en.wikipedia.org/wiki/Determinacy
[274]: https://en.wikipedia.org/wiki/Disjunctive_sum
[275]: https://en.wikipedia.org/wiki/First-player_and_second-player_win
[276]: https://en.wikipedia.org/wiki/Game_complexity
[277]: https://en.wikipedia.org/wiki/Impartial_game
[278]: https://en.wikipedia.org/wiki/Misère
[279]: https://en.wikipedia.org/wiki/Partisan_game
[280]: https://en.wikipedia.org/wiki/Solved_game
[281]: https://en.wikipedia.org/wiki/Sprague–Grundy_theorem
[282]: https://en.wikipedia.org/wiki/Strategy-stealing_argument
[283]: https://en.wikipedia.org/wiki/Zugzwang
[284]: https://en.wikipedia.org/wiki/Chess
[285]: https://en.wikipedia.org/wiki/Chomp
[286]: https://en.wikipedia.org/wiki/Clobber
[287]: https://en.wikipedia.org/wiki/Cram_(game)
[288]: https://en.wikipedia.org/wiki/Domineering
[289]: https://en.wikipedia.org/wiki/Hackenbush
[290]: https://en.wikipedia.org/wiki/Nim
[291]: https://en.wikipedia.org/wiki/Notakto
[292]: https://en.wikipedia.org/wiki/Subtract_a_square
[293]: https://en.wikipedia.org/wiki/Sylver_coinage
[294]: https://en.wikipedia.org/wiki/Toads_and_Frogs
[295]: https://en.wikipedia.org/wiki/Mex_(mathematics)
[296]: https://en.wikipedia.org/wiki/Nimber
[297]: https://en.wikipedia.org/wiki/On_Numbers_and_Games
[298]: https://en.wikipedia.org/wiki/Star_(game_theory)
[299]: https://en.wikipedia.org/wiki/Surreal_number
[300]: https://en.wikipedia.org/wiki/Winning_Ways_for_Your_Mathematical_Plays
[301]: https://en.wikipedia.org/wiki/Alpha–beta_pruning
[302]: https://en.wikipedia.org/wiki/Expectiminimax
[303]: https://en.wikipedia.org/wiki/Minimax
[304]: https://en.wikipedia.org/wiki/Monte_Carlo_tree_search
[305]: https://en.wikipedia.org/wiki/Negamax
[306]: https://en.wikipedia.org/wiki/Paranoid_algorithm
[307]: https://en.wikipedia.org/wiki/Principal_variation_search
[308]: https://en.wikipedia.org/wiki/Claude_Shannon
[309]: https://en.wikipedia.org/wiki/John_Conway
[310]: https://en.wikipedia.org/wiki/John_von_Neumann
[311]: https://en.wikipedia.org/wiki/Evolutionary_game_theory
[312]: https://en.wikipedia.org/wiki/Bishop–Cannings_theorem
[313]: https://en.wikipedia.org/wiki/Evolution_and_the_Theory_of_Games
[314]: https://en.wikipedia.org/wiki/Evolutionarily_stable_set
[315]: https://en.wikipedia.org/wiki/Evolutionarily_stable_state
[316]: https://en.wikipedia.org/wiki/Replicator_equation
[317]: https://en.wikipedia.org/wiki/Risk_dominance
[318]: https://en.wikipedia.org/wiki/Stochastically_stable_equilibrium
[319]: https://en.wikipedia.org/wiki/Weak_evolutionarily_stable_strategy
[320]: https://en.wikipedia.org/wiki/Chicken_(game)
[321]: https://en.wikipedia.org/wiki/Cultural_group_selection
[322]: https://en.wikipedia.org/wiki/Fisher's_principle
[323]: https://en.wikipedia.org/wiki/Mobbing_(animal_behavior)
[324]: https://en.wikipedia.org/wiki/Terminal_investment_hypothesis
[325]: https://en.wikipedia.org/wiki/John_Maynard_Smith
[326]: https://en.wikipedia.org/wiki/George_R._Price
[327]: https://en.wikipedia.org/wiki/William_Donald_Hamilton
[328]: https://en.wikipedia.org/wiki/Mechanism_design
[329]: https://en.wikipedia.org/wiki/Algorithmic_mechanism_design
[330]: https://en.wikipedia.org/wiki/Bayesian-optimal_mechanism
[331]: https://en.wikipedia.org/wiki/Incentive_compatibility
[332]: https://en.wikipedia.org/wiki/Market_design
[333]: https://en.wikipedia.org/wiki/Myerson_ironing
[334]: https://en.wikipedia.org/wiki/Monotonicity_(mechanism_design)
[335]: https://en.wikipedia.org/wiki/Participation_constraint_(mechanism_design)
[336]: https://en.wikipedia.org/wiki/Revelation_principle
[337]: https://en.wikipedia.org/wiki/Strategyproofness
[338]: https://en.wikipedia.org/wiki/Vickrey–Clarke–Groves_mechanism
[339]: https://en.wikipedia.org/wiki/Virtual_valuation
[340]: https://en.wikipedia.org/wiki/Myerson–Satterthwaite_theorem
[341]: https://en.wikipedia.org/wiki/Revenue_equivalence
[342]: https://en.wikipedia.org/wiki/Border's_theorem
[343]: https://en.wikipedia.org/wiki/Digital_goods_auction
[344]: https://en.wikipedia.org/wiki/Knapsack_auction
[345]: https://en.wikipedia.org/wiki/Truthful_cake-cutting
[346]: https://en.wikipedia.org/wiki/Bertrand_paradox_(economics)
[347]: https://en.wikipedia.org/wiki/Chainstore_paradox
[348]: https://en.wikipedia.org/wiki/Computational_complexity_of_games
[349]: https://en.wikipedia.org/wiki/Helly_metric
[350]: https://en.wikipedia.org/wiki/Multi-agent_system
[351]: https://en.wikipedia.org/wiki/PPAD_(complexity)
[352]: https://en.wikipedia.org/wiki/File:Square_root_of_x.svg
[353]: https://en.wikipedia.org/wiki/Portal:Mathematics
[354]: https://en.wikipedia.org/wiki/File:Commons-logo.svg
[355]: https://commons.wikimedia.org/wiki/Category:Game%20theory
[356]: https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Game_theory
[357]: https://en.wikipedia.org/wiki/Category:Game_theory
[358]: https://en.wikipedia.org/wiki/Help:Authority_control
[359]: https://www.wikidata.org/wiki/Q1546627#identifiers
[360]: https://d-nb.info/gnd/4182285-7
[361]: https://aleph.nkp.cz/F/?func=find-c&amp;local_base=aut&amp;ccl_term=ica=ph135592&amp;CON_LNG=ENG
[362]: https://en.wikipedia.org/w/index.php?title=Strategy_(game_theory)&amp;oldid=1347054546
[363]: /wiki/Help:Category
[364]: /wiki/Category:Strategy_(game_theory)
[365]: /wiki/Category:Articles_with_short_description
[366]: /wiki/Category:Short_description_matches_Wikidata
[367]: /wiki/Category:CS1_errors:_deprecated_parameters
[368]: /wiki/Category:All_articles_with_incomplete_citations
[369]: /wiki/Category:Articles_with_incomplete_citations_from_September_2018
[370]: /wiki/Category:Commons_category_link_is_locally_defined
