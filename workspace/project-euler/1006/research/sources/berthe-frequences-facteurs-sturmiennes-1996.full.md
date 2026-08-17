<!-- source: https://www.irif.fr/~berthe/Articles/st.pdf | converted from PDF -->

Fr´equences des facteurs des suites sturmiennes

Val´erie Berth´e
Laboratoire de Math´ematiques Discr`etes
CNRS-UPR 9016
Case 930, 163 avenue de Luminy
F-13288 Marseille Cedex 9
France

R´esum´e : Dekking a explicit´e les fr´equences des facteurs de la suite de
Fibonacci en utilisant le graphe des mots. Nous g´en´eralisons ce r´esultat aux
suites sturmiennes en montrant, ´egalement par le graphe des mots, que les
fr´equences des facteurs de mˆeme longueur d’une suite sturmienne prennent au
plus 3 valeurs. Nous explicitons ces valeurs et donnons, pour chacune d’elles,
le nombre de facteurs ayant cette fr´equence en fonction du d´eveloppement en
fraction continue de l’angle α de la suite sturmienne.

1 Introduction

Les suites sturmiennes, dont la plus connue est la suite de Fibonacci, point
ﬁxe de la substitution σ d´eﬁnie par σ(a) = ab et σ(b) = a, ont de nombreuses
caract´erisations (voir, par exemple, [6] et [22]).

1. Les suites sturmiennes ont pour fonction de complexit´e p(n) = n + 1,
pour tout n. Rappelons que la fonction de complexit´e, d´eﬁnie pour une
suite `a valeurs dans un alphabet de cardinal ﬁni, compte le nombre de
facteurs de longueur donn´ee de cette suite. Or une suite dont la complexit´e
satisfait p(n) ≤ n, pour un entier n, est ultimement p´eriodique. Les suites
sturmiennes sont donc les suites de complexit´e minimale parmi les suites
non-ultimement p´eriodiques (voir [9]).

2. Les suites sturmiennes sont exactement les suites ´equilibr´ees sur un al-
phabet `a deux lettres qui sont non-ultimement p´eriodiques (voir [9], [17],
[18]). Rappelons qu’une suite ´equilibr´ee est telle que la diﬀ´erence entre
le nombre d’occurrences d’une lettre dans deux de ses facteurs de mˆeme
longueur est born´ee par 1 en valeur absolue.

3. Les suites sturmiennes sont des rotations irrationnelles : ce sont exacte-
ment les suites obtenues en codant l’orbite d’un point ρ du cercle unit´e sous

1

la rotation d’angle irrationnel α, par rapport `a des intervalles compl´ementaires
du cercle unit´e de longueur α et 1 − α (voir [17] et [18]).

4. Notons que les rotations correspondent `a des codages de trajectoires de
pente initiale irrationnelle dans un billard carr´e, o`u l’on code les cˆot´es
horizontaux par a et les cˆot´es verticaux par b (voir [19]).

5. Une seconde mani`ere “graphique” de consid´erer les suites sturmiennes
consiste `a coder le trac´e d’une demi-droite de pente irrationnelle dans le
plan euclidien muni d’un rep`ere orthonorm´e, de la mani`ere suivante (voir
[18]).

