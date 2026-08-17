# Pattern-finder report — round 33: clique-complex homology gate (directive 39, FIRST) — CLOSED

## What this round did

Directive 39 reopened the run and named the clique-complex homology gate as the
FIRST line: compute H1(Cl(G)) of the controls and check the Cioaba–Mim
classification before the line becomes route twelve. The on-disk computation
(`code/out/homology_controls.py`, 12:35, and `research_clique_complex_chi.py`)
had no report and no capture. This round verified it, **proved** the H1 closed
form, and delivered the gate verdict.

## The computation (exact integer arithmetic)

dim H1(Cl(G)) = (E − v + 1) − rk(delta_2), delta_2 the triangle→edge boundary map.
Two independent exact routes agree: rational Fraction elimination and mod-p
elimination at p = 1009, 65537.

| graph | v | k | E | T | rank(delta_2) | dim H1 |
|---|---|---|---|---|---|---|
| rook(3) | 9 | 4 | 18 | 6 | 6 | **4** |
| bvls | 243 | 22 | 2673 | 891 | 891 | **1540** |

## The structural fact — PROVEN, not conjectured

λ = 1 means every edge is in exactly one triangle. Two triangles sharing edge
{a,b} would make a and b share ≥ 2 common neighbours, contradicting λ=1. So all
triangles are **edge-disjoint**; their boundary vectors have disjoint support and
are independent, hence **rk(delta_2) = T exactly** (forced by λ=1, not a
2-data-point observation). Therefore for every connected λ=1 SRG:

    dim H1(Cl(G)) = (E − v + 1) − T = vk/3 − v + 1 = 2T − v + 1.

Edge-disjointness histogram verified on both controls: {1:18} (rook), {1:2673}
(bvls).

Family sequence over u ∈ {1,3,4,10,31}:

    [4, 364, 1540, 227920, 163190944]        (99 → 364)

`analyze_sequence`: not a low-degree polynomial (divisor-63 signature); all ≡ 0
(mod 4); mod-2 period 1. `oeis_lookup`: **no match** (recorded miss).

## Gate verdict: REFUTED-ON-ARRIVAL as a separator (as the steering predicted)

- H1 is **nonzero on both controls** (4, 1540), and predicted nonzero (364) at
  99, so Cioaba–Mim's H1=0 criterion cannot separate 99 from 243. The line is
  closed beside the eigenvalue routes: **no homology obstruction, no separation.**
- The closed form is now a **theorem** and therefore fully parameter-determined —
  it holds for ANY λ=1 SRG including both controls — which is precisely why it
  carries no separating power. This is the honest end of the homology line: not
  refuted by a counterexample but closed because the invariant is atomic in
  (v,k) and both existing members realize it.

## Sequence-tools verdict (round 33)

Consistent with rounds 1–32: every family sequence is parameter-determined
(harmless for both 9 and 243), an OEIS miss, or a mechanism trace. The H1(Cl)
family is the newest addition to the "divisor-63-governed polynomial" class,
now with a proof of its closed form. **No sequence on disk separates
srg(99,14,1,2) from its controls.** Nothing promoted to durable memory (server
degraded); findings live in the report and note. NOTHING FURTHER on this line.

## Files
- `code/out/homology_controls.py` — direct rational H1 of both controls (gate source).
- `code/out/research_clique_complex_chi.py` — Euler char, mod-p double-prime check.
- `code/out/pf_h1_closed_form.py` — rank + closed-form exact verification.
- `research/notes/clique-complex-h1-closed-form.md` — the claim with the proof.
