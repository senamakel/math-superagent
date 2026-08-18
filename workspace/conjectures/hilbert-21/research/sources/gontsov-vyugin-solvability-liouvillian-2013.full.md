<!-- source: https://arxiv.org/pdf/1312.2518 | converted from PDF -->

arXiv:1312.2518v1  [math.CA]  9 Dec 2013
Solvability of linear diﬀerential systems in the Liouvillian sense

R. R. Gontsov, I. V. Vyugin
∗

Abstract

The paper concerns the solvability by quadratures of linear diﬀerential systems, which is
one of the questions of diﬀerential Galois theory. We consider systems with regular singu-
lar points as well as those with (non-resonant) irregular ones and propose some criteria of
solvability for systems whose (formal) exponents are suﬃciently small.

1 Introduction

Consider on the Riemann sphere C a linear diﬀerential system

dy
dz = B(z) y, y(z) ∈ Cp, (1)

of p equations with a meromorphic coeﬃcient matrix B(z) having singularities at points a1, . . . , an.
A singular point z = ai is said to be regular, if any solution of the system has at most polyno-
mial growth in any sector of small radius with vertex at this point and an opening less than 2π.
Otherwise the point z = ai is said to be irregular.
The Picard–Vessiot extension of the ﬁeld C(z) of rational functions corresponding to the
system (1) is a diﬀerential ﬁeld F obtained by adjoining to C(z) all entries of a fundamental
matrix Y (z) of the system (1). One says that the system (1) is solvable by quadratures, if the
entries of the matrix Y (z) are expressed in elementary or algebraic functions and their integrals
or, more formally, if the ﬁeld F is contained in some extension of C(z) obtained by adjoining
algebraic functions, exponentials or integrals:

C(z) = F1 ⊆ . . . ⊆ Fm, F ⊆ Fm,

where Fi+1 = Fi⟨xi⟩ (i = 1, . . . , m − 1), and either xi is algebraic over Fi, or xi is an exponential
of an element in Fi, or xi is an integral of an element in Fi. Such an extension C(z) ⊆ Fm is
called Liouvillian, thus solvability by quadratures means that the Picard–Vessiot extension F is
contained in some Liouvillian extension of the ﬁeld of rational functions.
Solvability or non-solvability of a linear diﬀerential system by quadratures is related to
properties of its Galois group. The diﬀerential Galois group G = Gal (F/C(z)) of the system
(1) (of the Picard–Vessiot extension C(z) ⊆ F ) is the group of diﬀerential automorphisms of the
ﬁeld F (i. e., automorphisms commuting with diﬀerentiation) that preserve elements of the ﬁeld
C(z):
 G = {σ : F → F ∣
∣
∣ σ ◦ d
dz = d
dz ◦ σ, σ(f ) = f ∀f ∈ C(z)
}.

∗The author is partially supported by Dynasty Foundation, Simons-IUM fellowship and grant RFBR 12-01-
33058.
 1

As follows from the deﬁnition, the image σ(Y ) of the fundamental matrix Y (z) of the system
(1) under any element σ of the Galois group is a fundamental matrix of this system again, that
is, σ(Y ) = Y (z)C, C ∈ GL(p, C). As every element of the Galois group is determined uniquely
by its action on a fundamental matrix of the system, the Galois group G can be regarded as
a subgroup of the matrix group GL(p, C). Moreover this subgroup G ⊂ GL(p, C) is algebraic,
i. e., closed in the Zariski topology of the space GL(p, C) (the topology whose closed sets are
those determined by systems of polynomial equations), see [12, Th. 5.5].
The Galois group G can be represented as a union of ﬁnite number of disjoint connected sets
that are open and closed simultaneously (in the Zariski topology), and the set containing the
identity matrix is called the identity component. The identity component G0 ⊂ G is a normal
subgroup of ﬁnite index [12, Lemma 4.5]. Due to the Picard–Vessiot theorem, solvability of the
system (1) by quadratures is equivalent to solvability of the subgroup G0 [12, Th. 5.12], [13,
Ch. 3, Th. 5.1]. (Recall that a group H is said to be solvable, if there exist intermediate normal
subgroups {e} = H0 ⊂ H1 ⊂ . . . ⊂ Hm = H such that each factor group Hi/Hi−1 is Abelian,
i = 1, . . . , m.)
Alongside the Galois group one considers the monodromy group M of the system (1) gen-
erated by the monodromy matrices M1, . . . , Mn corresponding to analytic continuation of a
fundamental matrix Y (z) around the singular points a1, . . . , an. (The matrix Y (z) considered
in a neighbourhood of a non-singular point z0 goes to Y (z)Mi under an analytic continuation
along a simple loop γi encircled a point ai.) As the operation of analytic continuation commutes
with diﬀerentiation and preserves elements of the ﬁeld C(z) (single-valued functions), one has
M ⊆ G. Furthermore the Galois group of a system whose singular points are all regular is a
closure of its monodromy group (in the Zariski topology, see [13, Ch. 6, Cor. 1.3]), hence such
a system is solvable by quadratures, if and only if the identity component of its monodromy
group is solvable.
We are interested in the cases when the answer to the question concerning solvability of a
linear diﬀerential system by quadratures can be given in terms of the coeﬃcient matrix of the
system. For example, in the case of a Fuchsian system (a particular case of a system with regular
singular points)
 dy
dz = ( n∑

i=1
 Bi
z − ai
 )y, Bi ∈ Mat(p, C), (2)

