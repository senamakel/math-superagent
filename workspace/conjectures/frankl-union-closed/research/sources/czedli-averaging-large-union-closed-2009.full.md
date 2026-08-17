<!-- source: https://www.math.u-szeged.hu/~czedli/m/publ.pdf/czedli_on-averaging-Frankl's-conjecture-for-large-union-closed-sets.pdf | converted from PDF -->

On averaging Frankl’s conjecture for large union-closed-sets

Gnabor Cznedli

Dedicated to Lfaszlfo LovfaszN president of IMUN on his sixtieth birthday

Abstract. Let F be a union”closed family of subsets of an m”element set AN Let n 4
|F| ≥ 6 and for a ∈ A let sjap denote the number of sets in F that contain aN FranklAs
conjecture from :R’R“ also known as the unionGclosed sets conjecture“ states that there
exists an element a ∈ A with n − 6sjap ≤ AN Strengthening a result of qao and Yu [’] we
verify the conjecture for the particular case when m ≥ J and n ≥ 6m − 6m/2N Moreover“
for these “largeg families F we prove an even stronger version via averagingN Namely“ the
sum of the n − 6sjap“ for all a ∈ A“ is shown to be non”positiveN Notice that this stronger
version does not hold for all union”closed familiesO however we conjecture that it holds for a
much wider class of families than considered hereN Blthough the proof of the result is based
on elementary lattice theory“ the paper is self”contained and the reader is not assumed to
be familiar with latticesN

1. Introduction and the main theorem

