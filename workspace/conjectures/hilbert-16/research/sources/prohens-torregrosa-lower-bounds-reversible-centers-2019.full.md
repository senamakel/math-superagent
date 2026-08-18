<!-- source: https://ddd.uab.cat/pub/artpub/2019/204392/newlowbou_a2019v32n1p331.pdf | converted from PDF -->

NEW LOWER BOUNDS FOR THE HILBERT NUMBERS
USING REVERSIBLE CENTERS

R. PROHENS AND J. TORREGROSA

Abstract. In this paper we provide the best lower bounds, that are known up
to now, for the Hilbert numbers of polynomial vector ﬁelds of degree N , H(N ),
for small values of N . These limit cycles appear bifurcating from new symmetric
Darboux reversible centers with very high simultaneous cyclicity. The considered
systems have, at least, three centers, one on the reversibility straight line and
two symmetric about it. More concretely, the limit cycles are in a three nests
conﬁguration and the total number of limit cycles is at least 2n+m, for some values
of n and m. The new lower bounds are obtained using simultaneous degenerate
Hopf bifurcations. In particular, H(4) ≥ 28, H(5) ≥ 37, H(6) ≥ 53, H(7) ≥ 74,
H(8) ≥ 96, H(9) ≥ 120, and H(10) ≥ 142.

1. Introduction

We consider two-dimensional diﬀerential systems

˙x = P (x, y), ˙y = Q(x, y), (1)

in which P and Q are polynomials of degree N . The maximum possible number,
H(N ), of limit cycles of system (1) is known as the Hilbert number. As usual we
deﬁne limit cycle as every isolated periodic solution.
As it follows from former deﬁnition, the Hilbert number refers to the total amount
of limit cycles that system (1) exhibits and, in this sense, it is a global concept. For
instance, Shi (see [24]) and Chen and Wang (see [5]) proved that H(2) ≥ 4. For
cubics, Li, Liu, and Yang (see [18]) and Li and Liu (see [19]) proved that H(3) ≥ 13.
In our work we prove, among other new best lower bounds for the Hilbert numbers,
that H(4) ≥ 28.
The aim of this work is to obtain new lower bounds values for H(N ). This
goal is attained by simultaneously perturbing some reversible centers. We proceed
studying simultaneous degenerate Hopf bifurcations of reversible centers and, to
overcome heavy computations, we use an eﬃcient way (parallelization method) for
the Lyapunov quantities calculation.
This work strongly relies on the results of Christopher, [7], and Han, [12] and [13].
The idea is to estimate the generic cyclicity of a family of simultaneous centers from
the series expansion of the Lyapunov quantities at a point on the center variety. In
particular, if the ﬁrst r linear terms of the Lyapunov quantities are independent,
then the cyclicity is bigger or equal than r, if we consider also the trace as another
independent parameter. The germ of this linearization idea can be glimpsed at the
work of Chicone and Jacobs, see [6], where, for higher order limit cycles bifurcations,

Date: January 10, 2018.
2010 Mathematics Subject Classiﬁcation. Primary 34C07, Secondary: 37G15, 34C23, 34C25.
Key words and phrases. Polynomial diﬀerential equation; Limit cycles; Bifurcation and number
of periodic orbits; 16th Hilbert number. 1

This is a preprint of: “New lower bounds for the Hilbert numbers using reversible centers”, Rafel
Prohens, Joan Torregrosa, Nonlinearity , vol. 32, 331–355, 2019.

2 R. PROHENS AND J. TORREGROSA

the Lyapunov quantities are obtained from the Taylor series expansion of the per-
turbation parameters. We want to remark that, in the paper [7], Christopher studies
this symmetric simultaneous bifurcation, only up to ﬁrst order perturbation, of a
quartic system obtaining 22 limit cycles in two symmetric nests of 6 cycles and one
nest of 10. For short, we say that these limit cycles are in conﬁguration ⟨6, 10, 6⟩. In
Section 3 we give the precise deﬁnition of the conﬁguration concept and we describe
de complete bifurcation mechanism.
The present work can be considered as a continuation of the Christopher’s one
since, to obtain limit cycles, we use the same mechanism to study symmetric simul-
taneous bifurcation of limit cycles but using higher order perturbation for the same
center of degree 4 and linear order for a new Darboux centers of bigger degrees. Our
main results are the following.

Theorem 1. H(4) ≥ 28, H(5) ≥ 37, H(6) ≥ 53, H(7) ≥ 74, H(8) ≥ 96,
H(9) ≥ 120, and H(10) ≥ 142. Moreover, the conﬁgurations of limit cycles for N =
4, . . . , 10, are ⟨8, 12, 8⟩, ⟨11, 15, 11⟩, ⟨16, 21, 16⟩, ⟨23, 28, 23⟩, ⟨30, 36, 30⟩, ⟨38, 44, 38⟩,
and ⟨45, 52, 45⟩, respectively.

Corollary 2. (a) H(13) ≥ 212, H(17) ≥ 384, H(21) ≥ 568, H(31) ≥ 1184,
H(35) ≥ 1536, H(39) ≥ 1920, and H(43) ≥ 2272.
(b) For each pair (N0, K0) ∈ {(4, 28), (5, 37), (6, 53), (7, 74), (8, 96), (9, 120), (10, 142)},
we have that H(N ) ≥ K0
(N0 + 1)2 N 2

when N = 2
k(N0 + 1) − 1, for k ∈ N.

The linear computational approach to estimate lower bounds for the cyclicity of
centers has, at least, two advantages. The ﬁrst one is computational, and it is based
on the fact that, by shortening the length of the expressions to be manipulated, more
fast computations can be performed. The second one has to do with the functional
independence argument of the Lyapunov quantities, since this argumentation is
replaced by an study, in most of the cases, on the independence of their linear parts.
Nevertheless, sometimes, linear terms of the Lyapunov quantities are not inde-
pendent and, for studying the simultaneous bifurcation, we must take into account
higher order terms. This disadvantage was considered by Christopher and, to over-
come the setback that the computations are no longer linear and become unman-
ageable, under some generic assumptions, something speciﬁc can be proved, see [7,
Th.3.1].
The improvement for N = 4, with respect to Christopher’s work, is that we
obtain 28 limit cycles in two nests of 8 cycles and one nest of 12, i.e. in a ⟨8, 12, 8⟩
conﬁguration. The key point in obtaining this new best estimation of H(4) is the
use of ﬁfth order, instead of linear order, approximation of the Lyapunov quantities.
It is also worth mentioning that, despite having tried to use this technique in the
cubic case, we have not been able to improve the current lower bound of H(3). See,
respectively, Sections 5 and 4.
Concerning the parallelization method, roughly speaking, it is as follows. We,
one-by-one, compute the linear part of a ﬁxed number of Lyapunov quantities of
simpler diﬀerential equations having only one perturbation monomial. Then, by
taking the summation of all the results, we obtain the corresponding linear part of
the Lyapunov quantity of the complete diﬀerential equation. If we proceed in this

HILBERT NUMBERS USING REVERSIBLE CENTERS 3

way it can be checked that the computations in each simpler equation are shorter
in size and time. See [20] for more details.
In our paper, we follow former approach and latter technique applied to families of
polynomial reversible symmetric diﬀerential systems (1) having two centers outside
the symmetry line, which will be the x-axis, plus one more extra center at the origin.
See Figure 1. Then, we force the existence of two symmetric weak foci of order n

Figure 1. Schematic phase portrait of the polynomial reversible
symmetric diﬀerential systems (1) having one center at the origin plus
two more symmetric centers.

where the symmetric centers were located, out oﬀ the x-axis. We aim to create n
limit cycles, by using only reversible perturbations, around each one of them; in this
way, 2n simultaneous limit cycles will be achieved. After that, by perturbing again
the system, but without the reversibility property, we can generate m more limit
cycles surrounding a weak focus of order m at the origin. Summing up, the total
number of limit cycles we have generated is 2n + m, in conﬁguration ⟨n, m, n⟩.
The proof of Theorem 1 is done in Sections 5,6 and 7, while Corollary 2 is proved
in Section 8. We note that the supplied lower bounds for the Hilbert numbers,
H(N ), for N = 4, . . . , 10, in Theorem 1 signiﬁcantly improve the previous best
known Hilbert numbers. See for instance [14, 15, 20]. We also give a a new general
lower bound for the Hilbert numbers, H(N ). See Corollary 2.
Even taking into account that the parallelization method has more facilities than
using other ways to proceed in ﬁnding new better lower bounds of H(N ), some
obstacles are found in to go ahead for values of N higher than those considered. Next,
we comment some of them. The ﬁrst obstruction concerns the computer memory. In
spite oﬀ the usage of linear approximations, the computations of Lyapunov quantities
for higher values of N requires, increasing N , more and more memory. Another
arising problem is the necessity to get reversible diﬀerential systems providing good
seeds for bifurcating the required number of limit cycles. Finally, another problem,
for our computational approach, is how to obtain good ﬁrst integrals in such a way
that, when moving to complex variables, the coeﬃcients in the diﬀerential equations
are all rational numbers.
This paper is structured as follows. In Section 2 we recall, not only some of the
known best estimates of lower bounds for the Hilbert numbers, but also the corre-
sponding known best estimations of lower bounds for the cyclicity of non degenerated
monodromic equilibrium points. In Section 3 we describe the methodology used to
get the main results. In Section 4 we provide a detailed description of the method
applied to a cubic vector ﬁeld, getting a characterization of all cubic systems having
a reversible center with two extra symmetric centers out of the symmetry axis. In
Section 5, we study some reversible quartic systems and, by considering ﬁfth order

4 R. PROHENS AND J. TORREGROSA

terms in the Lyapunov quantities Taylor series, and we get the new best lower bound
H(4) ≥ 28. Section 6 is devoted to get some families of reversible polynomial vector
ﬁelds of degrees 5, . . . , 9 with a rational ﬁrst integral having simultaneous bifurcation
of limit cycles. In this section we present, among other lower bounds for the Hilbert
numbers, the new best lower bounds H(5) ≥ 37 and H(6) ≥ 53. In Section 7 we
study some Darboux reversible centers having a curve of equilibria. In this section
we obtain the new best lower bounds H(7) ≥ 74, H(8) ≥ 96, H(9) ≥ 120 and
H(10) ≥ 142. Finally, in Section 8 we prove Corollary 2.

2. Previous estimations for M (N ) and H(N )

