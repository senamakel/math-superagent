<!-- source: https://arxiv.org/pdf/2411.06763 | converted from PDF -->

THE SHINTANI–FADDEEV MODULAR COCYCLE: STARK UNITS
FROM q-POCHHAMMER RATIOS

GENE S. KOPP

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
2.2. Fractional linear transformations 11
2.3. The covering groups ˜SL2(R) and Mp2(R) 12
2.4. The q-Pochhammer symbol and variants 13
2.5. The Dedekind eta function and its logarithm 14
2.6. Jacobi theta functions with characteristics 15
2.7. Characters of modular theta functions 17
2.8. The Jacobi triple product formula 20
2.9. Modular specializations of the q-Pochhamer symbol 21
3. On moduli spaces of ray class data 21
3.1. Ray class groups and ray class fields of orders 22
3.2. The flat imprimitive ray class monoid 23
3.3. Key properties of orders 25

Date: May 2, 2025.
2020 Mathematics Subject Classification. 11R37 (primary), 11F37, 11F67, 11R27, 11R42, 11R54
(secondary).
Key words and phrases. Stark conjectures, real quadratic field, double sine function, double gamma func-
tion, noncompact quantum dilogarithm, q-Pochhammer symbol, meromorphic modular cocycle, holomorphic
quantum modular form, ray class field, non-maximal order, partial zeta function, Hilbert’s 12th problem.
1arXiv:2411.06763v3  [math.NT]  3 May 2025
2 GENE S. KOPP

3.4. The main correspondence 26
4. Modular properties of the q-Pochhammer symbol 31
4.1. A working definition for first cohomology 31
4.2. Modular and Jacobi cocycles 32
4.3. Cocycles as generalized modular weights 32
4.4. Stable values and real multiplication values of modular cocycles 33
4.5. Stable values and real multiplication values of Jacobi cocycles 35
4.6. The Shintani–Faddeev cocycles 37
4.7. The Shintani–Faddeev modular cocycle with half-integral characteristics 38
4.8. The double sine function 40
4.9. Multiplicative quantum modularity of the q-Pochhammer symbol 42
4.10. Functional equations of the Shintani–Faddeev cocycles 43
4.11. Values at rational τ and quantum modularity 45
4.12. Special properties of the Shintani–Faddeev cocycle at real multiplication points 46
4.13. Conductor-lowering/level-raising relations 49
5. Cohomological interpretations of the Shintani–Faddeev cocycles 52
5.1. Generalized first group cohomology 52
5.2. Equivariant (Q, V )-cohomology of Γ-sheaves 53
5.3. From the working definition to equivariant (Q, V )-cohomology 56
6. Partial zeta functions 58
6.1. Ray class partial zeta functions 58
6.2. Ideal coset partial zeta functions 59
6.3. Equivalence of partial zeta functions 59
6.4. Galois-theoretic partial zeta functions 60
6.5. The rank 1 abelian Stark–Tate conjecture 60
7. Partial zeta functions at s = 0 and continued fractions 62
7.1. Hirzebruch–Jung continued fractions 62
7.2. Shintani’s limit formula and Stark–Tangedal–Yamamoto class invariants 66
7.3. Telescoping the product 71
7.4. The global phase factor 74
7.5. The r-dependent phase factor 75
8. Culmination of proofs of main theorems and concluding remarks 76
8.1. Completing the proof of Theorem 1.1 76
8.2. Stark units and conditional results 78
8.3. Example 79
8.4. Asymptotics of the q-Pochhammer symbol 79
9. Typesetting note 80
10. Acknowledgments 81
References 82

1. Introduction

In the theory of singular moduli, special values of modular functions generate abelian
Galois extensions of imaginary quadratic fields. Such modular functions may be speci-
fied as ratios of products of q-Pochhammer symbols (for example, eta quotients and theta

THE SHINTANI–FADDEEV MODULAR COCYCLE 3

quotients)—in particular, theta quotients yield elliptic units. In this paper, we prove that
certain other ratios of q-Pochhammer symbols meromorphically continue as a function of τ
(with q = e
2πiτ ) to a region that includes an open subset of the real line, where their special
values at real quadratic points are closely related to certain special values of L-functions at
s = 0. Then, under the assumption of a version of the Stark conjectures, limiting ratios of
q-Pochhammer symbols generate abelian extensions of real quadratic fields.
The central objects of interest are the Shintani–Faddeev Jacobi cocycle (m, A) ↦→ σm,A(z, τ )
and the closely related Shintani–Faddeev modular cocycle (with characteristics r) A ↦→
ש
r
A(τ ).
1 The Shintani–Faddeev Jacobi cocycle is a mapping from the Jacobi group Z
2⋊SL2(Z)
to complex meromorphic functions that serves as a generalized factor of automorphy describ-
ing the modular transformation law of the q-Pochhammer symbol. The function σm,A(z, τ )
has been identified by Dimofte (in a slightly different form) as a partition function of a
certain topological quantum field theory on a squashed lens space [24]. It has been called
both the rarefied hyperbolic gamma function and the generalized noncompact quantum dilog-
arithm by Sarkissian and Spiridonov [60]; it has also been studied by Garoufalidis and
Wheeler [30] and Wheeler [76]. It generalizes the Shintani’s double sine function [65, 66]
(named by Kurokawa [46]), which was rediscovered by Faddeev [25] and is called the non-
compact quantum dilogarithm in the physics literature. Our name—the Shintaini–Faddeev
Jacobi cocycle—was chosen to emphasize the basic algebraic role of the function (as a mero-
morphic cocycle for the Jacobi group) and its dual history (and importance) in number
theory and physics.
Our main theorem, Theorem 1.1, expresses a Stark class invariant as the square of a real
multiplication (RM) value of the Shintani–Faddeev modular cocycle (or equivalently, an RM
value of the Shintani–Faddeev Jacobi cocycle), up to an explicit root of unity. The Stark
class invariant is the value exp(−Z ′
A(0)) for a Dirichlet series ZA(s) that is defined as the
difference of two ray class partial zeta functions of a real quadratic field F . Stark conjectured
that the value exp(−Z ′
A(0)) is an algebraic unit in an abelian extension of F [71–73]. Tate’s
refinement of Stark’s conjectures includes the further prediction that the square root of this
invariant is in an abelian extension of F [75]. The square roots we obtain from RM values of
ש
r are sometimes positive and sometimes negative, and the sign defines a new class invariant.
The sign plays a key role in an application to quantum information theory, the construction of
symmetric, informationally complete, positive operator-valued measures (SIC-POVMs) [2].

1.1. The Shintani–Faddeev Jacobi and modular cocycles. Before stating our main
theorems, we give a short, self-contained description of the transcendental functions of in-
terest. Here and throughout the paper, we use the notation e(z) := e
2πiz for the complex
exponential.
For m = ( m1
m2 ) ∈ Q
2 and A = ( a b
c d ) ∈ SL2(Z), we will consider the following infinite
product defined for (z, τ ) ∈ C × H:

σm,A(z, τ ) =
 ∞∏

k=0
 1 − e( z
cτ +d + (m2 + k) aτ +b
cτ +d − m1)

1 − e(z + kτ ) .

This product will often be written as a ratio of two infinite q-Pochhammer symbols

σm,A(z, τ ) =
 (e
( z
cτ +d + m2 aτ +b
cτ +d − m1) , e( aτ +b
cτ +d ))
∞
(e(z) , e(τ ))∞ ,

1The notation ש
r
A(τ ) uses the Hebrew letter shin. See Section 9 for typesetting information.

4 GENE S. KOPP

using the notation (w, q)∞ = ∏∞
k=0(1−wqk). We will also write σm,A(z, τ ) for a meromorphic
continuation of this function, and we will interpret

σm,A(z0, τ ) = lim
z→z0 σm,A(z, τ )

when necessary, for example, when there are zeros in the numerator and denominator of the
product formula.
The Shintani–Faddeev Jacobi cocycle is the function from Z
2 ⋊ SL2(Z) to a space of mero-
morphic functions given2 by (m, A) ↦→ σm,A. For (m, A) ∈ Z
2 ⋊ SL2(Z), the function
σm,A(z, τ ) has a meromorphic continuation to the domain C × DA, where

DA =
 



C \ (−∞, −d/c] if c > 0,
C if c = 0 and d > 0,
H if c = 0 and d < 0,
C \ [−d/c, ∞) if c < 0.

Let r ∈ Q2, and consider the congruence group

Γr = {A ∈ SL2(Z) : Ar − r ∈ Z
2}.

Define the “shin” function to be
 ש
r
A(τ ) = σr,A(0, τ );

it continues meromorphically to τ ∈ DA. The Shintani–Faddeev modular cocycle is the
function from Γr to a space of meromorphic functions given by A ↦→ שA.

1.2. Partial zeta functions and the Stark conjectures. We now describe the definitions
of the ray class groups and zeta functions needed for the statement of the main theorem.
Let F be a number field and O be an order in F . Let m be an ideal of O and Σ a subset
of the set of real embeddings of F . The following algebraic structures are defined in [43, 44]
and generalize the standard definitions from class field theory to arbitrary orders.
The ray class group of the order O modulo (m, Σ) is

Clm,Σ(O) = J
∗
m(O)
Pm,Σ(O),

where
 J∗
m(O) = {invertible fractional ideals of O coprime to m}, and

Pm,Σ(O) = {αO such that α ≡ 1 (mod m) and ρ(α) > 0 for ρ ∈ Σ}.

The flat imprimitive ray class monoid is

Clm
♭
m,Σ(O) = J♭
m(O)
∼m,Σ ,

where
 J♭
m(O) = {a ∈ J∗
O(O) : aO[S−1
m ] ⊆ O[S−1
m ]} with

Sm = {α ∈ O : αO + m = O},

2For m ∈ Z
2, σm,A does not depend on m1 (but does depend on m2); indeed, this vestigial variable
does not appear in treatments [24, 60]. We keep it for bookkeeping purposes, to emphasize the Jacobi group
action.
 THE SHINTANI–FADDEEV MODULAR COCYCLE 5

and the equivalence relation ∼m,Σ is defined by

a ∼m,Σ b ⇐⇒ ∃c ∈ J
♭
m(O) and α, β ∈ O[S−1
m ] such that a = αc, b = βc,
α − β ∈ mO[S−1
m ], sgn(ρ(α)) = sgn(ρ(β)) for all ρ ∈ Σ.

The submonoid of zero classes is

ZClm
♭
m,Σ(O) = {[d] ∈ Clm
♭
m,Σ(O) : d ⊆ m}.

If the real embeddings of F are labeled ρ1, . . . , ρr and Σ = {ρj1, . . . , ρjk}, the pair (m, Σ)
may be abbreviated as m∞j1 · · · ∞jk.
Let A ∈ Clm
♭
m,Σ(O), and let R be the element of Clm,Σ(O) defined by

R := {αO : α ≡ −1 (mod m) and ρ(α) > 0 for all ρ ∈ Σ}.

For Re(s) > 1, define the ray class partial zeta function and the differenced ray class partial
zeta function, respectively, by

ζm,Σ(s, A) = ∑

a∈A Nm(a)
−s, and

Zm,Σ(s, A) = ζm,Σ(s, A) − ζm,Σ(s, RA).

The Takagi existence theorem associates to the ray class group Clm,Σ(OF ) a ray class field.
This correspondence is extended to nonmaximal orders by [44, Thm. 1.1], which associates to
Clm,Σ(OF ) the ray class field H O
m,Σ of O modulo (m, Σ), a particular abelian Galois extension
of F with certain properties.
A famous series of conjectures of Stark connects the leading term of the Taylor series
expansion of partial zeta functions at s = 1 to units in abelian extensions. More generally,
the Stark conjectures describe generalized regulators for Artin L-functions of possibly non-
abelian Galois extensions [69–73]. The present paper is concerned only with the rank 1 Stark
conjecture in the abelian case with real quadratic base field.
For a real quadratic field F and A ∈ Clm∞2(OF ), the Stark conjectures predict that the
real number exp(−Z ′
m∞2(0, A))

is an algebraic unit εA. Except in trivial cases (when exp(−Z ′
m∞2(0, A)) = εA = 1), Stark
conjectured that H OF
m∞2 = F (εA). He also conjectured a compatibility with the Artin map:
(Art(A))(εid) = εA. Tate’s refinement of the Stark conjectures [75] includes the claim that
F (ε1/2
A ) is abelian over F , which he attributes to Stark.

1.3. Eta-multiplier and theta-multiplier characters. The Shintani–Faddeev cocycles
are intimately connected to the Dedekind eta function and Jacobi theta functions, which
are half-integral weight modular forms with character. The properties of these functions are
reviewed in Section 2. For now, we describe their characters briefly in order to state the
main theorem.
For τ ∈ H, the Dedekind eta function is

η(τ ) = e
( τ
24
) ∞∏

k=1 (1 − e(kτ )) .

6 GENE S. KOPP

Under the fractional linear transformation action A · τ = aτ +b
cτ +d of A = ( a b
c d ) ∈ SL2(Z), the
eta function transforms by

η( aτ + b
cτ + d
) = ψ(A, √
cτ + d) √cτ + d η(τ ).

Here ψ is a character of the metaplectic group (see Section 2.3) taking values is the group
of complex roots of unity µ∞(C). (In fact, its values are all 24-th roots of unity.) Its square
is a bona fide character of the modular group: ψ2 : SL2(Z) → µ∞(C). A formula for ψ due
to Rademacher is given as Theorem 2.4.
For r = ( r1
r2 ) ∈ Q
2 and τ ∈ H, the Jacobi theta function with characteristics r is

θr(τ ) =
 ∞∑

n=−∞ e( 1
2 (
n + r2 + 1
2)2 τ + (
n + r2 + 1
2) (
−r1 + 1
2)) .

Under the fractional linear transformation action of A = ( a b
c d ) ∈ Γr, this theta function
transforms by
 θr(A · τ ) = ψ(A, √cτ + d)3 χr(A)
√cτ + d θr(τ ). (1.1)

The character χr : Γr → µ∞(C) is given by the formula

χr(A) := −(−1)
δ2(Ar−r)e
(−1
2 det
(Ar r)) , where (1.2)

δ2(q) :=
 {
1, if q ∈ 2Z2,
0, if q /∈ 2Z2.

For proofs of (1.1) and (1.2), see Theorem 2.14 and Lemma 2.15.

1.4. Main result: a limit formula. The main theorem relates a generalized “Sark class
invariant” exp(Z ′
m∞2(0, A)) to a limit of ratios of q-Pochhammer symbols. It may be consid-
ered a refinement of Shintani’s Kronecker limit formula in the real quadratic case [65]. Its
statement does not require Shintani decomposition or continued fractions.

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

{B ∈ Γr : B · β = β} = ⟨A⟩ or ⟨−I, A⟩

with A ( β
1 ) = λ ( β
1 ) for λ > 1. Let n = 2
|ϕ−1(A)|, where ϕ : Clm
♭
m∞1∞2(O) → Clm
♭
m∞2(O) is
the natural quotient map. Then

exp
(
nZ ′
m∞2(0, A)) = (ψ−2χ
−1
r )(A) ש
r
A(β)
2 , (1.3)

where שr denotes the Shintani–Faddeev modular cocycle. Explicitly, the value

שr
A(β) = lim
y→0+ ( ̃wy, ̃qy)∞
(wy, qy)∞ = lim
y→0+
 ∞∏

k=0
 1 − ̃wy ̃qk
y
1 − wyqk
y ,

where the parameters in the product are qy = e(β + yi), wy = e(r2(β + yi) − r1)), ̃qy =
e(A · (β + yi)), and ̃wy = e(r2(A · (β + yi)) − r1).

THE SHINTANI–FADDEEV MODULAR COCYCLE 7

The proof of Theorem 1.1 relies on most of the lemmas in the paper and will be completed
in Section 8.1. The key idea of the proof is to use the cocycle condition to “telescope” a
variant of Shintani’s formula based on a continued fraction expansion.
The statement of Theorem 1.1 could be made slicker in several ways, at the expense of
hiding some of the complexity behind further definitions.
• The value שr
A(τ ) in Theorem 1.1 is a real multiplication (RM) value of the cocycle ש
r,
as defined in Section 4.4. It may be written as

שr[β] := שr
A(τ ) ,

as it only depends on the real quadratic number β. Indeed, it also depends only on
the class of שr in a certain cohomology group.
• The RM values of the Jacobi cocycle coincide with those of the modular cocycle:

σ[r2β − r1, β] = ש
r[β],

although this equivalence hides a shift in the elliptic variable in the definition of
the RM value. Thus, Theorem 1.1 may also be understood as a result about the
RM values of Shintani–Faddeev Jacobi cocycle. From this perspective, the theorem
exhibits all Stark class invariants of ray class fields over real quadratic fields as RM
values of a single object, the Jacobi cocycle σ.
• The characters could be absorbed into the definition of either the modular or the
Jacobi cocycle. In particular, if one defines the “samech cocycle” to be

סr
A(τ ) = (ψ−2χ
−1
r )(A) שr
A(τ )
2 ,

then (1.3) becomes exp
(
nZ ′
m∞2(0, A)) = סr[β],
and the matrix A may be left out of the theorem statement.
We give a corollary to Theorem 1.1 that is particularly essential to the construction of
SIC-POVMs in [2].

Corollary 1.2. If β is a real quadratic number, r ∈ Q
2, and

{B ∈ Γr : B · β = β} = ⟨A⟩ or ⟨−I, A⟩

such that A ( λ
1 ) = λ ( β
1 ) for λ > 1, then ס
r[β] = (ψ−2χ
−1
r )(A) ש
r
A(β)
2 is a positive real
number.

Proof. By Theorem 3.14, every such pair (r, β) corresponds to some A ∈ Clm
♭
m∞2(O) in the
manner of Theorem 1.1. Since Z ′
m∞2(0, A) ∈ R, it follows from (1.3) that (ψ−2χ
−1
r )(A) ש
r
A(β)2

is a positive real number. □

1.5. Conditional results and conjectures: algebraicity. If one assumes an appropriate
version of a Stark conjecture, our main theorem implies that the RM values of the Shintani–
Faddeev cocycle lie in abelian extensions of real quadratic fields, at least in the maximal
order case.

Theorem 1.3. Assume Conjecture 6.9 (a consequence of Tate’s refinement of the Stark
conjectures). Let β ∈ R such that aβ2 + bβ + c = 0 with a, b, c ∈ Z, b2 − 4ac not a square,
and let r ∈ Q
2.
(1) There exists some n ∈ N such that שr[β]
n is an algebraic unit in an abelian extension
of F = Q(β).

8 GENE S. KOPP

(2) If b2 − 4ac is a fundamental discriminant, then we may take n = 1. Moreover, if
c = βZ + Z, and m is the kernel of the OF -module map OF → ((r2β − r1)OF + c)/c
given by 1 ↦→ r2β − r1, then ס
r[β] ∈ Hm∞2.

We conjecture that the assumption in Theorem 1.3(2) that the discriminant is fundamental
(equivalently, that (βZ + Z : βZ + Z) = OF ) is unnecessary. It is not clear whether that
conjecture, stated below as Conjecture 1.4, follows from the Stark conjectures and their
existing refinements. Obstructions to proving this include discrepancies in Euler factors
between “Galois-theoretic” and “ray class-theoretic” L-functions in the non-maximal order
case, as well as the failure of some pairs (r, β) to be in the image of primitive classes under
any of the maps Υm in Theorem 3.14. Numerical evidence for Conjecture 1.4 is given in [2].

Conjecture 1.4. If β ∈ R such that aβ2 + bβ + c = 0 with a, b, c ∈ Z, b2 − 4ac not a square,
and r ∈ Q2, then ש
r[β] is an algebraic unit in an abelian extension of Q(β). Moreover, if
m is an O-invertible ideal such that (r, β) ∈ MO,m in the notation of Theorem 3.14, then
ס
r[β] ∈ Hm∞2.

In addition to these results and conjectures, it is natural to ask for:

(1) a precise description of the field generated by √סr[β] = √
(ψ−2χ−1
r )(A) ש
r
A(β), as a
ray class field or a subfield thereof, and
(2) an analogue of the Shimura reciprocity law, that is, a complete description of the
action of Gal(Q/Q(β)) on the values שr[β].

It is possible to deduce a Shimura reciprocity law for the squares שr[β]
2, in the fundamental
discriminant case, from the Stark conjectures and the results of the present paper. How-
ever, we are hopeful that the study of SIC-POVMs and related objects will help produce
conjectural answers to (1) and (2), and we postpone these lines of inquiry to future work.

1.6. Prior work. The function σm,A(z, τ ) defining the Shintani–Faddeev Jacobi cocycle is
studied under other names by Dimofte [24] and Sarkissian and Spiridonov [60] in mathe-
matical physics and by Garoufalidis and Wheeler [30] and Wheeler [76] in the context of
low-dimensional topology and quantum modularity, with Chern–Simons theory playing a
central role for both sets of authors.
Yamamoto first suggested that Shintani’s formula for the Stark unit would “telescope”
down to a limit of an absolute value of a ratio of q-Pochhammer symbols, showing this in one
example and suggesting that the general case could be handled using continued fractions [79].
Our Theorem 1.1 brings Yamamoto’s idea to its fulfillment while also removing the absolute
value and giving a cocycle interpretation.
The present author has previously given another limit formula for ray class partial zeta
function of real quadratic fields that also does not require Shintani decomposition or con-
tinued fractions [42]. That formula, which is substantially more complicated, relied on a
different continuous interpolation of the arithmetic zeta functions, using Mellin transforms
of non-holomorphic indefinite theta functions.
Outside of the lines of research opened by Shintani and Faddeev, variants of the double
sine function have appeared in other areas of mathematics. One such variant is the quantum
exponential function in the theory of quantum groups; see Woronowicz [77]. A related
function also appears in the work of Malyuzhinets on wave diffration in a wedge-shaped
region; see the review [55] and the references therein.

THE SHINTANI–FADDEEV MODULAR COCYCLE 9

Several constructions in the number theory literature have both similar names and an
indirect mathematical relationship to the Shintani–Faddeev cocycles. The Shintani cocycle
constructed by Solomon [67, 68] is a cocycle for SL2(Z) (or, with appropriate modification,
GL2(Q)) valued in power series that may be used to evaluate ray class zeta functions of real
quadratic fields at nonpositive integers; Hill’s generalization applies to totally real fields [33].
Sczech’s Eisenstein cocycle [15,16,61] is related to the Shintani cocycle but encodes Shintani’s
Kronecker formula for the derivative of a ray class partial zeta function of a totally real field at
s = 0 by means of an integration pairing with cycles. The Shintani and Eisenstein cocycles
allow for p-adic interpolation, and the Eisenstein cocycle plays an important role in the
work of Dasgupta, Kakde, and Ventullo on the Gross–Stark and Brumer–Stark conjectures
[21–23]. The rigid meromorphic cocycles of Darmon and Vonk [19, 20] (and, in particular,
the Dedekind–Rademacher cocycle) are p-adic rigid meromorphic modular 1-cocycles for
SL2(Z
[ 1
p ]) whose real multiplication values are conjectured (and in some cases, proven)
to be algebraic numbers in abelian extensions of a real quadratic field. Finally, papers of
Radchenko and Zagier [58] and Choie and Kumar [17] discuss (but do not formalize) a cocycle
interpretation of the Herglotz–Zagier function, which (conjecutrally) produces rank 2 Stark
regulators in the real quadratic case.

1.7. Applications and future work. Work of Marcus Appleby, Steven Flammia, and the
author uses the Shintani–Faddeev modular cocycle as part of a conjectural construction of
symmetrically complete positive operator-valued measures (SIC-POVMs) [2]. The Shintani–
Faddeev modular cocycle provides the “correct” signed square roots of the Stark units needed
to extend the present author’s previous results on the problem [41] to arbitrary dimension.
The construction of SIC-POVMs may be viewed as a geometric interpretation of Stark units.
Many future research directions naturally stem from this paper. Elucidating the precise
mathematical relationships between the Shintani–Faddeev cocycle and the various cocycles
discussed in Section 1.6 is an important (and far from trivial) undertaking. Investigating
RM values of other, generally noncommutative, “quantum modular cocycles” studied by
Garoufalidis and Wheeler [30] and Wheeler [76] is sure to prove interesting. More broadly, one
hopes to make sense of the myriad possible connections to quantum modularity, knot theory,
3-manifolds, topological quantum field theory, and gauge theory. Another future direction
of research may be to align the constructions in this paper with Manin’s noncommutative
geometry perspective on real multiplication [50].
The author is hopeful the results of this paper will eventually be extended to arbitrary
(not just totally real) number fields. For example, in the complex cubic case, the analo-
gous 1-cocycle for SL3 seems to come from the elliptic gamma function [26, 27]—this has
been partially shown by the impressive work of Bergeron, Charollois, and Garc´ıa [11], but
further work would be needed to define the cocycle precisely, remove the a-smoothing, and
characterize arbitrary “stable values” of the cocycle. One can make some educated guesses
that hint at a program for general number fields to realize Stark units and variants thereof
as stable values of function-valued (r1 + r2 − 1)-cocycles for SLn. However, much work is
needed to pin down the details in the totally real (r2 = 0) and almost totally real (r2 = 1)
cases, and genuinely new ideas will be needed in the general case.

1.8. Structure of this paper. We briefly outline the format of the paper.
Section 2 proves needed basic results about q-Pochhammer symbols, eta functions, theta
functions, and the characters ψ and χr. Content that can be found elsewhere is summarized

10 GENE S. KOPP

with references to proofs provided. The identities we desire for the character χr do not
appear to be in the literature in the form we need and so must be proven in detail.
Section 3 provides background on ray class monoids and describes how ray classes are
associated to “real multiplication points” in a moduli space.
Section 4 introduces the Shintani–Faddeev modular and Jacobi cocycles and defines their
stable values (including real multiplication values). It relates them to the theta functions,
eta functions, and characters describes in Section 2. A more sophisticated perspective on
these cocycles is provided in Section 5 by a form of equivariant cohomology. Specifically,
ש
r is an element of a first cohomology group of the global sections of Γr-invariants of a
certain complex of sheaves. This approach is reminiscent of Bekki’s work on Eisenstein and
Shintani–Barnes cocycles [10] but is not directly compatible.
Section 6 defines the partial zeta functions of interest, proves relations between different
types of partial zeta functions, and connects a few different versions of the Stark conjectures.
Section 7 focuses on evaluating partial zeta functions at s = 0. It uses continued fractions
following the approach of Tangedal [74]. Several technical results on continued fractions and
related quantities are required, and their proofs constitute a large portion of that section.
The proofs of Theorem 1.1 and Theorem 1.3 are completed in Section 8. Some further
implications are discussed, and a numerical example is provided.

1.9. List of notation. The following list describes some of the notation used in the paper
that is nonstandard, uncommon, new, or holds some potential for confusion.
• e(z) = e2πiz for z ∈ C.
• C ∪ {∞} is the Riemann sphere (which can be identified with P1(C)).
• H := {τ ∈ C : Im(τ ) > 0} is the upper half plane.
• Vectors are assumed to be column vectors unless otherwise stated; the transpose of
a vector v is v⊤.
• If v = ( v1
v2 ) and w = ( w1
w2 ) are vectors, the “standard” symplectic form is denoted
[v, w] := − det ( v1 w1
v2 w2 ) = v2w1 − v1w2.
• If r = ( r1
r2 ) ∈ R2 and τ ∈ C, then [[r, τ ]] := [r, ( τ
1 )] = r2τ − r1.
• If A = ( a b
c d ) ∈ SL2(R) and τ ∈ C, then jA(τ ) := cτ + d, and sA(τ ) = sgn(jA(τ )).
• If A = ( a b
c d ) ∈ SL2(R) and τ ∈ C ∪ {∞}, then A · τ := aτ +b
cτ +d .
• If (m, A) ∈ Q
2 ⋊ SL2(Q) (the rational Jacobi group) and (z, τ ) ∈ C × (C \ Q), then
(m, A) · (z, τ ) := ( z
jA(τ ) + [[m, A · τ ]] , A · τ ), and A · (z, τ ) := (0, A) · (z, τ ).

• For r ∈ Q2, the group Γr = {A ∈ SL2(Z) : Ar − r ∈ Z
2}.
• If F is a number field, then ρ1, . . . , ρr1 are its real embeddings, and ∞1, . . . , ∞r1 are
formal symbols denoting the associated real places. If F is a real quadratic field,
we will sometimes fix a choice of real embedding F ⊂ R and denote ρ1(x) = x and
ρ2(x) = x′ for x ∈ F , so that x ↦→ x′ is the nontrivial Galois automorphism.
• Cquad is the set consisting of those irrational complex numbers that are roots of a
degree two polynomial in Z[x], Rquad = Cquad ∩ R, and Hquad = Cquad ∩ H.
• If R is a commutative Noetherian domain with fraction field F , and a, b are fractional
R-ideals (that is, finitely generated R-submodules of F ), then the quotient ideal is
the fractional ideal (a : b) = {γ ∈ F : γb ⊆ a}.
• If R is a commutative ring and a, b are R-ideals, then a and b are coprime, or a is
coprime to b, if a + b = R. This terminology will be used even in rings that are not
Dedekind domains, particularly non-maximal orders of number fields. Additionally,

THE SHINTANI–FADDEEV MODULAR COCYCLE 11

if R is a commutative Noetherian domain, then a fractional ideal c is coprime to an
integral ideal m if c = ab
−1 for an integral ideal a and an invertible integral ideal b
such that a and b are both coprime to m.
• If r = ( r1
r2 ) ∈ R2, then {r} := ( r1−⌊r1⌋−1
r2−⌊r2⌋ ).
• The character ψ on Mp2(Z) is a variant of the Rademacher/Meyer invariant and is
defined in Theorem 2.4.
• The character χr on Γr is defined in Theorem 2.14; see Lemma 2.15 for a simplified
formula.
• The theta function ϑr(z, τ ) is defined in Definition 2.8, and θr(τ ) = ϑr(0, τ ).
• The ray class group of an order Clm,Σ(O) and the associated ray class field of an
order H O
m,Σ are defined in Section 3.1. We set Hm,Σ = H OF
m,Σ.

• The flat imprimitive ray class monoid Clm
♭
m,Σ(O) is defined in Section 3.2, together

with its submonoid of zero classes ZClm
♭
m,Σ(O).
• For A ∈ SL2(Z), the complex domain DA is defined in (4.2), and the complex domain
̃DA is defined in (4.3).
• The function σm,A(z, τ ) is defined in Definition 4.16.
• The function ש
r
A(τ ) is defined in Definition 4.18.
• The “stable value”/“RM value” notation w[β] (e.g., with w = ש
r) is defined in
Section 4.4 for modular cocycles and Section 4.5 for Jacobi cocycles.
• Hirzebruch–Jung (HJ) continued fractions and Hirzebruch–Jung (HJ) cycle data are
defined in Section 7.1, with attached notation.

2. Preliminaries on q-Pochhammer symbols and half-integral weight
modular forms

In this section, we will provide some necessary foundational definitions and results about
q-Pochhammer symbols as well as certain (fractional weight) modular forms on congruence
subgroups of SL2(Z) and its metaplectic cover Mp2(Z).

2.1. SL2 and the standard symplectic form. For a commutative ring R with unity, the
group SL2(R) is the same as the symplectic group Sp2(R) (a special case of the general
symplectic group Sp2n(R)). In particular, the 2 × 2 symplectic group is defined to be

Sp2(R) = {( a b
c d ) ∈ Mat2×2(R) : ( a b
c d )
⊤ ( 0 1
−1 0 ) ( a b
c d ) = ( 0 1
−1 0 )},

those matrices preserving the standard symplectic form [u, v] := u⊤ ( 0 1
−1 0 ) v. Examining

this condition, we note ( a b
c d )⊤ ( 0 1
−1 0 ) ( a b
c d ) = ( 0 ad−bc
−(ad−bc) 0 ), so the condition is equivalent
to ad − bc = 1.
We also introduce the notation [[u, τ ]] := [u, ( τ
1 )] = u2τ − u1 for u = ( u1
u2 ).

2.2. Fractional linear transformations. The special linear group SL2(R) acts on C∪{∞}
by the fractional linear transformation action ( a b
c d ) · τ = aτ +b
cτ +d (with ( a b
c d ) · ∞ = a
c ), and this
action restricts to an action on the upper half plane H. If τ = ( a b
c d ) ∈ SL2(R) and τ ∈ C,
we define jA(τ ) := cτ + d

and note that j satisfies the cocycle relation jA1A2(τ ) = jA1(A2 · τ )jA2(τ ).

12 GENE S. KOPP

If A ∈ SL2(R) is hyperbolic, meaning that Tr(A) > 2, the action of A on C ∪ {∞} has two
fixed points, both in R ∪ {∞}. Following Katok [38], the attracting fixed point β of A is the
fixed point satisfying β = limn→∞ An · τ for all (equivalently, any) τ ∈ H. Equivalently, ( β
1 )

is an eigenvector of A with eigenvalue greater than 1.
A real number generating a quadratic extension of Q will be called a real quadratic number,
and the set of all real quadratic numbers will be denoted Rquad. If β is a real quadratic
number, we denote by β′ its unique nontrivial Galois conjugate. If A ∈ SL2(Z) is hyperbolic,
then its fixed points are two Galois conjugate real quadratic numbers. The set of all complex
numbers generating quadratic extensions of Q will be denoted Cquad, and those in the upper
half-plane by Hquad = Cquad ∩ H.
The real Jacobi group is the semidirect product R2 ⋊ SL2(R) with group operation

(m, A)(n, B) = (m + An, AB).

The Jacobi group acts on C × H by the Jacobi action

(m, A) · (z, τ ) = ( z
jA(τ ) + [[m, A · τ ]] , A · τ ) . (2.1)

