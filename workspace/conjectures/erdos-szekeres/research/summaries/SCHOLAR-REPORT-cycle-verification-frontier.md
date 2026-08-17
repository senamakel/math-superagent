# Scholar report — verification cycle: frontier status, claim-status audit, discrepancies

What this scholar pass verified against full texts and captures, and the two
discrepancies it found. (Memory server was down for `remember_memory`; the two
durable findings that could not be stored are written here verbatim so a later
pass can push them to Cognee once the server recovers.)

## What this cycle verified (full texts read, claims confirmed against them)

1. **PointSAT (Krapivin–Przybocki–Heule, arXiv:2607.02958).** Theorem 1.1
   verified verbatim (line 29–31 of the HTML full text): the largest point set
   in R² with no 6-hole or 7-gon has **23** points, i.e. h(6,7)=24. The
   32-point no-7-gon experiment (lines 295–299): 200,000 abstract order-type
   solutions generated over 2191 core-hours, **zero realizable** — evidence
   only, the abstract space was not exhausted, so ES(7)=33 is neither proved
   nor refuted. Claims `kph-h67-24`, `kph-32-no7gon-no-realizable-found`,
   `kph-flippability-method` match the source. **Adjacent problem** (6-hole
   variant): keep out of Established as ES(7) progress.

2. **Dumitru (arXiv:2512.24061, Dec 2025).** Abstract verified: SAT encoding on
   triple-orientation variables + 4-set convexity criterion + convex-layer
   anchoring; UNSAT certificates only for **anchored subfamilies**; heavy-tailed
   runtime; ES(7)=33 open. Matches `dumitru-es7`.

3. **Koshelev–Koshka (arXiv:2604.20120, preprint).** Linear-subreduction method
   (fix abscissae, orientation constraints become LIA) and exact values
   h(6,≥2)=17, h(6,1)=18 asserted-by-source; adjacent Ramsey/bicolored values
   not ES(7) progress. Matches `kk-linear-subreduction`, `kk-h61-h62`,
   `kk-adjacent-not-esz7`.

4. **gsplit Phase 2 (steer 11) is DONE on disk.** `code/out/gsplit_phase2.captured.txt`
   carries the command line and `EXIT: 0`; it reproduces Phase 1 exactly
   (N(N−1) at N=8..16, zero missing/extra) and Phase 2 split counts **4 / 2 / 0**
   at n=5,6,7 on the validated rotating-line enumerator. Task
   `gsplit-enumeration-recheck` is `done`. Claim `gsplit-enum-completeness-and-n7-zero`
   (checked) is correctly anchored there.

5. **Allowable-sequence branch is closed with reasons.** The approaches ledger's
   row says "no reason recorded", but `research/approaches/allowable-sequence-circular-representation.md`
   §VERDICT and Cognee both carry the full adjudication: depth=block refuted
   (per-point reversal count over a half-period is constantly N−1 by the
   pair-reversal axiom), contiguous-block convexity false (fails both
   directions), correct criterion is first-or-last extreme in a projection
   order, and the replay bug (`[B,A,D,C]` not `[D,C,B,A]`) is identified. The
   empty reason line is a rendering artifact, not missing content. **Do not
   re-open or re-derive the depth/staircase or contiguous-block mechanisms.**

## Discrepancy 1 — `baek-balko-decomposable` status: proved vs asserted-by-source

