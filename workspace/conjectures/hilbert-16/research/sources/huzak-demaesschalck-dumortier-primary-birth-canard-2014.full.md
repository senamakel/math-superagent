<!-- source: https://documentserver.uhasselt.be/bitstream/1942/17161/1/pdfs.pdf | converted from PDF -->

COMMUNICATIONS ON doi:10.3934/cpaa.2014.13.2641
PURE AND APPLIED ANALYSIS
Volume 13, Number 6, November 2014 pp. 2641–2673

PRIMARY BIRTH OF CANARD CYCLES IN SLOW-FAST
CODIMENSION 3 ELLIPTIC BIFURCATIONS

Renato Huzak, Peter De Maesschalck and Freddy Dumortier

Hasselt University, Campus Diepenbeek, Agoralaan Gebouw D
3590 Diepenbeek, Belgium

(Communicated by Xingfu Zou)

Abstract. In this paper we continue the study of “large” small-amplitude
limit cycles in slow-fast codimension 3 elliptic bifurcations which is initiated in
[8]. Our treatment is based on blow-up and good normal forms.

1. Introduction. This paper deals with the canard phenomenon and correspond-
ing limit cycles of canard type, as they appear in slow-fast families of vector ﬁelds in
the (x, y)-plane. The prototypical example where the canard phenomenon appears
is the Van der Pol system, where the unique singular point of a speciﬁc slow-fast
structured vector ﬁeld undergoes a Hopf bifurcation upon variation of a control pa-
rameter. Letting ϵ denote the singular parameter separating the two time scales in
the Van der Pol system, a weighted rescaling of (x, y, ϵ) exposes a rescaled system
of diﬀerential equations in rescaled variables (X, Y ), where the slow-fast structure
has disappeared and where a traditional Hopf bifurcation is observed. The periodic
orbit(s) seen in the (X, Y )-space are considered small-amplitude limit cycles in the
traditional (x, y)-plane, since they typically are contained in an O(ϵ)-neighbourhood
of the Hopf point. Traditional techniques from dynamical systems and bifurcation
theory can be used to deal with those small-amplitude limit cycles. Besides these
cycles, the (x, y)-plane may also contain so-called slow-fast cycles of canard type,
with properties typically associated to slow-fast systems. It is precisely at the in-
terface between small-amplitude cycles and canard cycles that a delicate analysis
is needed. Those families of cycles are unbounded in (X, Y )-space and yet close
to the origin in (x, y)-coordinates. Pioneering work has been done in [12] (in a
codimension 1 scenario) and in [2] for systems that are locally similar to the Van
der Pol system in higher codimension.
In [2], the way the interface between small-amplitude cycles and canard cycles is
examined is by blowing up the origin. The traditional rescaling from above is seen
in one of the charts of the blow-up construction. In the blow-up construction, one
can also examine other charts, the so-called phase directional rescaling charts. It
is precisely those charts that become important in a study of the birth of canard
cycles. We remind the reader that in most papers on slow-fast systems using blow-
up, the phase directional rescaling charts are only studied minimally, just enabling
the contributing authors to trace orbits passing through these charts and to focus

2000 Mathematics Subject Classiﬁcation. Primary: 34E15, 37G15, 34E20, 34C23, 34C26.
Key words and phrases. Blow-up, center manifold, cyclicity, singular perturbations, normal
form.
 2641

2642 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

attention to the traditional rescaling charts. Indeed, only a few properties are
needed of these phase directional rescaling charts to examine large amplitude canard
cycles, the so-called detectable cycles, see also [10].
Here, we also study the birth of canard cycles, i.e. cycles at the interface between
small-amplitude cycles and canard cycles, but in a more degenerate context: while
the underlying bifurcation mechanism in the Van der Pol equation is a codimension 1
Hopf bifurcation, we now consider a codimension 3 singularity in a slow-fast context.
The essential extra diﬃculty is that besides the singular parameter ϵ, we now have 3
extra parameters unfolding the codimension 3 singularity, and even without a slow-
fast structure, a blow-up is needed to give a complete study. As can be expected,
we present a study where two blow-up constructions are combined: one to unfold
the codimension 3 singularity (a “primary blow-up”), and one to dissolve the slow-
fast structure (a “secondary blow-up”). Cycles that are bounded in coordinates
after the secondary blow-up could be called small-amplitude cycles. As they grow
in size under inﬂuence of some perturbation parameter, they meet the boundary
of the secondary blow-up and give birth to intermediary-sized cycles: those cycles
are of size O(1) in coordinates after the primary blow-up. This birth of canard
cycles is largely similar to the one treated in [2]. In primary blow-up coordinates,
the intermediary-sized cycles are already of canard type, but may continue growing
until they meet the boundary of the primary blow-up and give birth to canard cycles
of size O(1) in original coordinates. This birth process actually diﬀers more than a
bit from the situation discussed in [2] and [12], and the study of limit cycles in this
situation is the topic of this paper.
One of the main properties of the primary blow-up is that it is not ϵ that is
included in the blow-up construction, since the primary blow-up does not involve
dissolving the slow-fast structure; instead, the primary blow-up is involved with
desingularizing a codimension 3 singularity. As a consequence, the family of vector
ﬁelds being blown up has a slow-fast structure both before and after blow-up.
Instead of presenting a general technique for treating a birth of canard situation
in case of a blow-up preserving the slow-fast structure, we choose to demonstrate
the (quite intricate) techniques in a situation for which a lot of results already have
been obtained:

• We study a slow-fast codimension 3 singularity that is the slow-fast variant of
a well-studied codimension 3 singularity (see [5]).
• The desingularization of the singularity using a primary and secondary blow-
up has been worked out before (see [8]). Both the detectable canard cycles
([3]) and the small-amplitude limit cycles ([8]) have been characterized before.
On top of that, the birth problem associated to the secondary blow-up has
been dealt with. (See [8].)

We claim that the results are general enough to be useful in other situations,
and furthermore the results contribute to a complete understanding of the slow-fast
codimension 3 singularities and nearby limit cycles.
In Section 2, we present a more detailed setting and introduce the setting using a
precise system of equations in mind. In Section 3, we carry out the desingularization
via blowing-ups. Section 4 contains precise statements of the results we aim to prove.
Section 5 ﬁnally contains detailed proofs of the results.
The technique of blow-up is crucial in this paper, not only in proving the results,
but already in stating the results. We therefore refer the interested reader to [13]
for more informations about desingularizations of nilpotent singularities in families

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2643

of planar vector ﬁelds, and continue under the assumption that reader has suﬃcient
background.

2. Slow-fast codimension 3 elliptic bifurcations. We deal with the slow-fast
family of planar systems

