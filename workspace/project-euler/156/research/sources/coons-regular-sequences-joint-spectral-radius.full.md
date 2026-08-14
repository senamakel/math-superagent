<!-- source: https://arxiv.org/pdf/1511.07535 | converted from PDF -->

arXiv:1511.07535v1  [math.CO]  24 Nov 2015
REGULAR SEQUENCES AND THE JOINT SPECTRAL RADIUS

MICHAEL COONS

Abstract. We classify the growth of a k-regular sequence based on informa-
tion from its k-kernel. In order to provide such a classiﬁcation, we introduce
the notion of a growth exponent for k-regular sequences and show that this
exponent is equal to the joint spectral radius of any set of a special class of
matrices determined by the k-kernel.

1. Introduction

Let K be a ﬁeld of characteristic zero. The k-kernel of f : Z⩾0 → K is the set

Kerk(f ) := {
{f (kℓn + r)}n⩾0 : ℓ ⩾ 0, 0 ⩽ r < kℓ} .

The sequence f is called k-automatic provided the set Kerk(f ) is ﬁnite [6]. In
1992, as a generalisation of automatic sequences, Allouche and Shallit [1] intro-
duced the notion of regular sequences. By their deﬁnition, a sequence f taking
values in K is called k-regular, for an integer k ⩾ 1, provided the K-vector space
⟨Kerk(f )⟩K spanned by Kerk(f ) is ﬁnite dimensional. Connecting regular sequences
to ﬁnite sets of matrices, Allouche and Shallit [1, Lemma 4.1] showed that a K-
valued sequence f is k-regular if and only if there exist a positive integer d, a ﬁnite
set of matrices Af = {A0, . . . , Ak−1} ⊆ Kd×d, and vectors v, w ∈ Kd such that
f (n) = wT Ai0 · · · Ais v, where (n)k = is · · · i0 is the base-k expansion of n. More-
over, their proof showed that all such collections of matrices can be described (or
constructed) by considering spanning sets of ⟨Kerk(f )⟩K.
In their seminal paper, Allouche and Shallit [1, Theorem 2.10] proved that given
a k-regular sequence f , there is a positive constant cf such that f (n) = O(ncf ).
In this paper, we determine the optimal value of the constant cf . To state our
result, we require a few deﬁnitions. Let k ⩾ 1 be an integer and f : Z⩾0 → K be
a (not eventually zero) k-regular sequence. We deﬁne the growth exponent of f ,
denoted GrExp(f ), by
 GrExp(f ) := lim sup
n→∞
f (n)̸=0
 log |f (n)|
log n .

The joint spectral radius of a ﬁnite set of matrices A = {A0, A1, . . . , Ak−1}, denoted
ρ(A), is deﬁned as the real number

ρ(A) = lim sup
n→∞ max
0⩽i0,i1,...,in−1⩽k−1
 ∥
∥Ai0 Ai1 · · · Ain−1∥
∥
1/n ,

where ∥ · ∥ is any (submultiplicative) matrix norm. This quantity was introduced
by Rota and Strang [8] and has a wide range of applications. For an extensive
treatment, see Jungers’s monograph [7].

Theorem 1. Let k ⩾ 1 and d ⩾ 1 be integers and f : Z⩾0 → K be a (not eventually
zero) k-regular sequence. If Af is any collection of k integer matrices associated to
a basis of the K-vector space ⟨Kerk(f )⟩K, then

logk ρ(Af ) = GrExp(f ),

where logk denotes the base-k logarithm.

Date: February 1, 2018.
The research of M. Coons was supported by ARC grant DE140100223.

1

2 MICHAEL COONS

We note that Theorem 1 holds for K replaced by any N¨otherian ring R, where
Af is any collection of k matrices associated to an R-module basis of the R-module
spanned by Kerk(f ), where this R-module is viewed as an R-submodule of the set
of a sequences with entries in R. In particular, the result holds for the ring Z.

Remark 2. In engineering circles, for certain choices of A related to a set D
of forbidden sign patterns, the quantity log2 ρ(A) is sometimes referred to as the
capacity of the set D, denoted cap(D). See Jungers, Blondel, and Protasov [4,
Section II] for details.

2. The growth exponent of a regular sequence

In this section, all matrices are assumed to have entries in K and all regular
sequences are supposed to not eventually be zero.

