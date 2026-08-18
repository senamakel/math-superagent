<!-- source: https://arxiv.org/pdf/2407.13465 | converted from PDF -->

arXiv:2407.13465v2  [math.DS]  1 Oct 2024
A NOTE ON HILBERT 16TH PROBLEM

ARMENGOL GASULL1 AND PAULO SANTANA2

Abstract. Let H(n) be the maximum number of limit cycles that a planar
polynomial vector ﬁeld of degree n can have. In this paper we prove that H(n)
is realizable by structurally stable vector ﬁelds with only hyperbolic limit cycles
and that it is a strictly increasing function whenever it is ﬁnite.

1. Introduction and statement of the main results

Consider the planar polynomial system of diﬀerential equations X = (P, Q) given
by

(1) ˙x = P (x, y), ˙y = Q(x, y),

where the dot means the derivative in relation to the independent variable t and P ,
Q : R2 → R are polynomials. To system (1) corresponds a polynomial vector ﬁeld
X = P ∂
∂x + Q ∂
∂y in the phase plane of the variables x and y. In this paper we make
no distinction between system (1) and its respective vector ﬁeld. The degree of X
is the maximum of the degrees of P and Q. Given n ∈ N, let X n be the set of the
planar polynomial systems (1) of degree n, endowed with the coeﬃcients topology.
Given X ∈ X n, let π(X) ∈ Z⩾0 ∪ {∞} be its number of limit cycles (i.e. isolated
periodic orbits).
In his famous address to the International Congress of Mathematicians in Paris
1900, David Hilbert raised his famous list of problems for the 20th century [2],
with the second part of the 16th problem being about the limit cycles of planar
polynomial vector ﬁelds. Hilbert asks if there is a uniform upper bound for the
number of limit cycles of polynomial vector ﬁelds of degree n. More precisely, given
n ∈ N let H(n) ∈ Z⩾0 ∪ {∞} be given by,

H(n) = sup{π(X) : X ∈ X n}.

Under this notation the second part of Hilbert’s 16th problem consists in obtaining
an upper bound for H(n) and it is yet an open problem. Even for the quadratic
case, it is not known if H(2) < ∞. However, advances has been made and lower
bounds for H(n) have been found. For small values of n, the best lower bounds so
far are H(2) ⩾ 4 [3, 18], H(3) ⩾ 13 [10] and H(4) ⩾ 28 [15]. In general, it is known
that H(n) increases at least as fast as O(n2 ln n) [4, 8, 11]. However, although the
known lower bounds are given by strictly increasing functions, this does not imply
that H(n) itself is strictly increasing. In our ﬁrst main result we prove this fact.

Theorem 1. Given n ∈ N, it holds H(n + 1) ⩾ H(n) + 1.

2020 Mathematics Subject Classiﬁcation. Primary: 34C07.
Key words and phrases. Hilbert 16th problem; limit cycles; structurally stable vector ﬁelds.

1

2 ARMENGOL GASULL AND PAULO SANTANA

In particular, it follows from Theorem 1 that if H(n0) = ∞ for some n0 ∈ N,
then H(n) = ∞ for every n ⩾ n0.
The proof of Theorem 1 is essentially a consequence from the fact that given
X ∈ X n, we can embed X into X n+1 and bifurcate one more limit cycle, while
the others persist. This persistence follows from our second main result. To state
it properly we will remind the notion of structural stability and comment on its
particularities when it is restricted to the polynomial case.
Roughly speaking, a smooth vector ﬁeld is structurally stable if small perturba-
tions do not change the topological character of its orbits. The hallmark work on
this area is due to Peixoto [12] and his characterization theorem, which states that
a C1-vector ﬁeld on a closed (i.e. compact and without boundary) two dimensional
manifold is structurally stable if, and only if, the following statements hold.

(a) It has at most a ﬁnite number of singularities, all hyperbolic.
(b) It has at most a ﬁnite number of periodic orbits, all hyperbolic.
(c) It does not have saddle connections.

