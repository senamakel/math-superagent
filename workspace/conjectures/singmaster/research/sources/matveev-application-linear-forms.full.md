<!-- source: https://hal.science/hal-03243010/document | converted from PDF -->

HAL Id: hal-03243010

https://hal.science/hal-03243010v1

Preprint submitted on 31 May 2021

HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
 L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.

HAL Authorization

On solutions of the Diophantine equation L n + L m = 3 a

Pagdame Tiebekabe, Ismaïla Diouf

To cite this version:

Pagdame Tiebekabe, Ismaïla Diouf. On solutions of the Diophantine equation L n + L m = 3 a. 2021. ⟨hal-
03243010⟩

MALAYA JOURNAL OF MATEMATIK
Malaya J. Mat. 9(02)(2021), 1–11.
http://doi.org/10.26637/mjm902/001

On solutions of the Diophantine equation Ln + Lm = 3
a

PAGDAME TIEBEKABE *1,2 AND ISMA¨ILA DIOUF1

1 Cheikh Anta Diop University, Faculty of Science, Department of Mathematics and Computer science, Laboratory of Algebra, Cryptology,
Algebraic Geometry and Applications (LACGAA) Dakar, Senegal.
2 University of Kara, Sciences and Tecnologies Faculty (FaST), Department of Mathematics and Computer science, Kara, Togo. PoBOX: 43

Received 12 November 2020; Accepted 17 March 2021

Abstract. Let (Ln)n≥0 be the Lucas sequence given by L0 = 2, L1 = 1 and Ln+2 = Ln+1 + Ln for n ≥ 0. In this
paper, we are interested in ﬁnding all powers of three which are sums of two Lucas numbers, i.e., we study the exponential
Diophantine equation Ln + Lm = 3a in nonnegative integers n, m, and a. The proof of our main theorem uses lower bounds
for linear forms in logarithms, properties of continued fractions, and a version of the Baker-Davenport reduction method in
Diophantine approximation.

AMS Subject Classiﬁcations: 11B39, 11J86

Keywords: Linear forms in logarithm, Diophantine equations, Fibonacci sequence, Lucas sequence, perfect powers.

Contents

1 Introduction 1

2 Preliminaries 2
2.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.2 Inequalities involving the Lucas numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.3 Linear forms in logarithms and continued fractions . . . . . . . . . . . . . . . . . . . . . . . . 4

3 Main Results 5

4 Reducing of the bound on n 9

5 Acknowledgement 10

1. Introduction

The determination of perfect powers of Lucas and Fibonacci sequences does not date from today. The real
contribution of determination of perfect powers of Lucas and Fibonacci sequences began in 2006. By classical
and modular approaches of Diophantine equations, Bugeaud, Mignotte, and Siksek [5] deﬁned all perfect powers
of Lucas and Fibonacci sequences by solving the equations Fn = yp and Ln = yp respectively. From there,
many researchers tackled similar problems. It is in the same thought that, others have determined the powers of
2 of the sum/difference of two Lucas numbers [3], powers of 2 of the sum/difference of Fibonacci numbers [4],
powers of 2 and of 3 of the product of Pell numbers and Fibonacci numbers.

∗Corresponding author. Email addresses: pagdame.tiebekabe@ucad.edu.sn (Pagdame Tiebekabe),
ismaila.diouf@ucad.edu.sn (Isma¨ıla Diouf)

https://www.malayajournal.org/index.php/mjm/index ©2021 by the authors.

Pagdame Tiebekabe and Isma¨ıla Diouf

We move our interest on the powers of 3 as a sum of two Lucas numbers. This paper follows the following
steps : We ﬁrst give the generalities on binary linear recurrence, then we demonstrate an important inequality on
Lucas numbers and ﬁnally determine and reduce a coarse bound by section 3. The section 4 is devoted to the
reduction of the obtained bound in section 3 and discussion of possible different cases. We know from Bravo and
Lucas [3] that the only solutions of the Diophantine equation Fn + Fm = 2
a in positive integers n, m and a with
n ≥ m are given by 2F1 = 2, 2F2 = 2, 2F3 = 4, 2F6 = 16,

and F2 + F1 = 2, F4 + F1 = F4 + F2 = 4, F5 + F4 = 8, F7 + F4 = 16.

and in [4] that all solutions of the Diophantine equation Ln + Lm = 2
a in nonnegative integers n ≥ m and a, are

2L0 = 4, 2L1 = 2, 2L3 = 8, L2 + L1 = 4, L4 + L1 = 8, and L7 + L2 = 32.

