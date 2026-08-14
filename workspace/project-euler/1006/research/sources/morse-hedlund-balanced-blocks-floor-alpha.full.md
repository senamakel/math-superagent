<!-- source: https://hal.science/hal-03869990v2/document | converted from PDF -->

HAL Id: hal-03869990

https://hal.science/hal-03869990v2

Submitted on 23 Nov 2023

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

Factor-balanced S-adic languages

Léo Poirier, Wolfgang Steiner

To cite this version:

Léo Poirier, Wolfgang Steiner. Factor-balanced S-adic languages. Theoretical Computer Science, 2024, 998,
pp.114535. ⟨10.1016/j.tcs.2024.114535⟩. ⟨hal-03869990v2⟩

FACTOR-BALANCED S-ADIC LANGUAGES

L´EO POIRIER AND WOLFGANG STEINER

Abstract. A set of words, also called a language, is letter-balanced if the number of occur-
rences of each letter only depends on the length of the word, up to a constant. Similarly, a
language is factor-balanced if the diﬀerence of the number of occurrences of any given factor
in words of the same length is bounded. The most prominent example of a letter-balanced
but not factor-balanced language is given by the Thue–Morse sequence. We establish con-
nections between the two notions, in particular for languages given by substitutions and,
more generally, by sequences of substitutions. We show that the two notions essentially co-
incide when the sequence of substitutions is proper. For the class of Thue–Morse–Sturmian
languages, we give a full characterisation of factor-balancedness.

1. Introduction

The study of balancedness of languages goes back at least to Morse and Hedlund [MH40]
who proved that each block of length n in a Sturmian sequence of slope α has ⌊nα⌋ or ⌈nα⌉
occurrences of the letter that has frequency α (and thus ⌊n(1−α)⌋ or ⌈n(1−α)⌉ occurrences
of the other letter). In other words, the diﬀerence between the number of occurrences of
a letter in blocks of the same length is at most 1; we call this property letter-1-balanced,
previously it has often been simply called balanced. More generally, a language is letter-
balanced if the number of occurrences of a letter only depends on the length of a word in
the language, up to an additive constant. We do not only consider the occurrence of letters
but also of longer blocks, and we say that a language is factor-balanced if the number of
occurrences of each block in a word of the language only depends on the length of the word,
up to a constant that can depend on the block. Usually, languages coming from a symbolic
dynamical system (or subshift) are considered; we use the slightly weaker property of being
factorial. For inﬁnite sequences, balancedness is equivalent to bounded symbolic discrepancy,
as studied in [Ada04]. These concepts have applications in operations research, for optimal
routing and scheduling and are related to Fraenkel’s conjecture; see [BCB19] for references.
Some relations between letter-balancedness and factor-balancedness have been studied in
[Ada03, Que10], and more recently in [BCB19]. Here, we improve on these results and show
that factor-balancedness is preserved by the application of a substitution. We consider lan-
guages (or subshifts) given by a sequence of substitutions, also called S-adic languages. When
the substitutions are left or right proper, i.e., the image of each letter starts or ends with the
same letter, we show that letter-balancedness (on all levels) implies factor-balancedness; this
was previously known only under the assumption that the substitutions have unimodular in-
cidence matrices [BCBD+21]. A particular case is that of a substitutive shift with a proper
substitution. Here, we cannot remove the assumption of properness, as for example the

Date: November 23, 2023.
This work was supported by the Agence Nationale de la Recherche through the projects CODYS (ANR-
18-CE40-0007) and IZES (ANR-22-CE40-0011). 1

Thue–Morse shift is not factor-balanced [Sad16, BCB19]; we give a short proof in Section 5.
For non-proper substitutions, we have to require balancedness for all factors of length 2, not
only for letters, in order to get factor-balancedness.
In Section 2, we deﬁne most of the notions and give a characterisation of letter-balancedness
in terms of the distance to a frequency vector. The eﬀect of substitutions on balancedness
is studied in Section 3. Section 4 contains our main results, on sequences of substitutions.
Finally, we consider the balancedness of a particular class of S-adic languages in Section 5.

2. Balancedness

For a ﬁnite alphabet A, let A
∗ be the set of ﬁnite words over A. A language is a subset
L ⊆ A
∗. A word v ∈ A
∗ is a factor of w ∈ A
∗ if there exist p, s ∈ A
∗ such that w = pvs;
here, p is a preﬁx and s is a suﬃx of w. We denote the set of factors of w by F (w), and the
set of factors of elements of L by F (L). A langage L is factorial if F (L) = L. The length of
a word w ∈ A
∗ is denoted by |w|, i.e., |w| = n if w ∈ A
n. We denote the preﬁx (resp. suﬃx)
of length n of a word w by pref n(w) (resp. suﬀ n(w)). The number of occurrences of a word v
in w, i.e., the number of diﬀerent decompositions w = pvs, is denoted by |w|v. A language L
is called C-balanced w.r.t. v if

