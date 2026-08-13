<!-- source: https://arxiv.org/pdf/2606.23721 | pdftotext -layout of the FULL PDF -->

                                                 Holes in Valid-Extension Sets of Finite Gilbreath Sequences

                                                                                          Leila Muney


                                                                                             Abstract

                                                     Given a finite sequence of integers, form its difference triangle by repeatedly taking absolute
                                                 differences of consecutive entries. We call the sequence Gilbreath if the leftmost entry of every
                                                 row below the top is 1. The Gilbreath conjecture, which remains open, asserts that every initial
                                                 segment of the primes is a Gilbreath sequence.
                                                     This paper studies the local extension problem: given a Gilbreath sequence, which integers




arXiv:2606.23721v2 [math.CO] 16 Jul 2026
                                                 can be appended to it while preserving the Gilbreath property? We call the set of such admissible
                                                 values the valid-extension set of the sequence. A previously proposed characterization in the
                                                 literature predicts that this set always fills a natural parity interval around the last term. We
                                                 show that this fails in general: the valid-extension set can have interior holes, with the smallest
                                                 failure occurring at length 5 for the sequence (2, 3, 5, 9, 15).
                                                     The paper develops a corrected extension set theory. We give an exact criterion for member-
                                                 ship in the valid-extension set, an algorithm that computes it, and a sharp condition determining
                                                 exactly when the set fills the candidate interval. This last condition is an order-sensitive ana-
                                                 logue of the classical Brown completeness criterion for subset sums. We also establish endpoint
                                                 validity and reflection symmetry, determine the exact minimum size of the valid-extension set
                                                 together with its unique minimizer, exhibit a family whose valid-extension set has exponentially
                                                 many components, and provide enumeration data through length 11.



                                           1    Introduction

                                           Given a finite integer sequence S = (s1 , . . . , sn ), its difference triangle is defined by s0a := sa and

                                                                        sba := sb−1    b−1
                                                                                a+1 − sa        for b ≥ 1, 1 ≤ a ≤ n − b.

                                           The sequence is Gilbreath if sb1 = 1 for every 1 ≤ b ≤ n − 1. Figure 1 depicts the construction of
                                           the triangle for n = 5.
                                           The iterated absolute-difference triangle was first studied by Proth and rediscovered by Gilbreath in
                                           the context of the prime sequence. Computer experiments by Killgrove and Ralston [14] and most
                                           extensively by Odlyzko [16], the latter for primes up to 1013 (about 3.4 × 1011 primes), provide
                                           substantial numerical evidence that initial segments of the primes are Gilbreath. The assertion
                                           that this property holds for every initial segment of the primes is known as Gilbreath’s conjecture,
                                           and remains open. It is recorded as Problem A10 in Guy [13] and as Appendix Problem 68 in
                                           Montgomery [15].
                                           The features of the prime sequence responsible for the Gilbreath property have been investigated
                                           through several lenses. Croft, reported by Gardner [10], observed that the property does not seem
                                           to depend on primality in any deep sense: he conjectured that any sequence beginning with 2,


                                                                                                 1
                                            s1 s2 s3 s4 s5
                                                s11 s12 s13 s14
                                                     s21 s22 s23
                                                          s31 s32
                                                               s41


Figure 1: Difference triangle of an arbitrary sequence of length n = 5. The sequence is Gilbreath
if and only if s11 = s21 = s31 = s41 = 1.


continuing with odd numbers, and having sufficiently small gaps should be Gilbreath. This small-
gap heuristic was later formalized in probabilistic form by Chase [7], who proved that sequences
beginning 2, 3 with random small gaps are almost surely Gilbreath.
Our finite family Gn (defined below) is naturally aligned with this small-gap perspective, but the
results in this paper do not address the Gilbreath conjecture directly. Instead, we focus on a finite,
local question: given a Gilbreath sequence, which integers can be appended to it while preserving
the Gilbreath property?
For a Gilbreath sequence S, the valid extension set is

                             KS := {k ∈ Z : (s1 , . . . , sn , k) is Gilbreath}.

We call the cardinality |KS | the extension width of S. We work with the family

        Gn := {S = (s1 , . . . , sn ) : S is strictly increasing, Gilbreath, and (s1 , s2 ) = (2, 3)}.

The choice (s1 , s2 ) = (2, 3) is arbitrary: a shift argument (Section 7.1) shows that |KS | and the
structure of KS depend only on the gap sequence, so all results extend to the shifted family with
initial pair (a, a + 1) for any integer a.


1.1   Note on a previously claimed interval characterization

Gatti [11] introduces a nested-absolute-value equation

                                sn−1
                                 1   − sn−2
                                        2   − |· · · − |sn − k| · · · | = 1

characterizing membership of k in KS , and proposes to unfold this into an independently signed
sum
                           k = ±sn−1
                                  1    ± sn−2
                                          2   ± · · · ± s1n−1 + sn ± 1,
treating the n signs as freely chosen in {+1, −1}. However, the signs in this unfolding are not
independent in general; some independent sign choices produce values that do not return a Gilbreath
sequence when appended to S. Gatti [11] further claims that the set of all possible values attainable
from this formula produces a parity interval that is equal to KS . We show in Section 5 that this is
not the case: the signed formula can both miss values in the candidate interval and include values
that are not valid extensions.

                                                      2
The present paper develops a corrected extension-set theory. We give an exact algorithm for KS ,
clarify the relationship between the signed-sum set of [11], the candidate interval CS , and the
true valid-extension set KS , identify the surviving features (endpoint validity, parity, and reflection
symmetry), characterize precisely when KS = CS , and study the extremal and disconnectedness
behavior of KS .


1.2    Notation guide

For ease of reference, we collect the main notation used throughout the paper below.


Gn               Strictly increasing Gilbreath sequences of length n beginning with (2, 3).

KS               The valid-extension set: all k ∈ Z such that (S, k) is Gilbreath.

KS+              The increasing valid extensions:

                                                 KS+ = {k ∈ KS : k > sn }.

ei               The right anti-diagonal entry
                                                            ei = sin−i .

A(S)             The anti-diagonal sum:
                                                                   n−1
                                                                   X
                                                          A(S) =         ei .
                                                                   i=1

ri               The new right-edge entries created after appending a proposed extension k:

                                           r0 = |k − sn |,         ri = |ri−1 − ei |.

FS               The folding map determined by the right anti-diagonal:

                                         FS (d) = |· · · ||d − e1 | − e2 | · · · − en−1 | .

                 Thus FS (|k − sn |) = rn−1 .

CS               The candidate set:

                                 CS = {k ∈ Z : |k − sn | ≤ A(S) + 1, k ≡ sn              (mod 2)};

                 the parity-compatible interval of radius A(S) + 1 around sn .

HS               The hole set:
                                                          HS = CS \ KS .

h(S)             The defect:
                                                h(S) = |HS | = |CS | − |KS |.

S±               The signed-sum set obtained by treating the signs in the unfolded absolute-value
                 expression as independent.


                                                      3
WS               The weight multiset WS = {e1 , . . . , en−1 , 1} associated to the signed-sum relax-
                 ation.

Σ(W )            The set of subset sums of a multiset W .

DS               The valid distance set:
                                             DS = {|k − sn | : k ∈ KS }.

Pe               The reverse preimage step for x 7→ |x − e|.

Ti               The unnormalized reverse-tree sets used to compute DS .

Qa               The normalized preimage step after dividing by 2.

Tei , Li , ai    The normalized reverse-tree sets, interval lengths, and normalized anti-diagonal
                 entries used in the interval-completeness criterion.

Ln               The minimal sequence
                                                (2, 3, 5, 7, . . . , 2n − 1).

Un               The doubling sequence

                                             (2, 3, 5, 9, 17, . . . , 2n−1 + 1).

Vn               The component-doubling family from Section 13.

Mn               The maximum extension width:

                                                   Mn = max |KS |.
                                                            S∈Gn


mn               The minimum extension width:

                                                   mn = min |KS |.
                                                            S∈Gn


Nn               The number of sequences in Gn :

                                                       Nn = |Gn |.


1.3       Summary of main results

The paper has three main parts. We summarize them here and indicate where the main results are
proved.
First, we give an exact criterion for valid extensions. The right anti-diagonal of the difference
triangle determines an iterated absolute-value map FS , and a proposed extension k is valid exactly
when
                                         FS (|k − sn |) = 1
(Proposition 2). This identifies the valid distance set as a fiber of a composition of folding maps
and leads to the reverse-tree algorithm for computing KS exactly (Proposition 18). The criterion


                                                  4
immediately yields the candidate bound KS ⊆ CS (Corollary 3), and a short parity argument gives
endpoint validity and reflection symmetry of KS (Theorems 15 and 16).
Second, we compare the true extension set with the signed-sum relaxation implicit in [11]. We show
that the signed-sum set is an affine image of a subset-sum set associated to the right anti-diagonal
(Theorem 12). Thus the question of when the signed sums fill the natural candidate interval CS
is governed by Brown’s classical criterion for when subset sums fill a full interval. The equality
KS = CS is more rigid: the signs must be compatible with the ordered nested absolute-value
recurrence. Our main structural theorem gives the exact ordered analogue:
                                                    X
                       KS = CS ⇐⇒ ei ≤ 1 +              ej (1 ≤ i ≤ n − 2).
                                                      j>i

This is Theorem 20.
Third, we study the consequences of this criterion. We identify the first failure of interval-
completeness: for n ≤ 4 all sequences in Gn are interval-complete, while at n = 5 the unique
counterexample is (2, 3, 5, 9, 15), with a single hole at 15 (Theorem 24). We determine the min-
imum possible extension width, showing that it is 5 for every n ≥ 3, uniquely achieved by
Ln = (2, 3, 5, 7, . . . , 2n − 1) (Theorem 25). We also compute the extension width of the doubling
sequence Un = (2, 3, 5, 9, 17, . . . , 2n−1 + 1), obtaining |KUn | = 2n−1 + 1 (Theorem 29); exhaustive
computation through n ≤ 10 shows this value is the maximum extension width in Gn , giving rise
to Conjecture 30. We construct an explicit family Vn ∈ Gn whose valid-extension set has exactly
2n−4 connected components in the parity lattice (Theorem 35), so the maximum component count
over Gn grows exponentially in n. Finally, we give enumeration data for Nn = |Gn | through n ≤ 11
and extremal data through n ≤ 10 (Section 14).


1.4   Related work

