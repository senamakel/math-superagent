<!-- source: https://emis.muni.cz/journals/INTEGERS/papers/k14/k14.pdf | converted from PDF -->

#A14 INTEGERS 10 (2010), 187-199

MULTIPLICITIES OF INTEGER ARRAYS

Lane Clark
Department of Mathematics, Southern Illinois University Carbondale, Carbondale,
IL 62901-4408, USA lclark@math.siu.edu

Received: 5/17/09, Accepted: 12/28/09 , Published: 5/5/10

Abstract
We prove a general theorem about the multiplicity of the entries in certain integer
arrays which is best possible in general. As an application we give non-trivial
bounds for the multiplicities of several well-known combinatorial arrays including
the binomial coeﬃcients, Narayana numbers and the Eulerian numbers. For the
binomial coeﬃcients we obtain the result of Singmaster.

1. Introduction

An integer array or array is a function a : N
2 → N where a(n, 0) = 1 (n ∈
N). For a function b : P
2 → N where b(n, 1) = 1 (n ∈ P), consider the array
a(n, k) = b(n, k + 1) (n ∈ P, k ∈ N) where a(0, 0) = 1 and a(0, k) = 0 (k ∈ P).
We write a = shift b and say a results from shifting b. Here N denotes the non-
negative integers, P denotes the positive integers and [n] = {1, . . . , n} (n ∈ P). The
cardinality of a set S is denoted # S or |S|.
Suppose a is an array. Then

(D1) a is semi-triangular if and only if there exists a strictly increasing function d :
N ↦→ N such that a(n, k) ̸= 0 ⇔ 0 ≤ k ≤ d(n) (n ∈ N).

Suppose a = (a, d) is a semi-triangular array. Then

(D2) a is increasing if and only if a(n + 1, k) > a(n, k) for 1 ≤ k ≤ d(n) (n ∈ N).

(D3) a is semi-unimodal if and only if there exists a non-decreasing function
f : N → N with 0 ≤ f (n) ≤ d(n), limn→∞ f (n) = ∞, and a(n, 0) ≤
· · · ≤ a(n, f (n) − 1) < a(n, f (n)) which includes every non-zero value of the
a(n, k) (n ∈ N). Then the largest value a(n, f (n)) of the a(n, k) ﬁrst occurs
at k = f (n).

The non-zero entries of a semi-triangular, increasing, semi-unimodal array a =
(a, d, f ) have the general form given in Figure 1.

INTEGERS: 10 (2010) 188

Suppose a = (a, d, f ) is a semi-triangular, semi-unimodal array. Then

(D4) a has multiplicity r if and only if at most r of a(n, 0), . . . , a(n, d(n)) assume

any identical value (n ∈ N). Then ra(n, f (n)) ≥ d(n) (n ∈ N) by the Pigeon-

hole Principle.

(D5) a is ∆-bounded if and only if f (n) ≤ f (n − 1) + ∆ (n ∈ P).

(D6) a has growth function g : [0, ∞) → [τ, ∞) where τ ∈ R, which is continuous,

strictly increasing, surjective and satisﬁes g(f (n)) ≤ a(n, f (n)) (n ∈ N).

Since f is non-decreasing with limn→∞ f (n) = ∞ and g is strictly increasing,
g(f (n)) is non-decreasing with limn→∞ g(f (n)) = ∞. Here g has continuous,
strictly increasing, surjective, inverse function g−1 : [τ, ∞) → [0, ∞). The growth
function g is not unique: the larger the g, the smaller the g−1, and the better our
bound in Theorem 2.
A semi-triangular, increasing, semi-unimodal, ∆-bounded array a = (a, d, f, r, ∆,
g) with multiplicity r and growth function g is called normal.
For k ≥ 1, take the smallest n0 with k ≤ d(n0). Then a(n, k) is a strictly
increasing function of n ≥ n0. Hence, a(n + m, k) ≥ a(n, k) + m ≥ m + 1 for
n+m ≥ n ≥ n0. Here f (n) is non-decreasing (illustrated for f (n) strictly increasing)
and d(n) is strictly increasing.

Figure 1: General form of non-zero entries of a semi-triangular, increasing, semi-
unimodal array

INTEGERS: 10 (2010) 189

Suppose a = shift b and a = (a, d, f, r, ∆, g) is a normal array. Then

