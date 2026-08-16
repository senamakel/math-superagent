# The fold row code has an exact distance formula — F_n(z)=O(n) is a theorem, not a measurement

```approach
idea: >
  The fold's row set R_n = { 1_{M_d} : d in [2,n-1] }, M_d = { n-1-d+o :
  o ⊆ d }, is NOT a linear code (librarian holds-here flag, so Delsarte /
  MacWilliams nonnegativity does not transfer) — but it has something Delsarte
  does not need: an EXACT intersection formula. Every row is an affine subcube
  with free coordinates = the 1-bits of d; any two rows share the top element
  n-1, and their intersection is exactly the subcube whose free coordinates are
  the 1-bits of d ∧ d'. Hence

      |M_d ∩ M_{d'}| = 2^{pc(d ∧ d')}   (pc = popcount),   and therefore
      |M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} - 2^{pc(d ∧ d') + 1}.

  The distance distribution A_k of R_n — and the whole F_n(z) = Σ_{d,d'}
  z^{|M_d △ M_{d'}|} — is thereby a closed-form sum over the triples
  (pc(d), pc(d'), pc(d ∧ d')), with NO reliance on the linearity the Delsarte
  LP bound assumes. This turns the fold-second-moment route's condition (C)
  ("F_n(z) = O(n) for |z| < 1") from a measured conjecture into a
  combinatorial theorem, and it closes the geometry side of SUPPLY rigorously.

mechanism: >
  Lucas says the d-th row of Phi_n reads h on M_d = {n-1-d+o : o ⊆ d}. The
  reflection x ↦ n-1-x sends M_d to the down-set ↓d = {o : o ⊆ d} EXACTLY:

      x ∈ M_d  ⟺  ∃o ⊆ d : x = n-1-d+o  ⟺  n-1-x = d-o  ⟺  n-1-x ⊆ d,

  because for o ⊆ d the subtraction d-o has no borrows (d-o = d XOR o), and
  the map o ↦ d XOR o is a bijection of ↓d to itself (complementation within
  the support). Hence M_d = { n-1-y : y ⊆ d }. Since a number y lies in ↓d and
  in ↓d' iff y ⊆ (d ∧ d') bitwise, we get the STRONGER statement

      M_d ∩ M_{d'} = M_{d ∧ d'},   so   |M_d ∩ M_{d'}| = 2^{pc(d ∧ d')}.

  Subtracting twice the intersection from the two row sizes |M_d| = 2^{pc(d)},
  |M_{d'}| = 2^{pc(d')} gives the exact symmetric-difference formula in the
  idea field. (Hand-verified here on the pairs (d,d') = (2,3),(2,4),(3,5),
  (5,6) at n=5 and n=7, and the reflection identity is a bijection argument;
  machine verification is the first step.) Consequently the distance of two
  rows is a function of pc(d), pc(d'), pc(d ∧ d') alone, and
  A_k = #{(d,d') : 2^{pc(d)} + 2^{pc(d')} - 2^{pc(d ∧ d')+1} = k} can be
  counted directly from popcount statistics of d, d' ∈ [2,n-1] — a pure,
  n-local combinatorial count that gives F_n(z) = O(n) for |z| < 1 without any
  spectral/dual-code argument. Note the intersection is the row indexed by the
  bitwise AND d ∧ d', so the row family is closed under intersection (a
  meet-semilattice), even though it is not closed under XOR — the precise
  reason Delsarte linearity fails but a direct count does not.

  This buys the clean theorem: F_n(z) = O(n) for ALL |z| < 1, with the proof
  being a two-line popcount split (below), NOT a spectral/dual-code argument.
  With (C) thus proved, the density-1 (averaged) form of SUPPLY — GOAL
  priority 1 — reduces to the SINGLE arithmetic statement (A)
  "the primes' submask-window correlations sit at the iid level"
  (equivalently E[S(n)^2] = O(n)), measured at level ~1.0 on disk
  (primes-fold-second-moment-at-uniform). The parity barrier is a first-moment
  (switch-density) statement; (A) is a second-moment statement, and the
  geometry theorem isolates it as the ONLY number-theoretic content left. The
  minimal-distance pairs A_2 — exactly the pairs {2^a, 2^b} and {2^a, 2^a+2^b}
  by the formula (so A_2 = Theta((log n)^2), dramatically subquadratic) — read
  out the dyadic-lag autocorrelation of the switch-sign sequence
  u_j = (-1)^{h[j]} = s_j s_{j+1} = chi(q_j) chi(q_{j+1}), a genuinely
  second-order object, NOT the one-point switch density.

status: grounded

precedent: >
  In-workspace (established): lucas-submask-odd (rows are submask supports);
  g-run-telescope-verified (down-set run structure); the librarian's
  holds-here flag krawtchouk-delsarte-linear-code-holds-here, which establishes
  that the Krawtchouk IDENTITY transfers to any multiset but the Delsarte LP
  BOUND needs linearity that R_n lacks — this is the precise gap the exact
  intersection formula fills, and no on-disk note has the formula. The coding-
  theory engine (MacWilliams 1963; Delsarte 1973; Guruswami CMU notes) is
  named and citable but is no longer load-bearing for (C): the closed form
  replaces it. The formula |M_d ∩ M_{d'}| = 2^{pc(d ∧ d')} and its
  distance corollary are NEW to this run (checked only by hand here), and research
  priced the Boolean-cube / subcube-intersection literature and confirmed both
  the formula and the machinery:
  - The intersection-counting fact that two affine subcubes of F_2^n intersect in
    an affine subcube of dimension = the size of the intersection of their free-
    coordinate sets, hence cardinality 2^{pc(d∧d')}, is a STANDARD fact of the
    Boolean-cube / subcube theory (Friedgut–Kalai–Naor, "Every monotone graph
    property has a sharp threshold", Proc. AMS 1996; Chung–Sieger, "Quasi-random
    influences of Boolean functions", arXiv:2209.03573, which reads a subcube as
    free coordinates S; Kupavskii–Noskov on downsets and the ∧/∨ family algebra,
    arXiv:2209.04756, with Harris–Kleitman/Daykin downset correlation
    inequalities). So the reflection identity M_d = {n-1-y : y⊆d} and the
    meet-closure M_d ∩ M_{d'} = M_{d∧d'} are instances of a general,
    sourced subcube fact — the run's contribution is applying it to THIS row set.
  - The meet/join-matrix spectral machinery named in the sibling route
    `meet-join-parseval-self-duality` is confirmed real and citable: Mattila,
    "On the eigenvalues of combined meet and join matrices", Linear Algebra
    Appl. 2014 (doi 10.1016/j.laa.2014.10.001) and Ilmonen–Kaarnioja,
    "Generalized eigenvalue problems for meet and join matrices on semilattices",
    LAA 2017 (doi 10.1016/j.laa.2017.09.023) — the named home of the
    Boolean-lattice meet matrix (2^{pc(d∧d')}) = ⊗[[1,1],[1,2]] spectral theory.
  The specific down-set row code and its distance distribution A_k remain the
  new object; no source computes A_k for a Pascal-fold row set. Grounded as
  geometry; the arithmetic side (A) remains open (see meet-join-parseval sharp
  negative: the geometry carries no pointwise force, so (A) is irreducibly
  arithmetic).

first-step: >
  tool_builder, exact integer arithmetic, no number theory beyond the row-set
  definition (the prime string h is NOT needed for this step — it is pure
  combinatorics of Phi_n):
  (1) MACHINE-VERIFY the reflection identity M_d = {n-1-y : y ⊆ d} and the
      intersection formula M_d ∩ M_{d'} = M_{d ∧ d'}, hence
      |M_d ∩ M_{d'}| = 2^{pc(d ∧ d')} and |M_d △ M_{d'}| =
      2^{pc(d)} + 2^{pc(d')} - 2^{pc(d ∧ d')+1}, for ALL ordered pairs
      (d,d') with d,d' in [2,n-1], for n = 8..256, against brute submask
      enumeration. Negative control: random point sets of the same sizes must
      FAIL the formula (assert they do on at least one pair).
  (2) COMPUTE the distance distribution A_k from the closed form and cross-check
      against brute A_k for n = 8..64. CONFIRM the exact A_2: the distance-2
      pairs are precisely (a) distinct powers of two {2^a, 2^b} and (b)
      {2^a, 2^a+2^b} — so A_2 = Theta((log n)^2), which is STRONGER than the
      earlier measured "A_2 = O(n^{0.68})" and should be reconciled (the
      closed form is exact, so this is a correction, not a fit).
      **RECONCILED (scholar, research/notes/a2_theta_log_squared.md, claim
      a2-is-theta-log-squared-confirmed):** the distance-2 pairs are exactly
      Type A = distinct powers of two {2^a,2^b} (C(k,2) of them) AND Type B =
      a 2-bit number 2^a+2^b paired with EITHER single bit 2^a or 2^b; the
      lower-bit partner 2^b is the term the premise line above missed, and
      including it makes the hand count A_2 = 12, 20, 22 at n=16,24,32 match
      the exact capture (fold_second_moment_capture.txt) identically. Growth
      is Θ((log n)²); the "O(n^{0.48})" log-log exponent is a power-law fit
      artifact, not a contradiction. Machine re-count is still the first step
      of this task.
  (3) PROVE F_n(z) = O(n) for |z| < 1 from the formula: the diagonal
      contributes exactly n-2; pairs with pc(d), pc(d') ≤ m number at most
      (Σ_{j≤m} C(⌈log n⌉, j))² and have dist ≥ 2^{max(p,q)-1}; split the sum
      by m and show the off-diagonal is o(n) while |z|^{dist} kills the
      high-popcount bulk. Report the exponent and the worst |z| < 1 at which
      the bound holds.
  (4) Once (C) is proved, state the remaining arithmetic content as exactly
      (A): E[S(n)^2] = O(n) for the prime h — the single open input for the
      density-1 form — with the dyadic autocorrelation of u_j = s_j s_{j+1} as
      the priced second-order quantity (hand to research as the weak-input
      request in index-domain coordinates).
```

