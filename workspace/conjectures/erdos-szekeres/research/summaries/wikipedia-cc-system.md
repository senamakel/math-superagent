# CC systems (Wikipedia; Knuth's *Axioms and Hulls*)

Source: https://en.wikipedia.org/wiki/CC_system (Knuth 1992, LNCS 606)
Full text: [[wikipedia-cc-system.full]]

A **CC system** (counterclockwise system) is a ternary relation *pqr* on triples of distinct points modelling "p,q,r in counterclockwise order" (Knuth), axiomatising the orientation data of a planar point set in general position. This is the exact finite object the run's SAT arm encodes: an abstract order type / rank-3 chirotope as a relation on triples.

## The five axioms (Knuth 1992 p.4)

For all distinct p,q,r,s,t:
1. **Cyclic symmetry**: pqr ⇒ qrp.
2. **Antisymmetry**: pqr ⇒ not prq.
3. **Nondegeneracy**: either pqr or prq.
4. **Interiority**: if tqr ∧ ptr ∧ pqt, then pqr.
5. **Transitivity**: if tsp ∧ tsq ∧ tsr ∧ tpq ∧ tqr, then tpr.

(Axiom 5 is the transitivity law — the rank-3 instance of Felsner–Weil's *generalized transitivity law*; axioms 4–5 are what the SMQH/Dumitru/Scheucher/Balko–Valtr encoders post to force a genuine order type.)

## From points to a CC system, and back

A planar point set (no three collinear) induces a CC system: *pqr* ⟺ det[[xp,yp,1],[xq,yq,1],[xr,yr,1]] > 0. General position ⟺ determinant never zero on distinct triples. **Converse fails:** not every CC system arises from Euclidean points (non-stretchable/abstract). [Knuth pp.25–26]

## Equivalent notions and enumeration

- Two-to-one correspondence between CC systems and **uniform acyclic oriented matroids of rank 3**; those correspond 1-1 to **topological equivalence classes of pseudoline arrangements with one marked cell**. [6][7]
- CC systems ⟺ pseudoline arrangements ⟺ sorting networks with adjacent compare-exchanges; counts within polynomial factors. [6][p.35]
- **Convex hull in a CC system**: the pairs *pq* such that *pqr* ∈ system for every third *r*, forming a cycle — enables O(n log n) hull / hull-vertex / Graham-scan generalisations (Aichholzer–Miltzow–Pilz 2013). [8][9][10]
- **Enumeration (OEIS A006246):** non-isomorphic CC systems on n points: 1,1,1,2,3,20,242,6405,316835,28627261… growing exponentially in **n²**; realizable ones grow only Θ(n log n) [7][p.40]. Count bound C_n ≤ 3^{C(n,2)} [13]; **Knuth's conjecture** C_n ≤ n·2^{n−2}·C_{n−1}. [13]

## Bearing

- Supplies the exact axiom set the orientation-variable SAT encoders post; these are what make an encoder enforce "this triple orientation is a genuine order type".
- Quantifies the realizability trap: abstract CC systems outnumber realizable ones super-exponentially (n² vs n log n), so a purely abstract lower bound would likely be unrealizable — matching the run's rule that an order-type construction must be realized in exact coordinates before it counts.
- Knuth's recursion constant 2^{n−2} is a coincidence of notation with the ES bound, not a link; the recursion enumerates order types, not convex-n-gon-freeness.

```claim
id: cc-system-axioms
statement: A CC system (Knuth) is a ternary relation pqr satisfying cyclic symmetry, antisymmetry, nondegeneracy, interiority and transitivity; a realizable planar point set yields one via the 3x3 orientation determinant, but not every CC system is realizable. CC systems are a 2-to-1 cover of uniform acyclic rank-3 oriented matroids and 1-1 with marked pseudoline arrangements; realizable ones count only ~exp(Theta(n log n)) vs ~exp(n^2) abstract.
hypotheses: triples of distinct points, general position
holds-here: yes
status: asserted (Knuth's published statements, restated by Wikipedia — a secondary source; the axioms and counts are quoted, not independently verified here)
bearing: exact axiom set the SAT arm's encoder must post to force genuine order types; quantifies the unrealizability trap (abstract >> realizable count)
anchor: research/sources/wikipedia-cc-system.full.md
answers: cc-system-axioms-basis (the transitivity/interiority axioms the encoders cite are here made explicit)
```