whose coeﬃcients Bi are suﬃciently small, Yu. S. Ilyashenko and A. G. Khovansky [9] have ob-
tained an explicit criterion of solvability. Namely, the following statement holds:
There exists ε = ε(n, p) > 0 such that a condition of solvability by quadratures for the
Fuchsian system (2) with ∥Bi∥ < ε takes an explicit form: the system is solvable by quadratures,
if and only if all the matrices Bi are triangular (in some basis).
In this article we propose a reﬁnement of the above assertion in which it is suﬃcient that
the eigenvalues of the residue matrices Bi be small (the estimate is given), and we also propose
a generalization to the case of a system with irregular singular points.

2 A local form of solutions of a system near its singular points

A singular point ai of the system (1) is said to be Fuchsian, if the coeﬃcient matrix B(z) has a
simple pole at this point.
Due to Sauvage’s theorem, a Fuchsian singular point of a linear diﬀerential system is regular
(see [8, Th. 11.1]). However, the coeﬃcient matrix of a system at a regular singular point may

2

in general have a pole of order greater than one. Let us write the Laurent expansion of the
coeﬃcient matrix B(z) of the system (1) near its singular point z = a in the form

B(z) = B−r−1
(z − a)r+1 + . . . + B−1
z − a + B0 + . . . , B−r−1 ̸= 0. (3)

The number r is called the Poincar´e rank of the system (1) at this point (or the Poincar´e rank
of the singular point z = a). For example, the Poincar´e rank of a Fuchsian singularity is equal
to zero.

The system (1) is said to be Fuchsian, if all its singular points are Fuchsian (then it can be
written in the form (2)). The system whose singular points are all regular will be called regular
singular.
According to Levelt’s theorem [15], in a neighbourhood of each regular singular point ai of
the system (1) there exists a fundamental matrix of the form

Yi(z) = Ui(z)(z − ai)
Ai(z − ai) ̃Ei, (4)

where Ui(z) is a holomorphic matrix at the point ai, Ai = diag(ϕ1
i , . . . , ϕ
p
i ) is a diagonal integer
matrix whose entries ϕ
j
i organize in a non-increasing sequence, ̃Ei = (1/2πi) ln ̃Mi is an upper-
triangular matrix (the normalized logarithm of the corresponding monodromy matrix) whose
eigenvalues ρ
j
i satisfy the condition 0 ⩽ Re ρj
i < 1.

Such a fundamental matrix is called a Levelt matrix, and one also says that its columns form a
Levelt basis in the solution space of the system (in a neighborhood of the regular singular point
ai). The complex numbers βj
i = ϕ
j
i + ρj
i are called the (Levelt) exponents of the system at the
regular singular point ai.
If the singular point ai is Fuchsian, then the corresponding matrix Ui(z) in the decomposition
(4) is holomorphically invertible at this point, that is, det Ui(ai) ̸= 0. It is not diﬃcult to check
that in this case the exponents of the system at the point ai coincide with the eigenvalues of the
residue matrix Bi. And in the general case of a regular singularity ai there are estimates for the
order of the function det Ui(z) at this point obtained by E. Corel [4] (see also [6]):

ri ⩽ ordai det Ui(z) ⩽ p(p − 1)
2 ri,

where ri is the Poincar´e rank of the regular singular point ai. These estimates imply the
inequalities for the sum of exponents of the regular system over all its singular points, which are
called the Fuchs inequalities:

− p(p − 1)
2
 n∑

i=1 ri ⩽
 n∑

i=1
 p∑

j=1 βj
i ⩽ −
 n∑

i=1 ri (5)

(the sum of exponents is an integer).
Let us now describe the structure of solutions of the system (1) near one of its irregular
singular points. We suppose that the irregular singularity ai of Poincar´e rank ri is non-resonant,
that is, the eigenvalues b1
i , . . . , bp
i of the leading term B−ri−1 of the matrix B(z) in the expansion
(3) at this point are pairwise distinct. Let us ﬁx a matrix Ti reducing the leading term B−ri−1
to the diagonal form T −1
i B−ri−1Ti = diag(b
1
i , . . . , bp
i ).

3

Then the system possesses a uniquely determined formal fundamental matrix ̂Yi(z) of the form

̂Yi(z) = ̂Fi(z)(z − ai)
Λie
Qi(z),

where

a) ̂Fi(z) is a matrix formal Taylor series in z − ai and ̂Fi(ai) = Ti;

b) Λi is a constant diagonal matrix whose diagonal entries are called the formal exponents of
the system (1) at the irregular singular point ai;

c) Qi(z) = diag(q1
i (z), . . . , qp
i (z)) is a diagonal matrix whose diagonal entries qj
i (z) are poly-
nomials in (z − ai)−1 of degree ri without a constant term,

qj
i (z) = − bj
i
ri (z − ai)
−ri + o((z − ai)
−ri).

Furthermore a punctured neighbourhood of the point ai can be covered by a set {S1
i , . . . , SNi
i }
of ”good” open sectors with vertex at this point (which we take to be arranged in counterclock-
wise order starting with S1
i ) such that in each Sj
i there exists a unique genuine fundamental
matrix
 Y j
i (z) = F j
i (z)(z − ai)
Λie
Qi(z) (6)

of the system (1) whose factor F j
i (z) has the asymptotic expansion ̂Fi(z) in Sj
i (see [11, Th.
21.13, Prop. 21.17]). In every intersection Sj
i ∩ Sj+1
i the fundamental matrices Y j
i and Y j+1
i
necessarily diﬀer by a constant invertible matrix:

Y j+1
i (z) = Y j
i (z)C j
i , C j
i ∈ GL(p, C),

and it is understood that the logarithmic term (z − ai)Λi is analytically continued from S1
i to
S2
i , from S2
i to S3
i , ..., from SNi
i to S1
i , so that