Proposition 1 Soit a une suite sturmienne. Il existe alors α irrationnel
dans ]0, 1[ et ρ tels que a = a(α, ρ) ou a(α, ρ) et o`u les suites a(α, ρ) =
(an)n∈IN (respectivement a(α, ρ) = (an)n∈IN) sont d´eﬁnies sur {a, b} de la
mani`ere suivante :

an = { a si ⌊(n + 1)α + ρ⌋ − ⌊nα + ρ⌋ = 0
b si ⌊(n + 1)α + ρ⌋ − ⌊nα + ρ⌋ = 1,

respectivement

an = { a si ⌈(n + 1)α + ρ⌉ − ⌈nα + ρ⌉ = 0
b si ⌈(n + 1)α + ρ⌉ − ⌈nα + ρ⌉ = 1.

On appelle angle (ou fr´equence, ou encore pente) d’une suite sturmienne le
r´eel α qui lui est ainsi associ´e.
La fr´equence f (B) d’un bloc B est d´eﬁnie comme la limite, si elle existe, du
nombre d’apparitions de ce bloc parmi les n premi`eres lettres de la suite, divis´e
par n. Notons que l’existence des fr´equences de blocs pour les suites sturmiennes
est assur´ee par la caract´erisation 3.

Dekking a montr´e, dans [10], que les fr´equences des facteurs de mˆeme longueur
de la suite de Fibonacci prenaient au plus 3 valeurs; il a, de plus, explicit´e
ces valeurs et donn´e, pour chacune d’elles, le nombre de facteurs ayant cette
fr´equence. Il ´etudie pour cela le graphe des mots. Le but de cet article est de
montrer, ´egalement en utilisant le graphe des mots, un r´esultat analogue pour
les suites sturmiennes. Plus pr´ecis´ement, nous montrons que les fr´equences des
facteurs de mˆeme longueur des suites sturmiennes d’angle α prennent au plus
trois valeurs, valeurs que nous explicitons en fonction du d´eveloppement en frac-
tion continue de α; nous donnons, de plus, le nombre de facteurs ayant chacune
de ces trois fr´equences.

Th´eor`eme 1 Consid´erons une suite sturmienne d’angle α. Soit m ≥ 1. Soient
p1
q1 et p2
q2 deux m-points de Farey cons´ecutifs tels que p1
q1 < α < p2
q2 .

2

Les fr´equences des facteurs de longueur m sont `a valeurs dans l’ensemble :

p2 − αq2, αq1 − p1, α(q1 − q2) + p2 − p1.

Plus pr´ecis´ement, soient ( p
(n)

q(n) ) et (c(n)) les suites des convergents et des
quotients partiels associ´ees `a α dans son d´eveloppement en fraction continue.
Supposons kq(n) + q(n−1) < m < (k + 1)q(n) + q(n−1), avec n ≥ 1 et 1 ≤ k ≤
c(n+1). Les fr´equences des facteurs de longueur m sont `a valeurs dans l’ensemble
: {(−1)
n(kp(n) + p(n−1) − α(kq(n) + q(n−1))), (−1)
n(αq(n) − p(n)),

(−1)
n(−α((k − 1)q(n) + q(n−1)) + (k − 1)p(n) + p(n−1))}.

Supposons m = kq(n) + q(n−1), avec n ≥ 1 et 1 ≤ k ≤ c(n+1). Les fr´equences
des facteurs de longueur m sont `a valeurs dans l’ensemble :

{(−1)
n(kp(n) + p(n−1) − α(kq(n) + q(n−1))), (−1)
n(αq(n) − p(n))}.

De plus, il y a

• m − q2 + 1 facteurs de fr´equence p2 − αq2;

• m − q1 + 1 facteurs de fr´equence αq1 − p1;

• (q1 + q2) − m − 1 facteurs de fr´equence α(q1 − q2) + p2 − p1.

On rappelle qu’un m-point de Farey est un ´el´ement α de [0, 1] tel que α = p
q ,
avec p ≥ 0, 1 ≤ q ≤ m et pgcd(p, q) = 1. Les points de Farey v´eriﬁent les
propri´et´es suivantes (voir [11]) :

Proposition 2 1. Si p
q , p
′′

q′′ , p
′

q′ sont trois m-points de Farey cons´ecutifs, alors

p′′

q′′ = p + p′

q + q′ .

2. Deux m-points de Farey p
q et p
′

q′ tels que m ≤ q + q′ − 1 sont cons´ecutifs
si et seulement si p′q − q′p = 1.

3. Soit m ≥ 2. Deux m-points de Farey successifs n’ont pas le mˆeme d´enominateur.

Notons que la connaissance des fr´equences de blocs d’une suite sturmienne
u permet une description pr´ecise de la mesure associ´ee au syst`eme dynamique
(O(u), T ), o`u T est le d´ecalage qui `a la suite (un)n∈IN associe la suite (un+1)n∈IN
et o`u O(u) est l’adh´erence de l’orbite sous le d´ecalage T de la suite u, dans
{a, b}IN muni du produit des topologies discr`etes. En eﬀet, on d´eﬁnit une mesure
de probabilit´e µ sur la famille B des bor´eliens de O(u), de la mani`ere suivante

3

: la mesure µ est l’unique mesure de probabilit´e invariante par T , telle que
µ([w]) = f (w), o`u [w] est le cylindre correspondant aux suites de O(u) de
pr´eﬁxe w et o`u f (w) est la fr´equence d’apparition du bloc w dans la suite u. Or
le syst`eme dynamique associ´e `a une suite sturmienne est uniquement ergodique,
c’est-`a-dire qu’il existe une unique mesure T -invariante. Par cons´equent, la
mesure µ d´eﬁnie ci-dessus est l’unique mesure T -invariante associ´ee au syst`eme
dynamique (O(u), T ).

Le th´eor`eme 1 peut ˆetre prouv´e soit en utilisant la d´eﬁnition combinatoire
(p(n) = n + 1) des suites sturmiennes, ce que nous faisons ici, soit en utilisant
leur caract´erisation dynamique (les suites sturmiennes sont des rotations irra-
tionnelles) (voir [4]). En eﬀet, on v´eriﬁe qu’`a chaque facteur B de la suite on
peut associer un intervalle I du cercle unit´e de la mani`ere suivante : l’ensemble
des entiers n tels que le facteur B apparaisse `a l’indice n de la suite correspond
`a l’ensembles des entiers tels que {αn + ρ} appartienne `a l’intervalle I, o`u α
et ρ sont associ´es `a la suite consid´er´ee selon la proposition 1. On d´eduit de
l’´equir´epartition de la suite ({αn + ρ})n∈IN que la fr´equence f (B) du facteur B
est alors ´egale `a la longueur de I. Or les (n + 1) intervalles I correspondant aux
(n + 1) blocs de longueur n sont obtenus en pla¸cant les points {−α}, {−2α},
· · · , {−nα} sur le segment [0, 1], la notation {x} d´esignant la partie fraction-
naire de x. Par cons´equent, le th´eor`eme 1 correspond `a une autre formulation
du th´eor`eme des trois distances, utilis´e en analyse diophantienne (voir [21], [23]
ou [24]) :

Th´eor`eme des trois distances Soit α un nombre irrationnel. Pla¸cons les
points {α}, {2α}, · · · , {nα} sur le segment [0, 1]. Les (n + 1) segments trouv´es
ont au plus trois longueurs, l’une ´etant la somme des deux autres.

On a bien sˆur remplac´e ici α par 1 − α.

Ce travail a ´et´e motiv´e par un article de Burrows et Sulston : ceux-ci asso-
cient, dans [8], une suite de valeurs d’entropies (Hn)n∈IN `a une suite binaire u,
aﬁn de donner une mesure du d´esordre de la suite u et ´eventuellement aﬁn de “re-
connaˆıtre” les suites quasi-cristallines (c’est-`a-dire les suites pouvant mod´eliser
un r´eseau atomique unidimensionnel quasi-cristallin) ou, plus g´en´eralement, les
suites de spectre discret. La suite (Hn) converge vers l’entropie m´etrique du
syst`eme dynamique symbolique associ´e `a la suite u et les termes Hn sont d´eﬁnis
`a partir de fr´equences conditionnelles. Nous montrons dans [5] que cette mesure
du d´esordre ne permet pas en fait de faire une classiﬁcation entre les suites selon
leurs propri´et´es spectrales.
Notons que les suites ´etudi´ees dans [5] sont des suites substitutives et que
les techniques de calcul des fr´equences employ´ees reposent sur les substitutions
sous-jacentes. Ces techniques ne peuvent donc ˆetre utilis´ees ici car les suites
sturmiennes ne sont g´en´eralement pas substitutives (voir [7], voir aussi [3]).

4

2 Le graphe des mots

L’outil utilis´e ici pour la preuve combinatoire est le graphe des mots (voir [20])
: le graphe des mots, ´egalement appel´e graphe de Rauzy est un sous-graphe du
graphe de de Bruijn.
Le graphe des mots de longueur n, associ´e `a une suite, est le graphe orient´e
Γn, dont les sommets sont les facteurs de longueur n de la suite, avec une arˆete
de U vers V si V suit U dans la suite, c’est-`a-dire, plus pr´ecis´ement, s’il existe
un mot W de longueur n − 1 tel que

U = xW et V = W y, avec x, y ∈ {a, b},

et tel que xW y soit un facteur de la suite.
Consid´erons une suite sturmienne. De la complexit´e (p(n) = n+1, pour tout
n), on d´eduit l’existence d’un unique facteur Dn de longueur n biprolongeable `a
droite, c’est-`a-dire ayant deux extensions `a droite dans la suite1. Un tel facteur
est encore appel´e facteur sp´ecial ou facteur expansif. Soit, de mˆeme, Gn l’unique
facteur de longueur n biprolongeable `a gauche. Une suite sturmienne pr´esente
deux types de graphes selon que Gn = Dn ou que Gn ̸= Dn :

✬ ✩✛

✫ ✪

✲

1

2

3
✛

Gn Dn Gn = Dn

✛

✛

✤

✣
 ✜

✢

✤

✣
 ✜

✢

1

3

Notons que Dn−1 est un suﬃxe de Dn et que Gn−1 est un pr´eﬁxe de Gn, c’est-
`a-dire que l’on peut ´ecrire Dn = xDn−1 et Gn = Gn−1y, o`u x et y appartiennent
`a {a, b}.

Soit U un sommet de Γn. On note U + le nombre d’arˆetes de Γn d’origine U
et U − le nombre d’arˆetes d’extr´emit´e U . Le lemme suivant permet de d´eduire
du graphe des mots des r´esultats sur les fr´equences.

1Notons qu’on entend g´en´eralement par extension d’un facteur B un facteur Bx, o`u x est
une lettre qui suit le bloc B dans la suite. Nous appellons ici extension par abus de langage,
la lettre x elle-mˆeme.
 5

Lemme 1 Soient U et V deux sommets reli´es par une arˆete tels que U + = 1
et V − = 1. Les facteurs U et V ont alors la mˆeme fr´equence.

En eﬀet, ´ecrivons U = xW et V = W y, o`u x et y sont des lettres. Comme
U + = 1, le facteur U a pour unique extension droite y; de mˆeme, le facteur
V a pour unique extension gauche x. Par cons´equent, nous avons les ´egalit´es
suivantes entre les fr´equences :

f (U ) = f (U y) = f (xW y) = f (xV ) = f (V ).

Par branche (1) ou (3), repr´esent´ees sur la ﬁgure ci-dessus, on entend tous les
mots de ce chemin, Dn et Gn exclus. En revanche, Dn et Gn seront inclus dans
la branche (2).
On d´eduit alors du lemme pr´ec´edent que les mots d’une mˆeme branche ont
mˆeme fr´equence. On associera donc `a une branche la fr´equence des mots de
cette branche.

3 Quelques propri´et´es des suites sturmiennes

Nous allons rappeler, dans ce paragraphe, quelques propri´et´es des suites stur-
miennes.

Lemme 2 L’ensemble des facteurs d’une suite sturmienne est stable par image
miroir. On en d´eduit, en particulier, que Gn est l’image miroir de Dn.

Par image miroir, on entend le retourn´e d’un mot. Par exemple, abaa est le
miroir de aaba.
Pour montrer ce lemme (voir par exemple [2]), il suﬃt de consid´erer la
caract´erisation 2 des suites sturmiennes comme suites ´equilibr´ees. En eﬀet, le
cardinal d’un ensemble ´equilibr´e de facteurs de longueur n sur un alphabet `a
deux lettres est au plus n + 1 (voir [9]). Un ensemble ´equilibr´e de facteurs est
tel que la diﬀ´erence entre le nombre d’occurrences d’une lettre dans deux de ses
facteurs de mˆeme longueur est born´ee par 1 en valeur absolue. Par cons´equent,
en adjoignant les images miroirs des n + 1 facteurs de longueur n d’une suite
sturmienne `a ces mˆemes facteurs, on obtient encore un ensemble ´equilibr´e de
facteurs, donc de mˆeme cardinal n + 1.

Lemme 3 Les suites sturmiennes de mˆeme angle ont mˆemes facteurs.

Ce lemme est une cons´equence directe de la minimalit´e des rotations irra-
tionnelles (caract´erisation 3) (voir [16]).

Le r´esultat suivant permet d’expliciter les facteurs expansifs (voir [2] ou [15]).

Lemme 4 Le facteur expansif de longueur m d’une suite sturmienne d’angle α
est le retourn´e du bloc a1a2 · · · am, o`u (an)n∈IN = a(α, 0).

6

En eﬀet, le bloc a1a2 · · · am a deux prolong´es `a gauche suivant que l’on consid`ere
la caract´erisation par partie enti`ere inf´erieure ou sup´erieure donn´ee dans la
proposition 1. On conclut alors grˆace aux deux lemmes pr´ec´edents.

On en d´eduit le lemme suivant ([16]).

Lemme 5 Soit m ≥ 1. Soient p1
q1 et p2
q2 deux m-points de Farey cons´ecutifs. Les
suites sturmiennes dont l’angle α v´eriﬁe α ∈ ] p1
q1 , p2
q2 [ ont mˆeme facteur expansif
de longueur m − 1.

En eﬀet, on a ⌊kα⌋ = ⌊k p1
q1 ⌋, pour 1 ≤ k ≤ m. On d´eduit donc ce r´esultat du
lemme 4.

Lemme 6 Deux suites sturmiennes ayant le mˆeme facteur expansif de longueur
m − 1 ont les mˆemes facteurs de longueur m.

On montre ce lemme par r´ecurrence. On v´eriﬁe qu’il est vrai pour m = 2. Sup-
posons que deux suites sturmiennes ayant le mˆeme facteur expansif de longueur
m−1 ont les mˆemes facteurs de longueur m. Consid´erons alors deux suites stur-
miennes ayant le mˆeme facteur expansif Dm de longueur m et par cons´equent le
mˆeme facteur biprolongeable `a gauche Gm, d’apr`es le lemme 2. En particulier,
par hypoth`ese de r´ecurrence, ces deux suites ont mˆemes facteurs de longueur
m, car elles ont le mˆeme facteur expansif de longueur m − 1. Montrons que les
facteurs de longueur m ont les mˆemes extensions dans les deux suites.
Supposons que Gm−1 ̸= Dm−1. Le facteur Dm a pour extensions a et b, dans
les deux suites. Les facteurs de longueur m diﬀ´erents de Dm ont une unique
extension droite. Or le suﬃxe de longueur m − 1 d’un facteur de longueur m
diﬀ´erent de Dm est diﬀ´erent de Dm−1, car Gm−1 ̸= Dm−1; on conclut alors en
notant que ce suﬃxe a donc une unique extension droite, qui est la mˆeme dans
les deux suites, par hypoth`ese de r´ecurrence.
Supposons maintenant que Gm−1 = Dm−1. On note Dm = xDm−1. On a,
d’apr`es le lemme 2 : Gm = Gm−1x. Notons de plus x = a, si x = b et x = b, si
x = a. Le facteur xDm−1 a pour extensions droites a et b, dans les deux suites,
par d´eﬁnition. De mˆeme, le facteur Dm−1x a pour extensions gauches a et b.
Par cons´equent, le facteur xDm−1 a pour unique extension droite x, dans les
deux suites. Le raisonnement est le mˆeme que pr´ec´edemment pour les facteurs
de longueur m restants.

On d´eduit le lemme suivant de la repr´esentation par parties enti`eres.

Lemme 7 Soit m ≥ 1. Soient p1
q1 et p2
q2 deux m-points de Farey cons´ecutifs. On
consid`ere une suite sturmienne dont l’angle α v´eriﬁe α ∈ ] p1
q1 , p2
q2 [. Supposons
p1
q1 < α < p1+p2
q1+q2 . On a alors Dq1+q2−1 = aDq1+q2−2. De mani`ere analogue, si
p1+p2
q1+q2 < α < p2
q2 , alors Dq1+q2−1 = bDq1+q2−2.

7

Preuve Montrons que l’on a ⌊(q1+q2−1)α⌋ = p1+p2−1. En eﬀet, on a d’apr`es
la proposition 2 : (p1+p2)q1−(q1+q2)p1 = 1. On en d´eduit que p1+p2−1
q1+q2−1 ≤ p1
q1 , et
donc que
p1 + p2 − 1 ≤ α(q1 + q2 − 1). On montre, de mˆeme que p2
q2 ≤ p1+p2
q1+q2−1 , ce
qui implique que (q1 + q2 − 1)α < p1 + p − 2.
Supposons p1
q1 < α < p1+p2
q1+q2 . On a donc ⌊(q1 + q2)α⌋ ≤ p1 + p2 − 1, ce qui
implique que ⌊(q1 + q2 − 1)α⌋ = ⌊(q1 + q2)α⌋. On d´eduit de la proposition 1 et du
lemme 4 que
Dq1+q2−1 = aDq1+q2−2.
On montre, de mani`ere analogue que si p1+p2
q1+q2 < α < p2
q2 alors Dq1+q2−1 =
bDq1+q2−2.

Soit m ≥ 1. Soient p1
q1 et p2
q2 deux m-points de Farey cons´ecutifs. Ces deux
m-points de Farey sont ´egalement deux (q1 + q2 − 1)-points de Farey successifs,
d’apr`es la proposition 2. Par cons´equent, les suites sturmiennes dont l’angle α
v´eriﬁe α ∈ ] p1
q1 , p2
q2 [ ont le mˆeme facteur expansif de longueur q1 + q2 − 2 (lemme
5) et donc les mˆemes facteurs de longueur q1 + q2 − 1 (lemme 6). En particulier,
le facteur Gq1+q2−2 a deux extensions, d’apr`es le lemme 7, selon la position de α
par rapport `a p1+p2
q1+q2 , ce qui implique que Gq1+q2−2 = Dq1+q2−2, ou en d’autres
termes, que Gq1+q2−2 est un palindrome. Plus g´en´eralement, la proposition
suivante donne une caract´erisation des facteurs sp´eciaux palindromes.

Proposition 3 Soit m ≥ 1. Soient p1
q1 et p2
q2 deux m-points de Farey cons´ecutifs
tels que p1
q1 ̸= 0 et p2
q2 ̸= 1. On consid`ere une suite sturmienne dont l’angle α
v´eriﬁe α ∈ ] p1
q1 , p2
q2 [. On a Gm = Dm si et seulement si m = q1 + q2 − 2.

Preuve La preuve de cette proposition repose sur les propri´et´es de bonne
approximation des points de Farey.
Notons que l’hypoth`ese p1
q1 ̸= 0 et p2
q2 ̸= 1 implique que Gq1+q2−1 n’est pas
un palindrome. En eﬀet, supposons que l’on ait Gq1+q2−1 = Dq1+q2−1. On a vu
que Gq1+q2−2 = Dq1+q2−2. On en d´eduit donc que Gq1+q2−1 est une puissance
(q1 + q2 − 1)- i`eme d’une lettre que nous noterons x, ce qui implique, d’apr`es
le lemme 7, que p1
q1 = 0 ou p2
q2 = 1. Plus pr´ecis´ement, on v´eriﬁe que x = a si
p1
q1 = 0 et que x = b, si p2
q2 = 1.
Par cons´equent, il suﬃt de montrer que l’on a Gm ̸= Dm pour max(q1, q2) ≤
m < q1 + q2 − 2. Supposons donc que Gm = Dm, avec max(q1, q2) ≤ m <
q1 + q2 − 2. On v´eriﬁe que

Dm = b1 · · · bm, o`u (bn) = a(α, 1 − {α(m + 2)}),

selon le mˆeme raisonnement que pour le lemme 4. De l’´egalit´e Gm = Dm,
on d´eduit que la diﬀ´erence ⌊αk + 1 − {α(m + 2)}⌋ − ⌊αk⌋ est constante pour
1 ≤ k ≤ m + 1. Cette diﬀ´erence vaut de plus 1 ou 0.

8

Supposons que ⌊αk + 1 − {α(m + 2)}⌋ − ⌊αk⌋ = 0, pour tout 1 ≤ k ≤ m + 1.
On a donc
 1 − {α(m + 2)} < 1 − {αk}, pour tout 1 ≤ k ≤ m + 1. (1)

Posons p = 1 + ⌊α(m + 2)⌋ et q = m + 2. Montrons que l’on a :

α < p2
q2 < p
q < p − p2
q − q2 . (2)

On v´eriﬁe ais´ement l’in´egalit´e α < p
q . Or p
q est un (q1 + q2 − 1)-point de Farey.
Les deux m-points de Farey cons´ecutifs p1
q1 et p2
q2 sont ´egalement, d’apr`es la
proposition 2.1, deux (q1 + q2 − 1)-points de Farey cons´ecutifs, puisque, par
hypoth`ese sur m, q ≤ q1 + q2 − 1. On obtient donc : p2
q2 < p
q , ce qui implique la
derni`ere in´egalit´e de (2), `a savoir p
q < p−p2
q−q2 . On en d´eduit que p − αq > p2 − αq2,
ce qui est en contradiction avec l’´equation (1), dans laquelle on a aﬀect´e `a k la
valeur q2.
Dans le cas o`u ⌊αk + 1 − {α(m + 2)}⌋ − ⌊αk⌋ = 0, pour tout 1 ≤ k ≤ m + 1,
on obtient ´egalement une contradiction en faisant intervenir q1 au lieu de q2.

Remarque Il existe de nombreuses preuves de cette proposition (voir par
exemple [4], [12] ou [14]). Hubert ([14]) prouve en particulier ce r´esultat en
exploitant ´egalement les propri´et´es de bonne approximation des points de Farey
mais en utilisant la repr´esentation 4 des suites sturmiennes, comme codages de
trajectoires dans un billard carr´e.
On peut ´egalement donner une preuve de la proposition 3 en utilisant la
caract´erisation des mots strictement bisp´eciaux donn´ee par Mignosi et de Luca
dans [12], `a partir des mots standard de Rauzy (voir [19]). En eﬀet, si on a
l’´egalit´e Dm = Gm, on v´eriﬁe que le mot Gm est alors strictement bisp´ecial,
c’est-`a-dire que les quatre extensions aGm, bGm, Gma et Gmb sont des facteurs
de suites sturmiennes. Notons que sous les hypoth`eses de la proposition 3, le
mot Gq1+q2−2 est alors un ´el´ement de P ER, en reprenant les notations de [12],
c’est-`a-dire que Gq1+q2−2 admet deux p´eriodes, q1 et q2, premi`eres entre elles,
ou en d’autres termes, que Gq1+q2−2 est un mot maximal pour le th´eor`eme de
Fine et Wilf (voir [13]).

4 Preuve du th´eor`eme 1

On consid`ere une suite sturmienne d’angle α. Soient ( p
(n)

q(n) ) et (c(n)) les suites
des convergents et des quotients partiels associ´es `a α dans son d´eveloppement
en fraction continue.
 9

Rappelons que la suite des convergents est d´eﬁnie, par r´ecurrence, de la
mani`ere suivante (voir, par exemple, [11]) :
{ p(n+1) = c(n+1)p(n) + p(n−1), p(−1) = 1, p(0) = c(0)

q(n+1) = c(n+1)q(n) + q(n−1), q(−1) = 0, q(0) = 1.

On a, de plus, pgcd(p(n), q(n)) = 1 et (α − p
(n)

q(n) ) du signe de (−1)
n. Nous
allons supposer n pair pour ﬁxer les id´ees, le raisonnement ´etant analogue si
l’on suppose n impair. On v´eriﬁe que l’on a la situation suivante :

p(n)

q(n) < α < p(n+1)

q(n+1) < kp(n) + p(n−1)

kq(n) + q(n−1) < p(n−1)

q(n−1) ,

pour 0 ≤ k ≤ c(n+1). Or les convergents p
(n)

q(n) et p
(n−1)

q(n−1) satisfont

p(n−1)q(n) − p(n)q(n−1) = 1,

ce qui implique que

(kp(n) + p(n−1))q(n) − (kq(n) + q(n−1))p(n) = 1.

On d´eduit alors de la proposition 2.2 le lemme suivant.

Lemme 8 Les points p
(n)

q(n) et kp
(n)+p
(n−1)

kq(n)+q(n−1) sont deux M -points de Farey cons´ecutifs,
pour
1 ≤ k ≤ c(n+1), avec M = kq(n) + q(n−1).

Par cons´equent, on d´eduit le th´eor`eme 1 du th´eor`eme suivant.

Th´eor`eme 2 Soit u une suite sturmienne d’angle α. Soit m ≥ 1 . Soient p1
q1
et p2
q2 deux m-points de Farey cons´ecutifs tels que p1
q1 < α < p2
q2 .
Les fr´equences des facteurs de longueur m sont `a valeurs dans l’ensemble :

p2 − αq2, αq1 − p1, α(q1 − q2) + p2 − p1.

Plus pr´ecis´ement, il y a

• m − q2 + 1 facteurs de fr´equence p2 − αq2;

• m − q1 + 1 facteurs de fr´equence αq1 − p1;

• (q1 + q2) − m − 1 facteurs de fr´equence α(q1 − q2) + p2 − p1.

La preuve de ce r´esultat se fait par r´ecurrence sur m et est bas´ee sur l’´evolution
du graphe des mots ´etudi´ee par Arnoux et Rauzy dans [1]. En eﬀet, la taille des
branches donne le nombre de facteurs correspondant `a chacune des fr´equences.
De plus, les fr´equences des branches reliant Dm `a Gm sont donn´ees par f (Dm−1a)

10

et f (Dm−1b) (si elles sont non vides), alors que la fr´equence de la branche du
milieu est donn´ee par f (Dm). On utilisera donc l’hypoth`ese suppl´ementaire de
r´ecurrence suivante (sur m) : f (Dm−1a) = p2 − αq2 et f (Dm−1b) = αq1 − p1.
On v´eriﬁe que la propri´et´e est vraie pour m = 1. En eﬀet, la lettre a a pour
fr´equence 1 − α et la lettre b a pour fr´equence α, d’apr`es la caract´erisation 3 des
suites sturmiennes comme codages de rotations et plus pr´ecis´ement, d’apr`es la
propri´et´e d’´equir´epartition de la suite ({αn + ρ})n∈IN, α ´etant irrationnel.
Supposons la prori´et´e vraie pour m ≥ 1. Montrons qu’elle est vraie pour
m + 1. Soient p1
q1 et p2
q2 deux m-points de Farey cons´ecutifs. Soit u une suite
sturmienne d’angle α tel que p1
q1 < α < p2
q2 . Nous allons distinguer trois cas
selon la position de m par rapport `a q1 + q2 − 2 : dans les deux premiers cas
(m < q1 + q2 − 2 et m = q1 + q2 − 2), p1
q1 et p2
q2 sont ´egalement deux (m+ 1)-points
de Farey cons´ecutifs alors que dans le troisi`eme cas (m = q1 + q2 − 1), p1
q1 et p2
q2
ne sont plus des (m + 1)-points de Farey cons´ecutifs (d’apr`es la proposition 2).
Notons que si p1
q1 = 0 ou si p2
q2 = 1, on ne consid`ere que le cas m = q1 + q2 − 1.
En eﬀet, on a alors m = sup(q1, q2) = q1 + q2 − 1.

• Supposons m < q1 + q2 − 2. On a donc, d’apr`es ce qui pr´ec`ede, p1
q1 ̸= 0 et
p2
q2 ̸= 1.

Par hypoth`ese de r´ecurrence, on a f (Dm−1a) = p2 − αq2 et f (Dm−1b) =
αq1 − p1. Montrons que l’on a Gm−1 ̸= Dm−1. Les (m − 1)-points de
Farey cons´ecutifs encadrant l’angle α sont, d’apr`es la proposition 2 :

• p1
q1 et p2
q2 , si m ≥ sup(q1, q2) + 1;

• p1−p2
q1−q2 et p2
q2 , si m = q1;

• p1
q1 et p2−p1
q2−q1 , si m = q2.

Dans le cas o`u les (m − 1)-points de Farey cons´ecutifs encadrant l’angle
α sont diﬀ´erents de 0 et de 1, l’in´egalit´e Gm−1 ̸= Dm−1 r´esulte de la
proposition 3. Dans le cas o`u m = q1, l’´egalit´e p1−p2
q1−q2 = 0 implique que
p1
q1 = 1
m et que p2
q2 = 1
m−1 . On a alors Dm−1 = bam−2, d’apr`es le lemme
7. Le facteur Gm−1 ´etant l’image miroir du facteur Dm−1, on a donc
Gm−1 ̸= Dm−1. De mˆeme, dans le cas o`u m = q2, l’´egalit´e p2−p1
q2−q1 = 1
implique que p1
q1 = m−2
m−1 , p2
q2 = m−1
m et que Dm−1 = abm−2. On a donc
montr´e, dans tous les cas, que Gm−1 ̸= Dm−1.

Par cons´equent, on en d´eduit que

f (Dm) = f (Dm−1) = α(q1 − q2) + p2 − p1.

On peut donc aﬀecter aux trois branches du graphe des mots de longueur
m les fr´equences correspondantes :

11

✬ ✩Dm−1a✛

✫ ✪Dm−1b

✲

p2 − αq2

α(q1 − q2) + p2 − p1

αq1 − p1
✛

Gm Dm

Γm

Les mots de la branche (1) ont pour fr´equence p2 − αq2, les mots de la
branche (2) ont pour fr´equence α(q1 − q2) + p2 − p1 et les mots de la
branche (3) ont pour fr´equence αq1 − p1.

L’´evolution du graphe des mots est la suivante :

p2 − αq2

α(q1 − q2) + p2 − p1

αq1 − p1

✬ ✩DmaxGm ✛

✫yGm ✪Dmb

✲

✛

Gm+1 = Gmz Dm+1

Γm+1

On a compl´et´e le graphe par la gauche, c’est-`a-dire qu’on a associ´e `a
chaque facteur distinct de Gm son unique extension `a gauche et `a Gm ses
deux extensions `a gauche.

Rappelons que l’hypoth`ese m < q1 +q2 −2 implique, d’apr`es la proposition
2, que p1
q1 et p2
q2 sont ´egalement deux (m + 1)-points de Farey cons´ecutifs
encadrant l’angle α.

On a, de plus, f (Dmx) = f (Dm−1x),

pour x = a ou b. En eﬀet, on a Dm−1x ̸= Gm, car Gm−1 ̸= Dm−1. On
a de mˆeme f (Dm+1) = f (Dm), car Dm ̸= Gm, d’apr`es la proposition 3.
Par cons´equent, les mˆemes fr´equences sont associ´ees aux mˆemes branches.

Il reste `a ´evaluer le nombre de facteurs ayant chacune des trois fr´equences.
Ces nombres sont donn´es par la taille des branches du graphe. Or on

12

constate que le nombre de facteurs de la branche (1) (respectivement de
la branche (3)) augmente de 1 quand on passe de Γm `a Γm+1, alors que
le nombre de facteurs de la branche (2) diminue de 1 (voir [1]).

• Supposons maintenant que m = q1 + q2 − 2, ce qui implique que p1
q1 ̸= 0
et que p2
q2 ̸= 1. On a l’´egalit´e Gm = Dm, d’apr`es la proposition 3, mais
en revanche on a Gm−1 ̸= Dm−1. En eﬀet, si q1 ̸= 2 et q2 ̸= 2 alors
m ≥ sup(q1, q2)+1, ce qui implique que p1
q1 et p2
q2 sont des (m−1)-points de
Farey cons´ecutifs. On conclut en appliquant la proposition 3. Supposons
maintenant que q1 ou q2 soit ´egal `a 2. Supposons q1 = 2 pour ﬁxer les
id´ees, le raisonnement ´etant analogue si q2 = 2. On a alors q2 > q1 = 2,
car p2
q2 ̸= 1. Par cons´equent, p1
q1 et p2−p1
q2−q1 sont deux (m− 1)-points de Farey
cons´ecutifs encadrant l’angle α. Supposons de plus que p2−p1
q2−q1 = 1. On a
alors p2
q2 = 2
3 , m = 3 et d’apr`es le lemme 7 D2 = ab ̸= G2. Supposons
maintenant p2−p1
q2−q1 ̸= 1. On a m − 1 = q2 − 1 ̸= q1 + (q2 − q1) − 2. On
conclut ici encore en appliquant la proposition 3. On a donc montr´e dans
tous les cas l’in´egalit´e Gm−1 ̸= Dm−1.

On a donc f (Dm) = f (Dm−1) = α(q1 − q2) + p2 − p1. (3)

Par hypoth`ese de r´ecurrence, les mots de la branche (1) ont pour fr´equence
p2 − αq2, les mots de la branche (2) ont pour fr´equence α(q1 − q2) + p2 − p1
et d’apr`es l’´equation (3), les mots de la branche (3) ont pour fr´equence
αq1 − p1. La branche (1) a de plus (q1 − 1) ´el´ements et la branche (3)
comporte (q2 − 1) ´el´ements, par hypoth`ese de r´ecurrence.

On constate que l’´evolution du graphe des mots d´epend de la premi`ere
lettre de Dm+1. Par cons´equent, d’apr`es le lemme 7, il faut distinguer
deux cas selon que p1
q1 < α < p1+p2
q1+q2 ou que p1+p2
q1+q2 < α < p2
q2 . Nous
supposerons ici que p1
q1 < α < p1+p2
q1+q2 , le raisonnement ´etant analogue dans
l’autre cas. On a donc : Dm+1 = aDm et Gm+1 = Gma.

L’´evolution du graphe des mots est la suivante, en compl´etant ici encore
le graphe par la gauche (voir [1]) :

La branche (1) est vide. On v´eriﬁe que la branche (2) comporte un ´el´ement
de plus que la branche (1) de Γm, `a savoir q1 ´el´ements et que la branche

13
 ✬ ✩Dm−1a ✛

✫ ✪Dm−1b
 ✲Gm = Dm
 ✛

Gm+1 = Gma Dm+1 = aDm

Γm
 DmbbGm
 Γm+1

Ø

p2 − αq2

αq1 − p1

✛

✛

✤

✣
 ✜

✢

✤

✣
 ✜

✢

(3) ( de Γm+1) comporte ´egalement un ´el´ement de plus que la branche
correspondante de Γm, c’est-`a-dire q2 ´el´ements.

On a de plus f (Dmx) = f (Dm−1x), pour x = a ou b, car Dm−1 ̸= Gm−1.
Les fr´equences des facteurs de longueur m + 1 prennent donc deux valeurs
donn´ees par
f (Dm+1) = f (Dma) pour les mots de la branche du milieu de Γm+1 et par
f (Dmb) pour les mots de la troisi`eme branche, ce qui ach`eve la r´ecurrence
dans ce cas, en rappelant que p1
q1 et p2
q2 sont deux (m + 1)-points de Farey
cons´ecutifs.

• Supposons enﬁn que m = q1 + q2 − 1. On suppose toujours que p1
q1 <
α < p1+p2
q1+q2 , c’est-`a-dire que α est compris entre les (m + 1)-points de
Farey cons´ecutifs p1
q1 et p1+p2
q1+q2 . On a donc Dm = aDm−1 et Gm = Gm−1a,
d’apr`es le lemme 7.

Si p1
q1 ̸= 0 et p2
q2 ̸= 1, on v´eriﬁe que p1
q1 et p2
q2 sont des (m − 1)-points de
Farey successifs encadrant l’angle α, ce qui implique que Gm−1 = Dm−1,
d’apr`es la proposition 3. Si p1
q1 = 0, on a alors Gm−1 = Dm−1 = am−1. De
mˆeme, si p1
q1 = 1, Gm−1 = Dm−1 = bm−1. On a donc, dans tous les cas,
l’´egalit´e Gm−1 = Dm−1.

On a f (Dmb) = f (Dm−1b) car Dm−1b = Gm−1b ̸= Gm. Par cons´equent,
on obtient que f (Dmb) = αq1 − p1.

On d´eduit, de plus, du lemme 1 que

f (Dm) = f (Gm).

Or Gm = Gm−1a = Dm−1a. En utilisant l’hypoth`ese de r´ecurrence, on
obtient donc que f (Dm) = p2 − αq2.

On en d´eduit que

f (Dma) = f (Dm) − f (Dmb) = −α(q1 + q2) + p1 + p2.

14

Il reste `a d´eterminer la troisi`eme fr´equence, si elle existe, et `a consid´erer la
longueur des branches, pour achever la r´ecurrence. Pour cela, nous allons
distinguer deux cas selon que p1
q1 = 0 ou non.

• Supposons p1
q1 ̸= 0. Montrons que l’on a Gm ̸= Dm. Si p2
q2 ̸= 1, il
suﬃt d’appliquer la proposition 7. Si p2
q2 = 1, on a alors p1
q1 = m−1
m .
Or on a suppos´e p1
q1 < α < p1+p2
q1+q2 , c’est-`a-dire m−1
m < α < m
m+1 . On
a donc Dm = abm−1 ̸= Gm, d’apr`es le lemme 7.
On en d´eduit que
 f (Dm+1) = f (Dm) = p2 − αq2.

On constate de plus que l’´evolution de la taille des branches du graphe
des mots est analogue `a celle du premier cas (m < q1 + q2 − 2),
puisque Gm ̸= Dm. Plus pr´ecis´ement, le nombre de facteurs de la
branche (1) (respectivement de la branche (3)) augmente de 1 quand
on passe de Γm `a Γm+1, alors que le nombre de facteurs de la branche
(2) diminue de 1. Par cons´equent, parmi les q1 + q2 + 1 facteurs de
longueur q1 + q2, il y a 1 (c’est-`a-dire m + 1 − (q1 + q2) + 1) facteur
de fr´equence −α(q1 + q2) + p1 + p2 (branche 1), q1 − 1 (c’est-`a-dire
2q1 + q2 − (m + 1) − 1) facteurs de fr´equence p2 − αq2 (branche 2)
et q2 + 1 (c’est-`a-dire m + 1 − q1 + 1) facteurs de fr´equence αq1 − p1
(branche 3).

• Supposons que p1
q1 = 0. On a donc p2
q2 = 1
m , c’est-`a-dire m = q2. On
a de plus Dm+1 = Gm+1 = am+1.

Par cons´equent, on obtient

f (Dm+1) = f (Dma) = 1 − α(q2 + 1).

On v´eriﬁe alors que seul Dm+1 a pour fr´equence 1 − α(q2 + 1) et que
les q2 facteurs de longueur q2 + 1 restant ont pour fr´equence α.

Remarques

• On constate que l’´evolution de la forme du graphe des mots est gou-
vern´ee par la place de α par rapport aux (q1 + q2)-points de Farey p1
q1 ,
p1+p2
q1+q2 et p2
q2 . En eﬀet, on en d´eduit la lettre qui prolonge Dq1+q2−2
dans Dq1+q2−1 (lemme 7), ce qui d´etermine, en particulier, quelle est
la branche qui des branches (1) ou (3) de Γq1+q2−2 se transforme en
branche du milieu pour Γq1+q2−1. En particulier, on peut d´emontrer le
th´eor`eme 1 sans utiliser la proposition 3 en ajoutant quelques hypoth`eses
de r´ecurrence suppl´ementaires. Par souci de clart´e, nous avons pr´ef´er´e
d´emontrer s´epar´ement la proposition 3.

15

• De nouvelles fr´equences n’apparaissent quand on passe des mots de longueur
n aux mots de longueur n + 1, que lorsque Gn−1 = Dn−1, dans le cas o`u
p1
q1 ̸= 0 et p2
q2 ̸= 1. Le processus est alors le suivant : on soustrait `a la
plus grande des fr´equences des branches (1) et (3), la plus petite des ces
fr´equences, qui est une “mesure d’approximation” de l’angle α; il s’agit de
l’algorithme des fractions continues.

• Arnoux et Rauzy ont ´egalement ´etudi´e dans [1] les suites de complexit´e
2n + 1, telles qu’il existe, pour tout n, un unique facteur de longueur
n ayant trois prolongements `a droite, not´e Dn, et un unique facteur de
longueur n ayant trois prolongements `a gauche, not´e Gn. Arnoux et Rauzy
montrent qu’une telle suite peut se repr´esenter g´eom´etriquement comme
un ´echange de six intervalles sur le cercle unit´e. Cet ´echange est unique-
ment ergodique. Par cons´equent, les fr´equences de blocs existent pour une
telle suite. La m´ethode utilis´ee ici se g´en´eralise facilement. En eﬀet, le
graphe des mots admet alors quatre branches, trois branches allant de Dn
`a Gn et une branche allant de Gn `a Dn. On montre en particulier qu’il
existe, pour les facteurs de longueur donn´ee, au plus quatre fr´equences
dont l’une est la somme des trois autres.

Remerciements Je remercie J.-P. Allouche, J. Berstel et P. Liardet pour
leurs pr´ecieux conseils ainsi que P. Hubert pour de nombreuses discussions. Je
remercie ´egalement J.-M. Dumont qui m’a indiqu´e la r´ef´erence [21]. Enﬁn, je
remercie le rapporteur de cet article pour ses commentaires judicieux.

R´ef´erences

[1] P. ARNOUX et G. RAUZY Repr´esentation g´eom´etrique de suites de com-
plexit´e 2n + 1, Bull. Soc. math. France 119 (1991), 199–215.

[2] J. BERSTEL Mots de Fibonacci, S´eminaire d’Informatique Th´eorique,
LITP, Universit´es Paris 6-7 (1980-81), 57–78.

[3] J. BERSTEL et P. S´E´EBOLD Morphismes de Sturm, Bull. Belg. Math.
Soc. 1 (1994), 175–189.

[4] V. BERTH´E Fonctions de Carlitz et automates. Entropies conditionnelles,
Th`ese, Univ. Bordeaux I (1994).

[5] V. BERTH´E Conditional entropy of some automatic sequences, J. Phys. A:
Math. Gen. 27 (1994) 7993–8006.

[6] T. C. BROWN Descriptions of the characteristic sequence of an irrational,
Canad. Math. Bull. 36 (1993), 15–21.

16

[7] D. CRISP, W. MORAN, A. POLLINGTON et P. SHIUE Substitution in-
variant cutting sequences, Journal de Th´eorie des Nombres de Bordeaux 5
(1993), 123–137.

[8] B. L. BURROWS et K. W. SULSTON Measures of disorder in non-periodic
sequences, J. Phys. A: Math. Gen. 24 (1991), 3979–3987.

[9] E. M. COVEN et G. A. HEDLUND Sequences with minimal block growth,
Math. Systems Theory 7 (1973), 138–153.

[10] F. M. DEKKING On the Prouhet-Thue-Morse Measure, Acta Universitatis
Carolinae, Mathematica et Physica, 33 (1992), 35–40.

[11] G. H. HARDY et E. M. WRIGHT An introduction to the theory of numbers,
Oxford Science Publications (1979).

[12] A. DE LUCA et F. MIGNOSI Some combinatorial properties of Sturmian
words, Theoret. Comput. Sci., `a paraˆıtre.

[13] N. J. FINE et H. S. WILF Uniquenes theorems for periodic functions, Proc.
Amer. Math. Soc. 16 (1965), 109–114.

[14] P. HUBERT Communication priv´ee.

[15] F. MIGNOSI Inﬁnite words with linear subword complexity, Theoret. Com-
put. Sci. 65 (1989), 221–242.

[16] F. MIGNOSI On the number of factors of Sturmian words, Theoret. Com-
put. Sci. 82 (1991), 71–84.

[17] M. MORSE et G. A. HEDLUND Symbolic dynamics, Amer. J. Math. 60
(1938), 815–866.

[18] M. MORSE et G. A. HEDLUND Symbolic dynamics II: Sturmian trajec-
tories, Amer. J. Math. 62 (1940), 1–42.

[19] G. RAUZY Mots inﬁnis en arithm´etique, dans : M. Nivat et D. Perrin,
eds., Automata on Inﬁnite Words, Lecture Notes in Computer Science 192
(1985), 165–171.

[20] G. RAUZY Suites `a termes dans un alphabet ﬁni, S´em. de Th´eorie des
Nombres de Bordeaux (1983), 25-01–25-16.

[21] N. B. SLATER Gaps and steps for the sequence nθ mod 1, Proc. Cambridge
Phil. Soc. 63 (1967), 1115–1123.

[22] K. B. STOLARSKY Beatty sequences, continued fractions, and certain shift
operators Canad. Math. Bull. 19 (1976), 473–482.

17

[23] V. T. S ´OS On the distribution mod 1 of the sequence nα, Ann. Univ. Sci.
Budapest E˝otv˝os Sect. Math. 1 (1958), 127–134.

[24] S. ´SWIERCZKOWSKI On successive settings of an arc on the circumfer-
ence of a circle, Fund. Math. 46 (1958), 187–189.

18