Beyond the historical references in the introduction, the present paper relates to several active
threads in additive number theory and combinatorial dynamics.
The signed-sum relaxation arising in this paper connects the extension problem to the classical
theory of subset sums and complete sequences. Brown’s criterion gives a necessary and sufficient
condition for the subset sums of a finite sequence of nonnegative integers to fill the entire inter-
val from 0 to their total sum [4]. This is the finite completeness criterion used in Section 6 to
characterize when S± = CS . Complete sequences and related subset-sum questions also appear
in the Erdős line of additive number theory: Burr and Erdős studied Ramsey-type completeness
properties [5], and Conlon, Fox, and Pham recently resolved several problems on subset sums,
completeness, and colorings, including questions of Burr and Erdős [9]. In this terminology, the
classical completeness criterion governs when the signed sums fill the candidate interval. Our main
interval-completeness theorem identifies a strictly stronger order-sensitive condition governing when
the true valid-extension set fills the interval. The gap between these two conditions captures the
consistency required by the nested absolute-value structure.
Chase [7], mentioned in the introduction, formalizes Croft’s small-gap heuristic in probabilistic form.
Like ours, Chase’s model fixes the starting point 2, 3 and treats subsequent entries as free, but the
questions are different: Chase studies probabilistic eventual Gilbreath behavior, whereas we study
the local finite extension problem of determining exactly which next values preserve the Gilbreath


                                                  5
property. More recently, Chase, Hunter, and Tao [8] combine probabilistic and deterministic ap-
proaches to Gilbreath’s conjecture, proving a Cram’er random-model analogue and establishing a
deterministic inverse theorem that identifies the principal obstructions to the Gilbreath property
under suitable assumptions on prime gaps. Their work seeks to understand global mechanisms
governing Gilbreath’s conjecture, whereas our focus is complementary: we develop an exact struc-
tural theory of the finite valid-extension set KS , giving complete characterizations, algorithms, and
extremal results for the local extension problem.
Granville [12] also studies Gilbreath’s conjecture from a global perspective, developing a frame-
work based on sieving, reverse sieving, and equivalence classes of finite sequences to reduce the
conjecture to a collection of representative cases. While his approach likewise aims to understand
the conjecture itself, our work instead analyzes the finite extension problem for a fixed Gilbreath
sequence, characterizing the exact set of admissible next values and the combinatorial structure of
the resulting valid-extension set KS .
Bhat, Cobeli, and Zaharescu [2] study the same Proth–Gilbreath triangle as a discrete dynamical
system, introducing the operator Υ that sends the top row to the left edge and analyzing      its six-
fold “helicoidal” iteration, an associated F2 [[X]] involution T (f )(X) = f X/(1 + X) · (1 + X)−1 ,
                                                                                       

and the statistical distribution of 0’s and nonzero entries along rays parallel to an edge. Their
padding construction ([2, Prop. 3.1]) builds a triangle backwards from a prescribed southern vertex
by choosing eastern-edge values. This is reminiscent of our reverse-tree process (Section 8), but
the inverse problem is different: their construction pads the eastern edge to realize a single target
apex, whereas our reverse tree runs up the right anti-diagonal from the apex value 1 to enumerate
the entire valid-extension set KS . Equivalently, our valid distance set is the fiber over 1 of an
ordered composition of folding maps x 7→ |x − ei |, with the fold parameters supplied by the right
anti-diagonal. Earlier work in this dynamical direction includes the Proth–Gilbreath analogue of
Caragiu, Zaharescu, and Zaki [6] and the quasi-periodicity study of Bhat, Cobeli, and Zaharescu [3].
Agama [1] reformulates Gilbreath’s conjecture through a “gap sequence / path / circuit” framework.
While both Agama’s paper and ours provide a finite structural reframing, our machinery and goals
are different. Agama examines gap sequences through path combinatorics, while we examine the
combinatorial and additive structure of the extension set of a fixed finite sequence.
It is important to note that the counts Nn = |Gn | coincide (after an index shift) with OEIS
sequence [20], where a comment of T. D. Noe already identifies that the slowest- and fastest-growing
length-n Gilbreath sequences are the minimal sequence Ln = (2, 3, 5, 7, . . . , 2n−1) and the doubling
sequence (2, 3, 5, 9, 17, . . .), respectively. Our minimum extension-width theorem (Theorem 25)
and doubling-sequence extension-width formula (Theorem 29) show that these sequences are also
extremal for extension width: the minimal sequence is the unique minimizer for all n ≥ 3, and
exhaustive computation shows that the doubling sequence is the maximizer for n ≤ 10. We attribute
the growth extremizer identification to [20] and claim novelty only for the cardinality formulas of
the corresponding KS and the general structural theory.
For clarity, we explicitly state what we do and do not claim as new. We do not claim novelty
for the enumeration Nn = |Gn |, which coincides with OEIS [20], nor for the identification of the
minimal sequence and doubling sequence as the extremal-growth sequences, which is stated as a
note there. We also do not claim novelty for the classical subset-sum completeness criterion used to
analyze S± , which is due to Brown [4]. The contributions we believe to be new are the structural
theory of the valid-extension set KS : the exact membership criterion, the reverse-tree algorithm
producing KS , the interpretation of KS = CS as an ordered folding analogue of classical subset-sum

                                                  6
completeness, and the interval-completeness criterion (Theorem 20). We also identify the first hole,
prove the exact minimum extension-width theorem with uniqueness (Theorem 25), and identify the
structural properties of the exponentially disconnected family Vn (Theorem 35). The correction to
the interval-filling claim of [11] is the conceptual starting point, but the paper develops a broader
extension-set theory around it. We note that these originality claims are based on searches in the
literature and databases, and we would welcome correction.
For more context on iterated-difference and difference-triangle sequences, see the OEIS discussion
in Section 14.1.


2    The exact extension criterion

Throughout, for S ∈ Gn we define the right anti-diagonal

                                      ei := sin−i ,          1 ≤ i ≤ n − 1.

Thus e1 = s1n−1 = sn − sn−1 is the last gap, while en−1 = sn−1
                                                           1   = 1 is the bottom entry of the
triangle. We also set
                                                n−1
                                                X
                                        A(S) :=     ei .
                                                             i=1

Example 1. For S = (2, 3, 5, 9, 15), the difference triangle is

                                               2 3 5 9 15
                                                 1 2 4 6
                                                   1 2 2
                                                     1 0
                                                        1

The left diagonal below the top row is (1, 1, 1, 1), so S is Gilbreath. The right anti-diagonal is

                                        (e1 , e2 , e3 , e4 ) = (6, 2, 0, 1),

and A(S) = 9. Figure 2 highlights these two parts of the triangle.

The right anti-diagonal determines a composition of folding maps. Define

                     FS : Z≥0 → Z≥0 ,         FS (d) := |· · · ||d − e1 | − e2 | · · · − en−1 | .

Here the entries e1 , e2 , . . . , en−1 are applied in their fixed anti-diagonal order. This order is part of
the structure; unlike the signed-sum relaxation studied later, the fold parameters cannot be sorted
or chosen independently.
Given a proposed extension k, set
                                                r0 := |k − sn |
and then recursively
                                   ri := |ri−1 − ei |,         1 ≤ i ≤ n − 1.



                                                         7
                     2     3      5      9     15

                                                                 left diagonal = 1 (Gilbreath)
                           1      2      4     6
                                                                 right anti-diagonal
                                  1      2     2                 both (apex)

                                         1     0

                                               1


Figure 2: Anatomy of the difference triangle of S = (2, 3, 5, 9, 15). The left diagonal (red) consists
of 1’s, which is the defining Gilbreath condition. The right anti-diagonal (blue) is (e1 , e2 , e3 , e4 ) =
(6, 2, 0, 1). When a proposed extension k is appended, the new right-edge entries are computed by
comparing the previous new entry with these anti-diagonal entries. The bottom apex 1 belongs to
both structures, since en−1 = sn−1
                                 1  .


Thus r0 is the new entry created in row 1 after appending k, r1 is the new entry created in row 2,
and so on. Equivalently, if d = |k − sn |, then

                                               FS (d) = rn−1 .

In particular, FS (|k − sn |) is the new bottom entry of the extended triangle.
The following criterion is essentially bookkeeping: appending k only creates one new right-edge
entry in each row, and those entries are exactly the ri ’s.

Proposition 2 (Iterated absolute-value criterion). Let S ∈ Gn and k ∈ Z. Then

                                      k ∈ KS   ⇐⇒        FS (|k − sn |) = 1.

Equivalently, with r0 , . . . , rn−1 defined as above,

                                         k ∈ KS     ⇐⇒       rn−1 = 1.

Proof. Appending k to S creates one new entry on the right side of each row of the difference
triangle. The new entry in row 1 is
                                      r0 = |k − sn |.
If the new entry in row i is ri−1 , then the old rightmost entry in that row is ei , so the new entry
in the next row is
                                           |ri−1 − ei | = ri .
Therefore rn−1 = FS (|k − sn |) is exactly the new bottom entry of the extended triangle. Since all
old entries are unchanged, the extended sequence is Gilbreath if and only if this new bottom entry
is 1.

It is useful to record the corresponding fiber interpretation. If

                                         DS := {|k − sn | : k ∈ KS }


                                                         8
is the valid distance set, then Proposition 2 gives
                                    DS = {d ∈ Z≥0 : FS (d) = 1}.
Thus the extension problem is an inverse problem for a finite composition of folding maps x 7→
|x − ei |. The reverse-tree algorithm in Section 8 computes this fiber exactly.
Corollary 3 (Candidate bound). If k ∈ KS , then
                                         |k − sn | ≤ A(S) + 1.

Proof. Let
                                              d := |k − sn |.
Suppose
                                d > A(S) + 1 = e1 + · · · + en−1 + 1.
We show that no sign flip occurs while computing the ri ’s. Since r0 = d, the claim is true at the
beginning. If
                                  ri−1 = d − (e1 + · · · + ei−1 ),
then
                               ri−1 > ei + ei+1 + · · · + en−1 + 1 ≥ ei .
Hence
                          ri = |ri−1 − ei | = ri−1 − ei = d − (e1 + · · · + ei ).
By induction,
                           rn−1 = d − (e1 + · · · + en−1 ) = d − A(S) > 1.
Thus FS (d) = rn−1 ̸= 1, so k ∈
                              / KS . Taking the contrapositive gives the desired bound.


3      Parity

The right-adjusted display of the difference triangle is most naturally read along diagonals rather
than columns. For fixed a, the entries
                                         sa , s1a , s2a , . . . , sn−a
                                                                   a

form one diagonal of the triangle. The first diagonal is special: s1 = 2 is even, while the Gilbreath
condition says
                                    s11 = s21 = · · · = sn−1
                                                         1   = 1.
Thus the first diagonal has parity pattern
                                      even, odd, odd, . . . , odd.
Lemma 4. For every S = (s1 , . . . , sn ) ∈ Gn , every term sa with a ≥ 2 is odd, and every positive-
row entry sba with a ≥ 2 and b ≥ 1 is even. Equivalently, every diagonal after the first begins with
an odd entry and then consists entirely of even entries. In particular,
                                             e1 , e2 , . . . , en−2
are even, while
                                                 en−1 = 1.

                                                       9
We note that this lemma is also stated in [11]. We include a proof for completeness.

