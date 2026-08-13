<!-- source: https://www.erdosproblems.com/forum/discuss/242 | converted from HTML -->

242 Discussion Thread | Erdős Problems

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

Order by [oldest first][41] or [newest first][42]. (The most recent comments are highlighted in a red border.)

-

A solution to this conjecture has been "claimed" by K. Bradford in his latest preprint [[Br26]][43].

**[Alfaiz][44]**— [04:33 on 13 Feb 2026][45]

👍 0 📝 0 🤖 0

  -

The final sentence on the covering system seems to hint it is incorrect/ incomplete.
Taking the first primes modulo different moduli doesnt create a covering system.

In particular, none of the 6 remaining residues modulo 840 by Mordell are excluded here.

**[StijnC][46]**— [06:36 on 13 Feb 2026][47]

👍 2 📝 0 🤖 0

  -

While not *quite* as notorious as [[1135][48]], this problem also regularly attracts a large number of low-quality solution attempts. I would not give too much attention to any new preprints on this problem unless either (a) the result has been accepted for publication in a reputable journal, (b) the author has an existing track record of reputable publications in the general area of diophantine equations or analytic number theory, (c) only realistic partial results are claimed, (d) an expert is willing to vouch for the correctness (or at least plausibility) of the results, or (e) the result has been properly formalized.

EDIT: For what it is worth, [here is the ChatGPT Pro critique][49] of this latest attempt.

**[TerenceTao][40]**— [06:46 on 13 Feb 2026][50]

👍 2 📝 0 🤖 0

-

Perhaps It is easier to prove that solutions exist for almost all prime denominators?

**[Dogmachine][33]**— [14:31 on 01 Feb 2026][51]

👍 1 📝 0 🤖 0

  -

This is true, and follows e.g. from Vaughan's (much stronger) almost all result listed in the remarks.

**[Thomas Bloom][31]**— [15:33 on 01 Feb 2026][52]

👍 0 📝 0 🤖 0

-

I've been formalizing Erdős-Straus in Lean, 531 formalized items, 484 complete, hope it might be of use to one of you to finish this off: https://github.com/leochlon/erdstrau

Sorry-free lean4 proofs including: ES for $n = 420k + r$ with $k$ odd, $r \in \{121, 169, 289, 361\}$; all $n \equiv 529 \pmod{840}$ via CRT (174 declarations, witnesses like $(133, 23460, 71764140)$ for $n=529$); 348/420 coverage; 20 conditional certificates for $n \equiv 1 \pmod{840}$ (reducing to divisor conditions); and a formal refutation of one proposed ED2 covering scheme.

Showed the full conjecture reduces to one construction: given $q \equiv 3 \pmod 4$ and $s^2 + p = qk$, find $\delta, b, c$ with $(4b-1)(4c-1) = 4p\delta + 1$ and $\delta \mid bc$. Setting $b = (q+1)/4$ works for small $q$; general case open.

**[leonchlon][53]**— [20:26 on 27 Jan 2026][54]

👍 0 📝 0 🤖 0

  -

For the reduction at the end;
Could you add a few quantifiers to have a clear remaining goal?

We need to prove it for every k, or for one value of k of a particular parity?
There is a constraint on $s$?
(Or $p$ is just minus a quadratic residue mod $q$?)

**[StijnC][46]**— [06:32 on 29 Jan 2026][55]

👍 0 📝 0 🤖 0

  -

See the remarks for some well-known parametric solutions (which I assume your formalisation is using). In particular it's not too hard to prove via elementary methods that this conjecture follows from (and is in fact equivalent to) the statement that for any prime $p$, there exist integers $a,c,d\geq 1$ such that either $p\equiv -a/c\pmod{4acd-1}$ or $p\equiv -\frac{4c^2d+1}{k}\pmod{4cd}$ for some $k\mid 4c^2d+1$. This might be nice, and not too hard, to formalise, see Theorem 1 of [BlEl22] for a proof of the equivalence.

Using this you can prove the conjecture for many congruence classes, and can efficiently check it's true for all small primes $p$. One can certainly refine Mordell's modulo $840$ conditions for example - this was already done by Terzi in 1971 to a modulo $120120$ condition. I'm sure that by continuing computations one can forever narrow down the congruential conditions, but I don't think this is a viable path to the full conjecture.

