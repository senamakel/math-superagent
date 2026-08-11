# Cabanillas, "A variant of Ostrowski numeration" — arXiv:1904.01874v2

Source: https://arxiv.org/pdf/1904.01874 (full text read). This is the **primary
source** for this run: it supplies the exact algorithm that replaces the
(unscalable) scan for the PE591 answer.

## What it establishes (with locations)

- **defines a variant of Ostrowski α-numeration** (`§2.3`, Def. 4) coding all
  integers and all reals of `[0,1)` with the same α-admissible digit sequence.
  Digits `d_k ∈ {0..a_k}` with the Markovian-style condition
  `d_k = 0 ⇒ (d_{k-1}=a_{k-1} or d_i=0 ∀i≥k)` (differs from classical Ostrowski).

- **δ-sequence** (`§2.3`): `δ_{-1}=1, δ_0=α, δ_k = -a_k δ_{k-1}+δ_{k-2}`,
  `δ_k = |q_k α − p_k|`, strictly decreasing to 0.

- **Algorithm 3(ii) — α-numeration of a real β∈[0,1)**:
  `b_k = min(a_k, ⌈β_{k-1}/δ_{k-1}⌉)`, `β_k = b_k δ_{k-1} − β_{k-1}`, `β_0=β`,
  `k=1,2,…`. Output `(b_k)` is the α-numeration of β.

- **Def. 6** `§4.3`: `{nα}` is a *best α-approximation* of β iff
  `||nα−β|| < ||kα−β||` for all `0 ≤ k < n`. A best α-approximation is always a
  best **right** or best **left** α-approximation.

- **Prop. 9** `§4.3` (best *right* positive approximations, `{nα} ≥ β`):
  `n = 0`; terminal prefix `n = Σ_{i=1}^{s} b_i q_{i-1}` if expansion terminates;
  and `n = Σ_{i=1}^{2k−1} b_i q_{i−1} + j·q_{2k−1}`, `j ∈ {0,…,b_{2k}−1}`, `k≥1`.

- **Prop. 10** `§4.3` (best *left* positive approximations, `{nα} ≤ β`):
  terminal prefix `n = Σ_{i=1}^{s} b_i q_{i−1}`; and
  `n = Σ_{i=1}^{2k} b_i q_{i−1} + j·q_{2k}`, `j ∈ {0,…,b_{2k+1}−1}`, `k≥0`.

  (Here `(q_i)` are the convergent denominators, `q_{-1}=0,q_0=1`; `(b_i)` the
  α-numeration of β.)

- **Thm. 1** `§4.1`: three-distance theorem with precise gap lengths in terms of
  the `δ_k` and convergents.

## Why it applies here / what it lets us compute

Set `α = {√d} = √d − ⌊√d⌋ ∈ (0,1)` (turning `b·√d` into a circle rotation mod 1)
and `β = {π} ≈ 0.14159…`. For fixed `b`, the best integral part is
`a = round(π − b·√d)`, and the error is `||b·√d − π||_Z = ||b·α − β||_Z`. Both
`b` signs matter (approximation to `+β` via `β`, to `−β` via `1−β`).

Cabanillas Def. 6 + Prop. 9/10 give an exact, **finite** (`O(log L)`) candidate
list for the global minimum of `||nα−β||` over `n ≤ L`: the union of the Prop 9
and Prop 10 records, restricted to `n ≤ L`. `α` is irrational here (√d
non-square), so the irrational-irrational case (Prop. 9/10 Case 2) applies.
This is the scalable method for `n = 10^13` — no scan of `[0,L]`.

## Hypotheses check
- `α` irrational: holds (`α={√d}`, d non-square).
- `β ∈ [0,1)`: holds (`β={π}`).
- The propositions enumerate **positive** `n` for β and, by symmetry, for `1−β`/
  negative `n` (paper §2.4 gives α-numeration of negative integers and the
  complement `β → 1−β`). PE591 needs both sides ⇒ consider β **and** `1−β`.

## What it does not settle
- Not a numeric PE591 answer (paper is pure theory).
- Requires high-precision π for the α-numeration digits, and exact integer
  convergents; the paper does not address finite-precision stops.
- Sections §3.2/§4.4 (D_α, counting) are not needed here.

## Verification status
The run's `toolkits/ostrowski_verify.py` checks these candidate sets against
brute force on small `(α,β,L)`. I could not execute code in this session, but the
harness exists and reproduces the structure; final numeric confirmation is a
remaining task.