|w|v − |w′|v ≤ C for all w, w′ ∈ L with |w| = |w′|.

(By symmetry, this is equivalent to ∣
∣|w|v − |w′|v∣
∣ ≤ C for all w, w′ ∈ L with |w| = |w′|.) It
is called C-balanced for length n if it is C-balanced for all v ∈ A
n. We often omit the C and
say that a language is balanced for length n if it is C-balanced for length n for some C ≥ 0.
Instead of “(C-)balanced for length 1”, we also say letter-(C-)balanced ; other papers use
the term “balanced” instead of letter-1-balanced or instead of letter-balanced, and a letter-
balanced language is sometimes called “ﬁnitely balanced”. A language is factor-(C-)balanced
if it is (C-)balanced for all lengths n ≥ 1; in [Sad16], a factor-balanced language is called
totally ﬁnitely balanced. Note that factor-C-balancedness is a strong property that is satisﬁed
for certain Sturmian languages [FV02], but we do not study this property here. We are only
interested in factor-balancedness, which means that for each n there exists Cn such that L
is Cn-balanced for length n; equivalently, for each v ∈ F (L) there exists Cv such that L is
Cv-balanced w.r.t. v. (Note that |w|v = 0 for all w ∈ L, v /∈ F (L).) We ﬁrst show that
balancedness for length n is the same as balancedness for lengths up to n.

Lemma 2.1. If a language is balanced for length n, then it is balanced for all lengths k ≤ n.

Proof. Let L ⊂ A
∗ be C-balanced for length n, k < n. For all v ∈ A
k, w ∈ A
∗, we have
|w|v = ∑

