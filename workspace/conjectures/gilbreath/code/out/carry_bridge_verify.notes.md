# Carry-bridge and ν₂ reproduction — verification note

This run verifies step 1 of the adopted carry-decorrelation approach
(`research/approaches/two-s-complement-carry-decorrelation-nu2-supply.md`) and
the ν₂ reproduction it consumes. Everything is exact integer / boolean
arithmetic unless flagged "numerical" or "approximate".

## Part 1 — the two's-complement carry bridge for |a−b| (EXACT, PASS)

The composed finite transducer is two machines working on the m-bit binary
expansion:

1. **3-state MSB-first comparator** (states EQ / GT / LT) fixes the sign of
   a−b: the first differing bit from the MSB decides.
2. **2-state LSB-first borrow-subtractor** produces the magnitude via the
   two's-complement identity
       a − b ≡ a + b̄ + 1   (mod 2^m),
   where b̄ is the bitwise complement. The key point of the adopted approach:
   a subtraction **borrow** is exactly an addition **carry** of `a + b̄ + 1`,
   so the Diaconis–Fulman carry machinery applies to the |a−b| magnitude. The
   `+1` of the complement is the carry-in `cin=1`.

The composed transducer was machine-checked to equal `|a−b|` for **ALL**
`0 ≤ a, b < 2^14` — all **268,435,456** (a,b) pairs —
via a numpy-vectorized boolean bit-steps route compared against the
independent numpy `|a−b|` reference (two different routes to the same value).
Result: **0 mismatches, a<b, a=b, and a>b all included.**

- A first bug (carry-in 0 instead of 1) was caught and fixed: with `cin=0` the
  transducer returned `a−b−1` (all 2^28 pairs mismatched); with `cin=1` it
  matches exactly. This is exactly the content of the two's-complement bridge:
  the `+1` is load-bearing.
- The per-pair reusable function `lib.carry.absdiff_transducer` agrees with
  Python `abs(int)` on 4000 random pairs.

The transducer as a **finite-state computation of |a−b|** is therefore
established beyond doubt. The approach correctly does NOT claim automaticity
of the input (that was the refuted binary-carry-transducer); it only used the
transducer as exact arithmetic, which survives.

## Part 2 — ν₂(n) and w(n) from scratch (REPRODUCED, EXACT)

Definitions on the prime right diagonal through q_n (cell A_k[n−k]):

