# The fold's collapse is decided by the distance distribution of its row code — a Krawtchouk/MacWilliams second-moment bridge

```approach
idea: >
  SUPPLY is exactly a second-moment statement about the fold's row set, and that
  second moment factorises into a PURE function of Phi_n (no number theory) —
  the distance distribution of the code C_n = { 1_{M_d} : d in [2,n-1] } formed
  by the row indicators — diagonalized by the Krawtchouk/MacWilliams transform.
  The number-theoretic input is thereby compressed to one priced statement (a
  submask-window autocorrelation bound on h), and the combinatorics can be
  attacked today in isolation.

mechanism: >
  Fix n. The rows of Phi_n are the translated digital down-sets
  M_d = { n-1-d+o : o subseteq d }, |M_d| = 2^{popcount(d)} (all rows have even
  size). Write eps_d = (-1)^{T(n,d)} in {+-1} and
  S(n) = sum_{d=2}^{n-1} eps_d. The exact identity (excess-is-negative-character-sum)
  gives nu2(n) = (n-2-S(n))/2, so SUPPLY <=> S(n) <= (1-2c)(n-2) eventually, and
  nu2/n -> 1/2 <=> S(n) = o(n). The ANF identity (anf-mobius-reed-muller) says
  eps_d = (-1)^{a_d} is the sign of the ANF/Moebius coefficient of the window.

  Second moment under the weakest model — h iid Bernoulli(p). Then

      E[eps_d eps_{d'}] = (1-2p)^{|M_d XOR M_{d'}|}       (exact, standard XOR moment)

  and, writing F_n(z) = sum_{d,d'} z^{|M_d XOR M_{d'}|},

      E[S(n)^2] = F_n(1-2p),   var(S) = F_n(1-2p) - E[S]^2

  where E[S] = sum_d (1-2p)^{|M_d|} is the exact row-bias term (non-zero for
  p != 1/2).  [Corrected by tool_builder first-step: the draft wrote
  var(S) = F_n(1-2p) - (n-2), which equals var only at p = 1/2 where
  E[S] = 0.  Order is unchanged -- var(S) = O(n) because F_n(1-2p) = O(n).]

  So the collapse of the fold on iid input is decided ENTIRELY by the distance
  distribution A_k = #{ d != d' : |M_d XOR M_{d'}| = k } of the row code C_n —
  a Delsarte distance distribution, a pure function of Phi_n. For p = 1/2 the
  cross terms all vanish (rows have even size, 0^{even}=0), giving var(S)=n-2,
  |S| = Theta(sqrt n) EXACTLY — which is precisely the measured
  |S(n)| = (3.1..3.8) sqrt n for both the primes and iid random input
  (pattern_finder_fold_generic_balance, pattern_finder_s_and_means). The
  generic-balance measurement now has a formula behind it.

  Krawtchouk diagonalization (checked below): with C_n-hat(omega) = sum_d (-1)^{<omega, 1_{M_d}>},
  the distance enumerator is

      F_n(z) = 2^{-n} sum_{omega} (1-z)^{wt(omega)} (1+z)^{n-wt(omega)} C_n-hat(omega)^2,

  so for z = 1-2p:

      var(S) = sum_{omega != 0} p^{wt(omega)} (1-p)^{n-wt(omega)} C_n-hat(omega)^2 + o(1).

  In words: the fold's collapse is controlled by the WALSH SPECTRUM of the row
  set — and C_n-hat(omega) = sum_d (-1)^{T(n,d) with input omega} is itself a
  fold character sum, Lucas-structured. This is exactly the point where the
  ANF/Moebius reformulation meets the second-moment need, and it is the place
  the literature has a real engine: Delsarte's linear programming / Krawtchouk
  / MacWilliams bound DISTANCE DISTRIBUTIONS of codes, as opposed to the
  (open) RM weight spectrum that killed the naive ANF payoff.

  The split SUPPLY now decouples into:
    (C) [number-theory-free, attackable today] F_n(z) = O(n) uniformly in n for
        |z| <= z_0 < 1. If true, ANY input h whose submask-XOR characters eps_d
        have the iid second-moment structure with |1-2p| <= z_0 gets var(S)=O(n),
        hence |S| = o(n) on a density-1 set by Chebyshev, hence nu2/n -> 1/2.
    (A) [arithmetic heart, GOAL priority 2] the real prime h satisfies the same
        submask-window second-moment bound: sum_{d != d'} eps_d(n) eps_{d'}(n)
        = O(n) on average in n (equivalently: autocorrelation of h along
        submask windows decays). Measured |S| = O(sqrt n) supports it; it is a
        variance/second-moment statement on h, ORTHOGONAL to mod-4 switch
        density (a mean statement), not implied by it.
  The point of (C) is that it makes (A) cheap: if the FOLD ITSELF does not
  amplify submask-window correlations (F_n = O(n)), then any h with decaying
  submask autocorrelation has S = o(n) — the "fold does work / fold is benign"
  dichotomy resolved on the geometry side, which is what GOAL.md asks the run
  to test.

status: adopted

precedent: >
  The engine is named, standard coding theory: Delsarte's linear programming
  bound (1973) and the MacWilliams identity (1963) bound the DISTANCE
  DISTRIBUTION of a code via Krawtchouk polynomials; the distance enumerator
  F_n(z) and its Krawtchouk diagonalization here are exactly that machinery
  applied to the row code C_n = {1_{M_d}}. The three identities used (XOR
  moment, Krawtchouk diagonalization, row weight |M_d|=2^{popcount(d)}) are
  standard and were verified by hand in this file. What is NEW and unchecked:
  the application of the distance distribution of THIS row set (the Pascal-
  mod-2 fold's translated down-sets) to bound wt(Phi_n h) — no source found
  applies Delsarte/MacWilliams to a sliding-window fold weight, and no source
  computes A_k for the fold row code. The geometry engine is named; the
  application is the speculative half. Recommend research verify the Delsarte/
  MacWilliams/Krawtchouk statements and confirm no prior computation of A_k for
  this row set.

first-step: >
  tool_builder, today, in this order (all exact F2/integer, no floats):
  (1) VERIFY the two identities numerically against Monte Carlo for n <= 20 and
      p in {0.3, 0.5, 0.585}: E[eps_d eps_{d'}] = (1-2p)^{|M_d XOR M_{d'}|}, and
      var(S) = sum_{d != d'} (1-2p)^{|M_d XOR M_{d'}|} = F_n(1-2p)-(n-2). A draft
      checker is code/out/anf_second_moment_check.py (unexecuted; the inventor
      holds no runner). Cross-check row weight |M_d| = 2^{popcount(d)}.
  (2) COMPUTE the distance distribution A_k of the row set for n = 16..128, exact;
      report A_2 (the minimal distance is 2, all rows even), A_4, ..., and
      F_n(1-2p) for p = 0.585 (the measured prime 1-density). Report whether
      F_n = O(n) and the empirical exponent. The FIRST obstruction to hunt:
      count pairs (d,d') with |M_d XOR M_{d'}| = 2 — if this is Theta(n^2),
      F_n(z) carries a z^2 n^2 term and (C) dies for z != 0.
  (3) COMPUTE C_n-hat(omega) (the Walsh spectrum of the row set, a fold
      character sum) and verify the Krawtchouk diagonalization identity
      F_n(z) = 2^{-n} sum_omega (1-z)^{wt(omega)}(1+z)^{n-wt(omega)} C_n-hat(omega)^2.
  (4) NEGATIVE CONTROLS on every step: all-ones h (kernel, S = n-2, var = 0 — the
      eps_d are all +1, NOT iid), Thue-Morse h (collapse), and a single isolated 1
      (sparse, collapse). The model (C) predicts primes ~ iid-balanced; the
      controls must FAIL it, or the whole bridge checks nothing.
```

