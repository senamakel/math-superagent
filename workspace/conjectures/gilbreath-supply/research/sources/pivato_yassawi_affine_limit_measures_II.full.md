<!-- source: https://arxiv.org/pdf/math/0108083 | converted from PDF -->

arXiv:math/0108083v2  [math.DS]  29 Apr 2003
Ergod. Th. & Dynam. Sys. (2003), 30, 1–20
Printed in the United Kingdom c⃝ 2003 Cambridge University Press

Limit Measures for Aﬃne Cellular Automata
II

Marcus Pivato† and Reem Yassawi‡†

† Department of Mathematics, Trent University
(e-mail: pivato@xaravve.trentu.ca)
‡ Department of Mathematics, Trent University, Lady Eaton College,
Peterborough, Ontario, K9L 1Z6 Canada
(e-mail: ryassawi@trentu.ca)

(Received ??? )

Abstract. If M is a monoid, and A is an abelian group, then A
M is a compact abelian
group; a linear cellular automaton (LCA) is a continuous endomorphism F : A
M−→A
M

that commutes with all shift maps. If F is diﬀusive, and µ is a harmonically mixing
(HM) probability measure on A
M, then the sequence {FN µ}∞
N =1 weak*-converges to the
Haar measure on A
M, in density. Fully supported Markov measures on A
Z are HM, and
nontrivial LCA on A(ZD) are diﬀusive when A = Z/p is a prime cyclic group.

In the present work, we provide suﬃcient conditions for diﬀusion of LCA on A(ZD) when
A = Z/n is any cyclic group or when A = (
Z/pr )J (p prime). We also show that any fully

supported Markov random ﬁeld on A(ZD) is HM (where A is any abelian group).

