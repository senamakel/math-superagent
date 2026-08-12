<!-- source: https://hal.science/hal-02300013/document | converted from PDF -->

HAL Id: hal-02300013

https://hal.science/hal-02300013v1

Submitted on 29 Sep 2019

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

Distributed under a Creative Commons CC BY-NC-SA 4.0 - Attribution - Non-commercial use - ShareAlike -
International License

Suite de permutations lors d’une course de n coureurs de
vitesses constantes

Hugues Déprés

To cite this version:

Hugues Déprés. Suite de permutations lors d’une course de n coureurs de vitesses constantes. [Rapport de
recherche] Ecole normale supérieure de lyon - ENS LYON. 2019. ⟨hal-02300013⟩

Suite de permutations lors d'une course de n coureurs de vitesses constantes

Suite de permutations lors d'une course de n coureurs de vitesses constantes
 Hugues Déprés

Résumé : On considère n coureurs avec des vitesses constantes et di˙érentes sur une piste circulaire de longueur unitaire.
On les numérote de 1 à n ; leur ordre sur la piste forme une permutation.On étudie la suite de ces permutations au cours
du temps et plus particulièrement, combien de permutations apparraissent.

On utilise le théorème de Kronecker pour montrer qu'avec des vitesses Q linéairement indépendantes, toutes les permuta-
tions apparraissent. On montre également que, dans ce cas, les fréquences d'apparition sont les mêmes. Plus généralement
on donne une méthode géométrique pour calculer la fréquence dans un cas quelconque.

1. Introduction

On s'intéresse à n coureurs de dossards numérotés de 1 à n dans une course, sur un circuit circulaire, pendant un nombre
in˝ni de tours (˝gure 1,voir annexe).

On suppose que leurs vitesses sont constantes, toutes di˙érentes et on les notera v 1 < v 2 < v 3 <    < v n .

On appelle alors permutation, la liste d'entiers de [[1 ; n ]] obtenue par lecture des numéros des coureurs, dans l'ordre, à
partir de la ligne de départ, à un instant où ils ne se dépassent pas.

C'est une permutation des entiers de [[1 ; n ]] .

On note cette permutation : ( x 1 ; x 2 ; : : : ; x n ) avec x i 2 [[1 ; n ]] pour i 2 [[1 ; n ]] . Par exemple, la ˝gure 1 correspond à la
permutation (4,5,1,3,2). La permutation suivante dépend de l'évènement qui se produit en premier :

 soit le coureur 5 (le plus rapide) dépasse le coureur 1 ce qui donne la permutation (4,1,5,3,2),
 soit le coureur 2 franchit la ligne ce qui donne la permutation (2,4,5,1,3),
 soit le coureur 3 dépasse le coureur 2 ce qui donne la permutation (4,5,1,2,3).

Ce problème est inspiré de questions posées dans [1] et [3].

L'objet de ce travail est l'étude de la suite des permutations apparaissant au cours du temps et plus particulièrement :

 trouver cas toutes les permutations apparraissent,
 sinon savoir lesquelles apparaissent,
 trouver la fréquence d'apparition de chaque permutation.

2. Table des matières

1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
2. Table des matières . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
3. Simpli˝cations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
4. Cas particulier : n = 2 coureurs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
5. Théorème d'approximation de Kronecker . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
6. Cas de n coureurs de vitesses Q-linéairement indépendantes . . . . . . . . . . . . . . . . . . . . . . . . . . 2
7. Introduction d'une base . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
8. Symétrie du problème . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
9. Cas de n = 3 coureurs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
10. Cas de n = 4 coureurs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
11. Fréquence d'apparition de chaque permutation pour des vitesses Q-linéairement indépendantes . . . . . . 5
12. Fréquences d'apparition pour des coureurs de vitesse non Q-linéairement indépendantes . . . . . . . . . . 8
13. Cas où les n vitesses forment un Q espace vectoriel de dimension n-1 . . . . . . . . . . . . . . . . . . . . . 9
14. Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
15. Bibliographie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
16. Figures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

3. Simpli˝cations

On normalise le problème en considérant que le temps et la longueur du circuit sont tels qu'un coureur de vitesse 1 met
un temps 1 pour e˙ectuer un tour.

La position des coureurs sur le circuit est alors déterminée par la partie fractionnaire de leur vitesse multipliée par
le temps t depuis le début de la course : c'est à dire les parties fractionnaires de v 1 t; v 2 t; : : : ; v n t que l'on notera
f v 1 t g ; f v 2 t g ; :::; f v n t g où f x g désigne la partie fractionnaire de x .

1

Suite de permutations lors d'une course de n coureurs de vitesses constantes

Si v = ( v 1 ; v 2 ; : : : ; v n ) est le vecteur des vitesses, alors on notera f t: vg le vecteur des parties fractionnaires des positions :
f t: vg = ( f v 1 t g ; f v 2 t g ; :::; f v n t g ) .

Lemme 1. Dans le cas où au plus un croisement se produit à un instant t , soit entre 2 coureurs, soit entre un
coureur et la ligne d'arrivée, alors,la permutation suivante s'obtient :

 soit en échangeant deux éléments consécutifs dont le premier a une vitesse plus grande que le deuxième,
 soit en mettant le dernier élément en 1 er et en décalant tous les autres.

En e˙et, un coureur qui va moins vite ne peut pas doubler un coureur qui va plus vite.

Cependant, la situation se complique si plusieurs croisements se produisent en même temps, car il faut alors séparer les
coureurs en groupes qui se croisent au même point et en déduire les e˙ets sur la nouvelle permutation.

Dans chaque groupe (voir ˝gure 2), c'est le coureur le plus rapide qui sera le premier après le croisement et ainsi de suite
dans l'ordre décroissant des vitesses.

Lemme 2. Tous les coureurs se retrouvent au départ après un certain temps T () tous les rapports de vitesses
sont rationnels.

Preuve 1. Il existe p i entier (nombre de tours parcouru) tel que v i  T = p i  1 (la longueur du parcours est 1 ) et donc
v i
v j est rationnel.

Réciproquement, si k j  v 1 = p j  v j alors on choisit T = 1
v 1
 nY

i =2 p i  1

4. Cas particulier : n = 2 coureurs

