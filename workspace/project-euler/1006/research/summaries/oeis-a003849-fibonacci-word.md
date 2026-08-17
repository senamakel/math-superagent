> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-a003849-fibonacci-word.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A003849 | converted from HTML -->

A003849 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A003849 - OEIS] [3]

A003849

The infinite Fibonacci word (start with 0, apply 0->01, 1->0, take limit).

228

0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

0,1

COMMENTS

A Sturmian word.

Define strings S(0)=0, S(1)=01, S(n)=S(n-1)S(n-2); iterate; sequence is S(infinity). If the initial 0 is omitted from S(n) for n>0, we obtain [A288582][11] (n+1).

The 0's occur at positions in [A022342][12] (i.e., [A000201][13] - 1), the 1's at positions in [A003622][14].

Replace each run (1;1) with (1;0) in the infinite Fibonacci word [A005614][15] (and add 0 as prefix) [A005614][15] begins: 1,0,1,1,0,1,0,1,1,0,1,1,... changing runs (1,1) with (1,0) produces 1,0,0,1,0,1,0,0,1,0,0,1,... - [Benoit Cloitre][16], Nov 10 2003

Characteristic function of [A003622][14]. - [Philippe Deléham][17], May 03 2004

The fraction of 0's in the first n terms approaches 1/phi (see for example Allouche and Shallit). - [N. J. A. Sloane][18], Sep 24 2007

The limiting mean and variance of the first n terms are 2-phi and 2*phi-3, respectively. - [Clark Kimberling][19], Mar 12 2014, Aug 16 2018

Let S(n) be defined as above. Then this sequence is S(1) + Sum_{n=0..} S(n), where the addition of strings represents concatenation. - [Isaac Saffold][20], May 03 2019

The word is a concatenation of three runs: 0, 1, and 00. The limiting proportions of these are respectively 1 - phi/2, 1/2, and (phi - 1)/2. The mean runlength is (phi + 1)/2. - [Clark Kimberling][19], Dec 26 2010

From [Amiram Eldar][21], Mar 10 2021: (Start)

a(n) is the number of the trailing 0's in the dual Zeckendorf representation of (n+1) ( [A104326][22]).

The asymptotic density of the occurrences of k (0 or 1) is 1/phi^(k+1), where phi is the golden ratio ( [A001622][23]).

The asymptotic mean of this sequence is 1/phi^2 ( [A132338][24]). (End)

REFERENCES

J.-P. Allouche and J. Shallit, Automatic Sequences, Cambridge Univ. Press, 2003.

Jean Berstel, Fibonacci words—a survey, In The book of L, pp. 13-27. Springer Berlin Heidelberg, 1986.

J. C. Lagarias, Number Theory and Dynamical Systems, pp. 35-72 of S. A. Burr, ed., The Unreasonable Effectiveness of Number Theory, Proc. Sympos. Appl. Math., 46 (1992). Amer. Math. Soc. - see p. 64.

Wolfdieter Lang, The Wythoff and the Zeckendorf representations of numbers are equivalent, in G. E. Bergum et al. (edts.) Application of Fibonacci numbers vol. 6, Kluwer, Dordrecht, 1996, pp. 319-337. [See [A317208][25] for a link.]

G. Melançon, Factorizing infinite words using Maple, MapleTech journal, vol. 4, no. 1, 1997, pp. 34-42, esp. p. 36.

Michel Rigo, Formal Languages, Automata and Numeration Systems, 2 vols., Wiley, 2014. Mentions this sequence - see "List of Sequences" in Vol. 2.

LINKS

N. J. A. Sloane, [Table of n, a(n) for n = 0..10945][26]

A. G. M. Ahmed, [AA Weaving][27], in Proceedings of Bridges 2013: Mathematics, Music, Art, Architecture, Culture.

Jean-Paul Allouche, Julien Cassaigne, Jeffrey Shallit, and Luca Q. Zamboni, [A Taxonomy of Morphic Sequences][28], arXiv preprint arXiv:1711.10807 [cs.FL], Nov 29 2017.

J.-P. Allouche and M. Mendes France, [Automata and Automatic Sequences][29], in: Axel F. and Gratias D. (eds), Beyond Quasicrystals. Centre de Physique des Houches, vol 3. Springer, Berlin, Heidelberg, pp. 293-367, 1995; DOI https://doi.org/10.1007/978-3-662-03130-8_11.


*[excerpt ends; 16050 characters not shown — see `research/sources/oeis-a003849-fibonacci-word.full.md`]*
