<!-- source: https://emis.muni.cz/journals/BBMS/Bulletin/bul971/cassaigne.pdf | converted from PDF -->

Complexit ´e et facteurs sp ´eciaux

Julien Cassaigne

R´esum´e
Dans l’ensemble des facteurs d’une suite inﬁnie `a valeurs dans un ensemble
ﬁni, certains ´el´ements jouent un rˆole particulier : les facteurs sp´eciaux et bi-
sp´eciaux. Nous montrons comment ils peuvent servir `acalculer lacomplexit´e
de suites, c’est-`a-dire le nombre de facteurs de longueur donn´ee, et `aprouver
que certaines fonctions peuvent ˆetre obtenues comme complexit´es de suites
alors que d’autres ne le peuvent pas.

Abstract

Among the factors of an inﬁnite sequence on a ﬁnite alphabet, some ele-
ments have a particular importance: special and bispecial factors. We show
how they can be used to compute the complexity of sequences, i.e. the num-
ber of factors with a given length, and to prove that certain functions are
obtainable as sequence complexity whereas other functions are not.

1 Introduction

Pour appr´ecier la structure d’une suite u =(un)n∈N de symboles d’un alphabet
ﬁni Σ, et en particulier pour mesurer la diversit´e des motifs qui apparaissent dans
cette suite, on peut utiliser la fonction de complexit´e de la suite, qui est une fonction
de N dans N, habituellement not´ee pu ou simplement p,qui `atout entier n associe
le nombre de facteurs de longueur n de u,c’est-`a-dire le nombre de mots w ∈ Σ
n

tels que w = ukuk+1 ... uk+n−1 pour un certain entier k.
Ainsi, la suite la plus simple possible, la suite constante aω avec a ∈ Σ, a pour
complexit´e la fonction constante p(n) = 1, alors qu’une suite al´eatoire a presque

Received by the editors May 95.
Communicated by M. Boﬀa.
1991 Mathematics Subject Classiﬁcation : 68R15, 11B85.
Key words and phrases : Subword complexity, special factors, substitutive sequences.

Bull. Belg. Math. Soc. 4 (1997), 67–88

68 J. Cassaigne

