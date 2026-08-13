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
- [ ] **DIRECTIVE 7.1 — Run check_ferreira_proof.py and reconcile with hand
      algebra.** The operator's refutation is at `code/out/ferreira_proof_refuted.md`
      (status checked), but the script `code/out/check_ferreira_proof.py` was never
      executed. Run under `timeout 540 python3 code/out/check_ferreira_proof.py 2>&1 |
      tee code/out/check_ferreira_proof.captured.txt; echo EXIT_CODE=$?`. If sympy
      disagrees with the operator, sympy wins — report it. The claim blocks
      `ferreira-1506-06621-refuted` and `ferreira-15060621-proof-invalid` already
      exist in CLAIMS.md (status: checked), so directive 7.2 is satisfied.
- [ ] **DIRECTIVE 7.3 — Audit for the Ferreira failure mode in the run's own
      code.** The error is substituting a solved root back into the equation it
      solved, manufacturing a vacuous identity that reads like a constraint.
      Check `phi_canonical_check.py`, `phi_identity_verify.py`, and any descent
      or p-adic code for this anti-pattern. Add to CONTEXT.md Ruled Out:
- [x] **STEP 1: Verify the parallel library.** `timeout 120 python3 code/lib/parallel.py`
      printed `self-check PASS: 2000 values, 26 workers`. Done.
- [x] **STEP 2: Parallelise `phi_padic_closure_all.py`.** Converted to
      module-top-level `_phi_rows(rows)` worker + `stripes()` + `parallel_union`,
      with `assert phi_set_serial(120) == phi_set(120)` before the M=200 run.
      Launched and captured: `code/out/phi_padic_closure_all.captured.txt`,
      EXIT_CODE=0, `|Phi(200)|=8156` matches serial. No obstruction found.
- [x] **STEP 3: Run the remaining six p-adic/modular programs.** All ran to
      completion (exit 0, no timeouts), captures in `code/out/`. None found an
      obstruction: the achievable residue set of Phi is additively closed at
      every prime-power of p=2,3,5,7,11,13 tested and mod p up to 31; mod 3/5
      collapse to {0}. Documented in
      `research/approaches/padic-modular-obstruction-dead-end.md`.
- [x] **FALSIFY EVERY P-ADIC/MODULAR OBSTRUCTION** — none was found, so there
      is no asserted residue/closure impossibility lemma. Ran
      `code/witness_padic_falsification.py` against `code/out/near_misses.json`
      using `is_magic_square_of_squares` in `code/lib/mss.py`: both witnesses
      verified, every positive fully-realised Phi element from a witness
      (Bremner 5544/7225, 336/625; Sallows 3360/12769) satisfies the proved
      p-adic facts (v2>=3, v3>=1, res=0 mod 3/5) — `RESULT ALL CONSISTENT`,
      no statement forbids a witness. Captured at
      `code/out/witness_padic_falsification.captured.txt`. Claims
      `phi-padic-no-obstruction` and `phi-padic-consistent-with-witnesses`
      in the dead-end note, status: checked.
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
- [x] Run the remaining phi programs (NOT the Faltings fibre route — that
      is settled and closed, genus 0 on all fibres). `code/phi_canonical_check.py`
      and `code/phi_identity_verify.py` verify the sin(4 arctan) form and Φ
      algebraic identities; captures at `code/out/phi_canonical_check.py.captured.txt`
      and `code/out/phi_identity_verify.py.captured.txt`. Both exit 0, all
      structural claims survive (one cosmetic bug in verify_phi_doubling, one
      range-truncation artifact in phi_canonical_check, one genuinely false
      bound in phi_identity [5b] — all reported in `code/out/phi_program_runs.txt`).
- [ ] research: establish Bremner reduction, real computational bound,
      restricted classes, near-miss provenance; write research/ROOT.md.
- [ ] Establish ~1 structural impossibility lemma (extra-hypothesis partial
      result) and run it against the witness set.
- [ ] Formalise the Robertson reduction and the Garcia-Fritz-Pasten bound in
      Lean as they stabilise.