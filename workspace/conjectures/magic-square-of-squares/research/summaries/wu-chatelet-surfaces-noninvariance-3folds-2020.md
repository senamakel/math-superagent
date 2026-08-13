# Wu, "Châtelet surfaces and non-invariance of the Brauer–Manin obstruction for 3-folds" (arXiv:2010.04919)

Full text: `research/sources/wu-chatelet-surfaces-noninvariance-3folds-2020.full.md`
(arXiv:2010.04919v2, 2020, full PDF on disk, 114KB Markdown).

## What it establishes

Han Wu constructs three kinds of Châtelet surfaces with prescribed arithmetic
behaviour under field extensions, and uses them to study weak approximation with the
Brauer–Manin obstruction and the Hasse principle with the Brauer–Manin obstruction
for 3-folds (pencils of Châtelet surfaces over a curve) under field extensions.

- **Prop 1.3.1 / Cor 1.3.2 / Cor 1.3.3** (unconditional): for any extension L/K and
  any finite S ⊂ Ω_K ∖ {complex, 2-adic} splitting completely in L, there exist
  Châtelet surfaces V₁, V₂, V₃ over K with Br(V_L′)/Br(L′) ≅ Z/2Z and prescribed
  local/global behaviour.
- **Thm 1.4.1.1 / 1.4.2.1 / 1.4.2.2** (conditional on Stoll's conjecture): Châtelet
  surface bundles X → C over a curve with non-invariant BM-obstruction behaviour
  under base change.
- Explicit unconditional examples illustrate the constructions and the exceptions.

**Companion role:** this is the 3-fold case of the already-held Wu surfaces paper
(arXiv:2103.01784); the two sit together as the frontier's earlier cited-by-2 row.

## Bearing on the magic-square-of-squares problem

The `brauer-manin-k3-surface` approach is closed on Bremner II's K3 S (S(Q) is
nonempty — `catIII-k3-has-q-point`), so BM cannot prove S(Q) = ∅. Wu's two papers
are the standing caveat that BM behaviour is **not base-change-invariant**: any
obstruction claim must say which field it is over, and the MSS provably exists over
extension fields (`extension-field-mss-exist`), so a Q-level BM conclusion cannot be
silently transferred to Q(√3,√133)/Q. This paper extends that caveat to 3-folds.

```claim
id: wu-chatelet-3folds-bm-noninvariance
statement: "Wu (arXiv:2010.04919) constructs Châtelet surfaces and 3-fold pencils of
them over which weak approximation with the Brauer–Manin obstruction and the Hasse
principle with the Brauer–Manin obstruction are not invariant under base field
extension (general constructions conditional on a conjecture of Stoll; explicit
unconditional examples)."
hypotheses: number fields; Châtelet surfaces / pencils of them over a curve; Stoll's
conjecture for the conditional part only
holds-here: yes (caution for any Brauer–Manin sweeping statement: behaviour is not
base-change-invariant)
evidence: proved (full PDF on disk, arXiv:2010.04919v2)
bearing: fortifies the Ruled-out entry that Brauer–Manin cannot be used as a blanket
non-existence tool across fields, given MSS exist over extension fields
anchor: research/summaries/wu-chatelet-surfaces-noninvariance-3folds-2020.md
```