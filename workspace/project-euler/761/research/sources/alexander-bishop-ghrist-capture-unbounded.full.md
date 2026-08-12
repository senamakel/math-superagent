<!-- source: https://www2.math.upenn.edu/~ghrist/preprints/convexcapture.pdf | converted from PDF -->

CAPTURE PURSUIT GAMES ON UNBOUNDED DOMAINS

S. ALEXANDER, R. BISHOP, AND R. GHRIST

ABSTRACT. We introduce simple tools from geometric convexity to analyze capture-
type (or “Lion and Man”) pursuit problems in unbounded domains. The main result is
a necessary and sufﬁcient condition for eventual capture in equal-speed discrete-time
multi-pursuer capture games on convex Euclidean domains of arbitrary dimension and
shape. This condition is presented in terms of recession sets in unit tangent spheres.
The chief difﬁculties lie in utilizing the boundary of the domain as a constraint on the
evader’s escape route. We also show that these convex-geometric techniques provide
sufﬁcient criteria for pursuit problems in non-convex domains with a convex decom-
position.
 1. INTRODUCTION

Games of pursuit and evasion are among the oldest and most elegant problems in
game theory, osculating differential equations, control theory, differential geometry,
and graph theory. This paper focuses on global geometric features of capture-type
pursuit problems. The primary contribution is an introduction of tools from geometric
convexity which allow for results so general as to be independent of the number of
pursuers, and the dimension and (to a lesser extent) the geometry of the playing ﬁeld.

1.1. Of lions and men. The history of pursuit-evasion games is rich, with the earliest
formal problems being inspired by naval exploits [3]. Isaac’s text [12] is the classical
source for the early survey of the ﬁeld, with a focus on differential methods. A more
recent text by Nahin [25] gives a colloquial overview with more colorful history.

The particular pursuit problem considered in this paper goes under the name of Lion
& Man. The original Lion & Man problem (attributed to Rado in the 1930s) involves a
single pursuer chasing a single evader at equal speeds in continuous time on a domain
D equal to a planar Euclidean disc. In this well-known setting, it was a surprise to ﬁnd
that the evader can win if the pursuer keeps on the radius to the evader (see Little-
wood’s geometric proof [21] of Besicovich’s 1952 result and the subsequent paper of
Croft [6]). This problem was generalized by Flynn [8] to account for different speed ra-
tios and solved via differential methods. More recent treatments of the problem appear
in [20, 2, 33, 17].

Research supported by DARPA SToMP # HR0011-07-1-0002 and NSF MSPA-MCS # 0528086.

1

2 S. ALEXANDER, R. BISHOP, AND R. GHRIST

Although pursuit games are traditionally played on a planar Euclidean domain, there
are examples of more general playing ﬁelds, such as graphs [26], spheres [18, 32], sur-
faces of revolution [22, 10], Euclidean halfspaces [15], hypersurfaces of Euclidean space
[31], and general compact CAT(0) metric spaces [1]. The geometry of a playing ﬁeld
has been used as a parameter in proving computational complexity of certain pursuit
games [27, 19]. Necessary and sufﬁcient capture criteria are rare, sufﬁciency being
more common in the literature. The focal point of this paper is a necessary and sufﬁ-
cient criterion for capture which applies to general convex Euclidean domains.

1.2. Assumptions. The following are ﬁxed assumptions for all but the ﬁnal sections of
this paper.

(1) D is a closed unbounded convex Euclidean domain with boundary.
(2) There is a single evader E and N pursuers {Pj}N
1 , represented as points with
initial locations E0 and {P 0
j } respectively.
(3) For each t ∈ N, the evader jumps from location Et to Et+1, a point within unit
distance of Et. Then, each pursuer may jump from P t
j to P t+1
j , at most a unit
distance.
(4) The evader E wins the game if P t
j ̸= Et for all t and j.
(5) Each pursuer Pj has perfect information about D and about its current position
P t
j and that of the evader Et+1.

The principal result of this paper is a necessary and sufﬁcient condition for the pur-
suers to win, regardless of evader strategy, as a function of E0, {P 0
j }, and D.

1.3. Notation. We ﬁx the following standard notation. Euclidean n-dimensional space
is denoted En with norm ∥ · ∥. We choose n so that D has nonempty interior, that is,
D lies in no hyperplane of En. The unit sphere in En is Sn−1 = {x ∈ En : ∥x∥ = 1}.
Given two points P and Q in En, the line containing them is denoted P Q, the segment
between them P Q, and the distance between them |P Q|. Assuming P ̸= Q, let [P Q] ∈
Sn−1 denote the unit vector −−→
P Q/ |P Q|. The closed ball of radius r about a point O ∈ En

is denoted B(O, r). A cone with central angle α is the union of all rays from a point
making angle ≤ α with a ﬁxed ray.

We may abuse notation and use E to denote either the evader or an evader’s initial
position, E0. The same holds for pursuers, using Pj instead of the more cumbersome
P 0
j .
 2. PRIOR AND PRESENT RESULTS

We detail known results for Lion & Man problems, graded as a function of domain
characteristics. In all cases, the assumptions of §1.2 are in effect.

CAPTURE PURSUIT GAMES ON UNBOUNDED DOMAINS 3

2.1. Compact domains. When D is compact, there is no route of escape, and the evader
is always captured. No intricate strategy is required: the greedy strategy of having the
pursuer move along the geodesic path to the evader’s present location is efﬁcacious if
not efﬁcient. For compact convex domains, this is an exercise for the reader. The greedy
strategy works as well for any compact CAT(0) domain (a geodesic metric space whose
curvature – as measured by comparison triangles – is nowhere positive): see [1] for de-
tails.

2.2. No boundaries. In the case where D = En, there is an obvious necessary and
sufﬁcient criterion for capture:

(⋆) E is in the interior of the convex hull of {Pj }N
1 .