When the right-hand side of (2.1) is well-defined, we will use the same notation (m, A)·(z, τ ),
even when (z, τ ) /∈ C × H. In particular, the Jacobi action gives an action of the rational
Jacobi group Q
2 ⋊ SL2(Q) on C × (C \ Q).
Of particular import is the integer Jacobi group Z
2 ⋊ SL2(Z), which is used to describe the
transformation laws of theta functions. The subgroups Z
2 ⋊ {I} and {0} ⋊ SL2(Z) describe
elliptic transformations and modular transformations, respectively.
For N ∈ N and r ∈ Q
2, we define several congruence subgroups of SL2(Z):

Γ(N ) := {A ∈ SL2(Z) | A ≡ I (mod N )},

Γ1(N ) := {A ∈ SL2(Z) | A ≡ ( 1 ∗
0 1 ) (mod N )}, and

Γr := {A ∈ SL2(Z) | Ar ≡ r (mod 1)}.

Note that Γ( 1/N
0
 ) = Γ1(N ), and Γr ⊂ Γ(N ) for r ∈ 1
N Z
2.

2.3. The covering groups ̃SL2(R) and Mp2(R). In this section, we review the definition

of the universal covering group ̃SL2(R) of SL2(R) and the metaplectic group Mp2(R).

The group ̃SL2(R) may be defined as follows:

̃SL2(R) := {
(A, λ) : A ∈ SL2(Z),
λ : H → C continuous with exp(λ(τ )) = cτ + d
 } .

Its group law is defined by (A1, λ1)(A2, λ2) = (A1A2, λ3) where λ3(τ ) = λ1(A2 · τ ) + λ2(τ ).
This group fits into a short exact sequence of the form

1 → Z → ̃SL2(R) → SL2(R) → 1, (2.2)

where the left map is given by n ↦→ (I, 2πin), and the right map is given by (A, λ) ↦→ A.
This construction may be described more abstractly: Topologically, SL2(R) is homotopy

equivalent to a circle (by Iwasawa decomposition), so π1(SL2(R)) ∼= Z, and ̃SL2(R) is the

topological universal cover of SL2(R) endowed with a group structure. (Algebraically, ̃SL2(R)
is also the universal perfect central extension of SL2(R).) For convenience, we also define

THE SHINTANI–FADDEEV MODULAR COCYCLE 13

the group ̃SL2(Z) = {(A, λ) ∈ ̃SL2(R) : A ∈ SL2(Z)}. (This is an abuse of notation, because
̃SL2(Z) it is not a canonical covering group of SL2(Z) itself as an abstract group.)
The metaplectic group Mp2(R) (a special case of the more general Mp2n(R)) is defined as
a double cover of SL2(R) = Sp2(R). In particular,

Mp2(R) := {(A, ϵ) : A ∈ SL2(Z),
ϵ : H → C continuous with ϵ(τ )
2 = cτ + d
 } ,

with multiplication law given by (A1, ϵ1)(A2, ϵ2) = (A1A2, ϵ3) with ϵ3(τ ) = ϵ1(A2 · τ )ϵ2(τ ). A

surjective map ̃SL2(R) → Mp2(R) may be defined by sending (A, λ) ↦→ (A, ϵ) with ϵ(τ ) =
exp( 1
2λ(τ )); the kernel of this map is identified with 2Z ⊂ Z in the exact sequence (2.2).
The metaplectic group is the two-fold central covering group of SL2(R), fitting into the short
exact sequence 1 → Z/2Z → Mp2(R) → SL2(R) → 1.
We also define the integer metaplectic group Mp2(Z) := {(A, ϵ) ∈ Mp2(R) : A ∈ SL2(Z)}.
More generally, for any discrete subgroup Γ ≤ SL2(R), we will define the metaplectic cover
MΓ := {(A, ϵ) ∈ Mp2(R) : A ∈ Γ}. In particular, we will use the groups MΓ(N ), MΓ1(N ),
and MΓr, for N ∈ N and r ∈ Q.

2.4. The q-Pochhammer symbol and variants. We will need to use several versions of
the q-Pochhammer symbol.

Definition 2.1. The finite q-Pochhammer symbol is

(w, q)n =
 



n−1∏

k=0(1 − wqk) for n ≥ 0, and

−n∏

k=1
(1 − wq−k)−1 for n < 0.

This definition is equivalent to the following recursive definition, extended to negative inte-
gers so as to preserve the recursion:

(w, q)0 = 1, and

(w, q)n+1 = (w, q)n(1 − wqn).

Definition 2.2. The infinite q-Pochhammer symbol is defined for w, q ∈ C with |q| < 1 by

(w, q)∞ = lim
n→∞(w, q)n =
 ∞∏

k=0
 (
1 − wqk) .

The following alternative notations are also used. The infinite q-Pochhammer symbol in
“Jacobi form notation” for z ∈ C and τ ∈ H is

ϖ(z, τ ) := (e(z) , e(τ ))∞.

The infinite q-Pochhammer symbol in “characteristics notation” for r = ( r1
r2 ) ∈ R2 and τ ∈ H
is ϖr(τ ) := ϖ([[r, τ ]] , τ ) = (e(r2τ − r1) , e(τ ))∞.

Lemma 2.3. If z ∈ C, τ ∈ H, and m, n ∈ Z, then

ϖ(z + mτ + n, τ ) = (e(z) , e(τ ))
−1
m ϖ(z, τ ).

14 GENE S. KOPP

Proof. Follows from inspection of the product forms of both sides. □

2.5. The Dedekind eta function and its logarithm. In this section, we review the
transformation theory of the Dedekind eta function. Proofs of assertions that are not proven
here may be found in [4, 59].
The Dedekind eta function

η(τ ) = e( τ
24
) ϖ(τ, τ ) = e
( τ
24
) ∞∏

k=1
(1 − e(kτ )) for τ ∈ H

has a continuous, well-defined logarithm defined by

(log η)(τ ) = 2πiτ
24 +
 ∞∑

k=1 log(1 − e(kτ )).

The function (log η)(τ ) has a modularity property for the group ̃SL2(Z). Specifically, for

(A, λ) ∈ ̃SL2(Z),
 (log η)(A · τ ) = 2πi
24 Ψ(A, λ) + 1
2λ(τ ) + (log η)(τ ), (2.3)

where Ψ : ̃SL2(Z) → Z is an integer-valued group homomorphism.
Rademacher defines a function (not a homomorphism) Φ : SL2(Z) → Z satisfying the
relation
 (log η)(A · τ ) = 2πi
24 Φ(A) + 1
21 c̸=0 log(−i sgn(c)(cτ + d)) + (log η)(τ ), (2.4)

where the middle term in interpreted as zero if c = 0, taking 1 c̸=0 = 1 and using the principal
branch of the logarithm otherwise. This function is defined as

Φ(A) =
 { b
d , if c = 0,

a+d
c − 12 sgn(c)s(d, |c|), if c ̸= 0, (2.5)

where s(d, |c|) is the Dedekind sum

s(h, k) =
 |k|−1∑

j=1
 ( j
k − ⌊ j
k
 ⌋ − 1
2
) (hj
k − ⌊ hj
k
 ⌋ − 1
2
 ) .

(See (71.1), (71.2), and (71.22) on p. 150–151 and (68.3) on p. 146 of [59].) Comparing (2.3)
and (2.4), we see that Ψ and Φ are related by the identity

Ψ(A, λ) = Φ(A) + 6
πi (1 c̸=0 log(−i sgn(c)(cτ + d)) − λ(τ )) . (2.6)

The modular transformation law for η(τ ) follows from that for (log η)(τ ). If (A, ϵ) ∈
Mp2(Z), then η(A · τ ) = ψ(A, ϵ)ϵ(τ )η(τ ), (2.7)
where ψ(A, ϵ) = exp
( 2πi
24 Ψ(A, λ)
) for any λ with ϵ(τ ) = exp
( 1
2λ(τ )
). We also introduce the
shorthand ψ2(A) := (ψ(A, ϵ))
2, which does not depend on the choice of ϵ. Note that ψ2 is a
character of SL2(Z).
For the purposes of explicit calculation, it is important to note that the function ψ(A, ϵ)
can be expressed in terms of Jacobi symbols without needing to use Dedekind sums.

THE SHINTANI–FADDEEV MODULAR COCYCLE 15

Theorem 2.4. Let A = ( a b
c d ) ∈ SL2(Z) and τ ∈ H. If c = 0, then

ψ(A, ϵ)ϵ(τ ) = e
(sgn(d)b
24
 ) .

If c > 0, then

ψ(A, ϵ) ϵ(τ )
√
−i(cτ + d) =
 



( d
c ) e( 1−c
8 ) e( bd(1−c2)+c(a+d)
24 ) , if 2 ∤ c,
( c
|d| ) e( d
8 ) e( ac(1−d2)+d(b−c)
24 ) , if 2 ∤ d.

Here, ( d
c ) and ( c
|d| ) are Jacobi symbols. If c < 0, then ψ(A, ϵ) = iψ(−A, iϵ).

Proof. See [59, p. 163]. □

2.6. Jacobi theta functions with characteristics. In this section, we review the trans-
formation theory of Jacobi theta functions with arbitrary real characteristics. Our primary
reference is Rademacher [59]. The author was unable to find a suitable source for the general
transformation laws of theta functions with characteristics, so those have been proven here.
Jacobi defined four theta functions, ϑj for j ∈ {1, 2, 3, 4}; we will treat ϑ1 as the “basic”
theta function and define other theta functions in terms of ϑ1. The primary advantage of
this approach is that the full SL2(Z)-action takes ϑ1-values to other ϑ1-values, whereas the
other ϑj are permuted with each other by the action.

Definition 2.5. For z ∈ C and τ ∈ H, the first Jacobi theta function is

ϑ1(z, τ ) = −
 ∞∑

n=−∞ e( 1
2 (n + 1
2)2 τ + (
n + 1
2) (
z + 1
2)) .

The first Jacobi theta function satisfies elliptic and modular transformation laws. (These
may also be interpreted as a single transformation law under the action of Z
2 ⋊ SL2(Z).)

Theorem 2.6. If z ∈ C, τ ∈ H, and k, ℓ ∈ Z, then

ϑ1(z + kτ + ℓ, τ ) = (−1)k+ℓe(
− 1
2k2τ − kz) ϑ1(z, τ ).

Proof. See [59, p. 177, (80.31)]. There is a misprint in that formula, corrected here. □

Theorem 2.7. If z ∈ C, τ ∈ H, and (A, ϵ) ∈ Mp2(Z) with A = ( a b
c d ), then

ϑ1(A · (z, τ )) = ψ(A, ϵ)
3e( cz2

2(cτ + d)
) ϵ(τ )ϑ1(z, τ ).

Proof. See [59, p. 180]. □

Theta functions with characteristics involve an additional pair of real parameters r ∈ R
2,
often taken to be rational in applications. In the special case r ∈ {
( 0
0 ) , ( 0
1/2 ) , ( 1/2
0 ) , ( 1/2
1/2 )}
,
they are essentially the four classical Jacobi theta functions usually called ϑj for j ∈
{1, 2, 3, 4}. There is no widely accepted notational convention for theta functions with char-
acteristics, and the following definition reflects the author’s preferred notation. The use of
a shift by r2τ − r1 (the symplectic pairing of ( r1
r2 ) with ( τ
1 )) instead of the more commonly
used r1τ + r2 makes the modular transformation law nicer.

16 GENE S. KOPP

Definition 2.8. For r = ( r1
r2 ) ∈ R2, z ∈ C, and τ ∈ H, the Jacobi theta function with
characteristics is

ϑr(z, τ ) =
 ∞∑

n=−∞ e
( 1
2 (
n + r2 + 1
2)2 τ + (n + r2 + 1
2) (
z − r1 + 1
2))

= −e( 1
2r2
2τ + r2 (z − r1 + 1
2)) ϑ1(z + r2τ − r1, τ ).

In particular, ϑ1(z, τ ) = −ϑ( 0
0 )(z, τ ).

Shifting the characteristics by a pair of integers simply multiplies the theta function by a
constant of norm 1.

Proposition 2.9. Let r = ( r1
r2 ) ∈ R
2, m = ( m1
m2 ) ∈ Z2, z ∈ C, and τ ∈ H. Then

ϑr+m(z, τ ) = e(−m1 (r2 + 1
2)) ϑr(z, τ ).

Proof. By Definition 2.8, we have

ϑr+m(z, τ ) = ∑

n∈Z e((
n + m2 + r2 + 1
2)2 τ + (n + m2 + r2 + 1
2) (
z − m1 − r1 + 1
2))

= ∑

n∈Z e((
n + r2 + 1
2)2 τ + (
n + r2 + 1
2) (
z − m1 − r1 + 1
2))

= e
(
−m1 (
r2 + 1
2)) ϑr(z, τ ),

where in the second-to-last line we substituted n ↦→ n − m2. □

The modular transformation law for the theta function with characteristics also follows
by direct calculation from the modular transformation law for θ1; however, it is more com-
plicated, so we give a detailed proof.

Theorem 2.10. Let r = ( r1
r2 ) ∈ R
2, z ∈ C, τ ∈ H, and (A, ϵ) ∈ Mp2(Z) with A = ( a b
c d ).
Then ϑAr(A · (z, τ )) = ψ(A, ϵ)3κ(A, r)e
( cz2
2(cτ +d) ) ϵ(τ )ϑr(z, τ ), (2.8)

where κ(A, r) = e( 1
2 (cr1 + (d − 1)r2 − acr2
1 − 2bcr1r2 − bdr2)) . (2.9)

Proof. By Definition 2.8,

ϑAr(A · (z, τ )) = −e
( 1
2(cr1 + dr2)2 aτ +b
cτ +d + (cr1 + dr2) ( z
cτ +d − ar1 − br2 + 1
2))

× ϑ1( z
cτ +d + (cr1 + dr2) aτ +b
cτ +d − (ar1 + br2), aτ +b
cτ +d )

= −e
( cr1+dr2
2(cτ +d) ((cr1 + dr2)(aτ + b) + 2z − (2ar1 + 2br2 − 1)(cτ + d))
)

× ϑ1( z+(cr1+dr2)(aτ +b)−(ar1+br2)(cτ +d)
cτ +d , aτ +b
cτ +d ) ,

= −e
( cr1+dr2
2(cτ +d) (r2τ − r1 + 2z − (ar1 + br2 − 1)(cτ + d))
)

× ϑ1( z+r2τ −r1
cτ +d , aτ +b
cτ +d ) , (2.10)

using the relation
 (cr1 + dr2)(aτ + b) − (ar1 + br2)(cτ + d) = r2τ − r1

THE SHINTANI–FADDEEV MODULAR COCYCLE 17

in (2.10). Using the transformation law for ϑ1 from Theorem 2.7, we obtain

ϑAr(A · (z, τ )) = −e( cr1+dr2
2(cτ +d) (r2τ − r1 + 2z − (ar1 + br2 − 1)(cτ + d))
)

× ψ(A, ϵ)3e( c(z+r2τ −r1)2

2(cτ +d) ) ϵ(τ )ϑ1(z + r2τ − r1, τ )

= −ψ(A, ϵ)3e(
− 1
2(ar1 + br2 − 1)(cr1 + dr2)
)

× e( c(z+r2τ −r1)2+(cr1+dr2)(r2τ −r1+2z)
2(cτ +d) ) ϵ(τ )ϑ1(z + r2τ − r1, τ )

= −ψ(A, ϵ)3e(
− 1
2(ar1 + br2 − 1)(cr1 + dr2)
)

× e( cz2
2(cτ +d) + 1
2r2(r2τ − r1 + 2z)
) ϵ(τ )ϑ1(z + r2τ − r1, τ )

= −ψ(A, ϵ)3e( 1
2(cr1 + dr2 − acr2
1 + (ad + bc)r1r2 + bdr2
2)
)

× e( cz2
2(cτ +d) + r2
2τ
2 + r2 (
z − r1 + 1
2) + r1r2
2 − r2
2 ) ϵ(τ )ϑ1(z + r2τ − r1, τ )

= −ψ(A, ϵ)
3e
( 1
2(cr1 + (d − 1)r2 − acr2
1 − (ad + bc − 1)r1r2 − bdr2
2)
)

× e
( cz2
2(cτ +d) ) e( r2
2τ
2 + r2 (
z − r1 + 1
2)) ϵ(τ )ϑ1(z + r2τ − r1, τ )

= ψ(A, ϵ)
3e( cr1+(d−1)r2−acr2
1−2bcr1r2−bdr2
2
2 ) e( cz2
2(cτ +d) ) ϵ(τ )ϑr(z, τ )

= ψ(A, ϵ)
3κ(A, r)e
( cz2
2(cτ +d) ) ϵ(τ )ϑr(z, τ ). □

Lemma 2.11. Let r ∈ Q
2. The function κ satisfies the following cocycle condition: For any
A, B ∈ Γr, κ(AB, r) = κ(A, Br)κ(B, r).

Proof. This follows from Theorem 2.10 by applying (2.8) to each of ϑr((A1A2) · (z, τ )) with
A = A1A2, ϑr(A1 · (A2 · (z, τ ))) with A = A1, and ϑr(A2 · (z, τ )) with A = A2, and comparing
the results. □

Lemma 2.12. Let r = ( r1
r2 ) ∈ R
2 and A = ( a b
c d ) ∈ SL2(Z). With κ(A, r) defined as in
Theorem 2.10,
 κ(A, A
−1r) = κ(A−1, r)
−1

= e
( 1
2(
cr1 + (−a + 1)r2 − cdr2
1 + 2bcr1r2 − abr2
2)) . (2.11)

Proof. By Lemma 2.11, 1 = κ(I, r) = κ(AA−1, r) = κ(A, A
−1r)κ(A
−1, r), so κ(A, A
−1r) =
κ(A
−1, r)−1. The second equality of (2.11) follows by plugging in A
−1 = ( d −b
−c a ) to (2.9). □

2.7. Characters of modular theta functions. We will now consider modular forms de-
fined by theta functions. We define a character χr on the group Γr that will play an important
role in the theory of the Shintani–Faddeev modular cocycle.

Definition 2.13. Let r ∈ R2, τ ∈ H. The theta null with characteristics is

θr(τ ) = ϑr(0, τ ).

Theorem 2.14. Let r ∈ Q
2. The function θr(τ ) is a weight 1
2 modular form with character
for the group MΓr = {(A, ϵ) ∈ Mp2(Z) : A · r ≡ r (mod 1)}.

18 GENE S. KOPP

Specifically, for (A, ϵ) ∈ MΓr and τ ∈ H,

θr(A · τ ) = ψ(A, ϵ)
3χr(A)ϵ(τ )θr(τ )

where χr is a character on Γr defined by the formula

χr(A) = e( (c−d+1)r1+(−a+b+1)r2−cdr2
1+2(a−1)dr1r2−(a−2)br2
2
2 ) .

Proof. We first apply the modular transformation formula given in Theorem 2.10.

θr(A · τ ) = ϑA(A−1r)(A · (0, τ ))

= ψ(A, ϵ)
3κ(A, A
−1r)ϵ(τ )ϑA−1r(z, τ ).

Since A ∈ Γr, so is A−1, and A
−1r = r + m for some m = ( m1
m2 ) ∈ Z
2. Applying Proposi-
tion 2.9 and regrouping factors, we have

θr(A · τ ) = ψ(A, ϵ)3χr(A)ϵ(τ )θr(τ ), (2.12)

where χr(A) := κ(A, A
−1r)e
(
−m1 (
r2 + 1
2)). We have

m = (A
−1 − I)r = ( (d − 1)r1 − br2
−cr1 + (a − 1)r2
) .

Applying Lemma 2.12, we may write χr as

χr(A) = e( cr1+(−a+1)r2−cdr2
1+2bcr1r2−abr2
2
2 ) e(
− ((d − 1)r1 − br2) (r2 + 1
2))

= e
( (c−d+1)r1+(−a+b+1)r2−cdr2
1+2(bc−d+1)r1r2−(ab−2b)r2
2
2 )

= e
( (c−d+1)r1+(−a+b+1)r2−cdr2
1+2(a−1)dr1r2−(a−2)br2
2
2 ) .

The fact that χr is a character on Γr follows by applying (2.12) to each of θr((A1A2) · τ )
with A = A1A2, θr(A1 · (A2 · τ )) with A = A1, and θr(A2 · τ ) with A = A2, and comparing
the results. □

The character χr can be written in a somewhat nicer way, as the following lemma shows.

Lemma 2.15. Let r ∈ 1
N Z
2 for N ∈ N. The character χr on Γr has the following formula.

χr(A) = −(−1)δ2(Ar−r)e
( 1
2 [Ar, r]) , where

δ2(q) :=
 {
1, if q ∈ 2Z
2,
0, if q /∈ 2Z
2.

Moreover, χr takes values in the group µN ′(C) of N ′-th roots of unity, where

N ′ =
 {
N if N is odd,
2N if N is even.

Proof. Write A = ( a b
c d ) and r = ( r1
r2 ); we have A−1 = ( d −b
−c a ). By Theorem 2.14,

χr(A) = χr(A
−1)
−1

= e
( (−c−a+1)r1+(−d−b+1)r2+acr2
1+2a(d−1)r1r2+b(d−2)r2
2
2 )−1

THE SHINTANI–FADDEEV MODULAR COCYCLE 19

= e
( (a+c−1)r1+(b+d−1)r2−acr2
1−2a(d−1)r1r2−b(d−2)r2
2
2 )

= e
( (ar1+br2−r1)+(cr1+dr2−r1)−ar1(cr1+dr2)−(d−2)r2(ar1+br2)
2 ) .

Set r′ = ( r′
1
r′
2
 ) := Ar = ( ar1+br2
cr1+dr2 )
. Then,

χr(A) = e( (r′
1−r1)+(r′
2−r2)−ar1r′
2−(d−2)r2r′
1
2 )

= e
( (r′
1−r1)+(r′
2−r2)+2r2r′
1−(ar1r′
2+dr2r′
1)
2 ) .

Moreover, ar1r′
2 + dr2r′
1 = ar1r′
2 + (r′
2 − cr1)r′
1 = r1(ar′
2 − cr′
1) + r′
1r′
2 = r1r2 + r′
1r′
2. Thus,

χr(A) = e( (r′
1−r1)+(r′
2−r2)+2r2r′
1−(r1r2+r′
1r′
2)
2 )

= e
( (r′
1−r1)+(r′
2−r2)+(r′
1−r1)(r′
2−r2)+(r2r′
1−r1r′
2))
2 ) .

Since r
′ ≡ r (mod 1), we see that e( (r′
1−r1)+(r′
2−r2)+(r′
1−r1)(r′
2−r2)
2 ) ∈ {±1}, and moreover that

e
( (r′
1−r1)+(r′
2−r2)+(r′
1−r1)(r′
2−r2)
2 ) = −(−1)δ2(Ar−r).

Also, r2r′
1 − r1r′
2 = [r′, r] = [Ar, r], so

χr(A) = −(−1)
δ2(Ar−r)e( 1
2 [Ar, r]) . (2.13)

Clearly the right-hand side (2.13) is a (2N )-th root of unity. Moreover, when N is odd, we
check δ2(Ar − r) ≡ 1 ≡ 1 + [Ar, r] (mod 2) when Ar ≡ r (mod 2), and δ2(Ar − r) ≡ 0 ≡
1 + [Ar, r] (mod 2) when Ar ̸≡ r (mod 2), so in fact χr(A) is an N -th root of unity. □

Lemma 2.16. Let r ∈ Q
2. For any m ∈ Z
2 and any A ∈ Γr,

χr+m(A) = χr(A).

Proof. For all τ ∈ H, Theorem 2.14 gives

θr+m(A · τ ) = ψ(A, ϵ)
3χr+m(A)ϵ(τ )θr+m(τ );

θr(A · τ ) = ψ(A, ϵ)
3χr(A)ϵ(τ )θr(τ ).

Dividing, we have θr+m(A · τ )
θr(A · τ ) = χr+m(A)
χr(A) · θr+m(τ )
θr(τ ) .

By Proposition 2.9, θr+m(A·τ )
θr(A·τ ) = e
(
−m1 (
r2 + 1
2)) = θr+m(τ )
θr(τ ) . Therefore χr+m(A) = χr(A). □

Remark 2.17. While the metaplectic transformation law for the modular theta nulls with
rational characters is sufficient for proving the properties of the (multiplicative) Shintani–
Faddeev modular cocycle, a similar study of additive cocycles would require working out the
transformation law for log θr under a corresponding congruence subgroup ̃Γr of ̃SL2(Z).

20 GENE S. KOPP

2.8. The Jacobi triple product formula. The Jacobi triple product formula relates a
certain q-series to a certain infinite product and can be seen as an expression for a Jacobi
theta function in terms of infinite q-Pochhammer symbols. Beyond its importance in the
theory of modular forms, this ubiquitous formula has Lie theoretic, probabilistic, and physical
interpretations, among others [5, 6, 49]. It is commonly stated as follows.

Theorem 2.18. If w, q ∈ C with |q| < 1, then

∞∑

n=−∞ wnqn2 =
 ∞∏

k=1
 (1 − q2k) (
1 + wq2k−1) (
1 + w−1q2k−1) . (2.14)

Proof. See [59, p. 231, (100.1)]. □

After a change of variables, the Jacobi triple product formula is equivalent to the following.

Proposition 2.19. If z ∈ C and τ ∈ H, then

ϖ(z, τ )ϖ(−z, τ ) = −ie(
− τ
12) (
e
( z
2 ) − e
(− z
2 )) ϑ1(z, τ )
η(τ ) . (2.15)

Proof. In Theorem 2.18, take w = e
(
z − τ
2 + 1
2) = −e(
z − τ
2 ) and q = e
( τ
2 )
. Then, the
left-hand side of (2.14) becomes

∞∑

n=−∞ wnqn2 =
 ∞∑

n=−∞ e(nz − n
2 τ + n
2 + n2
2 τ )

= e
(
− τ
8 + 1
2 (
z + 1
2)) ∞∑

n=−∞ e( 1
2 (
n − 1
2)2 τ + (n − 1
2) (
z + 1
2))

= −ie(
− τ
8 + z
2 ) ϑ1(z, τ ). (2.16)

The right-hand side of (2.14) becomes

∞∏

k=1
 (
1 − q2k) (
1 + wq2k−1) (
1 + w−1q2k−1)

=
 ∞∏

k=1 (1 − e(kτ )) (
1 − e(
z − τ
2 + (2k − 1) τ
2 )
)) (
1 − e
(−z + τ
2 + (2k − 1) τ
2 )
))

=
 ∞∏

k=1 (1 − e(kτ )) ×
 ∞∏

k=1 (1 − e(z + (k − 1)τ ))) ×
 ∞∏

k=1 (1 − e(−z + (k + 1)τ )))

=
 ( η(τ )
e
( τ
24)
 )
 (ϖ(z, τ )) ( ϖ(−z, τ )
1 − e(−z)
)

= e(− τ
24 + z
2 )

e( z
2 ) − e(
− z
2 ) η(τ )ϖ(z, τ )ϖ(−z, τ ). (2.17)

Equating (2.17) and (2.16) and multiplying/dividing/rearranging factors, we get (2.15). □

The following version of the triple product formula incorporates “characteristics” r and
will be used in Section 4.10 to prove important identities for the Shintani–Faddeev cocycles.

THE SHINTANI–FADDEEV MODULAR COCYCLE 21

Proposition 2.20. If r ∈ R
2, z ∈ C, and τ ∈ H, let

ϖr(z, τ ) = ϖ(z + [[r, τ ]] , τ ) =
 ∞∏

k=0 (1 − e(z + (k + r2)τ − r1)) .

Then
 ϖr(z, τ )ϖ−r(−z, τ ) = ie(− ( r2
2
2 + 1
12) τ − r2 (
z − r1 + 1
2))

× (
e( z+r2τ −r1
2 ) − e
( −z−r2τ +r1
2 )) ϑr(z, τ )
η(τ ) . (2.18)

Proof. Make the substitution z ↦→ z + r2τ − r1 in Proposition 2.19. We have

ϖr(z, τ )ϖ−r(−z, τ ) = −ie
(− τ
12) (
e( z+[[r,τ ]]
2 ) − e(− z+[[r,τ ]]
2 )) ϑ1(z + [[r, τ ]] , τ )
η(τ ) .

Using the relation ϑr(z, τ ) = −e( 1
2r2
2τ + r2(z − r1 + 1
2)) ϑ1(z + [[r, τ ]] , τ ),

ϖr(z, τ )ϖ−r(−z, τ ) = ie(
− τ
12) (
e
( z+r2τ −r1
2 ) − e( −z−r2τ +r1
2 ))

× e(− 1
2r2
2τ − r2(z − r1 + 1
2)
) ϑr(z, τ )
η(τ ) ,

which can be algebraically simplified to (2.18). □

2.9. Modular specializations of the q-Pochhamer symbol. The following formulas can
be proven directly by manipulation of the infinite products. Taking q = e(τ ):

ϖ( 0
1 )(τ ) = (q, q)∞ = q−1/24η(τ );

ϖ( 0
1/2 )(τ ) = (q1/2, q1/2)∞
(q, q)∞ = q1/48 η(τ /2)
η(τ ) ;

ϖ( 1/2
1 )(τ ) = (q2, q2)∞
(q, q)∞ = q−1/24 η(2τ )
η(τ ) ;

ϖ( 1/2
1/2
 )(τ ) = (−q1/2, −q1/2)∞
(q, q)∞ = ζ48q1/48 η((τ + 1)/2)
η(τ ) . (2.19)

Thus, we see that ϖr(τ ) is a weak modular function on Γ(2) with character when r ∈ 1
2Z
2.
Conversely, when r /∈ 1
2Z
2, ϖr(τ ) is not modular (although we haven’t proven non-modularity
rigorously). Nonetheless, ϖr(τ ) satisfies a more complicated modular-like property, which
will be examined in Section 4.

3. On moduli spaces of ray class data

It will be helpful to have an interpretation of the “ray class data” determining a Stark unit
as a point on some continuous “moduli space.” We use the phrase “moduli space” in a loose
sense. In particular, our moduli space will be described as the quotient of (R/Z)
2 ×(R\Q) by
an action of discrete group that is not properly discontinuous. Ray class data will correspond
to the dense set of points (Q/Z)
2 × Rquad.

22 GENE S. KOPP

3.1. Ray class groups and ray class fields of orders. We briefly review some definitions
and results from [44] that generalize standard results about ray class groups and ray class
fields to non-maximal orders. Let O be an order in a number field F , let m be an ideal in
O, and let Σ be a subset of the real embeddings of F .

Definition 3.1. The ray class group of the order O modulo (m, Σ) is

Clm,Σ(O) = J
∗
m(O)
Pm,Σ(O),

where
 J∗
m(O) = {invertible fractional ideals of O coprime to m}, and

Pm,Σ(O) = {αO such that α ≡ 1 (mod m) and ρ(α) > 0 for ρ ∈ Σ}.

The study of the structure of ray class groups naturally leads to the study of certain groups
of units satisfying congruence conditions.

Definition 3.2. For a commutative ring with unity R and an ideal I of R, define the group

UI(R) := {α ∈ R× : α ≡ 1 mod I} = (1 + I) ∩ R×.

If R has real embeddings and Σ is a subset of the real embeddings of R, define

UI,Σ(R) := {α ∈ R× : α ≡ 1 mod I and ρ(α) > 0 for ρ ∈ Σ}.

A key theorem of [44] relates different class groups of orders to each other via a surjective
map whose quotient is described using the U-groups.

Theorem 3.3. Let F be a number field and O ⊆ O′ ⊆ OF be orders of F . Let m be an ideal
of O, m
′ an ideal of O′ such that mO′ ⊆ m
′, and Σ′ ⊆ Σ ⊆ {embeddings F ↪→ R}. Let d be
any O′-ideal such that d ⊆ (m : O′). We have the following exact sequence.

1 → Um′,Σ′(O′)
Um,Σ(O) → Um′(O′/d)
Um(O/d) × {±1}|Σ\Σ′| → Clm,Σ(O) → Clm′,Σ′(O′) → 1.

Proof. See [44, Thm. 6.5]. □

To the ray class group of an order, there is associated a ray class field of the order, denoted
H O
m,Σ. Some of its important properties are summarized by the following theorem.

Theorem 3.4. Let F be a number field, O an order of F , m an ideal of O, and Σ a subset of
the set of real embeddings of F . Then there exists a unique abelian Galois extension H O
m,Σ/F
with the property that a prime ideal p of OF that is coprime to the quotient ideal (m : OF )
splits completely in H O
m,Σ/F if and only if p ∩ O = πO, a principal prime O-ideal having
π ∈ O with π ≡ 1 (mod m) and ρ(π) > 0 for ρ ∈ Σ.
Additionally, these fields have the following properties:
• H OF
mOF ,Σ ⊆ H O
m,Σ ⊆ H OF
(m:OF ),Σ.
• There is a canonical isomorphism ArtO : Clm,Σ(O) → Gal
(H O
m,Σ/F )
.

Proof. See [44, Thm. 1.1, Thm. 1.2, Thm. 1.3]. □

We provide one new proposition about ray class groups of orders that will be relevant to
our moduli interpretation.

THE SHINTANI–FADDEEV MODULAR COCYCLE 23

Proposition 3.5. Let O ⊆ O′ be an orders in the same number field F . Let m be an
O′-ideal (thus also an O-ideal) and Σ a subset of the real embeddings of F . Then the map
ext = ext
(O′;m,Σ)
(O;m,Σ) : Clm,Σ(O) → Clm,Σ(O′) induced by ideal extension ext(a) = aO′ is an
isomorphism.

Proof. By Theorem 3.3 with d = (m : O′) = m and m
′ = mO′ = m, there is an exact sequence

1 → Um,Σ(O′)
Um,Σ(O) → Um(O′/m)
Um(O/m) → Clm,Σ(O) → Clm,Σ(O′) → 1.