The authoritative digest
(`research/summaries/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.md`)
records `baek-balko-decomposable` as **asserted-by-source**: "The proof of
Theorem 8 is omitted" in the held SoCG version (deferred to JCTA 2026). The
thread file, the weakened doc, and the librarian's probe note all agree. But
the derived `derived/CLAIMS.md` index (and CONTEXT.md Established — "Baek–Balko
split/decomposable result ... proved (SoCG 2025)") still say **proved**. The
claim-bearing note is the source of truth and is correct; the derived files are
stale and should re-render from it. **Action for the next writer of CONTEXT.md:
correct the Established line to "split threshold proved, decomposable-set
theorem asserted-by-source (proof omitted in SoCG 2025)"** — anything resting
on decomposable as proved is resting on an unverified source claim.

## Discrepancy 2 — stale head-of-queue row in CONTEXT.md Gaps

CONTEXT.md Gaps still lists "STEERING — head of queue (steer 11): re-capture
gsplit Phase 2 with provenance" as the next task, with the full command, but the
task ledger says `done` and the capture EXISTS with provenance (`EXIT: 0`,
4/2/0 reproduced). The head of queue is now the next task in the task ledger
(`es-nogon-scorer-and-problem`), not the gsplit re-capture. **Action: curator
updates the Gaps section** so no role re-runs a finished capture.

## Durable findings (could not reach `remember_memory`; push to Cognee later)

**Finding F1 — computational frontier for ES(7)=33 (2026).** PointSAT
(arXiv:2607.02958): h(6,7)=24; 32-point no-7-gon search over 200,000 abstract
order types found zero realizable (2191 core-hrs) — evidence, not proof. Dumitru
(arXiv:2512.24061): SAT encoding with 4-set convexity criterion + convex-layer
anchoring gives UNSAT only for anchored subfamilies. Koshelev–Koshka
(arXiv:2604.20120): linear-subreduction (fix abscissae → LIA); h(6,≥2)=17,
h(6,1)=18. All three, plus SMQH, fail to realize or refute a 32-point
no-convex-7-gon set; ES(7)=33 stands unproved; abstract order-type space is
dominated by unrealizable types (any upper-bound argument must enforce
realizability).

**Finding F2 — Baek–Balko SoCG 2025 status.** Split-k-gon threshold
ESsplit(k)=2^{k-2}+1 is proved-in-source (Lemmas 10/11 complete); the
decomposable-set theorem (Theorem 8) is asserted-by-source ("proof omitted",
JCTA deferred); the signotope analogue (every signotope on ≥2^{k-2}+1 vertices
contains a weak k-gon) is open and equivalent to a Goodman–Pollack conjecture —
a well-posed stronger target for the run's SAT arm after reproducing
ES(5)=9/ES(6)=17; Theorem 19 x-blow-ups give new 2^{k-2}-point no-convex-k-gon
families the es-nogon scorer should test.

## Sources that do not help (and why)

- **Conlon–Fox–He–Mubayi–Suk–Verstraete "Big line or big convex polygon"**
  (`cfhmsv-big-line-big-convex`) — generalizes to ℓ collinear members and to
  pseudoline convexity; its ℓ=3 case is real but the new bounds are asymptotic
  (2^{n+O(√(n log n))} type), so it does not bear on the exact 2^{n-2}+1
  constant. Recorded for context; not a tool for the exact conjecture.
- **Wikipedia / MathWorld / erdosproblems encyclopedic tier** — no mathematics
  the primaries do not establish more reliably. Pointers and drift-guards only.
- **MIS-DOWNLOAD stubs** (wrong physics/NLP PDFs fetched from guessed URLs) —
  already redirected; never cite as evidence.

## Postscript — steering directive executed: allowable-sequence closure confirmed on disk

The steering directive asked that the allowable-sequence adjudication be closed
into the approaches ledger, and noted the general failure mode (write refused →
content must fall back to a role holding the tool or to `write_document`, never
silently abandoned). Verified: the closure **is already on disk and the ledger is
current** — `research/approaches/allowable-sequence-circular-representation.md`
has `status: refuted` and a `killed-by` field carrying, verbatim in substance,
the full adjudication: (1) reversal-depth = block index is a structural
impossibility (constant per-point reversal count N−1 by the pair-reversal axiom;
observed 3,7,15,31 at n=4..7 against the block binomials); (2) contiguous-block/
staircase convexity false in both directions (n=6: 62096/64839 agreement, false
positives and negatives); and what survives — the exact circular sequence is
correctly constructible, the GP axioms hold on es_construct at n=4..7, the old
`[A] replay ok:False` was an encoder run-reversal bug now fixed (swap each tied
group's pairs independently), and the correct convexity-from-sequence criterion
is pointwise extreme-in-projection, agreeing with the exact oracle on every
|S|≥4 subset (n=6: 64839/64839). `read_ledger { ledger: approaches, id:
allowable-sequence-circular-representation }` confirms the reason renders under
"What closed, and why". **The context snapshot's "no reason recorded" row was
stale, not missing.** Do NOT re-open or re-derive depth=block or contiguous-block
convexity.

On the general failure mode: agent-run-79's `record_entry` refusal did not lose
the payload — its `write_document` of the `killed-by` field (or a prior write)
landed and re-derived the ledger. The directive's rule is now recorded here as
the workspace stand-in for Cognee (which is down): **when a role's write is
refused for lack of a tool, hand the content to a role that holds it or write it
to the workspace with `write_document`; never silently abandon it.** A later
pass should push this lesson to Cognee once the memory server recovers.

## What the run still lacks

- **ES(7)** open: no exact value beyond n=6, no general upper bound at the
  conjectured constant, no counterexample. Every current attack (SMQH, PointSAT,
  Dumitru, Koshelev–Koshka) stops at evidence.
- **Machine verification of the Koshelev–Koshka 17/18-point coordinate sets**
  and the PointSAT 23-point witness (h(6,7)) against `lib.es_geom` — cheap
  oracle checks that would upgrade those asserted computational claims.
- **Cognee storage** of F1/F2 (memory server down this cycle; workspace file is
  the stand-in).
- **CONTEXT.md corrections** for the two discrepancies above (Gaps head-of-queue;
  Established decomposable=asserted).