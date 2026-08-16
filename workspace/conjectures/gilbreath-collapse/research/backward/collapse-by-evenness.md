```skeleton
id: collapse-by-evenness
goal: >
  Prove COLLAPSE — every second-moment functional of w(h) is a function of the
  short-range (pair) correlations of h — and name the exact correlation order.
implies: >
  Let chi_A(h) = (−1)^{Σ_{i∈A} h_i}. By the concrete form in problem.md,
  S(n,h)² = Σ_{d,d'} chi_{M_d △ M_{d'}}(h), and S(n,h) = Σ_d chi_{M_d}(h).
  G-evenness gives |M_d △ M_{d'}| even, and |M_d| = 2^{pc(d)} even for every
  d,d' ≥ 2. G-even-set-is-product-of-pairs writes each chi_{M_d△M_{d'}} and
  each chi_{M_d} as a product of pair characters chi_{i,j}; G-pair-telescopes
  writes every chi_{i,j} (any distance) as ∏_{k=i}^{j−1} chi_{k,k+1}. Hence S
  and S² are both polynomials in the n−1 adjacent-pair XOR characters
  (chi_{k,k+1})_{k=0}^{n−2}. Since w = ((n−2) − S)/2, every functional in
  span{1, w, w²} factors through the adjacent-pair correlations of h. The
  adjacent XORs determine h exactly up to global complement ({h, ¬h}), and S, S²
  are constant on {h, ¬h} (evenness of each |M_d|). Correlation order is exactly
  1: order 0 would force S² constant, and S² is visibly non-constant (hand-check:
  at n=4, S² = 2 + 2·chi_{0,2}, taking values 0 and 4). So COLLAPSE holds with
  order 1, and the problem's heuristic sufficient condition (index sets being
  short) is strictly stronger than needed — a long index set such as
  M_{2^m} △ M_{2^{m−1}} = {n−1−2^m, n−1−2^{m−1}} still contributes only
  adjacent-pair data, by telescoping.
status: discharged
rests-on:
  - imported-result-3 (meet-semilattice size formula: |M_d△M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}, all terms even for d,d' ≥ 2)
  - imported-concrete-form (Walsh expansion S² = Σ_{d,d'} chi_{M_d△M_{d'}}, problem.md)
```

```gap
id: G-evenness-of-symmetric-difference
lemma: >
  For every n and every 2 ≤ d,d' ≤ n−1, the symmetric difference M_d △ M_{d'}
  has even cardinality. This follows from |M_d| = 2^{pc(d)} even for d ≥ 2
  (row d is the indicator of the down-set of d, so |M_d| = #submasks(d)
  = 2^{pc(d)}), and the parity identity
  |M_d △ M_{d'}| = |M_d| + |M_{d'}| − 2|M_d ∩ M_{d'}| ≡ 2^{pc(d)} + 2^{pc(d')}
  ≡ 0 + 0 ≡ 0 (mod 2). The full meet-semilattice formula
  |M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1} (imported-result-3)
  gives the same conclusion and is the stronger cross-check.
status: discharged
discharged-by: elementary parity (submask count |M_d| = 2^{pc(d)}, d ≥ 2); agrees with imported-result-3
next: >
  (verification, not a proof gap) reproduce |M_d| = 2^{pc(d)} and the parity of
  |M_d △ M_{d'}| at n ≤ 12 with the canonical oracle, as the negative-control
  cross-check GOAL.md requires.
```

```gap
id: G-even-set-is-product-of-pairs
lemma: >
  For any even-size A ⊆ {0,…,n−1}, A admits a perfect matching, and
  chi_A(h) = ∏_{{i,j} in the matching} chi_{i,j}(h) for every h.
status: discharged
discharged-by: elementary (pair consecutive elements of the sorted set A)
```

```gap
id: G-pair-telescopes-to-adjacent
lemma: >
  For all i < j and all h, chi_{i,j}(h) = (−1)^{h_i ⊕ h_j}
  = ∏_{k=i}^{j−1} (−1)^{h_k ⊕ h_{k+1}} = ∏_{k=i}^{j−1} chi_{k,k+1}(h).
status: discharged
discharged-by: elementary F₂ telescoping (h_i ⊕ h_j = Σ_{k=i}^{j−1} (h_k ⊕ h_{k+1}))
```

```gap
id: G-local-verification-and-formalisation
lemma: >
  (Not a missing lemma — the remaining work.) Convert this discharged skeleton
  into a run-owned theorem: (a) tool_builder reproduces imported-result-3 and
  the evenness/telescoping conclusion with the canonical oracle, with a negative
  control shown failing; (b) lean_prover formalises the collapse theorem — S and
  S² as functions of the adjacent-pair XORs — with #print axioms showing no
  sorryAx.
status: open
next: >
  tool_builder: write Phi_n, M_d, S(n,h) once in code/lib, cross-check against
  brute submask enumeration, then confirm |M_d △ M_{d'}| even for all d,d' at
  n ≤ 12 and confirm S²(h) is constant on {h, ¬h} (equivalently determined by
  adjacent XORs) on a random sample plus a deliberately broken evenness control
  that fails. lean_prover: formalise "chi_{i,j} = ∏ adjacent chi" and "even A ⇒
  chi_A is a product of pairs", then the composite collapse statement; report
  #print axioms.
```
