<!-- source: https://cs.uwaterloo.ca/~shallit/Papers/part1.pdf | converted from PDF -->

Decision Algorithms for Fibonacci-Automatic Words, I:
Basic Results

Hamoon Mousavi1, Luke Schaeﬀer2, and Jeﬀrey Shallit
1

April 10, 2015

Abstract

We implement a decision procedure for answering questions about a class of inﬁnite
words that might be called (for lack of a better name) “Fibonacci-automatic”. This
class includes, for example, the famous Fibonacci word f = 01001010 · · · , the ﬁxed
point of the morphism 0 → 01 and 1 → 0. We then recover many results about the
Fibonacci word from the literature (and improve some of them), such as assertions
about the occurrences in f of squares, cubes, palindromes, and so forth.

1 Decidability

As is well-known, the logical theory Th(N, +), sometimes called Presburger arithmetic, is
decidable [43, 44]. B¨uchi [10] showed that if we add the function Vk(n) = ke, for some ﬁxed
integer k ≥ 2, where e = max{i : ki | n}, then the resulting theory is still decidable. This
theory is powerful enough to deﬁne ﬁnite automata; for a survey, see [9].
As a consequence, we have the following theorem (see, e.g., [50]):

Theorem 1. There is an algorithm that, given a proposition phrased using only the univer-
sal and existential quantiﬁers, indexing into one or more k-automatic sequences, addition,
subtraction, logical operations, and comparisons, will decide the truth of that proposition.

Here, by a k-automatic sequence, we mean a sequence a computed by deterministic ﬁnite
automaton with output (DFAO) M = (Q, Σk, ∆, δ, q0, κ). Here Σk := {0, 1, . . . , k − 1} is the
input alphabet, ∆ is the output alphabet, and outputs are associated with the states given
by the map κ : Q → ∆ in the following manner: if (n)k denotes the canonical expansion of
n in base k, then a[n] = κ(δ(q0, (n)k)). The prototypical example of an automatic sequence

1School of Computer Science, University of Waterloo, Waterloo, ON N2L 3G1, Canada;
sh2mousa@uwaterloo.ca, shallit@uwaterloo.ca .
2Computer Science and Artiﬁcial Intelligence Laboratory, The Stata Center, MIT Building 32, 32 Vassar
Street, Cambridge, MA 02139 USA; lrschaeffer@gmail.com .

1

is the Thue-Morse sequence t = t0t1t2 · · · , the ﬁxed point (starting with 0) of the morphism
0 → 01, 1 → 10.
It turns out that many results in the literature about properties of automatic sequences,
for which some had only long and involved proofs, can be proved purely mechanically using
a decision procedure. It suﬃces to express the property as an appropriate logical predicate,
convert the predicate into an automaton accepting representations of integers for which
the predicate is true, and examine the automaton. See, for example, the recent papers
[2, 31, 33, 32, 34]. Furthermore, in many cases we can explicitly enumerate various aspects
of such sequences, such as subword complexity [13].
Beyond base k, more exotic numeration systems are known, and one can deﬁne automata
taking representations in these systems as input. It turns out that in the so-called Pisot
numeration systems, addition is computable [29, 30], and hence a theorem analogous to
Theorem 1 holds for these systems. See, for example, [8]. It is our contention that the power
of this approach has not been widely appreciated, and that many results, previously proved
using long and involved ad hoc techniques, can be proved with much less eﬀort by phrasing
them as logical predicates and employing a decision procedure.
We have implemented a decision algorithm for one such system; namely, Fibonacci rep-
resentation. In this paper we report on our results obtained using this implementation. We
have reproved many results in the literature purely mechanically, as well as obtained new
results, using this implementation. In this paper we focus on results on the inﬁnite and ﬁnite
Fibonacci words.
The paper is organized as follows. In Section 2, we brieﬂy recall the details of Fibonacci
representation. In Section 3 we report on our mechanical proofs of properties of the inﬁnite
Fibonacci word; we reprove many old results and we prove some new ones. In Section 4 we
apply our ideas to prove results about the ﬁnite Fibonacci words. Some details about our
implementation are given in the last section.
This paper, and the two companion papers [22, 23], represent the full version of a paper
presented at the Journ´ees Montoises on September 26 2014.

2 Fibonacci representation

Let the Fibonacci numbers be deﬁned, as usual, by F0 = 0, F1 = 1, and Fn = Fn−1 +Fn−2 for
n ≥ 2. (We caution the reader that some authors use a diﬀerent indexing for these numbers.)
It is well-known, and goes back to Ostrowski [41], Lekkerkerker [39], and Zeckendorf [51],
that every non-negative integer can be represented, in an essentially unique way, as a sum
of Fibonacci numbers (Fi)i≥2, subject to the constraint that no two consecutive Fibonacci
numbers are used. For example, 43 = F9 + F6 + F2. Also see [11, 25].
Such a representation can be written as a binary string a1a2 · · · an representing the integer∑

1≤i≤n aiFn+2−i. For example, the binary string 10010001 is the Fibonacci representation
of 43.
For w = a1a2 · · · an ∈ Σ
∗
2, we deﬁne [a1a2 · · · an]F := ∑
1≤i≤n aiFn+2−i, even if a1a2 · · · an
has leading zeroes or consecutive 1’s. By (n)F we mean the canonical Fibonacci representa-

2

tion for the integer n, having no leading zeroes or consecutive 1’s. Note that (0)F = ϵ, the
empty string. The language of all canonical representations of elements of N is ϵ + 1(0 + 01)
∗.
Just as Fibonacci representation is the analogue of base-k representation, we can deﬁne
the notion of Fibonacci-automatic sequence as the analogue of the more familiar notation of k-
automatic sequence [16, 3]. We say that an inﬁnite word a = (an)n≥0 is Fibonacci-automatic
if there exists an automaton with output M = (Q, Σ2, q0, δ, κ, ∆) that an = κ(δ(q0, (n)F ))
for all n ≥ 0. An example of a Fibonacci-automatic sequence is the inﬁnite Fibonacci word,

f = f0f1f2 · · · = 01001010 · · ·

which is generated by the following 2-state automaton:

q0/0 q1/1

0
 1

0

Figure 1: Canonical Fibonacci representation DFAO generating the Fibonacci word

To compute fi, we express i in canonical Fibonacci representation, and feed it into the
automaton. Then fi is the output associated with the last state reached (denoted by the
symbol after the slash). Another characterization of Fibonacci-automatic sequences can be
found in [49].
A basic fact about Fibonacci representation is that addition can be performed by a ﬁnite
automaton. To make this precise, we need to generalize our notion of Fibonacci represen-
tation to r-tuples of integers for r ≥ 1. A representation for (x1, x2, . . . , xr) consists of a
string of symbols z over the alphabet Σ
r
2, such that the projection πi(z) over the i’th co-
ordinate gives a Fibonacci representation of xi. Notice that since the canonical Fibonacci
representations of the individual xi may have diﬀerent lengths, padding with leading zeroes
will often be necessary. A representation for (x1, x2, . . . , xr) is called canonical if it has no
leading [0, 0, . . . 0] symbols and the projections into individual coordinates have no occur-
rences of 11. We write the canonical representation as (x1, x2, . . . , xr)F . Thus, for example,
the canonical representation for (9, 16) is [0, 1][1, 0][0, 0][0, 1][0, 0][1, 0].
Thus, our claim about addition in Fibonacci representation is that there exists a determin-
istic ﬁnite automaton (DFA) Madd that takes input words of the form [0, 0, 0]
∗(x, y, z)F , and
accepts if and only if x+y = z. Thus, for example, Madd accepts [0, 0, 1][1, 0, 0][0, 1, 0][1, 0, 1],
since the three strings obtained by projection are 0101, 0010, 1001, which represent, respec-
tively, 4, 2, and 6 in Fibonacci representation. This result is apparently originally due to
Berstel [5]; also see [6, 27, 28, 1].
Since this automaton does not appear to have been given explicitly in the literature
and it is essential to our implementation, we give it here. The states of Madd are Q =
{0, 1, 2, . . . , 16}, the input alphabet is Σ2 × Σ2 × Σ2, the ﬁnal states are F = {1, 7, 11},

3

the initial state is q0 = 1, and the transition function δ is given below. The automaton
is incomplete, with any unspeciﬁed transitions going to a non-accepting dead state that
transitions to itself on all inputs. This automaton actually works even for non-canonical
expansions having consecutive 1’s; an automaton working only for canonical expansions can
easily be obtained by intersection with the appropriate regular languages. The state 0 is a
“dead state” that can safely be ignored.