Théorème 3. Dans le cas n = 2 , toutes les permutations apparaissent et la suite des permutations est périodique
de période 2 : les permutations (1,2) et (2,1) alternent.

5. Théorème d'approximation de Kronecker

Dé˝nition 1. Des réels v 1 ; v 2 ; : : : ; v n sont dit Q-linéairement indépendants s'il n'existe pas d'entiers a 1 ; :::; a n , non tous
nuls, véri˝ant : a 1 v 1 + a 2 v 2 + ::: + a n v n = 0

Théorème 4 (Kronecker [5, Théorème 444 p486]) . Si v 1 , v 2 , ..., v n sont Q-linéairement indépendants, alors pour
tous réels r 1 , r 2 , ..., r n , " et T , on peut trouver un réel t > T et des entiers p 1 , p 2 , ..., p n tels que pour tout i
entre 1 et n on ait :
 j v i t   p i   r i j < 

6. Cas de n coureurs de vitesses Q-linéairement indépendantes

Une conséquence du théorème d'approximation de Kronecker est le théorème suivant :

En dé˝nissant n valeurs distinctes r i parmi les valeurs 2 k   1
2 n avec k 2 [[1 ; n ]] et " < 1
2 n , par exemple

0 1
n 2
n

r 1
" " r 2
" "
 k   1
n
 r k
" "
 k
n n   1
n
 r n
" "
 1

le théorème de Kronecker garantit qu'il existe un temps t pour lequel les n coureurs sont proches, à moins de " , d'un r i .

On en déduit le théorème suivant en utilisant les n ! choix possibles pour les r i sur les n positions  2 k   1
2 n
 
 k =1 ;:::;n .

Théorème 5. Si les vitesses sont Q-linéairement indépendantes, les n ! permutations possibles pour n coureurs
apparaissent.

7. Introduction d'une base

Le théorème de Kronecker permet de traiter les cas de vitesses Q-linéairement indépendantes, mais pas les autres cas.
Or, on a envie de l'utiliser quand seulement une partie des vitesses sont Q-linéairement indépendantes entre elles.

2

Suite de permutations lors d'une course de n coureurs de vitesses constantes

Lemme 6. On peut écrire les vitesses des coureurs comme combinaisons linéaires à coe˚cients entiers de quan-
tités Q-linéairement indépendantes.

C'est-à-dire : pour tous réels ( v 1 ; v 2 ; : : : ; v n ) , il existe un entier r 6= 0 , des entiers ( c i;j ) i 2 [[1 ;n ]] ;j 2 [[1 ;r ]] et des réels
w 1 ; w 2 ; : : : ; w r Q-linéairement indépendants tels que 8 i 2 [[1 ; n ]] , v i = X

j 2 [[1 ;r ]] c i;j w j .

Si on prend R comme Q-espace vectoriel, il s'agit en fait d'extraire d'une famille de vecteurs, une base de l'espace
engendré par ( v 1 ; v 2 ; : : : ; v n ) que l'on modi˝e pour avoir des c i;j entiers.

Preuve 2. Si les vitesses des coureurs ne sont pas Z-linéairement indépendantes, on a pour un entier i 1 2 [[1 ; n ]] ,
mv i 1 = X

j 6= i 1 b j v j avec m; b 1 ; b 2 ; ::: entiers. On pose alors v j; 1 = v j
m , alors on a v i 1 = X

j 6= i 1 b j v j; 1 .

Si les n   1 quantités ( v j; 1 ) j 6= i 1 ne sont pas Z-linéairement indépendantes, on recommence : l'une des vitesse v i 2 s'écrit
mv i 2 = P
 j 6= i 2 b j v j avec m; b 1 ; b 2 ; ::: entiers.

On crée ainsi des quantités ( v j; 2 ) , ( v j; 3 ) , ::: qui sont en nombre décroissant, jusqu'à avoir des quantités ( v j;p ) j 2 [[1 ;r ]] qui
sont Z-linéairement indépendantes et qui permettent d'écrire les vitesses des coureurs.

Les vitesses v 1 ; v 2 ; : : : ; v n s'écrivent alors comme combinaisons linéaires à coe˚cients entiers de ces ( v j;r ) j 2 [[1 ;r ]]

8. Symétrie du problème

Dans une con˝guration donnée : n coureurs de vitesse v 1 ; v 2 ; : : : ; v n , on obtient une certaine suite de permutations.

Si on renverse le temps, on va obtenir la suite des permutations renversées : ( a 1 ; a 2 ; : : : ; a n ) devient ( a n ; a n   1 ; : : : ; a 1 ) .

On se pose donc la question de savoir si ces permutations renversées apparaissent quand le temps s'écoule normalement.

On observe dans les simulations que le nombre de permutations est toujours pair. On conjecture donc que si une
permutation ( a 1 ; a 2 ; : : : ; a n ) apparaît dans la suite de permutations, alors la permutation renversée ( a n ; a n   1 ; : : : ; a 1 )
apparaît aussi.

On utilise le lemme précédent et le théorème d'approximation de Kronecker pour prouver le théorème suivant :

Lemme 7. Pour tout " > 0 et pour tout temps T , on peut trouver un instant t > T tel que à t , tous les coureurs
sont à une distance au plus " de la ligne d'arrivée.

8 " > 0 , 8 T 2 R, 9 t > T : 8 i 2 [[1 ; n ]] , jf v i t gj ⩽ " ou j 1   f v i t gj ⩽ "

Preuve 3. On utilise les quantités ( v j;r ) j dé˝nies par le lemme précédent et qui permettent d'écrire les vitesses des
coureurs.

Soit " 0 > 0 . D'après le théorème de Kronecker, on peut trouver un temps T tel que pour t > T , ces quantités donnent
des positions à une distance " 0 près de la ligne d'arrivée : 8 j , jf v j;r t gj ⩽ " 0 .

Si v i = X
 j b i;j v j;r avec b i;j des entiers dé˝nis au lemme 2, alors la distance de v i à la ligne d'arrivée est majorée par

P
 j j b i;j j " 0 : jf v i t gj ⩽ P
 j j b i;j j " 0 .

Il su˚t donc de prendre " 0 = "
max i P
 j j b i;j j et on a le résultat :

il existe un temps T tel que pour t > T , 8 i 2 [[1 ; n ]] , jf v i t gj ⩽ "