Y 1
i (z)e
2πiΛi = Y Ni
i (z)C Ni
i in SNi
i ∩ S1
i . (7)

The matrices C 1
i , . . . , C Ni
i are called Stokes matrices of the system (1) at the non-resonant
irregular singular point ai. They satisfy the relation

e
2πiΛi = M 1
i C 1
i . . . C Ni
i , (8)

where M 1
i is the monodromy matrix of Y 1
i at the point ai. Indeed, the fundamental matrix
Y 1
i can be continued from S1
i into S2
i as Y 2
i (C 1
i )−1, since Y 1
i = Y 2
i (C 1
i )−1 in S1
i ∩ S2
i . Fur-
ther it is continued from S2
i into S3
i as Y 3
i (C 1
i C 2
i )−1, etc. Finally, in SNi
i it becomes equal to
Y Ni
i (C 1
i . . . C Ni−1
i )−1. Then it comes back into S1
i as Y 1
i e2πiΛi(C 1
i . . . C Ni
i )−1 according to (7),
whence the relation (8) follows. It is also known that all the eigenvalues of any Stokes matrix are
equal to 1, that is, the Stokes matrices are unipotent (see [11, Prop. 21.19] or [19, Th. 15.2]).

4

3 Linear diﬀerential systems and meromorphic connections on
holomorphic vector bundles

Let us recall some notions concerning holomorphic vector bundles and meromorphic connections
in a context of linear diﬀerential equations. Here we mainly follow [11, Ch. 3] or [7] (see also
[3]).
In an analytic interpretation, a holomorphic bundle E of rank p over the Riemann sphere is
deﬁned by a cocycle {gαβ(z)}, that is, a collection of holomorphic matrix functions corresponding
to a covering {Uα} of the Riemann sphere:

gαβ : Uα ∩ Uβ −→ GL(p, C), Uα ∩ Uβ ̸= ∅.

These functions satisfy the conditions

gαβ = g−1
βα , gαβgβγgγα = I (for Uα ∩ Uβ ∩ Uγ ̸= ∅).

Two holomorphically equivalent cocycles {gαβ(z)}, {g′
αβ(z)} deﬁne the same bundle. Equiva-
lence of cocycles means that there exists a set {hα(z)} of holomorphic matrix functions hα :
Uα −→ GL(p, C) such that
 hα(z)gαβ (z) = g′
αβ(z)hβ(z). (9)

A section s of the bundle E is determined by a set {sα(z)} of vector functions sα : Uα −→ Cp

that satisfy the conditions sα(z) = gαβ(z)sβ(z) in intersections Uα ∩ Uβ ̸= ∅ .
A meromorphic connection ∇ on the holomorphic vector bundle E is determined by a set
{ωα} of matrix meromorphic diﬀerential 1-forms that are deﬁned in the corresponding neigh-
bourhoods Uα and satisfy gluing conditions

ωα = (dgαβ)g−1
αβ + gαβωβg−1
αβ (for Uα ∩ Uβ ̸= ∅). (10)

Under a transition to an equivalent cocycle {g′
αβ} connected with the initial one by the relations
(9), the 1-forms ωα of the connection ∇ are transformed into the corresponding 1-forms

ω′
α = (dhα)h
−1
α + hαωαh
−1
α . (11)

Conversely, the existence of holomorphic matrix functions hα : Uα −→ GL(p, C) such that
the matrix 1-forms ωα and ω′
α (satisfying the conditions (10) for gαβ and g′
αβ respectively) are
connected by the relation (11) in Uα, indicates the equivalence of the cocycles {gαβ } and {g′
αβ}
(one may assume that the intersections Uα ∩Uβ do not contain singular points of the connection).
Vector functions sα(z) satisfying linear diﬀerential equations dsα = ωαsα in the correspond-
ing Uα, by virtue of the conditions(10) can be chosen so that a set {sα(z)} determines a section
of the bundle E, which is called horizontal with respect to the connection ∇. Thus horizon-
tal sections of a holomorphic vector bundle with a meromorphic connection are determined by
solutions of local linear diﬀerential systems. The monodromy of a connection (the monodromy
group) characterizes ramiﬁcation of horizontal sections under their analytic continuation along
loops in C not containing singular points of the connection 1-forms and is deﬁned similarly to
the monodromy group of the system (1). A connection may be called Fuchsian (logarithmic),
regular or irregular depending on the type of the singular points of its 1-forms (as singular points
of linear diﬀerential systems).
If a bundle is holomorphically trivial (all matrices of the cocycle can be taken as the identity
matrices), then by virtue of the conditions (10) the matrix 1-forms of a connection coincide

5

on non-empty intersections Uα ∩ Uβ. Hence horizontal sections of such a bundle are solutions
of a global linear diﬀerential system deﬁned on the whole Riemann sphere. Conversely, the
linear system (1) determines a meromorphic connection on the holomorphically trivial vector
bundle of rank p over C. It is understood that such a bundle has the standard deﬁnition by
the cocycle that consists of the identity matrices while the connection is deﬁned by the matrix
1-form B(z)dz of coeﬃcients of the system. But for us it will be more convenient to use the
following equivalent coordinate description (a construction already appearing in [3]).
At ﬁrst we consider a covering {Uα} of the punctured Riemann sphere C \ {a1, . . . , an} by
simply connected neighbourhoods. Then on the corresponding non-empty intersections Uα ∩ Uβ
one deﬁnes the matrix functions of a cocycle, g′
αβ(z) ≡ const, which are expressed in terms of
the monodromy matrices M1, . . . , Mn of the system (1) via the operations of multiplication and
taking the inverse (see [7]). In this case the matrix diﬀerential 1-forms ω′
α deﬁning a connection
are equal to zero. Further the covering {Uα} is complemented by small neighbourhoods Oi of
the singular points ai of the system, thus we obtain the covering of the Riemann sphere C.
To non-empty intersections Oi ∩ Uα there correspond matrix functions g′
iα(z) = Yi(z) of the
cocycle, where Yi(z) is a germ of a fundamental matrix of the system whose monodromy matrix
at the point ai is equal to Mi (so, for analytic continuations of the chosen germ to non-empty
intersections Oi ∩ Uα ∩ Uβ the cocycle relations giαgαβ = giβ hold). The matrix diﬀerential 1-
forms ω′
i determining the connection in the neighbourhoods Oi coincide with the 1-form B(z)dz
of coeﬃcients of the system. To prove holomorphic equivalence of the cocycle {g′
αβ, g′
iα} to the
identity cocycle it is suﬃcient to check existence of holomorphic matrix functions

