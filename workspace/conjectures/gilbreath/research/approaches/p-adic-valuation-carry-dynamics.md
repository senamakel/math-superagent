```approach
idea: p-adic-valuation-carry-dynamics
mechanism: |
  Every entry A_k(i) for k >= 1, i >= 1 is even, so it carries a 2-adic
  valuation v_2(A_k(i)) in {1, 2, 3, ...} (and v_2(0) = infinity). The
  conjecture A_k(1) in {0,2} is EXACTLY the statement

      v_2(A_k(1)) in {1, infinity}  for all k,

  i.e. the valuation of the second entry never attains a finite value >= 2.
  This reformulation is not a congruence on the value; it is a full valuation
  profile, and it obeys an EXACT local law, not a lift that fails at higher
  powers of 2.

  The exact law is the non-Archimedean (ultrametric) triangle inequality of the
  2-adic valuation. For any integers a, b:

      v_2(|a-b|) >= min(v_2(a), v_2(b)),
      with EQUALITY iff v_2(a) != v_2(b),
      with strict lift (>= min + 1) iff v_2(a) = v_2(b).

  The "lift" case is the carry of binary subtraction: when a and b have the
  same valuation t, write a = 2^t u, b = 2^t v with u, v odd; then
  |a-b| = 2^t |u-v| and u-v is even, so the valuation rises. The further lift
  is governed by the ODD parts u, v, which is the same rule one level down —
  a clean renormalization/self-similarity. This is the standard valuation
  formulation of the Ducci map, and it is the object the mod4-pascal approach
  needed but never had: mod4-pascal tried |a-b| == a+b (mod 2^t), which needs
  min(a,b) == 0 (mod 2^{t-1}) and fails at t = 3; the valuation law above is
  exact for every t, because the "carry" (min term) is absorbed into the
  valuation rather than discarded.

  Concretely, the triangle of valuations V_k(i) = v_2(A_k(i)) is a cellular
  automaton driven by carries of the halved gap sequence h_n = (p_{n+1}-p_n)/2.
  Position 1 (the second entry) receives a valuation that is the result of a
  cascade of carries down the light cone. The conjecture becomes: the carry
  cascade into position 1 never raises the valuation past 1. If the carry
  dynamics can be shown to be "absorbing" in the sense that a value 2
  (i.e. valuation 2) at the block boundary is forced to drop its valuation
  before it reaches position 1 — a statement about the carry automaton of
  binary addition, which is finite-state over the bits but exact — then the
  conjecture follows. This is a genuinely different axis from everything
  closed: it tracks ALL bits via valuation, not residues modulo a fixed prime
  power (mod4-pascal) or modulo an odd prime (mod6-structure), and it is
  exact rather than a bounded approximation.

  Why it beats what was refuted: mod4-pascal died because a congruence lift
  conflates 0 with 4 and 2 with 6 at mod 4, and cannot reach mod 8. The
  valuation law does not lift a congruence; it replaces it with the exact
  ultrametric/carry structure, so the min() branch that killed mod4 is the
  whole engine rather than the obstruction. rule90 governed only the {0,1}
  interior bits; the valuation automaton governs the part (the carries) that
  regeneration actually turns on. Speculative: that the carry cascade is
  provably absorbing at the left edge for 2-then-odd starts — this is the
  claim research must source or falsify (p-adic/carry treatments of the
  difference map, e.g. in the Ducci-sequence and 2-adic dynamics literature).
precedent: |
  (grounded, librarian cycle 2026) The exact 2-adic/Pascal linear core the
  approach needs is now in the library from four independent primary Ducci
  sources, with the boundary the approach cannot cross.

  GROUNDED — the mod-2 map IS the exact linear core, proved in the cyclic
  Ducci literature: Avart 2011 (Fib. Q. 49.2, held) proves the identity
  T^n(x) = Σ_i C(n,i)·r^i(x) over Z2 (the Pascal/Rule-90 kernel, exactly the
  run's rule90-interior-xor), and Calkin–Stevens–Thomas 2005 (Fib. Q. 43.1,
  held) give the complete cycle-length characterization via the minimal
  polynomial µ_n(λ) = (1+λ)^n + 1 and the power-of-2 nilpotence proof
  (I+S_L)^{2^r} = I + I = 0. Glaser–Schöffl 1995 (Fib. Q. 33.4, held) give
  the same kernel via Pascal's triangle mod 2 (their Theorem 1) PLUS the
  digit-sum fact 2^{s2(k)} ones in row k (Glaisher, property (7)) and the
  all-1s row at k = 2^r − 1 / all-0s interior at 2^r (properties (5),(6)) —
  the exact binomial-parity facts the rule90-regeneration thread uses.

  GROUNDED — the p-adic valuation law (v2(|a−b|) ≥ min(v2 a, v2 b), equality
  iff valuations differ, lift iff equal) is the exact non-Archimedean
  triangle inequality; it is not in these papers (they work mod 2 / over Z2,
  not over Z_2^× valuations), so the CARRY-level (v ≥ 2) content remains
  genuinely open, exactly as the approach states: "research must source or
  falsify (p-adic/carry treatments...)".

  BOUNDARY — every one of the four sources is about the CYCLIC map. The
  nilpotence/cycle-length conclusions (zero iff power of 2, concatenation
  characterization, period divisibility) are cyclic-object theorems. The
  Gilbreath triangle has no wraparound; a valuation-carry cascade into
  position 1 of a non-cyclic row is NOT a cyclic Ducci quantity. The
  approach's claim "the carry cascade into position 1 never raises the
  valuation past 1" is a half-infinite statement the Ducci/carry literature
  does not address; Eppstein 2011 (held) is the standing demonstration that
  half-infinite behaviour diverges from cyclic. So the valuation law's
  transfer is safe (it is a pointwise identity), but any absorption or
  boundedness conclusion must be proved for the windowed half-infinite
  object, not imported.

  What would falsify the approach: a single row k ≤ 1000 with v2(A_k(1)) ≥ 2
  (i.e. A_k(1) a multiple of 4) — the oracle says none exists (depth 1000,
  A_k(1) ∈ {0,2}); or a counterexample valuation cascade in a 2-then-odds
  start (Eppstein-class) showing the left-edge valuation can be raised past 1
  — which would show the absorption claim is class-false.
status: proposed
first-step: |
  Compute the valuation triangle V_k(i) = v_2(A_k(i)) from the depth-1000
  prime rows and verify the exact law (equality iff valuations differ, lift
  iff equal) holds at every interior cell. Then extract the carry rule into
  position 1: for each k, record the minimal chain of cells whose valuations
  determine V_k(1), and test whether V_k(1) > 1 ever occurs (it must not, by
  the verified conjecture to depth 1000 — so the test is that the computed
  cascade reaches valuation 1 at the lead and that the boundary carries that
  *would* raise it are provably blocked). Hand research the precise question:
  what does the 2-adic/carry literature (Ducci valuations, "carry propagation"
  in binary addition) already prove about valuations that never exceed 1 at a
  fixed position.
```
