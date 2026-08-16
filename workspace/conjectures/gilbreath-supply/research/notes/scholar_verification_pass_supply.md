# Scholar digest & verification pass — the reference library against SUPPLY

Author: scholar. This pass re-read the key load-bearing sources against their
full texts and checked the library's digests for accuracy, contradictions, and
what each actually contributes to (or rules out for) the run's central
hypothesis: **can the fold Φ force `wt(Φ_n h) ≥ c·n` from an input weaker than
positive mod-4 switch density?**

## What this pass verified verbatim against the full text

| Source | Claim verified | Full-text location | Verdict |
| --- | --- | --- | --- |
| ABGS 2011 | Problem 1.1 (consecutive-pair residue frequency) "wide open, and cannot be treated using L-functions" | §1 p.401 lines 191-194 | exact |
| ABGS 2011 | §9: do the ordered pair classes occur asymptotically equally often? N/N'→1 is open | §9 lines 1394-1407 | exact |
| ABGS 2011 | §7 m=4 counts: (1,1)=16574,(1,3)=22521,(3,1)=22520,(3,3)=16715; switch 45041, equal 33289 | §7 lines 1308-1310 | exact — summary's corrected numbers confirmed |
| Pivato–Yassawi 2006 | Thm 7.1: Φ=1+σ randomizes µ ⟺ µ Lucas mixing | lines 1729-1732 | exact |
| Hofer 2025 | Lemma 1 (M1ᵀ diag((−1)^tᵢ) M1 = M2, tᵢ=s₂(i) mod 2 Thue–Morse); Cor 1 det = ∏(−1)^{s₂(i)} | lines 321-323, 394-400 | exact |
| ABGS Prop 4.1 (power-of-2 independence) | heuristic symmetry | (not directly re-spotted, consistent with summary) | consistent |

The digests are faithful. No misstatement was found in the load-bearing claims.

## The one bookkeeping gap worth closing

**`linearisation` is used as a claim id but no claim block gives it one.** It is
the theorem `ν₂(n) = wt(Φ_n h)` over F₂ (problem.md fact 1, imported as proved;
BACKWARD.md explicitly marks it "discharged on the strength of problem.md facts
1-2"). THREADS.md therefore lists two threads (`frontier-refocus`,
`literal-vs-fold-grounding`) as "resting on nothing recorded". This is not a
scientific gap — the linearisation is theorem-precise and matches the oracle —
but it is a provenance gap: a reader cannot trace the id to a block. Recommend
giving it a claim id (`linearisation-fold-weight`) anchored to problem.md fact 1
+ the oracle cross-check, so the threads' `rests-on` resolves.

## What each source actually contributes / rules out for the central hypothesis

- **ABGS 2011** — the parity-barrier fact: positive mod-4 switch density (the
  arithmetic input the reduction needs) is itself a named open problem,
  L-function-inaccessible. This is *why* attacking the fold directly is the only
  live route. VERIFIED.
- **LOS 2016** — conjectural: differing pairs (a,−a) exceed equal pairs (a,a) at
  every x≥5 (mod 4). If true, switch density not just positive but ≥ ~1/2. A
  *conjecture* (Hardy–Littlewood heuristic), not a theorem — must not be cited as
  proof. Complements ABGS without contradicting (ABGS §9 openness and LOS
  Conj 1.2 can both hold).
- **Lau 2024** — the strongest statement of the barrier: even *one* non-constant
  2-term pattern (1,3)/(3,1) mod 4 is not known to occur infinitely often. The
  switch side is beyond current methods. Confirms the reduction is a dead end.
- **Maynard 2016 Thm 3.3** — positive-density *equal*-residue clusters (the
  wrong direction). Strengthens door 2/3's refutation with density. Does NOT
  touch the switch side.
- **Shiu 2000 (expository)** — quantitative strings of congruent primes; refutes
  door 3 (arbitrarily long all-zero runs in h), equal side only.
- **Pivato–Yassawi 2006 Thm 7.1** — the named *weakest-input* candidate: h's
  empirical measure being Lucas mixing is the sharp ergodic condition for the
  fold's randomization. **Does not close the finite request** (ergodic measure
  statement at density-one *times*, not a bound on one fixed finite string).
  Together with the absent **finite-prefix transfer** this is the run's central
  open gap.
- **Takei 2017** — measure rigidity for Rule 90 (strong-mixing input → uniform
  along Cesàro means). Same finite-transfer caveat. Confirms the picture.
