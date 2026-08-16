<!-- source: https://arxiv.org/pdf/1707.01440 | converted from PDF -->

arXiv:1707.01440v1  [math.NT]  5 Jul 2017
ON SUBWORDS IN THE BASE-q EXPANSION OF
POLYNOMIAL AND EXPONENTIAL FUNCTIONS

HAJIME KANEKO AND THOMAS STOLL

Abstract. Let w be any word over the alphabet {0, 1, . . . , q − 1}, and denote
by h either a polynomial of degree d ≥ 1 or h : n ↦→ mn for a ﬁxed m. Fur-
thermore, denote by eq(w; h(n)) the number of occurrences of w as a subword
in the base-q expansion of h(n). We show that

lim sup
n→∞
 eq(w; h(n))
log n ≥ γ(w)
l log q ,

where l is the length of w and γ(w) ≥ 1 is a constant depending on a property
of circular shifts of w. This generalizes work by the second author as well as
is related to a generalization of Lagarias of a problem of Erd˝os.

1. Introduction

Let q ≥ 2 be an integer and w a nonempty ﬁnite word over the alphabet Aq :=
{0, 1, . . . , q − 1}. We denote by l = l(w) the length of w which is the number of
symbols (or letters) in w. For any integer n ≥ 1, consider the ﬁnite base-q expansion
of n,
 n =
 M∑

i=0 niqi,

where M = M (n) = ⌊logq n⌋ denotes the position of the most signiﬁcant digit. We
write (n)q = nM nM−1 · · · n0
as a shorthand notation and regard this as a word over Aq. For convenience, put
(0)q := 0. In this paper, we are concerned with the quantity eq(w; n) which denotes
the number of (possibly overlapping) occurrences of the word w in the ﬁnite base-
q expansion of n. For example, for q = 10, w = 202 and n = 20202 we have
e10(202; 20202) = 2. In what follows, we denote by wk the k-th concatenation
power of a word w; if k = 0, then wk will denote the empty word. For instance, for
the word w = 20 and k = 3 we have wk = 202020.
The investigation on the number of occurrences of subwords in digital expansions
along special subsequences of integers has undergone some fundamental progress in
recent times. A classical point of view, dating back to the work of Gelfond [4], is
to study the distribution in residue classes. The related sequences are automatic
sequences such as, for example, the Thue–Morse sequence or the Rudin–Shapiro
sequence. We refer the reader to [2, 5, 10, 11, 12] for an up-to-date list of the
related work.

2010 Mathematics Subject Classiﬁcation. 11A63 (primary), 11B85 (secondary).
Key words and phrases. combinatorics on words; rareﬁed sequences; maximal order of magni-
tude; Hensel’s lifting lemma.
 1

2 HAJIME KANEKO AND THOMAS STOLL

A second and diﬀerent problem is to investigate the number of occurrences of
digital blocks in these rareﬁed sequences. We will consider this problem along poly-
nomial and exponential subsequences in the present paper. We will show that for
any ﬁxed w there are terms in these rareﬁed sequences whose base-q expansion
contains not too few occurrences of w as subwords. For that purpose we will estab-
lish lower bounds on the maximal order of magnitude of the associated counting
function.
We denote the set of nonnegative integers (resp. positive integers) by N (resp.
Z
+) and use the standard Landau resp. Vinogradov notation f = O(g) resp.
f ≪ g to indicate that |f | ≤ C|g| for some absolute constant C > 0. As common,
we denote a possible dependence on the parameters in the index of the symbols.
For a better understanding of the ﬂavour of our results, let us ﬁrst give two
examples in the case of a polynomial rariﬁcation.
First, consider w′ = 0l (l ﬁxed) which is the l-th concatenation power of the
single letter 0 and let f (X) ∈ Z[X] be any arbitrary but ﬁxed polynomial of degree
d ≥ 1 with f (N) ⊂ N. Since eq(w; f (n)) ≤ log f (n)
log q for suﬃciently large n we have

lim sup
n→∞ eq(w; f (n))
log n ≤ d
log q .

On the other hand, by choosing a positive integer a such that the coeﬃcients of
f (X + a) are all positive, we have

lim sup
n→∞ eq(w; f (n))
log n ≥ lim sup
L→∞
 eq(w; f (qL + a))
log(qL + a) ≥ d
log q .

In fact, in the base-q expansion of f (qL + a) the d blocks of 0’s between consecutive
powers of q are each of length L + Oq,f (1) as L → ∞. This leads to

