> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/erdos-problems-64.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.erdosproblems.com/64 | converted from HTML -->

64 | Erdős Problems

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

T. F. Bloom, Erdős Problem #64, https://www.erdosproblems.com/64, accessed 2026-08-12

[Previous][29]

[Next][30]


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

*[excerpt ends; 119 characters not shown — see `research/sources/erdos-problems-64.full.md`]*
