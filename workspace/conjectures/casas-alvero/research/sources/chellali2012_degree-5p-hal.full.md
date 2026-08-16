<!-- source: https://hal.science/hal-00748843/document | converted from PDF -->

HAL Id: hal-00748843

https://hal.science/hal-00748843v1

Preprint submitted on 8 Nov 2012

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

HAL Authorization

La conjecture de Casas Alvero pour les degrés 5𝑝𝑒

Mustapha Chellali

To cite this version:

Mustapha Chellali. La conjecture de Casas Alvero pour les degrés 5𝑝𝑒. 2012. ⟨hal-00748843⟩

La conjecture de Casas Alvero pour les degr´e 5pe

Mustapha CHELLALI & Alain SALINIER

R´esum´e : Selon la conjecture de Casas Alvero, si un polynˆome `a une variable de degr´e n sur un corps commutatif de

caract´eristique 0 est non premier avec chacune de ses n − 1 premi`eres d´eriv´es, alors il est de forme c(X − r)n. Soient

p un nombre premier et e un entier, la conjecture a ´et´e d´emontr´ee pour les polynˆomes de degr´e pe, 2pe, 3pe

(p ̸= 2) et 4pe (p ̸= 3, 5, 7). Dans ce travail on montre que la conjecture est vrai pour les polynˆomes de degr´e

5pe (p ̸= 2, 3, 7, 11, 131, 193, 599, 3541, 8009). On corrige aussi une erreur dans [4] pour les degr´e 4pe

1 Introduction

Soit k un corps commutatif, P ∈ k[X] un polynˆome de degr´e n, la conjecture de Casas-
Alvero veut que si P est non premier avec chacune de ses n − 1 premi`eres d´eriv´ees, alors
c’est un monˆome, c’est-´a-dire de la forme c(X − r)n. Cette conjecture est ´evidement fausse si
la caract´eristique de k est ̸= 0 comme le montre l’exemple P = X p+1 − X p en caract´eristique
p. Suivant [6], il importe de modiﬁer l’´enonc´e de la conjecture en caract´eristique ̸= 0,
en rempla¸cant les d´eriv´es ordinaire P (i) par les d´eriv´es de Hasse d´eﬁnies par P (X + h) =∑

i Pi(h)X i (en caract´eristique 0 on a simplement Pi = P (i)/i!). Un lien int´eressant a ´et´e
trouv´e entre la conjecture en caract´eristique 0 et la conjecture en caract´eristique p ̸= 0 (cf
[6] voir aussi [4] pour une preuve ´el´ementaire), en notons Fp la clˆoture alg´ebrique de Fp, il
s’´enonce comme suit :

Proposition 1.1 Soit n un entier ≥ 1

• Si pour un nombre premier donn´e p la conjecture de Casas-Alvero est vrai sur Fp pour
tout polynˆome de degr´e n, alors elle est vrai en caract´eristique 0 pour tout polynˆome
de degr´e de la forme npe (e ∈ N)

• Inversement si la conjecture est vrai en caract´eristique 0 pour tout polynˆome de degr´e
n, alors elle est vrai sur Fp pour tout polynˆome de degr´e n, sauf peut ˆetre pour un
nombre ﬁni de p.

Comme cons´equence on obtient :

• Pour n = 1, il n’y a aucun mauvais nombre premier, par cons´equent la conjecture est
vrai pour tout polynˆome de degr´e pe (p premier)

1

• Pour n = 2, si un polynˆome de degr´e 2 v´eriﬁe les hypoth`eses de Casas-Alvero, comme
il a une racine double, c’est un monˆome, par suite la conjecture est vrai pour tout
polynˆome de degr´e 2pe (p premier)

• Pour n = 3, cherchons les mauvais nombres premiers, soit p un nombre premier , soit
P un polynˆome de degr´e 3 sur Fp v´eriﬁant les hypoth`eses de Casas-Alvero , apr`es
transformation aﬃne on se ram`ene `a P de la forme X 3 − aX 2, ´ecartons d’abord les cas
p = 2, 3 puisque la conjecture de Casas-Alvero est v´eriﬁ´ee pour 3e et que on sait que
X 3 − X 2 est un contre exemple en caract´eristique 2

