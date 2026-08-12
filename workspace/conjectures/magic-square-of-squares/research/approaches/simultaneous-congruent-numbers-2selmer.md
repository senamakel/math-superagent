# Approach: Simultaneous congruent numbers and 2-Selmer group arithmetic

```approach
idea: The four three-term APs through the centre (differences u, v, u+v, u-v) each give a congruent-number curve E_d: y² = x³ − d²x. The four curves are not independent — the additive relations among the d's impose multiplicative relations among the corresponding Selmer classes. Non-existence follows if those relations force a rank contradiction in the 2-Selmer group of a composite twist.

mechanism: For each difference d ∈ {u, v, u+v, u-v}, the condition that e² ± d are both squares is equivalent to d being a congruent number with the same scaling e. Concretely, there exist rational points on E_d whose x-coordinates produce the AP. The standard descent lemma: the 2-Selmer group Sel₂(E_d) sits in an exact sequence and its elements correspond to factorisations d = d₁d₂ with d₁x² + d₂y² = z². The four differences satisfy u + v − (u+v) = 0 and u − v − (u−v) = 0. These additive relations induce linear relations in the 2-Selmer groups of the four curves when pulled back to a common étale algebra. If those relations are incompatible with the local solubility (which is everywhere satisfied), then no rational point exists.

This is distinct from Bremner's approach on E: y² = x(x² − c²). Instead of seeking three points in 2E(Q) in arithmetic progression, we study the simultaneous membership of four numbers in the congruent-number set, linked by their additive relations. The four-curve approach turns the problem into a question about the intersection of Selmer conditions, which can be computed via 2-descent on the relevant twist of the associated elliptic surface.

status: proposed
first-step: Write the explicit 2-descent map for each E_d (d = u, v, u+v, u-v) with the same scaling e², derive the linear relations among Sel₂(E_d) classes induced by u + v = (u+v) and u − v = (u−v), and check whether the system has any rational solution compatible with local solubility at all primes.
```