<!-- source: https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=190&what=fullteng&option_lang=eng | converted from PDF -->

Izvestiya: Mathematics 62:4 723–772 c⃝1998 RAS(DoM) and LMS

Izvestiya RAN: Ser. Mat. 62:4 81–136 UDC 511

An explicit lower bound for a homogeneous rational
linear form in logarithms of algebraic numbers

E. M. Matveev

Abstract. In this paper we study linear forms Λ = b1 ln α1 + ··· + bn ln αn with
rational integer coeﬃcients bj (bn ̸=0, n ⩾ 2), where the αj are algebraic numbers
satisfying the so-called strong independence condition. In standard notation, we
prove an explicit estimate of the form

|Λ| > exp(
−CnDn+2Ωln(
CnDn+2Ω
′) ln(eB))
.

Its novel feature is that it contains no factors of the form n
n.

§ 1. Introduction

Consider a ﬁeld K,[K : Q]= DK, and numbers β0,...,βn ∈ K, α1,...,αn ∈
K∗ = K\{0}. In the general case, the theory of linear forms in logarithms studies
expressions of the form
 Λ= β0 + β1 ln α1 + ··· + βn ln αn, (1.1)

and in the so-called homogeneous rational case it studies expressions of the form

Λ= b1 ln α1 + ··· + bn ln αn, (1.2)

where bj = βj ∈ Z.
We always assume that Λ ̸=0 and βn ̸=0. We have n ⩾ 1 in the general case
and n ⩾ 2 in the homogeneous rational case.
This theme has recently been thoroughly investigated both because of its numer-
ous applications and because it has yielded fruitful ideas, connected mainly with
the names of Gelfond, who laid down the foundations of the method, and Baker,
who suggested a decisive improvement. A brief history of this problem up to 1976
can be found in [1] along with the explicit estimates

|Λ| > exp
(
−C1Ω(ln Ω
′)ln(BΩ)
) (1.3)

This work was partially supported by an individual grant from the Soros Foundation.
AMS 1991 Mathematics Subject Classiﬁcation. 11J86, 11J25.

724 E. M. Matveev

in the general case and
 |Λ| > exp
(
−C1Ω(ln Ω
′)ln B) (1.4)

in the homogeneous rational case. Here we use the following notation:

Aj ⩾ max{
4, ln H(αj)
}
, 1 ⩽ j ⩽ n,

Ω= A1 ... An, Ω
′ = A1 ...An−1,A1 ⩽ ··· ⩽ An,

B ⩾ max{
4,H(β1),...,H(βn)
},C1 =(16nD)
200n,D = DK,

and H(α) is the usual height of an algebraic number α, that is, the maximum of the
absolute values of the coeﬃcients in the minimal polynomial of α over Z. Moreover,
Baker used the principal values of the logarithms.

Remark. Other authors denote by Aj the exponentials of our Aj , which forces them
to write ln Aj instead of our Aj.
It was realized that, in the case of so-called strong independence of α1,...,αn,
the constant C1 can be considerably improved, and the general case can be reduced
to this case with some loss of precision. An explicit estimate, which is better than
Baker’s, was obtained in [2] for the linear form (1.2) under the condition of strong
independence. This estimate is also in terms of the usual heights.
In this paper, the condition of strong independence means the following equation:

[
K(√
α1 ,..., √
αn ) : K] =2n. (1.5)

Other exponents of the radicals can be used here and, in the early papers, these were
determined by the methods of proof. Then it was observed that the square root is
enough and gives better estimates. Other exponents may be useful in the p-adic
case. Condition (1.5) enables us to apply Kummer theory, simpliﬁes the ﬁnal step
of the proof and improves the dependence of our estimate on n. Therefore we also
call (1.5) the Kummer condition. (More precisely, we say that α1,...,αn satisfy
the Kummer condition with respect to the ﬁeld K.) This condition was originally
introduced by Baker and Stark in [3].
In the paper [4] (which appeared in 1980) the constant C1 in (1.3) takes the form
C1 = Dn+2C2(n). The constant C2 equals n2n28n+51 in the general case, and we
have C2 = n
n+429n+26 under the hypothesis (1.5). (Also, some dependence on n
and D appears under the logarithm sign in ln Ω
′.)
Since then, the dependence on D has remained the same. For n =2 this was
established by Gelfond as long ago as 1952 (see [5], § 3.4, Theorem 3). It is strange
that the general case was not done until recently. One of the reasons why Wald-
schmidt was able to obtain this dependence and to improve the other constants
is that he used the logarithmic heights (see the deﬁnition in § 3) instead of the
logarithms of the usual heights, and, in his notation, we have

Aj ⩾ max {h(αj), | ln αj|
D , 1
D
 } , 1 ⩽ j ⩽ n;

ln B ⩾ max
{h(β0),...,h(βn)
}. (1.6)

Explicit lower bound for a homogeneous rational form 725

It is worth noting that Waldschmidt’s estimate depends on one more parameter,
which can be written as
 E =max { | ln αj|
DAj :1 ⩽ j ⩽ n} .

The smaller the value of E, the better is the estimate for |Λ|. Shorey [6] was the
ﬁrst to study the dependence on this parameter in the Gelfond–Baker method. But
very small E are rarely encountered. Wishing to get examples in which the estimate
for |Λ| is good just because E is small, it is more convenient to use techniques based
on the properties of so-called G-functions, which give better estimates here than
the Gelfond–Baker method. (See [7] for rational αj and [8] for the general case.)
Of course, any improvement is of value in the computational applications of linear
forms in logarithms. Most of the recent estimates take this parameter into account.
In this paper, we also introduce a parameter of this type, and the dependence we
get is better than the preceding ones.
Waldschmidt’s estimate is concerned with (1.1) only. Hence, in estimating (1.2),
we are forced to regard (1.2) as a particular case of (1.1), although (1.2) could clearly
admit a better estimate. In theoretical and practical applications, the homogeneous
rational case is more important than the general case (see, for example, [9], [10]).
Waldschmidt’s constant C2 was comparatively large, but it was small enough to
allow some computer calculations using estimates of linear forms in logarithms.
This suggests obtaining new explicit bounds for |Λ| in the homogeneous rational
case.
In 1983, the author [11] announced the following estimate for the case of strong
independence:
 |Λ| > exp
(
−C2Dn+2Ωln(e5D2An−1)ln(e2B)
),

C2 = e8nn+4.5(2e3)
n. (1.7)

If K is a complex ﬁeld, then D may be replaced by D/2. The constant C2 in (1.7)
is better than Waldschmidt’s. The dependence on the bj is also improved since the
parameter B in (1.7) equals

B =max { |bj|Aj
An :1 ⩽ j ⩽ n} , (1.8)

while the usual deﬁnition of B in (1.6) yields

B =max
{|bj| :1 ⩽ j ⩽ n}. (1.9)

Unfortunately, the author did not publish the proof of (1.7). This was mainly
because he tried to prove a similar result without the assumption (1.5), but no
success has been achieved in this direction. If we remove (1.5), C2 becomes very
large (there appears an extra factor nn), and formula (1.8) for B must be replaced
by (1.9). At the same time, despite the diﬃculty of computing C2 when getting
estimates of the type (1.7), we can use the fact that K is complex and improve the

726 E. M. Matveev

dependence on B of the form (1.9) to that on B of the form (1.8) by slightly changing
the notation in the original proof. In this paper we get even better dependence on
B than in (1.8). This is also achieved by slightly changing the notation.
It turns out that (1.5) is satisﬁed in the most important practical applications
of linear forms in logarithms. Therefore it is necessary to have good estimates in
the rational homogeneous case even under the restriction (1.5). Various authors
([12] in 1987 and [13] in 1990) returned twice to this problem. They used [4] as
a paradigm and, changing some notation and parameters, obtained estimates with
constants like Waldschmidt’s and with dependence on B of the form (1.8). Hence
their C2 is worse than that in (1.7).
Among other improved estimates of linear forms in logarithms, we distinguish
independent results of W¨ustholz [14] and Philippon and Waldschmidt [15] presented
at the Durham conference in 1986. Their estimates contain no factor ln Ω
′.This
success was achieved by using new estimates for the multiplicity of zeros for alge-
braic groups, which were obtained by the methods of algebraic geometry. However,
technical diﬃculties in these proofs are so big that we still have no explicit estimates
without worsening the dependence on n or B. For example, ln Ω
′ was retained in
the papers [12] and [13], although they appeared after Durham.
A very precise estimate for n = 2 was obtained in [16]. Although the dependence
on B is of the form ln
2 B, the constant C2 is rather small, which makes this estimate
better than others in applications where all parameters are not large. The proof
uses Schneider’s method instead of Baker’s. This estimate has been repeatedly
improved.
Waldschmidt’s recent paper [17] contains a new explicit estimate for (1.2), where
ln Ω
′ is also eliminated. A feature of this result is the absence of (1.5) and the
dependence on B of the form (1.9). This improvement is paid for by the appearance
of a factor n3n in the estimate. The proof is based on a modiﬁcation of Schneider’s
method.
Another recent explicit estimate for |Λ| in the homogeneous rational case is due
to Baker and W¨ustholz [18]. The authors were able to combine the new estimates
of the multiplicity of zeros with Kummer theory and to obtain an estimate for
|Λ| without the factor ln Ω
′ and without worsening the dependence on n.Their
constant C1 has the form

C1 = 18(n +1)! nn+1(32D)
n+2 ln(2nD).

We note that their estimate concerns the case without condition (1.5). Although
the authors reduce this case to the case of strong independence, they do not give
the corresponding explicit estimate. Clearly, passing to the general case gives an
extra factor 2
1−nn! and worsens the dependence on B. In [18], the dependence
on B is of the form (1.9). But in applications it is extremely important to have
the dependence (1.8), not (1.9). For example, the authors of [19] prefer to use [17]
instead of [18], despite the much worse dependence on n.
In this paper we present a new explicit estimate of linear forms in logarithms
in the homogeneous rational case under the Kummer condition. This estimate is
stronger than that announced in [11]. As the main improvement, we eliminate the
factor nn in C2. This factor provides the greatest diﬃculties in practical applica-
tions (see, for example, [9], [10]). As already noted, the same factor appears when

Explicit lower bound for a homogeneous rational form 727

we omit (1.5). Then it becomes dominant, therefore we do not prove our estimate
in the general case. To remove it completely, one needs new ideas.
Another improvement concerns the dependence on | ln αj|, which will be con-
siderably weaker than in (1.6). We also remove the lower bound 1/D for Aj by
including weaker conditions.
Our estimate contains a factor of the type ln Ω
′, and is in this respect weaker
than the estimates described above. This factor is not inherent. In the author’s
opinion, it can be eliminated in the same way as in [18]. But the author does not
know to what extent this could worsen the dependence on n and B.

§ 2. Statements of the results

Throughout the paper we use the following notation. K is an algebraic number
ﬁeld of degree DK over Q,and K is embedded in C.If K ⊆ R, we put κ =1,
otherwise κ =2. We write D = DK/κ. There are given α1,... ,αn ∈ K∗,
n ⩾ 2, which satisfy the Kummer condition. Let h(αj), 1 ⩽ j ⩽ n,be their
absolute logarithmic heights, and let ln α1,..., ln αn be arbitrary ﬁxed values of
the logarithms. We put
 ρ = rankR{ln α1,... , ln αn}.

Consider a linear form Λ= b1 ln α1 + ··· + bn ln αn

where b1,...,bn ∈ Z, bn ̸=0.
We use positive numbers A1,...,An. (Recall that they correspond to (ln Aj)in
the notation of other authors.) We take

ϑ ⩾ 1
n
 ( h(α1)
A1 + ··· + h(αn)
An
 ) , (2.1)

E ⩾ 1
nD max {∣
∣
∣
∣± ln α1
A1 ± ··· ± ln αn
An
 ∣
∣
∣
∣

} , (2.2)

E1 = 1
(n − 1)Dϑ
 ( 1
A1 + ··· + 1
An
 )

and specify the parameters C1, C2, C3, C∗
3 by the conditions

C∗
3 exp(C∗
3 ) Ee
2ϑ ⩾ en/ρ,C3 =max {
C∗
3 , n
ρ
 } . (2.3)

C1 = (
1+ e−2n

148
 ) (n ln 2 + 2)
 (
1+ 1
n )

C3 ,

C2 =4(n +1) (
6+ 5
n ln 2 + 2
 ) e2n

n1/2C3 . (2.4)

For brevity we write

Ω= A1 ...An,ω =Ω ( C1Dϑ
e
 )n (
C3 exp(C3) Ee
2ϑ
 )ρ . (2.5)

728 E. M. Matveev

Let C0 satisfy the condition

C0 ⩾ max {
2C3, ln (
C2D max { C0ω
C1AnϑD ,C0, 2C3E1
C1
 })} . (2.6)

We also put
 B0 =
 n−1∑

j=1
 |bn| + |bj|
g. c. d.(bj,bn)2DωC0C2 , (2.7)

B1 =
 n−1∑

j=1
 1
g. c. d.(bj,bn)2C1nDϑ
 ( |bn|
Aj + |bj|
An
 ) ,

B2 =
 n−1∑

j=1
 | ln αj|
(
|bn| + |bj|
)

|bn|2DωC0C2 ,

B3 =
 n−1∑

j=1
 | ln αj|
2C1|bn|Dϑn
 ( |bn|
Aj + |bj|
An
 ) ,

and assume that
W0 ⩾ max{
2C3, ln
(
e(1 + B0 + B1 + B2 + B3)
)}. (2.8)

Theorem 2.1. Suppose that
 Dω min{C0,W0}
2C3 ⩾ 1, (2.9)

ω
C1ϑAj
 min{C0,W0}
2C3 ⩾ 1, 1 ⩽ j ⩽ n, (2.10)

3(C1Dϑ)
n−1 DΩ
Aj
 (
C3 exp(C3) Ee
2ϑ
 )ρ−1 C0
C3 ⩾ 1, 1 ⩽ j ⩽ n. (2.11)

Then ln |Λ| > −91 · 2nC2C0D2W0ω. (2.12)

The following theorem simpliﬁes the assertion of Theorem 2.1. It enables us to
compare our results with previous ones, and it may be applied when no special
precision is needed.

Theorem 2.2. Suppose that ϑ =1, E =1, C3 = n/ρ,

Aj =max {h(αj), | ln αj|
D , 1
DC1
 } , 1 ⩽ j ⩽ n, (2.13)

B =max { |bj|Aj
An :1 ⩽ j ⩽ n} , (2.14)

C′
0 =ln ( C2Dω
C1An
 ) . (2.15)

Explicit lower bound for a homogeneous rational form 729

Then ln |Λ| > −112 · 2nC2C′
0D2ω ln(2eB). (2.16)

We note that here the factor which depends on n is equal to

112 · 2nC2ϑ
nCn
1 e−n (
C3 exp(C3) Ee
2ϑ
 )ρ < 215 ( ne
2ρ
 )ρ ρ(2e2ρ ln 2)
n

n1/2 .

Theorem 2.3. Suppose that K = Q, Aj ⩾ h(αj), 1 ⩽ j ⩽ n, E =1, C3 = n.
Let C0, W0, B, C′
0 satisfy (2.6), (2.8), (2.14), (2.15).Then:
(i) the inequalities (2.12), (2.16) hold with ϑ =1;
(ii) if αj ∈ Z, αj > 0 and Aj =ln αj , 1 ⩽ j ⩽ n, then the inequali-
ties (2.12), (2.16) hold with ϑ = 1
2 (1 − 1/nen+1);
(iii) for this ϑ we have Dω/(C1Anϑ) >E1/C1 in (2.6).

Remark 2.1. The following example shows that the case κ =2, ρ =1 is not
uncommon. For an algebraic number β with 0 <β < 1we have

|b1π + b2 arcsin β| = |b1 ln α1 + b2 ln α2|,

where α1 = −1and α2 satisﬁes the equation α
2
2 − 2iβα2 − 1= 0.

Remark 2.2. We can exclude the case κ =1, ρ = 2. Indeed, if K ⊆ R and α ∈ K,
then also |α| = ±α ∈ K, and we have

|b1 ln α1 + ··· + bn ln αn| ⩾ ∣
∣b1 ln |α1| + ··· + bn ln |αn| ∣
∣.

Hence we can take only positive αj and only principal values of the logarithms.

