# Claim: h16-sharp-abelian-named-family/G-ect-apply

```claim
id: h16-sharp-abelian-named-family-G-ect-apply
statement: For supplied exact data for the named family, the balance chain and Wronskians agree entrywise with explicit rational functions over Q, and every finite sign/nonvanishing/Sturm certificate holds.
status: formalised
formalisation: code/lean/h16_sharp_abelian_named_family_G_ect_apply-c816737f.lean
```

This formalisation carries the original hypotheses as the structure `ECTApplicationData d`: `μ`, rational endpoint `h₀` and positivity; `chain` and `wronskians`; explicit rational functions; finite conditions; exact-chain and exact-Wronskian equalities; and the finite certificate. The theorem proves only the finite conjunction from these supplied fields. It does not compute the Yang family data or prove those fields for a concrete family. The kernel verdict is verified with no sorry and axioms `propext`, `Quot.sound`.
