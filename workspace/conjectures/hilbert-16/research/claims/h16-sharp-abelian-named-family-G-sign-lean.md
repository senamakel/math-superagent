# Claim: h16-sharp-abelian-named-family/G-sign-lean

```claim
id: h16-sharp-abelian-named-family-G-sign-lean
statement: For every finite rational certificate c carrying μ, h₀ > 0, cleared-denominator Wronskian polynomials, and a proof of each indexed finite sign/Sturm condition, h₀ > 0 and every indexed sign/Sturm condition hold.
hypotheses: The binder c carries the finite certificate data and its `sign_certificate`; these are assumptions/data, not independently established for a concrete named family in this file.
holds-here: yes
status: formalised
evidence: kernel-checked by `lean_check`; no sorry; axioms only propext, Classical.choice, Quot.sound.
formalisation: code/lean/h16_sharp_abelian_named_family_G_sign_lean-5d93a1d6.lean
falsifier: A concrete certificate whose supplied sign_certificate is false, or a stronger theorem claiming that this interface itself defines analytic ECT systems or proves the GMV zero bound.
```

The original informal node is stronger than the checked theorem: this file formalises the finite certificate layer only. It does not formalise ECT systems, Abelian integrals, period-annulus ovals, Picard–Fuchs equations, or the cited GMV implication. Those missing analytic bridges remain catalogued rather than papered over.
