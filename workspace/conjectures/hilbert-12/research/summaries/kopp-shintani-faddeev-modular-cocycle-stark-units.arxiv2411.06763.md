> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/kopp-shintani-faddeev-modular-cocycle-stark-units.arxiv2411.06763.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2411.06763 | converted from PDF -->

## What it claims

Abstract. We give a new interpretation of Stark units associated to real quadratic fields
as real multiplication values of a modular cocycle. The cocycle of interest is a meromorphic
factor describing the modular transformations of the q-Pochhammer symbol and is related to
the Shintani–Barnes double sine function and the Faddeev quantum dilogarithm. We prove
a refinement of Shintani’s Kronecker limit formula that relates square roots of Stark class
invariants to real multiplication values of the cocycle, which are cohomological invariants.

Contents

1. Introduction 2
1.1. The Shintani–Faddeev Jacobi and modular cocycles 3
1.2. Partial zeta functions and the Stark conjectures 4
1.3. Eta-multiplier and theta-multiplier characters 5
1.4. Main result: a limit formula 6
1.5. Conditional results and conjectures: algebraicity 7
1.6. Prior work 8
1.7. Applications and future work 9
1.8. Structure of this paper 9
1.9. List of notation 10
2. Preliminaries on q-Pochhammer symbols and half-integral weight modular forms 11
2.1. SL2 and the standard symplectic form 11
2.2. Fractional linear…

Dat…

## Statements it makes

Theorem 1.1. Let O be an order in a real quadratic field F ⊂ R, with Galois conjugation
map x ↦→ x′, and let m be a nonzero O-ideal. Let A ∈ Clm
♭
m∞2(O) \ ZClm
♭
m,Σ(O), let A0 be
the class of A in Cl(O), choose some b ∈ A
−1
0 coprime to m, and write bm = α(βZ + Z) for
some α, β ∈ F such that α is totally positive and β > β′. Choose r = ( r1
r2 ) ∈ Q
2 such that
α(r2β − r1)O ∈ bA and r2β′ − r1 > 0. Write

Corollary 1.2. If β is a real quadratic number, r ∈ Q
2, and

Theorem 1.3. Assume Conjecture 6.9 (a consequence of Tate’s refinement of the Stark
conjectures). Let β ∈ R such that aβ2 + bβ + c = 0 with a, b, c ∈ Z, b2 − 4ac not a square,
and let r ∈ Q
2.
(1) There exists some n ∈ N such that שr[β]
n is an algebraic unit in an abelian extension
of F = Q(β).

Conjecture 1.4. If β ∈ R such that aβ2 + bβ + c = 0 with a, b, c ∈ Z, b2 − 4ac not a square,
and r ∈ Q2, then ש
r[β] is an algebraic unit in an abelian extension of Q(β). Moreover, if
m is an O-invertible ideal such that (r, β) ∈ MO,m in the notation of Theorem 3.14, then
ס
r[β] ∈ Hm∞2.

Definition 2.1. The finite q-Pochhammer symbol is

Definition 2.2. The infinite q-Pochhammer symbol is defined for w, q ∈ C with |q| < 1 by

Lemma 2.3. If z ∈ C, τ ∈ H, and m, n ∈ Z, then

Theorem 2.4. Let A = ( a b
c d ) ∈ SL2(Z) and τ ∈ H. If c = 0, then

Definition 2.5. For z ∈ C and τ ∈ H, the first Jacobi theta function is

Theorem 2.6. If z ∈ C, τ ∈ H, and k, ℓ ∈ Z, then

Theorem 2.7. If z ∈ C, τ ∈ H, and (A, ϵ) ∈ Mp2(Z) with A = ( a b
c d ), then

Definition 2.8. For r = ( r1
r2 ) ∈ R2, z ∈ C, and τ ∈ H, the Jacobi theta function with
characteristics is

Proposition 2.9. Let r = ( r1
r2 ) ∈ R
2, m = ( m1
m2 ) ∈ Z2, z ∈ C, and τ ∈ H. Then

Theorem 2.10. Let r = ( r1
r2 ) ∈ R
2, z ∈ C, τ ∈ H, and (A, ϵ) ∈ Mp2(Z) with A = ( a b
c d ).
Then ϑAr(A · (z, τ )) = ψ(A, ϵ)3κ(A, r)e
( cz2
2(cτ +d) ) ϵ(τ )ϑr(z, τ ), (2.8)

Lemma 2.11. Let r ∈ Q
2. The function κ satisfies the following cocycle condition: For any
A, B ∈ Γr, κ(AB, r) = κ(A, Br)κ(B, r).

Lemma 2.12. Let r = ( r1
r2 ) ∈ R
2 and A = ( a b
c d ) ∈ SL2(Z). With κ(A, r) defined as in
Theorem 2.10,
 κ(A, A
−1r) = κ(A−1, r)
−1

Definition 2.13. Let r ∈ R2, τ ∈ H. The theta null with characteristics is

Theorem 2.14. Let r ∈ Q
2. The function θr(τ ) is a weight 1
2 modular form with character
for the group MΓr = {(A, ϵ) ∈ Mp2(Z) : A · r ≡ r (mod 1)}.

Lemma 2.15. Let r ∈ 1
N Z
2 for N ∈ N. The character χr on Γr has the following formula.

Lemma 2.16. Let r ∈ Q
2. For any m ∈ Z
2 and any A ∈ Γr,

Theorem 2.18. If w, q ∈ C with |q| < 1, then

Proposition 2.19. If z ∈ C and τ ∈ H, then

Proposition 2.20. If r ∈ R
2, z ∈ C, and τ ∈ H, let

Definition 3.1. The ray class group of the order O modulo (m, Σ) is

Definition 3.2. For a commutative ring with unity R and an ideal I of R, define the group

Theorem 3.3. Let F be a number field and O ⊆ O′ ⊆ OF be orders…


*[further statements in the full text]*

*[digest of a 202443 character source; every section, statement, and proof in full at `research/sources/kopp-shintani-faddeev-modular-cocycle-stark-units.arxiv2411.06763.full.md`]*