a(n, k) ̸= 0 ⇔ 0 ≤ k ≤ d(n) if and only if b(n, k) ̸= 0 ⇔ 1 ≤ k ≤ d(n) + 1;

a(n + 1, k) > a(n, k) for 1 ≤ k ≤ d(n) if and only if

b(n + 1, k) > b(n, k) for 2 ≤ k ≤ d(n) + 1;

a(n, 0) ≤ · · · ≤ a(n, f (n − 1) < a(n, f (n)) if and only if

b(n, 1) ≤ · · · ≤ b(n, f (n)) < b(n, f (n) + 1);

a has multiplicity r if and only if b has multiplicity r;

g(f (n)) ≤ a(n, f (n)) if and only if g(f (n)) ≤ b(n, f (n) + 1).

In this case we give the parameters d, f, r, ∆, g for b, not for a = shift b, and we
say that b is a normal array, not that a = shift b is a normal array.
An array a is combinatorial if and only if the a(n, k) enumerate mathematical
structures. For example, the binomial coeﬃcients (
n
k) enumerate the k-subsets of an
n-set; the Narayana numbers N (n, k) enumerate the Catalan paths from (0, 0) to
(n, n) with k peaks; and the Eulerian numbers A(n, k) enumerate the permutations
of [n] with k − 1 ascents. These are normal combinatorial arrays as are many other
combinatorial arrays.

2. Results

Suppose function c : X 2 → N where X = N or P. For t ∈ N, let

Nc(t) = # {
(n, k) ∈ X 2 : c(n, k) = t
} .

Observation 1. Suppose a = shift b. Then Na(t) = Nb(t) for all t ∈ P .

If a = (a, d) is a semi-triangular array, then Na(0) = Na(1) = ℵ0 by deﬁnition.
Suppose a = (a, d, f ) is a semi-triangular, increasing, semi-unimodal array. Since
a is semi-triangular and increasing, d(n), a(n, 1) ≥ n. Since a is semi-unimodal,
a(n, k) ≥ a(n, 1) ≥ n or a(n, k) = 1 for 1 ≤ k ≤ d(n). Consequently, Na(t) ≤
d(0) + · · · + d(t) for t ≥ 2.
We now prove the main result of the paper. The inﬁnite families of normal
combinatorial arrays given in Examples 1 and 2 demonstrate our result is best
possible in general apart from the constant r∆.

Theorem 2. Suppose that a = (a, d, f, r, ∆, g) is a normal array. For all integers
t ≥ 2, Na(t) < r(
g−1(t) + ∆
)
.

INTEGERS: 10 (2010) 190

Proof. Fix t ≥ 2. Let m = m(t) be the smallest positive integer satisfying
a(m, f (m)) ≥ t which exists since a(m, f (m)) ≥ g(f (m)) and g(f (m)) is non-
decreasing with limm→∞ g(f (m)) = ∞. Then (m − 1, f (m − 1) ∈ N)

t > a(m − 1, f (m − 1)) ≥ g(f (m − 1)), i.e., f (m − 1) < g−1(t).

Suppose a(n, k) = t. Since a is increasing and semi-unimodal, n ≥ m. We may
assume that 1 ≤ k ≤ f (n) since a is semi-unimodal. Suppose k ≥ f (m) + 1, hence,
f (n) ≥ k > f (m). Then n > m since n ≥ m. Since a is semi-unimodal, increasing,
f (n) ≥ k > f (m) and n > m,

t = a(n, k) ≥ a(n, f (m)) > a(m, f (m)) ≥ t,

which is a contradiction. Hence, 1 ≤ k ≤ f (m) (see Figure 2). For each such k,
there is at most one n with a(n, k) = t since a is increasing. For each such n and
k, there are at most r − 1 other values 0 ≤ ℓ ≤ d(n) with a(n, ℓ) = t since a has
multiplicity r. Since a is ∆-bounded, there are at most

r f (m) ≤ r (
f (m − 1) + ∆
) < r(
g−1(t) + ∆
)

pairs (n, k) with a(n, k) = t. !

The following is a special case of Theorem 2.

Corollary 3. Suppose a = (a, d, f, r, ∆, g) is a normal array. If g(x) = τ x−c where
τ ∈ (1, ∞) and c ∈ R, then
 Na(t) < r(
logτ t + c + ∆
) .

Figure 2: Part of the proof of Theorem 2

INTEGERS: 10 (2010) 191

Proof. Apply Theorem 2 with g−1(x) = logτ x + c. !

