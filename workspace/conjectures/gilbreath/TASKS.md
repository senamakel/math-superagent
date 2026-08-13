# Tasks

## Directive 14 (steer): Fix vacuous claim in regeneration thread, choose concentration hypothesis, housekeeping

Directive 13 corrected the bounded-support re-scope as vacuous for primes, but left
the old text at line 16 of `research/threads/regeneration.md`'s `next:` block saying
"The primes satisfy this" about `gaps ⊆ {2,4,6}, first gap = 2` — a claim Directive 13
already refuted. Directive 14 fixes that line, then demands a separation check before
any concentration hypothesis is written into the thread, and cleans up bare output
files littering `code/pattern_finder/`.

### Immediate (in order)

- [x] **1. Fix the vacuous claim in the `next:` block of `research/threads/regeneration.md`.** DONE. The old Route A line "The primes satisfy this" (re bounded-support) has been replaced with the concentration-hypothesis selection workflow from the directive: run the separation check first, pick from the three candidates, do not re-assert any bounded-support hypothesis.

- [ ] **2. Run the gap-hypothesis separation check (Directive 14).** Before writing any concentration hypothesis into the thread, compute for the primes and for a {2..20} random-gap sequence of the same length: max gap, mean gap, max gap over every window of length W for a few W, and the empirical frequency of gaps > G for G = 6, 10, 20. A hypothesis is only usable if the primes column satisfies it and the {2..20} column does not. If none of the three candidates (bounded mean gap per window, bound on frequency of gaps > G, Cramér g_n = O(log² p_n)) separates them, say so — that is a real finding and means the sweep families are the wrong negative controls.

  Command:
  ```
  timeout 540 python3 -c "
  P=[p for p in range(2,200000) if all(p%d for d in range(2,int(p**0.5)+1))]
  ..." 2>&1 | tee code/out/gap_hypothesis_separation.captured.txt; echo EXIT_CODE=$?
  ```

  Report both columns in the capture. Output: `code/out/gap_hypothesis_separation.captured.txt`.

- [ ] **3. Pick ONE concentration hypothesis from the three candidates, based on the separation check.** Acceptance criterion: the primes satisfy it (must tolerate rare large gaps — prime gaps are unbounded, gap 34 below 2000), and {2..20} fails it. Write it into `research/threads/regeneration.md` Route A.

- [ ] **4. Housekeeping: move bare .txt output files from `code/pattern_finder/` to `code/out/` or delete them.** The directory holds b.txt, bits.txt, c.txt, s_runs2.txt, e_bits.txt, and others — these are outputs, not code. A reader cannot tell which are inputs. Also re-check disk usage (at 3.50 GiB of 8 GiB cap).

- [ ] **5. Lean 4 formalisation (unchanged, runs in parallel).** Define the operator, prove (odd, even, even, ...) shape preservation, reduce to the {0,2} second-entry claim. Report `#print axioms` and every `sorry`.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal:** `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`; `b_k = 2 + Σ(j_i+1) − (k−1)`. Zero failures on all 1,154 sweep sequences AND primes. `code/out/step_law_and_recharge_verified.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified 101/101; combinatorial.
- **Event-rate sweep (this run, 1,154 sequences):** step law + recharge identity universal (0 failures); 852/1,154 (73.8%) reach b_k=0 within 10 rows. Mechanism combinatorial, rate not. Narrow finite support + first-gap-2 survives; {2..20}, {2..100}, Geom(p=.25) die 100%. **But "narrow finite support" is NOT a property of the primes (Directive 13) — gaps 8,10,12,14,34 occur below 2000, prime gaps are unbounded.** `code/out/event_rate_sweep_analysis.captured.txt`, `code/out/event_rate_sweep.notes.md`.
- **CHT Theorem 1.6 hypothesis check — DONE.** M=7, L=2, R_0=419,430,400 ≫ 1000; `holds-here: no`. `code/out/cht_hyp_check.captured.txt`.
- **Rule 90 depth prediction — CLOSED** (null computed; tol=1 p=0.017, tol=0 dead). Thread `research/threads/rule90-regeneration.md`.
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000).
- **Library:** 92 sources on disk, downloads halted; no downloads until a specific gap is stated.
- **Lean 4 + Mathlib:** not yet started. Blocking: none.

### Threads

- `research/threads/regeneration.md` — LIVE. Route A re-scoped per Directive 14: mechanism combinatorial, rate hypothesis must be a CONCENTRATION condition chosen after separation check against primes vs {2..20}. Route B (analytic, prime-gap hypothesis) unchanged.
- `research/threads/rule90-regeneration.md` — CLOSED (Directive 9). Depth-timing corollary refuted; the proved Rule 90 interior identification stands.

### Refuted this cycle (do not re-assert)

- **Bounded-support re-scope "gaps ⊆ {2,4,6}, first gap = 2" — REFUTED as vacuous (Directive 13).** The primes violate every finite gap-support condition (gaps 8,10,12,14,34 below 2000; unbounded in general). A theorem conditional on finite support says nothing about Gilbreath.
- **"The primes satisfy this" (re the bounded-support claim) — REFUTED and removed (Directive 14).** Was still present at line 16 in the `next:` block of `research/threads/regeneration.md` after Directive 13 corrected other lines.