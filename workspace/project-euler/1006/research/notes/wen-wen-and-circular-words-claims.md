# Wen & Wen, "Some properties of the singular words of the Fibonacci word" — claim

```claim
id: wen-wen-singular-words-structure
statement: The Fibonacci infinite word F_∞ admits two decompositions into its
singular words w_n (Theorems 1, 2); w_n is a palindrome for n >= 1 and
primitive for n >= 2; w_n appears exactly once in F_{n-1}F_n; the singular words
satisfy w_n = w_{n-2} w_{n-3} w_{n-2}; adjacent singular words of the same
order are positively separated; a factor w of F_∞ is a special (right-special)
word iff w is a prefix of some finite Fibonacci word F_n (Theorem 5); and for
any factor u of F_∞, u^4 is never a factor (Theorem 3).
hypotheses: Fibonacci/rabbit convention (a=b, b=a-complement of PE1006's S);
finite Fibonacci words F_n with |F_n| = f_n the Fibonacci numbers.
holds-here: true (single-letter alphabet relabel — the structures are
convention-independent).
status: sourced
follows-from: (independent corroboration) fibonacci-unique-special-factor-reverse,
fibonacci-squares-conjugate-finite-word
bearing: Primary structural anchor for the factor set the run sums over: the
special/prefix characterization (Theorem 5) corroborates the one-right-special
factor structure; the power facts (u^4 never a factor) bound the square/power
content of factors (= window-prefix length bounds).
anchor: research/sources/wen-wen-singular-words-fibonacci-word-1994.full.md
(https://www.mat.univie.ac.at/~slc/opapers/s30wen.pdf)
```

# Hegedüs–Nagy, "Representations of Circular Words" — claim

```claim
id: hegedus-nagy-circular-words-fibonacci-trees
statement: For the finite Fibonacci words f_1=b, f_2=a, f_n=f_{n-1}f_{n-2}, the
tree of the circular word (f_i)° has exactly one branching node on every level
except the last two (Thm 3); if j > i then phi_i is a subtree of phi_j
(Cor 1); the distance between two consecutive branching nodes on a path is a
Fibonacci number (Thm 4). The paper restates as Lemma 2 (after Séébold) that
if u^2 is a factor of the infinite Fibonacci word then u is a conjugate of some
finite Fibonacci word, and notes the Sturmian fact that the number of distinct
length-k factors of the infinite Fibonacci word is k+1.
hypotheses: Fibonacci word convention f_1=b, f_2=a (relabel of PE1006's); the
Sturmian factor-complexity fact k+1 is assumed standard.
holds-here: yes — the relabel preserves all factor/conjugacy facts; the k+1
factor count is exactly the problem's "k+1 distinct Fibonacci subwords".
status: sourced
follows-from: governing-factor-complexity (independent second source for the
k+1 count); fibonacci-squares-conjugate-finite-word (second independent
statement of the Séébold square-factor lemma)
bearing: second, independent (EPTCS/arXiv 1405.5607) source for the k+1 factor
count and for the square-conjugate identification used in the run's
factor-structure arguments.
anchor: research/sources/hegedus-nagy-representations-circular-words-arxiv.full.md
(https://arxiv.org/html/1405.5607v1; EPTCS 151 (2014) 261-270)
```