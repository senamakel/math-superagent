# Milestone 0

The workspace is legible and the char-p boundary is pinned down, so the run can
now attack the claimed proof.

## What this milestone establishes
- **Canonical oracle in place.** `code/lib/casas_alvero.py` decides the
  derivative-sharing hypothesis exactly over Q and F_p; the guard capture
  (`code/out/oracle_guard.captured.txt`) names lib.casas_alvero and ends
  ALL GUARDS PASSED.
- **The char-p boundary is verified twice, independently.** The sympy oracle
  flags x^{p+1}-x^p over F_p as a CA non-pure-power; the refuter's TPTP
  encoding independently recovered x^3+x^2 over F_2
  (`code/out/refute_char2.md`). Two formalisations agree on where CA breaks in
  char p, so an encoding that carries the Ghosh argument can be trusted to be
  faithful.
- **Open-degree coverage comparison corrected.** Two genuine discrepancies
  between the published open list and the settled-family complement:
  n=98 (covered by 2p^k, listed open) and n=96 (open via p=2 bad for degree 6,
  omitted). Re-derived in
  `research/patterns/open_degree_complement_and_sequences.md`.

## Next
The char-p stress test of the Ghosh proof's Brouwer-degree / Abel-Gontcharoff
step is now DONE (this run). Close-read of §4 (thread
`research/threads/ghosh-char0-step.md`, Findings section) located the char
dependence exactly in the proof of Proposition 4.3: (a) eq (4.18) uses the
leading coefficient −n of F(n,j_n,n) as a unit, so char ∤ n is required at the
step d = n; (b) Corollary 3.9's minimal-generator bound (the ℂ-only
Abel-Gontcharoff/Brouwer step) holds only for char p ∉ 𝒫(n). The argument
genuinely stops in char p (at d = n with p | n) and does not produce the false
char-p statement. Both the sympy oracle and the TPTP refuter agree on where CA
breaks in char p, so the guard on any future Ghosh-carrying encoding is
trusted.
