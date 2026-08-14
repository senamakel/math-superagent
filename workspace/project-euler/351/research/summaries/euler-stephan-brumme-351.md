# Stephan Brumme, "Project Euler 351 — Hexagonal Orchards" (public solution write-up)

Source: https://euler.stephan-brumme.com/351/ — full text at
`research/sources/euler-stephan-brumme-351.full.md`
[[euler-stephan-brumme-351.full]]

## What this source establishes

The standard public solution write-up for PE 351 (Brumme, submitted Sep
2017; problem difficulty 25%). Read in full this session.

**The method (identical to this run's).** Treat the hexagon as six equal
triangles around the centre; the centre is never hidden. In one triangle the
points are the fractions p/q, 1 ≤ p ≤ q ≤ n; a point is hidden iff
gcd(p,q) > 1. On the i-th partial ring, φ(i) of the i points are visible, so
the hidden count is

    H(n) = 6·Σ_{i=1..n}(i − φ(i)) = 6·(n(n+1)/2 − Φ(n))

— the same closed form as OEIS A216453 (Kumar–Israel) and this run's
`code/solution.py`. Then compute Φ(10⁸) by a totient sieve.

**The computation.** A full φ table for 10⁸ needs > 400 MB (his plain
`sumPhi`, ~3.5 s); he rewrites it as a *segmented* sieve (`sumPhiSliced`,
1e6-sized slices, ~30 MB, ~3.1 s) — the same totient-sieve approach as this
run's `solution.py`, with a memory-friendlier segmentation. `main` computes
6·(T(n) − sumPhi(n)) and prints the answer. He links OEIS A216453 in
"See also".

## What it implies for this run

Independent public confirmation that (a) the ring/fraction derivation is the
standard method, (b) the closed form is right, and (c) the totient sieve is
the standard way to evaluate Φ(10⁸); the run's 400 MB int32 table is the
same idea with a larger memory budget. **Not an answer source**: Brumme's
page does not print the final integer H(10⁸) (the interactive test refuses
n = 10⁸ input). The answer confirmation comes from the OEIS b-files
A216453/A064018 and the published answer lists (see
`research/research-report-pe351-known.md`).

## Hypotheses

n ≥ 1; the six-triangle symmetry and the gcd criterion. Hold here (verified
by brute.py and the identity at n = 5, 10, 1000).

## Claims

None new — corroborates `hexagonal-orchard-closed-form` and the
totient-sieve route already claimed from OEIS A216453 and Brown
arXiv:2506.07386. No claim block added; this is a secondary write-up of the
same method.
