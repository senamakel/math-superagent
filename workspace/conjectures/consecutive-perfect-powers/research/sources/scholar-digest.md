# Scholar digest — what the reference library establishes for this investigation

This note is the scholar's consolidated reading of `research/sources/`. Each
source was judged against what this run is doing: re-deriving (in-workspace)
the partial results that lead toward or reconstruct the solution of
`x^p - y^q = 1`. The workspace is a **calibration** sandbox: the published
proof (Mihailescu 2002) and Cassels 1960 are screened at the network boundary,
so every claim below that touches the challenge equation itself is either the
run's own computation (marked `checked`) or `asserted` on the held technique
tier — never supplied as a finished statement.

## Structure of a minimal counterexample

Any solution of `x^p - y^q = 1` (x,y>0, p,q>1) descends to one with prime
exponents via `(x^a)^P`: composite `p = aP` maps `(x,p)` to `(x^a, P)`
(claim `prime-reduction-identity`, `checked` on 40 cases). So the minimal
counterexample has p,q prime. The prime pairs split exhaustively:

- **p = 2**: `x^2 - y^q = 1` has only `(x,y,q)=(3,2,3)` (claims
  `exp2-cases-numerically`, `exp2-independent-searches`, verified to 10^7/10^8;
  the *proof* in Z is `G-full-case-p2`, still open for formalisation).
- **q = 2**: `x^p - y^2 = 1` has no solution (p odd) — verified numerically to
  10^8; proof in Z[i] is `G-full-case-q2`, still open.
- **p,q both odd primes**: the open content, forced into `Z[zeta_p]`. The
  Cassels chain is `p | y, q | x` → double-Wieferich → class-group descent.

**Current verification bound:** oracle `solutions(N)` returns exactly
`{(3,2,2,3)}` for every N in {9,…,10^8} (`oracle-single-solution`, `checked`).
No double-Wieferich pair among distinct odd primes p,q ≤ 200 (`checked`).

## What each source establishes, and where it bears

### Cassels 1953 / 1960 (sourced records — full proofs screened)
`cassels-1960-II.md`: for `x^p - y^q = 1`, p,q odd, any solution satisfies
`p | y` and `q | x`; the 1960 paper notes the Catalan equation "has never been
proved" **at the time of writing (1960)**. `cassels-1953.md`: technique origin —
"every prime divisor of one base below the bound divides the other."
Neither supplies a proof in this workspace; both are the *scope* record. The
run's `cassels-selfcontained.md` skeleton re-derives `p|y, q|x` from the
machinery.

### Ring / ramification machinery (Thaine 1988; Steidl–Tasche 1989; Keune; Milne; Nguyen)
- `Z[zeta_p]` is the ring of integers of `Q(zeta_p)`; `(p) = (1-zeta_p)^{p-1}`
  totally ramified, residue degree 1, ramification index p-1 — claims
  `zeta-p-ring-and-ramification`, `faktor-pairwise-coprime-off-ramified`
  (asserted; the polynomial identity `1-z^a=(1-z)(1+…+z^{a-1})` is the
  computational core and is exact).
- **The valuation identity — HYPOTHESIS CORRECTED this run** (claim
  `valuation-identity-xp-1`): the earlier library statement used `p ∤ x`, which
  is **FALSE** (p=3, x=2: `v_3(7)=0` but `1+v_3(1)=1`). The correct hypothesis
  is the LTE congruence `p | (x-1)` (mirror `q | (y+1)`):
  `v_p(x^p-1)=v_p(x-1)+1`. This is the load-bearing engine of the whole
  Cassels `p|y, q|x` chain; any lemma built on the `p∤x` form is false.

### Class-number / Stickelberger / cyclotomic-units tier
(`relative-class-number-analytic.md`, `stickelberger-cyclotomic-units.md`,
`ichimura-2006`, `sinnott-1978`, `washington`, `milne`)
- **Minus class number**: `h^-(Q(zeta_p)) = 2p·∏_{chi odd}(-1/2 B_{1,chi})`,
  `B_{1,chi}=(1/p)Σ chi(a)a`. Normalisation pinned correct at p=3,5 by exact
  hand computation (`minus-class-normalisation-checked`); the full ladder has
  been verified by an **exact** route — `code/hminus_full.py` over
  `lib/cyclo.py` with sympy.Rational, no floats — reproducing OEIS A000927
  exhaustively for all 24 odd primes p ≤ 97, consecutively (claim
  `minus-class-number-formula`, `status: checked` at
  `code/out/hminus_full100.captured.txt`; matches A000927 by prime index).
  **Provenance correction (this run, an adversarial board review was right):**
  the two float programs formerly cited as "two independent routes"
  (verify_claims.py, hminus_exact.py) both evaluate the same product and are
  NOT independent; the exact exhaustive run is the source of record. The
  catalogue also exposed Washington 1st-edition errata at p=59 and p=97.
  h^- is easy to compute for very large p; **h^+ is not known for any p ≥ 71**
  (`minus-class-computable-plus-not`) — a structural fact: a proof must not need
  the plus part. Schoof 2003 (full text, `schoof-real-cyclotomic-class-numbers.primary.md`)
  confirms the exact sequence 0→Cl+→Cl→Cl−→0 and that the computed proxy
  h~+|h+ bounds the true plus part (`schoof-plus-minus-exact-sequence`); Hida's
  Iwasawa notes (`hida-elementary-iwasawa-cyclotomic.primary.md`) give a second
  primary statement of the relative class number formula in the same shape, and
  confirm Stickelberger's annihilator plus the cyclicity of the minus part over
  the Iwasawa algebra (`relative-class-number-formula-second-source`,
  `iwasawa-minus-cyclic`).
