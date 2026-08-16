# Scholar pass: the new material in research/ against the goal

Author: scholar. Date: this pass. Covers what the research agent's digestion pass
added to `research/` and whether it moves the goal.

## What this pass found

The reference library is **mature**: all 34 full texts under `research/sources/`
have matching digests under `research/summaries/`, and every digest carries its
claim blocks (38 ids, `grep '^id:'` confirms). So there is no undigested source
left to process. The genuinely new *work-product* in `research/` since the last
scholar synthesis is:

1. `research/notes/pivato_lucas_mixing_equivalence.md` — the Lucas-mixing bridge,
   with three claim blocks, answering (in its own telling) request
   `walsh-spectral-subset-b904`.
2. `research/notes/tool_builder_fold_rank_correction.md` — the decisive fold-rank
   correction (checked, n=2..20).
3. Two live threads (`averaged-mean-structure`, `finite-prefix-transfer`) and the
   backward skeletons (`supply-averaged-second-moment`, `weak-input-fold`,
   `supply-switch-equivalence`, `supply-from-endpoint-parity`).
4. Computed/checked claim blocks in `code/out/` (g_mean_linear_grounded,
   rw_hand_oracle_checked, avg_supply_note, negative_controls_...).

The librarian's and scholar_synthesis's geography/equivalence reads agree with the
framework in problem.md and GOAL.md: the parity barrier is real, the switch-
density reduction is a dead end, and the only live route is the fold `Φ` forcing
`wt(Φ_n h) ≥ c·n` from an input weaker than positive mod-4 switch density.

## What each new piece actually establishes

**Pivato–Yassawi 2006 Thm 7.1 (verified verbatim, lines 1690–1730).**
`Φ = 1+σ` on `(Z/p)^s` asymptotically randomizes `µ` (weak-* to Haar along a
Cesàro-density-one set of times) **iff** `µ` is Lucas mixing. `holds-here: yes`
for the fold — SUPPLY's `Φ_n` is the finite `1+σ` over Z/2, and Lucas' theorem is
the shared engine. Its bearing is that it names a *proved, sharp* ergodic
candidate for the weakest input (`Lucas mixing of the prime-gap-parity measure`),
which is exactly the shape GOAL priority 2 asks about. This is the single most
valuable piece of new material.

**But the closure flag below overreaches.** Thm 7.1 is ergodic: measures on
infinite configurations, weak-* convergence, density-one *times*. It does **not**
state the finite bound `wt(Φ_n h) ≥ c·n` for one fixed string `h` at one depth
`n`. The note's own "open step" paragraph concedes both halves (a) and (b) are
absent. So the theorem does not close the request.

**Fold-rank correction (checked, exact F₂, n=2..20).** Operative `Φ_n` is
`(n−2)×n`, rows `d=2..n−1`, rank `n−2`, nullity 2, ker = span(even-alt, odd-alt)
= the period-2 strings; all-ones is their XOR, in ker but not the whole ker.
`problem.md` fact 3 ("rank n−3, nullity 1, ker = span(all-ones)") is internally
inconsistent (for n columns, nullity 1 forces rank n−1) and matches no row-range
convention (d=0..n−1→rank n; d=1..n−1→rank n−1; d=2..n−1→rank n−2). Bearing: a
string gives `ν₂(n)=0` exactly when period-2 — sharpens dyadic collapse at period
2 to "exactly 0". This is a checked computation, the strongest evidence class the
pass produced, and it is durable memory.

**G-mean-linear / averaged form (checked).** `M(n) = (1/n)Σ_{k≤n} ν₂(k)/k`
rises 0.4394→0.4973 (n=100→4000) for the primes while Thue–Morse falls
0.2255→0.0641 and the all-ones kernel sits at 0.0000. So the averaged signal is
specific to the prime input (negative controls pass: all-ones and Thue–Morse do
NOT reproduce it). Measured, not proved — but it keeps the averaged form
(GOAL priority 1) alive and is the most promising numerical target.