The group Um(O′/m) = {α ∈ (O′/m)
× : α ≡ 1 (mod m)} is the trivial group, so Um(O′/m)
Um(O/m) is
the trivial group, and thus the map from Clm,Σ(O) to Clm,Σ(O′) is an isomorphism. □

3.2. The flat imprimitive ray class monoid. In [43], the present author and Lagarias
describe several different ray class monoids that extend the usual definition of the ray class
group to the structure of a larger (but still finite) monoid (semigroup with identity). The
present paper requires one of these constructions in particular, the flat imprimitive ray class
monoid, which extends the ray class group to include classes of ideals not coprime to the
modulus.
We extend the ray class group to a monoid by extending J∗
m(O) to a large monoid J
♭
m(O)
still consisting of O-invertible ideals, but relaxing the condition of coprimality to m to a
condition of semilocal integrality at m. We use the term flat (and the corresponding musical
symbol) because nonzero O-ideals are invertible if and only if they are flat as O-modules,
and to avoid the ambiguity of the term “invertible” (as ideals in J♭
m(O) not coprime to m
are invertible as O-ideals but not invertible in the monoid J
♭
m(O)).

Definition 3.6. We define the following submonoid of the group of invertible ideals:

J
♭
m(O) = {a ∈ J
∗(O) : aO[S−1
m ] ⊆ O[S−1
m ]}.

The condition that aO[S−1
m ] ⊆ O[S−1
m ] is equivalent to the condition that aOp ⊆ Op for all
nonzero prime ideals p ⊆ m; we call this condition semilocal integrality at m. Consider the
equivalence relation ∼m,Σ on J
♭
m(O) defined by

a ∼m,Σ b ⇐⇒ ∃c ∈ J
♭
m(O) and α, β ∈ O[S−1
m ] such that a = αc, b = βc,
α ≡ β (mod m) , sgn(ρ(α)) = sgn(ρ(β)) for all ρ ∈ Σ.

The flat imprimitive ray class monoid is

Clm
♭
m,Σ(O) = J♭
m(O)
∼m,Σ .

Classes in the image of the map Clm,Σ(O) ↪→ Clm
♭
m,Σ(O) are called primitive, and other
classes are called imprimitive. The submonoid of zero classes is

ZClm
♭
m,Σ(O) = {[d] ∈ Clm
♭
m,Σ(O) : d ⊆ m}.

We now show that the ray class group embeds into the flat imprimitive ray class monoid
in the expected manner.

Proposition 3.7. The inclusion map J∗
m(O) ↪→ J♭
m(O) induces an injection of monoids
Clm,Σ(O) ↪→ Clm
♭
m,Σ(O).

24 GENE S. KOPP

Proof. Consider a, b ∈ Jm(O). We wish to show that a is equivalent to b in Clm,Σ(O) if and
only if a ∼m,Σ b.
If a is equivalent to b in Clm,Σ(O), then there is some γO ∈ Pm,Σ(O) such that a = γb,
γ ≡ 1 (mod m), and ρ(γ) > 0 for all ρ ∈ Σ. It follows that a ∼m,Σ b by taking c = b and
(α, β) = (1, γ).
Conversely, suppose a ∼m,Σ b. Then there are some c ∈ J
♭
m(O) and α, β ∈ O[S−1
m ] such
that a = αc, b = βc, α ≡ β (mod m), and sgn(ρ(α)) = sgn(ρ(β)) for all ρ ∈ Σ. Since a, b are
coprime to m, it follows (from the equations a = αc and b = βc and the semilocal integrality
of αO, βO, and c) that αO, βO, and c are also coprime to m. Thus, αβ−1 ≡ 1 (mod m).
Also, a = (αβ−1)b, and ρ(αβ−1) for all ρ ∈ Σ, so a and b are equivalent in Clm,Σ(O). □

To facilitate describing the structure of the monoid Clm
♭
m,Σ(O), we define a suitable notion
of an exact sequence of commutative monoids. As in an exact sequence of abelian groups,
we want the fibers of the latter map to be cosets of the image of the former; to guarantee
this property, we impose it directly, because it is not sufficient to say that the image of the
former map is the kernel of the latter.

Definition 3.8. A sequence
 · · · → A α
−→ B β
−→ C → · · ·

of commutative monoids with homomorphisms between them is exact at B if every nonempty
preimage of an element C under β is a coset of an image of α; that is, if for all c ∈ C, either
β−1(c) = ∅, or there exists b ∈ B such that

bα(A) = β−1(c).

A sequence that is exact at all objects with an in-arrow and out-arrow is simply called exact.

We prove a proposition “resolving” the map from Clm
♭
m,Σ(O) to Cl(O) in order to under-

stand the structure of Clm
♭
m,Σ(O).

Proposition 3.9. Let ϕ : Clm
♭
m,Σ(O) → Cl(O) be the map given by ϕ([b]) = [b]. Then,
there is an exact sequence of monoids

(O/m, ×) × {±1}Σ ψ
−→ Clm
♭
m,Σ(O) ϕ
−→ Cl(O) → 1.

Proof. Exactness at Cl(O) is equivalent to the surjectivity of ϕ. By [44, Lem. 5.12] (taking
d = m), every class in Cl(O) is represented by some b ∈ J∗
m(O), and J
∗
m(O) ⊆ J♭
m(O), so ϕ is
surjective.
Define the map ψ : (O/m, ×) × {±1}Σ → Clm
♭
m,Σ(O) by

ψ(α, ϵ) = [αO] where α ≡ α (mod m) and sgn(ρ(α)) = ϵρ.

This map is well-defined because:

(i) For any pair (α, ϵ), the set (α + m) ∩ {α ∈ O : sgn(ρ(α)) = ϵρ} ̸= ∅.
(ii) If α1, α2 ∈ O \ {0}, α1 ≡ α2 (mod m), and sgn(ρ(α1)) = sgn(ρ(α2)), then [α1O] =
[α2O] in Clm
♭
m,Σ(O).

THE SHINTANI–FADDEEV MODULAR COCYCLE 25

To prove exactness at Clm
♭
m,Σ(O), consider a class B ∈ Cl(O). By [44, Lem. 5.12], we
may write B = [b] for some b ∈ J
∗
m(O). Clearly ϕ([αb]) = B for any α ∈ O[S−1
m ] \ {0},
so {[αb] : α ∈ O[S−1
m ] \ {0}} ⊆ ϕ
−1(B). On the other hand, suppose a ∈ J
♭
m(O) such that
ϕ([a]) = B. Then a is equivalent to b in Cl(O), so a = αb for some α ∈ F ×. Moreover, αO =
ab
−1 ∈ J♭
m(O), that is, αO is semilocally integral at m, so α ∈ O[S−1
m ]\{0}. Therefore, {[αb] :
α ∈ O[S−1
m ] \ {0}} = ϕ
−1(B). The left-hand set is the same as [b]ϕ
(
(O/m, ×) × {±1}Σ)
, so

we have proven that the sequence is exact at Clm
♭
m,Σ(O). □

The exact sequence in Proposition 3.9 is related to the ray class group by the following
commutative diagram, where in both rows the image of the first map consists of the classes
of principal ideals.
 (O/m)
× × {±1}
Σ Clm,Σ(O) Cl(O) 1

(O/m, ×) × {±1}
Σ Clm
♭
m,Σ(O) Cl(O) 1
ψ ϕ

The monoid of zero classes has the properties that im(ψ) ∩ ZClm
♭
m,Σ(O) = {(0, ϵ)} (which

does not depend on the choice of ϵ), and ϕ restricts to an isomorphism ZClm
♭
m,Σ(O) ∼= Cl(O).

Example 3.10. This example shows that, in contrast to the case of the ray class group seen
in Proposition 3.5, the surjective monoid homomorphism ext = ext
(O′;m,Σ)
(O;m,Σ) : Clm
♭
m,Σ(O) →

Clm
♭
m,Σ(O′) induced by extension of ideals ext(a) = aO′ need not be an isomorphism when
m is an O′-ideal. Let O = Z[3
√3] and O′ = Z[√3], and consider the unit ε = 2 + √
3. Let
a = 3O and b = 3εO. Then, ext(a) = ext(b) = 3O′.
We show by contradiction that a ̸∼9O′,∅ b. If a ∼9O′,∅ b, then we would have βa = αb
for α ≡ β (mod 9O′). We obtain 3βO = 3εαO, so εαβ−1 ∈ O× = ⟨−1, ε
3⟩, and thus
α = ±ε3n+1β for some n ∈ Z, so ±ε3n+1β ≡ β (mod 9O′). We must have 3εO = b = βc for
c ∈ J♭
9O′(O), so 3O′ = βcO′, and we must have β | 3 in O′ = Z[√3], that is, βγ = 3 for some
γ ∈ O′. Multiplying both sides of the congruence by γ, we obtain ±3ε3n+1 ≡ 3 (mod 9O′),
so ±ε3n+1 ≡ 1 (mod 3O′). Note that ε3 = 26 + 15
√3 ≡ 1 (mod 3O′), so the congruence
simplifies to ±ε ≡ 1 (mod 3O′). But, since ε = 2 + √
3, we obtain a contradiction.

3.3. Key properties of orders. We now recall a few basic results and definitions regarding
orders of number fields.

Proposition 3.11. If O is an order in a number field and a is a fractional O-ideal, the
following are equivalent:
(1) a is invertible as an O-ideal.
(2) For every nonzero prime p of O, the localization ap := aOp is a principal Op-ideal.

Proof. See [44, Prop. 3.8] or [18, Cor. 2.1.7]. □

Definition 3.12. If O is an order in a number field F and a is a fractional O-ideal, the
multiplier ring (or multiplier order ) of a is

ord(a) := (a : a) = {x ∈ F : xa ⊆ a}.

26 GENE S. KOPP

Proposition 3.13. If O is an order in a quadratic field, a is a fractional O-ideal, and
O′ = ord(a), then a is an invertible fractional O′-ideal.

Proof. See [36, p. 557]. □

3.4. The main correspondence. We will now describe classes in ray class groups of real
quadratic fields as corresponding to special “real multiplication” points

Q2/Z
2 × (F \ Q) ρ1
↪−→ Q
2/Z
2 × Rquad ⊂ R2/Z
2 × R

modulo an action of SL2(Z) or GL2(Z). We will use this correspondence is to relate Stark
units (more specifically, Stark–Tangedal–Yamamoto invariants), attached to objects on the
left-hand side of (3.1), to RM values of Shintani–Faddeev modular cocycles, attached to
objects on the right-hand side of (3.1). A similar correspondence can be given in the complex
case, replacing Rquad by the set Hquad of quadratic numbers in the upper half-plane; a notable
difference in the real case is that the action of SL2(Z) on Q2/Z
2 × Rquad is not totally
discontinuous. These correspondences are also related to Gauss composition for quadratic
forms, as will be explored further in [9].

Theorem 3.14. Let O be an order in a real quadratic field F , and let Fquad = F \ Q. Let
m be a nonzero O-ideal and O′ = ord(m). There are explicit compatible functions

Clm
♭
m∞1∞2(O) SL2(Z)\(Q2/Z
2 × Fquad)

Clm
♭
m∞2(O) GL2(Z)\(Q
2/Z
2 × Fquad)

̃Υm

Υm
 (3.1)