Here in this paper, we determine all the solutions of the following Diophantine equation:

Ln + Lm = 3
a (1.1)

in nonnegative integers n ≥ m and a.
We are interested in ﬁnding all powers of three which are sums of two Lucas numbers, i.e., we study the
exponential Diophantine equation Ln + Lm = 3
a in nonnegative integers n, m, and a. The proof of our main
theorem uses lower bounds for linear forms in logarithms, properties of continued fractions, and a version of the
Baker-Davenport reduction method in Diophantine approximation.
We notice that many authors have already tackled this type of problems.

2. Preliminaries

2.1. Generalities

Deﬁnition 2.1. Let k ≥ 1. The sequence {Hn}n≥0 ⊆ C is called a recurrent linear sequence of order k if the
sequence satisﬁes Hn+k = a1Hn+k−1 + a2Hn+k−2 + · · · + akHn

for all n ≥ 0 with a1, . . . , ak ∈ C, ﬁxed.

We suppose that ak ̸= 0 (otherwise, the sequence {Hn}n≥0 satisﬁes a recurrence of order less than k). If
a1, . . . , ak ∈ Z and H0, . . . , Hk−1 ∈ Z, then we can easily prove by induction on n that Hn is an integer for all
n ≥ 0. The polynomial f (X) = X k − a1X k−1 − a2X k−2 − · · · − ak ∈ C,

is called the characteristic polynomial of (Hn)n≥0. We suppose that

f (X) =
 m∏

i=1
(X − αi)
σi,

where α1, . . . , αm are distinct roots of f (X) with respectively σ1, . . . , σm their multiplicities.

