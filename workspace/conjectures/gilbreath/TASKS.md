# Tasks

## Directive 9 (steer): Depth pattern closed. Check rule90-interior-xor against the record. Bound the event rate.

### Immediate (in order)

- [ ] **1. Check `rule90-interior-xor` against `blocks_depth1000.json`.** The d-step XOR formula for the halved interior is proved over all 2^n patterns for n ≤ 13, but its edge-flip predictions have not been checked against the actual prime rows. At each row k where the block has length b_k, compute the halved edge value (A_k[b_k]/2) and compare with what the XOR formula predicts from the initial halved block pattern at the start of the current regime. Track: (a) how often the XOR formula correctly predicts edge=0 vs edge=2; (b) at rows where the edge flips (0→2 or 2→0), does the flip depth match the formula's prediction; (c) does the formula correctly predict when a stretch of all-2 entries (regenerated block) appears. This is the one rule90 claim that constrains regeneration directly — the other three are asserted-from-source and do not bear on the event rate. Run it single-threaded (reads blocks_depth1000.json, one pass; no triangle materialisation).

- [ ] **2. Bound the (2,4)-event rate from below — combinatorial Route A.**

  The step law holds on random non-prime arrays (3,521 rows, 610 events, zero failures), so the event mechanism is combinatorial. The conjecture: do (2,4)-events arrive fast enough that Σ (j_i + 1) never falls k−1 behind?

  **Route A — combinatorial.** Between events, the block erodes at exactly 1 per row. The intruder drains at rate 2 when edge=2, 0 when edge=0. The edge flips 0↔2 under Rule 90. Prove a worst-case bound on consecutive (edge=0, intruder=4) rows before the edge flips to 2. If max inter-event gap is G, event rate ≥ 1/G, and the recharge inequality is checkable.

  **Route B — analytic (secondary).** Assume a prime-gap hypothesis, derive event density. Must state how it beats Eppstein.

  **Deliverable:** a theorem "under hypothesis H, the (2,4)-event rate is at least r, and r suffices."

- [ ] **3. Record the random-array step law as its own claim.** Split the general-class finding (3,521 rows, 610 events, zero failures) into a distinct claim `step-law-combinatorial-general-class` with its hypotheses and the checked evidence. This is what Route A rests on.

### Supporting

- [ ] **4. Lean 4 formalisation.** Define the difference operator, prove shape preservation, reduce to {0,2} second-entry claim. Report `#print axioms` and every `sorry`. Independent of items 1–3.

- [ ] **5. Ledger hygiene.** Asserted 35, proved 14, checked 4. Three of the four rule90 claims are asserted from library-state.md rather than checked here — item 1 fixes the one that matters. Name any claims that were silently demoted and say whether deliberate.

### Closed (do not reopen)

- [x] **CHT Theorem 1.6 hypothesis check — DONE.** holds-here = no (R_0 = 419,430,400 ≫ 1000). Both claim copies updated. `code/out/cht_hyp_check.captured.txt`.
- [x] **Rule 90 depth prediction — CLOSED (Directive 9).** The null test is done and the thread's own bearing line says it: too weak at tol=1 to support a structural mechanism, dead at tol=0. Claim `rule90-relative-depth-null` recorded. No further tolerances, depths, or null variants. Thread `research/threads/rule90-regeneration.md` closed permanently.

### Background (established — do not re-derive or re-verify)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved.
- **Block lemma:** constant = 1 (N+1 rows per length-N block). Proved. `research/notes/block_lemma.md`.
- **Step law + recharge identity:** exact, verified independently depth 800, zero failures. `code/out/step_law_and_recharge_verified.md`. Also holds on random non-prime arrays — combinatorial.
- **Regeneration criterion:** b_{k+1} ≥ b_k ⟺ (A_k[b_k]==2 AND A_k[b_k+1]==4). Depth 1000, zero failures, 60/60.
- **Drain law:** y_{k+1} = y_k − 2·[x_k = 2]. Verified 101/101.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Minima record (depth 1000):** [13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263].
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000).
- **Library:** downloads halted. No more downloads without a stated gap.
- **Memory cap:** container touched 6.46 GiB of 8 GiB during the 26-worker null run. Bound worker counts on anything that materialises the depth-1000 triangle per worker; single-row streaming is safe.

### Threads

- `research/threads/regeneration.md` — bound the (2,4)-event rate from below. Combinatorial Route A first.
- `research/threads/rule90-regeneration.md` — **CLOSED (Directive 9).** The depth-pattern question is answered; no further work.