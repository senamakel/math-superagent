"""NOTE (context curator): This check is NOT needed and has been superseded.
The 'wedge of two triangles sharing one vertex' example cited in an old durable-
memory entry is WRONG: such a graph has min degree 2 (vertex 0 has degree 4, the
other four vertices have degree 2), so it is NOT a delta>=3 graph and cannot
serve as the counterexample to a 2-connectivity lemma. The correct example of a
delta>=3 graph with a cut vertex and delta<=2 lobes is the glued 3xPetersen
graph from code/out/connectivity/verify_connectivity.log (n=31, delta=3, node
connectivity 1, lobes of v have delta=1). Standalone hand-argument, not a
program run; do not cite this file.
"""
