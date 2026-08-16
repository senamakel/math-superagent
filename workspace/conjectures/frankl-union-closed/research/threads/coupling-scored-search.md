# Scored program search on the coupling constant

## Dated section — 2025-xx (STEP 1–4, harness-inversion fix

The scorer `code/search/uc-coupling/score.py` suffered the harness-inversion bug
the thread predicted: it let the candidate supply the coupling atoms
(a1,a2,b1,b2) and scored `g(P,α)/Eh` at that one P — an UPPER bound on the
required `inf_P g/Eh` — so candidates climbed to 0.421992 (c0033, a=0.01) past
the proved ceiling t̂_max ≈ 0.3823455. This pass ran the four-step sequence.

### STEP 1 — the true inner-inf (new scorer, do not replace score.py yet)

Wrote `code/search/uc-coupling/inner_inf_scorer.py`: takes ONLY α from the
candidate, MINIMISES `g(P,α)/Eh` over the 4-parameter two-atom class internally,
certifying a rigorous LOWER bound on `inf_P g/Eh` via mpmath.iv interval
branch-and-bound over (a1,a2,b1,b2), with feasibility (a≤t<b, β∈(0,1], Eh>0),
time-boxed to <10 s.

**Verdict: NOT certifiable in 10 s.** At t=0.38234, α=0.035, the true
`inf_P g/Eh = 1.00000889` (Yu's minimizer a≈0.3300622, b2=1), but the margin
above 1 is only **8.89e-6**. The outward-rounded enclosure width near the
minimizer is ~21× the cell width (measured: lower bound stays below 1 until
cell width ≈4e-7), so cells must be bisected to ~20 levels in 4 dimensions
(the minimizer sits ON the box boundary b2=1, the boundary-collapse case the
crude intervals failed on before). The B&B hits the 10 s wall after only
~1100 splits (time verdict "inconclusive (time)"). This exactly reproduces the
`code/out/yugamma_global_sup.py` part2 failure (0 boxes certified near the
collapsed minimizer). **Per the directive's own rule — do not search the wrong
objective — the scored search STOPS here: the rigorous inner-inf is the
blocker.** The infimum is genuinely ≥1 (the theorem point is real); what is
infeasible is *certifying* it by crude interval B&B in the budget. A certificate
needs an exact/analytic inf or a tailored interval-arithmetic bound exploiting
the structure, not a generic 4-d B&B.

### STEP 2 — guards on score.py (independent of STEP 1)

(a) **Ceiling clamp**: if a certified SCORE would exceed
    t_hat_max = 0.3823455334 (+slack 1e-6), score.py now prints INVALID with the
    violating value instead of a SCORE line. This is correct because Γ̂(t) is
    proved non-increasing, so a score above t̂_max inside the two-atom class is
    definitionally a missing-inf artifact, not a certificate.
(b) **Degenerate-atom bound** (`A_FLOOR = 0.1`, `B_MINUS_A_FLOOR = 0.1`): rejects
    the small-a hole c0033 exploits (a1=a2=b1=0.01). Yu's witness
    (a=0.3300622, b-a=0.3350) passes cleanly — the guard is chosen so the
    certified witness is not weakened.
(c) **INVALID self-test block** (`python3 score.py __selftest__`): re-checks
    every exploit point each call so the guards cannot regress. All c0000..c0033
    exploit points are confirmed rejected; Yu's witness stays admissible.
    SELF-TEST PASS.

### STEP 3 — re-calibration through the real harness contract

`python3 score.py candidates/c0009.py` (Yu's certified witness) still prints
**SCORE: 0.3823435642**, within the ceiling. A guard that broke calibration on
the certified witness would be a failed fix; this one did not.

### STEP 4 — re-score every candidate module

| id  | new result | reading |
|-----|------------|---------|
| c0000,c0001,c0002,c0005,c0006,c0007,c0009,c0016..c0023 | SCORE: 0.3823435642 | Yu witness block, believable |
| c0024 | INVALID (score 0.3823610 > ceiling) | missing-inf exploit |
| c0025 | INVALID (0.3823610 > ceiling) | exploit |
| c0026 | INVALID (0.3824280 > ceiling) | exploit |
| c0027 | INVALID (0.3825300 > ceiling) | exploit |
| c0028 | INVALID (0.3826835 > ceiling) | exploit |
| c0029 | INVALID (0.3828830 > ceiling) | exploit |
| c0030 | INVALID (0.3838000 > ceiling) | exploit |
| c0031 | INVALID (0.3859550 > ceiling) | exploit |
| c0032 | INVALID (0.3937600 > ceiling) | exploit |
| c0033 | INVALID (degenerate-atom a=0.01 < floor) | exploit |

Non-scored legacy rows: c0003, c0008 invoke the scorer's old positional-float
main() from inside the module (now rejected: "candidate module not found:
0.035"); c0004 is a diagnostic probe that prints "SCORE: 0.5" itself but exposes
no parameters and is independently rejected (INVALID: no readable parameters) —
confirms the harness does NOT trust candidate-emitted SCORE lines; c0010 is
malformed (IndentationError) and not a real candidate.

### Verdict

STEP 1's rigorous inner-inf is **NOT feasible in 10 s** (margin 8.9e-6, needs
~4e-7 cell width, B&B is exponential in the 4 dims and only ~1100 splits in
10 s). That infeasibility is the blocker that stops the scored search per the
directive: the harness cannot certify `inf_P g/Eh ≥ 1` and therefore cannot
certify any t. Only the Yu-witness plateau at 0.3823435642 (the genuinely
argmin coupling) survives the guards, and it is capped at t̂_max. Nothing in the
two-atom class certifies above t̂_max.

## Prior thread body

```thread
id: coupling-scored-search
question: (CLOSED BY DIRECTIVE 10) Does the original scored program search over
  Yu's two-atom coupling — where a candidate supplies (α,a1,a2,b1,b2) and the
  scorer evaluates g(P,α)/Eh at that ONE P — find anything above the proved
  ceiling t̂_max ≈ 0.38235?
status: dead
rests-on: yu-record-0-38234, yu-gamma-hat-nonincreasing, yu-gamma-half-is-phi-over-2
blocked-by: none — closed by operator directive 10, not reopened; directives 10+11 in force
next: |
  (0) [directive 10] CLOSED. Γ̂(t) = sup_α inf_P g/Eh is a sup-INF. A candidate
      supplying the INF variable P made the scorer evaluate g/Eh at one P, an
      UPPER bound on an infimum, so the harness maximised the wrong quantity.
      Every score above 0.3823455 (c0024–c0033 up to 0.421992) certifies
      nothing; the plateau at 0.3823435642 across c0009–c0023 was the real
      signal. Reopened only under the rebuilt scorer where the candidate
      proposes α alone and score.py minimises over P internally — see task
      fix-scorer-to-sup-inf.
  (1) [directive 11] The high scores are verifier exploits, not just a missing
      inf: c0033 (α=0.035, a1=a2=b1=0.01, b2=1.0) opens with the docstring
      "probing scorer inf-hole"; driving a to 0.01 widens the feasible t-range
      so the infimum is taken where the certificate is vacuously ≥1. The scorer
      admits a degenerate-atom hole at small a, caught by the t̂_max ceiling
      check. Fix belongs in score.py, never in a note asking the searcher not to
      try: harden score.py (above-ceiling ⇒ INVALID), add the degenerate-atom
      constraint (lower bound on b−a or a), add every exploit to the INVALID
      self-test block, re-calibrate on Yu's witness, re-score every candidate on
      disk. None of c0028–c0033 may reach CLAIMS.md, solution.md, or a board
      post.
```

## Why this direction (now closed)

The prior `coupling-half` thread resolved the *push to c = 1/2* as outcome (b):
Yu's Prop-1 two-atom relaxation reproduces 0.38234 but its certificate Γ̂(t) is
proved non-increasing in t, so it certifies nothing above t̂_max ≈ 0.38235.
The original scored search let a candidate supply the coupling atoms
(α, a1, a2, b1, b2) and scored `g(P,α)/Eh` at that single P. That inverted the
objective: Γ̂ is a sup over α of an inf over P, and a single P is an upper bound
on the inf, so the harness maximised the wrong quantity. The real signal was the
plateau at 0.3823435642 across c0009–c0023 (Yu's witness, the argmin); the climb
to 0.421992 (c0033, docstring "probing scorer inf-hole") past the proved ceiling
was the missing-inf signature plus a degenerate-atom hole at small a (driving a→0.01
widens the feasible t-range so the infimum is taken where the certificate is
vacuously ≥1), and it certifies nothing. This thread is closed by directive 10
and stayed closed by directive 11; the direction is reopened only with a scorer
that minimises over P internally and rejects any witness above t̂_max (task
`fix-scorer-to-sup-inf`).

## What would falsify it

A candidate inside Yu's two-atom class scoring strictly above t̂_max ≈ 0.38235
would falsify the proved Γ̂ non-increase (F_t ⊆ F_t′) — that is extraordinary and
must be re-checked against both the proof and the scorer before it is believed.
A score of 0.5 would prove Frankl only if the witness survives independent
re-verification; it is far more likely a scorer exploit. A score above 0.38234
that escapes the two-atom class (a richer coupling object) is the genuine way to
improve the frontier, and is a different, still-open question.

**The lesson (directive 10, permanent):** when the scored object is a sup-inf, a
candidate that supplies the INF variable turns the harness into a maximiser of
the wrong quantity, and scores climb smoothly and look like progress; only the
proved ceiling caught it. Keep a known-value rung on every scored search.

## Reconciliation with established results

- Γ̂(t) non-increasing (proved): within the two-atom class the plateau is
  t̂_max ≈ 0.3823455333667 (Cambie). The binding constraint is expected to be
  `t` itself (the ceiling a ≤ t), not a slack constraint inside the coupling.
- Γ̂(1/2) = φ/2 = 0.8090169943… at the α=0 collapse (proved exact); the global
  sup over α>0 is numerical-only (open in `yugamma-half-collapse`).
- The scorer's calibration target 0.38234 is hand-verified
  (`code/out/yu_optimization_verbatim.md`, Γ̂ = 1.000008892 vs paper 1.00000889).