More generally we have the following result.

Corollary 4. Suppose a = (a, d, f, r, ∆, g) is a normal array. If g(x) = Ω (τ x)
where τ ∈ (1, ∞), then Na(t) = O( logτ t ) .

Proof. If g(x) = Ω (τ x), then g−1(x) = O(logτ x). Theorem 2 implies Na(t) =
O ( logτ t ). !

Example 5. (Polynomial Growth) Fix integer s ≥ 2. Let a(n, k) denote the
number of functions f : [s] → [2n] with Image(f ) ⊆ [n + k] for 1 ≤ k ≤ ⌊n/2⌋, and,
Image(f ) ⊆ [2n] − [k − 1] for ⌊n/2⌋ + 1 ≤ k ≤ n. Set a(n, 0) = 1 for n ∈ N. Then

a(n, k) =
 




1, k = 0;
(n + k)
s, 1 ≤ k ≤ ⌊n/2⌋;
(2n + 1 − k)
s, ⌊n/2⌋ + 1 ≤ k ≤ n;
0, otherwise .

The combinatorial array a(n, k) is normal (in particular, is increasing) with d(n) =
n, f (n) = ⌈n/2⌉, g(x) = (3x − 1)
s with τ = −1 (odd s) and τ = 0 (even s), r = 2
and ∆ = 1 . Then g−1(x) = (1/3)x
1/s + (1/3) and Theorem 2 implies

Na(t) < 2 t
1/s

3 + 8
3 .

Suppose n ∈ P. If n is even, then a(n, 1), . . . , a(n, n) is the set (n + 1)
s < · · · <
(n + ⌊n/2⌋)
s where each is assumed twice. If n is odd, then a(n, 1), . . . , a(n, n) is
the set (n + 1)
s < · · · < (n + ⌊n/2⌋)
s < (n + ⌊n/2⌋ + 1)
s = a(n, ⌊n/2⌋ + 1) where
each is assumed twice except (n + ⌊n/2⌋ + 1)
s which is assumed once.
Suppose t = u
s where non-zero u ≡ 0 mod 3.
If n ≥ u, then all non-zero a(n, k) ≥ (u + 1)
s > t except a(n, 0) = 1 < t.
If n ≤ (2u − 3)/3, then all a(n, k) ≤ (3n/2 + 1)
s ≤ (u − 1/2)
s < t. For each
2u/3 ≤ n ≤ u − 1, there are precisely two 0 ≤ k ≤ n with a(n, k) = t. Hence,

Na(t) = 2u
3 = 2t
1/s

3 .

Consequently, for inﬁnitely-many t,

Na(t) = 2t
1/s

3 .

INTEGERS: 10 (2010) 192

Example 6. (Exponential Growth) Fix integer s ≥ 2. Let a(n, k) denote the
number of functions f : [2n] → [s] where f (n + k + 1) = · · · = f (2n) = 1 for
1 ≤ k ≤ ⌊n/2⌋, and, f (2n + 2 − k) = · · · = f (2n) = 1 for ⌊n/2⌋ + 1 ≤ k ≤ n. Set
a(n, 0) = 1 for n ∈ N. Then

a(n, k) =
 




1, k = 0;
s
(n+k), 1 ≤ k ≤ ⌊n/2⌋;
s
(2n+1−k), ⌊n/2⌋ + 1 ≤ k ≤ n;
0, otherwise .

The combinatorial array a(n, k) is normal (in particular, is increasing) with d(n) =
n, f (n) = ⌈n/2⌉, g(x) = s
3x−1 with τ = s
−1, r = 2 and ∆ = 1. Then g−1(x) =
(1/3) logs x + (1/3) and Theorem 2 implies

Na(t) < 2 logs t
3 + 8
3 .

Suppose n ∈ P. If n is even, then a(n, 1), . . . , a(n, n) is the set s
n+1 < · · · <
s
n+⌊n/2⌋ where each is assumed twice. If n is odd, then a(n, 1), . . . , a(n, n) is the
set s
n+1 < · · · < s
n+⌊n/2⌋ < s
n+⌊n/2⌋+1 = a(n, ⌊n/2⌋ + 1) where each is assumed
twice except s
n+⌊n/2⌋+1 which is assumed once.
Suppose t = s
u where non-zero u ≡ 0 mod 3.
If n ≥ u, then all non-zero a(n, k) ≥ s
(u+1) > t except a(n, 0) = 1 < t. If
n ≤ (2u − 3)/3, then all a(n, k) ≤ s
3n/2+1 ≤ s
u−1/2 < t. For each 2u/3 ≤ n ≤ u − 1,
there are precisely two 0 ≤ k ≤ n with a(n, k) = t. Hence,

