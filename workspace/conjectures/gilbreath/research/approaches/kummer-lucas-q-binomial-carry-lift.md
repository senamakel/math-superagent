```approach
idea: Kummer–Lucas / Gaussian-binomial closed form for the F2 → Z lift — the integer "carries" that the absolute-difference operator introduces are exactly the binomial-coefficient carries classified by Kummer's and Lucas's theorems, so the full (unhalved) triangle is a q-deformation of the Pascal-mod-2 (Rule 90) triangle, and A_k(1) has a closed form as a Gaussian-binomial transform whose boundedness can be attacked algebraically.

mechanism: |
  Established (this run, rule90-interior-xor): inside any {0,2} block the
  halved entries are {0,1}-valued and evolve by XOR, i.e. the mod-2 Pascal
  law A_{k+d}(i)/2 = XOR_j [C(d,j) mod 2] · (A_k(i+j)/2). The run's mod4-pascal
  approach died because it tried to LIFT the congruence |a−b| ≡ a+b (mod 2^t);
  that lift is blocked at t=3 (it needs min(a,b) ≡ 0 mod 2^{t−1}, fails on
  |2−6|=4). This approach does not lift a congruence. It computes the
  SIGNED forward-difference triangle Δ_k(i) = Σ_{j≤k} (−1)^{k−j} C(k,j) a_{i+j}
  EXACTLY in the integers using Kummer's and Lucas's theorems, and treats the
  absolute value A_k(i) = |Δ_k(i)| only at the end as a single fold.

  The exact ingredients, all classical:
  - Lucas's theorem: C(n,k) mod p is the product over digits of C(n_i, k_i) mod p.
  - Kummer's theorem: v_p(C(n,k)) = the number of carries in k + (n−k) base p.
  - The Gaussian binomial [n choose k]_q = Σ q^{stat} (generating function of the
    "inversion/carry" statistic) interpolates between C(n,k) at q=1 and, at
    q=−1, the alternating "signed" binomial coefficient — which is precisely the
    kernel that makes the mod-2 Pascal triangle the Sierpinski gasket.
  So the lift from the F2 interior to the integer triangle is not an arbitrary
  "carry" bookkeeping (the two's-complement transducer, proposed separately);
  it is the q-binomial / carry statistic, with closed forms and Gaussian-polynomial
  identities (q-binomial theorem, q-Vandermonde, the q-Lucas analogue).

  Reformulation: write each halved-gap ancestor with its binary expansion. Then
  Δ_k(i) is a signed sum whose coefficients C(k,j) have 2-adic valuations given
  in closed form by Kummer (digit-wise), so Δ_k(i) mod 2^m is a digit-combinatorial
  function of the gaps. The conjecture A_k(1) ∈ {0,2} is exactly the claim that the
  folded value |Δ_k(1)| (plus the min-branch correction) never leaves {0,2}. The
  correction from the fold is the single obstruction every mod-lift hit; here it is
  kept as an explicit, separate, nonnegative term rather than discarded.

status: refuted
side: general-class / dynamical (the Kummer–Lucas lift is a property of the operator, not of primality; the primes only enter through the binary digits of the halved gaps)
killed-by: |
  REFUTED — the reformulation is the forward-difference / binomial-transform
  linearization, and its load-bearing identity A_k(i) = |Δ_k(i)| is FALSE on
  this problem, already established by held claim `fwd-diff-identity-refuted`
  (checked). First violation at (k,i)=(3,2), INSIDE the leading {0,2} block:
  the signed forward difference Δ_3(2) = 4 but the Gilbreath entry A_3(2) = 0.
  First violation at position 1 is k=4 (|Δ_4(1)| = 6, A_4(1) = 2); 17 of the
  first 20 rows fail. Mechanism: |u−v| = ||u|−|v|| holds iff u·v ≥ 0, and the
  signed difference triangle has ADJACENT OPPOSITE SIGNS (first pair
  (D_3(2), D_3(3)) = (2,−2), from any strict local extremum of the prime gaps,
  which the primes have at i=2: gaps 2,4). Because the sign pattern interleaves
  at every level, the absolute value is NOT an end-of-pipeline single fold; the
  min-branch activates throughout the light cone, so the "compute the signed
  part exactly via Kummer/Lucas, then fold once at the end" program has a false
  first premise. The candidate's speculative half — that the fold correction
  admits a closed form in the q-binomial/carry statistic — is exactly the
  min-branch activation pattern, which is the refuted sign-coherence /
  minimal-counterexample route (sign-coherence-forward-differences),
  structurally the same obstruction.

  What is TRUE and survives: Gaussian binomials [n choose k]_q genuinely
  interpolate C(n,k) at q=1 against the Sierpinski/Pascal-mod-2 kernel at
  q=−1, and Kummer/Lucas give the carry statistic — all classical (Granville's
  survey Kummer/Lucas/Sierpinski; Kubelka's self-similarity mod p; Fraenkel–
  Kontorovich q-sieves; Northshield's Pascal-mod-2 line sums). But that
  machinery governs the SIGNED linear part, whose absolute-value-identity is
  refuted at the first cell that matters (3,2) inside the block. It cannot be
  the q-deformation the candidate needs because the signed linear triangle is
  not sign-coherent here, and the fold is present at every level, not once.

  Verdict: refuted, killed by `fwd-diff-identity-refuted` at its first-statement
  cell. Do not re-propose the signed-forward-difference linearization for
  Gilbreath; an independent MathOverflow practitioner comment (held claim
  `mo-thread-practitioner-confirms-fwd-diff-dead-route`) confirms this is a
  known dead route ("I forgot about the absolute values of the differences").
precedent: |
  - held claim `fwd-diff-identity-refuted` (checked): A_k(i)=|Δ_k(i)| false at
    (3,2) inside the {0,2} block; anchor code/out/check_fwd_diff_identity.notes.md
  - held claim `sign-coherence-forward-differences` (refuted approach): the
    fold = min-branch activation is not digit-combinatorial; no closed form
  - held claim `mo-thread-practitioner-confirms-fwd-diff-dead-route`
  - The q-binomial/Kummer/Lucas machinery itself (real but misapplied):
    Granville, "Arithmetic properties of binomial coefficients" (Kummer:
    v_p(C(n,m)) = carries of m+(n−m) base p; Lucas); Kubelka 2004
    "Self-Similarity and Symmetries of Pascal's Triangles and Simplices Mod p"
    (doi 10.1080/00150517.2004.12428445); Fraenkel–Kontorovich, "The Sierpinski
    Sieve of Nim-varieties and Binomial Coefficients" (doi
    10.5281/zenodo.8346356); Formichella–Straub "Gaussian binomial coefficients
    with negative arguments" (arXiv:1802.02684); Northshield "Sums across
    Pascal's triangle modulo 2" (hdl.handle.net/1951/69939)
named-mathematics: Kummer's theorem, Lucas's theorem, Gaussian binomial coefficients (q-binomials), the q-binomial theorem and q-Vandermonde, the carry/inversion statistic, the Sierpinski gasket as Pascal mod 2
speculative: The honest load-bearing claim — that the min-branch fold correction itself admits a closed form in terms of the same q-binomial/carry statistic, so that A_k(1) is a single Gaussian-binomial transform and not an unsimplified 2^k-fold sum — is CONJECTURED, not established. If it fails, the Kummer–Lucas lift still gives an exact digit formula for the SIGNED part and leaves the fold as a bounded, separately-trackable correction.
falsifier: If no closed form for the fold correction emerges (i.e. the min-branch activation pattern along the light cone of (k,1) is not itself digit-combinatorial), then the approach degenerates into the refuted sign-coherence/minimal-counterexample route and should be refuted rather than pursued.
first-step: |
  (a) Reproduce Lucas/Kummer on the oracle: for the halved-gap row, compute
  Δ_k(i) = Σ (−1)^{k−j} C(k,j) g_{i+j} exactly for k ≤ 12 and verify
  Δ_k(i) mod 2 == XOR_j [C(k,j) mod 2] · (g mod 2) at every cell (this must
  hold — Lucas — and is the sanity check). (b) For the SAME cells compute the
  min-branch activation pattern (where |a−b| took the min branch) and test the
  load-bearing conjecture: is the set of activated cells, or the running count
  of activations along each light cone, expressible via the carry statistic
  of Kummer's theorem (base-2 carries of j + (k−j))? Report the first cell
  where the pattern deviates from the q-binomial prediction, or the closed
  form that matches to depth 12. Cost O(depth^2), trivial.
```
