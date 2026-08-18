# Goal: Project Euler 1006

Let `S_0 = "0"`, `S_1 = "01"`, and for `n >= 2`, `S_n = S_{n-1}S_{n-2}` where juxtaposition means concatenation. A Fibonacci subword (factor) of length `k >= 1` is a contiguous substring of length `k` occurring in some `S_n`. The statement gives that there are exactly `k+1` distinct such factors.

Interpret each binary factor as a decimal integer, allowing leading zeroes in the word but hence ignoring them numerically. Define `Psi(k)` as the sum of the squares of these `k+1` integers. Required: `Psi(10^18) mod 101001001`.

Examples/oracles: `S_2=010`, `S_3=01001`, `S_4=01001010`; factors of length 3 are `001,010,100,101`, so `Psi(3)=20302`; and `Psi(10) mod 101001001 = 10699667`.