sˆurement pour complexit´e p(n)=(#Σ)n,o`u#Σ d´esigne le cardinal de l’alphabet
Σ. Entre ces deux extrˆemes, on trouve par exemple les suites ultimement p´eriodiques,
dont la complexit´eest born´ee, les suites sturmiennes, de complexit´e p(n)= n+1, les
suites automatiques, pour lesquelles p(n)= O (n), et les suites substitutives, dont
la complexit´e peut atteindre O (n
2). Dans son survol [2], Allouche cite de nombreux
autres exemples de suites ou de familles de suites dont on connaˆıt la complexit´e.
Dans cet article, nous pr´esentons un outil qui permet d’obtenir un certain nombre
de r´esultats int´eressants sur la complexit´e des suites : les facteurs sp´eciaux,qui
sont lesfacteursde la suite qui peuvent ˆetre prolong´es de plusieurs mani`eres, et
les facteurs bisp´eciaux qui sont sp´eciaux dans les deux directions `a la fois. Il se
trouve que les nombres de facteurs sp´eciaux et bisp´eciaux sont reli´es aux diﬀ´erences
premi`ere et seconde de la fonction de complexit´e. Dans le cas, qui est celui d’un grand
nombre de suites classiques, o`ula complexit´e est suﬃsamment basse, le nombre de
facteurs bisp´eciaux est tr`es faible et il est souvent ais´ede l’´evaluer, et d’obtenir ainsi
la complexit´e beaucoup plus facilement qu’avec un calcul direct. Nous montrons
notamment comment cette technique s’applique aux suites substitutives d´eﬁnies par
un morphisme circulaire.
Nous envisageons ´egalement un autre point de vue sur la complexit´e des suites :
trouver quelles fonctions peuvent ˆetre des fonctions de complexit´e. On se rend ra-
pidement compte en eﬀet que ce n’est pas le cas de n’importe quelle fonction, et
que les quelques conditions n´ecessaires naturelles (p est une fonction croissante
et 1 ⩽ p(n) ⩽ (#Σ)n, par exemple) sont loin d’ˆetre suﬃsantes. En particulier,
un r´esultat classique [10] dit que les fonctions de complexit´enon born´ees sont
sup´erieures `a n + 1 : une fonction qui croˆıt comme √
n par exemple n’est donc cer-
tainement pas une fonction de complexit´e. Une autre zone interdite, moins connue,
se trouve `a l’autre extr´emit´e du spectre : si p(n)n’est pas (#Σ)n pour tout n,alors
p(n)= O (α
n)avec α< #Σ, `a cause de la relation p(m + n) ⩽ p(m)p(n), va-
lable quels que soient les entiers m et n. Une fonction telle que (#Σ)n/ log n n’est
donc pas une fonction de complexit´e. L’utilisation des facteurs sp´eciaux nous permet
d’approcher des deux cˆot´es la fronti`ere des fonctions de complexit´e : d’une part nous
construisons des familles de suites qui permettent de prouver que certaines fonctions
sont r´ealis´ees, et d’autre part nous donnons une condition n´ecessaire plus ﬁne qui
limite les variations de p(n +1) − p(n) quand p(n)croˆıt lentement.

2 Suites et langages

2.1 Complexit ´e d'un langage factoriel

La complexit´e d’une suite est en fait un cas particulier de la complexit´ed’un
langage : ´etant donn´e un langage L ⊂ Σ
∗, la fonction de complexit´ede L est la
fonction pL d´eﬁnie par pL(n)= #(L ∩ Σ
n). La complexit´ede la suite u n’est autre
que la complexit´e du langage F (u)form´e de tous les facteurs de u.
Il n’y a pas grand chose de g´en´eral `a dire sur les complexit´es de langages ar-
bitraires : n’importe quelle fonction restant dans les bornes 0 ⩽ p(n) ⩽ (#Σ)n

peut ˆetre obtenue. Il faut donc se restreindre `a une classe donn´ee de langages, par
exemple les familles classiques : langages rationnels, langages alg´ebriques, etc. Nous

Complexit´eet facteurs sp´eciaux 69

nous int´eresserons ici exclusivement `a la classe des langages factoriels, dont font
partie tous les langages de facteurs de suites F (u) : un langage L est dit factoriel si
tout facteur d’un ´el´ement de L est ´egalement ´el´ement de L.
Toutefois, la plupart des langages factoriels ne sont pas de la forme F (u), et leur
complexit´e n’est pas toujours la complexit´e d’une suite. En particulier, pL n’est pas
n´ecessairement une fonction croissante, alors que pu l’est toujours : c’est par exemple
le cas du langage des mots sans chevauchements sur l’alphabet {a, b} [5, 6]. La raison
de cette diﬀ´erence est assez simple : dans le langage des mots sans chevauchements,
il existe des mots non prolongeables `adroite, par exemple abbabb qui ne peut ˆetre
prolong´eni par a ni par b sans faire apparaˆıtre un chevauchement (abbabba ou bbb).
Cela ne se produit jamais avec les facteurs d’une suite, qui peuvent toujours ˆetre
prolong´es d’une mani`ere au moins.

2.2 Le probl `eme des suites non r ´ecurrentes

Un avantage des langages factoriels sur les suites est que les propri´et´es des pre-
miers sont ind´ependantes du sens de lecture des mots. Les suites par contre sont
dissym´etriques (pour ´eviter cela il faudrait consid´erer des suites biinﬁnies, c’est-`a-
dire index´ees par Z), et en particulier la propri´et´e de prolongeabilit´e`adroite ´enonc´ee
ci-dessus n’est pas vraie `a gauche : il peut exister des pr´eﬁxes de u dont aucun pro-
longement n’est facteur de u. Les suites pour lesquelles cela ne se produit pas sont
dites r´ecurrentes, et la plupart des suites classiques en font partie.
En pratique, nous travaillerons soit avec des langages factoriels dont tous les
´el´ements sont prolongeables `adroite et `a gauche (appel´es langages factoriels prolon-
geables), soit avec des suites r´ecurrentes, dont les langages de facteurs sont toujours
factoriels prolongeables. Nous pourrons ainsi traiter de mani`ere sym´etrique les deux
extr´emit´es des mots.
Pour calculer la complexit´e d’une suite non r´ecurrente u surunalphabetΣ, il
suﬃra d’ajouter `a l’alphabet Σ une nouvelle lettre z et d’´etudier le langage

L = F (u) ∪{ znw | n ∈ N et w pr´eﬁxe de u }

(qui est l’ensemble des facteurs de la suite biinﬁnie ωzu, et donc factoriel et prolon-
geable). Il sera ensuite facile de passer `a u au moyen de la relation

pL(n)= pu(n)+ n.

3 Facteurs sp ´eciaux et bisp ´eciaux

Dans toute cette section, L est un langage factoriel prolongeable sur l’alphabet
Σ. On suppose pour le moment que Σ n’a que deux ´el´ements : Σ = {a, b}.

3.1 Arbres et graphes de facteurs

3.1.1 L'arbre des facteurs `adroite

Il est commode de repr´esenter le langage L sous forme d’un arbre, appel´e arbre
des facteurs `adroite de L (on d´eﬁnit ´egalement l’arbre des facteurs `a gauche). C’est

70 J. Cassaigne

un arbre inﬁni dont les sommets sont ´etiquet´es par les ´el´ements de L et les arˆetes
par les lettres, de sorte qu’il y a une arˆete d’´etiquette x entre les sommets u et v si
et seulement si v = ux.On le repr´esente conventionnellement en pla¸cant la racine,
´etiquet´ee par le mot vide, `a gauche, si bien que quand on lit de la gauche vers la
droite les ´etiquettes du chemin entre la racine et le sommet ´etiquet´e u on retrouve le
mot u ; on peut alors se contenter d’indiquer les ´etiquettes des arˆetes, ou la derni`ere
lettre des ´etiquettes de sommet. Par exemple, l’arbre des facteurs `a droitedela suite
de Fibonacci
 f = abaababaabaababaababaabaababaabaababaaba . . .

(point ﬁxe de la substitution qui transforme a en ab et b en a)est repr´esent´esur la
ﬁgure 1.
 ε
 a
 a

a
 a

a
 a

a

a
b
 b
 b

b
 b

b
 a

b

b

a

a

a
 b

a

a

a

a
b

b
 a

a

a
b

b

b
a

a
 b

b

b

b

a

a

a
a
a
 a

a

a
a
a
b
b
b
b
a
 a

b
b
b
b
a
a
a
a
a

a ···

···
···
···

···
···

···
···
···
···
···

Fig. 1– Arbre `a droite des facteurs de la suite de Fibonacci

La complexit´e p(n) est clairement le nombre de sommets de l’arbre situ´es `a l’ab-
cisse n. Comme le langage L est prolongeable, toutes les branches de l’arbre sont
inﬁnies, et la complexit´e ne peut donc qu’augmenter quand n croˆıt. Cela se produit
chaque fois que l’arbre comporte un embranchement, et s’il y a k embranchements
`a l’abcisse n on a pr´ecis´ement p(n +1) = p(n)+ k. Autrement dit, le nombre d’em-
branchements `a l’abcisse n est la diﬀ´erence premi`ere de la complexit´e. Ce sont les
´etiquettes de ces embranchements que nous nommerons facteurs sp´eciaux `adroite.
Dans l’exemple de la suite de Fibonacci (et pour les suites sturmiennes en g´en´eral)
p(n)= n + 1 donc p(n +1) − p(n) = 1 pour tout n : il y a exactement un embran-
chement `a chaque abcisse.

3.1.2 Graphes de Rauzy

Une autre repr´esentation agr´eable de L utilise non plus un arbre inﬁni mais une
famille de graphes ﬁnis. Pour tout entier n,le graphe de Rauzy d’ordre n de L est le
graphe ﬁni dont les sommets sont ´etiquet´es par les mots de L de longueur n et les
arˆetes par les mots de L de longueur n + 1, l’arˆete ´etiquet´ee w joignant le sommet
´etiquet´epar le pr´eﬁxe de longueur n de w `a celui ´etiquet´e par son suﬃxe de longueur
n. Les premiers graphes pour la suite de Fibonacci sont repr´esent´es sur la ﬁgure 2.
`A cause de la prolongeabilit´ede L, tout sommet a au moins une arˆete entrante et
une arˆete sortante. Ceux qui ont deux arˆetes sortantes sont pr´ecis´ement les mots qui

Complexit´eet facteurs sp´eciaux 71

baab
 aaba

abaa baba

abab

n =4

aab

baa
 aba bab

n =3

ε

n =0
 ab

n =1
 aa
 ab

ba
n =2

aabaab

baabaa
 abaaba
 baabab

babaab
 aababa

ababaa

n =6

aabaa
 baaba

abaab
 aabab
 ababa

babaa

n =5

sp´eciaux `a gauche sp´eciaux `a droite bisp´eciaux

Fig. 2 – Graphes de Rauzy d’ordre 0 `a 6 de la suite de Fibonacci

´etiquetaient les embranchements `a l’abcisse n dans l’arbre des facteurs `a droite, les
facteurs sp´eciaux `adroite.De mˆeme, nous appellerons facteurs sp´eciaux `agauche
les ´etiquettes des sommets o`u arrivent deux arˆetes. Quand ces facteurs sp´eciaux
sont peu nombreux, il est parfois possible de d´ecrire explicitement la structure des
graphes de Rauzy [3, 13], ce qui en fait un outil tr`es eﬃcace pour ´etudier les suites
de faible complexit´e.

3.2 Facteurs sp ´eciaux

Formellement, un mot u ∈ L est dit sp´ecial `adroite pour L si les mots ua et ub
sont tous deux dans L, sp´ecial `agauche si au et bu sont dans L.

Proposition 3.1 Soit L un langage factoriel prolongeable sur un alphabet binaire.
Le langage L poss`ede le mˆeme nombre de facteurs sp´eciaux de longueur n `agauche
ou `a droite, et nous noterons ce nombre s(n).Il v´eriﬁe

s(n)= p(n +1) − p(n) .

Preuve. Soit sd(n) le nombredefacteurs sp´eciaux `a droite de longueur n.Parmi les
p(n) facteurs de longueur n,ilya sd(n) facteurs qui se prolongent de deux mani`eres `a

72 J. Cassaigne

droite, et les autres p(n) − sd(n) facteurs ne se prolongent que d’une seule mani`ere.
On obtient ainsi une fois et une seule tous les facteurs de longueur n +1, donc
p(n +1) = 2sd(n)+(p(n) − sd(n)), d’o`ula relation sd(n)= p(n +1) − p(n). On
d´emontre de mˆeme que sg(n)= p(n +1) − p(n), o`u sg(n) est le nombre de facteurs
sp´eciaux `a gauche, et on en d´eduit que sd(n)= sg(n).

Une cons´equence imm´ediate de cette proposition est que la complexit´e du langage
L est une fonction croissante.

3.3 Facteurs bisp ´eciaux

Lorsqu’un facteur u est sp´ecial `ala fois `a gauche et `a droite, on dit qu’il est
bisp´ecial. Trois cas peuvent se pr´esenter, selon le nombre d’´el´ements de L ∩ ΣuΣ: si
cet ensemble a quatre ´el´ements (le maximum), on dit que u est bisp´ecial strict. S’il
n’en a que trois, u est bisp´ecial ordinaire. Enﬁn, il est possible que cet ensemble ait
deux ´el´ements ({aua, bub} ou {aub, bua}) et on dit dans ce cas que u est bisp´ecial
faible.
Quand on prolonge `a droite un facteur sp´ecial `a gauche u, on obtient un ou deux
facteurs qui peuvent ˆetre sp´eciaux `a gauche ou non, en fonction de la nature de u :
– aucun n’est sp´ecial `a gauche si u est bisp´ecial faible ;
– un seul est sp´ecial `a gauche si u est non bisp´ecial ou bisp´ecial ordinaire ;
– les deux sont sp´eciaux `a gauche si u est bisp´ecial strict.
R´eciproquement, un pr´eﬁxe de facteur sp´ecial `a gauche est sp´ecial `a gauche,
donc on peut construire l’arbre des facteurs sp´eciaux `agauche,qui est un sous-
arbre de l’arbre des facteurs `a droite, dans lequel on ne garde que les sommets dont
les ´etiquettes sont sp´eciales `a gauche. Dans cet arbre, un embranchement indique un
bisp´ecial strict et une feuille indique un bisp´ecial faible. Cet arbre est souvent plus
facile `ad´ecrire que l’arbre de tous les facteurs, le cas extrˆeme ´etant celui des suites
sturmiennes pour lesquelles il est ﬁliforme. On peut bien entendu aussi construire
l’arbre des facteurs sp´eciaux `a droite, qui est orient´e vers la gauche. Pour bien
indiquer qu’il s’agit de facteurs sp´eciaux, on indique `a la racine les deux lettres a et
b par lesquelles les facteurs sp´eciaux peuvent se prolonger (ﬁgures 3 et 4).

··· ba ba a b a a ba ba a b a ε a
b

Fig. 3 – Arbre des facteurs sp´eciaux `a droite pour la suite de Fibonacci

Les diﬀ´erents types de facteurs bisp´eciaux interviennent ´egalement lors de l’ex-
pansion des graphes de Rauzy : pour passer du graphe des facteurs de longueur n
`a celui des facteurs de longueur n + 1, on remplace chaque arˆete par un sommet et
chaque sommet par une, deux, trois ou quatre arˆetes selon que le mot qui ´etiquette ce
sommet est non sp´ecial, sp´ecial non bisp´ecial ou bisp´ecial faible, bisp´ecial ordinaire,
bisp´ecial strict (cf. ﬁgure 5). En particulier, si aucun facteur de longueur n n’est
bisp´ecial, il n’y a qu’une expansion possible.

Complexit´eet facteurs sp´eciaux 73

bisp´eciaux faiblesbisp´eciaux stricts

···

···

···

··· a

b
 a

b
 b

a
 b

a
 a

b
 b

a
 a

b
 a

b

a b aa b a b b aa b b a b aa b

b a bb a b a a bb a a b a bb a ε a

b

Fig. 4 – Arbre des facteurs sp´eciaux `a droite pour la suite de Thue-Morse

rang n

rang n +1
 bisp. strictbisp. ordinairebisp. faiblesp. `a gauchesp. `adroitenon sp´ecial
 Fig. 5 – Expansion des graphes de Rauzy

Proposition 3.2 Soit L un langage factoriel prolongeable sur un alphabet binaire,
et s, bs et bf les fonctions comptant les facteurs sp´eciaux, bisp´eciaux stricts, et
bisp´eciaux faibles de L. On a alors

bs(n) − bf(n)= s(n +1) − s(n) .

Preuve. Voir la construction des arbres de facteurs sp´eciaux ci-dessus.

Pour calculer p(n), il est donc suﬃsant de connaˆıtre bs(n)et bf(n) et d’appliquer
les propositions 3.2 puis 3.1.
On peut ´egalement utiliser des s´eries g´en´eratrices : `ala fonction p on associe
la s´erie P (X)= ∞∑

n=0 p(n)X n,et de mˆeme les s´eries S(X), BS(X)et BF (X)sont

associ´ees `a s, bs et bf. Les relations entre ces s´eries sont r´esum´ees dans la proposi-
tion 3.3.

Proposition 3.3 Soit L un langage factoriel prolongeable sur un alphabet binaire,
et P , S, BS et BF les s´eries g´en´eratrices des fonctions p, s, bs et bf associ´ees `a
L. On suppose de plus que p(1) = 2.Alors

P (X)= 1
1 − X (1 + XS(X))

et S(X)= 1
1 − X (1 + X(BS(X) − BF (X)))

soit P (X)= 1
(1 − X)2
 (1+ X 2(BS(X) − BF (X))) .

74 J. Cassaigne

Preuve. Il suﬃt de sommer les relations des propositions 3.1 et 3.2. L’hypoth`ese
p(1) = 2, qui dit que les deux lettres de l’alphabet sont eﬀectivement utilis´ees,
assure que le mot vide est un facteur sp´ecial et donc que s(0) = 1.

3.4 Le cas des alphabets plus grands

Quand l’alphabet Σ a plus de deux ´el´ements, la situation se complique quelque
peu, surtout en ce qui concerne les facteurs bisp´eciaux, car un mot peut ˆetre pro-
longeable par plusieurs lettres de l’alphabet sans l’ˆetre par toutes. Supposons donc
que Σ a k ´el´ements.
Soit u un ´el´ement quelconque de L.On d´eﬁnit l’ordre `adroite de u,not´e md(u),
par md(u)=# { x ∈ Σ | ux ∈ L }− 1 ,

de sorte que md(u) est un entier compris entre 0 et k − 1. Un ´el´ement de L sera
dit sp´ecial `adroite si son ordre `a droite est non nul. On d´eﬁnit de mˆeme l’ordre `a
gauche mg(u)etles ´el´ements sp´eciaux `a gauche. Cette d´eﬁnition est bien compatible
avec celle donn´ee plus haut dans le cas k = 2 ; mais alors que sur l’alphabet binaire
lesfacteurssp´eciaux sont tous d’ordre (`adroite ou `a gauche) 1, si l’alphabet est plus
grand ils n’ont pas n´ecessairement tous le mˆeme ordre.
Comme avec un alphabet binaire, les facteurs sp´eciaux correspondent `a des em-
branchements dans les arbres de facteurs et les graphes de Rauzy. Le nombre de
branches est ´egal `a l’ordre du facteur sp´ecial, augment´e d’une unit´e.

Proposition 3.4 Soit L un langage factoriel prolongeable. Alors

∑

u∈L∩Σn md(u)= ∑

u∈L∩Σn mg(u)= p(n +1) − p(n) .

Cette quantit´esera not´ee s(n).

Preuve. Puisque md(u) + 1 compte les mots de longueur |u| +1 de L commen¸cant
par u, la somme ∑

u∈L∩Σn (md(u)+1)

compte donc tous les mots de longueur n +1 de L et vaut donc p(n +1), et de mˆeme
avec les ordres `a gauche, ce qui donne les ´egalit´es annonc´ees.

Le nombre s(n)peut encore ˆetre consid´er´e comme le nombre de facteurs sp´eciaux
`adroite (ou `a gauche) de L `a condition de compter m fois un facteur dont l’ordre
`adroite est m. Aussi, nous l’appellerons parfois, par abus de langage, nombre de
facteurs sp´eciaux de L, en sous-entendant que ceux-ci doivent ˆetre compt´es avec
multiplicit´e.
Un facteur u sp´ecial `adroite et `a gauche est encore dit bisp´ecial. Notons que les
ordres `adroite et `a gauche d’un facteur bisp´ecial sont tous les deux non nuls mais
n’ont aucune raison d’ˆetre ´egaux. Nous allons encore classer les facteurs bisp´eciaux
en fonction du nombre d’´el´ements de l’ensemble L ∩ ΣuΣ. Celui-ci vaut au plus
(md(u)+1)(mg(u) + 1), et si c’est le cas on dit que u est bisp´ecial strict ;ilvaut au
moins max(md(u),mg(u)) + 1, car chaque prolongement de u `adroite ou `a gauche

Complexit´eet facteurs sp´eciaux 75

donne au moins un ´el´ement de L ∩ ΣuΣ : c’est le cas que nous avons appel´e bisp´ecial
faible pour un alphabet binaire. Mais cette fois tous les interm´ediaires sont possibles
entre ces deux extrˆemes : on peut quantiﬁer cela au moyen d’un troisi`eme entier
m(u), l’ordre bilat`ere du facteur bisp´ecial, d´eﬁni ainsi :

m(u)= # (L ∩ ΣuΣ) − md(u) − mg(u) − 1 .

C’est un entier relatif, compris entre − min(md(u),mg(u)) et md(u)mg(u), donc entre
−(k − 1) et (k − 1)
2 ;si k = 2, on retrouve les trois cat´egories de facteurs bisp´eciaux,
qui correspondent aux trois ordres (bilat`eres) possibles, −1, 0 et 1. Notons que si u
est un ´el´ement non bisp´ecial, on peut ´egalement d´eﬁnir son ordre bilat`ere, qui est
toujours nul.

Proposition 3.5 Soit L un langage factoriel prolongeable. Alors

∑

u∈L∩Σn m(u)= s(n +1) − s(n) .

Cette quantit´esera not´ee b(n).

Preuve. Quand on prolonge par une lettre `a droite un facteur sp´ecial `a gauche u,
la nature de u permet de d´eterminer, non le nombre de facteurs sp´eciaux `a gauche
obtenus, mais la somme de leurs ordres `a gauche :
–si u n’est pas bisp´ecial, on obtient un facteur sp´ecial `a gauchedemˆeme ordre
que u ;
–si u est bisp´ecial, on obtient un certain nombre de facteurs sp´eciaux `a gauche
dont la somme des ordres `a gauche est mg(u)+ m(u).
Comme s(n) est la somme des ordres `a gauche de tous les facteurs u de longueur n,
la variation de s(n) est donc la somme des m(u).

Comme dans le cas de l’alphabet binaire, les propositions 3.4 et 3.5 peuvent
d’exprimer en termes de s´eries g´en´eratrices :

Proposition 3.6 Soit L un langage factoriel prolongeable, et P , S et B les s´eries
g´en´eratrices des fonctions p, s et b associ´ees `a L.Alors

P (X)= 1
1 − X (1 + XS(X))

et
 S(X)= 1
1 − X (s(0) + XB(X))

soit
 P (X)= 1
(1 − X)2
 (1+ (p(1) − 2)X + X 2B(X)) .

Preuve. La seule diﬀ´erence notable avec la proposition 3.3 est le terme constant de
S, qui vaut s(0) = p(1) − 1, soit k − 1 si toutes les lettres de l’alphabet sont utilis´ees.

76 J. Cassaigne

Pour que la notion d’arbre de facteurs sp´eciaux soit utilisable, il faut un crit`ere
plus ﬁn que l’ordre : ´etant donn´ee une partie Σ
′ de Σ `a au moins deux ´el´ements,
on construit l’arbre des facteurs sp´eciaux `agauche de type Σ
′ en ne conservant dans
l’arbre des facteurs `a droite que ceux qui se prolongent `a gauche par chacune des
lettres de Σ
′. L’ensemble des facteurs sp´eciaux `a gauche est donc d´ecrit par une
famille d’arbres (un pour chaque partie Σ
′), mais en pratique on peut se limiter aux
arbres non vides avec Σ
′ maximal (i.e. aucune partie plus grande ne donne le mˆeme
arbre), ce qui en g´en´eral donne un petit nombre d’arbres, qu’on pourra appeler base
de la famille des arbres des facteurs sp´eciaux `a gauche. Dans ces arbres, tous les
embranchements et toutes les extr´emit´es de branches (feuilles) sont ´etiquet´es par
des facteurs bisp´eciaux, et r´eciproquement tous les facteurs bisp´eciaux d’ordre non
nul donnent un embranchement ou une feuille sur au moins l’un des arbres de base :
on peut donc d´eterminer les facteurs bisp´eciaux qui contribuent `alacomplexit´epar
simple observation de la base, et il est alors facile de calculer leur ordre.

4 Calcul de la complexit´ede suitesd ´eﬁnies par morphismes

Dans cette section, nous montrons, `a l’aide de quelques exemples, comment les
outils que nous venons de pr´esenter peuvent ˆetre utilis´es pour calculer la complexit´e
de certaines suites d´eﬁnies au moyen de morphismes de mono¨ıdes libres, ce qui est
le cas d’un grand nombre de suites classiques. Nous entendons par suites d´eﬁnies
par morphismes non seulement les suites qui sont point ﬁxe d’un morphisme, mais
aussi les images de tels points ﬁxes par un second morphisme, et plus g´en´eralement
les suites d´eﬁnies par des syst`emes S-adiques,c’est-`a-dire par application successive
d’une suite de morphismes pris dans un ensemble ﬁni.

4.1 Suite de Thue-Morse

La suitedeThue-Morseest le point ﬁxe

t = abbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaab . . .

du morphisme θ :Σ
∗ −→ Σ
∗

a ↦−→ ab
b ↦−→ ba
 .

Comme la suite de Thue-Morse est r´ecurrente, les constructions de la section 3
s’appliquent et il suﬃt de connaˆıtre ses facteurs bisp´eciaux pour calculer sa com-
plexit´e.

Proposition 4.1 Les facteurs bisp´eciaux de la suite de Thue-Morse sont

bisp´eciaux stricts : ε, θm(ab), θm(ba) pour m ⩾ 0 ;

bisp´eciaux ordinaires : a, b ;

bisp´eciaux faibles : θm(aba), θm(bab) pour m ⩾ 0.

La ﬁgure 4, qui montre l’arbre des facteurs sp´eciaux `a droite de la suite de Thue-
Morse, illustre bien ce r´esultat. La preuve repose sur le lemme classique suivant :

Complexit´eet facteurs sp´eciaux 77

Lemme 4.2 Tout facteur de t est de la forme y = r1.θ(x).r2 avec x ∈ F (t) et
ri ∈{ε, a, b}.Si |y| ⩾ 5 cette d´ecomposition est unique.
Preuve de la proposition. Soit y un facteur tel que |y| ⩾ 5. D’apr`es le lemme, y
s’´ecrit de mani`ere unique y = r1.θ(x).r2. Supposons que r2 = a.Si lemot ya ´etait
facteur de t, on pourrait aussi lui appliquer le lemme : ya = r′
1.θ(x′).r′
2. Comme θ(x′)
ne peut pas se terminer par aa,on aurait n´ecessairement r′
2 = a,donc y = r′
1.θ(x′).ε,
ce qui contredirait l’unicit´e dans le lemme. Le facteur y ne peut donc se prolonger
`a droite que par un b.De mˆeme, si r2 = b le seul prolongement possible est ya.Si y
est sp´ecial `a droite, alors n´ecessairement r2 = ε. Le prolongement ya se d´ecompose
alors sous la forme ya = r1.θ(x).a, donc a un prolongement unique yab dont la
d´ecomposition est n´ecessairement r1.θ(xa).ε,donc xa est facteur de t,et pour la
mˆeme raison xb est aussi facteur de t,donc x est sp´ecial `adroite.
On voit donc que les facteurs sp´eciaux `a droite de longueur au moins 5 sont tous
de la forme y = r1θ(x)avec x lui-mˆeme sp´ecial `a droite. Une propri´et´esym´etrique
est v´eriﬁ´ee `a gauche, donc les facteurs bisp´eciaux de longueur au moins 5 sont tous
des images par θ de facteurs bisp´eciaux, qui de plus ont mˆeme ordre. Il ne reste plus
qu’`a´enum´erer les facteurs bisp´eciaux courts pour pouvoir conclure : ε, ab, ba, abba,
baab sont stricts, a et b sont ordinaires, et aba et bab sont faibles.
On a donc :
 BS(X) − BF (X)=1 + 2
 ∞∑

n=0
 (X 2.2n − X 3.2n)

et on en d´eduit imm´ediatement les s´eries S(X)et P (X). On retrouve ainsi les
formules classiques [4] :
 s(n)=
 



 1si n =0
2si 0 <n ⩽ 2
4si 2.2
m <n ⩽ 3.2
m

2si 3.2
m <n ⩽ 4.2
m

p(n)=
 



 1si n =0
2si n =1
4si n =2
4n − 2.2
m − 4si 2.2
m <n ⩽ 3.2
m

2n +4.2
m − 2si 3.2
m <n ⩽ 4.2
m

o`u m est un entier positif ou nul.
La suite de Thue-Morse est un cas particuli`erement simple, mais de nombreuses
suites d´eﬁnies par morphisme peuvent ˆetre trait´ees sur le mˆeme mod`ele, `a condition
d’avoir un lemme de synchronisation similaire au lemme 4.2, qui assure un d´ecoupage
unique des facteurs suﬃsamment longs. Cela se produit notamment quand les mor-
phismes sont circulaires.

4.2 Action d'un morphisme circulaire

4.2.1 Morphismes circulaires

Nous appelons morphisme circulaire un morphisme injectif f :Σ
∗ → Σ
′∗ tel que
f(Σ) est un code circulaire,c’est-`a-dire

∀u ∈ Σ
∗, ∀v ∈ Σ
∗, ∀x ∈ Σ, ∀t ∈ Σ
′∗, ∀s ∈ Σ
′+,
[(f(x)= ts et f(u)= sf(v)t)=⇒ (t = ε et u = xv)]

78 J. Cassaigne

(voir [6]).

Remarque. Il existe une autre d´eﬁnition de la circularit´e, plus faible, adopt´ee
par exemple par Mignosi et S´e´ebold [9]. Cette notion n’est utile que dans le cas
de morphismes destin´es `aˆetre it´er´es (i.e. dont on consid`ere un point ﬁxe), car le
lemme de synchronisation correspondant ne vaut que pour les facteurs de ce point
ﬁxe. Pour des morphismes qui ne sont pas it´er´es, par exemple un morphisme de
codage appliqu´e une seule fois, comme le morphisme g du th´eor`eme 5.1, elle n’est
plus utilisable : on peut alors recourir `a une notion plus g´en´erale de circularit´esur
un langage [6] ; nous conservons ici la d´eﬁnition la plus restrictive aﬁn de simpliﬁer
l’expos´e. Notons que le morphisme θ d´eﬁnissant la suite de Thue-Morse n’est pas
circulaire selon cette d´eﬁnition.

