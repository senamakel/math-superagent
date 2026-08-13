# ROOT — Singmaster's conjecture: the landscape

This is the top-level research index for the Singmaster conjecture run. It answers
the six research questions with exact, sourced statements, and records the structure
of a minimal counterexample, the current verification bound, and the settled
restricted classes. Detail and full citations are in
`research/summaries/singmaster-literature-exact.md`; sources are under
`research/sources/`; claims in the ledger (`research/CLAIMS.md`).

**Counting convention (fixed):** `N(a)` counts all integer `(n,k)` with
`1 ≤ k ≤ n-1` and `C(n,k) = a`, counting **both mirrors** `(n,k)` and `(n,n-k)` and
including the trivial pair `C(a,1) = C(a,a-1)`. Under this convention `N(3003) = 8`.
Every bound below is convention-dependent; a "4 in the interior" under MRSTT is the
both-halves count.

## The six research questions — exact answers

1. **Singmaster 1971:** `N(a) = O(log a)` (Amer. Math. Monthly 78 (1971) 385–386;
   doi:10.2307/2316907). Mechanism: `C(2k,k) ≥ 2^k` forces `k ≤ log₂a`, and for each
   `k` the map `n ↦ C(n,k)` is injective in `n`; the reproduction records the sharper
   `N(a) ≤ 2 + 2 log₂ a`. Conjecture: `N(a) = O(1)`; Erdős suggested
   `O(log log a)` might be closer to the truth.

2. **Abbott–Erdős–Hanson 1974:** `N(a) = O(log a / log log a)` (Amer. Math. Monthly
   81 (1974) 256–261; doi:10.2307/2319526). Same paper: the **average and normal
   order of `N(a)` is 2**.

