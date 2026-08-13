Solve by the arithmetic of rational points on curves. The problem reduces to a single elliptic curve: a 3×3 magic square of squares exists iff there are three points of E(Q) whose x-coordinates lie in 2E(Q) and form an arithmetic progression. Reason about that curve — its rank, its torsion, descent and the Selmer groups that bound rank, heights and the size of a generator, the image of the doubling map, and the AP-length bounds now available for elliptic curves — and use every other capability in service of that argument rather than instead of it.

Two cautions this problem has already earned:

A bound proved for x(P) is not automatically a bound for x(2P). Say which map a cited theorem is about before applying it, because the magic-square progression is of doubled-point x-coordinates.

The deliverable is non-existence, which is a claim that a set is empty, so the failure mode is an argument that proves too much. Every impossibility lemma — every modular sieve, every local or p-adic obstruction, every descent step — must be run against the witness set in `code/out/near_misses.json` using the verifier in `code/lib/mss.py`. A lemma that also forbids the Sallows LS1 grid or Bremner's 7-square grid is false and is recorded as refuted, not weakened. A lemma that has not been run against the witness set is `asserted`, never `checked`.

The box this runs on has 28 CPUs and no container CPU quota. A search worth running is worth running across them: use `multiprocessing`, and say in the captured output how many workers were used and what the search space was.
