<!-- source: https://univ-fcomte.hal.science/tel-02292193/document | converted from PDF -->

HAL Id: tel-02292193

https://univ-fcomte.hal.science/tel-02292193v1

Submitted on 19 Sep 2019

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

Distributed under a Creative Commons CC BY-NC-ND 4.0 - Attribution - Non-commercial use - No
Derivative Works - International License

Points de petite hauteur en géométrie diophantienne

Aurélien Galateau

To cite this version:

Aurélien Galateau. Points de petite hauteur en géométrie diophantienne. Mathématiques [math]. Université
de Bourgogne - Franche Comté, 2016. ⟨tel-02292193⟩

UNIVERSITÉ DE BOURGOGNE FRANCHE-COMTÉ

Laboratoire de Mathématiques de Besançon

Mémoire d’Habilitation

Présenté par

Aurélien Galateau

Points de petite hauteur
en géométrie diophantienne

Soutenu le 2 décembre 2016 devant le jury composé de :

Francesco Amoroso Professeur, Université de Caen (rapporteur)

Huayi Chen Professeur, Université Paris 7

Éric Gaudron Professeur, Université de Clermont-Ferrand

Philipp Habegger Professeur, Universität Basel (rapporteur)

Marc Hindry Professeur, Université Paris 7

Federico Pellarin Professeur, Université de Saint-Étienne

Martín Sombra Professeur, Universitat de Barcelona (rapporteur, excusé)

Remerciements

Ce mémoire présente mes travaux de recherche depuis la ﬁn de ma thèse il y
a neuf ans. Pendant cette période, j’ai pu compter sur l’aide de mes diﬀérentes
institutions d’accueil et de nombreux collègues mathématiciens.

Je souhaite d’abord remercier l’Institut de Mathématiques de Bâle, et en par-
ticulier David Masser dont j’ai été l’assistant entre 2007 et 2009. J’ai bénéﬁcié les
deux années suivantes d’une bourse post-doctorale au Laboratoire de Mathéma-
tiques d’Orsay, dans la compagnie stimulante d’Emmanuel Breuillard et Emmanuel
Ullmo. Depuis 2011, je suis maître de conférences au Laboratoire de Mathéma-
tiques de Besançon. J’y ai rejoint l’équipe d’Algèbre et Théorie des Nombres dont
je salue les membres avec gratitude. C’est un plaisir d’enseigner et de faire des ma-
thématiques dans cet environnement bienveillant où on peut toujours compter sur
le soutien des collègues, qu’ils soient mathématiciens, informaticiens ou techniciens
administratifs. Ces cinq dernières années, dans le cadre d’un détachement au CNRS,
j’ai fait de nombreux séjours de recherche au Laboratoire Poncelet à Moscou, où Eli-
zaveta Kryukova et Michael Tsfasman m’ont oﬀert des conditions de travail idéales.
Mes remerciements vont aussi au BICMR de Pékin, à l’IMPA de Rio et à l’ESI de
Vienne.

Francesco Amoroso, Philipp Habegger et Martín Sombra ont accepté d’écrire un
rapport sur ce mémoire. Je m’en réjouis d’autant plus que certains de leurs travaux
ont été une source d’inspiration importante pour les résultats qui sont exposés ici.
Je suis également reconnaissant à Huayi Chen, Éric Gaudron, Marc Hindry et Fe-
derico Pellarin d’avoir accepté de compléter le jury. Depuis mes premiers pas dans
la recherche, j’ai souvent pu proﬁter de leurs conseils, de leurs encouragements et
de leurs lumières mathématiques.

Je tiens à remercier Sinnou David, qui n’a jamais cessé depuis plus de dix ans
de me communiquer ses intuitions et son magniﬁque enthousiasme. Un grand merci
également à Antoine Chambert-Loir pour son énergie contagieuse et à Gaël Rémond
pour son jugement infaillible.

La recherche en mathématiques est une activité collective, et les travaux décrits
ici ont grandement bénéﬁcié de conversations avec mes collègues, collaborateurs et
amis mathématiciens, parmi lesquels : Cécile Armana, Jean-Robert Belliard, Vincent
Bosser, Alberto Cámara, Sara Checcoli, Agnès David, Christophe Delaunay, Phi-
lippe Lebacque, Francesco Lemma, Valéry Mahé, César Martínez, Amilcar Pacheco,
Fabien Pazuki, Martin Widmer. Un salut amical enﬁn aux compagnons de route
avec qui je partage l’aventure mathématique : David Cohen, Adrien Deloro, Benja-
min Girard, Anne-Sophie Kaloghiros, Pierre-Yves Le Gall, Vésale Nicolas, Florent
Schaﬀhauser, Alexey Zykin. Et à tous mes proches pour leur soutien indéfectible.

Introduction

La géométrie diophantienne est l’étude des solutions entières ou rationnelles
de systèmes d’équations polynomiales à l’aide des concepts et des techniques de
la géométrie algébrique. Celle-ci, et en particulier sa formulation moderne dans la
théorie des schémas développée par Grothendieck à partir des années 50, donne une
interprétation géométrique des systèmes d’équations algébriques. Elle leur associe
également un certain nombre d’invariants à partir desquels elle entreprend de les
classiﬁer.

Le but ultime de la géométrie diophantienne est d’énumérer les solutions des
problèmes diophantiens en fonction de leurs invariants géométriques. Ce programme
très ambitieux est encore loin de son terme, y compris dans le cadre relativement
simple des courbes algébriques. L’outil central dans sa mise en œuvre est la théorie
des hauteurs développée à la suite des travaux de Weil sur les points rationnels des
jacobiennes, qui quantiﬁe la « complexité arithmétique » des solutions d’un problème
diophantien. La propriété de Northcott permet alors de les dénombrer si on sait
borner leur hauteur en fonction des invariants géométriques du problème.

Les recherches sur les petites valeurs de la hauteur trouvent leur origine dans
l’étude de la mesure de Mahler d’un polynôme, qui donne des indications sur la
répartition de ses racines dans le plan complexe. On peut d’abord essayer de minorer
précisément la hauteur dès lors qu’elle ne s’annule pas. Cette question spéciﬁquement
« arithmétique » se situe dans le prolongement d’un célèbre problème encore non
résolu posé par Lehmer au début des années 30. Il existe aussi des estimations
de nature plus « géométrique » où on quantiﬁe la rareté des points algébriques de
petite hauteur de certains objets géométriques, dans la lignée d’une conjecture sur
les courbes formulée par Bogomolov au début des années 80.

Les estimations géométriques sur les points de petite hauteur jouent un rôle
important dans l’obtention via la méthode de Vojta de bornes explicites précises
sur le nombre de points rationnels des courbes, et sur leur distribution dans des ob-
jets de dimension supérieure. Elles sont également utilisées, en concurrence avec les
estimations arithmétiques, pour donner des résultats qualitatifs en direction d’une
conjecture de Pink et de Zilber, qui étend dans une large mesure la conjecture de
Manin-Mumford et trouve sa formulation la plus générale dans le cadre des variétés
de Shimura mixtes (comprenant notamment les tores, les variétés abéliennes et leurs
espaces de modules).
 5

6 INTRODUCTION

Les travaux résumés dans ce mémoire contribuent à la connaissance des points de
petite hauteur dans diﬀérents contextes de la géométrie diophantienne : les variétés
abéliennes, les corps de nombres et les modules de Drinfeld. Mes recherches ont
d’abord porté sur une version précise du théorème d’Ullmo et de Zhang résolvant
la conjecture de Bogomolov, puis elles ont évolué vers des questions de nature plus
arithmétique concernant les diﬀérentes variantes du problème de Lehmer. J’ai pris
le temps de me confronter à ces sujets classiques pour approfondir ma connaissance
du domaine, avant de m’orienter progressivement vers les objets modulaires qui sont
au centre des recherches actuelles.

Les chemins pris pour étudier les points de petite hauteur suivent le plus sou-
vent un schéma façonné par Liouville au milieu du xixe siècle et qui, sans cesse
perfectionné depuis, a permis de démontrer de nombreux résultats d’approximation
diophantienne ou de transcendance. L’analyse p-adique joue ici un rôle privilégié :
elle permet de traduire sous une forme métrique des résultats profonds de la théorie
algébrique des nombres, aﬁn d’extrapoler les propriétés d’annulation de polynômes
auxiliaires construits grâce à un lemme de Siegel.

On peut dans certains cas estimer la hauteur plus directement en la décomposant
en une somme de contributions locales qu’on étudie séparément. Il faut pour cela
disposer d’informations p-adiques particulièrement fortes, ou encore les consolider
artiﬁciellement à l’aide d’un procédé d’« accélération p-adique » ou d’un théorème
d’équidistribution.

Le premier chapitre est consacré à des estimations géométriques pour la hauteur
canonique construite par Néron et Tate sur les variétés abéliennes. Dans la foulée
des résultats de ma thèse, je donne une forme « eﬀective » de la conjecture de
Bogomolov pour les sous-variétés d’une variété abélienne, sous une conjecture de
Serre concernant ses places de réduction ordinaire. Dans le cas des hypersurfaces,
j’obtiens un résultat inconditionnel en compensant la perte d’information p-adique
par une propriété algébrique locale.

