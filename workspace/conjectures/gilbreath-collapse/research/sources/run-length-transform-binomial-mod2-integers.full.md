<!-- source: https://math.colgate.edu/~integers/w81/w81.pdf | converted from PDF -->

#A81 INTEGERS 22 (2022)

SUMS OF PRODUCTS OF BINOMIAL COEFFICIENTS MOD 2
AND RUN LENGTH TRANSFORMS OF SEQUENCES

Chai Wah Wu
IBM Research AI, IBM T. J. Watson Research Center, Yorktown Heights,
New York
cwwu@us.ibm.com

Received: 11/24/21, Revised: 5/6/22, Accepted: 8/12/22, Published: 8/24/22

Abstract
We study properties of functions of binomial coeﬃcients mod 2 and derive a set
of recurrence relations for sums of products of binomial coeﬃcients mod 2. We
show that they result in sequences that are the run length transforms of well known
basic sequences. In particular, we obtain formulas for the run length transform of
the positive integers, Fibonacci numbers, extended Lucas numbers and Narayana’s
cows sequence.

1. Introduction

When is the binomial coeﬃcient even or odd, i.e., what is ( n
k
 ) (mod 2)? It is

well known that when Pascal’s triangle of binomial coeﬃcients is taken mod 2, the
result has a fractal structure in the limit and corresponds to Sierpi´nski’s triangle
(also known as Sierpi´nski’s gasket or Sierpi´nski’s sieve) [8, 10, 4, 5].
Lucas’ theorem [2, 3] provides a simple way to determine the binomial coeﬃ-
cients modulo a prime. It states that for integers k, n and prime p, the following
relationship holds ( n
k
 ) ≡
 m∏

i=0
 ( ni
ki
 ) (mod p)

where ni and ki are the digits of n and k in base p, respectively1.
When p = 2, then ni and ki are the bits in the binary expansion of n and k, and( ni
ki
 ) is 0 if and only if ni < ki. This implies that ( n
k
 ) is even if and only if

ni < ki for some i.
The truth table of ni < ki is

1If the lengths of the base p representations of n and k diﬀer, leading 0’s are prepended to the
shorter representation.

INTEGERS: 22 (2022) 2

ni ki ni < ki
0 0 0
0 1 1
1 0 0
1 1 0

and is logically equivalent to ki ∧ (¬ni). Let us consider the notation ∧, ∨ and ¬
to also function as operations on integers by treating them as bitwise operations
[1, 6, 11] on the binary representation of numbers
2. For instance, 11 ∧ 14 is the
bitwise AND of 10112 and 11102, which is equal to 10102 = 10. This implies the
following well-known fact [10].

Theorem 1. For integers n and k, ( n
k
 ) ≡ 0 (mod 2) if and only if k ∧ (¬n) ̸= 0.

Incidentally, for bits ni and ki, ni < ki is logically equivalent to ¬(ki ⇒ ni).

Consider ( n
k
 ) ( m
r
 ) (mod 2). Clearly this is equivalent to
(( n
k
 ) (mod 2)) (( m
r
 ) (mod 2)) .

Thus ( n
k
 ) ( m
r
 ) ≡ 0(mod 2) if and only if k ∧ (¬n) ̸= 0 or r ∧ (¬m) ̸= 0. This

in turn implies the following result.

Theorem 2. The product of two binomial coeﬃcients modulo 2 satisﬁes
( n
k
 ) ( m
r
 ) ≡ 0 (mod 2) if and only if (k ∧ (¬n)) ∨ (r ∧ (¬m)) ̸= 0.

Analogously for sequences of integers {n[j]}, {k[j]} we have the following result

for (∏T
j=1
 ( n[j]
k[j]
 )) (mod 2).

Theorem 3. The product of T binomial coeﬃcients mod 2 satisﬁes

T∏

j=1
 ( n[j]
k[j]
 ) ≡ 0 (mod 2) if and only if

(k[1] ∧ (¬n[1])) ∨ (k[2] ∧ (¬n[2])) ∨ · · · ∨ (k[T ] ∧ (¬n[T ])) ̸= 0.

These equivalences are simply consequences of Lucas’ theorem for p = 2 but
the use of the bitwise notation will be helpful in deriving properties of binomial
coeﬃcients mod 2. For instance, the following well-known result can easily be
shown.

2Again, leading 0’s are added to the binary operations ∧ and ∨ if the operands diﬀer in bit
lengths. Furthermore, negative integers are represented in binary using the 2’s complement format
[1, 6, 12], in which case leading 1’s are prepended.

INTEGERS: 22 (2022) 3

Lemma 1. The central binomial coeﬃcient ( 2n
n
 ) is even if and only if n > 0.

Proof. First note that ( 0
0
 ) = 1 is odd. For n > 0, let n = 2sr where r is odd.

Then n ∧ ¬2n = 2s(r ∧ ¬2r) since the s least signiﬁcant bits are 0. As r is odd,
r ∧ ¬2r ̸= 0, and the conclusion follows from Theorem 1.

As is common in formulas involving logical operators, ¬ has higher precedence
than ∧ which in turn has higher precedence than ∨.

2. Run Length Transform

For a sequence {bi} of bits, let the 1-runs R denote the sequence of lengths of consec-
utive 1’s in the sequence. For example, for the bits 011011100111, the consecutive
1’s have lengths 2, 3 and 3 and R = (2, 3, 3).
The run length transform of sequences of numbers is deﬁned as follows [7].

