<!-- source: https://www.renyi.hu/~p_erdos/1979-22.pdf | converted from PDF -->

Some Unconventional Problems
in Number Theory

A mélange of simply posed conjectures
with frustratingly elusive solutions .

PAuL Eenós

Hungarian Academy of Sciences

Universip' of Colorado

Boulder, CO 80309

I state some curious, unusual, and mostly unsolved problems in various branches of number
theory.

Factorial Powers

1. Put f(n) =E(l/p) for p<n and p}(2n ) . In a previous paper 16] written with Graham,

Ruzsa and Straus, we conjectured that there is an absolute constant C so that for all n,f(n)<C . I

further conjectured for n > 4, ( 2n) is never squarefree. It is surprising that this simple conjecture

presents so many difficulties .

Since ( 2n) 0 (mod 4) except if n = 2k, we "only" have to prove that ( 2*
 ) is divisible by

the square of an odd prime for k > 3 . But this does not seem easy. I conjecture that for k>8 . 2k

is not the sum of distinct powers of 3 . (However, 28=256=3 5+3 2 +3+ 1 .) This conjecture would

imply that for k > 9 ( 22k 1 -0 (mod 3), but as far as I see there is no method at our disposal to

attack this conjecture. There is no doubt that for n >no(k,a), ( 2n )=0 (mod p°) for some p > k .

For p > 2.p21
(171 ) and there is a good chance that this is the greatest (2n ) with this property .

In other words, for n > 171, the number ( 2n) is perhaps divisible by the square of an odd prime .

2. Let M(n ; k) = jn + 1, . . . , n + k] be the least common multiple of the integers n + i for

I < i 5 k. 1 conjecture that for m > n + k, M(n ; k) zM(m ; k), or more generally for I > k and
ni> n + k, M(n ; k) ~ M(m ; l). Unfortunately, I do not see any method to attack these very

attractive conjectures . Probably M(n ; k) = M(m ; 1) has very few solutions when m > n + k and

1 > 1 . 1 only know M(4 ; 3) = M(13 ; 2) and M(3 ; 4) = M(19; 2). If, similarly, we put A(n ; k)-

I1`_,(n+i), then I conjecture also that A(n ;k)=A(m ;l) probably has very few solutions for
m ;?n+k and 1>1 .
Suppose that k>3 and m > n + k . Observe that then, for each k, M(n ;k) > M(m ; k)

has infinitely many solutions. Yet I cannot decide whether the same is true for M(n ; k) >
M(m ; k + 1). (The referee found two solutions, namely M(96 ; 7) >M(104 ;8) and M(132; 7) >
M(139 ;8).) Let nk denote the smallest solution of M(n ;k) >M(m ; k) . Try to determine or

VOL . 52, NO . 2, MARCH 1979
 AIZiCLE.

67

estimate n,, . It is almost certainly the case that nk/k-aoo and perhaps this will not be difficult to
prove. It would be worthwhile to compute nk for small values of k, for perhaps then one can
formulate some reasonable conjectures . (Added in proof: nk/k-+oo is indeed easy, but I have no
good upper bound for nk.)
Let uk be the smallest integer for which M(uk,k) > M(uk + I ;k). It is easy to see that

uk - (1 + o(1))k and uk> k . It seems to me that if t < uk and T > t then M(t ; k) < M(T; k).
Perhaps I overlooked a simple argument but I could not prove this.

Unustud Sieve Processes

3. Consider the integers of the form

n -ape + b, where a > 1,0 < b <p, and p is prime .

 (1)

It is easy to see by the sieve of Eratosthenes that almost all integers n are of the form (1), but I
could not prove that every sufficiently large integer is of this form. In fact, this seems rather

unlikely. In view of this I hoped that perhaps the equation

n - akt + b, where a > 1,0 -<b < k, k is an integer, k > 2

 (2)

would be solvable for every sufficiently large n . Selfridge and Wagstaff made a preliminary
computer search and in their opinion it is quite possible that (2) is not solvable for infutitely
many n. It would be interesting to find some large (say of size 10'3 or larger) values of n not of

the form (2). Denote by g(x) the number of integers n <x not of the form (1), and by G(x) those
not of the form (2). Clearly G(x) < g(x) . It follows from the Brun-Selberg Sieve that g(x) <

c,x(logx) _. Probably G(x) <x` for x >xo(c) for some c > 0, and perhaps for all c >0 .
Let u, <u2, . . ., be an infinite sequence of integers. It is probably not difficult to prove that

the density of integers not of the form n=ate+b for a > 1 and 0<b <u; exists and is positive if