That this is necessary and sufﬁcient has been discovered and rediscovered in various
contexts within the literature. See, in particular, [6, 11, 36, 17, 28]. The perspective of
the present paper is to incorporate the boundary of the domain as a type of stationary
pursuer, whose geometry affects the success of a given pursuit strategy. This greatly
impacts strategy and feasibility of capture, as it is possible for the pursuers to corner
the evader.

2.3. Radius: one pursuer. The paper of Sgall [33] solves a Lion & Man problem on the
closed ﬁrst quadrant Q = {(x1, x2) ∈ E2 : xi ≥ 0}. All the assumptions of §1.2 hold
with D = Q and N = 1. For this case, Sgall shows that the pursuer can win if and only
if
 (⋆) The set {z ∈ Q : ∥zE∥ ≤ ∥zP ∥} is bounded.

The resulting algorithm is denoted Spheres in [17]: we will refer to it as Radius, fol-
lowing the terminology of Croft’s 1964 paper [6] (hearkening back to the earlier work
of Besicovich, Littlewood, and Rado). The algorithm proceeds as follows. Let O denote
a center: a point on the ray with end E through P , not between E and P , such that the
component of Q − B(O, |OP |) which contains E is bounded. The existence of a center
O follows from (⋆). The algorithm produces P t+1 from P t and Et+1 by choosing the
point that lies within unit distance of P t and closest to Et+1 along the segment OEt+1.

Algorithm 1 P ′ = Radius(P, E′, O)

Require: |P E′| > 1

1: P ′ ⇐ point on OE′ ∩ B(P, 1) closest to E′

2: return P ′

Sgall proves that for D = Q, Radius always succeeds in a ﬁnite number of moves for
systems satisfying (⋆), and that a quadratic number of moves in |OP | is a sharp upper
bound. It is remarked at the end of the proof that the result and proof generalize from
the quadrant Q to any planar wedge of angle < π, as well as to higher-dimensional
convex Euclidean cones, with the obvious modiﬁcation to (⋆) above. However, Sgall

4 S. ALEXANDER, R. BISHOP, AND R. GHRIST

fails to notice that there is a distinction between wedges of angle < π/2 and those with
angle ≥ π/2: for the latter (⋆) implies that the center must be in Q, but this is no longer
true for the former. We demonstrate in §4.1 if the angle < π/2, his algorithm may fail
to work because it may require the pursuer to move outside the domain.

2.4. Radius: multiple pursuers. The paper of Kopparty and Ravishankar [17] consid-
ers the broader setting of N pursuers in a convex Euclidean domain in dimension n
bounded by ﬁnitely many hyperplanes. Their main result is an extension of the proof
of Sgall that the Radius algorithm works in this setting. Condition (⋆) above general-
izes in the following manner:

(⋆) E is in the interior of the convex hull of {Pj}N
1 ∪ {Fk}M
1 where Fk is the orthog-
onal projection of E onto the kth bounding hyperplane of D.

Their algorithm is a simple extension of Sgall’s: choose N centers Oj for E and the Pj
such that the set D − ∪jB(Oj, |OjPj|) has a bounded component containing E. Discard
the pursuers Pj for which the ray from E through Pj intersects the boundary of D,
and evolve via P ′
j = Radius(Pj, E, Oj ). Theorem 3 of [17] claims that Radius leads to
successful capture, assuming (⋆) holds at time t = 0: see Figure 1.

P t
1 P t+1
1
 P t
2

P t+1
2

Et
 Et+1

O1
 O2

D

FIGURE 1. One Radius step makes positive progress along the radial
direction from center Oj. (Note: centers O1, O2 and lengths not drawn
to scale.)

Their paper has additional results, including a modiﬁed algorithm called Planes, which
is guaranteed to work only in the case of D = En (as does Radius, albeit more slowly).

CAPTURE PURSUIT GAMES ON UNBOUNDED DOMAINS 5

2.5. New results. We show the following.

(1) The conditions (⋆) above all generalize to a Boundedness Condition applicable
to arbitrary convex Euclidean domains.
(2) The application of Radius is invalid on general convex Euclidean domains (even
2-d cones), contradicting the claims of [33] and [17]. However, there exists a
(restrictive) additional geometric assumption under which the proofs of [17]
become valid. This condition is not needed when there is a single pursuer and
the domain D diverges to inﬁnity on a wide enough set of directions.
(3) The Boundedness Condition is necessary and sufﬁcient for the existence of a
successful pursuit strategy (RotatingRadius) on convex Euclidean domains (not
merely those with piecewise-linear boundaries).
(4) The Boundedness Condition gives a sufﬁcient capture criterion on non-convex
Euclidean domains which are expressed as a ﬁnite union of convex domains.
The same algorithm RotatingRadius is played in a parallel projected fashion on
the convex components.

All mathematical tools used are very elementary ideas from Euclidean, spherical and
convex geometry.
 3. ELEMENTARY GEOMETRY

This section covers basic deﬁnitions from convex geometry [29] and culminates in a
general reformulation of the Boundedness Condition. For the remainder of this section,
assume D is a convex Euclidean domain.

Deﬁnition 1. A Euclidean domain D with a conﬁguration of one evader E and N pursuers
{Pj}N
1 satisﬁes the Boundedness Condition if the intersection

(1)
 

 N⋂

j=1 Hj


 ∩ D is bounded,

where Hj is the closed halfspace containing E whose boundary hyperplane passes through Pj
orthogonal to EPj.

In this section, we reformulate this condition in terms of spherical convexity [7]. (One
could just as easily work with cones in the non-normalized setting, but we prefer think-
ing in terms of visibility spheres.)

Deﬁnition 2. A subset A ⊂ Sn−1 of the unit sphere in En is said to be convex if the cone
over A, C(A) = {v ∈ En : v = λx for some x ∈ A, λ ∈ [0, ∞)}
is a convex subset of En.

Remark 3. A great k-sphere in Sn−1, for 0 ≤ k ≤ n−1, being by deﬁnition the intersection
of Sn−1 with a (k + 1)-plane through the origin, is a convex subset of Sn−1 according to
our deﬁnition. In particular, when k = 0, a pair of antipodal points is a convex subset.

