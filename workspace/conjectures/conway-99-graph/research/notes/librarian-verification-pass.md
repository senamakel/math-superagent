# Librarian verification pass — library is complete against the open attack surface

Status: this cycle's librarian work was a *verification*, not an acquisition.
The library (49 full-text sources in `research/sources/`) is closed per the
steering directive, and no genuine acquisition gap remains. Recorded so a later
pass does not re-open acquisition against stale rows.

## 1. Both previously-open REQUESTS rows are answered on disk

The rendered `derived/REQUESTS.md` still carries two open rows, but each is
answered by a claim block with an `answers:` line in a note — the ledger simply
has not re-derived to drop them. Per the requests mechanism ("a request closes
when a note carries a claim block with `answers: <id>`"), both are closed:

- `published-mechanism-ruling-5cf8` (mechanism ruling out srg(33,8,1,2)):
  answered by claim `srg33-mechanism-answers-request` in
  `research/notes/bagchi-mu2-dichotomy-resolution.md` (carries
  `answers: published-mechanism-ruling-5cf8`). Mechanism =
  eigenvalue-multiplicity integrality (g numerator 2k−(v−1) = −16 not divisible
  by √(4k−7) = 5). Spectral => provably cannot transfer to v=99 (which passes
  integrality), so the 33 precedent is a dead end as a structural template.
- `exact-list-prime-051a` (excluded automorphism orders):
  answered in `research/notes/automorphism-orders-consolidated.md`
  (`answers: exact-list-prime-051a`) and cross-referenced in
  `research/notes/wilbrink-order11-makhnev.md`. Content: |G| | 2·3³·7·11
  (Makhnev–Minakova 2004); prime divisors of |G| ⊆ {2,3} (Behbahani–Lam 2011);
  if 7 | |G| then G ≅ Z₇, if 2 | |G| then |G| | 6 (Cesarz–Woldar 2025);
  no Z₆, S₃, Z₉, E₉ (Crnković–Maksimović 2020, full mechanism in library).

## 2. The sole reserved acquisition is legitimately dropped

The only acquisition the steer authorized after the library closed was
`serve-supersimple-22242-existence` — the Gronau–Mullin spectrum verdict for a
super-simple 2-(22,4,2) design (b=77, r=14, λ=2, no two blocks meeting in 3
points), the v=22 row of the super-simple (v,4,2) existence spectrum. That task
is DROPPED because the design was resolved constructively, so no source is
needed: CP-SAT OPTIMAL in 167.35s (7315 bools, 156131 branches), explicit
77-block certificate `code/out/coclique_lift_clean_design.txt`, independently
verified (degrees all 14, 231 pairs covered exactly twice, max triple overlap
1) — `code/out/coclique_lift_cpsat.captured.txt`. Construction beats citation.
Do not chase the literature for this.

## 3. The one open live line's gate is answered by computation, not citation

Task `incidence-prank-parameter-determinism` (thread `incidence-code`) asks
whether the incidence p-rank / 2-rank of the triangle geometry is
parameter-determined, which decides whether it can separate 99 from 243. This
is settled by `code/out/incidence_prank_determinism.captured.txt`:

- **rank_2(N)/rank_3(N) is NOT parameter-determined**: the naive mod-2 spectral
  rule (2-rank settled by the real eigenvalue multiplicities) FAILS on doily
  srg(15,6,1,3) (predicted 1, actual 5) and GQ(2,4) srg(27,10,1,5) (predicted
  1, actual 7). So the incidence code is a *possible* 99-vs-243 separator, and
  Assmus–Key's p-rank-of-STS variation carries through.
- **But it is unprovable as a 99 obstruction**: there is no second member of
  the (99,14,1,2) parameter class to measure. The available same-parameter
  pair, cospectral Shrikhande vs rook(4) at (16,6,2,2), does NOT separate
  (rank_2 16 = 16, both full). A 99 value would be settled only by an actual
  (99,14,1,2) system — the very object whose existence is open.

So this gate needs no source: the computation decides both facts. No literature
acquisition would move the line.

## 4. Conclusion

No acquisition gap remains. Do not re-open the library except against a NEW
phase-4 argument that names a source it is blocked on, stated precisely in
`derived/REQUESTS.md`. The two request rows above are resumption artifacts;
a future reader fixing them should simply confirm the `answers:` lines and let
the ledger re-derive.
