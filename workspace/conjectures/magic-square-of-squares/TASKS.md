# Tasks

- [x] Read problem.md, GOAL.md, AGENTS.md — the run targets the open 3x3 magic square of squares conjecture; deliverable is a genuine partial result, not a claim of resolution.
- [x] tool_builder: build code/lib/mss.py + code/check_near_misses.py (exact
      arithmetic): verifier, worked examples rerun fresh, both 7-square
      near-misses constructed+verified, incidence rank, (c,u,v) extraction,
      Pythagorean pairs; write code/out/near_misses.json with provenance for
      Sallows LS1 and Bremner's magic square.
- [x] Re-download Garcia-Fritz-Pasten and Rome-Yamagishi from PDF endpoints
      (both were abstract-page wrappers; now 21KB and 40KB — real papers).
- [ ] **RUN THE PHI PROGRAMS** — these exist and have never been executed:
      `code/out/phi_fibre_genus_run.py`, `code/out/verify_phi_doubling.py`,
      `code/phi_canonical_check.py`, `code/phi_identity_verify.py`. Run them
      and capture output before opening another approach. If `phi_fibre_genus_run.py`
      confirms genus 0 on all fibres (as expected from homogeneity), record it
      as further confirmation the Faltings fibre attack is dead. If any
      surprises, open a new thread.
- [ ] scholar: process the two newly-downloaded full papers into claim blocks.
      Garcia-Fritz-Pasten 2026 (arXiv:2604.04850) establishes Bremner's rank
      conjecture unconditionally (Theorem 1.8: AP length ≤ C^(r+1)) and gives
      a short proof that uniform-rank-boundedness ⇒ uniform-AP-boundedness
      (Theorem 1.2). Rome-Yamagishi 2024 (arXiv:2406.09364) proves n×n magic
      squares of squares exist for all n ≥ 4 via the circle method — settles
      a conjecture of Várilly-Alvarado but does NOT address the 3×3 case.
      Digest what each implies for this problem; file claim blocks.
- [ ] Extract the Garcia-Fritz-Pasten theorem into CONTEXT.md Established:
      Bremner's conjecture is proved — APs on elliptic curves have length
      bounded by C^(r+1). The MSS requires an AP of length 4 on the Robertson
      elliptic curve; this does not directly give non-existence but bounds
      where to look. Also: the uniformity corollary plus a rank bound would
      turn the problem into a finite computation. State the gap: what is the
      known rank of the Robertson curve for a putative MSS?
- [ ] Open thread `uniformity-bremner-ap-bound`: does Theorem 1.8, combined
      with a bound on the rank of the Robertson curve E: y² = x(x²-c²) when
      c = e² is the centre of an MSS, give a finite bound on the size of a
      minimal counterexample? If yes, the problem reduces to a finite
      computation (though possibly astronomically large).
- [ ] research: establish Bremner reduction, real computational bound,
      restricted classes, near-miss provenance; write research/ROOT.md.
- [ ] Establish ~1 structural impossibility lemma (extra-hypothesis partial
      result) and run it against the witness set.
- [ ] Formalise the Robertson reduction and the Garcia-Fritz-Pasten bound in
      Lean as they stabilise.