(1.1) lim sup
n→∞ eq(w; f (n))
log n = d
log q .

As a second example, on the other end of the spectrum, let w′ = (q − 1)
l be
the l-th concatenation power of the single letter q − 1. Theorem 1 in [12] states
that there exists N0(q, f, l) > 1 such that for all N ≥ N0(q, f, l) there is an n with
eq(w′; f (n)) = N. From the method of the proof, it follows that

(1.2) lim sup
n→∞ eq(w′; f (n))
log n ≥ 1
log q .

In fact, in the proof the author generates one block of consecutive q − 1’s, hence
also losing the factor d with respect to the previous result.
We conjecture that (1.1) holds true for any w, however, this seems to be a very
diﬃcult question.
Our ﬁrst result gives a result for general w in the spirit of (1.2) and deals with
a question posed in [12]. Denote by γ′(w) the number of occurrences of w in w2

(circular shifts) and put γ(w) = γ′(w) − 1 (for example, γ(2020) = 2, γ(0l) =
γ((q − 1)
l) = l). Note that 1 ≤ γ(w) ≤ l for all non-empty words w.

THEOREM 1.1. Let f (X) ∈ Z[X] be a polynomial of degree d ≥ 1 with f (N) ⊂ N.
Let w be a word over the alphabet Aq with length l ≥ 1. Then

lim sup
n→∞ eq(w; f (n))
log n ≥ γ(w)
l log q .

SUBWORDS IN BASE-q EXPANSIONS 3

Our second result concerns exponential functions. A famous (still open) problem
by Erd˝os says that for all suﬃciently large n the ternary expansion of 2n always
contains the digit 2. We refer to the article of Lagarias [8] and to [3] for recent and
related results. Lagarias [8, Conjecture 1.12] generalized Erd˝os’ conjecture: For all
multiplicatively independent positive integers m and q the base-q expansion of the
integers mn, n = 1, 2 . . . contain any given word w in its base-q expansion for all
suﬃciently large n ≥ n0(w). While Theorem 1.2 does not provide an answer to this
conjecture it gives a quantitative lower bound along a subsequence of integers and
therefore (up to a constant factor) the correct maximal order of magnitude.

THEOREM 1.2. Let p be a prime number, m be a positive integer not a power
of p and w a ﬁnite word over the alphabet Ap with length l ≥ 1. Then we have

lim sup
n→∞ ep(w; mn)
log n ≥ γ(w)
l log p .

In Section 2 we provide a proof of Theorem 1.1 and Section 3 is devoted to a
proof of Theorem 1.2. Both proofs are based on Hensel’s lifting lemma. For a prime
number p we use Zp for the ring of p-adic integers and Qp for the ﬁeld of p-adic
numbers; we denote by vp(u) the p-adic order of u ∈ Zp.

2. Proof of Theorem 1.1

In what follows, we suppose that w ̸= 0l since we have a better result by (1.1) in
the case of a block consisting of 0’s only. We choose a0 to be a nonnegative integer
satisfying f ′(a0) ̸= 0. We write

w = 0kwk+1 · · · wl, k + 1 ≤ l

with wk+1 ̸= 0, where all of the wi, i = k + 1, . . . , l are of length 1 (letters).

LEMMA 2.1. There exists a nonnegative integer c = c(q, f ), depending only on
q and f (X), satisfying the following: For any positive integer L, there exists a
nonnegative integer N = N (q, f, L) such that the base-q expansion of f (N ) is of
the form (f (N ))q = vwk+1 · · · wlwL−10c(f (a0))q,
where v is a ﬁnite word over Aq or the empty word.

Proof. Let q := pe1
1 · · · pet
t , where p1, . . . , pt are distinct prime factors of q and
e1, . . . , et are positive integers. Let bq,L be a nonnegative integer whose base-q
expansion is denoted as

(bq,L)q = wk+1 · · · wlwL−10c(f (a0))q,

for some c that we will determine later.
Let L′ be the length of the word wL0c(f (a0))q. For any i = 1, . . . , t, consider
the pi-adic order of an integer m by vpi (m). If c is suﬃciently large depending only
on q and f (X), then we see for any i = 1, . . . , t that

vpi (f (a0) − bq,L) > 2vpi (f ′(a0))

by f ′(a0) ̸= 0. Putting g(X) := f (X) − bq,L,
we get vpi (g(a0)) > 2vpi (f ′(a0)) = 2vpi(g′(a0)).

4 HAJIME KANEKO AND THOMAS STOLL

