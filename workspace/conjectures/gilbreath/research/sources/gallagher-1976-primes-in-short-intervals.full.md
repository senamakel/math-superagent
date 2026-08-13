<!-- source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/DCE557AC8750333E68426FCEEC11858C/S0025579300016442a.pdf/div-class-title-on-the-distribution-of-primes-in-short-intervals-div.pdf | converted from PDF -->

ON THE DISTRIBUTION OF PRIMES IN SHORT
INTERVALS

P. X. GALLAGHER

One of the formulations of the prime number theorem is the statement that the
number of primes in an interval (n, n + ft], averaged over n ^ JV, tends to the limit A,
when JV and h tend to infinity in such a way that h ~ AlogJV, with A a positive
constant.
In this note we study the distribution of values of n(n + h) — n(n), for n < N
and h ~ A log JV. We show that, assuming a certain uniform version of the (unproved)
prime r-tuple conjecture of Hardy and Littlewood [3], the distribution tends to the
Poisson distribution with parameter A as N -* oo. Using a sieve upper bound for the
r-tuple problem, we also get an unconditional exponential upper bound for the tail
of the distribution.
Our method has many features in common with the argument by which Hooley [4]
has studied the distribution of values of the differences between consecutive integers
prime to n, for «/$(«) large. An analogous result for primes has been announced by
Hooley in [5].
Explicitly, the r-tuple conjecture is an asymptotic formula for the number 7rd(JV)
of positive integers n < JV for which n + du ..., n + dr are all prime. Here
du ..., dr are distinct integers. The formula is

provided ^"d ^ 0, where

and where vd(p) is the number of distinct residue classes mod p occupied by dt,..., dr.
Formula (1) is the prime number theorem, for r = 1. For r ^ 2, it has not been
proved for any d; the source of (1) in these cases is a heuristic application of the
circle method, and a summation of the corresponding (multiple) singular series [3].
Lavrik [8] has proved that (1) holds in mean over cubes 1 < du ...,dr < H, in the
range JV/log
ciV < H < JV"; a similar mean result for the (small) cubes of side h would
suffice for our purpose.

THEOREM 1. Denote by Pk(h, N) the number of integers n < JV for which the
interval (n, n + h] contains exactly k primes. Then
 (2)

for N -» oo, h ~ AlogJV, provided, for each r, (1) holds, uniformly for
1 < du ...,dr < h, withdu ..., dr distinct and Sf& =£ 0.

[MATHEMATIKA 23 (1976), 4-9]

https://doi.org/10.1112/S0025579300016442 Published online by Cambridge University Press

ON THE DISTRIBUTION  OF  PRIMES  I N  SHORT INTERVALS  5

Our argument for (2) goes through a computation of the  moments of
n(n +  h) — n(n), and depends on the fact that, for each r, yd averages to 1 over cubes:

£ 3> d~h' (A-•oo). (3)
lidi d r4h
distinct
For r = 2, a smoothed variant of this was used by Hardy and Littlewood to refute
earlier asymptotic Goldbach conjectures. A  simple proof of (3) for r = 2, starting
with the singular series representation for £?d, was given by Bombieri and Davenport
in [1]. Our proof of (3) starts with the product definition of £fd, and is closer to an
argument of Hooley in [5].
Using Selberg's sieve, Klimov [7] obtained for each r the upper boundf

^ (4)
log'JV

for N -> oo, uniformly for d in small cubes. For this, see Halberstam and Richert [2],
Theorem 5.7. Using (4) instead of (1), we get upper bounds for the kth moments of
n(n + h) —  n(n) for n < N, as Bombieri and Davenport did for k — 2. For large k,
these bounds give

THEOREM  2. For positive constants \i > X >  I, the number of n < N for which
n(n + XlogN) — n(n) >  n is <, Ne~
c>t'
x, where C is an absolute constant.

1. Reduction to (3). For each positive integer k,

£ (n(ri + h)- n(n))
k =  £ £ 1
n<N n^N  n<pi, ...» pfc<n +  fc

where the inner sum is over all r-tuples du ..., dr satisfying 1 <  dt < ... < dr <  h,
and a{k, r) is the number of maps from the set {1, ..., k} onto {1, ..., /•}. For the d
with £fd # 0, we use (1); for the others, dlt ..., dr occupy all residue classes modulo
some prime, so nd(N) < r. Using (3), it follows that

_ h
r N

^ "
 Or% ' r ! log'N
and hence
 1 N
J {n{n + h) - «(«))* - ^(A), (5)

with

In §3, it is shown that mk(X) is the kth moment  of the Poisson distribution with

t Th e  notation Fg C stands fo r fim  F/G  <  1.

https://doi.org/10.1112/S0025579300016442 Published online by Cambridge University Press

6 P. X. GALLAGHER

parameter A, and that the corresponding moment generating function is entire. The
result (2) now follows from general theorems on moments [6, Chapter 4].
Putting h = AlogJV, and using (4) instead of (1), we get