where the action of GL2(Z) on Q
2/Z
2 × Fquad is A · (r, β) = (sA(β)Ar, A · β), the quantity
sA(β) = sgn(ρ1(jA(β)), the notation GL2(Z)\(Q2/Z
2 × F ) denotes the set of orbits of this
right action (and similarly for SL2(Z)), and the downward maps are the obvious quotient
maps. If O′ = O, then ̃Υm and Υm are injective. Generally, the image of ̃Υm is described as

im( ̃Υm) = SL2(Z)\MO′,m, where

MO′,m = {(r, β) ∈ Q/Z × FO′ : [[r, β]] m ⊆ βZ + Z}, and

FO′ = {β ∈ F : ord(βZ + Z) = O′}.

In particular, for m ∈ N,
 im( ̃ΥmO) = SL2(Z)\
( 1
m Z2/Z
2 × FO) .

These functions factor through the monoid maps induced by extension of ideals: ̃Υm(A) =
̃Υm(ext
(O′;m∞1∞2)
(O;m∞1∞2) (A)
); Υm(A) = Υm(ext
(O′;m∞2)
(O;m∞2) (A)
). Additionally, the zero classes are

ZClm
♭
m∞1∞2(O) = ̃Υ
−1
m ({0} × Fquad).

The function ̃Υm is described as follows: Given A ∈ Clm
♭
m∞1∞2(O), let A0 be the class of A
in the narrow class group Cl∞1∞2(O). Choose an integral ideal b ∈ A
−1
0 that is coprime to m.
Express bm = α(βZ + Z) with ρ1(α), ρ2(α) > 0 and ρ1(β) > ρ2(β). Choose a representative
γO of bA such that γ ∈ b and ρ1(γ), ρ2(γ) > 0, and write γ = α [[r, β]] for some r ∈ Q
2. Set

̃Υm(A) = SL2(Z) · (r, β).

THE SHINTANI–FADDEEV MODULAR COCYCLE 27

The function Υm(A) is then defined by Υm(A) = GL2(Z) · ̃Υm(̃A) for any choice of lift of A
to ̃A ∈ Clm
♭
m∞1∞2(O).

Proof. We will first show that the map ̃Υm is well-defined, that is, that it does not depend
on the choices of b, α, β, or γ. Consider two such tuples of choices (b1, α1, β1, γ1) and
(b2, α2, β2, γ2), as well as corresponding r1 and r2 such that γj = αj [[rj, βj]]. We have
bjm = αj(βjZ + Z). Moreover, b1m and b2m are both in the ideal class mA
−1
0 , so there exists
some δ ∈ O[S−1
m ]
× such that α1(β1Z + Z) = δα2(β2Z + Z) and ρ1(δ), ρ2(δ) > 0. Thus, there
are integers a, b, c, d, a
′, b
′, c
′, d
′ such that
( α1β1
α1 ) = ( a b
c d ) ( δα2β2
δα2 ) and ( δα2β2
δα2 ) = ( a′ b′
c′ d′ ) ( α1β1
α1 ) .

Thus, the matrices ( a b
c d ) and ( a′ b′
c′ d′ ) are inverses of each other in GL2(Z), and β1 = ( a b
c d ) · β2.
Set A = ( a b
c d ). We have
 ρ1(β1) − ρ2(β1) = A · ρ1(β2) − A · ρ2(β2)

= det(A) (ρ1(β2) − ρ2(β2))
Nm(cβ + d)

= det(A) (ρ1(β2) − ρ2(β2))
Nm(δ−1α1α−1
2 ) ,

and ρ1(β1) − ρ2(β1), ρ1(β2) − ρ2(β2), and Nm(δ−1α1α−1
2 ) are all positive, so det(A) = 1, and
A ∈ SL2(Z).
Since b1m = δb2m and every ideal of a quadratic order is invertible in its multiplier ring,
it follows that b1O′ = δb2O′. Moreover, if f = (O : O′) is the relative conductor, then m ⊇ f;
thus, [44, Prop. 4.8] says that the extension map ext(a) = aO′ defines an isomorphism
Jm(O) → Jm(O′) on fractional ideals coprime to m. Since b1 and δb2 are coprime to m, it
follows that we can “cancel” the factor of O′ and obtain b1 = δb2. Equivalently, δ−1b1 = b2.
We are given that γ1O ∈ b1A, so δ−1γ1O ∈ δ−1b1A = b2A; we are also given that
γ2O ∈ b2A. So δ−1γ1O and γ2O belong to the same class in Clm
♭
m∞1∞2(O); that is, there is
some global unit ε ∈ O such that εδ−1γ1 − γ2 ∈ mO[S−1
m ] and sgn(ρi(εδ−1γ1)) = sgn(ρi(γ2))
for i ∈ {1, 2}. As δ, γ1, γ2 are positive at both real places, it follows that ρi(ε) > 0 for
i ∈ {1, 2}. We may write

ε ( α2β2
α2 ) = E ( α2β2
α2 ) for some E ∈ SL2(Z).

We then have εδ−1 ( α1β1
α1 ) = εA ( α2β2
α2 ) = AE ( α2β2
α2 )
. Write AE = ( e f
g h )
. Thus,

εδ−1γ1 − γ2 = εδ−1(r12α1β1 − r11α1) − (r22α2β2 − r21α2)

= (r12(eα2β2 + f α2) − r11(gα2β2 + hα2)) − (r22α2β2 − r21α2)

= (−gr11 + er12 − r22) α2β2 − (hr11 − f r12 − r21) α2.

Moreover, γ2 ∈ b2, and εδ−1γ1 = δ−1b1 = b2, so

εδ−1γ1 − γ2 ∈ b2 ∩ mO[S−1
m ] = b2m,

because b2 is coprime to m. Thus, −gr11 + er12 − r22 and hr11 − f r12 − r21 are integers, so

(AE)−1r1 = ( h −f
−g e ) r1 ≡ r2 (
mod Z
2) .

28 GENE S. KOPP

We also know that α2jAE(β2) = εδ−1α1, and α1, α2, δ, ε are positive at both real embeddings,
so sAE(β) = 1. Thus, sAE(β)AEr2 ≡ r1 (mod Z
2) and AE · β2 = A · β2 = β1. We have now
established that ̃Υm is well-defined.
We now observe that ̃Υm factors through the induced extension map

ext
O′;m∞1∞2
O;m∞1∞2 : Clm
♭
m∞1∞2(O) → Clm
♭
m∞1∞2(O′).

This is seen by observing that bm = bO′m, and γO ∈ bA =⇒ γO′ ∈ bO′ext
O′;m∞1∞2
O;m∞1∞2 (A),
so the definition of ̃Υm(A) remains unchanged under replacing b by bO′. It follows (because
MO′,m depends only on O′, not on O) that one need only prove the claims about the image
of ̃Υm in the case when O′ = O.
Now suppose that O′ = O; it follows by Proposition 3.13 that m is O-invertible. To
prove that ̃Υm is injective and that it has image specified in the theorem statement, we will
construct a function ̃Ωm : SL2(Z)\MO,m → Clm
♭
m∞1∞2(O)

and show that ̃Ωm defines an inverse to ̃Υm. Consider (r, β) ∈ MO,m such that ρ1(β) >
ρ2(β); note that every SL2(Z)-orbit in Fquad contains such a β. Represent r ∈ Q2/Z
2 by
an element r ∈ Q2 such that [[r, β]] is totally positive. Since ord(βZ + Z) = O, it follows
from Proposition 3.13 that βZ + Z is O-invertible, so (m : βZ + Z) is also O-inverible. By
Proposition 3.11, for every nonzero prime p of O, we have (m : βZ + Z) = αpOp for some αp.
We may choose some α ∈ F × such that α is totally positive, αOp = αpOp whenever p ⊇ m,
and α(βZ + Z) ⊆ m. Setting b = α (βZ + Z : m), it follows that α(βZ + Z) = bm, b is an
integral O-ideal, and b + m = O. Define γ = α [[r, β]] and

̃Ωm(r, β) = [γb
−1] ∈ Clm
♭
m∞1∞2(O).

To show that ̃Ωm is well-defined, consider (r1, β1), (r2, β2) ∈ MO,m such that [[r1, β]] , [[r2, β]]
are totally positive and

(r2, β2) = A · (r1 + n, β1) = (sA(β1)A(r1 + n), A · β1)

for some A = ( a b
c d ) ∈ SL2(Z) and n ∈ Z
2. Consider two choices of α1, α2 as above. These in
turn determine bj = αj (βjZ + Z : m) and γj = αj [[rj, βj]] for j ∈ {1, 2}. We have

γ2 = α2 [[sA(β1)A(r1 + n), A · β1]] = α2sA(β1) [[A(r1 + n), A · β1]]

= α2sA(β1)
jA(β1) [[r1 + n, β1]] = α2sA(β1)
α1jA(β1) (γ1 + α1 [[n, β1]]) . (3.2)

We also have

b2 = α2 (β2Z + Z : m) = α2
 ( aβ1 + b
cβ1 + d Z + Z : m
) = α2
jA(β1) (β1Z + Z : m) = α2
α1jA(β1)b1.

Thus, γ2b
−1
2 = sA(β1) (γ1 + α1 [[n, β1]]) b
−1
1 = (γ1 + α1 [[n, β1]]) b
−1
1 .
Since b1 = α1 (β1Z + Z : m) (and m is O-invertible), we have b1m = α1(β1Z + Z). Thus,
α1 [[n, β1]] ∈ b1m ⊆ m, so γ1 + α1 [[n, β1]] ≡ γ1 (mod m) .
Therefore, γ2b
−1
2 ∼m γ1b
−1
1 . (3.3)

THE SHINTANI–FADDEEV MODULAR COCYCLE 29

Moreover, the αj and γj are totally positive, and sA(β1) = sgn(jA(β1)), so by (3.2) we have
sgn(ρi(γ1 + α1 [[n, β, )]]) = sgn(ρ1(jA(β1))) sgn(ρi(jA(β1))). That is,

sgn(ρ1(γ1 + α1 [[n, β]])) = sgn(ρ1(jA(β1)))
2 = 1, and

sgn(ρ1(γ1 + α1 [[n, β]])) = sgn(Nm(jA(β1))) = sgn( ρ1(β1) − ρ2(β1)
ρ1(β2) − ρ2(β2)
) = 1,

using the conditions that ρ1(βj) > ρ2(βj) in the last step. Hence (3.3) can be improved to

γ2b
−1
2 ∼m∞1∞2 γ1b
−1
1 ,

and therefore the function ̃Ωm is well-defined.
It remains to check that ̃Ωm ◦ ̃Υm is the identity on Clm
♭
m∞1∞2 and ̃Υm ◦ ̃Ωm is the identity
on SL2(Z)\(Q2/Z
2 × Fquad). But these claims follow directly from the definitions of the two
functions. The formula ZClm
♭
m∞1∞2(O) = ̃Ωm({0} × Fquad) = ̃Υ
−1
m ({0} × Fquad) also follows
directly from the construction of ̃Ωm.
In the special case m = mO for m ∈ N, we have

MO,mO = {(r, β) ∈ Q/Z × FO : (r2β − r1)mO ⊆ βZ + Z}

= {(r, β) ∈ Q/Z × FO : r2β − r1 ∈ 1
m (βZ + Z)
}

= 1
m Z/Z × FO.

Thus, im( ̃ΥmO) = SL2(Z)\ ( 1
m Z/Z × FO).
Finally, we must show that quotienting by ∼m∞ on the left-hand side of (3.1) corresponds
under ̃Υm to quotienting on the right-hand side by GL2(Z). (The statements about Υm will
then follow.) Consider the ideal class R−+ ∈ Clm∞1∞2(O) given by

R−+ = {λO : λ ≡ 1 (mod m) , ρ1(λ) < 0 < ρ2(λ)};

then Clm
♭
m∞2(O) is Clm
♭
m∞1∞2(O) modulo the action of {I, R−+} (where I is the identity

class). Consider any A ∈ Clm
♭
m∞1∞2(O). Choose b1 ∈ A−1
0 , and write b1m = α1(β1Z + Z),
γ1O ∈ b1A with γ1 ∈ b1, and γ1 = α1 [[r1, β1]] such that α1, γ1 are totally positive and
ρ1(β1) > ρ2(β1), so that ̃Υm(A) = SL2(Z) · (r1, β1). Choose some A ∈ GL2(Z) such that
det(A) = −1 and ρ2(jA(β1)) < 0 < ρ1(jA(β1)). Choose some n ∈ Z
2 such that δ :=
[[r1 + n, β1]] has ρ1(δ) < 0 < ρ2(δ). Let b2 = jA(β1)b1, α2 = α1jA(β1)2, β2 = A · β1,
γ2 = −jA(β1)δ, and r2 = A(r2 + n) = sA(β)A(r2 + n). We may then check that b2 ∈
jA(β1)A
−1
0 = (R−+A)
−1
0 ,

b2m = jA(β1)α1(βZ + Z) = α1jA(β1)
2((A · β)Z + Z),

γ2O = jA(β1)δO ∈ jA(β1)b1R−+A = b2R−+A, γ2 ∈ b2, and

γ2 = α1jA(β1)
2 [[A(r1 + n), A · β1]] = α2 [[r2, β2]] .

Moreover, α2, γ2 are totally positive, and Nm(jA(β1)) = det(A) ρ1(β1)−ρ2(β1)
ρ1(β2)−ρ2(β2) , and taking the
sign of each factor shows that ρ1(β2) > ρ2(β2). Therefore,

̃Υm(R−+A) = SL2(Z) · (r2, β2) = SL2(Z) · A · (r1, β1) = A · SL2(Z) · (r1, β1) = A · ̃Υm(A).

This proves that Υm defines a function from Clm
♭
m∞2(O) → GL2(Z)\(Q2/Z
2 × Fquad) making
the diagram (3.1) commute. (It then follows from the corresponding statements for ̃Υm that

30 GENE S. KOPP

Υm factors through the induced extension map ext
(O′;m∞2)
(O;m∞2) , that its image is GL2(Z)\MO′,m,
and that is is injective whenever O′ = O.) □

The maps ̃Υm and Υm have some unintuitive behavior that should be pointed out. Firstly,
by varying m, every (r, β) lies in the image of infinitely many ̃Υm. Indeed, if (r, β) ∈ MO,m,
then (r, β) ∈ MO,n for every nonzero O-ideal n ⊆ m.
If (r, β) = ̃Υm(A) for some primitive class A in a ray class group Clm∞1∞2(O), then
(r, β) ∈ MO,n if and only if n ⊆ m and n is O-invertible; in such cases, we may consider A
to be the canonical preimage of (r, β) and m to be the “level” of (r, β). One might hope
that every (r, β) is in the image of a ray class group (rather than only a ray class monoid);
however, that is not always true.

Example 3.15. Let (r, β) = (( 0
1/3 ) , 3
√3
) = (( −2
1/3 ) , 3
√3
)
, where the latter representative
is chosen so that [[r, β]] = √3 + 2 is totally positive. In order for (r, β) ∈ SL2(Z)\Mm,O,
we must have O = ord(
3
√3Z + Z
) = 3√3Z + Z and (
√3 + 2)m ⊆ 3
√
3Z + Z. The latter
condition and the integrality of m implies that

m ⊆ 1
√
3 + 2
 (3
√
3Z + Z
) ∩ (3
√3Z + Z
) = 3
√3Z + 3Z.

However, 3
√3Z + 3Z = 3OQ(
√3) is not O-invertible. In the partial order on ideals, there are
four largest invertible O-ideals contained in 3
√
3Z + 3Z, giving the four possibilities

m ⊆ 9
√3Z + 3Z,

m ⊆ 3
√3Z + 9Z,

m ⊆ (3
√3 + 3)Z + 9Z, or

m ⊆ (3
√3 + 6)Z + 9Z.

Since there is no unique maximum O-invertible value of m for which (r, β) ∈ Mm,O (i.e., no
well-defined “level”), it follows that (r, β) is not in the image of a ray class group.
We give more details in the case m = 9
√3Z + 3Z. We compute ̃Ωm(r, β) by taking α = 3,
b = α (βZ + Z : m) = 3 (O : 3O) = O, and γ = α [[r, β]] = 3√3 + 6. Thus,

̃Ωm(r, β) = [γb
−1] = [(3√3 + 6)O] = [3√
3O] ∈ Clm
♭
m∞1∞2(O).

Thus, (r, β) = ̃Υm([3
√3O]), and the class [3√3O] is imprimitive. (It can similarly be
checked that ̃Ωm(r, β) is imprimitive in the cases m = 3
√3Z + 9Z, m = (3
√
3 + 3)Z + 9Z,
and m = (3
√3 + 6)Z + 9Z. It follows that the same is true for subideals of these.)

This example shows the necessity of working with the pathologies of the ray class monoids
to describe all RM points in terms of ideal-theoretic data defining zeta functions.
Finally, we note some consequences of the reduction theory for binary quadratic forms
for our correspondence. These are important for intermediate steps in Section 7 that use
continued fraction expansions corresponding to reduced representatives.

Definition 3.16. Let A ∈ Clm
♭
m∞1∞2(O) (resp. Clm
♭
m∞2(O)), and write

̃Υm(A) = SL2(Z) · (r, β) (resp. Υm(A) = GL2(Z) · (r, β)).

THE SHINTANI–FADDEEV MODULAR COCYCLE 31

We say that (r, β) is a reduced representative of ̃Υm(A) (resp. Υm(A)) if −1 ≤ r1 < 0,
0 ≤ r2 < 1, and 0 < ρ2(β) < 1 < ρ1(β).

Proposition 3.17. Every ̃Υm(A) (resp. Υm(A)) has at least one, and at most finitely many,
reduced representatives.

Proof. Follows from [39, Thm. 1.3 and Thm. 1.4]. □

4. Modular properties of the q-Pochhammer symbol

In this section, we describe how the q-Pochhammer symbol transforms under modular
transformations and give a framework for understanding the transformation factor as a
modular 1-cocycle or Jacobi 1-cocycle and evaluating its real multiplication values (or more
generally, its stable values), which are cohomological invariants. We define a notion of w-
modular form for a modular cocycle A ↦→ wA; this notion is a multiplicative analogue of
Zagier’s concept of a holomorphic quantum modular form. The q-Pochhammer symbol with
characteristics is a w-modular form for w = ש
r, the Shintani–Faddeev modular cocycle. We
endeavor to keep the theory as simple as possible for now so as not to obscure what’s going
on, postponing more sophisticated cohomological interpretations to Section 5.

4.1. A working definition for first cohomology. Let F be any sheaf of multiplicative
groups of C-valued functions on a topological space X, and let X ◦ be an open subset of X.
Let Γ be a group with a continuous action Γ × X → X. For A ∈ Γ and f ∈ F(U ), we write
f A ∈ F(A
−1 · U ) for the function defined by f A(u) = f (A · u).
We are concerned primarily with sheaves of analytic or meromorphic functions, usually
on connected open sets, for which restriction maps are injective. To lessen the notational
overload, we will not write the restriction maps unless they are needed. In other words, if
U1, U2 ⊆ X and fj ∈ F(Uj), we write

f1 = f2 to mean f1|U1∩U2 = f2|U1∩U2 and

f1f2 to mean (f1|U1∩U2)(f2|U1∩U2).

Additionally, for arbitrary subsets S ⊆ X, we will write F(S) := ⋃
U ⊇S F(U ), where the
union denotes a direct limit over open sets U taken with respect to the restriction maps.
Moreover, for arbitrary S1, S2 ⊆ X, we set FS1(S2) := F(S1 ∩ S2).

Definition 4.1. A system of domains U = (UA)A∈Γ is a Γ-tuple of open subsets of X ◦ that
is also an open cover of X ◦, that is, a map (A ↦→ UA) : Γ → {open subsets of X ◦} such that
X ◦ = ⋃

A∈Γ UA. A 1-cochain for U is an element w = (wA)A∈Γ of the multiplicative group

C 1
U (Γ, F) = ∏

A∈Γ F(UA).

A 1-cocycle for U is an element of the subgroup

Z 1
U (Γ, F) = {w ∈ C 1
U (Γ, F) : wA1A2 = wA2
A1 wA2}.

A 1-coboundary for U is an element of the subgroup

B1
U (Γ, F) = {w ∈ C 1
U (Γ, F) : wA = f Af −1 for some f ∈ F(X ◦)}.

A first cohomology class for U is an element of the quotient group

H 1
U (Γ, F) = Z 1
U (Γ, F)
B1
U (Γ, F).

32 GENE S. KOPP

A cohomology class is typically denoted as [w] for w ∈ Z 1
U (Γ, F).

4.2. Modular and Jacobi cocycles. We now restrict to the group actions and sheaves of
interest for this paper. On any complex manifold, we will denote by A and M the sheaves
of rings of analytic functions and meromorphic functions, respectively, so that A
× and M×

are the sheaves of multiplicative groups of nowhere vanishing analytic functions and nonzero
meromorphic functions, respectively.

Definition 4.2. Suppose X = C ∪ {∞}, X ◦ = C, and Γ is a discrete subgroup of SL2(R)
acting by fractional linear transformations ( a b
c d ) · τ = aτ +b
cτ +d . Suppose H ⊆ UA ⊆ C ∪ {∞}
for A ∈ Γ, and {UA}A∈Γ is an open cover of C. If F = A
× or F = M×, the elements of the
groups C 1
U (Γ, F), Z 1
U (Γ, F), B1
U (Γ, F), and H 1
U (Γ, F) are called modular 1-cochains, modular
1-cocycles, modular 1-coboundaries, and modular first cohomology classes, respectively.

The first example of a weight cocycle is the standard modular cocycle.

Example 4.3. For A = ( a b
c d ) ∈ SL2(R) and τ ∈ C, define

jA(τ ) = cτ + d.

For any Γ ≤ SL2(R), jA is an analytic modular cocycle for the constant system of domains
UA = C.

Definition 4.4. Suppose X = X ◦ = C × (C \ Q) and Γ is a discrete subgroup of R2 ⋊ SL2(R)
acting by the Jacobi action

(m, A) · (z, τ ) = ( z
jA(τ ) + [[m, A · τ ]] , A · τ )

(where A · τ denotes the fractional linear transformation action). Suppose C × H ⊆ UA ⊆ X
for A ∈ Γ, and {UA}A∈Γ is an open cover of X ◦. If F = A
× or F = M×, the elements of
the groups C 1
U (Γ, F), Z 1
U (Γ, F), B1
U (Γ, F), and H 1
U (Γ, F) are called Jacobi 1-cochains, Jacobi
1-cocycles, Jacobi 1-coboundaries, and Jacobi first cohomology classes, respectively.

4.3. Cocycles as generalized modular weights. Recall that a meromorphic modular
form of weight k is a meromorphic function f : H → C whose coboundary is jk
A; that is,
such that f (A · τ ) = jA(τ )kf (τ ) This definition may be generalized so as to replace jk
A by an
arbitrary modular cocycle w.

Definition 4.5. Let w ∈ Z 1
U (Γ, M×
C ) be a modular cocycle for some system of domains U .
A meromorphic complex-valued function f : H → C is a w-modular form 3 if

f (A · τ ) = wA(τ )f (τ )

for all τ ∈ H (except where both sides have a pole).

We also define a compatible generalization of meromorphic Jacobi forms.

3The author has used the term “wannabe modular form” in several talks on the subject but is now aware
that Zagier calls the additive analogues of such functions—that is, f such that f (A · τ ) − f (τ ) or more
generally jA(τ )
−kf (A · τ ) − f (τ ) has a larger domain of analyticity—“holomorphic quantum modular forms.”
The latter terminology has appeared in print in work of Bringmann, Ono, and Wagner [14]. We primarily
use the term “w-modular form” (where the cocycle w is specified) in this work, but when discussing these
objects in general, we refer to them informally as “multiplicative holomorphic quantum modular forms.”

THE SHINTANI–FADDEEV MODULAR COCYCLE 33

Definition 4.6. Let u ∈ Z 1
U (Γ, M×
C×(C\Q)) be a Jacobi cocycle for some system of domains
U . A meromorphic complex-valued function of two variables g(z, τ ) for z ∈ C and τ ∈ H is
a u-Jacobi form if g((m, A) · (z, τ )) = u(m,A)(z, τ )g(z, τ )
for all (z, τ ) ∈ C × H (except where both sides have a pole).

4.4. Stable values and real multiplication values of modular cocycles. In this sec-
tion, we show how a modular 1-cocycle—and indeed, a first cohomology class—can sometimes
be evaluated at a point to produce a numerical value. Doing so requires choosing “canonical”
generators for certain stabilizers. We restrict to the case when Γ is a finite-index subgroup
of SL2(Z).

Definition 4.7. Let Γ be a finite-index subgroup of SL2(Z), and let β ∈ C ∪ ∞. Define A
+
β
to be the unique element of Γ with the following properties:
(1) The stabilizer stabΓ(β) = ⟨A+
β ⟩ (if −I /∈ Γ) or stabΓ(β) = ⟨±I, A+
β ⟩ (if −I ∈ Γ).
(2) The following condition holds in the appropriate case:
– If β ∈ Rquad, then A
+
β ( β
1 ) = λ ( β
1 ) for some λ > 1.
– If β ∈ SL2(Z) · ∞ = Q ∪ {∞}, then A
+
β = P ( 1 b
0 1 ) P −1 for some b > 0 and some
P ∈ SL2(Z).
– If β ∈ SL2(Z) · 1+
√−3
2 , then A+
β = P ( 0 −1
1 −1 ) P −1 for some P ∈ SL2(Z).
– If β ∈ SL2(Z) · √
−1, then A+
β = P ( 0 −1
1 0 ) P −1 for some P ∈ SL2(Z).
– Otherwise, A
+
β = I.

The positivity conditions for choosing a generator of the stabilizer may be understood
geometrically in terms of the fractional linear transformation action. For β ∈ Rquad, the
eigenvalue condition λ > 1 means that A
+
β acts on C ∪ {∞} with β as an attracting fixed
point, dynamically speaking. Additionally, A
+
β preserves the modular geodesic between β
and β′ setwise, and it moves points on this geodesic a distance of 2 log λ toward β in the
hyperbolic metric. For β ∈ Q ∪ {∞}, the matrix A+
β acts by shifting points along horocycles
centered on the point τ = β, and the condition b > 0 specifies the direction of this movement.

Proposition 4.8. Let Γ be a finite-index subgroup of SL2(Z), U a system of domains for Γ,
and w a meromorphic modular 1-cocycle for U . Let β ∈ C ∪ {∞}, and suppose β ∈ UA+
β . If

defined, the value w[β] := wA+
β (β) ∈ C
× depends only on the class of w in Z1
U (Γ,M
×
C )
B1
U (Γ,M×
{β},C) , where

M{β},C denotes the sheaf of meromorphic functions that are analytic at β. In particular,
[w] ∈ H 1
U (Γ, A
×
C ) defines a canonical value [w][β] := w[β] ∈ C
×. For [w] ∈ H 1
U (Γ, M×
C ), we
instead obtain [w][β] ∈ C
×/λ
2Z where λ = jA+
β (β).

Proof. Let A = A
+
β . Consider w, ̃w ∈ Z 1
U (Γ, M×
C ) such that [ ̃w] = [w] ∈ H 1
U (Γ, M×
C ). Then,
we can write
 ̃wA(τ ) = f (A · τ )
f (τ ) wA(τ )

for some f ∈ M
×(C). Near τ = β, we have a Laurent series expansion

f (τ ) =
 ∞∑

k=n ck(τ − β)
k

34 GENE S. KOPP

for some n ∈ Z (possibly negative) and cn ̸= 0. Since β = A · β, writing A = aτ +b
cτ +d , we have

f (A · τ ) =
 ∞∑

k=n ck
 ( aτ + b
cτ + d − aβ + b
cβ + d
 )k

=
 ∞∑

k=n ck
 ( (ad − bc)(τ − β)
(cτ + d)(cβ + d)
 )k

=
 ∞∑

k=n ckjA(β)
−kjA(τ )−k(τ − β)k.

Thus, as τ → β, we have

lim
τ →β f (A · τ )
f (τ ) = lim
τ →β cnjA(β)−njA(τ )−n

cn = jA(β)
−2n.

Hence ̃wA(τ ) = λ−2nwA(τ ) where λ = jA(β). Therefore, [w] ∈ H 1
U (Γ, M×
C ) defines a canonical
element [w][β] ∈ C×/λ
2Z.
Moreover, if f ∈ M×
{β},C(C), then n = 0, so ̃wA(τ ) = wA(τ ). Therefore, the class of w in

Z1
U (Γ,M×
C )
B1
U (Γ,M
×
{β},C) defines a canonical value [w][β] ∈ C
×. □

Definition 4.9. We call w[β] := wA+
β (β) the stable value of w at β; we may also write this
quantity as [w][β] to indicate that it only depends on the class [w] (although we typically
use the former for notational simplicity). If β ∈ Rquad, we also call w[β] (or [w][β]) the real
multiplication value (RM value) of w (or [w]) at β.

We now describe the RM values of jA(τ ) and show that the two uses of λ earlier in this
section are consistent with each other.

Lemma 4.10. If β ∈ C ∪ {∞} and A+
β ( β
1 ) = λ ( β
1 )
, then

j[β] = λ.

Proof. Let A = A
+
β . For any R ∈ GL2(C), we have

jRAR−1(R · β) = jRA(β)jR−1(R · β)

= jR(A · β)jA(β)jR−1(R · β)

= jR(β)jA(β)jR−1(R · β).

But also 1 = jI(β) = jR−1R(β) = jR−1(R · β)jR(β). Thus, jRAR−1(R · β) = jA(β). Choose R
such that RAR−1 is in Jordan form:

RAR−1 = (
λ−1 δ
0 λ
) ,

where δ = 0 if λ ̸= 1. Thus, jA(β) = jRAR−1(R · β) = λ. □

More precisely, we can directly compute in the hyperbolic, parabolic, and elliptic cases,
respectively, that:
• If β ∈ Rquad, then j[β] is a unit in the real quadratic field Q(β).
• If β ∈ SL2(Z) · ∞ = Q ∪ {∞}, then j[β] = 1.
• If β ∈ SL2(Z) · 1+
√−3
2 , then j[β] = −1+
√−3
2 .

THE SHINTANI–FADDEEV MODULAR COCYCLE 35

• If β ∈ SL2(Z) · √
−1, then j[β] = √
−1.
• Otherwise, j[β] = 1.
Moreover, in the hyperbolic case, we have the following characterization of j[β] as the fun-
damental totally positive unit of a certain real quadratic order.

Proposition 4.11. Let β ∈ Rquad and λ = j[β]. If O = (βZ + Z : βZ + Z), then λ is a
generator of the group O×
+ of totally positive units of O.

Proof. Write O×
+ = ⟨ε⟩. Clearly λ is a totally positive unit in O (as it is in O, is greater
than 1, and is the eigenvalue of an integral matrix), so λ is some positive integral power of
ε. On the other hand, ε(βZ + Z) = βZ + Z, so there exists a, b, c, d ∈ Z such that

εβ = aβ + b,
ε = cβ + d.

That is, ε ( β
1 ) = ( a b
c d ) ( β
1 ). Since ε is an eigenvalue of ( a b
c d ), it follows that ε′ = ε−1 is also
an eigenvalue of ( a b
c d ), so det ( a b
c d ) = 1. Therefore, ( a b
c d ) is some integral power of A
+
β , so ε
is an integral power of λ. As we’ve already shown that λ is a positive integral power of ε,
we conclude that λ = ε. □

4.5. Stable values and real multiplication values of Jacobi cocycles. On can define
stable values of Jacobi cocycles is a similar way to stable values of modular cocycles. We will
restrict to irrational β because the Jacobi group action is not well-defined on (C ∪ {∞}) ×
(C ∪ {∞}) but is well-defined on C × (C \ Q). Stable values will be trivial except when
β ∈ Rquad (real multiplication points) and β ∈ (SL2(Z) · √
−1
) ∪ (SL2(Z) · −1+
√−3
2 ) (elliptic
points). It will turn out that (ignoring rational points) the stable values of Jacobi cocycles
are identical to stable values of related modular cocycles.

Definition 4.12. Let Γ be a finite-index subgroup of Z
2 ⋊ SL2(Z). Let β ∈ C \ Q and
ρ ∈ βQ + Q. Define m+
ρ,β to be the unique element of Z2 such that

stabΓ(z, β) = ⟨(m+
ρ,β, B+
ρ,β)⟩ or ⟨(0, −I), (m+
ρ,β, B+
ρ,β)⟩,

where B+
ρ,β = (A
+
β )
k for some k ∈ N and A
+
β is defined with respect to the subgroup Γ∩SL2(Z)
as in Definition 4.7.

Definition 4.13. Let Γ be a finite-index subgroup of Z
2 ⋊ SL2(Z). Let β ∈ C \ Q and
ρ ∈ βQ + Q. Define the stable value of u at (ρ, β) to be

u[ρ, β] := um+
ρ,β ,B+
ρ,β (ρ, β).

If β ∈ Rquad, then u[ρ, β] is also called the real multiplication (RM) value of u at (ρ, β).

Lemma 4.14. Let Γ be a finite-index subgroup of Z
2 ⋊ SL2(Z), and let β ∈ C \ Q. If r ∈ Q2

and ρ = [[r, β]], then m+
ρ,β = (I − B+
ρ,β)r.

Proof. Write m+
ρ,β = m = ( m1
m2 ) and B+
ρ,β = B = ( a b
c d ). The stability condition B · β = β
means that aβ+b
cβ+d = β, that is, cβ2 = (a − d)β + b. Thus,

(−cβ + a)(cβ + d) = −c2β2 + (ac − cd)β + ad

= −c((a − d)β + b) + (ac − cd)β + ad = −bc + ad = 1.

36 GENE S. KOPP

That is, (cβ + d)
−1 = −cβ + a, and it follows that
ρ
jB(β) + [[m, B · β]] = [[r, β]] (cβ + d)−1 + [[m, β]]

= (r2β − r1)(−cβ + a) + (m2β − m1)

= −r2(cβ2) + (cr1 + ar2 + m2β)β − (ar1 + m1)

= −r2((a − d)β + b) + (cr1 + ar2 + m2)β − (ar1 + m1)

= (cr1 + dr2 + m2)β − (ar1 + br2 + m1).

But also ρ
jB(β) + [[m, B · β]] = ρ = r2β − r1, so

(cr1 + dr2 + m2)β − (ar1 + br2 + m1) = r2β − r2. (4.1)

Since β /∈ Q, we can equate coefficients of β and 1 in (4.1), obtaining m2 = −cr1 + (1 − d)r2
and m1 = (1 − a)r1 − br2, that is, m = (I − B)r. □

Proposition 4.15. Let um,A(z, τ ) be a Jacobi cocycle for a finite-index subgroup Γ ≤ Z
2 ∩
SL2(Z) with the property that Γ ∩ (Z
2 ⋊ {I}) = Z
2. For each r ∈ Q2, define an associated
modular cocycle wr
A(τ ) = u(I−A)r,A([[r, τ ]] , τ ).

Then wr is a modular cocycle for the group Γ ∩ Γr. If β ∈ C \ Q and wr[β] is defined, then

u[[[r, β]] , β] = wr[β].

Proof. First, we check the modular cocycle condition. In the Jacobi group, we have the
identity
 ((I − A1)r, A1)((I − A2)r, A2) = ((I − A1)r + (A1 − A1A2)r, A1A2)

= ((I − A1A2)r, A1A2).

The Jacobi action and the modular action are also related by the identity

((I − A)r, A) · ([[r, τ ]] , τ ) = ([[r, τ ]]
jA(τ ) + [[(I − A)r, A · τ ]] A · τ )

= ([[r, A · τ ]] + [[r − Ar, A · τ ]] , A · τ )

= ([[Ar, A · τ ]] , A · τ ) .

Thus, using the Jacobi cocycle condition and the two identities just shown, we have

wr
A1A2(τ ) = u(I−A1A2)r,A1A2([[r, τ ]] , τ )

= u(I−A1)r,A1(((I − A2)r, A2) · ([[r, τ ]] , τ )) u(I−A2)r,A2([[r, τ ]] , τ )

= u(I−A1)r,A1([[A1r, A1 · τ ]] , A1 · τ ) u(I−A2)r,A2([[r, τ ]] , τ )

= wr
A1(A2 · τ )wr
A2(τ ).

Now, we check the equality of stable values. Let m = m+
β and B = B+
β . Then B is also
the positive generator for the stabilizer of β in Γ ∩ Γr (because it is the smallest power of A
+
β
fixing m modulo βZ + Z, or equivalently, fixing r modulo Z2). Therefore, using Lemma 4.14,

u[[[r, β]] , β] = u(I−B)m,B([[r, β]] , β) = wr[β]. □

THE SHINTANI–FADDEEV MODULAR COCYCLE 37

4.6. The Shintani–Faddeev cocycles. We now define the main transcendental functions
of interest in this paper, which give nontrivial examples of a Jacobi cocycle and a modular
cocycle. For now, we define them as coboundaries on M×
H and M×
C×H, which we will later
extend to cocyles on larger systems of domains.
We will define both the “modular” and “Jacobi” versions of the cocycle in terms of special
cases of the following function.

Definition 4.16. For m ∈ R
2, A ∈ SL2(R), z ∈ C, and τ ∈ H, define the following
meromorphic function of z and τ :

σm,A(z, τ ) = ϖ( z
jA(τ ) + [[m, A · τ ]] , A · τ )

ϖ(z, τ ) .

Definition 4.17. The Shintani–Faddeev Jacobi cocycle is the (Z
2 ⋊ SL2(Z))-tuple

(σm,A(z, τ ))(m,A)∈Z2⋊SL2(Z).

Here, we meromorphically continue σm,A(z, τ ) to (z, τ ) ∈ C × DA, where

DA =
 



C \ (−∞, −d/c] if c > 0,
C if c = 0 and d > 0,
H if c = 0 and d < 0,
C \ [−d/c, ∞) if c < 0.
 (4.2)

The existence of the meromorphic continuation will be shown in Theorem 4.29. In the case
when m = 0, we will sometimes drop m and write

σA(z, τ ) := σ0,A(z, τ ) .

Definition 4.18. Let r ∈ Q2. The Shintani–Faddeev modular cocycle (with rational char-
acteristics r) of A ∈ Γr is the Γr-tuple
 (ש
r
A(τ ))A∈Γr,

where שr
A(τ ) = σr,A(0, τ ). Here, we meromorphically continue ש
r
A(τ ) to τ ∈ ̃DA, where

̃DA =
 



 C \ (−∞, −d/c] if c > 0,
C if c = 0,
C \ [−d/c, ∞) if c < 0. (4.3)

The existence of the meromorphic continuation will be shown in Theorem 4.30.

For τ ∈ H, except when r ∈ Z
2 and r2 ≤ 0, we have

ש
r
A(τ ) = ϖr(A · τ )
ϖr(τ ) =
 ∞∏

k=0
 1 − e((k + r2)(A · τ ) − r1)
1 − e((k + r2)τ − r1) .

The Shintani–Faddeev modular cocycle is related to the Shintani–Faddeev Jacobi cocycle
by the following proposition.

Proposition 4.19. The following relations of meromorphic functions hold for r ∈ Q
2, A ∈
Γr, and τ ∈ DA.
ש
r
A(τ ) = σ(I−A)r,A([[r, τ ]] , τ )

38 GENE S. KOPP

= (
e( [[r, τ ]]
j(A, τ )
) , e(A · τ ))−1

[(I−A)r,( 1
0 )] σA([[r, τ ]] , τ ) ; (4.4)

ש
r
A(τ ) = (
e([[
A
−1r, τ ]]) , e(τ )
)[r,(I−A)( 1
0 )] σA([[
A
−1r, τ ]] , τ ) . (4.5)

Proof. For τ ∈ H, write
 ש
r
A(τ ) = ϖr(A · τ )
ϖr(τ ) = ϖ([[r, A · τ ]] , A · τ )
ϖ([[r, τ ]] , τ ) . (4.6)

To prove (4.4), express

[[r, A · τ ]] = [[Ar, A · τ ]] + [[(I − A)r, A · τ ]]

= [[r, τ ]]
jA(τ ) + [(I − A)r, ( A·τ
1 )]

= [[r, τ ]]
jA(τ ) + [(I − A)r, ( 1
0 )] (A · τ ) + [(I − A)r, ( 0
1 )] .

Note that [(I − A)r, ( 1
0 )] and [(I − A)r, ( 0
1 )] are integers because Ar ≡ r (mod Z
2). Apply
Lemma 2.3 to the numerator of (4.6) to prove (4.4).
Similarly, to prove (4.5), express

[[r, τ ]] = [[
A
−1r, τ ]] + [
(I − A−1)r, ( 1
0 )
] τ + [
(I − A
−1)r, ( 0
1 )] ,

and again apply Lemma 2.3, this time to the demoninator of (4.6).
Both (4.4) and (4.5) then hold on DA by meromorphic continuation. □

Remark 4.20. The zeros of the analytic function ϖ(z, τ ) for (z, τ ) ∈ C × H occur exactly
when z ∈ τ N0 + Z, where N0 is the set of nonnegative integers. It follows that, for (m, A) ∈
Z
2 ⋊ SL2(Z), the meromorphic function σm,A(z, τ ) has its poles and zeros at z-values at
lattice points in τ Z + Z, with the poles occurring in a cone and the zeros occurring in the
opposite cone. It may be shown using the double gamma product formula (4.7) that the
locations of the poles and zeros remain the same for (z, τ ) ∈ C × DA. It may further be
shown that the poles and zeros of ש
r
A(τ ) occur at discrete sets of rational numbers.

Remark 4.21. For (m, A) ∈ Z
2 ⋊ SL2(Z), the function σm,A(z, τ ) can be written as a ratio
of q-Pochhammer symbols not only on the upper half-plane H, but also on the lower half-
plane −H. This is done in [24]. The function σm,A(z, τ ) can thus be sensibly defined on
C \ {jA(τ ) ≤ 0} in all cases; this is discussed further in [2].

4.7. The Shintani–Faddeev modular cocycle with half-integral characteristics. As
an aside, we deal with the special cases when r ∈ 1
2Z
2, in which we obtain simple expressions
for ש
r
A(τ ). If r ∈ 1
2Z, then −I ∈ Γr, and the identity ש
r
A(τ ) = ש
r
−A(τ ) implies that שr
A(τ ) is
meromorphic on DA ∪ D−A = C \ {−d/c}. Moreover, from (2.19), we have the relations

ϖ( 0
1 )(τ ) = q−1/24η(τ );

ϖ( 0
1/2 )(τ ) = q1/48 η(τ /2)
η(τ ) ;

ϖ( 1/2
1 )(τ ) = q−1/24 η(2τ )
η(τ ) ;

THE SHINTANI–FADDEEV MODULAR COCYCLE 39

ϖ( 1/2
1/2
 )(τ ) = ζ48q1/48 η((τ + 1)/2)
η(τ ) .

For all A ∈ SL2(Z), let ˆϵA(τ ) = ϵ(τ )ψ(A, ϵ) for any choice of square root function ϵ(τ )
2 =
jA(τ ); the relation ˆϵA(τ ) = η(A·τ )
η(τ ) shows that there is no dependence on the choice of square
root. Let P = ( 1 0
0 2 ), Q = ( 2 0
0 1 ), and R = ( 1 1
0 2 ). We obtain the following relations.

For A ∈ SL2(Z): ש( 0
1 )
A (τ ) = e
(− A·τ
24 ) η(A · τ )
e(
− τ
24) η(τ )

= e
( τ −A·τ
24 ) ˆϵA(τ ).

For A ∈ Γ( 0
1/2 ): ש( 0
1/2 )
A (τ ) = e
( A·τ
48 ) η( A·τ
2 )/η(A · τ )
e
( τ
48) η( τ
2 )/η(τ )

= e
( A·τ −τ
48 ) η(P AP −1 · (P · τ ))/η(P · τ )
η(A · τ )/η(τ )

= e
( A·τ −τ
48 ) ˆϵP AP −1(P · τ )
ˆϵA(τ ) .

For A ∈ Γ( 1/2
1 ): ש( 1/2
1 )
A (τ ) = e
(− A·τ
24 ) η(2(A · τ ))/η(A · τ )
e(
− τ
24) η(2τ )/η(τ )

= e
( τ −A·τ
24 ) η(QAQ−1 · (Q · τ ))/η(Q · τ )
η(A · τ )/η(τ )

= e
( τ −A·τ
24 ) ˆϵQAQ−1(Q · τ )
ˆϵA(τ ) .

For A ∈ Γ( 1/2
1/2
 ): ש
( 1/2
1/2
 )

A (τ ) = e
( A·τ
48 ) η( A·τ +1
2 )/η(A · τ )
e
( τ
48) η( τ +1
2 )/η(τ )

= e
( A·τ −τ
48 ) η(RAR−1 · (R · τ ))/η(R · τ )
η(A · τ )/η(τ )

= e
( A·τ −τ
48 ) ˆϵRAR−1(R · τ )
ˆϵA(τ ) .

In the last three cases, it is noteworthy that:

( ˆϵP AP −1(P · τ )
ˆϵA(τ )
 )2 = jP AP −1(τ )ψ2(P AP −1)
jA(τ )ψ2(A) = jP AP −1(τ )
jA(τ ) = jP (A · τ )
jP (τ ) = 2
2 = 1;

( ˆϵQAQ−1(Q · τ )
ˆϵA(τ )
 )2 = jQAQ−1(τ )ψ2(QAQ−1)
jA(τ )ψ2(A) = jQAQ−1(τ )
jA(τ ) = jQ(A · τ )
jQ(τ ) = 1
1 = 1;

( ˆϵRAR−1(R · τ )
ˆϵA(τ )
 )2 = jRAR−1(τ )ψ2(RAR−1)
jA(τ )ψ2(A) = jRAR−1(τ )
jA(τ ) = jR(A · τ )
jR(τ ) = 2
2 = 1.

Therefore, ש( 0
1/2 )
A (τ ) = ±e
( A·τ −τ
48 ), ש( 1/2
1 )
A (τ ) = ±e( τ −A·τ
24 )
, and ש

( 1/2
1/2
 )

A (τ ) = ±e( A·τ −τ
48 )
, where
the signs depend (only) on A.

40 GENE S. KOPP

4.8. The double sine function. The Shintani–Faddeev Jacobi cocycle of A = S = ( 0 −1
1 0 )
is closely related to Shintani’s double sine function. The double sine function is defined in
terms of the double gamma function originally studied by Barnes [7].

Definition 4.22. For ω1, ω2 ∈ R+ and z ∈ R such that −z /∈ ω1N0 + ω2N0, and s ∈ C such
that Re(s) > 2, define the double zeta function by

ζ2(s, z; ω1, ω2) =
 ∞∑

m=0
 ∞∑

n=0(z + ω1m + ω2n)−s.

This function is holomorphically continued to ω1, ω2 ∈ C and z ∈ C such that Re(ω1) > 0,
Re(ω2) > 0, and Re(z) > 0, and s ∈ C \ {1, 2} by the contour integral formula

ζ2(s, z; ω1, ω2) = Γ(1 − s)
2πi
 ∫

C
 e
−zt

(1 − e−ω1t)(1 − e−ω2t)(−t)s dt
t ,

where C is a contour following the real line from below staring at ∞ − iε, going clockwise
around zero, and following the real line from above to ∞ + iε. See [7, §38] for a proof of this
formula.
Define double gamma function by

Γ2(z; ω1, ω2) := ρ2(ω1, ω2) exp
( d
ds ζ2(s, z; ω1, ω2)
∣
∣
∣
∣s=0
) ,

where ρ2(ω1, ω2) is a nonzero constant independent of z whose exact value is irrelevant to
our considerations. The double gamma function has a product formula

Γ2(z; ω1, ω2)−1 = z exp
(
γ22(ω1, ω2)z + 1
2γ21(ω1, ω2)z2) (4.7)

× ∏

m,n≥0
(m,n)̸=0
 (
1 + z
mω1 + nω2
 ) exp
(
− z
mω1 + nω2 + z2

2(mω1 + nω2)2
 ) ,

which extends Γ2 to a meromorphic function of z ∈ C and ω1, ω2 ∈ C \ {0} such that ω2
ω1 is
not a negative real number. See [7, §19–24] for a proof of this formula and the definition of
γ22(ω1, ω2) and γ21(ω1, ω2).
Define the double sine function (which does not depend on the value of ρ2(ω1, ω2)) by

Sin2(z; ω1, ω2) = Γ2(ω1 + ω2 − z; ω1, ω2)
Γ2(z; ω1, ω2) . (4.8)

(This function is called S2 by Koyama and Kurokawa [45] and Tagedal [74].) We will often
specialize to the case ω2 = 1, in which case we set

Γ2(z, τ ) := Γ2(z; τ, 1),

Sin2(z, τ ) := Sin2(z; τ, 1).

Theorem 4.23 (Shintani). We have the following relation between double sine function and
the Shintani–Faddeev Jacobi cocycle of A = S = ( 0 −1
1 0 ):

σS(z, τ ) = e
( τ − 3 + τ −1

24 + (τ − z)(1 − z)
4τ
 ) (
1 − e( z
τ
 )) Sin2(z, τ )
−1.

Proof. This is a rephrasing of [65, Prop. 5]. □

The restriction ω2 = 1 is not a serious restriction, by the following identity.

THE SHINTANI–FADDEEV MODULAR COCYCLE 41

Proposition 4.24. For any α ∈ C×,

Sin2(αz; αω1, αω2) = Sin2(z, ω1, ω2). (4.9)

In particular,
 Sin2(z; ω1, ω2) = Sin2
( z
ω2 ; ω1
ω2
 ) . (4.10)

Proof. Consider the Laurent series expansion

e−zt
(1−e−ω1t)(1−e−ω2t) = 1
ω1ω2 t
−2 + ω1+ω2−2z
2ω1ω2 + ω2
1+3ω1ω2+ω2
2−6z(ω1+ω2−z)
12ω1ω2 + O(t).

By the residue theorem, we have

ζ2(0, z; ω1, ω2) = 1
2πi
 ∫

C
 e−zt
(1−e−ω1t)(1−e−ω2t) dt
t = ω2
1+3ω1ω2+ω2
2−6z(ω1+ω2−z)
12ω1ω2 .

Moreover, for α > 0, we have

ζ2(s, αz; αω1, αω2) = α−sζ2(s, z; ω1, ω2).

Taking the derivative in s,

ζ ′
2(s, αz; αω1, αω2) = α−sζ ′
2(s, z; ω1, ω2) − (log α)α−sζ2(s, z; ω1, ω2),

and thus
 ζ ′
2(0, αz; αω1, αω2) = ζ ′
2(0, z; ω1, ω2)

− (log α) ω2
1+3ω1ω2+ω2
2−6z(ω1+ω2−z)
12ω1ω2 ;

ζ ′
2(0, α(ω1 + ω2 − z)); αω1, αω2) = ζ ′
2(0, ω1 + ω2 − z; ω1, ω2)

− (log α) ω2
1+3ω1ω2+ω2
2−6z(ω1+ω2−z)
12ω1ω2 .

Thus,
 Sin2(αz; αω1, αω2) = exp (ζ ′
2(0, α(ω1 + ω2 − z)); αω1, αω2) − ζ ′
2(0, αz; αω1, αω2))

= exp (ζ ′
2(0, ω1 + ω2 − z); ω1, ω2) − ζ ′
2(0, z; ω1, ω2))

= Sin2(z; ω1, ω2),

proving (4.9) for α > 0. The claim follows for all α ∈ C
× because the ratio of the two
sides is a meromorphic function in α. Equation (4.10) follows by a specialization of the
variables. □

The double sine function satisfies the following “quasiperiodicity” properties with respect
to the elliptic transformations z ↦→ z + 1 and z ↦→ z + τ .

Proposition 4.25. The double sine function satisfies the identities

Sin2(z + 1, τ ) = (2 sin
(πz
τ
 ))−1 Sin2(z, τ ) and

Sin2(z + τ, τ ) = (2 sin(πz))
−1 Sin2(z, τ ).

Proof. This is a special case of [47, Thm. 2.1]. □

The reader should be aware of different conventions for related functions appearing in the
physics literature, denoted by Sb(z) and Φb(z).

42 GENE S. KOPP

Definition 4.26. The physicist’s double sine function is

Sb(z) := Sin2(z; b, b
−1)
−1.

Faddeev’s noncompact quantum dilogarithm is defined by

Φb(z) = exp ( 1
4
 ∫

C
 e
−2izw

sinh(wb) sinh(wb−1) dw
w
 ) ,

where C is a contour that follows the real line from −∞ the ∞ except near zero, where it
goes into the upper half plane to avoid the pole at w = 0.

The noncompact quantum dilogarithm may be expressed in terms of the Shintani–Faddeev
Jacobi cocycle as follows.

Proposition 4.27. For Im(b2) > 0, we have

Φb(z) = σS
( 1
2 − b2

2 − izb, b2) .

Proof. This formula is given as [29, eq. (53)]. □

There is a fast-converging integral formula for the logarithm of the double sine function.
While we don’t require if for our main results, we have used it to check formulas numerically
in Mathematica.

Proposition 4.28. If 0 < Re(z) < Re(ω1 + ω2), then

Sin2(z; ω1, ω2) = exp
 (
− ∫ ∞

0
 ( sinh (( ω1+ω2
2 − z) t)

2 sinh ( ω1t
2 ) sinh ( ω2t
2 ) − ω1 + ω2 − 2z
ω1ω2t
 ) dt
t
 )
 .

Proof. This formula is stated in the case of Sb(z) = Sin2(z; b, b
−1)−1 in [56, App. B]. The
general case follows by Proposition 4.24. □

4.9. Multiplicative quantum modularity of the q-Pochhammer symbol. From the
definition of σA, we have ϖ ( z
cτ +d , A · τ ) = σA(z, τ ) ϖ(z, τ ). In order to show that ϖ is a
σ-Jacobi form in a nontrivial sense, we need to show that σA(z, τ ) are defined on larger
domains than ϖ is.

Theorem 4.29. The function ϖ(z, τ ) is a meromorphic σA-Jacobi form for Γ = SL2(Z)
with the system of domains DA defined by (4.2). Specifically, it satisfies the elliptic relation

ϖ(z + mτ + n, τ ) = (e(z) , e(τ ))
−1
m ϖ(z, τ )

and the modular relation
 ϖ( z
j(z, τ ), A · τ ) = σA(z, τ ) ϖ(z, τ ),

and σA(z, τ ) is meromorphic on C × DA.

Proof. The elliptic relation is straightforward to check. The modular relation holds by the
definition of σA(z, τ ); however, we must prove that σA(z, τ ) meromorphically continues to
(z, τ ) ∈ C × DA. Write A = ( a b
c d ).
First, note that ϖ(z, τ + b) = ϖ(z, τ ).

THE SHINTANI–FADDEEV MODULAR COCYCLE 43

So, when c = 0 and d > 0, σA(z, τ ) = 1 (and thus is defined for (z, τ ) ∈ C × C). When c = 0
and d < 0, there is nothing to prove.
Now suppose c > 0. Divide a by c with negative remainder to obtain a = ck − c′ for some
k ∈ Z and some c′ ∈ Z with 0 ≤ c′ < c. Set

B = (
a′ b′

c′ d
′
) = S−1T −kA = ( c d
ck − a dk − b
) .

We then have A = T kSB, so by the cocycle condition,

σA(z, τ ) = σT k( z
jSB(τ ), SB · τ ) σS
( z
jB(τ ), B · τ ) σB(z, τ )

= σS
( z
jB(τ ), B · τ ) σB(z, τ ) .

By Theorem 4.23, σS(z′, τ ) analytically continues to all τ ∈ C\(−∞, 0]. Thus, σS( z
jB(τ ), B · τ )

continues (in τ ) to the lower half-plane and the portion of the real line where B · τ > 0. We
have B · τ = a′τ +b′
c′τ +d′ = cτ +d
c′τ +d′ , and cd′ − dc′ = a′d′ − b′c′ = 1, so d′
c′ − d
c = 1
cc′ > 0 and d′
c′ > d
c .

Thus, τ > − d
c implies that B · τ > 0 and σS( z
jB(τ ) , B · τ ) is well-defined. The inequality

