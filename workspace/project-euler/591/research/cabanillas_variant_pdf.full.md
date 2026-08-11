<!-- source: https://arxiv.org/pdf/1904.01874 | converted from PDF -->

arXiv:1904.01874v2  [math.NT]  12 Sep 2019
A variant of Ostrowski numeration

Emmanuel Cabanillas

ABSTRACT :

In this article, we propose a variant of the usual Ostrowski α-numeration ( where α is a real in
[0, 1[) that codes integers ( positive as well as negative) and reals of [0, 1[ ( instead of [−α, 1−α[),
so that for every integer n, n and {nα} have the same coding sequence. These coding sequences
respect natural lexicographic orders and will be used to prove well known results on order prop-
erties of Kronecker sequences ({nα − β})n.

Contents

1 Introduction 2
1.1 overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 continued fraction expansions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 semi-convergents and best rationals . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2 A numeration system 7
2.1 Ostrowski’s numeration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 α-numeration for a rational α . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.3 α-numeration for an irrational α . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.4 α-numeration of negative integers . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

3 Complements 22
3.1 dynamic generating α-numeration . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.2 α-germs and orbits of α-rotation . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.3 shift and inductive structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

4 Order properties of Kronecker sequences 28
4.1 a one-page proof of the ”three distance theorem” . . . . . . . . . . . . . . . . . . 28
4.2 order coincidence of ({nα})n and ({nα′})n . . . . . . . . . . . . . . . . . . . . . . 30
4.3 best left or right α-approximation of a real in [0, 1[ . . . . . . . . . . . . . . . . . 32
4.4 measure of repartition of ({kα})0⩽k<ν . . . . . . . . . . . . . . . . . . . . . . . . 34

5 References 37

1

1 Introduction

1.1 overview

Ostrowski’s numeration system is based on convergents (qn)n∈N of a real α ∈ [0, 1[ and code,
with a sequence of digits non negative integers as well as reals in [−α, 1 − α[ ( see [6] for the
original article and [1] for a survey). Deﬁnitions are mentioned in 2.1
In 2.2 and 2.3, we propose a variant of this system : it is still based on (qn)n, but the ”
markovian condition” is changed and we will be able to code any integer n and any real {nα}
with the same ﬁnite sequence ( {x} denotes the fractional part of a real x). We study separately
the cases α irrational and α rational. This last case could appear uninteresting, but it is useful
for applications to numerical semigroups for example ( see [3]).
In 3, we give some dynamical aspects of this α-numeration.
In 4, we use it to explore some order properties of Kronecker sequences ({nα + β})n, as the
famous ” three distance theorem”. These sequences have been widely studied with various points
of view and we refer to [1] for an exhaustive bibliography.

1.2 notations

All along this paper, we will denote : Z the set of integers, N∗ the set of positive integers and
N the set of non negative integers.
For all reals x, ⌊x⌋ denotes its ﬂoor ,⌈x⌉ its ceiling and {x} its fractional part.
For a sequence d = (dk)k∈N∗, we use the following notations for slices of d : for all integers r, s
such that 0 < r ⩽ s :
 d[r,s] = (dr, dr+1, · · · , ds) ; d[r,∞] = (dr, dr+1, · · · )

We will also use concatenation of sequences and intuitive notations as (3, 5, 04, 1, 6, 0∞) to de-
note (3, 5, 0, 0, 0, 0, 1, 6, 0, 0, 0, · · · ). Moreover, if (ak)k∈N∗ is a sequence of positive integers and
if we restrict ourself to sequences in ∏k{0 · · · ak}, then max at the index k will denote ak : for
example, (max, 1, 0, max, 3, · · · , ) means (a1, 1, 0, a4, 3, ...). So, the notation maxr or (max, 0)r,
where r ∈ N ∪ {∞} will often be used. For example : (02, max3, 04, (max, 0)∞) denotes the
sequence (0, 0, a3, a4, a5, 0, 0, 0, 0, a10, 0, a12, 0, a14, 0, · · · ).

For α-numeration, we will often use two lexicographic orders on sequences of RN∗ :
◮ the reversed lexicographic order ( RLO) denoted ⩽
R :

d ⩽
R d
′ ⇔ d = d
′ or ∃j ∈ N∗,
 {dj < d′
j
∀i > j, di = d′
i

◮ the alternate lexicographic order ( ALO) denoted ⩽
A :

d ⩽
A d
′ ⇔ d = d
′ or ∃j ∈ N∗,
 {(−1)j−1dj < (−1)j−1d′
j
∀i ∈ {1 · · · j − 1}, di = d′
i

ALO is a total order on RN∗, but RLO is only a partial order on RN∗. Now, RLO is a total
order on on R(N∗), the set of real sequences that ends with 0∞.
We will also use ALO with a shift on indices for continued fraction expansions in 1.3 ( named
CFE in this paper).
 2

1.3 continued fraction expansions

All results given in this subsection are well known and we just want to underline some nota-
tions and simple facts.

• Every irrational θ can be uniquely represented by its continued fraction expansion ( CFE) and
we will write θ = [t0, t1, · · · ] = [tk]k∈N, such that tk ∈ N∗ for all k ∈ N∗ and t0 ∈ Z. θ is the limit
of the ” convergents” ([t0, t1, · · · , tn])n, a sequence of rationals deﬁned inductively by :

∀x ∈ R, ∀x1, · · · , xn ∈ R∗
+, [x] = x ; [x, x1, · · · , xn] = x + 1
[x1, · · · , xn] (1)

We will denote, for all integer n, pn
qn ( or pn(θ)
qn(θ) if necessary) the reduced fraction that represents
[t0, t1, · · · , tn].
In addition, if we deﬁne ϕ :
 ϕ :
 {
Z × (N∗)N∗ → R\Q
(tk)k∈N → [tk]k∈N

this map is bijective and increasing, with the Alternate Lexicographic Order ( ALO) on Z ×
(N∗)N deﬁned by :

(tk)k∈N ⩽A (t′
k)k∈N ⇔ (∀k ∈ N, tk = t′
k) or ∃j ∈ N,
 {
∀k ∈ {0 · · · j − 1}, tk = t′
k
(−1)jtj < (−1)jt′
j

We also have an expression for the inverse function of ϕ :

ϕ
−1 :
 {
R\Q → Z × (N∗)N∗

θ → (tk)k∈N, with t0 = ⌊θ⌋; ∀k ∈ N∗, tk = AT k−1({θ})

where T is the Gauss map : ]0, 1[→ [0, 1[, x → {1/x} and A : x → ⌊1/x⌋. We know that
T k(α) ̸= 0 for all k ∈ N if and only if α is irrational in ]0, 1[.

• The case of rationals seems easier, since these one are represented by ﬁnite CFE, namely the
convergents of irrationals. But, we would like to associate to them inﬁnite CFE, in order to
extend ϕ to an increasing map with ALO.
We introduce an ∞ number : N∗ will denote N∗ ∪ {∞}, with the usual extension of the order
( ∀n ∈ N∗, n < ∞) and of the operations ( ∀n ∈ N, n + ∞ = ∞ and 1/∞ = 0). Then, we can
end CFE of rationals with an inﬁnite sequence of ∞. With those conventions, the former map
ϕ extends to an increasing and bijective map ˜ϕ from a subset E of Z × (N∗)N∗ to R. Then, ˜ϕ−1

is given by the same expressions, if we extend T and A to [0, 1[, with T (0) = 0 and A(0) = ∞.
We can precise E : it is the set of sequences (tk)k such that t0 ∈ Z and tk ∈ N∗ for k ∈ N∗,
such that tk = ∞ ⇒ (tk+1 = ∞ and ( tk−1 ̸= 1 or k = 1)). So to say : if the sequence contains
∞, the last ” ﬁnite digit” in the CFE is greater or equal to 2. We will prefer an alternative
way : we will end CFE of rationals with [1, ∞∞], where ∞∞ denotes an inﬁnite sequence of ∞.
Then, we extend naturally the ALO to sequences of CFE, described by :

C = {(tk) ∈ Z × N∗ × (N∗)
N, ∀k ⩾ 2, (tk = ∞ ⇒ (tk+1 = ∞ and tk−1 ∈ {∞, 1})}

The extension of ϕ to an increasing and bijective map ϕ1 from C to R is quite natural, but its
inverse function will use more complicated maps T1 and A1 :

3

We consider the map I : u → ⌈u⌉ − 1 and A1, T1 both deﬁned on [0, 1] by :

A1 :
 



0 → ∞
1 → 1
x → I(1/x) if x ̸= 0, 1
 ; T1 :
 



0 → 0
1 → 0
x → 1 if 1/x ∈ N\{0, 1}
x → {1/x} else

We can now express the inverse function of ϕ1 :

ϕ
−1
1 :
 {
R → C
θ → (tk)k∈N, with t0 = I(θ); ∀k ∈ N∗, tk = A1T k−1
1 (θ − I(θ))

For convenience, we abreviate CFE of rationals and omit ∞∞, the inﬁnite ” ∞” ending se-
quence. So, 9/4 = [2, 3, 1] and ∀n ∈ Z, n = [n − 1, 1].

N.B : all along this paper, CFE of a real ( so for any rational) α will denote ϕ
−1
1 (α),
but the notation [t0, t1, · · · , tk] will be more general ( see (1)).

1.4 semi-convergents and best rationals

• Let α be a real with CFE [ak]k∈N and (pk/qk)k its convergents sequence, such that pk/qk =
[a0, · · · , ak], for all k such that ak < ∞ ( see beginning of this section).
A semi-convergent of α is any rational of the form mpk+pk−1
mqk+qk−1 , with m ∈ {0 · · · ak} and k ∈ N
such that ak < ∞ ( we take m > 0 if k = 0 to avoid 1/0 !). So, convergents are particular
semi-convergents.

Lemma 1 Let α be a real with CFE [ak]k∈N. Semi-convergents of α are exactly the rationals
with CFE [a0, · · · , as−1, bs, 1], such that s ∈ N, bs ∈ {1 · · · as} and as+1 < ∞.

Proof :
Consequence of the deﬁnition and the well known fact : ∀m ∈ N, [a0, · · · , as−1, m] = mps−1+ps−2
mqs−1+qs−2 . ■

• Let α be a rational and [a0, a1, a2, · · · , ar, 1] its CFE. ( we denote ar+1 = 1)
We have the following induction formula :

p−2 = 0 ; p−1 = 1 ; ∀n ∈ {0 · · · r + 1} , pn = anpn−1 + pn−2

q−2 = 1 ; q−1 = 0 ; ∀n ∈ {0 · · · r + 1} , qn = anqn−1 + qn−2

We have α = pr+pr−1
qr+qr−1 = pr+1
qr+1 .

Let α′ = [a′
0, a′
1, · · · , a′
r′, 1] be an other rational with r′ ⩾ r. With obvious notations, we see
that , for n ∈ {0 · · · r} :

(∀k ∈ {0 · · · n}, ak ⩽ a′
k) ⇒ (∀k ∈ {0 · · · n}, pk ⩽ p′
k and qk ⩽ q′
k)

In addition, for j, n integers such that 1 ⩽ j ⩽ n ⩽ r :

(aj < a
′
j and ∀k ∈ {1 · · · j − 1}, ak ⩽ a′
k) ⇒ qj < q′
j

4

• Now, we would like to precise the CFE of reals in ←→
[θ, θ′] ( denotes the set of reals that are
between θ and θ′, even if θ > θ′), where θ and θ′ are two diﬀerent reals and ﬁnd the rationals in
this interval with the lowest reduced denominator.

First, we introduce a simple and natural notion :

Deﬁnition 1 ( CFE-depth of a real) .
let x be a real. We name CFE-depth of x the non negative integer, denoted µ(x) and deﬁned
by : µ(x) = +∞ if x is irrational and µ(x) = s, if x = [a0, a1, · · · , as, 1] is the CFE of x.

We remark that :

µ(x) = 0 ⇔ x ∈ Z ; ∀n ∈ Z, µ(x + n) = µ(x) ; ∀x ̸∈ Z, µ(T (x)) = µ(x) − 1

We denote θ = [tk]k∈N and θ′ = [t′
k]k∈N, according to our ϕ1-representation. We will abreviate
t and t′ these CFE-sequences. We denote r the smallest integer k such that tk ̸= t′
k. Then we
have r ⩽ min(µ(θ), µ(θ′)) + 2, when θ or θ′ is rational ( if they are both irrationals, r is ﬁnite !
). Indeed, the extremal case when r = µ(θ) + 2 for example corresponds to θ = [t0, · · · , tr−2, 1]
and θ′ = [t0, · · · , tr−2, 1, t′
r, ...], with t′
r < ∞.

We remark that, all integers in ←→
[θ, θ′] minimize the denominator of their reduced fraction : it
is 1 !! So, we can suppose that ⌊θ⌋ = ⌊θ′⌋ and even that θ, θ′ ∈ [0, 1[.

The following Lemma proves that, in that case, there is only one rational in ←→
[θ, θ′], that

minimizes the value of its denominator : it is usually named the ” best rational” in ←→
[θ, θ′]

Proposition 1 let θ and θ′ be two diﬀerent reals in [0, 1[ and θ = [tk]k∈N, θ′ = [t′
k]k∈N their
respective CFE. We denote r the lowest integer k such that tk ̸= t′
k.

(i) there is a unique rational in ←→
[θ, θ′] that minimizes the denominator. We denote it γ.
- if r ⩽ min(µ(θ), µ(θ′)), then γ = [t0, · · · , tr−1, min(tr, t′
r), 1].
- else, µ(θ) < µ(θ′) ( up to swap) and γ = θ.
(ii) in both cases, µ(γ) ⩽ min(µ(θ), µ(θ′)) and γ = [t0, · · · , ts−1, min(ts, t′
s), 1], where s = µ(γ) ⩽
r and ∀k ∈ {0 · · · s − 1}, tk = t′
k.

(iii) the best rational in ←→
[θ, θ′] is the common semi-convergent of θ and θ′ with the greatest
denominator.

Proof :
(i) if r ⩽ min(µ(θ), µ(θ′)). Suppose that tr < t′
r. We have for (dk)k∈N ∈ C:

[dk]k∈N ∈ ←→
[θ, θ′] ⇔
 {∀k < j, dk = tk = t′
k
σr(t) ⩽A σr(d) ⩽A σr(t′) (∗)

where σ is the usual shift : for any sequence u, ∀k ∈ N, σ(u)k = uk+1.
But, if we want the lowest denominator for the rational [dk]k∈N, we have to choose the lowest dk or the
∞ value ( if possible), for all k. So we have to choose ﬁrst dr = tr and then, the condition (*) becomes :
σr+1(d) ⩽A σr+1(t). So, we choose dr+1 = 1 and ∀k > r + 1, dk = ∞.
- else, one at least of µ(θ) and µ(θ′) is ﬁnite and they can not be equal, since r can not be greater than
both of them. Suppose µ(θ) < µ(θ′), then we have µ(θ) < r and ∀k ∈ {0 · · · µ(θ)}, tk = t′
k. So, the same

arguments as in the previous case prove that θ is the best rational in ←→
[θ, θ′].

(ii) it is plain in the ﬁrst case, since µ(γ) = r. If µ(θ) < r and µ(θ) < µ(θ′), then γ = θ and ts = t′
s.

(iii) is a consequence of (ii), Lemma 1 and the remark following it. ■

5

Remark : as a direct consequence of (iii) : θ is the best rational in ←→
[θ, θ′] if and only if θ is a
semi-convergent of θ′.

• Let α be a real, [ak]k∈N∗ its CFE and r = µ(α), the CFE-depth of α. So, we denote
[a0, a1, · · · , ar, 1] the CFE of α if α is rational. We also denote (pn/qn)n the usual sequence
of convergents of α.
We consider the usual notion of best rational approximation of a real α : for p, q two integers,
p/q is said a best rational approximation of α if and only if :

∀q′ ∈ {1 · · · q − 1} , ∀p′ ∈ Z , ∣
∣
∣
∣ p′

q′ − α
∣
∣
∣
∣ > ∣
∣
∣
∣ p
q − α
∣
∣
∣
∣

It is well known that best rational approximation of a real are exactly its reduced convergents.
Now, we can consider two sided similar deﬁnitions :

Deﬁnition 2 ( best sided rational approximation) .
for p, q two integers, p/q is said a best left rational approximation of α if and only if :

∀q′ ∈ {1 · · · q − 1} , ∀p′ ∈ Z , p′

q′ < p
q ⩽ α or p′

q′ > α

p/q is said a best right rational approximation of α if and only if :

∀q′ ∈ {1 · · · q − 1} , ∀p′ ∈ Z , p′

q′ > p
q ⩾ α or p′

q′ < α

Here is a corollary of Proposition 1 :

Corollary 1 .
(i) best left rational approximations of α are the semi-convergents of α, that are lower than α.
(ii) best right rational approximations of α are the semi-convergents of α, that are greater than
α.

Proof :
(i) we remark that p/q is a best left rational approximation of α if and only if p/q is the best rational in
[p/q, α] and use the remark below Proposition 1. Same arguments for (ii). ■

If we denote (pk/qk)k the reduced convergents of α, then :
- its best left rational approximations are :

p2i + mp2i+1
q2i + mq2i+1 ; i ∈ {0 · · · (µ(α) − 1)/2} ; m ∈ {0 · · · a2i+2}

- its best right rational approximations are :

p2i−1 + mp2i
q2i−1 + mq2i ; i ∈ {1 · · · µ(α)/2} ; m ∈ {0 · · · a2i+1}

6

2 A numeration system

2.1 Ostrowski’s numeration

We will only deal here with the case α irrational, even if the rational case is interesting ( see
next section). We denote Ωα the set of sequences of integers deﬁned as follows ( we denote
[ak]k∈N the continued fraction expansion of α) :

Ωα = {(dn)n∈N∗, d1 ∈ {0 · · · a1 − 1}, ∀k ∈ N∗\{1}, dk ∈ {0 · · · ak} and (dk = ak ⇒ dk−1 = 0)}

What we call ” markovian condition” is the last implication : dk = ak ⇒ dk−1 = 0.
From this set of inﬁnite sequences, we extract two subsets, that will be our numeration sets
for reals and integers respectively : Oα is the set of sequences d of Ωα such that d does not ” end
with” (max, 0)∞, an inﬁnite sequence ak0ak+20 · · · . So to say, there is an inﬁnite number of even
and an inﬁnite number of odd values of k such that dk < ak. Now, O(α) is the set of sequences d of
Ωα ( or Oα) that ends with an inﬁnite sequence of 0 : so to say dk = 0 for any suﬃciently large k.

We deﬁne then two maps :

fα :
 




O(α) → N

d → ∞∑

k=1 dkqk−1 ; gα :
 



Oα → [−α, 1 − α[

d → ∞∑

k=1 dk(αqk−1 − pk−1)

It is well known that fα and gα are well deﬁned and are bijective. Moreover :

∀d ∈ O(α), {fα(d)α} = {gα(d)}

But, we will emphasize an other aspect : the maps above are increasing for the usual order on
N and R respectively and following orders on O(α) and Oα.

- the reversed lexicographic order ( RLO) on O(α) :

d ⩽
R d
′ ⇔ d = d
′ or ∃j ∈ N∗,
 {dj < d′
j
∀i > j, di = d′
i

- the alternate lexicographic order ( ALO) on Oα :

d ⩽
A d
′ ⇔ d = d
′ or ∃j ∈ N∗,
 {(−1)j−1dj < (−1j−1d′
j
∀i ∈ {1 · · · j − 1}, di = d′
i

These are total orders on these sets respectively.

Our aim is to ﬁnd a variant of Ostrowski numeration that has same properties, but that code
reals of [0, 1[ instead of [−α, 1 − α[ and also all integers, positive as well as negative ones.
We will see that it suﬃces to change the markovian condition : instead of dk = ak ⇒ dk−1 = 0,
we take dk = 0 ⇒ (dk−1 = ak−1 or di = 0 for all i ⩾ k).

7

2.2 α-numeration for a rational α

Why do we consider this case α rational ? Indeed, the set {{nα}, n ∈ N} is ﬁnite and triv-
ial. It can not deﬁne a base of numeration for [0, 1[. But the order properties of the sequence
({nα})n∈N are not obvious and our Ostrowski-like numeration will help.

• Let α be a rational in [0, 1[ and α = [0, a1, · · · , ar, 1] its CFE. We will denote (pk/qk)0⩽k⩽r+1
its convergents, so that α = pr+1
qr+1 .

Deﬁnition 3 ( α-admissible sequences) .
a sequence d in Nr is said α-admissible if and only if :

∀j ∈ {1 · · · r},
 {dj ∈ {0 · · · aj}
dj = 0 ⇒ (∀i ⩾ j, di = 0) or dj−1 = aj−1

We will denote Eα the set of α-admissible sequences.

Remark : for j = 1, the second condition reduces to d1 = 0 ⇒ ∀i ⩾ 1, di = 0. So to say,
d = (0, · · · , 0) is the only element of Eα , whose ﬁrst coordinate is 0.

Lemma 2 .
(i)
 ∀d ∈ Eα, ∀k ∈ {1 · · · r},
 k∑

i=1 diqi−1 < qk + qk−1

(ii) let d, d′ ∈ Eα and n ∈ {1 · · · r} such that d′
n > 0.

∀k ∈ {1 · · · n},
 k∑

i=1(di − d
′
i)qi−1 < qk

Proof :
(i) by plain induction on k.
(ii) by induction ( on 2 ranks) on k :
- it is true for k = 0 ( obvious) and for k = 1 : indeed d
′
1 > 0 ( else, we would have d
′ = 0 and d
′
n = 0) :
then (d1 − d
′
1)q0 ⩽ (a1 − 1)q0 = q1 − 1.
- we suppose that it is true for the ranks k − 2 and k − 1, where k is an integer in {2 · · · n}. Then, we
have two cases for the rank k :
◮ Case 1 : dk − d
′
k ⩽ ak − 1, then, with the induction hypothesis on rank k − 1 :

k∑

i=1(di − d
′
i)qi−1 < qk−1 + (ak − 1)qk−1 = akqk−1 = qk − qk−2 < qk

the last inequality is true, for k ⩾ 2.
◮ Case 2 : dk = ak, d
′
k = 0, then d
′
k−1 = ak−1 ( else, we would have d
′
j = 0 for all j ⩾ k, but d
′
n ̸= 0)
and dk−1 − d
′
k−1 ⩽ 0. So with the induction hypothesis on rank k − 2 :

k∑

i=1(di − d
′
i)qi−1 < qk−2 + akqk−1 = qk

■
 8

We consider the reversed lexicographic order ( RLO) denoted ⩽
R on Nr :

d ⩽
R d
′ ⇔ d = d
′ or ∃j ∈ {1 · · · r},
 {
dj < d′
j
∀i ∈ {j + 1 · · · r}, di = d′
i

It is a total order on Eα.

Lemma 3 the map Ψα below is increasing from (Eα, ⩽R) to ({0 · · · qr+1 − 1}, ⩽).

Ψα :
 



Eα → {0 · · · qr+1 − 1}

d → r∑

j=1 djqj−1

Proof :
First, for all d ∈ Eα, Ψα(d) ∈ {0 · · · qr+1 − 1}, with Lemma 2 (i).
Now, let prove that Ψα is increasing. Let d, d
′ ∈ Eα, such that d <R d
′. We have j ∈ {1 · · · r}, such
that : dj < d
′
j and ∀i ∈ {j + 1 · · · r}, di = d
′
i

So :
 Ψα(d
′) − Ψα(d) =
 j−1∑

i=1(d
′
i − di)qi−1 + (d
′
j − dj)qj−1

We just have to prove that : j−1∑

i=1(di − d
′
i)qi−1 < qj−1, since d
′
j − dj ⩾ 1. This is shown by Lemma 2 (ii),

for d
′
j > 0. ■

Now, we prove that Ψα is surjective : the following algorithm explains the inverse function of
Ψα. We will denote mk = qk + qk−1 for any k ∈ {0 · · · r}. So mr = qr+1.

Algorithm 1 let n ∈ {0 · · · mr − 1}.
With the following algorithm, we have d ∈ Eα and Ψα(d) = n.

Input: n
Output: (di)i∈{1···r}

for k ← r to 1 step −1 do

dk ← max (
0, ⌊ n−qk−2
qk−1
 ⌋) ;
n ← n − dkqk−1
end

Proof :
We begin with a remark : if n < ms for an integer s ∈ {1 · · · r}, then : dk = 0 for k ∈ {s + 1 · · · r}.
Indeed, we will have n < mk for all k ∈ {s · · · r} so n − qk−2 < qk−1 for all k ∈ {s + 1 · · · r}.
Let us prove the result by induction on s, where s in an integer such that n ∈ {0 · · · ms − 1} :
- for s = 1, m1 = a1 + 1. Let n ∈ {0 · · · a1}. Then d1 = n and d = (d1) ∈ Eα, Ψα(d) = d1 = n.
- we suppose that the algorithm is available for all n ∈ {0 · · · ms−1 − 1}, with s ⩾ 2.
Let n ∈ {ms−1 · · · ms − 1}. Then qs−1 ⩽ n − qs−2 < (as + 1)qs−1, so ds ∈ {1 · · · as}. We denote
n1 = n − dsqs−1, the value of n after the loop for k = s. We have : qs−2 ⩽ n1 < qs−1 + qs−2 = ms−1. By

induction hypothesis, d
′ = (d1, · · · , ds−1) ∈ Eα and n1 = Ψα(d
′) = s−1∑

i=1 diqi−1. But, n = n1 + dsqs−1 and

so Ψα(d) = n, because we have d ∈ Eα : indeed, we have 2 subcases :

9

◮ Case 1 : if n1 ⩾ ms−2, then ds−1 > 0 and, since (d1, · · · , ds−1) ∈ Eα, then d ∈ Eα.
◮ Case 2 : if n1 < ms−2 ( which leads to s ⩾ 3, for m0 = q0), then ds−1 = 0 and n2 = n1 ( n2 : the
value of n after the loop for k = s − 1). But, since n1 ⩾ qs−2, then n2 − qs−4 ⩾ as−2qs−3 and ﬁnally
ds−2 = as−2. By induction hypothesis, d
′ = (d1, · · · , ds−3, as−2, 0) is α-admissible, so d ∈ Eα. ■

Proposition 2 Ψα is an order isomorphism between (Eα, ⩽R) and ({0 · · · qr+1 − 1}, ⩽).

Remark : as a direct consequence : Eα has qr+1 elements.
Proof :
a direct consequence of Lemma 3 and Algorithm 1 ■

• Now, we will deal with α-numeration for elements of Uα = {{kα}, k ∈ N}. Since, α = pr+1
qr+1 and
this fraction is reduced, we have Uα = { n
qr+1 , n ∈ {0 · · · qr+1 − 1}}. So, this set is very simple,
but we will focus on the map k → {kα}, with the order point of view :
We consider the alternate lexicographic order ( ALO) denoted ⩽
A on Rr :

d ⩽
A d
′ ⇔ d = d
′ or ∃j ∈ {1 · · · r},
 {
(−1)j−1dj < (−1)j−1d′
j
∀i ∈ {1 · · · j − 1}, di = d′
i

It is another total order on Eα. We deﬁne also :

∀i ∈ {−2 · · · r}, δi = (−1)
i(qiα − pi)

We have, with a0 = 0 here :

δ−2 = α ; δ−1 = 1 ; δ0 = {α} = α ; ∀i ∈ {0 · · · r}, δi = −aiδi−1 + δi−2

Let T be the Gauss map : ]0, 1[→ [0, 1[, x → {1/x}.
By induction on i, with the fact that : ai = ⌊ 1
T i−1(α) ⌋ if i ⩽ r − 1, we obtain :

∀i ∈ {0 · · · r − 1}, δi
δi−1 = T i(α)

Beware : for i = r, T r−1(α) = [0, ar, 1] = 1
ar+1 , so :

δr
δr−1 = δr−2 − arδr−1
δr−1 = 1
T r−1(α) − ar = 1

So : δr = δr−1. We will prove ( proof of Algorithm 2) that δr = δr−1 = 1
qr+1 .
To summarize this :

∀i ∈ {0 · · · r − 1}, 0 < δi < δi−1 ; δr = δr−1 = 1
qr+1

Lemma 4 let d, d′ ∈ Eα and j ∈ {1 · · · r}, , then :

(−1)
j−1(d
′
j − dj) > 0 ⇒
 r∑

i=j+1
(−1)
i(d
′
i − di)δi−1 < δj−1

10

Proof :
First, we remark that, for all i, we have (−1)
i(d
′
i − di) ⩽ ai, so :

r∑

i=j+1(−1)
i(d
′
i − di)δi−1 ⩽
 r∑

i=j+1 aiδi−1 =
 r∑

i=j+1(δi−2 − δi) = δj−1 + δj − δr−1 − δr

◮ Case 1 : if (−1)
j+1(d
′
j+1 − dj+1) ⩽ aj+1 − 1, then :

r∑

i=j+1(−1)
i(d
′
i − di)δi−1 ⩽ δj−1 − δr−1 − δr < δj−1

◮ Case 2 : if (−1)
j+1(d
′
j+1 − dj+1) = aj+1.
◮◮ Subcase 1 : if j is even, d
′
j+1 = 0 and dj+1 = aj+1. We can not have d
′
j = aj, for, with our hypothesis,
dj > d
′
j. So d
′
i = 0 for all i > j and :

r∑

i=j+1(−1)
i(d
′
i − di)δi−1 = aj+1δj −
 r∑

i=j+2(−1)
idiδi−1 ⩽
 (r−j−1)/2∑

p=0 aj+2p+1δj+2p =

=
 (r−j−1)/2∑

p=0 (δj+2p−1 − δj+2p+1) = δj−1 − δr′ < δj−1

with r′ = r or r − 1.
◮◮ Subcase 2 : if j is odd, similar arguments lead to the same conclusion ( we swap d and d
′). ■

Proposition 3 .
(i) the map Λα ( deﬁned below) is an order isomorphism, with ALO on Eα :

Λα :
 



Eα → { n
qr+1 , n ∈ {0 · · · qr+1 − 1}
}

d → r∑

j=1 dj(−1)j−1δj−1

(ii) we have : ∀n ∈ {0 · · · qr+1 − 1}, {nα} = Λα(Ψ−1
α (n))

Proof :
(i) First, we will show that Λα is increasing : let d, d
′ ∈ Eα with d <A d
′. Then, we have j ∈ {1 · · · r}
such that : (−1)
j−1dj < (−1)
j−1d
′
j and ∀i < j, di = d
′
i

So :
 Λα(d
′) − Λα(d) = (−1)
j−1(d
′
j − dj)δj−1 +
 r∑

i=j+1(−1)
i−1(d
′
i − di)δi−1

Now : (−1)
j−1(d
′
j − dj)δj−1 ⩾ δj−1

so with Lemma 4, we obtain : Λα(d
′) − Λα(d) > 0

Now that we have proved that Λα is increasing, we can easily deduce that Λα(Eα) ⊂ [0, 1[ : ﬁrst,
remark that (0, · · · , 0) is the lowest element of Eα ( with ALO), so Λα(d) ⩾ 0 for all d ∈ Eα. Now,
(a1, 0, a3, 0, · · · ) is the greatest element of Eα for ALO, so :

∀d ∈ Eα, Λα(d) ⩽
 (r−1)/2∑

p=0 a2p+1δ2p =
 (r−1)/2∑

p=0 (δ2p−1 − δ2p+1) = δ−1 − δr′ < 1

11

with r′ = r or r − 1.

(ii) we just have to show this equality to complete the proof : let d ∈ Eα. It is suﬃcient to prove that
Λα(d) = {Ψα(d)α}. Now :
 Λα(d) =
 r∑

j=1 dj(qj−1α − pj−1) = αΨα(d) − k

where k = r∑

j=1 djpj−1 is an integer. So Λα(d) = {Ψα(d)α} modulo 1. But, we have seen that both

terms are in [0, 1[, q.e.d. ■

Remarks : result (ii) means that the map n → {nα} ( with 0 ⩽ n < qr+1), is, from the order
point of view, the ” same thing” as the identity (Eα, RLO) → (Eα, ALO).

We can sum up these formulae : ∀n ∈ {0 · · · qr+1 − 1}, with d = Ψ−1
α (n) :

n =
 r∑

j=1 djqj−1 ; ⌊nα⌋ =
 r∑

j=1 djpj−1 ; {nα} =
 r∑

j=1(−1)
j−1djδj−1

The following algorithm expresses the inverse function of Λα.

Algorithm 2 let β ∈ { n
qr+1 , n ∈ N}. Applying the algorithm below, we have :
(i) b ∈ Eα.
(ii) β = Λα(b).

Input: β
Output: (bi)i∈{1···r}

for k ← 1 to r do

bk ← min (
ak, ⌈ β
δk−1
 ⌉) ;
β ← bkδk−1 − β
end

Proof :
First, we denote (βk)k∈{0···r} the ﬁnite sequence deﬁned by :

β0 = β ; ∀k ∈ {1 · · · r} , βk = bkδk−1 − βk−1

Thus, βk is the value of β after k loops in Algorithm 2. So, we have :

bk = min(ak, ⌈βk−1/δk−1⌉)

(i) let us verify that b ∈ Eα : by induction on k, we will prove that ”(b1, · · · , bk) is α-admissible and that
−δk < βk < δk−1 for all k ∈ {0 · · · r}”.
- it is true for k = 0, since δ0 = α > 0 and δ−1 = 1.
- we suppose that it is true for k − 1 with k ∈ {1 · · · r}. Then, βk−1
δk−1 > −1, so ⌈ βk−1
δk−1
 ⌉ ⩾ 0 and 0 ⩽ bk ⩽ ak.
If bk−1 > 0, then (b1, · · · , bk) is α-admissible, for (b1, · · · , bk−1) ∈ Eα. If bk−1 = 0, then βk−2 ⩽ 0 and we
have 2 cases :
◮ Case 1 : if βk−2 = 0, then by obvious induction, βi = 0 and bi = 0 for all i ⩾ k − 1.
◮ Case 2 : else, we have βk−2 < 0 , so k ⩾ 3 and :

βk−3 = bk−2δk−3 − βk−2 > bk−2δk−3

12

So βk−3
δk−3 > bk−2, which leads to bk−2 = ak−2.
In these both cases, we have : (b1, · · · , bk) satisﬁes the conditions of Eα.
Now : by induction hypothesis, we have :

−δk−1 < βk−1 < δk−2

◮ Case 1 : if βk−1
δk−1 ⩽ ak, then : bk = ⌈ βk−1
δk−1
 ⌉ so βk−1 ⩽ bkδk−1, so βk ⩾ 0 and bk < βk−1
δk−1 + 1, so βk < δk−1.

◮ Case 2 : if βk−1
δk−1 > ak, then bk = ak and βk < 0. Moreover :

βk = akδk−1 − βk−1 > akδk−1 − δk−2 = −δk

(ii)
 Λα(b) =
 r∑

k=1
(−1)
kbkδk−1 =
 r∑

k=1
((−1)
kβk − (−1)
k−1βk−1) = (−1)
rβr − β

we also have β = Λα(b) + (−1)
rβr. Now, −δr < βr < δr−1.
Claim : ” for every k ∈ {−1 · · · r−1}, qr+1δk is the kth remainder, denoted ρk in the euclidean algorithm
between pr+1 and qr+1 and we have ρr−1 = 1.”
Indeed, by double induction on k :
- it is true for k = −1 and k = 0, since qr+1δ−1 = qr+1 = ρ−1 and qr+1δ0 = pr+1 = ρ0.
- then, both sequences satisfy the same double induction formula :

∀k ∈ {1 · · · r − 1}, qr+1δk = qr+1δk−2 − akqr+1δk−1 ; ρk = ρk−2 − akρk−1

Now, euclidean algorithm stops when we obtain a rest equal to 0, and the former rest is the greatest
common divisor of ρ−1 and ρ0, namely 1 here, since the convergent fractions are reduced. So, ρr−1 = 1.
But, we have chosen the continued fraction expansion of α, that ends with 1, so ρr−2 = ar + 1, and
qr+1δr = ρr−2 − arρr−1 = 1.
We conclude : δr = δr−1 = 1
qr+1 and |βr| ∈ [0, 1/qr+1[.
Now, the former facts show that βkqr+1 ∈ Z for all k, so : βr = 0. ■

• We can easily extend this numeration to [0, 1[, by adding a last ” digit” that can range in
[0, 1[. First, we extend the ALO to Eα × [0, 1[ : (d, ǫ) ⩽A (d′, ǫ′) if and only if (d = d′ and ǫ ⩽ ǫ′)
or d <A d′.

Corollary 2 the map ˜Λα is an order isomorphism, with ALO on Eα × [0, 1[ :

˜Λα :
 



Eα × [0, 1[→ [0, 1[

(d, ǫ) → r∑

j=1 dj(−1)j−1δj−1 + ǫδr

Proof :
a direct consequence of Proposition 3. ■

Remark : if ˜Λα(d, ǫ) = β then ǫ = {qr+1β}, with usual notations.

13

2.3 α-numeration for an irrational α

• Let α be an irrational and [ak]k∈N its CFE. We extend our notion of α-admissible sequence :

Deﬁnition 4 (α-admissible sequences) .
a sequence d in NN∗ is said α-admissible if and only if d does not end with (max, 0)∞, an inﬁnite
sequence of ak, 0, ak+2, 0, · · · ( so to say there are an inﬁnite number of even and odd indices k
such that dk > 0 or dk+1 < ak) and :

∀j ∈ N∗,
 {dj ∈ {0 · · · aj}
dj = 0 ⇒ (∀i ⩾ j, di = 0) or dj−1 = aj−1

Thus, the null-sequence is the only α-admissible sequence that begins with 0. We denote Eα
the set of α-admissible sequences and E(α) the subset of Eα of sequences, that ends with 0∞, an
inﬁnite sequence of 0.

• We consider two lexicographic total order, respectively on Eα and E(α) :
- the reversed lexicographic order ( RLO) on E(α) :

d ⩽
R d
′ ⇔ d = d
′ or ∃j ∈ N∗,
 {dj < d′
j
∀i > j, di = d′
i

- the alternate lexicographic order ( ALO) on Eα :

d ⩽
A d
′ ⇔ d = d
′ or ∃j ∈ N∗,
 {(−1)j−1dj < (−1j−1d′
j
∀i ∈ {1 · · · j − 1}, di = d′
i

• We deﬁne : ∀i ∈ N ∪ {−1} , δi = (−1)
i(qiα − pi)

with, as usual pi/qi being the reduced fraction of the convergent [a0, · · · , ai]. We have then :

δ−1 = 1 ; δ0 = α ; ∀i ∈ N∗ , δi = −aiδi−1 + δi−2

Let T be the Gauss map : ]0, 1[\Q →]0, 1[\Q, x → {1/x}.
By induction on i, with the fact that : ai = ⌊ 1
T i−1(α) ⌋ if i ∈ N∗, we obtain :

∀i ∈ N , δi
δi−1 = T i(α)

(δi)i∈N is a decreasing and positive sequence, that converges towards 0.

Lemma 5 let d, d′ ∈ Eα and j ∈ {1 · · · r}, , then :

(−1)
j−1(d
′
j − dj) > 0 ⇒
 ∞∑

i=j+1
(−1)
i(d
′
i − di)δi−1 < δj−1

Proof :
We have 2 cases :
◮ Case 1 : if (−1)
j+1(d
′
j+1 − dj+1) ⩽ aj+1 − 1, then :

∞∑

i=j+1(−1)
i(d
′
i − di)δi−1 ⩽ (aj+1 − 1)δj +
 ∞∑

i=j+2(−1)
i(d
′
i − di)δi−1

14

But, nor d nor d
′ ends with (max, 0)
∞, an inﬁnite sequence of ” (ak, 0)”, so :

∃k > j + 1, (−1)
k(d
′
k − dk) < ak ; ∀i > j, (−1)
i(d
′
i − di) ⩽ ai

We deduce :
 ∞∑

i=j+2(−1)
i(d
′
i − di)δi−1 <
 ∞∑

i=j+2 aiδi−1 =
 ∞∑

i=j+2(δi−2 − δi) = δj+1 + δj

We conclude : ∞∑

i=j+1(−1)
i(d
′
i − di)δi−1 < aj+1δj + δj+1 = δj−1

◮ Case 2 : if (−1)
j+1(d
′
j+1 − dj+1) = aj+1.
◮◮ Subcase 1 : if j is even, d
′
j+1 = 0 and dj+1 = aj+1.
We can not have d
′
j = aj, for (−1)
j−1dj < (−1)
j−1d
′
j, so d
′
i = 0 for all i > j and, since d does not end
with (max, 0)
∞, then :

∞∑

i=j+1(−1)
i(d
′
i − di)δi−1 = aj+1δj −
 ∞∑

i=j+2(−1)
idiδi−1 <
 ∞∑

p=0 aj+2p+1δj+2p

Indeed, (−1)
j+2pdj+2pδj+2p−1 ⩾ 0, for all p ∈ N, since j is even. So :

∞∑

i=j+1(−1)
i(d
′
i − di)δi−1 <
 ∞∑

p=0(δj+2p−1 − δj+2p+1) = δj−1

◮◮ Subcase 2 : if j is odd, similar arguments lead to the same conclusion ( we swap d and d
′).■

• Now, we deﬁne two maps on these sets :

Proposition 4 .
(i) the map Ψα ( deﬁned below) is an order isomorphism from (E(α), ⩽R) to (N, ⩽).

Ψα :
 



E(α) → N

d → ∞∑

j=1 djqj−1

(ii) the map Λα ( deﬁned below) is an order isomorphism from (Eα, ⩽A) to ([0, 1[, ⩽). :

Λα :
 




Eα → [0, 1)

d → ∞∑

j=1 dj(−1)j−1δj−1

(iii) we have : ∀n ∈ N, {nα} = Λα(Ψ−1
α (n))

Remark 1 : the inﬁnite sum in the deﬁnition of Ψα is in fact a ﬁnite one. The inﬁnite sum
in the deﬁnition of Λα is well deﬁned since :

∀j ∈ N∗, 0 ⩽ djδj−1 ⩽ ajδj−1 = δj−2 − δj

Remark 2 : if we had deﬁned Eα without the restriction about the ending of the sequences,
then the result about Λα would have been valid, except that : for x ∈ {{nα}, n ∈ N}, x would
have three ( two for 0) preimages : the one in E(α) and those that end with (max, 0)∞, an

15

inﬁnite sequence of ”ak, 0”.

Proof :
(i) see proof of Lemma 3 and proof of Algorithm 1.
(ii) ﬁrst, we will prove that Λα is increasing : let d, d
′ ∈ Eα such that d <A d
′. Then, we have j ∈ N∗

such that : (−1)
j−1dj < (−1)
j−1d
′
j and ∀i < j, di = d
′
i
So :
 Λα(d
′) − Λα(d) = (−1)
j−1(d
′
j − dj)δj−1 +
 ∞∑

i=j+1(−1)
i−1(d
′
i − di)δi−1

But, (−1)
j−1(d
′
j − dj )δj−1 ⩾ δj−1, so with Lemma 5, we obtain : Λα(d
′) − Λα(d) > 0.
Now that we have proved that Λα is increasing, we can easily deduce that Λα(Eα) ⊂ [0, 1[ : ﬁrst,
remark that (0, · · · , 0) is the lowest element of Eα ( with ALO), so Λα(d) ⩾ 0 for all d ∈ Eα. In addition,
if j is even (−1)
j−1djδj−1 ⩽ 0 and if j is odd, say j = 2p + 1, with p a non negative integer, then
(−1)
j−1djδj−1 ⩽ a2p+1δ2p, this inequality being strict for at least one p, so :

∀d ∈ Eα, Λα(d) <
 ∞∑

p=0 a2p+1δ2p =
 ∞∑

p=0(δ2p−1 − δ2p+1) = δ−1 = 1

For the surjectivity, we refer to Algorithm 3(ii) below.
(iii) see proof of Proposition 3(ii). ■

Algorithm 3 .
(i) the inverse function of Ψα is deﬁned by the following algorithm :
Let n ∈ N and r = max({k ∈ N, n < qk + qk−1}). We deﬁne d by : ∀k > r, dk = 0 and

Input : n Output : (di)i∈{1···r}

for k = r to k = 1 with step −1 :
 {dk = max (0, ⌊ n−qk−2
qk−1
 ⌋)

n ← n − dkqk−1

(ii) the inverse function of Λα is deﬁned by the following ( inﬁnite) ” algorithm” :
Let β ∈ [0, 1[. We denote β0 = β and deﬁne the sequences b = (bk)k∈N∗ and (βk)k∈N∗ by :

Input : β Output : (bi)i∈N∗

for k = 1 to k = ∞ with step 1 :
 {
bk = min (
ak, ⌈ βk−1
δk−1
 ⌉)

βk = bkδk−1 − βk−1

Proof :
(i) see proof of Algorithm 1.
(ii) the proof that b ∈ Eα is the same as the proof of Algorithm 2, with the additional argument : b does
not end with (max, 0)
∞, an inﬁnite sequence of ” (ak, 0)”, that will be shown below.
First, we remark that (βk)k converges towards 0, for (−1)
kβk − (−1)
k−1βk−1 = (−1)
kbkδk−1 is the

general term of a convergent serie. We can deﬁne β′ = ∞∑

j=1 bj(−1)
j−1δj−1 and verify that β′ = β :

β′ =
 ∞∑

j=1(−1)
j−1(βj + βj−1) = β0 = β

Suppose that b ends with (max, 0)
∞ : this means that, we have r ∈ N∗, such that :

(r = 1 or br−1 ̸= 0) ; ∀p ∈ N, br+2p = ar+2p ; br+2p+1 = 0

16

So :
 β =
 r−1∑

j=1 bj(−1)
j−1δj−1 + (−1)
r−1 ∞∑

p=0 ar+2pδr+2p−1 =
 r−1∑

j=1 bj(−1)
j−1δj−1 + (−1)
r−1δr−2

If r = 1, then β = δ−1 = 1, so r ⩾ 2 and we recognize β = Λα(b′), where b′ = (b1, · · · , br−2, br−1 − 1) ∈
E(α). Using the proof of Algorithm 2, we obtain βr−1 = 0, so b ends with an inﬁnite sequence of ” 0”. ■

We can sum up these formulae : for all non negative integers n, if we denote d = Ψ−1
α (n) :

n =
 ∞∑

j=1 djqj−1 ; ⌊nα⌋ =
 ∞∑

j=1 djpj−1 ; {nα} =
 ∞∑

j=1(−1)
j−1djδj−1

Notations : if no ambiguity, we will denote n = (d1, d2, · · · , ds)α the Ψα-numeration of an
integer n and β = (b1, · · · )α the Λα-numeration of a real β of [0, 1[.

Remark 1 : we denote Nα the completion of (N, D), where D is the distance deﬁned by :

∀n, n′ ∈ N, D(n, n′) = |{n′α} − {nα}|

Proposition 4 proves that Nα can be represented ( bijectively) by Eα : if n ∈ Nα is represented

by d ∈ Eα then we could deﬁne : {nα} := ∞∑

j=1
(−1)j−1djδj−1. We obtain a bijective map :

Nα → [0, 1[ ; n → {nα}

Remark 2 : in next subsection, we will study the eﬀect of the symmetry β → 1 − β on
α-numeration of reals of [0, 1[. But now, we are interested in this symmetry acting both on α
and β, which gives a much simpler result :
- ﬁrst, let α be a real in ]0, 1/2[ and let us consider the CFE of α and 1 − α :

α = [ak]k∈N ⇒ 1 − α = [0, 1, a1 − 1, a[2,∞]]

Indeed, if we denote 1 − α = [a′
k]k∈N, α1 = [a[2,∞]] and α′
1 = [a′
[2,∞]], then a′
0 = a0 = 0, a′
1 = 1
and : α = 1
a1 + α1 ; 1 − α = 1
1 + α′
1
So : α
′
1 = 1
1 − α − 1 = 1
1
α − 1 = 1
a1 − 1 + α1

- secondly : let α ∈]0, 1/2[, β ∈]0, 1[ and (bk)k its α-numeration, then :

1 − β = (1, b1 − 1, b[2,∞])1−α

Indeed : if we denote δ′
i the analoguous of δi ( related to α) for 1 − α ( see above), then :

δ′
−1 = 1 ; δ′
0 = 1 − α ; ∀i ⩾ 1, δ′
i = δi−1

The last equality is obtained with obvious induction and previous result on CFE. Now, we
just have to verify that :
 δ′
0 − (b1 − 1)δ′
1 + ∑

i⩾2 (−1)
i−1bi−1δ′
i−1 = 1 − β

that is an easy calculation...
 17

2.4 α-numeration of negative integers

Let α be an irrational in ]0, 1[ and [ak]k∈N its CFE. We have seen at 2.3 that Eα, the set of
α-admissible sequences is in bijective correspondance with [0, 1[, via the following map :

Λα : d = (dk)k∈N∗ →
 ∞∑

k=1 dkδ′
k−1

where δ′ is the sequence deﬁned by :

δ′
−1 = −1 ; δ′
0 = α ; ∀k ∈ N∗, δ′
k = akδ′
k−1 + δ′
k−2

with notations of 2.3, we have :

∀k ∈ {−1 · · · + ∞}, δ′
k = qkα − pk = (−1)
kδk

In addition δ′ converges towards 0 and we could set δ′
∞ = 0.

In order to deﬁne the α-numeration of negative integers, we consider the natural involution of
[0, 1[, that we denote C : the complement to 1.

C :
 {
C(0) = 0
∀x ∈]0, 1[, C(x) = 1 − x

We also have : ∀x ∈ [0, 1[, C(x) = {−x}. We can see C as the usual conjugacy over the
unit circle U, the set of complex of moduli one, via the bijection : [0, 1[→ U, x → e2iπx. C is
decreasing, when restricted to ]0, 1[.

Question : is there a simple and natural expression of conjugate involution Cα of Eα, induced
by C, via Λα, that is : Cα = Λ
−1
α ◦ C ◦ Λα

Thinking of the analoguous problem for usual (bk)k basis-numeration, where b is an integer
bigger than 1, we could try to use a kind of ” complement to (ak)k∈N∗” transformation. Indeed,
(ak)k∈N∗ is the biggest sequence in Eα for the usual lexicographic order. But, we also have to
add 1 to the ﬁrst digit, so, let m be the following sequence :

m1 = a1 + 1 ; ∀k > 1, mk = ak

We extend the deﬁnition of Ψα to all real sequences in l1(δ′) = {u ∈ RN∗, ∑k |ukδ′
k| < +∞}.

Lα : l1(δ′) → R; d →
 ∞∑

k=1 dkδ′
k−1

Then, Lα(m) = 1, for :

∞∑

k=1 mkδ′
k−1 = α +
 ∞∑

k=1 akδ′
k−1 = α +
 ∞∑

k=1(δ′
k − δ′
k−2) = α − δ′
−1 − δ′
0 = 1

Since Lα is linear, we have :

∀d ∈ l1(δ′), Lα(m − d) = 1 − Lα(d)

18

In particular, for d ∈ Eα, we obtain : Lα(m − d) = 1 − Ψα(d). So, the question is : do we
always have m − d ∈ Eα ? Unfortunately, no. But, m − d ∈ Eα in most cases.
First, since d does not end with (max, 0)∞ ( see 1.2), that is also the case for m − d.
Secondly, if d is not the null sequence, then mk −dk ∈ {0 · · · ak} for all k ∈ N∗, and m1 −d1 > 0.
Finally, the only case where d ∈ Eα and m − d ̸∈ Eα is when m − d contains a ﬁnite word of
consecutive 0, that is not preceeded by a maximal digit ( say dk = ak) and that is not succeeded
by a 0. We will name such a word, a not admissible word. Such a word can appear in m − d,
for d can contain a word with consecutive maximal digits.
We will see below how to convert such a sequence into an α-admissible sequence. First, let ∼
denote the equivalence relation on l1(δ′), induced by Lα :

∀u, v ∈ l1(δ′), u ∼ v ⇔ Lα(u) = Lα(v)

This relation ∼ is compatible with the linear structure of l1(δ′).

We have, for all r, s ∈ N∗ :

(0
r, 1, (max, 0)
s−1, max, −1, 0
∞) ∼ 0
∞ (1)

Indeed :
 Lα((0
r, 1, (max, 0)
s−1, max, −1, 0
∞)) = δ′
r +
 s∑

k=1 ar+2kδ′
r+2k−1 − δ′
r+2s =

= δ′
r +
 s∑

k=1(δ′
r+2k − δ′
r+2k−2) − δ′
r+2s = 0

Case 1 : a list of an even number of consecutive 0 ( not preceeded by a maximal digit
and not succeeded by a 0). So, if we have a sequence (ek)k, such that e[1,r] = [e1, · · · , er] only
contains admissible words and such that er ̸= ar, er+2s+1 ̸= 0 and ek = 0 for k ∈ {r + 1 · · · r + 2s}
( where r, s ∈ N∗).
Then, adding (ek)k to relation (1), we obtain :

(ek)k⩾1 ∼ (e[1,r], 1, (max, 0)
s−1, max, er+2s+1 − 1, e[r+2s+2,∞])

Thus, the new sequence (e′
k)k only contains admissible words in its ﬁrst r + 2s + 1 digits.

Case 2 : a list of an odd number of consecutive 0 ( not preceeded by a maximal digit and
not succeeded by a 0). So, if we have a sequence (ek)k, such that e[1,r] only contains admissible
words and such that er ̸= ar, er+2s ̸= 0 and ek = 0 for k ∈ {r + 1 · · · r + 2s − 1} ( r, s ∈ N∗).
Then, adding (ek)k to relation (1) ( with r − 1 instead of r), we obtain :

(ek)k⩾1 ∼ (e[1,r−1], er + 1, (max, 0)
s−1, max, er+2s − 1, e[r+2s+1,∞])

Thus, the new sequence (e′
k)k does not contain any not admissible word in its ﬁrst r +2s digits.

In both cases, we have converted the not admissible word of (ek)k into an admissible word,
giving the same image for Lα. This provides a ( possibly inﬁnite) process to convert any not
admissible element of m − Eα into an element of Eα. We only have to browse once the sequence
(ek)k to convert it into an equivalent α-admissible sequence :

19

Process of conversion :
let d denote an α-admissible sequence that is not the null sequence and e = m − d. Then
e ∈ {1 · · · a1} × ∏k>1{0 · · · ak}. We denote (rj)j and (sj)j the sequences of positive integers such
that, the ﬁnite lists of consecutive 0 in e are for indices from rj + 1 to rj + 2sj or rj + 2sj − 1,
depending on the parity of the lengths (lj)j of these lists. We apply then the inductive following
process :
We suppose that we have converted the digits of e for the indices k ⩽ rj. Then : we can
suppose that erj < aj ( if erj = aj, then we change rj ← rj + 1) and er+lj +1 > 0.
- Case 1 : if lj is even, then :

e ← (e[1,rj], 1, (max, 0)
sj −1, max, erj +2sj +1 − 1, e[rj +2sj+2,∞])

- Case 2 : if lj is odd, then :

e ← (e[1,rj−1], erj + 1, (max, 0)
sj −1, max, erj +2sj − 1, e[rj +2sj+1,∞])

So, this process explicits the map Cα, that is the relation between the α-numerations of β and
1 − β for a real β ∈]0, 1[. We will name this map : CFE-complement.
Now, let us consider the particular case of β = {nα}, where n ∈ N∗. We have seen in 2.3
that n and β have the same α-numeration. Since {−nα} = 1 − β, it is natural to deﬁne the
α-numeration of −n as follows :

Deﬁnition 5 (α-numeration of a negative integer) .
for any positive integer n, we deﬁne the α-numeration of −n as the CFE-complement of the
α-numeration of n.

Notations : we denote Ec
(α) the subset of Eα of sequences ending with max∞, that is to say :

Ec
(α) = {e ∈ Eα, ∃k ∈ N, ∀i > k, ei = ai}

We have then Ec
(α) = Cα(E(α)) and Ec
(α) is the set of α-admissible sequences that ” α-numerate”
negative integers ( see Proposition below).
We will also denote Fα = E(α) ∪ Ec
(α) and we extend RLO, that we deﬁned on E(α), to Fα :

∀d, d
′ ∈ Fα, d <R d
′ ⇔ ∃k ∈ N∗, ((dk < d
′
k, ∀i > k, di = d
′
i) or (∀i ⩾ k, di = ai, d
′
i = 0))

Remark : the above process of conversion is, in that frame, an algorithm, since an element of
Ec
(α) only contains a ﬁnite number of lists of consecutive 0.

Proposition 5 we can extend Ψα from E(α) to Fα as follows :

∀e ∈ Ec
(α), ̃Ψα(e) = −1 −
 ∞∑

k=1(ak − ek)qk−1

hence, ̃Ψα is an order isomorphisme from (Fα, ⩽R) to (Z, ⩽) and we still have :

∀n ∈ Z, Λα( ̃Ψ−1
α (n)) = {nα}

Proof :
- Formula and injectivity : let e ∈ Ec
(α). First, we remark that the sum in the deﬁnition of ̃Ψα(e) is ﬁnite,
since ek = ak for k large enough. Let denote d = m − e and :

n =
 ∞∑

k=1 dkqk−1 ; β =
 ∞∑

k=1 dkδ′
k−1

20

Now, ̃Ψα(e) = −n and n is a positive integer ( d ends with 0∞ and d1 > 0), so ̃Ψα(e) ∈ Z
∗
−.
But d is not always in E(α). Nevertheless β ∈]0, 1[ for :

β = Lα(d) = Lα(m) − Lα(e) = 1 − Λα(e)

indeed, e ∈ Eα. Finally :
 nα − β =
 ∞∑

k=1 dkpk−1 ∈ N

so : β = {nα}. We obtain : Λα(e) = 1 − β = {−nα}. We can conclude :

∀e ∈ F(α), Λα(e) = { ̃Ψα(e)α} (1)

Since, Λα is injective, we deduce that ̃Ψα is injective.
- Surjectivity : let n ∈ N∗, d = Ψ−1
α (n) and e = Λ−1
α (1 − {nα}). Then, e ∈ Ec
(α) ( see the beginning of
this section) and, with (1) :
 Λα(e) = { ̃Ψα(e)α} = 1 − {nα} = {−nα}

So, ̃Ψα(e) = −n, for ̃Ψα(e) ∈ Z. So, ̃Ψα is surjective.
- Increase : let e, e′ ∈ Ec
(α) such that e <R e′.

— Case 1 : if e ∈ Ec
(α) and e′ ∈ E(α), then ̃Ψα(e) < 0 ⩽ ̃Ψα(e′).
— Case 2 : if e, e′ ∈ E(α), we have proved in Proposition 2 that Ψα(e) < Ψα(e′).
— Case 3 : if e, e′ ∈ Ec
(α), then :

̃Ψα(e′) − ̃Ψα(e) =
 ∞∑

k=1(e′
k − ek)qk−1 = Ψα(d
′) − Ψα(d)

where d = ((ek)k∈{1···r}, 0∞) and d
′ = ((e′
k)k∈{1···r}, 0∞), the integer r being such that e′
i = ei = ai
for i > r. Since e, e′ are α-admissible, we can claim that d, d
′ ∈ E(α). So, with Proposition 2,
Ψα(d
′) − Ψα(d) > 0. So, ̃Ψα(e′) − ̃Ψα(e) > 0.
We have proved that ̃Ψα is increasing on Fα. ■

Note that the deﬁnition of ̃Ψα in Proposition 5 could be given by the same formula for d in
E(α) and for d in Ec
(α), with the following convention : +∞ = 0, so that qn −−−→
n→∞ 0. Indeed, if
we deﬁne :
 ∀d ∈ Fα, Ψα(d) =
 ∞∑

k=1 dkqk−1

then, it is convenient, since :

∞∑

k=1 akqk−1 =
 ∞∑

k=1(qk − qk−2) = 0 + 0 − q0 − q−1 = −1

We also have, with this convention a coherent result for both ” improper expansions” of an
integer n, herited from improper expansions of {nα} ( see remark 2, below Proposition 4),
whose proper expansion is (d1, d2, · · · , dr) with dr > 0. Indeed, these improper expansions are
(d[1,r], 1, (max, 0)∞) and (d[1,r−1], dr + 1, (max, 0)∞) ( if dr < ar) or (d[1,r], 0, 1, (max, 0)∞) ( if
dr = ar). Moreover :

∀s ∈ N,
 ∞∑

j=0 as+2j+1qs+2j =
 ∞∑

j=0(qs+2j+1 − qs+2j−1) = 0 − qs−1

21

3 Complements

3.1 dynamic generating α-numeration

• What follows is inspired by the analoguous result for the usual Ostrowski numeration made
by Ito in [5] :

Proposition 6 let α be an irrational and [ak]k∈N its CFE. Let β ∈ [0, 1[ and (bk)k its α-
numeration. We have : ∀k ∈ N∗, (ak, bk) = AH k−1(α, β)

where H is a self map of the open trapezoid U deﬁned by : for (x, y) ∈ R2

(x, y) ∈ U ⇔
 {
0 < x < 1
−x < y < 1

H : (x, y) → ({ 1
x
 } , min (⌊ 1
x
 ⌋ , ⌈ y
x
 ⌉) − y
x
 )

A : (x, y) → (⌊ 1
x
 ⌋ , min (⌊ 1
x
 ⌋ , ⌈ y
x
 ⌉))

Remark 1 : we could prefer the following expressions, distinguishing two cases :

∀(x, y) ∈ U,
 {A(x, y) = (⌊1/x⌋, ⌈y/x⌉) ; H(x, y) = ({1/x}, {−y/x}) if y ⩽ x⌊1/x⌋
A(x, y) = (⌊1/x⌋, ⌊1/x⌋) ; H(x, y) = ({1/x}, {−y/x} − 1) else

Indeed, if y > x⌊1/x⌋, then : ⌊1/x⌋ < y/x < 1/x, so ⌊1/x⌋ = ⌈y/x⌉ − 1.

Remark 2 : let us verify that H(U ) ⊂ U : if y ⩽ x⌊1/x⌋, that is obvious. Else, {−y/x} − 1 =
−{y/x} > −{1/x}, for ⌊1/x⌋ < y/x < 1/x and so {y/x} < {1/x} ( see remark 1).

Proof :
we denote (αk, γk) = H k(α, β) for all k ∈ N. We avoid here the notation βk for it is used below as
reference to Algorithm 3.
We already know that ak = px(AH k−1(α, β)), where px : (x, y) → x, since T (x) = px(H(x, y)) for all
x, y ∈]0, 1[ ( T is the Gauss map, see 1.3). By deﬁnition, we have :

γ0 = β ; ∀k ∈ N∗, γk = min(ak, ⌈γk−1/αk−1⌉) − γk−1
αk−1

We denote γ′
k = βk
δk−1 , with notations of Algorithm 3 ( see 2.3). We also have :

∀i ∈ N, αi = T i(α) = δi
δi−1 so γ′
i
αi = βi
δi

Thus, according to Algorithm 3 on reals :

∀k ∈ N∗, bk = min(ak, ⌈βk−1/δk−1⌉) ; βk = bkδk−1 − βk−1

We deduce :
 ∀k ∈ N∗, γ′
k = bk − γ′
k−1
αk−1
Yet, γ′
0 = β = γ0 and we obtain, by obvious induction : γk = γ′
k for all integer k ∈ N. Then :

∀k ∈ N∗, bk = min(ak, ⌈γk−1/αk−1⌉)

This ends the proof. ■
 22

3.2 α-germs and orbits of α-rotation

Our α-numeration is related to fα, the rotation on the circle R/Z deﬁned by :

∀x ∈ R/Z, fα(x) = α + x ( mod 1)

Let α be an irrational and [ak]k its CFE. We know that fα is topologically transitive : its
orbits are dense in X = R/Z. Moreover, it is uniquely ergodic : there is only one fα-invariant (
and ergodic) measure on X : the Lebesgue measure.
Now, we will explicit the conjugate of fα on Eα, namely the map gα : Eα → Eα, such that :

Λα ◦ gα = fα ◦ Λα

We remind some notations : Eα is the set of α-admissible sequences and Fα = E(α) ∪ Ec
(α),
where

E(α) = {(dk)k ∈ Eα, ∃n ∈ N, ∀k > n, dk = 0} ; Ec
(α) = {(dk)k ∈ Eα, ∃n ∈ N, ∀k > n, dk = ak}

We will use an equivalence relation on Eα, that deﬁnes the notion of germ of a sequence :

∀d, d
′ ∈ Eα, d ≂ d
′ ⇔ ∃k ∈ N, ∀i > k, di = d
′
i

We remark that the class of (0) is E(α) and that the class of (ak)k∈N∗ is Ec
(α).
More generally, we can extend RLO to each class of germs of Eα, as follows :

(dk)k <R (d
′
k)k ⇔ ∃j ∈ N∗,
 {dj < d′
j
∀k > j, dk = d′
k

Remark : for each class of germs of Eα, RLO is a total order and every element of the class
has a successor ( except for Ec
(α), where (ak)k∈N∗ is the maximal element) and a predecessor (
except for E(α), where (0) is the minimal element).

• The following Proposition explicits the orbits of gα. Before that, we remark that : for β, β′ ∈
R/Z, β and β′ are in the same orbit of fα if and only if it exists n ∈ Z, such that β′ − β = nα
mod 1. So, an orbit of gα is the set of α-numerations of the {β + nα}, n ∈ Z, for some β ∈ [0, 1[.

Proposition 7 Let α be an irrational, [ak]k its CFE and gα deﬁned as above, then :
(i) the orbits of gα are exactly the classes of germs of Eα, except for the orbit of (0), that is Fα.
(ii) gα is the successor map on each of theses classes ( with RLO).

Proof :
First, the class of (0), via gα, is Fα, the set of α-numerations of the {nα}, n ∈ Z, as we have seen in
previous subsection 3.1.
Let β ∈ [0, 1[ such that β ̸∈ {{nα}, n ∈ Z}. We denote b = (bk)k its α-numeration and C the class of
germ of b in Eα.
If b′ ∈ C, then we have an integer r ∈ N, such that b′
i = bi for all integer i > r. We denote β′ = Λα(b′),
then :
 β′ − β =
 r∑

k=1
(b′
k − bk)δ′
k−1

but, δ′
i = αqi − pi and qi, pi are integer for all i ∈ N. So, β′ − β ∈ Z + αZ and we conclude that β′ is
in the fα-orbit of β and that b′ is in the gα-orbit of b.
Conversely, suppose that b′ is in the gα-orbit of b. We want to show that b and b′ have the same
germ. By obvious induction, it suﬃces to show that this is the case for b′ = gα(b), that is to say for
β′ = β + α. But, since b is not (ak)k, then there exists an index r such that br < ar. We denote

23

d = (b[1,r], 0∞). Then, the successor of d in (E(α), RLO) is d
′ such that d
′
i = 0 for all i > r. We claim
now that b′ = (d
′
(1,r], b[r+1,∞]). Indeed, b′ ∈ Eα and :

Λα(b′) − Λα(b) = Λα(d
′) − Λα(d) = α

So, b′ and b have the same germ.
By the way, we have also proved that gα is the successor map on the class of germ of b. ■

Remark 1 : this proves that R/(Z + αZ) is represented, via our α-numeration Λα, by germs
of sequences of Eα.

Remark 2 : we can deﬁne, on each orbit X of fα, a natural order, which makes them
isomorphic to (Z, ⩽) ( but not canonically) :

∀x, x′ ∈ X, x ⩽ x′ ⇔ ∃n ∈ N, x′ = f n
α (x)

In the same way, each class of germ of (Eα, RLO) ( except for the class of (0), where we
consider Fα) is isomorphic to (Z, ⩽).

• Now, we deﬁne, for any x in R, ||x||, the distance of x to Z. We also have : ||x|| =
min({x}, {−x}). Later, we deﬁne several maps on R by : for all β ∈ R

Dα(β) = lim inf
n→+∞(n||nα − β||) ; D+
α (β) = lim inf
n→+∞(n{nα − β}) ; D−
α (β) = lim inf
n→+∞(n{β − nα})

Remark 3 : Dα = min(D+
α , D−
α ), for lim inf ” respects” the min.

Remark 4 : these 3 maps are fα-invariant. Indeed, if x ∈ R, then :

∀n ∈ N∗, n{nα − (x + α)} = {(n − 1)α − x} = j + 1
j × j{jα − x}

where j = n − 1. But, j+1
j converges to 1 as j tends to inﬁnity, so the lim inf is the same...
This proves that these maps could be deﬁned on R/(Z + αZ), the additive group of orbits of
fα and so they only depend on the germ of the α-numeration of β ∈ R/Z. In other words, these
maps only depand on the asymptotic behaviour of the α-numeration of β.

It is well known that Dα(0) is null if and only if the sequence of partial quotients of α is
unbounded and that Dα(0) can be deﬁned, restricting n to the denominators of convergents of
α. But, we have more precise results :

lim inf
n→+∞
 ( 1
an + 2
 ) ⩽ Dα(0) ⩽ lim inf
n→+∞
 ( 1
an
 )

Moreover, Dirichlet’s theorem on diophantine approximation gives ( see [4]) :

∀β ∈ R, Dα(β) ⩽ 1

And Minkowski has proved that ( see [4] again) :

∀β ∈ R\(Z + αZ), min(Dα(β), Dα(1 − β)) ⩽ 1
4

In 4.3, we give some results that helps to compute D+
α (β) and D−
α (β), in relation to the
α-numeration of β.
 24

3.3 shift and inductive structure

• Let α be a real in [0, 1[ and [0, a1, a2, · · · ] its CFE. We denote a = (a1, · · · ) and σ the usual
shift on sequences. We have seen that : if α is not null, then [0, σ(a)] is the CFE of T1(α), where
T1 is an extension of the Gauss map, described in 1.3. We recall that µ(α) = +∞ if α is not
rational and µ(α) = r if α is rational and its CFE is [0, a1, · · · , ar, 1]. We deﬁne inductively the
sequence : (αk)k by :
 α0 = α ; ∀k ∈ {1 · · · µ(α)}, αk = { 1
αk−1
 }

With the remark above, we obtain :

∀k ∈ {0 · · · µ(α) − 1}, αk = [0, ak+1, · · · ] = [0, σk(a)]

Moreover, if α is rational and r = µ(α), then αr = 0, for αr−1 = [0, ar, 1] = 1
ar+1 .

According to the deﬁnition of the sets (Eαk )k, we can claim :

∀b ∈ Eα, ∀k ∈ N, (σk(b) ∈ Eαk ⇔ bk+1 ̸= 0 or σk(b) = (0))

In particular :
 ET (α) ⊂ σ(Eα) and σ(Eα)\ET (α) = {0} × (ET 2(α)\{(0)})

In addition, if we denote for any k ∈ {0 · · · a1 − 1} :
- Eα,k : the set of α-admissible sequences whose ﬁrst digit is k. We have Eα,0 = {(0)}.
- Eα,a1 : the set of α-admissible sequences whose ﬁrst digit is a1 and second is non null, except
for (a1, 0, 0, · · · ), that is in this set.
- E′
α,a1 : the set of α-admissible sequences whose ﬁrst digit is a1 and second is null, except for
(a1, 0, 0, · · · ), that is not in this set.

(Eα,k)k∈{0···a1} ∪ E′
α,a1 is clearly a partition of Eα and ALO induces an order on these subsets
: ( where B <A B′ means that for every b ∈ B and b′ ∈ B′, we have b <A b′)

Eα,0 <A Eα,1 <A Eα,2 <A · · · <A Eα,a1 <A E′
α,a1

Lemma 6 .
(i) for any k ∈ {1 · · · a1}, the map ( see below) is a bijective decreasing map ( induced by σ).

σk :
 {
(Eα,k, ⩽A) → (ET (α), ⩽A)
(k, d[2,∞]) → (d[2,∞])

(ii) the map ( see below) is a bijective increasing map ( induced by σ2).

σ(2) :
 {
(E′
α,a1 , ⩽A) → (ET 2(α)\{(0)}, ⩽A)
(a1, 0, d[3,∞]) → (d[3,∞])

Proof :
direct consequence of former remarks and deﬁnition of sets Eα and ALO. ■

So to say, (Eα, <A) consists in one null element, followed by a1 ordered copies of (ET (α), <A′)
and, at the end a copy of (ET 2(α)\{(0)}, <A), where <A′ denotes inversed ALO.

25

We deduce a result on Kronecker sequences :

Corollary 3 let α be a real in [0, 1[, T the usual Gauss map x → {1/x}.
We denote a1 = ⌊1/α⌋ and Kα = {{kα}, k ∈ N}.
The following union are disjoint :

Kα = α
 

{0} ∪ ⋃

j∈{1···a1}
(j − KT (α)) ∪ (a1 + T (α)(KT 2(α)\{0})





Proof :
direct consequence of Lemma 6 ■

• Now, we would like to specify the eﬀect of the shift on the integers and reals of [0, 1[, via their
α or T (α)-numerations.

We deﬁne a sequence of integers (νk)k by :

ν0 = ν ; ∀k ∈ {1 · · · µ(α) − 2}, νk =
 {
⌊νk−1αk−1⌋ if nk+1 ̸= 0 or σk(n) = (0)
⌊νk−1αk−1⌋ + 1 else

Lemma 7 let k ∈ {0 · · · µ(α) − 2} and n = (ni)i the α-numeration of ν ( we denote ν = (n)α
for example these numeration...)
⊲ Case 1 : if nk+1 ̸= 0 or σk(n) = (0), then νk = (n[k+1,∞])αk = σk(n)αk .
⊲ Case 2 : else νk = (1, n[k+2,∞])αk = (1, σk+1(n))αk .

Proof :
we will denote pk(x) and qk(x) for the reduced of the kth convergent of a real x, for any non negative

integer k and [a0(x), a1(x), · · · , ak(x), ...] its CFE. We have remarked that, if we denote T (x) = { 1
{x} }
,
then : ∀j ∈ N∗, aj(T (x)) = aj+1(x)

By obvious induction, we can deduce that :

∀x ∈ [0, 1[, ∀j ∈ N, qj−1(T (x)) = pj(x) (1)

We denote r = µ(α). Now, we will use an induction on k ∈ {0 · · · r − 2}. Result (i) is true for k = 0 (
we are in Case 1) . Suppose it is true for k − 1, where k ∈ {1 · · · r − 2}, then :

νk−1 = (n′
k, n[k+1,r])αk−1 = (n′
k, σk(n))

with n′
k = 1 or nk, but n′
k > 0 in all cases.
◮ Case 1 : if nk+1 ̸= 0 or σk(n) = (0), then : with the formula that follows the proof of Algorithm 3 and
(1) :
 νk = ⌊νk−1αk−1⌋ = n′
kp0(αk−1) +
 r∑

j=k+1 njpj−k(αk−1) =
 r∑

j=k+1 njqj−k−1(αk)

For p0(αk−1) = 0. So we obtain the αk-numeration of νk : it is σk(n) for σk(n) ∈ E(αk).
◮ Case 2 : if nk+1 = 0 and nk+2 ̸= 0, then (n[k+1,∞]) ̸∈ Eαk , but :

νk = q0 +
 r∑

j=k+2 njqj−k−1(αk)

So we obtain the αk-numeration of νk : it is (1, n[k+2,∞]) for it is in E(αk). ■

26

We also deﬁne a sequence (γk)k of reals :

γ0 = β ; ∀k ∈ {1 · · · µ(α)}, γk = 1
αk−1 (bkαk−1 − γk−1)

Lemma 8 let k ∈ {0 · · · µ(α) − 2}.
⊲ Case 1 : if bk+1 ̸= 0 or σk(b) = (0), then γk = (b[k+1,∞])αk = σk(b)αk .
⊲ Case 2 : else γk < 0 and γk+1 = (b[k+2,∞])αk+1 = σk+1(b)αk+1 .

Proof :
we will use same notations as in previous proof. First, we remark that ( by obvious induction) :

∀x ∈]0, 1[, ∀i ∈ N, qi(x) = a1(x)qi−1(T (x)) + pi−1(T (x)) ; pi(x) = qi−1(T (x))

We denote r = µ(α) and argue with induction on k. It is clear for k = 0. Suppose it is true for k − 1,
with k ∈ {1 · · · r − 2}.
— if bk ̸= 0 or σk−1(b) = (0), then γk−1 = (b[k,∞])αk−1 . So :

γk−1 =
 r∑

j=k bj[αk−1qj−k(αk−1) − pj−k(αk−1)] =
 r∑

j=k bj[αk−1(akqj−k−1(αk) + pj−k−1(αk)) − qj−k−1(αk)]

The term of the above sum for j = k is equal to bkαk−1, so :

γk = 1
αk−1 (bkαk−1 − γk−1) =
 r∑

j=k+1 bj
 [ qj−k−1(αk)
αk−1 − (akqj−k−1(αk) + pj−k−1(αk))
]

But, 1
αk−1 = ak + αk, so :
 γk =
 r∑

j=k+1 bj[αkqj−k−1(αk) − pj−k−1(αk)]

Case 1 : bk+1 ̸= 0 or bk+2 = 0 : we recognize the αk-numeration of γk, since (b[k+1,r]) ∈ Eαk , with our
hypothesis.
Case 2 : bk+1 = 0 and bk+2 ̸= 0, then (b[k+1,r]) ̸∈ Eαk and :

γk =
 r∑

j=k+2 bj[αkqj−k−1(αk) − pj−k−1(αk)]

so :

γk+1 = − γk
αk =
 r∑

j=k+2 bj
 [ pj−k−1(αk)
αk − qj−k−1(αk)
] =
 r∑

j=k+2 bj[αk+1qj−k−2(αk+1) − pj−k−2(αk+1)]

the last equality is obtained as above in Case 1...
Now, (b[k+2,r]) ∈ Eαk+1 and γk+1 = (b[k+2,r])αk+1 . We deduce that γk+1 ∈]0, 1[ and γk < 0.

— if bk = 0 and bk+1 ̸= 0, then, with induction hypothesis, we obtain the result since we are in Case 1.
■
 27

4 Order properties of Kronecker sequences

4.1 a one-page proof of the ”three distance theorem”

In this section, we will be interested in lengths of subdivisions of [0, 1] by ﬁnite sets {{kα}, k ∈
{1 · · · N − 1}}, where α is a real in [0, 1[ and N a positive integer.
Let us remark that, if we consider subdivisions of the circle S1, that is to say of R/Z, then
their lengths are invariant by translations. In that case, subdivisions by sets like {{kα + β}, k ∈
{0 · · · N − 1}} are the same, from a metric point of view, for all real β.

The well known 3 distance theorem ( see [7]) claims that these subdivisions are quite simple
: they all contains at most 3 diﬀerent lengths, one being the sum of the others :

Let α be a real in [0, 1[, with CFE [ak]k. We denote, as usual, pn/qn the reduced fraction of
the convergent [a0, · · · , an] and δn = (−1)n(αqn − pn). We remind that (δn)n is a positive and
decreasing sequence that converges towards 0 ( if α is irrational).
Let N be a positive integer. If α is rational, we suppose that N ⩽ q, where q is the denominator
of the reduced fraction of α. So, the set {{kα}, k ∈ {0 · · · N − 1}} contains exactly N elements.

Theorem 1 ( 3 distance theorem) .
the set {{kα}, k ∈ {1 · · · N − 1}} divides [0, 1] into N intervals of length taking at most 3 values,
one being the sum of the others.
We can precise a bit : let s be the lowest integer such that N ⩽ qs + qs−1, then :
- if N = qs + (1 − i)qs−1, with i ∈ {0 · · · as − 1}, the lengths of above intervals take 2 values :

δs + iδs−1 and δs−1

- if N ̸= qs + (1 − i)qs−1, with i ∈ {0 · · · as − 1}, the lengths of above intervals take 3 values :

δs−1, δs + iδs−1 and δs + (i + 1)δs−1

Proof :
According to propositions 2 and 4, algorithm 1 and 3, we can write : N −1 = (n1, · · · , ns)α, with ns ̸= 0.
Let denote (uj)j∈{0···N −1} the increasing sequence that enumerates our set {{kα}, k ∈ {0 · · · N − 1}}. We
have u0 = 0 and denote uN = 1. The aim of this result is to prove that uj − uj−1 take at most 3 values,
when j ranges over {1 · · · N }.
We will denote E(N ) the set of α-admissible sequences that are lower or equal, for RLO, than (ni)i.
These sequences are the α-numeration of integers of {0 · · · N − 1}. Let k ∈ {1 · · · N − 1}, then k =
(k1, · · · , kr)α, (ki)i ∈ E(N ) and kr > 0. So, 1 ⩽ r ⩽ s.
We denote j the integer such that uj = {kα}. Then uj−1 = {k′α}, where k′ = ((k′
i)i)α and (k′
i)i is the
predecessor of (ki)i in (E(N ), ALO). In a similar way uj+1 = {k”α}, where k” = ((k”i)i)α and (k”i)i is
the successor of (ki)i in (E(N ), ALO).
We will suppose that s is even, because the other case can easily be deduced ( see end of the proof).
◮ Case 1 : if r is odd. Then k′ = (k[1,r], 1, (max, 0)
ν)α, where ν = s−r−1
2 . So, more explicitly :

(k′
i)i = (k1, · · · , kr−1, kr, 1, ar+2, 0, ar+4, 0, · · · , as−1, 0)

So :
 uj − uj−1 = δr −
 s−1∑

i=r+2;i odd aiδi−1 = δr −
 s−1∑

i=r+2;i odd(δi−2 − δi) = δs−1

◮ Case 2 : if r is even. Then, we deﬁne K = (k[1,r−1], kr + 1, (max, 0)
ν), where ν = s−r
2 .
◮◮ subcase 1 : if K ∈ E(N ), then K is the predecessor of (ki)i in (E(N ), ALO) and :

uj − uj−1 = δr−1 −
 s−1∑

i=r+1;i odd aiδi−1 = δr−1 −
 s−1∑

i=r+1;i odd(δi−2 − δi) = δs−1

28

◮◮ subcase 2 : if K ̸∈ E(N ). We have then 2 subsubcases :
◮◮◮ subsubcase 1 : if r < s, then kr = ar. We denote K ′ = (k[1,r], 0, 1, (max, 0)
ν)α, where ν = s−r−2
2 .
Then, K ′ ∈ E(N ) and K ′ is the predecessor of (ki)i in (E(N ), ALO). So :

uj − uj−1 = δr+1 −
 s−1∑

i=r+3;i odd aiδi−1 = δr+1 −
 s−1∑

i=r+3;i odd(δi−2 − δi) = δs−1

◮◮◮ subsubcase 2 : if r = s then ks = ns or (ks = ns − 1 and (k[1,s−1]) >R (n[1,s−1]).
We denote t the greatest odd integer i such that ki > 0. So k = (k[1,t], (max, 0)
ν, ks)α, where ν = s−t−1
2 .
Then, the predecessor of (ki)i in (E(N ), ALO) is (k[1,t−1], kt − 1). So :

uj − uj−1 = δt−1 − ksδs−1 −
 s−2∑

i=t+1;i even aiδi−1 = δt−1 − ksδs−1 −
 s−2∑

i=t+1;i even
(δi−2 − δi) = δs−2 − ksδs−1

N.B : r = s and ks = ns is valid for k = N − 1. But, r = s, ks = ns − 1 and (k[1,s−1]) >R (n[1,s−1])
is possible for at least one k < N if and only if (n[1,s−1]) ̸= (max
s−1). That is to say if and only if :
N ̸= qs + qs−1 − (as − ns)qs−1 = qs−2 + (ns + 1)qs−1.
So, the length δs−2 − nsδs−1 always occur in our subdivision, but the length δs−2 − (ns − 1)δs−1 occur
if and only if N ̸= qs−2 + (ns + 1)qs−1. We put i = as − ns and obtain the conditions of Theorem 1.

◮ Case 3 : the last interval. What about 1 − uj, where j = (K)α and K is the greatest element of
(E(N ), ALO) ? Then K = ((max, 0)
s/2), so :

1 − uj = 1 −
 s−1∑

i=1;i odd aiδi−1 = 1 −
 s−1∑

i=1;i odd(δi−2 − δi) = 1 − δ−1 + δs−1 = δs−1

So, the case s even is proven !

If s is odd, we use similar arguments, replacing ”predecessor” by ” successor” and ”uj − uj−1 ” by
”uj+1 − uj”. ■
 29

4.2 order coincidence of ({nα})n and ({nα′})n

• Let α and α′ be two diﬀerent reals in [0, 1). We look for the greatest N such that ({nα})n∈{0···N −1}
and ({nα′})n∈{0···N −1} are in the same order in the following meaning :

({nα})n∈I is in the same order than ({nα
′})n∈I if and only if (∀n, n′ ∈ I, {nα} < {n′α} ⇔ {nα
′} < {n′α
′})

where I is an interval of Z.
This property is related with another one, concerning integral parts :

Lemma 9 let α, α′ ∈ R and N a positive integer. The following assertions are equivalent :
(i) ({nα})n∈{0···N −1} and ({nα′})n∈{0···N −1} are in the same order.
(ii) ∀n ∈ {0 · · · N − 1}, ⌊nα⌋ = ⌊nα′⌋

Proof :
Let n, n′ ∈ {0 · · · N − 1} such that n < n′. We denote d = n′ − n ∈ {0 · · · N − 1}. Then :

⌊n′α⌋ = ⌊dα⌋ + ⌊nα⌋ + ǫ where ǫ ∈ {0, 1}

so : {n′α} − {nα} = {dα} − ǫ

thus, the sign of {n′α} − {nα} only depends on ǫ. We have the same equalities and remark with α
′ and
ǫ′ instead of α and ǫ.
(ii) ⇒ (i) : suppose that (ii) is true. Then, with above notations, we have ǫ = ǫ′, so {n′α} − {nα} and
{n′α
′} − {nα
′} have the same sign.
(i) ⇒ (ii) : suppose that (ii) is false. Then we have an integer ν ∈ {1 · · · N − 1} such that :

∀k ∈ {0 · · · ν − 1}, ⌊kα⌋ = ⌊kα
′⌋ and ⌊να⌋ ̸= ⌊να
′⌋

suppose that α < α
′, then : ⌊να⌋ < ⌊να
′⌋. If we denote n′ = ν, n = ν − 1 and d = 1, then, with above
notations : ǫ = 0 and ǫ′ = 1, so {n′α} − {nα} and {n′α
′} − {nα
′} do not have the same sign. ■

• Suppose that α is a real and p/q is a convergent of α. We claim that :

∀n ∈ {0 · · · q − 1}, ⌊nα⌋ = ⌊ np
q
 ⌋

Indeed : ∣
∣
∣α − p
q ∣
∣
∣ < 1
q2 , so : ∀n ∈ {1 · · · q − 1}, ∣
∣
∣nα − n p
q ∣
∣
∣ < 1
q . But, {n p
q } ∈ [ 1
q , 1 − 1
q ], since p

and q are coprime, so ⌊nα⌋ = ⌊ np
q ⌋
.

• Is this result still valid for semi-convergents instead of convergents ? for other reduced rationals
? The following result gives the answer...and a bit more.

Proposition 8 .
(i) let α and α′ be two reals such that 0 < α < α′ < 1. We denote γ the best rational in ]α, α′]
and q the denominator of its reduced fraction. Then

q = max{N ∈ N, ∀n ∈ {0 · · · N − 1}, ⌊nα⌋ = ⌊nα
′⌋}

(ii) let α be a real in [0, 1) and p/q a reduced fraction, with q ∈ N∗, such that α is not the
nearest left strict convergent of p/q.

p/q is a semi-convergent of α ⇔ ∀k ∈ {0 · · · q − 1}, ⌊kα⌋ = ⌊kp/q⌋

30

Remark : for a positive integer n, we have ⌊nα⌋ < ⌊nα′⌋ if and only if there exists an integer
p such that α < p/n ⩽ α′.

Proof :
(i) is a consequence of the remark.

(ii) the best rational in ←→
[α, p/q] is the common semi-convergent of α and p/q, that has the greatest de-
nominator ( see Proposition 1 (iii)). But, semi-convergents of p/q are either p/q or p′/q′ where p′, q′ are
integers such that 1 ⩽ q′ < q. So, we have two cases.
If p/q is a semi-convergent of α, then there are no integers a, b such that b ∈ {1 · · · q − 1} and
α < a/b ⩽ p/q or p/q < a/b ⩽ α. The previous remark implies ⇒ of (ii).

If p/q is not a semi-convergent of α, then the best rational in ←→
[α, p/q] is p′/q′ with p′, q′ two integers such
that 0 < q′ < q. If p/q < α then p/q < p′/q′ ⩽ α and we use remark 2. Else, since α is not the nearest
left strict convergent of p/q, we have p”, q” two integers such that α < p”/q” < p/q and 0 < q” < q. We
conclude with remark 2. ■

• We also have direct consequences for sums of ⌊kα⌋ and {kα} : we will denote

∀n ∈ N, ∀x ∈ R, In(x) =
 n−1∑

k=0⌊kx⌋ ; Fn(x) =
 n−1∑

k=0{kx}

Obviously, Fn is 1-periodic, In is non decreasing and :

∀n ∈ N, ∀x ∈ R, In(x) + Fn(x) = n(n − 1)x
2 (1)

Moreover, let p, n be 2 positive integers and d = gcd(p, n). We denote n′ = n/d and p′ = p/d.
Then n′ and p′ are coprime, so {{ kp′
n′ } , k ∈ {0 · · · n′ − 1}
} = { j
n′ , j ∈ {0 · · · n′ − 1}
}. So, we

have, since ({ kp′
n′ })
k is n′-periodic :

∀p, n ∈ N∗, Fn ( p
n
 ) = n − gcd(p, n)
2 (2)

We also have, for two reals x and x′ :

In(x) = In(x′) ⇔ ∀k ∈ {0 · · · n − 1}, ⌊kx⌋ = ⌊kx′⌋

So, Proposition 8 gives : In(x) = In(x′) if and only if n is lower or equal to the denominator
of the reduced best rational in ]x, x′], if x < x′.
In [2], we can ﬁnd an expression of In(x) and Fn(x) in terms of the Ostrowski x-numeration
of n. In what follows, we restrict ourselves to a special case :

Corollary 4 Let α be a real and p/q a fraction of integers, such that α is not the nearest left
strict convergent of p/q.

p
q a reduced semi-convergent of α ⇔
 q−1∑

k=0⌊kα⌋ = (p − 1)(q − 1)
2

Proof :
direct consequence (1),(2) and Proposition 8 (ii). ■

Remark : we deduce an expression of the mean value of ({kα})1⩽k<q if p
q is a reduced
semi-convergent of α : 1
q − 1
 q−1∑

k=1{kα} = 1
2 + qα − p
2

31

4.3 best left or right α-approximation of a real in [0, 1[

Let α be a real, [ak]k∈N∗ its CFE and r = µ(α), the CFE-depth of α. So, we denote
[a0, a1, · · · , ar, 1] the CFE of α if α is rational. We also denote (pn/qn)n the usual sequence
of convergents of α. We consider points of R2 with the product order : (x, y) ⩽ (x′, y′) if and
only if x ⩽ x′ and y ⩽ y′.
We recall some notations mentioned at 3.2 : for any x in R, ||x||, the distance of x to Z. We
also have : ||x|| = min({x}, {−x}).

Deﬁnition 6 ( best α-approximation of a real) .
let α and β be two reals in [0, 1[ and n a non negative integer.
⊲ {nα} is a best α-approximation of β if and only if :

∀k ∈ {0 · · · n − 1}, ||nα − β|| < ||kα − β||

⊲ {nα} is a best right ( resp. left) α-approximation of β if and only if :

∀k ∈ {0 · · · n − 1}, {nα − β} < {kα − β} ( resp. {β − nα} < {β − kα})

Remarks : we could also consider approximations of β by nα mod 1, for negative integers n.
Best sided α-approximations of a real are easier to describe than best α-approximations. But,
there is a simple relation : a best α-approximation is also a best right or left α-approximation
of β.
First, we remark that these notions are closely related to minimal points in R2 of sequences
({nα − β}, n)n∈N and ({β − nα}, n)n∈N : best right ( resp. left) α-approximations of β are
obtained for the values of n such that ({nα − β}, n) ( resp. ({β − nα}, n)) is a minimal point of
the sequence ({kα − β}, k)k∈N ( resp. ({β − kα}, k)k∈N).
Moreover :
 ∀x ∈ R, {x − β} =
 {
{x} − β ∈ [0, 1 − β[ if {x} ⩾ β
{x} + 1 − β ∈ [1 − β, 1[ if {x} < β

Finally : (1 − β, 0) is a trivial minimal point of ({nα − β}, n)n∈N, so the other minimal points
must verify {nα} ⩾ β.

Proposition 9 (best right ( positive) α-approximations) .
⊲ Case 1 : α is rational and [0, a1, · · · , ar, 1] is its CFE. We suppose that β ∈ {{nα}, n ∈ N}
and denote (b1, b2, · · · , br) the α-numeration of β ( see 2.2).

Best right ( positive) α-approximations of β are the {nα} for n = 0, for n = r∑

i=1 biqi−1 and for

the following n :

n =
 2k−1∑

i=1 biqi−1 + jq2k−1 ; j ∈ {0 · · · b2k − 1} ; k ∈ {1 · · · ⌊r/2⌋}

⊲ Case 2 : if α is irrational and [ak]k∈N is its CFE. Let β be a real in [0, 1[ and (bk)k∈N∗ its
α-numeration. ( see 2.3)

Best right ( positive) α-approximations of β are the {nα} for n = 0, for n = s∑

i=1 biqi−1, if

bk = 0 for all integer k > s, and for the following n :

n =
 2k−1∑

i=1 biqi−1 + jq2k−1 ; j ∈ {0 · · · b2k − 1} ; k ∈ N∗

32

Proof :
We denote t = min({i, b2i ̸= 0}), except if all b2i are null : we then denote t the greatest integer i such
that b2i−1 ̸= 0: so we have, in that case, b = (max, 0)
t. Then, for all cases ( see deﬁnition of E(α)), we
have : b2t−1 ̸= 0 ; b = ((max, 0)
t−1, b[2t−1,∞])

Following last remarks above Proposition 9, we need the α-numeration, say ν, of the least integer n such
that {nα} ⩾ β. According to Proposition 2,3,4, it is the minimum of elements d of E(α) for RLO, such
that d ⩾A b. We claim that ν = b[1,2t−1]. Indeed, the condition d ⩾A b implies that

d[1,2t−2] = (max, 0)
t−1 = b[1,2t−2] and d2t−1 ⩾ b2t−1

But, b[1,2t−1] is minimal ( for RLO) among these one and satisﬁes ν ⩾A b.
Now, if we denote n1 = Ψα(ν) this least integer n such that {nα} ⩾ β, then :

∀n < n1, {nα − β} ∈ [1 − β, 1[ ; {n1α − β} ∈ [0, 1 − β[

So, for the product order in Z
2 :

∀n ∈ {1 · · · n1 − 1}, (1 − β, 0) < ({nα − β}, n)

Hence, no points ({nα − β}, n) is minimal, for n ∈ {1 · · · n1 − 1}.
If bk = 0 for all integer k ⩾ 2t, then ν = b and {n1α − β} = 0, so this gives the only minimal point (
with n = 0).
For the other cases : if n ⩾ n1, let denote d its α-numeration. Then, the minimality condition for
({nα − β}, n) is equivalent to : d ⩾A b and d is minimal among these ( elements of Eα greater than b for
ALO) for the product of orders (ALO,RLO).
Of course, ν is the ﬁrst ( for RLO) of these minimal ( for (ALO,RLO)) elements. The next one ( for RLO)
must satisfy : d <A ν and d is minimal for RLO : it gives the successive (b[1,2t−1], j), j ∈ {0 · · · b2t − 1}
and then (b[1,2t+1], j), j ∈ {0 · · · b2t+2 − 1} if b2t+2 ̸= 0 ( but this is still true, if b2t+2 = 0 !), and so on...■

• we have a similar result for best left ( positive) α-approximations :

Proposition 10 (best left ( positive) α-approximations) .
⊲ Case 1 : α is rational and [0, a1, · · · , ar, 1] is its CFE. We suppose that β ∈ {{nα}, n ∈ N}
and denote (b1, b2, · · · , br) the α-numeration of β.

Best left ( positive) α-approximations of β are the {nα} for n = r∑

i=1 biqi−1 and for the following

n :
 n =
 2k∑

i=1 biqi−1 + jq2k ; j ∈ {0 · · · b2k+1 − 1} ; k ∈ {0 · · · ⌊(r − 1)/2⌋}

⊲ Case 2 : α is an irrational and [ak]k∈N is its CFE. Let β be a real in [0, 1[ and (bk)k∈N∗ its
α-numeration.
Best left ( positive) α-approximations of β are the {nα} for n = s∑

i=1 biqi−1, if bk = 0 for all

integer k > s, and the following n :

n =
 2k∑

i=1 biqi−1 + jq2k ; j ∈ {0 · · · b2k+1 − 1} ; k ∈ N

Proof :
the proof is similar to those of previous Proposition. ■

33

4.4 measure of repartition of ({kα})0⩽k<ν

• If α is an irrational, we know that the sequence of probability measures (µn)n deﬁned as below
converges ( for weak-star topology) to the Lebesgue measure.

∀ν ∈ N∗, µν = 1
ν
 ν−1∑

k=0 D{kα}

where Dx is the Dirac-measure in x.
Can we precise these measures ? That is the aim of the following study. It is suﬃcient to
give an expression of µν([0, β[), where β is any real of [0, 1[. So, we want to count integers k in
{0 · · · ν − 1}, such that, given a real β in [0, 1[, we have {kα} < β.

• Another approach of this question is the following : note L the lattice in R2 generated by
(1, 0) and (α, 1). What is the cardinality of L ∩ R, if R is the rectangle : R = [0, β[×[0, ν[ ?

• For two reals α and β in [0, 1[ and for a positive integer ν, we denote n = (nk)k and b = (bk)k
the respective α-numeration of ν and β. We denote σ the usual shift on sequences. We will also
use the two total orders on ﬁnite sequences of reals : RLO, denoted ⩽R and ALO, denoted ⩽A
( see 1.2 and 2.3).
We also denote :

N (α, β, ν) = {k ∈ {0 · · · ν − 1}, {kα} < β} ; E(α, β, ν) = {d ∈ E(α), d <R n and d <A b}

With the results of section 2.3. we can claim that : Ψα gives a one to one correspondance
between N (α, β, ν) and E(α, β, ν). We will denote C(α, β, ν) the cardinality of these ﬁnite sets.
We will denote α = [ak]k∈N the CFE of α ( with a0 = 0) and r the CFE depth of α ( r = +∞
if and only if α is irrational). We suppose ν ⩽ q if α is a rational and p/q is a reduced fraction
that represents α. As in section 3.3, we use the following notations :

α0 = α ; ∀k ∈ {1 · · · r}, αk = { 1
αk−1
 }

ν0 = ν ; ∀k ∈ {1 · · · r − 2}, νk =
 {⌊νk−1αk−1⌋ if nk ̸= 0 or nk+1 = 0
⌊νk−1αk−1⌋ + 1 else

β0 = β ; ∀k ∈ {1 · · · r}, βk = 1
αk−1 (bkαk−1 − βk−1)

Remark 1 :

d ∈ E(α) ⇔ d = (0) or
 {
d1 ∈ {1 · · · a1}
σ(d) ∈ E(α1) or
 



d1 = a1
d2 = 0
σ2(d) ∈ E(α2)\{(0)}

These three cases are exclusive.

Remark 2 : let d ∈ E(α), then :

d <R n ⇔ σ(d) <R σ(n) or (σ(d) = σ(n) and d1 < n1)

d <A b ⇔ d1 < b1 or (d1 = b1 and σ(b) <A σ(d))

34

Proposition 11 we denote n = (nk)k the α-numeration of ν and b = (bk)k the α-numeration
of β. We denote s the minimum of the lengths of n and b, when we drop the eventual inﬁnite ”
0-tail”. So, ns or bs is not null, but σs(n) or σs(b) is the null sequence.

C(α, β, ν) =
 s∑

i=1(−1)
i−1[biνi + τi + ǫi − ǫ′
i]

τi =
 {
1 if nini+1 = 0 and σi(n) ̸= (0)
min(bi, ni) else

ǫi =
 {
1 if bi < ni and σi(b) <A σi(n)
0 else ǫ′
i =
 {
1 if σi(b) <R σi(n)
0 else

Proof :
we want to enumerate sequences d of E(α) such that d <R n and d <A b. We will consider several cases
and subcases, depending on the cancellation of the bi and ni...
First, we remark that b1 > 0 and n1 > 0, for we can suppose that b ̸= (0) and n ̸= (0).
◮ Case 1 : b2 > 0.
◮◮ subcase 1 : n2 > 0 or σ(n) = (0). Let us count sequences d as follows :
— if d1 = 0, then d = (0) ∈ E(α, β, ν) for n ̸= (0) and b ̸= (0) : 1 sequence.
— if 0 < d1 < b1. Then d <A b. So d ∈ E(α, β, ν) if and only if d <R n.
—— if σ(d) = σ(n) and d1 < n1, this gives, exactly min(b1, n1) − 1 sequences d.
—— if σ(d) <R σ(n), this gives, for every d1 ∈ {1 · · · b1 −1}, ν1 possible sequences d, according to Lemma
6 : so, we have ν1(b1 − 1) sequences d for this subcase.
— if d1 = b1, then, d ∈ E(α, β, ν) if and only if d <R n and σ(d) >A σ(b).
—— if σ(d) = σ(n), this gives a unique sequence d = (b1, σ(n)) if and only if b1 < n1 and σ(n) >A σ(b)
( because n2 ̸= 0, so (b1) ⊔ σ(n) ∈ E(α)) and no sequences d else. This gives ǫ1 sequences.
—— if σ(d) <R σ(n). Since d1 is ﬁxed ( d1 = b1), counting these sequences is the same, according to
Lemma 6, as counting sequences u of E(α1) ( since d2 can not be null if σ(d) >A σ(b)) such that u <R σ(n)
and u >A σ(b). But,σ(n) is the α1- numeration of ν1 ( see Lemma 7) and σ(b) is the α1-numeration of
β1 ( see Lemma 8). So, we obtain ν1 − C(α1, β1, ν1) − ǫ′
1 sequences d for this subcase, where ǫ′
1 = 1 if
and only if u can be equal to σ(b), so if and only if σ(b) <R σ(n) and 0 else.

If we summarize this subcase, we obtain :

C(α0, β0, ν0) = ν1b1 + min(b1, n1) + ǫ1 − ǫ′
1 − C(α1, β1, ν1)

◮◮ subcase 2 : n2 = 0 and σ(n) ̸= (0).
— if d1 = 0 : 1 sequence for d = (0).
— if 0 < d1 < b1, this is the same count as in the previous subcase, except that : we have σ(n) = (0, n[3,∞])
with n3 ̸= 0, so σ(n) is not a possible value for σ(d) ∈ E(α1) if d1 < b1 ( for b1 ⩽ a1). So, we must
replace min(b1, n1) by 1 : this is the role of τ1. Furthermore, the condition σ(d) <R σ(n) is equivalent
to σ(d) <R (1, n[3,∞]) = (1, σ2(n)) that is the α1-numeration of ν1 : so this gives τ1 − 1 + ν1(b1 − 1)
sequences.
— if d1 = b1, we have n2 = 0, so u <R σ(n) is equivalent to u <R (1, σ2(n)) and (1, σ2(n)) is the α1-
numeration of ν1. As above, we obtain ν1 − C(α1, β1, ν1) − ǫ′
1 sequences d for this subcase. Now, with all
previous arguments, we obtain C(α1, β1, ν1) = ν2b2 + τ2 + ǫ2 − ǫ′
2 − C(α2, β2, ν2), but ν1 = (1, σ2(n))α1
and n2 = 0, so we must replace 0 by 1 for the value of n2 in the formula for τ2 and ǫ2. But, it does not
change the result, for b2 ̸= 0 ! At the end, ν2 = (σ2(n))α2 , so the induction goes on.

If we summarize this subcase, we obtain ( here ǫ1 = 0) :

C(α0, β0, ν0) = ν1b1 + τ1 + ǫ1 − ǫ′
1 − (ν2b2 + τ2 + ǫ2 − ǫ′
2) + C(α2, β2, ν2)

◮ Case 2 : if b2 = 0 and σ(b) ̸= 0. Then b1 = a1. We can copy all arguments given in Case 1, except if
d1 = b1 and σ(d) <R σ(n) : indeed, σ(b) is not the α1-numeration of β1 ( for β1 < 0 and σ(b) ̸∈ Eα1 ). But,
σ2(b) is the α2-numeration of β2 ( see Lemma ...). So, we must look for a formula between C(α0, β0, ν0)

35

and C(α2, β2, ν2). Moreover, σ(d) >A σ(b) if and only if d2 > 0 or (d2 = 0 and σ2(d) <A σ2(b)).
— if d2 > 0, then counting these sequences is the same as counting sequences d such that d2 > 0 and
σ(d) <R σ(n), so counting sequences u ∈ E(α1) such that u ̸= (0) and u <R σ(n). With the same
arguments as in Case 1 ( separating 2 cases : if n2 is null or not), we obtain ν1 − 1 such sequences.
— if d2 = 0. We will study 3 subcases, depending on n2 and n3 :
◮◮ subcase 1 : if n2 = 0, then we count sequences d such that σ2(d) <R σ2(n) and σ2(d) <A σ2(b).
So, we obtain C(α2, β2, ν2) such sequences, because σ2(n) and σ2(b) are the α2-numeration of ν2 and β2
respectively.
◮◮ subcase 2 : if n2 ̸= 0 and ( n3 ̸= 0 or σ2(n) = (0)), then we count sequences d such that
σ2(d) ⩽R σ2(n) : we obtain C(α2, β2, ν2) + ǫ”1 such sequences, with ǫ”1 = 1 if σ2(n) <A σ2(b), ǫ”1 = 0
else...( σ2(n) and σ2(b) are still the α2-numeration of ν2 and β2 respectively).
◮◮ subcase 3 : if n2 ̸= 0, n3 = 0 and σ3(n) ̸= (0), then σ2(n) is not the α2-numeration of ν2 : it is
(1, σ3(n)). Now, σ2(d) ⩽R σ2(n) is equivalent to σ2(d) <R (1, σ3(n)), so we obtain C(α2, β2, ν2) se-
quences d ( see Lemma 7 again).

If we summarize this case 2 :

C(α0, β0, ν0) = ν1b1 + τ1 + ǫ1 − 1 + ǫ”1 + C(α2, β2, ν2)

where ǫ”1 = 1 if n2 ̸= 0, (n3 ̸= 0 or σ2(n) = (0)) and σ2(n) <A σ2(b). ǫ”1 = 0 else.

Now, let us summarize and generalize all cases :
for all i ∈ {1 · · · s − 1} : ( we have σi(b) ̸= (0))
- if bi+1 > 0, then : C(αi−1, βi−1, νi−1) = νibi + τi + ǫi − ǫ′
i − C(αi, βi, νi).
- if bi+1 = 0 and σi(b) ̸= (0), then : C(αi−1, βi−1, νi−1) = νibi + τi + ǫi + ǫ”i + C(αi+1, βi+1, νi+1) − 1,
where ǫ”i = 1 if ni+1 ̸= 0, (ni+2 ̸= 0 or σi+1(n) = (0)) and σi+1(n) <A σi+1(b) and 0 else.
We claim that : ǫ”i − 1 = −ǫ′
i + ǫ′
i+1 − ǫi+1 − τi+1

— if ni+1 = 0, then ǫi+1 = 0, τi+1 = 1 and σi(b) <R σi(n) ⇔ σi+1(b) <R σi+1(n), so ǫ′
i = ǫ′
i+1. Moreover,
ǫ”i = 0, so the equality is true.
— if ni+1 > 0 , then σi(b) <R σi(n) ⇔ σi+1(b) ⩽R σi+1(n).
If σi+1(b) = σi+1(n), then ǫi+1 = 0, τi+1 = 0, ǫ′
i = 1, ǫ′
i+1 = 0 and ǫ”i = 0, so the equality is true.
If σi+1(b) ̸= σi+1(n), then ǫ′
i = ǫ′
i+1. If ni+2 ̸= 0 or σi+1(n) = (0) then ǫ”i = 1 − ǫi+1 and τi+1 = 0.
Else, ǫi+1 = 0 ( for bi+2 ̸= 0),ǫ”i = 0 and τi+1 = 1. In both cases, the equality is true.

From this equality, we deduce that : if bi+1 = 0, and σi(b) ̸= (0), then

C(αi−1, βi−1, νi−1) = νibi + τi + ǫi − ǫ′
i − (νi+1bi+1 + τi+1 + ǫi+1 − ǫ′
i+1) + C(αi+1, βi+1, νi+1)

So, the induction formula for bi+1 > 0 can be generalized to all cases and we conclude with : if s = 1, then
n = (n1) or b = (b1). In the ﬁrst case, ν1 = 0 and C(α, β, ν) counts the d = (d1) such that 0 ⩽ d1 < n1
and d1 < b1. So C(α, β, ν) = min(b1, n1) = τ1 and ǫ1 = 0 = ǫ′
1, since σ(n) = (0). In the second case, we
have σ(b) = (0) ̸= σ(n). Our former arguments give : C(α, β, ν) = b1ν1 + τ1 + ǫ1 − 1 and ǫ′
1 = 1. This is
the initialization of our induction. ■

• We can deduce similar results for conditions with large inequalities instead of strict ones.
For example : if we denote C ′(α, β, ν) = #{k ∈ {0 · · · ν}, {kα} ⩽ β}, then :

C ′(α, β, ν) = C(α, β, ν) + D

where : D = 1n⩽Ab + 1b⩽Rn − 1n=b

Indeed, if we denote E′(α, β, ν) = {d ∈ E(α), d ⩽R n, d ⩽A b}, then C ′(α, β, ν) is the number
of elements of E′(α, β, ν). This set is E(α, β, ν) plus the element n if and only if n ⩽A b, plus
the element b if and only if b ⩽R n... if n = b, we have to count once this element.

36

5 References

[1] V Berth´e : ” autour du syst`eme de num´eration d’Ostrowski”, Bull. Belg. Math. Soc. 8
(2001), 209-238

[2] T.C. Brown and P.J.-S. Shiue : ” sums of fractional parts of integer multiples of an irra-
tional”, J.Number Theory 50 (1995), 181-192.

[3] E.Cabanillas : ” quotients of numerical semigroups generated by two numbers”, hal-02097473
and Arxiv 1904.08240 ( 2019)

[4] J. W. S. Cassels : ” an introduction to Diophantine approximation”, Cambridge, Cambridge
University Press, 1957.

[5] S. Ito : ”some skew product transformations associated with continued fractions and their
invariant measures” , Tokyo J. Math. 9 (1986), 115-133.

[6] Ostrowski : ” bemerkungen zur Theorie der Diophantischen Approximationnen I,II” , Abh.
Math. Sem Hamburg I ( 1922), 77-98 and 250-251

[7] V. T. S S`os : ”on the distribution mod 1 of the sequence n α”, Ann. Univ. Sci. Budapest,
Eotvos Sect. Math. 1 (1958), 127-134.
 37
