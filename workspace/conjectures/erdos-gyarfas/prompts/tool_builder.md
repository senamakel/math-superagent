The single most valuable program on this run is the oracle, and it is small:
given a graph, return its minimum degree and the exact set of its cycle
lengths. Write it first, check it by hand on graphs whose answers you can state
without a computer — $K_4$, $K_{3,3}$, the Petersen graph, the cube — and put
it in `code/lib/` so nothing on this run recomputes it. Every claim about small
graphs the run makes later rests on this file being right.

`nauty` is installed and its binaries are Debian-prefixed: `nauty-geng`,
`nauty-countg`, `nauty-shortg`, `nauty-directg`. `nauty-geng -q -c -d3 <n>`
generates every connected graph on $n$ vertices with minimum degree at least 3,
one per line in graph6, up to isomorphism — which is exactly the search space
this conjecture lives in, without the $n!$ relabellings a hand-rolled generator
would grind through. `networkx.from_graph6_bytes` reads that format directly.
Use it as the exhaustive check; do not write your own generator.

The counts grow fast, so state the count before you run anything: pipe
`nauty-geng` into `wc -l` at each $n$ and report the sequence. That number
tells you where exhaustive generation stops being the method and the SAT
encoding takes over, and knowing where that boundary is, is itself a result.

`igraph` is installed beside `networkx` and is substantially faster for cycle
and connectivity work on the sizes this will reach. Prefer it when the
enumeration is the bottleneck, and cross-check the two against each other on
small cases.