Before to start with the global concept of the Hilbert number, H(N ), a local
concept concerning the bifurcation of small limit cycles around a speciﬁc equilibrium
point is also considered. This is the case for the cyclicity of an equilibrium point.
Roughly speaking, a monodromic equilibrium point for a family of vectors ﬁelds
in (1) has ﬁnite cyclicity M (N ) if, in Hausdorﬀ distance, the maximum number of
limit cycles is M (N ), and they appear in a close neighbourhood of the equilibrium
point, when the perturbation tends to zero whereas the neighbourhood shrinks to
the equilibrium point. From previous deﬁnitions it is easy to conclude that M (N ) ≤
H(N ), for all N .
In this section we present the known best estimations, up to now, of M (N ) and
H(N ). As we prove in this work, some of them will be improved from our results.
A classical bifurcation mechanism to study the existence of periodic orbits around
an equilibrium point of monodromic type is the non-degenerate Hopf bifurcation
method. This mechanism studies the limit cycles that emerge from an equilibrium
point of center-focus type when, by changing the sign of the trace in a suitable way,
its stability changes from stable to unstable or vice-versa. The non-degenerate Hopf
bifurcation method can be generalized, by computing the Lyapunov quantities, to
more degenerate critical points. This generalization is known as the degenerated
Hopf bifurcation method and it is used to give estimations of M (N ), see [1], for
instance. Besides former reference, see also [13, 30] for more results on bifurcation
theory of limit cycles. Among these specialized references, a general approach to
qualitative theory of diﬀerential equation can be found in [9].

In the last decades some improvements of the lower bounds of H(N ) have been
achieved by using better estimates of M (N ). In fact, this is the case for some special
small values of N . At this point it is worth to mention that only for quadratic
polynomial vector ﬁelds we know the exact value of it, that is M (2) = 3. This fact
was proved by Bautin in [2]. Concerning M (N ) for N ≥ 3, up to now, only lower
bounds for these numbers has been obtained, as detailed below.
In ﬁnding lower bounds of H(N ) it is worth mentioning that one of the most used
techniques to create limit cycles is by perturbing Zq-equivariant polynomial Hamil-
tonian vector ﬁelds. Frequently, this technique is combined with other procedures
such as: Hopf bifurcation method, homoclinic and heteroclinic bifurcation methods,
Abelian integrals and bifurcation from inﬁnity, . . . , see [9, 13, 23].
The known best result on M (3) was obtained by ˙Zo l¸adek in [31], getting M (3) ≥
11. This work has been amended in [33] although the same bound for M (3) is
maintained. The proof was made, after a cubic perturbation of a cubic diﬀerential
equation having a rational ﬁrst integral, by bounding the zeros of the displacement

HILBERT NUMBERS USING REVERSIBLE CENTERS 5

map. This displacement map, in ﬁrst approximation, is given by a linear Poincar´e-
Pontriaguin integral which is expressed in terms of twelve Abelian or Melnikov type
integrals (ﬁrst order Melnikov integrals) generating the aforementioned eleven limit
cycles. Linked with the ﬁrst paper of ˙Zo l¸adek, in 2005, Christopher in [7], among
other results, conﬁrmed the lower bound for cubic polynomial vector ﬁelds, that
is M (3) ≥ 11. He uses a family of cubic systems, C (12)
31 according ˙Zo l¸adek’s more
recent classiﬁcation [32], having also a rational ﬁrst integral and showing that the
linear part of the ﬁrst Lyapunov quantities have maximal rank 11. In [4], Bondar
and Sadovsk˘ı also proved, with the same technique but with a diﬀerent Darboux
center, that M (3) ≥ 11.
In the case N = 4, that is on quartics systems, in [11], Gin´e proved that M (4) ≥
21, by studying small limit cycles bifurcating from an elementary center-focus type
equilibrium point. In the case N = 5, i.e. concerning lower bounds of M (5), the
known best estimation is the one given by Gin´e in [11], where M (5) ≥ 26 was proved.
These limit cycles also bifurcate from an elementary center-focus type equilibrium
point at the origin. In this paper, Gin´e conjectured that the number of functionally
independent focal values, i.e. the minimum number of ideal generators of the ideal
generated by the focal values, of system (1) with an elementary center-focus type
equilibrium point at the origin is M (N ) = N 2 + 3N − 7. We want to point out that,
regarding Gin´e’s conjecture, we would have M (4) = 21 and M (5) = 33.
In the cases N = 6, . . . , 13, Liang and Torregrosa in [20] proved that the cyclicity
of some holomorphic Darboux center for system (1) is, at least, N 2 + N − 2, for
4 ≤ N ≤ 13. Hence, we have the lower bound H(N ) ≥ M (N ) ≥ N 2 + N − 2, for
4 ≤ N ≤ 13. We point out that in that work, the authors say that the best center
candidate to produce high cyclicity is of Darboux type. One consequence of their
paper is that, by one hand, this result gives the highest known up to now lower
bound of M (6), M (7), . . . , M (13), and that these numbers are smaller than those
conjectured before. In particular, for N = 6, 8, 10 are also the best lower bound for
Hilbert numbers, i.e. H(6) ≥ 40, H(8) ≥ 70, and H(10) ≥ 108.
A lower bound of M (N ), for all N , was given by Movasati, see [22, Cor 4.1]. In
this paper it is proved that, the cyclicity of holomorphic centers perturbing with
polynomial degree N systems is not less than M (N ) ≥ N 2 − 2. In regards to upper
bounds of M (N ), Mardesic, in [21], proved that an upper bound for the cyclicity
of a period annulus around an equilibrium point of center-focus type, given by a
Hamiltonian polynomial of degree N diﬀerential equation, is M (N ) ≤ (N 4 + N 2 −
2)/2. This bound was obtained as an upper bound of the number of zeros of the
corresponding Abelian integral.

Next we summarize some of the recent progress in ﬁnding lower bounds of H(N ).

On H(2), Shi (see [24]) and Chen and Wang (see [5]) proved that H(2) ≥ 4. They
obtained these four limit cycles in two nests, one with 3 and another with 1.
On H(3), in 2009, Li, Liu, and Yang (see [18]), by counting the number of ze-
ros of some Abelian integrals, demonstrated that an speciﬁc planar cubic system
has H(3) ≥ 13. Later, Li and Liu (see [19]) also proved that H(3) ≥ 13, using
Z2-equivariant cubic perturbations, Hopf bifurcation and changing the stability of
inﬁnity. These 13 limit cycles appear in two nests of 6 and one coming from inﬁnity.
About H(4), Christopher, [7] in 2005, provided a quartic system with H(4) ≥ 22.
As we have mentioned before, he used the linear parts of the Lyapunov quantities

6 R. PROHENS AND J. TORREGROSA

for center bifurcations with symmetries, the limit cycles appear in two nests of 6 and
one nest of 10. Recently, in 2011, Johnson constructed (see [15]) a quartic system
that has 24 limit cycles, using Lyapunov quantities, in four nests of 6. Moreover, the
existence of 2 more, having each one inside two of these nests, is showed numerically.
Then, H(4) ≥ 26.
In the study of H(5), in 2008, Wu, Gao, and Han in [28] found that H(5) ≥
28, in four diﬀerent conﬁgurations, by using the perturbation of a Z2-equivariant
symmetric quintic Hamiltonian system. Later, in 2010, Wu, Wang, and Tian, in
[29] proved also H(5) ≥ 28 with a Z4-equivariant symmetric quintic vector ﬁeld,
by using the Hopf and polycycle bifurcation methods. Also in 2010, Johnson and
Tucker, in [17], studied the limit cycle bifurcation of a Z2-equivariant quintic planar
Hamiltonian vector ﬁeld under Z2-equivariant quintic perturbation and, by computer
aided approach, proved that H(5) ≥ 27. In 2015, Sun and Han in [25] also proved
that H(5) ≥ 28 using Z4-equivariant perturbations.
Concerning H(6), in 2005, Wang and Yu, showed that H(6) ≥ 35, by using global
and local bifurcations, see [26]. In this paper the authors perturb a ﬁfth-degree
Z2-equivariant symmetric Hamiltonian system by adding a sixth-degree polynomial
system. More recently, in 2015, Liang and Torregrosa, by computing the required
independent linear parts of the Lyapunov quantities, proved that H(6) ≥ M (6) ≥
40, see [20].
On H(N ), for N ≥ 7, it is worth mentioning the relevant paper of Han and Li
[14] in 2012. The results in this work improved almost all existing lower bounds of
H(N ) for such values of N , up to that moment. More concretely, they proved that
H(7) ≥ 65, H(9) ≥ 98, H(11) ≥ 153, H(12) ≥ 157,. . . In 2010, Johnson and Tucker
in [16] proved that H(7) ≥ 53, perturbing a Z2-equivariant planar Hamiltonian
vector ﬁeld of degree 7. The proof follows a computer aided approach. For N = 11,
before the paper of Han and Li, the best one was the one given by Wang and Yu in
2006, in [27], proving that H(11) ≥ 121 using a Z12-equivariant vector ﬁeld. With
respect to H(8), until 2012 the best lower bound for this Hilbert number was the one
given by Han and Li, as H(8) ≥ 67. Nevertheless, in 2015, Liang and Torregrosa,
in [20], obtained a new better one, that is H(8) ≥ M (8) ≥ 70. In this paper it was
also proved that H(10) ≥ M (10) ≥ 108.
Concerning the rate of grow of H(N ) as N increases, one of the ﬁrst results in
ﬁnding a general lower bound we want to point out, is the work of Christopher
and Lloyd in 1995, see [8], where they introduced a recurrence mechanism to pro-
vide a lower bound for H(N ) of type KN 2 log N. Recently, in 2012, Han and Li
improved this mechanism by providing a better lower bound of the same kind, see
[14]. Concretely, for N big enough, they showed that H(N ) grows at least as fast
as (N + 2)2 log(N + 2)/(2 log 2).

3. The bifurcation mechanism

The bifurcation mechanism, in short, is as follows. First, we consider a reversible
system (symmetric with respect to the x-axis) having a center at the origin and two
more at two symmetric points (xc, ±yc), with x2
c + y2
c ̸= 0. Second, we consider a
ﬁrst perturbation obtaining n (simultaneously) hyperbolic limit cycles in two nests
while the origin remains as a center. Finally, we consider a second perturbation
of the system giving us m limit cycles, around this third nest, increasing the total

HILBERT NUMBERS USING REVERSIBLE CENTERS 7

