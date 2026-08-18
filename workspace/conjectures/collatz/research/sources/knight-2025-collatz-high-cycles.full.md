<!-- source: https://hal.science/hal-04261183/document | converted from PDF -->

HAL Id: hal-04261183

https://hal.science/hal-04261183v1

Preprint submitted on 26 Oct 2023

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

Distributed under a Creative Commons CC BY 4.0 - Attribution - International License

Collatz High Cycles Do Not Exist

Kevin Knight

To cite this version:

Kevin Knight. Collatz High Cycles Do Not Exist. 2023. ⟨hal-04261183⟩

Collatz High Cycles Do Not Exist

Kevin Knight

September 23, 2023

Abstract

The Collatz function takes odd n to (3n + 1)/2 and even n to n/2. Under the
iterated Collatz function, every positive integer is conjectured to end up in the trivial
cycle 1-2-1. Two types of cycles are of special interest. Consider the set S consisting
of the smallest members of all cycles containing the same number of odd terms. The
circuit contains the smallest member of S, while the high cycle contains the largest.
It is known that no circuits of positive integers exist (except 1-2-1); this paper shows
that there are likewise no high cycles of positive integers.

1 Introduction

The Collatz function is
 T (n) =
 



 3n + 1
2 , if n is odd;

n
2, otherwise.

Iterating this function famously yields interesting sequences. For example:

31 → 47 → 71 → 107 → 161 → 242 → 121 → 182 → 91 → 137 → 206
→ 103 → 155 → 233 → 350 → 175 → 263 → 395 → 593 → 890 → 445
→ 668 → 334 → 167 → 251 → 377 → 566 → 283 → 425 → 638 → 319
→ 479 → 719 → 1079 → 1619 → 2429 → 3644 → 1822 → 911 → 1367
→ 2051 → 3077 → 4616 → 2308 → 1154 → 577 → 866 → 433 → 650
→ 325 → 488 → 244 → 122 → 61 → 92 → 46 → 23 → 35 → 53 → 80
→ 40 → 20 → 10 → 5 → 8 → 4 → 2 → 1 → 2 → 1 → . . .

The Collatz conjecture posits that every positive integer eventually reaches 1. The con-
jecture was veriﬁed in 2021 for all 1 ≤ n ≤ 10
21 [2], but it has not yet been proven or
refuted.
 1

100

90

80

70

60

50

40

30

20
 323
13

491
13

743
13

1121
13
 1688
13
 844
13

422
13
347
13

527
13

797
13
 1202
13
 601
13

908
13

454
13

383
13

581
13
 878
13

439
13

665
13
 1004
13
 502
13
485
13
 734
13
 557
13

842
13
 638
13

367
13
 421
13

211
13
 227
13

251
13
 259
13

283
13
 287
13

319
13

Figure 1: All of the rational Collatz cycles of length k = 8 with x = 5 odd terms. Of special
note are the outermost cycle (the circuit), in light gray, and the innermost cycle (the high
cycle), in dark gray.

If T i(n) = n for some positive integer n, there is a Collatz cycle of length i whose ﬁrst
term is n. The only known T -cycle is the trivial one: 1 → 2 → 1.
The unresolved Weak Collatz conjecture claims that there are no positive integer cycles.
(It is called “weak” because it allows for the possibility of a start number that diverges to
inﬁnity, never reaching 1.)
We can also consider cycles with rational values. Figure 1 shows all cycles of length k = 8
with x = 5 odd terms. Considering the term 211
13 to be odd (by its numerator), the next term
produced by the Collatz process is (3( 211
13 ) + 1)/2 = 323
13 (also odd).
For any k and x, the outermost and innermost cycles are of special interest. Let S contain
the smallest members of each cycle (here, 211
13 , 227
13 , . . . 319
13 ). The outermost cycle (called the
circuit) contains the lowest member in S, while the innermost cycle (called the high cycle)
contains the highest member in S.
Steiner [10] showed that no positive integer circuits exist for any k, x (except k = 2, x =

2

1). The current paper shows likewise that no high cycles of positive integers exist.

2 Parity vectors

Associated with every cycle member m is a unique parity vector that records the even (0)
and odd (1) terms obtained from k iterations of the Collatz function.

Example 2.1 (Cycle member to parity vector). Starting with m = 211
13 , we encounter 5 odd
terms followed by 3 even terms, so the corresponding parity vector is 11111000.

Likewise, given a parity vector v, we can compute a cycle member m.

Example 2.2 (Parity vector to cycle member). Applying v = 110 to arbitrary start number
n yields [3 3n+1
2 + 1]/2/2 = 9
8n + 5
8. To make a cycle, we set n = 9
8n + 5
8. Solving this equation
yields n = −5, which is part of the −5 → −7 → −10 → −5 cycle.

