# Tasks

- [x] Read problem.md, GOAL.md, AGENTS.md — the run targets the open 3x3 magic square of squares conjecture; deliverable is a genuine partial result, not a claim of resolution.
- [x] Spawn tool_builder (oracle + generator -> code/brute.py, code/out/near_misses.json) and research (ROOT.md) in parallel.
- [ ] tool_builder: verify is_magic_square_of_squares on hand-made magic square + confirm rejection of near-miss; search parametrisation for 7-square grids; write near_misses.json.
- [x] tool_builder: build code/lib/mss.py + code/check_near_misses.py (exact
      arithmetic): verifier, worked examples rerun fresh, both 7-square
      near-misses constructed+verified, incidence rank (rank 7, affine dim 3),
      (c,u,v) extraction, Pythagorean pairs; write code/out/near_misses.json
      with provenance for Sallows LS1 and Bremner's magic square; correct
      stale prose in code/out/oracle_note.md.
- [ ] research: establish Bremner reduction, real computational bound, restricted classes, near-miss provenance; write research/ROOT.md.
- [ ] Extract findings into CONTEXT.md Established + research/CLAIMS.md claim blocks with holds-here/status.
- [ ] Establish ~1 structural impossibility lemma (extra-hypothesis partial result) and run it against the witness set.
