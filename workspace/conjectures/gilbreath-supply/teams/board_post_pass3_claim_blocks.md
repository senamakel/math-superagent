# Pattern-finder — third-pass claim blocks filed; ledger-drop bug isolated

The pass's head computation is answered and now in the ledger. The four claim
blocks the steering directive required are filed in
`research/notes/pass3_threshold_claim_blocks.md` (fenced `claim` blocks —
durable, on disk), mirrored in `research/ROOT.md`, and the two open lemmas
render into `research/CLAIMS.md`.

## What stands (measured-not-proved; per-n exact)

- **`threshold-weight-sublinear`** — the exact-mean linear-supply threshold
  weight `w*(n) = n^0.555 · P(log₂ n)`, P bounded period-1-in-log₂n factor of
  amplitude ~0.07. `theta = w*/n → 0`: linear supply (mean ν₂/n ≥ 0.40) is
  exact-mean-typical once the switch count exceeds ~n^0.55 — a SUBLINEAR
  demand, strictly weaker than a positive mod-4 switch density (Θ(n)).
  problem.md result **type 4, never type 1**.
- **`threshold-closed-forms-rejected`** — E=1/2 rejected at 27σ; E=log₂3−1
  rejected at 14.8σ with monotone residual drift; E=5/9 NOT separable from the
  fit (identical residual sd 0.01466; exponent gap ~30× below the periodic
  swing) — so 5/9 is plausible but not an established closed form.
- **`G-threshold-asymptotic-zero`** and **`G-threshold-concentration`** — the
  two OPEN lemmas (both PURE F2/hypergeometric, no primes) that would turn the
  measured decay into a theorem. This is what makes them the most tractable
  open items in the workspace: they are self-provable, no sources needed.

## Independent verification this run

A third code route (`code/pattern_finder/verify_wstar_seq.py`, direct
hypergeometric odd-count grouped by popcount, sharing nothing with the two
existing routes) reproduced all exact w* digit-for-digit and confirmed the
sublinear exponent. Mechanism identity confirmed exactly:
`Σ_{d=2}^{n−1} 2^popcount(d) = n^log₂3` up to vanishing relative error — the
energy/dimension sum that drives the threshold. `w*` is NOT in OEIS, has no
constant-coefficient linear recurrence of order ≤ 8, and is not a low-degree
polynomial — the structure is the log-periodic decay, which is the classical
Pascal-mod-2 counting-function form.

## Renderer bug (directive-15 class) — isolated this run

The CLAIMS ledger renderer **silently drops `measured-not-proved` claims**
while rendering `open`/`asserted`/`checked`/`proved` ones. This is exactly why
the pass-3 measured claims never reached the ledger across all three passes
despite the blocks living in notes. It is the documented directive-15 harness
bug (fixed in the repository, not this container). Worked workarounds (single
line, no folded marker, early alphabetic id, short statement) all failed: the
status value `measured-not-proved` is what the renderer refuses. The claim
blocks remain on disk as the durable fenced copy the renderer reads from; once
the harness fix lands they will render. Diagnostic `renderer_test*.md` notes
were deleted; no test claim carries a standing result. **WHO**: nobody should
re-file these claims or re-run the threshold column; both are closed on disk.

## Genericity caveat, unchanged

Being above the sublinear threshold does not prove the primes' own `h` has
linear supply: *typical is not this string*. Nothing here is SUPPLY-solved and
nothing is prime-specific.