By Hensel’s lifting lemma [9] there exists a pi-adic integer ξi ∈ Zpi such that
f (ξi) = bq,L. Thus, for any i = 1, . . . , t, there exists an integer Ni ≤ pL′ei
i such that

f (Ni) ≡ bq,L (mod pL′ei
i ).

By the Chinese remainder theorem, there is an integer N with

0 ≤ N < pL′e1
1 · · · pL′et
t = qL′
(2.1)

and N ≡ Ni (mod pL′ei
i )
for any i = 1, . . . , t. Consequently, we obtain

f (N ) ≡ bq,L (mod qL′ ),

which implies the lemma. □

In what follows, we use the integer N constructed in the proof of Lemma 2.1
(note that N < qL′ , see (2.1)). For any positive integer L, we see by Lemma 2.1
that
 eq(w; f (N )) ≥ γ(w)(L − 2).(2.2)

By (2.1) and the deﬁnition of L′, we get

N < qL′ ≤ qlL+c′,(2.3)

where c′ = c′(q, f ) is a constant depending only on q and f (X). Thus, we obtain
from (2.2) and (2.3) that

1
l log q − c′

l log N ≤ L
log N ≤ 2
log N + eq(w; f (N ))
γ(w) log N .

Noting that N tends to inﬁnity as L tends to inﬁnity (by w ̸= 0l), we deduce the
theorem by the inequality above. This concludes the proof of Theorem 1.1.

3. Proof of Theorem 1.2

For the proof of Theorem 1.2, we ﬁrst introduce a generalization of Hensel’s
lemma and deﬁne the notation which we use throughout this section. Let p be a
prime number. For any positive integer m1 with m1 ≡ 1 (mod p), we set m1 =
1 + ape, where a, e are positive integers with p ∤ a. Put g(u) := (1 + ape)
u for any
u ∈ Zp. Let again vp(u) be the p-adic order of u ∈ Zp. It is known that for any
u, u′ ∈ Zp with vp(u − u′) ≥ N and N ∈ N, we have

vp(g(u) − g(u′)
) ≥ N + 1(3.1)

(see [7, Chapter 2, p.26]).
Let F be a function from Zp to Zp and let u ∈ Zp, s ∈ Z
+, and N ∈ N. We call
F diﬀerentiable modulo ps at u with order N if there exists ∂sF (u) ∈ Qp satisfying,
for any integer k > N and h ∈ Zp,

F (u + pkh) ≡ F (u) + pkh∂sF (u) (mod pk+s).(3.2)

Note that if we add a constant term to F , then both the diﬀerentiability of F and
the value ∂sF (u) are not changed.
In the following proposition we generalize the second statement of Corollary 2.6
in [1]. This is needed in order to consider the case where the derivative is not a

SUBWORDS IN BASE-q EXPANSIONS 5

p-adic unit. We investigated this concept for general continuous functions that are
not necessarily diﬀerentiable in [6].

PROPOSITION 3.1. Let F be a function from Zp to Zp. Let j, n, s, N be non-
negative integers with j + N < n and j < s and let u ∈ Zp. Assume that

vp(
F (u)
) ≥ n.(3.3)

Moreover, suppose for any x ∈ Zp with x ≡ u (mod pn−j) that F is diﬀerentiable
modulo ps at x with order N and that

vp(
∂sF (x)
) = j.(3.4)

Then there exists a ξ ∈ Zp satisfying
F (ξ) = 0

and
 ξ ≡ u (mod pn−j).

Proof. We construct ξ ∈ Zp satisfying the conditions of Proposition 3.1, using the
Newton method. It suﬃces to show that there exists a u1 ∈ Zp satisfying

vp(
F (u1)
) ≥ n + 1(3.5)

and
 u1 ≡ u (mod pn−j).(3.6)

In fact, u1 will then satisfy (3.3), the assumption on the diﬀerentiability, and (3.4)
with new nonnegative integers j1 = j, n1 = n + 1, s1 = s, and N1 = N because if
x ∈ Zp satisﬁes x ≡ u1 (mod pn1−j1 ), then x ≡ u (mod pn−j).
Let i be an integer with 0 ≤ i ≤ p−1. Noting that n−j > N and n−j +s ≥ n+1,
we see by (3.2) that

F (u + pn−j · i) ≡ F (u) + pn−j · i∂sF (u) (mod pn+1).