{ P ′ = 3X 2 − 2aX
P2 = 3X − a

Si 0 est racine de P ′′ −→ a = 0 −→ P = X 3, sinon la racine de P ′′ en commun avec
P est a −→ 2a = 0 −→ a = 0. Ainsi 2 est le seul mauvais nombre premier.

Conclusion : Si p est nombre premier ̸= 2 la conjecture de Casas-Alvero est vrai pour
les polynˆomes de degr´e 3pe

• Pour n = 4, cherchons les mauvais nombres premiers, soit p un nombre premier , soit
P un polynˆome de degr´e 4 sur Fp v´eriﬁant les hypoth`eses de Casas-Alvero , apr`es
transformation aﬃne on se ram`ene `a P de la forme X 4 − aX 3 + bX 2, ´ecartons d’abord
les cas p = 2, 3 puisque la conjecture de Casas-Alvero est v´eriﬁ´ee pour 2e et que on
sait que X 4 − X 3 est un contre exemple en caract´eristique 3.


 P ′ = 4X 3 − 3aX 2 + 2bX
P2 = 6X 2 − 3aX + b
P3 = 4X − a

Supposons d’abord que 0 n’est pas racine de P ′′ et P ′′′ soit ab ̸= 0, ´ecrivons P =
X 2(X − x1)(X − x2), soient α, β les racines de P ′′ et P ′′′ en commun avec P , on peut
supposer que β = x1, deux cas sont alors possibles (α, β) = (x1, x1) ou (α, β) = (x2, x1)

– 1 er cas : (α, β) = (x1, x1)
{ 4x1 = a = x1 + x2 −→ x2 = 3x1
6x
2 − 12x
2 + b = 0 −→ b = 6x
2 soit 6x
2 = x1x2 = 3x
2 −→ x1 = x2 = 0

– 2 `eme cas : (α, β) = (x2, x1)
{ 4x1 = a = x1 + x2 −→ x2 = 3x1
6x
2 − 12x1x2 + b = 0 −→ b = −2x
2 soit − 2x
2 = x1x2 = 3x
2 −→ 21x
2 = 0 −→ p = 7

Inversement si p = 7, prenons x1 = 1 et x2 = 3x1 = 3 et P = X 2(X − 1)(X − 3)
on a P ′′′(1) = 0 et P ′′(3) = 0, donc P v´eriﬁe les hypoth`eses de Casas-Alvero dans

F7 et n’est pas monˆome, ainsi 7 est un mauvais nombre premier.

Supposons maintenant que 0 est racine de P ′′ ou P ′′′ soit a ou b = 0 (mais pas les deux
car dans ce cas P serait monˆome et p un bon nombre premier )

2

• a = 0 −→ x1 + x2 = 0, on peut supposer que la racine de P ′′ est alors x1 ̸= 0 −→
6x
2 + b = 0 −→ b = −6x
2 = x1x2 = −x
2 −→ 5x
2 = 0 −→ p = 5. Inversement si
p = 5, posons x1 = 1 et x2 = −1 et P = X 2(X − 1)(X + 1) on a P ′(0) = P ′′′(0) = 0
et P ′′(1) = 6 − 1 = 0, donc P v´eriﬁe les hypoth`eses de Casas-Alvero dans
 F5 et n’est
pas monˆome, ainsi 5 est un mauvais nombre premier. Ce cas est pass´e inaper¸cu dans
[4] suite a une erreur de consid´eration de d´eterminant (cf page 33)

• b = 0 −→ x1x2 = 0, on peut supposer que la racine de P ′′′ est alors x1 ̸= 0 −→
4x1 − a = 0 −→ a = 4x1 = x1 + x2 −→ 3x
2 = 0 −→ x1 = x2 = 0.

Conclusion : Si p est nombre premier ̸= 3, 5, 7 la conjecture de Casas-Alvero est vrai
pour les polynˆomes de degr´e 4pe

2 Cas des degr´es 5pe

Notre r´esultat principal est :

Proposition 2.2 La conjecture de Casas-Alvero est vrai pour les polynˆomes de degr´e 5pe,
e entier et p premier ̸= 2, 3, 7, 11, 131, 193, 599, 3541, 8009

Preuve : Nous allons poursuivre les m´ethodes ci-dessus pour d´eterminer les mauvais
nombres premiers pour les polynˆomes de degr´e 5. Soit P un polynˆome de degr´e 5 sur Fp
v´eriﬁant les hypoth`eses de Casas-Alvero , apr`es transformation aﬃne on se ram`ene `a P de
la forme X 5 − aX 4 + bX 3 − cX 2, ´ecartons d’abord les cas p = 2, 3, 5 puisque la conjecture de
Casas-Alvero est v´eriﬁ´ee pour 5e et que X 5 − X 4 est un contre exemple en caract´eristique 2
et X 5 + X 4 est un contre exemple en caract´eristique 3.

 P ′ = 5X 4 − 4aX 3 + 3bX 2 − 2cX
P2 = 10X 3 − 6aX 2 + 3bX − c
P3 = 10X 2 − 4aX + b
P4 = 5X − a

Soient α, β, γ les racines de P ′′, P ′′′, P (4) en commun avec P , nous distinguons deux cas :

• 1 er cas : 0 /∈ {α, β, γ}

Ecrivons P = X 2(X − x1)(X − x2)(X − x3), on peut supposer γ = x1

– Cas (α, β, γ) = (x1, x1, x1)


 P4(x1) = 5x1 − a = 0 −→ 5x1 = a = x1 + x2 + x3 −→ 4x1 = x2 + x3
P3(x1) = 0 −→ 10x
2 − 20x
2 + b = 0
−→ b = 10x
2 = x1x2 + x1x3 + x2x3 = 4x
2 + x2(4x1 − x2) −→
 6x
2 − 4x1x2 + x
2 = 0

P2(x1) = 0 −→ 10x
3 − 30x
3 + 30x
3 − x1x2x3 = 0 −→ 10x
2 = x2x3 = x2(4x1 − x2)
−→
 10x
2 − 4x1x2 + x
2 = 0

Comme x1 est suppos´e ̸= 0, posons r = x2/x1, on a le syst`eme :

3

{ r2 − 4r + 6 = 0
r2 − 4r + 10 = 0

Le resultant de ces deux ´equations est 16 ̸= 0 puisque p ̸= 2, par suite ce cas est
impossible.

– Cas (α, β, γ) = (x3, x2, x1)


 P4(x1) = 5x1 − a = 0 −→ 5x1 = a = x1 + x2 + x3 −→ 4x1 = x2 + x3
P3(x2) = 0 −→ 10x
2 − 20x1x2 + b = 0
−→ b = −10x
2 + 20x1x2 = x1x2 + x1x3 + x2x3 = 4x
2 + x2(4x1 − x2)
−→
 4x
2 − 16x1x2 + 9x
2 = 0

P2(x3) = 0 −→ 10x
3 − 30x1x
2 + 3(−10x
2 + 20x1x2)x3 − x1x2x3 = 0
−→ 10x
2 − 30x1x3 + 3(−10x
2 + 20x1x2) − x1x2 = 0
−→ 10(4x1 − x2)2 − 30x1(4x1 − x2) + 3(−10x
2 + 20x1x2) − x1x2 = 0
−→
 40x
2 + 9x1x2 − 20x
2 = 0

Comme x1 est suppos´e ̸= 0, posons r = x2/x1, on a le syst`eme :
{ 9r2 − 16r + 4 = 0
−20r2 + 9r + 40 = 0

Le resultant de ces deux ´equations est 32036 = 22.8009 puisque p ̸= 2 cela n’est
possible que si p = 8009. Inversement si p = 8009 on va remonter ces ´equations
pour construir un contre exemple modulo p. eliminon r entre ces deux equations
on obtient r = 440/239 = 2113 mod 8009. En ﬁxant x1 = 1 alors x2 = r et
x3 = 4x1 − x2 = 4 − r, cela doone le contre exemple :

P = x
2(x − 1)(x − r)(x − 4 + r) = x
5 − 5x
4 − 3309x
3 + 3313x
2 mod 8009

On v´eriﬁe bien que modulo 8009 on a

P4(1) = 0
P3(r) = 0
P2(4 − r) = 0

– Cas (α, β, γ) = (x2, x1, x1)


 P4(x1) = 5x1 − a = 0 −→ 5x1 = a = x1 + x2 + x3 −→ 4x1 = x2 + x3
P3(x1) = 0 −→ 10x
2 − 20x
2 + b = 0
−→ b = 10x
2 = x1x2 + x1x3 + x2x3 = 4x
2 + x2(4x1 − x2) −→
 6x
2 − 4x1x2 + x
2 = 0

P2(x2) = 0 −→ 10x
3 − 30x1x
2 + 30x
2x2 − x1x2x3 = 0
−→ 10x
2 − 30x1x2 + 30x
2 − x1x3 = 0
−→ 10x
2 − 30x1x2 + 30x
2 − x1(4x1 − x2) = 0
−→
 26x
2 − 29x1x2 + 10x
2 = 0

4

Comme x1 est suppos´e ̸= 0, posons r = x2/x1, on a le syst`eme :
{ r2 − 4r + 6 = 0
10r2 − 29r + 26 = 0

Le resultant de ces deux ´equations est 386 = 2.193 puisque p ̸= 2 cela n’est
possible que si p = 193. Inversement si p = 193 on va remonter ces ´equations
pour construir un contre exemple modulo p. eliminon r entre ces deux equations
on obtient r = 34/11 = 161 mod 193. En ﬁxant x1 = 1 alors x2 = r et x3 =
4x1 − x2 = 4 − r, cela doone le contre exemple :

P = x
2(x − 1)(x − r)(x − 4 + r) = x
5 − 5x
4 + 10x
3 − 6x
2 mod 193

On v´eriﬁe bien que modulo 193 on a
 P4(1) = 0
P3(r) = 0
P2(4 − r) = 0

– Cas (α, β, γ) = (x1, x2, x1)


 P4(x1) = 5x1 − a = 0 −→ 5x1 = a = x1 + x2 + x3 −→ 4x1 = x2 + x3
P3(x2) = 0 −→ 10x
2 − 20x1x2 + b = 0
−→ b = −10x
2 + 20x1x2 = x1x2 + x1x3 + x2x3 = 4x
2 + x2(4x1 − x2)
−→
 4x
2 − 16x1x2 + 9x
2 = 0

P2(x1) = 0 −→ 10x
3 − 30x1x
2 + 3(−10x
2 + 20x1x2)x1 − x1x2x3 = 0
−→ 10x
2 − 30x1x1 + 3(−10x
2 + 20x1x2) − x2x3 = 0
−→ 10x
2 − 30x1x1 + 3(−10x
2 + 20x1x2) − x2(4x1 − x2) = 0
−→
 −20x
2 + 56x1x2 − 29x
2 = 0

Comme x1 est suppos´e ̸= 0, posons r = x2/x1, on a le syst`eme :
{ 9r2 − 16r + 4 = 0
29r2 − 56r + 20 = 0

Le resultant de ces deux ´equations est 256 = 28 puisque p ̸= 2 ce cas est impossible.

– Cas (α, β, γ) = (x2, x2, x1)


 P4(x1) = 5x1 − a = 0 −→ 5x1 = a = x1 + x2 + x3 −→ 4x1 = x2 + x3
P3(x2) = 0 −→ 10x
2 − 20x1x2 + b = 0
−→ b = −10x
2 + 20x1x2 = x1x2 + x1x3 + x2x3 = 4x
2 + x2(4x1 − x2)
−→
 4x
2 − 16x1x2 + 9x
2 = 0

P2(x2) = 0 −→ 10x
3 − 30x1x
2 + 3(−10x
2 + 20x1x2)x2 − x1x2x3 = 0
−→ 10x
2 − 30x1x2 + 3(−10x
2 + 20x1x2) − x1x3 = 0
−→ 10x
2 − 30x1x2 + 3(−10x
2 + 20x1x2) − x1(4x1 − x2) = 0
−→
 −4x
2 + 31x1x2 − 20x
2 = 0

5

Comme x1 est suppos´e ̸= 0, posons r = x2/x1, on a le syst`eme :
{ 9r2 − 16r + 4 = 0
20r2 − 31r + 4 = 0

Le resultant de ces deux ´equations est −524 = −22.131 puisque p ̸= 2 cela n’est
possible que si p = 131. Inversement si p = 131 on va remonter ces ´equations
pour construir un contre exemple modulo p. eliminon r entre ces deux equations
on obtient r = 44/41 = 49 mod 131. En ﬁxant x1 = 1 alors x2 = r et x3 =
4x1 − x2 = 4 − r, cela doone le contre exemple :

P = x
2(x − 1)(x − r)(x − 4 + r) = x
5 − 5x
4 + 26x
3 − 22x
2 mod 131

On v´eriﬁe bien que modulo 131 on a
 P4(1) = 0
P3(r) = 0
P2(4 − r) = 0

• 2 `eme cas : 0 ∈ {α, β, γ}

Autrement dit a ou b ou c = 0, on a les resultants

Resx(P, P2) = 100 a
3 c4 − 24 a
2 b
2 c3 − 459 a b c4 + 98 b
3 c3 + 729 c5

Resx(P, P3) = 96 a
3 b
2 c − 18 a
2 b
4 − 480 a b
3 c + 81 b 5 + 1000 b
2 c2

Resx(P, P (4)) = 4 a
5 − 25 b a
3 + 125 c a
2

– 1er cas : a = 0
Dans ce cas les resultants ci-dessus deviennent :

Resx(P, P2) = c3(98 b
3 + 729 c2)
Resx(P, P3) = b
2(81 b
3 + 1000 c2)

Si P v´eriﬁe les hypoth`eses de Casas-Alvero on aura alors

c3(98 b
3 + 729 c2) = 0
b
2(81 b
3 + 1000 c2) = 0

Si c = 0 −→ 81b
5 = 0 −→ b = 0 car p ̸= 3. Si b = 0 −→ 729c5 = 0, soit
93c5 = 0 −→ c = 0. si bc ̸= 0 le syst`eme ci-dessus a un d´eterminant nul :

98.1000 − 81.729 = 0

Soit 11.3541 = 0 −→ p = 11 ou p = 3541

6

∗ Cas p = 11 prenons c = 1 if faut que b
3 = −729/98 = 3 mod 11 −→ b = −2,
d’o`u :
 P = x
5 − 10x
3 − 3x
2

On v´eriﬁe que
 P = x
2(x + 1)(x + 3)(x − 4) mod 11

On v´eriﬁe que
 P2(−3) = 0 mod 11
P3(−3) = 0 mod 11
P4(0) = 0 mod 11

∗ Cas p = 3541 pour r´ealiser 81 b
3 + 1000 c2 = 0 il suﬃt de prendre b = −10 et
c = 9 :
 P = x
5 − 10x
3 − 9x
2

On v´eriﬁe que

P = x
2(x + 1)(x − 1567)(x + 1566) mod 3541

On v´eriﬁe que
 P2(1567) = 0 mod 3541
P3(−1) = 0 mod 3541
P4(0) = 0 mod 3541

– 2`eme cas : b = 0
Dans ce cas les resultants ci-dessus deviennent :

Resx(P, P2) = c4 · (100 a
3 + 729 c)
Resx(P, P4) = a
2 · (4 a
3 + 125 c)

Si P v´eriﬁe les hypoth`eses de Casas-Alvero on aura alors

c4 · (100 a
3 + 729 c) = 0
a
2 · (4 a
3 + 125 c) = 0

Si c = 0 −→ 4a
5 = 0 −→ a = 0 car p ̸= 2. Si a = 0 −→ 729c5 = 0, soit
93c5 = 0 −→ c = 0. si ac ̸= 0 le syst`eme ci-dessus a un d´eterminant nul :

100.125 − 4.729 = 0

Soit 9584 = 24.599 = 0 −→ p = 599. Pour r´ealiser a
2 · (4 a
3 + 125 c) = 0 prenons
c = 4 et a = −5 d’o`u :
 7

P = x
5 + 5x
4 − 4x
2

On v´eriﬁe que
 P = x
2(x + 1)(x + 269)(x − 265) mod 599

et
 P2(−269) = 0 mod 599
P3(0) = 0 mod 599
P4(−1) = 0 mod 599

– 3`eme cas : c = 0
Dans ce cas les resultants ci-dessus deviennent :

Resx(P, P3) = (−9) · b
4 · (2 a
2 − 9 b)
Resx(P, P4) = a
3 · (4 a
2 − 25 b)

Si P v´eriﬁe les hypoth`eses de Casas-Alvero on aura alors

(−9) · b
4 · (2 a
2 − 9 b) = 0
a
3 · (4 a
2 − 25 b) = 0

Si b = 0 −→ 4a
5 = 0 −→ a = 0 car p ̸= 2. Si a = 0 −→ 92b
5 = 0 −→ b = 0. si
ab ̸= 0 le syst`eme ci-dessus a un d´eterminant nul :

2.(−25) + 4.9 = 0

Soit −14 = −2.7 = 0 −→ p = 7. Pour r´ealiser (−9) · b
4 · (2 a
2 − 9 b) = 0 prenons
b = 2 et a = 3 d’o`u :
 P = x
5 − 3x
4 + 2x
3

On v´eriﬁe que
 P = x
3(x − 1)(x − 2) mod 7

et
 P2(0) = 0 mod 7
P3(1) = 0 mod 7
P4(2) = 0 mod 7

8

3 Conclusion

• Les resulats ci dessus ne permettent pas de d´ecider pour les degr´es : 12,20,24,28,30,35,36,...

• Les m´ethode ci dessus ne semblent pas s’´etendre au cas du degr´es 6, le contre exemple
de [6]
 P = X 6 + 3144481702696843X 4 + X 3 + 2707944513497181X 2

p = 7390044713023799

laisse supposer que les mauvais nombres premiers de ce cas sont tr´es grands et leur
nombre est grand

References

[1] Casas Alvero., Higher order polar germs, Journal of Algebra 240,. (2001) 240,
1, 326-337,

[2] G. Diaz-Toca and L. Gonzalez-Vega On a conjecture about univariate poly-
nomials and their roots. In A. Dolzmann, A. Seidl, and T. Sturm, editors,
Algorithmic Algebra and Logic 2005, pages 83 -90, Norderstedt, Germany,
2005. Books on Demand.

[3] Jan Draisma,On the Casas-Alvero conjecture http://www.win.tue.nl/
jdraisma/talks/casasalverotalk.pdf

[4] Draisma, Jan; and Jong, Johan P.On the Casas-Alvero conjecture. (English)
Eur. Math. Soc. Newsl. 80, 29-33 (2011). MSC2000: *37-99 30-99 .

[5] Duong Hoang Dung, On the Cassa-Alvero Conjecture
http://www.math.leidenuniv.nl/ edix/tag 2009/duong 2.pdf

[6] Hans-Christian graf von bothmer, Oliver Labs, Josef Schicho, and Christiaan
Van de woestijne ,The Casas-Alvero conjecture for infnitely many degrees,
http://arxiv.org/abs/math/0605090v2

Polynomials over commutative rings
MSC-numbers 2000: 13M10 13P05 13P10 P

*************
Adresses des auteurs

*************
Prof M.Chellali
D´epartement de math´ematiques
Facult´e des sciences, Universit´e Mohammed 1
Oujda, Maroc.
 9

*************
Prof Alain Salinier
D´epartement de Math´ematiques
Facult´e des Sciences et Techniques de Limoges
123, avenue Albert Thomas
87060 LIMOGES Cedex (FRANCE)
*************

email : mustapha.chellali@gmail.com
alain.salinier@unilim.fr
 10
