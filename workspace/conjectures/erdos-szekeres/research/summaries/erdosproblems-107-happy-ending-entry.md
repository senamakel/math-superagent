> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/erdosproblems-107-happy-ending-entry.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.erdosproblems.com/107 | converted from HTML -->

107 | Erdős Problems

[image: Logo] [1]

[Forum][2] [Inbox][3] [Favourites][4] [Tags][5]

More

[FAQ][6] [Prizes][7] [Problem Lists][8] [Definitions][9] [Links][10]

[Forum][2]

Menu

[Inbox][3] [Favourites][4] [Tags][5] [FAQ][6] [Prizes][7] [Problem Lists][8] [Definitions][9] [Links][10]

Dual View [Random Solved][11] [Random Open][12]

FALSIFIABLE Open, but could be disproved with a finite counterexample. - $500

Let $f(n)$ be minimal such that any $f(n)$ points in $\mathbb{R}^2$, no three on a line, contain $n$ points which form the vertices of a convex $n$-gon. Prove that $f(n)=2^{n-2}+1$.

[#107][13]: [Er61,p.245] [Er75f,p.106] [Er81] [Er82e] [Er83c] [Er95,p.184] [Er97c] [Er97e] [Va99,4.66]

[geometry][14] | [convex][15]

The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.

Comment activity that has not yet been incorporated into the remarks

None Partial Solution

There are no solutions, partial or complete, claimed in the comments.

-->

The Erdős-Klein-Szekeres 'Happy Ending' problem. The problem originated in 1931 when Klein observed that $f(4)=5$. Turán and Makai showed $f(5)=9$. Erdős and Szekeres proved the bounds\[2^{n-2}+1\leq f(n)\leq \binom{2n-4}{n-2}+1.\]( [ErSz60] and [ErSz35] respectively). There were several improvements of the upper bound, but all of the form $4^{(1+o(1))n}$, until Suk [Su17] proved\[f(n) \leq 2^{(1+o(1))n}.\]The current best bound is due to Holmsen, Mojarrad, Pach, and Tardos [HMPT20], who prove\[f(n) \leq 2^{n+O(\sqrt{n\log n})}.\]In [Er97e] Erdős clarifies that the \$500 is for a proof, and only offers \$100 for a disproof. Graham [Gr04] offers \$1000 for a proof.

This problem is [#1 in Ramsey Theory][16] in the graphs problem collection.

See also [[216]][17], [[651]][18], and [[838]][19].

[View the LaTeX source][20]

This page was last edited 11 April 2026. [View history][21]

External data from [the database][22] - you can help update this
Formalised statement? [Yes][23]
Related OEIS sequences: [A000051][24]

[2 comments on this problem][25]

[0 claimed proofs for this problem][26]

**Likes this problem** | [JineonBaek][27], [old-bielefelder][28], [jnie][29], [Dogmachine][30], [Sam_Petkov][31] |

**Interested in collaborating** | [Sam_Petkov][31] |

**Currently working on this problem** | None  |

**This problem looks difficult** | [JineonBaek][27] |

**This problem looks tractable** | None  |

**The results on this problem could be formalisable** | None  |

**I am working on formalising the results on this problem** | None  |

**Additional thanks to**: Casey Tompkins and Wouter van Doorn

When referring to this problem, please use the original sources of Erdős. If you wish to acknowledge this website, the recommended citation format is:

T. F. Bloom, Erdős Problem #107, https://www.erdosproblems.com/107, accessed 2026-08-16

[Previous][32]

[Next][33]


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
[13]: /107
[14]: /tags/geometry
[15]: /tags/convex
[16]: https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/Convex.html
[17]: /216
[18]: /651
[19]: /838
[20]: /latex/107
[21]: /history/107
[22]: https://github.com/teorth/erdosproblems
[23]: https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/107.lean
[24]: https://oeis.org/A000051
[25]: /forum/discuss/107
[26]: /forum/thread/107/proof-claims
[27]: /forum/user/JineonBaek
[28]: /forum/user/old-bielefelder
[29]: /forum/user/jnie

*[excerpt ends; 81 characters not shown — see `research/sources/erdosproblems-107-happy-ending-entry.full.md`]*