hα : Uα −→ GL(p, C), hi : Oi −→ GL(p, C),

such that
 ω′
α = (dhα)h
−1
α + hαωαh
−1
α , ω′
i = (dhi)h
−1
i + hiωih
−1
i . (12)

Since we have ωα = B(z)dz and ω′
α = 0 for all α, the ﬁrst equation in (12) is rewritten as a
linear system d(h
−1
α ) = (B(z)dz)h
−1
α ,

which has a holomorphic solution h−1
α : Uα −→ GL(p, C) since the 1-form B(z)dz is holomorphic
in a simply connected neighbourhood Uα. The second equation in (12) has a holomorphic
solution hi(z) ≡ I, as ωi = ω′
i = B(z)dz.

One says that a bundle E has a subbundle E′ ⊂ E of rank k < p that is stabilized by a
connection ∇, if the pair (E, ∇) admits a coordinate description {gαβ}, {ωα} of the following
blocked upper-triangular form:

gαβ = ( g1
αβ ∗
0 g2
αβ
 ) , ωα = ( ω1
α ∗
0 ω2
α
 ) ,

where g1
αβ and ω1
α are blocks of size k × k (then the cocycle {g1
αβ } deﬁnes the subbundle E′ and
the 1-forms ω1
α deﬁne the restriction ∇′ of the connection ∇ to the subbundle E′).

Example 1. Consider a system (1) whose monodromy matrices M1, . . . , Mn are of the same
blocked upper-triangular form, and the corresponding holomorphically trivial vector bundle E
with the meromorphic connection ∇. Suppose that in a neighbourhood of each singular point
ai of the system there exist a fundamental matrix Yi(z) whose monodromy matrix is Mi, and
a holomorphically invertible matrix Γi(z) such that Γi Yi is a blocked upper-triangular matrix

6

(with respect to the blocked upper-triangular form of the matrix Mi). Let us show that to the
common invariant subspace of the monodromy matrices there corresponds a vector subbundle
E′ ⊂ E that is stabilized by the connection ∇.
We use the above coordinate description of the bundle and connection with the cocycle
{g′
αβ, g′
iα} and set {ω′
α, ω′
i} of matrix 1-forms. The matrices g′
αβ are already blocked upper-
triangular since the monodromy matrices M1, . . . , Mn are (and ω′
α = 0), while the matrices
g′
iα = Yi can be transformed to such a form, Γi g′
iα = Γi Yi. Thus changing the matrices g′
iα onto
Γi g′
iα and matrix 1-forms ω′
i onto
 Γi ω′
i Γ−1
i + (dΓi)Γ−1
i ,

we pass to the holomorphically equivalent coordinate description with the cocycle matrices and
connection matrix 1-forms having the same blocked upper-triangular form.

The following auxiliary lemma points to a certain block structure of a linear diﬀerential
system in the case when the corresponding holomorphically trivial vector bundle with the mero-
morphic connection has a holomorphically trivial subbundle that is stabilized by the connection.

Lemma 1. If a holomorphically trivial vector bundle E of rank p over C endowed with a
meromorphic connection ∇ has a holomorphically trivial subbundle E′ ⊂ E of rank k that is
stabilized by the connection, then the corresponding linear system (1) is reduced to a blocked
upper-triangular form via a constant gauge transformation ˜y(z) = Cy(z), C ∈ GL(p, C). That
is,
 CB(z)C −1 = ( B′(z) ∗
0 ∗
 ) ,

where B′(z) is a block of size k × k.

Proof. Let {s1, . . . , sp} be a basis of global holomorphic sections of the bundle E (which are
linear independent at each point z ∈ C) such that the 1-form of the connection ∇ in this basis
is the 1-form B(z)dz of coeﬃcients of the linear system. Consider also a basis {s′
1, . . . , s′
p} of
global holomorphic sections of the bundle E such that s′
1, . . . , s′
k are sections of the subbundle
E′, (s′
1, . . . , s′
p) = (s1, . . . , sp)C −1, C ∈ GL(p, C).
Now choose a basis {h1, . . . , hp} of sections of the bundle E such that these are horizontal
with respect to the connection ∇ and h1, . . . , hk are sections of the subbundle E′ (this is possible
since E′ is stabilized by the connection). Let Y (z) be a fundamental matrix of the system whose
columns are the coordinates of the sections h1, . . . , hp in the basis {s1, . . . , sp}. Then

̃Y (z) = CY (z) = ( k × k ∗
0 ∗
 )

is a blocked upper-triangular matrix, since its columns are the coordinates of the sections
h1, . . . , hp in the basis {s′
1, . . . , s′
p}. Consequently, the transformation ˜y(z) = Cy(z) reduces
the initial system to a blocked upper-triangular form. □

