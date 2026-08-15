# Pattern analysis of the sharp-kernel census C_N

Author: pattern-recognition specialist. All statements are EXACT over the
enumerated instances; each structural conclusion is a **conjecture** (it holds
for every term enumerated, but is not a proof).

## Data

The finite sharp-kernel class
`C_N = { graphs on <= N vertices : min-degree >= 4, K4-free, K_{2,3}-free,
every vertex-neighbourhood induces a graph of max-degree <= 2 }`.
This is the size-bound universe: any 5-chromatic unit-distance graph contains a
5-critical (min-deg>=4) subgraph, which is a UDG and hence satisfies all four
conditions, so it lies in C_N. The kernel's conditions are exactly certified
in `code/out/sharp_nbhd_cert.captured.txt` (Groebner-basis / exact-arithmetic
proofs).

Per-N kernel-member counts (complete enumeration via nauty-geng across 28
parallel residue slices):

| n | kernel members | 4-chromatic | 3-colourable |
|---|---------------|-------------|--------------|
| 8 | 1            | 1           | 0            |
| 9 | 4            | 1           | 3            |
|10 | 16           | 16          | 0            |
|11 | 228          | 198         | 30           |

**Every member of C_8..C_11 is 4-colourable** — verified by BOTH the calibrated
Cadical153 SAT oracle and independent exhaustive DSATUR backtracking (0
disagreements). The prior recorded result (census-kernel-4color-result.md)
stopped at N=10; the n=11 enumeration (228 members, all 4-colour-tested) was
completed and is captured in `code/out/census_kernel_n11_test.captured.txt`.

## Sequence structure

`1, 4, 16, 228` (kernel-count, n=8..11):
- Not a low-degree polynomial (differences 3,12,212 never become constant).
- No constant-coefficient linear recurrence of order <= 3.
- Leading ratios 4.0, 4.0, 14.25 — super-exponential onset at n=11, matching
  the expectation that the finite check, not a closed form, is the only route
  (the class accumulates combinatorially as N grows; nothing clean governs it).

`1, 1, 16, 198` (4-chromatic members) and `0, 0, 3, 30` (3-colourable members):
- The 3-colourable subsequence is divisible by 3 (0,0,3,30) but too short to
  carry weight.
- Neither fits a low-order polynomial or recurrence.

Conclusion: **no exploitable closed-form/recurrence structure** in the kernel
counts. The size-bound result is a census, not a formula.

## Structural regularity: Moser spindle as the universal 4-critical core

Among the 4-chromatic kernel members:

| n | four-chromatic | contain Moser SUBgraph | contain Moser INDUCED |
|---|----------------|------------------------|-----------------------|
| 8 | 1             | 1                      | 0                     |
| 9 | 1             | 1                      | 0                     |
|10 | 16            | 10                     | 0                     |
|11 | 198           | 118                    | 0                     |

Facts established (exact over all enumerated members):
1. The Moser spindle (7 vertices, 11 edges) is **edge-critical**: removing any
   single edge makes it 3-colourable (confirmed;
   `code/out/confirm_moser_critical` output). It is the minimal 4-chromatic
   graph.
2. It is the **dominant** 4-critical subgraph: present (as a subgraph) in
   118/198 n=11 four-chromatic members, 10/16 n=10, and the single four-chromatic
   members at n=8 and n=9. The most common 7v/11e 4-critical core canonical
   form equals the Moser spindle (verified).
3. **It is NEVER an induced subgraph** of any kernel member (0/198).

The "never induced" fact is a direct, structural consequence the kernel
itself supplies: the Moser spindle has a vertex of degree 3 (degrees 4,3,3,3,3,3,3),
so any induced copy would violate the kernel's min-degree>=4 condition. (The
Moser is itself K4-free — verified it contains no K4 subgraph — so K4-freeness
does not exclude it; the min-degree condition does.) This is exactly why the
census survives: the kernel is a sound superset of 5-critical UDGs.

## What this says for the lower bound

- A 5-chromatic UDG, if it exists, must contain a 5-critical subgraph that is a
  kernel member. Since every kernel member through N=11 is 4-colourable,
  **every UDG on <= 11 vertices is 4-colourable** (exact census; conjecture in
  the proof sense — three kernel lemmas plus the oracle, all checked).
- The kernel-count sequence is not cleanly predictable, so pushing the bound
  beyond N=11 is purely a matter of making the n=12+ enumeration feasible
  (the cost is nauty-geng growth, not a closed form that could be extended by
  analysis alone).
- The fact that the Moser spindle — the archetypal non-4-colourable-forced
  gadget in the plane — is already the dominant subgraph of the 4-chromatic
  kernel members, yet never forces 5-chromaticity at any N<=11, is a concrete
  instance of the problem's core difficulty: 4-chromatic subgraphs are abundant
  and harmless; accumulated rigidity, not a single gadget, is what would be
  needed.

## Artifacts

- code/analyze_kernel_chrom.py / code/out/analyze_kernel_chrom.captured.txt
- code/analyze_cores_small.py / code/out/analyze_cores_small.captured.txt
- code/check_moser_containment.py / code/out/check_moser_containment.captured.txt
- code/verify_dominant_core.py, code/enum_core_graphs.py,
  code/confirm_moser_critical.py
- code/out/census_kernel_n11_test.captured.txt (the N=11 census verdict)
