# Approach: Cross-prime minus-class-number Bernoulli condition (the synthesis)

```approach
idea: Replace the open Mihăilescu forcing step with its computable consequence: a hypothetical solution x^p − y^q = 1 with p, q distinct odd primes forces a cross-prime divisibility q | h^−(Q(ζ_p)) (and symmetrically p | h^−(Q(ζ_q))) in the minus class groups, and h^− is a fully computable Bernoulli product — so the condition reduces to exact integer divisibility, giving a new, sweepable necessary condition on the exponent pair (p,q) that is distinct from the double-Wieferich sieve.
mechanism: The run already holds (checked, OEIS-verified at all odd p ≤ 97) the analytic formula h^−(Q(ζ_p)) = 2p ∏_{χ odd} (−½ B_{1,χ}). Research this round established the decisive subtlety: cross-prime divisibility q | h^−(Q(ζ_p)) with q ≠ p is decided by this analytic Bernoulli product, NOT by Herbrand–Ribet (which is a same-prime statement about p-torsion). Since h^− is h^+-independent and exactly computable, "q | h^−(Q(ζ_p))" is a finite, exact, per-pair integer test — no unknown plus class number, no p-adic L-function, no new literature needed. This produces a necessary condition on the exponent pair that is genuinely different in kind from double-Wieferich: it constrains (p,q) by the arithmetic of the opposite cyclotomic field's minus class group. Conditional on the descent forcing q | h^− (the open request `exact-statement-mihăilescu-bbf8`), every hypothetical second solution must lie in the surviving set, which is exactly the shape check_conditions(p,q) evaluates and parallel_map sweeps.
status: adopted
precedent: held claims `minus-class-number-formula` (checked), `minus-class-normalisation-checked`, `minus-class-computable-plus-not`, `a000927-catalogue-reproduced`; research this round on Herbrand–Ribet / Kummer / Main Conjecture (Ribet 1976; Mazur–Wiles 1984; Lozano-Robledo 2007) establishing the same-prime/cross-prime distinction.
first-step: (1) Extend the held exact h^− computation (lib.cyclo.Cyclo, Fraction arithmetic) to every odd prime p ≤ 300, producing exact integers h^−(Q(ζ_p)). (2) Build the cross-prime divisibility matrix: for all distinct odd primes p,q ≤ 300, evaluate q | h^−(Q(ζ_p)) and p | h^−(Q(ζ_q)) by exact integer division. (3) Add crossprime_condition(p,q) to check_conditions, calibrate so the known solution 3^2−2^3=1 is excluded-by-hypothesis (p=2 even; no odd-prime lemma applies), and report the surviving (p,q) pairs as the new candidate set alongside the held double-Wieferich sweep.
```

## Why this is the synthesis, not one of the three candidates

The three proposals this round were analytic-S-unit (Subspace), analytic-approximation (Padé), and algebraic-Iwasawa. Research resolved them as: Subspace **refuted** (ineffective + growing S); Padé **grounded but loose** (its direct theorems are fixed-base / fixed-equal-exponent, so they do not match the variable-base, variable-exponent form x^p − y^q = 1; the matching superelliptic framing has effective constants that are the already-ruled-out astronomical Baker bounds); Iwasawa **grounded with a correction** — and the correction is the new idea.

The correction: my Iwasawa candidate said "Herbrand–Ribet converts q | h^−(Q(ζ_p)) into q | B_k". That is wrong as stated, because Herbrand–Ribet is a *same-prime* statement (p | B_k ⟺ p-torsion of Cl(Q(ζ_p))). The descent's divisibility is *cross-prime* (q ≠ p), and cross-prime divisibility is governed by the **analytic Bernoulli class-number formula**, which this run already holds and has checked against OEIS A000927. Neither my candidate nor the run's prior work had named that distinction; research supplied it. The productive move is therefore not "Herbrand–Ribet" but "exact integer divisibility of the computable minus class number by the opposite prime", and that is a runnable, uniform, new necessary condition.

## Known-solution placement (falsifier check)

The known solution 3^2 − 2^3 = 1 has p = 2 even, so the odd-prime hypothesis of every lemma here excludes it. At p = 2 the field Q(ζ_2) = Q is trivial and there are no even-k eigenspaces; the Bernoulli condition is vacuous, never excluding the known solution. Nothing here over-proves to "no solution at all". The symmetric pair (p,q)=(2,3) is excluded-by-hypothesis, not refuted.

## What is conditional and what is not

- **Held and checked, not conditional:** h^−(Q(ζ_p)) = 2p ∏_{χ odd} (−½ B_{1,χ}) is computable in exact arithmetic; the run reproduced OEIS A000927 for all odd p ≤ 97 (`a000927-catalogue-reproduced`, checked) and holds the formula from two sources (`minus-class-number-formula`, `relative-class-number-formula-second-source`).
- **Conditional:** the claim "a solution forces q | h^−(Q(ζ_p)) and p | h^−(Q(ζ_q))" rests on the descent forcing some non-trivial q-torsion in the minus class group — the open request `exact-statement-mihăilescu-bbf8`. Until that is pinned, the sweep is a **candidate necessary condition**, and this file states that plainly. The falsifier for the forcing statement is recorded in REQUESTS.md: if Mihăilescu's final step does not proceed through the double-Wieferich conditions / minus-class-group descent, the condition must be re-placed.
- **Possible refinement (second, independent route):** there is a classical congruence expressing q | h^−(Q(ζ_p)) in terms of ordinary Bernoulli numbers B_{2k} mod q (the same-prime case is irregularity; the cross-prime case is a Carlitz/Kummer-type product congruence). Confirming that statement would give a second, character-sum-free route to the same matrix — the independent verification rule 11 requires. That is a research follow-up, not a prerequisite for the first step.

## What it buys

1. A **new necessary condition** on a hypothetical second solution, different in kind from double-Wieferich (which the run already swept: no pair below 200 survives). It constrains (p,q) through the opposite field's minus class group.
2. A **computed candidate set** — the pairs (p,q) passing both the double-Wieferich sieve and the cross-prime Bernoulli sieve — which is the concrete object later steps (and the open forcing lemma) must attack.
3. **Zero new literature risk**: the first step uses only held, checked claims and exact integer arithmetic. The cost grows polynomially in p (character sums over a = 1..p−1), not in the problem's search bound — it is a sweep over the *description* (exponent pairs), not over the answer space.
4. A **calibration anchor** for the descent machinery: the irregular primes p = 37, 59, 67 (where p | h^−(Q(ζ_p)), same-prime) are the known warm-up, and the cross-prime matrix extends that structure to q ≠ p.

## Verification plan

- Exact integer arithmetic throughout (`lib.cyclo.Cyclo` already reproduced A000927; no floats).
- Cross-check the matrix by two routes: (a) direct exact integer division of computed h^−; (b) the ordinary-Bernoulli-number congruence once confirmed by research.
- Calibrate `crossprime_condition(2,3)` to report excluded-by-hypothesis (p even), matching the held `cond-evaluator-odd-prime-wieferich` behaviour.
- Report the surviving pair set and its intersection with the double-Wieferich sweep, with the bound reached and runtime.