Proof. We work modulo 2. Since signs and absolute values do not matter modulo 2, the recurrence

                                            sba = sb−1    b−1
                                                   a+1 − sa

becomes
                                     sba ≡ sb−1
                                            a   + sb−1
                                                   a+1           (mod 2).
Equivalently,
                                     sb−1    b    b−1
                                      a+1 ≡ sa + sa              (mod 2).
Thus, once one diagonal
                                              sa , s1a , s2a , . . .
is known modulo 2, the next diagonal is obtained by adding adjacent entries on that diagonal.
The first diagonal is known: s1 = 2 is even, and the Gilbreath condition gives

                                      s11 = s21 = · · · = sn−1
                                                           1   = 1.

Thus the first diagonal has parity pattern

                                      even, odd, odd, . . . , odd.

For a triangle of size 5, the resulting parity pattern is

                                            E O O O                    O
                                              O E E                    E
                                                O E                    E
                                                  O                    E
                                                                       O

where E denotes even and O denotes odd.
The general case follows by the same propagation. First, the second diagonal has the desired
pattern, since
                                  s2 ≡ s1 + s11 ≡ E + O ≡ O,
while for b ≥ 1,
                                    sb2 ≡ sb+1
                                           1   + sb1 ≡ O + O ≡ E.
Now suppose some diagonal a ≥ 2 begins with an odd entry and has only even entries below it:

                          sa ≡ 1   (mod 2),          sba ≡ 0       (mod 2)       (b ≥ 1).

Then the next diagonal satisfies

                                sa+1 ≡ sa + s1a ≡ 1 + 0 ≡ 1                (mod 2),

so its top entry is odd. For every b ≥ 1,

                              sba+1 ≡ sb+1
                                       a   + sba ≡ 0 + 0 ≡ 0               (mod 2),

so all lower entries are even. By induction, every diagonal after the first has this pattern.

                                                       10
Finally, ei = sin−i . For 1 ≤ i ≤ n − 2, the entry ei lies below the top of one of the later diagonals,
so it is even. The last anti-diagonal entry is

                                            en−1 = sn−1
                                                    1   =1

by the Gilbreath condition.

Corollary 5. For every S ∈ Gn , every k ∈ KS satisfies

                                           k ≡ sn      (mod 2).

In the normalization s1 = 2, every k ∈ KS is odd.

Proof. Let k ∈ KS , and define r0 , . . . , rn−1 as in Section 2. By Proposition 2,

                                                rn−1 = 1,

which is odd.
Since
                                          rn−1 = |rn−2 − en−1 |
and en−1 = 1, the value rn−2 must be even. For all earlier steps, the entries

                                            e1 , e2 , . . . , en−2

are even by Lemma 4. Subtracting an even number and taking an absolute value does not change
parity. Therefore the parity of
                                      rn−2 , rn−3 , . . . , r0
is the same. In particular, r0 is even.
But
                                             r0 = |k − sn |.
Thus k − sn is even, so
                                           k ≡ sn      (mod 2).
Finally, sn is odd by Lemma 4, so every k ∈ KS is odd.


4     Candidate set, holes, and defect

Definition 6. The candidate set of S ∈ Gn is

                      CS := {k ∈ Z : |k − sn | ≤ A(S) + 1, k ≡ sn      (mod 2)}.

By Corollary 3 and Corollary 5, KS ⊆ CS always.
Lemma 7. |CS | = A(S) + 2.

Proof. By Lemma 4, e1 , . . . , en−2 are even and en−1 = 1, so A(S) is odd and A(S) + 1 is even. The
interval |k − sn | ≤ A(S) + 1 restricted to k ≡ sn (mod 2) contains A(S) + 2 integers.

                                                     11
Definition 8. The hole set of S is HS := CS \KS , and the defect is h(S) := |HS | = A(S)+2−|KS |.
We say S is interval-complete if h(S) = 0 (equivalently, KS = CS ).

Thus the previously claimed interval characterization is equivalent to the assertion h(S) = 0 for all
S ∈ Gn . The next sections identify exactly when this holds and the first case where it fails. But
first, we examine the signed-sum set proposed by [11].


5     The signed-sum set

It is useful to separate two different enlargements of KS . Let S ∈ Gn have right anti-diagonal
(e1 , . . . , en−1 ), and define the signed-sum set originally defined by [11] to be

                   S± := {sn + ϵ1 e1 + · · · + ϵn−1 en−1 + ϵn : ϵ1 , . . . , ϵn ∈ {±1}} .

This is the set obtained by treating all signs in the unfolded expression as independent.
Every valid extension lies in this signed-sum set. Indeed, if k ∈ KS , then the chain

                                  r0 = |k − sn |,          ri = |ri−1 − ei |

ends at rn−1 = 1. Unfolding the absolute values along this actual chain determines a consistent
choice of signs, and hence expresses k as an element of S± . Thus

                                                 KS ⊆ S± .

On the other hand, every element of S± has the correct parity and lies within distance A(S) + 1 of
sn , so
                                           S± ⊆ CS .
Therefore
                                             KS ⊆ S± ⊆ CS .

Both containments can be strict, and they fail for different reasons. The containment S± ⊆ CS
may be strict because signed sums need not realize every parity-compatible value in the interval.
The containment KS ⊆ S± may be strict because an arbitrary independent choice of signs need
not be consistent with the intermediate values in the nested absolute-value recurrence.

Example 9 (The signed sums need not fill the candidate interval). Let

                                           S = (2, 3, 5, 9, 15).

Then the right anti-diagonal is
                                      (e1 , e2 , e3 , e4 ) = (6, 2, 0, 1),
so
                                                 A(S) = 9
and
                              CS = {5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25}.



                                                      12
The signed-sum offsets from sn = 15 are

                                           ±6 ± 2 ± 0 ± 1 ± 1.

These produce
                                 {−10, −8, −6, −4, −2, 2, 4, 6, 8, 10},
but not 0. Hence
                        S± = {5, 7, 9, 11, 13, 17, 19, 21, 23, 25} = CS \ {15}.
In this example the signed-sum set coincides with the true valid-extension set:

                                                  S± = KS ,

but it does not coincide with the full candidate interval CS . Thus the interval-filling conclusion
does not follow merely from the existence of a signed-sum expression.

Example 10 (The signed sums can contain invalid extensions). Let

                                          S = (2, 3, 5, 9, 17, 19).

The right anti-diagonal is
                                   (e1 , e2 , e3 , e4 , e5 ) = (2, 6, 2, 0, 1),
so A(S) = 11, and the candidate set is

                         CS = {7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31}.

In this case the signed sums do fill the whole candidate interval:

                                                  S± = CS .

However, the true valid-extension set is smaller:

                             KS = {7, 9, 11, 13, 15, 19, 23, 25, 27, 29, 31}.

Thus
                                           S± \ KS = {17, 21}.
The values 17 and 21 arise from some independent choices of signs, but those choices are not
compatible with the nested absolute-value recurrence. Therefore the signed-sum set can contain
false positives even when it fills the entire candidate interval.

These examples show that the signed-sum set and the candidate interval play different roles. The
signed-sum set S± is an intermediate superset of the true valid-extension set KS , while the candidate
interval CS is a still coarser parity-and-size bound. The reverse-tree algorithm in Section 8 computes
KS exactly by enforcing the missing consistency conditions.




                                                       13
6    Signed sums and subset-sum completeness

The signed-sum set S± has a useful reformulation in the language of subset sums. This reformulation
explains exactly which part of the extension problem is classical and which part is new. The equality
S± = CS is a standard complete-sequence question: do the subset sums of a certain multiset fill
the entire interval from 0 to their total sum? The equality KS = CS , by contrast, is more rigid: it
asks for the same interval-filling phenomenon under the fixed order imposed by the nested absolute
values.
For a finite multiset W = {w1 , . . . , wm } of nonnegative integers, write
                                             (                            )
                                               X
                                Σ(W ) :=           wi : I ⊆ {1, . . . , m}
                                                    i∈I

for its set of subset sums, with multiplicities respected. We use the following classical criterion
of Brown [4]. Zero weights do not affect Σ(W ), so the usual positive-sequence form of Brown’s
criterion applies after deleting zeros; we state the equivalent nonnegative multiset form. Related
complete-sequence questions, including Ramsey-type versions originating with Burr and Erdős,
remain active in additive and combinatorial number theory [5, 9].

Theorem 11 (Classical completeness criterion). Let W = {w1 , . . . , wm } be a finite multiset of
nonnegative integers, listed in nondecreasing order

                                            0 ≤ w1 ≤ w2 ≤ · · · ≤ wm ,

and let T = w1 + · · · + wm . Then
                                              Σ(W ) = {0, 1, . . . , T }
if and only if                                X
                                 wj ≤ 1 +           wi      for every 1 ≤ j ≤ m.
                                              i<j

A multiset satisfying this condition will be called complete.

Proof. Suppose first that the displayed inequalities hold. We prove by induction on j that the
subset sums of {w1 , . . . , wj } fill {0, 1, . . . , w1 + · · · + wj }. The case j = 0 is trivial. If the claim
holds through j − 1, set Tj−1 = w1 + · · · + wj−1 . After adding wj , the subset sums are the union of

                          {0, 1, . . . , Tj−1 }   and     {wj , wj + 1, . . . , wj + Tj−1 }.

The inequality wj ≤ Tj−1 + 1 says exactly that these two intervals overlap or touch, so their union
is the full interval {0, 1, . . . , Tj−1 + wj }.
Conversely, suppose Σ(W ) = {0, 1, . . . , T }. If the inequality failed for some j, then
                                                        X
                                             wj > 1 +      wi .
                                                                i<j
                P
The integer 1 +P i<j wi could not be represented as a subset sum: using only weights before wj
gives at most   i<j wi , while using wj or any later weight gives at least wj . This contradicts
completeness. Hence all the inequalities hold.

                                                           14
Given S ∈ Gn with right anti-diagonal (e1 , . . . , en−1 ), define the associated weight multiset

                                         WS := {e1 , e2 , . . . , en−1 , 1}.

Let B := A(S) + 1. Since en−1 = 1, the value 1 appears in WS at least twice, and
                                          X
                                               w = B.
                                                  w∈WS

Theorem 12 (Subset-sum reformulation). Let S ∈ Gn , and write B = A(S) + 1. Then

                                      S± = {sn − B + 2t : t ∈ Σ(WS )}.

Consequently,
                                  S± = CS     ⇐⇒       Σ(WS ) = {0, 1, . . . , B}.

Proof. Write each ϵi ∈ {−1, +1} uniquely as ϵi = 2δi − 1, with δi ∈ {0, 1}. Substituting into the
definition of S± ,
                            n−1
                            X                         n−1
                                                      X
                     sn +         ϵi ei + ϵn = sn +         (2δi − 1)ei + (2δn − 1)
                            i=1                       i=1
                                                            n−1                        n−1
                                                                               !                      !
                                                            X                          X
                                            = sn + 2              δi ei + δn       −         ei + 1
                                                            i=1                        i=1
                                            = sn − B + 2t,

