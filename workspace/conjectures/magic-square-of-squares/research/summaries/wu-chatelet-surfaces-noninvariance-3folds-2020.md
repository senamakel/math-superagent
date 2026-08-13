# Wu, "Châtelet surfaces and non-invariance of the Brauer–Manin obstruction for 3-folds" (arXiv:2010.04919)

Full text: `research/sources/wu-chatelet-surfaces-noninvariance-3folds-2020.full.md`
(arXiv:2010.04919v2, 2020, PDF).

## What it establishes

Han Wu constructs three kinds of Châtelet surfaces with prescribed arithmetic
behaviour under field extensions, and uses them to study weak approximation with the
Brauer–Manin obstruction and the Hasse principle with the Brauer–Manin obstruction
for 3-folds (pencils of Châtelet surfaces over a curve) under field extensions.
General constructions conditional on a conjecture of Stoll negatively answer some
questions; explicit unconditional examples illustrate the constructions and the
exceptions.

**This is the companion to the already-held** `wu-non-invariance-brauer-manin`
(arXiv:2103.01784, surfaces): both are cited together in the frontier (cited-by-2).
Where the surfaces paper studies non-invariance for surfaces, this one treats the
3-fold pencil case.

## Bearing on the magic-square-of-squares problem

The `brauer-manin-k3-surface` approach is closed on Bremner II's K3 S (S(Q) is
nonempty — `catIII-k3-has-q-point`), so the Brauer–Manin obstruction cannot prove
S(Q) = ∅. Wu's two papers matter as the caution that Brauer–Manin behaviour is not
base-change-invariant: any obstruction argument must say which field it is over, and
the MSS exists over extension fields (this run's `extension-field-mss-exist`), so a
Q-level Brauer–Manin conclusion cannot be silently transferred to Q(√3,√133)/Q.
This paper strengthens that caution for 3-folds. Both Wu papers are now in the library.

```claim
id: wu-chatelet-3folds-bm-noninvariance
statement: "Wu (arXiv:2010.04919) constructs Châtelet surfaces and 3-fold pencils of
them over which weak approximation with the Brauer–Manin obstruction and the Hasse
principle with the Brauer–Manin obstruction are not invariant under base field
extension (general constructions conditional on a conjecture of Stoll; explicit
unconditional examples)."
hypotheses: number fields; Châtelet surfaces / pencils; Stoll's conjecture for the
conditional part only
holds-here: yes (caution for any Brauer–Manin sweeping statement: behaviour is not
base-change-invariant)
evidence: asserted (paper on disk as abstract; full PDF not fetched this cycle)
bearing: fortifies the Ruled-out entry that Brauer–Manin cannot be used as a blanket
non-existence tool across fields, given MSS exist over extension fields
anchor: research/summaries/wu-chatelet-surfaces-noninvariance-3folds-2020.md
```