<!-- source: https://ems.press/content/serial-article-files/45026 | converted from PDF -->

Elem. Math. 52 (1997) 122 – 126
0013-6018/97/030122-5 $ 1.50+0.20/0
 c⃝ Birkha¨user Verlag, Basel, 1997

Elemente der Mathematik

Best Lower and Upper Approximates
to Irrational Numbers

Clark Kimberling

Clark Kimberling received his Ph.D. in 1970 from the Illinois Institute of Technology.
Aside from number theory, his interests include triangle geometry, playing musical
instruments, and composing.

Wherever fractional notation of the form p=q occurs in this paper, p and q denote rela-
tively prime positive integers. The rational number p=q is a best approximate to  (e.g.,
Lang [L]) if for every b=c having denominator c < q,

jq − pj < jc − bj: (1)

These conditions imply qj − p=qj < cj − b=cj < qj − b=cj; so that

j − p=qj < j − b=cj; (2)

which is to say that p=q is nearer  than any b=c having c < q. However, (1) is
stronger than (2), as exempliﬁed by (; p=q; b=c)= (1; 3=5; 1=2); in other words “best
approximate” is “better” than “nearest approximate”.
Given a positive irrational number , the principal convergents pi=qi to  are well known
to be the best approximates to ; this theorem lends itself to a lemma proved in [L]:

Lemma 1 Suppose p0=q0; p1=q1;::: are the principal convergents to a positive irrational
number .If b=c satisﬁes jc − bj < jqi − pij,then c  qi+1.

.
 Die Approximation irrationaler Zahlen durch rationale Zahlen spielt in der Zahlentheo-
rie eine grosse Rolle. Erinnert sei zum Beispiel an den beru¨hmten Satz von Liouville;
er liefert die Mo¨glichkeit, die Transzendenz einer reellen Zahl mit Hilfe ihrer rationalen
Approximationen zu beweisen. Clark Kimberling konstruiert im vorliegenden Beitrag
auf einfache Weise beste untere und obere rationale Approximationen und setzt sie in
Beziehung zu den bereits von Perron eingefu¨hrten “besten” und “na¨chsten Na¨herun-
gen”. ust
 Elem. Math. 52 (1997) 123

We modify inequality (1), calling p=q a best lower approximate to  if p=q < and for
every b=c < having c < q, q − p < c − b; (1L)

and calling p=q a best upper approximate to  if p=q > and for every b=c < having
c < q, p − q< b − c: (1U)

Before solving for p=q in these cases, we note that the analogous problem for “nearest”
lower and upper approximates is solved in Perron [P, pp. 55–63], where, ironically, they
are called “beste Na¨herungen”. Perron’s solutions are the same as those obtained below
— a surprise in view of the aforementioned nonequivalence of “nearest” and “best”.
For irrational x,let jjxjj denote the distance from x to the integer nearest to x.Let bxc
denote the greatest integer  x, and deﬁne ((x)), the fractional part of x,by ((x)) = x−bxc.
Then
 jjxjj = ˆ ((x)) if ((x)) < 1=2
1 − ((x)) otherwise, (3)

and (1) can be written as jjqjj < jjcjj:
Next we recall some basics about continued fractions, principal convergents, and inter-
mediate convergents. Suppose  has continued fraction [[a0; a1; a2;:::]], and let

p−2 = 0; p−1 = 1; pi = aipi−1 + pi−2
and q−2 = 1; q−1 = 0; qi = aiqi−1 + qi−2

for i  0. The principal convergents of  are the rational numbers pi=qi for i  0.
Now for all nonnegative integers i and j,deﬁne

pi;j = jpi+1 + pi and qi;j = jqi+1 + qi:

The fractions pi;j
qi;j = jpi+1 + pi
jqi+1 + qi ; 1  j  ai+2 − 1; (4)

are the i-th intermediate convergents of . As proved in [L, p. 16],

 < pi