Moreover, the family of structurally stable vector ﬁelds is open and dense in the
set of all C1-vector ﬁelds. For the structural stability of polynomial vector ﬁelds
endowed with the coeﬃcients topology there are two main characterizations, given
by Sotomayor [19] and Shafer [16]. The former deﬁnes structural stability of X ∈
X n as the structural stability of its Poincar´e compactiﬁcation. The latter does not
make use of this embedding and thus deals with new objects, such as saddles at
inﬁnity. Hence, they obtained diﬀerent sets of necessary and suﬃcient conditions
for structural stability. Yet, there are many similarities. Let X ∈ X n. In both
cases for X to be structurally stable, statements (a) and (c) above are necessary
and also the following weak version of statement (b).

(b′) It has at most a ﬁnite number of periodic orbits, none of even multiplicity.

So far it is not known if non-hyperbolic limit cycles of odd multiplicity are possible
for a structurally stable vector ﬁeld in the polynomial world. More precisely, there
is the following open question.

Question 1 ([16, 19]). If X ∈ X n has a non-hyperbolic limit cycle of odd multi-
plicity, then is X structurally unstable in X n?

Question 1 was explicitly raised by Sotomayor [19, Problem 1.1] and Shafer
[16, Question 3.4] and kept both of them from obtaining necessary and suﬃcient
conditions for structural stability in X n. For more details, we refer to [17]. Another
important similarity between both works is the fact that structural stability is a
generic property. That is, if we let Σn ⊂ X n be the family of the structurally
stable elements, then Σn is open and dense, independently of the two approaches.
Therefore, from now on we denote by Σn the set of structurally stable vector ﬁelds
of degree n under either one of these two deﬁnitions.
Let Σn
h ⊂ Σn be the family of structurally stable vector ﬁelds such that all
their limit cycles are hyperbolic. In our second main result we prove that H(n) is
realizable by the elements of this family.

Theorem 2. For n ∈ N, the following statements hold.

(a) If H(n) < ∞, then there is X ∈ Σn
h such that π(X) = H(n).
(b) If H(n) = ∞, then for each k ∈ N there is Xk ∈ Σn
h such that π(Xk) ⩾ k.

A NOTE ON HILBERT 16TH PROBLEM 3

Finally, due to its relation with the possible case of H(n) = ∞, we also include
at the end of this note a proof for the following folklore result: a planar analytic
vector ﬁeld has an enumerable number of limit cycles.
The paper is organized as follows. In Section 2 we recall some properties of
rotated vector ﬁelds and prove how they can be used to transform non-hyperbolic
limit cycles in hyperbolic ones. The main theorems are proved in Section 3. In
Section 4 we prove the folklore result and provide some further remarks.

2. Rotated vector fields

Given a planar polynomial vector ﬁeld X = (P, Q), let Xα = (Pα, Qα) be the
one-parameter family given by

(2) Pα = P cos α − Q sin α, Qα = Q cos α + P sin α,

with α ∈ R. Observe that X0 = X and that Xα deﬁnes a completed family of rotated
vector ﬁelds, see Duﬀ [5]. Throughout out this paper, Xα will always denote the
family given by (2).
In his seminal work Duﬀ [5] studied the properties of Xα. In particular, he proved
the following result that we simply state for family (2), but that holds for more
general 1-parametric families of C1 vector ﬁelds.

Theorem 3 ([5]). Let Xα be the family of rotated vector ﬁelds (2) and suppose
that Xα0 has a limit cycle γα0 . Then:

(a) If γα0 has odd multiplicity, then it is persistent for |α − α0| small and it
either contracts or expands monotonically as α varies in a certain sense.
(b) If γα0 has even multiplicity, then for |α − α0| small it splits in two limit
cycles, one stable and the other unstable, as α varies in a certain sense.
If α varies in the opposite sense, then γα0 disappears and no other limit
cycles appear in its neighborhood.