Le second chapitre rassemble des résultats impliquant hauteurs et courbes el-
liptiques. On donne d’abord une réponse positive au problème de Lehmer elliptique
dans le cas galoisien, ainsi qu’une minoration de la hauteur canonique sur les puis-
sances d’une courbe elliptique, qui découlent tous deux d’un théorème de comptage
prouvé par Masser à la ﬁn des années 80. On s’intéresse ensuite aux corps engendrés
par une inﬁnité d’invariants modulaires associés à des courbes elliptiques à multi-
plications complexes, et on montre que certains de ces corps satisfont la propriété
(B) introduite par Bombieri et Zannier pour étudier la version relative du problème
de Lehmer sur les corps de nombres.

Le troisième chapitre traite de la hauteur canonique introduite par Denis sur les
modules de Drinfeld. Le contexte est celui des corps de fonctions de dimension 1, ce
qui exclut d’emblée toute implication géométrique. On montre d’abord l’analogue
d’un résultat de Habegger portant sur les corps engendrés par la torsion d’un module
de Drinfeld de rang 2 non exceptionnel. Puis on décrit quelques résultats nouveaux
au sujet du pendant drinfeldien de la conjecture de Lehmer. Celle-ci est vériﬁée dans
le cas des extensions purement inséparables pour les modules admettant une place

INTRODUCTION 7

supersingulière. Sans hypothèse sur le point considéré, il est possible de donner une
borne à la Dobrowolski pour les modules à multiplications complexes, et une borne
polynomiale pour les modules quelconques.

Les travaux présentés ici suivent l’ordre chronologique approximatif de leur réa-
lisation. Chacun des trois chapitres est autonome. Il commence avec une liste des
articles décrits, et se termine par une bibliographie séparée précédée d’une brève
discussion des perspectives ouvertes par ces recherches.

Chapitre 1

Minorations géométriques sur les variétés abéliennes

Les travaux décrits dans ce chapitre se situent dans le prolongement de ma
thèse. Ils visent à établir une forme « eﬀective » de la conjecture de Bogomolov
démontrée par Ullmo à la ﬁn des années 90. Cette version eﬀective s’applique à une
conjecture formulée indépendamment par Pink et Zilber, et qui décrit l’intersection
d’une variété plongée dans une variété abélienne avec ses sous-groupes algébriques
de codimension suﬃsamment grande.

Travaux présentés

[1] « Minoration du minimum essentiel sur les variétés abéliennes », Comment. Math.
Helv. 85 (2010), 775-812.

[2] « Un théorème de zéros dans les groupes algébriques commutatifs », Publ. Math.
Besançon 1 (2014), 35-44.

[3] « Petits points des hypersurfaces d’une variété abélienne », Int. Math. Res. Not.
2 (2012), 339-359.

1. Le problème de Bogomolov eﬀectif

Les questions qui m’ont intéressé au cours de ma thèse et dans les années qui ont
suivi trouvent leur origine dans une conjecture formulée par Bogomolov [Bog80].
Celle-ci aﬃrme la discrétion de la métrique induite par la hauteur de Néron-Tate
sur une courbe algébrique de genre au moins 2.

Démontrée par Ullmo [Ull98], la conjecture de Bogomolov a été rapidement
généralisée par Zhang [Zha98] aux sous-variétés des variétés abéliennes. Sous sa
formulation la plus classique, le théorème de Zhang montre le caractère sporadique
des points de petite hauteur canonique dans une sous-variété, à condition que celle-ci
ne soit pas « de torsion », c’est-à-dire qu’elle ne soit pas une composante d’un sous-
groupe algébrique de la variété abélienne dans laquelle elle est plongée. Il fournit

9

10 1. MINORATIONS SUR LES VARIÉTÉS ABÉLIENNES

également une nouvelle preuve de la conjecture de Manin-Mumford démontrée par
Raynaud [Ray83] quinze ans plus tôt.

Peu après, David et Philippon [DP99] ont donné une version explicite du théo-
rème de Zhang, en minorant le minimum essentiel des sous-variétés qui ne sont pas
de torsion. Comme l’avaient prévu Bombieri et Zannier [BZ96], leur résultat est
uniforme : si la sous-variété n’est pas le translaté d’une variété de torsion, son mi-
nimum essentiel est minoré uniquement en fonction de son degré et de la variété
abélienne ambiante.

Les estimations de David et Philippon étaient loin d’être optimales, et ils ont eux-
mêmes formulé un peu plus tard des conjectures précises à ce sujet (voir [DP07]).
L’amélioration des bornes n’a pas tardé à devenir un enjeu important. Rémond
[Rém00] a d’abord montré comment utiliser la minoration du minimum essentiel
pour donner une version explicite de la conjecture de Mordell démontrée par Faltings
[Fal83]. Il est apparu qu’une optimisation de la borne de David et Philippon en
la hauteur de Faltings de la variété ambiante (telle qu’ils l’ont établie pour les
puissances de courbes elliptiques dans [DP07]) permettait d’éliminer cette hauteur
de la borne sur le nombre de points rationnels d’une courbe algébrique de genre
supérieur à 2.

À la suite des résultats précurseurs de Bombieri, Masser et Zannier [BMZ99], un
nouveau champ d’application s’est ouvert pour ce type d’estimation « géométrique ».
Selon la voie explorée par Habegger et Viada, une minoration précise (et « quasi-
optimale ») du minimum essentiel en le degré de la sous-variété permet de donner
une réponse positive à une conjecture formulée indépendamment par Zilber [Zil02]
et par Pink [Pin05] dans le cas des courbes plongées dans une variété abélienne, et
qui a depuis été démontrée par Habegger et Pila [HP16].

Conjecture 1.1 (Pink, Zilber). Soient A une variété abélienne et C une courbe
tracée dans A. Si C n’est pas incluse dans un sous-groupe algébrique strict de A, il
y a un nombre ﬁni de points de C qui appartiennent à un sous-groupe algébrique de
A de codimension au moins 2.

Remarquons que cet énoncé renforce la conjecture de Manin-Mumford pour les
courbes considérées, et qu’il s’y réduit si la variété ambiante est simple. C’est lorsque
celle-ci a beaucoup de facteurs simples que la conjecture de Pink et Zilber prend tout
son sens. On renvoie à Chambert-Loir [CL12] pour plus de détails sur ce problème.

2. Résultats pour les variétés banales

Les techniques développées dans ma thèse permettaient essentiellement de prou-
ver une forme « eﬀective » de la conjecture de Bogomolov, sous une conjecture de
Serre concernant les places de réduction ordinaire d’une variété abélienne. Elles
étaient inspirées par l’approche d’Amoroso et David [AD03] sur l’analogue torique,
et reposaient en grande partie sur les propriétés p-adiques des points de torsion des
variétés abéliennes, qui peuvent s’interpréter de façon galoisienne via la théorie de
Raynaud [Ray74] ou en passant par les groupes formels.

Seuls les cas de petite codimension avaient été traités dans ma thèse, l’obstruc-
tion pour la codimension quelconque provenant de l’absence dans le cas général d’un
relèvement du Frobenius en caractéristique nulle. Ce défaut rendait particulièrement

2. RÉSULTATS POUR LES VARIÉTÉS BANALES 11

délicate la phase dite de « descente » qui clôt le schéma de preuve utilisé ici. J’ai
commencé par développer une combinatoire spéciﬁque, et en l’associant à l’approche
« équivariante » introduite par Amoroso [Amo07] dans l’étude du cas torique, j’ai
pu achever ce travail.

Commençons par donner quelques précisions sur le minimum essentiel. Introduit
par Szpiro, il peut s’interpréter comme une mesure de la hauteur d’une variété, qui
permet de quantiﬁer précisément la répartition de ses points de petite hauteur. On
se donne une variété abélienne A de dimension g déﬁnie sur ¯Q, plongée dans un
espace projectif et munie de la hauteur de Néron-Tate associée qu’on notera ˆh.

Définition 1.2. Soit V une sous-variété de A. Le minimum essentiel de V , noté
ˆµess(V ), est l’inﬁmum des réels h tels que {P ∈ V ( ¯Q) , ˆh(P ) ≤ h} est Zariski-dense
dans V .

Le théorème de Zhang décrit précisément les sous-variétés de A pour lesquelles le
minimum essentiel s’annule : ce sont les translatés d’une sous-variété abélienne par
un point de torsion.

On ﬁxe désormais un corps de nombres K sur lequel A est déﬁnie. Rappelons
qu’un idéal premier p de OK de caractéristique résiduelle p est dit ordinaire si
A est de bonne réduction en p, et si le groupe de p-torsion sur ¯Fp de la variété
réduite est de rang maximal (égal à g). Suivant Chambert-Loir [CL12], on dit
que A est « banale » si ses premiers ordinaires ont une densité naturelle égale à 1
(quitte à étendre le corps de déﬁnition). Serre conjecture que toute variété abélienne
déﬁnie sur ¯Q est banale ; c’est notamment le cas des produits arbitraires de courbes
elliptiques, de surfaces abéliennes et de variétés CM. Dans [1], j’obtiens le résultat
« quasi-optimal » suivant :

Théorème 1.3. Supposons que A soit banale. Si V n’est pas incluse dans le
translaté d’une sous-variété abélienne stricte de A :

ˆµess(V ) ≫A 1

deg(V )
 1
codim(V ) log (2deg(V ))g8g .

