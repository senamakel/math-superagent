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
  (n+4e+3)/4 so 4x−n ∈ {3,7,11,15,19,23,27,31,39,59}. Since x ≥ (n+3)/4 in
  n ≡ 1 mod 4, any polynomial family whose x(k) = (n(k)+4E+3)/4 has FIXED
  excess E covers only n with e ≤ E — never a whole class, by the maximal
  rows — so a degree-1 family for an open class must be a sub-progression
  family (next bullet), not an in-class one. (`code/out/extended_minimal_x.json`,
  `code/out/extended_verify.captured.txt`.)
- **Sub-class identity families for r=1: a batch exists, but the capture is
  NOT yet trustworthy** (construction + poly-positivity only; attribution
  bug found). `code/search_subprogression.py` runs Salez's seven converse
  equations (Prop 3) over n = 840M·k + b with b ≡ 1 mod 840, gcd(b,M)=1,
  b a QNR mod 840M — the only b Schinzel-legal for a polynomial family (b is
  a QR mod 840, so M must supply a prime q ∤ 840 with b a QNR mod q).
  Capture `code/out/subprogression.captured.txt` prints poly-positive x,y,z
  for M ∈ {11,13,17,19,22,23,26,29,31} (visual extent; the run hit the 540s
  timeout BEFORE printing its summary — no count, no residue breakdown; the
  extended capture is empty). Hand-verified here (exact arithmetic): for
  p=9240k+4201, A=(p+1)/11 solves via (3p, 3Ap, 3A); A=(p+23)/88 solves via
  (22Ap, Ap, 22A); for p=9240k+5881, A=(3p+1)/11 solves via (3p, 3Ap, A).
  **Trap:** the script's `verify_and_emit` never runs `is_identity`, and the
  printed (a,b) header is unreliable — the (22Ap, Ap, 22A) triple valid for
  n ≡ 4201 mod 9240 reappears under b=5881, where it fails (1/z > 4/n at
  k=0). Do not cite any family from this capture by its header; re-run each
  through `is_identity` at its claimed (a,b) first. Shapes are instances of
  the seven known linear forms (Salez: no new degree-1 shape exists), so the
  open question is the covering assembly, not the shape.
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

- **Source integrity (operator directive 2)**: `research/sources/yamamoto-1965-paper.full.md`
  is only the J-STAGE landing page (title/author/nav, no mathematics); the real
  PDF has no text layer and is TOMBSTONED — Yamamoto 1965 is not a source this
  run has read, and its Type I/II attribution rests on Elsholtz–Tao's
  restatement alone. `mathworld-egyptian-fraction.full.md` is an encyclopedia
  entry: orientation-only, never a load-bearing anchor.

- **Coverage density triangulated** (checked, operator directive 5): three
  independent routes agree. restricted to `extended_subprogression.full.txt`
  (88 classes, moduli 11..37) the operator's CRT computation gives
  4552829/4816253 = 0.945305, the run's `exact_union_density.py` gives
  0.945305 by factoring over K mod 6 branches, and the run's
  `independent_density_check.py` gives 0.94530 by direct empirical count over
  K < 3·10⁶ (converging 0.92800 → 0.94180 → 0.94462 → 0.94514 → 0.94530).
  The apparent discrepancy between 0.9453 and 0.9611 is entirely input scope:
  the former reads one capture file, the latter all three. The density method
  is sound — stop re-verifying it. (`code/out/coverage_triangulated.md`.)
- **Modulus-11 saturation ANSWERED — structural (checked, directive 5)**:
  of the 8 M=11-missing t-residues [0,1,2,3,4,6,8,9], **six are impossible**:
  [0,1,2,6,9] make 840t+1 a QR mod 11 and t=8 makes it ≡0 mod 11
  (non-primitive) — no polynomial family at modulus 11 can cover them
  (Schinzel). Only {3,4} are Schinzel-legal-but-uncovered at pure M=11, and
  **both are already realized at composite moduli**: M=33 covers t≡3 mod 11,
  M=22 covers t≡4. So prime 11 is **fully saturated over its 5 legal residues
  {3,4,5,7,10}, gap 0** (`definitive_structure.py`, `schinzel_residue_gap.py`).
  The "8 missing residues" is an artifact of reading pure-M=11 families only:
  no new family is needed there, and 6 residues are unobtainable for ever.
  This ends the saturation question for modulus 11: it cannot be saturated as
  posed (6 QR-blocked), and the other 2 are already covered elsewhere.
  **Schinzel narrowing (directive 7):** of the 8 "missing" residues at M=11,
  only 2 are actually reachable — s∈{3,4}. The other six are Schinzel-forbidden:
  s∈{0,1,2,6,9} give b a QR mod 11 (no ℤ[k]-polynomial identity possible),
  and s=8 gives b divisible by 11 (not primitive). Same analysis at M=23:
  11 QNR-allowed residues, 9 realised, gap={3,8}. The saturation question at
  each modulus reduces to the QNR-allowed-but-unrealised residues only.