qi <  < pi;j
qi;j < pi;j+1
qi;j+1 <  < pi+2
qi+2 <  if i is even; (5)

 > pi
qi >  > pi;j
qi;j > pi;j+1
qi;j+1 >  > pi+2
qi+2 >  if i is odd; (6)

and pi;j−1qij − pijqi;j−1 =(−1)j for i = 0; 1; 2;::: and j = 1; 2;:::; ai+2 − 1. If the
range of j in (4) is extended to 0  j  ai+2 − 1, then the principal convergents are
included among the intermediate convergents. We shall refer to both kinds as simply
convergents, those in (5) as even-indexed convergents, and those in (6) as odd-indexed
convergents.
Suppose now that q  1. Taking x = q in (3) gives jjqjj = jq − pj,where

p = ˆ bqc if ((q)) < 1=2
bqc + 1 otherwise, so that jjqjj = ˆ ((q)) if ((q)) < 1=2
1 − ((q)) otherwise.

124 Elem. Math. 52 (1997)

Lemma 2 If pi=qi are the principal convergents to a positive irrational number  and
i is even, then ((qi+2)) < 1=2 < ((qi+1)),

((jqi+1)) = j((qi+1)) − j + 1; (7)

and ((jqi+1)) + ((qi)) > 1 (8)

for j = 1; 2;:::; ai+2 − 1.

Proof. The ﬁrst assertion merely expresses the fact that the integer nearest qi is pi for
even i > 0, and that the integer nearest qi+1 is pi + 1. Continuing, it is well known
([L, p. 8]) that pi+1 − qi+1< 1=qi+2;

so that ((qi+1)) > 1 − 1=qi+2.Now ai+2  ai+2qi+1 + qi = qi+2, whence

0 < j((qi+1)) − j + 1 < 1for 1  j  ai+2 − 1:

Since ((jqi+1)) is an irrational number having the same fractional part as j((qi+1)) −
j + 1, identity (7) is proved. Continuing,

pi+2qi+1 − qi+2pi+1 = −1 < 0 = pi+2qi+2 − qi+2pi+2;

so that > pi+2
qi+2 > pi+2 − pi+1
qi+2 − qi+1 :

Then (ai+2qi+1 + qi − qi+1) > ai+2pi+1 + pi − pi+1, which implies

((qi))
1 − ((qi+1)) = qi − pi
pi+1 − qi+1 > ai+2 − 1:

Thus for 0  j  ai+2 − 1, we have

j(1 − ((qi+1))) < ((qi));

so that j((qi+1)) − j + 1 +((qi)) > 1;

and (8) follows from (7). h

Lemma 3 If pij=qij are the convergents to a positive irrational number  and i is even,
then

((qi0)) > ((qi1)) > ((qi2)) >  > ((qi;ai+2−1)) > 1 − ((qi+1;0)) > ((qi+2;0)):

Elem. Math. 52 (1997) 125

Proof. When j = 0, we are dealing with principal convergents, hence best approximates
to ,so that jjqi0jj > jjqi+1;0jj > jjqi+2;0jj;

or equivalently, ((qi0)) > 1 − ((qi+1;0)) > ((qi+2;0)):

Next, using Lemma 2, we ﬁnd for j = 0; 1;::: ; ai+2 − 2that

((jqi+1)) = j((qi+1)) − j + 1 > (j + 1)((qi+1)) − (j + 1)+ 1 =(((j + 1)qi+1));

so that ((qij)) > ((qi;j+1)). Finally,

1 − ((qi+1)) = pi+1 − qi+1< 1=qi+2 < 1=ai+2;

whence ai+2((qi+1)) > ai+2 − 1, and

((qi;ai+2−1)) = (ai+2 − 1)((qi+1)) − (ai+2 − 1)+ 1 > 1 − ((qi+1)): h

Theorem 1 The best lower approximates to a positive irrational number  are the
even-indexed convergents to .