!>„ . *r(N)£ (2XTN,

from which it follows that

-J- £ (*(« + h) - «(«))* £ £ o{k, r)(2Xf
N n= l r= l
sj k(2Xkf.

Hence the proportion of n < JV for which n(n + h) — n(n) > \i is <, k(2kX/fi)
k. If
nlX > 4, we choose k = [i(///A)]. Then A: > $(fi/X), so the proportion is

If fi/X < 4, the result is trivial.

2. Proof of {T). Let Ai = I ! Wi - dj).

Then 1 < vd(p) ^ r, with equality at the right, unless p | Dt. The pth factor in ^ d is

1 + — = 1 + a(p, vt(p)), (6)
(P ~ 1)
where f(p - I)- 2, v = r;
fl(p,v)<P (7)
[(p-l)- 1 , v<r .

It follows that the product for SfA converges. Defining aA(q) for squarefree q by

aA(q) = El a(P'
 VI(P

we get an absolutely convergent series expansion

^d = £ a*(«), (8)

where the sum is over squarefree #.
We need an estimate for the remainder in (8) which is uniform for d in the A-cube.
It follows from the bounds on a(p, v) that

q>x q>x <p (q)

where co(q) is the number of prime factors of q, and C is a positive constant depending
only on r. Puttingq = de with d\D and (e, D) = 1, this is

dfo 4>(d) e-zin <j)
2(e) d\D <j)(d) x
(e , r>) = l <^ (xhY/x,

https://doi.org/10.1112/S0025579300016442 Published online by Cambridge University Press

ON THE DISTRIBUTION OF PRIMES IN SHORT INTERVALS 7

with a constant depending only on r and e. It follows that +A (_ - .>

5^ = Z , ^ <h
aM + o(ff((xhy/x)), (9)

distinct distinct
with a constant depending only on r and G.
The inner sum in (9) is
I  n <p,

v pi ,
where ]T'l stands for the number of r-tuples of not necessarily distinct integers
dt dT with 1 <: du ...,dr < h which, for each prime p\q, occupy exactly v(p)
residue classes mod p; the outer sum is over all "vectors " = (..., v(p), ...) p|, with
components satisfying 1 < v(p) < p. A simple lattice point argument using the
Chinese remainder theorem gives, for q < h,

the product representing the number of ways of choosing the residue classes of
du ...,dr mod q subject to the congruence restrictions in £' .
Thus the inner sum in (9) is

\ —) A(q) + O\ [ —) B(q) | + O(h
r~
i C(q)), (10)

with
 A(q)= ina(p,v(p))(
 P

B(q) =
 v P I i

We have
 v f u \ v(p)

C(q) =

A{q)= n ( f «(P>

= n \t
P\q

C(q)= Tl I t |a(p,v)|).

We show first that A(q) = 0 for g > 1. Using (6), the pth factor in A(q) is

(P ~ !)-'((/ - (P - 1)0 f ( ^ )«r(r, v) - p- 1 t v(P Wr, v)) .
I v=i \ v / v = i \ v / ;

https://doi.org/10.1112/S0025579300016442 Published online by Cambridge University Press

8 P. X. GALLAGHER

By formulae (i) and (ii) of §3, the two sums here are p
r and p p+ 1 — (p — Vf p respec-
tively, and the factor vanishes.
Using the bounds (7) for a(p, v), we may estimate B(q) and C(q). By (i) of §3, the
pth factor in B(q) is <^ p'/(p — 1), so

B(q) < C<°«

More simply, the pth. factor in C(q) is <^ p/(p — 1), so

Returning to (9) and (10), it follows that (9) is h
r plus a remainder term which is

+ h
r(xhyixf'
1 £ Cra(9)—

h
r(hxY/x

choosing x = A*. Since x < A, the conditions <j < //, assumed earlier, are satisfied.

3. Combinatorial identities. We prove here the standard identities for the
" Stirling numbers of the second kind " o(k, r)/rl which have been used above. These
are
 S ( ^ )r , v) = / + 1 - (p -

' A
v «
(iii) X o(r,v)—= S
v=i v! p=o

r=o r! = e

the last two identities show that mr(A), the left side of (iii), is the rth moment of the
Poisson distribution with parameter X, and that the corresponding moment generating
function (iv) is entire.
To prove (i), classify the maps from {1, ..., r} to {1,..., p) by the size of the image.
There are (?) subsets of size v in {1, ...,p}; for each such subset, the number of maps
with this image is a(r, v). To prove (ii), write

https://doi.org/10.1112/S0025579300016442 Published online by Cambridge University Press

ON THE DISTRIBUTION OF PRIMES IN SHORT INTERVALS

and use (i). To prove (iii), multiply (i) by X
p\p\ and sum over p:

r oo

T ff(r,v) Y

From this and
 v J p \ v!

the identity (iii) follows. To prove (iv), multiply (iii) by z
rjr[ and sum over r.

References

1. E. Bombieri and H. Davenport. " Small differences between prime numbers ", Proc. Roy. Soc.
Ser. A. 293 (1966), 1-18.
2. H. Halberstam and E. Richert. Sieve Methods (Academic Press, 1974).
3. G. H. Hardy and J. E. Littlewood. " Some problems of ' Partitio Numerorum': III. On the
expression of a number as a sum of primes ", Acta Mathematica, 44 (1922), 1-70.
4. C. Hooley. " On the difference between consecutive numbers prime to n. II" , Publ. Math.
Debrecen, 12 (1965), 39-49.
5. C. Hooley. " On the intervals between consecutive terms of sequences ", Proc. Symp. Pure
Math., 24 (1973), 129-140.
6. M. G. Kendall and A. Stuart. The Advanced Tlieory of Statistics, Vol. I (Griffin, 1958).
7. N. I. Klimov. " Combination of elementary and analytic methods in the theory of numbers ",
UspehiMat. Nauk, 13 (1958), no. 3 (81), 145-164.
8. A. F.Lavrik. " On the theory of distribution of primes, based on I. M. Vinogradov's method of
trigonometrical sums ", Trudy Mat. lnst. Sleklov., 64 (1961), 90-125.

Mathematics Department 10H15: NUMBER THEORY; Multiplicative
Columbia University Theory; Distribution of primes.
New York, New York 10027 (U.S.A.). Received on the 10th of October, 1975.

https://doi.org/10.1112/S0025579300016442 Published online by Cambridge University Press