Remark 2.3. The dependence on κ was stated in [11]. The dependence on ρ is
introduced here for the ﬁrst time. If κ =2, ρ = 1, then the estimate becomes
better.

Remark 2.4. The dependence (2.7) on the bj is new, since it takes into account
the possibility of a non-trivial g. c. d.(bj,bn). It may be useful, say, in the study of
Catalan’s equation, where we encounter the form

±p ln p ± q ln q + pq ln ( u
v
 ) .

Remark 2.5. The lower bounds in (2.9)–(2.11) are technical, as well as the lower
bounds for C0/C3, W0/C3. Changing these bounds may worsen the estimate for
|Λ|, but to a lesser extent than if we simply increase the corresponding parameters
to satisfy the initial conditions. The corresponding changes can easily be made in
§§ 11, 12. Our bounds are chosen because they are satisﬁed in the case K = Q.

Remark 2.6. The conditions (2.1)–(2.11) are easily seen to be homogeneous
in A1,...,An. That is, they remain valid if we multiply each Aj by some λ> 0
and divide ϑ, E by λ. We may optimize our estimate by varying A1,... ,An.

730 E. M. Matveev

Roughly speaking, we must minimize E in (2.2) with a ﬁxed ϑ and with equal-
ity in (2.1). This may actually be further improved if we take into account the
considerations of § 5.

Remark 2.7. The case (ii) of Theorem 2.3 strengthens the general case by a factor
of order 2n. Here ϑ need not satisfy (2.1).

Remark 2.8. The case (ii) of Theorem 2.3 may be further improved if we estimate
the volume of the body W more precisely (see § 5). Similarly, the parameter ϑ
of Theorem 2.1 may be speciﬁed more precisely than in (2.1). The corresponding
expression for ϑ can be found in § 5. Here we use its simplest estimate to avoid
complicated statements in the theorem.

§ 3. Notation and lemmas

We have DK embeddings of K into C. Accordingly, there are DK Archimedean
valuations of the ﬁeld K:
 |α|σ = ∣
∣α
(σ)∣
∣, 1 ⩽ σ ⩽ DK.

Complex-conjugate embeddings correspond to equal valuations, but it is convenient
to take them both. We identify K with the embedding corresponding to σ =1. We
enumerate the prime ideals of K by indices σ> DK and deﬁne non-Archimedean
valuations of K by the formula

|α|σ = (Norm p)
−k,k = ordp(α), p = pσ,σ > DK,α ∈ K∗.

For such valuations we have the product formula

∞∏

σ=1 |α|σ =1,α ∈ K∗.

Note also that |α|σ ̸= 1 for only ﬁnitely many σ.
If γm ∈ K for some non-zero integer m, then the following formulae deﬁne |γ|σ,
σ ⩾ 1, and ln γ(σ),1 ⩽ σ ⩽ D, without extending the ground ﬁeld K:

|γ|σ = |γm|
1/m
σ , ln γ(σ) = m
−1 ln(γm)
(σ).

The product formula remains valid for such γ.
Usually, σ |∞ means that σ is Archimedean, and σ ∤ ∞ means that σ is non-
Archimedean. In the latter case, σ | p means that the ideal pσ divides the ideal (p).
The indexing of valuations is convenient when no speciﬁc properties of them are
needed, for example, when we sum over all σ.Let Kσ be the metric completion
of K with respect to the valuation σ. We introduce the notation

κσ =[Kσ : Qσ],σ ⩾ 1, κ = κ1,

so that κσ = 1 for real σ and κσ =2 for complex σ.

Explicit lower bound for a homogeneous rational form 731

The local logarithmic height and the absolute logarithmic height of a set of num-
bers B = {βj ∈ K : j ∈J } are deﬁned as follows:

hσ(B)= ln max
{|βj|σ : j ∈J }
,σ ⩾ 1,

h(B)= 1
DK
 ∞∑

σ=1 hσ(B).

(We put ln 0 = −∞.) The absolute logarithmic height of a number α ∈ K is deﬁned
as follows:

h(α)= h(
{1,α}) = 1
DK
 ∞∑

σ=1 max
{0, ln |α|σ} = 1
2DK
 ∞∑

σ=1
∣
∣ln |α|σ∣
∣.

The absolute logarithmic height of α is independent of the ﬁeld which contains α.
Note that h(α) = 0 only for the roots of 1. For any other α ̸= 0 we will have
h(α) ⩾ C(K) > 0. This constant can be found explicitly for a ﬁxed K, but the
general problem is still open. See [20] for a review of results on this problem.
We shall use various ways of enumerating the components of a vector. We ﬁx
the following notation for some of these:
1) ¯u =(u1,...,un), notation (¯),
2) ˜u =(u1,...,un−1), notation (˜),
3) ¯u′ =(u0,... ,un), notation (¯′),
4) ˜u′ =(u0,... ,un−1), notation (˜′).
Vectors of other types will be denoted by ¯u′′, with an indication of how to
enumerate their components, for example:
5) ¯u′′ =(u1,... ,uJ ), notation (¯′′).
We always use the same letter for the components of a vector and for the vector
itself.
Let ¯u,¯v be real vectors. We write ¯u ⩾ ¯v (resp. ¯u> ¯v) if the corresponding
inequality holds for each component. We also introduce the notation

|¯u| = |u1| + ··· + |un|.

Let f (x) ̸= |x| be a scalar function of one scalar variable (f may depend on other
numerical arguments). To each vector ¯u we assign a vector f (¯u) as follows:

f (¯u)= (
f (u1),... ,f (un)
)
.

We deﬁne the scalar product of two vectors ¯u,¯v by

¯u · ¯v = u1v1 + ··· + unvn.

Given a scalar function f (x, y) ̸= xy and vectors ¯u,¯v, we put

f (¯u, ¯v)=
 n∏

j=1 f (uj,vj ).

732 E. M. Matveev

For example, the linear form (1.2) can be written as

Λ= ¯b · ln ¯α,

and ¯α
¯l denotes
 ¯α
¯l =
 n∏

j=1 α
lj
j .

We shall say that ¯l is the multi-exponent of ¯α.
This notation remains valid for vectors of all types, provided that the range of
the summation corresponds to the type of the vectors (both vectors must be of the
same type).
The following notation deals with vectors of one type and produces vectors of
another type. We put

˜χ(¯u, ¯b)= ˜χ(¯u)= (χ1,...,χn−1), ˜ν(¯u, ¯b)= ˜ν(¯u)= (ν1,...,νn−1),

where the components are deﬁned as follows:

χj = ujbn − unbj, 1 ⩽ j ⩽ n − 1,

νj = ujbn − unbj
g. c. d.(bj,bn) , 1 ⩽ j ⩽ n − 1.

We may omit the argument ¯b, assuming that we ﬁx the value of ¯b which ﬁgures in
the linear form (1.2). We note that ˜χ is deﬁned for ¯b of any type while ˜ν is deﬁned
only for integer ¯b. The reason for introducing ˜ν is that the bj may be relatively
prime in their totality but not pairwise coprime.
The following property of the vectors ˜χ,˜ν is obvious but useful:

˜χ(¯u + x¯b)= ˜χ(¯u), ˜ν(¯u + x¯b)= ˜ν(¯u).

We use j, k, l, m, s, t, λ, τ , M to denote integer-valued variables. More-
over, j, m, s, t, τ , M will be non-negative. In what follows we often omit such
explanations. The set of natural numbers (positive integers) is denoted by N,and
the set of non-negative integers by N0.
The following equation can be obtained if we remove the parentheses from |¯a|
M

by the binomial formula: |¯a|
M

M ! = ∑

|m|=M
 ¯a
m

m!
¯1 . (3.1)

Here ¯a ⩾ ¯0and ¯1=(1,..., 1). Retaining only one term in the right-hand side, we
get the inequality |¯a|
|m|

|m|! ⩾ ¯a
m

m!
¯1 . (3.2)

We state the following trivial assertion as a lemma.

Explicit lower bound for a homogeneous rational form 733

Lemma 3.1. Let fj(z, m) and gj(z, m)(with 1 ⩽ j ⩽ n − 1 and m =0, 1,... ) be
functions that satisfy the relations

fj(zj,mj)=
 mj∑

τj=0 cj(mj,τj)gj(zj,τj),mj ⩾ 0, 1 ⩽ j ⩽ n − 1,

for some cj(mj,τj). Then the functions

F (˜z, ̃m)=
 n−1∏

j=1 fj(zj,mj),G(˜z, ̃m)=
 n−1∏

j=1 gj(zj,mj)

satisfy the relations

F (˜z, ̃m)= ∑

˜τ ⩽ ̃m C( ̃m, ˜τ )G(˜z, ˜τ ),G( ̃m, ˜τ )=
 n−1∏

j=1 cj(mj ,τj).

Now we introduce a notion which, in some sense, generalizes the notion of log-
arithmic height. Given a vector ¯α ∈ (K∗)
n and a set W⊆ R
n, we put

hσ(¯α, W)=sup
{w · ln |¯α|σ : w ∈W}
,σ ⩾ 1,

h(¯α, W)= 1
DK
 ∞∑

σ=1 hσ(¯α, W).

If W⊆ Z
n,then h(¯α, W)= h(
{ ¯α
w : w ∈W})
.If W is the set of standard basis
vectors, then h(¯α, W)= h(
{ ¯α})
.

Lemma 3.2. (i) If V⊆ W,then h(¯α, V) ⩽ h(¯α, W).
(ii) h(¯α, rW)= rh(¯α, W), r> 0.
(iii) h(¯α, V + W)= h(¯α, V)+ h(¯α, W).
(iv) h(¯α, {¯v}) =0, ¯v ∈ R
n.
(v) h(¯α, W +¯v)= h(¯α, W), ¯v ∈ R
n.
(vi) h(¯α, W) is independent of the choice of the ﬁeld containing the numbers α.

Proof. (i) is obvious. (ii), (iii) follow from the more precise (and also obvious)
equations

hσ(¯α, rW)= rhσ(¯α, W),hσ(¯α, V + W)= hσ(¯α, V)+ hσ(¯α, W)

valid for each σ. (iv) follows from the product formula. (v) follows from (iii) and (iv).
(vi) is analogous to a property of the usual logarithmic height and is proved similarly
(see [21], § 3.1).

734 E. M. Matveev

§ 4. The general scheme of the proof

The main idea in the study of linear forms in logarithms, originating in the
papers of Gelfond, is to consider simultaneously two auxiliary functions, one of
which has good algebraic properties while the other has good analytic properties.
Assuming |Λ| small, we may, for some range of the arguments, replace one of these
functions by another with a small error term. But the appropriate choice of the
auxiliary function is rather diﬃcult. Here one of the main ideas is due to Baker.
His auxiliary function was of the form

G(˜z′)= ∑(0) P0(z0, ¯l )
 n−1∏

j=1 α
(lj bn−lnbj )zj /bn
j ,

where P0(z0, ¯l ) are polynomials with indeterminate coeﬃcients, and the summation
runs over some set L0 ⊆ Z
n of indices ¯l. (More precisely, the polynomial part of the
function was introduced by Fel’dman in [22], and many choices of L0 were suggested.
The main improvement in the present paper is also achieved by a suitable choice
of L0.) Taking partial derivatives, dividing all expressions by a common factor and
putting zj = z, we get the following set of functions:

Gs(z, ̃m
′)= ∑(s) P (m0)
s (z, ¯l )˜χ ̃m(¯l )˜α ˜χ(¯l )z/bn. (4.1)

Here s = 0. (In what follows we encounter such expressions for other s as well.) We
shall use the analytic properties of these functions. At the same time, we consider
functions with good algebraic properties. They have the form

Fs(x, ̃m
′)= ∑(s) P (m0)
s (x, ¯l )˜χ ̃m(¯l )¯α
¯lx. (4.2)

We prove our theorems by induction on s. At step zero, s = 0, we must choose
the coeﬃcients of the polynomials, not all zero, to satisfy the equations

Fs(x, ̃m
′)= 0, | ̃m
′| ⩽ Ms,x ∈Xs (4.3)

for some M0 and X0,where

X0 = {0, ±1, ±2,... , ±X0}. (4.4)

This will be done in § 6 via an analogue of Siegel’s lemma.
The inductive step is carried out as follows. First we get the equations

Fs ( x
2 , ̃m
′) =0, | ̃m
′| ⩽ Ms+1,x ∈Xs+1, (4.5)

with some Ms+1 ⩽ Ms and Xs+1 such that

Ms+1 ⩾ Ms + [
− M0
2s+1(1 + ε0)
 ] +1,s ⩾ 0,

Xs = {±1, ±3,... , ±(2Xs − 1)
},s > 0. (4.6)

Explicit lower bound for a homogeneous rational form 735

(Here and in what follows we shall introduce small parameters ε whose values are
to be speciﬁed later. Note that X0 is slightly diﬀerent from the other Xs.) The
numbers Xs are deﬁned by

Xs+1 = { 2Xs, 0 ⩽ s ⩽ S1,
Xs,S1 <s, S1 =log2
 ( M0
2+2ε0
 ) . (4.7)

This will be done in § 10 by applying an extrapolation technique to the functions
Gs(z, ̃m
′) in (4.1).
We note that, for our choice of S1, the numbers Xs, Ms do not change for s>S1,
which simpliﬁes the induction.
Now we look at the consequences of (4.5). Put

x =2y +1, ¯l =2¯λ + ¯δ, ¯δ ∈{0, 1}n, ¯λ ∈Ls(¯δ).

Then we have

0= Fs ( x
2 , ̃m
′) = ∑

¯δ
 ( ∑

¯λ P (m0)
s ( x
2 , ¯l) ˜χ ̃m(¯l )¯α¯λx+¯δy)
¯α¯δ/2.

At this point of the proof, we use the Kummer condition. It says that the
numbers ¯α¯δ/2, ¯δ ∈{0, 1}n, are linearly independent over K. The coeﬃcients of
¯α¯δ/2 in Fs(x/2, ̃m
′)belongtothe ﬁeld K, whence they must be all zero, and we
deduce from (4.5) that

∑

¯λ P (m0)
s ( x
2 , 2¯λ + ¯δ) ˜χ ̃m(2¯λ + ¯δ)¯α¯λx =0,

| ̃m
′| ⩽ Ms+1,x ∈Xs+1, ¯δ ∈{0, 1}n. (4.8)

Now take ¯δ for which not all the polynomials are zero, and put

Ls+1 = Ls(¯δ),Ps+1(z, ¯λ)= Ps ( z
2 , 2¯λ + ¯δ) .

Since we have (4.8) for all ̃m
′ with | ̃m
′| ⩽ Ms+1, we can deduce the following
equations with the help of (4.8) and Lemma 3.1:

∑(s+1) P (m0)
s+1 (x, ¯λ)˜χ ̃m(¯λ)¯α¯λx =0.

Denoting the left-hand side by Fs+1(x, ̃m
′), we get (4.3) for s + 1. This completes
the inductive step.
Let ¯δs denote the ¯δ chosen at the step s. Then, for each ¯λ ∈Ls, the initial ¯l ∈L0
can be recovered by the formula

¯l = ¯l(¯λ)= 2s¯λ + ¯λs, ¯λs = ¯δ0 +2¯δ1 + ··· +2s−1¯δs−1. (4.9)

736 E. M. Matveev

We used Lemma 3.1 to reduce the expressions ˜χ ̃m(
¯l(¯λ)
) to the form ˜χ ̃m(¯λ), but
in what follows it will be convenient to avoid this.
Now let us see how long the induction must be. Each component of a vector
¯l ∈Ls ranges over the set

Ls,j,0 ⩽ lj ⩽ Ls,j,1,Ls,j ⩾ Ls,j,1 − Ls,j,0, 1 ⩽ j ⩽ n, (4.10)

and we easily see from the inductive step that

Ls+1,j ⩽ Ls,j
2 , 1 ⩽ j ⩽ n, 0 ⩽ s ⩽ S.

If we take S> log2(L0,n), then the range for ln becomes less than 1 after S
steps, so there will be no summation over ln. The idea of getting rid of summation
only over ln is due to van der Poorten [23].
Now let L0 ⩾ max{
deg P0(z, ¯l ): ¯l ∈L0}
.

Then we can choose some x0 ∈XS and m0 ⩽ L0/|XS| so that the numbers

η(¯l )= P (m0)
S (x0, ¯l ), ¯l ∈LS,

are not all zero. Suppose that we have the inequality

MS ⩾ [LS,1]+ ··· +[LS,n−1]+ L0
|XS| . (4.11)

Then (4.3) for s = S yields the equations

LS,n−1,1∑

ln−1=LS,n−1,0 ···
 LS,1,1∑

l1=LS,1,0
 n−1∏

j=1(bnlj − bjln)
mj η(¯l )= 0,

0 ⩽ mj ⩽ [LS,j], 1 ⩽ j ⩽ n − 1.
 (4.12)

A novel feature of our proof is that we allow the numbers Ls,j,0 and Ls,j,1 to
depend on the values of lj+1,... ,ln, but the numbers Ls,j will be independent of
them.

Lemma 4.1. Let LS,j be of the form (4.10). Then the system of equations (4.12)
has no non-zero solution η(¯l ).

Proof. Put ξ1(l1,... ,ln−1)= η(¯l ). We recursively deﬁne

ξj+1 = ξj+1(m1,... ,mj,lj+1,... ,ln−1)

=
 LS,j,1∑

lj =LS,j,0(bnlj − bjln)
mj ξj, 1 ⩽ j ⩽ n − 1.

Explicit lower bound for a homogeneous rational form 737

We see that the collection {ξj+1} is obtained from {ξj} with the help of Vander-
monde matrices. Hence the collection {ξj+1} is non-zero provided that {ξj} is. But
the numbers {
ξn( ̃m)
} form the left-hand side of (4.12). This proves the lemma.

We have deduced the equations (4.12) under the assumption that the linear form
is small. Lemma 4.1 contradicts them. This proves the theorem about the estimate
for linear forms in logarithms.

Remark 4.1. The collections Xs as chosen in (4.4), (4.6) contain both positive and
negative integers, which enables us to improve considerably the constants in the
estimates for linear forms. This was not done in [12], [13], and this is what makes
the estimates of these papers weaker than those in [11].

§ 5. Construction of the initial collection of multi-exponents

Here and in the following sections, we introduce some parameters in terms of
which the estimates of the linear forms are obtained. Finally, we shall put them in
correspondence with the parameters of § 2. We introduce the parameters as they
become necessary, and we explain our choice. Some of the parameters are more
detailed than needed for the theorems of § 2. They may be useful in more accurate
estimates, especially for particular values of the αj.
We begin by describing the construction of the set of multi-exponents, L0,for
the initial auxiliary function F0(x, ̃m
′). This set will satisfy

L0 ⊆ (W + w0) ∩ Z
n (5.1)

for some W⊆ R
n and w0 ∈ R
n. Todothis, take some L> 0 and some set
{ϑ0,ϑ1,...,ϑσ,... } of non-negative integers satisfying the following conditions:
1) if ln |¯α|σ = ¯0, then ϑσ = 0 and the other ϑσ are positive (σ ⩾ 1);
2) complex-conjugate K(σ) correspond to equal ϑσ;
3) if ρ =1, then ϑ1 Im(ln ¯α)= ϑ0 Re(ln ¯α) (in particular, ϑ0 =0 if K ⊆ R).
Note that only ﬁnitely many ϑσ are non-zero.
We deﬁne W⊆ R
n as follows: w ∈W if

