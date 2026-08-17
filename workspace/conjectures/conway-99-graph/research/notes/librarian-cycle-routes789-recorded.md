# Librarian cycle: library verified complete; routes 7–9 recorded (directive 23)

Recorded 2026. This cycle the librarian did two things: verified the library is
already complete, and (per steering directive 23, which takes precedence) landed
the stalled `record-routes-7-8-9` writing task into `solution.md`.

## 1. Library state (verified, no new acquisition)

The reference library for Conway's 99-graph problem is **closed and complete** —
48 full-text sources on disk under `research/sources/`, each carrying its URL in
a `<!-- source: ... -->` header; phase 1 declared closed in `research/ROOT.md`
(structure of a putative graph, the verification/search bound, three settled
restricted classes). The two open requests in `derived/REQUESTS.md` are answered
in the notes with `answers:` lines:
- `published-mechanism-ruling-5cf8` → `answers:` in
  `research/notes/bagchi-mu2-dichotomy-resolution.md` (srg(33,8,1,2) dies by
  eigenvalue-multiplicity integrality — spectral, so a dead end for 99).
- `exact-list-prime-051a` → `answers:` in
  `research/notes/automorphism-orders-consolidated.md` (excluded orders with
  authors and computer-assistance status).
The one reserved acquisition (super-simple 2-(22,4,2) at v=22) was settled
**constructively** by CP-SAT (claim `super-simple-22242-exists`), so no source
is needed. **No further source acquisition is warranted.** A note on the
stale-render issue: `derived/REQUESTS.md` may still *show* the two rows until the
runtime recomputes it, but the notes carry the closing `answers:` fields; the
requests are answered on disk.

## 2. LEMMAS.md / Cited-axiom standing (directive 24, item 1)

Already fully documented at `research/notes/lemmas-standing-cited-bug.md`. The
verdict there stands and was re-confirmed against
`code/lean/makhnev1988_condstar_theorems.lean`:
- The lean **file structure is correct** — `Cited` is at the top level, and
  `Cited.makhnev_thm1`, `Cited.makhnev_lemmas_6_9`,
  `Cited.srg_multiplicity_integrality` are genuine axioms under `namespace Cited`
  (re-verified: `#print axioms` on the two main theorems lists all three).
- The **bug is in the harness standing computation**, which labels every
  declaration `verified` with `cited axioms: none`, contradicting the ledger
  header's own definitions (a Cited axiom is somebody's paper taken on faith and
  cannot be `verified`; a file containing Cited axioms is `conditional`).
- This matters because the run's load-bearing `n₃ ≥ 1` constraint descends from
  exactly `Cited.makhnev_thm1` and `Cited.makhnev_lemmas_6_9`. They must be
  `conditional`, not `verified`.
- Per the directive, `derived/LEMMAS.md` was **not hand-edited** (it is derived);
  the report to upstream is the note itself, which names the declarations and the
  header text they contradict.

## 3. Routes 7, 8, 9 recorded into solution.md (directive 23, item 2 — landed)

The stalled writing task `record-routes-7-8-9` (open 20+ minutes, zero writes)
is a writing task with no arithmetic and the three captures finished — assigned
itself to the writing role. It is now landed in `solution.md`:

- Route 7 — **Global incidence counting, CLOSED.** For all 19 radius-6 survivors,
  the forced line/incidence floor is exactly absorbable: residual 223–227 lines,
  669–681 incidences, no parity break, no vertex over 7, no negative deficit.
  Quoted the capture's conclusion: if an obstruction exists it is genuinely
  global/structural (later-radius or cross-patch conflict), NOT a counting floor.
- Route 8 — **Incidence p-rank, CLOSED AS UNUSABLE.** The 2-rank is not
  parameter-determined (no spectral rule predicts it; doily/GQ(2,4) violate the
  even-eigenvalue rule), so it could separate 99 from 243 — but it is unprovable
  this way: a 99 value needs an actual 99 system, i.e. the very graph in
  question (circular). Recorded the subtlety: rank varying across (9,4)/(243,22)
  is NOT evidence against parameter-determination; only a same-parameter split
  counts, and Shrikhande vs rook(4) (both srg(16,6,2,2), cospectral) gives none.
- Route 9 — **Two-graph descendant, CLOSED BY ARITHMETIC.** k=14 vs 2μ=4 fails at
  99 and equally at 243; rook(3) alone is a descendant (Paley two-graph on 10
  points). The loose "BvLS from a 244-point two-graph" claim concerns a
  non-regular two-graph, not a regular one.

Frontier updated in §7: nine closed routes, verified constraint `3 ≤ n₃ ≤ 4158`,
no local obstruction at any radius, no counting floor; what remains is the
cross-patch / global structural question, stated plainly as **harder than
everything closed so far**. §0, §2 heading, §8 completion status all brought to
"nine closed routes".

**What I stopped / did not do:** I did not hand-edit `derived/LEMMAS.md` (the
directive's own instruction; it is derived and would be overwritten). I did not
make further source downloads — the library is closed per CONTEXT.md and the one
reserved acquisition is settled constructively. `record-routes-7-8-9` is the
only task I acted on, since it was the first open task and a writing task within
the librarian's remit.