Generalizing this idea, B¨ohm and Sontacchi [4] give the cycle member associated with
arbitrary parity vector v as
 f (v) =
 x−1∑

i=0 2
di(v) 3
x−i−1

2k − 3x , (2.1)

where d0(v) < . . . < dx−1(v) are the (zero-based) indices of 1s in v. Since we are only
interested in Collatz cycles with positive terms, the denominator must be positive, so k >
x log2 3.
The Weak Collatz Conjecture can be restated: “Is there a parity vector v such that f (v)
is an integer greater than 2?”
It will sometimes be useful to refer to the numerator only:

g(v) =
 x−1∑

i=0 2
di(v) 3
x−i−1. (2.2)

Note that rotating a parity vector produces another term in the same rational cycle.

Example 2.3 (Rotation). f (100) = 1
5, f (001) = 4
5, and f (010) = 2
5. These are all entry
points into the 1
5 → 4
5 → 2
5 → 1
5 cycle.

Finally, we can restrict ourselves to aperiodic parity vectors. Consider f (1101011010) =
23
5 , which is part of the double cycle 23
5 → 37
5 → 58
5 → 29
5 → 46
5 → 23
5 → 37
5 → 58
5 → 29
5 →
46
5 → 23
5 . Had these been integers, the aperiodic f (11010) would also be an integer.

3

3 No integer circuits

The parity vector vc = 1
x0
k−x is associated with the smallest member of the (k, x)-circuit.
Following Equation 2.1,
 f (vc) =
 x−1∑

i=0 2
i3
x−i−1

2k − 3x .

We provide a simple proof that (non-trivial) Collatz circuits do not exist, after three
lemmas.

Lemma 3.1. f (vc) simpliﬁes to 3
x − 2
x

2k − 3x.

Proof. By induction, omitted. □

Lemma 3.2. If there is a non-trivial positive integer circuit of length k with x odd terms,
then 2 · ( 3
2)x ≥ 2
k−x − 1.

Proof. This follows from the fact that the putative circuit’s smallest member is at least 1.

3
x − 2
x

2k − 3x ≥ 1

3
x − 2
x ≥ 2
k − 3
x

2 · 3
x ≥ 2
k + 2x

2 · (3
2 )
x ≥ 2
k−x − 1.
 □

Lemma 3.3 (Ellison [7]). For integers k and x, with x > 17, we have 2
k − 3
x > 2.56
x.

Proof. We start with Ellison’s original bound (for k > 27) and use the fact that k > x log2 3
in positive cycles.
 2
k − 3
x > 2
k

ek/10 > 1.8
k > 1.8
x log2 3 > 2.56
x, for x > 17. □

Theorem 3.4 (Steiner, 1977). Non-trivial Collatz circuits do not exist.

Proof. Assume f (vc) = 3
x − 2
x

2k − 3x is a positive integer. Then the following are also positive

integers:
 4

3
x − 2
x

2k − 3x + 1,

3
x − 2
x

2k − 3x + 2
k − 3
x

2k − 3x,

2
k − 2
x

2k − 3x,

2
x(2
k−x − 1)
2k − 3x , and 2
k−x − 1
2k − 3x .

We can remove the 2x in the last step without aﬀecting the expression’s purported inte-
grality, since the denominator is odd.
However, the last term is actually less than one; we invoke Lemmas 3.3 and 3.2 to show
that the denominator outstrips the numerator. For x > 17,

2
k − 3
x > 2.56
x > 2 · (1.5)x ≥ 2
k−x − 1.

2
k−x − 1 = 0 only when k = 2, x = 1; setting aside this case, we obtain the contradiction
0 < 2k−x−1
2k−3x < 1. Cases of x ≤ 17 are handled by the fact that any non-trivial Collatz cycle
must contain many millions of odd terms [6]. □

To date, all no-circuit proofs depend on deep lower bounds for 2k − 3
x, such as Ellison’s,
which are all derived from Alan Baker’s pioneering transcendental number theory work [1].
As Jeﬀrey Lagarias [9] remarks, “The most remarkable thing about Theorem [. . . ] is the
weakness of its conclusion compared to the strength of the methods used in its proof.”1

4 The high cycle

In this section, characterize the Collatz high cycle.

Deﬁnition 4.1. Let vh be a (k, x)-parity vector with 1s indexed by di(v) = ⌊ k
xi⌋, for 0 ≤
i ≤ x − 1.

Example 4.2. For k = 8, x = 5, vh = 11011010.