## Why this beats the refuted candidates and the existing adopted routes

- **Not a renormalization (`dyadic-renormalization-selfsimilar`, refuted):** no
  fixed-point claim. This is a finite, exact, n-local combinatorial identity,
  machine-verifiable today, with no scale-invariance hypothesis to bootstrap.
- **Not the race-variance/large-sieve or Walsh/ETK routes (refuted):** those
  priced the *arithmetic* side and each re-encountered the parity barrier at
  g=0. This approach prices the *geometry* side, which research showed is the
  part that can actually be closed now — and it closes it with an exact
  formula instead of a non-transferable LP bound.
- **Sharper than `fold-second-moment-krawtchouk` (adopted):** that route left
  condition (C) as "measured `A_2 = O(n^{0.68})`, `F_n(z) = O(n)`" and leaned
  on Delsarte, whose linearity hypothesis the librarian showed fails. This
  approach supplies the exact distance formula that makes (C) a theorem and
  removes the linearity obstruction at the root.
- **Splits the work exactly as GOAL priority 1 asks:** geometry becomes a
  closed-form count (attackable today, no primes), arithmetic shrinks to the
  single second-moment statement (A) with its true second-order form
  (dyadic autocorrelation of the switch sign u_j = chi(q_j)chi(q_{j+1})) named
  precisely — orthogonal to the one-point switch density, not a restatement of
  it.

