<!-- source: https://publish.uwo.ca/~pyu/pub/preprints/YH_JAAC2011a.pdf | converted from PDF -->

Journal of Applied Analysis and Computation Website:http://jaac-online.com/
Volume 1, Number 1, February 2011 pp. 143–153

A STUDY ON ZOLADEK’S EXAMPLE
∗

Pei Yua,† and Maoan Han
b

Abstract In this paper, we consider an example of third-order polynomial
planar system, proposed by Zoladek who claimed that this example had eleven
small-amplitude limit cycles around a center. We use focus value computation
to show that for this example there may exist maximal nine small-amplitude
limit cycles around the center due to Hopf bifurcation.

Keywords Hilbert’s 16th problem, integrable system, limit cycle, focus value,
Hopf bifurcation.

MSC(2000) 34C07, 34C23.

1. Introduction

The second part of the well-known Hilbert’s 16th problem [1] is to consider the
existence of limit cycles in planar polynomial vector ﬁelds. This is a very diﬃcult
problem, not completely solved even for quadratic systems after more than 100 years
since Hilbert proposed the problem. If the problem is restricted to the vicinity of
isolated singular points, it becomes a particular version to estimate the number of
small-amplitude limit cycles (or small limit cycles) bifurcating from an elementary
center or an elementary focus. This is equivalent to studying degenerate Hopf
bifurcations, and the main task becomes computing the so-called focus values of the
point and determining center conditions. In the past six decades, many researchers
have considered the local problem and obtained many results. Bautin [2] ﬁrst proved
that quadratic systems can have maximal three small limit cycles around a center or
a focus point. For cubic systems, many investigations have shown that in the vicinity
of a singular point the number of small-amplitude limit cycles can be ﬁve [4], six [5],
seven [3, 5, 6], eight [7, 8], and nine [8]. On the other hand, the number of limit
cycles existed in multiple singular points for cubic planar polynomial systems can be
ten [9], eleven [10, 11], twelve [12, 13, 14], and thirteen [15, 16, 17]. More information
about the Hilbert’s 16th problem may be found in the survey article [10]. It should
be pointed out that the nine small-amplitude limit cycles given in [8] are obtained by
perturbing an elementary center (linear center) of general cubic systems, while the
nine small-amplitude limit cycles obtained in this paper are obtained by perturbing
a center of an integrable system with cubic polynomials.

†Corresponding author. Fax: (519) 661-3523.
Email addresses: pyu@uwo.ca; mahan@shnu.edu.cn
aDepartment of Applied Mathematics, The University of Western Ontario
London, Ontario, Canada N6A 5B7
bDepartment of Mathematics, Shanghai Normal University, Shanghai, 200234
China
∗This work was supported by the Natural Sciences and Engineering Research
Council of Canada (NSERC) and the National Natural Science Foundation
of China (NNSFC).

144 P. Yu, M. Han

In this paper, we will pay particular attention to the example of third-order
planar integral system, proposed by Zoladek [18] who claimed that this system
could have eleven small-amplitude limit cycles around a center. The example is
related to the following equations:

˙x = x
3 + x y + 5
2 x + a,

˙y = − a x
3 + 6 x
2 y − 3 x
2 + 4 y2 + 2 y − 2 a x, (1.1)

where a is a parameter. System (1.1) has a rational Darboux integral:

H = f 5
1
f 4
2 = (x
4 + 4 x
2 + 4 y)
5

(x5 + 5 x3 + 5 x y + 5
2 x + a)4 , (1.2)

and the integrating factor of system (1.1) is M = 20 f 4
1 f −5
2 . For a < − 2
5/4, system
(1.1) has a center at
 C0 = ( − a
2 , − a
2 + 2
4
 ), (1.3)

and ﬁve (real or complex) ﬁxed points at (x, y) = (r, − 2 r3+5 r+2 a
2 r ), where r is
the root of polynomial equation: r5 − 10 r − 4 a = 0. In addition, system (1.1) has
a saddle point and a non-elementary point at inﬁnity. One example of the phase
portrait of system (1.1) for a = − 4 is shown in Figure 1.
-14

-12

-10

-8

-6

-4

-2

 0

 2

 4

 6

-3 -2 -1  0  1  2  3

y
 x

Figure 1. A phase portrait of system (1.1) when a = − 4.

In [18], the author used second-order Poincar´e-Pontriagin integral (or Abelian
integral) to show that there exist eleven small-amplitude limit cycles around the
center C0. In this paper, we shall use focus value computation to show by per-
turbing system (1.1) with cubic polynomials that there may exist maximal nine
small-amplitude limit cycles around C0 due to Hopf bifurcation.

A STUDY ON ZOLADEK’S EXAMPLE 145

To consider perturbing system (1.1), we add cubic polynomial perturbations to
system (1.1) up to ε2, as follows:

˙x = x
3 + x y + 5
2 x + a + ε p(ε, x, y),

