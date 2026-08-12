> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/torpedo_half_line_systematics.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

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

*[excerpt ends; 34469 characters not shown — see `research/sources/torpedo_half_line_systematics.full.md`]*