X¯ϵ,b,λ :
 { ˙x = y

˙y = −xy + ¯ϵ(b0 + b1x + b2x2 − x3 + x4 ¯H(x, λ) + y2G(x, y, λ)
), (1)

where G and ¯H are smooth, ¯ϵ ≥ 0 is the singular parameter that is kept small,
b = (b0, b1, b2) are regular perturbation parameters close to 0 and λ ∈ Λ, with Λ
a compact subset of some euclidean space. The family X¯ϵ,b,λ represents slow-fast
codimension 3 elliptic bifurcations, in analogy with the terminology introduced in
[5] and [8].
Let us recall that [5] is devoted to the study of generic bifurcations of three-
parameter families of planar vector ﬁelds around singular points whose linear parts
are nilpotent. The authors dealt with three categories: the saddle case, the elliptic
case and the focus case. Dealing with slow-fast systems (¯ϵ ∼ 0, ¯ϵ > 0), in [8]
we distinguish only between the elliptic case (1) and the saddle case, obtained by
putting the +-sign in front of x3 in (1). The focus case is possible in the family (1)
if the parameter ¯ϵ > 0 is suﬃciently large, but then (1) is not of slow-fast type. For
more details we refer to [8].
The family X¯ϵ,b,λ contains for ¯ϵ = 0 a curve of singular points given by {y = 0}.
All points on the curve except for the origin are normally hyperbolic. Of course,
the dynamics for ¯ϵ = 0 can be studied by canceling the common factor y and seeing
that orbits of X0,b,λ take the form y = y(x), with dy
dx = −x. In other words, orbits
lie on parabolas that intersect the curve of singular points transversally, except at
the origin, where the parabola has a second-order contact with the curve (see Figure
1). The origin (x, y) = (0, 0) is a so-called contact point, and we observe that it is
of nilpotent type.
 Figure 1. The dynamics of X0,b,λ.

The ¯ϵ-perturbation may cause the curve y = 0 to perturb into some invariant
curve with a dynamics on it, but with a speed that is O(¯ϵ). This way, so-called
detectable canard limit cycles may appear: a fast movement along the top of a
parabola above {y = 0} is followed by a slow movement connecting the two ends of
the parabola along y = 0.
As mentioned above the papers [8] and [3] are devoted to the study of the limit
cycles that may appear in the family X¯ϵ,b,λ perturbing from X0,(0,0,0),λ. The paper
[3] deals with systems (1) but emphasizes passage near the generic turning point

2644 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

(x, y) = (0, 0) in order to study the detectable canard limit cycles, whereas in the
paper [8] the focus is on small amplitude limit cycles near (x, y) = (0, 0).
Let us ﬁrst explain what is our goal of the present paper. We reparametrize the
b-parameters, by introducing weighted spherical parameters as used in [8]:

(b0, b1, b2) = (r3 ¯B0, r2B1, rB2), r ≥ 0, B = ( ¯B0, B1, B2) ∈ S
2.

We obtain an (¯ϵ, B, r, λ)-family of vector ﬁelds in R2:
{ ˙x = y

˙y = −xy + ¯ϵ(r3 ¯B0 + r2B1x + rB2x2 − x3 + x4 ¯H(x, λ) + y2G(x, y, λ)). (2)

For r = 0, system (2) has no limit cycles near (x, y) = (0, 0). For r ̸= 0, r ∼ 0,
system (2) has been studied in an (¯ϵ, B, λ)-uniform neighborhood of the origin in
(x, y)-space (see [2], at least in the Li´enard setting, i.e. G ≡ 0, and [1]). This local
study is valid in a small neighborhood of (x, y) = (0, 0) and the domain on which
the arguments of [2] and [1] can be applied shrinks to (x, y) = (0, 0) when r → 0.
The idea in [8] was to start the study of limit cycles of (2) in a neighborhood
of the origin (x, y) = (0, 0) that does not shrink to the origin when ¯ϵ → 0 and
r → 0. This means that the transition from small amplitude limit cycles to small
(but detectable) canard limit cycles has to be considered. The goal of the present
paper is to study this “birth of canards” in the (x, y) − plane, i.e. so-called “large”
small amplitude limit cycles.
As mentioned above, in [8] slow-fast codimension 3 saddle bifurcations have been
studied. In slow-fast codimension 3 saddle bifurcations, one ﬁnds no birth of canards
because detectable canard limit cycles are not present (see [8] and [3]).
Now we want to provide few details on what is shown in [8] and how the above
mentioned birth of canards comes into play. In [8], the best way we saw to study the
small limit cycles problem of (2) was by applying the so-called “primary” blow-up:

(x, y, r) = (u¯x, u
2 ¯y, u¯r), (3)

with ¯x2 + ¯y2 + ¯r2 = 1 and ¯r ≥ 0, u ≥ 0, u ∼ 0. We also divided the system we got by
u. The precise elaboration can be found in [8] or in Section 3. Roughly speaking this
blow-up transforms the r-family of quite “degenerate” two-dimensional problems (2)
into a less degenerate, but still ¯ϵ-singular, three-dimensional problem. Instead of
having to work in a r-uniform neighborhood of the origin, we now have to consider
a neighborhood inside {u ≥ 0} of the primary blow-up locus {(u, ¯x, ¯y, ¯r); u =
0, ¯x2 + ¯y2 + ¯r2 = 1, ¯r ≥ 0}.
As it is usual in working along a sphere it is preferable to work in diﬀerent charts.
He have the family chart “¯r = 1” and the phase-directional charts “¯x = ±1, ¯y =
±1”. The family chart is the traditional rescaling chart, and it amounts to making
a standard rescaling of the phase variables (x, y). The phase-directional charts link
the family chart to the original phase plane and we use them to study dynamics
of (2) near the “equator” {(u, ¯x, ¯y, ¯r); u = 0, ¯r = 0, ¯x2 + ¯y2 = 1} of the primary
blow-up locus.
In [8] we detected, depending on region in the B-space, all possible closed curves
(so-called limit periodic sets) on the (primary) blow-up locus which can produce
limit cycles of the blown-up vector ﬁeld for u¯r > 0 and ¯ϵ > 0, and we saw that a
birth of canards, near a limit periodic set with large parts on the “equator” of the
blow-up locus, is possible only for those values of B which are in the slow-fast Hopf
region: ¯B0 ∼ 0, B1 = −1 and B2 in an arbitrarily large compact interval. The

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2645

subject of this paper is a study of cyclicity of the limit periodic set near which the
birth of canards occurs. In the slow-fast Hopf region, some of the results from [8]
have been proved by using the cyclicity results that we will prove in this paper (see
Theorem 2.4, Theorem 2.5 and Section 3.8 in [8]).
Let us recall that, instead of using coordinates on S
2 (B ∈ S
2), we used diﬀerent
charts of the sphere (jump chart, slow-fast Bogdanov-Takens chart, slow-fast Hopf
chart, etc.) and we proved that, outside the slow-fast Hopf region (i.e. chart), sys-
tem (2) has at most one hyperbolic limit cycle, in an (¯ϵ, r, λ)-uniform neighborhood
of (x, y) = (0, 0). The size of this limit cycle goes to zero when r → 0 because the
essential parts of the study of this case have been done in the family chart “¯r = 1”;
for more details we refer to [8].
Here we point out that the proofs of all these results from [8] were based on
performing an extra blow-up at the origin (¯x, ¯y, ¯ϵ) = (0, 0, 0) which depends on
region in the B-space in which one looks. We called it “secondary” blow-up.
Being interested in the birth of canards, we consider (2) where B is in the slow-
fast Hopf region. We introduce the following rescaling:

(¯ϵ, ¯B0) = (ϵ2E, ϵB0), ϵ ≥ 0, ϵ ∼ 0, (E, B0) ∈ S
1, E ≥ 0.

The calculations will be performed, as usual, in charts. When E is in any compact
interval and B0 = ±1, then the system (2) has no small-amplitude limit cycles
(hence no birth of canards occurs); for details see [8]. When E = 1 and B0 ∼ 0,
then (2) changes into
{ ˙x = y

˙y = −xy + ϵ
2(ϵr3B0 − r2x + B2rx
2 − x3 + x4 ¯H(x, λ) + y2G(x, y, λ)
), (4)

where G and ¯H are smooth, ϵ > 0 is the singular parameter that is kept small,
r > 0 is a regular parameter that is kept small, B0 is a regular parameter close
to 0, B2 is a regular parameter in an arbitrary compact subset of R and λ ∈ Λ,
with Λ a compact subset of some euclidean space. If we introduce a new variable
Y = y + 1
2 x2, then (4) changes into

Xϵ,r,B0,B2,λ :
 



 ˙x = y − 1
2 x2

˙y = ϵ2(ϵr3B0 − r2x + B2rx
2 − x
3 + x4 ¯H(x, λ)

+(y − 1
2 x2)
2G(x, y − 1
2 x2, λ)
).
 (5)

where we denote Y again by y. We prefer to work in the so-called Li´enard plane.
We recall that when G = 0 and ¯H is polynomial, the given family (1) of
vector ﬁelds is of (generalized) polynomial Li´enard type of degree (1, n), where
n = deg ¯ϵ(...). The 1 in (1, n) comes from the degree of the polynomial in front of
y in ˙y. Determining the maximum number of limit cycles of a Li´enard type vector
ﬁeld of degree (m, n) is one of the major open problems in the ﬁeld of planar dy-
namics (see [14]), and [8], [3], [9] and this paper contribute to the extensive research
in this area, in the case n ≥ 4 and m = 1. We point out that there is a strong link
between results on slow-fast type Li´enard equations, as treated in this paper, and
general Li´enard equations, see [6] an [7].
As mentioned in the introduction, in Section 3 we study system (5) in the family
chart and in the phase-directional charts of the primary blow-up (3), and we detect
a limit periodic set on the blow-up locus near which a birth of canards occurs (see

2646 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

Figure 2). In [8], this limit periodic set was denoted by L00. In this paper, we
denote it by Γ. The fact that Γ is on the primary blow-up locus, with a part on the
“equator” of the primary blow-up locus, explains the title “Primary birth of canard
cycles ...” that we have chosen for this paper.
In Section 4 we deﬁne a diﬀerence map near Γ which enables us to introduce
the notion of cyclicity of Γ. Then we state the results about the cyclicity of Γ,
depending on the parameter B2. When B2 ̸= 0, then at most one limit cycle may
appear near Γ. When B2 ∼ 0, then the cyclicity of Γ depends on the higher order
terms in ¯H, in analogy with the results in [2]. If we suppose that ¯H(0, λ) ̸= 0 for
all λ ∈ Λ, then at most two limit cycles may come near Γ.
In Section 5, we give a detailed proof of all statements formulated in Section 4.
We use similar methods as in [2] to study the diﬀerence map near Γ; we exploit
symmetries that are present both in the system (5) and in the blow-up construction
(3), we use C k-normal forms (see [11]) near semi-hyperbolic singularities P +
0 and
P −
0 on Γ (see Figure 2), etc.

3. Blow-up construction and detection of Γ. If we add the equation ˙r = 0 to
(5), we obtain a τ = (ϵ, B0, B2, λ)-family of vector ﬁelds in R3:

Xτ := Xϵ,r,B0,B2,λ + 0 ∂
∂r .

As mentioned in the introduction, we consider the so-called primary blow-up map
(deﬁning a singular change of coordinates)

Θ : R+ × S
2 → R3 : (u, (¯x, ¯y, ¯r)) ↦→ (x, y, r) = (u¯x, u
2 ¯y, u¯r), ¯r ≥ 0.

The blown-up vector ﬁeld is deﬁned as the pullback of the original vector ﬁeld Xτ
divided by u:
 ¯Xτ := 1
u Θ∗Xτ . (6)

In order to detect Γ for ϵ = u = B0 = 0, we have to study the blown-up vector
ﬁeld ¯Xτ near the blow-up locus {0} × S
2
+, in the family chart “¯r = 1” (see Section
3.1) and in the phase-directional chart “¯y = 1” (see Section 3.2). (We denote
by S
2
+ the half-sphere in (¯x, ¯y, ¯r)-space with ¯r ≥ 0.) The phase-directional charts
“¯x = ±1, ¯y = −1” are not relevant when studying the limit periodic set Γ.

3.1. Family chart “¯r = 1”. We use the following family rescaling of (5):

(x, y, r) = (u¯x, u
2 ¯y, u), (7)

with (¯x, ¯y) in an arbitrarily large disk in R2 and u = r ≥ 0. The blown-up ﬁeld is
a τ -family of 3-dimensional vector ﬁelds (after division by the positive factor r):

X (1)
τ :
 



 ˙¯x = ¯y − 1
2 ¯x2

˙¯y = ϵ2(ϵB0 − ¯x + B2 ¯x2 − ¯x3 + r¯x4 ¯H(r¯x, λ)

+r(¯y − 1
2 ¯x2)2G(r¯x, r2(¯y − 1
2 ¯x2), λ)
)

˙r = 0.
 (8)

The vector ﬁeld X (1)
τ represents a singular perturbation problem with ϵ as sin-
gular parameter. If we treat X (1)
τ as a (τ, r)-family of 2-dimensional vector ﬁelds, it
can be easily seen that X (1)
τ for ϵ = 0 has a curve of singularities (a critical curve)

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2647

given by {¯y − 1
2 ¯x2 = 0}. The critical curve consists of partially hyperbolic singular-
ities, except at the origin (¯x, ¯y) = (0, 0), where we deal with a nilpotent singularity
(so-called turning point). We see that the curve is normally attracting when ¯x > 0
and normally repelling when ¯x < 0.
The ϵ-perturbation may cause the curve {¯y − 1
2 ¯x2 = 0} to perturb to some
invariant curve which follows the attracting part of the critical curve until it reaches
the section {¯x = 0} and then follows the repelling part of the critical curve. To
see that this connection between the attracting part and the repelling part of the
critical curve is possible for ¯x ∼ 0, we desingularize X (1)
τ near the origin (¯x, ¯y, ϵ) =
(0, 0, 0) using the so-called secondary blow-up (¯x, ¯y, ϵ) = (ṽx, v2̃y, ṽϵ) where v ≥ 0,
(̃x, ̃y, ̃ϵ) ∈ S
2 and ̃ϵ ≥ 0.
In the family chart “̃ϵ = 1” one obtains, after dividing by v, the family of vector
ﬁelds { ˙̃x = ̃y − 1
2 ̃x2

˙̃y = B0 − ̃x + O(v).

For B0 = v = 0, dynamics of the above system are of center type with a regular
orbit γ = {̃y = 1
2 ̃x2 − 1} connecting the end point of the attracting part of the
critical curve and the end point of the repelling part of the critical curve, and
pointing from the attracting part to the repelling part. The end points are located
on the “equator” of the secondary blow-up locus {v = 0} and can be studied in
phase-directional charts “̃x = ±1, ̃y = ±1”(see also [8]).
For ¯x ̸= 0, we can consider the slow dynamics along {¯y − 1
2 ¯x2 = 0}:

¯x′ = −1 + B2 ¯x − ¯x2 + r¯x3 ¯H(r¯x, λ). (9)

When parameter B2 is kept in any compact set K ⊂] − 2, 2[, then (9) is strictly
negative in an arbitrary compact set in the ¯x-space by taking r small enough. For
(B2, r) ∼ (±2, 0), a saddle-node singularity appears in (9), located near ¯x = ±1.
When B2 is kept in any compact set K ⊂ R \ [−2, 2], then one has two simple
singularities in the slow dynamics, for r ∼ 0.
Combining the case ¯x ∼ 0 and the case ¯x ̸= 0 we ﬁnd that a passage from
¯x = +∞ to ¯x = −∞, along the critical curve, is possible when the slow dynamics
has no simple singularities. As a consequence, the critical curve, for r = 0, will be
a part of the limit periodic set Γ (see Figure 2).

3.2. Phase-directional chart “¯y = 1”. As we are interested in the points of
intersection of the critical curve {¯y − 1
2 ¯x2 = 0} with the “equator” of the primary
blow-up locus, we consider the phase-directional chart “¯y = 1” where the blow-up
map is
 (x, y, r) = (U ¯X, U 2, U R), U ≥ 0, (10)

where U ∼ 0, R ≥ 0 and ( ¯X, R) is in an arbitrarily large disk in R2. We obtain a
blown-up ﬁeld which, after dividing by U , can be written as

X (2)
τ :
 



 ˙¯X = 1 − 1
2 ¯X 2 − 1
2 ϵ2 ¯XΨ( ¯X, U, R, τ )

˙U = 1
2 ϵ2U Ψ( ¯X, U, R, τ )

˙R = − 1
2 ϵ2RΨ( ¯X, U, R, τ ),
 (11)

2648 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

where Ψ( ¯X, U, R, τ ) = ϵR3B0 − R2 ¯X + RB2 ¯X 2 − ¯X 3 + U ¯X 4 ¯H(U ¯X, λ) + U (1 −
1
2 ¯X 2)
2G(U ¯X, U 2(1 − 1
2 ¯X 2), λ).
On {U = 0, R = 0} X (2)
τ has singularities at ¯X = ±√2 + O(ϵ2) which represent
the above mentioned intersection points for ϵ = 0. The eigenvalues of the linear part
at P ±
ϵ = (±
√2 + O(ϵ2), 0, 0) are given by (∓
√2 + O(ϵ2), ∓ϵ2(
√2 + O(ϵ2)), ±ϵ2(
√2 +
O(ϵ2))). Hence, we ﬁnd that P ±
ϵ are hyperbolic (resonant) saddles for ϵ > 0 and
semi-hyperbolic singularities for ϵ = 0.
For ϵ > 0, dynamics of X (2)
τ near P ±
ϵ , restricted to {U = 0} (the blow-up locus),
are of saddle type. In P +
ϵ (resp. P −
ϵ ) we have the ¯X-axis as stable manifold (resp.
unstable manifold). For U = R = 0 and ϵ ≥ 0, dynamics of X (2)
τ points from P −
ϵ
to P +
ϵ . As a consequence, Γ will contain the part of the “equator” of the (primary)
blow-up locus between P −
0 and P +
0 .

3.3. Combining the family chart “¯r = 1” and the phase-directional chart
“¯y = 1”. The primary blow-up locus {0}×S
2
+ can be considered as a 2-dimensional
closed disc which we denote by ¯D. Let Γ denote the limit periodic set on ¯D deﬁned
as the union of the critical curve {¯y − 1
2 ¯x2 = 0} and the regular arc A of ∂ ¯D
between P −
0 and P +
0 (see Figure 2). Hence the limit periodic set Γ represents a
limiting situation, for ϵ = u = 0.
As mentioned in the introduction, we are interested in an upper bound on the
number of limit cycles of ¯Xτ that can bifurcate from Γ, for ϵ > 0 and u > 0.

P −
0

P +
0

critical curve

nilpotent singularity
 {R = 0}

A

semi-hyperbolic singularities

¯D

Figure 2. The dynamics of the vector ﬁeld ¯Xτ on ¯D for ϵ = 0,
and the singular cycle Γ = {critical curve} ∪ A.

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2649

4. Statement of the results. We suppose that τ ∈ [0, ϵ0]×[−B0
0 , B0
0 ]×[−B0
2 , B0
2 ]×
Λ where ϵ0 > 0 and B0
0 > 0 are small and ﬁxed, and B0
2 > 2 is arbitrarily large and
ﬁxed. We denote by B the compact set [−B0
0 , B0
0 ] × [−B0
2 , B0
2 ].
As it is usual in studying the cyclicity of a limit periodic set with two “corners”
(e.g. Γ with P −
0 and P +
0 ), it is preferable to link limit cycles to zeros of a diﬀerence
map rather than to ﬁxed points of a return map. We choose two sections Σ1
0 ⊂
{ ¯X = 0} and Σ2
0 ⊂ {¯x = 0}. Section Σ
1
0 is expressed in the coordinates ( ¯X, U, R) of
X (2)
τ and parametrized by (U, R) ∈ [−U 0, U 0] × [0, R0], where U 0 > 0 and R0 > 0
are small and ﬁxed; section Σ
2
0 is expressed in the coordinates (¯x, ¯y, r) of X (1)
τ and
parametrized by (¯y, r) where ¯y ∼ 0 and r ∼ 0 (see Figure 3).
We are interested in examining orbits of ¯Xτ and − ¯Xτ , deﬁned in (6), that start
at the section Σ
1
0 and meet the section Σ2
0 in ﬁnite time. To be more precise, we
denote by o+
U,R,τ (resp. o−
U,R,τ ) the forward orbit (resp. the backward orbit) of ¯Xτ
starting at the point (U, R) ∈ Σ1
0, for τ ∈ [0, ϵ0] × B × Λ. Now we can deﬁne the
following set in (U, R, τ )-space:

D = {(U, R, τ ) : o+
U,R,τ and o−
U,R,τ reach Σ2
0 in f inite time}.

Remark 1. Based on Section 3.1 and Section 3.2, orbit o+
U,R,τ (resp. o−
U,R,τ ) follows
the arc A until it comes close to point P +
0 (resp. P −
0 ), then follows the attracting
(resp. repelling) branch of the critical curve {¯y − 1
2 ¯x2 = 0}, for an appropriate
parameter B2, and meets Σ
2
0, close to the turning point (¯x, ¯y) = (0, 0). Since γ
deﬁned in Section 3.1 contains (̃x, ̃y) = (0, −1), ¯y = ϵ2̃y and ¯x-component of (8) is
equal to ¯y for ¯x = 0, we have that orbit o±
U,R,τ intersects Σ2
0 transversally. Hence
we may add “transversally” in deﬁnition of D ⊂ [−U 0, U 0]×]0, R0]×]0, ϵ0] × B × Λ.

