```claim
id: lagarias-W2-formal
statement: Under the cited Eliahou numerical implication, a positive accelerated Collatz cycle whose period k is below 10,439,860,591 or whose odd-entry count is below 6,586,818,670 has period 2 and one odd entry, representing the trivial cycle.
hypotheses: k and oddCount are natural numbers; the numerical bound disjunction; `_hcycle : True` is a placeholder for the cycle predicate because the cited source statement was not reconstructed fully in Lean.
holds-here: The implication is kernel-checked, but the cited theorem is assumed.
evidence: code/lean/lagarias_W2-eb4a08bf.lean, lean_check verdict conditional.
status: conditional
formalisation: code/lean/lagarias_W2-eb4a08bf.lean
falsifies: A compiled proof showing the cited Eliahou implication is false, or a mismatch between the source's cycle convention and this accelerated-map encoding.
```

```claim
id: lagarias-W2
statement: (W2) The trivial cycle {1,2} is the only positive-integer 3x+1 cycle with period less than 10,439,860,591, and the only one with fewer than 6,586,818,670 odd integers.
hypotheses: Eliahou 1993, Theorem 3.2, with the accelerated map convention.
holds-here: asserted by Lagarias's overview; formalised only conditionally in the narrower Lean encoding above.
evidence: Lagarias overview §6.1 (W2), citing Eliahou 1993.
status: conditional
formalisation: code/lean/lagarias_W2-eb4a08bf.lean
falsifies: A published non-trivial cycle satisfying either bound, or a source-level mismatch in the formal encoding.
```
