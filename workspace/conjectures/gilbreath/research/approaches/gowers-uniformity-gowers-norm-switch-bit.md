```approach
idea: Attack the supply bottleneck ν₂/n through higher-order Fourier analysis (Gowers uniformity) of the ±1 switch bit u_j = (−1)^{h(j)} = (−1)^{[gap_{j+1} ≡ 2 (mod 4)]}. The supply density ν₂/n is the density of 1s of the involutive F₂ fold ζ(h); lower-bounding it is equivalent to controlling the mean of the multiplicative system f(d) = (−1)^{ζ(h)[d]} = Π_{j⊆d} u_j over the Boolean lattice, and Green–Tao / Gowers–Wolf supply exactly the machine that separates "system average → 1/2 (uniform)" from "biased (structured)".

mechanism: ζ (subset-zeta = Möbius over F₂) is an involution, so ζ(h) sparse ⟺ h = ζ(sparse) is 2-adically structured; the collapse class (period 2^k) and Thue–Morse sit in that structured direction, while odd-period words and the primes sit in the uniform direction (dyadic-oddfactor-infimum-bounded, dyadic-separating-invariant-three-strings). The Gowers U² norm (additive 4-cycle energy Σ_γ |û(γ)|⁴) and the higher U^k norms, evaluated along 2-adic subcubes, are the natural detectors of exactly this structure; the inverse conjecture for the Gowers norms (Green–Tao, Bergelson–Tao–Ziegler) plus the Gowers–Wolf theory of system averages gives a quantitative "small Gowers norm ⟹ multiplicative system average → 1/2" statement. That statement, if it holds, is a proved general-class theorem: anti-2-adic switch bits (in the sense of small 2-adic-subcube Gowers norms) have ν₂/n bounded below — with the primes' switch bit as the instance. This is a genuine third setting for the supply side, not a restatement of the refuted uncertainty-principle or odometer routes: those wanted dyadic spectral mass in the kernel of a surjective fold (kernel = span(all-ones), no dyadic subspace), whereas this works on the full ±1 system in the Walsh basis, where Parseval is non-degenerate.

status: refuted
killed-by: Two independent grounds, both decisive, the first fatal to the
  object the proposal is actually about.
  (1) WRONG OBJECT FOR THE SUPPLY DENSITY. The proposal's load-bearing
  identification is "ν₂/n is the density of 1s of the involutive F₂ fold
  ζ(h), i.e. ν₂(q_n) = #{d ≤ n : ζ(h)[d] = 1}". This is exactly the
  identification the run ALREADY refuted in `boolean-influence-parity-subset-density`
  (refuted) and `thue-morse-sublinear-supply-witness` (corrected): the fold
  bit ζ(h)[d] is a mod-4 PARITY statistic (it fires on halved values that are
  odd, i.e. actual values ≡ 2 mod 4: 2,6,10,…), not a {0,2}-membership
  counter. ν₂ counts cells exactly 2 within the maximal {0,2} suffix. The
  ground truth refutes the equality: Thue–Morse h gives TM ν₂(100) = 27 but
  the fold count is 7, first mismatch at n = 1 (claims
  `thue-morse-sublinear-supply-witness`, `dyadic-separating-invariant-three-strings`).
  So a Gowers-uniformity statement about u = (−1)^{ζ(h)} = Π_{j⊆d} u_j, i.e.
  about the SAME fold parity, certifies the mean of a product that is NOT ν₂/n.
  It tells you whether the fold PARITY density → 1/2, not whether ν₂/n ≥ c.
  (2) THE NAMED THEOREMS DO NOT SUPPLY THE TRANSFER. Green–Tao–Ziegler's
  inverse theorem GI(s) (arXiv:1009.3998; U⁴=Glasgow 2010) says: f:[N]→ℂ,
  |f|≤1, ‖f‖_{U^{s+1}} ≥ δ ⟹ f correlates with a bounded-complexity s-step
  nilsequence F(g(n)Γ). That is an inverse statement about LARGE norms
  (structure detection), not a "small norm ⟹ system average → 1/2" forward
  theorem. The forward small-norm ⟹ equidistribution step is exactly the
  content of Green–Tao/Bergelson–Tao–Ziegler / Host–Kra for ADDITIVE
  patterns; obtaining it on the 2-adic SUBMASK product (a boolean-lattice
  average, not an AP average) is precisely the open load-bearing step the file
  flags, and the literature does not supply it in the required form. The
  candidate therefore has no named theorem whose hypotheses hold here bridging
  the fold-parity mean to ν₂/n ≥ c. The separating claim it wants (collapse
  words have large norm, primes small) is not even measured anywhere, and
  (1) shows the object it would separate (fold parity) is the wrong quantity
  for G-supply anyway.
  (3) INDEPENDENT: the fashion the proposal draws on — higher-order Fourier
  analysis of (Möbius/von Mangoldt) multiplicative functions (Frantzikinakis–
  Host 2016, JAMS; Tao–Teräväinen 2023, JEMS) — is about the smooth /
  structured large-scale behaviour of multiplicative number-theoretic
  functions, not about the combinatorial switch bit of prime gaps mod 4, and
  it gives no lower bound on the {0,2}-suffix count. No source applies Gowers
  norms to the Gilbreath / iterated-absolute-difference problem (none found).
  The honest, still-open conditional route G-supply sits on remains
  `abgs-2011-s9-mod4-switch-limit-open` (two-point mod-4 correlation), NOT a
  uniformity-norm statement about the fold.
precedent: >
  Sourced: Green–Tao–Ziegler, "An inverse theorem for the Gowers U^{s+1}[N]-
  norm", arXiv:1009.3998; Green–Tao–Ziegler "An inverse theorem for the U⁴-
  norm" (Glasgow Math. J., 2010); Green–Tao "An inverse theorem for the U³(G)
  norm" (Proc. Edinb. Math. Soc., 2008); Tao–Ziegler correspondence-principle
  inverse theorem over F₂ⁿ; Loved/quantitative U⁵/U⁶ over F₂ⁿ (Canad. J. Math.);
  Host–Kra "A point of view on Gowers uniformity norms" (HAL 01252534);
  Frantzikinakis–Host "Higher order Fourier analysis of multiplicative
  functions" (JAMS, doi:10.1090/jams/857); Tao–Teräväinen "Quantitative bounds
  for Gowers uniformity of the Möbius and von Mangoldt functions" (JEMS,
  doi:10.4171/jems/1404).
  Internal claims: thue-morse-sublinear-supply-witness (fold-parity ≠ real ν₂,
  first mismatch n=1), dyadic-separating-invariant-three-strings,
  dyadic-collapse-proved, dyadic-oddfactor-infimum-bounded,
  subset-zeta-preserves-automaticity-christol, subset-zeta-rational-substitution-verified.
  Sibling refuted approach: boolean-influence-parity-subset-density (the
  identical fold-parity-vs-ν₂ conflation, refuted and killed by it).
  No source was found applying Gowers uniformity / higher-order Fourier
  analysis of the switch bit to the Gilbreath problem.
buy: The one durable, sourced fact this surfaces is worth keeping: the inverse
  theorem GI(s) is the precise statement for "large U^{s+1}-norm ⟹ correlates
  with a bounded-step nilsequence", and its hypotheses (|f|≤1, integer
  interval [N]) are trivially met by u. But the G-supply question is about a
  boolean-lattice average of a fold whose parity is the WRONG quantity, and no
  forward-equidistribution theorem over 2-adic subcubes is available to close
  it. The route buys a vocabulary for identifying 2-adic structure, not a
  lower bound on ν₂/n. Retire it; the supply-side separating invariant stays
  open (`dyadic-linear-complexity-supply`, measured 2-adic spectral mass), not
  a Gowers norm.
first-step: Compute U² (additive energy) and the 2-adic-subcube Gowers norms of u for the four families — period 2^k, period 3, Thue–Morse, and the real prime switch bit to n ≤ 2·10^5 — and check the separating prediction: collapse/rigid words (period 2^k, Thue–Morse) have large norm, odd-period and primes have small norm. This is an O(n²) (or FFT) correlation computation, not a search; a single inversion of the prediction refutes the separating claim.
```