Lemma 3. Let k ⩾ 1 be an integer and A = {A0, A1, . . . , Ak−1} be a ﬁnite set of
matrices. Given ε > 0 then there is a submultiplicative matrix norm ∥ · ∥ such that
∥Ai∥ < ρ(A) + ε for each i ∈ {0, 1, . . . , k − 1}.

Lemma 3 can be found in Blondel et al. [5, Proposition 4], though it was ﬁrst
given in the original paper of Rota and Strang [8].

Proposition 4. Let k ⩾ 2 be an integer and f : Z⩾0 → K be a k-regular function.
For any ε > 0, there is a constant c = c(ε) > 0 such that for all n ⩾ 1,

|f (n)|
nlogk(ρ(Af )+ε) ⩽ c,

where Af is the set any set of matrices associated to a spanning set of ⟨Kerk(f )⟩K.

Proof. Let ε > 0 be given and let ∥ · ∥ be a matrix norm such that the conclusion
of Lemma 3 holds. Then

|f (n)| ⩽ ∥v∥ · ∥w∥ ·
 s∏

j=0 ∥Aij ∥ ⩽ ∥v∥ · ∥w∥ · (ρ(A) + ε)
s,

where the base-k expansion of n is is · · · i0. Using the bound s ⩽ logk n with some
rearrangement gives the result. □

Lemma 5. Let k ⩾ 1 be an integer and A = {A0, A1, . . . , Ak−1} be a ﬁnite set of
matrices. If ε > 0 is a real number, then there is a positive integer m and a matrix
Ai0 · · · Aim−1 , such that

(ρ(A) − ε)
m < ρ(Ai0 · · · Aim−1 ) < (ρ(A) + ε)
m.

Proof. This is a direct consequence of the deﬁnition of the joint spectral radius. □

Now let k ⩾ 2 be an integer, and suppose that f : Z⩾0 → K is an un-
bounded k-regular sequence. Given a word w = is · · · i0 ∈ {0, . . . , k − 1}∗, we
let [w]k denote the natural number such that (n)k = w. Let {{f (n)}n⩾0 =
{g1(n)}n⩾0, . . . , {gd(n)}n⩾0} be a basis for the K-vector space ⟨Kerk(f )⟩K. Then
for each i ∈ {0, 1, . . . , k − 1}, the sequences {g1(kn + i)}n⩾0, . . . , {gd(kn + i)}n⩾0
can be expressed as K-linear combinations of {g1(n)}n⩾0, . . . , {gd(n)}n⩾0 and hence
there is a set of d × d matrices Af = {A0, . . . , Ak−1} with entries in K such that

Ai[g1(n), . . . , gd(n)]T = [g1(kn + i), . . . , gd(kn + i)]
T

for i = 0, . . . , k − 1 and all n ⩾ 0. In particular, if is · · · i0 is the base-k expansion
of n, then Ai0 · · · Ais [g1(0), . . . , gd(0)]T = [g1(n), . . . , gd(n)]T . (We note that this
holds even if we pad the base-k expansion of n with zeros at the beginning.) We
call such a set of matrices Af , constructed in this way, a set of matrices associated
to a basis of ⟨Kerk(f )⟩K.

REGULAR SEQUENCES AND THE JOINT SPECTRAL RADIUS 3

This construction allows us to provide a lower bound analogue of Proposition 4.

Proposition 6. Let k ⩾ 2 be an integer and f : Z⩾0 → K be a k-regular function.
For any ε > 0, there is a constant c = c(ε) > 0 such that for inﬁnitely many n ⩾ 1,

|f (n)|
nlogk(ρ(Af )−ε) ⩾ c,

where Af is any set of matrices associated to a basis of ⟨Kerk(f )⟩K.

Proof. Let ε > 0 be given. Then by Lemma 5 there is a positive integer m and a
matrix A = Ai0 · · · Aim−1 such that ρ(A) > (ρ(Af ) − ε)
m. Let λ be an eigenvalue
of A with |λ| = ρ(A). Then there is an eigenvector y such that Ay = λy. Pick a
vector x such that x
T y = c1 ̸= 0. Then
∣
∣x
T A
ny∣
∣ = |c1| · |λ|n = |c1| · ρ(A)
n > |c1| · (ρ(Af ) − ε)
nm .

Using a method developed by Bell, Coons, and Hare [3], it follows (see Appendix
A for details) that there are words u1, . . . , ud, v1, . . . , vt from {0, 1, . . . , k − 1}∗ and
a positive constant c2 such that for each n ⩾ 0 there is an element from