Pour les morphismes circulaires, on a le lemme de synchronisation suivant [6] :

Lemme 4.3 Soit f un morphisme circulaire. Il existe trois ensembles ﬁnis N, R1
et R2 de mots de Σ
′∗ tels que que tout mot u ∈ F (f(Σ
∗)) \ N s’´ecrit de mani`ere
unique u = r1.f(v).r2 avec v ∈ Σ
∗ et ri ∈ Ri. Par ailleurs, si f(v′)= u1uu2 avec
v′ ∈ Σ
∗, alors on reconnaˆıt v dans v′ : v′ = v1vv2 avec f(v1)= u1r1 et f(v2)= r2u2.

Il peut y avoir plusieurs choix possibles pour les ensembles Ri. Quand f(Σ) est
un code bipr´eﬁxe (i.e. si f(u)est pr´eﬁxe de f(v), alors u est pr´eﬁxe de v,et demˆeme
avec les suﬃxes), on peut prendre pour R1 l’ensemble des suﬃxes stricts d’images de
lettres, et pour R2 l’ensemble des pr´eﬁxes stricts. Cela n’est pas possible en g´en´eral.
Par exemple, pour le morphisme sur {a, b}∗ d´eﬁni par f(a)= ab et f(b)= aba,on
peut prendre N = {ε, a, b, aa, ba, baa}, R1 = {ε, a, b, ba} et R2 = {ab,aba,abaa} : R1
ne pose pas de probl`eme car le code est suﬃxe, mais par contre R2 ne peut contenir
ε et a.
Pour simpliﬁer, nous supposerons donc que f(Σ) est un code bipr´eﬁxe. Cette
hypoth`ese n’est en fait pas indispensable, ce qui compte est que f(Σ) est un code `a
d´elai de d´echiﬀrage born´e, et c’est le cas pour tout morphisme circulaire. Il pourra
toutefois ˆetre n´ecessaire, quand le code n’est pas bipr´eﬁxe, de distinguer les facteurs
sp´eciaux en fonction des mots d’une certaine longueur par lesquels ils se prolongent,
et non plus seulement les lettres.

