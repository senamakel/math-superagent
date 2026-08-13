<!-- source: https://math.osu.edu/sites/math.osu.edu/files/Egyptian_Fractions.pdf | converted from PDF -->

Egyptian fractions, Sylvester’s sequence, and the
Erdős-Straus conjecture

Ji Hoon Chun

Monday, August 1, 2011

1 Egyptian fractions

Many of these ideas are from the Wikipedia entry “Egyptian fractions.”

1.1 Introduction

An Egyptian fraction is a number of distinct unit fractions with positive denominators added
together.

Example. 2
7 = 1
4 + 1
28
1
5 = 1
5 (= 1
6 + 1
30 )
3
179 = 1
60 + 1
10740

The restriction on distinct unit fractions is needed, because otherwise all fractions can
easily be made into Egyptian fractions simply by using a
b = 1
b + · · · + 1
b . The Egyptians did
not represent 2
3 or 3
4 by unit fractions. (It can be though, 2
3 = 1
2 + 1
6 .)

1.2 History

1.2.1 Hieroglyphs

Ancient Egyptians represented a reciprocal of a number by placing a hieroglyph above the
number. The fractions 1
2 , 2
3 , and 3
4 had their own distinct symbols. (Clagett)

1.2.2 The Rhind Mathematical Papyrus

The Rhind Mathematical Papyrus is a document made around 1650 BC (during the Second
Intermediate Period) in the Egyptian Middle Kingdom. It was later bought by Henry Rhind,
and the papyrus was named after him. It was written by Ahmes (Ahmose). The papyrus is
divided into three parts. The ﬁrst part contains a list of Egyptian fraction representations
of 2
n for odd n from n = 3 to n = 101, as well as 40 problems. The second part is about
geometry, speciﬁcally volumes, areas, and pyramids. The third book contains 24 additional
problems. (Spalinger)
 1

1.2.3 Other ancient texts

Several other Egyptian papyri from earlier times have tables of Egyptian fractions. The
Lahun Mathematical Papyri (around 1850 BC) also had Egyptian fraction decompositions
for 2
n , the Egyptian Mathematical Leather Roll (around 1900 BC) had Egyptian fraction
decompositions for 1
n fractions, and the Akhmin wooden tablet (around 1950 BC) also
contains Egyptian fraction decompositions for 1
n fractions.

1.3 Methods to convert a non-Egyptian fraction into an Egyptian
fraction

1.3.1 Fractions in the form 1
n

• 1
n = 1
n+1 + 1
n(n+1)

1.3.2 Fractions in the form 2
n

• 2
n = 2
n+1 + 2
n(n+1)

• 2
n = 1
n + 1
2n + 1
3n + 1
6n

• 2
n = 1
2 1
n + 3
2 1
n (n is a multiple of 3)

• 2
n = 1
3 1
n + 5
3 1
n (n is a multiple of 5)

• 2
mn = 1
kn + 1
kmn (k = m+1
2 ) (Gardner 2002)

• 2
mn = 1
m 1
k + 1
n 1
k (k = m+n
2 ) (Eves 1953)

1.3.3 Fractions in the form m
n

• a
mn = 1
m 1
k + 1
n 1
k (k = m+n
a ) (Eves 1953)

• The greedy algorithm

1.4 The greedy algorithm

Some of these ideas are from the Wikipedia entry “Greedy algorithm for Egyptian fractions.”

1.4.1 Introduction

The greedy algorithm is a method that will convert any fraction into an Egyptian fraction.
m
n = 1
⌈ n
m ⌉ + −n (mod m)
n⌈ n
m ⌉ . If −nmod m ̸= 1, then repeat the method with −n (mod m)
n⌈ n
m ⌉
as the new “ m
n ” until all fractions are unit fractions. (Sigler 2002, Sylvester 1880)

2

5
31 = 1
7 + 4
217
1
7 + 1
55 + 3
11935
1
7 + 1
55 + 1
3979 + 2
47489365
1
7 + 1
55 + 1
3979 + 1
23744683 + 1
1127619917796295