{|f ([ui(im−1 · · · i0)
nvj]k)| : i = 1, . . . , d, j = 1, . . . , t} ,

which is at least c2(ρ(Af ) − ε)
nm. Here, as previously, we have used the notation
[w]k to be the integer n such that (n)k = w.
If M = max{|ui|, |vj| : i = 1, . . . , d, j = 1, . . . , t}, then

N = [ui(im−1 · · · i0)
nvj]k < k2M+nm,

so that logk(N ) − 2M < nm. Thus, by the ﬁnding of the previous paragraph, there
are inﬁnitely many N such that

|f (N )|
N logk(ρ(Af )−ε) = |f (N )|
(ρ(Af ) − ε)logk N > c2
(ρ(Af ) − ε)2M ,

which is the desired result. □

Proof of Theorem 1. For a given ε > 0, Proposition 4 implies that

lim
n→∞ |f (n)|
nlogk(ρ(Af )+2ε) = 0,

and Proposition 6 implies that

lim sup
n→∞ |f (n)|
nlogk(ρ(Af )−2ε) = ∞.

Taken together these give

logk(ρ(Af ) − 2ε) ⩽ GrExp(f ) ⩽ logk(ρ(Af ) + 2ε).

Since ε can be taken arbitrarily small, this proves the theorem. □

We end this section by highlighting one major diﬀerence between Proposition 4
and Proposition 6. Proposition 4 is true for Af related to any spanning set of the
K-vector space ⟨Kerk(f )⟩K, while Proposition 6 requires Af to be associated to a
basis of ⟨Kerk(f )⟩K. In fact, these two propositions give the following corollary.

Corollary 7. Let k ⩾ 2 be an integer and f : Z⩾0 → K be a k-regular function. If
Bf is any set of matrices associated to f and Af is any set of matrices associated
to a basis of ⟨Kerk(f )⟩K, then ρ(Af ) ⩽ ρ(Bf ).

4 MICHAEL COONS

Equality in the conclusion of the above corollary would be desirable, but un-
fortunately, this is not (in general) the case. To see this, consider the 2-regular
function f , where, for (n)2 = is · · · i0, we have f (n) = wT Ai0 · · · Ais v, with

Af = {A0, A1} = {(
1 0
0 1
)} , wT = [1 0], and v = [1 1]T .

Then also for any number x > 1, we have f (n) = x
T Bi0 · · · Bis y, with

Bf = {B0, B1} =
 





1 0 0
0 1 0
0 0 x







 , x
T = [1 0 0], and y = [1 1 0]T ,

and ρ(Af ) = 1 < x = ρ(Bf ).

Appendix A.

For a given ε > 0, we had by Lemma 5 that there is a positive integer m and a
matrix A = Ai0 · · · Aim−1 such that ρ(A) > (ρ(Af ) − ε)
m. Choosing an eigenvalue
λ of A with |λ| = ρ(A), we found vectors x and y such that x
T y = c1 ̸= 0 and

(1) ∣
∣x
T A
ny∣
∣ = |c1| · |λ|n = |c1| · ρ(A)
n > |c1| · (ρ(Af ) − ε)
nm .

In this appendix, we follow an argument of Bell, Coons, and Hare [3, p. 198]
to provide the existence of words u1, . . . , ud, v1, . . . , vt from {0, 1, . . . , k − 1}∗ such
that for each n ⩾ 0 there is an element from

{|f ([ui(im−1 · · · i0)
nvj]k)| : i = 1, . . . , d, j = 1, . . . , t} ,

which is at least c2(ρ(Af ) − ε)
nm.
To this end, let k ⩾ 2 be an integer, suppose that f : Z⩾0 → K is an unbounded
k-regular sequence, and Af = {A0, . . . , Ak−1} be a set of matrices associated to a
basis {{f (n)}n⩾0 = {g1(n)}n⩾0, . . . , {gd(n)}n⩾0} of the K-vector space ⟨Kerk(f )⟩K.
We claim that the K-span of the vectors [g1(i), . . . , gd(i)], as i ranges over all
natural numbers, must span all of Kd. If this were not the case, then their span
would be a proper subspace of Kd and hence the span would have a non-trivial
orthogonal complement. In particular, there would exist c1, . . . , cd ∈ K, not all
zero, such that c1g1(n) + · · · + cdgd(n) = 0

