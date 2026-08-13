# Tasks

- [x] Read problem.md, GOAL.md, AGENTS.md — the run targets the open 3x3 magic square of squares conjecture; deliverable is a genuine partial result, not a claim of resolution.
- [x] tool_builder: build code/lib/mss.py + code/check_near_misses.py (exact
      arithmetic): verifier, worked examples rerun fresh, both 7-square
      near-misses constructed+verified, incidence rank, (c,u,v) extraction,
      Pythagorean pairs; write code/out/near_misses.json with provenance for
      Sallows LS1 and Bremner's magic square.
- [x] Re-download Garcia-Fritz-Pasten and Rome-Yamagishi from PDF endpoints
      (both were abstract-page wrappers; now 21KB and 40KB — real papers).
- [x] Re-download Wu 2103.01784 from PDF endpoint (was 6.6KB abstract-page
      wrapper; now 78KB, real paper with theorems).
- [x] **Ferreira 1506.06621 — handle per steer directive 6.** PDF fetched
      (65,364 bytes, real paper, not a wrapper — the /abs/ and /html/ wrappers
      were the stale copies the steer spotted). Category math.GM, no
      presumption of correctness. Error located at (46)→(47): substituting
      z2 = m−√(m²−2nw−w²) into (46) yields the tautology 0=0, not the paper's
      (47). Verified by sympy (`code/out/check_ferreira_proof.py`) and by
      construction with witness m=5,n=3,w=1. Claim `ferreira-15060621-proof-invalid`
      in CLAIMS.md, status: checked. The paper establishes nothing.
- [x] **DIRECTIVE 7.1 — Run check_ferreira_proof.py.** Executed; capture at
      `code/out/check_ferreira_proof.captured.txt`, EXIT_CODE=0, sympy agrees
      with the operator — the substitution yields 0=0. Ferreira refuted.
- [x] **DIRECTIVE 7.3 — Audited this run's own code for the Ferreira
      anti-pattern.** `phi_canonical_check.py`, `phi_identity_verify.py`,
      descent and p-adic code checked; no substitution-of-solved-root-back
      pattern found. Recorded in CONTEXT.md Ruled Out.
- [x] **DIRECTIVE 8: Re-download Hulse et al. and Wolird from arXiv PDF endpoints.**
      Done; real papers (68KB and 11KB) on disk.
- [x] **DIRECTIVE 8: Record the witness_padic_falsification result.** Claims
      `phi-padic-no-obstruction`, `phi-padic-consistent-with-witnesses`,
      `phi-padic-residue-closure` all `status: checked` in CLAIMS.md with
      exact bounds. No drift.
- [x] **STEP 1: Verify the parallel library.** PASS.
- [x] **STEP 2: Parallelise `phi_padic_closure_all.py`.** PASS, |Φ(200)|=8156 matches serial.
- [x] **STEP 3: Run the remaining six p-adic/modular programs.** All exit 0, no
      obstruction found. Frontier closed as a proof route.
- [x] **FALSIFY EVERY P-ADIC/MODULAR OBSTRUCTION.** Both witnesses verified,
      no statement forbids a near-miss. RESULT ALL CONSISTENT.
- [x] **k3_surface_checks.py exact rewrite.** DONE; S(Q) nonempty, Brauer-Manin
      cannot prove S(Q)=∅, approach `brauer-manin-k3-surface` closed outright.
- [x] **DIRECTIVE 9: Gathering phase OVER.** The run has what it needs. No
      further downloads without a new stated gap.
- [x] **Run the four Pell programs the operator ran externally.** Captures on
      disk at `code/out/{verify_pell_records,verify_pell_argmax_unique,
      pell_record_seq,prove_pell_record}.captured.txt`; claim
      `phi-suprema-are-pell-pairs` in CLAIMS.md, status: checked.
      **CORRECTION (directive 11):** verify_pell_argmax_unique REFUTES its own
      name — ties=2 at M≤60 and M≤960, record-strictly-increasing=False. The
      argmax is NOT unique; Pell pairs are always among the maximisers but not
      the only ones. The claim `phi-suprema-are-pell-pairs` states this
      correctly (no uniqueness asserted).

