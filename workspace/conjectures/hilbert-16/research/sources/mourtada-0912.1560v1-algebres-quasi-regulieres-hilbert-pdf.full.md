<!-- source: https://arxiv.org/pdf/0912.1560v1 | converted from PDF -->

arXiv:0912.1560v1  [math.DS]  8 Dec 2009
ACTION DE DERIVATIONS IRREDUCTIBLES SUR LES

ALGEBRES QUASI-REGULIERES D’HILBERT

par Abderaouf Mourtada

A la mmoire de Jean Martinet

Universit de Bourgogne, I.M.B.
U.M.R. 5584 du C.N.R.S., U.F.R. des Sciences et Techniques
9, avenue Alain Savary, B.P. 47 870, 21078 Dijon Cedex.
E-mail: mourtada@u-bourgogne.fr

Mots-cls: 16me problme d’Hilbert, cycle limite, cyclicit, polycycle, singularit de
champ de vecteurs, application de Dulac, application de retour de Poincar, struc-
ture asymptotique quasi-analytique, action diﬀrentielle, idal diﬀrentiel, faisceau
diﬀrentiel, projection intgrale, multiplicit algbrique.

Classiﬁcation AMS: 34C07 (Primary) 34C08, 37G15 (Secondary).

Abstract. We study the action of irreducible derivations χ on some Hilbert’s quasi-
regular algebras QRH of germs at 0, of real analytic functions on (U, 0), where U
is some semi-algebraic open set. We show that these algebras are χ-ﬁnite or locally
χ-ﬁnite: the degree of the projection πχ restricted to ﬁbers of QRH, is ﬁnite and
the diﬀerential ideals are noetherian or locally noetherian. Moreover, these algebras
satisfy to the double inclusion: for every germ f , there exist an algebraic multiplicity
maχ(f ) such that, modulo some algebraic factor which vanishs only on the germ of
the boundary (∂U, 0), and depends only on ma, the diﬀerential ideal of f coincides
with the saturation of his transverse ideal. In last, we give an application to the
generalised Hilbert’s 16th problem about limit cycles: there is no accumulation of
limit cycles on hyperbolic polycycles in compact analytic families of vector ﬁelds on
the sphere S2. This is a highly non trivial result, it includes the case of a polycycle
that is an accumulation of cycles.
 Introduction

Le problme de Dulac ([E], [I]), dit que tout champ de vecteurs analytique
sur la sphre relle S2 a un nombre ﬁni de cycles limites, autrement dit il n’y a pas
accumulation de cycles limites sur les polycycles. Le 16me problme d’Hilbert
algbrique ([Hi]), demande d’tablir une majoration de ce nombre en fonction du
degr pour les champs de vecteurs algbriques du plan rel. Plus gnralement ([Ro1]),
il s’agit de montrer qu’il n’y a pas accumulation de cycles limites sur les ensembles
1

2

limites priodiques, dans les familles compactes de champs de vecteurs analytiques
sur S2: c’est le problme d’Hilbert analytique. Soit Γk un polycycle hyper-
bolique et monodromique rel, k singularits, tangent `a un champ de vecteurs
analytique r´eel X0 d´eﬁni sur un voisinage U0 de Γk. On suppose, uniquement pour
simpliﬁer la prsentation, que le rapport des valeurs propres en chaque singularit de
Γk est gal −1. Dans la section IVC, on montre le thorme fondamental

Thorme 0. Soit Xν un dploiement analytique de X0 q paramtres. Alors il existe
des entiers N et L et des voisinages Γk ⊂ U ⊂ U0 et V ∈ (Rq, 0) tels que

(i) pour tout ν ∈ V , le nombre de cycles limites de Xν dans U est major par
N ,

(ii) la multiplicit de chacun de ces cycles limites est majore par L.

Plusieurs travaux, sur des cas gnriques, ont t tablis par moi mme ([M]), ou par
Il’yashenko, Yakovenko et Kaloshin ([I-Y2], [Ka]), o les singularits semi-hyperboliques
sont aussi considres. La dmarche adopte dans ces travaux consiste, d’abord en une
prparation gnrique des singularits (dans une classe de diﬀrentiabilit suﬃsament
grande), suivie d’une application de la procdure d’limi-
nation de Khovanski ([K1]). Dans [M], les conditions gnriques sont algbriquement
controles tout au long de cette procdure. Cependant, dans [I-Y2], il semble trs diﬃ-
cile de relier les conditions gnriques de cette procdure celles, gomtriques provenant
du polycycle.

Dans le cas gnral du thorme 0, et en vue de couvrir les cas les plus dgnrs,
l’approche mise en oeuvre peut se rsumer ainsi: on prpare localement (dans une
subdivision ﬁnie), l’application de retour pν du polycycle perturb. Dans cette
prparation, les proprits de ﬁnitude de pν (le nombre de ses points ﬁxes et leur
multiplicit), sont donnes par celles d’un certain jet ﬁni qui est un fewnomial [K1].
La thorie de Khovanski s’applique aisment ces jets.

Voici les ides de base de cette approche: soient (x, α) des coordonnes analytiques
locales sur ((R+∗)
k × Rq, 0), et soit Bk = {∏k
j=1 xj = 0}. Soit B ⊃ R{x, α} un
anneau local de germes de fonctions analytiques sur ((R+∗)
k × Rq, 0), continues
sur (Bk, 0). Soit χ un germe en 0 de champs de vecteurs composantes dans B.
On s’intresse aux drivations qui induisent une action inﬁnitsimale sur B, et plus
particulirement celles qui satisfont aux conditions suivantes: χ(B) ⊂ B, Sing(χ) ⊂
(Bk, 0) et (Bk, 0) est invariant par le ﬂot ϕχ (cf. partie IB). Le but est d’tudier les
proprits de ﬁnitude topologiques et algbriques des lments de l’algbre B relativement
la distribution induite par la drivation χ dans ((R+∗)
k × Rq, 0).

Les concepts suivants sont dvelopps dans la partie IB. Soit U ∈ ((R+∗)
k × Rq, 0)
un ouvert sur lequel est ralise la drivation χ. Soit ϕχ,U le ﬂot de χ dans U , et soit
πχ,U : U → ̃U = U/ϕχ,U la projection intgrale le long des orbites de χ dans U .
Un germe f ∈ B est dit χ-rgulier s’il existe un tel ouvert U tel que le degr de πχ,U
restreinte aux ﬁbres de f soit ﬁni. Il est dit χ-ﬁni s’il est χ-rgulier et si son idal
diﬀrentiel Iχ,f est noethrien dans une extension toile de B. Il est dit localement
χ-ﬁni s’il est χ-rgulier et s’il existe une subdivision ﬁnie (Ui) de U , invariante par
χ, telle que chaque idal restriction Iχ,f |Ui soit noethrien dans une extension toile

3

de l’anneau restriction B|Ui. Une sous-algbre ou une sous-classe de B est dite χ-
ﬁnie (resp. localement χ-ﬁnie) si chacun de ses lments est χ-ﬁni (resp. localement
χ-ﬁni). Un rsultat majeur de la partie IB est

Lemme de ﬁnitude IB1. Soit M l’idal maximal de B et soit M0 ⊂ M un idal
stable par χ. Soit B′ ⊂ B une sous-algbre χ-ﬁnie et stable par χ. Alors la classe
CM0,B′ = {f ∈ g + M0Iχ,g; g ∈ B′} est χ-ﬁnie.

Dans ce cas, on dit que f est χ-quivalente g et plus gnralement, on parle d’algbres
ou de classes χ-quivalentes. Ce lemme donne une ide du type de prparation que
l’on souhaite tablir. Dcrivons brivement les outils pour atteindre cet objectif. Si
γ ⊂ U est une orbite de χ, le lemme d’isomorphie IB4 dit que les ﬁbres du fais-
ceau diﬀrentiel Iχ,f [γ] sont isomorphes dans les anneaux analytiques locaux R{.}
correspondants. D’o l’existence d’un unique idal transverse Jχ,f,γ dans un anneau
analytique R{β} dont les coordonnes β sont des intgrales premires de χ le long de γ.
De plus, le lemme de saturation IB5 permet de reconstruire chaque ﬁbre du faisceau
diﬀrentiel partir de cet idal transverse: pour tout m ∈ γ, Iχ,f (m) = π∗
χm (Jχ,f,γ).
La question naturelle qui se pose alors est: si γ adhre 0, quel est le lien entre la
ﬁbre diﬀrentiel en 0 et le satur de cet idal transverse? Il est clair que ce lien est
d’autant plus fort que l’orbite γ est principale dans U , i.e le satur de toute transver-
sale analytique γ est un voisinage de 0 dans U . L’idal I((Bk, 0)) est principal de
gnrateur θ = ∏k
j=1 xj . Alors, ce lien s’exprime en gnral par une double inclusion
qui relaxe l’galit le long de γ, et qui s’inspire du Nullstellensatz d’Hilbert

(∗) (θn)π∗
χ(Jχ,f,γ) ⊂ Iχ,f ⊂ π∗
χ(Jχ,f,γ )

Le plus petit de ces entiers n est la multiplicit mχ(f ) de f relativement χ. Si
l’anneau B possde une structure asymptotique, il se trouve que cette multiplicit est
intimement lie la multiplicit algbrique maχ(f ) qui est l’indice de stationnarit d’une
suite croissante d’idaux transverses, qui converge vers Jχ,f,γ. Ainsi, en tudiant
l’action de χ sur les jets ﬁnis de f , et en utilisant la double inclusion (∗), on montre
que f est χ-quivalente son jet d’ordre maχ(f ) (cf. sections II, III, IV). Le lemme
de ﬁnitude ci-dessus donnera les proprits de ﬁnitude voulues.

La projection πχ est unidimensionnelle. On peut gnraliser cette approche du
bord (Bk, 0), en considrant des projections p-dimensionnelles le long, par exemple
des feuilles d’un feuilletage de dimension p.

Le germe de l’application de Dulac, et de ses dploiements, appartiennent cer-
taines algbres QRH1,. dcrites dans la partie IA. L’algbre QRHk,.(x, .) ⊂ B est
constitue des germes qui sont quasi-analytiques dans les coordonnes x

QRH ∩ (∩n∈NMn
x) = {0}

(Mx = ⟨x1, . . . , xk⟩ ⊂ B); et qui possdent une structure asymptotique lmen-
taire dans les coordonnes x: ces ingrdients sont des fonctions lmentaires d’Ecalle-
Khovanski. Soit χ ∈ ΞHk une drivation d’Hilbert ralise sur un ouvert Uk ∈
((R+∗)
k × Rq, 0), de dimension de non trivialit k − 1 (cf. partie IVA). Elle ad-
met une action sur l’algbre QRHk,. et elle possde une orbite principale γ incluse

4

dans Uk. Dans la partie IVC, on montre le thorme gnral suivant, dont le thorme 0
est une consquence immdiate

Thorme IVC1. L’algbre QRHk,. est localement χ-ﬁnie et satisfait localement la
double inclusion (∗).

La drivation χ n’est pas rduite. Il existe une dsingularisation (πk, Nk) entirement
dcrite pas les algbres QRHk,. (cf. partie IVA), et dans laquelle les singularits rduites
de χ sont de la forme
 χℓ = ρ ∂
∂ρ −
 ℓ∑

j=1 sjuj ∂
∂uj

pour ℓ = 0, . . . , k − 1. Le thorme IVC1 est donc une consquence de l’tude de
l’action des drivations rduites χℓ sur les algbres QRHp,.(ρ, ρ′, .), avec p ≤ k. Or,
une drivation χℓ, ralise sur un ouvert Up, admet une orbite principale incluse dans
Up si et seulement si p = 1. Dans ce cas, on montre les rsultats principaux suivants
dans les sections II et III

Thorme principal II1. L’algbre QRH1,.(ρ, .) est χ0-ﬁnie et satisfait la double
inclusion.

Ce thorme, de dmonstration simple et basique est une introduction aux autres
thormes. Notons QRH1,.
cvg la restriction d’un anneau analytique R{.} au graphe
des fonctions lmentaires de l’algbre QRH1,. correspondante. Sa χℓ-ﬁnitude est une
consquence simple de rsultats de gomtrie analytique classique et de la thorie de
Khovanski-Tougeron ([K1], [T]).

Thorme principal IIIA1. Pour tout ℓ, l’algbre QRH1,.
cvg satisfait la double in-
clusion relativement χℓ.

Thorme principal IIIB1. Pour tout ℓ, l’algbre QRH1,. est localement χℓ-ﬁnie et
satisfait localement la double inclusion.

Si p > 1, la drivation χℓ admet une orbite principale γp incluse dans le bord Bp:
le satur dans Up de toute semi-transversale analytique γp est un voisinage de 0
dans Up. Les ﬁbres diﬀrentielles le long de γp ne sont pas forcment isomorphes et il
n’existe pas forcment d’idal transverse. Plus gnralement, deux questions se posent
concernant les anneaux QRHp,.: sont-ils noethriens? et leurs semi-analytiques
sont-ils induits par une structure o-minimale au dessus de R?

La preuve du thorme IVC1 s’appuie sur les trois thormes principaux ci-dessus, et
sur 6 lemmes de base (cf. partie IB). Soit Dk le diviseur exceptionnel du morphisme
(πk, Nk) de dsingularisation de χ (cf. IVA). Soit f ∈ QRHk,. et soient ̃f et ̃χ les
relevs de f et χ par πk. Il s’agit de montrer que le faisceau I eχ, ef [Dk] est localement
̃χ-ﬁni. La drivation ̃χ admet une unique singularit a0 sur Dk. Soit γ1 ⊂ Dk une
orbite de ̃χ et soit a1 = γ1 ∩ ∂Dk. Par compacit de Dk, il suﬃt de montrer que le
faisceau I eχ, ef [a0γ1a1] est localement ̃χ-ﬁni.
 5

L’orbite γ0 = π−1
k (γ) est principale dans un voisinage U1,a0 de a0. Le rsultat en
a0 est donc une consquence du thorme principal IIIB1. En tout point a ∈ γ1, un
reprsentant du germe (γ1, a) est principal dans un voisinage U1,a de a; cependant
il est inclus dans le bord de U1,a. Grce au lemme de cohrence IB3, les rsultats du
thorme principal IIIB1 en a0 se germiﬁent en tout point a ∈ γ1 suﬃsament proche
de a0: le germe en a de ̃f est ̃χ-quivalent un lment ga d’une algbre convergente
QRH1,.
cvg, qui elle, satisfait au thorme principal IIIA1. Or, comme ̃f , ce germe se
prolonge au dessus de γ1 en une fonction g dont tous les germes appartiennent
une algbre convergente. Le lemme d’isomorphie s’applique aux faisceaux de cette
algbre le long d’orbites incluses dans le bord. Un recollement des idaux de g et de
̃f donne le rsultat au dessus de γ1. En a1, on utilise un argument de rcurrence sur
la dimension de non trivialit de la drivation d’Hilbert (cf. lemmes de rcurrence,
parties IVB et IVC). Sa preuve est elle mme construite autour des 6 lemmes de
base et des 3 thormes principaux

L’application de Dulac de chaque singularit de Xν est induite par un lment d’une
algbre QRH1,. (cf. appendice VA). Les cycles limites de Xν correspondent aux
intesections isoles des orbites d’une drivation d’Hilbert χ ∈ ΞHk et des ﬁbres d’un
germe f ∈ QRHk,.. Le thorme 0 est alors une consquence simple du thorme IVC1:
la proprit (i) est quivalente la χ-rgularit de f , et la proprit (ii) est une consquence
de la noethrianit ou la locale noethrianit de l’idal diﬀrentiel Iχ,f . Cette approche
algbrique et gomtrique est appliquable tout ensemble limite priodique. Comme
dans le problme de Dulac, la seule diﬃcult rside dans la complexit des structures
asymptotiques des meilleures algbres et drivations d’Hilbert correspondantes.

L’article est compos de 4 sections I,...,IV et un appendice V. Chaque section est
subdivise en parties A, B,... et chaque partie est subdivise en paragraphes 1, 2,...

Remerciements. Je remercie vivement mes collgues A. Jebrane, P. Mardesic,
R. Moussu, M. Pelletier, C. Rousseau et D. Schlomiuk, pour leur soutien durant
ce pnible travail. Je tiens remercier particulirement R. Roussarie, qui a apport
d’normes amliorations certains rsultats de ce travail.

I. Dﬁnitions et lments de base.

A. Dﬁnitions des algbres.

§1. L’algbre A
p,q.

Soit (x, α) = (x1, · · · , xp, α1, · · · , αq) des coordonn´ees sur Rp × Rq.

Dﬁnition IA1. On note A
p,q(x, α) (ou simplement A
p,q) l’alg`ebre r´eelle locale des
germes analytiques r´eels de ((R+∗)
p, 0) × (Rq, 0) qui sont continus sur le germe en
0 du bord Bp = {x1 × · · · × xp = 0}.

Sauf mention contraire, toutes les alg`ebres de rfrence consid´er´ees dans la suite
sont des sous-alg`ebres locales de A
p,q qui contiennent l’algbre analytique R{x, α}.
Ces algbres A
p,q ne sont pas stables par les drivations les plus lmentaires: f =
x sin(1/x) ∈ A
1,0 mais x∂f /∂x ̸∈ A
1,0. Dans le problme d’Hilbert, ces algbres
serviront uniquement d’espaces d’intgrales premires pour les drivations considres

6

(voir sections III et IV).

§2. L’algbre SBp,q des germes sectoriellement borns.