Deﬁnition 1. The run length transform of {Sn}n≥0 is given by {Tn}n≥0, where
T0 = S0, and for n > 0, Tn = Πi∈RSi with R being the 1-runs of the binary
representation of n.

In the rest of this paper, as in [7], we assume that S0 = 1. As an example,
suppose n = 463, which is 111001111 in binary. It has a run of 3 1’s and a run of
4 1’s, and thus Tn = S3 · S4. Some ﬁxed points of the run length transform include
the sequences {1, 0, 0, . . . } and {1, 1, 1, . . . }. In [7], the following result is proved
about the run length transform.

Theorem 4. Let {Sn}n≥0 be deﬁned by the recurrence Sn+1 = d0Sn + d1Sn−1 with
initial conditions S0 = 1, S1 = c1. Then the run length transform of {Sn} is given by
{Tn}n≥0 satisfying T0 = 1, T2n = Tn, T4n+1 = c1Tn, and T4n+3 = d0T2n+1 + d1Tn.

Note that the sequence {Sn} may not uniquely deﬁne the values of d0 and d1 in
Theorem 4. For instance, for the sequence {Sn} = {1, 2, 4, 8, . . . }, d0 and d1 can be
chosen to be any integers such that 2d0 + d1 = 4. On the other hand, note that the
run length transform is injective (one-to-one), since Si = T2i−1 for i ≥ 0 and the
sequence {Sn} can be derived from the corresponding sequence {Tn}.

INTEGERS: 22 (2022) 4

3. Recurrence Relations of Products of Binomial Coeﬃcients Modulo 2

Deﬁnition 2. Consider integers ai, i = 1, . . . , 4, with 0 ≤ a1 + a2, and 0 ≤ a3 + a4.
Deﬁne
 F (n, k) = ( a1n + a2k
a3n + a4k
 ) ( n
k
 ) (mod 2)

and g(n, k) = ((a3n + a4k) ∧ ¬(a1n + a2k)) ∨ (k ∧ ¬n).

By Theorem 2, F (n, k) = 1 if and only if g(n, k) = 0. One direct consequence
of this is a property we will often use: if g(m, r) = wg(n, k) for some w ̸= 0, then
F (m, r) = F (n, k). The functions F and g depend on the integers ai whose values
are clear from the context. We next show that F satisﬁes various recurrence rela-
tions. In the formulas below, the arithmetical operations + and × have precedence
over the bitwise logical operators ∧, ∨ and ¬.

Theorem 5. The following relations hold for the function F :

• F (n, k) = 0 if k > n,

• F (2
rn, 2
rk) = F (n, k) for r > 0,

• F (2n, 2k + 1) = F (4n + 1, 4k + 2) = F (4n + 1, 4k + 3) = F (4n + 2, 4k + 1) =
F (4n + 2, 4k + 3) = F (4n, 4k + 1) = F (4n, 4k + 2) = F (4n, 4k + 3) = 0,

• Suppose a3 ∈ {0, 1}. If a1 = 1 or a3 = 0, then F (4n+1, 4k) = F (4n+3, 4k) =
F (2n + 1, 2k) = F (n, k),

• If a3 ∧ ¬a1 ≡ 0 (mod 4) and 0 ≤ a1, a3 < 4, then F (4n + 1, 4k) = F (n, k),

• If a3 ∧ ¬a1 ̸≡ 0 (mod 4), then F (4n + 1, 4k) = 0,

• If 3a3 ∧ ¬3a1 ̸≡ 0 (mod 4), then F (4n + 3, 4k) = 0,

• If a3 ∧ ¬a1 ̸≡ 0 (mod 2), then F (2n + 1, 2k) = 0.

Proof. If k > n, then by deﬁnition ( n
k
 ) = 0 and thus F (n, k) = 0.

Note that g(2n, 2k) = (2(a3n + a4k) ∧ ¬(2(a1n + a2k))) ∨ (2k ∧ ¬2n) = 2g(n, k)
since the least signiﬁcant bit is 0, i.e., F (2n, 2k) = F (n, k).

Next F (n, k) = 0 if ( n
k
 ) ≡ 0 (mod 2), i.e., if (k ∧ ¬n) > 0. It is easy to see

that F (2n, 2k + 1) = F (4n + 1, 4k + 2) = F (4n + 1, 4k + 3) = F (4n + 2, 4k + 1) =
F (4n + 2, 4k + 3) = 0 and F (4n, 4k + i) = 0 for 1 ≤ i ≤ 3.
Since g(4n+1, 4k) = (4(a3n+a4k)+a3 ∧¬4(a1n+a2k)+a1)∨(4k∧¬(4n+1)) and
4k ∧ ¬(4n + 1) ≡ 0 (mod 4), the least signiﬁcant 2 bits of g(4n + 1, 4k) are equal to

INTEGERS: 22 (2022) 5

