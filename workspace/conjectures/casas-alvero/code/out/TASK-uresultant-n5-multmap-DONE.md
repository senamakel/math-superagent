# Task uresultant-n5-multmap — DONE

Recorded 2026. The memory server was down (remember_memory / note_scratch both
returned "the memory server cannot index right now"), so the durable facts are
stored here in the file system and must be forwarded to Cognee on recovery.

## Result
Executed and captured: **ALL CHECKS PASSED**,
`code/out/uresultant_n5_multmap.captured.txt`, full writeup
`code/out/uresultant_n5_multmap.md`, script
`code/uresultant/multmap_n45_certificate.py`.

- n=4: multiplication-map char poly validated = pure power t^16 = 4^2
  (V(I)={0} = CA on traceless slice, no lex), agreeing with the lex eliminant
  u^8 (nilpotency index; the run's index-vs-length distinction).
- n=5: coordinate nilpotency (a2^19, a3^13, a4^10, a5^1 all in I) + 0-dim
  vdim 125 = 5^3 certifies rad(I)=m_0, V(I)={0} = CA at degree 5, past the
  lex wall (lex does not close in 180s).
- New latent boundary: the 125x125 mult-map determinant is infeasible
  symbolically; coordinate nilpotency gives the same single-point certificate.

Marking task `uresultant-n5-multmap` done. Connect to the claims ledger and
Cognee on memory recovery.
