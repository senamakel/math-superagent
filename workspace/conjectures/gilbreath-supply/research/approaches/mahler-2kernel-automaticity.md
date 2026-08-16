# Contrapositive via Mahler's 2-kernel: small ν₂ forces h to be 2-automatic

```approach
idea: >
  Attack SUPPLY by its contrapositive, classified by the 2-kernel: if
  ν₂(n)/n → 0 on a density-1 set of n, then the prime-gap window satisfies
  ⊕_{s⊆d} τ[s] = 0 for all but o(n) of the frequencies d, which forces the
  2-kernel of the string τ (equivalently h) to be finite-dimensional, hence —
  by Mahler's method / Christol's theorem — forces the prime gap-parity string
  to be 2-automatic. The primes are not 2-automatic, so SUPPLY holds. The number
  theory is only the (cheap, conditional) non-automaticity of the primes.

mechanism: >
  ν₂(n) = #{d : T(n,d)=1}, and T(n,d) = 0 means the window satisfies the linear
  equation XOR_{s⊆d} τ[n−1−s] = 0. A string whose 2-kernel — the set of
  subsequences τ along arithmetic progressions with step a power of two, the
  Mahler normal form — spans a finite-dimensional space over F2 is 2-automatic;
  equivalently (Christol) its generating function is algebraic over F2(x).
  Allouche–Shallit's treatment of the ring of k-regular sequences is already on
  disk (allouche_shallit_kregular_sequences, allouche_shallit_kregular_II).
  So the route is: (a) a small-ν₂ set gives many annihilating equations
  XOR_{s⊆d} τ[s] = 0 over the submask lattice, which — by the Möbius involution —
  force the 2-kernel's dimension to be bounded on a density-1 set; (b) Mahler/
  Christol then make τ 2-automatic; (c) the prime gap-parity string is not
  2-automatic (its first difference is the primes mod 4; automaticity would make
  the prime-indicator an automatic set, contradicted by a sparsity/density
  theorem). This is the contrapositive of the broken general equivalence: the
  general statement failed only because h = e_{2^m} is sparse yet amplifies; the
  2-kernel route avoids that witness because e_{2^m} has an infinite 2-kernel
  dimension and is not 2-automatic — the amplification witness is exactly the
  case the automaticity condition rules out. The mechanism therefore uses Φ's
  Möbius structure to bound ν₂ from below, with the prime input only at step (c).

status: refuted

killed-by: >
  The central inference (a) — "small ν₂ (sparse Möbius/ANF support of the
  windows) on a density-1 set of n forces the 2-kernel of the infinite string τ
  to be finite" — is unsupported and is not a theorem. The 2-kernel of τ is
  spanned by the subsequences τ(2^j m + r) over all j,r; finiteness of that span
  is a rigid GLOBAL condition on the single infinite string. Small ν₂(n) only
  constrains individual windows τ_n locally (their ANF weights), and on a
  density-1 set these are local, n-specific constraints. No theorem in the
  literature connects "window ANF is sparse on a density-1 set" to
  "finite-dimensional 2-kernel", and none could evidently, since the e_{2^m}
  amplification witness (switch-equivalence.md) shows sparse window structure
  coexisting with linear fold weight while the coherent 2-kernel condition
  simply does not follow. The Möbius involution (step a's engine) is a
  bijection on each fixed window; it does not transfer to a global
  finite-dimensionality statement about the infinite string.

precedent: >
  The pieces that ARE real: Christol's theorem / finite k-kernel ⟺ k-automatic
  (Allouche–Shallit, "The ring of k-regular sequences" I & II, on disk
  allouche_shallit_kregular_sequences / _II), which is exactly step (b). Step
  (c) has ONE sound, well-sourced half: the prime INDICATOR χ_P (n ↦ 1_P(n))
  is not k-automatic for any k — Hartmanis–Shank 1968, restated in Coons 2008
  arXiv:0810.3709, Schützenberger 1968 (no infinite subset of primes is
  finite-automaton recognizable; see Rigo's Recognizable sets, Minsky–Papert
  gap argument). But the string h = ((q_{j+1}−q_j)/2) mod 2 is the gap-parity
  BY-PRIME-INDEX string, NOT the prime indicator by integer value; no source
  found proves THIS string non-automatic, and it is not reducible to χ_P's
  non-automaticity in any sourced step.

grounding-note: >
  Verified: step (b) is a genuine classical theorem; the non-automaticity of the
  prime indicator (not the gap-parity string) is genuinely established. Refuted
  on: step (a) is the load-bearing inference and it does not hold — there is no
  source and no evident mechanism making density-1 sparse window ANF imply a
  finite 2-kernel. The route's promised "sidestep of the e_{2^m} witness" is
  therefore not earned: the witness is excluded only by asserting the conclusion
  (finite 2-kernel) rather than by showing the premise forces it. Step (c) is
  additionally overclaimed for the gap string specifically — I searched "prime
  gap string automaticity" and "prime gap sequence not automatic" and found no
  proof that the by-index gap-parity string is non-automatic; only the prime
  indicator is established so.

first-step: >
  Price the two number-theory-free halves before any computation: (i) read the
  exact statement of the finite-2-kernel ⟹ 2-automatic theorem in
  Allouche–Shallit (on disk) and Christol, and write it as a claim block with
  hypotheses; (ii) establish the claim "the prime gap-parity string h is not
  2-automatic" — check whether automaticity of h forces automaticity of the
  prime-indicator sequence and obtain a contradiction, and record which theorem
  (Cobham, sparsity of automatic sets, Christol + transcendence) gives it. If
  (ii) turns out to require an unproved input, that is the arithmetic cost, and
  it is priced before any computation is spent.
```
