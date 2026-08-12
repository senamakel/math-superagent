<!-- source: https://en.wikipedia.org/wiki/Pursuit-evasion | converted from HTML -->

Pursuit–evasion - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

(Redirected from [Pursuit-evasion][1])

Mathematical game/problem

[image: icon] [2]

 |

This article **needs [more citations][3]**. Please help [improve this article][4] by [adding citations to reliable sources][5]. Unsourced material may be challenged and [removed][6].
*Find sources:*["Pursuit–evasion"][7] – [news][8]**·**[newspapers][9]**·**[books][10]**·**[scholar][11]**·**[JSTOR][12]*( October 2021)**( [Learn how and when to remove this message][13])*

 |

**Pursuit–evasion**(variants of which are referred to as **cops and robbers**and **graph searching**) is a family of problems in [mathematics][14] and [computer science][15] in which one group attempts to track down members of another group in an environment. Early work on problems of this type modeled the environment geometrically. [1] In 1976, [Torrence Parsons][16] introduced a formulation whereby movement is constrained by a [graph][17]. [2] The geometric formulation is sometimes called **continuous pursuit–evasion**, and the graph formulation **discrete pursuit–evasion**(also called **graph searching**). Current research is typically limited to one of these two formulations.

## Discrete formulation

[[edit][18]]

In the discrete formulation of the pursuit–evasion problem, the environment is modeled as a [graph][17].

### Problem definition

[[edit][19]]

There are innumerable possible variants of pursuit–evasion, though they tend to share many elements. A typical, basic example is as follows (cops and robber games): Pursuers and evaders occupy [nodes][20] of a graph. The two sides take alternate turns, which consist of each member either staying put or moving along an [edge][21] to an adjacent node. If a pursuer occupies the same node as an evader the evader is captured and removed from the graph. The question usually posed is how many pursuers are necessary to ensure the eventual capture of all the evaders. If one pursuer suffices, the graph is called a [cop-win graph][22]. In this case, a single evader can always be captured in time linear to the number of *n*nodes of the graph. Capturing *r*evaders with *k*pursuers can take in the order of *rn*time as well, but the exact bounds for more than one pursuer are [still unknown][23].

Often the movement rules are altered by changing the velocity of the evaders. This velocity is the maximum number of edges that an evader can move along in a single turn. In the example above, the evaders have a velocity of one. At the other extreme is the concept of [infinite][24] velocity, which allows an evader to move to any node in the graph so long as there is a [path][25] between its original and final positions that contains no nodes occupied by a pursuer. Similarly some variants arm the pursuers with "helicopters" which allow them to move to any vertex on their turn.

Other variants ignore the restriction that pursuers and evaders must always occupy a node and allow for the possibility that they are positioned somewhere along an edge. These variants are often referred to as **sweeping problems**, whilst the previous variants would fall under the category of **searching problems**.

### Variants

[[edit][26]]

Several variants are equivalent to important graph parameters. Specifically, finding the number of pursuers necessary to capture a single evader with infinite velocity in a graph *G*(when pursuers and evader are not constrained to move turn by turn, but move simultaneously) is equivalent to finding the [treewidth][27] of *G*, and a winning strategy for the evader may be described in terms of a [haven][28] in *G*. If this evader is invisible to the pursuers then the problem is equivalent to finding the [pathwidth][29] or vertex separation. [3] Finding the number of pursuers necessary to capture a single invisible evader in a graph *G*in a single turn (that is, one movement by the pursuers from their initial deployment) is equivalent to finding the size of the minimum [dominating set][30] of *G*, assuming the pursuers can initially deploy wherever they like (this later assumption holds when pursuers and evader are assumed to move turn by turn).

The board game [Scotland Yard][31] is a variant of the pursuit–evasion problem.

### Complexity

[[edit][32]]

The complexity of several pursuit–evasion variants, namely how many pursuers are needed to clear a given graph and how a given number of pursuers should move on the graph to clear it with either a minimum sum of their travel distances or minimum task-completion time, has been studied by [Nimrod Megiddo][33], [S. L. Hakimi][34], [Michael R. Garey][35], [David S. Johnson][36], and [Christos H. Papadimitriou][37] (J. ACM 1988), and R. Borie, C. Tovey and S. Koenig. [4]

### Multi-player pursuit–evasion games

[[edit][38]]

