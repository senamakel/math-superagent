# Exact integrality feasibility for srg(v,k,1,2) — CORRECTED

Computed by hand in exact integer arithmetic and cross-checked against the
Makhnev–Minakova classification and the Berlekamp–van Lint–Seidel five-member
list. **This replaces the earlier `feasibility-candidates.md` conclusion, which
used the k=14-specific formula `f=(-k+4(v-1))/7` and wrongly reported k=32 as
passing integrality.**

## The correct general test

For `srg(v,k,λ,μ)` with `λ=1, μ=2`:
- counting: `v = 1 + k + k(k-2)/2`
- `delta = (λ-μ)² + 4(k-μ) = 4k-7`, must be a perfect square `(2u+1)²`
  (equivalently `k = u²+u+2` — this is exactly the perfect-square condition).
- eigenvalues `r,s = (-1 ± √(4k-7))/2`.
- multiplicity of `s`: `g = ½[(v-1) - (2k-(v-1))/√delta]`, `f = (v-1)-g`.
  Integrality requires `2k-(v-1)` divisible by `√(4k-7)` AND the quotient
  parity even.

## Exact tabulation (integer arithmetic)

| k | v | 4k−7 | √ | r,s | (2k−(v−1))/√ | g | f | feasible? |
|---|---|---|---|---|---|---|---|---|
| 4   | 9     | 9   | 3  | 1,−2   | (8−8)/3 = 0      | 4   | 4   | YES (Paley 9, spectrum 1⁴−2⁴) |
| 8   | 33    | 25  | 5  | 2,−3   | (16−32)/5 = −16/5 | —   | —   | **NO — 2k−(v−1) not div by 5** |
| 14  | 99    | 49  | 7  | 3,−4   | (28−98)/7 = −10   | 54  | 44  | YES (spectrum 3⁵⁴−4⁴⁴; matches Brouwer) |
| 22  | 243   | 81  | 9  | 4,−5   | (44−242)/9 = −22  | 132 | 110 | YES (BVLS, spectrum 4¹³²−5¹¹⁰) |
| 32  | 513   | 121 | 11 | 5,−6   | (64−512)/11 = −448/11 | — | — | **NO — not div by 11** |
| 44  | 969   | 169 | 13 | 6,−7   | (88−968)/13 = −880/13 | — | — | **NO — not div by 13** |
| 112 | 6273  | 441 | 21 | 10,−11 | (224−6272)/21 = −288 | 3280 | 2992 | integrality passes; existence open |
| 994 | 494019| 3969| 63 | 31,−32 | (1988−494018)/63 = −7810 | 250914|243104| integrality passes; existence open |

## Conclusion

**Eigenvalue-multiplicity integrality leaves exactly the five parameter sets**
```
(9,4), (99,14), (243,22), (6273,112), (494019,994)
```
which is precisely the Berlekamp–van Lint–Seidel / Makhnev–Minakova list
`k = u²+u+2` with `u ∈ {1,3,4,10,31}`.

### Corrections this establishes
1. **`srg(33,8,1,2)` does not exist — by eigenvalue-multiplicity integrality.**
   `u=2 → k=8` fails integrality (2k−(v−1)=−16 not divisible by 5). This
   removes the "nearest precedent" that problem.md highlights — the mechanism is
   the surviving-on-9-and-243 integrality argument, so it gives *no* new weapon
   against 99.
2. **problem.md's candidate list `k=8(33),32(513),44(969)` is wrong** — these
   pass the perfect-square test but fail multiplicity integrality.
3. **k=32 and k=44 are both ruled out by integrality** (the earlier corridor note
   wrongly reported k=32 as passing); only 6273 and 494019 are genuinely open
   later members.

## Source support
- Makhnev & Minakova 2004 (via Cesarz–Woldar abstract & search digest):
  `k=u²+u+2`, `u∈{1,3,4,10,31}`.
- Berlekamp–van Lint–Seidel five-member list (via Zaw 2020 Deza paper and
  Keramatipour 2026 SAT paper): only (9,4),(99,14),(243,22),(6273,112),
  (494019,994).