The degree deg E (which is an integer) of a holomorphic vector bundle E endowed with a
meromorphic connection ∇ may be deﬁned as the sum

deg E =
 n∑

i=1 resai tr ωi

7

of the residues of local diﬀerential 1-forms tr ωi over all singular points of the connection (the
notation ”tr” is for the trace), where ωi is the local matrix diﬀerential 1-form of the connection
∇ in a neighbourhood of its singular point ai. Later when calculating the degree of a bundle we
will apply the Liouville formula tr ωi = d ln det Yi, where Yi is a fundamental matrix of the local
linear diﬀerential system dy = ωi y.

4 Solvability of regular singular systems with small exponents

Consider a system (1) with regular singular points a1, . . . , an of Poincar´e rank r1, . . . , rn respec-
tively. If the real part of the exponents of this system is suﬃciently small, then the following
necessary condition, of solvability by quadratures, holds.

Theorem 1. Let for some k ∈ {1, . . . , p − 1} the exponents βj
i of the regular singular system
(1) satisfy the condition

Re βj
i > −1/nk, i = 1, . . . , n, j = 1, . . . , p, (13)

and, for each pair βj
i ̸≡ βl
i (mod Z), i = 1, . . . , n, one of the conditions

Re βj
i − Re βl
i ̸∈ Q or Im βj
i ̸= Im βl
i. (14)

Then the solvability of the system (1) by quadratures implies the existence of a constant matrix
C ∈ GL(p, C) such that the matrix CB(z)C −1 is of the following blocked form:

CB(z)C −1 = ( B′(z) ∗
0 ∗
 ) ,

where B′(z) is an upper-triangular matrix of size k × k.

Remark 1. Though the inequalities (13) restrict the real parts of the exponents from below,
together with the estimates (5) they provide boundedness from above.
Remark 2. The sum of the Poincar´e ranks of a regular singular system whose exponents
satisfy the condition (13) is indeed restricted because of the Fuchs inequalities (5), namely,∑n
i=1 ri < p/k.

The proof of the theorem is based on two auxiliary lemmas.

Lemma 2. Let the exponents βj
i of the regular singular system (1) satisfy the condition (13).
If the monodromy matrices of this system are upper-triangular, then there is a constant matrix
C ∈ GL(p, C) such that the matrix CB(z)C −1 has the form as in Theorem 1.

Proof. We use a geometric interpretation (exposed in the previous section) according to
which to the regular singular system (1) there corresponds the holomorphically trivial vector
bundle E of rank p over the Riemann sphere endowed with the meromorphic connection ∇ with
the regular singular points a1, . . . , an.
Since the monodromy matrices M1, . . . , Mn of the system are upper-triangular there exists,
as shown in Example 1, a ﬂag E1 ⊂ E2 ⊂ . . . ⊂ Ep = E of subbundles of rank 1, 2, . . . , p respec-
tively that are stabilized by the connection ∇. Indeed, a fundamental matrix Y determining the
monodromy matrices M1, . . . , Mn of the system can be represented near each singular point ai
in the form Y (z) = Ti(z)(z − ai)
Ei, Ei = (1/2πi) ln Mi,

8

where Ti is a meromorphic matrix at the point ai. This matrix can be factored as Ti = Vi Pi,
with a holomorphically invertible matrix Vi at ai and an upper-triangular matrix Pi which is a
polynomial in (z − ai)±1 (see, for example, [6, Lemma 1]). Thus the matrix V −1
i Y is upper-
triangular.
Let us estimate the degree of each subbundle Ej, j ⩽ k, noting that in a neighbourhood of
each singular point ai the initial system is transformed via a holomorphically invertible gauge
transformation in a system with a fundamental matrix of the form

Yi(z) = ( U ′
i(z) ∗
0 ∗
 ) (z − ai)

( A′
i 0
0 ∗
 )
(z − ai)

( E′
i ∗
0 ∗
 )

such that the matrix Y ′
i (z) = U ′
i(z)(z −ai)A′
i(z −ai)E′
i is a Levelt fundamental matrix for a linear
system of j equations with the regular singular point ai. The matrix 1-form of coeﬃcients of
this system in a neighbourhood of ai is a local 1-form of the restriction ∇j of the connection ∇
to the subbundle Ej, and the exponents ˜β1
i , . . . , ˜βj
i of this system (the eigenvalues of the matrix
A′
i + E′
i) form a subset of the exponents of the initial system at ai. Therefore,

Re ˜βl
i > −1/nk, l = 1, . . . , j.

The degree of the holomorphically trivial vector bundle Ep is equal to zero, and for j ⩽ k one
has:
 deg Ej =
 n∑

i=1 resaid ln det Y ′
i (z) =
 n∑

i=1 ordai det U ′
i(z) +
 n∑

i=1 tr(Λ
′
i + E′
i) =

=
 n∑

i=1 ordai det U ′
i(z) +
 n∑

i=1
 j∑

l=1 Re ˜βl
i > −j/k ⩾ −1.

As the degree of a subbundle of a holomorphically trivial vector bundle is non-positive, one has
deg Ej = 0, hence all the subbundles E1 ⊂ . . . ⊂ Ek are holomorphically trivial (a subbundle of
a holomorphically trivial vector bundle is holomorphically trivial, if its degree is equal to zero,
see [11, Lemma 19.16]). Now the assertion of the lemma follows from Lemma 1. □

A matrix A will be called N -resonant, if there are two eigenvalues λ1 ̸= λ2 such that λN
1 = λN
2 ,
that is,
 |λ1| = |λ2|, arg λ1 − arg λ2 = 2π
