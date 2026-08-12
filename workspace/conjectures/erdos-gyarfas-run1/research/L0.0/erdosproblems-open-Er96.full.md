<!-- source: https://www.erdosproblems.com/search_bib/Er96/open | converted from HTML -->

Erdős Problems

[image: Logo] [1]

[Forum][2] [Inbox][3] [Favourites][4] [Tags][5]

More

[FAQ][6] [Prizes][7] [Problem Lists][8] [Definitions][9] [Links][10]

[Forum][2]

Menu

[Inbox][3] [Favourites][4] [Tags][5] [FAQ][6] [Prizes][7] [Problem Lists][8] [Definitions][9] [Links][10]

Dual View [Random Solved][11] [Random Open][12]

0 solved out of 6 shown (show only [solved][13] or [open][13] or [formalised][13] or [unformalised][13])

FALSIFIABLE Open, but could be disproved with a finite counterexample. - $1000

Does every finite graph with minimum degree at least 3 contain a cycle of length $2^k$ for some $k\geq 2$?

[#64][14]: [Er93,p.343] [Er94b] [Er95,p.174] [Er96] [Er97b] [Er97c]

[graph theory][15] | [cycles][16]

The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.

Comment activity that has not yet been incorporated into the remarks

None Partial Solution

There are no solutions, partial or complete, claimed in the comments.

-->

Conjectured by Erdős and Gyárfás, who believed the answer must be negative, and in fact for every $r$ there must be a graph of minimum degree at least $r$ without a cycle of length $2^k$ for any $k\geq 2$.

This was solved in the affirmative if the minimum degree is larger than some absolute constant by Liu and Montgomery [LiMo20] (therefore disproving the above stronger conjecture of Erdős and Gyárfás). Liu and Montgomery prove a much stronger result: if the average degree of $G$ is sufficiently large then there is some large integer $\ell$ such that for every even integer $m\in [(\log \ell)^8,\ell]$, $G$ contains a cycle of length $m$.

An infinite tree with minimum degree $3$ shows that the answer is trivially false for infinite graphs.

The conjecture has been confirmed for various families of graphs; see the comment by Alfaiz for a list.

This problem is [#69 in Extremal Graph Theory][17] in the graphs problem collection.

[View the LaTeX source][18]

This page was last edited 10 April 2026. [View history][19]

External data from [the database][20] - you can help update this
Formalised statement? [Yes][21]

[1 comment on this problem][22]

[0 claimed proofs for this problem][23]

**Likes this problem** | [Fedir][24], [Chillguy][25], [Sam_Petkov][26], [mattryanwatts][27] |

**Interested in collaborating** | [Sam_Petkov][26] |

**Currently working on this problem** | [Chillguy][25], [Sam_Petkov][26], [mattryanwatts][27] |

**This problem looks difficult** | None  |

**This problem looks tractable** | [Chillguy][25] |

**The results on this problem could be formalisable** | [Chillguy][25] |

**I am working on formalising the results on this problem** | [Chillguy][25] |

**Additional thanks to**: Alfaiz, Desmond Weisenberg, and Yuval Wigderson

When referring to this problem, please use the original sources of Erdős. If you wish to acknowledge this website, the recommended citation format is:

T. F. Bloom, Erdős Problem #64, https://www.erdosproblems.com/64, accessed 2026-07-26

OPEN This is open, and cannot be resolved with a finite computation. - $500

Let $f(n)\to \infty$ (possibly very slowly). Is there a graph of infinite chromatic number such that every finite subgraph on $n$ vertices can be made bipartite by deleting at most $f(n)$ edges?

[#74][28]: [EHS82] [Er87] [Er90] [Er93,p.342] [Er94b] [Er95] [Er95d,p.62] [Er96] [Er97b] [Er97c] [Er97d] [Er97f]

[graph theory][15] | [chromatic number][29] | [cycles][16]

The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.

Comment activity that has not yet been incorporated into the remarks

None Partial Solution

There are no solutions, partial or complete, claimed in the comments.

-->

Conjectured by Erdős, Hajnal, and Szemerédi [EHS82].

Rödl [Ro82] has proved this for hypergraphs, and also proved there is such a graph (with chromatic number $\aleph_0$) if $f(n)=\epsilon n$ for any fixed constant $\epsilon>0$.

It is open even for $f(n)=\sqrt{n}$. Erdős offered \$500 for a proof but only \$250 for a counterexample. This fails (even with $f(n)\gg n$) if the graph has chromatic number $\aleph_1$ (see [[111]][30]).

The analogous question with vertices instead of edges is true, and was proved by GPT 5.5 Pro (prompted by Chojecki) - see [[750]][31].

[View the LaTeX source][32]

This page was last edited 16 July 2026. [View history][33]

External data from [the database][20] - you can help update this
Formalised statement? [Yes][34]

[0 comments on this problem][35]

[0 claimed proofs for this problem][36]

**Likes this problem** | [SkyYang][37], [Sam_Petkov][26] |

**Interested in collaborating** | [Sam_Petkov][26] |

**Currently working on this problem** | [SkyYang][37], [RealBelgian][38], [Sam_Petkov][26] |

**This problem looks difficult** | [SkyYang][37] |

**This problem looks tractable** | None  |

**The results on this problem could be formalisable** | None  |

**I am working on formalising the results on this problem** | None  |

When referring to this problem, please use the original sources of Erdős. If you wish to acknowledge this website, the recommended citation format is:

T. F. Bloom, Erdős Problem #74, https://www.erdosproblems.com/74, accessed 2026-07-26

OPEN This is open, and cannot be resolved with a finite computation.

The cycle set of a graph $G$ on $n$ vertices is a set $A\subseteq \{3,\ldots,n\}$ such that there is a cycle in $G$ of length $\ell$ if and only if $\ell \in A$. Let $f(n)$ count the number of possible such $A$.

Prove that $f(n)=o(2^n)$.

Prove that $f(n)/2^{n/2}\to \infty$.

[#84][39]: [Er94b] [Er95] [Er96] [Er97d]

[graph theory][15] | [cycles][16]

The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.

Comment activity that has not yet been incorporated into the remarks

None Partial Solution

There are no solutions, partial or complete, claimed in the comments.

-->

Conjectured by Erdős and Faudree, who showed that $2^{n/2}<f(n) \leq 2^{n-2}$. The first problem was solved by Verstraëte [Ve04], who proved\[f(n)\ll 2^{n-n^{1/10}}.\]This was improved by Nenadov [Ne25] to\[f(n) \ll 2^{n-n^{1/2-o(1)}}.\]One can also ask about the existence and value of $\lim f(n)^{1/n}$.

[View the LaTeX source][40]

[View history][41]

External data from [the database][20] - you can help update this
Formalised statement? No ( [Create a formalisation here][42])
Related OEIS sequences: Possible

[0 comments on this problem][43]

[0 claimed proofs for this problem][44]

**Likes this problem** | None  |

**Interested in collaborating** | None  |

**Currently working on this problem** | None  |

**This problem looks difficult** | None  |

**This problem looks tractable** | None  |

**The results on this problem could be formalisable** | None  |

**I am working on formalising the results on this problem** | None  |

**Additional thanks to**: Tuan Tran

When referring to this problem, please use the original sources of Erdős. If you wish to acknowledge this website, the recommended citation format is:

T. F. Bloom, Erdős Problem #84, https://www.erdosproblems.com/84, accessed 2026-07-26

OPEN This is open, and cannot be resolved with a finite computation.

Let $n\geq 4$ and $f(n)$ be minimal such that every graph on $n$ vertices with minimal degree $\geq f(n)$ contains a $C_4$. Is it true that, for all large $n$, $f(n+1)\geq f(n)$?

[#85][45]: [Er93,p.345] [Er94b] [Er95] [Er96]

[graph theory][15] | [ramsey theory][46]

The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.

Comment activity that has not yet been incorporated into the remarks

None Partial Solution

There are no solutions, partial or complete, claimed in the comments.

-->

The function $f(n)$ is a reformulation of the Ramsey number $R(C_4,K_{1,n})$, in that\[R(C_4,K_{1,n})=\min\{ m : f(m)\leq m-n\}\]and\[f(n)=\min\{ m : m\geq R(C_4, K_{1,n-m})\}.\]The behaviour of this Ramsey number more generally is [[552]][47].

A weaker version of the conjecture asks for some constant $c$ such that $f(m)>f(n)-c$ for all $m>n$. This question can be asked for other graphs than $C_4$.

The bounds in [[552]][47] imply in particular that $f(n)<\sqrt{n}+1$ and\[f(n)=(1+o(1))\sqrt{n}.\]It is easy to check that $f(4)=2$.

[View the LaTeX source][48]

This page was last edited 06 December 2025. [View history][49]

External data from [the database][20] - you can help update this
Formalised statement? [Yes][50]
Related OEIS sequences: [A006672][51] possible

[1 comment on this problem][52]

[0 claimed proofs for this problem][53]

**Likes this problem** | None  |

**Interested in collaborating** | None  |

**Currently working on this problem** | None  |

**This problem looks difficult** | None  |

**This problem looks tractable** | None  |

**The results on this problem could be formalisable** | None  |

**I am working on formalising the results on this problem** | None  |

**Additional thanks to**: Boris Alexeev

When referring to this problem, please use the original sources of Erdős. If you wish to acknowledge this website, the recommended citation format is:

T. F. Bloom, Erdős Problem #85, https://www.erdosproblems.com/85, accessed 2026-07-26

OPEN This is open, and cannot be resolved with a finite computation. - $100

Determine the Ramsey number\[R(C_4,S_n),\]where $S_n=K_{1,n}$ is the star on $n+1$ vertices.

In particular, is it true that, for any $c>0$, there are infinitely many $n$ such that\[R(C_4,S_n)\leq n+\sqrt{n}-c?\]

[#552][47]: [BEFRS89] [Er93,p.345] [Er94b] [Er95] [Er96]

[graph theory][15] | [ramsey theory][46]

The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.

Comment activity that has not yet been incorporated into the remarks

None Partial Solution

There are no solutions, partial or complete, claimed in the comments.

-->

A problem of Burr, Erdős, Faudree, Rousseau, and Schelp [BEFRS89]. Erdős often asked about $R(C_4,S_n)$ in the equivalent formulation of asking for a bound on the minimum degree of a graph which would guarantee the existence of a $C_4$ (see [[85]][45]).

It is known that\[ n+\sqrt{n}-6n^{11/40} \leq R(C_4,S_n)\leq n+\lceil\sqrt{n}\rceil+1.\]The lower bound is due to [BEFRS89], the upper bound is due to Parsons [Pa75]. The lower bound of [BEFRS89] is related to gaps between primes, and assuming e.g. Cramer's conjecture on gaps between primes their lower bound would be $n+\sqrt{n}-n^{o(1)}$.

Erdős offered \$100 for a proof or disproof of the second question in [BEFRS89]. In [Er96] Erdős asks (an equivalent formulation of) whether $R(C_4,S_n)\geq n+\sqrt{n}-O(1)$, but says this is probably 'too optimistic'.

They also ask, if $f(n)=R(C_4,S_n)$, whether $f(n+1)=f(n)$ infinitely often, and is the density of such $n$ $0$? Also, is it true that $f(n+1)\leq f(n)+2$ for all $n$? A similar question about an equivalent function is the subject of [[85]][45].

Parsons [Pa75] proved that\[R(C_4,S_n)=n+\lceil\sqrt{n}\rceil\]whenever $n=q^2+1$ for a prime power $q$ and\[R(C_4,S_n)=n+\lceil\sqrt{n}\rceil+1\]whenever $n=q^2$ for a prime power $q$ (in particular both equalities occur infinitely often).

This has been extended in various works, all in the cases $n=q^2\pm t$ for some $0\leq t\leq q$ and prime power $q$. We refer to the work of Parsons [Pa75], Wu, Sun, Zhang, and Radziszowski [WSZR15], and Zhang, Chen, and Cheng ( [ZCC17] and [ZCC17b]) for a precise description. In every known case\[R(C_4,S_n)=n+\lceil\sqrt{n}\rceil+\{0,1\},\]and Zhang, Chen, and Cheng [ZCC17] speculate whether this is in fact true for all $n\geq 2$ (whence the answer to the question above would be no).

This problem is [#19 in Ramsey Theory][54] in the graphs problem collection.

[View the LaTeX source][55]

This page was last edited 01 February 2026. [View history][56]

External data from [the database][20] - you can help update this
Formalised statement? No ( [Create a formalisation here][42])
Related OEIS sequences: [A006672][51]

[1 comment on this problem][57]

[0 claimed proofs for this problem][58]

**Likes this problem** | None  |

**Interested in collaborating** | None  |

**Currently working on this problem** | None  |

**This problem looks difficult** | None  |

**This problem looks tractable** | None  |

**The results on this problem could be formalisable** | None  |

**I am working on formalising the results on this problem** | None  |

**Additional thanks to**: Stijn Cambie

When referring to this problem, please use the original sources of Erdős. If you wish to acknowledge this website, the recommended citation format is:

T. F. Bloom, Erdős Problem #552, https://www.erdosproblems.com/552, accessed 2026-07-26

OPEN This is open, and cannot be resolved with a finite computation.

Suppose $n\equiv 1\pmod{m}$. We say that an edge-colouring of $K_n$ using $m$ colours is balanced if every vertex sees exactly $\lfloor n/m\rfloor$ many edges of each colours.

For which graphs $G$ is it true that, if $m=e(G)$, for all large $n\equiv 1\pmod{m}$, every balanced edge-colouring of $K_n$ with $m$ colours contains a rainbow copy of $G$? (That is, a subgraph isomorphic to $G$ where each edge receives a different colour.)

[#811][59]: [Er91] [Er93,p.346] [ErTu93] [Er96]

[graph theory][15] | [ramsey theory][46]

The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.

Comment activity that has not yet been incorporated into the remarks

None Partial Solution

There are no solutions, partial or complete, claimed in the comments.

-->

In [Er91] Erdős credits this problem to himself, Pyber, and Tuza. This problem was explored in a paper of Erdős and Tuza [ErTu93]. In [Er96] Erdős seems to suggest that this might be true for every graph $G$, and specifically asks specific challenge posed in [Er91] and [Er96] is whether, in any balanced edge-colouring of $K_{6n+1}$ by $6$ colours there must exist a rainbow $C_6$ and $K_4$.

In general, one can ask for a quantitative version, defining $d_G(n)$ to be minimal (if it exists) such that if $n$ is sufficiently large and the edges of $K_n$ are coloured with $e(G)$ many colours such that the minimum degree of each colour class is $\geq d_G(n)$ then there is a rainbow copy of $G$. Erdős and Tuza [ErTu93] proved that\[\lfloor n/6\rfloor \leq d_{C_4}(n) \leq \left(\frac{1}{4}-c\right)n\]for some constant $c>0$.

Axenovich and Clemen [AxCl24] have proved that there exist infinitely many graphs without this property. In particular, they show that for any odd $\ell \geq 3$ and $m=\lfloor \sqrt{\ell}+3.5\rfloor$ there exist arbitrarily large $n$ such that $K_n$ has a balanced edge-colouring using $\ell$ colours which contains no rainbow $K_m$. They conjecture that $K_m$ lacks this property for all $m\geq 4$.

Clemen and Wagner [ClWa23] proved that $K_4$ does lack this property.

[View the LaTeX source][60]

This page was last edited 14 October 2025. [View history][61]

External data from [the database][20] - you can help update this
Formalised statement? No ( [Create a formalisation here][42])
Related OEIS sequences: Possible

[1 comment on this problem][62]

[0 claimed proofs for this problem][63]

**Likes this problem** | None  |

**Interested in collaborating** | None  |

**Currently working on this problem** | None  |

**This problem looks difficult** | None  |

**This problem looks tractable** | None  |

**The results on this problem could be formalisable** | None  |

**I am working on formalising the results on this problem** | None  |

**Additional thanks to**: msellke

When referring to this problem, please use the original sources of Erdős. If you wish to acknowledge this website, the recommended citation format is:

T. F. Bloom, Erdős Problem #811, https://www.erdosproblems.com/811, accessed 2026-07-26


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
[13]: 
[14]: /64
[15]: /tags/graph theory
[16]: /tags/cycles
[17]: https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/PowerOfTwoCycles.html
[18]: /latex/64
[19]: /history/64
[20]: https://github.com/teorth/erdosproblems
[21]: https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/64.lean
[22]: /forum/discuss/64
[23]: /forum/thread/64/proof-claims
[24]: /forum/user/Fedir
[25]: /forum/user/Chillguy
[26]: /forum/user/Sam_Petkov
[27]: /forum/user/mattryanwatts
[28]: /74
[29]: /tags/chromatic number
[30]: /111
[31]: /750
[32]: /latex/74
[33]: /history/74
[34]: https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/74.lean
[35]: /forum/discuss/74
[36]: /forum/thread/74/proof-claims
[37]: /forum/user/SkyYang
[38]: /forum/user/RealBelgian
[39]: /84
[40]: /latex/84
[41]: /history/84
[42]: https://github.com/google-deepmind/formal-conjectures
[43]: /forum/discuss/84
[44]: /forum/thread/84/proof-claims
[45]: /85
[46]: /tags/ramsey theory
[47]: /552
[48]: /latex/85
[49]: /history/85
[50]: https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/85.lean
[51]: https://oeis.org/A006672
[52]: /forum/discuss/85
[53]: /forum/thread/85/proof-claims
[54]: https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/RamseyCkStar.html
[55]: /latex/552
[56]: /history/552
[57]: /forum/discuss/552
[58]: /forum/thread/552/proof-claims
[59]: /811
[60]: /latex/811
[61]: /history/811
[62]: /forum/discuss/811
[63]: /forum/thread/811/proof-claims
