# SMQH GitHub repository — landing/README record (`automatic-symmetries`)

> **Source:** `https://github.com/bsubercaseaux/automatic-symmetries` (raw GitHub landing / converted HTML, held at `research/sources/smqh-github-repo-search.full.md`). The README and structure of the repo behind Subercaseaux–Mackey–Qian–Heule, arXiv:2506.00224.

## What this record establishes

The repository landing page + README (the page's rendered content is largely the
README, which the sibling note [[smqh-automatic-symmetries-repo-README]] carries
in full). It documents:

- **Requirements:** `eznf` + `PySAT` for the Python SAT encodings; `allsat-cadical`
  for solution enumeration; `Localizer` (bsubercaseaux/localizer) for the
  realizability step.
- **The 16-point / 6-gon symmetry experiments:** `experiments/16-6-4sym.sh`
  generates the 66 4-fold-symmetric 16-point no-6-gon sets (~minutes);
  `16-6-5sym.sh` the 932 5-fold ones (<20 min). These land in `realizations/`.
- **The everywhere-unbalanced minimality** experiments and the automated proof of
  Proposition 4.2 (via `scripts/axiom_proof.py`).

## Bearing

Confirms the computational pipeline shape the run's SAT arm should mirror:
(1) `eznf` encodes the ES problem as a CNF over orientation/CC variables
([[smqh-erdos-szekeres-encoder.py]]), (2) `allsat-cadical` enumerates all
satisfying assignments (the abstract order types), (3) `Localizer` decides which
are realizable. This is the exact pattern PointSAT generalises (diversity +
partial-realization + flippability) and the realistic cost model for a 32-point
search.

It is also the repo-artifact evidence that the 16-point experiments exist but the
**32-point no-7-gon inner-12 data does not** — see
[[LIBRARIAN-closed-SMQH-inner12-dead-end]] and claim `smqh-inner12-never-published`.

```claim
id: smqh-pipeline-shape
statement: The SMQH computational pipeline is: eznf encodes the ES g-gon problem as CNF over orientation/CC variables; allsat-cadical enumerates satisfying assignments (abstract order types); Localizer decides realizability. This mirrors the point/abstract vs realizable divide and is the cost model a 32-point ES(7) search must budget.
hypotheses: the automatic-symmetries repo's software stack as documented (eznf, PySAT, allsat-cadical, Localizer).
holds-here: yes — the run's SAT arm reproduces exactly this pipeline to reach a known answer (ES(5)=9 / ES(6)=17) before attempting ES(7).
status: catalogued (artifact/documentation read this run).
bearing: gives the run's computational arm its concrete software pipeline and the realizability-separation step that every abstract-order-type search needs.
anchor: research/summaries/smqh-github-repo-search.md
follows-from: smqh-erdos-szekeres-encoder, kph-flippability-method
```

(see also [[smqh-repo-tree]], the exhaustive file listing.)
