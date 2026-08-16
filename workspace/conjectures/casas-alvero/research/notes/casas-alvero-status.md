# Casas-Alvero — established status and claims

This note holds the run's central claims about the status and structure of the
Casas-Alvero conjecture, each tied to a source physically held in
`research/sources/`. Claim blocks below feed `research/CLAIMS.md`.

## The status question: has CA been proved?

```claim
id: ca-status-2025
statement: A complete proof of the Casas-Alvero conjecture has been CLAIMED
  (Soham Ghosh, arXiv:2501.09272, Jan 2025, v2 Mar 2026 "major revisions") but
  is an unverified preprint, not peer-reviewed or independently validated. The
  conjecture is therefore best treated as still OPEN as of 2026.
hypotheses: characteristic-0 field, all degrees d≥3
holds-here: true (this is the status question, not a theorem)
status: asserted-by-source
bearing: Determines the run's target per GOAL.md: a claimed proof that does
  not stand does not change the working assumption that CA is open.
anchor: research/sources/ghosh2025_proof_html.full.md (Theorem A + intro),
  research/sources/ghosh2025_proof_arxiv-abstract-v2.full.md (version record),
  research/sources/wikipedia_casas_alvero.full.md (still "Unsolved")
falsifies: A peer-reviewed publication or independent expert verification of
  the Ghosh argument.
```

```claim
id: ghosh-v2-version-record
statement: arXiv:2501.09272 version history, verified from the arXiv abs page:
  v1 submitted 16 Jan 2025 (15 KB); v2 submitted 21 Mar 2026 (30 KB, comment
  "Major revisions"). No withdrawal, no journal publication. The v2 doubles the
  length, consistent with either strengthening or repair; no community verdict
  exists either way.
hypotheses: none — bibliographic fact
holds-here: true
status: verified (primary source, held)
bearing: When the run cites the Ghosh claim, say which version; v1 full text and
  v2 record are both held. The claim has been revised but not withdrawn and not
  refereed.
anchor: research/sources/ghosh2025_proof_arxiv-abstract-v2.full.md
falsifies: an arXiv page showing different version dates/sizes, or a journal
  publication notice.
```

```claim
id: peerreviewed-2025-schaub-spivakovsky
statement: "On the Casas-Alvero conjecture", J. Commut. Algebra 17(2):199-202,
  Summer 2025 (received Nov 2024, accepted Jan 2025), peer-reviewed: CA is
  equivalent to ht(R_1,...,R_{d-1}) = d-1 in K[a_1,...,a_{d-1}] for the
  resultants R_i = Res(f, H_i(f)); and proves R_i ∉ (R_1,...,Ř_i,...,R_{d-1})
  for i ∈ {d-3,d-2,d-1}. Published independently of Ghosh's preprint; gives no
  support to it.
hypotheses: char-0 field K, monic degree d
holds-here: true
status: asserted-by-source (peer-reviewed; not re-proved here)
bearing: The resultant/height reformulation this run's scheme-theoretic method
  targets is now stated by a refereed source — cite it rather than re-derive.
  The non-membership for the three highest resultants is a concrete partial
  result to stress-test / extend.
anchor: research/sources/schaub_spivakovsky_jca-2025_on-casas-alvero.full.md
  (abstract; full text paywalled)
falsifies: a correction/erratum of the paper, or a computation showing the
  non-membership fails for some d.
```

## Smallest open degree

```claim
id: smallest-open-degree
statement: As of the held 2012-2024 sources, the smallest degree for which CA
  is not known to hold is 20, not 30.
hypotheses: d=12 verified by Castryck-Laterveer-Ounaïes 2012; d=8, d≤7 earlier
holds-here: true
status: asserted-by-source
bearing: Corrects problem.md's stale "n=30 smallest open" recall. The 30-claim
  ignored the 2012 degree-12 verification.
anchor: research/sources/castryck2012_degree12_html.full.md ("d=20, the next
  open case"), research/sources/schaub_spivakovsky_upper-bound-bad-primes_2024.full.md
  ("smallest degree not known is n=20"), research/sources/wikipedia_casas_alvero.full.md
falsifies: A held source settling degree 20 unconditionally (other than the
  unverified Ghosh preprint).
```