1Note that certain circuits can be ruled out without these deep bounds. For example, if k and x are not
co-prime, then we can factor 2k −3
x. E.g., (2
k/2 +3
x/2)(2
k/2 −3x/2) > 2
k/2 > 2xlog3/2 > 1.72
x > 2
k−x −1. Or

for the case of vc = 1111111100000, it follows that if f (vc) = 3
8 − 28

213 − 38 is an integer, then so is 31f (vc) + 206,

but it happens that 31 3
8 − 2
8

213 − 38 + 206 213 − 3
8

213 − 38 = 3
12

213 − 38, which is not integral.

5

Example 4.3. For k = 21, x = 13, vh = 110110101101101011010.

The vector vh is the well-known (upper) Christoﬀel word [3], constructed so that its 1s
are roughly evenly spread among its 0s. The cycle member corresponding to vh is

f (vh) =
 x−1∑

i=0 3
x−i−12
⌊ k
x i⌋

2k − 3x .

Now we list a number of properties of vh.
First, f (vh) is the smallest member of its cycle.

Theorem 4.4 (Halbeisen and Hungerb¨uhler [8]). For every (k, x) parity vector v that is a
rotation of vh, we have f (vh) ≤ f (v).

Remark 4.5. It is known that a Christoﬀel word vh is at a lexicographic extreme among all
its rotations [3]. However, lexicographic ordering does not always coincide with f -ordering.
For example, f (11110010) = 259
13 , f (11100101) = 395
13 , and f (10111100) = 341
13 . Of course,
lexicographic ordering correlates roughly with f -ordering, as left-heavy vectors tend to be
associated with smaller cycle members.

Theorem 4.6. Among all the (k, x) upper Christoﬀel words, f (vh) is maximized when k =
⌈x log2 3⌉.

Proof. Let vh be an upper Christoﬀel word with k = ⌈x log2 3⌉. Let u be a longer (k + 1, x)-
high-cycle parity vector. Replacing k by k + 1 increases the numerator of f (v) by no more
than a factor of 2, while increasing the denominator by more than a factor of 2.

f (u) =
 x−1∑

i=0 3
x−i−12
⌊ k+1
x i⌋

2k+1 − 3x =
 x−1∑

i=0 3
x−i−12
⌊ k
x i+ i
x ⌋

2k+1 − 3x

<
 x−1∑

i=0 3
x−i−12
⌊ k
x i⌋+1

2k+1 − 2 · 3x = 2 · x−1∑

i=0 3
x−i−12
⌊ k
x i⌋

2(2k − 3x) = f (v). □

Similar reasoning holds if u is a (k + n, x) upper Christoﬀel word, for any n ≥ 1.
Next, we conﬁrm the reader’s suspicion that f (vh) is indeed a member of the high cycle.
Let S contain the smallest members of each (k, x)-cycle.

Theorem 4.7 (Halbeisen and Hungerb¨uhler [8]). Let v be a parity vector associated with
the smallest member of any (k, x)-cycle, and let vh be an upper Christoﬀel word with k =
⌈x log2 3⌉. Then, f (vh) ≥ f (v).
 6

Remark 4.8 (Tangential). This theorem is useful for proving that any Collatz cycle must
be long. Just for example, it is easy to verify empirically that f (vh) < 10
13 for all x <
10, 000, 000, implying that every cycle (not just the high cycle) with fewer than ten million
odd terms has some member less than 10
13. Since no Collatz counter-examples exist among
the ﬁrst 10
20 positive integers [2], a purported Collatz cycle must have more than ten million
odd terms. Stronger results have been obtained through analytical means [8]. Of course,
f (vh) will outstrip any ﬁnite conﬁrmation, after some x, because O(3
xx) exceeds O(2
k − 3
x).

Recall the cycle member corresponding to vh.

f (vh) =
 x−1∑

i=0 3
x−i−12
⌊ k
x i⌋

2k − 3x ,

Due to the ﬂoor function, we cannot simplify this expression as we did for f (vc). Its
value can only be partially wrangled through upper and lower bounds.

Theorem 4.9 (Halbeisen and Hungerb¨uhler [8]).

3
x(x/20)
2⌈x log2 3⌉ − 3x < f (vh) < 3
x(7x/10)
2⌈x log2 3⌉ − 3x.

These bounds can be improved from (x/20, 7x/10) to (x/6, x/2); we omit the proof for
brevity.

5 No integer high cycles

In this section, we prove our main result that f (vh) is never an integer. To do this, we need
two more facts about Christoﬀel words. First, f (vR
h ) is a member of the same cycle as f (vh).

