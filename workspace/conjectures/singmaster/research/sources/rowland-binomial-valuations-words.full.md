<!-- source: https://ericrowland.github.io/papers/Binomial_coefficients%2C_valuations%2C_and_words.pdf | converted from PDF -->

Binomial coeﬃcients, valuations, and words

Eric Rowland

Department of Mathematics
Hofstra University
Hempstead, NY 11549, USA
eric.rowland@hofstra.edu

Abstract. The study of arithmetic properties of binomial coeﬃcients
has a rich history. A recurring theme is that p-adic statistics reﬂect the
base-p representations of integers. We discuss many results expressing
the number of binomial coeﬃcients ( n
m) with a given p-adic valuation
in terms of the number of occurrences of a given word in the base-p
representation of n, beginning with a result of Glaisher from 1899, up
through recent results by Spiegelhofer–Wallner and Rowland.

Keywords: binomial coeﬃcients, p-adic valuation, regular sequences

1 Valuations of binomial coeﬃcients

In 1852, Kummer [10, pages 115–116] determined the exact power of a prime p
that divides a binomial coeﬃcient ( n
m). To state this result, let νp(n) denote the
p-adic valuation of n, that is, the exponent of the highest power of p dividing n.

Theorem 1 (Kummer). Let p be a prime, and let n and m be integers with
0 ≤ m ≤ n. Then νp(
( n
m)) is the number of carries involved in adding m to n−m
in base p.

Kummer’s theorem is the ﬁrst of many results to express arithmetic informa-
tion about binomial coeﬃcients in terms of base-p representations of integers.
Glaisher [6, §14] seems to have been the ﬁrst to count binomial coeﬃcients
satisfying a given congruence condition. He showed that the number of integers
m in the range 0 ≤ m ≤ n such that ( n
m
) is odd is 2
|n|1 . Here |n|1 is the number
of 1s in the standard base-2 representation of n.
Half a century later, Glaisher’s result was generalized to an arbitrary prime
by Fine [5, Theorem 2]. For a prime p and an integer n ≥ 0, let θp,0(n) be the
number of integers m in the range 0 ≤ m ≤ n such that ( n
m
) ̸≡ 0 mod p. Let
|n|w be the number of occurrences of the word w in the base-p representation of
n. Fine showed that
 θp,0(n) =
 p−1∏

d=0(d + 1)|n|d.

Since the publication of Fine’s result, many authors have been interested in
generalizations to higher powers of p. A natural quantity to study is the number
θp,α(n) of binomial coeﬃcients ( n
m), for 0 ≤ m ≤ n, with νp(( n
m)) = α.

2 E. Rowland

Carlitz [3, Equations (1.7)–(1.9)] gave a recurrence involving θp,α(n) and a
secondary quantity ψp,α(n) deﬁned as the number of integers m in the range
0 ≤ m ≤ n such that νp((m + 1)( n
m)) = α. Namely,

θp,α(pn + d) = (d + 1)θp,α(n) + (p − d − 1)ψp,α−1(n − 1)