Na(t) = 2u
3 = 2 logs t
3 .

Consequently, for inﬁnitely-many t,

Na(t) = 2 logs t
3 .

In passing we mention the Inﬁnite Pigeonhole Principle: If κ is a regular cardinal,
λ is a cardinal with λ < κ, and a : κ → λ, then there exists t ∈ λ with |a
−1(t)| ≥ κ.
In particular, |N × N| = |N| = ℵ0 is a regular cardinal. An array a : N
2 → N
may be viewed as a function a : ℵ0 → ℵ0 by traversing successive diagonals of
the displayed form of a. If a is semi-triangular, then |a
−1(0)| = |a
−1(1)| = ℵ0
by deﬁnition. For a normal array a = (a, d, f, r, ∆, g), Theorem 2 gives the upper
bound |a
−1(t)| < r(g−1(t) + ∆) for all t ≥ 2. Hence Theorem 2 is, in a sense, a
complement of the Inﬁnite Pigeonhole Principle which provides a lower bound for
some |a
−1(t)|.

INTEGERS: 10 (2010) 193

3. Applications

Suppose a = (a, d, f, r, ∆, g) is a normal array. Theorem 2 gives Na(t) < r(
g−1(t) +
∆
)
. The normal combinatorial arrays in Examples 1 and 2 show this bound is best
possible apart from the constant r∆.
We apply Theorem 2 to several of the numerous normal combinatorial arrays
including the well-known binomial coeﬃcients (
n
k)
, Narayana numbers N (n, k) and
Eulerian numbers A(n, k). For the binomial coeﬃcients we obtain the result of
Singmaster [11]. For all the other arrays a we obtain non-trivial bounds for Na(t)
which to our knowledge are new. The results of Examples 3 − 6 are summarized in
the following table.

a(n, k) d(n) f (n) g(x) r ∆ Na(t)(
n
k) n ⌊n/2⌋ 2
x 2 1 < 2 log2 t + 2 (t ≥ 2) [11]
N (n, k) n ⌈n/2⌉ 4
x−1/x 2 1 < 2 log3 t (t ≥ B)
A(n, k) n ⌈n/2⌉ (x/e)
x 2 1 < 3 ln t/ ln ln t (t ≥ B)
Q(n, k) n ⌈n/2⌉ ρ
x 2 1 < 2 logρ t + 2 (t ≥ 2)

Table 1: Results from Examples 3–6

One would hope that a better bound than that provided by the general Theorem
2 could be obtained for a particular normal array by using its own special properties.
Even slight improvements of this general bound can require deep results from, say,
number theory (see Example 7).

3.1. Binomial Coeﬃcients

Example 7. The array of binomial coeﬃcients a(n, k) = (
n
k
) .

The maximum of the (
n
k) is ( n
⌊n/2⌋
) = ( n
⌈n/2⌉
) ≥ 2
⌊n/2⌋ for n ∈ N. The array
b(n, k) is normal with d(n) = n, f (n) = ⌊n/2⌋, g(x) = 2
x with τ = 1, r = 2 and
∆ = 1. Then g−1(x) = log2 x and Theorem 2 implies

Na(t) < 2 log2 t + 2 (t ≥ 2) .

This is the result of Singmaster [11].
Singmaster [11] searched up to t = 2
48 and found that all Na(t) ≤ 8. He also
found that Na(t) = 6 only for t = 120, 210, 1540, 7140, 11628, 24310 and
Na(t) = 8 only for t = 3003. Singmaster conjectured there that Na(t) = O(1).
Erd˝os concurred with this conjecture stating that it must be very hard (see [11;
p.385]). Singmaster [12] showed that there are inﬁnitely-many t with Na(t) ≥ 6.

INTEGERS: 10 (2010) 194

He conjectured there that Na(t) ≤ 10. Both conjectures are still open. The
best result to date is Abbott, Erd˝os and Hanson [1] who showed that Na(t) =
O (log t/log log t) for t ≥ 2 . Their proof used a deep result of Ingham [5] on the dis-
tribution of the primes: If α ≥ 5/8, then there is a prime between x and x+x
α for all
suﬃciently large x . See de Weger [16] for some further results on the multiplicities
of the binomial coeﬃcients.