~l/t~ converges and is 0 otherwise. More generally (1) could be replaced by the equation

n = au? + b, where a > 1 and 0 < b < A

 (3)

and one could try to find non-trivial conditions on u, <u2 < • • • and v, <v2 < . . . that (3)

should be solvable for all sufficiently large n. I am not very hopeful of success. There is more

hope if we only insist that almost all n should be of the form (3).

Barriers

4. Let f(m) > 0 for 1 < ;r. < oc be any positive function defined on the integers. Then n is

called a barrier for f(m) if for all m < n, m + f(m) < n . Clearly ¢+(m) and a(m) do not have barriers
because they increase too fast . Let V(m) be the number of distinct prime factors of m . Probably
V(m) has infinitely many barriers, but I am very far from being able to prove this . I cannot even

prove that there is an e > 0 for which eV(m) has infinitely many barriers. One could try to attack
this problem by sieve methods, but it seems to me that these methods are not strong enough at
present .
Let 9(m) be the number of prime factors of m, multiple factors counted multiply . It seems
certain that 0(m) also has infinitely many barriers . But this, if true, is certainly unattackable by

present day methods. Selfridge observed that n=99840 is the largest barrier for 0(m) less than

105. Selfridge and I then investigated d(n), the number of divisors of n. Since max(d(n-1)+n-1,
d(n - 2) + n -2) > n + 2, the most we can hope here is that for infinitely many n,

max (m + d(m)) - n + 2 .

 (4)

It is extremely doubtful whether (4) has infinitely many solutions . In fact it is quite possible that
lim max (m + d(m) - n) = oo. Selfridge and I observed that 24 satisfies (4) and we convinced
n + Cc M <n
ourselves that if there is an n > 24 which satisfies (4), then this n must be enormously large, far
beyond the range of our tables or computers .
It is not difficult to show that the product F(m)=Ha; (where m-Ilp;4) of the number of

prime factors of m has infinitely many barriers .

68 MATHEMATICS MAGAZINE

Translation Properties

5. Denote by A the sequence 1 <a, <a2< A is said to have the translation property if for
every n there is a r„ > 0 so that u is in A if, and only if, u + t„ is in A for every I <u < n. It is not
hard to show that the squarefree numbers have the translation property . (II& must have been
known, although perhaps it does not appear in this form in the literature .) More generally let
b, <b 2< . . . i where (b„ b,) - 1 and E I / b; < oo, and let A be the sequence of integers not
divisible by any of the b's. It follows easily from the sieve of Eratosthenes that A has the
translation property .
If the condition 7.1/b, < oo is dropped, the situation is much more complicated . If
Xb<x(1/b,)=o(loglogx), then it can be deduced by Brun's method that A has the translation
property. If this condition is also dropped, I have no non-trivial result . I do not know if the
integers which are sums of two squares have the translation property . I do not know what
happens if we divide the primes into two disjoint classes q, <q2< • ' • ; and r, <r2< • • • , both
having for every x more than cx/logx terms not exceeding x . Denote by Q,<Q2< . . . the
integers composed of the primes q, <q2< • • • . Can the sequence Q, <Q 2< . . . have the
translation property? Let p, <p2 < . . . be the sequence of all primes. It is not hard to show that

Pk <Pk+I < • • • can never have the translation property .
Let A have the translation property. The task of determining the smallest t„ which satisfies
the definition of the translation property for A will not be easy. For example, if A is the
sequence of squarefree numbers, I expect that t„ >expn` . I am quite sure that t„ increases faster
than poiynomially; perhaps this will not be hard to prove .

6. It is extremely difficult to obtain results on the difference of consecutive primes . A
well-known conjecture of Cramer states that

limsu A,+I -A, - 1
n-00 (logn)z

This conjecture is completely unattackable by present day methods and I expect that it will stay
in this class for a very long time .
Let Q I < Q2 < . . . be the sequence of consecutive squarefree numbers . It is curious that
Q~+ I - Qn is almost as difficult to study as p.., I - pn . The best upper bound is, as far as I know,
still due to Richert and Rankin [10, 111 who proved that for every e > 0 and n >%, Qn+ I - Qn <
n'~` There is no doubt that this inequality holds with 2/9+e, replaced by e, but the proof is
nowhere in sight. Perhaps Qn+ I - Q n < c logn holds, but I am very doubtful. It is easy to see that

limsup(Q.+I -Q„)ioglogn(logn) -1 >rr2/6

