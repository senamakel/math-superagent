> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/eppstein-small-numerators.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.ics.uci.edu/~eppstein/numth/egypt/smallnum.html | converted from HTML -->

## What is in it

  - Small Numerators
    - Numerator 3
    - Numerator 4
      - Modular Conditions
      - Particular Values


## What it claims

The algorithms described above work for any input. We now discuss techniques limited to specific numerators. The typical question here is how many terms are needed to represent fractions with a given numerator. For fractions 2/y the answer is clearly 2. Some fractions 3/y require 3 terms, as we see below. It is not known whether any fraction 4/y requires 4 terms.

More generally, good bounds are known on the number of terms needed to represent x/y measured as a function of y [[Vos85]][1], but there seems to be less work on measuring this minimum number of terms as a function only of x. As we note in the section on 4/y, a solution to this specific case would have implications for the general problem.

## Statements it makes

**Theorem: **3/y has a two-term expansion if and only if y has a factor congruent to 2 mod 3.

*[digest of a 7523 character source; every section, statement, and proof in full at `research/sources/eppstein-small-numerators.full.md`]*