a3 ∧ ¬a1 (mod 4). This means that if a1 = 1 or a3 = 0, then g(4n + 1, 4k) = 4g(n, k)
and F (4n + 1, 4k) = F (n, k). If a3 ∧ ¬a1 ̸≡ 0 (mod 4), then F (4n + 1, 4k) = 0.
Similarly, we write g(4n + 3, 4k) = (4(a3n + a4k) + 3a3 ∧ ¬(4(a1n + a2k) + 3a1)) ∨
(4k ∧ ¬(4n + 3)) which is equal to 4g(n, k) if a1 = 1 or a3 = 0, i.e., F (4n + 3, 4k) =
F (n, k) if a1 = 1 or a3 = 0 and F (4n + 3, 4k) = 0 if 3a3 ∧ ¬3a1 ̸≡ 0 (mod 4).
Finally, g(2n+1, 2k) = (2(a3n+a4k)+a3 ∧¬(2(a1n+a2k)+a1))∨(2k∧¬(2n+1)).
Thus F (2n + 1, 2k) = 0 if a3 ∧ ¬a1 ̸≡ 0 (mod 2). If a1 = 1 or a3 = 0, then
g(2n + 1, 2k) = 2g(n, k) and F (2n + 1, 2k) = F (n, k).

4. Sums of Products of Binomial Coeﬃcients Modulo 2

In this section, we show that for various values of ai’s, the sequence a(n) =
∑n
k=0 F (n, k) corresponds to the run length transforms of well-known sequences3.
In particular, we show that the sequences

n∑

k=0
 [( n − k
2k
 ) ( n
k
 ) (mod 2)] ,

n∑

k=0
 [( n + k
n − k
 ) ( n
k
 ) (mod 2)] ,

n∑

k=0
 [( n + 2k
2n − k
 ) ( n
k
 ) (mod 2)] ,

and n∑

k=0
 [( n − k
6k
 ) ( n
k
 ) (mod 2)]

are the run length transform of the Fibonacci numbers, the positive integers, the
extended Lucas numbers and Narayana’s cows sequence, respectively.

It is clear that a(n) is upper bounded by a(n) ≤ ∑n
k=0
 [( n
k
 ) (mod 2)] with

equality when a1 = a4 = 1, a2 = a3 = 0 or when a1 = a2 = a3 = a4 =

1. The sequence α(n) = ∑n
k=0
 [( n
k
 ) (mod 2)] is known as Gould’s sequence

or Dress’ sequence and is the run length transform of the positive powers of 2:
1, 2, 4, 8, 16, 32, . . . (see OEIS [9] sequence A001316).

Lemma 2. The sequence a(n) satisﬁes the following properties:

• a(0) = 1,

3Again, a(n) depends on the integers ai whose values are deduced from the context.

INTEGERS: 22 (2022) 6

• a(2rn) = a(n) for r > 0,

• Suppose a3 ∈ {0, 1}. If a1 = 1 or a3 = 0, then a(4n+1) = a(n)+∑n
k=0 F (4n+
1, 4k + 1), a(4n + 3) = a(n) + ∑3
m=1 ∑n
k=0 F (4n + 3, 4k + m), and a(2n + 1) =
a(n) + ∑n
k=0 F (2n + 1, 2k + 1),

• If a3 ∧ ¬a1 ̸≡ 0 (mod 4), then a(4n + 1) = ∑n
k=0 F (4n + 1, 4k + 1),

• If 3a3 ∧ ¬3a1 ̸≡ 0 (mod 4), then a(4n + 3) = ∑3
m=1 ∑n
k=0 F (4n + 3, 4k + m),

• If a3 ∧ ¬a1 ̸≡ 0 (mod 2), then a(2n + 1) = ∑n
k=0 F (2n + 1, 2k + 1).

Proof. First, note that a(0) is trivially equal to 1. Next, a(2n) = ∑2n
k=0 F (2n, k) =
∑n
k=0 F (2n, 2k) + ∑n−1
k=0 F (2n, 2k + 1) which is equal to a(n) by Theorem 5.
Suppose a3 ∈ {0, 1} and a1 = 1 or a3 = 0. By Theorem 5, several of the
terms F (n, k) vanish or can be rewritten and the following relations hold. Firstly,
a(4n + 1) = ∑3
m=0 ∑n
k=0 F (4n + 1, 4k + m) − F (4n + 1, 4n + 2) − F (4n + 1, 4n + 3) =
∑3
m=0 ∑n
k=0 F (4n + 1, 4k + m) = ∑n
k=0 F (n, k) + ∑n
k=0 F (4n + 1, 4k + 1).
Secondly, a(4n + 3) = ∑3
m=0 ∑n
k=0 F (4n + 3, 4k + m) which is equal to

n∑

k=0 F (n, k) +
 3∑

m=1
 n∑

k=0 F (4n + 3, 4k + m).

Next, a(2n + 1) = ∑2n+1
k=0 F (2n + 1, k) = ∑n
k=0 F (2n + 1, 2k) + ∑n
k=0 F (2n +
1, 2k +1) = ∑n
k=0 F (n, k)+∑n
k=0 F (2n+1, 2k +1). The other cases follow similarly
from Theorem 5.

In particular, if a1 = 1 or a3 = 0 then ∑n
k=0 F (2n + 1, 2k + 1) = a(2n + 1) − a(n),
an equation that we will often use in what follows.

4.1. Run Length Transform of the Fibonacci Sequence

Consider the case a1 = 1, a2 = −1, a3 = 0, a4 = 2.

Lemma 3. For a1 = 1, a2 = −1, a3 = 0, a4 = 2, the following relations hold for
the function F :

• F (4n + 1, 4k + 1) = F (4n + 3, 4k + 3) = 0,

• F (4n + 3, 4k + 1) = F (n, k),

• F (4n + 3, 4k + 2) = F (2n + 1, 2k + 1).