6 S. ALEXANDER, R. BISHOP, AND R. GHRIST

Given D, we can encode the constraints imposed by the boundary as well as the possi-
ble avenues of escape in terms of dual convex subsets of the unit sphere.

Deﬁnition 4. Given D ⊂ En, the normals set, N , is the subset of Sn−1 containing all
the outer unit normal vectors to support hyperplanes in En which intersect D but not its
interior.

It is worth noting a point that many authors have misstated: the set of outer unit nor-
mals used in this deﬁnition is not necessarily convex, though its closure N is. See [38]
for an example where this distinction is critical.

Deﬁnition 5. The dual A0 of a convex set A ⊂ Sn−1 is the set of all unit vectors v making
angle ≥ π/2 with every vector in A.

Then A0 is a closed convex set, and A00 is the closure of A.

Deﬁnition 6. The recession set of D, R, is the subset of Sn−1 containing all unit vectors in
the directions of half-lines lying in D.

The following lemma is well known and easy to prove (see [29, p. 123, Corollary
14.2.1]). We denote the closed hemisphere with pole x in Sn−1 by Hx.

Lemma 7. For D ⊂ En convex, N 0 = R. Equivalently, x ∈ R if and only if H−x ⊃ N .

The encoding of the boundary (N ) and the directions of escape (R) are thus dual. In the
special case when N is the empty set (that is, D = En), its dual R = Sn−1 is the entire
unit sphere, in accordance with Deﬁnition 6. On the other hand, when D is compact,
then R is empty and N = Sn−1.

Lemma 8. For D ⊂ En convex, N lies in a closed hemisphere of Sn−1 if and only if D is
unbounded.

Proof. The closure of N , being convex and nonempty, either lies within a closed hemi-
sphere of Sn−1 or coincides with Sn−1. By Lemma 7, the latter case occurs if and only
if R is empty, hence if and only if D is bounded. ⋄

The following is a general reformulation of the Boundedness Condition in terms of
recession sets and normals sets. Recall [EPj ] denotes the unit vector in the direction
from E to Pj.

Theorem 9. The following are equivalent:

(1) D ⊂ En satisﬁes the Boundedness Condition.
(2) No closed hemisphere of Sn−1 contains N ∪ {[EPj ]}N
1 .
(3) The union of the open hemispheres in Sn−1 with poles [EPj ] contains R.
(4) The spherical convex hull of N ∪ {[EPj ]}N
1 equals Sn−1.

CAPTURE PURSUIT GAMES ON UNBOUNDED DOMAINS 7

P1
 P2

E
 R

N
 D

FIGURE 2. The geometry of the domain and the pursuers is encoded
in the visibility (unit tangent) sphere at E: pictured is the recession set
R, its dual the normals set N , and the perceived locations of the pur-
suers [EPj]. The Boundedness Condition is equivalent to saying that
the spherical convex hull of N and the [EPj ] is the entire visibility
sphere.

Proof. The equivalence of the Boundedness Condition with (2) above follows from
Lemma 8 applied to the set given by the intersection of D with the appropriate halfs-
paces as in Deﬁnition 1. The equivalence of Conditions (2) and (3) follows from Lemma
7, since x ∈ ∪jint H[EPj] for every x ∈ R if and only if for every hemisphere H−x con-
taining N we have [EPj] ∈ int Hx for some j. The equivalence of (2) and (4) follows
from Deﬁnition 2. ⋄

Note that this result specializes in the case of D = En: the evader must lie in the interior
of the convex hull of the pursuers.

The Boundedness Condition means that the evader cannot simultaneously move away
from the boundary of the playing ﬁeld and all the pursuers. If the evader ever can,
then, of course, the evader wins.

Proposition 10. The Boundedness Condition is a necessary condition for the existence of a
successful pursuit strategy.

Proof. If the Boundedness Condition fails, then all of the vectors [EPj ] together with
N lie within a single hemisphere H of Sn−1, thanks to Theorem 9. Let v be the unique
vector in Sn−1 dual to H. By deﬁnition, v ∈ R. Moving E in the direction v has an in-
ﬁnite trajectory which furthermore never decreases the distance to any Pj (as a trivial
calculation shows). ⋄

8 S. ALEXANDER, R. BISHOP, AND R. GHRIST

4. BOUNDARY EFFECTS AND Radius

We consider carefully under which circumstances the Radius algorithm of [17, 33] is
valid and effective.

4.1. When Radius fails. The ﬁrst step of Radius in [17, p. 120] is to discard all the pur-
suers Pj for which the ray EPj intersects a bounding hyperplane of D, or equivalently,
for which [EPj ] /∈ R. However, the Boundedness Condition may fail to be preserved
under this step; worse, all the pursuers may be discarded. On the other hand, if the
discarding step is omitted, the algorithm may move pursuers out of the playing ﬁeld.
Figure 3 gives a planar example involving a single pursuer.
 O
 P t

Et

P t+1

Et+1

R

N
 U
 D D

FIGURE 3. For a thin cone, the recession set R and the hemispheres
set U (see Deﬁnition 14) do not partition the unit tangent sphere [left].
Consequently, the Radius algorithm can fail, in this case [right] by de-
manding that P t+1 lie outside of D. (Note: the point O is not drawn at
the appropriate distance to D for scale purposes.)

Remark 11. It may be argued that the chances of having pursuers ‘tricked’ into a bound-
ary collision via Radius is rare; or that this is a result of a degenerate set of initial condi-
tions; or still that the difference between where Radius and where the laws of physics
demand a pursuer go are too small to affect the outcome of the game. In dimension
two, such consideration might have validity. However, as the dimension of the domain
D increases, the possibilities for mischief on the part of an adversarial evader increase
dramatically. Consider the example of a domain D whose recession set is very thin.
For example, in 3-d, this would correspond to a domain with minimal cone angle near
zero and maximal cone angle near π, as in Figure 4. In the case of several pursuers be-
ginning near the boundary and which just barely satisfy the Boundedness Condition,
it is possible for the evader to ‘zig-zag’ and force pursuers to collide into the boundary
at many/all time steps. Small errors in progress induced by these boundary effects
could presumably accumulate under such an evader strategy.