˙y = − a x
3 + 6 x
2 y − 3 x
2 + 4 y2 + 2 y − 2 a x + ε q(ε, x, y), (1.4)

where p(ε, x, y) and q(ε, x, y) are given by

p(ε, x, y) = a001 + a101 x + a011 y + a201 x
2 + a111 x y + a021 y2

+ a301 x
3 + a211 x
2 y + a121 x y2 + a031 y3

+ ε [a002 + a102 x + a012 y + a202 x
2 + a112 x y + a022 y2

+ a302 x
3 + a212 x
2 y + a122 x y2 + a032 y3],

q(ε, x, y) = b001 + b101 x + b011 y + b201 x
2 + b111 x y + b021 y2

+ b301 x
3 + b211 x
2 y + b121 x y2 + b031 y3

+ ε [b002 + b102 x + b012 y + b202 x
2 + b112 x y + b022 y2

+ b302 x
3 + b212 x
2 y + b122 x y2 + b032 y3].
 (1.5)

It is easy to show that under the following conditions:

a00k = 1
64 [32 a a10k + 16(a
2 + 2) a01k − 16a
2 a20k − 8a(a
2 + 2) a11k
−4(a
2 + 2)
2a02k + 8a
3 a30k + 4a
2(a
2 + 2) a21k

+2a(a
2 + 2)
2a12k + (a
2 + 2)
3a03k],

b00k = 1
64 [32 a b10k + 16(a
2 + 2) b01k − 16a
2 b20k − 8a(a
2 + 2) b11k
−4(a
2 + 2)
2b02k + 8a
3 b30k + 4a
2(a
2 + 2) b21k

+2a(a
2 + 2)
2b12k + (a
2 + 2)
3b03k],

b01k = − a10k + 1
16 [16a a20k +4(a
2 +2)a11k −12a
2a30k −4(a
2 +2)a21k
−(a
2 +2)2a12k + 8a b11k +8(a
2 +2)b02k −4a
2b21k

−4a(a
2 +2)b12k −3(a
2 +2)2b03k]

≡ a
∗
01k,
 (1.6)

where k = 1, 2, then the perturbed system (1.4) still has the same center C0. Now,
applying a translation x = − a
2 + ¯x, y = − a
2+2
4 + ¯y, and a linear transformation to
system (1.4), we obtain the following new system:

˙¯x = ωc ¯y + a
2−8√2a4−64 ¯x
2 + ¯x ¯y + a
2
√2a4−64 ¯x
3 + ε ¯p(ε, ¯x, ¯y),

˙¯y = − ωc ¯x − 3 ¯x
2 − 2(a
2+28)
√2a4−64 ¯x ¯y + 4 ¯y2 − 4a
2(a
2+5)
a4−32 ¯x
3 + 6 a
2
√2a4−64 ¯x
2 ¯y + ε ¯q(ε, ¯x, ¯y),
(1.7)
in which
 ωc = 1

2
√
2(a2 + 2)
 [(a
4 − 32) + ω1 ε + ω2 ε2 + ω3 ε3 + · · · ]1/2

146 P. Yu, M. Han

and
 ¯p(ε, ¯x, ¯y) = ¯a101 ¯x + ¯a011 ¯y + ¯a201 ¯x
2 + ¯a111 ¯x ¯y + ¯a021 ¯y2

+ ¯a301 ¯x
3 + ¯a211 ¯x
2 ¯y + ¯a121 ¯x ¯y2 + ¯a031 ¯y3

+ ε [¯a102 ¯x + ¯a012 ¯y + ¯a202 ¯x
2 + ¯a112 ¯x ¯y + ¯a022 ¯y2

+ ¯a302 ¯x
3 + ¯a212 ¯x
2 ¯y + ¯a122 ¯x ¯y2 + ¯a032 ¯y3]

+ ε2[ · · · ] + ε3[ · · · ] + · · ·

¯q(ε, ¯x, ¯y) = ¯b101 ¯x + ¯b011 ¯y + ¯b201 ¯x
2 + ¯b111 ¯x ¯y + ¯b021 ¯y2

+ ¯b301 ¯x
3 + ¯b211 ¯x
2 ¯y + ¯b121 ¯x ¯y2 + ¯b031 ¯y3

+ ε [
¯b102 ¯x + ¯b012 ¯y + ¯b202 ¯x
2 + ¯b112 ¯x ¯y + ¯b022 ¯y2

+ ¯b302 ¯x
3 + ¯b212 ¯x
2 ¯y + ¯b122 ¯x ¯y2 + ¯b032 ¯y3]

+ ε2[ · · · ] + ε3[ · · · ] + · · ·
 (1.8)

Here, ωj, ¯aijk and ¯bijk are explicitly expressed in terms of the original coeﬃcients
aijk, bijk and a.

Next, employing a method (e.g. the perturbation method given in [19]) to
compute the focus value of system (1.7), we obtain the following focus values:

