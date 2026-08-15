<!-- source: https://smsxgz.github.io/post/math/an_elegant_result/ | converted from HTML (primary text captured 2025, original Feb 2020) -->

# An elegant result — Blog of smsxgz (Feb 12, 2020)

Full text of "An elegant result", the source of the record-low index recurrence
used to solve Project Euler 700. Based on the method of brob26 (Project Euler
forum).

## Contents

Let $A, M$ be two positive integers such that $A < M$.

Define the sequence $\{c_n\}$ that satisfies $0 \le c_n < M$ and
$c_n \equiv A n (\mathrm{mod}\ M)$ for $n \ge 1$.

Moreover let $n_1 = 1$ and if $c_{n_k} > 0$, we define

$$ n_{k + 1} = \min \{n: n > n_k, c_n < c_{n_k} \}. $$

Hence $A n_{k+1}$ is the first positive multiple of $A$ that yields a residual
less than $c_{n_k}$.

Following theorem shows the recurrence relation of the sequence $\{n_k\}$.

### Theorem 1

Suppose that $c_{n_{k+1}} > 0$, then we have

$$ n_{k+2} = \left\lceil \frac{c_{n_k}}{c_{n_{k+1}}} \right\rceil n_{k+1} - n_k. $$

Following proof is based on the proof of brob26.

**Proof.** Define $\alpha = \left\lceil \frac{c_{n_k}}{c_{n_{k+1}}} \right\rceil$.
Note that

$$ A (\alpha n_{k+1} - n_k) \equiv \left\lceil \frac{c_{n_k}}{c_{n_{k+1}}} \right\rceil c_{n_{k+1}} - c_{n_k} ~~(\mathrm{mod}\ M), $$

and

$$ 0 = \frac{c_{n_k}}{c_{n_{k+1}}} c_{n_{k+1}} - c_{n_k} \le
   \left\lceil \frac{c_{n_k}}{c_{n_{k+1}}} \right\rceil c_{n_{k+1}} - c_{n_k} <
   \left( \frac{c_{n_k}}{c_{n_{k+1}}} + 1\right) c_{n_{k+1}} - c_{n_k} = c_{n_{k+1}}. $$

Then by the definition of $n_{k+2}$, we know that $n_{k+2} \le \alpha n_{k+1} - n_k$.

Next, we will show that for $1 \le t \le \alpha$, there holds
$n_{k+2} - t n_{k+1} + n_k \ge 0$.

For $t = 1$, $n_{k+2} - n_{k+1} + n_k \ge 0$ holds apparently. Furthermore,
assume that for $1 \le t < \alpha$ we have $n_{k+2} - t n_{k+1} + n_k \ge 0$.

Now observe that

$$ A (n_{k+2} - t n_{k+1} + n_k) \equiv c_{n_{k+2}} - t c_{n_{k+1}} + c_{n_k} ~~(\mathrm{mod}\ M). $$

Since $t c_{n_{k+1}} \ge c_{n_{k+1}} > c_{n_{k+2}}$, we have
$c_{n_{k+2}} - t c_{n_{k+1}} + c_{n_k} < c_{n_k}$. And, we also have

$$ c_{n_{k+2}} - t c_{n_{k+1}} + c_{n_k} \ge - (\alpha - 1) c_{n_{k+1}} + c_{n_k} > 0. $$

Thus $n_{k+2} - t n_{k+1} + n_k > 0$. Then by (a counting/minimality argument
completed in the original), iterating over $t$ forces equality, so
$n_{k+2} = \alpha n_{k+1} - n_k$. $\square$

## Why it applies here (Project Euler 700)

With $A = 1504170715041707$ and $M = 4503599627370517$ the Eulercoins are
exactly the record-low residues $c_{n_k}$, and the recurrence gives successive
indices directly in O(log M) steps rather than scanning $n = 1..M$ (M ~ 4.5e15).
The run verifies each step against brute force; see
`research/summaries/record-low-recurrence.md` and `code/out/verify_recurrence.txt`.