where t = n−1
           P
             i=1 δi ei + δn is a subset sum of WS . As the δi range independently over {0, 1}, the
value t ranges over Σ(WS ). This proves the first identity.
For the equivalence, note that

                                   CS = {sn − B + 2u : u ∈ {0, 1, . . . , B}},

since CS consists of all parity-compatible values in the interval [sn − B, sn + B]. Both S± and
CS are images under the injective affine map x 7→ sn − B + 2x, so they coincide if and only if
Σ(WS ) = {0, 1, . . . , B}.

Corollary 13. The equality S± = CS holds if and only if WS is complete in the sense of Theo-
rem 11.

Theorem 12 isolates the classical part of the problem. The signed-sum set forgets the order in
which the absolute values are evaluated: it only remembers the multiset of fold sizes. By Brown’s
criterion, the question S± = CS is answered by sorting the weights in WS and checking whether
each new sorted weight is at most one plus the sum of the preceding sorted weights.
The true valid-extension set is different. A signed expression represents a genuine element of KS
only if its signs arise from an actual chain

                                                ri = |ri−1 − ei |.



                                                         15
This chain processes the anti-diagonal entries in their fixed geometric order. Thus the interval-
completeness condition for KS has the same “no gap” shape as Brown’s criterion, but the order is
forced:                                           X
                                         ei ≤ 1 +     ej .
                                                            j>i

In short, Brown’s condition is a sorted subset-sum completeness criterion, while Theorem 20 below
is an ordered folding completeness criterion.

Proposition 14 (Hierarchy of completeness conditions). For every S ∈ Gn , if KS = CS , then WS
is complete (equivalently, S± = CS ). The converse fails.

Proof. If KS = CS , then the inclusion chain KS ⊆ S± ⊆ CS forces S± = CS . By Corollary 13, this
is equivalent to completeness of WS .
For the converse, take
                                          S = (2, 3, 5, 9, 17, 19),
as in Example 10. Its right anti-diagonal is

                                   (e1 , e2 , e3 , e4 , e5 ) = (2, 6, 2, 0, 1),

so
                                          WS = {2, 6, 2, 0, 1, 1}.
Sorted, this is (0, 1, 1, 2, 2, 6). The cumulative sums are

                                               0, 1, 2, 4, 6, 12,

and each entry is at most one plus the sum of the preceding entries. Thus WS is complete, so
S± = CS . However, the ordered criterion of Theorem 20 fails at i = 2, since

                           e2 = 6 > 1 + e3 + e4 + e5 = 1 + 2 + 0 + 1 = 4.

Therefore KS ̸= CS . Indeed, Example 10 computes S± = CS but KS = CS \ {17, 21}.

The classical completeness criterion governs when the signed sums fill the candidate interval. The
ordered interval-completeness criterion governs when the true valid-extension set fills the interval.
The gap between the two captures the consistency required by the nested absolute-value structure:
elements of S± \ KS are exactly values produced by independent sign choices that cannot occur
along any actual folding chain.


7    Endpoint validity and symmetry

Theorem 15 (Endpoint validity). For every S ∈ Gn ,

                          sn − A(S) − 1 ∈ KS          and     sn + A(S) + 1 ∈ KS .




                                                       16
Proof. Take d = A(S) + 1 = e1 + e2 + · · · + en−1 + 1. We prove by induction on i that

                       ri = ei+1 + ei+2 + · · · + en−1 + 1     (0 ≤ i ≤ n − 1),

where the empty sum (at i = n − 1) is 0. For i = 0 this is the definition of d. Assuming the formula
for ri−1 , we have                                              
                            ri−1 = ei + ei+1 + · · · + en−1 + 1 > ei ,
since the bracketed remainder is at least 1. Hence no sign flip occurs and

                        ri = |ri−1 − ei | = ri−1 − ei = ei+1 + · · · + en−1 + 1.

At i = n − 1 this gives rn−1 = 1, so both sn + (A(S) + 1) and sn − (A(S) + 1) lie in KS .

Theorem 16 (Reflection symmetry). For every S ∈ Gn and every k ∈ Z, k ∈ KS iff 2sn − k ∈ KS .
Hence KS , CS , and HS are symmetric about sn .

Proof. k ∈ KS depends on k only through |k − sn |, which is invariant under k 7→ 2sn − k.


7.1   Shift-invariance

For any integer c, the map S 7→ S + c preserves the entire difference triangle below row 0, hence
the Gilbreath property and the anti-diagonal. The correspondence k ↔ k + c gives a bijection
KS → KS+c . Consequently |KS |, |CS |, h(S), the component count, and other purely combinatorial
invariants depend only on the gap sequence and are independent of s1 . All results extend verbatim
to the shifted family with initial pair (a, a + 1) for any integer a.


8     A reverse-tree algorithm

The iterated absolute-value criterion yields a backward algorithm for computing KS . Instead of
starting with a proposed extension k and pushing the distance |k − sn | downward through the
absolute values, we start at the required final value 1 and compute all possible previous values.
In Section 2, we viewed the valid distance set as the fiber FS−1 ({1}). The reverse-tree algorithm
computes this fiber by inverting the folds one at a time.
Definition 17. For e ∈ Z≥0 and T ⊆ Z≥0 , define the preimage step

                         Pe (T ) := {e + t : t ∈ T } ∪ {e − t : t ∈ T, e ≥ t}.

This is exactly the set of nonnegative solutions x to equations of the form |x − e| = t with t ∈ T .
The branch x = e + t is always allowed, whereas the branch x = e − t is allowed only when e ≥ t.
Thus the second branch is not |e − t| in general.
Proposition 18 (Reverse-tree characterization). Let Tn−1 := {1} and recursively Ti−1 := Pei (Ti )
for i = n − 1, n − 2, . . . , 1. Then

                                  DS := {|k − sn | : k ∈ KS } = T0 ,

and KS = {sn + d : d ∈ DS } ∪ {sn − d : d ∈ DS }.

                                                  17
Proof. The condition d = |k − sn | ∈ DS is equivalent to: there exists a nonnegative chain r0 =
d, r1 , . . . , rn−1 with ri = |ri−1 − ei | and rn−1 = 1. Working backward, if ri = t then the possible
values of ri−1 ≥ 0 are ei + t (always) and ei − t (only when ei ≥ t), so the possible values form
exactly Pei ({t}). Iterating gives T0 = DS .

Example 19 (Reverse tree for S = (2, 3, 5, 9, 15)). Let S = (2, 3, 5, 9, 15). Its right anti-diagonal
is (e1 , e2 , e3 , e4 ) = (6, 2, 0, 1). We begin from the required final value T4 = {1} and move upward
through the anti-diagonal:
                         T3 = P1 ({1}) = {0, 2},             T2 = P0 ({0, 2}) = {0, 2},
since the lower branch 0 − 2 is not allowed,
                  T1 = P2 ({0, 2}) = {0, 2, 4},         T0 = P6 ({0, 2, 4}) = {2, 4, 6, 8, 10}.
Thus DS = T0 = {2, 4, 6, 8, 10}, and reflecting these distances around sn = 15 gives
                    KS = {15 ± d : d ∈ DS } = {5, 7, 9, 11, 13, 17, 19, 21, 23, 25}.
This process is visualized in the figure below.


                         2 3 5 9 15                 {5, 7, 9, 11, 13, 17, 19, 21, 23, 25}

                            1 2 4       6           {2, 4, 6, 8, 10}

                                1 2     2           {0, 2, 4}

                                   1    0           {0, 2}

                                        1           {0, 2}

                                                    1


                 Figure 3: The reverse-tree process on the sequence (2, 3, 5, 9, 15).



9    Interval-complete sequences

We now characterize exactly when KS equals the full candidate interval CS . By Corollary 13,
the weaker equality S± = CS is controlled by the classical subset-sum completeness of the sorted
multiset WS . The equality KS = CS is more rigid. It requires the independently signed expression
to be compatible with the ordered folding recurrence ri = |ri−1 − ei |, or equivalently with the
fiber condition FS (d) = 1. The criterion below is therefore an ordered folding analogue of Brown’s
completeness criterion. Figure 4 illustrates the local mechanism that underlies the criterion.
Theorem 20 (Interval-completeness criterion). Let S ∈ Gn with n ≥ 2 and right anti-diagonal
(e1 , . . . , en−1 ). Then KS = CS if and only if
                                       n−1
                                       X
                            ei ≤ 1 +           ej        for every 1 ≤ i ≤ n − 2.
                                       j=i+1


                                                         18
                   (a) a ≤ L: Qa (Te) = {0, 1, . . . , a + L} is the full interval.
                                                                     Qa (Te) = {0, . . . , a + L}
                                                                     upper: a + Te = [a, a + L]
                                    lower: a − Te = [0, a]


                    0           a              L                 a+L

                   (b) a > L: lower branch starts at a − L > 0, leaving a gap.
                                            missing: {0, . . . , a − L − 1}
                                                                               upper: a + Te = [a, a + L]
                                                                 lower: a − Te = [a − L, a]


                    0                   a−L                  a            a+L


Figure 4: The mechanism behind the interval-completeness criterion (Theorem 20). With Te =
{0, 1, . . . , L}, the preimage map Qa (Te) consists of a lower branch a − Te and an upper branch
a + Te. (a) When a ≤ L, the two branches meet at a and together cover the full integer interval
{0, 1, . . . , a + L}. (b) When a > L, the lower branch starts
                                                          P at a − L > 0 and the values {0, 1, . . . , a −
L − 1} are missing from Qa (T ). The criterion ei ≤ 1 + j>i ej ensures that case (a) occurs at every
                                e
step of the reverse tree.


Proof. For n = 2 the index range 1 ≤ i ≤ n − 2 is empty, the condition holds vacuously, and indeed
G2 = {(2, 3)} has KS = CS = {1, 3, 5}; we therefore assume n ≥ 3.
We use the reverse-tree characterization of Proposition 18. Recall Tn−1 = {1}, and Ti−1 = Pei (Ti )
for i = n − 1, . . . , 1, with DS = T0 . By Lemma 4, en−1 = 1 and e1 , . . . , en−2 are even. The first
reverse step gives
                                         Tn−2 = P1 ({1}) = {0, 2}.

From this stage onward, all elements of Ti are even, since they arise by adding or subtracting an
even ej from even values. We normalize by dividing by 2: write ai := ei /2 for 1 ≤ i ≤ n − 2, and
set
                          Ten−2 := Tn−2 /2 = {0, 1},    Tei−1 := Qai (Tei ),
where Qa (Te) := {a + u : u ∈ Te} ∪ {a − u : u ∈ Te, a ≥ u} is the normalized preimage map. Then
DS = 2Te0 .
For 0 ≤ i ≤ n − 2, define Li := 1 + n−2
                                                 P
                                                   j=i+1 aj , so Ln−2 = 1 and Li−1 = ai + Li . The full
