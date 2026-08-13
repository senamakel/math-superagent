# Hassett & Várilly-Alvarado, "Failure of the Hasse principle on general K3 surfaces"

[[hassett-varilly-alvarado-k3-hasse]]

Source: `https://www.math.brown.edu/bhassett/papers/K3Hasse/K3Hasse10.pdf` (Advances in Math 288 (2016) 436–478). Statements below are the paper's own theorems; section numbers refer to the local full text.

## What it establishes

**Theorem 1.1 (main).** There exists a K3 surface `X₁` of degree 2 over Q — a double cover of P² branched over a smooth plane sextic — together with a **2-torsion Brauer class** `A` (an Azumaya algebra, quaternion `(B²−4AD, A)`) such that:
- `X₁` has **geometric Picard rank 1** (Prop. 5.5, via Elsenhans–Jahnel specialization and tritangent-line data mod 3 / 11);
- `X₁` is locally soluble, `X₁(A_Q) ≠ ∅` (Table 1: explicit Q_p-points at R and all bad primes, by Weil conjectures + search);
- the local invariants are `inv_p A(P) = 0` for all finite p, `inv_∞ A(P) = 1/2` for all real points (Prop. 5.6);
- hence `X₁(A_Q)^A = ∅` while `X₁(A_Q) ≠ ∅`: a **transcendental Brauer–Manin obstruction to the Hasse principle on a K3 surface** (first such unconditional example).

**Why the class is transcendental:** with Pic rank 1, `H¹(Q, Pic) = 1`, so by Hochschild–Serre `Br₁ X = Br₀ X` (constant classes never obstruct); `A` is therefore not algebraic (end of §5.5).

**Blueprint for the run (Thm 1.1 + §3–§4):** for any degree-2 K3 `w² = −½·det(M)` with quadratic forms A,…,F, the quaternion `(B²−4AD, A)` extends to Br(X) (Prop. 3.3); it can ramify **only** at real places, 2-adic places, and primes of bad reduction (Lemmas 4.4, 4.7, Cor. 4.6); at odd bad-reduction primes with < 8 ordinary double points the evaluation is constant (Props 4.1, Lemma 4.2 via Colliot-Thélène–Skorobogatov). The paper's §6 gives the exact **7-step computational certification pipeline** used to construct such (X, A) pairs.

## What it implies here

**Holds-here: machinery, not the surface.** Bremner II's K3 `S` (intersection of three quadrics in P⁵, NS(Q)-rank 12) is not a degree-2 double cover of P², so Theorem 1.1's specific example does not transfer. What transfers:
1. **The transcendental part of Br matters and is computable in practice** — this paper is the existence proof that a BM obstruction on a K3 can be certified unconditionally, and §6 is a ready-made check-list for the adopted `brauer-manin-k3-surface` approach (compute algebra, control ramification, evaluate at local points, point-count for Pic rank).
2. The approach file already notes Br(S)/Br(Q) = algebraic + `Br(S_Q̄)^{Gal}`; this paper's Prop. 4.1/Lemma 4.2 machinery (constant evaluation at mild bad reduction) is exactly what the approach's step 3 needs if S has such fibres.
3. **The "hinge" caution is reinforced but not resolved**: MSS exist over Q(√3) and not (conjecturally) Q — a transcendental class vanishes over a quadratic extension, which is the pattern here; but nothing in this paper constructs such a class for S.

**What it does not settle:** whether Bremner's S admits any nontrivial Br class, algebraic or transcendental; the surface is different (rank-12 NS, not rank-1). No theorem here applies directly; only the method does.

```claim
id: hassett-varilly-alvarado-transcendental-bm-k3
statement: There is an explicit K3 surface X_1/Q of degree 2, geometric
  Picard rank 1, locally soluble, with a 2-torsion Brauer class A whose
  invariants are 0 at all finite places and 1/2 at all real points, giving an
  unconditional transcendental Brauer-Manin obstruction to the Hasse
  principle (X_1(A_Q) != empty, X_1(A_Q)^A = empty).
hypotheses: X_1 the explicit sixth-degree double cover of the paper; class A
  the quaternion (B^2-4AD, A); certification via Elsenhans-Jahnel + CTS
holds-here: no
status: proved
bearing: method template and local-invariant machinery for the adopted
  Brauer-Manin line on Bremner II's S; shows a certified transcendental
  obstruction on a K3 is achievable in practice; the magic-square K3 S is a
  different surface (NS-rank 12, not this rank-1 double cover), so the
  theorem does not transfer directly
anchor: research/sources/hassett-varilly-alvarado-k3-hasse.full.md
```

**Does not help directly**: it is not a reduction of the magic-square problem; it is the state-of-the-art toolkit for the approach that is currently adopted. Recorded as such so nobody re-reads the 65k-char text for a magic-square statement that is not there.