# Pattern-finder: the 2-connected count sequence is corrupted; corrected to A002218

## The sequence in the run's log was wrong

`code/out/commands.log` recorded this output from an older generator
(`lib/biconnected_gen.py`'s earlier `layer_by_layer`):

```
n=3: 1, n=4: 1, n=5: 4, n=6: 19, n=7: 121   "nonisomorphic 2-connected graphs"
```

That is **not** the 2-connected count. The old generator seeded only from a
triangle and added only *path ears* (never single-edge chords), so it produced
a narrow subclass of graphs that all (a) contain a triangle and (b) are built
without chord-additions. The OEIS match of `1,1,4,19,121` to **A280939** (the
e.g.f. `2*sinh(x/2)/sqrt(2-exp(x))` expansion) is a numerical coincidence — that
sequence has no graph-interpretation here and must not be cited as a count of
2-connected graphs.

Evidence it is wrong: the true number of nonisomorphic 2-connected graphs on
n vertices (OEIS A002218) is 1, 3, 10, 56, 468 for n=3..7, already differing at
n=4 (only C4, K4 and the diamond are 2-connected on 4 vertices; the old code
reported 1).

## The corrected generator matches an independent enumeration

The current generator `generate_2connected_levels(n_target)` seeds **all**
cycles (length 3..N), closes under **both** path ears and single-edge chords,
and dedups each vertex-count level by exact networkx VF2 isomorphism. Running it:

```
n=3: 1, n=4: 3, n=5: 10, n=6: 56, n=7: 468
```

Independent check (a second route): brute-force enumeration of **all** graphs on
n labelled vertices, keeping those networkx marks `is_biconnected`, deduplicated
by an exact brute-force canonical labelling, for n=3..6:

```
independent n=3: 1, n=4: 3, n=5: 10, n=6: 56
```

Exact agreement with the generator, and with A002218.

## Sequence analysis

`analyze_sequence` over the correct terms 1,3,10,56,468,7123,194066: not a
low-degree polynomial; leading ratios grow (3.0, 3.33, 5.6, 8.36, 15.2) —
consistent with the known super-exponential (~n^n) growth of the 2-connected
class. `find_linear_recurrence` (orders 1..8): no constant-coefficient linear
recurrence fits; the class has no simple LRS closed form. This matches the
catalogue (A002218 has no elementary closed form; enumeration by Robinson).

## Why it matters to the run

The run's `G-heart` verification task ("every 2-connected graph with δ ≥ 3 on
≤ N vertices has a 4/8/16-cycle") depends on *correctly generating the
2-connected class*. The old triangle-only, path-ear-only generator would have
undercounted it and, critically, **missed triangle-free 2-connected graphs such
as C4** — exactly the class relevant to the conjecture. The corrected generator
is validated. The n=8 level (7123 graphs) is too slow for the current pairwise
VF2 dedup within the tool timeout; that is the practical ceiling on this
generator, not a mathematical one.

## Conjecture / status

- Correctness of the corrected generator = verified numerically (exact match to
  an independent brute-force enumeration on n ≤ 6), sourced to A002218.
- The old logged sequence = refuted as a 2-connected count; its A280939 match
  is coincidence and must not be cited.
- Structures shown on these sequences: no linear recurrence, no low polynomial
  degree — nothing further to extract exactly.