−ϑσL ⩽ w · ln |¯α|σ ⩽ ϑσL, σ ⩾ 1, (5.2)

−ϑ0L ⩽ w · Im(ln ¯α) ⩽ ϑ0L. (5.3)

One may also introduce other conditions in the deﬁnition of W. In any case,
W will be a bounded symmetric body. Put

L0,j,0 = L0,j,0(wj+1,...,wn)= inf{wj : w ∈W},

L0,j,1 = L0,j,1(wj+1,...,wn)= sup{wj : w ∈W}, (5.4)

L0,j =sup{L0,j,1 − L0,j,0 : wj+1,...,wn ∈ R}, 1 ⩽ j ⩽ n.

The usual modern approach is to choose some positive numbers A1,...,An in
order to put subsequently

L0,j,0 = − L
2Aj ,L0,j,1 = L
2Aj ,L0,j = L
Aj , 1 ⩽ j ⩽ n. (5.5)

738 E. M. Matveev

The body W is deﬁned by the condition that if w ∈W,then

L0,j,0 ⩽ wj ⩽ L0,j,1, 1 ⩽ j ⩽ n. (5.6)

Then we can regard (5.2), (5.3) as deﬁning the numbers ϑσ. We proceed in this
way when there is no other information about the numbers α. In particular cases,
all the conditions (5.2)–(5.6) may be used to describe W. This can improve the
dependence of our estimate for |Λ| on the numbers αj.
The main idea which enables us to eliminate the factor nn from the estimate of
|Λ| is to regard the inequality

|w · ln ¯α| ⩽ ϑ
∗
0L, w ∈W, (5.7)

not as the deﬁnition of ϑ
∗
0 but as a part of the deﬁnition of W for suitable choice
of ϑ
∗
0. (In the real case, ϑ1 = ϑ
∗
0.)
Take ϑ such that
 ϑ ⩾ 1
Ln h(¯α, W)= 1
nDK
 ∞∑

σ=1 ϑσ. (5.8)

Having ﬁxed ϑ, ϑ
∗
0, we need to ﬁnd the body W of maximal volume such
that (5.7), (5.8) are satisﬁed. This problem is rather diﬃcult and we shall use
the following lemma.

Lemma 5.1. Let W0 ⊆ R
n be a symmetric convex body, let ¯v ∈ C
n be a vector
(¯v ̸= ¯0), and let η> 0.Put ρ = rankR{Re ¯v, Im ¯v},

ϑ
∗
1 =sup
{|w · ¯v| : w ∈W0}
, E = {
w ∈ R
n : |w · ¯v| ⩽ ϑ
∗
1}.

Then Vol(W0 ∩ ηE) ⩾ Vol(W0)min{1,ηρ}.

Proof. The assertion is obvious if η ⩾ 1. Suppose that η< 1. Consider the
subspaces V = R Re(¯v)+ R Im(¯v)and V ⊥ (which is orthogonal to V in R
n). We
have dim V = ρ,dim V ⊥ = n − ρ. Consider the function

f (w)= Voln−ρ(
W0 ∩ (w + V ⊥)
)
, w ∈V.

By the Brunn–Minkowski theorem (see [24], Theorem 21.1), f (rw) is a decreasing
function of r ⩾ 0for each w ∈V.Let E ′ be the orthogonal projection of E onto V.
We have

Voln(W0 ∩ ηE)= ∫

w∈ηE ′ f (w) d Volρ(w)

= ∫

ηw∈ηE ′ f (ηw) d Volρ(ηw)= η−ρ ∫

w∈E ′ f (ηw) d Volρ(w)

⩾ η−ρ ∫

w∈E ′ f (w) d Volρ(w)= η−ρ Vol(W0),

which proves the lemma.

Explicit lower bound for a homogeneous rational form 739

We deﬁne Ω0 by the relation
 Vol(W)= Ln

Ω0 . (5.9)

Using only (5.5), (5.6), we get a body W0 of volume

Vol(W0)= Ln

Ω , Ω= A1 ...An.

If we simply take L0 = W∩ Z
n,then |L0| can be less than Vol(W). We can
increase |L0| using Blichfeld’s theorem (see [25], Ch. 3, Theorem 1), which implies
that there is a vector w0 such that

∣
∣(W + w0) ∩ Z
n∣
∣ > Vol(W).

Then for L0 in (5.1) we get |L0| >Ln/Ω0. We can take only a subset of these
points so that
 |L0| = [ Ln

Ω0
 ] +1. (5.10)

If we increase Ω0, then (5.10) will mean that we take fewer points than possible.
The vector w0 is deﬁned up to adding an element of Z
n, so it can be chosen to
satisfy
 w0 ∈ [−0.5, 0.5]
n.

By Lemma 3.2, adding w0 to W does not change the value of the ϑ in (5.8), but it
worsens the constant ϑ
∗
0 by an additive term which does not exceed the number ε∗

deﬁned by
 ε∗ =max
 {|w · ln ¯α| : w ∈ [−0.5, 0.5]
n}

L . (5.11)

We also put
 ϑ
∗ = ϑ
∗
0 + ε∗ (5.12)

and introduce the following parameters

B1 =max
 {∣
∣˜ν(w)
∣
∣ : w ∈W}

M0 ,

B0 =max
 {∣
∣˜ν(w)
∣
∣ : w ∈ [−0.5, 0.5]
n}

M0 .
 (5.13)

Then we have ∣
∣˜ν(¯l )
∣
∣ ⩽ (B1 + B0)M0 for ¯l ∈L0.

740 E. M. Matveev

§ 6. Siegel’s lemma

We introduce the notion of the length of a vector with weight coeﬃcients because
the corresponding theorem in [20] was stated and proved in these terms. Consider
a vector ¯a
′′ =(a1,... ,aJ ) ∈ KJ

and a set of positive numbers (the weight coeﬃcients)

Q = {qjσ :1 ⩽ j ⩽ J; σ ⩾ 1}. (6.1)

If σ ∤ ∞, we put qjσ = 1. Denote by Q
′ the set of reciprocals. We deﬁne the local
length and the absolute length of a vector ¯a
′′ with weight coeﬃcients Q as follows:

∥¯a
′′∥Q,σ =
 ( J∑

j=1
 |aj|
2
σ
q2
jσ
 )1/2, 1 ⩽ σ ⩽ DK,

∥¯a
′′∥Q,σ =max { |aj|σ
qjσ :1 ⩽ j ⩽ J} ,σ > DK,

∥¯a
′′∥Q =
 ( ∞∏

σ=1 ∥¯a
′′∥Q,σ
)1/DK .

(To deﬁne heights, we must replace the maximum by summation over the Archime-
dean valuations.)
For vectors ¯a
′′, ¯p′′ ∈ KJ we have the inequalities

|¯a
′′ · ¯p′′|σ ⩽ ∥¯a
′′∥Q′,σ ·∥¯p′′∥Q,σ. (6.2)

Lemma 6.1 ([20], Theorem 3). Given vectors

¯a
′′
i =(ai1,...,aiJ ) ∈ KJ ,i =1,... ,I < J,

and a set of weight coeﬃcients Q as in (6.1),put

qj =
 ∞∏

σ=1 q1/DK
jσ , 1 ⩽ j ⩽ J, q =(q1 ...qJ )
1/J . (6.3)

Then the system of linear equations

¯a
′′
i · ¯p′′ =0, 1 ⩽ i ⩽ I,

has a non-zero solution ¯p′′ =(p1,...,pJ ) ∈ KJ which satisﬁes the condition

∥¯p′′∥Q ⩽ γ
(

q−J I∏

i=1 max
{q, ∥¯a
′′
i ∥Q′ }
)1/(J−I),

γ = ∣
∣∆(K)
∣
∣1/(2DK) max{1, 0.5J 1/2},
 (6.4)

where ∆(K) is the discriminant of the ﬁeld K.

Explicit lower bound for a homogeneous rational form 741

Remark 6.1. The expression for γ in [20] contained simply 0.5J 1/2 assuming that
J ⩾ 4. But it is clear from the proof that we can take γ as in (6.4). In this paper,
J> 4.
The reason for introducing the weight coeﬃcients is that the solution ¯p′′ has
small components at the large factors, while large numbers correspond only to
small factors, whence their contribution to the estimates is small. This is the main
diﬀerence from the result obtained in [26].
Another diﬀerence from [26] is that we do not require that the system have
full range. Hence theorems in [26] require either caution in application or a slight
sharpening with the help of the considerations of [20]. Here it is important that the
heights of linear forms (without weight coeﬃcients) have upper bound at least 1,
except for the zero forms, where we must also take at least 1 for the upper bound.
According to Lemma 6.1, we need an estimate for ∣
∣∆(K)
∣
∣.

Lemma 6.2. Suppose that α0,...,αn are non-zero algebraic numbers, K =
Q(α0,...,αn), DK =[K : Q].Put K0 = Q(α0), D0 =[K0 : Q],and
Kj = Kj−1(αj), Dj =[Kj : Kj−1], 1 ⩽ j ⩽ n.Then

ln
∣
∣∆(K)
∣
∣ ⩽ DK ln(DK)+2DK
 n∑

j=0(Dj − 1)h(αj), (6.5)

ln
∣
∣∆(K)
∣
∣ ⩽ DK ln(DK)+2DK(DK − 1) max
{h(αj): 0 ⩽ j ⩽ n}
. (6.6)

Proof. Put D′ =(D0,... ,Dn). Obviously, DK = D0 ...Dn, and we can take the
numbers ω( ¯d
′)= ¯α
′ ¯d′, ¯0′ ⩽ ¯d
′ < D′ as a basis of K over Q. Consider the number

∆= det(
ω( ¯d
′)
(σ))

1⩽σ⩽DK; ¯0′⩽ ¯d′<D′.

From Hadamard’s inequality we get the estimate

|∆| ⩽ DDK/2
K
 n∏

j=0
 DK∏

σ=1 max{
1, |αj|σ}Dj −1. (6.7)

If we interpret the ﬁeld K geometrically, then the Z-module M0 generated by
the numbers ω( ¯d
′) becomes a DK-dimensional lattice of volume Vol(M0)= |∆|.
Clearly, M0 lies in the fractional ideal M1 generated by the numbers ω( ¯d
′). There-
fore Vol(M1) ⩽ Vol(M0).
Suppose that we have a decomposition of ideals (αj )= aj/bj,0 ⩽ j ⩽ n,where
aj, bj are relatively prime integral ideals. Then the ideal M2 = M1 ∏n
j=0 bDj −1
j is
integral. On account of (6.7), its volume equals

Vol(M2)= Vol(M1)
 n∏

j=0 Norm(bj)
Dj −1 =Vol(M1)
 n∏

j=0
 ∏

σ>D max{
1, |αj|σ}Dj −1

⩽ DDK/2
K
 n∏

j=0
 ∞∏

σ=1 max{
1, |αj|σ}Dj −1

= exp
(
0.5DK ln DK + DK
 n∑

j=0(Dj − 1)h(αj)
).

742 E. M. Matveev

As M2 is an integral ideal, we have M2 ⊆M = (1), and hence
∣
∣∆(K)
∣
∣1/2 =Vol(M) ⩽ Vol(M2),

which yields the inequality (6.5).
Successively using the obvious inequality

(D1 − 1) + (D2 − 1) ⩽ (D1D2 − 1),D1,D2 ⩾ 1,

we can now simplify (6.5) and obtain (6.6). This proves the lemma.

Note that if there is no α0,we may take α0 =1.
Lemma 6.2 is the only point in this paper where we need DK,not D = DK/κ.

Remark 6.2. Estimate (6.5) is more precise than the following estimate in [18],
Lemma 2:
 ln
∣
∣∆(K)
∣
∣ ⩽ n(DK − 1)DK ln 2 + 2(DK − 1)
 n∑

j=1 h(αj)deg αj.

§ 7. Some basis polynomials

The way of representing the polynomials P (z) is important in the estimates.
It was Fel’dman who realized that the polynomials under consideration need not
necessarily be in Z[x]. They are only required to be integer-valued, that is, to be
integers for all integer values of the argument. Fel’dman initiated a systematic use
of the basis polynomials

∆(z, 0) = 1, ∆(z, k)= z(z +1) ... (z + k − 1)
k! ,k =1, 2,...

This system of polynomials was later modiﬁed. We shall use the polynomials intro-
duced in [27]. For H ∈ N put

∆(z, l, H)= (∆(z, H)
)λ∆(z, h),l = λH + h, 0 ⩽ h ⩽ H, l ∈ N0.

Clearly, deg ∆(z, l, H)= l.For γ ̸= 0 we also put

∆(γz,l,H,m)= ∆
(m)(γz,l,H)
γmm! .

Lemma 7.1. Suppose that H, L0,N ∈ N,M0,L−1 ∈ N0,L0 = L−1H + H1,
0 ⩽ H1 ⩽ H.Let d0 be the lowest common denominator of the numbers

∆(N x,l,H,m),x ∈ Z, 0 ⩽ l ⩽ L0, 0 ⩽ m ⩽ M0.

Then
 d0 ⩽ exp(1.03883HM0), (7.1)

d0 ⩽ H!
L−1H1! ( 2.8361e(M0 + L−1 +1)
L0
 )L0 . (7.2)

