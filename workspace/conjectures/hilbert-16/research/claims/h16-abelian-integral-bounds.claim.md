```claim
id: h16-abelian-integral-bounds
statement: The finite-parameter abstraction of the Abelian-integral zero-count problem: if the parameter space is a finite type and every isolated-zero set is finite, then the cardinalities of the isolated-zero sets have a common natural-number bound. This is the logical uniformity extraction (finite type + pointwise finiteness ⇒ uniform bound) — the checked Lean theorem proves this abstraction, NOT the analytic Abelian-integral theorem itself and not the Binyamini–Dor numerical bound. The analytic content is carried by the companion claims h16-bny-abelian-bound and h16-bd-abelian-linear-in-m.
hypotheses: Parameter is a Fintype; every isolated-zero set is finite; the Lean abstraction is a placeholder interface, so the statement is the logical uniformity principle, not the analytic theorem.
holds-here: yes (as the logical abstraction)
status: formalised
evidence: Lean theorem code/lean/h16_abelian_integral_bounds-0afc0918.lean (kernel-checked).
falsifier: A model of the finite-type + pointwise-finiteness hypotheses with no common bound would falsify the abstraction; the analytic Abelian-integral bound itself is carried by h16-bny-abelian-bound / h16-bd-abelian-linear-in-m.
formalisation: code/lean/h16_abelian_integral_bounds-0afc0918.lean
note: This block previously had no statement, so the entailment ledger could not read it and flagged its dependents as "following from nothing". The statement field is now restored from the formalisation's documented content.
follows-from:
answers:
```