number of limit cycles obtained. Then, we will say that the 2 × n + m limit cycles
appear in conﬁguration ⟨n, m, n⟩.
The limit cycles appear using degenerated Hopf bifurcations of some order k and
all the unperturbed polynomial systems have rational ﬁrst integrals. Concerning
the Lyapunov quantities computation we use linear or higher order developments
of Lyapunov quantities, as in the works of Christopher ([7]) and Han ([12]). In
this paper, reversible diﬀerential systems in the (x, y)-plane means invariant under
the change of variables (x, −y, −t) → (x, y, t). Moreover, all the centers are non
degenerate.
As all the computations are quite hard to do and the obtained expressions are
too big to be written here, we will describe only the bifurcation mechanism more
in detail. This bifurcation scheme is the same followed by Christopher (see also [7])
but we use higher instead of ﬁrst order. In some simple cases and for lower degrees
we will also show which are the Taylor series of the Lyapunov quantities.

3.1. Degenerated Hopf bifurcation. An analytic system with a non-degenerate
equilibrium point of center-focus type can be transformed to the system

x′ = λx − y + f (x, y),

y′ = x + λy + g(x, y), (2)

where f and g are analytic functions with lower order terms of degree 2 in x, y,
being λ a real parameter and with the equilibrium point located at the origin.
When λ = 0 we have a weak focus or a center at the origin. The problem to distin-
guish its stability is the well-known center-focus problem. There are some classical
approaches to solve it, see [1] for instance. Here we will use the Andronov-Poincar´e
method, that is the computation of the obstruction conditions for its integrabil-
ity, but using complex notation. Hence, following the approach of [24], system (2)
writes, in complex coordinates (z = x + iy), as

z′ = (λ + i)z + F2(z, ¯z) + F3(z, ¯z) + · · · , (3)

where Fj are homogeneous polynomials of degree j in z, ¯z.
Now, if λ = 0, we look for the existence of a formal ﬁrst integral of the form

H(z, ¯z) = z ¯z + H3(z, ¯z) + H4(z, ¯z) + · · · ,

with Hj homogeneous polynomials of degree j in z, ¯z. This can be done imposing
that the level curves of H contain solutions of equation (3). Straightforward com-
putations show that the coeﬃcients of H3 can be uniquely determined in terms of
the coeﬃcients of F2, by solving the diagonal linear system of equations obtained
vanishing all the coeﬃcients in z, ¯z of the homogeneous polynomial of degree 3

¯zF2 + z ¯F2 + iz ∂H3
∂z − i¯z ∂H3
∂ ¯z .

We can not follow exactly in the same way, to ﬁx the coeﬃcients of H4, because the
linear system of equations obtained vanishing the coeﬃcients of the homogeneous
polynomial of degree 4,

¯zF3 + z ¯F3 + iz ∂H4
∂z − i¯z ∂H4
∂ ¯z + ∂H3
∂z F2 + ∂H3
∂ ¯z ¯F2 ≡ 0,

has not maximum rank ﬁve. This obstruction can be removed by adding an extra
term, L1z2 ¯z2 for example, in the above homogeneous identity. This constant L1

8 R. PROHENS AND J. TORREGROSA

is known as the ﬁrst Lyapunov quantity. Clearly, H is a Lyapunov function when
L1 ̸= 0 and gets the stability of the origin. When L1 = 0, we need to compute
higher degree terms of the function H for distinguishing when the equilibrium point
is a center or a focus. This constant L1 can be thought as the ﬁrst obstruction for
(3) being integrable. In the recursive procedure to get Hj, for j = 3, . . . , it can be
proved that all the linear systems giving the coeﬃcients of H2k+1, k = 1, 2, . . . , have
maximum rank. Consequently H2k+1 can be uniquely determined. But in each even
step, i.e. to determine H2k+2, k = 1, 2, . . . , we need to add a correction term of
the form Lkzk+1 ¯zk+1. These quantities Lk are the well known Lyapunov quantities
associated to equation (3). Clearly, the ﬁrst non-vanishing Lyapunov quantity, Lk,
gives the stability of the origin. In this case, as usual, we say that the origin is a weak
focus of order k. We would remark that the main computational diﬃculties to obtain
the Lyapunov quantities, applying this procedure or in general other methods, are
only because of their huge expressions.
For polynomial systems, the Lyapunov quantities can be used, besides to deter-
mine the stability of the origin and the center conditions of system (2), to obtain
periodic orbits from the origin. For example when L1 < 0 and λ = 0 the origin is
stable and for λ > 0, small enough, the stability of the origin changes to unstable
and an small stable hyperbolic periodic orbit bifurcates from the origin. This is the
well-known Hopf bifurcation. An analogous procedure can be used to create k limit
cycles from a weak focus of order k by a degenerate Hopf bifurcation. These limit
cycles are also known as small limit cycles. See [3], for instance.
Now we will describe how the small limit cycles appear in a degenerate Hopf
bifurcation. Suppose that system (2) is a polynomial system, that we call system
S, having, without loss of generality, an stable weak focus of order k at the origin.
Then, λ = 0 and the Lyapunov quantities satisfy L1 = L2 = · · · = Lk−1 = 0,
Lk < 0. Let Γ be a level curve of H which is suﬃciently near the origin that the
ﬂow is inward across it. Now we perturb system S in such a way that the perturbed
system, we call it system S1, has λ = L1 = L2 = · · · = Lk−2 = 0, Lk−1 > 0. The
origin is thus unstable. If S1 is suﬃciently near S, the ﬂow remains inward across Γ
and, if H 1 is the Lyapunov function corresponding to S1, there exists a level curve
Γ1 of H 1 inside Γ and suﬃciently near the origin that the ﬂow is outward across Γ1.
By the Poincar´e-Bendixson Theorem, there is a limit cycle between Γ and Γ1. The
next step is to take a perturbation, S2, of system S1 so that L1 = · · · = Lk−3 = 0
and such that Lk−2 < 0. In this case, if the perturbation is suﬃciently small, the
ﬂow remains inward across Γ and outward across Γ1. Hence, S2 has a limit cycle
between Γ and Γ1 and, since the origin is stable for S2, there is also a limit cycle
inside Γ1. Proceeding in this way, k limit cycles can be generated. The necessary
conditions (denoting L0 = λ) are

LjLj+1 < 0, |Lj| ≪ |Lj+1|, j = 0, . . . , k − 1.

When we study the degenerate Hopf bifurcation in a family of polynomial systems
(2) of ﬁxed degree, there is a classical problem: “the existence of parameters ensuring
the independence of the Lyapunov quantities to get exactly k periodic orbits near a
weak focus of order k”. Another related question is “which is the maximum weak
focus order in a given family”. Both questions concern to Hilbert’s 16th problem,
providing lower bounds for the Hilbert number, H(N ). A way to tackle this problem
is obtaining polynomial families having a weak focus of the highest order that unfold

HILBERT NUMBERS USING REVERSIBLE CENTERS 9

this number of periodic orbits. We recall that, for analytical perturbations, always
a weak focus of order k unfolds k hyperbolic limit cycles, see [23].

3.2. Cyclicity of centers. In this paper we select polynomial center families of
degree N having cyclicity at least k. We recall that the cyclicity at an equilibrium
point can be deﬁned as the maximum number of isolated periodic orbits bifurcating
from it. In our approach this is equivalent to say that, in the parameters space,
near the origin and after perturbing the center with polynomials also of degree N ,
there will be a curve of weak foci of order k passing though the origin and unfolding
k hyperbolic periodic orbits. We remark that, in the parameters space, the origin
corresponds to the case in which the system, not perturbed, has a center. As we can
always obtain a limit cycle with the trace parameter, λ, we will restrict our analysis
to the class of zero trace perturbations. That is, to the perturbations whose lower
degree terms are of degree two. As we have mentioned before, to get the existence
of these curves in the parameters space and the corresponding unfolding from the
Taylor developments, we follow the ideas of Christopher, [7], and Han, [12]. The
existence of a curve of weak focus is obtained studying the intersection of the Taylor
developments of the varieties Lj = 0, for j = 1, . . . , k − 1 ensuring that along it
Lk is non-vanishing. The unfolding of k limit cycles (adding the trace parameter)
and their hyperbolicity is obtained from the transversality of the intersection of the
varieties. Clearly, using the implicit function theorem, if the matrix deﬁned by the
linear terms of L1, . . . , Lk have rank k we have (adding λ) at least k hyperbolic limit
cycles bifurcating from the center point.
Consider the equation
 z′ = iz + Fc(z, ¯z), (4)

in complex variables (z = x + iy), with Fc a polynomial starting with second order
terms, having a center at the origin. The Lyapunov quantities, Lj, associated with
equation
 z′ = iz + Fc(z, ¯z) + F (z, ¯z), (5)

where F is a polynomial perturbation, also starting with second order terms in z, ¯z,
can be written, using its Taylor series in the parameters space, as

Lj = L(1)
j + L(2)
j + L
(3)
j + · · · , (6)

where L
(ℓ)
j are homogeneous polynomials of degree ℓ in the coeﬃcients of F .
All the computations in this paper are done adapting the algorithm described
above, see also [20], for obtaining directly the Taylor series of Lj up to order ℓ,
generally ℓ = 1, and in some cases ℓ = 2 or higher, at the selected center.

3.3. Simultaneous Hopf bifurcations. The use of previous described center bi-
furcation method, combined with symmetry techniques (reversible systems), is a
useful tool in obtaining lower bounds for the number of limit cycles in polynomial
systems, see [8]. We use this tool, with two perturbations, to obtain limit cycles
appearing simultaneously in three nests of limit cycles, two symmetric out of the
symmetry line and one on it. We are going to present the idea of combining these
two perturbations to generate limit cycles.

10 R. PROHENS AND J. TORREGROSA

Let f and g be polynomials in x, y. Consider a polynomial reversible system with
an equilibrium point of center type at the origin

x′ = −y + yfc(x, y2),

y′ = x + gc(x, y2), (7)

having two more symmetric equilibrium points, (xc, ±yc), of center type out of the
symmetry line. This conﬁguration is depicted in Figure 1. We consider a general
perturbation of degree N of system (7) in two independent steps.

First, considering that we want to preserve the center at the origin, we take a
perturbation of system (7) keeping the reversibility symmetry at the origin,

x′ = −y + yfc(x, y2) +
 N∑

k+2ℓ+1=1 fk,2ℓ+1 xky2ℓ+1,

y′ = x + gc(x, y2) +
 N∑

k+2ℓ=1 fk,2ℓ xky2ℓ.
 (8)

