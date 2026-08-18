<!-- source: https://projecteuler.net/problem=1006 | converted from HTML -->

#1006 Fibonacci Subwords - Project Euler

[image: projecteuler.net]

## Fibonacci Subwords

[1] Published on Sunday, 12th July 2026, 11:00 am and solved by 65

### Problem 1006

Starting with two strings $S_0 = 0$ and $S_1 = 01$, we define $S_n$ as the concatenation $S_{n − 1}S_{n − 2}$ for $n \ge 2$.
For example, $S_2 = 010$, $S_3 = 01001$ and $S_4 = 01001010$.
A string is called a Fibonacci subword if it is a **substring contiguous subsequence**of some $S_n$.

Interestingly, for each positive integer $k$, there are only $k + 1$ different Fibonacci subwords of length $k$. We interpret them as decimal numbers (ignoring leading zeros) and let $\Psi(k)$ be the sum of their squares.

For example, the four different Fibonacci subwords of length $3$ are $001, 010, 100, 101$. Therefore $\Psi(3) = 1^2 + 10^2 + 100^2 + 101^2 = 20302$.
You are also given $\Psi(10) \equiv 10699667 \pmod{101001001}$.

Find $\Psi(10^{18}) \bmod 101001001$.

Copied to Clipboard

Project Euler: [Copyright Information][2] | [Privacy Policy][3]

The page has been left unattended for too long and that link/button is no longer active. Please refresh the page.


## Links

[1]: minimal=1006
[2]: copyright
[3]: privacy
