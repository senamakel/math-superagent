> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/L0.0/cgmo_opening_dijkstra.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.cs.utexas.edu/~EWD/transcriptions/EWD12xx/EWD1200.html | converted from HTML -->

## What it claims

For educational purposes we analyse the opening pages of an 11-page article that appeared in *The American Mathematical Monthly*, Volume 102 Number 2 / February 1995. We added line numbers in the right margin.

line 4: Since in this article, squares don&rsquo;t get alternating colours, it could be argued that the term &ldquo;chessboard&rdquo; is misplaced.

line 4: The introduction of the name &ldquo; B &rdquo; seems unnecessary: it is used —in the combination &ldquo;the board B &rdquo;— in the text for Figure 1 and in line 71; in both cases just &ldquo;the board&rdquo; would have done fine. In line 77 occurs the last use of B, viz. in &ldquo; X ⊂ B &rdquo;, which is dubious since B was a board and not a set; in line 77, I would have preferred &ldquo;Given a set X of cells&rdquo;.

line 7/8: The first move, being a move like any other, does not deserve a separate description. The term &ldquo;step&rdquo; is redundant.

line 8: Why not &ldquo;a move consists of&rdquo;?

line 10/11: At this stage the italics are puzzling, since a move is possible if, for some i,&thinsp; j, cell (…

line…

## Statements it makes

**Lemma 1.**[**9**] *The set L*(1) ∪*L*(2) ∪*L*(3) *of all *(*i*,*&thinsp;j*) *with i + j ≤ 3 is unavoidable.*
*Proof:*To each cell ( i, &thinsp;j) assign the *weight*2 −( i + j). Observe that:  | 35 |

**Lemma 2.**L (1) ∪ L (2) *is unavoidable*.

**Lemma 3.***If a configuration of pebbles (with at most one pebble per cell) can be
reached by moves which ***allow***accumulations of pebbles in cells, then in fact it can* | 70 |

**Theorem 1.**X ⊂ B*is unavoidable if and only if after executing the moves in*M ( X),
*some cell contains at least 3 pebbles.*
 | 80 |

*[digest of a 16047 character source; every section, statement, and proof in full at `research/L0.0/cgmo_opening_dijkstra.full.md`]*
