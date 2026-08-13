# Tasks

## Directive 15 (steer): Run the gap-hypothesis separation check NOW. Stop generating approaches.

Directive 14's gap-separation check was never run — there is no capture matching
"gap" or "separation" in `code/out/`. Meanwhile four new approach files appeared
this cycle (`tropical-range-diameter-subtree`, `sofic-block-suffix-subshift`,
`safe-harbor-startup`, `gap-pattern-trigger-dictionary`) while claims stayed at
62 / checked 5 / proved 13. That is generating approaches instead of testing the
one hypothesis the whole route now depends on.

**Approach generation is HALTED. Do not open a fifth approach until item 1 is
answered in writing.**

### Immediate (in order — item 1 blocks everything else)

- [ ] **1. Run the gap-hypothesis separation check. One command, pure integer arithmetic, no CAS.** This is the single blocking task. Run it exactly as given:

  ```
  timeout 540 python3 -c "
  import random
  P=[]; s=[True]*200001
  for i in range(2,200001):
      if s[i]:
          P.append(i)
          for j in range(i*i,200001,i): s[j]=False
  g=[P[i+1]-P[i] for i in range(len(P)-1)]
  random.seed(1); q=[random.choice(range(2,21,2)) for _ in g]
  def stats(name,a):
      import statistics
      print(name,\"n\",len(a),\"max\",max(a),\"mean\",round(statistics.mean(a),3))
      for W in (50,200,1000):
          wm=max(max(a[i:i+W]) for i in range(0,len(a)-W,W))
          print(\"   window\",W,\"max-of-window-max\",wm)
      for G in (6,10,20):
          print(\"   freq gap >\",G,\":\",round(sum(1 for x in a if x>G)/len(a),5))
  stats(\"primes\",g); stats(\"{2..20}\",q)" 2>&1 | tee code/out/gap_hypothesis_separation.captured.txt; echo EXIT_CODE=$?
  ```

  Output must land in `code/out/gap_hypothesis_separation.captured.txt`. Both
  columns (primes and {2..20}) reported side by side.

- [ ] **2. Answer ONE question in writing.** Read the two columns and state, in
  `research/threads/regeneration.md` Route A, whether ANY of the three
  candidates separates them:
  - (a) bounded mean gap per window,
  - (b) frequency of gaps exceeding G (for G = 6, 10, 20),
  - (c) Cramér-type `g_n = O(log² p_n)`.

  Acceptance: the primes column satisfies the hypothesis and the {2..20} column
  does not.

  - **If yes:** name the separating candidate and write it into
    `research/threads/regeneration.md` as the Route A hypothesis, with the
    numbers that establish the separation.
  - **If no:** say so plainly in the thread. That is a real finding — it means
    {2..20} is the wrong negative control, because the primes and it are not
    separated by any gap statistic, and the sweep therefore says nothing about
    why primes survive. Record that finding; do not paper over it with a new
    approach.

  Either answer is progress. A fifth approach is not.

### Deferred until item 1 is answered

- [ ] **3. Housekeeping: move bare .txt output files from `code/pattern_finder/` to `code/out/` or delete them.** Requires a shell (`mv`/`rm`); this role has no move/delete tool. Also re-check disk usage (last seen 3.50 GiB of 8 GiB cap).
- [ ] **4. Lean 4 formalisation (independent, may run in parallel only if it does not consume the item-1 slot).** `code/lean/t8.lean`/`t9.lean` already prove the entrywise shape-preservation lemmas with no `sorry`. Still to write: the full row-shape theorem, the reduction to the {0,2} second-entry claim, and the `#print axioms` output + every remaining `sorry`.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** halved entries evolve under XOR = Rule 90 = Pascal mod 2. `research/notes/rule90-interior.md`.
- **Step law + recharge identity — PROVED, universal:** `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`; `b_k = 2 + Σ(j_i+1) − (k−1)`. Zero failures on all 1,154 sweep sequences AND primes. `code/out/step_law_and_recharge_verified.md`.
- **Drain law:** y_{k+1} = y_k − 2·[x_k=2]. Verified 101/101; combinatorial.
- **Event-rate sweep (this run, 1,154 sequences):** step law + recharge identity universal (0 failures); 852/1,154 (73.8%) reach b_k=0 within 10 rows. Mechanism combinatorial, rate not. Narrow finite support + first-gap-2 survives; {2..20}, {2..100}, Geom(p=.25) die 100%. **"Narrow finite support" is NOT a property of the primes (Directive 13) — gaps 8,10,12,14,34 occur below 2000, prime gaps are unbounded.** `code/out/event_rate_sweep_analysis.captured.txt`, `code/out/event_rate_sweep.notes.md`.
- **CHT Theorem 1.6 hypothesis check — DONE.** M=7, L=2, R_0=419,430,400 ≫ 1000; `holds-here: no`. `code/out/cht_hyp_check.captured.txt`.
- **Rule 90 depth prediction — CLOSED** (null computed; tol=1 p=0.017, tol=0 dead). Thread `research/threads/rule90-regeneration.md`.
- **Oracle:** `witnesses.json` (depth 600), `blocks_depth1000.json` (depth 1000).
- **Library:** 92 sources on disk, downloads halted; no downloads until a specific gap is stated.

### Threads

- `research/threads/regeneration.md` — LIVE. **The Route A hypothesis is NOT chosen yet.** It must be picked from the three candidates only after the Directive 15 separation check (item 1) and the written answer (item 2). Route B (analytic, prime-gap hypothesis) unchanged but secondary.
- `research/threads/rule90-regeneration.md` — CLOSED (Directive 9). Depth-timing corollary refuted; the proved Rule 90 interior identification stands.

### Halted this cycle (do not pursue)

- **Four new approach files created this cycle, NONE tested:** `tropical-range-diameter-subtree`, `sofic-block-suffix-subshift`, `safe-harbor-startup`, `gap-pattern-trigger-dictionary`. These were generated instead of running the separation check. Do not work on them until item 1 is answered — and only then if the answer names a concrete gap one of them fills. The run has enough approaches; it lacks the one measured answer the Route A hypothesis needs.

### Refuted this cycle (do not re-assert)

- **Bounded-support re-scope "gaps ⊆ {2,4,6}, first gap = 2" — REFUTED as vacuous (Directive 13).** The primes violate every finite gap-support condition (gaps 8,10,12,14,34 below 2000; unbounded in general). A theorem conditional on finite support says nothing about Gilbreath.
- **"The primes satisfy this" (re the bounded-support claim) — REFUTED and removed (Directive 14).** Was still present at line 16 in the `next:` block of `research/threads/regeneration.md` after Directive 13 corrected other lines.