[0,0,0] [0,0,1] [0,1,0] [0,1,1] [1,0,0] [1,0,1] [1,1,0] [1,1,1]
0 0 0 0 0 0 0 0 0
1 1 2 3 1 3 1 0 3
2 4 5 6 4 6 4 7 6
3 0 8 0 0 0 0 0 0
4 5 0 4 5 4 5 6 4
5 0 0 0 0 0 0 9 0
6 2 10 1 2 1 2 3 1
7 8 11 0 8 0 8 0 0
8 3 1 0 3 0 3 0 0
9 0 0 5 0 5 0 4 5
10 0 0 9 0 9 0 12 9
11 6 4 7 6 7 6 13 7
12 10 14 2 10 2 10 1 2
13 0 15 0 0 0 0 0 0
14 0 0 0 0 0 0 16 0
15 0 3 0 0 0 0 0 0
16 0 0 0 0 0 0 5 0

Table 1: Transition table for Madd for Fibonacci addition

We brieﬂy sketch a proof of the correctness of this automaton. States can be identiﬁed
with certain sequences, as follows: if x, y, z are the identical-length strings arising from
projection of a word that takes Madd from the initial state 1 to the state t, then t is identiﬁed
with the integer sequence ([x0
n]F + [y0
n]F − [z0
n]F )n≥0. With this correspondence, we can
verify the following table by a tedious induction. In the table Ln denotes the familiar Lucas
numbers, deﬁned by Ln = Fn−1 + Fn+1 for n ≥ 0 (assuming F−1 = 1). If a sequence (an)n≥0
is the sequence identiﬁed with a state t, then t is accepting iﬀ a0 = 0.

4

state sequence
1 0
2 (−Fn+2)n≥0
3 (Fn+2)n≥0
4 (−Fn+3)n≥0
5 (−Fn+4)n≥0
6 (−Fn+1)n≥0
7 (Fn)n≥0
8 (Fn+1)n≥0
9 (−Ln+2)n≥0
10 (−2Fn+2)n≥0
11 (−Fn)n≥0
12 (−2Fn+1)n≥0
13 (Ln+1)n≥0
14 (−3Fn+2)n≥0
15 (2Fn+1)n≥0
16 (−2Fn − 3Ln)n≥0

Table 2: Identiﬁcation of states with sequences

Note that the state 0 actually represents a set of sequences, not just a single sequence.
The set corresponds to those representations that are so far “out of synch” that they can
never “catch up” to have x + y = z, no matter how many digits are appended.

Remark 2. We note that, in the spirit of the paper, this adder itself can, in principle, be
checked mechanically (in Th(N, 0), of course!), as follows:
First we show the adder A is specifying a function of x and y. To do so, it suﬃces to
check that ∀x ∀y ∃z A(x, y, z)

and ∀x ∀y ∀z ∀z′ A(x, y, z) ∧ A(x, y, z′) =⇒ z = z′.

The ﬁrst predicate says that there is at least one sum of x and y and the second says that
there is at most one.
If both of these are veriﬁed, we know that A computes a function A = A(x, y).
Next, we verify associativity, which amounts to checking that

∀x ∀y ∀z A(A(x, y), z) = A(x, A(y, z)).

We can do this by checking that

∀x ∀y ∀z ∀w ∀r ∀s ∀t (A(x, y, r) ∧ A(r, z, t) ∧ A(y, z, s)) =⇒ A(x, s, t).

5

Finally, we ensure that A is an adder by induction. First, we check that ∀x A(x, 0) = x,
which amounts to ∀x ∀y A(x, 0, y) ⇐⇒ x = y.

Second, we check that if A(x, 1) = y then x < y and there does not exist z such that
x < z < y. This amounts to

∀x, y, A(x, 1, y) =⇒ ((x < y) ∧ ¬∃z (x < z) ∧ (z < y)).

This last condition shows that A(x, 1) = x+1. By associativity A(x, y+1) = A(x, A(y, 1)) =
A(A(x, y), 1) = A(x, y) + 1. By induction, A(x, y) = A(x, 0) + y = x + y, so we are done.

Another basic fact about Fibonacci representation is that, for canonical representations
containing no two consecutive 1’s or leading zeroes, the radix order on representations is the
same as the ordinary ordering on N. It follows that a very simple automaton can, on input
(x, y)F , decide whether x < y.
Putting this all together, we get the analogue of Theorem 1:

Procedure 3 (Decision procedure for Fibonacci-automatic words).
Input: m, n ∈ N, m DFAOs witnessing Fibonacci-automatic words w1, w2, . . . , wm, a ﬁrst-
order proposition with n free variables ϕ(v1, v2, . . . , vn) using constants and relations deﬁn-
able in Th(N, 0, 1, +) and indexing into w1, w2, . . . , wm.
Output: DFA with input alphabet Σn
2 accepting {(k1, k2, . . . , kn)F : ϕ(k1, k2, . . . , kn) holds}.

We remark that there was substantial skepticism that any implementation of a decision
procedure for Fibonacci-automatic words would be practical, for two reasons:

• ﬁrst, because the running time is bounded above by an expression of the form

2
2...2p(N )

where p is a polynomial, N is the number of states in the original automaton specifying
the word in question, and the number of exponents in the tower is one less than the
number of quantiﬁers in the logical formula characterizing the property being checked.

• second, because of the complexity of checking addition (15 states) compared to the
analogous automaton for base-k representation (2 states).

Nevertheless, we were able to carry out nearly all the computations described in this paper
in a matter of a few seconds on an ordinary laptop.

3 Mechanical proofs of properties of the inﬁnite Fi-
bonacci word

Recall that a word x, whether ﬁnite or inﬁnite, is said to have period p if x[i] = x[i + p] for
all i for which this equality is meaningful. Thus, for example, the English word alfalfa has

6

period 3. The exponent of a ﬁnite word x, written exp(x), is |x|/P , where P is the smallest
period of x. Thus exp(alfalfa) = 7/3.
If x is an inﬁnite word with a ﬁnite period, we say it is ultimately periodic. An inﬁnite
word x is ultimately periodic if and only if there are ﬁnite words u, v such that x = uvω,
where vω = vvv · · · .
A nonempty word of the form xx is called a square, and a nonempty word of the form
xxx is called a cube. More generally, a nonempty word of the form xn is called an n’th power.
By the order of a square xx, cube xxx, or n’th power xn, we mean the length |x|.
The inﬁnite Fibonacci word f = 01001010 · · · = f0f1f2 · · · can be described in many
diﬀerent ways. In addition to our deﬁnition in terms of automata, it is also the ﬁxed point
of the morphism ϕ(0) = 01 and ϕ(1) = 0. This word has been studied extensively in the
literature; see, for example, [4, 6].
In the next subsection, we use our implementation to prove a variety of results about
repetitions in f .

3.1 Repetitions

Theorem 4. The word f is not ultimately periodic.

Proof. We construct a predicate asserting that the integer p ≥ 1 is a period of some suﬃx
of f : (p ≥ 1) ∧ ∃n ∀i ≥ n f [i] = f [i + p].

(Note: unless otherwise indicated, whenever we refer to a variable in a predicate, the range
of the variable is assumed to be N = {0, 1, 2, . . .}.) From this predicate, using our program,
we constructed an automaton accepting the language

L = 0
∗ {(p)F : (p ≥ 1) ∧ ∃n ∀i ≥ n f [i] = f [i + p]}.

This automaton accepts the empty language, and so it follows that f is not ultimately
periodic.
Here is the log of our program:

p >= 1 with 4 states, in 60ms
i >= n with 7 states, in 5ms
F[i] = F[i + p] with 12 states, in 34ms
i >= n => F[i] = F[i + p] with 51 states, in 15ms
Ai i >= n => F[i] = F[i + p] with 3 states, in 30ms
p >= 1 & Ai i >= n => F[i] = F[i + p] with 2 states, in 0ms
En p >= 1 & Ai i >= n => F[i] = F[i + p] with 2 states, in 0ms
overall time: 144ms

The largest intermediate automaton during the computation had 63 states.
A few words of explanation are in order: here “F” refers to the sequence f , and “E” is our
abbreviation for ∃ and “A” is our abbreviation for ∀. The symbol “=>” is logical implication,
and “&” is logical and.
 7

From now on, whenever we discuss the language accepted by an automaton, we will omit
the 0∗ at the beginning.
We recall an old result of Karhum¨aki [37, Thm. 2]:

Theorem 5. f contains no fourth powers.

Proof. We create a predicate for the orders of all fourth powers occurring in f :