Explicit lower bound for a homogeneous rational form 743

If z ∈ C, then for some coeﬃcients δ(l, m) > 0 we have

∣
∣∆(z, l, H, m)
∣
∣ ⩽ δ(l, m) (
e (
1+ |z|
H
 ))l , (7.3)

L0∑

l=0
 M0∑

m=0 δ(l, m) ⩽ exp (
L−1 +2+ H
e
 ) . (7.4)

Proof. See [27]. We have only inserted the factor N . The dependence on N is clear.

We put N =2S, (7.5)

with S taken from § 4. The reason for introducing N is our desire to avoid fractional
values of the argument after the substitution z = x/2 below.

Remark 7.1. We do not use the estimate (7.1) because (7.2) is better in our case.
All preceding authors used estimates of the type (7.1). Also, we do not use inequali-
ties (7.3), (7.4), since we need more careful estimates in the presence of the factor N .

Here and in what follows we use the quantitative version of Stirling’s formula,

N N e−N (2πN )
1/2 <N ! <N N e−N (2πN )
1/2e1/(12N ),N ∈ N. (7.6)

Lemma 7.2. In the notation of Lemma 7.1 we have

H!
L−1H1! ⩽ H L0e−L0(2πH)
L0/(2H) exp ( L0
12H 2
 ) . (7.7)

Proof. If H1 = 0, then (7.7) is a simple consequence of (7.6). Now let H1 ⩾ 1. Put
x = H1/H (1/H ⩽ x ⩽ 1). Using (7.6), we have the inequality

H!
L−1H1! ⩽ H L0e−L0(2πH)
L0/(2H) exp ( L0
12H 2 + f (x)
) ,

f (x)= Hx ln(x) − x ln(2πH)
2 + ln(2πHx)
2 − x − 1
x
12H .

Diﬀerentiating, we get

f ′′(x)= 24(Hx)
2 − 12(Hx)+ 4
24Hx3 ,

and we easily see that f ′′(x) ⩾ 0for Hx ⩾ 1. Hence f (x) is convex and attains
its maximal value at x =1/H or at x =1. For x =1 we have f (1) = 0, and the
lemma is true in this case. For x =1/H we have

f ( 1
H
 ) = − ln(H) − ln(2πH)
2H + ln(2π)
2 + 1
12 − 1
12H 2 .

A simple calculation shows that the maximal value of f (1/H) is attained at H =1
and equals zero. This proves the lemma.

744 E. M. Matveev

Lemma 7.3. Suppose that γ ̸=0, H ∈ N, H> 1, z0 ⩾ max
{|z|,H}
.Then

∣
∣
∣
∣ ∆
(τ )(γz,l,H,m)
τ !
 ∣
∣
∣
∣ ⩽ δ(l, m, τ ) (
e (
1+ |γ|z0
H
 ))l , (7.8)

where ∞∑

l=0
 ∑

m+τ ⩽l δ(l, m, τ ) ⩽ (
1 − e
√
2πH
 )−1 e(H+1)/e. (7.9)

Proof. The derivative contains ( l
m+τ) terms with the factor (
m+τ
τ )
. The numerator
of each term is estimated in terms of

|γ|
τ (
|γ|z0 + H)l−m−τ = ( H
e
 )l (
e(
1+ |γ|z0
H
 ))l|γ|
τ (
|γ|z0 + H)−m−τ ,

which yields
 ∑

m+τ ⩽l
 ( l
m + τ
 )(
m + τ
τ
 )( 1
|γ|z0 + H
 )m ( |γ|
|γ|z0 + H
 )τ

= (
1+ |γ| +1
|γ|z0 + H
 )l ⩽ ( H +1
H
 )l .

Now we put l = λH + h (0 ⩽ h< H). Using (7.6) and the inequality
(1 + 1/H)
H <e,we get

∞∑

l=0
 ∑

m+τ ⩽l δ(l, m, τ ) ⩽
 ∞∑

λ=0
 H−1∑

h=0
 ( H
e
 )l ( H+1
H )l

H!λh!

=
 ∞∑

λ=0
 ( ( H+1
e )H

H!
 )λ H−1∑

h=0
 ( H+1
e )h

h! ⩽ e(H+1)/e ∞∑

λ=0
 ( e
√2πH
 )λ ,

which proves (7.9).

Remark 7.2. Having an estimate for the absolute value of the polynomial P (z)for
|z| ⩽ z0 and wishing to estimate |P (z)| for large z, we must insert an extra factor
(
|z|/z0)deg P .

§ 8. Construction of the initial auxiliary function

We shall write the polynomials of the auxiliary function in the form

P0(z, ¯l )=
 L0∑

l0=0 pl0,¯l∆(Nz, l0,H0), ¯l ∈L0. (8.1)

Explicit lower bound for a homogeneous rational form 745

For brevity we introduce the multi-index

¯l′ =(l0, ¯l ) ∈L
′
s, L
′
s = {0,... ,L0}×Ls.

The following important idea, which is typical for the homogeneous rational
case, is to consider somewhat diﬀerent auxiliary functions, other than Gs(z, ̃m
′),
Fs(z, ̃m
′) in (4.1), (4.2). At ﬁrst, dividing by an appropriate number, we can
replace ˜χ(¯l )by ˜ν(¯l ) (not in the exponent). This evident improvement has not yet
been made. A less evident improvement is to replace ˜ν ̃m(¯l )by ∆
(˜ν(¯l ), ̃m
)
.The
possibility of doing this distinguishes the form (1.2) from (1.1) and enables us to
obtain the estimate (1.4) instead of (1.3). This idea is due to Fel’dman [28]. Thus
we get the following new functions instead of (4.1), (4.2) respectively:

Ψ0(z, ̃m
′)= ∑(0)(N m0m0!)
−1P (m0)
0 (z, ¯l )∆
(˜ν(¯l ), ̃m
) ˜α ˜χ(¯l )z/bn, (8.2)

Φ0(x, ̃m
′)= ∑(0)(N m0m0!)
−1P (m0)
0 (x, ¯l )∆
(˜ν(¯l ), ̃m
) ¯α
¯lx. (8.3)

(In this section, we need only s = 0.) Using Lemma 3.1, we can transform the
functions (8.2), (8.3) into (4.1), (4.2) and vice versa. Therefore, the system of
equations (4.3) is equivalent to the system

Φ0(x, ̃m
′)= 0, | ̃m
′| ⩽ M0,x ∈X0. (8.4)

By formulae (8.1), we can regard Φ0(x, ̃m
′) as a linear form in the variables p¯l′ ∈ K.
Conditions (8.4) are linear equations with respect to p¯l′. To satisfy them, we apply
Lemma 6.1. The multi-index ¯l′ corresponds to the index j. The multi-index (x, ̃m
′)
corresponds to the index of the linear form i. For the weight coeﬃcients (6.1) we
take q¯l′,σ = q¯l′ = exp
(
c0(L0 − l0)
), 1 ⩽ σ ⩽ D, ¯l′ ∈L
′
0, (8.5)

with some constant c0 > 0. Now let us estimate the parameters in Lemma 6.1.
Taking (5.10) into account, we have

J = |L
′
0| =(L0 +1)|L0| > (L0 +1)Ln

Ω0 . (8.6)

The parameter q in (6.3) equals

q = exp

( L0∑

l0=0
 ∑(0) c0 L0 − l0
J
 )
 = exp

(

c0
 L0∑

l0=0
 L0 − l0
L0 +1
 )
 = ec0L0/2. (8.7)

The number of equations is

I = |X0|∆(M0 +1,n) ⩽ (2X0 + 1)(1 + ε1) M n
0
n! ,

(1 + ε1) ⩾ (1+ n +1
2M0
 )n . (8.8)

746 E. M. Matveev

(Here and in what follows we estimate small expressions by introducing small
parameters ε whose exact value will be speciﬁed in the end of the proof using
the known values of the main terms.)
We estimate the lengths of the expressions Φ0(x, ̃m
′), regarded as linear forms
in the p¯l′ with the weight coeﬃcients (8.5). The estimates must contain the com-
ponents for
1) the exponential part ¯α
¯lx,
2) the absolute value of the polynomial part ∆(N x,l,H,m),
3) the denominator d0 of the polynomials,
4) the absolute value of ∆
(˜ν(¯l ), ̃m
)
. (This expression appears when we diﬀeren-
tiate the auxiliary function, so we call it the diﬀerential part.)
The contribution of the coeﬃcients ¯p′ to the estimate of Φ0(x, ̃m
′) is small by the
choice of the weight coeﬃcients. We optimize the choice of parameters by making
estimates of the same order for all the components. This gives an improvement
if we take into account that the role of these components becomes diﬀerent in
the extrapolation. In this paper we consider the exponential part separately and
equalize all other components.
Using the notation of § 3 and the deﬁnition of ϑ in (5.8), we estimate the factor
¯α
¯lx as follows:
 exp
(
|x|h(¯α, L0)
) ⩽ exp
(
|x|h(¯α, W)
) ⩽ exp
(
|x|ϑnL)
. (8.9)

According to (3.2), (5.13), the absolute value of ∆
(˜ν(¯l ), ̃m
) is estimated by

∣
∣∆
(˜ν(¯l ), ̃m
)∣
∣ ⩽
 (
| ̃m| +(B1 + B0)M0)| ̃m|

| ̃m|! ⩽
 (
(1 + B1 + B0)M0)M0

M0! .

Introducing a parameter W such that

W ⩾ ln
(
e(1 + B1 + B0)
) (8.10)

and using Stirling’s formula (7.6), we get

∣
∣∆
(˜ν(¯l ), ̃m
)∣
∣ ⩽ exp(WM0)
(2πM0)1/2 , | ̃m| ⩽ M0. (8.11)

On account of (7.2), (7.7), the denominator is estimated by

d0 ⩽ exp
(
c0L0(1 + ε2)
) (8.12)

with some ε2 if we choose c0 so that

c0 ⩾ ln ( 2.8361H0(M0 + L−1 +1)
L0
 ) . (8.13)

If, moreover, c0 satisﬁes the inequality

c0 ⩾ ln (
e (
1+ N (X02n+1 +0.5)
H0
 )) , (8.14)

Explicit lower bound for a homogeneous rational form 747

then by (7.8), (8.5) we get
∣
∣∆(Nx, l0,H0,m0)
∣
∣q¯l′ ⩽ δ(l0,m0, 0) exp(c0L0),

|x| ⩽ Z0 +0.5. (8.15)

Remark 8.1. In this section, we use (8.15) only for |x| ⩽ X0, which is possible if
Z0 ⩾ X0. Actually we shall choose Z0 to be much bigger than X0 to simplify the
arguments of the subsequent sections.
We see that the polynomial part is estimated in the same way as the denominator.
The diﬀerential part can also be estimated similarly if we guarantee that c0L0 =
WM0 (compare (8.11) with (8.12) and (8.13)).
By (7.9), the remaining part is estimated by

L0∑

l0=0 δ(l0,m0, 0) |L0|
1/2

(2πM0)1/2 ⩽ 0.2eε3c0L0. (8.16)

As a result, combining (8.6), (8.11), (8.12), (8.15), (8.16), we get
∥
∥Φ0(x, ̃m
′)
∥
∥Q′ ⩽ 0.2 exp
(
c0L0(3 + ε2 + ε3)+ ϑ|x|nL)
. (8.17)

(Note that the right-hand side is greater than q in (8.5). This is important in (6.4).)
Multiplying out the inequalities (8.17), we get

I∏

i=1 max{
q, ∥¯a
′′
i ∥Q′ } =
 X0∏

x=−X0
 ∏

| ̃m′|⩽M0
∥
∥Φ0(x, ̃m
′)
∥
∥Q′

⩽ exp (
I (
c0L0(3 + ε2 + ε3)+ ϑnLX0(X0 +1)
2X0 +1
 )) . (8.18)

If we guarantee that

Jc0L0
2 ⩾ I (
c0L0(3 + ε2 + ε3)+ ϑnLX0(X0 +1)
2X0 +1
 ) , (8.19)

then (8.5), (8.18) show that by Lemma 6.1 there is a non-zero vector ¯p′′ =
{p¯l′ ∈ K : ¯l′ ∈L
′
0} that satisﬁes equations (8.4) and condition (6.4). This con-
dition takes here the following form:

∥¯p′′∥Q ⩽ γ ⩽ exp(ε4c0L0). (8.20)

Let us now choose values of the parameters that satisfy all the above conditions.
We express them in terms of two new parameters, c1, c2 (to be speciﬁed later)
which describe respectively M0/L and X0/W . We put

X0 = c2DW ⩾ 1
ε5 ,ω0 =Ω0
 ( c1ϑD
e
 )n ,

M0 = c0L0
W ,L = M0
c1nϑD ,

L0 +1 ⩾ 2WDω0(1 + ε1) ((2 + ε5)(3 + ε2 + ε3)+(1 + ε5) c2
c1
 ) c2en nn

n! .
 (8.21)

748 E. M. Matveev

Substituting the expressions for M0, L, X0 into (8.19) and using (8.6), (8.8),
we get the condition for L0. Hence (8.19) will be satisﬁed. Note that we have
WM0 = c0L0.
We must also guarantee that M0,L0,X0 ∈ Z. This can be done because we
have not yet ﬁxed c0, W , L0.First we get X0 ∈ Z by slightly decreasing W ,
then we obtain that L0 ∈ Z, and ﬁnally we get M0 ∈ Z with the help of c0.The
parameter H0 will be chosen so that the right-hand sides of (8.13) and (8.14) have
the same order.
 § 9. The interpolation formula

The main analytic tool in the Gelfond–Baker method is an interpolation formula
which follows from Cauchy’s residue theorem. We recall this formula and prove
some related technical inequalities, which improve earlier estimates.
We denote by D[x, R)and D[x, R] respectively the open and closed discs in C of
radius R centred at x,and by Γ(x, R) the circle of radius R centred at x.
Consider a ﬁnite set X⊆ C (of the nodes of interpolation) along with some
positive integers t = t(x) (the multiplicity of x) attributed to each x ∈X .We
denote such an object by (X , T ). We put

Q(z)= ∏

x∈X(z − x)
t(x).

This polynomial determines (X , T ) and vice versa. We say that

Q(z)=
 T∏

τ =1 qτ (z),qτ (z)= ∏

t(x)⩾τ(z − x), 1 ⩽ τ ⩽ T, (9.1)

is the standard decomposition of Q(z). Fix also the notation

U =deg Q(z),uτ =deg qτ (z) ⩾ 1, 1 ⩽ τ ⩽ T. (9.2)

Let f (z) be an analytic function in D[0,R]and let X⊆ D[0,R). Then for
z ∈D[0,R)\X we have f (z)= f1(z)+ f2(z),

where
 f1(z)= 1
2πi
 ∫

Γ(0,R)
 Q(z)
Q(ζ) · f (ζ) dζ
ζ − z ,

with Γ(0,R) oriented anti-clockwise, and

f2(z)= ∑

x∈X
 t(x)−1∑

τ =0
 f (τ )(x)
2πiτ !
 ∫

Γ(x,r)
 Q(z)
Q(ζ) · (ζ − x)
τ dζ
ζ − z ,

with Γ(x, r) oriented clockwise. Here z/∈D[x, r] ⊆D[0,R), x ∈X . We also deﬁne
numbers r, r0, δ0 as follows:

r0 =min{
|z − x| : x ∈X },