A ﬁrst result deals with the smoothness of the transition map from Σ1
0 to Σ
2
0
along the trajectories of ¯Xτ in positive and negative time.

Theorem 4.1. There exists a small ball W around (U, R) = (0, 0) such that for
any degree k ≥ 1 of smoothness there exist 0 < ϵk ≤ ϵ0 so that the mappings

H+ : Dk = D ∩ (W × [0, ϵk] × B × Λ) → Σ2
0 :

(U, R, τ ) ↦→ (¯y, r) = (−ϵ2h+(U, R, τ ), U R) (12)

and
 H− : Dk = D ∩ (W × [0, ϵk] × B × Λ) → Σ2
0 :

(U, R, τ ) ↦→ (¯y, r) = (−ϵ2h−(U, R, τ ), U R) (13)

(deﬁned by following respectively the orbits o+
U,R,τ and o−
U,R,τ until they reach Σ2
0)
are C ∞ and have C k-extensions to Dk. Moreover, functions h+ and h− are strictly
positive and C ∞ with C k-extensions to Dk.

A proof of Theorem 4.1 is given in Section 5.1.

Remark 2. Whereas the functions H± are C ∞ on Dk ( ¯Xτ is C ∞), presence of
hyperbolic saddles P ±
ϵ , ϵ > 0, weakens the obtained smoothness: one has C k-
smoothness on Dk for all k, in the sense that possibly ϵk → 0 as k → +∞ (see
also [3]). The boundary of the domain Dk of H± includes the sets {ϵ = 0} and
{R = 0}, and might include other parts of the parameter space, where orbits o±
U,R,τ
get trapped at a saddle-node but nearby orbits can meet {¯x = 0}. Let us recall that
such a saddle-node may appear for B2 ∼ ±2, in the family chart “¯r = 1” (Section
3.1).

2650 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

The functions h+ and h− in respectively (12) and (13) play a central role in the
search for the limit cycles near Γ. Zeros of δ := h+ − h−, for U > 0, R > 0 and
ϵ > 0, correspond to periodic orbits Hausdorﬀ-close to Γ. To be more precise, for
each ﬁxed value of (r, τ ), r > 0, we can treat the function δ as 1-variable function
deﬁned on “segment” lτ
r := {(U, R); (U, R, τ ) ∈ Dk, U R = r, U ≥ 0}, for some
k ≥ 1. We want to study the number of isolated zeros (counted with multiplicity)
of the function δ on lτ
r for each ﬁxed value of (r, τ ) where r > 0.
To study the isolated zeros of δ on lτ
r , we will consider its Lie-derivative LY δ =
U ∂δ
∂U − R ∂δ
∂R along the vector ﬁeld Y = U ∂
∂U − R ∂
∂R . The reason to introduce this
Lie-derivative is that the equation {LY δ = 0} can be reduced to a simpler form
than the equation {δ = 0} which contains exponential terms (see Section 5.2).
As the vector ﬁeld Y has no zeros on {U R = r}, r > 0, Rolle’s theorem will
permit to ﬁnd the maximum number of the zeros of δ from zeros of LY δ. This trick
with a Lie-derivative along a vector ﬁeld is used in [2].
We say that (U0, R0, τ0) ∈ Dk, U0 > 0, is a zero of multiplicity n ≥ 1 of the
function δ if δ(U0, R0, τ0) = (LY δ)(U0, R0, τ0) = ... = (L
n−1
Y δ)(U0, R0, τ0) = 0 and
(L
n
Y δ)(U0, R0, τ0) ̸= 0. We inductively deﬁne Lm
Y δ as: L
0
Y δ = δ, L
2
Y δ = LY (LY δ)
and Lm
Y δ = LY (L
m−1
Y δ) for m ≥ 3.
The notion of cyclicity of δ enables us to state main results in this paper.

Deﬁnition 4.2. a) δ(U, R, τ ) is said to have ﬁnite cyclicity at B2 = ¯B2 ∈ [−B0
2 , B0
2 ]
if there exist N ∈ N0, k ∈ N1, r0 > 0 suﬃciently small, a small ball W around
(U, R) = (0, 0) and a small ball V around (ϵ, B0, B2) = (0, 0, ¯B2) such that for
each ﬁxed value of (r, τ ) ∈]0, r0] × V × Λ the number of isolated zeros (counting
multiplicity) of δ(U, R, τ ) on {(U, R); (U, R, τ ) ∈ Dk ∩ (W × V × Λ), U R = r, U ≥ 0}
is bounded by N (the number of isolated zeros of a function with an empty domain
is 0).
b) the minimum of such N is called the cyclicity of δ at B2 = ¯B2. The cyclicity of
Γ at B2 = ¯B2 is the cyclicity of δ at B2 = ¯B2.

Remark 3. Since we study the system (5) for r > 0, it is suﬃcient to deﬁne the
cyclicity of δ for U > 0 and R > 0 (r = U R). As we can see in Theorem 4.1, the
functions h+ and h− are deﬁned not only for U ≥ 0, but also for U < 0. Here
we point out that symmetries deﬁned in Section 5.2 include the variable U and
play an important role in the study of the cyclicity of δ: in Section 5.2 we will use
h−(U, R, ϵ, B0, B2, λ) = h+(−U, R, ϵ, −B0, −B2, λ).

Our ﬁrst main result states that for B2 ̸= 0 at most one (hyperbolic) limit cycle
may perturb from Γ. The case B2 ̸= 0 is easy to treat because of the presence of
the term B2rx
2 in (5) which makes sure that for B0 = 0 the blown-up vector ﬁeld
¯Xτ is far away from center behavior on the primary blow-up locus.

Theorem 4.3. a) If −2 < ¯B2 < 2 and ¯B2 ̸= 0, then the cyclicity of Γ at B2 = ¯B2
is equal to 1. When ¯B2 > 0, then we deal with a hyperbolic and attracting limit
cycle. When ¯B2 < 0, then we deal with a hyperbolic and repelling limit cycle.
b) If ¯B2 = ±2, then the cyclicity of Γ at B2 = ¯B2 is equal to 1. When ¯B2 = 2, then
we deal with a hyperbolic and attracting limit cycle. When ¯B2 = −2, then we deal
with a hyperbolic and repelling limit cycle.
c) If 2 < | ¯B2| ≤ B0
2 , then the cyclicity of Γ at B2 = ¯B2 is 0.

A proof of Theorem 4.3 is given in Section 5.3.

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2651

Remark 4. Let K denote an arbitrary compact subset of R such that K ⊂]0, B0
2 ].
Theorem 4.3 implies that there exist k ∈ N1, r0 > 0, a ball W around (U, R) = (0, 0)
and a ball V around (ϵ, B0) = (0, 0) such that for each ﬁxed value of (r, τ ) ∈
]0, r0] × V × K × Λ the number of zeros (counting multiplicity) of δ(U, R, τ ) on
{(U, R); (U, R, τ ) ∈ Dk ∩ (W × V × K × Λ), U R = r, U ≥ 0} is bounded by 1.
Hence, we have found that at most one hyperbolically attracting limit cycle can
occur in an (ϵ, B0, B2, λ, r)-uniform neighborhood of Γ where ϵ > 0, ϵ ∼ 0, B0 ∼ 0,
λ ∈ Λ, r > 0, r ∼ 0 and B2 ∈ K. This result is used in the proof of Theorem 2.4.
in [8].

When B2 ∼ 0, then one might have more than one limit cycle, as explained in
[8], and it is due to the fact that one studies perturbations of a vector ﬁeld of center
type (symmetries introduced in Section 5.2 imply that ¯Xτ is of center type on the
blow-up locus, for B0 = B2 = 0). In order to make this situation less degenerate,
we assume that ¯H(0, λ) ̸= 0 for each λ ∈ Λ, like in [8].

Theorem 4.4. Suppose that ¯H(0, λ) ̸= 0 for all λ ∈ Λ. Then the cyclicity of Γ at
B2 = 0 is bounded by 2. In other words, no more than 2 limit cycles of ¯Xτ may
bifurcate from Γ, for B2 ∼ 0.

Remark 5. Theorem 4.4 implies that at most two limit cycles can be found in an
(ϵ, B0, B2, λ, r)-uniform neighborhood of Γ where ϵ > 0, ϵ ∼ 0, B0 ∼ 0, B2 ∼ 0,
λ ∈ Λ, r > 0 and r ∼ 0. This result is also used in [8].

A proof of Theorem 4.4 is given in Section 5.4.

5. Proofs of Theorem 4.1-Theorem 4.4. We start by proving Theorem 4.1.
Besides proving Theorem 4.1, in Section 5.1 we get a nice structure of a forward
transition map between Σ
1
0 and Σ2
+ (see Figure 3). (For a precise deﬁnition of Σ2
+
we refer to later sections.) That structure is given by (46) in Theorem 5.9, and in
Section 5.2 it is used to obtain the exponential form (63) of LY δ.
We repeat once more that the exponential form of LY δ will be used in the proof
of Theorem 4.3 and in the proof of Theorem 4.4.

5.1. Proof of Theorem 4.1. We will provide an explicit proof for H+, hence
working in forward time; the treatment of H− is completely analogous.
We split H+ into three parts. Choose the sections Σ1
0 and Σ2
0, as explained
above. We also choose a section Σ1
+ (resp. Σ
2
+) near P +
ϵ transverse to arc A
(resp. transverse to the critical curve {¯y = 1
2 ¯x2}) (Figure 3). Σ1
+ (resp. Σ
2
+)
is parametrized by two regular parameters. We refer to Section 5.1.2 for precise
deﬁnitions of Σ
1
+ and Σ2
+.
One deﬁnes (see Figure 3):
1. the regular transition map R
τ
+ near the arc A from Σ
1
0 to Σ
1
+, deﬁned by the
ﬂow of ¯Xτ ,
2. the Dulac map Dτ
+ describing the corner passage near P +
ϵ from Σ
1
+ to Σ2
+ deﬁned
by the ﬂow of ¯Xτ ,
3. the singular transition map S τ
+ near the critical curve from Σ
2
+ to Σ2
0, deﬁned
by the ﬂow of ¯Xτ ,
4. the transition maps Hτ
±(U, R) := H±(U, R, τ ) near Γ from Σ
1
0 to Σ2
0 deﬁned by
the ﬂow of ± ¯Xτ . In particular Hτ
+ = S τ
+ ◦ Dτ
+ ◦ Rτ
+ for (U, R, τ ) ∈ D.

2652 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

Our goal is to study the transition maps R
τ
+, Dτ
+ and S τ
+. We start with Dτ
+.
Choosing appropriate normalizing coordinates near P +
0 will appear to be a helpful
tool in simplifying the calculation of the transition map Dτ
+.

Sτ
+
 Rτ
+ P −
ϵDτ
+

P +
ϵ

Σ2
+
 Hτ
−

Σ1
+
 Σ2
0
 Σ1
0
 ¯D
 {R = 0}{U R = r}
 Figure 3. The maps Rτ
+, Dτ
+ and S τ
+, for ϵ > 0.

5.1.1. Normalizing coordinates. Since we want to study the corner passage near P +
ϵ ,
we will change X (2)
τ , deﬁned in (11), near P +
ϵ by the equivalent family Yτ deﬁned
as:
 Yτ := − 2
Ψ( ¯X, U, R, τ ) X (2)
τ . (14)

As τ can be chosen in the compact set [0, ϵ0] × B × Λ, we can suppose that Yτ is
deﬁned in a ﬁxed neighborhood of P +
0 .
We now introduce the coordinate change

z = ¯X − √2. (15)

In the coordinates (z, U, R) the vector ﬁeld Yτ can be written as

̃Yτ :
 



 ˙z = 2√2z + z2

Ψ(
√2 + z, U, R, τ ) + ϵ2(√2 + z)

˙U = −ϵ2U
˙R = ϵ
2R.
 (16)

Our goal is to normally linearize the vector ﬁeld (16), i.e. to linearize the dif-
ferential equation of the hyperbolic variable z in (16). We aim at getting a normal
linearization of (16) that is as smooth as possible. The theorems that are pre-
sented in [11] provide normal linearizations that respect a lot of essential structure,
combined with a maximal smoothness.

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2653

We consider ﬁrst local invariant manifolds of (16) near the singularity Qϵ :=
P +
ϵ − (√2, 0, 0). Section 3.2 implies that Qϵ is a hyperbolic saddle for ϵ > 0 and
a semi-hyperbolic singularity for ϵ = 0. The well-known center manifold theorem
implies now that for each k ≥ 1 there exists a C k (B0, B2, λ)-family of local center
manifolds of the extended family of vector ﬁelds ̃Yτ +0 ∂
∂ϵ at (z, U, R, ϵ) = (0, 0, 0, 0),
where (B0, B2, λ) ∈ B × Λ. In fact the (B0, B2, λ)-family of center manifolds of the
extended family forms a τ -family of invariant manifolds of ̃Yτ at Qϵ.
It is known that in general one cannot expect the existence of a C ∞ center
manifold of a C ∞ vector ﬁeld. Since we deal with a speciﬁc C ∞ vector ﬁeld, we
utilize Theorem 1 in [11] to see that there exists a ball V around (U, R) = (0, 0),
0 < ϵ1 ≤ ϵ0 and a C 1-graph z = φ(U, R, ϵ, B0, B2, λ) on V ×[0, ϵ1]×B ×Λ that forms
a τ -family of invariant manifolds of (16), with φ(0, 0, 0, B0, B2, λ) = 0. Moreover, φ
is C ∞ for U ̸= 0 and there exists a decreasing sequence (ϵk)k≥1 for which φ is C k