N j, j ∈ {1, 2, . . . , N − 1}.

Let a group M ⊂ GL(p, C) be generated by matrices M1, . . . , Mn. If these matrices are
suﬃciently close to the identity (in the Euclide topology) then the existence of a solvable normal
subgroup of ﬁnite index in M implies their triangularity, see Theorem 2.7 [13, Ch. 6]. According
to the remark following this theorem, the requirement of proximity of the matrices Mi to the
identity can be weakened as follows.

Lemma 3. There is a number N = N (p) such that if the matrices M1, . . . , Mn are not
N -resonant, then the existence of a solvable normal subgroup of ﬁnite index in M implies their
triangularity.

Proof of Theorem 1. From the theorem assumptions it follows that the identity component
G0 of the diﬀerential Galois group G of the system (1) is solvable, hence G0 is a solvable normal
subgroup of G of ﬁnite index. Then the monodromy group M of this system also has a solvable
normal subgroup of ﬁnite index, namely M ∩ G0.

9

As follows from the deﬁnition of the exponents βj
i of a linear diﬀerential system at a regular
singular point ai, these are connected with the eigenvalues µj
i of the monodromy matrix Mi by
the relation µj
i = exp(2π i βj
i ).

Therefore,

µj
i = exp(2π i(Re βj
i + i Im βj
i )) = e
−2π Im βj
i (cos(2π Re βj
i ) + i sin(2π Re βj
i )),

and for any N the matrices Mi are non N -resonant by the conditions (14) on the numbers βj
i .
Now the assertion of the theorem follows from Lemma 2 and Lemma 3. □

As a consequence of Theorem 1 we obtain the following reﬁnement of the Ilyashenko–
Khovansky theorem on solvability by quadratures of a Fuchsian system with small residue
matrices.

Corollary 1. Let the eigenvalues βj
i of the residue matrices Bi of the Fuchsian system (2)
satisfy the condition

Re βj
i > − 1
n(p − 1) , i = 1, . . . , n, j = 1, . . . , p, (15)

and, for each pair βj
i ̸≡ βl
i (mod Z), i = 1, . . . , n, one of the conditions (14). Then the solvability
of the Fuchsian system (2) by quadratures is equivalent to the simultaneous triangularity of the
matrices Bi.

Proof. The necessity of simultaneous triangularity is a direct consequence of Theorem 1,
since the exponents of the Fuchsian system (2) at ai coincide with the eigenvalues of the residue
matrix Bi. Suﬃciency follows from a general fact that any linear diﬀerential system with an
(upper-) triangular coeﬃcient matrix is solvable by quadratures (one should begin with the last
equation). □

Remark 3. The inequalities (15) restricting the real parts of the exponents of the Fuchsian
system from below also provide their boundedness from above because of the Fuchs relation∑n
i=1 ∑p
j=1 βj
i = 0 (see (5)). Namely,

− 1
n(p − 1) < Re βj
i < np − 1
n(p − 1) .

In particular, the integer parts ϕ
j
i of the numbers Re βj
i for such a system have to belong to the
set {−1, 0, 1}.

Remark 4. If each residue matrix Bi of the Fuchsian system (2) only has one eigenvalue
βi, then the solvability of this system by quadratures is also equivalent to the simultaneous
triangularity of the matrices Bi (not depending on values of Re βi). Indeed, in this case each
monodromy matrix Mi only has one eigenvalue µi = e2πiβi, hence is not N -resonant. Then the
solvability implies the simultaneous triangularity of the monodromy matrices and existence of
a ﬂag E1 ⊂ E2 ⊂ . . . ⊂ Ep = E of subbundles of the holomorphically trivial vector bundle
E that are stabilized by the logarithmic connection ∇ (corresponding to the Fuchsian system).
Since deg E = ∑n
i=1 pβi = 0, the degree ∑n
i=1 jβi of each subbundle Ej is zero and all these
subbundles are holomorphically trivial.
 10

It is natural to expect that for a general Fuchsian system (with no restrictions on the ex-
ponents) solvability by quadratures not necessarily implies simultaneous triangularity of the
residue matrices. This is indeed illustrated by the following example of A. Bolibrukh.

Example 2 (A. Bolibrukh [2, Prop. 5.1.1]). There exist points a1, a2, a3, a4 on the Riemann
sphere and a Fuchsian system with singularities at these points, whose monodromy matrices are

M1 =
 










 1 1 1 −1 0 0 −1
0 −1 −1 0 0 0 1
0 0 1 1 2 2 2
0 0 0 1 1 0 1
0 0 0 0 1 1 1
0 0 0 0 0 1 0
0 0 0 0 0 0 −1
 










 , M2 =
 










 1 1 0 1 1 1 0
0 −1 1 1 −1 1 −1
0 0 −1 −1 1 −1 0
0 0 0 1 1 1 0
0 0 0 0 −1 −1 1
0 0 0 0 0 1 0
0 0 0 0 0 0 −1
 










 ,

M3 =
 










 1 0 1 0 −1 0 0
0 −1 −1 1 −1 1 2
0 0 1 1 −1 1 2
0 0 0 −1 1 −1 −2
0 0 0 0 −1 1 1
0 0 0 0 0 1 1
0 0 0 0 0 0 −1
 










 , M4 =
 










 1 0 1 −1 1 1 0
0 −1 1 −2 0 0 0
0 0 −1 1 0 0 0
0 0 0 −1 1 0 1
0 0 0 0 1 1 0
0 0 0 0 0 1 1
0 0 0 0 0 0 −1
 










 ,

