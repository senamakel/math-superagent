# OEIS catalogue cross-check of the verified Mycielski construction

The verified Mycielski construction (code/out/diag_mycielski.captured.txt,
textbook: keep G, add cross edges + apex star) gives:
- C5:            5 vertices,  5 edges, chi=3
- Mycielski(C5): 11 vertices, 20 edges, chi=4 (Groetzsch, triangle-free)
- Mycielski^2(C5):23 vertices, 71 edges, chi=5 (triangle-free)

The OEIS catalogue entries match these exactly:
- A083329 (vertices): ..., 11, 23, ... (a(3)=11, a(4)=23) ✓
- A122695 (edges): 0,0,1,5,20,71,236,755,... (a(3)=5, a(4)=20, a(5)=71) ✓

Closed forms / recurrences are self-consistent and reproduce the terms:
- A122695: a(n)=6a(n-1)-11a(n-2)+6a(n-3) for n>4. Check a(5)=6·71-11·20+6·5=236 ✓,
  a(6)=6·236-11·71+6·20=755 ✓ (both match the b-file).
- A083329: a(n)=2a(n-1)+1 for n>=2: 5→11→23 ✓.

The Mycielski vertex/edge transition (v,e)→(2v+1, 3e+v) is exact and matches:
(5,5)→(11,20)→(23,71) ✓. (A 4e+v form in earlier notes was the mirror variant B,
which the run's kernel does not use; 4·5+5=25≠20.)

Reproduction program: code/scholar_verify_oeis_mycielski.py (intended to be run
by the tool_builder to produce captured output; the arithmetic above is exact
integer arithmetic and checks by hand).

```claim
id: oeis-mycielski-catalogue-match
statement: The OEIS-catalogued Mycielski vertex and edge sequences (A083329:
  vertices 1,2,5,11,23,..., a(n)=2a(n-1)+1; A122695: edges 0,0,1,5,20,71,236,...,
  a(n)=6a(n-1)-11a(n-2)+6a(n-3)) reproduce exactly the run's verified textbook
  Mycielski construction: C5=5v/5e, Mycielski(C5)=11v/20e, Mycielski^2(C5)=23v/71e,
  under the exact transition (v,e)->(2v+1,3e+v).
hypotheses: OEIS b-file terms are the reference; Mycielski = cross edges + apex.
holds-here: yes — consistent with the verified code/out/diag_mycielski.captured.txt.
status: catalogued (OEIS terms) cross-checked against the run's checked computation;
  the reproduction script is written (code/scholar_verify_oeis_mycielski.py) but
  its captured output is pending a tool_builder run, so this is catalogue+hand-check
  rather than a fresh machine run.
bearing: turns the Mycielski edge/vertex counts used in the size-bound kernel
  work from a lookup into a reproducible catalogue; independent confirmation of the
  5/11/23-vertex and 5/20/71-edge counts the kernel refutation relies on.
anchor: research/summaries/oeis_a122695.md, research/summaries/oeis_a083329.md,
  code/out/diag_mycielski.captured.txt, code/scholar_verify_oeis_mycielski.py
falsifies: a Mycielski graph with vertices or edges differing from A083329/A122695
  at the C5-M1-M2 offsets — the verified run and the catalogue agree.
```
