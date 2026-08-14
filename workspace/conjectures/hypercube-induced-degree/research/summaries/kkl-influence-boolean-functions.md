# The influence of variables on Boolean functions (KKL)

Source: J. Kahn, G. Kalai, N. Linial, "The influence of variables on Boolean
functions", IEEE FOCS 1988, pp. 68–80. URL: https://doi.org/10.1109/sfcs.1988.21923

## What it establishes

**KKL theorem:** For any Boolean function f: {0,1}^n → {0,1} with expectation
α, there exists a coordinate i whose influence (discrete-derivative L2 norm)
satisfies

    ||f_i||_2^2  >=  c · α(1−α) · log(n)/n

for an absolute constant c > 0, where f_i is the derivative in coordinate i.
For a balanced function (α = 1/2), max_i Inf_i(f) ≥ c' · log(n)/n.

Method: harmonic analysis on {0,1}^n with the Beckner–Bonami–Gross
hypercontractive inequality.

## Relevance to problem.md

This is the standard tool that produces a bound on a **maximum-influence**
quantity (an individual coordinate) rather than only an average. The problem.md
note lists "influence/Fourier arguments" as one of the four stuck techniques —
this is the primary source of that technique. But note what it bounds: the
maximum **influence of a coordinate**, which concerns how a function changes
when a single bit is flipped — a boundary-type sensitivity, not the maximum
internal degree of the level set S. The connection between D(S) and coordinate
influences is not a direct transfer and must be established (it is a gap, not a
fact). KKL is here because it is the canonical "maximum-from-analysis" result —
the kind of quantity problem.md says the lower bound must come from — and
because it bounds a sum over S of boundary degrees, close to but not equal to
D(S).
