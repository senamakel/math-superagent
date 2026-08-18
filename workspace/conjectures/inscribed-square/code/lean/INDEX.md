# Index — code/lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `SanityCyclic.lean` | Kernel-checked sanity lemmas: `CyclicallyOrdered` forces t₁ ≠ t₂ and t₁ ≠ t₃ (pairwise distinctness), so the cyclic-order hypothesis is not degenerate. Verified with no sorry; axioms only propext/Classical.choice/Quot.sound. |
| `aikl2025_coisotropic_c0_rigidity-fe871eba.lean` | Lean formalization of the AIKL 2025 coisotropic C⁰-rigidity statement (node aikl2025-coisotropic-c0-rigidity). The theorem is conditional on the Cited.aikl2025_theorem axiom; predicates are abstract placeholders for the smooth/coisotropic geometry. |
| `matschke2009_mod2_intersection-aec7691d.lean` | Formalizes an abstract conditional version of Matschke 2009 Theorem 2.8; geometric configuration-space objects are intentionally represented by explicit structure fields. |
| `matschke2009_special_trapezoid_criterion-4ca30655.lean` | Conditional Lean encoding of Matschke's special-trapezoid criterion; abstracts the geometric predicates and cites Corollary 2.10/2.12. |
| `matschke2014_stromquist_locally_monotone-7a8aaa95.lean` | Conditional Lean formalisation of the cited Stromquist locally-monotone square-peg theorem; abstracts the geometric predicates and exposes the cited theorem as an axiom. |
| `toeplitz_square_peg_G-membrane_avoids_special_trapezoids-5eec1594.lean` | Typed formalization boundary for the open membrane-avoidance statement; records the exact existence/disjointness proposition while exposing missing geometric definitions. |
| `toeplitz_square_peg_G-nondegeneracy-bound-on-C-eeae5287.lean` | Lean statement of the G-nondegeneracy bound, making the otherwise undefined class, square object, production predicate, and side-length functional explicit; currently an unproved skeleton. |
| `toeplitz_square_peg_G_curve_outside_published_classes-a7681979.lean` | Lean formalization of the exact logical exhibit shape; exposes the missing definitions of C and the three exclusion classes. |
| `toeplitz_square_peg_G_named_class_membrane-77cb53e4.lean` | Formalises the named-class membrane-avoidance implication with explicit parameterised curve, generator, membrane, and special-trapezoid predicates. |