Using vp (
pn−j∂sF (u)
) = n ≤ vp(
F (u)
)
,
we ﬁnd i satisfying F (u + pn−j · i) ≡ 0 (mod pn+1).
Putting u1 := u + pn−j · i, we obtain (3.5) and (3.6). □

We now prove the diﬀerentiability of the function g(u) = (1 + ape)
u, where a
and e are positive integers with p ∤ a.

PROPOSITION 3.2. Let u ∈ Zp.
1) Suppose that e ≥ 2 or p ≥ 3. Then, for any u ∈ Zp, we have that g is diﬀeren-
tiable modulo pe+1 at u with order 0. Moreover,

∂e+1g(u) = ape.

2) Assume that e = 1 and p = 2. Let 1 + a′ · 2t := (1 + 2a)
2, where a′ and t are
integers with 2 ∤ a′ and t ≥ 3. Then g is diﬀerentiable modulo 2t at u with order 0.
Moreover, ∂tg(u) = a′2t−1.

6 HAJIME KANEKO AND THOMAS STOLL

For the proof of Proposition 3.2, we need the following auxiliary result.

LEMMA 3.3. Assume that e ≥ 2 or p ≥ 3. Let k be a nonnegative integer and
h ∈ Zp. Then we have

(1 + ape)
hp
k ≡ 1 + ahpk+e (mod pk+e+1).(3.7)

Proof. We may assume that h is a nonnegative integer because N is dense in Zp.
Moreover, it suﬃces to show (3.7) in the case where h is not divisible by p. In fact,
assume that (3.7) holds for any h ∈ N not divisible by p. Then, for any nonnegative
integer h = h′ps, where s = vp(h) ≥ 1, we see

(1 + ape)
hp
k = (1 + ape)
h′p
k+s ≡ 1 ≡ 1 + ahpk+e (mod pk+e+1),

which implies (3.7).
First, we show (3.7) in in the case of h = 1, namely,

(1 + ape)
p
k ≡ 1 + apk+e (mod pk+e+1).(3.8)

If k = 0, then (3.8) is trivial. If k ≥ 1, then the inductive hypothesis implies that

(1 + ape)
p
k−1 = 1 + ape+k−1 + cpe+k

for some integer c, and so

(1 + ape)
p
k = (1 + ape+k−1 + cpe+k)
p ≡ (1 + ape+k−1)
p (mod pk+e+1).

Since
 (1 + ape+k−1)
p = 1 + ape+k +
 p∑

j=2
 (
p
j
)(ape+k−1)
j,

we deduce (3.8), using e + k < p(e + k − 1)

by k ≥ 1, and e ≥ 2 or p ≥ 3.
Finally, if h ≥ 0 is a general integer not divisible by p, then (3.7) follows
from (3.8) by considering the binomial expansion of (1 + apk+e)
h. □

Proof of Proposition 3.2. Let k be any positive integer and u, h ∈ Zp. First, we
assume that e ≥ 2 or p ≥ 3. Using Lemma 3.3, we get

g(u + hpk) = g(u)(1 + ape)
hp
k

≡ g(u)(1 + ahpe+k) (mod pk+e+1)

≡ g(u) + hpk · ape (mod pk+e+1)

by g(u) ≡ 1 (mod p), which implies the ﬁrst statement.
Next, suppose that e = 1 and p = 2. In the same way as above, using Lemma 3.3
again, we see by k − 1 ≥ 0 that

g(u + 2k · h) = g(u)(1 + a′ · 2t)
h·2
k−1

≡ g(u) + (h · 2k) · (a′ · 2t−1) (mod 2k+t),

which implies the second statement. □

SUBWORDS IN BASE-q EXPANSIONS 7

We are now ready to give a proof of Theorem 1.2.
We may assume that m and p are coprime. In fact, if m is not coprime to p,
then putting m =: m′ps, where s = vp(m) and m′ ≥ 2, we have

ep(w; mn) ≥ ep(w; m′n).

Put mp−1 =: 1+ape and g(u) := (1+ape)
u, where a and e are positive integers with
p ∤ a and u ∈ Zp. If p = 2 and e = 1, then we deﬁne a′ and t as in Proposition 3.2.
For any ﬁnite word v = vd−1vd−2 · · · v0 on the alphabet Ap, we put

ϕp(v) :=
 d−1∑

i=0 vipi.

Moreover, for any positive integer L, let

ϕp(wL0c1) =: bp,L,

for some c that we will determine later.
Put F (u) := g(u)− bp,L for u ∈ Zp. We apply Proposition 3.1 with u = 0, N = 0,

