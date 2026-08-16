# Move the index shift into a weight: level sets of π via Perron / the explicit formula

```approach
idea: >
  Convert the index-domain correlation
  S(n) = Σ_{d=2}^{n−1} (−1)^{T(n,d)} = Σ_{d=2}^{n−1} Π_{R ∈ runs(↓d)} χ(q_{a_R}) χ(q_{b_R})
  into a VALUE-domain double character sum by extracting the "π-level set"
  π(p') − π(p) = 2^{ν₂(d+1)} − 1 via Perron's formula / the explicit formula.
  The index shift — the one thing that killed every value-domain route (it sits
  inside the character argument χ(q_{j+2^g}) with no integer shift) — is moved
  OUT of the argument into a weight z^{π(p')−π(p)}. Summing over d then becomes
  a coefficient extraction in z, and what remains is a genuine value-domain
  bilinear form in χ over free prime arguments p, p', where Linnik dispersion
  and the large sieve actually have an integer structure to feed on.

mechanism: >
  The run telescope puts every pair in the scale-g stratum at index separation
  2^g (g = ν₂(d+1)), so the stratum is Σ_j χ(q_j) χ(q_{j+2^g}). Over prime
  PAIRS this is

      Σ_j χ(q_j) χ(q_{j+2^g})  =  Σ_{p < p' ≤ x} χ(p) χ(p') · 1_{π(p') − π(p) = 2^g − 1}.

  The indicator of a fixed prime-count distance is a level set of π, and it can
  be extracted as a coefficient: for the generating function

      Σ_{k ≥ 1} 1_{π(p') − π(p) = k} z^k  =  z^{π(p') − π(p)},

  the g-stratum is [z^{2^g − 1}] of F(z; x) := Σ_{p < p' ≤ x} χ(p) χ(p') z^{π(p') − π(p)}.
  The named engine is the explicit formula (Riemann–von Mangoldt: π(x) =
  Li(x) + Σ_ρ Li(x^ρ) + negligible), which turns z^{π(p')−π(p)} into a
  controlled oscillatory weight whose structure is understood unconditionally
  (prime number theorem) and conditionally (Riemann hypothesis). Hence F(z; x)
  is a SMOOTHED value-domain bilinear form: the exotic index relation has been
  absorbed into the weight, the character arguments are free, and the toolbox
  that previously did not apply — Linnik's dispersion method, the
  Bombieri–Vinogradov / large-sieve estimates for χ at shifted integer
  arguments — now applies to p and p' rather than to q_j and q_{j+2^g}. S(n)
  is recovered as a finite sum of coefficients, one per dyadic scale
  g ≤ log₂ n. This is deliberately NOT a reopening of
  `dispersion-bilinear-large-sieve` (refuted): there the shift sat inside the
  character argument with no value shift; here the shift is moved into a weight
  and the characters sit at free prime arguments.

status: refuted

first-step: >
  (symbolic_math + tool_builder, exact arithmetic, real prime residues)
  (1) VERIFY the coefficient identity: for the real primes up to x = 40000,
      compute A_g(k) := Σ_{p<p'≤x} χ(p) χ(p') 1_{π(p')−π(p)=k} for k = 1,2,4,8
      and assert A_g(2^g − 1) equals Σ_j χ(q_j) χ(q_{j+2^g}) in the matching
      window. (2) BUILD F(z; x) = Σ_{p<p'≤x} χ(p) χ(p') z^{π(p')−π(p)} for
      |z| = 1 − ε and confirm the [z^{2^g−1}] coefficient reproduces A_g.
      (3) PRICE the dispersion step: print whether F(z; x) factorizes as
      Σ_m α_m Σ_n χ(n) β_m(n) with β_m multiplicatively smooth, and whether the
      z^{π} weight is tame enough for Linnik's method. FALSIFIER: if F(z; x)
      does not admit a value-domain factorization (the π-level-set weight is
      not smooth enough to pass through dispersion), the route dies with the
      reason recorded — the index→value conversion is the single load-bearing
      step and everything else is standard machinery.

killed-by: >
  The load-bearing step — "the index shift is moved into a weight z^{π(p')−π(p)},
  leaving χ evaluated at free prime arguments p, p'" — is false as stated, and
  the machinery it was to unlock therefore cannot engage. Substituting j = π(p)
  (the prime's INDEX) turns the generating function into

      F(z;x) = Σ_{p<p'≤x} χ(p)χ(p') z^{π(p')−π(p)}
             = Σ_{j<j'} χ(q_j) χ(q_{j'}) z^{j' − j}.

  This is a function ONLY of the index-domain sequence (χ(q_j))_j: the weight
  z^{π(p')−π(p)} is literally z^{(index difference)}, and the character χ(p) is
  χ(q_{π(p)}), i.e. evaluated at the index. There are no "free prime value
  arguments" anywhere — the conversion is an identity that never leaves the
  prime index, and this is exactly the coordinate the refuted
  `dispersion-bilinear-large-sieve` route showed the value-domain toolbox
  cannot touch. Linnik's dispersion needs the argument of χ to shift by an
  INTEGER IN THE VALUE (n−l); here every shift is j'−j, an index difference,
  so there is no integer value-shift for dispersion or the large sieve to feed
  on. Feeding z^{π(p')−π(p)} into the explicit formula makes the weight
  z^{Li + Σ_ρ Li(x^ρ) + ...} — more oscillatory, not smoother, and still a
  function of the index π. Second: the proposal carries an off-by-one — the
  pair (p,p')=(q_j, q_{j+2^g}) has π(p')−π(p)=2^g, so the correct level-set
  index is 2^g, not 2^g−1 (at g=0 the route's [z^{2^g−1}]=[z^0] coefficient
  is empty while the adjacent/separation-1 stratum is the [z^1] one). And
  third: the g=0 (adjacent-index, separation 1) coefficients of F, which under
  any reading the coefficient extraction must recover, are precisely the mod-4
  switch-pair object that the parity barrier (abgs-p1-wide-open,
  lau-nonconstant-pattern-open) says is L-function-inaccessible — so the route
  re-encounters the barrier at its own coarsest scale rather than escaping it.
  The proposal's own falsifier (does F admit a value-domain factorization?) is
  answered in the negative structurally: the weight is a level-set indicator of
  π, i.e. a function of the index, so no smooth β_m(n) factorisation with free
  value argument exists.

precedent: >
  The engines named are real and standard, with exact statements:
  - Perron / explicit formula for π(x) = Li(x) + Σ_ρ Li(x^ρ) + (negligible):
    Riemann–von Mangoldt; see e.g. Montgomery–Vaughan "Multiplicative Number
    Theory I" (Springer), Ch. 12, and Leboeuf, "Prime Correlations and
    Fluctuations", Lett. Math. Phys. 66 (2003), DOI 10.1007/s00023-003-0958-2
    (explicit trace formulas for π with the zeta-zero expansion).
  - Value-shifted character sums (what dispersion/large sieve actually bound):
    "Sums of Values of Nonprincipal Characters over a Sequence of Shifted
    Primes", Proc. Steklov Inst. Math. (2018), DOI 10.1134/S0081543817080156
    (Σ_{n≤x} Λ(n) χ(n−l) ≪ x exp(−0.6√ln D) — a VALUE shift n−l, exactly the
    hypothesis that fails here); "Shifted character sums with multiplicative
    coefficients II", J. Number Theory (2018), sciencedirect
    S0022314X17301178 (Σ f(n)χ(n+a) — value shifts a of the argument).
  - Inside-workspace: the parity barrier claims abgs-p1-wide-open (ABGS §9:
    consecutive-pair asymptotics "cannot be treated using L-functions") and
    lau-nonconstant-pattern-open (even one non-constant 2-term residue pattern
    open), both in research/summaries/. The precedent route
    `dispersion-bilinear-large-sieve` was refuted for the same index-vs-value
    reason and is cited in research/APPROACHES.md.
  Verification caveat: no execution tool was registered on the research pass, so
  the regrouping identity F(z;x) = Σ_{j<j'} χ(q_j)χ(q_{j'})z^{j'−j} is held by
  the hand-substitution j=π(p) (a dictionary identity, not machine-checked);
  `code/out/check_levelset_identity.py` is written to assert it and the
  off-by-one at n≤200 but NOT yet executed.
```

