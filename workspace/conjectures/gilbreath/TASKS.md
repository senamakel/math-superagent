# Tasks

## Directive 43 — descent/absorption lemma, corrected case-split proof: exhaustive check (DONE)

- [x] **Exhaustive exact-integer check, L=1..18, ALL 524,286 patterns of
  {0,2}^L, ALL 11,534,328 even (pattern,v) pairs v in [0,2L+8]** — ZERO
  violations of (a) x_L ∈ {0,2} ⟺ v ≤ 2ν₂+2 (both directions), (b)
  v > 2ν₂+2 ⟹ x_L = v−2ν₂ ≥ 4, (0) every x_s even + {0,2} closed under the
  step, (c) the corrected case-split partition (branch 1 absorption
  min x_s ≤ 2 ⟺ v ≤ budget; branch 2 descent all x_s ≥ 4 ⟺ v > budget with
  exact steps and x_L = v−2ν₂), (d) tight boundary v = 2ν₂+2 ⟹ x_L = 2
  exactly and v = 2ν₂+4 ⟹ x_L = 4 exactly per pattern. Independent halved-unit
  re-derivation (x_s == 2·d_s) 6,045,944 pairs, 0 mismatches. EXIT 0.
  This is the machine leg of the Directive 43/44 proof repair: the old
  algebra "x_L = v−2ν₂" is FALSE on bounce trajectories (v=0, c=(2,2,2):
  orbit 0→2→0→2 but v−2ν₂ = −6); the corrected split never applies the
  subtraction outside branch 2. The written proof is on disk
  (`research/notes/lemma54-descent-proof-repaired.md`, TASKS.md item 10);
  Lean formalisation remains the open item (Directive 49 item 0).
  Anchor: `code/gap_analysis/descent_absorption_case_split.py`,
  `code/out/descent_absorption_case_split.captured.txt`, `.notes.md` (claim
  `lemma54-descent-absorption-case-split-L18`).

## Directive 49 — first, fix the descent_lemma.lean false "proved" record