ψp,α(pn + d) =
 {(d + 1)θp,α(n) + (p − d − 1)ψp,α−1(n − 1) if 0 ≤ d ≤ p − 2
pψp,α−1(n) if d = p − 1.

As we will see in Section 3, this recurrence comes close to giving a matrix gen-
eralization of Fine’s theorem, but it is not of the right form.
Nonetheless, Carlitz’s recurrence can be used to obtain formulas for θp,α(n).
Let nℓ · · · n1n0 be the standard base-p representation of n. For α = 1, Carlitz [3,
Equation (2.5)] showed

θp,1(n) =
 ℓ−1∑

i=0(nℓ +1)(nℓ−1 +1) · · · (ni+2 +1)ni+1(p−ni −1)(ni−1 +1) · · · (n0 +1).

Dividing by θp,0(n) = (nℓ + 1) · · · (n0 + 1) gives

θp,1(n)
θp,0(n) =
 ℓ−1∑

i=0
 ni+1
ni+1 + 1 · p − ni − 1
ni + 1 .

This equation is our ﬁrst indication that expressions for θp,α(n)
θp,0(n) can be simpler

than expressions for θp,α(n) alone. In particular, θp,1(n)
θp,0(n) is a polynomial in the
variables |n|w for words w ∈ {0, 1, . . . , p − 1}
∗ of length 2. For p = 2 we obtain

θ2,1(n) = 2|n|1 · 1
2 |n|10,

which was obtained by Howard [7, Equation (2.4)] and by Davis and Webb [4,
Theorem 7]. For p = 3 we have

θ3,1(n) = 2|n|13|n|2 (|n|10 + 1
4 |n|11 + 4
3 |n|20 + 1
3 |n|21
) ,

which also follows from the work of Huard, Spearman, and Williams [8]. For
p = 5 we have

θ5,1(n) = 2
|n|13
|n|2 4
|n|3 5
|n|4(2|n|10 + 3
4 |n|11 + 1
3 |n|12 + 1
8 |n|13

+ 8
3 |n|20 + |n|21 + 4
9 |n|22 + 1
6 |n|23

+ 3|n|30 + 9
8 |n|31 + 1
2 |n|32 + 3
16 |n|33

+ 16
5 |n|40 + 6
5 |n|41 + 8
15 |n|42 + 1
5 |n|43
)
,

and so on.
 Binomial coeﬃcients, valuations, and words 3

2 Formulas for arbitrary prime powers

We have seen that θp,1(n)
θp,0(n) is a polynomial in |n|w. In fact this is true for θp,α(n)
θp,0(n)
in general. Barat and Grabner [2, §3] showed this implicitly while studying the
asymptotic behavior of ∑N
n=0 θp,α(n).
Rowland [12] gave an algorithm for computing a polynomial expression for
θp,α(n)
θp,0(n) . For p = 2 one computes

θ2,2(n) = 2
|n|1 (− 1
8 |n|10 + |n|100 + 1
4 |n|110 + 1
8 |n|
2
10
)

(which was obtained by Howard [7, Equation (2.5)] and by Huard, Spearman,
and Williams [9, Theorem C]),

θ2,3(n) = 2
|n|1 ( 1
24 |n|10 − 1
2 |n|100 − 1
8 |n|110 + 2|n|1000 + 1
2 |n|1010 + 1
2 |n|1100

+ 1
8 |n|1110 − 1
16 |n|
2
10 + 1
2 |n|10|n|100 + 1
8 |n|10|n|110 + 1
48 |n|
3
10
)
,

and so on. The number of nonzero terms in the polynomial θ2,α(n)
2|n|1 for α =
0, 1, 2, . . . is sequence A275012 [11]:

1, 1, 4, 11, 29, 69, 174, 413, 995, 2364, 5581, 13082, 30600, 71111, 164660, 379682, . . .

The algorithm for computing these polynomials also establishes bounds on
their total degree and on the length of words that appear.

Theorem 2 (Rowland [12]). Let p be a prime, and let α ≥ 0. Then θp,α(n)
θp,0(n) is
given by a polynomial of degree α in |n|w for words w satisfying |w| ≤ α + 1.

However, the algorithm is not particularly fast, as it constructs a polynomial
by summing over certain sets of integer partitions. Spiegelhofer and Wallner [14]
produced a faster algorithm by developing a better understanding of the struc-
ture of this polynomial. In particular, they showed that the polynomial repre-
sentation of θp,α(n)
θp,0(n) is unique, as long as words of the form 0w and w(p − 1)
are not used. Therefore one can talk about the coeﬃcient of a given monomial.
Moreover, this coeﬃcient can be read oﬀ from a certain power series. One can see
evidence of this by looking at the coeﬃcient of |n|10 in the expressions computed
for θ2,α(n)
2|n|1 . The sequence of coeﬃcients is

0, 1
2 , − 1
8 , 1
24 , − 1
64 , 1
160 , − 1
384 , . . . .

These are the coeﬃcients in the power series for log(1 + x
2 ) at x = 0.
The polynomial
 Tp(n, x) :=
 n∑

m=0 xνp(( n
m)) = ∑

α≥0 θp,α(n)xα

4 E. Rowland

is a central object in Spiegelhofer and Wallner’s result. Let

T p(w, x) := Tp(valp(w), x)
θp,0(valp(w)) ,

where valp(w) is the integer obtained by reading w in base p. Deﬁne the rational
function
 rp(w, x) := T p(w, x)T p(wLR, x)
T p(wR, x)T p(wL, x) ,

where the left and right truncations of a word are deﬁned for ℓ ≥ 0, c ∈ {1, . . . , p−
1}, and d ∈ {0, 1, . . . , p − 1} by

ϵL = ϵ (c0ℓ)L = ϵ (c0
ℓw)L = w
ϵR = ϵ cR = ϵ (wd)R = w.

Theorem 3 (Spiegelhofer–Wallner [14]). Let p be a prime, and let α ≥ 0.
Let w1, . . . , wm be words of length ≥ 2 on the alphabet {0, 1, . . . , p − 1} that do
not begin with 0 or end with p − 1. Then the coeﬃcient of |n|k1
w1 · · · |n|
km
wm in the
polynomial θp,α(n)
θp,0(n) is the coeﬃcient of xα in the power series expansion for

1
k1! (log rp(w1, x))k1 · · · 1
km! (log rp(wm, x))km .

3 Matrix generalizations of Fine’s theorem

Spiegelhofer and Wallner’s polynomial Tp(n, x) turns out to have a product for-
mula which generalizes Fine’s theorem. Note that the ﬁrst equation in Carlitz’s
recurrence,
θp,α(pn + d) = (d + 1)θp,α(n) + (p − d − 1)ψp,α−1(n − 1),

can be rewritten in terms of Tp(n, x) as

Tp(pn + d, x) = (d + 1) Tp(n, x) +
 {
0 if n = 0
(p − d − 1) xνp(n)+1 Tp(n − 1, x) if n ≥ 1.

To simplify this equation, let us introduce a secondary polynomial

T ′
p(n, x) :=
 {0 if n = 0
x
νp(n)+1 Tp(n − 1, x) if n ≥ 1,

so that ψp,α−1(n − 1) is the coeﬃcient of xα in T ′
p(n, x). Then we have

Tp(pn + d, x) = (d + 1) Tp(n, x) + (p − d − 1)T ′
p(n, x).

We are close to being able to write
[
Tp(pn + d, x)
T ′
p(pn + d, x)

] = Mp(d) [
Tp(n, x)
T ′
p(n, x)
] (1)

Binomial coeﬃcients, valuations, and words 5

for some 2 × 2 matrix Mp(d), thereby expressing Tp(pn + d, x) and T ′
p(pn + d, x)
in terms of Tp(n, x) and T ′
p(n, x). Carlitz’s second equation,

ψp,α(pn + d) =
 {(d + 1)θp,α(n) + (p − d − 1)ψp,α−1(n − 1) if 0 ≤ d ≤ p − 2
pψp,α−1(n) if d = p − 1,

expresses ψp,α(pn + d) in terms of θ and ψ. But because the coeﬃcient of x
α in
T ′
p(n, x) is ψp,α−1(n − 1) we instead need to express ψp,α(pn + d − 1) in terms
of θ and ψ. The desired equation is

ψp,α(pn + d − 1) = dθp,α(n) + (p − d)ψp,α−1(n − 1),

which is equivalent to

T ′
p(pn + d, x) = d x Tp(n, x) + (p − d) x T ′
p(n, x).

Therefore, the matrix we seek is

Mp(d) = [
d + 1 p − d − 1
d x (p − d) x
 ] .

Theorem 4 (Rowland [13]). Let p be a prime, and let n ≥ 0. Let nℓ · · · n1n0
be the standard base-p representation of n. Then

Tp(n, x) = [
1 0] Mp(n0) Mp(n1) · · · Mp(nℓ) [
1
0

] .

Setting x = 0 gives Fine’s result as a special case. Namely, the deﬁnition of
T ′
p(n, x) implies T ′
p(n, 0) = 0, so Equation (1) becomes

[
θp,0(pn + d)
0
 ] = [
d + 1 p − d − 1
0 0
 ] [
θp,0(n)
0
 ] ,

or simply θp,0(pn + d) = (d + 1) θp,0(n).

Moreover, Theorem 4 generalizes naturally to multinomial coeﬃcients. For a
k-tuple m = (m1, m2, . . . , mk) of non-negative integers, deﬁne

total m := m1 + m2 + · · · + mk

and
 mult m := (total m)!
m1! m2! · · · mk! .

Let cp,k(n) be the coeﬃcient of xn in (1 + x + x2 + · · · + xp−1)
k. For each
d ∈ {0, 1, . . . , p − 1}, let Mp,k(d) be the k × k matrix whose (i, j) entry is

6 E. Rowland

cp,k(p (j − 1) + d − (i − 1)) xi−1. For example, let p = 5 and k = 3; the ma-
trices M5,3(0), . . . , M5,3(4) are



1 18 6
0 15x 10x
0 10x2 15x2


 ,
 

3 19 3
x 18x 6x
0 15x2 10x2


 ,
 

 6 18 1
3x 19x 3x
x2 18x2 6x2


 ,



 10 15 0
6x 18x x
3x2 19x2 3x2


 ,
 

 15 10 0
10x 15x 0
6x2 18x2 x2


 .

Theorem 5 (Rowland [13]). Let p be a prime, let k ≥ 1, and let n ≥ 0. Let
e = [
1 0 0 · · · 0] be the ﬁrst standard basis vector in Z
k. Let nℓ · · · n1n0 be the
standard base-p representation of n. Then
∑

m∈Nk
total m=n
 xνp(mult m) = e Mp,k(n0) Mp,k(n1) · · · Mp,k(nℓ) e⊤.

The proof essentially amounts to showing that, for d ∈ {0, 1, . . . , p − 1},
0 ≤ i ≤ k − 1, and α ≥ 0, the map β deﬁned by

β(m) := (⌊m/p⌋, m mod p)

is a bijection from the set

A = {m ∈ Nk : total m = pn + d − i and νp(mult m) = α − νp
( (pn + d)!
(pn + d − i)!
 )}

to the set

B =
 k−1⋃

j=0
 ( {c ∈ Nk : total c = n − j and νp(mult c) = α − νp
( n!
(n − j)!
 ) − j}

× {d ∈ {0, 1, . . . , p − 1}k : total d = pj + d − i
} )

.

The following lemma implies that if m ∈ A then β(m) ∈ B.

Lemma 6. Let p be a prime, k ≥ 1, n ≥ 0, d ∈ {0, 1, . . . , p − 1}, and 0 ≤ i ≤
k − 1. Let m ∈ Nk with total m = pn + d − i. Let j = n − total⌊m/p⌋. Then
total(m mod p) = pj + d − i, 0 ≤ j ≤ k − 1, and

νp
( (pn + d)!
(pn + d − i)!
 ) + νp(mult m) = νp
( n!
(n − j)!
 ) + νp(mult⌊m/p⌋) + j.

We conclude by mentioning a connection to regular sequences. A sequence
s(n)n≥0, with entries in some ﬁeld, is p-regular if the vector space generated
by the set of subsequences {s(pen + i)n≥0 : e ≥ 0 and 0 ≤ i ≤ p
e − 1} is ﬁnite-
dimensional. For example, the sequence (θp,0(n))n≥0 is a p-regular sequence of

Binomial coeﬃcients, valuations, and words 7

integers [1, Example 14]. It follows from Theorem 5 and [1, Theorem 2.2] that
the sequence of polynomials




 ∑

m∈N
k
total m=n
 xνp(mult m)






n≥0

is p-regular for each k.

References

1. Jean-Paul Allouche and Jeﬀrey Shallit, The ring of k-regular sequences, Theoretical
Computer Science 98 (1992) 163–197.
2. Guy Barat and Peter J. Grabner, Distribution of binomial coeﬃcients and digital
functions, Journal of the London Mathematical Society 64 (2001) 523–547.
3. Leonard Carlitz, The number of binomial coeﬃcients divisible by a ﬁxed power of
a prime, Rendiconti del Circolo Matematico di Palermo 16 (1967) 299–320.
4. Kenneth Davis and William Webb, Pascal’s triangle modulo 4, The Fibonacci
Quarterly 29 (1989) 79–83.
5. Nathan Fine, Binomial coeﬃcients modulo a prime, The American Mathematical
Monthly 54 (1947) 589–592.
6. James W. L. Glaisher, On the residue of a binomial-theorem coeﬃcient with respect
to a prime modulus, Quarterly Journal of Pure and Applied Mathematics 30 (1899)
150–156.
7. Fred T. Howard, The number of binomial coeﬃcients divisible by a ﬁxed power of
2, Proceedings of the American Mathematical Society 29 (1971) 236–242.
8. James Huard, Blair Spearman, and Kenneth Williams, Pascal’s triangle (mod 9),
Acta Arithmetica 78 (1997) 331–349.
9. James Huard, Blair Spearman, and Kenneth Williams, Pascal’s triangle (mod 8),
European Journal of Combinatorics 19 (1998) 45–62.
10. Ernst Kummer, ¨Uber die Erg¨anzungss¨atze zu den allgemeinen Re-
ciprocit¨atsgesetzen, Journal f¨ur die reine und angewandte Mathematik 44
(1852) 93–146.
11. The OEIS Foundation, The On-Line Encyclopedia of Integer Sequences, http:
//oeis.org.
12. Eric Rowland, The number of nonzero binomial coeﬃcients modulo pα, Journal of
Combinatorics and Number Theory 3 (2011) 15–25.
13. Eric Rowland, A matrix generalization of a theorem of Fine, https://arxiv.org/
abs/1704.05872.
14. Lukas Spiegelhofer and Michael Wallner, An explicit generating function arising in
counting binomial coeﬃcients divisible by powers of primes, https://arxiv.org/
abs/1604.07089.
