# Shared context

What this run knows, in its own words; written by the context curator. It is
re-sent on nearly every model call, so each line must save an agent real work
and nothing here may be wrong. Token budget `MATH_AGENT_CONTEXT_TOKENS`
(10000). Detail is compressed into the anchored files; link before expanding.

**Problem:** Erdős–Straus `4/n = 1/x + 1/y + 1/z`, open since 1948; deliverable
is a partial result stated exactly, never a claim of the whole. The instrument
is the two-term reduction `4/n − 1/x = d/(nx)`, `d = 4x−n`, split via
divisors of `(nx)²`. Claims ledger is `research/CLAIMS.md` (now populated, one
row per claim); failed directions live in the ledgers, and in
`code/out/verify_elementary_reductions.md` and `code/minimal_x/*.py` for this
cycle's computed claims.

## Established

Each marked **checked** (this run computed it), **sourced** (primary text on
disk), or asserted-by-source.

- **Oracle ground truth** (checked): `solves(n,x,y,z)` = exact integer
  cross-multiplication; `is_identity` = sympy simplifies
  `4/n(k)−1/x−1/y−1/z` to 0 in k; `naive_solve` is a bounded brute force, only
  for small n, cap artifacts are not gaps. Reproduced all 12 witnesses, solved
  every n ∈ [2,200], even case m=1..49. (`code/oracle.py`, `code/brute.py`.)
- **Classical cover** (checked): the five Mordell conditions (n≡2 mod 3,
  3 mod 4, 2|3 mod 5, 3|5|6 mod 7, 5 mod 8) leave exactly
  `{1,121,169,289,361,529}` mod 840 open; all six are squares mod 840
  (1,11²,13²,17²,19²,23²), each ≡1 mod 24; smallest prime in an open class is
  1009. (`code/out/esc_residues.py`, `verify_library_claims.py` Claim 2.)
- **All eight classical covering identities now explicit and identity-checked**
  (checked; last block of `code/out/commands.log`): (n,x,y,z) forms — 2 mod 3:
  (n, (n+1)/3, n(n+1)/3); 3 mod 4: ((n+1)/4, n(n+1)/2, n(n+1)/2); 5 mod 8
  (n=8k+5): ((n+3)/4, n(n+3)/8, n(n+3)/4); 2 mod 5 (n=20k+17):
  ((n+3)/4, n(n+3)/10, n(n+3)/2); 3 mod 5 (n=20k+18):
  ((n+2)/4, 3n(n+2)/20, 3n(n+2)/4); 6 mod 7 (n=28k+27):
  ((n+1)/4, 2n(n+1)/7, 2n(n+1)); 5 mod 7 (n=28k+26): ((n+2)/4, n(n+2)/7,
  n(n+2)); 3 mod 7 (n=28k+24): ((n+4)/4, n(n+4)/14, n(n+4)/2). All pass
  `is_identity` (diff ≡ 0 in k); denominators integral exactly by the stated
  n+c ≡ 0 mod modulus. Upgrades "the other 834 classes fall by polynomial
  identities" from sourced to identity-checked here; the mod-5/mod-7 forms
  (previously unattested in sources) are now on disk — do not re-derive.
- **Even case trivial; n≡3 mod 4 corrected** (checked): `4/(2m)=1/m+1/(2m)+1/(2m)`;
  for n=4k+3, `x=(n+1)/4, y=n(n+1)/4+1, z=y(y−1)` is an identity, integral and
  positive for k=0..4999. The brief's `x=n, y=(n+1)/2, z=n(n+1)/2` is FALSE
  (solves 3/n; residual exactly 1/n). (`code/out/verify_elementary_reductions.md`.)
- **Prime reduction** (sourced): f(nm) ≥ f(n), so it suffices to prove for
  prime n — a minimal counterexample is prime ≡1 mod 840.