0 < −n (mod m) < m. So, the numerator of the second fraction in the expansion
continues to decrease until it reaches 1. ⌈ n
m ⌉ < n (assuming n > m), so the denominator of
the ﬁrst fraction is smaller than the denominator of the original fraction. Also, n⌈ n
m ⌉ > n
(assuming n > m), so the denominators of the fractions increase every step.
No known algorithm gives the most concise Egyptian fraction representations of every
fraction (for either meaning of concise, least number of terms or smallest denominator). The
greedy algorithm may give many terms with large denominators when another method gives
fewer terms and smaller denominators. The above fraction can be written more concisely
as 5
31 = 1
7 + 1
62 + 1
434 , one of ﬁve representations of length 3.

1.4.2 Maximum-length expansions

Depending on the fraction m
n , the greedy algorithm may give m terms in the resulting
Egyptian fraction, or fewer than x terms. 1
n trivially has 1 term. 2
n always has 2 terms, as
(let n′ = n−1
2 ) 2
2n′+1 = 1
n′+1 + 1
(n′+1)(2n′+1) . Freitag and Phillips (1999) give a necessary
and suﬃcient condition for a fraction to have m terms.

Theorem. 1 For a fraction m
n , the greedy algorithm for Egyptian fractions gives m terms
if n = km! + 1 (k ∈ N).

Proof. Induction on m is used. The statement is true for m = 1. Consider some m ≥ 1.
Then for k ∈ N, m
km!+1 = 1
k(m−1)!+1 + m−1
k′(m−1)!+1 (where k′ = k (km! + m + 1)).

Theorem. 2 For a fraction m
n , a necessary condition for its greedy algorithm expansion to
have x terms is for y = km + 1 (k ∈ N).

Proof. n = km + r (0 ≤ r < m). Then m
km+r = 1
k+1 + m−r
(k+1)(km+r) . When r = 1,
m − r = m − 1.

From these two theorems it is possible to deduce the necessary and suﬃcient case. First
of all there is an important deﬁnition.

Deﬁnition. Let sets Sm (m ≥ 3) be deﬁned by the following rule: S3 = {0} and s ∈ Sm iﬀ
0 ≤ s < (m − 1)! and ms
2 + (m + 1) s ≡ t (m − 1) (mod (m − 1)!) (t ∈ Sm−1).

• S4 = {0, 4}

• S5 = {0, 6, 12, 18}

• S6 = {0, 18, 30, 48, 60, 78, 90, 108}
 3

Theorem. 3 A fraction m
n has m terms in its greedy algorithm expansion iﬀ n = km! +
sm + 1 (s ∈ Sm, k ≥ 0, and k and s are not both 0).

Proof. If m
n has m terms in its greedy algorithm expansion, from Theorem 2, n = (k (m − 1)! + s) m+
1 = km!+sm+1 (0 ≤ s < (m − 1)!). Then m
km!+sm+1 = 1
k(m−1)!+s+1 + m−1
(k(m−1)!+s+1)(km!+sm+1) .
Also, (k (m − 1)! + s + 1) (km! + sm + 1) ≡ (s + 1) (sm + 1) (mod (m − 1)!).
This formula is true for m = 3. Assume that it is true for some m − 1 ≥ 3. Then for s
such that ms
2 (m + 1) s ≡ t (m − 1) (mod (m − 1)!) (t ∈ Sm−1), the formula is also true for
m. Since that equivalence is how Sm is deﬁned, the formula is true for m.

The smallest n such that m
n has m terms in its greedy algorithm expansion is:

• m = 3: n = 1 · 3! + 0 · 3 + 1 = 7

• m = 4: n = 0 · 4! + 4 · 4 + 1 = 17

• m = 5: n = 0 · 5! + 6 · 5 + 1 = 31

• m = 6: n = 0 · 6! + 18 · 6 + 1 = 109

1.4.3 Irrational numbers

The greedy algorithm can also be used for irrational numbers (from the MathWorld entry
“Egyptian Fraction”), although then the series will be inﬁnite (because an irrational number
cannot be represented as the sum of rational numbers). For instance,

• √2 = 1 + 1
3 + 1
13 + 1
253 + 1
218201 + · · ·

• e = 2 + 1
2 + 1
5 + 1
55 + 1
9999 + 1
3620211523 + · · ·

• π = 3 + 1
8 + 1
61 + 1
5020 + 1
128541455 + · · ·

• log 2 = 1
2 + 1
6 + 1
38 + 1
6071 + · · ·

1.5 Sylvester’s sequence