On obtient donc le théorème suivant qui prouve la symétrie du problème pour toutes les con˝gurations de vitesse (˝gure
6) :

Théorème 8. Si il existe un réel t 2 R+ et des vitesses v 1 ; v 2 ; : : : ; v n telles qu'on observe une permutation
( a 1 ; a 2 ; : : : ; a n ) , alors il existe un temps t 0 2 R+ tel qu'on observe la permutation ( a n ; a n   1 ; : : : ; a 1 ) .

Preuve 4. Soit " , d'après le lemme précédent, il existe t 0 > t tel que ( v 1 t 0 ; v 2 t 0 ; : : : ; v n t 0 ) soient à une distance de moins
de " d'un entier.

Alors à l'instant t 0   t , f v 1 ( t 0   t ) g ; f v 2 ( t 0   t ) g ; : : : ; f v n ( t 0   t ) g est à une distance au plus " de 1   f v 1 ( t ) g ; 1  
f v 2 ( t ) g ; : : : ; 1   f v n ( t ) g .

On note d ( a; b ) = min( j b   a j ; 1   j b   a j ) la distance modulo 1.
 3

Suite de permutations lors d'une course de n coureurs de vitesses constantes

On prend " < 1
2 max  max i 6= j d ( f v i t g ; f v j t g ) ; max i d ( f v i t g ; 0) ; 

Alors on a bien la permutation ( a n ; a n   1 ; : : : ; a 1 ) à l'instant t 0   t .

9. Cas de n = 3 coureurs

Dans le cas n = 3 , la première permutation est (1,2,3) juste après le départ.

Comme les coureurs sont dans l'ordre de leurs vitesses, aucun dépassement ne peut avoir lieu avant que le plus rapide
ne franchisse la ligne : la deuxième permutation est (3,1,2).

La troisième permutation est (2 ; 3 ; 1) si le coureur 2 termine son tour avant que le 3 ne double le 1 ou bien dans le cas
contraire, la troisième permutation est (1 ; 3 ; 2) (˝gure 3).

On obtient l'arbre de la ˝gure 4 pour les évolutions possibles des permutations sans croisement simultané : pas de
dépassement en même temps qu'un passage de la ligne d'arrivée. L'astérisque signale une permutation qui est déjà
apparue dans l'arbre.

Le résultat suivant est connu pour n = 3 avec des vitesses entières [2] et on le prouve en utilisant la symétrie du problème.

Théorème 9. Les 6 permutations apparaissent pour la con˝guration v 1 < v 2 < v 3 si et seulement si v 1 + v 2 6= v 3 .

Seul les permutations (1 ; 2 ; 3) ; (2 ; 1 ; 3) ; (3 ; 1 ; 2) ; (3 ; 2 ; 1) apparaissent quand v 1 + v 2 = v 3 .

Preuve 5. Si v 3 = v 1 + v 2 , alors suposons que la permutation (1 ; 3 ; 2) apparaisse. Il existe un réel t > 0 tel que

f v 1 t g < f ( v 1 + v 2 ) t g < f v 2 t g ce qui donne v 1 t   b v 1 t c < ( v 1 + v 2 ) t   b ( v 1 + v 2 ) t c < v 2 t   b v 2 t c .

On obtient alors :

‹ soit v 1 t   b v 1 t c < ( v 1 + v 2 ) t   b v 1 t c   b v 2 t c < v 2 t   b v 2 t c

d'où 0 ⩽ v 2 t   b v 2 t c ⩽ ( v 2 t   b v 2 t c ) + ( b v 1 t c   v 1 t ) et donc, 0 ⩽ v 2 t   b v 2 t c < v 2 t   b v 2 t c ce qui est absurde,

‹ soit v 1 t   b v 1 t c < ( v 1 + v 2 ) t   b v 1 t c   b v 2 t   1 c + 1 < v 2 t   b v 2 t c

d'où 0 ⩽ v 2 t   b v 2 t c + 1 ⩽ ( v 2 t   b v 2 t c ) + ( b v 1 t c   v 1 t ) et donc, 0 ⩽ v 2 t   b v 2 t c + 1 < v 2 t   b v 2 t c ce qui est absurde.

Donc la permutation (1 ; 3 ; 2) n'arrive pas. De plus, par symétrie, (2 ; 3 ; 1) n'arrive pas.

Mais, comme (1 ; 2 ; 3) et (3 ; 1 ; 2) apparaissent et, par symétrie, (3 ; 2 ; 1) et (2 ; 1 ; 3) apparaissent aussi, alors l'ensemble des
permutations est f (1 ; 2 ; 3) ; (3 ; 2 ; 1) ; (2 ; 1 ; 3) ; (3 ; 2 ; 1) g .

Si v 3 6= v 1 + v 2 , alors (1 ; 2 ; 3) et (3 ; 1 ; 2) apparaissent. Ensuite, c'est soit (2 ; 3 ; 1) , soit (1 ; 3 ; 2) , soit 2 croise la ligne en

même temps que 3 double 1 , alors ˆ v 3 t   1 = v 2 t
v 2 t = 1 = ) v 3 = v 1 + v 2 . Par symétrie, toutes les permutations

apparaissent.

10. Cas de n = 4 coureurs

Si on connaît la suite de permutations générée par n = 4 coureurs, comme la position d'un coureur ne dépend que du
temps, pour connaître la suite de permutations générés par les 3 premiers coureurs, il su˚t d'enlever le coureur 4 de
toute la suite de permutations (et de supprimer les permutations identiques consécutives).

Par conséquent, pour obtenir le nombre maximal de permutations pour n = 4 coureurs, il faut que chaque sous-ensemble
de 3 coureurs véri˝e la contrainte pour n = 3 coureurs obtenue précédemment : v 3 6= v 1 + v 2 . Dans le cas contraire, au
plus 16 permutations peuvent apparaitre (En e˙et, pour chaque permutation du cas n = 3 qui ne peut pas apparaitre,
4 permutations du cas n = 4 , ne peuvent pas apparaitre).

Mais ces contraintes ne su˚sent pas comme l'indique le théorème suivant :

Théorème 10. Si v 2 + v 3 = v 1 + v 4 , alors au plus 16 permutations peuvent apparaitre.