δ0 = { r0 if |X | =1,
min{
|x − y| : x, y ∈X ,x ̸= y} otherwise, (9.3)

r = min{r0,δ0}
2 .

Explicit lower bound for a homogeneous rational form 749

Lemma 9.1. Let (X , T ) be an object as above, with X⊆ R, z/∈X , z ∈ R.Sup-
pose that the standard decomposition (9.1) of Q(ζ) satisﬁes (9.2), each factor qτ (ζ)
is even or odd, and its roots form an arithmetic progression with some diﬀerence
δτ > 0. (If uτ =1,weput δτ = |z|.) Put also

zτ =max {
|z|, δτ uτ
2
 } , 1 ⩽ τ ⩽ T, z0 ⩾ max{zτ :1 ⩽ τ ⩽ T }.

Then for each ζ ∈ C with |ζ| >z0 we have

∣
∣
∣
∣ Q(z)
Q(ζ)
 ∣
∣
∣
∣ ⩽ ( z0
|ζ|
 )U , (9.4)

and for each ζ ∈ Γ(x, r), x ∈X and r deﬁned in (9.3) we have

∣
∣
∣
∣ qτ (z)
qτ (ζ)
 ∣
∣
∣
∣ ⩽ ( 2ez0
δ0uτ
 )uτ , 1 ⩽ τ ⩽ T. (9.5)

Remark 9.1. Such polynomials Q(ζ) usually occur when the set X is symmetric and
forms an arithmetic progression, while t(−x)= t(x)and t(x) decreases when x> 0.
Then all δτ are equal. However, a more complicated situation will be encountered
below.

Proof. Taking into account the structure of the roots of qτ (ζ), we see that ∣
∣qτ (z)
∣
∣

increases when we shift z by δτ outwards the centre. Hence ∣
∣qτ (z)
∣
∣ ⩽ qτ (zτ ) ⩽
qτ (z0)and ∣
∣Q(z)
∣
∣ ⩽ Q(z0). Now (9.4) follows from the inequality

|z2
0 − x
2|
|ζ2 − x2| ⩽ z2
0 − x
2

|ζ|2 − x2 ⩽ ( z0
|ζ|
 )2 .

Proving (9.5), we shall omit τ in qτ (z), uτ , δτ . We also assume that z0 = z.
Denote by y any root of q(ζ). There are two cases.

Case 1. r = |z − x|
2 < δ
2 .Then we have

a) ∣
∣
∣
∣ z − y
ζ − y
 ∣
∣
∣
∣ =2 if y = x,

b) ∣
∣
∣
∣ z − y
ζ − y
 ∣
∣
∣
∣ ⩽ δ +2r
δ − r ⩽ 4 (this is possible only when y, z lie on diﬀerent sides

of x and |x − y| = δ0),

c) ∣
∣
∣
∣ z − y
ζ − y
 ∣
∣
∣
∣ ⩽ 2δ +2r
2δ − r < 2 for all other y.

If u = 1, then (9.5) holds because we always have z = z0 ⩾ δ0.
If u = 2, (9.5) is non-trivial in the case b) only. Then ±y are the roots of q(ζ),
δ =2y and (9.5) follows from the inequality

∣
∣
∣
∣ q(z)
q(ζ)
 ∣
∣
∣
∣ ⩽ 2(2y +2r)
2y − r ⩽ (
2e max{y +2r, 2y}
4y
 )2 .

750 E. M. Matveev

This inequality is easily veriﬁed by considering 0 <r < y and y ⩽ r ⩽ 2y separately,
according to the maximal value in the deﬁnition of zτ .
If u ⩾ 3, we have
∣
∣
∣
∣ q(z)
q(ζ)
 ∣
∣
∣
∣ ⩽ 4 · 2u−1 <eu ⩽ ( 2ezτ
δu
 )u ⩽ ( 2ez0
δ0u
 )u .

Case 2. r = δ0/2. Then ∣
∣q(z)
∣
∣ ⩽ ∣
∣q(z0)
∣
∣ ⩽ zu
0 . Hence to obtain (9.5) it remains
to verify the inequality ∣
∣q(ζ)
∣
∣ ⩾ ( δ0u
2e
 )u . (9.6)

The point x may not be a root of q(ζ). Therefore we ﬁrst move x to one of the
roots without decreasing ∣
∣q(ζ)
∣
∣. We compute the number of roots on the left (v1)
and on the right (v2)of x.If v1 >v2 (resp. v1 <v2), we move x to the root closest
to y from the left (resp. from the right), and if v1 = v2,we move x to the root
closest to ζ.We also shift ζ to the closest point of Γ(y, r), keeping Im ζ ﬁxed. Then
we contract all the zeros so that the distance between them becomes δ0.Thus we
may assume in the remainder of the proof that δ = δτ = δ0.
Taking into account the structure of the roots of q(ζ), we can shift Γ(x, r)
together with ζ by δ towards the centre. This decreases ∣
∣q(ζ)
∣
∣. Hence we may
assume that x is the closest to zero. The following argument is based on the
inequalities

|ζ − y| ⩾ |y − x|− r, ∣
∣(ζ − y − x)(ζ − x + y)
∣
∣ ⩾ y2 − r2.

We apply the second inequality to the pairs of roots of q(ζ) that are symmetric with
respect to x, and we apply the ﬁrst inequality to the other pairs. This shows that
the minimum of ∣
∣q(ζ)
∣
∣ is attained at the ζ ∈ R which is closest to zero. There are
two possibilities: u is even (u =2X), or u is odd (u =2X + 1). For simplicity we
assume that δ = 2, which is possible because both parts of (9.6) are homogeneous
for ζ ∈ Γ(x, δ/2).
If u =2X +1, then

∣
∣q(ζ)
∣
∣ ⩾ ∣
∣q(1)
∣
∣ =(2X − 1)!! (2X +1)!! =
 (
(2X +1)!!
)2

2X +1 =
 ( (2X+1)!
2X X! )2

2X +1

>
 ( u
ue
−u
2X X X e−X )2

2X = ( u
e
 )u (
1+ 1
2X )2X+1

e > ( u
e
 )u .

Here we have used (7.6) for N =2X +1 and N = X, as well as the inequality
(1 + 1/N )
N +1 >e.
The case u =2X is treated similarly. We have

∣
∣q(ζ)
∣
∣ ⩾ ∣
∣q(0)
∣
∣ = (
(2X − 1)!!
)2 = ( (2X)!
2X X!
 )2 > ( uue−u

2XX X e−X
 )2 = ( u
e
 )u ,

which proves (9.6) and the lemma.

The following assertion is stated as a lemma because it will be used repeatedly
in what follows.
 Explicit lower bound for a homogeneous rational form 751

Lemma 9.2. Let f (z, ζ) be an analytic function of ζ deﬁned for some ﬁxed z ∈ R.
Consider (X , T ) with z/∈X such that the corresponding Q(ζ) satisﬁes the assump-
tions of Lemma 9.1.Let δ0, r, U , T be as in (9.1)–(9.3), and let z0 be as in
Lemma 9.1. Suppose that for some positive a0, a1, a2, a3, a4 and for some z1 ⩾ |z|,
f (z, ζ) satisﬁes for |ζ| ⩽ R the inequality

∣
∣f (z, ζ)
∣
∣ ⩽ a0 exp
(
a1 + a2z1 + a3 ln
( R
z0
 ) + a4R)
,

R = U − a3
a4 . (9.7)

Suppose also that the following conditions hold with some constant c3:

0 <c3 ⩽ ln ( a1 + a2z1
a4z0c3e
 ) , (9.8)

U ⩾ a3 + a1 + a2z1
c3 . (9.9)

Then ∣
∣f (z, z)
∣
∣ < 2a0 + ∑

x∈X
 t(x)−1∑

τ =0 2rτ ∣
∣
∣
∣ Q(z)
Q(ζx)
 ∣
∣
∣
∣ ·
 ∣
∣f (τ )(z, x)
∣
∣

τ ! . (9.10)

(The derivatives are taken with respect to ζ,and ζx ∈ Γ(x, r) is the point with the
minimal value of |Q(ζ)|.)

Proof. We apply the interpolation formula to f (z, ζ)and ζ = z, estimating the ﬁrst
term by (9.4). In the ﬁrst case we see from (9.7), (9.8) that

R ⩾ a1 + a2z1
c3a4 ⩾ exp(c3)ez0 >ez0,

|ζ − z| ⩾ R − z0 ⩾ (
1 − 1
e
 ) R> R
2 ,
∣
∣
∣
∣ f (z, ζ)Q(z)
Q(ζ)
 ∣
∣
∣
∣ <a0 exp (
a1 + a2z1 + a3 ln ( R
z0
 ) + a4R − U ln ( R
z0
 ))

= a0 exp (
a1 + a2z1 − (U − a3)ln ( U − a3
a4z0e
 ))

⩽ a0 exp (
c3(U − a3) − (U − a3)ln ( a1 + a2z1
c3a4z0e
 ))

⩽ a0 exp (
(U − a3) (
c3 − ln ( a1 + a2z1
c3a4z0e
 ))) ⩽ a0,

which gives the estimate for the ﬁrst term in the right-hand side of (9.10). The
second term follows directly from the interpolation formula. This proves the lemma.
Below we shall estimate the factor ∣
∣Q(z)/Q(ζx)
∣
∣ with the help of (9.5).

752 E. M. Matveev

§ 10. The inductive step of the proof

We introduce a set of functions similar to (8.3):

Φs(x, ̃m
′)= ∑(s)(
(2−sN )
m0 m0!
)−1P (m0)
s (x, ¯λ)∆
(˜ν(¯l ), ̃m
)¯α
¯lx/2
s

= γx
s ∑(s)(
(2−sN )
m0 m0!
)−1P (m0)
s (x, ¯λ)∆
(˜ν(¯l ), ̃m
)¯α¯λx.

Here the sum is taken over the set of multi-indices ¯λ ∈Ls and ¯l = ¯l(¯λ) is deﬁned
in (4.9). Also γs =¯α¯λs/2
s and ¯λs is deﬁned in (4.9). For s = 0 we put ¯λ0 = ¯0and
γ0 =1.
The inductive step of the proof consists of two parts.
Part 1. Before proving (4.5), we establish that

Φs(x, ̃m
′)= 0,x ∈{0, ±1, ±2,... , ±Zs}, | ̃m
′| ⩽ M (x), (10.1)

for some Zs and some multiplicities M (x) (to be determined later).
Part 2. In this part, we prove the inequalities

Φs ( x
2 , ̃m
′) =0,x ∈Xs+1, | ̃m
′| ⩽ Ms+1, (10.2)

which are equivalent to (4.5). Later we determine the multiplicity Ms+1 and verify
that it is compatible with (4.6).
In part 1 we put L1 = K, and in part 2 we put L2 = K(√
α1 ,... , √
αn ).We see
that if z = x ∈ Z in part 1 (j =1) or if z = x/2, x ∈ Z in part 2 (j = 2), then the
values of (
Φs(z, ̃m
′)
)2
s belong to the ﬁeld Lj.
Enumerate the valuations of the ﬁeld Lj by the indices σ as described in § 3
and let S′ be the set of indices such that Lj remains ﬁxed or complex-conjugate
(if κ = 2) under the corresponding inclusion of Lj into C. Hence |S′| = κ.The
remaining indices form the set S. Note that the values of ∣
∣Φs(x, ̃m)
∣
∣σ are equal for
σ ∈S′. We also introduce the functions

Ψs(ζ, ̃m
′)= ∑(s)(
(2−sN )
m0 m0!
)−1P (m0)
s (ζ, ¯λ)∆
(˜ν(¯l ), ̃m
)˜α ˜χ(¯l )ζ/(2
sbn),

f (z, ζ)= fj(z, ζ)= Ψs(ζ, ̃m
′)

( ∏

σ∈S
∣
∣Φs(z, ̃m
′)
∣
∣σ
)1/κ,j =1, 2.

If we assume that the linear form in the logarithms is small, then the value of
Ψs(z, ̃m
′)isclose to Φs(z, ̃m
′), and the value of ∣
∣f (z, z)
∣
∣ is either close to 1 by the
product formula or it is equal to 0. Thus our task is to exclude the ﬁrst case by
showing that ∣
∣f (z, z)
∣
∣ is small enough.
On account of the deﬁnition of ˜χ(¯l )in § 3, the diﬀerence between ∣
∣Φs(ζ, ̃m
′)
∣
∣1
and ∣
∣Ψs(ζ, ̃m
′)
∣
∣ is estimated with the help of the inequality
∣
∣¯α
¯lζ/2
s − ˜α ˜χ(¯l )ζ/(2
sbn)∣
∣ = ∣
∣¯α
¯lζ/2
s∣
∣ · ∣
∣e−Λζln/(2
sbn) − 1∣
∣

⩽ exp
(
ϑ
∗L∣
∣
∣
∣ ζ
2s
 ∣
∣
∣
∣
) · 1.1 · ∣
∣
∣
∣ Λζln
2sbn
 ∣
∣
∣
∣ , (10.3)

where Λ is our linear form (1.2), which is assumed to be small.

Explicit lower bound for a homogeneous rational form 753

Here we have used the deﬁnition (5.12) of ϑ
∗, (5.7), (5.11) and the fact that
|ez − 1| ⩽ 1.1|z| for all z ∈ C with |z| ⩽ 0.1.
The estimate of ∣
∣f (z, ζ)
∣
∣ is similar to that of ∥
∥Φ0(z, ̃m
′)
∥
∥
Q′ , but we add (8.20),
use (6.2) and take into account that the exponent of the radical is now κ,not
[Lj : Q]. Therefore the corresponding similar estimate contains an extra factor
[Lj : Q]/κ in the exponent. We also assume that

∣
∣
∣
∣ Λζln
2sbn
 ∣
∣
∣
∣ < 0.1 (10.4)

for all ζ which are encountered below. Then the assumption (9.7) of Lemma 9.2
holds with
 a0 =0.22,a1 = a1sj = c0L0(3 + ε2 + ε3 + ε4) [Lj : Q]
κ ,

a2 = a2sj = ϑ(2−sL)n [Lj : Q]
κ ,

a3 = L0,a4 = a4s = ϑ
∗2−sL.
 (10.5)

Let us also introduce the following constants:

ηs = a2s1
c3 + (a3 + a1s1)/c3
2Xs + 1
Xs ,

ξs = a2s1
2c3 ,η0s = a1s1
4Xsc3 . (10.6)

We prove equations (10.1) by induction on |x|. The base is given by the equations
for x ∈Xs and M (x)= Ms. As the next step, we prove them for

x = z ∈ Z, |z| ⩽ 2Xs,z /∈Xs,z0 = z1 =2Xs,

| ̃m
′| ⩽ M (z)=[Ms − ηs]+ 1. (10.7)

The cases s =0 and s> 0 diﬀer in the following respect. If s =0,we must
prove (10.1) for X0 < |z| ⩽ 2X0,and if s> 0, we must prove (10.1) for even z with
|z| ⩽ 2Xs. Now we can proceed to prove (10.1) by induction for

x = z ∈ Z, 2Xs < |z| ⩽ Zs,z0 = z1 = |z|,

| ̃m
′| ⩽ M (z)= [
Ms − ηs − ξs ln ( |z|
2Xs
 )] +1,

Zs =2n+1Xs.
 (10.8)

It follows that the multiplicity M (z) is even and decreases for z> 2Xs.When
we use Lemma 9.2, we include all x ∈ Z such that either M (x) >M (z)or |x| < |z|
and M (x)= M (z)in the set X of the nodes of interpolation. Their multiplicities
are t(x)= M (x) − M (z)+ 1,x ∈X . (10.9)

754 E. M. Matveev

Proving (10.2) (part 2, j = 2), we shall take

X = {0, ±1,... , ±Zs}.

Hence for z = x/2, x ∈Xs+1, takingintoaccount that Xs+1 =2Xs,we can take

|z| ⩽ z1 =2Xs − 1,z0 = Zs +0.5,

Ms+1 =[Ms − ηs − ξsn ln 2 − η0s]+ 1,

t(x)= M (x) − Ms+1 +1. (10.10)

Compared with the maximal x in part 1, we have added two points ±Zs to X and
slightly increased the multiplicities.
The idea of including all previously obtained points with the multiplicities
already proved for them was suggested to the author by A. Shmelev, but the
appropriate revision of the extrapolation technique turned out to be technically
diﬃcult.
We consider the standard decomposition of the polynomial Q(ζ) corresponding
to the above set (X , T ). The following lemmas enable us to estimate U =deg Q(ζ)
and other parameters of § 9.

Lemma 10.1. Suppose that ϕ(z) is a convex decreasing function, X ′, X ′′, Y ′

belong to Z and satisfy X ′ <X ′′ and Y ′ ⩽ ϕ(X ′′).Put E = {
(x, y) ∈ R
2 : X ′ <x ⩽ X ′′,
Y ′ ⩽ y ⩽ ϕ(x)
}.Then

Card(E∩ Z
2) ⩾ Vol(E) − ϕ(X ′) − ϕ(X ′′)
2 .

Remark 10.1. When ϕ(x) is not convex, one should not divide by 2 in the estimate.
When ϕ(x) increases, one must take Y ′ ⩽ ϕ(X ′), X ′ ⩽ x< X ′′ in the hypothesis
and interchange X ′, X ′′ in the estimate.