We observe that Theorem 3 does not provide information about the hyperbolic-
ity of the limit cycles involved. However, it follows from Andronov et al [1, The-
orems 71&72] that this information can be given in the analytic case. For sake of
simplicity and for the paper to be self-contained, we provide a proof of a simple
version of such theorems, suﬃcient for our goals.

Proposition 1. Let Xα be the family of rotated vector ﬁelds (2) and suppose that
Xα0 has a limit cycle γα0 . Then, for |α − α0| > 0 small enough, all the limit cycles
detailed in Theorem 3 that bifurcate from γα0 are hyperbolic.

Proof. For simplicity, let us assume α0 = 0. If γ0 is hyperbolic, then there is
nothing to prove. Hence, suppose that γ0 is not hyperbolic. Let I ⊂ R be a
small neighborhood of α0 = 0 and Σ be a small normal section of γ0, endowed
with a coordinate system s ∈ R such that s = 0 at p, where {p} = γ0 ∩ Σ. Let
D : I × Σ → R be its associated displacement map. Since Xα is analytic in (x, y; α),
it follows that D is well deﬁned and analytic. Let T > 0 be the period of γ0 and let
γ0(t) be the parametrization of γ0 given by the ﬂow of X0 and such that γ0(0) = p.

4 ARMENGOL GASULL AND PAULO SANTANA

It follows from Perko [13, Lemma 2] that, for some C ∈ R\{0},

∂D
∂α (0, 0) = C ∫ T

0
 (e− ∫ t
0 div(γ0(τ )) dτ ) Xα ∧ ∂Xα
∂α (γ0(t); 0) dt(3)
 = C ∫ T

0
 (e− ∫ t
0 div(γ0(τ )) dτ ) (
P 2 + Q2)(γ0(t); 0) dt ̸= 0.

Therefore, from the Implicit Function Theorem we have that there is a unique
function α = α(s), with α(0) = 0, such that

(4) D(α(s), s) = 0.

Moreover, since D is analytic, it follows that α(s) is also analytic. Diﬀerentiating (4)
in relation to s we obtain,

(5) ∂D
∂α (α(s), s)α
′(s) + ∂D
∂s (α(s), s) = 0.

From (3) we have that ∂D
∂α (α(s), s) ̸= 0 for |s| small. Hence, it follows from (5)
that,

(6) α
′(s) = − ∂D/∂s
∂D/∂α (α(s), s).

Since γ0 is not hyperbolic, it follows that ∂D
∂s (0, 0) = 0 and thus from (6) we have
α
′(0) = 0. Since α
′ is an analytic function, either 0 is an isolated zero of α
′ or
α
′(s) ≡ 0 (and in particular α(s) ≡ 0) in a neighborhood of s = 0. Let us discard
this second possibility. In this case, from (4), D(0, s) ≡ 0 for |s| small and thus
γ0 belongs to a continuous band of periodic orbits, contradicting the deﬁnition of
limit cycle. Therefore, it follows from (5) that

∂D
∂s (α(s), s) = − ∂D
∂α (α(s), s)α
′(s) ̸= 0,

for |s| > 0 small. Hence, any limit cycle of Xα near γ0 is hyperbolic, for |α| > 0
small, as we wanted to prove. □

We observe that Perko [13, Theorem 3] also provided a similar result about the
hyperbolicity of the limit cycles considered at Theorem 3(b). For more details about
the theory of rotated vector ﬁelds and its generalizations, we refer to Han [7], Perko
[14, Section 4.6] and the references therein.

3. Proof of the main theorems

Given X = (P, Q) ∈ X n, let πh(X) be its number of hyperbolic limit cycles.
Observe that in general we have πh(X) ⩽ π(X).
In this paper we also work with the possibility of π(X) = ∞ for some X ∈ X n.
We choose to do this because although Il’yashenko [9] and ´Ecalle [6] independently
claimed to have proved that this is impossible, it seems that some of their results
start to be under discussion. For instance, in the recent work [20] a possible gap was
found in Il’yashenko’s proof. Our results are not based on these ﬁniteness results.

