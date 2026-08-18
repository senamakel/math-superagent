<!-- source: https://images.math.cnrs.fr/freeze/Le-probleme-3n-1-y-a-t-il-des-cycles-non-triviaux-III.html | converted from HTML -->

Images des mathématiques

---

# Le problème 3n+1 : y a-t-il des cycles non triviaux ? (III)

Piste rouge &Eacute;crit par Eliahou, Shalom

Cet article est le dernier volet d’une série consacrée au problème $3n+1$. Les deux premiers volets sont [1] sur piste verte et [2] sur piste bleue.

Rappelons la définition de la transformation de Collatz : si $n$ est un entier pair, on le transforme en $n/2$ ; s’il est impair, on le transforme en $3n+1$.

On symbolise cette transformation par une petite flèche, par exemple $10 \rightarrow 5$ et $5 \rightarrow 16$. La règle générale s’écrit donc $n \rightarrow n/2$ ou $n \rightarrow 3n+1$, suivant que $n$ est pair ou impair.

La *trajectoire de $n$*est la suite obtenue en partant de $n$ et en lui appliquant la transformation de Collatz de façon répétée. Par exemple, la trajectoire de $1$ est la suite $1,4,2,1, \ldots$, qui est donc un **cycle de longueur 3**, appelé le **cycle trivial**.

Le **problème de Collatz**consiste à déterminer s’il est vrai que la trajectoire de tout entier strictement positif $n$ de départ atteint $1$. Cette prédiction a été vérifiée sur ordinateur jusqu’à $5 \times 10^{18}$ par Tomás Oliveira e Silva en 2009 [3].

Le logo [4] représente toutes les trajectoires atteignant $1$ en au plus 18 étapes. Une image de celui-ci, qu’on peut agrandir un peu, se trouve dans le [volet vert][1].

Rappelons enfin qu’une liste commentée de tous les articles publiés sur ce problème est maintenue par Jeff Lagarias [5], qui vient aussi de publier un livre très complet sur le sujet : *The Ultimate Challenge : The $3x+1$ Problem*[6].

### Cycles de Collatz

Par commodité, appelons *cycle de Collatz*toute trajectoire cyclique de la transformation de Collatz sur les nombres entiers relatifs. On en connaît cinq à ce jour :

- la trajectoire de $1$, *cycle trivial*de longueur 3 ;

- celle de $0$, de longueur 1 ;

- celle de $-1$, de longueur 2 ;

- celle de $-5$, de longueur 5 ;

- celle de $-17$ enfin, de longueur 18.

On conjecture qu’il n’y en a pas d’autres. Un sous-problème du problème de Collatz consiste à déterminer s’il est vrai que le seul cycle de Collatz dans les entiers strictement positifs est le cycle trivial.

Dans le [volet bleu][2] de cette série, on a prouvé l’inexistence de cycles de Collatz de longueur 5 dans les entiers positifs. Dans une première partie du présent article, sur piste bleue aussi, on va exclure l’existence de tels cycles en longueur 18. Puis, en s’aventurant sur piste rouge avec des logarithmes, le langage commode des intervalles, et quelques concepts d’approximation rationnelle, on exclura bien d’autres longueurs : toutes celles comprises entre 4 et 17.026.679.260, très précisément.

### Deux ingrédients de preuve

Notre preuve d’exclusion de la longueur 5 pour les cycles de Collatz dans les entiers positifs, donnée dans le volet bleu, est constituée de deux ingrédients principaux :

- d’une part, la stabilité du cycle présumé sous l’action de la transformation de Collatz ;

- d’autre part, une équation très contraignante associée à ce cycle.

Pour exclure de plus grandes longueurs de cycles, le premier ingrédient se généralise facilement, comme on le verra.

Par contre, le second avait découlé d’une description précise de la répartition des pairs et des impairs dans le cycle. Or il est illusoire d’espérer obtenir une telle description en longueur supérieure, pour des raisons d’explosion combinatoire. Comment surmonter cet obstacle, alors ? Grâce à un petit saut dans l’abstraction, en acceptant d’introduire une notation spécifique distinguant les pairs des impairs dans le cycle présumé.

### Notations pour un cycle

Voici ces notations, qu’on utilisera dans toute la suite de l’article. On considère un hypothétique cycle de Collatz $C$ dans les entiers positifs. On notera $N$ sa longueur et $a_1, a_2, \ldots,a_N$ la liste de ses éléments distincts deux à deux, dans leur ordre d’apparition sur la trajectoire de $a_1$ :
\[ a_1 \rightarrow a_2 \rightarrow \ldots \rightarrow a_N \rightarrow a_1. \]
On notera aussi :

- $p$ le nombre d’éléments pairs de $C$ ;

- $q$ le nombre de ses éléments impairs.

On ignore tout *a priori*de $p$ et $q$, si ce n’est qu’ils satisfont l’égalité
\[ p + q \, = \, N. \]
Poursuivant sur notre lancée, on notera
\[ b_1,\ldots,b_p \]
la liste des éléments pairs de $C$, et
\[ c_1,\ldots,c_q \]
celle de ses éléments impairs.

Enfin, le plus petit élément de $C$ jouera un rôle particulier. On le notera $m$. Ce nombre est forcément impair [7].

Nous allons maintenant, dans ce cadre plus général, revisiter nos deux ingrédients de preuve.

### Stabilité par transformation de Collatz

Premier ingrédient : *si l’on applique la transformation de Collatz à la liste des éléments du cycle $C$, on retombe sur cette même liste, à l’ordre près.*

En effet, en appliquant la transformation de Collatz aux éléments
\[ a_1, a_2, \ldots, a_{N-1},a_N \]
de $C$, dans leur ordre d’apparition sur la trajectoire de $a_1$, on obtient la liste
\[ a_2,a_3, \ldots, a_N, a_1. \]
C’est toujours la liste d’origine, juste décalée cycliquement d’un cran. Le cycle $C$ est donc bien stable par transformation de Collatz [8].

### Pairs et impairs

Passons maintenant au second ingrédient de preuve, à savoir l’équation associée au cycle $C$. On ignore comment se répartissent les pairs $b_1,\ldots,b_p$ et les impairs $c_1,\ldots,c_q$ dans $C$. Mais évidemment, en les agrégeant, la liste
\[b_1, \ldots, b_p, c_1, \ldots, c_q\]
obtenue n’est rien d’autre qu’un *réarrangement*de la liste des éléments de $C$. Or, comme on l’a vu, celle-ci est globalement stable par transformation de Collatz. De plus, on sait exactement ce que donne cette transformation sur les $b_i$ et les $c_j$, puisqu’on connaît leur parité ! Faisons-le donc. En appliquant la transformation de Collatz à la liste
\[b_1, \ldots, b_p, c_1, \ldots, c_q,\]
on obtient la liste
\[\frac{b_1}2, \ldots, \frac{b_p}2, 3c_1+1, \ldots, 3c_q+1,\]
et ces deux listes contiennent exactement les mêmes éléments à l’ordre près, à savoir ceux de $C$.

