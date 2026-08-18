```claim
id: matschke2009-mod2-intersection-formalisation
statement: For an abstract data package containing a square-free predicate, generator predicate, mod-2 intersection function, and the asserted parity theorem, a square-free curve and generator path have intersection value true.
status: formalised
evidence: Lean kernel
formalisation: code/lean/matschke2009_mod2_intersection-aec7691d.lean
hypotheses: D.parity_theorem is the encoded geometric/parity result; hγ carries “γ does not inscribe a square”; hω carries “ω represents a generator”; the conclusion `intersection γ ω = true` encodes mod-2 intersection number 1.
limitations: This is not a formalization of the actual topology or the isomorphism π₁((S¹)²\Δ) ≅ ℤ. Those objects are abstract fields, and the parity theorem is an input field. Thus the Lean theorem checks the logical reduction, not Matschke's geometric theorem itself.
```