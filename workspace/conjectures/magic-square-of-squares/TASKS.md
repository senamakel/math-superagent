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
- [x] **BLOCKER 1 (part 1): Complete the truncated `robertson-elliptic-reduction`
      claim.** The statement now names the curve E: y² = x(x²−c²), the three
      points P₀, P₁, P₂ ∈ E(Q) whose x-coordinates in 2E(Q) are a−b, a, a+b,
      the AP condition x₂P₂−x₂P₁ = x₂P₁−x₂P₀, and that {X,X±c} all rational
      squares ⇔ (X,Y) ∈ 2E(Q). Traced through Bremner 1999 eqs. (2)–(4)
      verbatim; claim block updated and `research/CLAIMS.md` re-derived.
- [ ] **BLOCKER 1 (part 2): Verify the completed reduction against the paper
      and check non-degeneracy for the Garcia-Fritz–Pasten application.**
      The GFP theorem bounds AP length for points on an elliptic curve; the
      MSS AP is of *x-coordinates of doubled points* (x₂Pᵢ), not of Pᵢ
      themselves. Scholar: confirm that the GFP theorem's hypotheses
      (non-degeneracy, no constant x-coordinate, distinctness) are satisfied
      for x-coordinates of points in 2E(Q) on E_e: y² = x(x²−e⁴). If
      x₂P = (x⁴+2c²x²+c⁴)/(4y²) and the theorem requires the curve's own
      x-coordinate, the AP condition may need restating in terms of the
      Kummer surface K = E/{±1} ∼= P¹.  Downgrade `robertson-elliptic-reduction`
      status from `proved` to `asserted` if this check reveals an unstated
      hypothesis or a mismatch between the AP in the theorem and the AP in
      the reduction.
- [ ] **BLOCKER 2: Scholar to digest the re-downloaded Wu paper.** The file
      `research/sources/wu-non-invariance-brauer-manin.full.md` is now 78KB of
      real content.  Read it, replace the auto-generated digest in
      `research/summaries/wu-non-invariance-brauer-manin.md`, and either (a)
      confirm the claim `wu-bm-noninvariance-under-base-change` with the exact
      theorem statement and its conditional hypothesis (Stoll's conjecture),
      or (b) drop the claim and mark it as `status: dropped` with the reason.
      The bearing on this problem: if BM obstruction behaviour is not
      invariant under base change, then the existence of MSS over Q(√3,√133)
      does not rule out a BM-obstruction proof over Q — but the Wu result is
      conditional on Stoll's conjecture and constructs artificial surfaces,
      not the K3 S of Bremner II.
- [ ] scholar: process the Garcia-Fritz-Pasten and Rome-Yamagishi papers into
      claim blocks. Garcia-Fritz-Pasten 2026 (arXiv:2604.04850) establishes
      Bremner's rank conjecture unconditionally (Theorem 1.8: AP length ≤
      C^(r+1)) and gives a short proof that uniform-rank-boundedness ⇒
      uniform-AP-boundedness (Theorem 1.2). Rome-Yamagishi 2024
      (arXiv:2406.09364) proves n×n magic squares of squares exist for all
      n ≥ 4 via the circle method — settles a conjecture of Várilly-Alvarado
      but does NOT address the 3×3 case.
- [ ] Extract the Garcia-Fritz-Pasten theorem into CONTEXT.md Established:
      Bremner's conjecture is proved — APs on elliptic curves have length
      bounded by C^(r+1). The MSS requires an AP of length 3 on the Robertson
      elliptic curve (three doubled-point x-coordinates); this does not
      directly give non-existence but bounds where to look. Also: the
      uniformity corollary plus a rank bound would turn the problem into a
      finite computation.
- [ ] Open thread `uniformity-bremner-ap-bound`: does Theorem 1.8, combined
      with a bound on the rank of the Robertson curve E: y² = x(x²−c²) when
      c = e² is the centre of an MSS, give a finite bound on the size of a
      minimal counterexample? If yes, the problem reduces to a finite
      computation (though possibly astronomically large).
- [ ] Run the remaining phi programs that are NOT the Faltings fibre route
      (which is settled and closed — genus 0 on all fibres, thread correctly
      dead). `code/phi_canonical_check.py` and `code/phi_identity_verify.py`
      verify the sin(4 arctan) form and the Φ algebraic identities; those
      results bear on the Φ-triple conjecture but are not blockers.
- [ ] research: establish Bremner reduction, real computational bound,
      restricted classes, near-miss provenance; write research/ROOT.md.
- [ ] Establish ~1 structural impossibility lemma (extra-hypothesis partial
      result) and run it against the witness set.
- [ ] Formalise the Robertson reduction and the Garcia-Fritz-Pasten bound in
      Lean as they stabilise.