Le symbole ≫A signiﬁe que l’inégalité est vraie à condition de multiplier le membre
de droite par un réel strictement positif dépendant de A. Le facteur logarithmique
devrait conjecturalement disparaître. Il est inhérent à la méthode diophantienne et
sans importance dans les applications.

En utilisant cette estimation et le théorème de « hauteur bornée » de Habegger
[Hab09], Viada [Via10] donne une réponse à la conjecture 1.1 dans le cas des
variétés banales.

Corollaire 1.4 (Viada). Si A est banale, toute courbe de A qui n’est pas incluse
dans un sous-groupe algébrique strict admet un nombre ﬁni de points appartenant à
un sous-groupe algébrique de codimension au moins 2.

En suivant des chemins similaires, Checcoli, Veneziano et Viada ([CVV14] puis
[CVV16]) ont obtenu des extensions partielles de ce résultat à la dimension supé-
rieure.

La preuve du théorème 1.3 procède selon un schéma classique d’approximation
diophantienne, dont une étape clé consiste habituellement à relier le degré d’un

12 1. MINORATIONS SUR LES VARIÉTÉS ABÉLIENNES

fermé algébrique à celui d’un polynôme d’interpolation en utilisant un « lemme de
zéros ».

Amoroso et David [AD03] avaient annoncé une version très générale de ce ré-
sultat, valable dans le cadre des groupes algébriques commutatifs et recourant au
formalisme des « dessous d’escaliers » pour prendre en charge la question des multi-
plicités. Ils en avaient donné une démonstration dans le cas torique sans multiplicité,
suﬃsant pour les applications qu’ils avaient en vue.

Dans [2], je donne une preuve de ce lemme de zéros dans les groupes algébriques
commutatifs, inspirée de travaux classiques de Philippon qui mélangent algèbre com-
mutative, théorie de l’intersection et des outils combinatoires assez ﬁns.

On peut notamment en déduire l’estimation suivante, qui est utilisée au cours
de la preuve du théorème 1.3 ([1, Lemme 4.3]).

Proposition 1.5. Supposons que Z soit un fermé algébrique de A incomplète-
ment déﬁni par des polynômes de degré au plus L. On a l’inégalité :

deg(Z) ≪A L
codim(Z).

Notons que c’est la stratégie équivariante d’Amoroso qui permet de se ramener à
cette version simple découlant d’un théorème de Philippon [Phi86, Proposition 3.3].
Pour une utilisation de la forme plus sophistiquée démontrée dans [2], on renvoie à
[Gal10, Théorème 6.1].
 3. Le cas des hypersurfaces

Il était naturel à ce stade de pousser un peu plus les méthodes connues pour ob-
tenir une minoration inconditionnelle, celle-ci entraînant immédiatement une preuve
complète de la conjecture 1.1.

Si p est un idéal premier de OK et p désigne sa caractéristique résiduelle, la
principalité locale de l’idéal de déﬁnition d’une hypersurface permet de faire contri-
buer collectivement les points d’un sous-groupe de p-torsion de A dans le schéma
diophantien. On peut alors se contenter de propriétés p-adiques plus faibles que
dans le cas ordinaire, mais valables pour presque tout p. Dans [3], j’obtiens ainsi le
théorème suivant.

Théorème 1.6. Soit V une hypersurface de A qui n’est pas le translaté d’une
sous-variété abélienne. On a :

ˆµess(V ) ≫A 1

deg(V ) log (2deg(V )
)2g .

Le cœur de mon approche du problème de Bogomolov est d’utiliser les propriétés
de ramiﬁcation de la p-torsion d’une variété abélienne pour un nombre premier p
bien choisi, puis d’en déduire que la variété V est « proche p-adiquement » de ses
translatés par certains points de p-torsion (où p est un idéal premier divisant p).
Si le minimum essentiel de V est trop petit, ceci permet d’extrapoler les propriétés
d’annulation d’un polynôme d’interpolation de V construit grâce à un lemme de
Siegel, et d’arriver à une contradiction en comptant les composantes irréductibles
de son lieu d’annulation.
 3. LE CAS DES HYPERSURFACES 13

Dans le cas où p est une place de réduction ordinaire, les estimations obtenues
en examinant la structure de schéma en groupe associée au groupe de p-torsion A[p]
(donnée par exemple dans Mumford [Mum74, III]) sont particulièrement favorables.
Elles sont même analogues à la situation torique, pour peu qu’on se restreigne au
sous-groupe Gp de A[p] annulé modulo p. Pour leur donner corps, ﬁxons un système
de paramètres (t1, . . . , tg) au voisinage de 0 (le neutre de A). Si P ∈ Gp est dans
l’ouvert de déﬁnition du système de paramètres, on a ([Gal10, Corollaire 2.9]) :

∀v | p, ∀ 1 ≤ i ≤ g : |ti(P )|v ≤ p− 1
p−1 ,

où v est une place d’une extension ﬁnie de K sur laquelle P est déﬁni.

Lorsque le p-rang chute, les propriétés de ramiﬁcation de la p-torsion se dé-
gradent fortement. Un théorème classique d’Ogus permet toutefois d’éviter l’annu-
lation du p-rang pour un ensemble de premiers PA de densité 1. En s’appuyant sur
les propriétés locales ﬁnes de la structure de schéma en groupe de la p-torsion, on
peut alors construire un sous-groupe non nul Hp de A[p] (pour p ∈ PA), qui véri-
ﬁe même des estimations encore plus fortes à condition de considérer un système
« tordu » de paramètres (t1,p, . . . , tg,p). Si P ∈ Hp et v | p dans un corps de déﬁnition
de P ([3, Proposition 3.6]) :

|t1,p(P )|v ≤ p− 1
p−1 et ∀ 2 ≤ i ≤ g : |ti,p(P )|v ≤ p
−1.

Mais dès qu’on se restreint à un sous-groupe strict de Gp, la machine diophantienne
se « grippe » et le gain dans l’extrapolation reste bloqué au niveau de l’interpolation.

En examinant avec soin les propriétés du groupe formel de la variété abélienne
en caractéristique p, on peut aussi donner des estimations plus faibles mais incon-
dionnelles, qui s’avèrent décisives ici ([3, Proposition 3.1]).

Lemme 1.7. Soit α le p-rang de la réduction de A modulo p et P ∈ Gp dans
l’ouvert de déﬁnition de (t1, . . . , tg). On a :

∀v | p, ∀ 1 ≤ i ≤ g : |ti(P )|v ≤ p
− 1
pg−α+1 .

L’idée diophantienne qui permet d’exploiter au mieux ces propriétés est la sui-
vante : on interpole directement sur le translaté de la variété de départ par un
certain Gp ; puis en utilisant la formule de Leibniz, on extrapole à un ordre plus
grand qui serait même théoriquement inﬁni sans certaines complications techniques
liées à l’arithmétique et à la géométrie des variétés abéliennes.

Cette stratégie repose sur la principalité locale de l’idéal de déﬁnition d’une
hypersurface (le caractère local de cette propriété étant d’ailleurs insuﬃsamment
souligné dans [3]). Celle-ci permet de factoriser la section d’interpolation dans un
quotient adéquat, et ﬁnalement de rassembler les contributions isolées des diﬀérents
éléments de Gp.

J’ai ensuite essayé d’étendre la validité de ce théorème à la codimension quel-
conque, en utilisant des suites régulières d’interpolation et des outils de la théorie de
l’intersection arithmétique. Mais les bornes classiques d’interpolation géométrique,
et surtout arithmétique, telles qu’on peut les déduire par exemple des travaux de
Chardin et Philippon [CP99], sont inopérantes dans cette situation. Elles s’adaptent

14 1. MINORATIONS SUR LES VARIÉTÉS ABÉLIENNES

notamment assez mal aux fermés fortement réductibles qui apparaissent dans le
schéma diophantien.

La démonstration récente par Habegger et Pila de la conjecture 1.1 a largement
modiﬁé la donne sur ces questions. Ils ont montré qu’en utilisant l’o-minimalité, on
pouvait se contenter d’une minoration « arithmétique » de la hauteur (comme celle
que fournit le théorème classique de Masser [Mas86]) bien éloignée de ce que prédit
l’analogue du problème de Lehmer sur les variétés abéliennes. Dans ce contexte,
la résolution inconditionnelle du problème de Bogomolov eﬀectif est devenue moins
urgente.
 4. Perspectives

L’analogue torique du problème de Bogomolov a rebondi avec la contribution
d’Amoroso et Viada [AV09], qui ont grandement simpliﬁé l’approche diophantienne
usuelle en associant à la majoration classique (par Chardin [Cha88]) de la fonction
de Hilbert géométrique une minoration plus spéciﬁque (dûe à Chardin et Philippon
[CP99]). Une autre idée importante apparaissant en ﬁligrane dans leur travail est
que les techniques de transcendance permettent de majorer « gratuitement » le degré
d’une hypersurface contenant les points de petite hauteur dans la conjecture de
Bogomolov.

J’ai essayé sans succès d’adapter leur nouveau point de vue aux variétés abé-
liennes, et je me suis convaincu que celui-ci n’avait essentiellement aucune incidence
sur la situation métrique (p-adique), qui est pour l’instant le facteur limitant dans
le cadre abélien.