and as far as I know this has never been improved .
I proved (in [51) that for 0 < a < 2,

lim x Y, (Q.+I-Q.)a=C4
X 00

 Q„ < x

and Hooley recently proved [81 that (5) holds for a < 3 . No doubt (5) holds for every a .

Miscellaneous Problems

7. There are many unconventional problems connected with the divisors of n. R . R. Hall and
I have a long paper on this subject . Here I just state a conjecture of mine which is more than
forty years old : The density of integers n which have two divisors d, <d2<(1 +e)d, is I for every

e > 0. I can prove that the density exists, but cannot prove that it is 1, even for large values of e .
A much stronger and more recently formulated conjecture is as follows : Denote by d '(n) the
number of integers k for which n has at least one divisor t where 2' <t <2"' . Then for almost
all integers n.d+(n)/d(n)- .0 as n-+oe .

n- co
 (5)

VOL . 52, NO. 2, MARCH 1979

 69

S. Let h(n) be the smallest integer so that every µ, where I < µ <n!, is the sum of h(n) or

fewer distinct divisors of n! . I proved h(n) < n. The proof by induction is easy. No doubt very
much more is true : At(n)=o(n) and probably h(n) - o(n`) and hopefully h(n) < (loge)° for some

c. (I was lead to h(n) by studying b - I +

 + I where x, < . . . < xk and k is minimal .)
X,

 Xk

9. An old conjecture of Strauss and myself states that for every n > 3

4

 1

 I

 1

P!

 x 1

 x2

 x 3

is solvable in integers x 1,x2,x3 where l <x, <x2 <x3 . This conjecture seems surprisingly difficult .
A forthcoming paper of Strauss and Subbarao deals with some related questions .

10. Forty years ago I asked : does x - z ° have any nontrivial solutions in integers? Chao
Ko found infinitely many solutions [I]; perhaps he found them all .

11. Put pk +, - pk = dk (where ( pk ) is the sequence of primes). Turan and I proved that both

dk+I >d1 and dk+I <dk have infinitely many solutions. But we could not prove that at least one

of the inequalities dk+2 >dk,, >dk and dk+2 <dk+, <dk has infinitely many solutions. If our
conjecture is false then, as we observed, there is a k o so that for k>k o,dk+ ,-dk alternates in

sign. This is certainly not the case and perhaps the proof is not hard . I offer 100 dollars for a
proof or disproof.

12. Let 1= r, < . . . <r o(„)= n - 1 be the 0(n) integers relatively prime to n . I conjectured
nearly forty years ago that there is an absolute constant C so that

$(R) - 1

 2

i (r,+i_rr)2<Cn) •

 (6)
.-t

This does not look hard, but it has not yet been settled and I offer 250 dollars for a proof or
disproof. No doubt (6) holds if 2 is replaced by any positive a (C must then be replaced by Q .
Hooley proved this for a < 2 .

This paper is based on remarks presented at the fifth annual Mathematics and Statistics Conference in
October, 1977, at Miami University in Oxford, Ohio .

Referemea

(1) Ko Chao, Note on the diophantine equation x'j Y-z', J. Chinese Math. Soc., 2 (1910) 205-207 (Math . Rev.
V . 2, p. 346).
121 P. Erd6s, On the density of some sequences of integers, Bull . Amer. Math. Soc., 54 (1948) 685-ó92 .
(3)	 On the difference of consecutive primes, Bull. Amer. Math Soc., 54 (1948) 885-889.

(41	 , On the equation X1 + . .. + k - b (in Hungarian), Mat. iapok, 1 (1950) 192-210. (MR 13, p.

208.)
(5)

 ,Some problems and results in elementary number theory, Publ. Math. Debrecen, 2 (1931) 103-109.
(MR 13, p. 627.)

(6)

 , R L. Graham, 1. Z Ruzsa and E Straus, On the prime factors of ( 2~ ), Math. Comp, 29 (1975)
83-92.

(7)

 , and P. Turan, On some new questions on the distribution of prime numbers, Buli. Amer. Math.
Soc., 54 (1948) 271-278.
[81 C Hooley, On the intervals between consecutive terms of sequences, Proc. Symp. Pure Math. XXN.
Analytic Number Theory, Amer. Math. Soc., 1973, 129-140.
[9) W. H. Mills, Number theory conference, Boulder, Colorado, 1959 .
[10] R A. Rankin, Van der Corpus's method and the theory of exponent pairs, Quart . J. Math., 6 (Ser. 2) (1955)
147-153 .
[1l) H. E Richert, On the difference between consecutive squarefree numbers, J. London Math. Soc., 29 (1954)
16-20.

70

 MATHEMATICS MAGAZINE
