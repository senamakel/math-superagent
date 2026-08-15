# A083329 & A122695 — the canonical Mycielski vertex/edge counts, with the 3e+v transition

<!-- sources: https://oeis.org/A083329, https://oeis.org/A122695 -->

## What these are

The vertex and edge counts of the iterated Mycielski graphs, used by the run's
kernel-building machinery (`Mycielski^k(C5)` cores in `diag_mycielski.py`,
`verdict_mycielski_core.py`, `refute_mycielski_kernel.py`).

- **A083329** (vertices): `1,2,5,11,23,47,95,...` closed form
  `a(0)=1, a(n)=3·2^(n−1)−1`; recurrence `a(n)=2a(n−1)+1` (n≥2).
- **A122695** (edges): `0,0,1,5,20,71,236,755,...` closed form
  `a(n)=(18−27·2^n+14·3^n)/36`; recurrence `a(n)=6a(n−1)−11a(n−2)+6a(n−3)` (n>4);
  generating function `x^2(1−x+x^2)/((1−x)(1−2x)(1−3x))`.

## What they establish here

They confirm the run's verified Mycielski construction values at the right
offsets (catalogue vs `code/out/diag_mycielski.captured.txt`):

- vertices: `A083329[2..4] = (5, 11, 23)` ✓ matches C5, M(C5), M²(C5).
- edges:   `A122695[3..5] = (5, 20, 71)` ✓ matches C5=5e, M=20e, M²=71e.

**The canonical (no-mirror) transition is `(v,e) → (2v+1, 3e+v)`.**
Check by hand: C5 `(5,5) → (11, 3·5+5=20) → (23, 3·20+11=71) → (47, 3·71+23=236)`,
every term matching the b-file. The `4e+v` form that appeared in some notes is
the **mirror variant B** `(5,25,111,467)` — `4·5+5=25≠20` — which the run does
**not** use. The verified counts (20, 71, 236) only match the `3e+v` canonical
form.

## Verification status

`catalogued` (OEIS b-file terms) cross-checked by hand and against
`code/out/diag_mycielski.captured.txt`; the corrected reproduction script
`code/scholar_verify_oeis_mycielski.py` (fixed to `3e+v`) reproduces 20, 71,
236 without reading the b-file. The script itself awaits a tool_builder run,
so this remains catalogue + hand-check, not a fresh machine reproduction.

```claim
id: oeis-mycielski-catalogue-match
statement: The OEIS-catalogued Mycielski vertex and edge sequences (A083329:
  vertices 1,2,5,11,23,..., a(n)=2a(n-1)+1; A122695: edges 0,0,1,5,20,71,236,...,
  a(n)=6a(n-1)-11a(n-2)+6a(n-3)) reproduce exactly the run's verified textbook
  Mycielski construction: C5=5v/5e, Mycielski(C5)=11v/20e, Mycielski^2(C5)=23v/71e,
  under the exact transition (v,e)->(2v+1,3e+v).
hypotheses: OEIS b-file terms are the reference; Mycielski = cross edges + apex;
  canonical no-mirror variant.
holds-here: yes — consistent with the verified code/out/diag_mycielski.captured.txt.
status: catalogued (OEIS terms) cross-checked against the run's checked computation;
  the reproduction script code/scholar_verify_oeis_mycielski.py is corrected to 3e+v
  and awaits a tool_builder run, so this is catalogue+hand-check rather than a fresh
  machine run.
bearing: turns the Mycielski edge/vertex counts used in the size-bound kernel work
  from a lookup into a reproducible catalogue; independent confirmation of the
  5/11/23-vertex and 5/20/71-edge counts the kernel refutation relies on.
anchor: research/summaries/oeis_a122695.md, research/summaries/oeis_a083329.md,
  code/out/diag_mycielski.captured.txt, code/scholar_verify_oeis_mycielski.py
falsifies: a Mycielski graph with vertices or edges differing from A083329/A122695
  at the C5-M1-M2 offsets — the verified run and the catalogue agree.
```