- **Stickelberger**: `s = Z[G]θ ∩ Z[G]` annihilates Cl(Q(zeta_p));
  `[Z[G]^- : s^-] = h^-` (`stickelberger-annihilator`,
  `stickelberger-annihilates-plus-index-formula`, `iwasawa-index-of-stickelberger`).
- **Circular units**: `[E+ : C+] = h^+` up to a power of 2 (`circular-units-index-plus-part`)
  — the non-computable half of the obstruction is the index of cyclotomic
  units in all units.

### Effective finiteness (Tijdeman survey)
Baker's method gives an effective but astronomically large upper bound on any
solution. The specific bound for THIS equation was not retrieved (the source
describes the *technique*, not the constant). This is the reason computation
cannot finish the job — the bound is many orders beyond feasibility. Re-
deriving the exact size is optionally a gap but not a productive one.

## Relation to the known solution at every lemma
`(3,2,2,3)`: p=2 even. Every odd-prime lemma (`p|y,q|x`, double-Wieferich,
both-odd descent) is **excluded by hypothesis** at it — never refuted by it.
`p|y`=2|2 and `q|x`=3|3 happen to hold; double-Wieferich fails there
(`3^1≢1 mod 4`, `2^2≢1 mod 9`) exactly as it must. This is the calibration the
whole run is measured against.

## What the sources do NOT settle
The deep both-odd descent (G-odd-descent) — converting the ideal relation to an
element relation without assuming class numbers — is the only step with no
cheap move in any source; the technique tier (minus class number, Stickelberger
annihilator, circular-units index) is exactly what would carry it, and that is
what the run holds now.

```claim
id: scholar-digest-valuation-corrected
statement: The valuation/LTE identity v_p(x^p-1)=1+v_p(x-1) holds iff p | (x-1)
  (mirror v_q(y^q+1)=1+v_q(y+1) iff q | (y+1)); the form with hypothesis p ∤ x
  is false (p=3,x=2).
hypotheses: p,q odd primes; the congruence p|(x-1) / q|(y+1).
holds-here: yes — corrects the load-bearing engine of the Cassels chain.
status: checked (hand proof via Fermat & LTE; positions CLAIMS.md corrected row)
anchor: research/sources/zetap-ring-ramification.md; research/CLAIMS.md
bearing: no Cassels/divisibility lemma may be built on the p∤x form.
follows-from: fermat-little-theorem, lifting-the-exponent
answers: valuation-identity-hypothesis
```

## Remainder
- Seen what the run still lacks: the in-workspace execution of
  `hminus_check.py` for p=7..43, and the formalisation of the three open
  exponent-side lemmas (`G-full-case-p2`, `G-full-case-q2`,
  `prime-reduction-identity`). None of the held sources closes the deep descent.
- Sources that do not help further: `keune-number-fields.md` and
  `washington-*.md` are catalogues/metadata (ring structure already covered by
  Nguyen/Milne/Conrad); `conrad-cyclotomic-extensions.about.md` is background
  (Galois group, Φ_n irreducibility) adding nothing beyond the ring/ramification
  tier it feeds; `tijdeman-*.md` is technique-only and its constant is not
  needed to make the "cannot compute" argument. Read them once, not again.
- Contradiction with recalled memory: none beyond the already-recorded
  open-vs-settled framing (Mihailescu 2002) and the corrected valuation
  hypothesis, both of which are now documented above and in CONTEXT.md.

## This-run additions (scholar)

**Ring/ramification tier now primary-captured (Conrad).** The foundational facts
previously held only at summary/metadata level — `Z[ζ_n] = O_{Q(ζ_n)}`, the
ramification `(p) = (1-ζ_p)^{p-1}`, `P=(1-ζ_p)` principal — are now captured
with proofs from `conrad-factorization-cyclotomic.primary.md`
(claims `zeta-p-ring-of-integers-and-ramification`,
`ramification-of-p-cyclotomic`, both `asserted`), and the unit-rank basis
`O^×≅W×Z^r` with rank `(p-3)/2` from `conrad-unit-theorem.about.md`
(claim `dirichlet-unit-theorem-cyclotomic-rank`, added this run). These are the
prerequisite the whole cyclotomic ideal-factorisation approach rests on.

**Verification-discipline flag (do not promote un-run scripts).** Two exact
checks are written but NOT executed in this run (no program runner available to
the scholar): `code/scholar_verify_ramification.py` (re-derives
`(p)=∏_{k=1}^{p-1}(1-ζ^k)=(1-ζ)^{p-1}` for odd primes via Φ_p(1)=p and exact
sympy reduction mod Φ_p) and `code/out/maillet_verify.py` (re-produces
`det(M_q)=±q^{(q-3)/2} h_1(q)` against OEIS A000927). Until a computing role
runs them and its captured output is read, `zeta-p-ring-of-integers-and-ramification`
stays `asserted` and `maillet-determinant-equals-class-number` stays `sourced` —
neither is `checked`. A claim is `checked` only when its captured output has
been read.

**Independent oracle route identified (Maillet determinant).** The
Binomial/determinant identity `det(M_q) = ± q^{(q-3)/2} h_1(q)` from
arXiv:2402.13829 is a genuinely different route to `h^-(Q(ζ_p))` than the
Bernoulli-product formula — no shared arithmetic — so it can discharge rule 11
(independent verification) once it is actually run. It is a candidate for the
computing role's agenda, not yet an established claim.

**Cleanup:** `research/sources/columbia-cyclotomic-class-groups.primary.md` is a
duplicate pointer to the canonical `columbia-ant-cyclotomic-and-class-numbers.primary.md`;
delete on next cleanup.
