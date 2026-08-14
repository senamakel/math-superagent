# Formally verified UNSAT certificate checking — GRAT / LRAT for the colouring oracle

**Sources** (technique tier; abstracts read verbatim via exa_search results):
- Lammich, "Efficient Verified (UN)SAT Certificate Checking", J. Automated
  Reasoning (2019), doi:10.1007/s10817-019-09525-z — introduces **GRAT**, a
  formally verified toolchain for **DRAT** certificates (generator + checker
  proven correct down to the integer-array representation of the formula, in
  Isabelle/HOL); supports full DRAT; faster than the unverified drat-trim.
- Lammich, "Fast and Verified UNSAT Certificate Checking" (2024),
  doi:10.1007/978-3-031-63498-7_26 — extends to the **LRAT/DRUP lineage**
  (LRUP, LRAT, LPR), streamed in parallel with CaDiCaL, verified down to LLVM
  IR; "if the checker reads an LRAT certificate and CNF, it guarantees the
  certificate proves unsatisfiability of the formula."
- Since 2016 the SAT competition mandates UNSAT certificates in its main
  track; DRAT became the de facto standard, with DRUP/LRAT generalisations.

## What this establishes for the run's oracle

GOAL.md's oracle 2 (complete k-colourability test) reports UNSAT when a
candidate graph is not 4-colourable — the load-bearing fact behind any
claimed 5-chromatic graph. A SAT solver's UNSAT is a claim about the solver, so
the run's own GOAL discipline requires the independent, mechanical
re-verification. The standard for that is:

- **SAT side:** produce a satisfying assignment (a colouring witness) — trivial
  to check.
- **UNSAT side:** have the solver emit a **DRAT/LRAT certificate**; check it
  with a **formally verified checker** (GRAT, or an Isabelle-verified LRAT
  checker). The checker is proven sound w.r.t. the CNF semantics, so a passing
  check is a theorem: the graph really is not k-colourable.

This is exactly the "complete method" GOAL.md asks for, with the 
"independently of the producing code" discipline satisfied at the proof-checker
level rather than by re-running a second solver. Two independent paths remain
cheaper and are also good practice: (a) the symmetry-broken exhaustive search
(claim `symmetry-breaking-sat-technique`) as a second colouring test, and
(b) the Kostochka–Yancey hereditary-sparseness certificate
(`ky-potential-method`) as a no-SAT-required 4-colourability proof where it
applies.

## Note on download

Not downloaded; this is a note from search-result abstracts (the primary
papers are JAR/Springer, technique-tier, no Hadwiger–Nelson content). The
claim here is about a verification standard, not about the plane-colouring
problem, so it carries no answer-tier risk.

```claim
id: drat-lrat-verified-unsat-certificates
statement: An UNSAT answer from a SAT solver can be made a machine-checked theorem: solvers emit DRAT/LRAT clausal certificates, and formally verified checkers (GRAT 2019; Isabelle-verified LRAT checkers 2024) prove the certificate entails unsatisfiability of the CNF, with correctness established down to integer-array / LLVM semantics. The SAT-competition main track has required UNSAT certificates since 2016.
hypotheses: CNF formula in DIMACS; solver produces a valid DRAT/LRAT/DRUP/LPR certificate; the colouring CNF correctly encodes k-colourability of the graph (a separate encoding check, e.g. on the 7-vertex graph).
holds-here: yes — makes the oracle's "not 4-colourable" verdict an independently checkable proof artifact, satisfying GOAL.md's complete-method and independent-re-verification discipline for any claimed 5-chromatic graph: SAT + assignment witness checked by hand/program, UNSAT + DRAT certificate checked by a verified checker.
status: sourced (abstracts of Lammich 2019 JAR and 2024, read verbatim from search results; the 2016 competition rule is stated in the 2017/2024 papers)
bearing: the certification pipeline for every future "chi >= 5" claim the run makes; also relevant to G-exhaust UNSAT certificates.
anchor: research/sources/drat-verified-unsat-certificates.md
```