# Scholar verification pass — audit verdict and c6 grounding

**Scope.** This pass re-read the two load-bearing full texts against their
digests, closed one arithmetic gap, and re-verified two open-task gates. The
library is phase-1 complete and already thoroughly digested by passes 1–8 +
consolidation passes; this added no new source (library is CLOSED) and no
re-derivation of already-checked content.

## Verified against full texts (no contradiction found)

1. **Makhnev 1988 (primary Russian full text), Theorem 2's 99-case mechanism.**
   Read the closing lemmas directly: Lemma 8, Lemma 9 ("each of A1, A2 contains
   exactly 6 triangles from [A2]", `12·10:20 = 6`), and the conclusion
   "Λ₀ is a strongly regular subgraph with parameters (33, 12, 1, 6)", plus the
   Theorem-2 (115,18,1,3) case `|Γ(Q)| = 15 + 15(18−16) = 195` contradicting
   v=115. The digest claims `makhnev1988-condstar-theorems` /
   `makhnev99-shorter-proof-integrality` (closure 39 pts, 12 inner + 20 outer
   triangles, subobject srg(33,12,1,6)) match the primary text verbatim.
   No misreading found.

2. **Reimbayev hexagon bound (arXiv:2409.10620), full §3.** Read the complete
   derivation: the c6 closed form, the relations (3)–(9) of Prop 5, the
   elimination to `n12 = F(n,k) + n3`, and the conclusion
   `n12 = (1/12) n k (k-2)(2k^2-21k+53) + n3`. Matches the digest that the
   identity (not merely a bound) holds, with the bound attained iff n3=0, and
   that n3=0 ⇒ (via Makhnev) nonexistence of srg(99,14,1,2).

## Gap closed this pass: Reimbayev's c6 Table-3 values (new exact grounding)

No capture previously reproduced the paper's c6 table. Hand-verified here in
exact integer arithmetic that the closed form reproduces the table:
(9,4)->-168, (99,14)->-47,288,703, (243,22)->-2,975,686,065 (the three
smallest rows, division exact over Z); two largest rows catalogued verbatim.
Note: `research/notes/scholar-reimbayev-c6-table-verified.md`, claim
`reimbayev-c6-table-verified`.

**Consequence (consistent with the standing directive-21 rule):** c6 and the
base hexagon term are pure (n,k) functions ⇒ parameter-determined ⇒ zero
separating power between 99 and the 9/243 controls. The whole order-6 counting
structure carries exactly ONE non-parameter-determined term, n3 — confirming
n3 is the sole live pivot and the c6/hexagon/count side is exact everywhere it
is used.

## Re-verified gates (already captured; their task rows read stale-open)

- **Two-graph descendant gate** (`code/out/verify_twograph_gate.captured.txt`):
  (99,14,1,2) has k=14 ≠ 2μ=4, descendant n = 2(2k−λ−μ) = 50 ≠ 99 ⇒ NOT a
  descendant of a *regular* two-graph; rook(3) is (k=4=2μ), BvLS is not. Line
  inert for 99 exactly as for 243. Task `verify-twograph-gate` marked open but
  is in fact answered/closable.
- **Incidence 2-rank determinism gate**
  (`code/out/incidence_prank_determinism.captured.txt`): 2-rank is NOT settled
  by parameters (naive spectral rule fails on doily and GQ(2,4)) but is
  UNPROVABLE as a 99-vs-243 separator (the only same-parameter pair,
  Shrikhande/rook(4), does not separate, and no second srg(99,14,1,2) exists to
  measure). Task `incidence-prank-parameter-determinism` marked open but
  answered/closable.

## No source contradictions found

Makhnev 1988 primary vs Reimbayev's citation of it: faithful (condition (*) =
n3=0 confirmed in the primary text). Reimbayev's c6 vs the run's independent
C6 counts: both give 4,980,690 for BvLS. The Bagchi/BN1988 μ=2 "grid" concern
is already resolved (`c6-resolved-no-bite`). No claim on disk contradicts
recalled memory.

## Sources that do not help (reconfirmed, unchanged from prior passes)

Paywalled/preview-only (Brouwer–Haemers chapter, Makhnev 2013, Bagchi 2006
original), a solved variant (Zehavi–Oliveira), SAT-limitation report with no
boundary (Keramatipour), wrong-download records (Bagchi, Behbahani–Lam-2011,
Östergård–Soicher arXiv-guess, Bondarenko–Radchenko), and the 9 OEIS rows: all
judged `does not help` with reasons recorded. Nothing re-read this pass changes
those verdicts.

## Durable finding to store (memory server down; record lives on disk)

Claim `reimbayev-c6-table-verified` (research/notes/scholar-reimbayev-c6-table
-verified.md): Reimbayev's c6 closed form reproduces his Table 3 exactly over
the integers for the three smallest family members; combined with the run's
independent exact C6 counts the load-bearing hexagon identity
n12 = (1/12)nk(k−2)(2k²−21k+53) + n3 is exact; c6/base-hexagon are
parameter-determined (no 99-vs-243 separating power), leaving n3 as the sole
live pivot. Store once Cognee recovers.