Theorem 5.1 (Cohn [5]). The reverse vR
h of an upper Christoﬀel word vh is also a rotation
of it.

Therefore, f (vh) and f (vR
h ) are in the same cycle. Indeed, f (vR
h ) is the largest member
of the cycle, though we do not need this fact; also for interest, the left-rotation distance is
the multiplicative inverse of x modulo k.

Theorem 5.2 (Berstel et al [3]). For aperiodic vh, we have vh = 1u0, and vR
h = 0u1.

Example 5.3. vh = 11011010, vR
h = 01011011, and u = 101101. Incidentally, u is always
a palindrome, though we do not need this fact.

Because vh and vR
h are virtually identical, diﬀering only in their ﬁrst and last components,
we expect f (vh) and f (vR
h ) to have similar summands. We express both in terms of u, via
Equations 2.1 and 2.2.
 7

f (vh) = 2g(u) + 3x−1

2k − 3x

f (vR
h ) = 6g(u) + 2k−1

2k − 3x

In the ﬁrst case, we create vh by shifting u one place to the right (doubling every
summand) and adding a 1 to the left edge. In the second case, shifting u requires both a
doubling (for the same reason) and a tripling (from adding a 1 to the right edge).

Theorem 5.4 (Main result). No high cycle consists of integers.

Proof. We know f (vh) and f (vR
h ) are both members of the high cycle (Theorems 4.7 and
5.1). If they are both integers, then so are

3f (vh) − f (vR
h ) + 1,

3 2g(u) + 3x−1

2k − 3x − 6g(u) + 2k−1

2k − 3x + 2
k − 3
x

2k − 3x ,

2
k − 2
k−1

2k − 3x , and 2
k−1

2k − 3x .

However, 2
k−1 is not divisible by any odd number, so we have a contradiction. □

Example 5.5. For the (8, 5)-high-cycle, Figure 1 gives f (vh) = 319
13 and f (vR
h ) = 842
13 .
Combining gives 3 319
13 − 842
13 + 13
13 = 27
13.

Note that if we left-rotate vh and vR
h by one position each, we obtain an alternate
pair of high-loop members (u01 and u10), whose simple diﬀerence provides the necessary
contradiction. For example, cycle members 485
13 and 421
13 in Figure 1 cannot both be integers,
because 485
13 − 421
13 = 26
13.

6 Summary

Notable features of our proof versus the no-circuit proof include:

• Instead of assuming, by way of contradiction, that f (vc) is an integer, we instead
assume that both f (vh) and f (vR
h ) are both integers.

• Unlike the no-circuit proof, we do not require deep lower bounds [1, 7] on the size of
2
k − 3
x.

• We require no closed-form expression for any high cycle member; by contrast, the
no-circuit proof relies on the expression f (vc) = 3x−2x
2k−3x .

8

References

[1] Alan Baker, Transcendental number theory, Cambridge University Press, 1975.

[2] David Barina, Convergence veriﬁcation of the Collatz problem, The Journal of Super-
computing 77 (2021), 2681–2688.

[3] Jean Berstel, Aaron Lauve, Christophe Reutenauer, and Franco V. Saliola, Combina-
torics on words: Christoﬀel words and repetitions in words, American Mathematical
Society, Providence, RI, 2009.

[4] Corrado B¨ohm and Giovanna Sontacchi, On the existence of cycles of given length in
integer sequences like xn+1 = xn/2 when x is even and xn+1 = 3xn + 1 otherwise, Atti
della Accademia Nazionale dei Lincei. Classe di Scienze Fisiche, Matematiche e Naturali
64 (1978), 260–264.

[5] Harvey Cohn, Markoﬀ forms and primitive words, Mathematische Annalen 196 (1972),
8–22.

[6] Shalom Eliahou, The 3x + 1 problem: new lower bounds on nontrivial cycle lengths,
Discrete Mathematics 118 (1993), 45–56.

[7] W. J. Ellison, On a theorem of S. Sivasankaranarayana Pillai, S´eminaire de th´eorie des
nombres de Bordeaux (1971), 1–10.

[8] Lorenz Halbeisen and Norbert Hungerb¨uhler, Optimal bounds for the length of rational
Collatz cycles, Acta Arithmetica LXXVIII (1997), 227–239.

[9] Jeﬀrey C. Lagarias, The 3x+1 problem and its generalizations, The 3x+1 Problem: The
Ultimate Challenge (Jeﬀrey C. Lagarias, ed.), American Mathematical Society, 2010,
pp. 31–54.

[10] R. P. Steiner, A theorem on the Syracuse problem, Proc. 7th Manitoba Conference on
Numerical Mathematics, 1977, pp. 553–559.

9
