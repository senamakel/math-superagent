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