Deﬁnition 2.2. We deﬁne the sequences (An)n≥0 and (Bn)n≥0 for all positive integers N by
{ An+2 = aAn+1 + An, A0 = 0, A1 = 1
Bn+2 = aBn+1 + Bn, B0 = 2, B1 = a.

For a = 1, (An)n≥0 = (Fn)n≥0 and (Bn)n≥0 = (Ln)n≥0 , which are Fibonacci and Lucas sequences
respectively, deﬁned above.
 2

On solutions of the Diophantine equation Ln + Lm = 3
a

Remark 2.3. If k = 2, the sequence (Hn)n≥0 is called a binary recurrent sequence. In this case, the
characteristic polynomial is of the form

f (X) = X 2 − a1X − a2 = (X − α1)(X − α2).

Suppose that α1 ̸= α2, then Hn = c1αn
1 + c2αn
2 for all n ≥ 0.

Deﬁnition 2.4. The binary recurrent sequence {Hn}n≥0 is said to be non degenerated if c1c2α1α2 ̸= 0 and
α1/α2 is not a root of unity.

Binet’s formula for the general term of Fibonacci and Lucas sequences is obtained using standard methods
for solving recurrent sequences, which are given by :

Fn = αn − βn

α − β and Ln = αn + βn

where (α, β) =
 ( 1 + √5
2 , 1 − √5
2
 )
 are the zeros of the characteristic polynomial X 2 − X − 1.

Deﬁnition 2.5. For all algebraic numbers γ, we deﬁne its measure by the following identity :

M(γ) = |ad|
 d∏

i=1 max{1, |γi|},

where γi are the roots of f (x) = ad
 d∏

i=1(x − γi) is the minimal polynomial of γ.

Let us deﬁne now another height, deduced from the last one, called the absolute logarithmic height. It is the
most used one.

Deﬁnition 2.6. ( Absolute logarithmic height)

For a non-zero algebraic number of degree d on Q where the minimal polynomial on Z is f (x) = ad
 d∏

i=1
(x −

γi), we denote by
 h(γ) = 1
d
 (
log |ad| +
 d∑

i=1 log max{1, |γi|}
)
 = 1
d log M(γ).

the usual logarithmic absolute height of γ.

The following properties of the logarithmic height, will also be used in the next section:

• h(γ ± η) ≤ h(γ) + h(η) + log 2.

• h(γη±1) ≤ h(γ) + h(η).

• h(γs) = |s|h(γ).

2.2. Inequalities involving the Lucas numbers

In this section, we state and prove important inequalities associated with the Lucas numbers that will be used in
solving the equation (1.1).

Proposition 2.7. For n ≥ 2, we have

0.94 αn < (1 − α−6)αn ≤ Ln ≤ (1 + α−4)αn < 1.15 αn (2.1)

Proof. This follows directly from the formula Ln = αn + (−1)nα−n. ■

3

Pagdame Tiebekabe and Isma¨ıla Diouf

2.3. Linear forms in logarithms and continued fractions

In order to prove our main result, we have to use a Baker-type lower bound several times for a non-zero linear
forms of logarithms in algebraic numbers. There are many of these methods in the literature like that of Baker
and W¨ustholz in [1]. We recall the result of Bugeaud, Mignotte, and Siksek which is a modiﬁed version of the
result of Matveev [8]. With the notation of section 2, Laurent, Mignotte, and Nesterenko [7] proved the following
theorem:

Theorem 2.8. Let γ1, γ2 be two non-zero algebraic numbers, and let log γ1 and log γ2 be any determination of
their logarithms. Put D = [Q(γ1, γ2) : Q]/[R(γ1, γ2) : R], and

Γ := b2 log γ2 − b1 log γ1,

where b1 and b2 are positive integers. Further, let A1, A2 be real numbers > 1 such that

log Ai ≥ max {h(γi), | log γi|
D , 1
D
 } , (i = 1, 2).

Then, assuming that γ1 and γ2 are mutiplicatively independent, we have

log |Γ| > −30.9 · D4 (max {log b′, 21
D , 1
2
 })2 log A1 · log A2,

where b
′ = b1
D log A2 + b2
D log A1 .

We shall also need the following theorem due to Matveev, Lemma due to Dujella and Peth˝o and Lemma due
to Legendre [6, 8].

Theorem 2.9. (Matveev [8])
Let n ≥ 1 an integer. Let L a ﬁeld of algebraic number of degree D. Let η1, . . . , ηl non-zero elements of L
and let b1, b2, . . . , bl integers, B := max{|b1|, ..., |bl|},

and
 Λ := ηb1
1 · · · ηbl
l − 1 =
 ( l∏

i=1 ηbi
i
 )
 − 1.

Let A1, . . . , Al reals numbers such that

Aj ≥ max{Dh(ηj), | log(ηj)|, 0.16}, 1 ≤ j ≤ l.

Assume that Λ ̸= 0, So we have

log |Λ| > −3 × 30l+4 × (l + 1)5.5 × d2 × A1...Al(1 + log D)(1 + log nB)

Further, if L is real, then

log |Λ| > −1.4 × 30l+3 × (l)4.5 × d
2 × A1...Al(1 + log D)(1 + log B).

During our calculations, we get upper bounds on our variables which are too large, so we have to reduce them.
To do this, we use some results from the theory of continued fractions. In particular, for a non-homogeneous linear
form with two integer variables, we use a slight variation of a result due to Dujella and Peth˝o, (1998) which is in
itself a generalization of the result of Baker and Davemport [2].
For a real number X, we write ∥X∥ := min{| X − n |: n ∈ Z} for the distance of X to the nearest integer.

4

On solutions of the Diophantine equation Ln + Lm = 3
a

Lemma 2.10. (Dujella and Peth˝o, [6])
Let M a positive integer, let p/q the convergent of the continued fraction expansion of κ such that q > 6M
and let A, B, µ real numbers such that A > 0 and B > 1. Let ε := ∥µq∥ − M ∥κq∥.
If ε > 0 then there is no solution of the inequality

0 < mκ − n + µ < AB−m

in integers m and n with log(Aq/ε)
log B ⩽ m ⩽ M.

Lemma 2.11. (Legendre)
Let τ real number such that x, y are integers such that
∣
∣
∣
∣τ − x
y
 ∣
∣
∣
∣ < 1
2y2 .

then x
y = pk
qk is the convergence of τ .

Further, ∣
∣
∣
∣τ − x
y
 ∣
∣
∣
∣ > 1
(qk+1 + 2)y2 .

3. Main Results

Our main result can be stated in the following theorem.

Theorem 3.1. The only solutions (n, m, a) of the exponential Diophantine equation
Ln + Lm = 3
a in nonnegative integers n ≥ m and a, are : (1, 0, 1) and (4, 0, 2)

i.e L1 + L0 = 3, and L4 + L0 = 9.

Proof. First, we study the case n = m, next we assume n > m and study the case n ≤ 200 with SageMath in
the range 0 ≤ m < n ≤ 200 and ﬁnally we study the case n > 200. Assume throughout that equation (1.1)
holds. First of all, observe that if n = m, then the original equation (1.1) becomes

Ln = 3a

2 .

This equation has no solution because, ∀n > 0, Ln ∈ Z. So from now, we assume n > m.
If n ≤ 200, the search with SageMath in the range 0 ≤ m < n ≤ 200 gives the solutions (n, m, a) ∈
{(1, 0, 1), (4, 0, 2)}. Now for the rest of the paper, we assume that n > 200 . Let ﬁrst get a relation between a
and n which is important for our purpose. Combining (1.1) and the right inequality of (2.1), we get:

3
a = Ln + Lm ≤ 2αn + 2αm < 2n+1 + 2m+1 = 2
n+1(1 + 2n−m) ≤ 2
n+1(1 + 1/2) < 2
n+2.

Taking log both sides, we obtain

a log 3 ≤ (n + 2) log 2 =⇒ a ≤ (n + 2)c1 where c1 = log 2
log 3 .

Rewriting equation (1.1) as:

Ln + Lm = αn + βn + Lm = 3
a =⇒ αn − 3
a = −βn − Lm.

5

Pagdame Tiebekabe and Isma¨ıla Diouf

Taking absolute value both sides, we get

|αn − 3
a| = |βn + Lm| ≤ |β|
n + Lm < 1
2 + 2αm ∵ |β|
n < 1
2 , and Lm < 2αm.

Dividing both sides by αn and considering that n > m, we get:

∣
∣1 − α−n · 3
a∣
∣ < α−n

2 + 2αm−n < 1
αn−m + 2
αn−m ∵ 1
2αn < 1
αn−m ; n > m

Hence ∣
∣1 − α−n · 3
a∣
∣ < 3
αn−m (3.1)

Let’s take γ1 := α, γ2 := 3, b1 := n, b2 := a, Γ := a log 3 − n log α

in order to apply Theorem 2.8. Therefore equation (3.1) can be rewritten as:

∣
∣1 − eΓ∣
∣ < 3
αn−m where eΓ = α−n3
a. (3.2)

Since Q(
√5) is the algebraic number ﬁeld containing γ1, γ2; so we can take D := 2. Using equation (1.1)
and Binet formula for Lucas sequence, we have :

αn = Ln − βn < Ln + 1 ≤ Ln + Lm = 3
a

which implies 1 < 3
aα−n and so Γ > 0. Combining this with (3.2), we get

0 < Γ < 3
αn−m (3.3)

where we used the fact that x ≤ ex − 1, ∀x ∈ R. Applying log on right and left hand side of (3.3), we get

log Γ < log 3 − (n − m) log α. (3.4)

Logarithm height of γ1 and γ2 are:

h(γ1) = 1
2 log α = 0.2406 · · · , h(γ2) = log 3 = 1.09862 · · · , thus we can choose

log A1 := 0.5 and log A2 := 1.1.

Finally, by recalling that a ≤ (n + 2)c1; c1 = 0.63093, we get :

b′ := b1
D log A2 + b2
D log A1 = n
2.2 + a = 0.45n + a < 0.45n + (n + 2)c1 < 2n.

It is easy to see that α and 3 are multiplicatively independent. Then by Theorem 2.8, we have

log Γ ≥ −30.9 · 24 (max {log(2n), 21
2 , 1
2
 })2 · 0.5 · 1.1

log Γ > −272 (max {log(2n), 21
2 , 1
2
 })2 . (3.5)

Combining (3.4) and (3.5), we obtain the following important result

(n − m) log α < 276 (
max {log(2n), 21
2 , 1
2
 })2 . (3.6)

6

On solutions of the Diophantine equation Ln + Lm = 3
a

Let us ﬁnd a second linear form in logarithm. For this, we rewrite (1.1) as follows:

αn(1 + αn−m) − 3
a = −βn − βm.

Taking absolute values in the above relation, we get

|αn(1 + αm−n) − 3a| < 2, β = (1 − √5)/2, |β|
n < 1 and |β|
m < 1; ∀n > 200, m ≥ 0.

Dividing both sides of the above inequality by αn(1 + αm−n), we obtain

∣
∣1 − 3
aα−n(1 + αm−n)
−1∣
∣ < 2
αn i.e |Λ| < 2
αn . (3.7)

All the conditions are now met to apply a Matveev’s theorem (Theorem 2.9).

• Data:
 t := 3; γ1 := 3; γ2 := α; γ3 := 1 + αm−n

b1 := a; b2 := −n, b3 = −1.

As before, K = Q(√5) contains γ1, γ2, γ3 and has D := [K : Q] = 2. Before continuing with the
calculations, let’s check whether Λ ̸= 0.

Λ ̸= 0 comes from the fact that if it was zero, we would have

3
a = αn + αm (3.8)

Taking the conjugate of the above relation in Q(
√5), we get :

3
a = βn + βm. (3.9)

Combining (3.8) and (3.9), we get :

αn < αn + αm = |βn + βm| ≤ |β|n + |β|
m < 2.

Recall that n > 200. This relation is impossible for n > 200. Hence Λ ̸= 0.

• Calculation of h(γ3)

Let us now estimate h(γ3) where γ3 = 1 + αm−n

γ3 = 1 + αm−n < 2 and γ−1 = 1
1 + αm−n < 1

so | log γ3| < 1. Notice that

h(γ3) ≤ |m − n| ( log α
2
 ) + log 2 = log 2 + (n − m) ( log α
2
 ) .

7

Pagdame Tiebekabe and Isma¨ıla Diouf

• The calculation of A1 and A2 gives :
 A1 := 2.2

and
 A2 := 0.5

and we can take
 A3 := 2 + (n − m) log α since h(γ3) := log 2 + (n − m) ( log α
2
 )

• Calculation of B

Since a < (n + 2)c1, it follows that, B = max{1, n, a}. Thus we can take B = n + 1.

The Matveev’s theorem gives the lower bound on the left hand side of (3.7) by replacing the data. We get :

exp (−C(1 + log(n + 1)) · 2.2 · 0.5 · (2 + (n − m) log α))

where
 C := 1.4 · 30
6 · 3
4.5 · 2
2(1 + log 2) < 9.7 × 1011.

Replacing in equation (3.7), we get:

exp (−C(1 + log(n + 1)) · 2.2 · 0.5 · (2 + (n − m) log α)) < |Λ| < 2
αn

which leads to

n log α − log 2 < C((1 + log(n + 1)) · 1.1 · (2 + (n − m) log α) < 2C log n · 1.1 · (2 + (n − m) log α)

then
 n log α − log 2 < 1.26 × 1012 log n · (2 + (n − m) log α) (3.10)

where we used inequality 1 + log(n + 1) < 2 log n, which holds for n > 200.
Now, using (3.6) in the right term of the above inequality (3.10) and doing the related calculations, we get

n < 7.3 × 10
14 log n (max {log(2n), 21
2
 })2 . (3.11)

If max{log(2n), 21/2} = 21/2, it follows from (3.11) that n < 8.04825 · 1016 log n =⇒ n < 3.5 · 1018. On
the other hand, if max{log(2n), 21/2} = log(2n), then from (3.11), we get n < 7.3 · 1014 log n log2(2n) and so
n < 7.2 · 10
19. We can easily see that for the two possible values of max{log(2n), 21/2}, n < 7.2 · 1019.
All the calculations done so far can be summarized in the following lemma.

Lemma 3.2. If (n, m, a) is a solution in positive integers of (1.1) with conditions n > m and n > 200, then
inequalities
 a ≤ n + 2 < 1.2 × 1020 hold.

8

On solutions of the Diophantine equation Ln + Lm = 3
a

4. Reducing of the bound on n

Dividing across inequality (3.3) : 0 < a log 3 − n log α < 3
αn−m by log α, we get

0 < aγ − n < 7
αn−m ; where γ := log 3
log α . (4.1)

The continued fraction of the irrational number γ is :

[a0, a1, a2, ......] = [1, 2, 3, 1, 1, 2, 3, 2, 4, 2, 1, 11, 2, 1, 11, ......]

and let denote pk/qk its convergent. An inspection using SageMath gives the following inequality

4977896525362041575 = q41 < 1.2 × 1020 < q42 = 805929983250536127817.

Furthermore, aM := max {ai|i = 0, 1, ..., 42} = 161 Now applying Lemma 2.11 and properties of continued
fractions, we obtain
 |aγ − n| > 1
(aM + 2)a . (4.2)

Combining equation (4.1) and (4.2), we get

1
(aM + 2)a < |aγ − n| < 7
αn−m =⇒ 1
(aM + 2)a < 7
αn−m =⇒ αn−m < 7 · (161 + 2)a < 1.3692 · 10
23.

Applying log above and divide by log α, we get :

(n − m) ≤ log (7 · 163 · a)
log α < 111.

To improve the upper bound on n, let consider

z := a log 3 − n log α − log ρ(u) where ρ = 1 + α−u. (4.3)

From (3.7), we have
 |1 − ez| < 2
αn . (4.4)

Since Λ ̸= 0, then z ̸= 0. Two cases arise : z < 0 and z > 0. For each case, we will apply Lemma 2.10.

• Case 1 : z > 0

From (4.4), we obtain 0 < z ≤ ez − 1 < 2
αn . Replacing (4.3) in the above inequality, we get:

0 < a log 3 − n log α − log ρ(n − m) ≤ 3
aα−nρ(n − m)
−1 − 1 < 2α−n

hence 0 < a log 3 − n log α − log ρ(n − m) < 2α−n

and by diving above inequality by log α

0 < a ( log 3
log α
 ) − n − log ρ(n − m)
log α < 5 · α−n. (4.5)

Taking, γ := log 3
log α , µ := − log ρ(n − m)
log α , A := 5, B := α, inequality (4.5) becomes

0 < aγ − n + µ < AB−n.

9

Pagdame Tiebekabe and Isma¨ıla Diouf

Since γ is irrational, we are now ready to apply lemma 2.10 of Dujella and Peth¨o on (4.5) for n − m ∈
{1, ..., 111}.

Since a ≤ 1.2 × 1020 from lemma 3.2, we can take M = 1.2 × 10
20, and we get

n < log(Aq/ε)
log B where q > 6M

and q is the denominator of the convergent of the irrational number γ such that ε := ||µq|| − M ||γq|| > 0.
With the help of SageMath, with conditions z > 0, and (n, m, a) a possible zero of (1.1), we get
n < 112 which contradicts our assumption n > 200. Then it is false.

• Case 2 : z < 0

Since n > 200, then 2
αn < 1
2 . Hence (4.4) implies that |1 − e|z|| < 2. Also, since z < 0, we have

0 < |z| ≤ e|z| − 1 = e|z||e|z| − 1| < 4
αn .

Replacing (4.3) in the above inequality and dividing by log 3, we get:

0 < n ( log α
log 3
 ) − a + ρ(n − m)
log 3 < 4
log 3 · α−n < 4 · α−n (4.6)

In order to apply lemma 3.2 on (4.6) for n − m ∈ {1, 2, ..., 111}, let’s take again M = 1.2 × 10
20. With the
help of SageMath, with conditions z < 0, and (n, m, a) a possible zero of (1.1), we get n < 111 which
contradicts our assumption n > 200. Then it is false.
This completes the proof of our main result (Theorem 3.1). ■

5. Acknowledgement

The author is thankful to the referee for his valuable suggestions which improved the presentation of the paper.
The authors also thank the professor Maurice Mignotte for his remarks and diponibility.

References

[1] A. Baker and G. W¨ustholz, Logarithmic and Diophantine Geometry, Vol 9 New Mathematical Monographs
(Cambridge University Press), 2007.

[2] A. Baker and H. Davenport, The equations 3x2 − 2 = y2 and 8x2 − 7 = z2, Quart. J. Math. Oxford Ser. 20
(1969), 129-137.

[3] J. J. Bravo and F. Lucas, Powers of Two as Sums of Two Lucas Numbers, Journal of Integers sequences,
Vol.17(2014) Article 14.8.3

[4] Bravo, J. J. and Luca, F. On the Diophantine Equation Fn + Fm = 2
a, Quaestiones Mathematicae, (2016)
39 (3), 391–400.

[5] Y. Bugeaud, M. Mignotte, and S. Siksek, Classical and modular approaches to exponential Diophantine
equations. I. Fibonacci and Lucas perfect powers, Ann. of Math. 163 (2006), 969-1018.

[6] A. Dujella and A. Peth¨o, A generalization of a theorem of Baker and Davenport, Quart. J. Math. Oxford
Ser. 49 (1998), no. 195, 291-306.
 10

On solutions of the Diophantine equation Ln + Lm = 3
a

[7] M. Laurent, M. Mignotte, and Y. Nesterenko, Formes lin´eaires en deux logarithmes et d´eterminants
d’interpolation, (French) (Linear forms in two logarithms and interpolation determinants), J. Number Theory
55 (1995), 285-321.

[8] E. M. Matveev, An explicit lower bound for a homogeneous rational linear form in the logarithms of
algebraic numbers, II, Izv. Ross. Akad. Nauk Ser. Mat. 64 (2000), 125-180. Translation in Izv. Math. 64
(2000), 1217-1269.
 This is an open access article distributed under the Creative Commons Attribution
License, which permits unrestricted use, distribution, and reproduction in any medium,
provided the original work is properly cited.

11
