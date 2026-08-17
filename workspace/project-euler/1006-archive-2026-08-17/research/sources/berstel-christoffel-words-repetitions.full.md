<!-- source: https://webpages.math.luc.edu/~lauve/papers/wordsbook.pdf | converted from PDF -->

Combinatorics on Words:
Christoﬀel Words and Repetitions in Words

Jean Berstel Aaron Lauve Christophe Reutenauer
Franco Saliola

2008

Ce livre est d´edi´e `a la m´emoire de Pierre Leroux (1942–2008).

Contents

I Christoﬀel Words 1

1 Christoﬀel Words 3
1.1 Geometric deﬁnition . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Cayley graph deﬁnition . . . . . . . . . . . . . . . . . . . . . 6

2 Christoﬀel Morphisms 9
2.1 Christoﬀel morphisms . . . . . . . . . . . . . . . . . . . . . . 9
2.2 Generators . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

3 Standard Factorization 19
3.1 The standard factorization . . . . . . . . . . . . . . . . . . . . 19
3.2 The Christoﬀel tree . . . . . . . . . . . . . . . . . . . . . . . . 23

4 Palindromization 27
4.1 Christoﬀel words and palindromes . . . . . . . . . . . . . . . 27
4.2 Palindromic closures . . . . . . . . . . . . . . . . . . . . . . . 28
4.3 Palindromic characterization . . . . . . . . . . . . . . . . . . 36

5 Primitive Elements in the Free Group F2 41
5.1 Positive primitive elements of the free group . . . . . . . . . . 41
5.2 Positive primitive characterization . . . . . . . . . . . . . . . 43

6 Characterizations 47
6.1 The Burrows–Wheeler transform . . . . . . . . . . . . . . . . 47
6.2 Balanced1 Lyndon words . . . . . . . . . . . . . . . . . . . . . 50
6.3 Balanced2 Lyndon words . . . . . . . . . . . . . . . . . . . . . 50
6.4 Circular words . . . . . . . . . . . . . . . . . . . . . . . . . . 51
6.5 Periodic phenomena . . . . . . . . . . . . . . . . . . . . . . . 54

i

7 Continued Fractions 57
7.1 Continued fractions . . . . . . . . . . . . . . . . . . . . . . . . 57
7.2 Continued fractions and Christoﬀel words . . . . . . . . . . . 58
7.3 The Stern–Brocot tree . . . . . . . . . . . . . . . . . . . . . . 62

8 The Theory of Markoﬀ Numbers 67
8.1 Minima of quadratic forms . . . . . . . . . . . . . . . . . . . . 67
8.2 Markoﬀ numbers . . . . . . . . . . . . . . . . . . . . . . . . . 69
8.3 Markoﬀ’s condition . . . . . . . . . . . . . . . . . . . . . . . . 71
8.4 Proof of Markoﬀ’s theorem . . . . . . . . . . . . . . . . . . . 75

II Repetitions in Words 81

1 The Thue–Morse Word 83
1.1 The Thue–Morse word . . . . . . . . . . . . . . . . . . . . . . 83
1.2 The Thue–Morse morphism . . . . . . . . . . . . . . . . . . . 84
1.3 The Tarry-Escott problem . . . . . . . . . . . . . . . . . . . . 86
1.4 Magic squares . . . . . . . . . . . . . . . . . . . . . . . . . . . 90

2 Combinatorics of the Thue–Morse Word 93
2.1 Automatic sequences . . . . . . . . . . . . . . . . . . . . . . . 93
2.2 Generating series . . . . . . . . . . . . . . . . . . . . . . . . . 96
2.3 Overlaps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
2.4 Complexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
2.5 Formal languages . . . . . . . . . . . . . . . . . . . . . . . . . 104
2.6 The Tower of Hanoi . . . . . . . . . . . . . . . . . . . . . . . 111

3 Square-Free Words 119
3.1 One example, three constructions . . . . . . . . . . . . . . . . 119
3.2 Square-free morphisms and codes . . . . . . . . . . . . . . . . 123
3.3 A 3-square-free test . . . . . . . . . . . . . . . . . . . . . . . . 126
3.4 A 2-square-free test . . . . . . . . . . . . . . . . . . . . . . . . 129

4 Squares in Words 133
4.1 Counting squares . . . . . . . . . . . . . . . . . . . . . . . . . 133
4.2 Centered squares . . . . . . . . . . . . . . . . . . . . . . . . . 138
4.3 Preﬁx arrays . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
4.4 Crochemore factorization . . . . . . . . . . . . . . . . . . . . 142
4.5 Suﬃx trees . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145

5 Repetitions and Patterns 157
5.1 Maximal repetitions . . . . . . . . . . . . . . . . . . . . . . . 157
5.2 Repetition thresholds . . . . . . . . . . . . . . . . . . . . . . . 158
5.3 Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
5.4 Zimin patterns . . . . . . . . . . . . . . . . . . . . . . . . . . 164
5.5 Bi-ideal sequences . . . . . . . . . . . . . . . . . . . . . . . . 167
5.6 Repetitions in Sturmian words . . . . . . . . . . . . . . . . . 168

Bibliography 171

Index 181

Preface

This book grew out of two series of ﬁve two-hour lectures, given by Jean
Berstel and Christophe Reutenauer in March 2007. The lectures were deliv-
ered during the school on “Combinatorics on Words” organized by Sreˇcko
Brlek, Christophe Reutenauer and Bruce Sagan that took part within the
theme semester on Recent Advances in Combinatorics on Words at the Cen-
tre de Recherches Math´ematiques (CRM), Montr´eal, Canada.
Notes for the lectures were written down by Aaron Lauve and Franco
Saliola. They have augmented their notes with several topics and have added
more than 100 exercises. There has been a lot of work in adding bibliographic
references and a detailed index.
The text is divided into two parts. Part I, based on the lectures given by
Christophe Reutenauer, is a comprehensive and self-contained presentation
of the current state of the art in Christoﬀel words. These are ﬁnitary versions
of Sturmian sequences. It presents relationships between Christoﬀel words
and topics in discrete geometry, group theory, and number theory. Part I
concludes with a new exposition of the theory of Markoﬀ numbers.
Part II, based on the lectures by Jean Berstel, starts with a system-
atic exposition of the numerous properties, applications, and interpretations
of the famous Thue-Morse word. It then presents work related to Thue’s
construction of a square-free word, followed by a detailed exposition of a
linear-time algorithm for ﬁnding squares in words. This part concludes with
a brief glimpse of several additional problems with origins in the work of
Thue.

Acknowledgements

We gratefully acknowledge the generosity of Amy Glen and Gw´ena¨el Ri-
chomme, who agreed to read a preliminary version of this text. Implementa-
tion of their numerous comments improved the quality of the text tremen-
dously. We also thank Anouk Bergeron-Brlek for lending us a third set of

v

notes and Lise Tourigny through whom all things are possible. Finally, we
would like to thank the CRM and Fran¸cois Bergeron, the principal organizer
of the CRM theme semester, for providing an excellent scientiﬁc program
and working environment during the semester as well as support throughout
the preparation of this text.

Typesetting

The book was typeset with the LATEX document preparation system together
with the following LATEX packages:

algorithm2e
amsbsy
amsfonts
amsmath
amsrefs
amssymb
amsthm
 array
bbm
calc
caption
color
colordvi
ednotes
 gastex
graphicx
ifthen
mathtools
multicol
pstricks
pst-node
 pst-poly
pst-tree
rotating
stmaryrd
subfigure
xypic

and Will Robertson’s LATEX code for typesetting magic squares [Rob2005].

Notation

We gather in one place the notational conventions shared by the two parts.
The reader may also consult the subject index to locate the major occur-
rences within the text of most of the symbols and bold words below.

Let N denote the set of nonnegative integers. If a, b and n are integers,
then the notation a ≡ b mod n shall mean that a − b is divisible by n.
Equivalently, a ≡ b mod n if and only if a and b have the same remainder
upon division by n.
Let A denote a ﬁnite set of symbols. The elements of A are called letters
and the set A is called an alphabet. A word over an alphabet A is an
element of the free monoid A∗ generated by A. The identity element ǫ of A∗

is called the empty word. Given a word w ∈ A∗, the square of w is the
monoid product w2 = ww in A∗. Higher powers of w are deﬁned analogously.
We frequently take A to be a subset of the nonnegative integers N. The reader
is cautioned to read 101 not as “one hundred and one” but as “1 · 0 · 1,” an
element of {0, 1}3.
If w ∈ A∗, then there exists a unique integer r ≥ 0 and unique letters
a1, a2, . . . , ar ∈ A such that w = a1a2 · · · ar; the number r is called the
length of w and denoted by |w|. A positive integer p is a period of w if
ai = ai+p for all 1 ≤ i ≤ |w| − p. (Note that if p ≥ |w|, then p is a period
of w.) If w ∈ A∗ and a ∈ A, then |w|a denotes the number of occurrences of
the letter a in the word w so that

|w| = ∑

a∈A |w|a.

If w = a1a2 · · · ar, where a1, a2, . . . , ar ∈ A, then the reversal of w is the
word
 ̃w = ar · · · a2a1.

ix

We say w is a palindrome if w = ̃w.
An inﬁnite word is a map from N to A, typically written in bold or
as a sequence such as w = w(0)w(1)w(2) · · · or w = w0w1w2 · · · (we freely
pass between the two notations wn and w(n) in what follows). Any ﬁnite
word m gives rise to a periodic inﬁnite word denoted m∞, namely

m∞ = mmm · · · .

A factorization of a ﬁnite word w over A is a sequence (w1, w2, . . . , wr)
of words over A such that the relation w = w1w2 · · · wr holds in the monoid
A∗. We sometimes write w = (w1, w2, . . . , wr) to emphasize a particular
factorization of w. Factorizations of inﬁnite words are similarly deﬁned (with
wr necessarily the only inﬁnite word in the sequence). If w is a ﬁnite or
inﬁnite word over A and w = uv for some (possibly empty) words u and v,
then u is called a preﬁx of w and v is a suﬃx of w. Conversely, a factor of a
ﬁnite or inﬁnite word w is a ﬁnite word v such that w = uvu′ for some words
u, u′; we say v is a proper factor if v ̸= ǫ and uu′ ̸= ǫ. Given two words
w, w′ ∈ A∗, we say that w is a conjugate of w′ if there exists u, v ∈ A∗ such
that w = uv and w′ = vu.
Let w be a ﬁnite or inﬁnite word over an alphabet A and write w =
a0a1a2 · · · , where a0, a1, a2, . . . ∈ A. If v is is a factor of w, then

v = aiai+1 · · · aj for some 0 ≤ i < j,

and aiai+1 · · · aj is said to be an occurrence of v in w. (Speciﬁcally, an
occurrence of v in w also includes information about where it appears in w;
for the factor above, we say the starting index is i.) If u and v are words,
then u is said to contain v if there is an occurrence of v in u.
Given two alphabets A, B, a morphism from A∗ to B∗ shall always
mean a “morphism of monoids.” That is, a set mapping f : A∗ → B∗

satisfying f (uv) = f (u)f (v) for all u, v ∈ A
∗.

In particular, f (ǫA∗) = ǫB∗ since the empty word ǫ is the only element in
a free monoid satisfying w2 = w. The identity morphism on A∗ is the
morphism sending each w ∈ A∗ to itself. The trivial morphism from A∗

to B∗ is the morphism sending each w ∈ A∗ to ǫB∗.

Part I

Christoﬀel Words

1

Chapter 1

Christoﬀel Words

Although the theory of Christoﬀel words began to take shape in the late
1800s [Chr1875, Smi1876, Mar1879, Mar1880, Mar1881, Chr1888], the term
was not introduced until 1990 by Jean Berstel [Ber1990]. By now there are
numerous equivalent deﬁnitions and characterizations of Christoﬀel words.
We choose as our working deﬁnition and point-of-view a geometric one: a
Christoﬀel word is a “discretization” of a line segment in the plane by a
path in the integer lattice Z × Z [OZ1981, Ber1990, BL1993].

1.1 Geometric deﬁnition

Notation. If a, b ∈ N, then a and b are said to be relatively prime if 1 is
the only positive integer that divides both a and b. The notation a ⊥ b shall
mean “a and b are relatively prime”.

Suppose a, b ∈ N and a ⊥ b. The lower Christoﬀel path of slope b
a is
the path1 from (0, 0) to (a, b) in the integer lattice Z × Z that satisﬁes the
following two conditions.

(i) The path lies below the line segment that begins at the origin and
ends at (a, b).

(ii) The region in the plane enclosed by the path and the line segment
contains no other points of Z × Z besides those of the path.

1By a path in Z × Z from (a, b) to (c, d) we actually mean a continuous map α : [0, 1] →
(Z × R) ∪ (R × Z) such that α(0) = (a, b) and α(1) = (c, d). Since such paths are essentially
determined by the points of Z × Z that lie on the path, we identify such a path with a
sequence of points in Z × Z with consecutive points of the sequence diﬀering by ⃗e1 or ⃗e2,
where ⃗e1 and ⃗e2 are the standard basis vectors of R2.

3

4 CHAPTER 1. CHRISTOFFEL WORDS

Upper Christoﬀel paths are deﬁned analogously, using paths in Z × Z
that lie above the line segment. See Figure 1.1 for examples. The unmodiﬁed
term Christoﬀel path will always mean lower Christoﬀel path.

Figure 1.1: The lower and upper Christoﬀel paths of slope 4
7 .

Since every step in a Christoﬀel path moves from a point (i, j) ∈ Z × Z
to either the point (i + 1, j) or the point (i, j + 1), a Christoﬀel path of slope
b
a determines a word C(a, b) in the alphabet {x, y} by encoding steps of the
ﬁrst type by the letter x and steps of the second type by the letter y. See
Figure 1.2.

x x
 x x
 x x
 x

y
 y
 y
 y
 x
 x x
 x x
 x x

y
 y
 y
 y

Figure 1.2: The lower and upper Christoﬀel words of slope 4
7 are
xxyxxyxxyxy and yxyxxyxxyxx, respectively.

Deﬁnition 1.1. Let a, b ∈ N. A word w ∈ {x, y}∗ is a (lower) Christoﬀel
word of slope b
a if a ⊥ b and w = C(a, b). A Christoﬀel word is trivial
if its length is at most 1, and is nontrivial otherwise. Upper Christoﬀel
words are deﬁned analogously.

Since every positive rational number can be expressed as b
a where a ⊥ b
in only one way, there is a unique lower Christoﬀel word of slope r for all
positive rational numbers r.

Examples. The following are examples of Christoﬀel words.
1. The Christoﬀel word of slope 0 is x, since C(1, 0) = x.

1.1. GEOMETRIC DEFINITION 5

2. The Christoﬀel word of slope ∞ is y, since C(0, 1) = y.
3. The Christoﬀel word of slope 1 is xy, since xy = C(1, 1).
4. The Christoﬀel word of slope 4
7 is xxyxxyxxyxy (see Figure 1.2).

Remarks. 1. The empty word ǫ is not a Christoﬀel word since 0 ̸⊥ 0. There-
fore, x and y are the only trivial Christoﬀel words.
2. The square or higher power of a Christoﬀel word is not a Christof-
fel word. Nor is a Christoﬀel word the power of a shorter word, that is,
Christoﬀel words are primitive words. These statements follow from the
observation that the number of occurrences of the letters x and y in the
k-th power of a word are both multiples of k (so they cannot be relatively
prime if k ≥ 2).
3. Christoﬀel words have a natural generalization to inﬁnite sequences:
replace the deﬁning line segment of slope b
a with an inﬁnite ray of irrational
slope before building the lattice path. The resulting right-inﬁnite word is
called a (characteristic) Sturmian word. See [PF2002], [Lot2002, Chapter
2] or [AS2003] for more information. While many of the references cited in
what follows oﬀer results at this level of generality, we restrict ourselves to
Christoﬀel words here.

Exercise 1.1. Christoﬀel words are primitive words, as are all of their
conjugates.

Exercise 1.2. Suppose a and b are nonnegative integers. Then a ⊥ b if
and only if the line segment from (0, 0) to (a, b) contains no integer points
besides (0, 0) and (a, b).

Exercise 1.3. Suppose a ⊥ b. Prove that the region bounded by the segment
from (0, 0) to (a, b) and the Christoﬀel path from (0, 0) to (a, b) has area
1
2 (a + b − 1). (Hint: Consider the region bounded by the upper and lower
Christoﬀel words.)

Exercise 1.4. Suppose a and b are nonnegative integers. Then a ⊥ b if and
only if a ⊥ (a + b).

Exercise 1.5. (Fibonacci word) Let φ
∨ denote the conjugate 1−√5
2 of the
golden ratio. Using the Christoﬀel construction, compute the ﬁrst 16 or so
letters in the (Sturmian) word s corresponding to the ray of slope −φ
∨. The
inﬁnite word f satisfying s = xf is called the Fibonacci word. (The word
f is the “cutting sequence” of the ray of slope −φ
∨: it records the order in
which the ray intersects the lines x = i and y = j for i, j ∈ N.)

6 CHAPTER 1. CHRISTOFFEL WORDS

1.2 Cayley graph deﬁnition

We introduce an equivalent deﬁnition for the Christoﬀel word of slope b
a
that will occasionally be useful. In fact, it is the deﬁnition originally used by
Christoﬀel [Chr1875]. It amounts to reading edge-labellings of the Cayley
graph of Z/(a+b)Z.

Deﬁnition 1.2. Suppose a ⊥ b and (a, b) ̸= (0, 1). The label of a point
(i, j) on the (lower) Christoﬀel path of slope b
a is the number ib−ja
a . That
is, the label of (i, j) is the vertical distance from the point (i, j) to the line
segment from (0, 0) to (a, b).

0
7 4
7 8
7

1
7 5
7 9
7

2
7 6
7 10
7

3
7 7
7

0
7

Figure 1.3: The labels of the points on the Christoﬀel path of
slope 4
7 .

The labels 1
7 and 10
7 from Figure 1.3 hold a special place in the theory.
We return to them in Chapters 3 and 2, respectively. Exercise 1.8 gives an
interesting fact about the label 3
7 (or rather, the number 3).
Now, suppose w is a lower Christoﬀel word of slope b
a and suppose ( s
a , t
a )

are two consecutive labels on the Christoﬀel path from (0, 0) to (a, b). Either
( s
a , t
a ) represents a horizontal step (in which case t = s + b) or it represents
a vertical step (in which case t = s − a). The following lemma summarizes
these observations.

Lemma 1.3. Suppose w is a lower Christoﬀel word of slope b
a and a ⊥ b.
If s
a and t
a are two consecutive labels on the Christoﬀel path from (0, 0) to
(a, b), then t ≡ s + b mod (a + b). Moreover, t takes as value each integer
0, 1, 2, . . . , a + b − 1 exactly once as ( s
a , t
a ) ranges over all consecutive pairs
of labels.

We have discovered an equivalent deﬁnition of (lower) Christoﬀel words.
(See Exercise 1.7 for details.)

1.2. CAYLEY GRAPH DEFINITION 7

Deﬁnition 1.4. Suppose a ⊥ b. Consider the Cayley graph of Z/(a + b)Z
with generator b. It is a cycle, with vertices 0, b, 2b, 3b, . . . , a, 0 mod (a + b).
Starting from zero and proceeding in the order listed above,

(i) label those edges (s, t) satisfying s < t by x;

(ii) label those edges (s, t) satisfying s > t by y;

(iii) read edge-labels in the prescribed order, i.e., 0 x
→ b ∗
→ · · · ∗
→ a y
→ 0.

The lower Christoﬀel word of slope b
a is the word x · · · y formed above.

Example. Pick a = 7 and b = 4. Figure 1.4 shows the Cayley graph of Z/11Z
with generator 4 and edges u → v labelled x or y according to whether or not
u < v. Reading the edges clockwise from 0 yields the word xxyxxyxxyxy,

0 x 4 x

8 y

1
x
5
x9
y
2x

6
x

10
y 3
x 7 y

Figure 1.4: The Cayley graph of Z/(7+4)Z with generator 4 and
the associated Christoﬀel word.

which is the Christoﬀel word of slope 4
7 (see Figure 1.2).

Remark. Had we chosen the generator a instead of b for Z/(a + b)Z and
swapped the roles of x and y in Deﬁnition 1.4, the resulting word would
have been the upper Christoﬀel word of slope b
a . (This fact is immediate
after Proposition 4.2 but perhaps diﬃcult to see before it.)

Exercise 1.6. Suppose a ⊥ b. Let (i, j) be the point on the Christoﬀel path
path from (0, 0) to (a, b) with label t
a . Then t ≡ (i + j)b mod (a + b) and
t ≡ ((a − i) + (b − j))a mod (a + b).

Exercise 1.7. Let w be the Christoﬀel word of slope b
a . Let wk denote the
(k + 1)-st letter of w.

(a) wk = x if and only if kb mod (a + b) < (k + 1)b mod (a + b).

8 CHAPTER 1. CHRISTOFFEL WORDS

(b) wk = y if and only if the set {kb + 1, kb + 2, . . . , kb + b} contains a
multiple of a + b.

Exercise 1.8. ([Sim2004, Theorem 3]) Suppose a ⊥ b and suppose w =
w0w1 · · · wa+b−1 is the Christoﬀel word of slope b
a , where wi ∈ {x, y} for
0 ≤ i < a + b. If 0 < c < a + b is such that ca ≡ −1 mod (a + b), show that
{jc mod (a + b) | j = 0, 1, . . . , a − 1
} = {
k mod (a + b) | wk = x
}.
Chapter 2

Christoﬀel Morphisms

In this chapter we introduce the monoid of Christoﬀel morphisms and exhibit
a minimal set of generators for the monoid. See also Chapter 2 of [Lot2002].

2.1 Christoﬀel morphisms

Deﬁnition 2.1. A Christoﬀel morphism is an endomorphism of the
free monoid {x, y}∗ that sends each Christoﬀel word onto a conjugate of
a Christoﬀel word.

Note that the set of Christoﬀel morphisms is closed under composition
since any endomorphism of {x, y}∗ maps conjugate words to conjugate words
(Exercise 2.1).
If G is an endomorphism of {x, y}∗ and w = a0a1 · · · ar is a word in
{x, y}∗ with a0, a1 . . . , ar ∈ {x, y}, then

G(w) = G(a0a1 · · · ar) = G(a1)G(a2) · · · G(ar).

Therefore, G is determined by the images of x and y, so we identify G with
the ordered pair (G(x), G(y)).

Example. We use the above notation to deﬁne the following ﬁve important
endomorphisms of {x, y}∗.

G = (x, xy), D = (yx, y),
̃G = (x, yx), ̃D = (xy, y),

E = (y, x).

9

10 CHAPTER 2. CHRISTOFFEL MORPHISMS

It is easy to see that these ﬁve morphisms are injective on {x, y}∗ (Exercise
2.4). The remainder of this section is devoted to showing that they are also
Christoﬀel morphisms.

Lemma 2.2. The morphism G maps the Christoﬀel word of slope b
a to the
Christoﬀel word of slope b
a+b . The morphism ̃D maps the Christoﬀel word
of slope b
a to the Christoﬀel word of slope a+b
a .

Proof. We ﬁrst prove the result for G. Suppose a ⊥ b. The Christoﬀel word
w of slope b
a , by deﬁnition, encodes the steps of the Christoﬀel path from
(0, 0) to (a, b): the letter x encodes the step ⃗e1 and the letter y encodes the
step ⃗e2, where ⃗e1 and ⃗e2 are the standard basis vectors of R2. Since G maps
x to x and y to xy, the word G(w) corresponds to the path obtained from
the Christoﬀel path from (0, 0) to (a, b) by replacing each step ⃗e2 by the two
steps ⃗e1 and ⃗e2. We will show that this path is the Christoﬀel path from
(0, 0) to (a + b, b), implying that G(w) is the Christoﬀel word of slope b
a+b .
Deﬁne a linear transformation G : R2 → R2 by G(c, d) = (c + d, d) for
all (c, d) ∈ R2. Let W denote the Christoﬀel path from (0, 0) to (a, b). Then
G(W ) is a path in the integer lattice Z × Z consisting of steps G(⃗e1) = ⃗e1
and G(⃗e2) = ⃗e1 + ⃗e2. See Figure 2.1. We argue that the path obtained from

W G
−−−→ G(W )

Figure 2.1: The image of a Christoﬀel path W under the linear
transformation G.

G(W ) by replacing the steps ⃗e1 + ⃗e2 with the pair of steps ⃗e1 and ⃗e2 is the
Christoﬀel path from (0, 0) to (a + b, b).
Let R denote the region between the Christoﬀel path W and the line
segment from (0, 0) to (a, b). Then there are no integer points in the interior
of the region G(R) because G is a linear transformation and the region R
contains no integer points in its interior. Therefore, there are no integer
points in the interior of the region obtained from G(R) by adjoining the
triangles with vertices ⃗v, ⃗v +⃗e1 and ⃗v + (⃗e1 +⃗e2) whenever ⃗v and ⃗v + (⃗e1 +⃗e2)
are in G(R). See Figure 2.2. The boundary of this new region consists of the
line segment from (0, 0) to (a + b, b) and the path P obtained from the path
G(W ) by replacing the steps ⃗e1 +⃗e2 with the steps ⃗e1 and ⃗e2. Also, (a+b) ⊥ b
since a ⊥ b (see Exercise 1.2 or 1.4). Therefore, P is the Christoﬀel path
from (0, 0) to (a + b, b). Moreover, P is the path encoded by the word G(w)

2.1. CHRISTOFFEL MORPHISMS 11

G
−−−→

Figure 2.2: The image of the region between the line segment
and the Christoﬀel path from (0, 0) to (3, 2) under the map G.

since P is obtained from the Christoﬀel path from (0, 0) to (a, b) by replacing
each step ⃗e2 with the steps ⃗e1 and ⃗e2 (see Figure 2.3). Hence, G(w) is the
Christoﬀel word of slope b
a+b .

w
 G
−→ −→ G(w)

Figure 2.3: The geometric interpretation of the morphism G.

The proof that ̃D(w) is a Christoﬀel word for any Christoﬀel word w is
similar: deﬁne a linear transformation ̃D : R2 → R2 by ̃D(c, d) = (c, c + d)
for all (c, d) ∈ R2 and argue, as above, that ̃D maps the Christoﬀel word of
slope b
a to the Christoﬀel word of slope a+b
a .

Tracing backwards through the proof we also have the following result.

Corollary 2.3. If u is a Christoﬀel word of slope at most one, then the
unique word w such that G(w) = u is a Christoﬀel word. If u is a Christoﬀel
word of slope at least one, then the unique word w such that ̃D(w) = u is a
Christoﬀel word.
 G(w)
 x ←[ x
xy ←[ y
−−−−−→ w

Figure 2.4: Christoﬀel words G(w) of slope less than 1 come from
Christoﬀel words w.

The next lemma relates the image of G with that of ̃G. We will use it
again in future chapters.

12 CHAPTER 2. CHRISTOFFEL MORPHISMS

Lemma 2.4. For every word w ∈ {x, y}∗, there exists a word u ∈ {x, y}∗

such that G(w) = xu and ̃G(w) = ux, and a word v ∈ {x, y}∗ such that
D(w) = yv and ̃D(w) = vy.

Proof. We prove the result for G and ̃G; the proof for D and ̃D is the same.
Proceed by induction on the length of w. If |w| = 1, then w is either x or y. So
G(x) = x = ̃G(x) with u = ǫ, or G(y) = xy and ̃G(y) = yx with u = y. This
establishes the base case of the induction. Let w be a word of length r ≥ 1
and suppose the claim holds for all words of length less than r. If w = xw′ for
some w′ ∈ {x, y}∗, then the induction hypothesis implies there exists a word
u′ ∈ {x, y} such that G(w′) = xu′ and ̃G(w′) = u′x. Therefore, G(w) =
G(x)G(w′) = xxu′ and ̃G(w) = ̃G(x) ̃G(w′) = xu′x. Taking u = xu′, we
are done. Suppose, instead, that w = yw′. Then the induction hypothesis
implies there exists u′ ∈ {x, y} such that G(w′) = xu′ and ̃G(w′) = u′x.
Here, G(w) = G(y)G(w′) = xyxu′ and ̃G(w) = ̃G(y) ̃G(w′) = yxu′x, so
take u = yxu′.

Corollary 2.5. The morphisms G, D, ̃G and ̃D are Christoﬀel morphisms.

Proof. By Lemma 2.2, G and ̃D map Christoﬀel words to Christoﬀel words.
Hence, they are Christoﬀel morphisms. We prove that ̃G is a Christoﬀel
morphism; the same argument proves that D is a Christoﬀel morphism. Let
w be a Christoﬀel word. Lemma 2.4 implies there exists a word u ∈ {x, y}∗

such that G(w) = xu and ̃G(w) = ux. Therefore, G(w) and ̃G(w) are
conjugate words. Since G(w) is a Christoﬀel word, ̃G(w) is a conjugate of
a Christoﬀel word; that is, ̃G is a Christoﬀel morphism.

We now turn to proving that E is a Christoﬀel morphism.

Lemma 2.6. The morphism E maps lower Christoﬀel words of slope r onto
upper Christoﬀel words of slope 1
r .

Proof. This follows from an argument similar to that of Lemma 2.2, by using
reﬂection about the line x = y. See Figure 2.5.

Lemma 2.7 (Cohn [Coh1972], de Luca, Mignosi [dLM1994]). Suppose a ⊥
b. The lower and upper Christoﬀel words of slope b
a are conjugates.

Proof. Suppose a ⊥ b and let w be the Christoﬀel word of slope b
a . The word
ww encodes a path in Z × Z from (0, 0) to (2a, 2b). It consists of two copies
of the Christoﬀel path of slope b
a , the ﬁrst starting at the origin and the
second starting at (a, b). See Figure 2.6.

2.1. CHRISTOFFEL MORPHISMS 13

Figure 2.5: The geometric interpretation of the morphism E is
reﬂection about the line x = y.

Let P denote the point on the ﬁrst copy of the Christoﬀel path that is
farthest (vertically) from the line segment deﬁning the Christoﬀel path. By
Lemma 1.3, this distance is a+b−1
a . Let P ′ denote the corresponding point on
the translated copy of the Christoﬀel path. Then P and P ′ determine a word
w′ ∈ {x, y}∗ by encoding the part of the path from P to P ′ as a word in the
letters x, y. Note that w′ is a factor of ww of length equal to that of w. Since
w′ is a factor of ww and l(w′) = l(w), the words w′ and w are conjugate
(see Exercise 2.3). It remains to show that w′ is the upper Christoﬀel word

P
 P ′

Figure 2.6: The path in Z × Z corresponding to the word ww =
xxyxyxxyxy. The factor corresponding to the path from P to P ′

is w′ = yxyxx. There are no integer points in the shaded region,
so w′ is an upper Christoﬀel word.

of slope b
a . We will argue that there is no other integer point in the region
(shaded in Figure 2.6) enclosed by the line segment P P ′ and the path from
P to P ′. The argument is illustrated in Figure 2.7. Suppose (i, j − 1) is an
integer point directly below a point (i, j) on the path from P to P ′, with

14 CHAPTER 2. CHRISTOFFEL MORPHISMS

i > 0. Then (i − 1, j) is also a point on the path. Suppose the point (i, j − 1)

b(i−1, (i−1)b
a )
 b (i, ib
a )

b
(i−1,j)
 b (i,j)

b (i,j−1)

Figure 2.7: The points (i, j) and (i − 1, j) are on a Christoﬀel
path, whereas (i, j − 1) is not.

lies above or on the segment P P ′. Then the vertical distance from (i, j − 1)
to the segment from (0, 0) to (2a, 2b) is at most the vertical distance from
this segment to P , by the choice of P . The former is ib
a − (j − 1) and the
latter is a+b−1
a . That is,
 ib − (j − 1)a
a ≤ a + b − 1
a .

Equivalently, (i−1)b−ja
a ≤ − 1
a . But (i−1)b−ja
a is nonnegative because it is the
distance from the point (i − 1, j) to the segment from (0, 0) to (2a, 2b). This
is a contradiction, so there is no integer point within the region enclosed by
the line segment P P ′ (of slope b
a ) and the path from P to P ′. That is, w′ is
the upper Christoﬀel word of slope b
a .

Theorem 2.8. The morphisms G, D, ̃G, ̃D, E are Christoﬀel morphisms.

Proof. The ﬁrst four morphisms are Christoﬀel morphisms by Corollary 2.5.
It remains to show that E is a Christoﬀel morphism. This follows from
the previous two results: if w is a Christoﬀel word, then E(w) is an upper
Christoﬀel word, which is a conjugate of the corresponding lower Christoﬀel
word.

Exercise 2.1. Prove that if f is an endomorphism of a free monoid A∗ and
w and w′ are conjugate words in A∗, then f (w) and f (w′) are conjugate.

Exercise 2.2. Suppose A is a ﬁnite set. Let ⟨A⟩ denote the free group
generated by A and let A∗ denote the free monoid generated by A. Prove
that any w, w′ ∈ A∗ are conjugate in ⟨A⟩ (in the group-theoretic sense) if
and only if w, w′ are conjugate in A∗ (in the word-theoretic sense).

2.2. GENERATORS 15

Exercise 2.3. Suppose w and w′ are words of the same length. If w′ is a
factor of ww, then w and w′ are conjugate.

Exercise 2.4. Prove that the morphisms G, D, ̃G, ̃D are injective. (Hint:
Study a minimal counterexample, a pair of words u ̸= v with total length
|u| + |v|.)

Exercise 2.5. Complete the proof of Lemma 2.4: For every word w ∈
{x, y}∗, there exists a word v ∈ {x, y}∗ such that D(w) = yv and ̃D(w) = vy.

Exercise 2.6. Recall that the reversal of a word w = a0a1 · · · ar is the word
̃w = ar · · · a1a0. Let w be a word over {x, y}∗. Prove that

̃G(w) = ̃G( ̃w) and ̃D(w) = ̃D( ̃w).

Exercise 2.7. If u ∈ {x, y}∗ is a palindrome, then G(u)x and D(u)y are
palindromes.

Exercise 2.8. (A stronger version of Lemma 2.4) If w ∈ {x, y}∗ is a palin-
drome, then there exist palindromes u, v ∈ {x, y}∗ such that G(w) = xu
and ̃G(w) = ux, and D(w) = yv and ̃D(w) = vy.

2.2 Generators

The following theorem gives a manageable characterization of the monoid
of Christoﬀel morphisms. We will see in Section 3.2 that it implies a very
close relationship between the set of Christoﬀel morphisms and the set of
Christoﬀel words. References in the language of Sturmian words and Stur-
mian morphisms include [MS1993], [Lot2002, Chapter 2], [WW1994] and
[BdLR2008].

Theorem 2.9. The monoid of Christoﬀel morphisms is generated by G, D,
̃G, ̃D and E.

In fact, D = E ◦ G ◦ E and ̃G = E ◦ ̃D ◦ E, but it will simplify the proof
to retain these superﬂuous generators. The proof makes frequent use of the
following easy fact, so we separate it as a lemma.

Lemma 2.10. If w is a Christoﬀel word or a conjugate of a Christoﬀel
word, then xx and yy cannot both be factors of w.

16 CHAPTER 2. CHRISTOFFEL MORPHISMS

× ×

No yy if b
a < 1. No xx if b
a > 1.

Figure 2.8: Impossible conﬁgurations in Christoﬀel words.

Proof. Indeed, let w be the Christoﬀel word of slope b
a . Figure 2.8 indicates
a geometric proof of the following statements. If b
a < 1, then w begins with
xx and yy is not a factor of w. In the case b
a > 1, w ends with yy and xx
is not a factor of w. The only nontrivial Christoﬀel word with neither xx
nor yy is C(1, 1) = xy. Since w begins with an x and ends with a y, xx and
yy are not both factors of the square w2. Finally, since every conjugate of
w appears as a factor of w2, the property holds for conjugates of Christoﬀel
words as well.

Proof of Theorem 2.9. In ﬁve steps.

1. A Christoﬀel morphism f is nonerasing, that is, the length of f (w) is
at least the length of w.
An erasing morphism f must necessarily send x or y to the empty word.
In the ﬁrst case, f (xyy) is not primitive, in the second f (xxy) is not prim-
itive. On the other hand, all conjugates of a Christoﬀel word are primitive
(Exercise 1.1).

2. If f is a nonidentity Christoﬀel morphism, then f (x) and f (y) must begin
or end by the same letter.
Assume f (x) begins by x (study E ◦ f otherwise) and f (y) begins by y.
There are two possibilities:
(i): Suppose f (x) ends by y. Either f (y) ends by x or we are done. In
the remaining case, f (xy) = f (x)f (y) becomes x · · · yy · · · x, so xx and yy
are both factors of every conjugate of f (xy), save perhaps for f (y)f (x) =
y · · · xx · · · y. On the other hand, f (xy) is a conjugate of a Christoﬀel word
u that is not equal to f (x)f (y) or f (y)f (x) since u begins by x and ends by
y. Lemma 2.10 yields a contradiction.

(ii): Suppose instead f (x) ends by x and f (y) ends by y. Note that in
this case, xx is a factor of f (xxy) = f (x)f (x)f (y) = (x · · · x)(x · · · x)(y · · · y).
Hence, yy is not a factor of f (xxy) by the lemma. In particular, yy is a factor
of neither f (x) nor f (y). Similarly, by considering f (xyy), we see that xx

2.2. GENERATORS 17

is a factor of neither f (x) nor f (y). This in turn forces f (x) = (xy)ix,
f (y) = y(xy)j and f (xy) = (xy)i+j+1. Whence i + j = 0 (Exercise 1.1).
Then f is the identity morphism, contrary to our hypothesis.

3. If f is a nonidentity Christoﬀel morphism, then there exists a morphism
g : {x, y}∗ → {x, y}∗ and an H ∈ {G, D, ̃G, ̃D} such that f = H ◦ g.
A nonempty word w on {x, y} belongs to {x, xy}∗ (i.e., is a word on
the “letters” x and xy) if and only if w begins by x and does not contain
the factor yy. Similar descriptions hold for words in {y, xy}∗, {x, yx}∗ and
{xy, y}∗. We argue that the image of f belongs to one of these monoids.
Since G, D, ̃G and ̃D are injective morphisms (Exercise 2.4), with images
in the respective monoids above, this will allow us to compose f with G−1,
D−1, ̃G−1 or ̃D−1, respectively to ﬁnd g.
Since f (xy) is a conjugate of a Christoﬀel word, xx and yy are not both
factors of f (xy). Assuming yy is not a factor of f (xy), it follows that yy is
a factor of neither f (x) nor f (y). By Step 2, f (x) and f (y) must then begin
or end by the same letter, setting up several cases to check.
(i): If f (x) and f (y) both begin by x, then the image of f is a subset of
{x, xy}∗. Therefore, G−1 ◦ f = g is also a morphism of {x, y}∗.

(ii): If f (x) and f (y) both begin by y, then neither may end by y (on
account of the lemma and our assumption that yy is not a
factor of f (xy)). Thus f (x) and f (y) both end by x and neither contain yy
as a factor. That is,
f (x), f (y) ∈ {x, yx}∗ and ̃G−1 ◦ f is a morphism of {x, y}∗.

(iii): The cases where f (x) and f (y) end by the same letter are handled
analogous to the cases above.

4. In the composition f = H ◦ g built above, g is a Christoﬀel morphism.
We now have that f = H ◦ g, with H ∈ {G, D, ̃G, ̃D}, and that f sends
Christoﬀel words onto conjugates of Christoﬀel words. We aim to show that
g does as well. We analyze the case H = G, the rest being similar.
First, recall that if G(w) is a Christoﬀel word, then w is a Christoﬀel
word too (Corollary 2.3). We must show that if G(w) is a conjugate of a
Christoﬀel word then w is as well. This is now easy, for if G(w) = uv with
vu a Christoﬀel word, then v begins by x and u ends by y. Moreover, by
the deﬁnition of G, u must begin by x and yy is a factor of neither u, v nor
uv. This implies that u, v ∈ {x, xy}∗, so G−1(u) and G−1(v) are deﬁned,
w = G−1(u) G−1(v) and G−1(v) G−1(u) is a Christoﬀel word.

5. There exist Hi ∈ {G, D, ̃G, ̃D} such that f = H1 ◦ · · · ◦ Hs.

18 CHAPTER 2. CHRISTOFFEL MORPHISMS

From Step 4, f = H1 ◦ g for some Christoﬀel morphism g and some
H1 ∈ {G, D, ̃G, ̃D}. Moreover, |f (x)|+ |f (y)| > |g(x)|+ |g(y)|. An induction
on |f (x)| + |f (y)| completes the proof.

Remark. We have proved something a priori stronger.

Corollary 2.11 (Berth´e, de Luca, Reutenauer [BdLR2008]). A morphism
f on {x, y}∗ is a Christoﬀel morphism if and only if f (xy), f (xxy) and
f (xyy) are conjugates of Christoﬀel words.

Chapter 3

Standard Factorization

The ﬁrst section of this chapter proves that every Christoﬀel word can be
expressed as the product of two Christoﬀel words in a unique way, and
the second section builds an inﬁnite, complete binary tree whose vertices
correspond to Christoﬀel words via this unique factorization.

3.1 The standard factorization

This section proves that every Christoﬀel word can be expressed as the
product of two Christoﬀel words in a unique way. This factorization is called
the standard factorization and was introduced by Jean-Pierre Borel and
Fran¸cois Laubie [BL1993]. Most of the results in this section are due to
them.
Given that a ⊥ b, recall the method of labelling the Christoﬀel path from
(0, 0) to (a, b) for nontrivial Christoﬀel words. By Lemma 1.3, if a and b are
nonzero, then there is a unique point C on this path having label 1
a . We call
C the closest point for the path. It is the lattice point on the Christoﬀel
path from (0, 0) to (a, b) with minimum nonzero distance to the line segment
from (0, 0) to (a, b).

Deﬁnition 3.1. Suppose a ⊥ b with a, b > 0. The standard factorization
of the Christoﬀel word w of slope b
a is the factorization w = (w1, w2), where
w1 encodes the portion of the Christoﬀel path from (0, 0) to the closest point
C and w2 encodes the portion from C to (a, b).

Example. The standard factorization of the Christoﬀel word of slope 4
7 is
(xxy, xxyxxyxy). See Figure 3.1.
 19

20 CHAPTER 3. STANDARD FACTORIZATION

b

x x
 x x
 x x
 x

y
 y
 y
 y

Figure 3.1: The closest point for the Christoﬀel path of slope
4
7 occurs between the third and fourth steps, thus the standard
factorization of xxyxxyxxyxy is (xxy, xxyxxyxy).

Proposition 3.2. If (w1, w2) is the standard factorization of a nontrivial
Christoﬀel word, then w1 and w2 are Christoﬀel words.

Proof. Suppose w is a Christoﬀel word of slope b
a and let (i, j) be the point
on the Christoﬀel path from (0, 0) to (a, b) labelled 1
a . Then w1 encodes the
subpath P1 from (0, 0) to (i, j) and w2 encodes the subpath P2 from (i, j)
to (a, b). See Figure 3.2.
Since (i, j) is the point on the Christoﬀel path that is closest to the line
segment from (0, 0) to (a, b) without being on the segment, no point of the
Christoﬀel path besides (0, 0), (a, b) and (i, j) lies in the triangle determined
by these three points. See Figure 3.2. Let S1 be the line segment from (0, 0)
to (i, j). Note that the region bounded by P1 and S1 contains no interior
lattice points. Since, moreover, no integer points lie in the interior of the

b
(i, j)
 P1
 P2

Figure 3.2: The standard factorization of a Christoﬀel word gives
two Christoﬀel words.

line segment S1, it follows that i ⊥ j (Exercise 1.2) and w1 is the Christoﬀel
word of slope j
i . Similarly, w2 is the Christoﬀel word of slope b−j
a−i .

In fact, the standard factorization is the only factorization of a Christoﬀel
word with this property.

3.1. THE STANDARD FACTORIZATION 21

Theorem 3.3 (Borel, Laubie [BL1993]). A nontrivial Christoﬀel word w
has a unique factorization w = (w1, w2) with w1 and w2 Christoﬀel words.

We present a proof suggested by Hugh Thomas.

Proof. Let (w1, w2) denote the standard factorization of w. Recall that this
factorization is obtained from cutting the Christoﬀel path at its closest point
C. Suppose there is another factorization w = (u, v) with u and v Christoﬀel

b C

h
 b C′
h′

u
 v

No interior lattice points for

the region ∪ .

A
 B

Figure 3.3: A Christoﬀel factorization w = uv at cutpoint C′.

words. See Figure 3.3. That is, C ′ = (c, d) is another point on the path
having no integer points in its corresponding regions (shaded in Figure 3.3)
and satisfying c ⊥ d. We reach a contradiction by comparing triangles ABC
and ABC ′ in Figure 3.3. Since w1, w2 are Christoﬀel words, we know there
are no integer lattice points in the interior of triangle ABC. Moreover, the
only lattice points on its boundary occur at A, B and C. By Pick’s Theorem
(Exercise 3.1), we have

area ABC = i + 1
2 b − 1 = 0 + 3
2 − 1 = 1
2 ,

where i is the number of lattice points interior to ABC and b is the number
of lattice points on its boundary. The same may be said for triangle ABC ′:
since u, v are Christoﬀel words, the line segments AC ′ and BC ′ do not cross
the Christoﬀel path for w; since w is a Christoﬀel word, this implies there are
no interior lattice points in ABC ′; there are only 3 boundary lattice points
by the same reasoning. Now we have two triangles with the same base, the
same area, but diﬀerent heights. Contradiction.

Finally, we record some additional facts about the factorization (w1, w2)
that will be useful in what follows. Recall that SL2(Z) is the group of in-
vertible matrices with integer entries and determinant equal to 1.

22 CHAPTER 3. STANDARD FACTORIZATION

Lemma 3.4. Suppose (w1, w2) is the standard factorization of the Christof-
fel word w of slope b
a , where a ⊥ b. Then
(|w1|x |w2|x
|w1|y |w2|y
) ∈ SL2(Z).

Proof. The point (i, j) of the Christoﬀel path labelled 1
a is (|w1|x, |w1|y).
Also, (a − i, b − j) = (|w2|x, |w2|y). Since exactly three integer points lie in
the triangle with vertices (0, 0) (i, j), (a, b), it follows from Pick’s Theorem
(see Exercises 3.1 and 3.2) that

det ( i j
a − i b − j
) = 1.

Therefore, the matrix is an element of SL2(Z).

Lemma 3.5. Let w denote the Christoﬀel word of slope b
a and let (w1, w2)
denote its standard factorization. Then |w1|b ≡ 1 mod (a+b) and |w2|a ≡ 1
mod (a + b). Moreover, |w1| and |w2| are relatively prime.

Proof. By Exercise 1.6, the point (i, j) on the Christoﬀel path from (0, 0) to
(a, b) has label t
a , where t satisﬁes

t ≡ (i + j)b mod (a + b),

t ≡ ((a − i) + (b − j)
)a mod (a + b)

(recall that |w|x = a and |w|y = b). Since (|w1|x, |w1|y) is the closest point
of the Christoﬀel path to the line segment from (0, 0) to (a, b), it has label
1
a . Applying the above to t = 1 and the point (i, j) = (|w1|x, |w1|y), we have
|w1|b ≡ 1 mod (a + b) and |w2|a ≡ 1 mod (a + b).
It remains to show that |w1| and |w2| are relatively prime. By Corollary
3.4, (|w1|x |w2|x
|w1|y |w2|y
) ∈ SL2(Z).

This implies that

det (|w1| |w2|
|w1|y |w2|y
) = det (|w1|x |w2|x
|w1|y |w2|y
) = 1.

That is, there exist integers k and l such that |w1|k+|w2|l = 1, which implies
|w1| ⊥ |w2| (see B´ezout’s Lemma in Exercise 3.3).

3.2. THE CHRISTOFFEL TREE 23

Exercise 3.1 (Pick’s Theorem). Let P be a simple polygon (that is, the
boundary of P has no self-intersections) with vertices in Z × Z. Then the
area of P is i + 1
2 b − 1, where i is the number of integer points in the interior
of P and b is the number of integer points of the boundary of P . (Hint:
Proceed by induction on the number of vertices of P .)

Exercise 3.2. Suppose i, j, k, l are positive integers. If no other integer
points lie in the triangle with vertices (0, 0), (i, j), (i + k, j + l), then

det (i j
k l
) = 1.

(Hint: Use Pick’s Theorem above and the fact that the determinant is twice
the area of the triangle.)

Exercise 3.3 (B´ezout’s Lemma). Let a and b be positive integers. If the
greatest common divisor of a and b is d, then there exist integers i and j
such that ia + jb = d. Moreover, a ⊥ b if and only if there exist integers i
and j such that ia + jb = 1.

3.2 The Christoﬀel tree

We close this chapter with a description of the Christoﬀel tree, following
[BL1993] and [BdL1997]. This is the inﬁnite, complete binary tree whose
root is labelled (x, y) and whose vertices are labelled by pairs (u, v) of words
in {x, y}∗ subject to the following branching rules.

(u, v)

(u, uv)

◦G
 (uv, v)

◦ ̃D

View the vertex (u, v) above as a morphism (x, y) f
↦→ (u, v). We have labelled
the edges to indicate that f = (u, v) has two branches, f ◦ G and f ◦ ̃D.
These rules were introduced by Gerard Rauzy in [Rau1984]. The ﬁrst few
levels of the Christoﬀel tree appear in Figure 3.4.

Theorem 3.6. The Christoﬀel tree contains exactly once the standard fac-
torization of each (lower) Christoﬀel word.

Example. Recall that (xxy, xxyxxyxy) is the standard factorization of the
Christoﬀel word of slope 4
7 (see Figure 3.1). It appears in Figure 3.4 at the
ﬁfth level as (G ◦ ̃D ◦ G ◦ G)(x, y).

24 CHAPTER 3. STANDARD FACTORIZATION

(x, y)

(x, xy)

(x, xxy)

(x, x3y) (x3y, x2y)
 (xxy, xy)

(x2y, x2yxy)

(x2y, x2yx2yxy) (x2yx2yxy, x2yxy)

(x2yxy, xy)
 (xy, y)

(xy, xyy)

(xy, xyxy2) (xyxy2, xy2)
 (xyy, y)

(xy2, xy3) (xy3, y)

Figure 3.4: The Christoﬀel tree.

Proof of Theorem 3.6. In three steps.

1. Each vertex (u, v) on the tree has the property that u, v and uv are
Christoﬀel words.

We have seen that G and ̃D send Christoﬀel words to Christoﬀel words.
Since each f = (u, v) on the tree corresponds to a composition of Gs and ̃Ds,
we get immediately that u = f (x), v = f (y) and uv = f (xy) are Christoﬀel
words.

2. A vertex (u, v) on the Christoﬀel tree is the standard factorization of the
Christoﬀel word uv.
By Step 1, u, v and uv are Christoﬀel words. By Theorem 3.3, the only
way to factor uv as Christoﬀel words is the standard factorization (u, v).

3. The standard factorization (w1, w2) of a Christoﬀel word w appears ex-
actly once in the Christoﬀel tree.

We demonstrate how to write

(w1, w2) = (H1 ◦ H2 ◦ · · · ◦ Hr) (x, y)

for some r ∈ N and Hi ∈ {G, ̃D}, thereby explicitly describing a path in
the Christoﬀel tree from the root to the vertex (w1, w2). The argument is
illustrated in the example following this proof. We need only argue that
standard factorizations may be lifted via G or ̃D. Speciﬁcally, we apply
G−1 if w1w2 has slope less than 1 and ̃D−1 if w1w2 has slope greater than 1

3.2. THE CHRISTOFFEL TREE 25

(see Corollary 2.3). An example where the slope is less than 1 is illustrated
in Figure 3.5.
 b C
 x ←[ x
xy ←[ y
−−−−−→
 b G−1C

Figure 3.5: C is the closest point for the Christoﬀel path of
G(xxyxxyxy) = xxxyxxxyxxy and G−1(C) is the closest point
for the Christoﬀel path of the word xxyxxyxy. (Here G is the lin-
ear transformation (⃗e1, ⃗e2) ↦→ (⃗e1 + ⃗e2, ⃗e2) mimicing G.)

The ﬁgure suggests that the closest point does not change under a change
of basis. More precisely, we claim that if (u, v) is the standard factorization
of the Christoﬀel word uv of slope less than 1, then (G−1(u), G−1(v)) is
the standard factorization of G−1(uv). First, since yy is not a factor of uv
(see the proof of Lemma 2.10), yy is not a factor of u or v. Hence, u and v
are in the image of G. Moreover, u and v are Christoﬀel words, so G−1(u)
and G−1(v) are as well (Corollary 2.3). This is the standard factorization of
G−1(uv) by Theorem 3.3. The same argument works for ̃D.
Finally, the fact that (w1, w2) can occur at most once in the Christoﬀel
tree comes from the following property of binary trees. Each vertex describes
a unique path back to the root, a ﬁnite sequence of statements of the form,
“I was a left branch” or “I was a right branch.” Since being a left branch
corresponds to precomposition by G and being a right branch corresponds
to precomposition by ̃D, if (w1, w2) appears at two distinct vertices of the
graph, then we have two expressions of the form

(w1, w2) = (H1 ◦ H2 ◦ · · · ◦ Hr) (x, y)

(w1, w2) = (
H′
1 ◦ H
′
2 ◦ · · · ◦ H
′
s) (x, y)

for some r, s ∈ N and Hi, H′
i ∈ {G, ̃D}. Since the only Christoﬀel word in
the image of both G and ̃D is xy (corresponding to the root of the tree), it
follows that H1 = H′
1, H2 = H′
2, . . . , Hr = H′
s. Therefore, both vertices of
the graph describe the same (unique) path back to the root, contradicting
the assumption that the two vertices are distinct.

Example. We illustrate the ideas of Step 3 of the proof in Figure 3.6, march-
ing upwards from the vertex (xxxy, xxxyxxy) to the root (x, y).

26 CHAPTER 3. STANDARD FACTORIZATION

some Christoﬀel words w . . . and their standard factorizations

xy

xxy
 xyxyy

xxyxxyxy

xxxyxxxyxxy
 slope < 1, apply G−1

slope > 1 (ends with yy),
apply eD−1
 slope < 1, apply G−1

slope < 1 (starts with xx),
apply G−1
 (x , y)

(x , xy)

(xy , xyy)

(xxy , xxyxy)

(xxxy , xxxyxxy)

Figure 3.6: Paths in the Christoﬀel tree from (u, v) to the root
(x, y) preserve the cutting points for standard factorizations.

Note that we have found a characterization of those Christoﬀel mor-
phisms that preserve Christoﬀel words. Namely, f : (x, y) ↦→ (w1, w2) is
such a morphism if and only if (w1, w2) is a standard factorization of a
Christoﬀel word.

Exercise 3.4. Let f be a Christoﬀel morphism. Prove that f takes Christof-
fel words to Christoﬀel words if and only if f = (w1, w2), where (w1, w2) is
the standard factorization of some Christoﬀel word. (Hint: One direction is
Theorem 3.3. For the other direction, use the Christoﬀel tree to show that
f is a composition of Gs and ̃Ds.)

Chapter 4

Palindromization

Recall that a word u is a palindrome if it is equal to its own reversal
(u = ̃u). This chapter begins with the observation that if w is a nontrivial
Christoﬀel word, then w = xuy with u a (possibly empty) palindrome.
It continues by investigating the set of palindromes u for which xuy is a
Christoﬀel word.

4.1 Christoﬀel words and palindromes

We prove that every nontrivial (lower) Christoﬀel word can be expressed
as xuy with u a palindrome, and that the corresponding upper Christoﬀel
word is yux.

Lemma 4.1. Suppose a ⊥ b. Translation by the vector ⃗e2 − ⃗e1 and rotation
about the point ( a
2 , b
2 ) each map the interior points of the lower Christoﬀel
path from (0, 0) to (a, b) onto the interior points of the upper Christoﬀel path
from (0, 0) to (a, b).

Proof. Translation: Let Q be a point diﬀerent from (0, 0) and (a, b) on the
lower Christoﬀel path from (0, 0) to (a, b). Then the translated point Q +
(⃗e2 − ⃗e1) is an integer point lying above the lower Christoﬀel path, and so
it lies above the segment from (0, 0) to (a, b). Since there is no path in the
integer lattice consisting of steps ⃗e1 and ⃗e2 that avoids Q and Q + (⃗e2 − ⃗e1),
and that has Q and Q + (⃗e2 − ⃗e1) on opposite sides of the path, it follows
that Q + (⃗e2 − ⃗e1) lies on the upper Christoﬀel path from (0, 0) to (a, b).

Rotation: Since there are no lattice points enclosed by the (upper or
lower) Christoﬀel path and the segment from (0, 0) to (a, b), a half-turn

27

28 CHAPTER 4. PALINDROMIZATION

P

P ′

Figure 4.1: Translation by ⃗e2 − ⃗e1 maps P onto P ′; rotation
about ( 7
2 , 2) maps P onto the reverse of P ′.

about the midpoint of the line segment from (0, 0) to (a, b) maps the lower
Christoﬀel path to the upper Christoﬀel path.

The following result is the consequence of the above geometric lemma.
(Recall that a Christoﬀel word is nontrivial if its length is at least two.)

Proposition 4.2. Suppose a ⊥ b. If w is a nontrivial lower Christoﬀel word
of slope b
a , then w = xuy with u a palindrome. If w′ is the upper Christoﬀel
word of slope b
a , then w′ = yux. In particular, w′ = ̃w.

Proof. Let w and w′ be the nontrivial lower and upper Christoﬀel words of
slope b
a , respectively. By construction any lower Christoﬀel word begins by
x and ends by y, so w = xuy for some u ∈ {x, y}∗. Similarly, w′ = yu′x for
some u′ ∈ {x, y}∗. The words u and u′ correspond to the subpaths P and
P ′ obtained from the lower and upper Christoﬀel paths from (0, 0) to (a, b),
respectively, by removing the endpoints. By Lemma 4.1, P is a translate of
P ′, so u = u′. Also by Lemma 4.1, a half-turn rotation maps P ′ onto P .
Since rotation reverses the direction of P ′, it follows that u = ̃u′ = ̃u. So u
is a palindrome. Finally, w′ = yu′x = yux = ỹux = ̃w.

4.2 Palindromic closures

We next determine those palindromes u for which xuy is a Christoﬀel word,
following the work of Aldo de Luca [dL1997] and others. A function Pal that
maps words to palindromes is deﬁned and it will be shown that x Pal(v)y
is a Christoﬀel word for every v ∈ {x, y}∗. It will be useful to have the
terminology palindromic preﬁx and palindromic suﬃx, that is, a preﬁx
(respectively, suﬃx) u of a word w such that u is a palindrome.

4.2. PALINDROMIC CLOSURES 29

Proposition 4.3 (de Luca [dL1997]). Let w be a word. Write w = uv,
where v is the longest suﬃx of w that is a palindrome. Then w+ = w̃u is
the unique shortest palindrome having w as a preﬁx.

Proof. The proof is left as an exercise (Exercise 4.5).

Deﬁnition 4.4. Let w be a word. The word w+ constructed in Proposition
4.3 is called the (right) palindromic closure of w.

Example. Let w = yxyxxy. The longest palindromic suﬃx of w is v =
yxxy. Putting u = yx, we have w+ = w̃u = yxyxxyxy and w+ is indeed a
palindrome.

Deﬁnition 4.5 (de Luca [dL1997]). Deﬁne a function Pal : {x, y}∗ →
{x, y}∗ recursively as follows. For the empty word ǫ, let Pal(ǫ) = ǫ. If
w = vz ∈ {x, y}∗ for some z ∈ {x, y}, then let

Pal(w) = Pal(vz) = (Pal(v)z)
+.

The word Pal(w) is called the iterated palindromic closure of w.

Example. We compute Pal(xyxx).

Pal(x) = (Pal(ǫ)x)
+ = x+ = x.

Pal(xy) = (Pal(x)y)
+ = (xy)
+ = xyx.

Pal(xyx) = (Pal(xy)x)
+ = ((xyx)x)
+ = xyxxyx.

Pal(xyxx) = (Pal(xyx)x)
+ = ((xyxxyx)x)
+ = xyxxyxxyx.

Note that the Christoﬀel word of slope 4
7 is xxyxxyxxyxy = x Pal(xyxx)y.

The map w ↦→ Pal(w) is injective. A complete proof is outlined in the
exercises (Exercise 4.9). Brieﬂy, the inverse map is obtained by taking the
ﬁrst letter after each palindromic preﬁx of Pal(w) (excluding Pal(w), but
including the empty preﬁx ǫ). The fact that this procedure works follows
from the observation that the only palindromic preﬁxes of Pal(w) are those
obtained during the iterated construction of Pal(w).

Example. Suppose Pal(w) = xyxxyxxyx. The palindromic preﬁxes of Pal(w)
excluding Pal(w) are: ǫ; x; xyx; and xyxxyx. The ﬁrst letter after these pre-
ﬁxes are: x; y; x; x. Therefore, w = xyxx. This agrees with the computation
of Pal(xyxx) in the previous example. Moreover, from that computation we
note that the words Pal(ǫ), Pal(x), Pal(xy), Pal(xyx) and Pal(xyxx) are
palindromic preﬁxes of Pal(xyxx), and that they are the only palindromic
preﬁxes of Pal(xyxx). See Exercise 4.8.

30 CHAPTER 4. PALINDROMIZATION

The remainder of this section is devoted to proving a result that implies,
among other things, that xuy is a Christoﬀel word if u is in the image of Pal.
Before stating the full result we recall the deﬁnition of a period of a word.
A positive integer p is a period of w if wi = wi+p for all 1 ≤ i ≤ |w| − p,
where wi denotes the i-th letter of the word w. (Again, we allow p ≥ |w|.)

Theorem 4.6 (Borel, Laubie [BL1993], de Luca [dL1997], Berth´e, de Luca,
Reutenauer [BdLR2008]). Let v ∈ {x, y}∗. Then w = x Pal(v)y is a Christof-
fel word. If (w1, w2) is the standard factorization of w, then

µ(v) = (|w1|x |w2|x
|w1|y |w2|y
) ∈ SL2(Z),

where µ : {x, y}∗ → SL2(Z) is the multiplicative monoid morphism deﬁned
by
 µ(x) = (1 1
0 1

) and µ(y) = (1 0
1 1

) ,

and Pal(v) has relatively prime periods |w1| and |w2|.

Remark. We provide a converse to this result in Proposition 4.14, namely,
if w is a Christoﬀel word then w = x Pal(v)y for some v ∈ {x, y}∗.

Example. Let w = xxyxxyxxyxy denote the Christoﬀel word of slope 4
7 .
Note that xyxxyxxyx has periods 3 and 8. In previous examples we saw that
w = x Pal(xyxx)y and that the standard factorization of w is (w1, w2) =
(xxy, xxyxxyxy). Therefore,

µ(xyxx) = (1 1
0 1
) (1 0
1 1
) (1 1
0 1
) (1 1
0 1

) = (2 5
1 3

) = (|w1|x |w2|x
|w1|y |w2|y
) .

The proof is divided into three propositions. We begin by proving that
x Pal(v)y is a Christoﬀel word.
The following formulae of Jacques Justin give a very useful method for
computing Pal(v).

Lemma 4.7 (Justin [Jus2005]). For any word w ∈ {x, y}∗,

Pal(xw) = G
( Pal(w)x) = G
( Pal(w)
)x,

Pal(yw) = D
( Pal(w)y) = D
( Pal(w)
)y. (4.8)

4.2. PALINDROMIC CLOSURES 31

A proof of this result is outlined in Exercise 4.11.

Example. We compute Pal(xyxx) using the formulae of Justin.

Pal(xyxx) = G
( Pal(yxx)
)x

= G
(D
( Pal(xx)
)
y)x

= G
(D(xx)y)x

= G
(yxyxy)
x

= xyxxyxxyx.

Proposition 4.9. Suppose v ∈ {x, y}∗. Then w = x Pal(v)y is a Christoﬀel
word.

Proof. Proceed by induction on |v|. Suppose the length of v is zero. Then
Pal(v) = ǫ and w = xy, which is a Christoﬀel word. Suppose that x Pal(v)y
is a Christoﬀel word for all words v of length at most r and let v′ ∈ {x, y}∗

be a word of length r + 1. If v′ begins with x, then write v′ = xv for some
v ∈ {x, y}∗. Then, by the formulae of Justin,

x Pal(v′)y = x Pal(xv)y = xG(Pal(v)x)y = G(x Pal(v)y).

This is a Christoﬀel word because x Pal(v)y is a Christoﬀel word (by the
induction hypothesis) and because G maps Christoﬀel words to Christoﬀel
words (Lemma 2.2).
If v′ = yv, then

x Pal(v′)y = x Pal(yv)y = xD(Pal(v)y)y.

Lemma 2.4 implies there exists a word u such that ̃D(Pal(v)y) = uy and
D(Pal(v)y) = yu. The ﬁrst equality together with ̃D(y) = y implies that
u = ̃D(Pal(v)). Therefore, D(Pal(v)y) = y ̃D(Pal(v)). Hence,

x Pal(v′)y = xD(Pal(v)y)y = xy ̃D(Pal(v))y = ̃D(x Pal(v)y).

This is a Christoﬀel word because x Pal(v)y is a Christoﬀel word (by the
induction hypothesis) and because ̃D maps Christoﬀel words to Christoﬀel
words (Lemma 2.2).

We next prove that the entries of the matrix µ(v) are given by the
numbers of occurrences of the letters x and y in the words w1 and w2, where
(w1, w2) is the standard factorization of the Christoﬀel word x Pal(v)y.

32 CHAPTER 4. PALINDROMIZATION

Proposition 4.10. Suppose v ∈ {x, y}∗. If (w1, w2) is the standard factor-
ization of the Christoﬀel word x Pal(v)y, then

µ(v) = (|w1|x |w2|x
|w1|y |w2|y
) .

Proof. We proceed by induction on the length of v. If |v| = 0, then v = ǫ. So
the Christoﬀel word x Pal(ǫ)y is xy and its standard factorization is (x, y).
Therefore,
 µ(ǫ) = (1 0
0 1
) = (|x|x |y|x
|x|y |y|y
) .

This establishes the base case of the induction. Suppose the result holds for
all words v of length at most r − 1 ≥ 0 and let v′ be a word of length r.
If v′ begins with x, then v′ = xv for some v ∈ {x, y}∗. By the induction
hypothesis,

µ(v′) = µ(x)µ(v) = (1 1
0 1

) (|w1|x |w2|x
|w1|y |w2|y
) = (|w1| |w2|
|w1|y |w2|y
) ,

where (w1, w2) is the standard factorization of x Pal(v)y. Writing (w′
1, w′
2)
for the standard factorization of the Christoﬀel word x Pal(v′)y, we would
like to show that (
|w1| |w2|
|w1|y |w2|y
) = (
|w′
1|x |w′
2|x
|w′
1|y |w′
2|y
) .

In view of Lemma 3.4 and Exercise 4.3, it suﬃces to show that |w′
1|x +
|w′
2|x = |w1| + |w2| and |w′
1|y + |w′
2|y = |w1|y + |w2|y. Equivalently, we need
to show that |x Pal(v′)y|x = |x Pal(v)y| and |x Pal(v′)y|y = |x Pal(v)y|y. By
the formulae of Justin (4.8),

x Pal(v′)y = x Pal(xv)y = xG(Pal(v))xy = G(x Pal(v)y).

Since G = (x, xy) replaces each letter of a word m ∈ {x, y}∗ with a word
having exactly one occurrence of x, the number of occurrences of the letter
x in G(m) is the length of m. Therefore,

|x Pal(v′)y|x = |G(x Pal(v)y)|x = |x Pal(v)y|.

Since G = (x, xy) ﬁxes the letter x and replaces y with a word having exactly
one occurrence of y, we have |G(m)|y = |m|y for any word m ∈ {x, y}∗.
Therefore,
 |x Pal(v′)y|y = |G(x Pal(v)y)|y = |x Pal(v)y|y.

4.2. PALINDROMIC CLOSURES 33

This completes the induction for words beginning with the letter x.
If, instead, v′ begins with the letter y, then v′ = yv for some v ∈ {x, y}∗,
and
 µ(v′) = µ(y)µ(v) = (
1 0
1 1

) (|w1|x |w2|x
|w1|y |w2|y
) = (|w1|x |w2|x
|w1| |w2|
 ) ,

where (w1, w2) is the standard factorization of x Pal(v)y. As above, we need
only show that |x Pal(v′)y|y = |x Pal(v)y| and |x Pal(v′)y|x = |x Pal(v)y|x.
By the formulae of Justin (4.8), x Pal(v′)y = x Pal(yv)y = xD(Pal(v))yy.
Since D = (yx, y), it follows that |D(m)|y = |m| and |D(m)|x = |m|x for
any word m ∈ {x, y}∗, so

|x Pal(v′)y|y = |xD(Pal(v))yy|y = | Pal(v)yy| = |x Pal(v)y|,

|x Pal(v′)y|x = |xD(Pal(v))yy|x = |x Pal(v)|x = |x Pal(v)y|x.

This completes the induction.

We now turn to the computation of periods of the word Pal(v). The
treatment here is based on the paper [BR2006] of Borel and Reutenauer.
The following result determines a period of palindromes having palindromic
preﬁxes.

Lemma 4.11 (de Luca [dL1997]). If a palindrome u has a palindromic preﬁx
p ̸= u, then u has a period |u| − |p|.

Proof. Write u = pv for some word v. Then u = ̃vp because u and p are
palindromes. Since u = pv, we have ui = pi for 0 ≤ i < |p|. And since u = ̃vp,
we have ui+|v| = pi for 0 ≤ i < |p|. Therefore, ui = ui+|v| for 0 ≤ i < |p|.
That is, u has period |v| = |u| − |p|.

Proposition 4.12. Suppose v ∈ {x, y}∗. The word Pal(v) has periods |w1|
and |w2|, where (w1, w2) is the standard factorization of the Christoﬀel
word x Pal(v)y. Moreover, the periods |w1| and |w2| are relatively prime and
| Pal(v)| = |w1| + |w2| − 2.

Proof. Let (w1, w2) denote the standard factorization of x Pal(v)y. Then w1
and w2 are Christoﬀel words by Proposition 3.2. There are two cases to
consider.
Case 1: w1 or w2 is a trivial Christoﬀel word. If w1 = x, then

µ(v) = (1 |w2|x
0 |w2|y
) .

34 CHAPTER 4. PALINDROMIZATION

Since det(µ(v)) = 1, it follows that |w2|y = 1. So w2 = xey for some e ∈ N.
Hence, Pal(v) = xe, which has periods |w1| = 1 and |w2| = e + 1, and length
|w1| + |w2| = 1 + (e + 1) − 2 = e. The same argument holds if w2 = y.
Case 2: w1 and w2 are nontrivial Christoﬀel words. By Proposition 4.2,
there exist palindromes u1 and u2 such that w1 = xu1y and w2 = xu2y.
Therefore, Pal(v) = u1xyu2. The previous lemma implies that Pal(v) has
periods | Pal(v)| − |u1| = |u2| + 2 = |w2| and | Pal(v)| − |u2| = |u1| + 2 = |w1|.
The fact that |w1| and |w2| are relatively prime follows from Lemma 3.5.

Exercise 4.1. Given any endomorphism f of the monoid {x, y}∗ and any
word w ∈ {x, y}∗, one has
(|f (w)|x
|f (w)|y
 ) = (|f (x)|x |f (y)|x
|f (x)|y |f (y)|y
) (|w|x
|w|y
 ) .

Exercise 4.2. Show that the monoid SL2(Z) ∩ N2×2 is generated by
(1 1
0 1

) and (1 0
1 1

),

which are the images of x and y under the morphism µ of Theorem 4.6.

Exercise 4.3 ([Ran1973, BdL1997]). Two matrices

M = (a b
c d
) and M ′ = (a′ b′

c′ d′
) in N2×2 ∩ SL2(Z)

satisfy a + b = a′ + b′ and c + d = c′ + d′ if and only if M = M ′.

Exercise 4.4. If w ∈ {x, y}∗, then E(Pal(w)) = Pal(E(w)). (Hint: First
establish that (E(w))+ = E(w+).)

Exercise 4.5. Prove Proposition 4.3. (Hint: Show that w+ = wv−1 ̃w, where
the product on the left is evaluated in the free group generated by x and y.)

Exercise 4.6. If p ̸= w+ is a palindromic preﬁx of w+, then p is a (palin-
dromic) preﬁx of w.

Exercise 4.7. Given two letters x and y and an integer s > 0, prove that:

(a) Pal(xys) = (xy)sx;

(b) Pal(xsy) = Pal(xs)y Pal(xs) = xsyxs;

(c) Pal(xysx) = Pal(xys) Pal(xys).

4.2. PALINDROMIC CLOSURES 35

Exercise 4.8. Let w be a word and z ∈ {x, y}.

(a) If u is a preﬁx of w, then Pal(u) is a preﬁx of Pal(w).

(b) uz is a preﬁx of w if and only if Pal(u)z is a preﬁx of Pal(w).

(c) If p is a palindromic preﬁx of Pal(w), then p = Pal(u) for some preﬁx
u of w.

(Hint: Proceed by induction on the length of w and use Exercise 4.6.)

Exercise 4.9 (Pal is injective.). If ǫ = p1, p2, . . . , pr denote the sequence
of palindromic preﬁxes of Pal(w) diﬀerent than Pal(w) listed in order of in-
creasing length, and if z1, z2, . . . , zr ∈ {x, y} denote the letters in Pal(w) im-
mediately following the preﬁxes p1, p2, . . . , pr in Pal(w), then w = z1z2 · · · zr.
(Hint: Use Exercise 4.8.)

Exercise 4.10. If w = vzu, where u does not have an occurrence of the
letter z, then
 Pal(wz) = Pal(w) Pal(v)
−1 Pal(w),

where the product is evaluated in the free group generated by {x, y}. (Hint:
Using Exercise 4.8, establish that the longest palindromic suﬃx of Pal(w)z
is z Pal(v)z.)

Exercise 4.11. (Lemma 4.7) Let αx = G = (x, xy) and αy = D = (yx, y).
Verify the formulae of Justin: show that for any word w ∈ {x, y}∗ and any
z ∈ {x, y},
 Pal(zw) = αz( Pal(w)
)z.

(Hint: Proceed by induction on |w|. Establish the case |w| = 0, then write
w = w′a, where a is the last letter of w and consider the following two cases.

1. If the letter a occurs in w′, then write w′ = vau, where u is a word
that does not have any occurrences of a, and use Exercise 4.10 and the
induction hypothesis.

2. If the letter a does not occur in w′, then show that

αz( Pal(w)
)z =
 {
(Pal(zw′)a)+, if z = a,
(Pal(zw′)a)+, if z ̸= a = Pal(zw′a) = Pal(zw)

using Exercise 4.10, the induction hypothesis and Exercise 4.7.

36 CHAPTER 4. PALINDROMIZATION

This completes the induction.)

Exercise 4.12 (Generalization of Lemma 4.7; see [Jus2005]). Let α denote
the morphism deﬁned for words in {x, y}∗ by α(x) = G = (x, xy) and
α(y) = D = (yx, y). For any words v, w ∈ {x, y}∗,

Pal(vw) = α(v) (Pal(w)) Pal(v).

(Hint: Proceed by induction on |v| and use Exercise 4.11.)

4.3 Palindromic characterization

Here we provide a converse to Theorem 4.6, namely xuy is a Christoﬀel word
only if u = Pal(v) for some v in {x, y}∗. We also give a characterization of
the image of Pal in terms of periods.

Lemma 4.13. Fix an alphabet A and suppose p ⊥ q with p, q > 1. Up to
a permutation of A, there exists a unique word u ∈ A∗ satisfying: u has at
least two distinct letters, |u| = p + q − 2 and u has periods p and q.

Proof. (This proof is illustrated in the example below.) Since |u| = p + q − 2,
write u = u1u2 · · · up+q−2, where uj ∈ A for 1 ≤ j ≤ p + q − 2. We will show
that 1, 2, . . . , p + q − 2 (the positions of the letters u1, u2, . . . , up+q−2 in u)
can be partitioned into two nonempty sets S and T such that ui = uj if and
only if i and j both belong to S or both belong to T .
Since p ⊥ q, it follows that p ⊥ (p + q), and so p generates Z/(p + q)Z.
Let G denote the Cayley graph of Z/(p + q)Z with generator p. Consider
the graph G′ = G − {0, p + q − 1} obtained from G by removing the vertices
0 and p + q − 1. Since G is connected and two vertices have been removed,
G′ has at most two connected components. If there is only one connected
component, then 0 and p + q − 1 are adjacent in G, and so p + q − 1 is
either p mod (p + q) or −p mod (p + q). The former implies that q = 1
and the latter implies that p = 1, contrary to the assumption that p, q > 1.
Therefore, there are exactly two connected components of G′.
Suppose i and j correspond to adjacent vertices in one connected com-
ponent of G′. Then 0 < i, j < p + q − 1 and either j = i + p or j = i − q (since
p ≡ −q mod (p + q)). If j = i + p, then uj = ui+p = ui since u has period
p; and if j = i − q, then uj = ui−q = ui since u has period q. It follows that
ui = uj if i and j are in the vertex set of one connected component of G′.
Therefore, ui = a for all i in the vertex set of one connected component of
G′ and uj = b for all j in the vertex set of the other connected component

4.3. PALINDROMIC CHARACTERIZATION 37

of G′. Since u has at least two distinct letters, we have a ̸= b. Thus, up to a
permutation of the alphabet A, the word u is uniquely deﬁned.

Example. Suppose p = 4 and q = 7. The Cayley graph of Z/(4 + 7)Z
with generator 4 and the graph obtained by removing the vertices 0 and
4 + 7 − 1 = 10 are shown in Figure 4.2. The vertex sets of the two con-
nected components are {1, 2, 4, 5, 6, 8, 9} and {3, 7}. Therefore, the words
xxyxxxyxx and yyxyyyxyy are the only words u of length 4 + 7 − 2 = 9
with periods 4 and 7 that have at least two distinct letters.

0 4
 8

1

5

92

6

10

3
 7 4
 8

1

5

92

6

3
 7

Figure 4.2: The Cayley graph of Z/(4+7)Z with generator 4 and
the connected components obtained by removing 0 and 10 = 4 +
7 − 1.

Remark. From the proof of the lemma, one learns that the word u in question
has exactly two distinct letters. Of course, this is already the case in the
setting of interest to us, namely A = {x, y}.

Proposition 4.14 (de Luca, Mignosi [dLM1994]).

1. u = Pal(v) for some v ∈ {x, y}∗ if and only if xuy is a Christoﬀel
word.

2. u = Pal(v) for some v ∈ {x, y}∗ if and only if u has relatively prime
periods p and q and |u| = p + q − 2.

Proof of 1. By Theorem 4.6, if u = Pal(v) then xuy is a Christoﬀel word.
Conversely, let w = xuy be a Christoﬀel word and let (w1, w2) be its standard
factorization. Then by Corollary 3.4,
(|w1|x |w2|x
|w1|y |w2|y
) ∈ SL2(Z) ∩ N2×2

38 CHAPTER 4. PALINDROMIZATION

(writing N2×2 for the set of 2 × 2 matrices with nonnegative integer entries).
Let N be any matrix in SL2(Z) ∩ N2×2 such that N11 + N12 = |w|x and
N21 +N22 = |w|y. Since SL2(Z)∩N2×2 is generated by the matrices µ(x) and
µ(y) (see Exercise 4.2), there exists a word v ∈ {x, y}∗ such that N = µ(v).
By Theorem 4.6, w′ = x Pal(v)y is a Christoﬀel word and

µ(v) = (|w′
1|x |w′
2|x
|w′
1|y |w′
2|y
) ,

where (w′
1, w′
2) is the standard factorization of w′. Since N = µ(v), it follows
that |w|x = |w′|x and |w|y = |w′|y. Thus w and w′ have the same slope, and
so w = w′ since there is a unique Christoﬀel word of any given slope. Since
w = xuy and w′ = x Pal(v)y, we have u = Pal(v).

Proof of 2. By Theorem 4.6, if u = Pal(v), then u has relatively prime
periods |w1| and |w2| and |u| = |w1|+|w2|−2, where (w1, w2) is the standard
factorization of the Christoﬀel word xuy. Conversely, suppose u ∈ {x, y}∗

has length |u| = p + q − 2 and relatively prime periods p, q > 0. If p = 1 or
q = 1, then u = xp+q−2 or u = yp+q−2, and in both cases Pal(u) = u. So
suppose p, q > 1.
Since p and q are relatively prime, there exist integers 0 < p′, q′ < p + q
such that pp′ ≡ 1 ≡ qq′ mod (p + q) (Exercise 1.6). We argue that p′ + q′ =
p + q and that p′ ⊥ q′. Since pp′ ≡ 1 ≡ qq′ mod (p + q) and p ≡ −q
mod (p + q), we have

p(p′ + q′) ≡ p′p + q′p ≡ 1 + q′p ≡ 1 − qq′ ≡ 0 mod (p + q).

Therefore, p + q divides p(p′ + q′). Since p and p + q are relatively prime, if
follows that p + q divides p′ + q′. Since 0 < p′ + q′ < 2(p + q), we conclude
that p + q = p′ + q′. Finally, since pp′ ≡ 1 mod (p′ + q′), it follows that
p′ ⊥ (p′ + q′), or p′ ⊥ q′.
Let w be the Christoﬀel word of slope p′
q′ and write w = xu′y for some
u′ ∈ {x, y}∗. Then |u′| = p′ + q′ − 2 = p + q − 2 = |u|. By Part (1) of
this theorem, since w is a Christoﬀel word, there exists a word v ∈ {x, y}∗

such that u′ = Pal(v). Let (w1, w2) be the standard factorization of w. By
Theorem 4.6, u′ has periods |w1| and |w2|. By Lemma 3.5, |w1|p′ ≡ 1 ≡ |w2|q′

mod (p′ + q′). Since p′ + q′ = p + q, and 0 < |w1|, |w2| < p + q, it follows
that |w1| = p and |w2| = q because pp′ ≡ 1 ≡ qq′ mod (p + q). Therefore,
u′ is a word of length p + q − 2 having relatively prime periods p and q.
Since such words are unique up to a permutation of the alphabet (Lemma
4.13), it follows that either u′ = u or u′ = E(u). Therefore, u = Pal(v) or
u = E(Pal(v)) = Pal(E(v)), where the last equality is Exercise 4.4.

4.3. PALINDROMIC CHARACTERIZATION 39

Exercise 4.13. Prove the following statements.

(a) If p ⊥ q and w is a word of length p + q − 1 having periods p and
q, then w is a power of a letter. (Hint: Use the ideas in the proof of
Lemma 4.13.)

(b) (Fine-Wilf Theorem) If p and q are positive integers and w is a word
of length p + q − gcd(p, q) having periods p and q, then w has period
gcd(p, q).

40 CHAPTER 4. PALINDROMIZATION

Chapter 5

Primitive Elements in the
Free Group F2

In this chapter we prove that the positive primitive elements of the free
group F2 = ⟨x, y⟩ are conjugates of Christoﬀel words. We begin by recalling
the relevant deﬁnitions.

5.1 Positive primitive elements of the free group

Let F2 denote the free group generated by the letters x and y. Recall that
every element g of F2 has a unique representation as a reduced word over
the alphabet {x, y, x−1, y−1}, where reduced means that there are no fac-
tors of the form xx−1, x−1x, yy−1 or y−1y in an expression g = a1a2 · · · ar(
with ai ∈ {x, y, x−1, y−1}
). The length of an element g ∈ F2, denoted by
ℓ(g), is the length of the reduced expression for g as a word over the alphabet
{x, y, x−1, y−1}.
A basis (u, v) of F2 is a pair of elements u, v ∈ F2 that generate F2. A
primitive element of F2 is an element u ∈ F2 such that (u, v) is a basis
of F2 for some v ∈ F2. By Exercise 5.1, any endomorphism f of F2 is an
automorphism if and only if (f (x), f (y)) is a basis of F2.
Remark. We have previously used the adjective primitive to refer to words
that are not nontrivial powers of shorter words (see Chapter 1). This will
be the customary sense of the word after the present chapter as well. To
avoid confusion here, we shall never omit the word element when referring
to primitive elements of F2.
Example. Since x and y generate F2, the couples (x, y) and (y, x) are bases
of F2. So x and y are primitive elements of F2.

41

42 CHAPTER 5. PRIMITIVE ELEMENTS IN THE FREE GROUP F2

Example. Let u = xxy and v = xxyxyxxy. Then F2 is generated by u and
v because u(u−1vu−1)−1 = xxy(xy)−1 = x and x−1x−1u = y. Therefore,
(xxy, xxyxyxxy) is a basis of F2 and xxy and xxyxyxxy are primitive ele-
ments of F2. Note that xxy is a Christoﬀel word and xxyxyxxy is a conjugate
of the Christoﬀel word xxyxxyxy.

An element u ∈ F2 is positive if it is an element of the monoid {x, y}∗ ⊆
F2. Recall that u, v ∈ F2 are called conjugate if there exists g ∈ F2 such
that u = gvg−1. The following result establishes the relationship between
the notions of (monoid-theoretic) conjugacy in {x, y}∗ and (group-theoretic)
conjugacy in F2.

Lemma 5.1. Suppose u and v are positive elements of F2. Then u and v
are conjugate in F2 if and only if u and v are conjugate in {x, y}∗.

Proof. (Solution to Exercise 2.2.) Let u and v be positive elements of F2.
That is, u, v ∈ {x, y}∗. Suppose u and v are conjugate in {x, y}∗. Then
there exist words w, m ∈ {x, y}∗ such that u = wm and v = mw. Thus
mum−1 = m(wm)m−1 = mw = v, so u and v are conjugate in F2.
For the converse we prove the following statement: If h ∈ F2, then any
positive elements u and v are conjugate in {x, y}∗ whenever v = huh−1. We
proceed by induction on the length of h. If the length of h is 0, then h is the
identity element of F2 and v = u.
Now suppose that the statement holds for all h ∈ F2 of length less than
r > 0. Suppose g ∈ F2 is of length r and suppose that u and v are positive
elements with v = gug−1. Let g = a1 · · · ar be a reduced expression for g,
where ai ∈ {x, y, x−1, y−1} for 1 ≤ i ≤ r. We consider three cases.

(i): If ℓ(gu) < ℓ(g) + ℓ(u), then the ﬁrst letter z of u must be a−1
r ∈
{x, y}. Write u = zu1 and g = hz−1 for some u1 ∈ {x, y}∗ and some h ∈ F2.
Then
 v = gug−1 = (hz−1)(zu1)(hz−1)
−1 = h(u1z)h
−1.

Since ℓ(h) < r and z ∈ {x, y}, it follows from the induction hypothesis that
u1z and v are conjugate in {x, y}∗. Since u1z and u = zu1 are conjugate in
{x, y}∗, it follows that u and v are conjugate in {x, y}∗.

(ii): If ℓ(ug−1) < ℓ(u) + ℓ(g−1), then an argument similar to that of the
previous case shows that u and v are conjugate in {x, y}∗.

(iii): Finally, suppose that ℓ(gu) = ℓ(g) + ℓ(u) and ℓ(ug−1) = ℓ(u) +
ℓ(g−1). Then a reduced expression for gug−1 is obtained by concatenating
the reduced expressions for g, u and g−1. Since u, v ∈ {x, y}∗ and v = gug−1,
it follows that g and g−1 are words in {x, y}∗. Therefore, g = 1 and u = v.

5.2. POSITIVE PRIMITIVE CHARACTERIZATION 43

This completes the induction.

Exercise 5.1. Suppose f : F2 → F2. Then f ∈ Aut(F2) if and only if
(f (x), f (y)) is a basis of F2.

Exercise 5.2. Suppose r and s are nonnegative integers such that r +s > 0.
Verify that w = xryxs is a primitive element of the free group ⟨x, y⟩ and
that w is a conjugate of the Christoﬀel word xr+sy.

5.2 Positive primitive characterization

In this section we prove the following characterization of the Christoﬀel
words.

Theorem 5.2 (Osborne, Zieschang [OZ1981], Kassel, Reutenauer [KR2007]).
The words in {x, y}∗ that are conjugates of Christoﬀel words are exactly the
positive primitive elements of the free group F2 = ⟨x, y⟩.

We begin by recalling some results about the free group F2. There is a
natural homomorphism from F2 onto the free Abelian group Z2 deﬁned by
mapping the generators x and y of F2 onto the generators (1, 0) and (0, 1)
of Z2, respectively. This induces a map from the group Aut(F2) of auto-
morphisms of F2 onto the group Aut(Z2) ∼= GL2(Z) of automorphisms of
Z2. The map Aut(F2) → GL2(Z) is given by composing an automorphism
ϕ ∈ Aut(F2) with the morphism F2 → Z2 described above. The following
result of Jakob Nielsen from 1917 describes the kernel of this homomor-
phism. (Recall that an automorphism ϕ : G → G of a group G is an inner
automorphism if there exists an h ∈ G such that ϕ(g) = hgh−1 for all
g ∈ G.)

Theorem 5.3. The kernel of the natural group homomorphism Aut(F2) →
GL2(Z) is the subgroup of inner automorphisms.

Proof. A proof of this classical result from combinatorial group theory can
be found in either [LS2001, Chapter I, Proposition 4.5] or [MKS2004].

The following result characterizes pairs of generators of the free Abelian
group Z2.

Lemma 5.4. (a, b) and (c, d) generate Z2 if and only if |ad − bc| = 1.

44 CHAPTER 5. PRIMITIVE ELEMENTS IN THE FREE GROUP F2

Proof. Suppose |ad − bc| = 1. Then (1, 0) and (0, 1) are in the span of (a, b)
and (c, d). Indeed, d(a, b) − b(c, d) = (ad − bc, 0) = ±(1, 0) and a(c, d) −
c(a, b) = ±(0, 1). Thus (a, b) and (c, d) generate Z2.
Conversely, suppose (a, b) and (c, d) generate Z2. Then the matrix equa-
tion (a c
b d

) ⃗x = ⃗b

has a unique solution ⃗x ∈ Z2 for all vectors ⃗b ∈ Z2. For ⃗b = (0, 1)T , we have

⃗x = (a c
b d

)−1 (0
1

) = 1
ad − bc
 ( d −c
−b a

) (0
1

) = 1
ad − bc
 (−c
a

) ∈ Z2.

It follows that |ad − bc| divides |a| and |c|. Since (a, b) and (c, d) generate
Z2, there exists i, j ∈ Z such that i(a, b) + j(c, d) = (1, 0). In particular,
ia + jc = 1, from which it follows that |a| ⊥ |c| (see B´ezout’s Lemma in
Exercise 3.3). Since |ad − bc| divides |a| and |c|, and since |a| ⊥ |c|, we have
|ad − bc| = 1.

Proof of Theorem 5.2. Suppose w is a Christoﬀel word and let (u, v) de-
note its standard factorization. By Theorem 3.6, the couple (u, v) is in the
Christoﬀel tree. Hence, (w, v) = (uv, v) is in the Christoﬀel tree as well.
Since the root (x, y) of the Christoﬀel tree is a basis of F2 and since (u, uv)
and (uv, v) are bases of F2 whenever (u, v) is a basis of F2, it follows that
each couple (u, v) in the Christoﬀel tree is a basis of F2. In particular, (w, v)
is a basis of F2, thus w is a positive primitive element of F2.
Now suppose w′ ∈ {x, y}∗ is a conjugate of a Christoﬀel word w. By
Lemma 5.1, there exists u ∈ {x, y}∗ such w′ = u−1wu. Since w is a primitive
element of F2, there exists v ∈ F2 such that (w, v) is a basis of F2. Thus
(w′, u−1vu) = (u−1wu, u−1vu) is a basis of F2 and w′ is a positive primitive
element of F2 as well.
Conversely, suppose w is a positive primitive element of F2. Then there
exists w′ ∈ F2 such that (w, w′) is a basis of F2. Therefore, g = (w, w′)
is an automorphism of F2 (by Exercise 5.1). Our proof will construct an
automorphism f = (u, v) of F2 with u and v Christoﬀel words and show
that g = (w, w′) is conjugate (in the group-theoretic sense) to f = (u, v).
This will imply that w is a conjugate of u (and w′ is a conjugate of v) in
{x, y}∗. We begin by analyzing the image of g in Z2.
Deﬁne a group homomorphism F2 → Z2 by x ↦→ (1, 0) and y ↦→ (0, 1) and
let (a, b) and (c, d) denote the images of w and w′, respectively, under this

5.2. POSITIVE PRIMITIVE CHARACTERIZATION 45

homomorphism. Note that (a, b) and (c, d) generate Z2 because (w, w′) is a
basis of the free group F2. Therefore, by the previous lemma, ad − bc = ±1.
Note that a and b are nonnegative since w is a positive element of F2. Let
us analyze the possibilities for small values of a and b. Both cannot be zero
since ad − bc = ±1. If a = 0, then ±1 = ad − bc = −bc, which implies that
b = 1. Thus w = y, which is a Christoﬀel word. If b = 0, then ad − bc = ±1
implies that a = 1. So w = x, which is a Christoﬀel word. Hence, we suppose
a and b are positive integers. Fix n ≥ 1. A direct computation (see Exercise
5.2) reveals that all w ∈ F2 with (a, b) = (n, 1), respectively (a, b) = (1, n),
are positive primitive elements of F2 and are conjugate to the Christoﬀel
word xny, respectively ynx. Hence, we further suppose a, b ≥ 2.
If c < 0 and d ≥ 0 or if c ≥ 0 and d < 0, then |ad − bc| ≥ 2, contradicting
the fact that |ad − bc| = 1. Therefore, c and d are both nonnegative or
both nonpositive. If c and d are both nonpositive, then replace w′ with
(w′)−1; thus we can assume that c and d are nonnegative. Finally, we assume
ad − bc = 1 (otherwise, swap w and w′ in what follows). In summary, we
have a basis (and automorphism) g = (w, w′) of F2 such that: the images
(a, b) and (c, d) of w and w′ generate Z2; the points (a, b) and (c, d) lie in
the ﬁrst quadrant; and ad − bc = 1. Hence,
(a c
b d

) ∈ SL2(Z) ∩ N2×2.

Deﬁne a semigroup morphism M : {G, ̃D}∗ → SL2(Z) ∩ N2×2 by

M (G) = (1 1
0 1
) and M ( ̃D) = (1 0
1 1

) .

Since the monoid SL2(Z) ∩ N2×2 is generated by the 2 × 2 matrices M (G)
and M ( ̃D) (see Exercise 4.2), there exists an endomorphism f of {x, y}∗

such that f is a composition of the morphisms G and ̃D, and

M (f ) = (a c
b d

) .

Since f is a composition of the morphisms G and ̃D, the couple (f (x), f (y))
is an element of the Christoﬀel tree. Therefore, (f (x), f (y)) is a basis of F2
by the ﬁrst paragraph of this proof. In particular, f is an automorphism of
F2 and the elements u = f (x) and v = f (y) are Christoﬀel words.
We now compute the composition of f with the natural morphism F2 →
Z2 deﬁned above. Note that we need only compute the images of f (x) and

46 CHAPTER 5. PRIMITIVE ELEMENTS IN THE FREE GROUP F2

f (y) since they generate Z2. Note that the image of f (x) is (|f (x)|x, |f (x)|y)
and the image of f (y) is (|f (y)|x, |f (y)|y). Since G replaces each letter of a
word m with a word having exactly one occurrence of x, we have |G(m)|x =
|m|. Since G replaces y with xy, we have |G(m)|y = |m|y. Equivalently, for
any word m ∈ {x, y}∗,
(|G(m)|x
|G(m)|y
 ) = (|m|
|m|y
) = (1 1
0 1
) (
|m|x
|m|y
) = M (G) (|m|x
|m|y
) .

Similarly,
(| ̃D(m)|x
| ̃D(m)|y
 )
 = (|m|x
|m|
 ) = (1 0
1 1
) (|m|x
|m|y
) = M ( ̃D) (|m|x
|m|y
) .

Since f is a composition of the morphisms G and ̃D, these two identities
imply that the number of occurrences of the letters x and y in the word
f (m) is given by
(|f (m)|x
|f (m)|y
) = M (f ) (|m|x
|m|y
) = (
a c
b d

) (|m|x
|m|y
) .

In particular, (|f (x)|x, |f (x)|y) = (a, b) and (|f (y)|x, |f (y)|y) = (c, d). There-
fore, the image of u in Z2 is (a, b) and the image of v in Z2 is (c, d).
In summary, g = (w, w′) and f = (u, v) are two automorphisms of F2
that give the same morphism of Z2 after composing with the map F2 → Z2.
By Theorem 5.3, the morphism f −1g is an inner automorphism of F2. We
conclude that there exists z ∈ F2 such that f −1g(m) = zmz−1 for all m ∈ F2.
Applying f to each side of this equality, we get g(m) = f (z)f (m)f (z)−1. In
particular, w = g(x) is conjugate in F2 to the Christoﬀel word u = f (x) and
w′ = g(y) is conjugate in F2 to the Christoﬀel word v = f (y). Then Lemma
5.1 yields that w and w′ are conjugates of Christoﬀel words in the monoidal
sense.

By reﬁning the method of the above proof one can obtain the following
result relating the Christoﬀel morphisms with the automorphisms of the free
group F2. Recall that an element w ∈ F2 is positive if w ∈ {x, y}∗ ⊆ F2. An
endomorphism f of F2 is a positive morphism if both f (x) and f (y) are
positive.

Theorem 5.5 (Wen, Wen [WW1994]). The Christoﬀel morphisms of {x, y}∗

are exactly the positive morphisms of the free group ⟨x, y⟩.

Chapter 6

Characterizations

By now we have presented several characterizations of Christoﬀel words—
discretization of line segments, Cayley graphs of cyclic groups, palindromiza-
tion and the positive primitive elements of F2. In this chapter we present a
few more, beginning with one that we have already met in passing.
If w is a (lower) Christoﬀel word, then by deﬁnition it looks like xuy for
some u ∈ {x, y}∗. After Lemma 2.7 and Proposition 4.2, we moreover know
that w is a conjugate of the word yux. The converse also holds.

Theorem 6.1 (Pirillo [Pir1999]). Given u ∈ {x, y}∗, xuy is a Christoﬀel
word if and only if xuy and yux are conjugate.

x u y x u y
y u x

Figure 6.1: The word yux is a conjugate of xuy if and only if xuy
is a Christoﬀel word.

6.1 The Burrows–Wheeler transform

Suppose w is a word over an ordered alphabet1 A. For example, take w to
be the Christoﬀel word xxyxy or the word abraca. Write w and all of its
distinct conjugates as rows in a matrix, listed in lexicographic order.2 The

1We use the inherited ordering for all subsets A of {a < b < c < · · · < z}. In particular,
x precedes y in our favourite alphabet {x, y}.
2The usual dictionary ordering, where aardvark comes before ant comes before anthill.

47

48 CHAPTER 6. CHARACTERIZATIONS

Burrows–Wheeler transform BW T (w) of w is the last column of this
matrix. See Figure 6.2.

x x y x y↦→
x x y x y
x y x x y
x y x y x
y x x y x
y x y x x
 a b r a c a↦→
a a b r a c
a b r a c a
a c a a b r
b r a c a a
c a a b r a
r a c a a b

Figure 6.2: Instances of the Burrows–Wheeler transform. The
transforms xxyxy ↦→ yyxxx and abraca ↦→ caraab are obtained by
reading the last columns of the matrices above.

This is not quite the map introduced by Michael Burrows and David
J. Wheeler [BW1994]. Their map, call it BW T +, maps a word w to the
pair (BW T (w), k), whenever w appears as the k-th row of the Burrows–
Wheeler matrix. For example, BW T +(bracaa) = (caraab, 4) (see Figure
6.2). This augmented map turns out to be injective on A∗ (Exercise 6.2). It
was introduced as a scheme for lossless data compression, and as Giovanni
Manzini shows, BW T + is very eﬀective at its intended purpose [Man2001].
Alternative to introducing BW T +, we could restrict our attention to
those words that are lexicographically least among their conjugates. These
are the so-called Lyndon words. Evidently, BW T becomes injective under
this restriction. More interestingly, it becomes a special case of a mapping
introduced by Ira M. Gessel and Christophe Reutenauer in the study of
descent sets of permutations [GR1993]. See also [CDP2005].
When w = xuy is a (lower) Christoﬀel word, it happens that w appears
as the ﬁrst row of its Burrows–Wheeler matrix (i.e., Christoﬀel words are
Lyndon words). This and other interesting properties are illustrated in Fig-
ure 6.3. The ﬁrst two are explained in Exercise 6.3. The third is explained
by our next characterization of Christoﬀel words.

Theorem 6.2 (Mantaci, Restivo, Sciortino [MRS2003]). A word w ∈ {x, y}∗

is a conjugate of a Christoﬀel word if and only if BW T (w) takes the form
yqxp, where p ⊥ q.

Exercise 6.1. Prove Theorem 6.1. (Hint: This is a consequence of the Fine-
Wilf Theorem; see Exercise 4.13.)

6.1. THE BURROWS–WHEELER TRANSFORM 49

x x y x y
x y x x y
x y x y x
y x x y x
y x y x x

Figure 6.3: The Burrows–Wheeler matrix for the Christoﬀel word
of slope q
p possesses three interesting properties: (i) the lower- and
upper-Christoﬀel words comprise the ﬁrst and last rows, respec-
tively; (ii) any two consecutive rows diﬀer in two consecutive po-
sitions; (iii) the last column takes the form yqx
p

Exercise 6.2. The Burrows–Wheeler transform BW T is injective on Lyn-
don words (cf. [CDP2005] for more details):
Given a Lyndon word w = a1a2 · · · an, let b1b2 · · · bn and c1c2 · · · cn denote
the ﬁrst and last columns, respectively, of the Burrows–Wheeler matrix.

(a) Deﬁne a permutation σ ∈ Sn by putting σ(i) = j if the j-th row of
the Burrows–Wheeler matrix is aiai+1 · · · ai−1. Verify that ai = bσ(i).

(b) Deﬁne a permutation π ∈ Sn by the n-cycle π = (σ(1)σ(2) . . . σ(n)).
Verify that bi = cπ(i).

(c) Let w′ be a Lyndon word with BW T (w′) = BW T (w) = c1c2 · · · cn.
Deduce that w = w′.

Exercise 6.3 (Property (ii) of Figure 6.3). Given the Christoﬀel word w
of slope q
p , let wt denote the conjugate of w obtained by reading |w| letters
along the Christoﬀel path of ww, starting at the lattice point C labelled t
p .
For example, w0 = w and wp+q−1 is the upper Christoﬀel word of slope q
p
(see the proof of Lemma 2.7). Let nt(k) denote the numerator of the label
k steps after C along the Christoﬀel path for wt. That is, nt(k) = t + kq
mod (p + q).

(a) If two successive conjugates wt−1 and wt have longest common preﬁx
u, then wt−1 = uxyv and wt = uyxv′. In particular, nt(0)− nt−1(0) =
1 and nt(|u| + 2) − nt−1(|u| + 2) = 1.

(b) In general, one has nt−1(k) mod (p + q) < nt(k) mod (p + q). There
is precisely one instance of 0 ≤ k < p + q with nt(k) mod (p + q) <
nt−1(k) mod (p + q).

(c) In the factorizations uxyv and uyxv′ of part (a), one has v = v′.

(d) The (t + 1)-st row of the Burrows–Wheeler matrix for w is wt.

50 CHAPTER 6. CHARACTERIZATIONS

6.2 Balanced1 Lyndon words

We next introduce an important class of words ﬁrst deﬁned by Marston
Morse and Gustav A. Hedlund in 1940. A word w ∈ {x, y}∗ is balanced1 if
for each pair u, v of factors of w of equal length, one has
∣
∣
∣ |u|x − |v|x ∣
∣
∣ ≤ 1, or equivalently ∣
∣
∣ |u|y − |v|y ∣
∣
∣ ≤ 1.

Serge Dulucq and Dominique Gouyou-Beauchamps [DGB1990] have shown
that the set of balanced1 words is exactly the set of factors of Christoﬀel
words, or equivalently of Sturmian words (cf. [Lot2002, Chapter 2]). The
characterization we seek is the following.

Theorem 6.3 (de Luca, Mignosi [dLM1994]). A word xuy is a Christoﬀel
word if and only if xux, xuy, yux, and yuy are balanced1.

Alternatively, one may replace the extra “balanced1” checks with a single
“Lyndon” check.

Theorem 6.4 (Berstel, de Luca [BdL1997]). A word w is a Christoﬀel word
if and only if it is a balanced1 Lyndon word.

6.3 Balanced2 Lyndon words

There is another notion of “balanced” that may be given to Lyndon words.
Before deﬁning it, we need to introduce a fundamental result about Lyndon
words. Recall that

a word w is a Lyndon word if and only if for all nontrivial
factorizations w = (u, v), w < vu in the lexicographic order.

Note that we did not allow w ≤ vu. Otherwise stated, we demand that
Lyndon words are primitive. We thus have an equivalent deﬁnition: w is a
Lyndon word if w < v for all proper suﬃxes v of w. If we choose v to
be the lexicographically least suﬃx of w, a surprising thing happens (cf.
[Lot1997, Chapter 5]).

Proposition 6.5 (Chen, Fox, Lyndon [CFL1958], Duval [Duv1983]). If w =
uv is a Lyndon word with v its lexicographically least proper suﬃx, then u
and v are also Lyndon words and u < v.

This is the standard factorization of a Lyndon word, which we call the
right factorization in what follows. It happens that v is simultaneously the

6.4. CIRCULAR WORDS 51

longest proper suﬃx that is Lyndon, which brings us to an alternative left
factorization due to Anatolii I. Shirshov [Shi1962] and Xavier G. Viennot
[Vie1978].

Proposition 6.6. If w = uv is a Lyndon word with u a proper Lyndon
preﬁx of maximal length, then v is also a Lyndon word and u < v.

The left factorization and right factorization of a Lyndon word sometimes
coincide. This led Guy Melan¸con [Mel1999] to introduce a second, recursive,
notion of balanced: call a Lyndon word w balanced2 if w is a letter or there
is a factorization w = (u, v) that is both a left and right factorization with
the further property that u and v are balanced2.

Example. The reader may check that aabaacab, xxyy, and xxyxxyxy are
Lyndon words. Among these, only xxyxxyxy is balanced2. See Figure 6.4.

left factorizations

right factorizations

a a b a a c a b x x y y x x y x x y x y

Figure 6.4: The left and right factorizations of three Lyndon
words. Only xxyxxyxy, the Christoﬀel word of slope 3
5 , is seen to
be a balanced2 Lyndon word.

Theorem 6.7 (Melan¸con [Mel1999]). A word w ∈ {x, y}∗ is a Christoﬀel
word if and only if it is a balanced2 Lyndon word.

6.4 Circular words

Many of the results in this and the preceding chapters deal with conjugates
of Christoﬀel words, but do not distinguish one conjugate from another.
Such results are perhaps better described in terms of circular words: the
conjugacy class of a word w is called a circular word and is denoted by
(w). Our next characterization makes explicit mention of these words.

Theorem 6.8 (Borel, Reutenauer [BR2006]). The following are equivalent
for a word w ∈ {x, y}∗ of length n ≥ 2:

52 CHAPTER 6. CHARACTERIZATIONS

(i) w is a conjugate of a Christoﬀel word;

(ii) the circular word (w) has k+1 factors of length k for k = 0, 1, . . . , n−1;

(iii) w is a primitive word and (w) has n − 1 factors of length n − 2.

Example. Take w = yxxxyxx, which is a conjugate of the Christoﬀel word
of slope 2
5 . We list the distinct factors of each length in Figure 6.5.

x x

x
yx
x

y
 ℓ distinct factors of length ℓ
1 y x
2 yx xx xy
3 yxx xxx xxy xyx
4 yxxx xxxy xxyx xyxx yxxy
5 yxxxy xxxyx xxyxx xyxxy yxxxy xyxxx
6 yxxxyx xxxyxx xxyxxy xyxxyx yxxyxx xxyxxx xyxxxy

Figure 6.5: For Christoﬀel words w, there are ℓ+1 distinct factors
of length ℓ = 1, 2, . . . in the circular words (w).

A brief proof of Theorem 6.8 aﬀords us the opportunity to introduce
several additional results from the theory of Sturmian words.

Theorem 6.9 (folklore). A word w ∈ {x, y}∗ is a conjugate of a Christoﬀel
word if and only if w and all of its conjugates are primitive and balanced1.

Remarks. 1. The requirement that all conjugates be balanced1 is essential
here. For example, xyyx is balanced1 but is certainly not conjugate to a
Christoﬀel word.
2. Antonio Restivo attributes this theorem to Oliver Jenkinson and Luca Q.
Zamboni [JZ2004] when he speaks about the Burrows–Wheeler transform.
He calls a word strongly balanced if it satisﬁes the conditions of the theorem.
We indicate below a proof suggested by Genevi`eve Paquin.

Proof. The forward direction is essentially [Lot2002, Proposition 2.1.10].
First, conjugates of primitive words are primitive, so we need only analyze
the balanced1 implication. This follows from a geometric argument. Suppose
w is a conjugate of the Christoﬀel word of slope b
a . If some conjugate of w is
not balanced1, then there are two factors u and v of ww of the same length
with |u|y and |v|y diﬀering by at least 2. On the other hand, u and v follow
the line of slope b
a , so the quantities |u|y and |v|y can diﬀer by at most 1.

The reverse direction follows from Theorem 6.4. Indeed, if w and all of
its conjugates are primitive and balanced1, then the lexicographically least

6.4. CIRCULAR WORDS 53

conjugate w′ is a Lyndon word (since it is primitive). Hence w′ is a Christoﬀel
word and w is a conjugate of a Christoﬀel word.

A sequence (inﬁnite word) w = a0a1a2 · · · over an alphabet A is called
ultimately periodic if w can be factored as w = uv∞ for some ﬁnite words
u, v ∈ A∗. We do not assume u ̸= ǫ so periodic words are ultimately periodic.
If w is not ultimately periodic, we say that w is aperiodic.

Theorem 6.10 (Morse, Hedlund [MH1940]). If a sequence in {x, y}N is
aperiodic, then it is balanced1 if and only if it has exactly k + 1 factors of
length k for all k ≥ 0.

Remark. The factor complexity described above is often taken as the def-
inition of Sturmian word. In the proof sketch below, we will only need
the trivial part of the forward direction, cf. [Lot2002, Proposition 2.1.2]: a
balanced1 sequence in {x, y}N has at most k + 1 factors of length k for all
k ≥ 0.

Theorem 6.11 (Coven, Hedlund [CH1973]). A sequence in {x, y}N is ape-
riodic if and only if it has at least k + 1 factors of length k for all k ≥ 0.

Remark. Periodic sequences with balanced1 factors are sometimes excluded
from the deﬁnition of Sturmian words in the literature. Ultimately periodic
(but not periodic) sequences are called “skew-words” by Morse and Hedlund
[MH1940]. In the sketch below, we will actually use a “circular” version of
this theorem, cf. [BR2006, Lemma 4.1]: a word w is primitive if and only if
(w) has at least k + 1 factors of length k for all 0 ≤ k < |w|.

Proof of Theorem 6.8. (i) ⇒ (ii) ⇒ (iii): Suppose w is a conjugate of a
Christoﬀel word of length n. Then w and its conjugates are primitive and
balanced1 (Theorem 6.9). Hence, (w) has at most k + 1 factors of length k
and at least k + 1 factors of length k for all 0 ≤ k < n (by the two remarks
above). In particular, w is primitive and (w) has exactly n − 1 factors of
length n − 2.

(iii) ⇒ (i): Suppose w is primitive and (w) has exactly n − 1 factors of
length n − 2. Then (w) has at least k + 1 factors of length k for all 0 ≤ k < n
(by the remark following Theorem 6.11). This implies the existence of a
special factor u of length n − 2 with (w) = (xuy) = (yux) (Exercise 6.4).
But then either xuy or yux is a Christoﬀel word (Theorem 6.1). That is, w
is a conjugate of a Christoﬀel word.

54 CHAPTER 6. CHARACTERIZATIONS

Exercise 6.4. If w is a word of length n and (w) has at least n factors
of length n − 1, then there is a factor u of (w) of length n − 2 so that
(w) = (xuy) = (yux). In particular, w is a conjugate of a Christoﬀel word,
by Theorem 6.1. (Hint: The u that you seek is the unique factor of length
n − 2 that may be extended to the left in two ways (and to the right in two
ways) to a factor of length n − 1.)

6.5 Periodic phenomena

Our ﬁnal characterization of Christoﬀel words is another folklore result that
says that the superposition of two periodic phenomena gives rise to all the
Christoﬀel words. It is anticipated in the original papers on the subject
[Chr1875, Smi1876].

Theorem 6.12 (Superposition of two periodic phenomena). Suppose p and
q are positive integers and p ⊥ q. Set P = {ip : 0 < i < q} and Q = {jq :
0 < j < p}. Write P ∪ Q as {a1, a2, . . . , an}, where a1 < a2 < · · · < an and
n = p + q − 2. Then the word xw1w2 . . . wny, where wi = x if ai ∈ P and
wi = y if ai ∈ Q, is the Christoﬀel word of slope p
q .

The proof is left as an exercise.

Examples. 1. Let p = 4 and q = 7. Then p and q are relatively prime,
P = {4, 8, 12, 16, 20, 24} and Q = {7, 14, 21}. The superposition of P and Q
is given below with the elements of Q in boldface.

4 7 8 12 14 16 20 21 24
x x y x x y x x y x y

Thus we obtain the Christoﬀel word xxyxxyxxyxy of slope 4
7 .
2. Another example (of length 99) appears implicitly in the following pas-
sage from The Brooklyn Follies by Paul Auster:

This was the truth of the world, she told her father at breakfast
that morning, and in order to get a grip on that truth, she had
decided to spend the day sitting in the rocking chair in her room,
shouting out the word rejoice every forty-one seconds and the
word grieve every ﬁfty-eight seconds . . . [Aus2006, page 50].

3. Our ﬁnal example is arguably one of the very ﬁrst examples. Caroline
Series suggests [Ser1985], tongue-in-cheek, that the earliest astronomers were
acquainted with Theorem 6.12. Indeed, in Babylonian calendars from 490
B.C., one ﬁnds extremely accurate approximations such as, “19 years = 235

6.5. PERIODIC PHENOMENA 55

lunar months.” Surely the original calculation was written down in tally
form, “month, month, . . . , month, year, month, month, . . . , month, year,
. . . ,” forming one of the ﬁrst recorded Christoﬀel words.

56 CHAPTER 6. CHARACTERIZATIONS

Chapter 7

Continued Fractions

This chapter exhibits relationships between the Christoﬀel tree, contin-
ued fractions and the Stern–Brocot tree of positive rational numbers. See
[BL1993, GKP1994, BdL1997] for further information, and for a geometric
approach to continued fractions, see [Dav1992].

7.1 Continued fractions

Suppose α ∈ R. The (simple) continued fraction representation of α is
the sequence of integers a0, a1, a2, . . . constructed recursively as follows: let

β0 = α and a0 = ⌊β0⌋;

if i > 0 and ai−1 ̸= βi−1, then let

βi = 1
βi−1 − ai−1 and ai = ⌊βi⌋;

if i > 0 and ai−1 = βi−1, then the recursion terminates. The continued
fraction representation of α is commonly denoted by

α = a0 + 1

a1 + 1

a2 + 1

a3 + 1
. . .

or more compactly by α = [a0, a1, a2, a3, . . .].

57

58 CHAPTER 7. CONTINUED FRACTIONS

Example. Let α = 10
23 . Then

β0 = 10
23 , a0 = ⌊β0⌋ = 0;
β1 = 1
β0−a0 , = 23
10 a1 = ⌊β1⌋ = 2;
β2 = 1
β1−a1 = 10
3 , a2 = ⌊β2⌋ = 3;
β3 = 1
β2−a2 = 3, a3 = ⌊β3⌋ = 3.

Since β3 = a3, the process ends and the continued fraction representation of
10
23 is [0, 2, 3, 3], or
 10
23 = 0 + 1

2 + 1

3 + 1
3

.

Note that, by construction, the integers a1, a2, . . . are positive. The con-
tinued fraction representation of α ∈ R is ﬁnite (that is, the above process
terminates) if and only if α is a rational number.
If [a0, a1, a2, . . . , ai, . . .] is the continued fraction representation of α, then
the i-th continuant of α, for i > 0, is the rational number with continued
fraction representation [a0, a1, . . . , ai−1, ai].

Example. From the previous example, the continued fraction representation
of 10
23 is given by the sequence [0, 2, 3, 3]. Therefore, the continuants of 10
23 are

0 + 1
2 = 1
2 , 0 + 1

2 + 1
3
 = 3
7 , 0 + 1

2 + 1

3 + 1
3
 = 10
23 . (7.1)

7.2 Continued fractions and Christoﬀel words

In his 1876 note [Smi1876], Henry J. Smith showed that the sequences ob-
tained from periodic phenomena in Chapter 6.5 can be obtained from the
continued fraction representation of the associated rational number, and
vice versa. He eﬀectively proved the following characterization of Christoﬀel
words.

Theorem 7.2 (Smith [Smi1876]). A word w = xuy is a Christoﬀel word
if and only if uyx or uxy is equal to sn, where sn is deﬁned recursively by
s−1 = x, s0 = y, and sn+1 = scn
n sn−1 for n ≥ 0, where [c0, c1, . . .] is the
continued fraction representation of |w|y
|w|x .

7.2. CONTINUED FRACTIONS AND CHRISTOFFEL WORDS 59

Examples. 1. The continued fraction representation of 4
7 is [0, 1, 1, 3]. Thus,

s1 = s0
0s−1 = x,

s2 = s1
1s0 = xy,

s3 = s1
2s1 = xyx,

s4 = s3
3s2 = (xyxxyxxyx)xy,

and indeed, x(xyxxyxxyx)y is the the Christoﬀel word of slope 4
7 .
2. The continued fraction representation of 2
5 is [0, 2, 2]. Hence,

s1 = s0
0s−1 = x,

s2 = s2
1s0 = xxy,

s3 = s2
2s1 = (xxyxx)yx,

and x(xxyxx)y is the Christoﬀel word of slope 2
5 .

Smith’s theorem gives a method to obtain the continued fraction repre-
sentation [c0, c1, c2, . . .] of any positive rational number α by considering the
Christoﬀel word xuy of slope α. Let v be uxy (or uyx if uxy does not work).
The integers ci are determined inductively as follows. Let c0 be the highest
power of y that is a preﬁx of v. Suppose that c0, c1, . . . , ci and s0, s1, . . . , si+1
have been constructed. Then ci+1 is the largest integer n such that sn
i+1si is
a preﬁx of v. We illustrate this procedure with the following example.

Example. The Christoﬀel word of slope 4
7 is x(xyxxyxxyx)y. Let v be the
word xyxxyxxyxxy. Then c0 = 0 since v does not begin with y. Since
s1s0 = xy is a preﬁx of v, but s2
1s0 = x2y is not, we have c1 = 1. Since
s2s1 = xyx is a preﬁx of v while s2
2s1 = (xy)2x is not, we have c2 = 1.
Finally, c3 = 3 since v = (xyx)3xy = (s3)3s2.

In [Smi1876], one also ﬁnds a geometric method of obtaining the contin-
uants of real numbers (see Section 20, loc. cit.). We now explain this method
for rational numbers b
a > 0. To ﬁnd the continuants for an irrational number
α, simply replace the line segment from (0, 0) to (a, b) in what follows by
the ray of slope α.
Consider the subpath of the lower Christoﬀel path from (0, 0) to (a, b)
beginning at (1, 0) and ending at (a, b). For example, if (a, b) = (23, 10),
then this subpath is the lower path depicted in Figure 7.1. The convex hull
of this subpath determines a sequence of integer points beginning with (1, 0)
and ending with (a, b) by following the upper boundary from left to right.
For (a, b) = (23, 10), we have the sequence (1, 0), (3, 1), (5, 2), (7, 3), (23, 10);

60 CHAPTER 7. CONTINUED FRACTIONS

again see Figure 7.1. Similarly, the upper Christoﬀel path determines a se-
quence of integer points (following the lower boundary of its convex hull)
beginning at (0, 1) and ending at (a, b). Let σ(a, b) denote the sequence ob-
tained from these two sets of integer points by deleting (1, 0) and (0, 1) and
ordering the remaining points using the natural (lexicographic) ordering of
N2. Let ext(a, b) denote the subsequence of σ(a, b) consisting of the points
that are extreme points of either of the convex hulls deﬁned above. Recall
that an extreme point of a convex set S in the plane is a point in S that
does not lie in any open line segment joining two points of S.

Example. Let b
a = 10
23 . Then the lower Christoﬀel path determines the se-
quence of points (1, 0), (3, 1), (5, 2), (7, 3), (23, 10); and the upper Christof-
fel path determines the sequence of points (0, 1), (1, 1), (2, 1), (9, 4), (16, 7),
(23, 10). See Figure 7.1. The sequences σ(23, 10) and ext(23, 10) are

b
 b
 b

b b
 b
 b
 b

Figure 7.1: The convex hulls of the lower Christoﬀel path from
(0, 1) to (23, 10) and the upper Christoﬀel path from (1, 0) to
(23, 10).

σ(23, 10) : (1, 1), (2, 1), (3, 1), (5, 2), (7, 3), (9, 4), (16, 7), (23, 10)

and
 ext(23, 10) : (2, 1), (7, 3), (23, 10).

Proposition 7.3. Suppose a and b are positive integers and a ⊥ b. Let
(p1, q1), (p2, q2), . . . , (ps, qs) denote the sequence ext(a, b). Then the i-th con-
tinuant of b
a , for 1 ≤ i ≤ s, is qi
pi .

7.2. CONTINUED FRACTIONS AND CHRISTOFFEL WORDS 61

Example. Let b
a = 10
23 . In the previous example, we found that ext(23, 10)
comprises the integer points (2, 1), (7, 3) and (23, 10). The proposition thus
implies that 1
2 , 3
7 and 10
23 are the continuants of 10
23 , in agreement with the
computation in (7.1).
We now describe how to obtain the sequences σ(a, b) and ext(a, b) from
the Christoﬀel tree. We begin with σ(a, b).

Proposition 7.4. Suppose a and b are positive integers and a ⊥ b. Let
(x, y) = (u0, v0), (u1, v1), . . . , (ur, vr) = (u, v) denote the unique path in the
Christoﬀel tree from (x, y) to (u, v) where uv is the Christoﬀel word of slope
b
a . Then σ(a, b) is the sequence of integer points

(1, 1), (|u1v1|x, |u1v1|y), (|u2v2|x, |u2v2|y), . . . , (|uv|x, |uv|y) = (a, b).

Example. Continuing with the above example ( b
a = 10
23 ), Figure 7.2 illustrates
the unique path from the root (x, y) to the vertex labelled

(x
3yx2yx2y, x3yx2yx2yx3yx2yx2yx2y)

and the corresponding sequence of integer points.
The sequence ext(a, b) can also be obtained from the Christoﬀel tree. Be-
gin with the unique path (x, y) = (u0, v0), (u1, v1), . . . , (ur, vr) = (u, v) from
(x, y) to (u, v), where uv is the Christoﬀel word of slope b
a . Let (ui1, vi1),
(ui2, vi2), . . ., (uik , vik ) denote the set of points immediately preceding a
“bend” in the path, i.e., the points (uj, vj) for which the subpath from
(uj, vj) to (uj+2, vj+2) is one of the paths in Figure 7.3.

Proposition 7.5. Suppose a ⊥ b and let (ui1, vi1 ), (ui2, vi2 ), . . ., (uik, vik )
denote the points constructed above. Then ext(a, b) is the sequence

(|ui1vi1|x, |ui1 vi1|y), (|ui2 vi2|x, |ui2 vi2|y), . . . , (|uik vik|x, |uik vik |y), (a, b).

Example. In Figure 7.2 we see that the vertices (x, xy) and (x3yx2y, x2y)
are the only vertices in the path that satisfy the conditions in Figure 7.3.
Therefore, ext(23, 10) is obtained from the three points (x, xy), (x3yx2y, x2y)
and (x3yx2yx2y, x3yx2yx2yx3yx2yx2yx2y) by counting the number of oc-
currences of the letters x and y in these pairs of words: ext(23, 10) is the
sequence (2, 1), (7, 3), (23, 10).

Exercise 7.1. Find the continued fraction representations of the golden
ratio φ = 1+√5
2 and its negated conjugate −φ
∨ = √
5−1
2 . Show that the n-
th continuant of φ is Fn+1/Fn, where Fn is the n-th Fibonacci number
deﬁned recursively by F0 = F1 = 1 and Fn = Fn−1 + Fn−2 for all n ≥ 2.

Exercise 7.2. Rework Exercise 1.5 using Exercise 7.1 and Theorem 7.2.

62 CHAPTER 7. CONTINUED FRACTIONS

(x, y)

(1, 1)

(x, xy)

(2, 1)

(x, x
2y)
 (3, 1)

(x
3y, x
2y)

(5, 2)

(x
3yx
2y, x
2y)

(7, 3)

(x
3yx
2yx
2y, x
2y)

(9, 4)

(x
3yx
2yx
2y, x
3yx
2yx
2yx
2y)

(16, 7)

(x
3yx
2yx
2y, x
3yx
2yx
2yx
3yx
2yx
2yx
2y)

(23, 10)

Figure 7.2: The sequences σ(23, 10) and ext(23, 10) can be ob-
tained from the Christoﬀel tree by counting the number of occur-
rences of the letters x and y along the path from the root (x, y) to
(u, v), where uv is the Christoﬀel word of slope of 10
23 .

7.3 The Stern–Brocot tree

The mediant of two fractions a
b and c
d is a+c
b+d . This operation gives rise to
the Stern–Brocot tree, constructed recursively as follows. Let s0 denote the
sequence 0
1 , 1
0 , where 1
0 is viewed as a formal fraction. For i > 0, let si denote
the sequence obtained from si−1 by inserting between consecutive elements
of the sequence their mediant. The ﬁrst few iterations of this process yields
the following sequences.
 0
1 , 1
0 (s0)

7.3. THE STERN–BROCOT TREE 63

(uj, vj)

ooooooooo

(uj+1, vj+1)
 OOOOOOOOO
 (uj+2, vj+2)
 (uj, vj)
 OOOOOOOOO
 (uj+1, vj+1)

ooooooooo

(uj+2, vj+2)

Figure 7.3: The points (|ujvj|x, |ujvj|y) are in the sequence
ext(a, b).
 0
1 , 1
1 , 1
0 (s1)

0
1 , 1
2 , 1
1 , 2
1 , 1
0 (s2)

0
1 , 1
3 , 1
2 , 2
3 , 1
1 , 3
2 , 2
1 , 3
1 , 1
0 (s3)

0
1 , 1
4 , 1
3 , 2
5 , 1
2 , 3
5 , 2
3 , 3
4 , 1
1 , 4
3 , 3
2 , 5
3 , 2
1 , 5
2 , 3
1 , 4
1 , 1
0 (s4)

The mediants constructed in the i-th iteration of the above process, for i > 0,
are the vertices in the i-th level of the Stern–Brocot tree; there is an edge
in the Stern–Brocot tree between a vertex a
b in level i and a vertex c
d in level
i − 1 if and only if a
b and c
d are consecutive elements of the sequence si. For
example, there is an edge between 2
1 and 3
2 since 3
2 and 2
1 are consecutive
elements of the sequence s3:

0
1 , 1
3 , 1
2 , 2
3 , 1
1 , 3
2 , 2
1 , 3
1 , 1
0

Figure 7.4 shows the top 5 levels of the Stern–Brocot tree. Each fraction in
the tree is of the form a+c
b+d , where a
b is the nearest ancestor above and to the
right of a+c
b+d and c
d is the nearest ancestor above and to the left of a+c
b+d .

Proposition 7.6. The Christoﬀel tree is isomorphic to the Stern–Brocot
tree via the map that associates to a vertex (u, v) of the Christoﬀel tree the
fraction |uv|y
|uv|x . The inverse map associates to a fraction b
a the pair (u, v),

where (u, v) is the standard factorization of the Christoﬀel word of slope b
a .

64 CHAPTER 7. CONTINUED FRACTIONS

1
1

1
2

1
3

1
4

1
5 2
7
 2
5

3
8 3
7
 2
3

3
5

4
7 5
8
 3
4

5
7 4
5
 2
1

3
2

4
3

5
4 7
5
 5
3

8
5 7
4
 3
1

5
2

7
3 8
3
 4
1

7
2 5
1

Figure 7.4: The ﬁrst ﬁve levels of the Stern–Brocot tree

By Theorem 3.6, if a ⊥ b and a, b > 0, then the standard factoriza-
tion (u, v) of the Christoﬀel word of slope b
a appears exactly once in the
Christoﬀel tree. Together with the above isomorphism, this implies the fol-
lowing classical result about the Stern–Brocot tree.

Corollary 7.7. Every positive rational number appears in the Stern–Brocot
tree exactly once.

Moreover, Propositions 7.3 and 7.4 combine with Proposition 7.6 to give
a method for determining the continuants of a real number from the Stern–
Brocot tree. We leave the details to the interested reader.
The following exercises outline a proof of the fact that the Stern–Brocot
tree contains each positive rational number exactly once without mention of
Christoﬀel words. See [GKP1994, Chapter 4.5].

Exercise 7.3. Suppose a
b and c
d are connected by an edge of the Stern–
Brocot tree. Then (a + c) ⊥ (b + d). (Hint: Proceed by induction on the level
of the fractions in the tree, and use B´ezout’s Lemma from Exercise 3.3.)

Exercise 7.4. If a ⊥ b and c ⊥ d and a
b < c
d , then a
b < a+c
b+d < c
d . Hence,
each level of the Stern–Brocot tree preserves the natural order of the rational
numbers.

Exercise 7.5. Suppose a ⊥ b. Then a
b is contained in the Stern–Brocot
tree exactly once. (Hint: Use the previous exercise to show that a
b can occur

7.3. THE STERN–BROCOT TREE 65

at most once. To show that a
b occurs in the tree, begin with the sequence
0
1 < a
b < 1
0 and take mediants. Argue that a
b is eventually the mediant of
two fractions.)

66 CHAPTER 7. CONTINUED FRACTIONS

Chapter 8

The Theory of
Markoﬀ Numbers

In 1879 and 1880, Andrey A. Markoﬀ (later and better known as Markov)
published two memoirs on the minima of indeﬁnite binary quadratic forms
[Mar1879,Mar1880]. He later used the results to answer a longstanding ques-
tion of Bernoulli [Ber1771, Mar1881]. In this chapter, we reformulate some
of the results from these memoirs in terms of Christoﬀel words.

8.1 Minima of binary quadratic forms

Let f (x, y) = ax2 + bxy + cy2 be a real binary quadratic form. The discrim-
inant of f is d(f ) = b2 −4ac, and the minimum of f is m(f ) = inf |f (x, y)|,
where x and y range over all pairs of integers that are not both zero. Two
binary forms f and g are equivalent if there exist r, s, t, u ∈ R such that
ru − st = ±1 and f (x, y) = g(rx + sy, tx + uy). If f and g are equivalent
binary quadratic forms, then d(f ) = d(g) (Exercise 8.1).
Markoﬀ’s work was motivated by the following result of Alexander Ko-
rkine and Grigorii Zolotareﬀ [KZ1873]. For any binary quadratic form f with
d(f ) > 0,
 m(f ) ≤
 √d(f )
√5 , (8.1)

with equality if and only if f is equivalent to a scalar multiple of

f0(x, y) = x
2 − xy − y2,

67

68 CHAPTER 8. THE THEORY OF MARKOFF NUMBERS

and if f is not equivalent to a scalar multiple of f0, then m(f ) ≤ √d(f )/
√8,
with equality if and only if f is equivalent to a scalar multiple of

f1(x, y) = x2 − 2xy − y2.

After learning of these results, Markoﬀ set himself the task of ﬁnding the
quantity that should replace √5 in (8.1) for forms that are not equivalent to
scalar multiples of f0 or f1 [Mar1879]. He concluded that if f is such a form,
then m(f ) ≤ √d(f )/
√221/25, with equality if and only if f is equivalent
to a scalar multiple of
 f2(x, y) = 5x2 − 11xy − 5y2.

Furthermore, he showed that this sequence of exceptions (f0, f1, f2, . . . ) and
better approximations (
√5, √8, √221/25, . . . ) may be extended indeﬁnitely.
Markoﬀ’s idea was to study a bi-inﬁnite sequence of positive integers
associated to a binary quadratic form g with positive discriminant. We
brieﬂy describe how he obtained this sequence. It is a well-known result
(see, for example, Carl F. Gauss’s Disquisitiones Arithmeticae [Gau1986] or
[Dic1930, Chapter VII]) that any binary quadratic form g is equivalent to a
reduced form f (x, y) = ax2 + bxy + cy2: the form f is said to be reduced
if f (x, 1) = ax2 + bx + c has a positive root ξ and a negative root η satis-
fying |η| < 1 < ξ. Writing ξ = [a0, a1, a2, . . .] and −η = [0, a−1, a−2, . . .] for
the continued fraction representations of ξ and −η, we obtain a bi-inﬁnite
sequence
 A = (. . . , a−2, a−1, a0, a1, a2, . . .).

Then √
d(f )/m(f ) is equal to supi∈Z λi(A), where

λi(A) = ai + [0, ai+1, ai+2 . . .] + [0, ai−1, ai−2 . . .]. (8.2)

Conversely, if A = (. . . , a−1, a0, a1, . . .) is a bi-inﬁnite sequence of positive
integers, then there exists a form f such that √d(f )/m(f ) = supi∈Z λi(A).
In the following we present results from [Mar1879, Mar1880] concern-
ing the bi-inﬁnite sequences of positive integers A such that supi λi(A) <
3. As revealed in the work of Thomas W. Cusick and Mary E. Flahive
[CF1989] and Christophe Reutenauer [Reu2005, Reu2006], Christoﬀel words
make an unexpected appearance here. We recast Markoﬀ’s results in these
terms. As a hint of what is to come, we rewrite the Markoﬀ numbers
(
√5, √8, √221/25, . . .) in the form predicted by the general theory:
√
9 − 4
12 <
 √
9 − 4
22 <
 √
9 − 4
52 < · · · < 3.

8.2. MARKOFF NUMBERS 69

The “squared” integers appearing above are explicitly computable and we
ﬁnd them below. Additional information on the Markoﬀ theory may be found
in [Fro1913], [Dic1930] and [Cas1957].

Exercise 8.1. Show that if f and g are equivalent binary quadratic forms,
then they have the same discriminant.

8.2 Markoﬀ numbers

We are interested in the bi-inﬁnite sequences A = (. . . , a−1, a0, a1, . . .) where
the ai belong to the positive integers P (in what follows, we write A ∈ PZ).
Again, to such a sequence A we deﬁne positive real numbers λi(A) ∈ R>0
by
 λi(A) = ai + [0, ai+1, ai+2, . . .] + [0, ai−1, ai−2, . . .],

where following Chapter 7, [a0, a1, a2, . . .] denotes the limit as i goes to
inﬁnity of the i-th continuant

[a0, a1, . . . , ai] := a0 + 1

a1 + 1

a2 + 1

· · · + 1

ai−1 + 1
ai .

Given A as above, denote the supremum of the λi(A) by M (A):

M (A) = sup
i∈Z
 {λi(A)
} ∈ R>0 ∪ {∞}. (8.3)

We will frequently view sequences A ∈ PZ or B ∈ PN as (inﬁnite) words
in what follows, e.g., B = b0b1b2 · · · . In such a case, we denote by [B] the
continued fraction [b0, b1, b2, . . .].

Examples. 1. Take A = · · · 111 · · · . Then λi(A) = 1 + [0, 1, . . .] + [0, 1, 1 . . .]
for each i, so we have M (A) = √
5+1
2 + √5−1
2 = √5. See Exercise 7.1.

2. Take A = · · · 222 · · · . Then M (A) is computed to be √
8.

Before stating our next two examples, we introduce some additional no-
tation. If w is a ﬁnite word, let

∞w∞ = · · · www · · ·

70 CHAPTER 8. THE THEORY OF MARKOFF NUMBERS

denote the periodic bi-inﬁnite word obtained by repeating w inﬁnitely often
in each direction. Also, let ϕ denote the morphism ϕ : {x, y}∗ → {1, 2}∗

deﬁned by ϕ(x) = 11 and ϕ(y) = 22.

Finally, given any A ∈ PZ, we deﬁne the reversal map A ↦→ ̃A by ai ↦→ a−i.

Examples. 3. Take A = ∞ϕ(xy)∞ = ∞(1122)∞. Since A is periodic, one
need only compute λi(A) for four consecutive values of i in order to deter-
mine M (A). The result is computed to be √
221/25.
4. Let w denote the bi-inﬁnite (nonperiodic) discretization of the line
ℓ(x) = √5−1
2 x (see Exercise 1.5). Taking A = ϕ(w), one ﬁnds that M (A) is
approximately 3.2268.
5. Given any A ∈ PZ, we consider ̃A. It is immediate that λi( ̃A) = λ−i(A)
for all i ∈ Z and M ( ̃A) = M (A).

As observed above, M (A) may be computed in a ﬁnite number of steps
when A is periodic. This will always be the case if M (A) < 3, as the next
theorem states. We need one more morphism in order to state it. Deﬁne
η : {x, y}∗ → N2×2 to be the monoid morphism given by

η(x) = (1 1
1 0

)2 = (2 1
1 1
) and η(y) = (2 1
1 0

)2 = (5 2
2 1
).

Theorem 8.4 (Markoﬀ [Mar1879, Mar1880]). Let A ∈ PZ be a bi-inﬁnite
sequence of positive integers. Then M (A) < 3 if and only if there ex-
ists a Christoﬀel word w such that A = ∞ϕ(w)∞. In this case, M (A) =√9 − 4/c2, where c is the (1, 2)-coordinate of the matrix η(w).

Remark. The numbers c obtained in the theorem are the so-called Markoﬀ
numbers It happens that c is also equal to 1
3 trace(η(w)); the interested
reader may try to prove this now or wait for the hint in Lemma 8.7.

Examples. 1. Take w = x (i.e., A = · · · 111 · · · ). Then η(w) = (2 1
1 1

),

c = 1 and √9 − 4/12 = √5 agrees with the value for M (A) computed in
the preceding example.
2. Taking w = y, we ﬁnd c = 2 and M (· · · 222 · · · ) = √9 − 4/22 = √8, as
computed in the preceding example.
3. Suppose w is the Christoﬀel word xy. Then A = ∞(1122)∞ and

η(w) = (2 1
1 1

) (5 2
2 1

) = (12 5
7 3
)
,

8.3. MARKOFF’S CONDITION 71

giving c = 5 and M (A) = √ 221
25 .

Before proceeding to the proof of Theorem 8.4 (section 8.4), we raise a
long-standing open question. Implicit in the theorem is a mapping w ↦→ c(w)
of Christoﬀel words to Markoﬀ numbers. As c(w) is somewhat correlated to
|w|, it is plausible (indeed, provable) that the image of c in P is not surjective.
The complimentary question remains open.

Open Question (Frobenius [Fro1913]). Is the mapping w ↦→ c(w) injective?

Exercise 8.2. The map from words w to Markoﬀ numbers c(w) = (η(w))12
may be injective on Christoﬀel words, but it is not injective on all of {x, y}∗.
(Hint: Use the word w = xxyy.)

Exercise 8.3. Given ﬁxed morphisms α, β ∈ End({x, y}∗), deﬁne a repre-
sentation ρ : {x, y}∗ → End({x, y}∗) of the monoid {x, y}∗ by sending x
to α, y to β and concatenation to composition. For example, ρxyy is the
morphism w ↦→ (α ◦ β ◦ β)(w).

Show that there are Christoﬀel morphisms α and β so that ∣
∣ ρw(y)
∣
∣x equals
the Markoﬀ number c(w) for all words w ∈ {x, y}∗. (Hint: Try to mimic
the action of the map η above; as a further hint, α and β both belong to
{G, ̃D}∗.)

8.3 Markoﬀ’s condition

Lemma 8.5. Suppose β and γ are two real numbers with continued fraction
representations [b1, b2, b3, . . .] and [c1, c2, c3, . . .], respectively. Determining
whether β ≤ γ amounts to comparing ﬁnite preﬁxes b1b2 · · · bi and c1c2 · · · ci
with the following rules:

β < γ ⇐⇒
 



 b1 < c1,
or b1 = c1 and b2 > c2,
or b1 = c1 and b2 = c2 and b3 < c3,
and so on.

Proof. Exercise 8.4.

Given two (possibly inﬁnite) words B = b1b2 · · · and C = c1c2 · · · , we say
that B precedes C in the alternating lexicographic order if the preﬁxes
b1b2 · · · bi and c1c2 · · · ci satisfy the conditions of the lemma for some i > 0.

72 CHAPTER 8. THE THEORY OF MARKOFF NUMBERS

Given a word w over an alphabet X, a letter x ∈ X and any p ∈ P, the
word xp is called a block of w if there is a factorization w = uxpv such that
u ∈ X ∗ does not end by x and v ∈ X ∗ does not begin by x.

Lemma 8.6 (Markoﬀ). Given A ∈ PZ, if M (A) ≤ 3 then ai ∈ {1, 2} for all
i ∈ Z and the blocks of 1s and 2s are of even length.

Note that the converse is false, as evidenced by the “Fibonacci line”
constructed in Example 4.

Proof. First note that λi(A) is equal to ai plus a positive number. This
forces ai < 3, i.e., ai ∈ {1, 2} for all i ∈ Z. We show that 12n1 and 21n2 are
not factors of A for odd numbers n by induction on n. The case n = 1 is a
simple calculation:
If 121 is a factor of A, choose i to be the position of this 2. Then

λi(A) = 2 + 1

1 + 1
∗1
 + 1

1 + 1
∗2
 .

Since each ∗i > 1, we have 1 + 1
∗i < 1 + 1
1 , or 1
1 + 1
∗i > 1
1 + 1 . But then

λi(A) > 2 + 1
2 + 1
2 = 3,

contradicting the hypothesis M (A) ≤ 3. If 212 is a factor of A, choose i to
be the position of the second 2 and write

λi(A) = 2 + 1
∗1 + 1

1 + 1

2 + 1
∗2
 .

Since ∗1 < 3, the second summand is bounded below by 1
3 . Turning to the

ﬁnal summand, we use the inequality 1
∗2 > 0. This yields

1

1 + 1

2 + 1
∗2
 > 1

1 + 1
2 + 0
 = 2
3 ,

8.3. MARKOFF’S CONDITION 73

or λi(A) > 2 + 1
3 + 2
3 = 3, again contradicting the hypothesis M (A) ≤ 3.

To rule out factors 21n2 and 12n1 for odd n > 1, we observe the following
useful fact (see Exercise 8.5):

If A ∈ PZ has a factorization ̃B 2211 C with B and C right-
inﬁnite words, then M (A) ≤ 3 implies [B] ≤ [C]. (⋆)

From this fact we deduce that A cannot be factored as · · · 2(2211)1 · · · ,
because the integral part of [B] = [2, . . .] would be greater than that of
[C] = [1, . . .] (a contradiction after Lemma 8.5).

Case 1: there is a factor 21n2 in A with n > 1 and n odd.
We analyze the slightly longer factor 1r2s1n2 with s ≥ 1 and r maximal
(possibly inﬁnite). We know that 212, 121 and 222111 are not factors of A.
These exclude, respectively, the possibilities r = 1, s = 1 or s ≥ 3. We are
left with s = 2 and the two possibilities: (i) 21r(2211)1n−22, with r < n − 1,
is a factor of A; or (ii) 1r(2211)1n−22, with r ≥ n − 1, is a factor of A. We
may apply induction in the ﬁrst possibility to further assume that n is even
and less than n − 2.
Comparing [B] to [C] using Lemma 8.5, both possibilities yield a con-
tradiction according to (⋆):

(i) B : 1 1 · · · 1 2⩽⩾· · ·⩾̸⩽
C : 1 1 · · · 1 1 (ii) B : 1 1 · · · 1 1⩽⩾· · ·⩽̸⩾
C : 1 1 · · · 1 2r, evenn − 2, odd

Case 2: there is a factor 12n1 in A with n > 1 and n odd.
The analysis is similar. Assume 12n1s2r is a factor of A (with s ≥ 1 and
r maximal). As above, one easily reduces to the case s = 2. The remaining
possibilities, r < n − 2 and even or r ≥ n − 1, are again handled using (⋆)
and Lemma 8.5.

Lemma 8.7. Fix a 2 × 2 symmetric matrix M and set

N = (5 2
2 1

) M (2 1
1 1
)
.

Then N21 = 1
3 trace N .

Proof. Exercise 8.6.

74 CHAPTER 8. THE THEORY OF MARKOFF NUMBERS

Corollary 8.8. If w = yux is an upper Christoﬀel word, then η(u) is sym-
metric and (η(w))21 = 1
3 trace (η(w)).

Markoﬀ introduced the following condition to exploit this property in
his proof of Theorem 8.4.

Deﬁnition 8.9. Suppose s ∈ {x, y}Z. We say s satisﬁes the Markoﬀ con-
dition if for each factorization s = ̃uabv with {a, b} = {x, y}, one has either
u = v, or u = mbu′ and v = mav′ for some (possibly empty) ﬁnite word
m and right-inﬁnite words u′, v′.

Examples. 1. Take s = ∞(xxy)∞. Then the factorization

̃u · ab · v = ∞(xxy)xx · yx · xy(xxy)
∞

yields u = m · b · u′ = x · x · (yxx)∞ and v = m · a · v′ = x · y · (xxy)∞. On
the other hand, the factorization

̃u · ab · v = ∞(xxy)xxyx · xy · xxy(xxy)
∞

yields u = m · b · u′ = x · y · (xxy)∞ and v = m · a · v′ = x · x · (yxx)∞.
2. Taking s = ∞(xxyxy)∞, the pattern ab appears in two distinct ways as
“xy” and two distinct ways as “yx.” We check one of the four possibilities
and leave the rest for the reader. The factorization

s = ∞(xxyxy) x xyx · yx · xyx y (xxyxy)
∞

yields m = xyx, u = xyx · x · (yxyxx)∞ and v = xyx · y · (xxyxy)∞.
3. The bi-inﬁnite word s = ∞(xxyy)∞ does not satisfy the Markoﬀ condi-
tion (both ab = xy and ab = yx fail to give factorizations for s satisfying
the criteria of the deﬁnition).

Remarks. 1. Reutenauer has shown that a bi-inﬁnite word s satisﬁes the
Markoﬀ condition if and only if it is balanced1 (Theorem 3.1 of [Reu2006]).
2. Note that in the ﬁrst two examples above, m is a palindrome. This is
always the case; a proof is outlined in Exercise 8.8 (see also [GLS2008]).

Exercise 8.4. Prove Lemma 8.5.

Exercise 8.5. Two useful properties of λi:

(a) Suppose A = ̃B 2211 C is a factorization with B and C right-inﬁnite
words. If i is the location of the second 2 after ̃B, show that λi(A) ≤ 3
if and only if [B] ≤ [C] (with λi(A) = 3 if and only if [B] = [C]).

8.4. PROOF OF MARKOFF’S THEOREM 75

(b) Suppose A = ̃B 1122 C is a factorization with B and C right-inﬁnite
words. If i is the location of the ﬁrst 2 after ̃B, show that λi(A) ≤ 3
if and only if [B] ≥ [C] (with λi(A) = 3 if and only if [B] = [C]).

Exercise 8.6. Prove Lemma 8.7 and deduce Corollary 8.8. (Hint: If w =
yux is an upper Christoﬀel word, then u is a palindrome.)

8.4 Proof of Markoﬀ’s theorem

After the preceding lemmas, it will be easier to prove the following equivalent
statement of Theorem 8.4.

Theorem 8.10. A bi-inﬁnite sequence A ∈ PZ satisﬁes M (A) < 3 if and
only if there exists an upper Christoﬀel word w such that A = ∞ϕ(w)∞. In
this case, M (A) = √9 − 4/c2, where c = (η(w))21 = 1
3 trace(η(w)).

Suppose A ∈ PZ satisﬁes M (A) < 3. We have seen that A belongs to
{1, 2}Z and moreover its blocks of 1s and 2s have even lengths. We may thus
write A = ϕ(s) for some s ∈ {x, y}Z. We begin by showing that s satisﬁes
the Markoﬀ condition.
Given a factorization s = (̃u, yx, v), we may write A = ̃B 2211 C for
some B = ϕ(u) and C = ϕ(v) in {11, 22}P. From the assumption M (A) ≤ 3
and (⋆) we have [B] ≤ [C], or B ≤ C in the alternating lexicographic
order. Equivalently, since B, C ∈ {11, 22}P, we have u ≤ v in the natural
lexicographic order on {x, y}∗. If u = v, then [B] = [C] and M (A) = 3 (see
Exercise 8.5), which was excluded in the hypotheses of the theorem. Thus
u < v. Letting m = u1u2 · · · ur be the longest common preﬁx of u and v,
we have ur+1 = x and vr+1 = y (since u < v). Analysis of the factorization
s = (̃u, xy, v) is similar (see Exercise 8.5).
We conclude that s satisﬁes the Markoﬀ condition, but in fact more is
true. Namely, the m’s occuring in instances of the Markoﬀ condition have
bounded length N = N (s) (depending only on s). Otherwise, we may ﬁnd an
inﬁnite sequence of factors x ̃mn yx mny of s (or ̃s) satisfying mn is a proper
preﬁx of mn+1 for all n. One uses these factors and the ideas in Exercise
8.5 to show that M (A) = supλi(A) = 3, contradicting the hypotheses of the
theorem.

Lemma 8.11 (Reutenauer [Reu2006, Lemma 3.1]). If s ∈ {x, y}Z satisﬁes
the Markoﬀ condition, then xx and yy are not simultaneously factors of s.

Proof. Suppose xx and yy are both factors of s. Then s = u′xxwyyv′ or
u′yywxxv′ for some ﬁnite word w and some inﬁnite words u′ and v′. Pick w

76 CHAPTER 8. THE THEORY OF MARKOFF NUMBERS

to be of minimal length among all such ﬁnite words. Suppose s = u′xxwyyv′;
the other case is dealt with in a similar manner. By the minimality of w, we
have that w = (yx)p for some p ∈ N. If p = 0, then s = u′xxyyv′, which
contradicts the hypothesis that s satisﬁes the Markoﬀ condition. So suppose
p ≥ 1. Let u = x̃u′ and v = (xy)pyv′. Then s = ̃uxyv. Since s satisﬁes the
Markoﬀ condition, there are two cases.
Case 1: the words u and v are equal.
Then s = ̃vxyv = ̃v′y(yx)pxyv = ̃v′yy(xy)p−1xxyv, contradicting the
minimality of w.
Case 2: there exist right-inﬁnite words u′′ and v′′ and a ﬁnite word m such
that u = myu′′ and v = mxv′′.
Since u = x̃u′ and v = (xy)pyv′, we have that m is nonempty. If |m| ≥
2p + 1, then m begins with (xy)py. So we have s = ̃uxyv = · · · y(yx)pxyv =
· · · yy(xy)p−1xxxyv, contradicting the minimality of w. If |m| < 2p + 1, then
m is a preﬁx of (xy)py. Therefore, m = (xy)i for some 1 < i < p − 1. This
implies s = ̃uxyv = ̃u′′y(yx)ixyv = ̃u′′yy(xy)i−1xxyv, again contradicting
the minimality of w.

Next, we lift sequences s satisfying the Markoﬀ condition via the mor-
phisms G = (x, xy) and ̃D = (xy, y). We claim there exists a sequence
s′ ∈ {x, y}Z such that s = G(s′) or s = ̃D(s′) (apply G−1 if yy is not a fac-
tor of s and ̃D−1 otherwise). It is straightforward (though tedious) to verify
that s′ also satisﬁes the Markoﬀ condition (Exercise 8.8) and moreover that
the bounds on the |m|’s satisfy N (s′) < N (s), cf. [Reu2006, Section 3]. An
induction on N (s) allows us to write s′ as ∞(w′)∞ for some upper Christof-
fel word w′ (note that s = ∞(yx)∞ when N (s) = 0). Thus A = ∞ϕ(w)∞

for some upper Christoﬀel word w, as desired.
To prove the converse, we write A = ∞ϕ(w)∞ for some upper Christoﬀel
word w and compute M (A) explicitly.

Example. Suppose A = ∞ϕ(yxyxx)∞. In Figure 8.1, we compute the ﬁrst
few λi(A).

Returning to the proof, there are evidently only 2|w| distinct λi(A) to
compute, but we can do better. Since ̃w is a conjugate of w (Proposition
4.2), we have ̃A = ∞ϕ( ̃w)∞ = ∞ϕ(w)∞ = A. Consequently, we need only
consider those i corresponding to 1s and 2s in odd positions within their
corresponding blocks in ϕ(w).
We introduce some notation to make things simpler. Index the sequence
A = (an)n∈Z by setting n = 1 to be the location of the start of some copy of
ϕ(w) (in particular, a1 = 2, see Figure 8.1). We have seen that it is enough

8.4. PROOF OF MARKOFF’S THEOREM 77

A = · · · 1 2 2 1 1 2 · · ·
··· 0 1 2 3 4 5 ···
 i λi

1 2
97 √21170 ≈ 2.999982286
2 2.969370222
3 2.124075049
4 2.124075049
5 2.969370224
...

Figure 8.1: The upper Christoﬀel word yxyxx and some of the
10 possible λi(A) values. They were computed using the technique
indicated in the proof of Lemma 8.14.

to compute λi for i corresponding to odd integers. We claim it is enough
to compute λ1. Indeed, we now show that λ1 > λj when j ̸≡ 1 mod 2|w|
corresponds to any other odd integer, i.e., M (A) = λ1(A).
Our proof uses the fact that upper and lower Christoﬀel words are the
least and greatest lexicographically among the conjugates of either (see Ex-
ercise 6.3). We compare w (an upper Christoﬀel word), ̃w (the corresponding
lower Christoﬀel word) and some other conjugate u of w. We have w > u
(lexicographically), which implies w∞ > u∞ and ϕ(w)∞ > ϕ(u)∞ (in the
alternating lexicographic order). By Lemma 8.5, this in turn implies that
[ϕ(w)∞] > [ϕ(u)∞] (as real numbers). Similarly, [∞ϕ( ̃w)] < [∞ϕ(u)]. In
terms of our sequence, we have

[a1, a2, . . .] > [aj, aj+1, . . .]

[a0, a−1, . . .] < [aj−1, aj−2, . . .],

or equivalently
 [a1, a2, . . .] > [aj, aj+1, . . .]

[0, a0, a−1, . . .] > [0, aj−1, aj−2, . . .].

Thus λ1(A) > λj(A), proving our assertion that M (A) = λ1(A).

To understand the Markoﬀ numbers c = 1, 2, 5, . . . we need three classical
facts about the continued fraction representations of quadratic numbers:
α ∈ R is a quadratic number if it is a solution to a monic, quadratic
polynomial over Q. In what follows, we use the notation c1, c2, . . . , cp to
represent the periodic, right-inﬁnite sequence c1, c2, . . . , cp, c1, c2, . . . , cp, . . ..
Also, given a quadratic number α = a±√b
c , we write α
∨ for its conjugate

root, i.e., α
∨ = a∓√b
c .

78 CHAPTER 8. THE THEORY OF MARKOFF NUMBERS

Theorem 8.12 (Lagrange). A number α ∈ R is quadratic if and only if
its continued fraction representation is ultimately periodic. That is, α =
[c0, c1, . . . , cr−1, cr, cr+1, . . . , cr+p−1] (with period p).

Theorem 8.13 (Galois). If a real number α = [c0, c1, c2, . . .] is quadratic,
then the sequence (cn) is purely periodic with period p if and only if α > 1 and
−α
∨ ∈ (0, 1). In this case, α = [c0, c1, . . . , cp−1] and −1
α
∨ = [cp−1, . . . , c1, c0].

Lemma 8.14. If α = [c0, c1, . . . , cp−1], then

α = aα + b
cα + d , where (a b
c d
) = (c0 1
1 0
) · · · · · (cp−1 1
1 0
) .

Sketch of Proof. We illustrate the key idea for p = 2 and leave the proof as
an exercise. Suppose α = [ a, b ] = [a, b, a, b, a, b, · · · ]. Then

α = a + 1

b + 1

a + 1
. . .
 = a + 1

b + 1
α
 .

That is, α = a+ α
bα + 1 = (ab + 1)α + a
bα + 1 . Compare with (a 1
1 0
) (b 1
1 0
)
.

From the above facts we deduce that M (A) = λ1(A) = a1 + [0, a2, . . .] +
[0, a0, a−1, . . .] = α − α
∨, where α = [ϕ(w)∞]. Moreover, the matrix in
Lemma 8.14 for our α is precisely η(w). Now let’s ﬁnd a, b, c, d explicitly.
From cα
2 + dα = aα + b,

we deduce
 α − α
∨ = 1
c
 √
(d − a)2 + 4bc

= 1
c
 √
(d + a)2 − 4

(this last step because det η(w) = 1, by deﬁnition of η(x) and η(y), so
bc = ad − 1). Finally, we know from Lemma 8.7 that 3c = a + d, i.e.,

M (A) = λ1(A) = 1
c
 √9c2 − 4 =
 √
9 − 4
c2 ,

8.4. PROOF OF MARKOFF’S THEOREM 79

concluding the proof of Markoﬀ’s theorem.

In closing, we mention that the values M (A) computed above are part
of a larger story. The set of values M (A) for all bi-inﬁnite sequences A, not
only those obeying Markoﬀ’s restrictions, is called the Markoﬀ spectrum.
Further results on this spectrum may be found in [CF1989].

Exercise 8.7. Prove Lemma 8.14.

The following exercise shows that any m from Deﬁnition 8.9 is a palin-
drome and that xmy is a lower Christoﬀel word or yux is an upper Christoﬀel
word. (The proof in [GLS2008] uses more balanced1 results than we have
set down in Chapter 6.)

Exercise 8.8 ([GLS2008]). Let s be an inﬁnite word in the letters x and y
satisfying the Markoﬀ condition.

(a) Prove that if yy is not a factor of s, then G−1(s) satisﬁes the Markoﬀ
condition; likewise for ̃D−1(s) when xx is not a factor of s. (See
[Reu2006].)
(b) Prove that if two (maximal) blocks xa and xb are factors of s, then
|a − b| ≤ 1; likewise for blocks consisting of the letter y.
(c) Consider a factor y ̃mxymx of s. If m starts with an x, conclude
that m takes the form xayxbyxcy · · · yxa (including the possibility
m = xa). Moreover, xa is the smallest block of x that is a factor of
s.
(d) If u is a palindrome, then (G(u))axa is a palindrome for all a ≥ 1.
(e) Prove that m is a palindrome. (Hint: Proceed by induction on the
number of x-blocks in m. Consider the preimage of s under G or ̃D.)

80 CHAPTER 8. THE THEORY OF MARKOFF NUMBERS

Part II

Repetitions in Words

81

Chapter 1

The Thue–Morse Word

This chapter introduces the Thue-Morse word and presents several equiva-
lent characterizations. We end with a novel application of the Thue-Morse
word to construct magic squares.

1.1 The Thue–Morse word

Recall that a binary word is a word over the alphabet {0, 1}.

Deﬁnition 1.1. The Thue-Morse word t = t0t1t2 · · · is the binary word
t : N → {0, 1} deﬁned recursively by: t0 = 0; and for n ≥ 0, t2n = tn and
t2n+1 = ¯tn, where ¯a = 1 − a for a ∈ {0, 1}. (See Figure 1.1.)

t = t0 t1 t2 t3 · · · tm · · · t2m t2m+1 · · ·
= 0 1 1 0 · · · a · · · a ¯a · · · .

Figure 1.1: The Thue-Morse word t. Here a ∈ {0, 1}.

Example. Here are the ﬁrst forty letters of the Thue–Morse word,

t = 0110100110010110100101100110100110010110 · · ·

Our ﬁrst characterization of the Thue-Morse word is in terms of binary
expansions of nonnegative integers. For every n ∈ N, let d2(n) denote the
sum of the digits in the binary expansion of n.

Proposition 1.2. For all n ∈ N, we have tn = d2(n) mod 2.

83

84 CHAPTER 1. THE THUE–MORSE WORD

Proof. Note that d2 satisﬁes the following recurrence relations: d2(0) = 0;
d2(2n) = d2(n); and d2(2n + 1) = d2(n) + 1. Since d2(n) mod 2 satisﬁes the
same recurrences deﬁning tn, we have tn = d2(n) mod 2.

Exercise 1.1. If t = t0t1t2 · · · is the Thue-Morse word, show that
∑

n≥0
(−1)
tnx
n = (1 − x)(1 − x2)(1 − x4)(1 − x8) · · · .

Exercise 1.2 ([AS1999]). Let t = t0t1t2 · · · be the Thue-Morse word and
let sn = (−1)tn for n ≥ 0. Compute the following.
( 1
2
 )s0 ( 3
4
 )s1 ( 5
6
 )s2 · · · (2i + 1
2i + 2
 )si · · · .

(Hint: Let P = ∏n≥0 ( 2n+1
2n+2 )sn, Q = ∏n≥1 ( 2n
2n+1 )sn. Show that P Q = Q
2P .)

1.2 The Thue–Morse morphism

Deﬁnition 1.3. The Thue-Morse morphism is the map µ : {0, 1}∗ →
{0, 1}∗ deﬁned by µ(0) = 01 and µ(1) = 10.

The Thue-Morse morphism µ is an example of a 2-uniform morphism:
a morphism ξ of words over an alphabet A is a k-uniform morphism if
ξ(a) is a word of length k for all a ∈ A. Chapter 2.1 will have more to say
about k-uniform morphisms.
If s is an inﬁnite word over the alphabet {0, 1}, then let ¯s be the image
of s under the endomorphism deﬁned by 0 ↦→ 1 and 1 ↦→ 0. This morphism
is often called the exchange morphism. Note that µ(¯s) = µ(s) for any
ﬁnite or inﬁnite word s over {0, 1}.

Proposition 1.4. The Thue-Morse word t is a ﬁxed point of the Thue-
Morse morphism µ, i.e., µ(t) = t. Moreover, t and ¯t are the only ﬁxed
points of µ.

Proof. Suppose s is a binary word. Since µ maps each a ∈ {0, 1} to a¯a, it
follows that (µ(s))2n = sn and (µ(s))2n+1 = ¯sn for all n ≥ 0. So if µ(s) = s,
then s2n = sn and s2n+1 = ¯sn. If s0 = 0, then s = t; and if s0 = 1, then
s = ¯t. Therefore, t and ¯t are the only ﬁxed points of µ.

The above result characterizes the Thue-Morse word as the inﬁnite bi-
nary word beginning with 0 that is a ﬁxed point of µ. Deﬁning inﬁnite words

1.2. THE THUE–MORSE MORPHISM 85

in this fashion, as ﬁxed points of morphisms, is a useful technique that will
be employed often in what follows. Let us underscore the necessary ingredi-
ents. Fix n ∈ N and a monoid endomorphism ϕ : A∗ → A∗. We write ϕn for
the n-fold composition of ϕ with itself, the n-th iterate of ϕ. If a is a preﬁx
of ϕ(a) for a given a ∈ A, then ϕn(a) is a preﬁx of ϕn+1(a) for all positive
integers n: indeed, writing ϕ(a) = au, we have

ϕ
n+1(a) = ϕ
n(ϕ(a)) = ϕ
n(au) = ϕ
n(a)ϕ
n(u).

Therefore, the sequence ϕ1(a), ϕ2(a), ϕ3(a), . . . has a (unique) well-deﬁned
limit, which we denote by
 ϕ
∞(a) = lim
n→∞ ϕ
n(a).

Not surprisingly, the Thue-Morse word is a limit of the morphism µ.

Proposition 1.5. The Thue-Morse word t is the limit µ∞(0) = lim
n→∞ µn(0)

of the Thue-Morse morphism µ. Moreover, ¯t = µ∞(1).

Proof. Note that µ(µ∞(0)) = µ∞(0). Therefore, µ∞(0) is a ﬁxed point of µ
beginning with 0. So t = µ∞(0) by Proposition 1.4.

By formalizing the properties of the iterates µn of µ, we arrive at an-
other recursive construction of the Thue-Morse word that is independent
of the Thue-Morse morphism. This characterization has many interesting
consequences, several of which are explored in the exercises.

Proposition 1.6. Fix u0 = 0 and v0 = 1, and let un+1 = unvn and vn+1 =
vnun for n ≥ 0. Then for all n ≥ 0, one has:

(i) un = µn(0) and vn = µn(1);

(ii) vn = ¯un and un = ¯vn;

(iii) for n even, un and vn are palindromes;

(iv) for n odd, ̃un = vn.

Proof. Exercise 1.5.

Exercise 1.3. If t is the Thue-Morse word and µ the Thue-Morse morphism,
then µ(tn) = t2nt2n+1 for all n ≥ 0.

Exercise 1.4. For any ﬁnite binary word w, µ(w) = µ(w) and µ( ̃w) = ̃µ(w).

Exercise 1.5. Prove Proposition 1.6. (Hint: Proceed by induction on n.)

86 CHAPTER 1. THE THUE–MORSE WORD

Exercise 1.6. Show that the Thue-Morse word is a word over the alphabet
{0110, 1001}.

Exercise 1.7. The set of ﬁnite factors of t is equal to the set of ﬁnite factors
of ¯t.

Exercise 1.8. If s is a ﬁnite factor of t, then ̃s is also a factor of t.

Exercise 1.9 (Characterization of the blocks of t, [AAB+1995]). Let A =
(an)n≥0 = 0, 1, 3, 4, 5, 7, 9, 11, 12, 13, . . . denote the lexicographically least
subsequence of nonnegative integers satisfying, for all m ≥ 1, if m ∈ A, then
2m /∈ A. Show that
 t = 0
a1−a01
a2−a10
a3−a21
a4−a3 · · · .

Exercise 1.10 ([Pro1851]). Deﬁne an inﬁnite word a by letting ai (for i ≥ 1)
denote the biggest integer j such that 2j−1 divides i without remainder. The
ﬁrst few letters of a are 1213121412131215 · · · . Deﬁne another inﬁnite word
b to be the word obtained from (01)∞ = 010101 · · · by deleting ai letters
after skipping two letters. That is, keep 2 letters, delete a1 = 1 letter, keep
2 letters, delete a2 = 2 letters, keep 2 letters, delete a3 = 1 letter, and so
on. So b begins as 01101001 · · · . Show that b is the Thue-Morse word.

Exercise 1.11 ([AS2003, Theorem 1.7.7]). Let t be the Thue-Morse word
and µ the Thue-Morse morphism. Show that if φ : {0, 1}∗ → {0, 1}∗ is a
morphism such that φ(t) = t, then φ = µn for some n ≥ 0.

1.3 The Tarry-Escott problem

We next highlight a connection between the Thue-Morse word and a clas-
sical problem in number theory named after Gaston Tarry and Edward B.
Escott in recognition of their contributions to the problem around 1910.
Early results and references appear in [DB1937] and [Wri1959].

Deﬁnition 1.7 (The Tarry-Escott problem). For m ∈ N ﬁnd a positive
integer r and two sequences (a1, . . . , ar) and (b1, . . . , br) of integers such
that
 a1 + a2 + · · · + ar = b1 + b2 + · · · + br,

a
2
1 + a
2
2 + · · · + a
2
r = b
2
1 + b2
2 + · · · + b2
r,
...
a
m
1 + a
m
2 + · · · + a
m
r = b
m
1 + bm
2 + · · · + bm
r .

1.3. THE TARRY-ESCOTT PROBLEM 87

If (a1, . . . , ar) and (b1, . . . , br) form a solution to the Tarry-Escott prob-
lem for m ∈ N, then we say r is the size of the solution, m is the degree of
the solution and we write (a1, . . . , ar) m
= (b1, . . . , br).

Example. The sequences (0, 3, 5, 6) and (1, 2, 4, 7) satisfy

0
1 + 3
1 + 5
1 + 6
1 = 1
1 + 2
1 + 4
1 + 7
1 = 14,

0
2 + 3
2 + 5
2 + 6
2 = 1
2 + 2
2 + 4
2 + 7
2 = 70.

Therefore, (0, 3, 5, 6) 2
= (1, 2, 4, 7). This solution has size 4 and degree 2.

Eug`ene Prouhet was the ﬁrst to provide a general-form solution to the
Tarry-Escott problem (in fact, he did it 60 years prior to the work of Tarry
and Escott). He solved the Tarry-Escott problem of size 2m and degree m
for every m > 1 by partitioning the set of integers from 0 through 2m+1 − 1
into two sets using the Thue-Morse word.

Theorem 1.8 (Prouhet [Pro1851]). For every m > 0, there exists a solution
of size 2m to the Tarry-Escott problem of degree m.

Proof. Let t be the Thue-Morse word and suppose m > 1. For 1 ≤ i ≤ 2m+1,
let ai denote the index of the i-th 0 in the Thue-Morse word t and let bi
denote the index of the i-th 1 in t. Then the sequences (a1, . . . , a2m) and
(b1, . . . , b2m ) form a solution to the Tarry-Escott problem of degree m. The
veriﬁcation of this last statement constitutes Exercise 1.12. (Alternatively,
see [Wri1959].)

Example. From the table below, we see that the indices for the ﬁrst eight 0s
and 1s of t are (0, 3, 5, 6, 9, 10, 12, 15) and (1, 2, 4, 7, 8, 11, 13, 14), respectively.

tn : 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0
n : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

We leave it to the reader to verify that

(0, 3, 5, 6, 9, 10, 12, 15) 3
= (1, 2, 4, 7, 8, 11, 13, 14).

Prouhet was in fact interested in the more general problem of partitioning
the set {0, 1, . . . , nm+1 − 1} into n sets such that each pair of sets form a
solution to the Tarry-Escott problem of degree m. We brieﬂy describe the
partitioning; the construction is illustrated in Figure 1.2.
Fix positive integers n and m and consider a circle with n marked spots.
Write 0 next to the ﬁrst spot, then write 1 next to the second spot, and

88 CHAPTER 1. THE THUE–MORSE WORD

a
 bc
 0
 1
2
 5
 3

4
 7
 8

6
 11
 9

10
 13
 14

12

15
 16

17

19
 20

18

21
 22

23

26
 24

25

Figure 1.2: Prouhet’s partitioning of {0, 1, . . . , 33 − 1}.

so on, except that you skip one spot for every multiple of n, two spots for
every multiple of n2, etc. until nm+1 − 1 is reached. We get a partition of
{0, 1, . . . , nm+1 − 1} into n sets by considering where each integer lies on the
circle.

Example. Take n = 3 and m = 2. Figure 1.2 illustrates Prouhet’s decompo-
sition of {0, 1, . . . , 26} into the three sets

a = (0, 5, 7, 11, 13, 15, 19, 21, 26),

b = (1, 3, 8, 9, 14, 16, 20, 22, 24),

c = (2, 4, 6, 10, 12, 17, 18, 23, 25).

We leave it to the reader to verify that a 2
= b, a 2
= c and b 2
= c.

Remark. Prouhet’s construction deﬁnes a generalization of the Thue-Morse
word to an n-letter alphabet: use the construction to partition N into n sets,
P1, . . . , Pn; associate to each Pj a unique letter aj; and deﬁne a word w by
wi = aj if i ∈ Pj. The word w is called the generalized Thue-Morse
word over the alphabet {a0, a1, . . . , an−1}. For example, the generalized
Thue-Morse word over {0, 1, 2} begins as 012120201120201 · · · (see Figure
1.2).
As with the Thue-Morse word t, there are several equivalent characteriza-
tions of the generalized Thue-Morse word w. It can also be constructed using

1.3. THE TARRY-ESCOTT PROBLEM 89

n-uniform morphisms: if γ(ai) = aiai+1 · · · ana0 · · · ai−1 for all 1 ≤ i ≤ n,
then w = γ∞(a0). And if ai = i for all 0 ≤ i ≤ n − 1, then wm is the sum of
the digits in the base n expansion of m modulo n.

Recent research surrounding the Tarry-Escott problem includes studying
the structure of solutions of minimal size and also multi-dimensional gener-
alizations. We describe each brieﬂy. A solution to the Tarry-Escott problem
of degree m is said to be ideal if its size is m + 1. Ideal solutions are known
to exist for sizes 1, 2, . . . , 10 and 12; see [BI1994, BLP2003].

Example. The ﬁrst ideal solution of degree greater than 10 was found by
Nuutti Kuosa, Jean-Charles Meyrignac and Chen Shuwen [BLP2003]:
(0, 11, 24, 65, 90,129, 173, 212, 237, 278, 291, 302)

11
= (
3, 5, 30, 57, 104, 116, 186, 198, 245, 272, 297, 299
).

A multi-dimensional generalization of the Tarry-Escott problem was re-
cently introduced by Andreas Alpers and Rob Tijdeman [AT2007]. Their
results include the following generalization of Prouhet’s result.

Theorem 1.9. For every k ∈ N, there exist diﬀerent multisets
{(a1, b1), . . . , (a2k , b2k )
} ⊆ Z2 and {(c1, d1), . . . , (c2k , d2k )
} ⊆ Z2,

with ai ̸= bi for at least one i ∈ {1, 2, . . . , 2k}, such that

2k
∑

i=1 a
ε1
i bε2
i =
 2k
∑

i=1 c
ε1
i d
ε2
i

for all nonnegative integers ε1 and ε2 with ε1 + ε2 ≤ k.

Exercise 1.12. Prove Theorem 1.8; that is, show that Prouhet’s solution
satisﬁes the Tarry-Escott problem.

Exercise 1.13. If (a1, a2, . . . , ar) and (b1, b2, . . . , br) form an ideal solution
to the Tarry-Escott problem, then the polynomials (x−a1)(x−a2) · · · (x−ar)
and (x − b1)(x − b2) · · · (x − br) diﬀer only in their constant terms.

Exercise 1.14. Suppose {a1, . . . , ar} and {b1, . . . , br} are distinct sets of
integers. The following are equivalent.

(a) ∑r
i=1 a
j
i = ∑r
i=1 b
j
i for j = 1, . . . , k.

(b) (x − 1)k+1 divides the polynomial ∑r
i=1 (
xai − xbi).

90 CHAPTER 1. THE THUE–MORSE WORD

(c) The degree of the polynomial (x − a1) · · · (x − ar) − (x − b1) · · · (x − br)
is at most r − (k + 1).

Exercise 1.15. Suppose (a1, . . . , ar) and (b1, . . . , br) form a solution to the
Tarry-Escott problem of degree m. If λ and ν are positive integers, then

(λa1 + ν, . . . , λar + ν) and (λb1 + ν, . . . , λbr + ν)

also form a solution of size r and degree m. (Hint: Use the previous exercise.)

1.4 Magic squares

A magic square of order m ∈ N is an m × m matrix whose entries are
distinct elements of {1, 2, . . . , m2} such that the sum of the entries in every
row, column and diagonal is the same. In Exercise 1.16, it is shown that
this sum must be 1
2 m(m2 + 1). In what follows we outline, without proof,
a method to construct a magic square of order 2m for all m ≥ 2 using the
Thue-Morse word t. The reader is referred to [AL1977] for a proof.
To construct a magic square M of order 2m for m ≥ 2, ﬁrst number the
entries of M from left to right, top to bottom, beginning with 1. Let the
n-th entry of M be n if tn−1 = 1. Finally, arrange the unused numbers in
decreasing order to ﬁll the remaining entries of M from left to right and top
to bottom.

Example. We use the above method to construct a magic square of order
22 = 4. Consider the ﬁrst 42 = 16 letters of the Thue-Morse word.

n : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
tn−1 : 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0

From the above table, we see that tn−1 = 1 if n ∈ {2, 3, 5, 8, 9, 12, 14, 15},
so we obtain the partially-completed magic square at the left in Figure 1.3.
The unused numbers, in decreasing order, are 16, 13, 11, 10, 7, 6, 4, 1. These
are used to ﬁll in the empty entries, preserving the order. The resulting
magic square is shown at the right in Figure 1.3.

Remark. The magic square in Figure 1.3, with the central columns inter-
changed, appears in the engraving Melencolia I (Figure 1.5) by the German
Renaissance artist and mathematician Albrecht D¨urer. A similar “magic
square”, depicted in Figure 1.4, appears on a fa¸cade of La Sagrada Fam´ılia,
a basilica in Barcelona, Spain. It is obtained from D¨urer’s magic square by
subtracting 1 from four cells so that the sum of the rows, columns and di-
agonals is 33. Strictly speaking, it is not a magic square because there are
two occurrences of 10 and 14 and it does not include 12 or 16.

1.4. MAGIC SQUARES 91

2 3

5 8

9 12

14 15
 16 2 3 13

5 11 10 8

9 7 6 12

4 14 15 1

Figure 1.3: Left: the n-th box of the magic square is n if tn−1 = 1.
Right: the unused numbers (in boldface) are inserted in decreasing
order into the empty boxes.

1 14 14 4

11 7 6 9

8 10 10 5

13 2 3 15

Figure 1.4: This “magic square” appears on the Passion fa¸cade
of La Sagrada Fam´ılia, a basilica in Barcelona, Spain. The basilica
was originally designed by the architect Antoni Gaud´ı (1852–1926).

Exercise 1.16. If M is a magic square of order m, prove that the sum of
every column, row and diagonal is equal to 1
2 m(m2 + 1).

Exercise 1.17. Construct a magic square of order 8.

92 CHAPTER 1. THE THUE–MORSE WORD

Figure 1.5: Melencolia I by Albrecht D¨urer.

Chapter 2

Combinatorics of the
Thue–Morse Word

This chapter uses the Thue-Morse word to shed light on several classical and
modern results on the combinatorics of words.

2.1 Automatic sequences

We begin by presenting a characterization of the Thue-Morse word using
automata. Brieﬂy, an automaton is a model of computation; it accepts as
input a ﬁnite word and uses the letters of the word to transition from state
to state. Automata are used in this section to construct a class of inﬁnite
words called automatic sequences and in Section 2.5.1 to construct certain
languages.

Deﬁnition 2.1. A ﬁnite deterministic automaton A = ⟨A, Q, q0, F, ·⟩
consists of an alphabet A, a ﬁnite set Q of states, an initial state q0, a
set F ⊆ Q of ﬁnal states, and a next state function · : Q × A → Q.

For the empty word ǫ and each state q ∈ Q, we deﬁne q · ǫ = q. For any
u ∈ A∗ and a ∈ A, we deﬁne q · ua = (q · u) · a. This extends the domain of
the next state function to Q × A∗.
A ﬁnite deterministic automaton A = ⟨A, Q, q0, F, ·⟩ can be represented
as an adorned directed graph as follows (see Figure 2.1 and Figure 2.2 for
examples): the vertex set of the graph corresponds to the set of states Q,
with each vertex labelled by the corresponding state; there is a labelled
arrow q a
−→ p if and only if q · a = p, where a ∈ A and q, p ∈ Q; there is an
(unlabelled) arrow pointing at the initial state q0; and the ﬁnal states are

93

94 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

represented by a double circle. Note that if q ∈ Q and a1, . . . , ai ∈ A, then

a0 b 0

1

1

Figure 2.1: An automaton with states Q = {a, b}, alphabet A =
{0, 1} and initial state q0 = a. There are no ﬁnal states.

computing q · (a1 · · · ai) amounts to starting at the vertex q and following
the unique edge q a1−→ q1 starting at q and labelled a1, then following the
unique edge q1 a2−→ q2, and so on. The last vertex of this path is the state
q · (a1 · · · ai).
The Thue-Morse word t is obtained from the automaton of Figure 2.1
as follows. For each n ∈ N, let bin(n) ∈ {0, 1}∗ denote the binary expansion
of n and consider the state sn = a · bin(n). If bin(n) has an even number
of 1s, then sn = a; otherwise sn = b. Since tn = d2(n) mod 2, where d2(n)
denotes the number of 1s occurring in bin(n) (Proposition 1.2), it follows
that φ(sn) = tn, where φ is the morphism deﬁned by φ(a) = 0 and φ(b) = 1.
This construction is a realization of t as an automatic sequence.

Deﬁnition 2.2. Let ⟨Σk, Q, q0, F, ·⟩ be a ﬁnite deterministic automaton over
the alphabet Σk = {0, 1, . . . , k −1} for some k ∈ N and let φ : Q → X denote
a function from the set of states into some alphabet X. A k-automatic
sequence over X is the inﬁnite word x0x1x2 · · · over the alphabet X given
by deﬁning xn = φ(q0 · a0a1 · · · ai), where a0a1 · · · ai ∈ Σ∗
k is the base-k
expansion of n ∈ N.

Proposition 2.3. The Thue-Morse word is a 2-automatic sequence.

Recall that a morphism ξ : A∗ → A∗ is k-uniform for some k ∈ N
if the word ξ(a) has length k for all a ∈ A. Alan Cobham proved that k-
automatic sequences correspond to 1-uniform morphic images of ﬁxed points
of k-uniform morphisms [Cob1972]. The following theorem is one half of Cob-
ham’s result; see [Cob1972] or Theorem 6.3.2 of [AS2003] for the complete
statement.

Theorem 2.4 (Cobham). If an inﬁnite word w is the ﬁxed point of a k-
uniform morphism for some k ≥ 2, then w is a k-automatic sequence.

Proof. Suppose w is a word over A and let ξ denote a k-uniform morphism
with ξ(w) = w. Deﬁne an automaton over the alphabet {0, 1, . . . , k − 1}

2.1. AUTOMATIC SEQUENCES 95

with state set A, initial state w0 and next state function given by deﬁning,
for 0 ≤ i < k, q · i to be the letter in position i of ξ(q). Then induction on n
establishes that w0 · (a0 · · · ai) = wn, where a0 · · · ai is the base-k expansion
of n (Exercise 2.1).

By Proposition 1.4, the Thue-Morse word is the ﬁxed point of the 2-
uniform Thue-Morse morphism µ. Accordingly, this result gives a second
proof that the Thue-Morse word is 2-automatic (in fact, it rebuilds the
automaton in Figure 2.1).

There are several interesting connections between automatic sequences
and other areas of mathematics and the physical sciences; for example, sev-
eral important sequences occurring in number theory are k-automatic se-
quences. These connections are described in the book by Jean-Paul Allouche
and Jeﬀrey Shallit [AS2003].

Remark. Evidently, the automata formalism allows one to succinctly de-
scribe words with complicated factor-behaviour. But it has many “practi-
cal” applications as well. The reader is invited to reﬂect on the following
question before returning to our discussion on the Thue-Morse word.

Is it possible, given two positive integers k and n, to build a word
w over an n-element alphabet A such that every word of length
k over A occurs in w exactly once?

For example, 10011 possesses 00, 01, 10 and 11 as factors, each occurring
exactly once. Such words, when they exist, are called linear de Bruijn
words. See Exercise 2.3 for more details on their construction. Also, see
[LZ1970] and [Men2003] for applications to shift registers and fractal ren-
dering, respectively, and [Mor2004] for connections to Part I of this book
(speciﬁcally, to Lyndon words).

Exercise 2.1. Complete the proof of Theorem 2.4.

Exercise 2.2. A (circular) de Bruijn word w(k,n) is a word over an n
element alphabet A such that every length k word over A appears as a factor
of the circular word (
w(k,n)) exactly once.

(a) Use the automaton pictured in Figure 2.2 to prove that there exists
a de Bruijn word w(3,2).
(b) Prove that de Bruijn words w(k,2) exist for all positive integers k.
(Hint: The states in Figure 2.2 are members of {a, b}3−1 and the
edges are of the form yu x
→ ux for x, y ∈ {a, b}.)

96 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

aa ab

bbba
 b
 b

a

a

a
 b

a

b

Figure 2.2: An automaton building a de Bruijn word w3,2.

(c) Prove that de Bruijn words exist for all positive integers k and n.
(Hint: The algorithm you will give should construct a word of length
nk. The minimum possible length is achieved.)

Exercise 2.3. A linear de Bruijn word w[k,n] is a word over an n element
alphabet A such that every length k word over A is a factor of w[k,n] exactly
once. Use Exercise 2.2 to prove that linear de Bruijn words w[k,n] exist for
all positive integers k and n. (Hint: The minimum-length linear de Bruijn
words have length nk + (k − 1).)

2.2 Generating series

We next present a characterization of the Thue-Morse word t in terms of a
generating series over Z/2Z for the elements of t. We begin by recalling the
relevant notions; see also Chapters 4 and 6 of [Sta1999] or [AS2003].
A generating series of a sequence (sn)n∈N of elements of a ﬁeld k is the
formal power series ∑
n∈N snxn in one variable x. The ring of all formal power
series in the variable x and with coeﬃcients in k is denoted by kJxK. A series
f (x) ∈ kJxK is said to be rational if there exist polynomials p(x), q(x) ∈ k[x]
such that f (x) = p(x)/q(x). An element f (x) ∈ kJxK is said to be algebraic
over the quotient ﬁeld k(x) of the polynomial ring k[x] if there exist p0(x),
p1(x), . . . , pn(x) ∈ k(x), not all 0, such that

p0(x) + p1(x)f (x) + · · · + pn(x)(f (x))
n = 0.

If f (x) ∈ kJxK is not algebraic over k(x), then f (x) is transcendental over
k(x). Note that if f (x) ∈ kJxK is rational, then it is algebraic over k(x).

Example. The prototypical example of a rational generating series is the
series F (x) = ∑
n≥0 Fnxn built from the Fibonacci numbers (F0 = 1, F1 =

2.2. GENERATING SERIES 97

1; Fn = Fn−1 + Fn−2 for n ≥ 2). One has

1 + (x
2 + x − 1)F (x) = 0.

Let t(x) denote the generating series for the letters of the Thue-Morse
word t over the ﬁnite ﬁeld Z/2Z of two elements. That is,

t(x) = ∑

n≥0 tnx
n ∈ (Z/2Z)JxK.

Also let ¯t(x) ∈ (Z/2Z)JxK denote the generating series for the letters of ¯t.
The next result shows that t(x) and ¯t(x) are algebraic over (Z/2Z)(x).

Proposition 2.5 ([CKMFR1980]). The generating series t(x) and ¯t(x) are
the two solutions to the equation

x + (1 + x)
2Z + (1 + x)
3Z 2 = 0.

Proof. We prove only that t(x) is a solution. Observe that f (x)2 = f (x2)
for any formal power series f ∈ (Z/2Z)JxK. Thus,

t(x) = ∑

n≥0 t2nx
2n + ∑

n≥0 t2n+1x
2n+1

= ∑

n≥0 tnx
2n + ∑

n≥0
(1 + tn)x
2n+1

= ∑

n≥0 tnx
2n + ∑

n≥0 x
2n+1 + ∑

n≥0 tnx2n+1

= t(x
2) + x
1 + x2 + xt(x2)

= (1 + x)t(x)
2 + x
1 + x2 .

Therefore, (1 + x)2t(x) = (1 + x)3t(x)2 + x.

Let Fq denote the ﬁnite ﬁeld with q elements, q a power of a prime.
A theorem of Harry Furstenberg [Fur1967] states that over Fq, every al-
gebraic series in one variable is the diagonal of a rational series in two
variables, where the diagonal of a series ∑
n,m∈N a(n, m)xnym is deﬁned to
be ∑
n∈N a(n, n)xn (see also [AS2003, Theorem 12.7.3]). Jean-Paul Allouche
noticed that the Thue-Morse series t(x) is the diagonal of the following
rational series in F2(x) (see Exercise 2.4):

R(x, y) = y

1 + y(1 + xy) + x
(1 + xy)2 .

98 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

Open Question. Find a combinatorial reason for this identity.

In [CKMFR1980], Gilles Christol, Teturo Kamae, Michel Mend`es France,
and G´erard Rauzy classify automatic sequences consisting of elements from a
ﬁnite ﬁeld in terms of the algebraicity of their generating series. Explicitly,
they show that a sequence (sn)n∈N over Fq is q-automatic if and only if∑
n∈N snxn is algebraic over Fq(x). Together with the above computation,
this gives another proof that the Thue-Morse word is a 2-automatic sequence.

Exercise 2.4. Show that the diagonal D(x) ∈ (Z/2Z)JxK of the series

R(x, y) = y

1 + y(1 + xy) + x
(1 + xy)2 .

satisﬁes (1 + x)3D(x)2 + (1 + x)2D(x) + x = 0. Conclude that D(x) = t(x).

2.3 Overlaps

An overlap is a word of the form auaua, where a is a letter and u is a
(possibly empty) word. A word w is said to be overlap-free if no overlap is
a factor of w. The following result was ﬁrst proved by Axel Thue [Thu1912].

Theorem 2.6. The Thue-Morse word t is overlap-free.

We need the following two lemmas.

Lemma 2.7. Let C = {01, 10}. If x ∈ C ∗, then 0x0 /∈ C ∗ and 1x1 /∈ C ∗.

Proof (Robert Cori). If w ∈ C ∗, then |w|0 = |w|1. Since x ∈ C ∗, we have
|0x0|0 = |x|0 + 2 = |x|1 + 2 > |x|1 = |0x0|1. Thus 0x0 /∈ C ∗.

Lemma 2.8. Fix w ∈ {0, 1}∗ and let µ denote the Thue-Morse morphism.
If w is overlap-free, then µ(w) is overlap-free.

Proof. Let w be a shortest word such that µ(w) is not overlap-free. So
there exist words x, y, u ∈ {0, 1}∗ and a letter a ∈ {0, 1} such that µ(w) =
xauauay. Since µ is 2-uniform, the minimality of w implies that |x|, |y| ≤ 1.
We consider two cases.
Case |x| = 1. Here |y| = 0, since |auaua| is odd. Also, x ̸= a since aa
is not in the image of µ. Hence, µ(w) = ¯aauaua. If |u| is even then both u
and aua are in {01, 10}∗, contradicting the previous lemma. So |u| is odd.
Hence, ua is in the image of µ; that is, there exists some v ∈ {0, 1}∗ such

2.4. COMPLEXITY 99

that ua = µ(v¯a). Since µ(w) = ¯aaµ(v¯a)µ(v¯a) = µ(¯av¯av¯a) and µ is injective,
we have w = ¯av¯av¯a. So w is not overlap-free.
Case |x| = 0. Here y = ¯a, and the preceding argument again shows that
w is not overlap-free.

Proof of Theorem 2.6. By Lemma 2.8, µn(0) is overlap-free, so the preﬁxes
of µ∞(0) are overlap-free. Hence, t is overlap-free by Proposition 1.5.

Remark. Since the Thue-Morse word t is overlap-free and a ﬁxed point of
a nonidentity morphism (Proposition 1.4), it is natural ask which inﬁnite
binary words have these properties. This was answered by Patrice S´e´ebold
in [S´e´e1982]. (See also [BS1993] and [AS2003, Corollary 1.7.9].) Remarkably,
t and ¯t are the only inﬁnite binary words with these properties.

Exercise 2.5. Show that arbitrarily long squares can be found as factors
of the Thue–Morse word t.

Exercise 2.6 ([Brl1989]). Let t be the Thue-Morse word, and consider a
factorization t = xs, where x is a nonempty ﬁnite word and s is an inﬁnite
word. Then either x ends with a square or s starts with a square.

Exercise 2.7 ([Ber1995]). The Thue-Morse word is the lexicographically
greatest inﬁnite overlap-free binary word beginning with 0.

2.4 Complexity

The complexity function cw(n) of a word w is the function that counts the
number of distinct factors of length n in the word w. Closed-form expressions
for the complexity function of the Thue-Morse word were ﬁrst discovered in
1989 independently by Sreˇcko Brlek [Brl1989] and Aldo de Luca and Stefano
Varricchio [dLV1989]. In 1995, John Tromp and Jeﬀrey Shallit provided a
new approach [TS1995] that recovers the earlier results. Our presentation is
based on the work of de Luca and Varricchio [dLV1989].

n : 0 1 2 3 4 5 6 7 8 9 10 11
ct(n) : 1 2 4 6 10 12 16 20 22 24 28 32

Figure 2.3: The ﬁrst 12 values of ct(n).

Lemma 2.9. Let u be a factor of the Thue-Morse word t of length at least
four. Then the starting position of two occurrences of u have the same parity.

100 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

Proof. Suppose u begins by tntn+1tn+2tn+3 = tmtm+1tm+2tm+3 with n even
and m odd. Since n is even, u must begin by a¯a for some a ∈ {0, 1} (e.g., by
Deﬁnition 1.1). Thus tm+1 = tn+1 = ¯a. Since m + 1 is even and t is a word
over the alphabet {01, 10} (Exercise 1.6), we have tn+2 = tm+2 = a. Since
n + 2 is even, tm+3 = tn+3 = ¯a. Since m + 3 is even, tm+4 = a. Therefore,
tm · · · tm+4 = a¯aa¯aa is an overlap as well as a factor of t, contradicting the
fact that t is overlap-free.

As a consequence we obtain a recursive deﬁnition of the complexity func-
tion ct(n) of the Thue-Morse word t.

Proposition 2.10. ct(0) = 1, ct(1) = 2, ct(2) = 4, ct(3) = 6, and for
m ≥ 2,

ct(2m + 1) = 2ct(m + 1) and ct(2m) = ct(m + 1) + ct(m).

Proof. We prove only ct(2m + 1) = 2ct(m + 1), the argument for the other
identity being similar. Let u be a factor of t of length 2m + 1 with m ≥ 1.
We consider two cases.
If u begins at an even position, then the letter following u in t is deter-
mined by the last letter of u since t is a word over the alphabet {01, 10}.
Therefore, there is a bijection between the factors of length 2m + 1 that
begin at an even position and the factors of length 2m + 2 that begin at an
even position. The latter are in bijection with factors of length m + 1 since
t2n = tn and t2n+1 = ¯tn for all n ≥ 0. Therefore, there are ct(m + 1) factors
of t of length 2m + 1 that begin at an even position.
Similarly, if u begins at an odd position then the letter preceding u in t
is determined by the ﬁrst letter of u, so there is a bijection between factors
of length 2m + 1 beginning in an odd position and factors of length m + 1.
Therefore, there are ct(m + 1) factors of t of length 2m + 1 that begin at an
odd position.
By Lemma 2.9, no factor of t of length at least 4 can begin at both an
odd position and an even position, so ct(2m + 1) = 2ct(m + 1).

Our next aim is a closed-form expression for the complexity function
ct(n) of the Thue-Morse word. A (ﬁnite) factor u of the Thue-Morse word t
is said to be right special if both u0 and u1 are also factors of t. (The left
special factors of t are deﬁned analogously.) Let st(n) denote the number of
right special factors of t of length n. There is a strong connection between
the factors of t and its right special factors, which we exploit to develop
a closed-form expression for ct(n). Each right special factor of length n

2.4. COMPLEXITY 101

n : 0 1 2 3 4 5 6 7 8 9 10 11
ct(n) : 1 2 4 6 10 12 16 20 22 24 28 32
st(n) : 1 2 2 4 2 4 4 2 2 4 4 4

Figure 2.4: The ﬁrst 12 values of ct(n) and st(n).

determines two distinct factors of length n + 1 while any factor that is not
right special determines only one factor of length n + 1. Thus, ct and st are
related by

ct(n + 1) = 2st(n) + (ct(n) − st(n)) = st(n) + ct(n). (2.11)

Proposition 2.12. st(1) = 2, st(2) = 2, st(3) = 4 and for all m ≥ 2,

st(2m + 1) = st(m + 1) and st(2m) = st(m).

Proof. This follows from (2.11) and the recursion for ct(n) developed in
Proposition 2.10: if m ≥ 2, then

st(2m + 1) = ct(2m + 2) − ct(2m + 1)

= (ct(m + 2) + ct(m + 1)) − 2ct(m + 1)

= ct(m + 2) − ct(m + 1)

= st(m + 1),

and
 st(2m) = ct(2m + 1) − ct(2m)

= 2ct(m + 1) − (ct(m + 1) + ct(m))

= ct(m + 1) − ct(m)

= st(m).

It follows immediately that st(n) ∈ {2, 4} for all n > 0. But we can be
much more precise: for all n ≥ 3,

st(n) =
 



4, if n ∈ ⋃ k∈N
k≥1 (2k, 2k + 2k−1] ,

2, if n ∈ ⋃ k∈N
k≥1 (2k + 2k−1, 2k+1] . (2.13)

This follows from the above recurrences for st(n). See Exercise 2.11.

102 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

Proposition 2.14. For all n ≥ 3,

ct(n) =
 {3 · 2k + 4(r − 1), if 1 ≤ r ≤ 2k−1,
4 · 2k + 2(r − 1), if 2k−1 < r ≤ 2k,

where k and r are uniquely determined by n = 2k + r with 1 ≤ r ≤ 2k.

Proof. Fix n ≥ 3. Suppose ﬁrst that n ∈ (2k, 2k + 2k−1] for some positive
integer k ≥ 1. Since ct(n) = 2 + ∑n−1
i=1 st(i) and st(i) ∈ {2, 4} for all i ≥ 1
(see (2.11) and (2.13), respectively), it follows that ct(n) = 2+4(n−1)−2m,
where m is the number of elements i in {1, 2, . . . , n − 1} such that st(i) = 2.
By (2.13), m is the cardinality of the set {1, 2} ∪ ⋃k−1
j=1 (2j + 2j−1, 2j+1].
Thus m = 2 + (1 + 2 + · · · + 2k−2) = 2k−1 + 1, and so ct(n) = 4(n − 1) − 2k.
If n ∈ (2k + 2k−1, 2k+1] for some positive integer k ≥ 1, then a similar
argument shows that ct(n) = 2(n − 1) + 2k+1. We conclude that

ct(n) =
 {
4(n − 1) − 2k, if 2k + 1 ≤ n ≤ 2k + 2k−1,
2(n − 1) + 2k+1, if 2k + 2k−1 < n ≤ 2k+1,

for all n ≥ 3, where k is a positive integer such that 2k + 1 ≤ n ≤ 2k+1.
Replacing n by 2k + r, where r = n − 2k, establishes the proposition.

Remarks. 1. A word s is said to be recurrent if every ﬁnite factor of s
occurs inﬁnitely often in s. Exercise 2.8 establishes that the Thue-Morse
word t is recurrent. This implies that t and every suﬃx of t have the same
complexity function, and so too does any inﬁnite word with the same set
of factors as t. Surprisingly, if a recurrent inﬁnite word s has the same
complexity function as t, then the set of factors of s is either the set of factors
of t or the set of factors of δ(t), where δ is the letter-doubling morphism
deﬁned by δ(0) = 00 and δ(1) = 11 [ABG2007].
2. A word s is said to be uniformly recurrent if for every n ∈ N, there
exists a smallest integer Rs(n) such that any factor of s of length n is a
factor of any factor of s of length Rs(n). The function Rs : N → N is called
the recurrence index of s. The Thue–Morse word t is uniformly recurrent
with Rt(1) = 3 because t is overlap-free and Rt(2) = 7 because 00 is not a
factor of t0 · · · t5 = 011010 (Exercise 2.10).

The notion of special factors has come to play an important role in the
theory of words. We close this section with two results concerning the left
special factors of the Thue-Morse word t. (Recall that u is a left special
factor of t if 0u and 1u are factors of t.)

2.4. COMPLEXITY 103

Proposition 2.15. A word u starting with 0 is a left special factor of the
Thue–Morse word t if and only if it is a preﬁx of µn(010) for some n ∈ N.

Proof. Suppose u is a preﬁx of µn(010) for some n ∈ N. We use Exercise
2.13: the image under µ of a left special factor of t is a left special factor of
t. Since 010 is a left special factor of t, we infer that µn(010) is a left special
factor of t for all n ≥ 0. Finally, u is a left special factor of t since it is a
preﬁx of a left special factor of t.
We show that the preﬁxes of µn(010) exhaust all the left special factors of
t that begin with 0. Since the set of ﬁnite factors of t is closed under reversal
(Exercise 1.8), any left special factor determines a right special factor, and
conversely. Thus, the number of left special factors of t having length ℓ is
equal to st(ℓ). And since u is a left special factor if and only if ¯u is a left
special factor (Exercise 2.12), the number of left special factors of length ℓ
that begin with 0 is equal to 1
2 st(ℓ) ∈ {1, 2}. Since the preﬁxes of µn(010)
are left special factors, we need only show that if st(ℓ) = 4, then there are
two distinct words that appear as length ℓ preﬁxes of the words µn(010).
If st(ℓ) = 4, then 2k < ℓ ≤ 2k + 2k−1 for some positive integer k. The
length ℓ preﬁx of µk−1(010) is µk−1(01)v for some nonempty preﬁx v of
µk−1(0). The length ℓ preﬁx of µk(010) = µk−1(011001) is µk−1(01)u for
some nonempty preﬁx u of µk−1(1). Since the ﬁrst letters of u and v are
diﬀerent, we have at least two distinct preﬁxes of the words µn(010) (n ≥ 0)
that have length ℓ.

Figure 2.5 depicts the tree of all the left special factors of the Thue-
Morse word that begin with 0. It is obtained by considering the preﬁxes of
the iterates µn(010) for n ∈ N. Since every preﬁx of the Thue-Morse word is

b 0
 b 1
 b 1
 b 0
 b 1
 b 0
 b 0
 b 1
 b 1
 b 0
 b 0
 b 1
 b 0
 b · · ·

b
0
 b
0
 b
1 b
0
 b
1 b
1 b
0

Figure 2.5: The tree of left special factors beginning with 0 of
the Thue-Morse word.

a preﬁx of µn(010) for suﬃciently large n, we obtain the following immediate
corollary.

Corollary 2.16. Every preﬁx of the Thue-Morse word is a left special factor.

Let t denote the Thue-Morse word and µ the Thue-Morse morphism.

104 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

Exercise 2.8. Prove that every factor of t occurs inﬁnitely often in t (that
is, prove that t is recurrent) and conclude that if s is a suﬃx of t, then
cs(n) = ct(n) for all n ∈ N.

Exercise 2.9 ([CH1973]). Prove that a word s is uniformly recurrent if
and only if every factor w of s occurs in s inﬁnitely often and the distances
between consecutive occurrences of w in s are bounded.

Exercise 2.10. Show that t is uniformly recurrent and the recurrence index
Rt of t satisﬁes Rt(1) = 3 and Rt(2) = 7. (Hint: Use the previous exercise.)

Exercise 2.11. Suppose n ≥ 3 and k is a positive integer such that 2k +1 ≤
n ≤ 2k+1. Then
 st(n) =
 {
4, if n ∈ (2k, 2k + 2k−1] ,
2, if n ∈ (2k + 2k−1, 2k+1] .

(Hint: Proceed by induction on k using Proposition 2.12.)

Exercise 2.12. If s is a right special factor of t, then ¯s is also a right
special factor of t. Prove this also holds for left special factors of t. (Hint:
Use Exercise 1.7.)

Exercise 2.13. Prove that if s is a right special factor of t, then µ(s) is a
right special factor of t. Prove this also holds for left special factors.

Exercise 2.14. Find another proof of Corollary 2.16 using Proposition 1.6,
Exercise 1.8 and the previous exercise.

2.5 Formal languages

The goal of this section is to give a brief introduction to an aspect of formal
language theory that involves the generation of languages.
A language over an alphabet A is a set of words over A. Several lan-
guages have a natural method for their generation. This has lead to the
Chomsky hierarchy of classes of languages, with each class of languages
in the hierarchy strictly containing the previous one. These are the regu-
lar languages, the context-free languages, the context-sensitive languages
and the recursively enumerable languages. In what follows we will brieﬂy
illustrate the theory of regular and context-free languages using languages
constructed from the Thue-Morse word. In particular, we prove that the lan-
guage of factors of the Thue-Morse word is neither regular nor context-free,

2.5. FORMAL LANGUAGES 105

and the language of binary words that are not preﬁxes of the Thue-Morse
word is context-free, but not regular. We also consider the language of binary
words that are not factors of the Thue-Morse word.

2.5.1 Regular languages

Recall from Deﬁnition 2.1 that a ﬁnite deterministic automaton A over an
alphabet A consists of a ﬁnite set of states Q, an initial state q0, a set of
ﬁnal states F and a next state function, denoted by · : Q × A → Q, that
extends to Q × A∗ multiplicatively.
A word u ∈ A∗ is accepted by the automaton if the state q0 · u is a
ﬁnal state and rejected otherwise. For example, abbbaaab is accepted by
the automaton in Figure 2.2 while abbbaaaba is rejected. The language of
words accepted by an automaton A is denoted by L(A).

L(A) = {w ∈ A
∗ : q0 · w ∈ F }.

Deﬁnition 2.17. A language L ⊆ A∗ is regular if there exists a ﬁnite
deterministic automaton A over A such that L = L(A).

Let A = ⟨A, Q, q0, F, ·⟩ be a ﬁnite deterministic automaton and L the
regular language accepted by A. If a1, a2, . . . , ap ∈ A with a1a2 · · · ap ∈ L,
then q0, q0 · a1, q0 · (a1a2), . . . , q0 · (a1 · · · ap) describes a sequence of states
of the automaton. If two of these states are the same (e.g., if p ≥ |Q|), then
there exist integers 0 ≤ i < j ≤ p such that q0 · (a1 · · · ai) = q0 · (a1 · · · aj).
So, for all n ∈ N,

q0 · (a1 · · · ai)(ai+1 · · · aj)
n = q0 · (a1 · · · ai).

In particular, q0 ·(a1 · · · ai)(ai+1 · · · aj)n(aj+1 · · · ap) is a ﬁnal state for all n ∈
N. This observation is known as the pumping lemma for regular languages.

Lemma 2.18 (Pumping lemma for regular languages). Suppose L ⊆ A∗ is
a regular language. There exists an integer p ≥ 1 such that for every word
w ∈ L with |w| ≥ p, there is a factorization w = (x, y, z) in A∗ satisfying
y ̸= ǫ, |xy| ≤ p and xynz ∈ L for all n ∈ N.

The integer p in the statement of the lemma is called the pumping
length of L. The terminology reﬂects the observation that a word w ∈ L can
be “pumped up” by repeating y an arbitrary number of times. The primary
use of the pumping lemma is to prove that languages are not regular.

106 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

Proposition 2.19. The set of factors of the Thue-Morse word t and the
set of preﬁxes of t are not regular languages.

Proof. Let L denote the set of factors (respectively, preﬁxes) of the Thue-
Morse word t and suppose that L is a regular language. Let p denote the
pumping length of L and let w denote a factor (preﬁx) of t of length at
least p. The pumping lemma for regular languages implies that there is a
factorization w = xyz such that y ̸= ǫ and xynz ∈ L for all n ∈ N. Thus
xy3z is a factor of t for some nonempty word y, which contradicts the fact
that t is overlap-free (Theorem 2.6).

The fact that the set of preﬁxes of t is not a regular language also follows
from Exercise 2.18, which characterizes the inﬁnite words whose preﬁxes
form a regular language as those words that are ultimately periodic. (An
inﬁnite word w is ultimately periodic if there exist ﬁnite words x and y
such that w = xyyy · · · .)
It happens that regular languages are closed under complementation
(Exercise 2.16), thus the following result is immediate from Proposition 2.19.

Corollary 2.20. The set of binary words that are not factors of the Thue-
Morse word t is not a regular language, nor is the language consisting of the
binary words that are not preﬁxes of t.

Below we will see that one of these languages is context-free while the
same question for the other language remains open.

Exercise 2.15. Let A denote the automaton deﬁned by A = {a, b}, Q =
{1, 2, 3, 4}, q0 = 1, F = {4} and next state function given by the following
table.
 · 1 2 3 4
a 2 2 4 2
b 1 3 1 3

Draw the graph of A and describe the language L(A) accepted by A.

Exercise 2.16. The complement of a regular language is a regular language.

Exercise 2.17. Let L = {
w ∈ {0, 1}∗ : |w|0 = |w|1}. Show that L is not a
regular language.

Exercise 2.18. Let w be an inﬁnite word over an alphabet A and let L ⊆ A∗

be the language consisting of the preﬁxes of w. Then L is regular if and only
if there exist ﬁnite words x and y such that w = xyyy · · · . Conclude that
the language of preﬁxes of the Thue-Morse word is not regular.

2.5. FORMAL LANGUAGES 107

2.5.2 Context-free languages

Informally, a grammar provides a set of recursive rules for rewriting words
over an alphabet A as words over a subset T of A. We will be concerned
with the so-called context-free grammars.

Deﬁnition 2.21. A context-free grammar G = ⟨V, T, P ⟩ consists of an
alphabet V of variables, an alphabet T of terminal letters, which is
disjoint from V , and a ﬁnite set P ⊆ V × (V ∪ T )
∗ of productions.

Suppose (v, u) is a production in a context-free grammar G. The ter-
minology “context-free” comes from the fact that v can be replaced by
u regardless of the context in which v occurs. So if w = xvy is a word
in (V ∪ T )
∗, then the application of the rule (v, u) produces the new word
w′ = xuy. Often, letters from V will still occur in the word u of a production
(v, u), so other productions can be used to replace these letters.
If (v, u) is a production and w = xvy and w′ = xuy, then we write
w → w′. Note that v → u for (v, u) ∈ P . More generally, given a sequence
w0, . . . , wn of words over V ∪ T such that w0 → w1, w1 → w2, . . . , wn−1 →
wn, we write w0 → w1 → · · · → wn or w0 ∗
→ wn. Such a sequence is called a
derivation from w0 to wn of length n, and we say that wn is derived from
w0. A context-free grammar G = ⟨V, T, P ⟩ generates a language L(G, v) by
considering all the words over T that can be derived from a particular vari-
able v ∈ V . Such languages are the context-free languages.

Deﬁnition 2.22. A language L ⊆ T ∗ is a context-free language if there
exists a context-free grammar G = ⟨V, T, P ⟩ and a variable v ∈ V such that

L = L(G, v) = {w ∈ T ∗ : v ∗
→ w}.

It happens that the class of context-free languages coincides with the
class of languages accepted by pushdown automata, which will not be deﬁned
here. As in the case of regular languages, there exists a pumping lemma for
context-free languages (see Exercise 2.22), whose primary use is to prove
that a language is not context-free. In light of this, the proof of Proposition
2.19 also proves the following.

Proposition 2.23. The set of factors of the Thue-Morse word and the set
of preﬁxes of the Thue-Morse word are not context-free languages.

Unlike for regular languages, context-free languages are not closed under
complementation. Therefore, one can ask whether the complements of the
languages of the above proposition form context-free languages.

108 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

Theorem 2.24. The set of binary words that are not preﬁxes of the Thue-
Morse word t is a context-free language.

Proof. If w = w0w1 · · · wr is a preﬁx of t, then w0 = 0, w2n = wn and
w2m+1 = wm for all n, m ∈ N with 2n ≤ |w| and 2m+1 ≤ |w|. Consequently,
a word w is not a preﬁx of t if and only if w begins with 1, or w = xay¯az
with |y| = |x| − 1 and a ∈ {0, 1}, or w = xayaz with |x| = |y| and a ∈ {0, 1}.
Since the class of context-free languages is closed under ﬁnite union (Exercise
2.21), we need only provide context-free grammars that generate each of
these three languages. We call the languages A, B and C below. To simplify
notation, we write v → {u1, u2, . . . , un} to denote the set of productions
v → u1, v → u2, . . . , v → un.
Consider the context-free grammar A with variables α and β, terminals
{0, 1}, and productions α → 1β and β → {ǫ, 0β, 1β}. Beginning with α,
these productions generate all binary words beginning with 1: if w is a binary
word beginning with 1, then

α → 1β → 1(w1β) → 1w1(w2β) → 1w1w2(w3β) → · · · → w;

and every word in L(A, α) begins with 1. Hence, A = L(A, α) is context-
free.
Next consider the grammar B with variables {α, β, γ}, terminals {0, 1}
and productions

α → γ1β, β → {ǫ, 0β, 1β}, γ → {0γ0, 0γ1, 1γ0, 1γ1, 00, 10}.

We will show that L(B, α) is the language of binary words x0y1z, where
x, y, z ∈ {0, 1}∗ with |y| = |x| − 1. Suppose w = x′(a0)y1z with a ∈ {0, 1}
and |y| = |x′|. By arguing as in the previous paragraph, we can show that
1β ∗
→ 1z for any z ∈ {0, 1}∗. Therefore, α → γ1β ∗
→ γ1z. So if l = |y| − 1,

α ∗
→ γ1z → (x′
0γyl) 1z → x′
0 (x′
1γyl−1) yl1z → · · · → x′γy1z → w.

Thus w ∈ L(B, α). The reverse containment is straightforward to prove.
Similarly, {x1y0z : x, y, z ∈ {0, 1}∗, |y| = |x| − 1} is a context-free language,
so B is as well.
Finally, consider the grammar C with variables {α, β, ξ}, terminals {0, 1}
and productions α → ξ0β, β → {ǫ, 0β, 1β} and ξ → {0ξ0, 0ξ1, 1ξ0, 1ξ1, 0}.
Arguing as in the previous paragraph, it follows that L(C, α) is the context-
free language of all binary words x0y0z, where x, y, z ∈ {0, 1}∗ and |x| = |y|.
Similarly, {x1y1z : x, y, z ∈ {0, 1}∗, |x| = |y|} is a context-free language and
so is C.

2.5. FORMAL LANGUAGES 109

So the complement of the preﬁxes of the Thue-Morse word t is a context-
free language. The analogous question for all factors of t remains open.

Open Question. Is the set of binary words that are not factors of the
Thue-Morse word a context-free language?

Towards answering this question, Narad Rampersad has recently shown
that the language is not an unambiguous context-free language [Ram2007].
We outline the argument below.
There are, in a typical grammar, many ways to derive a word from a
variable, as is illustrated in the following example.

Example. Consider the context-free grammar G with variable A, terminal a,
and productions A → AA and A → a. There are two distinct paths to aa:

A → AA → aA → aa,

A → AA → Aa → aa.

By taking the convention to always apply a production to the leftmost
remaining variable, we obtained the so-called leftmost derivations. As the
reader might imagine, this need not remove all the ambiguity.

Example. In the previous example there is exactly one leftmost derivation
of aa. However, there are two leftmost derivations of aaa:

A → AA → aA → aAA → aaA → aaa,

A → AA → AAA → aAA → aaA → aaa.

Deﬁnition 2.25. A context-free language L is unambiguous if there exists
a context-free grammar G generating L such that every w ∈ L has exactly
one leftmost derivation in G.

Example. Let L be the context-free language generated by the context-free
grammar G of the previous two examples. Then L = {an : n ≥ 1}. This
language is unambiguous because it can be generated by the context-free
grammar with variable A, terminal a, and productions A → Aa and A → a.

The following result of Noam Chomsky and Marcel-Paul Sch¨utzenberger
is useful in proving that a given language is not unambiguous context-free.

Proposition 2.26 (Chomsky, Sch¨utzenberger [CS1963]). If L ⊆ A∗ is
an unambiguous context-free language, then the generating series FL(x) =∑
n≥0 |L ∩ An|xn is algebraic over Q(x).

110 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

See Section 2.2 for the necessary notions regarding generating series. We
apply this result with L equal to the language of binary words that are not
factors of the Thue-Morse word t. So L ∩ {0, 1}n is the set of binary words
of length n that are not factors of t. If ct(n) is the number of factors of t
of length n, then |L ∩ {0, 1}n| = 2n − ct(n). It follows that the series FL(x)
is algebraic if and only if the series Ct(x) = ∑n≥0 ct(n)xn is algebraic. And
Ct(x) is algebraic if and only if St(x) = ∑
n≥0 st(n)xn is algebraic, where
st(n) = ct(n + 1) − ct(n) for all n ∈ N.

Lemma 2.27 (Carlson [Car1921]). A power series with integer coeﬃcients
and radius of convergence 1 is either rational or transcendental.

We know from Section 2.4 that the sequence (st(n))n≥0 is bounded be-
tween 2 and 4, so the series St(x) is either rational or transcendental by
the above lemma. If the series St(x) is rational, then the sequence st(n) is
ultimately periodic (Exercise 2.24). But this is not possible by (2.13). So the
series St(x) is not algebraic and L is not unambiguous context-free.

Theorem 2.28 (Rampersad [Ram2007]). The set of binary words that are
not factors of the Thue-Morse word t is not unambiguous context-free.

Exercise 2.19. Let L = {0n1n : n ∈ N}. Show that L is a context-free
language, but not a regular language.

Exercise 2.20. Deﬁne a context-free grammar G = ⟨{α, β, γ, δ}, {0, 1}, P ⟩
with productions P given by

α → β, α → γ, β → δ0β, β → δ0δ,
γ → δ1γ, γ → δ1δ, δ → 0δ1δ, δ → 1δ0δ, δ → ǫ.

Show that L(G, α) is the language of binary words with a diﬀerent number
of occurrences of 0s and 1s.

Exercise 2.21. If L and L′ are context-free languages, then L ∪ L′ is a
context-free language.

Exercise 2.22 (Pumping Lemma for Context-Free Languages). Let L be a
context-free language. There exists p ∈ N such that if w ∈ L and |w| ≥ p,
then there exists a factorization w = (u, v, x, y, z) satisfying |v|, |y| > 0,
|vxy| ≤ p, and uvixyiz ∈ L for each i ≥ 0. (Hint: Argue that if |w| ≥ b|V |+1,
where b is the maximum number of variables in the right-hand side of a
production, then there is a derivation of the form ξ → vξy with v, y ̸= ǫ.)

2.6. THE TOWER OF HANOI 111

Exercise 2.23. Prove that the language L = {anbncn : n ∈ N} ⊆ {a, b, c}∗

is neither regular nor context-free.

Exercise 2.24. If {a0, a1, a2, . . .} is a sequence in R taking only ﬁnitely
many values and satisfying a linear recurrence relation (i.e.,

an = γ1an−1 + · · · γkan−k (∀ n ≫ 0)

for ﬁxed γi ∈ R and k ∈ N), then {a0, a1, a2, . . .} is ultimately periodic.

2.6 The Tower of Hanoi

In the following we will use the Thue-Morse word to construct a solution to
the Tower of Hanoi puzzle. Our exposition is based on an article by Jean-
Paul Allouche, Dan Astoorian, Jim Randall and Jeﬀrey Shallit [AARS1994].
The Tower of Hanoi is a puzzle that appears to have been invented
by the French number theorist Fran¸cois ´Edouard Anatole Lucas (1842-1891)
under the pseudonym “N. Claus (of Siam)”. It consists of a ﬁxed number of
disks, no two of which have the same radius, placed on top of each other in
order of size with the largest disk on the bottom. See Figure 2.6. There are
two other piles, which initially contain no disks. The goal of the puzzle is to
move all the disks to one of the other piles according to the following rule:
exactly one disk can be moved from one pile to another as long as the disk
will not cover a smaller disk.
The Tower of Hanoi puzzle may be modelled by the directed graph in
Figure 2.7. The three nodes each represent one of the piles, and the arrows
represent moving a disk from one pile to another. A word over the alpha-
bet {a, b, c, ¯a, ¯b, ¯c} encodes a sequence of disk movements. For example, acb
encodes the following sequence of disk movements: move a disk from Pile
1 onto Pile 2; move a disk from Pile 1 onto Pile 3; move a disk from Pile
2 onto Pile 3. A solution to the problem of moving n disks from Pile i to
Pile j amounts to constructing a word Han(n, i, j) over {a, b, c, ¯a, ¯b, ¯c}. We
do this recursively in n.
If n = 0, then there are no disks to move, so the empty word provides a
solution. Thus, let
 Han(0, i, j) = ǫ.

The solution is nearly as simple for n = 1: a single letter chosen from
{a, b, c, ¯a, ¯b, ¯c} depending on the particular values of i and j.

112 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

Figure 2.6: The Tower of Hanoi puzzle, reprinted with permis-
sion from Ed. Lucas, R´ecr´eations Math´ematiques, Editions Albert
Blanchard, Paris [Luc1893].

Otherwise, suppose the solution Han(n − 1, k, ℓ) has been constructed
for all {k, ℓ} ⊆ {1, 2, 3}. To move n disks from Pile i to Pile j, we may move
the top n − 1 disks to an intermediate pile k, move the remaining disk from
i to j, then move the n − 1 disks from k to j. That is, we deﬁne

Han(n, i, j) = Han(n − 1, i, k) Han(1, i, j) Han(n − 1, k, j).

Examples. (Refer to Figure 2.7.)

Han(1, 1, 2) = a,

2.6. THE TOWER OF HANOI 113

1
 2

3
 a

¯a
 b

¯b
c ¯c

Figure 2.7: A model for the Tower of Hanoi puzzle.

Han(2, 1, 3) = Han(1, 1, 2) Han(1, 1, 3) Han(1, 2, 3)

= a¯cb,

Han(3, 1, 2) = Han(2, 1, 3) Han(1, 1, 2) Han(2, 3, 2)

= (a¯cb)(a) Han(2, 3, 2)

= (a¯cb)(a) Han(1, 3, 1) Han(1, 3, 2) Han(1, 1, 2)

= (a¯cb)(a)(c¯ba).

Remark. This solution is optimal in the sense that it constructs a word of
minimal length that solves the Tower of Hanoi puzzle. See Exercise 2.25.

In the above examples, Han(1, 1, 2) is a preﬁx of Han(2, 1, 3) and Han(2, 1, 3)
is a preﬁx of Han(3, 1, 2). This generalizes as follows: for n even, Han(n, 1, 3)
is a preﬁx of Han(n + 1, 1, 2); for n odd, Han(n, 1, 2) is a preﬁx of Han(n +
1, 1, 3). The limit of this sequence is the Hanoi word.

Deﬁnition 2.29. The Hanoi word h is lim
n→∞ Hn, where

Hn =
 {
Han(n, 1, 3), if n is even,
Han(n, 1, 2), if n is odd.

Example. From the previous example: H1 = a, H2 = a¯cb and H3 = a¯cbac¯ba.
Here are the ﬁrst forty letters of the Hanoi word,

h = a¯cbac¯ba¯cb¯acba¯cbac¯bacb¯ac¯ba¯cbac¯ba¯cb¯acba¯cb¯a · · · .

Note that by cyclically permuting the letters a, b, c and ¯a, ¯b, ¯c simultane-
ously, the word Han(n, 1, 2) becomes Han(n, 2, 3). This observation allows
for a recursive construction of the words Hn.

114 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

Lemma 2.30. For all n ≥ 1,

Hn =
 {
Hn−1 ¯c σ(Hn−1), for n even,
Hn−1 a σ2(Hn−1), for n odd,

where σ is the permutation of {a, b, c, ¯a, ¯b, ¯c} deﬁned by

σ(a) = b, σ(b) = c, σ(c) = a, σ(¯a) = ¯b, σ(¯b) = ¯c, σ(¯c) = ¯a.

To study the structure of the Hanoi word h, it is useful to introduce two
other inﬁnite words g and b that encode the structure of h. The word g is
obtained from h by removing the bars from the barred letters of h, and b
is the binary word that records the location in h of the barred letters. We
make this explicit.
For each n ∈ N, let Gn denote the ﬁnite word over the alphabet {a, b, c}
that is the image of Hn under the morphism deﬁned by x ↦→ x and ¯x ↦→ x
for x ∈ {a, b, c}, and let Bn denote the binary word that is the image of
Hn under the morphism deﬁned by x ↦→ 0 and ¯x ↦→ 1 for x ∈ {a, b, c}. Let
g = limn→∞ Gn and let b = limn→∞ Bn.

Example. The table below lists the ﬁrst four words of the sequences (Hn)n≥1,
(Gn)n≥1 and (Bn)n≥1.

n 1 2 3 4

Hn a a¯cb a¯cb ac¯b a a¯cb ac¯b a¯cb ¯acb a¯cb
Gn a acb acb acb a acb acb acb acb acb
Bn 0 010 010 001 0 010 001 010 100 010

The table suggests that g = limn→∞ Gn has a rather simple structure.

Proposition 2.31. The word g is the periodic word (acb)∞.

Proof. From Lemma 2.30 we derive the following identity for Gn (n ≥ 1).

Gn =
 {Gn−1 c σ(Gn−1), if n is even,
Gn−1 a σ2(Gn−1), if n is odd.

Induction on n establishes that Gn is of the form (acb)ia for n odd and of
the form (acb)j for n even.

Next is a characterization of b = limn→∞ Bn using the endomorphism
ν : {0, 1}∗ → {0, 1}∗ deﬁned by ν(0) = 01 and ν(1) = 00. This morphism is
known as the period-doubling morphism.

2.6. THE TOWER OF HANOI 115

Proposition 2.32. The word b is ν∞(0). That is, b is the ﬁxed point of ν
beginning with 0.

Proof. From Lemma 2.30 we derive the following identity for Bn (n ≥ 1).

Bn =
 {Bn−11Bn−1, if n is even,
Bn−10Bn−1, if n is odd.

Deﬁne a sequence vn by
 vn =
 {
Bn0, for n even,
Bn1, for n odd,

so that Bn+1 = vnBn for all n ≥ 0. Then vn and vn+2 end in the same letter
and it follows that vn+2 = vn+1vnvn.
We also have νn+2(0) = νn+1(0)νn+1(1) = νn+1(0)νn(0)νn(0) for all
n ≥ 0. We conclude that vn = νn(0) for all n ≥ 0 since they satisfy the same
recurrence and the same initial condition (v0 = B00 = ν0(0)).
Finally, for i ∈ N ﬁxed, choose n ∈ N such that |Bn| > i. Then bi is the
letter in position i of Bn, hence it is the letter in position i of vn = νn(0).
It follows that b = limn→∞ νn(0).

It is perhaps not surprising to learn that h, g and b are k-automatic
sequences (indeed, for g and b this follows from Theorem 2.4). We leave the
veriﬁcation to the exercises, but display an automaton for b in Figure 2.8.
We conclude, as promised, with a link between the Hanoi and Thue-Morse

0 1

0
 1

0

1

Figure 2.8: The automaton for b.

words.
Since b is a ﬁxed point of the morphism ν, it immediately follows that

b2n = 0 and b2n+1 = ¯bn (2.33)

116 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

for all n ≥ 0. Comparing the Thue-Morse word t and the word b,

t = 0110100110010110100101100110100110010110 · · ·

b = 0100010101000100010001010100010101000101 · · ·

we make the following observation.

Proposition 2.34. If t is the Thue-Morse word and b = limn→∞ Bn, then

bn =
 {1, if tn+1 = tn,
0, otherwise.

Proof. We prove the equivalent statement that bn = (tn+1 + tn + 1) mod 2.
Let sn = (tn+1 + tn + 1) mod 2 for all n ≥ 0. Then working modulo 2,

s0 = t1 + t0 + 1 = 1 + 0 + 1 = 0,

s2n = t2n+1 + t2n + 1 = ¯tn + tn + 1 = 0,

s2n+1 = t2n+2 + t2n+1 + 1 = tn+1 + ¯tn + 1

= tn+1 + tn = sn − 1 = ¯sn.

Comparing with (2.33), we see bn and sn satisfy the same recurrences.

Since the Hanoi word h can be reconstructed from the words g and b, it
follows from Proposition 2.31 and Proposition 2.34 that h can be constructed
directly from the Thue-Morse word.

Theorem 2.35. The Hanoi word h is obtained from the Thue-Morse word
t by placing a bar over the n-th letter of (acb)∞ if and only if tn = tn+1.

Exercise 2.25 ([AARS1994]). This aim of this exercise is to prove that the
Hanoi word provides an optimal solution to the Tower of Hanoi problem.

(a) Let Tn = | Han(n, i, j)| for i ̸= j and n ≥ 0. Argue that Tn = 2Tn−1+1
for all n ≥ 0.

(b) Show that Tn = 2n − 1 for all n ≥ 0.

(c) Prove that Han(n, i, j) provides an optimal solution to the Tower of
Hanoi problem containing n disks. (Hint: Argue that any optimal
solution requires at least Tn disk movements.)

Exercise 2.26. Let ν(0) = 01 and ν(1) = 00, and let b = limn→∞ νn(0).
Then b satisﬁes the following for all n ≥ 0.

(a) b4n+1 = 1.

2.6. THE TOWER OF HANOI 117

(b) b4n+3 = bn.

(c) bn = 1 if and only if the binary expansion of n ends with an odd
number of 1s.

(Hint: To prove (c), show that the automaton in Figure 2.8 outputs b. Al-
ternatively, use Propositions 1.2 and 2.34.)

Exercise 2.27. The bar-free Hanoi word g = (acb)∞ is 3-automatic.

Exercise 2.28 ([AARS1994]). The Hanoi word h is a ﬁxed point of the
morphism ϕ : {a, b, c, ¯a, ¯b, ¯c}∗ → {a, b, c, ¯a, ¯b, ¯c}∗ deﬁned by

ϕ(a) = a¯c, ϕ(b) = c¯b, ϕ(c) = b¯a,
ϕ(¯a) = ac, ϕ(¯b) = cb, ϕ(¯c) = ba.

Exercise 2.29. The Hanoi word h is a 2-automatic sequence. Find a ﬁnite
deterministic automaton that outputs h.

Exercise 2.30 ([AB1992, AAB+1995]). Let s denote the word obtained
from the periodic word (101◦)∞ = 101 ◦ 101 ◦ 101 ◦ · · · over the alphabet
{0, 1, ◦} by replacing the symbols ◦ with successive terms of the word s.
Thus s begins as
 s = 101110101011101110111010101 · · · .

Prove that s = ¯b. (Hint: Show that sn = 0 if tn = tn+1 and sn = 1 otherwise.
Alternatively, note that, by construction, s4n+3 = sn, s4n = 1, s2n+2 = 1
and s4n+1 = 0 for all n ≥ 0 and use Exercise 2.26.)
(This construction is an example of a Toeplitz word or a Toeplitz sequence.
For more information see [AB1992].)

118 CHAPTER 2. COMBINATORICS OF THE THUE–MORSE WORD

Chapter 3

Square-Free Words

A ﬁnite or inﬁnite word m is called k-th-power-free if there is no word
u ̸= ǫ such that uk is a factor of m. The special case of square-free words
has been studied at least since [Thu1906], where Thue used the notion in
his study of patterns in inﬁnite words (see Chapter 5.3). We indicate some
elements of the theory below.

3.1 One example, three constructions

There are only 6 nonempty square-free words on two letters, namely

0, 1, 01, 10, 010, 101.

By contrast, there are inﬁnitely many square-free words on three letters.
Indeed, even inﬁnite ones (see Exercises 3.1 and 3.2). Below, we look at an
inﬁnite square-free word m on three letters related to the Thue-Morse word.

Construction I. (Braunholtz [Bra1963]) Starting to the right of the initial 0
in the Thue-Morse word t, record the lengths of blocks of 1s in t:

t : 011 01 0 011 0 01 011 0 · · ·
m : 2 1 0 2 0 1 2 · · ·

The word m thus constructed is square-free. Indeed, suppose u = a1 · · · an
is a word such that uu is a factor of m. Then

(0 1
a1 · · · 0 1
an ) (0 1
a1 · · · 0 1
an )0

is a factor of t, providing t with an overlap and contradicting Theorem 2.6.

119

120 CHAPTER 3. SQUARE-FREE WORDS

Construction II. (Thue [Thu1906]) It is clear from Theorem 2.6 that the
Thue-Morse word t does not have 111 as a factor. This allows us to deﬁne
m above as the (unique) preimage of t under the morphism γ : (0, 1, 2) ↦→
(0, 01, 011).

Our ﬁnal construction of m is based on two auxillary words t′ and t′′

derived from t.
Construction III. (Morse, Hedlund [MH1944]) Construct the word t′ by
reading the letters of t two at a time and converting from base 2 to base 4:
(00, 01, 10, 11) ↦→ (0, 1, 2, 3). That is, t′
n = 2tn + tn+1.

t : 0 1 1 0 1 0 0 1 1 0 0 1 0 · · ·
t′ : 1 3 2 1 2 0 1 3 2 0 1 2 · · · (3.1)

Next, construct t′′ by reducing the letters of t′ modulo 3.

t′ : 1 3 2 1 2 0 1 3 2 0 1 2 · · ·
t′′ : 1 0 2 1 2 0 1 0 2 0 1 2 · · ·

Finally, let t′′+1∞ denote the word on {0, 1, 2} deﬁned by (t′′+1∞)n ≡ t′′
n+1
mod 3.

Proposition 3.2. The words m and t′′ + 1∞ coincide.

Proof. Note that t′′
n ≡ tn+1 − tn mod 3. We claim that this expression also
equals mn − 1 mod 3, from which the desired result follows.
To prove the claim, we consider the auxiliary word p deﬁned by recording
the position of the n-th occurrence of 0 in t. That is, pn = N if tN = 0 and
|t0t1 · · · tN −1|0 = n − 1:
 t : 0 1 1 0 1 0 0 1 1 0 · · ·
p : 0 3 5 6 9 · · ·

From the deﬁnition of the Thue-Morse word, we know that

pn =
 {
2n, if tn = 0
2n + 1, otherwise. (3.3)

In other words, pn = 2n + tn. Evidently, mn equals 0, 1 or 2 according
to whether pn+1 − pn − 1 equals 0, 1 or 2 (see Figure 3.1). But this last
expression is also equal to the value of tn+1 − tn + 1, proving the claim.

We conclude with alternative constructions of t′ and t′′, in the spirit of
Proposition 1.5.

3.1. ONE EXAMPLE, THREE CONSTRUCTIONS 121

t : 0 1 1 0 1 0 0 1 1 0 · · ·
p : 0 3 5 6 9 · · ·

m : 2 1 0 2

Figure 3.1: Deﬁning p by pn = 2n + tn, the relationship between
t, p and m is uncovered.

Proposition 3.4 (Morse, Hedlund [MH1944]). The endomorphism α of
words over the alphabet {0, 1, 2, 3} deﬁned by α : (0, 1, 2, 3) ↦→ (12, 13, 20, 21)
satisﬁes t′ = α∞(1).

Proof. The proof rests on the following identity (see Exercise 3.5):
[µn(0)1
]′ = α
n(1) for all n ≥ 0,

where µ is the Thue-Morse morphism and [µn(0)1]′ denotes the word con-
structed from µn(0)1 in the same manner that t′ is constructed from t (read-
ing two letters at a time and converting from base 2 to base 4).

Example. Taking n = 2, we have µ2(0)1 = 01101, [01101
]′ = 1321 and
α2(1) = α(13) = 1321.

Continuing with the proof, we prove that µn(0)1 is a preﬁx of t for all n.
Indeed, we have seen that t = µ∞(0) and moreover µn+1(0) = µn(0)µn(1),
since µ is a morphism. Since µn(1) begins in 1, the result follows. Using
the identity above, we conclude that αn(1) is a preﬁx of t′, ﬁnishing the
proof.

Let β be the endomorphism of {0, 1, 2, 3}∗ deﬁned by β : (0, 1, 2, 3) ↦→
(0, 1, 2, 0). An immediate corollary of Proposition 3.4 is that t′′ = β(α∞(1)
).
We use this fact to prove a diﬀerent characterization of t′′ due to Marshall
Hall [Hal1964]. We call the endomorphism σ that he uses the morphism
of Hall in what follows.

Proposition 3.5 (Hall [Hal1964]). Let σ denote the morphism on {0, 1, 2}∗

deﬁned by σ : (0, 1, 2) ↦→ (12, 102, 0). Then t′′ = σ∞(1).

Proof. The proof rests on the altogether not obvious identities of Exercise
3.6, which may be proved by parallel induction on n:

σn+1(0) = β(α
n(12)
),

122 CHAPTER 3. SQUARE-FREE WORDS

σn+1(1) = β(α
n(132)
),

σn+1(2) = β(α
n(0)
).

The proof is now immediate, for we have

σn+2(1) = σn+1(102) = βα
n(132120)

= βα
n+1(132) = βα
n+2(1)βα
n+1(2).

In particular, σn and βαn have common preﬁxes of strictly increasing lengths
for all n ≥ 2.

Remark. The Thue-Morse word and its derivatives are not the only inﬁnite
words the reader has seen that can be described as the ﬁxed point of a
morphism. See Exercise 3.7 for a Fibonacci example.

Exercise 3.1 ([Lot1997, Lemma 2.1.2]). Fix an alphabet A and let P be a
property of elements of A∗ which is closed under taking factors. Show that
the following two statements are equivalent if and only if A is ﬁnite.

(a) The set LP of words w ∈ A∗ having propery P is inﬁnite.
(b) There exists an inﬁnite word w on A whose (ﬁnite) factors all have
property P.

Exercise 3.2 ([MH1944]). For each inﬁnite word a = a0a1 · · · on A =
{a, b}, deﬁne an inﬁnite word b = b0b1 · · · on B = {a, b, c} by

bn =
 



a, if anan+1 ∈ {aa, bb},
b, if anan+1 = ab,
c, if anan+1 = ba.

Prove that if a is overlap-free, then b is square-free.

Exercise 3.3. Show that t′ and t′′ are square-free. (Hint: Use Exercise 3.2
with a = t.)

Exercise 3.4 ([AARS1994]). Show that the Hanoi word h (Deﬁnition 2.29)
is square-free.

Exercise 3.5. Complete the proof of Proposition 3.4. That is, verify the
identity [µn(0)1
]′ = αn(1). (Hint: A proof by induction seems natural. You
may want to simultaneously verify
[µn(0)0
]′ = α
n(0), [µn(1)0
]′ = α
n(2), [µn(1)1
]′ = α
n(3),

where given a word w, the word w′ is built as in (3.1) by reading the letters
of w two at a time and converting from binary.)

3.2. SQUARE-FREE MORPHISMS AND CODES 123

Exercise 3.6. Given α, β and σ as in Proposition 3.5, verify that the
identities below hold for all n:

σn+1(0) = β(α
n(12)
), σn+1(1) = β(α
n(132)
), σn+1(2) = β(α
n(0)
).

Exercise 3.7. Let Φ denote the composition E◦D of Christoﬀel morphisms
from Chapter 2 of Part I, i.e., (x, y) Φ
↦→ (xy, x). Prove that Φ∞(x) is the
Fibonacci word f deﬁned in Exercise 1.5 of Part I.

Exercise 3.8. An automaton for t′.

(a) Prove that the automaton in Figure 3.2 outputs the word t′. (Hint:
Use the argument in the proof of Theorem 2.4 and Proposition 3.4.)

0 1

2 3
 0

0
 11 11

0

0

Figure 3.2: An automaton that outputs t
′.

(b) Develop a combinatorial characterization of t′
n based on the binary
expansion of n. (Hint: By deﬁnition, t′
n = 2tn + tn+1, so t′
n is either
0 or 1 if tn = 0 and is either 2 or 3 if tn = 1.)

3.2 Square-free morphisms and codes

A morphism h : A∗ → B∗ is a square-free morphism, or more simply
h is square-free, if for every square-free word w over A, the image h(w)
is square-free over B. Exercise 3.10 indicates a strong connection between
square-free morphisms and the more general notion of k-th power–free mor-
phisms.
Evidently, the trivial morphism h : A∗ → {ǫ} is square-free. We rule out
this case in what follows; by “morphism” we shall always mean “nontrivial
morphism.”
A complete characterization of square-free morphisms does not exist,

124 CHAPTER 3. SQUARE-FREE WORDS

though Maxime Crochemore [Cro1983b] showed that the monoid of square-
free morphisms is not ﬁnitely generated.1 One evident fact is the following.

Proposition 3.6. If h : A∗ → B∗ is a square-free morphism and if h∞(a)
exists for some a ∈ A, then h∞(a) is a square-free word.

Remark. The converse to this proposition is false, as veriﬁed by the mor-
phism of Hall: we have seen that σ∞(1) = t′′ is square-free, and clearly 101
is square-free, but σ(101) = 1 0 2 1 2 1 0 2 is not.

Short of demanding square-freeness, one might ask if h is at least k-
square-free: a morphism h is called k-square-free if it preserves the square-
free property of words of length at most k. This notion was introduced in
developing criteria to test whether or not h is square-free. Early results in
this direction include the following.

Proposition 3.7 (Crochemore [Cro1982]). If |A| = 3, a morphism h : A∗ →
B∗ is square-free if and only if h is 5-square-free.

This leads naturally to the notion of test sets: a set T ⊆ A∗ is a test
set for the square-freeness of h if one may deduce that h is square-free by
checking that h(t) is square-free for all t ∈ T . The proposition states that a
test set for “ternary morphisms” is the set of all square-free words on three
letters of length at most ﬁve. Fortunately, each such word is a factor of a
square-free word of length equal to ﬁve, so a minimal test set contains a
quite manageable thirty elements. (See Exercise 3.9.)

Theorem 3.8 (Crochemore [Cro1982]). A morphism h : A∗ → B∗ is square-
free if and only if it is k-square-free for

k = max {
3, 1 + ⌈ M (h) − 3
m(h)
 ⌉} ,

where ⌈-⌉ is the ceiling function, M (h) = max{|h(a)| : a ∈ A} and m(h) =
min{|h(a)| : a ∈ A}.

Example. If h is a uniform morphism, then M (h) = m(h) and k = 3. The
theorem then reads, “3-square-free uniform morphisms are square-free,” a
statement which also follows from Theorem 3.11 below.

1More generally, the monoid of k-th-power-free morphisms (k ≥ 3) and overlap-free
morphisms are also not ﬁnitely generated. (See [RW2002] and [Ric2003].)

3.2. SQUARE-FREE MORPHISMS AND CODES 125

Crochemore’s theorem gives an upper bound on the size of test sets in
the general case. See also [HYY2003], where Hung-Kuei Hsiao, Yow-Tzong
Yeh and Shyr-Shen Yu give a similar test set involving

max {k : h(a) ∩ B∗h(A
k)B∗ ̸= ∅
} .

A more precise description of test sets, at least in the setting of k-th-power-
free morphisms (k ≥ 3), has been undertaken by Gw´ena¨el Richomme and
Francis Wlazinski [RW2004, RW2007].
The balance of this chapter is devoted to two important k-square-free
tests for a morphism to be square-free. We begin with some elementary
properties of square-free morphisms.

Lemma 3.9. Let h : A∗ → B∗ be a (nontrivial) morphism, and let C denote
the set of images {h(a) : a ∈ A}. If h is square-free, then:

(i) h is nonerasing,

(ii) h is injective on its alphabet,

(iii) no element c ∈ C is the preﬁx of another element c′ ∈ C,

(iv) no element c ∈ C is the suﬃx of another element c′ ∈ C.

Proof. (i): Suppose that h is erasing (i.e., there is a letter a ∈ A with
h(a) = ǫ). Since h is not the trivial morphism, there is some b ∈ A such
that h(b) ̸= ǫ. But then, bab is square-free while h(bab) = h(b)h(b) is not
square-free.

(iii): Suppose a, b ∈ A and x ∈ B∗ are such that h(b) = h(a)x. Then
h(ab) = h(a)h(a)x fails to be square-free.

(ii) & (iv): Follow the proof of (iii).

After the lemma, we may restrict our search for square-free morphisms
to nonerasing injective morphisms h. If, moreover, h is 2-square-free, then
the proof of the lemma realizes h(A) as a code in B∗.

Deﬁnition 3.10. A code over an alphabet B is a set of words C ⊆ B∗

such that every w ∈ C ∗ has a unique factorization w = (c1, c2, · · · , cr) with
cj ∈ C.

In the context of codes, Properties (iii) and (iv) of the above lemma
are the deﬁnitions of preﬁx code and suﬃx code: we say that a code C is
a preﬁx code (respectively, suﬃx code) if no element of C is the preﬁx
(respectively, suﬃx) of another element of C. A code C that is both a preﬁx

126 CHAPTER 3. SQUARE-FREE WORDS

code and a suﬃx code is called a biﬁx code. If, moreover, no element of
C is a factor of another element of C, then C is called an inﬁx code. An
important class of inﬁx codes are uniform codes, that is, codes C whose
elements have a common length.
Examples. The (nonuniform) code {01, 12, 0210} is inﬁx while the code
{0, 101} is not. The code {01, 02, 12} is uniform, while {10, 01, 11, 00, 10011}
is not even a code.
As we will focus our attention on (nonerasing, injective) 2-square-free
morphisms, we freely use the language of codes in what follows. Moreover,
if h : A∗ → B∗ is a morphism giving rise to a code (that is, C(h) := h(A)
is a code in B∗), then we transport properties naturally deﬁned for C to h
and vice versa. For example, we speak freely below of “k-square-free codes”
(a code coming from a k-square-free morphism) and “inﬁx morphisms” (a
morphism whose associated code is inﬁx).

Exercise 3.9. A few square-free facts about ternary alphabets A:

(a) Every square-free word over A of length less than ﬁve appears as a
preﬁx of some square-free word over A of length ﬁve.

(b) There are 30 square-free word of length ﬁve.

(c) There are square-free words in A7 which cannot be extended to longer
square-free words. Seven is the minimal integer with this property.

Exercise 3.10 ([BEM1979]). A nonerasing morphism h : A∗ → B∗ is said
to be k-th-power-free if h(w) is k-th-power-free for each k-th-power-free word
w. Show that if h is a square-free morphism such that

(a) h(A) is inﬁx, and

(b) if |h(a)| > 1 then h(a) does not begin and end in the same letter,

then h is k-th-power-free for all k ≥ 2.

3.3 A 3-square-free test for square-freeness

Our ﬁrst theorem goes back to Axel Thue’s work. It has also been given
in the paper by Dwight Bean, Andrzej Ehrenfeucht and George McNulty
[BEM1979].

Theorem 3.11. A 3-square-free inﬁx morphism is square-free.

In particular, inﬁx morphisms have a test set composed of square-free
words of length at most 3. Before starting the proof, we consider a notion
closely related to inﬁx.

3.3. A 3-SQUARE-FREE TEST 127

Deﬁnition 3.12. A code C is comma-free if for all ucv ∈ C ∗, with c ∈ C,
one has u, v ∈ C ∗.

Example. The code {0121, 01021, 20102} is comma-free. (This is more easily
seen after the forthcoming lemma.) The Thue-Morse morphism µ : (0, 1) ↦→
(01, 10) is not comma-free because µ(00) = 0101 = 0µ(1)1.

Lemma 3.13. A comma-free code is inﬁx. Conversely, a 2-square-free inﬁx
code is comma-free.

Proof. Let C = C(h) be a comma-free code associated to some morphism
h : A∗ → B∗. Assume that ucv ∈ C for some c ∈ C. Since C is comma-free,
this implies u, v ∈ C ∗, and since C is a code, this forces u = v = ǫ.
Conversely, suppose C is 2-square-free and inﬁx. Consider a word ucv ∈
C ∗ with c ∈ C and u, v ∈ B∗. Then ucv = c0 · · · cn for unique c0, . . . , cn ∈ C.
First, we establish the factorization in Figure 3.3 for some 0 ≤ j < n and
c′, v′ ̸= ǫ.
 c0 · · · cj cj+1 · · · cn
u c v

u
′′ c
′ c
′′ v′

Figure 3.3: A factorization as ucv of a word c0 · · · cn in C∗ for a
2-square-free inﬁx code C.

The index j is chosen so that |c0 · · · cj−1| ≤ |u| < |c0 · · · cj|. By the inﬁx
property of C, c cannot be a factor of cj, so there are two cases: (i) c and
cj begin and end at the same point within ucv, or (ii) the preﬁx uc eclipses
the right edge of cj. In the latter case, again because C is inﬁx, cj+1 cannot
end before (or at) the end of c. So we have factorizations

cj = u′′c
′ c = c
′c
′′ cj+1 = c
′′v′

for some words u′′, c′, c′′, v′ ∈ B∗, with c′, v′ ̸= ǫ.
Noting that cjc contains a square, we deduce by the 2-square-free prop-
erty of C that cj = c. The ﬁrst case above then satisﬁes u, v ∈ C ∗ and we
are done.
In the remaining case (u′′ and c′′ are both nonempty), we see that ccj+1
also contains a square (forcing cj = c = cj+1). We further suppose that |c′| >
|c′′| (assuming |c′| ≤ |c′′| instead, one reaches the same conclusion). Since c′

is a suﬃx of cj = c, we see that c′′ is a suﬃx of c′. Thus c = c′c′′ = xc′′c′′

(for some x ∈ B∗) contains a square and C is not even 1-square-free.

128 CHAPTER 3. SQUARE-FREE WORDS

Proof of Theorem 3.11. Suppose h : A∗ → B∗ is a 3-square-free inﬁx mor-
phism and set C = C(h). Assume the result is false and let w = a0a1 · · · an
(ai ∈ A) be a shortest square-free word such that h(w) contains a square uu
(u ∈ B∗ \ {ǫ}). We have n ≥ 3 by hypothesis.
Writing h(ai) = ci, we may assume that the product uu starts at the
beginning of or within c0 and ends within or at the end of cn (otherwise
we could have chosen a shorter word w). We claim that the factorization in
Figure 3.4(a) cannot happen and that the true picture is Figure 3.4(b) for
some 0 < j < n.

c0 · · · cn
u u

(a) u is a factor of c0.
 c0 · · · cj · · · cn
u u

(b) cj straddles the factorization uu.

Figure 3.4: Potential instances of the square uu within h(w).

Indeed, if the ﬁrst picture holds true, one would have c1 as a factor of
u (since n > 1), and hence as a factor of c0, violating the inﬁx property of
C. Turning to the second picture, we reﬁne it by introducing factorizations
cj = ps, c0 = p′s′ and cn = p′′s′′ as in Figure 3.5 (with s′, p, p′′ ̸= ǫ).

p′ s′ p s p′′ s′′
c0 · · · cj · · · cn
u u

Figure 3.5: An instance of the square uu within h(w).

Note that either c1 or cn−1 is a factor of u (since n ≥ 3). Say we are in
the ﬁrst case (the other one being symmetric). Then

cj · · · cn = pus′′ = ps′c1 · · · cj−1ps′′.

Moreover, since C is a comma-free code by Lemma 3.13, the factoriza-
tion (ps′)c1(c2 · · · cj−1ps′′) ∈ C ∗ means that ps′ ∈ C ∗ \ {ǫ}. Writing ps′ =
c′c′′ · · · c(r), there are four cases to consider. See Figure 3.6.

p s′

c
′

(a) ps′ ∈ C.
 p s′

c
′ c
′′

(b) p, s′ ∈ C.
 p s′

c
′ · · ·

(c) p begins in c
′.
 p s′

· · · c
(r)

(d) s′ ends in c
(r).

Figure 3.6: Possible factorizations of ps′ inside C∗.

3.4. A 2-SQUARE-FREE TEST 129

Cases (c) and (d) of Figure 3.6 are excluded because C is biﬁx. that is,
because c′ is a preﬁx of cj and c(r) is a suﬃx of c0, respectively.
In Case (b), one has p = c′ = cj and s′ = c′′ = c0 (since C is biﬁx).
Moreover, p′ = ǫ and s = ǫ. We now have the factorizations

u = c0c1 · · · cj = cj+1 · · · cn−1p′′,

or c0c1 · · · cjs′′ = cj+1 · · · cn. The preﬁx property of C then gives us that
s′′ = ǫ and p′′ = cn. Indeed, c0 is a preﬁx of cj+1 (or vice versa) and hence
they are equal. Continuing this line of reasoning, peeling oﬀ the left-most ci
at each step, we are left with one of three possibilities depending on whether
n − j is less than, equal to or greater than j + 1:

cℓ · · · cjs′′ = ǫ s′′ = ǫ ǫ = cℓ · · · cn−1p′′.

Since h is nonerasing, the only allowable result above is the middle one. So
we conclude that p′′ = cn, n = 2j + 1 and ck = cj+1+k for 0 ≤ k ≤ j, i.e., w
is a square.
In Case (a) of Figure 3.6, we have c′ = ps′ = cj (C is preﬁx) and s = s′.
It follows that c1 · · · cj−1p = cj+1 · · · cn−1p′′,

or c1 · · · cj−1 = cj+1 · · · cn−1 and p = p′′, because C is preﬁx. Moreover, since
h(ai) = ci and h is injective on its alphabet, we have

a1 · · · aj−1 = aj+1 · · · an−1.

We use this equality to show that w contains a square. Towards this end,
notice that h(a0ajan) = c0cjcn = p′spsps′′ contains a square. It follows from
the 3-square-free property of h that a0ajan contains a square, thus a0 = aj
or aj = an. In both cases, the word

w = a0 · · · an = a0(
a1 · · · aj−1)aj(a1 · · · aj−1)an

contains a square, contradicting our assumptions on w.

3.4 A 2-square-free test for square-freeness

Our next theorem is due to Pavel Goralˇc´ık and Tomas Vanicek. Before stat-
ing it, we need to introduce two more properties of codes in the spirit of
inﬁx.
 130 CHAPTER 3. SQUARE-FREE WORDS

Deﬁnition 3.14. A code C ⊆ B∗ is a preﬁx-suﬃx code, or a ps-code,
if for every c ∈ C and every factorization c = ps in B∗, either c is the only
word in C starting in p or c is the only word in C ending in s. That is,

ps, p′s, ps′ ∈ C =⇒ p′ = p or s′ = s .

Note that we have allowed for trivial factorizations ps = pǫ or ps = ǫs
above. In particular, ps-codes are biﬁx. The term ps-code was introduced in
the thesis of Veikko Ker¨anen. See also [Ker1986, Ker1987]. The notion has
also been used by Michel Leconte (e.g., [Lec1985]), who calls such a code
faithful.

Example. The codes {012, 120, 201} and {012, 02122, 021102} are ps-codes,
while {0, 12, 102} and {112, 0120, 012012} are not.

Given a code C ⊆ B∗ and an element w ∈ B∗ (not necessarily in C), we
say w is left synchronizing (in C) if for every u, v ∈ B∗ with uwv ∈ C ∗,
one has u ∈ C ∗. The right synchronizing property is analogously deﬁned.
The property of codes we need is that of strongly synchronizing: a code C is
called strongly synchronizing if for every c ∈ C and every factorization
c = ps ∈ B∗, p is left synchronizing or s is right synchronizing.

Remark. This may be compared to the more prevalent notion of synchro-
nizing codes C: for all c ∈ C and ucv ∈ C ∗, one has uc, cv ∈ C ∗. See
[BP1985, Chapter VII.2] for more details. A strongly synchronizing code is
comma-free and so synchronizing (Exercise 3.11). It is also inﬁx (Lemma
3.13).

The condition of being strongly synchonizing seems rather diﬃcult to
check. Goralˇc´ık and Vanicek [GV1991] call a code bissective if it is a
strongly synchronizing ps-code.

Theorem 3.15. If a strongly synchronizing ps-morphism is 2-square-free,
then it is square-free.

Proof. A strongly synchronizing morphism h : A∗ → B∗ is inﬁx (Exercise
3.11 and Lemma 3.13). If we can show that h is also 3-square-free, then
Theorem 3.11 ﬁnishes the proof for us. Let C denote the code C(h) and
suppose we are given a word w = a1a2a3 (ai ∈ A) such that h(w) contains
the square uu for some u ∈ B∗ \ {ǫ}. We argue that w contains a square.
Write x = h(a1), y = h(a2) and z = h(a3). We begin by reducing the
problem to the situation illustrated in Figure 3.7.
If uu is a factor of xy, then h(a1a2) = xy contains a square. Since h is
2-square-free, a1 must equal a2 and w contains a square. Similarly, if uu is
a factor of yz, then w contains a square.

3.4. A 2-SQUARE-FREE TEST 131

p′ s′ p s p′′ s′′
x y z
u u

Figure 3.7: Factorizations of the code words x, y, z ∈ C and the
square uu ∈ B∗ inside the product xyz.

Suppose uu is neither a factor of xy nor of yz. If u is a factor of x, then
y is a factor of the second u, which implies y is a factor of x. Since C is inﬁx,
x = y, and w contains a square because h is 2-square-free. Similarly, if u is
a factor of z, then w contains a square.
We thus have the situation depicted in Figure 3.7, with s′, p, s, p′′ ̸= ǫ.
In particular, we learn that

xy = p′s′ps = p′sp′′s, (3.16)

yz = psp′′s′′ = ps′ps′′. (3.17)

As h is strongly synchronizing and y = ps ∈ C, there are two cases to
consider: p is left synchronizing or s is right synchronizing.
In the ﬁrst case, (3.17) gives ps′ ∈ C ∗. So we have ps ∈ C and ps′ =
c1 · · · cr ∈ C ∗ (ci ∈ C). Since psp′′ = ps′p, either c1 is a preﬁx of ps or vice
versa, both possibilities forcing s′ = s by the preﬁx property of C. Then
(3.17) shows that p′′ = p. In the second case, (3.16) gives p′′s ∈ C ∗, from
which one also learns that p′′ = p and s = s′.
We now have y = ps, x = p′s, z = ps′′ ∈ C,

which in turn implies either p′ = p or s′′ = s (as C is a ps-code). In other
words x = y or z = y, which shows that w = xyz contains a square.

Exercise 3.11. Prove that a strongly synchronizing code C ⊆ B∗ is both
synchronizing and comma-free. (Hint: There are two cases to consider: either
C is the entire alphabet B or it is not.)

132 CHAPTER 3. SQUARE-FREE WORDS

Chapter 4

Squares in Words

This chapter deals with occurrences of squares in ﬁnite words. We begin by
providing bounds for the number of occurrences of squares of primitive words
and for the number of distinct squares in a ﬁxed ﬁnite word. The remain-
der of the chapter is devoted to describing a linear-time algorithm to test
whether a word contains a square. The necessary ingredients include cen-
tered squares, preﬁx arrays, the Crochemore factorization and suﬃx trees.

4.1 Counting squares

Here we establish bounds on the number of occurrences of squares of prim-
itive words and the number of distinct squares in a ﬁxed ﬁnite word.

Example. The word aaaaaa contains three squares: aa, aaaa, aaaaaa. Only
aa is a square of a primitive word, and it appears 5 times in aaaaaa.

Example. Let w = abaababaabaab. There are eight words whose squares
occur in w: a; ab; ba; aba; baa; aab; abaab; and baaba. They are all primitive.
The squares for a and aba occur thrice and twice, respectively.

Preﬁxes play an important role in dealing with squares, so we introduce
the preﬁx poset of an alphabet.

Deﬁnition 4.1. Given an alphabet A, the preﬁx poset PA = (A∗, <) is
the poset deﬁned by the order relation x ≤ y if x is a preﬁx of y. The poset
contains a unique minimal element ǫ and is ranked by word length.

The explicit poset structure of PA will play a role in Chapter 4.5. Here,
we use only the ordering relation to help establish the desired bounds on
squares in a word. The following result, due to Maxime Crochemore and
Wojciech Rytter [CR1995, Lemma 10], will also be useful.

133

134 CHAPTER 4. SQUARES IN WORDS

w w
v v
u u

v u

(a) w is a preﬁx of vu.
 w w
v v
u u

v u

(b) vu is a preﬁx of w.

Figure 4.1: The Three Squares Lemma says (a) is impossible
when u is primitive.

Lemma 4.2 (Three Squares Lemma). Let u, v and w be words such that
uu < vv < ww. If u is primitive, then |u| + |v| ≤ |w|.

Proof. Suppose u, v and w are three words such that uu < vv < ww with
|w| < |u| + |v|. We will show that u is not primitive. We begin by arguing
for the situation illustrated in Figure 4.2.

w
v t r
u u

Figure 4.2: Proof of the Three Squares Lemma.

Since vv < ww, we must have v < w as well, so write w = vt (t ̸= ǫ). Note
that vt is a preﬁx of vv because both are preﬁxes of ww and |vt| = |w| < |vv|.
It follows that t is a preﬁx of v. Since u is also a preﬁx of v, we have either
u ≤ t or t < u. The ﬁrst case would imply |w| = |vt| = |t| + |v| ≥ |u| + |v|,
contradicting our hypothesis. Therefore, u = tr for some r ̸= ǫ. Finally, r is
also a preﬁx of w because wr is a preﬁx of ww (since wr = vtr = vu and vu
is a preﬁx of vv, which is a preﬁx of ww).
Case I: |u|+|t| > |v|. Then vv is a preﬁx of wu, since |wu| = |vtu| > |vv|.
Write v = us for some nonempty word s. We are in the situation illustrated
in Figure 4.3. We show that u is not primitive in 6 steps.
1. u begins with rs and sr. In particular, sr = rs.
Since wrs = vtrs = vus = vv and vv < ww, it follows that wrs is a
preﬁx of ww of length |vv|. Also, wu is a preﬁx of ww and |wu| > |vv|.
Hence, wrs is a preﬁx of wu, which implies that u begins with rs. So write
u = rsu′. Then uu is a preﬁx of vu (since uu < vv and |u| < |v|) and
vu = usu = usrsu′. Hence, u is a preﬁx of srsu′, so u also begins with sr.

2. r = zλ and s = zν for some word z and some λ, ν ∈ N.

4.1. COUNTING SQUARES 135

w r
v t u
u s u s

t r u r

Figure 4.3: Case I in the proof of the Three Squares Lemma.

This follows from Step 1 and Exercise 4.3.

3. zu = uz′ for some conjugate z′ of z.
Since v = us, it follows that uu is a preﬁx of vu = usu. So u is a preﬁx
of su. Let s′ be the word such that su = us′. Exercise 4.4 and Step 2 imply
zu = uz′.

4. ru = ur′ for some word r′.
This follows from Step 2 and Step 3.

5. rt = tr.
Observe that vu is a preﬁx of wu since both words are preﬁxes of ww
(because u < v < w) and |vu| < |vv| < |wu|. Thus vu is a preﬁx of vtu since
wu = vtu. It follows that u is a preﬁx of tu. Write tu = ut′ for some word
t′. Combined with Step 4, we have rtu = rut′ = ur′t′ = trr′t′.

6. u is not primitive.
By Step 5 and Exercise 4.3, there exists a nonempty word p and non-
negative integers α and β such that r = pα and t = pβ. Since r and t are
nonempty, α + β ≥ 2. Hence, u = tr = pα+β is not primitive.

Case II: |u|+|t| ≤ |v|. This case is illustrated in Figure 4.4, and is argued
as in Case I. The proof is left to Exercise 4.7.

w r
v t u
u t v
t u

Figure 4.4: Case II in the proof of the Three Squares Lemma.

Remark. The primitive condition in the Three Squares Lemma is necessary:
consider u = a3, v = a4 and w = a5.

136 CHAPTER 4. SQUARES IN WORDS

Our ﬁrst application of the Three Squares Lemma concerns the number
of squares of primitive words occurring in a ﬁnite word. This also appears
in [CR1995].
For the convenience of the reader we recall the deﬁnition of big-O nota-
tion. Given two functions f, g : N → R>0, write f (n) = O (g(n)) if there
exist a positive integer N and a positive constant c such that f (n) ≤ cg(n)
for every n ≥ N . That is, g(n) is an asymptotic upper bound for f (n).

Theorem 4.3. The number of occurrences of squares of primitive words in
a word of length n is O (n log n).

Proof. We argue that the number of squares of primitive words that start
in position i is always at most logφ(n) + 1, where φ = 1+√5
2 is the golden
ratio.
Let w be a word of length n and let y1 < y2 < · · · < yk be the primitive
words such that y2
1, y2
2, . . . , y2
k begin in position i. Repeated application of
the Three Squares Lemma gives that |yj| ≥ |yj−1| + |yj−2| for all 3 ≤ j ≤ k.
Since |y1| ≥ 1 and |y2| ≥ 2, it follows that n = |w| ≥ |yk| ≥ Fk+1, where
Fk+1 is the (k + 1)-st Fibonacci number. This, in turn, is greater φk−1 (see
Exercise 4.9), thus k ≤ logφ(n) + 1.

Remark. As shown in [Cro1981, Lemma 10], the bound provided in Theorem
4.3 is optimal and obtained by the preﬁxes of the Fibonacci word f of length
Fk (the so-called “Fibonacci words,” see Exercises 4.12 and 4.13).

Our second application of the Three Squares Lemma concerns the num-
ber of distinct squares in a word. It comes in the proof of the following
theorem due to Aviezri S. Fraenkel and Jamie Simpson [FS1998].

Theorem 4.4. Any word of length n contains at most 2n distinct squares.

Proof. Let m be a word of length n. For 0 ≤ i ≤ n − 2, denote by si
the number of squares in m starting at position i that have no occurrence
starting at a position greater than i. We are interested in the number s0 +
s1 + · · · + sn−2. We will prove that si ≤ 2 for each i.
Suppose on the contrary that si ≥ 3. Then there exist three distinct
words u, v and w with uu < vv < ww such that uu, vv and ww begin at
position i and have no occurrence starting at a position greater than i.
If u is primitive, then the Three Squares Lemma implies |w| ≥ |u| + |v| >
2|u| = |uu|. Hence uu is a proper preﬁx of w. This implies that there is an
occurrence of uu beginning at position i + |w|, a contradiction.
If u is not primitive, then u = yk for some primitive word y and some
k ≥ 2. So yy < vv < ww since yy is a proper preﬁx of uu. By the Three

4.1. COUNTING SQUARES 137

Squares Lemma, |w| ≥ |v| + |y|. We may assume that |uu| > |w| because
otherwise there is another occurrence of uu in m at a position greater than
i. Therefore, w is a common preﬁx of y2k and vv such that |w| ≥ |v| + |y| >
|v| + |y| − gcd(|v|, |y|). By the Fine-Wilf Theorem (Exercise 4.5), the words y
and v are integer powers of some nonempty word. Since y is primitive, this
word is y. Thus v = yℓ for some ℓ > k. Therefore, vv = y2ℓ = y2ℓ−2ky2k =
y2ℓ−2kuu. Since vv begins at position i, it follows that uu also begins at
position i + (2ℓ − 2k)|y| > i. This is a contradiction.

Remarks. 1. Lucian Ilie recently proved a three overlap lemma similar in
spirit to the Three Squares Lemma and used it to show that the number
of squares occurring in a word of length n is bounded by 2n − O (log n)
[Ili2007].
2. It has been conjectured that the 2n in the statement of Theorem 4.4 may
be replaced by n [FS1998, Lot2005, Ili2007]. In some sense, this is the best
one can hope for: Fraenkel and Simpson construct a sequence of words—
described in Exercise 4.8—where the number of squares in each word is very
close to the length of the word.

Exercise 4.1 (Levi’s Lemma). Let u, v, x, y ∈ A∗ and suppose uv = xy.

(a) If |u| ≥ |x|, then there exists t ∈ A∗ such that u = xt and y = tv.

(b) If |u| < |x|, then there exists t ∈ A∗ \{ǫ} such that x = ut and v = ty.

Exercise 4.2. Let y ∈ A∗ and x, z ∈ A∗ \ {ǫ}. If xy = yz, then there
exist words u, v ∈ A∗ and an integer p ≥ 0 such that x = uv, z = vu
and y = (uv)pu = u(vu)p. (Hint: Proceed by induction on |y| using Levi’s
Lemma above.)

Exercise 4.3. If xy = yx for some words x, y ∈ A∗, then there exists a
word z ∈ A∗ and nonnegative integers k and l such that x = zk and y = zl.
(Hint: Proceed by induction on |xy|.)

Exercise 4.4. Let x, y, z be words over some alphabet A. If zlx = xy for
some positive integer l, then zx = xz′ for some conjugate z′ of z.

Exercise 4.5 (Fine-Wilf Theorem). Let u, v ∈ A∗. There exists w ∈ A∗ \{ǫ}
such that u, v are integer powers of w if and only if there exist i, j ≥ 0 so that
ui and vj have a common preﬁx (or suﬃx) of length |u| + |v| − gcd(|u|, |v|).

Exercise 4.6 (Synchronization). If u is a primitive word, then there are
exactly two occurrences of u in the word uu (as a preﬁx and as a suﬃx).

138 CHAPTER 4. SQUARES IN WORDS

Exercise 4.7. Complete Case II in the proof of Three Squares Lemma by
arguing |u| + |t| ≤ |v| implies u is not primitive. (Hint: The situation is
depicted in Figure 4.4; argue as in Case I.)

Exercise 4.8 ([FS1998]). For each m ∈ N, let Qm denote the concatenation
of 00101001, 00010010001, . . . , and 0m+110m10m+11. For example, Q1 =
00101001 and Q2 = 0010100100010010001. Show that the number of squares
having at least one occurrence in Qm is very close to |Qm| by proving the
following.

(a) The length of Qm is 3m2+13m
2 .

(b) The number of squares in Qm is 3m2+7m−6
2 + ⌊ m+1
2 ⌋.

Exercise 4.9. Recall that the Fibonacci numbers are deﬁned by F0 = 1,
F1 = 1 and Fn = Fn−1 + Fn−2 for all n ≥ 2. Prove that Fn > φn−2

for all n ≥ 2, where φ = 1+√5
2 . (Hint: Recall that φ satisﬁes a quadratic
polynomial.)

4.2 Centered squares

The results in this and the next two sections may be found in the book by
Maxime Crochemore, Christophe Hancart and Thierry Lecroq [CHL2001,
CHL2007].

Given a factorization w = (u, v) ∈ A∗, a centered square at (u, v) is
a factor rsrs of w, with rs ̸= ǫ, such that either: u = αrsr and v = sβ for
some α, β ∈ A∗; or u = αr and v = srsβ for some α, β ∈ A∗. See Figure
4.5. In the former case we say that rsrs is a left-centered square of w at
(u, v) and in the latter case we say that rsrs is a right-centered square
of w at (u, v).
In developing an algorithm for testing square-freeness, one could start
with a “divide and conquer” method: given a word w, choose a factorization
w = (u, v) and look for centered squares at (u, v), as illustrated in Figure
4.5; if no centered square is found, then repeat the method for the words
u and v. We begin by observing that no cavalier implementation of this
method can possibly run in linear time.
Let TC(|u|, |v|) denote the time it takes to test for a left-centered square
in uv at (u, v). Using the divide and conquer method, the computation time
T (n) for testing square-freeness of a word of length n is

T (n) = T (⌊ n
2
 ⌋) + T (⌈ n
2
 ⌉) + TC(⌊ n
2
 ⌋ , ⌈ n
2
 ⌉) .

4.2. CENTERED SQUARES 139

u v

α r s r s β

w

Figure 4.5: The divide and conquer method for ﬁnding squares.

We show in Section 4.3 that TC(|u|, |v|) is linear in |uv|, meaning that the
divide and conquer algorithm only yields T (n) = O (n · log n). Nevertheless,
the notion of centered squares can be exploited to build a linear-time test
for square-freeness. We establish this in Section 4.4.

Lemma 4.5. A word uv has a left-centered square at (u, v) if and only if
there exists a nontrivial factorization u = (x, y) and words r and s such
that

(i) r is a common suﬃx of u and x,

(ii) s is a common preﬁx of y and v,

(iii) |sr| ≥ |y|.

Exercise 4.10 asks the reader to turn Figure 4.6 into a proof of this
lemma. The lemma becomes powerful with the observation that one is not
looking for the beginning of the square.

u v
r s

r s
x y

Figure 4.6: A picture proof of Lemma 4.5.

For a word w = w0w1 · · · wn−1 of length n, we write w(i, j) for the factor
wi · · · wj−1. Stopping short of wj allows that w(i, j)w(j, k) = w(i, k) and
that |w(i, j)| = j − i. We abbreviate the preﬁx w(0, i) of length i by w(i) and
the corresponding suﬃx (starting at position i) by w(i) so that w = w(i)w(i).
Finally, we let x⪖y and x⪕y denote, respectively, the longest common
preﬁx and longest common suﬃx of x and y.

Corollary 4.6. A word uv has a left-centered square at (u, v) if and only if
there is an integer i (0 ≤ i ≤ |u| − 1) such that

|u⪕u(i)| + |v⪖u
(i)| ≥ |u| − i.

140 CHAPTER 4. SQUARES IN WORDS

Exercise 4.10. Turn Figure 4.6 into a proof of Lemma 4.5.

4.3 Preﬁx arrays

The preﬁx array of two words x and y is the sequence of lengths of the
longest preﬁxes common to x and suﬃxes of y:

prefx,y(i) := |x⪖y(i)|, for 0 ≤ i ≤ |y|.

Similarly, the suﬃx array of x and y is the sequence of lengths of the
longest suﬃxes common to x and preﬁxes of y:

suﬀ x,y(i) := |x⪕y(i)|, for 0 ≤ i ≤ |y|.

Example. Consider the words u = abacabaabacaa and v = bacaccab. We
record a few preﬁx and suﬃx arrays in Figure 4.7.

0 1 2 3 4 5 6 7 8 9 10 11 12 13
u a b a c a b a a b a c a a
prefu,u 13 0 1 0 3 0 1 5 0 1 0 1 1 0
suﬀu,u 0 1 0 1 0 1 0 1 2 0 1 0 1 13

v b a c a c c a b
prefv,u 0 4 0 0 0 2 0 0 4 0 0 0 0 0

Figure 4.7: Assorted preﬁx and suﬃx arrays for the words u =
abacabaabacaa and v = bacaccab.

Rephrasing Corollary 4.6 in this language, we see that a word uv has a
left-centered square at (u, v) if and only if there exists 0 ≤ i ≤ |u| − 1 such
that suﬀu,u(i) + prefv,u(i) ≥ |u| − i.

It is this formulation of the existence of left-centered squares that gives us
TC(|u|, |v|) = O (|u| + |v|). Indeed, the complexity of computing suﬀu,u and
pref v,u is linear in |u| (we prove only the ﬁrst of these facts here); likewise
for right-centered squares and |v|.

Lemma 4.7. Fix d = |x⪖y|. For each 0 < j < d one has

x⪖y(j) =
 {
x⪖x(j) = y⪖x(j) = y⪖y(j), if |x⪖x(j)| < d − j,
x(j, d)
(x(d−j)⪖y(d)), if |x⪖x(j)| ≥ d − j.

4.3. PREFIX ARRAYS 141

Proof. The case |x⪖x(j)| < d − j is pictured in Figure 4.8 (the common
preﬁx being r). From the picture, it is clear that the string of given quantities
are all equal whenever s ̸= ǫ.

x

y
 0 d
x⪖y

x⪖y
 0 j d
r r s

r

Figure 4.8: A proof of the ﬁrst case of Lemma 4.7.

The argument supporting the other case is similar.

Corollary 4.8. Fix k < |x| and d = prefx,x(k). For each 0 < j < d one has

pref x,x(k + j) =
 {
prefx,x(j), if prefx,x(j) < d − j,
d − j + |x(d−j)⪖x(k+d)|, otherwise.

The signiﬁcance of this result is that one need not perform as many
pref (-) and suﬀ (-) calculations as one might guess. In Figure 4.9, we un-
derline the preﬁx computations we get for free from the corollary. We leave
it to the reader to develop the analogous suﬃx corollary and underline the
free suﬃx computations.

0 1 2 3 4 5 6 7 8 9 10 11 12 13
x a b a c a b a a b a c a a
prefx,x 13 0 1 0 3 0 1 5 0 1 0 1 1 0
suﬀx,x 0 1 0 1 0 1 0 1 2 0 1 0 1 13

prefx,x(j) + j 1 3 3 7

k = 4
d = 3 k = 7
d = 5

Figure 4.9: Using Corollary 4.8 to compute the preﬁx array
prefx,x of a word x. The underlined entries come at no cost.

We codify our ﬁndings as Algorithm 1. Note that the inner while-loop
will not deﬁne pref[k + j] for values k + j > n = |x| because d cannot be
larger than n − k. In particular, the algorithm always terminates with the
values (k, d) = (n, 0). For the reader unfamiliar with such computations, we
carefully analyze the cost for one pass through Steps 3–11. Suppose the
pair (k, d) at Step 3 becomes (k′, d′) at Step 11. Then k′ − k − 1 entries are

142 CHAPTER 4. SQUARES IN WORDS

input : a word x of length n.
output: an array pref[0, n] of length n + 1.

pref[0] := n ; pref[1] := pref x,x(1)1 k := 1 ; d := pref[k]2 while k < n do3 j := 14 while pref[j] < d − j do5 pref[k + j] := pref[j]6 j := j + 17 end8 if d − j < 0 then d = j9 pref[k + j] := (d − j) + ∣
∣x(d−j)⪖x(k+d)∣
∣10 k := (k + j) ; d := pref[k]11 end12

Algorithm 1: ||||
Computing the preﬁx array prefx,x of a word x.

simply copied from earlier in the array, for a “cost” on the order of k′ − k,
after which a single computation is performed with cost on the order of
|x(d−j)⪖x(k+d)| = d′−d+j = d′−d+k′−k. In total, we get 2(k′−k)+(d′ −d)
as the cost for one pass. If in r steps we move from k1 = 1 to kr = n, adding
the cost of successive passes gives a telescoping sum. The total cost is on
the order of 2kr − 2k1 − (dr − d1) = 2n − 2 − 0 + ∣
∣x⪖x(1)∣
∣, or O (n).

Corollary 4.9. For a given word x of length n, the preﬁx and suﬃx arrays
pref x,x and suﬀx,x can be constructed in O (n) time.

Exercise 4.11 ([CHL2007, Theorem 2.35]). The complexity of computing
pref v,u is linear in |u|.

4.4 Crochemore factorization

Towards the goal of developing a linear-time test for square-freeness, Maxime
Crochemore [Cro1983a] introduced a factorization of words similar to the
popular Ziv-Lempel factorization.1 His factorization of a word w, which may

1The factorization introduced by Abraham Lempel and Jacob Ziv in [LZ1976] was
later implemented by Terry Welch [Wel1984]. The so-called LZW algorithm is behind
many lossless data compression algorithms (e.g., the TIFF image ﬁle format).

4.4. CROCHEMORE FACTORIZATION 143

also be found in the literature as the “f -factorization” or “s-factorization,”
will be denoted c(w) in what follows.

Deﬁnition 4.10. The Crochemore factorization of a word w is the
unique factorization c(w) = (x1, x2, . . . , xn)

of w with each xi satisfying either:

(C1) xi is a letter that does not appear in the factor x1 · · · xi−1; or

(C2) xi is the longest preﬁx of xixi+1 · · · xn that also has an occurrence
beginning within x1 · · · xi−1 (i.e., there is a preﬁx uxi of w with u
shorter than x1 · · · xi−1).

Example. The Crochemore factorizations of abababb and abaababacabba are

(
a, b, abab, b
)

1 1 2 2 and (a, b, a, aba, ba, c, ab, ba
)
,

1 1 2 2 2 1 2 2

where beneath each xi in the factorization (x1, . . . , xn) we have written “1”
or “2” according to whether (C1) or (C2) was used to build the factor.

The following result characterizes words containing squares in terms of
its Crochemore factorization.

Notation. For any factor u of a word w, let πw(u) be the starting index of
the ﬁrst occurrence of u in w.

Theorem 4.11 (Crochemore [Cro1983a]). Let w be a word with Crochemore
factorization c(w) = (x1, . . . , xk). Then w contains a square if and only if
there exists j ∈ N with 2 ≤ j ≤ k such that

(i) πw(xj) < |x1x2 · · · xj−1| ≤ πw(xj) + |xj|, or

(ii) the pair (xj−1 , xj) has a centered square, or

(iii) j ≥ 3 and the pair (x1 · · · xj−2 , xj−1xj) has a right-centered square.

Proof. Let c(w) = (x1, . . . , xk) be the Crochemore factorization of w. If
(ii) or (iii) holds for some 2 ≤ j ≤ k, then w obviously contains a square.
Suppose (i) holds. This case is illustrated in Figure 4.10. Since πw(xj) <
|x1x2 · · · xj−1|, the ﬁrst occurrence of xj must begin within x1x2 · · · xj−1.
Option (A) in the ﬁgure is ruled out because it violates the condition
|x1x2 · · · xj−1| ≤ πw(xj) + |xj|. Options (B) and (C) provide, respectively,
the squares xjxj and rr within w.

144 CHAPTER 4. SQUARES IN WORDS

r s

(C)
x1x2 · · · xj−1 xj

(A) (B)

Figure 4.10: The possible positions (A)–(C) for the ﬁrst occur-
rence of the word xj within x1x2 · · · xj−1xj.

Conversely, suppose that none of (i)–(iii) hold, yet there is a square zz
within w. Letting j be minimal with zz a factor of x1x2 · · · xj, we derive a
contradiction in three steps.

1. zz is not a factor of xj.
Indeed, since (i) does not hold, either xj is a new letter, in which case
zz is clearly not a factor of xj, or πw(xj) + |xj| < |x1x2 · · · xj−1|, meaning
the ﬁrst occurrence of xj is a proper factor of x1x2 · · · xj−1. Then zz is also
a proper factor of x1x2 · · · xj−1, contradicting the minimality of j.

2. zz is not a factor of xj−1xj.
By Step 1, zz is not a factor of xj. If zz is a factor of xj−1, then we
violate the minimality of j. Finally, if zz straddles the boundary between
xj−1 and xj, then (xj−1, xj) has a centered square, violating the assumption
that (ii) does not hold.

3. zz is not a factor of x1x2 · · · xj.
After Steps 1 and 2, we need only rule out the case that zz is a centered
square for (x1x2 · · · xj−2, xj−1xj). Since (iii) does not hold, we may assume
zz is a left-centered square. We are left with the situation pictured in Figure
4.11 with t ̸= ǫ. By the deﬁnition of the Crochemore factorization, xj−1

x1 · · · xj−2 xj−1 xj xj+1 · · · xk
r s r s
xj−1 t t

Figure 4.11: A left-centered square at (x1 · · · xj−2 , xj−1xj) that
satisﬁes none of Conditions (i)–(iii) from Theorem 4.11.

cannot be a single letter (since it occurs before its indicated position as a
preﬁx of s). On the other hand, (C2) is also violated: xj−1 should be the
longest preﬁx of xj−1 · · · xk that also has an occurrence within x1 · · · xj−2,
but s is strictly longer than xj−1.

4.5. SUFFIX TREES 145

We have already seen that the preﬁx (suﬃx) array for testing for left-
centered (right-centered) squares can be built in linear time. Now, if the
Crochemore factorization can be formed in linear time (and it can, see Sec-
tion 4.5), then we have developed a square-free test that runs in linear time
relative to |w|.

Corollary 4.12 ([CHL2007, Theorem 9.14]). A word may be tested for
square-freeness in linear time.

Proof. Given a word w to test, ﬁrst compute the Crochemore factorization
of w (which can be done in linear time; see Section 4.5), and then test Cases
(i)–(iii) in Theorem 4.11 for j = 2, . . . , k:

(i): Is πw(xj) < |x1x2 · · · xj−1| ≤ πw(xj) + |xj|? Each test takes O (1)
time.

(ii): Does the pair (xj−1 , xj) have a centered square? Each such test takes
O (|xj−1| + |xj|) = O (|xj−1xj|) time, by Corollaries 4.6 and 4.9.

(iii): Does the pair (x1 · · · xj−2 , xj−1xj) have a right-centered square? Each
such test takes O (|xj−1xj|) time because the cost of testing for a right-
centered square at (u, v) is linear in |v|.

We conclude that test j may be completed in O (|xj−1xj|) time. Summing
this bound for each j = 2, . . . , k, we ﬁnd the total running time to be on the
order of O (|w|).

Exercise 4.12 ([Smi1876]). Deﬁne an inﬁnite word f as the limit of the
iterations f0 = y, f1 = x, and fn = fn−1fn−2 for n ≥ 2. Verify that this is
the Fibonacci word from Exercise 3.7. (The intermediate iterations in the
procedure are often called the “Fibonacci words.”)

Exercise 4.13 ([BS2006]). Compute the ﬁrst six terms in the Crochemore
factorization (x1, x2, x3, . . .) of f . Posit and prove a peculiar relationship
between the xi’s (i ≥ 4) and the ﬁnite Fibonacci words from Exercise 4.12.

4.5 Suﬃx trees

Given a word w ∈ A∗, the suﬃx tree T (w) is a data structure that compactly
stores for fast retrieval every factor (in particular, every suﬃx) of w. Chief
among its applications is a solution to the factor problem.2

2The terminology varies in the literature; this is also known as the substring problem.

146 CHAPTER 4. SQUARES IN WORDS

Factor Problem: Given a word w of length n, ﬁnd all locations
of all occurrences of a factor f within w.

It happens that T (w) can be built in O (n) time (more precisely, O (n log |A|)
time, but one typically assumes a ﬁxed alphabet). Moreover, once this
“preprocessing” is done, using T (w) one can solve the factor problem in
O (|f | + k) time, assuming k instances of the factor f within w. Otherwise
stated, your favourite PDF viewer could ﬁnd all instances of “Fibonacci”
within the text you are reading faster than you could consult its index.
More information on the construction and applications of this “jewel”
in stringology is readily found in [Gus1997, CR2002]. Here, we are chieﬂy
concerned with its application to the Crochemore factorization. As such, we
indicate the key ingredients of a linear time construction below but stop
short of a detailed proof.

4.5.1 Deﬁnition and examples

The suﬃx tree may be described using the preﬁx poset PA introduced in
Deﬁnition 4.1. That poset has a meet operation3 that we have already met:
(x, y) ↦→ x⪖y, the longest common preﬁx operation of Section 4.2. To
begin, let Suﬀ(w) denote the sub-poset of PA consisting of the suﬃxes of w
(including the empty word). The unadorned suﬃx tree of w, denoted by
Suﬀ(w), is the closure of Suﬀ(w) under⪖in PA.
Example. Figure 4.12 depicts the posets Suﬀ(ababaa) and Suﬀ(ababaa).

ǫ
 a
 aa

abaa

ababaabaa

babaa

(a) The subposet Suﬀ(ababaa) in PA.
 ǫ
 a aa

aba abaa

ababaa

ba baa

babaa

(b) The closure Suﬀ(ababaa) in PA.

Figure 4.12: Construction of the unadorned suﬃx tree Suﬀ(w)
for w = ababaa.

Before deﬁning the suﬃx tree, we need the notion of covers: if x and y
are elements of a poset P , then we say that y covers x and write x ⋖ y, if
x < y and if there does not exist z ∈ P such that x < z < y.

3of Lattice theory, cf., [Sta1997, Chapter 3.3].

4.5. SUFFIX TREES 147

Deﬁnition 4.13. The suﬃx tree T (w) of a word w is the labelled, rooted,
directed tree with nodes and arrows deﬁned as follows.

Nodes. There is one node U for each u ∈ Suﬀ(w). It carries two labels:
the ﬁrst occurrence πw(u) of u and “True” or “False” according to
whether or not u is a suﬃx of w.

Arrows. There is a labelled arrow U v′
−→ V whenever U and V are the
nodes corresponding to suﬃxes u and v with u ⋖ v ∈ Suﬀ(w) and
v = uv′.

The root node E is the node corresponding to ǫ. It is labelled 0 and True.
A suﬃx node of T (w) is a node U labelled by True. A leaf node is a suﬃx
node with no outgoing arrows.

For every node U in T (w), let position(U ) be the numerical label at-
tached to U , let suffix(U ) denote the Boolean label attached to U and
let path(U ) = v1v2 · · · vt, where E v1−→ · · · vt−→ U is the unique path in T (w)
from E to U . Then path(U ) is the word u ∈ Suﬀ(w) corresponding to
the node U , suffix(U ) is True if and only if path(U ) ∈ Suﬀ(w), and
position(U ) = πw(path(U )).

Notation. In the interest of legibility, we keep the labelling convention intro-
duced above by representing nodes with capital letters and their associated
paths with the corresponding lowercase letter, e.g., U is the node correspond-
ing to u ∈ Suﬀ(w). In ﬁgures, the position property of a node is displayed,
and the node is double-circled if it is a suﬃx node.

Example. The suﬃx tree T (ababaa) is pictured in Figure 4.13. (Compare it
with Figure 4.12(b).)
 0
 0
 4
 0
 2
 0
1
 3
 1

a
 a
 ba a

baa
ba a

baa

Figure 4.13: The suﬃx tree T (ababaa).

Example. The suﬃx tree T (abacabaabaca) is pictured in Figure 4.14.

148 CHAPTER 4. SQUARES IN WORDS

0
 0
 6
 0
 4

0 0

2
 2
1 5

1
 13
 3

a
 abaca ba
 abaca

ca baabaca
ca
 baabaca
ba abaca

ca
 baabaca

ca
 baabaca

Figure 4.14: The suﬃx tree T (abacabaabaca).

Remarks. 1. In the preceding examples, each factor f appearing in w is a
preﬁx of path(U ) for a unique node U in T (w). This is true in general. See
Exercise 4.14.
2. The above construction is often called the compact suﬃx tree in the
literature, in which case the name “suﬃx tree” is reserved for the tree T ♯(w)
that may be recovered from T (w) by adding enough bivalent nodes so that
all arrow labels are letters. The advantage of using T ♯(w) is that it may
be viewed as an automaton whose language is Suﬀ(w). The disadvantage is
that it is too large (in terms of the number of states and arrows).

Proposition 4.14. If a tree T has n nodes and e edges, let n + e be a
measure of the size of T . Given a word w ∈ A∗ of length N , the trees T (w)
and T ♯(w) have sizes O (N ) and O (N 2), respectively.

Proof. Exercise 4.15.

In particular, since the run-time for an algorithm is at least as large as its
output, constructing T ♯(w) in linear time is impossible.4

The suﬃx tree for w may be built recursively in several diﬀerent ways.
Peter Weiner [Wei1973] and Edward M. McCreight [McC1976] were the ﬁrst
to describe algorithms to do this in linear time. Weiner’s method adds longer
and longer suﬃxes of w to a tree, starting with the last letter of w, whereas
McCreight’s method adds shorter and shorter suﬃxes, starting with the
entire word w. For more details on their algorithms and how they might be
implemented in linear time, see [Gus1997] and [CHL2007] respectively.

4There does exist a general scheme for building an automaton of smallest size with
language Suﬀ(w). We refer the interested reader to [CHL2007, Chapter 5.5] for details.

4.5. SUFFIX TREES 149

Below, we brieﬂy describe the “on-line” algorithm of Esko Ukkonen
[Ukk1995] for constructing T (w). Ukkonen’s method may also be imple-
mented in O (|w| log |A|) time. It has the novel advantage of not needing
to see the entire word w before beginning the construction of T (w). Our
description largely follows that of [Gus1997].

4.5.2 On-line construction

Recall the notation w(i) and w(j, i) from Section 4.2 for the preﬁx w0 · · · wi−1
and the factor wj · · · wi−1, respectively, of w = w0 · · · wn−1. The idea driving
Ukkonen’s on-line algorithm is to start by building the suﬃx tree T (
w(1))
,
then continue recursively, building the tree T (w(i+1)) from T (w(i)) for 1 ≤
i < n. The passage from one phase of the construction to the next exploits
a simple relationship between the suﬃxes of w(i+1) and w(i):

Suﬀ(w(i+1)) = {uwi | u ∈ Suﬀ(
w(i))} ∪ {
ǫ}

= {w(j, i)wi | 0 ≤ j ≤ i
} ∪ {ǫ}.

In order to achieve the O (n) complexity, Ukkonen actually works with
implicit suﬃx trees at each step, passing to a true suﬃx tree only at the
last step. The implicit suﬃx tree T ♭(w) of a word w diﬀers from T (w) in
that the root node and interior suﬃx nodes are not labelled as suﬃxes, and
interior bivalent nodes do not appear at all.

Example. Figure 4.15 depicts the implicit version of the tree in Figure 4.14.

0
 0
 6 0 4
 0

2

1 5
 1

3

a
 abaca ba abaca

cabaabacacabaabaca

ba abaca

cabaabaca
cabaabaca

Figure 4.15: The implicit suﬃx tree T ♭(abacabaabaca).

We begin by constructing T ♭(w). As we will see shortly, one easily passes
from T ♭(w) to T (w) by one extra walk through the tree. Let us say that
there are n phases in the construction, with phase i + 1 corresponding to

150 CHAPTER 4. SQUARES IN WORDS

adding the letter wi to the tree T ♭(w(i)). The reader may ﬁnd it useful to
look at the elementary examples in Figure 4.16 before reading further. The
ﬁrst phase is always the same and handled in constant time: make the tree
E w0−→ U with position(E) = 0, suffix(E) = “False”, position(U ) = 0 and
suffix(U ) = “True”.
Within phase i + 1 (for i > 1), there are i + 1 extensions, one for each
suﬃx of w(i) (incuding the empty suﬃx). We order the suﬃxes from longest
to shortest, so extension j + 1 corresponds to processing the factor w(j, i)wi.
Each extension is processed according to rules below.

Rule 1 If v = uv′ is a suﬃx of w(i) corresponding to a leaf node V , and V

is a leaf node of U with path(U ) = u, then replace the arrow U v′
−→ V

with U v′wi−−→ V .

Rule 2 If u = w(j, i) is a suﬃx of w(i) corresponding to a node U of T ♭(w(i))

and no edge leaving U begins by wi, then add a new node V : set
position(V ) = j, suffix(V ) = True and add the edge U wi−→ V .

Rule 3 If u = w(j, i) is a suﬃx of w(i) that does not correspond to a node
of T ♭(w(i)), i.e., there are nodes V1 v
−→ V2 with u = path(V1)u′ and
v = u′v′, and if v′ does not begin by wi, then add two new nodes U
and V : set suffix(U ) = False, suffix(V ) = True, position(V ) = j and

position(U ) = position(V2); add the edges U wi−→ V and U v′
−→ V2 and

replace V1 v
−→ V2 by V1 u′
−→ U .

Rule 4 If u = w(j, i) is a suﬃx of w(i) and a path extending from u begins
by wi, then do nothing (the suﬃx w(j, i)wi is already present).

The sequences (a0, a1, . . .) in Figure 4.16 indicate which rules were applied
during phase i. One might observe the following behaviour (Exercise 4.16).

Lemma 4.15. Let aj(i) denote the rule used during extension j of phase i.
Then:

(i) if aj(i) ∈ {1, 2, 3}, then aj(i′) = 1 for all future phases i′;

(ii) if aj(i) = 4, then aj′(i) = 4 for future extensions j′ of i.

The importance of the lemma will be evident a bit later. First, let us
explain how to recover the suﬃx tree T (w) from T ♭(w) by processing an
additional ‘end-of-text’ character external to the alphabet A (say $). Note
that since $ does not appear in A, no suﬃx of w$ is a proper preﬁx of

4.5. SUFFIX TREES 151

0 0a
 0
 0

1

ab

b
 0
 0

1

aba

ba

0
 0

1

abab

bab

0
 0

1

ababa

baba
 0
 0
 0

2

1 3
 1

ab
 abb

b

b b

abb

0
 0 0 0

1 1

a
 ba ba

ba ba
 0
 0
 0

2

1
 3
 1

ab
 abb

b

b b

abb

·b
 ·a

·b

(1, 2)
 (1, 1, 4)

(1, 1, 4, 4)

·a ·b

(1, 1, 4, 4, 4) (1, 1, 3, 3, 4)

·$ ·$

ababa ababb

Figure 4.16: The suﬃx trees T (ababa) and T (ababb), built using
Ukkonen’s on-line algorithm. Each implicit suﬃx tree is built from
the last by lengthening leaves or adding nodes in a systematic
manner.

152 CHAPTER 4. SQUARES IN WORDS

another (i.e., there are no implicit suﬃx nodes in T ♭(w$)). Instead of using
Rules 1–4 to pass from T ♭(w) to T ♭(w$), we use the following modiﬁcations
and arrive directly at T (w): if Rule 1 should apply for w(j, n)$, do nothing;
if Rule 2 or 3 should apply, set suffix(U ) = “True” in place of adding the
new node V ; Rule 4 will never apply by our choice of $.

Proposition 4.16. The above procedure constructs the suﬃx tree T (w) of
a word w ∈ A∗ in O (|w|3) time.

Proof. The key issue is how to locate the ends of the i + 1 suﬃxes of w(i)
within T ♭(w(i)). If we start from the root of the current tree, the j-th ex-
tension to phase i + 1 would take O (i + 1 − j) time to locate. We leave the
details to Exercise 4.17.

4.5.3 Towards a linear-time algorithm

So far, we have a blueprint for construction of T (w) in O (|w|3) time—hardly
the O (|w|) time advertised in the introduction. Ukkonen begins with this
blueprint and introduces several modiﬁcations to reduce the time and space
demands of the execution. Chief among them is the notion of suﬃx links
that stems from the following observation, which we leave as an exercise.

Lemma 4.17. Suppose w ∈ A∗. If U is a node in T ♭(w) with path(U ) = av
for some a ∈ A, then there exists a unique node V with path(V ) = v.

Deﬁne the suﬃx link function S on nodes of T ♭(–) by S(U ) = V (in the
notation of Lemma 4.17). Note that once S(U ) has been deﬁned in phase i,
its value does not change in subsequent phases. Less trivial is the observation
that if a new node U is created in extension j of some phase i, then it will
be possible to deﬁne S(U ) at least by the end of extension j + 1 (so S(U ) is
ready for use in phase i + 1). Creating and maintaining suﬃx links greatly
reduces the time required to apply Rules 1–4 during each phase. Indeed,
if during phase i you have ﬁnished working on extension j, you need not
march from the root all the way to w(j + 1, i). You can get there in constant
time if w(j, i) corresponds to a node (following a suﬃx link), and in time
proportional to i − j − 1 otherwise. Implemention of suﬃx links thus reduces
the total run-time from O (|w|3) to O (|w|2).
We are now ready to use Lemma 4.15. The next speed boost begins
by reducing the space requirements, replacing the edge labels w(j, k) with
the pair of integers (j, k) (see Exercise 4.15). This is useful as follows. If
w(j, i) corresponds to a leaf, it will correspond to a leaf for all i′ > i by the
lemma. As a result, it is suﬃcient to just label it (j, e) where e represents

4.5. SUFFIX TREES 153

the “current-end-of-text.” Incrementing e once per phase is suﬃcient to deal
with all leaves in that phase. Moreover, one may simply keep a counter j0
that points to the “last-known-leaf” from the previous phase. Then j0 + 1
is the starting index of the ﬁrst suﬃx in the current phase that needs to
be explicitly dealt with. Next, again by the lemma, one notes that as soon
as Rule 4 is applied in extension j, one can immediately skip to the start
of the next phase (all remaining extensions j′ will be by Rule 4 and all
relevant suﬃx links have already been made). Finally, Ukkonen shows that
the total number of times Rule 2 or 3 must be applied is bounded by 2|w|.
Implementing these last tricks yields the advertised O (|w|) time for the on-
line algorithm. Again, we refer the reader to [Gus1997] for omitted details.

4.5.4 Crochemore factorizations and square-free tests

We have shown that using preﬁx arrays and the Crochemore factorization
c(w) of a word w, one can test for square-freeness in O (|w|) time. To verify
that the test can truly run in O (|w|) time, it remains only to show that
c(w) can be built in linear time.

Proposition 4.18 (Crochemore [Cro1986]). The Crochemore factorization
c(w) = (x1, x2, . . . , xn) of a word w may be realized in linear time.

Proof. As usual, the factor x1 is the single letter w0. Next, assume that the
ﬁrst i factors x1, x2, . . . , xi have been found and write w = x1 · · · xix′ with
|x1 · · · xi| = N . Use the suﬃx tree to search for preﬁxes p of x′ within w.
Choose p such that |p| is maximal among all preﬁxes q with πw(q) < N .
If p = ǫ, then put xi+1 equal to wN (the ﬁrst letter of x′). Otherwise, put
xi+1 = p.
The above procedure evidently results in the Crochemore factorization
of w. Since the suﬃx tree can be built in linear time, it remains only to
verify that the indicated search may be carried out in linear time. We leave
this to Exercise 4.20.

Example. The Crochemore factorization (a, b, a, c, aba, abaca) is readily built
from the suﬃx tree T (abacabaabaca) in Figure 4.14. It passes Tests (i) and
(iii) of Theorem 4.11 at each index 2 ≤ j ≤ 6 and ﬁrst fails Test (ii) at
(x5, x6).

Complete details on the use of Crochemore’s algorithm to test for square-
freeness may be found in [CHL2007, Chapter 9.3]. We mention that Dan
Gusﬁeld and Jens Stoye have a suﬃx-tree method for testing square-freeness

154 CHAPTER 4. SQUARES IN WORDS

that avoids both the Crochemore factorization and suﬃx arrays [GS2002].5

While their algorithm is somewhat simpler to describe, the present one af-
fords us the opportunity to introduce more tools of the trade.

4.5.5 Further applications

It is worthwhile to mention a few additional uses of suﬃx trees. Exercises
4.18–4.22 outline several that are within reach, despite the rapid introduc-
tion to suﬃx trees above. Touching on a central theme of Part I, suﬃx trees
may also be used to ﬁnd the maximal palindrome p within a word w in linear
time. We close by mentioning the k-mismatch problem.
Fix two words s = s0 · · · sr and w = w0 · · · wn over an alphabet A, with
r ≤ n. Given k ∈ N, a k-mismatch of s within w is a factor wi · · · wi+r of
w such that wi+j ̸= sj for at most k integers 0 ≤ j ≤ r. The k-mismatch
problem is to ﬁnd all k-mismatches of s within w. Gad M. Landau and
Uzi Vishkin [LV1986] and Eugene W. Myers [Mye1986] have shown that
this can be done in O (kn) time. Moreover, Gad M. Landau and Jeanette P.
Schmidt [LS1993] developed a method to test for k-mismatch square-freeness
in O (kn log n
k ) time. It uses, as we did in Section 4.2, a divide-and-conquer
idea as its starting point.

Exercise 4.14. Verify from the deﬁnition of T (w) that if f is any proper
factor of w, then there is a unique node U ∈ T (w) with f a preﬁx of path(U ).

Exercise 4.15. Prove Proposition 4.14. Also, prove that if one replaces the
factors w(j, k) labelling edges by the extremal indices (j, k), then T (w) also
takes up only O (w) space.

Exercise 4.16. Prove Lemma 4.15.

Exercise 4.17. Prove Proposition 4.16.

Exercise 4.18 (The Factor Problem). Given a text w and a factor f , return
in O (|w| + |f | + k) time all k instances of f within w. (Hint: Assume, or
prove, that the following modiﬁcation of T (w) may also be built in O (|w|)
time: instead of labelling internal nodes U with position(U ), label them with
the set {position(V ) | V is a leaf node whose path passes through U }.)

Exercise 4.19 (Longest Common Factor). The longest common factor of
two words u, v can be found in linear time relative to |u| + |v|. (Hint: Build

5Though admittedly they introduce so-called branching squares and DFS arrays in
their place.

4.5. SUFFIX TREES 155

a suﬃx tree for each word ﬁrst, and do a bottom-up search. See [CR2002,
Theorem 5.3].)

Exercise 4.20 (Longest Preﬁx Factor). Given the suﬃx tree for a word
w ∈ A∗ and a suﬃx s beginning at position i in w, return in O (|p|) time
the longest preﬁx p of s such that πw(p) < i.

Exercise 4.21 (All Distinct Factors). The number of distinct factors of
a word w may be counted in O (|w|) time. The distinct factors may be
enumerated (printed) in O (|w| + N ) time, where N is the sum of the lengths
of the distinct factors of w.

Exercise 4.22 (Smallest k-Repeat). Given w ∈ A∗ and k ∈ N, ﬁnd in
O (|w|) time the shortest factor s that occurs exactly k times within w.

156 CHAPTER 4. SQUARES IN WORDS

Chapter 5

Repetitions and Patterns

In this ﬁnal chapter, we outline several directions of research departing from
the Thue-Morse word and square-free work of the preceding chapters. More
details may be found in [Lot1997, Chapter 2], [Lot2002, Chapter 3] and, of
course, the original sources cited below.

5.1 Maximal repetitions

Let v and w be words and write w = w0w1w2 · · · , where w0, w1, w2, . . .
are letters. Recall that wiwi+1 · · · wj is said to be an occurrence of v in
w if v = wiwi+1 · · · wj. (In particular, an occurrence of v in w includes
information about where v appears in w.) Here we will be concerned with
occurrences of repetitions in a ﬁxed word.
A repetition is a word of the form unv, where u is a word, v is a preﬁx
of u and n ≥ 2. Thus, squares and overlaps are examples of repetitions. If r
is a repetition, then the minimal period of r is the smallest positive integer
p such that ri = ri+p for all 0 ≤ i < |r| − p. An occurrence of a repetition
r = wi · · · wj in w is extendible if wi−1r or rwj+1 has the same minimal
period as r. An occurrence of a repetition is nonextendible if it is not
extendible. A maximal repetition, or a run, in a word is an occurrence
of a nonextendible repetition in the word.

Examples. Let w = abaabababaaab.
1. The second occurrence of baba in w is an extendible repetition since
ababa has minimal period 2. Note that babaa does not have minimal period
2. The ﬁrst occurrence of baba in w is also an extendible repetition.
2. The ﬁrst occurrence of the square aa in w is a maximal repetition, but
the other two occurrences of aa are not maximal repetitions because they

157

158 CHAPTER 5. REPETITIONS AND PATTERNS

occur in the cube aaa.
3. The occurrences of abababa, aaa and abaaba in w are also maximal
repetitions.

Any occurrence of a repetition in a word w can be extended to a max-
imal repetition, so the maximal repetitions in w carry all the information
about repetitions that occur in w. Moreover, thanks to the work of Roman
Kolpakov and Gregory Kucherov [KK1999a, KK1999b], we know that the
number of maximal repetitions in a word of length n is linear in n, so this
fact has practical applications. However, their arguments did not provide an
explicit bound on the number of maximal repetitions. The ﬁrst such bound,
5n, was established by Wojciech Rytter [Ryt2006], and was later improved
to 3.44n [Ryt2007]. The best result in this direction was recently announced
by Maxime Crochemore and Lucian Ilie.

Theorem 5.1 (Crochemore, Ilie [CI2007]). The number of maximal repeti-
tions in a word of length n is less than 1.6n.

Crochemore and Ilie also provide suggestions on how to improve the
above bound [CI2007, Section 7]. In their analysis, they use the fact that
the number of maximal repetitions with periods at most 9 in a word of length
n is at most n (see their Lemma 2). If this fact can be improved, then their
argument gives a better bound. For example, if it holds for periods at most
32, then their argument gives a bound of 1.18n.

5.2 Repetition thresholds

In addition to minimal periods p = |u| for the words r = unv above, there
is the notion of exponent |r|/p, a number lying between n and n + 1 and
measuring how close r is to a pure power. Given an inﬁnite word s, the
critical exponent of s is the supremum of the exponents of all its (ﬁnite)
factors r.
Fran¸coise Dejean [Dej1972] introduced this notion in the interest of gen-
eralizing the square-free questions of Thue. She asked,

Given a ﬁxed n-letter alphabet A, what is the minimal critical
exponent among all inﬁnite words over A?

We call this the repetition threshold rt(n) for n.

Example. A quick check reveals that every binary word of length four has
a factor with exponent 2. Hence, the exponent is at least 2 for any inﬁnite

5.3. PATTERNS 159

binary word s. On the other hand, Exercise 5.1 tells us that the exponent
of the Thue-Morse word t is at most 2. That is, rt(2) = 2.

Appealing to Thue’s work again, we recall that there exist square-free
words on 3 letters, so rt(3) < 2. Dejean was able to show that, in fact,
rt(3) = 7
4 . She was also able to show that rt(4) ≥ 7
5 and rt(n) ≥ n
n−1 for
n ≥ 5. She furthermore conjectured that these bounds are tight.
In [Pan1984], Jean-Jacques Pansiot ﬁnally answered the question in the
aﬃrmative for n = 4. Results for larger n have been less forthcoming.
Jean Moulin-Ollagnier veriﬁed the case 5 ≤ n ≤ 11 [MO1992]. Interest-
ingly, James D. Currie and Mortez Mohammad-Noori veriﬁed the cases
12 ≤ n ≤ 14 [CMN2007] by using certain Sturmian words to construct
binary words whose critical exponents achieve the desired lower bound n
n−1 .
The work continues and is likely to end in a positive answer. For exam-
ple, Arturo Carpi has proven that Dejean’s conjecture holds for all n ≥ 33
[Car2006, Car2007].

Exercise 5.1. Words of the form r = unv, with v a preﬁx of u, are called
fractional powers in the literature.1 Prove that a word w is overlap-free
if and only if it contains no fractional power r as a factor with exponent
greater than 2.

Exercise 5.2 ([BMBGL2007]). Suppose β ≥ 2 and m ≥ 1 are integers. Let
A be an m-letter alphabet A and ﬁx a ∈ A and a cyclic permutation σ of
A. Deﬁne a generalization of the Thue–Morse word as tβ,m = ξ∞(a), where

ξ(x) = xσ(x)σ2(x) · · · σβ−1(x)

for all x ∈ A. Show that the critical exponent e(tβ,m) of tβ,m is

e(tβ,m) =
 



∞, if m | β − 1,
2β
m , if m ∤ (β − 1) and β > m,
2, if β ≤ m.

5.3 Patterns

A pattern p is a nonempty word over some alphabet A. Given a pattern p =
a1a2 · · · an (ai ∈ A), an instance of a pattern p is a word x1x2 · · · xn (xi ∈
B∗ \ {ǫ}) such that ai = aj implies that xi = xj. Equivalently, x1x2 · · · xn

1One can ﬁnd these called “sesquipowers” in the literature, even for n > 1. We prefer
to reserve that terminology for n = 1, given the etymology of “sesqui.”

160 CHAPTER 5. REPETITIONS AND PATTERNS

is an instance of p if there exists a nonerasing morphism h : A∗ → B∗ such
that h(p) = x1x2 · · · xn. An Abelian instance of a pattern p is a word
x1x2 · · · xn such that ai = aj implies that xi equals some rearrangement, or
anagram of xj, i.e., |xi|b = |xj|b for each b ∈ B. We denote this by xi ∼ xj.

Example. Consider the pattern p = aabb. The word

zxzyzxzyzxyyxyyyz = z(xzyz)(xzyz)(xyy)(xyy)yz

contains an instance of p (use the mapping (a, b) ↦→ (xzyz, xyy)), while

xyzxxyzxzyyyxyzy = x(yzx)(xyz)(xzyy)(yxyz)y

contains an Abelian instance of p.

Deﬁnition 5.2. A pattern p is k-avoidable (respectively, Abelian k-
avoidable) if there exists an inﬁnite word x on k letters that contains
no instance (Abelian instance) of p as a factor.

Remarks. 1. Note that a word on k letters is also a word on k + 1 letters,
i.e., “k-avoidable” implies “(k + 1)-avoidable” for all k ∈ N \ {0}.
2. In terms of morphisms, we say that p is k-avoidable if and only if for all
nonerasing morphisms h : A∗ → B∗, h(p) is not a factor of x. Likewise for
Abelian k-avoidable.

Examples. 1. The pattern ababa is 2-avoidable since t is overlap-free.
2. The pattern aa is 3-avoidable because there exists an inﬁnite word on
3 letters that is square-free (e.g., the word m = 2102012 · · · from Chapter
3.1).

The study of words avoiding patterns goes back to Thue [Thu1906]. He
asked, given p ∈ A∗ and w ∈ B∗ with w suﬃciently longer than p, can one
always ﬁnd a nonerasing morphism h : A∗ → B∗ such that h(p) is a factor
of w? He answered himself in the negative (see the second example above).
The present notion of pattern appeared independently in [BEM1979] and
[Zim1982].
The question of Abelian pattern avoidance was ﬁrst posed by Paul Erd˝os
[Erd1961], hidden among a list of 66 other unsolved research problems. An
important early result is due to Frederik Michel Dekking.

Theorem 5.3 (Dekking [Dek1979]). The pattern a4 is Abelian 2-avoidable.

We indicate his argument below. Using a similar argument, Dekking also
showed that a3 is Abelian 3-avoidable. He furthermore raised the question

5.3. PATTERNS 161

whether a2 is Abelian 4-avoidable. An early step towards the ultimate answer
was provided by A. A. Evdokimov [Evd1968], who gave an example of an
inﬁnite word without Abelian squares over 25 letters. This was improved to
5 letters by Peter A. B. Pleasants [Ple1970]. The ﬁnal answer was given by
Veikko Ker¨anen: he gives an 85-uniform morphism over 4 letters generating
an inﬁnite word without Abelian squares [Ker1992].
Turning to Dekking’s argument, let φ : {0, 1}∗ → {0, 1}∗ be the mor-
phism taking (0, 1) to (0001, 011). We will show that φ∞(0) avoids the pat-
tern a4 in the Abelian sense. We will also make use of an auxillary morphism
g : {0, 1}∗ → Z/5Z taking (0, 1) to (2, −1).

Lemma 5.4. Fix a sequence of letters a1, . . . , an ∈ {0, 1} and consider
factorizations φ(ai) = pisi for some choice of preﬁxes pi and suﬃxes si ̸= ǫ.
If g(p1) ≡ · · · ≡ g(pn) mod 5, then p1 = · · · = pn or s1 = · · · = sn.

Proof. Considering the preﬁxes p of 0001 and 011, the possible values for
g(p) are 0, 1, 2 and 4. In particular, g(0001) ≡ g(011) ≡ 0 mod 5.
Now, if g(pi) ≡ 0 for all i, then pi = ǫ for all i. If g(pi) ≡ 1 for all i, then
si = 1 for all i. If g(pi) ≡ 2 for all i, then pi = 0 for all i. If g(pi) ≡ 4 for all
i, then pi = 00 for all i.

Lemma 5.5. Let q = q1 · · · qm be a pattern, with qi ∈ {0, 1}, and suppose
that Q1 · · · Qm is a shortest Abelian instance of q in φ∞(0). Then g(Qj ) ̸≡ 0
mod 5 for some 1 ≤ j ≤ m.

Proof. Choose a preﬁx w = a1 · · · aN of φ∞(0) so that Q1 · · · Qm is a factor
of φ(a1 · · · aN ). We may assume that φ(a1 · · · aN ) = P Q1 · · · QmS for some
P, S ∈ {0, 1}∗ with S ̸= ǫ (replacing N by N + 1 if necessary). Suppose

w: a1 a2 · · · aN

φ(a1) φ(aN )
φ(w): P Q1 Q2 · · · Qm S

Figure 5.1: If Q1 · · · Qm occurs in φ
∞(0), then there is a (mini-
mal) N and a preﬁx w = a1 · · · aN of φ
∞(0) so that φ(w) has the
factorization P Q1 · · · QmS with S ̸= ǫ.

that g(Qj) ≡ 0 mod 5 for all 1 ≤ j ≤ m. We will construct a shorter
Abelian instance t1 · · · tm of q within a1 · · · aN , contradicting the minimality
of |Q1 · · · Qm|.

162 CHAPTER 5. REPETITIONS AND PATTERNS

We ﬁrst argue for the existence of a subsequence i1 < i2 · · · < im of
{1, 2, . . . , N } with the property that φ(aij ) ends within Qj. That is, there
is a nonempty suﬃx sj of φ(aij ) that is also a preﬁx of Qj. See Figure 5.2.
If this is not the case, then there is an index j ≥ 2 yielding the situation

φ(ai1 ) φ(ai2 ) φ(aim ) φ(aN )

P Q1 Q2 · · · Qm−1 Qm S
p1 s1 p2 s2 pm sm pm+1 sm+1

Figure 5.2: Analysis of the preﬁx P Q1 · · · QmS of φ
∞(0). Given
the preimage a1 · · · aN , there exist indices 1 ≤ i1 < · · · < im <
im+1 = N so that φ(aij ) = pjsj is a factorization centered on
(P Q1 · · · Qj−1 , Qj · · · QmS) with sj ̸= ǫ.

illustrated in Figure 5.3 (i.e., Qj−1 is a proper factor of φ(aij )). We deduce

pj−1 sj−1
pj sj

φ(ai)
· · · Qj−1 Qj

Figure 5.3: Analysis of the preﬁx P Q1 · · · QmS of φ
∞(0). An
impossible relationship between the φ(ai)’s and the Qj’s.

that g(pj−1) ≡ g(pj ) (since g(Qj−1) ≡ 0), and moreover that pj−1 = pj
(applying Lemma 5.4 with n = 2 and a1 = a2 = aij ). But then Qj−1 = ǫ,
which is absurd.
In summation, we do indeed have the situation illustrated in Figure 5.2.
Let us augment that picture by labelling a few more factors. See Figure 5.4.
Note that each Q′
j is in the image of φ, so we get g(Q′
j) ≡ 0 (indeed, g(φ(0))

φ(ai1 ) φ(ai2 ) φ(aim ) φ(aN )

P Q1 Q2 · · · Qm−1 Qm S
p1 s1 Q′
1 p2 s2 Q′
2 p3 · · · · · · pm sm Q′
m pm+1 sm+1
T1 T2 · · · Tm

Figure 5.4: Analysis of the preﬁx P Q1 · · · QmS of φ
∞(0). Factors
Tj and Q′
j are added to Figure 5.2 in order to apply Lemma 5.4.

and g(φ(1)) are both zero modulo 5). Since g(Qj) ≡ 0 for all 1 ≤ j ≤ m,
we must have g(sj) + g(pj+1) ≡ 0 for all 1 ≤ j ≤ m. On the other hand,

5.3. PATTERNS 163

0 ≡ g(φ(aij )) ≡ g(pj) + g(sj) for all 1 ≤ j ≤ m, from which we infer that
g(pj) ≡ g(pj+1) mod 5 for all 1 ≤ j ≤ m. Lemma 5.4 then tells us that
p1 = · · · = pm+1 or s1 = · · · = sm+1. We consider the ﬁrst case (the second
being symmetric).
Referring to Figure 5.4, note that Tj is φ(tj) for some word tj, and that
t1 · · · tm is a factor of φ∞(0) satisfying |t1 · · · tm| < |Q1 · · · Qm| (because
|φ(0)|, |φ(1)| > 1). We will show that t1 · · · tm is an Abelian instance of q in
φ∞(0), contradicting the assumption that Q1 · · · Qm is a shortest Abelian
instance of q in φ∞(0). Suppose qi = qj; we need to show that |ti|z = |tj|z
for z ∈ {0, 1}. Since Q1 · · · Qm is an Abelian instance of q, we have Qi ∼ Qj.
Looking again at Figure 5.4, we infer that Tkpk+1 = pkQk for all 1 ≤ k ≤
m. Since pk = pk+1 for all 1 ≤ k ≤ m, it follows that Tk ∼ Qk for all
1 ≤ k ≤ m. Consequently, Ti ∼ Tj, so |Ti|z = |Tj|z for all z ∈ {0, 1}. Since
|Tk|0 = 3|tk|0 + |tk|1 and |Tk|1 = |tk|0 + 2|tk|1 for all 1 ≤ k ≤ m, we have

3|ti|0 + |ti|1 = 3|tj|0 + |tj|1 and |ti|0 + 2|ti|1 = |tj|0 + 2|tj|1.

It follows that |ti|z = |tj|z for z ∈ {0, 1}. Hence, t1 · · · tm is an Abelian
instance of q in φ∞(0).

Proof of Theorem 5.3. Suppose a4 is not Abelian 2-avoidable in φ∞(0) and
consider a shortest Abelian instance P Q1Q2Q3Q4R of a4. Since Qi ∼ Qj
for all 1 ≤ i, j ≤ 4, we have that g(Qj ) is constant for all j (and nonzero by
Lemma 5.5). In particular, the sequence

g(P ), g(P Q1), g(P Q1Q2), g(P Q1Q2Q3), g(P Q1Q2Q3Q4) (5.6)

is an arithmetic progression of length 5. We claim that it does not contain
the number 3, which is a contradiction.
To see the claim, build a factorization of P and each Qj, analogous to
that in the proof of Lemma 5.5, as follows: Find the unique i1 so that

|φ(a1 · · · ai1−1)| ≤ |P | < |φ(a1 · · · ai1)|.

Write P = φ(a1 · · · ai1−1)p1 for some preﬁx p1 of φ(ai1). Repeat for each
factor in (5.6), writing, e.g., P Q1 = φ(a1 · · · ai2−1)p2 for some preﬁx p2 of
φ(ai2). (We do not demand that i1 < i2 < · · · < i5.) Since g(t) ≡ 0 for any
t in the image of φ, the sequence in (5.6) becomes

g(p1), g(p2), g(p3), g(p4), g(p5).

The preﬁxes above were chosen so that φ(aij ) = pjsj with sj ̸= ǫ. We
observed in the proof of Lemma 5.4 that g(p) must belong to {0, 1, 2, 4} for
such preﬁxes p. This completes the proof of the claim and the theorem.

164 CHAPTER 5. REPETITIONS AND PATTERNS

Dekking’s technique of comparing arithmetic progressions works for more
general patterns than just powers. Consider the following example.

Example. The word φ∞(0) avoids a3ba2b3 in the Abelian sense (Exercise
5.7).

The above example is a “true” generalization of Dekking’s theorem, as
opposed to the Abelian 2-avoidability of, say, abababba, which is the same
as (ab)4 (indeed as a4) in the sense of Abelian pattern avoidance. James
Currie and Terry Visentin have begun to investigate which binary patterns
are Abelian 2-avoidable. In [CV2007], many such patterns are found; the
avoidance proofs are in the spirit of the Dekking argument above.

Exercise 5.3 (K¨onig’s Lemma [Lot2002, Proposition 1.2.3]). If X is an
inﬁnite preﬁx-closed set of words over a ﬁnite alphabet A, then there is an
inﬁnite word x having all of its preﬁxes in X.

Exercise 5.4 ([Lot2002, Proposition 1.6.3]). A pattern p is k-avoidable if
and only if there are inﬁnitely many words in {0, 1, . . . , k − 1}∗ that avoid
p. (Hint: A standard application of K¨onig’s Lemma above.)

Exercise 5.5 ([Dek1979]). Show that a3 is Abelian 3-avoidable.

Exercise 5.6. The pattern a2 is not Abelian 3-avoidable. The pattern a3 is
not Abelian 2-avoidable. (Hint: Maximal words avoiding the patterns have
length seven and nine, respectively.)

Exercise 5.7. The pattern a3ba2b3 is Abelian 2-avoidable. (Hint: Use the
word φ∞(0) and argue, as in the proof of Theorem 5.3, with arithmetic
progressions.)

5.4 Zimin patterns

We conclude our introduction to the theory of patterns with a discussion of
certain unavoidable patterns. The reader interested in learning more about
unavoidability may consult [Lot2002, Chapter 3]. See also [Cur1993], where
a number of open questions are posed—some with prizes attached.

Deﬁnition 5.7. Given a ﬁxed alphabet A, the set of Zimin words Z(A)
are the words in A∗ deﬁned recursively as follows:

(i) every letter a ∈ A is a Zimin word;

(ii) if p is a Zimin word over A \ {a}, then pap is a Zimin word.

5.4. ZIMIN PATTERNS 165

Example. The Zimin words Z({a, b, c}) include a, aba, abacaba and all im-
ages of these under permutations of the ordered alphabet (a, b, c).
As it happens, the Zimin words are unavoidable in a sense we now make
precise (indeed, this is why A. I. Zimin introduced them [Zim1982]). A pat-
tern p over A is called k-unavoidable if every suﬃciently long word w
over a k-letter alphabet B contains an instance of p. More precisely, there
is an integer N so that if |w| ≥ N , then there is a nonerasing morphism
hw : A∗ → B∗ so that hw(p) is a factor of w.
We will also need an avoidability notion for sets. Given a set P =
{p1, p2, . . . , pn} of words in A∗, we say that P is a k-unavoidable set if
every suﬃciently long word w over a k-letter alphabet B has an associated
nonerasing morphism hw : A∗ → B∗ satisfying hw(pi) is a factor of w for
all 1 ≤ i ≤ n. Conversely, we say that P is a k-avoidable set if there is
an inﬁnite word x over B with |B| = k so that, no matter the morphism
h : A∗ → B∗, x does not have the factor h(pi) for at least one pi ∈ P .
Note that in the case |P | = 1, this notion reduces to the preceding
pattern-avoidance notion. We call P a set of patterns in what follows to
emphasize the connection. Finally, given two sets of patterns P and P ′, we
write P .
= P ′ if for each k ∈ N either both are k-avoidable or both are
k-unavoidable.

Proposition 5.8. Fix a letter a ∈ A and two words p1, p2 ∈ (A \ a)∗. Then

{p1, p2} .
= {p1ap2}.

Proof. Fix k and suppose that {p1, p2} is a k-avoidable set. Then there
is an inﬁnite word x over B = {0, 1, . . . , k − 1} such that, no matter the
morphism hˆa : (A \ a) → B, either hˆa(p1) or hˆa(p2) is not a factor of x.
Now, {p1ap2} being a k-unavoidable set would mean that h(p1)h(a)h(p2)
exists within some preﬁx of x (for some h : A∗ → B∗). Deﬁning hˆa to be
the restriction of h to A \ a, this forces both hˆa(p1) and hˆa(p2) to be factors
of x. Consequently, {p1ap2} must be a k-avoidable set.
Conversely, suppose that {p1ap2} is a k-avoidable set. Then there is
an inﬁnite word x over B = {0, 1, . . . , k − 1} such that, no matter the
morphism h : A∗ → B∗, x does not contain the factor h(p1)h(a)h(p2). Now,
{p1, p2} being a k-unavoidable set would mean that there is an integer N
satisfying: for all w ∈ Bn (n ≥ N ), there exists a nonerasing morphism
hw : (A \ a)∗ → B∗ such that both hw(p1) and hw(p2) are factors of w.
Being an inﬁnite word, x cannot avoid every word of length N . In fact,
there must be a word w of length N yielding the factorization

x = uwvwx′ with v ̸= ǫ

166 CHAPTER 5. REPETITIONS AND PATTERNS

for some u, v ∈ B∗. Writing w = w′
1hw(p1)w′′
1 and w = w′
2hw(p2)w′′
2 , we
further factorize x as
 uw′
1hw(p1)w′′
1 vw′
2hw(p2)w′′
2 x′.

Extending hw to a morphism h of A∗ by deﬁning h(a) = w′′
1 vw′
2 would
then contradict our assumptions on {p1ap2}. Consequently, {p1, p2} is a k-
avoidable set.

Corollary 5.9. The Zimin words are k-unavoidable for every k ∈ N \ {0}.

Proof. Fix an alphabet A and a Zimin word w ∈ Z(A). We reason by in-
duction on the length ℓ of w, supposing every Zimin word having less than
|A| distinct letters and of length less than ℓ has been shown k-unavoidable
for all k.
The base case ℓ = 1 holds because each a ∈ A is k-unavoidable for all
k ∈ N \ {0}. If w is a Zimin word of length ℓ > 1, then w = pap for some
a ∈ A and p ∈ (A \ a)∗ \ {ǫ}. Moreover, p ∈ Z(A) ∩ (A \ {a})∗ by deﬁnition.
Proposition 5.8 then gives
 {pap} .
= {p, p} .
= {p}.

Now, p is k-unavoidable for all k by induction, implying pap is as well.

In a certain sense, Zimin words are the only unavoidable patterns. This
is indicated by the next result.

Theorem 5.10 (Zimin, [Zim1982]). A pattern p on an alphabet A is un-
avoidable if and only if there exists a Zimin word z on an alphabet B and a
nonerasing morphism h : A∗ → B∗ so that h(p) appears as a factor of z.

Example. The pattern p = abcba is unavoidable because of the Zimin word
z = abacaba. More speciﬁcally, the morphism h deﬁned by (a, b, c) ↦→ (b, a, c)
maps p to bacab, the central factor of z.

Finding the morphism h in the theorem may be diﬃcult. Luckily, Propo-
sition 5.8 can give us more than Corollary 5.9. To illustrate, consider the
pattern p = abxbcycazactcb on the alphabet A = {a, b, c, x, y, z, t}.

Corollary 5.11. The pattern p above is 3-unavoidable.

Proof. Using the proposition, we have

{p} .
= {abxbcyca, actcb}

5.5. BI-IDEAL SEQUENCES 167

(eliminating z). Continuing by eliminating y, x and t, we arrive at

{p} .
= {ab, bc, ca, ac, cb}.

We show that Q = {ab, bc, ca, ac, cb} is a 3-unavoidable set by considering
the words w in {0, 1, 2}∗ of length 14. If w contains a square, then w does
not avoid Q (take h(a) = h(b) = h(c) = u). Otherwise, one checks that w
contains all six factors ij with {i, j} ⊆ {0, 1, 2} (there are many square-free
words of length 14, but if Thue could do it, so can you). Taking h(a) = 0,
h(b) = 1 and h(c) = 2, we see that such a w also does not avoid Q. Finally,
if w is a word of length 15 or greater, then it has a preﬁx of length 14, so it
also does not avoid Q. This completes the proof.

Exercise 5.8. If a pattern p is (k +1)-unavoidable for some k, then it is also
k-unavoidable (and the same bound N on the length of exceptional words
will suﬃce).

Exercise 5.9. A set of patterns P is k-unavoidable if and only if it is not
k-avoidable.

Exercise 5.10 (Zimin images). In Theorem 5.10, it was shown that mor-
phic preimages of factors of Zimin words are unavoidable. Show that the
same does not hold for morphic images. Consider aba and ﬁnd a nonerasing
endomorphism γ on {a, b}∗ so that γ(aba) is 2-avoidable.

5.5 Bi-ideal sequences

The recursive form of Zimin words has been exploited in many ways not
outlined above. We mention a few of them here and refer the reader to
[Lot2002, Chapter 4] for more details.
Zimin words have a natural generalization called sesquipowers. These
are deﬁned recursively as follows: any nonempty word is a sesquipower of
order 1; a word w over an alphabet A is a sesquipower of order n > 1 if
w = w0vw0 for some words w0, v ∈ A∗ with w0 ̸= ǫ and w0 a sesquipower of
order n − 1. So w is a sesquipower if and only if it is a nonempty image of a
Zimin word under a morphism h (not necessarily nonerasing). A sequence of
words wn ∈ A∗ is called a bi-ideal sequence if each term in the sequence
is a sesquipower of the preceding term, i.e.,

wn = wn−1vnwn−1

for some choice of words vn ∈ A∗.

168 CHAPTER 5. REPETITIONS AND PATTERNS

The use of bi-ideal sequences in algebraic structures is quite old (see,
e.g., m-sequences in [Jac1956] or [Sch1961, Section IV.5]), but the termi-
nology was not coined until 1966 by Michel Coudrain and Marcel-Paul
Sch¨utzenberger. In [CS1966], they use bi-ideal sequences to give criteria for
a ﬁnitely generated semigroup to be ﬁnite (see [Lot2002, Theorem 4.5.10]).
Closer to the topics in the present book, bi-ideal sequences may also be
used to improve upon a classical result of Anatoly I. Shirshov [ˇSir1957] on
n-divisions. Suppose u is a word over a totally-ordered alphabet. A factor-
ization u = (x1, x2, . . . , xn) is called an n-division if each xi is nonempty
and u is lexicographically greater than any nontrivial anagram xi1xi2 · · · xin
of the factors. The following appears as Theorem 4.4.5 in [Lot2002].

Theorem 5.12 (de Luca, Varricchio [dLV1999]). Fix a totally-ordered al-
phabet A of cardinality k. Given positive integers p and n, every suﬃciently
long word w ∈ A∗ satisﬁes:

(i) there exists u ̸= ǫ such that up is a factor of w; or

(ii) there exists a factor u of w that is the n-th term of a bi-ideal sequence.
Moreover, u has an n-division u = (x1, x2, . . . , xn) where each xi is a
Lyndon word and x1 > x2 > · · · > xn.

Finally, to any bi-ideal sequence (wn)n≥1, one may naturally associate
an inﬁnite word w = limn→∞ wn with arbitrarily long sesquipower preﬁxes.
Inﬁnite words constructed in this fashion are precisely the recurrent words.
See Exercise 5.11.

Exercise 5.11 ([Lot2002, Proposition 4.3.1]). Recall that an inﬁnite word x
is recurrent if every ﬁnite factor of x occurs within x inﬁnitely often. Prove
that every recurrent inﬁnite word is the limit of some bi-ideal sequence.
(Hint: Given a recurrent word x, set w1 = x1 and deﬁne a bi-ideal sequence
w1, w2, w3, . . . recursively, using the recurrent property of x.)

5.6 Repetitions in Sturmian words

To tie the two parts of this book together, we brieﬂy mention some results
concerning repetitions in inﬁnite words that are constructed from lines of
irrational slope as Christoﬀel words were constructed from line segments of
rational slope in Part I.
We begin with the Fibonacci word. Let φ be the golden ratio. Let ℓ be the
positive ray in R2 of slope −φ
∨ = φ − 1 beginning at the origin, and let s be
the inﬁnite binary word obtained by discretizing ℓ. The Fibonacci word,

5.6. REPETITIONS IN STURMIAN WORDS 169

denoted by f , is the inﬁnite binary word satisfying s = xf . We have already
encountered f : it was introduced in Exercise 1.5 of Part I, and studied in
Exercises 3.7 and 4.12 of Part II.
It is known from the work of Filippo Mignosi and Giuseppe Pirillo
[MP1992] that f contains no powers of exponent greater than 2 + φ, and
that it contains powers of exponent less than but arbitrarily close to this
number. Therefore, the critical exponent of f is 2 + φ.
This result has been extended as follows. For any irrational real number
α, let s be the inﬁnite word obtained by discretizing the line of slope α/(1 +
α) passing through the origin in R2, and let cα denote the inﬁnite binary
word satisfying s = xcα. Such words are called characteristic Sturmian
words. Mignosi proved that if the continued fraction representation of α has
bounded partial quotients, then the powers occurring in cα are bounded, and
conversely [Mig1991]. Detailed studies of the exact exponent of powers that
appear in a Sturmian word have been carried out later.
Finally, we mention a recent, interesting connection between repetitions
and transcendence. It has been shown that if a binary inﬁnite word has
inﬁnitely many preﬁxes that are repetitions of exponent 2 + ε for some ε,
then the real number whose binary expansion is this inﬁnite word is either
rational or transcendental [FM1997]. As a consequence, any number whose
binary expansion is a Sturmian word is either rational or transcendental.
For more results in this direction, see [AB2005].

170 CHAPTER 5. REPETITIONS AND PATTERNS

Bibliography

For the convenience of the reader, each entry below is followed by ↑ and a list of
page numbers indicating the location within the book where the citation occurs.

[ABG2007] A. Aberkane, S. Brlek, and A. Glen. Sequences having the Thue-Morse
complexity, 2007. Preprint. ↑102

[AB2005] B. Adamczewski and Y. Bugeaud. On the decimal expansion of algebraic
numbers. Fiz. Mat. Fak. Moksl. Semin. Darb. 8:5–13, 2005. ↑169

[AL1977] A. Adler and S.-Y. R. Li. Magic cubes and Prouhet sequences. Amer.
Math. Monthly 84 (8):618–627, 1977. ↑90

[AAB+1995] J.-P. Allouche, A. Arnold, J. Berstel, S. Brlek, W. Jockusch, S. Plouﬀe,
and B. E. Sagan. A relative of the Thue-Morse sequence. Discrete Math. 139 (1-
3):455–461, 1995. Formal power series and algebraic combinatorics (Montreal,
PQ, 1992). ↑86, 117

[AARS1994] J.-P. Allouche, D. Astoorian, J. Randall, and J. Shallit. Morphisms,
squarefree strings, and the Tower of Hanoi puzzle. Amer. Math. Monthly 101
(7):651–658, 1994. ↑111, 116, 117, 122

[AB1992] J.-P. Allouche and R. Bacher. Toeplitz sequences, paperfolding, Towers
of Hanoi and progression-free sequences of integers. Enseign. Math. (2) 38 (3-
4):315–327, 1992. ↑117

[AS1999] J.-P. Allouche and J. Shallit. The ubiquitous Prouhet-Thue-Morse se-
quence. In Sequences and their applications (Singapore, 1998), pages 1–16. 1999.
↑84

[AS2003] J.-P. Allouche and J. Shallit. Automatic sequences: theory, applications,
generalizations. Cambridge University Press, Cambridge, 2003. ↑5, 86, 94, 95,
96, 97, 99

[AT2007] A. Alpers and R. Tijdeman. The two-dimensional Prouhet-Tarry-Escott
problem. J. Number Theory 123 (2):403–412, 2007. ↑89

171

172 BIBLIOGRAPHY

[Aus2006] P. Auster. The Brooklyn Follies. Henry Holt and Company, LLC, 175
Fifth Avenue, New York, New York 10010, 2006. ↑54

[BEM1979] D. R. Bean, A. Ehrenfeucht, and G. F. McNulty. Avoidable patterns
in strings of symbols. Paciﬁc J. Math. 85 (2):261–294, 1979. ↑126, 160

[Ber1771] J. Bernoulli. Sur une nouvelle esp`ece de calcul. In Recueil pour les as-
tronomes, pages 255–284. 1771. ↑67

[Ber1990] J. Berstel. Trac´e de droites, fractions continues et morphismes it´er´es. In
Mots, pages 298–309. 1990. ↑3

[Ber1995] J. Berstel. Axel Thue’s papers on repetitions in words: a translation.
Publications du Laboratoire de Combinatoire et d’Informatique Math´ematique,
vol. 20. Universit´e du Qu´ebec `a Montr´eal, Canada, 1995. ↑99

[BdL1997] J. Berstel and A. de Luca. Sturmian words, Lyndon words and trees.
Theoret. Comput. Sci. 178 (1–2):171–203, 1997. ↑23, 34, 50, 57

[BP1985] J. Berstel and D. Perrin. Theory of codes. Pure and Applied Mathematics,
vol. 117. Academic Press Inc., Orlando, FL, 1985. ↑130

[BS2006] J. Berstel and A. Savelli. Crochemore factorization of Sturmian and
other inﬁnite words. In Mathematical foundations of computer science 2006,
pages 157–166. 2006. ↑145

[BS1993] J. Berstel and P. S´e´ebold. A characterization of overlap-free morphisms.
Discrete Appl. Math. 46 (3):275–281, 1993. ↑99

[BdLR2008] V. Berth´e, A. de Luca, and C. Reutenauer. On an involution of
Christoﬀel words and Sturmian morphisms. European J. Combin. 29 (2):535–
553, 2008. ↑15, 18, 30

[BMBGL2007] A. Blondin-Mass´e, S. Brlek, A. Glen, and S. Labb´e. On the critical
exponent of generalized Thue-Morse words. Discrete Math. Theor. Comput. Sci.
9 (1):293–304, 2007. ↑159

[BL1993] J.-P. Borel and F. Laubie. Quelques mots sur la droite projective r´eelle.
J. Th´eor. Nombres Bordeaux 5 (1):23–51, 1993. ↑3, 19, 21, 23, 30, 57

[BR2006] J.-P. Borel and C. Reutenauer. On Christoﬀel classes. Theor. Inform.
Appl. 40 (1):15–27, 2006. ↑33, 51, 53

[BI1994] P. Borwein and C. Ingalls. The Prouhet-Tarry-Escott problem revisited.
Enseign. Math. (2) 40 (1-2):3–27, 1994. ↑89

[BLP2003] P. Borwein, P. Lisonˇek, and C. Percival. Computational investigations
of the Prouhet-Tarry-Escott problem. Math. Comp. 72 (244):2063–2070 (elec-
tronic), 2003. See also http://eslp.yeah.net. ↑89

[Bra1963] C. H. Braunholtz. An inﬁnite sequence of 3 symbols with no adjacent
repeats. Amer. Math. Monthly 70 (6):675–676, 1963. Advanced Problems and
Solutions: Solution 5030 to a question of H. Noland, with a remark by T. Tamura.
↑119

BIBLIOGRAPHY 173

[Brl1989] S. Brlek. Enumeration of factors in the Thue-Morse word. Discrete Appl.
Math. 24 (1-3):83–96, 1989. First Montreal Conference on Combinatorics and
Computer Science, 1987. ↑99

[BW1994] M. Burrows and D. J. Wheeler. A block-sorting lossless data compression
algorithm. Technical Report 124, 1994. ↑48

[Car1921] F. Carlson. ¨Uber Potenzreihen mit ganzzahligen Koeﬃzienten. Math. Z.
9 (1-2):1–13, 1921. ↑110

[Car2006] A. Carpi. On the repetition threshold for large alphabets. In Mathemat-
ical foundations of computer science 2006, pages 226–237. 2006. ↑159

[Car2007] A. Carpi. On Dejean’s conjecture over large alphabets. Theoret. Comput.
Sci. 385 (1-3):137–151, 2007. ↑159

[Cas1957] J. W. S. Cassels. An introduction to Diophantine approximation. Cam-
bridge Tracts in Mathematics and Mathematical Physics, No. 45. Cambridge
University Press, New York, 1957. ↑69

[CFL1958] K.-T. Chen, R. H. Fox, and R. C. Lyndon. Free diﬀerential calculus,
IV. The quotient groups of the lower central series. Ann. of Math. (2) 68:81–95,
1958. ↑50

[CS1963] N. Chomsky and M.-P. Sch¨utzenberger. The algebraic theory of context-
free languages. In Computer programming and formal systems, pages 118–161.
1963. ↑109

[Chr1875] E. B. Christoﬀel. Observatio arithmetica. Annali di Matematica 6:145–
152, 1875. ↑3, 6, 54

[Chr1888] E. B. Christoﬀel. Lehrs¨atze ¨uber arithmetische eigenschaften du irra-
tionnalzahlen. Annali di Matematica Pura ed Applicata, Series II 15:253–276,
1888. ↑3

[CKMFR1980] G. Christol, T. Kamae, M. Mend`es France, and G. Rauzy. Suites
alg´ebriques, automates et substitutions. Bull. Soc. Math. France 108 (4):401–
419, 1980. ↑97, 98

[Cob1972] A. Cobham. Uniform tag sequences. Math. Systems Theory 6:164–192,
1972. ↑94

[Coh1972] H. Cohn. Markoﬀ forms and primitive words. Math. Ann. 196:8–22, 1972.
↑12

[CS1966] M. Coudrain and M.-P. Sch¨utzenberger. Une condition de ﬁnitude des
mono¨ıdes ﬁniment engendr´es. C. R. Acad. Sci. Paris S´er. A-B 262:A1149–
A1151, 1966. ↑168

[CH1973] E. M. Coven and G. A. Hedlund. Sequences with minimal block growth.
Math. Systems Theory 7:138–153, 1973. ↑53, 104

[Cro1981] M. Crochemore. An optimal algorithm for computing the repetitions in
a word. Inform. Process. Lett. 12 (5):244–250, 1981. ↑136

174 BIBLIOGRAPHY

[Cro1982] M. Crochemore. Sharp characterizations of squarefree morphisms. The-
oret. Comput. Sci. 18 (2):221–226, 1982. ↑124

[Cro1983a] M. Crochemore. Recherche lin´eaire d’un carr´e dans un mot. C. R. Acad.
Sci. Paris S´er. I Math. 296 (18):781–784, 1983. ↑142, 143

[Cro1983b] M. Crochemore, R´egularit´es ´evitables (th`ese d’´etat). Ph.D. Thesis, 1983.
↑124

[Cro1986] M. Crochemore. Transducers and repetitions. Theoret. Comput. Sci. 45
(1):63–86, 1986. ↑153

[CDP2005] M. Crochemore, J. D´esarm´enien, and D. Perrin. A note on the Burrows-
Wheeler transformation. Theoretical Computer Science 332 (1-3):567–572, 2005.
↑48, 49

[CHL2001] M. Crochemore, C. Hancart, and T. Lecroq. Algorithmique du texte.
Vuibert, Paris, 2001. ↑138

[CHL2007] M. Crochemore, C. Hancart, and T. Lecroq. Algorithms on strings.
Cambridge University Press, Cambridge, 2007. Translated from the 2001 French
original. ↑138, 142, 145, 148, 153

[CI2007] M. Crochemore and L. Ilie. Analysis of maximal repetitions in strings.
In Mathematical Foundations of Computer Science 2007, pages 465–476. 2007.
↑158

[CR1995] M. Crochemore and W. Rytter. Squares, cubes, and time-space eﬃcient
string searching. Algorithmica 13 (5):405–425, 1995. ↑133, 136

[CR2002] M. Crochemore and W. Rytter. Jewels of stringology. World Scientiﬁc
Publishing Co. Inc., River Edge, NJ, 2002. ↑146, 155

[Cur1993] J. Currie. Unsolved Problems: Open Problems in Pattern Avoidance.
Amer. Math. Monthly 100 (8):790–793, 1993. ↑164

[CMN2007] J. D. Currie and M. Mohammad-Noori. Dejean’s conjecture and Stur-
mian words. European J. Combin. 28 (3):876–890, 2007. ↑159

[CV2007] J. D. Currie and T. I. Visentin. On Abelian 2-avoidable binary patterns.
Acta Inform. 43 (8):521–533, 2007. ↑164

[CF1989] T. W. Cusick and M. E. Flahive. The Markoﬀ and Lagrange spectra.
Mathematical Surveys and Monographs, vol. 30. American Mathematical Soci-
ety, Providence, RI, 1989. ↑68, 79

[Dav1992] H. Davenport. The higher arithmetic: An introduction to the theory of
numbers. Cambridge University Press, Cambridge, Sixth, 1992. ↑57

[Dej1972] F. Dejean. Sur un th´eor`eme de Thue. J. Combinatorial Theory Ser. A
13:90–99, 1972. ↑158

[Dek1979] F. M. Dekking. Strongly nonrepetitive sequences and progression-free
sets. J. Combin. Theory Ser. A 27 (2):181–185, 1979. ↑160, 164

BIBLIOGRAPHY 175

[Dic1930] L. E. Dickson. Studies in the theory of numbers. U. Chicago Press, 1930.
Reprinted as Introduction to the theory of numbers, Dover Publications (1957).
↑68, 69

[DB1937] H. L. Dorwart and O. E. Brown. The Tarry-Escott Problem. Amer. Math.
Monthly 44 (10):613–626, 1937. ↑86

[DGB1990] S. Dulucq and D. Gouyou-Beauchamps. Sur les facteurs des suites de
Sturm. Theoret. Comput. Sci. 71 (3):381–400, 1990. ↑50

[Duv1983] J.-P. Duval. Factorizing words over an ordered alphabet. J. Algorithms
4 (4):363–381, 1983. ↑50

[Erd1961] P. Erd˝os. Some unsolved problems. Magyar Tud. Akad. Mat. Kutat´o Int.
K¨ozl. 6:221–254, 1961. ↑160

[Evd1968] A. A. Evdokimov. Strongly asymmetric sequences generated by a ﬁ-
nite number of symbols. Dokl. Akad. Nauk SSSR 179:1268–1271, 1968. English
translation in Soviet Math. Dokl. 9 (1968), 536–539. ↑161

[FM1997] S. Ferenczi and C. Mauduit. Transcendence of numbers with a low com-
plexity expansion. J. Number Theory 67 (2):146–161, 1997. ↑169

[FS1998] A. S. Fraenkel and J. Simpson. How many squares can a string contain?.
J. Combin. Theory Ser. A 82 (1):112–120, 1998. ↑136, 137, 138

[Fro1913] F. G. Frobenius. ¨Uber die Markoﬀschen Zahlen. Sitzungsberichte der
K¨oniglich Preussischen Akademie der Wissenschaften, Berlin, 1913. Also in:
Frobenius, F.G., Gesammelte Abhandlungen, Springer-Verlag, 1968, vol. 3, 598–
627, ed. J.-P. Serre. ↑69, 71

[Fur1967] H. Furstenberg. Algebraic functions over ﬁnite ﬁelds. J. Algebra 7:271–
277, 1967. ↑97

[Gau1986] C. F. Gauss. Disquisitiones arithmeticae. Springer-Verlag, New York,
1986. Translated and with a preface by Arthur A. Clarke, revised by William
C. Waterhouse, Cornelius Greither and A. W. Grootendorst and with a preface
by Waterhouse. ↑68

[GR1993] I. M. Gessel and C. Reutenauer. Counting permutations with given cycle
structure and descent set. J. Combin. Theory Ser. A 64 (2):189–215, 1993. ↑48

[GLS2008] A. Glen, A. Lauve, and F. V. Saliola. A note on the Markoﬀ condition
and central words. Inform. Process. Lett. 105 (6):241–244, 2008. ↑74, 79

[GV1991] P. Goralˇc´ık and T. Vanicek. Binary patterns in binary words. Internat.
J. Algebra Comput. 1 (3):387–391, 1991. ↑130

[GKP1994] R. L. Graham, D. E. Knuth, and O. Patashnik. Concrete mathematics:
a foundation for computer science. Addison-Wesley Longman Publishing Co.,
Inc., Boston, MA, USA, 1994. ↑57, 64

176 BIBLIOGRAPHY

[Gus1997] D. Gusﬁeld. Algorithms on strings, trees, and sequences. Cambridge Uni-
versity Press, Cambridge, 1997. Computer science and computational biology.
↑146, 148, 149, 153

[GS2002] D. Gusﬁeld and J. Stoye. Simple and ﬂexible detection of contiguous
repeats using a suﬃx tree (preliminary version). Theoret. Comput. Sci. 270 (1-
2):843–856, 2002. ↑154

[Hal1964] M. Jr. Hall. Generators and relations in groups—The Burnside problem.
In Lectures on modern mathematics, vol. ii, pages 42–92. 1964. ↑121

[HYY2003] H. K. Hsiao, Y. T. Yeh, and S. S. Yu. Square-free-preserving and
primitive-preserving homomorphisms. Acta Math. Hungar. 101 (1-2):113–130,
2003. ↑125

[Ili2007] L. Ilie. A note on the number of squares in a word. Theoretical Computer
Science 380 (3):373–376, 2007. ↑137

[Jac1956] N. Jacobson. Structure of rings. American Mathematical Society, Collo-
quium Publications, vol. 37. American Mathematical Society, 190 Hope Street,
Prov., R. I., 1956. ↑168

[JZ2004] O. Jenkinson and L. Q. Zamboni. Characterisations of balanced words via
orderings. Theoret. Comput. Sci. 310 (1-3):247–271, 2004. ↑52

[Jus2005] J. Justin. Episturmian morphisms and a Galois theorem on continued
fractions. Theor. Inform. Appl. 39 (1):207–215, 2005. ↑30, 36

[KR2007] C. Kassel and C. Reutenauer. Sturmian morphisms, the braid group B4,
Christoﬀel words and bases of F2. Ann. Mat. Pura Appl. (4) 186 (2):317–339,
2007. ↑43

[Ker1986] V. Ker¨anen. On the k-freeness of morphisms on free monoids. Ann. Acad.
Sci. Fenn. Ser. A I Math. Dissertationes 61:55, 1986. ↑130

[Ker1987] V. Ker¨anen. On the k-freeness of morphisms on free monoids. In STACS
87 (Passau, 1987), pages 180–188. 1987. ↑130

[Ker1992] V. Ker¨anen. Abelian squares are avoidable on 4 letters. In Automata,
languages and programming (Vienna, 1992), pages 41–52. 1992. ↑161

[KK1999a] R. Kolpakov and G. Kucherov. Finding maximal repetitions in a word
in linear time. In 40th annual symposium on foundations of computer science
(New York, 1999), pages 596–604. 1999. ↑158

[KK1999b] R. Kolpakov and G. Kucherov. On maximal repetitions in words. In
Fundamentals of computation theory (Ia¸si, 1999), pages 374–385. 1999. ↑158

[KZ1873] A. Korkine and G. Zolotareﬀ. Sur les formes quadratiques. Math. Ann. 6
(3):366–389, 1873. ↑67

[LS1993] G. M. Landau and J. P. Schmidt. An algorithm for approximate tandem
repeats. In Proc. 4th annual symposium on comb. pattern matching, pages 120–
133. 1993. ↑154

BIBLIOGRAPHY 177

[LV1986] G. M. Landau and U. Vishkin. Introducing eﬃcient parallelism into ap-
proximate string matching and a new serial algorithm. In Proc. 18th annual
ACM symposium on theory of computing, pages 220–230. 1986. ↑154

[Lec1985] M. Leconte. A characterization of power-free morphisms. Theoret. Com-
put. Sci. 38 (1):117–122, 1985. ↑130

[LZ1970] A. Lempel and J. Ziv. On a homomorphism of the de Bruijn graph and
its applications to the design of feedback shift registers. IEEE Transactions on
Computers 19 (12):1204–1209, 1970. ↑95

[LZ1976] A. Lempel and J. Ziv. On the complexity of ﬁnite sequences. IEEE Trans-
actions on Information Theory 22:75–81, 1976. ↑142

[Lot1997] M. Lothaire. Combinatorics on words. Cambridge Mathematical Library.
Cambridge University Press, Cambridge, 1997. ↑50, 122, 157

[Lot2002] M. Lothaire. Algebraic combinatorics on words. Encyclopedia of Math-
ematics and its Applications, vol. 90. Cambridge University Press, Cambridge,
2002. ↑5, 9, 15, 50, 52, 53, 157, 164, 167, 168

[Lot2005] M. Lothaire. Applied combinatorics on words. Encyclopedia of Mathe-
matics and its Applications, vol. 105. Cambridge University Press, Cambridge,
2005. ↑137

[dL1997] A. de Luca. Sturmian words: structure, combinatorics, and their arith-
metics. Theoret. Comput. Sci. 183 (1):45–82, 1997. ↑28, 29, 30, 33

[dLM1994] A. de Luca and F. Mignosi. Some combinatorial properties of Sturmian
words. Theoret. Comput. Sci. 136 (2):361–385, 1994. ↑12, 37, 50

[dLV1989] A. de Luca and S. Varricchio. Some combinatorial properties of the
Thue-Morse sequence and a problem in semigroups. Theoret. Comput. Sci. 63
(3):333–348, 1989. ↑99

[dLV1999] A. de Luca and S. Varricchio. Finiteness and regularity in semigroups
and formal languages. Monographs in Theoretical Computer Science. An EATCS
Series. Springer-Verlag, Berlin, 1999. ↑168

[Luc1893] ´E. Lucas. R´ecr´eations math´ematiques, Vol. 3. Gauthier-Villars et Fils,
Paris, 1893. Reprinted by Librairie Scientiﬁque et Technique Albert Blanchard,
Paris, 1979. ↑112

[LS2001] R. C. Lyndon and P. E. Schupp. Combinatorial group theory. Classics in
Mathematics. Springer-Verlag, Berlin, 2001. Reprint of the 1977 edition. ↑43

[MKS2004] W. Magnus, A. Karrass, and D. Solitar. Combinatorial group theory:
Presentations of groups in terms of generators and relations. Dover Publications
Inc., Mineola, NY, second edition, 2004. ↑43

[MRS2003] S. Mantaci, A. Restivo, and M. Sciortino. Burrows-Wheeler transform
and Sturmian words. Inform. Process. Lett. 86 (5):241–246, 2003. ↑48

178 BIBLIOGRAPHY

[Man2001] G. Manzini. An analysis of the Burrows-Wheeler transform. J. ACM 48
(3):407–430, 2001. ↑48

[Mar1879] A. Markoﬀ. Sur les formes quadratiques binaires ind´eﬁnies. Math. Ann.
15 (3):381–406, 1879. ↑3, 67, 68, 70

[Mar1880] A. Markoﬀ. Sur les formes quadratiques binaires ind´eﬁnies. Math. Ann.
17 (3):379–399, 1880. (second memoire). ↑3, 67, 68, 70

[Mar1881] A. Markoﬀ. Sur une question de Jean Bernoulli. Math. Ann. 19 (1):27–
36, 1881. ↑3, 67

[McC1976] E. M. McCreight. A space-economical suﬃx tree construction algo-
rithm. J. Assoc. Comput. Mach. 23 (2):262–272, 1976. ↑148

[Mel1999] G. Melan¸con, Visualisation de graphes et combinatoire des mots. Th`ese
d’Habilitation `a Diriger les Recherches. Universit´e Bordeaux I, 1999. ↑51

[Men2003] F. Mendivil. Fractals, graphs, and ﬁelds. Amer. Math. Monthly 110
(6):503–515, 2003. ↑95

[Mig1991] F. Mignosi. On the number of factors of Sturmian words. Theoret. Com-
put. Sci. 82 (1, Algorithms Automat. Complexity Games):71–84, 1991. ↑169

[MP1992] F. Mignosi and G. Pirillo. Repetitions in the Fibonacci inﬁnite word.
RAIRO Inform. Th´eor. Appl. 26 (3):199–204, 1992. ↑169

[MS1993] F. Mignosi and P. S´e´ebold. Morphismes Sturmiens et r`egles de Rauzy. J.
Th´eor. Nombres Bordeaux 5 (2):221–233, 1993. ↑15

[Mor2004] E. Moreno. On the theorem of Fredricksen and Maiorana about de Bruijn
sequences. Adv. in Appl. Math. 33 (2):413–415, 2004. ↑95

[MH1940] M. Morse and G. A. Hedlund. Symbolic dynamics II. Sturmian trajec-
tories. Amer. J. Math. 62:1–42, 1940. ↑53

[MH1944] M. Morse and G. A. Hedlund. Unending chess, symbolic dynamics and
a problem in semigroups. Duke Math. J. 11:1–7, 1944. ↑120, 121, 122

[MO1992] J. Moulin-Ollagnier. Proof of Dejean’s conjecture for alphabets with
5, 6, 7, 8, 9, 10 and 11 letters. Theoret. Comput. Sci. 95 (2):187–205, 1992. ↑159

[Mye1986] E. W. Myers. An O(N D) diﬀerence algorithm and its variations. Algo-
rithmica 1 (1):251–266, 1986. ↑154

[OZ1981] R. P. Osborne and H. Zieschang. Primitives in the free group on two
generators. Invent. Math. 63 (1):17–24, 1981. ↑3, 43

[Pan1984] J.-J. Pansiot. `A propos d’une conjecture de F. Dejean sur les r´ep´etitions
dans les mots. Discrete Appl. Math. 7 (3):297–311, 1984. ↑159

[Pir1999] G. Pirillo. A new characteristic property of the palindrome preﬁxes of a
standard Sturmian word. S´em. Lothar. Combin. 43:Art. B43f, 3 pp. (electronic),
1999. ↑47

BIBLIOGRAPHY 179

[Ple1970] P. A. B. Pleasants. Non-repetitive sequences. Proc. Cambridge Philos.
Soc. 68:267–274, 1970. ↑161

[Pro1851] E. Prouhet. M´emoire sur quelques relations entre les puissances des nom-
bres. C. R. Acad. Sci. Paris. S´er. I 33:225, 1851. ↑86, 87

[PF2002] N. Pytheas Fogg. Substitutions in dynamics, arithmetics and combina-
torics. Lecture Notes in Mathematics, vol. 1794. Springer-Verlag, Berlin, 2002.
Edited by V. Berth´e, S. Ferenczi, C. Mauduit and A. Siegel. ↑5

[Ram2007] N. Rampersad. On the context-freeness of the set of words containing
overlaps. Inform. Process. Lett. 102 (2-3):74–78, 2007. ↑109, 110

[Ran1973] G. N. Raney. On continued fractions and ﬁnite automata. Math. Ann.
206:265–283, 1973. ↑34

[Rau1984] G. Rauzy. Des mots en arithm´etique. In Avignon conference on language
theory and algorithmic complexity (Avignon, 1983), pages 103–113. 1984. ↑23

[Reu2005] C. Reutenauer. Mots de Lyndon g´en´eralis´es. S´em. Lothar. Combin.
54:Art. B54h, 16 pp. (electronic), 2005. ↑68

[Reu2006] C. Reutenauer. On Markoﬀ’s property and Sturmian words. Math. Ann.
336 (1):1–12, 2006. ↑68, 74, 75, 76, 79

[Ric2003] G. Richomme. Some non ﬁnitely generated monoids of repetition-free
endomorphisms. Inform. Process. Lett. 85 (2):61–66, 2003. ↑124

[RW2002] G. Richomme and F. Wlazinski. Some results on k-power-free mor-
phisms. Theoret. Comput. Sci. 273 (1-2):119–142, 2002. WORDS (Rouen, 1999).
↑124

[RW2004] G. Richomme and F. Wlazinski. Overlap-free morphisms and ﬁnite test-
sets. Discrete Appl. Math. 143 (1-3):92–109, 2004. ↑125

[RW2007] G. Richomme and F. Wlazinski. Existence of ﬁnite test-sets for k-power-
freeness of uniform morphisms. Discrete Appl. Math. 155 (15):2001–2016, 2007.
↑125

[Rob2005] W. Robertson. Square cells: an array cooking lesson. The PracTEX Jour-
nal 2, 2005. ↑vii

[Ryt2006] W. Rytter. The number of runs in a string: improved analysis of the
linear upper bound. In STACS 2006, pages 184–195. 2006. ↑158

[Ryt2007] W. Rytter. The number of runs in a string. Information and Computation
205 (9):1459–1469, 2007. ↑158

[Sch1961] M. P. Sch¨utzenberger. On a special class of recurrent events. Ann. Math.
Statist. 32:1201–1213, 1961. ↑168

[S´e´e1982] P. S´e´ebold. Morphismes it´er´es, mot de Morse et mot de Fibonacci. C. R.
Acad. Sci. Paris S´er. I Math. 295 (6):439–441, 1982. ↑99

180 BIBLIOGRAPHY

[Ser1985] C. Series. The geometry of Markoﬀ numbers. Math. Intelligencer 7 (3):20–
29, 1985. ↑54

[Shi1962] A. I. Shirshov. Bases of free Lie algebras. Algebra i Logika 1:14–19, 1962.
↑51

[Sim2004] J. Simpson. Disjoint Beatty sequences. Integers 4:A12, 10 pp. (elec-
tronic), 2004. ↑8

[ˇSir1957] A. I. ˇSirˇsov. On some non-associative null-rings and algebraic algebras.
Mat. Sb. N.S. 41(83):381–394, 1957. ↑168

[Smi1876] H. J. S. Smith. Note on continued fractions. Messenger Math. 6:1–14,
1876. ↑3, 54, 58, 59, 145

[Sta1997] R. P. Stanley. Enumerative combinatorics. Vol. 1. Cambridge Studies in
Advanced Mathematics, vol. 49. Cambridge University Press, Cambridge, 1997.
With a foreword by Gian-Carlo Rota, Corrected reprint of the 1986 original.
↑146

[Sta1999] R. P. Stanley. Enumerative combinatorics. Vol. 2. Cambridge Studies in
Advanced Mathematics, vol. 62. Cambridge University Press, Cambridge, 1999.
With a foreword by Gian-Carlo Rota and appendix 1 by Sergey Fomin. ↑96

[Thu1906] A. Thue. ¨Uber unendliche zeichenreihen. Norske Vidensk. Selsk. Skrifter,
I. Math.-Naturv. Kl. 7:1–22, 1906. reprinted in A. Thue, Selected Mathematical
Papers, Nagell, Selberg, Selberg, eds. (1977) pp. 139–158. ↑119, 120, 160

[Thu1912] A. Thue. ¨Uber die gegenseitige lage gleicher teile gewisser zeichenreihen.
Norske Vidensk. Selsk. Skrifter, I. Math.-Naturv. Kl. 1:1–67, 1912. reprinted in
A. Thue, Selected Mathematical Papers, Nagell, Selberg, Selberg, eds. (1977) pp.
413–477. ↑98

[TS1995] J. Tromp and J. Shallit. Subword complexity of a generalized Thue-Morse
word. Inform. Process. Lett. 54 (6):313–316, 1995. ↑99

[Ukk1995] E. Ukkonen. On-line construction of suf-
ﬁx trees. Algorithmica 14 (3):249–260, 1995. See also
http://www.allisons.org/ll/AlgDS/Tree/Suffix, where it really is online.
↑149

[Vie1978] X. G. Viennot. Alg`ebres de Lie libres et mono¨ıdes libres. Lecture Notes
in Mathematics, vol. 691. Springer, Berlin, 1978. Bases des alg`ebres de Lie libres
et factorisations des mono¨ıdes libres. ↑51

[Wei1973] P. Weiner. Linear pattern matching algorithms. In 14th annual IEEE
symposium on switching and automata theory (Univ. Iowa, Iowa City, Iowa,
1973), pages 1–11. 1973. ↑148

[Wel1984] T. A. Welch. A technique for high-performance data compression. Com-
puter 17:8–19, 1984. ↑142

BIBLIOGRAPHY 181

[WW1994] Z. X. Wen and Z. Y. Wen. Local isomorphisms of invertible substitu-
tions. C. R. Acad. Sci. Paris S´er. I Math. 318 (4):299–304, 1994. ↑15, 46

[Wri1959] E. M. Wright. Prouhet’s 1851 solution of the Tarry-Escott problem of
1910. Amer. Math. Monthly 66 (3):199–201, 1959. ↑86, 87

[Zim1982] A. I. Zimin. Blocking sets of terms. Mat. Sb. (N.S.) 119(161) (3):363–
375, 447, 1982. ↑160, 165, 166
Index

N, vii
|w|a, vii
m∞, viii
a ⊥ b, 3
C(a, b), 4
xxyxxyxxyxy, 5, 19, 23, 29, 30, 37, 54,
59
G, 9, 23, 30, 76
D, 9, 30
̃G, 9
̃D, 9, 23, 76
E, 9
G, 10, 25
̃D, 11
SL2(Z), 21
Pal, 29
w+, 29
N2×2, 38
P, 69
R>0, 69
λi(A), 69
M (A), 69
t, 83
¯s, 84
ϕ
∞, 85
bin(n), 94
Fq, 97, 98
ct(n), 99
Han(n, i, j), 112, 116
C(h), 126
O (n), 136
w(i, j), 139
w(i), 139
w(i), 139⪖, 139, 146⪕, 139
 πw(u), 143, 147
Suﬀ(w), 146
rt(n), 158
.
=, 165

Abelian k-avoidable, 160
Abelian instance, 160
accepted by an automaton, 105
algebraic series, 96, 110
alphabet, vii
alternating lexicographic order, 71, 75
anagram, 160
aperiodic sequence, 53
k-automatic sequence, 94
automatic sequences, 115
automaton, 93, see ﬁnite determinis-
tic, 105
pushdown, 107
k-avoidable pattern, 160
k-avoidable set, 165

B´ezout’s Lemma, 22, 23, 44, 64
balanced1, 50, 53, 79
balanced2, 51
basis, 41, see free group
bi-ideal sequence, 167
biﬁx code, 126
big-O, 136
binary quadratic form, 67
discriminant of a, 67
equivalent, 67
minimum of a, 67
reduced, 68
binary word, 83
bissective code, 130
block, 72, 86

182

INDEX 183

Burrows–Wheeler transform, 48

Cayley graph, 6, 36, 37, 47
centered square, 138
left-, 138
right-, 138
Chomsky hierarchy, 104
Christoﬀel morphism, 9, 26, 46
G, D, ̃G, ̃D and E, 9
Christoﬀel path, 4, 59
closest point for a, 19
lower, 3
slope, 3
upper, 4
Christoﬀel tree, 44, 57, 61, 63
Christoﬀel word, 4
lower, 4, 7
nontrivial, 4, 28
of slope 4
7 , 5, 19, 23, 29, 30, 37,
54, 59
slope, 4
standard factorization, 19, 30, 44
trivial, 4, 5
upper, 4, 27
circular word, 51, 95
closest point, 19
code, 125
biﬁx, 126
bissective, 130
comma-free, 127
faithful, 130
inﬁx, 126
left synchronizing, 130
preﬁx, 125
preﬁx-suﬃx, 130
ps-code, 130
right synchronizing, 130
strongly synchronizing, 130
suﬃx, 125
synchronizing, 130
uniform, 126
comma-free code, 127
compact suﬃx tree, 148
complexity function, 99
conjugate
 group-theoretic, 14, 42
monoid-theoretic, viii, 14, 42
root, 5, 61, 77
contain, viii
context-free grammar, 107
derivation, 107
leftmost derivation, 109
context-free language, 104, 107
pumping lemma for a, 110
unambiguous, 109
continuant, 58
continued fraction, 57, 71
continuant, 58
representation, 57
cover relation, 146
covers, 146
critical exponent, 158, 169
Crochemore factorization, 143
cutting sequence, 5

de Bruijn word, 95, 96
degree, 87, see Tarry-Escott
derivation, 107
derived, 107
diagonal, 97, see generating series
discretization, 3, 168
discriminant, 67
n-division, 168

empty word, vii
erasing morphism, 16
exponent, 158
critical, 158, 169
extendible repetition, 157
extreme point, 60

factor, viii
left special, 100, 102
proper, viii
right special, 100
Factor Problem, 146
factorization, viii
Crochemore, 143
n-division, 168
left Lyndon, 51

184 INDEX

right Lyndon, 50
standard, 19, 30
faithful code, 130
Fibonacci, 146
number, 61, 96, 136, 138
word, 5, 70, 122, 123, 136, 145,
168
words, 136, 145
ﬁnal states, 93, see ﬁnite deterministic
automaton
Fine-Wilf Theorem, 39, 48, 137
ﬁnite deterministic automaton, 93, 96,
105, 106, 111, 115, 123, 148
ﬁnal states, 93
initial state, 93
next state function, 93
states, 93
ﬁrst occurrence, 143, 147
πw(u), 143, 147
formal language theory, 104
forumlae of Justin, 30–33
fractal rendering, 95
fractional power, 159
free group, 41
basis, 41
inner automorphism, 43
positive element, 42
primitive element, 41

generalized Thue-Morse word, 88
generating series, 96
algebraic, 96
diagonal, 97
Fibonacci numbers, 96
rational, 96
transcendental, 96
golden ratio, 5, 61, 136
grammar, 107, see context-free

Hanoi word, 113
and Thue-Morse word, 115
automatic sequence, 115

ideal solution, see Tarry-Escott
identity morphism, viii
 implicit suﬃx tree, 149
index
recurrence, 102
starting, 143, 147
inﬁx code, 126
initial state, 93, see ﬁnite determinis-
tic automaton
inner automorphism, 43
instance
Abelian, 160
of a pattern, 159
iterate of an endomorphism, 85
iterated palindromic closure, 29

K¨onig’s Lemma, 164

label, 6, 19
language, 104, 148
context-free, 104, 107
regular, 104, 105
leaf node, 147
left factorization, 51
left special factor, 100, 102
left synchronizing code, 130
left-centered square, 138
leftmost derivation, 109
length
in the free group, 41
in the free monoid, vii
letter-doubling morphism, 102
letters, vii
Levi’s Lemma, 137
lexicographic order, 47
alternating, 71, 75
longest common preﬁx, 139⪖, 139
longest common suﬃx, 139⪕, 139
lower Christoﬀel word, 7
Lyndon word, 48, 50, 95, 168
left factorization, 51
right factorization, 50

magic square, 90
La Sagrada Fam´ılia, 90

INDEX 185

Melencolia I, 90
from the Thue-Morse word, 90
of order 2m, 90
order, 90
Markoﬀ numbers., 70
Markoﬀ spectrum, 79
maximal repetition, 157
mediant, 62
minimal period, 157
k-mismatch, 154
morphism, viii
Christoﬀel, 9, 46
erasing, 16
exchange, 84
ﬁxed point of a, 85
Hall, 121, 124
identity, viii
iterate, 85
letter-doubling, 102
nonerasing, 16, 125
period-doubling, 114
positive, 46
square-free, 123
k-square-free, 124
Thue–Morse, 84
trivial, viii, 123
uniform, 124
k-uniform, 84
morphism
k-uniform, 94
morphism of Hall, 121, 124

next state function, 93, see ﬁnite de-
terministic automaton
nonerasing morphism, 16, 125
nonextendible repetition, 157
nontrivial Christoﬀel word, 28

occurrence, 157
extendible repetition, 157
nonextendible repetition, 157
number of, vii, 31, 133
of a factor, viii
starting index, viii, 99, 143
Open Question
 Thue-Morse generating series, 98
context-free language of non-factors
of t, 109
Markoﬀ numbers, 71
order, 90, see magic square
overlap, 98, 137
overlap-free word, 98

palindrome, viii, 15, 27, 74
palindromic closure, 29
palindromic preﬁx, 28, 33
palindromic suﬃx, 28
path, 147
pattern, 159
Abelian k-avoidable, 160
Abelian instance of a, 160
k-avoidable, 160
k-avoidable set, 165
instance of a, 159
k-unavoidable, 165
k-unavoidable set, 165
period, 30, 33
minimal, 157
period-doubling morphism, 114
periodic phenomena, 54
periodic sequences, 53
Pick’s Theorem, 21–23
poset
cover relation, 146
covers, 146
position, 147
positive element, 42
positive morphism, 46
k-th-power-free word, 119
preﬁx, viii
longest common, 139
palindromic, 28, 33
proper, viii
preﬁx array, 140
preﬁx code, 125
preﬁx poset, 133, 146
preﬁx-suﬃx code, 130
primitive element, 41
primitive word, 5, 41, 133
productions, 107

186 INDEX

proper factor, viii
ps-code, 130
pumping lemma
for context-free languages, 110
for regular languages, 105
pumping length
for regular languages, 105
pushdown automata, 107

quadratic form
binary, 67
equivalent, 67
minumum of a, 67
reduced, 68
quadratic number, 77

rational series, 96, 110
recurrence index, 102
recurrent, 102
uniformly recurrent, 102
recurrent word, 168
reduced word, 41
regular language, 104, 105
pumping lemma for a, 105
rejected by an automaton, 105
relatively prime, 3
repetition, 157
extendible, 157
maximal, 157
nonextendible, 157
repetition threshold, 158
reversal, vii, 15, 27
right factorization, 50
right special factor, 100
right synchronizing code, 130
right-centered square, 138
root node, 147
run, 157

sequence
aperiodic, 53
bi-ideal, 167
cutting, 5
periodic, 53
ultimately periodic, 53, 106, 110
 sesquipowers, 167
shift registers, 95
size, 87, see Tarry-Escott
skew-words, 53
square
centered, 138
left-centered, 138
right-centered, 138
square-free morphism, 123
k-square-free morphism, 124
square-free word, 119
standard factorization, 19, 26, 44, 63
starting index, viii, 99, 143, 147
πw(u), 143, 147
starting position, see starting index
states, 93, see ﬁnite deterministic au-
tomaton
Stern–Brocot tree, 57, 63
strongly synchronizing code, 130
Sturmian word, 5, 50, 53, 159
characteristic, 5, 169
suﬃx, viii
longest common, 139
palindromic, 28
proper, viii
Suﬀ(w), 146
suffix, 147
suﬃx array, 140
suﬃx code, 125
suﬃx link, 152
suﬃx node, 147
suﬃx tree, 147
T (w), 147
compact, 148
implicit, 149
leaf node, 147
path, 147
position, 147
root node, 147
suffix, 147
suﬃx node, 147
unadorned, 146
synchronizing code, 130
left, 130
right, 130

INDEX 187

strongly, 130

Tarry-Escott problem, 86
Thue-Morse word, 87
degree of a, 87
ideal solution, 89
Prouhet’s solution, 87
size of a, 87
terminal letters, 107
test set for square-freeness, 124
Three Squares Lemma, 134
Thue-Morse morphism, 84, 95
Thue–Morse word, 83, 94, 96, 98, 103,
106, 108, 116
and Hanoi word, 115
automaton, 94
complexity function, 100
generalized, 88
generating series, 97
Toeplitz sequence, 117
Toeplitz word, 117
Tower of Hanoi, 111
transcendental series, 96, 110
trivial morphism, viii, 123

ultimately periodic, 53, 106, 110
unadorned suﬃx tree, 146
unambiguous context-free language, 109
k-unavoidable pattern, 165
k-unavoidable set, 165
uniform code, 126
uniform morphism, 124
k-uniform morphism, 84, 94
uniformly recurrent, 102
upper Christoﬀel word, 27

variables, 107

word, vii
accepted, 105
anagram of a, 160
as a ﬁxed point of a morphism, 85
balanced1, 50
balanced2 Lyndon, 51
binary, 83
characteristic Sturmian, 5, 169
 Christoﬀel, 4
circular, 51, 95
conjugate, 5
contains, viii
critical exponent, 158, 169
de Bruijn, 95
derived, 107
exponent, 158
factor of, viii
Fibonacci, 123, 145, 168
fractional power, 159
Hanoi, 113
inﬁnite, viii
Lyndon, 48, 50, 95, 168
minimal period, 157
occurrence, viii, 157
overlap, 98, 137
overlap-free, 98
pattern, 159
k-th-power-free, 119
primitive, 5, 41, 133
recurrence index, 102
recurrent, 102, 168
reduced, 41
rejected, 105
repetition, 157
reversal, 27
square-free, 119
Sturmian, 53, 159
Thue–Morse, 83
Toeplitz, 117
ultimately periodic, 106
uniformly recurrent, 102
Zimin, 164

Zimin word, 164