Proposition 2. Let X ∈ X n. Then the following statements hold.
(a) If π(X) < ∞, then there is Y ∈ X n such that πh(Y ) ⩾ π(X).
(b) If π(X) = ∞, then for each k ∈ N there is Yk ∈ X n such that πh(Yk) ⩾ k.

A NOTE ON HILBERT 16TH PROBLEM 5

Proof. Let X ∈ X n and Xα be its respective family of rotated vector ﬁelds, given
by (2). Let also:
(i) h ∈ Z⩾0 ∪ ∞ be the number of hyperbolic limit cycles of X;
(ii) m ∈ Z⩾0 ∪ ∞ be the number of non-hyperbolic limit cycles X of odd
multiplicity;
(iii) m± ∈ Z⩾0 ∪ ∞ be the number of non-hyperbolic limit cycles γ of X of even
multiplicity and such that γ bifurcates in two hyperbolic limit cycles for
±α > 0 small.
Observe that π(X) = h + m + m+ + m−. Suppose ﬁrst π(X) < ∞. Without loss of
generality, suppose m+ ⩾ m−. It follows from Proposition 1 that Xα has at least
h + m + 2m+ hyperbolic limit cycles for α > 0 small enough. Hence, if we take
Y = Xα, then Y ∈ X n and

πh(Y ) ⩾ h + n + 2m+ ⩾ h + n + m+ + m− = π(X).

If π(X) = ∞, then h, m, m+ or m− are equal to inﬁnity. In any case we apply
the same reasoning on an sequence of vector ﬁelds having an increasing number of
limit cycles, obtaining the ﬁnal desired sequence of vector ﬁelds. □

Proof of Theorem 2. Suppose ﬁrst H(n) < ∞ and let Z ∈ X n be such that π(Z) =
H(n). It follows from Proposition 2 that there is Y ∈ X n such that πh(Y ) ⩾ π(Z).
Hence, it follows from the deﬁnition of H(n) that,

π(Y ) = πh(Y ) = π(Z) = H(n).

Hence, every limit cycle of Y is hyperbolic and any vector ﬁeld in X n, close enough
to Y, has also exactly H(n) limit cycles, all of them hyperbolic. In particular, there
is an arbitrarily small perturbation X ∈ Σn
h of Y such that π(X) = H(n).
Suppose now H(n) = ∞. Observe that there is a sequence (Zj), with Zj ∈ X n,
such that π(Zj ) → ∞ and π(Zj) < ∞ for every j ∈ N, or there is Z ∈ X n such
that π(Z) = ∞. In either case it follows from statement (a) or (b) of Proposition 2,
respectively, that for each k ∈ N there is Yk ∈ X n such that πh(Yk) ⩾ k. Therefore,
for each k ∈ N we can take a small enough perturbation Wk ∈ Σn of Yk such that
πh(Wk) ⩾ k. It follows from the deﬁnition of Σn that π(Wk) < ∞. Moreover,
some of these limit cycles may be non-hyperbolic and with odd multiplicity. Thus,
it follows similarly to the proof of Proposition 2, from the structural stability of
Wk and from the fact that Σn is open and dense in X n, that we can take a small
enough rotation Xk ∈ Σn of Wk such that the following statements hold.
(i) The hyperbolic limit cycles persist.
(ii) The non-hyperbolic limit cycles become hyperbolic.
(iii) Xk and Wk are topologically equivalent.
In particular, it follows from (iii) that we do not have the bifurcation of new limit
cycles and thus we conclude that Xk ∈ Σn
h and π(Xk) ⩾ k. □

We now prove a technical lemma that we will need to proof Theorem 1.

Lemma 1. Let X ∈ X n and B ⊂ R2 a closed ball centered at the origin. Then
there is an arbitrarily small perturbation Y of X having a regular point p ∈ R2\B
such that ℓ ∩ B = ∅, where ℓ is the straight line p + sY (p), s ∈ R.