CAPTURE PURSUIT GAMES ON UNBOUNDED DOMAINS 9

O1O2
 P1P2
 E

FIGURE 4. A higher-dimensional convex domain with a thin but long
recession set could lead to a situation in which boundary collisions are
prevalent.

Further generalizations of this example to domains which have several independent
cone angles close to π along with several close to zero could prove more challenging,
since the evader has multiple directions in which to escape, while pursuers can expe-
rience a boundary collision at many time steps.

4.2. When Radius works. If no pursuers are discarded but the evader always moves
so that the Radius algorithm leaves them in D, then the evader is captured. Thus in
Figure 1, even if the evader moves steadily in the recession direction that makes angle
π/4 with the positive x and y axes, the escape route will be blocked. The following
is a corrected version of Theorem 3 of [17]. The proof that Radius works in this re-
stricted case follows the proof of [17] exactly. We include a careful proof for the sake of
completeness.

Theorem 12. For any convex unbounded D, the pursuers win if (1) the Boundedness Condi-
tion holds and (2) [EPj] ∈ R for all j.

Proof. Condition (2) implies that Oj ∈ D for all j, and P t+1
j =Radius(P t
j , Et+1
j , Oj )
returns a value in D, since P t+1
j lies on the segment OjEt+1 ⊂ D. Since the colinearity
and order of the triples (Et, P t
j , Oj) are maintained as a function of t, the evader must
remain for all t within the (bounded!) domain of Eqn. (1). However, since the angle
∠OP t
j P t+1
j is obtuse and |P t
j P t+1
j | = 1, the Law of Cosines implies that

|OjP t+1
j |
2 > |OjP t
j |
2 + 1,

10 S. ALEXANDER, R. BISHOP, AND R. GHRIST

implying the eventual capture of E. ⋄

Remark 13. It is permissible to discard any number of pursuers ab initio, so long as the
Boundedness Condition holds with the remaining pursuers.

In the case of a single pursuer P , we can present a simple condition on the playing
ﬁeld D that guarantees the success of Radius.

Deﬁnition 14. For a ﬁxed domain D, let U denote the union of all closed hemispheres in Sn−1

that contain N .

By Theorem 9, the Boundedness Condition in the single pursuer case becomes [EP ] /∈
U.

Lemma 15. Assume there is a single pursuer P , and that R ∪ U = Sn−1. Then the pursuer
wins following Radius if the Boundedness Condition holds.

Proof. Since R ∪ U = Sn−1, the Boundedness Condition [EP ] /∈ U implies [EP ] ∈ R,
and so the hypotheses of Theorem 12 are satisﬁed. ⋄

If the condition of Lemma 15 fails, then Radius may fail, as the planar example in
Figure 3 illustrates.

Theorem 16. In the case of a single pursuer, if D contains a cone with central angle at least
π/4, then the Boundedness Condition guarantees capture via Radius.

Proof. Suppose D contains a cone with central angle π/4. Equivalently, R contains a
spherical disk of radius π/4 centered on some unit vector v (that is, all unit vectors
making angle ≤ π/4 with v). Since R and N are dual, the set N must be contained in
a spherical disk of radius π/4 about −v. It follows that U, the union of all closed hemi-
spheres containing N , contains the spherical disk of radius 3π/4 about −v. Therefore
R ∪ U = Sn−1, as desired. Lemma 15 completes the proof. ⋄

When D does not contain a sufﬁciently large subcone, it is still possible to ensure cap-
ture, as we demonstrate in the next section.

5. SUFFICIENCY OF THE BOUNDEDNESS CONDITION

We introduce Algorithm RotatingRadius to resolve the deﬁciencies of Radius and pro-
vide a complete characterization of when capture is possible. From Theorem 12 we
see that the Radius algorithm works if {[EPj ]}N
1 ⊂ R. In this case, under the Radius
algorithm, each pursuer Pj computes a center Oj on the line EPj and moves radially
away from this center. The centers Oj are ﬁxed throughout the game, and the evader
is blocked from entering a family of expanding concentric spheres about each Oj.

CAPTURE PURSUIT GAMES ON UNBOUNDED DOMAINS 11

However, in the case where [EPj] /∈ R, Radius may move a pursuer P t
j to a position
P t+1
j outside D. When this occurs, the strategy of the RotatingRadius algorithm is to
recalculate P t+1
j to lie in D, using nearest-point projection. RotatingRadius then recal-
culates the center Ot+1
j , changing the blocking sphere so that the new one continues to
contain the old one even though they are no longer concentric. The key is to show this
may be done while keeping the radii of the blocking spheres bounded.

Theorem 17. Discrete-time equal-speed capture on a convex domain D is achievable if and
only if the initial positions of the pursuers and evader satisfy the Boundedness Condition.

5.1. The RotatingRadius algorithm. One begins by discarding those pursuers {Pj} for
which [EPj ] ∈ N . By Theorem 9, this move preserves the Boundedness Condition.
After the evader moves from Et to Et+1, each pursuer P t
j and its corresponding center
Ot
j is updated according to (P t+1
j , Ot+1
j ) =RotatingRadius(P t
j , Et, Ot
j, D). See Figure 5.

O

O′

P ′′

P ′′
 P ∗

P ∗
 P ′

P ′ P

E

E′
 H∗

H∗

D

FIGURE 5. The RotatingRadius algorithm deals with boundary colli-
sions in Radius by projecting P ′′ to P ∗ in the boundary ∂D and then
moving the center O to O′ with P ′ placed along E′O′.

5.2. Radial progress. For Radius, Sgall bases his estimate of capture time on the fol-
lowing estimate, which we adapt to RotatingRadius.

Lemma 18. If P t+1
j ̸= Et+1,
 |Ot