on V × [0, ϵk] × B × Λ.
The main beneﬁt of Theorem 1 in [11] is hence the fact that a single center
manifold of ̃Yτ +0 ∂
∂ϵ is constructed that can be made as smooth as required, provided
one takes ϵ small enough. It is clear that this result improves the center manifold
theorem.

Remark 6. We ﬁx the center manifold z = φ of ̃Yτ + 0 ∂
∂ϵ given in Theorem 1 in
[11].

Now we have to straighten the center manifold z = φ. After applying the coor-
dinate change
 Z = z − φ (17)

to (16), the z-component of (16) can be written as
{ ˙Z = 2√2(Z + φ) + (Z + φ)2

Ψ(
√2 + Z + φ, U, R, τ ) − 2√2φ + φ2

Ψ(√2 + φ, U, R, τ ) + ϵ2Z. (18)

Here we used the fact that the family of the invariant manifolds z = φ(U, R, τ ) of
(16) is expressed by a solution to the partial diﬀerential equation

2
√2φ + φ2

Ψ(
√2 + φ, U, R, τ ) + ϵ2(
√2 + φ + U ∂φ
∂U − R ∂φ
∂R ) = 0. (19)

Remark 7. The equation (19) implies that φ = O(ϵ2).

Taking into account (18), one gets a family of vector ﬁelds




 ˙Z = −(A(U, R, τ ) + Zκ(U, R, Z, τ ))Z
˙U = −ϵ2U
˙R = ϵ2R, (20)

The functions A and κ are C ∞ for U ̸= 0 and C k for (U, R) ∈ V , |Z| small,
ϵ ∈ [0, ϵk], (B0, B2) ∈ B and λ ∈ Λ. Bearing in mind Remark 7, we ﬁnd that

A(U, R, τ ) = − ∂
∂Z
 ( 2
√2(Z + φ) + (Z + φ)
2

Ψ(
√2 + Z + φ, U, R, τ )
 )∣
∣
∣Z=0 − ϵ2

= −2
√2
−R2√2 + RB22 − 2√2 + U 4 ¯H(U √2, λ) + O(ϵ), (21)

2654 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

where O(ϵ) is C ∞ for U ̸= 0 and C k for (U, R) ∈ V , ϵ ∈ [0, ϵk], (B0, B2) ∈ B and
λ ∈ Λ. Hence A(0, 0, 0, B0, B2, λ) = 1.
We are now in a position to use the following normal linearization theorem (see
[11], Theorem 2):

Theorem 5.1. Consider a family of vector ﬁelds (20), with the above-mentioned
conditions. There exists a local C 1-family of diﬀeomorphisms of the form

(Z, U, R) → (̃z, U, R), ̃z = Φ(Z, U, R, τ ),

with Φ(0, U, R, τ ) = 0 and ∂Φ
∂Z (0, U, R, τ ) = 1, deﬁned for (Z, U, R) ∈ ̃V near the
origin and for ϵ ∈ [0, ϵ1] (up to shrinking ϵ1 if necessary), (B0, B2) ∈ B, λ ∈ Λ,
conjugating the family (20) to




 ˙̃z = −A(U, R, τ )̃z
˙U = −ϵ2U
˙R = ϵ2R. (22)

Φ is C ∞ for U R ̸= 0 and C k on ̃V × [0, ϵk] × B × Λ, up to shrinking ϵk if necessary.

5.1.2. Dulac map Dτ
+ near P +
ϵ . In this section we express ﬁrst the Dulac map Dτ
+ in
normalizing coordinates, i.e. Dτ
+ calculated from {̃z = 1}, parametrized by (U, R),
to {R = R1}, parametrized by (̃z, U ′), for the expression (22). We suppose that
R1 > 0 is small enough such that the section {R = R1} lies in the domain of the
function A. The U ′-component of Dτ
+ is U R
R1 . Let us denote the ̃z-component of Dτ
+
by dτ
+.

Proposition 5.2. There exists a ball ̃W around (U, R) = (0, 0) such that the ̃z-
component dτ
+(U, R) = d+(U, R, τ ) of Dτ
+ is C k on Ωk := (̃W ∩ {R > 0})×]0, ϵk] ×
B × Λ and has a C k-extension to the closure Ωk, up to shrinking ϵk if necessary
where (ϵk)k≥1 is introduced in Section 5.1.1. Moreover,

d
τ
+(U, R) = exp − 1
ϵ2
 ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′

= exp − 1
ϵ2
 (αk(U, R, τ ) + βk(U, R, τ ) ln R), (23)

where αk and βk are C k-functions on Ωk and βk(U, 0, τ ) = −A(0, 0, τ ).

Proof. We consider a τ -family of orbits γτ of (22) starting at (1, U, R) where U ∼ 0,
R ∼ 0 and 0 < R < R1, ϵ ∼ 0 and ϵ > 0. The expression (22) implies that the
(U, R)-component of γτ is expressed by

(U (t), R(t)) = (U exp(−ϵ2t), R exp(ϵ2t)).

The time to go from {̃z = 1} to {R = R1} is given by

t(R) = 1
ϵ2 ln R1
R .

We now look at the ﬁrst line of (22) where one substitutes U (t), R(t). Integrating
from {̃z = 1} to {R = R1}, one obtains

ln dτ
+(U, R)
1 = − ∫ t(R)

0 A(U exp(−ϵ2s), R exp(ϵ2s), τ )ds.

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2655

Hence we have that

dτ
+(U, R) = exp − ∫ 1
ϵ2 ln R1
R

0 A(U exp(−ϵ
2s), R exp(ϵ2s), τ )ds.

We make in the integral the change of variable: R′ = R exp(ϵ2s). This gives

d
τ
+(U, R) = exp − 1
ϵ2
 ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′. (24)

To end this let us use the change of variable ¯R = R′
R1 . Then (24) changes into

d
τ
+(U, R) = exp − 1
ϵ2
 ∫ 1

R/R1
 A( U R
¯RR1 , ¯RR1, τ )
¯R d ¯R.

If we denote R/R1 by V , then we have that

d
τ
+(U, R) = exp − 1
ϵ2
 ∫ 1

V
 f (V / ¯R, ¯R, U, τ )
¯R d ¯R, (25)

where f (V ′, ¯R, U, τ ) = A(U V ′, ¯RR1, τ ). Let us recall that the domain of A(U, R, τ )
only shrinks in the ϵ-direction when degree of smoothness k increases. If we use
a Taylor formula at ﬁrst order in ¯R = 0, then we have that f (V ′, ¯R, U, τ ) =
f (V ′, 0, U, τ ) + ¯Rf1(V ′, ¯R, U, τ ). As a consequence we have the following expres-
sion for the integral in (25):
∫ 1

V
 f (V / ¯R, 0, U, τ )
¯R d ¯R + ∫ 1

V f1(V / ¯R, ¯R, U, τ )d ¯R, (26)

Let us ﬁrst study the ﬁrst integral in (26). Using the change of variable w = V / ¯R
we have that
∫ 1

V
 f (V / ¯R, 0, U, τ )
¯R d ¯R = ∫ 1

V
 f (w, 0, U, τ )
w dw = −A(0, 0, τ ) ln V + ¯F (V, U, τ ), (27)

where ¯F is arbitrarily (ﬁnitely) smooth by taking small ϵ. To study the second
integral in (26), we use the following lemma (see [3]):

Lemma 5.3. 1) Let f (V, R) be a C k-function on [0, 1] × [0, 1], k ≥ 2, and let b ≥ 0
be a ﬁxed integer. Deﬁne

F (V ) = ∫ 1

V Rbf (V /R, R)dR, V ∈ [0, 1].

Then F (V ) is of the form F (V ) = α(V ) + β(V )V ln V , for some C k−2 functions
α and β, deﬁned on [0, 1], and F (0) = ∫ 1
0 Rbf (0, R)dR. Furthermore, β = O(V b),
provided we have k ≥ b + 2. 2) Should f depend smoothly on extra parameters up
to some order, then so will the resulting functions α and β be smooth w.r.t. these
parameters up to the same order.

Hence Lemma 5.3, with b = 0, implies that
∫ 1

V f1(V / ¯R, ¯R, U, τ )d ¯R = ̃αk(V, U, τ ) + ̃βk(V, U, τ )V ln V, (28)

where ̃αk, ̃βk are C k functions provided f1 is C k+2 for k ≥ 1. Let us recall that f1
is arbitrarily (ﬁnitely) smooth by taking ϵ small enough. Expressions (27) and (28),

2656 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

together with the fact that V = R
R1 , imply that the integral in (25) can be written
as
 ̃αk( R
R1 , U, τ ) + ¯F ( R
R1 , U, τ ) + A(0, 0, τ ) ln R1 − ̃βk( R
R1 , U, τ ) R
R1 ln R1

+( ̃βk( R
R1 , U, τ ) R
R1 − A(0, 0, τ )) ln R. (29)

If we denote the ﬁrst line in (29) by αk and the expression in front of ln R by βk,
then we obtain that

dτ
+(U, R) = exp − 1
ϵ2
 (αk(U, R, τ ) + βk(U, R, τ ) ln R), (30)

where for each k ≥ 1 αk and βk are C k, by taking ϵ suﬃciently small, and
βk(U, 0, τ ) = −A(0, 0, τ ) = −1 + O(ϵ).
It remains to study the smoothness of the transition map dτ
+(U, R). We focus
here to the fact that, by choosing ϵ small enough, the exponent A(0,0,τ )
ϵ2 can be
chosen arbitrarily high, so that any degree of smoothness can locally be obtained.
For the sake of completeness, let us prove it.
For R > 0 and ϵ > 0, we have nothing to prove due to the smoothness of αk and
βk.
Since βk(U, 0, τ ) < 0, d
τ
+(U, R) → 0 when R → 0 or ϵ → 0. Choose now any
k ≥ 1. In what follows, we show that, by choosing ϵ small enough, ∂I dτ
+(U, R) →
0 when R → 0 where I = (i1, i2, i3, i4, i5, i6), 1 ≤ |I| ≤ k and where ∂I =
∂|I|/∂U i1∂Ri2∂ϵ
i3∂Bi4
0 ∂Bi5
2 ∂λ
i6.
Straightforward calculations show that any derivative ∂I d
τ
+(U, R), 1 ≤ |I| ≤ k,
is a ﬁnite linear combination of the following expressions:

exp − 1
ϵ2
 (αk + βk ln R) l∏

j=1 ∂Ij ( − 1
ϵ2 (αk + βk ln R)
), (31)

where |Ij| ≥ 1 and ∑l
j=1 |Ij| = |I|.
On account of (31) it is suﬃcient to show that by choosing ϵ small enough the
expression
 1
ϵm ¯α(U, R, τ )| ln R|n1 1
Rn2 exp − 1
ϵ2
 (αk + βk ln R) (32)

goes to 0 as R → 0 where ¯α is continuous. We suppose that m ∈ N1, n1 ∈ N0 and
n2 ∈ N0 are arbitrary and ﬁxed.
¯α in (32) is bounded and, with no loss of generality, we suppose that ¯α = 1. The
logarithm of (32) is

−m ln ϵ + n1 ln | ln R| − n2 ln R − 1
ϵ2
 (αk + βk ln R)

= 1
ϵ2
 ( − mϵ2 ln ϵ + n1ϵ
2 ln | ln R| − n2ϵ2 ln R − αk − βk ln R) (33)

As ln | ln R| ≤ ln 1
R for R ∼ 0, (33) is bounded above by

1
ϵ2
 ( − mϵ2 ln ϵ − αk + (−βk − n1ϵ2 − n2ϵ2) ln R). (34)

Since βk ∼ −1, we have that −βk − n1ϵ2 − n2ϵ2 > 0 by taking ϵ small enough.
Hence (34) goes to −∞ as R → 0. It also goes to −∞ as ϵ → 0, for R small.

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2657

Let us ﬁnally deﬁne sections Σ
1
+ and Σ2
+. We denote by

ϕ( ¯X, U, R) = ϕτ ( ¯X, U, R) = (ψτ ( ¯X, U, R), U, R) = ( ̃Z, U, R)

the τ -family of coordinate changes conjugating (Yτ ), deﬁned in (14), to (22) lo-
cally near P +
ϵ . ϕ is the succession of the mapping deﬁned in (15), the mapping
deﬁned in (17), the mapping deﬁned in Theorem 5.1 and the dilatation (̃z, U, R) →
(−̃z/̃z0, U, R) = ( ̃Z, U, R), for ̃z0 > 0 small enough such that for each ϵ ∼ 0,
(B0, B2) ∈ B and λ ∈ Λ section {(−̃z0, U, R) | U ∼ 0, R ∼ 0, R ≥ 0} lies in the
domain of the inverse of the diﬀeomorphism deﬁned in Theorem 5.1. Let us remark
that (22) is unchanged under the dilatation.
Let σ1
+ = {(1, U, R) | U ∼ 0, R ∼ 0, R ≥ 0}
and σ2
+ = {( ̃Z, U ′, R1) | ̃Z ∼ 0, ̃Z ≥ 0, U ′ ∼ 0}.
By taking R1 > 0 suﬃciently small and ﬁxed one can suppose that these sections lie
in the domain of ϕ
−1 for each ϵ ∼ 0, (B0, B2) ∈ B and λ ∈ Λ. We now choose Σ2
+ in
the ( ¯X, U, R) coordinates of Yτ near P +
ϵ inside {R = R1} and transversally cutting
the τ -family of invariant manifolds ¯X = √2 + φ(U, R, τ ) of Yτ (φ is ﬁxed in Remark
6). Hence we can take Σ2
+ = ϕ
−1(σ2
+). We parametrize Σ2
+ by { ¯X ∼ √2, U ∼ 0}.
We choose Σ1
+ = ϕ
−1(σ1
+) transversally cutting the arc A. We parametrize Σ
1
+ by
(U, R). The sections Σ
1
+ and Σ2
+ depend, in a C k way, on τ bearing in mind that
only ϵ decreases when the smoothness requirements increase.
The map Dτ
+ from Σ1
+ to Σ2
+, deﬁned by the ﬂow of Yτ (i.e. X (2)
τ ), can be
studied now, by Proposition 5.2, in the normalizing coordinates ( ̃Z, U, R) in the
region { ̃Z > 0, R > 0}, from σ1
+ to σ2
+. It can be expressed by:
(U, R) → (d+(U, R, τ ), U R/R1).