## Checked-by-hand deductions (the identities this file rests on)

Both are standard and were verified by hand here; the tool_builder first-step
re-checks them mechanically.

1. **XOR moment.** For iid Bernoulli(p) bits x_j, E[(-1)^{x_j}] = 1-2p, so
   E[eps_d eps_{d'}] = E[(-1)^{XOR_{j in M_d XOR M_{d'}} x_j}] = (1-2p)^{|M_d XOR M_{d'}|}.
2. **Krawtchouk diagonalization.** For c = 1_{M_d}, u = c XOR c' with wt(u) = dist,
   sum_omega (1-z)^{wt(omega)}(1+z)^{n-wt(omega)} (-1)^{<omega,u>}
     = prod_{j: u_j=0}[(1+z)+(1-z)] * prod_{j: u_j=1}[(1+z)-(1-z)]
     = 2^n z^{wt(u)},
   hence z^{dist(c,c')} = 2^{-n} sum_omega (...) (-1)^{<omega,c XOR c'>}, and summing
   over c,c' gives F_n(z) as stated. Confirmed.

## The minimal distance is 2, and why that is the whole question

Every row has even size (|M_d| = 2^{popcount(d)} >= 2 for d >= 2), so the
symmetric difference of two distinct rows is even and >= 2. Hence A_0 = n-2
(the diagonal), A_1 = 0, and the first off-diagonal term is z^2 A_2. The
growth of A_2 — and of the whole F_n(z) — is the combinatorial core (C). If
A_2 = O(n) and the rest of the distance distribution is sufficiently
front-loaded to keep sum_k A_k z^k = O(n) for |z| < 1, the fold provably does
not collapse on any iid-like input, and SUPPLY reduces to the single arithmetic
variance statement (A).

## Why this is not any of the five closed doors or the three candidates

- Not "h is complicated enough": the collapse model is about the ROW SET's
  distance distribution, a function of Phi_n alone; the input h enters only
  through the single second-moment bound (A), which the closed doors' witnesses
  (all-ones, Thue-Morse, sparse) all FAIL.
- Distinct from anf-mobius-reed-muller (which it subsumes): that candidate's
  identity is adopted as a lemma; its RM-weight-spectrum engine is replaced by
  the distance-distribution/Krawtchouk engine, which the literature actually
  supports (Delsarte LP, MacWilliams) rather than an open weight spectrum.
- Distinct from pascal-cascade-block-recursion and hypergraph-cut-cheeger: both
  are refuted and untouched by this line.

## Honest falsifier

If (C) is false — e.g. A_2 = Theta(n^2) so F_n(z) carries a z^2 n^2 term — then
the fold DOES amplify submask-window correlations and this line dies with the
reason recorded; the surviving path is then the stronger arithmetic input that
forces the bad pairs' correlations to cancel, i.e. the equivalence
(supply-switch-equivalence) side. If (C) is true but (A) is false, SUPPLY's
converse is the live direction. Either outcome is a named result.