Preuve 6. On a alors

( v 4   v 3 ) + ( v 4   v 2 ) = v 4   v 1
Alors ( v 4   v 3 ; v 4   v 2 ; v 4   v 1 ) sont 3 vitesses dont l'une est la somme des 2 autres, alors elles correspondent à une
con˝guration à 3 coureurs dont toutes les permutations n'apparaissent pas.

On en déduit que pour la con˝guration ( v 4   v 3 ; v 4   v 2 ; v 4   v 1 ; v 4 ) toutes les con˝gurations n'apparaissent pas.

En e˙et le nombre de permutations est le même que pour ( v 1 ; v 2 ; v 3 ; v 4 ) : considèrons la ligne d'arrivée comme un coureur
de vitesse 0, et maintenant observons la course depuis le coureur de vitesse v4. Pour lui c'est comme si les autres coureurs
tournaient dans l'autre sens avec les vitesses ( v 4   v 3 ; v 4   v 2 ; v 4   v 1 ) . On conclut en remarquant qu'il existe une bijection
entre les permutations obtenus par ces 2 visions.
 4

Suite de permutations lors d'une course de n coureurs de vitesses constantes

En particulier pour ( v 1 ; v 2 ; v 3 ; v 4 ) = (1 ; 4 ; 7 ; 10) , par simulation, on constate que 16 permutations apparaissent sur les 24
possibles. Mais, on a v 3 6= v 1 + v 2 , v 4 6= v 1 + v 2 , v 4 6= v 1 + v 3 et v 4 6= v 3 + v 2 , donc toutes les permutations de chacun
des sous-ensembles de 3 coureurs apparaissent.

11. Fréquence d'apparition de chaque permutation pour des vitesses Q-linéairement indé-
pendantes

On note f xg le vecteur des parties fractionnaires des composantes du vecteur x,

On note ˜ [ a;b ] la fonction caractéristique du pavé [ a; b] = f x = ( x 1 ; x 2 ; : : : ; x n ) j 8 j 2 [[1 ; n ]] ; a j ⩽ x j ⩽ b j g

avec a = ( a 1 ; a 2 ; : : : ; a n ) , b = ( b 1 ; b 2 ; : : : ; b n ) .