1. Introduction
Let A be a ﬁnite abelian group, with discrete topology. If M is any set, then A
M is a compact
abelian group when endowed with the Tychonoﬀ product topology and componentwise
addition. If M is a monoid (for example, a lattice: Z
D × NE), then the action of M
on itself by translation induces a natural shift action of M on conﬁguration space: for all
e ∈ M, and a ∈ A
M, deﬁne σe[a] = [bm|m∈M] where, ∀m ∈ M, bm = ae.m. Here “.” is the
monoid operator (“+” for M = Z
D × NE).
A linear cellular automaton (LCA) is a continuous endomorphism F : A
M −
←⊃ which
commutes with all shift maps. If µ is a measure on A
M, it is natural to consider the
sequence of measures {Fnµ|n∈N}, and ask whether this sequence converges in the weak*
topology on the space M [
A
M] of Borel probability measures on A
M. If {Fnµ|n∈N} does not
itself converge, we might hope at least for convergence in density (that is, convergence of a
subsequence {
Fjµ|j∈J }
, where J ⊂ N is a subset of Ces`aro density 1), or convergence of the

Ces`aro average 1
N
 N∑

n=1 Fnµ.

† This research partially supported by NSERC Canada.

Prepared using etds.cls [Version: 1999/07/21 v1.0]

2 M. Pivato, R. Yassawi

Let H denote the Haar measure on A
M. Since H is invariant under the algebraic
operations of A
M, it seems like a natural limit point for {Fnµ|n∈N}. Indeed, D. Lind showed
[5] that, if A = Z/2, and F is the automaton deﬁned: F(a)0 = a(−1) + a1, and µ is any

Bernoulli measure, then wk
∗− lim
N →∞ 1
N
 N∑

n=1 Fnµ = H. Lind also showed that {Fnµ|n∈N} does

not converge to H; convergence fails along the subsequence {
F(2
n)µ|n∈N}
.
Later, Ferrari, Maass, Martinez, and Ney showed similar Ces`aro convergence results in a
variety of special cases [7, 1]. Recently, Pivato and Yassawi [6] developed broad suﬃcient
conditions for convergence. The concepts of harmonic mixing for measures and diﬀusion
for LCA were introduced; if µ is a harmonically mixing probability measure and F a diﬀusive
LCA, then {Fnµ|n∈N } weak* converges to H in density, and thus, also in Ces`aro mean.

This paper is a continuation of [6]. First we will extend the results on diﬀusion of LCA
to a broader class of abelian groups: in §3, to the case when A = Z/n, for any n ∈ N, and

then in §4, to the case when A = (
Z/pr )J (p prime, J, r ∈ N). Next, in §5, we demonstrate

harmonic mixing for any Markov random ﬁeld on A(ZD) with full support.

2. Preliminaries
We recommend that the reader consult [6] before reading the present work; we will depend
heavily upon results introduced there. We will now brieﬂy review the relevant concepts; all
theorems in this section are proved in [6].

2.1. Characters and Harmonic Mixing Let T
1 be the unit circle group. A character of
A
M is a continuous group homomorphism φ : A
M−→T
1. The set of all characters of A
M

forms a group, denoted ̂AM.
If [
χm|m∈M] is a sequence of characters of A, with all but ﬁnitely many elements equal

to the constant 1-function (denoted “11”), then deﬁne χ = ⊗

m∈M χm : A
M−→T
1; thus, if

a = [
am|m∈M] is an element of A
M, then χ(a) = ∏

m∈M χm(am). All elements of ̂AM

arise in this manner. The rank of the character χ is the number of nontrivial entries in the
coeﬃcient system [χm|m∈M]
.

When A = Z/n, elements of ̂A are maps of the form χ(a) = exp ( 2πi
n c · a)
, where c ∈

Z/n is some constant. Elements of ̂AM are then products of the form χ(a) = ∏

m∈M χm(am),

where, ∀m ∈ M, χm : a ↦→ exp ( 2πi
n cm · a) for some cm ∈ A, with all but ﬁnitely many cm

are equal to 0. In this case, we will use the term coeﬃcient system also to describe the
sequence [cm|m∈M]
.
If µ is a measure on A
M, then the Fourier coeﬃcients of µ are deﬁned: ̂µ[χ] = ⟨χ, µ⟩ =∫

AM χ dµ, for every χ ∈ ̂AM. The measure µ is called harmonically mixing if, for all

ǫ > 0, there is some R > 0 so that, for all χ ∈ ̂AM, ( rank [χ] ≥ R ) =⇒ ( |̂µ[χ]| < ǫ ).

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata II 3

Let M [
A
M; C] be the space of complex-valued Borel measures on A
M, treated as a
Banach algebra under the total variation norm, with operations of addition and convolution.
Let H ⊂ M [
A
M; C] be the set of harmonically mixing measures.

Proposition 1. Let A be any ﬁnite abelian group.
1. H is an ideal of M [
A
M; C]
.
2. H is closed under the total variation norm and dense in the weak* topology.
3. H contains all Bernoulli measures β⊗M, where β is a measure on A such that, for any
subgroup G ⊂ A, the support of µ extends over more than one coset of G.
4. If M = Z, then, for any N > 0, H contains all N -step Markov measures on A
Z giving
nonzero probability to all elements of A
[0..N ].
5. H contains any measure absolutely continuous with respect to the aforementioned
Bernoulli or Markov measures. ✷

2.2. Linear Cellular Automata A cellular automaton (CA) is a continuous map F :
A
M−→A
M that commutes with all shift maps. The Curtis-Hedlund-Lyndon Theorem [4]
states that any CA is determined by a local map f : A
U−→A, where U ⊂ M is some ﬁnite
subset (a “neighbourhood of the identity”). F is an LCA if and only if f is a homomorphism
from the product group A
U into A.
The set End (A) of group endomorphisms from A to itself is a ring under composition
and pointwise addition: if f, g are in End (A), then so are f◦g and f+g. If Hom (
A
U; A
) is
the set of group homomorphisms from A
U into A, then there is a natural bijection between
(End (A))
U and Hom (
A
U; A
), as follows: For each u ∈ U, suppose that fu ∈ End (A).
Deﬁne f : A
U−→A by f[au|u∈U] = ∑

u∈U fu(au). Then f is a group homomorphism, and

every element of Hom (
A
U; A
) arises in this manner.
Thus, if F is an LCA, then there is some set of coeﬃcients {fu ; u ∈ U} so that, for any
a ∈ A
M, F(a) = b, where for all m ∈ M, bm = ∑

u∈U fu (
a(m.u)) = ∑

u∈U fu (σu(a)m).

For any u ∈ U, treat fu as an endomorphism on A
M by letting it act componentwise on
elements of A
M. Then ∀a ∈ A
M, F(a) = ∑

u∈U fu ◦ σu(a). Thus, F can be written as a

formal “polynomial of shift maps”:
 F = ∑

u∈U fu ◦ σu.

If A = Z/n (n ∈ N), then the elements of End (A) are all maps of the form f ([a]n) =
[f · a]n, where “[•]n” refers to a mod-n congruence class, and f ∈ Z/n is a constant,
with multiplication via the natural ring structure on Z/n. In this case, we can write

F = ∑

u∈U fu · σu, a polynomial with coeﬃcients in Z/n. For example, if M = Z and

F = σ−1 + 3 ◦ σ1 + 5σ2, then this means that F(a)k = [
a(k−1) + 3 · a(k+1) + 5 · a(k+2)]
n.

2.3. Diﬀusion If F : A
M −
←⊃ is an LCA and χ is a character of A
M, then χ ◦ F is also a
character. F is called diﬀusive† if, for every nontrivial χ ∈ ̂AM, there is some subset

† In [6], this was called diﬀusion in density. Since diﬀusion in density is the only kind we will encounter
in this paper, we have opted for more concise terminology.

Prepared using etds.cls

4 M. Pivato, R. Yassawi

Jχ ⊂ N of density 1 so that lim
j→∞
j∈Jχ rank [
χ ◦ Fj] = ∞. We will abbreviate this to

“rank [χ ◦ FN ]−−−−
dense
N →∞−→∞”.

Theorem 2. Let p be a prime number, and A = Z/p. Let D ≥ 1. Then any nontrivial

LCA on A(ZD) is diﬀusive. ✷

By nontrivial we mean that F, as a polynomial of shift maps, has more than one
nontrivial coeﬃcient. The signiﬁcance of diﬀusion and harmonic mixing is the following:

Theorem 3. Let A be a ﬁnite abelian group, and M a countable monoid. Suppose that
F : A
M −
←⊃ is an LCA, and that µ is a harmonically mixing measure on A
M.
If F is diﬀusive, then there is a set J ⊂ N of Ces`aro density 1 so that wk
∗−lim
j→∞
j∈J Fjµ = H.

Thus, wk
∗− lim
N →∞ 1
N
 N∑

n=1 Fnµ = H. ✷

For example, Fnµ weak*-converges to Haar measure in density whenever µ is one of the
aforementioned Bernoulli or N -step Markov measures.

3. Diﬀusion on other cyclic groups
Suppose n = pr1
1 · . . . prJ
J , where p1, . . . , pJ are distinct primes and r1, . . . , rJ ∈ N. Let

A = Z/n, and Aj = Z/qj , with qj = prj
j , for j ∈ [1..J]. Then A ∼=
 J⊕

j=1 Aj , and

thus, ̂A ∼=
 J⊕

j=1 ̂Aj . There is then a canonical identiﬁcation: A
M ∼=
 J⊕

j=1 A
M
j , and

thus, ̂AM ∼=
 J⊕

j=1
 ̂AM
j . Concretely: if χ ∈ ̂AM has coeﬃcient sequence [cm|m∈M]
, then,

χ ∼=
 J⊕

j=1 χ[j], where for each j ∈ [1..J], χ[j] ∈ ̂AM
j has coeﬃcient sequence [
c[j]
m |m∈M], with

c[j]
m = [cm]qj for all m ∈ M. Also,

End (A) ∼=
 J⊕

i,j=1 Hom (Ai, Aj ) (∗)
 J⊕

j=1 End (Aj) ∼=
 J⊕

j=1 Z/qj .

((∗) is because cross-terms are trivial). Concretely, if f ∈ N, and f : A −
←⊃ is the map
[a]n ↦→ [f ·a]n, then f = f
[1]⊕. . .⊕f
[J], where, for each j, f
[j] : Aj −
←⊃ is the map [a]qj ↦→ [fj·a]qj ,
and where f ≡ fj (mod p). In particular, if qj divides f , then f
[j] is trivial.
Thus, if F : A
M −
←⊃ is the LCA ∑

u∈U fu ◦ σu, with fu ∈ End (A), then, ∀u ∈ U, we can write

fu = f
[1]
u ⊕ . . . ⊕ f
[J]
u , with f
[j]
u ∈ End (Aj) a scalar-multiplication map determined by some

f [j]
u ∈ Z/qj , and then write F =
 J⊕

j=1 F[j], where, ∀j ∈ [1..J], F[j] : A
M
j −
←⊃ is the LCA given

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata II 5

by ∑

u∈U f [j]
u ◦ σu. Note also that, if χ =
 J⊕

j=1 χj ∈ ̂AM, then χ ◦ F =
 J⊕

j=1
 (χj ◦ F[j]).

Lemma 4. If F =
 J⊕

j=1 F[j] is an LCA on
 J⊕

j=1 A
M
j , then

( F is diﬀusive ) ⇐⇒ ( ∀j ∈ [1..J], F[j] is diﬀusive. )

Proof:

Proof of “⇐=”: Let χ ∈ ̂AM be nontrivial. Thus, χ = χ[1] ⊕ . . . ⊕ χ[J], where at least
one of χ[j] ∈ ̂AM
j , is nontrivial; suppose it is χ[j0]. Since F[j0] is diﬀusive , we conclude:

rank [
χ ◦ FN ] ≥ rank [
χ[j0] ◦ (
Fj0)N ]−−−−
dense
n→∞−→∞.

Proof of “=⇒”: Suppose that Fj0 is not diﬀusive. Let χj0 be some character on A
M
j0

so that rank [χj0 ◦ Fj0 ] −−−
∕
dense
n→∞−→ ∞, and let χ =
 J⊕

j=1 χj, where χj = 11 for all j ̸= j0. Then

rank [χ ◦ F] = rank [χj0 ◦ Fj0 ] −−−
∕
dense
n→∞−→ ∞, so F is not diﬀusive. ✷

Hence, we have reduced the proof of diﬀusion to the prime power case.
Suppose A = Z/8, and let F = Id + 2σ1 act on A
Z. Then F4·N = Id for all N ∈ N, so F
cannot be diﬀusive. This motivates the conditions of the following theorem.

Lemma 5. Let M = Z
D. Let A = Z/q, where q = pr, p is prime and r ∈ N. Let

F = ∑

u∈U fu ◦ σu.

If fu ∈ [0...q) are relatively prime to p for at least two u ∈ U, then F is diﬀusive .

Proof: Let χ ∈ ̂AM have coeﬃcient sequence [
cv|v∈V], where cv ∈ Z/q, for all v ∈ V,

with V ⊂ M some ﬁnite subset. Thus, χ[N ] = χ ◦ FN has coeﬃcient sequence [
c[N ]
m |m∈M]
,
where, for all m ∈ M,

c[N ]
m = ∑

v∈V
 ∑

u1,...,uN ∈U
v+u1+...+uN = m
 cv · fu1 · . . . · fuN (1)

Thus, rank [χ ◦ FN ] is the number of these coeﬃcients that are nonzero, mod q.

Case 1: One of the coeﬃcients {cv|v∈V} is nonzero, mod p.

Consider the character χ/p and the (nontrivial) LCA F/p on Z/pM induced by the

coeﬃcients [
cv|v∈V] and [fu|u∈U] respectively, and, for all N ∈ N, the character χ[N ]
/p
induced by [c[N ]
m |m∈M]
.

First, note that ∀N ∈ N, χ[N ]
/p = χ/p ◦ FN
/p (simply consider equation (1), only mod p
instead). Notice that, for any m and N , if the expression in (1) is nonzero mod p, then
it must be nonzero mod q. Thus rank [χ[N ]] ≥ rank [
χ[N ]
/p ] = rank [χ/p ◦ FN
/p]
. Hence, it

suﬃces to show that rank [
χ/p ◦ FN
/p]
−−−−
dense
N →∞−→∞.

Prepared using etds.cls

6 M. Pivato, R. Yassawi

But one of {cv|v∈V} is nonzero, mod p, so χ/p is nontrivial as a character on Z/pM. Thus,

by Theorem 2, rank [
χ/p ◦ FN
/p]
−−−−
dense
N →∞−→∞.

Case 2: All the coeﬃcients {cv|v∈V} are divisible by p.

Let ps be the greatest power of p that divides all elements of {cv|v∈V}; clearly s < r. Let
̃r = r − s and ̃q = p̃r, and let ̃A = Z/̃q. We will reduce the problem to consideration of
an LCA on Z/̃q, and then apply Case 1.

For all v ∈ V, let ̃cv = cv/ps, and let ̃χ ∈ ̂̃AM be the corresponding character. Let ̃F
be the LCA on ̃A
M having the same coeﬃcients as F; thus, ̃χ[N ] = ̃χ ◦ ̃FN has coeﬃcient
sequence [
̃c[N ]
m |m∈M]
, where, for all m ∈ M, ̃c[N ]
m = ∑

v∈V
 ∑

u1,...,uN ∈U
v+u1+...+uN = m
 ̃cv · fu1 · . . . · fuN .

Clearly, for all N ∈ N and m ∈ M, c[N ]
m = ps · ̃c[N ]
m , so if ̃c[N ]
m ̸≡ 0 (mod ̃q), then c[N ]
m ̸≡ 0
(mod q). Thus, rank [χ[N ]] ≥ rank [ ̃χ[N ]]. But by construction, at least one coeﬃcient of

̃χ is nonzero, mod p. Thus, by Case 1, we have: rank [ ̃χ ◦ ̃FN ]
−−−−
dense
N →∞−→∞. ✷

Theorem 6. Let n ∈ N, and A = Z/n. Let D ≥ 1, and let F : A(ZD) −
←⊃ be an LCA such
that, for each prime divisor p of n, at least two coeﬃcients of F are relatively prime to p.
Then F is diﬀusive.

Proof: Write n = pr1
1 · . . . prJ
J , A = A1 ⊕ . . . ⊕ AJ , F = F1 ⊕ . . . ⊕ FJ as before. By
Lemma 4, it suﬃces to show that each of F1, . . . , FJ is diﬀusive. By Lemma 5 and the
hypothesis, this is the case. ✷

4. Diﬀusion on ﬁnite abelian groups
Now suppose A is an arbitrary ﬁnite abelian group. Then A has a canonical decomposition:

A =
 K⊕

k=1
 Jk⊕

j=1 A(k,j), with A(k,j) = Z/q(k,j) ; q(k,j) = pr(k,j)
k , where p1, . . . , pK are distinct

primes with r(k,1), r(k,2), . . . , r(k,Jk) natural numbers for each k ∈ [1..K].
We will assume that A is of the special form where, for all k ∈ [1..K], rk,1 = . . . =

rk,Jk = rk. In other words, A =
 K⊕

k=1 Ak, with Ak = (
Z/qk )Jk , where p1, . . . , pK

are distinct primes, with qk = prk
k , and rk, Jk ∈ N. Thus, as before, End (A) =
K⊕

j,k=1 Hom (Aj, Ak) =
 K⊕

k=1 End (Ak), (cross-terms are trivial), and A
M ∼= A
M
1 ⊕. . .⊕A
M
K,

so we can write any LCA F : A
M −
←⊃ as a direct sum F = F1 ⊕ . . . ⊕ FK, where Fk : A
M
k −
←⊃.
By Lemma 4, to prove F is diﬀusive, it suﬃces to show that each of F1, . . . , FK is diﬀusive.
Hence, we will assume from now on that A = (
Z/q)J , where p is prime, q = pr, and J ∈ N.
Elements of A are thought of as J-tuples of Z/q-elements. A is a J-dimensional module
over the commutative ring† Z/q. The endomorphisms of A as an abelian group are just

† If r = 1 then q = p is prime, Z/q is a ﬁeld, and A is a Z/q-vector space. It may be helpful to keep this
case in mind in what follows.

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata II 7

the Z/q-linear endomorphisms of this Z/q-module, and are described by J × J matrices of
elements in Z/q.

Lemma 7. Let A = (
Z/q)J , where p is prime and q = pr.

1. Any χ ∈ ̂A is of the form: χ(a) = exp ( 2πi
q · ⟨c, a⟩), where c = (c1, . . . , cJ ) ∈ (Z/q)
J ,

and for any a = (a1, . . . , aJ ) ∈ (Z/q)
J , we deﬁne ⟨c, a⟩ = c1a1 + . . . + cJ aJ . Thus, χ
is nontrivial if and only if c ̸= 0.
2. If f ∈ End (A) has matrix F with adjoint †F, then χ ◦ f is the character a ↦→

exp ( 2πi
q · ⟨c
′, a⟩
), where c
′ = †F · c.

In particular, χ ◦ f is nontrivial if and only if c is not in ker[ †F].
3. Let f ∈ Aut (A). If χ ∈ ̂A is nontrivial then χ ◦ f is also nontrivial. ✷

Let V ⊂ M be a subset not containing 0. If G = ∑

m∈M gmσm is an LCA on A
M, then a

subset W ⊂ M is called V-separating for G if, for every w ∈ W, gw ∈ Aut (A), but for
all v ∈ V, g(w−v) = 0. Intuitively, W indexes a set of nontrivial (indeed, automorphic)
coeﬃcients of G, separated from one another by V-shaped “gaps”. If U = V ⊔ {0}, and
χ = ⊗

u∈U χu is a character, then we will show that these gaps ensure that (χ ◦ G)w is

nontrivial, for all w ∈ W. We will then construct V-separating sets for G = FN . This
argument was already used implicitly to prove Theorem 15 in [6].

Proposition 8. Let M = Z
D. An LCA F : A
M −
←⊃ is diﬀusive if, for every ﬁnite subset
V ⊂ M not containing zero, and every R ∈ N, there is a set J(V;R) ⊂ N of density 1 so that,
for all j ∈ J(V;R) there is a V-separating set Wj ⊂ M for Fj with card [Wj] > R.

Proof: Suppose F is not diﬀusive; thus, there is some character χ = ∏

u∈U χu so that

rank [
χ ◦ FN ] −−−
∕
dense
N →∞−→ ∞; hence, there is some subset B ⊂ N of nonzero upper density

and some bound R so that rank [χ ◦ FN ] < R for all N ∈ B.

Fix u0 ∈ U and let V = {u − u0 ; u ∈ U \ {u0}}; let J(V;R) be the set described by the
hypothesis. The set B ⊂ N has nonzero upper density, so B ∩ J(V;R) ̸= ∅; let j ∈ B ∩ J(V;R),
and let Wj ⊂ M be the V-separating set for Fj.

Write Fj = ∑

m∈M f
[j]
m σm, and then write χ ◦ Fj = ∏

m∈M χ[j]
m , where χ[j]
m =

∏

u∈U
 (χu ◦ f
[j]
m−u). Then ∀w ∈ Wj, χ[j]
(w+u0) = ∏

u∈U
 (
χu ◦ f
[j]
(w+u0−u)) = (χu0 ◦ f
[j]
w ) ·

∏

v∈V
 (
χ(v+u0) ◦ f
[j]
(w−v)) = (
χu0 ◦ f
[j]
w ) ·
 (∏

v∈V 11
)
 = (
χu0 ◦ f
[j]
w )
, which is nontrivial by

Lemma 7, because f
[j]
w is an automorphism. Thus, χ[j]
w ̸= 11 for all w ∈ W + u0, a set of
cardinality greater than R, contradicting the hypothesis that rank [χ ◦ Fj] < R. ✷

Applying Proposition 8 often involves tracking binomial coeﬃcients, mod p, via Lucas’
Theorem [6]. For a ﬁxed prime p, and any n ∈ N, let P(n) ∈ [0...p)
N be the p-ary expansion

Prepared using etds.cls

8 M. Pivato, R. Yassawi

of n (conventionally written with digits in reversed order). Thus, for example, if p = 3, then
P(34) = . . . 0000001021.
If n, N ∈ N, with P(n) = [
n[i]|∞
i=0] and P(N ) = [N [i]|∞
i=0] then we write “n ≪ N ” if
n[i] ≤ N [i] for all i ∈ N. Lucas’ Theorem then implies:
( [ N
n
 ]
p ̸= 0
 )
 ⇐⇒ ( n ≪ N )

A commuting automorphism linear cellular automaton is an LCA of the form
F = ∑

u∈U fu ◦ σu, where {fu|u∈U} ⊂ Aut (A) is a commuting collection of automorphisms of

A. For example:

• {fu|u∈U } are simultaneously diagonalizable automorphisms. In other words, there is
some Z/q-basis B = {b1, . . . , bJ } for A, so that the elements of B are eigenvectors for
every element of {fu|u∈U}, and all eigenvalues are relatively prime to p.

• There is some f ∈ Aut (A) so that ∀u ∈ U, fu = f
nu for some nu ∈ Z.

Theorem 9. If G : A(ZD) −
←⊃ is a commuting automorphism LCA with two or more
nontrivial coeﬃcients, then G is diﬀusive.

Proof: We will use Proposition 8; the argument is basically identical to the proof of
Theorem 15 in [6], so we will only sketch it here.

Suppose G = g0σn0 + g1σn1 + . . . + gU σnU , where g0, g1, . . . , gU ∈ Aut (G) commute,
and where n0, n1, . . . , nU ∈ Z
D. We can rewrite: G = g0 ◦ (F ◦ σn0) , where:

F = Id + f1σm1 (Id + f2σm2 [ . . . (Id + fU−1σmU −1 [Id + fU σmU ]) . . .]) ,

and, for all u ∈ [1..U ], mu = nu − nu−1, and fu = g−1
u−1 ◦ gu. We can do this because
g0, g1, . . . , gU are automorphisms, and thus, invertible. It suﬃces to show that F is
diﬀusive.

Let J ∈ N. The coeﬃcients of F commute, so we can employ the Binomial Theorem —and
thus, Lucas’ Theorem —to compute the coeﬃcients of FJ , mod p.

Let L
U (J) = {[k1, k2, . . . , kU ] ∈ NU ; kU ≪ kU−1 ≪ . . . k2 ≪ k1 ≪ J}
.

Then FJ = ∑

n∈ZD f
[J]
n ◦ σn, where f
[J]
n = ∑

k∈LU (J)
(k1 m1+...+kU mU )=n
 f
[J]
(k), and, for any k =

[k1, k2, . . . , kU ] ∈ NU , we deﬁne

f
[J]
(k) := [ J
k1
 ]
p
[ k1
k2
 ]
p . . . [ kU−1
kU
 ]
pf
k1
1 ◦ f
k2
2 ◦ . . . ◦ f
kU
U .

(See [6] for details.)

Fix a ﬁnite subset V ⊂ Z
D not containing 0, and let R > 0; we want to build a V-
separating set for FJ of cardinality R. To do this, note that there is some Γ ∈ N such
that, if J ∈ N and P(J) contains at least R “gaps” of size at least Γ (ie. sequences of
Γ successive zeros, delimited by nonzero entries), then we can construct a set WJ ⊂ Z
D

with card [WJ ] ≥ R, so that:

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata II 9

1. For every w ∈ WJ , there is a unique k ∈ L
U (J) so that (k1m1 + . . . + kU mU ) = w;
thus f
[J]
w = f
[J]
(k) ∈ Aut (A).
2. For all v ∈ V, there are no k ∈ L
U (J) with (k1m1 + . . . + kU mU ) = w − v; thus
f
[J]
(w−v) = 0.

Thus, WJ is V-separating for FJ . By Birkhoﬀ’s Ergodic Theorem, the set J(Γ;R) of J ∈ N
with R such Γ-gaps is a set of Ces`aro density one. Thus, we satisfy the conditions of
Proposition 8. ✷

To apply Proposition 8 it is clearly suﬃcient to construct sets J(V;R) for some increasing
sequence of numbers R1, R2, . . . →∞, along with a sequence V1, V2, . . . so that, for any ﬁnite
V ⊂ M we have V ⊂ Vk + m for some m ∈ M and k ∈ N. Also, it suﬃces to prove that the
LCA FK is diﬀusive for some power K > 0: for any χ ∈ ̂AM, and any k ∈ [0...K), χ ◦ Fk is
also a character; if FK is diﬀusive, then rank [
χ ◦ Fk ◦ Fn·K]−−−−
dense
n→∞−→∞ for every k ∈ [0...K),
which in turn implies that rank [χ ◦ Fn]−−−−
dense
n→∞−→∞.

j : . . . ∗ 1 0 ∗ . . . ∗ 1 0 ∗ . . . ∗ 0 q 1 ∗ . . . ∗ ∗ ∗ . . . ∗ ∗ ∗
w : . . . 0 0 0 0 . . . 0 0 1 0 . . . 0 0 1 0 0 . . . 0 0 0 . . . 0 0 0
v : . . . 0 0 0 0 . . . 0 0 0 0 . . . 0 0 0 0 0 . . . 0 0 ∗ . . . ∗ ∗ ∗
j + w : . . . ∗ 1 0 ∗ . . . ∗ 1 1 ∗ . . . ∗ 1 0 1 ∗ . . . ∗ ∗ ∗ . . . ∗ ∗ ∗
j + w − 1 : . . . ∗ 1 0 ∗ . . . ∗ 1 1 ∗ . . . ∗ 1 0 ∗ ∗ . . . ∗ ∗ ∗ . . . ∗ ∗ ∗
j + w − v : . . . ∗ 1 0 ∗ . . . ∗ 1 1 ∗ . . . ∗ 1 0 ∗ ∗ . . . ∗ ∗ ∗ . . . ∗ ∗ ∗
j + w − v − 1 : . . . ∗ 1 0 ∗ . . . ∗ 1 1 ∗ . . . ∗ 1 0 ∗ ∗ . . . ∗ ∗ ∗ . . . ∗ ∗ ∗
2w : . . . 0 0 0 0 . . . 0 1 0 0 . . . 0 1 0 0 0 . . . 0 0 0 . . . 0 0 0
2v : . . . 0 0 0 0 . . . 0 0 0 0 . . . 0 0 0 0 0 . . . 0 ∗ ∗ . . . ∗ ∗ ∗
2w − 2v : . . . 0 0 0 0 . . . 0 1 0 0 . . . 0 0 q q q . . . q ∗ ∗ . . . ∗ ∗ ∗
2w − 2v − 1 : . . . 0 0 0 0 . . . 0 1 0 0 . . . 0 0 q q q . . . q ∗ ∗ . . . ∗ ∗ ∗
↑ ↑ ↑ ↑ ↑ ↑ ↑
Digit # . . . . . . i2 . . . . . . . . . i1 . . . . . . . . . i0 . . . . . . . . . Lv . . . 2 1 0

Figure 1. The p-ary expansions of j, w, v, etc. Here, “∗” represents any digit in in [0...q].

Proposition 8 can be applied even when the coeﬃcients of F do not commute. For
example:

Example 10: Let A = (
Z/p)2, and let F : A
Z −
←⊃ have local map f : A
{0,1}−→A given:

f ([ x0
y0
 ] , [ x1
y1
 ]) = (y0, x0 + y1) = [ 0 1
1 0
 ] · [ x0
y0
 ] + [ 0 0
0 1
 ] · [ x1
y1
 ]

This invertible LCA was studied in [1], where it was shown to take fully supported Markov
measures to Haar measure in the weak* Ces`aro limit. Proposition 3.1 of [1] can be
reformulated as:

FN =
 N∑

m=0 f
[N ]
m σm, where f
[N ]
m =
 [ ϕ
(N −2)
m ϕ
(N −1)
m
ϕ
(N −1)
m ϕ
(N )
m
 ]

,

with ϕ
(N )
m =
 { [ ( N +m
2 )
m ]
p if m ≡ N (mod 2)

0 if m ̸≡ N (mod 2) .

Prepared using etds.cls

10 M. Pivato, R. Yassawi

Thus, if m ≡ (N − 1) (mod 2), then the matrix f
[N ]
m is antidiagonal, and an automorphism

iﬀ ϕ
(N −1)
m = [ ( N −1+m
2 )
m ]

p ̸= 0, which, by Lucas’ Theorem, occurs only when m ≪ N −1+m
2 .

If m ≡ N ≡ (N − 2) (mod 2), then matrix f
[N ]
m is diagonal, and an automorphism iﬀ
m ≪ N +m
2 and m ≪ N −2+m
2 .

As noted earlier, it suﬃces to prove that F2 is diﬀusive. So, ﬁx V = (0 . . . 2V ] ⊂ Z and
R > 0; we will ﬁnd a set J(V;R) and, for all j ∈ J(V;R) some Wj ⊂ Z with card [Wj] > R, so

that 2Wj is V-separating for F2j. In other words, ∀w ∈ Wj, f
[2j]
2w ∈ Aut (A), but ∀v ∈ V,
f
[2j]
(2w−v) = 0. This is equivalent to:

∀w ∈ Wj, ϕ
(2j)
2w ̸= 0 ̸= ϕ
(2j−2)
2w , but for all even v = 2u ∈ V, ϕ
(2j)
(2w−v) = 0 = ϕ
(2j−2)
(2w−v), and

for all odd v = 2u + 1 ∈ V, ϕ
(2j−1)
(2w−v) = 0. This, in turn, is equivalent to:

For all w ∈ Wj, 2w ≪ j + w and 2w ≪ j + w − 1, (2)

but for all u ∈ (0 . . . V ],

2w − 2u ̸≪ j + w − u, 2w − 2u ̸≪ j + w − u − 1,

and 2w − 2u − 1 ̸≪ j + w − u − 1. (3)

So, let q = p − 1, LV = ⌈logp(V )⌉ + 1 and LR = ⌈log2(R)⌉, and let J(V;R) be the set of
all j ∈ N such that P(j) contains the word “0q1” somewhere after the ﬁrst LV digits, and
contains at least LR separate instances of the word “10” after the “0q1”. By Birkhoﬀ’s
Ergodic Theorem, J(V;R) ⊂ N has density 1.

Suppose j ∈ J(V;R); and suppose that “0q1” occurs at position i0 > Lv, while “10” occurs
at positions i(LR) > . . . > i2 > i1. Let w to be a number so that P(w) contains the
word “010” at i0, and contains either “01” or “00” at each of i1, i2, . . . , i(LR), with zeros
everywhere else. Clearly, we can construct 2LR > R distinct numbers w of this kind; let
Wj be the set of all such numbers.

For example, if w has “01” at i1 and “00” at i2, and v ∈ [0...V ], then the p-ary expansions
of the relevant numbers are depicted in Figure 1. By inspection, one can see that equations
(2) and (3) are satisﬁed. Clearly, this will be true for any choice of w ∈ Wj and v ∈ V.

5. Harmonic Mixing of Markov Random Fields
Notation: Suppose a = A
M, with a = [
am|m∈M]. If V ⊂ M, then a|V = [av|v∈V] ∈ A
V.

This determines a continuous map prV : A
M ∋ a ↦→ a|V ∈ A
V; if µ ∈ M [
A
M]
, then
let prV∗ (µ) be the V-marginal projection of µ (so that, for any U ⊂ A
V, prV∗(µ) [U] =
µ [
U × A
M\V]).

If b ∈ A
V, then ⟨b⟩ = {
a ∈ A
M ; a|V = b} is the associated cylinder set, and, if

µ ∈ M [
A
M]
, then µ[b] is the measure of this cylinder set. If W ⊂ M is disjoint from V,
and c ∈ A
W, then b c ∈ A
V⊔W is deﬁned so that (b c) |V = b and (b c) |W = c; thus,
⟨b c⟩ = ⟨b⟩ ∩ ⟨c⟩.
Let B(V) be the sigma-subalgebra of A
M generated by coordinates in V; if φ ∈
L
1 (
A
M, µ)
, let EV [φ] ∈ L
1 (
A
V, µ) be the conditional expectation of φ given B(V),
which we regard as a function on A
V. If b ∈ A
V, then the conditional probability

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata II 11

measure of µ, given b, is the unique measure µb ∈ M [
A
M] such that ⟨φ, µb⟩ = EV [φ] (b)
for every φ ∈ L
1 (
A
M, µ)
. The map A
V ∋ b ↦→ µb ∈ M [A
M] is measurable, and, if
µV = prV∗(µ) is the marginal projection of µ onto A
V, then µ has the disintegration

[10, 3]: µ = ∫

AV µb dµV[b]. Note that prV(µb) = δb, the point mass at b. If W ⊂ M \ V

and c ∈ A
W, we will sometimes write µb[c] as “µ [c // b]”, or, if a ∈ A
M is a µ-random

conﬁguration, as “µ
 [ a|W = c

a|V = b
 ]
”

5.1. Markov Processes Let (X, X ) be a measurable space, and let µ ∈ M [
X
Z] be
a probability measure. Let U = [0...U ) ⊂ Z. If n ∈ Z and x ∈ X
(U+n), then
⟨x⟩ = {
y ∈ X
Z ; y∣
∣(U+n) = x
}, and µx is the conditional probability measure of µ, given
x. µ is the path distribution of a (X-valued, U -step, nonstationary) Markov process if,
for any n ∈ Z and x ∈ X
(U+n), events occuring after time n + U are independent of those
occuring before time n, relative to µx: for any Vp ⊂ (−∞...n), Vf ⊂ [U + n...∞), and
yp ∈ X
Vp and yf ∈ X
Vf , we have µx [yp yf ] = µx [yp] · µx [yf ].
Any U -step Markov process is entirely described by its (U + 1)-dimensional marginals
µ[n...U+n] = pr[n...U+n]∗[µ] for all n ∈ Z, which are called the (U -step) transition
probabilities of µ. If X is ﬁnite, then M [X; R] ∼= RX; if U = 1, then the transition
probabilities {µ{n,n+1}}

n∈Z can be encoded by a sequence of transition probability
matrices {
Q(n) ∈ RX×X ; n ∈ Z
} and state distributions {
ηn ∈ RX ; n ∈ Z
} so that,
for any n ∈ Z, η(n+1) = Q(n) · ηn, and, for any xn, x(n+1) ∈ X, µ{n,n+1} [xn, x(n+1)] =

Q(n)
(x(n+1); xn) · ηn (xn).

If µ[n...U+n] = µ[0...U] for all n ∈ Z, then µ is stationary. If X is ﬁnite and U = 1, this
means there is some Q ∈ RX×X and η ∈ M [X] (with Q · η = η) so that Q(n) = Q and
ηn = η for all n ∈ Z. We call η the stationary state distribution.
If M ⊂ M [X
[0...n]] is a ﬁnite family of transition probabilities, we say µ is M-
semistationary if µ[n...U+n] ∈ M for all n ∈ Z. When X is ﬁnite and U = 1, this
means that there are some ﬁnite families Q and H of transition probability matrices and
state distributions, respectively, for µ so that, for any η ∈ H and Q ∈ Q, Q · η ∈ H; we say
Q-semistationary.
If µ is M-semistationary, then µ has full support if every element of M has full support
on X
[0...U]; as a consequence, µ assigns nonzero probability to every ﬁnite cylinder set. If
X is ﬁnite and U = 1, this means that every entry of every transition probability matrix in
Q is nonzero.
If µ ∈ M [
X
Z] is a Markov process, u, w ∈ X, and n ∈ Z, then the sandwich measure

nµw
u ∈ M [X] is deﬁned so that, if x = [xn|n∈Z] is a µ-random sequence, then for any

V ⊂ X, nµw
u (V) = µ [ xn+1 ∈ V
(xn = u)&(xn+2 = w)
 ].

5.2. Exponential Harmonic Mixing If A is a ﬁnite abelian group, and µ ∈ M [
A
M; C], we
will say µ is exponentially harmonically mixing with decay parameter λ > 0 (or “λ-
EHM”) if, for all χ ∈ ̂AM with rank [χ] ≥ R, we have |⟨χ, µ⟩| < e−λ·R. It is straightforward

Prepared using etds.cls

12 M. Pivato, R. Yassawi

to verify the following

Lemma 11. Suppose (X, ρ) is a probability space, and X ∋ x ↦→ νx ∈ M [
A
M; C] is a
measurable function so that νx is λ-EHM for all x ∈ X. If φ : X−→C is measurable and

∥φ∥∞ = 1, then ∫

X φ(x) · νx dρ [x] is also λ-EHM. ✷

If µ is a stationary, fully supported U -step Markov measure on A
Z, then µ is harmonically
mixing ( Part 4 of Proposition 1 in this paper, or Corollary 10 of [6]). The same method
easily generalizes to show:

Proposition 12. Suppose A is a ﬁnite abelian group, and that M ⊂ M [
A
[0...n]] is a ﬁnite
family of fully supported transition probabilities.
1. There is a constant λ > 0 determined by M, so that, if µ is any M-semistationary
Markov process on A
Z, then µ is λ-EHM.
2. In particular, if µ is a 1-step Q-semistationary Markov process with full support, then

−λ = 1
2 · sup

ξ,χ∈ ̂A
χ̸=11 sup
Q,P∈Q log ∥
∥ξ• · †Q · χ• · †P
∥
∥∞, where ξ• is the diagonal matrix

with elements of ξ along the diagonal (so that, for any φ ∈ CA, ξ•φ is the result of
multiplying ξ and φ componentwise), and where ∥•∥∞ is the uniform operator norm.

Proof: (Sketch) Proposition 8 in [6] showed that a stationary 1-step Markov matrix was
harmonically mixing; in fact, the proof showed that |⟨χ, µ⟩| < e−λR for all χ ∈ ̂AZ with
rank [χ] = R, where

− λ := 1
2 · sup

ξ,χ∈ ̂A
χ̸=11 log ∥
∥ξ• · †Q · χ• · †Q∥
∥
∞. The same argument works for a semistationary

1-step process; this yields Part 2.

The proof of Corollary 10 in [6] showed how any fully supported U -step process could
be “recoded” as a fully supported 1-step process; harmonic mixing of the latter implied
harmonic mixing of the former. Corollary 10 thus followed from Proposition 8. By an
identical argument Part 1 follows from Part 2. ✷

5.3. Markov Random Fields Let U ⊂ M be a ﬁnite “neighbourhood of 0” (e.g. M = Z
D

and U = [−1...1]
D). For any subset V ⊂ M, let cl(V) := V + U, and let ∂(V) := cl(V) \ V
(see Figure 2(A)).
µ ∈ M [
A
M] is a (nonstationary) Markov random ﬁeld [2, 9] with interaction
range U (or “U-MRF”) if, for any W ⊂ M, and any a ∈ A
∂(W), events occuring “inside”
W are independent of those occuring “outside”, relative to the conditional measure µa. In
other words, for any Vin ⊂ W, Vout ⊂ M \ cl(W), and bin ∈ A
Vin , bout ∈ A
Vout , we have:
µa [bin bout] = µa [bin] · µa [bout].
For example, if M = Z, then the U -step Markov processes on A
M are exactly the Markov
random ﬁelds with interaction range U = (−U...U ).
µ is stationary if it is invariant under translation by M. In this case, µ(U+m) = µU for
every m ∈ M, and µU = prU∗(µ) is called the local interaction for µ.

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata II 13

????????????????k
k-1

k+1
k+2
k+3
 c

(B)

0
 V
V

U (A)
 M {k}

Figure 2. (A) U, V, and ∂V. (B) A sandwich measure.
 VU

U M

M

Ζ

1
−1
 V
 k

k

k
k-1

k+1
k+2
k+3

Figure 3. ̃M = M × Z and ̃U = U × {−1, 0, 1}; ̃Vk and ∂ ̃Vk.

If I ⊂ M [
A
U] is ﬁnite, then µ is I-semistationary if µ(U+m) ∈ I for every m ∈ M. I is
called the set of local interactions. We say µ has full support if all elements of I have
full support on A
U.

Lamination Processes: Suppose ̃U ⊂ ̃M = M × Z and µ ∈ M [
A ̃M] is a ̃U-MRF. By a

suitable recoding, we can assume ̃U = U × {−1, 0, 1} for some U ⊂ M. We can then realize
µ via an A
M-valued, 1-step Markov process, called the lamination process. Intuitively,
we imagine this Markov process as constructing a µ-random conﬁguration in A ̃M by laying
down successive random “M-layers”, with each M-layer conditional on the previous one.
To see that this is a Markov process on A
M, ﬁx k, and let ̃Vk = M × (−∞...k) (the
“past”). Then ∂(̃Vk) = M × {k} (the “present”) and ̃M \ cl(̃Vk) = M × (k...∞) (the
“future”); the Markov ﬁeld condition of µ implies that events in the past are independent
of those in the future, given complete information about the present (see Figure 3). The
original ﬁeld measure µ ∈ M [
A
M×Z] is also the path distribution (as a measure on (
A
M)Z)

Prepared using etds.cls

14 M. Pivato, R. Yassawi

for the lamination process.

Sandwich Measures: Again assume ̃M = M×Z and ̃U = U×{−1, 0, 1}. If a ∈ A
M×{k−1}

and c ∈ A
M×{k+1} (see Figure 2(B)), then the sandwich measure determined by a and
c is the sandwich measure (k−1) µc
a ∈ M [
A
M] of the lamination process; since k is implicit
in the deﬁnition of a and c, we will suppress it, and denote the sandwich measure as “µc
a”.
In other words, µc
a is the conditional measure µa c, projected onto A
M×{k}. The following
is easy to verify:

Lemma 13. 1. µc
a is a Markov random ﬁeld on A
M, with interaction range U.
2. If ̃I ⊂ M [
ÃU] and µ is ̃I-semistationary, then there is some ﬁnite I ⊂ M [
A
U] so
that all sandwich measures of µ are I-semistationary.
3. If µ has full support, then so does every sandwich measure of µ. ✷

The harmonic mixing of an MRF depends on the the harmonic mixing of its sandwich
measures:

Proposition 14. If A is a ﬁnite abelian group, and µ is a semistationary MRF on A
M×Z

and all sandwich measures of µ are λ-EHM, then µ is λ
′-EHM, where λ
′ = λ/2.

Proof: See §5.5. ✷

From this follows our main result:

Theorem 15. Suppose A is a ﬁnite abelian group, U ⊂ Z
D, and let ̃I ⊂ M [A
U] be a ﬁnite
set of local interactions with full support. Then ∃λ > 0 so that if µ is any ̃I-semistationary
MRF on A
ZD , then µ is λ-EHM.

Proof: (by induction on D) If D = 1, this is just Proposition 12.

Suppose inductively that the claim is true for MRFs on Z
D−1, and let µ ∈ A
ZD . By
Lemma 13, all sandwich measures of µ are I-semistationary MRFs on A
ZD−1 , where I
is some ﬁnite set of local interactions with full support. Thus, by induction hypothesis,
all these sandwich measures are λ-EHM for some λ > 0. Thus, by Proposition 14, µ is
λ
′-EHM, with λ
′ = −λ/2. ✷

5.4. Markov Operators When X is ﬁnite, a 1-step X-valued Markov process can be deﬁned
by a series of with transition probability matrices {Q(n)}n∈Z. These matrices deﬁne linear
operators on the space M [X; R] ∼= RX, so that, if ηn ∈ M [X] is the state distribution at
time n, then Q(n) · ηn = ηn+1 is the state distribution at time n + 1.
When X is an arbitrary measurable space (with sigma-algebra X ), transition probabilities
are described by linear operators on the vector space M [X; R] (which, for technical reasons,
we will treat as linear operators on M [X; C]).

Idea: Informally speaking, a Markov operator is linear operator Q : M [X; C] −
←⊃
mapping the set M [X] of probability measures into itself. Suppose (y0, y1) ∈ X
{0,1}

is a random couple, and Q is the transition probability operator from time 0 to time

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata II 15

1. If x ∈ X, and δx ∈ M [X] is the point mass at x, then the probability measure
qx := Q(δx) is the conditional state distribution of y1 given that y0 = x: for all U ⊂ X,

qx[U] = Prob [ y1 ∈ U
y0 = x
 ]. When X is ﬁnite, measures on X are vectors and Q is a matrix,

and qx is just the xth column of this matrix.

Suppose y0, y1 have distributions η0, η1 ∈ M [X] respectively, with η1 = Q(η0). If
φ : X−→C is a measurable function, then the expected value of φ(y1) is given by
⟨φ, η1⟩ = ⟨φ, Q(η0)⟩ = 〈 †Q(φ), η0〉, where †Q is the adjoint of Q.

For any measurable U ⊂ X, let †q
U := †Q (11U ). Thus, for any x ∈ X, †q
U (x) =

†Q (11U ) (x) = 〈 †Q (11U ) , δx〉 = ⟨11U , Q(δx)⟩ = ⟨11U , qx⟩ = qx[U]. When X is ﬁnite and
Q is a matrix and U = {u} is a singleton set, then †q
U is just the uth row of Q (or the
uth column of †Q).

We need to develop some technology to make these ideas well-deﬁned.

Formalism: If Φ : X−→C is measurable, then let ∥Φ∥∞ = sup
x∈X |Φ(x)|, and consider the

Banach space M∞(X, X ) = {Φ : X−→C ; Φ measurable,
∥Φ∥∞ < ∞} and its unit ball, B1 = {Φ ∈ M∞ ; ∥Φ∥∞ ≤ 1}. Now, M [X; C] embeds into
the dual space M∗
∞ in a natural way; endow it with the appropriate weak* topology. The
following results are straightforward:

Lemma 16. The simple functions of the form Φ = ∑n φn11Un are dense in M∞ (where
φn ∈ C and Un ⊂ X are measurable).
The weak* topology on M [X; C] is determined by convergence on measurable sets. Thus,
a sequence {µn}∞
n=1 converges to µ ∈ M [X; C] if and only if µn[U]−−−−
n→∞−→µ[U] for all
measurable U ⊂ X. ✷

If a function X ∋ x ↦→ µx ∈ M [X; C] is measurable relative to the weak* Borel algebra
of M [X; C], and ν is some other measure on X, then µ = ∫

X µx dν[x] is the measure so
that, for all U ⊂ X, µ[U] = ∫

X µx[U] dν[x]; by Lemma 16, this well-deﬁnes the action of µ
on M∞.
If Q : M [X; C] −
←⊃, then deﬁne ∥Q∥ := sup
x∈X ∥qx∥var (note: this is not the operator norm

of Q). Say that Q is smooth if Q is linear, measurable relative to the weak* Borel sigma
algebra, and ∥Q∥ < ∞.

Lemma 17. (a) If Q is smooth, then its adjoint †Q : M∞ −
←⊃ is a well-deﬁned, bounded
linear operator, and ∥
∥ †Q∥
∥
∞ ≤ ∥Q∥.

(b) If X ∋ x ↦→ qx ∈ M [X; C] is a measurable function and M = sup
x∈X ∥qx∥var < ∞,

then the function Q : M [X; C] −
←⊃ deﬁned: Q(µ) = ∫

X qx dµ[x] is smooth and
continuous, and ∥Q∥ = M .

Proof of (a): For any φ ∈ M∞, and any x ∈ X, deﬁne ( †Qφ)(x) = ⟨φ, qx⟩. Then
†Q(φ) is measurable (the function X ∋ x ↦→ δx ∈ M [X; C] is measurable; hence, so is the
function (x ↦→ qx); thus, so is †Q(φ)). Also, ∥
∥ †Q(φ)
∥
∥∞ ≤ ∥φ∥∞ · sup
x∈X ∥qx∥var.

Prepared using etds.cls

16 M. Pivato, R. Yassawi

Proof of (b): Clearly, Q is well-deﬁned and linear, and ∥Q∥ = M . To see
that Q is continuous, let U ⊂ X; then Q(µ)[U] = ∫
X qx[U] dµ[x]. The function
X ∋ x ↦→ qx[U] ∈ C is measurable; thus, if µn−−−−
n→∞−→µ in the weak* topology, then
Q(µn)[U] = ∫

X qx[U] dµn[x] −−−−
n→∞−→ ∫
X qx[U] dµ[x] = Q(µ)[U]. ✷

We deﬁne a Markov operator to be a smooth linear operator on M [X; C] that maps
M [X] into itself. By Lemma 17, it suﬃces to deﬁne a measurable collection (x ↦→ qx) of
transition probability measures. We will be concerned with the following case:

Example 18: Suppose ̃M = M × Z and µ ∈ M [
A ̃M] is an MRF and consider the
lamination process; we claim the transition probabilities are determined by a sequence
{Q(n)}n∈Z of Markov operators.

Let Mk := M×{k} for k = n or n+1. If c ∈ A ̃M is a µ-random conﬁguration, then for each
a ∈ A
M, q
(n)
a is the conditional distribution of c| M(n+1) given that c|Mn = a. Formally,

if µa ∈ M [
A
M] is the conditional distribution given a, then q
(n)
a = prM(n+1) ∗ (µa). The

map A
M ∋ a ↦→ q
(n)
a ∈ M [
A
M] is measurable because the map A
Mn ∋ a ↦→ µa ∈ M [
A
M]

is measurable [10], while prM(n+1) : M [
A
M]
−→M [
A
M(n+1) ] is continuous.

If χ ∈ M∞, then let χ• : M∞ −
←⊃ be the bounded linear operator induced by
multiplication with χ: for any φ ∈ M∞ and x ∈ X, (χ•φ) (x) = χ(x) · φ(x). To establish
that Markov processes on A
Z were EHM (Proposition 12), we bounded the norm of operators
of the form ξ• ◦ Q ◦ χ• ◦ P, where ξ, χ ∈ ̂AM. We will employ a similar strategy to show
that MRFs are EHM; this will require the following result:

Lemma 19. Let Q, P : M [X] −
←⊃ be Markov operators. For any φ ∈ M∞, deﬁne
µφ
x ∈ M [X; C] by: dµφ
x = †P(φ) · dqx.

(a) For any χ ∈ M∞, ∥
∥ †Q ◦ χ• ◦ †P
∥
∥
∞ = sup
φ∈B1 sup
x∈X
 ∣
∣〈
χ, µφ
x〉∣
∣.

(b) Suppose that µ ∈ M [
X
Z] is a Markov process and Q and P are the transition
probability operators at time 0 and 1, respectively. For any u, w ∈ X, let µu =
P ◦ Q(δu) be the conditional probability measure on X at time 2 induced by state
u ∈ X at time 0, and let µw
u be the sandwich measure on X induced by u ∈ X at time

0 and w ∈ X at time 2. Then for any Φ ∈ M∞, µΦ
u = ∫

X Φ(w) · µw
u dµu [w].

Proof of (a): For any φ ∈ B1 and x ∈ X, †Q◦χ•◦ †P(φ)(x) = 〈 †Q ◦ χ• ◦ †P(φ), δx〉 =〈
χ• ◦ †P(φ), Q(δx)
〉 = 〈
χ · †P(φ), qx〉 = 〈
χ, µφ
x〉. Thus,
∥
∥ †Q ◦ χ• ◦ †P
∥
∥∞ = sup
φ∈B1
 ∥
∥ †Q ◦ χ• ◦ †P(φ)
∥
∥∞ = sup
φ∈B1 sup
x∈X
 ∣
∣ †Q ◦ χ• ◦ †P(φ)(x)
∣
∣

= sup
φ∈B1 sup
x∈X
 ∣
∣
〈χ, µφ
x〉∣
∣ .

Proof of (b): We want to show that for any V ⊂ X,

µΦ
u (V) = ∫

X Φ(w) · µw
u (V) dµu [w] .

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata II 17

First, suppose that W ⊂ X and Φ = 11W. Let µW
x := µ11W
x ; thus, dµW
x = †pW dqx.
Then:

µW
u (V) = ∫

V dµW
u [v] = ∫

V
 †pW (v) dqu [v] = ∫

V pv [W] dqu [v]

= ∫

V µ [ x2 ∈ W
x1 = v
 ] dqu [v] (a)
 ∫

V µ [ x2 ∈ W
(x1 = v)&(x0 = u)
 ] dqu [v]

(b)
 ∫

W µw
u (V) dµu[w] = ∫

X 11W(w) · µw
u (V) dµu[w].

(a) follows from the Markov property. To see (b), let Xk be the sigma-subalgebra
of X
Z generated by coordinate xk, and let Ek [•] (resp. Ek,j [•]) be the conditional
expectation with respect to Xk (resp. Xk ∨ Xj). Let W2 = {
x ∈ X
Z ; x2 ∈ W} and
V1 = {x ∈ X
Z ; x1 ∈ V}. Then
∫

V µ [ x2 ∈ W
(x1 = v)&(x0 = u)
 ] dqu [v] = ∫

V E0,1 [11W2] (u, v) dqu [v]

= ∫

X 11V · E0,1 [11W2 ] (u, v) dqu [v] = E0 [11V1 · E0,1 [11W2]] (u)

= E0 [
E0,1 [11V1 · 11W2 ]] (u) = E0 [11V1 · 11W2 ] (u)

= E0 [
E0,2 [11V1 · 11W2 ]] (u) = E0 [
11W2 · E0,2 [11V1]] (u)

= ∫

W µ [ x1 ∈ V
(x2 = w)&(x0 = u)
 ] dµu [w] = ∫

W µw
u (V) dµu[w].

Next, if Φ = ∑

n φn11Wn is a simple function, then †P(Φ) = ∑

n φn †pWn, so that

dµΦ
x = †P(Φ) · dqx = ∑

n φn †pWn dqx = ∑

n φn dµWn
x . Thus,

µΦ
x (V) = ∫

V dµΦ
x = ∑

n φn · ∫

V dµWn
x = ∑

n φn · µWn
x [V]

= ∑

n φn · ∫

X 11Wn (w)µw
u (V) dµu [w] = ∫

X
 (
∑

n φn11Wn (w)

)
 · µw
u (V) dµu [w]

= ∫

X Φ(w) · µw
u (V) dµu [w] , as desired.

Finally, if {Φn}∞
n=1 is a bounded sequence of simple functions so that Φn−−−−n→∞−→Φ in M∞,
then †P(Φn)−−−−n→∞−→ †P(Φ) in M∞, so that µΦn
x −−−−n→∞−→µΦ
x in the weak* topology on M [X].
But by dominated convergence, we also know that

µΦn
x (V) = ∫

X Φn(w) · µw
u (V) dµu [w] −−−−n→∞−→ ∫

X Φ(w) · µw
u (V) dµu [w] ;

hence, µΦ
x (V) = ∫
X Φ(w) · µw
u (V) dµu [w], for all V ⊂ X, as desired. ✷

Prepared using etds.cls

18 M. Pivato, R. Yassawi

5.5. Uniform Harmonic Mixing Now, let X = A
M, and consider a 1-step Markov process
on A
M determined by a sequence of Markov operators {
Q(n) ; n ∈ Z
}. For every n ∈ Z,
a ∈ A
M and φ ∈ M∞, deﬁne nµφ
a ∈ M [A
M; C] so that d nµφ
a = †Q(n+1)(φ) dq
(n)
a as in
Lemma 19.
If λ > 0 then the sequence {
Q(n) ; n ∈ Z
} is uniformly harmonically mixing with
decay parameter λ (or “λ-UHM”) if, for every a ∈ A
M and measurable φ ∈ B1,
and every n ∈ Z, the measure nµφ
a is λ-EHM. Thus, applying Lemma 19(a), we have:∥
∥
∥ †Q(n+1) ◦ χ• ◦ †Q(n)∥
∥
∥
∞ ≤ e−λ·R for any χ ∈ ̂AM with rank [χ] ≥ R.

Proposition 20. Let ̃U = U×{−1, 0, 1} and µ ∈ M [
A
M×Z] be a ̃U-MRF such that ∀n ∈ Z,
a ∈ A
M×{n}, and c ∈ A
M×{n+2}, the sandwich measure µc
a is λ-EHM. Then {
Q(n) ; n ∈ Z
}

is λ-UHM.

Proof: Let φ ∈ B1. By Lemma 19(b), nµφ
a = ∫

AM φ(c) · µc
a dµa [c], where

µa = Q(n+1) ◦ Q(n)(δa). By hypothesis, µc
a is λ-EHM for all c ∈ A
M; apply Lemma 11
to conclude that nµφ
a is also λ-EHM. ✷

Proposition 21. Let µ ∈ M [
A
M×Z] be a the path distribution of a Markov process
determined by Markov operators {
Q(n) ; n ∈ Z
}.
If {
Q(n) ; n ∈ Z
} is λ-UHM, then µ is λ
′-HM, where λ
′ = λ/2.

Proof: Let χ ∈ ̂AM×Z with rank [χ] = 2R, and suppose that χ =
 2K⊗

k=0 χ(k), where,

for all k ∈ [0..2K], χ(k) is a character on A
M×{nk}, with rank [
χ(k)] = Rk, for some
n0 < n1 < . . . < n2K. For any k ∈ [1..2K], deﬁne †Qk = †Q(nk) ◦ †Q(nk−1) ◦ . . . ◦
†Q(n(k−1)+2) ◦ †Q(n(k−1)+1).

If {ηn ; n ∈ Z} ⊂ M [
A
M] are the state distributions of the process, then it is not hard
to show:

⟨χ, µ⟩ = 〈 †Q(n(2K)+1) ◦ χ(2K)
• ◦ †Q2K ◦ χ(2K−1)
• ◦ †Q(2K−1) ◦ · · · ◦ †Q2 ◦ χ(1) ◦ †Q1 (χ(0)) ,

η(n(2K)+1)
〉 ,

(see e.g. Claim 1 of Proposition 8 in [6]). Thus,

|⟨χ, µ⟩|

≤

(1)
 ∥
∥
∥ †Q(n(2K)+1) ◦ χ(2K)
• ◦ †Q2K ◦ χ(2K−1)
• ◦ . . . ◦ †Q2 ◦ χ(1) ◦ †Q1 (χ(0))∥
∥
∥
∞

≤

(2)
 ∥
∥
∥ †Q(n(2K)+1) ◦ χ(2K)
• ◦ †Q2K ◦ χ(2K−1)
• ◦ . . . ◦ †Q2 ◦ χ(1) ◦ †Q1∥
∥
∥
∞

≤

(3)
 ∥
∥
∥ †Q(n(2K)+1) ◦ χ(2K)
• ◦ †Q2K∥
∥
∥
∞ ·
 K−1∏

k=1
 ∥
∥
∥ †Q(2k+1) ◦ χ(2k)
• ◦ †Q2k∥
∥
∥
∞ ·
 K−1∏

k=0
 ∥
∥
∥χ(2k+1)
• ∥
∥
∥∞

≤

(4)
 K∏

k=1
 ∥
∥
∥ †Q(n(2k)+1) ◦ χ(2k)
• ◦ †Q(n(2k))∥
∥
∥∞

≤

(5)
 K∏

k=1 exp [−λ · R2k] = exp
 [ K∑

k=1 −λ · R2k
]
 = exp
 [

−λ ·
 K∑

k=1 R2k
]

Prepared using etds.cls
 Limit Measures for Aﬃne Cellular Automata II 19

(1) Because η(n(2K)+1) is a probability measure. (2) Because ∥
∥χ(0)∥
∥
∞ = 1.

(3) Separating out χ(k)
• for all odd k.

(4) Dropping χ(k)
• for all odd k, and †Q(n(2k)−1), †Q(n(2k)−2), . . . , †Q(n(2k−1)+2) for every
k (because ∥
∥ †Q(n)∥
∥ ≤ 1 for every n ∈ Z).

(5) By UHM hypothesis and Lemma 19(a). By the same logic, |⟨χ, µ⟩| ≤

exp
 [

−λ ·
 K∑

k=1 R(2k−1)
]

.

Now, clearly, one of
 ( K∑

k=1 R2k
)
 and
 ( K∑

k=1 R(2k−1)
)
 must equal or exceed R, since

together, they sum to rank [χ] = 2R. Thus either −λ ·
 K∑

k=1 R2k ≤ −λ · R or

−λ ·
 K∑

k=1 R(2k−1) ≤ −λ · R. Hence |⟨χ, µ⟩| ≤ −λ · R. ✷

Proof of Proposition 14: If µ is a MRF and all sandwich measures of µ are λ-EHM,
then, by Proposition 20, the sequence {
Q(n) ; n ∈ Z
} is λ-UHM. Then, by Proposition
21, µ is λ
′-HM, where λ
′ = λ/2. ✷

6. Conclusion
We have demonstrated that a broad class of probability measures on A
M weak*-converge to
Haar measure in density, when acted on by a wide class of LCA. Many interesting questions
remain. For example, can we establish harmonic mixing for Markov random ﬁelds without
full support, such as those supported on subshifts of ﬁnite type? What about measures on
soﬁc shifts? How can we characterize either diﬀusion or harmonic mixing when M is not
a lattice, but instead, a nonabelian group or monoid? Finally, what happens when A is
a nonabelian group? The natural analogy of LCA for nonabelian A are “multiplicative”
cellular automata [8], where the local map is computed by (noncommutatively) multiplying
the values of neighbouring coordinates. What is the asymptotic behaviour of measures
under such automata?
 References

[1] Alejandro Maass and Servet Mart´inez. Time averages for some classes of expansive one-dimensional
cellular automata. In Eric Goles and Servet Martinez, editors, Cellular Automata and Complex
Systems, pages 37–54. Kluwer Academic Publishers, Dordrecht, 1999.
[2] Pierre Br´emaud. Markov Chains: Gibbs ﬁelds, Monte Carlo Simulation, and Queues. Springer-
Verlag, 1999.
[3] H. Furstenberg. Ergodic Theory and Combinatorial Number Theory. Princeton University Press,
Princeton, New Jersey, 1981.
[4] G. Hedlund. Endomorphisms and automorphisms of the shift dynamical systems. Mathematical
System Theory, 3:320–375, 1969.
[5] Douglas Lind. Applications of ergodic theory and soﬁc systems to cellular automata. Physica D,
10:36–44, 1984.

Prepared using etds.cls

20 M. Pivato, R. Yassawi

[6] Marcus Pivato and Reem Yassawi. Limit measures for aﬃne cellular automata. Ergodic Theory &
Dynamical Systems, 22(4):1269–1287, August 2002.
[7] Servet Mart´inez Pablo Ferrari, Alejandro Maass and Peter Ney. Ces`aro mean distribution of group
automata starting from measures with summable decay. Ergodic Theory and Dynamical Systems,
20(6):1657–1670, 2000.
[8] Marcus Pivato. Multiplicative cellular automata on nilpotent groups: Structure, entropy, and
asymptotics. Journal of Statistical Physics, 110(1/2):247–267, January 2003.
[9] Ross Kindermann and J. Laurie Snell. Markov Random Fields and their Applications. American
Mathematical Society, Providence, Rhode Island, 1980.
[10] Laurent Schwartz. Lectures on disintegration of measures. Tata Institute of Fundamental Research,
Bombay, 1975.

Prepared using etds.cls

????????????????k
k-1

k+1
k+2
k+3
 c M
a {k}