whereas the coeﬃcient matrix of this system is not upper-triangular. Moreover, this system
cannot be transformed in an upper-triangular form neither via a constant gauge transformation
nor even a meromorphic (rational) one preserving the singular points a1, a2, a3, a4 and the orders
of their poles. Thus the residue matrices of this Fuchsian system are not triangular in any basis
though the system is solvable by quadratures, since its monodromy group generated by the
triangular matrices is solvable.
We notice that Corollary 1 does not apply to this example as its exponents cannot satisfy
the conditions (15). Indeed, for any exponent βj
i = ϕ
j
i + ρ
j
i one has

ρ
j
i = 1
2πi ln µj
i , µj
i ∈ {−1, 1},

hence Re ρj
i is equal to 0 or 1/2. The inequalities (15) imply (for n = 4, p = 7)

Re βj
i > − 1
24 ,

hence ϕ
j
i is equal to 0 or 1 (see Remark 3). Therefore, the sum of the exponents over all singular
points is positive, which contradicts the Fuchs relation.

5 A criterion of solvability for a non-resonant irregular system
with small formal exponents

Consider the system (1) with non-resonant irregular singular points a1, . . . , an of Poincar´e rank
r1, . . . , rn respectively. If the real part of the formal exponents of this system is suﬃciently
small, then the following criterion of solvability by quadratures holds.

11

Theorem 2. Let at each singular point ai the formal exponents λj
i of the irregular system
(1) be pairwise distinct and satisfy the condition

Re λj
i > − 1
n(p − 1) ,

and, for every pair (λj
i , λl
i), one of the conditions (14). Then this system is solvable by quadra-
tures if and only if there is a constant matrix C ∈ GL(p, C) such that CB(z)C −1 is upper-
triangular.

Proof. As in Corollary 1, suﬃciency does not require a special proof. Let us prove necessity.
Consider a fundamental matrix Y of the system (1) and the representation of the diﬀerential
Galois group G with respect to this matrix. The connection matrices between Y and the
fundamental matrices Y 1
1 , . . . , Y 1
n (the latter were deﬁned at the end of Section 2) denote by
P1, . . . , Pn respectively: Y (z) = Y 1
i (z)Pi, i = 1, . . . , n.

Then, as we noted earlier, the monodromy matrices Mi = P −1
i M 1
i Pi (i = 1, . . . , n) with respect
to Y belong to the group G. Moreover, as follows from Ramis’ theorem [18]1, the corresponding
Stokes matrices
 ̃C 1
i = P −1
i C 1
i Pi, . . . , ̃C Ni
i = P −1
i C Ni
i Pi (i = 1, . . . , n)

also belong to G. Therefore, by the relation

e
2πĩΛi = Mi ̃C 1
i . . . ̃C Ni
i , ̃Λi = P −1
i ΛiPi,

(see (8)), the group G also contains the matrices e2πĩΛi of formal monodromy.
Denote by ̂M the group ⟨e2πĩΛi, ̃C 1
i , . . . , ̃C Ni
i ⟩
n
i=1 generated by the matrices of formal mon-
odromy and Stokes matrices over all singular points. As follows from the condition of the
theorem, the group G possesses the solvable normal subgroup G0 of ﬁnite index. Hence the
subgroup ̂M ⊂ G possesses the solvable normal subgroup of ﬁnite index, ̂M ∩ G0. Since for
any N the matrices generating the group ̂M are non N -resonant, according to Lemma 3 they
are simultaniously reduced to an upper-triangular form by conjugating to some non-degenerated
matrix ̃C (non-resonance of the formal monodromy matrices e2πĩΛi follows from the conditions
on the formal exponents, the eigenvalues of the matrices ̃Λi, and is proved as in Theorem 1; for
the Stokes matrices it follows from their unipotence). We may assume that they are already
upper-triangular (otherwise we would consider the fundamental matrix Y ̃C instead of Y ). As
follows from [5, Ch. VIII, §1], the relation

Λi = Pi ̃Λi P −1
i ,

where ̃Λi is an upper-triangular matrix and Λi is a diagonal matrix whose diagonal elements are
pairwise distinct, implies that the matrix Pi writes Pi = Di Ri, where Ri is an upper-triangular
matrix (the conjugation Ri ̃Λi R−1
i annulates all the oﬀ-diagonal elements of the matrix ̃Λi) and
Di is a permutation matrix for Λi (that is, the conjugation D−1
i Λi Di permutes the diagonal
elements of the matrix Λi).

1It is diﬃcult to ﬁnd the original proof of it, but there exist various variants of this theorem and comments to
it proposed by the other authors (see [10, Ths. 1, 6], [14], [16, Th. 2.3.11]+[17, Prop. 1.3]).

12

In a neighbourhood of each ai we pass from the set of fundamental matrices Y 1
i , . . . , Y Ni
i ,
which correspond to the sectors S1
i , . . . , SNi
i , to the fundamental matrices

̃Y j
i (z) = Y j
i (z)Pi (in particular, ̃Y 1
i = Y )

connected to each other in the intersections Sj
i ∩ Sj+1
i by the relations

̃Y j+1
i (z) = ̃Y j
i (z) ̃C j
i .

From the decomposition of Pi above and from (6) it follows that the matrices ̃Y j
i can be written

̃Y j
i (z) = F j
i (z)(z − ai)
Λie
Qi(z)Di Ri = F j
i (z)Di(z − ai)
Λ′
ie
Q′
i(z)Ri,

where Λ
′
i = D−1
i Λi Di, Q′
i(z) = D−1
i Qi(z) Di

are diagonal matrices obtained from the corresponding matrices Λi, Qi(z) by a permutation of
the diagonal elements. Therefore, in the intersections Sj
i ∩ Sj+1
i we have the relations

