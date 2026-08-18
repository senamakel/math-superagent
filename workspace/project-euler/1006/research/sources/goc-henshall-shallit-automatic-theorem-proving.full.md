<!-- source: https://arxiv.org/pdf/1203.3758 | converted from PDF -->

arXiv:1203.3758v2  [cs.FL]  29 Mar 2012
Automatic Theorem-Proving in Combinatorics
on Words

Dane Henshall and Jeﬀrey Shallit

School of Computer Science, University of Waterloo, Waterloo, ON N2L 3G1 Canada
dhenshall@uwaterloo.ca, shallit@cs.uwaterloo.ca

Abstract. We describe a technique for mechanically proving certain
kinds of theorems in combinatorics on words, using automata and a
package for manipulating them. We illustrate our technique by solving,
purely mechanically, an open problem of Currie and Saari on the lengths
of unbordered factors in the Thue-Morse sequence.

Dedicated to the memory of Sheng Yu (1950–2012): friend and colleague

1 Introduction

The title of this paper is a bit of a pun. On the one hand, we are concerned
with certain natural questions about automatic sequences: sequences over a ﬁnite
alphabet where the n’th term is expressible as a ﬁnite-state function of the base-
k representation of n. On the other hand, we are interested in answering these
questions purely mechanically, in an automated fashion.
Let x = (a(n))n≥0 be an inﬁnite sequence over a ﬁnite alphabet ∆. Then x is
said to be k-automatic if there is a deterministic ﬁnite automaton M taking as
input the base-k representation of n, and having a(n) as the output associated
with the last state encountered [3]. In this case, we say that M generates the
sequence x.
For example, in Figure 1, we give an automaton generating the well-known
Thue-Morse sequence t = t(0)t(1)t(2) · · · = 011010011001 · · · [2]. The input is
n, expressed in base 2, and the output is the number contained in the state last
reached. Thus t(n) is the sum, modulo 2, of the binary digits of n.

0

0 1

0
1

1

Fig. 1. A ﬁnite automaton generating the Thue-Morse sequence

For at least 25 years, researchers have been interested in the algorithmic
decidability of assertions about automatic sequences. For example, in one of the
earliest results, Honkala [17] showed that, given an automaton, it is decidable if
the sequence it generates is ultimately periodic.
Recently, Allouche et al. [1] found a diﬀerent proof of Honkala’s result using a
more general technique. Using this technique, they were able to give algorithmic
solutions to many classical problems from combinatorics on words such as

Given an automaton, is the generated sequence squarefree? Or overlapfree?