candidate distance set (after normalization) corresponds to {0, 1, . . . , L0 }: indeed, |CS | = A(S) + 2
and the candidate distances are {0, 2, 4, . . . , A(S) + 1}, normalizing to {0, 1, . . . , (A(S) + 1)/2} =
{0, 1, . . . , L0 } since L0 = 1 + (a1 + · · · + an−2 ) = 1 + (A(S) − 1)/2 = (A(S) + 1)/2.
Therefore KS = CS is equivalent to Te0 = {0, 1, . . . , L0 }. The proof reduces to the following
elementary claim, whose content is exactly Figure 4.

Claim. Let Te ⊆ {0, 1, . . . , L} and a ≥ 0. Then Qa (Te) = {0, 1, . . . , a + L} if and only if Te =
{0, 1, . . . , L} and a ≤ L.

Proof of claim. (⇐) Suppose Te = {0, 1, . . . , L} and a ≤ L. Then {a+u : u ∈ Te} = {a, a+1, . . . , a+

                                                             19
L}, and since a ≤ L, every u ∈ Te with u ≤ a is in Te, so {a − u : u ∈ Te, a ≥ u} = {0, 1, . . . , a}. The
union is {0, 1, . . . , a + L}.
(⇒) Suppose Qa (Te) = {0, 1, . . . , a + L}. Any v > a in Qa (Te) can only arise as v = a + u for some
u ∈ Te (since a − u ≤ a). Hence for every 1 ≤ u ≤ L, the value a + u being in Qa (Te) forces u ∈ Te.
So {1, . . . , L} ⊆ Te. Also, a ∈ Qa (Te) requires 0 ∈ Te (via a + 0 or a − 0). Thus Te = {0, 1, . . . , L}.
It remains to show a ≤ L. If a = 0, this is immediate. If a > 0, then the value 0 ∈ Qa (Te) cannot
arise from the upper branch a + u, so it must arise from the lower branch a − u = 0 for some u ∈ Te.
Hence a = u ∈ Te. Since Te ⊆ {0, 1, . . . , L}, this forces a ≤ L.                                □

Boundedness. Before applying the claim we record that Tei ⊆ {0, 1, . . . , Li } for every i. This holds
at i = n − 2 since Ten−2 = {0, 1} and Ln−2 = 1; and if Tei ⊆ {0, . . . , Li }, then every element of
Qai (Tei ) has the form ai + u or ai − u with 0 ≤ u ≤ Li , hence lies in [0, ai + Li ] = [0, Li−1 ]. Thus
Tei−1 ⊆ {0, . . . , Li−1 }, completing the induction.
                                    P
Sufficiency. Suppose ei ≤ 1 + j>i ej for every 1 ≤ i ≤ n − 2. Since en−1 = 1, this rearranges to
                                                            Pn−2
ei ≤ 2 + n−2
         P
            j=i+1 ej , and dividing by 2 gives ai ≤ 1 +        j=i+1 aj = Li . By the claim (⇐) applied at
each step i = n − 2, n − 3, . . . , 1, the equality Tei−1 = {0, 1, . . . , Li−1 } propagates from Ten−2 down
to Te0 = {0, 1, . . . , L0 }. Hence DS = 2Te0 is the full parity-compatible interval, and KS = CS .
Necessity. Conversely, suppose KS = CS , equivalently Te0 = {0, 1, . . . , L0 }. Since Te0 = Qa1 (Te1 ) and,
by the boundedness established above, Te1 ⊆ {0, 1, . . . , L1 }, the claim (⇒) forces Te1 = {0, 1, . . . , L1 }
and a1 ≤ L1 . Iterating,
                     P Ti = {0, 1, . . . , Li } and ai ≤ Li for
                         e
                                                              P every 1 ≤ i ≤ n − 2. In unnormalized
form, ei ≤ 2Li = 2 + i<j≤n−2 ej , equivalently ei ≤ 1 + j>i ej (using en−1 = 1).

Remark 21 (Generality of the criterion). The proof of Theorem 20 uses the Gilbreath assumption
only through Lemma 4 (which gives en−1 = 1 and e1 , . . . , en−2 even). The criterion therefore applies
to any ordered tuple of nonnegative integers (e1 , . . . , em−1 ) with em−1 = 1 and the remaining entries
even, regardless of whether (ei ) arises as the right anti-diagonal of a Gilbreath sequence. In this
generality, with F (d) = || · · · ||d − e1 | − e2 | · · · − em−1             −1
                                                             P |, the fiber F ({1}) coincides
                                                                                         P with the full
parity-compatible interval {0, 2, . . . , A + 1}, A = i ei , if and only if ei ≤ 1 + j>i ej for every
1 ≤ i ≤ m − 2.

Corollary 22. The minimal sequence Ln = (2, 3, 5, 7, . . . , 2n − 1) is interval-complete.

Proof. Its right anti-diagonal is (2, 0, 0, . . . , 0, 1). The only nontrivial criterion is at i = 1: e1 = 2 ≤
1 + 0 + · · · + 0 + 1 = 2.

Corollary 23. The doubling sequence Un = (2, 3, 5, 9, 17, . . . , 2n−1 + 1) is interval-complete, so
|KUn | = A(Un ) + 2 = 2n−1 + 1.

Proof. For every positive row b ≥ 1, the triangle of Un has row b equal to

                                              (1, 2, 4, . . . , 2n−b−1 ).

Thus the right anti-diagonal is

                                  (e1 , . . . , en−1 ) = (2n−2 , 2n−3 , . . . , 2, 1).



                                                          20
At each i, we have ei = 2n−i−1 , while
                                  X
                             1+       ej = 1 + (2n−i−1 − 1) = 2n−i−1 .
                                              j>i

Equality holds throughout the criterion, so Un is interval-complete. Since

                                                      A(Un ) = 2n−1 − 1,

we get
                                              |KUn | = A(Un ) + 2 = 2n−1 + 1.




10       The first hole

              sn − A(S) − 1                                                                     sn + A(S) + 1
                                                       hole at k = sn = 15


                   5          7        9       11      13     15       17     19       21     23      25
                                               CS : 11 odd integers from 5 to 25


Figure 5: The first hole. For S = (2, 3, 5, 9, 15), the candidate set CS consists of all odd integers
in [sn − A(S) − 1, sn + A(S) + 1] = [5, 25]. The valid-extension set KS (blue dots) contains all of
these except the center value k = 15 (marked ×). Thus HS = {15} and h(S) = 1.

Theorem 24 (First hole). For n ≤ 4, every S ∈ Gn has KS = CS . The smallest n for which some
S ∈ Gn has KS ̸= CS is n = 5. At this length, the unique sequence S ∈ G5 with KS ̸= CS is

                                                       S = (2, 3, 5, 9, 15).

Explicitly,

          CS = {5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25},            KS = {5, 7, 9, 11, 13, 17, 19, 21, 23, 25},

so HS = {15} (Figure 5).

Proof. The case n ≤ 4. The families are

                   G2 = {(2, 3)},             G3 = {(2, 3, 5)},        G4 = {(2, 3, 5, 7), (2, 3, 5, 9)}.

Their right anti-diagonals are respectively

                                       (1),         (2, 1),     (2, 0, 1),     (4, 2, 1).

Each satisfies the criterion of Theorem 20 (vacuously for n = 2, and directly for the others), so all
four sequences are interval-complete.
The case n = 5. G5 has six sequences. These are obtained by extending the two elements of G4 :
                                   +                            +
                                  K(2,3,5,7) = {9, 11},        K(2,3,5,9) = {11, 13, 15, 17}.

                                                                21
Thus the displayed six sequences are all of G5 . We list them with their right anti-diagonals:

                                      S                        (e1 , e2 , e3 , e4 )
                                      (2, 3, 5, 7, 9)          (2, 0, 0, 1)
                                      (2, 3, 5, 7, 11)         (4, 2, 2, 1)
                                      (2, 3, 5, 9, 11)         (2, 2, 0, 1)
                                      (2, 3, 5, 9, 13)         (4, 0, 2, 1)
                                      (2, 3, 5, 9, 15)         (6, 2, 0, 1)
                                      (2, 3, 5, 9, 17)         (8, 4, 2, 1)
                                                               P
For each of these we check the criterion ei ≤ 1 + j>i ej at i = 1, 2, 3. All five sequences except
(2, 3, 5, 9, 15) satisfy the criterion at every i and are therefore interval-complete by Theorem 20. For
(2, 3, 5, 9, 15), the criterion fails at i = 1: e1 = 6 > 1 + 2 + 0 + 1 = 4. The corresponding extension
sets are
                           S                KS                                      |KS |
                           (2, 3, 5, 7, 9) {5, 7, 9, 11, 13}                          5
                           (2, 3, 5, 7, 11) {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21} 11
                           (2, 3, 5, 9, 11) {5, 7, 9, 11, 13, 15, 17}                 7
                           (2, 3, 5, 9, 13) {5, 7, 9, 11, 13, 15, 17, 19, 21}         9
                           (2, 3, 5, 9, 15) {5, 7, 9, 11, 13, 17, 19, 21, 23, 25}    10
                           (2, 3, 5, 9, 17) {1, 3, 5, . . . , 33}                    17
and only (2, 3, 5, 9, 15) has |KS | ̸= A(S) + 2.
Identifying the hole. The right anti-diagonal of S = (2, 3, 5, 9, 15) is (6, 2, 0, 1) (Example 1). Ap-
plying the reverse tree of Proposition 18:

                     T4 = {1}, T3 = P1 ({1}) = {0, 2}, T2 = P0 ({0, 2}) = {0, 2},

                   T1 = P2 ({0, 2}) = {0, 2, 4}, T0 = P6 ({0, 2, 4}) = {2, 4, 6, 8, 10}.
The value 0 would be in T0 only via 6 − 6, but 6 ∈
                                                 / T1 ; hence 0 ∈
                                                                / T0 . Therefore DS = {2, 4, 6, 8, 10},
giving KS = {15 ± d : d ∈ DS } = CS \ {15}, so HS = {15}.


11     Minimum extension width

Theorem 25 (Minimum extension width). For every n ≥ 3,

                                               min |KS | = 5,
                                              S∈Gn

and the minimum is uniquely achieved by the minimal sequence Ln = (2, 3, 5, 7, . . . , 2n − 1).

We separate the proof into three lemmas.

Lemma 26. For every S ∈ Gn , |DS | ≥ 3.

Proof. The reverse tree starts with Tn−1 = {1}, and the first step gives Tn−2 = P1 ({1}) = {0, 2}.
Each preimage step Pe (T ) contains the translated set {e + t : t ∈ T } with the same cardinality as
T , so the cardinality of Ti is non-decreasing as i decreases.

                                                         22