Proof. It follows from Shafer [16, Theorem 3.2] that we can take an arbitrarily
small perturbation Y ∈ X n of X such that Y has at most a ﬁnite number of

6 ARMENGOL GASULL AND PAULO SANTANA
 x

y

B
 ℓ+

ℓ− p

Y (p)

θ ϕ

ℓ

Figure 1. Illustration of ℓ± and ℓ.

singularities. Let Y = (P, Q) and let Pi and Qi, i ∈ {0, . . . , n}, be homogeneous
polynomials of degree i such that P = P0 + · · · + Pn and Q = Q0 + · · · + Qn.
Replacing Y by an arbitrarily small perturbation if necessary, we can also suppose
Pn(1, 0)Qn(1, 0) ̸= 0. Let p = (x, 0), x > 0. Since Y has at most a ﬁnite number
of singularities, there is x0 > 0 such that if x > x0, then p is a regular point of Y .
Let ℓ+ and ℓ− be the two straight lines tangents to B and passing through p. Let
θ = θ(x) be the angle between ℓ± and the x-axis and observe that,

lim
x→∞ θ(x) = 0.

Let also ϕ = ϕ(x) be the angle between ℓ and the x-axis, which is given by

ϕ(x) = arctan Q(x, 0)
P (x, 0) ,

see Figure 1. Since Pn(1, 0)Qn(1, 0) ̸= 0 it follows that,

lim
x→∞ ϕ(x) = arctan Qn(1, 0)
Pn(1, 0) ̸= 0.

As a consequence, |ϕ(x)| > |θ(x)| for x > 0 big enough and thus ℓ ∩ B = ∅. □

Proof of Theorem 1. Suppose ﬁrst H(n) < ∞. It follows from Theorem 2(a) that
there is Z ∈ Σn
h such that π(Z) = H(n). Let B ⊂ R2 be a closed ball centered at
the origin and such that all the limit cycles of Z are in the interior of B. From
Lemma 1 and the structural stability of Z, we can suppose that Z has a regular point
p ∈ R2\B such that p + sZ(p) ̸∈ B for every s ∈ R. Let Y = (P, Q) ∈ Σn
h be the
vector ﬁeld obtained from Z by translating p to the origin. Let X = (R, S) ∈ X n+1

be given by
 R(x, y) = (ax + by)P (x, y), S(x, y) = (ax + by)Q(x, y),

with a = −Q(0, 0) and b = P (0, 0). Let ℓ ⊂ R2 be the line given by ax + by = 0
and observe that X and Y are equal on each connected component of R2\ℓ, except
by the rescaling of time characterized by dt/dτ = ax + by. It follows from Lemma 1
that B ∩ ℓ = ∅ and thus πh(X) = π(X) = π(Y ). Observe that ℓ is a line of

A NOTE ON HILBERT 16TH PROBLEM 7

singularities of X. In particular, the origin is a singularity of X and its Jacobian
matrix is given by,

DX(0, 0) =
 ( aP (0, 0) bP (0, 0)

aQ(0, 0) bQ(0, 0)
 )
 =
 ( ab b2

−a2 −ab
 )
 .

Hence, det DX(0, 0) = 0 and Tr DX(0, 0) = 0. Let Xε,δ = (Rε, Sδ) be given by

Rε(x, y) = (ax + (b + ε)y)P (x, y), Sδ(x, y) = ((a + δ)x + by)Q(x, y),

and observe that we can take |ε| > 0 and |δ| > 0 small enough such that the
following statements hold.
(i) All the hyperbolic limit cycles inside B persist.
(ii) The origin is an isolated singularity.
(iii) det DXε,δ(0, 0) > 0 and Tr DXε,δ(0, 0) = 0.
Hence, the origin is a monodromic singularity of Xε,δ. Let L1 be its ﬁrst Lyapunov
constant (see Adronov et al. [1, p. 254]). Except perhaps by an arbitrarily small
perturbation on the nonlinear terms of Xε,δ, we can suppose L1 ̸= 0. Therefore, we
can take another small enough perturbation W ∈ X n+1 of Xε,δ such that a limit
cycle bifurcates from the origin, while the others persist. Hence we obtain