Ces idées pourraient cependant féconder des questions connexes, comme le laisse
espérer le travail récent de Martínez-Metzmeier [MM15] qui borne la torsion des
sous-variétés des tores. Son résultat améliore signiﬁcativement les estimations exis-
tantes, en particulier celles qui sont issues des derniers résultats sur la conjecture
de Bogomolov. Nous cherchons maintenant à transposer son théorème aux variétés
abéliennes, en combinant l’approche de Serre et Hindry sur la conjecture de Manin-
Mumford, les idées introduites par Beukers et Smyth [BS01] dans le cas des courbes
du tore, et la double estimation des fonctions de Hilbert suivant la voie inaugurée
par Amoroso et Viada.

Dans ce contexte, il serait précieux de disposer d’une version totalement explicite
du théorème de Serre sur les homothéties dans la représentation galoisienne associée
à la torsion d’une variété abélienne. Avec A. David, nous essayons désormais de
préciser les constantes dans la preuve complète que Wintenberger [Win02] a donnée
de ce théorème.
 Bibliographie

[AD03] F. Amoroso & S. David – « Minoration de la hauteur normalisée dans
un tore », J. Inst. Math. Jussieu 2 (2003), no. 3, p. 335–381.

[Amo07] F. Amoroso – « Bogomolov on tori revisited », Prépublication (2007).

[AV09] F. Amoroso & E. Viada – « Small points on subvarieties of a torus »,
Duke Math. J. 150 (2009), no. 3, p. 407–442.

Bibliographie 15

[BMZ99] E. Bombieri, D. Masser & U. Zannier – « Intersecting a curve with al-
gebraic subgroups of multiplicative groups », Internat. Math. Res. Notices
20 (1999), p. 1119–1140.
[Bog80] F. Bogomolov – « Points of ﬁnite order on abelian varieties », Izv. Akad.
Nauk SSSR Ser. Mat. 44 (1980), no. 4, p. 782–804.
[BS01] F. Beukers & C. Smyth – « Cyclotomic points on curves », Millenial
Conference on Number Theory, May 21-26, 2000, Urbana Champaign. AK
Peters. (2001).
[BZ96] E. Bombieri & U. Zannier – « Heights of algebraic points on suvarieties
of abelian varieties », Ann. Scuola Norm. Sup. Pisa 23 (1996), no. 4,
p. 779–792.
[Cha88] M. Chardin – « Une majoration de la fonction de Hilbert et ses consé-
quences pour l’interpolation algébrique », Bull. Soc. Math. France 117
(1988), p. 305–318.
[CL12] A. Chambert-Loir – « Relations de dépendance et intersections excep-
tionnelles », Séminaire Bourbaki, Astérisque 348 (2012), p. 149–188.
[CP99] M. Chardin & P. Philippon – « Régularité et interpolation », J. Alge-
braic Geom. 8 (1999), p. 471–481.
[CVV14] S. Checcoli, P. Veneziano & E. Viada – « On torsion anomalous
intersections », Rend. Lincei Mat. Appl. 1 (2014), no. 25, p. 1–36.

[CVV16] , « Some explicit cases of the torsion anomalous conjecture », À
paraître aux Trans. Amer. Math. Soc. (2016).
[DP99] S. David & P. Philippon – « Minoration des hauteurs normalisées des
sous-variétés des tores », Ann. Scuola Norm. Sup. Pisa 28 (1999), no. 3,
p. 489–543.
[DP07] , « Minoration des hauteurs normalisées des sous-variétés des puis-
sances de courbes elliptiques », Internat. Math. Res. Papers (2007).
[Fal83] G. Faltings – « Endlichkeitssätze für abelsche Varietäten über Zah-
lenkörpern. », Invent. Math. 73 (1983), p. 349–366.
[Gal10] A. Galateau – « Le problème de Bogomolov eﬀectif sur les variétés
abéliennes », Algebra Number Theory 4 (2010), no. 5, p. 547–598.
[Hab09] P. Habegger – « Intersecting subvarieties of abelian varieties with alge-
braic subgroups of complementary dimension », Invent. Math. 176 (2009),
no. 2, p. 405–447.
[HP16] P. Habegger & J. Pila – « O-minimality and certain anomalous inter-
sections », À paraître aux Ann. Sci. École Norm. Sup. (2016).
[Mas86] D. Masser – « Letter to D. Bertrand », (1986).
[MM15] C. Martìnez-Metzmeier – « The number of maximal torsion cosets in
subvarieties of tori », Prépublication (2015).
[Mum74] D. Mumford – Abelian Varieties, Tata Lecture Notes. Cambridge Uni-
versity Press, 1974.
[Phi86] P. Philippon – « Lemmes de zéros dans les groupes algébriques commu-
tatifs », Bull. Soc. Math. France 114 (1986), p. 353–383.

16 1. MINORATIONS SUR LES VARIÉTÉS ABÉLIENNES

[Pin05] R. Pink – « A common generalization of the conjectures of André-Oort,
Manin-Mumford and Mordell-Lang », Prépublication (2005).

[Ray74] M. Raynaud – « Schémas en groupes de type (p, . . . , p) », Bull. Soc.
Math. France 2 (1974), p. 241–280.

[Ray83] , « Courbes sur une variété abélienne et points de torsion », Invent.
Math. 71 (1983), p. 207–233.

[Rém00] G. Rémond – « Décompte dans une conjecture de Lang », Invent. Math.
142 (2000), no. 3, p. 513–545.

[Ull98] E. Ullmo – « Positivité et discrétion des points algébriques des courbes »,
Ann. of Math. 147 (1998), p. 167–179.

[Via10] E. Viada – « Lower bounds for the normalized height and non-dense
subsets of subvarieties of abelian varieties », Int. J. Number Theory 6
(2010), no. 3, p. 471–499.

[Win02] J.-P. Wintenberger – « Démonstration d’une conjecture de Lang dans
des cas particuliers », J. reine angew. Math. 553 (2002), p. 1–16.

[Zha98] S. Zhang – « Equidistribution of small points on abelian varieties », Ann.
of Math. 147 (1998), p. 159–165.

[Zil02] B. Zilber – « Exponential sums equations and the Schanuel conjecture »,
J. London Math. Soc. 65 (2002), no. 1, p. 27–44.

Chapitre 2

Problèmes de hauteur et courbes elliptiques

Les questions abordées ici concernent des minorations « arithmétiques » de hau-
teurs en lien avec les courbes elliptiques. On présente d’abord des résultats concer-
nant la hauteur de Néron-Tate sur les courbes elliptiques et leurs produits, en di-
rection du problème de Lehmer sur les variétés abéliennes. On explique ensuite
comment la théorie des courbes elliptiques à multiplication complexe permet de
construire des extensions inﬁnies de Q avec une structure galoisienne compliquée,
sur lesquelles la hauteur de Weil vériﬁe la propriété (B) introduite par Bombieri et
Zannier.
 Travaux présentés

[4] « Some consequences of Masser’s counting theorem on elliptic curves », à paraître
au Math. Z., 18 pages. En collaboration avec V. Mahé.

[5] « Small height in ﬁelds generated by singular moduli », Proc. Amer. Math. Soc.
144 (2016), 2771-2786.

1. Le problème de Lehmer sur les variétés abéliennes

Les recherches sur les points de petite hauteur trouvent leur origine dans une
question posée par Lehmer [Leh33] à propos de la mesure de Mahler des nombres
algébriques non cyclotomiques. Reformulé en termes plus modernes, le problème de
Lehmer revient à minorer de façon optimale en fonction de son degré la hauteur
de Weil d’un nombre algébrique qui n’est pas une racine de l’unité. Cette question
n’est toujours pas entièrement résolue, malgré quelques avancées notoires (parmi
lesquelles Smyth [Smy71], ou plus récemment Borwein, Dobrowolski et Mossin-
ghoﬀ [BDM07]). Dobrowolski [Dob79] s’est rapproché de la borne conjecturée à
un facteur logarithmique près, ce facteur d’erreur étant sans conséquence dans les
nombreuses applications de son théorème.

17

18 2. HAUTEURS SUR LES COURBES ELLIPTIQUES

On ﬁxe désormais une variété abélienne A de dimension g, déﬁnie sur un corps
de nombres K et plongée dans un espace projectif. Si P ∈ A( ¯K) est d’ordre inﬁni,
on peut aussi chercher une minoration optimale de sa hauteur de Néron-Tate ˆh(P ).
L’analogue du problème de Lehmer dans les variétés abéliennes peut se formuler de
la façon suivante.

Conjecture 2.1. Si P est de degré d := [K(P ) : K] et n’a aucun multiple dans
une sous-variété abélienne stricte :
ˆh(P ) ≫A 1

d 1
g .

Lorsque la variété est à multiplication complexe (CM), David et Hindry [DH00]
montrent que cette borne est vraie à un facteur logarithmique près. Leur théorème
est l’analogue de l’estimation de Dobrowolski sur les nombres algébriques et il géné-
ralise un résultat de Laurent [Lau83] sur les courbes elliptiques. Le schéma général
de la preuve est identique : il repose sur l’existence d’un relèvement du Frobenius
dans l’anneau des endomorphismes en caractéristique nulle, pour une quantité suﬃ-
sante d’idéaux premiers. Mais sans hypothèse sur la variété abélienne, cette propriété
n’est plus garantie et les meilleurs résultats connus sont encore très éloignés de la
borne espérée, ce qui a notamment pour eﬀet de limiter l’attaque via Lehmer de la
conjecture de Pink et Zilber.

