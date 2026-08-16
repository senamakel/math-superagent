<!-- source: https://www.erdosproblems.com/forum/thread/64 | converted from HTML -->

64 Discussion Thread | Erdős Problems

[image: Logo] [1]

[Forum][2] [Inbox][3] [Favourites][4] [Tags][5]

More

[FAQ][6] [Prizes][7] [Problem Lists][8] [Definitions][9] [Links][10]

[Forum][2]

Menu

[Inbox][3] [Favourites][4] [Tags][5] [FAQ][6] [Prizes][7] [Problem Lists][8] [Definitions][9] [Links][10]

Dual View [Random Solved][11] [Random Open][12]

FALSIFIABLE Open, but could be disproved with a finite counterexample. - $1000

Does every finite graph with minimum degree at least 3 contain a cycle of length $2^k$ for some $k\geq 2$?

[#64][13]: [Er93,p.343] [Er94b] [Er95,p.174] [Er96] [Er97b] [Er97c]

[graph theory][14] | [cycles][15]

The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.

Comment activity that has not yet been incorporated into the remarks

None Partial Solution

There are no solutions, partial or complete, claimed in the comments.

-->

Conjectured by Erdős and Gyárfás, who believed the answer must be negative, and in fact for every $r$ there must be a graph of minimum degree at least $r$ without a cycle of length $2^k$ for any $k\geq 2$.

This was solved in the affirmative if the minimum degree is larger than some absolute constant by Liu and Montgomery [LiMo20] (therefore disproving the above stronger conjecture of Erdős and Gyárfás). Liu and Montgomery prove a much stronger result: if the average degree of $G$ is sufficiently large then there is some large integer $\ell$ such that for every even integer $m\in [(\log \ell)^8,\ell]$, $G$ contains a cycle of length $m$.

An infinite tree with minimum degree $3$ shows that the answer is trivially false for infinite graphs.

The conjecture has been confirmed for various families of graphs; see the comment by Alfaiz for a list.

This problem is [#69 in Extremal Graph Theory][16] in the graphs problem collection.

[View the LaTeX source][17]

This page was last edited 10 April 2026. [View history][18]

External data from [the database][19] - you can help update this
Formalised statement? [Yes][20]

[2 comments on this problem][21]

[0 claimed proofs for this problem][22]

**Likes this problem** | [Fedir][23], [Chillguy][24], [Sam_Petkov][25], [mattryanwatts][26], [ZackaryLoevseth][27] |

**Interested in collaborating** | [Sam_Petkov][25], [ZackaryLoevseth][27] |

**Currently working on this problem** | [Sam_Petkov][25], [mattryanwatts][26], [RajveerKapoor][28] |

**This problem looks difficult** | None  |

**This problem looks tractable** | None  |

**The results on this problem could be formalisable** | None  |

**I am working on formalising the results on this problem** | None  |

**Additional thanks to**: Alfaiz, Desmond Weisenberg, and Yuval Wigderson

When referring to this problem, please use the original sources of Erdős. If you wish to acknowledge this website, the recommended citation format is:

T. F. Bloom, Erdős Problem #64, https://www.erdosproblems.com/64, accessed 2026-08-16

Order by [oldest first][29] or [newest first][30]. (The most recent comments are highlighted in a red border.)

-

A small improvement building on the work of A. Carr: any minimal counterexample has strictly more than \(2/3\) (up from \(4/7\)) of its vertices of degree exactly \(3\). Found by ChatGPT 5.6 Sol High, not verified.

Let \(G\) be a counterexample to the Erdős--Gyárfás conjecture of minimum order and, subject to that, minimum size. Define\[ V_3=\{v\in V(G):d(v)=3\}, \qquad V_{\ge4}=\{v\in V(G):d(v)\ge4\}. \]Then\[ |V_3|\ge 2|V_{\ge4}|+1, \]and consequently\[ |V_3|>\frac23|V(G)|. \]Carr proved that \(V_{\ge4}\) is independent and that every vertex of \(G\) has a neighbor of degree \(3\). Hence every edge incident with \(V_{\ge4}\) joins \(V_{\ge4}\) to \(V_3\), while every vertex of \(V_3\) has at most two neighbors in \(V_{\ge4}\). Therefore\[ 4|V_{\ge4}| \le \sum_{v\in V_{\ge4}}d(v) =e(V_{\ge4},V_3) \le 2|V_3|, \]so\[ |V_3|\ge2|V_{\ge4}|. \]It remains to exclude equality. Suppose that\[ |V_3|=2|V_{\ge4}|. \]Equality must then hold throughout the preceding inequalities. Thus every vertex of \(V_{\ge4}\) has degree \(4\), and every vertex of \(V_3\) has exactly two neighbors in \(V_{\ge4}\) and one neighbor in \(V_3\). Construct a graph \(H\) with vertex set \(V_{\ge4}\) by replacing each \(x\in V_3\), whose two neighbors in \(V_{\ge4}\) are \(u_x\) and \(v_x\), with the edge \(u_xv_x\). The graph \(H\) is simple: two distinct vertices of \(V_3\) with the same two neighbors in \(V_{\ge4}\) would form a \(4\)-cycle in \(G\). Moreover, every vertex of \(H\) has degree \(4\). Since\[ |V(H)|=|V_{\ge4}|<|V(G)|, \]the minimality of \(G\) implies that \(H\) contains a cycle of length \(2^k\) for some \(k\ge2\). Replacing each edge of this cycle by its corresponding two-edge path through \(V_3\) produces a cycle in \(G\) of length\[ 2^{k+1}, \]a contradiction. Hence equality is impossible, and\[ |V_3|\ge2|V_{\ge4}|+1. \]Finally,\[ 3|V_3| >2\bigl(|V_3|+|V_{\ge4}|\bigr) =2|V(G)|, \]and therefore\[ |V_3|>\frac23|V(G)|. \]

**[jul059][31]**— [16:32 on 26 Jul 2026][32]

👍 0 📝 0 🤖 0

-

The conjecture is confirmed for these cases:

(i) $K_{1,m}$-free graphs with minimum degree at least $m+1$ or maximum degree at least $2m-1$ by S. E. Shauger in [Sh98].
(ii) Planar claw-free graphs by D. Daniel and S. E. Shauger in [DaSh01].
(iii) 3-connected cubic planar graphs by C. C. Heckman and R. Krakovski in [HeKr13].
(iv) Cayley graphs on generalized quaternion groups, dihedral groups, semidihedral groups and groups of order $p^3$ in M. H. Ghaffari and Z. Mostaghim [[GhMo18]][33].
(v) Cayley graphs of order $2p^2$ and $4p$ by M. Ghasemi and R. Varmazyar in [[GhVa21]][34].
(vi) $P_8$-free graphs by Y. Gao and S. Shan in [[GaSh22]][35].
(vii) $P_{10}$-free graphs by Z. Hu and C. Shen in [[HuSh24]][36].
(viii) Diameter-2 graphs by A. Carr in [[Ca26]][37].

Additionally:
(I) K. Markstrom in [[Ma04]][38] has shown that any cubic counterexample to this conjecture must have at least 30 vertices.
(ii) Nowbandegani and H. Esfandiari in [[NoEs11]][39] has shown that any bipartite counterexample must have at least 32 vertices.
(iii) Nowbandegani, H. Esfandiari, M. H. S. Haghighi and K. Bibak in [[NEHB14]][40] has shown that any cubic claw-free counterexample must have 114 vertices and every claw-free graph with minimum degree at least 3 has a cycle whose length is $2^k$ or $3\times2^k$, for some positive integer $k$.
(iv) A. Carr in [[Ca26b]][41] has shown that in any minimal counterexample, every vertex is adjacent to a vertex of degree exactly $3$, and at least $4/7$ of its vertices have degree exactly $3$.

[Sh98]: S. E. Shauger, Results on the Erd˝os-Gy´arf´as conjecture in K1,m-free graphs, Congr. Numer. 134 (1998) 61-65.
[DaSh01]: D. Daniel, S. E. Shauger, A result on the Erd˝os-Gy´arf´as conjecture in planar graphs, Congr. vol. 153 (2001) 129-139
[HeKr13]: C. C. Heckman, R. Krakovski, Erd˝os-Gy´arf´as conjecture for cubic planar graphs, Electron. J. Comb. 20(2) (2013) 7-43.

(The site has been updated to address this comment.)

**[Alfaiz][42]**— [19:00 on 06 Dec 2025][43]

👍 1 📝 1 🤖 0

**All comments are the responsibility of the user. Comments appearing on this page are not verified for correctness. Please keep posts mathematical and on topic.**

[Log in][44] to add a comment.

[Back to the forum][45]


## Links

[1]: /
[2]: /forum
[3]: /dm
[4]: /favourites
[5]: /tags
[6]: /faq
[7]: /prizes
[8]: /lists
[9]: /definitions
[10]: /links
[11]: /random_solved
[12]: /random_open
[13]: /64
[14]: /tags/graph theory
[15]: /tags/cycles
[16]: https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/PowerOfTwoCycles.html
[17]: /latex/64
[18]: /history/64
[19]: https://github.com/teorth/erdosproblems
[20]: https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/64.lean
[21]: /forum/discuss/64
[22]: /forum/thread/64/proof-claims
[23]: /forum/user/Fedir
[24]: /forum/user/Chillguy
[25]: /forum/user/Sam_Petkov
[26]: /forum/user/mattryanwatts
[27]: /forum/user/ZackaryLoevseth
[28]: /forum/user/RajveerKapoor
[29]: /forum/thread/64?order=oldest
[30]: /forum/thread/64?order=newest
[31]: /forum/user/jul059
[32]: /forum/thread/64#post-8130
[33]: https://link.springer.com/article/10.1007/s00010-017-0518-3
[34]: http://elib.mi.sanu.ac.rs/files/journals/mv/282/mvn282p37-42.pdf
[35]: https://arxiv.org/pdf/2109.01277
[36]: https://arxiv.org/pdf/2308.05675
[37]: https://arxiv.org/pdf/2508.19302
[38]: http://abel.math.umu.se/~klasm/Uppsatser/cycex.pdf
[39]: https://www.researchgate.net/publication/312286036_An_Experimental_Result_on_the_Erdos-Gyarfas_Conjecture_in_Bipartite_Graphs
[40]: https://arxiv.org/pdf/1109.5398
[41]: https://arxiv.org/pdf/2605.22844
[42]: /forum/user/Alfaiz
[43]: /forum/thread/64#post-2069
[44]: /forum/login?next=%2Fforum%2Fthread%2F64
[45]: /forum/
