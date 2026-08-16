# Summary — Prime and Möbius correlations for very short intervals in F_q[x]

Source: Pär Kurlberg & Lior Rosenzweig, arXiv:1802.01215 (fixed characteristic /
large finite field). Full text: `kurlberg_rosenzweig_prime_mobius_correlations_short_intervals.full.md`.

## What this establishes

Function-field (F_q[x]) analogues of the distribution of primes and prime k-tuples
in **very short intervals** `I(f) = {f(x)+a : a ∈ F_p}` for `f` a degree-d
polynomial and `p` prime, plus cancellation in Möbius sums and their correlations
(the function-field Chowla-type sums).

- **Generic (Morse) f:** main terms of order `p` with error `O(√p)` (square-root
  cancellation).
- **A general theorem on correlations of arithmetic class functions** (Theorem 3):
  for `φ₁,…,φ_k` class functions on the symmetric group `S_d`, the correlation
  `⟨φ₁(f(x)+h₁)…φ_k(f(x)+h_k)⟩` over Morse `f` has main term `∏_i c(φ_i)` with
  explicit constants `c(φ_i)`, and square-root error — for distinct shifts `h_i ∈ F_p`.
- **Equivalence:** square-root cancellation in Möbius sums ⟺ square-root
  cancellation in Chowla-type (correlation) sums.
- **Non-generic / failure cases:** exhibits `f` with NO cancellation, and intervals
  where the "primes are independent" heuristic fails badly.
- Techniques: Katz equidistribution, Galois groups `S_d^k` for generic shifts,
  explicit Chebotarev (Prop. 8 via [12]).

## Why it matters here

This is the single most on-topic of the four function-field grounding sources for
the reopened pass's **K>1 territory**. It proves **higher-order (k-point)
correlations** of arithmetic class functions — including products of prime
indicators at separated shifts `h_1,…,h_k` — with square-root cancellation under
spectral (Katz) equidistribution hypotheses. That is precisely a K≥2 correlation
object controlled by an arithmetic/spectral input, the shape GOAL priority 2 asks
whether the fold can read.

**The transfer gap is NOT closed.** The shifts `h_i` here are *value* shifts
(`f(x)+h_i`, an additive translate of the argument), and consecutiveness is in
the *value* argument `x`, not the *degree-then-lex order* of irreducibles. The
fold's two-point object reads two irreducibles *adjacent in the lex/degree order*
with residue difference mod T² — a different, index-domain adjacency. This source
does not control that lex-consecutive pair; it controls value-shifted correlations
of a fixed polynomial's values. So it supplies a K>1 correlation theorem over
F_q but not the switch-density analogue at the fold's own order.

```claim
id: kurlberg-rosenzweig-class-function-correlations
statement: Over F_p[x], for Morse f of degree d and distinct shifts h_1..h_k ∈ F_p,
  the k-point correlation of arithmetic class functions φ_1..φ_k (prime indicators,
  Möbius, divisor functions) has main term ∏_i c(φ_i) with explicit constants and
  error O(√p); square-root cancellation in Möbius sums is equivalent to that in
  Chowla-type correlation sums; non-generic f have no cancellation.
hypotheses: Morse f (generic), distinct value shifts h_i, p prime, (p,2d)=1; a
  spectral/equidistribution (Katz) input holds.
holds-here: provides a K>=2 value-shifted correlation theorem over F_q, the shape
  GOAL priority 2 wants, but at VALUE shifts of a fixed polynomial — NOT the
  degree-ordered lex-consecutive irreducible pair the fold reads. Transfer open.
status: proved (Kurlberg–Rosenzweig 2018, arXiv:1802.01215).
bearing: strongest available higher-order-correlation theorem over F_q and the
  model-world template for "a K>1 functional controlled by a spectral input";
  the lex-consecutive switch object remains uncontrolled and is the model's own step.
anchor: research/sources/kurlberg_rosenzweig_prime_mobius_correlations_short_intervals.full.md
```

## Keyword map
function field; correlations; Möbius sums; Chowla; very short intervals; Morse
polynomial; Katz equidistribution; prime k-tuples.