v0 = v00 + v01 ε + v02 ε2 + · · · ≡ v00 + 1
2 (b011 − b∗
011) ε + 1
2 (b012 − b∗
012) ε2 + · · ·

vk = v0k + vk1 ε + vk2 ε2 + · · · , k = 1, 2, · · · (1.9)
where v0k = 0, k = 1, 2, · · · , since C0 is a center. Thus, when b011 = b∗
011, v01 = 0,
and b012 = b∗
012 yields v02 = 0. For convenience, in the following, we call vk1 as
ε-order focus values, and vk2 as ε2-order focus values.

Remark 1. An alternative procedure to analyze system (1.1) is ﬁrst to apply a
translation and a linear transformation to system (1.1) and then add perturbations
p(ε, x, y) and q(ε, x, y) to the transformed system. This procedure will generate
the same result as that given by analyzing system (1.4).

In the next two sections, we shall consider the existence of small-amplitude limit
cycles, based on the ε-order and ε2-order focus values, respectively.

2. The number of limit cycles based on ε-order fo-
cus values

We ﬁrst consider the ε-order focus values. Denote ˜H(3) for the maximal number
of small-amplitude limit cycles bifurcating from the center C0. Then, for this case,
we have the following theorem.

Theorem 1. With the ε-order focus values, ˜H(3) = 9.

Proof. Based on the obtained ε-order focus values, we solve the ﬁrst eight equa-
tions: vk1, k = 1, 2, · · · , 8 for b101, b201 b111, b021, b301, b211, b121 and b031 to

A STUDY ON ZOLADEK’S EXAMPLE 147

obtain

b101 = b∗
101 = − a a101 − a
2 a011 + 1
2 (a
2−) a201 + a
4 (a
2 +10) a111
+ 1
24 (3a
4 −4a
2 +17) a021 − a
4 (a
2 + 8) a301 + 1
8 (a
4 + 2a
2 + 5) a211
− a
48 (3a
4 + 12a
2 + 116) a121 + 1
21994930176000 (46747280800000a
8

−687341568000a
6 − 4370117689344000 − 15886629487529168a
4

+34371511716608475a
2 − 4370117689344000) a031,
b201 = b∗
201 = − 3 a101 − 15 a
2 a011 + 9 a
2 a201 + 3
4 (3a
2 +10) a111 + a
8 (9a
2 −10) a021
− 3
4 (3a
2 +4) a301 − 3 a
8 (3a
2 − 8) a211 − 1
16 (9a
4 − 20a
2 + 172) a121
+ a
128303759360000 (2590088655000000a
6 + 83421692820598608a
4

− 631135948827669425a
2 + 373978546560195000) a031,
b111 = b∗
111 = − 9 a011 + 7 a201 + 3 a021 + 9
2 a211 + 9 a a121
+ 3
32075939840000 (19146020265571122a
4 − 81345441450987275a
2

+ 23437660127232000) a031,
b021 = b∗
021 = +4 a111 − 6 a121 − 9 a
10485760000 (51418022656a
4 − 311155569125) a031,
b301 = b∗
301 = − 13 a011 + 5 a201 + a a111 − 1
24 (3a
2 + 164) a021 − 2 a a301
− 1
8 (3a
2 − 80) a211 − a
12 (a
2 − 120) a121
+ 1
769822556160000 (42335402600908032a
6 + 1032569283113924199a
4

−6419549479578590300a
2 + 2146353266294784000) a031,
b211 = b∗
211 = 3 a a021 + 6 a301 − 3 a
32075939840000 (943726387828224a
4

− 10706188880760835a
2 + 11678964377872500) a031,
b121 = b∗
121 = − 15
2 a021 + 7
2 a211 − 3
2566075187200 (187685481266381a
2

−97602502656000) a031,
b031 = b∗
031 = 8
3 a121 + 1240857537 a
41943040 a031.

Deﬁning the critical point

B∗
1 = (b∗
101, b∗
201, b∗
111, b∗
021, b∗
301, b∗
211, b∗
121, b∗
031), (2.1)

then at this critical point, vk1 = 0, k = 1, 2, · · · , 8, and

v91 = − 258237837 a031
32 a9(a4 − 32) ,

v101 = 23476167 a031 (57697a4 − 35728a2 − 88704)
64 a11(a4 − 32)2 ,

v111 = − 23476167 a031 (2304313595a8 −1702233920a6 −11829269248a4

1024 a13(a4 − 32)3

−
39211065344a2 +8642101248)
1024 a13(a4 − 32)3 .
 (2.2)

This clearly shows that when a031 ̸= 0, we have v91 ̸= 0 for a < − 2
5/4. Setting
a031 = 0 results in v91 = v101 = v111 = · · · 0. Hence, at most we can have nine
small-amplitude limit cycles bifurcating from the center C0, based on the analysis
of ε-order focus values.
Further, evaluating the determinant of the following Jacobian at the critical

