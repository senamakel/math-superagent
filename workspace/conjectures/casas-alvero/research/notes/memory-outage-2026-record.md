# Memory-write outage 2026-08 — what will be re-stored once the server recovers

The Cognee memory server was down for writes this cycle (5 consecutive
`remember_memory` calls failed: "the memory server cannot index right now …
its own health report did not answer within 8 seconds"). Passages recalled
fine; indexing was refused so nothing would be accepted-and-dropped silently.
Prior notes (librarian-cycle-2026-gap-reconfirm-and-integrity.md,
scholar-digest-assessment.md) already recorded the same outage.

Nothing is lost: every durable finding this cycle is on disk in the note,
which is the canonical store. When the server recovers, re-store these two
findings (see AGENTS rule: durable recall lives in Cognee; a statement nobody
can trace is worth less than no statement):

1. **resultant-monomials-d4-i3-hand-verified** (text in
   research/notes/resultant-monomials-d4-hand-verified.md):
   R_3 = Res_x(f,H_3) = -3a_1^4+16a_1^2a_2-64a_1a_3 at d=4; unique pure power
   a_1^4 coeff -3 = (-1)^(d-i)(C(d,i)-1)^(d-i); unique degree-2 monomial a_1a_3
   coeff -64 = C(4,3)^3; the pure-power coefficient is the closed binomial
   value sum_k(-1)^k C(d-i,k) C(d,i)^k = (1-C(d,i))^(d-i) for every d,i by
   binomial theorem. Upgrades resultant-monomials to checked at (4,3).

2. **claim-ledger contradicts-field hygiene** (text in this note):
   `contradicts:` must name one real claim id; prose there gets tokenised into
   phantom ids. Fixed the smallest-open-degree-20-vs-2020-survey block
   (device the 5 dangling rows). CLAIMS.md went 108->103 entries.

## Still queued for an executor (not claimed here)
- Full R_1 = Res(f,f') and R_2 = Res(f,H_2) expansions at d=4 to confirm
  "no OTHER pure power" uniqueness at i=1,2 — script
  code/scholar/verify_monomial_structure.py written, no capture yet.
- verify_deg6_witness.py (upgrade deg6-explicit-witness-gvb to checked).