We observe that is not restrictive to assume that the origin remains as a critical
point. Then, we translate system (8) in order that the center (xc, yc) moves to
the origin. Additionally, we restrict the perturbation parameters fk,ℓ such that the
perturbation terms in the translated system start with terms of degree 2. Then, the
method of small limit cycles generation around the origin, described in the ﬁrst part
of this section, applies. Let n be the maximum number of limit cycles obtained,
around the origin, with this technique. Then, we have n small limit cycles, by a
simultaneous degenerated Hopf bifurcation, surrounding each one of the equilibrium
points (xc, ±yc).
We remark that the origin of system (8) remains a center when the 2n limit cycles
have been created. Clearly, with this method we can obtain, at most, as limit cycles
as the number of free parameters, that is 2n ≤ (N +5)(N −2)/2. In the next sections
it is shown that in our best results never reach this number but, nevertheless, we
are close to it.

The second step is to consider a perturbation that completely breaks the symmetry
at the origin,
 x′ = −y + yfc(x, y2) +
 N∑

k+2ℓ+1=2 ek,2ℓ+1 xky2ℓ+1,

y′ = x + gc(x, y2) +
 N∑

k+2ℓ=2 ek,2ℓ xky2ℓ.
 (9)

Let m be the maximum number of small limit cycles obtained using, once again,
the previous described technique to study the degenerate Hopf bifurcation, but now
applied to system (9). As above, we can obtain, at most, as many limit cycles as
the number of free parameters; that is, m ≤ N (N + 2)/2.
Finally, from the above arguments, and since the perturbation parameters in sys-
tems (8) and (9) are independent, we have that the 2n small limit cycles surrounding
the equilibria (xc, ±yc) are hyperbolic and remain after the other perturbation, i.e.
they remain while m limit cycles emerging from the origin. This method is used in
detail, in the next section, for a cubic system.

HILBERT NUMBERS USING REVERSIBLE CENTERS 11

Considering all together, at least 2n + m small limit cycles has been obtained; m
small limit cycles surrounding the origin and n small limit cycles surrounding each
one of the two symmetric equilibrium points. We will say that the 2 × n + m limit
cycles are in conﬁguration ⟨n, m, n⟩.

4. Reversible cubic centers with two extra symmetric centers out
of the symmetry line

The aim of this section is to present the method introduced in Section 3, of
simultaneous occurrence of limit cycles via a degenerate Hopf bifurcation, through a
particular case. We introduce this method by studying some cubic reversible family
of centers. We want to remark that using other families of cubic centers and other
bifurcation techniques, more limit cycles can be obtained, see [18, 19].
First, see Proposition 3, we classify all reversible cubic systems having a non-
degenerate equilibrium point of center type at the origin plus two more non-degene-
rate centers out of the reversibility symmetry line. Clearly, up to an aﬃne change
of variables and a time rescaling if necessary, it is not restrictive to assume that the
symmetry axis is the straight line y = 0. Hence, the reversible cubic centers family,
having two extra symmetric centers out of the symmetry line, that we consider write
as x′ = −y + a11xy + a21x2y + a03y3,

y′ = x + b20x2 + b02y2 + b30x3 + b12xy2. (10)

Second, see Proposition 5, following the procedure described in the previous sec-
tion, we study the simultaneous degenerate Hopf bifurcation of limit cycles in con-
ﬁguration ⟨1, 7, 1⟩ for family (10).
As we will see in the proof we can not provide better examples using this bifur-
cation technique for cubic vector ﬁelds. We recall that the family of cubic systems
can exhibit up to 13 limit cycles, as it is proved in [18, 19].

We ﬁnish this section showing some systems of family (10), with diﬀerent phase
portraits, exhibiting the same conﬁguration ⟨1, 7, 1⟩ of limit cycles.

Proposition 3. After a rescaling, if necessary, the reversible cubic system (10) has
three non-degenerate centers, one at the origin and two at (xc, ±yc) with x2
c +y2
c ̸= 0,
if and only if, the determinant of the Jacobian matrix of system (10) at (xc, yc), α,
is positive, a03 = 1,

a11 = (x2
ca21 + y2
c − 1)/xc,

b02 = (x4
cy2
c (a2
21 + 2b30) + x2
cy2
c (2 − y2
c )a21 + α2x2
c − 2x2
cy2
c − y4
c + y2
c )/(2xcy4
c ),

b12 = −(x4
cy2
c (a2
21 + 2b30) + 2x2
cy2
c a21 + α2x2
c − y6
c − 2x2
cy2
c + y2
c )/(2x2
cy4
c ),

b20 = (x2
cy2
c a21 − 2x4
cb30 − y4
c − 2x2
c + y2
c )/(2x3
c),
 (11)

and c1 = 0 or c2 = 0, with

c1 =x2
c(x2
ca21 − y2
c + 1)α2 + y2
c (
x6
ca3
21 + 3x4
ca2
21 + 2x6
ca21b30
− x2
c(y4
c + 2x2
c + y2
c − 3)a21 + 2x4
c(y2
c + 1)b30 − 2x2
c − y2
c + 1)
, (12)

c2 =x4
cy2
c a2
21 − 2x2
cy2
c (y2
c − 1)a21 + 2x4
cy2
c b30 + α2x2
c − y6
c − 2x2
cy2
c + y2
c . (13)

Moreover, system (10) either has a polynomial inverse integrating factor when c1 = 0
or a polynomial ﬁrst integral of degree four when c2 = 0.

12 R. PROHENS AND J. TORREGROSA

Proof. Straightforward computations show that when a03 = 0 it is not possible to
have a weak focus at (xc, yc). Hence, after a re-scaling of the (x, y) variables if
necessary, we have a03 = 1. Then, imposing that system (10) has a non-degenerate
weak focus at (xc, yc), the determinant of the Jacobian matrix at this point, that we
call α, must be positive and, furthermore, we get conditions (11).

Following the procedure described in Section 3, the ﬁrst Lyapunov quantity is

L1 = −c1c2/(4α3x5
cy5
c ),

where c1 and c2 are given by expressions (12) and (13), respectively. Hence, condi-
tions c1 = 0 or c2 = 0 are required for the existence of a center at (xc, yc).
When c1 = 0, system (10) has the polynomial inverse integrating factor

V (x, y) =g1g2 x4 + g1g3 x2
c x2y2 + 2g1g4 x4
cy2
c y4 − g1g5 xc x3 + 2g1g6 x3
c xy2

+ g7 x2
c x2 + g8 x4
c y2 − g4g9g10 x3
cy2
c x − g2
4g9 x4
cy4
c ,

where

g1 = (x2
ca21 + y2
c − 1)x2
cα2 − y2
c (x2
ca21 − 2x2
c − y2
c + 1),

g2 = x2
c(x2
ca21 − y2
c + 1)α2 + y2
c (x6
ca3
21 + 3x4
ca2
21 − (y4
c + 2x2
c + y2
c − 3)x2
ca21
− 2x2
c − y2
c + 1),

g3 = 2α2x2
c + y2
c (
3x4
ca2
21 + x2
c(2y2
c + 5)a21 − y4
c − 2x2
c − y2
c + 2),

g4 = x2
ca21 + y2
c + 1,

g5 = 2x2
c(x2
ca21 − y2
c + 1)α2 + y2
c (x6
ca3
21 + (y2
c + 4)x4
ca
2
21 − x2
c(y4
c + 6x2
c − 5)a21
− y6
c − 2x2
cy2
c − 6x2
c − y2
c + 2),

g6 = 2α2x2
c + y2
c (x4
ca2
21 + x2
c(2y2
c + 1)a21 + y4
c − 2x2
c − y2
c )
,

g7 = −2x4
c(x2
ca21 − y2
c + 1)α4 + x2
cy2
c (x6
ca3
21 − x4
c(4x2
c − y2
c + 2)a
2
21 − 4x2
cy4
c − y6
c
− x2
c(8x2
cy2
c + y4
c − 6x2
c − 6y2
c + 7)a21 − 2x2
cy2
c + 10x2
c + 5y2
c − 4
)α2

+ (x2
ca21 − 2x2
c − y2
c + 1)(
x6
ca3
21 + 2x4
cy2
c a2
21 + x2
c(y4
c + 6x2
c + 3y2
c − 3)a21
+ 4x2
cy2
c + y4
c + 6x2
c + y2
c − 2
)
y4
c ,

g8 = −4α4x4
c − 2x2
cy2
c (x4
ca
2
21 + 2x2
cy2
c a21 + 2x2
ca21 + y4
c − 4x2
c − 2y2
c + 1)α2

+ y4
c (x2
ca21 − 2x2
c − y2
c + 1)(
x4
ca
2
21 + x2
c(2y2
c + 3)a21 + y4
c + 2x2
c + 5y2
c + 2)
,

g9 = x2
ca21 − 2x2
c − y2
c + 1,

g10 = −2α2x2
c + y2
c (x4
ca2
21 + x2
c(2y2
c − 1)a21 + y4
c + 2x2
c + y2
c − 2
)
.

The proof ﬁnishes by direct calculations showing that, when c2 = 0, system (10) is
a Hamiltonian system with a degree four polynomial ﬁrst integral. □

Remark 4. In the above proof, before obtaining the inverse integrating factor, two
more Lyapunov quantities can be computed. But they vanish when L1 = 0. This fact
could indicate that only one limit cycle can be obtained around the equilibrium point
lying outside the symmetry axis.

HILBERT NUMBERS USING REVERSIBLE CENTERS 13

Proposition 5. The cubic system

x′ = −(256x2 − 147y2 − 512x + 844)y,

y′ = (4x2 − 293y2 − 8x)(x − 1). (14)

has a center at the origin and two symmetric centers at (1, ±2). Moreover, there
exists a cubic polynomial perturbation such that it unfolds 9 small limit cycles by a
simultaneous degenerate Hopf bifurcation in conﬁguration ⟨1, 7, 1⟩. In detail, after
perturbing, 7 limit cycles surround the origin while each one of the 2 other limit
cycles surrounds one of the perturbed symmetric centers.

Proof. The ﬁrst statement follows because system (14) has the next rational ﬁrst
integral
 H(x, y) = (61x2 + 183y2 − 122x + 211)5

(1220x2 − 14945y2 − 2440x + 3376)4 .

The second statement follows from considering the perturbation monomials in two
steps, ﬁrst the reversible perturbation monomials with respect to the origin, and then
the non reversible ones. We can proceed in this way because both perturbations are
independent. Let us expose these arguments in detail.
First, we perturb system (14) only with the cubic reversible perturbation mono-
mials as it is given in expression (8), that is

x′ = −(256x2 − 147y2 − 512x + 844)y + f21x2y + f03y3 + f11xy + f01y,