for every n, contradicting the fact that g1(n), . . . , gd(n) are K-linearly independent
sequences.
Let ⟨Af ⟩ denote the semigroup generated by the elements of Af . We have just
shown that there exist words X1, . . . , Xd in ⟨Af ⟩ such that

[g1(0), . . . , gd(0)]X1, . . . , [g1(0), . . . , gd(0)]Xd

span Kd.
Now consider x
T A
ny as described in the ﬁrst paragraph of this appendix. By
construction, we may write x
T = ∑j αj [g1(0), . . . , gd(0)]Xj for some complex num-
bers αj. Then
 x
T A
n = ∑

j αj[g1(0), . . . , gd(0)]XjA
n.

Let uj be the word in {0, 1, . . . , k − 1}∗ corresponding to Xj and let y = is · · · i0
be the word in {0, . . . , k − 1}∗ corresponding to A; that is y = is · · · i0 where
A = Ais · · · Ai0 and similarly for uj. Then we have

[g1(0), . . . , gd(0)]XjA
n = [g1([ujyn]k), . . . , gd([ujyn]k)]T .

REGULAR SEQUENCES AND THE JOINT SPECTRAL RADIUS 5

Write yT = [β1, . . . , βd]. Then

x
T A
ny = ∑

i,j αiβjgj([uiyn]k).

By assumption, each of {g1(n)}n⩾0, . . . , {gd(n)}n⩾0 is in the K-vector space gen-
erated by Kerk(f ), and hence there exist natural numbers p1, . . . , pt and q1, . . . , qt
with 0 ⩽ qm < kpm for m = 1, . . . , t such that each of for s = 1, . . . , d, we have
gs(n) = ∑t
i=1 γi,sf (kpin + qi) for some constants γi,s ∈ K. Then

x
T A
ny = ∑

i,j,ℓ αiβjγℓ,jf ([uiynvℓ]k),

where vℓ is the unique word in {0, 1, . . . , k − 1}∗ of length pℓ such that [vℓ]k = qℓ.
Let K = ∑i,j,ℓ |αi| · |βj| · |γℓ,j|. Then since |x
T A
ny| ⩾ |c1| · (ρ(Af ) − ε)
nm for all
n, some element from
{
|f ([uiynvj]k)| : i = 1, . . . , d, j = 1, . . . , t}}

is at least (|c1|/K) · (ρ(Af ) − ε)
nm for each n.

Acknowledgements. We thank Bj¨orn R¨uﬀer for several useful conversations.

References

1. Jean-Paul Allouche and Jeﬀrey Shallit, The ring of k-regular sequences, Theoret. Comput. Sci.
98 (1992), no. 2, 163–197. MR 1166363 (94c:11021)
2. Jason P. Bell, Michael Coons, and Kevin G. Hare, Growth degree classiﬁcation for ﬁnitely
generated semigroups of integer matrices, Semigroup Forum, to appear.
3. , The minimal growth of a k-regular sequence, Bull. Aust. Math. Soc. 90 (2014), no. 2,
195–203. MR 3252000
4. Vincent D. Blondel, Rapha¨el Jungers, and Vladimir Protasov, On the complexity of computing
the capacity of codes that avoid forbidden diﬀerence patterns, IEEE Trans. Inform. Theory 52
(2006), no. 11, 5122–5127. MR 2300380 (2007m:94086)
5. Vincent D. Blondel, Yurii Nesterov, and Jacques Theys, On the accuracy of the ellipsoid
norm approximation of the joint spectral radius, Linear Algebra Appl. 394 (2005), 91–107.
MR 2100578 (2005i:15043)
6. Alan Cobham, Uniform tag sequences, Math. Systems Theory 6 (1972), 164–192. MR 0457011
(56 #15230)
7. Rapha¨el Jungers, The joint spectral radius, Lecture Notes in Control and Information Sciences,
vol. 385, Springer-Verlag, Berlin, 2009, Theory and applications. MR 2507938 (2011c:15001)
8. Gian-Carlo Rota and Gilbert Strang, A note on the joint spectral radius, Nederl. Akad. Weten-
sch. Proc. Ser. A 63 = Indag. Math. 22 (1960), 379–381. MR 0147922 (26 #5434)

School of Math. and Phys. Sciences, University of Newcastle, Callaghan, Australia
E-mail address: Michael.Coons@newcastle.edu.au