## Char-0 is essential: CA false in char p

```claim
id: charp-false
statement: CA is false in positive characteristic p; x^{p+1} - x^p is a
  separable counterexample not a pure power. Any proof of CA must use
  characteristic 0 somewhere and must break in char p.
hypotheses: char K = p > 0
holds-here: true (the hard constraint every candidate argument must survive)
status: asserted-by-source
bearing: Every candidate argument must be run against the char-p witnesses and
  the failing step named; an argument that also proves the char-p statement is
  refuted.
anchor: research/sources/grafvonbothmer2007_infinitely_many.full.md (Sec 3),
  research/sources/schaub_spivakovsky_bad-primes_2024.full.md, Wikipedia
falsifies: A char-free argument that nevertheless fails to generalise to char p
```

## Minimal counterexample structure (Laterveer-Ounaïes 2012)

```claim
id: min-counter-structure
statement: A non-trivial (non-pure-power) CA polynomial of degree N has at
  least 5 distinct roots (so N≥6), at least 4 distinct roots in its open
  Gauss-Lucas hull; CA holds if f has ≤4 distinct roots; a root of
  multiplicity ≥ N-2 forces f=(x-a)^N; the shared-root set {alpha_i} of
  f and f^(i) cannot have cardinality 2.
hypotheses: char 0, monic degree N
holds-here: true
status: asserted-by-source
bearing: Any counterexample is quite non-degenerate — it constrains what a
  minimal counterexample can look like (multiplicity patterns, number of
  distinct roots), which is one of the run's candidate structural targets.
anchor: research/sources/laterveer_ounaies_constraints_2012.full.md
falsifies: A held counterexample, or a later source contradicting these
  propositions.
```

## Restricted classes already settled

```claim
id: settled-classes
statement: CA holds in char 0 for degrees p^k and 2p^k (Graf-von-Bothmer et al
  2007); for 3p^k (p≠2) and 4p^k (p≠3,5,7) via p-adic valuations
  (Draisma-de Jong); for 5p^k, 6p^k, 7p^k with classified bad primes
  (Castryck et al 2012). Degree 12 verified. Degree 20 (Massri 2018): no
  counterexample with three recycled roots. Finiteness: for each n, the
  arithmetic Casas-Alvero scheme has finitely many K-points over any field
  (Ghosh 2024 preprint). Real-rooted: CA holds for real-rooted polynomials
  (Polstra 2012, Yakubovich 2015). Convex hull: a counterexample over C has a
  root not a vertex of its convex hull (Polstra 2012).
hypotheses: as stated, each with its bad-prime exclusions; real-rooted rows need char 0
holds-here: true
status: asserted-by-source
bearing: The run must not re-derive these; they are the settled boundary any
  new result must extend. The first composite non-covered degree is 20
  (30's old status superseded).
anchor: research/sources/grafvonbothmer2007_infinitely_many.full.md,
  research/sources/castryck2012_degree12_html.full.md,
  research/sources/massri2018_degree20.full.md,
  research/sources/ghosh2024_finiteness_full.full.md,
  research/sources/polstra2017_convex-hulls-casas-alvero.full.md,
  research/sources/yakubovich2025_validity-casas-alvero.full.md,
  research/sources/chellali2012_degree-5p-hal.full.md
falsifies: A held source contradicting any specific class; note Massri, Ghosh
  2024 and Yakubovich are preprints.
```