148 P. Yu, M. Han

point B∗
1 ,

JB∗
1 =
 














 ∂v11
∂b101 ∂v11
∂b201 ∂v11
∂b111 ∂v11
∂b021 ∂v11
∂b301 ∂v11
∂b211 ∂v11
∂b121 ∂v11
∂b031
∂v21
∂b101 ∂v21
∂b201 ∂v21
∂b111 ∂v21
∂b021 ∂v21
∂b301 ∂v21
∂b211 ∂v21
∂b121 ∂v21
∂b031
∂v31
∂b101 ∂v31
∂b201 ∂v31
∂b111 ∂v31
∂b021 ∂v31
∂b301 ∂v31
∂b211 ∂v31
∂b121 ∂v31
∂b031
∂v41
∂b101 ∂v41
∂b201 ∂v41
∂b111 ∂v41
∂b021 ∂v41
∂b301 ∂v41
∂b211 ∂v41
∂b121 ∂v41
∂b031
∂v51
∂b101 ∂v51
∂b201 ∂v51
∂b111 ∂v51
∂b021 ∂v51
∂b301 ∂v51
∂b211 ∂v51
∂b121 ∂v51
∂b031
∂v61
∂b101 ∂v61
∂b201 ∂v61
∂b111 ∂v61
∂b021 ∂v61
∂b301 ∂v61
∂b211 ∂v61
∂b121 ∂v61
∂b031
∂v71
∂b101 ∂v71
∂b201 ∂v71
∂b111 ∂v71
∂b021 ∂v71
∂b301 ∂v71
∂b211 ∂v71
∂b121 ∂v71
∂b031
∂v81
∂b101 ∂v81
∂b201 ∂v81
∂b111 ∂v81
∂b021 ∂v81
∂b301 ∂v81
∂b211 ∂v81
∂b121 ∂v81
∂b031
 















B∗
1
 ,

yields

det(JB∗
1 ) = − 373423834799904305184768
5 a36(a4 − 32)8 ̸= 0, for a < − 2
5/4. (2.3)

Thus, by proper perturbations, one can obtain nine small-amplitude limit cycles
around the center C0. The proof is complete.

Remark 2. It is seen from the above proof that when the nine bij1 coeﬃcients are
used for solving the ε-order focus values, only a031 is needed to obtain nine limit
cycles, and all other aij1 coeﬃcients can be set zero for ε-order analysis.

Moreover, it is noted that in addition to the critical condition B∗
1 , setting a031 =
0 results in all the ε-order focus values to be zero. Thus, we have the following
result.

Theorem 2. All the ε-order focus values become zero under the following condi-
tions:

a031 = 0,

b101 = − a a101 − a
2 a011 + 1
2 (a
2−) a201 + a
4 (a
2 +10) a111 + 1
24 (3a
4 −4a
2 +17) a021
− a
4 (a
2 + 8) a301 + 1
8 (a
4 + 2a
2 + 5) a211 − a
48 (3a
4 + 12a
2 + 116) a121,

b201 = − 3 a101 − 15 a
2 a011 + 9 a
2 a201 + 3
4 (3a
2 +10) a111 + a
8 (9a
2 −10) a021
− 3
4 (3a
2 +4) a301 − 3 a
8 (3a
2 − 8) a211 − 1
16 (9a
4 − 20a
2 + 172) a121,

b111 = − 9 a011 + 7 a201 + 3 a021 + 9
2 a211 + 9 a a121,

b021 = 4 a111 − 6 a121,

b301 = − 13 a011 + 5 a201 + a a111 − 1
24 (3a
2 + 164) a021 − 2 a a301 − 1
8 (3a
2 − 80) a211
− a
12 (a
2 − 120) a121,

b211 = 3 a a021 + 6 a301,

b121 = − 15
2 a021 + 7
2 a211,

b031 = 8
3 a121. (2.4)

A STUDY ON ZOLADEK’S EXAMPLE 149

3. The number of limit cycles based on ε2-order fo-
cus values

Now, we turn to consider the ε2-order focus values under the conditions given in
(2.4) such that all the ε-order focus values are zero. Note that except the coeﬃcient
a031, we leave other unused aij1 coeﬃcients in the expressions of bij1 and hope
they might be used in the ε2-order analysis. From the ε2-order analysis, we have
the following result.
Theorem 3. With the ε2-order focus values, ˜H(3) = 9.
Proof. Based on the calculated ε2-order focus values, we solve the ﬁrst eight
equations: vk2 = 0, k = 1, 2, · · · , 8 for b102, b202 b112, b022, b302, b212, b122 and
b032 to obtain

