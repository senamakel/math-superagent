# Proof skeleton — COLLAPSE decided at the index multiset {M_d △ M_{d'}}

This skeleton decomposes the goal of *settling* COLLAPSE (GOAL.md: "say which
it is — theorem or artifact") into three gaps about the multiset
`{ M_d △ M_{d'} }`. The inference is a two-way reduction: the Walsh identity
makes the support of `h ↦ S(n,h)²` exactly that multiset, and imported items
3, 5, 6, 7 give the endpoint/telescoping form of each character — so a
description of the multiset *decides* the conjecture in both directions.
G-collapse-range is where the two sides fork, and its `next` checks the fork
before anything else.

```skeleton
goal: Settle COLLAPSE. Affirmative: S(n,h)² depends only on the short-range
      correlations of h (a function of the order-K correlation statistics for
      one explicit K). Negative (the witness): there exist K, n, h, h' with
      identical order-K correlations but S(n,h)² ≠ S(n,h')². The two are
      exclusive; GOAL.md requires naming which holds, not leaving it indicated.

implies: For A ⊆ [n−1] write m(A) = #{ (d,d') : M_d △ M_{d'} = A }. By the
      definitional Walsh identity
          S(n,h)² = (Σ_d (−1)^{T(n,d)})² = Σ_{d,d'} χ_{M_d △ M_{d'}}(h)
                  = Σ_A m(A)·χ_A(h),      χ_A(h) = (−1)^{⟨h,A⟩},
      the Fourier support of h ↦ S(n,h)² is exactly {A : m(A) > 0}. So
      G-collapse-multiset (exact m(A)) and G-collapse-range (the run/span
      structure of each A in the support) together determine, for every K,
      whether the support is contained in the order-K short-range class.
      IF contained, imported items 6–7 give χ_A(h) = ∏_runs χ(r_{a_R})χ(r_{b_R})
      (r the prefix-XOR of h), and G-collapse-telescope assembles
          S(n,h)² = F_K( (⟨h, I⟩)_{I interval, |I| ≤ K} )
      for an explicit F_K — the affirmative side. IF G-collapse-range instead
      produces A* in the support whose span exceeds every order-K class while
      its weight m(A*) survives the cancellation, G-collapse-telescope's
      witness step hands the two strings h, h' differing only at A* — the
      negative side. One of the two must hold once the multiset is exact, so
      the three gaps settle the goal.
status: sketched
rests-on: (no claim ids recorded yet — the claims ledger is empty at turn 0).
      The reduction's inputs are the four facts imported-as-proved in
      problem.md: item 3 (M_d ∩ M_{d'} = M_{d∧d'}, exact size of the symmetric
      difference), item 5 (run structure of M_d), item 6 (telescoping over a
      run), item 7 (endpoint-sign form). All four are asserted-by-source in
      this run until the canonical oracle reproduces them; nothing past them is
      trusted before then. The dependencies are named here rather than left
      implicit, but they are not yet claim ids on disk.
```

```gap
id: G-collapse-multiset
lemma: For each n, the multiset { M_d △ M_{d'} : d,d' ∈ [2, n−1] } is described
      exactly: a closed form for the multiplicity m(A) of every set A that
      occurs — which subsets of [n−1] arise as a symmetric difference, and how
      many pairs (d,d') produce each. Imported item 3 gives the SIZES |A| in
      closed form; missing is WHICH sets occur, with multiplicity, and how the
      multiplicity is distributed over sizes (the tail control that makes
      item 4's O(n) bound on F_n(z) = Σ_{d,d'} z^{|A|} precise). GOAL.md
      priority 1 — the crux of everything else.
status: open
next: tool_builder: with the canonical oracle M_d in code/lib, enumerate all
      (n−2)² pairs (n ≤ 128 gives 15876 pairs — trivial), collect the distinct
      sets A with multiplicities m(A) to code/out/multiset_census_n128, and
      tabulate each A by (|A|, span(A), run decomposition, pc(d), pc(d'),
      pc(d∧d'), ν₂(d+1), ν₂(d'+1)) to expose the pattern. Negative control:
      cross-check each |A| against item 3's closed form and force a mismatch
      on a deliberately broken oracle to confirm the check measures anything.
```

```gap
id: G-collapse-range
lemma: The run/span structure of each A = M_d △ M_{d'} in the support, as a
      function of (pc(d), pc(d'), pc(d∧d'), ν₂(d+1), ν₂(d'+1)) — and from it,
      the precise collapse predicate. The fork to settle: does the WEIGHT of
      the support concentrate on short-range A (bounded span / few short runs),
      or do long-span A carry surviving weight? Sharp dyadic families are
      already known by hand-computation (unverified — to be confirmed by the oracle's
      first run before the fork is trusted), so the per-set reading is dead on
      arrival and must not be the lemma: M_{2^k−1} △ M_{2^k} = [n−2^k−1, n−2]
      (one run of length 2^k); M_{2^k−1} △ M_{2^k−2} is 2^{k−1} singleton
      runs (the points {n−2^k, n−2^k+2, …, n−2}); and
      M_{2^k} △ M_{2^k+1} = {n−2^k−2, n−2} (size 2, span 2^k). So the
      honest lemma is the weighted one: the multiplicities m(A) put the bulk
      of F_n(z) on short-span A, and the collapse order K is the span where the
      residual long-span weight vanishes. If instead some long-span A survives
      with non-cancelling weight, that A is the witness seed (gap
      G-collapse-telescope, negative side).
status: open
next: tool_builder: from the G-collapse-multiset census, compute span(A) and
      run-length multiset per A, then the weighted span histogram
      H_n(k) = Σ_{A : span(A)=k} m(A). Decide the fork by checking whether
      H_n(k) is supported on k ≤ K₀ for an absolute K₀, or has a tail reaching
      the dyadic families (spans 2^k, 2^k+1 with multiplicity ≥ 1). This is a
      handful of lines over the census — run it before any theorem work. If the
      tail is real, the affirmative reading needs a cancellation argument or
      fails; if it is empty, hand the closed form
      span(A) = f(pc(d), pc(d'), pc(d∧d'), ν₂(d+1), ν₂(d'+1)) to theorem_prover.
```

```gap
id: G-collapse-telescope
lemma: Given the exact multiset (G-collapse-multiset) and its run/span
      structure (G-collapse-range), import items 6–7 to write each character
      in endpoint form and assemble the whole functional. Affirmative side:
      prove the finite sub-claim that χ_A(h) = ∏_runs χ(r_{a_R})χ(r_{b_R})
      (r = prefix-XOR of h) is a function of the order-K interval correlations
      (⟨h, I⟩)_{|I| ≤ K} when A has bounded span, then group the census by run
      structure to obtain the explicit F_K with
      S(n,h)² = F_K((⟨h, I⟩)_{|I| ≤ K}). Negative side: if G-collapse-range
      yields a long-span A* in the support, construct two strings h, h' with
      identical order-K correlations for all K below span(A*) but
      χ_{A*}(h) ≠ χ_{A*}(h') — a satisfiability question, not a search.
status: open
next: theorem_prover / sat_solver: (affirmative) formalise the finite Fourier
      sub-claim — for A a disjoint union of runs of total span ≤ K,
      χ_A(h) = ∏_t χ_{I_t}(h) is a function of the length-≤K interval
      characters — with the product-over-runs step from imported items 6–7;
      (negative) hand sat_solver the constraint system
      ⟨h, I⟩ = ⟨h', I⟩ for all intervals I with |I| ≤ K, and
      Σ_{i ∈ A*} (h[i] ⊕ h'[i]) ≡ 1 (mod 2), with K = span(A*) − 1 — SAT on
      this is a witness, UNSAT would show the two strings cannot differ at A*
      alone. Run the negative side only if G-collapse-range reports a tail.
```