c′ < c allows us to induct on c′, and again using the fact the (−∞, − d′
c′ ) ⊆ (
−∞, − d
c )
, we
have shown that σA(z, τ ) meromorphically continues to τ ∈ DA.
If c < 0, we use the relation 1 = σA−1A(z, τ ) = σA−1( z
jA(τ ) , A · τ ) σA(z, τ ). Since A
−1 =
( d −b
−c a )
, the result on positive c tells us that sA(τ ) meromorphically continues the lower half-
plane and to real τ such that A · τ > a
c . It is straightforward to check that this is equivalent
to the condition that τ < − d
c . □

Theorem 4.30. Let r ∈ Q2. The function ϖr(τ ) is a ש
r-modular form for Γr with the
system of domains ̃DA as defined in (4.3). Specifically, it satisfies the modular relation

ϖr(A · τ ) = ש
r
A(τ ) ϖr(τ ),

and ש
r
A(τ ) is meromorphic on ̃DA.

Proof. The modular relation follows by the definition of ש
r
A(τ ). By Proposition 4.19,

ש
r
A(τ ) = (
e([[
A
−1r, τ ]]) , e(τ )
)
[r,(I−A)( 1
0 )] σA([[
A
−1r, τ ]] , τ ) .

Thus, ש
r
A(τ ) extends to a meromorphic function on DA. The domain ̃DA = DA unless c = 0
and d < 0. This final case only arises when −I ∈ Γr, that is, when r ∈ 1
2Z2, and in this case,
we may replace A by −A to show that ש
r
A(τ ) is meromorphic on C. □

4.10. Functional equations of the Shintani–Faddeev cocycles. In this section, we ob-
tain functional equations for σA(z, τ ) and ש
r
A(τ ), using modularity of classical theta functions
discussed in Section 2.

Theorem 4.31. For A ∈ SL2(Z), z ∈ C, and τ ∈ DA,

σA(z, τ ) σA(−z, τ ) = ψ2(A)e( z
2(cτ +d) ) − e
(− z
2(cτ +d))

e
( z
2 ) − e
(− z
2 ) e( τ −A·τ
12 + cz2
2(cτ +d) ) .

44 GENE S. KOPP

Proof. Define the function f (z, τ ) for z ∈ C and τ ∈ H by

f (z, τ ) := ϑ1(z, τ )
η(τ ) .

This function is a meromorphic Jacobi form of weight 0. Specifically, by (2.7) and Theo-
rem 2.7, it satisfies the following modular transformation law for A = ( a b
c d ) ∈ SL2(Z).

f ( z
cτ + d, A · τ ) = ψ2(A)e
( cz2

2(cτ + d)
) f (z, τ ).

By the Jacobi triple product formula, specifically by (2.15),

ϖ(z, τ )ϖ(−z, τ ) = −ie(
− τ
12) (
e
( z
2 ) − e
(− z
2 )) f (z, τ ).

By definition, we have

σA(z, τ ) σA(−z, τ ) = ϖ( z
cτ +d , A · τ ) ϖ(− z
cτ +d , A · τ )

ϖ(z, τ )ϖ(−z, τ ) .

Thus,
 σA(z, τ ) σA(−z, τ ) = −ie(− A·τ
12 ) (e
( z
2(cτ +d) ) − e(− z
2(cτ +d) ))

−ie(
− τ
12) (
e
( z
2 ) − e(
− z
2 )) × f ( z
cτ +d , A · τ )

f (z, τ )

= e(− A·τ
12 ) (e
( z
2(cτ +d) ) − e
(− z
2(cτ +d)))

e(
− τ
12) (
e
( z
2 ) − e(
− z
2 )) × ψ2(A)e
( cz2
2(cτ +d) )

= ψ2(A)e( z
2(cτ +d) ) − e(
− z
2(cτ +d) )

e
( z
2 ) − e(
− z
2 ) e( τ −A·τ
12 + cz2
2(cτ +d) ) . □

We will need a version of the previous theorem for the Shintani–Faddeev cocycle with
characteristics, ש
r
A(τ ).

Theorem 4.32. Let r ∈ Q
2 \ Z2, A ∈ Γr, and τ ∈ ̃DA. We have the identity

שr
A(τ ) ש−r
A (τ ) = ψ2(A)χr(A)e
(( r2
2
2 + 1
12) (τ − A · τ )
) e( r2(A·τ )−r1
2 ) − e( −r2(A·τ )+r1
2 )

e
( r2τ −r1
2 ) − e( −r2τ +r1
2 ) . (4.11)

Proof. For τ ∈ H, define the function fr(τ ) := θr(τ )
η(τ ) . By Theorem 2.14 and (2.7), we have
the modular transformation law

fr(A · τ ) = ψ2(A)χr(A)fr(τ ). (4.12)

Taking z = 0 in Proposition 2.20,

ϖr(τ )ϖ−r(τ ) = ie
(− ( r2
2
2 + 1
12) τ − r2 (−r1 + 1
2)) (e
( r2τ −r1
2 ) − e
( −r2τ +r1
2 )) fr(τ ). (4.13)

By definition,
 ש
r
A(τ ) ש
−r
A (τ ) = ϖr(A · τ )ϖ−r(A · τ )
ϖr(τ )ϖ−r(τ ) . (4.14)

Applying (4.13) to (4.14), and then using (4.12) to simplify the resulting expression, yields
(4.11) for τ ∈ H. The identity extends to τ ∈ ̃DA by analytic continuation. □

THE SHINTANI–FADDEEV MODULAR COCYCLE 45

4.11. Values at rational τ and quantum modularity. In this section, we’ll evaluate
σA(z, τ ) for τ = m
n ∈ DA ∩ Q. The values of σA(z, τ ) at rational τ are not needed for the
main results of this paper. We hope that they may be useful in the future—perhaps further
study of these values could lead to a definition of a p-adic analogue of the Shintani–Faddeev
cocycle using p-adic interpolation. They also suggest a connection to quantum modularity.
Our formula for σA(z, τ ) will be stated in Proposition 4.34 with a restriction on the value
of z. This restriction could potentially be removed by a careful accounting of branch cuts.
The cyclic quantum dilogarithm Dζ(w) is a finite product appearing in the asymptotic
formula describing the behavior of the q-Pochhamer symbol as q approaches an n-th root of
unity ζ. The cyclic quantum dilogarithm plays a role in Garoufalidis and Zagier’s work on
Nahm’s conjecture on the modularity of certain q-hypergeometric series [31]. It is defined as

Dζ(w) :=
 n−1∏

k=1(1 − ζ kw)
k. (4.15)

The behavior of the q-Pochhammer symbol as q approaches a primitive n-th root of unity
ζ is described as follows.

Proposition 4.33. Let ζ be a primitive n-th root of 1. When |w| < 1 and q = e−t/n2ζ for
Re(t) > 0, (w; q)∞ = R(wn, t)Dζ(w)
−1/n(1 + O(t)) as t → 0, (4.16)
where
 R(x, t) := (1 − x)
1/2 exp(− Li2(x)/t)

and the root Dζ(w)−1/n is defined by taking the (−n)-th root of each term in the product
(4.15) using the standard branch of the logarithm.

Proof. This is [8, Prop. 3.2]. □

We can evaluate σA(z, τ ) at τ = m
n in terms of Dζ(w), giving a “quantum modularity”
property for a function related to Dζ(w).

Proposition 4.34. Let A = ( a b
c d ) ∈ SL2(Z), and let m, n ∈ Z, gcd(m, n) = 1, n > 0 such
that jA( m
n ) > 0. For Im(z) > 0,

σA(z, m
n
 ) = De( am+bn
cm+dn )(e
( nz
cm+dn))−1/(cm+dn)

De( m
n )(e(z))
−1/n . (4.17)

Proof. Suppose z ∈ C and τ ∈ H; let ̃z = z
cτ +d and ̃τ = A·τ . Suppose also that τ = m
n − t
2πin2
for a small complex number t with positive real part, and let ̃m = am + bn, ̃n = cm + dn.
We have
 σA(z, τ ) = (e(̃z) ; e(̃τ ))∞
(e(z) ; e(τ ))∞ .

Let ζ = e
( m
n )
. If τ = m
n − t
2πin2 then as t → 0,

̃τ = aτ + b
cτ + d = a m
n + b
c m
n + d − t

2πin2 (
c m
n + d
)2 + O(t
2)

= am + bn
cm + dn − t
2πi(cm + dn)2 + O(t
2)

46 GENE S. KOPP

= ̃m
̃n − t
2πĩn2 + O(t
2).

Also, as t → 0,
 ̃z = nz
cm + dn + O(t).

Let ̃z′ = nz
cm+dn and ̃τ ′ = ̃m
̃n − t
2πĩn2 . Then, it follows from the asymptotic formula in (4.16)
and the continuity in w of the functions on the right-hand side that

lim
t→0 (e(̃z) ; e(̃τ ))∞
(e(̃z′) ; e(̃τ ′))∞ = 1. (4.18)

Let ζ = e
( m
n ) and ̃ζ = e
( ̃m
̃n ). As t → 0, we have by Proposition 4.33 that

(e(z) ; e(τ ))∞ = R(e(nz) , t)Dζ(e(z))
−1/n(1 + O(t)) and

(e(̃z′) ; e(̃τ ′))∞ = R(e(̃ñz′) , t)D̃ζ(e(̃z′))
−1/̃n(1 + O(t)). (4.19)

However, ̃ñz′ = (cm + dn) nz
cm+dn = nz. Thus, by (4.18) and (4.19),

(e(̃z) ; e(̃τ ))∞
(e(z) , e(τ ))∞ = D̃ζ(e(̃z))
−1/̃n

Dζ(e(z))−1/n (1 + O(t)).

Sending t → 0 proves the proposition. □

The restrictions |w| < 1 in Proposition 4.33 and Re(z) > 0 in Proposition 4.34 are there
to avoid branch points of the logarithm and dilogarithm functions and could be removed or
relaxed by a more careful analysis. In particular, both sides of (4.17) analytically continue
in z to a larger domain, so the identity would continue to hold on that larger domain.
Formally, (4.17) seems to imply that f (
z, m
n ) := − 1
n log De( m
n )(e(z)) defines a quantum
Jacobi form of weight 0 in the sense of Bringmann and Folsom [13]. (See also Zagier [82].)
There are a few issues with this: The function f has branch points at z ∈ 1
n Z, and Propo-
sition 4.34 is proven only for Im(z) > 0 and jA( m
n ) > 0. These issues could potentially be
resolved by handling branch cuts carefully to extend the domain of (4.17) and relaxing the
definition of a quantum Jacobi form to allow some undefined values.
The evaluation of ש
r
A(τ ) at rational τ is more subtle due to the possible zeros of Dζ(w).
The details are deferred to later work.

4.12. Special properties of the Shintani–Faddeev cocycle at real multiplication
points. The Shintani–Faddeev cocycle with characteristics has the following pseudolattice
invariance property at fixed points.

Proposition 4.35. Suppose that r ∈ Q2, A ∈ Γr, and β ∈ ̃DA such that A · β = β. Let
n ∈ Z
2. We have the invariance relation

ש
r+n
A (β) =
 



jA(β) שr
A(β) if r ∈ Z
2 and r2 ≤ 0 < r2 + n2,
jA(β)−1 ש
r
A(β) if r ∈ Z
2 and r2 + n2 ≤ 0 < r2,
ש
r
A(β) otherwise.

Proof. Let e1 = ( 1
0 ) and e2 = ( 0
1 ). For τ ∈ H, we have ϖr+e1(τ ) = ϖr(τ ), and thus
ש
r+e1
A (τ ) = ש
r
A(τ ); the latter identity holds for all τ ∈ ̃DA by analytic continuation.

THE SHINTANI–FADDEEV MODULAR COCYCLE 47

Suppose that r1 /∈ Z or r2 ̸= 0. Then, ϖr+e2(τ ) = (1 + e(r2τ − r1))
−1ϖr(τ ) and thus

ש
r+e2
A (τ ) = 1 − e(r2τ − r1)
1 − e(r2(A · τ ) − r1) ש
r
A(τ )

for τ ∈ H. Again by analytic continuation, this identity of meromorphic functions holds for
τ ∈ ̃DA. Setting τ = β, numerator and denominator become equal, and so שr+e1
A (τ ) = שr
A(τ ).
In the case when r1 ∈ Z and r2 = 0, we instead must write

ש
r+e2
A (τ ) = lim
z→0 σr+e2,A(z, τ )

= lim
z→0 1 − e(z)
1 − e(jA(τ )−1z)σr,A(z, τ )

= jA(τ ) e
((1 − jA(τ )
−1)z) ש
r
A(τ ) .

Setting τ = β, we obtain שr+e2
A (β) = jA(β) ש
r
A(β).
The proposition follows by writing n = n1e1 + n2e2 ∈ Z
2 and making an induction
argument. □

Proposition 4.35 does not imply that ש
r
A(β) is doubly periodic as a function of real r ∈ R
2;
it generally isn’t.
At fixed points, the Shintani–Faddeev cocycle with characteristics has a simplified func-
tional equation relating values at r and −r.

Theorem 4.36. Suppose that r ∈ Q2 \ Z
2, A ∈ Γr, and β ∈ ̃DA such that A · β = β. Then,

ש
r
A(β) ש−r
A (β) = ψ2(A)χr(A).

Proof. Follows from Theorem 4.32 by simplifying (4.11) in the case when A · β = β. □

The following theorem shows that the real multiplication values of the Shintani–Faddeev
modular cocycle satisfy a GL2(Z)-invariance property.

Theorem 4.37. Suppose that r ∈ Q2, A ∈ Γr, R ∈ GL2(Z), and β ∈ ̃DA such that A · β = β.
Let sR(β) = sgn(jR(β)), and suppose sR(β) ̸= 0. Then,