b102 = b∗
102 = − a a102 − a
2 a012 + 1
2 (a
2−) a202 + a
4 (a
2 +10) a112
+ 1
24 (3a
4 −4a
2 +17) a022 − a
4 (a
2 + 8) a302 + 1
8 (a
4 + 2a
2 + 5) a212
− a
48 (3a
4 + 12a
2 + 116) a122 + 1
21994930176000 (46747280800000a
8

−687341568000a
6 − 4370117689344000 − 15886629487529168a
4

+34371511716608475a
2 − 4370117689344000) a032 + ˜b102,
b202 = b∗
202 = − 3 a102 − 15 a
2 a012 + 9 a
2 a202 + 3
4 (3a
2 +10) a112 + a
8 (9a
2 −10) a022
− 3
4 (3a
2 +4) a302 − 3 a
8 (3a
2 − 8) a212 − 1
16 (9a
4 − 20a
2 + 172) a122
+ a
128303759360000 (2590088655000000a
6 + 83421692820598608a
4

− 631135948827669425a
2 + 373978546560195000) a032 + ˜b202,
b112 = b∗
112 = − 9 a012 + 7 a202 + 3 a022 + 9
2 a212 + 9 a a122
+ 3
32075939840000 (19146020265571122a
4 − 81345441450987275a
2

+ 23437660127232000) a032 + ˜b112,
b022 = b∗
022 = +4 a112 − 6 a122 − 9 a
10485760000 (51418022656a
4 − 311155569125) a032

+˜b022,
b302 = b∗
302 = − 13 a012 + 5 a202 + a a112 − 1
24 (3a
2 + 164) a022 − 2 a a302
− 1
8 (3a
2 − 80) a212 − a
12 (a
2 − 120) a122 + 1
769822556160000
(42335402600908032a
6 + 1032569283113924199a
4

−6419549479578590300a
2 + 2146353266294784000) a032 + ˜b302,
b212 = b∗
212 = 3 a a022 + 6 a302 − 3 a
32075939840000 (943726387828224a
4

− 10706188880760835a
2 + 11678964377872500) a032 + ˜b212,
b122 = b∗
122 = − 15
2 a022 + 7
2 a212 − 3
2566075187200 (187685481266381a
2

−97602502656000) a032 + ˜b122,
b032 = b∗
032 = 8
3 a122 + 1240857537 a
41943040 a032 + ˜b032,

where the coeﬃcients ˜bij2 are explicitly expressed in terms of a201, a111, a021,
a301, a211, a121, and are given in Appendix.
Similarly, deﬁning the critical point,

B∗
2 = (b∗
102, b∗
202, b∗
112, b∗
022, b∗
302, b∗
212, b∗
122, b∗
032), (3.1)

150 P. Yu, M. Han

then at this critical point, vk2 = 0, k = 1, 2, · · · , 8, and

v92 = − 28693093 (9a032 − 5a021 a121)
32 a9(a4 − 32) ,

v102 = 2608463 (9a032 − 5a021 a121)
64 a11(a4 − 32)2 (57697a4 − 35728a2 − 88704),

v112 = − 2608463 (9a032 − 5a021a121)
1024 a13(a4 − 32)3

×(2304313595a8 −1702233920a6 −11829269248a4 −39211065344a2 +8642101248).
(3.2)

This implies that when 9 a032 − 5 a021 a121 ̸= 0, we have v92 ̸= 0 for a < − 2
5/4.
Setting a032 = 5
9 a021 a121 yields v92 = v102 = v112 = · · · 0. Therefore, at most we
can have nine small-amplitude limit cycles bifurcating from the center C0, based on
the analysis of ε-order focus values.
Further, evaluating the determinant of the following Jacobian at the critical
point B∗
2 ,

JB∗
2 =
 














 ∂v12
∂b102 ∂v12
∂b202 ∂v12
∂b112 ∂v12
∂b022 ∂v12
∂b302 ∂v12
∂b212 ∂v12
∂b122 ∂v12
∂b032
∂v22
∂b102 ∂v22
∂b202 ∂v22
∂b112 ∂v22
∂b022 ∂v22
∂b302 ∂v22
∂b212 ∂v22
∂b122 ∂v22
∂b032
∂v32
∂b102 ∂v32
∂b202 ∂v32
∂b112 ∂v32
∂b022 ∂v32
∂b302 ∂v32
∂b212 ∂v32
∂b122 ∂v32
∂b032
∂v42
∂b102 ∂v42
∂b202 ∂v42
∂b112 ∂v42
∂b022 ∂v42
∂b302 ∂v42
∂b212 ∂v42
∂b122 ∂v42
∂b032
∂v52
∂b102 ∂v52
∂b202 ∂v52
∂b112 ∂v52
∂b022 ∂v52
∂b302 ∂v52
∂b212 ∂v52
∂b122 ∂v52
∂b032
∂v62
∂b102 ∂v62
∂b202 ∂v62
∂b112 ∂v62
∂b022 ∂v62
∂b302 ∂v62
∂b212 ∂v62
∂b122 ∂v62
∂b032
∂v72
∂b102 ∂v72
∂b202 ∂v72
∂b112 ∂v72
∂b022 ∂v72
∂b302 ∂v72
∂b212 ∂v72
∂b122 ∂v72
∂b032
∂v82
∂b102 ∂v82
∂b202 ∂v82
∂b112 ∂v82
∂b022 ∂v82
∂b302 ∂v82
∂b212 ∂v82
∂b122 ∂v82
∂b032
 