4.2.2 Action sur les facteurs bisp ´eciaux

Soit L ⊂ Σ
∗ un langage factoriel prolongeable, et L
′ = F (f(L)) la clˆoture fac-
torielle de son image par le morphisme circulaire f (L
′ est ´egalement un langage
factoriel prolongeable). Nous allons montrer, dans le cas o`u f(Σ) est bipr´eﬁxe, qu’il
est possibleded´ecrire les facteurs bisp´eciaux de L
′ connaissant ceux de L et les
couples de lettres qui peuvent les prolonger. De mˆeme, on peut construire les arbres
de facteurs sp´eciaux de L
′ en fonction de ceux de L. En pratique, il est souvent plus
simple de repr´esenter d’abord ces arbres et d’y lire les facteurs bisp´eciaux d’ordre
non nul.
Soit u un facteur bisp´ecial de L
′ n’appartenant pas `a N.Grˆace au lemme 4.3, le
mot u s’´ecrit de mani`ere unique u = r1.f(v).r2 avec r1 ∈ R1, r2 ∈ R2 et v ∈ Σ
∗.De
plus, la deuxi`eme partie du lemme implique que v ∈ L. Puisqu’on a suppos´e f(Σ)
bipr´eﬁxe, on peut choisir R1 et R2 de sorte que r1 soit un suﬃxe strict et r2 un
pr´eﬁxe strict d’image de lettre.

