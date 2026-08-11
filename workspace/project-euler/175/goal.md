# Goal

## 1. Verbatim problem statement

Quoted exactly as it appears in `/workspace/problem.html`, after HTML-to-markdown
conversion (the `$...$` math delimiters are kept as in the converted document;
`&gt;` renders as `>`, `<br>` becomes a line break, `<dfn>...</dfn>` becomes plain
text rendered "Shortened Binary Expansion"):

> Define $f(0)=1$ and $f(n)$ to be the number of ways to write $n$ as a sum of powers of $2$ where no power occurs more than twice.
>
> For example, $f(10)=5$ since there are five different ways to express $10$:
> $10 = 8+2 = 8+1+1 = 4+4+2 = 4+2+2+1+1 = 4+4+1+1.$
>
> It can be shown that for every fraction $p / q$ ($p > 0$, $q > 0$) there exists at least one integer $n$ such that $f(n)/f(n-1)=p/q$.
>
> For instance, the smallest $n$ for which $f(n)/f(n-1)=13/17$ is $241$.
> The binary expansion of $241$ is $11110001$.
> Reading this binary number from the most significant bit to the least significant bit there are $4$ one's, $3$ zeroes and $1$ one. We shall call the string $4,3,1$ the Shortened Binary Expansion of $241$.
>
> Find the Shortened Binary Expansion of the smallest $n$ for which $f(n)/f(n-1)=123456789/987654321$.
>
> Give your answer as comma separated integers, without any whitespaces.

## 2. Precise restatement in my own words

**Definition of $f$.** $f(0)=1$. For each integer $n \ge 1$, $f(n)$ is the number
of distinct ways to write $n$ as a sum of powers of $2$ (summands are of the form
$2^k$ with $k \ge 0$), counted as multisets of summands (order of summands does
not matter), subject to the restriction that no single power $2^k$ may occur more
than twice in one way.

**The fraction.** For positive integers $p$ and $q$, define the target ratio
$p/q$. The statement asserts (without proof here) that for every
$p,q$ with $p>0$, $q>0$ there exists at least one positive integer $n$ with
$$\frac{f(n)}{f(n-1)} = \frac{p}{q}.$$
Here $p=123456789$ and $q=987654321$, both positive, and the target is the
fraction $$\frac{123456789}{987654321}$$ in lowest-value form as given (we only
need the ratio; note the existence claim applies to any $p,q$).
The required $n$ is the **smallest** positive integer satisfying
$f(n)/f(n-1) = 123456789/987654321$.

**Shortened Binary Expansion (SBE).** Take the binary expansion of $n$ (most
significant bit is a $1$; leading zeros are not written). Read it from the most
significant bit to the least significant bit and record the lengths of the
maximal constant runs of bits: first the run of $1$'s, then the run of $0$'s,
then $1$'s, and so on, alternating. The list of these run lengths (each a
positive integer) is the SBE of $n$, written as comma-separated integers.

**Worked example of SBE.** $n=241$ has binary expansion $11110001$, whose runs
from the MSB are $1111$, $000$, $1$, with lengths $4$, $3$, $1$, so the SBE of
$241$ is the string `4,3,1`.

**Requested output.** The SBE of the smallest $n$ for which
$f(n)/f(n-1) = 123456789/987654321$, given as comma separated integers with no
whitespace (e.g., in the style `4,3,1`).

**Completion criteria.**

- Produce the comma-separated integer string that is the SBE of the smallest
  $n$ satisfying the ratio condition (not yet done; do not solve here).
- Validate the method against the oracle below before any full-size run.

## 3. Small cases and worked examples (test oracle)

Verbatim from the statement; these are the oracle every implementation must
reproduce before it is trusted at the full target size.

1. $f(10) = 5$, because the five ways to express $10$ are:
   $10 = 8+2 = 8+1+1 = 4+4+2 = 4+2+2+1+1 = 4+4+1+1.$
   (Check: every summand is a power of $2$; in each way no power occurs more
   than twice; there are exactly five such ways.)

2. The smallest $n$ for which $f(n)/f(n-1)=13/17$ is $241$.
   (Check: $f(241)/f(240) = 13/17$ and no smaller $n$ has ratio $13/17$.)

3. The binary expansion of $241$ is $11110001$.

4. Reading $11110001$ from the most significant bit to the least significant
   bit, there are $4$ one's, $3$ zeroes and $1$ one; the string $4,3,1$ is the
   Shortened Binary Expansion of $241$.

Do not solve the problem here; the answer string for
$123456789/987654321$ is intentionally not computed in this document.