Proof. First, g(4n + 1, 4k + 1) = (8k + 2 ∧ ¬(4(n − k))) ∨ (4k + 1 ∧ ¬4n + 1) ̸= 0,
i.e F (4n + 1, 4k + 1) = 0.

INTEGERS: 22 (2022) 7

Next, g(4n + 3, 4k + 1) = (8k + 2 ∧ ¬(4(n − k) + 2)) ∨ (4k + 1 ∧ ¬4n + 3) =
(4(2k ∨ n − k)) ∨ 4(k ∧ ¬n) = 4g(n, k), i.e., F (4n + 3, 4k + 1) = F (n, k).
Note that (4k + 2 ∧ ¬4n + 3) = (4k ∧ ¬4n) = 2(2k ∧ ¬2n) and (2k + 1 ∧ ¬2n + 1) =
(2k ∧ ¬2n). Similarly, (4k + 3 ∧ ¬4n + 3) = (4k ∧ ¬4n) = 2(2k + 1 ∧ ¬2n + 1).
Furthermore, g(4n + 3, 4k + 2) = (8k + 4 ∧ ¬(4(n − k) + 1)) ∨ (4k + 2 ∧ ¬4n + 3) =
2((4k + 2 ∧ ¬2(n − k)) ∨ (2k + 1 ∧ ¬2n + 1)) = 2g(2n + 1, 2k + 1) where we have
used the fact that (8k + 4 ∧ ¬(4(n − k) + 1)) = (8k + 4 ∧ ¬(4(n − k))). This implies
that F (4n + 3, 4k + 2) = F (2n + 1, 2k + 1).
Finally, g(4n + 3, 4k + 3) = (8k + 6 ∧ ¬(4(n − k))) ∨ (4k + 3 ∧ ¬4n + 3). Since
8k + 6 ∧ ¬4(n − k) ̸= 0, this implies that F (4n + 3, 4k + 3) = 0.

Theorem 6. Let a(n) = ∑n
k=0
 [( n − k
2k
 ) ( n
k
 ) (mod 2)]
. Then a(n) satisﬁes

the equations a(0) = 1, a(2n) = a(n), a(4n + 1) = a(n) and a(4n + 3) = a(2n +
1) + a(n). In particular, a(n) is the run length transform of the Fibonacci sequence
1, 1, 2, 3, 5, 8, 13, . . . .

Proof. By Lemma 2, a(0) = 1 and a(2n) = a(n). Next, by Lemma 2 and Lemma
3, we obtain a(4n + 1) = a(n). Similarly, a(4n + 3) = a(n) + ∑3
m=1 ∑n
k=0 F (4n +
3, 4k+m) = a(n)+∑n
k=0 F (n, k)+F (2n+1, 2k+1) = a(2n+1)+a(n). By Theorem
4, a(n) is the run length transform of the Fibonacci sequence 1,1,2,3,5,8,13,...

Note that in this case a(n) corresponds to OEIS sequence A246028. Other values
of ai can also generate the same sequence. For instance, it can be shown that the
values of n∑

k=0
 [( 2k
n − k
 ) ( n
k
 ) (mod 2)] ,

n∑

k=0
 [( n + 3k
2k
 ) ( n
k
 ) (mod 2)] ,

and of n∑

k=0
 [( n + 3k
n + k
 ) ( n
k
 ) (mod 2)]

all correspond to the run length transform of the Fibonacci sequence as well.
In what follows, the proofs and derivations of the run length transforms and the
intermediate lemmas are similar to the proofs of the above results and are omitted
for brevity. Interested readers are referred to [13] for full details.

4.2. Run Length Transform of the Truncated Fibonacci Sequence

Next, consider the case a1 = a3 = 0, a2 = 3, a4 = 1.

INTEGERS: 22 (2022) 8

Lemma 4. For a1 = a3 = 0, a2 = 3, a4 = 1, the following relations hold for the
function F :

• F (4n + 1, 4k + 1) = F (4n + 3, 4k + 1) = F (n, k),

• F (4n + 3, 4k + 2) = F (2n + 1, 2k + 1),

• F (4n + 3, 4k + 3) = 0.

Theorem 7. Let a(n) = ∑n
k=0
 [( 3k
k
 ) ( n
k
 ) (mod 2)]
. Then a(n) satisﬁes the

equations a(0) = 1, a(2n) = a(n), a(4n+1) = 2a(n) and a(4n+3) = a(2n+1)+a(n).
In particular, a(n) is the run length transform of the truncated Fibonacci sequence
1, 2, 3, 5, 8, 13, . . . .

Note that in this case a(n) corresponds to OEIS sequence A245564. This sequence
is also equal to n∑

k=0
 [( 3k2
m

k2
m
 ) ( n
k
 ) (mod 2)]

and n∑

k=0
 [( 3k2
m

2k2
m
 ) ( n
k
 ) (mod 2)]

for all integers m ≥ 0.

4.3. Run Length Transform of {1, 1, 2, 4, 8, 16, 32, . . . }

Consider the case a1 = 1, a2 = a3 = 0, a4 = 2.

Lemma 5. For a1 = 1, a2 = a3 = 0, a4 = 2, the following relations hold for the
function F :

• F (4n + 1, 4k + 1) = 0,

• F (4n + 3, 4k + 1) = F (n, k),

• F (4n + 3, 4k + 2) = F (4n + 3, 4k + 3) = F (2n + 1, 2k + 1).