- **Rampersad–Wiebe 2023** — does NOT cover the submask-XOR fold (it analyses
  run-length transforms of different binomial-product sums). The earlier
  "RW is the fold Φ itself" gloss is retracted (`rw-not-the-submask-xor-fold`).
  Its `rw-average-nonlinear` (~1.207^r growth) is a caution that F₂-binomial sums
  need not grow linearly.
- **Meshulam, Donoho–Stark** — Walsh-side uncertainty on (Z/2)^n. Correct and
  exactly the right coordinate system, but *directional only*: they constrain
  Walsh-basis supports, not the co-domain `wt(Φ_n h)`, and their equality cases
  (subgroup indicators) are precisely the five-closed-doors low-weight inputs.
  They sharpen the obstruction, do not give the bound.
- **Bacher** — mod-2 Pascal determinant/LU structure of *square symmetric*
  matrices; does not directly give the value for the run's *rectangular offset*
  fold (holds-here unchecked).
- **Odlyzko 1993** — the {0,2}-reduction context; Gilbreath verified to 10^13;
  deep-large cells rare & gap-driven. Situates ν₂; does not give SUPPLY.

## Contradictions found / confirmed

- **Kernel correction (live, resolved):** operative Φ_n rank n−2, nullity 2,
  ker = span(even-alt, odd-alt), all-ones in ker. The inherited "rank n−3,
  nullity 1, ker = span(all-ones)" is wrong (fits no row-range). Closed door 1
  (all-ones) survives untouched.
- **RW "is the fold" → corrected** to "does not cover the fold". Recorded.
- **ABGS vs LOS** — not a factual contradiction (both are heuristic; §9 openness
  and Conj 1.2 coexist). Flagged as emphasis difference, resolved.
- **dip_sparsity_monotonic vacuous** (ran on the unfloored literal oracle) — to
  be deleted, not cited.

## What does not help (so nobody re-reads it)

- `citations_w*` (5 files) — reference lists, not evidence; their cited sources
  are already digested.
- `odlyzko_gilbreath` — bibliography index page.
- `granville_martin_prime_number_races` ×2 — mirrors of one paper, single-
  residue race context only (captured as `gm-chebyshev-bias-positive-density`).
- Shiu primary summary file is a **cookie-error stub** (Wiley) — the full text is
  NOT on disk; the Shiu input is carried via the expository copy, which is
  adequate for door 3 but should be flagged as not-primary where precision on
  hypotheses matters.

## Where this leaves the run

The library fully supports the framework in ROOT.md and GOAL.md:
- The switch-density reduction is a verified dead end (ABGS verbatim).
- The only live route is the fold forcing `wt(Φ_n h) ≥ c·n` from a weaker input.
- The central missing pieces remain: (a) the finite-prefix transfer (ergodic
  Lucas-mixing ⇒ finite weight), and (b) whether the prime-gap-parity empirical
  measure is Lucas mixing / a submask-window correlation or variance bound on h.
  Request `walsh-spectral-subset-b904` stays genuinely open.

Durable findings from this pass were stored with `remember_memory` (ABGS parity
barrier + counts; fold-rank correction; Pivato finite-transfer caveat; weakest-
input picture; averaged-form-with-discriminating-controls).

```claim
id: linearisation-fold-weight
statement: nu2(n) — the number of 2s in the floored maximal {0,2} suffix of the right
  diagonal of the absolute-difference triangle of the primes — equals wt(Phi_n h) over F2,
  h[j] = ((q_{j+1} - q_j)/2) mod 2, Phi_n the Pascal-mod-2 fold with entries
  C(k-1, j-(n-k)) mod 2, rows d = 2..n-1. This is problem.md fact 1 (imported as proved)
  and is independently consistent with the run's oracle (s_sos == s_direct on n=8..60)
  and with the excess identity 2*nu2(n) - (n-2) = -S(n), S(n) = sum_{d=2}^{n-1}(-1)^{T(n,d)}.
hypotheses: the floored convention k in [2, n-1] (the unfloored bottom-end reading is
  identically 0); the absolute-difference triangle of the primes.
holds-here: yes — this is the operative definition of nu2 throughout the run.
status: asserted (problem.md fact 1, imported as proved; oracle-consistent but no formal
  derivation on disk)
bearing: gives the linearisation a claim id so that threads frontier-refocus and
  literal-vs-fold-grounding can resolve their 'rests-on: linearisation' provenance gap.
anchor: problem.md fact 1; BACKWARD.md; code/out/oracle_fold_verify.py
```