L’approche la plus eﬃcace à ce jour pour minorer la hauteur de Néron-Tate
d’une variété abélienne sans CM est un théorème de Masser (la lettre non publiée
[Mas86] pour le cas général, et [Mas89] pour les courbes elliptiques), qui compte le
nombre de points, déﬁnis sur un corps de nombres ﬁxé, dont la hauteur est majorée
par une borne « de type Lehmer ». Il en déduit immédiatement une minoration de
la hauteur de Néron-Tate.

Théorème 2.2 (Masser). Si P ∈ A( ¯K) est d’ordre inﬁni et de degré d, on a
l’inégalité suivante : ˆh(P ) ≫A 1
d2g+1 log(2d)2g .

Le théorème de comptage donne également des informations très utiles sur la torsion
des variétés abéliennes.

Avec Mahé, nous avons d’abord cherché à minorer la hauteur de Néron-Tate par
voie diophantienne directe en utilisant les propriétés du polynôme caractéristique de
l’endomorphisme de Frobenius. Notre stratégie produit des résultats, au moins en
dimension 1, mais ceux-ci sont un peu plus faibles que la borne de Masser. Comme
on le verra plus bas, la même approche permet d’obtenir une borne polynomiale
pour la hauteur canonique d’un module de Drinfeld en rang quelconque.

2. Le cas des extensions galoisiennes

Impressionnés par la robustesse du théorème de Masser, nous avons essayé de
l’utiliser pour minorer la hauteur dans certaines situations particulières, en particu-
lier celle des extensions galoisiennes. La question analogue sur les corps de nombres
a été traitée par Amoroso et David [AD99] comme corollaire d’une généralisation
à la dimension quelconque du théorème de Dobrowolski.

3. LA PROPRIÉTÉ (B) 19

Dans le cadre des variétés abéliennes, la pertinence de ce point de vue est limitée
au cas CM, pour lequel la borne de Dobrowolski est connue. Dans [4], suivant les
idées d’Amoroso et David, nous avons d’abord combiné le théorème de comptage de
Masser et des calculs de volume pour la métrique euclidienne induite par la hauteur
de Néron-Tate, aﬁn de minorer la hauteur sur les puissances d’une courbe elliptique
E.
 Théorème 2.3. Si P ∈ Eg( ¯K) est de degré d et n’a aucun multiple dans une
sous-variété abélienne stricte :

ˆh(P ) ≫E,g 1

d
1+ 2
g log(2d) 2
g .

Ceci permet de s’approcher à « une puissance ε près » de la borne de Lehmer dans
le cas galoisien sur E. Une utilisation plus directe du comptage de Masser donne un
résultat un peu meilleur, où le facteur d’erreur est logarithmique.

Pour faire disparaître ce facteur d’erreur, nous avons mis en place une nouvelle
méthode où le comptage de Masser est combiné avec des bornes issues des tra-
vaux de Serre sur les représentations galoisiennes associées à la torsion des courbes
elliptiques. Le principal résultat de [4] est le suivant.

Théorème 2.4. Soit P ∈ E( ¯K) d’ordre inﬁni tel que l’extension K(P )/K est
galoisienne de degré d. On a : ˆh(P ) ≫E 1
d .

Le cas CM se traite comme pour les corps de nombres. Le théorème de David
et Hindry fournit une minoration plus forte dès qu’il existe deux conjugués de P
linéairement indépendants sur End(E). Si cela n’est pas le cas, une descente kum-
merienne et la borne « relative » de Ratazzi [Rat04] permettent de conclure. Les
techniques employées ici donnent même naturellement l’inégalité plus ﬁne suivante,
pour tout ε > 0 et sous les hypothèses du théorème 2.4 :

ˆh(P ) ≫E,ε 1

d 1
2 +ε .

Dans le cas non CM, le théorème de l’image ouverte de Serre [Ser72] borne
eﬃcacement l’ordre d’un point de torsion déﬁni sur une extension galoisienne de K
en fonction de son degré. Ceci suﬃt à estimer la partie kummerienne de l’extension.
La partie restante étant « écrasée » grâce au comptage de Masser, on peut assez vite
conclure avec le théorème 2.2.

Comme sur les corps de nombres, il est possible de pousser un peu les méthodes
pour obtenir une minoration « de type Lehmer » lorsque le degré de la clôture
galoisienne de K(P )/K est majoré par une puissance ﬁxe de d, mais cette puissance
doit rester strictement inférieure à 2 dans le cas non CM.

3. La propriété (B)

Si le problème de Lehmer est toujours ouvert sur les corps de nombres comme
sur les variétés abéliennes, on sait qu’il est possible dans certaines conﬁgurations de
donner une minoration beaucoup plus forte de la hauteur.

20 2. HAUTEURS SUR LES COURBES ELLIPTIQUES

Schinzel [Sch73] a été le premier à mettre ce phénomène en évidence, en mi-
norant par une constante absolue la hauteur de Weil d’un nombre algébrique non
cyclotomique et totalement réel. Amoroso et Dvornicich [AD00] ont ensuite montré
un résultat du même ordre sur la clôture abélienne Qab de Q, qui a vite été étendu
par Amoroso et Zannier [AZ00] à la clôture abélienne Kab d’un corps de nombres K
quelconque. Ces derniers auteurs ont également formulé une version « relative » de
la conjecture de Lehmer, où le degré absolu est remplacé par le degré relatif sur Qab,
et dont on peut démontrer des formes faibles particulièrement utiles (notamment en
direction de la conjecture de Pink et Zilber).

Bombieri et Zannier [BZ01] ont lancé l’étude systématique de ces corps en
posant la déﬁnition suivante.

Définition 2.5. On dit qu’une extension K de Q vériﬁe la propriété de Bogo-
molov, ou propriété (B), s’il existe c(K) > 0 telle que :

∀x ∈ K \ µ∞ : h(x) ≥ c(K).

Les corps de nombres satisfont la propriété (B) en vertu du « théorème de Nor-
thcott. » Bombieri et Zannier donnent également un analogue ultramétrique du
théorème de Schinzel pour les corps à degré local uniformément borné au-dessus
d’un nombre premier ﬁxé. Checcoli [Che13] a depuis montré que leur théorème
s’applique notamment aux extensions galoisiennes de Q dont le groupe de Galois est
d’exposant ﬁni.

Récemment, Amoroso, David et Zannier [ADZ14] ont uniﬁé le cas abélien et
le critère de Checcoli, en traitant le cas des extensions galoisiennes d’un corps de
nombres dont le groupe de Galois est d’exposant ﬁni sur son centre. Ils ont aussi
proposé des conjectures à peine plus ambitieuses, mais qui semblent encore hors de
portée avec les techniques actuelles.

La propriété (B) ne se limite pas à ce type de conﬁguration galoisienne. Habegger
[Hab13] a ainsi prouvé que le corps engendré par la torsion d’une courbe elliptique
déﬁnie sur Q satisfait la propriété (B). La structure galoisienne de ce corps peut
être précisée grâce au théorème de l’image ouverte de Serre [Ser72], et elle sort du
cadre traité dans [ADZ14] pourvu que E ne soit pas de type CM.

L’exemple le plus simple en dehors du champ exploré par Amoroso, David et
Zannier est le suivant. On considère une famille (Kn)n∈N de corps quadratiques
deux-à-deux distincts, et pour tout n, on se donne une extension abélienne Ln de
Kn.
Question 2.6. Le compositum des (Ln)n∈N vériﬁe-t-il la propriété (B) ?

D’après Bombieri et Zannier [BZ01], on sait que le « théorème de Northcott »
s’applique au compositum des (Kn)n∈N, qui a donc la propriété (B).

4. Corps engendrés par une famille d’invariants singuliers

On peut expliciter la question précédente en considérant, pour tout premier p, le
corps quadratique imaginaire Kp := Q(
√−p) et son corps de classe de Hilbert Lp :=
Kp(jp), où jp est l’invariant modulaire d’une courbe elliptique ayant multiplication
complexe par l’anneau des entiers de Kp.

5. PERSPECTIVES 21

Dans [5], je montre que de nombreux sous-corps du compositum des (Lp)p∈P
vériﬁent la propriété (B).

Théorème 2.7. Pour tout premier q ≥ 3, il existe un ensemble Pq de densité
(de Dirichlet) 1
4 tel que le compositum LPq des (Lp)p∈Pq a la propriété (B).

Les Pq sont largement distincts, dans le sens où, pour deux premiers q ̸= q′, l’en-
semble Pq ∩ Pq′ est de densité 1
8 .

La preuve de ce théorème est basée sur la théorie du corps de classe, selon
laquelle les premiers inertes d’un corps de nombres sont totalement décomposés
dans son corps de Hilbert. Le théorème de la progression arithmétique de Dirichlet
permet d’aﬃrmer que l’ensemble Pq des premiers p tels que q soit inerte dans Kp est
de densité au moins 1
4 . On se retrouve alors dans la situation étudiée par Bombieri
et Zannier avec un degré local borné, et il est possible de minorer la hauteur de
façon totalement explicite :

∀x ∈ LPq \ µ∞ : h(x) ≥ log ( q
2 )

q2 + 1 .

Ces méthodes semblent toutefois impuissantes à décrire la situation dès qu’on consi-
dère des premiers totalement décomposés dans les Kp (donnant lieu à la réduction
ordinaire des courbes elliptiques CM associées).