## Established vs speculation

- **Established (this run):** ζ is an F₂ involution (`subset-zeta-preserves-automaticity-christol`, `subset-zeta-rational-substitution-verified`); collapse ⟺ 2-adically structured (`dyadic-collapse-proved`); the supply density ν₂/n is the density of 1s of the fold (`dyadic-linear-complexity-supply`, `g-supply-transfer-measured`); odd-period words are linear, Thue–Morse is sublinear, primes sit on the linear side (`dyadic-separating-invariant-three-strings`).
- **Speculation (to be checked by research):** the load-bearing transfer — that a quantitative bound on the 2-adic-subcube Gowers norms of u forces the system average E_d Π_{j⊆d} u_j → 0 (hence ν₂/n → 1/2) — is not yet established here and may not exist in exactly that form. The right named statement is likely Gowers–Wolf (system averages) or the inverse theorem for the U^k norms on F₂ⁿ.

## Scholze gate (must reproduce a held claim)

The reformulation must reproduce the two poles already in the ledger as one phenomenon: `dyadic-collapse-proved` (period 2^k ⟹ ν₂ = O(1)) should read as "2-adically structured ⟹ the multiplicative system is degenerate/biassed", and `dyadic-oddfactor-infimum-bounded` (odd period ⟹ ν₂ ≥ c·n) should read as "non-2-adic ⟹ the system is uniform". If the Gowers-norm vocabulary cannot at least split these two known classes, it is not yet worth adopting.

## Falsifier

Smallest input that breaks the separating claim: if any odd-period word (say period 3) has LARGER 2-adic-subcube Gowers norm than a collapse word (say period 2), the "structured ⟺ collapse" dictionary fails as a separator, and the transfer is refuted before any theorem is attempted.
