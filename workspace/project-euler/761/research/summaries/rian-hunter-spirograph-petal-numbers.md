> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/rian-hunter-spirograph-petal-numbers.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://thelig.ht/petalnumbers/part2.html | converted from HTML -->

## What is in it

- The Number Hiding Inside the Spirograph Part 2
  - Deriving p as b → ∞
  - Proof That P P ∞ n ≠ 0 is Transcendental
  - Computing P P ∞ n
  - Conclusion
  - Addendum: Computing the Fixed Points of tan x
- this is necessary for the series reversion
# algorithm to work
assert not s.coeff(x, 0)…


## What it claims

After the I published the first article about the Petal Numbers, I received two interesting responses on Reddit. Reddit user *[existentialpenguin][2]*commented that he did a search for the approximate form of p as b → ∞ (`4.603338`) in the OEIS and found [an entry][3] that matched very closely. That entry lists that it is the solution of ( arccos ( 1 p) + π) 2 + 1 = p 2, derived from a different problem completely. Reddit user *[BruhcamoleNibberDick][4]*then sketched out a derivation of p resulting in the same equation, which would in theory prove the two numbers are equal.

In this article we'll go over a derivation of p inspired by *BruhcamoleNibberDick*'s comment, prove that p is indeed transcendental, and finally we'll provide an efficient method to compute p.

*[digest of a 16178 character source; every section, statement, and proof in full at `research/sources/rian-hunter-spirograph-petal-numbers.full.md`]*