Complexit´eet facteurs sp´eciaux 79

Comme u est sp´ecial `a droite, il se prolonge au moins de deux mani`eres ua et
ub.Les mots r2a et r2b ne peuvent ˆetre pr´eﬁxes de la mˆeme image de lettre, donc v
se prolonge par au moins deux lettres diﬀ´erentes x et y,avec r2a pr´eﬁxe de f(x)et
r2b pr´eﬁxe de f(y), c’est-`a-dire que v est sp´ecial `adroite dans L ; son ordre `adroite
est sup´erieur ou ´egal `a celui de u.Demˆeme, v est sp´ecial gauche dans L,donc est
bisp´ecial.
R´eciproquement, si v est un facteur bisp´ecial, l’ensemble R1f(v)R2 contient un
certain nombre de facteurs bisp´eciaux, dont la somme des ordres est exactement
l’ordre de v `a condition qu’aucun d’entre eux ne soit dans N. Les couples (r1,r2)
tels que r1f(v)r2 est bisp´ecial, et les ordres correspondants, ne d´ependent que de
l’ensemble des couples de lettres (x1,x2)tels que x1vx2 ∈ L.
On voit donc que, connaissant les facteurs bisp´eciaux de L, on peut calculer des
facteurs bisp´eciaux de L
′ en appliquant f et en ajoutant un ou plusieurs pr´eﬁxes et
suﬃxes r1 et r2, qui ne d´ependent que des lettres par lesquelles le facteur consid´er´e
se prolonge. On obtient ainsi tous les facteurs bisp´eciaux de L
′,sauf peut-ˆetre ceux
qui sont ´el´ements de N, qu’il faut d´eterminer `a la main, et que nous appellerons
facteurs bisp´eciaux exceptionnels.

4.3 Complexit ´e du point ﬁxe d'un morphisme

`A tout morphisme f :Σ
∗ → Σ
∗, on associe le langage

L(f)= F ({ f n(x) | n ∈ N et x ∈ Σ })

(c’est la clˆoture factorielle d’un DOL-langage o`u toutes les lettres de l’alphabet
servent d’axiomes), qui est prolongeable pourvu que f soit non-eﬀa¸cant (l’image
d’une lettre n’est jamais le mot vide) et que chaque lettre soit prolongeable des
deux cˆot´es, c’est-`a-dire
 ∀x ∈ Σ, ∃a, b ∈ Σ,axb ∈ L(f)

ce qui exclut les morphismes du type (a ↦→ ab, b ↦→ bb). Si de plus il existe une lettre
a ∈ Σ telle que f(a) ∈ aΣ
∗ et que ⋃

n∈N Alph (f n(a)) = Σ, la suite de mots (f n(a))

a pour limite un mot inﬁni u = f ω(a) dont l’ensemble des facteurs est exactement
L(f).
Quand f est circulaire il est possible, en it´erant le proc´ed´ed´ecrit ci-dessus,
de d´ecrire l’ensemble des facteurs bisp´eciaux de L(f)`a partir des seuls bisp´eciaux
exceptionnels, ce qui permet de construire les arbres de facteurs sp´eciaux. Si f est
bipr´eﬁxe, les facteurs bisp´eciaux de L(f) sont tous de la forme

u = s0f(s1)f 2(s2) ...f k−1(sk−1)f k(v)f k−1(pk−1)f k−2(pk−2) ...f 2(p2)f(p1)p0

avec v bisp´ecial exceptionnel, pi plus grand pr´eﬁxe commun de deux images de
lettres, et si plus grand suﬃxe commun (pas n´ecessairement des mˆemes lettres).

80 J. Cassaigne

4.4 Un exemple non primitif

Consid´erons le morphisme suivant :

f :Σ
∗ −→ Σ
∗

a ↦−→ aba
b ↦−→ bb
 .

Ce morphisme n’est pas primitif, car les images successives de b ne contiennent
aucun a (un morphisme f est dit primitif s’il existe un entier n tel que l’image de
chaque lettre par f n contient toutes les lettres). La suite qu’il engendre,

f ω(a)= ababbababbbbababbababbbbbbbbababbababbbbababbababbbbbbbbbbbbbbbbab . . .

est r´ecurrente (tout facteur apparaˆıt une inﬁnit´e de fois), mais pas uniform´ement
r´ecurrente puisqu’il existe des facteurs arbitrairement longs qui ne contiennent pas
de a.
Le morphisme f est bipr´eﬁxe, mais n’est pas circulaire. Toutefois, tout facteur
de longueur sup´erieure ou ´egale `a 4 qui n’est pas une puissance de b se synchronise.
On va donc appliquer la m´ethode d´ecrite en 4.3, en traitant `a part les puissances de
b. Parmi les petits facteurs (longueur inf´erieure `a 4) non puissances de b, on trouve
que seul bab est bisp´ecial : c’est donc le seul bisp´ecial exceptionnel. Les autres facteurs
bisp´eciaux non puissances de b seront les images it´er´ees de ce mot par f,car pi =
si = ε est le seul pr´eﬁxe ou suﬃxe commun `a f(a)et f(b). Les puissances de b sont
toutes des facteurs bisp´eciaux (c’est d’ailleurs une propri´et´eg´en´erale des suites qui
contiennent des puissances arbitrairement grandes de b mais aussi une inﬁnit´ede a),
stricts quand l’exposant est une puissance de 2, ordinaires sinon.
Les facteurs bisp´eciaux sont donc :

bisp´eciaux stricts : f m(b), de longueur 2
m,pour m ⩾ 0;

bisp´eciaux ordinaires : les autres puissances de b : ε, b3, b5, b6, b7, b9,etc. ;

bisp´eciaux faibles : f m(bab), de longueur 2
m(3 + m/2), pour m ⩾ 0.

Ceci fournit une expression des s´eries BS et BF sous forme de sommes inﬁnies, ainsi
que les ´equations fonctionnelles suivantes :

BS(X)= BS(X 2)+ X ;

BF (X)= ϕ(X, X)avec ϕ(X, Y )= ϕ(XY X, Y Y )+ YXY .

On peut enﬁn ´ecrire que s(n)= 1 + q − r,o`u q = ⌈log2 n⌉ est lenombredefacteurs
bisp´eciaux stricts de longueur inf´erieure `a n,et r = ⌈ W (128n log 2)
log 2 − 6
⌉ est le nombre
de facteurs bisp´eciaux faibles de longueur inf´erieure `a n (W (x) est l’unique fonction
analytique r´eelle sur ] − 1/e, +∞[ telle que W (x)eW (x) = x). On calcule ensuite :

p(n)= 1 + n−1∑

m=0 s(m)

=1 + n + q−1∑

m=0(n − 1 − 2
m) − r−1∑

m=0(n − 1 − 2
m(3 + m/2))

=1 + n +(n − 1)q − (2
q − 1) − (n − 1)r +(2
r+1 +2
r−1r − 2) .

Complexit´eet facteurs sp´eciaux 81

Dans cette expression, les termes dominants sont nq et nr,soit

p(n)= nlog n − W (128n log 2)
log 2 + O (n) .

On peut alors, en utilisant le fait que W (x)= log x − log log x + O ( log log x
log x
 ) obtenir
un ´equivalent de la complexit´ede la suite ´etudi´ee : p(n) ∼ n log2 log2 n.
Notons que le th´eor`eme de Pansiot [12] permet d’´etablir que p(n)croˆıt comme
n log log n,car f est polynomialement divergent, mais ne donne pas d’´equivalent
exact.

5 Suites de complexit´e afﬁne

5.1 Suites de complexit ´e ultimement afﬁne

J.-P. Allouche et J. Berstel ont pos´ele probl`eme suivant : pour quels entiers α
et β existe-t-il des suites dont la complexit´e est la fonction aﬃne p(n)= αn + β ?
Si on veut que ce soit vrai pour tout n ⩾ 0, la seule possibilit´eest β =1 et
α =# Alph (u)−1 (sur un alphabet binaire, cela correspond aux suites sturmiennes,
de complexit´e p(n)= n + 1 ; sur un alphabet plus grand, de telles suites existent
´egalement, voir par exemple la suite f ω(c1)du th´eor`eme 5.1). On recherche donc des
fonctions de complexit´e ultimement aﬃnes, c’est-`a-dire telles qu’il existe un rang n0
tel que pour tout n ⩾ n0 on a p(n)= αn + β. Pour que ce soit possible, il faut que
(α, β) ∈{0, 1}× (N \{0}) ∪ (N \{0, 1}) × Z. Nous verrons que cette condition est
suﬃsante, et ce sur tout alphabet ayant au moins deux ´el´ements.
Allouche [1] a d´evelopp´e plusieurs techniques pour construire, `a partir d’une suite
de complexit´e ultimement αn + β, des suites de complexit´es diﬀ´erentes, par exemple
αn + β + 1. Cependant il reste des couples (α, β) qui ne peuvent ˆetre obtenus par
ces techniques en partant des quelques suites de complexit´e ultimement aﬃne d´ej`a
connues. Il est donc n´ecessaire de construire de nouveaux points de d´epart. C’est
dans cet objectif que cette ´etude a ´et´e faite, mais celui-ci a ´et´ed´epass´e puisque nous
obtenons directement toutes les complexit´es ultimement aﬃnes possibles.
Pour cela, nous consid´erons une famille `a trois param`etres de suites, d´eﬁnies par
un morphisme it´er´e sur un alphabet plus ou moins grand, suivi d’un codage vers
l’alphabet `a deux lettres Σ = {a, b}.

