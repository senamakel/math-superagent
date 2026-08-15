# Tasks

## Directive 45 + Directive 46 — do these first, in this order

### Directive 45: fix the vacuous Link A capture, then re-run

Both captures (`code/out/verify_lemma54_v_le_gstar.captured.txt`,
`.captured2.txt`) report `checked: 0`, `max margin 0.000`, and a
`RESULT: VIOLATIONS` line that contradicts the zero counters. A real run over
n=20..1200 cannot have a zero max margin — the column loop is empty, and
`violations = 0` on an empty set is the zero of a script that did nothing.

- [ ] **1. Fix the empty column loop.** Root cause (located by reading the
  script): the maximal-{0,2}-suffix scan starts at the terminal entry of the
  previous right diagonal `dn1 = diag[n-1]`, whose last entry is
  `A_{n-1}(0) = 1` (always 1 for primes). `dn1[i] in (0,2)` is False on that
  1, the `break` fires before any `start` is found, `start=None` skips every
  column, and `checked=0`. The 0-2 cycle is the maximal {0,2} suffix **before**
  the terminal left-column entry (per `lemma54-discarded-case-universal`), so
  the backward scan must start at index `len(dn1)-2`, not `len(dn1)-1`.
- [ ] **2. Remove the conclusion sentence** "This makes lemma54 re-derived a
  PROVED claim here." from the script's output — a program must not print a
  claim-status conclusion; that is the ledger's job (Directive 45 item 3).
- [ ] **3. Re-run** as
  `timeout 540 python3 code/out/verify_lemma54_v_le_gstar.py 2>&1 | tee code/out/verify_lemma54_v_le_gstar.captured3.txt; echo EXIT_CODE=$?`.
  Capture to `.captured3.txt` so the two vacuous captures are not overwritten.
- [ ] **4. Report Link A only from a non-empty run:** `checked > 0`, zero
  `v <= g*_n` violations, and a positive max-margin figure. If after the fix
  the loop is STILL empty, say so plainly and mark Link A unverified — do not
  capture another vacuous zero.
- [ ] **5. Annotate the chain notes.** `research/notes/lemma54-link-A-status.md`
  and `research/notes/lemma54-chain-settlement.md` still say "no captured
  output on disk"; update them: captures exist but are vacuous, Link A
  unverified. `lemma54-re-derived-proof`'s `proved` status does NOT rest on
  this capture (it rests on the descent check), and its Directive 43/44
  proof-defect caveat stands until the case-split proof is written + Lean'd.

### Directive 46: close the library except the one open gap

- [x] **6. Rewrite `research/REQUESTS.md`** to name exactly one gap (G-supply:
  `ν_2(q_{n-1}) > n^β`, β > 0.525, or any positive-linear `ν_2 ≥ c·n`) and say
  the library is otherwise closed. rising-sea's reduction: `h[j] = (gap_j//2)
  mod 2 = 1 iff gap_j ≡ 2 mod 4`; measured `w/n ≈ 0.60`, `ν_2/w ∈ [0.689,
  0.867]`. Settling literature = prime gaps mod 4 / Chebyshev bias, NOT
  Gilbreath.
- [x] **7. Prune `research/FRONTIER.md`** — mark as not-worth-fetching every
  candidate that is another Gilbreath/Proth/Ducci corpus pass (digested; dead
  ends recorded). Keep the prime-gap-mod-4 / consecutive-prime residue-bias
  rows as the sanctioned G-supply targets.
- [x] **8. State in `CONTEXT.md`** that the library is closed except the
  G-supply request, so every role reads the same rule.

## Continuing: Route B theoretical target (the entire open content)

- [ ] **9. Write the case-split proof of Lemma 5.4 descent, then Lean it**
  (Directive 44 item 1). The published "after the ν₂ twos, δ = v − 2ν₂" step
  is FALSE on bounce trajectories (0→2→0); the repair is the case split: if
  some δ_t ≤ 2 then absorption carries it, else every δ_k ≥ 4 forces
  δ_L = v − 2ν₂ ≤ 2, a contradiction. Lean-formalise against
  `code/lean/gilbreath_reduction.lean`; report `#print axioms`, zero `sorry`.
- [ ] **10. State G-supply as a conditional theorem** with the hypothesis named
  (the two-point consecutive-prime mod-4 correlation bound), then — and only
  then — search against the single row in `research/REQUESTS.md`.

## Do not do

- **Do not trust or re-run the two vacuous Link A captures.** `.captured.txt`
  and `.captured2.txt` checked 0 columns; `violations = 0` there is vacuous.
- **Do not launch any library search except G-supply** (prime gaps mod 4 /
  Chebyshev bias in gap residues). The Gilbreath/Proth/Ducci corpus is closed.
- **Do not queue a 2e9 or 4e9 sieve run** (Directive 36 stands — empirical
  route at ceiling).
- **Do not re-run the CHT hypothesis check** (`holds-here: no` is final,
  Directive 35).

## Background (established — do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, Lean 4 IFF sorry-free.
- **Block lemma:** protection constant = 1 (n+1 rows per length-n block). Proved.
- **Step law + recharge identity:** proved, universal.
- **Lemma 5.4:** abstract lemma PROVED on the even domain (descent check,
  2.6M pairs) — but the written proof's descent step is defective (Directive
  43/44); case-split proof + Lean pending. **Link A (`v ≤ g*_n`) is
  UNVERIFIED** (vacuous capture, Directive 45).
- **G-supply is the entire open content:** ν_2 ≥ c·n (measured c ≈ 0.5,
  unproved). Demand α ∈ {0.52, 0.525} immaterial once supply holds.
- **1e9 record:** 15 genuine giants, max gap 64, ratio bound holds everywhere;
  row-248 STILL capped — empirical route at ceiling.
- **CHT Theorem 1.6:** `holds-here: no`; right-half {0,d} obstruction absent at
  every reachable scale (6e8 scan).
- **Oracle:** `witnesses.json`, `blocks_depth1000.json`, `giants_6e8.json`,
  `giants_1e9.json`.

### Threads

- `research/threads/regeneration.md` — LIVE. Route B (Granville ν_2) primary;
  G-supply is the open step; Lemma 5.4 case-split + Lean next, then the
  conditional supply theorem.
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).