(n > 0) ∧ ∃i ∀t < 3n f [i + t] = f [i + n + t].

The resulting automaton accepts nothing, so there are no fourth powers.

n > 0 with 4 states, in 46ms
t < 3 * n with 30 states, in 178ms
F[i + t] = F[i + t + n] with 62 states, in 493ms
t < 3 * n => F[i + t] = F[i + t + n] with 352 states, in 39ms
At t < 3 * n => F[i + t] = F[i + t + n] with 3 states, in 132ms
Ei At t < 3 * n => F[i + t] = F[i + t + n] with 2 states, in 0ms
n > 0 & Ei At t < 3 * n => F[i + t] = F[i + t + n] with 2 states, in 0ms
overall time: 888ms

The largest intermediate automaton in the computation had 952 states.
Next, we move on to a description of the orders of squares occurring in f . An old result
of S´e´ebold [48] (also see [36, 26]) states

Theorem 6. All squares in f are of order Fn for some n ≥ 2. Furthermore, for all n ≥ 2,
there exists a square of order Fn in f .

Proof. We create a predicate for the lengths of squares:

(n > 0) ∧ ∃i ∀t < n f [i + t] = f [i + n + t].

When we run this predicate, we obtain an automaton that accepts exactly the language
10
∗. Here is the log ﬁle:

n > 0 with 4 states, in 38ms
t < n with 7 states, in 5ms
F[i + t] = F[i + t + n] with 62 states, in 582ms
t < n => F[i + t] = F[i + t + n] with 92 states, in 12ms
At t < n => F[i + t] = F[i + t + n] with 7 states, in 49ms
Ei At t < n => F[i + t] = F[i + t + n] with 3 states, in 1ms
n > 0 & Ei At t < n => F[i + t] = F[i + t + n] with 3 states, in 0ms
overall time: 687ms
 8

The largest intermediate automaton had 236 states.
We can easily get much, much more information about the square occurrences in f . The
positions of all squares in f were computed by Iliopoulos, Moore, and Smyth [36, § 2], but
their description is rather complicated and takes 5 pages to prove. Using our approach, we
created an automaton accepting the language

{(n, i)F : (n > 0) ∧ ∀t < n f [i + t] = f [i + n + t]}.

This automaton has only 6 states and eﬃciently encodes the orders and starting positions
of each square in f . During the computation, the largest intermediate automaton had 236
states. Thus we have proved

Theorem 7. The language

{(n, i)F : there is a square of order n beginning at position i in f}

is accepted by the automaton in Figure 2.

0

[0, 0] 2
[1, 0]
 5

[0, 1]
 1[0, 1]
 4

[0, 0]
[0, 0]
 3
[0, 0]
[0, 1]

[0, 0]

[0, 0] [1, 0]

Figure 2: Automaton accepting orders and positions of all squares in f

Next, we examine the cubes in f . Evidently Theorem 6 implies that any cube in f must
be of order Fn for some n. However, not every order occurs.

Theorem 8. The cubes in f are of order Fn for n ≥ 4, and a cube of each such order occurs.

Proof. We use the predicate

(n > 0) ∧ ∃i ∀t < 2n f [i + t] = f [i + n + t].

When we run our program, we obtain an automaton accepting exactly the language
(100)0
∗, which corresponds to Fn for n ≥ 4.
 9

n > 0 with 4 states, in 34ms
t < 2 * n with 16 states, in 82ms
F[i + t] = F[i + t + n] with 62 states, in 397ms
t < 2 * n => F[i + t] = F[i + t + n] with 198 states, in 17ms
At t < 2 * n => F[i + t] = F[i + t + n] with 7 states, in 87ms
Ei At t < 2 * n => F[i + t] = F[i + t + n] with 5 states, in 1ms
n > 0 & Ei At t < 2 * n => F[i + t] = F[i + t + n] with 5 states, in 0ms
overall time: 618ms

The largest intermediate automaton had 674 states.
Next, we encode the orders and positions of all cubes. We build a DFA accepting the
language {(n, i)F : (n > 0) ∧ ∀t < 2n f [i + t] = f [i + n + t]}.

Theorem 9. The language

{(n, i)F : there is a cube of order n beginning at position i in f}

is accepted by the automaton in Figure 3.

0

[0, 0]
 4[0, 1] 1

[0, 0]
 2[0, 1]
[0, 0]
3 [0, 0]
5 [0, 1][0, 0] [1, 0] [0, 0]

Figure 3: Automaton accepting orders and positions of all cubes in f

Finally, we consider all the maximal repetitions in f . Let p(x) denote the length of the
least period of x. If x = a0a1 · · · , by x[i..j] we mean aiai+1 · · · aj. Following Kolpakov and
Kucherov [38], we say that f [i..i + n − 1] is a maximal repetition if

(a) p(f [i..i + n − 1]) ≤ n/2;

(b) p(f [i..i + n − 1]) < p(f [i..i + n]);

(c) If i > 0 then p(f [i..i + n − 1]) < p(f [i − 1..i + n − 1]).

10

Theorem 10. The factor f [i..i + n − 1] is a maximal repetition of f iﬀ (n, i)F is accepted by
the automaton depicted in Figure 4.0
 5
[0, 1]

7

[1, 1] 10
 [0, 0]
 11
 [1, 0]

1

8

[0, 0] 2

4
 [1, 0]

3

[1, 0] [0, 0]

[0, 0]
12

[1, 0]
 6

[0, 1]
 [0, 0]

[1, 1] [1, 0]

[0, 0] [1, 0]

9
 [0, 0]

[1, 0]

[0, 0]
 [0, 1][1, 1]
 [1, 0]
 [0, 1]
 [0, 0]

[0, 1]

Figure 4: Automaton accepting occurrences of maximal repetitions in f

An antisquare is a nonempty word of the form xx, where x denotes the complement of x
(1’s changed to 0’s and vice versa). Its order is |x|. For a new (but small) result we prove

Theorem 11. The Fibonacci word f contains exactly four antisquare factors: 01, 10, 1001,
and 10100101.

Proof. The predicate for having an antisquare of length n is

∃i ∀k < n f [i + k] ̸= f [i + k + n].

11

When we run this we get the automaton depicted in Figure 5, specifying that the only
possible orders are 1, 2, and 4, which correspond to words of length 2, 4, and 8.

0 2[1]
1 [0]
3 [1]

[0]
 Figure 5: Automaton accepting orders of antisquares in f

Inspection of the factors of these lengths proves the result.

3.2 Palindromes and antipalindromes

We now turn to a characterization of the palindromes in f . Using the predicate

∃i ∀j < n f [i + j] = f [i + n − 1 − j],

we specify those lengths n for which there is a palindrome of length n. Our program then
recovers the following result of Chuan [15]:

Theorem 12. There exist palindromes of every length ≥ 0 in f .

We could also characterize the positions of all nonempty palindromes. The resulting
21-state automaton is not particularly enlightening, but is included here to show the kind of
complexity that can arise.
 12
 0
 19

[0, 0]

1
 3

[0, 0]
 11

[0, 1]
2
 7

[0, 0]
 [1, 0]
 [0, 0]

4
 [0, 1]

17
[0, 0]

5

18
 [0, 0]

6
 [0, 0]
 [0, 0]

8

[0, 1]
 14
[0, 0]

9

[1, 1]
 12
 [1, 0]

13
 [0, 1]
 10
 [1, 0]

[1, 1]
 [0, 0]

15

[0, 1]

[1, 0]

[0, 0]
 [0, 1]

[1, 0]
 [0, 0]
 16

[1, 1]
 [1, 0]

[0, 0]

[0, 0]
 [1, 0]

[1, 1]

[0, 0]

[1, 0][1, 1] [0, 1]
 [0, 0]
 [0, 1]

[1, 0]

[0, 0]

Figure 6: Automaton accepting orders and positions of all nonempty palindromes in f

13

Although the automaton in Figure 6 encodes all palindromes, more speciﬁc information
is a little hard to deduce from it. For example, let’s prove a result of Droubay [21]:

Theorem 13. The Fibonacci word f has exactly one palindromic factor of length n if n is
even, and exactly two palindromes of length n if n odd.

Proof. First, we obtain an expression for the lengths n for which there is exactly one palin-
dromic factor of length n.

∃i (∀t < n f [i + t] = f [i + n − 1 − t]) ∧
∀j (∀s < n f [j + s] = f [j + n − 1 − s]) =⇒ (∀u < n f [i + u] = f [j + u])

