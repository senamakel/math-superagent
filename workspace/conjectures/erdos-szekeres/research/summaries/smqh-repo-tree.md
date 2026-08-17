# SMQH GitHub repository — full tree (`automatic-symmetries`)

> **Source:** `https://api.github.com/repos/bsubercaseaux/automatic-symmetries/git/trees/main?recursive=1` (recursive git tree API response, held at `research/sources/smqh-repo-tree.full.md`). Artifact evidence for the library's SMQH-inner-12 close.

## What the tree establishes

The full recursive file listing of `bsubercaseaux/automatic-symmetries` (the repo behind Subercaseaux–Mackey–Qian–Heule, arXiv:2506.00224). It contains only:

- `encoders/erdos_szekeres.py` (the ES encoder, [[smqh-erdos-szekeres-encoder.py]]), `encoders/everywhere_unbalanced*.py`
- `experiments/16-6-4sym.sh`, `16-6-5sym.sh` (the **16-point / 6-gon** symmetry experiments)
- `realizations/helpers/16-6-4fold-*.txt`, `16-6-5fold-sym.txt`
- scripts, plus empty `formulas/`, `orientations/`, `solutions/` (all `.gitkeep`)

There is **no inner-12 data, no 32-point no-7-gon data file, no 4-fold-32-point orientation table** anywhere in the tree.

## Bearing

This is the primary-artifact evidence for the dead-end close in
[[LIBRARIAN-closed-SMQH-inner12-dead-end]]: the six non-realizable inner-12
configurations behind `smqh-no-realizable-4fold-32-no7gon` were **never
published** (not even as repository data), so they cannot be extracted into a
concrete forbidden local structure without re-running the ~1 CPU-year
enumeration. **Do not re-search for them.** The ES(7) computational frontier
status is: SMQH (4-fold, no realizable 32-pt no-7-gon), PointSAT (200k abstract
candidates, none realizable), Dumitru (UNSAT only on anchored subfamilies) — all
three fail to realize any 32-point no-7-gon set, but none exhausts the abstract
space, so none refutes ES(7)=33.

```claim
id: smqh-inner12-never-published
statement: The six non-realizable inner-12 configurations behind the SMQH claim that no 4-fold-symmetric 32-point no-7-gon set is realizable were never published, and are absent from the automatic-symmetries repository (no inner-12 / 32-point data file exists in the recursive tree). They cannot be extracted into concrete forbidden local structures without re-running the ~1 CPU-year SAT enumeration.
hypotheses: the SMQH paper's 310,187,713-solution / 6-configurations claim; the public repo tree as fetched.
holds-here: true (verified against the primary repo tree artifact this run).
status: catalogued (artifact evidence — the absence is documented, the underlying SMQH claim stays asserted-by-source per kph/smqh).
bearing: closes the 'extract inner-12 as a restricted class' route: not reproducible from public artifacts. Reinforces that all ES(7) computational routes reach 32-point no-7-gon candidates and none has realized one.
anchor: research/summaries/LIBRARIAN-closed-SMQH-inner12-dead-end.md
follows-from: smqh-no-realizable-4fold-32-no7gon, smqh-erdos-szekeres-encoder
```

(see also [[smqh-github-repo-search]], the same repo's README-landing record.)