5.1.3. Regular transition map Rτ
+. Let us recall that the map R
τ
+, from a subset of
Σ1
0 to Σ1
+, is deﬁned by the ﬂow of X (2)
τ . The transition map R
τ
+ can be represented
as going from a subset of Σ1
0 to σ1
+, i.e. with values in the normalizing coordinates
( ̃Z, U, R). One obtains map R+(U, R, τ ). Hence R+ is expressed in (U, R) with
values in (U, R).
We split R+ into two parts. Choose ¯X0 ∈]0, √2[, suﬃciently close to √2, such
that for each ϵ ∼ 0, (B0, B2) ∈ B and λ ∈ Λ section {( ¯X0, U, R) | U ∼ 0, R ∼ 0, R ≥
0} lies in the domain of ϕ and such that ¯X0 is strictly smaller than the ¯X-coordinate
of ϕ
−1
τ (1, 0, 0). Let T+(U, R, τ ) represent the transition map from (a subset of) Σ
1
0
to { ¯X = ¯X0} along the trajectories of X (2)
τ .

Lemma 5.4. There exists a ball ̃W1 around (U, R) = (0, 0) and 0 < ̃ϵ ≤ ϵ0 such
that T+ is C ∞ on Ω1 := (̃W1 ∩ {R ≥ 0}) × [0, ̃ϵ] × B × Λ and

T+(U, R, τ ) = (U (1 + ϵ2 ¯T (U, R, τ )), R(1 + ϵ2 ¯T (U, R, τ ))−1), (35)

where ¯T is C ∞ on Ω1.

Proof. Notice ﬁrst that the parameter (B0, B2, λ) takes values in the compact set
B × Λ. Hence the ¯X-component of X (2)
τ is strictly positive for ¯X ∈ [0, ¯X0] and
(ϵ, U, R) ∼ (0, 0, 0). This means that the family (11) has no singularities between
the sections Σ
1
0 and { ¯X = ¯X0}, under the given conditions on the parameters.

2658 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

In other words, the orbit of (11), starting at (U, R) ∈ Σ1
0, (U, R) ∼ (0, 0), reaches
{ ¯X = ¯X0} in a ﬁnite time. Remark that this fact is clear for ϵ = 0. The fundamental
results on the existence, uniqueness and continuity with respect to parameters of
solutions to initial value problems imply now that we deal with a C ∞ transition
map T+ = (T 1
+, T 2
+) (X (2)
τ is C ∞).
We know that T+ preserves U R, i.e. T 1
+(U, R, τ )T 2
+(U, R, τ ) = U R for any τ .
We also know that T+ preserves {U = 0} and {R = 0}. It means that there exist
C ∞-functions t1
+ and t
2
+, such that:

T 1
+(U, R, τ ) = U t1
+(U, R, τ ), T 2
+(U, R, τ ) = Rt
2
+(U, R, τ ).

Hence we ﬁnd that t1
+(0, 0, τ ) ̸= 0 and t2
+ = 1/t1
+, for any τ . We obtain that

T+(U, R, τ ) = (U t1
+(U, R, τ ), R 1
t1
+(U, R, τ ) ).

If ϵ = 0, then T+(U, R, τ ) = (U, R). This means that there exist a C ∞-function ¯T
such that t
1
+(U, R, τ ) = 1 + ϵ2 ¯T (U, R, τ ).

Choose sections π+
τ := ϕ({( ¯X0, U, R) | U ∼ 0, R ∼ 0, R ≥ 0}). We parametrize
π+
τ through ϕ by (U, R). In order to ﬁnish the study of R+, we need to consider the
regular transition map F+ : π+
τ → σ1
+ along the trajectories of (22), expressed using
the chosen parametrization on π+
τ , σ1
+. Notice that ϕ leaves the (U, R)-component
unchanged. This means that the regular map T+ is expressed by (35) if we use for
{ ¯X = ¯X0} the normalizing coordinates ( ̃Z, U, R). Then we have
R+(U, R, τ ) = F+(T+(U, R, τ ), τ ).

Lemma 5.5. There exists a ball ̃W2 around (U, R) = (0, 0) such that F+ is C k on
Ω2
k := (̃W2 ∩ {R ≥ 0}) × [0, ϵk] × B × Λ, up to shrinking ϵk if necessary, and

F+(U, R, τ ) = (U (1 + ϵ
2 ¯F (U, R, τ )), R(1 + ϵ2 ¯F (U, R, τ ))
−1),

where ¯F is C k on Ω2
k.

Proof. The study of F+ is analogous to the study of T+. Notice that the domain of
A in (22) only shrinks in the ϵ-direction as the smoothness requirements increase,
and that π+
τ is a graph of a C k-function which has the same smoothness property
as A.

Combining Lemma 5.4 and Lemma 5.5 we get:

Proposition 5.6. There exists a ball ̃W3 around (U, R) = (0, 0) such that R+ is
C k on Ω3
k := (̃W3 ∩ {R ≥ 0}) × [0, ϵk] × B × Λ, up to shrinking ϵk if necessary, and

R+(U, R, τ ) = (U (1 + ϵ
2 ¯R(U, R, τ )), R(1 + ϵ2 ¯R(U, R, τ ))−1), (36)

where ¯R is C k on Ω3
k.

Proof. We have

R+(U, R, τ ) = F+(T+(U, R, τ ), τ )

= (U (1 + ϵ2 ¯T )(1 + ϵ2 ¯F (T+, τ )), R(1 + ϵ
2 ¯T )−1(1 + ϵ2 ¯F (T+, τ ))
−1)

= (U (1 + ϵ
2 ¯R(U, R, τ )), R(1 + ϵ2 ¯R(U, R, τ ))−1).

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2659

5.1.4. Combining R+ and Dτ
+. In the following proposition we give the expression
for the transition map (Dτ
+ ◦ R+)(U, R, τ )
going from (a subset of) Σ1
0 to σ2
+, using the chosen parametrization on Σ1
0, σ2
+.

Proposition 5.7. There exists a ball ̃W4 around (U, R) = (0, 0) such that Dτ
+ ◦ R+
is well deﬁned and C k on Ω4
k := (̃W4 ∩ {R > 0})×]0, ϵk] × B × Λ and has a C k-
extension to Ω4
k, up to shrinking ϵk if necessary. Moreover,

(Dτ
+ ◦ R+)(U, R, τ ) = (d
τ
+(R+(U, R, τ )), U R
R1
 ),

where
d
τ
+(R+(U, R, τ )) = exp − 1
ϵ2
 ( ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′ + ϵ
2l(U, R, τ )), (37)

with l(U, R, τ ) = l(k)
1 (U, R, τ ) + l(k)
2 (U, R, τ )R ln R.

Functions l(k)
1 , l(k)
2 are C k on Ω4
k. The function l does not depend on k.

Proof. The above-mentioned smoothness properties of Dτ
+ ◦ R+ follow directly from
Proposition 5.2 and Proposition 5.6. From Section 5.1.2 and (36), it is clear that
the U ′-component of Dτ
+ ◦ R+ is

U (1 + ϵ2 ¯R(U, R, τ )).R(1 + ϵ2 ¯R(U, R, τ ))−1/R1 = U R/R1.

Using expressions (23) (we write α = αk and β = βk) and (36) we obtain that

d
τ
+(R+(U, R, τ )) = exp − 1
ϵ2
 (α(U (1 + ϵ2 ¯R), R(1 + ϵ2 ¯R)
−1, τ )

+β(U (1 + ϵ2 ¯R), R(1 + ϵ2 ¯R)−1, τ ) ln R(1 + ϵ2 ¯R)−1)

= exp − 1
ϵ2
 (α(U, R, τ ) + β(U (1 + ϵ2 ¯R), R(1 + ϵ2 ¯R)−1, τ ) ln R

+O(ϵ2 ¯R) − β(U (1 + ϵ2 ¯R), R(1 + ϵ2 ¯R)
−1, τ ) ln(1 + ϵ2 ¯R)
). (38)

On account of Proposition 5.2, we have that

β(U, R, τ ) = −A(0, 0, τ ) + R ¯β(U, R, τ ). (39)

Based on (39), we have

β(U (1 + ϵ2 ¯R), R(1 + ϵ2 ¯R)−1, τ )

= −A(0, 0, τ ) + R(1 + ϵ2 ¯R)−1 ¯β(U (1 + ϵ2 ¯R), R(1 + ϵ2 ¯R)
−1, τ )

= −A(0, 0, τ ) + R( ¯β(U, R, τ ) + O(ϵ2 ¯R))

= β(U, R, τ ) + RO(ϵ2 ¯R). (40)

Using (40) and the fact that ln(1 + ϵ2 ¯R(U, R, τ )) = O(ϵ2 ¯R), the expression (38)
changes to

dτ
+(R+(U, R, τ ))

= exp − 1
ϵ2
 (α(U, R, τ ) + β(U, R, τ ) ln R + O(ϵ2 ¯R) + O(ϵ2 ¯R)R ln R)

= exp − 1
ϵ2
 ( ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′ + O(ϵ2 ¯R) + O(ϵ2 ¯R)R ln R).

2660 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

This completes the proof.

The section σ2
+ is contained in a family directional chart and we can use for it
better adapted coordinates. On section σ2
+ we can consider coordinates (¯x, r), where
(¯x, ¯y, r) are the coordinates of X (1)
τ , deﬁned in (8). The changes of coordinates

( ̃Z, U ′) → (¯x, r)

are given by r = U ′R1 (ϕ leaves the (U, R)-component unchanged) and ¯x = ¯xτ,r( ̃Z)
(we have eliminated U ′ = r
R1 in the expression of ¯x).

Lemma 5.8. One has

¯xτ,r( ̃Z) = 1
R1
 (√2 + φ( r
R1 , R1, τ )
) − ̃z0
R1 ̃Z(1 + O( ̃Z)), (41)

where φ is ﬁxed in Remark 6, ̃z0 > 0 is deﬁned at the end of Section 5.1.2 and
the domain of O( ̃Z) only shrinks in the ϵ-direction as the smoothness requirements
increase.

Proof. On account of blow-up formulas (7) and (10) we get the following relation
between the coordinates ¯x and ¯X, on σ2
+:

¯x = ¯X
R1 . (42)

The mappings deﬁned in (15) and (17), together with Theorem 5.1 and the dilata-
tion deﬁned in Section 5.1.2, imply the following relation between the coordinates
¯X and ( ̃Z, U ′), on σ2
+:

¯X = √2 + φ(U ′, R1, τ ) − ̃z0 ̃Z(1 + O( ̃Z)). (43)

Based on Theorem 5.1, O( ̃Z) in (43) has the required property stated in Lemma
5.8.
Putting together (42) and (43) we ﬁnd the relation between ¯x and ( ̃Z, r) on σ2
+:

¯x = 1
R1 (
√2 + φ( r
R1 , R1, τ )) − 1
R1 ̃z0 ̃Z(1 + O( ̃Z)). (44)

Parameterizing section σ2
+ by (¯x, r), the transition map from (a subset of) Σ1
0 to
σ2
+ along the trajectories of ¯Xτ is equal to
(¯xτ,U R(d
τ
+(R+(U, R, τ ))), U R). (45)

We denote by ¯x(U, R, τ ) the ﬁrst component in (45). Combining Proposition 5.7
and Lemma 5.8 we obtain the ﬁnal form for the transition map from (a subset of)
Σ1
0 to Σ2
+ = ϕ−1(σ2
+), where Σ
2
+ is parametrized by (¯x, r):

Theorem 5.9. There exists a ball ̃W5 around (U, R) = (0, 0) such that ¯x(U, R, τ ) is
well deﬁned and C k on Ω5
k := (̃W5 ∩{R > 0})×]0, ϵk]×B×Λ and has a C k-extension
to Ω5
k, up to shrinking ϵk if necessary. Moreover,

¯x(U, R, τ ) = 1
R1
 (√2 + φ( U R
R1 , R1, τ )
)

− exp − 1
ϵ2
 ( ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′ + ϵ2L(U, R, τ )), (46)

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2661

where
 L(U, R, τ ) = L
(k)
1 (U, R, τ ) + L
(k)
2 (U, R, τ )R ln R.

Functions L
(k)
1 and L
(k)
2 are C k on Ω5
k. The function L does not depend on k.

Proof. The above-mentioned smoothness property of ¯x(U, R, τ ) follows directly from
Proposition 5.7 and Lemma 5.8. Taking into account (41) we get

¯x(U, R, τ ) = 1
R1
 (√2 + φ( U R
R1 , R1, τ )
)

− ̃z0
R1 dτ
+(R+(U, R, τ ))
(1 + O(d
τ
+(R+(U, R, τ )))
). (47)

Of course, we have that

1 + O(d
τ
+(R+(U, R, τ ))) = exp − 1
ϵ2
 ( − ϵ2 ln(1 + O(d
τ
+(R+(U, R, τ ))))),

where ln(1 + O(d
τ
+(R+(U, R, τ )))) is arbitrarily (ﬁnitely) smooth by taking ϵ small
enough. This follows directly from the fact that functions O( ̃Z) in Lemma 5.8 and
dτ
+(R+(U, R, τ ))) are arbitrarily (ﬁnitely) smooth by taking ϵ small enough. If we
use (37), then the expression (47) changes to

¯x(U, R, τ ) = 1
R1
 (√2 + φ( U R
R1 , R1, τ )
)

− exp − 1
ϵ2
 ( ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′ + ϵ2l(U, R, τ )

−ϵ
2 ln(1 + O(d
τ
+(R+(U, R, τ )))) − ϵ2 ln ̃z0
R1
 )
.

The rest of the proof is now trivial.

