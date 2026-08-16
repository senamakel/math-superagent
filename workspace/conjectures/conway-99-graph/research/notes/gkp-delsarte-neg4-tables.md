# Greaves–Koolen–Park "Improving the Delsarte bound" (arXiv:2012.09391) — bearing on (99,14,1,2)

**Source now in library:** `research/sources/greaves-koolen-park-delsarte-bound.full.md`
(summary `research/summaries/greaves-koolen-park-delsarte-bound.md`).
Also `research/sources/koolen-cao-yang-smallest-eigenvalue-survey.full.md`
(Koolen–Cao–Yang survey, arXiv:2011.11935) — landed as the survey the
`least-eigenvalue-minus-4-structure` approach's first-step named.

## What the paper does
GKP combine the Delsarte (maximal-clique) bound, a cubic "maximal-clique
polynomial" M_Γ(c), and the claw/edge-regular machinery to rule out infinite
families of feasible SRG parameter sets with smallest eigenvalue −4, −5, −6,
−7. Theorem 4.3 is the generic infinite-family exclusion; the appendix gives
explicit nonexistence tables per smallest-eigenvalue value.

## The check the approach called for: is (99,14,1,2) in the −4 table?

**No.** The −4 table (Table 1) contains only
`(v,k,λ,µ)` = (23276,1330,372), (25025,1426,399), (27455,1696,480),
(38875,2046,569) — all v ≫ 99. None of the −5/−6/−7 tables contains it either.
So **the GKP −4 repertoire does not rule out (99,14,1,2)**, exactly as the
approach note (research/approaches/least-eigenvalue-minus-4-structure.md) had
already flagged from the abstract ("none of its excluded sets is (99,14,1,2)").
This is now checked directly against the tables in the held full text, not
inferred.

## Why the −4 gate is 99-specific (recomputed)
For srg(v,k,1,2), s is the smaller root of x² − (λ−µ)x − (k−µ) = x² + x − (k−2):
- rook(9,4,1,2): x²+x−2, roots 1, −2 → smallest eigenvalue **−2**.
- srg(99,14,1,2): x²+x−12, roots 3, −4 → smallest eigenvalue **−4**.
- bvls(243,22,1,2): x²+x−20, roots 4, −5 → smallest eigenvalue **−5**.
So the value −4 holds for 99 and neither control: any argument that uses
"smallest eigenvalue = −4" as a hypothesis cannot be refuted by the two
existing members (the hypothesis fails on them). This is the opposite of the
closed eigenvalue-only routes, which survive verbatim on all three. (Simple
algebra; not a new computation — matches `brouwer-srg-table-51-100` which lists
`? 99 14 1 2 | 3 54 | -4 44`.)

## The wall at −4
The approach note already records (from Birkhoff–Jiang–Polyanskii, and restated
in the Koolen–Cao–Yang survey framework) that the class "smallest eigenvalue
≥ −λ" has a finite forbidden-induced-subgraph characterization only for
λ < λ* ≈ 2.0198. Since −4 = −λ with λ=4 > λ*, there is no finite
forbidden-subgraph basis for the −4 class — the "forbidden subgraph from a
−4 basis" plan cannot fire. The Neumaier geometric dichotomy (a primitive SRG
with smallest eigenvalue −m is geometric if (m+1)(a+1)−k > (c−1)(m+1)/2) fails
its hypothesis at (99,14,1,2): with m=4, a=λ=1 (Hoffman-clique param), c=2,
k=14 gives 5·2−14 = −4, not > 2.5.

Net: the −4 structural theory is the soundest genuinely-99-specific gate in the
library, but none of its published nonexistence tables contains 99, and no
finite subgraph basis exists at −4. The live remainder is the geometric-SRG
classification literature at smallest eigenvalue −4 (van Dam / Koolen–Yang /
Spence lineage), not the Delsarte/claw tables.

```claim
id: gkp-delsarte-neg4-tables-do-not-rule-out-99
hypotheses: none beyond (99,14,1,2) being feasible with smallest eigenvalue -4.
statement: The Greaves-Koolen-Park "-4/-5/-6/-7 nonexistence tables"
  (arXiv:2012.09391, appendix) do not contain (99,14,1,2); its parameter set
  appears in none of them. The -4 table lists only (v,k,lambda,mu) =
  (23276,1330,372),(25025,1426,399),(27455,1696,480),(38875,2046,569), all
  v >> 99.
evidence: sourced (read directly from the held full text, lines 460-571).
holds-here: yes - confirms the approach note's expectation that GKP does not
  rule out 99, now by direct table inspection rather than inference.
status: sourced
```

```claim
id: smallest-eigenvalue-gate-99-specific
hypotheses: srg(v,k,1,2).
statement: Smallest eigenvalue s is -2 for rook(9,4,1,2), -4 for (99,14,1,2),
  -5 for bvls(243,22,1,2); so -4 holds for 99 and neither control, making
  least-eigenvalue = -4 a 99-specific hypothesis the controls cannot refute.
evidence: reasoned (eigenvalue formula x^2+x-(k-2), roots at k=4,14,22).
holds-here: yes.
status: checked (algebra)
```