Proof. For integer m, n deﬁne the sets

Smn = {
(x, y) ∈ R
2 : m − 1 <x ⩽ m, n ⩽ y< n +1}
, Sm = ⋃

n Smn,

E ′ = ⋃

(m,n)∈E Smn, Em =(E/E ′) ∩Sm.

It follows from the properties of ϕ(z)that all Em are either empty or curvilinear
right-angled triangles with straight perpendicular sides and with convex (down-
wards) hypotenuses. Their horizontal perpendicular sides are less than 1, and the
sum of their vertical perpendicular sides is at most (
ϕ(X ′) − ϕ(X ′′)
)
. Hence we get

Vol(E) − Card(E∩ Z
2)= Vol(E) − Vol(E ′) ⩽ Vol (E/E ′)

= ∑

m Vol(Em) ⩽ ϕ(X ′) − ϕ(X ′′)
2 .

Explicit lower bound for a homogeneous rational form 755

Lemma 10.2. For the above set (X , T ) we have r =1/2.In part 1(j =1) we
have δ0 =2 for X = Xs (s> 0),and δ0 =1 otherwise. In part 2(j =2) we
have δ0 =1. In both cases (j =1, 2), U satisﬁes (9.9) with a0, a1, a2, a3 given
in (10.5).

Proof. The estimates for δ0, r are obvious. For |z| ⩽ 2Xs we simply have U ⩾ 2Xsηs
and (9.9) is satisﬁed. Hence we shall assume that |z| > 2Xs. We use Lemma 10.1
with
 y = ϕ(x)= Ms − ηs − ξs ln ( x
2Xs
 ) +1,

X ′ =2Xs,X ′′ = z0,Y ′ = [
ϕ(X ′′)
].

All hypotheses of this lemma are satisﬁed. Integrating, we see that the set E in this
lemma satisﬁes
 Vol(E) ⩾ ξs(z0 − 2Xs) − 2Xs(
ϕ(X ′) − ϕ(X ′′)
)
.

To carry out the integration, it is convenient to take the inverse function of ϕ(x),

x = ϕ
−1(y)= 2Xs exp ( Ms − ηs − y +1
ξs
 ) .

To estimate U , we may compute the number of points (x, y) ∈ Z
2 that satisfy
|x| <z0, M (z0) ⩽ y ⩽ M (x). Using Lemma 10.1, we must take into account the
symmetry of M (x) and exclude the two points with x = ±z0. We organize all points
into groups according to the value of x: x =0, 0 < |x| ⩽ Xs, Xs < |x| ⩽ 2Xs,
2Xs < |x| ⩽ z0. This yields

U ⩾ (
ϕ(X ′) − ϕ(X ′′)
) +2Xs(
Ms − [ϕ(X ′′)
] +1) +2Xs([ϕ(X ′)
] − [
ϕ(X ′′)
] +1)

+2 (
ξs(z0 − 2Xs) − 2Xs(
ϕ(X ′) − ϕ(X ′′)
) − (
ϕ(X ′) − ϕ(X ′′)
2 − 1))

⩾ 2ξsz0 +2Xs(
Ms +1 − ϕ(X ′) − 2ξs) − 2.

On account of (10.7), we get (9.9) for j =1.
The estimate of U in part 2 is the same as that in part 1 for x = Zs, with an
additional term which is at least 2Zsη0s (we use Lemma 10.1 again with another Y ′).
Hence,
 U ⩾ a3 + a1s1 + a2s1Zs
c3 +2 ⩾ a3 + a1s2 + a2s2Xs+1
c3 + a1s1
c3 .

Now, since z1 = Xs+1,we get (9.9) for j = 2. This proves Lemma 10.2.
By the choice of the parameters in (10.5)–(10.10), Lemma 10.2 yields that condi-
tions (9.7), (9.9) of Lemma 9.2 hold. We discuss condition (9.8) in the next section.
Here we assume that (9.8) also holds. Thus we see that the ﬁrst term in f (z, z)is
less that 0.44. If we prove that the second term is also less than 0.44, then we get

756 E. M. Matveev

∣
∣f (z, z)
∣
∣ ⩽ 0.88 and, under the assumption that the linear form in the logarithms
is small, Φs(x, ̃m
′)= 0.
Let us now estimate the second term in (9.10). This term contains the factor∣
∣f (τ )(z, x)
∣
∣/τ ! for our function f (z, ζ). For the derivatives of this function we have

f (τ )
j (z, x)
τ ! = ∑

|˜τ ′|=τ
 ∑(s) L0∑

l0=0 pl0,¯l(¯λ) ∆
(τ0)(Nz, l0,H0,m0)
τ0!

× ∆
(˜ν(¯l ), ̃m
) ( ˜χ(¯l )
2sbn
 )˜τ (ln ˜α)˜τ ˜α ˜χ(¯l )x/(2
sbn)(˜τ !)
−˜1( ∏

σ∈S
∣
∣Φs(x, ̃m
′)
∣
∣σ
)1/κ.

If we replace here ˜α ˜χ(¯l )x/(2
sbn) by ¯α
¯lx/2
s, then, provided that τ + | ̃m
′| ⩽ M (x),
all terms for each ˜τ ′ are zero, and the error term is estimated with the help of (10.3).
The exponential parts of the expressions are estimated as before, as is the denom-
inator. To estimate the polynomial part, we use Lemma 7.3. The estimate (7.8)
is the same for polynomials and their derivatives if we appropriately choose ε3
in (8.16). Note also that we have |z|/′2s ⩽ Z0 for |z| ⩽ Zs, which is taken into
account in (8.14). Thus the polynomial part of f (τ )
j (z, x)/τ ! is estimated as in § 8.
There are new factors in the diﬀerential part. Let us estimate them more
precisely. For ∆
(˜ν(¯l ), ̃m
) we have

∣
∣∆
(˜ν(¯l ), ̃m
)∣
∣ ⩽
 (
| ̃m| +(B1 + B0)M0)| ̃m|

| ̃m|! .

Using (3.1), we similarly get

∑

|˜τ |=µ
 ∣
∣
∣
∣
∣
( ˜χ(¯l )
bn
 )˜τ (ln ˜α)˜τ

(˜τ !)
˜1
 ∣
∣
∣
∣
∣ ⩽
 (
(B2 + B3)M0)µ

µ! ,

where B2, B3 are deﬁned similarly to (5.13):

B3 = max { ∑n−1
j=1 ∣
∣
∣ln(αj) wj bn−wnbj
bn
 ∣
∣
∣ : w ∈W}

M0 ,

B2 = max {∑n−1
j=1 ∣
∣
∣ln(αj) wj bn−wnbj
bn
 ∣
∣
∣ : w ∈ [−0.5, 0.5]
n}

M0 .
 (10.11)

Now we introduce a condition on W which is stronger than (8.10):

W ⩾ ln
(
e(1 + B0 + B1 + B2 + B3)
).

This yields an estimate similar to (8.15):

∑

|˜τ |=µ
 ∣
∣
∣
∣
∣∆
(˜ν(¯l ), ̃m
) ( ˜χ(¯l )
bn
 )˜τ (ln ˜α)˜τ

(˜τ !)
˜1
 ∣
∣
∣
∣
∣ ⩽ (
| ̃m| +(B1 + B0)M0)| ̃m| (
(B2 + B3)M0)µ

| ̃m|! µ!

⩽
 (
M0(1 + B0 + B1 + B2 + B3)
)| ̃m|+µ
(
| ̃m| + µ
)
! ⩽ exp(c0L0)
(2πM0)1/2 .

Explicit lower bound for a homogeneous rational form 757

Thus, changing the condition for W , we can estimate ∣
∣f (τ )
j (z, x)
∣
∣/τ !, x ∈Xs,
τ ⩽ M (x), by the same expression (9.7) as for the function ∣
∣f (z, x)
∣
∣ itself, but
with an extra factor 1.1 · ∣
∣Λlnζ/(2sbn)
∣
∣ from (10.3), provided that we assume the
inductive hypothesis that points already considered satisfy (10.1) or (10.2):

∣
∣
∣
∣
∣ f (τ )
j (z, x)
τ !
 ∣
∣
∣
∣
∣ ⩽ 0.22 ∣
∣
∣
∣Λlnx
2sbn
 ∣
∣
∣
∣ exp
(
a1sj + a2sj|z| + a4|x|
).

(The term a3 ln(R/z0) in the exponent is necessary only for large ζ ∈ Γ(0,R).)
Since we have r ⩽ 1 in (9.10), we can make the second term small if we assume
that |Λ| is small:

1 > ∣
∣
∣
∣ ΛZ0Uln
bn
 ∣
∣
∣
∣ exp(a1s2 + a2s22Xs + a4sZs) ∣
∣
∣
∣ Q(z0)
Q(ζ)
 ∣
∣
∣
∣ (10.12)

for all required U , z0, ln, ζ. This completes the proof of the inductive step.

The rest of this section is devoted to obtaining upper bounds for U =deg Q(ζ)
and V =ln
∣
∣Q(z0)/Q(ζ)
∣
∣ in the second term of the interpolation formula. In the
course of the induction we added new points and increased the multiplicities, there-
fore it suﬃces to consider the second part only (j = 2) with the multiplicities given
by (10.10), and to take δ0 =1, z0 =2n(2Xs +1).
Using the notation of § 9, we deduce from (9.5) that

U =
 T∑

τ =1 uτ ,V ⩽
 T∑

τ =1 uτ ln ( 2ez0
δ0uτ
 ) . (10.13)

Let us estimate uτ =deg qτ . We put

t1 = η0s +2,t2 = t1 + ξsn ln 2,t3 = t2 + ηs,

ϕ(τ )=
 



 2n+1(2Xs +1), 0 ⩽ τ ⩽ t1

2n+1(2Xs + 1) exp ( η0s +2 − τ
ξs
 ) ,t1 <τ ⩽ t2,

2Xs +1,t2 <τ ⩽ t3,

and verify that T ⩽ t3,uτ ⩽ ϕ(τ ), 1 ⩽ τ ⩽ T. (10.14)

The estimate of T follows directly from (10.10) because we have

T = Ms − Ms+1 +1.

To estimate uτ , we recall that qτ (ζ) has zeros x ∈ Z whose multiplicities in Q(ζ)
are at least τ .The case τ> t2 is possible only when M (x) is deﬁned by (10.7),
whence x ∈Xs and we have (10.14) for these τ .

758 E. M. Matveev

Now let τ ⩽ t2.Then M (x) is deﬁned by (10.8) and uτ =2x +1, where x is the
largest number that satisﬁes
 M (x) − Ms+1 +1 ⩾ τ.

Solving this inequality, we get

x ⩽ 2n+1Xs exp ( η0s +2 − τ
ξs
 ) ,

which yields (10.14) for t1 <τ ⩽ t2. The estimate for τ ⩽ t1 is obvious since we
always have x ⩽ 2n+1Xs.
On account of (10.13), (10.14) we can write

U ⩽ ∫ t3

0 ϕ(τ ) dτ, V ⩽ ∫ t3

0 ϕ(τ )ln ( 2ez0
ϕ(τ )
 ) dτ,

and simple integration yields

U ⩽ 2n+1(2Xs + 1)(2 + U0),U0 = η0s + ξs(1 − 2−n)+ ηs2−n−1 (10.15)

and
 V ⩽ 2n+1(2Xs + 1)(2 + V0),

V0 = η0s + ξs(
2 − (2 + n ln 2)2−n) + ηs(
1+(n +1) ln 2)
2−n−1. (10.16)

Recall also that it is enough to estimate U , V for s ⩽ S1 only (where S1 is given
by (4.7)), because Xs, Ms do not change when s> S1, and the inductive step goes
through automatically. The only expression which increases as a function of s is
the denominator in z/2s in the polynomials. But this was taken into account at
the very beginning by putting N =2S in (7.5), (8.1) and (8.14).

§ 11. The choice of the main parameters

Here we specify the values of the parameters introduced above (except for the
ε) to complete all the steps in the proof and to make them compatible with the
parameters of § 2. We ﬁrst show how to complete the ﬁnal part of the proof (see
§ 4). We make some natural assumptions. The ﬁrst of these is that

W ⩾ W0 ⩾ 2c3,c0 ⩾ C0 ⩾ 2c3. (11.1)

Suppose also that for some ε6 we have

ε6 ⩾ 1
L0 ,ε6 ⩾ 1
M0 . (11.2)

The multiplicities Ms+1 in (4.6) must be compatible with Ms+1 in (10.10). This
means that for s ⩽ S1 we must have

ηs + ξsn ln 2 + η0s ⩽ M0
2s+1(1 + ε0) .

Explicit lower bound for a homogeneous rational form 759

However, according to (10.5), (10.6), (8.21), we have

2s+1(ηs + ξsn ln 2 + η0s)

=2s+1 ( a2s1
c3 + a3
2Xs + 3a1s1
2c3Xs + 1
Xs + a2s1n ln 2
2c3 + a1s1
4c3Xs
 )

= (2 + n ln 2)ϑLnD
c3 + L0
X0 + 2
X0 + 3c0L0D(3 + ε2 + ε3 + ε4)
2c3X0

< M0(2 + n ln 2)
c1c3 + M0(
10 + 3(ε2 + ε3 + ε4)+2ε6)

2c2c3 .

Now put

c4 =(2 + n ln 2) n +1
n ,c1 =(1 + ε0) c4
c3 ,

c5 =(n +1) 10 + 3(ε2 + ε3 + ε4)+2ε6
2 ,c2 =(1 + ε0) c5
c3 . (11.3)

This yields the correspondence between (10.10) and (4.6). If s> S1,then we also
have Ms+1 = Ms in both cases. Estimating the decrease of the multiplicities, we
easily get
 MS ⩾ M0 − M0(1 − 2−S)
1+ ε0 = M0(ε0 +2−S)
1+ ε0 .

On account of (11.1), our choice of c2 yields

L0
2X0 < M0
n(1 + ε0) .

Hence, in the right-hand side of (4.11) we have

L0
|XS| < MS
n .

To estimate the remaining terms in the right-hand side of (4.11), we employ the
parameter E1 in (2.2). This yields

LS,1 + ··· + LS,n−1 ⩽ LDϑ(n − 1) E1
2S .

So to verify (4.11) it suﬃces to have

M0 ε0 + 2
−S (n−1)
n
1+ ε0 ⩾ LDϑ(n − 1) E1
2S ,

or, equivalently, ( 2Sε0n
n − 1 +1) c4
c3 ⩾ E1.

760 E. M. Matveev

In particular, it follows that we can take ε0 =0 if E1 ⩽ c4/c3. This is what was
done in previous papers. Then the condition of the type E1 ⩽ c4/c3 gives a lower
bound for the parameters Aj . However, (4.11) may be satisﬁed by an appropriate
choice of S and ε0. In this paper we simply take (in all cases) ε0 = ε6 and choose
S so that 2S ⩾ E1(1 + ε0) n − 1
nc1ε0 . (11.4)

Another condition to be satisﬁed is (9.8), which remained untreated in § 10. Let
us treat it here. Using (10.5), we rewrite it in the form

ec3 exp(c3) ⩽ a1 + a2z1
a4z0 = a1sj + a2sj z1
a4sz0 . (11.5)

We ﬁrst show that the minimum of the right-hand side is attained for j = 1 (part 1
of the inductive step) and for

z1 = z0 = Zs =2n+1Xs. (11.6)

The worst value of z1 for j = 1 is obvious. It remains to compare the case j =1
with the case j =2, where

z1 =2Xs,z0 =2n+1Xs +0.5 ⩽ 2n+1Xs
 (
1+ 2−n−2

X0
 ) .

We must show that

a1s1 + a2s12n+1Xs
a4s2n+1Xs ⩽ a1s2 + a2s22Xs

a4s2n+1Xs (
1+ 2−n−2
X0
 ) .

Using (8.21), (10.5) and the formulae [L1 : Q]/κ = D,[L2 : Q]/κ =2nD,we
rewrite this inequality as

1
2n+2c4 ⩽ (3 + ε2 + ε3 + ε4)(2n − 1 − 2−n−2),

and it becomes evident because of (11.1), (11.3). Thus we have to verify (11.5) for
j = 1 and for z0, z1 in (11.6).
Multiplying (11.5) by ϑ
∗ = ε∗ + ϑ
∗
0 (see (5.11), (5.12)) and using the nota-
tion (10.5), we can rewrite (11.5) in the form