Solving multi-player pursuit–evasion games has also received increased attention; see R Vidal et al., Chung and Furukawa [39], Hespanha et al. and the references therein. Marcos A. M. Vieira and Ramesh Govindan and Gaurav S. Sukhatme provided an algorithm that computes the minimal completion time strategy for pursuers to capture all evaders when all players make optimal decisions based on complete knowledge. This algorithm can also be applied to when evader are significantly faster than pursuers. Unfortunately, these algorithms do not scale beyond a small number of robots. To overcome this problem, Marcos A. M. Vieira and Ramesh Govindan and Gaurav S. Sukhatme design and implement a partition algorithm where pursuers capture evaders by decomposing the game into multiple multi-pursuer single-evader games.

## Continuous formulation

[[edit][40]]

In the continuous formulation of pursuit–evasion games, the environment is modeled geometrically, typically taking the form of the [Euclidean plane][41] or another [manifold][42]. Variants of the game may impose maneuverability constraints on the players, such as a limited range of speed or acceleration. Obstacles may also be used.

If a lion is chasing a man with equal speed, then it is clear that the man can escape on a plane or a sphere by always moving on the straight line away from the lion. When both are confined in a circular disk, it seemed likely for the lion to catch the man. Besicovitch proved in 1952 that the man has a strategy to evade capture indefinitely against any strategy. [5]

## Applications

[[edit][43]]

One of the initial applications of the pursuit–evasion problem was [missile guidance][44] systems formulated by [Rufus Isaacs][45] at the [RAND Corporation][46]. [1]

## See also

[[edit][47]]

- [Angel problem][48]
- *[Chases and Escapes][49]*
- [Homicidal chauffeur problem][50]
- [Princess and monster game][51]
- [Search games][52]
- [Pursuit curve][53]

## Notes

[[edit][54]]

1. 1 2 Isaacs 1965
2. ↑ Parsons 1976
3. ↑ Ellis 1994
4. ↑ Borie 2009
5. ↑ Littlewood, John Edensor (1988). Bollobás, Béla (ed.). *Littlewood's miscellany*(Rev. ed., repr ed.). Cambridge: Cambridge University Press. pp. 114– 117. [ISBN][55] [978-0-521-33702-1][56].

## References

[[edit][57]]

- [Isaacs, R.][45] (1965). *Differential Games: A Mathematical Theory with Applications to Warfare and Pursuit, Control and Optimization*. New York: John Wiley & Sons. [OCLC][58] [489835778][59].
- [Parsons, T. D.][16] (1976). "Pursuit–evasion in a graph". *Theory and Applications of Graphs*. Springer-Verlag. pp. 426– 441.
- Borie, R.; Tovey, C.; Koenig, S. (2009). ["Algorithms and Complexity Results for Pursuit–Evasion Problems"][60]. In Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI). Retrieved 2010-03-11.
- Ellis, J.; Sudborough, I.; Turner, J. (1994). ["The vertex separation and search number of a graph"][61]. *Information and Computation*. **113**(1): 50– 79. [doi][62]: [10.1006/inco.1994.1064][61].
- Fomin, F.V.; Thilikos, D. (2008). ["An annotated bibliography on guaranteed graph searching"][63]. *Theoretical Computer Science*. **399**(3): 236– 245. [doi][62]: [10.1016/j.tcs.2008.02.040][63].
- Kirousis, M.; [Papadimitriou, C.][64] (1986). ["Searching and pebbling"][65]. *Theoretical Computer Science*. **42**(2): 205– 218. [doi][62]: [10.1016/0304-3975(86)90146-5][65].
- Nowakowski, R.; Winkler, P. (1983). ["Vertex-to-vertex pursuit in a graph"][66]. *Discrete Mathematics*. **43**( 2– 3): 235– 239. [doi][62]: [10.1016/0012-365X(83)90160-7][66].
- [Petrosjan, Leon][67] (1993). "Differential Games of Pursuit (Series on Optimization, Vol 2)". *World Scientific Pub Co Inc*. **2**.
- [Seymour, P.][68]; [Thomas, R.][69] (1993). ["Graph searching, and a min-max theorem for tree-width"][70]. *Journal of Combinatorial Theory, Series B*. **58**(1): 22– 33. [doi][62]: [10.1006/jctb.1993.1027][70].
- Vidal; et al. (2002). ["Probabilistic pursuit–evasion games: theory, implementation, and experimental evaluation"][71] (PDF). *IEEE Transactions on Robotics and Automation*. **18**(5): 662– 669. [doi][62]: [10.1109/TRA.2002.804040][72].
- Marcos A. M. Vieira; Ramesh Govindan & Gaurav S. Sukhatme. "Scalable and Practical Pursuit–Evasion with Networked Robots". *Journal of Intelligent Service Robotics*: [73].
- Chung and Furukawa (2008). "A Reachability-Based Strategy for the Time-Optimal Control of Autonomous Pursuers". *Engineering Optimization*. **40**(1): 67– 93. [Bibcode][74]: [2008EnOp...40...67C][75]. [doi][62]: [10.1080/03052150701593133][76]. [S2CID][77] [120015118][78].
- Hespanha; et al. (1999). "Multiple-agent probabilistic pursuit–evasion games". *Proceedings of the 38th IEEE Conference on Decision and Control*. pp. 2432– 2437.

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Pursuit–evasion&oldid=1368306851][79] "

