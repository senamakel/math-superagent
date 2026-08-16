# rootdiff_identity.captured.txt — deleted, deliberately no capture

`code/out/rootdiff_identity.captured.txt` does **not** exist and must not be
recreated by re-running `code/rootdiff/verify_rootdiff_identity.py`.

- It was a **zero-byte failed redirection** (truncated on open; command timed
  out before anything flushed). Its mere existence read as the identity
  verified computationally when nothing ran — exactly the failure GOAL.md's
  capture rule names.
- Chosen fix: **directive 10's option 2** — the computational check is
  deliberately superseded by the proof in
  `research/notes/root-difference-identity-verified.md`, which proves both
  identities (H_i(f) = e_{n-i}(x-beta), R_i = prod H_i(f)(beta)) over any
  commutative ring with no division, strictly stronger than a sympy check at
  n=4,5,6, and names the only two failure modes a run could have caught
  (convention clash; dropped leading coefficient).
- A re-run **cannot terminate**: measured that the symbolic resultant
  Res_x(f,H_2) at n=5 does not finish within 550 s (and recurs in section B
  n=5,6 and section C2 n=6). See the research note.
- The capture file was physically deleted this run (`rm`). The live question —
  the char-p break of the collapse step — IS computationally verified by
  `code/rootdiff/verify_charp_break.py` (capture
  `code/out/charp_break.captured.txt`, ALL CHECKS PASSED 42/42).