We write x[i] = a(i), and we let x[i..i + n − 1] denote the factor of length
n beginning at position i in x. A sequence is said to be squarefree if it contains
no factor of the form xx, where x is a nonempty word, and is said to overlapfree
if it contains no factor of the form ayaya, where a is a single letter and y is a
possibly empty word.
The technique of Allouche et al. is at its core, very similar to work of B¨uchi,
Bruy`ere, Michaux, Villemaire, and others, involving formal logic; see, e.g., [5].
The basic idea is as follows: given the automaton M , and some predicate P (n) we
want to check, we alter M by a series of transformations to a new automaton M ′

that accepts the base-k representations of those integers n for which P (n) is true.
Then we can check the assertion “∃ n P (n)” simply by checking if M ′ accepts
anything (which can be done by a standard depth-ﬁrst search on the underlying
directed graph of the automaton). We can check the assertion “∀ n P (n)” by
checking if M ′ accepts everything. And we can check assertions like “P (n) holds
for inﬁnitely many n” by checking if M ′ has a reachable cycle from which a ﬁnal
state is reachable.
Using this idea, Allouche et al. were able to show to reprove, purely mechan-
ically using a computer program, the classic theorem of Thue [24,25,4] that the
Thue-Morse sequence t is overlapfree.
More recently, the technique has been applied to give decision procedures for
other properties of automatic sequences. For example, Charlier et al. [6] showed
that it can be used to decide if a given k-automatic sequence

– contains powers of arbitrarily large exponent;
– is recurrent;
– is uniformly recurrent.

A sequence is said to be recurrent if every factor that occurs, occurs inﬁnitely
often. A sequence x is said to be uniformly recurrent if it is recurrent and fur-
thermore for each ﬁnite factor w occurring in x, there is a constant c(w) such
that two consecutive occurrences of w are separated by at most c(w) positions.
More recently, variations of the technique have been used to

– compute the critical exponent;
– compute the initial critical exponent;
– decide if a sequence is linearly recurrent;
– compute the Diophantine exponent.

(For deﬁnitions of these terms see [22].)

2 The decision procedure

In [6] we have the following theorem:

Theorem 1. If we can express a property of a k-automatic sequence x using
quantiﬁers, logical operations, integer variables, the operations of addition, sub-
traction, indexing into x, and comparison of integers or elements of x, then this
property is algorithmically decidable.

Let us outline how the decision procedure works.
First, the input to the decision procedure: an automaton M = (Q, Σk, ∆, δ, q0, τ )
generating the k-automatic sequence x. Here

– Q is a nonempty set of states;
– Σk := {0, 1, . . . , k − 1};
– ∆ is the output alphabet;
– δ : Q × Σ → Q is the transition function;
– q0 is the initial state; and
– τ : Q → ∆ is the output mapping.

In this paper, we assume that the automaton takes as input the represen-
tation of n in base k, starting with the least signiﬁcant digit; we call this the
reversed representation of n and write it as (n)k. We allow leading zeroes in the
representation (which, because of our convention, are actually trailing zeroes).
Thus, for example, 011 and 01100 are both acceptable representations for 6 in
base 2.
We might also need to encode pairs, triples, or r-tuples of integers. We handle
these by ﬁrst padding the reversed representation of the smaller integer with
trailing zeroes, and then coding the r-tuple as a word over Σr
k. For example, the
pair (20, 13) could be represented in base-2 as

[0, 1][0, 0][1, 1][0, 1][1, 0],

where the ﬁrst components spell out 00101 and the second components spell out
10110. Of course, there are other possible representations, such as

[0, 1][0, 0][1, 1][0, 1][1, 0][0, 0],

which correspond to non-canonical representations having trailing zeroes; these
are also permitted.
Rather than present a detailed proof, we illustrate the idea of the decision
procedure in the proof of the following new result:

Theorem 2. The following problem is algorithmically decidable: given two k-
automatic sequences x and y, generated by automata M1 and M2, respectively,
decide if x is a shift of y (that is, decide if there exists a constant c such that
x[n] = y[n + c] for all n ≥ 0.

Proof. We ﬁrst create an NFA M that accepts the language

{(c)k : ∃n such that x[n] ̸= y[n + c]}.

To do so, on input (c)k, M

– guesses w1 = (n)k nondeterministically (perhaps with trailing zeroes ap-
pended),
– simulates M1 on w1,
– adds n to c and computes the base-k representation of w2 = (n + c)k digit-
by-digit “on the ﬂy”, keeping track of carries, as necessary, and simulates
M2 on w2, and
– accepts if the outputs of both machine diﬀer.

We now convert M to a DFA M ′, and change ﬁnal states to non-ﬁnal (and
vice versa). Then M ′ accepts the language

{(c)k : x[n] = y[n + c] for all n ≥ 0}.

Thus, x is a shift of y if and only if M ′ accepts any word, which is easily checked
through depth-ﬁrst search. ⊓⊔

Remark 1. As we can see, the size of the automata involved depends, in an un-
pleasant way, on the number of quantiﬁers needed to state the logical expression
characterizing the property being checked, because existential quantiﬁers are im-
plemented through nondeterminism, and universal quantiﬁers are implemented
through nondeterminism and complementation (which is implemented in a DFA
by exchange of the role ﬁnal and non-ﬁnal states). Thus each new quantiﬁer
could increase the current number of states, say n, to 2n using the subset con-
struction. If the original automata have at most N states, it follows that the
running time is bounded by an expression of the form

22...2p(N )

where p is a polynomial and the number of exponents in the tower is one less
than the number of quantiﬁers in the logical formula characterizing the property
being checked.
This extraordinary computational complexity raises the natural question of
whether the decision procedure could actually be implemented for anything but
toy examples. Luckily the answer seems to be yes — at least in some cases —
as we will see below.

3 Borders

A word w is bordered if it begins and ends with the same word x with 0 <
|x| ≤ |w|/2; Otherwise it is unbordered. An example in English of a bordered

word is entanglement. A bordered word is also called biﬁx in the literature, and
unbordered words are also called biﬁx-free or primary.
Bordered and unbordered words have been actively studied in the literature,
particularly with regard to the Ehrenfeucht-Silberger problem; see, for example,
[13,18,10,11,14,15,7,16,19,12], just to name a few.
Currie and Saari [8] studied the unbordered factors of the Thue-Morse se-
quence t. They proved that if n ̸≡ 1 (mod 6), then t has an unbordered factor
of length n. (Also see [21, Lemma 4.10 and Problem 4.1].) However, this is not
a necessary condition, as

t[39..69] = 0011010010110100110010110100101,

which is an unbordered factor of length 31. Currie and Saari left it as an open
problem to give a complete characterization of the integers n for which t has an
unbordered factor of length n.
The following theorem and proof, quoted practically verbatim from [6], shows
that, more generally, the characteristic sequence of n for which a given k-
automatic sequence has an unbordered factor of length n, is itself k-automatic:

Theorem 3. Let x = a(0)a(1)a(2) · · · be a k-automatic sequence. Then the
associated inﬁnite sequence b = b(0)b(1)b(2) · · · deﬁned by

b(n) =
 {1, if x has an unbordered factor of length n;
0, otherwise;

is k-automatic.

Proof. The sequence x has an unbordered factor of length n

iﬀ
∃j ≥ 0 such that the factor of length n beginning at position j of x is unbordered
iﬀ
there exists an integer j ≥ 0 such that for all possible lengths l with 1 ≤ l ≤ n/2,
there is an integer i with 0 ≤ i < l such that the supposed border of length l
beginning and ending the factor of length n beginning at position j of x actually
diﬀers in the i’th position
iﬀ

there exists an integer j ≥ 0 such that for all integers l with 1 ≤ l ≤ n/2 there
exists an integer i with 0 ≤ i < l such that x[j + i] ̸= x[j + n − l + i].

Now assume x is a k-automatic sequence, generated by some ﬁnite automa-
ton. We show how to implement the characterization given above with an au-
tomaton.
We ﬁrst create an NFA that given the (j, l, n)k guesses the base-k represen-
tation of i, digit-by-digit, checks that i < l, computes j + i and j + n − l + i on
the ﬂy, and checks that x[j + i] ̸= x[j + n − l + i]. If such an i is found, it accepts.
We then convert this to a DFA, and interchange accepting and nonaccepting

states. This DFA M1 accepts (j, l, n)k such that there is no i, 0 ≤ i < l such
that x[j + i] = x[j + n − l + i]. We then use M1 as a subroutine to build an NFA
M2 that on input (j, n)k guesses l, checks that 1 ≤ l ≤ n/2, and calls M1 on the
result. We convert this to a DFA and interchange accepting and nonaccepting
states to get M3. Finally, this M3 is used as a subroutine to build an NFA M4
that on input n guesses j and calls M3.
The characteristic sequence of these integers n is therefore k-automatic. ⊓⊔

Since the proof is constructive, one can, in principle, carry out the con-
struction to get an explicit description of the lengths for which the Thue-Morse
sequence has an unbordered factor.
Doing so results in the following theorem:

Theorem 4. There is an unbordered factor of length n in t if and only if the
base-2 representation of n (starting with the most signiﬁcant digit) is not of the
form 1(01∗0)
∗10∗1.

Proof. The proof of this theorem is purely mechanical, and it involves performing
a sequence of operations on ﬁnite automata. The second author wrote a program
in C++, using his own automata package, to perform these operations. There
are four stages to the computation, which are described in detail below.

Stage 1

Let T be the automaton of Figure 1 generating the Thue-Morse sequence
t. Stage 1 takes T as input and outputs an automaton M1, where M1 accepts
w ∈ ({0, 1}4)
∗ if and only if w is the base-2 representation of some (n, j, l, i) ∈ S1,
where

S1 = {(n, j, l, i) : 0 < l ≤ n/2 and i < j and t[j + i] ̸= t[n + j − l + i]}. (1)

The size of M1 was only 102 states. However, since the input alphabet for
M1 is of size 24 = 16, a considerable amount of complexity is being stored in the
transition matrix. Stage 1 passed all 1.3 million tests meant to ensure that M1
corresponds to S1.

Stage 2

The purpose of Stage 2 is to remove the variable i by simulating it. The
resulting machine, after being negated, accepts (n, j, l) iﬀ the length n factor of
t starting at index j has a border of length l. So Stage 2 produces the automaton
M2, which is the negation of the result of simulating i. More formally, M2 accepts
a word w ∈ ({0, 1}3)
∗ if and only if w is the base-2 representation of some
(n, j, l) ∈ S2, where

S2 = {(n, j, l) :̸ ∃i for which (n, j, l, i) ∈ S1} (2)

The size of M2 after subset construction was 8689 states, and it minimized
down to 127 states. The output of Stage 2 passed all 1.6 million tests meant to

ensure that M2 corresponds to S2.

Stage 3

The purpose of Stage 3 is to remove l by simulating it. By the end of Stage 3,
most of the work has already been done. The output of Stage 3, M3, accepts an
input word w ∈ ({0, 1}2)
∗ if and only if w is the base-2 representation of some
(n, j) ∈ S3, where
 S3 = {(n, j) :̸ ∃l such that (n, j, l) ∈ S2} (3)

or, in other words

S3 = {(n, j) : t has an unbordered factor of length n at index j}. (4)

The size of M3 after subset construction was 1987 states, and it minimized
down to 263 states. The output of Stage 3 passed all 1.9 million tests meant to
ensure that M3 corresponds to S3.

Stage 4

Finally, Stage 4 simulates j on M3 and negates the result. So the output
of Stage 3 is an automaton that accepts the binary representation of a positive
integer n > 1 if and only if the Thue-Morse word has no unbordered factor of
length n. Formally put, the automaton M4 produced by Stage 4 accepts a word
w ∈ {0, 1}∗ if and only if w is the base-2 representation of some n ∈ S4, where

S4 = {n ∈ N : n > 1, ̸ ∃j for which (n, j) ∈ S3}. (5)

The size of M4 after subset construction is 2734 states, and it minimized to 7
states. M4 accepts the reverse of 1(01∗0)
∗10∗1. Therefore the Thue-Morse word
has an unbordered factor of length n if and only if the base-2 representation of
n (starting with the most signiﬁcant digit) is not of the form 1(01∗0)
∗10∗1.
The total computation took 9 seconds of CPU time on a 2.9GHz Dell XPS
laptop. ⊓⊔

Remark 2. Here are some additional implementation details.
In order to implement the needed operations on automata, we must decide
on an encoding of elements of (Σn
k )
∗. We could do this by performing a perfect
shuﬄe of each individual word over Σ∗
k, or by letting the alphabet itself be
represented by k-tuples. The decision represents a tradeoﬀ between state size
and alphabet size. We used the latter representation, since (a) it makes the
algorithms considerably easier to implement and understand and (b) decreases
the number of states needed.
It was mentioned earlier how many tests were passed in each stage. In order
to make sure that the ﬁnal automaton is what we expect, a number of tests are
run after each stage on the output of that stage.

For example, let x be an automatic sequence. The testing framework requires
a C++ function which given n computes x[n]. Before any operations are done,
the automaton given for x is tested against the C++ function to make sure that
they match for the ﬁrst 10,000 elements. Then, at each stage before Stage 4
the resulting automaton is tested to give conﬁdence that the operations on the
automata are giving the desired results.
For example, after Stage 2 of computing the set of lengths for which there
exists an unbordered factor of an automatic sequence x, we expect the machine
M2 to accept the language S2, where

S2 = {(n, j, l) :̸ ∃i for which x[j + i] = x[n + j − l + i]} (6)

This is then tested by making sure M2 accepts (n, j, l)k if and only if (n, j, l) ∈ S2
for all n, j, l ≤ 1400. These tests were invaluable to debugging, and provide
conﬁdence in the ﬁnal result of the computation.
Finally, we have to address the issue of multiple representations. It is easy
to forget that automata accept words in Σk∗, and not integers. For some op-
erations, such as complement and intersection, it is crucial that if one binary
representation is accepted by the automaton, then all binary representations
must be accepted.

4 Additional results

We also applied our decision procedure above to two other famous sequences:
the Rudin-Shapiro sequence [20,23] and the paperfolding sequence [9].
For a word w ∈ 1(0 + 1)
∗, we deﬁne aw(n) to be the number of (possibly
overlapping) occurrences of w in the (ordinary, unreversed) base-2 representation
of n. Thus, for example, a11(7) = 2.
The Rudin-Shapiro sequence r = r(0)r(1)r(2) · · · is then deﬁned to be r(n) =
(−1)
a11(n). It is a 2-automatic sequence generated by an automaton of four states.
The paperfolding sequence p = p(0)p(1)p(2) · · · is deﬁned as follows: writing
(n)200 as 1i0aw for some i ≥ 0 some a ∈ {0, 1}, and some w ∈ {0, 1}∗, we have
p(n) = (−1)
a. It is a 2-automatic sequence generated by an automaton of four
states.

Theorem 5. The Rudin-Shapiro sequence has an unbordered factor of every
length.

Proof. We applied the same technique discussed previously for the Thue-Morse
sequence.
Here is a summary of the computation:
Stage 1: 269 states
Stage 2: 85313 states minimized to 1974
Stage 3: 48488 states minimized to 6465
Stage 4: 6234 states.

The Stage 4 NFA has 6234 states. We were unable to determinize this automa-
ton directly (using two diﬀerent programs) due to an explosion in the number
of states created. Instead, we reversed the NFA (creating an NFA for LR) and
determinized this instead. The resulting DFA has 30 states, and upon minimiza-
tion, gives a 1-state automaton accepting all strings. ⊓⊔

Theorem 6. The paperfolding sequence has an unbordered factor of length n if
and only if the reversed representation (n)2 is rejected by the automaton given
in Figure 4.
 49
 1213
 12

0

1

1

1
 8

3

1
 1

0

0
 10

6

14

7

5

0
 1

0
 0

11
 0

0

0
15
 0,1
 0 1

1
16
 1
 0 1

11

1
 1

0
 0

0

0
 1
 0,10

Fig. 2. A ﬁnite automaton for unbordered factors in the paperfolding word

Proof. We applied the same technique discussed previously for the Thue-Morse
sequence.
Here is a summary of the computation: 6 seconds cpu time on a 2.9GHz Dell
XPS laptop.

Stage 1, 159 states
Stage 2, 1751 minimized down to 89 states
Stage 3, 178 minimized down to 75 states
Stage 4, 132 minimize down to 17 states . ⊓⊔

5 Further work

In the future, we plan to extend this work to explicitly compute the number of
distinct unbordered factors of length n in the Thue-Morse sequence. (A conjec-
ture about this number was given in [6].)

6 Open problems

Which of the problems mentioned in § 1 are algorithmically decidable for the
more general class of morphic sequences?
Can the techniques be applied to detect abelian powers in automatic se-
quences?

References

1. J.-P. Allouche, N. Rampersad, and J. Shallit. Periodicity, repetitions, and orbits
of an automatic sequence. Theoret. Comput. Sci. 410 (2009), 2795–2803.
2. J.-P. Allouche and J. O. Shallit. The ubiquitous Prouhet-Thue-Morse sequence.
In C. Ding, T. Helleseth, and H. Niederreiter, editors, Sequences and Their Appli-
cations, Proceedings of SETA ’98, pp. 1–16. Springer-Verlag, 1999.
3. J.-P. Allouche and J. Shallit. Automatic Sequences: Theory, Applications, Gener-
alizations. Cambridge University Press, 2003.
4. J. Berstel. Axel Thue’s Papers on Repetitions in Words: a Translation. Number 20
in Publications du Laboratoire de Combinatoire et d’Informatique Math´ematique.
Universit´e du Qu´ebec `a Montr´eal, February 1995.
5. V. Bruy`ere, G. Hansel, C. Michaux, and R. Villemaire. Logic and p-recognizable
sets of integers. Bull. Belgian Math. Soc. 1 (1994), 191–238. Corrigendum, Bull.
Belg. Math. Soc. 1 (1994), 577.
6. E. Charlier, N. Rampersad, and J. Shallit. Enumeration and decidable properties
of automatic sequences. In G. Mauri and A. Leporati, editors, Developments in
Language Theory, 15th International Conference, DLT 2011, Vol. 6795 of Lecture
Notes in Computer Science, pp. 165–179. Springer, 2011.
7. J. C. Costa. Biinﬁnite words with maximal recurrent unbordered factors. Theoret.
Comput. Sci. 290 (2003), 2053–2061.
8. J. D. Currie and K. Saari. Least periods of factors of inﬁnite words. RAIRO
Inform. Th´eor. App. 43 (2009), 165–178.
9. F. M. Dekking, M. Mend`es France, and A. J. van der Poorten. Folds! Math.
Intelligencer 4 (1982), 130–138, 173–181, 190–195. Erratum, 5 (1983), 5.
10. J.-P. Duval. Une caract´erisation de la p´eriode d’un mot ﬁni par la longueur de ses
facteurs primaires. C. R. Acad. Sci. Paris 290 (1980), A359–A361.
11. J.-P. Duval. Relationship between the period of a ﬁnite word and the length of its
unbordered segments. Discrete Math. 40 (1982), 31–44.
12. J.-P. Duval, T. Harju, and D. Nowotka. Unbordered factors and Lyndon words.
Discrete Math. 308 (2008), 2261–2264.
13. A. Ehrenfeucht and D. M. Silberger. Periodicity and unbordered segments of words.
Discrete Math. 26 (1979), 101–109.
14. T. Harju and D. Nowotka. Periodicity and unbordered words: a proof of the
extended duval conjecture. J. Assoc. Comput. Mach. 54 (2007), 1–20.

