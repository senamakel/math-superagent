# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `DIGEST.md` | Entry point to research/ — which source establishes what, ordered by usefulness, plus open gaps for the n=5000 canonical enumeration. |
| `cubic_sublattices.md` | Independent cross-product proof (Horváth arXiv:2203.01901) of cubic-sublattice existence/classification; corroborates frame×scale decomposition. Non-quaternion route. |
| `ehrhart_cubes.md` | Ionascu Thm 3.1 Ehrhart polynomial of a lattice cube; backs the pts(t) point-count formula validated on cubes A and B. |
| `goswick_0806.3943.md` | **Primary 3D source.** Euler-matrix quaternion parametrization; Sárközy Thm 1.2 (primitive 3-icube ↔ primitive Lipschitz quaternion of odd norm); Cor 5.12 frame×scale; Thm 5.10 twin count. Basis of frame enumeration. Full text: `icubes_goswick.md`. |
| `icubes_goswick.md` | Full converted text of arXiv:0806.3943 (companion to `goswick_0806.3943.md`). |
| `kiss_kutas_1108.3113.md` | **Canonical enumeration.** Primary-Hurwitz-quaternion pinning of the 24-fold symmetry (Claim 2.6, Thm 4.2) so each cube/orbit is generated once. Counts m-icubes. Full text: `kk_full_actual.full.md`. |
| `kk_full.md` | Duplicate placeholder of Kiss–Kutas; see `kiss_kutas_1108.3113.md`. |
| `kk_full_actual.full.md` | Full converted text of arXiv:1108.3113 (companion to `kiss_kutas_1108.3113.md`). |
| `kk_full_actual.md` | Duplicate placeholder of Kiss–Kutas; see `kiss_kutas_1108.3113.md`. |
| `kk_primary_theorem_report.md` | Citable-statement extract of the primary-Hurwitz theorem + Sárközy, with exact quotes/URLs; cautions 1108.3113 is a Z^4 paper. |
| `pe579_lattice_cube_theory.md` | Run's own synthesized theory note (enumeration strategy + Ehrhart + power-sum plan). Full derivation not executed here; flagged for implementer. |
| `verify_cross.py` | Independent cross-product-divisor parametrization of cubes; cross-checks brute.py C/S for n=1,2,4,5. |
| `verify_examples.py` | Naive brute-force cube enumerator (independent of frame method) for oracle check. Run it to confirm C(1..4). |
| `verify_primary.py` | Validates that primary primitive odd-norm quats generate each primitive frame exactly once (vs all primitive quats). **Must be run by implementer.** |
