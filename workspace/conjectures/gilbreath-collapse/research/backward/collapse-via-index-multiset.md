# Collapse: what would suffice

Notation. `Δ_n = { M_d △ M_{d'} : d,d' ∈ [2,n−1] }` (multiset, size `(n−2)²`),
`m(A) = #{ (d,d') : M_d △ M_{d'} = A }`. `χ_A(h) = (−1)^{Σ_{i∈A} h_i}`, and by
expanding `(Σ_d χ_{M_d})²` we get the exact Fourier identity

    S²(h) = Σ_{A ⊆ [n]} m(A) χ_A(h),

so S² is determined by `Δ_n` with multiplicities. All symmetric-difference sizes
`2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}` are even, so every character in the
sum has even degree in the ±1 basis.

**Correlation order, pinned.** Pair correlations up to lag K are the complete
joint counts `N_ab(k) = #{ i ∈ [n−k] : h_i = a, h_{i+k} = b }` for every
`1 ≤ k ≤ K`, `a,b ∈ {0,1}`. `C_K(h)` is that list. "S² factors through
K-pair correlations" := S² is constant on each `C_K`-fiber. This is the
standard reading of "pair correlations" (degree 2, at range ≤ K), and it is the
right decision object: two strings with equal `C_K` for large K are the witness
the problem asks for, and the threshold in K is the collapse order. (The
adjacent 2-gram count `N_ab(1)` is only the lag-1 slice — strictly coarser than
the full pair-correlation data `C_K`; testing only it would refute a claim the
problem does not make, so the test below uses `C_K` for all lags ≤ K.)

Two hand-derived index families (to be confirmed by the oracle) that locate
where a witness must live:

1. `d = 2^j+1, d' = 2^j` gives `M_d △ M_{d'} = { n−2−2^j, n−2 }` — a pair at
   distance `2^j`, `m ≥ 2`. Long-range pair characters occur in S².
2. `d = 2^m−2, d' = 2^m−1` gives `{ n−2^m, n−2^m+2, …, n−2 }` — `2^{m−1}`
   isolated singletons, run count and diameter `Θ(n)`, `m ≥ 2`.

Both are invisible to the imported `O(n)` distance enumerator (item 4): they
weigh `z^{Θ(n)} = o(1)` in `F_n(z)`. So item 4 alone cannot rule out a witness.

```skeleton
goal: Settle COLLAPSE. Decide whether S² factors through the pair correlations
      of h at some bounded order K; if it does, name the minimal absolute K*;
      if not, give n and h,h' with C_K(h) = C_K(h') for K = n−1 (all pair
      correlations) yet S²(h) ≠ S²(h') — the refutation witness.
implies: >
  (1) Fourier identity S² = Σ_A m(A) χ_A reduces the whole question to Δ_n;
      G-mset is the crux. (2) Factoring through K-pair correlations is exactly
      constancy on C_K-fibers, so the decision is a fiber test, not a support
      argument: a long-range pair in supp(m) does NOT by itself refute collapse
      ((Σ_i x_i)² has Walsh support on every pair). (3) G-witness tests the
      fibers directly at n ≤ 20: a witness refutes collapse and ends the run;
      none bounds the K=1 reading away. (4) G-order finds the threshold
      K*(n) = min{ K : S² constant on C_K-fibers }; sup_n K*(n) < ∞ is the
      collapse theorem (with the true order named), K*(n) = Ω(n) is the
      refutation that survives. (5) Imported items 4,6,7 do NOT compose: item 4
      controls Σ z^{|A|}, a size weighting, while the families above sit in
      supp(m) with m ≥ 2 and o(1) weight — the step "small z-weight ⇒ outside
      the support / negligible" is false and is the named failure of the naive
      composition (GOAL priority 2).
rests-on: none from the claims ledger (empty; imported items 3–7 are
      asserted-by-source, not locally verified). G-mset rests on items 3 and 5
      once the oracle re-verifies them; G-order reconciles with item 4.
status: live
```

```gap
id: G-witness
lemma: For each n ≤ 20 and each K ≤ n−1, determine whether h,h' ∈ F₂ⁿ exist
      with C_K(h) = C_K(h') but S²(h) ≠ S²(h'). In particular report whether
      any K < n−1 yields a witness, and whether K = n−1 does.
status: open
next: >
  Build the canonical oracle (Φ_n, M_d, S) in code/lib and cross-check against
  brute submask enumeration n ≤ 9. Then for n ≤ 20, group h ∈ F₂ⁿ by C_K for
  K = 1,2,3,… and test constancy of S² per fiber; report the first witness
  (h,h',K) or the absence bound, with a deliberately broken negative control
  shown failing.
```

```gap
id: G-mset
lemma: Exact description of Δ_n: M_d △ M_{d'} as a disjoint union of runs (via
      M_d ∩ M_{d'} = M_{d∧d'} and the down-set run structure), and a closed
      form for the multiplicity m(A) of each A ⊆ [n].
status: open
next: >
  From the oracle census n ≤ 20, tabulate each A ∈ Δ_n by (|A|, diam, run
  count, run lengths, m(A)); cross-check |A| against
  2^{pc(d)}+2^{pc(d')}−2^{pc(d∧d')+1}; confirm the two hand-derived families
  above (single far pair; alternating singletons), then derive the general
  formula — the run count and run lengths decide whether C_K with bounded K can
  ever see every character in supp(m).
```

```gap
id: G-order
lemma: The threshold K*(n) = min{ K : S² is constant on C_K-fibers } satisfies
      sup_n K*(n) < ∞ (collapse at the named order K*) or K*(n) = Ω(n) (no
      sublinear collapse; G-mset then supplies the explicit witness pair).
status: open
next: >
  From the G-mset census compute K*(n) for n ≤ 20 by the G-witness fiber test
  and fit it against n; then formalise the Fourier identity S² = Σ_A m(A) χ_A
  and the fiber-constancy characterisation in Lean, #print axioms with no
  sorryAx.
```

First attack: **G-witness** — a witness ends the run (GOAL priority 3); absence
at n ≤ 20 is the strongest admissible evidence for the collapse branch and
hands G-mset its data.