The ﬁrst part of the predicate asserts that f [i..i + n − 1] is a palindrome, and the second
part asserts that any palindrome f [j..j + n − 1] of the same length must in fact be equal to
f [i..i + n − 1].
When we run this predicate through our program we get the automaton depicted below
in Figure 7.

0
 3

[0]
 1

[1]
 2

[0]
6 [0] 7[1]

[0]
 5
[1]
 4 [0]

[0] [0]

[1]
 [0]

Figure 7: Automaton accepting lengths with exactly one palindrome

It may not be obvious, but this automaton accepts exactly the Fibonacci representations
of the even numbers. The easiest way to check this is to use our program on the predicate
∃i n = 2i and verify that the resulting automaton is isomorphic to that in Figure 7.
Next, we write down a predicate for the existence of exactly two distinct palindromes
of length n. The predicate asserts the existence of two palindromes x[i..i + n − 1] and
x[j..j + n − 1] that are distinct and for which any palindrome of the same length must be
equal to one of them.

∃i ∃j (∀t < n f [i + t] = f [i + n − 1 − t]) ∧ (∀s < n f [j + s] = f [j + n − 1 − s]) ∧
(∃m < n f [i + m] ̸= f [j + m]) ∧
(∀u(∀k < n f [u+k] = f [u+n−1−k]) =⇒ ((∀l < n f [u+l] = f [i+l]) ∨ (∀p < n f [u+p] = f [j+p])))

14

Again, running this through our program gives us an automaton accepting the Fibonacci
representations of the odd numbers. We omit the automaton.

The preﬁxes are factors of particular interest. Let us determine which preﬁxes are palin-
dromes:

Theorem 14. The preﬁx f [0..n − 1] of length n is a palindrome if and only if n = Fi − 2 for
some i ≥ 3.

Proof. We use the predicate ∀i < n f [i] = f [n − 1 − i]

obtaining an automaton accepting ϵ + 1 + 10(10)∗(0 + 01), which are precisely the represen-
tations of Fi − 2.

Next, we turn to the property of “mirror invariance”. We say an inﬁnite word w is
mirror-invariant if whenever x is a factor of w, then so is xR. We can check this for f by
creating a predicate for the assertion that for each factor x of length n, the factor xR appears
somewhere else:
 ∀i ≥ 0 ∃j such that f [i..i + n − 1] = f [j..j + n − 1]
R.

When we run this through our program we discover that it accepts the representations of all
n ≥ 0. Here is the log:

t < n with 7 states, in 99ms
F[i + t] = F[j + n - 1 - t] with 264 states, in 7944ms
t < n => F[i + t] = F[j + n - 1 - t] with 185 states, in 89ms
At t < n => F[i + t] = F[j + n - 1 - t] with 35 states, in 182ms
Ej At t < n => F[i + t] = F[j + n - 1 - t] with 5 states, in 2ms
Ai Ej At t < n => F[i + t] = F[j + n - 1 - t] with 3 states, in 6ms
overall time: 8322ms

Thus we have proved:

Theorem 15. The word f is mirror invariant.

An antipalindrome is a word x satisfying x = xR. For a new (but small) result, we
determine all possible antipalindromes in f :

Theorem 16. The only nonempty antipalindromes in f are 01, 10, (01)
2, and (10)
2.

Proof. Let us write a predicate specifying that f [i..i + n − 1] is a nonempty antipalindrome,
and further that it is a ﬁrst occurrence of such a factor:

(n > 0) ∧ (∀j < n f [i + j] ̸= f [i + n − 1 − j]) ∧ (∀i′ < i ∃j < n f [i′ + j] ̸= f [i + j]).

15

When we run this through our program, the language of (n, i)F satisfying this predicate
is accepted by the following automaton:

0 2[0, 0]
 1
 3
[0, 0]

[0, 1]

[1, 0]

[1, 1]

4
 [1, 1]
 [1, 0]

[0, 0]

Figure 8: Automaton accepting orders and positions of ﬁrst occurrences of nonempty an-
tipalindromes in f

It follows that the only (n, i) pairs accepted are (2, 0), (2, 1), (4, 3), (4, 4), corresponding,
respectively, to the strings 01, 10, (01)2, and (10)
2.

3.3 Special factors

Next we turn to special factors. It is well-known that f has exactly n + 1 distinct factors
of length n for each n ≥ 0. This implies that there is exactly one factor x of each length n
with the property that both x0 and x1 are factors. Such a factor is called right-special or
sometimes just special. We can write a predicate that expresses the assertion that the factor
f [i..i + n − 1] is the unique special factor of length n, and furthermore, that it is the ﬁrst
occurrence of that factor, as follows:

(∀i
′ < i ∃s < n f [i
′ + s] ̸= f [i + s]) ∧ ∃j ∃k ((∀t < n f [j + t] = f [i + t])
∧ (∀u < n f [k + u] = f [i + u]) ∧ (f [j + n] ̸= f [k + n])).

Theorem 17. The automaton depicted below in Figure 9 accepts the language

{(i, n)F : the factor f [i..i+n−1] is the ﬁrst occurrence of the unique special factor of length n}.

16

0
 6

[0, 1]
 1

[1, 0]
 5

[1, 1]

[0, 1]

2 [0, 0]

3

[0, 1]

[1, 0]
 4

[0, 0] [0, 0]

[1, 0] [0, 1] [0, 0][1, 0]
 Figure 9: Automaton accepting ﬁrst positions and lengths of special factors in f

Furthermore it is known (e.g., [42, Lemma 5]) that

Theorem 18. The unique special factor of length n is f [0..n − 1]
R.

Proof. We create a predicate that says that if a factor is special then it matches f [0..n − 1]
R.
When we run this we discover that all lengths are accepted.

3.4 Least periods

We now turn to least periods of factors of f ; see [45] and [24] and [19, Corollary 4].
Let P denote the assertion that n is a period of the factor f [i..j], as follows:

P (n, i, j) = f [i..j − n] = f [i + n..j]
= ∀ t with i ≤ t ≤ j − n we have f [t] = f [t + n].

Using this, we can express the predicate LP that n is the least period of f [i..j]:

LP (n, i, j) = P (n, i, j) and ∀n′ with 1 ≤ n′ < n ¬P (n
′, i, j).

Finally, we can express the predicate that n is a least period as follows

L(n) = ∃i, j ≥ 0 with 0 ≤ i + n ≤ j − 1 LP (n, i, j).

Using an implementation of this, we can reprove the following theorem of Saari [45,
Thm. 2]:
 17

Theorem 19. If a word w is a nonempty factor of the Fibonacci word, then the least period
of w is a Fibonacci number Fn for n ≥ 2. Furthermore, each such period occurs.

Proof. We ran our program on the appropriate predicate and found the resulting automaton
accepts 10+, corresponding to Fn for n ≥ 2.

Furthermore, we can actually encode information about all least periods. The automaton
depicted in Figure 10 accepts triples (n, p, i) such that p is a least period of f [i..i + n − 1].

0
 1

[0, 0, 0]

9

[0, 0, 1] [1, 0, 0]
 [1, 0, 1]
 10

[0, 0, 1]
 17

[0, 0, 0]
 18

[1, 0, 0]
 2
 5

[1, 0, 1]
 3

[0, 0, 0]
 4

8
 [0, 0, 0]

[1, 0, 0]

[0, 0, 0]

6

7
 [1, 0, 0] 12

[0, 0, 0]
 13

[1, 1, 0]

[0, 1, 0]15

[0, 0, 1]
 [0, 0, 0]
 [1, 0, 1]

[0, 0, 1]

14
 [1, 0, 0]

[0, 0, 0]
 [0, 0, 0]

[1, 0, 0]
 11

[0, 0, 1]

[1, 0, 0] [1, 1, 1]

[0, 0, 0]

[1, 1, 0]

16
 [1, 0, 1]
 [0, 0, 1]

[0, 0, 0]

[0, 0, 0]

[0, 0, 1]

[0, 1, 0]
 [0, 1, 0]
 [1, 0, 1]

[0, 0, 1]
 [0, 0, 0]

[1, 0, 0]

[0, 0, 1]
 [0, 0, 0]

Figure 10: Automaton encoding least periods of all factors in f

We also have the following result, which seems to be new.

18

Theorem 20. Let n ≥ 1, and deﬁne ℓ(n) to be the smallest integer that is the least period
of some length-n factor of f . Then ℓ(n) = Fj for j ≥ 1 if Lj − 1 ≤ n ≤ Lj+1 − 2, where Lj
is the j’th Lucas number deﬁned in Section 2.