## Speculation, marked

The identity A_g(2^g−1) = Σ_j χ(q_j)χ(q_{j+2^g}) is exact (it is the same sum
regrouped — up to the off-by-one, which should be 2^g). That F(z;x) is then
tractable by dispersion / the large sieve is pure speculation: the weight
z^{π(p')−π(p)} is a *function of the prime-counting function between two
primes*, not a smooth multiplicative coefficient, and no source is known to
treat a bilinear form whose weight is a level-set indicator of π. The first
step is designed to kill that cheaply. The value of the proposal if it
survives: it converts the one genuinely untooled object (index-domain
correlation) into the one domain where a century of machinery exists.

## Distinctness check

- Not `dispersion-bilinear-large-sieve` (refuted: value-shift of χ at n−l).
  Here the shift is absorbed into the weight; χ is evaluated at free arguments.
  — This distinctness fails: the substitution j=π(p) shows χ is NOT evaluated
  at free value arguments; the two routes are the same index-domain object seen
  from two sides, and both die on the same index-vs-value obstruction.
- Not `prime-race-variance-large-sieve` / `matomaki-radziwill` (refuted: value-
  domain Höeffding/BDH do not reach index-domain correlations). Here the
  index-domain object is first *transformed* into a value-domain object.
  — The transformation is an identity; no value-domain object is produced.
- Not `dyadic-gap-character-correlation` (refuted: premise falsified by
  stratification). That route bounded the same S(n) directly in index
  coordinates; this one changes the coordinates first.
  — As above, the coordinate change is vacuous.