B∗
2
 ,

yields
 det(JB∗
2 ) = − 373423834799904305184768
5 a36(a4 − 32)8 ̸= 0, for a < − 2
5/4.

Hence, by proper perturbations, one can obtain nine small-amplitude limit cycles
around the center C0. The proof is ﬁnished.
Remark 3. The unused aij1 coeﬃcients remained in the system does not help to
get more limit cycles. It is not surprising to see that det(JB∗
2 ) = det(JB∗
1 ), and
the formulas for the focus values: v92, v102, v112, are exactly the same as that for
v91, v101, v111 if a021 = 0 or a121 = 0.
Remark 4. Again it is seen from the above proof that when the nine bij2 coeﬃcients
are used for solving the ε2-order focus values, only a032 (if setting a021 = 0 or
a121 = 0) is needed to obtain nine limit cycles, and all other aij2 coeﬃcients can
be set zero for ε2-order analysis.
It is also noted that in addition to the critical condition B∗
2 , setting a032 =
5
9 a021 a121 leads to all the ε2-order focus values being zero. Thus, we have the
following result.
Theorem 4. All the ε2-order focus values become zero under the critical condition
B∗
2 with a032 = 5
9 a021 a121.
Remark 5. From the proofs of Theorems 1 and 3, it is easy to see that even with
higher εn-order focus values, it is not possible to obtain more than nine small-
amplitude limit cycles bifurcating from the center.

A STUDY ON ZOLADEK’S EXAMPLE 151

4. Conclusion

In this paper, based on ε-order and ε2-order focus values, we have shown that
the example given by Zoladek [18] can exhibit maximal nine small-amplitude limit
cycles around the center. It is unlikely to have more small-amplitude limit cycles
even using higher εn-order focus values.

Appendix

In this appendix, the coeﬃcients ˜bij2 given in Section 3 are listed below, where
˜bij2 is denoted by bbij2.

