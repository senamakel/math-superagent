<!-- source: https://arxiv.org/pdf/1506.06621v2 | converted from PDF -->

arXiv:1506.06621v2  [math.GM]  26 Jun 2015
On the 3 × 3 magic square constructed with nine distinct
square numbers

Jailton C. Ferreira

Abstract

A proof that there is no 3 × 3 magic square constructed with nine distinct square
numbers is given.

1 Introduction

In 1984 Martin Labar [1] formulated the problem: Can a 3 × 3 magic square be constructed
with nine distinct square numbers? The problem is found in the second edition of Guy’s Unsolved
Problems in Number Theory [2] and became famous when Martin Gardner republished it in 1996
[3].

2 The proof
 a b c

d ε f

g h i

Figure 1

Let be the square given in Figure 1 such that a, b, c, d, ε, f, g, h, i ∈ N and

a + b + c = x (1)

d + ε + f = x (2)

g + h + i = x (3)

a + d + g = x (4)

b + ε + h = x (5)

c + f + i = x (6)

a + ε + i = x (7)

c + ε + g = x (8)

The equations (1), (2), (3), (5), (6) (4), (7) and (8) can be rewritten as

a = x − b − c (9)

d = x − ε − f (10)

1

g = x − ε − i (11)

b = x − ε − h (12)

c = x − f − i (13)

a + d + g − x = 0 (14)

a + ε + i − x = 0 (15)

c + ε + g − x = 0 (16)

Substituting sequentially a, d, g, b and c given by (10) to (13) into the equations (14) to (16) we
obtain, respectively,
 0 = 0 (17)

2ε + f + h + 2i − 2x = 0 (18)

ε − f − h − 2i + x = 0 (19)

Summing (18) and (19) we ﬁnd ε = x
3 (20)

The set of equations (1) to (8) can be put in the form

a = ε + ∆1 (21)

b = ε − (∆1 + ∆2) (22)

c = ε + ∆2 (23)

d = ε − (∆1 − ∆2) (24)

f = ε + (∆1 − ∆2) (25)

g = ε − ∆2 (26)

h = ε + (∆1 + ∆2) (27)

i = ε − ∆1 (28)

Let us notice that ∆1 ̸= 0, ∆2 ̸= 0 and ∆1 ̸= ∆2 to obtain the magic square constructed with nine
distinct square numbers.
Let us consider that ηn = (n + 1)
2 − n2 (29)

ηn+1 = ηn + 2 (30)

where n ∈ N and n > 0. The Figure 2 was obtained using the equations (29) and (30).

❙
❙ ❙
❙ ❙
❙ ❙
❙ ❙
❙
✓
✓ ✓
✓ ✓
✓ ✓
✓ ✓
✓

12 22 32 42 52 62 ...

1 4 9 16 25 36 ...

3 5 7 9 11 ... Figure 2

2

Let us assume that there exist 0 < m < e and e < n such that

n2 + m2 = 2e2 (31)

The values of n2 and m2 are
 n2 = e2 +
 n−1∑

k=e ηk (32)

and
 m2 = e2 −
 e−1∑

k=m ηk (33)

or n2 = e2 + ηe + ηn−1
2 ((n − 1) − (e − 1)) (34)

and m2 = e2 − ηm + ηe−1
2 ((e − 1) − (m − 1)) (35)

Considering a = n2, i = m2 and ε = e2 we have

ηe + ηn−1
2 ((n − 1) − (e − 1)) − ηm + ηe−1
2 ((e − 1) − (m − 1)) = 0 (36)

or
 (−e + n)(−2e2 + 2(1 + e)
2 + 2(−1 − e + n)) −
((−2 − 2e2 + 2(1 + e)
2 − 2(e − m))(e − m) = 0 (37)

Let us assume that there exist w and z such that

c = (n + w)
2 (38)

and g = (m − z)
2 (39)

where w and z are positive integers. In this case we have

(−e + n + w)(−2e2 + 2(1 + e)
2 + 2(−1 − e + n + w)) −

((−2 − 2e2 + 2(1 + e)
2 − 2(e − m + z))(e − m + z) = 0 (40)

Subtracting (37) from (40) we obtain

2nw + w2 + (−2m + z) = 0 (41)

Solving (41) for z we ﬁnd z1 = m + √
m2 − 2nw − w2 (42)

and z2 = m − √
m2 − 2nw − w2 (43)

The root z1 implies that m − z is not a positive integer, however m − z must be a positive integer.
Therefore z = z2.
We have assumed 2e2 = m2 + n2 (44)

and 2e2 = (m − z)
2 + (n + w)
2 (45)

Subtracting (44) from (45) we obtain

(m − z)
2 + (n + w)
2 − (m2 + n2) = 0 (46)

3

Substituting (43) into (46) we have

n2 − 2nw − w2 − (n + w)
2 = 0 (47)

Solving (47) for w we ﬁnd w1 = 0 (48)

and w2 = −2n (49)

The root w2 implies in n + w negative, however n + w must be a positive integer. Therefore w = 0.
Since that w = 0 the condition ∆1 ̸= ∆2 is not satisﬁed.There is no magic square constructed with
nine distinct square numbers.

References

[1] Martin Labar, Problem 270, College Math. J. 15, pp. 69, 1984.

[2] Richard Guy, Unsolved Problems in NumberTheory, 2nd edition, Springer-Verlag, New York,
Problem D15, pp. 170-171, 1994.

[3] Martin Gardner, The magic of 3 × 3, Quantum, pp. 24-26,1996.

4