By Lemma 4, e1 = sn − sn−1 is a positive even integer, so e1 ≥ 2.
Case 1. If e2 = · · · = en−2 = 0, then each step P0 ({0, 2}) = {0, 2} leaves the set unchanged, so
T1 = {0, 2}. The final step is Pe1 ({0, 2}). Since e1 ≥ 2, both e1 − 0 = e1 and e1 − 2 are nonnegative,
giving T0 = {e1 − 2, e1 , e1 + 2}, three distinct values.
Case 2. If some ej with 2 ≤ j ≤ n − 2 is positive, take the largest such j. Then ej+1 = · · · = en−2 =
0, so Tj = {0, 2}. Since ej is a positive even integer (Lemma 4), ej ≥ 2, and Tj−1 = Pej ({0, 2}) =
{ej − 2, ej , ej + 2} has 3 distinct elements. By cardinality non-decrease, |T0 | ≥ 3.
In both cases |DS | = |T0 | ≥ 3.

Lemma 27. If |KS | = 5, then (e1 , e2 , . . . , en−1 ) = (2, 0, 0, . . . , 0, 1).

Proof. By Theorem 16, |KS | = 2|DS | if 0 ∈
                                          / DS and |KS | = 2|DS | − 1 if 0 ∈ DS . So |KS | = 5
requires |DS | = 3 and 0 ∈ DS .
For 0 ∈ DS = Pe1 (T1 ), we need e1 − t = 0 for some t ∈ T1 , i.e., e1 ∈ T1 . Since e1 ≥ 2, this means
T1 contains an element ≥ 2.
If |T1 | ≥ 3, then Pe1 (T1 ) contains the three distinct positive elements {e1 + t : t ∈ T1 }, plus the
element 0 from the lower branch, giving |DS | ≥ 4 and contradicting |DS | = 3. Hence |T1 | = 2.
The sequence Tn−2 = {0, 2}, Tn−3 , . . . , T1 has non-decreasing cardinality, so all these sets have
cardinality 2. Each middle ej is even (Lemma 4), so either ej = 0, in which case Pej ({0, 2}) = {0, 2},
or ej ≥ 2, in which case Pej ({0, 2}) = {ej − 2, ej , ej + 2} has three distinct elements. Preservation
of cardinality 2 therefore forces ej = 0 for each 2 ≤ j ≤ n − 2, and T1 = {0, 2}.
Since e1 ∈ T1 = {0, 2} and e1 ≥ 2, e1 = 2. Combined with en−1 = 1, we get (e1 , . . . , en−1 ) =
(2, 0, . . . , 0, 1).

Lemma 28. If S ∈ Gn has (e1 , e2 , . . . , en−1 ) = (2, 0, 0, . . . , 0, 1), then S = Ln .

Proof. Write gj := sj+1 − sj for the gaps of S. Since (s1 , s2 ) = (2, 3), we have g1 = 1. Also
gn−1 = sn − sn−1 = e1 = 2.
We prove by descending induction that

                                          gj = 2       (2 ≤ j ≤ n − 1).

The base case j = n − 1 was just proved. Now suppose 2 ≤ j ≤ n − 2 and assume inductively that

                                         gj+1 = gj+2 = · · · = gn−1 = 2.

Then the row-1 entries strictly to the right of position j are all 2. Hence, by induction on the row
index, every entry sba with a ≥ j + 1, b ≥ 2, and a + b ≤ n is zero: in row 2 these are absolute
differences of equal row-1 entries, and in higher rows they are absolute differences of zeros.
Now use the anti-diagonal hypothesis at index i = n − j. Since ei = sin−i , we have

                                                en−j = sn−j
                                                        j   = 0.




                                                         23
We propagate this zero upward to row 2. For each m = 2, 3, . . . , n − j − 1, the entry sm
                                                                                         j+1 is zero
by the preceding paragraph, and the recurrence gives

                                sm+1
                                 j   = |sm      m           m      m
                                         j+1 − sj | = |0 − sj | = sj .

If n − j = 2, this already says s2j = 0. Otherwise, applying the identity successively for

                                  m = n − j − 1, n − j − 2, . . . , 2,

gives
                                      sn−j
                                       j   = sn−j−1
                                              j     = · · · = s2j .

Since sn−j
       j   = 0, it follows in all cases that s2j = 0. But

                              s2j = |s1j+1 − s1j | = |gj+1 − gj | = |2 − gj |.

Therefore gj = 2, completing the descending induction.
Thus g1 = 1 and g2 = · · · = gn−1 = 2, so

                                  S = (2, 3, 5, 7, . . . , 2n − 1) = Ln .




Proof of Theorem 25. By Lemma 26, |DS | ≥ 3, so |KS | ≥ 2 · 3 − 1 = 5. Equality requires 0 ∈ DS
and |DS | = 3, which by Lemma 27 forces the anti-diagonal (2, 0, . . . , 0, 1), which by Lemma 28
forces S = Ln . Conversely, Ln has this anti-diagonal, and the reverse tree gives DLn = {0, 2, 4},
hence |KLn | = 5.


12      The doubling sequence and the maximum-width conjecture

Theorem 29 (Extension width of the doubling sequence). For every n ≥ 2, |KUn | = 2n−1 + 1.

Proof. By Corollary 23.

Conjecture 30 (Maximum width). For every n ≥ 2, maxS∈Gn |KS | = 2n−1 + 1, uniquely achieved
by Un .

This conjecture is verified by exhaustive computation for n ≤ 10; see Table 1. A proof would have to
use the fact that the anti-diagonal arises from a Gilbreath sequence, not from arbitrary nonnegative
integers, since the reverse-tree analysis alone permits anti-diagonals exceeding the doubling bound.


13      An exponentially disconnected family

For a finite set X ⊆ Z all of one parity class, #comp(X) denotes the number of maximal runs of
common difference 2.


                                                    24
Definition 31. For n ≥ 5, set Vn := (v1 , . . . , vn ) where v1 = 2, vi = 2i−1 + 1 for 2 ≤ i ≤ n − 1,
and vn = 2n−1 − 1.

So Vn follows the doubling through position n − 1 and then undershoots at the last position by 2:
V5 = (2, 3, 5, 9, 15), V6 = (2, 3, 5, 9, 17, 31), V7 = (2, 3, 5, 9, 17, 33, 63).

Example 32. For V5 , the reverse tree gives D5 = {2, 4, 6, 8, 10}, a single block of 5 consecutive even
integers. For V6 , the right anti-diagonal is (14, 6, 2, 0, 1); running the reverse tree, the preimage
step P14 applied to D5 splits each element into two preimages 14 − d and 14 + d, giving D6 =
{4, 6, 8, 10, 12} ∪ {16, 18, 20, 22, 24}, two 5-element blocks separated by a gap. Figure 6 shows the
first three stages.

                                E6 = 14


                 D5                            E7 = 30                    1 component


                 D6                                                       2 components


                 D7                                                       4 components



                       0       10         20     30      40        50      60


Figure 6: Component doubling in the family Vn (Theorem 35). Each horizontal block represents a
maximal run of even integers spaced by 2. The recursion Dn = PEn (Dn−1 ), with En = 2n−2 − 2,
sends Dn−1 to two separated reflected copies En − Dn−1 and En + Dn−1 . Thus the number of
components doubles at each step.

Lemma 33. For n ≥ 5, Vn ∈ Gn with right anti-diagonal ei = 2n−i−1 − 2 for 1 ≤ i ≤ n − 2 and
en−1 = 1.

Proof. The first n − 1 terms of Vn form the doubling sequence Un−1 , whose triangle is the powers-
of-two array. The final gap is vn − vn−1 = (2n−1 − 1) − (2n−2 + 1) = 2n−2 − 2, giving e1 = 2n−2 − 2.
The rightmost entry of Un−1 ’s row 1 is 2n−3 , so e2 = |2n−2 − 2 − 2n−3 | = 2n−3 − 2. Iterating,
ei = 2n−i−1 − 2 for 1 ≤ i ≤ n − 2; in particular en−2 = 0. Finally en−1 = |1 − 0| = 1.

Throughout this section write Dn := DVn for the distance set of Vn , and recall the preimage map
Pe of Section 8. By Lemma 33 the right anti-diagonal of Vn is (e1 , . . . , en−1 ) = (2n−2 − 2, 2n−3 −
2, . . . , 2, 0, 1), and the anti-diagonal of Vn is precisely that of Vn−1 with one new leading entry
En := 2n−2 − 2 prepended. Consequently the reverse-tree process (Proposition 18) for Vn is the
process for Vn−1 followed by one additional preimage step:

                           Dn = PEn (Dn−1 ),       En = 2n−2 − 2    (n ≥ 6).                       (1)

We first isolate the arithmetic of the extremes of Dn , since the component count and cardinality
both depend on it.




                                                  25
Lemma 34 (Extremes and structure of Dn ). For every n ≥ 5 the set Dn consists of positive even
integers, and
                    min Dn = 2n − 8,       max Dn = 2n−1 − 2n + 4.
Moreover, for n ≥ 6 the recursion (1) acts as two disjoint reflected copies:

                                      Dn = (En − Dn−1 ) ⊔ (En + Dn−1 ),                          (2)

where every element of En − Dn−1 is strictly smaller than every element of En + Dn−1 .

Proof. We argue by induction on n.
Base case n = 5. The reverse-tree computation in Example 32 gives D5 = {2, 4, 6, 8, 10}, all positive
and even, with min D5 = 2 = 2(5) − 8 and max D5 = 10 = 24 − 2(5) + 4. This establishes the base
case. (The split (2) is asserted only for n ≥ 6.)
Inductive step. Fix n ≥ 6 and assume the statement for n − 1; in particular Dn−1 consists of
positive even integers with

                         min Dn−1 = 2n − 10,         max Dn−1 = 2n−2 − 2n + 6.                   (3)

Recall that

                 PEn (Dn−1 ) = {En + d : d ∈ Dn−1 } ∪ {En − d : d ∈ Dn−1 , En ≥ d}.

We first show the second branch is unconditional, i.e. that En ≥ d for every d ∈ Dn−1 . It suffices
to check En ≥ max Dn−1 . Using (3),

                 En − max Dn−1 = (2n−2 − 2) − (2n−2 − 2n + 6) = 2n − 8 ≥ 4 > 0,                  (4)

since n ≥ 6. Hence En > max Dn−1 ≥ d for all d ∈ Dn−1 , so both branches are active and
Dn = (En − Dn−1 ) ∪ (En + Dn−1 ).
Disjoint and ordered. Every element of the lower branch satisfies En − d < En (as d > 0), while
every element of the upper branch satisfies En +d > En . Hence each element of En −Dn−1 is strictly
below En and each element of En + Dn−1 strictly above, giving (2) with the claimed ordering; in
particular the union is disjoint.
Parity and positivity. Each d ∈ Dn−1 is even and En = 2n−2 − 2 is even, so En ± d is even. The
smallest element of Dn is En − max Dn−1 = 2n − 8 > 0 by (4); hence all elements of Dn are positive.
New extremes. By the ordering in (2),

                                      min Dn = En − max Dn−1 = 2n − 8,

              max Dn = En + max Dn−1 = (2n−2 − 2) + (2n−2 − 2n + 6) = 2n−1 − 2n + 4.
