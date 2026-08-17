# Thread: mechanical-word / floor-sum route (directive 2), with slope correction

---
thread:
  question: Can Psi(k) for PE1006 be computed for k=10^18 in O(log) via the mechanical-word / geometrically weighted floor-sum, evaluated by the universal Euclidean (Chtholly / AtCoder floor_sum) algorithm?
  status: live
  rests-on: governing-sturmian, governing-factor-complexity, mechanical-word-digit-rule, governing-universal-euclidean
  blocked-by: none
  next: DIRECTIVE 6 ACCEPTANCE — run the evaluator (code/lib/ueuclid.py, directive-4 monoid, tests 1-3 vs direct loops) and then reproduce, in order: Psi(k) vs mech_psi for k=1..150, Psi(10)=10699667, Psi(10^4)=34432237 (10001 factors), Psi(10^6)=20938836 (1000001 factors), then k=10^18 with F(n)>k and stability across two approximants. The old anchors 16242174/77578256 are DISCARDED (directive 6 confirms phase4-anchors-invalid). The new anchors are asserted from outside the container — verify them in-container before they gate the O(log) run (k=10^4: check_phase4_anchors.py vs the valid direct method; k=10^6: window/residue route). Strictness: NextFib must be the least Fibonacci STRICTLY > k; lib/fibword.py next_fib is strict (bisect_right), so the trap is not live — a non-strict version is one Fibonacci short at k=F_n (k=3 then gives 10101 with 3 of 4 factors). Lean (checked .lean file) is the closing step, gated behind the executable reproducing the anchors.
---

## Steering redirect (this cycle) — build the universal-Euclidean primitive now

The operator directs: build the O(log) evaluator for the geometrically
weighted floor sum and its second moment ahead of further structural probing.
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
      are invalid (claim phase4-anchors-invalid) and are discarded. The new
      anchors, asserted from outside the container by the independent
      window/residue route, are Psi(10^4)=34432237 (count 10001) and
      Psi(10^6)=20938836 (count 1000001). Verify them in-container first,
      then match them exactly and in negligible time.
  Only after (5) passes, run k=10^18 with a Fibonacci approximant whose
  denominator exceeds 10^18, and confirm stability across two approximants.
- If the outer sum over the k+1 representatives resists one pass: the x_m
  are themselves the orbit frac(-m*a), so m is another floor-sum index —
  carry the joint state in the same monoid rather than looping over m.

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
  them with 34432237 (k=10^4) and 20938836 (k=10^6), asserted from outside
  the container and pending in-container verification. The prefix-bound
  strictness trap the directive warns about (NextFib must be strictly greater
  than k, else k=3 yields 10101 with 3 of 4 factors) is not live in
  `code/lib/fibword.py`: `next_fib` uses `bisect_right`.