π(W ) ⩾ π(Y ) + 1 = H(n) + 1,

and thus H(n + 1) ⩾ H(n) + 1.
Suppose now H(n) = ∞. It follows Theorem 2(b) that there is a sequence (Zk),
with Zk ∈ Σn
h, such that π(Zk) → ∞. Since π(Zk) < ∞, we can apply the above
reasoning on each Zk obtaining a sequence (Wk), with Wk ∈ X n+1, such that
π(Wk) → ∞ and thus proving that H(n + 1) = ∞. □

4. Final remarks and a folklore result

Theorem 1 is not the ﬁrst known result about recurrence properties of H(n).
It follows from the proof of Christopher and Lloyd [4] that H(2n + 1) ⩾ 4H(n).
Roughly speaking, given X ∈ X n, the authors translate all the limit cycles of
X to the ﬁrst quadrant and thus apply the non-invertible transformation (x, y) ↦→
(u2, v2), followed by the rescaling of time dt/dτ = 2uv. Hence, obtaining Y ∈ X 2n+1

with a diﬀeomorphic copy of X in each open quadrant.
The challenge of Theorem 1 has been to relate H(n + 1) with H(n). It is much
more easy for example to prove that H(n + 2) ⩾ H(n) + 1. Indeed, given X ∈ X n

let Y = (x
2 + y2)X ∈ X n+2 and observe that Y is equivalent to X except at the
origin, where it has an extra degenerate singularity. Hence, similarly to the end of
the proof of Theorem 1, we can take a small perturbation of Y creating an extra
limit cycle.
We end this note with the following folklore result.

Proposition 3. Let X be a planar analytic vector ﬁeld. Then X has an enumerable
number of limit cycles. In particular, H(n) ⩽ ℵ0 for every n ∈ N.

Proof. If X has no limit cycles, then there is nothing to prove. Suppose therefore
that X has at least one limit cycle and let Γ = {γa}a∈A be an indexation of all its
limit cycles, A ̸= ∅. For each a ∈ A, set

δa = inf{d(γa, γb) : b ∈ A, b ̸= a},

8 ARMENGOL GASULL AND PAULO SANTANA

where d(γa, γb) is the usual distance between the compact sets γa and γb,

d(γa, γb) = min{||qa − qb|| : qa ∈ γa, qb ∈ γb}.

Since X is analytic, it follows that γa must be isolated (see [14, p. 217]) and thus
δa > 0 for every a ∈ A. Let Na ⊂ R2 be the open δa/2-neighborhood of γa, a ∈ A.
Observe that if a ̸= b, then Na ∩ Nb = ∅ (for otherwise d(γa, γb) < max{δa, δb}).
For each a ∈ A, choose ra ∈ Na ∩ Q2 and deﬁne i(a) = ra. Observe that ra ̸= rb if
a ̸= b. Hence, we have an injective map i : A → Q2 and thus A is enumerable. □

Notice that Proposition 3 is optimal for the analytic case. For instance, the
planar analytic vector ﬁeld

˙x = −y + x sin(x
2 + y2), ˙y = x + y sin(x
2 + y2),

has inﬁnitely many limit cycles, given by x
2 + y2 = kπ, with k ∈ Z>0.

Acknowledgments

This work is supported by the Spanish State Research Agency, through the
projects PID2022-136613NB-I00 grant and the Severo Ochoa and Mar´ıa de Maeztu
Program for Centers and Units of Excellence in R&D (CEX2020-001084-M), grant
2021-SGR-00113 from AGAUR, Generalitat de Catalunya, and by S˜ao Paulo Re-
search Foundation (FAPESP), grants 2019/10269-3, 2021/01799-9 and 2022/14353-
1.
 References