On note f : t 7! ( f 1 ( t ) ; f 2 ( t ) ; : : : ; f n ( t )) une fonction continue de [0 ; + 1 [ dans Rn .

Dé˝nition 2. On dit que la fonction f est équirépartie modulo 1 sur Rn si

lim
T ! + 1 1
T
 Z T

0 ˜ [ a; b] ( f f ( t ) g ) d t =
 nY

j =1 ( b j   a j )

pour tous pavés [ a; b[ ˆ [0 ; 1] n avec a = ( a 1 ; a 2 ; : : : ; a n ) ; b = ( b 1 ; b 2 ; : : : ; b n )

Kuipers et Niederreiter [4] dé˝nissent les fonctions équiréparties en dimension n mais ne donnent pas le théorème suivant :

Théorème 11. La fonction f est équirépartie modulo 1 sur [0 ; 1] n si et seulement si pour toute fonction continue
w : [0 ; 1] n  ! R, on a
 lim
T ! + 1 1
T
 Z T

0 w ( f f ( t ) g ) d t = Z
 [0 ; 1] n w ( x) d x

Preuve 7. Réécrivons la dé˝nition de l'équirépartition pour la fonction f :

f est équirépartie modulo 1 sur [0 ; 1] n () 8 a; b 2 [0 ; 1] n , lim
T ! + 1 1
T
 Z T

0 ˜ [ a; b] ( f f ( t ) g ) d t = Z
 [0 ; 1] n ˜ [ a; b] ( x) d x

Soit f équirépartie modulo 1 sur [0 ; 1] n , alors la propriété

P ( h ) :  lim
T ! + 1 1
T
 Z T

0 h ( f f ( t ) g ) d t = Z
 [0 ; 1] n h ( x) d x 

est vraie par linéarité pour toute fonction en escalier h : [0 ; 1] n ! R.

Soit w une fonction continue sur [0 ; 1] n . [0 ; 1] n est compact, donc on peut appliquer le théorème de Heine. On en déduit
que w est uniformément continue.

Alors pour tout " > 0 , il existe une fonction en escalier h telle que jj w   h jj 1 ⩽ "
3 .

Alors pour tout T > 0 ,

1
T
 Z T

0 w ( f f ( t ) g ) d t   Z
 [0 ; 1] n w ( x) d x = 1
T
 Z T

0 w ( f f ( t ) g ) d t   1
T
 Z T

0 h ( f f ( t ) g ) d t

+ 1
T
 Z T

0 h ( f f ( t ) g ) d t   Z
 [0 ; 1] n h ( x) d x

+ Z
 [0 ; 1] n h ( x) d x   Z
 [0 ; 1] n w ( x) d x

On en déduit par inégalité triangulaire et par linéarité et croissance de l'intégrale :

 1
T
 Z T

0 w ( f f ( t ) g ) d t   Z
 [0 ; 1] n w ( x) d x

 ⩽ 1
T
 Z T

0 j ( w   h )( f f ( t ) g ) j d t

+

 1
T
 Z T

0 h ( f f ( t ) g ) d t   Z
 [0 ; 1] n h ( x) d x

+ Z
 [0 ; 1] n j ( h   w )( x) j d x

5

Suite de permutations lors d'une course de n coureurs de vitesses constantes

D'après la propriété P ( h ) , il existe T 1 tel que pour tout T ⩾ T 1 , on a

 1
T
 Z T

0 h ( f f ( t ) g ) d t   Z
 [0 ; 1] n h ( x) d x

 ⩽ "
3 .

On en déduit que

 1
T
 Z T

0 w ( f f ( t ) g ) d t   Z
 [0 ; 1] n w ( x) d x

 ⩽ 1
T
 Z T

0
 "
3 d t + "
3 + Z
 [0 ; 1] n "
3 d x ⩽ "

Ce qui prouve lim
T ! + 1 1
T
 Z T

0 w ( f f ( t ) g ) d t = Z
 [0 ; 1] n w ( x) d x

La réciproque se démontre de la même façon que le théorème 12 (ci-dessous Preuve 8).

Dé˝nition 3. Pour ˙ 2 S n une permutation de [[1 ; n ]] , on dé˝nit :

V ˙ =  v = ( v 1 ; v 2 ; : : : ; v n ) 2 [0 ; 1] n j v ˙ (1) ⩽ v ˙ (2) ⩽    ⩽ v ˙ ( n ) 	 .

Théorème 12. Soit f une fonction équirépartie modulo 1 sur [0 ; 1] n .

Pour tout ˙ appartenant à S n , lim
T ! + 1 1
T
 Z T

0 ˜ V ˙ ( f f ( t ) g ) d t = Z
 [0 ; 1] n ˜ V ˙ ( x) d x

Preuve 8.

Soit " > 0 . On dé˝nit f  
" = min  1 ; d ( x; V ˙ )
"
  et f +
" = max  0 ; 1   d ( x; V ˙ )
"
  .

On a
 f +
" ⩾ ˜ V ˙ ⩾ f  
" .

qui donne Z
 [0 ; 1] n f +
" ( x) d x ⩾ Z
 [0 ; 1] n ˜ V ˙ ( x) d x ⩾ Z
 [0 ; 1] n f  
" ( x) d x (1) .

Soit S la surface de contact entre V ˙ et V ˙ , alors

0 ⩽ Z
 [0 ; 1] n f +
" ( x) d x   Z
 [0 ; 1] n f  
" ( x) d x ⩽ 2 "S (2)

Par ailleurs, pour T > 0 , on a pour tout t 2 [0 ; T ] :

f +
" ( f f ( t ) g ) ⩾ ˜ V ˙ ( f f ( t ) g ) ⩾ f  
" ( f f ( t ) g ) .

qui donne par croissance de l'intégrale
 1
T
 Z T

0 f +
" ( f f ( t ) g ) d t ⩾ 1
T
 Z T

0 ˜ V ˙ ( f f ( t ) g ) d t ⩾ 1
T
 Z T

0 f  
" ( f f ( t ) g ) d t .

Comme les fonctions f +
" et f  
" sont continues, on peut appliquer le théorème 11 et on trouve :
Z
 [0 ; 1] n f +
" ( x) ⩾ 1
T
 Z T

0 ˜ V ˙ ( f f ( t ) g ) d t ⩾ Z
 [0 ; 1] n f  
" ( x) (3) .

Les inégalités (1) , (2) et (3) donnent
 0 ⩽ Z T

0 ˜ V ˙ ( f f ( t ) g ) d t   Z
 [0 ; 1] n ˜ V ˙ ( x) d x ⩽ 2 "S

On conclut en faisant tendre " vers 0.

Or les V ˙ ont par symétrie tous le même volume, ils sont disjoints sauf aux bords et leur union donne [0 ; 1] n , donc par

théorème de Chasles : Z
 [0 ; 1] n ˜ V ˙ ( x) d x = 1
jS n j = 1
n ! .

De plus, on a le critère suivant, en notant < x; y > le produit scalaire canonique de Rn :

6

Suite de permutations lors d'une course de n coureurs de vitesses constantes

Théorème 13 ([4, Théorème 9.9 p83]) . La fonction f est équirépartie modulo 1 sur Rn si et seulement si pour
tout vecteur h de Z
n , h 6= 0,
 lim
T ! + 1 1
T
 Z T

0 e 2 ˇi< h; f ( t ) > d t = 0

Preuve 9. On prouve que le théorème 11 implique le théorème 13.

= )

On suppose que la fonction f est équirépartie modulo 1 sur Rn .

La fonction x 7! e 2 ˇi< h; x> est continue sur [0 ; 1] n .

Alors, on a, d'après le théorème 11, en utilisant Z 1

0 e 2 ˇix d x = 0 pour tout entier non nul  et ici h 6= 0 :

lim
T ! + 1 1
T
 Z T

0 e 2 ˇi< h; f f ( t ) g > d t = Z
 [0 ; 1] n e 2 ˇi< h; x> d x (1)

= Z Z ::: Z 1

0 e 2 ˇi P h k x k d x 1 d x 2 ::: d x n (2)

= 0 (3)

( =

On suppose maintenant que pour tout vecteur h de Z
n , h 6= 0, lim
T ! + 1 1
T
 Z T

0 e 2 ˇi< h; f ( t ) > d t = 0 .

On note ( ei) i les vecteurs de la base canonique de Rn .

Soit w une fonction continue véri˝ant pour tout x 2 [0 ; 1] n , w ( x + ei) = w ( x) pour tout i .

Alors d'après le théorème de Stone-Weierstrass trigonométrique (ADMIS), il existe une suite de polynômes trigonomé-
triques qui convergent uniformément vers w .

Soit " > 0 . Il existe un polynôme trigonométrique P qui s'écrit : P ( x) = X

h2 H c he 2 ˇi< h; x> avec H ˝ni tel que jj w   P jj 1 ⩽

" .

Alors,

 1
T
 Z T

0 w ( f f ( t ) g ) d t   Z
 [0 ; 1] n w ( x) d x

 ⩽

 1
T
 Z T

0 w ( f f ( t ) g )   P ( f f ( t ) g ) d t

+

 1
T
 Z T

0 P ( f f ( t ) g ) d t   Z
 [0 ; 1] n P ( x) d x

+

 Z
 [0 ; 1] n P ( x)   w ( x) d x

On a

 1
T
 Z T

0 w ( f f ( t ) g )   P ( f f ( t ) g ) d t

 ⩽ 1
T
 Z T

0 j w ( f f ( t ) g )   P ( f f ( t ) g ) j d t ⩽ 1
T
 Z T

0 " d t = "

et

 Z
 [0 ; 1] n P ( x)   w ( x) d x

 ⩽ Z
 [0 ; 1] n j P ( x)   w ( x) j d x ⩽ Z
 [0 ; 1] n " d x = "

On a e 2 ˇi< h; f ( t ) > = e 2 ˇi< h; f f ( t ) g > + c où c est un entier. Alors e 2 ˇi< h; f ( t ) > = e 2 ˇi< h; f f ( t ) g >

Par linéarité, lim
T ! + 1 1
T
 Z T

0 P ( f f ( t ) g ) d t = lim
T ! + 1 1
T
 Z T

0
 X

h2 H c he 2 ˇi< h; f f ( t ) g > d t

Pour les termes non constants de P , lim
T ! + 1 1
T
 Z T

0 c he 2 ˇi< h; f f ( t ) g > d t = lim
T ! + 1 c h 1
T
 Z T

0 e 2 ˇi< h;f ( t ) > d t = 0 car h 6= 0

Pour le terme constant, h 6= 0 , on a lim
T ! + 1 1
T
 Z T

0 c 0e 2 ˇi< 0 ; f f ( t ) g > d t = c 0.

7

Suite de permutations lors d'une course de n coureurs de vitesses constantes

Et Z
 [0 ; 1] n P ( x) d x = Z
 [0 ; 1] n
 X

h2 H c he 2 ˇi< h;x> d x.

Or pour h 6= 0 , on a Z
 [0 ; 1] n c he 2 ˇi< h;x> d x = 0 donc Z
 [0 ; 1] n P ( x) d x = Z
 [0 ; 1] n
 X

h2 H c he 2 ˇi< h;x> d x = Z
 [0 ; 1] n c 0 d x = c 0

Alors lim
T ! + 1 1
T
 Z T

0 P ( f f ( t ) g ) d t   Z
 [0 ; 1] n P ( x) d x = 0 .

Il existe donc T 1 tel que pour T ⩾ T 1 ,

 1
T
 Z T

0 P ( f f ( t ) g ) d t   Z
 [0 ; 1] n P ( x) d x

 ⩽ "

Alors pour T ⩾ T 1 ,

 lim
x ! 1 + 1
T
 Z T

0 w ( f f ( t ) g ) d t   Z
 [0 ; 1] n w ( x) d x

 ⩽ 3 "

On a prouvé lim
x ! 1 + 1
T
 Z T

0 w ( f f ( t ) g ) d t = Z
 [0 ; 1] n P ( x) d x

Si w ne véri˝e pas w ( x + ei) = w ( x) pour tout i , alors on applique la propriété à g véri˝ant g ( x + ei) = g ( x) pour tout

i et Z
 [0 ; 1] n j w   g j ⩽ " 0 avec g une fonction continue, dé˝nie par morceaux.... (ADMIS)

En notant g la fonction t 7! ( v 1 t; v 2 t; : : : v n t ) = t: ( v 1 ; : : : ; v n ) , on a < h; g( t ) > = t < h; ( v 1 ; : : : ; v n ) > . D'autre part, on

sait que lim
T ! + 1 1
T
 Z T

0 e 2 ˇit d t = 0 si et seulement si  6= 0

Or < h; ( v 1 ; : : : ; v n ) > n'est jamais nul lorsque les vitesses sont Q-linéairement indépendantes, donc d'après le critère
précédent, la fonction g est équirépartie modulo 1.

On prend comme dé˝nition pour la fréquence d'apparition d'une permutation ˙ , dans le problème des coureurs, la
proportion du temps pendant lequel la permutation apparaît. Ce qui conduit à la dé˝nition suivante :

Dé˝nition 4. On appelle fréquence d'apparition d'une permutation ˙ le réel suivant, quand il existe :

lim
T ! + 1 1
T
 Z T

0 ˜ V ˙ ( f ( v 1 t; v 2 t; : : : ; v n t ) g ) d t .

On déduit des résultats précédents :

Théorème 14. Les fréquences d'apparition des permutations sont identiques et égales à 1
n ! , lorsque les vitesses
sont Q-linéairement indépendantes.

12. Fréquences d'apparition pour des coureurs de vitesse non Q-linéairement indépendantes

D'après la partie 8., lorsque les coureurs n'ont pas des vitesses Q-linéairement indépendantes, il existe un entier r 6= 0 ,
des entiers ( c i;j ) i 2 [[1 ;n ]] ;j 2 [[1 ;r ]] et des réels w 1 ; w 2 ; : : : ; w r Q-linéairement indépendants tels que

8 i 2 [[1 ; n ]] , v i =
 rX

j =1 c i;j w j .

On note w = ( w 1 ; w 2 ; : : : ; w r ) le vecteur des vitesses linéairement indépendantes. On dira dans la suite que ces vitesses
correspondent à des coureurs ˝ctifs.

On sait que la fonction vectorielle g : t 7! t: w = ( w 1 t; w 2 t; : : : ; w r t ) où w est le vecteur composé des vitesses des coureurs
˝ctifs est équirépartie modulo 1 dans Rn , d'après le paragraphe précédent.

Soit h : Rr ! Rn la fonction qui, à la position des coureurs ˝ctifs modulo 1, associe la position des coureurs réels modulo
1 : h ( f w 1 t g ; f w 2 t g ; :::; f w r t g ) = ( f v 1 t g ; f v 2 t g ; :::; f v n t g ) . h existe car f v i t g = f P c i;j f w j t gg et les ( c i;j ) sont entiers.

On a, pour tout ˙ appartenant à S n :

lim
T ! + 1 1
T
 Z T

0 ˜ V ˙ ( f v 1 t g ; f v 2 t g ; :::; f v n t g ) d t = lim
T ! + 1 1
T
 Z T

0 ˜ V ˙ ( h( f w 1 t g ; f w 2 t g ; :::; f w r t g )) d t

= lim
T ! + 1 1
T
 Z T

0 ˜ h  1 ( V ˙ ) ( f w 1 t g ; f w 2 t g ; :::; f w r t g ) d t

8

Suite de permutations lors d'une course de n coureurs de vitesses constantes

Théorème 15. La fréquence d'apparition d'une permutation ˙ vaut Z
 [0 ; 1] r ˜ h  1 ( V ˙ ) ( x) d x

Utilisation : On calcule l'image réciproque par h de chaque V ˙ . Pour cela, on détermine les hyperplans qui séparent
les h   1 ( V ˙ ) . On en déduit les h   1 ( V ˙ ) ; le volume de h   1 ( V ˙ ) est proportionnel à la fréquence d'apparition de ˙ .

Voir la ˝gure 7 : dans le cas n = 3 et r = 2 avec 3 coureurs de vitesses 1 ; ˇ; 2 + ˇ . Les hyperplans qui séparent les h   1 ( V ˙ )
sont les droites ( d i ) . Les volumes h   1 ( V ˙ ) sont les réunions des zones Pn .

13. Cas où les n vitesses forment un Q espace vectoriel de dimension n-1

Si les vitesses forment un Q espace vectoriel de dimension n-1, il existe des coe˚cients c i 2 Z tels que :
 nX

i =1 c i  v i = 0 ;

et si l'on impose pgcd c i = 1 , ces coe˚cients sont uniques (à un changement de signe de tous les c i près)

Théorème 16. Dans [0 ; 1] n , la fonction f ( v 1 t; v 2 t; : : : ; v n t ) g est dense dans les hyperplans
 nX

i =1 c i  x i = l où l est

un entier relatif quelconque.

Preuve 10. La fonction ne peut pas prendre d'autre valeur. Puisqu'au départ
 nX

i =1 c i  x i est un entier et le reste quand

l'un des coureur fait un tour.

Montrons que la fonction est dense dans ces hyperplans. Pour ça, on utilise les coureurs ˝ctifs dé˝nie à la partie 7 :
v 2
c 1 ; v 3
c 1 ; ::: v n
c 1 . On déduit alors du théorème de Kronecker, qu'il existe pour chaque position des coureurs de 2 à n , un

instant t où les coureurs sont proches de ces positions. Mais il nous reste un degré de liberté, puisque pour chaque
position du coureur i , il y a c 1 positions qui conviennent pour le coureur ˝ctif associée.

On utilise le théorème de Bezout : on sait qu'il existe ( a 1 ; :::; a n ) tel que 1 =
 nX

i =1 a i  c i .

Donc on sait qu'il existe, d'après le théorème de Kronecker, un instant T où les coureurs ˝ctifs de 2 à n ont une position

proche de a i % c i
c i , alors x 1 = 1 =c 1 .

Donc soit ( y 1 ; :::y n ) un point dans un des hyperplans, on sait d'après le théorème de Kronecker qu'il existe un instant T 0 ,
où les coureurs de 2 à n ont des positions proches de y 2 ; :::; y n , et ensuite en prenant les instants T 0 ; T 0 + T; T 0 + 2  T; :: ,
on sait qu'il en existe un où les coureurs ont des positions proches de ( y 1 ; :::y n ) .

Lemme 17. La distance entre ces hyperplans est 1
v
u
u
t nX

i =1 c 2
i

Pour qu'une permutation n'apparaisse pas, il faut que le V ˙ correspondant n'intersecte aucun hyperplan.

Théorème 18. Dans Rn , la distance minimale entre 2 hyperplans parallèles entre lesquels un V ˙ puisse s'insérer

est 1
p n .

Preuve 11. Les points d'un V ˙ sont, à une permutation des coordonnées près, (0 ; 0 ; 0 :::; 0); (1 ; 0 ; 0 :::; 0);

(1 ; 1 ; 0 ; :::; 0); ::: ; (1 ; 1 ; 1 ; :::; 1) .

Prenons 2 hyperplans parallèles, et notons A = ( a 1 ; a 2 ; :::; a n ) un vecteur normal à ces plans et unitaire. La plus petite
distance qu'il peut y avoir entre ces 2 plans sans qu'ils ne touchent V ˙ est max P 2 V ˙ ( < P ; A > )   min Q 2 V ˙ ( < Q ; A > ) , et

on peut se contenter de prendre P et Q parmi les sommets. De plus on sait qu' il existe i tel que j a i j ⩾ 1
p n , et alors soit

P i   1 le sommet juste avant que la i-ème coordonnée passe à 1, et P i celui juste après, on a j < A ; P i >   < A ; P i   1 >

j = j a i j ⩾ 1
p n Donc max P 2 V ˙ ( < P ; A > )   min P 2 V ˙ ( < P ; A > ) ⩾ 1
p n .

Le cas d'égalité est atteint avec A = (   1
p n ; 1
p n ; :::; (   1) i
p n ; ::: )

Maintenant, 2 possibilités, soit la relation entre les vitesses fait intervenir tout les coureurs et alors, comme tous les c i
sont entiers, on déduit des théorèmes précédents que toutes les permutations apparaissent si tous les c i ne valent pas 1

9

Suite de permutations lors d'une course de n coureurs de vitesses constantes

ou -1, ou si j
 mX

i =1 c i j ⩽ 1 j . Sinon on peut ignorer les coureurs qui n'apparait pas dans la relation, et utiliser le résultat

précédent.

Théorème 19. Le nombre de permutations qui apparaissent, selon m le nombre de coe˚cient non nul dans la
relation entre les c i , est :

 n ! si tous les c i ne valent pas 1 ou -1, ou si j
 mX

i =1 c i j ⩽ 1 j .

 n !
m !   m !   2   m 2
  !  2  sinon et si m est pair

 n !
m !   m !    m + 1
2
  !   m   1
2
  !  sinon et si m est impair

Preuve 12. On se place dans Rm , si tous les c i ne valent pas 1 ou -1, ou si j
 mX

i =1 c i j ⩽ 1 j , alors d'après le lemme 17 la

distance entre les hyperplans
 mX

i =1 c i x i = l est strictement inférieure à 1
p m . On en déduit d'après le théorème 18 que les

hyperplans intersectent tous les V ˙ et donc d'après le théorème 16, toute les permutations apparraissent.

Dans l'autre cas : la distance entre les hyperplans est 1
p m . Il faut encore se demander si les V ˙ sont dans le bon sens.

Seul celles pour lesquelles les c ˙ ( i ) alternent entre 1 et -1 conviennent. Pour celles ci, comme elles sont compris entre
mX

i =1 c i x i = 0 et
 mX

i =1 c i x i = 1 ou entre
 mX

i =1 c i x i = 0 et
 mX

i =1 c i x i =   1 , et donc les permutations concernées n'apparraisent

jamais. Les autres permutations sont intersectées par un hyperplan, et donc d'après le théorème 16, ces permutations
apparraissent.

Reste à savoir combien de permutations cela fait en tout. Pour alterner -1 et 1, si m est pair on a 2 possibilités : les 1

aux indices pairs et les -1 aux impairs où l'inverse ensuite on peut permuter les 1 où les -1, on a alors 2   m 2
  !  2

permutations qui n'apparaissent pas dans le problème à m coureurs. Si m est impair, ce sont les plus nombreux parmi

les 1 et -1 qui sont aux indices impairs et lesmoins nombreux aux indices pair. On a  m + 1
2
  !   m   1
2
  !

Ces résultats forment aussi un majorant pour la cas général, en prenant une relation entre les vitesses :

Théorème 20. Le nombre de permutations qui apparaissent, selon m le nombre de coe˚cient non nul dans la

relation entre les c i , est majoré, quand tous les c i ne valent 1 ou -1 et quand j
 mX

i =1 c i j ⩽ 1 j , par :

 n !
m !   m !   2   m 2
  !  2  si m est pair

 n !
m !   m !    m + 1
2
  !   m   1
2
  !  si m est impair

Preuve 13. La fonction f ( v 1 t; v 2 t; : : : ; v n t ) g prend toujours ses valeurs dans les hyperplans
 nX

i =1 c i  x i = l , donc les

permutations décrit ci dessus ne peuvent pas non plus apparaitre.

On retrouve pour n = 4 les résultats de la partie 10.

14. Conclusion

On a démontré la symétrie du problème et résolu entièrement le cas n = 3 .

Pour n quelconque, dans le cas de n vitesses Q-linéairement indépendantes, on a démontré que toutes les permutations
apparaissent et ont les mêmes fréquences d'apparition.

Dans le cas n = 4 , on a étudié et démontré plusieurs résultats : vitesses indépendantes, symétrie, application du cas
n = 3 , cas particuliers de vitesse : 1 grande et 3 quelconques... Mais, ce cas n = 4 reste un problème ouvert.

Pour le cas de n vitesses non Q-linéairement indépendantes, on propose une méthode géométrique pour calculer les
permutations qui apparaissent et leurs fréquences.
 10

Suite de permutations lors d'une course de n coureurs de vitesses constantes

15. Bibliographie

[1] Tournoi français des jeunes mathématiciennes et mathématiciens, problèmes du 1er tournoi français des jeunes ma-
thématiciens, 2011, https://www.tfjm.org/static/files/Problemes-TFJM2011-fr.pdf, problème 3 : un boulier,
p. 3, consulté le 8 mars 2017

[2] G. BECK, http ://demonstrations.wolfram.com/, The Four-Runner Problem, http://demonstrations.wolfram.
com/TheFourRunnerProblem/, 12 janvier 2008, consulté le 8 mars 2017

[3] G. BECK, http ://blog.wolfram.com, The Celebration Continues : 5,000+ Demonstrations, http://blog.wolfram.
com/2009/07/22/the-celebration-continues-5000-demonstrations/, 23 février 2016, consulté le 8 mars 2017

[4] L. KUIPERS, H. NIEDERREITER, Uniform distribution of sequences, Chapitre 1, John Wiley & Sons, 1974

[5] G.H.HARDY, E.M.WRIGHT, Introduction à la théorie des nombres, Chapitre 23, Vuibert, 2006
 11

Suite de permutations lors d'une course de n coureurs de vitesses constantes

16. Figures
 1

2
 3
 4
 5
 1 234 5

Figure 1 - Course de 5 coureurs et lecture de la permutation associée

632
 5 4 1
 6
3
2
 5
4 1
 6 3 2
 5
4 1

Avant À l'instant t Après
Figure 2 - Exemple de croisements multiples à un instant t

1 2 3
 = )
 1 23
 = )
 12 3
 OU
 1 23
 OU
 12 3

Figure 3 - Course de 3 coureurs : 3 premières permutations possibles

(1,2,3) (3,1,2)
 (1,3,2)

(2,3,1)
 (1,2,3)*

(2,1,3)

(1,2,3)*

(2,1,3)*
 (3,2,1)

(1,2,3)*
 (1,3,2)*

(1,3,2)*
 (2,3,1)*

(1,2,3)*

(3,1,2)*

( a; b; c ) * permutation déjà apparue
un seul dépassement
dépassements simultanés
 Figure 4 - Arbre des permutations possibles pour 3 coureurs
 12

Suite de permutations lors d'une course de n coureurs de vitesses constantes
 0 v 1 t
0

v 2 t
 1

1
 0 v 1 t
0

v 2 t
 1

1

Figure 5 - Interprétation géométrique pour n = 2 du théorème de Kronecker

0 t t 0   t t 0

6

3
2

5
4

1
 6

3
 2
 5 4
 1
 6
 3

2

54

1 6

32

5
4
 1

Figure 6 - Illustration de la symétrie du problème

d i : ( v 1 ; v 2 ) lieu de croisement des coureurs de
vitesse v 1 et v 2 (pas de croisement de plus de 2
coureurs ici)

Pn = h   1 ( V ˙ ) pour une des permutations ˙ .

zone permutation aire
P1 (1,2,3) 4/24
P2 (3,1,2) 2/24
P3 (1,3,2) 3/24
P4 (2,1,3) 2/24
P5 (3,2,1) 1/24
P6 (1,2,3) 1/24
P7 (3,1,2) 2/24
P8 (2,3,1) 3/24
P9 (2,1,3) 2/24
P10 (3,2,1) 4/24

permutation fréquence
(1,2,3) 5/24
(3,1,2) 4/24
(1,3,2) 3/24
(2,1,3) 4/24
(3,2,1) 5/24
(2,3,1) 3/24
 0 f t g
0

f ˇt g

1 d 1 : (0 ; ˇ )

1

d 2 : (0 ; 1); ( ˇ; 2 + ˇ )

d 3 : (0 ; 2 + ˇ )

d 4 : (0 ; 2 + ˇ ) d 5 : (1 ; ˇ )

d 6 : (1 ; 2 + ˇ )

d 7 : ( ˇ; 2 + ˇ )

P1
 P2
 P3

P4
 P5
 P6
 P7

P8
 P9 P10

On utilise 2 coureurs  ˝ctifs  de vitesses 1 et ˇ : (1 ; ˇ ) est une famille Q-linéairement indépendante qui engendre
(1 ; ˇ; 2 + ˇ ) . On utilise un coureur ˝ctif de vitesse 0 pour la ligne d'arrivée.
Figure 7 - Recherche des permutations pour 3 coureurs de vitesse 1 ; ˇ; 2 + ˇ

13