- **THE square obstruction, now stated precisely** (sourced, primary —
  Schinzel, Funct. Approx. 28 (2000) Thm 1, `research/summaries/schinzel-three-unit-fractions.md`):
  for (a,b)=1 and **b a quadratic residue mod a**, no polynomials
  F₁,F₂,F₃ ∈ ℤ[k] with positive leading coefficients satisfy
  `4/(ak+b) = 1/F₁+1/F₂+1/F₃`. With a=840 and b∈{1,121,169,289,361,529}, every
  b is a square mod 840, so **no single polynomial identity covers any open
  class**. Any new family must leave the ℤ[k]-polynomial shape: rational
  functions, non-integral-per-k shapes, or a finite sub-covering by
  residue-class families (which is what the minimal-x sweep below actually
  exhibits). This answers the run's earlier `exact-statement-from-b7df`
  request. (Salez 2014's "seven constant-coefficient modular equations are
  complete for degree-1" is the same boundary; sourced.)
- **Type I/II** (sourced): for odd prime p every solution is Type I (p divides
  exactly one of x,y,z) or Type II (exactly two), f(p) = 3f_I + 3f_II;
  Elsholtz–Tao Prop 1.6 (f_I=f_II=0 at odd perfect squares) is sourced with its
  proof located (quadratic reciprocity, `research/sources/pomerance-erdos-straus.full.md`
  lines 665–685; claim `elt-prop16-vanishing-odd-squares`).
- **Elsholtz–Tao Prop 1.9 / Salez seven equations** (sourced): the complete
  list of polynomial-solvable primitive classes is four Type-I forms
  (n ≡ −f mod 4ad with f|4a²d+1; n ≡ −f mod 4ac + n ≡ −c/a mod f;
  n ≡ −f mod 4cd + n² ≡ −4c²d mod f; n ≡ −1/e mod 4ab with e|a+b) and three
  Type-II forms (n ≡ −e mod 4ab; −4a²d mod f with 4ad|f+1; −4a²d−e mod 4ade).
  The explicit (a,...,f) sextuple constructions for each are in
  `elsholtz-tao-counting.full.md` lines 2390–2470 — the raw material for any
  parametrised Type-I/II family search; verify_identity-checked against
  witnesses before reuse. Salez's seven equations are the degree-1 linear case
  of the same list.
- **Minimal-excess divisor criterion** (checked, exact, 2705/2705 — this
  cycle's main computed result): for n=4m+1 (all six classes), candidate
  `x_e = (n+4e+3)/4` with `d_e = 4e+3`; a split `d_e/(n x_e) = 1/y+1/z`
  exists **iff −n·x_e (mod d_e) is the residue of a divisor of (n·x_e)²**.
  Holds at the minimal e of every row and fails at every e′<e;
  brute-force agreement everywhere. (`code/minimal_x/divisor_criterion_validate.py`,
  `code/out/divisor_criterion_validate.captured.txt`, data
  `code/out/extended_minimal_x.json`.)
- **Subfamily criteria** (checked, 2705/2705 — classical prime-divisor
  subfamilies, now verified over the six open classes):
  - e=0 (x=(n+3)/4 works) ⟺ some prime q≡2 (mod 3) divides n·(n+3)/4.
  - e≤1 (x=(n+7)/4 works) ⟺ some prime q≡3,5,6 (mod 7) divides n·(n+7)/4.
  For prime n≡1 mod 3 the q≡2 mod 3 factor can only sit in (n+3)/4: e.g.
  n=1009 (253=11·23, 11≡2 mod 3) has e=0; n=1201 ((n+3)/4=301=7·43, no
  such factor) has e=5. About 60% (1612/2705) of rows have e=0, ~80% e≤1.
  (`code/minimal_x/subgroup_validate.py`; these are also per-n identities of
  the Mordell type, not new covering families by themselves.)
- **Extended open-class sweep** (checked): all n=840k+r ≤ 378529 (k≤450, six
  classes, 2705 values) have a minimal solution with excess ≤14; x values are
  (n+4e+3)/4 so 4x−n ∈ {3,7,11,15,19,23,27,31,39,59}. (`code/out/extended_minimal_x.json`,
  `code/out/extended_verify.captured.txt`.)
- **Verification bounds** (sourced): 10¹⁴ Swett 1999; 10¹⁷ Salez 2014; 10¹⁸
  Mihnea–Dumitru 2025 (arXiv:2509.00128, S₂₉ filter). None reproduced here.
- **Bradford two-variable reduction** (sourced): for prime p the conjecture is
  equivalent to the existence of x∈[⌈p/4⌉,⌈p/2⌉] and d|x² with
  d≡−px (mod 4x−p) [Type I] or d≡−x (mod 4x−p) [Type II]. The natural ansatz
  frame (search pairs (x(k),d(k)) instead of triples).
- **Sourced context** (asserted-by-source, ledgers hold the details): Xu —
  tame solutions n₂,n₃ | (6m+k)(24m+1), only 9 wild primes among 7185 primes
  24m+1, m≤30000; Bradford 2026 — claimed elementary proof whose final
  covering step is **not proved** (do not cite as a proof); Mballa — symmetric
  y=z solutions for all n≡0,2,3 mod 4 and almost all n≡1 mod 4; Bello et al —
  divisor parametrisation; Swett — the six-class lemma (n mod 840 outside the
  set ⇒ solved) dated to 1999. (`research/summaries/*.md`.)

## Ruled out

- **Brief's n≡3 (mod 4) identity is 3/n, not 4/n** (checked). All oracle.py
  rows encoding it FAIL — script bug, not equation; their "unsolved" lists
  (127,149,157,…) are z-cap artifacts (n=127 needs z=134112). Do not re-raise.
- **verify_library_claims.py Claim 3 Type-I/II check is meaningless**: its
  "type" counts denominators divisible by n at tiny n with x≤4n, so every
  triple looks typed. Never cite its "I/II at odd squares" output.
- **Subgroup characterization of minimal excess is NOT exact** (checked,
  refuted): membership of −n·x_e in the subgroup generated by primes of n·x_e
  mod d_e predicts a split at e′<e in 56 cases (all blocked by the u≤n·x
  pairing), within k≤450. The exact version is the divisor-residue criterion
  above (prime-power refinement matters). Clustered at r=361 (18) and r=1
  (12). (`code/minimal_x/exceptions_analyze.py`.)
- **Naive d=7 criterion "prime ∈ {3,5,6}"** (dividing n or (n+7)/4) is
  refuted — mismatches at n=1681,6721,8401; the corrected form is
  q≡3,5,6 **(mod 7)**, checked 2705/2705. Ditto naive prime-in-{2}-mod-3 → the
  q≡2 (mod 3) statement.
- **Bradford 2026 is not a proof** (sourced): v1 ends stating the covering
  step remains; treat its Lemma 1/2 families as candidates for is_identity
  checking, nothing more.
- **No period ≤59 in e(k)** over k≤450 in any of the six classes (checked):
  naive "minimal excess repeats in a way a small-modulus shape could ride"
  is out; excess is driven by the divisor/prime-divisor structure instead.
- Schinzel Thm 2 (no polynomial identities when m>3b>0) is strictly weaker
  than Thm 1 for our shape; do not cite it separately.

## Numbers

- 12 witnesses in `code/out/witnesses.json`, all verified (e.g. n=121:
  4/121 = 1/31 + 1/1254 + 1/427614). All 12 satisfy x=(n+t)/4 with
  t∈{3,15,19,23,31,47} (observed, not proved).
- Extended sweep: 2705 rows; excess distribution over all rows
  {0:1612, 1:563, 2:351, 3:63, 4:58, 5:39, 6:4, 7:13, 9:1, 14:1}; per-class
  maxima: r=1 e=7 (k=119), r=121 e=9 (k=293), r=169 e=7 (k∈{25,80,261}),
  r=289 e=7 (k=194), r=361 e=14 (k=141, n=118801 **prime**), r=529 e=7
  (k∈{209,288}). The extremes are the natural targets for a new-shape ansatz.
- **Falsification oracle is closed**: prime witnesses now exist in all six
  classes (r=1: n=2521; r=121: n=1801; r=169: n=1009; r=289: n=1129;
  r=361: n=1201; r=529: n=3049). Any impossibility claim contradicted by
  these is false as stated.
- AP subfamilies: many full residue classes k≡a (mod M≤60) sit inside
  {k : e(k)=0} per class (whole list in `code/out/extended_verify.captured.txt`).
  These fire through n acquiring a prime ≡2 (mod 3) divisor; for prime n that
  factor must lie in (n+3)/4, so the prime-relevant part is a genuine
  subfamily of the open class. This is the concrete seed for a finite
  sub-covering attack.
- d=3 and d=7 criteria: 2705/2705 both; minimality exact 2705/2705;
  divisor criterion holds at minimal e and fails at all e′<e, 2705/2705.

## Recalled

Durable memory (prior-run, recall_memory) holds: the pointer card for
erdosproblems.com #242; the obstruction summary (six classes = primitive
square residues mod 840; Mordell no-identity-for-QR; Salez seven-equations
complete for degree-1; type I/II definition; verification bounds); the oracle
corrections (wrong 3/n identity; cap artifacts); the witness x=(n+t)/4
observation. All are recalled, not re-derived; the checked rows above
supersede nothing except where stated. `research/CLAIMS.md` carries the full
claim ledger with `holds-here` and evidence class per row — read it before
re-deriving any of the sourced statements above.

Two 2026 works converged (recalled, durable): Mballa (arXiv:2602.20036) —
symmetric y=z families for n ≡ 1 (mod 4) via a divisor b ≡ 3 (mod 4) of n;
proved for density-one set; **for n=840k+1 the b≡3 mod 4 structure becomes
b·840k+1 = multiple-of-b, i.e. k ≡ −b⁻¹ mod /b·gcd(840,b)**, so e.g. b=11
gives k ≡ 5 mod 11 sub-progression covered ([full construction in
`research/sources/mballa-unified-parametric.full.md`] §5.1, example n=6721).
Ventas (arXiv:2605.04551) — same b≡3 mod 4 divisor mechanism, heuristic.
These give concrete sub-progressions of the open classes already covered;

## Contradictions

- Brief's n≡3 (mod 4) identity vs computation (settled: brief wrong).
- Elsholtz–Tao Prop 1.6 asserted "no Type I/II at odd squares" vs
  verify_library_claims.py Claim 3's noise (detector broken; Prop 1.6 exact
  statement still unread — treat as asserted-by-source). Schinzel Thm 1 is
  the sharp, checkable statement of the same obstruction.