[1] A. A. Andronov et al Theory of Bifurcations of Dynamic Systems on a Plane, Wiley, New
York & Toronto (1973).
[2] F. E. Browder, Mathematical Developments Arising from Hilbert Problems, Proc. Sympos.
Pure Math., volume XXVIII, part I (1976).
[3] L. Chen and M. Wang, The relative position, and the number, of limit cycles of a quadratic
diﬀerential system, Acta Math. Sinica (Chin. Ser.) 22, 751–758 (1979).
[4] C. Christopher and N. G. Lloyd, Polynomial Systems: A Lower Bound for the Hilbert
Numbers, Proc. R. Soc. Lond., Ser. A 450, No. 1938, 219–224 (1995).
[5] G. F. D. Duff, Limit-cycles and rotated vector ﬁelds, Ann. Math. (2) 57, 15–31 (1953).
[6] J. ´Ecalle, Introduction aux fonctions analysables et preuve constructive de la conjecture de
Dulac, Actualit´es Math´ematiques. Paris: Hermann, ´Editeurs des Sciences et des Arts.
[7] M. Han, Global behavior of limit cycles in rotated vector ﬁelds, J. Diﬀer. Equations 151, No.
1, 20–35 (1999).
[8] M. Han and J. Li, Lower bounds for the Hilbert number of polynomial systems, J. Diﬀer.
Equations 252, No. 4, 3278–3304 (2012).
[9] Y. S. Il’yashenko, Finiteness theorems for limit cycles, Translations of Mathematical Mono-
graphs, American Mathematical Society (1991).
[10] C. Li, C. Liu and J. Yang, A cubic system with thirteen limit cycles, J. Diﬀer. Equations
246, No. 9, 3609–3619 (2009).
[11] J. Li, Hilbert’s 16th Problem and bifurcations of Planar Polynomial Vector Fields, Int. J.
Bifurc. Chaos 13, 47–106 (2003).
[12] M. M. Peixoto, Structural stability on two-dimensional manifolds, Topology 1, 101–120
(1962).
[13] L. M. Perko, Bifurcation of limit cycles: Geometric theory, Proc. Am. Math. Soc. 114, No.
1, 225–236 (1992).
[14] L. M. Perko, Diﬀerential equations and dynamical systems, vol. 7 of Texts in Applied Math-
ematics, Springer-Verlag, New York, third ed, 2001.
[15] R. Prohens and J. Torregrosa, New lower bounds for the Hilbert numbers using reversible
centers, Nonlinearity 32, No. 1, 331–355 (2019).

A NOTE ON HILBERT 16TH PROBLEM 9

[16] D. Shafer, Structural stability and generic properties of planar polynomial vector ﬁelds, Rev.
Mat. Iberoam. 3, No. 3-4, 337–355 (1987).
[17] P. Santana, On the structural instability of non-hyperbolic limit cycles on planar polynomial
vector ﬁelds, to appear in S˜ao Paulo J. Math. Sci. (2024).
[18] S. Songling, A concrete example of the existence of four limit cycles for plane quadratic
systems, Sci. Sin. 23, 153–158 (1980).
[19] J. Sotomayor, Stable planar polynomial vector ﬁelds, Rev. Mat. Iberoam. 1, No. 2, 15–23
(1985).
[20] M. Yeung, On the monograph “Finiteness Theorems for limit cycles” and a special case of
alternant cycles, Preprint, arXiv:2402.12506 (2024).

1 Departament de Matem`atiques, Facultat de Ci`encies, Universitat Aut`onoma de
Barcelona, 08193 Bellaterra, Barcelona, Spain ; and Centre de Recerca Matem`atica,
Edifici Cc, Campus de Bellaterra, 08193 Cerdanyola del Vall`es (Barcelona), Spain
Email address: armengol.gasull@uab.cat

2 IBILCE–UNESP, CEP 15054–000, S. J. Rio Preto, S˜ao Paulo, Brazil
Email address: paulo.santana@unesp.br
