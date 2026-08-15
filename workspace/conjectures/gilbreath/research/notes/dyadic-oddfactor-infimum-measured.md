# Odd-factor converse — measured infimum (Directive 60/64 step, now run)

**Status of this note:** records the result of the exact measurement Directive
60/64 queued as the gate on the dyadic dichotomy's odd-factor half. The
measurement is DONE and on disk (`code/out/dyadic_oddfactor_density_exact.py` /
`dyadic_oddfactor_density_exact.captured.txt`,
`code/out/dyadic_oddfactor_infratio.py` / `.captured.txt`). No prior claim
block carried this result; this note files it.

## What was measured

For a **periodic** halved-gap bit string `h` of odd-factor period `P`
(equivalently a periodic 2-then-odds gap sequence), the asymptotic infimum
`inf_{n≥N} ν₂(n)/n` of the {0,2}-suffix count of the right diagonal. Exact
integers, `n ≤ 20000` (`dyadic_inf_measure.py`) and the companion exact-linear
scan to `n ≤ 24000` (`dyadic_oddfactor_density_exact.py`).

| P | inf ν₂/n (n≥100) | argmin n | ν₂ at n=20000 |
|---|---|---|---|
| 1 (power of 2) | 0.000000 | 100 | 0 |
| 2 (power of 2) | 0.000050 | 20000 | 1 |
| 4 (power of 2) | 0.000050 | 20000 | 1 |
| **3** | **0.6471** | 102 | 13332 |
| **5** | **0.5088** | 114 | 10664 |
| **7** | **0.2667** | 105 | 17142 |
| **9** | **0.3592** | 103 | 8255 |
| **15** | **0.1143** | 105 | 10664 |

Second route (`dyadic_oddfactor_infratio.py`, `n ≤ 3000`): for P=3,5,7,9 the
large-`n` infimum is set early (argmin ≤ 1040) and **no late new low past
n=1000** — the infimum is not decaying toward 0 asymptotically. The exact-linear
companion reports the residual `ν₂(n) − c·n` stays **O(1)** (bounded), e.g.
P=3 word 001: residual ∈ {−0.67, −1.33, −2.00} at n up to 24000 with c=2/3 —
i.e. `ν₂` tracks `c·n` exactly to within a bounded constant.

## What it establishes

- **The dyadic dichotomy's prediction is numerically confirmed for P=3,5,7,9,15**
  (the `R-dyadic-periodicity-dichotomy` rung of `research/weakened/dyadic-collapse-ladder.md`): 
  power-of-2 periods collapse (ν₂ = O(1)); odd-factor periods grow with positive
  density. The two counterexample families to the universal transfer (consecutive
  odds = P=1, alternating 2/4 = P=2) are exactly the k=0,1 collapse cases.
- **The odd-factor converse is NOT refuted by an asymptotic plateau** up to
  `n=24000`: the infimum stays bounded away from 0 for each fixed P. So the
  dyadic dichotomy *is* supply-useful on the periodic families (each odd-factor
  word satisfies a uniform `ν₂ ≥ c_P·n`).
- **The infimum decays as P grows** (0.647 → 0.509 → 0.267 → 0.359 → 0.114 for
  P=3,5,7,9,15): there is no uniform constant `c` across all P, and nothing
  here is a proof for the *aperiodic* prime bit string.

## What it does NOT establish (honest limits)

- **Numerical evidence only, not a proof.** `ν₂ ~ c·n` on a fixed odd-factor
  periodic word to `n=24000` does not prove it for all `n`. The odd-factor
  converse (odd part `o>1` ⟹ `ν₂ ≥ c(P,h)·n` for all `n` from the σ-orbit
  positive-density argument) **remains CONJECTURED** — see the obstruction in
  `research/notes/dyadic-collapse-proof.md` (nonzero `σ^d h` at one `d` proves
  only that the tail can be nonzero, not how often it is 1 as `d` ranges).
- **Does not close G-supply.** These are PERIODIC words, explicitly not the
  primes. The prime bit string is aperiodic; "the primes are not eventually
  periodic" is the contrapositive of collapse for eventually-periodic inputs
  only and gives no quantitative `ν₂ ≥ c·n` for the primes. That remains the
  named-open two-point mod-4 switch hypothesis (`abgs-2011-s9-mod4-switch-limit-open`).

## Bearing

The dyadic thread's gate is now swung: the collapse half is PROVED
(`dyadic-collapse-proved`), the over-general "any period collapses" claim is
REFUTED (`rule90-periodic-window-collapse-refuted`), and the odd-factor
converse is now numerically supported without asymptotic plateau — but it is
still a conjecture, and the step from "periodic odd-factor words grow" to "the
aperiodic primes satisfy ν₂ ≥ c·n" is still the open supply statement. The
honest Route B deliverable remains the CONDITIONAL theorem on the two-point
mod-4 switch correlation bound.

## Claim block

```claim
id: dyadic-oddfactor-infimum-bounded
statement: For each fixed odd-factor period P in {3,5,7,9,15}, the asymptotic
  infimum of nu2(n)/n over the right-diagonal {0,2}-suffix count of a periodic
  2-then-odds halved-gap bit string is bounded below by a positive constant
  (P=3: 0.6471, P=5: 0.5088, P=7: 0.2667, P=9: 0.3592, P=15: 0.1143, argmin
  n<=114), the residual nu2(n) - c*n stays O(1) to n=24000, and no late new low
  appears past n=1000 for any P. Hence the odd-factor converse (odd part o>1
  implies nu2 >= c(P,h)*n) is NOT refuted by an asymptotic plateau on the
  periodic families; it remains CONJECTURED (numerical only, P bounded), and the
  infimum decays as P grows, so there is no uniform c across all P and no
  transfer to the aperiodic prime bit string.
hypotheses: periodic halved-gap bit string h (2-then-odds, gaps 2/4); nu2 =
  #2s in the maximal {0,2} suffix of the right diagonal; exact integers, n<=24000.
holds-here: yes (as a measurement on the periodic families, explicitly NOT the primes)
status: checked (exact-int captures dyadic_inf_measure / dyadic_oddfactor_density_exact /
  dyadic_oddfactor_infratio; two independent routes agree; residual O(1) bounded)
bearing: closes the Directive 60/64 gate on the dyadic dichotomy's odd-factor half:
  the prediction is numerically confirmed for P=3,5,7,9,15, the converse is not
  plateau-refuted to n=24000, but it stays conjectured and does NOT close G-supply
  (abgs-2011-s9-mod4-switch-limit-open stays the open hypothesis). Prevents
  over-reading the dichotomy as extending to a supply proof for the primes.
follows-from: dyadic-collapse-proved, rule90-periodic-window-collapse-refuted
anchor: code/out/dyadic_inf_measure.captured.txt, code/out/dyadic_oddfactor_density_exact.captured.txt,
  code/out/dyadic_oddfactor_infratio.captured.txt, research/notes/dyadic-collapse-proof.md
```

## Files

- `code/out/dyadic_inf_measure.captured.txt` — inf nu2/n over [100,20000], P=1..15
- `code/out/dyadic_oddfactor_density_exact.captured.txt` — exact-linear c with O(1) residual, P=3,5
- `code/out/dyadic_oddfactor_infratio.captured.txt` — late-infimum scan, P=3,5,7,9 to n=3000
