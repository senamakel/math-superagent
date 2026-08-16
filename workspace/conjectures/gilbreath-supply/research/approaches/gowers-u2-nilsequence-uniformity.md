# SUPPLY is U²-uniformity of the prime character over the dyadic odometer — Green–Tao nilsequence orthogonality

```approach
idea: >
  The adopted route `lucas-mixing-finite-transfer` is stuck on a missing tool: a
  QUANTITATIVE finite transfer from correlation decay to a density-1 weight
  bound. That tool exists in a different, named world — Gowers uniformity and
  Green–Tao nilsequence orthogonality. Recast SUPPLY as: the sequence
  s_j = χ(q_j) = (−1/q_j) is U²-uniform over the dyadic odometer, i.e. its
  correlation with every submask/down-set indicator (a degree-1 character of the
  dyadic group) is small. Then S(n) = Σ_d (−1)^{T(n,d)} is a sum of U²-linear
  characters evaluated at s, and its smallness follows from the Green–Tao
  "Möbius randomness law" — the strong orthogonality of the Liouville-type sign
  along primes to low-complexity nilsequences — without ever resolving the
  mod-4 switch-density mean.

mechanism: >
  Lucas' theorem makes the fold read h along the down-sets ↓d; exponentiated,
  (−1)^{T(n,d)} is the value of the character χ_{↓d} of the 2-adic group at the
  prime-indexed sign s. The functions 1_{↓d} are exactly the degree-1 characters
  (polynomial phases of degree 1) on the dyadic odometer Z₂. Hence
  S(n) = Σ_{d≤n} ⟨s, χ_{↓d}⟩ is the sum of the degree-1 Fourier coefficients of
  s over a growing window — and S(n) = o(n) is precisely the statement that s
  has no degree-1 (dyadic) bias, i.e. s is U²-uniform along the dyadic scales.

  This is the exact finite, quantitative shadow of "Lucas mixing" that
  Pivato–Yassawi (adopted) state only qualitatively for measures. The engine
  that fills the missing transfer is named: Green–Tao, "The Möbius function is
  strongly orthogonal to nilsequences" and "The quantitative behaviour of
  polynomial orbits on nilmanifolds" (both Ann. Math. 2012), together with the
  Gowers U^k inverse theorem (Green–Tao–Ziegler): a sequence failing to be
  U²-uniform correlates with a degree-1 nilsequence, and a Liouville-type
  multiplicative sign AT THE PRIMES is strongly orthogonal to such
  low-complexity nilsequences. The relevant object is λ at primes = (−1)^{Ω}
  weighted by prime indicator, whose orthogonality to 2-step/dyadic
  nilsequences is exactly the shape of the theorems above (with the caveat
  below).

  The priced input is therefore NOT "s is complicated" (five doors) and NOT the
  switch-density mean (ABGS): it is a single U²-uniformity / nilsequence
  orthogonality statement about χ at primes, an object the additive-combinatorial
  literature actually bounds at low complexity, and which is ORTHOGONAL to the
  one-point mean (claim lucas-mixing-orthogonal-to-switch-density, asserted).

status: refuted

precedent:
  - "Green & Tao, The Möbius function is strongly orthogonal to nilsequences,
    Ann. of Math. 175 (2012) 541–566, arXiv:0807.1736. EXACT statement
    grounded: for G/Γ a nilmanifold, g:Z→G a polynomial sequence, F Lipschitz,
    |(1/N)Σ_{n≤N} μ(n)F(g(n)Γ)| ≪_{F,G,Γ,A} log^{-A} N for every A>0. The
    orthogonality is of MÖBIUS/LOUISVILLE evaluated at the value n, in the
    Walsh/classical additive-combinatorial sense, against a nilsequence F(g(n))."
  - "Green, Tao & Ziegler, An inverse theorem for the Gowers U^{s+1}[N]-norm,
    Ann. of Math. 176 (2012) 1231–1372. The U^2/Gowers inverse theorem lives on
    the WALSH/Fourier basis chi_S(x)=(-1)^{<S,x>} of {0,1}^m; a sequence with
    large U^2-norm correlates with a degree-1 phase."
  - "Pivato & Yassawi, Asymptotic randomization of sofic shifts (2006) Thm 7.1,
    arXiv:math/0306136 (adopted, on disk)."
  - "On-disk claims: lucas-mixing-iff-fold-randomization (sourced),
    lucas-mixing-orthogonal-to-switch-density (asserted),
    supply-fold-submask-zeta-involution (the fold cell is the F2 Möbius/zeta
    transform = ANF coefficient, NOT a Walsh character)."
killed-by: >
  BASIS MISMATCH. The reformulation equates 'S(n)=o(n)' with 's is U^2-uniform
  over the dyadic odometer', claiming that the fold reads degree-1 characters
  (Walsh phases chi_S = (-1)^{<S,x>}) of the dyadic group and that the fold sum
  S(n)=Σ_d (−1)^{T(n,d)} is a sum of their Fourier coefficients. Both the U^2
  norm and the Gowers/green–Tao inverse theorem (and the nilsequence
  orthogonality it inverts) live on the WALSH basis chi_S. But the fold cell
  (−1)^{T(n,d)} is NOT a Walsh character: by Lucas, T(n,d)=⊕_{o⊆d} h[n-1-d+o]
  is the F2 Möbius/zeta (submask-XOR) transform — the ALGEBRAIC NORMAL FORM
  coefficient of a window, on the DOWN-SET/Zeta basis, which is one Möbius
  transform away from the Walsh basis (the two diagonalise different matrices;
  the down-set indicator 1_{↓d} is a degree-popcount(d) ANF polynomial and is
  NOT equal to any Walsh character chi_S). So the folds S(n) are sums of ANF
  (zeta-basis) coefficients, not of U^2 Fouriier (Walsh-basis) coefficients, and
  'U^2-uniformity' — a Walsh/Wiener-basis notion governing the Green–Tao /
  Gowers inverse theorem — does not bind S(n). Concretely: green-tao nilsequence
  orthogonality is a theorem about Möbius at INTEGER VALUES (μ(n) against
  F(g(n)Γ)); here the object is chi(q_j)=(-1)^{(q_j-1)/2} at PRIME INDEX j, and
  the low-complexity 'characters' it is folded against are zeta/ANF functions,
  not Walsh/nilsequences. The quantitative finite transfer the adopted
  lucas-mixing route lacks is therefore NOT supplied: the machinery named
  (Gowers U^2, Green–Tao, GTZ inverse theorem) governs a different basis and
  does not touch this fold. The route is a genuine change of world, but the
  world it names is the wrong one for the object; the reformulation cannot even
  be stated in that world. (The candidate's own open-step (a) — derive
  'S(n)=o(n) ⟺ s is U^2-uniform' — is exactly the step that fails, because the
  two sides live on different bases.)
open-step: >
  The precise finite transfer, now with a named engine. (a) The exact statement
  "S(n) = o(n) ⟺ s is U²-uniform over the dyadic odometer" must be derived —
  this is the quantitative replacement for the qualitative ergodic transfer the
  adopted route lacks. (b) Whether χ-along-primes is strongly orthogonal to
  degree-1 dyadic nilsequences is exactly a two-point/parity-type statement at
  the dyadic scales, and at scale g=0 it re-encounters the adjacent-pair parity
  barrier; the LIVE hope is the AVERAGED over dyadic scales (the sum over d),
  which is a U² statement and is plausibly weaker than pointwise switch density.
  Both (a) and (b) must be priced, not assumed.
first-step: >
  tool_builder, exact F₂ + character arithmetic on the real s_j = χ(q_j):
  (1) compute the degree-1 (dyadic) Fourier coefficients of s over windows of
  length 2^m for m ≤ 12 — i.e. for each submask/character χ_{↓d} compute
  ⟨s, χ_{↓d}⟩ — and print max over d of |⟨s,χ_{↓d}⟩|/window; the falsifier: if
  the max does not decay like o(window), the U²-uniformity input fails for the
  real primes and the route is dead; (2) verify the identity S(n) = Σ_d ⟨s,χ_{↓d}⟩
  against the fold oracle for n ≤ 200, with all-ones and Thue–Morse as negative
  controls (both must show LARGE low-degree bias, exhibiting the collapse);
  (3) hand the per-degree bias table to research as the priced U² input, labelled
  a measurement, not a proof.
```