bb102:=-119/16*a211*a1*a011-133/48*a121^2*a1^3+10247/96*a121*a021+994561814791373/2474429644800
*a021*a1^4*a121+23/96*a021*a1^3*a211-253/18*a121^2*a1-355/96*a121*a211-7*a121*a201-45/32
*a021*a1^2*a301+29/8*a121*a011+1/48*a111*a021+75/16*a111*a211+5*a111*a201+87/16*a211*a1
*a201+115/48*a021*a1*a201-63/32*a211*a1^2*a301-569/384*a211*a1^4*a121-9/2*a111*a011-227/48
*a021*a1*a011+9/2*a1*a201^2+3/2*a1*a011^2-55/64*a1^3*a211^2-1/2*a011*a301-9/16*a1^4*a121
*a201-7/24*a021*a101-15/8*a211*a101+71/192*a1^3*a021^2+9/16*a1^4*a121*a011+4*a1*a211^2
-2*a101*a201+2*a101*a011-9/8*a1^3*a211*a201+5/2*a111*a301*a1-9*a1*a201*a011-1/4*a111^2
*a1^3-384434875/325582848*a121*a1^8*a021+9/8*a1^3*a211*a011+1/8*a111*a211*a1^4+a111*a101
*a1+1/24*a021^2*a1^5-153348194797115/175959441408*a121*a021*a1^2+415/96*a121*a211*a1^2
+63/32*a111*a211*a1^2+17/24*a301*a021-29/12*a121*a301*a1+65/96*a1*a021*a211+215/96*a111
*a021*a1^2+113/48*a111*a121*a1^3+83/24*a121*a201*a1^2-1/4*a301^2*a1^3-41/12*a121*a101*a1
+7/4*a011*a1^2*a301-113/48*a121*a301*a1^3-a101*a1*a301-5/2*a111^2*a1-101/192*a121^2*a1^5
+29/24*a121*a011*a1^2+31/24*a201*a1^3*a021-31/24*a011*a1^3*a021+1/16*a111*a121*a1^5
-1/24*a111*a021*a1^4-1/48*a121*a1^6*a021-1/24*a211*a1^5*a021-1/16*a121*a1^5*a301
+1/24*a021*a1^4*a301+1/2*a111*a301*a1^3-7/4*a111*a011*a1^2-1/3*a101*a1^2*a021
-7/4*a201*a1^2*a301+263/24*a111*a121*a1-1/8*a211*a1^4*a301-469/96*a1*a021^2
+7/4*a1^2*a111*a201:
bb202:=-289987194845/176160768*a121*a1*a021-7/8*a201*a1^3*a121-43/4*a301*a121+15/2*a301*a111
+21/8*a1*a211*a101-5/2*a1*a021*a301+85/4*a121*a1*a011+113/4*a111*a121-565/12*a121^2
+227/32*a1^2*a021^2-749/48*a121^2*a1^2+156662310309817/57378078720*a121*a1^3*a021
+15/32*a1^3*a211*a111+113/16*a1^2*a021*a201+7/64*a121^2*a1^6
-83047798165451/229113856000*a121*a1^5*a021+3*a201^2-15/2*a111^2+15/2*a211^2+18*a021*a011
-251/12*a021^2-15417194375/1374683136*a121*a1^7*a021+21/64*a1^4*a211^2-9/4*a1^2*a111^2
+3*a111*a101+113/64*a1^4*a021^2-1/2*a121*a1^3*a011+15*a111*a1*a011+3/8*a1^2*a211^2
-3*a301*a101-71/8*a111*a121*a1^2+245/16*a1*a021*a111-59/32*a1^2*a021*a211
-67/32*a1^4*a021*a211+77/32*a1^3*a021*a111+7/4*a101*a121*a1^2-77/32*a1^3*a021*a301
-83/16*a1^2*a021*a011+49/128*a121*a1^5*a211+5/12*a121^2*a1^4-6*a201*a011-41/8*a1*a021*a101
-12*a021*a201-33/16*a211*a1^2*a011+55/32*a121*a211*a1^3-21/16*a211*a1^2*a201
-15/32*a211*a1^3*a301-1/8*a301*a1^4*a121-153/16*a1*a211*a111+15/2*a201*a211-27/2*a211*a011
+1/8*a111*a121*a1^4-95/32*a121*a211*a1-29/4*a021*a211+9/2*a301*a1^2*a121-15*a301*a1*a011
-9/2*a111*a1*a201+9/2*a111*a1^2*a301+3*a1*a301*a211+9/2*a1*a301*a201
-9/4*a1^2*a301^2-3*a011^2-7*a101*a121-a201*a1*a121:
bb112:=9/8*a211*a1*a011-456179816730741/458227712000*a021*a1^4*a121-131979/112*a121*a021
+45/64*a211*a1^4*a121+3249631747890371/769822556160*a121*a021*a1^2-9/16*a021*a1^3*a211
-9/16*a021*a1^2*a301+39/8*a021*a1*a011+21/16*a121*a211*a1^2+9/4*a211*a101+9/16*a211
*a1^2*a301-9/8*a111*a121*a1^3+9/8*a021*a1*a201-9*a011*a301+9/16*a111*a021*a1^2
-39/8*a111*a021+9*a121*a301*a1-9/16*a111*a211*a1^2-213/16*a1*a021*a211-21*a121*a201
-9/4*a121*a201*a1^2+9/8*a121*a301*a1^3+9/2*a121*a101*a1+9*a111*a011+9/4*a121*a011*a1^2
+437/16*a1*a021^2+9/8*a121^2*a1^3+42*a121*a011-45/8*a111*a211+3/4*a021*a101+3*a301*a021
-9/8*a211*a1*a201-43/8*a121^2*a1-687/16*a121*a211+9/32*a1^3*a021^2+9/32*a1^3*a211^2
+9/32*a121^2*a1^5-81/4*a111*a121*a1:
NB022:=-2845760393/16777216*a121*a1*a021+3/8*a121*a1^3*a021+3/4*a111*a121*a1^2+3/2*a201*a1*a121
+15/2*a111*a121+200851651/8192000*a121*a1^5*a021-3/4*a301*a1^2*a121-3/16*a121^2*a1^4
-3/8*a121*a211*a1^3+39/2*a021*a011+6*a121*a211*a1-1/4*a121^2*a1^2-3/2*a121*a1*a011

152 P. Yu, M. Han