Some of these ideas are from the Wikipedia entry “Sylvester’s sequence.”

1.5.1 Introduction and relation to Egyptian fractions

Sylvester’s sequence is a sequence related to the greedy algorithm for Egyptian fractions.
One way to ﬁnd it is to apply the greedy algorithm for Egyptian fractions to 1, but at each
step use the largest unit fraction that keeps the sum of the unit fractions less than 1 (change
m
n = 1
⌈ n
m ⌉ + −n (mod m)
n⌈ n
m ⌉ to m
n = 1
⌊ n
m ⌋ + 1 + −n (mod m)
n (⌊ n
m ⌋ + 1) ). The sequence is comprised

of the denominators of the resulting fractions.
1 = 1
2 + 1
3 + 1
7 + 1
43 + 1
1807 + 1
3263443 + · · · , so the ﬁrst 6 terms are 2, 3, 7, 43, 1807, 3263443.
(Sloane.)
 4

1.5.2 Formal (sequential) deﬁnition

Deﬁnition. e0 = 2, en = 1 +
 n−1∏

i=0 ei.

Corollary. e0 = 2, en = en−1 (en−1 − 1) + 1.

Proof. An exercise.

The sequence’s values grow doubly exponentially, which means that they grow at the rate

of a
bx. Speciﬁcally, en = ⌊E2n+1 + 1
2 ⌋, where E = 1
2 √6 exp [∑∞
i=1 2
−i−1 log (1 + (2ei − 1)
−2)] =

1.2640847 . . .. (Aho and Sloane 1973, Vardi 1991, Graham et al. 1994.)

Fact.
 ∞∑

i=0
 1
ei = 1. So, 1
2 + 1
3 + 1
7 + 1
43 + 1
1807 + · · · = 1.

Proof. From the recurrence equation,

en = en−1 (en−1 − 1) + 1

en+1 = en (en − 1) + 1

en+1 − 1 = en (en − 1)
1
en+1 − 1 = 1
en (en − 1)
1
en+1 − 1 = 1
en − 1 − 1
en
1
en = 1
en − 1 − 1
en+1 − 1

So,
 n−1∑

i=0
 1
ei =
 n−1∑

i=0
 ( 1
ei − 1 − 1
ei+1 − 1
 ) = 1
e0 − 1 − 1
en − 1 = 1 − 1
en − 1 →(n→∞) 1.

1.5.3 Relation to prime numbers

Theorem. (Euclid) There are inﬁnitely many prime numbers.

Proof. For two terms ei and ej (i < j), ej ≡ 1 (mod ei) since en(en−1)+1
en = (en − 1) + 1
en .
So, any two numbers in Sylvester’s sequence are relatively prime. Any prime p divides
no more than one number in Sylvester’s sequence, because if it divides more than one,
those numbers would not be relatively prime. Since there are inﬁnitely many numbers in
Sylvester’s sequence, there are also inﬁnitely many prime numbers.

Note. The second part of the ﬁrst statement assumes en and en+1. For en and en+2, repeat
the operation to get

[en (en − 1) + 1] ([en (en − 1) + 1] − 1) + 1
en = [en (en − 1) + 1] (en − 1) + 1
en

For the general case, en and en+k+1, it’s

[en+k (en+k − 1) + 1] ([en+k (en+k − 1) + 1] − 1) + 1
en = [en+k (en+k − 1) + 1] (en+k − 1)+ 1
en

5

1.5.4 Convergence of series

According to Badea (1993), given any sequence that grows such that en ≥ e2
n−1 − en−1 + 1
and ∑ 1
ei = E ∈ Q, there exists an N such that for all n > N the sequence is deﬁned by
en = e2
n−1 − en−1 + 1.

1.6 The Erdős-Straus conjecture

1.6.1 Introduction

Deﬁnition. A Diophantine equation is an equation where its solutions are restricted to
integer values.

Conjecture. (Erdős 1950) The Diophantine equation 4
n = 1
a + 1
b + 1
c can be solved for any
natural number n ≥ 2.

The greedy algorithm gives 3 or fewer terms for most cases of n. The greedy expansion
gives 4 terms when n = km! + sm + 1 (k ∈ N, m = 4, s ∈ {0, 4}), n = 25, 49, 73, . . . or
17, 41, 65, . . . ≡ 1 or 17 (mod 24).
4
n = 1
n + 1
n−2
3 + 1 + 1
n ( n−2
3 + 1) . When n = 2 (mod 3), n−2
3 + 1 ∈ N, so this expansion

