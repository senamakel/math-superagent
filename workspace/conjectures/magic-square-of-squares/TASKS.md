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

- [ ] **RUN `verify_pell_symbolic.py`** (directive 11, item 1):
      `timeout 540 python3 code/out/verify_pell_symbolic.py 2>&1 | tee code/out/verify_pell_symbolic.captured.txt; echo EXIT_CODE=$?`
      Reconcile its sympy output with the four numeric results already captured.

- [ ] **ANSWER THE GFP-x2P BLOCKING QUESTION** (directives 10 and 11, item 2):
      Does the Garcia-Fritz–Pasten AP-length bound (Theorem 1.8, C^(r+1))
      apply to x-coordinates of *doubled* points x(2P) or only to x(P)? The
      run's files already contain the answer — GFP §1.1 defines an AP as
      x(P_i) for P_i ∈ E(Q), and 2Q ∈ E(Q) so doubled points are covered —
      but it is scattered across CONTEXT.md, TASKS.md, the uniformity thread,
      CLAIMS.md, and the approach file. Consolidate the answer in ONE place
      the operator can read: write `code/out/gfp_x2p_answer.md` with a claim
      block stating:
      - the exact GFP definition of "arithmetic progression on E"
      - why x(2Q) falls under it (2Q ∈ E(Q))
      - the resulting bound on the Robertson curve E: y² = x(x²−c²)
      - the effective-constant gap (HMS makes C computable but >> 3, so
        C^(r+1) < 3 fails for any plausible rank)
      - conclusion: approach sound on definitions, blocked by constant size,
        NOT refuted; the conditional reduction to a finite computation
        (Theorem 1.2, uniform rank boundedness) is the best structural result.
      **The claim block MUST carry `answers: exact-reduction-magic-507c`.** That
      field — not prose saying "RESOLVED" in REQUESTS.md — is the only thing
      that closes the request in the ledger. The run wrote "RESOLVED" in
      REQUESTS.md prose five times while no claim block on disk carries the
      `answers:` field, which is exactly why the operator still sees
      "Still open" after five consecutive checks. Without that field the
      request stays open no matter what the prose says.
      If GFP does NOT apply, declare `uniform-height-bound-elliptic-ap`
      REFUTED IN ITS CURRENT FORM and state whether restating on the Kummer
      surface K = E/{±1} recovers it — and file the same claim block with
      `answers: exact-reduction-magic-507c`. Either answer is a genuine
      partial result. **Nothing else is worth more right now.**

- [ ] **PARK THE THREE NEW APPROACHES** opened in violation of directive 10
      ("do not open a fifth approach before answering the blocking question"):
      `freys-curve-four-q-isogenies`, `integral-brauer-manin-nine-square`,
      `richardson-orbits-weyl-group`. Change their status from `proposed` to
      `parked-behind-blocking-question`. Do not delete them; they may become
      relevant after the blocking question is answered, but no work on them
      until then. The run went from 12 to 15 approaches with proved stuck at
      16 while the operator watched; this stops the proliferation.

## After the blocking question is answered

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