3.2. Narayana Numbers

The Narayana numbers are attributed to Narayana [7] and are deﬁned by

N (n, k) = 1
n
 (
n
k
)( n
k − 1

) (n, k ∈ P) .

They have a nice combinatorial deﬁnition. A Catalan path P is a lattice path from
(0, 0) to (n, n) that does not go below the line y = x. Then P = (s1, . . . , s2n)
where each sj ∈ {V = (0, 1), H = (1, 0)}. Here P has a peak at j provided
(sj−1, sj) = (V, H). If Cat(n) denotes the set of Catalan paths from (0, 0) to
(n, n), then |Cat(n)| = (
2n
n )
/(n + 1) is the Catalan number Cn. If Cat(n, k) de-
notes the set of Catalan paths from (0, 0) to (n, n) with k peaks, then the statistic
|Cat(n, k)| = N (n, k). Hence, N (n, 1) + · · · + N (n, n) = Cn. Sulanke [14], [15]
cataloged more than 200 other statistics on Cat(n) with Narayana distribution. Ri-
ordan [10] showed that the number of labelled plane trees with n edges and k leaves
is N (n, k). Many other statistics of combinatorial structures have Narayana distri-
bution (cf. [2], [8], [9]). The Narayana numbers are sequence A001263 in Sloane
[13].

Example 8. The array of Narayana numbers N (n, k).
The maximum of the N (n, k) occurs at ⌈n/2⌉ for odd n and at ⌈n/2⌉ and
⌈n/2⌉ + 1 for even n. Further, N (n, ⌈n/2⌉) ≥ 4
⌈n/2⌉−1/⌈n/2⌉ for n ∈ P. The
array N (n, k) is normal with d(n) = n, f (n) = ⌈n/2⌉, g(x) = 4
x−1/x with τ = 1,
r = 2 and ∆ = 1. Then g−1(x) < log3x − 1 (x ≥ B) and Observation 1 and
Theorem 2 imply
 NN (t) < 2 log3 t (t ≥ B) .

To our knowledge this non-trivial bound for NN (t) is new. We conjecture that
NN (t) = O(1). In view of Erd˝os’ comments regarding the multiplicities of the
binomial coeﬃcients this conjecture may be hard. We note that NN (105) = 4 :
N (7, 3) = N (7, 5) = N (15, 2) = N (15, 14) = 105. The non-zero values of N (n, k)
for 1 ≤ n ≤ 10 are given in the following table.

INTEGERS: 10 (2010) 195

k
N (n, k) 1 2 3 4 5 6 7 8 9 10
1 1
2 1 1
3 1 3 1
4 1 6 6 1
n 5 1 10 20 10 1
6 1 15 50 50 15 1
7 1 21 105 175 105 21 1
8 1 28 196 490 490 196 28 1
9 1 36 336 1176 1764 1176 336 36 1
10 1 45 540 2520 5292 5292 2520 540 45 1

Table 2. Small values of N (n, k)

3.3. Eulerian Numbers

The Eulerian numbers A(n, k) may be deﬁned by the recurrence relation

A(n, k) = (n − k + 1) A(n − 1, k − 1) + k A(n − 1, k) (n, k ≥ 2)

with initial conditions A(n, 1) = 1 for n ≥ 1 and A(1, k) = 0 for k ≥ 2 (cf. Comtet
[3; pps.240–246]). Hence, A(n, k) ̸= 0 if and only if 1 ≤ k ≤ n. Dillon and Roselle
[4] ﬁrst showed that A(n, k) is the number of permutations of [n] with k − 1 ascents
or with k − 1 descents.

Example 9. The array of Eulerian numbers A(n, k) .
The maximum of the A(n, k) occurs at ⌈n/2⌉ for odd n and at ⌈n/2⌉ and
⌈n/2⌉ + 1 for even n. The recurrence relation for the A(n, k) implies A(n, ⌈n/2⌉) ≥
⌈n/2⌉ A(n − 1, ⌈(n − 1)/2⌉) for n ≥ 3. Iteration of this inequality and Stirlings
Formula gives the weak bound A(n, ⌈n/2⌉) ≥ (⌈n/2⌉/e)
⌈n/2⌉ for n ∈ P. In fact,

A(n, ⌈n/2⌉) ∼ √
12 ( n
e
 )n .

