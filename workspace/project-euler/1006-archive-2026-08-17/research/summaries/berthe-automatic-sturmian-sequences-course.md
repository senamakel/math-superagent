# Berthé, "Sequences of Low Complexity: Automatic and Sturmian Sequences" (course notes)

<!-- source: https://www.irif.fr/~berthe/Articles/chili.pdf -->

Lecture-course notes (not a research paper) on complexity theory of infinite words,
automatic sequences, and Sturmian sequences.

## What it establishes / provides relevant to PE1006
- **Complexity function** p(n) = #distinct length-n factors; factor frequencies.
- **Theorem 6.3 (Hedlund & Morse / Hedlund)**: a sequence u is Sturmian iff u is the coding
  of the orbit of x under rotation by an irrational angle α for a two-part partition — the
  mechanical-word / rotation characterization of Sturmian words.
- **Theorem 6.5 (three-distance theorem)**: the n+1 intervals from {iα}, 0<=i<=n, take at
  most three lengths; refined counts via convergents — the Diophantine structure behind how
  the n+1 factors are placed.
- Frequencies of length-n factors of a Sturmian sequence take at most three values (Thm 6.4).

## What it implies for this problem
Background / surrounding theory. It independently confirms the Sturmian identification (the
Fibonacci word, slope 1/φ² irrational, is the coding of a rotation, hence Sturmian with
exactly k+1 factors). It does **not** provide the consecutive-factor lex-order enumeration
(Perrin–Restivo) nor a closed form for Ψ(k), so it is not itself load-bearing for the sum.
The three-distance theorem is a conceptual backdrop to how the factors distribute but is not
needed to sum their squares once the lex-order enumeration is in hand. `status: background`.

## Full text
[[berthe-automatic-sturmian-sequences-course.full]]
