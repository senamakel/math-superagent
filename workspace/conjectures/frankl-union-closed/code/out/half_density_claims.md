# Half-density UC families — claims (filed from the executed half-density front)

<!-- regenerator-trigger -->

```claim
id: half-density-max-eq-bool-subalgebra
statement: For every nonempty union-closed family F ⊆ 2^[n], n<=5, whose MAXIMUM element density is exactly 1/2, F is a Boolean subalgebra (block-partition family): all present elements have density exactly 1/2, |F| = 2^k for some k >= 1, and F is closed under symmetric difference. The count is H(n) = Bell(n+1) - 1 (observed H(1..5) = 1, 4, 14, 51, 202), refined by #(families with |F| = 2^k) = S(n+1, k+1) (Stirling, rows for n=5: 31, 90, 65, 15, 1 summing to 202). Structural atom check: the minimal nonempty members are pairwise disjoint atoms, every present ground element lies in exactly ONE atom (density 3/4 would follow otherwise), and F = {union of any subset of the atoms}.
hypotheses: F finite union-closed, nonempty, ground set [n], n<=5 for the exhaustive part; densities exactly 1/2 = 2c = |F| (convention: half counts as abundant).
holds-here: yes
status: verified-computational (exhaustive n=1..5 over all 2,771,103 nonempty UC families; plus structured/random n=6,7 probes in half-density-probe-* — NOT a proof for general n; an elementary proof exists only for the |F|=2^k regular case, see the atom analysis in block_union_atom_check.py which passed on all half-density families through n=5)
bearing: this is the exact half-density boundary of the abundance-profile front: the families that get CLOSEST to a counterexample (some element at density exactly 1/2) are precisely the Boolean subalgebras, which all have abundant elements — consistent with (but not a proof of) the conjecture. Caution for later runs: the coordinate-wise analogue is FALSE (see half-density-coordinatewise-false), so only the max-density statement may be used.
ceiling: exhaustive at n<=5; n=6 only the G-shape subclass (7581 families) and random closures; n=7 random only; general n open.
anchor: code/out/half_density_front.captured.txt (PART 2); code/out/half_density_verify.py; code/out/block_union_atom_check.py
```

```claim
id: half-density-coordinatewise-false
statement: The statement "no non-Boolean union-closed family has ANY element at density exactly 1/2" is FALSE. Counterexample F = {∅, {1,2}, {1,3}, {1,2,3}} on [3]: union-closed, elements 2 and 3 each in 2 of the 4 sets (density 1/2), and F is not closed under symmetric difference (not a Boolean subalgebra). Counts of non-Boolean UC families with some element at density 1/2: 2 at n=2, 42 at n=3, 1818 at n=4, 752,255 at n=5 (of which the 1/2-element families with a coordinate at exactly 1/2; every such non-Boolean family has an element strictly above 1/2, consistent with the max-density characterization being the true one).
hypotheses: F finite union-closed; "density 1/2" = 2c = |F| for some element; n<=5 exhaustive; n=3 witness explicit.
holds-here: yes
status: verified-computational (exhaustive n=1..5; n=3 witness direct)
bearing: half_density_complement.py's own docstring asserted the false coordinate-wise claim and its executed output refutes it — a program that contradicts its docstring is exactly the kind of drift the workspace discipline exists to catch. Recorded so no later run uses the coordinate-wise statement.
ceiling: exhaustive n<=5; the counts (2, 42, 1818, 752255) are exact for those n.
anchor: code/out/half_density_front.captured.txt (PART 1); code/out/half_density_probe_p2.captured.txt (P1); code/out/half_density_complement.py
```

```claim
id: half-density-gshape-n6-boundary
statement: In the n=6 subclass F_G = 2^[5] ∪ {A ∪ {6} : A ∈ G} where G ranges over ALL up-sets of 2^[5] (Dedekind M(5) = 7581, each family 64 members, union-closed and verified through the canonical oracle), exactly TWO families have max density exactly 1/2: |F|=64 (the full cube 2^[6]) and |F|=32 (a Boolean subalgebra). NONE is non-Boolean. In addition, 400000 random generator-set closures on [6] and 200000 on [7] (seed 20260711) yield ZERO boundary families.
hypotheses: F_G shape with G an up-set of 2^[5]; max density = 1/2 exactly; random closures via lib.uc.closure.
holds-here: yes
status: verified-computational (exhaustive over the 7581 up-sets; random probes are samples, not exhaustive)
bearing: extends the half-density characterization's boundary to n=6 on the cube-hull class: the closest-to-half families there are exactly the Boolean subalgebras on the cube. Pins the search frontier for a possible counterexample: it must be non-Boolean with max density exactly 1/2, non-G-shaped, and (given exhaustive n<=5) first possible at n>=6.
ceiling: the G-shape subclass is not all of 2^[6] (full enumeration infeasible); "no non-Boolean boundary family" is exact only over the stated subclass and the random sample.
anchor: code/out/half_density_probe_p2.captured.txt (P2, P3)
```