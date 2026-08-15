# Verdict — Mycielski kernel refutation is FALSE

The claim that the 5-critical core of `Mycielski^2(C5)` is a member of the
sharp-kernel universe `C_23` that is **not 4-colourable** is **refuted by the
run**: under the correct textbook Mycielski construction the 5-critical core
does **not** satisfy all four kernel conditions.

## The run

Command (as requested):

```
timeout 540 python3 code/run_refute_kernel.py 2>&1 | tee code/out/refute_kernel_verify.captured.txt
```

The shipped `code/refute_mycielski_kernel.py` implements `mycielski()` the
**wrong** way (installed a mirror-edge set `u_i u_j` that does not belong and
omitted the cross edges), so its own output is meaningless:

```
Mycielski(C5)=Groetzsch: n=11, edges=15, chi=4, triangle-free=False   <-- 15 wrong (real=20), triangle-free wrong (real=True)
Mycielski^2(C5): n=23, edges=41, chi=5, triangle-free=False           <-- 41 wrong (real=71), triangle-free wrong
5-critical core: n=18, edges=17, min-degree=1, chi=5                  <-- broken reduction
   deg>=4 = False, K4-free = False, K23-free = False, nbhd-maxdeg<=2 = False
No counterexample
```

(Full output: `code/out/refute_kernel_verify.captured.txt`.)

## Correct construction (independent route, exact chromatic oracle)

Textbook Mycielski(G): keep G; for each edge `v_i v_j` add **cross** edges
`u_i v_j` and `u_j v_i` (2|E|); add apex `w` adjacent to every `u_i` (|V|).
Total edges `= 4|E| + |V|`.

`code/diag_mycielski.py` (correct implementation):

```
C5: n=5 e=5 chi=3 triangle-free=True
Mycielski(C5): n=11 e=20 chi=4 triangle-free=True     # Groetzsch, textbook-correct
Mycielski^2(C5): n=23 e=71 chi=5 triangle-free=True   # real Mycielski^2(C5)
```

(Output: `code/out/diag_mycielski.captured.txt`.)

## Final verdict witness — `code/verdict_mycielski_core.py`

```
Mycielski^2(C5): n=23 e=71 chi=5 triangle-free=True min-degree=4
is 5-critical (every G-v 4-colourable): True      # Mycielski of 4-critical is 5-critical
not 4-colourable: True
5-colourable: True
explicit K2,3 subgraph: (0, 2, [1, 6, 12])        # two vertices with 3 common neighbours
   min-deg>=4   = True
   K4-free      = True
   K2,3-free    = False     <- FAILS
   nbhd-maxdeg<=2 = True
=> all four kernel conditions: False
```

(Output: `code/out/verdict_mycielski_core.captured.txt`.)

## Answers to the request

1. **Does the 5-critical core satisfy all four kernel conditions and fail
   4-colourability?**
   It fails **4-colourability** (correct, chi=5), and it satisfies **3** of the
   4 kernel conditions (`min-deg>=4`, `K4-free`, `nbhd-maxdeg<=2`), but it
   **fails `K2,3-free`** (explicit K2,3 on vertices `0, 2` with common
   neighbours `1, 6, 12`). So **it is NOT a member of `C_23`**, and it is
   therefore **NOT** a counterexample to `sharp-kernel-4color`. Triangle-free
   does **not** imply K2,3-free.

2. **Core vertex / edge count, min degree:**
   The whole `Mycielski^2(C5)` is already 5-critical (23 vertices, 71 edges,
   min-degree 4), so the core is the whole graph. The shipped script's "core"
   numbers (18 / 17 / min-degree 1) came from its broken construction and are
   void.

3. **Is this core a unit-distance graph?**
   **No — and this point stands regardless.** It is a general abstract graph;
   **nothing claims it is realizable as a plane unit-distance graph.** So even
   the *intended* claim could only refute the *combinatorial* kernel theorem
   `sharp-kernel-4color` (a general graph-theoretic statement), and it would
   **not** touch the N=11 plane unit-distance size bound. Since the K2,3-freeness
   condition fails, the intended combinatorial refutation also collapses.

## Claim block

```claim
id: mycielski-kernel-refutation-false
statement: The 5-critical core of Mycielski^2(C5) does NOT satisfy all four
  sharp-kernel-4color conditions: it fails K_{2,3}-freeness (explicit K2,3 on
  vertices 0,2 with common neighbours 1,6,12) while passing min-deg>=4,
  K4-free, and nbhd-maxdeg<=2. Hence it is NOT a member of C_23 and is NOT a
  counterexample to sharp-kernel-4color.
hypotheses: Mycielski^2(C5) is the textbook Mycielski double of C5 (cross edges
  + apex star; 23 vertices, 71 edges, chi=5, triangle-free); the kernel universe
  C_N = { graphs on <=N verts : min-deg>=4, K4-free, K2,3-free, nbhd-maxdeg<=2 }.
holds-here: yes (the hypotheses are precisely the problem's kernel)
status: checked
bearing: refutes the proposed counterexample to sharp-kernel-4color; leaves the
  N=11 plane unit-distance size bound untouched (the graph is general, not
  realized as a unit-distance graph).
anchor: code/out/refute_kernel_verify.md
```

## Notes

- The described vertex count "23", chi=5, and triangle-freeness of the *real*
  graph are all correct; but the shipped script's own numbers (15/41 edges,
  triangle-free=False, 18-vertex core) are **self-refuting** — a genuine
  Mycielski of a triangle-free graph is triangle-free, which the script's
  `triangle_free=False` output already contradicts.
- `code/refute_kernel_independent.py` reuses the same broken `mycielski()`
  and `critical_core()` from the shipped module, so it confirms only the broken
  construction, not the intended facts. Its real Groetzsch edge count "expect
  92*?" was itself a red flag (expect was wrong).
- The K2,3-freeness failure is inherent to the *intended* construction family,
  not a fixable coding slip: the triangle-free double has many pairs of
  vertices sharing >= 3 neighbours.