- **ν₂(n)** = number of 2s in the maximal {0,2} suffix of the diagonal body
  `diag[2:-1]` (Granville's supply quantity).
- **w(n)** = Hamming weight of the halved-gap bits
  `h_j = [(p_{j+1}−p_j)/2 mod 2]` over `j ∈ [2, n−1]` (= 1 iff gap ≡ 2 mod 4).

Computed from scratch with the run's oracle generator `lib.gilbreath`
(one row at a time), sieve to 1e6, columns n = 2..4999. The sampled table
**exactly reproduces** the earlier record `nu2_granville_check`:

```
n=50:26  n=100:42  n=200:98  n=400:203  n=800:389  n=1600:785  n=3200:1604  n=3999:2048
```
(exact match, including n=100 nu2=42 → nu2/n=0.420, the minimum of the earlier
[0.420,0.520] sampled range).

Full-range results (n = 2..4999, exact):

| quantity | value |
| --- | --- |
| ν₂ range | 0..2561 |
| w range | 0..2955 |
| ν₂/n range (all n) | [0.0000, 0.6842] |
| ν₂/n range (n≥17) | [0.2941, 0.6842] |
| worst ν₂/w | 0.0000 at n=3 (ν₂=0, w=1) |
| ν₂ ≥ w/2 violations | n ∈ {3,7,8,9,13,15} (last n=15) |
| ν₂ ≥ 0.45·n violations | last n=821 (see set in capture) |
| ν₂ ≥ w/2 over n≥17 | **TRUE** |
| ν₂ ≥ 0.45·n over n≥17 | FALSE (fails up to n=821) |

**Exactly stated.** On the sampled scale:

- `ν₂ ≥ w/2` holds on **every n ≥ 17** (all 4,983–15 = 4,968 such columns
  pass), and in fact the last violation is at n=15, so `ν₂ ≥ w/2` holds on
  **every n ≥ 16 on this data**.
- `ν₂ ≥ 0.45·n` does **not** hold on every n: it fails at scattered columns
  up to n=821 (worst low n). The relevant Route B threshold is not 0.45·n but
  `n^0.525` (exponent β>0.525), so this is not the load-bearing claim; the
  transfer `ν₂ ≥ w/2` and the fluctuation-bound `ν₂ ≈ n/2 + O(√n)` are the
  content.

Both "every n" bindings were tested on all 4,983 columns and reported with
their exact violation sets — not asserted.

## Part 3 — carry-decorrelation Markov chain (EXACT stationary density, EMPIRICAL/APPROX tracking)

The Diaconis–Fulman two-operand addition carry `c' = majority(a,b,c)` with
a,b i.i.d. Bernoulli(1/2):

- Transition matrix `T = [[3/4, 1/4], [1/4, 3/4]]`, solved exactly:
  stationary vector `π = [0.5, 0.5]`, carry density **exactly 1/2**.
- Empirical single-chain simulation over L=4,000,000 iid operand bits:
  carry density = **0.499603** — matches 1/2 (statistical error ~
  `1/√L ≈ 0.0005`).

So a 2-state Markov carry chain with Bernoulli(1/2) stationary density does
indeed give stationary count density **1/2**, matching ν₂/n ≈ 0.5.

**Exact vs approximate, precisely:**

- **Exact:** the stationary density of the two-operand carry chain is 1/2.
- **Approximate / empirical:** ν₂/n is NOT identically 1/2; it fluctuates in
  [0.2941, 0.6842] over n≥17, settling near 0.5 at large n (0.5121 at n=3999).
  The equality "ν₂/n = 1/2" is a *tendency*, not an identity.
- **Tracking, not equality:** the two's-complement borrow chain fed by the
  actual consecutive halved prime gaps (a=G[i], b=G[i+1], width m=8) gives
  borrow density **0.5646** — the same ballpark as ν₂/n ≈ 0.5 but not equal
  to it, exactly as the "tracks" claim in the approach states. The gap between
  0.5646 (real-bit borrow density) and 0.5 (iid stationary) is the empirical
  decorrelation gap the approach's mixing claim must close; it is positive and
  modest (≤ 0.065).

The carry/borrow chain is the right automaton (Part 1 proved the bridge
exactly) and its stationary density is the right reference value (1/2), but
the *input* to the chain on the real primes is not i.i.d. — the measured
0.5646 vs 0.5 is the concrete amount of mixing/non-concentration that the open
decorrelation statement would have to supply. This is the honest boundary of
the empirical evidence, consistent with the approach's own falsifier.

## Files

- `code/lib/carry.py` — reusable transducer (comparator, borrow-subtractor,
  absdiff_transducer, borrow_chain, add_carry_chain). Exhaustive-checked.
- `code/carry/verify_transducer.py` — Part 1 exhaustive check (2^28 pairs).
- `code/carry/reproduce_nu2.py` — Part 2 ν₂/w recomputation.
- `code/carry/markov_carry_chain.py` — Part 3 Markov chain.
- `code/out/carry_bridge_verify.captured.txt` — full consolidated output.

```claim
id: carry-bridge-exhaustive
statement: The composed two's-complement transducer (3-state MSB comparator x
  2-state LSB borrow-subtractor with the two's-complement identity a-b = a+~b+1,
  carry-in 1) equals |a-b| for ALL 0<=a,b<2^14 — all 268,435,456 pairs — with
  0 mismatches against an independent numpy |a-b| route; a<b, a=b, a>b all
  covered. A carry-in-0 bug produced all-2^28 mismatches and was fixed by
  setting cin=1 (the '+1' of the two's complement is load-bearing).
hypotheses: none
holds-here: yes
status: checked
bearing: establishes the finite-state exact arithmetic of |a-b| (the surviving
  core of the refuted binary-carry-transducer approach) that the adopted
  carry-decorrelation approach uses; the approach does not claim input
  automaticity.
anchor: code/carry/verify_transducer.py, code/out/carry_bridge_verify.notes.md
```

```claim
id: carry-bridge-nu2-reproduction
statement: On the prime right diagonal, nu2(n) from maximal {0,2} suffix and
  w(n)=Hamming weight of halved gap bits over j in [2,n-1], recomputed from
  scratch (oracle generator, sieve 1e6, n=2..4999) exactly reproduce the
  sampled nu2_granville_check table (n=50:26,100:42,200:98,400:203,800:389,
  1600:785,3200:1604,3999:2048). On this data nu2>=w/2 holds on every n>=16
  (last violation n=15); nu2>=0.45*n fails up to n=821 (Route-B threshold is
  n^0.525, not 0.45n, so this is not load-bearing).
hypotheses: none
holds-here: yes
status: checked
bearing: reproduces the supply-side nu2 of Route B and the transfer nu2>=w/2
  over the general scale; quantifies the exact violation sets of both lower
  bounds rather than asserting them.
anchor: code/carry/reproduce_nu2.py, code/out/carry_bridge_verify.notes.md
```

```claim
id: carry-markov-stationary-1-2
statement: The two-operand addition carry chain c'=majority(a,b,c) with a,b
  iid Bernoulli(1/2) has transition matrix [[3/4,1/4],[1/4,3/4]] and exact
  stationary vector [1/2,1/2] (carry density exactly 1/2); empirical single-
  chain simulation over 4e6 iid bits gives 0.499603. The real-prime borrow
  chain on consecutive halved gaps (m=8) gives density 0.5646 — same ballpark
  as nu2/n~0.5 but not equal, quantifying the decorrelation (non-iid) gap the
  approach's mixing claim must close.
hypotheses: iid Bernoulli(1/2) operand bits for the exact 1/2; otherwise
  empirical
holds-here: no (exact 1/2 needs iid inputs; real prime-gap bits are not iid)
status: checked
bearing: confirms the stationary-density 1/2 as the exact reference of the
  carry-decorrelation approach and measures the real-bit borrow density 0.5646
  against it; the equality is a tendency, not an identity.
anchor: code/carry/markov_carry_chain.py, code/out/carry_bridge_verify.notes.md
```
