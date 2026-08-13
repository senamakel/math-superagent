<!-- source: https://www.erdosproblems.com/242 | converted from HTML -->

242 | Erdős Problems

[image: Logo] [1]

[Forum][2] [Inbox][3] [Favourites][4] [Tags][5]

More

[FAQ][6] [Prizes][7] [Problem Lists][8] [Definitions][9] [Links][10]

[Forum][2]

Menu

[Inbox][3] [Favourites][4] [Tags][5] [FAQ][6] [Prizes][7] [Problem Lists][8] [Definitions][9] [Links][10]

Dual View [Random Solved][11] [Random Open][12]

FALSIFIABLE Open, but could be disproved with a finite counterexample.

For every $n>2$ there exist distinct integers $1\leq x<y<z$ such that\[\frac{4}{n} = \frac{1}{x}+\frac{1}{y}+\frac{1}{z}.\]

[#242][13]: [Er50c] [Er61] [Er79] [ErGr80] [Va99,1.13]

[number theory][14] | [unit fractions][15]

The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.

Comment activity that has not yet been incorporated into the remarks

None Partial Solution

There are no solutions, partial or complete, claimed in the comments.

-->

The [Erdős-Straus conjecture][16]. Perhaps the first place it appears in the literature is in a paper of Obláth [Ob50] (submitted in 1948), which describes it as a conjecture of Erdős.

The existence of a representation of $4/n$ as the sum of at most four distinct unit fractions follows trivially from a greedy algorithm.

Schinzel conjectured (see [Si56]) the generalisation that, for any fixed $a$, if $n$ is sufficiently large in terms of $a$ then there exist distinct integers $1\leq x<y<z$ such that\[\frac{a}{n} = \frac{1}{x}+\frac{1}{y}+\frac{1}{z}.\]When $a=5$ this conjecture is due to Sierpiński [Si56]. For more background and results on this generalisation see Pomerance and Weingartner [PoWe25].

It suffices to prove this when $n$ is prime. This has been verified for all $n\leq 10^{18}$ [MiDu25].

There are many partial results, some of which are listed below.

- Obláth [Ob50] noted it is true if $n+1$ is divisible by a prime $\equiv 3\pmod{4}$. This implies almost all $n$ have the required decomposition.
- Arguing via parametric solutions, Mordell [Mo69] proved it is true for all $n$ except those congruent to one of $\{1,121,169,289,361,529\}$ modulo $840$.
- Terzi [Te71] extended this to prove that it is true for all $n$ except those congruent to one of $198$ possible bad congruences modulo $120120$.
- Vaughan [Va70] proved that the number of exceptions in $[1,x]$ is\[\leq x \exp(-c(\log x)^{2/3})\]for some constant $c>0$.
- This conjecture is equivalent (see Theorem 1 of [BlEl22]) to the statement that, for any prime $p$, there exist integers $a,c,d\geq 1$ such that either $p\equiv -a/c\pmod{4acd-1}$ or $p\equiv -\frac{4c^2d+1}{k}\pmod{4cd}$ for some $k\mid 4c^2d+1$.
- Bright and Loughran [BrLo20] have shown there is no Brauer-Manin obstruction to the existence of solutions.
- If $f(n)$ counts the number of solutions then Elsholtz and Tao [ElTa13] have proved\[\sum_{p\leq N}f(p)=N(\log N)^{2+o(1)}\]and $f(p)\leq p^{3/5+o(1)}$ for all primes $p$.
- Elsholtz and Planitzer [ElPl20] have proved that for almost all $n$\[f(n) \geq (\log n)^{\log 6+o(1)}.\]

[View the LaTeX source][17]

This page was last edited 07 May 2026. [View history][18]

External data from [the database][19] - you can help update this
Formalised statement? [Yes][20]
Related OEIS sequences: [A073101][21] [A075245][22] [A075246][23] [A075247][24] [A075248][25] [A287116][26]

[18 comments on this problem][27]

[0 claimed proofs for this problem][28]

**Likes this problem** | [old-bielefelder][29], [jgold][30], [TFBloom][31], [jbbaehr22][32], [Dogmachine][33], [ArdaErgun][34] |

**Interested in collaborating** | [jgold][30], [Bradford][35], [auro][36] |

**Currently working on this problem** | [jgold][30], [alansbor][37], [Bradford][35], [auro][36], [mosesluajh][38] |

**This problem looks difficult** | [Vjeko_Kovac][39], [TFBloom][31], [TerenceTao][40] |

**This problem looks tractable** | [auro][36], [jbbaehr22][32] |

**The results on this problem could be formalisable** | [jbbaehr22][32] |

**I am working on formalising the results on this problem** | [jbbaehr22][32], [auro][36] |

**Additional thanks to**: Alfaiz and Bryce Orloski

When referring to this problem, please use the original sources of Erdős. If you wish to acknowledge this website, the recommended citation format is:

T. F. Bloom, Erdős Problem #242, https://www.erdosproblems.com/242, accessed 2026-08-13

[Previous][41]

[Next][42]


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
[13]: /242
[14]: /tags/number theory
[15]: /tags/unit fractions
[16]: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture
[17]: /latex/242
[18]: /history/242
[19]: https://github.com/teorth/erdosproblems
[20]: https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/242.lean
[21]: https://oeis.org/A073101
[22]: https://oeis.org/A075245
[23]: https://oeis.org/A075246
[24]: https://oeis.org/A075247
[25]: https://oeis.org/A075248
[26]: https://oeis.org/A287116
[27]: /forum/discuss/242
[28]: /forum/thread/242/proof-claims
[29]: /forum/user/old-bielefelder
[30]: /forum/user/jgold
[31]: /forum/user/TFBloom
[32]: /forum/user/jbbaehr22
[33]: /forum/user/Dogmachine
[34]: /forum/user/ArdaErgun
[35]: /forum/user/Bradford
[36]: /forum/user/auro
[37]: /forum/user/alansbor
[38]: /forum/user/mosesluajh
[39]: /forum/user/Vjeko_Kovac
[40]: /forum/user/TerenceTao
[41]: /241
[42]: /243