The array A(n, k) is normal with d(n) = n, f (n) = ⌈n/2⌉, g(x) = (x/e)
x with
τ = e
−1, r = 2 and ∆ = 1. Then g−1(x) < 3 ln x/2 ln ln x − 1 (x ≥ B) and
Observation 1 and Theorem 2 imply

NA(t) < 3 ln t
ln ln t (t ≥ B) .

To our knowledge this non-trivial bound for NA(t) is new. We conjecture that
NA(t) = O(1). The non-zero values of A(n, k) for 1 ≤ n ≤ 10 are given in the
following table.

INTEGERS: 10 (2010) 196

n
A(n, k) 1 2 3 4 5 6 7 8 9 10
1 1 1 1 1 1 1 1 1 1 1
2 1 4 11 26 57 120 247 502 1013
3 1 11 66 302 1191 4293 14608 47840
4 1 26 302 2416 15619 88234 455192
k 5 1 57 1191 15619 156190 1310354
6 1 120 4293 88234 1310354
7 1 247 14608 455192
8 1 502 47840
9 1 1013
10 1

Table 3. Small values of A(n, k)

3.4. Quasi-Eulerian Numbers

Suppose Q, b, c : P
2 → N and Q(n, k) satisﬁes the recurrence relation

Q(n, k) = b(n, k) Q(n − 1, k − 1) + c(n, k) Q(n − 1, k) (n, k ≥ 2) (1)

where Q(n, 1) = 1 (n ∈ P), Q(1, k) = 0 (k ≥ 2) and b(n, k), c(n, k) ̸= 0 ⇔ k ∈
[n] (n ∈ P). Hence, Q(n, k) ̸= 0 if and only if 1 ≤ k ≤ n. This deﬁnition of Q
is due to Kurtz [6] who investigated their concavity properties. Taking b(n, k) =
n − k + 1 and c(n, k) = k gives the Eulerian numbers. Hence, we call the Q(n, k) the
Quasi-Eulerian numbers.
Kurtz [6] proved that the Q satisfying (1) are strictly log-concave, hence have
a peak or plateau of width two, provided the following hold for 1 < k < n and
n ≥ 3:
 2 b(n, k) ≥ b(n, k − 1) + b(n, k + 1) (2)

2 c(n, k) ≥ c(n, k − 1) + c(n, k + 1). (3)

Suppose b(n, n) = 1 (n ∈ P) and

b(n, k) = c(n, n − k + 1) (k ∈ [n], n ∈ P) . (4)

If (4) holds, then (2) and (3) are equivalent. The Eulerian numbers satisfy (1) − (4).

INTEGERS: 10 (2010) 197

If Q satisﬁes (1) and (4), then Q is symmetric: Here Q(2, 1) = Q(2, 2) = 1.
Suppose Q(n − 1, k) = Q(n − 1, n − k) (k ∈ [n − 1], n ≥ 3). Then Q(n, 1) =
Q(n, n) = 1 and, for 2 ≤ k ≤ n − 1,

Q(n, n − k + 1) = b(n, n − k + 1) Q(n − 1, n − k)

+ c(n, n − k + 1) Q(n − 1, n − k + 1)

= c(n, k) Q(n − 1, k) + b(n, k) Q(n − 1, k − 1)

= Q(n, k) .

Suppose Q satisﬁes (1) − (4). Then the maximum of the Q(n, k) occurs at ⌈n/2⌉
for odd n and at ⌈n/2⌉ and ⌈n/2⌉ + 1 for even n (n ∈ P). Since Q is symmetric,
(1) implies Q(n, ⌈n/2⌉) ≥ c(n, ⌈n/2⌉) Q(n − 1, ⌈(n − 1)/2⌉). (5)

Iteration of (5) gives the weak bound

Q(n, ⌈n/2⌉) ≥
 n∏

k = 2 c(k, ⌈k/2⌉) ≥ g(⌈n/2⌉) (n ≥ 2) .

Suppose we can lift g : P → P to g : [0, ∞) → [τ, ∞) which is continuous, strictly
increasing and surjective. Then the array Q is normal with d(n) = n, f (n) =
⌈n/2⌉, g(x), r = 2 and ∆ = 1. Observation 1 and Theorem 2 imply

NQ(t) < 2 g−1(t) + 2 .

