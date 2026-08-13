Solve by structural graph theory. Reason about what a minimal counterexample must look like — connectivity, girth, degree distribution, forbidden subgraphs, separators, ear decompositions, DFS trees and their back edges, expansion — and use every other capability in service of that argument rather than instead of it.

The oracle for this problem is a checker that takes a graph and returns its minimum degree and the set of its cycle lengths. Verify it against small cases by hand before trusting anything computed past the literature's verification bound.