```claim
id: 5p-bad-primes-chellali
statement: CA holds for degrees 5p^e (e≥1, p prime) with p ≠ 2,3,7,11,131,193,
  599,3541,8009 (Chellali & Salinier 2012, HAL hal-00748843). This explicit
  bad-prime list for the 5p family is independent of Castryck et al.'s
  computational classification of 5p^k primes and should be cross-checked
  against it.
hypotheses: char 0, degree 5p^e, p outside the listed set
holds-here: true
status: asserted-by-source (HAL deposit, French; not journal-refereed as far
  as recorded here)
bearing: Gives the run an explicit finite bad-prime list for a settled
  infinite family — a target to recompute/verify (via the Ghosh J_T /
  Schaub-Spivakovsky criterion) and a check of intra-library agreement.
anchor: research/sources/chellali2012_degree-5p-hal.full.md (Prop 2.2)
falsifies: a counterexample in degree 5p^e for a p outside the list, or a
  source giving a different 5p bad-prime list.
```

## Claimed proofs that failed (the pattern)

```claim
id: battiston-withdrawn
statement: Giulia Battiston's 2015 claimed proof of CA (arXiv:1511.04932) was
  WITHDRAWN by the author: "contains a crucial error in its last page, I am
  thankful to Joseph Schicho for pointing it out to me." This joins the pattern
  of claimed CA proofs failing on a specific error, not surviving fresh attack.
hypotheses: none — historical fact about the literature
holds-here: true
status: asserted-by-source
bearing: Supports GOAL.md's warning against claiming CA; the deliverable is a
  partial result stated exactly. The Ghosh 2025 preprint is the current open
  claim and is likewise unverified.
anchor: research/sources/battiston_casas-alvero-survey_2015.full.md (comments)
falsifies: A source showing the Battiston paper was reinstated/validated.
```

## Reported computational boundary

```claim
id: computational-boundary
statement: Direct verification of CA by Gröbner basis is feasible over ℚ up to
  about degree 8; degree 12 was settled only by a combination of theoretical
  scenario reduction and Gröbner in characteristic p, costing ~3 weeks and
  ~90 GB RAM per scenario; pushing that method to d=20 is reported "utopic".
hypotheses: characteristic matters (ℚ vs 𝔽_p Gröbner answer different questions)
holds-here: true
status: asserted-by-source
bearing: This is the honest reportable boundary for this run's own oracle
  reproduction; recomputing ≤8 over ℚ and the char-p witnesses is the feasible
  target, with the feasibility ceiling (likely 9-10 over ℚ) itself a result.
anchor: research/sources/castryck2012_degree12_html.full.md
falsifies: A held source showing larger direct-over-ℚ verification succeeded
  cheaply.
```

## The char-p negative-control witnesses (for the oracle)

```claim
id: charp-witnesses
statement: The char-p witnesses the oracle must recognise as satisfying the
  hypothesis but NOT being pure powers are: x^{p+1} - x^p in char p (separable
  counterexample, Wikipedia/Schaub-Spivakovsky), and the explicit
  f(x)=x(x-1)^4(x-8)(x-18) over F_23 with common-root sets
  {1},{1,18},{1},{0},{18},{1} for derivatives 1..6 (Castryck et al, Example in
  Sec 1). Any polynomial f(X^p) without constant term also works (all
  derivatives vanish).
hypotheses: char K = p > 0
holds-here: true (these are the exact tests the oracle must pass)
status: asserted-by-source
bearing: The oracle in code/lib must report these as satisfying
  gcd(f,f^(i))≠1 for all i, and f NOT a pure power — the negative control that
  proves the checker measures the right thing. Also: generic random f must FAIL.
anchor: research/sources/wikipedia_casas_alvero.full.md,
  research/sources/schaub_spivakovsky_bad-primes_2024.full.md,
  research/sources/castryck2012_degree12_html.full.md (Sec 1 example)
falsifies: A run of the oracle showing one of these does NOT pass the
  hypothesis, or IS reported as a pure power.
```

## A third claimed-proof family (Fernández de las Heras 2013)

