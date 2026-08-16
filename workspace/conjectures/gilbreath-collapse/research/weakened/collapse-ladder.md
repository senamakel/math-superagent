```ladder
goal: Every second-moment functional of w(h) = wt(Φ_n h) factors through the short-range correlations of h; equivalently S(n,h)² = Σ_{d,d'} (−1)^{Σ_{i∈M_d△M_{d'}} h_i} is a function of the short-range correlations of h alone, for every h ∈ F₂ⁿ
difficulties: unrestricted-h, unrestricted-d, multiset-shape-unknown, locality-unproven, correlation-order-unspecified, witness-search-exponential
status: open
```

```rung
id: R-n8-multiset
statement: For n = 8, compute the multiset { M_d △ M_{d'} : 2 ≤ d,d' ≤ 7 } of 36 symmetric differences exactly: for each occurring A ⊆ {0,…,7}, record its multiplicity, its cardinality |A|, its diameter max(A) − min(A), and its decomposition into maximal runs of consecutive positions. No h appears and no functional is claimed; it is pure finite enumeration, the smallest case where a spread pair and a clumped pair can be compared.
off: unrestricted-h, locality-unproven, correlation-order-unspecified, witness-search-exponential
stance: open
merge: Extend to n = 9..20 and diff the multiset between n and n+1 to find the closure rule for which new sets appear. The specific number to watch is whether any set of small cardinality but diameter ≥ n/2 occurs, and with what multiplicity — that is the seed of a refutation witness. Naming the closure rule is what re-enables `multiset-shape-unknown` at general n, and it is GOAL.md Priority 1.
```

```rung
id: R-single-run-stratum
statement: For d, d' in the single-run stratum d = 2^g − 1 (so M_d = {n−2^g, …, n−1} is one suffix interval), prove that M_d △ M_{d'} is either empty or a single interval (a prefix of the longer suffix). Prove this run-count statement exactly, and record the separate, equally easy fact that this interval has length 2^g − 2^{g'} — so run count 1 does NOT imply short range, and this stratum alone does not establish collapse.
off: unrestricted-d, multiset-shape-unknown, witness-search-exponential
stance: open
merge: Allow d with two maximal runs (pc(d) − ν₂(d+1) = 1). Then M_d △ M_{d'} is a union of up to four runs; the question that re-enables `locality-unproven` is whether the surviving runs are necessarily adjacent (union still one interval) or can be non-adjacent (a spread set). Cheap to test at small n.
```

```rung
id: R-bounded-popcount
statement: For d, d' restricted to pc(d), pc(d') ≤ k, prove that every A = M_d △ M_{d'} is a union of at most f(k) intervals with f independent of n, and determine the smallest such f(k). This is the partial collapse of problem.md result-type 3 for the pc ≤ k stratum.
off: unrestricted-d, witness-search-exponential, correlation-order-unspecified
stance: open
merge: k = 1 is R-single-run-stratum. Run-count bounded is not short range, because an interval's length is not bounded pointwise (length 2^g at k = 1). The real re-enablement of `locality-unproven` is a weighted statement: prove that item 4's size concentration forces the surviving intervals to have length O(1) in the average over d,d' — not pointwise. Naming whether that weighted bound holds is the next move.
```

```rung
id: R-diameter-local
statement: For n ≤ 20, compute the joint distribution of (|A|, diam(A)) over the multiset { M_d △ M_{d'} }, and answer: does any A occur with |A| ≤ 8 and diam(A) ≥ n/4? If yes, list the first such (d,d'). If no, record the sharp bound diam(A) ≤ c(|A|) that holds for all n ≤ 20. This finite check decides whether small cardinality forces short range — the exact gap item 4 leaves open, since its O(n) bound sizes the sets but says nothing about their spread.
off: unrestricted-h, correlation-order-unspecified, witness-search-exponential
stance: open
merge: A small-diameter bound lifts R-smalln-collapse's empirical collapse toward a proof and discharges `locality-unproven`. A small set with large diameter (say {0, n−1}) is the index of a long-range Walsh character; if it survives with non-cancelling multiplicity it is a refutation witness, which re-enables `unrestricted-h` and ends the run.
```