y′ = (4x2 − 293y2 − 8x)(x − 1) + f30x3 + f12xy2 + f20x2 + f02y2 + f10x. (15)

We perturb in this way because this perturbation does not break the symmetry at
the origin and, hence, we keep the center at that point. Adding the next conditions,

f10 = f30 + 8f03 + 4f12, f11 = −2f21,
f01 = f21 − 4f03, f02 = −f12,
f20 = −8f03 − 2f30 − 4f12,

the points (1, ±2) remain as equilibrium points of system (15) with zero trace. That
is, they are either centers or weak foci. Now, we will study the degenerate Hopf
bifurcation and the maximum order at the equilibria (1, ±2) as weak foci.
Following the notation introduced in (6), the linear part of the ﬁrst three Lyapunov
quantities, after the change of variables
{
f30 = y4, f21 = y3, f12 = y2, f03 = 19208
61 y1 − 1
2y2 + 1
8y4
} ,

write as
 L
(1)
1 = y1, L
(1)
2 = −3003925
4148928y1, L
(1)
3 = 14324144100569
15300980932608y1.

Clearly, using these three quantities and after changing the trace, at (1, ±2) we can
get only one small limit cycle surrounding each equilibrium by using the double
symmetric Hopf bifurcation. Moreover, the origin remains as a center. Computing
higher order terms, in the Lyapunov Taylor series expansion on the perturbation
coeﬃcients, we can get no more limit cycles surrounding these equilibrium points.

14 R. PROHENS AND J. TORREGROSA

Secondly, to study the Hopf bifurcation at the origin, we consider a cubic non
reversible perturbation of system (14), independent with respect to the above one,

x′ = −(256x2 − 147y2 − 512x + 844)y + e30x3 + e12xy2 + e20x2 + e02y2,

y′ = (4x2 − 293y2 − 8x)(x − 1) + e21x2y + e03y3 + e11xy. (16)

Then, the linear parts of the ﬁrst ﬁve Lyapunov quantities at the origin, L(1)
j ,
j = 1, . . . , 5, are linearly independent with respect to the perturbation parame-
ters {e02, e03, e11, e12, e20}, because the matrix expressing these linear parts in terms
of the perturbation parameters









 973
844 0 2071
1688 2 0

− 314714···9820271
195243···1648896 − 66227···4599
9253···83360 − 211540···35229
15619···1680 − 106973···61723
462662···1680 − 984171···3183459
78097···55840
− 200346···233733021
111263···38484480 − 62294···25129
26365···915840 − 39622···881503
44505···3937920 − 575998···957887
329571···64480 − 445637···9457639
22252···968960
− 378263···05108291
54817···827228672 9201158864667
16237522460672 − 102311···7592337
10963···4457344 − 47561762093925
32475044921344 − 94410143272665
685223···03584
409395075
1202423168 3583821
2849344 − 914339715
4809692672 − 206403
1424672 269741085
2404846336
 









has determinant diﬀerent from zero. Then, by naming L
(1)
j = xj, j = 1, . . . , 5 to
these linear parts and by adding {−50723e30 + 64370e21 = x6, e30 = x7}, we get that
the linear part of the next two Lyapunov quantities are

L
(1)
6 = − 66694096304772573135207068214846052608276037011880146949968106767
118456040720121071307810175534967521775273397089522308616122531840 x1

− 986857882481001983077574408738310242905679762830619750163
2969506583172454313990723467150121014703569791340500746240 x2

− 368672592894986791238956153658592848962867997427877
1823801029483205625394394663302399350773808685383680 x3

− 137091470959965151517258036957371407797436275
64007751590654046173238284436782619114217472 x4

+ 20142243532513229363034276626368334529
11232015437703212769893400803269562944 x5,

L
(1)
7 = − 605442557589991878553884569125575916881324522829664632170711489980338597
337522008889632653804481076799506498365244602356647852921497039363112960 x1

− 4681103927192298270535681990962679610902010473387521657386808069
3384458306289173465937433586713357765007811345414923103317786624 x2

− 130456147973103575784262647445829365947450177664718011212431
166292368657657441583480514160406776823399908315068041789440 x3

− 64452346898380758995060611894437235640368695062374433
14590408235865645003155157306419194806190469483069440 x4

+ 234977057189451422295127519143367170772214655
256031006362616184692953137747130476456869888 x5.

Clearly, up to ﬁrst order perturbation of the Lyapunov quantities and adding the
trace parameter, we can only get 5 small limit cycles surrounding the origin, and no
more. Considering all together, using only the ﬁrst order Lyapunov quantities and
the trace parameter, we have 7 limit cycles in conﬁguration ⟨1, 5, 1⟩ for some cubic
systems near system (14).
If we want more limit cycles we can compute, up to order three, the ﬁrst seven
Lyapunov quantities. From the above ﬁrst order study, using the implicit function
theorem, up to a change of variables (in the parameters space), if necessary, we can
write Lj = xj +OK(x) for j = 1, . . . , 5 with x = (x1, . . . , x7) and K ≥ 2. Here OK(x)
denotes all the terms of degree at least K on the coordinates of x. It is clear that,
when Lj = 0 for j = 1, . . . , 5, we have L
(1)
6 = L(1)
7 = 0. But, in this case, we have also

HILBERT NUMBERS USING REVERSIBLE CENTERS 15

L(2)
6 = L(2)
7 = 0. Then, up to order two we have no more limit cycles. Computing
the third order and evaluating on L1 = · · · = L5 = 0 we have

L(3)
j (x6, x7) = C (3)
j x3
6 p2(x7/x6), for j = 6, 7,

with
 p2(λ) = 3695279045405753944 λ2 + 271388730148261 λ + 10087769971

and
 C (3)
6 = 14810743699301227153984257377365779343617
2167350437458050857073941269092541778503862023955797053468443248160 ,

C (3)
7 = 422529517425810659146496535729952424790939892023
24702107859473889845193968445764877445317232939145226398071951833940828160 .

Finally, as the above homogeneous parts of degree three are also multiple one from
the other and since L(4)
7 = 0, we need compute up to order ﬁve the ﬁrst seven Lya-
punov quantities. If we proceed in this way, doing the same simpliﬁcation procedure
as in the previous steps, we get

L(5)
7 (x6, x7) = C (5)
7 x5
6 p4(x7/x6)

with C (5)
7 = 9
19645876735529840 · · · 17973196784896000000
and p4(λ) =211148735150868711498020 · · · 214462220974330859217 λ
4

+ 153229267494841185603714 · · · 695050974950207558339 λ
3

− 278673331636981994254986 · · · 869624591189537981617 λ2

− 130937529746819089567596 · · · 578679565217539087419 λ
− 227414742460144672742349 · · · 215962576056358409128.

Then, after some necessary arrangements because of the linear dependence of the
ﬁrst order terms, the Lyapunov quantities up to order ﬁve can be written as
L1 =x1 + O6(x1, . . . , x7),

L2 =x2 + O6(x1, . . . , x7),

L3 =x3 + O6(x1, . . . , x7),

L4 =x4 + O6(x1, . . . , x7),

L5 =x5 + O6(x1, . . . , x7),

L6 =C (3)
6 x3
6p2(x7/x6) + O6(x1, . . . , x7),

L7 =C (5)
7 x5
6p4(x7/x6) + O6(x1, . . . , x7).

The polynomial p2 has two simple real zeros, λ1 and λ2, and the resultant of p2 and
p4 is diﬀerent from zero. Hence, for every x6 small enough and diﬀerent from zero,
there exist two curves near x1 = x2 = · · · = x5 = 0 and x7 = λℓx6, ℓ = 1, 2 such that
Lj = 0, j = 1, . . . , 6 and L7 ̸= 0. Moreover, over these curves, the intersection of the
varieties Lj is transversal. Consequently, as in [7], they deﬁne two families of weak
foci of order seven that unfold, perturbing also the parameter that deﬁnes the trace
at the origin, seven small limit cycles via a degenerate Hopf bifurcation. Hence,
by computing the Lyapunov quantities up to order ﬁve in terms of the perturba-
tion parameters, we have proved the existence of cubic polynomial perturbations

16 R. PROHENS AND J. TORREGROSA

of system (14) unfolding 9 small limit cycles by a simultaneous degenerate Hopf
bifurcation in conﬁguration ⟨1, 7, 1⟩, as we wanted prove.
Finally, we would like to remark that the homogeneous terms of degree 2 and 4
for all the computed Lyapunov quantities corresponding to the origin of system (16)
vanish identically. This explains why, in the above computations, only appear the
terms of degrees 1, 3 and 5. Additionally, we have not write down all the ﬁgures of
all the involved integer numbers in the previous expressions because of their size. □

Under the assumptions of Proposition 3 there are other cubic systems with the
same conﬁguration of two symmetric centers and one more on the symmetry line
and exhibiting the same bifurcation phenomenon. All of them with 9 limit cycles,
but having diﬀerent type of ﬁrst integrals or inverse integrating factors. We show
some of them in the next examples skipping the explicit computations.
The cubic system
 x′ = y3 − y,

y′ = 2x3 + 1
6 xy2 − 3x2 − 1
12y2 + x, (17)

has the inverse integrating factor

V = (12x2 − 8y2 − 12x + 9)(12x2 + 9y2 − 12x − 8),

and the polynomial ﬁrst integral

H = (12x2 − 8y2 − 12x + 9)9(12x2 + 9y2 − 12x − 8)
8.

Not all the systems with the described conﬁguration have a polynomial or rational
ﬁrst integral. For example the cubic system

x′ = −6yx
2 + y3 + 3xy − y,

y′ = −3
4xy2 − 5
8x3 + 21
4 y2 − 147
8 x2 + x, (18)

with an integrating factor

V = 205x4 − 1722x2y2 + 328y4 + 14678x3 − 2460xy2 − 12050x2 + 1612y2 + 2376x − 176

has the next ﬁrst integral

H = log (205x4 − 1722y2x2 + 328y4 + 14678x3 − 2460xy2 − 12050x2 + 1612y2

+ 2376x − 176
) + 54
√
401 arctanh
 (√401 (−1722x2 + 656y2 − 2460x + 1612)
32882x2 − 65764x + 33684
 )
 .

Inside this cubic family, after perturbation, there are also systems sharing this
conﬁguration with polynomial ﬁrst integral. For example, systems

x′ = 448x2y + 64y3 − 80xy − y,

y′ = 312x3 − 448xy2 + 17x2 + 40y2 + x, (19)

and x′ = y3 − y,