ש
sR(β)Rr
RAR−1 (R · β) =
 {
שr
A(β) if det(R) = 1,

שr
A(β) if det(R) = −1. (4.20)

Proof. By Lemma 4.10, jRAR−1(R · β) = jA(β) = λ > 0, so both values of the Shintani–
Faddeev modular cocycle in the statement are well-defined. Moreover, if sR(β) = −1, then
s−R(β) = 1, and (4.20) remains the same upon replacing R by −R; thus, without loss of
generality, we may restrict to the case of sR(β) = 1 (that is, jR(β) > 0).
We will first prove (4.20) in the case when det(R) = 1. Write R = ( a b
c d ) and r = ( r1
r2 ).
For τ ∈ H, we compute

ש
Rr
RAR−1(R · τ ) = ϖRr(R · (A · τ ))
ϖRr(R · τ )

= ϖ((cr1 + dr2) a(A·τ )+b
c(A·τ )+d − (ar1 + br2), a(A·τ )+b
c(A·τ )+d )

ϖ(
(cr1 + dr2) aτ +b
cτ +d − (ar1 + br2), aτ +b
cτ +d )

48 GENE S. KOPP

= ϖ( r2(A·τ )−r1
c(A·τ )+d , a(A·τ )+b
c(A·τ )+d )

ϖ( r2τ −r1
cτ +d , aτ +b
cτ +d ) .

By definition, we also have
 ש
r
A(τ ) = ϖ(r2(A · τ ) − r1, A · τ )
ϖ(r2τ − r1, τ ) .

Dividing, we obtain the identity

ש
Rr
RAR−1(R · τ )

ש
det(R)r
A (τ ) = σR(r2(A · τ ) − r1, A · τ )
σR(r2τ − r1, τ ) .

Taking the limit as τ → β, and using the fact that jR(β) > 0, we obtain

שRr
RAR−1(R · β)
ש
r
A(β) = 1,

proving (4.20) in the case of positive determinant.
Now we deal with the case when det(R) = −1. It is easy to see that (4.20) for R = R1 and
R = R2 implies the statement for R = R1R2, so since we have already proven the statement
for R ∈ SL2(Z), it suffices to prove it for any one matrix of negative determinant; say, fix
R = ( −1 0
0 1 ). Consider τ ∈ H. Then

ϖr(τ ) = (e(r2τ − r1), e(τ ))
∞ = (e(−r2τ + r1) , e(−τ ))∞ = ϖRr(R · τ ). (4.21)

Applying (4.21) to the numerator and demoninator, we have

שA
r (τ ) = ϖr(A · τ )

ϖr(τ ) = ϖRr(AR · τ )
ϖRr(R · τ ) = ש
RAR−1
Rr (R · τ ) .

Sending τ → β proves (4.20) is this (final) case, completing the proof of the lemma. □

Finally, we evaluate the real multiplication values of the Shintani–Faddeev modular cocycle
for r ∈ 1
2Z, showing that they are algebraic units of a simple form. These values are much
simpler than those for r ∈ Q \ 1
2Z that we will relate to Stark units.

Theorem 4.38. Let A ∈ SL2(Z) be non-parabolic, and let β be a fixed point of A with
associated eigenvalue ε. Then, for r ∈ Z
2,

שr
A(β) =
 {
ψ(A, √jA)
√ε if r2 > 0,
ψ(A, √jA) 1√ε if r2 ≤ 0. (4.22)

For r ∈ 1
2Z
2 \ 1
2Z, we have שr
A(β) ∈ {±1}. Therefore, if r ∈ 1
2Z
2, then ש
r
A(β) is an algebraic
unit in an abelian extension of Q(β).

Proof. By Proposition 4.35, it suffices to evaluate ש
r
A(β) for r ∈ {
( 0
1 ) , ( 0
1/2 ) , ( 1/2
1 ) , ( 1/2
1/2 )}.

Taking the principal branch of the square root ϵ(τ ) = √
jA(τ ), we obtain from Section 4.7
the formula

ש
( 0
1 )
A (β) = e( −(A · β) + β
24
 ) ψ(A, √jA)
√jA(β) = ψ(A, √
jA)√
jA(β).

THE SHINTANI–FADDEEV MODULAR COCYCLE 49

By Lemma 4.10, jA(β) = ε, proving (4.22). The fact the שr
A(β) ∈ {±1} for the half-integral
characteristics r ∈ {( 0
1/2 ) , ( 1/2
1 ) , ( 1/2
1/2 )} follows from the last line of Section 4.7.
Moreover, ε is a unit in Q(β) because it is an eigenvalue of an integral matrix of deter-
minant 1 with eigenvector ( β
1 )
, and ψ(A, √jA) is a 24-th root of 1. The maximal abelian
extension Q(β)
ab contains √ε and the 24-th roots of unity. □

Finally, we show an equivalence between stable values (including RM values) of the Jacobi
and modular Shintani–Faddeev cocycles.

Proposition 4.39. If r ∈ Q and β ∈ C \ Q, then

σ[[[r, β]] , β] = ש
r[β].

Proof. Proposition 4.19 gives following identity of meromorphic functions of τ ∈ ̃DA:

ש
r
A(τ ) = σ(I−A)r,A([[r, τ ]] , τ ) .

The claim then follows immediately by Proposition 4.15. □

4.13. Conductor-lowering/level-raising relations. We will now show that certain real
multiplication values of the Shintani–Faddeev modular cocycle can be written as products of
RM values at points of “conductor 1.” The “conductor 1” points correspond to ideal classes
of maximal orders, at which the RM values will be directly related to Stark class invariants
coming from L-functions.
First, we define the conductor of a (real or complex) quadratic number.

Definition 4.40. Suppose β ∈ Cquad is the root of a quadratic polynomial aβ2 + bβ + c = 0
with a, b, c ∈ Z, gcd(a, b, c) = 1. Write b2 − 4ac = ∆ = f 2∆0 where ∆0 is a fundamental
discriminant. We say that f is the conductor of β.
Equivalently, the conductor of β is the conductor of the multiplier ring ord(βZ + Z) =
(βZ + Z : βZ + Z) of the (pseudo-)lattice βZ + Z.

We use the following notation, following Iwaniec [35], for the set of integral matrices of
determinant f .

Definition 4.41. For f ∈ N, define

Gf = {(
a b
c d

) : a, b, c, d ∈ Z, ad − bc = f } .

It turns out that every quadratic number can be obtained from a quadratic number of
conductor 1 by an integral fractional linear transformation.

Lemma 4.42. If β ∈ Rquad is a real quadratic number of conductor f , then there exists
some B ∈ Gf and some α ∈ Rquad of conductor 1 such that β = B · α.

Proof. Let F = Q(β) and b = βZ + Z. Let O be the order of conductor f in F , and let OF
be the maximal order. Write bOF = α1Z + α2Z for some α1, α2 ∈ F . Since b is a sublattice
of bOF , we can write (
β
1
) = (
a b
c d

) (
α1
α2
) .

for some integral change-of-basis matrix B = ( a b
c d ). By general properties of lattices, the
change of basis matrix B has determinant det(B) = ±[bOF : b]. Possibly reordering the
basis {α1, α2}, we may assume det(B) = [bOF : b].

50 GENE S. KOPP

By Proposition 3.13, b is an O-invertible fractional ideal, so the index of b in bOF is

[bOF : b] = [bOF : bO]

= [OF : O] by [44, Prop. A.2]
= f.

Thus, det(B) = f ; that is, B ∈ Gf . If we let α = α1
α2 , then

B · α = a α1
α2 + b

c α1
α2 + d = aα1 + bα2
cα1 + dα2 = β
1 = β. □

The next two lemmas concern the basic properties of Gf and its interactions with with
congruence subgroups of SL2(Z).

Lemma 4.43. Let f, N ∈ N. If A ∈ Γ(f N ) and B ∈ Gf , then B−1AB ∈ Γ(N ).

Proof. Certainly det(B−1AB) = det(A) = 1. Moreover, we may write

A = I + f N A1

for some 2×2 integral matrix A1, where I is the 2×2 identity matrix. Also, since det(B) = f ,
f B−1 is an integral matrix. Thus,

B−1AB = I + N (f B−1)A1B ≡ I (mod N ) .

So B−1AB ∈ Γ(N ). □

Lemma 4.44. The right SL2(Z)-orbits in Gf are represented by upper triangular matrices:

Gf /SL2(Z) = {( a b
0 d ) SL2(Z) : ad = f, 0 ≤ b < a} .

Proof. A matrix ( a b
c d ) ∈ Gf can be integrally column-reduced to a unique matrix of the
desired form using the signed Euclidean algorithm on c and d, multiplying on the right by
products of the matrices ( 1 1
0 1 ) and ( 0 −1
1 0 ), and potentially multiplying by ( −1 0
0 −1 ) in the last
step. The column-reduction matrix has determinant 1. □

We now examine the values of ϖr under the action of the orbit representatives from
Lemma 4.44.

Proposition 4.45. Let r = ( r1
r2 ) ∈ Q2 and a, b, d ∈ Z with 0 ≤ b < a. Then, for τ ∈ H,

ϖr
( aτ + b
d
 ) =
 a−1∏

j=0
 d−1∏

ℓ=0 ϖ
( a b
0 d )
−1( j+r1
ℓ+r2
 )(τ )

Proof. The proof is a direct calculation:

ϖr
( aτ + b
d
 ) =
 ∞∏

k=0
 (1 − e((k + r2) aτ +b
d − r1))

=
 ∞∏

k=0
 (1 − e( a(k+r2)
d τ + ( b(k+r2)
d − r1)))

=
 d−1∏

ℓ=0
 ∞∏

m=0
 (1 − e( a(dm+ℓ+r2)
d τ + ( b(dm+ℓ+r2)
d − r1)))

THE SHINTANI–FADDEEV MODULAR COCYCLE 51

=
 d−1∏

ℓ=0
 ∞∏

m=0
 (1 − e(a (m + ℓ+r2
d ) τ + ( b(ℓ+r2)
d − r1)))

=
 d−1∏

ℓ=0
 ∞∏

m=0
 a−1∏

j=0
 (1 − e
((m + ℓ+r2
d ) τ + 1
a ( b(ℓ+r2)
d − j − r1)))

=
 a−1∏

j=0
 d−1∏

ℓ=0
 ∞∏

m=0
 (1 − e
((m + ℓ+r2
d ) τ − d(j+r1)−b(ℓ+r2)
ad ))

=
 a−1∏

j=0
 d−1∏

ℓ=0 ϖ d(j+r1)−b(ℓ+r2)
ad , ℓ+r2
d (τ )

=
 a−1∏

j=0
 d−1∏

ℓ=0 ϖ( a b
0 d )
−1( j+r1
ℓ+r2
 )(τ ),

using ( a b
0 d )
−1 = 1
ad ( d −b
0 a ) in the last step. □

We now give a “conductor-lowering/level-raising” relation for the RM values of the Shintani–
Faddeev modular cocycle.

Theorem 4.46. Let r ∈ Q/Z, f ∈ Z, and B ∈ Gf . Let A ∈ ⋂

s∈Q2/Z2

Bs−r∈Z2
 Γs. (In particular, this

holds if r ∈ 1
N Z/Z and A ∈ Γ(f N ).) Let α be a fixed point A. Then,

ש
r
BAB−1(B · α) = ∏

s∈Q2/Z2

Bs−r∈Z2
 ש
s
A(α)

Proof. By Lemma 4.44, we can represent B as B = ( a b
0 d ) C for some a, b, d ∈ Z, ad = f ,
0 ≤ b < a, and some C ∈ SL2(Z). Thus, by Proposition 4.45,

ϖr(B · τ ) = ϖr
( a(C · τ ) + b
d
 ) =
 a−1∏

j1=0
 d−1∏

j2=0 ϖ( a b
0 d )−1(j+r)(C · τ )

for all τ ∈ H, where j = ( j1
j2 )
. Thus,

ש
r
BAB−1(B · τ ) = ϖr(B · (A · τ ))
ϖr(B · τ )

=
 a−1∏

j1=0
 d−1∏

j2=0
 ϖ( a b
0 d )
−1(j+r)(CA · τ )

ϖ( a b
0 d )
−1(j+r)(C · τ )

=
 a−1∏

j1=0
 d−1∏

j2=0 ש
( a b
0 d )−1(j+r)

CAC−1 (C · τ ) .

Sending τ → α and using Theorem 4.37 with R = C −1, we obtain

שr
BAB−1(B · α) =
 a−1∏

j1=0
 d−1∏

j2=0 ש
C−1( a b
0 d )−1(j+r)
A (α) =
 a−1∏

j1=0
 d−1∏

j2=0 ש
B−1(j+r)
A (α) .

52 GENE S. KOPP

By Proposition 4.35, ש
B−1(j+r)
A (α) is periodic of period a in j1 and period d in j2. Moreover,
the set of column vectors s ∈ Q
2/Z2 of the form s = B−1(j + r) with j ∈ Z2 are precisely
those such that Bs − r ∈ Z
2. Thus,

ש
r
BAB−1(B · α) = ∏

s∈Q2/Z2

Bs−r∈Z2
 ש
s
A(α) . □

5. Cohomological interpretations of the Shintani–Faddeev cocycles

We will now offer some more formal cohomological perspectives on the groups of “cocycles”
and “cohomology classes” introduced in the previous section. In Section 4, we described the
tuple ש
r = (שr
A)A∈Γr of meromorphic functions as an element of a group Z 1
D(Γr, M×
C ) of “1-
cocycles,” defining a coset class [שr] in a quotient group H 1
D(Γr, M×
C ). A key property of
this “cohomology class” is that the stable values (including the real multiplication values)
are (essentially) independent of the choice of class representative; see Proposition 4.8. We
will now present several ways of describing the group H 1
D(Γr, M×
C ) (and variants thereof) in
a matter resembling existing cohomology theories. Similar constructions can also be used
for the groups of Jacobi cocycles, but we omit the details in that case.
Our cocycles are group-cohomological cocycles, with the essentially modification that they
are valued in abelian groups M×(UA) that vary based on the element A ∈ Γr. In Section 5.1,
we provide a simple generalization of the definition of the first cohomology of a group to
accomodate this modification. In Section 5.2, we provide a more complicated construction
of a sequence of cohomology groups, somewhat akin to equivariant sheaf cohomology; we
connect this construction to H 1
U (Γr, M×
C ) and to a “parabolic” variant in Section 5.3.
These constructions are meant to provide a launching point for any future efforts to de-
scribe the structure of H 1
U (Γr, M×
C ) (or a related group) using tools such as spectral sequences
to study maps between it and better-understood cohomology groups, such as Eichler coho-
mology. They are not intended to be a complete exposition of a new cohomology theory,
nor are they meant to be a final authoritative answer to the question of what group the
Shintani–Faddeev modular cocycle “should” live in.

5.1. Generalized first group cohomology. We first describe a simple modification of the
first group cohomology that encompass the groups described in Section 4.1.
Let Γ be any group and M an abelian group (written multiplicatively) with a compatible
right action of Γ (written as exponentiation). In other words, M is a right ZΓ-module. The
theory of group cohomology associates a series of comomology groups H n(Γ, M ) to the pair
(Γ, M ); see, for example, [63, Ch. VII] for details. The first cohomology group is a quotient
of two subgroups of the group of functions from Γ → M ; we denote evaluation of a function
m : Γ → M at m ∈ M by mg.

H 1(Γ, M ) =
 {m : Γ → M | mg1g2 = mg2
g1mg2}

{m : Γ → M | mg = cgc−1 for some c ∈ M }.

Now, suppose we have a function N : Γ → {subgroups of M } denoted by Ng. We may define
a generalized first cohomology group

̃H 1
N (Γ, M ) =
 {m : Γ → M | mg ∈ Ng, mg1g2 = m
g2
g1mg2}

{
m : Γ → M | mg = cgc−1 for some c ∈ ⋂

g∈Γ Ng}.

THE SHINTANI–FADDEEV MODULAR COCYCLE 53

Now, as in Section 4.1, let F be a sheaf of multiplicative groups of C-valued functions on
a topological space X with a continuous action Γ × X → X. Let U be a system of domains
in the sense of Definition 4.1. If each UA ⊇ H and the restriction maps F(UA) → F(H) are
injective for all A ∈ Γ, then it follows immediately from definitions that, for NA := F(UA),
̃H 1
N (Γ, M ) ∼= H 1
U (Γ, F).

In particular, this isomorphism holds when Γ = Γr, UA = DA, and either F = M× or
F = A
×.

5.2. Equivariant (Q, V )-cohomology of Γ-sheaves. We now describe a more sophisti-
cated approach that that produces higher cohomology groups H n
Q,V (Γ, F, X ◦) associated to
a sheaf on a space with a group action, along with other data.
Let X be a topological space with a continuous action of a group Γ. Let Q be a Γ-set,
that is, a set with a Γ-action. Fix open sets Vq ⊆ X for each n ∈ N and q ∈ Q
n. Suppose
that, for A ∈ Γ and q ∈ Q
n, A · Vq = VA·q
where the action is diagonal, and also suppose that

Vq ⊆
 n⋂

i=0 Vˆqi (5.1)

for q = (q0, . . . , qn) and ˆqi = (q0, . . . , qi−1, qi+1, . . . , qn).
We need the following definition of a Γ-sheaf, which behaves like a sheaf of ZΓ-modules
but is more general.

Definition 5.1. A Γ-sheaf F on X is a sheaf of abelian groups on X along with a “Γ-
action” defined by abelian group maps f ↦→ f A from F(U ) → F(A−1 · U ) commuting
with restriction maps (so that f A|V = (f |V )A for all open sets V ⊆ U ) and satisfying the
compatibility relations f I = f and (f B)
C = f BC. A map of Γ-sheaves is a map of sheaves
of abelian groups that commutes with the Γ-action.

We can define a “fixed sheaf functor” as follows; this functor is left exact.

Definition 5.2. For any Γ-sheaf F on X, we define the fixed sheaf F Γ of abelian groups by

F Γ(U ) = {f ∈ F(U ) : f |U ∩A−1·U = f A|U ∩A−1·U for all A ∈ Γ}.

Additionally, if φ : F → F ′ is a map of sheaves, then for f ∈ F Γ(U ), we define

φΓ
U (f ) = φU (f ).

Together, these data define a functor from the category of Γ-sheaves on X to the category
of sheaves of abelian groups on X.

Proposition 5.3. The fixed sheaf functor is left exact.

Proof. Consider an exact sequence of Γ-sheaves

1 → F1 φ
−→ F2 ψ
−→ F3.

We want to show that the sequence of sheaves of abelian groups

1 → F Γ
1 φΓ
−→ F Γ
2 ψΓ
−→ F Γ
3 .

is exact. To do so, we must show that ker φ
Γ = 1 and im φ
Γ = ker ψΓ.

54 GENE S. KOPP

The first is easy: For each open set U ⊆ X,

(ker φΓ)(U ) = (ker φU ) ∩ F Γ
2 (U ) = 1

because ker φU = 1; thus, ker φΓ = 1.
It remains to show that im φ
Γ = ker ψΓ; it’s clear that (im φΓ)(U ) ⊆ (ker ψΓ)(U ) for each
open set U ⊆ X, so we must show the reverse inclusion. For each U ,

(ker ψΓ)(U ) = (ker ψU ) ∩ F Γ
2 (U ) ⊆ ker ψU = im φU .

Suppose that f2 ∈ (ker ψΓ)(U ), so in particular, f2 ∈ im φU . Write f2 = φU (f1) for some
f1 ∈ F1. Thus, φU (f2) ∈ F Γ
2 (U ), so φU (f A
1 ) = φU (f1)
A = φU (f1). The function φU is
injective, so f A
1 = f1. Thus, f2 ∈ im φ
Γ
U = (im φΓ)(U ). We’ve now shown that (im φ
Γ)(U ) =
(ker ψΓ)(U ) for each U , so im φ
Γ = ker ψΓ. □

Let F be a Γ-sheaf on X with the group operation written multiplicatively. Define the
Γ-sheaf Cn with underlying sheaf of abelian groups

Cn = Cn
Q,V,F = ∏

q∈Qn+1 FVq

and group action defined for f ∈ Cn(U ) by

((fq)q∈Qn+1)
A = (f A
A·q)q∈Qn+1.

To check that Cn is a Γ-sheaf, observe that

(f A)q = f A
A·q ∈ F(A
−1(VA·q ∩ U ) = F(A
−1 · VA·q ∩ A−1 · U ) = F(Vq ∩ A
−1 · U ).

Now consider the complex of sheaves

1 → C0 ∂0−→ C1 ∂1−→ C2 ∂2−→ · · · ,

where the boundary maps are defined (on each Cn(U )) by

(∂nf )q0,...,qn+1 =
 n∏

j=0 f (−1)j
q0,...,qj−1,qj+1,...,qn+1.

We may apply the fixed sheaf functor to obtain a complex of sheaves of abelian groups

1 → (
C0)Γ ∂Γ
0−→ (
C1)Γ ∂Γ
1−→ (
C2)Γ ∂Γ
2−→ · · · .

Finally, we choose a particular open set X ◦ ⊆ X and apply the left exact functor C ↦→ C(X ◦),
φ ↦→ φX ◦ from the category of sheaves of abelian groups to the category of abelian groups.
Taking the induced maps to be dn = (∂Γ
n )X ◦, we obtain a complex of abelian groups

1 → (C0)Γ
(X ◦) d0−→ (C1)Γ
(X ◦) d1−→ (C2)Γ
(X ◦) d2−→ · · · . (5.2)

Definition 5.4. The equivariant (Q, V )-cohomology of F on X ◦ is defined to be the coho-
mology of (5.2), that is,
 H n
Q,V (Γ, F, X ◦) = ker(dn)
im(dn−1).

We will now compute the zeroth and first cohomology groups more explicitly. While not
needed for the definitions above, we will now add the assumption that the Vq cover X ◦.

THE SHINTANI–FADDEEV MODULAR COCYCLE 55

Proposition 5.5. Suppose that ⋃
q∈Q Vq ⊇ X ◦. Then,

H 0
Q,V (Γ, F, X ◦) ∼= F Γ(X ◦).

Proof. By Definition 5.4, the zeroth (Q, V )-cohomology group is

H 0
Q,V (Γ, F, X ◦) = ker(d0)
im(d−1) = ker(d0),

where the dn are as in (5.2). The condition that f ∈ (C0)
Γ
(X ◦) is equivalent to the condition
that f ∈ ∏
q∈Q F(X ◦ ∩ Vq) and fq = (f A)q = f A
A·q. The condition that d0(f ) = 0 means that
fq0 = fq1 for every pair (q0, q1) ∈ Q
2. Therefore, fixing any choice of q0 ∈ Q,

ker(d0) =
 {

f ∈ ∏

q∈Q F(X ◦ ∩ Vq) : fq = fq0 = f A
q0
}
 .

By gluing, the diagonal map defines an isomorphism F Γ(⋃
q∈Q(X ◦ ∩ Vq)
) ∼= ker(d0); more-

over, by hypothesis, F Γ(⋃
q∈Q(X ◦ ∩ Vq)
) = F Γ(X ◦). □

For the computation of the first cohomology, we will also assume that Γ acts transitively
on Q. We give a presentation of the first cohomology that generalizes the usual presentation
of standard group cohomology.

Proposition 5.6. Suppose that ⋃
q∈Q Vq ⊇ X ◦ and that Γ acts transitively on Q. Fix any
q0 ∈ Q, let Γ0 = stabΓ(q0), and choose for each q ∈ Q some Aq ∈ Γ with Aq · q = q0. Then,

H 1
Q,V (Γ, F, X ◦) ∼= Z 1
Q,V (Γ, F, X ◦)
B1
Q,V (Γ, F, X ◦) (5.3)

where
 Z 1
Q,V (Γ, F, X ◦) =
 {

g ∈ ∏

q∈Q F(Vq,q0) : gA1A2·q = gA−1
1
A2·qgA1·q0
}
 ; (5.4)

B1
Q,V (Γ, F, X ◦) =
 {

g ∈ ∏

q∈Q F(Vq,q0) : ∃ h ∈ F Γ0(Vq0)
such that gq = h
Aq h
−1
 }
 . (5.5)

These groups can also be written as

Z 1
Q,V (Γ, F, X ◦) ∼=
 {

w ∈ ∏

A∈Γ F(VA−1·q0,q0) : wA1A2 = wA2
A1 wA2;
wA = 1 for A ∈ Γ0
 }
 ; (5.6)

B1
Q,V (Γ, F, X ◦) ∼=
 {

w ∈ ∏

A∈Γ F(VA−1·q0,q0) : ∃ h ∈ F Γ0(Vq0)
such that wA = h
Ah
−1
 }
 . (5.7)

Proof. By Definition 5.4, the first (Q, V )-cohomology group is

H 1
Q,V (Γ, F, X ◦) = ker(d1)
im(d0) , (5.8)

where the dn are as in (5.2). The condition that f ∈ (C1)
Γ
(X ◦) is equivalent to the condition
that f ∈ ∏
(q1,q2)∈Q2 F(X ◦ ∩ Vq1,q2) and fq1,q2 = (f A)q1,q2 = f A
A·q1,A·q2. The condition that

56 GENE S. KOPP

d1(f ) = 0 means that fq1,q3 = fq1,q2fq2,q3 for every pair (q1, q2, q3) ∈ Q
3. If gq = fq,q0 for
f ∈ ker(d1), then

gA1A2·q = fA1A2·q,q0 = fA1A2·q,A1·q0fA1·q0,q0 = f A−1
1
A2·q,q0fA1·q0,q0 = gA−1
1
A2·qgA1·q0.

Thus, with Z 1
Q,V (Γ, F, X ◦) as defined in (5.4), there is a homomorphism

ker(d1) φ
−→ Z 1
Q,V (Γ, F, X ◦)

f ↦→ (fq,q0)q∈Q,

and the hypothesis that Γ acts transitively on Q ensures that φ is an isomorphism.
Moreover, f ∈ im(d0) if and only if fq1,q2 = hq1h
−1
q2 for some h ∈ (C0)
Γ
(X ◦). By transitivity
of the group action, this is equivalent to the condition that fq,q0 = h
A
q0h
−1
q0 for every A ∈ Γ
such that A · q = q0. In turn, setting h = hq0, this is equivalent to the condition that
fq,q0 = h
Aq h
−1 and h ∈ F Γ0(Vq0). Thus, φ(im(d0)) = B1
Q,V (Γ, F, X ◦) as defined in (5.5).
Therefore, (5.3) follows from (5.8).
Finally, the map sending g ↦→ w where wA = gA−1·q0 defines the isomorphisms (5.6) and
(5.7), having inverse maps defined by gq = wAq . □

5.3. From the working definition to equivariant (Q, V )-cohomology. As in both
Section 4.1 and Section 5.2, let X is a topological space with a continuous action of a group
Γ. As in Section 4.1, let F be a sheaf of multiplicative groups of C-values functions on X.
For A ∈ Γ and f ∈ F(U ), write f A ∈ F(A
−1 ·U ) for the function defined by f A(u) = f (A·u).
We see by inspection that F is a Γ-sheaf in the sense of Definition 5.1.
The cohomology group H 1
U (Γ, F) defined in Section 4.1 is identified with an equivariant
(Γ, V )-cohomology group by the following proposition.

Proposition 5.7. Let (UA)A∈Γ be a system of domains in the sense of Definition 4.1, cov-
ering an open subset X ◦ of X, and suppose UI = X ◦. For any A, B ∈ Γ, set VA = A · X ◦

and VA,B = B · UA−1B. For n ≥ 2, define VA = ⋂n−1
i=0 VAi,Ai+1 for A = (A0, . . . , An) ∈ Γ
n+1.
Then, H 1
U (Γ, F) ∼= H 1
Γ,V (Γ, F, X ◦).

Proof. We check directly that A · VB = AB · X ◦ = VAB, A · VB,C = AC · UB−1C = AC ·
U(AB)−1(AC) = VAB,AC, and thus A · VB = VAB for B ∈ Γ
n+1; the inclusion (5.1) is also
verified directly.
We now apply Proposition 5.6 with Q = Γ and q0 = I. We have VA−1·q0,q0 = VA−1,I = UA
and Γ0 = stabΓ(I) = {I}. Then (5.6) and (5.7) define the same groups of cocycles and
coboundaries as defined in Definition 4.1:

Z 1
U (Γ, F) ∼= Z 1
Γ,V (Γ, F, X ◦);

B1
U (Γ, F) ∼= B1
Γ,V (Γ, F, X ◦).

The proposition follows. □

Writing r = ( p1/q1
p2/q2
 )
, the Shintani–Faddeev modular cocycle satisfies an triviality condition

with respect to the matrix T q2 = ( 1 q2
0 1 )
; specifically, ש
r
T q2 (τ )) = 1. Suppose that r /∈ 1
2Z
2, so
that −I /∈ Γr. Under the fractional linear transformation action of Γr, let

Γr,∞ = stabΓ(∞) = ⟨T q2⟩.

THE SHINTANI–FADDEEV MODULAR COCYCLE 57

The triviality condition can be expressed by stating that שr is a member of the group

Z 1
D,par-∞(Γ, F) :=
 {

w ∈ ∏

A∈Γr F(DA) : wA1A2 = wA2
A1 wA2;
wA = 1 for A ∈ Γr,∞
 }

=
 {

w ∈ ∏

A∈Γr F(DA) : wA1A2 = wA2
A1 wA2; wT q2 = 1

}

with F = M×. We may additionally define

B1
D,par-∞(Γ, F) =
 {

w ∈ ∏

A∈Γr F(DA) : ∃ h ∈ F Γr,∞(C)
such that wA = h
Ah
−1
 }

H 1
D,par-∞(Γ, F) = Z 1
D,par-∞(Γ, F)
B1
D,par-∞(Γ, F). (5.9)

Note that this “parabolic at ∞” cohomology group is not the same as parabolic cohomology
imposing vanishing conditions at every cusp.
For q, q′ ∈ Γr · ∞ with q ̸= q′, define

sgnr(q, q′) =
 {
+1 if (∃ ( a b
c d ) ∈ Γr) (− d
c , ∞) ∈ Γr · (q, q′) and c ≥ 0
−1 if (∃ ( a b
c d ) ∈ Γr) (− d
c , ∞) ∈ Γr · (q, q′) and c < 0

This sign is well-defined because −I /∈ Γr, so in particular −I /∈ Γr,∞. Comparing (5.9)
with Proposition 5.6 and especially (5.6) and (5.7), we immediately obtain the following
proposition, identifying the “parabolic at ∞” cohomology group with an equivariant (Q, V )-
cohomology group for Q = Γr · ∞.

Proposition 5.8. Let r ∈ Q
2 \ 1
2Z
2. Let Q = Γr ·∞ (which is a subset of Q∪{∞} ∼= P1(Q)).
For q, q′ ∈ Q, set Vq = (C ∪ {∞}) \ {q} and

Vq,q′ =
 



(C ∪ {∞}) \ [q′, q] if q ̸= q′ and sgnr(q, q′) = +1,
(C ∪ {∞}) \ [q, q′] if q ̸= q′ and sgnr(q, q′) = −1,
Vq if q = q′.

(Here, for x, y ∈ R, the notation [x, y] is the usual closed interval from x to y if x ≤ y,
and [x, y] := [x, ∞) ∪ {∞} ∪ (−∞, y] if x > y. We define [∞, x] := {∞} ∪ (−∞, x] and
[x, ∞] := [x, ∞) ∪ {∞}.) For n ≥ 2, define Vq = ⋂n−1
i=0 Vqi,qi+1 for q = (q0, . . . , qn) ∈ Γ
n+1
r .
Then, H 1
D,par-∞(Γr, F) ∼= H 1
Q,V (Γr, F, C).

The definition of equivariant (Q, V )-cohomology should be more broadly applicable beyond
the propositions stated and proven in this section. In particular, the Shintani–Faddeev Jacobi
cocycle will be identified with an equivariant (Q, V )-cohomology class for the Jacobi group
Z
2 ⋊ SL2(Z). More generally, one hopes that the definition will apply to (r1 + r2 − 1)-cocycles
for Z
n ⋊ SLn(Z) encoding Kronecker limit formulas for more general number fields F with
[F : Q] = n and F ⊗ R ∼= Rr1 × C
r2. This seems particularly feasible in the totally real case
(r2 = 0, multiple sine functions) and the almost totally real case (r2 = 1, multiple elliptic
gamma functions, including the complex cubic case [11]).
It would also be interesting (in future work) to use this framework to consider additive
cocycles for the weight k action (f |kA)(τ ) := jA(τ )
kf (A · τ ) of finite-index subgroups of

58 GENE S. KOPP

SL2(Z), such as cocycles of holomorphic quantum modular forms, generalizing Eichler co-
homology. More generally, one could consider additive cocycles for the “weight w” action
(f |wA)(τ ) := wA(τ )f (A · τ ) for any multiplicative cocycle wA, including wA = ש
r
A.

6. Partial zeta functions

In this section, we introduce two partial zeta functions, the ray class partial zeta function
and the ideal coset partial zeta function, and we prove that they are closely related. We
also relate the ray class partial zeta function to the Galois-theoretic partial zeta function
appearing in Tate’s refinement of the Stark conjectures. We also discuss statements of the
Stark conjectures in terms of differenced ray class partial zeta functions.

6.1. Ray class partial zeta functions. Let F be a number field and O be an order in F .
Let m be an ideal of O and Σ a subset of the set of real embeddings of F .
To a ray class in the flat imprimitive ray class monoid, we associate a zeta function. (The
dependence of O is implicit in this definition, via the dependence on A.)

Definition 6.1 (Ray class partial zeta function). Let A ∈ Clm
♭
m,Σ(O). For Re(s) > 1, define

ζm,Σ(s, A) = ∑

a∈A
a⊆O
 Nm(a)
−s. (6.1)

In the case of the maximal order, the ray class partial zeta function can be reduced to the
ray class group case.

Proposition 6.2. Let A ∈ Clm
♭
m,Σ(OF ). Choose an ideal c ∈ J
∗
m(OF ) such that cA = [(γ0)]
for some γ0 ∈ OF , and let d = m + γ0OF . Then

ζm,Σ(s, A) = Nm(d)
−sζm′,Σ(s, A
′) (6.2)

where m
′ = d
−1m and A
′ = [γc
−1d−1] ∈ Clm,Σ(OF ).

Proof. By definition of Clm
♭
m,Σ(OF ), for an integral ideal m, we have that

a ∈ A ⇐⇒ ca = γOF with γ ≡ γ0 (mod m) and ρ(γ) > 0 for ρ ∈ Σ
=⇒ ca = γOF with γ ∈ d

=⇒ d|ca

=⇒ d|a because c is coprime to m and thus to d.

Additionally, γd
−1 is coprime to m
′, so A
′ = [γc
−1d−1] defines a class in Clm,Σ(OF ). Moreover,
for integral ideals a ∈ A, the ideals ad
−1 run over all ideals in the class A
′. Equation (6.2)
follows. □

The ray class partial zeta function has an analytic continuation to C \ {1} with a simple
pole at s = 1 [53, Ch. VII, Thm. 5.9]. Taking a difference of two ray class partial zeta
functions cancels the poles and leads to a nicer constant term at s = 1. This behavior led
Stark [71] to study certain differences of partial zeta functions.

Definition 6.3 (Differenced ray class partial zeta function). Let R be the element of
Clm
♭
m,Σ(O) defined by

R := {αO : α ≡ −1 (mod m) and ρ(α) > 0 for all ρ ∈ Σ}.

THE SHINTANI–FADDEEV MODULAR COCYCLE 59

For any ray class A ∈ Clm
♭
m,Σ(O), define

Zm,Σ(s, A) = ζm,Σ(s, A) − ζm,Σ(s, RA).

6.2. Ideal coset partial zeta functions. To a subset Σ of the set of real embeddings of
F and a function (ρ ↦→ ςρ) : Σ → {±1}, associate the cone

CΣ(ς) = {α ∈ F : sgn(ρ(α)) = ςρ for all ρ ∈ Σ}.

Definition 6.4 (Ideal coset partial zeta function). Let b be an ideal of O coprime to m, and
let γ0 ∈ b. Define Cm,Σ(b, γ0, ς) := (γ0 + bm) ∩ CΣ(ς).
The ideal coset partial zeta function is

ξO
m,Σ(s, b, γ0, ς) := ∑

γ∈Cm,Σ(b,γ0,ς)/ Um,Σ(O) Nm(γ)−s.

In the case when m is an ideal of a larger order O′, the zeta functions ζ O
m,Σ and ζ O′
m,Σ are
the same under ideal extension of b. Specifically, Um,Σ(O) = Um,Σ(O) by definition, and

Cm,Σ(b, γ0, ς) = (γ0 + bm) ∩ CΣ(ς) = (γ0 + bO′m) ∩ CΣ(ς) = Cm,Σ(bO′, γ0, ς),

so ξO
m,Σ(s, b, γ0, ς) = ξO′
m,Σ(s, O′b, γ0, ς).

6.3. Equivalence of partial zeta functions. From Proposition 3.9 we have the exact
sequence of multiplicative monoids

(O/m, ×) × {±1}Σ → Clm
♭
m,Σ(O) ϕ
−→ Cl(O) → 1.

For each A0 ∈ Cl(O), the exact sequence gives a surjection

(O/m, ×) × {±1}Σ ψA0−−→→ ϕ
−1(A0).

This surjection is described by the formula ψA0(γ0, ςρ) = [γb
−1], where b ∈ A0 is any rep-
resentative coprime to m, and γ ∈ O satisfying γ ≡ γ0 (mod m) and sgn(ρ(γ)) = ςρ for
ρ ∈ Σ.

Proposition 6.5. Let A0 ∈ Cl(O), and choose an integral ideal b ∈ A
−1
0 such that b is
coprime to m. Let A ∈ Clm
♭
m,Σ(O) such that ϕ(A) = A0. Choose some γ0 ∈ b and ς ∈ {±1}Σ

such that ψA0(γ0, ς) = A, where γ0 is the reduction of γ0 (mod m). Then,

Nm(b)
−sζm,Σ(s, A) = [U(m:m+γ0O),Σ(O) : Um,Σ(O)
]−1 ξO
m,Σ(s, b, γ0, ς).

Proof. For any a ∈ A, write ab = γO for some γ ∈ b such that γ ≡ γ0 (mod m) and
sgn(ρ(γ)) = ςρ. The choice of γ is determined up to a unit that stabilizes γ0 (mod m) and
is positive at the real places in Σ. The group of such units is precisely U(m:m+γ0O),Σ(O). The
map a ↦→ γ defines a bijection

A ∼
−→ Cm,Σ(b, γ0, ς)/ U(m:m+γ0O),Σ(O),
a ↦→ γ.

In terms of zeta functions, we have

Nm(b)
−sζm,Σ(s, A) = ∑

a∈A Nm(ab)
−s

60 GENE S. KOPP

= ∑

γ∈ Cm,Σ(b,γ0,ς)
U(m:m+γ0O),Σ(O)
 Nm(γ)
−s

= [U(m:m+γ0O),Σ(O) : Um,Σ(O)
]−1 ξm,Σ(s, b, γ0, ς). □

6.4. Galois-theoretic partial zeta functions. In this section, we introduce the Galois-
theoretic partial zeta functions used in Tate’s formulation of the rank 1 abelian Stark con-
jecture in [75, Sec. 4].

Definition 6.6 (Galois-theoretic partial zeta function). Let H/F be an abelian Galois ex-
tension of number fields. Let S be a finite set of places of F containing all the places that
ramify in H as well as all the infinite places of F , and let S = Sfin ⊔ S∞ for a set of finite
places Sfin and a set of infinite places S∞. For any σ ∈ Gal(H/F ) and Re(s) > 1, define

ζ Gal
S (σ, s) = ∑

a⊆OF
(∀p∈Sfin)a+p=OF
Art([a])=σ
 Nm(a)−s. (6.3)

In the case when H = H OF
m,Σ is a ray class field of the maximal order, the Galois theoretic
partial zeta function is equal to the ray class partial zeta function.

Theorem 6.7. Let A ∈ Clm,Σ(OF ) for m a nonzero OF -ideal and Σ a subset of the real
places of F . Let σ = Art(A) ∈ Gal(H OF
m,Σ/F ). Let Sfin be the set of primes of OF dividing m,
let S∞ be the set of infinite places of F , and let S = Sfin ⊔ S∞. Then,

ζ Gal
S (σ, s) = ζm,Σ(s, A).

Proof. An integral ideal a ⊆ OF is coprime to every p ∈ Sfin if and only if it is coprime to
m, and Art([a]) = σ if and only if a ∈ A. Thus, the Dirichlet series in (6.3) has the same
terms as the Dirichlet series is (6.1). □

Theorem 6.7 is essentially a restatement of Artin reciprocity, which we have used implicitly
here, in terms of zeta functions.

6.5. The rank 1 abelian Stark–Tate conjecture. We now state Tate’s refinement of the
rank 1 abelian Stark conjecture. The following conjecture appears as [75, (4.2) Conjecture
St(S, K/k)], but we remove several equivalent statements for conciseness. Our notation
differs from Tate’s only in that we denote field extension as H/F rather than K/k.

Conjecture 6.8 (Stark–Tate conjecture ST(S, H/F )). Let H/F be an abelian extension of
number fields, and let W be the number of roots of unity in H. Let S be a finite set of
places of F containing all the places that ramify in H as well as all the infinite places of F ,
satisfying |S| ≥ 2. Suppose that S contains a place p (finite or infinite) that splits completely
in F , and let T = S \ {p}. Let U T
S,H denote the set of elements α ∈ H × such that its Q-adic
valuations at places Q of H satisfy

|α|Q = 1 for Q|q /∈ S,

|α|Q = 1 for Q|q ∈ T, if |T | ≥ 2, and

|α|Q = a for Q|q and a constant, if T = {q}.

THE SHINTANI–FADDEEV MODULAR COCYCLE 61

Then, there is an element ε ∈ U T
S,H such that

log |σ(ε)|P = −W ζ ′
S(σ, 0) for each σ ∈ Gal(H/F ) and P|p

and such that H(ε1/W ) is abelian over F .

While Tate attributes the full conjecture to Stark in the case when p is Archimedean, his
statement is stronger that Stark’s published conjectures even in that case, so we use this
refinement even though only the Archimedean case is important to this paper. Precisely,
Stark conjectured that H(ε1/W ) is normal over F , without claiming in print that the group
Gal(H(ε1/W )/F ) is always abelian [73]. We will need Tate’s refinement to conclude that the
RM values of the Shintani–Faddeev modular cocycle live in abelian extensions of F .
We now give an alternatively statement of a special case of the Stark–Tate conjecture.

Conjecture 6.9. Let F be a real quadratic field and m a nonzero integral OF -ideal such
that m ̸= OF . Let {∞1, ∞2} be the two real places of F and {ρ1, ρ2} the corresponding real
embeddings. Let H = H OF
m∞2, and let ̃ρ1 : H → R be any embedding extending ρ1. Then, for
all A ∈ Clm∞2(OF ), there are elements εA ∈ O×
H such that

̃ρ1(εA) = exp(−2ζ ′
m∞2(0, A)
) ,

(Art(B))(εA) = εAB for B ∈ Clm∞2(OF ), |̃ρ2(εA)| = 1 for all ̃ρ2 extending ρ2, and H(ε1/2) is
abelian over F .

Proposition 6.10. Conjecture 6.8 implies Conjecture 6.9.

Proof. Assume Conjecture 6.8. The real place ∞1 is unramified in H/F , so H has real
embeddings; thus, the number of roots of unity in H is W = 2.
Let S = {prime ideals p|m} ∪ {∞1, ∞2}, and let T = S \ {∞1}. Then |T | ≥ 2, so

U T
S,H = {η ∈ O×
H : |̃ρ2(η)| = 1 for all ̃ρ2 extending ρ2}.

By Conjecture 6.8, there is an element ε of this group such that

log |̃ρ1(σ(ε))| = −2ζ ′
S(σ, 0) for each σ ∈ Gal(H/F ) (6.4)

and such that H(ε1/2) is abelian over F . This statement remains true if ε is replaced by −ε,
so choosing ε appropriately, we may assume ̃ρ1(ε) > 0. Denote also by ̃ρ1 an extension of ̃ρ1
to H(ε1/2), and let ν = ±ε1/2 so that ̃ρ1(ν) > 0. We have ε = ν2, and σ(ε) = σ(ν)
2 for any
σ ∈ Gal(H(ε1/2)/F ), and thus ̃ρ1(σ(ε)) = ̃ρ1(σ(ν))
2 > 0. Since any σ ∈ Gal(H/F ) may be
extended to H(ε1/2), it follows that ̃ρ1(σ(ε)) > 0 in (6.4), and thus

̃ρ1(σ(ε)) = exp(−2ζ ′
S(σ, 0)) for each σ ∈ Gal(H/F ).

For A ∈ Clm∞2(OF ), set εA = (Art(A))(ε). Thus, we have (Art(B))(εA) = εAB, and ζ ′
S(σ, 0) =
ζ ′
m∞2(0, A) by Theorem 6.7, completing the proof. □

We will actually use an essentially equivalent formulation in terms of the differenced
zeta function of a class in the ray class monoid. We show that Conjecture 6.9 (and thus
Conjecture 6.8) implies the statement we need.

Proposition 6.11. Assume Conjecture 6.9. Let F be a real quadratic field and m a nonzero
integral OF -ideal. Let {∞1, ∞2} be the two real places of F and {ρ1, ρ2} the corresponding

62 GENE S. KOPP

real embeddings. Let H = Hm∞2, and let ̃ρ1 : H → R be any embedding extending ρ1. Then,
for all A ∈ Clm
♭
m∞2(OF ), there are elements εA ∈ O×
H such that

̃ρ1(εA) = exp(
−Z ′
m∞2(0, A)) , (6.5)

(Art(B))(εA) = εAB for B ∈ Clm∞2(OF ), |̃ρ2(εA)| = 1 for all ̃ρ2 extending ρ2, and H(ε1/2
A ) is
abelian over F . For A ∈ Clm∞2(OF ), these are the same εA as in Conjecture 6.9.

Proof. If A ∈ ZClm
♭
m∞2(OF ) (including the case m = OF ), then ζm∞2(s, A) = ζm∞2(s, RA),

so Z ′
m∞2(0, A) = 0, and we may take εA = 1. Henceforth, assume A /∈ ZClm
♭
m∞2(OF ).
We now consider A ∈ Clm∞2(OF ). Standard results in the theory of L-functions give

ζm∞2(0, RA) = ζm∞2(0, A); (6.6)

ζ ′
m∞2(0, RA) = −ζ ′
m∞2(0, A). (6.7)

Specifically, (6.7) is proven as [74, Prop. 5] by means of writing the partial zeta functions
in terms of L-functions of finite-order Hecke characters, and (6.6) is proven similarly. Thus,
under the assumption of Conjecture 6.9,

̃ρ1(εA) = exp(−2ζ ′
m∞2(0, A)
) = exp
(−ζ ′
m∞2(0, A) + ζ ′
m∞2(0, RA)) = exp
(−Z ′
m∞2(0, A)
) .

Finally, consider a general A ∈ Clm
♭
m∞2(OF ). In the case when A = [a] with m|a, (6.5)
is trivially true with εA = 1, and the Galois action is trivial. Otherwise, choose an ideal
c ∈ J
∗
m(OF ) such that cA = [(γ0)] for some γ0 ∈ OF , and let d = m + γ0OF , m
′ = d−1m, and
A
′ = [γc
−1d−1] ∈ Clm,Σ(OF ). By Proposition 6.2, we have

Zm,Σ(s, A) = Nm(d)
−sZm′,Σ(s, A
′).

By (6.6), we also have Zm′,Σ(0, A
′) = 0; it follows that Z ′
m,Σ(0, A) = Z ′
m′,Σ(0, A
′). Since A is
not of the form A = [a] with m|a, we know that m
′ ̸= OF . Applying Conjecture 6.9 to A
′

and taking εA = εA′ proves the rest of the proposition. □

7. Partial zeta functions at s = 0 and continued fractions

In this section, we relate this value of a real quadratic ideal coset partial zeta function at
s = 0 to an RM value of the Shintani–Faddeev modular cocycle. That is, we demonstrate
that a formula like that given in Theorem 1.1 is true. We will need to tie up some loose ends
to complete the proof of Theorem 1.1 in Section 8.
Our proof relies on Shintani’s Kronecker limit formula for real quadratic fields, originally
proven in [65]. Many variants of this formula exist. Our presentation most closely follows
Tangedal [74], whose formula builds on earlier work of Zagier [80, 81], Arakawa [3], Hayes
[32], and Sczech [61, 62]. Yamamoto [78] independently developed a similar approach to
Tangedal’s; see Onodera [54] for a comparison.
In this section, to ease the burden of the notation, we will consider our real quadratic field
F to be embedded in R using the real embedding ρ1, so ρ1(β) = β and ρ2(β) = β′ for β ∈ F .

7.1. Hirzebruch–Jung continued fractions. Tangedal’s formulation of Shintani’s for-
mula uses a particular type of continued fraction expansion. Before discussing zeta functions,
we establish some fundamental results about these continued fractions and their connection
to expressions for elements of SL2(Z) in terms of the matrices S = ( 0 −1
1 0 ) and T = ( 1 1
0 1 ).

THE SHINTANI–FADDEEV MODULAR COCYCLE 63

Definition 7.1. For a0, a1, a2, . . . , ak, . . . real numbers, we denote

[a0, a1, a2, . . . , ak]− := a0 − 1

a1 − 1

a2 − 1
. . . − 1
ak
and [a0, a1, a2, . . .]− := lim
k→∞[a0, a1, a2, . . . , ak]− = a0 − 1

a1 − 1

a2 − 1
. . .
provided the limit exists. In the special case when the aj are integers and aj ≥ 2 for all j ≥ 1,
we call these expressions Hirzebruch–Jung continued fractions or HJ continued fractions. For
an irrational real number α, its unique such expression of the form

α = [a0, a1, a2, . . .]−
is its Hirzebruch–Jung (HJ) continued fraction expansion. We will also use the notation
[a0, a1, . . . , ak, ak+1, ak+2, . . . , ak+ℓ]− for a periodic Hirzebruch–Jung continued fraction.

Our terminology follows Popescu–Pampu [57]. These continued fractions play a crucial
role in Hirzebruch’s work on Hilbert modular surfaces [34] and were studied earlier by Jung
in a related context [37]. In the literature, HJ continued fractions are also called “-” con-
tinued fractions [38] or minus continued fractions [39], backwards continued fractions [1, 12],
negative-regular continued fractions [52], reduced regular continued fractions [28], and by-
excess continued fractions [48]. They are closely connected to the SL2(Z) reduction theory
of indefinite integral binary quadratic forms. Proofs of the fundamental properties of HJ
continued fractions and their connection to reduction theory are available in the work of
Svetlana Katok [38, 39].

Proposition 7.2. Let β be a real quadratic number. Then, β has a periodic HJ continued
fraction expansion β = [a0, . . . , ak, b1, . . . , bℓ]−.
This expression is purely periodic if and only if 0 < β′ < 1 < β.

Proof. See [39, Thm. 1.3 and Thm. 1.4]. □

Definition 7.3. If r = ( r1
r2 ), set {r} := ( r1−⌊r1⌋−1
r2−⌊r2⌋ ). That is, {r} ≡ r (mod 1), and {r} = r
if and only if −1 ≤ r1 < 0 and 0 ≤ r2 < 1.

Definition 7.4. Let β be a real quadratic number satisfying 0 < β′ < 1 < β, and let
r ∈ 1
N Z2 \ Z
2 satisfying {r} = r. The associated HJ cycle data are:
• positive integers k, ℓ,
• integers bn ≥ 2, n ∈ Z/ℓZ,
• real quadratic numbers βn for n ∈ Z/ℓZ,
• matrices P ∈ SL2(Z), A ∈ Γr,
• matrices Am,n ∈ SL2(Z) for m, n ∈ Z,
• rn ∈ 1
N Z
2 \ Z
2 for n ∈ Z/kℓZ, and
• real quadratic numbers wn for n ∈ Z/kℓZ.

64 GENE S. KOPP

(Sometimes we will use the term “HJ cycle data” while only requiring a subset of this data.)
They are defined as follows. The number β has a purely periodic Hirzeburch–Jung continued
fraction expansion β = [b0, b1, . . . , bℓ−1]−
of period ℓ; treat the indices as elements of Z/ℓZ, so bn+ℓ = bn. Let β = β0, β1, . . . , βℓ−1 be
the real numbers with Hirzebruch–Jung continued fraction expansions given by the cyclic
permutations of the Hirzebruch–Jung continued fraction expansion of β; that is,

βn = [bn, bn+1 . . . , bn+ℓ−1]−.

Let P = T b0ST b1S · · · T bℓ−1S, so P · β = β and ⟨−I, P ⟩ is the stabilizer of β under of the
SL2(Z)-action by fractional linear transformations. Choose k ∈ N so that A = P k is the
smallest positive power of P in Γr. Define the matrices Am,n for m, n ∈ Z by

Am,n =
 



T bmST bm+1S · · · T bn−1S for m < n,
I for m = n,
(T bnST bn+1S · · · T bm−1S)−1 for m > n.

Thus, An1,n2An2,n3 = An1,n3, A0,ℓ = P , A0,kℓ = A, βm = Am,n · βn, and in particular
βn = An,0 · β = A−1
0,n · β.
Let rn = {An,0r}, and let wn = [[rn, βn]]. The index n ∈ Z/kℓZ.

Lemma 7.5. Let β be a real quadratic number with 0 < β′ < 1 < β, and let βn and Am,n be
associated HJ cycle data, as in Def inition 7.4. Then,

jAm,n(βn) =
 



βm+1 · · · βn if m < n,
1 if m = n,
(βn+1 . . . βm)
−1 if m > n. (7.1)

Proof. If m = n, (7.1) holds because both sides are equal to 1. We will prove the recursion
jAm,n(βn) = βm+1jAm+1,n(βn); then (7.1) will follow by induction on n − m (for m < n) and
induction on m − n (for m > n).
To prove the recursion, use the fact that Am,n = T bmSAm+1,n and the cocycle property of
j. We have:
 jAm,n(βn) = jT bm SAm+1,n(βn)

= jT bm S(Am+1,n · βn)jAm+1,n(βn)

= j( bm −1
1 0
 )jAm+1,n(βn)

= βm+1jAm+1,n(βn). □

Lemma 7.6. Let β be a real quadratic number with 0 < β′ < 1 < β, and let βn be associated
HJ cycle data, as in Def inition 7.4. Let ε > 1 be the smallest totally positive unit greater
than 1 in Q(β) such that ε(βZ + Z) = βZ + Z (that is, ε is the fundamental totally positive
unit of the muliplier ring of βZ + Z). Then, the product

β0 · · · βℓ−1 = ε.

Proof. Follows from Lemma 7.5 and Proposition 4.11. (Note that this lemma is also stated
in [34, p. 215].) □

THE SHINTANI–FADDEEV MODULAR COCYCLE 65

Proposition 7.7. Let β be a real quadratic number, and write

β = [a0, . . . , ak, b0, . . . , bℓ−1]−. (7.2)

Then the 2-by-2 matrix

A = (T a0S · · · T akS)(T b0S · · · T bℓ−1S)(T a0S · · · T akS)−1

defines an element of SL2(Z) with attracting fixed point β. If HJ-expansion (7.2) for β is
primitive, then stabSL2(Z)(β) = ⟨−I, A⟩.

Proof. For any α ∈ R, a direct calculation shows that

T nS ( α
1 ) = α ( [n,α]−
1 ) . (7.3)

Set bi := bi (mod ℓ) for all i ∈ Z, and define the real numbers

αn = [an, . . . , ak, b0, . . . , bℓ−1]− and

βn = [bn, . . . , bn+ℓ−1]−.

Applying (7.3) repeatedly (using induction),

A ( β
1 ) = (α1 · · · αk+1)(β1 · · · βℓ)(α−1
k+1 · · · α−1
1 ) ( β
1 ) = ε ( β
1 ) ,

where ε = β1 · · · βℓ = β0 · · · βℓ−1 > 1 is a generator of the totally positive unit group of O×

for the real quadratic order O = (βZ + Z : βZ + Z) by Lemma 7.6. The group stabSL2(Z)(β)
is a discrete subgroup of

stabSL2(R)(β) = {± ( β β′
1 1 ) ( ev 0
0 e−v ) ( β β′
1 1 )−1 : v ∈ R} .

The eigenvalues of A are ε and ε′ = ε−1, corresponding to v = log ε. A general element of
the stabilizer looks like

± ( β β′
1 1 ) ( ev 0
0 e−v ) ( β β′
1 1 )−1 = ±1
β − β′
 ( βev−β′e−v −ββ′(ev−e−v)
ev−e−v −(β′ev−βe−v) ) ,

so if it is contained in SL2(Z), then e
v − e
−v = (β − β′)m for some m ∈ Z, which is only
possible if v ∈ (log ε)Z. Thus, stabSL2(Z)(β) = ±⟨A⟩ = ⟨−I, A⟩. □

The following lemma relates the HJ continued fraction expansion of a real quadratic num-
ber β with that of its nontrivial Galois conjugate β′.

Lemma 7.8. Let β be a real quadratic number with purely periodic Hirzebruch–Jung con-
tinued fraction expansion

β = [{2}n0, m1 + 3, {2}n1, . . . , mk + 3, {2}nk]−,

for integers mj, nj ≥ 0, where the notation {2}n stands for n consecutive 2s. Then, the
Hirzebruch–Jung continued fraction expansion of β′ is

β′ = [1, nk + 2, {2}mk, nk−1 + 3, {2}mk−1, . . . , n1 + 3, {2}m1, n0 + nk + 3]−.

Proof. By Proposition 7.7, β is the attracting fixed point of

A = (T 2S)
n0 k∏

i=1 T mi+3S(T 2S)
ni.

The Galois conjugate β′ is the attracting fixed point of A−1. To prove the lemma, we express
A
−1 in the form given in the conclusion of Proposition 7.7.

66 GENE S. KOPP

Let B = T ST = ( 1 0
1 1 ), and rewrite A as

A = T Bn0+1 ( k∏

i=1(ST )
−1T mi+1(ST )Bni+1)
 T −1.

Furthermore, using the relation B = ST −1S−1 and setting C = ST S, we may write

A = T ST −(n0+1) ( k∏

i=1 C −1T mi+1CT −(ni+1))
 T S−1T −1

We may then use the relations C = T −1ST −1 and C −1 = T S−1T to write

A = T ST −n0 ( k∏

i=1 S−1T mi+1ST −(ni+1))
 S−1T −1

Inverting A will switch the role of T and T −1, whereas S−1 = −S, and we can now see that
this will essentially switch the role of the mj and the nj. Specifically,

A−1 = T S
 (
k−1∏

i=0 T nk−i+1S−1T −(mk−i+1)S
)
 T n0S−1T −1

= (T ST T nkS−1T −1S−1T −1)D(T ST ST −nkT −1S−1T −1),

where
 D = T ST −mk (k−1∏

i=1 ST nk−i+1S−1T −(mk−i+1))
 ST n0+nk+1S−1T −1S−1T −1

= T ST −mk (k−1∏

i=1 S−1T nk−i+1ST −(mk−i+1))
 ST n0+nk+1S−1T −1S−1T −1

= (T 2S)mk (k−1∏

i=1 T nk−i+3S(T 2S)mk−i)
 T n0+nk+3S.

We also simplify
 T ST T nkS−1T −1S−1T −1 = −T ST nk+2S;

T ST ST −nkT −1S−1T −1 = −(T ST nk+2S)−1.

Thus, A−1 = P DP −1 for P = T ST nk+2S. Using Proposition 7.7 again, the lemma follows.
□

7.2. Shintani’s limit formula and Stark–Tangedal–Yamamoto class invariants.
Shintani’s formula expresses the derivative of a zeta value at zero as a product of values of
the double sine function. In Shintani’s original formulation [65], the product is not uniquely
determined but depends on certain choices. We present a formulation following Tangedal [74]
that gives a canonical product (in the real quadratic case) whose terms are determined by a
certain Hirzebruch–Jung continued fraction expansion.

THE SHINTANI–FADDEEV MODULAR COCYCLE 67

Definition 7.9. Let s ∈ C with Re(s) > 2, x1, x2 > 0 and ω1, ω2 > 0. The Shintani zeta
function in dimension 2 is the function

z2(s, (x1, x2), (ω1, ω2)) :=
 ∞∑

m=0
 ∞∑

n=0 ((x1 + mω1 + n)(x2 + mω2 + n))
−s .

More generally, one may allow the parameters x1, x2, ω1, ω2 to take complex values, but
we do not need to do so in this paper. (As a warning, our use of the variables xi deviates
from Shintani’s [65] and Tangedal’s [74], despite the similar notation.)
The following proposition is a special case of Shintani decomposition, generalized slightly
to the case of arbitrary orders in real quadratic fields. See [53, Chap. VII] for an exposition
of Shintani decomposition for the maximal order in a general totally real number fields.

Proposition 7.10. Let O be an order in a real quadratic field F , and let m be an integral
ideal of O and Σ = {∞1, ∞2}. Let b be a fractional ideal of O. Write bm = α(βZ + Z) for
some α, β ∈ F satisfying 0 < β′ < 1 < β, and such that sgn(ρ(α)) = ςρ for ρ ∈ {ρ1, ρ2}.
Let w0 = [[r0, β]] for some r0 ∈ Q
2 \ Z
2 with {r0} = r0. Associate to β and r0 the HJ
cycle data k, ℓ ∈ Z, bn ∈ Z, βn ∈ F , Am,n ∈ SL2(Z), and wn ∈ F . For each n ∈ Z, let
αn = α(βn+1 · · · β0) if n < 0 and αn = α(β1 · · · βn)−1 if n ≥ 0. Then,
[
Um,Σ(O) : U(m:m+αw0O),Σ(O)]−1 ξm,Σ(s, b, αw0, ς)

=
 kℓ−1∑

n=0 Nm(αn)
−sz2(s, (wn, w′
n), (βn, β′
n)).

Proof. For each n ∈ Z, αn−1Z + αnZ = αn(βnZ + Z). Moreover, βn = bn − β−1
n+1, so

αn(βnZ + Z) = αn ((bn − β−1
n+1) Z + Z
)

= αn+1 ((bnβn+1 − 1) Z + βn+1Z)

= αn+1(βn+1Z + Z).

By an induction argument, αn−1Z+αnZ is independent of n, so αn−1Z+αnZ = α−1Z+α0Z =
α(βZ + Z).
We may write the cone CΣ(ς) as a disjoint union of subcones

CΣ(ς) =
 ∞⊔

n=−∞(αn−1Q≥0 + αnQ>0).

Thus, the cone Cm,Σ(b, αw0, ς) may be written as

Cm,Σ(b, αw0, ς) =
 ∞⊔

n=−∞(αw0 + b ∩ m) ∩ (αn−1Q≥0 + αnQ>0). (7.4)

We have
 w0 − jA0,n(β)−1wn = [[r0, β0]] − jA0,n(β)
−1 [[rn, βn]]

= [[{A0,nrn}, A0,nβn]] − [[A0,nrn, A0,nβn]]

= [[{A0,nrn} − A0,nrn, β]] ∈ βZ + Z.

Since jA0,n(β) = β1 · · · βn by Lemma 7.5, and α(βZ + Z) = αn−1Z + αnZ,

w0 ∈ (β1 · · · βn)−1 wn + βZ + Z, so

68 GENE S. KOPP

αw0 ∈ αnwn + αn−1Z + αnZ.

Moreover, αnwn = αn [[rn, βn]] = αn(rn2βn − rn1) = rn2αn−1 + (−rn1)αn with 0 ≤ rn2 < 1
and 0 < −rn1 ≤ 1. Thus, (αw0 + b ∩ m) ∩ (αn−1Q≥0 + αnQ>0) = αnwn + αn−1Z≥0 + αnZ≥0 =
αn (wn + βnZ≥0 + Z≥0), so we may rewrite the cone decomposition (7.4) as

Cm,Σ(b, αw0, ς) =
 ∞⊔

n=−∞ αn(wn + βnZ≥0 + Z≥0).

Since εk is the smallest totally positive unit in O for which εkαw0 ≡ αw0 (mod m), a funda-
mental domain for the action of U(m:m+αw0),Σ(O) on Cm,Σ(b, αw0, ς) is given by ⊔kℓ−1
n=0 αn(wn +
βnZ≥0 + Z≥0). Thus,

ξm,Σ(s, b, αw0, ς)
[Um,Σ(O) : U(m:m+αw0O),Σ(O)
] = ∑

α∈Cm,Σ(b,αw0,ς)/ U(m:m+αw0O),Σ(O) Nm(α)−s

=
 kℓ−1∑

n=0
 ∞∑

m1=0
 ∞∑

m2=0 Nm(αn(wn + m1βn + m2))
−s

=
 kℓ−1∑

n=0 Nm(αn)
−sz2(s, (wn, w′
n), (βn, β′
n)). □

The following result is proven in Shintani’s original work on his Kronecker limit formula for
real quadratic fields. Shintani’s full proof, by manipulation of a contour integral expression
for the Shintani zeta function, is omitted from this paper.

Lemma 7.11. The Shintani zeta function has a meromorphic continuation in s that is
analytic at s = 0. Let x1, x2, ω1, ω2 > 0, and set r1 = ω2x1−ω1x2
ω1−ω2 and r2 = x1−x2
ω1−ω2 (that is,
x1 = r2ω1 − r1 and x2 = r2ω2 − r1). The evaluation of the Shintani zeta function at s = 0
is given by

z2(0, (x1, x2), (ω1, ω2)) = 1
4 ( 1
ω1 + 1
ω2
 ) B2(−r1) + B1(−r1)B1(r2) + 1
4(ω1 + ω2)B2(r2). (7.5)

The evaluation of the first derivative (in s) of the Shintani zeta function at s = 0 is given by

z′
2(0, (x1, x2), (ω1, ω2)) = log( Γ2(x1, ω1)Γ2(x2, ω2)
ρ2(ω1)ρ2(ω2)
 ) + ω1 − ω2
4ω1ω2 log( ω2
ω1
 ) B2(−r1). (7.6)

In both equations, B1 and B2 denote the Bernoulli polynomials

B1(r) = r − 1
2 and

B2(r) = r2 − r + 1
6.

Proof. The meromorphic continuation of z2 is proven as [64, Prop. 1]. Equation (7.6) is [65,
Prop. 3], and (7.5) is proven within Shintani’s proof of that proposition, on [65, p. 177]. We
have translated both equations into our preferred notation. □

The expressions in Lemma 7.11 become simpler when one takes a certain difference of two
z2-values.
 THE SHINTANI–FADDEEV MODULAR COCYCLE 69

Lemma 7.12. For 0 < x1 < ω1 and 0 < x2 < ω2,

z2(0, (ω1 + 1 − x1, ω2 + 1 − x2), (ω1, ω2)) − z2(0, (x1, x2), (ω1, ω2)) = 0 (7.7)

and
 z′
2(0, (ω1 + 1 − x1, ω2 + 1 − x2), (ω1, ω2)) − z′
2(0, (x1, x2), (ω1, ω2))

= log(Sin2(x1, ω1) Sin2(x2, ω2)) . (7.8)

Proof. As in Lemma 7.11, set r1 = ω2x1−ω1x2
ω1−ω2 and r2 = x1−x2
ω1−ω2 . We have

x1 = r2ω1 − r1, ω1 + 1 − x1 = (1 − r2)ω1 − (−1 − r1),

x2 = r2ω2 − r1, and ω2 + 1 − x2 = (1 − r2)ω2 − (−1 − r1).

Using the relations B1(1 − r) = −B1(−r) and B2(1 − r) = B2(r) together with (7.5), we
obtain (7.7).
Again using the relation B2(1 − r) = B2(r) (specifically, B2(1 + r1) = B2(−r2)), we obtain
cancellation of the second summand of (7.6) in the expression

z′
2(0, (ω1 + 1 − x1, ω2 + 1 − x2), (ω1, ω2)) − z′
2(0, (x1, x2), (ω1, ω2))

= log( Γ2(ω1+1−x1,ω1)Γ2(ω2+1−x2,ω2)
ρ2(ω1)ρ2(ω2) ) − log( Γ2(x1,ω1)Γ2(x2,ω2)
ρ2(ω1)ρ2(ω2) )

= log( Γ2(ω1+1−x1,ω1)Γ2(ω2+1−x2,ω2)
Γ2(x1,ω1)Γ2(x2,ω2) )

= log(Sin2(x1, ω1) Sin2(x2, ω2)) ,

proving (7.8). □

If A is a ray class in Clm∞1∞2(OF ), Tangedal uses the double sine function to define class
invariants U (i)
m (A) ∈ R for i ∈ {1, 2} [74]. He shows that, in the unproven cases of the
real quadratic abelian Stark conjectures, these invariants coincide with positive square roots
of Stark units. Tangedal’s invariants (and similar invariants defined by Yamamoto [78])
generalize in a straightforward manner to both nonmaximal orders and imprimitive classes,
so we describe them in that context.

Definition 7.13. Let O be an order in a real quadratic field F , and let m be an integral ideal
of O. Let A ∈ Clm
♭
m∞1∞2(O). Let (r, β) be a reduced representative of ̃Υm(A). Associate
to (r, β) the HJ cycle data k, ℓ ∈ Z and βi, wi ∈ F . Define the Stark–Tangedal–Yamamoto
invariant
 U (j)
m (A) =
 kℓ−1∏

i=0 Sin2(ρj(wi), ρj(βi)) for j ∈ {1, 2}.

The following proposition is a slight generalization of [74, Prop. 1].

Proposition 7.14. Let O be an order in a real quadratic field F , and let m be an integral
ideal of O. If A ∈ Clm
♭
m∞1∞2(O), then

Z ′
m∞1∞2(0, A) = − log(U (1)
m (A)U (2)
m (A)
) .

Proof. Let b, α, β, r, k, ℓ, βi, and wi be as in Definition 7.13. By Proposition 6.5,

Nm(b)
−sζm,Σ(s, A) = ξm,Σ(s, b, αw0, ς)
[
Um,Σ(O) : U(m:m+αw0O),Σ(O)
].

70 GENE S. KOPP

For each n ∈ Z, let αn = α(βn+1 · · · β0) if n < 0 and αn = α(β1 · · · βn)−1 if n ≥ 0. By
Proposition 7.10,
 ζm,Σ(s, A) = Nm(b)
sξm,Σ(s, b, αw0, ς)
[
Um,Σ(O) : U(m:m+αw0O),Σ(O)]

=
 kℓ−1∑

n=0 Nm(αnb
−1)
−sz2(s, (wn, w′
n), (βn, β′
n)).

Similarly, we apply the same results to ζm,Σ(s, RA). The associated HJ cycle data include
̃wn = β + 1 − wn, and one obtains

ζm,Σ(s, RA) = Nm(b)
sξm,Σ(s, b, α ̃w0, ς)
[
Um,Σ(O) : U(m:m+αw0O),Σ(O)
]

=
 kℓ−1∑

n=0 Nm(αnb
−1)
−sz2(s, ( ̃wn, ̃w′
n), (βn, β′
n)).

Subtracting, and using the fact that Zm,Σ(s, A) = 0 by (6.6), we have

Z ′
m,Σ(0, A) =
 kℓ−1∑

n=0 (z′
2(0, (wn, w′
n), (βn, β′
n)) − z′
2(0, ( ̃wn, ̃w′
n), (βn, β′
n)))

=
 kℓ−1∑

n=0 − log(Sin2(wn, βn) Sin2(w′
n, β′
n)) by Lemma 7.12

= − log(
U (1)
m (A)U (2)
m (A)
) ,

proving the proposition. □

The following theorem may be compared to [74, Thm. 1].

Theorem 7.15. Let O be an order in a real quadratic field F , and let m be an integral
O-ideal. Consider the surjective monoid map ϕ : Clm
♭
m∞1∞2(O) → Clm
♭
m∞2(O). If A ∈

Clm
♭
m∞2(O) \ ZClm
♭
m∞2(O), and ̃A ∈ Clm
♭
m∞1∞2(O) such that ϕ(̃A) = A, then U (1)(A) :=
U (1)(̃A) is well-defined. Moreover,

Z ′
m∞2(0, A) = −t log(
U (1)
m (A)
) ,

where t = |ϕ
−1(A)| ∈ {1, 2}. Additionally, U (1)(A) depends only on Υm(A).

Proof. Define the following classes in Clm∞1∞2(O):

R+− = {γO : γ ≡ 1 (mod m) , ρ1(γ) > 0, ρ2(γ) < 0},

R−+ = {γO : γ ≡ 1 (mod m) , ρ1(γ) < 0, ρ2(γ) > 0}, and

R−− = {γO : γ ≡ 1 (mod m) , ρ1(γ) < 0, ρ2(γ) < 0} = R+−R−+.

In Clm∞2(O), we also have

R = {γO : γ ≡ 1 (mod m) , ρ2(γ) < 0} = R+− ∪ R−−.

THE SHINTANI–FADDEEV MODULAR COCYCLE 71

Choose some ̃A ∈ Clm∞1∞2(O) such that ϕ(̃A) = A. It may be shown by the same method
as [3, Prop. 7] and [74, Cor. 1] that

U (1)
m (R−+ ̃A) = U (1)
m (̃A) and U (2)
m (R−+ ̃A) = (U (2)
m (̃A)
)−1 ; (7.9)

we omit the details. We complete the proof by cases.
Case 1: Assume that t = 1. Then R−+A = A and R−−A = R+−A. By (7.9), it follows that
(U (2)
m (R−+ ̃A)
)2 = 1; the properties of the double sine function also imply that U (2)
m (̃A) > 0

(because all the terms in the product defining it are positive), so U (2)
m (̃A) = 1. We have
Zm∞2(s, A) = Zm∞1∞2(s, ̃A), so by Proposition 7.14

Z ′
m∞2(0, A) = − log(U (1)
m (̃A)U (2)
m (̃A)) = − log(U (1)
m (̃A)) .

Case 2: Now assume that t = 2. Write A = ̃A ∪ R−+ ̃A, RA = R+− ̃A ∪ R−− ̃A, and

Zm∞2(s, A) = Zm∞1∞2(s, ̃A) + Zm∞1∞2(s, R−+ ̃A).

Thus, by Proposition 7.14,

Z ′
m∞2(0, A) = − log(U (1)
m (̃A)U (2)
m (̃A)
) − log(U (1)
m (R−+ ̃A)U (2)
m (R−+ ̃A))

= − log(U (1)
m (̃A)U (2)
m (̃A)U (1)
m (R−+ ̃A)U (2)
m (R−+ ̃A)) .

Therefore, it follows that Z ′
m∞2(0, A) = −2 log(U (1)
m (̃A)
).

We’ve now shown that Z ′
m∞2(0, A) = −t log(U (1)
m (̃A)) in all cases. It follows that U (1)
m (̃A)

depends only on Υm(A), and in particular, U (1)
m (A) := U (1)
m (̃A) is well-defined. □

7.3. Telescoping the product. We need the following identity for the double sine function.

Lemma 7.16. Sin2(ω1 + ω2 − z; ω1, ω2) = Sin2(z; ω1, ω2)
−1.

Proof. Follows directly from the definition of the double sine function, specifically (4.8). □

We also need the following identities for ϖr, whose proofs are straightforward.

Lemma 7.17. Let A ∈ SL2(R) and r = ( r1
r2 ) ∈ R2. Then,

ϖr(A · τ ) = ϖ ( [[A
−1r, τ ]]
j(A, τ ) , A · τ ) .

Proof. We use the identity [[r, A · τ ]] = [[A−1r,τ]]
j(A,τ ) . Specifically,

ϖr(A · τ ) = ϖ ([[r, A · τ ]] , A · τ ) = ϖ ( [[A
−1r, τ ]]
j(A, τ ) , A · τ ) .

This completes the proof. □

Lemma 7.18. Let b ∈ Z and r = ( r1
r2 ) ∈ R
2. If z = [[r, τ ]], then

ϖT bSr(T bS · τ )
ϖr(τ ) = e
( τ − 3 + τ −1

24 + (τ − z)(1 − z)
4τ
 ) (1 − e( z
τ
 )) Sin2(z, τ )−1.

72 GENE S. KOPP

Proof. We have T bS = ( b −1
1 0 ). Thus, by Lemma 7.17,

ϖT bSr(T bS · τ ) = ϖ
 ([[
(T bS)
−1T bSr, τ ]]

τ , − 1
τ + c
)
 = ϖ ( z
τ , − 1
τ
 ) ,

where in the last step, we simplified the elliptic term and used periodicity in the modular
coordinate. We also have ϖr(τ ) = ϖ(z, τ ). The claim now follows by Theorem 4.23. □

We actually need to transform the formula in Lemma 7.18 further. We will want to
translate z to some ̃z in the fundamental domain of the (pseudo)lattice τ Z + Z so that we
may compare the factors in Shintani’s formula. We also replace r by {r}.

Lemma 7.19. Let τ ∈ H, b ∈ Z, and r ∈ R
2. If ̃z = [[{r}, τ ]], then

ϖ{T bSr}(T bS · τ )
ϖ{r}(τ ) = e
( τ − 3 + τ −1

24 + (τ − ̃z)(1 − ̃z)
4τ
 ) Sin2(̃z, τ )
−1.

Proof. Write r = ( r1
r2 ). Note that {T bSr} = T bS̃r for some ̃r ≡ r (mod Z
2); it thus suffices
without loss of generality to prove the lemma under the assumption that {T bSr} = T bSr;
we make that assumption henceforth. Since T bSr = ( br1−r2
r1 ), it follows that 0 ≤ r1 < 1. Let
m = ⌊r2⌋; then, {r} = ( r1−1
r2−m )
.
As in Lemma 7.18, let z = [[r, τ ]]. Using the 1-quasiperiodicity of the double sine function
(from Proposition 4.25), we rewrite the formula in Lemma 7.18 as follows.

ϖT bSr(T bSτ )
ϖr(τ ) = e
( τ −3+τ −1
24 + (τ −z)(1−z)
4τ ) (
1 − e( z
τ )) Sin2(z, τ )
−1

= e
( τ −3+τ −1
24 + (τ −z)(1−z)
4τ ) (
1 − e( z
τ )) Sin2(z + 1, τ )
−1

2 sin ( πz
τ )

= e
( τ −3+τ −1
24 + (τ −z)(1−z)
4τ ) (
1 − e( z
τ )) Sin2(z + 1, τ )
−1

−i (
e( z
2τ ) − e(
− z
2τ ))

= e
( τ −3+τ −1
24 + (τ −z)(1−z)
4τ ) e
( z
2τ − 1
4) Sin2(z + 1, τ )
−1

= e
( τ −3+τ −1
24 + (τ −(z+1))(1−(z+1))
4τ ) Sin2(z + 1, τ )
−1.

Assume m ≥ 0. The case m < 0 may be handled similarly and is omitted. Note that
z + 1 = ̃z + mτ . By repeated use of the τ -quasiperiodicity property of the double sine
function (from Proposition 4.25), we have

ϖT bSr(T bSτ )
ϖr(τ ) = e
( τ −3+τ −1
24 + (τ −(z+1))(1−(z+1))
4τ ) (m−1∏

k=0 2 sin (π(̃z + kτ ))

)
 Sin2(̃z, τ )
−1. (7.10)

We also need to relate ϖr(τ ) to ϖ{r}(τ ), which we do using the q-product:

ϖ{r}(τ )
ϖr(τ ) =
 m−1∏

k=0 (1 − e(̃z + kτ ))

=
 m−1∏

k=0
 (
−ie( 1
2 (̃z + kτ )
)) e( 1
2(̃z + kτ )
) − e(
− 1
2(̃z + kτ ))

i

THE SHINTANI–FADDEEV MODULAR COCYCLE 73

=
 m−1∏

k=0 e( 2̃z−1
4 + kτ
2 ) (2 sin (π(̃z + kτ )))

= e
( m(2̃z−1)
4 + m(m−1)τ
4 ) m−1∏

k=0 2 sin (π(̃z + kτ )) . (7.11)

Dividing (7.10) by (7.11), and using the relation z + 1 = ̃z + mτ , we obtain (after some
algebra)
ϖr(T cSτ )
ϖ{rT cS}(τ ) = e
( τ −3+τ −1
24 + (τ −(z+1))(1−(z+1))
4τ − m(2̃z−1)
4 − m(m−1)τ
4 ) Sin(̃z; 1, τ )
−1

= e
( τ −3+τ −1
24 + (τ −̃z)(1−̃z)
4τ ) Sin(̃z; 1, τ )
−1.

We have now proved the lemma. □

We are now in a position to relate the Stark–Tangedal–Yamamoto invariant to an RM
value of the Shintani–Faddeev modular cocycle.

Proposition 7.20. Let O be an order in a real quadratic field F , and let m be an integral
ideal of O. Let A ∈ Clm
♭
m∞1∞2(O), and let (r, β) be a reduced representative of ̃Υm(A).
Associate to β and r the HJ cycle data k, ℓ ∈ Z, A ∈ Γr, and βi, wi ∈ F . Identify β with
ρ1(β). Then,
 U (1)
m (A)−1 = e
(− 1
24γ(A) − 1
4λr(A)) ש
r
A(β) ,

where
 γ(A) :=
 kℓ−1∑

n=0
 (
βn − 3 + β−1
n ) = k
 ℓ−1∑

n=0
 (
βn − 3 + β−1
n )

and
 λr(A) :=
 kℓ−1∑

n=0
 (βn − wn)(1 − wn)
βn .

Proof. By Definition 7.13,

U (1)
m (A) =
 kℓ−1∏

n=0 Sin2(wn, βn) =
 kℓ∏

n=1 Sin2(wn, βn).

We have βn = An,kℓ · β, T bn−1S · βn = βn−1, and T bn−1S · rn = rn−1. Thus, by Lemma 7.19,

Sin2(wn, βn)
−1 = e
(
−βn − 3 + β−1
n
24 − (βn − wn)(1 − wn)
4βn
 ) lim
τ →β ϖrn−1(An−1,kℓ · τ )
ϖrn(An,kℓ · τ ) ,

where the limit is taken over τ ∈ H. Taking the product from n = 1 to n = kℓ and using
the identities A0,kℓ = A and Akℓ,kℓ = I, we have

U (1)
m (A)
−1 = e
(
− 1
24γ(A) − 1
4λr(A)
) lim
τ →β
 kℓ∏

n=1
 ϖrn−1(An−1,kℓ · τ )
ϖrn(An,kℓ · τ )

= e
(
− 1
24γ(A) − 1
4λr(A)
) lim
τ →β ϖr(A · τ )
ϖr(τ )
= e
(
− 1
24γ(A) − 1
4λr(A)
) ש
r
A(β) ,

74 GENE S. KOPP

proving the proposition. □

To prove Theorem 1.1 from Proposition 7.20, we need to show that the root of unity
factors in front agree up to a plus or minus sign. This is done in Section 7.4 for the “global
phase factor” e(γ(A)) and in Section 7.5 for the “r-dependent phase factor” e(λr(A)).
We also need to show that the condition that 0 < β′ < 1 < β can be removed. This is
done as part of the final proof of Theorem 1.1 in Section 8.1.

7.4. The global phase factor. We relate the global phase factor to the eta-multiplier
character ψ.

Proposition 7.21. Let β be a real number purely periodic Hirzeburch–Jung continued frac-
tion expansion β = [b0, b1, . . . , bℓ−1],
and treat the indices as elements of Z/ℓZ, so bn+ℓ = bn. Let β0, β1, . . . , βℓ−1 be the real num-
bers with Hirzebruch–Jung continued fraction expansions given by the cyclic permutations of
the Hirzebruch–Jung continued fraction expansion of β = β0; that is,

βn = [bn, bn+1 . . . , bn+ℓ−1].

Let ℓ
′ be the length of the periodic part of the HJ continued fraction of the nontrivial Galois
conjugate β′ of β, and let P = T b0ST b1S · · · T bℓ−1S. We have the following identities:

ℓ−1∑

n=0
 (βn − 3 + β−1
n ) = −3ℓ +
 ℓ−1∑

n=0 bn = ℓ
′ − ℓ = Φ(P ) − 3 = Ψ(P, √
jP ).

Here Φ and Ψ are the integer-valued functions defined in Section 2.5 and appearing in the
transformation law of the logarithm of the Dedekind eta function.

Proof. First, note that the βn satisfy the recurrence βn = bn − β−1
n+1, that is, βn + β−1
n+1 = bn.
Thus, we may pair up the appropriate summands as follows.

ℓ−1∑

n=0
 (
βn − 3 + β−1
n ) = −3ℓ +
 ℓ−1∑

n=0 βn +
 ℓ−1∑

n=0 β−1
n

= −3ℓ +
 ℓ−1∑

n=0 βn +
 ℓ−1∑

n=0 β−1
n+1

= −3ℓ +
 ℓ−1∑

n=0 bn. (7.12)

This proves the first identity. To prove the second, consider the Hirzebruch–Jung continued
fraction expansion of the nontrivial Galois conjugate β′; let ℓ
′ be the length the periodic part
that expansion. By Lemma 7.8, each bn contributes bn − 2 entries to the periodic part of the
expansion of β′, so
 ℓ
′ =
 ℓ−1∑

n=0 bn − 2 = −2ℓ +
 ℓ−1∑

n=0 bn. (7.13)

By combining (7.12) and (7.13), we have

ℓ−1∑

n=0 βn − 3 + β−1
n = −3ℓ + (ℓ′ + 2ℓ) = ℓ
′ − ℓ,

THE SHINTANI–FADDEEV MODULAR COCYCLE 75

proving the second relation. For the relation to Φ and Ψ, we appeal to results of Meyer and
of Zagier. Writing P = ( a b
c d ) and combining formulas on [80, p. 155] and [80, p. 162], we
obtain the formula
 ℓ
′ − ℓ = a + d − 2(d, c)
c − 3,

where (d, c) := 6cs(d, c) and s(d, c) denotes the Dedekind sum in our notation from Sec-
tion 2.5. Zagier cites a proof by Meyer [51]. A straightforward induction on ℓ shows that
c > 0. Thus, by (2.5) and (2.6), we obtain the two relations involving Ψ and Φ. □

7.5. The r-dependent phase factor. We relate the r-dependent phase factor to the theta-
multiplier character χr.

Proposition 7.22. Let r and A be as in Proposition 7.20. Then,

λr(A) = λ−r(A).

Proof. If r = ( −1
0 ), the claim is trivial, so we assume r ̸= ( −1
0 ). Write

λr(A) =
 ℓ−1∑

n=0 an where an = (βn − wn)(1 − wn)
βn ,

and write
 λ−r(A) =
 ℓ−1∑

n=0 ̃an where ̃an = (βn − ̃wn)(1 − ̃wn)
βn ,

in a similar manner. We have wn = [[rn, βn]] with rn = {An,0r} and ̃wn = [[̃rn, βn]] with
̃rn = {−An,0r}. It follows from the assumption that r ̸= ( −1
0 ) that rn and ̃rn are also not
equal to ( −1
0 ). We’ll now compare the summands an and a′
n in three cases.
Case 1: If rn1 ̸= −1 and rn2 ̸= 0, then ̃wn = βn + 1 − wn, so

̃an = (βn − ̃wn)(1 − ̃wn)
βn = (−1 + wn)(−βn + wn)
βn = (βn − wn)(1 − wn)
βn = an. (7.14)

Case 2: If rn1 ̸= −1 and rn2 = 0, then ̃wn = 1 − wn, so

̃an = (βn − ̃wn)(1 − ̃wn)
βn = (βn − 1 + wn)wn
βn = wn(βn − 1 + wn)
βn .

A further algebraic calculation shows that

̃an − an = wn(βn − 1 + wn) − (βn − ̃wn)(1 − ̃wn)
βn = −βn + 2βnwn
βn = −1 + 2wn.

Moreover, since rn2 = 0, it follows that wn = rn2βn − rn1 = −rn1. Thus, ̃an = an − (1 + 2rn1).
Case 3: If rn1 = −1 and rn2 ̸= 0, then ̃wn = βn + 2 − wn, so

̃an = (βn − ̃wn)(1 − ̃wn)
βn = (−2 + wn)(−βn − 1 + wn)
βn = (2 − wn)(βn + 1 − wn)
βn .

A further algebraic calculation shows that

̃an − an = wn(βn − 1 + wn) − (βn − ̃wn)(1 − ̃wn)
βn = βn − 2 − 2wn
βn = 1 + 2(1 − wn)β−1
n .

Moreover, since rn1 = −1, it follows that wn = rn2βn−rn1 = rn2βn+1, so (1−wn)β−1
n = −rn2.
Thus, ̃an = an + (1 − 2rn2).

76 GENE S. KOPP

Since r(n+1)1 = rn2 − 1, the instances of Case 2 and Case 3 occur in pairs: rn2 = 0 ⇐⇒
r(n+1)1 = −1. When this happens, we have

̃an + ̃an+1 = (an + an+1) − 2(rn1 + r(n+1)2).

However, r(n+1)2 = {−rn1 + bnrn2} = {−rn1} = −rn1 (because rn1 ̸= 1). So, in fact,

̃an + ̃an+1 = an + an+1. (7.15)

Using (7.14) and (7.15), we see that

λ−r(A) =
 ℓ−1∑

n=0 ̃an =
 ℓ−1∑

n=0 an = λr(A),

as desired. □

Proposition 7.23. Let r and A be as in Proposition 7.20, and suppose r /∈ Z
2. Then,

e
( 1
2λr(A)
) = χr(A).

Proof. By Theorem 4.36, we have

ש
r
A(β) ש−r
A (β) = ψ2(A)χr(A). (7.16)

By Proposition 7.20 (and using Proposition 7.21 and Proposition 7.22), we also have

ש
r
A(β) ש
−r
A (β) = (e
( 1
24γ(A) + 1
4λr(A)
) U (1)
m (A)−1) (
e( 1
24γ(A) + 1
4λ−r(A)
) U (1)
m (RA)
−1)

= e
( 1
24γ(A)
)2 e( 1
4λr(A) + 1
4λ−r(A)
) (
U (1)
m (A)U (1)
m (RA))−1

= ψ2(A)e
( 1
4λr(A) + 1
4λ−r(A)) (
U (1)
m (A)U (1)
m (RA)
)−1 by Proposition 7.21

= ψ2(A)e
( 1
2λr(A)) (
U (1)
m (A)U (1)
m (RA)
)−1 by Proposition 7.22. (7.17)

The left-hand side of (7.17) is on the unit circle by (7.16), and U (1)
m (A) and U (1)
m (RA) are
positive real numbers, so U (1)
m (A)U (1)
m (RA) = 1. Equating (7.16) and (7.17), we have

ψ2(A)e
( 1
2λr(A)
) = ψ2(A)χr(A),

and thus e( 1
2λr(A)) = χr(A). □

8. Culmination of proofs of main theorems and concluding remarks

We now have everything we need to prove Theorem 1.1 and Theorem 1.3. We also simplify
the statement of Theorem 1.1 using the notation established throughout the paper. The
proofs consist mainly of piecing together our various results on modular cocycles and partial
zeta functions.

8.1. Completing the proof of Theorem 1.1. We will now bring together our calculations
on modular cocycles and zeta functions to prove Theorem 1.1. We restate the theorem in
terms of a modified version of (the square of) the shin cocycle that allows us to leave the
characters ψ and χr out of the statement.

Definition 8.1. Let r ∈ Q and A ∈ Γr. For τ ∈ ̃DA, define the samech modular cocycle

ס
r
A(τ ) = (ψ−2χ
−1
r )(A) ש
r
A(τ )
2 .

THE SHINTANI–FADDEEV MODULAR COCYCLE 77

Theorem 8.2 (Restatement of Theorem 1.1). Let O be an order in a real quadratic field
F ⊂ R, and let m be a nonzero O-ideal. Let A ∈ Clm
♭
m∞2(O) \ ZClm
♭
m∞2(O), and write

Υm(A) = GL2(Z) · (r, β)

in the notation of Theorem 3.14. Let n = 2
ϕ−1(A) , where ϕ : Clm
♭
m∞1∞2(O) → Clm
♭
m∞2(O) is
the natural quotient map. Then
 exp
(
nZ ′
m∞2(0, A)) = ס
r[β]. (8.1)

Proof. Theorem 4.37 implies the following relation for R ∈ GL2(Z):

ס
sR(β)Rr[R · β] =
 {
ס
r[β] if det(R) = 1,

סr[β] if det(R) = −1. (8.2)

If (8.1) holds for any pair (r, β) in a GL2(Z)-orbit, then it follows that both sides of (8.2)
must be real, so it will follow that
 ס
sR(β)Rr[R · β] = סr[β]. (8.3)

Since A /∈ ZClm
♭
m,Σ(O), we have r /∈ Z2; thus, ס
r[β] only depends on the class of r (mod Z
2)
by Proposition 4.35. Thus, it suffices to prove (8.1) for one pair (r, β) ∈ Z × Fquad in each
(Z
2 ⋊ GL2(Z))-orbit. Henceforth, we assume (r, β) is reduced in the sense of Definition 3.16.
By Theorem 7.15, we have

Zm∞2(0, A) = −t log(U (1)
m (A)
) = t log(
U (1)
m (A)
−1) ,

where U (1)
m (A) is the Stark–Tangedal–Yamamoto invariant, t = 1 if O has a unit u ≡
1 (mod m) with ρ1(u) > 0 and ρ2(u) < 0, and t = 2 otherwise. The former condition
(giving t = 1) is equivalent to O having a unit of negative norm (either u or −u) that is
congruent to 1 (mod m). Taking n = 2
t , we have

nZm∞2(0, A) = 2 log(
U (1)
m (A)
−1) = log(
U (1)
m (A)
−2) , (8.4)

where n = 2 if O has a unit of negative norm that is congruent to 1 (mod m), and n =
1 otherwise. Let A = A
+
β ∈ Γr be the canonical generator of the stabilizer of β. By
Proposition 7.20, we have

U (1)
m (A)−1 = e
(− 1
24γ(A) − 1
4λr(A)) ש
r
A(β) , (8.5)

where γ(A) and λr(A) are the rational invariants defined in that proposition. Moreover, these
invariants are related to metaplectic characters, as shown in Section 7.4 and Section 7.5.
Specifically, Proposition 7.21 says that γ(A) = Ψ(A, √
jA), and thus e
( 1
24γ(A)
)2 = ψ2(A);
Proposition 7.23 says that e( 1
2λr(A)) = χr(A). Squaring (8.5),
(U (1)
m (A)
)2 = e
( 1
24γ(A)
)−2 e( 1
2λr(A)
)−1 (ש
r
A(β))
2 = (ψ−2χ−1
r )(A) (ש
r
A(β))
2 = ס
r[β].

Finally, exponentiating (8.4), we have

exp(nZm∞2(0, A)) = (
U (1)
m (A))−2 = סr[β]. □

We now give a corollary stating the key functional equations and basic properties satisfied
by RM values the samech cocycle.

Corollary 8.3. Suppose that r ∈ Q
2 \ Z
2 and β ∈ Rquad. The following hold.

78 GENE S. KOPP

(1) ס
r[β]ס
−r[β] = 1.
(2) ס
r[β] = סr+n[β] for any n ∈ Z
2

(3) ס
sR(β)Rr[R · β] = סr[β] for any R ∈ GL2(Z).
(4) ס
r[β] is a positive real number.

Proof. Property (1) follows from Theorem 4.36. Property (2) follows from Proposition 4.35.
Property (3) follows from Theorem 8.2 via (8.3). Property (4) follows from Theorem 8.2
because (8.1) expresses ס
r[β] as the exponential of a real number. □

8.2. Stark units and conditional results. We now discuss the conditional implications of
our results under the assumption of Tate’s refinement of the Stark conjectures. In particular,
we will complete the proof of Theorem 1.3.

Proof of Theorem 1.3. For r ∈ Z
2 (and indeed r ∈ 1
2Z
2), the conclusion follows from Theo-
rem 4.38 (even without assuming Conjecture 6.9), so we may assume r /∈ Z
2 henceforth.
Let f be the conductor of β (that is, b2 − 4ac = f 2∆0 for a fundamental discriminant ∆0
and a positive integer f ). Set A = A+
β ∈ Γr. By Lemma 4.42, there is some B ∈ Gf and
some α of conductor 1 such that β = B · α. Choose n ∈ N so that

C := B−1AnB ∈ ⋂

s∈Q2/Z2

Bs−r∈Z2
 Γs.

Then, by Theorem 4.46, we have

ש
r[β]n = ש
r
An(β) = ש
r
BCB−1(B · α) = ∏

s∈Q2/Z2

Bs−r∈Z2
 ש
s
C(α) .

The values ש
s
C(α) are integral powers of ש
s[α], and α has conductor 1. Thus, (2) implies (1).
It suffices to prove (2) on the assumption of Conjecture 6.9. We henceforth assume f = 1.
Let w = [[r, β]] = r2β − r1. We have defined m to be the kernel of the map OF →
(wOF + c)/c given by 1 ↦→ w. In other words, m is the largest OF -ideal with the property
that (r, β) ∈ MOF ,m. Choose some A ∈ Clm∞2(OF ) such that Υ(A) = GL2(Z) · (r + Z
2, β).
By Theorem 8.2, for some n ∈ {1, 2} and A = A
+
β , we have

exp
(nZ ′
m∞2(0, A)
) = ס
r[β] = (ψ−2χ−1
r )(A)שr[β]2.

Let εA = exp
(
−Z ′
m∞2(0, A)
). By Proposition 6.11, it follows from Conjecture 6.9 that
εA ∈ O×
H, where H = Hm∞2, and ε1/2
A is a unit in an abelian extension of F . Thus, סr[β] =
εn
A ∈ O×
H, and ש
r[β] = ±
√(ψ2χr)(A) ε−n/2
A is a unit in an abelian extension of F . □

In Conjecture 1.4, we no longer define m to be the kernel of the map from O → (wOf +c)/c
sending 1 ↦→ w (taking here O = ord(c)). We avoid this because that kernel may not be an
O-invertible ideal, so that the associated MO,m would not appear in Theorem 3.14. We may
need to consider a noncanonical choice of a smaller O-invertible ideal m, as in Example 3.15.
(This is a conservative choice—we have not disproved the possibly-stronger conjecture that
m can be taken to be the kernel of the map from O → (wOf + c)/c sending 1 ↦→ w.)

THE SHINTANI–FADDEEV MODULAR COCYCLE 79

8.3. Example. For illustrative purposes, we give an example of a nontrivial RM value of
the Shintani–Faddeev modular cocycle. This example is related by a Galois automorphism
over Q(
√3) to the running example in [40, 42] and by Galois automorphisms over Q to the
SIC-POVM in dimension d = 5 [41].
Consider the order O = Z[
√3], which is the maximal order of Q(
√3) and has class
number 1. For the modulus 5∞2, the ray class group Cl5∞2(O) ∼= Z/8Z. Consider the ray
class A = [
√3O] ∈ Cl5∞2(O). Using PARI, we calculate to high precision the exponentiated
derivative partial zeta value

exp(Z ′
5∞2(0, A)) = exp(2ζ ′
5∞2(0, A)) ≈ 5.54060902431686855379 . . . (8.6)

by writing ζ ′
5∞2(0, A) as a linear combination of L-functions of finite-order Hecke characters.
Specifically, we take F = bnfinit(x^2-3) (a “Buchmann’s number field” object representing
the field F with certain auxiliary data) and C = bnrinit(F,[5,[1,0]],1) (a “Buchmann’s
number rays” object representing the ray class group Cl5∞2(O) with certain auxiliary data).
The command Lvals = bnrL1(C,0,6) produces a list containing the values of L′(0, χ
j) for
an order 8 Hecke character χ of modulus 5∞2 satisfying χ([
√
3O]) = e( 1
8)
. We may recover
ζ ′
5∞2(0, A) = 1
8 ∑7
j=0 e(
− j
8) L
′(0, χ
j).
In the notation of Theorem 1.1, we take m = 5O, A0 = [O], b = O, bm = α(βZ + Z)
with α = 5 and β = √
3, and r = ( 0
−1/5 ) ≡ ( 0
4/5 ) (mod Z
2). By Theorem 1.1 and a sign
computation, we obtain

ש( 0
4/5 )[√3
] = ש( 0
4/5 )
( 26 45
15 26 )
(√3
) = e−7πi/20√
exp(Z ′
5∞2(0, A)). (8.7)

Conditional on the Stark conjectures,

ש( 0
4/5 )[√
3
] ?
= e−7πi/20√ν (8.8)

where ν ≈ 5.54060902431686855379 . . . is a root of the polynomial

x8 − (8 + 5√3)x7 + (53 + 30
√3)x6 − (156 + 90√3)x5

+ (225 + 130√
3)x4 − (156 + 90√3)x3 + (53 + 30√
3)x2 − (8 + 5√3)x + 1.

We have done additional numerical checks of (8.7) and (8.8) by computing ש( 0
4/5 )
( 26 45
15 26 )(√
3
) in

Mathematica, both a limit of q-Pochhammer symbols and in terms of a product of double
sine values, applying numerical integration to Proposition 4.28 in the latter case.
For computational purposes, it is more efficient to compute RM values of שr via a product
of double sine values than as a limit of q-Pochhammer symbols; the comparison is comparable
to that described in [42, Sec. 3]. The comparative asymptotic efficiency of using double sine
to using the methods for L-functions (of finite-order Hecke characters) implemented in PARI
requires further investigation. More will be said about computational methods in [2].

8.4. Asymptotics of the q-Pochhammer symbol. We conclude with a few remarks
on the asymptotics of the q-Pochhammer symbol near the real line. Specifically, the ana-
lytic continuation properties of the ש-function explain the behavior of the function ϖr(τ ) =
(e2πi(r2τ −r1), e
2πiτ )∞ as τ → β ∈ Rquad along modular geodesics.
For β ∈ Q, the behavior of ϖr(τ ) as τ → β is intimately connected to the dilogarithm
function, as well as to the cyclic quantum dilogarithm, as discussed in Section 4.11. A much

80 GENE S. KOPP

more comprehensive study of the behavior of the q-Pochhammer symbol near roots of unity
may be found in the PhD thesis of Campbell Wheeler [76].
For real quadratic irrationals, the behavior of asympotic behavior as τ → β along the
modular geodesic between β′ and β is given by the following theorem.

Theorem 8.4. Let r ∈ Q
2 and β ∈ Rquad. Let νr,β = ש
r[β], which is related to a Stark class
invariant by Theorem 1.1. Let u be the smallest totally positive unit of the quadratic order
O = (βZ + Z : βZ + Z) such that u > 1 and (u − 1)(r2β − r1) ∈ βZ + Z. Then,

ϖr
( β + iβ′e
− log(u)t

1 + ie− log(u)t
 ) = νt
r,β(fr,β(t) + o(1)) as t → ∞. (8.9)

where fr,β is a smooth function satisfying fr,β(t + 1) = fr,β(t).

Proof. Let A = A
+
β . Diagonalize A = R ( u 0
0 u−1 ) R−1 (where u is the unit specified in the
statement), and define A
t = R ( ut 0
0 u−t ) R−1. If ω := β+iβ′

1+i , then for t ∈ R,

A
t · ω = β + iβ′e
−2 log(u)t

1 + ie−2 log(u)t

Thus, ϖr(A
t+1 · ω) = ש
r
A(A
t · ω) ϖr(A
t · ω), and limt→∞ ש
r
A(A
t · ω) = νr,β. Set gr,β(t) =
ν−t
r,βωr(A
t · ω). Then,

gr,β(t + 1) = ν−t−1
r,β שr
A(A
t · ω) ϖr(A
t · ω) = ν−1
r,βש
r
A(A
t · ω) gr,β(t).

Setting fr,β(t) = lim
n→∞
n∈Z gr,β(t + n), (8.9) follows. □

In fact, one may replace β′ by any x ∈ R in (8.9) (shifting fr,β by a constant depending on
x). Similarly, along the vertical geodesic between i∞ and β, we have the asymptotic formula

ϖr(β + ie− log(u)t) = νt
r,β( ̃fr,β(t) + o(1)) as t → ∞, (8.10)

where ̃fr,β = fr,β(t + c) for some c ∈ R. Equation (8.10) is illustrated in Figure 1 for the
example in Section 8.3. We omit a formal proof of these more general asymptotics. They hold
because modular geodesics approach β approximately vertically from above, and differences
between values of ϖr on nearby points on different geodesics may be bounded appropriately.
Further investigating the behavior of ϖr(τ ) near the real line could be interesting in
several ways. Analytically, such investigations might lead to improved asymptotic formulas,
or even exact formulas, for counting integer partitions into parts with congruence restrictions.
Algebraically, they could bring Stark units into the “quantum modular” universe, perhaps
connecting them to the many interesting objects already linked to quantum modular forms,
including as 3-manifolds and conformal field theories.

9. Typesetting note

The shin character ש and the samech character ס may used as \shin and \samech in
LATEX after adding the following lines to the preamble.
\DeclareFontFamily{U}{rcjhbltx}{}
\DeclareFontShape{U}{rcjhbltx}{m}{n}{<->rcjhbltx}{}
\DeclareSymbolFont{hebrewletters}{U}{rcjhbltx}{m}{n}
\DeclareMathSymbol{\shin}{\mathord}{hebrewletters}{152}
\DeclareMathSymbol{\samech}{\mathord}{hebrewletters}{115}

THE SHINTANI–FADDEEV MODULAR COCYCLE 81

1 2 3 4

5

10

15

20

25

30
 1 2 3 4

0.85

0.90

0.95

1.00
 1 2 3 4

-0.20

-0.15

-0.10

-0.05

0.05

0.10

0.15
 Figure 1. The top plot compares y = ∣
∣
∣
∣ϖ( 0
4/5
 )(√3 + ie−6 log(2+
√3)t)∣
∣
∣
∣

and y = µt for µ = e
− 7πi
20 √ν and ν as in (8.6). The middle and bot-

tom plots show graphs of y = ∣
∣
∣
∣µ−t ϖ( 0
4/5
 )(√3 + ie−6 log(2+
√3)t)∣
∣
∣
∣ and y =

arg(µ−t ϖ( 0
4/5
 )(√3 + ie−6 log(2+
√3)t)), respectively.

10. Acknowledgments

The author is supported by NSF DMS grant #2302514 and has been supported by the
Heilbronn Institute for Mathematical Research while conducting the research for this paper.
The author thanks Marcus Appleby, Kairi Black, Samit Dasgupta, Steven T. Flammia,
Edna Jones, Jeffrey C. Lagarias, Owen Patashnick, and David Solomon for helpful conversa-
tions. He also thanks Brett Tangedal for help checking the PARI computation in Section 8.3
and Eleanor McSpirit, Brett Tangedal, and Bora Yalkinoglu for pointing out several impor-
tant references.
The author is grateful to the developers of the computer algebra packages Mathematica
and PARI, which he has used to compute the example in Section 8.3.

82 GENE S. KOPP

References

[1] R. L. Adler and L. Flatto. The backward continued fraction map and geodesic flow. Ergodic Theory
Dynam. Systems, 4(4):487–492, 1984.
[2] M. Appleby, S. Flammia, and G. S. Kopp. A constructive approach to Zauner’s conjecture via the Stark
conjectures, 2025. Preprint arXiv:arXiv:2501.03970.
[3] T. Arakawa. Generalized eta-functions and certain ray class invariants of real quadratic fields. Math.
Ann., 260(4):475–494, 1982.
[4] M. Atiyah. The logarithm of the Dedekind η-function. Math. Ann., 278:335–380, 1987.
[5] M. Bal´azs and R. Bowen. Product blocking measures and a particle system proof of the Jacobi triple
product. Ann. Inst. Henri Poincar´e Probab. Stat., 54(1):514–528, 2018.
[6] M. Bal´azs, D. Fretwell, and J. Jay. Interacting particle systems and Jacobi style identities. Res. Math.
Sci., 9(3):Paper No. 48, 46, 2022.
[7] E. W. Barnes. The theory of the double gamma function. Philos. Trans. Roy. Soc. A, 196:265–387, 1901.
[8] V. V. Bazhanov and N. Y. Reshetikhin. Remarks on the quantum dilogarithm. J. Phys. A, 28(8):2217–
2226, 1995.
[9] O. Beckwith and G. S. Kopp. Gauss composition with level structure, 2025+. In preparation.
[10] H. Bekki. Shintani–Barnes cocycles and values of the zeta functions of algebraic number fields. Algebra
Number Theory, 17(6):1153–1208, 2023.
[11] N. Bergeron, P. Charollois, and L. E. Garcia. Elliptic units for complex cubic fields, 2023. Preprint
arXiv:2311.04110.
[12] C. Bjorklund and M. Litman. Error approximation for backwards and simple continued fractions. Res.
Number Theory, 10(1):Paper No. 2, 2024.
[13] K. Bringmann and A. Folsom. Quantum Jacobi forms and finite evaluations of unimodal rank generating
functions. Arch. Math. (Basel), 107(4):367–378, 2016.
[14] K. Bringmann, K. Ono, and I. Wagner. Eichler integrals of Eisenstein series as q-brackets of weighted
t-hook functions on partitions. Ramanujan J., 61(1):279–293, 2023.
[15] P. Charollois and S. Dasgupta. Integral Eisenstein cocycles on GLn, I: Sczech’s cocycle and p-adic
L-functions of totally real fields. Camb. J. Math., 2(1):49–90, 2014.
[16] P. Charollois, S. Dasgupta, and M. Greenberg. Integral Eisenstein cocycles on GLn, II: Shintani’s
method. Comment. Math. Helv., 90(2):435–477, 2015.
[17] Y. Choie and R. Kumar. Arithmetic properties of the Herglotz-Zagier-Novikov function. Adv. Math.,
433:Paper No. 109315, 36, 2023.
[18] E. C. Dade, O. Taussky, and H. Zassenhaus. On the theory of orders, in paricular on the semigroup of
ideal classes and genera of an order in an algebraic number field. Math. Ann., 148:31–64, 1962.
[19] H. Darmon, A. Pozzi, and J. Vonk. The values of the Dedekind–Rademacher cocycle at real multiplica-
tion points. J. Eur. Math. Soc. (JEMS), 26(10):3987–4032, 2024.
[20] H. Darmon and J. Vonk. Singular moduli for real quadratic fields: a rigid analytic approach. Duke
Math. J., 170(1):23–93, 2021.
[21] S. Dasgupta and M. Kakde. On the Brumer–Stark conjecture. Ann. of Math. (2), 197(1):289–388, 2023.
[22] S. Dasgupta and M. Kakde. Brumer–Stark units and explicit class field theory. Duke Math. J.,
173(8):1477–1555, 2024.
[23] S. Dasgupta, M. Kakde, and K. Ventullo. On the Gross–Stark conjecture. Ann. of Math. (2), 188(3):833–
870, 2018.
[24] T. Dimofte. Complex Chern–Simons theory at level k via the 3d-3d correspondence. Comm. Math.
Phys., 339(2):619–662, 2015.
[25] L. D. Faddeev. Discrete Heisenberg–Weyl group and modular group. Lett. Math. Phys., 34(3):249–254,
1995.
[26] G. Felder, A. Henriques, C. A. Rossi, and C. Zhu. A gerbe for the elliptic gamma function. Duke Math.
J., 141(1):1–74, 2008.
[27] G. Felder and A. Varchenko. The elliptic gamma function and SL(3, Z) ⋉ Z
3. Adv. Math., 156(1):44–76,
2000.
[28] Y. Y. Finkel’shtein. Klein polygons and reduced regular continued fractions. Russian Math. Surveys,
48(3):198, 1993.
 THE SHINTANI–FADDEEV MODULAR COCYCLE 83

[29] S. Garoufalidis and R. Kashaev. Resurgence of Faddeev’s quantum dilogarithm. In Topology and
Geometry—a Collection of Essays Dedicated to Vladimir G. Turaev, volume 33 of IRMA Lect. Math.
Theor. Phys., pages 257–271. Eur. Math. Soc., Z¨urich, 2021.
[30] S. Garoufalidis and C. Wheeler. Modular q-holonomic modules, 2022. Preprint arXiv:2203.17029.
[31] S. Garoufalidis and D. Zagier. Asymptotics of Nahm sums at roots of unity. Ramanujan J., 55(1):219–
238, 2021.
[32] D. R. Hayes. Brumer elements over a real quadratic base field. Exposition. Math., 8(2):137–184, 1990.
[33] R. Hill. Shintani cocycles on GLn. Bull. Lond. Math. Soc., 39(6):993–1004, 2007.
[34] F. E. P. Hirzebruch. Hilbert modular surfaces. Enseign. Math. (2), 19:183–281, 1973.
[35] H. Iwaniec. Topics in Classical Automorphic Forms, volume 17 of Graduate Studies in Mathematics.
American Mathematical Society, Providence, RI, 1997.
[36] C. U. Jensen and A. Thorup. Gorenstein orders. J. Pure Appl. Algebra, 219(3):551–562, 2015.
[37] H. W. E. Jung. Darstellung der Funktionen eines algebraischen K¨orpers zweier unabh¨angigen
Ver¨anderlichen x, y in der Umgebung einer Stelle x = a, y = b. J. Reine Angew. Math., 133:289–314,
1908.
[38] S. Katok. Coding of closed geodesics after Gauss and Morse. Geom. Dedicata, 63(2):123–145, 1996.
[39] S. Katok. Continued fractions, hyperbolic geometry and quadratic forms. In MASS Selecta: Teaching
and Learning Advanced Undergraduate Mathematics, pages 121–160. Amer. Math. Soc., Providence, RI,
2003.
[40] G. S. Kopp. Indefinite zeta functions. Res. Math. Sci., 8(1):Paper No. 17, 34, 2021.
[41] G. S. Kopp. SIC-POVMs and the Stark conjectures. Int. Math. Res. Not. IMRN, 2021(18):13812–13838,
2021.
[42] G. S. Kopp. A Kronecker limit formula for indefinite zeta functions. Res. Math. Sci., 10(2):Paper No.
24, 21, 2023.
[43] G. S. Kopp and J. C. Lagarias. Ray class monoids for orders of number fields, 2024. To replace Appendix
A of preprint arXiv:2212.09177v1.
[44] G. S. Kopp and J. C. Lagarias. Ray class groups and ray class fields for orders of number fields. Essent.
Number Theory, 4(1):1–65, 2025.
[45] S. Koyama and N. Kurokawa. Values of the double sine function. J. Number Theory, 123(1):204–223,
2007.
[46] N. Kurokawa. Multiple sine functions and Selberg zeta functions. Proc. Japan Acad. Ser. A Math. Sci.,
67(3):61–64, 1991.
[47] N. Kurokawa and S. Koyama. Multiple sine functions. Forum Math., 15(6):839–876, 2003.
[48] L. Luzzi and S. Marmi. On the entropy of Japanese continued fractions. Discrete Contin. Dyn. Syst.,
20(3):673–711, 2008.
[49] I. G. Macdonald. Affine root systems and Dedekind’s η-function. Invent. Math., 15:91–143, 1972.
[50] Y. I. Manin. Real multiplication and noncommutative geometry (ein Alterstraum). In The Legacy of
Niels Henrik Abel, pages 685–727. Springer, Berlin, 2004.
[51] C. Meyer. Die Berechnung der Klassenzahl Abelscher K¨orper ¨uber quadratischen Zahlk¨orpern. Akademie-
Verlag, Berlin, 1957.
[52] G. Myerson. On semi-regular finite continued fractions. Arch. Math. (Basel), 48(5):420–425, 1987.
[53] J. Neukirch. Algebraic Number Theory, volume 322 of Grundlehren der mathematischen Wissenschaften.
Springer-Verlag, Berlin, 1999. Translated from the German by N. Schappacher.
[54] K. Onodera. An analogue of the Dedekind–Rademacher sum and certain ray class invariants of real
quadratic fields. J. Number Theory, 133(6):1907–1931, 2013.
[55] A. V. Osipov and A. N. Norris. The Malyuzhinets theory for scattering from wedge boundaries: a
review. Wave Motion, 29(4):313–340, 1999.
[56] B. Ponsot. Recent progress in Liouville field theory. In Proceedings of 6th International Workshop on
Conformal Field Theory and Integrable Models, volume 19, pages 311–335, 2004.
[57] P. Popescu-Pampu. The geometry of continued fractions and the topology of surface singularities. In
Singularities in Geometry and Topology 2004, volume 46 of Adv. Stud. Pure Math., pages 119–195.
Math. Soc. Japan, Tokyo, 2007.
[58] D. Radchenko and D. Zagier. Arithmetic properties of the Herglotz function. J. Reine Angew. Math.,
797:229–253, 2023.

84 GENE S. KOPP

[59] H. Rademacher. Topics in Analytic Number Theory, volume 169 of Die Grundlehren der mathematischen
Wissenschaften. Springer-Verlag, New York–Heidelberg, 1973.
[60] G. A. Sarkissian and V. P. Spiridonov. General modular quantum dilogarithm and beta integrals. Proc.
Steklov Inst. Math., 309:251–270, 2020.
[61] R. Sczech. Eisenstein group cocycles for GLn and values of L-functions. Invent. Math., 113(3):581–616,
1993.
[62] R. Sczech. A new formula for calculating Stark units over real quadratic number fields.
Surikaisekikenkyusho Kokyuroku, 925:134–142, 1995.
[63] J.-P. Serre. Local Fields, volume 67 of Graduate Texts in Mathematics. Springer-Verlag, New York–
Berlin, 1979. Translated from the French by M. J. Greenberg.
[64] T. Shintani. On evaluation of zeta functions of totally real algebraic number fields at non-positive
integers. J. Fac. Sci. Univ. Tokyo Sect. IA Math., 23(2):393–417, 1976.
[65] T. Shintani. On a Kronecker limit formula for real quadratic fields. J. Fac. Sci. Univ. Tokyo Sect. IA
Math., 24(1):167–199, 1977.
[66] T. Shintani. On certain ray class invariants of real quadratic fields. J. Math. Soc. Japan, 30(1):139–167,
1978.
[67] D. Solomon. Algebraic properties of Shintani’s generating functions: Dedekind sums and cocycles on
PGL2(Q). Compositio Math., 112(3):333–362, 1998.
[68] D. Solomon. The Shintani cocycle. II. Partial ζ-functions, cohomologous cocycles and p-adic interpola-
tion. J. Number Theory, 75(1):53–108, 1999.
[69] H. M. Stark. Values of L-functions at s = 1. I. L-functions for quadratic forms. Adv. Math., 7:301–343,
1971.
[70] H. M. Stark. L-functions at s = 1. II. Artin L-functions with rational characters. Adv. Math., 17(1):60–
92, 1975.
[71] H. M. Stark. L-functions at s = 1. III. Totally real fields and Hilbert’s twelfth problem. Adv. Math.,
22(1):64–84, 1976.
[72] H. M. Stark. Class fields for real quadratic fields and L-series at 1. In Algebraic Number Fields: L-
functions and Galois properties (Proc. Sympos., Univ. Durham, Durham, 1975), pages 355–375. Aca-
demic Press, London–New York, 1977.
[73] H. M. Stark. L-functions at s = 1. IV. First derivatives at s = 0. Adv. Math., 35(3):197–235, 1980.
[74] B. A. Tangedal. Continued fractions, special values of the double sine function, and Stark units over
real quadratic fields. J. Number Theory, 124(2):291–313, 2007.
[75] J. Tate. On Stark’s conjectures on the behavior of L(s, χ) at s = 0. J. Fac. Sci. Univ. Tokyo Sect. IA
Math., 28(3):963–978, 1981.
[76] C. Wheeler. Modular q-difference equations and quantum invariants of hyperbolic three-manifolds. PhD
thesis, Rheinischen Friedrich-Wilhelms-Universit¨at Bonn, Bonn, Germany, 2023.
[77] S. L. Woronowicz. Quantum exponential function. Rev. Math. Phys., 12(6):873–920, 2000.
[78] S. Yamamoto. On Kronecker limit formulas for real quadratic fields. J. Number Theory, 128(2):426–450,
2008.
[79] S. Yamamoto. Factorization of Shintani’s ray class invariant for totally real fields. In Algebraic Number
Theory and Related Topics 2008, volume B19 of RIMS Kˆokyˆuroku Bessatsu, pages 249–254. Res. Inst.
Math. Sci. (RIMS), Kyoto, 2010.
[80] D. Zagier. A Kronecker limit formula for real quadratic fields. Math. Ann., 213:153–184, 1975.
[81] D. Zagier. Valeurs des fonctions zˆeta des corps quadratiques r´eels aux entiers n´egatifs. In Journ´ees
Arithm´etiques de Caen (Univ. Caen, Caen, 1976), volume 41–42 of Ast´erisque, pages 135–151. Soc.
Math. France, Paris, 1977.
[82] D. Zagier. Quantum modular forms. In Quanta of Maths, volume 11 of Clay Math. Proc., pages 659–675.
Amer. Math. Soc., Providence, RI, 2010.

Department of Mathematics, Louisiana State University, Baton Rouge, LA, USA
Email address: kopp@math.lsu.edu
