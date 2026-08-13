> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/allombert-belabas-aurifeuillian-2008.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.numdam.org/item/10.5802/jtnb.641.pdf | converted from PDF -->

## What it claims

L’accès aux articles de la revue « Journal de Théorie des Nom-
bres de Bordeaux » (http://jtnb.cedram.org/), implique l’accord
avec les conditions générales d’utilisation (http://jtnb.cedram.
org/legal/). Toute reproduction en tout ou partie cet article sous
quelque forme que ce soit pour tout usage autre que l’utilisation à
ﬁn strictement personnelle du copiste est constitutive d’une infrac-
tion pénale. Toute copie ou impression de ce ﬁchier doit contenir la
présente mention de copyright.

cedram
 Article mis en ligne dans le cadre du
Centre de diffusion des revues académiques de mathématiques
http://www.cedram.org/

Journal de Théorie des Nombres
de Bordeaux 20 (2008), 543-553

Practical Aurifeuillian factorization

par Bill ALLOMBERT et Karim BELABAS

Dedicated to Henri Cohen on his 60th birthday

Résumé. Nous décrivons un algorithme simple pour déterminer
les facteurs d’Aurifeuille des entiers Φd(a), où Φd est le d-ème
polynôme cyclotomique, et a un entier. Sous une hypothèse de
Riemann convenable, l’algorithme termine en temps polynomial
déterministe ˜O(d2L), utilisant un…

Abs…

## Statements it makes

Proposition 1.1 (Granville-Pleasants [5]). Let a ∈ Q∗ and let ζd be a
primitive d-th root of unity. Let a∗ be the squarefree integer, which is the

Proposition 2.1. Let d > 2, and (d, a) satisfy the conditions of Propo-
sition 1.1. Write a = a∗f 2, f ∈ Q∗ and let G(a) = f ∏p|a∗ g(p) ∈ Q(ζd).
Then ∏

Theorem 3.4. Let L := log(|a| + 1), and M(n) an upper bound for the
bit complexity of multiplication of two n-bits integers. Assume that for all
d > 1, there exists a prime ℓ ≡ 1 (mod d) satisfying ℓ ⩽ DdC for some con-
stants C < 8 and D. Given such an ℓ, Algorithm 3.1 runs in deterministic
time O(dM(dL) + dC/4+ε) = ˜O(d2L), using O(dL) space.

Corollary 3.5. Assuming the Generalized Riemann Hypothesis, Algo-
rithm 3.1 runs in time ˜O(d2L).

*[digest of a 21886 character source; every section, statement, and proof in full at `research/sources/allombert-belabas-aurifeuillian-2008.full.md`]*
