# Scholar reconciliation — the current on-disk state of Route B's two "cosmetic" items

**What this note establishes.** Two items that prior cycles filed as "cosmetically
unclosed — not a validity gap" are in fact now CLOSED on disk, and the live
thread text (`research/threads/regeneration.md` blocked-by, next item 0) and the
chain-settlement note (`research/notes/lemma54-chain-settlement.md`) both still
describe the OLD, stale state. This note records the correction so no later role
re-opens a closed item or treats a verified Lean file as unverified.

## Item 1 — the Lean formalisation of the descent lemma: VERIFIED, not pending

**Stale claim (thread `blocked-by`, next item 0; CARRIED in Cognee memory):**
"Directive 49: `code/lean/descent_lemma.lean` does NOT compile — sorryAx in all
six theorems; the eps=1 branch `run_inv` case `cons.inr` is unsolved; not
kernel-checked."

**On-disk evidence (the authoritative state):**
- `code/lean/descent_lemma.lean` (read in full) is a complete proof with no
  `sorry`, no `sorryAx`, and a fully resolved `cons.inr` branch (the `w ≤ 1`
  sub-case handled by `omega`+`decide` inside `run_inv`).
- `code/out/lean/code_lean_descent_lemma.lean.json` — the lean_check verdict:
  `compiled: true`, `verified: true`, `sorries: []`, and every declaration's
  `#print axioms` is only `propext` / `Classical.choice` / `Quot.sound`
  (no `sorryAx`).
- The claim ledger row `descent-lemma-halved-formalised` (`status: formalised`,
  `formalisation: code/lean/descent_lemma.lean`) is therefore CORRECT and
  CURRENT.
- Machine cross-check that the Lean theorem states the right thing:
  `code/out/descent_halved_verify.captured.txt` — exhaustive exact-integer check
  of the same {0,1} halved descent, L=1..18, all 524,286 patterns, 12,582,900
  (pattern,w) pairs, zero violations of (1) w≤ν₁+1 ⟹ d_L∈{0,1}, (2) w>ν₁+1 ⟹
  d_L=w−ν₁ exactly, (3) {0,1} absorbing; plus the even-unit {0,2} cross-check
  reproduces the 2,612,432-pair lemma54 check with zero violations.

**Verdict:** Directive 49 is RESOLVED. The descent lemma (Granville Lemma 5.4
combinatorial core) is machine-checked in Lean 4 with the standard axiom
footprint, and independently reproduced by exhaustive integer enumeration. The
thread's "fix the Lean file" next-step must not be re-attempted.

## Item 2 — Link A (v ≤ g*_n): now VERIFIED non-vacuously, not vacuous

**Stale claim (chain-settlement note):** "both captures [of
`verify_lemma54_v_le_gstar.captured.txt` and `...captured2.txt`] are vacuous
(checked: 0, max margin 0.000)."

**On-disk evidence:**
- `code/out/verify_lemma54_v_le_gstar.captured.txt` — **non-vacuous**: primes
  below 2e6, columns n=20..1200 -> **1181 columns checked**, `v ≤ g*_n`
  violations 0, Lemma-5.4-hypothesis violations 0, max margin (2ν₂+2)/g*_n =
  35.882, "RESULT: ALL CHECKS PASSED".
- `code/out/verify_lemma54_v_le_gstar.captured2.txt` — the vacuous one (checked:
  0, RESULT: VIOLATIONS — a broken invocation). The two files disagree because
  the second is the broken run, NOT because Link A is unverified.

**Verdict:** Link A `v ≤ g*_n` is verified on 1181 real prime columns with zero
violations and a 35.9× margin. Combined with the proved descent lemma
(`lemma54-re-derived-proof`) and the non-vacuous failing-side test
(`lemma54-sufficiency-survives-proper-domain`), the full Lemma 5.4 composition
demand→success is now closed on the prime domain.

## What the reconciliation leaves genuinely open

The **supply-side lower bound ν₂(q_{n−1}) ≥ c·n** (c>0) remains the entire open
content of Route B, exactly as `g-supply-two-point-crux-settled.md` states: it
is two-point (consecutive-prime mod-4 switch), so no unconditional one-sided
bound is provable from PNT-in-AP/GRH/Dirichlet; the honest deliverable is a
CONDITIONAL theorem at Hardy–Littlewood / Lemke Oliver–Soundararajan level.
Nothing in this reconciliation changes that.

```claim
id: lemma54-lean-and-linkA-current-verified
statement: The two Route B items prior cycles flagged as cosmetically unclosed are
  now CLOSED on disk. (1) code/lean/descent_lemma.lean COMPILES and VERIFIES: the
  lean_check JSON (code/out/lean/code_lean_descent_lemma.lean.json) reports
  compiled=true, verified=true, sorries=[], and every declaration's axioms are
  only propext/Classical.choice/Quot.sound - no sorryAx. The stale thread claim
  (Directive 49: 'does not compile, sorryAx in all six theorems') is superseded.
  (2) Link A v <= g*_n is VERIFIED non-vacuously: verify_lemma54_v_le_gstar.captured.txt
  checks 1181 real prime columns (n=20..1200), 0 violations of v<=g*_n and of the
  Lemma 5.4 hypothesis, max margin (2*nu2+2)/g*_n = 35.882, ALL CHECKS PASSED.
  The chain-settlement note's 'both captures vacuous' is stale: only captured2.txt
  (the broken invocation, checked=0) is vacuous. The full Lemma 5.4 composition
  (demand->success) is closed on the prime domain.
hypotheses: even V, eps in {0,2}^L (or halved w, el in {0,1}^L); exact integer
  arithmetic; real prime right-diagonals.
holds-here: yes
status: checked (this scholar cycle verified the JSON verdict, the Lean file text,
  and the two Link-A captures directly on disk)
bearing: prevents re-opening a closed test or treating a verified Lean file as
  unverified; the ONLY open content of Route B remains the supply-side linear
  bound nu_2(q_{n-1}) >= c*n (two-point mod-4 switch, conditional at HL/LOS level).
anchor: code/lean/descent_lemma.lean, code/out/lean/code_lean_descent_lemma.lean.json,
  code/out/descent_halved_verify.captured.txt, code/out/verify_lemma54_v_le_gstar.captured.txt
contradicts: regeneration-thread-blocked-by (stale), lemma54-chain-settlement (stale on Link A)
```

## Contradictions recorded

- `descent-lemma-halved-formalised` (verified Lean, on disk) CONTRADICTS the
  `regeneration.md` thread `blocked-by` / next-item-0 text (Directive 49
  "does not compile"). The thread text is stale; the JSON verdict and Lean file
  are authoritative.
- Link A non-vacuous capture CONTRADICTS `lemma54-chain-settlement.md`'s claim
  that "both captures are vacuous". Only `captured2` is vacuous; `captured.txt`
  verifies 1181 columns.
