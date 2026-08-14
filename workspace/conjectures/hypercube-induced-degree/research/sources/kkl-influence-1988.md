# Kahn–Kalai–Linial, "The influence of variables on Boolean functions" (FOCS 1988)

Source URL: https://doi.org/10.1109/sfcs.1988.21923
(Retrieved via search metadata + scholar summary; PDF not directly downloadable.)

## What this source establishes

**KKL theorem:** For any Boolean function f: {0,1}^n → {0,1} with expectation
α, there exists a coordinate i with influence
||f_i||_2^2 ≥ c·α(1−α)·log(n)/n for an absolute constant c > 0, where f_i is
the discrete derivative in coordinate i. For balanced f (α=1/2): max_i Inf_i(f)
≥ c'·log(n)/n.

Method: harmonic analysis on the Boolean cube with the Beckner–Bonami–Gross
hypercontractive inequality.

## Why it is here

This is the canonical "maximum-from-analysis" result on the cube — the kind of
quantity problem.md says a D(S) lower bound would have to come from. It bounds
the maximum *influence of a coordinate*, i.e. a flipping sensitivity, not the
maximum internal degree of the level set S. Whether D(S) transfers from
coordinate influences is a gap, not a fact, and it is the crux of why the
influence/Fourier technique is listed as one of the four "stuck" techniques in
problem.md.

## Claim block

```claim
id: kkl-influence-balanced
statement: Every Boolean f: {0,1}^n -> {0,1} with E f = a has a coordinate of
  influence >= c·a(1-a)·log(n)/n (KKL 1988, harmonic analysis +
  hypercontractivity).
hypotheses: f Boolean, expectation a.
holds-here: true as stated (asserted); the quantity is max per-coordinate
  influence (a boundary/derivative sensitivity), NOT max internal degree D(S).
  Transfer to D(S) is unproved and is the actual gap.
status: asserted-by-source.
bearing: the standard maximum-producing Fourier result on the cube; but the gap
  between coordinate influence and D(S) is precisely the obstruction, so KKL
  alone cannot give D(S) >= omega(log n). A stronger, vertexwise combination is
  needed.
anchor: kkl-1988
```