[Categories][80]:

- [Pursuit–evasion][81]
- [Combat modeling][82]

Hidden categories:

- [Articles with short description][83]
- [Short description matches Wikidata][84]
- [Articles needing additional references from October 2021][85]
- [All articles needing additional references][86]

Search

Pursuit–evasion

4 languages Add topic


## Links

[1]: /w/index.php?title=Pursuit-evasion&amp;redirect=no
[2]: https://en.wikipedia.org/wiki/File:Question_book-new.svg
[3]: https://en.wikipedia.org/wiki/Wikipedia:Verifiability
[4]: https://en.wikipedia.org/wiki/Special:EditPage/Pursuit–evasion
[5]: https://en.wikipedia.org/wiki/Help:Referencing_for_beginners
[6]: https://en.wikipedia.org/wiki/Wikipedia:Verifiability#Burden_of_evidence
[7]: https://www.google.com/search?as_eq=wikipedia&amp;q=%22Pursuit%E2%80%93evasion%22
[8]: https://www.google.com/search?tbm=nws&amp;q=%22Pursuit%E2%80%93evasion%22+-wikipedia&amp;tbs=ar:1
[9]: https://www.google.com/search?amp;q=%22Pursuit%E2%80%93evasion%22&amp;tbs=bkt:s&amp;tbm=bks
[10]: https://www.google.com/search?tbs=bks:1&amp;q=%22Pursuit%E2%80%93evasion%22+-wikipedia
[11]: https://scholar.google.com/scholar?q=%22Pursuit%E2%80%93evasion%22
[12]: https://www.jstor.org/action/doBasicSearch?Query=%22Pursuit%E2%80%93evasion%22&amp;acc=on&amp;wc=on
[13]: https://en.wikipedia.org/wiki/Help:Maintenance_template_removal
[14]: https://en.wikipedia.org/wiki/Mathematics
[15]: https://en.wikipedia.org/wiki/Computer_science
[16]: https://en.wikipedia.org/wiki/Torrence_Parsons
[17]: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)
[18]: /w/index.php?title=Pursuit%E2%80%93evasion&amp;action=edit&amp;section=1
[19]: /w/index.php?title=Pursuit%E2%80%93evasion&amp;action=edit&amp;section=2
[20]: https://en.wikipedia.org/wiki/Node_(graph_theory)
[21]: https://en.wikipedia.org/wiki/Edge_(graph_theory)
[22]: https://en.wikipedia.org/wiki/Cop-win_graph
[23]: https://en.wikipedia.org/wiki/Open_problem
[24]: https://en.wikipedia.org/wiki/Infinity
[25]: https://en.wikipedia.org/wiki/Path_(graph_theory)
[26]: /w/index.php?title=Pursuit%E2%80%93evasion&amp;action=edit&amp;section=3
[27]: https://en.wikipedia.org/wiki/Treewidth
[28]: https://en.wikipedia.org/wiki/Haven_(graph_theory)
[29]: https://en.wikipedia.org/wiki/Pathwidth
[30]: https://en.wikipedia.org/wiki/Dominating_set
[31]: https://en.wikipedia.org/wiki/Scotland_Yard_(board_game)
[32]: /w/index.php?title=Pursuit%E2%80%93evasion&amp;action=edit&amp;section=4
[33]: https://en.wikipedia.org/wiki/Nimrod_Megiddo
[34]: https://en.wikipedia.org/wiki/S._L._Hakimi
[35]: https://en.wikipedia.org/wiki/Michael_R._Garey
[36]: https://en.wikipedia.org/wiki/David_S._Johnson
[37]: https://en.wikipedia.org/wiki/Christos_H._Papadimitriou
[38]: /w/index.php?title=Pursuit%E2%80%93evasion&amp;action=edit&amp;section=5
[39]: https://web.archive.org/web/20070831180125/http://cmr.mech.unsw.edu.au/people/AlexChung/cfchung.htm
[40]: /w/index.php?title=Pursuit%E2%80%93evasion&amp;action=edit&amp;section=6
[41]: https://en.wikipedia.org/wiki/Euclidean_plane
[42]: https://en.wikipedia.org/wiki/Manifold
[43]: /w/index.php?title=Pursuit%E2%80%93evasion&amp;action=edit&amp;section=7
[44]: https://en.wikipedia.org/wiki/Missile_guidance
[45]: https://en.wikipedia.org/wiki/Rufus_Isaacs_(game_theorist)
[46]: https://en.wikipedia.org/wiki/RAND_Corporation
[47]: /w/index.php?title=Pursuit%E2%80%93evasion&amp;action=edit&amp;section=8
[48]: https://en.wikipedia.org/wiki/Angel_problem
[49]: https://en.wikipedia.org/wiki/Chases_and_Escapes
[50]: https://en.wikipedia.org/wiki/Homicidal_chauffeur_problem
[51]: https://en.wikipedia.org/wiki/Princess_and_monster_game
[52]: https://en.wikipedia.org/wiki/Search_games
[53]: https://en.wikipedia.org/wiki/Pursuit_curve
[54]: /w/index.php?title=Pursuit%E2%80%93evasion&amp;action=edit&amp;section=9
[55]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[56]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-33702-1
[57]: /w/index.php?title=Pursuit%E2%80%93evasion&amp;action=edit&amp;section=10
[58]: https://en.wikipedia.org/wiki/OCLC_(identifier)
[59]: https://search.worldcat.org/oclc/489835778
[60]: http://www.aaai.org/ocs/index.php/IJCAI/IJCAI-09/paper/viewPDFInterstitial/482/591
[61]: https://doi.org/10.1006%2Finco.1994.1064
[62]: https://en.wikipedia.org/wiki/Doi_(identifier)
[63]: https://doi.org/10.1016%2Fj.tcs.2008.02.040
[64]: https://en.wikipedia.org/wiki/Christos_Papadimitriou
[65]: https://doi.org/10.1016%2F0304-3975%2886%2990146-5
[66]: https://doi.org/10.1016%2F0012-365X%2883%2990160-7
[67]: https://en.wikipedia.org/wiki/Leon_Petrosyan
[68]: https://en.wikipedia.org/wiki/Paul_Seymour_(mathematician)
[69]: https://en.wikipedia.org/wiki/Robin_Thomas_(mathematician)
[70]: https://doi.org/10.1006%2Fjctb.1993.1027
[71]: https://www.cs.berkeley.edu/~sastry/pubs/PDFs%20of%20Pubs2000-2005/Pdfs%20of%20Misc.Others/Vidal/VidalShakerniaProbabilistic2002.pdf
[72]: https://doi.org/10.1109%2FTRA.2002.804040
[73]: https://doi.org/10.1007%2Fs11370-009-0050-y
[74]: https://en.wikipedia.org/wiki/Bibcode_(identifier)
[75]: https://ui.adsabs.harvard.edu/abs/2008EnOp...40...67C
[76]: https://doi.org/10.1080%2F03052150701593133
[77]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[78]: https://api.semanticscholar.org/CorpusID:120015118
[79]: https://en.wikipedia.org/w/index.php?title=Pursuit–evasion&amp;oldid=1368306851
[80]: /wiki/Help:Category
[81]: /wiki/Category:Pursuit%E2%80%93evasion
[82]: /wiki/Category:Combat_modeling
[83]: /wiki/Category:Articles_with_short_description
[84]: /wiki/Category:Short_description_matches_Wikidata
[85]: /wiki/Category:Articles_needing_additional_references_from_October_2021
[86]: /wiki/Category:All_articles_needing_additional_references
