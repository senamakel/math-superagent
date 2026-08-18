# Thread: mechanical-word / floor-sum route (directive 2), with slope correction

---
thread:
  question: Can Psi(k) for PE1006 be computed for k=10^18 in O(log) via the mechanical-word / geometrically weighted floor-sum, evaluated by the universal Euclidean (Chtholly / AtCoder floor_sum) algorithm?
  status: live
  rests-on: governing-sturmian, governing-factor-complexity, mechanical-word-digit-rule, governing-universal-euclidean
  blocked-by: none
  next: Convention question RESOLVED (refuter, this cycle): ueuclid is
    documented 1-indexed and matches the fhq/LOJ138/OI-wiki template; the
    0-indexed sum is the ue0 wrapper (verified 40/40 + 5/5 vs a literal
    0-indexed loop). The in-container __main__ capture
    (code/out/ueuclid_main.captured.txt) shows ALL MONOID TESTS PASSED —
    30/30 random vs ueuclid_direct, 30/30 S1-at-z=1 vs floor_sum, 6/6
    deterministic, 10^18 sanity dU=381966011250351898. The directive-6
    anchors are now VERIFIED IN-CONTAINER by the independent window/residue
    route (code/out/verify/window_residue_route.captured.txt: Psi(10^4)=
    34432237 count 10001, Psi(10^6)=20938836 count 1000001, k=1..60 ==
    brute). REMAINING: acceptance 4 — wire mech_psi formulation (B) through
    the monoid, pin the REDUCTION indexing (which power of 10 the j-th digit
    of the telescoped v carries) against mech_psi at SMALL k first; then
    acceptance 5 (anchors through the monoid); then k=10^18 under two
    Fibonacci approximants. Module on disk is final per directive 11; do NOT
    rebuild it.
    Full detail: research/notes/refuter-ueuclid-s1s2-false-alarm.md,
    code/refute/ueuclid-S1-index-refutation.md,
    code/out/verify/directive6-anchors-verified.md.
---

## Steering redirect (this cycle) — build the universal-Euclidean primitive now

The operator directs: build the O(log) evaluator for the geometrically
weighted floor sum and its second moment ahead of further structural probing.

## Scholar verification (this cycle)

The monoid composition formulas and the Euclidean recursion are now VERIFIED
against three full texts (fhq `[[universal-euclidean-geometric-weight-fhq.full]]`,
LOJ138 `[[loj138-universal-euclidean-floor-moments.full]]`, OI-wiki
`[[oi-wiki-universal-euclidean-floor-sum.full]]`), claim
`monoid-composition-formulas-verified` (proved). The S1/S2 compose rules are the
geometric-weight specialisation of LOJ138's general binomial rule. So the
solver implements the primitive from verified formulas, not an ad-hoc steer;
the acceptance tests 1-5 still gate it, but the correctness of the recursion
itself is no longer in question. Durable finding persisted on disk
(`research/notes/scholar-verified-monoid-primitive.md`) because the Cognee
memory server is down this cycle — store to memory when it recovers.
Toeplitz defects and extension-recurrence residues (pattern-hunt cycles 2-3)
are not on the critical path. Spec (verbatim paraphrase):

- Walk the lattice path of y = (p*t+q)/r for t = 1..n: one R step per unit of
  t, one U step per unit increase of floor(y). Take a monoid product over the
  path, split by the Euclidean recursion as in AtCoder floor_sum, so the path
  costs O(log) merges.
- A node carries, for its segment: dR, dU, w = z^dR with z the geometric ratio
  mod M; S0 = sum of z^t over its R steps; S1 = sum of z^t * floor(y);
  S2 = sum of z^t * floor(y)^2 — all relative to the segment origin, mod M.
- Compose left l with right r:
  dR = l.dR + r.dR; dU = l.dU + r.dU; w = l.w * r.w;
  S0 = l.S0 + l.w * r.S0;
  S1 = l.S1 + l.w * (r.S1 + l.dU * r.S0);
  S2 = l.S2 + l.w * (r.S2 + 2*l.dU*r.S1 + l.dU^2*r.S0).
  Identity: zeros with w = 1. The dU shifts carry floor values across a
  segment boundary — the one place this primitive goes wrong; test it hard.
