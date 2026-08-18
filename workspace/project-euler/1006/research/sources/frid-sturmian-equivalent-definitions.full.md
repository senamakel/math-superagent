<!-- source: https://www.i2m.univ-amu.fr/wiki/Combinatorics-on-Words-seminar/_media/lectures:lecture8slidessturmian.pdf | converted from PDF -->

Sturmian words: equivalent de˝nitions
 Anna FRID

Aix-Marseille Universit e, September 2020

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 1 / 26

De˝nition

The (factor) complexity pu(n) of an in˝nite word u is the number of its
distinct factors of length n.
 Theorem (Morse and Hedlund, 1938)

An in˝nite word u either is ultimately periodic, and then its complexity is
ultimately constant, or satis˝es pu(n) ≥ n + 1.

A word u of complexity pu(n) = n + 1 is called Sturmian .

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 2 / 26

De˝nition

The (factor) complexity pu(n) of an in˝nite word u is the number of its
distinct factors of length n.

Theorem (Morse and Hedlund, 1938)

An in˝nite word u either is ultimately periodic, and then its complexity is
ultimately constant, or satis˝es pu(n) ≥ n + 1.
 A word u of complexity pu(n) = n + 1 is called Sturmian .

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 2 / 26

De˝nition

The (factor) complexity pu(n) of an in˝nite word u is the number of its
distinct factors of length n.

Theorem (Morse and Hedlund, 1938)

An in˝nite word u either is ultimately periodic, and then its complexity is
ultimately constant, or satis˝es pu(n) ≥ n + 1.

A word u of complexity pu(n) = n + 1 is called Sturmian .

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 2 / 26

Fibonacci word

Example (Fibonacci morphism)
 ϕ(0) = 01, ϕ(1) = 0

0 → 01 → 01 0 → 010 01 → 01001 010 → 01001010 01001 → · · ·

Its ˝xed point is the Fibonacci word

ϕ
ω(0) = 0100101001001010010100100101001001 · · ·
 Lemma
The Fibonacci word is Sturmian.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 3 / 26

Fibonacci word

Example (Fibonacci morphism)
 ϕ(0) = 01, ϕ(1) = 0

0 → 01 → 01 0 → 010 01 → 01001 010 → 01001010 01001 → · · ·

Its ˝xed point is the Fibonacci word

ϕ
ω(0) = 0100101001001010010100100101001001 · · ·

Lemma
The Fibonacci word is Sturmian.
 Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 3 / 26

Balanced words

Let |u|a denote the number of occurrences of a to u

|01001|1 = 2
 An in˝nite word w over {0, 1} is said to be balanced if for every two its
factors x and y of the same length we have
 δ(x, y ) = ||x|1 − |y |1| ≤ 1.

Example
 01001 01001 01001 01001 · · ·

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 4 / 26

Balanced words

Let |u|a denote the number of occurrences of a to u

|01001|1 = 2

An in˝nite word w over {0, 1} is said to be balanced if for every two its
factors x and y of the same length we have
 δ(x, y ) = ||x|1 − |y |1| ≤ 1.
 Example
 01001 01001 01001 01001 · · ·

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 4 / 26

Balanced words

Let |u|a denote the number of occurrences of a to u

|01001|1 = 2

An in˝nite word w over {0, 1} is said to be balanced if for every two its
factors x and y of the same length we have
 δ(x, y ) = ||x|1 − |y |1| ≤ 1.

Example
 01001 01001 01001 01001 · · ·

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 4 / 26

Equivalence I

Theorem
A right in˝nite word is Sturmian if and only if it is aperiodic and balanced.
 Idea of the proof:
 In a balanced set of factors of length n, there are at most n + 1
elements;

A set of factors F is not balanced ⇐⇒ there exists a strong bispecial
w | 0w 0, 1w 1 ∈ F .

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 5 / 26

Equivalence I

Theorem
A right in˝nite word is Sturmian if and only if it is aperiodic and balanced.

Idea of the proof:
 In a balanced set of factors of length n, there are at most n + 1
elements;
 A set of factors F is not balanced ⇐⇒ there exists a strong bispecial
w | 0w 0, 1w 1 ∈ F .

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 5 / 26

Equivalence I

Theorem
A right in˝nite word is Sturmian if and only if it is aperiodic and balanced.

Idea of the proof:
 In a balanced set of factors of length n, there are at most n + 1
elements;

A set of factors F is not balanced ⇐⇒ there exists a strong bispecial
w | 0w 0, 1w 1 ∈ F .

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 5 / 26

One- and two-sided words

A typical Sturmian word may start for example with
 001000100100010001001000100100 · · ·
 Attention: · · · 00000010000000 · · ·

is not considered to be Sturmian, even though its complexity is n + 1. It is
two-sided and half-periodic.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 6 / 26

One- and two-sided words