Th´eor`eme 5.1 Soient j ⩾ 0, k ⩾ 1 et ℓ ⩾ 1 trois entiers. Soit Σk = {c1,... ,ck}
un alphabet `a k lettres. On consid`ere les deux morphismes f et g d´eﬁnis ainsi :

f :Σ
∗
k −→ Σ
∗
k
ci ↦−→ c1ci+1 si i ̸= k
ck ↦−→ c1
 et g :Σ
∗
k −→ Σ
∗

ci ↦−→ aℓbi+j

pour tout i compris entre 1 et k.
La suite u = g(f ω(c1)) a pour complexit´e

p(n)=(k − 1)n − k(k − 1)
2 − j(k − 2) + ℓ +1

pour n ⩾ max(ℓ, j + k − 1,j +1).

82 J. Cassaigne

Preuve. Calculons tout d’abord les facteurs bisp´eciaux de L(f). Le morphisme f
est circulaire et suﬃxe (mais non bipr´eﬁxe). Dans le lemme 4.3, on peut prendre
N = R1 = {ε, c2,... ,ck} et R2 = {c1,c1c2,... ,c1ck}.Leseul bisp´ecial exceptionnel
est ε, d’ordre 0 car il se prolonge par (c1,ci)et(ci,c1)pour 1 ⩽ i ⩽ k. Par ailleurs,
un mot de la forme u = r1f(v)r2 ne peut ˆetre bisp´ecial que si r1 = ε et r2 = c1.En
partant de ε,on obtient c1, puis c1c2c1,etc., quiseprolongent par (cm,ci)et(ci,cm)
pour tout i et pour un indice m ﬁx´e, et sont donc tous d’ordre 0.
On en d´eduit que la base des arbres des facteurs sp´eciaux `a gauche de L(f)ne
contient qu’un seul arbre, de type Σk, puisque chaque facteur bisp´ecial peut ˆetre
prolong´e`a gauche par chacune des k lettres de l’alphabet, et donc il en est de
mˆeme pour chaque facteur sp´ecial `a gauche. Comme tous les facteurs bisp´eciaux
sont d’ordre nul, cet arbre ne peut ˆetre que ﬁliforme, et est d’ailleurs ´etiquet´epar
la suite elle-mˆeme. En quelque sorte, f ω(c1) est une suite de Fibonacci g´en´eralis´ee,
et sa complexit´eest (k − 1)n +1.
 aa a a
aaa
 a a

bisp´eciaux stricts
 a
a
 aa aa
a a
aa
aa
a
 a

a aa a

a
 b
a b

b
 b

a
 b
a
 b
a ba b

b
 bb b

b
 b

ab
 ···

···
···
···

···

b

b
 bisp´eciaux faibles

a
a

a
a

b ε
 j +1

ℓ − 1
 lignes
k − 1

Fig. 6 – Arbre des facteurs sp´eciaux `a gauche de g(f ω(c1)) pour j =1, k =6, ℓ =4

On applique ensuite le morphisme g,qui est ´egalement circulaire et suﬃxe, pour
obtenir les facteurs bisp´eciaux de F (g(L(f))). On peut prendre

N = { aibi′ | i< ℓ, i′ ⩽ j + k } ,

R1 = { bi′ | i′ ⩽ j + k }∪ { aibi′ | 1 ⩽ i< ℓ, j < i′ ⩽ j + k }

et R2 = { ai | 1 ⩽ i< ℓ }∪ { aℓbi′ | i′ ⩽ j + k } .

Lesfacteursbisp´eciaux exceptionnels sont ε, d’ordre 1, bi′ pour 1 ⩽ i′ ⩽ j, d’ordre
0, bi′ pour j +1 ⩽ i′ ⩽ j + k − 2, d’ordre 1, bj+k−1, d’ordre 0, ai pour 1 ⩽ i ⩽ ℓ − 2,
d’ordre 0, et aℓ−1, d’ordre −1, sauf dans le cas ℓ =1 o`u ε = aℓ−1 est d’ordre 0. Les
autres bisp´eciaux sont de la forme bj+if(v)aℓbj+i′ o`u v est un bisp´ecial de L(f)se
prolongeant par (cm,ci)et (ci,cm), et i ⩽ m et i′ ⩽ m. Il sont tous d’ordre 0.
Il ne reste plus qu’`a compter les facteurs bisp´eciaux d’ordre non nul pour obtenir
la complexit´echerch´ee : si ℓ> 1, il y a un bisp´ecial faible de longueur ℓ − 1, et k − 1
bisp´eciaux stricts de longueurs 0 et j +1 `a j + k − 2, et si ℓ = 1 il y a seulement
k − 2bisp´eciaux stricts de longueur j +1 `a j + k − 2.
On en d´eduit ´egalement la forme de l’arbre des facteurs sp´eciaux `a gauche de
F (g(L(f))) (ﬁgure 6). Cet arbre comporte k − 1 branches inﬁnies (chaque facteur

Complexit´eet facteurs sp´eciaux 83

sp´ecial `a gauche pour L(f), d’ordre k − 1, donne un ´el´ement dans chacune des
branches) et une branche ﬁnie de longueur ℓ − 1, termin´ee par le facteur bisp´ecial
exceptionnel aℓ−1.

Corollaire 5.2 Pour tout couple d’entiers (α, β) ∈{0, 1}×(N\{0})∪(N\{0, 1})×Z,
il existe une suite binaire de complexit´e ultimement αn + β.

Preuve. La suite u d´eﬁniedans leth´eor`eme 5.1 fournit une solution dans tous les
cas, avec k = α +1 ⩾ 1et j et ℓ choisis en fonction de α et β.
Si k =1, la suite u a pour complexit´e ultimement j +ℓ+1.Sion prend j = ⌊ β−1
2
 ⌋

et ℓ = ⌊ β
2
 ⌋,on a p(n)= β pour n ⩾ ⌊ β+1
2
 ⌋.
Si k =2, la suite u a pour complexit´e ultimement n + ℓ. On prend donc ℓ = β
et (par exemple) j =0, et on a p(n)= n + β pour n ⩾ β.
Si k> 2, soit par exemple

j =max
 (0,
 ⌊ −k2 +3k − 2 − 2β
2k − 4
 ⌋)

et
 ℓ = β + k(k − 1)
2 + j(k − 2) − 1 ⩾ 1 .

La suite u a alors pour complexit´e p(n)= αn + β pour

n ⩾ max
 (α, α
2 − β
α − 1 ,β + α(α +1)
2 − 1

) .

5.2 Complexit ´e αn + β pour n ⩾ 1

La question suivante, variante du probl`eme ci-dessus, a ´et´epos´ee par Pascal
Alessandri : pour quelles valeurs de (α, β) existe-t-il une suite de complexit´e p(n)=
αn + β pour tout n ⩾ 1 ? Elle peut ˆetre r´esolue par une construction similaire.