(ε∗ + ϑ
∗
0)ec3 exp(c3) ⩽ c0L0(3 + ε2 + ε3 + ε4)D
2n+1LX0 + ϑnD.

To do so, we require that ϑ
∗
0ec3 exp(c3)= ϑnD (11.7)

and ε∗ec3 exp(c3) ⩽ c0L0(3 + ε2 + ε3 + ε4) D
2n+1LX0 . (11.8)

Explicit lower bound for a homogeneous rational form 761

On account of the notation (5.11), (8.21), the last inequality can be rewritten as

E2Dnec3 exp(c3) ⩽ M0(3 + ε2 + ε3 + ε4)
2nc2 ,

E2 = max
{∣
∣± ln(α1) ± ··· ± ln(αn)
∣
∣}

nD ,
 (11.9)

and this will be satisﬁed by choosing M0 large.
We regard (11.7) as the deﬁnition of ϑ
∗
0. This requires some caution because
the condition (5.7), which involves ϑ
∗
0, plays an important role in the deﬁnition of
the set W and hence inﬂuences ϑ in (5.8). To simplify the problem, we proceed as
follows. Consider a body W0 given by the same formulae as W, but without the
condition (5.7). It is independent of ϑ
∗
0. We have the equation h(¯α, W0)= ϑ for
some ϑ.As W⊆ W0, we can take the same ϑ for W by Lemma 3.2.
From now on, we assume that the sets W, W0 are deﬁned by (5.5), (5.6), with the
addition of (5.7) for W. According to the product formula, this yields (5.9) with ϑ
as in (2.1). Note that the numbers B0, B1, B2, B3 are determined by (5.13), (10.11)
more precisely than by (2.7). Now apply Lemma 5.1 with ϑ
∗
1 = ELnD/2 and with
E as in (2.2). Taking
 η−1 = ϑ
∗
1
Lϑ∗
0 = eEc3 exp(c3)
2ϑ ⩾ 1

(with ϑ
∗
0 as in (11.6) and with η−1 ⩾ 1 by (2.3)), we get W = W∩ ηE. It follows
that we may take
 Ω0 =Ω (
Eec3 exp(c3)
2ϑ
 )ρ ⩾ Ωen. (11.10)

When estimating linear forms in logarithms, it is important to minimize ω0
and the other parameters in (8.21). If E is small, then the choice c3 = C∗
3 is
good enough. If we have no information about the numbers αj, except for Aj ⩾
max{
h(αj), | ln αj|/D}
,then ϑ ⩽ 1, E ⩽ 1, and we may put c3 = 1 (or another
constant). This is what was done (less explicitly) in the papers of other authors.
The main idea of this paper that enables us to eliminate the factor nn from the
estimates is a better choice of c3.When c3 = n/ρ, the dependence of ω0 on c3 takes
the form (
c3 exp(c3)
)ρ

cn
3 = ( n
ρ
 )ρ−n en,

which yields nn in the denominator and eliminates this factor from the estimates.
When we want to use the possibility that E is small, we should put c3 = C3
with C3 as in (2.3). Then, choosing an appropriate ε0,we have c1 = C1 for c1 as
in (11.3) and C1 as in (2.4). The choice of c3 admits minor improvements which
will not be discussed here.
Now let us show how to simplify condition (11.8).
There is a connection between the parameters E2 and E.We have

E2 ⩽ max { | ln αj|
D :1 ⩽ j ⩽ n} ⩽ nEA, A =max{Aj :1 ⩽ j ⩽ n},

762 E. M. Matveev

so to satisfy (11.9) it suﬃces to have

EADn
2ec3 exp(c3) ⩽ 3M0
2nc2 .

By (11.10), (8.21), M0 contains ρ factors which are at least Eec3 exp(c3)/(2ϑ) ⩾
en/ρ. Hence we may simplify the last inequality by removing all ε and using (11.3).
This results in the inequality

D(c1Dϑ)
n−1 ( Ω
A
 )( c0
2c3
 )(
Eec3 exp(c3)
2ϑ
 )ρ−1 6(
6(2 + n ln 2) + 5n) (n +1)nn

2nn3n! ⩾ 1.

(11.11)
On account of (11.1), this inequality follows from (2.11). In the case of Theorem 2.3,
it will be veriﬁed by a direct computation.

§ 12. Proof of Theorem 2.1

It remains to choose small ε that satisfy the corresponding conditions, guarantee
that X0,L0,M0 ∈ Z (see (8.21)), choose S in § 4and H0 in § 8, and see how small
|Λ| must be in order to satisfy (10.4), (10.12). For brevity we put

ωj = ω0
Ajc1Dϑ , 1 ⩽ j ⩽ n,

with ω0 as in (8.21). Note that ω0 = ω,where ω is as in (2.5). Using (11.1), (2.9),
(2.10), (11.1), (11.10), we have

Dωj min{c0,W }
2c3 ⩾ 1, 0 ⩽ j ⩽ n. (12.1)

We put (see (8.8), (8.12), (8.16), (8.20), (8.21), (11.2))

ε0 = ε6 = e−2n

148 ,

1+ ε1 = (
1+ (n +1)ε6
2
 )n , (12.2)

ε2 = e−n

72 ,ε3 = e−n

91 ,

ε4 = e−2n

109 ,ε5 = 1
10n +11 .

We also introduce the following auxiliary functions:

ξ1 = ξ1(n)= (1 + ε0)(1 + ε1) (
(2 + ε5)(3 + ε2 + ε3)+(1 + ε5) c5
c4
 ) 4c5en nn

n! ,

ξ0 = ξ0(n)= ln ξ1(n),ξ2 = ξ2(n)= (
ξ1(n)ξ0(n)
)1/2
 (12.3)

Explicit lower bound for a homogeneous rational form 763

(c4, c5 are given in (11.3), whence ξ0, ξ1, ξ2 are independent of c3). One easily
sees that ξ1(n)/e2n ≫ n1/2, and a simple calculation (for small n) shows that the
minimal value of ξ1(n)/e2n (> 148) is attained at n = 2. The same estimate holds
for large n on account of the growth of the function. This yields

ξ1(n) ⩾ 148e2n. (12.4)

Moreover, it is easy to see that for C2 as in (2.4) we have

1 ⩽ C2
ξ1(n)
2c3 ⩽ 1.03. (12.5)

In other words, C2 is a simpliﬁed expression for ξ1/(2c3).
Now we estimate X0 in (8.21) with c2 given by (11.3). By (11.1) we have X0 >
10(n + 1), whence X0 ⩾ 10n +11 and ε5 satisﬁes (8.21). To obtain that X0 ∈ Z,
we note that W0 in (2.7) satisﬁes the same conditions as W ,and we take W =
W0(1 + εX ) with some εX such that

0 ⩽ εX ⩽ ε7 = 1
2c5 . (12.6)

This enables us to guarantee that X0 ∈ Z. The factor (1 + ε7) will be added to the
ﬁnal estimate for |Λ|. We easily see that putting

L0 = [ Dω0ξ1W
2c3
 ] +1 = (1+ εL) Dω0ξ1W
2c3 ,

M0 =(1 + εL) Dω0ξ1c0
2c3 ,

L
Aj =(1 + εL)Dωj
 ( ξ1
n
 ) c0
2c3 ,
 (12.7)

yields L0 ∈ Z, M0 ∈ Z,where εL and c0 satisfy

0 ⩽ εL ⩽ ε6,C0 ⩽ c0 ⩽ (1 + ε6)C0, (12.8)

with C0 given in § 2. Moreover, (2.6) implies that C0 satisﬁes all conditions for c0.
We also have (11.2) by (12.1), (12.3), (12.4). The factor (1 + ε6)
2 must be added
to the ﬁnal estimate of |Λ|. Now we deﬁne the numbers

L′
n =(1 + εL)ξ1 max { Dωnc0
2c3 , c0
2c3 , E1c3
c4
 } ,

S = [
log2
 ( 2L′
n
n
 )] ,H0 = [ ξ2W
C0
 ] +1,L−1 = [ L0
H0
 ] . (12.9)

Note that S satisﬁes (11.4) and S ⩾ [log2(2L0,n)
].
We need the following inequality for c0:

c0 ⩾ ln
(
(1 + ε6)DL′
n) ⩾ ln
(
(1 + ε6)ξ1D) ⩾ ξ0. (12.10)

This follows from (2.5), (12.5), (12.8).

764 E. M. Matveev

Now we verify the conditions (8.13), (8.14). Using the inequalities above, we
deduce in (8.13) that

ln (
2.8361H0 M0 + L−1 +1
L0
 )

⩽ ln (
2.8361(ξ2 +1) (
1+ 1
ξ1 + 1
ξ2
 ) c0
2c3
 ) ⩽ ln(L′
n) ⩽ c0.

To prove (8.14), we similarly obtain

ln (
e (
1+ N (Z0 +0.5)
H0
 ))

⩽ ln (
DL′
n(1 + ε6)(1 + ε5)e2n+2 2c5
ξ2
 ) ⩽ ln
(
DL′
n(1 + ε6)
) ⩽ c0

(N , Z0 are given by (8.5), (10.8)). Here we have used the inequalities

ξ1 ⩾ 2.8361(ξ2 +1) (
1+ 1
ξ1 + 1
ξ2
 ) ,

ξ2 ⩾ (1 + ε5)e2n+2 2c5
ξ2 ,

which may be veriﬁed by a calculation.
As the next step, we verify that the numbers ε in (12.2) satisfy the inequalities
in which they appear. Actually (12.2) gives simpliﬁed expressions. More precise
expressions will be obtained in the course of the argument. The inequalities (11.2)
for ε6 follow directly from (12.4) (we must only have ε6 ⩾ 1/ξ1). Let us verify that
ε2 satisﬁes (8.12). On account of (7.2), (7.7), (12.10) it suﬃces to prove that

ε2 ⩾ ln(2πH0)
2c0H0 + 1
12c0H 2
0 .

We shall repeatedly use the following simple inequalities: x ⩽ ex/e,ln x ⩽ x/e,
x> 0. By (12.3), (12.9) we easily get

1
12c0H 2
0 ⩽ 1
12ξ0ξ2
2 .

To complete the proof of (8.12), put

x =
 πξ2W
c3
DL′
n ⩽
 πξ2W
c3
ξ1 .

Then the inequalities (11.1), (12.4), (12.10), (12.12) yield that

ln(2πH0)
2c0H0 ⩽ ln ( 2πξ2W
2c3
 )

2c0ξ2W
2c3 = ln(DL′
n)+ln x

2c0ξ2W
2c3 ⩽ 1
2ξ2 + x
ec0ξ2 W
c3 ⩽ 1
2ξ2 + π
eξ0ξ1 .

Explicit lower bound for a homogeneous rational form 765

Hence (8.12) holds if we have the inequality

ε2 ⩾ 1
2ξ2 + π
eξ0ξ1 + 1
12ξ0ξ2
2 .

This inequality follows easily from (12.13).
Let us verify that ε3 in (12.3) satisﬁes (8.16). We begin by estimating |L0|.
Using (5.10), (8.21) and the notation there, we get

Ln

Ω0 = M n
0
Ω0(c1nDϑ)n = ( (1 + εL)ξ1
en
 )n ωn−1
0 Dc0
2c3 .

Since ε6 is small, we obtain

|L0| ⩽ Ln
Ω0 +1 ⩽
 (
1+(neε6)
n)
Ln

Ω0 < (1 + ε6)Ln

Ω0 .

Hence for J =(L0 +1)|L0| as in (8.6) we have

J ⩽ (1 + ε6)
2Dω0ξ1
 ( Ln

Ω0
 ) W
2c3

⩽ (
(1 + ε6) ω0c0
2c3en
 )n (
(1 + ε6)ξ1D)n+1 W
2c3

⩽ D−n (
(1 + ε6) Dω0
2c3en
 )n (
(1 + ε6)ξ1D)n+1 W
2c3

⩽ D−n exp ( W
2c3e +(1 + ε6) Dω0
e2n +(n +1)c0
)

⩽ D−n exp
 (

c0L0
 1
e + 1+ε6
e2n + n+1
2c3
ξ1
 )
 . (12.11)

On account of (7.9), the sum in (8.16) is estimated by

L0∑

l0=0
 ∑

τ +m0⩽l0 δ(l0,m0,τ ) 20
(2πM0)1/2 ⩽ e(H0−1)/e ⩽ ec0L0/(eξ2).

Since c3 ⩾ n/ρ ⩾ n/2, this together with (12.11) implies that (8.16) holds if we
have
 ε3 ⩾ 1
eξ2 +
 1
e + 1+ε6
e2n +1+ 1
n
2ξ1 .

But the condition (12.3) for ε3 is stronger than this.
It remains to verify (8.20) (for ε4) with γ given by (6.4). As J is estimated
by (12.11), we need only estimate ∣
∣∆(K)
∣
∣1/2DK . Since the right-hand side of (12.11)
contains D−n ⩽ 2D−1
K , it suﬃces to estimate DKh(αj) when we use (6.6). By (2.1)
we have
 DKh(αj) ⩽ κDnϑAj ⩽ κnDϑAj Dωj W
2c3 = κnDω0 W
2c3c1

⩽ κnDω0
 ( c3
c4
 ) W
2c3 ⩽ c0L0κ n
2c4ξ1 .

766 E. M. Matveev

This together with (12.11) shows that it is suﬃcient to have

ε4 ⩾ n
c4ξ1 +
 1
e + 1+ε6
e2n +1+ 1
n
2ξ1 .

But again the condition (12.3) for ε4 is stronger.
To end this section, we verify the inequalities of § 10, wherewe haveusedthe
assumption that the linear form in logarithms is small. This occured twice: when
we estimated the ﬁrst term of the interpolation formula in (10.4) and when we
estimated the second term in (10.12).
Let us see how small |Λ| must be to guarantee (10.12). We estimate the compo-
nents in the exponent of this condition by comparing them with the expression

F =2nDc0L0. (12.12)

Using (10.5), (10.6), (8.21), (11.3), we get

a1s2 =(3 + ε4 + ε6)F, a2s22Xs = ( 2c5
c4
 ) F. (12.13)

To estimate a4sZs, we use (10.8), (5.12), (11.7), (11.8). We get

a4sZs =2n+1ϑ
∗LX0 =2n+1(ϑ
∗
0 + ε∗)LX0

⩽ 2n+1ϑnDLX0 + c0L0D(3 + ε2 + ε3 + ε4)
ec3 exp(c3)

⩽ 2
 ( c5
c4 +3+ ε2 + ε3 + ε4) F

ec3 exp(c3) . (12.14)

To estimate V =ln
∣
∣Q(z0)/Q(ζ)
∣
∣, we use (10.15). We recall that it suﬃces to
consider s ⩽ S1 only, where S1 is given by (4.7). Then

Vs1 =2n+3Xs ⩽ 2n+3+sX0 ⩽ 2n+3X0M0 ⩽ 4c2F,

Vs2 =2n+2Xsη0s =(3 + ε2 + ε3 + ε4) F
c3 ,

Vs3 =2n+2Xsξs =2n+2X0ϑLn D
2c3 = 2c5
c3c4 F,

Vs4 =2n+2Xsηs =2Vs3 +2Vs2 +2n+1L0 +2n+2

⩽ 2Vs2 +2Vs3 + F ( 2
ln(ξ1) + 4
ξ2
2
 ) ,

V ⩽ (1+ ε5
2
 ) (
Vs1 + Vs2 + Vs3(
2 − (2 + n ln n)2−n)

+ Vs4(
1+(n +1) ln 2)
2−n−1)
.
 (12.15)

Using (10.15), we similarly get an estimate for U :

U ⩽ (1+ ε5
2
 ) (
Vs1 + Vs2 + Vs3(1 − 2−n)+ Vs42−n−1) = c6F, (12.16)

Explicit lower bound for a homogeneous rational form 767

where c6 = c6(n) is a parameter which may be obtained from (12.15). Note that
c6 contains c3 in the denominator of some terms. Hence we can simplify c6 by
replacing the c3 by n/2 ⩽ n/ρ ⩽ c3. It is easy to see that c6 ≪ 1, and a computer
check yields that the maximal value of c6 (< 71) is attained at n = 2. Using (12.16),
(12.12), (12.7), (12.10), (12.5), we then have