j =
 {e if e ≥ 2 or p ≥ 3,
t − 1 if e = 1 and p = 2,

s = j + 1, n = j + 1 and put c := n − 1. Then we see

vp(
F (0)
) = vp(1 − bp,L) ≥ n,

which implies (3.3). Moreover, the assumption on the diﬀerentiability and (3.4) in
Proposition 3.1 are satisﬁed by Proposition 3.2.
Thus, Proposition 3.1 implies that there exists ξ ∈ Zp satisfying g(ξ) = bp,L. Let
L′ be the length of the word wL0c1. Then we have

L′ = lL + c + 1.

Let N be an integer with
 pL′ ≤ N < 2pL′

and
 N ≡ ξ (mod pL′).

Using (3.1), we get
 m(p−1)N = g(N ) ≡ g(ξ) = bp,L (mod pL′)(3.9)

Putting N ′ = (p − 1)N , we obtain by (3.9) and mN ′ > pL′ that

ep(w; mN ′ ) ≥ γ(w)(L − 1)(3.10)

and that
 log N ′ ≤ log (
2(p − 1)
) + L′ log p

= log (
2(p − 1)
) + (c + 1) log p + lL log p.(3.11)

Combining (3.10) and (3.11), we deduce Theorem 1.2 by letting L tend to inﬁnity.

8 HAJIME KANEKO AND THOMAS STOLL

Acknowledgements

The ﬁrst author is supported by JSPS KAKENHI Grant Number 15K17505.
The second author acknowledges the support of the bilateral project ANR-FWF
(France-Austria) called MUDERA (Multiplicativity, Determinism, and Random-
ness), ANR-14-CE34-0009.
 References

[1] E. Y. Axelsson, A. Khrennikov, Generalization of Hensel’s lemma: Finding the roots of p-adic
Lipschitz functions, J. Number Theory 158 (2016), 217–233.
[2] M. Drmota, C. Mauduit and J. Rivat, The Thue–Morse sequence along squares is normal,
submitted, available at http://www.dmg.tuwien.ac.at/drmota/.
[3] T. Dupuy and D. Weirich, Bits of 3n in binary, Wieferich primes and a conjecture of Erd˝os,
J. Number Theory 158 (2016), 268–280.
[4] A. O. Gelfond, Sur les nombres qui ont des propri´et´es additives et multiplicatives donn´ees,
Acta Arith. 13 (1967/1968), 259–265.
[5] G. Hanna, Sur les occurrences des mots dans les nombres premiers, Acta Arith. 178 (2017),
no. 1, 15–42.
[6] H. Kaneko and T. Stoll, Hensel’s lemma for general continuous functions, submitted, available
at http://www.iecl.univ-lorraine.fr/∼Thomas.Stoll/.
[7] N. Koblitz, p-adic Numbers, p-adic Analysis, and Zeta-Functions, 2nd edition, Graduate
Texts in Mathematics 58, Springer Verlag 1984.
[8] J. Lagarias, Ternary expansions of powers of 2, J. Lond. Math. Soc. (2) 79 (2009), no. 3,
562–588.
[9] S. Lang, Algebraic Number Theory, Addison-Wesley Publishing Company, 1970.
[10] C. Mauduit and J. Rivat, Prime numbers along Rudin-Shapiro sequences, J. Eur. Math. Soc.
17 (2015), no. 10, 2595–2642.
[11] C. M¨ullner, Automatic sequences fulﬁll the Sarnak conjecture, arXiv:1602.03042.
[12] T. Stoll, On digital blocks of polynomial values and extractions in the Rudin–Shapiro se-
quence, RAIRO Theor. Inform. Appl. 50 (2016), no. 1, 93–99.

Institute of Mathematics, University of Tsukuba, 1-1-1, Tennodai, Tsukuba, Ibaraki,
305-8571, JAPAN; Center for Integrated Research in Fundamental Science and Engi-
neering (CiRfSE), University of Tsukuba, 1-1-1, Tennodai, Tsukuba, Ibaraki 305-8571,
JAPAN
E-mail address: kanekoha@math.tsukuba.ac.jp

1. Universit´e de Lorraine, Institut Elie Cartan de Lorraine, UMR 7502, Vandoeuvre-
l`es-Nancy, F-54506, France; 2. CNRS, Institut Elie Cartan de Lorraine, UMR 7502,
Vandoeuvre-l`es-Nancy, F-54506, France
E-mail address: thomas.stoll@univ-lorraine.fr