Soit θ = (θ1, · · · , θp) ∈]0, π/2[p et Sθ le polysecteur

(1) Sθ = {w = (w1, · · · , wp) ∈ (C∗)
p; | arg(wj )| < θj}

Soit (Sθ, ∞) le germe de Sθ `a l’inﬁni.

Pour simpliﬁer la prsentation dans toute la suite, nous noterons souvent pareille-
ment les germes, leurs reprsentants et les relevs de germes de fonctions dans la carte
w = − log(x).

Dﬁnition IA2. Les ´el´ements de l’alg`ebre SBp,q(x, α) ⊂ A
p,q(x, α) sont les germes
f qui admettent, pour tout θ ∈]0, π/2[p, un prolongement holomorphe et born´e sur
(Sθ, ∞) × (Cq, 0) dans la carte w = (wj = − log(xj ))j=1,··· ,p.

Ces alg`ebres SBp,q sont le lieu naturel o`u vivent les germes d’applications de Du-
lac des d´eploiements holomorphes d’´equations diﬀ´erentielles du 1er ordre, y compris
dans le domaine de Poincar´e (voir appendice A). Ce sont les anneaux de rfrences
dans le problme d’Hilbert (voir sections II, III et IV). Leur intrt premier rside
dans leur structure holomorphe produit. Notons ´egalement SBp,q
0 la sous-alg`ebre
de SBp,q des germes qui, pour tout θ, tendent vers 0 quand w → ∞ dans (Sθ, ∞),
uniform´ement en α. Contrairement `a l’algbre A
p,q, les alg`ebres SBp,q et SBp,q
0
sont stables par les d´erivations naturelles χj = xj ∂/∂xj ∼ −∂/∂wj (consquence
immdiate des formules de Cauchy dans les secteurs Sθ). Cependant, elles ne sont
pas quasi-analytiques (voir ci-dessous).

§3. Algbres quasi-analytiques QA
p,q.

Soit P + = {w = u + iv ∈ C; u ≥ 0}. Soient u0 ≥ 0, C > 0 et K > 1. Les
domaines de P + de type puissance sont les domaines de la forme

Ωpuis(u0, C, K) = {w ∈ P +; u > u0, |v| < CuK}

Les domaines de P + de type exponentiel sont les domaines de la forme

Ωexp(u0, C, K) = {w ∈ P +; u > u0, |v| < C(exp(u/K) − 1)}

Ces domaines sont stables par addition (opration qui correspond une multiplication
dans la coordonne x = − log w).

Dﬁnition IA3. Les domaines standards d’Ecalle-Il’yashenko sont les ouverts Ω de
P + qui contiennent un domaine de type puissance. On note EI l’ensemble de tels
domaines.

En particulier les domaines de type puissance et les domaines de type expo-
nentiel, sont des domaines standards. Une intersection ﬁnie et une union ﬁnie de
domaines standards est encore un domaine standard. Soit Ω ∈ EI, si t ∈ C est
tel que t + Ω soit inclus dans l’intrieur de P +, alors t + Ω ∈ EI, et si t > 0,

7

alors tΩ ∈ EI (la translation w ↦→ t + w correspond une homothtie x ↦→ ax, et
l’homothtie w ↦→ tw correspond une ramiﬁcation x ↦→ x
s).

Les domaines de type puissance et les domaines de type exponeniel sont bi-
holomorphiquement conjugus un ouvert contenant P +, par un diﬀomorphisme φ.
strictement rel et qui est quivalent l’identit l’inﬁni

φpuis(w) = w − 1
C1/K cos(π/2K) w1/K − U0

φexp(w) = w − K log(w) − U0 U0 > 0

Ecalle [E] et Il’yashenko [I] ont exhib´e, pour l’application de Dulac d’un col
hyperbolique rel, un type de tels domaines: exponentiel pour le premier (et ceci est
optimal pour les cols hyperboliques analytiquement normalisables: voir appendice
VA), et polynomial pour le deuxi`eme (K = 2).

L’application de Dulac d’une quation diﬀrentielle dans le domaine de Poincar
n’est pas borne sur un domaine de EI (voir appendice VA). Ceci motive la

Dﬁnition IA4. L’alg`ebre QA
p,q(x, α) ⊂ SBp,q(x, α) est l’ensemble des germes
f = ∑ fnα
n dont les coeﬃcients fn admettent un prolongement holomorphe et born
sur un mme domaine Ω ∈ EI p dans les coordonnes w = (wj = − log(xj))j=1,... ,p.

Ces algbres sont quasi-analytiques au sens suivant: soit Mx = ⟨x1, . . . , xp⟩ l’idal
de SBp,q engendr par les fonctions coordonnes xj, alors

(2) QA
p,q ∩ (∩nMn
x) = {0}

Pour p = 1 et q = 0, ce rsultat a t dmontr par Il’yashenko dans [I], par une double
application du principe de Phragmen-Lindelof dans P + ([Ru, p.244]), en utilisant
le diﬀomorphisme φpuis. Dans le cas gnral, notons Mx,0 l’idal de SBp,0(x) engendr
par les fonctions coordonnes xj ; si f = ∑k fkα
k ∈ QA
p,q ∩(∩nMn
x), alors pour tout
multi-indice k: fk ∈ QA
p,0∩(∩nMn
x,0) (par une simple identiﬁcation des coeﬃcients
des sries en α). Donc pour p = 1, on obtient encore l’galit (2). Supposons p > 1
et considrons la restriction de fk un voisinage de la diagonale de (R+∗)
p: soit
l’application g : (y, β) ∈ R+∗ ×Rp−1 ↦→ x = g(y, β) = (y, y(1+β1), . . . , y(1+βp−1)).
Soit U ∈ ((R+∗)
p, 0) sur lequel est ralise fk (il est indpendant de k), et soit V ∈
(R+∗ × Rp−1, 0) tel que g(V ) ⊂ U . Soit Fk le germe en 0 de fk ◦ g|V , c’est un
lment de l’anneau SB1,p−1(y, β) (car le germe l’inﬁni du translat complexe de tout
secteur Sθ est inclus dans le germe l’inﬁni d’un secteur Sθ′). Soit My l’idal de
SB1,p−1 engendr par la coordonne y, par la stabilit des domaines standards par
intersection ﬁnie et par translation, on a Fk ∈ QA
1,p−1 ∩ (∩nMn
y ) (on a mme que
Fk ∈ QA
1,0(y){β}, la srie tant convergente sur un produit Ω0 × W o Ω0 est un
domaine standard et W est un voisinage de 0 dans Cp−1). Le germe Fk est donc
identiquement nul, et il en est de mme pour fk et pour f .

Ces alg`ebres sont stables par les d´erivations χj (par les formules de Cauchy
dans les coordonnes wj dans les translats 1 + Ωj). Leur localit est un problme
ouvert. Elles sont strictement incluses dans les algbres SBp,q: en eﬀet, le germe

8

f (x) = x
log(− log(x) ∈ SB1,0(x) ∩ (∩nMn
x) (pour cela, il suﬃt de voir que pour tout
n ∈ N, le relev fn(w) = exp(−w(log(w) − n)) est born sur tout germe (Sθ, ∞) avec
θ ∈]0, π/2[). Cependant, si p > 0, la topologie de Krull de l’anneau QA
p,q (induite
par celle de l’anneau SBp,q) n’est pas spare (pour tout s > 0, x
s
1 ∈ M, o M est l’idal
maximal de SBp,q). Et les idaux les plus simples des anneaux QA
p,q ne sont pas
noethriens (ni dans l’anneau QA
p,q ni mme dans son extension A
p,q): tel est le cas
par exemple des idaux engendrs par les fonctions lmentaires fn = x(log x)
n ou
gn = x
1/n. Ainsi, une structure asymptotique dans un nombre ﬁni de fonctions
lmentaires est souhaitable.

§4. Algbres quasi-rgulires d’Hilbert QRHp,q.

La derni`ere condition de r´egularit´e qu’on impose sur les germes ´etudi´es est
l’existence d’une structure asymptotique lmentaire dans les variables quasi-ana-
lytiques xj. Pour (y, β) ∈ R+∗ × R, notons Ld (pour Logarithme d´eploy´e) la
fonction

(3) Ld(y, β) = ∫ y

1 t−1+βdt =
 



 yβ − 1
β pour β ̸= 0

log y pour β = 0

Ceci est simplement le compensateur ´el´ementaire d’Ecalle-Roussarie [E], [Ro2]. La
fonction f (y, β) = yLd(y, β) ∈ QA
1,1(y, β): soit F (w, β) = f (exp(−w), β) et soit
θ ∈ [0, π/2[, en faisant le changement de coordonnes t = exp(−z) dans l’intgrale
(3), on vriﬁe facilement que pour |β| suﬃsament petit, on a |F (w, β)| ≤ 1/ cos(θ)
sur le secteur Sθ. De plus, F (w, β) = ∑ Fn(w)βn avec

Fn(w) = 1
(n + 1)! (−w)
n+1 exp(−w)

chaque fonction Fn est borne sur le domaine exponentiel Ωexp(0, 1, n+2) et sur tout
compact de P +. Les fonctions Fn sont donc bornes sur n’importe quel domaine de
type puissance (voir appendice VA pour une preuve gnrale).

Soit q = (q1, q2) ∈ N2 et α = (µ, ν) des coordonnes sur Rq1 × Rq2 . Soient les
fonctions lmentaires zi,0(xi) = xi log xi et zi,j leurs d´eploiements

(4) zi,j(xi, µj) = xiLd(xi, µj)

Ces fonctions appartiennent `a l’algbre QA
1,1. Dans la suite, certaines notations
(de sens clair dans le texte) dsignent aussi bien des fonctions que les coordonnes
correspondantes. Soient

(5) Xi = (xi, zi,0, zi,1, · · · , zi,q1 ) et X = (X1, . . . , Xp)

Notons ̂x
i = (x1, · · · , xi−1, xi+1, · · · , xp) et ci et c les immersions

(6) ci(x, α) = (Xi, ̂x
i, α) c(x, α) = (X, α)
 9

Dﬁnition IA5. Convenons que QRH0,q(α) = R{α}. Alors, l’alg`ebre quasi-r´egu-
li`ere d’Hilbert QRHp,q(x, α) ⊂ QA
p,|q|(x, α) est l’ensemble des germes f ayant un
d´eveloppement asymptotique de ”type Hilbert”: pour tout i = 1, · · · , p, il existe
une suite (Gi,m)m dans QRHp−1,q(̂xi, α)[Xi] qui sont des polynˆomes homog`enes de
degr´e m dans la variable Xi telle que pour tout n ∈ N

(7) f (x, α) = ∑n

m=0Gi,m ◦ ci(x, α) + x
n
i hn avec hn ∈ SBp,|q|
0

Les variables analytiques ν n’interviennent pas dans la construction des fonctions
lmentaires (4), d’o la distinction faite dans les variables analytiques α. Dans le
problme d’Hilbert, les variables µ sont les paramtres qui dploient les valeurs propres
des singularits, et les variables ν sont tout autres paramtres.

L’unicit des sries formelles (7) ainsi que l’injectivit des morphismes srie formelle
associs sont dmontrs dans la section II. On y dmontre aussi l’existence et l’injectivit
d’un morphisme srie formelle f ∈ QRHp,q ↦→ ̂f ∈ c∗(R{α}[[X]]); ceci implique en
particulier que la topologie de Krull des algbres QRHp,q est spare. Les germes
quasi-analytiques (∈ QA
p,|q|) qui possdent une telle srie formelle forment une sur-
algbre de QRHp,q qui ne sera pas tudi dans ce travail. La sous-alg`ebre QRHp,q
cvg
des ´el´ements ”convergents” de l’alg`ebre QRHp,q est d´eﬁnie par

Dﬁnition IA6. On note QRHp,q
cvg = c∗(R{X, α}).

Une consquence algbrique de la transcendance du graphe de c est que le morphisme
c∗ est un isomorphisme sur son image. Ceci est dmontr aussi dans le section II.

B. Quelques gnralits et six lemmes de base.

Les anneaux de rfrence sont les anneaux locaux B telles que R{x, α} ⊂ B ⊂
A
p,q(x, α) et qui sont stables par les drivations

p∏

j=1 xj ∂
∂yi avec y = (x, α)

Ce sont des R-algbres. Dans la suite, on parlera indiﬀrement d’anneau ou d’alg-
bre. L’idal maximal de B est l’idal des germes nuls en 0. En cas d’ambiguit, on
note B(y) pour prciser le choix des coordonnes.

1. Anneaux restriction et anneaux extension.

Soit U un repr´esentant de ((R+∗)
p × Rq, 0) et soit Bp = {∏p
j=1 xj = 0} le
bord associ de germe (Bp, 0) en 0. Soit UO ⊂ U un sous-ensemble quelconque
dont l’adhrence contient 0. On note (U0, 0) le germe de U0 en 0 . On note aussi
∂0U0 = Bp ∩ U0 le bord associ et ∂0(U0, 0) son germe en 0. Soit B ⊂ A
p,q(y) un
anneau de rfrence et soit iU0 : (U0, 0) → (U, 0) le germe de l’injection canonique
(qu’on notera aussi iU0,U en cas d’ambiguit). On lui associe un morphisme toil

i∗
U0 : f ∈ B ↦→ i∗
U0 (f ) = f ◦ iU0

10

On gnralise ainsi les anneaux de rfrence B aux anneaux restriction nots B|U0 et
dﬁnis comme suit:
 B|U0 = i∗
U0 (B)

C’est un anneau local (qui n’est pas forcment intgre). Il ne dpend de U0 que par
son germe (U0, 0). Il est isomorphe B (par i∗
U0 ) si (U0, 0) est d’intrieur non vide
(ie. l’adhrence de l’intrieur de U0 contient 0): en eﬀet, une fonction analytique
nulle sur un ouvert connexe est nulle sur la composante connexe de son domaine
d’analycit contenant cet ouvert. Le sous-ensemble U0 est dit semi-analytique
lmentaire de B (ou dcrit par B) s’il existe V ∈ (U, 0) et contenant U0 et des
germes f1, . . . , fn, g1, . . . , gm ∈ B et reprsents sur V tels que

U0 = {y ∈ V ; f1(y) > 0, . . . , fn(y) > 0, g1(y) = 0, . . . , gm(y) = 0}

Il est dit semi-analytique de B (ou dcrit par B) si c’est une union ﬁnie de semi-
analytiques lmentaires de B. Dans ce cas, le morphisme i∗
U0 est un isomorphisme
si et seulement si (U0, 0) est d’intrieur non vide: en eﬀet, si U0,1, . . . , U0,ℓ sont les
semi-analytiques lmentaires formant U0, l’un des U0,j est un ouvert dont l’adhrence
contient 0, sinon il existe gi1,1, . . . , giℓ,ℓ ∈ B \ {0} tels que g = gi1,1 × · · · × giℓ,ℓ
est nulle sur (U0, 0); mais par l’isomorphisme i∗
U0, g est alors nulle, ce qui contredit
l’intgrit de B.

Soit I un idal de B. Le morphisme i∗
U0 tant surjectif, le sous-ensemble i∗
U0(I) est
un idal de B|U0 dit idal restriction. On le note simplement I|U0 ; il ne dpend de U0
que par son germe (U0, 0). Inversement, tout idal J de B|U0 est un idal restriction:
I = (i∗
U0 )
−1(J) est un idal de B et I|U0 = J.

Soit B′ ⊂ A
p
′,q′ (x
′, α
′) un anneau de rfrence. Soit U ′ ∈ ((R+∗)
p
′ × Rq′ , 0) et
soit U ′
0 un sous-ensemble de U ′ dont l’adhrence contient 0. L’anneau B′
|U ′
0 est
dit anneau extension de l’anneau B|U0 s’il existe un homomorphisme d’anneaux
injectif Ψ : B|U0 ֒→ B′
|U ′
0. Dans ce cas, si J est un id´eal de B|U0, on appelle idal
prolong associ J l’idal de B′
|U ′
0 engendr´e par le sous-ensemble Ψ(J). On le notera
simplement Ψ(J) si aucune confusion n’est craindre. Cet idal prolong est aussi un
idal restriction.

Soit ψ : U ′
0 → U0 un morphisme surjectif, continu sur U ′
0 ∪ {0} et tel que
ψ(0) = 0. On note de la mme faon son germe ψ : (U ′
0, 0) → (U0, 0). Ce germe induit
un morphisme toil ψ∗ qui agit sur l’anneau B|U0 et qui est injectif. On suppose que
ψ∗(B|U0) ⊂ B′
|U ′
0. Dans ce cas, on dira que l’anneau B′
|U ′
0 est une extension toile
de l’anneau B|U0 et on la note (B′
|U ′
0, ψ). Si g est un lment de B|U0, on a la relation
suivante entre les germes en 0 des ensembles de zros

(0) Z(ψ∗(g)) = ψ−1(Z(g))

Dans toute la suite, on ne considrera que des extensions toiles.
 11

Dﬁnition IB1. Soit I un idal de B.

(i) On dit que I est ”noethrien” sur U0 (ou que I|U0 est ”noethrien”) s’il ex-
iste une extension toile (B′
|U ′
0, ψ) de B|U0 dans laquelle l’idal prolong ψ∗(I|U0 )
est noethrien dans le sens classique: il existe h1, . . . , hn ∈ ψ∗(I|U0 ) tels que
pour tout h ∈ ψ∗(I|U0 ), il existe H1, . . . , Hn ∈ B′
|U ′
0 tels que h = ∑n
j=1 Hjhj.

(ii) On dit que I est localement ”noethrien” sur U0 (ou que I|U0 est locale-
ment ”noethrien”) s’il existe une subdivision ﬁnie de U0 en des sous-
ensembles Ui,0 qui adhrent 0 et telle que I soit ”noethrien” sur chaque
Ui,0.

Si (U0, 0) = (U, 0), on dit simplement que I est ”noethrien” ou localement ”noeth-
rien”. Dornavant, on enlve les guillemets au mot ”noethrien”. En cas d’ambigui-
t, on prcisera l’anneau de rfrence pour les idaux prolongs (qui est aussi l’extension
toile associe). Soit J ⊂ B|U0 un idal noethrien et soit (B′
|U ′
0, ψ) l’extension associe.
On sait dﬁnir le germe en 0 de l’ensemble des zros de l’idal prolong ψ∗(J): c’est
celui de n’importe quel systme ﬁni de gnrateurs de cet idal dans l’anneau B′
|U ′
0.
Maintenant, si g1, . . . , gn ∈ J sont tels que ψ∗(g1), . . . , ψ∗(gn) forment un systme
de gnrateurs de ψ∗(J) (il en existe), la relation (0) montre que le germe Z(g1) ∩
· · · ∩ Z(gn) est indpendant du systme ainsi choisi, et qu’on a donc une notion
d’ensemble des zros de l’idal J, qu’on note Z(J) et qui est donn par la formule
(ψ tant surjective)

(1) Z(ψ∗(J)) = ψ−1(Z(J))

En particulier, pour tout g ∈ J, on a g|Z(J) = 0.

2. Projection unidimensionnelle.

Soit ΞB la classe des germes en 0 de champs de vecteurs χ = ∑p+q
j=1 aj(y)∂/∂yj
dont les composantes aj sont des ´el´ements de B, et qui satisfont aux conditions
suivantes

(i) Sing(χ) ⊂ (Bp, 0): il existe un ouvert U ∈ ((R+∗)
p × Rq, 0) tel que le champ
χ se prolonge par continuit U et tel que l’ensemble singulier de χ sur U
soit inclus dans ∂0U .

(ii) (Bp, 0) est invariant par χ: il existe U comme dans (i) tel que ∂0U est une
union d’orbites de χ dans U .

(iii) χ(B) ⊂ B.

Un ouvert U satisfaisant aux conditions (i) et (ii) est dit admissible. Soit
χ ∈ ΞB et soit U un ouvert admissible. Soit ϕχ,U le ﬂot de χ dans U ; on note
πχ,U : U ↦→ ̃U = U/ϕχ,U la projection le long des orbites de χ dans U (on
l’appelle aussi le morphisme intgral de χ dans U ). L’espace ̃U tant muni de
la topologie quotient. Cette projection est donc continue et ouverte. Soit S ⊂
(R+∗)
p × Rq dont l’adhrence contient 0

12

Dﬁnition IB2. Le degr´e de la projection πχ,U restreinte au sous-ensemble S
est
 dπχ,U|S = sup
γ⊂U b0(γ ∩ S)

o γ est une orbite de χ dans U , et b0 est le premier nombre de Betti. On note

dπχ|(S,0) = inf
U dπχ,U|S

o la borne infrieure est prise sur tous les ouverts U admissibles.

La notation πχ dans cette dﬁnition, ne dsigne pas un germe. En gnral, il n’existe
pas de notion de germe en 0, pour la projection intgrale, qui soit indpendante des
ouverts U (ou du moins d’une base d’ouverts U ). Quand il en existe une, on note ce
germe πχ; c’est par exemple le cas quand le champ χ admet une orbite ”principale”
dans U (cf. ﬁn de cette section), ou plus gnralement, quand il admet dans U ,
(p + q − 1) intgrales premires Fj, analytiques et indpendantes: la (p+q-1)-forme
dF1 ∧ · · · ∧ dFp+q−1 ne s’annule pas sur U .

2.1 χ-rgularit et χ-ﬁnitude.

Soit U0 ⊂ (R+∗)
p × Rq dont l’adhrence contient 0. On dit que le germe (U0, 0)
(ou simplement U0) est invariant par χ s’il existe un ouvert U admissible tel que
U0 ∩ U soit une union d’orbites de χ dans U .

Dﬁnition IB3. Soit f ∈ B et Z(f ) le germe en 0 de son ensemble des zros. On
dit que f est χ-r´eguli`ere sur U0 si

dπχ|Z(f )∩(U0,0) < +∞

Si (U0, 0) = (U, 0) o U est un ouvert admissible, on dit simplement que f est
χ-rgulire. Van Den Dries parle dans l’un de ces travaux ([Dr]) d’une certaine
”proprit de ﬁnitude” (qui porte justement sur des projections unidimensionnelles
mais linaires!), qui est quivalente cette notion de χ-rgularit. Soit Iχ,f = ⟨χnf ; n ∈
N⟩ l’idal diﬀrentiel de f dans l’anneau B. Si U ′ ⊂ U est un ouvert admissible sur
lequel est ralise f , alors tous les germes χnf sont aussi raliss sur U ′. On note Z(Iχ,f
le germe en 0 de ∩n∈NSn, o Sn est un reprsentant de Z(χnf ) sur U ′. Cette dﬁnition
de l’ensemble des zros d’un idal diﬀrentiel coincide avec la dﬁnition classique en cas
de noethrianit. Remarquer que le germe Z(Iχ,f ) est invariant par χ.

Dﬁnition IB4. On suppose que f est χ-rgulire sur U0,

(i) on dit que f est χ-ﬁnie sur U0 si l’id´eal diﬀrentiel Iχ,f est noeth´erien sur
U0.

(ii) On dit que f est localement χ-ﬁnie sur U0 si Iχ,f est localement noeth-
rien sur U0, la subdivision associe tant invariante par χ.
 13

Dﬁnition IB5. Une classe C ⊂ B est dite χ-ﬁnie sur U0 (resp. localement
χ-ﬁnie sur U0) si tout f ∈ C est χ-ﬁnie sur U0 (resp. localement χ-ﬁnie sur U0).
Elle est dite χ-stable si χ(C) ⊂ C.

Si (U0, 0) = (U, 0) o U est un ouvert admissible, on dit simplement que f (ou la
classe C) est χ-ﬁnie, ou alors que f (ou la classe C) est localement χ-ﬁnie.

2.2 Six lemmes de base.

Le premier de ces lemmes, qui est un lemme fondamental, donne les proprits
de ﬁnitude d’une certaine classe de germes qui sont ”bien prpars” et dans une
extension approprie. On suppose donc dans ce lemme que les anneaux de rfrence
pour la noethrianit, sont les anneaux restriction B|U0. Soit M l’idal maximal de B

Lemme IB1 (lemme de χ-ﬁnitude). Soit B0 ⊂ B une alg`ebre χ-ﬁnie sur U0
(resp. localement χ-ﬁnie sur U0) et χ-stable. Soit M0 ⊂ M un id´eal χ-stable.
Soit NU0 ⊂ B l’idal des germes nuls sur (U0, 0). Alors la classe CB0,M0 = {f ∈
g + M0Iχ,g + NU0 ; g ∈ B0} ⊂ B est χ-ﬁnie sur U0 (resp. localement χ-ﬁnie sur
U0).

Preuve. Il suﬃt de la faire dans le cas de χ-ﬁnitude sur U0. Soit g ∈ B0 et soit

(2) f ∈ g + M0Iχ,g + NU0

Le germe (U0, 0) tant invariant par la drivation χ, l’idal NU0 est χ-stable. La
relation (2) implique donc que Iχ,f |U0 ⊂ Iχ,g|U0 . Montrons d’abord que l’id´eal
Iχ,f |U0 est noeth´erien dans l’anneau B|U0. L’algbre B0 tant χ-ﬁnie sur U0, l’idal
Iχ,g|U0 est noethrien dans l’anneau B|U0. Soit (g|U0 ), . . . , ((χℓg)|U0)) un systme de
gnrateurs de l’idal Iχ,g|U0 . L’idal maximal de B|U0 est M′ = M|U0 (car les lments
de B ⊂ A
p,q sont continues en 0). Comme M0 ⊂ M, on a M′
0 = (M0|U0 ) ⊂ M′.
En appliquant ℓ fois la drivation χ la relation (2), puis en prenant la restriction
(U0, 0), on obtient
 Iχ,g|U0 ⊂ Iχ,f |U0 + M′
0Iχ,g|U0
Comme l’idal Iχ,g|U0 est noethrien, le Lemme de Nakayama (cf. [L]) implique que
Iχ,g|U0 ⊂ Iχ, f |U0. On obtient alors Iχ,f |U0 = Iχ,g|U0 . L’idal Iχ,f |U0 est donc
noethrien dans l’anneau B|U0.

Montrons maintenant que f est χ-r´eguli`ere sur U0. Soit F = Z(Iχ,f |U0 ) ⊂ (U0, 0)
l’ensemble des z´eros de l’id´eal Iχ,f |U0 ; il est invariant par χ et dπχ|F ≤ 1. Or, on
a aussi F = Z(Iχ,g). Soit U un ouvert admissible tel que U0 ∩ U soit une union
d’orbites de chi dans U . Soit U ′ ⊂ U un ouvert admissible o sont raliss le germe g et
la relation (2). le sous-ensemble U0 ∩ U ′ est encore une union d’orbite de χ dans U ′.
Notons S le reprsentant du germe F sur U ′ et considrons alors les sous-ensembles

Sj = {m ∈ U ′ ∩ U0; |χjg(m)| = ℓ
max
i=0 |χig(m)|} \ S

Si U ′ est suﬃsament petit, une orbite γ de χ dans U ′ ∩ U0 rencontre Sj en un
nombre ﬁni d’intervalles σ de γ (dont certains peuvent tre rduits un point), et

14

ce nombre est uniform´ement major´e par un entier nj qui ne d´epend que de Sj.
En eﬀet, les extr´emit´es m de ces intervalles σ qui appartiennent γ satisfont des
´equations du type
 g±
i,j(m) = χjg(m) ± χig(m) = 0 i ̸= j

et ces germes g±
i,j (en nombre ﬁni) sont des lments de l’algbre B0 qui est χ-stable
et χ-ﬁnie sur U0. Si on note S±
i,j le reprsentant de Z(g±
i,j) sur U ′, on peut donc
prendre
 nj = ∑

i̸=j dπχ,U ′|S±
i,j∩U0

Maintenant, sur un de ces intervalles σ (non rduit un point!), considrons la fonction
fσ(t) = f ◦ ϕχ,U ′ (t, m) o m est un point de σ et t dcrit un intervalle τ de R tel
que ϕχ,U ′ (τ, m) = σ. Un calcul direct montre que les drivves successives de fσ sont
donnes par
 f (i)
σ (t) = χif ◦ ϕχ,U ′ (t, m)

Et la relation (2) drive j fois par rapport χ et restreinte U0 ∩ σ donne

(χjf )|U0∩σ = (χjg)|U0σ(1 + O(m))

Ceci montre que la drive j-me de fσ ne s’annule pas sur l’intervalle τ . Par consquent
et par le Lemme de Rolle appliqu la fonction fσ sur l’intervalle τ , on a

dπχ,U ′|S′∩U0 ≤
 ℓ∑

j=0 jnj ≤ ℓ
 ℓ∑

j=0 nj

o S′ est le reprsentant du germe Z(f ) sur U ′. □

L’hypothse M0 ⊂ M du lemme ne peut tre aﬀaiblie, comme le montre l’exem-
ple suivant: χ = x∂/∂x, g = x, h = −1 + sin(1/x) exp(−1/x) et f = g + hg;
B tant un anneau χ-stable contenant l’anneau R{x} et les drives successives χnh,
et B0 = R{x}. La ”bonne prparation” du lemme est rapprocher de celle que
l’on rencontre dans l’tude des singularits d’applications diﬀrentiables, et qui utilise
uniquement ”l’idal jacobien”. Ce qui consiste en fait regarder l’action simultane
de plusieurs drivations. Il faut noter que les algbres tudies dans ce travail ne sont
pas diﬀrentiables en 0.

Notons Cχ,B = {f ∈ B; Iχ,f noethrien dans B}. Soit la relation sur Cχ,B: f Rg ⇔
il existe un idal M0 ⊂ M χ-stable tel que f − g ∈ M0Iχ,g. D’aprs la preuve
prcdente, c’est une relation d’quivalence sur Cχ,B dite χ-quivalence dans B. Soient
C1 et C2 des algbres ou des classes telles que C1 ⊂ C2 ⊂ Cχ,B. On dit que C2 est
χ-quivalente C1 dans B si tout lment de C2 est χ-quivalent un lment de C1 dans
B. Ainsi, si C1 est une algbre χ-stable et χ-ﬁnie, le lemme de ﬁnitude dit que la
classe C2 ⊂ ∪M0 CM0,C1 est χ-ﬁnie (l’union tant prise sur tous les idaux M0 ⊂ M
et qui sont χ-stables).

Construction d’algbre χ-ﬁnie. Il en existe un grand nombre d’aprs la riche
littrature sur les proprits de ﬁnitude des sous-ensembles analytiques avec de fortes

15

conditions au bord ([T]), les sous-ensembles pfaﬃens et les constructions drives de la
thorie de l’o-minimalit ([W], [D-M-M], [L-R], [L-S], [D-S], [S]...); malheureusement,
la question de la noethrianit est rarement tudie dans ces derniers travaux. Un
exemple simple de construction, dduit des ides originales de Khovanski-Tougeron,
est illustr dans la section II par l’tude des sous-algbres convergentes QRHp,q
cvg. Il
s’appuie sur les ides suivantes

Lemme IB2 (lemme d’extension de Tougeron). Soit B0 une sous-alg`ebre de
B stable par χ. On suppose que

(i) les semi-analytiques dcrits par B0 ont un nombre ﬁni de composantes con-
nexes.

(ii) l’anneau B0 est noeth´erien dans B.

(iii) Il existe (p + q − 1) 1-formes ωj = ∑p+q
i=1 ai,jdyi avec ai,j ∈ B0, et un
ouvert admissible U telles que toute orbite de χ dans U soit une intersection
transverse de solutions sparantes des ωj.
Alors, l’alg`ebre B0 est χ-ﬁnie.

Preuve. L’hypothse (i) implique en particulier que les idaux diﬀrentiels de B0
sont noethriens dans B. Les hypothses (i) et (ii) impliquent que l’algbre B0 est
topologiquement noethrienne (cf. [T]). Si S est un semi-analytique de B0 et γ une
orbite r´eguli`ere de χ dans U

b0(γ ∩ S) = b0((∩
p+q−1
j=1 Γj) ∩ S)

o chaque Γj est une solution sparante de ωj. Par l’hypothse (iii), ces 1-formes sont
coeﬃcients dans B0. Donc, par la th´eorie de Khovanski -Tougeron ([K1], [K2], [T]),
ce nombre est major par un entier qui ne dpend que de S et des ωj. Et donc, tout
f ∈ B0 est χ-rgulier. □

Si de plus, B0 est un anneau de rfrence, on peut simpliﬁer l’hypothse (iii) comme
ceci: la drivation χ admet (p+q−1) intgrales premires indpendantes Fj ∈ B0. Cette
hypothse ne peut tre aﬀaiblie, commme le montre l’exemple suivant: prenons p = 1
et q = 2, soient B0 = R{x, α1, α2} et

χ = −x ∂
∂x + (aα1 − bα2) ∂
∂α1 + (bα1 + aα2) ∂
∂α2
avec a > 0 et b ̸= 0. Il est clair que l’anneau B0 ⊂ A
1,2(x, α) est un anneau de
rfrence qui est χ-stable et qui satifait aux hypothses (i) et (ii). Cependant, le germe
f = α1 ∈ B0 n’est pas χ-rgulier. Et le lemme I2 montre que la drivation χ n’admet
pas de paire d’intgrales premires indpendantes, dans aucun anneau de rfrence qui
satisfait aux hypothses (i) et (ii). Un calcul direct montre qu’il existe une paire
d’intgrales premires indpendantes qui sont linaires en α et dont les coeﬃcients
sont les fonctions oscillantes x
a cos(b log(x)) et x
a sin(b log(x)), qui appartiennent
l’anneau A
1,0(x) mais pas l’anneau SB1,0(x).

Faisceau diﬀrentiel.

Soient f ∈ B et χ ∈ ΞB. Soit U un ouvert admissible pour χ sur lequel f
est ralise. On note Iχ,f [U ] le faisceau diﬀrentiel de f sur U : sa ﬁbre Iχ,f,m

16

(qu’on note aussi Iχ,f (m)), en un point m ∈ U , est l’idal diﬀrentiel Iχm,fm ⊂
Bm = R{y − ym}; χm et fm tant les germes de χ et f en m, et y − ym sont les
coordonnes locales en m (les reprsentants d’lments de R{y − ym} tant considrs sur
des ouverts connexes). On suppose qu’en tout point m du bord ∂0U , il existe un
anneau de rfrence Bm ⊂ A
pm,qm(y − ym), qui est stable par χm (ainsi χm ∈ ΞBm)
et qui contient les germes en m d’lments de B qui sont reprsents sur un voisinage
de m ( en gnral, on choisi Bm comme tant l’anneau de ces germes). Dans ce
cas, on prolonge le faisceau Iχ,f [U ] par le faisceau Iχ,f [U ∪ ∂0U ], dont les ﬁbres
diﬀrentielles sur le bord ∂0U sont les idaux diﬀrentiels Iχm,fm des anneaux Bm
correspondants. Ce faisceau est donc le faisceau associ au prfaisceau F [U ∪ ∂0U ]
muni des morphismes restriction naturels, et dont les sections F (V ) (o V est un
ouvert de U ∪ ∂0U ) sont les idaux engendrs par la famille (χnf )n∈N dans l’anneau
des fonctions sur V dont le germe en tout point m ∈ V , est un lment de l’anneau
local Bm.

On montre deux rsultats importants concernant ces faisceaux. Conjointement
au lemme de ﬁnitude, ces rsultats (et leurs consquences) constituent le socle de ce
travail.

Lemme IB3 (lemme de cohrence). Le faisceau Iχ,f [U ] est cohrent: plus prcis-
ment, pour tout m ∈ U , il existe un ouvert Vm ⊂ U contenant m, et un entier ℓm
tels que en tout point m′ ∈ Vm, la ﬁbre Iχ,f (m′) est engendre par les germes en
m′ de (f, χf, . . . , χℓmf ). Si de plus, la ﬁbre en 0 Iχ,f (0) = Iχ,f est noethrienne
dans B, alors il existe un ouvert V ∈ (U, 0) et contenu dans U tel que le faisceau
Iχ,f [U ∪ ∂0V ] soit cohrent.

Preuve. Si la ﬁbre en 0 est noethrienne et si (f , χf, . . . , χℓf ) est un systme de
gnrateurs de Iχ,f dans B, alors il existe un voisinage ouvert V de 0 dans U tel que
la division
 χl+1f =
 ℓ∑

i=0 hiχif

soit ralise sur un voisinage de V dans U ∪ ∂0U . En drivant plusieurs fois cette galit,
on obtient que pour tout k, la division

χkf =
 ℓ∑

i=0 hi,kχif

est ralise sur ce mme voisinage. On obtient le rsultat en germiﬁant ces galits en
n’importe quel point de V ∪ ∂0V . Le reste du lemme s’obtient de la mme faon, car
pour tout m ∈ U , l’anneau Bm = R{y − ym} est noethrien. □

Soit (χi, Bi)i=1,2 deux couples tels que Bi est un anneau de rfrence et χi est
une drivation appartenant ΞBi. Soit Ui un ouvert admissible pour χi et soit
ϕ : U1 → U2 un diﬀomorphisme tel que ϕ∗(χ1) = χ2. On suppose que ϕ se
prolonge en un homomorphisme de U1 ∪ ∂0U1 sur U2 ∪ ∂0U2 tel que ϕ(0) = 0. On
note de la mme faon son germe en 0 ϕ : (U1, 0) → (U2, 0) (ainsi que celui de ϕ
−1),
et on suppose que ϕ
∗(B2) = B1 (donc ϕ
∗ est un isomorphisme et (ϕ
∗)
−1 = (ϕ
−1)
∗).
Un calcul direct montre que le diagramme suivant est commutatif
 17

B2 ϕ∗
−−−−→ B1

χ2

↓ 

↓χ1

B2 ϕ∗
−−−−→ B1

Donc, si f1 ∈ B1 et f2 = (ϕ
−1)
∗(f1), alors pour tout entier n

χn
1 f1 = ϕ
∗(χn
2 f2)

et par consquent
 Iχ1,f1 = ϕ
∗(Iχ2,f2)

Ceci est fortiori vrai aux voisinages de points m1 ∈ U1 et m2 = ϕ(m1) ∈ U2, les
anneaux locaux correspondants tant les anneaux de germes de fonctions analytiques
en ces points (on les appelle aussi ”anneaux analytiques” pour simpliﬁer). On verra
dans la suite des situations plus gnrales de tels ”transfert”, dont la premire est

Lemme IB4 (lemme d’isomorphie de Roussarie). Le faisceau Iχ,f [U ] est
compatible avec la projection πχ,U . Autrement dit, si γ est une orbite de χ
dans U , et si m1, m2 ∈ γ, alors les ﬁbres Iχ,f,m1 et Iχ,f,m2 sont isomorphes,
l’isomorphisme tant le germe du ﬂot ϕχ,U aux voisinages de m1 et m2.

Preuve. Soit t0 tel que m2 = ϕχ,U (t0, m1). Soient m′
1 ∈ U un point voisin de m1,
t voisin de 0 et m′
2 = ϕχ,U (t, m′
1) ∈ U . Alors, un calcul direct donne

f (m′
2) = f (ϕχ,U (t, m′
1)) = ∑

n≥0 χnf (m′
1) tn

n!

la srie tant uniformment convergente sur le produit d’un voisinage de m1 dans U et
d’un voisinage de 0 dans R (le ﬂot tant analytique sur ce produit et f est analytique
sur un voisinage de m1). Les id´eaux de germes de fonctions analytiques en un point,
sont ferm´es pour la topologie de la convergence uniforme ([B-M], [H]). Par
consquent, Iχ,f,m1 ⊃ (ϕχ,U (t, .))
∗(Iχ,f,ϕχ,U (t,m1)), o ϕχ,U (t, .) dsigne aussi le germe
de ce diﬀomorphisme aux points m1 et ϕχ,U (t, m1). En considrant le ﬂot inverse
((ϕχ,U (t, .))
∗ est un isomorphisme entre les anneaux analytiques correspondants),
on obtient Iχ,f,m1 = (ϕχ,U (t, .))
∗(Iχ,f,ϕχ,U (t,m1)). Et, en utilisant un recouvrement
ﬁni du segment d’orbite [m1, m2], on obtient

Iχ,f,m1 = (ϕχ,U (t0, .))
∗(Iχ,f,m2 )

o ϕχ,U (t0, .) dsigne aussi le germe aux points m1 et m2 de ce diﬀomorphisme. □

Soit U ∈ ((R+∗)
p × Rq, 0) et soit c : m ∈ U ↦→ m′ ∈ Rn un morphisme continu
sur U ∪ ∂0U tel que c(0) = 0. On note de la mme faon son germe c : (U, 0) →
(Rn, 0). Soit u une coordonne locale sur (Rn, 0). L’anneau B = c∗(R{u}) est
dit anneau restriction analytique (ou encore anneau convergent). Il est
isomorphe l’anneau restriction de rfrence R{u}|c(U). Il est clair que c’est un anneau
local et noethrien (l’image rciproque par c∗ de tout idal est un idal, et l’anneau R{u}

18

est noethrien). Soit y = (x, α) des coordonnes sur U , on suppose maintenant que
le morphisme c est analytique, et qu’il s’crit dans les coordonnes y et u

u = c(y) = (y, ψ(y))

On suppose aussi que pour tout i = 1, . . . , n − (p + q), j = 1, . . . , p + q, il existe
hi,j ∈ R{u} tel que
 p∏

k=1 xk ∂ψi
∂yj = c∗(hi,j)

Dans ce cas, on vriﬁe facilement que l’anneau convergent B est un anneau de rfrence.
Soit
 χ =
 p+q∑

j=1 aj ∂
∂yj ∈ ΞB

Pour tout i = 1, . . . , n, le germe gi(u) = ui ∈ R{u}, donc c∗(gi) ∈ B et par
consquent χc∗(gi) ∈ B (en particulier, pour i = 1, . . . , p + q, on a χc∗(gi) = ai),
il existe alors hi ∈ R{u} (il n’est pas unique en gnral!) tel que χc∗(gi) = c∗(hi).
Soit U ′ ⊂ U un ouvert admissible pour χ tel que les germes hi soient raliss sur un
ouvert U ∈ (Rn, 0) et contenant c(U ′). Soit

X =
 n∑

i=1 hi ∂
∂ui

c’est une drivation analytique ralise sur U. Le morphisme c est un diﬀomorphisme
de U ′ sur la varit analytique c(U ′) (c est une immersion), et par la construction de
X , on a

(*) c∗χ = X|c(U ′)

(on note encore de la mme faon le diﬀomorphisme associ c, et son germe en 0).
Ainsi, le diagramme suivant est commutatif

R{u} c∗
−−−−→ B

X 

↓ 

↓χ

R{u} c∗
−−−−→ B

Le diﬀomorphisme c se prolonge en un homomorphisme de U ′ ∪ ∂0U ′ sur son
image. Soit m ∈ ∂0U ′ et m′ = c(m), on note cm : (U ′, m) → (Rn, m′) le germe de c
aux points m et m′. Soit R{u − um′} l’anneau analytique local au point m′, et soit
Bm = c∗
m(R{u − um′}), c’est un anneau restriction analytique qui est un anneau
de rfrence (par les mmes raisonnements que ci-dessus, en supposant bien sr que les
germes hi,j sont raliss sur U). Il est clair qu’il contient les germes en m d’lments de
B reprsents sur un voisinage de m. De plus, il est stable par la drivation χm (par
la commutativit du digramme obtenu partir de la relation (∗) germiﬁe aux points
m et m′).
 19

Ainsi, pour tout f ∈ B ralise sur un certain ouvert V ∈ (U, 0) (et V ⊂ U ′), le
lemme de cohrence dit que le faisceau Iχ,f [V ∪ ∂0V ] est cohrent. Par la continuit
de la drivation χ et du morphisme c sur le bord ∂0U ′, l’image par c d’une orbite
rgulire de χ incluse dans le bord, est une partie connexe d’une orbite rgulire de
X dans U. Le lemme d’isomorphie s’applique aux faisceaux diﬀrentiels IX ,g[Ug] le
long de toute orbite rgulire (Ug ⊂ U tant un un voisinage ouvert de 0, sur lequel
g est reprsente). Ainsi, en transportant par le morphisme c∗, on obtient que le
lemme d’isomorphie s’apllique aussi aux faisceaux Iχ,f [V ∪ ∂0V ] le long d’orbites
rgulires incluses dans le bord. En gnral dans ce travail, le morphisme c est
une immersion dont l’image est le graphe de fonctions lmentaires (et simples!) de
Khovanski. Un exemple, dj rencontr, de tels anneaux convergents, est l’anneau
QRHp,q
cvg (pour lequel le morphisme c∗ est un isomorphisme (cf. Section II)).

Si l’une des drivations X satisfait l’hypothse (iii) du lemme d’extension (on
bien si elle admet (n − 1) intgrales premires analytiques et indpendantes), alors
ce lemme dit que l’algbre R{u} est X -ﬁnie. Il est clair, dans ce cas, que l’anneau
convergent B est aussi χ-ﬁni: si f ∈ B et si g ∈ R{u} est tel que f = c∗(g), alors
par transport par l’injection c
 dπχ|Z(f ) ≤ dπX |Z(g)

Idal χ-transverse.

Soit B un anneau de rfrence. Soient f ∈ B et χ ∈ ΞB. Soit U un ouvert admissi-
ble sur lequel f est ralise. Soit γ une orbite rgulire de χ dans U . Soient m, m′ ∈ γ et
t0 > 0 tel que ϕχ,U (t0, m) = m′. Soit σm ⊂ U une transversale γ en m, analytique.
Quitte rduire σm, on suppose que pour t dans un voisinage de [0, t0], l’image de σm
par le ﬂot ϕχ,U (t, .) est incluse dans U . Ainsi, σm′ = ϕχ,U (t0, σm) est une transver-
sale γ en m′, analytique. Soient β des coordonnes analytiques locales sur (σm, m),
il est clair que l’anneau restriction de rfrence R{y − ym}|σm est isomorphe l’anneau
analytique R{β} (qui lui mme est isomorphe l’anneau des intgrales premires analy-
tiques locales en m (cf. ci-dessous)). Par le diﬀomorphisme analytique ϕχ,U (t0, .),
on peut prendre β comme coordonnes analytiques locales sur (σm′ , m′). Par cette
identiﬁcation, le lemme d’isomorphie dit alors que i∗
σm(Iχ,f,m) = i∗
σm′ (Iχ,f,m′ ), d’o

Dﬁnition IB6. On appelle idal χ-transverse de f le long de γ l’idal restriction

Jχ,f,γ = i∗
σm(Iχ,f,m) = Iχ,f,m|σm ⊂ R{β} ∀m ∈ γ

o les coordonnes analytiques β sur σm sont des intgrales premires de χ le long de
γ.

Et inversement, on peut reconstruire toute ﬁbre Iχ,f,m le long de γ partir de l’idal
transverse Jχ,f,γ: soit Um ⊂ U le satur de σm par le ﬂot ϕχ,U (t, .) pour t dans
un voisinage de 0. Il est clair que l’espace quotient ̃Um = Um/ϕχm,Um s’identiﬁe
la transversale analytique σm. Ainsi, on peut parler du germe de la projection
intgrale πχm,Um : Um → σm, qu’on note simplement πχm : (Um, m) → (σm, m). On
lui associe le morphisme toil π∗
χm : R{β} → R{y − ym} qui est injectif; son image
est l’anneau des intgrales premires analytiques locales en m. Avant de poursuivre,

20

faisons une remarque simple qui sera souvent utilise dans la suite: soient ψ∗
1, ψ∗
2
deux morphismes toils, et soit I un idal, alors l’idal prolong (par ψ∗
1) associ l’idal
prolong (par ψ∗
2) associ I, coincide avec l’idal prolong (par (ψ2 ◦ ψ1)
∗) associ I,
ce que l’on note (ψ2 ◦ ψ1)
∗(I) = ψ∗
1 ◦ ψ∗
2(I).

Lemme IB5 (lemme de saturation). Pour tout m ∈ γ, on a Iχ,f,m =
π∗
χm (Jχ,f,γ).

Preuve. On se place dans un ﬂow-box au voisinage de m. Quitte rduire Um, soit
ψ : (t, β) ∈ τ × Σm ↦→ m′ ∈ Um le diﬀomorphisme normalisant tel que ψ({0} ×
Σm) = σm et (ψ−1)∗(χm) = Y = ∂/∂t. Notons de la mme faon son germe ψ :
(τ × Σ, (0, 0)) → (Um, m). On a le diagramme commutatif

(∗)
 R{y − ym} ψ∗
−−−−→ R{t, β}

χm

↓ 

↓Y

R{y − ym} ψ∗
−−−−→ R{t, β}

o ψ∗ est un isomorphisme. L’orbite γ ∩ Um est envoye sur l’orbite Γ = τ × {0}.
Notons ψ1 : Σm → σm (et son germe aux points 0 et m) la restriction de ψ
{0} × Σm. C’est un diﬀomorphisme. La projection intgrale πY,τ ×Σm s’identiﬁe
avec la projection canonique π : τ × Σm → Σm; notons de la mme faon son germe
π : (τ × Σm, (0, 0)) → (Σm, 0). Les diagrammes suivants est commutatifs

(∗ ∗ 1)
 (τ × Σm, (0, 0)) ψ
−−−−→ (Um, m)

π

↓ 

↓πχm

(Σm, 0) ψ1
−−−−→ (σm, m)

(∗ ∗ 2)
 (Σm, 0) ψ1
−−−−→ (σm, m)

iΣm 

↓ 

↓iσm

(τ × Σm, (0, 0)) ψ
−−−−→ Um
Par le choix des coordonnes β sur Σm et σm, le morphisme toil ψ∗
1 est l’identit de
l’anneau R{β}; on a donc les diagrammes commutatifs

(∗ ∗ ∗1)
 R{β} id
−−−−→ R{β}

π∗
χm

↓ 

↓π∗

R{y − ym} ψ∗
−−−−→ R{t, β}

(∗ ∗ ∗2)
 R{y − ym} ψ∗
−−−−→ R{t, β}

i
∗
σm 

↓ 

↓i
∗
Σm

R{β} id
−−−−→ R{β}
 21

Ces deux derniers diagrammes sont aussi valables pour les idaux prolongs. Soit
F = ψ∗(fm) = ∑ an(β)tn, d’aprs le diagramme (∗), on a ψ∗(Iχ,f,m) = IY,F ⊂
R{t, β}. D’aprs la dﬁnition de l’idal transverse

JY,F,Γ = iΣm )
∗(IY,F ) = i∗
Σm ◦ ψ∗(Iχ,f,m)

Et d’aprs le diagramme (∗ ∗ ∗2), on a JY,F,Γ = i∗
σm(Iχ,f,m) = Jχ,f,γ. Donc, d’aprs
le diagramme (∗ ∗ ∗1), il suﬃt de montrer que IY,F = π∗(JY,F,Γ). Par sa dﬁnition,
on vriﬁe facilement que JY,F,Γ = ⟨an; n ∈ N⟩ (d’o le nom d’idal des coeﬃcients
attribu par Roussarie cet idal). Soit M l’idal maximal de R{t, β}. Notons Fn =
j
n
t (F ). On a Fn ∈ π∗(JY,F,Γ) et F − Fn ∈ Mn pour tout n. Donc, par le thorme
d’intersection de Krull ([L]), F ∈ π∗(JY,F,Γ). Comme l’idal prolong π∗(JY,F,Γ) est
stable par la drivation Y, on obtient IY,F ⊂ π∗(JY,F,Γ. Inversement, pour tout
n ∈ N, on a Y nF = n!an + tHn avec Hn ∈ π∗(JY,F,Γ) (par le mme raisonnement
que pour F , en utilisant la srie de F ). Donc, pour tout n, an(= π∗(an)) ∈ IY,F +
Mπ∗(JY,F,Γ). Par consquent

π∗(JY,F,Γ) ⊂ IY,F + Mπ∗(JY,F,Γ)

Et, par le lemme de Nakayama ([L]), on obtient π∗(JY,F,Γ) ⊂ IY,F . □

Orbite principale et la double inclusion.

Si l’orbite γ adhre 0, et s’il existe une notion de germe de la projection intgrale
πχ,U en 0 (qu’on notera πχ), il se pose alors la question de comparer la ﬁbre en 0
Iχ,f et l’idal π∗
χ(Jχ,f,γ ) (dans une extension commune aux anneaux π∗
χ(R{β}) et
B). Intuitivement, il est tout fait lgitime d’esprer tablir la double inclusion

(
 p∏

j=1 xj)
N π∗
χ(Jχ,f,γ) ⊂ Iχ,f ⊂ π∗
χ(Jχ,f,γ)

qui relaxe l’galit du lemme de saturation, et qui s’inspire du Nullstelenzats d’Hilbert
([L]). Dans ce cas, il est ncessaire d’avoir l’galit

Z(Iχ,f ) = π−1
χ (Z(Jχ,f,γ))

(cf. formule (1)). Et pour cela, il suﬃt que γ soit ”principale” dans U

Dﬁnition IB7. Soit γ une orbite de χ dans U . Elle est dite principale dans U
si
 (i) elle adhre 0;

(ii) elle admet une transversale analytique σ0 ⊂ U qui rencontre en au plus un
point chaque orbite de χ dans U ;

(iii) pour toute transversale analytique σ ⊂ σ0, le satur

ϕχ,U (., σ) = π−1
χ,U (πχ,U (σ))

est un voisinage de 0 dans U .

22
 Ainsi, l’orbite principale γ est la seule orbite de χ dans U qui adhre 0. C’est
donc la seule orbite principale de χ dans U . Pour σ ⊂ σ0, notons Uσ = ϕχ,U (., σ),
c’est un voisinage ouvert de 0, qui est une union d’orbites de χ dans U (c’est un
ouvert admissible). L’espace quotient ̃Uσ s’identiﬁe donc un sous-espace de ̃U .
Par consquent, le morphisme πχ,Uσ : Uσ → ̃Uσ est simplement la restriction Uσ
du morphisme πχ,U . Par la dﬁnition de Uσ, et par la condition (ii), l’espace ̃Uσ
s’identiﬁe la transversale analytique σ. Par la condition (iii), le morphisme πχ,Uσ
se prolonge continment Uσ ∪ {0} en posant πχ,Uσ (0) = γ ∩ σ. On peut donc parler
du germe en 0 du morphisme πχ,U comme tant celui du morphisme πχ,Uσ : Uσ → σ
aux points 0 et γ ∩ σ. Ce germe est indpendant de la transversale σ ⊂ σ0; on le
note πχ. L’existence d’une orbite principale γ implique en particulier l’existence de
(p + q − 1) intgrales premires analytiques et indpendantes: si β sont des coordonnes
analytiques sur σ0, et si on pose gj(β) = βj, les germes Gj = π∗
χ(gj) admettent
des reprsentants Fj sur Uσ0, qui sont des intgrales premires de χ, analytiques et
indpendantes.

Autre cas de transfert.

On en a vu beaucoup, et on verra beaucoup. La premire apparition de chaque
nouveau cas sera trate en dtail. Un cas assez gnral, et abondamment employ dans
la suite est le suivant: pour i = 1, 2, soit Bi ⊂ A
pi,qi un anneau de rfrence. Soit
χi ∈ ΞBi une drivation, et Ui un ouvert admissible pour χi. On suppose que chaque
drivation χi admet une orbite principale γi dans Ui. Pour simpliﬁer, supposons que
Ui est le satur d’une transversale analytique σi, comme ci-dessus (quitte rduire
Ui). Soit Wi ⊂ σi une sous-varit analytique contenant le point mi = γi ∩ σi, et
soit Vi = π−1
χ,Ui (Wi), c’est une sous-varit analytique de Ui, qui adhre 0, et qui est
invariante par χi.

Notons Yi = χi|(Vi,0). En utilisant le ﬂot de Yi, on montre facilement que
Yi(Bi|Vi) ⊂ Bi|Vi. Soit Ψ : V2 → V1 un diﬀomorphisme analytique, continue en
0 avec Ψ(0) = 0. On note de la mme faon son germe Ψ : (V2, 0) → (V1, 0). On
suppose que Ψ∗Y2 = Y1, et que Ψ∗(B1|V1) ֒→ B2|V2. Dans ce cas, le diagramme
suivant est commutatif

(∗)
 B1|V1 Ψ∗
−−−−→ B2|V2

Y1

↓ 

↓Y2

B1|V1 Ψ∗
−−−−→ B2|V2

Une orbite principale tant la seule qui adhre 0, et Ψ tant continue en 0, on
a Ψ(γ2) = γ1. Comme Ψ est un diﬀomorphisme qui prserve les orbites, on peut
supposer, pour simpliﬁer que Ψ(W2) = W1 (quitte dplacer les transversales σi).
Notons ψ : W2 → W1 la restriction de Ψ W2. C’est un diﬀomorphisme analytique,
et on note de la mme faon son germe ψ : (W2, m2) → (W1, m1). Soit Vmi un
satur suﬃsament petit, de Wi par le ﬂot de Yi, et soit πYi ,mi le germe en mi de la
projection intgrale. Le diagramme suivant est commutatif
 23

(∗∗)
 (Vm2 , m2) Ψm2−−−−→ (Vm1 , m1)

πCalY 2 ,m2

↓ 

↓πY1,m1

(W2, m2) ψ
−−−−→ (W1, m1)

La varit Wi est analytique en mi. Donc, par un bon choix de coordonnes an-
alytiques locales (βi, β′
i) sur (σi, mi) (dans lesquelles (Wi, mi) est un graphe), on
obtient que l’anneau local R{βi, β′
i}|Wi sur (Wi, mi), est isomorphe l’anneau an-
alytique R{βi}. On obtient alors le diagramme commutatif partir du diagramme
ci-dessus

(∗ ∗ ∗)
 R{β1} ψ∗
−−−−→ R{β2}

π∗
Y1,m1

↓ 

↓π∗
Y2,m2

B1,m1|Vm1
 Ψ∗
m2−−−−→ B2,m2|Vm2

Les varits Vi tant analytiques en mi, les anneaux locaux Bi,mi|Vmi sont aussi iso-
morphes des anneaux analytiques.

Lemme IB6 (lemme de transfert). Soit f1 ∈ B1 et f2 ∈ B2 tel que f2|V2 =
Ψ∗(f1|V1 ). On a les galits suivantes

(a) Jχi,fi,γi|Wi = i∗
Wi,Vi,mi (Iχi,fi,mi|Vi,mi ).

(b) Iχi,fi,mi|Vi,mi = π∗
Yi,mi(Jχi,fi,γi|Wi).

(c) Iχ2,f2|V2 = Ψ∗(Iχ1,f1|V1 ).

(d) Jχ2,f2,γ2|W2 = ψ∗(Jχ1,f1,γ1|W1 ).

Preuve. Enlevons l’indice i pour un moment. Pour l’galit (a), par dﬁnition d’une
restriction, on a Jχ,f,γ|W = i∗
W,σ(Jχ,f,γ). Et par dﬁnition de l’idal transverse, on
a Jχ,f,γ = i∗
σ,Um(Iχ,f,m), o Um est un satur suﬃsament petit, de σ par le ﬂot de
χ. D’un autre ct, on a Iχ,f,m|Vm = i∗
Vm,Um(Iχ,f,m). Et, on vriﬁe facilement que
i∗
W,σ ◦ i∗
σ,Um = i∗
W,Vm ◦ i∗
Vm,Um.

Pour l’galit (b), par le lemme de saturation, on a

Iχ,f,m|Vm = i∗
Vm,Um ◦ π∗
χm (Jχ,f,γ)

D’un autre ct, on a π∗
Ym (Jχ,f,γ|W ) = π∗
Ym ◦ i∗
W,σ(Jχ,f,γ). Et, on vriﬁe facilement
que les morphismes πχm ◦ iVm,Um : Vm → σ et iW,σ ◦ πYm : Vm → σ, coincident.

Notons gi = fi,|Vi. Il est clair que Iχi,fi|Vi = IYi,gi , et ceci est encore vrai germiﬁ
en n’importe quel point de Vi. L’galit (c) est donc une consquence immdiate de la
commutativit du diagramme (∗). Pour l’galit (d), on utilise l’galit (a)

Jχ2,f2,γ2|W2 = i∗
W2,V2,m2 (Iχ2,f2,m2|V2,m2 )

24

puis la relation (c) germiﬁe aux points m1 et m2

(Iχ2,f2,m2|V2,m2 = Ψ∗
m2(Iχ1,f1,m1|V1,m1 )

et enﬁn, l’galit (b) pour obtenir

Jχ2,f2,γ2|W2 = i∗
W2,V2,m2 ◦ Ψ∗
m2 ◦ π∗
Y1,m1 (Jχ1,f1,γ1|W1 )

La composition de morphismes toils passe aux idaux prolongs. On conclut en
utilisant la commutativit du diagramme (∗ ∗ ∗), et la relation πY2,m2 ◦ iW2,V2,m2 =
idW2 . □

II. Action de la drivation χ = x∂/∂x et thorme principal 1

Les anneaux de rfrences dans toute la suite sont les anneaux SBp,|q|(x, α). Leur
topologie de Krull n’est pas spare. Leurs sous-algbres QA
p,|q| ne sont pas χ-ﬁnies:
l’idal diﬀrentiel du germe
 f = ∑

n>0 α
nx
1/n

n’est pas noethrien dans l’anneau SB1,1(x, α): en eﬀet, si tel est le cas, il existe
ℓ ∈ N, et des germes hi ∈ SB1,1 tels que

(0)
 ℓ∑

i=0 hiχif + χℓ+1f = 0

Soit hi = ∑n hn,i(x)α
n la srie de hi. Les coeﬃcients hn,i ∈ SB1,0(x); notons
ai = h0,i(0). Par une identiﬁcation des coeﬃcients des sries en α dans l’galit (0),
on obtient les relations suivantes pour tout n > 0

ℓ∑

i=0 ai( 1
n )
i + ( 1
n )
ℓ+1 = 0

ce qui est impossible (en utilisant un systme de Vandermonde adquat).

Grce la proprit de quasi-rgularit, la topologie de Krull des algbres
QRHp,q est spare et, pour p = 1, ces algbres sont χ-ﬁnies (cf. thorme II1). La
question de leur noethrianit est un problme ouvert.

Plaons nous dans l’anneau de rfrence SB1,|q|(x, α). Soit U ∈ (R+∗ × R|q|, 0) tel
que le sous-ensemble γ = {(x, α) ∈ U ; α = 0} soit connexe. Alors γ est une orbite
principale de χ dans U . Le morphisme int´egral de χ dans U est simplement la
projection canonique π : (x, α) ↦→ α (on notera de la mme faon son germe en 0).
Les id´eaux χ-transverses le long de γ sont donc des id´eaux de l’anneau analytique
R{α}. L’anneau (SB1,|q|(x, α), π) est une extension toile de l’anneau R{α}.
 25

thorme II1 (thorme principal 1). L’algbre QRH1,q est χ-ﬁnie et satisfait la
double inclusion: pour tout f ∈ QRH1,q d’idal χ-transverse Jχ,f,γ, il existe n(f )
tel que pour tout ε > 0

(1) (x
n(f )+ε)π∗(Jχ,f,γ ) ⊂ Iχ,f ⊂ π∗(Jχ,f,γ)

De plus, elle est χ-quivalente la sous-algbre QRH1,q
cvg.

L’argument principal de la preuve de la χ-ﬁnitude est que l’algbre QRH1,q sat-
isfait la double inclusion (1). La deuxime inclusion est une consquence du

Lemme II1 (lemme de division). Soit f ∈ SB1,|q| et Jχ,f,γ son id´eal χ-
transverse. Alors Iχ,f ⊂ π∗(Jχ,f,γ).

Preuve. On utilise le th´eor`eme de division VB1 de l’appendice B. Soit ∆ le com-
plmentaire du diagramme des exposants initiaux de Jχ,f,γ. Eﬀectuons la division
de f (x, .) dans Jχ,f,γ pour tout x ̸= 0. Soit Q ∈ π∗(Jχ,f,γ) telle que

Supp(f (x, .) − Q(x, .)) ⊂ ∆ pour tout x ̸= 0

Or, d’apr`es le lemme de saturation IB5, on a f (x, .) ∈ Jχ,f,γ pour tout x ̸= 0, et
donc f − Q ≡ 0; d’o`u le r´esultat. □

La premire inclusion est base sur la notion de multiplicit et sur la proprit de
quasi-analycit qui se substitue au thorme d’intersection de Krull ([L]) pour le
passage la limite. La mulptiplicit mχ(f ) est le plus petit des entiers n tel que
(x
n+ε)π∗(Jχ,f,γ ) ⊂ Iχ,f pour tout ε > 0. Elle concide avec la multiplicit al-
gbrique maχ(f ) qui se lit sur la srie asymptotique de f ∈ QRH1,q, en faisant agir
la drivation χ d’abord sur les composantes lmentaires de cette srie qui sont des
fewnomials [K2], solutions d’quations diﬀrentielles simples.

1. Operateurs diﬀrentiels d’Euler EF .

Pour tout multi-indice m = (m0, . . . , mq1) ∈ N1+q1 et tout q1-uplet de nombre
caract´eristiques (r1, . . . , rq1 ) avec rj = 1 + µj, on pose

r = (1, r1, . . . , rq1 ) et em(µ) = ⟨m, r⟩

A toute famille ﬁnie de multi-indices F ⊂ N1+q1 , on associe l’op´erateur

(2) EF = ∏

m∈F(χ − em(µ)Id)

et on note PF son polynˆome caract´eristique. On notera aussi

F?n = {m ∈ N1+q1 ; |m|?n}.

o ? est un oprateur binaire de comparaison. Les solutions de l’´equation EF · = 0
sont les combinaisons sur R{α} des mˆonomes x
em pour m ∈ F , et des fonctions

26

´el´ementaires x
em (log x)
p si em est racine multiple de PF . Donc, g´en´eriquement
en µ, les monˆomes x
em(µ) (pour m ∈ F ), forment une base du noyau de l’op´erateur
EF .

Les fonctions ´el´ementaires zj = xLd(x, µj ) satisfont aux ´equations diﬀ´erentielles

χzj = rj zj + x

donc, un monˆome X m = x
m0 zm1
1 · · · zmq1
q1 satisfait `a l’´equation diﬀ´erentielle

(3) χX m = emX m + monˆomes ≻

o`u ≺ est un ordre adquat sur ces monˆomes (associ l’ordre lexicographique sur
N1+q1 ). Par suite, tout monˆome X m est dans le noyau de l’op´erateur EF=|m|.
D’autre part, de la relation x
rj = x + µjzj on dduit que

x
em(µ) = ∑

|m′|=|m| cm′(µ)X m′

donc, pour tout n, la famille des monˆomes X m de longeur n est, g´en´eriquement
en µ, une base du noyau de l’op´erateur EF=n.

2. Le wronskien de l’oprateur EF=n et ses mineurs.

Soit n ∈ N et N (n) = ♯F=n. Notons Mn la matrice N (n) × N (n) dont les
colonnes sont les d´eriv´ees successives par χ des monˆomes X m (|m| = n), et soit

(4) ∆n(x, µ) = det Mn

Ces monmes forment une base du noyau de l’oprateur EF=n. Donc, en d´erivant les
colonnes de Mn, et en utilisant (3), on obtient

Lemme II2. Il existe une fonction algbrique bn(µ), non-identiquement nulle telle
que

(5) ∆n(x, µ) = bn(µ)x
sn(µ) avec sn(µ) = ⟨
∑
|m|=nm, r⟩

Cette fonction algbrique est donne par bn(µ) = ∆n(1, µ). Soit An(x, µ) la matrice
compl´ementaire de la matrice Mn(x, µ)

Lemme II3. Pour tout x0 ̸= 0 et pour tout ε > 0, les ´el´ements de la matrice
Mn(x0, µ)An(x, µ) appartiennent `a l’id´eal principal de SB1,q1 engendr´e par
x
nN (n)−n−εbn.

Preuve. Ces ´el´ements sont de la forme

(6) Bi,l(x, µ) = Li(x0, µ)Cl(x, µ)
 27

oˆu Li(x, µ) est la ligne d’indice i dans la matrice Mn et Cl(x, µ) est la colonne
d’indice l dans la matrice An. Il est clair, d’apr`es la d´eﬁnition de la matrice An que
ces ´el´ements sont divisibles par x
nN (n)−n−ε dans l’anneau SB1,q1 (chaque monme
X m est divisible par x
n−ε/s dans cet anneau, pour tout s > 0). Il suﬃt donc
de montrer que l’id´eal χ-transverse J, de Bi,l le long de γ est inclus dans l’id´eal
principal engendr´e par bn. Le lemme de division II1 permettra de conclure.

Pour cela, montrons par une rcurrence sur k, que pour tout (i, l) ∈ {1, . . . , N (n)}2

et pour tout k

(7) Li(x, µ)χkCl(x, µ) ≡ 0 [(bn)] dans SB1,q1

Pour k = 0, la relation (7) est une cons´equence de l’galit MnAn = ∆nId.

L’id´eal (bn) ´etant stable par χ, une d´erivation de (7) donne

Liχk+1Cl ≡ −(χLi)(χkCl) [(bn)]

or, pour i ̸= N (n) on a χLi = Li+1 d’apr`es la d´eﬁnition de la matrice Mn. Et en
utilisant l’op´erateur EF=n , on obtient

χLN (n) =
 N (n)∑

j=1 cj(µ)Lj

Et ceci prouve la relation (7). Maintenant, d’aprs la dﬁnition IB6 de l’idal χ-
transverse, l’idal J ⊂ R{µ} est engendr par les drives successives

(χkBi,l(x1, µ))k∈N

pour tout x1 > 0. On prend donc x1 = x0 et on utilise (7) pour ﬁnir la preuve du
lemme. □

3. Sur les blocs χ-homognes.

Soit c l’immersion de la partie IA, et soit HHn l’image par c∗ du R{α}-module
R{α}[X]n, engendr´e par les monˆomes X m d’une mˆeme longueur n (c∗(X) =
(x, (zj (x, µj ))j=1,... ,q1 )), rappelons qu’on note de la mme faon ces fonctions X, zj
et les coordonnes correspondantes). D’aprs le paragraphe 1, la restriction de c∗

ce module est un isomorphisme. Les lments du module HHn sont dits blocs
χ-homognes de degr n. Ces modules sont stables par les oprateurs d’Euler dﬁnis
ci-dessus.

Lemme II4. Tout g ∈ HHn satisfait la double inclusion. Plus prcisment, pour
tout ε > 0
 (x
n+ε)π∗(Jχ,g,γ) ⊂ Iχ,g ⊂ π∗(Jχ,g,γ)

Preuve. La deuxime inclusion est donne par le lemme de division II1. Un tel g
s’´ecrit

28

(8) g = ∑

|m|=n am(α)X m

il est donc dans le noyau de l’op´erateur EF=n . Par cons´equent, son id´eal diﬀ´erentiel
est engendr´e par la famille {χjg; j < N (n)}, et donc son id´eal χ-transverse le long
de γ est engendr´e par la famille {χjg(x0, .); j < N (n)} pour tout x0 ̸= 0. Plusieurs
d´erivations de (8) donnent le syst`eme

(9) Mn(am)m = (χjg)j

((am)m et (χjg)j dsignent les vecteurs colonnes associs). En particulier

(10) Mn(x0, .)(am)m = (χjg(x0, .))j

Mutiplions (9) par la matrice Mn(x0, .)An et utilisons (10)

∆n(χjg(x0, .))j = Mn(x0, .)An(χjg)j

Par le lemme II2, on a ∆n = x
sn bn, et par le lemme II3

Mn(x0, .)An ∈ (x
nN (n)−n−εbn)

Or, sn(0) = nN (n). Ce qui ﬁnit la preuve du lemme. □

Remarque II1. Un cas simple, o cette premire inclusion peut eﬀectivement tre
donne par le Nullstellensatz d’Hilbert, est le suivant: prenons q1 = 1 et supposons
J = R{α}. L’immersion c(x, α) = (x, z(x, µ), α) est un diﬀomorphisme sur la varit
image V = c(U ), qui se prolonge en un homomorhisme sur le bord ∂0U = {x = 0}.
La drivation sur V c∗(χ), se prolonge sur un voisinage W de 0, en une drivation
analytique
 X = x ∂
∂x + (rz + x) ∂
∂z

Soit G = (c∗)
−1(g). D’aprs le lemme de transfert IB6 et l’isomorphie de c∗ :
R{α}[x, z]n → HHn, on a Iχ,g = c∗(IX ,G (car R{α}[x, z]n|V ∼= R{α}[x, z]n). Plaons
nous dans le complexiﬁ de W . L’ensemble des zros de l’idal diﬀrentiel IX ,G est un
sous-ensemble analytique invariant par le ﬂot de X . Or, pour α ﬁx gnrique, les
seules feuilles analytiques de X sont {x = 0} et {x + µz = 0}. Par le Nullstellensatz
d’Hilbert, il existe M ∈ N tel que

(x(x + µz))
M ∈ IX ,G

et en appliquant c∗, on obtient x
(1+r)M ∈ Iχ,g. Ceci est encore valable pour g ∈
QRH1,(1,q2)
cvg , par la dﬁnition de cet anneau. On peut gnraliser cette ide plusieurs
fonctions lmentaires (q1 > 1), seulement l’estimation de l’entier M optimal semble
diﬃcile. Par la dmarche adopte dans ce travail, on obtient une estimation prcise et
optimal de cet entier, en se plaant dans des anneaux plus larges.
 29

4. Sur les fewnomials.

Le passage des blocs χ-homognes aux fewnomials est base sur l’inversion des
oprateurs EF

Lemme II5. Soit e(α) un germe analytique en 0 tel que e(0) ̸= n. Soit l’oprateur
E = χ − eId. Alors, pour tout g ∈ HHn, Iχ,Eg = Iχ,g.

Preuve. Il est clair que Iχ,Eg ⊂ Iχ,g. De la relation χg = eg + Eg, on dduit

EF=ng ≡ PF=n (e)g [Iχ,Eg]

Or EF=ng = 0 et le germe e n’est pas valeur propre de cet op´erateur, on obtient
donc g ∈ Iχ,Eg, par consquent Iχ,g ⊂ Iχ,Eg. □

Soit n ∈ N quelconque et soit f = ∑n
p=0 gp, o`u gp est un bloc χ-homog`ene de
degr´e p, f est un fewnomial d’aprs la terminologie de Khovanski [K1]. Appliquons
l’op´erateur EF<n `a f

(10′) EF<nf = EF<ngn

car deux oprateurs χ − eId et χ − e′Id commutent, et pour p < n, le bloc gp est
dans le noyau de l’oprateur EF<n. En appliquant plusieurs fois le lemme II5 gn,
on obtient que Iχ,EF<n = Iχ,gn , et d’aprs (10’), Iχ,gn ⊂ Iχ,f . De mme, Iχ,gn−1 ⊂
Iχ,f −gn ⊂ Iχ,f , ...etc. On obtient donc

Lemme II6. Iχ,f = ∑n
p=0 Iχ,gp .

Ces idaux tant des idaux diﬀrentiels, cette galit est encore vraie germiﬁe en tout
point de γ voisin de 0. Prenons la restriction une transversale γ, cette galit donne

Jχ,f,γ ⊂
 n∑

p=0 Jχ,gp,γ

et l’inclusion Iχ,gp ⊂ Iχ,f donne Jχ,gp,γ ⊂ Jχ,f,γ pour tout p = 0, . . . , n. D’o l’galit

(10”) Jχ,f,γ =
 n∑

p=0 Jχ,gp,γ

Lemme II7. Le germe f satisfait la double inclusion. Plus prcisment, pour tout
ε > 0
 (x
n+ε)π∗(Jχ,f,γ) ⊂ Iχ,f ⊂ π∗(Jχ,f,γ)

Preuve. Par les lemmes II4 et II6, on a

n∑

p=0(x
p+ε)π∗(Jχ,gp,γ) ⊂ Iχ,f ⊂
 n∑

p=0 π∗(Jχ,gp,γ)

30

ou plus simplement

(x
n+ε)
 n∑

p=0 π∗(Jχ,gp,γ) ⊂ Iχ,f ⊂
 n∑

p=0 π∗(Jχ,gp,γ)

L’galit (10”) permet de conclure. □

5. Sur les convergents.

Lemme II8. L’alg`ebre QRH1,q
cvg est χ-ﬁnie et satisfait la double inclusion. De
plus, elle est χ-quivalente la sous-algbre des fewnomials.

Preuve. Cette algbre est clairement stable par χ. Pour la χ-ﬁnitude, on utilise
le lemme d’extension IB2. L’anneau QRH1,q
cvg est la restriction d’un anneau ana-
lytique, c’st donc un anneau noethrien, d’o l’hypothse (ii) du lemme d’extension.
L’hypothse (iii) est claire: prendre ωj = dαj . La preuve de l’hypothse (i) est
une double application de la th´eorie de Khovanski et d’un thorme de [T] (elle est
aussi une consquence d’un travail rcent et gnral de Speissegger [S]). Soit X =
(x, z1, . . . , zq1 ) et z0(x) = x log x. Soit c0 l’immersion c0(X, α) = (X, z0(x), α) et
B1 l’algbre B1 = c∗
0(R{X, z0, α}). Le graphe de la fonction z0 est une solution
s´eparante de l’´equation diﬀ´erentielle

(11) ω0 = xdz0 − (z0 + x)dx = 0

considre sur un ouvert connexe U0, voisinage de 0 dans {x > 0, z0 < 0}. La
1-forme ω0 est coeﬃcients dans l’anneau analytique R{X, z0, α}. L’algbre B1 est
donc topologiquement noethrienne [T]. Soit c1 l’immersion c1(x, α) = (X(x, α), α),
alors QRH1,q
cvg = c∗
1(B1). les graphes des fonctions zj sont des solutions s´eparantes
des ´equations diﬀ´erentielles

(12) ωj = xdzj − ((1 + µj)zj + x)dx − (x log x(µj zj + x) − xzj) dµj
µj = 0

considres sur des ouverts connexes U(?j ), voisinages de 0 dans {x > 0, zj <
0, µj?j0 j = 1, . . . , q1}, o ?j =>, < (si l’un des µj est nul, alors zj = z0). Ces 1-
formes sont `a coeﬃcients dans l’alg`ebre B1. L’algbre QRH1,q
cvg est donc topologique-
ment noethrienne. D’o l’hypothse (i).

Soit f = ∑∞
p=0 gp ∈ QRH1,q
cvg et soit fn = ∑p≤n gp, o gp est un bloc χ-homogne
de degr p. D’aprs le lemme II6, la suite des idaux (Iχ,fn ) est croissante dans
l’anneau noethrien QRH1,q
cvg. Elle est donc stationnaire. Soit I sa limite et soit n0
son indice de stationnarit: c’est le plus petit entier n tel que Iχ,fn = Iχ,fn′ pour
tout n′ ≥ n. Soit MX = ⟨x, z0, z1, . . . , zq1 ⟩ ⊂ QRH1,q
cvg, il est inclus dans l’idal
maximal de QRH1,q
cvg, et il est stable par χ. Pour tout n ∈ N, on a f − fn ∈ Mn
X
d’aprs la srie de f . Donc, pour tout n ≥ n0, on a

Iχ,f ⊂ I + Mn
X et I ⊂ Iχ,f + Mn
X
 31

Par le thorme d’intersection de Krull, on a Iχ,f = I. Or I = Iχ,fn0 , donc en
germiﬁant ces galits le long de γ, et en prenant les restrictions une transversale, on
obtient Jχ,f,γ = Jχ,fn0 ,γ. Par consquent, le lemme II7 appliqu au fewnomial fn0,
montre que f vriﬁe la double inclusion. Soit k l’exposant d’Artin-Ress de l’idal
MX dans l’idal I ([L]): pour tout entier n, on a

Mn+k
X ∩ I = Mk
X ∩ (Mn
X I)

Prenons n > max{n0, k}. On a f − fn ∈ Mn
X et Iχ,f −fn ⊂ I, donc f − fn ∈ MX I.
Or, par le choix de n, I = Iχ,fn , le germe f est donc χ-quivalent au fewnomial fn,
et ceci ﬁnit la preuve du lemme. □

6. Enﬁn, sur l’algbre QRH1,q.

Soit f ∈ QRH1,q et soit ̂f = ∑∞
p=0 gp une s´erie formelle associ´ee `a f . Les
sommes ﬁnies fn = ∑p≤n gp sont des fewnomials. La suite des idaux diﬀrentiels
(Iχ,fn ) est croissante (dans chacun des anneaux QRH1,q
cvg, QRH1,q ou SB1,|q|). Il
en est de mme de la suite des idaux χ-transverses (Jχ,fn,γ) dans l’anneau R{α}.
Soit I la limite ”diﬀrentielle” de la suite (Iχ,fn ) dans l’anneau QRH1,q
cvg, et soit J
la limite ”χ-transverse” de la suite (Jχ,fn,γ) dans l’anneau R{α}. On va montrer
que la limite diﬀrentielle I, prolonge dans l’anneau SB1,|q|, coincide avec l’idal
diﬀrentiel de f dans cet anneau (mais pas forcment dans l’anneau QRH1,q). Par
contre, on montre que la limite χ-transverse J coincide avec l’idal χ-transverse
de f dans l’anneau R{α}; et cela grce deux arguments principaux: la proprit de
quasi-analycit et le thorme de division VB1.

Lemme II9. Pour tout n, on a Jχ,gn,γ ⊂ Jχ,f,γ.

Preuve. Supposons d’abord que f = gn + o(x
n). D’aprs la dﬁnition des sries
asymptotiques de f (cf. Df. IA5), on peut trouver ε > 0 suﬃsament petit, et
h ∈ SB1,|q| tels que

(13) f = gn + x
n+2εh

En germiﬁant l’galit x
n+2εh = f − gn en un point de γ (x > 0), et en prenant
la retriction une transversale des drives successives, on obtient Jχ,h,γ ⊂ Jχ,f,γ +
Jχ,gn,γ. Donc, d’apr`es le lemme de division II1, appliqu h, il existe h1 ∈ π∗(Jχ,f,γ)
et h2 ∈ π∗(Jχ,gn,γ) telles que h = h1 + h2. Maintenant, en consid´erant les id´eaux
diﬀ´erentiels et en utilisant l’galit (13), on obtient

Iχ,gn ⊂ Iχ,f + (x
n+2ε)(Iχ,h1 + Iχ,h2 )

soit
 Iχ,gn ⊂ Iχ,f + (x
n+2ε)(π∗(Jχ,f,γ) + π∗(Jχ,gn,γ))

Le lemme de division II1, appliqu f , donne

Iχ,gn ⊂ π∗(Jχ,f,γ) + (x
n+2ε)π∗(Jχ,gn,γ)

32

et le lemme II4 appliqu gn fournit

Iχ,gn ⊂ π∗(Jχ,f,γ) + (x
ε)Iχ,gn

L’idal Iχ,gn tant noethrien, et l’idal principal (x
ε) tant inclus dans l’idal maximal
de l’anneau SB1,q, le lemme de Nakayama ([L]) donne

Iχ,gn ⊂ π∗(Jχ,f,γ)

En prenant la restriction une transversale γ, on obtient Jχ,gn,γ ⊂ Jχ,f,γ. Main-
tenant, si ̂f = ∑
p≥0 gp, on montre comme ci-dessus que Jχ,g0,γ ⊂ Jχ,f,γ, puis en
supposant que pour tout p < n, on a Jχ,gp,γ ⊂ Jχ,f,γ, on montre comme ci-dessus
que
 Jχ,gn,γ ⊂ Jχ,f −Pp<n gp,γ ⊂ Jχ,f,γ

et ceci ﬁnit la preuve du lemme. □

Ce lemme et la proprit de quasi-analycit impliquent le

Lemme II10. Il existe une application s´erie formelle injective

f ∈ QRH1,q ↦→ ̂f = ∑

p≥0 gp ∈ c∗(R{α}[[X]])

Preuve. Pour prouver l’existence, il suﬃt de montrer que le germe nul admet une
unique srie qui est la srie nulle. En eﬀet, si ̂0 = ∑
p≥0 gp, le lemme II9 dit que
pour tout n, Jχ,gn,γ ⊂ {0}, et le lemme de division II1 dit alors que gn ≡ 0. Pour
prouver l’injection, prenons f ∈ QRH1,q tel que gp(f ) = 0 pour tout p. On a donc
f = o(x
n) pour tout n; comme QRH1,q ⊂ QA
1,|q|, on obtient f ≡ 0. □

Une consquence de cela est que le morphisme c∗ : R{X, α} → QRH1,q
cvg est un
isomorphisme. En eﬀet, si F = ∑
p≥0 Gp ∈ R{X, α} (les Gp tant ses parties
homognes en X de degr p), son image f = c∗(F ) admet comme srie ∑
p≥0 c∗(Gp),
et on a vu que la restriction de c∗ aux modules R{α}[X]p est un isomorphisme sur
les modules HHp.

Le rsultat cl de cette section est le suivant

Lemme II11. J = Jχ,f,γ.

Preuve. D’apr`es le lemme II9 et l’galit (10”), on a

(13′) Jχ,fn,γ ⊂ Jχ,f,γ pour tout n

donc J ⊂ Jχ,f,γ. Pour montrer l’autre inclusion, on utilise le th´eor`eme de division
VB1 (appendice VB), sur les algbres QA
1,|q|[.]. Les fonctions fn sont algbriques
dans les fonctions lmentaires zj; il existe donc Ω ∈ EI tel que f, fn ∈ QA[Ω] pour
tout n. Soit ϕ1, . . . , ϕl une base de J. Pour tout F ∈ QA[Ω], on note
 33

Q(F ) = ∑

i Qi(F )ϕi et R(F ) = F − Q(F )

o les fonctions Qi(F ) et R(F ) sont donnes par le thorme de division VB1. D’aprs la
dﬁnition de l’idal limite transverse J, on a Jχ,fn,γ ⊂ J pour tout n. Donc, d’apr`es
le lemme de division II1, on a R(fn) ≡ 0 pour tout n. Et, par unicit´e de la division
dans le thorme VB1, on a

R(f ) = R(f − fn) pour tout n

Or, f − fn = o(x
n). Le lemme VB1 implique que R(f ) = o(x
n) pour tout n.
Comme R(f ) ∈ QA[Ω], on obtient R(f ) ≡ 0. Ceci prouve que f ∈ π(J), et donc
(par un raisonnement maintenant classique), que Jχ,f,γ ⊂ J. □

Dﬁnition II1. L’indice de stationnarit de la suite d’idaux (Jχ,fn,γ) est dit mul-
tiplicit algbrique de f relativement χ le long de γ. On la note maχ(f ).

7. Preuve du thorme principal II1.

Soit n ≥ maχ(f ) et soit hn = f − fn = o(x
n+2ε) (d’aprs la srie asymptotique de
f ). On a Jχ,hn,γ ⊂ J d’apr`es le lemme II11. Et, par le lemme de division II1, on a

hn ∈ (x
n+2ε)π∗(J)

D’apr`es le lemme II7, on a (x
n+ε)π∗(J) ⊂ Iχ,fn . Donc, hn ∈ (x
ε)Iχ,fn . L’idal
(x
ε) est inclus dans l’idal maximal de SB, et il est satble par χ. Comme fn est
un fewnomial, le lemme de ﬁnitude IB1 et le lemme II8 impliquent que l’algbre
QRH1,q est χ-ﬁnie, et qu’elle est χ-quivalente la sous-algbre des fewnomials.

Ceci implique en particulier que Iχ,f = Iχ,fn pour tout n ≥ maχ(f ). En prenant
n = maχ(f ) et en utilisant la double inclusion du lemme II7, on obtient la double
inclusion pour l’algbre QRH1,q

(x
maχ(f )+ε)π∗(Jχ,f,γ ) ⊂ Iχ,f ⊂ π∗(Jχ,f,γ )

□

Remarque II2. En fait, cette multiplicit algbrique maχ(f ) est le plus petit entier
n tel que Iχ,f ⊃ (x
n+ε)π∗(Jχ,f,γ) pour tout ε > 0 (dans l’anneau SB1,|q|). En eﬀet,
supposons que Iχ,f ⊃ (x
maχ(f )−1+ε)π∗(Jχ,f,γ) pour tout ε > 0. On a

f − fmaχ(f )−1 ∈ (x
maχ(f )−1+2ε)π∗(Jχ,f,γ)

pour ε > 0 suﬃsament petit (par les mmes raisonnements que ci-dessus). Donc

Iχ,f ⊂ Iχ,fmaχ (f )−1 + (x
maχ(f )−1+2ε)π∗(Jχ,f,γ )

et en utilisant l’hypothse ci-dessus

(x
maχ(f )−1+ε)π∗(Jχ,f,γ) ⊂ Iχ,fmaχ (f )−1 + (x
maχ(f )−1+2ε)π∗(Jχ,f,γ)

Par le lemme de Nakayama, on obtient

34
 (x
maχ(f )−1+ε)π∗(Jχ,f,γ) ⊂ Iχ,fmaχ (f )−1

Mais ceci implique (par un raisonnement classique), que Jχ,f,γ ⊂ Jχ,fmaχ (f )−1,γ, ce
qui contredit la dﬁnition de la multiplicit algbrique maχ(f ).

8. Morphismes srie formelle des algbres QRHp,q.

Soit f ∈ QRHp,q(x, α) et soit ̂f i = ∑
n≥0 gi,n une srie formelle de f relativement
la variable xi (cf. Df. IA5). Montrons qu’elle est unique. Notons fi,n = ∑
ℓ≤n gi,n.

Soient hn ∈ SBp,|q|
0 tels que
 f − fi,n = x
n
i hn

Soient Ui,n ∈ ((R+∗)
p × R|q|, 0) une suite dcroissante d’ouverts telle que fi,n et hn
soient ralises sur Ui,n. Soient x
(n) = (x1,n, . . . , xi−1,n, 0, xi+1,n, . . . , xp,n) tel que
xj,n > 0 et (x
(n), 0) appartient l’intrieur de U i,n ∩ {xi = 0} dans Rp+|q|−1. Le
germe de f, fi,n et hn en (x
(n), 0) est un lment d’une algbre QRH1,q′(xi, α
′) (qui
dpend de n par les coordonnes analytiques α
′
j = xj − xj,n pour j ̸= i). Le germe
en (x
(n), 0) de gi,ℓ (pour ℓ ≤ n), est un lment du R{α
′}-module correspondant
HHℓ ⊂ QRH1,q′(xi, α
′). Donc, par le lemme II9, si f ≡ 0 alors fi,n ≡ 0, et ceci
pour tout n. Par consquent la srie ̂f i est identiquement nulle. L’injectivit de ce
morphisme srie formelle est une consquence facile de la proprit de quasi-analycit.

En partant de chaque srie formelle ̂f i, et en utilisant une rcurrence sur p, on
construit une srie formelle unique

̂f ∈ c∗(R{α}[[X]])

au sens suivant: pour tout n
 f − j
n
X ( ̂f ) ∈ Mn
xSBp,|q|
0

o Mx est l’idal de SBp,|q| engendr par les coordonnes x1, . . . , xp. Pour prouver
l’unicit de cette srie, il suﬃt de se placer dans n’importe quel carte projective dans
la coordonne x, par exemple: x1 = y1 et xi = yiy1 pour i ̸= 1. On utilise alors
la mthode de la premire partie de ce paragraphe, aux voisinages de points tels que
y1 = 0, α = 0 et yi,n > 0 pour i ̸= 1. Les formules suivantes (obtenues par un
calcul direct)

zi,j(xi, µj) = zi,j(yi, µj)y1 + (yi + µjzi,j(yi, µj))z1,j(y1, µj)

montrent que les jets dans les fonctions lmentaires X1(y1, µ), sont prservs (les fonc-
tions zi,j(yi, µj) sont analytiques dans les coordonnes yi − yi,n). L’injectivit de ce
morphisme est encore une consquence facile de la proprit de quasi-analycit.

III. Action de la drivation χ = x∂/∂x − ∑ℓ
j=1 sj(α)uj∂/∂uj

Soient α = (µ, ν) des coordonn´ees sur Rq1 × Rq2 et soit u une coordonn´ee sur
Rℓ. Posons α
′ = (α, u) et q = (q1, q2 + ℓ). On veut tudier l’action de la drivation

35

χ sur l’algbre QRH1,q(x, α
′). Les germes sj sont analytiques et on suppose pour
simpliﬁer la prsentation que sj(α) = 1 + µj. Soit U ∈ (R+∗ × R|q|, 0) un ouvert
tel que le sous-ensemble γ = {(x, α
′) ∈ U ; α
′ = 0} soit connexe. C’est une orbite
principale de χ dans U . Soit πχ (le germe de) la projection intgrale de χ dans
U . Quitte rduire U , l’espace πχ(U ) s’identiﬁe `a une transversale analytique `a
γ: W = {x = x0 > 0}. Des coordonn´ees analytiques naturelles sur W sont les
int´egrales premi`eres de χ, c’est dire la coordonne α et les (coordonnes) germes

λj(x, α
′) = x
sj (α)uj ∈ QRH1,q

Les idaux χ-transverses le long de γ sont donc des idaux de l’anneau R{α, λ}, et
on a le morphisme toil π∗
χ : R{α, λ} → SB1,|q|(x, α, u).

La question qui se pose est: l’algbre QRH1,q est-elle χ-ﬁnie? Le problme est
ouvert. Cependant, on montre dans cette section, qu’elle est localement χ-ﬁnie.

A. Etude globale et thorme principal 2.

Le germe en 0 de la projection πχ n’est pas isomorphe celui d’une pro-
jection linaire, d’o des diﬃcults nouvelles dans l’tude de cette action. La premire
diﬃcult apparat dans l’tude de l’action formelle de χ.

1. Action formelle.

Notons r = (1, (1 + µj)) et s = (sj ). Les valeurs propres de l’oprateur χ sont

em,n(α) = ⟨m, r⟩ − ⟨n, s⟩

Les monˆomes X mun satisfont aux ´equations diﬀ´erentielles

χ(X mun) = em,nX mun + monmes ≻

pour un ordre ≺ adquat sur ces monmes (induit par l’ordre sur les monmes X m).
Le degr d’un monme X mun relativement χ est |m| − |n|. Soit c l’immersion

c(x, α, u) = (X(x, µ), α, u)

Dﬁnition IIIA1. On note ̂HHp ⊂ c∗(R{α}[[X, u]]) le R{α}-module des sries de
monmes de degr p ∈ Z. Ses lments sont dits blocs χ-homognes formels de degr
p.

Dans l’action de χ0 = x∂/∂x (cf. section II), on a montr l’existence d’une ap-
plication srie formelle injective. Par une construction explicite, on en dduit
facilement le

Lemme IIIA1. Il existe une application srie doublement formelle et injective

f ∈ QRH1,q → ̂f = ∑

p∈Z gp(f ) ∈ ∑

p∈Z ̂HHp

Preuve. Soit f ∈ QRH1,q(x, α
′). Sous l’action du champ χ0, on lui associe une
unique s´erie formelle

36

(1) ̂f 0 = ∑

M≥0 g0,M (f )

o`u g0,M est un bloc χ0-homog`ene de degr´e M , i.e

g0,M = ∑

|m|=M am(α
′)X m

Or g0,M (f ) ∈ QRH1,q
cvg(x, α
′), on lui associe donc une unique s´erie convergente

(2) g0,M (f ) = ∑

p≤M gp(g0,M (f ))

o`u gp(g0,M (f )) est un bloc χ-homog`ene convergent de dgr p. Les blocs formels
gp(f ) sont donns par
 gp(f ) = ∑

M≥p gp(g0,M (f ))

Cette application est injective comme les applications (1) et (2). □

L’anneau c∗(R[[X, α
′]]) ←֓ c∗(R{α}[[X, u]]) est noethrien. Grce au thorme d’intersection
de Krull et au lemme d’Artin-Ress ([L]), on va montrer que toute srie ̂f est χ-
quivalente une somme ﬁnie de blocs χ-homognes (par des raisonnements abon-
damment employs dans la section II). L apparaissent les premires diﬃcults de cette
action: ces blocs χ-homognes gp(f ) peuvent tre formels, et mme en cas de con-
vergence d’un bloc gp, les valeurs propres correspondantes em,n peuvent avoir des
points d’accumulation dans Z \ {p}.

Lemme IIIA2. Soit e(α) un germe analytique en 0, tel que e(0) ̸= p, et soit
l’oprateur E = χ − eId. Pour tout g ∈ ̂HHp, on a Iχ,Eg = Iχ,g dans l’anneau
c∗(R[[X, α
′]]).

Preuve. Il suﬃt de montrer que Iχ,g ⊂ Iχ,Eg. Soit Gk = j
k
u(g). Comme la
drivation χ est diagonale dans la coordonne u, on a j
k
u(Eg) = EGk. Or le germe
Gk est dans le noyau de l’oprateur

∏

|m|−|n|=p, |n|≤k(χ − em,nId)

comme e(0) ̸= p, on montre par les mmes arguments que dans le lemme II5 que
Iχ,EGk = Iχ,Gk . Soit M l’idal maximal de c∗(R[[X, α
′]]). On a donc pour tout k

Iχ,g ⊂ Iχ,Eg + Mk

on obtient le rsultat par le thorme d’intersection de Krull. □
 37

Lemme IIIA3. Notons fp1,p2 = ∑p1≤p≤p2 gp(f ), alors Iχ,fp1 ,p2 ⊂ Iχ,fp1 ,p2+1.

Preuve. Le germe j
k
u(fp1,p2 ) est dans le noyau de l’oprateur

∏

p1≤|m|−|n|≤p2; |n|≤k(χ − em,nId)

et par le lemme IIIA2, on a
Iχ,gp2 +1 ⊂ Iχ,fp1 ,p2+1 + Mk

on conclut par le thorme d’intersection de Krull. □

Lemme IIIA4. Il existe p1, p2 ∈ Z tels que ̂f ≡ fp1,p2 [c∗(MX,u))Iχ,fp1 ,p2 ].

Preuve. D’aprs le lemme IIIA3, la suite d’idaux (Iχ,f−p,p ) est croissante et par le
thorme d’intersection de Krull, sa limite est l’idal diﬀrentiel de ̂f . Donc pour tout
p ∈ Z, on a Iχ,gp(f ) ⊂ Iχ, bf . Soit k1 et k2 les exposants d’Artin-Ress des idaux Mu
et c∗(MX ) dans l’idal Iχ, bf . Il suﬃt de prendre p1 = −k1 et p2 = k2. □

2. Multiplicit algbrique et la double inclusion.

Soit f ∈ QRH1,q(x, α, u). Dans l’action de χ0 sur QRH1,., la premire inclusion
est tablie grce la structure asymptotique de QRH1,. (bien adapte χ0), et la
notion de multiplicit algbrique: c’est le plus petit entier m tel que pour tout ε >
0, (x
m+ε)π∗
χ0 (Jχ0,f,γ0) ⊂ Iχ0,f dans l’anneau SB1,. correspondant. C’est aussi
l’indice de stationnarit de la suite des idaux χ0-transverses des lments de la srie
de f relativement χ0. D’aprs l’tude de l’action formelle de χ, cette structure
asymptotique n’est plus adapte χ et les les sous-espaces stables ̂HHp sont formels.
Ceci motive la

Dﬁnition IIIA2. Soit ̂f = ∑
p∈Z gp(f ) la srie de f relativement χ. Le germe f
est dit quasi-convergent si gp(f ) ∈ QRH1,q
cvg pour tout p. On note QRH1,q
qcvg le
R{α}-module correspondant.

Soit f ∈ QRH1,q
qcvg. Les sommes ﬁnies correspondantes fp1,p2 sont des lments de
l’anneau restriction analytique QRH1,q
cvg. Les lemmes IIIA2 et IIIA3 s’appliquent
sur cet anneau. Soit If l’idal limite diﬀrentiel de la suite (Iχ,f−p,p )p∈Z, et soit
Jf l’idal limite transverse de la suite (Jχ,f−p,p,γ)p∈Z. On obtient (en utilisant les
lemmes IIIA2 et IIIA3, et les raisonnements de la section II)

If = ∑

p∈Z Iχ,gp(f ) et Jf = ∑

p∈Z Jχ,gp(f ),γ

Il s’agit de comparer les idaux If et Iχ,f dans l’anneau SB1,|q|, et les idaux Jf et
Jχ,f,γ dans l’anneau R{α, λ}. Soit M′ l’id´eal maximal de R{α, λ} et soit K(M′
λ, Jf )
l’exposant d’Artin-Ress de l’id´eal M′
λ = ⟨λ1, . . . , λℓ⟩ ⊂ R{α, λ}, dans l’idal Jf .
Soit p0 le plus petit des entiers p ≥ −K tel que Jχ,gp,γ ̸⊂ M′Jf .

38

Dﬁnition IIIA3. La multiplicit´e alg´ebrique maχ(f ) est l’indice p de station-
narit´e de la suite croissante des id´eaux (Jχ,fp0 ,p,γ)p≥p0 . La multiplicit´e alg´ebrique
positive est ma+
χ (f ) = max{maχ(f ), 0}.

Cette multiplicit algbrique est invariante dans les perturbations de f dans l’idal
π∗
χ(M′Jf ) ∩ QRH1,q
qcvg. Ceci permet d’tendre QRH1,q
qcvg en une classe d’lments poss-
dant la notion de multiplicit algbrique

Dﬁnition IIIA4. Un germe f ∈ QRH1,q est dit presque quasi-convergent s’il
est limite dans la M(α,u)-topologie de SB1,|q|, d’une suite (fn)n de germes quasi-
convergents, dont la suite des idaux limites transverses (Jfn )n est croissante.

Lemme et dﬁnition IIIA5. Tout germe f presque quasi-convergent possde une
multiplicit algbrique maχ(f ) qui est la limite de la suite (maχ(fn))n, et un idal
limite transverse Jf qui est la limite de la suite (Jfn ).

Preuve. Montrons que les suites (maχ(fn)) et (Jfn ) admettent des limites qui ne
dpendent que de f . Soit J l’idal limite de la suite (Jfn ) d’indice de stationnarit
n0 et soit K l’exposant d’Artin-Ress de l’idal M′
(α,λ) dans J. Soit k > K, pour n
assez grand et n′ > n, on a fn′ − fn ∈ Mk
(α,u), et donc gp(fn′ ) − gp(fn) ∈ Mk
(α,u)
pour tout p ∈ Z. Par consquent, si n ≥ n0, on a Jχ,gp(fn′ ),γ ⊂ Jχ,gp(fn),γ + M′J
et Jχ,gp(fn),γ ⊂ Jχ,gp(fn′ ),γ + M′J. En sommant sur p la premire inclusion par
exemple, on obtient

J = ∪p≤maχ(fn′ )Jχ,gp(fn′ ),γ ⊂ ∪p≤maχ(fn′ )Jχ,gp(fn),γ + M′J

le lemme de Nakayama et la dﬁnition de J = Jfn donnent maχ(fn) ≤ maχ(fn′). La
deuxime inclusion donne l’ingalit inverse. La suite (maχ(fn)) est donc stationnaire.
Notons ma sa limite.

Soit (f ′
n) une autre suite de germes quasi-convergents qui tend vers f dans la
M(α,u)-topologie et dont la suite des idaux limites (Jf ′
n ) est croissante. Soit J ′ son
idal limite d’indice de stationnarit n′
0 et soit ma′ la limite de la suite (maχ(f ′
n)).
Montrons que J ′ = J et ma′ = ma. Pour tout k et n ≥ max(n0, n′
0) assez grand, on
a f ′
n − fn ∈ Mk
(α,u) et donc gp(f ′
n) − gp(fn) ∈ Mk
(α,u) pour tout p. Par consquent,
J ′ ⊂ J + (M′)
k et J ⊂ J ′ + (M′)
k pour tout k. Par le thorme d’intersection
de Krull, on obtient J ′ = J. Notons Jf cet idal. En appliquant le raisonnement
ci-dessus f ′
n − fn et Jf , on obtient ma′ = ma. □

Soit W0 ⊂ W un semi-analytique de l’anneau R{α, λ} qui adhre 0. Soit
U0 = π−1
χ (W0). On dﬁnit de la mme faon, une multiplicit algbrique restreinte
maχ(f|U0) en considrant les idaux χ-transverses et leurs idaux limites dans l’anneau
restriction R{α, λ}|W0 . On verra dans la partie B que tout f ∈ QRH1,q admet
une localisation ﬁnie dans laquelle il est ( extension toile prs), presque quasi-
convergent, et donc possde une multiplicit algbrique restreinte.

2.1. Exemples de germes quasi-convergents.

Omettons les exposants 1, q et 1, |q| pour un moment.
 39

(a) La sous-algbre intgrale-linaire Λ∗(QRH1,q(x, α, λ)).

Soit U0 ∈ (R+∗ × R|q|, 0) et soit Λ le diﬀomorphisme sur U dﬁnie par

Λ(x, α, u) = (x, α, λ(x, α, u)) ∈ U0

L’image Λ(U ) tant ouverte, le morphisme Λ∗ : SB1,|q|(x, α, λ) → SB1,|q|(x, α, u)
est injectif, la sous-algbre QRH1,q(x, α, λ) est donc isomorphe la sous-algbre

Λ∗(QRH1,q(x, α, λ) ⊂ QRH1,q(x, α, u)

(l’inclusion s’obtient en remarquant que x
sj = x + µjz(x, µj)). Le champ Λ∗χ coin-
cide avec la restriction Λ(U ) du champ χ0 et le diagramme suivant est commutatif

(∗)
 SB(x, α, λ) Λ
∗
−−−−→ SB(x, α, u)

χ0

↓ 

↓χ

SB(x, α, λ) Λ
∗
−−−−→ SB(x, α, u)

Lemme IIIA6. Λ∗(QRH(x, α, λ)) ⊂ QRHqcvg.

Preuve. Soit F ∈ QRH(x, α, λ) et soit f = Λ∗(F ). Soit ̂f = ∑p∈Z gp(f ) la s´erie

formelle de f relativement `a χ, et soit ̂F = ∑
p≥0 g0,p(F ) la s´erie formelle de F

relativement `a χ0. Prolongeons le morphisme Λ∗ aux sries formelles: Λ∗( ̂F ) =∑p Λ∗(g0,p(F )). D’aprs le diagramme ci-dessus, l’image par Λ∗ d’un sous-espace
stable par χ0, est incluse dans un sous-espace stable par χ: plus prcisment, pour
p ≥ 0, Λ∗(HHp) ⊂ ̂HHp ∩ QRHcvg . Donc, en utilisant les formules (1) et (2) du
lemme IIIA1, qui dﬁnissent la srie de f , on obtient gp(f ) = Λ∗(g0,p(F )) ∈ QRHcvg,
pour p ≥ 0 et gp(f ) = 0 pour p < 0. En eﬀet, crivons

g0,p(F ) = ∑

|n|=p,|m|≥0 bn,m(α)λ
mX n

les sries ∑
|m|≥0 bn,m(α)λ
m tant convergentes sur un voisinage de 0. Soit
∑

M≥0 FM avec FM = ∑

|n|+|m|=M bn,m(α)X nλ
m

la srie de F dans les variables (X, λ). Elle est bien dﬁnie d’aprs la srie ̂F et l’analycit
dans les coordonnes λ. Le germe Λ∗(FM ) est un bloc χ0-homogne de degr M . De
plus, on vriﬁe facilement que pour tout M

Λ∗(F − ∑

M ′≤M FM ′ ) = o(x
M ) dans l’anneau SB

Ceci prouve que Λ∗(FM ) = g0,M (f ). Or, il est facile de voir que gp(g0,M (f )) = 0
si p < 0 ou p > M , et que gp(g0,M (f )) = ∑
|n|=p,|m|=M−p Λ∗(bn,mX nλ
m) pour
0 ≤ p ≤ M . D’aprs la formule (2), on a

40
 gp(f ) = ∑

M≥p gp(g0,M (f )) = ∑

M≥p
( ∑

|n|=p,|m|=M−p Λ∗(bn,mX nλ
m))

donc
 gp(f ) = Λ∗(g0,p(F ))

et ceci ﬁnit la preuve du lemme. □

Soit γ0 = Λ(γ), elle est principale dans U0, et le morphisme Λ est un diﬀomor-
phisme de U sur un voisinage de γ0. En identiﬁant les intgrales premires de χ et
χ0, on obtient le diagramme commutatif

(∗∗)
 U πχ
−−−−→ W

Λ


↓ 

↓id

U0 πχ0−−−−→ W

Les idaux χ-transverse et χ0-transverse coincident (lemme de transfert IB6). Donc
si F ∈ QRH(x, α, λ) et si f = Λ∗(F ), on a Jχ,f,γ = Jχ0,F,γ0 (= JF d’aprs le thorme
principal II1). Or, on a JF = Jf d’aprs la dﬁnition de l’idal limite transverse, et
les sries de f et F . Et donc maχ(f ) = maχ0 (F ) ≥ 0. On a aussi If = Λ∗(IF ) =
Λ∗(Iχ0,F ) = Iχ,f en utilisant le diagramme (*). Par consquent, en appliquant le
morphisme Λ∗ la double inclusion

(x
maχ0 (F )+ε)π∗
χ0 (JF ) ⊂ Iχ0,F ⊂ π∗
χ0 (JF )

et en utilisant le diagramme (**), on obtient la gnralisation facile du thorme prin-
cipal II1

Lemme IIIA7. L’algbre Λ∗(QRH(x, α, λ)) est χ-ﬁnie et satisfait la double in-
clusion. Elle est χ-quivalente la sous-algbre Λ∗(QRHcvg(x, α, λ)).

(b) La sous-algbre algbrique QRH(x, α)[u]. Elle est clairement incluse dans
QRHqcvg (les blocs χ-homognes sont algbriques dans les variales (X, u)). Soit
f ∈ QRH(x, α)[u] de degr N (f ) en u, et soit S(µ) = N (f ) ∑ℓ
j=1 sj. Alors, ̂f =
∑p≥−N (f ) gp(f ), et le germe
 h = x
S(µ)f

s’identiﬁe un lment de l’algbre Λ∗(QRH(x, α)[λ]) (en utilisant les formules x
sj uj =
λj ). De plus, gp(h) = x
S(µ)gp−S(0)(f ) pour tout p ≥ (ℓ − 1)N (f ), et gp(h) = 0 si
p < (ℓ − 1)N (f ). La multiplicit algbrique de h est (par sa dﬁnition), maχ(h) =
maχ(f ) + ℓN (f ). Donc en appliquant les rsultats du (a), on obtient

Lemme IIIA8. L’algbre QRH(x, α)[u] est χ-ﬁnie et satisfait la double inclusion

(x
ma+
χ (f )+ε)π∗
χ(Jf ) ⊂ Iχ,f et (x
ℓN (f )+ε)Iχ,f ⊂ π∗
χ(Jf )

Elle est χ-quivalente la sous-algbre QRHcvg(x, α)[u].
 41

Le facteur x
ℓN (f ) dans la deuxime inclusion, est optimal comme le montre l’exemple
suivant: f = uN x log x (ℓ = 1 et s = 1), l’idal χ-transverse de f est (λ
N ). l’idal
satur π∗
χ(Jχ,f,γ) est l’idal (x
N uN ). Le plus petit entier n tel que x
nf ∈ (x
N uN )
(dans l’anneau SB), est N .

(c) La sous-algbre convergente QRHcvg. Elle est χ-ﬁnie d’aprs le lemme
d’extension IB2 (mme dmarche que dans la section II). Le lemme IIIA4 s’applique
cette algbre noethrienne: If = Iχ,f et Jf = Jχ,f,γ. Soit HHp ⊂ QRHcvg le R{α}-
module des blocs χ-homognes de degr p ∈ Z. Si ℓ > 0, il est de dimension inﬁnie
et la mthode de rduction de la section II est inoprante. Une premire approche la
premire inclusion est

Lemme IIIA9. Soit g ∈ HHp d’idal χ-transverse Jg et soit p+ = max(p, 0). Pour
tout ε > 0 et pour tout N

(x
p
++ε)π∗
χ(Jg) ⊂ Iχ,g + π∗
χ((M′
λ)
N )

Preuve. Par rcurrence sur ℓ. Le cas ℓ = 0 est donn par le lemme II4. Supposons
ℓ > 0. L’idal Iχ,g tant noethrien dans QRHcvg, g satisfait une quation diﬀrentielle
rsolue
 χM0+1g −
 M0∑

i=0 hiχig = 0

Son idal χ-transverse est donc engendr par la restriction de la famille (g, . . . , χM0 g)
toute transversale {x = x0 > 0}. Quitte eﬀectuer une homothtie en x, on peut
supposer que le polydisque de convergence de la srie de g (dans les variables X),
contient la transversale {x = 1}. Et quitte eﬀectuer une ramiﬁcation x
′ = x
sℓ , et
augmenter le nombre des variables µ, on peut supposer que sℓ ≡ 1. Ordonnons g
en puissances croissantes des fonctions lmentaires z: g = ∑|m|≥0 amzm et posons

gM = ∑

|m|≤M amzm

u′ = (u1, . . . , uℓ−1) et λ
′ = (λ1, . . . , λℓ−1)

On vriﬁe facilement (sur les monmes de gM ), que le germe x
M−pgM s’identiﬁe un
lment g′
M de l’algbre (Λ′)
∗(QRH(x, α, λℓ, u′)) avec

Λ′(x, α, u) = (x, α, λℓ, u′) et λℓ = xuℓ

Comme on l’a vu au (a), l’action de χ sur cette algbre est quivalente celle de la
drivation
 χ′ = x ∂
∂x −
 ℓ−1∑

j=1 sjuj ∂
∂uj

sur l’algbre QRH(x, α, λℓ, u′). Soit GM = ((Λ′)
∗)
−1(g′
M ). Il est χ′-homogne de
degr M . Par l’hypothse de rcurrence

42
 (x
M+ε)π∗
χ′ (JGM ) ⊂ Iχ′,GM + π∗
χ′ ((M′
λ′ )
N )

Or l’idal χ′-transverse de GM coincide avec l’idal χ-transverse de gM et le relev de
son idal diﬀrentiel est (x
M−p)Iχ,gM . Donc en relevant cette inclusion, on obtient

(x
p
++ε)π∗
χ(JgM ) ⊂ Iχ,gM + π∗
χ((M′
λ)
N )

Maintenant, si M ≥ M0 et si on se restreint la transversale {x = 1}, on voit
que l’idal χ-transverse de gM contient celui de g. Et si on prend M ≥ N + p+, on
a g − gM ∈ π∗
χ((M′
λ)
N ). D’o le rsultat. □

Lemme IIIA10. Soit f ∈ QRHcvg. Pour tout ε > 0 et pour tout N

(x
ma+
χ (f )+ε)π∗
χ(Jf ) ⊂ If + π∗
χ((M′
λ)
N )

Preuve. Soit p0 comme dans la dﬁnition IIIA3, et soient p1 ≤ p0 et p2 ≥ ma+
χ (f )
tels que If = Iχ,fp1 ,p2 . On a

If =
 p2∑

p=p1 Iχ,gp ⊃
 ma+
χ (f )
∑

p=p1 Iχ,gp et Jf =
 p2∑

p=p1 Jgp =
 ma+
χ (f )
∑

p=p1 Jgp

on obtient le rsultat en appliquant le lemme IIIA9 aux fonctions gp. □

l’anneau SB n’tant pas noethrien, on ne peut passer la limite dans ces inclusions.
Comme dans la section II, on contourne cette diﬃcult grce au thorme de division
VB2 (appendice VB), et grce au lemme de Nakayama. On obtient le trs important
rsultat suivant

Thorme IIIA1 (thorme principal 2). L’algbre QRHcvg satisfait globalement
la double inclusion: pour tout f ∈ QRHcvg de multiplicit algbrique ma+, il existe
un entier n(f ) tel que pour tout ε > 0

(x
ma++ε)π∗
χ(Jf ) ⊂ Iχ,f et (x
n(f ))Iχ,f ⊂ π∗
χ(Jf )

Preuve. La diﬃcult rside dans la transcendance des intgrales premires non triviales
de χ. Grce la convergence des sries d’lments de QRHcvg, on montre d’abord que
l’action de χ sur cette algbre est quivalente celle d’une drivation d’intgrales premires
non triviales algbriques, sur une autre algbre convergente. Le thorme de division
VB2 s’applique cette nouvelle drivation.

Gnralisons le diﬀomorphisme Λ en les diﬀomorphismes Λs suivants: soit s ≥ 0
et Λs : (x, α, u) ∈ U ↦→ (y, α, v) ∈ Us avec

y = x 1
s+1 et vj = x 1
s+1 +µj uj

Le champ (s + 1)(Λs)∗χ coincide avec la restriction Λs(U ) du champ
 43

Ys = y ∂
∂y − s
 ℓ∑

j=1 vj ∂
∂vj

Le morphisme Λ∗
s : SB(y, α, v) → SB(x, α, u) est un isomorphisme sur son image
et le diagramme suivant est commutatif

(∗)
 SB(y, α, v) Λ
∗
s−−−−→ SB(x, α, u)

1
s+1 Ys

↓ 

↓χ

SB(y, α, v) Λ
∗
s−−−−→ SB(x, α, u)

Soit γs = Λs(γ), elle est principale dans Us et le morphisme Λs est un diﬀo-
morphisme de U sur Λs(U ) qui est un voisinage de γs. En identiﬁant les intgrales
premires de χ et Ys, on obtient le diagramme commutatif

(∗∗)
 U πχ
−−−−→ W

Λs

↓ 

↓id

Us πYs−−−−→ W

Les idaux χ-transverses et Ys-transverses coincident.

Si s est un entier≥ 2, un calcul simple sur les monmes montre que l’image
Λ∗
s(SB(y, α, v)) contient les R{α}-modules HHp(x, α, u) pour p ≥ 0. Et il existe
un morphisme linaire: α ↦→ β(α) tel que l’image r´eciproque (Λ∗
s)
−1(HHp(x, α, u))
est incluse dans le R{β}-module HH(s+1)p(y, β, v) des blocs Ys-homog`enes de degr´e
(s+1)p, restreint l’image β(α). En eﬀet, si zj est une fonction lmentaire de l’algbre
QRH(x, α, u) qui satisfait l’quation χ0zj = rjzj+x, la fonction Zj = y−s(Λ∗
s)
−1(zj)
satisfait l’quation Y0Zj = (rj + s(rj − 1))Zj + (s + 1)y. Si m et n sont des multi-
indices tels que |m| − |n| = p ≥ 0

(2′) (Λ∗
s)
−1(X mun) = ym0+s|m|−2|n| ∏ Z mj
j
 ℓ∏

j=1 ynj (1−(s+1)µj )vnj
j

Maintenant, il suﬃt de remarquer que y1−(s+1)µj = y − (s + 1)µjyLd(y, −(s + 1)µj)
et d’utiliser la convergence des sries d’lments de HHp.

Soit f ∈ QRHcvg(x, α, u) et soient p1 et p2 comme dans le lemme IIIA10. Quitte
`a remplacer f par x
−p1 f , on peut supposer que p1 ≥ 0. Soit s un entier≥ 2 et
F = (Λ∗
s)
−1(fp1,p2). C’est un lment de l’algbre QRH(y, β, v)cvg retreinte l’image
β(α). La multiplicit algbrique de F relativement Ys est (s + 1)maχ(f ). Le lemme
IIIA10 s’applique l’action de Ys sur cette algbre: pour tout ε > 0 et pour tout N

(y(s+1)ma++ε)π∗
Ys (JF ) ⊂ IYs,F + π∗
Ys ((M′
λ)
N )

44
 Le thorme de division VB2 s’applique l’action de Ys sur l’anneau SB(y, α, v).
Soit n(F ) l’entier donn par ce thorme, il ne dpend que de JF = Jf et de s. Le
thorme de division VB2 appliqu F fournit la deuxime inclusion

(3) (yn(F ))IYs,F ⊂ π∗
Ys (JF )

Soit (ϕ1, . . . , ϕL) un systme de gnrateurs de JF dans l’anneau R{α, λ} et soit
N > (s + 1)ma+ + n(F ) + 1. Pour tout i = 1, . . . , L l’inclusion ci-dessus montre
qu’il existe hi ∈ SB(y, α, v) tel que

(4) y(s+1)ma++επ∗
Ys (ϕi) − yN hi ∈ IYs,F

Ceci implique que l’idal Ys-transverse de hi est inclus dans JF . Donc par le thorme
de division VB2, les inclusions (4) donnent

(y(s+1)ma++ε)π∗
Ys (JF ) ⊂ IYs,F + (y(s+1)ma++1)π∗
Ys (JF )

et par le lemme de Nakayama, on obtient

(5) (y(s+1)ma++ε)π∗
Ys (JF ) ⊂ IYs,F

On applique alors le morphisme Λ∗
s aux inclusions (3) et (5) et la commutativit du
diagramme (∗) pour obtenir le rsultat. □

Remarque IIIA1. De cette preuve, et du thorme de division VB2, on dduit le
rsultat suivant: si h ∈ QRH1,q
cvg, et si son idal χ-transverse est inclus dans celui de
f , alors
 (x
n(f ))Iχ,h ⊂ π∗
χ(Jχ,f,γ)

Remarque IIIA2. Soit W0 ⊂ W un semi-analytique de l’anneau R{α, λ}, qui
adhre 0. Soit U0 = π−1
χ (W0). Il est clair que le lemme IIIA9 est vrai sur les
restrictions W0 et U0 (la multiplicit algbrique restreinte coincide avec la multiplicit
algbrique d’un bloc gp). Par consquent, le lemme IIIA10 et le thorme principal
IIIA1, sont encore vrais sur les restrictions W0, U0, en utilisant la multiplicit al-
gbrique restreinte maχ(f|U0 ).

2.2. Exemple de germe presque quasi-convergent.

Soit f ∈ QRH1,q(x, α) d’idal χ-transverse Jχ,f,γ. On dit que f (ou Jχ,f,γ)
satisfait l’hypoth`ese (Hλ) s’il existe un entier N (f ) tel que

Jχ,f,γ ⊃ (M′
λ)
N (f )

On note C1
λ la classe des germes qui satisfont l’hypothse (Hλ). Tout f ∈ C1
λ
est presque quasi-convergent: soit fn = j
N (f )+n
u (f ), il est quasi-convergent et par
le lemme IIIA8, Jfn = Jχ,fn,γ. Par l’hypothse (Hλ), on a Jχ,f,γ ⊂ Jfn + M′Jχ,f,γ.
Donc, par le lemme de Nakayama, on a Jχ,f,γ = Jfn . De plus, la suite (fn) converge
vers f dans la M(α,u)-topologie. Par consquent, f possde une multiplicit algbrique
maχ(f ) et Jf = Jχ,f,γ.
 45

Lemme IIIA11. La classe C1
λ est χ-ﬁnie et satisfait la double inclusion

(x
ma+
χ (f )+ε)π∗
χ(Jf ) ⊂ Iχ,f et (x
ℓN (f )+ε)Iχ,f ⊂ π∗
χ(Jf )

De plus, elle est χ-quivalente la sous-classe QRH1,q
cvg ∩ C1
λ.

Preuve. Par l’hypothse (Hλ), x
ℓN (f )+ε(f − f0) ∈ π∗
χ(Jf ). Et par le lemme
IIIA8, (x
ℓN (f )+ε)Iχ,f0 ⊂ π∗
χ(Jf ), d’o la deuxime inclusion pour f . Soit F =

j
ℓN (f )+ma+

X (f − f0), on a f − f0 − F ∈ (x
ma++ε)π∗
χ(Jf ), et l’idal χ-transverse
de F est inclus dans M′Jf . Le germe f0 a la mme multiplicit algbrique que f , et
d’aprs le lemme IIIA8, il est χ-quivalent au germe

h = ∑

−N (f )≤p≤ma+ gp(f0)

De plus on a f0 − h ∈ (x
ma++ε)π∗
χ(Jf ). Maintenant, le germe h + F ∈ QRHcvg
a la mme multiplicit algbrique que f , et il est algbrique dans la variable X, il est
donc χ-quivalent un germe H algbrique dans les variables (X, u) (cf. (c)). D’aprs
le lemme IIIA8, le germe H satisfait la premire inclusion. Comme f − (h + F ) ∈
(x
ma++ε)π∗
χ(Jf ), le germe f satisfait la premire inclusion et il est χ-quivalent
H. □

Ce lemme est encore vrai pour la classe C1
λ,loc des germes f qui satisfont l’hypothse
(Hλ) sur une restriction W0(f ) ⊂ W .

B. Etude localise et thorme principal 3.

Pour ℓ = 0, on a montr dans la section II, que l’algbre QRH1,q est χ0-ﬁnie, et que
tout lment f se divise dans son idal χ-transverse Jχ0,f,γ0, dans l’anneau QA
1,|q|[Ωf ].
La question qui se pose alors est la suivante: f se divise-t-elle dans Jχ0,f,γ0 dans
un sous-anneau de QA
1,|q|, qui possde une structure asymptotique lmentaire?
La rponse est oui modulo une dsingularisation de Jχ0,f,γ0 (voir ci-dessous).

Pour ℓ > 0, on a vu dans la partie A que si le germe f est presque quasi-
convergent, il existe un entier n tel x
nf se divise dans son idal χ-transverse (qu’on
note simplement Jf ), disons dans l’anneau SB (on peut montrer que la division
se fait dans l’anneau QA, mais ceci ne sera pas utilis). Je pense qu’il est possible
de gnraliser le thorme de division VB2 l’action de la drivation χ (ie. avec valeurs
propres sj(µ) transcendantes), en utilisant encore les techniques de la rfrence [B-
M]. Cependant, si le germe f est gnral, sa srie formelle relativement χ (cf. lemme
IIIA1), est doublement formelle. D’o la diﬃcult de pouvoir approcher son idal
χ-transverse Jf , par l’intermdiaire d’idaux χ-transverses de germes simples.

Si cet idal Jf tait principal et monomial, sa reconnaissance dans la srie de
f , serait une simple tude sur les sries Tayloriennes. D’o l’ide du lemme IIIB1 ci-
dessous, bas sur une dsingularisation d’Hironaka. Grce cette dsingularisation,
on montre le thorme principal suivant

46

Thorme IIIB1 (thorme principal 3). L’algbre QRH1,q est localement χ-ﬁnie.

Nanmoins, cette dsingularisation donne un caractre fortement technique la
preuve du thorme. Il est donc trs souhaitable d’avoir un rsultat global (de χ-
ﬁnitude), par les mthodes algbrico-gomtriques des sections II et IIIA.

Lemme IIIB1. Soit J un idal de l’anneau R{α, λ}. Il existe une dsingularisation
d’Hironaka (ψ, N ) telle que dans chaque carte (a, Va), l’idal ψ∗
a(J) est principal et
monomial. Autrement dit, il existe une coordonne v sur Va, et un multi-indice n,
tels que ψ∗
a(J) = (vn).

Preuve. Elle est base sur une rcurrence sur le nombre de gnrateurs (indpendants)
de J. Soit (ϕ1, . . . , ϕL) un systme de gnrateurs de J. Si L = 1, par une dsingu-
larisation d’Hironaka ([Hir1,2]), le gnratuer ϕ1 se relve localement en un germe qui
est quivalent un monme. Si L > 1, on applique une dsingularisation d’Hironaka
au germe
 ϕ1 × · · · × ϕL × (ϕL − ϕL−1)

s’il est non identiquement nul. Localement dans cette dsingularisation, les trois
germes ϕL−1, ϕL et ϕL − ϕL−1 sont quivalents des monmes. Donc, en utilisant
l’ordre lexicographique sur les monmes, on a ou bien (ϕL−1) ⊂ (ϕL), ou bien
(ϕL) ⊂ (ϕL−1) et on applique l’hypothse de rcurrence. □

Preuve du thorme IIIB1. Pour bien illustrer les tapes cruciales de cette preuve,
commenons par le cas ℓ = 0

1. Cas ℓ = 0.

Soit f ∈ QRH1,q(x, α) (q = (q1, q2)), et soit Jf son idal χ-transverse le long de
γ (χ = χ0 et γ = γ0). Montrons que f se divise localement dans Jf dans un
sous-anneau de QA qui admet une structure asymptotique lmentaire. Soit
̂f = ∑
n≥0 gn sa srie asymptotique formelle relativement la drivation χ (section
II). Les fonctions gn sont des blocs χ-homognes de degr n, autrement dit si

Ld(x, µj) = x
µj − 1
µj

zj(x, µ) = xLd(x, µj ), z = (z1, . . . , zq1 ) et X = (x, z), alors

gn = ∑

|m|=n am(α)X m

avec am ∈ R{α}. On a vu dans la section II que si on note fn = ∑
n′≤n gn′, alors
f − fn ∈ (x
n)SB0 pour tout n. Soient Jgn , Jfn et Jf les idaux χ-transverses le
long de γ. Ce sont des idaux de l’anneau R{α}. La suite (Jfn ) est croissante et elle
converge vers Jf grce la proprit de quasi-analycit dans la coordonne x. De plus,
pour tout n, on a f − fn ∈ (x
n)π∗
χ(Jf ) dans l’anneau SB0. Et, Jfn = ∑n′≤n Jgn′ .
Donc, par unicit de la division (voir ci-dessous), il suﬃt de montrer que pour tout
n, le bloc gn se divise localement dans Jf , dans un sous-anneau de QA qui possde
une structure asymptotique lmentaire (ce sous-anneau tant indpendant de n!).
 47

Soit (ψ, N ) une dsingularisation dans laquelle l’idal Jf est principal et monomial
(lemme IIIB1), et soit (a, Va) une carte de coordonne v telle que

ψ∗
a(Jf ) = (ϕ(v)) avec ϕ(v) =
 p∏

j=1 vna,j
j

On peut supposer, sans perte de gnralit, que p = |q|. Les variables analytiques
de grande complexit dans l’algbre QRH1,q(x, µ, ν), sont les variables µ. Par une
suite d’clatements sphriques dans la coordonne v, on suppose que les relevs µj,a des
fonctions µj sont prpares de la faon suivante: pour tout i = 1, . . . , p

(1) µj,a(v) = µj,p+1−i + µ′
j,p+1−i

les fonctions µj,p+1−i tant indpendantes des coordonnes (vi, . . . , vp) et

µ′
j,p+1−i ∈ (v1 × · · · × vi)

En eﬀet, eﬀectuons un premier clatement sphrique dans la coordonne v: v = t1w
o t1 est une coordonne locale sur (R, 0), et w ∈ Sp−1 la sphre de Rp. Soit v1 une
coordonne analytique locale sur (Sp−1, w) ∼= (Rp−1, 0). Le relev du germe µj,a s’crit

ρ1 + t1θ1(t1, v1)

(avec ρ1 ≡ 0!). Supposons que, aprs i clatements sphriques des coordonnes vj

(j = 0, . . . , i − 1, v0 = v), le relev du germe µj,a s’crive

ρi(t1, . . . , ti−1) + t1 × · · · × tiθi(ti, vi)

o ti = (t1, . . . , ti) est une coordonne analytique sur (Ri, 0), et vi est une coordonne
analytique sur (Rp−i, 0). On applique alors la premire tape au germe θi(0, vi) (si
p − i > 1), et on pose ρi+1 = ρi + t1 × · · · × tiθi(ti, 0). On obtient les formules (1)
en posant
 µj,p+1−i = ρi et µ′
j,p+1−i = t1 × · · · × tiθi

Notons toujours (ψ, N ) la compose de ces deux dsingularisations (l’idal (ϕ) est
toujours monomial dans cette dsingularisation). Notons B l’une des algbres SB, QA
ou QRH (sans prciser les exposants). Dans la carte (a, Va), une extension naturelle
de l’anneau B(x, α), approprie f , est l’anneau (B(x, α, v), π), o π est (le germe de)
la projection canonique: (x, α, v) ∈ U × Va ↦→ (x, α) ∈ U (U ∈ (R+∗ × R|q|, 0) est
un ouvert produit). Prcisons un peu, dans ce cas simple, les proprits du transfert
par le morphisme π. Notons toujours χ = x∂/∂x la drivation dﬁnit sur U × Va. Le
morphisme π est une submersion, et on a π∗χ = χ (la coordonne v est une intgrale
premire de χ, et la restriction de π aux ﬁbres {v = const} est un diﬀomorphisme sur
son image U ). L’orbite Γ = {(α, v) = 0} est principale dans U × Va, et π(Γ) = γ.
Notons π0 la restriction de π une transversale {x = x0 > 0}. L’idal χ-transverse
de π∗(f ) = f , est l’idal prolong π∗
0(Jf ) ⊂ R{α, v}, il est engendr par un systme de
gnrateurs de Jf dans R{α}. Le morphisme Ψa : v ∈ Va ↦→ (ψa(v), v) ∈ Wa est une
immersion analytique, qui est un diﬀomorphisme sur son image Wa ⊂ {x = x0}.

48

L’anneau restriction R{α, v}|Wa est donc isomorphe l’anneau R{v}. Par consquent,
on a π∗
0(Jf )|Wa = (ϕ).

De mme, posons Ua = π−1
χ (Wa), le morphisme Φa : (x, v) ∈ (R+∗, 0) × Va ↦→
(x, Ψa(v)) ∈ Ua est une immersion analytique, qui est un diﬀomorphisme sur
son image Ua. Donc, si B est l’une des algbres SB ou QA, l’anneau restriction
B(x, α, v)|Ua est isomorphe l’anneau B(x, v). La drivation χ est prserve par ce
diﬀomorphisme. Soit g un bloc χ-homogne de la srie de f . Notons fa = Φ∗
a(f|Ua)
et ga = Φ∗
a(g|Ua). D’aprs le lemme de transfert IB6, l’idal χ-transverse de fa le
long de l’orbite {v = 0}, est (ϕ). On a g ∈ π∗
χ(Jf ), donc ga ∈ π∗
χ((ϕ)). Il s’agit
de montrer que le quotient de la division de ga par ϕ, est dans un sous-anneau de
QA
1,p(x, v) qui possde une structure asymptotique lmentaire. La complexit de
cette structure ne dpendra que du germe f par l’intermdiaire de son idal χ-

transverse Jf . Pour cela, on va construit une suite de p extensions ̃QRH
1,p

i (x, v) de
l’algbre QRH1,q+(0,p)(x, α, v)|Ua (rappelons que p = |q|). La rcurrence de cette con-
struction est base sur la rcurrence de construction de nouvelles fonctions lmentaires
d’Ecalle-Khovanski z..., y... partir des fonctions lmentaires z de l’algbre QRH1,q,
et des formules (1).

(a) Construction des extensions ̃QRH1,p

i .

Pour j = 1, . . . , q1, posons rj,0(v) = 1 + µj,a(v) et rj,1(v1, . . . , vp−1) = 1 +
µj,1(v1, . . . , vp−1). D’aprs (1), le germe τj,1 = µj,a − µj,1 = µ′
j,1 ∈ rad(ϕ) =
(v1 × · · · × vp). Pour tout m1 ∈ N, dveloppons les (relevs des) fonctions zj l’ordre
m1 dans la variable τj,1 = µj,a − µj,1

(21) Φ∗
a(zj) =
 m1∑

n=0 τ n
j,1zj,n + τ m1+1
j,1 yj,m1

En utilisant l’quation χΦ∗
a(zj) = rj,0Φ∗
a(zj) + x et en identiﬁant les coeﬃcients des
puissances de τj,1, on obtient des quations diﬀrentielles simples pour les fonctions
zj,n et yj,m1
 χzj,0 = rj,1zj,0 + x

(31) χzj,n = rj,1zj,n + zj,n−1

χyj,m1 = rj,0yj,m1 + zj,m1

avec les conditions initiales zj,n|x=1 ≡ 0 et yj,m1|x=1 ≡ 0. Comme pour les
fonctions lmentaires zj, on montre grce l’oprateur intgral de Dulac (cf. appen-
dice VA), que zj,n ∈ QA
1,p−1(x, v1, . . . , vp−1) et yj,m1 ∈ QA
1,p(x, v). Notons
zn = (z1,n, . . . , zq1,n), ym1 = (y1,m1, . . . , yq1,m1) et X1,m1 = (x, z0, . . . , zm1, ym1).
Un germe G1,n ∈ SB1,p(x, v) est un 1-bloc χ-homogne de degr n et de com-
plexit m1, si
 49

G1,n = ∑

|m′|=n am′(v)X m′
1,m1

avec am′ ∈ R{v}. Le germe G1,n est donc un lment de l’algbre QA
1,p(x, v). La

premire extension ̃QRH
1,p

1,m1(x, v) ⊂ QA
1,p(x, v) est l’algbre des germes qui
possdent une srie asymptotique formelle dans les 1-blocs χ-homognes, de

complexit m1: F ∈ QA
1,p est un lment de ̃QRH
1,p

1,m1 s’il existe une suite (G1,n) de
1-blocs χ-homognes de degr n et de complexit m1, telle que pour tout n

F − ∑

n′≤n G1,n′ ∈ (x
n)SB1,p
0

On note ̃QRH1,p

1 la limite inductive de ces algbres, quand m1 dcrit N.

Soit rj,2 = 1 + µj,2. D’aprs les formules (1), le germe τj,2 = µj,1 − µj,2 ∈
(v1 × · · · × vp−1). Soit m2 ∈ N et soit n1 ≤ m1. En utilisant les quations (31), on
vriﬁe facilement que les coeﬃcients zj,n1,n2 et yj,n1,m2 du dveloppement (22) l’ordre
m2 de la fonction zj,n1 dans la variable τj,2, satisfont des quations diﬀrentielles (32)
du mme type que les quations (31), de valeurs propres rj,1 ou rj,2. De plus, ces
coeﬃcients vriﬁent des relations linaires dduites des quations

∂nzj,0
∂τ n
j,1 = n!zj,n

Comme ci-dessus, on montre que zj,n1,n2 ∈ QA
1,p−2(x, v1, . . . , vp−2) et yj,n1,m2 ∈
QA
1,p−1(x, v1, . . . , vp−1). Pour n1 = 0, . . . , m1 et n2 = 0, . . . , m2, notons zn1n2 =
(z1,n1,n2, . . . , zq1,n1,n2), yn1,m2 = (y1,n1,m2, . . . , yq1,n1,m2) et ym1m2 = (yn1,m2).
Soit
 X2,m1,m2 = (x, (zn1n2), ym1 , ym1m2)

Un 2-bloc χ-homogne de degr n et de complexit (m1, m2), est un germe de
la forme
 G2,n = ∑

|m′|=n am′(v)X m′
2,m1,m2

avec am′ ∈ R{v}. La deuxime extension ̃QRH
1,p

2,m1,m2(x, v) ⊂ QA
1,p(x, v) est l’alg-
bre des germes qui possdent un dveloppement asymptotique dans les 2-blocs χ-

homognes de complexit (m1, m2). On note ̃QRH1,p

2 la limite inductive de ces al-
gbres.

En rptant ce procd p fois, on obtient l’extension ̃QRH1,p

p ⊂ QA
1,p(x, v) qui est la

limite inductive d’algbres ̃QRH
1,p

p,m1,... ,mp(x, v) dont les lments ont une structure
asymptotique lmentaire dans les p-blocs χ-homognes dans la variable

Xp,m1,... ,mp = (x, (zn1...np ), ym1, ym1m2 , . . . , ym1...mp )

50

Le uplet (m1, . . . , mp) tant la complexit de ces p-blocs. Les fonctions z... et y...

satisfont des quations diﬀrentielles (3p) du mme type que (31), de valeurs propres
rj,0, rj,1, ... et rj,p ≡ 1. Ainsi construites, les fonctions lmentaires zn1...ni ∈
QA
1,p−i(x, v1, . . . , vp−i)) sont indpendantes des coordonnes vp−i+1, . . . , vp. Un
rsultat qui gnralise le thorme principal II1 est le suivant

Lemme IIIB2. Pour tout i = 1, . . . , p et pour tout choix d’entiers m1, . . . , mi;

l’algbre ̃QRH
1,p

i,m1,... ,mi (x, v) est χ-ﬁnie et satisfait la double inclusion. De plus,
elle admet un morphisme srie formelle f ↦→ ̂f i qui est injectif, et on a les inclusions

Φ∗
a(QRH1,q+(0,p)
|Ua ) ֒→ ̃QRH1,p

1,m1 ֒→ ̃QRH1,p

2,m1,m2 ֒→ . . . ֒→ ̃QRH
1,p

p,m1,... ,mp

Preuve. D’aprs la preuve du thorme principal II1, la χ-ﬁnitude, la double inclusion
et l’existence d’un morphisme srie formelle injectif sont consquences du thorme de

division VB1, de la quasi-analycit: ̃QRH
1,p

i,... ⊂ QA
1,p(x, v), et de l’tude de l’action
de χ sur les i-blocs χ-homognes.

Pour cela, on se place dans la situation gnrale: on suppose que les valeurs pro-
pres rj,0 sont indpendantes et on gnralise les valeurs propres rj,1 en (rj,1,n)n, rj,2
en (rj,2,n1,n2)n1,n2, ...etc. Ainsi le nombre des valeurs propres indpendantes coin-
cide avec le nombre des fonctions lmentaires z... et y... qui satisfont aux quations
diﬀrentielles (3i) et la condition initiale z...
|x=1 = y...
|x=1 ≡ 0. On gnralise aussi
les germes τj,i(v) en des variables indpendantes τ = (τj,i). Notons µ... = r... − 1,
µi = (µ...) et α
i = (µi, τ, v). Soit HHi,n le R{α
i}-module des i-blocs χ-homognes
de degr n (et de complexit (m1, . . . , mi)). Il est stable par χ d’aprs la linarit du
systme (3i). Il s’agit donc de montrer que tout lment de HHi,n satisfait la double
inclusion, et que sa multiplicit algbrique est n. Mettons un ordre sur les monmes de
HHi,n compatible avec la triangularit du systme (3i). Pour tout multi-indice m′ de
longueur n, posons em′ = ∑ m′
...r.... Alors, d’aprs le systme (3i), le R{α
i}-module
HHi,n est inclus dans le noyau de l’oprateur

En = ∏

|m′|=n
(χ − em′ Id)

Pour pouvoir appliquer les mthodes de la section II HHi,n, il suﬃt de montrer
que, gnriquement en µi, ce module coincide avec le noyau de l’oprateur En. Or,
gnriquement en µi, la famille des monmes x
em′ forme une base de ce noyau. Or, par
une rcurrence sur les fonctions z... et y..., et par la rsolution triangulaire du systme
(3i), on montre que ces fonctions sont des combinaisons linaires des fonctions x
r...,
par un systme triangulaire inversible: en eﬀet, si χf = rℓ+1f + g avec f|x=1 ≡ 0,
et si g = ∑ℓ
j=0 aj(τ, r1, . . . , rℓ)x
rj (convention r0 = 1), o les aj sont des polynmes
en τ dont les coeﬃcients sont des fonctions rationnelles non identiquement nulles,
alors
 f =
 ℓ∑

j=0
 aj
rj − rℓ+1 x
rj − (
 ℓ∑

j=0
 aj
rj − rℓ+1 )x
rℓ+1
 51

Ainsi, f = ∑ℓ+1
j=0 bj(τ, r1, . . . , rℓ+1)x
rj et les fonctions bj sont des polynmes en τ ,
dont les coeﬃcients sont rationnelles et non identiquement nulles. Par consquent,
les monmes X m′
i,m1,...,mi forment une base du noyau de l’oprateur En pour des valeur
gnriques de µi.

La double inclusion est donc ralise sur le R{α
i}-module HHi,n, et en prenant
la restriction au graphe v ↦→ α
i(v) = (µi(v), τ (v), v), elle est ralise sur le R{v}-
module des i-blocs χ-homognes de degr n. Ds lors, on applique exactement la

dmarche de la section II l’algbre ̃QRH
1,p

i,m1,... ,mi(x, v). Si on note c l’immersion:
(x, v) ↦→ (Xi,m1,... ,mi(x, v), v), cette algbre est χ-quivalente la sous-algbre

̃QRH
1,p

i,m1,... ,mi,(cvg) = c∗(R{Xi,m1,... ,mi, v}

laquelle s’applique le lemme d’extension IB2. De plus, on obtient (comme dans la
section II) l’existence et l’injectivit du morphisme srie formelle f ↦→ ̂f i.

En substituant les formules (2i) (linaires dans les fonctions lmentaires), dans un
(i−1)-bloc, on obtient un i-bloc de mme degr (en convenant qu’un 0-bloc est un bloc
χ-homogne dans les variables (x, z)) . Par l’existence et l’injectivit des morphismes
sries formelles f ↦→ ̂f i−1 et f ↦→ ̂f i, cette application se prolonge injectivement de
̃QRH1,p

i−1,m1,...,mi−1 vers ̃QRH
1,p

i,m1,...,mi. Ceci donne les inclusions du lemme. Ces
extensions sont donc des extensions toiles, les morphismes associs tant simplement
l’identit. □

(b) Division de ga dans l’idal (ϕ) dans l’extension ̃QRH1,p

p .

Choisissons m1 ≥ max{na,j; j = 1, . . . , p}. Soit G1 l’image de ga dans l’extension
̃QRH1,p

1,m1. Il est de mme degr n que ga, et son idal χ-transverse est inclus dans (ϕ).
D’aprs les galits (1), les germes τj,1(v) appartiennent l’idal (v1×· · ·×vp) = rad((ϕ)).
Donc d’aprs les formules (21) et le choix de m1, on a la division

G1 = H1 + ϕH2

les germes H1 et H2 sont des 1-blocs de degr n, et les monmes de H1 sont ind-
pendants des fonctions lmentaires ym1. D’aprs les galits (1) et les quations (31),
les fonctions lmentaires z. sont indpendantes de la coordonne vp. Comme l’idal χ-
transverse de H1 est inclus dans (ϕ), un dveloppement taylorien de ses coeﬃcients
donne la division
 H1 = vna,p
p F1

le germe F1 tant un 1-bloc de degr n, dont l’idal χ-transverse est inclus dans (ϕ1) =
(vna,1
1 × · · · × vna,p−1
p−1 ). Ainsi, par une rcurrence sur i, et en choisissant m2 = m1,

..., mp = m1, on obtient que l’image Gp de ga dans l’algbre ̃QRH
1,p

p,m1,...,mp s’crit

Gp = ϕHp

le germe Hp tant un p-bloc de degr n.

52

(c) Division de fa dans l’idal (ϕ) dans l’extension ̃QRH
1,p

p .

Soient (gn,a(fa) les 0-blocs de la srie de fa. D’aprs le thorme de division VB1, il
existe un unique Q ∈ QA
1,p(x, v) tel que f = ϕQ. D’autre part, pour tout n ∈ N,
il existe un p-bloc Gp,n tel que gn,a(fa) = ϕGp,n. Soit N ∈ N, en utilisant le lemme
de division II1, appliqu au germe fa − ∑

n≤N gn,a, on obtient

Q − ∑

n≤N Gp,n ∈ (x
N )SB1,p
0

Et ceci prouve que Q ∈ ̃QRH1,p

p,m1,... ,m1.

Il est clair que l’idal χ-transverse de Q n’est pas propre. Soit maa sa multilicit
algbrique (lemme IIIB2). On a Iχ,Q ⊃ (x
maa+ε) pour tout ε > 0. Donc, par la
dﬁnition de la multiplicit algbrique, on a maa ≤ maχ(f ) pour tout a.

Remarque IIIB1. Notons ϕi(v) = ∏i
j=1 vna,j
j . Si h ∈ Φ∗
a(QRH1,q+(0,p)
|Ua ) et si on

note hi son image dans l’extension ̃QRH1,p

i,m1,... ,m1 , l’tude prcdente montre que la
srie formelle de hi est la somme d’une srie formelle ̂hi,1 indpendante des fonctions
lmentaires y..., et d’une srie formelle ̂hi,2 qui se divise par ϕi, dans l’anneau des

sries formelles associ ̃QRH
1,p

i,m1,... ,m1.

Remarque IIIB2. Une consquence facile de cette tude est que tout lment d’une al-

gbre ̃QRH... se divise dans son idal χ-transverse dans une extension ̃̃QRH... obtenue
en prenant aussi les dveloppements (2...) pour les fonctions lmentaires y.... Ces nou-
velles algbres satisfont aussi au lemme IIIB2,...etc.

2. Cas ℓ > 0.

Reprenons la drivation χ = x∂/∂x − ∑ℓ
j=1 sj(µ)uj ∂/∂uj. Soit

f ∈ QRH1,q(x, α, u)

et soit Jf ⊂ R{α, λ} son idal χ-transverse le long de γ = {(α, u)0}. Les coordonnes
λ = (λ1, . . . , λℓ) sont les intgrales premires non triviales de χ : λj = x
sj uj. Il s’agit
d’abord de diviser localement f dans l’idal π∗
χ(Jf ), dans un anneau qui possde une
structure asymptotique lmentaire. L’ide gnrale est la suivante: en gnral, les blocs
formels χ-homognes de la srie de f sont divergents, et leurs idaux χ-transverses
sont dans un anneau formel. Mais, on a vu dans la partie IIIA, que si le germe f
est presque quasi-convergent (bien approch par les germes quasi-convergents dans
la M(α,u)-topologie), alors il possde une multiplicit algbrique et un idal limite
transverse. On applique donc Jf une dsingularisation dans laquelle (ie. localement)
le germe f est presque quasi-convergent, et mieux encore, le quotient de cette
division locale par πchi∗(Jf ), satisfait lhypothse (Hλ) (ou mieux encore, son idal
χ-transverse n’est pas propre!). Ceci ncssite une prparation des intgrales premires
non triviales λj, simlaire celle des intgrales premires µj.

Soit donc (ψ, N ) une dsingularisation d’Hironaka dans laquelle l’idal Jf est prin-
cipal et monomial (lemme IIIB1). Soit (a, Va) une carte de cette dsingularisation

53

de coordonne v. Soit (ϕ) = ψ∗
a(Jf ) avec ϕ = ∏p
j=1 vnj
j et µj,a et soient λj,a les
relevs des coordonnes µj et λj. Notons sj,0 = 1 + µj,a (= rj,0, voir 1). On suppose
(pour simpliﬁer les notations!) que p = |q| et que les germes µj,a et λj,a sont prpars
sphriquement comme dans les formules (1)

(4) µj,a(v) = µj,p+1−i + µ′
j,p+1−i

(4′) λj,a = λj,p+1−i + λ
′
j,p+1−i

les fonctions µj,p+1−i et λj,p+1−i tant indpendantes des coordonnes (vi, . . . , vp) et
les fonctions µ′
j,p+1−i et λ
′
j,p+1−i appartiennent l’idal (v1 × · · · × vi) dans l’anneau
R{v}. Notons toujours (ψ, N ) la compose de ces deux dsingularisations.

Comme dans le paragraphe 1, on commence par relever les germes de f et
χ (qu’on note de la mme faon), dans l’extension naturelle dans les coordonnes
(x, α, v, u): f ∈ QRH1,q+(0,p)(x, α, v, u) et v sont des intgrales premires de χ. On
note aussi de la mme faon l’idal χ-transverse Jf , dans ce relev. Soient les mor-
phismes analytiques

ψa : v ∈ Va ↦→ (αa(v), λa(v)) et Ψa : v ∈ Va ↦→ (ψa(v), v) ∈ Wa = Ψa(Va)

Le morphisme Ψa tant un diﬀomorphisme sur son image, les anneaux R{v} et
R{α, λ, v}|Wa sont isomorphes; donc Ψ∗
a(Jf |Wa ) = (ϕ). Soit Ua = π−1
χ (Wa),
il contient l’orbite principale γa = {(α, v, u) = 0}. Par le diﬀomorphisme Ψa,
identiﬁons les varits analytiques Va et Wa, et les idaux Jf |Wa et (ϕ). Notons
πχ|Ua : (Ua, 0) → (Va, 0) le germe en 0 de la restriction la varit analytique Ua, de
la projection intgrale πχ. Il s’agit de diviser fa = f|Ua dans l’idal π∗
χ|Ua (ϕ). La

dmarche suit et gnralise celle du cas ℓ = 0: on construit p extensions ̃QRHi ⊂ QA,
de l’algbre QRH1,q+(0,p)
|Ua , telles que l’image de fa dans la p-me extension, se divise
par ϕ, dans cette p-me extension. Ces extensions possdent bien sr une structure
asymptotique lmentaire.

(a) Division par l’idal (vnp
p ) dans une extension ̃QRH1.

Reprenons les notations du 1 relatives aux formules (4) (qui remplacent les for-
mules (1)). Soient u(1) = (u1,1, . . . , uℓ,1) des coordonnes analytiques locales sur
(Rℓ, 0). La drivation
 X1 = χ −
 ℓ∑

j=1 rj,1(v)uj,1 ∂
∂uj,1

agit sur l’algbre QRH1,q+(0,p+ℓ)(x, α, v, u, u(1)). Il admet γ1 = {(α, v, u, u(1)) =
0} comme orbite principale. Notons λ
(1) = (λ1,1, . . . , λℓ,1) des coordonnes sur
(Rℓ, 0). Des coordonnes analytiques transverses γ1 sont (α, λ, v, λ
(1)). Soit W1 =
{(Ψa(v), λ
(1)(v)); v ∈ Va} et U1 = π−1
X1 (W1). Les germes λj,1(v) sont donns par

54

les formules (4’). Sur la varit analytique U1 (de dimension p + 1), on a donc les
relations supplmentaires x
rj,1(v)uj,1 = λj,1(v). Comme prcdement, on identiﬁe les
varits analytiques W1 et Va (de dimension p), et on note πX1|U1 : U1 → Va la
restriction associe. On a l’injection canonique

QRH(x, α, v, u) ֒→ QRH(x, α, v, u, u(1))

par la projection canonique π′ : (x, α, v, u, u(1)) ↦→ (x, α, v, u). Notons toujours f
son image dans cette extension. Par la dﬁnition de U1, la restriction π′
|U1 : U1 → Ua
est un diﬀomorphisme sur son image Ua. On a donc aussi l’injection canonique

QRH(x, α, v, u)|Ua ֒→ QRH(x, α, v, u, u(1))|U1

L’image de la drivation restreinte X1|U1 est la drivation χ, et les idaux transverses
(le long de γa et γ1, dans la varit Va), sont prservs (lemme de transfert IB6). Notons
toujours fa la restriction de f U1.

Soient w(1) = (w1,1, . . . , wℓ,1) des coordonnes sur (Rℓ, 0). Soit le diﬀomorphisme
sur (R+∗ × R2(p+ℓ), 0)

Φ1(x, α, v, u, u(1)) = (x, α, v, u(1), w(1)) = (x, α, v, u(1), u − u(1))

et soient X ′
1 = (Φ1)∗X1, U ′
1 = Φ1(U1) et γ′
1 = Φ1(γ1). On a trivialement

Φ∗
1(QRH(x, α, v, u(1), w(1))) = QRH(x, α, v, u, u(1))

et
 Φ1 ∗ (QRH(x, α, v, u(1), w(1))|U ′
1) = QRH(x, α, v, u, u(1))|U1

Soit f ′ = (Φ−1
1 )
∗(f ) et f ′
a sa restriction U ′
1. Pour poursuivre, on a besoin de la
dﬁnition suivante

Dﬁnition IIIB1. Soit t une coordonne locale sur (Rk, 0) et soit χ0 = x∂/∂x.
L’extension
 ̃QRH
1,(p,k)

1,m1 (x, v, t) ⊂ QA
1,p+k(x, v, t)

est l’algbre des germes qui possdent une srie asymptotique formelle dans les 1-blocs
χ0-homognes de complexit m1, construits (comme au 1) grce aux formules (4), et
dont les coeﬃcients appartiennent l’anneau R{v, t}.

Remarque IIIB3. Pour toute partition t = (t′, t”) ∈ Rk1 × Rk2

̃QRH1,(p,k)

1,m1 (x, v, t) ⊂ ̃QRH
1,(p,k1)

1,m1 (x, v, t′){t”}

les sries tant convergentes sur un produit, au sens suivant

̃QRH1,(p,k1)

1,m1 (x, v, t′){t”} ⊂ SB1,p+k(x, v, t)

et pour tout h ∈ ̃QRH
1,(p,k1)

1,m1 (x, v, t′){t”}, de srie
 55

h = ∑

|m|≥0 hm(t”)
m

il existe un domaine standard Ω tel que hm ∈ QA
1,p+k1[Ω] pour tout m.

Soient U1,a et U2,a les varits analytiques, images de U ′
1 par les projections canon-
iques

(x, α, v, u(1), w(1)) ↦→ (x, v, u(1)) et (x, α, v, u(1), w(1)) ↦→ (x, v, u(1), w(1))

et soient γ1,a, γ2,a les images de γ′
1. Les restrictions de ces projections ces varits sont
des diﬀomorphismes. Par une gnralisation facile des rsultats du 1, on a l’injection
suivante pour tout m1

(5) QRH1,q+(0,p+ℓ)(x, α, v, u(1), w(1))|U ′
1 ֒→ ̃QRH
1,(p,2ℓ)

1,m1 (x, v, u(1), w(1))|U2,a

La drivation X ′
1 (restreinte U ′
1) est prserve (par restriction U2,a). Choisissons

m1 > max{nj; j = 1, . . . , p}. Soit h ∈ ̃QRH
1,(p,2ℓ)

1,m1 tel que l’image de f ′
a dans cette
extension soit gale ha = h|U2,a . La motivation de ces extensions est la suivante:
par la dﬁnition de U1, on a

x
sj,0 uj|U1 = λj,a(v) et x
rj,1uj,1|U1 = λj,1(v)

pour tout j = 1, . . . , ℓ. Par consquent, par le diﬀomorphisme Φ1, un calcul direct
donne

(6) x
sj,0+rj,1wj,1|U ′
1 = λ
′
j,1x
rj,1 + λj,1(x
rj,1 − x
sj,0 )

(voir formules (4’)). Notons δj(x, v) = x
sj,0 − x
rj,1 . En utilisant les dveloppements
(21), on voit que l’image de δj dans l’extension (5), est un lment de l’idal (τj,1(v)) ⊂

rad((ϕ)) (plus prcisment, dans l’anneau ̃QRH
1,p

1,m1 (x, v)). D’aprs les formules (4’),
on a λ
′
j,1 ∈ rad((ϕ)), donc l’image du germe (6) dans l’extension (5), est un lment

de l’idal rad((ϕ)) dans l’anneau ̃QRH
1,p

1,m1(x, v)).

Posons donc S1 = m1 ∑ℓ
j=1(sj,0 + rJ,1) et notons

(7) h1 = j
m1
w(1) (x
S1 h) et h2 = x
S1 h − h1

(en prenant bien sr l’image du monme x
S1 dans l’extension (5)). Notons aussi
h1,a et h2,a leurs restrictions U2,a, par la remarque IIIB3, ce sont des lments de
l’extension (5). Et, par la remarque faite sur le germe (6), et par le choix de m1, le
germe h2,a se divise dans l’idal (ϕ)M′ dans l’extension (5) (M′ tant l’idal maximal
de R{v}). Comme l’idal X ′
1-transverse de ha est (ϕ), il en est de mme de celui de
h1,a.

56
 Le germe h1 est polynomial dans la coordonne w(1). L’galit (6) montre que sa re-

striction h1,a s’identiﬁe la restriction U1,a d’un lment F1 de l’algbre ̃QRH
1,(p,ℓ)

1,m1 (x, v, u(1)).
L’image dans cette extension, de la drivation X ′
1 (restreinte U2,a), est la drivation

χ1 = χ0 −
 ℓ∑

j=1 rj,1uj,1 ∂
∂uj,1

(restreinte U1,a). Les idaux transverses sont prservs dans cette extension. Notons
F1,a la restriction de F1 U1,a. L’idal χ1-transverse de F1,a, le long de γ1,a, est (ϕ).

Il s’agit maintenant de montrer que F1,a appartient l’idal (vnp
p ) dans l’anneau

̃QRH1,(p,ℓ)

1,m1|U1,a(x, v, u(1)). Pour cela, on commence par eﬀectuer une division de

F1 par vnp
p dans l’anneau ̃QRH
1,(p,ℓ)

1,m1 (x, v, u(1)). En eﬀet, d’aprs le thorme de di-
vision VB1 dans l’anneau QA
1,p+ℓ(x, v, u(1)), il existe f1 ∈ QA
1,p+ℓ(x, v, u(1)) et
R1, . . . , Rnp ∈ QA
1,p+ℓ−1(x, v1, . . . , vp−1, u(1)) tels que

F1 = vnp
p f1 +
 np−1∑

j=0 vj
pRj = vnp
p f1 + R

Par la remarque IIIB3, les oprations de prise de jet ﬁni en w(1), et d’extension
(5) commutent. Donc, d’aprs la remarque IIIB1, la srie formelle ̂F1 relativement
la drivation χ0, est la somme d’une srie formelle ̂F1,1 indpendante des fonctions
lmentaires ym1, et d’une srie formelle ̂F1,2 qui se divise dans l’idal (ϕ) dans l’anneau

formel associ ̃QRH
1,(p,ℓ)

1,m1 (x, v, u(1)). En divisant dans l’idal (vnp
p ), les 1-blocs χ0-
homognes et les restes de la srie ̂F1, et en utilisant l’unicit de la division de F1,

on voit que f1 ∈ ̃QRH
1,(p,ℓ)

1,m1 (x, v, u(1)) et que pour tout j = 0, . . . , np − 1, Rj ∈

̃QRH1,(p−1,ℓ)

1,m1 (x, v1, . . . , vp−1, u(1)).

Maintenant, pour montrer que R|U1,a ≡ 0, on utilise le lemme de saturation IB5.
Soit x0 > 0 suﬃsament petit, et soit m0 = (x0, 0) ∈ γ1,a. Redressons le champ
χ1|U1,a dans un voisinage de m0 inclus dans U1,a

x = x0 exp(t), uj,1 = λj,1(v)
x0 exp(−rj,1(v)t)

D’aprs le lemme de saturation IB5, le germe de F1,a en m0, appartient au satur
de l’idal (ϕ). Donc, dans les coordonnes locales (t, v) sur (Rp+1, 0), ce germe est
divisible par vnp
p . Par consquent, le germe de R|U1,a en m0, est divisible par vnp
p .
Or, les germes rj,1(v) et λj,1(v) sont indpendants de la coordonne vp (formules (4)
et (4’)). Comme R est polynomial dans la coordonne vp, de degr≤ np − 1, il s’ensuit
que R|U1,a ≡ 0.

On a donc construit f1 ∈ ̃QRH
1,(p,ℓ)

1,m1 (x, v, u(1)) tel que

F1,a = vnp
p f1,a
 57

(o f1,a est la restriction de f1 U1,a). L’idal χ1-transverse de f1,a est donc gal l’idal
(ϕ1) = (vn1
1 × · · · × vnp−1
p−1 ) et, toujours par la remarque IIIB1, la srie formelle de f1
relativement χ0, est la somme d’une srie formelle ̂f1,1 indpendante des fonctions
lmentaires ym1, et d’une srie formelle ̂f1,2 divisible par l’idal (ϕ1), dans l’anneau

formel associ ̃QRH
1,(p,ℓ)

1,m1 (x, v, u(1)).

En rsum, notons U1,a l’image de U1 par la projection canonique

(x, α, v, u, u(1)) ↦→ (x, v, u, u(1))

et Φ1,0 la restriction de Φ1 {α = 0}. Soit H ∈ ̃QRH
1,(p,2ℓ)

1,m1 (x, v, u(1), w(1))
tel que h2,a = ϕHa (Ha tant sa restriction U2,a). Notons H1 = Φ∗
1,0(H) et
H1,a sa restriction U1,a. L’image de la varit U1,a par la projection canonique
(x, v, u, u(1)) ↦→ (x, v, u(1)) est la varit U1,a, et par une identiﬁcation triviale,
Φ∗
1,0(f1) = f1. Donc, en composant toutes ces extensions, on obtient une extension

(̃QRH1,(p,2ℓ)

1,m1 (x, v, u, u(1))|U1,a , π1) ←֓ QRH1,q+(0,p)(x, α, v, u)|Ua

telle que
 π∗
1(x
S1 fa) = vnp
p f1,a + ϕH1,a

avec f1 ∈ ̃QRH
1,(p,ℓ)

1,m1 (x, v, u(1)), dont la srie formelle relativement χ0 est la somme
des deux sries formelles ̂f1,1 et ̂f1,2, et telle que l’idal χ1-transverse de f1,a est (ϕ1).
L’image dans cette extension, de la drivation χ (restreinte Ua), est la drivation X1
(restreinte U1,a).

(b) Division dans l’idal (ϕ) dans une extension ̃QRHp.

Dﬁnition IIIB2. Soient m1, . . . , mi ∈ N (i ≤ p), et soit t une coordonne locale
sur (Rk, 0). L’extension

̃QRH
1,(p,k)

i,m1,... ,mi(x, v, t) ⊂ QA
1,p+k(x, v, t)

est l’algbre des germes qui possdent une srie asymptotique formelle dans les i-blocs
χ0-homognes de complexit (m1, . . . , mi), construits grce aux formules (4), et dont
les coeﬃcients appartiennent l’anneau R{v, t}.

La remarque IIIB3 s’appliquent ces algbres.

Choisissons m2 = · · · = mp = m1. On rpte le procd du 2a, p − 1 fois, appliqu au
germe f1. On construit une suite de germes fi, Hi (avec f0 = f et H0 = 0), et une
suite d’extensions

(̃QRH1,(p,(i+2)ℓ)

i+1,m1,...,mi+1(x, v, u, u(1), . . . , u(i+1))|Ui+1,a, πi,i+1)

←֓ ̃QRH
1,(p,(i+1)ℓ)

i,m1,... ,mi (x, v, u, u(1), . . . , u(i))|Ui,a

58

telles que
 π∗
i,i+1(x
Si+1 fi,a) = ϕ
ϕi+1 fi+1,a + ϕHi+1,a

avec Si = mi ∑ℓ
j=1(rj,i−1 + rj,i) pour i = 1, . . . , p. Le germe

Hi ∈ ̃QRH
1,(p,(i+1)ℓ)

i,m1,... ,mi (x, v, u, u(1), . . . , u(i))

et le germe fi ∈ ̃QRH
1,(p,ℓ)

i,m1,... ,mi (x, v, u(i)) (en posant u(0) = u). les germes Hi,a et
fi,a dnotent leurs restrictions Ui,a. La srie formelle de fi relativement χ0, est la
somme d’une srie formelle ̂fi,1 indpendante des fonctions lmentaires ym1, ym1m2 , . . . , ym1···mi;

et d’une srie formelle ̂fi,2 divisible par ϕi dans l’anneau formel associ ̃QRH
1,(p,ℓ)

i,m1,... ,mi(x, v, u(i)).
La varit analytique Ui,a, de dimension p + 1, est donne par les conditions

Ui,a = {(x, v, u, . . . , u(i)) ∈ Ui ∈ (R+∗ × Rp+(i+1)ℓ, 0);

x
rj,k(v)uj,k = λj,k(v), j = 1, . . . , ℓ; k = 0, . . . , i}

L’image de la drivation

Xi = χ − ∑

j=1,... ,ℓ, k=1,... ,i rj,kuj,k ∂
∂uj,k

(restreinte Ui,a), est la drivation Xi+1 (restreinte Ui+1,a).

Posons Sa = S1 + · · · + Sp. On a donc construit une extension

(̃QRH
1,(p,(p+1)ℓ)

p,m1,...,mp (x, v, u, u(1), . . . , u(p))|Up,a, πp) ←֓ QRH1,q+(0,p)(x, α, v, u)|Ua

telle que
 π∗
p(x
Sa fa) = ϕQa

avec Q ∈ (̃QRH1,(p,(p+1)ℓ)

p,m1,...,mp (x, v, u, u(1), . . . , u(p)) (Qa tant sa retsriction Up,a).
L’idal Xp-transverse de Qa le long de γp = {(v, u, u(p)) = 0}, n’est pas propre. Le
germe Qa est donc presque quasi-convergent, car il satisfait l’hypothse (Hλ)
(cf. partie IIIA 2.2). Pour ﬁnir la preuve du thorme principal IIIB1, il suﬃt de
montrer que le germe Qa est Xp-ﬁni.

Plus gnralement, indiquons brivement comment on adapte les principaux rsul-
tats de la partie A, l’action de la drivation Xp (qu’on notera X pour simpliﬁer),

sur l’algbre tendue ̃QRH1,(p,(p+1)ℓ)

p,m1,...,mp (x, v, u, u(1), . . . , u(p)) (qu’on notera simplement

̃QRH1,(p,ℓ′)

p,m (x, v, u′)). Soit

Xp,m(x, v) = (x, z...(x, v), y...(x, v))
 59

les fonctions lmentaires de cette algbre (cf. 1 pour les notations z..., y...). Les
p-blocs formels X -homognes de degr k ∈ Z (et de complexit m), sont les sries
formelles de la forme
 Gk = ∑

|n|−|n′|=k an,n′(v)X n
p,m(u′)
n
′

avec an,n′ ∈ R{v}. On dﬁnit alors, de la mme faon que dans la partie A, les germes
quasi-convergents, la multiplicit algbrique relativement X , et les germes presque
quasi-convergents. Soit cp,m l’immesion

cp,m(x, v) = (Xp,m(x, v), v, u′)

et soit la sous-algbre convergente ̃QRH
1,(p,ℓ′

p,m,(cvg) = c∗(R{Xp,m, v, u′} (ici, Xp,m
dsignent des variables). Si on gnralise les valeurs propres rj,i (comme dans le
lemme IIIB2), on voit que cette algbre convergente est simplement la restriction
d’une algbre convergente QRH1,q′(x, α
′, u′)cvg au graphe du germe analytique

v ↦→ µ′(v) = (rj,i(v) − 1)j=1,... ,q1; i=0,... ,p

(Ceci n’est pas le cas pour l’algbre ̃QRH
1,(p,ℓ′)

p,m (x, v, u′): un lment de cette algbre
n’est pas forcment une restriction d’un lment d’une algbre QRH). Donc, par une
vriﬁcation aise des formules (2’) (partie A), appliques aux fonctions lmentaires z...,
y..., et utilisant uniquement les quations diﬀrentielles (3p) (partie A), et par le
lemme IIIB1, on obtient

Lemme IIIB3. L’algbre ̃QRH1,(p,ℓ′)

p,m,(cvg) est X -ﬁnie, et elle satisfait globalement la
double inclusion.

On dﬁnit de la mme faon que dans la partie A, la classe ̃C1
λ des germes qui
satisfont l’hypothse (Hλ). Donc, en utilisant le lemme IIIB1, qui remplace le
thorme principal II1, et le lemme IIIB3, qui remplace le thorme principal IIIA1, on
obtient

Lemme IIIB4. La classe ̃C1
λ est X -ﬁnie, et satisfait la double inclusion.

Ce lemme est encore vrai sur la restriction Up,a ⊂ Up, ce qui ﬁnit la preuve du
thorme. □

Cette preuve suggre la dﬁnition suivante de la multiplicit algbrique relativement
χ, pour tout f ∈ QRH1,q: soit D le diviseur exeptionnel de la dsingularisation
(ψ, N ), alors on pose
 maχ(f ) = inf
(ψ,N ) sup
a∈D(maX (Qa) − Sa(0))

et ce nombre est ﬁni, car D est compact, et la multiplicit algbrique des germes
d’idal transverse non propre (et mme des germes presque quasi-convergents), est
semi-continue suprieurement, comme fonction des variables v (ceci est tudi en dtail
dans l’article [M’]).

60
 IV. Dmonstration du thorme 0.

A. Dsingularisation de la drivation d’Hilbert.

Soit Ξ[QRHp,q] le QRHp,q-module de germes en 0 de champs de vecteurs `a
composantes dans QRHp,q et qui laissent invariant l’alg`ebre QRHp,q. Ce module
contient le sous-module engendr´e par les d´erivations ´el´ementaires xj∂/∂xj pour
j = 1, . . . , p. On s’intresse plus particuli`erement `a une sous-classe de Ξ[QRHp,q] qui
apparait dans le probl`eme d’Hilbert hyperbolique, et qui a la propri´et´e d’tre stable
dans une certaine d´esingularisation. Cette dsingularisation est inspire de la gomtrie
du polycycle dploy. On note cette classe ΞH[QRHp,q] et elle est d´eﬁnie de la faon
suivante: soit k ≤ p; posons rj = 1 + µj pour j = 1, . . . , k − 1, x = (x1, · · · , xk)
et x
′ = (xk+1, · · · , xp). Les ´el´ements de ΞHk[QRHp,q] sont les germes en 0, de
champs de vecteurs χ qui satisfont aux conditions suivantes

(a) si k = 1, ΞH1[QRHp,q] = {x1∂/∂x1, · · · , xp∂/∂xp}.

(b) Si k > 1, on a χx1 = ∏k
j=1 xj et χ admet comme int´egrales premi`eres
les fonctions coordonn´ees α
′ = (x
′, α) et (k − 1) germes gj(xj , xj+1, α
′) =
dj (xj, α
′) − xj+1 avec

dj = x
rj
j (1 + Dj) et Dj = O(xj ) ∈ QRHp−k+1,q(xj, x
′, α)

L’entier k − 1 est appel dimension de non trivialit de χ, et les germes gj sont
dits sesintgrales premires non triviales. On pose

ΞH[QRHp,q] = ∪
p
k=1ΞHk[QRHp,q]

1. Rduction de certains lments de Ξ[QRHp,q] des lments de
ΞH[QRHp,q].

Soit χ ∈ Ξ[QRHp,q] tel que χx1 = ∏k
j=1 xj et qui admet comme int´egrales
premi`eres la coordonn´ee α
′ et (k − 1) germes gj(xj , xj+1, α
′) = aj(α
′)dj (xj, α
′) −
fj+1(xj+1, α
′) tels que dj a la mme structure que dans le cas (b) ci-dessus et fj =
bj(α
′)xj (1 + O(xj)) ∈ QRHp−k,q+(0,1)(α
′, xj). Les fonctions aj et bj appartiennent
l’algbre ∈ QRHp−k,q avec aj(0) > 0 et bj(0) > 0. Par le thorme d’inversion VB4
(appendice VB), il existe un diﬀ´eomorphisme

H(x, α
′) = (h1(x1, α
′), . . . , hk(xk, α
′), α
′)

o`u les germes hj ont la mˆeme structure que les germes fj et tel que le champ H∗χ
soit quivalent `a un ´el´ement de ΞHk[QRHp,q].

2. Dsingularisation d’lments de ΞH.

Soit 1 < k ≤ p et χ ∈ ΞHk[QRHp,q] repr´esent´e sur U ∈ ((R+∗)
p × R|q|, 0) qu’on
choisit de la forme U = U1 × U2 de coordonn´ees (x, α
′).

2.1. Premier clatement de χ.
 61

Posons rk = 1 et pour i ≤ j, ri,j = ri × · · · × rj. Soit χpr ∈ ΞHk le champ
dont (k − 1) int´egrales premi`eres non triviales, sont les parties principales des
gj: gj,pr = x
rj
j − xj+1. Ces int´egrales premi`eres sont invariantes sous l’action
du sous-groupe du groupe lin´eaire GL(R, k), constitu´e des transformations de ma-
trice Tk,(ρ,α′) = Diag(ρ, ρr1,1, . . . , ρr1,k−1 ) avec ρ > 0. En utilisant l’action de χpr
sur x1, on obtient (Tk,(ρ,α′))
−1
∗ χpr = ρsk Ypr, avec sk = ∑k−1
j=1 r1,j et le champ
Ypr a la mˆeme expression que χpr dans la coordonn´ee y = Tk,(ρ−1,α′)(x). La
d´esingularisation adapt´ee au probl`eme est donc quasi-sph´erique dans la coordonn´ee
x et est ﬁbr´ee dans la coordonn´ee α
′. Soit la fonction

Q(y, α
′) =
 k∑

j=1 yrj,k
j

et pour ε > 0, les quasi-sphres

S+∗
k (ε) = {(y, α
′) ∈ (R+∗)
k × U2; Q(y, α
′) = ε}

on note S+∗
k (α
′, ε) leurs sections par les ﬁbres α
′ = constante. Le morphisme
d’´eclatement est

Tk : (ρ, y, α
′) ∈ R+∗ × S+∗
k (1) ↦→ (x, α
′) = (Tk,(ρ,α′)(y), α
′)

Soit Y le champ de vecteurs tel que ρsk Y = (Tk)
−1
∗ χ. Il admet comme int´egrales
premi`eres, outre la coordonn´ee α
′, les (k − 1) germes Gj = gj ◦ Tk et on v´eriﬁe
facilement que Gj = ρr1,j Lj avec Lj(ρ, y, α
′) = yrj
j (1 + O(ρ)) − yj+1, et elle est
localement induite par un lment de l’algbre QRHp
′(0),q′(0) avec p′(0) = p − k + 1
et q′(0) = (kq1 + k − 1, q2 + k − 1). Soit l’application L = (L1, . . . , Lk−1) et u
une coordonn´ee sur Rk−1. Pour simpliﬁer l’expression du champ Y, il est naturel
d’introduire le morphisme suivant

Lk(ρ, y, α
′) = (ρ, L(ρ, y, α
′), α
′) = (ρ, u, α
′)

Soit Lk,(ρ,α′) ses ﬁbres par (ρ, α
′) = constante et Dk(α
′) = Lk,(0,α′)(S+∗
k (α
′, 1)).
Notons simplement Dk au lieu de Dk(0).

Proposition IVA1.

(i) Le morphisme Lk,0 est un diﬀomorphisme de S+∗
k (0, 1) sur Dk qui se pro-
longe continument en une bijection de S+∗
k (0, 1) sur Dk.

(ii) Soit K un ouvert relativement compact de S+∗
k (0, 1). Alors, quitte `a r´eduire
le voisinage U2, le morphisme Lk est un diﬀomorphisme de Vk = (R+∗, 0) ×
((K × U2) ∩ S+∗
k (1)) sur son image ̃Uk = Lk(Vk). Les composantes de son
inverse sont localement induites par des lments de l’algbre QRHp
′(0),q′(0).

(iii) Sur ̃Uk, on a
 (Lk)∗Y ∼ ̃χ = ρ ∂
∂ρ −
 k−1∑

j=1 r1,j uj ∂
∂uj

62

Preuve. (i) Les (k − 1) germes Lj(0, ., .) sont des int´egrales premi`eres du champ
Ypr qui est transverse aux sph`eres S+∗
k (ε) car YprQ > 0. Donc, Lk,0 est un dif-
fomorphisme de S+∗
k (0, 1) sur Dk qui se prolonge continument S+∗
k (0, 1). Comme
rj (0) = 1 pour tout j, le systme

Q(y, 0) = 1 + u0, yj − yj+1 = uj

est linaire inversible, et ceci prouve que Lk,0 est une bijection de S+∗
k (0, 1) sur Dk.

(ii) C’est une cons´equence du (i), par transversalit´e et par la relative compacit´e
de K. La structure des composantes de l’inverse est consquence du thorme des
fonctions implicites driv du thorme de division VB3.

(iii) Etudions l’action de Y sur la coordonne ρ. On a ρr1,k = Q(x, α
′) = Q ◦
Tk(ρ, y, α
′) et donc ρsk (Yρr1,k ) = (χQ) ◦ Tk. Les sections de cette d´erni`ere fonction
par (ρ, α
′) =constante, sont (χQα′ ) ◦ Tk,(ρ,α′). Or pour y ∈ (R+∗)
k quelconque, on
a Qα′ ◦ Tk,(ρ,α′)(y) = ρr1,k Qα′(y), et donc

(χprQα′ ) ◦ Tk,(ρ,α′) = ρsk+r1,k (YprQα′)

La condition (b) sur la drivation d’Hilbert χ donne

((χ − χpr)Q) ◦ Tk = ρsk+r1,k O(ρ)

et donc
 Yρ = ρFk(ρ, y, α
′) avec Fk = 1
r1,k (YprQ) + O(ρ)

Soit ̂χ = (Lk)∗Y dﬁni sur ̃Uk. On a ̂χρ = ρ(Fk◦L
−1
k ). Or, les fonctions Gj ◦L
−1
k =
ρr1,j uj sont des int´egrales premi`eres de ̂χ. Par cons´equent ̂χuj = −r1,juj(Fk ◦L
−1
k ),
et le champ recherch´e est
 ̃χ = 1
Fk ◦ L
−1
k ̂χ

□

2.2. Sur le bord de S+∗
k (0, 1).

Ce bord est une union ﬁnie de sous-ensembles Bk′,i isomorphes chacun `a l’un
des sous-ensembles
 {0} × S+∗
k−k′,i(0, 1) ⊂ (R+)
k′ × (R+∗)
k−k′

avec k′ < k, l’indice i tant ´enum´eratif

Proposition IVA2. Soit y0 ∈ Bk′,i. Il existe un voisinage Vk′,i de (0, y0, 0) dans
R+∗ × S+∗
k (1) et un diﬀomorphisme Lk′,i de Vk′,i sur son image ̃Uk′,i tels que le
champ (Lk′,i)∗Y soit ´equivalent `a un ´el´ement de ΞHk′ [QRHp
′(k′),q′(k′)] avec p′(k′) =
p − k + k′ + 1 et q′(k′) = (kq1 + k − 1, q2 + k − k′ − 1). Ce morphisme Lk′,i se

63

prolonge continument et bijectivement sur V k′,i ∩ {0} × S+∗
k (0, 1). Ces composantes
et celles de son inverse sont induits par des lments de l’algbre QRHp
′,q′.

Preuve. Posons y0 = (y1,0, . . . , yk,0) et supposons d’abord que y0,1 = 0. Soit j0 le
plus petit des entiers j tels que yj,0 = 0 et yj+1,0 > 0. La preuve consiste trivialiser
le champ Y dans la coordonn´ee ρ en utilisant l’int´egrale premi`ere Gj0 puis, on le
trivialise de la mme faon dans les coordonnes yj telles que yj,0 > 0 et on utilise une
rcurrence sur le nombre d’intgrales premires non triviales. On a Gj0 = ρr1,j0 Lj0 et
Lj0 (ρ, y0, α
′) = −yj0+1,0 < 0, par consquent

Gj0 (ρ, y, α
′) = −yj0+1,0ρr1,j0 (1 + O(||y − y0||))

Soit G = (−Gj0 )
1/r1,j0 = cρ(1 + O(||y − y0||)) avec c > 0 et soit le morphisme

Ek′,i(ρ, y, α
′) = (G(ρ, y, α
′), Tk,(ρ/G,α′)(y), α
′) = (ρ′, y′, α
′)

par le thorme d’inversion VB4, gnralis plusieurs variables, il existe un voisinage
Vk′,i tel que le morphisme Ek′,i soit un diﬀomorphisme de Vk′,i sur son image V ′

qui est une sous-vari´et´e de (R+∗)
p
′ × R|q′| de codimension 1. De plus, il se prolonge
continument en une bijection de V k′,i ∩ {0} × S+∗
k (0, 1) sur V ′ ∩ {(ρ′, α
′) = 0}. Soit
Y ′ = (Ek′,i)∗Y, G tant une intgrale premire de Y, on a Y ′ρ′ = 0. Soit le morphisme
T ′
k(ρ′, y′, α
′) = (Tk,(ρ′,α′)(y′), α
′) dﬁni sur V ′. D’aprs la dﬁnition du morphisme
Ek′,i, on a le diagramme commutatif

(∗)
 Vk′,i Ek′,i
−−−−→ V ′

Tk

↓ 

↓T ′
k

Uk′,i id
−−−−→ Uk′,i

et donc les fonctions G
′
j = gj ◦ T ′
k sont des intgrales premires de Y ′. Or G
′
j =
(ρ′)
r1,j L′
j, donc les fonctions L′
j sont des intgrales premires de Y ′ et la sous-vari´et´e
V ′ est donn´ee par l’equation L′
j0 (ρ′, y′, α
′) = −1 qui est un graphe: y′
j0+1 =
f (ρ′, y′
j0, α
′) = 1+(y′
j0)
rj0 (1+O(y′
j0 )). Soit la projection canonique π′ : (ρ′, y′, α
′) ∈

V ′ ↦→ (ρ′, ̂y′j0+1, α
′) ∈ V ′
1 , le champ Y ′
1 = π′
∗Y ′ a pour intgrales premires les fonc-
tions L′
j pour j ̸∈ {j0, j0 + 1} et la fonction

L′
j0+1(ρ′, f, y′
j0+2, α
′) − L′
j0+1(ρ′, 1, 0, α
′) = a(ρ′, α
′)(y′
j0 )
rj0 (1 + O(y′
j0 )) − y′
j0+2

avec a(0) > 0. D’aprs le diagramme (∗), on a (T ′
k)
−1
∗ χ = (ρ′)
sk Y ′ et en utilisant
l’action de χ sur x1, on obtient Y ′y′
1 = ∏k
j=1 y′
j. Donc si k − k′ = 1, le champ Y ′
1 est
quivalent un lment de ΞHk′ par la rduction du paragraphe 1. Supposons k − k′ > 1
et rindxons les coordonnes y′
j et les intgrales premires L′
j. Il existe j1 ≥ j0 tel que
y′
j1,0 = 0 et y′
j1+1,0 > 0. Soit le morphisme

L
′
1 : (ρ′, y′, α
′) ∈ V ′
1 ↦→ (ρ′, ̂y′j1+1, α
′, L′
j1) = (ρ′, ̂y′j1+1, α
′, u′
j1 ) ∈ V ′
2

64

L’quation L′
j1 = u′
j1 est un graphe: y′
j1+1 = f1(ρ′, y′
j1, α
′, u′
j1 ). Par la mthode
ci-dessus, on montre que le morphisme L
′
1 est un diﬀomorphisme sur son im-
age et que le champ Y ′
2 = (L
′
1)∗Y ′
1 admet pour intgrales premires la coordonne
u′
j1 , les fonctions L′
j pour j ̸∈ {j1, j1 + 1} et la fonction L′
j1+1(ρ′, f1, y′
j1+2, α
′) −
L′
j1+1(ρ′, y′
j1+1,0, 0, α
′) = a1(ρ′, α
′, u′
j1 )(y′
j1 )
rj1 (1 + O(y′
j1 )) − y′
j1+2. Par l’hypothse
de rcurrence, il est quivalent un lment de ΞHk′ .

Supposons y1,0 > 0 et soit j0 le plus petit des entiers j tels que yj,0 > 0 et
yj+1,0 = 0. On trivialise le champ Y dans la coordonne ρ en utilisant l’intgrale pre-
mire Gj0 et le morphisme Ek′,i associ. Puis, on trivialise le champ Y ′ dans les co-
ordonnes y′
1, . . . , y′
j0 en utilisant les intgrales premires L′
1, . . . , L′
j0 par l’intrmdiaire
du morphisme
 L
′
0(ρ′, y′, α
′) = (ρ′, y′
j0+1, . . . , y′
k, L′
1, . . . , L′
j0−1, α
′)

le syst`eme d’´equations

L′
1 = u′
1, . . . , L′
j0−1 = u′
j0−1, L′
j0 = 1

dont les inconnues sont y′
1, . . . , y′
j0 , s’inverse ligne par ligne dans l’ alg`ebre QRHp
′,q′ .
Le champ Y ′
0 = (L
′
0)∗Y ′ admet pour intgrales premires la coordonne u′ et les
fonctions L′
j0+1, . . . , L′
k. D’aprs l’action de χ sur xj0+1, on a

Y ′y′
j0+1 = r1,j0 (y′
1)
r1 × · · · × (y′
j0 )
rj0 ∏

j>j0 y′
j(1 + O(ρ′))

et on conclut en utilisant la premire partie de la preuve. □

On note (πk, Nk) cette premire tape de la dsingularisation de χ de diviseur
exceptionnel Dk. Soit f ∈ QRHp,q et ̃f son relev par πk. Si a ∈ Dk, ̃fa est induit
par un lment de QRHp
′(0),q′(0) et si a ∈ ∂Dk tel que ̃χa soit de dimension de non
trivialit k′ − 1, ̃fa est induit par un lment de QRHp
′(k′),q′(k′).

B. L’hypothse (Hλ) et le lemme de rcurrence 1.

Considrons une drivation χ ∈ ΞHk[QRHk,q] ralise sur un voisinage U de 0.
Soient (gj) ses (k − 1) intgrales premires non triviales. Son morphisme intgral est
πχ(x, α) = (α, (gj(x, α))) = (α, λ). D’aprs les propositions IVA1 et IVA2, l’orbite
γ = {α = 0, g1 = · · · = gk−1 = 0} est principale dans U . Soit W une transversale
γ, analytique de coordonnes (α, λ). On dﬁnit de la mme faon que dans la partie
IIIA, les classes Ck
λ et Ck
λ,loc des germes f ∈ QRHk,q qui satisfont globalement ou
localement l’hypothse (Hλ).

Thorme IVB1. La classe Ck
λ,loc est localement χ-ﬁnie.

La preuve est base sur les thormes principaux II1 et IIIA2, et sur un argument
de rcurrence sur la dimension de non trivialit de la drivation d’Hilbert. Dﬁnissons
d’abord les anneaux des intgrales premires qui apparatront dans cette partie
 65

Dﬁnition IVB1. Soit t = (t1, . . . , tn) des coordonnes sur Rn. Notons A
n
0 (t) =
R{t}. Soit V0 un semi-analytique de l’anneau A
n
0 (t) qui est ouvert et qui adhre 0.
On note A
n
1 (V0) l’anneau des germes analytiques et borns sur (un germe en 0 de)
V0. Supposons dﬁni l’anneau A
n
i (.) et soit Vi un semi-analytique de cet anneau qui
est ouvert et qui adhre 0. On note A
n
i+1(Vi) l’anneau des germes analytiques et
borns sur (un germe en 0 de) Vi.

L’argument de rcurrence.

Soit x = (x1, . . . , xk), ρ = (ρ1, . . . , ρp) avec p > 0 et α = (µ, ν, ν′) des coordonnes
sur Rq1 × Rq2 × Rq3 . Soit q = (q1, q2 + q3) et soit une drivation χ ∈ ΞHk[QRHp+k,q]
ralise sur un ouvert U et d’int´egrales premi`eres non-triviales gj = x
rj
j (1+Dj)−xj+1.
Toujours d’aprs les propositions IVA1 et IVA2, la drivation χ admet une orbite
principale dans U incluse dans le bord de U : γ = {(ρ, α, (gj)j ) = 0}. Son morphisme
intgral est πχ : (x, ρ, α) ∈ U ↦→ (ρ, α, λ) = (ρ, α, (gj (x, ρ, α))j ) ∈ W o W est
isomorphe une semi-transversale γ.

(tk) Soit V un semi analytique d’un anneau A
q2
i (.) qui est ouvert et qui adhre 0
et soit
 im : ν ∈ V ↦→ (ρ(ν), µ(ν), ν, ν′(ν), λ(ν))) ∈ W

une immersion dont les composantes appartiennent l’anneau A
q2
i+1(V ).

Soit W0 = im(V ) ⊂ W et soit U0 = π−1
χ (W0). Notons U0,m et πχ,m les germes
de U0 et πχ en tout point m ∈ γ. Soit les morphismes π∗
χ : SBp,|q|+k−1 → SBp+k,|q|

et π∗
χ,m : SBp,|q|+k−1 → SBp,|q|+k

Lemme IVB1 (lemme de rcurrence 1). Soit f ∈ QRHk+p,q, on suppose que

(ik) Il existe N0 = (ni,0)i tel que pour tout m ∈ γ

π∗
χ,m|U0,m ((ρN0 )) ⊂ Iχ,f,m|U0,m

(iik) Il existe N1 = (ni,1) avec ni,1 > ni,0 tel que les germes f et Dj admettent
des reprsentants ∈ QRHcvg dans les quotients SB/(ρN1).

Alors f est localement χ-ﬁnie sur U0.

Remarque. Ce lemme est encore vrai dans des situations plus gnrales pour le
sous-ensemble W0. On garde cette formulation simple pour plus de cohrence avec
le deuxime lemme de rcurrence et parce qu’elle est suﬃsante pour la preuve du
thorme.

Preuve du lemme. Par rcurrence sur k. Le cas k = 1 est une consquence de la
premire partie de la preuve avec ̃χ = χ. Soit k > 1 et (πk, Nk) le premier clatement
de χ donn par les propositions IVA1 et IVA2, et soit Dk son diviseur exceptionnel.
Soient ̃χ et ̃f les relevs de χ et f par πk. Soit γ0 = π−1
k (γ). D’aprs la proposition
IVA1, la semi-transversale W est isomorphe une semi-transversale γ0 de mme
coordonne. Soit ̃U0 = π−1
k (U0), c’est aussi le satur de W0 par le ﬂot de ̃χ dans Nk.

Il s’agit de montrer que le faisceau I eχ, ef [Dk ∩ ̃U 0] est localement ̃χ-ﬁni.

66

(a) Au dessus de Dk.

Le dsingularis de χ est
 ̃χ = ρ0 ∂
∂ρ0 −
 k−1∑

j=1 r1,juj ∂
∂uj

soit a0 son unique singularit sur Dk. D’aprs l’hypothse (iik), il existe une fonction
g dﬁnie au dessus de tout relativement compact de Dk telle que pour tout a ∈ Dk,
le germe ga est induit par un lment de QRH1,.
cvg(ρ0, .) sur un semi-analytique de
QRHp,.
cvg(ρ, .) et

(1) ̃fa − ga ∈ (ρN1 )

Soit X(ρ, µ) les fonctions lmentaires de l’algbre QRHp(ρ, .) et soit l’immersion
c(ρ0, ρ, α, u) = (ρ0, α, X, u). Soit G ∈ QRH1,.
cvg(ρ0, .) tel que ga0 = c∗(G) et soit
ma+(G) sa multiplicit algbrique positive relativement ̃χa0 le long de γ0. Soit
U0 = c( ̃U0,a0 ) , Le point cl est que la multiplicit algbrique restreinte ma+(G|U0) ≤
ma+(G) est indpendante des reprsentants convergents de f et Dj dans les quo-
tients SB/(ρN1). En eﬀet, d’aprs la proposition IVA1, on a ρsk
0 ̃χ ∼ (π−1
k )∗(χ),
par consquent les ﬁbres diﬀrentielles le long de γ et γ0 sont isomorphes et d’aprs
l’hypothse (ik), les ﬁbres I eχa0 , efa0 ,m0| eU0,m0 contiennent l’idal π∗
eχa0 | eU0,m0 (ρN0 ) pour

tout m0 ∈ γ0. D’aprs (1), il en est de mme des ﬁbres de ga0 le long de γ0 restreintes
̃U0,a0 . Or le germe ga0 et les intgrales premires de ̃χ sont des lments d’un anneau
restriction analytique; le lemme d’isomorphie I4 s’applique: les ﬁbres diﬀrentielles
de ga0 le long de γ0 sont isomorphes et il en est de mme de celles de ̃fa0 restreintes
̃U0,a0 .

Il s’ensuit deux choses: d’une part, ̃fa0| eU0,a0 possde un idal ̃χa0-transverse le long

de γ0, qui coincide avec celui de ga0| eU0,a0 et qui contient l’idal (ρN0) (Il en est donc
de mme pour f|U0 le long de γ, par l’isomorphisme πk). D’autre part, la relation
(1) et le lemme IIIA5 montrent que ̃fa0| eU0,a0 est presque quasi-convergente,
et possde donc une multiplicit algbrique restreinte, qui conicide avec celle de
ga0| eU0,a0 et qui ne dpend donc pas du choix de g. Notons simplement ma+ cette
multiplicit.

Soit JG l’idal ̃χa0-transverse de G le long de c(γ0) et W0 = c(W0). Le thorme
principal IIIA1 s’applique l’action de ̃χa0 sur G par restriction U0

Ieχa0 ,G|U0 ⊃ (ρma++1
0 )π∗
eχa0 |U0(JG|W0 )

et en appliquant le morphisme c∗, on obtient

(2) Ieχa0 ,ga0 | eU0,a0 ⊃ (ρma++1
0 )π∗
eχa0 | eU0,a0 (Jga0 |W0)

Un plongement de f et χ est alors ncessaire. Soit f ′ et D′
j des reprsentants conver-
gents de f et Dj dans les quotients SB/(ρN1). Soit X(x, µ) les fonctions lmentaires

67

de l’algbre QRHk,.(x, .) et soient f ” = j
ma++3
X (f − f ′) et D”j = j
ma++3
X (Dj − D′
j).
Les germes f ” et D”j appartiennent l’idal (ρN1) et sont induits par des lments
de l’algbre QRHk,.
cvg(x, .) sur un semi-analytique de QRHp,.(ρ, .). En eﬀet, soit
(am(ρ, α)) la famille des coeﬃcients de f ” et des D”j dans leur dveloppement en
srie de X. Notons v = (am −am(0)) ces nouvelles coordonnes, les fonctions v(ν) ap-
partiennent aussi l’anneau A
q2
i+1(V ). Remplaons les coordonnes α par α
′ = (α, v)
et gardons les mmes notations pour im, W0, U0 ....

Ainsi, quitte remplacer f ′ par f ′+f ” et D′
j par D′
j +D”j, on peut supposer que f
et Dj admettent des reprsentants convergents dans les quotients SB/(ρN1)Mma++3
x .
La relation (1) est donc remplace par

(3) ̃fa − ga ∈ (ρma++2
0 ρN1)

et la relation (2) est encore satisfaite par l’invariance de la multiplicit algbrique
restreinte ma+.

Soit D0 = Dk ∩ ̃U 0. Montrons que pour tout a ∈ D0, le germe ̃fa est ̃χa-
quivalent ga sur ̃U0,a. Le thorme de ﬁnitude IB1 permettera de conclure. Soit γ1
une trajectoire incluse dans D0. Etudions le faisceau I eχ, ef ({a0} ∪ γ1)| fU0. En a0, on
a Jga0 |W0 ⊃ (ρN0 ) et d’aprs (2)

(4) Ieχa0 ,ga0 | eU0,a0 ⊃ (ρma++1
0 ρN0)

donc d’aprs (3), on a ( ̃fa0 − ga0 )| eU0,a0 ∈ MIeχa0 ,ga0 | eU0,a0 . Par consquent, ̃fa0 est

̃χa0 -ﬁnie sur ̃U0,a0.

Soit b ∈ γ1 suﬃsament proche de a0. D’aprs (4) et le lemme de cohrence IB3,
on a
 I eχ,g,b| eU0,b ⊃ (ρma++1
0 ρN0)

et donc d’aprs (3), ̃fb est ̃χb-ﬁnie sur ̃U0,b. Soit a un point quelconque de γ1, d’aprs
le lemme d’isomorphie IB4, les ﬁbres I eχ,g,b| eU0,b et I eχ,g,a| eU0,a sont isomorphes par le

ﬂot de ̃χ qui prserve l’idal (ρma++1
0 ρN0). Par consquent, ̃fa est ̃χa-ﬁnie sur ̃U0,a et
on a

(5) I eχ, ef,a| eU0,a ⊃ (ρma++1
0 ρN0 )

(b) Sur le bord de Dk.

Soit a1 = γ1 ∩ ∂Dk. Soit ̃χa1 le dsingularis de χ en a1. D’aprs la proposition
IVA2, c’est une drivation d’Hilbert de dimension de non trivialit k′ − 1 < k − 1.
Montrons d’abord la proprit (tk′ ). Dans la rduction de χ au voisinage de a1, on
trivialise dans la coordonne ρ0 en posant par exemple ρ′
0 = ρr1,1
0 |u1| = |λ1| si

68

u1(a1) ̸= 0. Les intgrales premires non triviales λ
′
j au voisinage de a1 sont des
fonctions rgulires des rapports
 u′
j = λj
(ρ′
0)r1,j

des intgrales premires non triviales en a0. Notons w ces nouvelles coordonnes
germiﬁes autour de γ1 et V ′ le semi-analytique de A
q2
i+1(V ) correspondant. On
obtient ainsi la proprit (tk′ ).

Montrons que ̃fa1 et ̃χa1 satisfont aux hypothses (ik′ ) et (iik′ ) du lemme. Soit
a ∈ γ1 suﬃsament proche de a1. D’aprs la proposition IVA2, les germes en a ∈ γ1
des champs ̃χ et ̃χa1 sont quivalents. Donc, d’aprs (5) et l’expression de πk en a1,
on a
 I eχa1 , efa1 ,a| eU0,a ⊃ ((ρ′
0)
ma++1ρN0)

ceci prouve l’hypothse (ik′ ) avec N ′
0 = (ma+ + 1, N0). Soient g′
j = (y′)
rj
j (1 + D′
j) −
y′
j+1 les intgrales premires non triviales de ̃χa1 . Les germes f et Dj admettent
des reprsentants convergents dans les quotients SB/(ρN1)Mma++3
x . Donc, d’aprs
l’expression de πk, les germes ̃fa1 et D′
j admettent des reprsentants convergents
dans les quotients SB/((ρ′
0)
ma++2ρN1 ). Ceci prouve l’hypothse (iik′ ) avec N ′
1 =
(ma+ + 2, N1). □

Preuve du thorme.

Soit f ∈ Ck
λ,loc et soit W0 ⊂ W un semi-analytique de R{α, λ} et N0 tels que

(6) Jχ,f,γ|W0 ⊃ MN0
λ|W0

En utilisant la stratiﬁcation analytique de W0, on peut supposer que c’est un graphe
analytique, d’o la proprit (tk). Notons que la preuve ci-dessous s’applique encore
des sous-ensembles W0 plus gnraux.

Soit U0 = π−1
χ (W0). La preuve reprend certains arguments de la preuve du
lemme de rcurrence IVB1 dont on reprend les notations. Soit (πk, Nk) le premier
clatement de χ de diviseur exceptionnel Dk et soit ̃U0 = π−1
k (U0).

(a) Au dessus de Dk. Soit

̃χ = ρ ∂
∂ρ −
 k−1∑

j=1 r1,j uj ∂
∂uj

le dsingularis de χ et ̃f le relev de f par πk. Soit γ0 = π−1
k (γ) et a0 l’unique
singularit´e de ̃χ sur Dk. La relation (6) est quivalente

(7) J eχa0 , efa0 ,γ0|W0 ⊃ MN0
λ|W0
 69

le germe ̃fa0 est donc presque quasi-convergent sur ̃U0,a0 et possde une multiplicit
algbrique restreinte ma+. D’aprs le lemme IIIA11, il est ̃χa0-ﬁni sur ̃U0,a0 et

Ieχa0 , efa0 | eU0,a0 ⊃ (ρma++1)π∗
eχa0 | eU0,a0 (J eχa0 , efa0 ,γ0|W0 )

Donc d’aprs (7), on a pour tout j

(8) Ieχa0 , efa0 | eU0,a0 ⊃ (ρma++1(ρr1,j uj)
N0 )| eU0,a0

Soit b ∈ γ1 proche de a0. L’une des coordonnes uj(b) est non nulle. Le lemme de
cohrence IB3 appliqu (8) donne

(9) I eχ, ef ,b| eU0,b ⊃ (ρN1 )

Soit X(ρ, µ) les fonctions lmentaires de l’algbre QRH1,.(ρ, .) et soit g = j
N1+1
X ( ̃f ).
Son germe en tout a ∈ Dk est induit par un lment de QRH1,.
cvg(ρ, .) et ̃fa − ga ∈
(ρN1+1). D’aprs (9) et le lemme de Nakayama, les ﬁbres en b de ̃f et g coincident,
et par le lemme d’isomorphie IB4, leurs faisceaux le long de γ1 coincident, et on a

(10) I eχ, ef ,a| eU0,a ⊃ (ρN1)

(b) Sur le bord de Dk.

On utilise le lemme de rcurrence IVB1. D’aprs (10), les ﬁbres de ̃f le long de γ1
satisfont l’hypothse (ik′ ). L’hypothse (iik′ ) est une consquence de la structure du
morphisme πk. □

C. Cas gnral et lemme de rcurrence 2.

Soient x = (x1, . . . , xk), α = (µ, ν) et χ ∈ ΞHk. Grce au thorme principal IIIB1,
on gnralise le thorme IVB1 dans le

Thorme IVC1. L’algbre QRHk,.(x, α) est localement χ-ﬁnie.

Preuve. Soit f ∈ QRHk,.. Nous allons montrer que f est localement χ-ﬁnie sur
un voisinage U de 0. Soit (πk, Nk) le premier clatement de la dsingularisation de
χ de diviseur exceptionnel Dk et soit ̃χ et ̃f les relevs par πk de χ et f . Montrons
que ̃f est localement ̃χ-ﬁnie sur un voisinage dans Nk de tout point de Dk.

1. Au dessus de Dk.

Soit u = (u1, . . . , uk−1) la coordonne globale sur Dk et (ρ, α, u) les coordonnes
sur Nk au dessus de Dk. D’aprs la partie A, on a

̃χ = ρ ∂
∂ρ −
 k−1∑

j=1 sjuj ∂
∂uj

70

et ̃fa ∈ QRH1,.(ρ, α, u − ua) pour tout a ∈ Dk. Soit a0 l’unique singularit de ̃χ sur
Dk et γ0 = {α = 0, u = 0} la trajectoire principale de ̃χa0 dans un voisinage Ua0
de a0. Soit πeχa0 : (ρ, α, u) ∈ Ua0 ↦→ (α, λ) ∈ W le morphisme intgral de ̃χa0.

1.1. En a0. Le rsultat est une consquence imm´ediate du thorme principal IIIB1.

1.2. En dehors de a0.

Soit J ⊂ R{α, λ} l’idal ̃χa0 -transverse de ̃fa0 le long de γ0. L’ide gnrale est la
suivante: on veut prparer ̃f dans J globalement au dessus de Dk. Ceci repose sur
une prparation de l’idal J + Mλ en vue de la dtermination de la perte d’analycit
dans J la traverse de l’ensemble singulier {ρ = 0, u = 0}. En eﬀet, l’ensemble
limite du satur du sous-ensemble Z(J) ∩ {λ = 0} est inclus dans le bord {ρ = 0}.
Soit donc (ψ, N ) une dsingularisation dans laquelle l’idal J + Mλ est principal,
monomial et ordonn (lemme IIIB1). Soit (c, Vc) une carte de cette dsingularisation
de coordonne v = (v1, . . . , vp). Notons Jc = (ϕ) = ψ∗
c (J) avec ϕ = ∏p
j=1 vnj
j .
Soient µj,c = ψ∗
c (µj), sj,c = 1 + µj,c et λj,c = ψ∗
c (λj). Quitte rindxer, on suppose
que

(1) (λk−1,c) ⊂ · · · ⊂ (λ1,c)

La perte d’analycit dans cette carte est alors l’image dans W du sous-ensemble
{λ1,c = 0}. Deux cas se prsentent:

(a) (λ1,c) ⊂ rad(ϕ). Dans ce cas, la perte d’analycit est totale: l’idal Jc satisfait
l’hypothse (Hλ) relativement l’idal ψ∗
c (Mλ). Le rsultat est donc une consquence
du thorme IVB1.

(b) Dans le cas contraire, soit p′ < p tel que λ1,c = vn
′
1
1 × · · · × vn
′
p′
p′ (1 + O(v)) avec
n′
j ≤ nj. Soit ϕ = ϕ
′ϕ” l’unique factorisation de ϕ telle que rad(ϕ
′) = rad(λ1,c)
et ϕ
′ ∧ ϕ” = 1. Pour obtenir une division globale (au dessus de Dk) de ̃f par
ϕ” = vnp′+1
p′+1 × · · · × vnp
p , il faut plutt tudier les intgrales premires ramiﬁes |λj,c|1/sj,c

(cf. (3) ci-dessous). Pour cela, une deuxime prparation des intgrales premires λj,c
et µj,c est ncessaire.

Pour simpliﬁer la prsentation, on notera toujours sj les relevs des fonctions
sj,c dans cette prparation. Soient p” = p − p′, v′
0 = (v′
j,0) = (v1, . . . , vp′ ), et
v”0 = (v”j,0) = (vp′+1, . . . , vp). Plaons nous dans un quadrant dans les coordonnes
v′
0, par exemple v′
j,0 > 0 pour tout j. Eﬀectuons une dsingularisation dans les
coordonnes v”0, et prenons par exemple la carte

(2) v”j,0 = v”1,0̂vj

puis faisons un clatement dans le couple (v”1,0, λ1,c). Deux cas se prsentent:

(b.1) |v”1,0| < ǫλ1,c. Dans ce cas, on pose

v”1,0 = v”1,1λ1,c, v”j,1 = ̂vj pour j > 1, v”1 = (v”j,1) et v′
1 = v′
0
 71

(b.2) λ1,c < (2/ǫ)|v”1,0|. Cette situation est couverte par un nombre ﬁni de cartes
qui sont de deux types: pour l’un, il existe j0 tel que (v′
j0,0)
n
′
j0 < (2/ǫ)|v”1,0|. Dans
ce cas, on pose

v′
j0,0 = v′
j0,1((2/ǫ)|v”0,1|)
1/n
′
j0 , v′
j,1 = v′
j,0 pour j ̸= j0,

v′
p′+1,1 = |v”0,1|1/n
′
j0 , v′
1 = (v′
j,1) etv”1 = (̂v2, . . . , ̂vp”) = (v”j,1)

Pour l’autre type, on a (v′
j,0)
n
′
j ≥ (2/ǫ)|v”1,0| pour tout j. Dans ce cas, on pose

v′
j,0 = v′
p′+1,1v′
j,1 avec
 p
′
∏

j=1(v′
j,1)
n
′
j = (2/ǫ)|v”0,1|,

v′
1 = (v′
j,1) et v”1 = (̂v2, . . . , ̂vp”) = (v”j,1)

Dans les deux cas, notons ̃v1 les coordonnes locales au voisinage des coordonnes
v′
. ou v”. qui ne sont pas voisines de 0. Soient µj,1, λj,1 et ϕ1 les relevs des fonctions
µj,c, λj,c et ϕ dans les coordonnes

v′
1 = (v′
1,1, . . . , v′
p′
1,1), v”1 = (v”1,1, . . . , v”p”1,1) et ̃v1 = (̃v1,1, . . . , ̃vep1,1)

On a (ϕ1) = (ϕ
′
1(v′
1))(ϕ”1(v”1)) avec rad(ϕ
′
1) = rad(λ1,1). On rpte alors ce procd
au plus p” fois appliqu aux cartes (b.2). A une certaine tape i de ce procd, on
obtient p”i = 0, auquel cas la perte d’analycit est totale et on est dans la situation
de l’hypothse (Hλ). Le rsultat est alors une consquence du thorme IVB1.

Plaons nous maintenant dans une carte (b.1) une certaine tape i. Soient µj,i,
λj,i et ϕi les relevs des fonctions µj,c, λj,c et ϕ dans les coordonnes

v′
i = (v′
1,i, . . . , v′
p′
i,i), v”i = (v”1,i, . . . , v”p”i,i) et ̃vi = (̃v1,i, . . . , ̃vepi,i)

On a (ϕi) = (ϕ
′
i(v′
i))(ϕ”i(v”i)) avec rad(ϕ
′
i) = rad(λ1,i). Soit (ci, Vi) cette carte
de coordonnes vi = (v′
i, ̃vi, v”i) avec Vi = V ′
i × ̃Vi × V ”i et V ′
i est un voisinage de
0 dans un quadrant, par exemple v′
j,i > 0 pour tout j. Soit Wi ⊂ W l’image de
cette carte et soit Ui le satur de Wi par le ﬂot de ̃χ. Il s’agit de diviser ̃f par ϕ”i
globalement au dessus de Di = Ui ∩ Dk.

Supposons que les fonctions µj,i et λj,i sont prpares sphriquement dans les coor-
donnes v”i comme dans le thorme principal IIIB1, dont on reprend les notations.
Divisons ρS ̃fa0|Ui,a0 par ϕ”i dans une extension adapte (̃QRHp”i|U0,p”i , πp”i ) sur
laquelle agit la drivation Xp”i . Soit Up”i le satur de U0,p”i par le ﬂot de Xp”i au
dessus de Dp”i+1
k et soit ∆i = U p”i ∩ Dp”i+1
k . Les sries de ρS ̃f dans les variables
w(n) = u(n−1) −u(n) sont convergentes sur un voisinage de 0 uniformment au dessus
de tout compact de la diagonale de Dp”i+1
k . Donc, la division en a0 est globale au
dessus de Di si ∆i est inclus dans cette diagonale.

72
 Or, en tout point a ∈ Di \ {a0}, il existe ℓ tel que uℓ(a) ̸= 0. Sur un voisinage
de a, les fonctions

(3) |uj|1/sj

|uℓ|1/sℓ = |λj|1/sj

|λℓ|1/sℓ

sont des intgrales premires de ̃χ. Notons τj,ℓ(vi) ces derniers rapports crits dans la
carte Vi pour des indices j, ℓ < k. Soit Vℓ,i = {vi ∈ Vi; τj,ℓ(vi) < 3 pour tout j}.
D’aprs (1) et l’clatement (b.1)

(4) λj,i ∈ Mv”i =⇒ λj,i ∈ (λ
2
1,i)Mv”i

Soit ki le plus grand indice j tel que λj,i ̸∈ Mv”i . D’aprs (1) et (4), les sous-
ensembles Vℓ,i sont vides pour tout ℓ = ki + 1, . . . , k − 1.

Plaons nous dans l’un des sous-ensembles Vℓ,i, par exemple V1,i et soient W1,i,
U1,i, U1,p”i , D1,i et ∆1,i les sous-ensembles correspondants. D’aprs l’clatement (b.1)

(5) µj,i − µj,i(v′
i, ̃vi, 0) ∈ (λ1,i)Mv”i

Donc les rapports τj,1 tendent vers τj,1(v′
i, ̃vi, 0) quand v”i tend vers 0 uniformment
en (v′
i, ̃vi). De plus, le sous-ensemble V1,i contient un produit V ′
1,i × V ”1,i o V ′
1,i =
{(v′
i, ̃vi) ∈ V ′
i × ̃Vi; τj,1(v′
i, ̃vi) < 2 pour tout j} et V ”1,i est un voisinage de 0.

Soit n ≤ p”i. Sur D1,i priv d’un voisinage de 0, la coordonne u1 ne s’annule
pas. Et d’aprs (5), |u1,n|1/s1,n /|u1|1/s1 tend vers 1 quand vi tend vers 0 (et mme
uniformment en (v′
i, ̃vi)). Donc, sur ∆1,i on a u1,n = u1. De mme, en utilisant les
rapports
 τ ′
j,1,n = |uj,n|
|u1,n|sj,n/s1,n

et la relation (5), on montre que sur ∆1,i on a uj,n = uj pour tout j et pour tout
n. Le sous-ensemble ∆1,i est donc inclus dans la diagonale de Dp”i+1
k .

Soit h le quotient de la division de ρS ̃f par ϕ”i au dessus de ∆1,i. Pour tout

A ∈ ∆1,i, on a hA ∈ ̃QRHp”i(ρ, vi, u − u(A), u(1) − u(1)(A), · · · , u(p”i) − u(p”i)(A)).
Soit A0 = {ρ = 0, vi = 0, u = u(1) = · · · = u(p”i) = 0} la singularit principale
de Xp”i . L’idal transverse de hA0|U1,p”i est (ϕ
′
i) qui satisfait l’hypothse (Hλ).
On conclut donc au rsultat par les mthodes de la partie B appliques au faisceau
IXp”i ,h[∆1,i].

2. Sur le bord de Dk.

On utilise le lemme de rcurrence 2 ci-dessous, qu’on a choisi de prsenter au 3
pour deux raisons: d’une part, ses ides gnralisent simplement celles des 1 et 2 et
celles du lemme de rcurrence 1, et d’autre part sa prsentation est beaucoup plus
diﬃcile essentiellement cause des notations. Soit γ ⊂ D1,i une trajectoire de ̃χ,

73

a = ∂Dk ∩ γ et k′ la dimension de non trivialit de la drivation d’Hilbert ̃χa. Il s’agit
de prouver les hypothses algbriques (ik′ ) et (iik′ ) et la proprit topologique (tk′ ) au
voisinage de a.

Soit Ck′ le sous-ensemble de ∂Dk constitu des points o la dimension de non
trivialt de la drivation d’Hilbert est k′ − 1. Quitte rduire les rapports τj,1 dans
un voisinage de leurs valeurs sur γ, on suppose que l’adhrence de D1,i ne rencontre
qu’une seule composante connexe de Ck′ . Soit Γ ⊂ ∆1,i l’orbite du champ Xp”i
correspondante γ et soit A le point de Γ correspondant a. D’aprs le 1.2, pour tout
point B de Γ voisin de A, les ﬁbres IXp”i ,h,B|U1,p”i sont noethriennes et satisfont,
par restriction U1,p”i l’inclusion

(ρn0 ) ⊂ IXp”i ,h,B

Or si b est le point de γ correspondant B, les germes Xp”i,B et ̃χb sont rguliers et
donc ”quivalents”: plus prcisment, les fonctions

u′
j,n = uj,n
|u1|sj,n/s1

sont des intgrales premires analytiques de Xp”i le long de Γ. Soit u′
j,n(Γ) leurs
valeurs sur Γ. Dans le changement de coordonnes ν′
j,n = u′
j,n − u′
j,n(Γ) germiﬁ au
dessus de Γ, le champ Xp”i est transform dans le champ ̃χ. Donc, dans une extension
vidente de SB|U1,i,b obtenue par adjonction des coordonnes ν′
j,n, les ﬁbres I eχ,ρS ef ,b
sont noethriennes et satisfont la double inclusion

(ρn0 )π∗
eχ,b(ϕ”i) ⊂ I eχ,ρS ef ,b ⊂ π∗
eχ,b(ϕ”i)

et ceci prouve l’hypothse (ik′ ) car le germe en b de la drivation d’Hilbert ̃χa est
quivalent la drivation ̃χb. L’hypothse (iik′ ) est une consquence de la structure du
morphisme de dsingularisation πk.

Dans la rduction de la drivation d’Hilbert χ au voisinage de a, on trivialise
dans la coordonne ρ en posant (ρ′)
s1 = ρs1 |u1| = |λ1,i|. Les intgrales premires non
triviales λ
′
j au voisinage de a sont des fonctions rgulires des rapports ν′
j = λj,i/(ρ′)
sj

d’intgrales premires en a0. On obtient donc la proprit (tk′ ) en posant

ρ(1) = v′
i, L′ = L, ̃ν = ̃vi, ν = v”i, ν′ = ((ν′
j), (ν′
j,n)), V ′ = V ′
1,i et V = V ”1,i

□

3. L’argument de rcurrence.

Dﬁnissons d’abord les espaces des intgrales premires correspondants cette situ-
ation et qui gnralisent ceux de la partie B

Dﬁnition IVC1. Soit (x, α) des coordonnes sur Rk × Rn. Notons

A
k,n
0 (x, α) = A
k,n(x, α)

Soit V un semi-analytique ouvert de A
k,n
0 (x, α) qui adhre 0. On note A
k,n
1 (V )
l’anneau des germes de fonctions analytiques et bornes sur (un germe en 0 de) V .

74

Supposone dﬁnis les anneaux A
k,n
i (.). Soit V un semi-analytique ouvert de A
k,n
i (.)
qui adhre 0. On note A
k,n
i+1(V ) l’anneau des germes de fonctions analytiques et
bornes sur (un germe en 0 de) V .

Dﬁnition IVC2. Soient (x, α, β) des coordonnes sur Rk × Rn × Rm. Notons

A
k,(n,m)
0 (x, α, β) = A
k,n+m(x, α, β)

Soit V ′ un semi-analytique ouvert d’un anneau A
k,n
i (.) qui adhre 0, et soit V un
voisinage de 0 dans Rm. On note A
k,(n,m)
i (V ′×V ) l’anneau des germes de fonctions
analytiques et bornes sur (le germe en 0 de) V ′ × V o V est le complexiﬁ de V .

Remarque IVC1. Tout f ∈ A
k,(n,m)
i (V ′ × V ) est la somme d’une srie

(6) f = ∑

N fN (x, α)βN

convergente sur le produit d’un reprsentant V ′
f de V ′ et d’un polydisque de Cm et
dont les coeﬃcients fN appartiennent l’anneau A
k,n
i+1(V ′) et sont tous raliss sur V ′
f .

Soient x = (x1, . . . , xk), ρ = (ρ1, . . . , ρL) avec L > 0 et α = (µ, ν, ̃ν, ν′) une coor-
donne sur Rq1 ×Rq2 ×Rq3 ×Rq4. Soient q = (q1, q2+q3 +q4) et χ ∈ ΞHk[QRHk+L,q].
Soit U un voisinage de 0 sur lequel χ est ralise et soient gj = x
rj
j (1 + Dj) − xj+1 ces
intgrales premires non triviales. Posons g = (g1, . . . , gk−1) et soit γ = {(ρ, α, g) =
0} l’orbite principale dans U . Soit πχ : (x, ρ, α) ∈ U ↦→ (ρ, α, λ) = (ρ, α, g) ∈ W
le morphisme intgral de χ. Soit ρ(1) = (ρ1, · · · , ρL′), ρ(2) = (ρL′+1, · · · , ρL),
β = (ρ(1), ̃ν) et soit

im : (β, ν) ∈ V ′ × V ↦→ (ρ(1), ρ(2)(β), µ(β, ν), ν, ̃ν, ν′(β, ν), λ(β, ν)) ∈ W

une immersion telle que

(tk) V ′ est un semi-analytique ouvert d’un anneau A
L′,q3
. (.) et V est un voisinage de
0 dans Rq2. De plus, les fonctions composantes de ρ(2) appartiennent un anneau
A
L′,q3
. (V ′) et les fonctions composantes de µ, ν′ et λ appartiennent un anneau
A
L′,(q3,q2)
. (V ′ × V ).

Soit W0 = im(V ′ × V ) et soit U0 = π−1
χ (W0). Si m ∈ γ, on note U0,m le germe
de U0 en m.

Lemme IVC1 (lemme de rcurrence 2). Soit f ∈ QRHk+L,q. On suppose que
(ik) il existe un idal J0 ⊂ R{ν} et N0 = (ni,0) tels que pour tout m ∈ γ, la ﬁbre
Iχ,f,m|U0,m satisfait, par restriction U0,m la double inclusion

π∗
χ,m((ρN0)J0) ⊂ Iχ,f,m ⊂ π∗
χ,m(J0)

(iik) il existe N1 = (ni,1) avec ni,1 > ni,0 tel que les germes f et Dj admettent
des reprsentants convergents dans les quotients SB/(ρN1).
 75

Alors f est localement χ-ﬁnie sur U0.

Preuve. Elle est base sur une rcurrence sur la dimension de non-trivialit k − 1
et sur les arguments de l’algorithme de ﬁnitude utiliss dans le lemme de rcurrence
IVB1. L’tape k = 1 est une consquence de ce qui suit. L’ide gnrale est la suivante:
aprs dsingularisation de χ si ncessaire, on divise le relev de f dans l’idal J0. Par
l’hypothse (ik), le quotient de cette division satisfait alors aux hypothses du lemme
de rcurrence IVB1.

Soit (πk, Nk) le premier clatement de la dsingularisation de χ de diviseur excep-
tionnel Dk et soit ̃χ et ̃f les relevs par πk de χ et f . En identiﬁant W0 son image
par π−1
k , soit ̃U0 le satur de W0 par le ﬂot de ̃χ. Montrons que ̃f est localement

̃χ-ﬁnie sur un voisinage dans ̃U0 de tout point de Dk ∩ ̃U 0.

3.1. Au dessus de Dk.

Soit u = (u1, . . . , uk−1) la coordonne globale sur Dk et (ρ0, ρ, α, u) les coordonnes
sur Nk au dessus de Dk. On a

̃χ = ρ0 ∂
∂ρ0 −
 k−1∑

j=1 sjuj ∂
∂uj

et ̃fa ∈ QRH1+L,.(ρ0, ρ, α, u − ua) pour tout a ∈ Dk. Soit a0 l’unique singularit de
̃χ sur Dk et γ0 = {ρ = 0, α = 0, u = 0} la trajectoire principale de ̃χa0 dans un
voisinage de a0.

3.1.1. En a0.

La preuve reprend, en la gnralisant, la mthode du thorme principal IIIB1. Soit
(ψ, N ) une dsingularisation (dans les coordonnes ν) dans laquelle l’idal J0 est prin-
cipal et monomial. En utilisant (6), on suppose que les fonctions µj et λj sont
prpares sphriquement dans cette dsingularisation. Soit donc (c, Vc) une carte de
cette dsingularisation de coordonne v et soit Wc ⊂ W0 et Uc ⊂ ̃U0 les ensembles
correspondants. Soit Jc = (ϕ) = ψ∗
c (J0), avec ϕ = ∏p
j=1 vnj
j . Soient µj,c = ψ∗
c (µj)
et λj,c = ψ∗
c (λj ) avec

(7) µj,c = µj,p+1−i + µ′
j,p+1−i et λj,c = λj,p+1−i + λ
′
j,p+1−i

les fonctions µj,p+1−i et λj,p+1−i sont indpendantes des coordonnes (vi, . . . , vp).
Les fonctions µ′
j,p+1−i et λ
′
j,p+1−i appartiennent l’idal (v1 × · · · × vi) dans l’anneau
A(V ′ × Vc).

Dans la division de ρS0
0 ̃fa0 par ϕ, les nouvelles fonctions lmentaires des exten-
sions ̃QRH portent sur les coordonnes (ρ0, ρ) de l’algbre QRH1+L,.. De plus les
(fonctions) coordonnes (µ, ν′) analytiques de cette algbre et les intgrales premires
λ donnent lieu, dans cette division, des (fonctions) coordonnes analytiques de
l’extension qu’on notera (ν′)
(0).

76
 Soit donc (̃QRH1+L

p (ρ0, ρ, v, ̃ν, (ν′)
(0), (u(j)
0 ))|Up , πp) l’extension dans laquelle la
division de π∗
p(ρS0
0 ̃fa0) par ϕ est ralise. Cette extension est dﬁnie par les formules
sphriques (7), et par une induction sur L comme pour les algbres QRH1+L,.. Soit
h0 le quotient de cette division. Soit Xp la drivation qui relve ̃χa0 sur Uc,0 germe de
Uc en a0. Soit Γ0 son orbite principale, et A0 sa singularit principale. On a ρ0 ̸= 0
le long de γ0. Donc en appliquant le morphisme π∗
p (πp tant germiﬁ le long de Γ0)
la double inclusion (ik), on obtient que les ﬁbres de h0 le long de Γ0 contiennent
ρN0 (par restriction Up).

Ds lors, on applique la mthode du lemme de rcurrence IVB1. Soit ma+ la
multiplicit algbrique d’un reprsentant convergent de h0 modulo (ρN1), il en existe
un d’aprs l’hypothse (iik). Ce reprsentant satisfait globalement la double inclusion
en A0 d’aprs le thorme principal IIIA1. Donc, en prenant un plongement de f et
des fonctions Dj un ordre quelconque n0,1 > ma+ (cf. lemme de rcurrence IVB1),
on obtient que h0 est Xp-ﬁnie sur une restriction Up,n0,1 de ce plongement (et il
en est de mme pour ̃fa0 sur Uc,0,n0,1 germe en a0 d’une restriction Uc,n0,1 de ce
plongement). De plus on a la double inclusion par restriction Up,n0,1

(8) (ρma++1
0 ρN0ϕ) ⊂ I
Xp,π∗
p (ρ
S0
0 efa0 ) ⊂ (ϕ)

3.1.2 En dehors de a0.

Comme dans le paragraphe 1.2, on veut dterminer la factorisation Jc = (ϕ
′)(ϕ”)
telle que le sous-ensemble image dans Wc de {ϕ
′ = 0} reprsente la perte d’analycit
la traverse des singularits a0(α) et telle que la division de ̃f par ϕ” soit globale
au dessus du sous-ensemble correspondant Dc ⊂ Dk. On gnralise la prparation du
paragraphe 1.2 aux anneaux A(V ′ ×Vc) de la faon suivante: soit λ
′
j,c(β) = λj,c(β, 0)
et λ”j,c = λj,c − λ
′
j,c. D’aprs (2), on a λ”j,c ∈ (v1). Donc, l’ensemble limite du
satur par le ﬂot de ̃χ de l’image dans Wc du sous-ensemble {(λ
′
j,c) = 0, v1 = 0}
est inclus dans l’ensemble singulier de ̃χ au dessus de a0. Considrons donc les
ensembles V ′
ℓ,c = {|λ
′
j,c| < 2|λ
′
ℓ,c|; pour tout j} pour ℓ = 1, . . . , k − 1 et V ′
k,c =
{|λ
′
j,c| < 2|v1|, pour tout j}. La pr´eparation (pr) est la suivante

(pr1) Sur V ′
k,c, on pose

v′
1 = v1 = (v′
1,1), v”1 = (v2, . . . , vp) = (v”1,1, . . . , v”p”1,1) et β1 = (β, v′
1)

Remarquons que p”1 < p. Les fonctions λj,c se relvent dans les fonctions λj,1 =
v′
1,1(λ
′
j,1(β1) + O(v”1)).

(pr2) Sur V ′
1,c par exemple, deux cas se prsentent:

(pr2.1) |v1| ≤ ǫ|λ
′
1,c|. On pose alors

v1 = v”1,1λ
′
1,c, v′
1 = λ
′
1,c = (v′
1,1), β1 = (β, v′
1) et v”1 = (v”1,1, v2, . . . , vp) = (v”j,1)

77

Les fonctions λj,c se relvent dans les fonctions λj,1 = v′
1,1(λ
′
j,1(β1) + O(v”1)). Re-
marquons que λ
′
1,1 ≡ 1.

(pr2.2) ǫ|λ
′
1,c| < |v1| < 2|λ
′
1,c|. Ce cas se trate comme le cas (pr1).

On rpte ce procd au plus p fois appliqu aux cartes (pr1). A une certaine tape,
on obtient p”. = 0. La perte d’analycit est alors totale.

Plaons nous dans une carte (pr2.1) une tape i. Les relevs des fonctions λj,c
s’crivent
 λj,i =
 p
′
i∏

ℓ=1 v′
ℓ,i(λ
′
j,i(βi) + O(v”i)) avec λ
′
1,i ≡ 1

D’aprs (7), on a O(v”i) = O(v”1,i). Dans ce cas, on applique la mthode prparatoire
(pr) ci-dessus aux (fonctions) coordonnes λ
′
j,i ̸≡ 1 et la coordonne v”1,i. Puis,
on applique la mthode du paragraphe 1.2 (cas (b)) au couple constitu du facteur
dominant de la prparation (pr) et de la (fonction) coordonne λ1,i qui reprsente la
perte d’analycit. On rpte ce procd au plus (k − 2 + p”i) fois appliqu aux cartes
(b.2). A une certaine tape de cette prparation, on obtient p”. = 0.

Dans tous les cas, notons ̃vi les coordonnes locales au voisinage des coordonnes
v”. qui ne sont pas voisines de 0. Posons vi = (v′
i, ̃vi, v”i) et ̃βi = (βi, ̃vi). On obtient
la factorisation du relev (ϕi) = (ϕ
′
i(v′
i))(ϕ”i(v”i)) et la prparation des relevs

λ1,i =
 p
′
i∏

j=1
(v′
j,i)
n
′
1,j,i (1 + O(v”i))

et pour ℓ ̸= 1
λℓ,i =
 p
′
i∏

j=1(v′
j,i)
n
′
ℓ,j,i (λ
′
j,i( ̃βi) + O(v”i)) avec n′
ℓ,j,i ≥ n′
1,j,i

D’aprs cette double prparation, il existe une partition v′
i = (ρ′
i, ρ”i) telle que
les coordonnes ρ”i soient des fonctions des coordonnes β′
i = (β, ρ′
i, ̃vi) appartenant
un anneau A.(V ′
i ) o V ′
i est un semi-analytique ouvert d’un anneau A.(.) donn
par la prparation ci-dessus. Comme dans le paragraphe 1, on utilise (7) pour
montrer que les rapports τj,ℓ(β′
i, v”i) convergent vers τj,ℓ(β′
i, 0) quand v”i tend
vers 0 uniformment en β′
i sur les sous-ensembles non vides Vℓ,i = {(β′
i, v”i) ∈
V ′
i × Vi; τj,ℓ < 3 pour tout j} o Vi est un voisinage de 0 dans Rp”i donn par la
prparation ci-dessus. De plus ce sous-ensemble Vℓ,i contient le produit de V ′
ℓ,i =
{β′
i ∈ V ′
i ; τi,ℓ < 2 pour tout j} qui est un semi-analytique ouvert de A.(V ′
i ), et
d’un voisinage V ”ℓ,i de 0.

Plaons nous dans l’un des sous-ensembles non vides Vℓ,i, par exemple V1,i et sup-
posons que les fonctions µj,i et λj,i sont prpares sphriquement dans les coordonnes
v”i. Soit h le quotient de la division de ρS1
0 ̃f par ϕ”i en a0 (si p”i = 0, on prend
h = ̃f ). Soit n′
i le plus petit entier tel que λ
n
′
i
1,i ∈ (ϕ
′
i). Choisissons un ordre n0,1 de
plongement de f et des fonctions Dj (cf. 3.1.1) tel que

78
 n0,1 > n0,0 = ma+ + 1 + S1(0) + 2n′
i

Soit (̃QRH
1+L

p”i|Up”i , πp”i ) l’extension associe cette division. Soient W1,i, U1,i ⊂
Uc,n0,1, U1,p”i , D1,i et ∆1,i les sous-ensembles correspondants V1,i. Comme dans
le paragraphe 1, on montre que ∆1,i est inclus dans la diagonale de Dp”i+1
k . Donc
cette division est globale au dessus de ∆1,i et pour tout A ∈ ∆1,i, on a hA ∈

̃QRH1+L

p”i (ρ0, ρ, vi, ̃ν, (ν′)
(1), u − u(A), u(1) − u(1)(A), · · · , u(p”i) − u(p”i)(A)). Les
coordonnes (v′)
(1) sont dﬁnies comme les coordonnes (v′)
(0).

En tout point b ∈ D1,i \ {a0}, les champs ̃χb et Xp,B (cf. 3.1.1) sont quivalents.
Comme dans le paragraphe 1, dont on reprend les notations, on construit une exten-
sion de SB|U1,i,b par adjonction de (fonctions) coordonnes (ν′)
(2) qui appartiennent
un anneau A.(V ′
1,i × V ”1,i) d’aprs (7) et la prparation ci-dessus. Et d’aprs (8) et le
lemme de cohrence I3, si en plus b ∈ U c,0,n0,1, on a la double inclusion dans cette
extension

(9) (ρma++1
0 ρN0ϕi) ⊂ I eχ,ρ
S0
0 ef ,b ⊂ (ϕi)

De mme, en tout point b ∈ D1,i \ {a0}, les champs ̃χb et Xp”i,B sont quivalents. On
construit donc une extension de cette dernire extension par adjonction de (fonc-
tions) coordonnes (ν′)
(3) ∈ A.(V ′
1,i × V ”1,i) et on note H l’image de h dans cette
extension. On a donc sur une restriction adquate au dessus de D1,i \ {a0}

(10) ρS1
0 ̃f = ϕ”iH

et si b est voisin de a0, la double inclusion (9) donne

(11) (ρS1+ma++1
0 ρN0ϕ
′
i) ⊂ I eχ,H,b

Or sur D1,i \ {a0}, la coordonne u1 ne s’annule pas et on a λ
n
′
i
1,i ∈ (ϕ
′
i). Donc
l’inclusion (11) donne

(12) (ρn0,0
0 ρN0) ⊂ I eχ,H,b

et par le plongement ci-dessus l’ordre n0,1, le germe de H en tout point de D1,i est
convergent modulo (ρn0,1
0 ρN1). Pour conclure, on applique la mthode du lemme de
rcurrence IVB1 H au dessus de D1,i et on utilise (10).

3.2 Sur le bord de Dk.

Soit a ∈ D1,i ∩ ∂Dk et k′ − 1 la dimension de non trivialitde la drivation
d’Hilbert en a. Il reste simplement nommer les donnes du lemme en fonction
de k′. On pose ρ(1)
k′ = (ρ(1), ρ′
i), ̃νk′ = (̃ν, ̃vi), νk′ = v”i, ρ(2)
k′ = (ρ(2), ρ”i),
ν′
k′ = (((ν′)
(j))j=0,...4, (ν′
j)) o les (fonctions) coordonnes (ν′)
(4) proviennent du

79

plongement l’ordre n0,1 et les ν′
j sont dtermins par les rapports τj,1 comme dans
le paragraphe 2. On pose aussi V ′
k′ = V ′
1,i, Vk′ = V ”1,i, N0,k′ = (n0,0, . . . , n0,0, N0)
et N1,k′ = (n0,1, . . . , n0,1, N1), n0,0 et n0,1 tant rpts p′
i fois. Le reste de la preuve
est maintenant classique! □

Preuve du thorme 0.

Soit (Xν , Γk) un dploiement analytique de X0 q0 paramtres. D’aprs le thorme
VA1 (appendice VA), il existe des transversales analytiques σj et τj au voisinage
de chaque sommet Pj tels que l’application de Dulac du coin Pj soit induite par
un lment dj ∈ QRH1,(1,q0)(xj , µj, ν). Posons α = (µ1, . . . , µk, ν) = (µ, ν) et q =
(q1, q2) = (k, q0). Soient λj (ν) les germes qui dploient les connexions γj,j+1. Les
cycles du champ Xν proches de Γk rencontrent les transversales σj aux points dont
les abscisses xj sont solutions du systme

(13) d1(x1, α(ν)) − f2(x2, α(ν)) = λ1(ν), . . . , dk(xk, α(ν)) − f1(x1, α(ν)) = λk(ν)

les germes fj ´etant des diﬀ´eomorphismes analytiques dans la variable xj qui prser-
vent l’origine et l’orientation. Par la rduction de la partie A, le systme (13) est
quivalent au systme

d1(x1, α(ν)) − x2 = λ1(ν), . . . , dk(xk, α(ν)) − x1 = λk(ν)

Posons x = (x1, . . . , xk) et λ = (λ1, . . . , λk−1). Soit χ ∈ ΞHk[QRHk,q] dont
(k − 1) intgrales non triviales sont gj(xj , xj+1, α) = dj (xj, α) − xj+1. Soit W0
l’image d’un voisinage de 0 dans Rq0 par l’immersion ν ↦→ (α(ν), λ(ν)) et soit
U0 = π−1
χ (W0). Soit f (x, α) = dk(xk, α) − x1 − λk(ν). Alors la partie (i) du thorme
est quivalente la χ-rgularit de f sur U0 et la partie (ii) est vriﬁe si l’idal diﬀrentiel
Iχ,f est localement noethrien sur U0 ( extensions toiles prs). Le thorme 0 est donc
une consquence simple du thorme IVC1 ci-dessus. □

Appendice V.

A. Dploiements d’applications de Dulac.

Il est connu ( [E] et [I] ) que l’application de Dulac d’une singularit´e hyperbolique
r´eelle est un ´el´ement de QA
1,0. Un th´eor`eme de [M-M] dit que l’application de Dulac
est ”convergente” si et seulement si la singularit´e est analytiquement normalisable.
Ceci limite consid´erablement le champ d’application des arguments classiques de
la g´eom´etrie analytique et justiﬁe l’approche quasi-analytique adopt´ee qui prolonge
celles d’Ecalle et d’Il’yashenko.

On se limitera au cas d’une ´equation diﬀ´erentielle r´esonnante de nombre car-
act´eristique r = 1; le cas r = n/m s’en d´eduit par une double ramiﬁcation et le
cas quasi-r´esonnant pr´esente moins de diﬃcult´e. Soit ων = xdy + y(1 + µ(ν) +
a(x, y, ν))dx un d´eploiement analytique `a q param`etres ν = (ν1, . . . , νq) d’une 1-
forme analytique r´eelle r´esonnante. Ce d´eploiement est induit par le d´eploiement

ωα = xdy + y(1 + µ + a(x, y, ν))dx

80

avec α = (µ, ν) ∈ W1 × Wq ∈ (R, 0) × (Rq, 0). On pose r = 1 + µ. L’objet de cette
partie est le

Thorme VA1. Soit d(., α) l’application de Dulac de ωα, alors il existe D ∈
QRH1,(1,q) tel que d = x
r(1 + D) et D(0) = 0.

La propri´et´e de quasi-analycit a ´et´e d´emontr´ee dans [E-M-R] sur des domaines
de EI de type puissance

(1) {w = u + iv; |v| < Cun; u ≫ 1}, C > 0, n ≥ 2

en utilisant l’id´ee g´eom`etrique d’Il’yashenko [I] bas´ee sur la structure de l’holonomie
de l’une des s´eparatrices. Or les domaines de EI qui s’imposent naturellement dans
le probl`eme sont les domaines qui sont optimaux pour les formes normales; i.e les
domaines d’Ecalle [E] de type exponentiel

(2) {w = u + iv; |v| < C exp(u/K) − 1; u ≫ 1}, C > 0, K > 1

On adopte une d´emarche qui combine l’id´ee g´eom`etrique d’Il’yashenko en modiﬁant
les chemins d’int´egration, et celle de Dulac [D] qui consiste `a construire une int´egrale
premi`ere analytique dans l’une des variables. On suppose que ωα est pr´epar´ee `a
l’ordre 1

(3) a = xy ∑

n≥1 an(x, ν)yn−1

et qu’on a la majoration suivante

(4) ∑

n≥1 ∥an∥D(0,1)×Wq ≤ 1/4

o`u Wq est le complexiﬁ´e de Wq. Soit

(5) f (x, y, α) = ∑

n≥1 fn(x, α)yn

l’int´egrale premi`ere de ωα telle que f (1, y, α) ≡ y. L’application de Dulac de ωα
est analytiquement conjugu´ee `a

(6) d(x, α) = f (x, 1/2, α)

et le th´eor`eme est cons´equence de la
 81

Proposition VA1. Il existe F ∈ QRH1,(1,q+1) tel que f = x
ry(1+F ) et F (0) = 0.

1. Oprateur intgral de Dulac.

Notons P + = {w ∈ C; Re(w) > 0}. Soit Ω un ouvert simplement connexe de
P + tel que 0 ∈ Ω et Hc(Ω) l’espace des fonctions holomorphes sur Ω et continues
sur Ω. Pour tout s ∈ C∗, on d´eﬁnit sur Hc(Ω) l’op´erateur Ls par

(7) Ls(f )(w) = s exp(−sw) ∫

γw exp((s − 1)z)f (z)dz

o`u γw ⊂ Ω est un chemin C1 rgulier joignant 0 et w. Pour s ﬁx´e, l’ensemble
Ls = {w ∈ P +; Re(sw) = 0} est dit direction singuli`ere de l’operateur Ls et
Ωs = {w ∈ P +; Re(sw) > 0} est dit domaine non-singulier de Ls. On montre que,
sous une certaine condition g´eom`etrique sur le chemin γw, et donc sur l’ouvert Ω,
l’op´erateur Ls est 2-lipschitzien.

Lemme VA1. Si Ω ⊂ Ωs et si le long du chemin γw la condition suivante est
satisfaite

(8) | tan(arg(s dz
dt ))| ≤ | exp(z)|

alors pour tout f ∈ Hc(Ω)

(9) |Ls(f )(w)| ≤ 2∥f ∥γw

Preuve. Soit t0 tel que z(t0) = w. Grˆace `a (8), on a la majoration

|Ls(f )(w)| ≤ 2∥f ∥γw| exp(−sw)| ∫ t0

0 |Re(sz ′)| exp(Re(sz))dt

le chemin γw ´etant C1-rgulier, la condition (8) implique que la fonction Re(sz′) ne
s’annule pas sur γw. Et comme Ω ⊂ Ωs, le r´esultat en d´ecoule facilement. □

2. Preuve de la proposition.

C’est une consquence du lemme VA1 et des lemmes ci-dessous. Les coeﬃcients
fn de la s´erie de f v´eriﬁent les ´equations diﬀ´erentielles

x ∂fn
∂x − nrfn = x
∑n−1

p=1 pan−pfp et f1 = x
r

Il est clair que chaque fonction fn est holomorphe, mais n’est pas forc´ement born´ee
sur P + × Wq+1. Pour n > 1, posons

hn = − 1
nr
 ∑n−1

p=1 pan−pfp

82

alors, les coeﬃcients fn sont donn´es par

fn = Lnr(hn)

et d’apr`es (4) on obtient
 ∥hn∥∗ ≤ 1
2 max
1≤p≤n−1 ∥fp∥∗

o`u ∗ est un domaine qui d´ependra du contexte. De mˆeme, soit Fn = fn/f1 les
coeﬃcients de la s´erie de 1 + F et

Hn = − 1
(n − 1)r
 n−1∑

p=1 pan−pFp

alors, on a
 Fn = L(n−1)r(Hn)

En particulier, la fonction ´el´ementaire z(x, µ) = xLd(x, µ) est donne par

z = Lr(− 1
r )

Lemme VA2. Les germes de f et F sont des ´el´ements de SB1,q+2.

Preuve. Le domaine non-singulier de l’oprateur Lnr coincide avec Ωr. Soit θ ∈
]0, π/2[ et Sθ = {w ∈ P +; | arg(w)| ≤ θ}. Si arg(r) est suﬃsament petit, le
secteur Sθ est inclus dans Ωr. Soit u0 > 0 tel que

(10) exp(u0) ≫ tan(θ)

et w0 ∈ Sθ tel que

(11) arg(w0) = θ et arg(w0 − u0) ∼ θ

Soit S0,θ = Sθ ∩ (Sarg(w0−u0) + u0). On joint w ∈ S0,θ `a 0 par un chemin C1-rgulier
voisin du chemin γw = [0, u0] ∪ [u0, w] qui satisfait `a la condition (8) du lemme VA1
grˆace `a (10) et (11). D’o le rsultat. □

Chemins exponentiels. Pour tout u0 ≥ 1 et K ≥ 1, notons

Vu0,K = {w = u0 + u + iv ∈ P +; u ≥ 0, |v| ≤ exp(u/K) − 1}

On joint un ´el´ement w ∈ Vu0,K `a 0 par le chemin

γw = [0, u0] ∪ {z = u0 + u + iC(exp(u/K) − 1); u ∈ [0, Re(w) − u0]}

o`u C ∈ [−1, 1] est une constante qui ne d´epend que de w. Par un calcul simple, il
existe M (K) > 0 tel que pour tout u0 ≥ 1 et sur tout chemin exponentiel

(12) | z′(u)
z(u) | ≤ M (K)
 83

Lemme VA3. Le germe de f est un ´el´ement de QA
1,q+2).

Preuve. Montrons que f satisfait la condition de quasi-analycit. Remarquons
d’abord que si r est r´eel, le domaine non-singulier de l’op´erateur Lnr est P +. Les
chemins γw de V1,1 satisfont clairement `a la condition (8) du lemme VA1.

Soit ϕ0 le morphisme d’´eclatement du point (∞, 0) de P + × C dans la direction
r´eelle 0 de RP 1

(13) ϕ0 : (w, ̃µ) ↦→ µ = ̃µ
w + 1

et soit Φ0 l’application

(14) Φ0(w, y, ̃µ, ν) = (w, y, ϕ0(w, ̃µ), ν).

Soit K > 1. Si ̃W1 ∈ (C, 0) est suﬃsament petit, les projections sur [0, 1] ∪ V1,K
des ﬁbres ϕ
−1
0 (µ) de ([0, 1] ∪ V1,K) × ̃W1 contiennent les sous-ensembles

(15) ∆µ(w) = {z ∈ [0, 1] ∪ V1,K; Re(z) ≤ Re(w), |z| ≤ |w|}

qui sont inclus dans le domaine non-singulier Ωr des op´erateurs Lnr. En eﬀet, si
z ∈]0, 1], on a Re(rz) = zRe(r) > 0 et si z ∈ V1,K

Re(rz) = Re(z) + Re( ̃µ
w + 1 z) > 0

Soit u0 > 1. Les chemins γw de [0, u0] ∪ Vu0,K sont inclus dans ∆µ(w) et satisfont
`a la condition (8) du lemme VA1 si u0 est suﬃsament grand. En eﬀet, elle est
clairement satisfaite sur le segment r´eel. Sur le chemin exponentiel

rz′ = z′ + µz z′

z
et d’apr`es (12)
 | Im(rz′)
Re(rz′) | ≤ exp(u0 + u)

Soit D(0, ρ) un disque de ̃W1. Soit ̃f , ̃F et ̃f1 les relev´es par Φ0 de f , F et f1. On
a donc
 ||1 + ̃F ||Vu0 ,K ×D(0,1/2)×D(0,ρ)×Wq ≤ C0

et
 || ̃f1(w, .)||D(0,ρ) ≤ C1| exp(−w)|

par cons´equent
 || ̃f (w, .)||D(0,1/2)×D(0,ρ)×Wq ≤ C2| exp(−w)|

84

Par les formules intgrales de Cauchy sur D(0, ρ), les coeﬃcients de la srie ̃f =∑k≥0̃ck ̃µk admettent les majorations

||̃ck(w, .)||D(0,1/2)×Wq ≤ Ck| exp(−w)|

Soit maintenant f = ∑
k≥0ckµk la s´erie de f . On a ck = (w + 1)
k̃ck et donc
chaque coeﬃcient ck est born´e sur le domaine Vu0,k+1. On conclut en remarquant
que le complmentaire de ces domaines dans n’importe quel domaine de type puis-
sance, est une partie relativement compact. □

Lemme VA4. Le germe de F est un ´el´ement de QRH1,(1,q+1).

Preuve. La d´emarche est classique ([I-Y], [M], [Ro2] ) pour la partie concernant la
structure asymptotique formelle de type Hilbert. Elle utilise les formes prnormales
de ωα. Les proprits du reste dcoulent d’une deuxime application des oprateurs
intgrals de Dulac.

On pr´epare analytiquement ωα `a un certain ordre 2N > 1 par un diﬀ´eomorphisme
qui pr´eserve la coordonn´ee x

a(x, y, α) = ∑

n≥1 an(x, α)yn avec an =
 { x
ñan(α) pour n ≤ 2N

x
2N +1̃an(x, α) pour n > 2N

Soit f1,N l’int´egrale premi`ere de la forme prnormale

(16) ωα,N = xdy + y(1 + µ + ∑2N

n=1an(x, α)yn)dx

telle que f1,N (1, y, α) ≡ y. Il est connu ([I-Y] par exemple) qu’il existe F1,N ∈
QRH1,(1,q+1)
cvg telle que

f1,N = x
ry(1 + F1,N ) et F1,N (0) = 0

En eﬀet, dans le morphisme Φα(x, y) = (x1, y1) = (xy, z(x, µ)y), la 1-forme ωα,N
se d´esingularise en

̃ωα,N = (µ + ∑N

n=1̃anx
n
1 )dy1 + (1 − y1∑N

n=1̃anx
n−1
1 )dx1

et cette 1-forme admet une int´egrale premi`ere analytique g qui v´eriﬁe g(x1, 0, α) =
x1. Soit g0 = x1 + µy1 l’int´egrale premi`ere de la partie lin´eaire. Par un calcul
simple
 dg0 ∧ ̃ωα,N = g0
 N∑

n=1 ̃anx
n−1
1 dx1 ∧ dy1

et ceci montre que g est divisible par g0.

Soit Ψα(x, y) = (X, Y ) le changement de coordonn´ees ramiﬁ´e
 85

(17) { X = x

Y = y(1 + F1,N )

la fonction f1,N ´etant une int´egrale premi`ere de ωα,N , la 1-forme ramiﬁ´ee ηα =
(Ψ−1
α )
∗ωα s’´ecrit
 ηα = XdY + Y (r + (XY )
2N +1b(X, Y, α))dX

avec b ∈ QRH1,(1,q+1)
cvg . Soit f2,N l’int´egrale premi`ere de ηα telle que f2,N (1, Y, α) ≡
Y . Soit Ψ(x, y, α) = (Ψα(x, y), α). L’int´egrale premi`ere f de ωα est donn´ee par

f = f2,N ◦ Ψ

Or il est facile de voir que f2,N s’´ecrit

(18) f2,N = X rY (1 + X N HN )

On montre alors que HN = ∑
n>2N hnY n est un ´el´ement de SB1,q+2 (et mme de
QA
1,q+2), en appliquant la m´ethode des lemmes pr´ec´edents aux coeﬃcients hn par
l’interm´ediaire des op´erateurs L(n−1)r−N sur le domaine non-singulier Ω2r−1. Ceci
implique en particulier que F ∈ QA
1,q+2 (pour un bon choix de N ), et donc que
F ∈ QRH1,(1,q+1) □

3. Remarque VA1.

On peut construire des chemins sur les feuilles de ωα qui ne quittent pas un
certain voisinage de 0, par exemple D(0, 1) × D(0, 1), et qui rencontrent une seule
fois chacune des transversales {x = 1} et {y = 1}. En eﬀet, soit Y = y(1 + F ).
D’apr`es l’´etude pr´ec´edente

(19) c1|y| ≤ ||Y (., y, .)||V ×W1×Wq ≤ c2|y|

Soit y0 < c1/c2. L’intgration relle au dessus du segment [1, y0] est presque une
translation relle dans la coordonne w. Maintenant, en utilisant (19) et l’int´egrale
premi`ere x
rY de la partie lin´eaire de ωα, on montre que l’int´egration au dessus des
chemins γw ne quitte pas le voisinage D(0, 1) × D(0, 1).

B. Les thormes de division.

Ils sont bas´es sur l’algorithme de division d’Hironaka [B-M]. Rappelons quelques
r´esultats de ce travail: soit a ∈ R{α} avec α = (α1, . . . , αq). On note eL(a) le plus
petit indice m ∈ Nq de coeﬃcient non nul dans la s´erie

a = ∑

m amα
m

les ´el´ements de Nq ´etant ordonn´es par l’ordre lexicographique (L(m), m1, . . . , mq)
o`u L(m) = ∑j λjmj est une forme lin´eaire positive. Soit J un id´eal de R{α} et

86

N (J) = {eL(a); a ∈ J} son diagramme des exposants initiaux. Il existe une liste
minimale m1, . . . , ml ∈ Nq telle que

N (J) = ∪
l
i=1{mi + Nq}

On d´eﬁnit une partition de Nq par

∆1 = m1 + Nq ∆i = mi + Nq − ∪
i−1
k=1∆k et ∆ = Nq − ∪
l
i=1∆i

alors

(i) toute famille a1, . . . , al ∈ J telle que eL(ai) = mi est une base de J
(ii) tout f ∈ R{α} se divise de mani`ere unique dans J sous la forme

f =
 l∑

i=1 Qiai + R Qi, R ∈ R{α}

mi + Supp(Qi) ⊂ ∆i et Supp(R) ⊂ ∆

La partie analytique de cette algorithme fournit des estimations pr´ecises: soit L
une forme linaire positive, σ > 0 et

R{α}L,σ = {f = ∑

m fmα
m; ||f ||L,σ < ∞} avec ||f ||L,σ = ∑ |fm|σL(m)

alors il existe L et ε > 0 tels que si f ∈ R{α}L,σ et σ ≤ ε

||Qi(f )||L,σ ≤ 2
σL(mi) ||f ||L,σ et ||R(f )||L,σ ≤ 2||f ||L,σ

Soit Ω ∈ EI un domaine quasi-analytique et QA
1,q[Ω] ⊂ QA
1,q l’algbre des germes
f = ∑ fm(x)α
m dont les coeﬃcients fm admettent un prolongement holomorphe
et born´e sur Ω. Pour l’action de χ0 = x∂/∂x sur ces algbres, on a le

Thorme VB1 (thorme de de division 1). Soit B = QA
1,q[Ω] ou SB1,q et J
un id´eal de R{α}. Soit a1, . . . , al une base de J. Alors pour tout f ∈ B, il existe
de mani`ere unique Qi, R ∈ B tels que

f = ∑

i Qiai + R

mi + Supp(Qi(x, .)) ⊂ ∆i Supp(R(x, .)) ⊂ ∆

La partie formelle de cet algorithme implique le
 87

Lemme VB1. Soit f = ∑
m fmα
m ∈ B. Si pour tout m, on a fm = o(x
n) (dans
l’anneau SB1,q), alors il en est de mˆeme pour les s´eries des Qi et de R.

Soit s ∈ N∗ et soit la drivation

χ = x ∂
∂x − s
 ℓ∑

j=1 uj ∂
∂uj

Quitte eﬀectuer une ramiﬁcation en x, on peut supposer que s = 1. La drivation χ
agit sur l’anneau SB1,.(x, α, u). Soit πχ : (x, α, u) ∈ U ↦→ (α, (λj )) = (α, (xuj )) ∈
W son morphisme intgral. Les idaux χ-transverses le long de γ = {(α, u) = 0} sont
des idaux de l’anneau R{α, λ}.

Thorme VB2 (thorme de division 2). Soit J un idal de R{α, λ}. Il existe
un entier n(J) tel que pour tout f ∈ SB(x, α, u) dont l’idal χ-transverse est inclus
dans J, alors (x
n(J))Iχ,f ⊂ π∗
χ(J).

Preuve. Soit Sθ un secteur dans la coordonne x et Pε un polydisque dans les
coordonnes (α, u) tels que la srie f = ∑ cn,m(x)α
num soit convergente sur Sθ × Pε.
Soit F = ∑ x
−|m|cn,mα
nλ
m. On a π∗
χ(F ) = f et pour tout x ∈ Sθ, la srie de
F (x, .) est convergente sur le produit de polydisques Pε × Pε|x|. De plus, l’idal
χ0-transverse de F est inclus dans J. Soit (ϕj) une base de l’idal J dans l’anneau
R{α, λ}. D’aprs le thorme de division VB1

(1) F = ∑ Qjϕj

Ce thorme se gnralise facilement aux produits de polydisques: soit L(n, m) =
L1(n) + L2(m) une forme linaire positive et soit σ = (σ1, σ2) avec σi > 0. Notons

R{α, λ}L,σ = {g = ∑ gn,mα
nλ
m, ||g||L,σ = ∑ |gn,m|σL1(n)
1 σL2(m)
2 < ∞}

alors il existe L, des entiers ℓ1,j, ℓ2,j et ε0 > 0 tels que si σi < ε0

||Qj(x, .)||L,σ < 2

σℓ1,j
1 σℓ2,j
2 ||F (x, .)||L,σ

Soit n(J) = max{ℓ2,j}, on a ||x
n(J)Qj(x, .)||L,σ < cj||F (x, .)||L,σ, par consquent si
ε est suﬃsament petit, on a qj = π∗
χ(x
n(J)Qj) ∈ SB(x, α, u). On obtient le rsultat
en relevant la relation (1)
 x
n(J)f = ∑ qjπ∗
χ′ (ϕj ) □

Soit ν = (ν1, . . . , νp), ν′ = (ν′
1, . . . , ν′
p′ ), α = (µ, ν′) et α
′ = (α, ν). L’algbre
QRH(x, α
′) s’identiﬁe une sous-algbre de B = QRH(x, α){ν}. Les sries d’lments
de B sont convergentes sur un voisinage produit. Soit f = ∑ fmνm ∈ B, l’algbre
QRH(x, α) tant locale de topologie de Krull spare, on peut dﬁnir, comme dans
[B-M], un ordre sur les monmes de B: soit M l’idal maximal de QRH(x, α), l’ordre

88

e(fm) de fm est le plus grand entier e tel que fm ∈ Me. Soit L(m) = ∑ λjmj
une forme linaire positive et soit (L(m), m1, . . . , mp) l’ordre lexicographique sur les
monmes νm. Pour tout entier ℓ, l’application L′(fmνm) = (ℓe(fm), L(m), m) est
un ordre sur les monmes de B.

Soit I = ⟨g1, . . . , gq⟩ un idal de B et soit gj = ∑ gj,mνm la srie de gj. On
suppose que pour tout j, il existe un coeﬃcient gj,m d’ordre 0. Soit mj le plus
petit de ces entiers et (∆j, ∆) la partition de Np associe. On dﬁnit le support de
f ∈ B par supp(f ) = {m; fm ̸= 0}. Les algorithmes formel et analytique de
[B-M] s’adaptent I et B et on obtient

Lemme VB2. Il existe L et ℓ tels que tout f ∈ B se divise de manire unique dans
I sous la forme
 f =
 q∑

j=1 Qjgj + R Qj, R ∈ B

mj + supp(Qj) ⊂ ∆j et supp(R) ⊂ ∆

L’algbre QRH(x, α
′) est isomorphe une sous-algbre B∗ de B dﬁnie comme suit:
Soit X(x, µ) les fonctions lmentaires de QRH. Alors f ∈ B∗ si et seulement si pour
tout n, la srie τn(f ) = ∑ j
n
X (fm)νm est un lment de QRHcvg. Si I est un idal de
B∗ satisfaisant aux mmes hypothses que ci-dessus, alors

Thorme VB3 (thorme de division 3). Tout f ∈ B∗ se divise de manire unique
dans I sous la forme
 f =
 q∑

j=1 Qjgj + R Qj, R ∈ B∗

mj + supp(Qj) ⊂ ∆j et supp(R) ⊂ ∆

Preuve. D’aprs la partie formel de l’algorithme (lemme VB1), si fm = o(x
n) pour
tout m, il en est de mme des sries des Qj et de R. Soit Qj(f ) et R(f ) donns par
le lemme VB2. Par l’unicit de la division, Qj(f ) = Qj(τn(f )) + Qj(f − τn(f )) et
R(f ) = R(τn(f )) + R(f − τn(f )). Par consquent τn(Qj(f )) = τn(Qj(τn(f ))) et
τn(R(f )) = τn(R(τn(f ))). Soit l’idal In = ⟨τn(g1), . . . , τn(gq)⟩, la partition de Np

qui lui est associe est la mme que celle de I. Soit Qj,n(τn(f )) et Rn(τn(f )) donns par
le lemme VB2 appliqu In, ce sont des lments de QRHcvg d’aprs la partie analytique
de l’algorithme. Or chaque coeﬃcient de la srie de ∑ Qj,n(τn(f ))(gj − τn(gj)) est
un o(x
n), donc par l’unicit de la division, τn(Qj(τn(f ))) = j
n
X (Qj,n(τn(f ))) et
τn(R(τn(f ))) = j
n
X (Rn(τn(f ))). □

D’aprs [B-M], une consquence de ce thorme est le thorme des fonctions implicites
pour les applications rgulires dans la coordonne ν. Une autre consquence est

Thorme VB4 (thorme d’inversion). Soit f = x(1 + O(x)) ∈ QRH(x, α). Il
existe un unique g = y(1 + O(y)) ∈ QRH(y, α) qui inverse f .

Preuve. Posons f = x(1 + F ) avec F ∈ QRH. Il existe un unique inverse en
classe C1. Cherchons G ∈ QRH tel que g = y(1 + G) soit un inverse. La condition

89

f ◦ g = Id donne l’quation G + (1 + G)F (y(1 + G), α) = 0 qui est analytique en G
et rgulire d’ordre 1. Le thorme des fonctions implicites permet de conclure. □

R´ef´erences.

[B-M] Bierstone E., Milman P.D., The local geometry of analytic mappings. Dot-
torato di Ricerca in Matematica. [Doctorate in Mathematical Research]
ETS Editrice, Pisa, (1988), iv+77pp. ISBN: 88-7741-419.

[D] Dulac H., Sur les cycles limites. Bull. Soc. Math. France 51 (1923), pp.
45-188.

[Dr] Dries L.V.D., Remarks on Tarski’s problem concerning (R, +, ., exp), Logic
Colloquium ’82, G. Lolli, G. Longo and A. Marcja, eds., North-Holland
(1984), pp. 97-121.

[D-M-M] Dries L.V.D., Macintyre A. and Marker D., The elementary theory of re-
stricted analytic ﬁelds with exponentiation, Annals of Maths., 140 (1994),
pp. 183-205.

[D-S] Dries L.V.D. and P. Speissegger, The real ﬁeld with convergent generalized
power series, Trans. Amer. Math. Soc., 350 (1998), pp.4377-4421.

[E] Ecalle J., Introduction aux fonctions analysables et preuve constructive de
la conjecture de Dulac. Actualit´es Math´ematiques, Hermann (1992).

[E-M-R] El Morsalani M., Mourtada A., Roussarie R., Quasi-regularity property for
unfolding of hyperbolic polycycles. Ast´erisque 220 (1994), pp. 303-326.

[H] Herv´e M., Several complex variables, local theory. Tata Institute of Funda-
mental Research, Bombay, Oxford University Press (1963).

[Hi] Hilbert D., Mathematische probleme (lecture), the second international
congress of mathematicians, Paris 1900. Nachr. Ges. Wiss. Gottingen
Math.-Phys. Kl. (1900), p. 253-297; Mathematical developmentsarising
from Hilbert’s problems. Proceedings of Symposium in Pure Mathematics,
A.M.S., F. Browder editor, 28 (1976), pp. 50-51.

[Hir1] Hironaka H., Resolution of th singularities of an algebraic variety over a
ﬁeld of characteristic zero, I, II. Ann. of Math., 79 (1964), pp. 109-326.

[Hir2] Hironaka H., Introduction to real-analytic sets and real-analytic maps. In-
stituto Matematico ”L. Tonelli”, Pisa (1973).

[I] Il’yashenko Y. S., Limits cycles of polynomial vector ﬁelds with non degen-
erate singular points on the real plane. Func. Ana. and Appl., 18.3 (1985),
pp. 199-209.

[I-Y1] Il’yashenko Y. S., Yakovenko S., Finitely smooth normal forms for local
diﬀeomorphisms and vector ﬁelds. Rus. Math. Surveys, 46 (1991), pp.
1-43.

[I-Y2] Il’yashenko Y. S., Yakovenko S., Hilbert-Arnold problem for elementary
polycycles. In Around Hilbert’s 16th problem, Advances in Sov. Math.
(1994).

90
 [Ka] Kaloshin V., The Hilbert 16th problem and an estimate for cylicity of an
elementary polycycle, Preprint.

[K1] Khovanskii A., Fewnomials. A.M.S., Providence, RI (1991).

[K2] Khovanskii A., Real analytic varieties with the ﬁniteness property and com-
plex abelian integrals. Funct. Anal. and Appl., 18 (1984), pp. 199-207.

[L] Lojasiewicz S., Introduction to Complex Analytic Geometry, Birkhauser
(1991).

[L-R] Lion J.M. et Rolin J.P., Volumes, feuilles de Rolle de feuilletages analytiques
et thorme de Wilkie, Ann. de Toulouse 7 (1998), pp. 93-112.

[L-S] Lion J.M. and Speissegger P., Analytic stratiﬁcation in the Pfaﬃan closure
of an o-minimal structure, Duke Math. J. 103, no 2 (2000), pp. 215-231.

[M] Mourtada A., Cyclicit´e ﬁnie des polycycles hyperboliques de champs de
vecteurs du plan; algorithme de ﬁnitude. Ann. Inst. Four. tome 41, fasc.
3 (1991), pp. 719-753.

[M1] Mourtada A., Extension aux cycles singuliers du thorme de Khovanski-
Varchenko, Prprint Janvier 2007.

[M2] Mourtada A., Application de Dulac en dimension quelconque: quasi-analy-
cit, monodromie et synthse, En cours de rdaction.

[M-M] Mourtada A. et Moussu R., Applications de Dulac et applications pfaﬃ-
ennes. Bull. Soc. Math. France 125 (1997), pp. 1-13.

[Ro1] Roussarie R., A note on ﬁnite cyclicity and Hilbert’s 16th problem. Springer
Lecture Notes in Mathematics 1331 (1988), pp. 161-168.

[Ro2] Roussarie R., On the number of limit cycles which appear by perturbation
of separatrix loop of planar vector ﬁelds. Bol. Soc. Bras. Mat. 17 (1986),
pp. 67-101.

[Ru] Rudin W., Real and complex analysis. McGraw-Hill, (1966).

[S] Speissegger P., The pfaﬃan closure of an o-minimal structure, J. reine
angew. Math. 508 (1999), pp. 189-211.

[T] Tougeron J.-C.,Alg`ebres analytiques topologiquement nœth´eriennes et th´e-
orie de Khovanski. Ann. Inst. Four., tome 41, fasc. 4 (1991), pp. 823-840.

[W] Wilkie A., Model completeness results for expansions of the ordered ﬁeld of
real numbers by restricted Pfaﬃan functions and the exponential function,
J. Amer. Math. Soc. 9 (1996), pp. 1051-1094.