### L’équation associée au cycle $C$

En particulier, comme dans le [volet bleu][2], prenons le produit $P$ des termes de $C$. En utilisant chacune des deux listes ci-dessus représentant $C$, on obtient à nouveau *deux expressions différentes*de $P$ :
\[ P \, = \, b_1 \cdots b_p c_1 \cdots c_q \]
d’une part, et
\[ P \, = \, \frac{b_1}2 \cdots \frac{b_p}2 (3c_1+1) \cdots (3c_q+1) \]
d’autre part. De cette double expression de $P$, on déduit aussitôt l’équation suivante associée à $C$, dans sa **version brute**:
\[ b_1 \cdots b_p c_1 \cdots c_q \, = \, \frac{b_1}2 \cdots \frac{b_p}2 (3c_1+1) \cdots (3c_q+1). \]
Quelques manipulations algébriques, exactement comme celles faites dans le volet bleu en longueur $N=5$, permettent de réécrire cette équation sous sa **forme épurée**[9].

Proposition. Soit $C$ un cycle de Collatz avec $p$ pairs, et $q$ impairs notés $c_1,\ldots,c_q$. Alors

\[ 2^p\, =\,\left(3+\frac{1}{c_1}\right)\left(3+\frac{1}{c_2}\right) \cdots \left(3+\frac{1}{c_q}\right). \]

### Cas particuliers

Pour $N=3$, on a le cycle trivial $1 \rightarrow 4 \rightarrow 2 \rightarrow 1$. On voit que $p=2$ et $q=1$, la liste des impairs $c_1,\ldots,c_q$ se réduisant à $c_1=1$. Il est alors bien vrai que
\[ 2^2 \, =\, \left(3+\frac{1}{1}\right). \]

Pour $N=5$, en supposant que le minimum du cycle est $a_1$, on avait trouvé trois pairs ($a_2$, $a_4$ et $a_5$) et deux impairs ($a_1$ et $a_3$), donnant donc $p=3$ et $q=2$. On retrouve bien l’équation
\[ 8 \, = \, \left(3+\frac1{a_1}\right) \left(3+\frac1{a_3}\right) \]
avec laquelle on avait exclu les cycles de Collatz de longueur 5 dans les entiers positifs.

### Une comparaison

On a établi deux fois l’équation associée à un cycle. Une première fois dans le [volet bleu][2] pour la longueur 5, puis ici en général. Que le lecteur s’amuse à comparer les deux preuves, tant cela peut servir de paradigme illustrant pourquoi les mathématiques raffolent d’abstraction !

Pour la longueur 5, la seule notation $a_1,\ldots,a_5$ des éléments du cycle présumé avait bien permis, mais au prix de quelque effort, d’analyser la situation et d’établir l’équation.

Par contre ici, on a accepté de considérer un cycle $a_1, \ldots, a_N$ de longueur $N$ non spécifiée, avec des nombres inconnus $p$ de pairs et $q$ d’impairs, et d’introduire une notation en $b_i$ et $c_j$ pour les distinguer dans le cycle. C’est assurément plus abstrait qu’en longueur 5. Mais cela a permis, finalement, d’obtenir l’équation annoncée de façon à la fois plus simple et plus générale.

Tels sont souvent, en quelque sorte, les termes du marché en mathématiques : au prix d’un peu d’abstraction supplémentaire, on gagne en puissance et on acquiert les moyens de pousser l’analyse plus loin.

### Un encadrement de $2^p$