Si les corps construits ici ont une structure locale contrôlée en un certain nombre
premier, ils sortent du cadre galoisien décrit dans [ADZ14]. En combinant le théo-
rème de Kronecker-Weber et un résultat de Pappalardi [Pap95] sur l’exposant du
groupe de classe d’un corps quadratique imaginaire, je montre qu’ils sont galoisiens
sur Q avec un groupe de Galois d’exposant inﬁni sur son centre.

La même méthode fonctionne avec des familles de corps de Hilbert de corps
quadratiques réels (ou encore avec des familles mixtes). Cet exemple est peut-être
moins intéressant dans notre contexte, car si on se ﬁe à l’heuristique de Cohen-
Lenstra [CL84], le nombre de classe des corps quadratiques réels est statistiquement
beaucoup plus petit que celui des corps quadratiques imaginaires.

Plus généralement, si on considère une famille (Kn)n∈N dont le degré est unifor-
mément borné sur Q, dont les discriminants sont premiers entre eux deux-à-deux
et qui ont un nombre premier inerte en commun, le compositum de leurs corps
de Hilbert vériﬁe la propriété (B). En me basant sur des travaux de Louboutin
[Lou01], j’ai construit une famille inﬁnie de « corps cubiques simples » soumise à
ces contraintes. En notant L le compositum des corps de classe de Hilbert, j’obtiens
la minoration suivante :
 ∀x ∈ L \ µ∞ : h(x) ≥ log(2)
18 .

Il est également possible ici, en particulier sous GRH, de quantiﬁer précisément la
complexité du groupe de Galois de l’extension galoisienne L/Q.

5. Perspectives

L’amélioration du théorème 2.2, qui était ma motivation première, est un déﬁ
qui ne pourra probablement pas être relevé sans idées nouvelles.

22 2. HAUTEURS SUR LES COURBES ELLIPTIQUES

Un prolongement naturel de [4] serait l’étude du problème de Lehmer sur les
variétés abéliennes dans le cas galoisien. La stratégie mise en place pour les courbes
elliptiques devrait donner des résultats en dimension plus grande, en associant le
théorème annoncé dans [Mas86] à des estimations classiques sur la torsion des
variétés abéliennes, telles qu’elles sont par exemples présentées dans [HR12]. Il
serait à ce sujet intéressant de revisiter le théorème de comptage de Masser, et d’en
chercher une variante comptant les points dont la hauteur passe sous une borne de
l’ordre de celle de la conjecture 2.1.

Très récemment, Amoroso et Masser [AM16] ont annoncé une nouvelle minora-
tion bien plus forte que celle de [AD99] pour les nombres algébriques engendrant une
extension galoisienne. La preuve utilise une version relative du théorème de Dobro-
wolski en dimension supérieure, démontrée par Delsinne [Del09] et dont l’équivalent
existe sur les variétés abéliennes CM.

Au sujet de la propriété (B), de nombreux problèmes restent encore ouverts. Par
exemple, comment étendre le théorème d’Habegger [Hab13] aux courbes elliptiques
déﬁnies sur un corps de nombres quelconque, ou mieux, à une variété abélienne
quelconque ? Le premier problème est déjà épineux. En l’attente d’une généralisation
du théorème d’Elkies [Elk87] sur les premiers supersinguliers, il suppose de mettre
en place une stratégie métrique valable pour un premier p de réduction ordinaire
alors que les éléments de Frobenius ne disposent pas de propriétés de commutation
évidentes dans le groupe de Galois associé à la p-torsion.

Mon travail sur les invariants modulaires était surtout conçu comme une transi-
tion vers des problèmes concernant les points spéciaux des variétés de Shimura. Alors
que les idées de Pila et Zannier ont permis la résolution de la conjecture d’André-
Oort dans un grand nombre de cas, on peut chercher à obtenir des bornes eﬀectives
dans le prolongement du résultat de Kühne [Küh12]. Je réﬂéchis à une approche
diophantienne de ces questions basée sur les propriétés des invariants singuliers.

Avec Lebacque et Tsfasman, nous nous intéressons aux liens entre la propriété
(B) et les empilements de sphère dans la lignée de [RT90]. La construction de
familles de réseaux « asymptotiquement denses », passe par une minoration forte de
la hauteur sur des corps peu ramiﬁés de dimension inﬁnie sur Q.

Bibliographie

[AD99] F. Amoroso & S. David – « Le problème de Lehmer en dimension
supérieure », J. reine angew. Math. 513 (1999), p. 145–179.

[AD00] F. Amoroso & R. Dvornicich – « A lower bound for the height in
abelian extensions », J. Number Theory 80 (2000), p. 260–272.

[ADZ14] F. Amoroso, S. David & U. Zannier – « On ﬁelds with the Property
(B) », Proc. Amer. Math. Soc. 142 (2014), no. 6, p. 1893–1910.

[AM16] F. Amoroso & D. Masser – « Lower bounds for the height in Galois
extensions », Prépublication (2016).

[AZ00] F. Amoroso & U. Zannier – « A relative Dobrowolski lower bound
over abelian extensions », Ann. Scuola Norm. Sup. Pisa 29 (2000), no. 4,
p. 711–727.
 Bibliographie 23

[BDM07] P. Borwein, E. Dobrowolski & M. Mossinghoff – « Lehmer’s pro-
blem for polynomials with odd coeﬃcients », Ann. of Math. 166 (2007),
p. 347–366.
[BZ01] E. Bombieri & U. Zannier – « A note on heights in certain inﬁnite
extensions of Q », Rend. Mat. Acc. Lincei 12 (2001), no. 9, p. 5–14.
[Che13] S. Checcoli – « Fields of algebraic numbers with bounded local degrees
and their properties », Trans. Amer. Math. Soc. (2013), no. 365, p. 2223–
2240.
[CL84] H. Cohen & H. Lenstra – « Heuristics on class groups of number
ﬁelds », Lecture Notes in Math. 1068 (1984), p. 33–62.
[Del09] E. Delsinne – « Le problème de Lehmer relatif en dimension supérieure »,
Ann. Sci. École Norm. Sup. 42 (2009), no. 6, p. 981–1028.
[DH00] S. David & M. Hindry – « Minoration de la hauteur de Néron-Tate sur
les variétés abéliennes de type C.M. », J. reine angew. Math. 529 (2000),
p. 1–74.
[Dob79] E. Dobrowolski – « On a question of Lehmer and the number of irre-
ducible factors of a polynomial », Acta Arith. 34 (1979), p. 391–401.
[Elk87] N. Elkies – « The existence of inﬁnitely many supersingular primes for
every elliptic curve over Q », Invent. Math. 89 (1987), p. 561–567.
[Hab13] P. Habegger – « Small height and inﬁnite nonabelian extensions », Duke
Math. J. 162 (2013), no. 11, p. 2027–2076.
[HR12] M. Hindry & N. Ratazzi – « Points de torsion sur les variétés abéliennes
de type GSp », J. Inst. Math. Jussieu 11 (2012), no. 1, p. 27–65.
[Küh12] L. Kühne – « An eﬀective result of André-Oort type », Ann. of Math.
176 (2012), no. 1.
[Lau83] M. Laurent – « Minoration de la hauteur de Néron-Tate », Séminaire de
théorie des nombres de Paris, 1981-1982, Progr. Math. 38 (1983), p. 137–
152.
[Leh33] D. H. Lehmer – « Factorization of certain cyclotomic functions », Ann.
of Math. 34 (1933), p. 461–479.
[Lou01] S. Louboutin – « The exponent three class group problem for some real
cyclic cubic number ﬁelds », Proc. Amer. Math. Soc. 130 (2001), no. 2,
p. 353–361.
[Mas86] D. Masser – « Letter to D. Bertrand », (1986).
[Mas89] , « Counting points of small height on elliptic curves », Bull. Soc.
Math. France 117 (1989), p. 247–265.

[Pap95] F. Pappalardi – « On the exponent of the ideal class group of Q(
√−d) »,
Proc. Amer. Math. Soc. 123 (1995), no. 3, p. 663–671.
[Rat04] N. Ratazzi – « Théorème de Dobrowolski-Laurent pour les extensions
abéliennes sur une courbe elliptique à multiplication complexe », Internat.
Math. Res. Notices 58 (2004), p. 3122–3152.
[RT90] M. Rosenbloom & M. Tsfasman – « Multiplicative lattices in global
ﬁelds », Invent. Math. 101 (1990), p. 687–696.

24 2. HAUTEURS SUR LES COURBES ELLIPTIQUES

[Sch73] A. Schinzel – « On the product of the conjugates outside the unit circle
of an algebraic number », Acta Arith. 24 (1973), p. 385–399.

[Ser72] J. P. Serre – « Propriétés galoisiennes des points d’ordre ﬁni des courbes
elliptiques », Invent. Math. 15 (1972), p. 259–331.

[Smy71] C. Smyth – « On the product of the conjugates outside the unit circle of
an algebraic integer », Bull. Lond. Math. Soc. 3 (1971), p. 169–175.

Chapitre 3

Petite hauteur canonique sur les modules de Drinfeld

