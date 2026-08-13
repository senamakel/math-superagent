# Tasks

## Directive 13 (steer): Revert the bounded-gap-support re-scope — the primes do NOT satisfy it; Route A needs a concentration hypothesis

Directive 12 re-scoped Route A to a hypothesis "gaps ⊆ {2,4,6}, first gap = 2", claimed to be satisfied by the primes and violated by the dying sweep families. **That hypothesis is VACUOUS for Gilbreath: the primes do not satisfy it.** Counterexamples (directive): 89→97 gap 8, 113→127 gap 14, 139→149 gap 10, 181→191 gap 10, 199→211 gap 12. Distinct prime gaps below 2000: {1,2,4,6,8,10,12,14,16,18,20,22,24,34}; 98 gaps below 2000 lie outside {1,2,4,6}. Prime gaps are unbounded (elementary: gap ≥ n after n!+2). So NO bounded-support hypothesis holds for the primes, and a theorem conditional on finite support says nothing about Gilbreath.

**What the sweep licenses is weaker, and must be stated that way:** survival correlates with gap support being CONCENTRATED on small values, not contained in a finite set. The separating property must tolerate rare large gaps — the primes have a gap of 34 below 2000 and still survive.

### Immediate (in order)

- [ ] **1. Revert the bounded-support hypothesis.** Remove/replace "gaps ⊆ {2,4,6}, first gap = 2" as a prime-satisfied hypothesis in `research/threads/regeneration.md` and `CONTEXT.md`. Record it refuted for vacuity, not weakened, with the directive's counterexamples.

- [ ] **2. Verify the directive's gap facts mechanically.** Run the primes-below-2000 one-liner to reproduce the distinct-gap set and the first gaps > 6. This is an oracle check on the claim that the bounded-support hypothesis fails — do not take it on the directive's word.

- [ ] **3. Pick ONE concentration hypothesis, state it, check it numerically against BOTH the primes and {2..20}, THEN write it into the thread.** Candidates (the directive's list):
  - (a) bounded mean gap on every window;
  - (b) a bound on the frequency of gaps exceeding G;
  - (c) Cramér-type g_n = O(log² p_n).
  Acceptance criterion: the primes satisfy it (it must tolerate rare large gaps — gap 34 below 2000), and {2..20} (the sweep family that dies 100%) fails it. No bounded-support hypothesis may be re-asserted.

- [ ] **4. Route A under the chosen hypothesis.** Re-scope Route A: mechanism (step law, drain law, edge-flip) combinatorial; rate hypothesis = the concentration condition. State how it beats Eppstein 2011 (gap bounds alone do not suffice; add non-concentration).

- [ ] **5. Lean 4 formalisation (unchanged, runs in parallel).** Define the operator, prove (odd, even, even, ...) shape preservation, reduce to the {0,2} second-entry claim. Report `#print axioms` and every `sorry`.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal:** `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`; `b_k = 2 + Σ(j_i+1) − (k−1)`. Zero failures on all 1,154 sweep sequences AND primes. `code/out/step_law_and_recharge_verified.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified 101/101; combinatorial.
- **Event-rate sweep (this run, 1,154 sequences):** step law + recharge identity universal (0 failures); 852/1,154 (73.8%) reach b_k=0 within 10 rows. Mechanism combinatorial, rate not. Narrow finite support + first-gap-2 survives; {2..20}, {2..100}, Geom(p=.25) die 100%. **But "narrow finite support" is NOT a property of the primes (Directive 13).** `code/out/event_rate_sweep_analysis.captured.txt`, `code/out/event_rate_sweep.notes.md`.
- **CHT Theorem 1.6 hypothesis check — DONE.** M=7, L=2, R_0=419,430,400 ≫ 1000; `holds-here: no`. `code/out/cht_hyp_check.captured.txt`.
- **Rule 90 depth prediction — CLOSED** (null computed; tol=1 p=0.017, tol=0 dead). Thread `research/threads/rule90-regeneration.md`.
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000).
- **Library:** 92 sources on disk, downloads halted; no downloads until a specific gap is stated.
- **Lean 4 + Mathlib:** not yet started. Blocking: none.

### Threads

- `research/threads/regeneration.md` — LIVE. Route A re-scoped per Directive 13: mechanism combinatorial, rate hypothesis must be a CONCENTRATION condition tolerating rare large gaps (bounded-support form vacuous for primes). Route B (analytic, prime-gap hypothesis) unchanged.
- `research/threads/rule90-regeneration.md` — CLOSED (Directive 9). Depth-timing corollary refuted; the proved Rule 90 interior identification stands.

### Refuted this cycle (do not re-assert)

- **Bounded-support re-scope "gaps ⊆ {2,4,6}, first gap = 2" — REFUTED as vacuous (Directive 13).** The primes violate every finite gap-support condition (gaps 8,10,12,14,34 below 2000; unbounded in general). A theorem conditional on finite support says nothing about Gilbreath.
