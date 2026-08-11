# Inhomogeneous Diophantine Approximation on a Circle Rotation:
Structure of record-holding b for min ||b·α − θ||_Z

## Problem restated

For non-square integer `d`, set `α = {√d} = √d − ⌊√d⌋ ∈ (0,1)`. We must find, among
`b ∈ [0, L]` with `L ≈ 10^13/√d`, a `b` that minimizes

    f(b) = ||b·√d − π||_Z  =  distance of (b·√d − π) to the nearest integer.

Because adding/subtracting an integer does not change the distance, and because in the
originating problem (Project Euler 591) the sign of `b` is free, this reduces to the
inhomogeneous rounding problem on the **circle rotation** `x ↦ x+α (mod 1)`, viewed mod
`1`:

    f(b) = ||b·α − β||_Z  where  β = {π} ≈ 0.14159265…  (α = {√d}, mod 1).

This is **inhomogeneous** Diophantine approximation: minimize the circular distance of an
orbit point `{bα}` to a fixed target `β`, over a finite horizon `b ≤ L`.

The "record minima" the question asks about are the values of `b` at which `f(b)` is
strictly smaller than at every earlier `b` — the "closest returns to a point of a
rotation." The question asks whether these `b` are always semiconvergent denominators
`m q_k + q_{k−1}`, `0 ≤ m ≤ a_{k+1}`, of `α`'s continued fraction. **Answer: only in
the homogeneous case (target 0). In the inhomogeneous case the record-holders are the
α-numeration prefix sums given by Cabanillas' Propositions 9–10 (below).** They reduce
to semiconvergent denominators only for special targets.

---

## 1. The three-distance / three-gap theorem

**Statement (Steinhaus conjecture, proved 1950s by Sós, Surányi, Świerczkowski).**
For any irrational `α` and any integer `N`, the points
`0, {α}, {2α}, …, {Nα}` divide the circle into arcs whose lengths take **at most three
distinct values**, and when there are three, the largest equals the sum of the other two.
For rational `α` the same holds up to the period.

Sources:
- https://en.wikipedia.org/wiki/Three-gap_theorem
- van Ravenstein, *The Three Gap Theorem (Steinhaus Conjecture)*, J. Austral. Math. Soc.
  A 45 (1988) 360–370, https://doi.org/10.1017/s1446788700031062
- Marklof–Strömbergsson, *The three gap theorem and the space of lattices*,
  https://doi.org/10.48550/arxiv.1612.04906
- Hamada, *A concise geometric proof of the three distance theorem*,
  https://doi.org/10.48550/arxiv.2308.11999

**Precise gap lengths (as used by Cabanillas, arXiv:1904.01874, Thm 1).**
Let `α = [0;a_1,a_2,…]`, convergents `p_n/q_n`, `δ_n = (−1)^n(q_n α − p_n) > 0` (decreasing
to 0). Let `s` be the lowest integer with `N ≤ q_s + q_{s−1}`.

- if `N = q_s + (1−i) q_{s−1}`, `i ∈ {0,…,a_s−1}`: gaps take **two** values
  `δ_s + i δ_{s−1}` and `δ_{s−1}`;
- otherwise they take **three** values
  `δ_{s−1}`, `δ_s + i δ_{s−1}`, `δ_s + (i+1) δ_{s−1}`.

**Why it matters here.** The three-gap theorem describes the geometric distribution of a
prefix of the orbit. It tells us the orbit points near a target `β` are spaced by the
`δ_n`-scale gaps, which is precisely what forces the record-holders to be few and
structured. It is, however, a *homogeneous* statement (gaps of `{nα}` itself, counts of
points, not a minimizer for a target); the sharp two-sided minimizer per `b` comes from
the inhomogeneous results in §3. The Berthé–Imbert algorithm (§3.2) is explicitly built
on the three-gap theorem.

---

## 2. Closest returns, Ostrowski representation, best approximations, semiconvergents