```claim
id: three-proofs-2013
statement: Fernández de las Heras & Fernández de las Heras (arXiv:1306.5656,
  2013, "Three proofs of the Casas-Alvero conjecture") claim three proofs of
  CA over C. Submitting to J. Approx. Theory. Like the Battiston (withdrawn)
  and Ghosh (unverified) claims, this is a claimed proof family that has not
  become an accepted peer-reviewed resolution; CA is still treated as open.
hypotheses: complex polynomial, char 0
holds-here: true
status: asserted-by-source
bearing: Documents the pattern that CA attracts claimed proofs which do not
  become accepted resolutions; reinforces the warning against claiming CA and
  the need to state partial results exactly.
anchor: research/sources/three-proofs-casas-alvero_2013.full.md
falsifies: A source showing one of its three proofs was published/validated.
```

## A fourth claimed-proof family (Yakubovich 2015)

```claim
id: yakubovich-2015-claim
statement: Yakubovich, "The validity of the Casas-Alvero conjecture"
  (arXiv:1504.00274, 2015, preprint) claims CA is solved affirmatively via
  Abel-Goncharov interpolation polynomials, Sz.-Nagy type identities, and a
  Schoenberg/Rolle analogue. Like the other claimed-proof families, it never
  became an accepted resolution: every post-2015 source (Castryck 2018,
  Schaub-Spivakovsky 2023-2025, Wikipedia) still treats CA as open.
hypotheses: complex polynomials, char 0; includes real-rooted special cases
holds-here: true
status: asserted-by-source (preprint)
bearing: Another instance of the pattern; also the run's first physical
  source with real-rooted partial results (with the same preprint caveat the
  rest of that paper carries).
anchor: research/sources/yakubovich2025_validity-casas-alvero.full.md
falsifies: a source showing the paper was validated/published as a resolution.
```

## A fifth claimed-proof family (Lu 2017)

```claim
id: lu-2017-claim
statement: Lu, "Casas-Alvero conjecture in computational algebraic geometry"
  (arXiv:1707.04754, 2017, preprint) claims a proof via regular sequences and
  dimension counts, in particular reducing CA to an F_p counting statement
  (Prop 2.3: CA holds for n iff for large primes p the variety
  Z(f^(1)(x_i1),...,f^(n-1)(x_i_{n-1})) over F_p has size p "for any branch").
  SUSPECT: since CA is false in char p, a proof whose core is an F_p count
  must either be stating a false char-p theorem or conceal the char-0-only
  step in the reduction; the paper does not appear to locate it. Unverified,
  and flagged for the oracle char-p test.
hypotheses: char 0 (claimed), but the argument is char-p-counting
holds-here: true (another claimed proof; runs into the char-p trap)
status: asserted-by-source (preprint), suspect
bearing: The precise char-p failure point to find: run Prop 2.3's counting
  against n = p+1 and the known char-p counterexamples — the count must NOT
  be p on their branches.
anchor: research/sources/lu2017_casas-alvero-computational-ag.full.md
falsifies: a correct char-0-only argument with this shape, or a demonstration
  that the F_p count does separate the pure-power branch.
```

## Real-rooted / convex-hull restricted classes

```claim
id: real-rooted-and-convex-hull
statement: CA holds for real-rooted complex polynomials (equivalent condition
  proved via Vieta/multiplicity by Polstra 2012, RHUMJ 13(1); partial results
  e.g. degree-n real-rooted trivial if its (n-2)-nd derivative has a double
  root, by Yakubovich 2015); and over C a CA counterexample cannot have all its
  roots as vertices of its convex hull (Polstra 2012).
hypotheses: char 0; real roots or convex-hull condition
holds-here: true (these are the "real-rooted" known cases problem.md lists)
status: asserted-by-source (Polstra: refereed undergrad journal; Yakubovich:
  preprint)
bearing: Supplies the real-rooted settled class the library was missing.
  Convex-hull statement is a geometric constraint on a minimal counterexample,
  complementing Laterveer-Ounaïes' Gauss-Lucas hull result.
anchor: research/sources/polstra2017_convex-hulls-casas-alvero.full.md,
  research/sources/yakubovich2025_validity-casas-alvero.full.md
falsifies: a real-rooted counterexample, or a counterexample with all roots on
  its convex hull.
```
