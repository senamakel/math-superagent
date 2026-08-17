<!-- source: https://arxiv.org/pdf/2411.09594 | converted from PDF -->

arXiv:2411.09594v1  [math.DS]  14 Nov 2024
A NOTE ON A RECENT ATTEMPT TO SOLVE
THE SECOND PART OF HILBERT’S 16TH PROBLEM

CLAUDIO A. BUZZI
1 AND DOUGLAS D. NOVAES2

ABSTRACT. For a given natural number n, the second part of Hilbert’s 16th Problem asks whether there exists
a ﬁnite upper bound for the maximum number of limit cycles that planar polynomial vector ﬁelds of degree n
can have. This maximum number of limit cycle, denoted by H(n), is called the nth Hilbert number. It is well-
established that H(n) grows asymptotically as fast as n2 log n. A direct consequence of this growth estimation is
that H(n) cannot be bounded from above by any quadratic polynomial function of n. Recently, the authors of
the paper [Exploring limit cycles of differential equations through information geometry unveils the solution to
Hilbert’s 16th problem. Entropy, 26(9), 2024] afﬁrmed to have solved the second part of Hilbert’s 16th Problem by
claiming that H(n) = 2(n − 1)(4(n − 1) − 2). Since this expression is quadratic in n, it contradicts the established
asymptotic behavior and, therefore, cannot hold. In this note, we further explore this issue by discussing some
counterexamples.
 1. INTRODUCTION

For a given natural number n, the second part of Hilbert’s 16th Problem asks whether there is a ﬁnite
upper bound for the number of limit cycles that planar polynomial vector ﬁelds of degree n can possess.
More precisely, let
 H(n) := sup{π(P, Q) : deg(P), deg(Q) ≤ n},

where π(P, Q) denotes the number of limit cycles of the polynomial differential system