y′ = −8x3 − 3x2 + x, (20)

have H = 468x4 − 1344x2y2 − 96y4 + 34x3 + 240xy2 + 3x2 + 3y2

HILBERT NUMBERS USING REVERSIBLE CENTERS 17

and
 H = −8x4 − y4 − 4x3 + 2x2 + 2y2

as ﬁrst integrals, respectively.
Moreover, all the considered systems have diﬀerent phase portraits in the Poincar´e
disk. In Figure 2 we depict all of them. The ﬁnite equilibrium points are all of them
of center or saddle type, meanwhile at inﬁnity the equilibrium points, when they
exist, all are of node or saddle type.

Figure 2. The qualitative phase portraits of cubic systems (14), (17),
(18), (19), and (20), on the Poincar´e sphere.

Finally, we remark that system (20) belongs to the family studied in [18] where
13 limit cycles appear bifurcating simultaneously from diﬀerent period annulus.

5. Reversible quartic systems

Christopher, in [7], study the simultaneous bifurcation of limit cycles in conﬁg-
uration ⟨n, m, n⟩ for a quartic Darboux center given by ˙Zo l¸adek in [32]. Using the
method described in Section 3, up to ﬁrst order, i.e. calculating the linear parts of
the Lyapunov quantities, he provides 22 limit cycles in conﬁguration ⟨6, 10, 6⟩.
In this section we extend this study to some reversible quartic systems having
rational ﬁrst integrals, using linear and higher order developments of the Lyapunov
quantities. More concretely, let us consider rational ﬁrst integrals of the type

HN,d(x, y) = (y2 + pN,d−1(x))
d

(xy2 + qN,d(x))
d−1 . (21)

18 R. PROHENS AND J. TORREGROSA

The given polynomials pN,d−1 and qN,d are of degree d − 1 and d, respectively. The
corresponding diﬀerential system writes as

x′ = −∂HN,d
∂y VN,d(x, y),

y′ = ∂HN,d
∂x VN,d(x, y), (22)

for a suitable inverse integrating factor VN,d(x, y). All the reversible systems pre-
sented in this section are symmetric with respect to the x-axis having a center at
the origin and two more at (xc, ±yc). All of them are non degenerate.
In the ﬁrst subsection, using ﬁrst order of Lyapunov quantities and simultaneous
bifurcations, we obtain diﬀerent conﬁgurations with 16, 19, and 22 limit cycles,
increasing with d. The last one, H4,5, is in the same class as Christopher’s center
and we recover his result. In the second subsection, using ﬁfth order developments,
we get the new lower bound H(4) ≥ 28, in a simultaneous bifurcation and in a
⟨8, 12, 8⟩ conﬁguration. See Proposition 6. As in the cubic family studied in the
previous section, only the developments of odd order are useful for obtaining more
limit cycles.

5.1. Conﬁgurations found in the class H4,d. Next table shows the results on
simultaneous bifurcation of limit cycles for system (22), of degree four, and d =
3, 4, 5, using the linear parts of the Lyapunov quantities. In the second row we
indicate, at the top, the found conﬁguration and, at the bottom, the total number
of small limit cycles.
 H4,3 H4,4 H4,5
⟨4, 8, 4⟩ ⟨5, 9, 5⟩ ⟨6, 10, 6⟩
(16) (19) (22)

Because of the size of the expressions of the Lyapunov quantities and as we are
following exactly the procedure described in Section 3 we only list the polynomials
that deﬁne the rational ﬁrst integrals (21):

p4,2 (x) = −24961
24336 x2 + 2 x − 1,

q4,3 (x) = 84551
36504 x3 − 3 x2 + 3 x − 1,

p4,3 (x) = 2230433
473616 x3 + 259
198 x2 − 67
66 x − 1,

q4,4 (x) = 2230433
631488 x4 + 259
198 x3 + 50
33 x2 − 134
99 x − 1,

p4,4 (x) = −3
4 x4 + 2 x2 + 4
3 x + 4
3,

q4,5 (x) = −3
5 x5 + 2 x3 + 4
3 x2 + 2
3 x + 8
15.

A more detailed study of the last family is done in Proposition 6 below.
We point out that the number of limit cycles strictly increases, with d, in each
studied example. We have not shown the results done for higher d because they are
worse than those presented.

HILBERT NUMBERS USING REVERSIBLE CENTERS 19

5.2. Higher order studies for a quartic system. In Proposition 5 we have seen
how higher order developments of the Lyapunov quantities can be used to increase
the number of small limit cycles. In that case only from the center on the symmetry
line we can get more limit cycles, passing from the conﬁguration ⟨1, 5, 1⟩, with a
ﬁrst order study, to the conﬁguration ⟨1, 7, 1⟩, with a ﬁfth order development.
In this subsection, we get the new lower bound of H(4) ≥ 28 by proceeding in a
similar manner to the previously exposed. Due to the diﬃculties on the computa-
tions we have only check how the number of limit cycles increases for a system of
degree four which is of type H4,5. As we have mentioned above, we have selected a
Darboux center which is in the same class as the one studied by Christopher.

Proposition 6. The quartic diﬀerential system associated to the rational ﬁrst inte-
gral
 H(x, y) = (2x4 − x2 + y2 − 2x − 2)
5

(8x5 − 5x3 + 5xy2 − 10x2 − 5x − 4)4 (23)

has one reversible center at the origin and two more centers at the points (1, ±2).
Perturbing with polynomials of degree four, from these centers bifurcate 22, 27, and
28 limit cycles in conﬁguration ⟨6, 10, 6⟩, ⟨8, 11, 8⟩, and ⟨8, 12, 8⟩, using the series
expansion of the Lyapunov quantities on the perturbation coeﬃcients up to order 1,
3, and 5, respectively.

Proof. It is easy to check that the reversible diﬀerential equation associated to the
rational ﬁrst integral (23) has a center at (0, 0), on the symmetry axis which is the
straight line {y = 0}, and two more symmetric centers at (1, ±2).
The limit cycles appear via a simultaneous degenerate Hopf bifurcation, following
the procedure described in Section 3. More concretely, let us denote by ˜L(ℓ)
j and ˆL
(ℓ)
j
the Taylor series expansion of order ℓ of the j Lyapunov quantities at the equilibrium
points obtained perturbing the diﬀerential equation, i.e. near the centers at (0, 0)
and (1, ±2), respectively. We notice that, by the symmetric perturbation procedure,
the j Lyapunov quantities at (1, 2) and (1, −2) coincide.
We will follow the same scheme described in the proof of Proposition 5.
Straightforward computations provide, after some linear changes in the param-
eters space, the ﬁrst Lyapunov quantities up to order 1. We can write them as
˜L(1)
j = xj + O2(x), for j = 1, . . . , 10 and ˆL
(1)
j = yj + O2(y), for j = 1, . . . , 6. We
have denoted by O2(x) and O2(y) all the terms of degree two in variables xj and yj,
respectively. Moreover, we observe that ˜L
(1)
11 , ˜L(1)
12 , ˆL
(1)
7 , and ˆL
(1)
8 are linear combina-
tions of the ﬁrst ten and six Lyapunov quantities up to order 1, respectively. From
these expressions, adding the perturbation parameters that control the traces at the
critical points after the perturbation, we get the same conﬁguration of limit cycles,
⟨6, 10, 6⟩, given by Christopher in [7]. For obtaining more limit cycles, before using
the “trace parameters”, we need to compute the Taylor series expansion of higher
order of the next Lyapunov quantities, ˜Lj, for j = 11, 12, and ˆLj, for j = 7, 8.
The second order terms in the Taylor developments of the Lyapunov quantities
are zero when the parameters that control ﬁrst order developments vanish, i.e. when
x1 = · · · = x10 = y1 = · · · = y6 = 0. Then, third order of Taylor developments of the
Lyapunov quantities are necessary to be computed so that more limit cycles could

20 R. PROHENS AND J. TORREGROSA

be obtained. If we compute them, we obtain the expressions

˜L
(3)
11 = C1x11x2
12 p2(x11/x12),

˜L
(3)
12 = C2x11x2
12 p2(x11/x12),

ˆL
(3)
7 = C3y3
8 p3(y7/y8),

ˆL
(3)
8 = C4y3
8 ˆp3(y7/y8),

for some constants C1, C2, C3, and C4 and polynomials

p2(λ) =7837649339589516 + 3741225987316λ + 431335779λ
2,

p3(λ) =20932383446945199488077206112653
+ 42671630228676522212733338314426λ

+ 27681018968522683495059877708953λ
2

+ 5653958549111204034021495620096λ
3

ˆp3(λ) =46246307507579267760260412353597030559
+ 94264434217259234279967744936711259963λ

+ 61137236767015531358857109782475722749λ
2

+ 12482954391842688462988145099794265513λ
3.

We want to remark that we have four functions but only three polynomials. From
previous expressions, we only have, up to order three, one extra limit cycle surround-
ing the origin. This is so because ˜L(3)
11 is diﬀerent from zero and the polynomial p2
appears in the two expressions ˜L(3)
11 and ˜L
(3)
12 . Surrounding each one of the critical
points (1, ±2) we have two more limit cycles, because the polynomials p3 and ˆp3
are of degree three and they have no common zeros, as it follows from the fact that
the resultant of them is not zero. Consequently, up to order three, we have the
conﬁguration ⟨8, 11, 8⟩ of limit cycles.
Finally, the development up to order four of ˜L11 and ˜L12 coincides but not the
corresponding to order ﬁve and it writes as ˜L(5)
12 = C5x12p4(x11/x12) with

p4(λ) = 34144153 · · · 7015797λ
4 + 64857960 · · · 8874396λ
3

+ 45819614 · · · 9678048λ2 + 14251184 · · · 3436944λ + 16440049 · · · 2184112.

We have not written completely the above polynomial of degree four, because each
coeﬃcient is an integer number with more than 200 ﬁgures.
Moreover, the resultant of the polynomials p3 and p4 is non zero, then the existence
of an extra hyperbolic limit cycle is guaranteed. Consequently, we get, at least,
twenty-eight small limit cycles in conﬁguration ⟨8, 12, 8⟩. This ﬁnishes the proof. □

We have not computed higher order Lyapunov quantities to ﬁnd more limit cycles
because to get the maximum, 28 limit cycles, we have exhausted all the perturbation
parameters. To get more limit cycles, if they exist, other mechanisms should be
applied.
 6. Simultaneous bifurcation of higher degree systems

This section is devoted to the perturbation of vector ﬁeld (22), for degrees N =
5, . . . , 9. Here we provide the new best lower bounds H(5) ≥ 37 and H(6) ≥ 53,