**[Thomas Bloom][31]**— [07:28 on 29 Jan 2026][56]

👍 0 📝 0 🤖 0

  -

In case anyone is curious, [this file][57] contains the claimed proof of "Full CRT coverage for n ≡ 529 (mod 840)". I think a quick look at this file is highly informative as to the source and veracity of the claimed results.

**[BorisAlexeev][58]**— [11:59 on 29 Jan 2026][59]

👍 1 📝 0 🤖 0

    -

Aha, thanks for pointing that out Boris. So this isn't actually a proof of anything - it's just verifying the conjecture for a collection of small $n$, and appeals to 'periodicity' to extend this to an infinite congruence class. This does not work, since the statement is obviously not periodic, so I'm not sure what they have in mind here.

I do think, however, that a genuine formalisation of the known congruence classes cases (and/or the equivalence mentioned in my earlier comment) would be valuable, and presumably quite straightforward to do automatically, since this is just messing about with elementary identities.

**[Thomas Bloom][31]**— [12:15 on 29 Jan 2026][60]

👍 1 📝 0 🤖 0

-

[Va70] is unable to load any reference.

(The site has been updated to address this comment.)

**[Alfaiz][44]**— [05:33 on 29 Jan 2026][61]

👍 0 📝 1 🤖 0

-

Mordell in [Mo68] has shown it is true, except possibly in cases where $n$ is prime and congruent to $1^2, 11^2, 13^2, 17^2, 19^2$ or $23^2$ (mod 840)

[Mo68]: Mordell, L. J. Diophantine Equations, pp. 287-290. Academic Press,1968.

(The site has been updated to address this comment.)

**[Alfaiz][44]**— [13:47 on 07 Dec 2025][62]

👍 0 📝 1 🤖 0

-

A [new paper][63] by C. Pomerance and A. Weingartner is the latest paper which deals with this problem. This paper also gives a great account of past improvements/progress on this problem.

(The site has been updated to address this comment.)

**[Alfaiz][44]**— [11:43 on 24 Nov 2025][64]

👍 1 📝 1 🤖 0

-

Li Delang in [his paper][65] has proved that for any given positive integers $N$ and $k$ the number of integers $n<N$ for which the equation $4/n = 1/x + 1/y + 1/z$ is unsolvable in positive integers x, y, z is not greater than $cN/(\log N)^k$, where $c$ is a constant depending only on $k$.

Also previously, Vaughan in [this paper][66] has given the upper bound on the count of possible exceptions as $N/\exp(c(\log N)^{2/3})$ for a positive constant $c$.

(The site has been updated to address this comment.)

**[Alfaiz][44]**— [12:35 on 23 Nov 2025][67]

👍 0 📝 0 🤖 0

-

In the case $a = 4$, the conjecture has been verified for $n<5000$ by Straus, $n<8000$ by Bernstein [here][68], $n<20000$ by Shapiro, $n<106128$ by Oblath in [Ob49], $n<171649$ by Rosati [here][69], $n<400000$ by C. Ko, C. Sun and S. J. Chang in [KoSuCh64], $n<10^7$ by Yamamoto in [Ya65], $n<1.1 \times 10^7$ by Jollensten in [Jo??] and $n \leq 10^{17}$ by Salez [here][70].

[Ob49]: R. Oblath, "Sur l'équation diophantienne $4/n = 1/x_1 + 1/x_2 + 1/x_3$" , Mathesis, 59 (1949), 308-316.
[KoSuCh64]: Chan Ko, Chi Sun, AND S. J. Chang, On equations $4/n = l/x + l/y + l/z$, Acta Sci. Natur. Szechuanensis 2 (1964), 21-35.
[Ya65]: K. Yamamoto, " On the diophantine equation $4/n = 1/x+1/y+1/z$", Mem. Fac. Sci. Kyushu University Ser. A, 19 (1965), 37-47.
[Jo??]: R. M. Jollensten, A note on the Egyption problem, in “Proceedings of the Seventh Southeastern Conference on Combinatorics, Graph Theory and Computing” (F. Hoffman et al., Eds.), pp. 578-589, Winnipeg Utilitas Math. Publ. Inc., Winnipeg.