Les résultats de ce chapitre concernent pour l’essentiel les petites valeurs de la
hauteur canonique sur les modules de Drinfeld. On montre d’abord que le corps
engendré par la torsion des modules de Drinfeld « non exceptionnels » de rang
2 vériﬁe la propriété (B) pour la hauteur canonique associée (ainsi que pour la
hauteur de Weil), en appliquant la stratégie développée par Habegger sur les courbes
elliptiques. On donne ensuite des résultats partiels en direction du problème de
Lehmer sur les modules de Drinfeld, concernant les extensions inséparables. On
explique ﬁnalement comment minorer la hauteur canonique, à la Dobrowolski dans
le cas CM, et de façon polynomiale dans le cas non CM.

Travaux présentés

[6] « Hauteur et torsion des modules de Drinfeld de rang 2 », soumis en juillet 2015,
28 pages. En collaboration avec A. Pacheco.

[7] « Lower bounds for the canonical height on Drinfeld modules », soumis en juin
2016, 24 pages. En collaboration avec V. Bosser.

1. Présentation

De nombreuses facettes de la théorie des modules de Drinfeld révèlent une ana-
logie partielle entre ces objets et les variétés abéliennes. Celle-ci vaut surtout d’un
point de vue arithmétique, dans la mesure où les modules de Drinfeld classiques
sont des objets de dimension 1. Denis [Den92] a ainsi construit une « hauteur ca-
nonique » pour laquelle il a démontré un certain nombre de propriétés comparables
à celles de la hauteur de Néron-Tate. Poonen [Poo95] a ensuite déﬁni des hauteurs
locales avec lesquelles il a pu prouver l’analogue du théorème de Mordell-Weil dans
le cadre drinfeldien.

Il est facile de se convaincre que la minoration de Lehmer est vériﬁée pour la
hauteur de Weil sur un corps de fonctions. Le problème est beaucoup plus diﬃcile si
on considère la hauteur canonique ˆhφ associée à un module de Drinfeld φ, mais on

25

26 3. HAUTEUR SUR LES MODULES DE DRINFELD

peut raisonnablement formuler le pendant drinfeldien de la conjecture de Lehmer.
Fixons un corps de fonctions K en une variable sur un corps ﬁni Fq.

Conjecture 3.1. Si x ∈ ¯K est d’ordre inﬁni pour φ et de degré d := [K(x) : K] :

ˆhφ(x) ≫φ 1
d .

Le premier résultat signiﬁcatif en direction de cette conjecture est dû à Denis
[Den92], qui démontre l’analogue du théorème de Dobrowolski pour les extensions
séparables dans le module de Carlitz C.

Théorème 3.2 (Denis). Si x ∈ ¯K est d’ordre inﬁni pour C et tel que K(x)/K
soit séparable de degré d : ˆhC(x) ≫C 1
d log(2d)3 .

Son théorème a été partiellement généralisé par Demangos [Dem15] aux modules
CM. Pour les modules généraux, Ghioca [Ghi07] donne une minoration polynomiale
de la hauteur canonique moyennant une hypothèse de positivité de la hauteur locale
associée à une place non archimédienne.

On peut également trouver des sous-corps de ¯K sur lesquels la hauteur cano-
nique ˆhφ associée à un module φ est minorée par un nombre réel strictement positif
lorsqu’elle ne s’annule pas. On dit que de tels corps satisfont la propriété (Bφ).

Un premier exemple a été produit par David et Pacheco [DP08], qui ont dé-
montré que la clôture abélienne Kab de K vériﬁe (Bφ) pour tout φ. Dans le cas CM,
leur théorème a ensuite été amélioré par Bauchère [Bau15] qui a établi l’analogue
du résultat principal de [ADZ14], traitant notamment les extensions galoisiennes
dont le groupe de Galois est d’exposant ﬁni sur son centre.

2. Torsion des modules de Drinfeld non exceptionnels de rang 2

Avec Pacheco, nous avons cherché des exemples de corps vériﬁant la propriété
(Bφ) au-delà de ceux envisagés par Amoroso, David et Zannier (et étudiés par Bau-
chère dans le cas CM). À la suite du travail d’Habegger [Hab13], nous nous sommes
penchés sur le corps Ktors engendré par la ¯K-torsion d’un module de Drinfeld φ déﬁni
sur K.

Le module de Carlitz et les modules CM de rang 2 étant déjà couverts par le
résultat principal de [DP08], nous nous sommes concentrés sur les modules de Drin-
feld de rang 2 sans CM. Dans ce cadre, la distribution des premiers supersinguliers
a été étudiée par Brown [Bro92] puis précisée par C. David [Dav95].

Soit φ un module de Drinfeld de rang 2, donné par l’action suivante sur la
variable t : φt := t + gτ + ∆τ 2,
où τ est le q-Frobenius sur K et (g, ∆) ∈ K × K∗. Le j-invariant de φ est déﬁni par
la formule : j(φ) := gq+1/∆, et il caractérise la classe de ¯K-isomorphisme de φ.

Définition 3.3. On dit que φ est exceptionnel si tj(φ) est un carré dans Fq(( 1
t )).

3. LE PROBLÈME DE LEHMER POUR LES EXTENSIONS INSÉPARABLES 27

Le résultat principal de [Bro92] est l’analogue du théorème d’Elkies pour les mo-
dules non exceptionnels de caractéristique ̸= 2. Il nous permet de démontrer dans
[6] le théorème suivant.

Théorème 3.4. Si φ est un module de rang 2 non exceptionnel en caractéristique
̸= 2, le corps Ktors engendré par la ¯K-torsion de φ satisfait la propriété (Bφ).

Nous prouvons également une minoration absolue de la hauteur de Weil pour les
éléments non constants de Ktors.

La preuve de ces résultats est basée sur la stratégie de [Hab13]. Pour les modules
non exceptionnels, le théorème de Brown assure l’existence d’un premier supersin-
gulier de degré suﬃsamment grand. Les propriétés galoisiennes des modules de Tate
en un tel premier (et notamment la théorie de Lubin-Tate) permettent d’obtenir
une estimation métrique très forte, puis d’en déduire une minoration absolue pour
la hauteur canonique. Le cas « ramiﬁé » donne lieu à des complications techniques
qui sont résolues par l’analogue du théorème de l’image ouverte et des arguments
de la théorie des groupes linéaires sur les corps ﬁnis.

L’absence de places archimédiennes permet de se passer du théorème d’équidis-
tribution utilisé par Habegger dans l’étude de la hauteur de Weil. On y parvient
aussi pour la hauteur canonique grâce à un procédé d’« accélération p-adique » en
l’idéal premier p qu’on a choisi.

Poonen [Poo98] a montré que les modules de Drinfeld n’admettent pas toujours
des premiers supersinguliers, ce qui crée un contraste important avec la conjecture de
Lang et Trotter sur les courbes elliptiques. L’extension de ces bornes à la torsion des
modules exceptionnels passe donc par l’analyse des premiers ordinaires, la première
diﬃculté à résoudre apparaissant dans le cas « non ramiﬁé » pour estimer la taille
de la classe d’un élément de Frobenius dans le groupe de Galois considéré.

Au delà des résultats obtenus, ce travail m’a permis de me familiariser avec la
technicité des modules de Drinfeld, mais aussi d’étudier en détail la preuve d’Ha-
begger et de mesurer les obstacles empêchant pour l’instant sa généralisation.

3. Le problème de Lehmer pour les extensions inséparables

Les résultats connus à l’heure actuelle en direction de la conjecture 3.1 sont
plus faibles que ceux dont on dispose sur les corps de nombres et sur les courbes
elliptiques. Avec Armana et Bosser, nous avons commencé à travailler ensemble aﬁn
de réduire cet écart.

Une première limite concerne les extensions inséparables, sur lesquelles le théo-
rème principal de [Den92] ne dit rien. Dans son travail sur les modules CM, Deman-
gos parvient à exploiter leur spéciﬁcité dans un schéma diophantien. Sa borne pour
la hauteur canonique est polynomiale en le degré inséparable (sous une hypothèse
concernant la densité des premiers supersinguliers).

Un premier résultat de [7] inverse la perspective : pour les extension purement
inséparables, nous obtenons sur certains modules une borne meilleure que pour les
extensions séparables, au niveau prédit par la conjecture 3.1. Notre minoration sur
le module de Carlitz C prend la forme suivante.

28 3. HAUTEUR SUR LES MODULES DE DRINFELD

Théorème 3.5. Si x ∈ ¯K est tel que K(x)/K soit purement inséparable de
degré d :
 ˆhC(x) ≥ q−6

d .

En examinant d’un peu plus près la constante de comparaison entre hauteur de
Weil et hauteur canonique donnée dans [Den95], il est possible de remplacer q−6

par (4q)−2 dans cette inégalité.

Nous montrons aussi une estimation de la même force pour les extensions insé-
parables sur un module de Drinfeld φ qui admet au moins un premier supersingulier
p. La constante est là encore totalement explicite ; elle dépend du degré de p, ainsi
que du rang de φ, de sa hauteur et du degré d’un corps de déﬁnition. Remarquons
une nouvelle fois qu’en vertu de [Poo98], l’existence d’un premier supersingulier
n’est pas toujours garantie. Elle est notamment réalisée pour le module de Carlitz,
pour les modules de rang 2 non exceptionnels et pour les modules CM déﬁnis sur
une extension cyclique de k.

