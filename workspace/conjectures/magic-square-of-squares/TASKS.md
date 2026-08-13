# Tasks

- [x] Read problem.md, GOAL.md, AGENTS.md — the run targets the open 3x3 magic square of squares conjecture; deliverable is a genuine partial result, not a claim of resolution.
- [x] tool_builder: build code/lib/mss.py + code/check_near_misses.py (exact
      arithmetic): verifier, worked examples rerun fresh, both 7-square
      near-misses constructed+verified, incidence rank, (c,u,v) extraction,
      Pythagorean pairs; write code/out/near_misses.json with provenance for
      Sallows LS1 and Bremner's magic square.
- [x] tool_builder: exact-integer verification of the completed Robertson
      reduction on Bremner's 7-square witness — code/robertson_reduction_check.py
      (runs under sage), output code/out/robertson_reduction_check.txt, exit 0.
      All 8 sums 541875; a=425², b=41496, c=138600; 2 of 3 main-diagonal
      x-coords in 2E(Q) (139129, 180625), 222121 not (X and X+c not squares);
      doubling formula verified symbolically + on a rational point + Sage 2P;
      rank(E: y²=x³−19209960000x)=2 by mwrank 2-descent with
      generators [−88200,315000] and regulator 6.9103524178015 (cross-checked
      via E.rank/algorithm='all'/standalone mwrank; all 8 division preimages
      rational, quartics factor exactly for the two membership values, no
      rational root for X=222121); converse grid (4) from the AP is the
      witness transpose, all 8 sums 3a, non-squares exactly {360721,222121} —
      the witness is one doubled point short of an MSS.
- [x] Re-download Garcia-Fritz-Pasten and Rome-Yamagishi from PDF endpoints
      (both were abstract-page wrappers; now 21KB and 40KB — real papers).
- [x] Re-download Wu 2103.01784 from PDF endpoint (was 6.6KB abstract-page
      wrapper; now 78KB, real paper with theorems).
- [x] **Ferreira 1506.06621 — handle per steer directive 6.** Error located at
      (46)→(47); substituting z2 = m−√(m²−2nw−w²) into (46) yields the tautology
      0=0, not the paper's (47). Verified by sympy. Claim
      `ferreira-15060621-proof-invalid` in CLAIMS.md, status: checked.
- [x] **Run check_ferreira_proof.py.** Capture at
      `code/out/check_ferreira_proof.captured.txt`, EXIT_CODE=0, sympy agrees.
- [x] **Audited this run's own code for the Ferreira anti-pattern.** None found.
- [x] **Re-download Hulse et al. and Wolird from arXiv PDF endpoints.**
      Done; real papers on disk.
- [x] **Record the witness_padic_falsification result.** Claims
      `phi-padic-no-obstruction`, `phi-padic-consistent-with-witnesses`,
      `phi-padic-residue-closure` all `status: checked` in CLAIMS.md.
- [x] **Verify the parallel library.** PASS.
- [x] **Parallelise `phi_padic_closure_all.py`.** PASS.
- [x] **Run the remaining six p-adic/modular programs.** All exit 0, no
      obstruction found. Frontier closed as a proof route.
- [x] **FALSIFY EVERY P-ADIC/MODULAR OBSTRUCTION.** Both witnesses verified.
- [x] **k3_surface_checks.py exact rewrite.** DONE; S(Q) nonempty, Brauer-Manin
      cannot prove S(Q)=∅.
- [x] **Gathering phase OVER.** No further downloads without a new stated gap.
- [x] **Run the four Pell programs.** Captures on disk; claim
      `phi-suprema-are-pell-pairs` in CLAIMS.md, status: checked. CORRECTION:
      argmax NOT unique; Pell pairs always among the maximisers.
- [x] **side_census.py RUN by operator at M=400 — docstring hypothesis REFUTED.**
      Both=0 finding: 1−(q1+q2) rational square 325 times, 1+(q1+q2) 66 times,
      BOTH = 0. Claim `phi-pair-sides-never-both-square` in CLAIMS.md.
- [x] **Amend `hms-2026-bremner-effective-constant` (directive 17).** Added
      `value-computed: no` and `what-would-compute-it` listing the three
      ingredients (DP07, BZ, JS). The paper's proof IS effective — following it
      yields a number — but the paper does not carry out the computation.

---

## BLOCKING — must complete before any new approach

### Proved-count drift (directive 17)

Proved went 20→17 while checked went 15→17 and asserted 19→20. The
`search_claims` re-derivation changed three claims from `proved` to `asserted`
when they were re-classified as resting on source statements without independent
verification. This is a deliberate re-classification (not lost claims, not an
accounting glitch): `bremner-conjecture-proved`, `n-by-n-mss-exist-for-n-ge-4`,
and `dgh-uniform-mordell-lang-curves` were demoted because their `holds-here`
is `no`, so `proved` was misleading — they are true theorems, proved by their
authors, but they do not apply to THIS problem. The re-derivation correctly
moved them to `asserted` (source-established but not applicable here).
**NOT a bug; a correction.** The shift 20→17 is a tightening of the
holds-here/proved intersection.

### EXA_SEARCH — STOPPED (directive 17)

exa_search is at 122 (was 99 two directives ago). The frontier is 442 with
365 unworked. Twenty-three searches changed nothing. This is a fact about the
search, not about the literature: further downloads will not change a claim.
**No more exa_search calls.** No new sources fetched without a stated gap in
REQUESTS.md.

