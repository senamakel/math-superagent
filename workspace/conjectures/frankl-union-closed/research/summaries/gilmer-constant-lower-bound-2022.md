# Gilmer, "A constant lower bound for the union-closed sets conjecture" (arXiv:2211.09055, Nov 2022)

**Full text:** [[gilmer-constant-lower-bound-2022.full]]

The first constant lower bound for Frankl's (union-closed sets) conjecture. Method: information theoretic. Take A, B independent uniform members of F; A∪B ∈ F so H(A∪B) ≤ log|F| = H(A) = H(B). If every element had density < c, an entropy inequality forces H(A∪B) > H(A), a contradiction.

```claim
id: gilmer-constant
statement: Every nonempty union-closed family F ⊆ 2^[n] has an element in at least a 0.01 fraction of its sets.
hypotheses: F union-closed, F ≠ {∅}, |F| finite
holds-here: yes
status: proved
bearing: The base of the entire entropy line. Improves Knill–Wójcik's Ω(1/log₂|F|). The information-theoretic strengthening used is: if A,B independent draws from a distribution on subsets of [n] with Pr[i∈A] < 0.01 for all i and H(A)>0, then H(A∪B) > H(A).
anchor: research/sources/gilmer-constant-lower-bound-2022.full.md
```

**Bearing for this run:** the constant 0.01 is superseded; the value here is the *method* (two independent copies, entropy inequality on their OR). This is the shape that (3−√5)/2 and later improvements all refine.

**Does not settle:** any constant beyond 0.01; the paper's own Conjecture 1 (that the technique can be pushed to (3−√5)/2) was later proved by AHS/Chase–Lovett/Sawin/Pebody and partially refuted by Sawin.
