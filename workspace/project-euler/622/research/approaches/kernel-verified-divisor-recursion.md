# Kernel-verified structural recursion over the divisor lattice

A route that proves no closed form at all. It writes the divisor sum as a
structurally recursive function, proves the function correct by one induction,
and lets the kernel unfold it to the answer. The opposite pole from both
closed-form routes.

```approach
idea: A total recursive function in Lean that walks the divisor lattice of
  2^60−1 as a product of 11 exponent-chains (one per prime, exponents
  0..v_p(2^60−1), total 4608 leaves), evaluated by the kernel, with
  correctness proved by structural induction — no inclusion-exclusion, no
  Möbius, no σ/τ table.
mechanism: The divisor lattice of a factored number is a product of chains,
  one chain per prime power; summing a per-divisor predicate over it is a
  structural recursion of depth 11 (the number of distinct primes), not a scan
  over deck sizes. Define `filteredSum : (exp : Fin 11 → Nat) → ...` computing
  Σ over divisors satisfying the order-60 predicate
  (m | 2^60−1 and m ∤ 2^12−1 and m ∤ 2^20−1 and m ∤ 2^30−1, each a cheap
  norm_num check per leaf). Correctness is a single induction over the 11
  primes using multiplicativity of the divisor set (CRT). The final theorem
  `filteredSum ... = 3010983666182119516` (the S(60) part) is obtained by
  letting the kernel unfold the recursion — a bounded, kernel-checked
  computation, explicitly not native_decide (no Lean.ofReduceBool). This is the
  certificate pattern: the expensive search (finding the 11-prime
  factorization and the order assignments) happened in Python; the kernel only
  checks the structural recursion that reproduces the sum.
status: refuted
precedent: "Mathematics grounded: the correctness of a structural recursion
  over the divisor lattice of m = prod p_i^{a_i} rests on (i) the divisor set
  being the Cartesian product of exponent-chains [0,a_i], one per prime —
  tau(2^60-1) = 4608 leaves, and (ii) the CRT order-lcm decomposition
  ord_{n1*n2}(a) = lcm(ord_{n1}(a),ord_{n2}(a)) (claim order-lcm-over-prime-
  powers, proved; sourced to Naor Thm 6.1.32 + Chappelon Prop 5) and the
  order-divisibility bijection ord_m(2)|d iff m|2^d-1 (claim
  order-divisibility-conrad, proved; Conrad Thm 2.1). These make the order-60
  predicate m|2^60-1 and m not dividing 2^12-1,2^20-1,2^30-1 decouple per
  prime power, so the recursion is correct by a single induction over the 11
  primes. The mathematics is standard and sourced. The speculative part is NOT
  answerable from the literature: whether Mathlib's kernel unfolds an
  11-deep, 4608-leaf recursion inside the lean_check timeout without
  native_decide is an engine/engineering question that must be tested in Lean
  (as the file's 'risk to test first' already says).
killed-by: Not refuted on mathematics — fully grounded. Passed over for the
  adopted line on cost: the kernel must unfold an 11-deep, 4608-leaf recursion
  inside the lean_check timeout, with no `native_decide`; the literature cannot
  settle this engine question either way, so the route is a risk on the
  deliverable rather than a result. The adopted `mobius-inversion-exponent-lattice`
  replaces that unfold with an 8-term signed σ/τ sum, each term a single
  kernel-checked literal, so the kernel work is a handful of `norm_num`/
  `ring` multiplications instead of 4608 leaf visits. If the Möbius tree ever
  stalls, this recursion remains the named fallback (with the hand-telescoped
  partial-sum form), not a reopened route. Honest boundary: the literature neither supports nor refutes
  the kernel-unfold budget; that is the one open risk, tested by writing
  code/lean/Lib/DivisorSum.lean and running lean_check, with the fallback of a
  hand-telescoped partial sum (not native_decide) already named in the file.
```

Grounding: the factorization 2^60−1 = 3^2·5^2·7·11·13·31·41·61·151·331·1321
(11 primes) and τ(2^60−1)=4608 are already in the `riffle-order-60` skeleton
(G-factorization, G-divisor-sums). The speculative part is the kernel's
unfold budget: whether an 11-deep recursion with 4608 leaves evaluates inside
the lean_check timeout without native_decide is exactly what must be tested
first. If it does not, the fix is to fold the primes into a smaller certificate
(a hand-telescoped partial sum), not to reach for native_decide.