HILBERT NUMBERS USING REVERSIBLE CENTERS 21

among others lower bounds. To reach them we use linear developments of Lyapunov
quantities, following the way introduced in the previous sections; that is, by the
simultaneous bifurcation of limit cycles in diﬀerential systems having the rational
ﬁrst integrals (21).
In the next subsections we only provide the polynomials pN,d−1 and qN,d, all with
rational coeﬃcients, and the number of simultaneous limit cycles in conﬁguration
⟨n, m, n⟩ for degrees N = 5, . . . , 9. Due to the size of the expressions we have only
listed the systems and the conﬁgurations. As it can be seen, for every degree N,
the sequence of the number of limit cycles in each conﬁguration is increasing with
d, up to the maximal value obtained for d = 2N − 3. We have not shown the
conﬁgurations for greater values of d because the total number of limit cycles is less
than the previous maximal value. Moreover, when we increase the degree N we get
better results in next sections using other type of systems. These are the reasons
why we stop the computations at these values.
All the systems are chosen so that the involved rational numbers be as small as
possible. We observe that the method described in Section 3 needs a normal form
transformation where the square root of the determinant of the Jacobian matrix at
the equilibrium points appears in the computations. In most of the cases, we achieve
that the determinant of the Jacobian matrix at the equilibrium points be a perfect
square. This fact simpliﬁes signiﬁcantly the involved calculations. Alternatively,
when a square root of an integer number appears we look for a system that has this
number as small as possible.
For the sake of brevity, we omit all the computations because of their size and
since they are similar to the ones shown in the previous sections.

6.1. Conﬁgurations found in the class H5,d. Next table shows the results on si-
multaneous bifurcation of limit cycles for system (22) of degree ﬁve, and d = 4, 5, 6, 7.
The total number of limit cycles obtained for each system is given in parentheses.
H5,4 H5,5 H5,6 H5,7
⟨8, 12, 8⟩ ⟨9, 13, 9⟩ ⟨10, 14, 10⟩ ⟨11, 15, 11⟩
(28) (31) (34) (37)
As in the previous degree four case, the sequences of the number of limit cycles in
each period annulus also is strictly increasing. Here the polynomials deﬁning the
rational ﬁrst integrals (21) are:

p5,3(x) = 1431
286 x3 − 1,

q5,4(x) = 27617
6864 x4 + 23
24 x3 + 1
48 x2 − 1,

p5,4(x) = 316801
7040 x4 − 96
5 x2 − 104
5 x − 1,

q5,5(x) = 316801
8800 x5 − 96
5 x3 + 71
5 x2 − 26 x − 1,

p5,5(x) = −512
205 x5 + 8 x3 − 3 x2 + 15
8 x − 1,

q5,6(x) = −256
123 x6 + 8 x4 − 3 x3 − 11
16 x2 + 9
4 x − 1,

p5,6(x) = 961
686 x6 + 31
7 x3 − 31
42 x2 + 1
7 x − 1,

22 R. PROHENS AND J. TORREGROSA

q5,7(x) = 2883
2401 x7 + 31
7 x4 − 31
42 x3 + 1
7 x2 + 1
6 x − 1.

6.2. Conﬁgurations found in the class H6,d. Next table shows the results on
simultaneous bifurcation of limit cycles for system (22) of degree six, and d =
6, 7, 8, 9. As in the previous case, the total number of limit cycles obtained for each
system is also given in parentheses.
H6,6 H6,7 H6,8 H6,9
⟨13, 18, 13⟩ ⟨14, 19, 14⟩ ⟨15, 21, 15⟩ ⟨16, 21, 16⟩
(44) (47) (51) (53)
In the above sequences we observe that not all of them are strictly increasing in each
period annulus. Here the polynomials deﬁning the rational ﬁrst integrals (21) are:

p6,5(x) = −6
5 x5 − 54 x4 + 243 x3 − 5103 x2 + 2510 x − 1,

q6,6(x) = −x6 − 54 x5 − 9921
2 x2 + 3012 x − 1,

p6,6(x) = −1232
577 x6 + 1232
577 x4 − 3152
577 x3 + 1822
577 x2 + 1232
577 x + 1232
577 ,

q6,7(x) = −1056
577 x7 + 1232
577 x5 − 3152
577 x4 + 5158
1731 x3 + 5272
1731 x2 + 1294
1731 x + 2588
4039,

p6,7(x) = 13
7 x7 + 4 x4 + 2 x3 − 261
104 x2 − 35
104 x − 1,

q6,8(x) = 13
8 x8 + 4 x5 + 2 x4 − 261
104 x3 + 29
104 x2 − 5
13 x − 1,

p6,8(x) = 25
8 x8 + 10 x4 − 40
9 x3 − 32
9 x2,

q6,9(x) = 25
9 x9 + 10 x5 − 40
9 x4 − 32
9 x3 + 2 x − 16
9 .

6.3. Conﬁgurations found in the class H7,d. Next table shows the results on
simultaneous bifurcation, and total number in parentheses, of limit cycles for sys-
tem (22) of degree seven, and d = 8, 9, 10, 11.
H7,8 H7,9 H7,10 H7,11
⟨19, 25, 19⟩ ⟨20, 25, 20⟩ ⟨21, 26, 21⟩ ⟨22, 27, 22⟩
(63) (65) (68) (71)
Besides the above sequences are increasing but not strictly, they are less than ex-
pected values comparing with the previous degrees. This fact could be indicate that,
for higher values of N , the proposed rational ﬁrst integral (21) will not allow us to
improve our results. Here the polynomials p7,d−1, q7,d in (21) are:

p7,7(x) = 32
7 x7 − 8 x5 + 10 x3 + 10 x2 − 16 x + 32
7 ,

q7,8(x) = 4 x8 − 8 x6 + 11 x4 + 10 x3 − 18 x2 + 8 x − 2,

p7,8(x) = −9
4 x8 − 2 x5 + 12 x4 − 3 x3 − 16
3 x2 + 13
3 ,

q7,9(x) = −2 x9 − 2 x6 + 12 x5 − 3 x4 − 49
9 x3 + 4
3 x2 + 26
9 ,

p7,9(x) = −10
9 x9 + 4 x5 − 2 x4 − 3
10 x3 + 151
90 x2 + 16
9 x − 16
45,

HILBERT NUMBERS USING REVERSIBLE CENTERS 23

q7,10(x) = −x10 + 4 x6 − 2 x5 − 3
10 x4 + 151
90 x3 + 44
45 x2 + 4
9 x − 2
25,

p7,10(x) = −5
8 x10 − 5
2 x5 + 25
22 x4 + 125
484 x3 − 3337
484 x2 + 10 x + 5
2,

q7,11(x) = −25
44 x11 − 5
2 x6 + 25
22 x5 + 125
484 x4 − 3337
484 x3 + 10 x2 + 2 x + 5
11.

6.4. Conﬁgurations found in the classes H8,13 and H9,15. Next table shows the
results on simultaneous bifurcation of limit cycles for system (22), for degree N = 8
and d = 13, and degree N = 9 and d = 15. The total number of limit cycles obtained
for each system is given in parentheses.
H8,13 H9,15
⟨28, 34, 28⟩ ⟨35, 41, 35⟩
(8, 90) (9, 111)
Here the polynomials deﬁning the rational ﬁrst integrals (21) are:

p8,12 (x) = 13
2 x12 + 13 x6 − 6 x5 − 18
13 x4 − 108
169 x3 − 2305
2028 x2 + 1
13 x − 1,

q8,13 (x) = 6 x13 + 13 x7 − 6 x6 − 18
13 x5 − 108
169 x4 − 2305
2028 x3 + 1
13 x2 + 1
12 x − 1,

p9,14 (x) = −583200
34969 x14 + 16200
187 x7 − 7560
187 x6 − 1764
187 x5 − 4116 x4

935 − 2401
935 x3

− 109
5 x2 + 26 x − 195
14 ,

q9,15 (x) = −544320
34969 x15 + 16200
187 x8 − 7560
187 x7 − 1764
187 x6 − 4116
935 x5 − 2401
935 x4

− 109
5 x3 + 26 x2 − 30 x + 15.

For these degrees we only consider the highest value d = 2N −3 because looking at
the sequences of degrees 6 and 7 and comparing with degrees 4 and 5, the observed
values for the number of limit cycles are less than the expected ones. In next section
we present better results for systems with these degrees.

7. Systems having an algebraic curve of equilibria

In this section, we consider the system (22) adding curves of equilibrium points.
Of course, the ﬁrst integrals are the same but the degree is increased. We will see
that, for some degrees, this approach provides better Hilbert numbers than the ones
obtained in the previous section. The degrees considered are N = 5, . . . , 10. More
concretely, we consider the unperturbed system

x′ = −∂HN,d
∂y VN,d(x, y)FM (x, y),

y′ = ∂HN,d
∂x VN,d(x, y)FM (x, y), (24)

where HN,d is deﬁned in (21), VN,d is a given polynomial and the polynomials FM ,
for M = 1, 2, 3, 4, are

F1(x, y) = 1 − 2 x, F3(x, y) = 1 − 2 x − 2 xy2,

F2(x, y) = 1 − 2 x − 2 y2, F4(x, y) = 1 − 2 x − 2 xy2 − 3 x2y2.

24 R. PROHENS AND J. TORREGROSA

In this section we provide the new best lower bounds: H(7) ≥ 74, H(8) ≥ 96,
H(9) ≥ 120, and H(10) ≥ 142.
The number and conﬁgurations of limit cycles obtained, using the bifurcation
mechanism described in Section 3, are given in the next table. We remark that, as
in the previous section, we get the Lyapunov quantities only up to ﬁrst order.

F1 F2 F3 F4
H4,5 ⟨6, 10, 6⟩ ⟨10, 15, 10⟩ ⟨16, 21, 16⟩ ⟨22, 27, 22⟩ ⟨28, 34, 28⟩
(4, 22) (5, 35) (6, 53) (7, 71) (8, 90)
H5,7 ⟨11, 15, 11⟩ ⟨15, 21, 15⟩ ⟨23, 28, 23⟩ ⟨29, 35, 29⟩ ⟨36, 41, 36⟩
(5, 37) (6, 51) (7, 74) (8, 93) (9, 113)
H6,9 ⟨16, 21, 16⟩ ⟨21, 28, 21⟩ ⟨30, 36, 30⟩ ⟨37, 43, 37⟩ ⟨45, 52, 45⟩
(6, 53) (7, 70) (8, 96) (9, 117) (10, 142)
H7,11 ⟨22, 27, 22⟩ ⟨28, 35, 28⟩ ⟨38, 44, 38⟩ ⟨45, 52, 45⟩
(7, 71) (8, 91) (9, 120) (10, 142)