Theorem 8. Let a(n) = ∑n
k=0
 [( n
2k
 ) ( n
k
 ) (mod 2)]
. Then a(n) satisﬁes the

equations a(0) = 1, a(2n) = a(n), a(4n + 1) = a(n) and a(4n + 3) = 2a(2n + 1).
In particular, a(n) = {1, 1, 1, 2, 1, 1, 2, 4, 1, 1, 1, 2, . . . } is the run length transform of
the sequence 1, 1, 2, 4, 8, 16, 32, . . . , i.e., 1 plus the positive powers of 2.

INTEGERS: 22 (2022) 9

4.4. Run Length Transform of {1, 2, 2, 2, 2, 2, . . . }

Consider the case a1 = 1, a2 = a4 = 2, a3 = 0.

Lemma 6. For a1 = 1, a2 = a4 = 2, a3 = 0, the following relations hold for the
function F :

• F (4n + 1, 4k + 1) = F (n, k),

• F (4n + 3, 4k + 1) = F (4n + 3, 4k + 3) = 0,

• F (4n + 3, 4k + 2) = F (2n + 1, 2k + 1).

Theorem 9. Let a(n) = ∑n
k=0
 [( n + 2k
2k
 ) ( n
k
 ) (mod 2)]
. Then a(n) satisﬁes

the equations a(0) = 1, a(2n) = a(n), a(4n + 1) = 2a(n) and a(4n + 3) = a(2n + 1).
In particular, a(n) = {1, 2, 2, 2, 2, 4, 2, 2, 2, 4, . . . } is the run length transform of the
sequence 1, 2, 2, 2, 2, 2, 2, . . . (OEIS A040000).

This sequence is also generated by ∑n
k=0
 [( n + 2k
n
 ) ( n
k
 ) (mod 2)]
.

4.5. Run Length Transform of the Positive Integers

OEIS sequence A106737 is deﬁned as a(n) = ∑n
k=0
 [( n + k
n − k
 ) ( n
k
 ) (mod 2)]
.

It was noted that the following recursive relationships appear to hold: a(2n) = a(n),
a(4n + 1) = 2a(n) and a(4n + 3) = 2a(2n + 1) − a(n). In this section we show that
this is indeed the case.

Let a1, a2, a3 = 1 and a4 = −1, i.e., F (n, k) = ( n + k
n − k
 ) ( n
k
 ) (mod 2) and

g(n, k) = ((n − k) ∧ ¬(n + k)) ∨ (k ∧ ¬n).

Lemma 7. For a1, a2, a3 = 1 and a4 = −1, the following relations hold for the
function F :

• F (4n + 1, 4k + 1) = F (n, k),

• F (4n + 3, 4k + 1) = 0,

• F (4n + 3, 4k + 2) = F (4n + 3, 4k + 3) = F (2n + 1, 2k + 1).

Theorem 10. For OEIS sequence A106737, a(0) = 1, a(2n) = a(n), a(4n + 1) =
2a(n) and a(4n + 3) = 2a(2n + 1) − a(n). Furthermore, a(n) is the run length
transform of the positive integers.

This sequence is also generated by each of the following expressions:
∑n
k=0
 [( n + k
2k
 ) ( n
k
 ) (mod 2)]
, ∑n
k=0
 [( n + 2k
k
 ) ( n
k
 ) (mod 2)] and

∑n
k=0
 [( n + 2k
n + k
 ) ( n
k
 ) (mod 2)]
.

INTEGERS: 22 (2022) 10

4.6. A Fixed Point of the Run Length Transform

The all ones sequence 1, 1, 1, . . . (OEIS sequence A000012) is a ﬁxed point of the
run length transform. We next show that it is also expressible as sums of products
of binomial coeﬃcients mod 2. To prove this, we look at the case a1 = a4 = 1,
a2 = −1, a3 = 0.

Lemma 8. For a1 = a4 = 1, a2 = −1, a3 = 0, the following relations hold for the
function F :

F (4n + 1, 4k + 1) = F (4n + 3, 4k + 1) = F (4n + 3, 4k + 2) = F (4n + 3, 4k + 3) = 0.

Theorem 11. For n, k ≥ 0, ( n − k
k
 ) ( n
k
 ) is odd if and only if k = 0, i.e.,

n∑

k=0
 [( n − k
k
 ) ( n
k
 ) (mod 2)] = 1

for all n.

Theorem 11 can also be interpreted via Sierpi´nski’s triangle generated by Pascal’s
triangle mod 2 and by looking at it as follows: if starting from the left edge of the
triangle and moving k steps to the right reaches a point of Sierpi´nski’s triangle, then
continuing moving diagonally k steps must necessarily reach a void of Sierpi´nski’s
triangle.

5. Third Order Recurrences

Deﬁnition 3. Let n be an odd positive integer not of the form 2
k − 1. The splitting
function µ(n) = (a, b, m) returns positive integers a, b, m such that a2
m + b = n
with 2m > 2b, and a is the smallest such number satisfying this.

A way to describe the numbers a and b in Deﬁnition 3 is that they are obtained
by splitting the binary expansion of n along the ﬁrst occurrence of 0. For instance
since 413 = 1100111012, which can be split into ‘11’ and ‘011101’, which is 3 and
29, thus µ(413) = (3, 29, 7). Note that n > 3b.
Theorem 4 shows that if a sequence satisﬁes a second order recurrence, then we
can easily determine the recurrence relations that the run length transform satisﬁes.
This result can be generalized to n-th order recurrences as follows.