### 2.1 Ostrowski numeration of integers
(Ostrowski 1922; https://en.wikipedia.org/wiki/Ostrowski_numeration)

Every integer `N ≥ 0` has a unique representation

    N = Σ_{k=1}^{m} b_k q_{k−1},   with
        0 ≤ b_1 ≤ a_1 − 1,
        0 ≤ b_k ≤ a_k  (k ≥ 2),
        b_k = 0 whenever b_{k+1} = a_{k+1}   (Markovian / "no consecutive max" condition),

where `(q_k)` are the denominators of the CF convergents of `α`. For `α = golden ratio`
(all `a_k = 1`) this is Zeckendorf representation (Fibonacci).

### 2.2 Best approximations and semiconvergents
(Lagrange; standard references Cassels, Khinchin; survey MDPI 2673-9909/2/3/23)

- A fraction `p/q` is a **best approximation of the second kind** if it minimizes
  `|qα − p|` among all `0 < q' ≤ q`. The best approximations of the second kind are
  **exactly the convergents** (Lagrange's theorem).
- A fraction is a **best approximation of the first kind** if it minimizes `|α − p/q|`
  among `0 < q' ≤ q`. These are exactly the convergents **and** **semiconvergents**
  (intermediate fractions):

        (t p_{n+1} + p_n) / (t q_{n+1} + q_n),   1 ≤ t ≤ a_{n+1}.

  So the denominators appearing are the **semiconvergent denominators**
  `m q_k + q_{k−1}` with `0 ≤ m ≤ a_{k+1}` (including the convergent denominations
  `m=0` and `m=a_{k+1}`, which give `q_{k−1}` and `q_{k+1}`).

### 2.3 Are the record-holders always semiconvergent denominators? —— No, not in general.

The homogeneous best-approximation theory says that the points `{nα}` closest to `0`
occur at the semiconvergent denominators `m q_k + q_{k−1}`. This is the classical
"closest returns to the origin" fact (see e.g. the closest-return discussion in
de Faria–de Melo, DOI 10.1090/s0894-0347-99-00324-0, where "denominators q_n of the
convergents are the closest return times of the orbit to itself").

But our target is an **arbitrary point** `β`, not `0`. Once `β` is not `{nα}` for any
`n` (as for `β = {π}`, which is irrational), the record-holders of `||bα − β||_Z` are
**not** generally of the form `m q_k + q_{k−1}`. The correct structure is given by the
α-numeration of `β` (Cabanillas, §3 below): each record-holder is a prefix
`Σ b_i q_{i−1}` of the α-numeration plus a multiple of a convergent denominator. Only
when `β` has a very special α-numeration does this coincide with a plain semiconvergent
denominator.

In short: **semiconvergents organize the homogeneous (target=0) records; the
inhomogeneous records need the Ostrowski/α-numeration machinery with target-dependent
prefixes.**

---

## 3. Exact O(log L) algorithm (the primary answer)

### 3.1 Cabanillas (arXiv:1904.01874) — both-sided record-holders

This paper gives the exact, complete set of `b` achieving new record minima of
`||bα − β||` from **both** sides, which is what we need for the minimum over `b ∈ [0,L]`.

**Setup.** `α ∈ (0,1)` irrational, CF `[0;a_1,a_2,…]`, convergents `p_n/q_n`; the
`δ`-sequence `δ_{−1}=1, δ_0=α, δ_k = −a_k δ_{k−1} + δ_{k−2}` (so `δ_k = |q_k α − p_k|`,
decreasing to 0).

**Algorithm 3(ii) — α-numeration of the target `β ∈ [0,1)`.** Compute digits `(b_k)`
and remainders `(β_k)` by

    b_k = min(a_k, ⌈β_{k−1}/δ_{k−1}⌉),   β_k = b_k δ_{k−1} − β_{k−1},   k = 1,2,3,…
    (β_0 = β; note δ_0 = α so b_1 = min(a_1, ⌈β/α⌉)).

The sequence `(b_k)` is the α-numeration of `β`.

**Proposition 9 — best RIGHT (positive) approximations** (those `{nα} ≥ β`, i.e. `nα` at
or above target): the record points are

    n = 0,
    n = Σ_{i=1}^{s} b_i q_{i−1}   (only if the α-expansion of β terminates, b_k=0 for k>s),
    n = Σ_{i=1}^{2k−1} b_i q_{i−1} + j·q_{2k−1},   j ∈ {0,…,b_{2k}−1},   k ≥ 1.

**Proposition 10 — best LEFT (positive) approximations** (those `{nα} ≤ β`): the record
points are

    n = Σ_{i=1}^{s} b_i q_{i−1}         (if expansion terminates),
    n = Σ_{i=1}^{2k}   b_i q_{i−1} + j·q_{2k},   j ∈ {0,…,b_{2k+1}−1},   k ≥ 0.

**Remarks.**
- The *global* minimum over `[0,L]` of `||nα − β||` is attained at one of the finitely
  many candidates listed, restricted to `n ≤ L`. There are `O(log L)` candidates.
- The candidate prefixes are the **α-numeration prefixes** `Σ b_i q_{i−1}` of `β`, plus
  `j`-multiples of convergent denominators — **not** the plain semiconvergent
  denominators of `α`. This is the precise sense in which §2.3's "no" is answered: the
  structure is target-dependent.

**Correctness of the record-holder concept.** Cabanillas defines (Def. 6): `{nα}` is a
*best (two-sided) α-approximation* of `β` iff `||nα − β|| < ||kα − β||` for all
`0 ≤ k < n`. A best approximation is always a best *right* or best *left*
approximation, and the propositions enumerate exactly those. So the record-holders of
`||bα − β||` are precisely the union of Prop 9 and Prop 10 candidates.

Source: arXiv:1904.01874 PDF (read in full), Propositions 9, 10, Algorithm 3,
Def. 6. URL: https://arxiv.org/abs/1904.01874 (also https://doi.org/10.48550/arXiv.1904.01874)

### 3.2 Berthé–Imbert (DMTCS 2009) — one-sided best-left sequence

A complementary, well-cited algorithm computes the *left-only* inhomogeneous best
approximations (relevant if one wants the target approached from one side).

**Algorithm 2 / Props. 4–6** (DMTCS 11:1 (2009) 153–172,
https://dmtcs.episciences.org/450/pdf). Let `f_n = |q_n α − p_n|` with
`f_{−1}=1, f_0=α, f_{n} = a_{n+1} f_n + f_{n+1}`. Iterating:
choose (uniquely) `n_i, c_i, e_i` with
`β − (k_i α − l_i) = c_i f_{n_i} + f_{n_i+1} + e_i`, `0 < e_i ≤ f_{n_i}`; then
- if `n_i` even: `(k_{i+1},l_{i+1}) = (k_i + q_{n_i}, l_i + p_{n_i})`;
- if `n_i` odd:  `(k_{i+1},l_{i+1}) = (k_i − c_i q_{n_i} + q_{n_i+1}, l_i − c_i p_{n_i} + p_{n_i+1})`.

The `(k_i, l_i)` enumerate the inhomogeneous **best left** approximations of `β` by
`kα − l` (Prop 4). For bounded-bit-length targets it runs in `O(log log x)` iterations
(Prop 6).

Its limitation for our problem: it is *one-sided*. The two-sided circular minimum
`||nα − β||` needs both sides, which Cabanillas' Prop 9/10 provides directly.

---

## 4. Which method to use here

For PE591-like data (`d < 100`, `n = 10^13`, several dozen independent `α = {√d}` and the
same `β = {π}`):

1. For each `d`: compute CF of `α = √d − ⌊√d⌋` (periodic, so cheap), the convergent
   denominators `q_k` and the `δ_k`, until `q_k` exceeds `L ≈ 10^13/√d`.
2. Run Cabanillas Algorithm 3(ii) to get the α-numeration digits `(b_k)` of
   `β = {π}` (with high-precision arithmetic for `π`).
3. Enumerate O(log L) candidates from Prop 9 and Prop 10 (both signs/parities), keep
   those `≤ L`, and take the minimum of `||nα − β||`.
4. For the PE591 quantity, the winning `n` gives `b` and then
   `a = round(π − n·√d)`; the reported value is `|a|`. Positive and negative `b` both
   matter (approximation to `+β` and `−β`), handled by considering `β` and `1−β` (i.e.
   left/right on both sides).

Exact integer arithmetic: the convergents `(q_k, p_k)` are computed in exact integers,
and `δ_k = |q_k α − p_k|` requires precision only about as large as `10^13` (double is
generally enough; use exact rational/MPFR for safety). This is an `O(log L)` method and
does not scan `[0,L]`.

---

## Sources

1. **Cabanillas, *A variant of Ostrowski numeration* (2019)**
   https://arxiv.org/abs/1904.01874 ; https://doi.org/10.48550/arXiv.1904.01874
   — Propositions 9, 10, Algorithm 3, Def. 6: exact both-sided record-holders and the
   α-numeration of the target; also Thm 1 (three-distance) and §1.4 (best left/right =
   semiconvergents) primary.
2. **Berthé & Imbert, *Diophantine Approximation, Ostrowski Numeration and the
   Double-Base Number System*, DMTCS 11:1 (2009) 153–172**
   https://dmtcs.episciences.org/450/pdf — Algorithm 2 / Props 4–6: one-sided best-left
   inhomogeneous approximations, O(log log x), built on three-gap theorem.
3. **Wikipedia: Three-gap theorem** https://en.wikipedia.org/wiki/Three-gap_theorem
   — statement of the Steinhaus conjecture and history.
4. **Wikipedia: Ostrowski numeration**
   https://en.wikipedia.org/wiki/Ostrowski_numeration — integer/real Ostrowski bases.
5. **van Ravenstein, *Three Gap Theorem* (1988)**
   https://doi.org/10.1017/s1446788700031062 — gap-length statement via continued
   fraction.
6. **Marklof–Strömbergsson, *The three gap theorem and the space of lattices***
   https://doi.org/10.48550/arxiv.1612.04906 — lattice proof of three-gap.
7. **MDPI continued-fraction survey (semiconvergents, best approx. 1st/2nd kind)**
   https://www.mdpi.com/2673-9909/2/3/23 — Lagrange: convergents = best 2nd kind;
   convergents+semiconvergents = best 1st kind; Legendre.
8. **de Faria–de Melo, *Rigidity of critical circle mappings II* (JAMS 1999)**
   https://doi.org/10.1090/s0894-0347-99-00324-0 — closest-return structure via
   convergent denominators (homogeneous case).

## Evidence caveats

- The Cabanillas statements are quoted from direct reading of the arXiv PDF (the full
  text was downloaded and read); this is the strongest evidence and directly resolves
  the "are they semiconvergents?" question (no, in general).
- The Berthé–Imbert algorithm is quoted from reading the DMTCS PDF.
- The three-gap precise lengths follow from van Ravenstein and from Cabanillas Thm 1.
- No claim here is a Project Euler answer; the task explicitly asked only for the
  underlying theory and algorithms, not the numeric value.