## Distinctness and honesty

- **Not a restatement of** `lucas-mixing-finite-transfer` (adopted): that route names the qualitative ergodic theorem and stops at the missing transfer. This route supplies the *quantitative engine* for exactly that transfer — Gowers U² / Green–Tao nilsequence orthogonality — which is a different, finite, quantitative world.
- **Not** `anf-mobius-reed-muller` (refuted): that route asked for the *weight spectrum* of the Reed–Muller code (open). This route asks for U²-uniformity of the *arithmetic sequence* s, a bound on low-degree Fourier coefficients, not the full weight spectrum.
- **Not** `walsh-subset-sum-fold-structure` (refuted): that route sought a bound from Φ alone valid for all x and died on kernel vectors. This route's input is the arithmetic sequence χ(q_j), and the kernel vectors (all-ones etc.) are exactly the inputs with maximal low-degree bias — the negative controls, not counterexamples.

**Speculative half:** whether U²-uniformity of χ-along-primes over dyadic scales is strictly weaker than positive mod-4 switch density. It is orthogonal to the mean (established for the Bernoulli model), but its quantitative content at scale g=0 is the adjacent-pair parity question, which is the named open barrier. If the averaged-over-scales form turns out to require that barrier, the finding is that Lucas mixing at low complexity IS the parity barrier — a genuine negative result for GOAL priority 3.