Theorem 12. Let {Sn}n≥0 be deﬁned by the (k + 1)-th order recurrence Sn+1 =
∑k
i=0 diSn−i with initial conditions Si = ci for i = 0, 1, . . . , k. Then the run length
transform of {Sn} is given by {Tn}n≥0 satisfying

INTEGERS: 22 (2022) 11

• w = 2
k+1,

• T0 = c0,

• T2n = Tn,

• Twn+i = TiTn, for i = 1, 3, 5, . . . , 2k − 1,

• Twn+2k+i = TbiT wn
2mi +ai for i = 1, 3, 5, . . . , 2
k −3 where µ(2k +i) = (ai, bi, mi),

• Twn+w−1 = ∑k
i=0 diT2k−in+2k−i−1.

Proof. The proof is similar to the proof of Theorem 4 (see [7] for a proof of Theorem
4) and is omitted.

Even though the right hand side in some of the recurrence relations above is a
product of 2 terms of {Tn}, one of the terms is determined solely by the initial
conditions ci’s. More speciﬁcally, note that for i = 1, 3, 5, . . . , 2
k − 1, Ti is a product
of Sj’s where j ≤ k and thus is a product of some cj’s. Similarly, for i ≤ 2
k − 3, we
have 2k+1 − 3 > 2
k + i > 3bi and therefore bi < 2k. Thus Tbi is also the product of
some cj’s. In particular, Theorem 12 for the case k = 1 corresponds to Theorem 4.
For k = 2, we have the following result on third order recurrences.

Corollary 1. Let {Sn}n≥0 be deﬁned by the recurrence Sn+1 = d0Sn + d1Sn−1 +
d2Sn−2 with initial conditions S0 = c0, S1 = c1, S2 = c2. Then the run length
transform of {Sn} is given by {Tn}n≥0 satisfying

• T0 = c0,

• T2n = Tn,

• T8n+1 = c1Tn,

• T8n+3 = c2Tn,

• T8n+5 = c1T2n+1, and

• T8n+7 = d0T4n+3 + d1T2n+1 + d2Tn.

Theorem 13. The following relations hold for the function F as deﬁned in Deﬁ-
nition 2:

• F (8n, 8k + i) = 0 for i = 1, . . . , 7,

• F (8n + 1, 8k + i) = 0 for i = 2, . . . , 7,

• F (8n + 3, 8k + i) = 0 for i = 4, 5, 6, 7,

• F (8n + 5, 8k + i) = 0 for i = 2, 3, 6, 7,

• If a3 ∧ ¬a1 ≡ 0 (mod 8) and 0 ≤ a1, a3 < 8, then F (8n + 1, 8k) = F (n, k),

INTEGERS: 22 (2022) 12

• If a3 ∧ ¬a1 ̸≡ 0 (mod 8), then F (8n + 1, 8k) = 0,

• If 3a3 ∧ ¬3a1 ≡ 0 (mod 8) and 0 ≤ 3a1, 3a3 < 8, then F (8n + 3, 8k) = F (n, k),

• If 3a3 ∧ ¬3a1 ̸≡ 0 (mod 8), then F (8n + 3, 8k) = 0,

• If 5a3 ∧ ¬5a1 ≡ 0 (mod 8) and 0 ≤ 5a1, 5a3 < 8, then F (8n + 5, 8k) = F (n, k),

• If 5a3 ∧ ¬5a1 ̸≡ 0 (mod 8), then F (8n + 5, 8k) = 0.

Lemma 9. The sequence a(n) satisﬁes the following properties:

• If a3 ∧ ¬a1 ≡ 0 (mod 8) and 0 ≤ a1, a3 < 8, then a(8n + 1) = a(n) +
∑n
k=0 F (8n + 1, 8k + 1),

• If 3a3 ∧ ¬3a1 ≡ 0 (mod 8) and 0 ≤ 3a1, 3a3 < 8, then a(8n + 3) = a(n) +
∑3
m=1 ∑n
k=0 F (8n + 3, 8k + m),

• If 5a3 ∧ ¬5a1 ≡ 0 (mod 8) and 0 ≤ 5a1, 5a3 < 8, then a(8n + 5) = a(n) +
∑

m∈{1,4,5} ∑n
k=0 F (8n + 5, 8k + m),

• If a3 ∧ ¬a1 ̸≡ 0 (mod 8), then a(8n + 1) = ∑n
k=0 F (8n + 1, 8k + 1),

• If 3a3 ∧ ¬3a1 ̸≡ 0 (mod 8), then a(8n + 3) = ∑3
m=1 ∑n
k=0 F (8n + 3, 8k + m),

• If 5a3∧¬5a1 ̸≡ 0 (mod 8), then a(8n+5) = ∑
m∈{1,4,5} ∑n
k=0 F (8n+5, 8k+m).

5.1. Run Length Transform of Narayana’s Cows Sequence

Narayana’s cows sequence (OEIS A000930) {bn : n ≥ 0} is deﬁned as b0 = b1 =
b2 = 1, bn = bn−1 + bn−3. The ﬁrst few terms are: 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28,
41, 60, 88, 129, 189, 277, 406, 595, . . . The following results show that

a(n) =
 n∑

k=0
 [( n − k
6k
 ) ( n
k
 ) (mod 2)]

is the run length transform of Narayana’s cows sequence.