- **Subprogression families** (checked, operator directive 4): 1451 parametric
  identity families for n ≡ 1 (mod 840), each n = a·k + b with b ≡ 1 (mod 840)
  and a = 840m for m ∈ {11,13,17,19,22,23,26,29,31,33,34,37,38,39,41,43}.
  Every family is an exact polynomial identity in ℤ[k] (operator-verified).
  123 distinct residue classes (m, s) of t = (n−1)/840. Coverage:
  732719497/762354697 = 96.112676% of n ≡ 1 (mod 840), up from 94.72% at 554
  families. The other five open classes are untouched. The per-prime avoided
  fractions are 14/23, 23/29, 24/31, 27/37, 35/41, 40/43 — the newest primes
  are the weakest. **The uncovered density factors over independent prime groups
  as a product of (p−c_p)/p, every factor strictly positive, so it is strictly
  positive for any finite set of families and can reach zero only if some modulus
  m has all m residues realised. 23 is the smallest prime with room (9/23,
  missing 14), but M=11 is the cheapest modulus to test overall, and it has
  only 3/11 residues covered (missing 0,1,2,3,4,6,8,9). The saturation question
  for modulus 11 is now the priority question: can the Salez seven-equation
  generator realise those 8 missing residues mod 11, or is there an obstruction?
  (Directive 5 — M=11 is the cheapest test.)**

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
- **A "verified" run whose aggregation line was piped away is not a result**
  (lesson learned this cycle): `extended_subprogression.py` was run with
  `| tail -50`, so its count/density summary died with the pipe while the
  FOUND lines survived in the capture; the JSON save never ran. The pattern to
  avoid: piping long-running aggregate output through `tail` or `head` and
  reading FOUND lines as if they were the result.
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
- Subprogression coverage (operator directive 3; superseded by the 1451-family
  row above — exact fractions in `code/out/subprogression_coverage.md`): 554
  families → 94.72% of n ≡ 1 (mod 840); as share of all n ≈ 0.1128%. Other
  five open classes: 0 families.
- **Wider-modulus sweep unfinished** (checked): `code/pattern_mining/extended_subprogression.py`
  (all M ≤ 60 + primes ≤ 101) was killed at the 540s timeout inside its FOUND
  loop; both captures (`extended_subprogression.captured.txt`, `.full.txt`) are
  fragments with no summary — no family count, no per-M residue table, no union
  density — and `code/out/subprogression_families.json` was never written (the
  `| tail -50` pipe masked the exit status). Visible families add moduli beyond
  the operator's set: M=38 (a=31920), 39 (32760), 41 (34440), 43 (36120). Whether
  the wider grid shrinks the 5.28% gap is still OPEN; a re-run must print the
  aggregation or it repeats the same dead end.

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
proved for density-one set. Concrete for the open classes: for n = 840k+1,
"b ≡ 3 (mod 4) divides n" becomes 840k ≡ −1 (mod b), i.e. k ≡ −840⁻¹
(mod b/gcd(840,b)); e.g. b=11 gives k ≡ 8 (mod 11), source example n=6721
(`research/sources/mballa-unified-parametric.full.md` §5.1). So each such b
yields an already-covered sub-progression of an open class. Ventas
(arXiv:2605.04551) uses the same b≡3 mod 4 mechanism, heuristically.

## Contradictions

- Brief's n≡3 (mod 4) identity vs computation (settled: brief wrong).
- **Bloem–Elsholtz survey lists the mod-840 unsolved classes as {1, 49, 121,
  169, 289, 361}** (full text, §2.2) vs this run's verified list
  {1, 121, 169, 289, 361, 529} (`code/verify_library_claims.py` Claim 2).
  49 is non-primitive (gcd(49,840)=7) and 529=23² is a primitive square, so
  the survey's list reads as a typo dropping 529 and adding 49. Cite the
  verified list, never the survey's.