- Naive d=7 criterion vs corrected (mod-7) criterion (settled by 2705 rows).
- Subgroup-only characterization vs exact divisor-residue criterion (settled:
  56 counterexamples).

## Gaps

- **Exact statement of Elsholtz–Tao Prop 1.6** from the full text is now
  resolved (proof located; see Established). What remains unread is nothing
  that changes the picture.
- **The AP→subfamily lift** is now proven in principle by Mballa's
  construction (every b≡3 mod 4 gives a k sub-progression); the gap is
  whether a finite union of such — or of e=0/E-T family sub-progressions —
  covers all of some open class, and the density of the union. The 56
  exception rows and the e∈{7,9,14} rows (r=1: k=22,119,234,288,355,387;
  r=361: k=1,34,112,141) are where a non-prime-divisor shape must appear.
- **Verification-bound reproduction**: any slice of the 10¹⁸ bound (or
  Salez's seven-equation sieve on a subset) on Salez's residual set R₂ ∪ R₇
  (moduli 840 → 892,371,480 → 25,878,772,920 with S₂₉) remains unreproduced.
- **An impossibility for a specific new shape** (named degree/shape in k),
  per the run's brief: the natural candidate is showing no rational-function
  family with x,y,z of fixed degree covers n ≡ 1 mod 840 — the exact
  obstruction beyond Schinzel Thm 1 to be pinned down with the Schinzel
  proof's techniques.