jP t
j |
2 + 1 < |Ot+1
j P t+1
j |
2.

Proof. Set P = P t
j . Since |EE′| ≤ 1, the distance from any point M of the interior of the
segment E′O to the line EO is < 1. Taking M such that P M ⊥ EO we see that there
are two points on E′O at distance 1 from P , and the one, P ′′, nearest to E′ forms an
obtuse angle ∠OP P ′′. Hence by the Law of Cosines, |OP |2 + 1 < |OP ′′|2. If P ′′ ∈ D,
then P t+1
j = P ′′ and we are done.

12 S. ALEXANDER, R. BISHOP, AND R. GHRIST

Algorithm 2 (P ′, O′) = RotatingRadius(P, E′, O, D)

Require: |P E′| > 1
1: P ′′ ⇐ Radius(P, E′, O)
2: if P ′′ ∈ D then
3: P ′ ⇐ P ′′

4: O′ ⇐ O
5: else
6: P ∗ ⇐ projection of P ′′ to D

7: P ′ ⇐ point on P ∗E′ ∩ B(P, 1) closest to E′

8: O′ ⇐ point on the ray −−→
E′P ′ with |E′O′| = |E′O|
9: end if
10: return (P ′, O′)

Otherwise we continue the algorithm by letting P ∗ be the nearest point in D to P ′′

(clearly |P P ∗| < 1), and letting H∗ denote the halfspace containing D and bounded by
the support hyperplane to D at P ∗ that is orthogonal to P ′′P ∗ . Then P ′ = P t+1
j is the
unique point on the segment E′P ∗ at distance 1 from P . Since E′ ∈ D and P ′′ /∈ D,
then E′ is in H∗ and so ∠E′P ∗P ′′ ≥ π/2. Hence |P ∗E′| < |P ′′E′|. Since |E′O′| = |E′O|,
we have

(2) |O′P ′|
2 > |O′P ∗|
2 > |OP ′′|
2 > |OP |
2 + 1.
 ⋄

5.3. A decreasing playing ﬁeld. Consider the closed ball Bt
j = B(Ot
j, |Ot
j P t
j |). Let Ct

be the component of (D − ∪jBt
j) containing Et. We prove that Ct is strictly mono-
tonically decreasing under the RotatingRadius algorithm, thus providing a set-valued
Lyapunov function.

Lemma 19. cl Ct+1 ⊂ Ct for every t.

Proof. In this proof, we ﬁx j and continue the notation of §5.1. Set Bt = Bt
j = B(Ot
j, |Ot
j P t
j |),
and let St be the boundary sphere of Bt. When P ′′ = P t+1
j , we have O = O′, so by
Lemma 18, Bt+1 is concentric with and larger than Bt. Otherwise we show that the
ball Bt+1 about O′ includes the intersection of D with the ball Bt about O, that is,

(3) (Bt+1 ∩ D) ⊃ (Bt ∩ D).

Consider two concentric spheres with center O′: St+1 through P ′ and S with radius
|OP ′′|. We also have two concentric spheres with center O: St through P and S′′

through P ′′. By (2), the corresponding balls satisfy Bt+1 ⊃ B and B′′ ⊃ Bt. There-
fore (3) will follow from

(4) (B ∩ D) ⊃ (B′′ ∩ D).

CAPTURE PURSUIT GAMES ON UNBOUNDED DOMAINS 13

Since S and S′′ have the same radius, their intersection S ∩ S′′ is an (n − 2)-sphere S′

centered at the midpoint of the segment OO′ and lying in the perpendicular bisecting
hyperplane of that segment. Let H
′ be the halfspace containing O′ and bounded by
this perpendicular bisector. Then

(B ∩ H′) ⊃ (B′′ ∩ H′).

Therefore (4) will follow in turn from

(5) (B′′ ∩ D) ⊂ H
′,

since then (B ∩ D) ⊃ (B ∩ H′ ∩ D) ⊃ (B′′ ∩ H′ ∩ D) ⊃ (B′′ ∩ D).

By construction, P ′′P ∗ is the shortest join from P ∗ to D, so D lies in the half-space H∗

bounded by the support hyperplane to D at P ∗ that is orthogonal to P ′′P ∗. Thus (5)
will follow from

(6) (B′′ ∩ H∗) ⊂ H′,

which we now verify.

The centers O and O′ of B′′ and B, respectively, and the point E′ all lie on a 2-plane
T orthogonal to the bounding hyperplane of H′. Moreover, T is also orthogonal to the
bounding hyperplane of H
∗ since P ′′ and P ∗ lie on T . By symmetry, it sufﬁces to verify
(6) when B′′, H∗ and H
′ are reinterpreted as their respective intersections with T .

Thus we regard H
∗ as a halfplane bounded by a support line at P ∗ for D ∩ T , and
H′ as the halfplane containing O′ bounded by the perpendicular bisecting line of OO′.
Similarly, S ∩ S′′ is an intersection of two circles, of equal radius and with centers at
equal distance from E′, and consists of two points on the bisecting line.

Because ∠E′P ∗P ′′ is obtuse, |E′P ∗| < |E′P ′′|. Since |E′O| = |E′O′|, then |O′P ∗| >
|OP ′′|, that is, P ∗ lies outside B. Since P ∗ ∈ H
′ and (B ∩ H) ⊃ (B′′ ∩ H), then P ∗

lies outside B ∪ B′′. Therefore the segment segment P ∗P ′′ lies except for its righthand
endpoint outside B ∪B′′. It follows that B′′ ∩H
∗ cannot leave H′, since on the bounding
line of H′, the intersection point with the bounding line of H∗ is separated from S ∩ S′′

by the intersection point with P ∗P ′′. ⋄

5.4. Proof of Theorem 17.

Proof. If Ot+1
j ̸= Ot
j, the closed halfspace Ht+1
j containing Ot+1
j and bounded by the

perpendicular bisecting hyperplane of Ot
jOt+1
j consists of the points of En that are no
further from Ot+1
j than from Ot
j.