Lemma 10. For a1 = 1, a2 = −1, a3 = 0, a4 = 6, the following relations hold for
the function F :

• F (8n + 1, 8k + 1) = 0,

• F (8n + 3, 8k + i) = 0 for 1 ≤ i ≤ 3,

• F (8n + 5, 8k + 1) = F (8n + 5, 8k + 5) = 0,

• F (8n + 5, 8k + 4) = F (2n + 1, 2k + 1),

• F (8n + 7, 8k + i) = 0 for i ∈ {3, 5, 6, 7},

INTEGERS: 22 (2022) 13

• F (8n + 7, 8k) = F (8n + 7, 8k + 1) = F (n, k),

• F (8n + 7, 8k + 2) = F (4n + 3, 4k + 1),

• F (8n + 7, 8k + 4) = F (4n + 3, 4k + 2),

• F (4n + 3, 4k + 3) = 0.

Theorem 14. Let a(n) = ∑n
k=0
 [( n − k
6k
 ) ( n
k
 ) (mod 2)]
. Then a(n) satisﬁes

the equations a(0) = 1, a(2n) = a(n), a(8n + 1) = a(8n + 3) = a(n), a(8n + 5) =
a(2n + 1), and a(8n + 7) = a(n) + a(4n + 3). In particular, the sequence

a(n) = {1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, . . . }

is the run length transform of Narayana’s cows sequence.

Proof. This is a consequence of Lemma 2, Corollary 1, Lemma 9, and Lemma 10.
Note that by Lemma 10, a(8n + 5) = a(n) + ∑n
k=0 F (2n + 1, 2k + 1) which is equal
to a(2n + 1) by Lemma 2. Similarly, a(8n + 7) = 2a(n) + ∑n
k=0 F (4n + 3, 4k + 1) +
F (4n + 3, 4k + 2) which is equal to a(n) + a(4n + 3).

5.2. Run Length Transform of 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, . . .

The following result shows that a(n) = ∑n
k=0
 [( n + 3k
6k
 ) ( n
k
 ) (mod 2)] is

equal to the run length transform of the sequence 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, . . . (OEIS
A008619).

Theorem 15. Let a(n) = ∑n
k=0
 [( n + 3k
6k
 ) ( n
k
 ) (mod 2)]
. Then a(n) satis-

ﬁes the equations a(0) = 1, a(2n) = a(n), a(8n + 1) = a(n), a(8n + 3) = 2a(n),
a(8n + 5) = a(2n + 1), and a(8n + 7) = a(4n + 3) + a(2n + 1) − a(n). In particular,
the sequence

a(n) = {1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 3, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 4, 2, 2, . . . }

is the run length transform of the sequence 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, . . . .

6. Fourth Order Recurrences

We ﬁrst start with the following Corollary to Theorem 4 for k = 3.

Corollary 2. Let {Sn}n≥0 be deﬁned by the recurrence Sn+1 = d0Sn + d1Sn−1 +
d2Sn−2 + d3Sn−3 with initial conditions S0 = c0, S1 = c1, S2 = c2, and S3 = c3.
Then the run length transform of {Sn} is given by {Tn}n≥0 satisfying

INTEGERS: 22 (2022) 14

• T0 = c0,

• T2n = Tn,

• T16n+1 = c1Tn,

• T16n+3 = c2Tn,

• T16n+5 = c2
1Tn,

• T16n+7 = c3Tn,

• T16n+9 = c1T2n+1,

• T16n+11 = c2T2n+1,

• T16n+13 = c1T4n+3,

• T16n+15 = d0T8n+7 + d1T4n+3 + d2T2n+1 + d3Tn.

Theorem 16. The following relations hold for the function F as deﬁned in Deﬁ-
nition 2:

• F (16n, 16k + i) = 0 for i = 1, . . . , 15,

• F (16n + 1, 16k + i) = 0 for i = 2, . . . , 15,

• F (16n + 3, 16k + i) = 0 for i = 4, . . . , 15,

• F (16n + 5, 16k + i) = 0 for i = 2, 3, 6, 7, 8, . . . , 15,

• F (16n + 7, 16k + i) = 0 for i = 8, . . . , 15,

• F (16n + 9, 16k + i) = 0 for i = 2, . . . , 7 and i = 10, . . . , 15,

• F (16n + 11, 16k + i) = 0 for i = 4, 5, 6, 7, 12, 13, 14, 15,

• F (16n + 13, 16k + i) = 0 for i = 2, 3, 6, 7, 10, 11, 14, 15,

• If ia3 ∧ ¬ia1 ≡ 0 (mod 16) and 0 ≤ ia1, ia3 < 16, then F (16n + i, 16k) =
F (n, k) for i ∈ {1, 3, 5, 7, 9, 11, 13},

• If ia3∧¬ia1 ̸≡ 0 (mod 16), then F (16n+i, 16k) = 0, for i ∈ {1, 3, 5, 7, 9, 11, 13}.

6.1. Run Length Transform of 1, 1, 2, 1, 3, 4, 7, 11, 18, . . .

Consider the sequence 1,1,2,1,3,4,7,11,18,. . . which is equal to the coeﬃcients in the
expansion of 1−2x3
1−x−x2 . This sequence (OEIS A329723) is also equal to the sequence
formed by prepending the Lucas numbers (OEIS A000032) with the terms 1, 1. The