There is a lot of literature on this conjecture. Surprisingly, I came across a [paper][71] which claims to solve the Erdos-Straus Conjecture. Another [paper][72] claims to be an "almost" complete proof of the Generalized Erdos Straus Conjecture.

I am highly skeptical of both these papers, but professionals can take a look at'em.

**[Alfaiz][44]**— [10:31 on 18 Nov 2025][73]

👍 0 📝 0 🤖 0

  -

Thanks! Yes, this conjecture has attracted quite a few 'proofs' over the years. Of those that I have looked at, none have seemed credible.

**[Thomas Bloom][31]**— [10:52 on 18 Nov 2025][74]

👍 0 📝 0 🤖 0

  -

The paper which claims to solve the Erdos-Straus Conjecture is again very mistaken.
Just had a look at the start of page 2, and it is full of unclear/ false steps.

**[StijnC][46]**— [13:12 on 18 Nov 2025][75]

👍 1 📝 0 🤖 0

-

This question belongs to the class of other first-order questions one might ask about whole numbers. For example, is every integer is the sum of four cubes? In general, they are algorithmically undecidable.

**[Dogmachine][33]**— [18:49 on 09 Aug 2025][76]

👍 0 📝 0 🤖 0

Show 4 more comments

**All comments are the responsibility of the user. Comments appearing on this page are not verified for correctness. Please keep posts mathematical and on topic.**

[Log in][77] to add a comment.

[Back to the forum][78]


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
[41]: /forum/thread/242?order=oldest
[42]: /forum/thread/242?order=newest
[43]: https://arxiv.org/abs/2602.11774
[44]: /forum/user/Alfaiz
[45]: /forum/thread/242#post-4274
[46]: /forum/user/StijnC
[47]: /forum/thread/242#post-4276
[48]: https://www.erdosproblems.com/1135
[49]: https://chatgpt.com/share/698ed01e-2ad4-800e-9986-b121ce41ae76
[50]: /forum/thread/242#post-4277
[51]: /forum/thread/242#post-4034
[52]: /forum/thread/242#post-4037
[53]: /forum/user/leonchlon
[54]: /forum/thread/242#post-3855
[55]: /forum/thread/242#post-3907
[56]: /forum/thread/242#post-3909
[57]: https://github.com/leochlon/erdstrau/blob/5d0f0467ef8a0a87b708b54c40213697ce4d66b6/ESLean/Residues/R529.lean
[58]: /forum/user/BorisAlexeev
[59]: /forum/thread/242#post-3911
[60]: /forum/thread/242#post-3912
[61]: /forum/thread/242#post-3906
[62]: /forum/thread/242#post-2078
[63]: https://arxiv.org/pdf/2511.16817
[64]: /forum/thread/242#post-1814
[65]: https://www.sciencedirect.com/science/article/pii/0022314X81900391
[66]: https://www.cambridge.org/core/journals/mathematika/article/abs/on-a-problem-of-erdos-straus-and-schinzel/6622BF4A083315C30DF1114A6F600223
[67]: /forum/thread/242#post-1794
[68]: https://gdz.sub.uni-goettingen.de/id/PPN243919689_0211?tify=%7B%22pages%22%3A%5B5%5D%2C%22pan%22%3A%7B%22x%22%3A0.495%2C%22y%22%3A0.757%7D%2C%22view%22%3A%22info%22%2C%22zoom%22%3A0.33%7D
[69]: http://www.bdim.eu/item?id=BUMI_1954_3_9_1_59_0&amp;fmt=pdf
[70]: https://arxiv.org/pdf/1406.6307
[71]: https://www.researchgate.net/publication/368513385_A_simple_direct_proof_of_the_Erdos--Straus_conjecture
[72]: https://arxiv.org/html/2508.07367v1
[73]: /forum/thread/242#post-1747
[74]: /forum/thread/242#post-1748
[75]: /forum/thread/242#post-1753
[76]: /forum/thread/242#post-29
[77]: /forum/login?next=%2Fforum%2Fthread%2F242
[78]: /forum/
