Solve by extremal graph theory and explicit construction, with a complete
(SAT/ILP) chromatic-number oracle underneath every witness. Chromatic number is
a decision problem — one Boolean per (vertex, colour), one clause per edge and
colour — and must be computed completely, never greedily: the whole content of a
`k`-chromatic witness is that no `(k-1)`-colouring exists, and a heuristic that
merely failed to find one has certified nothing.

The oracle for this problem is `isTriangleFree` plus exact `chi`, calibrated by
reproducing `h_3(3)=5` (the 5-cycle), `h_3(4)=11` (the Grötzsch graph) and
`h_3(5)=21` on its own, together with a search for small triangle-free
6-chromatic graphs — `h_3(6)` being the smallest open value and the natural
computational target.

Choose the half of the problem deliberately. The asymptotic constant is
entangled with `R(3,k)` and is not reachable; the ratio statement
`h_3(k+1)/h_3(k) -> 1` asks for a construction incrementing the chromatic number
at vertex-cost factor `1+o(1)`, where Mycielski's classical construction costs a
factor `~2`. Beating `2` by any margin is a genuine result and is a construction
question this workspace can attack directly. Understand first, exactly, why
Mycielski doubles.

Use sat_solver for every chromatic number and every bounded existence question,
coder for triangle-free graph generation with stated symmetry breaking,
symbolic_math for the independence-number and second-moment computations, and
pattern_finder on the structure of the extremal graphs — what they look like is
the content, not the numbers alone.