3. **Kane — current record:** Kane 2007, `N(t) = O((log t)(log log log t) /
   (log log t)³)` (Integers 7 #A53; full text at
   http://cseweb.ucsd.edu/~dakane/combinations2.pdf). This remains the best
   **unconditional** total bound. Conditional on Cramér's conjecture:
   `N(t) = O_ε((log t)^{2/3+ε})` (AEH/MRSTT).

4. **MRSTT 2021 (interior):** Theorem 1.3, arXiv:2106.03335, Quart. J. Math.
   For `0<ε<1`, `t` sufficiently large: **at most two** solutions in
   `exp((log n)^{2/3+ε}) ≤ m ≤ n/2`, hence **at most four** in the symmetric interior
   `exp((log n)^{2/3+ε}) ≤ m ≤ n − exp((log n)^{2/3+ε})`; and **at most one** in
   `exp((log n)^{2/3+ε}) ≤ m ≤ n/exp((log n)^{1−ε′})` for
   `0<ε′<ε/(2/3+ε)`. Threshold **effective but astronomically large**.
   **What is left open:** the whole boundary/small-`k` region
   `2 ≤ m ≤ exp((log n)^{2/3+ε})`, equivalently `2 ≤ m ≤ (log t)/(log₂t)^{3/2−ε}`.
   This is exactly where `m/log t → 0` and `n` grows extremely fast in `m`; the only
   handle there (Siegel/Beukers–Shorey–Tijdeman) is **ineffective in `k`**, so no
   uniform bound there exists yet.

5. **Infinite family `N(a) ≥ 6` (Fibonacci):** Singmaster 1975, Fibonacci Quart.
   13(4) 295–298. The identity
   > `C(n+1, k+1) = C(n, k+2)`
   has the infinite solution family (MRSTT Remark 1.4 / Singmaster eq. (6)), with
   `F_0=0, F_1=1`: for each `j ≥ 1`,
   > `n+1 = F_{2j+2}F_{2j+3}`, `k = F_{2j}F_{2j+3}`  (Singmaster's `n,k`);
   > equivalently `n = F_{2j+2}F_{2j+3} − 1`, `m = F_{2j}F_{2j+3} − 1` (MRSTT).
   Each common value occurs ≥ 6 times. `j=1` gives `C(15,5) = C(14,6) = 3003`;
   `j=2` gives `C(104,39)=C(103,40)=6.1218…×10²⁸` (does not recur elsewhere).

6. **de Weger / effective small-`k`:** J. Number Theory 63 (1997) 373–386.
   Fixed-`(k,l)` curves `C(n,k)=C(m,l)` solved with explicit constants only in
   isolated cases: `(2,3)` [Avanesov, Skolem]; `(2,4)` [de Weger 1996 / Pintér 1995,
   Gelfond–Baker]; `(3,4)` [de Weger, via Mordell; the curve is **genus 3**, a double
   cover of `Y²+Y=X³−X`, and has only trivial integral solutions]; `(2,5)`
   [Bugeaud–Mignotte–Siksek–Stoll–Tengely 2008, hyperelliptic];
   `(2,6),(2,8),(3,6),(4,6),(4,8)` [Stroeker–de Weger 1999, elliptic
   logarithms/Baker-type algorithm]; `n≤10⁶` or `t≤10⁶⁰` [Blokhuis–Brouwer–
   de Weger 2017]. de Weger's **Conjecture A**: no nontrivial collisions beyond the
   six one-offs and the Fibonacci family — which would imply `N(a)≤8` for all `a`
   and `N(a)≤6` for all `a≠3003`. This is the effective route, but it is a
   **conjecture**, and the generic Siegel finiteness for fixed pairs is **ineffective
   in the pair**, so no `k`-uniform effective bound follows from curve methods.

## Structure of a minimal counterexample (what a proof must exclude)

A counterexample to "uniform boundedness" is a sequence `a_i → ∞` with `N(a_i) → ∞`.
The structure forced by the established theorems (so a proof must contradict at least
one of these):

- **Interior part:** for `a = a_i` large, let the solutions `(n,m)` to `C(n,m)=a_i`
  be split by `m`. MRSTT Theorem 1.3 says at most 4 of them can lie in the interior
  `exp((log n)^{2/3+ε}) ≤ m ≤ n − exp((log n)^{2/3+ε})` (both halves). So a growing
  `N(a_i)` would have to be concentrated in the **boundary**:
  `2 ≤ m ≤ exp((log n)^{2/3+ε})`, i.e. (converting) `2 ≤ m ≤ (log a_i)/(log₂a_i)^{3/2−ε}`.
- **So a minimal counterexample is: infinitely many `a` with many distinct small-`m`
  solutions**, `m` ranging over `O((log a)/(log₂a)^{3/2−ε})` possible values, each
  `m` contributing at most 2 solutions (the `(n,m)` and its mirror). Any proof of
  Singmaster therefore reduces to ruling out many simultaneous
  `C(n_m, m) = a` for small `m`.
- **Witness constraint:** any argument must be consistent with `C(15,5)=C(14,6)
  =C(78,2)=3003` (and the whole Fibonacci family). An argument implying `N < 8` for
  3003, or `N < 6` for infinitely many Fibonacci values, is wrong.
- **The de Weger conjecture forces the counterexample off the small-`(m,m′)` pairs:**
  if Conjecture A held, the multiplicity of every large `a` would be at most 2 in the
  interior plus the bounded few collisions, giving `N(a) ≤ 8` uniformly. So a proof
  of Singmaster that does not go through de Weger must rule out *new* small-`m`
  collisions uniformly — precisely the ineffective part.

## Current verification bound (computational)

- Singmaster's 1975 search: no nontrivial repetition beyond the seven listed up to
  binomial values `≤ 2⁴⁸ ≈ 2.8×10¹⁴`.
- de Weger 1997: no nontrivial solutions `C(n,k)=C(m,l)` with value `≤ 10³⁰` OR
  `max(n,m) ≤ 1000`.
- Blokhuis–Brouwer–de Weger 2017: verified de Weger's Conjecture A for `n ≤ 10⁶` or
  `t ≤ 10⁶⁰`.
- This run's oracle (`witnesses.json`): all `C(n,k)` with `2≤k≤n/2`, `n≤20000`,
  value `≤10¹²`; the only `N≥6` values found are exactly 3003 (N=8) and the six
  Singmaster witnesses 120,210,1540,7140,11628,24310 (N=6). No `N≥9` found.
- **Largest known** `N(a)`: `N(3003) = 8`. **Infinitely many** `a` have `N(a) ≥ 6`
  (Fibonacci family). No `a` with `N(a) ≥ 9` is known.

## At least three restricted classes already settled (with hypotheses)

1. **Interior region (MRSTT 2021, Thm 1.3):** `exp((log n)^{2/3+ε}) ≤ m ≤ n/2`.
   Hypotheses: `0<ε<1`, `t` sufficiently large in `ε`. Conclusion: ≤ 2 per half,
   ≤ 4 total. Effective but unoptimized threshold. (Also falling-factorial analogue,
   Thm 1.8.)
2. **Specific fixed pairs `(k,l)` of the curve `C(n,k)=C(m,l)` — effective:** with
   explicit hypotheses "`(k,l)` in the list", the curves are solved:
   `(2,3)`, `(2,4)`, `(3,4)`, `(2,5)`, and `(2,6),(2,8),(3,6),(4,6),(4,8)`; plus
   finite (ineffective) for every fixed pair via Beukers–Shorey–Tijdeman.
   Conclusion for `(3,4)`: **no nontrivial** integral solutions at all; for the
   others, only the listed collisions. Constants explicit (each case is a completed
   computation).
3. **Falling-factorial interior (MRSTT Thm 1.8):** `exp((log n)^{2/3+ε}) ≤ m < n`,
   t large, at most two solutions to `(n)_m=t`. Sharp (achieved by an explicit
   infinite family). This is a different equation but the same technique; it is a
   genuinely settled restricted class.

Also settled (weaker, different shape): the **conditional** class under Cramér's
conjecture — `N(a) = O_ε((log a)^{2/3+ε})` for all `ε>0`, and the **average/normal**
class: `N(a) = 2` for almost all `a` (AEH).

## Gaps / what the library does not yet establish

- No source computes an explicit constant in Kane's 2007 bound (all sources give
  only the `O(·)` form). An **effective constant** for `N(a)` would be a genuine
  partial result.
- No source gives an effective bound for the **boundary** `2 ≤ m ≤ (log t)/(log₂t)^{3/2−ε}`;
  this is the open core.
- The genus of `C(x,k1)=C(y,k2)` as a function of `(k1,k2)`, and the explicit
  threshold where Faltings applies, are not stated in any downloaded source (de Weger
  only gives the single datum genus(C(n,3)=C(m,4)) = 3). Computing this genus
  function is a natural next task (not yet in the library).
- Whether any `a` with `N(a) ≥ 9` exists is open (only 3003 is known with 8; the
  Fibonacci family gives 6).