15. S. Holub. A proof of the extended Duval’s conjecture. Theoret. Comput. Sci. 339
(2005), 61–67.
16. S. Holub and D. Nowotka. On the relation between periodicity and unbordered
factors of ﬁnite words. Internat. J. Found. Comp. Sci. 21 (2010), 633–645.
17. J. Honkala. A decision method for the recognizability of sets deﬁned by number
systems. RAIRO Inform. Th´eor. App. 20 (1986), 395–403.
18. P. T. Nielsen. A note on biﬁx-free sequences. IEEE Trans. Inform. Theory IT-19
(1973), 704–706.
19. N. Rampersad, J. Shallit, and M.-w. Wang. Inverse star, borders, and palstars.
Inform. Process. Lett. 111 (2011), 420–422.
20. W. Rudin. Some theorems on Fourier coeﬃcients. Proc. Amer. Math. Soc. 10
(1959), 855–859.
21. K. Saari. On the Frequency and Periodicity of Inﬁnite Words. PhD thesis, Uni-
versity of Turku, Finland, 2008.
22. J. Shallit. The critical exponent is computable for automatic sequences. In
P. Ambro˘z, S. Holub, and Z. Mas´akov´a, editors, WORDS 2011, 8th International
Conference, pp. 231–239. Elect. Proc. Theor. Comput. Sci., 2011. Available at
http://arxiv.org/abs/1104.2303v2.
23. H. S. Shapiro. Extremal problems for polynomials and power series. Master’s
thesis, MIT, 1952.
24. A. Thue. ¨Uber unendliche Zeichenreihen. Norske vid. Selsk. Skr. Mat. Nat. Kl. 7
(1906), 1–22. Reprinted in Selected Mathematical Papers of Axel Thue, T. Nagell,
editor, Universitetsforlaget, Oslo, 1977, pp. 139–158.
25. A. Thue. ¨Uber die gegenseitige Lage gleicher Teile gewisser Zeichenreihen. Norske
vid. Selsk. Skr. Mat. Nat. Kl. 1 (1912), 1–67. Reprinted in Selected Mathematical
Papers of Axel Thue, T. Nagell, editor, Universitetsforlaget, Oslo, 1977, pp. 413–
478.