8iven an m[element snite set A ; {a1,. .. , am}Ma family gorM in other wordsM a
setj F of subsets of AM i0e0 FD P gAjM is called a union-closed family gover Ajif
X, Y ∈F implies X ∪ Y ∈F for all X, Y ∈F0 We always assume that A is snite
with “ ⊂ m 6; |A| and n 6; |F| ̸ 40 Θt was Jeter zrankl in RVNV who formulated
the following conjectureM now called as Frankl’s conjecture or the union-closed sets
conjecture6if F is as above then there exists an element of A which is contained
in at least half of the members of F0 Θn spite of a great number of papers by
outstanding authors gonly some of them are listed at the end of the present paper
but the reader can consult with their bibliographiesM tooj this conjecture is still
open0 The known achievements of this seld belong to two categories0
The majority of results belong to pure combinatoricsM with respect to both the
statements and their proofs0 They establish the conjecture under some extra stip[
ulations like upper bounds on m ; |A| or F or the presence of certain setgsj in F0
zor exampleM !orris [R5] resp0 zaro [+] settles the case m ⊂ V resp0 n ⊂ “NM and
Roberts [R”] improves this for n ⊂ ”50 Roberts [R”] also verises the conjecture for

DateH SubmittedH September 6F“ 6AA’O revised Duly JA“ 6AATN
Key words and phrasesH Union”closed sets“ Wranklvs conjecture“ latticeN
This research was partially supported by the NWSR of ¨ungary jOTIBp“ grant noN T A8R8JJ
and I FA:8TN
 1

2G NABOR CZ NEDLI

“small familiesPM i0e0 for n< ”m − RM while for “large familiesPM i0e0 for those with

n ̸ 4
m − R4
(“
4
 )[m/3] − R
4
 (
m
“
 ) − +
“ m T””.+ , gRj

this was done by 8ao and Yu [N]0 zor other achievements of combinatorial nature
cf0M e0g0M ﬂorton and Sarvate [RR] and Vaughan [RY]0 Dne can read more about the
problem at http6]]www0math0uiuc0edu] west]openp]unionclos0html andM of courseM
in zrankl [Y]0
Dn the other handM some results together with their proofs belongs to lattice
theory0 zor exampleM Reinhold [R“] proves the lattice theoretic version of the con[
jecture gto be mentioned laterj for lower semimodular latticesO cf0 Lbe [R] and [4]M
Lbe and ﬂakano [“] and Cerrmann [V] for similar results0
CoweverM there are no real links between the combinatorial and the lattice theo[
retical approachesM except of course for the statement of their equivalenceM cf0 Lbe
and ﬂakano [“]M who gives the credit to Joonen [R4] and Stanley [R+]0 Θn particu[
larM results that look “combinatorialP are proved by combinatorial methods0 Dne
of the novelties of the present work is that although the main result looks com[
binatorial without mentioning latticesM it is achieved via a purely lattice theoretic
method0 Lt this point it is worth assuring the reader from combinatorics that only
a very elementary part of lattice theory will be used and the paper is intended to
be self[contained0
Ψet F be a union[closed family over A and let the notations n ; |F| ̸ 4M m ;
|A| ; |{a1,. .. , am}| be sxed throughout0 zor a ∈ A let sgaj; |{B ∈F 6 a ∈ B}|0
Then zrankl7s conjecture claims the existence of an a ∈ A with n − 4sgaj ⊂ 50 Ψet
us say that F satisses the averaged Frankl’s property if
∑

a∈A
(
n − 4sgaj( ⊂ 5 .

Llthough this property clearly implies that zrankl7s conjecture holds for the given
FM there are many union[closed families for which the averaged zrankl7s property
failsO examples will be given laterM in the lattice environment0
zor a given m ; |A|M the maximum value of n is of course 4
m0Θf n is close to
4
m then we say that the family F is large0 Dur main result on large families is the
following0

Theorem 1. If F is a union-closed family over a nonempty m-element set A,
m ̸ “, and F is large in the sense

n 6; |F| ̸ 4
m − 4
m/2 ;4
m − √4m g4j

then F satisses the averaged Frankl’s property ∑
a∈A(
n − 4sgaj( ⊂ 5.

This theorem strengthens the afore[mentioned result of 8ao and Yu [N] in two
ways6 it deals with the averaged zrankl7s property and g4j allows much more families
than formula gRj0 Some more discussion on this theorem will be given at the end
of the paper0
 AVERAGING FRANKL8S CONJECTURE 3

2. Lattices and proofs

Θn order to sx our notations we recall some well known concepts from lattice
theory0 ’y a lattice gLO ⊂j we mean a partially ordered set such that for any
x, y ∈ L the supremum and insmum of {x, y} existO they are denoted by x ∨ y
and x ∧ yM respectively0 We deal only with snite latticesO they necessarily have a
unique least element 5 and a unique largest element R0 Ln element z of L is said
to be join-irreducible if for all x, y ∈ L the equation z ; x ∨ y implies z ∈{x, y}0
The set of join[irreducible elements distinct from 5 will be denoted by JgLj0 zor
a ⊂ b ∈ L the subset {x ∈ L 6 a ⊂ x ⊂ b} is denoted by [a, b] and it is called an
interval of L0 When a ;5 or b ; R then a particular notation applies6 ↑a ;[a, R]
and ↓b ;[5,b]0 The covering relation is desned via a ≺ b iﬁ a ⊂ b and |[a, b]| ;40
The basic facts on lattices can be found practically in any textbook on algebra like
’urris and Sankappanavar [”]0 gzor the present status of lattice theoryM which is
not needed hereM cf0 8r¨atzer [S]0j We will see soon that a union[closed family F
corresponds to a lattice consisting of |F| elements0 Ln advantage of lattices is that
while in case ofM sayM |F| ; R4 usually it is hopeless to visualize FM it is fairly easy
and inspirational to depict a twelve element lattice0
Θt is well[knownM cf0 Lbe and ﬂakano [“]M Joonen [R4] or Stanley [R+]M that
zrankl7s conjecture is equivalent to its lattice theoretical versionM i0e0M to the follow[
ing conjecture6 “for each snite lattice L with at least two elements there exists an
a ∈ JgLj with |↑a|⊂ |L|/4P0 Θn particularM the lattice theoretic zrankl7s conjecture
implies the original one0 Since we are interested in the averaged property for large
familiesM we have to analyze the proof of this implication0
Ψet FD P gAjbea large union[closed family with “ ⊂|A| ; mO assuming
∅∈ F does not hurt the generality0 Then the family D 6; {A \ X 6 X ∈F} is
intersection[closedM in other wordsM it is a closure system0 Therefore D is a lattice
with respect to the set inclusionO the set theoretic intersection serves as the meet
while the join is usually diﬁerent from the set union0 ﬂow let us consider anX ∈ JgDjM and let Z ; ⋁
{Y ∈D 6 Y< X}0 Then Z< XM i0e0 Z ⌊ XM
for X is join[irreducible0 Cence we can choose an element a

X ∈ X \ Z0 We claim
thatM for any Y ∈DM aX ∈ Y iﬁ X D Y 0 ΘndeedM if aX ∈ Y but X ̸D Y then
X ∩ Y ; X ∧ Y ̸; X gives X ∩ Y D ZM contradicting aX /∈ Z0 ﬂotice that aX
is uniqueO indeedM otherwise we had another element b ∈ A such that each Y ∈D
gand therefore each Y ∈Fj contained either both aX and b or none of themM which
easily led to |F| ⊂ 4
m−1M a contradiction0 Cence the mapping JgDj → AM X ↦→ aX
is injective0 BlearlyM 4m − 4
m/2 ⊂|F| ; |D|⊂|P gJgDjj| gives |JgDj|̸ m ; |A|0
ThereforeM the aforementioned mapping is a bijection0
ﬂowM for each a ; aX ∈ AM |{Y ∈F 6 a ∈ Y }| ; |{Y ∈D 6 aX /∈ Y }| ; |{Y ∈D 6
X ̸D Y }| ; |D\g↑Xj|0 This gives |{Y ∈F 6 aX ∈ Y }| ̸ |F|/4; n/4iﬁ |↑X|⊂ n/4M
and this makes it clear that Theorem R is a consequence of the followingM purely
lattice theoretic theorem0 ’efore formulating this theoremM we introduce some
notations for the rest of the paper0 zor a ∈ JgLj let rgaj; |L|− 4 {|↑a|M and let
rgLj; ∑
{rgaj6 a ∈ JgLj}0

4G NABOR CZ NEDLI

Theorem 2. Let L be a snite lattice consisting of at least two elements, and let
m ; |JgLj|̸ “.If |L|̸ 4
m − 4
m/2 then rgLj ̸ 5.

When proving this theoremM L is often treated as a {5, ∨} semilattice0 This
means that we forget about the meet operation ∧ and by a congruence we mean
an equivalence relation compatible with the join operation ∨ gbut not necessarily
with ∧j0 Ψet X ; {x1,. .., xm} be a sxed m[element set and consider its power
set P gXj; (
P gXj, D
( as a {5, ∨}[semilatticeO of course 5 is the empty set and ∨
stands for the set union ∪0

Lemma 1. There is a congruence i of the {5, ∨}-semilattice (
P gXj, D
( such that
L,as a {5, ∨}-semilattice, is isomorphic to the factor semilattice P gXj/i.

Proof. The lemma is a trivial consequence of the description of free {5, ∨}[semilatticesM
which belongs to the folklore of lattice theory and universal algebraM cf0 e0g0 ¨xercise
” of Section kRR gin page S+j in ’urris and Sankappanavar [”]0 □

Ψet ̃X stand for ∑{x} 6 x ∈ X⋁ ; JgP gXjj0 The i[class of an element u ∈
P gXj will be denoted by [u]i or simply by [u]0 Θn virtue of Ψemma R we will
assume that L equals P gXj/i and A ; {a1,. .. , am} ; JgLj such that ai ;[{xi}]
for i ∈{R,. .., m}0 zor a i[class [u] ∈ P gXj/i; L let eg[u]j ; e2g[u]j ;
|[u]i \{u}| ; |[u]|− RM the excess of [u] ∈ L0 Sometimes we use the notation
eCg[u]j ; |[u]m \{u}| for another equivalence m gnot necessarily a congruencej
on P gXjO then the subscript m is never dropped0 Since the isomorphism between
P gXj/i and L is considered sxedM we can use the notation egbj for any b ∈ L0
BlearlyM we have
 4
m/2 ̸ 4
m − n ; |P gXj|−|L| ; ∑

b∈L egbj. g“j

Ln element b ∈ L will be called an abundant element if egbj > 50 Θn accordance
with the terminology of latticesM for u ∈ P gXj the height of uM denoted by hgujis
desned as |u| ; |↓u ∩ ̃X|0

Lemma 2. If [u] ∈ L is abundant then hguj ̸ m/4 − R.

Proof. Θt belongs to the folklore gor it can trivially be extracted from the proof of
Ψemma Θ0“0N in 8r¨atzer [S]j that the i[classes of P gXj are convex subsemilattices0
This means that for every [u] ∈ P gXj/iM [u] is closed with respect to join and
v1 ⊂ v2 ⊂ v3 ∈ P gXj together with v1,v3 ∈ [u] imply v2 ∈ [u]0 CenceM without loss
of generalityM we may assume that u is a minimal element in its abundant i[class
[u] and there is an element v ∈ [u] such that u ≺ v0 Since P gXj and therefore
any of its interval can also be considered as a ’oolean algebraM we may take the
unique grelativej complement v′ of v in ↑u0 We have v ∧ v′ ; u and v ∨ v′ ;RM
hgvj; hguj T R and hgv′j; m − R0
Ψet m denote the smallest equivalence gnot a congruenceIj including {gt, t ∨ vj6
t ∈ [u, v′]}0 Dbserve that for every t ∈ [u, v′]M |[t]m| ; 4 and eCg[t]mj ; R0 ΘndeedM
otherwise t1∨v ; t2∨v would hold for some distinct t1,t2 ∈ [u, v′] and distributivity
would easily lead to a contradiction6 t1 ;gt1 ∧ v′j ∨ u ;gt1 ∧ v′j ∨ gv ∧ v′j;

AVERAGING FRANKL8S CONJECTURE 5

gt1 ∨ vj ∧ v′ ;gt2 ∨ vj ∧ v′ ; .. . ; t20 Since for each t ∈ [u, v′] we have gt, t ∨ vj;
gt ∨ u, t ∨ vj ∈ iM we obtain that m D i0 ﬂowM for a i[class b ∈ LM assume that
b ∩ [u, v′]; {t1,. .. , tℓ} with ℓ ̸ R and ti ̸; tj for i ̸; j0 Then m D i yields that
the ti ∨ v belong to bM whence egbj ̸ 4ℓ − R ̸ l ; eCg[t1]mj T {{ {T eCg[tℓ]mj0 Cence
we conclude
∑

b∈L egbj ̸ ∑

t∈[u,v′] eCg[t]mj ̸|[u, v′]| ;4
h(v′)−h(u) ;4
m−1−h(u). g”j

ﬂow g“j and g”j entail m/4 ̸ m − R − hgujM implying the lemma0 □

Lemma 3. There is at most one u ∈ P gXj such that hguj <m/4 and [u] is
abundant.

Proof. ’y way of contradiction we suppose that u1 and u2 are distinct abundant
elements of P gXj and hguij <m/4 for i ;R, 40 Θt follows from Ψemma 4 that
hgu1j; hgu2j; ⌊gm − Rj/4⌋ and ui is a minimal element in [ui] for i ∈{R, 4}0
Ψike in the previous proofM for i ∈{R, 4} there is a vi ∈ P gXj such that vi ∈ [ui]M
ui ≺ vi and vi has a unique grelativej complement v′
i ∈↑ui0 Ψet si ; {gt, t ∨ vij6
t ∈ [ui,v′
i]}M and let m ; s1 ∪ s20 gΘn generalM they are equivalencesM not necessarily
semilattice congruences0j The proof of Ψemma 4 shows that each of the si classes
has at most two elementsM |[t]si| ; 4 for all t ∈ [ui,v′
i]}M and m D i0 Cence for
i ;R, 4M like in case of g”jM
∑

[t]ti∈L/ti etig[t]sij; |[ui,v′
i]| ;4
m−1−⌊(m−1)/2⌋ ;4
⌊m/2⌋. g+j

This may give the feeling that
∑

b∈L egbj ̸ ∑

[t]C∈L/C eCg[t]mj ̸
′ 4
⌊m/2⌋ T4
⌊m/2⌋ ;4
⌊m/2⌋+1 . gYj

CoweverM the above estimation for the total excess ∑
b∈L egbj is not correct at ̸
′

since the contribution of g+j for i ; R and that for i ; 4 are not necessarily
“disjointPM so the “common contributionP has to be subtracted from 4
⌊m/2⌋+10
ﬂow consider a m[class H as a graph of m|H0 We disregard from loop edges0
Then this graph is a connected oneM and each of its edges has a unique color from the
color set {s1,s2}0 Two parallel edges with distinct colors are possible0 Since the
si[classes have at most two elementsM the degree of each vertex of this graph is at
most two0 Θf this graph contains no circle thenM in connection with HM nothing has
to be subtracted from 4
⌊m/2⌋+10 This is exemplised byM sayM H ; {w1,. .., w6} with
gw1,w2j, gw3,w4j, gw5,w6j ∈ s1 and gw2,w3j, gw4,w5j ∈ s2M then eCgHj ; +M and
this is the same as the sum et1g[w1]s1jT et1 g[w3]s1jT et1 g[w5]s1jT et2 g[w2]s2jT
et2g[w4]s2j0
So 4⌊m/2⌋+1 needs correction only for those H that contain a circle0 Since H is
connected with vertex degrees ⊂ 4M this means that H is a circleM and the colors
s1 and s2 alternate on this circle0 Since both s1 and s2 are included in the <
relation of P gXjM we can consider H as an oriented graph such that the start
point of each edge should be less then its endpoint0 Θn factM we imagine H as a

6G NABOR CZ NEDLI

regular |H|[gon in the plain0 Since the relation < is irre=exiveM it is impossible that
all edges are oriented clock[wise or they are all oriented anti[clockwise0 Therefore
there are consecutive elements t1,t,t2 of H such that t1 >t <t2 and gt, t1j ∈ si and
gt, t2j ∈ s1−i0 gThe possibility t1 ; t2 is allowed0j zrom gt, t1j ∈ si we conclude
that ui ⊂ t ⊂ v′
i while gt, t2j ∈ s1−i entails u1−i ⊂ t ⊂ v′
1−i0 Cence t belongs to the
interval [u1 ∨ u2,v′
1 ∧ v′
2]0 Since the “m[excessP eCg[t]mj ; egHj is one less than
the sum of the “si[excessesP gwith alternating ij of its edgesM we have to subtract
one from 4⌊m/2⌋+1 according to H0 We can associate the above t ∈ [u1 ∨ u2,v′
1 ∧ v′
2]
with this subtractionO t is not necessarily unique but distinct circles H give rise to
distinct elements t0 Cence the total subtraction is at most |[u1 ∨ u2,v′
1 ∧ v′
2]|0
Since u1 ̸; u2M hgu1 ∨ u2j ̸ hgu1j; hgu2jM so hgu1 ∨ u2j ̸ hgu1jT R ;
RT ⌊gm − Rj/4⌋ ; ⌊gm TRj/4⌋0 We cannot say v′
1 ̸; v′
2M we have only hgv′
1 ∧ v′
2j ⊂
hgv′
1j; m − R0 So we obtain

|[u1 ∨ u2,v′
1 ∧ v′
2]|⊂ 4
m−1−⌊(m+1)/2⌋ ;4
⌊m/2⌋−1 . gNj

ﬂow subtracting gNj from the right hand side of gYj we obtain that the total excess
is at least ∑

b∈L egbj ̸ 4
⌊m/2⌋+1 − 4
⌊m/2⌋−1 ;g“/4j { 4
⌊m/2⌋. gSj

zinallyM after inspecting even and odd values of m separatelyM we see that g“j con[
tradicts gSjM completing the proof of Ψemma “0 □

ﬂow we are in the position of proving Theorem 46

Proof of Theorem 2. Ψet H1,. .. , Hℓ be a complete list of abundant gi0e0M non[
singletonj i[classes0 Θt has already been mentioned that the Hi are gconvexj sub[
semilattices0 Therefore each Hi has a unique largest element wi0 Then Hi ;[wi]0
ﬀenote Hi \{wi} by Gi and let G ; G1 ∪ {{{ ∪ Gℓ0 BlearlyM |G| ; ∑

b∈L egbjM the
total excess of L0 We claim that
∑

g∈G |↓g ∩ ̃X| ; ∑

g∈G hggj ̸ m
4 {|G|. gVj

The equality is trivial by desnitions0 The inequality is almost clear by Ψemmas 4
and “M for all but at most one summands satisfy hggj ̸ m/40 Suppose there is a
g ∈ G with hggj <m/40 Then this g is unique and hggj; ⌊gm−Rj/4⌋ by Ψemmas 4
and “0 Since [g] is a convex subsemilattice and g is not its largest elementM there is an
element v ∈ [g]\{g} such that g ≺ v0 Ψet v′ be the complement of v in P gXj0 Then
hgg ∨ v′j; m − R0 Eoining gg, vj ∈ i and gv′,v′j ∈ i we have gg ∨ v′, Rj ∈ iM which
yields that g ∨ v′ ∈ G0 ﬂowM exploiting m ̸ “ the srst timeM ⌊gm − Rj/4⌋ <m − R
gives g ̸; g ∨ v′ and hggjT hgg ∨ v′j; ⌊gm − Rj/4⌋ T m − R ̸ 4 { m/4 proves gVj0
ﬂowM for ai ;[{xi}] ∈ JgLjM |↑ai|M computed in LM equals |↑{xi}\ G| ; |↑{xi}\
gG∩↑{xi}j| ;4
m−1 −|gG∩↑{xi}j|0 ﬂotice also that |L| ; n and for any y ∈ P gXjM
hgyj; |{xi ∈ X 6 {xi}⊂ y}|0 Cence

rgLj;
 m∑

i=1
(
|L|− 4 {|↑ai|( ; mn − 4
 m∑

i=1 |↑ai| ;

AVERAGING FRANKL8S CONJECTURE 7

mn − 4
 m∑

i=1
(
4
m−1 −|gG ∩↑{xi}j|( ; mn − m { 4
m T4
 m∑

i=1 |gG ∩↑{xi}j| ;

mgn − 4
mjT 4 { }
}{gg, xj6 x ∈ X, g ∈ G, and {x}⊂ g}
}
} ;

mgn − 4
mjT 4 ∑

g∈G |↓g ∩ ̃X|̸
(9) mgn − 4
mjT m {|G|

;m(
n − g4m −|G|j( ; m(n − (
4
m − ∑

e∈L egbj() ;
(3) mgn − nj; 5,

proving Theorem 40 □

The above proof reveals that condition g4j is far from being optimal for large
m0 CoweverM we do not see how far we could go with our methodM and therefore
we have decided not to spoil the simplicity of condition g4j by making the proof
much more complicated without reaching the optimal condition0 We conjecture that
Theorem R remains true if 4
m − 4
m/2 is replaced by something even smaller than
4
m − 4
m−20 We also conjecture that rgLj > 5 gequivalentlyM ∑
a∈A(
n − 4sgaj( < 5j
when 4
m >n> 4
m − 4
m−2 and m ̸ “0 These conjectures come from a great
number of examples examined by computerM and also from the following example0
Ψet L be the direct product of a ’oolean algebra with m − 4 atoms and the three
element chain0 gzor m ;”M L is given in zigure RO JgLj consists of the black[slled
elements0j We omit the details of showing that this lattice L has the properties
JgLj; mM |L| ;4
m − 4
m−2 ;“ { 4
m−2 and rgLj; 50

0c 2c 3c
1c
 KL
 2b 3b
1b

Figure 1

We conclude the paper with another example which shows that the averaged
zrankl7s property does not hold for all lattices orM equivalentlyM for all union[closed
families0 Take a ’oolean algebra B with k atoms0 gThe case k ; “ is depicted in
zigure R0j Ψet b1,. .., bk be the atoms of B0 Rename the 5 of B as c0M add a new 5
and for i ;R,. .. , kM add a new atom ci such that 5 ≺ ci ≺ bi0 This way we obtain a
lattice K consisting of 4
k TkTR elements0 ﬂow rgc0j; 4k TkTR−4{4
k ; kTR−4
k

andM for R ⊂ i ⊂ kM rgcij; 4k T k TR − 4gR T 4
k−1j; k − R0 Cence

rgKj; rgc0jT rgc1jT {{ { T rgckj; k2 TR − 4
k < 5

when k ̸ +0

8G NABOR CZ NEDLI

References

[:] Tetsuya BbeH Excess of a lattice“ qraphs and Vombinatorics 18 j6AA6p“ JRU–8A6N
[6] Tetsuya BbeH Strong semimodular lattices and FranklAs conjecture“ Blgebra Universalis 44
j6AAAp“ J’R–JT6N
[J] Tetsuya Bbe and Pumpei Nakano H Wranklvs conjecture is true for modular lattices“ qraphs
and Vombinatorics 14 j:RRTp“ JAU–J::N
[8] SN Purris and ¨N PN SankappanavarH A Course in Universal Algebra“ qraduate Texts
in Mathematics“ ’TN Springer”Verlag“ New York–Perlin“ :RT:O The Millennium /dition“
httpH;;wwwNmathNuwaterlooNca;∼snburris;htdocs;ualgNhtml N
[U] qN Lo WaroH UnionGclosed sets conjecture: improved bounds“ DN VombinN MathN VombinN
VomputN 16 j:RR8p“ R’–:A6N
[F] PN WranklH Extremal set systemsT Handbook of combinatorics“ Vols. 1, 2“ :6RJ–:J6R“ /lsevier“
Bmsterdam“ :RRUN
[’] Weidong qao and ¨ongquan YuH Note on the unionGclosed sets conjecture“ Brs VombinN 49
j:RRTp“ 6TA–6TTN
[T] qN qr¨atzerH General Lattice Theory“ Pirkh¨auser Verlag“ Pasel”Stuttgart“ :R’TN
[R] VN ¨errmann and RN LangsdorfH FranklAs conjecture for lower semimodular lattices“
httpH;;wwwNmathematikNtu”darmstadtNdeHTATA;∼herrmann;recherche;
[:A] RN MorrisH FCGfamilies and improved bounds for FranklAs conjecture“ /uropean DN VombinN
27 j6AAFp“ 6FR–6T6N
[::] RN MN Norton and EN qN SarvateH A note of the unionGclosed sets conjecture“ DN BustralN
MathN SocN SerN B 55 j:RRJp 8::–8:JN
[:6] PN PoonenH UnionGclosed families“ DN Vombinatorial Theory B 59 j:RR6p“ 6UJ–6FTN
[:J] DN ReinholdH FranklAs conjecture is true for lower semimodular lattices“ qraphs and Vombi”
natorics 16 j6AAAp“ ::U–::FN
[:8] zN Roberts“ TechN RepN NoN 6;R6“ School MathN StatN“ Vurtin UnivN TechN“ Perth“ :RR6N
[:U] RN PN StanleyH Enumerative CombinatoricsN VolT IT“ Pelmont“ VBH Wadsworth and
Prooks;Voole“ :RTFN
[:F] TN PN VaughanH Families implying the Frankl conjecture“ /uropean DN VombinN 23 j6AA6p“
TU:–TFAN

University of Szeged, Bolyai Institute, Szeged, Aradi vgertanguk tere 1, HUNGARY
6720
EGmail addressH czedli@math.u-szeged.hu
URLH http://www.math.u-szeged.hu/∼czedli/