5.1.5. Transition map S τ
+ and conclusion. We consider the transition map S τ
+ from
Σ2
+ to Σ2
0 ⊂ {¯x = 0} along the trajectories of the vector ﬁeld X (1)
τ deﬁned in (8).
Remark that S τ
+ can be treated entirely in the family chart “¯r = 1”. Section Σ2
+ is
parametrized by (¯x, r) and section Σ
2
0 is parametrized by (¯y, r). One obtains map
S τ
+(¯x, r) = (s+(¯x, r, τ ), r).
As mentioned in Section 3.1, in the family chart we consider r as a regular
parameter and observe that ϵ is a singular perturbation parameter. It is important
to realize that the slow dynamics (9) are characterized by a regular ﬂow box, with
possible isolated saddle-node singularities for (B2, r) ∼ (±2, 0), located away from
the origin (¯x, ¯y) = (0, 0). This case has already been treated in [4].
In order to be able to use the results in [4], we deﬁne a section

T = {̃x = 0},

along the secondary blow-up locus of the origin (¯x, ¯y) = (0, 0) (see Section 3.1).
More precisely, T is deﬁned in the family chart {̃ϵ = 1}, and parametrized by the
(secondary) blow-up coordinate ̃y. We denote by ̃y = ˆs+(¯x, r, τ ) the transition map
between Σ
2
+ and T . By following the orbits through the curve {¯x = ¯x(U, R, τ ), ¯y =
1/R2
1, r = U R}, (U, R, τ ) ∈ D, (ϵ, U, R) ∼ (0, 0, 0), in forward time until they reach
T , we end up with a C k-transition map ̃y = ˆs+(¯x(U, R, τ ), U R, τ ) with a C k-
extension to the closure of its domain. Degree of smoothness k can be chosen

2662 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

arbitrarily high by taking ϵ small enough. We refer to Theorem 3.1 of [4] and
Theorem 5.9 in this paper.
Since ¯y = ϵ2̃y, we obtain s+ = ϵ2ˆs+. For (ϵ, B0) ∼ (0, 0), ˆs+ is strictly negative
because γ ∩ T = (0, −1) where γ is deﬁned in Section 3.1.
It is now clear that the transition map
H+(U, R, τ ) = (s+(¯x(U, R, τ ), U R, τ ), U R), (U, R, τ ) ∈ D, (ϵ, U, R) ∼ (0, 0, 0),
has all the properties mentioned in Theorem 4.1 in this paper.

5.2. Diﬀerence map and Lie-derivative. In order to prove Theorems 4.3 and
4.4, we need to consider the diﬀerence map

∆(U, R, τ ) = H+(U, R, τ ) − H−(U, R, τ ), (48)

where (U, R, τ ) ∈ Dk and Dk, H± are deﬁned in (12) and (13).
The r-component of ∆ is equal to 0. The ¯y-component of ∆ can be written as
−ϵ2δ(U, R, τ ), where

δ(U, R, τ ) = h+(U, R, τ ) − h−(U, R, τ ), (49)

where (U, R, τ ) ∈ Dk.
The expression of (5) is invariant under the symmetry:

S : (r, B0, B2) → (−r, −B0, −B2). (50)

From the family rescaling (7) and the symmetry S, deﬁned in (50), it follows that
the vector ﬁeld X (1)
τ is invariant under the symmetry:

SF : (¯x, ¯y, r, ϵ, B0, B2, λ, t) → (−¯x, ¯y, −r, ϵ, −B0, −B2, λ, −t). (51)

The directional blow-up formula (10) and the symmetry S, deﬁned in (50), imply
that X (2)
τ is invariant under the symmetry

SP : ( ¯X, U, R, ϵ, B0, B2, λ, t) → (− ¯X, −U, R, ϵ, −B0, −B2, λ, −t). (52)

By the invariance of X (1)
τ (resp. X (2)
τ ) under SF (resp. SP ), deﬁned in (51) (resp.
(52)), one can write (49) as

δ(U, R, ϵ, B0, B2, λ) = h+(U, R, ϵ, B0, B2, λ) − h+(−U, R, ϵ, −B0, −B2, λ), (53)

where (U, R, ϵ, B0, B2, λ) ∈ Dk.
To study isolated zeros of δ, we will consider its Lie-derivative LY δ = U ∂δ
∂U −R ∂δ
∂R
(see Section 4). It is clear that LY (U R) = 0. We ﬁrst apply the Lie-derivation to
the expression −ϵ
2h+(U, R, τ ):

LY ( − ϵ2h+(U, R, τ )) = LY (s+(¯x(U, R, τ ), U R, τ ))

= ∂s+
∂ ¯x (¯x(U, R, τ ), U R, τ ).LY (¯x(U, R, τ )
), (54)

where (U, R, τ ) ∈ Dk.

Remark 8. From now on, we avoid mentioning the fact that degree of smoothness
of h+(U, R, τ ), ¯x(U, R, τ ), etc., depends on ϵ. We also do not specify domains of
h+(U, R, τ ), ¯x(U, R, τ ), etc., and we avoid pointing out that αk, βk, etc., depend on
degree k of smoothness. We merely say that all these functions are C k bearing in
mind that any (ﬁnite) degree of smoothness can be obtained. Similarly, we say that
F (U, R, τ ) is C k in (U, R, R ln R, τ ) if we can choose a suﬃciently smooth function
f such that F (U, R, τ ) = f (U, R, R ln R, τ ).

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2663

5.2.1. Study of LY(¯x(U, R, τ )). On account of (23) and (46) we get

LY (¯x(U, R, τ )
) = 1
ϵ2 exp − 1
ϵ2
 ( ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′ + ϵ2L
)

.LY (α + β ln R + ϵ2L), (55)

where α and β are the C k-functions deﬁned in (23), and L(U, R, τ ) is the C k-function
in (U, R, R ln R, τ ) introduced in Theorem 5.9.
We can write P = LY (α + β ln R + ϵ2L). In order to study P , we need the
following easy properties of the Lie-derivation:

Lemma 5.10. 1. LY (ln R) = −1.
2. If ̃ν(U, R, τ ) = ν(U, R, R ln R, τ ) is C k in (U, R, R ln R, τ ), then ζ(U, R, τ ) =
LY ̃ν(U, R, τ ) is C k in (U, R, R ln R, τ ) and moreover ζ(0, 0, τ ) ≡ 0 (one can also
write: ζ = o(1)).

Taking into account Lemma 5.10 and the fact that β(U, 0, τ ) = −A(0, 0, τ ) (see
Proposition 5.2), we obtain that

P (U, R, τ ) = LY (α + β ln R + ϵ2L)

= LY α + (ln R)LY β − β + ϵ2LY L

= −β(U, R, τ ) + o(1), (56)

where o(1) is C k in (U, R, R ln R, τ ). Based on (56), we ﬁnd that P (0, 0, τ ) =
A(0, 0, τ ) > 0. As a consequence, the function P (U, R, τ ) remains strictly positive
for U, R small enough and its logarithm is C k in (U, R, R ln R, τ ). Hence (55) changes
to (LY ¯x(U, R, τ ))(U, R, τ ) = 1
ϵ2 exp − 1
ϵ2
 ( ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′ + ϵ2 ¯L(U, R, τ )),

(57)
where ¯L is C k in (U, R, R ln R, τ ).

5.2.2. Study of ∂s+
∂¯x (¯x(U, R, τ ), UR, τ ). The derivative ∂s+
∂ ¯x can be expressed in
terms of an integral of divergence:

∂s+
∂ ¯x (¯x, r, τ ) = −ϵ
2π(¯x, r, τ )
s+(¯x, r, τ ) exp ∫

O¯x,r,τ divX (1)
τ dt, (58)

where O¯x,r,τ is the orbit through (¯x, 1
R2
1 , r) ∈ Σ2
+ in positive time until it hits Σ
2
0
and where
 π(¯x, r, τ ) = ϵB0 − ¯x + B2 ¯x2 − ¯x3 + r¯x4 ¯H(r¯x, λ)

+r( 1
R2
1 − 1
2 ¯x2)2G(r¯x, r2( 1
R2
1 − 1
2 ¯x
2), λ). (59)

This follows directly from the following well known result (see Proposition 2 of [10]):

Proposition 5.11. Let f be a vector ﬁeld on an open subset of Rn. Let S1 and S2
be two open sections of Rn, transverse to the ﬂow of f . Assume p ∈ S1, q ∈ S2 and
the orbit through p reaches q in ﬁnite time. Let T : S0 ⊂ S1 → S2 be the transition
map deﬁned in a neighborhood of p. If φi : Ui → Si are coordinates for Si with
Ui ⊂ Rn−1, then

det(D(φ−1
2 ◦ T ◦ φ1))(s1) = det(Dφ1(s1)|f (p))
det(Dφ2(s2)|f (q)) exp { ∫

O(p,q) divf dt
},

2664 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

where s1 = φ−1
1 (p), s2 = φ−1
2 (q), and where (Dφ1(s1)|f (p)) is a matrix composed
of the n × (n − 1) matrix Dφ1(s1) and the column vector f (p), and similarly for
(Dφ2(s2)|f (q)). The integral is taken over the orbit O(p, q) from p to q parametrized
by t.

We denote the integral in (58) by I(¯x, r, τ ).
From (58), we ﬁnally get:

∂s+
∂ ¯x (¯x(U, R, τ ), U R, τ ) = π(¯x(U, R, τ ), U R, τ )
h+(U, R, τ ) exp I(¯x(U, R, τ ), U R, τ ), (60)

where we used −ϵ2h+(U, R, τ ) = s+(¯x(U, R, τ ), U R, τ ).

Remark 9. 1. Taking into account Theorem 5.9 and (59) we see that function
π(¯x(U, R, τ ), U R, τ ) in (60) is a strictly negative C k-function by taking ϵ, U and R
small enough. Let us recall that R1 is suﬃciently small and ﬁxed such that Ψ in
(11) is strictly negative for ¯X ∼ √2, U ∼ 0, |R| ≤ R1, ϵ ∼ 0, (B0, B2) ∈ B and
λ ∈ λ.
2. On account of Theorem 4.1, we see that h+(U, R, τ ) is C k and strictly positive.

Remark 9 implies that − π(¯x(U,R,τ ),U R,τ )
h+(U,R,τ ) is strictly positive and C k, and its log-
arithm is a C k-function. Hence, (60) can be written as

∂s+
∂ ¯x (¯x(U, R, τ ), U R, τ ) = − exp 1
ϵ2 (ϵ2I(¯x(U, R, τ ), U R, τ ) + ϵ
2 ̃L(U, R, τ )
), (61)

where ̃L is a C k-function.

5.2.3. Combining LY(¯x(U, R, τ )
) and ∂s+
∂¯x (¯x(U, R, τ ), UR, τ ). Bearing in mind
(57) and (61), (54) can be written as

(LY ( − ϵ2h+))
(U, R, τ ) = − 1
ϵ2 exp 1
ϵ2
 ( − ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′

+ϵ
2I(¯x(U, R, τ ), U R, τ ) + ϵ2L
∗(U, R, τ )), (62)

where L
∗ is C k in (U, R, R ln R, τ ).

5.2.4. Lie-derivative of δ. Let us recall that τ = (ϵ, B0, B2, λ). We denote by τ ∗

the parameter (ϵ, −B0, −B2, λ).

Lemma 5.12. Suppose that f (U, R, τ ) is C k and write g(U, R, τ ) = f (−U, R, τ ∗).
Then
 (LY g)(U, R, τ ) = (LY f )(−U, R, τ ∗).

Proof. We have:

(LY g)(U, R, τ ) = U ∂g
∂U (U, R, τ ) − R ∂g
∂R (U, R, τ )

= (−U ) ∂f
∂U (−U, R, τ ∗) − R ∂f
∂R (−U, R, τ ∗)

= (LY f )(−U, R, τ ∗).

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2665

Using (53), (62) and Lemma 5.12, we ﬁnd the Lie-derivative of δ:

(LY δ)(U, R, τ ) = 1
ϵ4 exp 1
ϵ2
 ( − ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′

+ϵ2I(¯x(U, R, τ ), U R, τ ) + ϵ2L
∗(U, R, τ )
)

− 1
ϵ4 exp 1
ϵ2
 ( − ∫ R1

R
 A( −U R
R′ , R′, τ ∗)
R′ dR′

+ϵ2I(¯x(−U, R, τ ∗), −U R, τ ∗) + ϵ2L
∗(−U, R, τ ∗)
). (63)

It is clear that for ϵ > 0 and R > 0 the equation {LY δ = 0} is equivalent to

− ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′ + ∫ R1

R
 A( −U R
R′ , R′, τ ∗)
R′ dR′

+ϵ2I(¯x(U, R, τ ), U R, τ ) − ϵ
2I(¯x(−U, R, τ ∗), −U R, τ ∗) + ϵ2 ¯L
∗(U, R, τ ) = 0, (64)

where ¯L
∗ is a C k-function in (U, R, R ln R, τ ) which is identically zero for U = B0 =
B2 = 0. Our goal is to solve the equation (64) on segment {(U, R); U R = r, U ∼
0, U > 0, R ∼ 0, R > 0}, for each possible (r, τ ) such that r ∼ 0 and r > 0.

We ﬁrst simplify (64). It is clear that ∫ R1
R A( U R
R′ ,R′,τ )
R′ dR′ goes to +∞ as R → 0.

We aim at controlling the diﬀerence ∫ R1
R A( U R
R′ ,R′,τ )
R′ dR′ − ∫ R1
R A( −U R
R′ ,R′,τ ∗)
R′ dR′ in
(64).

Lemma 5.13. One has that
∫ R1

R
 A( U R
R′ , R′, ϵ, B0, B2, λ)
R′ dR′

= (1 + ϵf1(ϵ)) ∫ R1

R
 A( U R
R′ , R′, 0, B0, B2, λ)
R′ dR′ + ϵf2(U, R, τ ), (65)

where f1 is a C k-function, depending only on ϵ, and where f2 is a C k-function in
(U, R, R ln R, τ ).

Proof. The expression (21) implies that A(U, R, 0, B0, B2, λ) > 0. If we keep the
notation τ for (ϵ, B0, B2, λ) and denote (0, B0, B2, λ) by τ0, then we obtain that