These are the claimed formulas at n, completing the induction.

With the structure of Dn in hand, the main theorem follows.
Theorem 35 (Exponentially many components). For every n ≥ 5,

                |KVn | = 5 · 2n−4 ,     #comp(KVn ) = 2n−4 ,   h(Vn ) = 3 · 2n−4 − 2n + 5.

                                                     26
Proof. We first show, by induction on n ≥ 5, that

                            |Dn | = 5 · 2n−5   and     #comp(Dn ) = 2n−5 .                       (5)

For n = 5, D5 = {2, 4, 6, 8, 10} has |D5 | = 5 = 5 · 20 and is a single run, so #comp(D5 ) = 1 = 20 .
For n ≥ 6, Lemma 34 gives the disjoint union (2); since d 7→ En + d and d 7→ En − d are injective,
each copy has |Dn−1 | elements, so |Dn | = 2|Dn−1 | = 5 · 2n−5 .
For the component count, the gap separating the two copies in (2) is
                                    
 min(En + Dn−1 ) − max(En − Dn−1 ) = (En + min Dn−1 ) − (En − min Dn−1 ) = 2 min Dn−1 ≥ 4

by Lemma 34 (min Dn−1 = 2n − 10 ≥ 2 for n ≥ 6). A gap of at least 4 between consecutive even
integers breaks the run, so the two copies lie in distinct parity-lattice components, and within each
copy the reflection d 7→ En ± d preserves adjacency of common difference 2. Hence #comp(Dn ) =
2 #comp(Dn−1 ) = 2n−5 , proving (5).
By Lemma 34, min Dn = 2n − 8 > 0, so 0 ∈     / Dn and the reflection of Theorem 16 produces two
disjoint translated copies KVn = (vn − Dn ) ⊔ (vn + Dn ), separated by a gap of 2 min Dn ≥ 4. Hence

               |KVn | = 2|Dn | = 5 · 2n−4 ,    #comp(KVn ) = 2 #comp(Dn ) = 2n−4 .

Finally, by Lemma 33,
                      n−2
                      X
                            2n−i−1 − 2 + 1 = (2n−1 − 2) − 2(n − 2) + 1 = 2n−1 − 2n + 3,
                                      
           A(Vn ) =
                      i=1

so by Lemma 7 the candidate set has size A(Vn ) + 2 = 2n−1 − 2n + 5, and

             h(Vn ) = |CVn | − |KVn | = (2n−1 − 2n + 5) − 5 · 2n−4 = 3 · 2n−4 − 2n + 5.

Corollary 36. For every n ≥ 5,

                  max #comp(KS ) ≥ 2n−4        and    max h(S) ≥ 3 · 2n−4 − 2n + 5.
                 S∈Gn                                 S∈Gn


The first inequality is sharp for n ≤ 10 (by exhaustive computation); the second is not, in general.


14    Computational data

Table 1 records enumeration data for Gn computed using the corrected extension test, as well as
extremal-width data for 2 ≤ n ≤ 10, with N11 included since it is computable from the G10 frontier.
The data was generated using the reverse-tree algorithm of Proposition 18; the code in Section 17
reproduces the full table.
For 2 ≤ n ≤ 10 the unique maximizer of |KS | is the doubling sequence Un , and the unique minimizer
is Ln . The fraction of defective sequences grows from 1/6 ≈ 17% at n = 5 to 322054/559127 ≈
57.6% at n = 10.



                                                 27
       n           Nn    mn    #min     Mn    #max          #i.c.   #defective      max def   max comp
       2             1     3      1       3      1              1               0        0           1
       3             1     5      1       5      1              1               0        0           1
       4             2     5      1       9      1              2               0        0           1
       5             6     5      1      17      1              5               1        1           2
       6            27     5      1      33      1             22               5        5           4
       7           180     5      1      65      1            120              60       15           8
       8         1,786     5      1     129      1          1,026             760       47          16
       9        26,094     5      1     257      1         12,782          13,312      121          32
       10      559,127     5      1     513      1        237,073         322,054      281          64
       11   17,535,396     –      –       –      –              –               –        –           –

Table 1: Enumeration data for Gn computed using the corrected extension test, together with
extremal extension-width data. Here “#i.c.” is the count of interval-complete sequences (h(S) = 0),
“#defective” is the count with h(S) > 0, and components are counted in the parity lattice. For
n = 11 only N11 is recorded; per-sequence statistics for n = 11 were not enumerated.

14.1    OEIS connections

The enumeration Nn = |Gn | coincides, after an index shift, with OEIS [20] (“number of positive
increasing integer sequences of length n with Gilbreath transform (1, 1, 1, . . .)”), whose terms are
1, 1, 1, 2, 6, 27, 180, 1786, 26094, 559127, 17535396, . . .. This provides an independent confirmation of
our corrected values N2 , . . . , N11 = 1, 1, 2, 6, 27, 180, 1786, 26094, 559127, 17535396, and we attribute
the enumeration to that entry rather than claiming it as new. A comment of T. D. Noe on [20]
further records that the extremal (slowest- and fastest-growing) length-n sequences are the minimal
sequence and the doubling sequence, consistent with our Theorems 25 and 29.
By contrast, we did not find OEIS entries matching the interval-complete counts

                                  1, 1, 2, 5, 22, 120, 1026, 12782, 237073,

the maximum-defect sequence
                                       0, 0, 0, 1, 5, 15, 47, 121, 281,
or the Vn extension-set width 5 · 2n−4 ; to the best of our knowledge the structural theory of KS
developed here (interval-completeness criterion, holes, defect, and the Vn family) is new. For
broader context on the iterated-difference and difference-triangle literature, related OEIS entries
include A036262 [18] (the Gilbreath array of the primes), A036261 [17] (the corresponding iterated
absolute differences), A054977 [19] (the conjectured leftmost column), A173816 [21] (row sums),
and A347924–A347925 [22, 23] (Gatti polynomial coefficient numerators and denominators). None
of these coincide with the interval-complete, defect, or component sequences above. As exhaustive
sequence search is delicate, we would welcome verification of these originality claims.


15     Discussion

The framework of this paper has three complementary readings.
From the additive-combinatorics side, the signed-sum set associated to a finite Gilbreath sequence
is a subset-sum set (Theorem 12), and the coincidence S± = CS is governed by the classical

                                                     28
Brown completeness criterion applied to the weight multiset WS = {e1 , . . . , en−1 , 1}. The interval-
completeness criterion of Theorem 20 is the ordered analogue of Brown’s criterion: the same “next
weight is at most one plus the sum of previous weights” shape, but read in the fixed anti-diagonal
order forced by the folding recurrence.
From the dynamical-systems side, the valid distance set is the fiber over the apex value 1 of an
ordered composition of folding maps x 7→ |x − ei |. The reverse-tree algorithm of Section 8 solves
the corresponding inverse problem explicitly. This places the work alongside the Proth–Gilbreath
operator analysis of Bhat, Cobeli, and Zaharescu [2], which studies the forward dynamics of the
same triangle. Our results contribute the structural analysis of the inverse direction for finite
prefixes.
From the probabilistic side, the conjectures recorded in Section 16 ask for the asymptotic distri-
bution of the defect and component count over a uniformly random sequence S ∈ Gn . These are
the finite, deterministic counterparts of the small-gap probabilistic questions resolved by Chase [7],
who studies whether infinite sequences with random small gaps are Gilbreath. The framework of
this paper makes such finite-distribution questions concrete: each one is a statement about the
distribution of FS−1 ({1}) as S ranges over Gn .
In all three readings the central object is the same. The interval-completeness theorem is simulta-
neously a sharp completeness criterion for an ordered subset-sum problem, a structure theorem for
finite fibers of folding-map compositions, and a deterministic companion to the random Gilbreath
models studied recently.


16     Open questions

 (1) (Conjecture 30) Is Mn = 2n−1 + 1 for all n, uniquely achieved by Un ?

 (2) Asymptotics of pn := #{S ∈ Gn : h(S) = 0}/Nn . Data through n = 10 shows

                           pn = 1, 1, 1, 65 , 22   120 1026 12782 237073
                                              27 , 180 , 1786 , 26094 , 559127 ≈ 0.424.

      Does pn tend to a limit? More generally, what are the asymptotic distributions of h(S), |KS |,
      and #comp(KS ) under uniform sampling on Gn ? These are finite, deterministic analogues of
      the probabilistic Gilbreath questions resolved by Chase [7].

 (3) Closed form for maxS∈Gn h(S). The lower bound 3 · 2n−4 − 2n + 5 from Corollary 36 is not
     tight.

 (4) Is maxS∈Gn #comp(KS ) = 2n−4 for all n ≥ 5? Verified for n ≤ 10.

 (5) Stability classification near the minimum: characterize S ∈ Gn with |KS | ≤ 9.


17     Reproducible code

The following Python module computes the data in Table 1 using only the right anti-diagonal state
rather than repeatedly storing and rebuilding full difference triangles. This makes the computation
substantially faster than a direct triangle-based reference implementation. The program also verifies

                                                    29
the first-hole example and computes N11 by summing the number of increasing valid extensions
from the length-10 frontier.
 from functools import lru_cache

 def preimage_step(e, T):
     """
     Preimages of T under x -> |x-e|, with x >= 0.
     For each t in T, the solutions are x=e+t and, if e>=t, x=e-t.
     """
     out = set()
     for t in T:
         out.add(e + t)
         if e >= t:
             out.add(e - t)
     return tuple(sorted(out))

 @lru_cache(maxsize=None)
 def valid_distances_from_antidiagonal(e_tuple):
     """
     Given the right anti-diagonal (e_1,...,e_{n-1}), return
     D_S = {|k-s_n| : k in K_S}.
     """
     T = (1,)
     for e in reversed(e_tuple):
         T = preimage_step(e, T)
     return T

 def child_antidiagonal(e_tuple, d):
     """
     If d=|k-s_n| is a valid positive distance and k=s_n+d, return the
     right anti-diagonal after appending k.

     Old anti-diagonal: (e_1,...,e_{n-1}).
     New anti-diagonal: (d, |d-e_1|, ||d-e_1|-e_2|, ..., 1).
     """
     r = d
     new_e = [r]
     for e in e_tuple:
         r = abs(r - e)
         new_e.append(r)
     assert new_e[-1] == 1
     return tuple(new_e)

 def width_from_distances(D):
     """
     Full extension width |K_S| from the distance set D.
     Distance 0 contributes one extension; each positive distance
     contributes two symmetric extensions.
     """
     return 2 * len(D) - (1 if 0 in D else 0)

 def valid_extensions_from_state(sn, e_tuple):
     """
     Full two-sided valid-extension set K_S.
     """
     D = valid_distances_from_antidiagonal(e_tuple)
     out = set()
     for d in D:


                                               30
        out.add(sn + d)
        out.add(sn - d)
    return tuple(sorted(out))