s∈An−k |w|vs + |suﬀ n−1(w)|v, thus |w|v − |w′|v ≤ (#A)n−kC + n − 1 for w′ ∈ A
|w|. □

We will also use the following characterisation of letter-balancedness in terms of distance
from the line deﬁned by a frequency vector, cf. [BT02, Ada03].

Proposition 2.2. Let L ⊂ A
∗ be an inﬁnite letter-C-balanced factorial language. Then there
exists a (frequency) vector (fa)a∈A such that ∣
∣|w|a − fa|w|∣
∣ ≤ C for all a ∈ A, w ∈ L.

Proof. Since [0, 1]#A is compact, there exists a vector (fa)a∈A and a sequence of words vn ∈ L
such that limn→∞ |vn| = ∞ and limn→∞ |vn|a/|vn| = fa for all a ∈ A. For arbitrary but ﬁxed
2

w ∈ L, set kn = ⌊|vn|/|w|⌋, and decompose vn = vn,1 · · · vn,knvn,kn+1 with |vn,i| = |w| for all
1 ≤ i ≤ kn. Since vn,i ∈ L, L is letter-C-balanced, and |vn,kn+1| < |w|, we obtain that
∣
∣
∣
∣|w|a − |vn|a
|vn| |w|∣
∣
∣
∣ = |w|
|vn|
 ∣
∣
∣
∣|vn|
|w| |w|a − |vn|a
∣
∣
∣
∣ < |w|
|vn|
(|w| +
 kn∑

i=1
 ∣
∣|w|a − |vn,i|a∣
∣
) ≤ |w|2

|vn| + kn|w|
|vn| C

for all a ∈ A. Letting n → ∞, this gives that ∣
∣|w|a − fa|w|∣
∣ ≤ C. □

Lemma 2.3. Let L ⊂ A
∗ and (fa)a∈A such that ∣
∣|w|a − fa|w|∣
∣ ≤ C for all a ∈ A, w ∈ L.
Then L is letter-(2C)-balanced.

Proof. We have |w|a − |w′|a = |w|a − fa|w| + fa|w′| − |w′|a ≤ 2C for all w, w′ ∈ L, a ∈ A,
such that |w| = |w′|. □

3. Substitutions

In this section, we study how the application of a substitution inﬂuences balancedness.
Here, a substitution σ is a morphism from A
∗ to B∗, with the operation of concatenation,
i.e., σ(vw) = σ(v)σ(w) for all v, w ∈ A
∗. We use the notation

∥σ∥ := max
a∈A |σ(a)|, ⟨σ⟩ := min
a∈A |σ(a)|,

and call a substitution non-erasing if all images of letters are non-empty, i.e., ⟨σ⟩ ≥ 1. It is
left (resp. right) proper when all letter images start (resp. end) with the same letter.
To show that substitutions preserve balancedness, we use the following lemma.

Lemma 3.1. Let L ⊂ A
∗ be a letter-C-balanced factorial language and σ : A
∗ → B∗ a
substitution. Then, for all w, w′ ∈ F (σ(L)) with |w| = |w′|, there exist x, x
′, z, z′ ∈ B∗,
y, y′ ∈ L, such that

w = x σ(y) z, w′ = x
′ σ(y′) z′, |y| = |y′|, max{|x z|, |x
′z′|} ≤ (2 + C #A) ∥σ∥ − 2.

Proof. Since w, w′ ∈ F (σ(L)) and L is factorial, we can write w = x σ(v) u and w = x
′σ(v′) u′

with v, v′ ∈ L, u, u′, x, x
′ ∈ A
∗ such that |u|, |u′|, |x|, |x
′| < ∥σ∥. Assume w.l.o.g. that
|v| ≤ |v′|, let y = v, v′ = y′s′ with |y′| = |y|, z = u, z′ = σ(s′) u′. Since L is factorial, we
have y, y′ ∈ L. Since L is letter-C-balanced, we have

|σ(y)| − |σ(y′)| = ∑

a∈A
 (
|y|a − |y′|a) |σ(a)| ≤ (#A) C ∥σ∥,

thus
 |x
′z′| = |w′| − |σ(y′)| ≤ |w| − |σ(y)| + (#A) C ∥σ∥ ≤ 2 (∥σ∥ − 1) + (#A) C ∥σ∥.

Therefore, w = x σ(y) z and w′ = x
′ σ(y′) z′ satisfy all the required properties. □

Proposition 3.2. Let L ⊂ A
∗ be a factorial language and σ : A
∗ → B∗ a substitution. If L
is letter-balanced, then F (σ(L)) is letter-balanced.

Proof. Suppose that L is C-letter-balanced, and let w = x σ(y) z, w′ = x
′ σ(y′) z′ be as in
Lemma 3.1. Then, for all b ∈ B,

|w|b − |w′|b = |xz|b − |x
′z′|b + |σ(y)|b − |σ(y′)|b

≤ (2 + C #A) ∥σ∥ − 2 + ∑

a∈A
 (|y|a − |y′|a) |σ(a)|b ≤ 2 (1 + C #A) ∥σ∥ − 2. □

3

To study balancedness for length n, we use the n-th higher block code of a word a1a2 · · · aN ∈
A
N , N ≥ 0, which is the word over the alphabet A
n deﬁned by

(a1a2 · · · aN )(n) = (a1a2 · · · an)(a2a3 · · · an+1) · · · (aN −n+1aN −n+2 · · · aN ) ∈ (A
n)N −n+1

if N ≥ n, the empty word if N < n. Note that |w|v = |w(n)|v for all v ∈ A
n; in particular,
a language L is C-balanced for length n if and only if {w(n) : w ∈ L} is letter-C-balanced
(over the alphabet A
n).

Proposition 3.3. Let L ⊂ A
∗ be a factorial language that is balanced for length n, σ : A
∗ → B∗

a substitution, and u ∈ B∗ a (possibly empty) word that is a preﬁx of σ(a)u for all a ∈ A or a
suﬃx of uσ(a) for all a ∈ A. Then F (σ(L)) is balanced for length minw∈L∩An−1 |σ(w)|+|u|+1.
In particular,
• F (σ(L)) is balanced for length n if σ is non-erasing,
• F (σ(L)) is balanced for length n+1 if σ is left or right proper.

Proof. Let L ⊂ A
∗, σ : A
∗ → B∗, u ∈ B∗ be as in the statement of the proposition,
1 ≤ m ≤ minw∈L∩An−1 |σ(w)|+|u|+1. Assume w.l.o.g. that u is a preﬁx of σ(a)u for all
a ∈ A, the suﬃx case being symmetric. We deﬁne a substitution ˆσ : (A
n ∩ L)∗ → (Bm)∗ by

ˆσ(a1a2 · · · an) := (
σ(a1)pref m−1(σ(a2 · · · an)u))(m) for a1 · · · an ∈ A
n ∩ L.

(Here, ˆσ is a substitution on the alphabet A
n ∩ L, and the condition on m ensures that
pref m−1(σ(a2 · · · an)u) exists.) Then we have, for all w ∈ L,

(3.1) (σ(w)u)(m) = ˆσ(
w(n)) (σ(suﬀ n−1(w))u)(m).

Let Cn be such that L is Cn-balanced for length n. Then, by Lemma 2.1, L is letter-C1-
balanced for some C1 ≥ 0. Let w, w′ ∈ F (σ(L)) with |w| = |w′|, and write w = x σ(y) z,
w′ = x
′ σ(y′) z′ as in Lemma 3.1. Similarly to (3.1), we obtain that

(wu)(m) = (x pref m−1(σ(y)u))(m) ˆσ(y(n)) (
σ(suﬀ n−1(y))zu)(m).

Using a similar decomposition for (w′u)(m), we obtain for v ∈ Bm that

|w|v − |w′|v ≤ max {
|xz|, |x
′z′|} + (n − 1)∥σ∥ + ∑

t∈An∩L
 (|y|t − |y′|t) ∣
∣ˆσ(t)∣
∣v

≤ (2 + C1#A)∥σ∥ − 2 + (n − 1)∥σ∥ + (#A)n Cn ∥σ∥.

Here, we have used that |w|v = |w(m)|v, that L is Cn-balanced for length n, and that
|ˆσ(a1 · · · an)| = |σ(a1)| for a1 · · · an ∈ A
n ∩ L. This proves that F (σ(L)) is balanced for
length minw∈L∩An−1 |σ(w)|+|u|+1. If σ is non-erasing, then |σ(w)| ≥ n−1 for all w ∈ A
n−1,
thus F (σ(L)) is balanced for length n. If σ is left or right proper, then σ is non-erasing and
|u| ≥ 1, thus F (σ(L)) is balanced for length n+1. □

Theorem 3.4. Let L ⊂ A
∗ be a factorial language and σ : A
∗ → B∗ a substitution. If L is
factor-balanced, then F (σ(L)) is factor-balanced.

Proof. For non-erasing σ, the theorem is a direct consequence of Proposition 3.3. If F (σ(L))
is ﬁnite, then it is also factor-balanced. If F (σ(L)) is inﬁnite, then there exists a ∈ A
such that |σ(a)| ≥ 1 and {|w|a : w ∈ L} is unbounded. If L is letter-C-balanced, then
Proposition 2.2 gives some fa ≥ 0 such that |w|a ≥ fa|w| − C and thus |σ(w)| ≥ fa|w| − C
for all w ∈ L. By Proposition 3.3, balancedness of L for length n implies balancedness of
4

F (σ(L)) for length fa (n−1)−C+1. Note that fa > 0 since |w|a ≤ fa|w| + C and |w|a is
unbounded. Therefore, factor-balancedness of L implies that of F (σ(L)). □

When the incidence matrix of σ is invertible, we can also infer letter-balancedness of L
from that of F (σ(L)). Here, the incidence matrix of a substitution σ : A
∗ → B∗ is

Mσ := (|σ(a)|b)b∈B,a∈A.

Proposition 3.5. Let σ : A
∗ → B∗ be a substitution with invertible incidence matrix Mσ
and L ⊂ A
∗. If F (σ(L)) is letter-balanced, then L is letter-balanced.

Proof. If L is ﬁnite, then it is trivially letter-balanced. Assume in the following that L is
inﬁnite and Mσ invertible. Then σ is non-erasing and thus σ(L) inﬁnite. If F (σ(L)) is
letter-balanced, then Proposition 2.2 gives a frequency vector f = (fb)b∈B such that

D := {
(|σ(w)|b − |σ(w)|fb)b∈B : w ∈ L}

is a bounded set. Since (|σ(w)|b)b∈B = Mσ(|w|a)a∈A and Mσ is invertible, we have

M−1
σ D = {
(|w|a)a∈A − |σ(w)|M−1
σ f : w ∈ L}.

Therefore, the vectors (|w|a)a∈A, w ∈ L, have bounded distance from the line RM−1
σ f. Hence,
M−1
σ f is a non-negative vector and (f ′
a)a∈A := M−1
σ f/∥M−1
σ f∥1 is the frequency vector of L.
Since ∑

a∈A (|w|a − |w|f ′
a) = |w| − |w| = 0 for all w ∈ A
∗, the set

D′ := {
(|w|a − |w|f ′
a)a∈A : w ∈ L} = {
(|w|a)a∈A − |w|
∥M−1
σ f∥1 M−1
σ f : w ∈ L}

lies in the hyperplane H := {(xa)a∈A : ∑

a∈A xa = 0}. Therefore, D′ is the projection of
M−1
σ D to H along the line RM−1
σ f (which is not in H since M−1
σ f is non-negative and
non-zero), thus D′ is bounded. Hence, by Lemma 2.3, L is letter-balanced. □

4. S-adic languages

Now, we consider sequences of substitutions σ = (σk)k≥0, σk : A
∗
k+1 → A
∗
k. We set

σ[k,n) := σk ◦ σk+1 ◦ · · · ◦ σn−1
for n ≥ k ≥ 0, where σ[k,k) is the identity map; then σ[k,n) is a substitution from A
∗
n to A
∗
k.
The language of σ at level k is deﬁned by

L(k)
σ := {
w ∈ A
∗
k : w ∈ F (σ[k,n)(An)) for inﬁnitely many n > k}
,

and Lσ := L(0)
σ . (In other papers, the requirement for inﬁnitely many n > k is replaced by
“some n > k”; this can change the language only if a letter of Am does not occur in σm.)
Our deﬁnition ensures that

(4.1) F (
σ[k,n)(L(n)
σ )) = L(k)
σ for all n ≥ k ≥ 0.

A sequence of substitutions (σk)k≥0 is everywhere growing if limk→∞⟨σ[0,k)⟩ = ∞. It is
left (resp. right) proper when for each k ≥ 0 there exists n > k such that σ[k,n) is left
(resp. right) proper. The following theorem was proved in [BCBD+21, Corollary 5.5] for
unimodular incidence matrices, i.e., |det Mσk| = 1 for all k ≥ 0.

Theorem 4.1. Let σ be a left or right proper sequence of substitutions. If L(k)
σ is letter-
balanced for inﬁnitely many k, then Lσ is factor-balanced.
5

Proof. Assume that L(k)
σ is letter-balanced for inﬁnitely many k, which implies that it is
letter-balanced for all k by (4.1) and Proposition 3.2. Since σ is left or right proper, there
exist 0 = k0 < k1 < k2 < · · · such that σ[ki,ki+1) is left or right proper for all i ≥ 0. Therefore,
by Proposition 3.3, Lσ is balanced for all lengths n ≥ 1. □

The following corollary is the particular case of Theorem 4.1 with constant sequence σ =
(σ, σ, . . . ) for some substitution σ : A
∗ → A
∗; we write σ∞ for (σ, σ, . . . ). The language of a
substitution is Lσ := Lσ∞ (and consists of those w ∈ A
∗ that are in F (σn(A)) inﬁnitely often).

Corollary 4.2. Let σ : A
∗ → A
∗ be a substitution such that σk is left or right proper for
some k ≥ 1. If Lσ is letter-balanced, then Lσ is factor-balanced.

For invertible incidence matrices, letter-balancedness at level 0 implies letter-balancedness
at all levels by Proposition 3.5, which gives the following corollary of Theorem 4.1.

Corollary 4.3. Let σ = (σk)k≥0 be a left or right proper sequence of substitutions with invert-
ible incidence matrix Mσk for all k ≥ 0. If Lσ is letter-balanced, then Lσ is factor-balanced.

If σ is not proper, then we need balancedness for length 2 to infer factor-balancedness.

Theorem 4.4. Let σ be an everywhere growing sequence of substitutions such that L(k)
σ is
balanced for length 2 for inﬁnitely many k. Then Lσ is factor-balanced.

Proof. By Proposition 3.3, balancedness of L(k)
σ for length 2 implies balancedness of Lσ for
length ⟨σ[0,k)⟩+1. Since σ is everywhere growing, this implies that Lσ is factor-balanced. □

For primitive substitutions σ, a suﬃcient condition for balancedness for length n of Lσ is
given in [Ada03, Theorem 22], and it indicates that balancedness for length 2 and factor-
balancedness are closely related; see also [Que10, Section 5.4.3]. We prove that balancedness
for length 2 implies factor-balancedness for most substitutions.

Corollary 4.5. Let σ : A
∗ → A
∗ be an everywhere growing substitution. If Lσ is balanced
for length 2, then Lσ is factor-balanced.

We remark that, in Theorem 4.1, Corollary 4.3 and Theorem 4.4, factor-balancedness
holds not only for Lσ but for all L(k)
σ , k ≥ 0.

5. Thue–Morse–Sturmian languages

We conclude the paper by studying a special class of sequences of substitutions that occurs
naturally in [Ste20, KSZ22]. A language Lσ, σ ∈ {L, M, R}∞, with substitutions

L : 0 ↦→ 0, M : 0 ↦→ 01, R : 0 ↦→ 01,
1 ↦→ 10, 1 ↦→ 10, 1 ↦→ 1,

is Thue–Morse–Sturmian if σ is primitive. Recall that a sequence of substitutions (σn)n≥0
is primitive if, for each k ≥ 0, there exists n > k such that |σ[k,n)(a)|b ≥ 1 for all a ∈ An,
b ∈ Bk; in the case of σ ∈ {L, M, R}∞, this means that σ does not end with the constant
sequence L
∞ or R∞. However, the following results also hold for non-primitive sequences.

Proposition 5.1. For all σ ∈ {L, M, R}∞, Lσ is letter-2-balanced.
6

Proof. For σ = (σk)k≥0 ∈ {L, M, R}∞ \ {L, R}∞, let n ≥ 1 be minimal such that σn = M.
We claim that F (σ[0,n)({01, 10}∗)) is letter-2-balanced. Indeed, we have σ[0,n)(01) = 01w
and σ[0,n)(10) = 10w for some w ∈ {0, 1}∗. (This property is trivial for σ[n,n) and can be
shown inductively for σ[k,n), 0 ≤ k < n, since σk ∈ {L, R}.) Let v, v′ ∈ F (σ[0,n)({01, 10}∗))
with |v| = |v′|. If |v| ≥ |w|+3 then we can write v = pus, v′ = p′u′s′ such that |u|0 =
|u′|0 = |w|0+1, |u|1 = |u′|1 = |w|1+1 and ps, p′s′ ∈ F (σ[0,n)({01, 10}∗)). Since |ps| = |p′s′|
and |ps|0 − |p′s′|0 = |v|0 − |v′|0, it is suﬃcient to consider |v| ≤ |w|+2. If |v| ≤ |w|+1,
then v, v′ ∈ F (σ[0,n)({01}∗)), and it is well known that this language is letter-1-balanced; see
[Lot02, Chapter 2]. For |v| = |w|+2, we have |v|0 = |w|0+1 or v ∈ {0w0, 1w1}. Therefore,
F (σ[0,n)({01, 10}∗)) and thus Lσ are letter-2-balanced.
Let now σ ∈ {L, R}∞. If σ contains inﬁnitely many L’s and R’s, then Lσ is Sturmian and
thus letter-1-balanced; see e.g. [Lot02, Chapter 2]. Since L
n(0) = 0, L
n(1) = 10n, Rn(0) = 01n,
Rn(1) = 1, for all n ≥ 0, the languages LL∞ and LR∞ are also letter-1-balanced. Finally, if
σn = L, σk = R for all k > n, or σn = R, σk = L for all k > n, then Lσ = F (σ[0,n)({01}∗)),
which is again letter-1-balanced. □

For a characterisation of factor-balancedness of Thue–Morse–Sturmian languages, we need
the following lemma in order to show that applying any composition of substitutions L, M, R
to the Thue–Morse language, which is not factor-balanced, does not create a factor-balanced
language. More precisely, we show for σ ∈ {L, M, R}∗ that σ(011) occurs only trivially
in σ(w), w ∈ LM ∞. Here, {L, M, R}∗ is the set of compositions of substitutions in L, M, R.

Lemma 5.2. Let σ ∈ {L, M, R}∗, a, b ∈ {0, 1}, p, s, v ∈ {0, 1}∗, k ≥ 1, such that

σ(avb) = p σ(01k) s,

p is a strict preﬁx of σ(a) and s is a strict suﬃx of σ(b). Then avb = 01k (and p, s are empty)
or avb = 1k+1 (and s is empty).

Proof. The statement is clearly true when σ is the identity. For σ = σ0 ◦ σ1 ◦ · · · ◦ σn,
σi ∈ {L, M, R}, we prove the statement by induction on n.
Let ﬁrst σn = L. Then we have

σ[0,n)(L(avb)) = p σ[0,n)(0(10)k) s and 11 /∈ F (L(avb)).

If p is a strict preﬁx of σ[0,n)(a), in particular if a = 0, then σ[0,n)(av′b
′) = p σ[0,n)(01) s′ for a
preﬁx av′b
′ of L(avb) and a strict suﬃx s′ of σ[0,n)(b
′). By the induction hypothesis and since
11 ̸∈ F (L(av′b
′)), this implies that p is empty. Since σ[0,n)(0) starts with 0 and σ[0,n)(1) starts
with 1, we obtain that L(avb) = 0(10)k and thus avb = 01k. If a = 1 and p = σ[0,n)(1) p′, then
σ[0,n)(0v′b
′) = p′σ[0,n)(01) s′ for a preﬁx 10v′b
′ of L(1vb) and a strict suﬃx s′ of σ[0,n)(b
′). Now,
the induction hypothesis implies that p′ is empty, thus L(avb) = (10)k+1, i.e., avb = 1k+1.
Let now σn = M. Then we have

σ[0,n)(M(avb)) = p σ[0,n)(01(10)k) s and 111 /∈ F (M(avb)).

If p is a strict preﬁx of σ[0,n)(a), then σ[0,n)(av′b
′) = p σ[0,n)(011) s′, hence p is empty, and
avb = 01k. If a = 1 and p = σ[0,n)(1) p′, then we obtain that avb = 1k+1. If a = 0 and
p = σ[0,n)(0) p′, then σ[0,n)(1v′b
′) = p′σ[0,n)(011) s′, hence p′ is empty, which contradicts that
σ[0,n)(1) and σ[0,n)(0) start with diﬀerent letters.
Finally, let σn = R. Then we have

σ[0,n)(R(avb)) = p σ[0,n)(01k+1) s and 1k+2 /∈ F (R(avb)).
7

If p is a strict preﬁx of σ[0,n)(a), then R(avb) = 01k+1, thus avb = 01n. Otherwise, we have
a = 0 and p = σ[0,n)(0) p′, thus σ[0,n)(1v′b
′) = p′σ[0,n)(01k+1) s′, hence p′ is empty, which
contradicts that σ[0,n)(1) and σ[0,n)(0) start with diﬀerent letters. □

Theorem 5.3. Let σ = (σk)k≥0 ∈ {L, M, R}∞. Then Lσ is factor-balanced if and only if
σk ̸= M for inﬁnitely many k.

Proof. By Proposition 5.1, L(k)
σ is letter-balanced for all k ≥ 0. If σ does not end with M ∞,
then it is right proper. If σ also does not end with L
∞ or R∞, then it is everywhere growing,
and we can apply Theorem 4.1. If σ ends with LR∞ or RL
∞, then we have seen in the proof
of Proposition 5.1 that Lσ = F (σ({01}∗)) for some σ ∈ {L, M, R}∗, which is factor-balanced.
The cases of LL∞ and LR∞ are similar.
Consider now σ ending with M ∞. We ﬁrst prove that the Thue–Morse language LM ∞ is
not balanced for length 2, giving more details than [Sad16, Example 3]; a more general proof
can be found in [BCB19]. To this end, deﬁne recursively words wn, w′
n ∈ LM ∞ by

w1 = 00, M 2(w2n−1) = 0 w2n 0, M 2(w2n) = 1 w2n+1 1,

w′
1 = 01, M 2(w′
2n−1) = w′
2n 01, M 2(w′
2n) = w′
2n+1 10,

with |wn| = |w′
n| = 4n+2
3 . The second higher block codes are (w1)(2) = (00), (w′
1)(2) = (01),

M 2
2 ((w2n−1)(2)) (01)(11) = (01) (w2n)(2), M 2
2 ((w2n)(2)) (10)(00) = (10) (w2n+1)(2),

M 2
2 ((w′
2n−1)(2)) (10) = (w′
2n)(2), M 2
2 ((w′
2n)(2)) (01) = (w′
2n+1)(2),

with the substitution

M2 : ({0, 1}2)∗ → ({0, 1}2)∗, (00) ↦→ (01)(10), (01) ↦→ (01)(11),
(10) ↦→ (10)(00), (11) ↦→ (10)(01).

Using the abelianizations

ℓ2(w) =
 





|w|00
|w|01
|w|10
|w|11




 , MM2 = (|M2(cd)|ab)ab,cd∈{00,01,10,11} =
 





0 0 1 0
1 1 0 1
1 0 1 1
0 1 0 0




 ,

we obtain that

ℓ2(w2n) = M2
M2 ℓ2(w2n−1) + ℓ2(11), ℓ2(w2n+1) = M2
M2 ℓ2(w2n) + ℓ2(00),

ℓ2(w′
2n) = M2
M2 ℓ2(w′
2n−1) + ℓ2(10), ℓ2(w′
2n+1) = M2
M2 ℓ2(w′
2n) + ℓ2(00).

The right eigenvectors of MM2 (to the eigenvalues 2, −1, 0, 1) are

v2 =
 





1
2
2
1




 , v−1 =
 




 1
−1
−1
1
 



 , v0 =
 




 1
0
0
−1




 , v1 =
 




 1
−1
1
−1




 ,

thus
 ℓ2(w2n) = 42n − 1
18 v2 + 2n
3 v−1 − 1
2v0 and ℓ2(w′
2n) = 42n − 1
18 v2 − n
3 v−1 − 1
2 v0,

8

hence ℓ2(w2n) − ℓ2(w′
2n) = n v−1, i.e.,

|w2n|00 − |w′
2n|00 = |w′
2n|01 − |w2n|01 = |w′
2n|10 − |w2n|10 = |w2n|11 − |w′
2n|11 = n.

To ﬁnish the proof of the theorem, we have to show that F (σ(LM ∞)) is not factor-balanced
for all σ ∈ {L, M, R}∗. Since 111 /∈ LM ∞, Lemma 5.2 implies that |σ(w)|σ(011) = |w|011 for
all w ∈ LM ∞, and we clearly have 0 ≤ |w|11 − |w|011 ≤ 1. Therefore, we have
∣
∣|σ(w)|σ(011) − |σ(w′)|σ(011)∣
∣ ≥ ∣
∣|w|11 − |w′|11∣
∣ − 1

for all w, w′ ∈ LM ∞. Since |w|11 − |w′|11 is unbounded for w, w′ ∈ LM ∞ with |w| = |w′|, it is
also unbounded when we restrict to w, w′ with |w|0 = |w′|0 (and |w|1 = |w|′
1). Then we have
|σ(w)| = |σ(w′)|, thus σ(LM ∞) is not balanced for length |σ(011)|. □

We remark that, by Proposition 3.3, F (σ ◦ L(LM ∞)) is balanced for length |σ(0)| + 1
for any substitution σ. On the other hand, we have seen in the proof of Theorem 5.3 that
F (σ ◦ L(LM ∞)) is not balanced for length |σ(01010)| for any substitution σ ∈ {L, M, R}∗.

References

[Ada03] B. Adamczewski, Balances for ﬁxed points of primitive substitutions, Theoret. Comput. Sci.
307 (2003), no. 1, 47–75.
[Ada04] , Symbolic discrepancy and self-similar dynamics, Ann. Inst. Fourier (Grenoble) 54
(2004), no. 7, 2201–2234 (2005).
[BCB19] V. Berth´e and P. Cecchi Bernales, Balancedness and coboundaries in symbolic systems, Theoret.
Comput. Sci. 777 (2019), 93–110.
[BCBD
+21] V. Berth´e, P. Cecchi Bernales, F. Durand, J. Leroy, D. Perrin, and S. Petite, On the dimension
group of unimodular S-adic subshifts, Monatsh. Math. 194 (2021), no. 4, 687–717.
[BT02] V. Berth´e and R. Tijdeman, Balance properties of multi-dimensional words, Theoret. Comput.
Sci. 273 (2002), no. 1-2, 197–224.
[FV02] I. Fagnot and L. Vuillon, Generalized balances in Sturmian words, Discrete Appl. Math. 121
(2002), no. 1-3, 83–101.
[KSZ22] V. Komornik, W. Steiner, and Y. Zou, Unique double base expansions, 2022, arXiv:2209.02373.
[Lot02] M. Lothaire, Algebraic combinatorics on words, Encyclopedia of Mathematics and its Applica-
tions, vol. 90, Cambridge University Press, Cambridge, 2002.
[MH40] M. Morse and G. A. Hedlund, Symbolic dynamics II. Sturmian trajectories, Amer. J. Math. 62
(1940), 1–42.
[Que10] M. Queﬀ´elec, Substitution dynamical systems—spectral analysis, second ed., Lecture Notes in
Mathematics, vol. 1294, Springer-Verlag, Berlin, 2010.
[Sad16] L. Sadun, Finitely balanced sequences and plasticity of 1-dimensional tilings, Topology Appl.
205 (2016), 82–87.
[Ste20] W. Steiner, Thue-Morse-Sturmian words and critical bases for ternary alphabets, Bull. Soc.
Math. France 148 (2020), no. 4, 597–611.

Universit´e de Lyon, ENS de Lyon, D´epartement informatique de l’ENS de Lyon, 46 all´ee
d’Italie, F-69007 Lyon, France
Email address: leo.poirier@ens-lyon.fr

Universit´e Paris Cit´e, CNRS, IRIF, F-75006 Paris, France
Email address: steiner@irif.fr
 9