La preuve de ce théorème pour le module de Carlitz repose sur la forme très
particulière que prend la décomposition des idéaux premiers dans les extensions
purement inséparables : ceux-ci sont toujours totalement ramiﬁés. La trivialité de
l’extension résiduelle en le premier p := (t) et la forme simple de la loi du module de
Carlitz donnent lieu à une première information p-adique, qui est ensuite exploitée
par un procédé d’accélération p-adique. Si φ admet un premier supersingulier p,
on peut encore en déduire une estimation p-adique suﬃsamment forte grâce aux
propriétés du morphisme de Frobenius modulo p.

En l’absence d’un premier supersingulier, la même méthode produit une borne
plus faible mais polynomiale pour les extensions purement inséparables. On peut
également obtenir des résultats pour les extensions quelconques, où la borne décroît
exponentiellement avec le degré séparable. Les techniques mises en œuvre ici « se
recollent mal » avec celles utilisées par Denis et Demangos, ce qui empêche pour
l’instant de démontrer l’exact pendant du théorème de Dobrowolski sur le module
de Carlitz.
 4. Minorations de la hauteur avec et sans CM

Nous nous sommes ensuite penchés sur les modules CM, pour lesquels Demangos
a obtenu des résultats encourageants en direction de la conjecture 3.1. Dans [7],
nous démontrons une variante de son théorème où les exposants sont améliorés et
l’hypothèse sur la densité des premiers supersinguliers est retirée.

Théorème 3.6. Soit φ un module CM de rang r. Pour tout x ∈ ¯K de degré d
et degré inséparable di qui n’est pas de torsion pour φ :

ˆhφ(x) ≫φ 1

d
(di log(2d))2r+1 .

La principale spéciﬁcité de notre travail est l’utilisation d’un relèvement du
morphisme de Frobenius en caractéristique générique, pour une quantité suﬃsante
d’idéaux premiers. Ce fait est garanti par la théorie de Hayes (qui est par exemple

5. PERSPECTIVES 29

présentée dans [Hay92] et [Hay79]), qui relie la multiplication complexe à la théorie
du corps de classe des corps CM.

Le schéma de la preuve est pour le reste semblable à celui de [Dem15], qui
combine un lemme de Siegel absolu sur les corps de fonctions, une extrapolation ba-
sée sur des estimations p-adiques et un lemme de zéros. Contrairement à Demangos,
nous n’avons pas cherché à spéciﬁer la dépendance en φ de la constante apparaissant
dans le théorème 3.6.

La dernière étape de notre programme était d’obtenir une borne polynomiale
en toute généralité, ce dont Ghioca s’est approché dans [Ghi07]. Nous obtenons
la minoration suivante, valable pour un module de Drinfeld φ quelconque de rang
r ≥ 1.

Théorème 3.7. Pour tout x ∈ ¯K de degré d qui n’est pas de torsion pour φ :

ˆhφ(x) ≫φ 1
d4r2+5 .

Notre résultat est en fait légèrement plus précis, faisant apparaître le degré insépa-
rable et un facteur logarithmique en le degré.

La démonstration de ce théorème se fonde une nouvelle fois sur un schéma
d’approximation diophantienne, dont la première étape est le lemme de Siegel absolu
déjà appliqué dans le cas CM. L’extrapolation reﬂète des propriétés p-adiques liées
à l’annulation du polynome caractéristique Pp du morphisme de Frobenius sur la
réduction de φ modulo p. Ces propriétés sont plus faibles que celles retenues dans le
cas CM, ce qui explique la diﬀérence entres la borne obtenue ici et celle du théorème
3.6.
Le comptage ﬁnal des racines du polynôme auxiliaire est assez délicat. Il s’eﬀec-
tue en intégrant dans un principe de tiroirs des résultats classiques sur les racines de
Pp (l’analogue dans le cadre drinfeldien des « conjectures de Weil »). Remarquons
que la comparaison entre coeﬃcients et racines de Pp est bien meilleure dans un
contexte ultramétrique, et que le principe de tiroirs fonctionne car on travaille sur
un objet de dimension 1. Ces deux faits sont notamment pris en défaut si on se place
dans le cadre d’une variété abélienne déﬁnie sur un corps de nombres.

5. Perspectives

La suite du programme de recherche lancé avec Armana et Bosser concerne le
théorème de comptage de Masser [Mas86], que nous souhaitons adapter aux mo-
dules de Drinfeld aﬁn d’améliorer la borne donnée par le théorème 3.7. Le comptage
de Masser a déjà été transposé aux corps de nombres dans [LM04], ce qui indique
que le défaut de compacité des modules de Drinfeld ne devrait pas être ici un obstacle
insurmontable.

Un tel résultat pourrait aussi oﬀrir un angle d’attaque pour le problème de
Lehmer dans le cas galoisien, suivant les lignes de [4]. Dans le cadre du module de
Carlitz ou des modules CM, on peut aussi envisager de passer par des estimations en
dimension supérieure. Un analogue partiel de [AD00] pour les modules de dimension
2 a déjà été établi dans [Dio02].

30 3. HAUTEUR SUR LES MODULES DE DRINFELD

Il serait également intéressant de chercher des avatars du critère de Deuring
pour les modules de Drinfeld de rang quelconque, vu le rôle important joué par
les premiers supersinguliers dans les questions d’approximation diophantienne. Il
est possible de s’inspirer ici de résultats démontrés récemment dans les variétés
abéliennes (voir [Bla14] et [Sug13]).

Bibliographie

[AD00] F. Amoroso & S. David – « Minoration de la hauteur normalisée des
hypersurfaces », Acta Arith. 92 (2000), no. 4, p. 340–366.

[ADZ14] F. Amoroso, S. David & U. Zannier – « On ﬁelds with the Property
(B) », Proc. Amer. Math. Soc. 142 (2014), no. 6, p. 1893–1910.

[Bau15] H. Bauchère – « Minoration de la hauteur canonique pour les modules
de Drinfeld à multiplications complexes », J. Number Theory 157 (2015),
p. 291–328.

[Bla14] C. Blake – « A Deuring criterion for abelian varieties », Bull. London
Math. Soc. 46 (2014), no. 6, p. 1256–1263.

[Bro92] M. Brown – « Singular moduli and supersingular moduli of Drinfeld mo-
dules », Invent. Math. 110 (1992), p. 419–439.

[Dav95] C. David – « Supersingular reduction of Drinfeld modules », Duke Math.
J. 78 (1995), p. 399–411.

[Dem15] L. Demangos – « Lehmer problem and Drinfeld modules », Prépublication
(2015), p. 52 pages.

[Den92] L. Denis – « Hauteurs canoniques et modules de Drinfeld », Math. Ann.
294 (1992), p. 213–223.

[Den95] , « Problèmes diophantiens sur les t-modules », J. Théor. Nombres
Bordeaux 7 (1995), p. 97–110.

[Dio02] S. Dion – Analyse diophantienne et modules de Drinfeld, Thèse de docto-
rat de l’Université de Lille, 2002.

[DP08] S. David & A. Pacheco – « Le problème de Lehmer abélien pour un
module de Drinfeld », Int. J. Number Theory 4 (2008), p. 1043–1067.

[Ghi07] D. Ghioca – « The local Lehmer inequality for Drinfeld modules », J.
Number Theory 123 (2007), p. 426–455.

[Hab13] P. Habegger – « Small height and inﬁnite nonabelian extensions », Duke
Math. J. 162 (2013), no. 11, p. 2027–2076.

[Hay79] D. Hayes – « A brief introduction to Drinfeld modules », Studies in algebra
and number theory, Adv. in Math. Suppl. Stud. 6 (1979), p. 173–217.

[Hay92] , « Explicit class ﬁeld theory in global function ﬁelds », The Arith-
metic of Function Fields. Ohio State Univ. Math. Res. Inst. Publ. 2 (1992),
p. 1–32.

[LM04] T. Loher & D. Masser – « Uniformly counting points of bounded
height », Acta. Arith. 111 (2004), no. 3, p. 277–297.

[Mas86] D. Masser – « Letter to D. Bertrand », (1986).

Bibliographie 31

[Poo95] B. Poonen – « Local height functions and the Mordell-Weil theorem for
Drinfeld modules », Compos. Math. 97 (1995), no. 3, p. 349–368.

[Poo98] , « Drinfeld modules with no supersingular primes », Internat.
Math. Res. Notices 3 (1998), p. 151–159.

[Sug13] K. Sugiyama – « On a generalization of Deuring’s results », Prépublication
(2013). Table des matières

Remerciements 3

Introduction 5

Chapitre 1. Minorations géométriques sur les variétés abéliennes 9
1. Le problème de Bogomolov eﬀectif 9
2. Résultats pour les variétés banales 10
3. Le cas des hypersurfaces 12
4. Perspectives 14
Bibliographie 14

Chapitre 2. Problèmes de hauteur et courbes elliptiques 17
1. Le problème de Lehmer sur les variétés abéliennes 17
2. Le cas des extensions galoisiennes 18
3. La propriété (B) 19
4. Corps engendrés par une famille d’invariants singuliers 20
5. Perspectives 21
Bibliographie 22

Chapitre 3. Petite hauteur canonique sur les modules de Drinfeld 25
1. Présentation 25
2. Torsion des modules de Drinfeld non exceptionnels de rang 2 26
3. Le problème de Lehmer pour les extensions inséparables 27
4. Minorations de la hauteur avec et sans CM 28
5. Perspectives 29
Bibliographie 30

33