- Brouwer's table 51–100: `? 99 14 1 2 | 3 54 | -4 44` — open, spectrum 3⁵⁴,−4⁴⁴
  confirming the k=14 computation.

## Verification
r=3,s=−4 spectrum (54,44) for 99 matches Brouwer exactly; r=4,s=−5 (132,110) for
243 is consistent with the Deza-paper statement. Both positive controls (9,243)
pass; both negative controls (8, and the later 32,44) fail. Integrality is a weak
test (does not decide 99) but it exactly reproduces the five-member classification.

---

```claim
id: integrality-five-members
statement: Eigenvalue-multiplicity integrality (over Z) admits exactly the five
  parameter sets (9,4),(99,14),(243,22),(6273,112),(494019,994) in the family
  srg(v,k,1,2); equivalently k=u^2+u+2 with u in {1,3,4,10,31}. In particular
  srg(33,8,1,2) does not exist, ruled out by integrality (2k-(v-1)=-16 not
  divisible by sqrt(25)=5).
hypotheses: srg(v,k,lambda=1,mu=2) with the counting relation v=1+k+k(k-2)/2.
holds-here: yes — (99,14) is exactly the open member u=3; the two positive
  controls (9,243) pass and were checked; the two later members 513 and 969
  (which problem.md lists as open) fail integrality.
status: checked
bearing: kills problem.md's candidate list 33/513/969 as open and the corridor
  note's claim that k=32 passes integrality; integrality is refuted on arrival
  as a route to 99 since 9 and 243 both pass it.
anchor: code/out/feasibility-candidates-corrected.md
```

```claim
id: srg33-does-not-exist-integrality
statement: There is no strongly regular graph with parameters (33,8,1,2).
hypotheses: none beyond srg definition; integrality of eigenvalue multiplicities.
holds-here: yes — this is the member adjacent to 99 that problem.md flagged as
  the nearest precedent; it is excluded by the standard integrality test which
  cannot reach 99 (9 and 243 survive it).
status: checked
bearing: problem.md's claim that (33,8,1,2) needs a nonexistence proof is
  resolved — integrality is the mechanism; it provides no new weapon for 99.
anchor: code/out/feasibility-candidates-corrected.md
```

```claim
id: aut-bounds-established
statement: Automorphism group G of a putative srg(99,14,1,2): |G| divides
  2.3^3.7.11 (Makhnev-Minakova 2004); if 7||G| then G congruent Z_7; if 2||G|
  then |G| divides 6 i.e. G in {Z2,Z6,S3} (Cesarz-Woldar 2025, computer-free);
  no automorphism group Z6,S3,Z9,E9 of order 6 or 9 (Crnkovic-Maksimovic 2020).
hypotheses: existence of the graph is assumed hypothetically; the divisibility
  claims are conditional on existence.
holds-here: yes — all order constraints are conditions on any (99,14,1,2).
status: asserted-by-source (computer-free paper; the Frob(21) elimination in
  the Cesarz-Woldar arXiv version is computer-assisted; E9/Z9/S3/Z6 ruling is
  computational orbit-matrix work).
bearing: the graph has a very small (possibly trivial) automorphism group; this
  kills symmetry-assuming construction searches, which is why none has settled it.
anchor: research/sources/cesarz-woldar-automorph-conway99.full.md,
  research/sources/crnkovic-maksimovic-composite-automorphism.full.md
```

```claim
id: existence-status-open
statement: Existence of srg(99,14,1,2) is open: no construction and no
  nonexistence proof is known; Brouwer's table marks (99,14,1,2) with '?'.
  No nonexistence or existence claim has been published, refereed and
  confirmed; recent contributions are structural constraints only.
hypotheses: none.
holds-here: yes.
status: asserted-by-source (Brouwer table; Wikipedia; recent preprints).
bearing: sets the honest status.
anchor: research/sources/brouwer-srg-table-51-100.full.md
```