Choose a point Qj ∈ (B0
j ∩ D). By (3), Qj ∈ (Bt
j ∩ D) for all t. Thus, in the notation of
the preceding section, we always have Qj ∈ B′′j. Since Qj ∈ D and H∗
j is a supporting

14 S. ALEXANDER, R. BISHOP, AND R. GHRIST
 O
 O′

P ′′

P ∗P ′
 S = ∂B

S′′ = ∂B′′

P

E′
 H∗

D
 St = ∂Bt
St+1 = ∂Bt+1
 H ′

FIGURE 6. Progress in the RotatingRadius algorithm is proved by
demonstrating a nestedness property for balls Bt intersected with D.

halfspace for D, we also have Qj ∈ H∗
j . But then by (6), Qj ∈ H
t+1
j for all t. Therefore
the distance |QjOt
j| is nonincreasing in t.

The lengths |QjOt
j| are uniformly bounded for all t, as are the lengths |QjEt| by Lemma
19. Therefore the lengths |Ot
jEt| are uniformly bounded in t as well. By Lemma 18,

(7) |Ot
jEt|
2 ≥ |Ot
jP t
j |
2 ≥ |O0
j P 0
j |
2 + t.

Therefore capture occurs. ⋄

5.5. Quadratic estimate. The proof of Theorem 17 yields the following estimate, just
as in the setting of [33, 17].

Corollary 20. Under the Boundedness Condition, if Qj ∈ (B0
j ∩ D), then the pursuers catch
the evader in time

t < min
j
 [(
|QjO0
j | + max{|Qjx| : x ∈ C0
j }
)2 − |O0
j P 0
j |
2] .

Proof. For each j, the time of capture t satisﬁes

|O0
j P 0
j |
2 + t < |Ot
j P t
j |
2 ≤ (|Ot
jQj| + |QjP t
j |
)2 ≤ (|QjO0
j | + max{|Qjx| : x ∈ C0
j }
)2 .

The ﬁrst inequality is from (7), and the last is by the nonincreasing property of |QjOt
j|
and Lemma 19. ⋄

CAPTURE PURSUIT GAMES ON UNBOUNDED DOMAINS 15

6. NONCONVEX DOMAINS: CONVEX DECOMPOSITION

The tools used in the proofs of this paper are intimately linked to convexity, making the
prospects for extending Theorem 17 to arbitrary Euclidean domains seem dim. How-
ever, by ﬁxing a convex decomposition of a more general domain and using properties
of projections to convex sets, it is possible to give a surprisingly broad generalization.

6.1. The Extended Boundedness Condition. Consider a domain D in En, again with
a conﬁguration of one evader E and N pursuers {Pj}. Suppose D is expressible as
a union D = ∪Dα where each Dα is a convex domain with boundary. We assume
neither that this union is disjoint, nor that each Dα is noncompact, nor that each Dα is
n-dimensional.

The assumptions on the motion of the pursuers and evader must be modiﬁed slightly
in the non-convex setting. In particular, the unit-distance upper bound on the distance
moved per time step must now be interpreted within the interior geometry of D. Play-
ers may move to the endpoint of any (rectiﬁable) path in D of at most unit length from
the start point: players may not “jump” across corners or other boundary features.

Deﬁnition 21. Let PROJα : En → Dα denote nearest-point projection to Dα. The maps PROJα
are well-deﬁned projections, since Dα is convex. The Extended Boundedness Condition
states that the set of pursuers can be partitioned into nonempty collections {Pαjα ∈ Dα, 1 ≤
jα ≤ Nα}, where for each noncompact Dα, the conﬁguration of the evader PROJα(E) and Nα
pursuers {Pαjα} satisﬁes the Boundedness Condition.

Note that for compact Dα, the Extended Boundedness Condition merely says Dα con-
tains at least one designated pursuer.

FIGURE 7. On a domain with convex decomposition, one projects the
evader’s position onto convex factors and plays pursuit games in par-
allel.

16 S. ALEXANDER, R. BISHOP, AND R. GHRIST

Theorem 22. The Extended Boundedness Condition is sufﬁcient to ensure discrete-time equal-
speed capture on D.

Proof. Since the maps PROJα are projections, they are distance nonincreasing, and con-
sequently the jumps of PROJα(E) are at most unit distance. For each noncompact Dα,
let the Nα pursuers {Pαjα} follow the RotatingRadius algorithm applied to Dα with
evader PROJα(E). If Dα is compact, set O0
αjα = P 0
αjα ∈ D and continue as in Radius. If
a pursuer Pαjα captures PROJα(E) but PROJα(E) ̸= E, thereafter let Pαjα move where
PROJα(E) moves, namely P t
αjα = PROJα(Et) for subsequent t.

In accordance with the estimates in the preceding section, the projected or ‘ghost’
evader PROJα(E) is eventually captured for each α. However, PROJα(E) = E for at
least one α: E is captured. ⋄

6.2. Fewer pursuers. The Extended Boundedness Condition is dependent upon a choice
of convex decomposition. An infelicitous choice (too many components) leads to an
excessive lower bound on the number of pursuers needed.

In addition, the analogue of Proposition 10 does not hold in this context. If the Ex-
tended Boundedness Condition fails for a given decomposition (or even for any convex
decomposition), it does not imply that capture cannot be achieved.

Remark 23. As in §5.3, for each Dα, let Ct
α be the component of (Dα − ∪jαBt
jα) contain-
ing PROJα(Et). Say Ct
α and Ct
β are accessible from each other if and only if the interior
distance in D between them is ≤ 1. The possible locations for Et+1 are in those do-
mains Ct
β that are accessible from some Ct
α for which Et ∈ Dα. Consider the graph Γt

whose vertices Vα correspond to the domains Dα, and whose edges correspond to the
accessible pairs {Ct
α, Ct
β}. By Lemma 19, at each step no new edges are created while
some may be lost. Thus at step t, we can discard all the designated pursuers for all the
domains Dβ such that Vβ does not lie in the same connected component of Γt as any
Vα satisfying Et ∈ Dα.
 7. CONCLUDING REMARKS

