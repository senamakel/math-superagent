# Computed findings for PE1006 (verified, checked)

This note records the run's own computed results beside the programs that produced
them. Each is `status: checked` (verified computation, exact integer arithmetic).
Source-led results (Sturmian structure, Perrin–Restivo) are in the summaries under
`research/summaries/` and are not duplicated here.

## Extension formula — an exact recurrence for Psi(k+1)

`task_state_recurrence.py` (reads `structure.json`) establishes, for every
transition k -> k+1 among k = 1..59:

Let R(k) be the unique **right-special** length-k factor (extends to both w0 and w1);
v_R(k) its decimal value; N1(k) the number of length-k factors w with w·'1' a factor of
length k+1; P1(k) the sum of the values of those factors. Then

    Psi(k+1) = 100 ( Psi(k) + v_R(k)^2 ) + 20 P1(k) + N1(k).

Rationale: each length-k factor extends by a single final letter; exactly one (the
right-special R) extends both ways, every other exactly one way. Appending 0 gives
value 10·v_w, appending 1 gives 10·v_w + 1.

`Extension formula held for every k transition: True` for all 59 transitions checked.

This is an EXACT recurrence but not a closed recurrence in Psi(k) alone: it needs the
extra state (v_R, P1, N1). Closing the evolution of that state is the remaining step.

```claim
id: PE1006-extension-formula
statement: Psi(k+1) = 100(Psi(k) + v_R(k)^2) + 20 P1(k) + N1(k), where R(k) is the unique right-special length-k factor, P1(k) = sum of values of length-k factors w with w1 a factor, N1(k) = their count.
hypotheses: length-k factors of the Fibonacci word (Sturmian set, slope 1/phi^2); right-special factor unique per length.
holds-here: yes — verified exactly for every k = 1..59 transition against direct Psi(k+1).
status: checked
bearing: an exact state recurrence; the core of any poly-log(k) evaluation, needing only that the state (Psi, v_R, P1, N1) evolution be closed.
follows-from: PR-consecutive-factors-lex
anchor: code/out/computed-findings.md (task_state_recurrence.py)
```

## Psi(1..150) admits NO constant-order linear recurrence

`find_small_recurrence.py` tests, for each order d in 1..40, whether rational
coefficients c_0..c_{d-1} exist with
a[k] = c_0 a[k-1] + ... + c_{d-1} a[k-d] holding EXACTLY for all 150 terms. Consistency
decided by rank over several large primes. Result: **no order d in 1..40 gives a
consistent system over any tested prime.** Berlekamp–Massey order on 150 terms is 75
= n/2, the degenerate ceiling.

```claim
id: PE1006-no-loworder-linear-recurrence
statement: No constant-coefficient rational linear recurrence of order <= 40 fits Psi(1..150) exactly (rank-inconsistent over every large prime); BM order 75 = n/2 is the degenerate ceiling.
hypotheses: exact Psi(k) for k = 1..150 (code/out/psi_data_1_150.txt).
holds-here: N/A — this is a negative structural fact about the sequence.
status: checked
bearing: rules out "matrix-exponentiate a fixed constant-order recurrence in k"; whatever recurrence exists is in extra state / is piecewise in the Fibonacci/Zeckendorf structure of k.
anchor: code/out/computed-findings.md (find_small_recurrence.py, find_order_41_75.py, check_d75.py)
```

## Modular structure of M = 101001001

`task_a_modular.py`, `modular/modA_fast.py`, and an independent direct check all agree:

- M is **prime** (sympy + naive trial division to sqrt = 10049, no divisor).
- M−1 = 101001000 = 2^3 · 3 · 5^3 · 131 · 257; Legendre(5/M) = 1.
- ord_10(M) = **50500500**, verified minimal (divides M−1); 10^k mod M has period 50500500.
- Pisano period pi(M) = **101001000**, verified minimal (divides M−1).

```claim
id: PE1006-modular-structure
statement: M = 101001001 is prime; M-1 = 2^3·3·5^3·131·257; ord_10(M) = 50500500 (minimal); Pisano(M) = 101001000 (minimal). Legendre(5/M)=1.
hypotheses: none.
holds-here: yes.
status: checked
bearing: 10^(2e) mod M has period 50500500/gcd(2,50500500) = 25250250; relevant to evaluating powers of 10 in any closed form / recurrence over Z/M.
anchor: code/out/computed-findings.md (task_a_modular.py, modular/modA_fast.py)
```

## r(k) = Psi(k) mod M has no small eventual period

`task_b_period.py`: pure period (preperiod 0) none; `task_b_rigorous.py`: a search
requiring ≥40 aligned comparisons found **no** candidate (pre, T) with period < 150.
The (0, 150) row reported by modB is vacuous (the whole window), not a genuine period.

```claim
id: PE1006-no-small-eventual-period
statement: r(k) = Psi(k) mod 101001001 for k = 1..150 has no genuine eventual period with period < 150 (a ≥40-aligned-comparison search finds none).
hypotheses: exact r(1..150).
holds-here: N/A — negative structural fact about the modular sequence.
status: checked
bearing: rules out a simple "Psi mod M is eventually periodic in k" shortcut to r(10^18); the answer must come from the exact recurrence, not a modular period.
anchor: code/out/computed-findings.md (task_b_rigorous.py)
```

## Oracle agreement

`brute.py` reproduces both worked examples exactly (Psi(3)=20302, Psi(10)≡10699667 mod
M). `data.py` extends to Psi(1..150) and agrees with brute.py on every k in 1..30, and
the count k+1 holds for every k in 1..150. These are the oracle the method must match.

```claim
id: PE1006-oracle-agreement
statement: brute.py reproduces Psi(3)=20302 and Psi(10) ≡ 10699667 (mod 101001001); data.py computes Psi(1..150), agrees with brute on k <= 30, and count == k+1 holds for every k in 1..150.
hypotheses: none.
holds-here: yes.
status: checked
bearing: establishes the oracle dataset the real method must reproduce; any derived Psi(k) must match these 150 terms.
anchor: code/out/computed-findings.md (brute.py, data.py, psi_data_1_150.txt)
```
