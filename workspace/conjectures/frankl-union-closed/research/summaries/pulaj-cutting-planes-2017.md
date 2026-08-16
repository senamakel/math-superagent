# Pulaj, "Cutting planes for families implying Frankl's conjecture" (arXiv:1702.05947, 2017)

**Full text:** [[pulaj-cutting-planes-2017.full]]

Designs an exact cutting-plane / exact-IP algorithm to compute Poonen weights, characterizing FC and Non-FC families up to 10 elements. Constructs an explicit counterexample to a conjecture of Morris (2006) about Non-FC family generators.

```claim
id: poonen-theorem
statement: For a union-closed family A with ∅∈A and U(A)=[n], A is FC (every union-closed F⊇A has an element i∈[n] with |F_i| ≥ |F|/2) iff there exist nonnegative c_1..c_n summing to 1 such that for every union-closed B⊆P([n]) with B⊎A=B, Σ c_i|B_i| ≥ |B|/2.
hypotheses: A finite union-closed, ∅∈A, U(A)=[n]. (If ∅∉A the condition B⊎A=B becomes B⊎A⊆B.)
holds-here: yes
status: proved (Poonen 1992; is the load-bearing characterisation for the entire FC-computational line)
bearing: the exact-decision condition the oracle in phase 3 must reproduce: decide FC-ness by nonemptiness of the weight polyhedron P^A.
anchor: research/sources/pulaj-cutting-planes-2017.full.md
```

```claim
id: pulaj-algorithm
statement: There is an exact algorithm (cutting planes + exact rational IP) that computes whether a union-closed family A is FC/Non-FC via Poonen's weight polyhedron P^A, feasible on all FC-families up to 10 elements.
hypotheses: finite union-closed A, ∅∈A iff that polyhedron is defined; otherwise condition is B⊎A ⊆ B
holds-here: yes
status: proved (algorithm correctness; computational over n≤10)
bearing: This is the computable engine GOAL.md calls for under "the 3-set question, decided by the LP." P^A nonempty ⟺ FC.
anchor: research/sources/pulaj-cutting-planes-2017.full.md
follows-from: poonen-theorem
```

```claim
id: pulaj-morris-counterexample
statement: A conjecture of Morris (2006) about the structure of minimal generators of Non-FC-families is false.
hypotheses: the specific conjecture of Morris
holds-here: yes
status: proved (explicit witness)
bearing: a known-dead-end recorded so the run does not rebuild the same conjecture.
anchor: research/sources/pulaj-cutting-planes-2017.full.md
contradicts: morris-conj3
```

**Bearing:** the Poonen-weight LP is the exact-decision library function this run's oracle must reproduce (decide FC-ness by nonemptiness of P^A). Verifying Pulaj's FC-characterizations is a good "reproduce one published result computationally" target for phase 3.