Proof. Suppose qij is an even-indexed convergent, and c is a positive integer such that
((c)) < ((qij)). Wewishtoshow that c > qij. By Lemma 3, ((c)) < ((qi)),sothat
jjcjj < jjqijj, which by Lemma 1 implies c  qi+1.If c = qi+1,then ((c)) = ((qi+1)),
whichbyLemma 3implies
 ((c)) > 1 − ((qij)) > ((qij));

a contradiction. Also, clearly, c 6= qij, so it remains to consider the possibility that
qi+1 < c < qij; write c = mqi+1 + h,where 1  h < qi+1 and 1  m  j.Then

((c)) = ((mqi+1 + h));

and, using Lemma 2,

((mqi+1)) + ((h)) − 1 =((c)) < ((qij)) = ((jqi+1 + qi)) = ((jqi+1)) + ((qi)) − 1;

so that ((h)) < ((jqi+1)) − ((mqi+1)) + ((qi)):

Identity (7) easily gives ((jqi+1))  ((mqi+1)),so that ((h)) < ((qi)), and by Lemma
1, h > qi+1, a contradiction. h

Lemma 4 Let pi=qi denote the principal convergents to a positive irrational number
 =[[a0; a1; a2;:::]], and let p
0
i=q
0
i denote the principal convergents to the number 0 =
a0 + 1 − .If  − a0 < 1=2,then p
0
0=q
0
0 = 0=1, p
0
1=q
0
1 = 1=1, and

p
0
i
q0
i = (a0 + 1)qi−1 − pi−1
qi−1
for i = 2; 3;:::.If  − a0 > 1=2,then a1 = 1, p
0
0=q
0
0 = 0=1, p
0
1=q
0
1 = 1=(a2 + 1), and

p
0
i
q0
i = (a0 + 1)qi+1 − pi+1
qi+1
for i = 2; 3;:::.

126 Elem. Math. 52 (1997)

Proof. It is easy to verify that

0 = ˆ [[0; 1; a1 − 1; a2; a3; a4;:::]] if  − a0 < 1=2
[[0; a2 + 1; a3; a4;:::]] if  − a0 > 1=2.

The rest of the proof is routine and omitted. h

Theorem 2 The best upper approximates to a positive irrational number  are the
odd-indexed convergents to .

Proof. Suppose pij=qij is an odd-indexed convergent to . Suppose also, contrary to
(1U), that there exists b=c, with denominator c < qij, such that

pij − qij  b − c:

Substituting a0 + 1 − 0 for  and using principal convergents, we then have

(jpi+1 + pi) − (jqi+1 + qi)(a0 + 1 − 0)  b − c(a0 + 1 − 0);

(jqi+1 + qi)0 −  j(
(a0 + 1)qi+1 − pi+1 +(a0 + 1)qi − pi  c0 − (ca0 + c − b):
(9)
If  − a0 < 1=2, then by Lemma 4, inequality (9) can be written as

(jq
0
i+2 + q
0
i+1)0 − (jp
0
i+2 + p
0
i+1)  c0 − (ca0 + c − b);

so that q
0
i+1;j0 − p
0
i+1;j  c0 − (ca0 + c − b);

contrary to Theorem 1, since p0
i+1;j=q
0
i+1;j is an even-indexed convergent to 0 and

c < qij = jqi+1;j + qi = jq
0
i+2;j + q
0
i+1 = q
0
i+1;j:

On the other hand, if  − a0 > 1=2, then (9) can be written as

(jq
0
i + q
0
i−1)0 − (jp
0
i + p
0
i−1)  c0 − (ca0 + c − b);

so that q
0
i−1;j0 − p
0
i−1;j  c0 − (ca0 + c − b);

contrary to Theorem 1. h

References

[L] Serge Lang, Introduction to Diophantine Approximations, Addison-Wesley, Reading, Mass., 1966.

[P] Oskar Perron, Die Lehre von den Kettenbru¨chen, Chelsea, New York, 1950.

Clark Kimberling
Department of Mathematics
University of Evansville
1800 Lincoln Avenue
Evansville, Indiana 47722