following result shows that a(n) = ∑n
k=0
 [( n + 2k
2n − k
 ) ( n
k
 ) (mod 2)] is equal to

the run length transform of this sequence.

INTEGERS: 22 (2022) 15

Theorem 17. Let a(n) = ∑n
k=0
 [( n + 2k
2n − k
 ) ( n
k
 ) (mod 2)]
. Then a(n) satis-

ﬁes the equations a(0) = 1, a(2n) = a(n), a(16n + 1) = a(n), a(16n + 3) = 2a(n),
a(16n + 5) = a(n), and a(16n + 7) = a(n). Furthermore, a(16n + 9) = 2a(2n + 1),
a(16n + 11) = 2a(2n + 1), and a(16n + 13) = a(4n + 3). Finally a(16n + 15) =
a(8n + 7) + a(4n + 3). This implies that the sequence

a(n) = {1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 3, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 4, 1, 1, . . . }

is the run length transform of the extended Lucas sequence 1, 1, 2, 1, 3, 4, 7, 11, 18, . . . .

The sequences considered in the above sections and their run length transforms
are summarized in Table 1. In the table, the coeﬃcients ai describe the run length

transform expressed as ∑n
k=0
 [( a1n + a2k
a3n + a4k
 ) ( n
k
 ) (mod 2)]
.

Sequence
description OEIS
index Sequence terms
 Coeﬃcients
(a1, a2, a3, a4)
of Run
Length
Transform
 OEIS
index
of Run
Length
Trans-
form

Positive powers of 2 A000079 1, 2, 4, 8, . . . (1, 0, 0, 1) A001316
Fibonacci sequence A000045 1, 1, 2, 3, 5, 8, . . . (1, −1, 0, 2) A246028
Truncated Fibonacci
sequence 1, 2, 3, 5, 8, 13, . . . (0, 3, 0, 1) A245564
1 plus the positive
powers of 2 A011782 1, 1, 2, 4, 8, 16, . . . (1, 0, 0, 2) A245195
1 followed by 2’s A040000 1, 2, 2, 2, 2, 2, . . . (1, 2, 0, 2) A277561
Positive integers A000027 1, 2, 3, 4, 5, 6, . . . (1, 1, 1, −1) A106737
A sequence of 1’s A000012 1, 1, 1, 1, 1, 1, . . . (1, −1, 0, 1) A000012
Narayana’s cows
sequence A000930 1, 1, 1, 2, 3, 4, 6, 9, . . . (1, −1, 0, 6) A329720
Positive integers
repeated A008619 1, 1, 2, 2, 3, 3, 4, 4, . . . (1, 3, 0, 6) A278161
Lucas sequence
prepended with 1,1 A329723 1, 1, 2, 1, 3, 4, 7, 11, . . . (1, 2, 2, −1) A329722

Table 1: Table of various sequences and their run length transforms expressed as
sums of products of binomial coeﬃcients mod 2.

References

[1] R. P. Brent and P. Zimmermann, Modern Computer Arithmetic, Cambridge Univ. Press, New
York, 2010.

INTEGERS: 22 (2022) 16

[2] N. Fine, Binomial coeﬃcients modulo a prime, Amer. Math. Monthly 54 (1947), 589-592.

[3] A. Granville, Arithmetic properties of binomial coeﬃcients I: Binomial coeﬃcients modulo
prime powers, in Canad. Math. Soc. Conf. Proc., 20 (1997), 253-275.

[4] J. Leroy, M. Rigo, and M. Stipulanti, Generalized Pascal triangle for binomial coeﬃcients of
words, Adv. Appl. Math. 80 (2016), 24-47.

[5] P. Mathonet, M. Rigo, M. Stipulanti, and N. Z´ena¨ıdi, On digital sequences associated with
Pascal’s triangle, arXiv.2201.06636 (2022).

[6] D. A. Patterson and J. L. Hennessy, Computer Organization and Design - The Hardware /
Software Interface (Revised 4th Edition), The Morgan Kaufmann Series in Computer Archi-
tecture and Design, Academic Press, Cambridge, 2012.

[7] N. J. A. Sloane, On the number of ON cells in cellular automata, in S. Butler, J. Cooper,
and G. Hurlbert, editors, Connections in Discrete Mathematics: A Celebration of the Work
of Ron Graham, Cambridge Univ. Press, Cambridge, 2018, 13-38.

[8] I. Stewart, Four encounters with Sierpi´nski’s gasket, Math. Intelligencer 17 (1995), 52-64.

[9] The OEIS Foundation Inc., The on-line encyclopedia of integer sequences, 1996-present, URL
https://oeis.org/, founded in 1964 by N. J. A. Sloane.

[10] E. W. Weisstein, Sierpi´nski sieve. From MathWorld–A Wolfram Web Resource, URL http:
//mathworld.wolfram.com/SierpinskiSieve.html, [Online; accessed 21-April-2022].

[11] Wikipedia contributors, Bitwise operation — Wikipedia, the free encyclopedia, 2022, URL
https://en.wikipedia.org/wiki/Bitwise_operation, [Online; accessed 21-April-2022].

[12] Wikipedia contributors, Two’s complement — Wikipedia, the free encyclopedia, 2022, URL
https://en.wikipedia.org/wiki/Two’s_complement, [Online; accessed 10-July-2022].

[13] C. W. Wu, Sums of products of binomial coeﬃcients mod 2 and run length transforms of
sequences, arXiv:1610.06166 (2016-2022).