We close with a sequence of remarks delineating extensions, open problems, and sig-
niﬁcant aspects of the techniques here introduced.

Remark 24. General domains. We stress that the difﬁculties handled in this paper all
stem from the combination of dimensionality and constraints in the domains consid-
ered. In general, 2-dimensional playing ﬁelds are fairly easy to deal with (the proof
of Theorem 17 can be greatly simpliﬁed in the planar case). High-dimensional play-
ing ﬁelds without boundary are trivial. It is the combination of a potentially intricate,
high-dimensional boundary which provides the core challenge. There is seemingly no

CAPTURE PURSUIT GAMES ON UNBOUNDED DOMAINS 17

hope of adapting differential game-theoretic methods to such problems (since chang-
ing the boundary induces subtle global constraints), and we are left with geometry as
a recourse. Fortunately, there are sufﬁcient geometric tools available.

Remark 25. Recession sets. An important contribution of this paper is the recognition
of the recession set as a means of encoding domain geometry in pursuit problems.
This allows one to speak of the evader-pursuer sightlines, the boundary normals of
the domain, and the available escape routes in a common context — subsets of the unit
tangent sphere. The combination of Theorems 9 and 17 imply that feasibility of capture
is a function of the geometry of the recession set relative to evader-pursuer sightlines.
Moreover, the pursuers’ plan may be viewed as an attempt to move the vectors [EPj ]
into the recession set while preserving the boundedness condition.

Remark 26. Multiple evaders. We have considered multi-pursuer games with a sin-
gle evader. Consider a modiﬁcation to the assumptions of §1.2 in which there are M
evaders Eℓ moving in discrete time along the sequences {Et
ℓ} with |Et
ℓEt+1
ℓ | ≤ 1 for all
t. The goal of the pursuit game is to have all M evaders eventually captured.

Thanks to Proposition 10, the obvious necessary condition for capture is that the Bound-
edness Condition is satisﬁed for each Eℓ with respect to the entire collection of pursuers
{Pj}. Thanks to Theorem 17, the obvious sufﬁcient condition for capture is that there
is a partition of the pursuers, {Pℓ,i} for i = 1 . . . Mℓ, such that for each ℓ, the collection
(Eℓ, {Pℓ,i}) satisﬁes the Boundedness Condition on D. The obvious strategy in this case
is to play games in parallel.

In the case of multiple evaders, more complex strategies of pursuers’ trading ‘owner-
ship’ of an evader are possible. This remains an important and interesting challenge.

Remark 27. Information constraints. Similar network-theoretic issues surround issues
of communication and exchange of information between players. The necessary and
sufﬁcient conditions of this paper have the stringent assumptions of perfect evader
location and domain information, as well as initial all-to-all communication between
pursuers (to initialize centers Oj). Relaxing these assumptions generates a number of
interesting challenges.

For example, assume that the pursuers know only an approximate evader location, en-
coded as a compact convex set E (cf. [30]). Assume a monotonicity condition which
says that the set E t+1 is a subset of the translation of E t by a vector of at most unit
length. (That is, uncertainty of evader location can decrease but cannot increase.) Then
it is perhaps possible to reprove the Main Theorem by, for example, having each pur-
suer chase after the point of E closest to the pursuer’s center (this is well-deﬁned thanks
to convexity).

Other scenarios for uncertain information include those in which the pursuers do not
admit an initial all-to-all communication round, but rather communicate with pur-
suers which are sufﬁciently close. Far-off pursuers cannot be reached. This and similar
problems touch on many ideas currently in play in the control theory literature on
distributed consensus with limited/faulty communication [35].

18 S. ALEXANDER, R. BISHOP, AND R. GHRIST

Remark 28. Other noncooperative pursuit games. There are numerous examples of
pursuit-evasion games beyond the Lion & Man setting: see [12, 25] for an overview. We
mention in particular the case considered by Isaacs [12] in which the evader’s goal is
to reach a speciﬁed subset of the domain. More recent entries in the literature consider
pursuit games in which capture means not physical coincidence, but rather visibility
— the pursuer wins when there is a line-of-sight to the evader. For results in this genre,
see [34, 9]. More recently, much attention has been paid to probabilistic techniques in
pursuit games: see [13, 14, 37].

Stepping back from the game-theoretic perspective, one can consider a pursuit-evasion
game as a form of cooperative consensus problem, where a “swarm” of pursuers at-
tempts to reach positional consensus with an evasive “leader.” Consensus problems
have received a great deal of attention recently from the control-theory community,
with motivation from biologically observed swarming phenomena. Several authors
[5, 35, 23] have given decentralized algorithms for reaching consensus in a variety of
contexts.
 REFERENCES

