# Scholar digest assessment — this cycle's reading of the held library

This is the scholar's assessment of which held sources genuinely advance the
run's current direction (degree-20 frontier, char-p admissibility, minimal-
counterexample structure), which do not help, and what the run still lacks.
Each load-bearing summary already carries its claim blocks in its own digest
file; this note records the *joins and cuts*, not a re-digest of every file.

## Sources that help (and the one thing added this cycle)

- **Castryck–Laterveer–Ounaïes 2012** (degree 12, scenario framework, bad
  primes, V_k(d,t) variety) — the computational/theoretical cornerstone. The
  `ca-variety-results` reformulation is the exact object the scheme line of
  attack targets. Already in claim-block form.
- **Schaub–Spivakovsky 2023/2024/2025** (resultant reformulation, resultant-
  monomials structure, bad-prime criteria, minors criterion, upper bound) —
  the direct algebraic toolkit. THIS CYCLE: I independently hand-verified the
  load-bearing `resultant-monomials` claim (Thm 6/9) at d=3, upgrading it to
  `checked` there (see research/notes/verify-monomial-structure-d3.md). The
  general-degree statement still rests on the paper; a symbolic script for
  d=4 is queued (code/scholar/verify_monomial_structure.py).
- **Graf-von-Bothmer 2007** (p^k, 2p^k; lift theorem; char-p witnesses) — the
  engine of the settled families and the negative control.
- **Laterveer–Ounaïes 2012** (≥5 distinct roots, multiplicity-near-n,
  not-two shared roots, degree p+1 constraints) — the minimal-counterexample
  structure. All in claim-block form.
- **Ghosh 2024 finiteness / 2025 claim** — structurally the deepest scheme
  results (dim ≤2 in every characteristic; the char-0-only ℂ/Brouwer step).
  Unverified preprints; correctly labelled asserted/unchecked.
- **Massri 2018** (degree-20 no-3-recycled-roots; no multiplicity ≥11 root;
  p-adic Prop 7.7) — the only held source directly constraining the smallest
  open degree 20. Backed by full text.
- **Chellali–Salinier 2012** (5p^e explicit bad-prime list) — independent
  explicit list cross-checkable against Castryck. In claim-block form.
- **Polstra 2012** (convex-hull ⇔ trivial over C) — the geometric collapse
  step, char-0-only; the location where root-difference-coloring must break.
- **Draisma–de Jong 2011** (p-adic valuation method; not-two) — method source.
- **de Frutos 2013/2015** — superdiscriminant/bad-prime framework; the one-
  exponent discriminant literally equals the run's binomial criterion (checked
  per `defrutos-one-exponent-discriminant-equals-binomial-criterion`).

## Sources that do NOT help (recorded so nobody re-reads them)

- **Okolo 2025 (Zenodo, "OC framework")** — files restricted; the abstract is a
  crank-principle ("Blackness and Retraction forces", "metabolic efficiency of
  life") deriving from a self-styled "Organized Complexity" framework that
  claims to prove FTA-as-theorems. No mathematics recoverable; a claimed-proof-
  family entry only. Already flagged `okolo-2025-zenodo-crank`. Do not re-fetch.
- **Leggett 2025 (Zenodo, "dyadic dynamic system")** — same status: claimed
  proof inside a self-named framework with no refereed verification. Already
  flagged `leggett-2025-zenodo-dyadic`.
- **Gasull 2021 (SeMA, 33 open problems)** — abstract-only, paywalled; the CA
  connection is contextual (Gasull co-authored the Cima–Gasull–Mañosas
  extension paper) but nothing load-bearing is recoverable. Bibliographic lead
  only.
- **Yakubovich 2016** (Abel–Goncharov properties) — paywalled abstract; the
  new Sz.-Nagy identities are likely recoverable from the held 2013/2014 full
  texts' framework; nothing new is citable from the abstract alone.
- **three-proofs-casas-alvero 2013** (Fernández de las Heras) — a claimed
  proof that does not stand; recorded as a claimed-proof-family member, not a
  method. Its char-0-only content was never named, so it cannot even be tested
  against the char-p witnesses. Do not build on it.
- **Battiston 2015 (withdrawn), Dobrowolski 2017 (withdrawn), Lu 2017
  (suspect char-p trap)** — claimed-proof family; each recorded with the
  reason it does not stand. Not buildable methods.

## Contradictions observed

The library is internally consistent on the load-bearing items: the degree-5
bad-prime list agrees across Castryck Thm 4, Chellali–Salinier, and de Frutos
superdiscriminant; the degree-12 settlement and degree-20-as-smallest-open
agree across Castryck, Schaub–Spivakovsky, Wikipedia, Massri. Two genuine
contradictions are already recorded in the library and unchanged this cycle:
(1) **ordinary vs Hasse** derivative convention for the char-p bad-prime lists
   — resolved in favour of Hasse (the published lists use Hasse derivatives);
   the ordinary convention degenerates for p<n and gives wrong lists;
(2) the **degree-7 bad-prime count 366 vs 661** — resolved to 366 (the 661 is
   de Frutos's scheme-level "ineficaces" notion or a misreport, not the strict
   set).

One mild tension noted, not a contradiction: the abstract of de Frutos 2015
lists degree-6 bad primes as 53 primes (Castryck Table 1), and the thesis's
"ineficaces" language can differ from the strict CA-bad-prime set; the run's
own verified lists (n=5) match the strict set, so the distinction matters only
for degree 7+ counts.

## What the run still lacks (fresh assessment)

1. **A d=4 (and beyond) independent verification of `resultant-monomials`** by
   machine — d=3 is now hand-checked; d=4 symbolic resultant is feasible and
   queued. This upgrades a load-bearing engine from "rests on the paper" to
   "checked" for the degrees where the run actually computes.
2. **Any degree-20 constraint beyond Massri's no-3-recycled / no-mult-11.**
   Chávez Martínez 2018 (degree-20 with 4/5/6 distinct roots) is fetch-blocked
   at uva.es/unican.es; if the PDF is ever obtained it supplies the third
   degree-20 restricted class. Currently only asserted-by-abstract.
3. **A re-verification of the char-p break at d=2,3,4,5,6 (p=2)** — the oracle
   already confirms x^{p+1}−x^p and the deg-4/5/6 witnesses; the *named* break
   step (coefficient descent stops at the first pivot (d choose d−1)=d ≢ 0
   mod p) is located on paper for root-difference-coloring; the char-0-only
   Gauss–Lucas/convex-hull piece between the p^k grid remains the open hole.

## Bottom line
Nothing changes the run's standing status: **CA is open, smallest open degree
20, the Ghosh claim is unverified**. The one strengthening this cycle is the
d=3 monomial-structure check (independent of the source), closing the smallest
gap in the engine of the bad-prime criterion. All content is on disk; the
memory server was down for the Cognee store, so the finding lives in the note
until a later store.
