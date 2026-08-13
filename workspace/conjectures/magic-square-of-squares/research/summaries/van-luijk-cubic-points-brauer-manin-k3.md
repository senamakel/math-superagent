# Van Luijk, "Cubic points on cubic curves and the Brauer-Manin obstruction on K3 surfaces"

[[van-luijk-cubic-points-brauer-manin-k3]]

Source: `https://pub.math.leidenuniv.nl/~luijkrmvan/cubics/cubics.pdf` (preprint, Simon Fraser / Leiden). All statements below are from the paper's own proofs.

## What it establishes

**Construction.** For a smooth plane cubic `C` over a number field `k`, form `X = (C×C)/ρ` where `ρ(P,Q) = (Q,R)`, `P,Q,R` collinear on `C` (order-3 automorphism). `X` has 9 A₂ double points; its minimal resolution `Y` is a **K3 surface** (Prop. 2.2).

- **Y has a k-point iff C contains three collinear points defined over some Galois (Z/3Z)-extension of k** ("k-cubic points"), permuted transitively by Gal(l/k) (Lemmas 2.5, 2.7). So if C is locally soluble but has no k-cubic points, Y is a **counterexample to the Hasse principle on a K3** (Cor. 2.8, Thm 1.1).
- **Transcendental-lattice fact** (Prop. 3.9): `T_Y ≅ T_{C×C}(3)`. For diagonal cubics `ax³+by³+cz³=0`: `rk NS(Y) = 20` with **disc NS(Y) = −27** (Prop. 4.1), and if `abc` is not a cube in `k` then **H¹(k, Pic Ȳ) = {1}** (Prop. 4.2).
- **Proof of Thm 1.1**: when `H¹(k, Pic) = 1`, the Hochschild–Serre sequence gives `Br₁ Y = im Br k`, so the *algebraic* Brauer–Manin set `Y(A_k)^{Br₁} ≠ ∅` — i.e. **for this K3 the algebraic Brauer group does not obstruct** — while `Y(k) = ∅`. Conclusion (exact quote of abstract): "the algebraic part of the Brauer-Manin obstruction is not the only obstruction to the Hasse principle for K3 surfaces", *conditional on the existence of such a cubic*. Whether any cubic with these three properties exists (i.e. the third condition actually holds) is **open** (the Selmer curve `3x³+4y³+5z³=0` fails condition 3 — its collinear triples are Q-cubic points, found explicitly).
- Open Questions 1–3: existence of such a cubic, existence of a *diagonal* one, and whether BM is the only obstruction for K3 surfaces.

## What it implies here

**Holds-here: no — the central conditional is unfulfilled**, and more importantly the surface `Y` is a *different* K3 (a rational quotient of a self-product of a cubic, NS-rank 20 discriminant −27) unrelated to Bremner II's intersection-of-three-quadrics K3 `S: T²+U²=V²+W²=X²+Y², TU+VW+XY=0` (NS(Q)-rank 12). Mapping: the *method* this run's adopted Brauer–Manin approach needs — prove `S(Q)=∅` via an element of Br(S)/Br(Q) with constant nonzero evaluation — is exactly the kind of "alone not sufficient + algebraic part trivial doesn't preclude transcendental" landscape this paper maps, but **no theorem here endows Bremner's S with a nontrivial Br class or controls its evaluations**. The paper's conditional Theorem 1.1 does not apply: nothing here produces a cubic with conditions (1)–(3).

**What it rules out / cautions:** the "hinge" in CONTEXT.md (MSS exist over Q(√3) but not Q ⇒ BM obstruction vanishing upon base change) must fight the Wu result below and this paper's Open Question 3 — for K3s it is *not established* that BM explains all Hasse failures, so a bare computational "no BM obstruction" would prove nothing either way.

```claim
id: van-luijk-algebraic-br-not-sufficient-on-k3s
statement: If a smooth diagonal plane cubic a x^3 + b y^3 + c z^3 = 0 over a
  number field has local points everywhere, has no k-cubic points (three
  collinear points over a Galois Z/3Z extension), and abc is not a cube, then
  the K3 Y = min-res(CxC/rho) satisfies Y(A_k)^{Br_1 Y} != empty and Y(k) = empty:
  the algebraic Brauer-Manin obstruction is not the only one for K3 surfaces.
hypotheses: existence of such a cubic is OPEN (Selmer curve fails); Y is the
  cubic-quotient K3, not Bremner II's surface S
holds-here: no
status: proved (as a theorem conditional on the open existence hypothesis)
bearing: maps the limits of algebraic-Brauer arguments on K3s; the run's K3
  is a different surface, so the theorem neither applies nor obstructs the
  adopted Brauer-Manin line; reinforces that a transcendental class is needed
anchor: research/sources/van-luijk-cubic-points-brauer-manin-k3.full.md
```

This source **does not establish** anything about the magic-square K3 directly — it is methodology terrain for the adopted approach, and its conditional result is undischarged. Filed under the brauer-manin thread for the record.