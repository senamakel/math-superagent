```approach
idea: ducci-potential-max-decrease
mechanism: |
  The Gilbreath operator A_{k+1}(i) = |A_k(i) - A_k(i+1)| is EXACTLY the
  Ducci map (the "n-number game", studied since the 1940s — Ciamberlini &
  Marengoni, Ducci's original note, and the modern survey literature), applied
  to a half-infinite rather than a cyclic sequence. This run has never brought
  the Ducci-sequence theory itself to bear: it has only used the mod-2
  linearization (which is the Ducci proof technique for the power-of-2 case)
  and the block-lemma diagonal argument. The Ducci literature carries a second,
  nonlinear family of results — potential/energy arguments about the MAXIMUM
  and its position — that do not pass through any congruence lift.

  Two exact facts are elementary and do not depend on cyclicity:

  (1) M_k := max_i A_k(i) is non-increasing: |a-b| <= max(a,b) pointwise, so
      M_{k+1} <= M_k. This is a Lyapunov function of the full nonlinear
      operator, free of charge.

  (2) A_{k+1}(i) is strictly smaller than max(A_k(i), A_k(i+1)) unless one of
      A_k(i), A_k(i+1) is 0. So the maximum can only *persist* (not drop) if
      it is adjacent to a 0 every step — a rigid "ridge" condition. This is the
      same rigidity that CHT Theorem 1.6 isolates as the only obstruction
      (long 0-blocks and shallow {0,d}-blocks), but derived here as a local
      potential statement rather than a global inverse theorem.

  The proposal is the route problem.md explicitly names as the cleanest: an
  invariant that forces A_k(1) in {0,2} DIRECTLY, without tracking blocks. The
  candidate invariant is not M_k alone but a *localized* version, e.g.
  max_{i <= L} A_k(i) for a fixed window L, or the pair (M_k, position of a
  maximum), plus the parity constraint A_k(i) even for i >= 1. If one can prove
  a sharp Ducci-style "the maximum within the first L positions drops below 4
  within at most f(L) rows unless the row is {0,d}-rigid", then the {0,2}
  regime is forced for the primes by contradiction: a counterexample row with
  A_k(1) = 4 is a row where the first-window maximum reaches 4, and the
  potential argument must show the configuration that sustains a 4 there
  (a long shallow {0,d}-block feeding it) cannot persist.

  Honest tension, to be checked first: Eppstein 2011 shows that for general
  2-then-odds sequences the RIGHT EDGE can stay arbitrarily high (gap >
  row-sum), so a naive global max-decrease is false on the half-line. The
  proposal's value is precisely to locate WHERE the escape lives: Eppstein's
  escape injects one huge value at the far right edge, which the global M_k
  sees but a fixed left-window L does not. The localized potential is a
  different invariant from the one Eppstein defeats, and is exactly the right
  granularity for the left-column statement. Speculative: whether a sharp
  left-window max-decrease lemma with an explicit f(L) exists is open and is
  what research must settle (the exact statements of the Ducci max-decrease
  lemmas, and whether they survive localization to a window).

  Why it beats what was refuted: mod4-pascal tried to lift a congruence past
  mod 8 and died on the min() branch; the Ducci max/potential route never
  touches a congruence, it uses |a-b| <= max(a,b) and the 0-adjacency rigidity,
  which are exact. backward-automaton died on non-locality; a potential is a
  scalar, so there is no state space to be non-local. rule90 died on absorption
  time; this is not about absorption, it is about a monotone quantity.
precedent: |
  (grounded, librarian cycle 2026) The Ducci literature is now in the library
  and establishes BOTH halves of the mechanism, and the boundary it cannot
  cross.

  GROUNDED HALF — the potential/max-decrease technique is the standard proof
  engine of the Ducci literature: Chamberland 2003 (JDEA 9(3):339-342,
  author PDF held, "Unbounded Ducci sequences") proves Theorem 3.2 by exactly
  this pair: (i) show the maximum at most doubles in two iterations, factor
  out the power of two, and show the FACTORED maximum strictly decreases in
  every non-borderline case; (ii) classify the borderline cases where the
  maximum does not decrease — they are exactly the rigid strings
  (0,b,d,d), (0,0,c,d), (a,0,c,2a), (a,a,c,c), (a,b,a,b) (his Lemma 3.1),
  which iterate to zero directly. Both mechanism facts in the approach's
  "mechanism" field (max non-increasing; persistence only adjacent to a 0)
  are exactly Chamberland's ingredients, and the equality-case rigidity is
  precisely the {0,d}-block rigidity CHT isolate. So "potential = (factored
  max, rigidity classification of the equality case)" is a named, working
  method in the primary literature, not a speculation.

  GROUNDED HALF — the classical theorems the approach would import are all
  cyclic-object theorems: Ciamberlini–Marengoni 1937 (zero iff length 2^m,
  quoted in Chamberland and Calkin–Stevens–Thomas), Avart 2011 (nilpotent
  over Z2 iff concatenation of power-of-two-length copies), Glaser–Schöffl
  1995 (cycle lengths via Pascal mod 2; the mod-2/Pascal identity is their
  Theorem 1) — all for the CYCLIC map with wraparound |xn−x1|. NONE of the
  zero-convergence conclusions transfer to the half-infinite Gilbreath
  triangle: Eppstein 2011 (held, "Anti-Gilbreath sequences") constructs
  2-then-odds sequences with small gaps whose right edge escapes and
  re-enters the good regime infinitely often — the half-infinite object
  cannot be governed by the cyclic zero-convergence laws. The approach's
  honest tension (Eppstein's right-edge injection defeating a global
  max-decrease) is now documented as the correct diagnosis: the localization
  to a left window is exactly the move that cannot be imported from the
  cyclic literature, because the cyclic theorems have no "right edge" at all.

  CONSEQUENCE for the proposal: the "sharp left-window max-decrease lemma
  with explicit f(L)" is NOT in the Ducci literature (the cyclic theorems
  give no windowed version), so it would be a genuinely new statement, not a
  known one to source. The grounded, transferable asset is the factored-max +
  rigidity-classification proof TEMPLATE, applied to windows of a
  half-infinite row. What would falsify the approach: a computation showing
  the first-window maximum M_k(L) for the primes reaches ≥ 4 in a short
  window L at some depth ≤ 1000 (changing "M_k(L) <= 2 for all k" from
  conjecture to refuted), or a Ducci-theorem statement that the windowed
  max-decrease is false in the half-infinite class (Eppstein's construction
  is the closest known analogue and only defeats the GLOBAL version).
status: proposed
first-step: |
  Write a small checker that computes, for each prime row to depth 1000, the
  localized maxima M_k(L) = max_{1 <= i <= L} A_k(i) for a few fixed windows
  L in {2,4,8,16,32}, and test the two exact facts ((1) monotonicity of M_k(L)
  after accounting for the right-shift of the window as rows descend, (2) "a
  value persists only next to a 0"). Then state the precise conjecture: for
  which L does M_k(L) <= 2 for all k, and what is the minimal counterexample
  configuration (which row, which position first carries a value >= 4 into the
  window). Compare that configuration to CHT's two obstructions and to
  Eppstein's right-edge injection. This gives research a concrete claim to
  source against the Ducci max-decrease literature.
```
