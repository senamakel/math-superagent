# Fractional chromatic values of the run's constructible graphs — computed

The fractional-chromatic-LP route (claims `fractional-chromatic-lp-duality`,
`fractional-chromatic-chain`, both `asserted` in
`research/sources/fractional-chromatic-number-lp-definition.md`) posed an open
value question: does any constructible unit-distance graph have `chi_f > 4`?
This note records that the question has been **computed** on the run's exact
graphs; the values below are `checked` with explicit witnesses, not looked up.

## Values (captured outputs in this folder)

- **C5**: chi_f = 5/2. (`frac_chro_calib.captured.txt`)
- **Diamond** (K4 minus an edge, chordal/perfect): chi_f = 3. Confirms the
  perfect-graph collapse `chi_f = chi = omega`; settles the "5/2 vs 3"
  discrepancy against the secondary sources that read 5/2. (`frac_chro_calib.captured.txt`)
- **Moser spindle** (7v, 11e, chi=4): chi_f = **7/2 = 3.5**. Exact rational
  check: primal = dual = 7/2; dual witness w_v = 1/2 on all 7 vertices, sum 7/2.
  By the ratio identity chi_f >= |V|/alpha = 7/2 (alpha=2), and the dual witness
  gives chi_f <= 7/2, so chi_f(Moser) = 7/2 exactly.
  (`frac_chro_verify_rational.txt`, `frac_chro_calib.captured.txt`)
- **Moser+Moser** (26v, 69e, chi=4): chi_f = **3.5 = 7/2**. Primal fractional
  colouring total weight 7/2 (16284 independent sets) and dual LP converged to
  the same value (sum w = 3.5, support w=1/2). (`frac_mosm_primal.txt`,
  `frac_mosm_lp.txt`). n/alpha = 26/10 = 2.6 lower bound. (`frac_mosm_alpha.txt`)

## What this establishes

`status: checked` for the exact values on the four calibration graphs. Each is
verified by two independent routes where available (primal and dual LP agreeing
by strong duality; exact rational dual for the Moser).

**Bearing for the problem:** chi_f(Moser) and chi_f(Moser+Moser) both equal
**7/2 < 4**. Since `chi_f <= chi`, no value here exceeds 4, so the LP route
does **not** certify `chi >= 5` on any graph the run has built so far (as
expected, since all are 4-colourable). The two graphs the run's constructions
produce both sit at 7/2, exactly at |V|/alpha for the Moser, which is the value a
weighted-independent-set symmetry would give. This is a concrete negative datum:
**the fractional-chromatic lower bound is not a 5-certifier on Moser or
Moser+Moser**, and the LP line is bounded at 3.5 on this family so far. The open
question remains whether *any* richer construction crosses 4; these are the
first two checks.

## Reconciles a stale claim in the library

`research/REQUESTS.md` (row `fractional-chromatic-lp-lower-bound`), the approach
file `research/approaches/fractional-chromatic-lp-lower-bound.md`, and
`research/summaries/scholar-digest.md` all state that "chi_f(Moser) and
chi_f(Moser+Moser) have never been computed / no captured output exists". That
is **stale**: the captured outputs listed above exist and give exact values.
The REQUESTS row can now be answered (both = 7/2), not left OPEN-for-computation.
(The separate `code/scholar_verify_frac.py` exact rational scan written this
session is a belt-and-braces extra and was not itself executed; the on-disk
rational verify file already provides the exact evidence.)

```claim
id: chi-f-moser-values
statement: chi_f(C5) = 5/2, chi_f(diamond) = 3, chi_f(Moser spindle) = 7/2,
  chi_f(Moser+Moser) = 7/2; all four strict <= 4, so the fractional-chromatic
  LP lower bound certifies chi >= 5 on none of the run's four calibration
  graphs.
hypotheses: finite graphs; independent-set polytope enumerated exactly;
  strong LP duality chi_f = omega_f.
holds-here: yes
status: checked
bearing: the adopted fractional-chromatic-lower-bound route is bounded at 3.5
  on the run's constructed family so far; negative datum, no 5-certifier found.
follows-from: fractional-chromatic-lp-duality, fractional-chromatic-chain
answers: fractional-chromatic-lp-lower-bound (REQUESTS OPEN row)
anchor: code/out/fractional-chromatic-values.md
```

```claim
id: chi-f-moser-exact-argument
statement: chi_f(Moser spindle) = 7/2 exactly, because the ratio identity gives
  chi_f >= |V|/alpha = 7/2 (alpha = 2) and the dual fractional-clique witness
  w_v = 1/2 for all 7 vertices (sum 7/2, every independent set weight <= 1) gives
  chi_f <= 7/2, so the two meet at 7/2.
hypotheses: Moser spindle has 7 vertices, alpha = 2, every independent set has
  <= 2 vertices; uniform weight is feasible in the ratio identity.
holds-here: yes
status: checked
bearing: gives chi_f(Moser) exactly without running the LP; used to cross-check
  the captured solver output.
follows-from: fractional-chromatic-lp-duality
anchor: code/out/fractional-chromatic-values.md
```