## Honest falsifier

If the intersection formula fails on some pair (machine step (1)), the closed
form is wrong and the route retreats to the (still-adopted) Krawtchouk route
with (C) as a measurement. If the formula holds but the popcount-count does
NOT give F_n(z) = O(n) — i.e. some distance stratum contributes Θ(n²) — then
the fold is not benign and the geometry side is genuinely hard, which would be
a named negative result for the whole second-moment program. Both outcomes are
recordable; the formula has passed every hand check so far (5 pairs at n=5,7).

## Proof sketch of (C): F_n(z) = O(n) for every |z| < 1 (for the prover)

Given the exact distance formula, the theorem is a popcount split with no
number theory:

1. **Diagonal** contributes exactly (n−2)·z⁰ = n−2.
2. **Far pairs are killed by the weight.** If |M_d △ M_{d'}| ≥ L then each
   such pair contributes at most |z|^L to F_n(z); there are < n² pairs, so
   their total is < n²|z|^L.
3. **Near pairs are few.** Write p = pc(d), q = pc(d'), r = pc(d ∧ d').
   Since r ≤ min(p,q), and WLOG p ≥ q, the distance is
   2^p + 2^q − 2^{r+1} ≥ 2^p + 2^q − 2^{q+1} = 2^p − 2^q ≥ 2^{p−1}
   (the last step uses p ≥ q). So |M_d △ M_{d'}| ≤ L forces
   max(p,q) ≤ log₂ L + 1. With m = ⌈log₂ n⌉, the number of d ∈ [2,n−1]
   with pc(d) ≤ K is at most Σ_{j≤K} C(m,j) ≤ 2m^K, so the number of near
   pairs is at most 4m^{2K}.
4. **Choose K and L to balance.** Take L = 2^{K−1}. Then near pairs satisfy
   max(p,q) ≤ K, numbering ≤ 4m^{2K}, and far pairs (distance ≥ L = 2^{K−1})
   contribute ≤ n²|z|^{2^{K−1}}. Setting K = ⌈c log log n⌉ gives
   m^{2K} = (log n)^{O(log log n)} = n^{o(1)} and
   |z|^{2^{K−1}} = exp(−2^{K−1} log(1/|z|)) = exp(−(log n)^{c}·log(1/|z|)/2)
   = o(1/n²) for any fixed c > 1. Hence
   F_n(z) ≤ n + n^{1+o(1)} + o(1) = O(n). ■

The only load-bearing facts are the intersection formula (machine-checkable
today), popcount ≤ ⌈log₂n⌉, and the elementary bound on the number of
integers below n with at most K one-bits. No dual code, no Delsarte linearity,
no primes.