A typical Sturmian word may start for example with
 001000100100010001001000100100 · · ·

Attention: · · · 00000010000000 · · ·

is not considered to be Sturmian, even though its complexity is n + 1. It is
two-sided and half-periodic.
 Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 6 / 26

Slope of a word

De˝nition
The slope of a ˝nite word x over {0, 1} is

|x|1
|x| .
 The slope of an in˝nite word w over {0, 1} is the limit

π(w) = lim
n→∞ |w[0..n − 1]|1
n .

Lemma
Every balanced in˝nite word has a slope.

Lemma
A balanced word is periodic if and only if its slope is rational.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 7 / 26

Slope of a word

De˝nition
The slope of a ˝nite word x over {0, 1} is

|x|1
|x| .

The slope of an in˝nite word w over {0, 1} is the limit

π(w) = lim
n→∞ |w[0..n − 1]|1
n .
 Lemma
Every balanced in˝nite word has a slope.

Lemma
A balanced word is periodic if and only if its slope is rational.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 7 / 26

Slope of a word

De˝nition
The slope of a ˝nite word x over {0, 1} is

|x|1
|x| .

The slope of an in˝nite word w over {0, 1} is the limit

π(w) = lim
n→∞ |w[0..n − 1]|1
n .

Lemma
Every balanced in˝nite word has a slope.
 Lemma
A balanced word is periodic if and only if its slope is rational.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 7 / 26

Slope of a word

De˝nition
The slope of a ˝nite word x over {0, 1} is

|x|1
|x| .

The slope of an in˝nite word w over {0, 1} is the limit

π(w) = lim
n→∞ |w[0..n − 1]|1
n .

Lemma
Every balanced in˝nite word has a slope.

Lemma
A balanced word is periodic if and only if its slope is rational.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 7 / 26

Examples

Example

The slope of 01001 01001 01001 01001 · · ·

is 2/5.
 Example

The slope of the Fibonacci word 0 1 0 01 010 01001 01001010 · · · is

lim
n→∞ |ϕn(0)|1
|ϕn(0)| = lim
n→∞ Fn−2
Fn = 1
τ 2 ,

where τ = (1 + √5)/2.
 1
τ 2 = 0, 38 · · · .

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 8 / 26

Examples

Example

The slope of 01001 01001 01001 01001 · · ·

is 2/5.

Example

The slope of the Fibonacci word 0 1 0 01 010 01001 01001010 · · · is

lim
n→∞ |ϕn(0)|1
|ϕn(0)| = lim
n→∞ Fn−2
Fn = 1
τ 2 ,

where τ = (1 + √5)/2.
 1
τ 2 = 0, 38 · · · .

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 8 / 26

Mechanical words
 y = σx + ρ, 0 ≤ σ, ρ < 1.

1 0 1 0 0 1 0 1 0 1

w = w [0]w [1] · · ·

w [n] = ⌊(n + 1)σ + ρ⌋ − ⌊nσ + ρ⌋.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 9 / 26

Important choice
 ?

1 0

0 1

w [n] = ⌊(n + 1)σ + ρ⌋ − ⌊nσ + ρ⌋.

or

w [n] = ⌈(n + 1)σ + ρ⌉ − ⌈nσ + ρ⌉.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 10 / 26

Mechanical words

De˝nition
An in˝nite word w = w [0]w [1] · · · over {0, 1} is mechanical , if for all
n ≥ 0 we have w [n] = ⌊(n + 1)σ + ρ⌋ − ⌊nσ + ρ⌋,

or w [n] = ⌈(n + 1)σ + ρ⌉ − ⌈nσ + ρ⌉.

1 0 1 0 0 1 0 1 0 1Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 11 / 26

Mechanical words

De˝nition
An in˝nite word w = w [0]w [1] · · · over {0, 1} is mechanical , if for all
n ≥ 0 we have w [n] = ⌊(n + 1)σ + ρ⌋ − ⌊nσ + ρ⌋,

or w [n] = ⌈(n + 1)σ + ρ⌉ − ⌈nσ + ρ⌉.

1 0 1 0 0 1 0 1 0 1Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 11 / 26

Three equivalent de˝nitions

Theorem
For a right in˝nite word x over {0, 1}, the following conditions are
equivalent:
 px(n) = n + 1 ∀n;

x is a non-periodic balanced word;

x is a mechanical word with an irrational slope σ.
 If any of the conditions holds, the word is Sturmian.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 12 / 26

Three equivalent de˝nitions

Theorem
For a right in˝nite word x over {0, 1}, the following conditions are
equivalent:
 px(n) = n + 1 ∀n;

x is a non-periodic balanced word;

x is a mechanical word with an irrational slope σ.

If any of the conditions holds, the word is Sturmian.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 12 / 26

Mechanical words and rotations
 s
 0=1

r

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 13 / 26

