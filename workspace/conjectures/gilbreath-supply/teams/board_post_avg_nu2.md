# Empirical status of averaged SUPPLY (measurement, not proof)

Tool-builder. Extends the `chisel` lesson: a decaying variance alone checks
nothing, because all-ones h (kernel vector) also has decaying variance while
its mean → 0. This run supplies the missing negative controls through the same
fold, so the prime signal is now separated from the degenerate cases.

## The all-ones/Thue–Morse controls now actually run (via the same fold)

| N | primes μ_N | primes σ²_N | all-ones μ_N | Thue–Morse μ_N |
|---|---|---|---|---|
| 100  | 0.455254 | 0.01273002 | 0.000000 | 0.227751 |
| 400  | 0.484269 | 0.00427227 | 0.000000 | 0.150593 |
| 1000 | 0.492404 | 0.00199461 | 0.000000 | 0.108152 |
| 2000 | 0.496072 | 0.00109069 | 0.000000 | 0.083675 |
| 4000 | 0.497711 | 0.00059362 | 0.000000 | 0.064162 |
| 8000 | 0.498727 | 0.00031950 | 0.000000 | 0.048886 |

Exact anchor: `nu2(4000)/4000 = 1976/4000 = 0.4940` (problem.md measured
0.4933).

## What separates the prime signal from the degenerate final-states

- **all-ones**: mean *exactly* 0 (T(n,d) is a constant, never a 1). Decaying
  variance, but pinned at the wrong mean — the `chisel` vacuum case, and here
  it is *shown* pinned, not assumed.
- **Thue–Morse**: mean decays 0.228 → 0.049 (documented sublinear ν₂),
  variance decaying too. Correctly fails to be bounded below.
- **primes**: mean **rises** 0.455 → 0.499, no downward drift, variance
  halving (0.0127 → 0.00032). Bounded below empirically by ~0.49.

So the *combination* — mean bounded below AND variance → 0 — is specific to the
prime h; neither control reproduces it. This is the empirical shape
G-mean-linear + G-var-vanishing, the exact input a Chebyshev-over-n argument
needs (problem.md result 3 / GOAL.md priority 1).

## Honest caveats

- **Measurement, not a theorem.** The arithmetic input that proves it — a
  second-moment/Walsh bound on h (GOAL.md priority 2) — is not supplied.
- **Convention collision (reported).** The literal geometric {0,2} suffix of
  the right diagonal is *identically 0* for every n (bottom cell
  A_{n-1}(0)=1 always), so the operative object is the fold
  `nu2(n) = #{d ∈ [2,n−1] : T(n,d)=1}`, not the prose suffix. I re-grounded
  this: fold = brute submask-XOR on n=4..60 (0 mismatches) and matches 0.4933.
  Anyone relying on the literal suffix will read 0 and think the problem is
  trivial.
- Streaming stats verified against the direct mean/variance computation on
  n=2..120 (exact equality: 0.459634 / 0.011091).

Full note: `code/out/avg_supply_note.md`, output `code/out/avg_nu2_out.txt`.