Montrons maintenant que l’équation en question fournit un encadrement de $2^p$ très contraignant. Rappelons qu’on note $c_1,\ldots,c_q$ les éléments impairs de $C$ et $m$ son minimum. On a donc
\[ c_i \, \ge \, m \]
pour tout indice $i$ entre $1$ et $q$. En inversant, puis en ajoutant $3$, on obtient
\[ 3 \, pour tout $i$, sachant que les $c_i$ sont strictement positifs. En prenant le produit de ces $q$ termes, on obtient les inégalités suivantes :
\[ 3^q \, Maintenant, par l’équation associée au cycle, le terme du milieu est égal à $2^p$. On obtient donc l’encadrement suivant :
\[ 3^q \, Résumons formellement ce que l’on vient d’obtenir.

Proposition. Soit $C$ un cycle de Collatz dans les entiers positifs, avec $p$ pairs, $q$ impairs, et de minimum $m$. Alors

\[ 3^q \,

Voici pourquoi on pourra tirer des informations de cet encadrement : plus le minimum $m$ de $C$ est grand, plus son inverse $1/m$ est petit, et plus il sera difficile de trouver une puissance de $2$ coincée entre des puissances de $3$ et de $3+1/m$ avec un exposant commun $q$. On va voir que cela suffit déjà pour exclure la longueur 18.

### En longueur 18

On sait que la trajectoire de $-17$ est un cycle de Collatz de longueur 18 dans les entiers négatifs. Montrons qu’au contraire, il n’existe pas de cycle de Collatz $C$ de cette longueur dans les entiers positifs. Les symboles $p$, $q$ et $m$ ci-dessus sont compris relativement à cet hypothétique cycle $C$. En particulier, le minimum $m$ de $C$ est strictement plus grand que 1, puisque la trajectoire de $1$ est un cycle de longueur 3 et non pas 18.

Comme $p+q=18$, on a $p=18-q$, et l’encadrement de $2^p$ ci-dessus devient :
\[ 3^q \, Puisque $m > 1$, il suit que $\left(3+\frac{1}{m}\right) \[ 3^q \, Quelles sont les valeurs de $q$ satisfaisant ces deux inégalités ?

- Si $q$ est trop grand, alors $3^q$ dépassera $2^{18-q}$ et $q$ ne conviendra pas.

- De même, si $q$ est trop petit, alors $18-q$ sera trop grand et $2^{18-q}$ dépassera $4^q$ ; donc $q$ ne conviendra pas non plus.

Concrétisons ces observations avec une calculette. On trouve
$3^7=2187$ et $2^{11}=2048$, donnant l’inégalité
\[ 3^7 \, >\, 2^{11}. \]
Donc les valeurs de $q$ supérieures ou égales à 7 sont interdites. Dans l’autre sens, on a
\[ 2^{13} \, >\, 4^5, \]
puisque $4^5\,=\, 2^{10}$. Les valeurs de $q$ inférieures ou égales à 5 sont donc interdites également.

Reste une *unique*valeur permise, à savoir $q\,=\,6$, ce qui donne $18-q\,=\,12$. Or on a
\[ 2^{12} \, = \, 4^{6}, \]
en contradiction avec l’inégalité stricte $2^{18-q}\,

**Conclusion : il n’existe aucun cycle de Collatz de longueur 18 dans les entiers positifs.**

### Entrée douce sur piste rouge

On peut — et on va — aller au delà de l’exclusion de la longueur 18. Mais pour y arriver, on a besoin d’outils nous permettant de mieux exploiter la force de l’encadrement de $2^p$ obtenu plus haut. L’idée est de faire « descendre » $p$ et $q$ qui s’y trouvent en exposants, afin de les manipuler plus aisément. Or les mathématiques ont un outil tout indiqué pour cela : les logarithmes.

### Logarithmes

Notons simplement $\log$ la fonction logarithme en base 10 [10]. Que le lecteur peu à l’aise avec elle ne lâche pas prise à cet endroit ! Car, au début tout au moins, on utilisera cette fonction surtout comme une boîte noire, dotée des propriétés suivantes :

- $\log$ respecte l’ordre : si $x\,

- $\log$ permet de « descendre » les exposants : $\log(x^r)\, =\, r \log(x)$.

Cette seconde propriété se voit très bien sur ces valeurs de base : $\log(10) = 1$, $\log(100) = 2$, $\log(1000) = 3$, et plus généralement,
\[ \log(10^r) \, = \, r \log(10) \, = \, r. \]
Cela découle du fait que $\log$, à l’inverse de l’exponentielle, transforme produits en sommes [11]:
\[ \log(xy) \, = \, \log(x)+\log(y). \]

Enfin, une troisième propriété du logarithme intervenant ici est sa *continuité*: si $x$ et $y$ sont très proches, alors $\log(x)$ et $\log(y)$ le sont aussi, dans un sens pouvant être quantifié de façon précise. On indiquera à quel endroit cette propriété se manifeste.

### Un encadrement de $p/q$

On va pouvoir déduire, grâce aux logarithmes, un encadrement de $p/q$ à partir de celui de $2^p$ obtenu auparavant. Rappelons que pour un cycle de longueur $N=p+q$, avec $p$ pairs, $q$ impairs et de minimum $m$, on a forcément :
\[ 3^q \, Appliquons le logarithme à ces termes. Comme $\log$ respecte l’ordre, on obtient
\[ \log\left(3^q\right) \, Descendons les exposants, puisque $\log$ permet de le faire :
\[ q \log\left(3\right) \, Divisons ces termes par $q$. Cela donne
\[ \log\left(3\right) \, Enfin, divisant le tout par $\log(2)$, on obtient le résultat suivant.

Théorème. Soit $C$ un hypothétique cycle de Collatz dans les entiers positifs, avec $p$ pairs, $q$ impairs, et de minimum $m$. Alors on a forcément :

\[ \frac{\log(3)}{\log(2)} \,

Encore une fois, plus $m$ est grand, plus $1/m$ est petit et, par continuité, plus $\log(3+1/m)$ est proche de $\log(3)$. Autrement dit, le rapport $p/q$ se retrouve coincé entre deux nombres d’autant plus proches que $m$ est grand. Ces contraintes vont se révéler très fortes.

### Où la borne $5\times 10^{18}$ intervient

Pour un hypothétique cycle de Collatz non trivial $C$ dans les entiers positifs, de minimum $m$, on a forcément
\[ m \, > \, 5\times 10^{18}.\]

Cela découle de la vérification du problème $3n+1$ sur ordinateur par Tomás Oliveira e Silva jusqu’à cette borne : pour tout entier $n$ inférieur à $5\times 10^{18}$, sa trajectoire finit par atteindre 1. Celle-ci ne peut donc constituer un cycle autre que le cycle trivial de longueur 3. On en déduit ce qui suit.

Corollaire. Soit $C$ un cycle de Collatz non trivial dans les entiers positifs, avec $p$ pairs et $q$ impairs. Alors

\[ \frac{\log(3)}{\log(2)} \,

En effet, notant toujours $m$ le minimum de $C$, on a $m > 5\times 10^{18}$. En prenant les inverses, l’ordre s’inverse, ce qui donne
\[ \frac1m \, ou encore, comme $1/5 \,=\,0,2\,=\,2 \times 10^{-1}$,
\[ \frac1m \, Reste enfin, de chaque côté, à ajouter $3$ ; à prendre le logarithme, ce qui conserve l’ordre ; et à diviser par $\log(2)$. Cela donne l’inégalité :
\[ \frac{\log\left(3+\frac{1}{m}\right)}{\log(2)} \, Combinée à l’encadrement de $p/q$ obtenu plus haut, on obtient celui annoncé.

### Intervalles

Cet encadrement de $p/q$ s’exprime très bien dans le langage des intervalles : il dit que $p/q$ appartient à l’intervalle ouvert suivant [12]:
\[ \frac pq \, \in \, \left]\frac{\log(3)}{\log(2)} \, , \, \frac{\log\left(3+2\times10^{-19}\right)}{\log(2)}\right[. \]
Concrètement, voici les 25 premières décimales de ces extrémités :
\[ \begin{array}{rcl} \log(3)/\log(2) & = & 1,584962500721156181\mathbf{4}537389, \\ \log(3+2\times 10^{-19})/\log(2) & = & 1,584962500721156181\mathbf{5}499186. \end{array} \]
Leur différence est minuscule [13]: elle ne se manifeste qu’à partir de la 19ème décimale, montrée en gras. En gommant les dernières décimales, on déduit ce qui suit.

Corollaire. Soit $C$ un cycle de Collatz non trivial dans les entiers positifs, avec $p$ pairs et $q$ impairs. Alors $p/q$ appartient à l’intervalle suivant :

\[ p/q \, \in \, \left]1,584962500721156181\mathbf{4}5, \,\,1,584962500721156181\mathbf{5}5 \right[. \]

### Une conséquence drastique

Reprenons l’intervalle minuscule ci-dessus et désignons-le par $I$ :
\[ I \, = \, \left]1,584962500721156181\mathbf{4}5, \,\,1,584962500721156181\mathbf{5}5 \right[. \]
En quoi le fait de savoir que $p/q$ est contraint d’y habiter pourrait-il nous être utile ? Assez curieusement parce que, comme on le verra, *toute fraction appartenant à $I$ est tenue d’avoir ses numérateur et dénominateur très grands*, dans un sens tout à fait explicite. Concrètement, on verra que pour tout habitant rationnel $s/t$ de $I$, avec $s$ et $t$ entiers positifs, on a forcément
\[ \begin{array}{rcr} s & \ge & 10.439.860.591,\\ t & \ge & 6.586.818.670. \end{array} \]
En particulier, ces seuils s’appliqueront à $p$ et $q$ respectivement, puisque $p/q$ appartient à $I$. Il en découlera aussitôt que la longueur de notre présumé cycle $C$ doit dépasser la somme de ces seuils, à savoir $17.026.679.261$.

Entamons maintenant quelques préliminaires qui finiront par nous conduire à une preuve de ces affirmations.

### Convention

A partir d’ici, on dira simplement « rationnel » pour « nombre rationnel » ou « fraction d’entiers ». Et en écrivant un rationnel sous forme de fraction $s/t$, on supposera implicitement que $s$ et $t$ sont entiers, avec $t\ge 1$ [14].

### Rationnels économiques dans un intervalle

On est donc confrontés à la question suivante. Considérons un intervalle ouvert $J$ dans la droite des nombres réels, disons $J\, =\, ]x,y[$. Parmi tous les habitants rationnels $s/t$ de cet intervalle, autrement dit ceux satisfaisant
\[ x \, quel est *le plus économique*, c’est-à-dire celui avec numérateur et dénominateur minimaux ? Plus précisément, quel est *le*rationnel $a/b$ dans $J$ avec **dénominateur $b \ge 1$ minimal**et, ce $b$ étant fixé, avec **numérateur $a$ minimal en valeur absolue**?

Par exemple, dans l’intervalle ouvert $]0,1[$, l’habitant rationnel le plus économique est $1/2$, bien sûr.

Comme second exemple, considérons l’intervalle ouvert $J=]2,3[$. Alors *son habitant rationnel le plus économique est $5/2$*. En effet, d’une part $5/2$ appartient à $J$, puisque
\[ 2 \, D’autre part, montrons que *pour tout rationnel $s/t$ dans $]2,3[$, on a $s\, \ge\, 5$ et $t\, \ge\, 2$*. La borne $t\, \ge\, 2$ est évidente, puisque les rationnels avec dénominateur $1$ sont des nombres entiers, donc exclus de $J$ ! Pour établir $s\, \ge\, 5$, considérons au contraire un rationnel $r/t$ avec $t \ge 2$ mais $r \le 4$. Alors
\[ \frac rt \, \le \, 2, \]
et donc $r/t$ est exclu de $J$. Il suit bien que pour tout rationnel $s/t$ dans $J$, on a forcément $s \ge 5$ .

Heureusement, on dispose d’outils pour aborder ce problème de façon plus efficace et dans des intervalles bien plus corsés.

### Un cas apparemment particulier

Ce problème du rationnel le plus économique est très ancien et appartient à la théorie des approximations rationnelles. Des solutions en ont été données au 17ème siècle par John Wallis (1616-1703) et par Christiaan Huygens (1629-1695), avec le concept de *fractions continues*[15]. La motivation de Huygens était très concrète : il lui fallait déterminer les bons nombres de dents pour chaque paire de roues dentées contiguës de son célèbre planétarium !

Notre approche ici repose sur la solution du problème dans un cas apparemment particulier, celui des *intervalles de Farey*. En fait on pourra tout faire avec.

Définition. Une **paire de Farey**est une paire de rationnels $\frac{s_1}{t_1} \, intervalle de Farey**est un intervalle ouvert $\left]\frac{s_1}{t_1}, \; \frac{s_2}{t_2}\right[$ dont les extrémités forment une paire de Farey.

Par exemple, l’intervalle $\left]\frac{7}{9},\frac{4}{5}\right[$ est de Farey, puisque
\[ 4 \times 9 - 7 \times 5 \,=\, 36-35 \,=\, 1. \]
De façon remarquable, pour ces intervalles, décrire l’habitant rationnel le plus économique est très facile. Voici comment, en mots d’abord.

Le rationnel le plus économique dans un intervalle de Farey est la somme des numérateurs de ses extrémités, divisée par la somme de leurs dénominateurs.

Puis traduit en formules.

Proposition. Soit $J=\left]\frac{s_1}{t_1}, \; \frac{s_2}{t_2}\right[$ un intervalle de Farey. Alors le rationnel le plus économique dans $J$ est \[ \frac{s_1+s_2}{t_1+t_2}. \]

Voici quelques exemples.

- L’intervalle $]0,1[\, =\, \left]\frac{0}{1},\frac{1}{1}\right[$ est de Farey, et son habitant rationnel le plus économique est effectivement $(0+1)/(1+1)$, c’est-à-dire $1/2$.

- Pour l’intervalle $]2,3[\,=\,\left]\frac{2}{1},\frac{3}{1}\right[$, qui est aussi de Farey, on retrouve bien notre observation précédente : son rationnel le plus économique est $5/2\, =\, (2+3)/(1+1)$.

- Enfin, pour l’intervalle de Farey $\left]\frac{7}{9},\frac{4}{5}\right[$ ci-dessus, la proposition affirme que son rationnel le plus économique est $11/14$.

Ce résultat, qui nous sera fort utile plus loin, découle d’un énoncé bien plus général décrivant carrément *tous*les habitants rationnels d’un intervalle de Farey.

### Rationnels dans un intervalle de Farey

Commençons par un peu de terminologie maison. On dira d’un entier $s$ qu’il est un *panachage*de la paire d’entiers $(s_1,s_2)$ s’il est de la forme
\[s \, = \, a s_1 + b s_2,\]
où $a$ et $b$ sont deux nombres entiers strictement positifs. On appellera alors $a$ et $b$ les *coefficients*ou les *doses*du panachage.

Par exemple, 19 est un panachage de la paire (5,7), de coefficients 1 et 2, puisque une dose de 5 plus deux doses de 7 font bien 19.

Le résultat général dont nous aurons besoin, et qu’on appellera le **théorème du panachage**, dit ceci.

Pour un intervalle de Farey $J\, =\, \left]\frac{s_1}{t_1}, \; \frac{s_2}{t_2}\right[$, tout habitant rationnel $s/t$ de $J$ est de la forme suivante : son numérateur $s$ est un panachage de $(s_1,s_2)$, son dénominateur $t$ est un panachage de $(t_1,t_2)$, et les coefficients de ces deux panachages sont les mêmes. Et réciproquement, tout rationnel de cette forme habite dans $J$.

Voici le même énoncé, en formules.

Théorème. Soit $J=\left]\frac{s_1}{t_1}, \; \frac{s_2}{t_2}\right[$ un intervalle de Farey. Alors les rationnels $s/t$ appartenant à $J$ sont exactement ceux vérifiant : \[ \begin{array}{lcl} s & = & a s_1 + b s_2, \\ t & = & a t_1 + b t_2, \end{array} \] où $a$ et $b$ sont des entiers strictement positifs.

Notons que ce résultat entraîne instantanément le précédent, selon lequel le rationnel le plus économique dans $J$ est $(s_1+s_2)/(t_1+t_2)$. En effet, le plus petit panachage possible de $(s_1,s_2)$ est l’entier $s_1+s_2$, c’est-à-dire avec doses égales à 1, et celui de $(t_1,t_2)$ avec ces mêmes doses est l’entier $t_1+t_2$.

Notons aussi que ce théorème se vérifie aisément pour l’intervalle de Farey particulier
\[ J_0 \, =\, ]0,1[ \, =\, \left]\frac{0}{1},\frac{1}{1}\right[. \]
En effet, les rationnels $s/t$ dans $]0,1[$ sont exactement ceux pour lesquels
\[ 1 \, \le \, s \, \le \, t-1. \]
Or tout entier $s\, \ge\, 1$ est un panachage de la paire $(0,1)$ avec coefficients $t-s$ et $s$, qui sont bien strictement positifs comme requis ; et tout entier $t\, \ge\, s+1$ est un panachage de $(1,1)$ avec ces mêmes coefficients, puisque
\[ \begin{array}{lcl} s & = & (t-s)\times 0 \, +\, s \times 1, \\ t & = & (t-s)\times 1 \, +\, s \times 1. \end{array} \]
Le théorème est donc bien vrai pour l’intervalle $]0,1[$. La preuve dans le cas général, donnée ci-dessous, consiste à se ramener à ce cas particulier, grâce à un dictionnaire parfait entre les rationnels de $]0,1[$ et ceux de $]s_1/t_1, s_2/t_2[$.

### Preuve du théorème du panachage

Nous allons décrire ce dictionnaire parfait [16] par formules explicites. En fait, on va le faire au niveau des intervalles *fermés*:

- à tout rationnel $z$ dans $[0,1]$, on associera un rationnel dénoté $f(z)$ et appartenant à $\left[\frac{s_1}{t_1}, \; \frac{s_2}{t_2}\right]$ ;

- à tout rationnel $z'$ dans $\left[\frac{s_1}{t_1}, \; \frac{s_2}{t_2}\right]$, on associera un rationnel dénoté $g(z')$ et appartenant à $[0,1]$.

Voici les formules, un peu compliquées de prime abord, décrivant $f$ et $g$. Pour tout rationnel $c/d$ dans $[0,1]$, on définit
\[ f\left(\frac{c}{d}\right) \, = \, \frac{(s_2-s_1)\times c \,+\, s_1 \times d}{(t_2-t_1)\times c \,+\, t_1 \times d} ; \]
et pour tout rationnel $c'/d'$ dans $\left[\frac{s_1}{t_1}, \; \frac{s_2}{t_2}\right]$, on définit
\[ g\left(\frac{c'}{d'}\right) \, = \, \frac{t_1\times c' \,-\, s_1 \times d'}{(t_1-t_2)\times c' \,+\, (s_2-s_1) \times d'}. \]

Pour montrer que ces deux associations constituent un dictionnaire parfait entre les rationnels de l’intervalle ouvert $]0,1[$ et ceux de $J$, il suffit de vérifier les huit propriétés suivantes ; les quatre ci-dessous, plus les quatre autres obtenues en interchangeant partout $f$ avec $g$ et $[0,1]$ avec $\left[\frac{s_1}{t_1}, \; \frac{s_2}{t_2}\right]$ :

- *$f$ envoie les extrémités de $[0,1]$ sur celles de $\left[\frac{s_1}{t_1}, \; \frac{s_2}{t_2}\right]$*.

- *$f$ respecte l’ordre*: si $z_1$, $z_2$ sont rationnels et $z_1\,

- *$f$ préserve les panachages*, dans le sens que si l’on part d’un rationnel $z$ dans $[0,1]$ dont les numérateur et dénominateur
sont des panachages d’une même paire avec mêmes doses, alors il en est de même pour $f(z)$.

- *$f$ et $g$ sont inverses l’une de l’autre*: si l’on part d’un rationnel $z$ dans $[0,1]$, qu’on lui applique $f$, puis qu’on applique $g$ au résultat, alors on retombe sur $z$. Autrement dit, $g(f(z)) = z$.

Comment vérifier ces propriétés ? On l’indique brièvement ci-dessous. Mais on peut déjà conclure que ce dictionnaire parfait prouve le théorème du panachage en toute généralité.

### Vérification directe ... ou conceptuelle

Le lecteur patient saura prouver les propriétés ci-dessus par calcul direct. Mais celui connaissant un peu les matrices et les homographies pourra aussi le faire de façon plus conceptuelle. En effet, $f$ et $g$ sont essentiellement des homographies relativement aux matrices
\[ A = \left( \begin{array}{cc} s_2-s_1 & s_1 \\ t_2-t_1 & t_1 \end{array} \right) \quad \textrm{ et } \quad B = \left( \begin{array}{cc} t_1 & -s_1 \\ t_1-t_2 & s_2-s_1 \end{array} \right). \]
Ces matrices sont de déterminant 1 : cela découle directement de l’hypothèse que $J$ est un intervalle de Farey. De plus, elles sont inverses l’une de l’autre ; c’est grâce à cela que $f$ et $g$ sont des fonctions inverses l’une de l’autre [17].

### Application au problème $3n+1$

Considérons un hypothétique cycle de Collatz non trivial $C$ dans les entiers positifs, avec $p$ pairs et $q$ impairs. On a vu plus haut qu’alors, ${p}/{q}$ appartient à l’intervalle ouvert

\[ I \, = \, \left]1,584962500721156181\mathbf{4}5, \,\,1,584962500721156181\mathbf{5}5 \right[. \]

Cet intervalle n’est sûrement pas de Farey. Quel est donc son habitant rationnel le plus économique ? Voici tout de suite la réponse :

*Le rationnel le plus économique dans $I$ est*
\[\frac{10.439.860.591}{6.586.818.670}.\]

Comment peut-on l’affirmer, puisque la théorie présentée plus haut ne décrit les rationnels économiques que dans les intervalles de Farey ?

Eh bien, l’astuce consiste à construire **deux intervalles de Farey contigus englobant $I$**, c’est-à-dire contenant chacun une extrémité de $I$.

Voici ces deux intervalles contigus, avec l’extrémité respective de $I$ qui s’y trouve :

\[ \begin{array}{ccc} 1,584962500721156181\mathbf{4}5 & \in & \left]\frac{9.809.721.694}{6.189.245.291}, \, \frac{10.439.860.591}{6.586.818.670} \right[, \\ \\ 1,584962500721156181\mathbf{5}5 & \in & \left]\frac{10.439.860.591}{6.586.818.670}, \, \frac{630.138.897}{397.573.379} \right[. \end{array} \]

Un bon logiciel de calcul suffit pour constater que ces deux intervalles sont bien de Farey, et qu’ils contiennent les extrémités indiquées [18].

Or, on connaît le rationnel le plus économique dans chacun de ces deux intervalles de Farey : c’est la somme des numérateurs des extrémités, divisée par la somme de leurs dénominateurs [19]. Mais visiblement, ces deux rationnels-là sont bien moins économiques que l’extrémité commune des deux intervalles, à savoir
\[\frac{10.439.860.591}{6.586.818.670}.\]
C’est donc *lui*, le rationnel le plus économique strictement compris entre l’extrémité gauche du premier intervalle et l’extrémité droite du second. Et par conséquent, le plus économique dans $I$.

En particulier, tout habitant rationnel $s/t$ de $I$ satisfait
\[ \begin{array}{rcr} s & \ge & 10.439.860.591,\\ t & \ge & 6.586.818.670. \end{array} \]
Ces bornes respectives valent donc pour $p$ et $q$, puisque $p/q$ habite dans $I$. On vient de démontrer le résultat suivant.

*S’il existe un cycle de Collatz non trivial dans les entiers positifs, de longueur $N$, avec $p$ pairs et $q$ impairs, alors $p\, \ge\, 10.439.860.591$, $q\, \ge\, 6.586.818.670$, et donc $N \, \ge\, 17.026.679.261.$*

En particulier, s’il y avait un cycle de longueur exactement 17.026.679.261, ce que personne ne sait encore exclure, alors il contiendrait *exactement*10.439.860.591 pairs et 6.586.818.670 impairs. C’est rigide ! Et ça rappelle le cas de longueur 18, où la seule répartition possible était 12 pairs et 6 impairs.

### En longueur 18 milliards

Personne, disions-nous, ne sait encore exclure la longueur 17.026.679.261. Par contre, on en sait assez pour exclure la longueur 18 milliards pile. En effet, supposons qu’il existe un cycle de Collatz dans les entiers positifs de longueur $N=p+q$ *strictement supérieure*à 17.026.679.261.

Alors $p/q$ devrait habiter dans l’un des deux intervalles de Farey contigus ci-dessus, puisqu’ici il doit différer de leur extrémité commune $\frac{10.439.860.591}{6.586.818.670}$. Or, pour le rationnel $s/t$ le plus économique du deuxième intervalle, on voit que
\[ \begin{array}{lcl} s + t & = & (10.439.860.591+630.138.897)\,+\, (6.586.818.670+397.573.379) \\ & = & 18.054.391.537, \end{array} \]
ce qui dépasse légèrement 18 milliards. Quant à la valeur de $s+t$ correspondante pour le premier intervalle de Farey, elle est de l’ordre de 33 milliards.

On a donc obtenu l’inégalité suivante :
\[ p+q \, \ge \, 18.054.391.537. \]
Ce qui exclut, parmi bien d’autres, la longueur 18.000.000.000.

### Intervalles de Farey contigus

« Très bien », dira peut-être le lecteur pas encore épuisé. « Mais comment construire de tels intervalles de Farey contigus ? »

On peut lui donner deux réponses, l’une assez opaque et l’autre totalement transparente.

La première dirait : en prenant des convergentes secondaires successives d’une fraction continue. Bon.

Mais voici plutôt la seconde.

En coupant n’importe quel intervalle de Farey là où se situe son rationnel le plus économique, les deux morceaux contigus résultants forment chacun un intervalle de Farey !

Pour le redire en formules, partons d’un intervalle de Farey
\[ J\, =\, \left]\frac{s_1}{t_1}, \; \frac{s_2}{t_2}\right[. \]
Appelons **médian**son rationnel le plus économique, à savoir la fraction $(s_1+s_2)/(t_1+t_2)$. Alors les intervalles obtenus en coupant $J$ en son médian, c’est-à-dire
\[ J_1\, =\, \left]\frac{s_1}{t_1}, \; \frac{s_1+s_2}{t_1 + t_2}\right[ \quad \textrm{ et } \quad J_2\, =\, \left]\frac{s_1+s_2}{t_1 + t_2}, \; \frac{s_2}{t_2}\right[, \]
sont évidemment contigus *et ils sont tous deux de Farey*. La vérification se fait par un calcul direct instantané.

Reprenons maintenant notre minuscule intervalle $I$ défini plus haut [20]. Partons d’un intervalle de Farey $J$ contenant $I$, par exemple $J=]1,2[$. Coupons $J$ en son médian. Si ce médian tombe *en dehors de $I$*, alors l’un des deux intervalles de Farey résultant contient encore $I$. Dans ce cas, on remplace $J$ par ce sous-intervalle et on recommence. Au bout d’un nombre fini de telles étapes, il arrivera au contraire que le médian de $J$ *tombe dans $I$*. Il en résulte deux intervalles de Farey contigus englobant $I$, et on a fini.

C’est précisément en suivant cette procédure que l’on a construit la jolie paire d’intervalles de Farey contigus, englobant $I$, de laquelle on a déduit plus haut nos bornes inférieures pour $p$, $q$ et $N$.

### Conclusion

On a montré que tout hypothétique cycle de Collatz non trivial $C$ dans les entiers positifs doit contenir au moins 17 milliards d’éléments, s’il existe. Cela ne répond pas, hélas, à la question du titre de cet article. Mais c’est déjà ça, en attendant mieux.

Et un léger mieux viendra peut-être bientôt. En effet, cette borne de 17 milliards repose sur la vérification actuelle du problème $3n+1$ jusqu’à $5 \times 10^{18}$. Lorsque la vérification future du problème atteindra $2,17 \times 10^{20}$, dans quelques années sans doute, alors notre borne inférieure sur les longueurs de cycles sautera de 17 milliards à ... 186 milliards, d’un seul coup [21]! À part une bonne calculette, tous les ingrédients théoriques et numériques nécessaires pour s’en convaincre se trouvent dans cet article. Qui est partant pour le vérifier ?

**Post-scriptum :**

L’auteur remercie Etienne Ghys et Bruno Martin pour leurs commentaires, et Carole Gaboriau pour son aide technique. La rédaction d’Images des maths, ainsi que l’auteur, remercient pour leur relecture attentive, les relecteurs dont le pseudonyme est le suivant : Joël Merker,
Simon Billouet,
Christophe Boilley,
P.Levallois,
J. Struffi et
Gilles Damamme.

Article édité par [Ghys, Étienne][3]

## Notes

[1] [Le problème 3n+1 : élémentaire mais redoutable (I)][1]

[2] [Le problème 3n+1 : cycles de longueur 5 (II)][2]

[3] [http://www.ieeta.pt/ tos/3x+1.html][4]

[4] Dû à [Jason Davies][5], que je remercie vivement.

[5] Suivre le lien vers « 3X+1 Problem » dans sa [page web.][6]

[6] American Mathematical Society, 2010. Le lien vers « Book : The Ultimate Challenge : The 3x+1 Problem » dans la [page web][6] de l’auteur donne accès, en suivant le lien vers « Preview Material », à un survol de 27 pages en anglais.

[7] Car sinon on aurait $m \rightarrow m/2$, donc $m/2$ serait aussi dans $C$, en contradiction avec la minimalité de $m$ dans $C$.

[8] La notion générale de stabilité d’un ensemble sous l’effet d’une opération est extrêmement féconde en mathématiques. C’est à elle que nombre d’objets et concepts doivent leur existence.

[9] Ces manipulations consistent à multiplier les deux côtés de l’équation brute par $2^p$, puis à les diviser par $b_1 \cdots b_p$ et $c_1 \ldots c_q$.

[10] On aurait aussi pu prendre le logarithme népérien, la base choisie ne jouant aucun rôle ici.

[11] Propriété cruciale, grâce à laquelle les anciennes tables de logarithmes ont, pendant des siècles, joué le rôle de calculettes en papier !

[12] Rappelons que l’*intervalle ouvert*$]x,y[$ est constitué de tous les nombres réels $z$ satisfaisant $x

[13] C’est la continuité du logarithme qui en est responsable : deux nombres très proches ont des logarithmes très proches.

[14] Par contre, on n’aura pas besoin de supposer que $s$ et $t$ sont premiers entre eux même si, de fait, ils le seront automatiquement dans la plupart des cas rencontrés.

[15] Pour des articles récents dans Images des Mathématiques autour des fractions continues, voir par exemple [Nombres et représentations][7] de Valérie Berthé ou [Calendriers et fractions continues][8] de Anne Broise.

[16] On dirait cette *bijection*, en langage technique.

[17] Voir par exemple l’ [article de Wikipedia][9] sur les homographies, en particulier la courte section intitulée « Propriétés algébriques ».

[18] On peut faire le calcul en ligne sur la [calculatrice][10] du très sympathique serveur [WIMS][11], ou sur le moteur de recherche [Wolfram Alpha][12] par exemple. Ou sur son ordinateur avec un logiciel de calcul formel comme [Maxima][13], installable gratuitement. Merci à Gilles Damamme et à P. Levallois pour leurs suggestions sur WIMS et Maxima.

[19] Par exemple, pour le premier intervalle, ce rationnel le plus économique est $\frac{9.809.721.694\,+\,10.439.860.591}{ 6.189.245.291\,+\,6.586.818.670}$.

[20] C’est-à-dire $I = \left]1,584962500721156181\mathbf{4}5, \,\,1,584962500721156181\mathbf{5}5 \right[.$

[21] Plus précisément, la nouvelle borne inférieure sautera à 186.265.759.595. Un hypothétique cycle de Collatz de cette longueur aurait exactement 114.208.327.604 éléments pairs et 72.057.431.991 éléments impairs.

#### ▶ Cr&eacute;dits images

[Image à la une][14] - L’auteur remercie [Jason Davies][5], créateur du logo.

## Commentaires

-
-

### Le problème 3n+1 : y a-t-il des cycles non triviaux ? (III)

#### le 21 décembre 2011 à 07:50, par Cidrolin

Bonjour,
Ce problème n’est pas que difficile et déroutant, il est surtout chronophage. En tant qu’ancienne victime, je peux
témoigner : des pages et des pages de calcul sur la suite E(n ln3/ln2) ou sur les réduites de ln3/ln2. Sans aboutir.
Félicitations pour ces trois articles qui conduisent à un résultat démontré. Ils sont vraiment très clairs et très pédagogiques.
Dans la phrase :&laquo; divisant le tout par log(2), on obtient le résultat &raquo;, il manque &laquo; car log 2 est strictement positif &raquo;.
Pensez aux apprenants devant la résolution de 0.99^n < 0.000001

-
-

### Le problème 3n+1 : y a-t-il des cycles non triviaux ? (III)

#### le 24 décembre 2011 à 15:41, par Julien

Très bon article, qui aborde à la fois des points élémentaires et d’autres plus évolués.

Dans la mesure où les approximations rationnelles de ln(3)/ln(2) jouent un rôle dans la recherche des cycles, je suis toutefois un peu surpris de ne pas leur voir accorder plus d’importance.

Tant que j’y pense, une question peut-être naïve et déjà abordée (et résolue ?) ; si pour tout entier pair on peut choisir librement entre les opérations x->x/2 et x->3x+1, cela rend-il le problème de trouver un/des cycle(s) ou un chemin infini moins difficile ?

-
-

### Le problème 3n+1 : y a-t-il des cycles non triviaux ? (III)

#### le 6 janvier 2015 à 10:09, par Pierre Lecomte

Ah quel agréable article, limpide et très amusant !
Félicitation et merci !

-
-

### Le problème 3n 1 : y a-t-il des cycles non triviaux ? réponse (?) : il semblerait que non.

#### le 28 février 2016 à 17:14, par Deschamps Xavier

Bonjour,

Si je ne me trompe pas :

Pour répondre à cette question, il faut déterminer ce qui conditionne les cycles :

Combien de répétitions de la transformation 3n + 1 (réponse le nombre de 2 dans la décomposition de n + 1 en facteur premier et à chaque fois, elle transforme &laquo; ces 2 en 3 &raquo;)

Combien de répétition de la division par 2 (réponse : le nombre de 2 dans la décomposition de n en facteur premier)

donc ces transformations font la chasse aux 2. Cela permet d’accélérer les transformations.

Pour continuer, il faut faire apparaître des cycles dans la démonstration car c’est le problème. Comme on ne peut gérer les valeurs qui fluctuent, gérons la forme du nombre. Après un certain temps, ils sont de la forme 6k, 6k + 1 ou 6k + 2, ou 6k + 4 ou 6k + 5 ( = &laquo; 6k - 1 &raquo;) et passent de l’une à l’autre suivant la parité de k. Et comme au cours du calcul, k sert de compte à rebours les cycles finissent toujours par arriver au cycle trivial.

Il faudrait quelqu’un pour vérifier les calculs. Je joindrais bien un pdf de mes notes manuscrites si je savais comment le faire sur ce site.

-
-

### Le problème 3n+1 : y a-t-il des cycles non triviaux ? (III) ; deux &laquo; théorèmes &raquo;

#### le 20 mars 2016 à 15:39, par Philippe Gay

Bravo pour ces superbes articles !

Voici deux mini-théorèmes.

1- **Soit le problème de Syracuse en (3n + 1)/2. Tous les éléments de ses cycles connus (càd passant par 1, mais aussi par -1 , -5 et -17) et inconnus (s’ils existent !), excepté celui en zéro, sont différents de 0 modulo 3. **

J’obtiens cela grâce à la théorie des graphes. On peut vérifier que 1, 2, -1, -5, -7 , 10, -17... ne sont jamais divisibles par 3.

2 - **Soit le problème de Syracuse en (3n + 1)/2 et n’importe lequel de ses cycles connus et inconnus (s’ils existent). Il existe une relation entre la somme des termes pairs P, des nombres impairs I et le nombre de ses termes impairs W de ce cycle qui est I + W = P.**

J’obtiens cela grâce à une transformation matricielle.
Pour le cycle (1, 2) on 1+1= 2.
Pour(0), on a 0 +0 = 0.
Pour (-1), on 1 -1 = 0.
Pour (-5, -7, -10), on a 2 -12 = -10.
Pour (-17...), c’est vrai aussi.

Quand quelqu’un (pas moi !) aura trouvé un autre cycle, on vérifiera tout cela. (Pas sûr que cela soit pour bientôt !)

Plus sérieusement, c’est bien, mais c’est peut-être déjà cité. On voit juste que beaucoup d’outils ont été utilisés contre cette conjecture.

-
-

### Le problème 3n 1 : y a-t-il des cycles non triviaux ? (III)

#### le 19 février 2019 à 17:47, par CAMI

Soit Ni l’ensemble des entiers positifs impairs > 0 soit 2*n-1 pour n de 1 à N.
Définissons l’ensemble U(0) à élément unique = 1.
Définissons l’ensemble U(1) contenant les valeurs de (4^n-1)/3 pour n de 1 à N soit :
*1, 5, 21, 85, 341, 1365, ...., (4^N-1)/3 *on remarque que chaque valeur est égale à 1 quatre fois la plus grande valeur inférieure, U(1) contient N valeurs impaires toutes différentes.
Définissons l’ensemble U(2) comme suit :
on prend chaque valeur de U(1) soit U(1,n) pour n de 1 à N
SI U(1,n) est 1 modulo 6 on défini les termes de U(2)=(U(1,n)*4^n-1)/3 pour n de 0 à N
SI U(1,n) est 5 modulo 6 on défini les termes de U(2)=(U(1,n)*2^(2*n-1)-1)/3 pour ne de 0 à N
U(2) contient 2*N*N/3 valeurs impaires toutes différentes et toutes les valeurs impaires de U(2) sont différentes des valeurs de U(1)
On continu avec la même règle pour définir U(i 1) à partir de U(i)
Les valeurs dans U(i) non multiples de 3 sont les valeurs obtenues à partir des valeurs dans U(i 1) dans une suite de Collatz.
Une preuve de la validité de la conjecture pas accessible à tout le monde !

-
-

### Le problème 3n+1 : y a-t-il des cycles non triviaux ? (III)

#### le 25 février 2019 à 22:18, par Trebla

Bonsoir. Je propose une approche matricielle

Document joint : [syrdem2-converti.pdf][15]

  -
  -

### Le problème 3n+1 : y a-t-il des cycles non triviaux ? (III)

#### le 5 mai 2019 à 17:39, par Trebla

Sauf faille de raisonnement difficile à déceler, j’ai l’honneur de prétendre avoir résolu, ou presque, la conjecture de Syracuse par la méthode inverse et une approche matricielle. L’approche matricielle, qui se veut globale, pourrait nous dispenser de nous noyer dans des calculs inextricables tels que ceux qui sont proposés çà et là ainsi que des considérations d’altitude maximale et de temps de vol, considérations qui ont montré leurs limites face à la boîte de Pandore d’où ont toujours surgi de nouveaux cas calculatoires à résoudre sitôt en résolu un. Les considérations de Théorie des Nombres en tant que telle n’ont pas non plus mené bien loin.
L’ensemble de tous les antécédents de 1 devrait se confondre avec celui des entiers positifs qui lui sont supérieurs.

Document joint : [syrdem2-converti-2.pdf][16]

    -
    -

### Le problème 3n+1 : y a-t-il des cycles non triviaux ? (III)

#### le 9 mai 2019 à 13:00, par électron

Albert,
votre document ne constitue pas vraiment une preuve (loin s’en faut), mais l’idée est pertinente. Elle a même déjà été développée, notamment par Alves et al (2005), sans succès à ce jour. D’autre part, cette approche matricielle ne dit rien, me semble-t-il, sur l’existence hypothétique de trajectoires divergentes.
Vous pouvez me contacter par mail via le site www.probleme-syracuse.fr pour en discuter directement.
Olivier R

-
-

### Le problème 3n+1 : y a-t-il des cycles non triviaux ? (III)

#### le 30 mai 2021 à 17:39, par Nicolas

Très bon article jusqu’à l utilisation de Farey. Il est possible, sauf erreur de ma part, d obtenir un résultat bien meilleur en utilisant la formule de la durée.

Je note I nb d’éléments impairs, P nb d’éléments pairs , durée D = P+I
N entier positif

On a 2^p / (3^I * N) > 1 appelé aussi résidu de N (voir le site d’ eric roosendaal on y trouve une conjecture sur la valeur maximale de ce résidu mais sa valeur minimale est toujours supérieur à 1)

En utilisant le fait que 3^I = 2^ (P*I/P*log 3 / log 2) on obtient 2^(P *(1-I/P*log 3 / log 2))/N>1
Maintenant on passe N de l’autre côté, on met au log des 2 côtés et on divise par log 2, cela donne : P*(1-I/P*log 3 / log 2) > log N / log 2 soit P > log N / (log 2-I/P*log 3)

J espère que ça reste clair malgré la notation en ligne :)
En multipliant la dernière ligne par I/P on a I > log N * I/P / (log 2-I/P*log 3)
Et enfin en additionnant P+I = D > log N * (1+I/P) / (log 2-I/P*log 3)

Le plus dur est fait :) on sait que N > 5×10^18 et I/P > log 2 / log (3+2×10^-19) la relation inverse par rapport à celle dans l article, on met ces nombres dans la formule de D et on obtient D > 4,4*10^46 soit un nombre un peu plus grand que 18 milliard ;)

Bien sûr il est possible de calculer exactement I , P et D comme à la fin de l article mais le nombre obtenu ici est tellement grand que je vous laisse faire ce calcul.
Sans parler du fait que les nombres utilisés ont été amélioré.

Voilà, voilà, ce résultat renforce l’idée qu il n y a pas de cycles non triviaux.

-
-

### Le problème 3n+1 : y a-t-il des cycles non triviaux ? (III)

#### le 31 mai 2021 à 09:28, par Nicolas

Évidemment la formule dans mon message précédent ne fonctionne pas car le cycle ne passe pas par 1, je viens de comprendre, c est très bien Farey en fait :)

---


## Links

[1]: Le-probleme-3n-1-elementaire-mais-redoutable-I.html
[2]: Le-probleme-3n-1-cycles-de-longueur-5-II.html
[3]: _Ghys-Etienne_.html
[4]: http://www.ieeta.pt/~tos/3x+1.html
[5]: http://www.jasondavies.com/
[6]: http://www.math.lsa.umich.edu/~lagarias
[7]: Nombres-et-representations.html
[8]: Calendriers-et-fractions-continues.html
[9]: http://fr.wikipedia.org/wiki/Fonction_homographique
[10]: http://wims.unicaen.fr/wims/wims.cgi?session=9MD32885C4.2&amp;+lang=fr&amp;+module=tool%2Fnumber%2Fcalcnum.fr
[11]: http://wims.unicaen.fr/wims/wims.cgi?lang=fr
[12]: http://www.wolframalpha.com/
[13]: http://maxima.sourceforge.net/
[14]: img/arton1087.png
[15]: img/pdf/syrdem2-converti.pdf
[16]: img/pdf/syrdem2-converti-2.pdf
