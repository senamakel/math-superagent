<!-- source: https://www.erdosproblems.com/849 | converted from HTML -->

849 | Erdős Problems

[image: Logo] [1]

[Forum][2] [Inbox][3] [Favourites][4] [Tags][5]

More

[FAQ][6] [Prizes][7] [Problem Lists][8] [Definitions][9] [Links][10]

[Forum][2]

Menu

[Inbox][3] [Favourites][4] [Tags][5] [FAQ][6] [Prizes][7] [Problem Lists][8] [Definitions][9] [Links][10]

Dual View [Random Solved][11] [Random Open][12]

OPEN This is open, and cannot be resolved with a finite computation.

Is it true that, for every integer $t\geq 1$, there is some integer $a$ such that\[\binom{n}{k}=a\](with $1\leq k\leq n/2$) has exactly $t$ solutions?

[#849][13]: [Er96b]

[number theory][14] | [binomial coefficients][15]

The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.

Comment activity that has not yet been incorporated into the remarks

None Partial Solution

There are no solutions, partial or complete, claimed in the comments.

-->

Erdős [Er96b] credits this to himself and Gordon 'many years ago', but it is more commonly known as [Singmaster's conjecture][16]. For $t=3$ one could take $a=120$, and for $t=4$ one could take $a=3003$. There are no known examples for $t\geq 5$.

Both Erdős and Singmaster believed the answer to this question is no, and in fact that there exists an absolute upper bound on the number of solutions.

Matomäki, Radziwill, Shao, Tao, and Teräväinen [MRSTT22] have proved that there are always at most two solutions if we restrict $k$ to\[k\geq \exp((\log n)^{2/3+\epsilon}),\]assuming $a$ is sufficiently large depending on $\epsilon>0$.

[View the LaTeX source][17]

[View history][18]

External data from [the database][19] - you can help update this
Formalised statement? [Yes][20]
Related OEIS sequences: [A003016][21] [A003015][22] [A059233][23] [A098565][24] [A090162][25] [A180058][26] [A182237][27]

[0 comments on this problem][28]

[0 claimed proofs for this problem][29]

**Likes this problem** | None  |

**Interested in collaborating** | None  |

**Currently working on this problem** | None  |

**This problem looks difficult** | None  |

**This problem looks tractable** | None  |

**The results on this problem could be formalisable** | None  |

**I am working on formalising the results on this problem** | None  |

When referring to this problem, please use the original sources of Erdős. If you wish to acknowledge this website, the recommended citation format is:

T. F. Bloom, Erdős Problem #849, https://www.erdosproblems.com/849, accessed 2026-08-13

[Previous][30]

[Next][31]


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
[13]: /849
[14]: /tags/number theory
[15]: /tags/binomial coefficients
[16]: https://en.wikipedia.org/wiki/Singmaster%27s_conjecture
[17]: /latex/849
[18]: /history/849
[19]: https://github.com/teorth/erdosproblems
[20]: https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/849.lean
[21]: https://oeis.org/A003016
[22]: https://oeis.org/A003015
[23]: https://oeis.org/A059233
[24]: https://oeis.org/A098565
[25]: https://oeis.org/A090162
[26]: https://oeis.org/A180058
[27]: https://oeis.org/A182237
[28]: /forum/discuss/849
[29]: /forum/thread/849/proof-claims
[30]: /848
[31]: /850
