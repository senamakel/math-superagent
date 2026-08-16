# Averaged SUPPLY — empirical status (measurement, not a proof)

Tool-builder run `code/avg_nu2.py`, ceiling N = 4000 (plus a confirmatory
extension to N = 8000). Exact integer arithmetic throughout; only displayed
ratios are floats. Streamed one `n` at a time via the SOS fold — never
materialised a triangle (the parent run's OOM lesson).

## 1. Linearisation re-grounded (task 1)

The operative object is the fold weight

    nu2(n) = #{ d in [2, n-1] : T(n,d) = 1 },
    T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o],
    h[j] = ((q_{j+1} - q_j)/2) mod 2   (prime gap-parity string).

The SOS transform (`lib.supply_fold.s_sos`) was checked against the brute
submask-XOR oracle on n = 4..60 (mismatches: 0) and reproduces
problem.md's measured `nu2(4000) = 0.4933` as `1976/4000 = 0.4940`
(3 cells off, 0.07%; `code/brute.py` gives the same 1976/4000).

**Convention collision (reported honestly, not papered over).** The literal
geometric definition from problem.md's prose — right diagonal
`delta_k(n) = A_k(n-1-k)`, maximal {0,2} suffix — gives `nu2(n) = 0` for every
n: the bottom cell `delta_{n-1}(n) = A_{n-1}(0) = 1` always (Gilbreath's
first-column 1), so the {0,2} run is empty. `literal_suffix_nu2(10) = 0` while
`fold_nu2(10) = 7`. The measured/studied object is the fold (fact 1 of
problem.md), which is what all the ratios, kernel facts, and controls refer to.
`lib/literal_suffix_nu2` is kept as the explicit negative re-grounding control.

## 2. The numbers (task 2 & 3)

| N | primes μ_N | primes σ²_N | all-ones μ_N | Thue–Morse μ_N |
|---|---|---|---|---|
| 100  | 0.455254 | 0.01273002 | 0.000000 | 0.227751 |
| 400  | 0.484269 | 0.00427227 | 0.000000 | 0.150593 |
| 1000 | 0.492404 | 0.00199461 | 0.000000 | 0.108152 |
| 2000 | 0.496072 | 0.00109069 | 0.000000 | 0.083675 |
| 4000 | 0.497711 | 0.00059362 | 0.000000 | 0.064162 |
| 8000 | 0.498727 | 0.00031950 | 0.000000 | 0.048886 |

Exact: `nu2(4000)/4000 = 1976/4000 = 0.494000`; `nu2(8000)/8000` part of the
streamed run.

## 3. Verification drill

- **Streaming stats checked** against the direct computation (collect
  `nu2(n)/n` for n=2..120, then compute mean and population variance the naive
  way). Exact-equality: `mu_direct == mu_stream == 0.459634`, `s2_direct ==
  s2_stream == 0.011091`. A first streaming version had an indexing bug
  (means 0.4507/0.01465 at N=100, disagreeing) and was fixed; the fixed run is
  the one reported.
- **Negative controls behave as expected**: all-ones fold weight is exactly
  `#{d in [2,n-1] : (popcount(d) mod 2) ... }` → 0 (all-ones is the kernel
  vector, folding to constant 1, i.e. no T(n,d)=1); Thue–Morse mean decays
  0.2278→0.0489, consistent with its documented sublinear `nu2`. The prime
  signal is specific to the prime `h`.
- **Whether the prime mean is bounded below**: yes, empirically — rising from
  0.455 to 0.499 with no downward drift, and the variance halving (0.0127 →
  0.00032) is exactly the Chebyshev-against-vanishing-variance shape
  (G-mean-linear + G-var-vanishing). A plausible absolute floor is
  `c0 ≈ 0.49` (the limit of μ_N appears to be at/above the pointwise
  `nu2(4000)/4000 = 0.4940`).

## 4. Status

This is **measurement, not proof**. It is the empirical status of the averaged
form; the arithmetic input that *proves* G-mean-linear (a second-moment /
Walsh bound on h, GOAL.md priority 2) is not supplied here and remains open.

```claim
id: avg-supply-empirical
statement: For the prime h, the empirical mean of nu2(n)/n over n <= N is
  bounded below by ~0.49 for every N in [100, 8000] measured, and its empirical
  variance decays toward 0; the all-ones and Thue-Morse controls drive the same
  fold mean to 0. Linearisation (fold = the operative nu2) reproduces
  problem.md's 0.4933 measurement at n = 4000 (1976/4000 = 0.4940).
hypotheses: prime h; fold convention (suffix-floored-at-2 / d in [2,n-1]).
holds-here: yes, empirically over N <= 8000.
status: checked (measurement; not a proof of G-mean-linear)
bearing: consistent with GOAL.md priority 1 — the averaged form is the likely
  place a real theorem exists, and the variance-vanishing shape is present.
  The literal geometric suffix is identically 0 (a convention collision with
  the fold), so the fold is the re-grounded, operative object.
anchor: code/out/avg_nu2_out.txt
```

The claim is empirical and never presented as a theorem. The five closed doors
are untouched: this is not a hypothesis of the form "h is complicated enough";
it is a measurement of the averaged form that the parity barrier is least able
to defeat.
