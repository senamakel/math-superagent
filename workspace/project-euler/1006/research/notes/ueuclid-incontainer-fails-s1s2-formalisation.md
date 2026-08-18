The Lean statement formalises only the supplied numerical hand-check, not the executable Python function or its acceptance-test counts. It has no hypotheses: all numerals are data. The original prose's hypotheses/parameters `(1,0,1,5,3)` are not binders here because the implementation is not defined in Lean; they are reflected in the theorem's fixed reported pair. The theorem proves the reported pair differs from the stated correct pair, hence establishes the claimed hand-check but not the broader 0/30 test statistics.

Claim:
- id: ueuclid-incontainer-fails-s1s2-handcheck
- status: formalised
- formalisation: code/lean/ueuclid-incontainer-fails-s1s2-e1947a2b.lean
- statement: ((547 : ℕ), (2551 : ℕ)) ≠ ((426 : ℕ), (1578 : ℕ))
- axioms: propext only