```rung
id: R-distance-enumerator
statement: The distance enumerator F_n(z) = Σ_{d,d'} z^{|M_d △ M_{d'}|} is O(n) uniformly in n for each fixed |z| < 1, so the pairwise symmetric differences are concentrated on sets of small cardinality. Anchor: problem.md imported result 4 (no claim block yet — settled by import, not by a forward-loop proof). Note the bound is on size only, not diameter: it is compatible with a spread set of size 2.
off: unrestricted-h, correlation-order-unspecified, witness-search-exponential
stance: settled
merge: Split each coefficient of z^m by diameter (or by run count and run lengths) rather than by size alone. If the diameter stays O(1) in the dominant term, `locality-unproven` discharges and R-full-collapse follows by composition; if the diameter grows, that is the refutation seed — re-enabling `multiset-shape-unknown` with the shape, not the size, as the load-bearing unknown.
```

```rung
id: R-uniform-second-moment
statement: In the uniform model (h uniform on F₂ⁿ), E[w] = (n−2)/2, Var(w) = (n−2)/4, and E[S²] = n−2, with w exactly Binomial(n−2, ½). Anchor: problem.md imported result 2 (no claim block yet — settled by import).
off: unrestricted-h, multiset-shape-unknown, witness-search-exponential
stance: settled
merge: The average is the trace of the (n−2)²-vector of Walsh characters and averages away exactly the high-order structure the collapse is about. The next rung replaces the average with a pointwise claim: do h,h' with equal short-range pair correlations have equal S² — re-enabling `unrestricted-h` and `witness-search-exponential` together.
```

```rung
id: R-twovalued-boundary
statement: For h the difference sequence of a two-valued boundary r (h[j] = [r_j ≠ r_{j+1}]), determine whether items 4, 6 and 7 of problem.md compose: i.e. whether S(n,h)² reduces, via the telescoping identity (item 6) and the endpoint-sign form (item 7), to a sum over the run endpoints of the M_d △ M_{d'}, and whether that sum depends only on short-range correlations of h. State precisely the step that fails if it does not. This is GOAL.md Priority 2.
off: unrestricted-h, witness-search-exponential
stance: open
merge: Drop two-valuedness to a three-valued r. The negative control already shows the telescoping identity fails with 438 mismatches over 620,067 pairs, first at d=1, pos=0, so no amount of items 6–7 alone survives the drop. Re-enabling `unrestricted-h` requires naming what (if anything) survives the drop, and whether the failure of telescoping propagates to a failure of the collapse or is absorbed in the S² average.
```

```rung
id: R-smalln-collapse
statement: For every n ≤ 12 (extendable to n ≤ 20), verify by exhaustive enumeration that S(n,h)² is a function of the short-range pair-correlation vector c_t(h) = Σ_{i=0}^{n−1−t} h_i h_{i+t} (t ≤ k) for the smallest k that works, or output an explicit witness pair h,h' with equal c_t for all t ≤ k but different S². Negative control: a deliberately broken comparison must fail. This is GOAL.md Priority 3.
off: witness-search-exponential
stance: open
merge: Read off the empirical correlation order k(n) that suffices at n ≤ 12 and state the conjecture that S² lies in the span of order-k correlation functions for all n. Lifting that finite check to a proof re-enables `correlation-order-unspecified` and `locality-unproven` together.
```

```rung
id: R-full-collapse
statement: For every h ∈ F₂ⁿ, every second-moment functional of w(h) is a function of the short-range correlations of h alone, with the exact functional class and correlation order stated. Equivalently: the multiset { M_d △ M_{d'} } is dominated by sets that are unions of a bounded number of adjacent positions, so S² factors through the short-range correlations of h.
off:
stance: open
merge: This is the goal; settling it exhausts the ladder. First move: prove or refute that every A = M_d △ M_{d'} occurring with non-negligible multiplicity is a union of O(1) short intervals. A bounded-short-interval proof composes with R-smalln-collapse into the theorem; a single spread A with non-cancelling multiplicity is a refutation witness.
```