For the Eulerian numbers, c(n, k) = k and ∏n
k = 2 ⌈k/2⌉ ≥ (⌈n/2⌉/e)
⌈n/2⌉ and we
took g(x) = (x/e)
x in Example 9.
Our ﬁnal example is one inﬁnite sub-family of the functions Q.
Example 10. Certain arrays of Quasi-Eulerian numbers Q(n, k).
Suppose h : P → P with 2 h(k) ≥ h(k − 1) + h(k + 1) (k ≥ 2). For example,
h(k) = k or h ≡ ℓ ∈ P are such functions. Deﬁne Q, b, c : P
2 → N where Q is given
by (1) and where

c(n, k) = b(n, n − k + 1) =
 {
h(k), k ∈ [n], n ∈ P;
0, otherwise .

Then Q satisﬁes (1) − (4). Suppose ∏n
k = 2 h(k) ≥ ρ
⌈n/2⌉ (n ≥ 2) where ρ ∈ (1, ∞).
For example, if h ≡ ℓ ≥ 2, then ∏n
k = 2 h(k) = ℓ n−1 ≥ ρ
⌈n/2⌉ (n ≥ 2) where ρ = ℓ.
The array Q is normal with d(n) = n, f (n) = ⌈n/2⌉, g(x) = ρ
x with τ = ρ, r = 2
and ∆ = 1. Observation 1 and Theorem 2 imply

NQ(t) < 2 logρ t + 2 (t ≥ 2) .

INTEGERS: 10 (2010) 198

4. Conclusion

For every normal ∆-bounded array a = (a, d, f, r, ∆, g) with multiplicity r and
growth function g, Theorem 1 gives the non-trivial bound Na(t) < r(
g−1(t) + ∆
)

for all t ≥ 2. This bound is best possible in general, apart from the constant
r∆, as the combinatorial arrays in Examples 5 and 6 demonstrate. Perhaps special
properties of a particular array a can be used to give better upper bounds for Na(t).

References

[1] H. Abbott, P. Erd˝os, D. Hanson, On the Number of Times an Integer Occurs as a Binomial
Coeﬃcient, The American Mathematical Monthly 81 (1974), no. 3, 256–261.

[2] W. Chen, A General Bijective Algorithm for Trees, Proceedings of the National Academy of
Sciences 87 (1990), 9635–9639.

[3] L. Comtet, Advanced Combinatorics, D. Reidel Publishing Company (1974).

[4] J. Dillon, D. Roselle, Eulerian Numbers of Higher Order, Duke Mathematics Journal 35
(1968), no. 2, 247–256.

[5] A. Ingham, On the Diﬀerence Between Consecutive Primes, The Quarterly Journal of Math-
ematics (Oxford) 8 (1937), 255–266.

[6] D. Kurtz, A Note on Concavity Properties of Triangular Arrays of Numbers, Journal of
Combinatorial Theory Series A 13 (1972), 135–139.

[7] T. Narayana, Sur les Treillis Form´es par les Partitions d’une Unities et Leurs Applications ´a
la Th´eorie des Probabilit´es, Comptes Rendus de l’Acad´emie des Sciences Paris 240 (1955),
1188–1189.

[8] T. Narayana, A Partial Order and Its Application to Probability Theory, Sankhy¯a 21 (1959),
91–98.

[9] T. Narayana, Lattice Path Combinatorics with Statistical Applications, University of Toronto
Press (1979).

[10] J. Riordan, Enumeration of Plane Trees by Branches and Endpoints, Journal of Combina-
torial Theory Series A 19 (1975), 214–222.

[11] D. Singmaster, How Often Does an Integer Occur as a Binomial Coeﬃcient, The American
Mathematical Monthly 78 (1971), no. 4, 385–386.

[12] D. Singmaster, Repeated Binomial Coeﬃcients and Fibonacci Numbers, Fibonacci Quarterly
13 (1975), no. 4, 295–298.

[13] N. Sloane, The On-Line Encyclopedia of Integer Sequences, published electronically at
www.research.att.com/∼njas/sequences .

[14] R. Sulanke, Catalan Path Statistics Having the Narayana Distribution, Discrete Mathematics
180 (1998), 369–389.

INTEGERS: 10 (2010) 199

[15] R. Sulanke, Constraint Sensitive Catalan Path Statistics Having the Narayana Distribution,
Discrete Mathematics 204 (1998), 397–414.

[16] B. de Weger, Equal Binomial Coeﬃcients: Some Elementary Considerations, Journal of
Number Theory 63 (1997), 373–386.
