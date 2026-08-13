# Tasks

## Directive 12 (steer): Re-scope Route A — mechanism is combinatorial, rate is not

The event-rate sweep (1154 sequences, 852 deaths, 73.8%) contradicts the
regeneration thread's claim that Route A is "combinatorial, not about gaps"
with "no prime input." Both are true and about different things: the step law
and recharge identity hold universally (0 failures across all families) — the
mechanism IS combinatorial. But whether `Σ (j_i + 1) ≥ k−2` holds depends on
the event RATE, and the sweep shows the rate depends sharply on gap support:
{2..20} and Geom(p=.25) die 100%. A purely combinatorial bound on the event
rate would prove something false for those families.

**Resolution applied to `research/threads/regeneration.md`:** Route A re-scoped
to include a gap-support hypothesis (e.g. gaps ⊆ {2,4,6}, first gap = 2) that
the primes satisfy and the dying sweep families fail. The mechanism (step law,
drain law, edge-flip) is combinatorial; the rate hypothesis is about the input.

### Immediate (in order)

- [ ] **1. Find the gap-support hypothesis that separates primes from the dying families.** The sweep says it's not just "first gap = 2" — that helps {2,4} but {2..20} and Geom(p=.25) still die 100% with first gap forced to 2. Narrow support is the phase boundary: {2}, {2,4}, {2,4,6} survive (especially with f2); {2..20} and wider die. Extract the exact gap distribution from the sweep survivors vs dead — what property of the gap sequence makes the (2,4)-event rate sufficient? Check whether the primes' gap distribution (concentrated in {2,4,6} with ~72% at 2) falls definitively in the surviving regime. This is the content Eppstein 2011 already flags as necessary: gap bounds alone don't suffice, must add non-concentration. The sweep localises "non-concentration" to "gap support ⊆ {2,4,6} and skewed toward 2."

- [ ] **2. Run the inter-event gap analysis on the prime rows.** Extract from `blocks_depth1000.json`: inter-event gap distribution, jump-size distribution, cumulative recharge vs consumption at each event, worst-case inter-event gap, and whether the surplus trend is growing or shrinking. The data already exists — one program, run it, report the numbers. This is the measurement step the regeneration thread already lists as its first step.

- [ ] **3. Formalise the difference operator in Lean 4.** Define the operator, prove (odd, even, even, ...) shape preservation, reduce to {0,2} second-entry claim as a machine-checked lemma. Report `#print axioms` and every remaining `sorry`. Independent of items 1–2; can run in parallel.

- [ ] **4. Memory hygiene.** The container is at 3.38 GiB of 8 GiB. An OOM kill is silent. Before any large run, delete stale captures or compress the bigger output files. `code/out/event_rate_stats.jsonl` (378 KiB) and `code/out/commands.log` (511 KiB) are the largest — archive or truncate.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved and checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved, verified exhaustively. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** `research/notes/rule90-interior.md`. Halved entries evolve under XOR = Rule 90 = Pascal mod 2.
- **Regeneration criterion:** b_{k+1} ≥ b_k ⟺ (A_k[b_k]==2 AND A_k[b_k+1]==4). Zero failures to depth 1000, 60/60 events.
- **Step law and recharge identity — PROVED (this run):** `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`. Recharge: `b_k = 2 + Σ (j_i+1) − (k−1)`. Universal — holds on all 1154 sweep sequences (zero failures) and on the primes. `code/out/step_law_and_recharge_verified.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k = 2]. Verified 101/101 on primes; also combinatorial.
- **Event-rate sweep (this run, 1154 sequences, 3 batch depths):** step law + recharge identity universal (0 failures). 852/1154 (73.8%) reach b_k = 0, all within 10 rows. Phase boundary: {2}, {2,4}, {2,4,6} survive with first-gap-2; {2..20}, {2..100}, Geom(p=.25) die 100%. The mechanism is combinatorial; the event rate is not. `code/out/event_rate_sweep_analysis.captured.txt`, `code/out/event_rate_sweep.notes.md`.
- **CHT Theorem 1.6 hypothesis check — DONE.** M=7, L=2, R_0=419,430,400 ≫ 1000. `holds-here: no`. `code/out/cht_hyp_check.captured.txt`.
- **Rule 90 depth prediction — CLOSED.** tol=1 signal marginal (p=0.017), tol=0 dead. Thread `research/threads/rule90-regeneration.md` closed.
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000).
- **Library state:** 92 sources on disk, downloads halted. No more downloads until a specific gap is stated.
- **Lean 4 and Mathlib:** not yet started. Blocking: none.

### Threads

Two live threads:
- `research/threads/regeneration.md` — Route A re-scoped per Directive 12: mechanism is combinatorial, rate hypothesis must include gap-support condition. Route B (analytic, prime-gap hypothesis) unchanged.
- `research/threads/rule90-regeneration.md` — CLOSED per Directive 9. Null test done, tol=0 dead. The proved Rule 90 interior identification stands; the depth-timing corollary is refuted.

### Dead threads (do not reopen)

- `research/threads/event_rate_lower_bound.md` — sweep fix landed (Directive 11). Absorbed into regeneration thread.