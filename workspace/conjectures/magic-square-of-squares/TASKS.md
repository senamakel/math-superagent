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
- [ ] **REFACTOR THE SEVEN P-ADIC/MODULAR PROGRAMS FOR PARALLELISM AND TIMEOUTS, THEN RUN THEM.** These seven programs exist and have never produced captured output — they have been killed by the tool ceiling, not skipped: `code/phi_2adic.py`, `code/phi_3adic_closure.py`, `code/phi_padic_valuation.py`, `code/phi_padic_closure_all.py`, `code/phi_padic_closure_exact.py`, `code/phi_mod3_check.py`, `code/phi_modular_obstruction.py`. The four phi programs that DID produce captures (`phi_fibre_genus_run.py`, `verify_phi_doubling.py`, `phi_canonical_check.py`, `phi_identity_verify.py`) all used `timeout 300` or `timeout 600 python3 ... ; echo EXIT_CODE=$?` — that is the difference. Three rules, applied to every one:
      1. **Timeout wrapper.** Launch every one as `timeout 540 python3 code/<name>.py ; echo EXIT_CODE=$?` so a kill is visible as a result rather than as silence. The tool ceiling is 10 minutes; 540 seconds leaves headroom.
      2. **Parallelism.** This box has 28 CPUs and the container has CPU quota `max`. Any search over moduli, primes, or (m,n) pairs is embarrassingly parallel — split the outer loop with `multiprocessing.Pool`. State in the captured output how many workers were used and what the search space was. If the program already has a single-threaded loop, refactor it before running it.
      3. **Bounded capture.** If a search genuinely cannot finish inside the ceiling, that is a finding about the method — bound it explicitly, capture the partial result with the bound stated, and record what was NOT covered. Do not re-run the same unbounded search hoping it lands.
      Capture stdout to `code/out/<name>.captured.txt` for each. Do this before opening any new approach or thread.
- [ ] **FALSIFY EVERY P-ADIC/MODULAR OBSTRUCTION** — a p-adic or modular
      closure result is an IMPOSSIBILITY argument. Run every obstruction found
      against `code/out/near_misses.json` using the verifier in `code/lib/mss.py`.
      If a residue argument would also forbid the Sallows LS1 grid or Bremner's
      7-square grid, the argument is FALSE and must be recorded as refuted, not
      weakened. An obstruction lemma not run against the witness set has status
      `asserted`, never `checked`. Record outcomes in `code/out/` and as claim
      blocks.
- [ ] **Settle the doubled-point question for GFP from the paper on disk.**
      The paper (`research/sources/garcia-fritz-pasten-bremner-uniformity-2026.full.md`,
      21KB, real PDF) defines in §1.1: "an arithmetic progression of length M is
      a sequence of points P₁,…,P_M in E(Q) whose x-coordinates… form a
      non-trivial arithmetic progression in Q." The Robertson reduction requires
      x(2Qᵢ) in AP. Since 2Qᵢ ∈ E(Q), set Pᵢ = 2Qᵢ — GFP bounds every AP in
      E(Q), doubled points included. The approach is NOT refuted on this ground.
      However, C is ineffective (from Rémond's quantitative Mordell–Lang +
      Gao–Ge–Kühne), so C^(r+1) is almost certainly >> 3. Record: GFP-bounds-x2P
      is RESOLVED (approach sound on definitions; ineffective constant prevents
      a contradiction). Update the uniformity-bremner-ap-bound thread with
      this resolution.
- [ ] **BLOCKER 2: Scholar to digest the re-downloaded Wu paper.** The file
      `research/sources/wu-non-invariance-brauer-manin.full.md` is now 78KB of
      real content.  Read it, replace the auto-generated digest in
      `research/summaries/wu-non-invariance-brauer-manin.md`, and either (a)
      confirm the claim `wu-bm-noninvariance-under-base-change` with the exact
      theorem statement and its conditional hypothesis (Stoll's conjecture),
      or (b) drop the claim and mark it as `status: dropped` with the reason.
- [ ] scholar: process the Garcia-Fritz-Pasten and Rome-Yamagishi papers into
      claim blocks. Garcia-Fritz-Pasten 2026 (arXiv:2604.04850) establishes
      Bremner's rank conjecture unconditionally (Theorem 1.8: AP length ≤
      C^(r+1), C ineffective) and gives a short proof that uniform-rank-boundedness
      ⇒ uniform-AP-boundedness (Theorem 1.2). Rome-Yamagishi 2024
      (arXiv:2406.09364) proves n×n magic squares of squares exist for all
      n ≥ 4 via the circle method — settles a conjecture of Várilly-Alvarado
      but does NOT address the 3×3 case.
- [ ] Extract the Garcia-Fritz-Pasten theorem into CONTEXT.md Established:
      Bremner's conjecture is proved — APs on elliptic curves have length
      bounded by C^(r+1) (C ineffective). The MSS requires an AP of length 3
      of doubled-point x-coordinates on the Robertson curve; GFP's definition
      covers these (Pᵢ = 2Qᵢ ∈ E(Q)). The bound does not give non-existence
      but the uniformity corollary plus a rank bound would turn the problem
      into a finite computation.
- [ ] Open thread `uniformity-bremner-ap-bound`: does Theorem 1.8, combined
      with a bound on the rank of the Robertson curve E: y² = x(x²−c²) when
      c = e², give a finite bound on the size of a minimal counterexample?
      The doubled-point question is settled: GFP §1.1 defines AP as x(Pᵢ)
      for Pᵢ ∈ E(Q), and 2Qᵢ ∈ E(Q), so no mismatch. Risk: C is ineffective,
      so C^(r+1) is not computable and almost certainly >> 3.
- [ ] Run the remaining phi programs (NOT the Faltings fibre route — that
      is settled and closed, genus 0 on all fibres). `code/phi_canonical_check.py`
      and `code/phi_identity_verify.py` verify the sin(4 arctan) form and Φ
      algebraic identities; run them and capture output.
- [ ] research: establish Bremner reduction, real computational bound,
      restricted classes, near-miss provenance; write research/ROOT.md.
- [ ] Establish ~1 structural impossibility lemma (extra-hypothesis partial
      result) and run it against the witness set.
- [ ] Formalise the Robertson reduction and the Garcia-Fritz-Pasten bound in
      Lean as they stabilise.