Proof. We create an automaton accepting (n, p)F such that (a) there exists at least one
length-n factor of period p and (b) for all length-n factors x, if q is a period of x, then q ≥ p.
This automaton is depicted in Figure 11 below.

0 9[0, 1]
 1
8 [0, 0]

2
4
 [0, 0]
 3

[0, 0]

[1, 0]

5 [1, 0]

[0, 0]

6

[0, 0]
 7[1, 1]
 10

[1, 0] [1, 0]

[0, 0]

[1, 0]

[0, 0][0, 0]

[0, 1]

Figure 11: Automaton encoding smallest period over all length-n factors in f

The result now follows by inspection and the fact that (Lj − 1)F = 10(01)
(j−2)/2 if j ≥ 2
is even, and 100(10)
(j−3)/2 if j ≥ 3 is odd.

3.5 Quasiperiods

We now turn to quasiperiods. An inﬁnite word a is said to be quasiperiodic if there is some
ﬁnite nonempty word x such that a can be completely “covered” with translates of x. Here
we study the stronger version of quasiperiodicity where the ﬁrst copy of x used must be
aligned with the left edge of w and is not allowed to “hang over”; these are called aligned
covers in [14]. More precisely, for us a = a0a1a2 · · · is quasiperiodic if there exists x such
that for all i ≥ 0 there exists j ≥ 0 with i − n < j ≤ i such that ajaj+1 · · · aj+n−1 = x, where
n = |x|. Such an x is called a quasiperiod. Note that the condition j ≥ 0 implies that, in
this interpretation, any quasiperiod must actually be a preﬁx of a.
The quasiperiodicity of the Fibonacci word f was studied by Christou, Crochemore, and
Iliopoulos [14], where we can (more or less) ﬁnd the following theorem:

Theorem 21. A nonempty length-n preﬁx of f is a quasiperiod of f if and only if n is not
of the form Fn − 1 for n ≥ 3.
 19

In particular, the following preﬁx lengths are not quasiperiods: 1, 2, 4, 7, 12, and so
forth.

Proof. We write a predicate for the assertion that the length-n preﬁx is a quasiperiod:

∀i ≥ 0 ∃j with i − n < j ≤ i such that ∀t < n f [t] = f [j + t].

When we do this, we get the automaton in Figure 12 below. Inspection shows that this
DFA accepts all canonical representations, except those of the form 1(01)
∗(ϵ + 0), which are
precisely the representations of Fn − 1.

0
 1

[0] [1]
 [0]
 2

[0]
 3

[1] [0]
 4

[1]
 [0]

Figure 12: Automaton accepting lengths of preﬁxes of f that are quasiperiods

3.6 Unbordered factors

Next we look at unbordered factors. A word y is said to be a border of x if y is both a
nonempty proper preﬁx and suﬃx of x. A word x is bordered if it has at least one border. It
is easy to see that if a word y is bordered iﬀ it has a border of length ℓ with 0 < ℓ ≤ |y|/2.

Theorem 22. The only unbordered nonempty factors of f are of length Fn for n ≥ 2, and
there are two for each such length. For n ≥ 3 these two unbordered factors have the property
that one is a reverse of the other.

Proof. We can express the property of having an unbordered factor of length n as follows

∃i ∀j, 1 ≤ j ≤ n/2, ∃t < j f [i + t] ̸= f [i + n − j + t].

Here is the log:
 20

j >= 1 with 4 states, in 155ms
2 * j <= n with 16 states, in 91ms
j >= 1 & 2 * j <= n with 21 states, in 74ms
t < j with 7 states, in 17ms
F[i + t] != F[i + n - j + t] with 321 states, in 10590ms
t < j & F[i + t] != F[i + n - j + t] with 411 states, in 116ms
Et t < j & F[i + t] != F[i + n - j + t] with 85 states, in 232ms
j >= 1 & 2 * j <= n => Et t < j & F[i + t] != F[i + n - j + t] with 137 states, in 19ms
Aj j >= 1 & 2 * j <= n => Et t < j & F[i + t] != F[i + n - j + t] with 7 states, in 27ms
Ei Aj j >= 1 & 2 * j <= n => Et t < j & F[i + t] != F[i + n - j + t] with 3 states, in 0ms
overall time: 11321ms

The automaton produced accepts the Fibonacci representation of 0 and Fn for n ≥ 2.
Next, we make the assertion that there are exactly two such factors for each appropriate
length. We can do this by saying there is an unbordered factor of length n beginning at
position i, another one beginning at position k, and these factors are distinct, and for every
unbordered factor of length n, it is equal to one of these two. When we do this we discover
that the representations of all Fn for n ≥ 2 are accepted.
Finally, we make the assertion that for any two unbordered factors of length n, either
they are equal or one is the reverse of the other. When we do this we discover all lengths
except length 1 are accepted. (That is, for all lengths other than Fn, n ≥ 2, the assertion
is trivially true since there are no unbordered factors; for F2 = 1 it is false since 0 and 1
are the unbordered factors and one is not the reverse of the other; and for all larger Fi the
property holds.)

3.7 Recurrence, uniform recurrence, and linear recurrence

We now turn to various questions about recurrence. A factor x of an inﬁnite word w is
said to be recurrent if it occurs inﬁnitely often. The word w is recurrent if every factor that
occurs at least once is recurrent. A factor x is uniformly recurrent if there exists a constant
c = c(x) such that any factor w[i..i + c] is guaranteed to contain an occurrence of x. If
all factors are uniformly recurrent then w is said to be uniformly recurrent. Finally, w is
linearly recurrent if the constant c(x) is O(|x|).

Theorem 23. The word f is recurrent, uniformly recurrent, and linearly recurrent.

Proof. A predicate for all length-n factors being recurrent:

∀i ≥ 0 ∀j ≥ 0 ∃k > j ∀t < n f [i + t] = f [k + t].

This predicate says that for every factor z = f [i..i + n − 1] and every position j we can ﬁnd
another occurrence of z beginning at a position k > j. When we run this we discover that
the representations of all n ≥ 0 are accepted. So f is recurrent.
A predicate for uniform recurrence:

∀i ∃ℓ ∀j ∃s, j ≤ s ≤ j + l − n ∀p < n f [s + p] = f [i + p].

21

Once again, when we run this we discover that the representations of all n ≥ 0 are accepted.
So f is uniformly recurrent.
A predicate for linear recurrence with constant C:

∀i ∀j ∃s, j ≤ s ≤ j + Cn ∀p < n f [s + p] = f [i + p].

When we run this with C = 4, we discover that the representations of all n ≥ 0 are accepted
(but, incidentally, not for C = 3). So f is linearly recurrent.

Remark 24. We can decide the property of linear recurrence for Fibonacci-automatic words
even without knowing an explicit value for the constant C. The idea is to accept those pairs
(n, t) such that there exists a factor of length n with two consecutive occurrences separated
by distance t. Letting S denote the set of such pairs, then a sequence is linearly recurrent
iﬀ lim sup(n,t)∈S t/n < ∞, which can be decided using an argument like that in [47, Thm. 8].
However, we do not know how to compute, in general, the exact value of the lim sup for
Fibonacci representation (which we do indeed know for base-k representation), although we
can approximate it arbitrarily closely.

3.8 Lyndon words

Next, we turn to some results about Lyndon words. Recall that a nonempty word x is a
Lyndon word if it is lexicographically less than all of its nonempty proper preﬁxes.1 We
reprove some recent results of Currie and Saari [19] and Saari [46].

Theorem 25. Every Lyndon factor of f is of length Fn for some n ≥ 2, and each of these
lengths has a Lyndon factor.

Proof. Here is the predicate specifying that there is a factor of length n that is Lyndon:

∃i ∀j, 1 ≤ j < n, ∃t < n − j (∀u < t f [i + u] = f [i + j + u]) ∧ f [i + t] < f [i + j + t].

When we run this we get the representations 10
∗, which proves the result.

Theorem 26. For n ≥ 2, every length-n Lyndon factor of f is a conjugate of f [0..n − 1].

Proof. Using the predicate from the previous theorem as a base, we can create a predicate
specifying that every length-n Lyndon factor is a conjugate of f [0..n − 1]. When we do this
we discover that all lengths except 1 are accepted. (The only lengths having a Lyndon factor
are Fn for n ≥ 2, so all but F2 have the desired property.)

1There is also a version where “preﬁxes” is replaced by “suﬃxes”.

22

3.9 Critical exponents

Recall from Section 3 that exp(w) = |w|/P , where P is the smallest period of w. The critical
exponent of an inﬁnite word x is the supremum, over all factors w of x, of exp(w).
A classic result of [40] is

