# Scholar digest — cycle two (post-research-agent)

## What changed this cycle

The reference library was already fully digested (scholar-digest-complete.md);
this cycle the scholar re-verified the claim anchors against the full texts
and worked the one internal contradiction the prior digest had missed: the
standing Phase-4 acceptance anchors.

## Verdicte on the library

Every `research/sources/*.full.md` has a statement-level note in
`research/summaries/`; there are no `Digest only` / `not read` templates left.
The only files still described as "not read" are the six citation-graph rows
(metadata-only by construction — they record that papers exist and how often
they are cited, which is precisely what they are for) and OEIS A344953
(peripheral catalogue entry, verdict recorded: does not help).

Claims anchors verified against the full texts this cycle:

- `governing-universal-euclidean` — fhq note carries the 6-component monoid
  `Po{cntu,cntr,sumi,sums,sqrs,prod}` with the exact merge rule and the
  merge/flip recursion; OI-wiki carries the plain (x=1) f/g/h second-moment
  recursion; LOJ138 carries `sum floor((px+r)/q)^k1 * x^k2`; AtCoder math.hpp
  carries the O(log) unweighted floor_sum + inv_mod/pow_mod bases. Real.
- `mechanical-word-digit-rule` — Perrin Lecture 2 (digit formula) +
  Perrin–Restivo (characteristic word) + exact in-container verification
  k=1..100 with slope F(n−2)/F(n). Real.
- `governing-sturmian` (slope 1/phi^2), `governing-factor-complexity` (k+1) —
  Perrin–Restivo Example 2 + Theorem 1, Berstel DLT'95, brute k=1..20. Real.
- `conjugate-christoffel-factor-sturmian` — Bugeaud–Reutenauer Introduction
  bridge theorem + Thm 7.3 (Ostrowski). Real.

Sources that do not help (recorded previously, re-confirmed): Hieronymi
decidability (tier-3; decidability != feasible evaluation), MathWorld rabbit
(convention trap), A344953 (peripheral), citation graphs (metadata), Berstel–
Karhumäki tutorial (background), AtCoder internal header (base case only).

## The important finding — the Phase-4 anchors are invalid

**New claim `phase4-anchors-invalid`** (research/notes/phase4-anchors-invalid.md).

The acceptance anchors `Psi(10^4) ≡ 16242174` and `Psi(10^6) ≡ 77578256`
(mod 101001001), used by tasks `implement-solution` / `solution-builder`, the
thread's next-step, and now the steering redirect's test (5), were computed by
`Psi_collapse` in code/solution.py. That function uses the Toeplitz identity
C(j,jp) = A(jp−j), which the SAME file's Phase 3 proves holds only at
k = F_n − 1 (exact Toeplitz-defect scan k=1..400: fully Toeplitz at
1,2,4,7,12,20,33,54,88,143,232,376 only). Neither 10^4 nor 10^6 is of the form
F_n − 1 (F_21−1 = 10945 ≠ 10000; F_31−1 = 1346268 ≠ 10^6), and P3-extra shows
the collapse disagrees with the valid direct method at general k
(k=200: collapse 64554455 vs direct 83031232). **Therefore both anchors are
out-of-domain products of a method proven wrong there, and must not be gated
on.** This includes the steering redirect's step (5), which inherits them.

**Corrected acceptance:** validate the O(log) monoid against the valid direct
method (psi_direct / mech_psi, == brute for k ≤ 400) at general-k values —
e.g. k = 1000 and k = 10000 computed by the O(k^2) direct sum — then run
k = 10^18 and confirm stability across two approximants. The method (Phase 2,
telescoped v, universal-Euclidean monoid) is unchanged; only its test values
were wrong.

## Contradiction ledger (current)

1. `steer-d2-literal-slope` (holds-here: no, literal slope F(n−1)/F(n) fails)
   vs `mechanical-word-digit-rule` (corrected slope F(n−2)/F(n) → 1/phi^2) —
   prior cycle, still open, but the corrected side is verified in-container.
2. `phase4-anchors-invalid` vs the standing CONTEXT/tasks/thread acceptance
   anchors and the steering redirect's step (5) — filed this cycle. The
   redirect's step (5) should be read as "reproduce valid general-k values",
   not the two written numbers.
3. Within source Hal-05026908: Thm 3.3 (density φ−1 ≈ 0.618) vs Def 2.3 /
   Prop 2.1 (density 1/φ² ≈ 0.382) — different words (complement convention);
   recorded in its summary, not a blocker.

## Memory server

Cognee `remember_memory` failed its health check again this cycle (6th
consecutive). Durable findings are on disk in this file, in
`research/notes/phase4-anchors-invalid.md` and in the thread file; they should
be relaunched into memory when the server recovers.

## Ledger tooling caveat

`derived/THREADS.md` cannot parse `research/threads/mechanical-word-floor-sum.md`
("has no thread block") even though the file carries a correctly formatted
fenced `thread` block — same class of re-derivation bug as REQUESTS.md noted
in scholar-digest-complete.md. On-disk file is authoritative and human-readable;
the ledger render is stale. Not blocking.

## Still missing

- Valid general-k residues for the acceptance test: k=1000, k=10000 must be
  computed by the O(k^2) direct method (psi_direct) — no execution tool in
  this environment; `code/out/verify/check_phase4_anchors.py` is staged for it.
- The O(log) universal-Euclidean monoid itself (the steering redirect's build
  task — solver role).