(1)
 { ˙x = P(x, y),
˙y = Q(x, y).

Recall that a limit cycle of (1) is a (non-stationary) periodic orbit that is isolated from other periodic orbits
(see [8, Deﬁnition 9]). Thus, the second part of Hilbert’s 16th Problem consists of proving that H(n) < ∞
for all n ∈ N (see [8, Chapter 2]). The value H(n) is called the nth Hilbert number.
The most signiﬁcant advancement in understanding the asymptotic behavior of the function H(n) was
made by Christopher and Lloyd in [2], who introduced a method showing that H(n) grows as fast as
n2 log n. This classical result has been revisited and improved by several works, including [1, 4, 5]. In
particular, Han and Li in [4] reﬁned Christopher and Lloyd’s result, demonstrating that H(n) grows at least
as fast as (n + 2)2 log(n + 2)/(2 log 2) by establishing that

lim
n→∞ inf H(n)
(n + 2)2 log(n + 2) ≥ 1
2 log 2 .

This remains the best-known lower estimation for the asymptotic growth of H(n).
A direct conclusion from this asymptotic growth estimation is that H(n) cannot be bounded from above
by any quadratic polynomial function in n, as the expression (n + 2)2 log(n + 2)/(2 log 2) surpasses any
degree two polynomial in n for sufﬁciently large values of n.
Recently, the authors of the paper [3] afﬁrmed to have solved the second part of Hilbert’s 16th Problem
by claiming that

(2) H(n) = 2(n − 1)(4(n − 1) − 2),

2010 Mathematics Subject Classiﬁcation. 34C07, 34C23, 37G15.
Key words and phrases. limit cycles, Hilbert’s 16th Problem, Hilbert number, asymptotic growth estimation.

1

2 C.A. BUZZI AND D.D. NOVAES

for n ≥ 2 (see [3, Theorem 4]). They make use of the following scalar curvature associated to a Fisher
information metric:

(3) R = 1
√G
 [ ∂
∂x
 ( 1
√G
 ∂G22
∂x
 ) + ∂
∂y
 ( 1
√G
 ∂G11
∂y
 )] ,

where
 G11 = 2
 [( ∂P
∂x
 )2 + ( ∂Q
∂x
 )2]
 , G22 = 2
 [( ∂P
∂y
 )2 + ( ∂Q
∂y
 )2]
 , and G = G11G22.

Their approach relies on [3, Deﬁnition 1], which aims to provide an alternative deﬁnition for limit cycles,
referred to as being “in the framework of GBT”. It begins by establishing that
(A) a limit cycle is the periodic state of (1) in which R is positive in the neighborhood of the equilibrium points of
(1) and |R| is singular.

By |R| singular, they mean the existence of zeros of the denominator of |R| that makes |R| to diverge to
inﬁnity. Thus, it is also asserted that
(B) if R is positive in the neighborhood of the equilibrium points of (1) and the magnitude of R diverges to inﬁnity
at symmetrical singularities with respect to the origin, then (1) possesses only one limit cycle. Nonetheless, if
R is positive in the neighborhood of the equilibrium points of (1) and the magnitude of R diverges to inﬁnity
at different singularities, then (1) has more than one limit cycle such that the total number of distinctive
divergences of |R| to inﬁnity provides the maximum number of limit cycles of (1).

Subsequent to Deﬁnition 1, it is stated that such a deﬁnition “agrees with the deﬁnition of limit cycles in
the framework of classical bifurcation theory”, that is (non-stationary) periodic orbits isolated from other
periodic orbits. In this way, the approach employed in [3] to obtain (2) consisted in counting the number of
divergences of |R| to inﬁnity, as highlighted in the proof of [3, Theorem 4].
As previously mentioned, the function H(n) cannot be bounded from above by any quadratic polynomial
in n. Therefore, the relationship (2), which is quadratic in n, cannot hold. To explore this issue further,
we present counterexamples in the following sections. Section 2 discusses a well-known example from the
literature that contradicts (2), along with references to other known examples that serves as counterexamples
to (2). In Section 3, we provide examples of polynomial systems that exhibit limit cycles but do not satisfy
(A), and vice versa. This demonstrates that (A) is neither necessary nor sufﬁcient for the existence of limit
cycles of (1) and, therefore, is not equivalent to the standard deﬁnition of limit cycles. As a result, the
deﬁnition of limit cycles proposed in [3] is not applicable to the study of the second part of Hilbert’s 16th
problem, meaning that the number of singularities of |R| does not determine the maximum number of limit
cycles in (1), as suggested by assertion (B).

2. KNOWN COUNTEREXAMPLES IN THE LITERATURE

The objective of this section is not to construct new counterexamples to the main conclusion (2) of [3], but
rather to highlight known examples from the literature that serve as counterexamples for it.
In [5, Section 3], Li et al. revisited the class of polynomial differential systems originally studied by
Christopher and Lloyd [2], addressing a minor issue in the original analysis. This correction did not affect
the leading term n2 log n of the lower estimation for the asymptotic growth of H(n). Their approach, as well
as Christopher and Lloyd’s approach, consists of constructing a sequence of recursively deﬁned polynomial
differential systems (PHk) of degree 2k − 1, each possessing at least Sk limit cycles, where

Sk = 4k−1 (k − 13
6
 ) + 2k − 1
3 .

This sequence implies that

(4) H(2k − 1) ≥ Sk = 4k−1 (k − 13
6
 ) + 2k − 1
3 .

However, the conclusion (2) from [3] provides that

H(2k − 1) = 4(2k − 2)(2k+1 − 5),

A NOTE ON A RECENT ATTEMPT TO SOLVE THE SECOND PART OF HILBERT’S 16TH PROBLEM 3

which contradicts (4) for k ≥ 35. This means that system PHk, for k ≥ 35, has more limit cycles than
predicted by the main result of [3]. The other sequences of polynomial systems discussed in [5, Sections 4
and 5] also provide counterexamples to (2).
The works [4] and, more recently, [1] also provide similar lower estimations for the asymptotic growth of
H(n). Both works present sequences of polynomial differential systems with speciﬁed degrees and numbers
of limit cycles, differing in the mechanisms used to generate these limit cycles. Counterexamples to (2) can
be derived from these sequences in a way analogous to the approach outlined above.

3. POSSIBLE ISSUE FOR THE PROPOSED METHOD

We begin by presenting three examples of polynomial differential systems where the existence of limit
cycles is guaranteed, but assertion (A) does not hold. Speciﬁcally, in these examples, either R is negative in a
neighborhood of the unique equilibrium point, or R is positive in a neighborhood of the unique equilibrium
point, but |R| is not singular. These examples demonstrate that limit cycles satisfying (A) do not encompass
all possible limit cycles in polynomial systems. As a result, the maximum number of limit cycles satisfying
(A) for a polynomial system of degree n does not provide an upper bound for H(n). This likely explains
why the main result (2) of [3] does not agree with the established lower estimations for the asymptotic
growth of H(n), as discussed in the previous section.

Example 1. We start by considering the following cubic vector ﬁeld

(5)
 { ˙x = −y + x(x2 + y2 − 1),
˙y = x + y(x2 + y2 − 1),

which has a single equilibrium point, located at the origin (0, 0). This vector ﬁeld also has a unique limit cycle
surrounding the origin. To see that, it is enough to write system (5) in polar coordinates (x, y) = (r cos(θ), r sin(θ))
as follows: { ˙r = r(r2 − 1),
˙θ = 1.

This implies that system (5) has a unique limit cycle which is unstable and whose orbit corresponds to the unit circle
with center at the origin. Now, computing the function R we get

R(x, y) = R1(x, y)
R2(x, y) ,

where

R1(x, y) =72x10 − 216x8y2 − 204x8 − 320x7y − 3056x6y4 + 464x6y2 + 368x6 + 192x5y3 + 192x5y

− 3056x4y6 + 2360x4y4 − 304x4y2 − 240x4 − 192x3y5 − 216x2y8 + 464x2y6 − 304x2y4 − 96x2y2

+ 96x2 + 320xy7 − 192xy5 + 72y10 − 204y8 + 368y6 − 240y4 + 96y2 − 16 and

R2(x, y) =((3x2 + y2 − 1)2 + (2xy + 1)2)2((x2 + 3y2 − 1)2 + (2xy − 1)2)2.

Observe that R2 does not vanish at the origin, implying that R is continuous in its neighborhood. Additionally,
since R(0, 0) = −1 < 0, continuity ensures that R(x, y) remains negative in a neighborhood of the origin, which
corresponds to the unique equilibrium point of (5). Therefore, system (5) provides an example of a limit cycle that does
not satisfy assertion (A).

Example 2. Using the approach from Example 1, we can easily construct polynomial systems with any number of
limit cycles and a unique equilibrium point, where R is negative in its neighborhood. For instance, the following
polynomial system has a single equilibrium point at the origin and two nested limit cycles surrounding it:

(6)
 { ˙x = −y + x(x2 + y2 − 1)(x2 + y2 − 4),
˙y = x + y(x2 + y2 − 1)(x2 + y2 − 4).

Indeed, by applying a polar change of variables, one can deduce that (6) has exactly two limit cycles: an asymptotically
stable one, whose orbit corresponds to the unit circle centered at the origin; and an unstable one whose orbit corresponds
to a circle of radius two, also centered at the origin. The expression for R is cumbersome and thus omitted here, but

4 C.A. BUZZI AND D.D. NOVAES

following the same reasoning of Example 1, we conclude that R is continuous in a neighborhood of the origin, with
R(0, 0) = −80/289 < 0, implying that R remains negative near the origin. Therefore, system (6) provides examples
of limit cycles that do not satisfy assertion (A).

Example 3. Now, consider the system (5) under the following linear change of variables: (x, y) = (u, u + v/2). This
yields the transformed system:

(7)
 



 ˙u = −2u − v
2 + 2u3 + u2v + uv2

4 ,

˙v = 4u + 2u2v + uv2 + v3

4 .

Of course, system (7) has a unique equilibrium point at the origin (0, 0) and a unique limit cycle surrounding it.
Computing the function R for system (7), we obtain

R(u, v) = R1(u, v)
R2(u, v) ,

where

R1(u, v) =32( − 663552u10 − 8638464u9v − 25353216u8v2 − 7421952u8 − 37943808u7v3 − 18733056u7v

− 36060032u6v4 − 22151168u6v2 + 5670912u6 − 23658048u5v5 − 18140416u5v3 + 10874880u5v

− 10971920u4v6 − 11152128u4v4 + 7196416u4v2 − 2199552u4 − 3555048u3v7 − 4852576u3v5

+ 2186496u3v3 − 4174848u3v − 772632u2v8 − 1359232u2v6 + 296160u2v4 − 2595840u2v2

+ 219136u2 − 103056uv9 − 222052uv7 + 49248uv5 − 828032uv3 + 472064uv − 6399v10 − 18528v8

+ 18596v6 − 126272v4 + 134912v2 + 61440) and

R2(u, v) =((24u2 + 8uv + v2 − 8)2 + 16(4uv + v2 + 4)2)2((8u2 + 8uv + 3v2)2 + 4(2u2 + uv − 1)2)2.

Again, R2 does not vanish at the origin, so R is continuous in its neighborhood. Moreover, since R(0, 0) = 6/5 > 0,
continuity ensures that R(u, v) is positive in a neighborhood of the origin, corresponding to the unique equilibrium
point of (7). Additionally, since R2 is a product of sums of squares, it follows that R2(u, v) = 0 if and only if (u, v)
satisﬁes one of the following systems of algebraic equations:

S1 :
 {24u2 + 8uv + v2 − 8 = 0
4uv + v2 + 4 = 0 or S2 :
 {8u2 + 8uv + 3v2 = 0
2u2 + uv − 1 = 0.

We begin by analyzing S1. First, note that if (u, v) is a solution of S1, then v ̸= 0. Solving the second equation of
S1 for u and substituting into the ﬁrst equation yields the algebraic equation 17v4 + 152v2 + 384 = 0, which has no
real solutions. Next, for system S2, if (u, v) is a solution, then u ̸= 0. Solving the second equation of S2 for v and
substituting into the ﬁrst equation leads to the algebraic equation 3 − 4u2 + 4u4 = 0, which also has no real solutions.
This shows that the denominator R2 of R does not vanish, and hence |R| has no singularities. Therefore, system (7)
provides another example of a limit cycle that does not satisfy assertion (A).

From the above examples, we observed that assertion (A) is not necessary for the existence of limit cycles,
as there are polynomial systems with limit cycles where (A) does not hold. Nevertheless, we can still ask
whether (A) is a sufﬁcient condition for the existence of limit cycles. The following example provides a
negative answer to this question.

Example 4. Consider the following quadratic polynomial system:

(8)
 { ˙x = −y + x2,
˙y = x + xy.

This system and its properties have been extensively studied in the literature, as it appears as a normal form for a
class of isochronous quadratic systems, commonly referred to as S2 (see [6, 7]). This system has a unique equilibrium
point at the origin, which is a center, meaning that there exists a neighborhood U around the origin where all orbits in

A NOTE ON A RECENT ATTEMPT TO SOLVE THE SECOND PART OF HILBERT’S 16TH PROBLEM 5

U \ {(0, 0)} are periodic. Clearly, no periodic orbit in U is a limit cycle, as none are isolated from other periodic orbits.
In fact, this system does not have any limit cycles. By computing the function R for system (8), we obtain

R(x, y) = 1

(x2 + 1)2 (4x2 + (y + 1)2) .

Observe that R is continuous in a neighborhood of the origin, as its denominator does not vanish at (0, 0). Since
R(0, 0) = 1, continuity ensures that R remains positive in a neighborhood around the origin, which is the unique
equilibrium point of (8). Furthermore, |R| is singular at (x, y) = (0, −1). Thus, system (8) provides an example
where assertion (A) holds for every periodic orbit within U, despite the absence of limit cycles.

4. CONCLUSION

In this note, we have demonstrated that the recent attempt to solve the second part of Hilbert’s 16th
problem, as presented in [3], contains signiﬁcant issues. We began by exploring counterexamples which
demonstrate that the quadratic expression proposed for H(n) contradicts the well-established asymptotic
behavior of this function, which states that H(n) grows as fast as (n + 2)2 log(n + 2)/(2 log 2). Moreover,
we discussed how the alternative deﬁnition of limit cycles (A), used in [3], is not applicable to the study of
the second part of Hilbert’s 16th problem, as it is neither necessary nor sufﬁcient for the existence of limit
cycles in (1), according to the standard deﬁnition, which refers to (non-stationary) periodic orbits isolated
from other periodic orbits.
 REFERENCES

[1] M. ´Alvarez, B. Coll, P. D. Maesschalck, and R. Prohens. Asymptotic lower bounds on Hilbert numbers using canard cycles. Journal
of Differential Equations, 268(7):3370–3391, Mar. 2020.
[2] C. J. Christopher and N. G. Lloyd. Polynomial systems: a lower bound for the Hilbert numbers. Proc. Roy. Soc. London Ser. A,
450(1938):219–224, 1995.
[3] V. B. da Silva, J. P. Vieira, and E. D. Leonel. Exploring limit cycles of differential equations through information geometry unveils
the solution to Hilbert’s 16th problem. Entropy, 26(9), 2024.
[4] M. Han and J. Li. Lower bounds for the Hilbert number of polynomial systems. J. Differential Equations, 252(4):3278–3304, 2012.
[5] J. Li, H. S. Y. Chan, and K. W. Chung. Some lower bounds for H(n) in Hilbert’s 16th problem. Qual. Theory Dyn. Syst., 3(2):345–360,
2002.
[6] W. S. Loud. Behavior of the period of solutions of certain plane autonomous systems near centers. Contributions to Differential
Equations, 3:21–36, 1964.
[7] P. Mardeˇsi´c, C. Rousseau, and B. Toni. Linearization of isochronous centers. J. Differential Equations, 121(1):67–108, 1995.
[8] R. Roussarie. Bifurcation of planar vector ﬁelds and Hilbert’s sixteenth problem, volume 164 of Progress in Mathematics. Birkh¨auser Verlag,
Basel, 1998.

1UNIVERSIDADE ESTADUAL PAULISTA, IBILCE-UNESP - AV. CRISTOV ˜AO COLOMBO, 2265, 15.054-000, S. J. RIO PRETO, SP,
BRASIL
Email address: claudio.buzzi@unesp.br

2UNIVERSIDADE ESTADUAL DE CAMPINAS (UNICAMP), DEPARTAMENTO DE MATEM ´ATICA, INSTITUTO DE MATEM ´ATICA, ES-

TAT´ISTICA E COMPUTAC¸ ˜AO CIENT´IFICA (IMECC) - RUA S ´ERGIO BUARQUE DE HOLANDA, 651, CIDADE UNIVERSIT ´ARIA ZEFERINO
VAZ, 13083–859, CAMPINAS, SP, BRASIL
Email address: ddnovaes@unicamp.br