Theorem 27. The critical exponent of f is 2 + α, where α = (1 + √5)/2.

Although it is known that the critical exponent is computable for k-automatic sequences
[47], we do not yet know this for Fibonacci-automatic sequences (and more generally Pisot-
automatic sequences). However, with a little inspired guessing about the maximal repeti-
tions, we can complete the proof.

Proof. For each length n, the smallest possible period p of a factor is given by Theorem 20.
Hence the critical exponent is given by limj→∞(Lj+1 − 2)/Fj, which is 2 + α.

We can also ask the same sort of questions about the initial critical exponent of a word
w, which is the supremum over the exponents of all preﬁxes of w.

Theorem 28. The initial critical exponent of f is 1 + α.

Proof. We create an automaton Mice accepting the language

L = {(n, p)F : f [0..n − 1] has least period p}.

It is depicted in Figure 13 below. From the automaton, it is easy to see that the least period
of the preﬁx of length n ≥ 1 is Fj for j ≥ 2 and Fj+1 − 1 ≤ n ≤ Fj+2 − 2. Hence the initial
critical exponent is given by lim supj→∞(Fj+2 − 2)/Fj, which is 1 + α.

0
 4
[0, 0]
 6

[1, 0]1 [0, 1]

2 3
[0, 0]

[1, 0]
 [0, 0]
 7[1, 0]

5
 [1, 0]

[1, 1]

[0, 0]
 [0, 0]
 [0, 0]
Figure 13: Automaton accepting least periods of preﬁxes of length n

23

3.10 The shift orbit closure

The shift orbit closure of a sequence x is the set of all sequences t with the property that
each preﬁx of t appears as a factor of x. Note that this set can be much larger than the set
of all suﬃxes of x.
The following theorem is well known [7, Prop. 3, p. 34]:

Theorem 29. The lexicographically least sequence in the shift orbit closure of f is 0f , and
the lexicographically greatest is 1f .

Proof. We handle only the lexicographically least, leaving the lexicographically greatest to
the reader.
The idea is to create a predicate P (n) for the lexicographically least sequence b =
b0b1b2 · · · which is true iﬀ bn = 1. The following predicate encodes, ﬁrst, that bn = 1,
and second, that if one chooses any length-(n + 1) factor t of f , then b0 · · · bn is equal or
lexicographically smaller than t.

∃j f [j + n] = 1 ∧ ∀k ((∀s ≤ n f [j + s] = f [k + s]) ∨
(∃i ≤ n s.t. f [j + i] < f [k + i] ∧ (∀t < i f [j + t] = f [k + t])))

When we do this we get the following automaton, which is easily seen to generate the
sequence 0f .
 0
 3[0]
 1
[1] [0]
2 [1]

[0]
 [1]
 [0]

Figure 14: Automaton accepting lexicographically least sequence in shift orbit closure of f

3.11 Minimal forbidden words

Let x be an inﬁnite word. A ﬁnite word z = a0 · · · an is said to be minimal forbidden if z is
not a factor of x, but both a1 · · · an and a0 · · · an−1 are [18].

24

We can characterize all minimal forbidden words as follows: we create an automaton
accepting the language

{(i, n)F : f [i..i + n − 1] f [n] is not a factor of f and

f [i + 1..i + n − 1] f [n] is a factor and i is as small as possible }.

When we do so we ﬁnd the words accepted are

[1, 1]([0, 0][1, 1])
∗(ϵ + [0, 0]).

This corresponds to the words
 f [Fn − 1..2Fn − 3] f [2Fn − 2]

for n ≥ 3. The ﬁrst few are

11, 000, 10101, 00100100, 1010010100101, . . . .

3.12 Grouped factors

Cassaigne [12] introduced the notion of grouped factors. A sequence a = (ai)i≥0 has grouped
factors if, for all n ≥ 1, there exists some position m = m(n) such that a[m..m + ρ(n) + n − 2]
contains all the ρ(n) length-n blocks of a, each block occurring exactly once. One consequence
of his result is that the Fibonacci word has grouped factors.
We can write a predicate for the property of having grouped factors, as follows:

∀n ≥ 1 ∃m, s ≥ 0 ∀i ≥ 0
∃j s.t. m ≤ j ≤ m + s and a[i..i + n − 1] = a[j..j + n − 1] and
∀j′, m ≤ j′ ≤ m + s, j ̸= j′ we have a[i..i + n − 1] ̸= a[j′..j′ + n − 1].

The ﬁrst part of the predicate says that every length-n block appears somewhere in the
desired window, and the second says that it appears exactly once.
(This ﬁve-quantiﬁer deﬁnition can be viewed as a response to the question of Homer
and Selman [35], “...in what sense would a problem that required at least three alternating
quantiﬁers to describe be natural?”)
Using this predicate and our decision method, we veriﬁed that the Fibonacci word does
indeed have grouped factors.

4 Mechanical proofs of properties of the ﬁnite Fibonacci
words

Although our program is designed to answer questions about the properties of the inﬁnite
Fibonacci word f , it can also be used to solve problems concerning the ﬁnite Fibonacci words

25

(Xn), deﬁned as follows:
 Xn =
 



ϵ, if n = 0;
1, if n = 1;
0, if n = 2;
Xn−1Xn−2, if n > 2.

Note that |Xn| = Fn for n ≥ 1. (We caution the reader that there exist many variations
on this deﬁnition in the literature, particularly with regard to indexing and initial values.)
Furthermore, we have ϕ(Xn) = Xn+1 for n ≥ 1.
Our strategy for the the ﬁnite Fibonacci words has two parts:

(i) Instead of phrasing statements in terms of factors, we phrase them in terms of occur-
rences of factors (and hence in terms of the indices deﬁning a factor).

(ii) Instead of phrasing statements about ﬁnite Fibonacci words, we phrase them instead
about all length-n preﬁxes of f . Then, since Xi = f [0..Fi − 1], we can deduce results
about the ﬁnite Fibonacci words by considering the case where n is a Fibonacci number
Fi.

To illustrate this idea, consider one of the most famous properties of the Fibonacci
words, the almost-commutative property: letting η(a1a2 · · · an) = a1a2 · · · an−2anan−1 be the
map that interchanges the last two letters of a string of length at least 2, we have

Theorem 30. Xn−1Xn = η(XnXn−1) for n ≥ 2.

We can verify this, and prove even more, using our method.

Theorem 31. Let x = f [0..i − 1] and y = f [0..j − 1] for i > j > 1. Then xy = η(yx) if and
only if i = Fn, j = Fn−1 for n ≥ 3.

Proof. The idea is to check, for each i > j > 1, whether

f [0..i − 1]f [0..j − 1] = η(f [0..j − 1]f [0..i − 1]).

We can do this with the following predicate:

(i > j) ∧ (j ≥ 2) ∧ (∀t, j ≤ t < i, f [t] = f [t − j]) ∧
(∀s ≤ j − 3 f [s] = f [s + i − j]) ∧ (f [j − 2] = f [i − 1]) ∧ (f [j − 1] = f [i − 2]).

The log of our program is as follows:

i > j with 7 states, in 49ms
j >= 2 with 5 states, in 87ms
i > j & j >= 2 with 12 states, in 3ms
j <= t with 7 states, in 3ms
t < i with 7 states, in 17ms
j <= t & t < i with 19 states, in 6ms
F[t] = F[t - j] with 16 states, in 31ms
j <= t & t < i => F[t] = F[t - j] with 62 states, in 31ms
At j <= t & t < i => F[t] = F[t - j] with 14 states, in 43ms
i > j & j >= 2 & At j <= t & t < i => F[t] = F[t - j] with 12 states, in 9ms

26

s <= j - 3 with 14 states, in 72ms
F[s] = F[s + i - j] with 60 states, in 448ms
s <= j - 3 => F[s] = F[s + i - j] with 119 states, in 14ms
As s <= j - 3 => F[s] = F[s + i - j] with 17 states, in 58ms
i > j & j >= 2 & At j <= t & t < i => F[t] = F[t - j] & As s <= j - 3 => F[s] = F[s + i - j] with 6 states, in 4ms
F[j - 2] = F[i - 1] with 20 states, in 34ms
i > j & j >= 2 & At j <= t & t < i => F[t] = F[t - j] & As s <= j - 3 => F[s] = F[s + i - j] & F[j - 2] = F[i - 1] with 5 states, in 1ms
F[j - 1] = F[i - 2] with 20 states, in 29ms
i > j & j >= 2 & At j <= t & t < i => F[t] = F[t - j] & As s <= j - 3 => F[s] = F[s + i - j] & F[j - 2] = F[i - 1] & F[j - 1] = F[i - 2] with 5 states, in 1ms
overall time: 940ms