A(U, R, τ ) = A(U, R, τ0)
(1 + ϵF1(τ ) + ϵRF2(U, R, τ ) + ϵU F3(U, R, τ )
), (66)

where F1, F2 and F3 are C k. If we suppose that (U, R) = (0, 0) in (66), then we get

A(0, 0, τ ) = A(0, 0, τ0)(1 + ϵF1(τ )
) > 0. (67)

Taking into account (19) and the fact that the parameters B0, B2 and λ are ac-
companied by U or R in the expression Ψ, deﬁned in (11), the family of invariant
manifolds φ, ﬁxed in Remark 6, does not depend on (B0, B2, λ), for (U, R) = (0, 0).
As Ψ and φ appear in the expression (21), it follows that A(0, 0, τ ) does not depend
on (B0, B2, λ). Formula (67) now implies that F1(τ ) does not depend on (B0, B2, λ),
hence F1(τ ) = f1(ϵ).
It is clear that we can write (66) as

A(U, R, τ ) = A(U, R, τ0)
(1 + ϵf1(ϵ)
) + ϵRF2(U, R, τ ) + ϵU F3(U, R, τ ), (68)

2666 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

for some new C k-functions F2 and F3. Using (68), we have that
∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′ = (1 + ϵf1(ϵ)
) ∫ R1

R
 A( U R
R′ , R′, τ0)
R′ dR′

+ϵ ∫ R1

R
 R′F2( U R
R′ , R′, τ )
R′ dR′ + ϵ ∫ R1

R
 U RF3( U R
R′ , R′, τ )
R′2 dR′. (69)

Take any C k-function F4(U, R, τ ). In the proof of Proposition 5.2, we found that
∫ R1

R
 F4( U R
R′ , R′, τ )
R′ dR′ = α∗(U, R, τ ) + β∗(U, R, τ ) ln R, (70)

where α∗ and β∗ are C k and where β∗(U, 0, τ ) = −F4(0, 0, τ ). If we choose
F4(U, R, τ ) = RF2(U, R, τ ), then we get β∗(U, 0, τ ) = 0. In other words, ln R
in (70) is accompanied by R. Hence the second integral on the right hand side of
(69) is a C k-function in (U, R, R ln R, τ ). If we take F4(U, R, τ ) = U F3(U, R, τ ) in
(70), then we get β∗(U, 0, τ ) = 0. Hence the third integral on the right hand side
of (69) is a C k-function in (U, R, R ln R, τ ).

Using (21) and Lemma 5.13, we ﬁnd that

− ∫ R1

R
 A( U R
R′ , R′, τ )
R′ dR′ + ∫ R1

R
 A( −U R
R′ , R′, τ ∗)
R′ dR′

= (1 + ϵf1(ϵ)
)C(U, R, B2, λ) + ϵ ¯f2(U, R, τ ), (71)

where ¯f2 is a C k-function in (U, R, R ln R, τ ) and identically zero for U = B0 =
B2 = 0, and where

C(U, R, B2, λ) = −8
√2 ∫ R1

R
 B2R′ + U R
R′ ( ¯H( U R
R′ √2, λ) + ¯H( −U R
R′ √2, λ)
)

R′D(U, R, R′, B2, λ)D(−U, R, R′, −B2, λ) dR′,

(72)
with
 D(U, R, R′, B2, λ) = −
√2R′2 + 2B2R′ − 2
√2 + 4 U R
R′ ¯H( U R
R′ √2, λ).

Taking into account (71), (64) changes to

ϵ
2I(¯x(U, R, τ ), U R, τ ) − ϵ2I(¯x(−U, R, τ ∗), −U R, τ ∗)

+(1 + ϵf1(ϵ)
)C(U, R, B2, λ) + ϵ̃L∗(U, R, τ ) = 0, (73)

where ̃L
∗ is a C k-function in (U, R, R ln R, τ ) and identically zero for U = B0 =
B2 = 0.
It can be easily seen that C, deﬁned in (72), is bounded for R ∼ 0. We make
this statement precise in the following lemma:

Lemma 5.14.

C(U, R, B2, λ) = B2c1(U, R, B2, λ) + U c2(U, R, B2, λ), (74)

where c1 and c2 are C k-functions in (U, R, R ln R, B2, λ) and where c1 is strictly
negative for R ∼ 0 and R ≥ 0.

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2667

Proof. Using (72), we can write C as

C(U, R, B2, λ) = B2
 ∫ R1

R C1( U R
R′ , R′, B2, λ)dR′ + ∫ R1

R
 U R
R′2 C2( U R
R′ , R′, B2, λ)dR′,

(75)
where C1 and C2 are C ∞-functions. Bearing in mind (70), we see that the ﬁrst inte-
gral in (75) is a C k-function in (U, R, R ln R, B2, λ). We denote it by c1(U, R, B2, λ).
It is clear from (72) that c1 is strictly negative.
The second integral in (75) we can write as

U R ∫ R1

R
 1
R′2 C2( U R
R′ , 0, B2, λ)dR′ + U R ∫ R1

R
 1
R′ C3( U R
R′ , R′, B2, λ)dR′, (76)

where C3 is a C ∞-function. The second expression in (76) can, by (70), be written
as U C4(U, R, B2, λ) where C4 is a C k-function in (U, R, R ln R, B2, λ).
If we use the change of variables: R
R′ = w, then the ﬁrst expression in (76)
changes to
 U ∫ 1

R
R1 C2(U w, 0, B2, λ)dw.

The above integral can be written as U C5(U, R, B2, λ), for some C ∞-function C5.
We deﬁne now c2(U, R, B2, λ) = C4(U, R, B2, λ) + C5(U, R, B2, λ).

It remains to simplify the diﬀerence of divergence integrals in (73). The integral
of divergence I has been studied in detail in [10], if the slow dynamics (9) has no
zeros, and in [4], if the slow dynamics (9) has isolated saddle-node singularities
located away from the contact point (¯x, ¯y) = (0, 0).
As we mentioned above, a saddle-node singularity appears in (9) for (B2, r) ∼
(±2, 0), located near ¯x = ±1. Hence we may rely on [4]. When parameter B2 is
kept in any compact set K ⊂] − 2, 2[, then (9) is regular in an arbitrary compact
set in the ¯x-space by taking r small enough. As a consequence, we are allowed to
refer to [10]. When 2 < |B2| ≤ B0
2 , then one has simple zeros in the slow dynamics
and hence limit cycles near Γ are not possible.
We are now in a good position to prove Theorems 4.3 and 4.4.

5.3. Proof of Theorem 4.3. The symmetries SF and SP deﬁned, respectively, by
(51) and (52) imply that it suﬃces to prove Theorem 4.3 for B2 strictly positive.
Based on the discussion above, we distinguish three possibilities.

5.3.1. B2 ∈ K ⊂]0, 2[, K is any compact set. Our goal is to show that, by taking
U ∼ 0, R ∼ 0, R ≥ 0, ϵ ∼ 0 and ϵ ≥ 0, the left hand side of the equation (73) is
strictly negative for any B0 ∼ 0, B2 ∈ K and λ ∈ Λ. This implies that the equation
{LY δ = 0} has no solutions along {U R = r}, under the given conditions on the
parameters and variables, and for (R, ϵ) > (0, 0). Using the Rolle’s Theorem one
ﬁnds that the cyclicity of Γ at B2 ∈ K is bounded by one.
Consider ﬁrst the expression

ϵ2I(¯x(U, R, τ ), U R, τ ) − ϵ
2I(¯x(−U, R, τ ∗), −U R, τ ∗).

We may use Theorem 5.9 and results in [10], for B2 ∈ −K ∪K, to write the function
ϵ2I(¯x(U, R, τ ), U R, τ ) as

I(B2, U R, λ) + ϕ1(U, R, τ ) + ϕ2(U, R, τ )ϵ2 ln ϵ, (77)

2668 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

where ϕ1 and ϕ2 are C k-functions, including at ϵ = 0 and R = 0, ϕ1 = O(ϵ) and
where I(B2, r, λ) represents the slow divergence integral, deﬁned as:

I(B2, r, λ) = ∫ √2
R1

0
 wdw
−1 + B2w − w2 + rw3 ¯H(rw, λ) < 0. (78)

Using (77) we obtain that

ϵ2I(¯x(U, R, τ ), U R, τ ) − ϵ
2I(¯x(−U, R, τ ∗), −U R, τ ∗)

= I(B2, U R, λ) − I(−B2, −U R, λ) + ¯ϕ1(U, R, τ ) + ¯ϕ2(U, R, τ )ϵ2 ln ϵ, (79)

where ¯ϕ1 and ¯ϕ2 are C k-functions, including at ϵ = 0 and R = 0, and ¯ϕ1 = O(ϵ).
Taking into account (79) and Lemma 5.14 the equation (73) can be written as

I(B2, U R, λ) − I(−B2, −U R, λ) + C(U, R, B2, λ)

+ϵ̃L
∗(U, R, τ ) + ¯ϕ2(U, R, τ )ϵ2 ln ϵ = 0, (80)

for some new C k-function ̃L
∗ in (U, R, R ln R, τ ).

Remark 10. When B2 ∼ 0, we also deal with a regular slow dynamics and we may
hence use (80), where ̃L
∗ and ¯ϕ2 are identically zero by taking U = B0 = B2 = 0
(see Section 5.4).

Note that the left hand side of the equation (80) can be treated as a continuous
(including ϵ = 0) perturbation of I(B2, U R, λ) − I(−B2, −U R, λ) + C(U, R, B2, λ).
Hence it suﬃces to show that the ﬁrst line in (80) is strictly negative for B2 ∈ K,
λ ∈ Λ, U ∼ 0, R ∼ 0 and R ≥ 0.
Using the change of variables w = −w′ in I(−B2, −U R, λ), it can be easily seen
that
 I(B2, U R, λ) − I(−B2, −U R, λ)

= ∫ √
2
R1

− √2
R1
 wdw
−1 + B2w − w2 + U Rw3 ¯H(U Rw, λ) . (81)

Consider now

̃I(¯x, B2, r, λ) = ∫ ¯x

−¯x
 wdw
−1 + B2w − w2 + rw3 ¯H(rw, λ) , (82)

for B2 ∈ K, λ ∈ Λ and r ∼ 0. From Lemma 3.1 in [8] we know that for any ρ > 0
small there exist r0 > 0 and ν > 0 suﬃciently small such that ̃I(¯x, B2, r, λ) ≤ −ν
for ¯x ∈ [ρ, 1
ρ ], B2 ∈ K, r ∈ [−r0, r0] and λ ∈ Λ. If we take ρ = R1√2 , we get that (81)
is strictly negative for B2 ∈ K, λ ∈ Λ, U ∼ 0, R ∼ 0 and R ≥ 0.
To see that the ﬁrst line in (80) is strictly negative for B2 ∈ K, λ ∈ Λ, U ∼ 0,
R ∼ 0 and R ≥ 0, it suﬃces to observe that C(U, R, B2, λ) is, by Lemma 5.14,
strictly negative for B2 ∈ K, λ ∈ Λ, U ∼ 0, R ∼ 0 and R ≥ 0. Hence the cyclicity
of δ at B2 ∈ K is bounded by one.
To see that the cyclicity of Γ at B2 ∈ K is precisely one, we use Theorem 4.1.
We claim that there exists a C k-function b0(U, R, ϵ, B2, λ) ∼ 0, for B2 ∈ K, λ ∈ Λ,
(U, R, ϵ) ∼ (0, 0, 0), R ≥ 0 and ϵ ≥ 0, such that zeros of δ will occur for B0 =
b0(U, R, ϵ, B2, λ). In fact, since δ is C k (see Theorem 4.1), δ(U, R, 0, 0, B2, λ) = 0
and ∂δ
∂B0 (U, R, 0, 0, B2, λ) ̸= 0 (B0 is a breaking parameter), the implicit function
theorem implies existence of unique C k-function b0(U, R, ϵ, B2, λ) such that solution

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2669

of δ = 0, for ϵ ∼ 0 and B0 ∼ 0, can only occur for B0 = b0(U, R, ϵ, B2, λ). Hence
the cyclicity of Γ at B2 ∈ K is at least one.
Since the left hand side of the equation (80) is strictly negative, we deal with a
hyperbolically attracting limit cycle.

5.3.2. B2 ∼ 2. We invoke Lemma 5.14 and see that the function C in (73) is
bounded. Of course we have that ϵ̃L
∗ introduced in (73) is bounded due to the
fact that ̃L
∗ is C k in (U, R, R ln R, τ ). It remains to study ϵ2I(¯x(U, R, τ ), U R, τ ) −
ϵ2I(¯x(−U, R, τ ∗), −U R, τ ∗), i.e. the ﬁrst line in (73).
Since the slow dynamics (9) is regular for ¯x ≤ 0, the paper [4] shows us that
the contribution ϵ2I(¯x(−U, R, τ ∗), −U R, τ ∗) is bounded. Using [4] once more we
have that ϵ2I(¯x(U, R, τ ), U R, τ ) is dominated by the contribution of the saddle-node
singularity and it tends to −∞ as (U, R, B2, ϵ) → (0, 0, 2, 0).
Hence we ﬁnd that the cyclicity of Γ at B2 = 2 is bounded by one. Since the left
hand side of (73) is always negative for (U, R, B2, ϵ) near (0, 0, 2, 0), we deal with
a hyperbolically attracting limit cycle. We refer to Section 5.3.1 to see that the
cyclicity of Γ at B2 = 2 is one.

5.3.3. 2 < B2 ≤ B
0
2. The cyclicity of Γ in this case is zero.

5.4. Proof of Theorem 4.4. We suppose that ¯H(0, λ) ̸= 0 for all λ ∈ Λ. Our
goal is to solve equation (73) along the segment {(U, R)|U R = r, U ∼ 0, U > 0, R ∼
0, R > 0} for each ﬁxed (r, ϵ, B0, B2) ∼ (0, 0, 0, 0), r > 0, ϵ ≥ 0 and λ ∈ Λ. Remark
10 implies that the equation (73), for B2 ∼ 0, can be written as

I(B2, U R, λ) − I(−B2, −U R, λ) + C(U, R, B2, λ) + ̃̃L(U, R, τ ) = 0, (83)

where ̃̃L(U, R, τ ) is O(ϵ), C k in (U, R, R ln R, τ, ϵ
2 ln ϵ) and identically zero by taking
U = B0 = B2 = 0. Hence, we can write

̃̃L(U, R, τ ) = U G1(U, R, τ ) + B0G2(U, R, τ ) + B2G3(U, R, τ ), (84)

where Gi, i = 1, 2, 3, is O(ϵ) and C k in (U, R, R ln R, τ, ϵ
2 ln ϵ).
When U = B2 = 0, then I(B2, U R, λ) − I(−B2, −U R, λ) and C(U, R, B2, λ) are
identically zero. Based on (81), we have that

I(B2, U R, λ) − I(−B2, −U R, λ) = B2( − ∫ √
2
R1

− √2
R1
 w2dw
(1 + w2)2 + I1(U, R, τ )
)

+U R( − ¯H(0, λ) ∫ √2
R1

− √2
R1
 w4dw
(1 + w2)2 + I2(U, R, τ )), (85)

where I1 and I2 are O(U R, B2) and C ∞. Using (72) we obtain

C(U, R, B2, λ) = B2( − 4
√2 ∫ R1

R
 dR′

(2 + R′2)2 + η1(U, R, τ ))

+U ( − 8√2 ¯H(0, λ) ∫ R1

R
 RdR′

R′2(2 + R′2)2 + η2(U, R, τ )
), (86)

where η1 and η2 are O(U, B2) and C k in (U, R, R ln R, τ ) (see Lemma 5.14).

2670 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

Taking into account (84), (85) and (86), (83) changes to:

U ( − ¯H(0, λ)R ∫ √2
R1

− √
2
R1
 w4dw
(1 + w2)2 − 8√2 ¯H(0, λ) ∫ R1

R
 RdR′

R′2(2 + R′2)2 + G1(U, R, τ )
)

+ B2( − ∫ √2
R1

− √
2
R1
 w2dw
(1 + w2)2 − 4√2 ∫ R1

R
 dR′

(2 + R′2)2 + G3(U, R, τ ))

+ B0G2(U, R, τ ) = 0, (87)

for some new functions G1, G2, G3 that are O(U, B2, ϵ) and C k in the variable
(U, R, R ln R, τ, ϵ
2 ln ϵ).

Lemma 5.15. We have that

(i) −R ∫ √2
R1

− √2
R1
 w4dw
(1 + w2)2 − 8
√2 ∫ R1

R
 RdR′

R′2(2 + R′2)2 = −2√2 + f1(R)

and
 (ii) − ∫ √2
R1

− √2
R1
 w2dw
(1 + w2)2 − 4
√2 ∫ R1

R
 dR′

(2 + R′2)2 = − π
2 + f2(R),

where f1 and f2 are C ∞-functions in R and identically zero when R = 0.

Proof. We get

−R ∫ √
2
R1

− √
2
R1
 w4dw
(1 + w2)2 − 8√2 ∫ R1

R
 RdR′

R′2(2 + R′2)2

= −R( ∫ √
2
R1

− √2
R1
 w4dw
(1 + w2)2 + 2 ∫ √2
R

√
2
R1
 w4dw
(1 + w2)2 ) = −R ∫ √2
R

− √2
R
 w4dw
(1 + w2)2

= −
 √2(4 + 3R2)
(2 + R2) + 3RArcctg( R
√2 ) = −2
√2 + O(R),

where O(R) is a C ∞-function in R. In the ﬁrst step we used the change of variable:
w = √2
R′ . Similarly, we obtain

− ∫ √2
R1

− √
2
R1
 w2dw
(1 + w2)2 − 4√2 ∫ R1

R
 dR′

(2 + R′2)2

= − ∫ √2
R1

− √2
R1
 w2dw
(1 + w2)2 − 2 ∫ √
2
R

√2
R1
 w2dw
(1 + w2)2 = − ∫ √2
R

− √2
R
 w2dw
(1 + w2)2

=
 √2R
2 + R2 − Arcctg( R
√2 ) = − π
2 + O(R),

where O(R) is a C ∞-function in R.

With the help of Lemma 5.15 we infer that the equation (87) can be written as

U ( − ¯H(0, λ)2√2 + G1(U, R, τ )) + B0G2(U, R, τ )

+B2( − π
2 + G3(U, R, τ )
) = 0, (88)

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2671

for some new functions G1, G2, G3 that are O(U, R, B2, ϵ) and C k in the variable
(U, R, R ln R, τ, ϵ
2 ln ϵ). In order to be able to apply an algorithm of derivation-
division to the left hand side of (88), we have to get rid of the parameter B0 in
(88).
Again we invoke Theorem 4.1 and obtain that there exists a unique C k-function
b0(U, R, ϵ, B2, λ), for (U, R, ϵ, B2) ∼ (0, 0, 0, 0) and λ ∈ Λ, such that solutions of
δ(U, R, τ ) = 0, for ϵ ∼ 0 and B0 ∼ 0, can only occur for B0 = b0(U, R, ϵ, B2, λ).
Hence, it is suﬃcient to solve the following equation, with respect to variable R
(R > 0, R ∼ 0):
 δ( U2R2
R , R, ϵ, b0(U2, R2, ϵ, B2, λ), B2, λ) = 0, (89)

for each ﬁxed (U2, R2) > (0, 0), (U2, R2) ∼ (0, 0), ϵ > 0, ϵ ∼ 0, B2 ∼ 0 and
λ ∈ Λ. We will prove that there exist RP > 0, UP > 0, ϵ0 > 0, ̃B2 > 0 suﬃciently
small such that for each U2 ∈]0, UP [, R2 ∈]0, RP [, ϵ ∈]0, ϵ0], B2 ∈ [− ̃B2, ̃B2] and
λ ∈ Λ the equation (89) has at most two solutions (counting with multiplicity)
w.r.t. R ∈ [ U2R2
UP , RP ].
It can be easily seen that

