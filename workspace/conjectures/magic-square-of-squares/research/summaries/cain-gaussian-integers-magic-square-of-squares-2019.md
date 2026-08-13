> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/cain-gaussian-integers-magic-square-of-squares-2019.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1908.03236 | converted from PDF -->

## What it claims

Abstract. We show the 3 × 3 magic square of squares problem equivalent
to solving quartic polynomials with certain factorization constraints over an
abelian extension of the rationals. We analyze a particular case in which said
extension is assumed to be the Gaussian integers resulting a new search method.
Additionally, the magic square of squares is analyzed over ﬁnite ﬁelds and rings
of the form Z/nZ resulting in some conjectures enumerating the rings and ﬁnite
ﬁelds in which a magic square of squares can be constructed. Code is made
available.

1 Background

The construction of a 3 × 3 magic square of squares – sometimes called simply
the magic square of squares problem – is deﬁned to be 9 distinct squared integers
placed in a 3 × 3 grid, 


a2 b2 c2

d
2 e2 f 2

g2 h2 i2
 

 ,

such that the sums of the elements in each row, column, and the two main
diagonals sum to the same total. That is to say for some integer total T we
have a2 + b2 + c2 = d
2 + e2 + f 2 = g2 + h2 + i2 = T,

a2 + d
2 + g2 = b2 + e2 + h2 = c2 + f 2 + i2 = T,

and a2 + e2 + i2 = g2 + e2 + c2 = T.

In total…

## Statements it makes

Theorem 2.1: The total of any magic hourglass of squares T is 3 times the
central entry e2.

Theorem 2.2: For every integer solution to r2 + t2 = 2s2 there exist 3 in-
teger parameters m, n, and k such that

Theorem 2.2 has a nice reinterpretation as

Lemma 3.1: For every integer solution to r2 + t2 = 2s2 there exists a complex
number ω ∈ Z[i, √
k] such that k is an integer and

Theorem 3.2: A magic hourglass of squares,


Theorem 4.1: If there exists x, y, z ∈ Z[i] such that

Theorem 4.2: If there exists a magic hourglass of squares, then there exists
x, y, z ∈ Z such that
 Im[x
2y2z2] = −4Im[x
2]Im[y2]Im[z2]

Lemma 5.1: All 3 × 3 magic squares over ﬁnite ﬁelds of even order have
duplicate entries.

Corollary 5.1: All ﬁnite ﬁelds of even order are Parker.
Proof: By Lemma 3.1 any 3×3 magic square over a ﬁnite ﬁeld has duplicate
entries. □

Lemma 5.2: A ﬁnite ﬁeld of odd order, q, has q+1
2 squares.
Proof: This follows easily from the fact that F×
q is cyclic (for proof of which,
we cite Artin [7] again; Theorem 15.7.3). □

Corollary 5.2: The ﬁelds F3, F5, F7, F9, F11, and F13 are Parker.
Proof: By Lemma 5.2, each of the ﬁelds in question have fewer than 9
distinct squares. Therefore no 3 × 3 magic square of distinct squares can be
formed. □

Lemma 5.3: Any non-Parker ﬁnite ﬁeld contains either 4 distinct solutions
to x
2 + y2 = 0 with x, y ̸= 0 or 4 distinct solutions to x
2 + y2 = 2 with
x
2, y2 ̸= 2.
Proof: By deﬁnition, a non-Parker ﬁeld contains at least one magic square
of distinct squares. We use the standard variables

Corollary 5.3: The ﬁelds F19, F23, and F27 are Parker.
Proof: Let’s count the solutions x
2 +y2 = 0, 2 in each of of the ﬁelds in ques-
tion. This took us roughly 10 minutes per ﬁeld to do by hand (and was, in fact,
further veriﬁed with computation [9]). There are no solutions to x
2 + y2 = 0.
The respective solutions to x
2 + y2 = 2 are

Lemma 5.4: Magic squares of distinct squares over a ﬁnite ﬁeld with a central
entry of 0 are parametrized (up to scaling) by solutions to α
2 − β2 = β2 − γ2 = 1
(i.e. three consecutive squares) satisfying {α, β, γ} ∩ {0, 1, −1} = ∅.

Corollary 5.4: The ﬁelds F17 and F25 are Parker.

Theorem 5.1: F29 is the non-Parker ﬁeld of smallest order.
Proof: All ﬁnite ﬁelds of smaller order are Parker by Corollaries 5.1, 5.2,
5.3, and 5.4. We see that F29 is non-Parker by the aforementioned construction.
□

Algorithm 6.1:
# Input: A ﬁnite ﬁeld, Fq.
# Output: Set of all tuples (a2, b2, ..., i2) forming magic squares over Fq
# up to scaling.
function msos ﬁeld(Fq):
SQUARES ← {x
2 : x
2 ∈ Fq}
MSOS ← {}
e ← 0 # ﬁrst case.
for {a2, i2} ⊂ SQUARES:
if a2 + i2 ̸= 2e2: continue
c2, g2 ← 1, −1
B ← 3e2 − a2 − c2

Algorithm 6.1 was implemented in a computer algebra system [9] (actually, it
was ﬁrst written in a computer algebra system and then turned into pseudo-
code, but whatever). Some results:

Corollary 7.1:…


*[further statements in the full text]*

*[digest of a 24637 character source; every section, statement, and proof in full at `research/sources/cain-gaussian-integers-magic-square-of-squares-2019.full.md`]*