Th´eor`eme 5.3 Soit (α, β) ∈ N × Z. Il existe une suite de complexit´e p(n)= αn + β
pour tout n ⩾ 1 (et p(0) = 1)si et seulement si α + β ⩾ 1 et 2α + β ⩽ (α + β)2.

Preuve. Ces conditions sont ´evidemment n´ecessaires : p(1) = α + β est lenombrede
lettres distinctes apparaissant dans la suite, donc est un nombre strictement positif ;
et si la suite contient α + β lettres distinctes, elle ne peut contenir plus de (α + β)2

facteurs de longueur 2, donc 2α + β = p(2) ⩽ p(1)2 =(α + β)2.
Supposons maintenant que (α, β) satisfait les deux conditions, et que α> 0, le cas
α =0 ´etant facile `ar´esoudre avec des suites p´eriodiques. Soit k = α+1 et ℓ = α+β :
on va construire un HDOL-syst`eme G =(Σk,f,c1, Σl,h)o`uΣk = {c1,... ,ck} et
Σl = {d1,... ,dl}, de telle sorte que la suite associ´ee u = h(f ω(c1)) aura la complexit´e
voulue.
Le DOL-syst`eme sous-jacent (voir [6]) G
0 =(Σk,f,c1)est le mˆeme que pour
le th´eor`eme 5.1. La suite f ω(c1) est donc une suite de Fibonacci g´en´eralis´ee, de
complexit´e αn + 1 pour tout n.

84 J. Cassaigne

