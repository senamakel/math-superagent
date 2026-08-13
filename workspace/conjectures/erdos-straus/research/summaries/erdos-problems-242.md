> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/erdos-problems-242.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

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


*[excerpt ends; 1869 characters not shown — see `research/sources/erdos-problems-242.full.md`]*
