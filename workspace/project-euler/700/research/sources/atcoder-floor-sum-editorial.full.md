<!-- source: https://atcoder.jp/contests/practice2/editorial/579 | converted from HTML (primary text captured 2025) -->

# C - Floor Sum Editorial by yosupo — AtCoder Library Practice Contest

Full text of the AtCoder editorial defining the O(log) floor_sum recursion used
as the independent verification route for Project Euler 700 (see
`research/summaries/floor-sum-editorial.md`).

Design an algorithm to compute the following function quickly for
$(n, m, a, b \in \mathbb{Z}),\ (0 \leq n),\ (1 \leq m)$:

$$ f(n, m, a, b) = \sum_{i=0}^{n-1} \left\lfloor \frac{ai + b}{m} \right\rfloor $$

First, we can take $a, b$ modulo $m$; if $a = 0$ it is trivial, so it reduces to
the case $1 \le a < m, 0 \le b < m$.

Let $y = \left\lfloor \frac{an + b}{m} \right\rfloor$, $z = (an + b) \% m$.
The following identity holds:

$$ f(n, m, a, b) = f(y, a, m, z) $$

Designing the recursive function according to this identity, $a, m$ behave
like the Euclidean algorithm, so it can be computed in $O(\log a + \log m)$
levels of recursion. The proof of the identity follows.

The essential idea is the following transformation: instead of summing the value
over each $i$, count, for each value $x$, how many $i$ exceed that value, and sum
those counts.

$$ \begin{aligned} f(n, m, a, b) &= \sum_{i=0}^{n-1} \left\lfloor \frac{ai + b}{m} \right\rfloor \\ &= \sum_{x=1}^{y} \left(\#\ \text{of } i \in \{0, 1, \cdots, n - 1\} \text{ s.t. } \left\lfloor \frac{ai + b}{m} \right\rfloor \geq x \right) \\ &= \sum_{x=0}^{y - 1} \left( \#\ \text{of } i \in \{0, 1, \cdots, n - 1\} \text{ s.t. } \left\lfloor \frac{ai + b}{m} \right\rfloor \geq (y - x) \right) \end{aligned} $$

Here, rearranging the inner expression,

$$ \begin{aligned} \left\lfloor \frac{ai + b}{m} \right\rfloor \geq (y - x) &\Leftrightarrow \frac{ai + b}{m} \geq (y - x) \\ &\Leftrightarrow i \geq \frac{(y - x)m - b}{a} \end{aligned} $$

so the following holds:

$$ \left( \#\ \text{of } i \in \{0, 1, \cdots, n - 1\} \text{ s.t. } \left\lfloor \frac{ai + b}{m} \right\rfloor \geq (y - x) \right) = \left\lfloor n - \frac{(y - x)m - b}{a} \right\rfloor $$

Finally, using $y = \frac{an + b - z}{m}$, we obtain $f(n, m, a, b) = f(y, a, m, z)$:

$$ \begin{aligned} \left\lfloor n - \frac{(y - x)m - b}{a} \right\rfloor &= \left\lfloor n - \frac{(\frac{an + b - z}{m} - x)m - b}{a} \right\rfloor \\ &= \left\lfloor \frac{z + xm}{a} \right\rfloor \end{aligned} $$

This editorial explains code proposed by rsk0315 in the AtCoder Library Pull Request.