[1] S. Alexander, R. Bishop, and R. Ghrist, “Pursuit and evasion on non-convex domains of arbitrary
dimensions,” Proc. Robotics, Systems and Science, 2006.
[2] L. Alonso, A. Goldstein, and E. Reingold, “’Lion and man’: upper and lower bounds,” ORSA J.
Comput. 4(4), 1992, 447–452.
[3] P. Bouguer, “Sur les lignes courbes qui sont propres `a former les vo ˆutes en d ˆome,” M´emoires de
l’Acad´emie de Paris, 1732, 149–164.
[4] A. Chikrii and P. Prokopovich, “Simple pursuit of one evader by a group,” Cybernetics & Sys. Analysis,
28:3, 1992, 438–444. Translated from Kibernetika i Sistemnyi Analiz, 3, 1992, 131–137.
[5] J. Cort´es and F. Bullo, “Coordination and geometric optimization via distributed dynamical sys-
tems,” SIAM J. Control & Optimization, 44:5, 2005, 1543-1574.
[6] H. Croft, “’Lion and Man’: A Postscript.” J. London Math. Soc. 39, 1964, 385–390.
[7] L. Danzer, B. Gr ¨unbaum, V. Klee, “Helly’s theorem and its relatives,” Proc. Sympos. Pure Math. Vol.
VII, Amer. Math. Soc., 1963, 101–180.
[8] J. Flynn, “Lion and man: the general case,” SIAM J. Control, 12, 1974, 581–597.
[9] L. Guibas, J.-C. Latombe, S. LaValle, D. Lin, and R. Motwani, “A visibility-based pursuit-evasion
problem,” Inter. J. Comput. Geom. & Applications 9(4-5), 1999, 471–.
[10] N. Hovakimyan and A. Melikyan, “Geometry of pursuit-evasion on second order rotation surfaces,”
Dynamics & Control 10(3) 2000, 297–312.
[11] G. Ibragimov, “On a game of optimal pursuit of one evader by several pursuers,” Prikl. Mat. Mekh.
62(2), 1998, 199–205; transl. in J. Appl. Math. Mech. 62(2), 1998, 187–192.
[12] R. Isaacs, Differential Games, Wiley Press, NY, 1965.
[13] V. Isler, S. Kannan, and S. Khanna, “Locating and capturing an evader in a polygonal environment,”
in Proc. Workshop Alg. Foundations of Robotics, 2004.
[14] V. Isler, D. Sun. and S. Sastry, “Roadmap based pursuit-evasion and collision avoidance,” in Proc.
Robotics, Systems, & Science, 2005.
[15] R. Ivanov, “Theorem on the alternative in simple pursuit-evasion and optimality on a half space,”
Serdica 10(4), 1984, 397–411.
[16] V. Jankovic, “About a Man and Lions,” Mat. Vesnik 2, 1978, 359–361.
[17] S. Kopparty and C. Ravishankar, “A framework for pursuit-evasion games in Rn,” Information Proc.
Lett., 96, 2005, 114–122.

CAPTURE PURSUIT GAMES ON UNBOUNDED DOMAINS 19

[18] A. Kovshov, “The simple pursuit by a few objects on the multidimensional sphere,” Game Theory &
Applications II, L. Petrosjan and V. Mazalov, eds., Nova Science Publ., 1996, 27–36.
[19] N.-M. Lˆe, “On determining Mathematical Games optimal strategies in pursuit games in the plane,”
Theoretical Computer Science, 197, 1998, 203–234.
[20] J. Lewin, “The lion and man problem revisited,” J. Optim. Theory Appl., 49(3), 1986, 411–430.
[21] J. Littlewood, A Mathematician’s Miscellany, Methuen & Co., London 1953. Revised edition published
as Littlewood’s Miscellany, Cambridge University Press, 1986.
[22] A. Melikyan, Generalized Characteristics of First Order PDEs, Birkhauser, 1998.
[23] L. Moreau, “Stability of multiagent systems with time-dependent communication links,” IEEE Trans.
Aut. Control, 50:2, 2005, 169-182.
[24] F. Morley, “A curve of pursuit,” Amer. Math. Monthly, 28(2), 1921, 54–61.
[25] P. Nahin, Chases and Escapes: The Mathematics of Pursuit and Evasion, Princeton Press, 2007.
[26] T. Parsons, “Pursuit evasion in a graph,” in Theory & Application of Graphs, Y. Alavi and D. Lick, eds.,
Springer-Verlag, 1976, 426–441.
[27] J. Reif and S. Tate, “Continuous alternation: The complexity of pursuit in continuous domains,”
Algorithmica, 10, 1993, 157–181.
[28] B. Rikhsiev, “Optimality of pursuit time in an n-person differential game with simple motion,” Izv.
Akad. Nauk UzSSR Ser. Fiz.-Mat. Nauk 4, 1984, 37–39.
[29] R. Rockafellar, Convex Analysis, Princeton Univ. Press, Princeton, 1970.
[30] G. Rote, “Pursuit-evasion with imprecise target location,” Proc. 14th ACM-SIAM Symposium on Dis-
crete Algorithms, 2003, 747–753.
[31] N. Satimov and A. Kuchkarov, “Deviation from encounter with several pursuers on a surface.” Uzbek.
Mat. Zh. 1, 2001, 51–55.
[32] N. Satimov and A. Kuchkarov, “On the solution of a model differential pursuit-evasion game on a
sphere.” Uzbek. Mat. Zh. 1, 2000, 45–50.
[33] J. Sgall, “Solution of David Gale’s lion and man problem,” Theor. Comp. Sci. 259, 2001, 663–670
[34] I. Suzuki and M. Yamashita, “Searching for a mobile intruder in a polygonal region,” SIAM J. Com-
put., 21(5), 1992, 863–888.
[35] H. Tanner, A. Jadbabaie, and G. J. Pappas, “Flocking in ﬁxed and switching networks,” IEEE Trans.
Aut. Control, 52:5, 2007, 863–868.
[36] D. Vagin and N. Petrov, “The problem of the pursuit of a group of rigidly coordinated evaders,” Izv.
Akad. Nauk Teor. Sist. Upr. 5, 2001, 75–79.
[37] R. Vidal O. Shakernia, H. Kim, D. Shim, and S. Sastry, “Probabilistic pursuit-evasion games: theory,
implementation, and experimental evaluation,” IEEE Trans. Robotics & Aut. 18, 2002, 662–669.
[38] H. Wu, “The spherical images of convex hypersurfaces,” J. Differential Geometry, 9, 1974, 279–290.

DEPARTMENT OF MATHEMATICS, UNIVERSITY OF ILLINOIS, URBANA IL, 61801

E-mail address: sba@math.uiuc.edu

DEPARTMENT OF MATHEMATICS, UNIVERSITY OF ILLINOIS, URBANA IL, 61801

E-mail address: bishop@math.uiuc.edu

DEPARTMENT OF MATHEMATICS AND COORDINATED SCIENCE LABORATORY, UNIVERSITY OF ILLINOIS,
URBANA IL, 61801

E-mail address: ghrist@math.uiuc.edu