**Rampersad–Wiebe caveat (verified).** RW's 2-regular run-length machinery does
**not** cover SUPPLY's fold: SUPPLY reads `h` by the submask-XOR zeta transform
(an involution), not RW's `Σ C(a·n+a·k, ...)C(n,k)` run-length transforms. So RW
is corroborating background for 2-regular *sums*, not a direct tool for the fold.
The related approach `diagonal-2regular-automaton` must be checked against this
before it is treated as applying.

## Sources reviewed and found not to help (so nobody re-reads them)

- `odlyzko_gilbreath` — a bibliography index page (leads list, not evidence);
  the canonical Odlyzko 1993 source is already digested elsewhere. No claim added.
- `granville_martin_prime_number_races` / `_prime_races` — two mirrors of the
  same paper, both retained intentionally; single-residue race context only,
  already captured by claim `gm-chebyshev-bias-positive-density`.

## Contradictions, and their resolution

- **Rank contradiction (live, now settled).** `problem.md` fact 3 says
  "rank n−3, nullity 1, ker = span(all-ones)". The checked computation
  (`fold-rank-is-n-2-nullity-2-alternating`) proves the operative matrix has rank
  n−2, nullity 2, ker = period-2 strings. The board's earlier `rising-sea` dead-end
  was a symptom of exactly this: it computed with the d=1..n−1 constructor (rank
  n−1), different from the operative rows d=2..n−1. Resolved: use the operative
  d=2..n−1 matrix; problem.md fact 3 must be read as superseded.
- **Request-closure overreach (the most valuable flag in this pass).**
  `research/notes/pivato_lucas_mixing_equivalence.md` carries
  `answers: walsh-spectral-subset-b904`, but the request asks for a *finite*
  `wt(Φ_n h) ≥ c·n` lower bound using Φ's submask structure for an input not
  complicated in the five refuted senses. Thm 7.1 is an ergodic iff-statement; it
  does not give that finite bound. The request should be treated as **still open**
  until the finite-prefix transfer is supplied. I will not edit the derived
  REQUESTS.md (not mine to write), but this finding is on the record and in memory.

## What the run still lacks (unchanged, restated precisely)

- The finite-prefix transfer: a quantitative `wt(Φ_n h) ≥ c·n` (all n ≥ N₀ or on a
  density-1 set) from an arithmetic input on the prime-gap-parity prefix — the
  central gap, confirmed still open.
- Whether the prime-gap-parity empirical measure is Lucas mixing (not in any
  source; the arithmetic heart).
- A Walsh-spectral / submask-window variance bound on `h` (request
  `walsh-spectral-subset-b904`), the finite-input route to the transfer.

```claim
id: pivato-thm71-does-not-close-walsh-request
statement: Pivato-Yassawi 2006 Thm 7.1 (Phi = 1+sigma asymptotically randomizes mu iff mu is Lucas mixing) is an ergodic iff-statement about measures on infinite configurations converging weak-* along a density-one set of TIMES. It does not by itself give the finite lower bound wt(Phi_n h) >= c*n for one fixed prime-gap-parity string h at one depth n. Therefore the note pivato_lucas_mixing_equivalence carries an overreach when it sets answers: walsh-spectral-subset-b904: it names the sharp ergodic candidate but does not close the finite request, which additionally needs an absent finite-prefix transfer (both the prime-gap measure being Lucas mixing and quantitative stability).
hypotheses: the finite transfer (a) prime-gap empirical measure is Lucas mixing and (b) quantitative weak-* -> weight promotion are both absent from the library.
holds-here: yes as a caveat on an existing claim's bearing
status: sourced (Thm 7.1 verified verbatim at full text lines 1690-1730; the absence of the transfer is the note's own stated open step)
bearing: keeps request walsh-spectral-subset-b904 open; prevents the run treating the ergodic theorem as a proof of SUPPLY's finite bound.
anchor: research/sources/pivato_yassawi_sofic_randomization.full.md lines 1690-1730; research/notes/pivato_lucas_mixing_equivalence.md
```

## Durable memory written this pass

The Cognee store was empty (recall had failed 4× in-run). Writes now succeed. I
stored: the fold-rank correction, the Pivato–Yassawi Thm 7.1 statement with the
finite-transfer caveat, the parity-barrier/ABGS fact, and the Rampersad–Wiebe
does-not-cover-the-fold caveat. These are the first durable entries and should be
reached by later agents via recall_memory.