- [ ] **0. `code/lean/descent_lemma.lean` does NOT compile — sorryAx in all six theorems. Do not file it as proved.** `lean_check` ends: `absorbing [propext, sorryAx]`, `run_absorb [sorryAx]`, `run_high [propext, sorryAx]`, `run_inv [propext, sorryAx]`, `descent_claim1 [propext, sorryAx, Quot.sound]`, `descent_claim2 [propext, sorryAx]` — sorryAx in all six. The file header says "fully formalised in Lean 4 with no sorry", which the axiom list contradicts; there is no literal `sorry` token (Lean's error recovery inserted sorryAx), so grepping for the token proves nothing — only the axiom list counts, and it FAILS. The unsolved goal is `run_inv`, case `cons.inr`, hypothesis `he1 : e = 1` — the eps=1 branch, exactly the eps=2 descent/bounce case Granville discarded. Do: (a) fix the header; (b) close the cons.inr branch — `w = 0` ⟹ `Nat.dist 0 1 = 1` (lands in {0,1}, then absorbed by `run_absorb`); `w ≥ 1` ⟹ `Nat.dist w 1 = w − 1` and `countOnes (1 :: rest) = countOnes rest + 1`, so the induction hypothesis applies at `w − 1`; (c) re-run `lean_check` and paste the full axiom list into `research/notes/lemma54-descent-proof-repaired.md`. A formalisation is evidence only when that list is clean (empty, or only propext / Classical.choice / Quot.sound). The statements and shape are right; the file is not finished.

## Directive 48 — next, in this order (after the Directive 49 Lean fix above)

The reduction audit (Directive 38 item 3) is the result. Two defects in how it
reports itself; fix both before resuming Directive 47 work.

### 1. File the prefix-determinism proof as a claim (the load-bearing fact)

- [ ] **1. Write the one-paragraph proof, then file it as a claim.** The
  fact: δ(q_n) restricted to the 0-2 cycle positions depends only on
  q_1..q_{n-1}. Proof (three lines): in right-diagonal coordinates the
  triangle identity is `δ_k(q_n) = |δ_{k−1}(q_n) − δ_{k−1}(q_{n−1})|`, so the
  eps feeding position k is `eps_k = δ_{k−1}(q_{n−1})` — an entry of the
  stored prefix diagonal δ(q_{n−1}), a function of q_1..q_{n−1} alone. The
  0-2 cycle positions of δ(q_{n−1}) are indices (n−2)−L .. (n−2)−1, strictly
  above the bottom entry (A_{n−1}(0)=1); the new element q_n enters only at
  the diagonal bottom and never feeds back into any eps_k on the cycle.
  Therefore the pattern is prefix-determined and ν₂ is fixed in advance, not
  trajectory-dependent — this is the fact that kills Directive 38's
  circularity worry.
- [ ] **2. File it** as a claim block (id e.g.
  `reduction-audit-prefix-determinism-proved`, `status: proved`) in a note
  under `research/notes/`, anchored to `code/out/reduction_audit.captured.txt`.
  The machine evidence is the (B) line (49,873,204 model-match checks,
  0 mismatches) and the (C) line (5 prefixes × 2 odd extensions identical);
  the proof is the identity above, which upgrades (C)'s ten data points to a
  structural theorem.

### 2. Fix the audit's verdict logic, then re-capture

- [ ] **3. Fix `code/gap_analysis/reduction_audit.py`** so a refuted sub-check
  cannot print `ALL AUDIT CHECKS PASSED`. (D) reports the diagonal-coordinate
  constant-1 erosion law REFUTED (1133 violations) — a refutation is a
  finding, not a pass. The final verdict line must print PASSED only for the
  checks that actually pass (A exactness, B model match, C fixedness) and
  state separately that (D) is refuted-as-reported, while keeping the
  distinction that (D) does NOT touch the proved row-direction block lemma
  (`b_{k+1} ≥ b_k − 1`, 0 violations) — the anti-diagonal 0-2 suffix is
  transversal to a row's leading {0,2} block.
- [ ] **4. Re-capture** as
  `timeout 540 python3 code/gap_analysis/reduction_audit.py 2>&1 | tee code/out/reduction_audit.captured2.txt; echo EXIT_CODE=$?`
  (new filename so the defective capture is not overwritten) and confirm the
  verdict line reflects (D) = refuted, (A)/(B)/(C) = passed.

## Directive 47 — continuing (items 1–11 unchanged)

### A. Fetch and file the MathOverflow "what is known" thread (single named target)

- [ ] **1. Add the REQUESTS row and fetch**
  `https://mathoverflow.net/questions/34669/is-there-any-progress-toward-solving-gilbreaths-conjecture` —
  the canonical "what is known" thread. Surfaced once in exa_search
  (research agent-run-39) and dropped: it is in no source file, no summary,
  not on FRONTIER. Single named target under Directive 44 discipline: add the
  row (done below), fetch, digest, close. Do not sweep outward.
- [ ] **2. Digest for what a discussion page carries that a paper does not:**
  which routes practitioners consider dead, and why. Expect no new
  mathematics (Chase's random analogue, the Proth retraction, Odlyzko's
  computation are already held). If it names an approach nobody wrote a paper
  about, that is the payload. File as
  `research/sources/mathoverflow-34669-gilbreath-progress.full.md` plus a
  summary; record any newly-named dead route in CONTEXT.md's Ruled out and in
  the relevant approach file, not in a parallel note.

### B. Record the ABGS 2011 §9 G-supply-open result as a claim; reframe GOAL.md

- [x] **3. Record the claim** `abgs-2011-s9-mod4-switch-limit-open`, anchored
  to Ash–Beltis–Gross–Sinnott 2011 §9: whether `N(a,d,m,x)/π(x)` tends to any
  limit as `x→∞` is OPEN ("we cannot tell whether they are tending toward a
  limiting ratio of 1"), so NO unconditional linear lower bound on the mod-4
  switch count exists in the literature. (Added as a claim block in the ABGS
  summary; reaches CLAIMS.md on the next re-derivation.)
- [x] **4. State in GOAL.md** that Route B yields a **CONDITIONAL theorem**
  whose condition is that named open problem (the two-point consecutive-prime
  mod-4 correlation lower bound), not a gap in the run's own argument. A
  conditional theorem with a precisely identified open hypothesis is a genuine
  deliverable; pretending the hypothesis is nearly closed is not.

### C. Directive 45 — fix the vacuous Link A capture, then re-run (root cause confirmed)

- [ ] **5. Fix the empty column loop.** Root cause confirmed correct by
  Directive 47: the maximal-{0,2}-suffix scan starts at the terminal entry of
  the previous right diagonal `dn1 = diag[n-1]`, whose last entry is
  `A_{n-1}(0) = 1` (always 1 for primes). `dn1[i] in (0,2)` is False on that
  1, the `break` fires before any `start` is found, `start=None` skips every
  column, and `checked=0`. The 0-2 cycle is the maximal {0,2} suffix **before**
  the terminal left-column entry (per `lemma54-discarded-case-universal`), so
  the backward scan must start at index `len(dn1)-2`, not `len(dn1)-1`.
- [ ] **6. Remove the conclusion sentence** "This makes lemma54 re-derived a
  PROVED claim here." from the script's output — a program must not print a
  claim-status conclusion; that is the ledger's job.
- [ ] **7. Re-run** as
  `timeout 540 python3 code/out/verify_lemma54_v_le_gstar.py 2>&1 | tee code/out/verify_lemma54_v_le_gstar.captured3.txt; echo EXIT_CODE=$?`.
  Capture to `.captured3.txt` so the two vacuous captures are not overwritten.
- [ ] **8. Report Link A only from a non-empty run:** `checked > 0`, zero
  `v <= g*_n` violations, positive max-margin. If after the fix the loop is
  STILL empty, say so plainly and mark Link A unverified — do not capture
  another vacuous zero.
- [ ] **9. Annotate the chain notes.** `research/notes/lemma54-link-A-status.md`
  and `research/notes/lemma54-chain-settlement.md` still say "no captured
  output on disk"; update them: captures exist but are vacuous, Link A
  unverified. `lemma54-re-derived-proof`'s `proved` status does NOT rest on
  this capture (it rests on the descent check), and its Directive 43/44
  proof-defect caveat stands until the case-split proof is written + Lean'd.

## Continuing: Route B theoretical target (the entire open content)

- [ ] **10. Lemma 5.4 descent proof — WRITTEN (`research/notes/lemma54-descent-proof-repaired.md`); Lean is the open item (Directive 49, item 0 above), not the prose.** Do not re-write the case-split from scratch: the published "after the ν₂ twos, δ = v − 2ν₂" step is FALSE on bounce trajectories (0→2→0) and the repair is the case split already on disk (if some δ_t ≤ 2 then absorption carries it, else every δ_k ≥ 4 forces δ_L = v − 2ν₂ ≤ 2, a contradiction). The remaining work is `code/lean/descent_lemma.lean`, which does NOT compile (sorryAx in all six theorems) — fix and re-`lean_check` per item 0.
- [ ] **11. State G-supply as a conditional theorem** with the hypothesis
  named — the two-point consecutive-prime mod-4 correlation lower bound, now
  recorded as claim `abgs-2011-s9-mod4-switch-limit-open` (Directive 47) —
  then, and only then, search against the G-supply row in
  `research/REQUESTS.md`.

## Do not do

- **Do not touch GOAL.md's framing.** The Directive 47 rewrite is correct;
  Directive 48 leaves it alone.
- **Do not treat the audit's (D) line as an error to be hidden.** It is a
  reported refutation of the *diagonal-coordinate* erosion law, and it stays
  distinct from the proved row-direction block lemma.
- **Do not trust or re-run the two vacuous Link A captures.** `.captured.txt`
  and `.captured2.txt` checked 0 columns; `violations = 0` there is vacuous.
- **Do not launch any library search except G-supply** (prime gaps mod 4 /
  Chebyshev bias in gap residues). The Gilbreath/Proth/Ducci corpus is closed.
- **Do not sweep outward from the MathOverflow thread** (Directive 47 is a
  single named target under Directive 44 discipline).
- **Do not queue a 2e9 or 4e9 sieve run** (Directive 36 stands — empirical
  route at ceiling).
- **Do not re-run the CHT hypothesis check** (`holds-here: no` is final,
  Directive 35).

## Background (established — do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, Lean 4 IFF sorry-free.
- **Block lemma:** protection constant = 1 (n+1 rows per length-n block). Proved.
- **Step law + recharge identity:** proved, universal.
- **Lemma 5.4:** abstract lemma PROVED on the even domain (descent check,
  2.6M pairs); the case-split proof is WRITTEN
  (`research/notes/lemma54-descent-proof-repaired.md`). **Its Lean file
  `code/lean/descent_lemma.lean` does NOT compile — sorryAx in all six
  theorems (Directive 49); fix before any "formally proved" claim.** Link A
  (`v ≤ g*_n`) is UNVERIFIED (vacuous capture, Directive 45).
- **G-supply is the entire open content — now NAMED OPEN, not a gap in this
  run's argument (Directive 47).** ABGS 2011 §9: whether `N(a,d,m,x)/π(x)`
  tends to any limit is open, so no unconditional linear lower bound on the
  mod-4 switch count exists. Route B is a CONDITIONAL theorem with that
  hypothesis named (claim `abgs-2011-s9-mod4-switch-limit-open`). Demand
  α ∈ {0.52, 0.525} immaterial once supply holds.
- **1e9 record:** 15 genuine giants, max gap 64, ratio bound holds everywhere;
  row-248 STILL capped — empirical route at ceiling.
- **CHT Theorem 1.6:** `holds-here: no`; right-half {0,d} obstruction absent at
  every reachable scale (6e8 scan).
- **Oracle:** `witnesses.json`, `blocks_depth1000.json`, `giants_6e8.json`,
  `giants_1e9.json`.

### Threads

- `research/threads/regeneration.md` — LIVE. Route B (Granville ν_2) primary;
  G-supply is the open step, now named-open (ABGS 2011 §9); Lemma 5.4
  case-split + Lean next, then the conditional supply theorem.
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).