- Elsholtz–Tao Prop 1.6 asserted "no Type I/II at odd squares" vs
  verify_library_claims.py Claim 3's noise (detector broken — it counts
  denominators divisible by n among triples found by a bounded search, which
  hits trivial multiples at small n; never cite Claim 3's output). Prop 1.6
  itself is now sourced with its proof read (quadratic reciprocity); Schinzel
  Thm 1 is the sharp, checkable statement of the same obstruction.
- Naive d=7 criterion vs corrected (mod-7) criterion (settled by 2705 rows).
- Subgroup-only characterization vs exact divisor-residue criterion (settled:
  56 counterexamples).
- `verify_current_coverage.py` "123 identity failures" vs `verify_subprogression_coverage.py`
  / `reverify_extended_families.py` clean: the 123-failure run was a **parser
  bug** in the verifier (it truncated `y=28*(3920*k…` at the first `*(`),
  not a family failure — after the parser fix, 0 identity failures. Do not
  re-raise the "123 failures" alarm (`code/out/commands.log`).

## Gaps

- **Beyond M=11: the gap structure is now exact** (directive 5, resolved):
  M=11 is **fully saturated over its legal residues** — see Established. The
  live bottleneck is the **QNR-allowed-but-unrealized gaps** at larger primes:
  M=17 gap [3,13], M=19 [3,5,7,10], M=23 [3,8], M=29 8 residues, M=31,
  M=37, M=41, M=43. `definitive_structure.py` shows the **structural ceiling**:
  with primes {11..37} the irreducible uncovered density (QR-blocked core) is
  0.2542%/branch; adding 41,43 lowers it to 0.0606%/branch — i.e. even if
  every Schinzel-legal residue at every used prime were realized, ~0.06–0.25%
  of n≡1 (mod 840) within a branch is **permanently** unreachable by any
  polynomial family at those primes (the finite-bound generator got to
  96.11%). **Closing the flat 3.89% of a single branch needs either a prime
  ∤ 840 not yet used, or an irreducible core that no polynomial identity can
  touch.** The squares of the class (m²≡1 mod 840, density 0) are provably the
  only n≡1 mod 840 no single polynomial identity covers
  (`square_obstruction.py`); all non-square members are Schinzel-legal for
  some prime.
- **Bulk promote asserted → checked** (operator directive 4). Resolved for all
  838 blocks: the earlier `verify_current_coverage.py` "123 identity failures
  / '(' never closed" were a **parsing bug in the verifier, not false
  families** — after the parser fix it parses 838 FOUND blocks / 123 distinct
  (a,b) with **identity failures 0** (`verify_current_coverage.py` tail;
  `reverify_extended_families.py`: symbolic-identity failures 0;
  `numeric_recheck_sample.py`: 603 families, 0 exact-equality failures at
  sampled k). Every `subprogression.captured.txt` block is identity-checked at
  its claimed (a,b). The `M=37` resid count is 10 (CONTEXT's earlier "9" was
  from a truncated capture).
- **Failing command** (operator directive 4). Retry count 6, run-failed 5 in
  `code/out/commands.log`. Read and fix before writing new programs.
- **prime-reduction still sourced, not checked** (directive 1 priority, still
  the exit-blocker of `research/threads/elementary-reductions.md`): write the
  scaling-lift proof `4/n = 1/x+1/y+1/z ⇒ 4/(nm) = 1/(mx)+1/(my)+1/(mz)` in
  exact arithmetic, capture it, and flip the claim to checked; then
  `reduction-mod24` once the mod-3/mod-8 identities are checked.d** (directive 1 priority, still
  the exit-blocker of `research/threads/elementary-reductions.md`): write the
  scaling-lift proof `4/n = 1/x+1/y+1/z ⇒ 4/(nm) = 1/(mx)+1/(my)+1/(mz)` in
  exact arithmetic, capture it, and flip the claim to checked; then
  `reduction-mod24` once the mod-3/mod-8 identities are checked.ble mechanically by the
  cleared-denominator test. Run `is_identity` on every one in bulk and flip
  them from `asserted` to `checked`.
- **Failing command** (operator directive 4). Retry count 6, run-failed 5 in
  `code/out/commands.log`. Read and fix before writing new programs.
- **prime-reduction still sourced, not checked** (directive 1 priority, still
  the exit-blocker of `research/threads/elementary-reductions.md`): write the
  scaling-lift proof `4/n = 1/x+1/y+1/z ⇒ 4/(nm) = 1/(mx)+1/(my)+1/(mz)` in
  exact arithmetic, capture it, and flip the claim to checked; then
  `reduction-mod24` once the mod-3/mod-8 identities are checked.