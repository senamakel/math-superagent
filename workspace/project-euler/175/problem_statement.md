# Problem Statement (verbatim extraction)

Source: local file `/workspace/problem.html` (minimal Project Euler statement, plain-text converted; raw HTML verified against source). No external resources consulted.

## Definitions

> Define $f(0)=1$ and $f(n)$ to be the number of ways to write $n$ as a sum of powers of $2$ where no power occurs more than twice.

Decimal rendering of the same sentence (verbatim words):

> Define f(0)=1 and f(n) to be the number of ways to write n as a sum of powers of 2 where no power occurs more than twice.

Additional defined term:

> We shall call the string $4,3,1$ the **Shortened Binary Expansion** of $241$.

Definition context (full verbatim paragraph, including the run-counting rule):

> Reading this binary number from the most significant bit to the least significant bit there are $4$ one's, $3$ zeroes and $1$ one. We shall call the string $4,3,1$ the Shortened Binary Expansion of $241$.

## Small cases / worked example

Verbatim worked example:

> For example, $f(10)=5$ since there are five different ways to express $10$:<br>$10 = 8+2 = 8+1+1 = 4+4+2 = 4+2+2+1+1 = 4+4+1+1.$

Decimal rendering:

> For example, f(10)=5 since there are five different ways to express 10:
> 10 = 8+2 = 8+1+1 = 4+4+2 = 4+2+2+1+1 = 4+4+1+1.

Verbatim equivalence example:

> For instance, the smallest $n$ for which $f(n)/f(n-1)=13/17$ is $241$.<br>
> The binary expansion of $241$ is $11110001$.<br>
> Reading this binary number from the most significant bit to the least significant bit there are $4$ one's, $3$ zeroes and $1$ one. We shall call the string $4,3,1$ the Shortened Binary Expansion of $241$.

Decimal rendering:

> For instance, the smallest n for which f(n)/f(n-1)=13/17 is 241.
> The binary expansion of 241 is 11110001.
> Reading this binary number from the most significant bit to the least significant bit there are 4 one's, 3 zeroes and 1 one. We shall call the string 4,3,1 the Shortened Binary Expansion of 241.

Notes on the worked example (derived from the statement only, not a solution attempt):

- $241$ in binary is $11110001_2$ (verify: $128+64+32+16+1 = 241$).
- The bits read MSB→LSB form runs: $1111$ (four 1's), $000$ (three 0's), $1$ (one 1), giving the run-length string $4,3,1$.
- Hence the Shortened Binary Expansion of $241$ is the comma-separated list of run lengths of the binary representation's runs of equal bits, read from most significant to least significant bit.

## Target

Verbatim:

> Find the Shortened Binary Expansion of the smallest $n$ for which $f(n)/f(n-1)=123456789/987654321$.

Decimal rendering:

> Find the Shortened Binary Expansion of the smallest n for which f(n)/f(n-1)=123456789/987654321.

Existence is asserted verbatim in the statement:

> It can be shown that for every fraction $p / q$ ($p \gt 0$, $q \gt 0$) there exists at least one integer $n$ such that $f(n)/f(n-1)=p/q$.

Decimal rendering:

> It can be shown that for every fraction p / q (p > 0, q > 0) there exists at least one integer n such that f(n)/f(n-1)=p/q.

So the target values are: the integer $n$ (smallest with $f(n)/f(n-1)=123456789/987654321$), and its Shortened Binary Expansion, i.e., the run-length string of the binary representation of that $n$ read from the most significant bit to the least significant bit.

## Output format (verbatim quotes)

The complete output-format specification sentence, word for word:

> Give your answer as comma separated integers, without any whitespaces.

I.e., the final answer must be the Shortened Binary Expansion as integers separated by commas with no whitespace (no spaces, no line breaks — e.g., `4,3,1` for the sample).

Note: the statement itself does not specify trailing-newline behaviour; it specifies that the answer contains commas between integers and no whitespace.