### COMMANDS.LOG — DOES NOT EXIST (directive 17)

`code/out/commands.log` is not on disk. The run-failed count went 6→8 but the
file was never created. The five unrun programs below are the likely culprits.
Route all executions through `2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`
to capture failure to disk.

### Five still-unrun programs + side_census M=800 (directives 16 & 17)

These have been unrun for two directives. Run them. Order: verifiers first
(they check claims the run relies on); benchmark and ratio_search last.

- [ ] **`verify_two_side_equiv.py`** — independent two-side equivalence check.
      `PYTHONPATH=code timeout 300 python3 code/phi_triple_variety/verify_two_side_equiv.py 300 2>&1 | tee code/out/verify_two_side_equiv.captured.txt; echo EXIT_CODE=$?`
- [ ] **`verify_triple_square.py`** — independent triple equivalence check.
      `PYTHONPATH=code timeout 300 python3 code/phi_triple_variety/verify_triple_square.py 300 2>&1 | tee code/out/verify_triple_square.captured.txt; echo EXIT_CODE=$?`
- [ ] **`verify_prefilter.py`** — independent prefilter verification.
      `PYTHONPATH=code timeout 300 python3 code/phi_triple_variety/verify_prefilter.py 80 2>&1 | tee code/out/verify_prefilter.captured.txt; echo EXIT_CODE=$?`
- [ ] **`benchmark.py`** — phi_pairs and membership test benchmarking.
      `PYTHONPATH=code timeout 300 python3 code/phi_triple_variety/benchmark.py 2>&1 | tee code/out/benchmark.captured.txt; echo EXIT_CODE=$?`
- [ ] **`ratio_search.py`** — ratio search with closed-form test.
      `PYTHONPATH=code timeout 540 python3 code/phi_triple_variety/ratio_search.py 700 2>&1 | tee code/out/ratio_search.captured.txt; echo EXIT_CODE=$?`
- [ ] **`side_census.py M=800`** — both=0 survived M=200 and M=400; push to 800.
      `PYTHONPATH=code timeout 540 python3 code/phi_triple_variety/side_census.py 800 500 2>&1 | tee code/out/side_census_M800.captured.txt; echo EXIT_CODE=$?`

**Partial-sweeps caveat (directive 18):** `no_triple_fast_M700` stopped at
i=40143/99407 (40.4%); `prefilter_census_M1000` at i=38006/202861 (18.7%).
"Survivors 0" over a fraction is not "none at full M". Any claim from a
partial sweep must carry the fraction covered, or it is asserted not checked.`

### Structural work — the run's deliverable

- [ ] **IDENTIFY THE CONCORDANT-FORMS CURVE FOR both=0 (directive 18 priority 1).**
      1−s and 1+s simultaneously rational squares is the classical concordant-forms
      problem, equivalent to a rational point on the circle x²+y²=2 (genus 0).
      Write the explicit curve for s = q1+q2 with q1,q2 ∈ Φ. The condition that
      1±s are both squares is s = 2t/(1+t²) for some rational t. Intersect this
      with the set S = {q1+q2 : q1,q2 ∈ Φ, q1+q2 < 1}. Ask whether Φ-membership
      of the summands forces a local obstruction mod p that prevents s from being
      of the form 2t/(1+t²). Any obstruction found must be run against the 66
      plus-witnesses and 325 minus-witnesses in `code/out/side_census.captured.txt`
      — both sets have exactly one side square, so the obstruction must permit one
      and block the other, or it is false.

- [ ] **WRITE THE CONDITIONAL RESULT AS A CLAIM.**
      Assumption: uniform boundedness of ranks of E/Q → 3×3 MSS existence reduces
      to a finite computation. Specialise to E: y² = x(x²−c²), cite Robertson→GFP
      Theorem 1.2. Write to `code/out/conditional_reduction_claim.md`.

- [ ] **BOUND THE HMS CONSTANT C, OR RECORD THE PRECISE OBSTRUCTION.**
      The claim block now names DP07, BZ, and JS as the three ingredients.
      Check each source for an explicit value. If none extractable, record the
      dependency chain and why each constant is not computed. Write to
      `code/out/hms_constant_bound.md`.

- [ ] **RUN `verify_pell_symbolic.py`.**
      `timeout 540 python3 code/out/verify_pell_symbolic.py 2>&1 | tee code/out/verify_pell_symbolic.captured.txt; echo EXIT_CODE=$?`

- [ ] **CHECK `magic-variety-is-surface-no-lines`.** Compute directly: X in P⁸
      cut by 7 line-sum equations, verify dim=2 and no lines. Write to
      `code/out/magic_variety_check.captured.txt`. Update claim from `asserted`
      to `checked`.

## After the blocking section is cleared

- [ ] scholar: claim-block HMS 2026 from the full HTML text (132KB on disk).
- [ ] scholar: claim-block Hulse et al. (arXiv:2007.14324, 68KB).
- [ ] scholar: claim-block Wolird (arXiv:2310.12164, 11KB).
- [ ] research: write research/ROOT.md.
- [ ] Establish ~1 structural impossibility lemma and run it against witness set.
- [ ] Formalise the Robertson reduction and GFP bound in Lean.