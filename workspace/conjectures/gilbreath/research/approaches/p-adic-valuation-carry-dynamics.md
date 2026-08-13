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
