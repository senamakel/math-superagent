# Goal: Project Euler 1006

Define binary strings `S_0 = "0"`, `S_1 = "01"`, and, for every integer `n >= 2`, `S_n = S_{n-1}S_{n-2}` where juxtaposition means concatenation. For a positive integer `k`, let `F_k` be the set of distinct binary strings `x = x_0...x_{k-1}` of length `k` that occur as contiguous substrings of at least one `S_n` (equivalently, of the infinite Fibonacci word, once the factors stabilize). Define

`val(x) = sum_{j=0}^{k-1} x_j 10^{k-1-j}`,

where each `x_j` is 0 or 1; leading zeroes therefore do not change the integer value. Define

`Psi(k) = sum_{x in F_k} val(x)^2`.

The modulus is `M = 101001001`. The worked oracles in the statement are:

- `F_3 = {001, 010, 100, 101}`;
- `Psi(3) = 1^2 + 10^2 + 100^2 + 101^2 = 20302`;
- `Psi(10) mod M = 10699667`.

Compute `Psi(10^18) mod M`.