La construction du morphisme h d´epend du signe de β. Supposons tout d’abord
que ℓ ⩾ k,c’est-`a-dire que β> 0. Si ℓ = k,la suite f ω(c1)a d´ej`ala com-
plexit´echerch´ee et il suﬃt de prendre h = Id.Sinon, on d´eﬁnit h par h(c1)=
d1dk+1dk+2 ... dl et h(ci)= di pour 2 ⩽ i ⩽ k : le morphisme h est circulaire et
bipr´eﬁxe. On voit facilement que la base des arbres de facteurs sp´eciaux `a gauche
de F (u) a deux ´el´ements, un arbre ﬁliforme de type {d1,... ,dk} (image par h de
l’arbre de L(f)) et un arbredetypeΣl contenant le seul nœud ε,seul facteur
bisp´ecial exceptionnel, et seul facteur bisp´ecial d’ordre non nul, k − ℓ. Onend´eduit
imm´ediatement que la complexit´eest bien p(n)= αn + β pour n ⩾ 1.
Supposons maintenant que ℓ< k,c’est-`a-dire β ⩽ 0. On d´eﬁnit h de la mani`ere
suivante : h(c1)= d1, h(ci)= d1di pour 2 ⩽ i ⩽ ℓ,et h(cℓ+1), ..., h(ck)sont k − ℓ
´el´ements pris parmi l’ensemble E = d1{d2,... ,dl}2, qui en compte (ℓ − 1)2 ; comme
k − ℓ =1 − β ⩽ (α + β)2 − 2α − 2β +1 = (ℓ − 1)2, c’est toujours possible. L’ordre
des images n’a pas d’importance.
Le morphisme h est suﬃxe et circulaire, de d´elai de synchronisation 2, grˆace au
rˆole de marqueur jou´epar d1. Nous pouvons donc d´eterminer les facteurs sp´eciaux
`a gauche de F (u) en fonction de ceux de L(f).
Soit u un facteur sp´ecial `a gauche pour L(f) : il se prolonge par chacune des
lettres de Σk. Les suﬃxes communs des f(ci)sont ε et toutes les lettres di telles
que E ∩ d1Σkdi ̸= ∅ ; les facteurs sp´eciaux `a gauche pour F (u) obtenus sont donc
f(u), d’ordre ℓ − 1 (il se prolonge par chacune des lettres de H1 =Σl), et dif(u),
d’ordre # (E ∩ d1Σkdi) quand cet ensemble est non vide (il se prolonge par Hi =
{d1}∪ { dj | d1djdi ∈ E }). Les seuls mots non synchronis´es sont ε et certains di,
mais ils ne donnent pas de nouveaux facteurs sp´eciaux. Finalement, la base contient
un arbre pour chaque ensemble Hi, avec une ou plusieurs branches ﬁliformes partant
de ε (une branche pour chaque j tel que Hi ⊂ Hj). Comme pr´ec´edemment, ε est
le seul facteur bisp´ecial d’ordre non nul, et son ordre vaut k − ℓ (l’ordre de ε est
toujours ´egal `a p(2) − 2p(1) + 1).

Une extension int´eressante de ces deux probl`emes serait de chercher `a construire
des suites de complexit´e ⌊αn+ β⌋,avec α (et ´eventuellement β) non entier. Il semble
que cela ne soit pas possible.

6 Une famille continue de fonctions de complexit´e

Pour le moment, nous savons construire une famille d´enombrable de fonctions
de complexit´e. Nous allons montrer dans cette section que l’ensemble des fonctions
de complexit´e a la puissance du continu.

Th´eor`eme 6.1 Soit ϕ : R −→ R une fonction deux fois d´erivable et un r´eel stric-
tement positif x0 tels que

(i) 0 ⩽ ϕ′′(x) ⩽ 1 pour x ⩾ x0 ;

(ii) x log x = o(ϕ(x)).

Alors il existe une suite binaire u dont la complexit´ev´eriﬁe

pu(n) ∼ ϕ(n) .

Complexit´eet facteurs sp´eciaux 85

La seconde condition peut ˆetre remplac´ee, au prix d’une complication de la preuve,
par l’hypoth`ese plus faible et plus naturelle que ϕ′(x) tend vers +∞ quand x tend
vers +∞.

Preuve. Pour i ∈ N,soit qi le plus petit entier sup´erieur ou ´egal `a x0 tel que
⌊ϕ′(qi) − ϕ′(x0)⌋ = i.D’apr`es les propri´et´es de ϕ, ces entiers existent, sont positifs,
et la suite (qi) est strictement croissante. On d´eﬁnit une suite binaire u de la mani`ere
suivante : on part de la suite v sur l’alphabet d´enombrable Σ∞ = {c0,c1,... ,ci,...},
point ﬁxe du morphisme f qui `a ci associe c0ci+1 :

v = c0c1c0c2c0c1c0c3c0c1c0c2c0c1c0c4c0c1c0c2c0c1c0c3c0c1c0c2c0c1c0c5c0c1c0c2 ...

et on lui applique le morphisme g :Σ
∗
∞ −→ {a, b}∗

ci ↦−→ abqi pour obtenir u = g(v).

Les facteurs sp´eciaux de v sont faciles `ad´eterminer : `a gauche ce sont les pr´eﬁxes
de v,`a droite leurs images miroir (on pourrait les appeler facteurs sp´eciaux d’ordre
inﬁni, car ils se prolongent par toutes les lettres de Σ∞, sauf celles qu’ils contiennent
d´ej`a). Comme dans la preuve du th´eor`eme 5.1, on utilise le fait que g est un mor-
phisme circulaire (et suﬃxe) pour en d´eduire la forme de l’arbre des facteurs sp´eciaux
`a gauche de u.Ilest constitu´epar la r´eunion d’une inﬁnit´e de branches ﬁnies,
´etiquet´ees par bq0abq0, bq1abq0abq1, bq2abq0abq1abq0abq2,et en g´en´eral bqig(f i(c0)) pour
tout i ∈ N.
Le mot inﬁni a donc une inﬁnit´ede facteurs bisp´eciaux stricts et faibles. Les
bisp´eciaux stricts ´etiquettent les endroits o`u les branches se s´eparent, c’est-`a-dire
les bqi pour i ∈ N,et les bisp´eciaux faibles sont les ´etiquettes des branches enti`eres,
bqig(f i(c0)) pour i ∈ N. La longueur des premiers est simplement qi. Celle des seconds
est ri =2qi +2
i + ∑i−1
j=0 2
i−j−1qj, que l’on peut minorer par 2
i.
Le nombre de facteurs sp´eciaux s(n) est alors

s(n)=1 + min { i | n ⩽ qi }− min { i | n ⩽ ri } .

Le dernier terme est en O (log n). Sachant que ⌊ϕ′(qi) − ϕ′(x0)⌋ = i, le second terme
peut ˆetre encadr´epar

ϕ′(n) − ϕ′(x0) − 1 < min { i | n ⩽ qi } <ϕ′(n) − ϕ′(x0)+1

d`es que n ⩾ x0. En sommant une nouvelle fois, on trouve que

p(n)= 1 +
 n−1∑

m=0 s(m)= ϕ(n)+ O (n log n)

et l’hypoth`ese (ii) nous assure que le second terme est n´egligeable.

En quelque sorte, ce th´eor`eme montre que toutes les fonctions `a croissance suﬃ-
samment r´eguli`ere comprises entre n log n et n
2 sont asymptotiquement des fonctions
de complexit´e. C’est le cas notamment des n
α pour 1 <α < 2. Par cons´equent, le
cardinal de l’ensemble des fonctions de complexit´eest ´egal `a celui de R (il ne peut
bien sˆur pas ˆetre plus grand).

Remarque. Grillenberger [8] a montr´e comment construire des suites d’entropie
topologique h pour tout r´eel h compris entre 0 et log #Σ. Cela fournit donc une autre

86 J. Cassaigne

famille continue de fonctions de complexit´e, qui ont une croissance exponentielle (si
h> 0), contrairement aux nˆotres qui sont `a croissance polynomiale (et donc toutes
associ´ees `a des suites d’entropie nulle).

7 Complexit´e sous-afﬁne

Dans les deux sections pr´ec´edentes nous avons construit des familles de fonctions
de complexit´e. Nous allons maintenant voir une condition n´ecessaire que doivent
v´eriﬁer ces fonctions quand leur croissance n’est pas tr`es rapide, et qui les empˆeche
de croˆıtre de fa¸con trop oscillante.
Cette section r´esume les r´esultats qui sont pr´esent´es de mani`ere d´etaill´ee dans
[7]. Notre th´eor`eme principal, conjectur´e par Ferenczi, est le suivant :
Th´eor`eme 7.1 Soit u ∈ Σ
ω une suite sur un alphabet ﬁni dont la fonction de
complexit´e p(n) est sous-aﬃne, c’est-`a-dire que p(n)= O(n). Alors la fonction
s(n)= p(n +1) − p(n) est born´ee.
Cela signiﬁe par exemple que la situation suivante ne peut pas se produire :
p(n +1) − p(n) prend des valeurs faibles sauf en des “pics” arbitrairement hauts,
mais suﬃsamment ´etroits et espac´es pour ne pas trop faire augmenter p(n).
Une telle propri´et´e´etait d´ej`a connue pour certains types de suites, points ﬁxes de
substitutions primitives [11]. En particulier, le th´eor`eme 7.1 permet de red´emontrer
que si u est une suite automatique, alors (p(n +1) − p(n))n∈N est aussi une suite
automatique [14].
Notre preuve donne en fait un r´esultat plus g´en´eral et plus pr´ecis :
Th´eor`eme 7.2 Soit u ∈ Σ
ω une suite sur un alphabet ﬁni et p(n) sa fonction de
complexit´e. On suppose qu’il existe deux r´eels a> 0 et 1 ⩽ α ⩽ 3
2,et un entier n0,
tels que p(n) ⩽ an
α pour tout n ⩾ n0.Alors

s(n)= p(n +1) − p(n) ⩽ Kp(1)a3n
3(α−1)

pour tout n ⩾ n0,o`u K est une constante qui ne d´epend pas de u.
La constante K de ce th´eor`eme peut ˆetre explicit´ee, mais cela pr´esente peu
d’int´erˆet tant qu’il n’est pas ´etabli que l’exposant 3 dans a3n
3(α−1) est optimal.
C’est `a cause de cet exposant que α est limit´e`a 3
2 , car au-del`a de cette valeur le
th´eor`eme n’apporte rien de plus que la relation triviale s(n) ⩽ p(n +1) ⩽ a(n +1)α.
Mais nous ne connaissons aucune suite dont la complexit´ev´eriﬁe p(n)= O(n
α)mais
non s(n)= O(n
α−1). Il serait int´eressant de construire de telles suites, ou bien sˆur de
montrer qu’il n’en n’existe pas, ce qui renforcerait consid´erablement le th´eor`eme 7.2.
Pour d´emontrer les th´eor`emes 7.1 et 7.2, on utilise le lemme suivant, dont la
preuve, tr`es technique, consiste `a compter des chemins dans le graphe de Rauzy
d’ordre n1 associ´es `a des facteurs sp´eciaux de longueur comprise entre n1 et n2 :
Lemme 7.3 Soit L un langage factoriel prolongeable sur un alphabet binaire, p(n)
sa fonction de complexit´e, et n1 <n2 deux entiers. On suppose que s(n1) ⩾ 1.Soit
m =max
n1⩽n<n2 s(n). Alors la variation de complexit´eentre n1 et n2 est au moins

p(n2) − p(n1) ⩾ n1
2s(n1)2
 (m − s(n1)(1+ s(n1)+ s(n2 − 1))) .

Complexit´eet facteurs sp´eciaux 87

De fa¸con imag´ee, il signiﬁe que si s(n)pr´esente un pic entre n1 et n2,alors p(n)
croˆıt d’une valeur d’autant plus grande que le pic est haut et que s(n1)et s(n2)sont
petits, mais qui ne d´epend pas de la largeur du pic. Par un calcul relativement simple,
on ´etablit alors un r´esultat similaire au th´eor`eme 7.2 pour les langages factoriels
prolongeables sur un alphabet binaire. Au moyen d’un codage, il peut ˆetre ´etendu
aux langages sur un alphabet ﬁni quelconque. Pour obtenir le th´eor`eme 7.2, il ne
reste plus qu’`a traiter le cas des suites non r´ecurrentes comme indiqu´een 2.2.

8 Conclusion

Nous avons vu que l’´etude des facteurs sp´eciaux permettait de calculer plus
facilement certaines complexit´es, et d’obtenir d’autres r´esultats int´eressants sur les
fonctions de complexit´e. Cela est surtout vrai pour les suites dont la complexit´e
croˆıt lin´eairement, ou `a la rigueur de fa¸con quadratique, car le nombre de facteurs
bisp´eciaux est la diﬀ´erence seconde de la complexit´e qui est alors faible. Il serait
certainement utile d’avoir une interpr´etation combinatoire de diﬀ´erences d’ordre
plus ´elev´e, mais cela ne semble pas possible avec nos techniques, car les facteurs
bisp´eciaux n’ont plus aucune propri´et´e de prolongeabilit´e, ce qui interdit de les
repr´esenter par une structure comme l’arbre des facteurs sp´eciaux.
Nous sommes encore tr`es loin de pouvoir caract´eriser les fonctions qui sont des
fonctions de complexit´e, mˆeme si les th´eor`emes 6.1 et 7.1 permettent de se faire une
meilleure id´ee de l’endroit o`u se situe la limite. Il doit ˆetre possible de resserrer encore
cet encadrement, en cherchant la borne exacte sur s(n)dans le th´eor`eme 7.1, en
´etendant ce th´eor`eme de fa¸con plus pr´ecise aux degr´es plus grands, et le th´eor`eme 6.1
`a d’autres classes de fonctions.
Une autre direction de recherche possible est de voir comment des restrictions
sur les suites consid´er´ees inﬂuent sur les fonctions r´ealisables : si L est une famille
de langages ou de suites, notons P(L) l’ensemble des fonctions de complexit´edes
´el´ements de L. Obtient-on des ensembles diﬀ´erents quand L =Σ
ω, L = ωΣ
ω (suites
biinﬁnies), L est l’ensembles des suites r´ecurrentes ou uniform´ement r´ecurrentes, des
langages factoriels prolongeables, etc. ?

88 J. Cassaigne

R ´ef´erences

[1] J.-P. Allouche, Expos´eaux Journ´ees Montoises `a Bordeaux (1993).

[2] J.-P. Allouche, Sur la complexit´e des suites inﬁnies, Bull. Belg. Math. Soc. 1
(1994) 133–143.

[3] P. Arnoux et G. Rauzy, Repr´esentation g´eom´etriquedesuites decomplexit´e
2n +1, Bull. Soc. Math. France 199 (1991) 199–215.

[4] S. Brlek, Enumeration of factors in the Thue-Morse word, Discr. Appl. Math.
24 (1989) 83–96.

[5] J. Cassaigne, Counting overlap-free binary words, in STACS ’93, P. Enjalbert,
A. Finkel et K. W. Wagner (´ed.), W¨urzburg, Lect. Notes Comput. Sci. 665,
Springer-Verlag (1993) 216–225.

[6] J. Cassaigne, Motifs ´evitables et r´egularit´es dans les mots, Th`ese de Doctorat,
Universit´e Paris 6 (1994). Rapport LITP TH 94-04.

[7] J. Cassaigne, Special factors of sequences with linear subword complexity, in
Developments in Language Theory, World Scientiﬁc (1996).

[8] C. Grillenberger, Constructions of strictly ergodic systems — I. Given entropy,
Z. Wahr. verw. Geb. 25 (1973) 323–334.

[9] F. Mignosi et P. S´e´ebold, If a DOL language is k-power-free then it is circular,
in ICALP ’93, Lund, Lect. Notes Comput. Sci. 700, Springer-Verlag (1993).

[10] M. Morse et G. A. Hedlund, Sturmian sequences, Amer. J. Math. 61 (1940)
1–42.

[11] B. Moss´e, Notions de reconnaissabilit´e pour les substitutions et complexit´edes
suites automatiques. Preprint (1993).

[12] J.-J. Pansiot, Complexit´e des facteurs des mots inﬁnis engendr´es par mor-
phismes it´er´es, in ICALP ’84, Lect. Notes Comput. Sci. 172, Springer-Verlag
(1984) 380–389.

[13] G. Rote, Sequences with subword complexity 2n, J. Number Th. 46 (1994)
196–213.

[14] T. Tapsoba, Complexit´e de suites automatiques, Th`esede3ecycle,Universit´e
d’Aix-Marseille II (1987).
 Julien Cassaigne
Institut de Math´ematiques de Luminy
163 avenue de Luminy, case 930
F-13288 Marseille Cedex 9 (France)
Julien.Cassaigne@iml.univ-mrs.fr