ln U ⩽ n ln 2 + ln(c6)+ln(DW ω0)+ln (
(1 + ε6) ξ1c0
2c3
 )

⩽ n ln 2 + ln(c6)+ DW ω0
e + c0 ⩽ 2−nε6
 (
n ln 2 + ln(c6)+ 1
e +1) F.
(12.17)

Moreover, (10.12) contains the expression |Z0ln/bn|,which may be estimated
with the help of (8.14), (12.5), (12.9) as follows:

ln ∣
∣
∣
∣ Z0ln
bn
 ∣
∣
∣
∣ ⩽ ln ( eZ0N
H0
 ) +ln (
(ξ2 +1) W
2c3e
 )

⩽ c0 + W
2c3e2 +ln
(
ξ1(n)
) ξ2 +1
eξ1 ⩽ F 2−n 2+ e−2 + ξ2
ξ1 . (12.18)

Replacing the expressions in (10.12) by their bounds in (12.11)–(12.18), we see that
to satisfy (10.12) it suﬃces to have

ln |Λ| < −c7F (12.19)

with some parameter c7, which may be given explicitly.
Now let us study condition (10.4). It is much simpler than (10.12), but it contains
|ζ/2s| with |ζ| = R =(U − a3)/a4 given in (9.7). Hence we need a lower bound for
a4s2s. This can be obtained as in the proof of (12.14):

a4s2s = ϑ
∗
0L ⩾ M0
c1ec3 exp(c3) ⩾ exp(−c0) ⩾ exp(−ε6F ).

We see that the condition (10.4) is weaker than (10.12).
It remains to return to the original notation C0, W0 of § 2. We see from
(12.6)–(12.9) that (12.19) follows from

ln |Λ| < −(1 + ε7)(1 + ε6)
2ξ1c72nC0ωD W0
2c3 . (12.20)

But this leads to a contradiction. Hence (12.20) is not true.
A computer check shows that (12.5) holds and that

(1 + ε7)(1 + ε6)
2c7 ⩽ 91.

Hence, on account of (12.5), (2.12) follows from the negation of (12.20). This proves
Theorem 2.1.

768 E. M. Matveev

§ 13. Proof of Theorem 2.2

It follows from (2.13) that ϑ =1, E =1, C3 = n/ρ satisfy conditions (2.1),
(2.2), (2.3) respectively. In (2.6) we also have

Dω
C1ϑAn ⩾ 1 ⩾ E1
C1 .

We put C0 =1.23C′
0,where C′
0 is given by (2.15), and show that this C0 satis-
ﬁes (2.6). From (2.4), (2.11) we obviously have

C0 ⩾ C′
0 ⩾ ln ( C2Dω
C1An
 ) ⩾ 2n ⩾ 2n
ρ =2C3.

It remains to verify that 0.23C′
0 ⩾ ln C0 =ln(1.23C′
0). Writing C2 = C2(n)and
using the inequality C0 ⩾ ln C2(n), we get

ln(1.23C′
0)
C′
0 ⩽ ln
(
1.23 ln C2(n)
)

ln C2(n) ⩽ ln(
1.23 ln C2(2)
)

ln C2(2) ⩽ 0.23.

This proves (2.6).
We also have (2.11), (2.9), (2.10) for this C0.
It remains to show that we may take W0 =ln(2eB) in (2.8), where B is given
in (2.14). Since bn ̸=0, we have B ⩾ 1. Now we estimate the components of W0
in (2.7). Using (2.10), (2.13), we get

|bj|
ω = (bj|Aj /An
AjC1D/ωn ⩽ B, 1 ⩽ j ⩽ n.

Hence B0 <nB/C2 <B/(8n). Also, we have

|bn|
AjC1D = |bn|An/An
Aj C1D ⩽ B, 1 ⩽ j ⩽ n − 1,

as well as |bj|
AnC1D = |bj|Aj/An
AjC1D ⩽ B, 1 ⩽ j ⩽ n − 1.

Hence B1 ⩽ (n − 1)B/n.We also have

| ln αj |
ω =
 | ln αj |
DAj
ωjC1 ⩽ 1
C1 ⩽ B
C1

and |bj ln αj|
ω = ∣
∣
∣
∣ bjAj
An
 ∣
∣
∣
∣
 | ln αj |
DAj
ωjC1 ⩽ B
C1 .

Hence B2 ⩽ nB/(C1C2) ⩽ B/(8n). Finally, we have | ln αj |/(DAj) ⩽ 1 ⩽ B,as
well as |bj ln αj|
DAn = ( |bj|Aj
An
 ) | ln αj |
DAj ⩽ B.

Hence B3 ⩽ B(n − 1)/n.

Explicit lower bound for a homogeneous rational form 769

Combining these inequalities, we see that we may take

W0 =max
{2n/ρ, ln
(
e(
1+2B(1 − 1/(8n))
))}
.

This is still not exactly what we need, but it yields Theorem 2.2 if B is large enough.
It remains to show that we may assume ln(2eB) ⩾ 2n without loss of generality.
The parameter B of the form (2.14) is very convenient for stating estimates of
Liouville type.

Lemma 13.1. Suppose that Λ is given by (1.2), Aj ⩾ h(αj ), 1 ⩽ j ⩽ n, An > 0,
Λ/(2πi) /∈ Z, B is given by (2.14).Then

|eΛ − 1| ⩾ 21−D exp(−nDBAn).

Proof. This estimate follows immediately from the product formula for the algebraic
number γ = eΛ − 1= ¯α
¯b − 1 ̸=0.

Now assume that (2.12) does not hold. Then |Λ| < 0.1 and we have |γ| ⩽ 1.1|Λ|,
where γ is given in Lemma 13.1. This yields

− 91 · 2nC2C0Dn+2ω ln(2eB) ⩾ ln |Λ|

⩾ ln |γ|− ln(1.1) ⩾ (1 − D)ln2 − nDBAn − ln 1.1.

Since C2 is large in (2.4), we get

nDBAn ⩾ 90 · 2nC2C0Dn+2ωW0,

or
 B ⩾ 90 · 2nC2C0 Dn+1ω
Ann W0. (13.1)

In particular, B ⩾ C2D2ωnC0 ⩾ e2n and W0 =ln(2eB) satisﬁes (2.8), (2.9),
(2.10). This proves Theorem 2.2.

Remark. We see from (13.1) that to obtain non-trivial estimates for linear forms
in logarithms we must take suﬃciently large B in Theorem 2.2. This means also
that the estimate (2.16) undergoes no essential changes if we replace ln(2eB)by
ln(BF ), where F is of order ≪ Dω/An.

§ 14. Proof of Theorem 2.3

Let pk be the kth prime number.

Lemma 14.1. Let α1,...,αn be multiplicatively independent rational numbers.
Then they can be re-indexed in such a way that

h(αk) ⩾ ln pk, 1 ⩽ k ⩽ n.

Proof. Since the αj are multiplicatively independent, their factorizations into
primes contain at least n primes. If the greatest of these is p ⩾ pn, assign the

770 E. M. Matveev

index n to a number α that involves p.Then h(αn) ⩾ ln pn. By repeating this for
the remaining α, we complete the proof of Lemma 14.1.

Now we assume the hypotheses of Theorem 2.3. Note that here D = κ = ρ =1,
which simpliﬁes our task. Since C3 = n,we have

C1 ⩾ (2 + n ln 2) n +1
n2 . (14.1)

When K = Q,we have Aj ⩾ h(αj) ⩾ | ln αj |. Hence E = 1 satisﬁes (2.2). If
E =1, ϑ ⩽ 1, then C3 = n satisﬁes (2.3). From Lemma 14.1 we get the inequalities

Ω ⩾ Ω
∗
n =
 n∏

k=1 ln pk, Ω
Aj ⩾ Ω
∗
n−1,

DϑE1 ⩽ E∗
n = 1
(n − 1)
 n−1∑

k=1
 1
ln pk .

Lemma 14.2. (i) If C1 is given by (14.1),then

Cn
1 Ω
∗
nne
2 ⩾ 2.6n, Cn−1
1 Ω
∗
n−1ne
2 ⩾ 2.53n−1,

Cn−1
1 Ω
∗
n−1 > 1, E∗
n
C1 < 1.

(ii) For ϑ =1/(
2 − 2/(nen+1)
) we have

(ϑC1)
nΩ
∗
n ne
2ϑ ⩾ 1.39n, (ϑC1)
n−1Ω
∗
n−1 ne
2ϑ ⩾ 1.37n−1,

(ϑC1)
n−1Ω
∗
n−1 > 0.4, E∗
n
ϑC1 < 1.33.

Proof. For n ⩽ 100, the lemma is veriﬁed by direct calculation. When n = 100, we
also verify that (ln 2)
nΩ
∗
n ⩾ 2.8n,E∗
n ⩽ 0.5ln 2.

We also have ln pk > 6for k ⩾ 100. Since C1 > ln 2 and ϑ> 0.5, this proves the
lemma for n ⩾ 100 as well.

Let us consider case (i) of Theorem 2.3. Since Aj ⩾ h(αj), ϑ = 1 satisﬁes
condition (2.1). Lemma 14.2 (case (i)) guarantees that conditions (2.9)–(2.11)
of Theorem 2.1 hold. Hence case (i) of Theorem 2.3 is a direct consequence of
Theorems 2.1 and 2.2.
In case (ii) of Theorem 2.3, Lemma 14.2 again guarantees that conditions
(2.9)–(2.11) hold, but ϑ =1/(
2 − 2/(nen+1)
) may not satisfy (2.1). To prove
case (ii) of Theorem 2.3, we repeat the proof of Theorem 2.1, but without simplify-
ing the expression for ϑ. Therefore we must verify that our ϑ satisﬁes the conditions
of § 5.
 Explicit lower bound for a homogeneous rational form 771

We take the body W to be the same as in Theorem 2.1, taking into account
that ϑ
∗
0 is deﬁned by (11.7) for C3 = n. Now we estimate h(¯α, W). Since αj ∈ Z,
the contribution of the non-Archimedean valuations to the estimate of h(¯α, W)
equals ∑

σ>1 sup

{ n∑

j=1 ln |αj |σwj : w ∈W
}
 ⩽ ∑

σ>1
 n∑

j=1 − ln |αj|σ
2Aj = n
2 .

The contribution of the unique Archimedean valuation is ϑ
∗
0 by (11.2). Hence,
in (5.8) we have
 ϑ ⩽ h(¯α, W) ⩽ n
2 + ϑ
∗
0 = n ( 1
2 + ϑ
nen+1
 ) ,

and simple substitution shows that our ϑ is compatible with (11.3). We also
deduce (11.11) from Lemma 14.2(ii). This completes the proof of Theorem 2.3.

Bibliography

[1] A. M. Baker, “The theory of linear forms in logarithms”, Transcendence theory: advances
and applications (A. Baker, D. W. Masser, eds.), Academic Press, London 1977, pp. 1–27.
[2] J. H. Loxton and A. J. van der Poorten, “Computing the eﬀectively computable bound
in Baker’s inequality for linear forms in logarithms”, Bull. Austral. Math. Soc. 15 (1976),
33–57.
[3] A. Baker and H. M. Stark, “On a fundamental inequality in number theory”, Ann. of Math.
94 (1971), 190–199.
[4] M. Waldschmidt, “A lower bound for linear forms in logarithms”, Acta Arithm. 37 (1980),
257–283.
[5] A. O. Gelfond, Transcendental and algebraic numbers, Gostekhizdat, Moscow 1952; English
transl., Dover Publ., New York 1960.
[6] T. N. Shorey, “On linear forms in the logarithms of algebraic numbers”, Acta Arithm. 30
(1976), 27–42.
[7] N. I. Fel’dman, “Estimation of the absolute value of a linear form in logarithms of certain
algebraic numbers”, Mat. Zametki 2 (1967), 245–256; English transl., Math. Notes 2 (1967),
634–640.
[8] E. M. Matveev, “Linear forms in the values of G-functions, and Diophantine equations”,
Mat. Sb. 117 (1982), 379–396; English transl. in Math. USSR–Sb. 45 (1983).
[9] C. L. Stewart and Kunrui Yu, “On the abc conjecture”, Math. Ann. 291 (1991), 225–230.
[10] B. M. M. de Weger, “The weighted sum of two S-units being a square”, Indag. Math. 1:2
(1990), 243–262.
[11] E. M. Matveev, “An estimate of a linear form in the logarithms of algebraic numbers”,
Abstracts of the conf. “The theory of transcendental numbers and its applications” (Moscow,
2–4.02.1983), Moscow State Univ. Press, Moscow 1983. (Russian)
[12] J. H. Loxton, M. Mignotte, A. J. van der Poorten and M. Waldschmidt, “A lower bound for
linear forms in the logarithms of algebraic numbers”, C. R. Math. Rep. Acad. Sci. Canada.
11 (1987), 119–124.
[13] J. Blass, A. M. W. Glass, D. K. Manski, D. B. Meronk and R. P. Steiner, “Constants for
lower bounds for linear forms in the logarithms of algebraic numbers. I, II”, Acta Arithm.
55 (1990), pp. 1–14, 15–22; Corrigenda in: Acta Arithm. 65 (1993), 383.
[14] G. W¨ustholz, “A new approach to Baker’s theorem on linear forms in logarithms. III”, New
advances in transcendence theory (A. Baker, ed.), Cambridge Univ. Press, Cambridge 1988,
pp. 399–410.
[15] P. Philippon and M. Waldschmidt, “Lower bounds for linear forms in logarithms”, New
advances in transcendence theory (A. Baker, ed.), Cambridge Univ. Press, Cambridge 1988,
pp. 280–312.

772 E. M. Matveev

[16] M. Mignotte and M. Waldschmidt, “Linear forms in two logarithms and Schneider’s
method. II”, Acta Arithm. 53 (1989), 251–287.
[17] M. Waldschmidt, “Minorations de combinaisons lin´eaires de logarithmes de nombres
alg´ebriques”, Canad. J. Math. 45:1 (1993), 176–224.
[18] A. Baker and G. M. W¨ustholz, “Logarithmic forms and group varieties”, J. Reine Angew.
Math. 442 (1993), 19–62.
[19] Y. Bugeaud and K. Gy¨ory, “Bounds for the solutions of Thue-Mahler equations and norm
form equations”, Acta Arithm. 74 (1996), 273–292.
[20] E. M. Matveev, “On linear and multiplicative relations”, Mat. Sb. 184:4 (1993), 23–40;
English transl., Russ. Acad. Sci. Sb. Math. 78 (1994), 411–425.
[21] S. Lang, Fundamentals of Diophantine geometry, Springer–Verlag, New York 1983; Russian
transl., Mir, Moscow 1986.
[22] N. I. Fel’dman, “An improvement of the estimate of a linear form in the logarithms
of algebraic numbers”, Mat. Sb. 77 (1968), 423–436; English transl., Math. USSR–Sb. 6
(1968), 393–406.
[23] A. J. van der Poorten, “On Baker’s inequality for linear forms in logarithms”, Math. Proc.
Cambridge Philos. Soc. 80 (1976), 233–248.
[24] K. Leichtweiss, Konvexe Mengen, Springer–Verlag, Berlin–Heidelberg–New York 1980;
Russian transl., Mir, Moscow 1985.
[25] J. W. S. Cassels, An introductiion to Diophantine approximation, Cambridge Univ. Press,
Cambridge 1957; Russian transl., IL, Moscow 1961.
[26] E. Bombieri and J. M. Vaaler, “On Siegel’s Lemma”, Invent. Math. 73 (1983), pp. 11–32;
Addendum in: Invent. Math. 75 (1984), 377.
[27] E. M. Matveev, “On the arithmetic properties of the values of generalized binomial
polynomials”, Mat. Zametki 54:4 (1993), 76–81; English transl., Math. Notes 54 (1993),
1031–1034.
[28] N. I. Fel’dman, “An eﬃctive reﬁnement of the exponent in Liouville’s theorem”, Izv. Akad.
Nauk SSSR Ser. Mat. 35 (1972), 973–990; English transl., Math. USSR–Izv. 5 (1971), 985–
1002.

Moscow State Textile Academy
Chair of Higher Mathematics Received 24/JUL/96
Translated by A. V. DOMRIN

Typeset by AMS-TEX