---

## BLOCKING — must complete before any new approach

- [ ] **WRITE THE CONDITIONAL RESULT AS A CLAIM** (directive 12, item 1):
      The run's best structural output: assuming uniform boundedness of ranks
      of elliptic curves over Q, the existence of a 3×3 magic square of nine
      distinct squares reduces to a FINITE computation. State the specialisation
      to E: y² = x(x²−c²) explicitly, hypothesis named (uniform rank boundedness),
      reduction step cited (Robertson→Garcia-Fritz–Pasten Theorem 1.2). Write
      the claim block into `code/out/conditional_reduction_claim.md` with all
      required fields and `status: checked` (the Robertson reduction and the
      GFP theorem are both established; what is new here is the explicit
      specialisation). **This claim is the run's deliverable.** Nothing else
      is worth more right now.

- [ ] **BOUND THE HMS CONSTANT C, OR RECORD THE PRECISE OBSTRUCTION**
      (directive 12, item 2 + directive 13, item 2):
      HMS Theorem 1.1 (arXiv:2603.06483, 132KB HTML on disk) says C is
      "effectively computable." Extract from the full text what C is a
      function of: David–Philippon constants (quantitative Schneider–Lang),
      PFR constants (Gowers–Green–Manners–Tao), and the genus-2 curve degree
      in the Dimitrov–Gao–Habegger construction. Give any explicit bound the
      paper states or its ingredients imply. If none can be extracted, record
      that as the precise obstruction with the chain of dependencies and the
      reason each ingredient's constant is not computed in the source. Write
      the result to `code/out/hms_constant_bound.md`.

- [ ] **RUN `verify_pell_symbolic.py`** (directive 12, item 3):
      `timeout 540 python3 code/out/verify_pell_symbolic.py 2>&1 | tee code/out/verify_pell_symbolic.captured.txt; echo EXIT_CODE=$?`
      Reconcile its sympy output with the four numeric results already captured.

- [ ] **OPEN THE NEXT REQUEST IN REQUESTS.md** (directive 12, item 3):
      The only request (`exact-reduction-magic-507c`) is RESOLVED. The run is
      running without a stated gap. Open request `hms-constant-bound`:
      "What is the smallest explicit upper bound for C in HMS Theorem 1.1
      that can be extracted from the paper's ingredients (David–Philippon,
      PFR, the genus-2 construction), or from subsequent work?" If C cannot
      be extracted, state what is missing from each ingredient.

- [ ] **CHECK `magic-variety-is-surface-no-lines`** (directive 13, item 1):
      Compute directly rather than asserting on a source's word: X in P⁸ cut
      by 7 homogeneous line-sum equations, verify dimension = 2 (a surface)
      and the absence of lines. Write the program, run under timeout 540 with
      tee to `code/out/magic_variety_check.captured.txt`. Record the result
      as a claim block updating the status from `asserted` to `checked`.
      This is the one asserted claim directive 13 picked to make checked —
      it is a concrete computation the run can do.

## After the blocking section is cleared

- [ ] scholar: claim-block HMS 2026 from the full HTML text already on disk
      (`research/sources/harrison-mudgal-schmidt-sum-product-bremner-2026.html.full.md`,
      132KB). Theorem 1.1 effective-constant Bremner; Theorem 1.3 sum-product;
      Corollary 2.2 generalised APs. Replace the auto-generated summary.
- [ ] scholar: claim-block Hulse et al. (arXiv:2007.14324, 68KB, double
      Dirichlet series, asymptotic counts for 3-square APs).
- [ ] scholar: claim-block Wolird (arXiv:2310.12164, 11KB, Gaussian triplets
      ↔ Pythagorean triples).
- [ ] research: write research/ROOT.md — Bremner reduction, real computational
      bound, restricted classes, near-miss provenance.
- [ ] Establish ~1 structural impossibility lemma (extra-hypothesis partial
      result) and run it against the witness set.
- [ ] Formalise the Robertson reduction and the Garcia-Fritz-Pasten bound in
      Lean as they stabilise.