is an Egyptian fraction representation of 4
n . {n : n ≡ 17 (mod 24)} ⊂ {n : n ≡ 2 (mod 3)},
so that expansion also holds for the case n = 17 (mod 24). No similar solution exists for
the case n = 1 (mod 24) (Mordell 1967).
It has been shown that given an interval [1, N ], the fraction of n in that interval that
could be counterexamples to the conjecture → 0 as N → ∞ (Webb 1970).
This conjecture has been tested valid using computer searches for n ≤ 10
14 (Swett).

1.6.2 Generalizations

Conjecture. (Sierpiński 1956) There exists some N such that the Diophantine equation
5
n = 1
a + 1
b + 1
c can be solved for any natural number n ≥ N .

—

Conjecture. (Schinzel) For any given m ∈ N, there exists some N such that the Dio-
phantine equation m
n = 1
a + 1
b + 1
c can be solved for any natural number n ≥ N (Vaughan
1970).

2 References

• Aho, A. V. and Sloane, N. J. A. "Some Doubly Exponential Sequences." Fib. Quart.
11, 429-437, 1973.

• Badea, Catalin (1993). "A theorem on irrationality of inﬁnite series and applications".
Acta Arithmetica 63: 313–323.

• Clagett, Marshall Ancient Egyptian Science, A Source Book. Volume Three: Ancient
Egyptian Mathematics (Memoirs of the American Philosophical Society) American
Philosophical Society. 1999
 6

• Erdős, Paul (1950), "Az 1/x1 + 1/x2 + ... + 1/xn = a/b egyenlet egész számú megoldá-
sairól (On a Diophantine Equation)", Mat. Lapok. 1: 192–210.

• Eves, Howard (1953), An Introduction to the History of Mathematics, Holt, Reinhard,
and Winston

• Freitag, H. T.; Phillips, G. M. (1999). "Sylvester’s algorithm and Fibonacci numbers".
Applications of Fibonacci numbers, Vol. 8 (Rochester, NY, 1998). Dordrecht: Kluwer
Acad. Publ.. pp. 155–163.

• Gardner, Milo (2002), "The Egyptian Mathematical Leather Roll, attested short term
and long term", in Gratton-Guiness, Ivor, History of the Mathematical Sciences, Hin-
dustan Book Co, pp. 119–134

• Graham, R. L.; Knuth, D. E.; and Patashnik, O. Research problem 4.65 in Concrete
Mathematics: A Foundation for Computer Science, 2nd ed. Reading, MA: Addison-
Wesley, 1994.

• Mordell, Louis J. (1967), Diophantine Equations, Academic Press, pp. 287–290.

• Sierpiński, Wacław (1956), "Sur les décompositions de nombres rationnels en fractions
primaires" (in French), Mathesis 65: 16–32.

• Sigler, Laurence E. (trans.) (2002), Fibonacci’s Liber Abaci, Springer-Verlag

• Sloane, N. J. A. Sequences A000058/M0865, A014546, and A076393 in "The On-Line
Encyclopedia of Integer Sequences."

• Anthony Spalinger , The Rhind Mathematical Papyrus as a Historical Document,
Studien zur Altägyptischen Kultur, Bd. 17 (1990), pp. 295-, Helmut Buske Verlag
GmbH

• Swett, Allan, The Erdos-Straus Conjecture, <http://math.uindy.edu/swett/esc.htm>,
retrieved 2006-09-09.

• Sylvester, J. J. (1880). "On a point in the theory of vulgar fractions". American
Journal of Mathematics 3 (4): 332–335.

• Vardi, I. "Are All Euclid Numbers Squarefree?" and "PowerMod to the Rescue." §5.1
and 5.2 in Computational Recreations in Mathematica. Reading, MA: Addison-Wesley,
pp. 82-89, 1991.

• Vaughan, R. C. (1970), "On a problem of Erdős, Straus and Schinzel", Mathematika
17 (02): 193–198.

• Webb, William A. (1970), "On 4/n = 1/x + 1/y + 1/z", Proceedings of the American
Mathematical Society 25 (3): 578–584.
 7