−R ∂
∂R
 (δ( U2R2
R , R, τ )) = (LY δ)
( U2R2
R , R, τ ). (90)

Taking into account that {LY δ = 0} is equivalent, for R > 0 and ϵ > 0, to the

equation (88), (90) implies that { ∂
∂R (δ( U2R2
R , R, ϵ, b0(U2, R2, ϵ, B2, λ), B2, λ
)) = 0}
is equivalent, for R > 0 and ϵ > 0, to
U2R2
R
 ( − ¯H(0, λ)2√2 + G1( U2R2
R , R, ϵ, b0(U2, R2, ϵ, B2, λ), B2, λ)
)

+b0(U2, R2, ϵ, B2, λ)G2( U2R2
R , R, ϵ, b0(U2, R2, ϵ, B2, λ), B2, λ)

+B2( − π
2 + G3( U2R2
R , R, ϵ, b0(U2, R2, ϵ, B2, λ), B2, λ)) = 0, (91)

where G1, G2, G3 are identical to G1, G2, G3 introduced in (88).
Since δ(0, R, ϵ, 0, 0, λ) = 0 and δ(U, 0, ϵ, 0, 0, λ) = 0, we ﬁnd that
b0(0, R, ϵ, 0, λ) = 0 and b0(U, 0, ϵ, 0, λ) = 0.
Hence we can write b0 as:

b0(U2, R2, ϵ, B2, λ) = U2R2 ¯b0(U2, R2, ϵ, B2, λ) + B2 ̃b0(U2, R2, ϵ, B2, λ), (92)

where ¯b0 and ̃b0 are C k-functions.
Denote by ξ parameter (U2, R2, ϵ, B2, λ). Keeping in mind (92) the equation (91)
changes to
U2R2
R
 ( − ¯H(0, λ)2√2 + ¯G1(R, ξ)) + B2( − π
2 + ¯G2(R, ξ)
) = 0, (93)

where ¯G1 and ¯G2 are O( U2R2
R , R, B2, ϵ) and C k in ( U2R2
R , R, R ln R, ξ, ϵ2 ln ϵ).
Let us now recall the notion of a strict Chebyshev system of C k-functions of
degree one as it was introduced in [2].

Deﬁnition 5.16. Let F = {f0, f1} be a sequence of C k-functions deﬁned on an
interval [a, b] ⊂ R. One says that F is a strict Chebyshev system (in short, ST-
system) on [a, b] (of degree one) if one has that f0 ̸= 0 for all z ∈ [a, b] and ( f1
f0 )
′(z) ̸=
0 for all z ∈ [a, b].

2672 RENATO HUZAK, PETER DE MAESSCHALCK AND FREDDY DUMORTIER

In the next proposition, we give an essential property of ST-systems (of degree
one) that has been proven in [2].

Proposition 5.17. Let F = {f0, f1} be a ST-system on [a, b]. Let (α0, α1) ∈
R2 \ {(0, 0)} and let f = α0f0 + α1f1. Then the function f has at most one simple
zero on [a, b].

Let us write f0(R, ξ) = − π
2 + ¯G2(R, ξ)

and f1(R, ξ) = R−1( − ¯H(0, λ)2√2 + ¯G1(R, ξ)
).

In what follows, we prove that there exist RP > 0, UP > 0, ϵ0 > 0, ̃B2 > 0
suﬃciently small such that for each U2 ∈]0, UP [, R2 ∈]0, RP [, ϵ ∈ [0, ϵ0], B2 ∈
[− ̃B2, ̃B2] and λ ∈ Λ the system {f0(R, (U2, R2, ϵ, B2, λ)), f1(R, (U2, R2, ϵ, B2, λ))}
is a ST-system of degree one in the variable R ∈ [ U2R2
UP , RP ].
It is clear that f0 < 0 for ( U2R2
R , R, B2, ϵ) ∼ (0, 0, 0, 0). We have

f1
f0 = R−1(
ϑ1 + ̃G1(R, ξ)
) (94)

where ϑ1 = ¯H(0, λ)4
√2
π and where ̃G1 is an O( U2R2
R , R, B2, ϵ)-function and C k in

( U2R2
R , R, R ln R, ξ, ϵ2 ln ϵ). We can write
̃G1(R, ξ) = ̃g1( U2R2
R , R, R ln R, ξ, ϵ2 ln ϵ),

where ̃g1 is a C k-function. Applying ∂
∂R to (94) we get

R−1( − U2R2
R2 ∂1̃g1 + ∂2̃g1 + (1 + ln R)∂3̃g1) − R−2(ϑ1 + ̃g1)

= R−2( − ϑ1 − U2R2
R ∂1̃g1 + R∂2̃g1 + R(1 + ln R)∂3̃g1 − ̃g1), (95)

where ̃g1 and its derivatives are calculated in ( U2R2
R , R, R ln R, ξ, ϵ2 ln ϵ). The ex-
pression in (95) is non-zero by taking ( U2R2
R , R, ϵ, B2) ∼ (0, 0, 0, 0).
Using the Rolle’s Theorem one ﬁnds that the cyclicity of δ at B2 = 0 is bounded
by two. This completes the proof of Theorem 4.4.

REFERENCES

[1] P. De Maesschalck and F. Dumortier, Slow-fast Bogdanov-Takens bifurcations, J. Diﬀerential
Equations, 250 (2011), 1000–1025.
[2] F. Dumortier and R. Roussarie, Birth of canard cycles, Discrete Contin. Dyn. Syst. Ser. S ,
2 (2009), 723–781.
[3] P. De Maesschalck and F. Dumortier, Singular perturbations and vanishing passage through
a turning point, J. Diﬀerential Equations, 248 (2010), 2294–2328.
[4] P. De Maesschalck and F. Dumortier, Canard cycles in the presence of slow dynamics with
singularities, Proc. Roy. Soc. Edinburgh Sect. A, 138 (2008), 265–299.
[5] F. Dumortier, R. Roussarie, J. Sotomayor, and H. Zoladek, Bifurcations of Planar Vector
Fields, Lecture Notes in Mathematics, 1480, Springer-Verlag, Berlin, 1991.
[6] Freddy Dumortier, Compactiﬁcation and desingularization of spaces of polynomial Li´enard
equations, J. Diﬀerential Equations, 224 (2006), 296–313.
[7] Robert Roussarie, Putting a boundary to the space of Li´enard equations, Discrete Contin.
Dyn. Syst., 17 (2007), 441–448.
[8] R. Huzak, P. De Maesschalck and F. Dumortier, Limit cycles in slow-fast codimension 3 saddle
and elliptic bifurcations, J. Diﬀerential Equations, 255 (2013), 4012–4051.

CANARD CYCLES IN SLOW-FAST CODIMENSION 3 ELLIPTIC BIFURCATIONS 2673

[9] Peter De Maesschalck and Freddy Dumortier, Detectable canard cycles with singular slow
dynamics of any order at the turning point, Discrete Contin. Dyn. Syst., 29 (2011), 109–140.
[10] P. De Maesschalck and F. Dumortier, Time analysis and entry-exit relation near planar turn-
ing points, J. Diﬀerential Equations, 215 (2005), 225–267.
[11] P. Bonckaert, P. De Maesschalck and F. Dumortier, Well adapted normal linearization in
singular perturbation problems, J. Dynam. Diﬀerential Equations, 23 (2011), 115–139.
[12] M. Krupa and P. Szmolyan, Relaxation oscillation and canard explosion, J. Diﬀerential Equa-
tions, 174 (2001), 312–368.
[13] Daniel Panazzolo, Desingularization of nilpotent singularities in families of planar vector ﬁelds,
Mem. Amer. Math. Soc., 158 (2002).
[14] J. Llibre, A survey on the limit cycles of the generalized polynomial Li´enard diﬀerential
equations, Mathematical models in engineering, biology and medicine, AIP Conf. Proc., 1124
(2009), 224–233.

Received October 2013; revised April 2014.

E-mail address: renato.huzak@uhasselt.be
E-mail address: peter.demaesschalck@uhasselt.be
E-mail address: freddy.dumortier@uhasselt.be