The resulting automaton accepts [1, 0][0, 1][0, 0]
+, which corresponds to i = Fn, j = Fn−1
for n ≥ 4.

An old result of S´e´ebold [48] is

Theorem 32. If uu is a square occurring in f , then u is conjugate to some ﬁnite Fibonacci
word.

Proof. Assertion conj(i, j, k, ℓ) means f [i..j] is a conjugate of f [k..ℓ] (assuming j − i = ℓ − k)

conj(i, j, k, ℓ) := ∃m f [i..i + ℓ − m] = f [m..ℓ] and f [i + ℓ − m + 1..j] = f [k..m − 1].

Predicate:

(f [i..i + n − 1] = f [i + n..i + 2n − 1]) =⇒ conj(i, i + n − 1, 0, n − 1)

This asserts that any square uu of order n appearing in f is conjugate to f [0..n − 1].
When we implement this, we discover that all lengths are accepted. This makes sense since
the only lengths corresponding to squares are Fn, and for all other lengths the base of the
implication is false.

We now reprove an old result of de Luca [20]. Recall that a primitive word is a non-power;
that is, a word that cannot be written in the form xn where n is an integer ≥ 2.

Theorem 33. All ﬁnite Fibonacci words are primitive.

Proof. The factor f [i..j] is a power if and only if there exists d, 0 < d < j − i + 1, such that
f [i..j − d] = f [i + d..j] and f [j − d + 1..j] = f [i..i + d − 1]. Letting pow(i, j) denote this
predicate, the predicate ¬ pow(0, n − 1)

expresses the claim that the length-n preﬁx f [0..n − 1] is primitive. When we implement
this, we discover that the preﬁx of every length is primitive, except those preﬁxes of length
2Fn for n ≥ 4.

A theorem of Chuan [15, Thm. 3] states that the ﬁnite Fibonacci word Xn, for n ≥ 5,
is the product of two palindromes in exactly one way: where the ﬁrst factor of length
Fn−1 − 2 and the second of length Fn−2 + 2. (Actually, Chuan claimed this was true for all
Fibonacci words, but, for example, for 010 there are evidently two diﬀerent factorizations of
the form (ϵ)(010) and (010)ϵ.) We can prove something more general using our method, by
generalizing:
 27

Theorem 34. If the length-n preﬁx f [0..n − 1] of f is the product of two (possibly empty)
palindromes, then (n)F is accepted by the automaton in Figure 15 below.

0
 6[0]

1
 3

[1]

4

[0]

2
 [1]

[0]
 [0]

[0]

5 [0]
 [1]
 7[0] [0]

[1]

8 [1]

[0]

Figure 15: Automaton accepting lengths of preﬁxes that are the product of two palindromes

Furthermore, if the length-n preﬁx f [0..n − 1] of f is the product of two (possibly empty)
palindromes in exactly one way, then (n)F is accepted by the automaton in Figure 16 below.

0 5[0]
 9

[1]
 1
 [0]2
 4
[1]
 10
[0]
 3
[1]
 6[0][0]

[0]
 [1]
 [0]
7

[0]
 8[1] [0]
 [0]
[0]

Figure 16: Automaton accepting lengths of preﬁxes that are the product of two palindromes
in exactly one way

Evidently, this includes all n of the form Fj for j ≥ 5.

Proof. For the ﬁrst, we use the predicate

∃p ≤ n ((∀t < p f [t] = f [p − 1 − t]) ∧ (∀u < n − p f [p + u] = f [n − 1 − u])) .

28

For the second, we use the predicate

∃p ≤ n ((∀t < p f [t] = f [p − 1 − t]) ∧ (∀u < n − p f [p + u] = f [n − 1 − u]))) ∧
(∀q ≤ n ((∀m < q f [m] = f [q − 1 − m]) ∧ (∀v < n − q f [q + v] = f [n − 1 − v])) =⇒ p = q).

A result of Cummings, Moore, and Karhum¨aki [17] states that the borders of the ﬁnite
Fibonacci word f [0..Fn − 1] are precisely the words f [0..Fn−2k − 1] for 2k < n. We can prove
this, and more:

Proof. Consider the pairs (n, m) such that 1 ≤ m < n and f [0..m−1] is a border of f [0..n−1].
Their Fibonacci representations are accepted by the automaton below in Figure 17.

0
 1

[0, 1]
 4

[0, 0]

2 [0, 0]
 3

[1, 0]
 7

[0, 0]

8
 [0, 1]
 [1, 1]
 [0, 0]

5

[0, 0]

[0, 1]
 6
 [1, 1]

[1, 0]
 [0, 0][0, 1]
 [0, 1][1, 1]

[1, 0]
 [0, 0]

[1, 0]

9

[0, 0]
 [1, 0]

Figure 17: Automaton encoding borders of preﬁxes of f

We use the predicate

(n > m) ∧ (m ≥ 1) ∧ ∀i < m f [i] = f [n − m + i].

By following the paths with ﬁrst coordinate of the form 10+ we recover the result of Cum-
mings, Moore, and Karhum¨aki as a special case.

29

5 Details about our implementation

Our prover, called Walnut, was written in JAVA by Hamoon Mousavi, and was developed
using the Eclipse development environment.2 We used the dk.brics.automaton package,
developed by Anders Møller at Aarhus University, for automaton minimization.
3 Maple 15
was used to compute characteristic polynomials.4 The GraphViz package was used to display
automata.
5

Our program consists of about 5000 lines of code. We used Hopcroft’s algorithm for DFA
minimization.
A user interface is provided to enter queries in a language very similar to the language
of ﬁrst-order logic. The intermediate and ﬁnal result of a query are all automata. At
every intermediate step, we chose to do minimization and determinization, if necessary.
Each automaton accepts tuples of integers in the numeration system of choice. The built-in
numeration systems are ordinary base-k representations and Fibonacci base. However, the
program can be used with any numeration system for which an automaton for addition and
ordering can be provided. These numeration system-speciﬁc automata can be declared in
text ﬁles following a simple syntax. For the automaton resulting from a query it is always
guaranteed that if a tuple t of integers is accepted, all tuples obtained from t by addition
or truncation of leading zeros are also accepted. In Fibonacci representation, we make sure
that the accepting integers do not contain consecutive 1’s.
The program was tested against hundreds of diﬀerent test cases varying in simplicity from
the most basic test cases testing only one feature at a time, to more comprehensive ones
with many alternating quantiﬁers. We also used known facts about automatic sequences and
Fibonacci word in the literature to test our program, and in all those cases we were able to
get the same result as in the literature. In a few cases, we were even able to ﬁnd small errors
in those earlier results.
The source code and manual for Walnut is available for free download at
https://www.cs.uwaterloo.ca/~shallit/papers.html .

6 Acknowledgments

We thank Narad Rampersad and Michel Rigo for useful suggestions.

References

[1] C. Ahlbach, J. Usatine, C. Frougny, and N. Pippenger. Eﬃcient algorithms for Zeck-
endorf arithmetic. Fibonacci Quart. 51 (2013), 249–256.

2Available from http://www.eclipse.org/ide/ .
3Available from http://www.brics.dk/automaton/ .
4Available from http://www.maplesoft.com .
5Available from http://www.graphviz.org .
 30

[2] J.-P. Allouche, N. Rampersad, and J. Shallit. Periodicity, repetitions, and orbits of an
automatic sequence. Theoret. Comput. Sci. 410 (2009), 2795–2803.

[3] J.-P. Allouche and J. Shallit. Automatic Sequences: Theory, Applications, Generaliza-
tions. Cambridge University Press, 2003.

[4] J. Berstel. Mots de Fibonacci. S´eminaire d’Informatique Th´eorique, LITP 6-7 (1980–
81), 57–78.

[5] J. Berstel. Fonctions rationnelles et addition. In M. Blab, editor, Th´eorie des Langages,
´Ecole de printemps d’informatique th´eorique, pp. 177–183. LITP, 1982.

[6] J. Berstel. Fibonacci words—a survey. In G. Rozenberg and A. Salomaa, editors, The
Book of L, pp. 13–27. Springer-Verlag, 1986.

[7] J.-P. Borel and F. Laubie. Quelques mots sur la droite projective r´eelle. J. Th´eorie
Nombres Bordeaux 5 (1993), 23–51.