Mechanical words and rotations
 s
 0=1

r

r+s

w = 1 · · ·

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 14 / 26

Mechanical words and rotations
 0=1

s
 r

r+sr+2s

w = 10 · · ·

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 15 / 26

Mechanical words and rotations
 0=1

s
 r

r+sr+2s

r+3s
 r+4s
 r+5s

w = 10001 · · ·

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 16 / 26

Complexity of rotation words

w [0] = 1 ⇐⇒ 1 − σ < ρ < 1
 -s
 0=1

The ˝rst symbol is determined by one of two intervals where ρ is located
pw(1) = 2

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 17 / 26

Complexity of rotation words

w [k] = 1 ⇐⇒ −kσ < ρ < −(k + 1)σ

-s
 0=1

-2s
 -ks
-3s

The pre˝x of length k is determined by one of k + 1 intervals where ρ is
located pw (k) = k + 1.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 18 / 26

Mechanical vs. billiard de˝nition
 x

y
 1

1
 y = σx + ρ

0 1 0 0 1

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 19 / 26

Mechanical vs. billiard de˝nition
 x

y
 1

1
 y = σx + ρ

0 10 0 0 10

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 20 / 26

Billiards

0
 0

1
 0

1

0 010001 · · ·

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 21 / 26

Billiard words are Sturmian

0
 0

1
 0

1

0 010001 · · ·

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 22 / 26

Properties of Sturmian words

Lemma
A Sturmian word is never k-automatic.
 Proof. The frequency of 1 in a Sturmian word is irrational (and equal
to the slope). In a k-automatic word, this frequency is rational.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 23 / 26

Properties of Sturmian words

Lemma
A Sturmian word is never k-automatic.

Proof. The frequency of 1 in a Sturmian word is irrational (and equal
to the slope). In a k-automatic word, this frequency is rational.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 23 / 26

Properties of Sturmian words

Lemma
The set of factors of a Sturmian word depends only on its slope.
 0=1

s
 r

r+sr+2s

r+3s
 r+4s
 r+5s
 So, for many arguments we may take ρ = σ. Such Sturmian words are
characteristic .

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 24 / 26

Properties of Sturmian words

Lemma
The set of factors of a Sturmian word depends only on its slope.
 0=1

s
 r

r+sr+2s

r+3s
 r+4s
 r+5s
 So, for many arguments we may take ρ = σ. Such Sturmian words are
characteristic .

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 24 / 26

Properties of Sturmian words

Lemma
The set of factors of a Sturmian word depends only on its slope.
 0=1

s
 r

r+sr+2s

r+3s
 r+4s
 r+5s

So, for many arguments we may take ρ = σ. Such Sturmian words are
characteristic .

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 24 / 26

Properties of Sturmian words

Lemma
The characteristic word cσ of slope σ can be constructed from the
continued fraction of σ.
 Let
 σ = 1

m1 + 1 + 1

m2 + 1

m3 + 1
m4 + · · ·
 = [0, m1 + 1, m2, m3, · · · ].

Then cσ = limn→∞ sn, where

s−1 = 1, s0 = 0, sn = s mn
n−1sn−2.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 25 / 26

Properties of Sturmian words

Lemma
The characteristic word cσ of slope σ can be constructed from the
continued fraction of σ.

Let
 σ = 1

m1 + 1 + 1

m2 + 1

m3 + 1
m4 + · · ·
 = [0, m1 + 1, m2, m3, · · · ].
 Then cσ = limn→∞ sn, where

s−1 = 1, s0 = 0, sn = s mn
n−1sn−2.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 25 / 26

Properties of Sturmian words

Lemma
The characteristic word cσ of slope σ can be constructed from the
continued fraction of σ.

Let
 σ = 1

m1 + 1 + 1

m2 + 1

m3 + 1
m4 + · · ·
 = [0, m1 + 1, m2, m3, · · · ].

Then cσ = limn→∞ sn, where

s−1 = 1, s0 = 0, sn = s mn
n−1sn−2.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 25 / 26

Example: the Fibonacci word

The slope of the Fibonacci word is
 1
τ 2 = [0, 2, 1, 1, 1, 1, · · · ], where τ = 1 + √5
2 .

s−1 = 1

s0 = 0

s1 = 01

s2 = 01 0

s3 = 010 01

s4 = 01001 010
 So, it is indeed the Fibonacci word.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 26 / 26

Example: the Fibonacci word

The slope of the Fibonacci word is
 1
τ 2 = [0, 2, 1, 1, 1, 1, · · · ], where τ = 1 + √5
2 .

s−1 = 1

s0 = 0

s1 = 01

s2 = 01 0

s3 = 010 01

s4 = 01001 010

So, it is indeed the Fibonacci word.

Anna FRID Sturmian words I Aix-Marseille Universit e, September 2020 26 / 26