- Acceptance tests, in order, none skipped:
  (1) S0 vs a direct loop on random p,q,r,n,z;
  (2) S1 vs plain floor_sum at z=1 and vs a direct loop at z != 1;
  (3) S2 vs a direct loop;
  (4) directive 2's telescoped v evaluated through the primitive vs
      code/mech/mech_psi.py on k=1..150 and vs Psi(10) = 10699667;
  (5) DIRECTIVE 6: the old anchors Psi(10^4)=16242174 / Psi(10^6)=77578256
      are invalid (claim phase4-anchors-invalid) and are discarded. The
      replacement anchors Psi(10^4)=34432237 (count 10001) and
      Psi(10^6)=20938836 (count 1000001) are now VERIFIED in-container by the
      independent window/residue route (code/out/verify/
      window_residue_route.captured.txt, claim
      directive6-anchors-verified-incontainer, status checked). Match them
      exactly and in negligible time through the monoid.
  Only after (5) passes, run k=10^18 with a Fibonacci approximant whose
  denominator exceeds 10^18, and confirm stability across two approximants.
- If the outer sum over the k+1 representatives resists one pass: the x_m
  are themselves the orbit frac(-m*a), so m is another floor-sum index —
  carry the joint state in the same monoid rather than looping over m.

## Scholar correction this cycle — the acceptance command must be the module's own __main__

`code/lib/ueuclid.py` is on disk but has NOT been run in-container (no pass numbers on
the record; the "20/20 ALL PASS" captured file is from an OLDER module version). The two
external harnesses in `code/out/` (`test_ueuclid.py`, `ueuclid_tests.py`) import names
(`identity`, `chain`, `pow_node`, `make_atoms`, `direct_node`) that DO NOT EXIST in the
current module, so running either raises ImportError and makes the primitive look broken.

**Run this, not the harnesses:**
```
cd /workspace && python3 code/lib/ueuclid.py
```
It runs acceptance 1–3 (30 random vs `ueuclid_direct`, S1 at z=1 vs plain floor_sum,
deterministic boundary cases, large-n sanity at 10^18) and prints `ALL MONOID TESTS
PASSED` if sound. Post that number, then proceed to acceptance 4 (telescoped v through
the monoid vs mech_psi k=1..150, Psi(10)=10699667), then the directive-6 anchors
34432237 / 20938836, then k=10^18 with two Fibonacci approximants. See
`research/notes/scholar-digest-ueuclid-api-and-position-anchor.md`.

## Status of the underlying claims

`governing-sturmian` (slope 1/phi^2, Perrin-Restivo + Berstel DLT'95 anchors),
`governing-factor-complexity` (k+1, Morse-Hedlund / Perrin-Restivo Thm 1,
brute-verified k=1..20), `mechanical-word-digit-rule` (arc-midpoint
construction, exact k=1..100 in-container), `governing-universal-euclidean`
(O(log) monoid, four anchors: fhq / OI-wiki / LOJ138 / AtCoder floor_sum) —
all anchors verified present this cycle against the full texts.

## What the sources now establish (see claim notes)

- The collapse identity C(j,jp)=A(jp-j) is valid exactly at k = F_n - 1; at
  general k the deviation from translation-invariance is bounded by 1 per cell
  (pattern-hunt cycle 3, exact k=1..400).
- `phase4-anchors-invalid`: the acceptance anchors 16242174 / 77578256 are
  invalid (out of the collapse domain); directive 6 confirms this and replaces
  them with 34432237 (k=10^4) and 20938836 (k=10^6), now VERIFIED in-container
  by the independent window/residue route (claim
  directive6-anchors-verified-incontainer). The prefix-bound
  strictness trap the directive warns about (NextFib must be strictly greater
  than k, else k=3 yields 10101 with 3 of 4 factors) is not live in
  `code/lib/fibword.py`: `next_fib` uses `bisect_right`.