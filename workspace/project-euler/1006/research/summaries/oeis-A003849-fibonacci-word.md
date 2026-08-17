> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A003849-fibonacci-word.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A003849/internal | converted from HTML -->

A003849 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A003849 - OEIS] [3]

[A003849][4]

The infinite Fibonacci word (start with 0, apply 0->01, 1->0, take limit).

228

%I #331 Aug 16 2026 16:27:22

%S 0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,

%T 0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,

%U 0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1

%N The infinite Fibonacci word (start with 0, apply 0->01, 1->0, take limit).

%C A Sturmian word.

%C Define strings S(0)=0, S(1)=01, S(n)=S(n-1)S(n-2); iterate; sequence is S(infinity). If the initial 0 is omitted from S(n) for n>0, we obtain A288582(n+1).

%C The 0's occur at positions in A022342 (i.e., A000201 - 1), the 1's at positions in A003622.

%C Replace each run (1;1) with (1;0) in the infinite Fibonacci word A005614 (and add 0 as prefix) A005614 begins: 1,0,1,1,0,1,0,1,1,0,1,1,... changing runs (1,1) with (1,0) produces 1,0,0,1,0,1,0,0,1,0,0,1,... - _Benoit Cloitre_, Nov 10 2003

%C Characteristic function of A003622. - _Philippe Deléham_, May 03 2004

%C The fraction of 0's in the first n terms approaches 1/phi (see for example Allouche and Shallit). - _N. J. A. Sloane_, Sep 24 2007

%C The limiting mean and variance of the first n terms are 2-phi and 2*phi-3, respectively. - _Clark Kimberling_, Mar 12 2014, Aug 16 2018

%C Let S(n) be defined as above. Then this sequence is S(1) + Sum_{n=0..} S(n), where the addition of strings represents concatenation. - _Isaac Saffold_, May 03 2019

%C The word is a concatenation of three runs: 0, 1, and 00. The limiting proportions of these are respectively 1 - phi/2, 1/2, and (phi - 1)/2. The mean runlength is (phi + 1)/2. - _Clark Kimberling_, Dec 26 2010

%C From _Amiram Eldar_, Mar 10 2021: (Start)

%C a(n) is the number of the trailing 0's in the dual Zeckendorf representation of (n+1) (A104326).

%C The asymptotic density of the occurrences of k (0 or 1) is 1/phi^(k+1), where phi is the golden ratio (A001622).

%C The asymptotic mean of this sequence is 1/phi^2 (A132338). (End)

%D J.-P. Allouche and J. Shallit, Automatic Sequences, Cambridge Univ. Press, 2003.

%D Jean Berstel, Fibonacci words—a survey, In The book of L, pp. 13-27. Springer Berlin Heidelberg, 1986.

%D J. C. Lagarias, Number Theory and Dynamical Systems, pp. 35-72 of S. A. Burr, ed., The Unreasonable Effectiveness of Number Theory, Proc. Sympos. Appl. Math., 46 (1992). Amer. Math. Soc. - see p. 64.

%D Wolfdieter Lang, The Wythoff and the Zeckendorf representations of numbers are equivalent, in G. E. Bergum et al. (edts.) Application of Fibonacci numbers vol. 6, Kluwer, Dordrecht, 1996, pp. 319-337. [See A317208 for a link.]

%D G. Melançon, Factorizing infinite words using Maple, MapleTech journal, vol. 4, no. 1, 1997, pp. 34-42, esp. p. 36.

%D Michel Rigo, Formal Languages, Automata and Numeration Systems, 2 vols., Wiley, 2014. Mentions this sequence - see "List of Sequences" in Vol. 2.

%H N. J. A. Sloane, <a href="/A003849/b003849.txt">Table of n, a(n) for n = 0..10945</a>

%H A. G. M. Ahmed, <a href="https://archive.bridgesmathart.org/2013/bridges2013-263.pdf">AA Weaving</a>, in Proceedings of Bridges 2013: Mathematics, Music, Art, Architecture, Culture.

%H Jean-Paul Allouche, Julien Cassaigne, Jeffrey Shallit, and Luca Q. Zamboni, <a href="https://arxiv.org/abs/1711.10807">A Taxonomy of Morphic Sequences</a>, arXiv preprint arXiv:1711.10807 [cs.FL], Nov 29 2017.

%H J.-P. Allouche and M. Mendes France, <a href="https://webusers.imj-prg.fr/~jean-paul.allouche/allmendeshouches.pdf">Automata and Automatic Sequences</a>, in: Axel F. and Gratias D. (eds), Beyond Quasicrystals. Centre de Physique des Houches, vol 3. Springer, Berlin, Heidelberg, pp. 293-367, 1995; DOI https://doi.org/10.1007/978-3-662-03130-8_11.


*[excerpt ends; 13426 characters not shown — see `research/sources/oeis-A003849-fibonacci-word.full.md`]*
