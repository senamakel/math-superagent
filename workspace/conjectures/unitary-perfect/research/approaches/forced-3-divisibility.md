```approach
idea: Prove that every unitary perfect number is divisible by 3, using a local
  obstruction modulo 9 (or modulo 27) from the full balance equation combined
  with the 2-adic budget. All five known examples are divisible by 3, and the
  question is open; either direction is a result.
mechanism: Write n = 2^a·Π p_i^{e_i} with p_i odd distinct. The full balance is
  (2^a+1)·Π(p_i^{e_i}+1) = 2^{a+1}·Π p_i^{e_i}. If 3 ∤ n, then no p_i = 3.
  Reduce the equation modulo powers of 3. For p ≠ 3, p^e mod 9 is determined by
  p mod 9 and e mod 6 (since φ(9)=6). Compute the possible values of
  (p^e+1) mod 9 and p^e mod 9 for all p mod 9 with p ≠ 3. The RHS has factor
  2^{a+1} mod 9 which cycles (2,4,8,7,5,1) with period 6. The LHS has factor
  (2^a+1) mod 9 and factors (p_i^{e_i}+1) mod 9. The product equality mod 9
  (or mod 27) may force a contradiction unless some p_i ≡ something specific.
  More powerfully: combine with the 2-adic budget — each p_i^{e_i}+1 contributes
  a specific 2-adic valuation, and the total is a+1. The primes that can appear
  with v2=1 (which is most of them, since ω ≤ a+1) are those ≡ 1 mod 4. The
  interplay of mod-3 and mod-4 constraints on each p_i may force 3 into the
  prime set. Specifically, if no p_i = 3, then all p_i ≥ 5, and one can bound
  how many can be ≡ 2 mod 3 (forcing 3 | p_i^{e_i}+1, which would make the
  3-adic valuation on the LHS too large relative to the RHS). This is a local-
  global obstruction: the simultaneous constraints modulo 3, 4, and 2^a may
  have no solution without p_i = 3. The mechanism is elementary congruence
  chasing, sharpened by the exact 2-adic budget — it reduces to checking a
  finite (though possibly large) case analysis over residue classes.
status: proposed
first-step: Tabulate (p^e+1) mod 9 and mod 27 for all p mod 9 (p≠3) and e=1,2,3,4
  (higher exponents reduce mod 6); compute the 3-adic valuation v3(p^e+1) for
  each; write the full balance mod 9 and mod 27 and attempt to derive a
  contradiction when no p_i = 3, or identify the exact residue configuration
  that would be needed. Verify the candidate obstruction against the five known
  numbers (all divisible by 3) as sanity checks.
```