The ﬁrst column shows the results obtained in the previous section. The rest of the
columns display the results obtained for system (24), according FM . In each cell
of the table we have indicated the limit cycles conﬁguration (at the top) and the
degree of the system and the total number of small limit cycles (at the bottom in
parentheses).

For every degree N, we observe that, in almost all cases, the biggest values of
the lower bounds for the Hilbert numbers have been obtained perturbing a good
Darboux system giving a vector ﬁeld of degree N, instead of choosing other Darboux
systems with lower degree multiplied by a line of equilibria. This is the case for
degree 5 and 6.

8. Lower bounds for the Hilbert numbers using double symmetry

This section is devoted to prove Corollary 2. Its proof follows part of the approach
introduced in [8] to get an asymptotic lower bound of the form H(N ) > C N 2 log N,
for some constant C. Even though there are lower bounds that asymptotically behave
like this one, and that we do not improve, they do not give better results for small
values of N , see for instance [14].
Let us consider a polynomial system with c limit cycles. It is not restrictive to
assume that all of them are located at the ﬁrst quadrant, by performing a translation
if necessary. Assuming that the polynomial degree N diﬀerential system, (x′, y′) =
(f (x, y), g(x, y)), satisﬁes these hypotheses, the change of variables (u, v) = (x2, y2)
transforms this system to another one of degree 2N + 1 with 4c limit cycles. Using
this method for N = 2, 3, 4 we get the values H(5) ≥ 16, H(7) ≥ 52, and H(9) ≥ 112.
These lower bounds are smaller than the ones obtained in the previous sections, in
conﬁguration ⟨n, m, n⟩. Nevertheless, using this algorithm in a recursive way from
the new lower bounds given in Theorem 1, we can easily improve some known
results on the Hilbert numbers. Using the new values for N = 6, 7, 8, 9, 10, we
get H(13) ≥ 212, H(15) ≥ 296, H(17) ≥ 384, H(19) ≥ 480, and H(21) ≥ 568,
in a ﬁrst step, and H(27) ≥ 848, H(31) ≥ 1184, H(35) ≥ 1536, H(39) ≥ 1920,
and H(43) ≥ 2272, in a second step. But not all these values provide better lower
bounds, comparing with the results in [14]. The new ones are the detailed in the
ﬁrst statement of the corollary.

HILBERT NUMBERS USING REVERSIBLE CENTERS 25

Following the algorithm explained above, in a recursive way, Gasull, in [10], pro-
vides a lower bound for the Hilbert number of the form H(N ) > KN N 2, where KN =
cN /(N 2 + 1)2 and cN is the number of limit cycles of the starting system. Hence, the
second statement of the corollary follows using the results presented in this work for
N = 2, . . . , 10. We remark that for every cN in 4, 13, 28, 37, 53, 74, 96, 120, 142, the
corresponding KN value is

4
9, 13
16, 28
25, 37
36, 53
49, 37
32, 32
27, 6
5, 142
121,

being 6/5 the biggest one.
 9. Acknowledgements

This work has been realized thanks to the MINECO grants MTM2013-40998-P,
MTM2014-54275-P, MTM2016-77278-P (FEDER), and UNAB13-4E-1604 (FEDER),
and the AGAUR grant 2014 SGR568,

References

[1] A. A. Andronov, E. A. Leontovich, I. I. Gordon, and A. G. Maier. Theory of bifurcations of
dynamic systems on a plane. Halsted Press [A division of John Wiley & Sons], New York-
Toronto, Ont.; Israel Program for Scientiﬁc Translations, Jerusalem-London, 1973. Translated
from the Russian.
[2] N. N. Bautin. On the number of limit cycles appearing with variation of the coeﬃcients from
an equilibrium state of the type of a focus or a center. Mat. Sbornik N.S., 30(72):181–196,
1952.
[3] T. R. Blows and N. G. Lloyd. The number of limit cycles of certain polynomial diﬀeren-
tial equations. Proceedings of the Royal Society of Edinburgh: Section A Mathematics, 98(3-
4):215239, 1984.
[4] Y. L. Bondar′ and A. P. Sadovski˘ı. On a theorem of ˙Zo l ‘
adek. Diﬀer. Uravn., 44(2):263–265,
287, 2008.
[5] L. Chen and M. Wang. The relative position and number of limit cycles of the quadratic
diﬀerential system. Acta Math. Sin., 22:751–758, 1979.
[6] C. Chicone and M. Jacobs. Bifurcation of limit cycles from quadratic isochrones. J. Diﬀerential
Equations, 91(2):268–326, 1991.
[7] C. Christopher. Estimating limit cycle bifurcations from centers. In Diﬀerential equations with
symbolic computation, Trends Math., pages 23–35. Birkh¨auser, Basel, 2005.
[8] C. J. Christopher and N. G. Lloyd. Polynomial systems: a lower bound for the Hilbert num-
bers. Proc. Roy. Soc. London Ser. A, 450(1938):219–224, 1995.
[9] F. Dumortier, J. Llibre, and J. C. Art´es. Qualitative theory of planar diﬀerential systems.
Universitext. Springer-Verlag, Berlin, 2006.
[10] A. Gasull. From Abel’s diﬀerential equations to Hilbert’s sixteenth problem. Butl. Soc. Cata-
lana Mat., 28(2):123–146, 233, 2013.
[11] J. Gin´e. Higher order limit cycle bifurcations from non-degenerate centers. Appl. Math. Com-
put., 218(17):8853–8860, 2012.
[12] M. Han. Liapunov constants and Hopf cyclicity of Lienard systems. Ann. of Diﬀ. Eqs,
15(2):113–126, 1999.
[13] M. Han. Bifurcation Theory of Limit Cycles. Alpha Science International Limited, 2016.
[14] M. Han and J. Li. Lower bounds for the Hilbert number of polynomial systems. J. Diﬀerential
Equations, 252(4):3278–3304, 2012.
[15] T. Johnson. A quartic system with twenty-six limit cycles. Exp. Math., 20(3):323–328, 2011.
[16] T. Johnson and W. Tucker. An improved lower bound on the number of limit cycles bifurcating
from a Hamiltonian planar vector ﬁeld of degree 7. Internat. J. Bifur. Chaos Appl. Sci. Engrg.,
20(5):1451–1458, 2010.

26 R. PROHENS AND J. TORREGROSA

[17] T. Johnson and W. Tucker. An improved lower bound on the number of limit cycles bifurcating
from a quintic Hamiltonian planar vector ﬁeld under quintic perturbation. Internat. J. Bifur.
Chaos Appl. Sci. Engrg., 20(1):63–70, 2010.
[18] C. Li, C. Liu, and J. Yang. A cubic system with thirteen limit cycles. J. Diﬀerential Equations,
246(9):3609–3619, 2009.
[19] J. Li and Y. Liu. New results on the study of Zq-equivariant planar polynomial vector ﬁelds.
Qual. Theory Dyn. Syst., 9(1-2):167–219, 2010.
[20] H. Liang and J. Torregrosa. Parallelization of the Lyapunov constants and cyclicity for centers
of planar polynomial vector ﬁelds. J. Diﬀerential Equations, 259(11):6494–6509, 2015.
[21] P. Mardesic. An explicit bound for the multiplicity of zeros of generic abelian integrals. Non-
linearity, 4(3):845, 1991.
[22] H. Movasati. Center conditions: rigidity of logarithmic diﬀerential equations. Journal of Dif-
ferential Equations, 197(1):197–217, 2004.
[23] R. Roussarie. Bifurcation of planar vector ﬁelds and Hilbert’s sixteenth problem, volume 164
of Progress in Mathematics. Birkh¨auser Verlag, Basel, 1998.
[24] S. L. Shi. A method of constructing cycles without contact around a weak focus. J. Diﬀerential
Equations, 41(3):301–312, 1981.
[25] X. Sun and M. Han. On the number of limit cycles of a Z4-equivariant quintic near-Hamiltonian
system. Acta Math. Sin. (Engl. Ser.), 31(11):1805–1824, 2015.
[26] S. Wang and P. Yu. Bifurcation of limit cycles in a quintic Hamiltonian system under a
sixth-order perturbation. Chaos Solitons Fractals, 26(5):1317–1335, 2005.
[27] S. Wang and P. Yu. Existence of 121 limit cycles in a perturbed planar polynomial Hamiltonian
vector ﬁeld of degree 11. Chaos Solitons Fractals, 30(3):606–621, 2006.
[28] Y. Wu, Y. Gao, and M. Han. On the number and distributions of limit cycles in a quintic
planar vector ﬁeld. International Journal of Bifurcation and Chaos, 18(07):1939–1955, 2008.
[29] Y. H. Wu, X. D. Wang, and L. X. Tian. Bifurcations of limit cycles in a Z4-equivariant quintic
planar vector ﬁeld. Acta Mathematica Sinica, English Series, 26(4):779–798, Apr 2010.
[30] Y. Q. Ye, S. L. Cai, L. S. Chen, K. C. Huang, D. J. Luo, Z. E. Ma, E. N. Wang, M. S.
Wang, and X. A. Yang. Theory of limit cycles, volume 66 of Translations of Mathematical
Monographs. American Mathematical Society, Providence, RI, second edition, 1986.
[31] H. ˙Zo l ‘
adek. Eleven small limit cycles in a cubic vector ﬁeld. Nonlinearity, 8(5):843–860, 1995.
[32] H. ˙Zo l ‘
adek. Remarks on “The classiﬁcation of reversible cubic systems with center”. Topol.
Methods Nonlinear Anal., 8(2):335–342, 1996.
[33] H. ˙Zo l ‘
adek. The CD45 case revisited. In Mathematical sciences with multidisciplinary applica-
tions: in honor of professor Christiane Rousseau. And in recognition of the mathematics for
planet earth initiative, pages 595–625, Cham, 2016. Springer International Publishing.

Dept. de Matem`atiques i Inform`atica, Escola Polit`ecnica Superior, Universitat
de les Illes Balears. 07122, Palma de Mallorca. Spain
E-mail address: rafel.prohens@uib.cat

Dept. de Matem`atiques, Universitat Aut`onoma de Barcelona, Edifici C. 08193
Bellaterra, Barcelona. Spain
E-mail address: torre@mat.uab.cat