F j+1
i (z)Di(z − ai)
Λ′
ie
Q′
i(z)Ri = F j
i (z)Di(z − ai)
Λ′
ie
Q′
i(z)Ri ̃C j
i .

Thus in the sectors S1
i , . . . , SNi
i , which form a covering of a punctured neighbourhood of ai,
there are holomorphically invertible matrices F 1
i (z)Di, . . . , F Ni
i (z) Di respectively such that in
the intersections Sj
i ∩ Sj+1
i their quotients

(
F j
i (z)Di)−1 F j+1
i (z)Di = (z − ai)
Λ′
ie
Q′
i(z)Ri ̃C j
i R−1
i e
−Q′
i(z)(z − ai)
−Λ′
i

are upper-triangular matrices. As each matrix F j
i (z)Di has the same asymptotic expansion
̂Fi(z)Di in the corresponding Sj
i , there exists a matrix Γi(z) holomorphically invertible at the
point ai such that all the matrices

̃F j
i (z) = Γi(z)F j
i (z)Di, j = 1, . . . , Ni,

are upper-triangular (according to [1, Prop. 3]). In particular,

Γi(z)Y (z) = Γi(z) ̃Y 1
i (z) = Γi(z)F 1
i (z)Di(z − ai)
Λ′
ie
Q′
i(z)Ri = ̃F 1
i (z)(z − ai)
Λ′
ie
Q′
i(z)Ri

is an upper-triangular matrix. Hence (see Example 1) one has a ﬂag E1 ⊂ E2 ⊂ . . . ⊂ Ep = E of
subbundles of rank 1, 2, . . . , p respectively that are stabilized by the connection ∇. The bounds
on the formal exponents imply that these subbundles are holomorphically trivial, whence the
assertion of the theorem follows. The proof proceeds as for Lemma 2, there are only two small
diﬀerences: the ﬁrst one is that now we deal with formal fundamental matrices of subsystems
and their formal exponents, which form a subset of the formal exponents of the initial system
at each irregular singular point ai; the second one is the appearence of an exponential factor in
a formal fundamental matrix of a subsystem, but the logarithmic diﬀerential of such a factor
has a zero residue at ai. □

13

References

[1] W. Balser, W. B. Jurkat, D. A. Lutz, Invariants for reducible systems of meromorphic dif-
ferential equations, Proc. Edinburgh Math. Soc., 1980, V. 23, P. 163–186.

[2] A. A. Bolibruch, The 21st Hilbert problem for linear Fuchsian systems, Proc. Steklov Inst.
Math., 1994, V. 206.

[3] A. A. Bolibruch, S. Malek, C. Mitschi, On the generalized Riemann–Hilbert problem with
irregular singularities, Expo. Math., 2006, V. 24(3), P. 235–272.

[4] E. Corel, Relations de Fuchs pour les syst`emes diﬀ´erentiels r´eguliers, Bull. S. M. F, 2001,
V. 129, P. 189–210.

[5] F. R. Gantmacher, Theory of matrices, Chelsea, New York, 1959.

[6] R. R. Gontsov, Reﬁned Fuchs inequalities for systems of linear diﬀerential equations,
Izvestiya: Mathematics, 2004, V. 68(2), P. 259–272.

[7] R. R. Gontsov, V. A. Poberezhnyi, Various versions of the Riemann–Hilbert problem for lin-
ear diﬀerential equations, Russian Math. Surveys, 2008, V. 63(4), P. 603–639.

[8] P. Hartman, Ordinary diﬀerential equations, Wiley, New York, 1964.

[9] Yu. S. Ilyashenko, A. G. Khovansky, Galois theory of diﬀerential systems of Fuchsian type
with small coeﬃcients (in Russian), Keldysh Inst. Appl. Math., Preprint N 117, 1974.

[10] Yu. S. Ilyashenko, A. G. Khovansky, Galois groups, Stokes multipliers and Ramis’ theorem,
Funct. Anal. Appl., 1990, V. 24(4), P.

[11] Yu. S. Ilyashenko, S. Yakovenko, Lectures on analytic diﬀerential equations, Grad. Stud.
Math., V. 86, AMS, Providence, RI 2008.

[12] I. Kaplansky, An introduction to diﬀerential algebra, Hermann, Paris, 1957.

[13] A. G. Khovansky, Topological Galois theory. Solvability and non-solvability of equations in
ﬁnite terms (in Russian), MCCME, Moscow, 2008.

[14] V. Kostov, The Stokes multipliers and the Galois group of a non-Fuchsian system and the
generalized Phragmen–Lindel¨oﬀ principle, Funk. Ekvac., 1993, V. 36, P. 329–357.

[15] A. Levelt, Hypergeometric functions, Proc. Konikl. Nederl. Acad. Wetensch. Ser. A, 1961,
V. 64, P. 361–401.

[16] C. Mitschi, Diﬀerential Galois groups and G-functions, Computer Algebra and Diﬀerential
Equations, M. Singer, editor, Academic Press, 1991.

[17] C. Mitschi, Diﬀerential Galois groups of conﬂuent generalized hypergeometric equations: an
approach using Stokes multipliers, Paciﬁc J. Math., 1996, V. 176(2), P. 365–405.

[18] J.-P. Ramis, Filtration Gevrey sur le groupe de Picard–Vessiot d’une ´equation diﬀ´erentielle
irr´eguli`ere, Informes de Matematica, Preprint IMPA, Serie A-045/85, 1985.

[19] W. Wasow, Asymptotic expansions for ordinary diﬀerential equations, John Wiley & Sons,
New York–London–Sydney, 1965.
 14
