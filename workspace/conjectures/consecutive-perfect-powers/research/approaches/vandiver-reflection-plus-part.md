# Reflection principle + Vandiver — the other half of the class group

```approach
idea: Attack the class-group obstruction through h^+ and Q(ζ_p)^+ using the reflection principle (Spiegelungssatz) and Vandiver's conjecture: convert the forced q-torsion of Cl^-(Q(ζ_p)) into a simultaneous cross-prime statement, yielding the conditional theorem "p ∤ h^+ ⇒ [strong necessary condition]".
mechanism: the descent forces q | h^-(Q(ζ_p)) and p | h^-(Q(ζ_q)) (currently held only as crossprime-q-hminus-not-sourced). The reflection principle is named as "a Galois-module duality between eigenspaces Cl[ω^k] and Cl[ω^{1−k}], so a q-torsion class in Cl^-(Q(ζ_p)) reflects to a p-torsion class in the mirror — the cross-prime-correct replacement for the refuted same-prime Herbrand–Ribet."
status: refuted
killed-by: same-prime-not-cross-prime (the Spiegelungssatz is a same-conductor-prime statement relating eigenspaces of Cl(Q(ζ_p)) under ω mod p; it does not transfer torsion across two different fields Q(ζ_p), Q(ζ_q), so it cannot deliver the cross-prime forcing q|h^-(Q(ζ_p)) — the very gap `crossprime-q-hminus-not-sourced` it was meant to fill)
precedent: "Reflection principles for class groups", J. Number Theory, https://www.sciencedirect.com/science/article/pii/S0022314X17300732; Lemmermeyer, "Class groups of dihedral extensions", https://doi.org/10.1002/mana.200310263; Leopoldt, "Über den allgemeinen Spiegelungssatz für galoissche Zahlkörper", https://www.sciencedirect.com/science/article/pii/0022314X70900569; Jakubec, "Connection between the Wieferich congruence and divisibility of h^+", https://doi.org/10.4064/aa-71-1-55-64
```

**Literature verdict: REFUTED — the reflection principle is same-prime, not cross-prime. Its own distinguishing claim is a misreading.**

## The precise statement of the reflection theorem (and its scope)

Leopoldt's Spiegelungssatz / Hecke's theorem, in the cyclotomic case (sourced):
- **Hecke/Leopoldt**: for K = Q(ζ_l), l prime, with Cl(K)^± the ±1 eigenspaces of Cl(K) under complex conjugation, `rk_l Cl(K)^+ ≤ rk_l Cl(K)^−`. (Sources: "Reflection principles for class groups", J. Number Theory, https://www.sciencedirect.com/science/article/pii/S0022314X17300732, explicitly giving Hecke's Proposition: `rk_l Cl(K)^+ ≤ rk_l Cl(K)^−` for K=Q(ζ_l); Lemmermeyer, "Class groups of dihedral extensions", https://doi.org/10.1002/mana.200310263, for Kummer's original p|h^+ ⇒ p|h^− and Hecke's refinement.)
- **Eigenspace form**: the l-class group of Q(ζ_l) decomposes under Gal(Q(ζ_l)/Q) ≅ (Z/lZ)^× into eigenspaces `Cl[ω^k]`, and reflection relates `Cl[ω^i]` to `Cl[ω^j]` for the **same** field and the **same** prime l.
- Leopoldt's own generalisation (J. Reine Angew. Math. 199 (1958) 165–174; "Über den allgemeinen Spiegelungssatz für galoissche Zahlkörper", https://www.sciencedirect.com/science/article/pii/0022314X70900569) concerns the l-class group / l-divisor groups of subfields of a **single** Galois l-extension — still same-prime.

## The fatal defect: this is the same-prime statement the run already killed

The canditane's mechanism claims the reflection principle is "the cross-prime-correct replacement for the refuted same-prime Herbrand–Ribet." That is the opposite of what the theorem does. The Teichmüller character ω is the character **modulo p** (the conductor prime); `ω^k` and `ω^{1−k}` are both characters of Gal(Q(ζ_p)/Q). Reflection moves torsion between **eigenspaces of the same cyclotomic class group Cl(Q(ζ_p)) under the same prime p** — it does not transfer a q-torsion class from Cl(Q(ζ_p)) to a p-torsion class of Cl(Q(ζ_q)). There is no "mirror field" and no cross-prime step anywhere in the Spiegelungssatz.

This is exactly the objection that refuted `iwasawa-herbrand-ribet-classgroup`: Herbrand–Ribet is p-torsion of Cl(Q(ζ_p))[p] (same prime). The reflection principle is likewise p-torsion of Cl(Q(ζ_p)) (same prime) — it relates + and − under the same conductor prime. The descent's divisibility `q | h^-(Q(ζ_p))` is **cross-prime** (q ≠ p), and the reflection principle simply has nothing to say about it. The candidate's claim to be the "cross-prime-correct replacement" fails on exactly the same ground, restated.

## What survives

- The *Vandiver / plus-part* ingredient is real and even connected to Wieferich: Jakubec, "Connection between the Wieferich congruence and divisibility of h^+" (Acta Arith. 71 (1995), https://doi.org/10.4064/aa-71-1-55-64) proves, under specific congruence conditions, that q | h^+(Q(ζ_p+ζ_p^{-1})) forces the Wieferich congruence 2^{q−1} ≡ 1 (mod q^2). That is a genuine same-field link between the plus class number of a real cyclotomic field and a Wieferich-type congruence — but it is not a reflection-principle application to the Catalan forcing, and it does not supply the `q|h^-` forcing.
- The run already holds `kummer-vandiver-verified-range` (Vandiver verified to 163M, catalogued) — so "p ∤ h^+" is numerically near-certain, but that only makes the plus part *excise*, it does not manufacture a cross-prime reflection.
- Kummer's classical `p|h^+ ⇒ p|h^-` (same-prime) and Hecke's rank inequality are real, but the descent forces **q**|h^- (cross-prime), so they are inapplicable to the run's gap.

## What to do next

Do not reopen reflection as the cross-prime mechanism. If the plus part is to be used, the honest shape is Jakubec-type: a separate, same-field theorem connecting a cyclotomic plus class number to a Wieferich congruence — but it must be shown (not asserted) how any such theorem bears on a hypothetical solution of x^p−y^q=1, and the `q|h^-` forcing remains `crossprime-q-hminus-not-sourced` and untouched.

precedent: "Reflection principles for class groups", J. Number Theory, https://www.sciencedirect.com/science/article/pii/S0022314X17300732 (Hecke's rk_l Cl^+ ≤ rk_l Cl^−, same-prime); Lemmermeyer, "Class groups of dihedral extensions", https://doi.org/10.1002/mana.200310263; Leopoldt, "Über den allgemeinen Spiegelungssatz für galoissche Zahlkörper", https://www.sciencedirect.com/science/article/pii/0022314X70900569; Jakubec, "Connection between the Wieferich congruence and divisibility of h^+", https://doi.org/10.4064/aa-71-1-55-64.
killed-by: same-prime-not-cross-prime (the Spiegelungssatz is a same-conductor-prime statement relating eigenspaces of Cl(Q(ζ_p)) under ω mod p; it does not transfer torsion across two different fields Q(ζ_p), Q(ζ_q), so it cannot deliver the cross-prime forcing q|h^-(Q(ζ_p)) — the very gap `crossprime-q-hminus-not-sourced` it was meant to fill).
