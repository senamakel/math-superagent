> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/singmaster-1971.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://fermatslibrary.com/s/how-often-does-an-integer-occur-as-a-binomial-coefficient | converted from HTML -->

## What is in it

    - Comments
        - Products
        - Project


## What it claims

3003 occurs twice in its own row, twice in row 78 and twice in rows 14 and 15. $$ \binom{3003}{1} = \binom{78}{2} = \binom{15}{5} = \binom{14}{6} $$ Additionally, it’s the only number known to appear 8 or more times. There are also no known integers which occur in the triangle exactly five or seven times. To prove the $O( \log a)$ bound we start by defining $N(a)$ as the number of solutions of $a=\binom{i+j}{j}=\binom{i+j}{i}$ , with $i,j \geq 1$ (since Pascal's triangle is symmetrical along its central column). Since, $\binom{i+j}{i}$ increases in each of $i$ and $j$ (in other words, if you pick a diagonal and follow it down or pick a column and follow it down the binomial coefficients will always increase), any choice of $i$ or $j$ admits a new solution value for $N(a)$. Now let's suppose that $a$ satisfies $a \leq \binom{2b}{b}$ implies that $i$ or $j < b$, so the solution count $N(a)≤ 2b$. Take the least such $b$. Then $2^{b-1} ≤\binom{2(b−1)}{b−1}≤ a$, $b ≤1+\log_2 a$, and $N(a) ≤ 2 + 2 \log_2 a = O(\log a)$ In 2007, Daniel Kane, a mathematician from Harvard, was able to…

[FE…

## Statements it makes

PROPOSITION.

*[digest of a 8520 character source; every section, statement, and proof in full at `research/sources/singmaster-1971.full.md`]*