-41/4*a021^2-9*a021*a201-21/4*a021*a211-9/2*a211*a011 -85/4*a121^2-3*a101*a121:
bb302:=-16459830161293273/21994930176000*a021*a1^4*a121-1589743/1008*a121*a021+133/48*a121^2
*a1^3-20*a121*a201+64111487909344943/13856806010880*a121*a021*a1^2-283/48*a021*a1^3*a211
-29/8*a211*a1*a201+25/4*a211*a101-7874888876657/257753088000*a121*a1^6*a021-33/16*a111
*a211*a1^2+41/32*a1^3*a211^2+101/64*a211*a1^4*a121+449/48*a111*a021*a1^2+455/24*a021
*a1*a201-347/48*a1*a021*a211-13/8*a111*a121*a1^3+33/16*a211*a1^2*a301-491/24*a021*a1*a011
-449/48*a021*a1^2*a301-a111^2*a1+281/6*a121*a011+13/8*a121*a301*a1^3+2*a111*a301*a1
+15/32*a121^2*a1^5+5*a301*a201+427/96*a1^3*a021^2-3*a121*a201*a1^2-135/4*a111*a121*a1
+1247/48*a1*a021^2-7/8*a211*a1*a011+11/2*a121*a101*a1+9*a121*a211*a1^2-161/24*a121^2*a1
+923/24*a111*a021-119/12*a021*a101-905/48*a121*a211-a1*a301^2+17/8*a121*a011*a1^2
+9/4*a1*a211^2-26*a011*a301+26*a111*a011-205/8*a111*a211+20*a121*a301*a1
-41/3*a301*a021-5*a111*a201+10*a301*a211:
bb212:=-305753642565281/549873254400*a121*a1^3*a021-6*a1*a021*a111+5/2*a121^2*a1^2-3*a121*a1*a011
-30*a021*a211+200851651/4096000*a121*a1^5*a021+6*a1*a021*a301-15*a021*a201+41/2*a021^2
-9/2*a121*a211*a1+39*a021*a011+17229676735/29360128*a121*a1*a021
+9/8*a1^2*a021*a211+3/8*a1^2*a021^2:
bb122:=26812211609483/219949301760*a121*a021*a1^2-4*a1*a021^2-31/4*a121^2*a1-2475/28*a121*a021
+45/4*a121*a211+15/2*a111*a021-15/2*a301*a021+15/2*a121*a011:
bb032 :=
35/6*a021^2-5/2*a021*a211+5*a121^2-413619179/25165824*a121*a1*a021:

References

[1] D. Hilbert, Mathematical problems(M. Newton, Transl.), Bull. Amer. Math.,
8(1902), 437-479 .

[2] N. N. Bautin, On the number of limit cycles which appear with the variation of
coeﬃcients from an equilibrium position of focus or center type, Mat. Sbornik
(N.S.), 30(1952), 181-196.

[3] J. Li and J. Bai, The cyclicity of multiple Hopf bifurcation in planar diﬀerential
cubic systems: M (3) ≥ 7, Preprint, Hunming Institute Technology, 1989.

[4] C. J. Christopher and N. G. Lloyd, On the paper of Jin and Wang concerning
the conditions for a centre in certain cubic systems, Bull. London Math. Soc.,
22(1990), 5-12.

[5] N. G. Lloyd, T. R. Blows, M. C. Kalenge, Some cubic systems with several
limit cycles, Nonlinearity, 1(1988), 653-669.

[6] A. P. Sadovskii, Cubic systems of nonlinear oscillations with seven limit cycles,
Diﬀerential Equations, 39(2003), 505-516. (Translated from Diﬀerentsial’nye
Uravneniy, 39(4)(2003),472-481.

[7] E. M. James, N. G. Lloyd, A cubic system with eight small-amplitude limit
cycles, IMA J. Appl. Math., 47(1991), 163-171.

[8] P. Yu and R. Corless, Symbolic computation of limit cycles associated with
Hilbert’s 16th problem, Communications in Nonlinear Science and Numerical
Simulation, 14(2009), 4041-4056.

[9] M. Han, Y. Lin and P. Yu, A study on the existence of limit cycles of a planar
system with 3rd-degree polynomials, Int. J. Bifurcation and Chaos, 14(2004),
41-60.

[10] J. Li, Hilbert’s 16th problem and bifurcations of planar polynomial vector ﬁelds,
Int. J. Bifurcations and Chaos, 13(2003), 47-106.

A STUDY ON ZOLADEK’S EXAMPLE 153

[11] T. Zhang, H. Zang and M. Han, Bifurcation of limit cycles in a cubic system,
Chaos, Solitons and Fractals, 20(2004), 629-638.

[12] P. Yu and M. Han, Twelve limit cycles in a 3rd-order planar system with Z2
symmetry, Communication on Pure and Applied Analysis, 3(2004), 515-526.

[13] P. Yu and M. Han, Twelve limit cycles in a cubic case of the 16th Hilbert
problem, Int. J. Bifurcation and Chaos, 15(2005), 2191-2205.

[14] P. Yu and M. Han, Small limit cycles bifurcating from ﬁne focus points in cubic
order Z2-equivariant vector ﬁelds, Chaos, Solitons and Fractals, 24(2005), 329-
348.

[15] C. Li, L. Liu and J. Yang, A cubic system with thirteen limit cycles, J. Diﬀ.
Eqns 246(2009), 3609-3619.

[16] Y. Liu and J. Li, New results on the study of Zq-equivariant planar polynomial
vector ﬁelds, Qual. Theory Dyn. Syst., 9(2010), 167-219.

[17] J. Yang, M. Han, J. Li and P. Yu, Existence conditions of thirteen limit cycles
in a cubic system, Int. J. Bifurcation and Chaos, 20(2010), 2569-2577.

[18] H. ˙Zol¸adek, Quadratic systems with center and their perturbations, J. Diﬀ.
Eqns., 109(1994), 223-273 .

[19] P. Yu, Computation of normal forms via a perturbation technique, J. Sound
and Vib., 211(1998), 19-38.
