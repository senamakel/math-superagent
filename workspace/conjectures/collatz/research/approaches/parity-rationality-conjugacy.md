# Approach: parity-vector rationality via the Bernstein conjugacy

```approach
idea: Reduce Collatz dynamics to the 2-adic parity-vector conjugacy and investigate divergence through discrepancy/rotation theory.
mechanism: For the accelerated map T(x)=x/2 for even x and (3x+1)/2 for odd x, Bernstein–Lagarias prove a 2-adic conjugacy Φ∘S∘Φ⁻¹=T, with Q∞=Φ⁻¹ encoding parities. Rational 2-adics are exactly eventually periodic binary expansions. This is a reformulation, not a proof of the integer conjecture. The proposed extra step—using the three-distance theorem on valuation partial sums—is not established by the cited Collatz literature: the theorem governs a genuine irrational rotation sequence, and no source derives the claimed integer-valued-discrepancy-versus-rotation contradiction for the actual Collatz valuation sequence.
status: narrowed
survives: The conjugacy itself survives as an exact coordinate change and is a legitimate TOOL for any other line of attack (e.g. the parity vector is the same object as the gap pattern in the adopted divisibility approach — Q∞(n) eventually periodic with m ones in its period IS the shape data (L,m,gaps)). What closed is only the divergence-via-three-distance bridge: no lemma links v2(T^k(n)+1) to an irrational rotation, so the discrepancy argument has no object to attach to.
killed-by: The three-distance bridge is unsupported by any source (research assessment 2025): the theorem applies to rotation sequences, not to Collatz valuation sequences, and López–Stoll constrain rather than eliminate aperiodic rational-2-adic behaviour. The divergence half has no route through it without a lemma nobody has proved.
precedent: https://doi.org/10.1090/S0002-9939-1994-11639-4 (Bernstein 1994); https://doi.org/10.4153/CJM-1996-060-x (Bernstein–Lagarias 1996); https://arxiv.org/abs/2101.12747 (López–Stoll 2021); https://doi.org/10.48550/arxiv.1712.03758 (Beresnevich–Leong, three-distance application); claim ids: lagarias-2adic-ergodic, everett-parity-vector-bijection
first-step: n/a — closed as an independent line; the conjugacy is available as a tool inside other approaches.
```

## Literature assessment

**What it is called.** The established part is the *3x+1 conjugacy map*, *2-adic parity-vector encoding*, and Lagarias’ *periodicity conjecture*. The three-distance theorem is also the *three-gap theorem* (Steinhaus theorem).

**Precise sourced result.** Bernstein’s theorem gives a homeomorphism Φ of Z₂ with Φ⁻¹∘T∘Φ equal to the 2-adic shift (equivalently T∘Φ=Φ∘S). The parity map Q∞=Φ⁻¹ records the parity bits and intertwines T with the shift. A 2-adic integer is rational iff its binary expansion is eventually periodic. These facts hold for the 2-adic extension, but do not say that Q∞(n) is rational for every positive integer n; that is essentially the unresolved periodicity/Collatz assertion.

**Three-distance theorem.** For irrational α and N≥1, the points {0,α,…,(N−1)α} mod 1 have at most three distinct adjacent gap lengths. The theorem applies to a genuine irrational rotation sequence. No source found applies it to the sequence of Collatz valuations proposed here, and no theorem found derives the claimed “integer-valued discrepancy versus rotation” contradiction. López–Stoll provide a related density criterion for Φ and explicitly leave the rational-2-adic non-cyclic case constrained rather than eliminated.

**What it would buy.** If the missing discrepancy-to-rotation lemma were proved, it could address the divergent-orbit arm, which cycle Diophantine bounds do not. At present it is a grounded reformulation plus an unproved bridge, not a validated solution method.
