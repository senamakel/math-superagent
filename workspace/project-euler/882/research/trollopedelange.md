> **Excerpt only — read this first.** The complete text is beside it at `research/trollopedelange.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, and specific enough that nobody needs the full text.

<!-- source: https://emis.muni.cz/journals/INTEGERS/papers/l54/l54.pdf | converted from PDF -->

#A54 INTEGERS 11 (2011)

DIGITAL SUMS AND FUNCTIONAL EQUATIONS

Roland Girgensohn
1

Zentrum Mathematik, Technische Universit¨at M¨unchen, Germany

Received: 8/30/10, Revised: 6/14/11, Accepted: 8/22/11, Published: 9/19/11

Abstract
Let S(n) denote the total number of digits ‘1’ in the binary expansions of the integers
between 1 and n − 1. The Trollope-Delange formula is a classical result which
provides an explicit representation for S(n) in terms of the continuous, nowhere
diﬀerentiable Takagi function. Recently, connections have been established between
digital sums such as S(n) and certain functional equations associated with the
Takagi function and its relatives. In the present paper we explore such a connection
to derive a new, simple proof for the Trollope-Delange formula as well as for some
of its generalizations involving power and exponential sums.

1. Introduction

Let S(n) denote the total number of digits ‘1’ in the binary expansions of the
integers between 1 and n − 1. Since that is roughly half the number of all of those
digits, it is not far-fetched that S(n) must be of the order S(n) = 1
2 n log2 n +
O(n). Interestingly, it turns out that the capital-O term in this expansion can be
given explicitly as n times a continuous, 1-periodic function of log2 n. This was
ﬁrst proved by J.R. Trollope in [19]; subsequently, in [4], H. Delange gave a very
short and direct proof of this representation. The continuous function appearing in
their representation is a slight modiﬁcation of the well-known continuous, nowhere
diﬀerentiable Takagi function, investigated by T. Takagi already in 1903 [18] and
often presented as one of the simplest examples of a nowhere diﬀerentiable function.
The Trollope-Delange formula has been investigated and generalized intensively
in the intervening years. Bases other than 2 have been examined, the occurrence
of subblocks other than the digit ‘1’ has been counted, and other modiﬁcations
have been applied to these quantities. Always it turned out that a representation of
Trollope-Delange type of the quantity in question could be given, often with explicit
continuous functions. Some references to such work are given below.

1Postal address: Kepserstr. 5, 85356 Freising, Germany

INTEGERS: 11 (2011) 2

The purpose of the present note is to give a new and simple proof of the Trollope-
Delange formula and then to turn this proof into a method by applying it to some
other variations and generalizations of these sums. The method proceeds by extract-
ing functional equations from the digital sum sequences such as S(n), identifying
their solutions and then using this process to prove a formula of Trollope-Delange
type in just a few lines.
To ﬁx notation, let
 j = ∑

i≥0 ai(j) 2
i with ai(j) ∈ {0, 1} (1)

be the binary expansion of j ∈ N0, let

s(j) = ∑

i≥0 ai(j) (2)

be the number of digits ‘1’ in the binary expansion of j, and let

S(n) =
 n−1∑

j=0 s(j), (3)

S(n; t) =
 n−1∑

j=0 exp(t · s(j)) for t ∈ R and (4)

Sk(n) =
 n−1∑

j=0 s(j)
k for k ∈ N (5)

denote the digital sum in question as well as its so-called exponential and power
sums. Then the Trollope-Delange formula for S(n) is

1
n S(n) = 1
2 log2 n + 1
2 ̃F (log2 n) (6)

where the 1-periodic function ̃F is given by

̃F (u) = 1 − u − 2
1−u T ( 1
21−u
 ) for 0 ≤ u ≤ 1. (7)

Here, T is the Takagi function

T (x) =
 ∞∑

n=0
 1
2n d(2
nx) with d(x) = dist(x, Z) and x ∈ R. (8)

While this is the “direct” deﬁnition of the Takagi function, T can just as well be
deﬁned “indirectly” on [0, 1] as the only continuous solution of the system of two
functional equations

f ( x
2
 ) = 1
2 f (x) + x
2 , f ( x + 1
2
 ) = 1
2 f (x) + 1 − x
2 for x ∈ [0, 1]. (9)

INTEGERS: 11 (2011) 3

The system (9) is a speciﬁc example of the type of functional equations which, as
mentioned above, appear in the digital sum sequences and can therefore be used to

*[excerpt ends; 29412 characters not shown — see `research/trollopedelange.full.md`]*
