# SUPPLY ⇔ switch density (the equivalence / negative closure)

GOAL.md priority 3 (result 5): determine whether SUPPLY is equivalent to the
positive mod-4 switch-density statement, and prove it if that is the truth.
The known direction is asserted available; only the converse is open. This
skeleton is the complement of `supply-from-endpoint-parity.md`: proving it
closes the "weaker input" question negatively; refuting it is evidence for the
positive direction there.

```skeleton
goal: >
  Equivalence theorem: SUPPLY ⇔ SWITCH, where
  SWITCH := liminf_{n→∞} (1/n)·#{j ≤ n : q_{j+1} ≢ q_j mod 4} > 0
  (a positive density of adjacent mod-4 switches; equivalently h[j]=1 on a
  positive-density set).

implies: >
  SWITCH ⇒ SUPPLY is the known reduction (problem.md "the reduction that exists",
  asserted available, and discards Φ). So equivalence reduces to the single
  converse lemma G-sup-sw: SUPPLY ⇒ SWITCH. Its contrapositive is: if switch
  density has liminf 0 — i.e. along some n_i → ∞ the window h[0..n_i] carries
  o(n_i) ones — then ν₂(n_i)/n_i → 0, contradicting SUPPLY. Hence

      G-sup-sw  +  (known SWITCH ⇒ SUPPLY)   ⊢   SUPPLY ⇔ SWITCH.

  Quantifier care: the contrapositive must be stated for the windowed transform
  T(n,d) = ⊕_{o ∈ [0,d], o ⊆ d} h[n−1−d+o] of `supply-from-endpoint-parity.md`,
  NOT for the absolute zeta transform ⊕_{j ⊆ d} h[j]. The absolute form is FALSE
  as a general transfer — a single 1 in h (h = e_{2^k}) puts a 1 in s(d) for every
  d ⊇ 2^k, so sparse h can have heavy s — and this is the amplification the lemma
  must state around rather than against.

status: sketched

rests-on: >
  problem.md fact 1 (linearisation ν₂ = wt(Φ_n h)) and the asserted available
  reduction SWITCH ⇒ SUPPLY. Both asserted, neither ledger-grounded; the oracle
  must re-ground fact 1 before this chain is used. The run-telescoping form
  T(n,d) = ⊕_R [r_{a_R} ≢ r_{b_R}] from G-run-telescope is taken as notation here,
  not as a resting assumption of the equivalence argument itself.
```

```gap
id: G-sup-implies-switch
lemma: >
  For h arising from the primes (h[j] = [q_{j+1} ≢ q_j mod 4]), if a window
  h[a..b] has w ones with w = o(b−a), then its diagonal contribution
  #{d : T(b,d) = 1} is o(b−a). Precisely: liminf of switch density 0 forces
  liminf ν₂(n)/n = 0. The windowed form is essential; the absolute-zeta form of
  this statement is false (single sparse 1 amplifies), so the lemma's exact
  transform and window must be pinned first.
status: open
next: >
  First establish the truth before trying to prove it, because a refutation sends
  the run to `supply-from-endpoint-parity.md` instead. smt_solver/sat_solver:
  search for a {1,3}-valued boundary sequence r (so h is its mod-4 boundary) with
  o(n) ones whose windowed transform T(n,d) is 1 on a linear fraction of d — a
  witness refutes G-sup-sw and disproves the equivalence (making SUPPLY strictly
  weaker than SWITCH). If no witness up to the search bound, theorem_prover:
  prove the contrapositive via T(n,d) = ⊕_R [r_{a_R} ≢ r_{b_R}] by bounding how
  many d can have an odd number of runs "seeing" the o(n) scattered ones. Either
  outcome is a concrete, checkable first move; a negative control (all-ones h ⇒
  ν₂ = O(1), not the sparse case) must be included so the search is not vacuous.
```

## Cross-link

If G-sup-sw is refuted (a witness found), the equivalence is false and the
positive skeleton `supply-from-endpoint-parity.md` is the path; record the
witness as a claim so the search is not repeated. If G-sup-sw is proved, the
problem is closed honestly as equivalent to the known-hard switch-density
statement, and the run should report that rather than chase the fold further.