def candidate_set_from_state(sn, e_tuple):
    """
    Candidate set C_S.
    """
    A = sum(e_tuple)
    return tuple(k for k in range(sn - A - 1, sn + A + 2)
                 if (k - sn) % 2 == 0)

def is_interval_complete(e_tuple):
    """
    Check the criterion e_i <= 1 + sum_{j>i} e_j for all i<=n-2.
    Here e_tuple = (e_1,...,e_{n-1}).
    """
    tail_sum = e_tuple[-1] # e_{n-1}=1
    for e in reversed(e_tuple[:-1]):
        if e > 1 + tail_sum:
            return False
        tail_sum += e
    return True

def components_count(vals, step=2):
    """
    Number of connected components in one parity lattice.
    """
    vals = sorted(set(vals))
    if not vals:
        return 0
    count = 1
    for a, b in zip(vals, vals[1:]):
        if b - a != step:
            count += 1
    return count

def K_components_count(sn, e_tuple):
    """
    Number of connected components of K_S in the parity lattice.
    """
    return components_count(valid_extensions_from_state(sn, e_tuple), step=2)

def generate_states(max_n):
    """
    Generate states for G_n up to max_n.

    A state is (s_n, e_tuple, seq), where:
      s_n     = last term,
      e_tuple = right anti-diagonal,
      seq     = full sequence, kept only for reporting examples.
    """
    states = [(3, (1,), (2, 3))]
    by_n = {2: states}

    for n in range(3, max_n + 1):
        next_states = []
        for sn, e_tuple, seq in states:
            D = valid_distances_from_antidiagonal(e_tuple)


                                              31
           for d in D:
               if d > 0: # increasing extension k=s_n+d
                   k = sn + d
                   new_e = child_antidiagonal(e_tuple, d)
                   next_states.append((k, new_e, seq + (k,)))
       states = next_states
       by_n[n] = states
       print(f"generated G_{n}: {len(states)} sequences")

   return by_n

def summarize_states(states):
    """
    Compute one row of the numerical data table.
    """
    N = len(states)

   min_width = None
   max_width = None
   num_min = 0
   num_max = 0

   num_complete = 0
   num_defective = 0
   max_defect = 0
   max_components = 0

   min_seq = None
   max_seq = None
   max_defect_seq = None
   max_components_seq = None

   for sn, e_tuple, seq in states:
       D = valid_distances_from_antidiagonal(e_tuple)
       width = width_from_distances(D)
       defect = sum(e_tuple) + 2 - width
       comp = K_components_count(sn, e_tuple)

       if min_width is None or width < min_width:
           min_width = width
           num_min = 1
           min_seq = seq
       elif width == min_width:
           num_min += 1

       if max_width is None or width > max_width:
           max_width = width
           num_max = 1
           max_seq = seq
       elif width == max_width:
           num_max += 1

       if is_interval_complete(e_tuple):
           num_complete += 1
       else:
           num_defective += 1

       if defect > max_defect:
           max_defect = defect


                                              32
           max_defect_seq = seq

       if comp > max_components:
           max_components = comp
           max_components_seq = seq

   return {
       "N": N,
       "min_width": min_width,
       "num_min": num_min,
       "min_seq": min_seq,
       "max_width": max_width,
       "num_max": num_max,
       "max_seq": max_seq,
       "num_complete": num_complete,
       "num_defective": num_defective,
       "max_defect": max_defect,
       "max_defect_seq": max_defect_seq,
       "max_components": max_components,
       "max_components_seq": max_components_seq,
   }

def print_table(by_n):
    """
    Print the table data for n=2,...,10.
    """
    header = (
        "n | N_n | m_n | #min | M_n | #max | "
        "#ic | #def | max def | max comp | max seq"
    )
    print(header)
    print("-" * len(header))

   for n in range(2, 11):
       stats = summarize_states(by_n[n])
       print(
           n,
           stats["N"],
           stats["min_width"],
           stats["num_min"],
           stats["max_width"],
           stats["num_max"],
           stats["num_complete"],
           stats["num_defective"],
           stats["max_defect"],
           stats["max_components"],
           stats["max_seq"],
           sep=" | "
       )

def compute_N_next(states):
    """
    Given states for G_n, compute N_{n+1} by summing the number of
    positive valid distances.
    """
    total = 0
    for sn, e_tuple, seq in states:
        D = valid_distances_from_antidiagonal(e_tuple)
        total += sum(1 for d in D if d > 0)


                                              33
    return total

def verify_first_hole():
    """
    Verify the first-hole example S=(2,3,5,9,15).
    """
    S = (2, 3, 5, 9, 15)
    sn = 15
    e_tuple = (6, 2, 0, 1)

    C = candidate_set_from_state(sn, e_tuple)
    K = valid_extensions_from_state(sn, e_tuple)
    H = tuple(sorted(set(C) - set(K)))

    print("\nFirst-hole verification")
    print("S =", S)
    print("right anti-diagonal =", e_tuple)
    print("A(S) =", sum(e_tuple))
    print("C_S =", C)
    print("K_S =", K)
    print("H_S =", H)

def V_sequence(n):
    """
    The component-doubling family V_n.
    """
    assert n >= 5
    return (2,) + tuple(2**(i-1) + 1 for i in range(2, n)) + (2**(n-1) - 1,)

def V_antidiagonal(n):
    """
    Right anti-diagonal of V_n:
    e_i = 2^{n-i-1}-2 for 1<=i<=n-2, and e_{n-1}=1.
    """
    assert n >= 5
    return tuple(2**(n-i-1) - 2 for i in range(1, n-1)) + (1,)

def verify_V_family(up_to=10):
    """
    Verify the V_n formulas for n=5,...,up_to.
    """
    print("\nV_n family verification")
    print("n | V_n | |K| | components | defect")
    for n in range(5, up_to + 1):
        S = V_sequence(n)
        sn = S[-1]
        e_tuple = V_antidiagonal(n)
        D = valid_distances_from_antidiagonal(e_tuple)
        width = width_from_distances(D)
        comp = K_components_count(sn, e_tuple)
        defect = sum(e_tuple) + 2 - width
        print(n, S, width, comp, defect, sep=" | ")

if __name__ == "__main__":
    by_n = generate_states(10)
    print()
    print_table(by_n)

    N11 = compute_N_next(by_n[10])


                                              34
     print("\nN_11 =", N11)

     verify_first_hole()
     verify_V_family(10)


On a standard laptop, this anti-diagonal-state implementation produces the table through n = 10
and computes N11 in well under a minute. Runtime will vary by machine.


Acknowledgments

This project made use of AI tools during the exploratory stage, including computational experimen-
tation, conjecture generation, and preliminary drafting. The computational claims were verified
against an independent implementation; responsibility for the mathematical statements and proofs
rests with the author, and the arguments are offered for expert review.


References

 [1] T. Agama, On the gap sequence and Gilbreath’s conjecture, preprint, arXiv:2104.05258 (2021).

 [2] R. N. Bhat, C. Cobeli, and A. Zaharescu, Filtered rays over iterated absolute differences on
     layers of integers, Chaos, Solitons & Fractals 178 (2024), 114315.

 [3] R. N. Bhat, C. Cobeli, and A. Zaharescu, On quasi-periodicity in Proth–Gilbreath triangles,
     Bull. Math. Soc. Sci. Math. Roumanie 67(115) (2024), no. 1, 3–21.

 [4] J. L. Brown, Jr., Note on complete sequences of integers, American Mathematical Monthly 68
     (1961), no. 6, 557–560.

 [5] S. A. Burr and P. Erdős, A Ramsey-type property in additive number theory, Glasgow Mathe-
     matical Journal 27 (1985), 5–10.

 [6] M. Caragiu, A. Zaharescu, and M. Zaki, An analogue of the Proth–Gilbreath conjecture, Far
     East Journal of Mathematical Sciences 81 (2013), no. 1, 1–12.

 [7] Z. Chase, A random analogue of Gilbreath’s conjecture, Mathematische Annalen 388 (2024),
     2611–2625. doi:10.1007/s00208-023-02579-w.

 [8] D. Chase, J. Hunter, and T. Tao, Gilbreath’s conjecture, a Cramér random model, and a
     deterministic analysis, preprint, arXiv:2607.08712 (2026).

 [9] D. Conlon, J. Fox, and H. T. Pham, Subset sums, completeness and colorings, preprint,
     arXiv:2104.14766 (2021).

[10] M. Gardner, Mathematical games: patterns in primes are a clue to the strong law of small
     numbers, Scientific American 243 (1980), no. 6, 18–28.

[11] R. Gatti, Gilbreath equation, Gilbreath polynomials, and upper and lower bounds for Gilbreath
     conjecture, Mathematics 11 (2023), no. 18, 4006.



                                               35
[12] V. Granville, Piercing Gilbreath’s Conjecture: From Deep Number Theory Insights to Fintech
     and Cybersecurity, preprint, arXiv:2607.04166 (2026).

[13] R. K. Guy, Unsolved Problems in Number Theory, 3rd ed., Springer-Verlag, New York, 2004.

[14] R. B. Killgrove and K. E. Ralston, On a conjecture concerning the primes, Mathematical
     Tables and Other Aids to Computation 13 (1959), 121–122.

[15] H. L. Montgomery, Ten Lectures on the Interface Between Analytic Number Theory and Har-
     monic Analysis, CBMS Regional Conference Series in Mathematics 84, American Mathemat-
     ical Society, Providence, RI, 1994.

[16] A. M. Odlyzko, Iterated absolute values of differences of consecutive primes, Mathematics of
     Computation 61 (1993), no. 203, 373–380.

[17] N. J. A. Sloane et al., Sequence A036261, The On-Line Encyclopedia of Integer Sequences,
     https://oeis.org/A036261.

[18] N. J. A. Sloane et al., Sequence A036262, The On-Line Encyclopedia of Integer Sequences,
     https://oeis.org/A036262.

[19] N. J. A. Sloane et al., Sequence A054977, The On-Line Encyclopedia of Integer Sequences,
     https://oeis.org/A054977.

[20] N. J. A. Sloane et al., Sequence A080839, The On-Line Encyclopedia of Integer Sequences,
     https://oeis.org/A080839.

[21] N. J. A. Sloane et al., Sequence A173816, The On-Line Encyclopedia of Integer Sequences,
     https://oeis.org/A173816.

[22] N. J. A. Sloane et al., Sequence A347924, The On-Line Encyclopedia of Integer Sequences,
     https://oeis.org/A347924.

[23] N. J. A. Sloane et al., Sequence A347925, The On-Line Encyclopedia of Integer Sequences,
     https://oeis.org/A347925.




                                               36