[8] V. Bruy`ere and G. Hansel. Bertrand numeration systems and recognizability. Theoret.
Comput. Sci. 181 (1997), 17–43.

[9] V. Bruy`ere, G. Hansel, C. Michaux, and R. Villemaire. Logic and p-recognizable sets of
integers. Bull. Belgian Math. Soc. 1 (1994), 191–238. Corrigendum, Bull. Belg. Math.
Soc. 1 (1994), 577.

[10] J. R. B¨uchi. Weak secord-order arithmetic and ﬁnite automata. Zeitschrift f¨ur mathe-
matische Logik und Grundlagen der Mathematik 6 (1960), 66–92. Reprinted in S. Mac
Lane and D. Siefkes, eds., The Collected Works of J. Richard B¨uchi, Springer-Verlag,
1990, pp. 398–424.

[11] L. Carlitz. Fibonacci representations. Fibonacci Quart. 6 (1968), 193–220.

[12] J. Cassaigne. Sequences with grouped factors. In Developments in Language Theory
III, pp. 211–222. Aristotle University of Thessaloniki, 1998.

[13] E. Charlier, N. Rampersad, and J. Shallit. Enumeration and decidable properties of
automatic sequences. Internat. J. Found. Comp. Sci. 23 (2012), 1035–1066.

[14] M. Christou, M. Crochemore, and C. S. Iliopoulos. Quasiperiodicities in
Fibonacci strings. To appear in Ars Combinatoria. Preprint available at
http://arxiv.org/abs/1201.6162, 2012.

[15] W.-F. Chuan. Symmetric Fibonacci words. Fibonacci Quart. 31 (1993), 251–255.

[16] A. Cobham. Uniform tag sequences. Math. Systems Theory 6 (1972), 164–192.

[17] L. J. Cummings, D. Moore, and J. Karhum¨aki. Borders of Fibonacci strings. J. Combin.
Math. Combin. Comput. 20 (1996), 81–87.

31

[18] J. D. Currie, N. Rampersad, and K. Saari. Suﬃx conjugates for a class of morphic
subshifts. In J. Karhum¨aki, A. Lepist¨o, and L. Zamboni, editors, WORDS 2013, Vol.
8079 of Lecture Notes in Computer Science, pp. 95–106. Springer-Verlag, 2013.

[19] J. D. Currie and K. Saari. Least periods of factors of inﬁnite words. RAIRO Inform.
Th´eor. App. 43 (2009), 165–178.

[20] A. de Luca. A combinatorial property of the Fibonacci words. Inform. Process. Lett.
12 (1981), 193–195.

[21] X. Droubay. Palindromes in the Fibonacci word. Inform. Process. Lett. 55 (1995),
217–221.

[22] C. F. Du, H. Mousavi, L. Schaeﬀer, and J. Shallit. Decision algorithms for Fibonacci-
automatic words, II: Related sequences and avoidability. Submitted, 2015.

[23] C. F. Du, H. Mousavi, L. Schaeﬀer, and J. Shallit. Decision algorithms for Fibonacci-
automatic words, III: Enumeration and abelian properties. Submitted, 2015.

[24] D. D. A. Epple and J. Siefken. Collapse: a Fibonacci and Sturmian game. Available at
http://www.siefkenj.com/tmp/Fibonacci-4.pdf, 2014.

[25] A. S. Fraenkel. Systems of numeration. Amer. Math. Monthly 92 (1985), 105–114.

[26] A. S. Fraenkel and J. Simpson. The exact number of squares in Fibonacci words.
Theoret. Comput. Sci. 218 (1999), 95–106.

[27] C. Frougny. Linear numeration systems of order two. Inform. Comput. 77 (1988),
233–259.

[28] C. Frougny. Fibonacci representations and ﬁnite automata. IEEE Trans. Inform. Theory
37 (1991), 393–399.

[29] C. Frougny. Representations of numbers and ﬁnite automata. Math. Systems Theory
25 (1992), 37–60.

[30] C. Frougny and B. Solomyak. On representation of integers in linear numeration sys-
tems. In M. Pollicott and K. Schmidt, editors, Ergodic Theory of Z
d Actions (Warwick,
1993–1994), Vol. 228 of London Mathematical Society Lecture Note Series, pp. 345–368.
Cambridge University Press, 1996.

[31] D. Goc, D. Henshall, and J. Shallit. Automatic theorem-proving in combinatorics on
words. In N. Moreira and R. Reis, editors, CIAA 2012, Vol. 7381 of Lecture Notes in
Computer Science, pp. 180–191. Springer-Verlag, 2012.

[32] D. Goc, H. Mousavi, and J. Shallit. On the number of unbordered factors. In A.-H.
Dediu, C. Martin-Vide, and B. Truthe, editors, LATA 2013, Vol. 7810 of Lecture Notes
in Computer Science, pp. 299–310. Springer-Verlag, 2013.

32

[33] D. Goc, K. Saari, and J. Shallit. Primitive words and Lyndon words in automatic and
linearly recurrent sequences. In A.-H. Dediu, C. Martin-Vide, and B. Truthe, editors,
LATA 2013, Vol. 7810 of Lecture Notes in Computer Science, pp. 311–322. Springer-
Verlag, 2013.

[34] D. Goc, L. Schaeﬀer, and J. Shallit. The subword complexity of k-automatic sequences
is k-synchronized. In M.-P. B´eal and O. Carton, editors, DLT 2013, Vol. 7907 of Lecture
Notes in Computer Science, pp. 252–263. Springer-Verlag, 2013.

[35] S. Homer and A. L. Selman. Computability and Complexity Theory. Springer-Verlag,
2nd edition, 2011.

[36] C. S. Iliopoulos, D. Moore, and W. F. Smyth. A characterization of the squares in a
Fibonacci string. Theoret. Comput. Sci. 172 (1997), 281–291.

[37] J. Karhum¨aki. On cube-free ω-words generated by binary morphisms. Disc. Appl. Math.
5 (1983), 279–297.

[38] R. Kolpakov and G. Kucherov. On maximal repetitions in words. In G. Ciobanu and
G. P˘aun, editors, Fundamentals of Computation Theory: FCT ’99, Vol. 1684 of Lecture
Notes in Computer Science, pp. 374–385. Springer-Verlag, 1999.

[39] C. G. Lekkerkerker. Voorstelling van natuurlijke getallen door een som van getallen van
Fibonacci. Simon Stevin 29 (1952), 190–195.

[40] F. Mignosi and G. Pirillo. Repetitions in the Fibonacci inﬁnite word. RAIRO Inform.
Th´eor. App. 26 (1992), 199–204.

[41] A. Ostrowski. Bemerkungen zur Theorie der Diophantischen Approximationen. Abh.
Math. Sem. Hamburg 1 (1922), 77–98,250–251. Reprinted in Collected Mathematical
Papers, Vol. 3, pp. 57–80.

[42] G. Pirillo. Fibonacci numbers and words. Discrete Math. 173 (1997), 197–207.

[43] M. Presburger. ¨Uber die Volst¨andigkeit eines gewissen Systems der Arithmetik ganzer
Zahlen, in welchem die Addition als einzige Operation hervortritt. In Sparawozdanie z
I Kongresu matematyk´ow kraj´ow slowianskich, pp. 92–101, 395. Warsaw, 1929.

[44] M. Presburger. On the completeness of a certain system of arithmetic of whole numbers
in which addition occurs as the only operation. Hist. Phil. Logic 12 (1991), 225–233.

[45] K. Saari. Periods of factors of the Fibonacci word. In WORDS 07, 2007.

[46] K. Saari. Lyndon words and Fibonacci numbers. J. Combin. Theory. Ser. A 121 (2014),
34–44.

[47] L. Schaeﬀer and J. Shallit. The critical exponent is computable for automatic sequences.
Internat. J. Found. Comp. Sci. 23 (2012), 1611–1626.

33

[48] P. S´e´ebold. Propri´et´es combinatoires des mots inﬁnis engendr´es par certains morphismes
(Th`ese de 3
e cycle). PhD thesis, Universit´e P. et M. Curie, Institut de Programmation,
Paris, 1985.

[49] J. O. Shallit. A generalization of automatic sequences. Theoret. Comput. Sci. 61 (1988),
1–16.

[50] J. Shallit. Decidability and enumeration for automatic sequences: a survey. In A. A.
Bulatov and A. M. Shur, editors, CSR 2013, Vol. 7913 of Lecture Notes in Computer
Science, pp. 49–63. Springer-Verlag, 2013.

[51] E. Zeckendorf. Repr´esentation des nombres naturels par une somme de nombres de
Fibonacci ou de nombres Lucas. Bull. Soc. Roy. Li`ege 41 (1972), 179–182.

34
