# Berthé & Imbert, "Diophantine Approximation, Ostrowski Numeration and the Double-Base Number System" — DMTCS 11:1 (2009) 153–172

Source: https://dmtcs.episciences.org/450/pdf (full text read).

## What it establishes (with locations)

**Problem setting.** Given `x ≥ 2`, find the largest `2^a 3^b ≤ x` (best default
approximation, the key step of a greedy DBNS algorithm, Alg. 1). Taking logs with
`α = log_3 2`, `β = {log_3 x}`, this is the inhomogeneous Diophantine problem:
maximize `kα − l ∈ [0, β]`. The paper attacks it with an Ostrowski-type number
system.

**Ostrowski integer system (Prop 1, §3).** Every integer `N` is written uniquely as
`N = Σ_{k=1}^{m} b_k q_{k-1}` with `0 ≤ b_1 ≤ a_1−1`, `0 ≤ b_k ≤ a_k (k≥2)`, and
`b_k = 0` when `b_{k+1} = a_{k+1}` (Markovian/no-consecutive-max). Real-β base
(Prop 2) uses `θ_n = q_n α − p_n` with alternating signs; Prop 3 gives a
best-left base in `|θ_n|` but the paper notes (Remark 3) these digit sequences do
**not** directly yield the inhomogeneous best approximations.

**Main algorithm (Algorithm 2, §4) — inhomogeneous best-left approximations.**
Set `f_n = |q_n α − p_n|`, `f_{-1}=1, f_0=α`, `f_n = a_{n+1} f_{n+1} + f_n` (so
`f_{n-1} = a_{n+1} f_n + f_{n+1}`). Iterate `(k_0,l_0)=(0,0)`; at step `i` write
`β − (k_i α − l_i) = c_i f_{n_i} + f_{n_i+1} + e_i` with unique `n_i, c_i, e_i`
(`0 < e_i ≤ f_{n_i}`); then update
- `n_i` even: `(k_{i+1}, l_{i+1}) = (k_i + q_{n_i}, l_i + p_{n_i})`
- `n_i` odd:  `(k_{i+1}, l_{i+1}) = (k_i − c_i q_{n_i} + q_{n_i+1}, l_i − c_i p_{n_i} + p_{n_i+1})`.

**Prop 4** proves these `0 < k_i α − l_i` are *exactly* the inhomogeneous best-left
approximations of `β` (any `k`, `k_i < k < k_{i+1}`, has `kα−l < k_i α−l_i`).
**Prop 5** — the max over `k ≤ ⌊log_2 x⌋` is attained at the last `k_v ≤ ⌊log_2 x⌋`
(this is the bounded-horizon stopping rule). **Prop 6** — for `m`-bit `x` the
algorithm terminates in **O(log log x)** iterations (proof uses that `q`-denominators
grow at Fibonacci rate ⇒ `w(x) = O(log log x)`).

**Complexity/precision (Remark 2, Table 1).** Only denominators `q_i ≤ m` are needed;
double precision ≈ convergent 16 provides enough for inputs up to ~17 million bits.

**Prop 7 (§5) — signed/two-sided greedy fails** if done naively (the two-sided best
approximation need not give the largest `2^a3^b ≤ x`); the correct two-sided
strategy is: solve the best-left for `β` AND the best-right (via `1−α, 1−β`
symmetry) and take whichever side is closer.

## Hypotheses

`α ∈ (0,1)` irrational; `0 < β ≤ 1`. Here `α = {√d}` irrational holds; `β = {π}` holds.

## What it implies for this problem

A second, *independent* exact construction of the record-holders of the left-side
inhomogeneous approximation — and it is a genuine check on the run's method, not a
duplicate: it iterates a different recursion (based on the `f_n` and `c_i`) than
Cabanillas' α-numeration prefixes. The run's consolidated note
(`research/notes/inhomogeneous_record_structure.md` §3.2) describes exactly this
Algorithm 2 and correctly flags its limitation: it is **one-sided** (best-left
only), whereas PE591 needs the two-sided circular minimum `||bα − β||_Z`; Cabanillas
Prop 9/10 gives both sides directly, so it remains the primary method. The
signed/two-sided caution of Prop 7 corroborates the run's critical correction that
**both signs of b matter**.

## Does it contradict memory.md?

No — it *confirms*. The record updates (`+q_n` even; `−c_i q_n + q_{n+1}` odd with a
target-dependent `c_i`) are **not** plain semiconvergent denominators
`m q_k + q_{k-1}`, matching memory's "records are NOT semiconvergents in general"
(falsified hypothesis). And Prop 7's warning that the two-sided best approximation
can fail when naively combined corroborates why the run's both-sign solver
(β AND 1−β) reproduces the oracle while a one-sided/positive-only search gave the
wrong S.

## Verdict

Primary-corrobating source, not the primary method. It independently derives the
left-side records and motivates the both-sides handling; the run's method
(Cabanillas) covers both sides and is already verified. Keep as the independent
cross-check for the record structure.
