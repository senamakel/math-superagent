<!-- source: https://www.ams.org/journals/proc/1970-025-03/S0002-9939-1970-0256984-9/S0002-9939-1970-0256984-9.pdf | converted from PDF -->

ON  1/n  = l/x+l/y+l/z

WILLIAM  A.  WEBB

Abstract.  It  is  shown  that  the  number  of  positive  integers
n^N  for  which  4/w  =  l/x  +  l/y  +  l/z  is  not  solvable  in  positive
integers,  is  less  than  a  constant  times  iV/(log  N)114.

I.  Introduction.  Erdos  has  conjectured  that  the  equation

(I)  4/w  =  1/x  +  1/y  +  1/z

is  solvable  in  positive  integers  for  all  integers  «^2.  This  has  not  as
yet  been  proved,  but  it  is  known  that  (I)  is  solvable  for  n  less  than
some  constant  [l],  [2],  [5].  Using  the  methods  found  in  these  works
and  some  fairly  advanced  analytic  techniques,  it  can  be  shown  that
S(N)<^N/(log  N)a  where  a  is  a  constant  less  than  one,  and  S(N)  is
the  number  of  positive  integers  n  less  than  N  for  which  (I)  is  not
solvable.  In  this  paper  it  is  shown  that  better  estimates  can  be  ob-
tained  using  methods  which  are  essentially  elementary.

II.  Principal  results.  By  looking  at  the  problem  somewhat  differ-
ently,  we  are  able  to  obtain  various  conditions  on  n  which  imply  the
solvability  of  (I),  and  then  apply  sieve  methods  to  obtain  an  upper
bound  for  S(N).  The  basic  lemma  needed  is  the  following:

Lemma  1.  a/b  =  1/x  +  l/y  if  and  only  if  there  exist  divisors  di  and  d2
of  b  such  that  a\  (di+d2)  (a,  b,  x,  y  positive  integers).

A proof  of a generalized  form  of the  above  lemma  may  be  found  in  [6 ].
We  will  illustrate  the  method  by  considering  primes  modulo  8.

Lemma  2. Let  p  be a  prime,  then  (I)  is  solvable  if:
(i)  p =  7 (mod  8) and  n = 0 (mod  p)  or n+l  =  0  (mod  p)  or  w+2=0
(mod  p)  or 2n+l  =  0  (mod  p)  or
(ii)  p = 3 (mod  8) and  n = 0  (mod  p)  or w-fT^O  (mod  p)  or
(iii)  p =  5  (mod  8)  and  n = 0  (mod  p).

Proof.
Case  (i).  Let  p = 8t +  7, and  r = 2(t +  l).  Then

4/»  =  1/rn  +  p/2(t  +  l)n.

Received  by  the  editors  April  18,  1969 and,  in  revised  form,  November  21,  1969.
A MS  Subject  Classifications.  Primary  1010; Secondary  1064.
Key  Words  and  Phrases.  Diophantine  equation,  divisors,  residue  classes,  Selberg's
sieve. 578

on  4/»=  l/x+l/y+l/2  579

If  p\n,  the  last  fraction  is  reducible  and  (I)  is  solvable  trivially.
(Note:  l/x  =  l/(x-f-l)+l/x(x  +  l).)  To  obtain  the  other  conditions,
apply  Lemma  1  to  the  following  pairs  of  divisors  of  2(t +  l)n:  n  and
1, n  and  2,  2»  and  1.
Case (ii).  Let  p = it+3,  and  r = t +1.  Then

4/m  =  1/rn  +  p/(t  +  l)n.

If  p\n,  p/(t+l)n  is  reducible;  and  if  p\n  +  l  apply  Lemma  1.
Case  (iii).  If  p = 5  (mod  8),  p +  l=6  (mod  8)  which  implies  that
p +  1  has  a  prime  divisor  q  such  that  q = \r  — l.  Then

4/w  =  1/rre  +  <?/»■«.

If  p\n,  then  o|^  +  l  and  both  p  and  1  divide  the  denominator  of
the  last  fraction.  Therefore  we  may  apply  Lemma  1 again.

Theorem  1. S(N)«N/(log  N)7'*.

Proof.  We  apply  Selberg's  sieve  to  the  positive  integers  g  N,  where
the  sifting  classes  for  a  given  prime  are  those  given  for  n  in  the  state-
ment  of  Lemma  2.  (Note  that  these  residue  classes  are  distinct.)
In  particular,  we  apply  Theorem  3,  p.  213  of  [3],  which  states  that

S(N) ^ NQ-i + z TJ (l  -  ttV  / 2
»e<P \  f(P)  I

where (P =  {p I p is a prime  g  N, p  ^  1  (mod 8), p  y± 2},

ft  =  {n I w is  a  positive  integer  ^  iV},

f(p)  =  />/4       Up  =  1  (mod 8)

=  j>/2        if  /> sa 3  (mod  8)

=  p  \l  p  =  S  (mod  8),
n»  -up,

/(<*) = n/(p)      forrfinw,
P\d
T> =  {d\d  divides II(<P)» rf =  z1/2},

z  =  TV2'3,
e = Q(»)= E-Jjr'
deD     g(0)

and

580  W. A. WEBB  [July

provided  \Ra\  ^=d/f(d)  where

E       1 =  N/f(d)  +  Rd

n€G;<i!ff(7i)

and  o"(«) =  YlPi  where  the  product  is  over  all  primes  pt  which  are
moduli  of  sifting  classes  containing  n.
If  d=pip2  ■ ■ ■ pT,  then

E       1 =  number  of n  ^  N  which  are  sifted  by
nea;d|(7(n) pi,  p2,  ■ ■ ■ , and  p,,

=  number  of  n  ^  TV which  satisfy  a  system  of

congruences:
(II) n  =  hi  (mod  pi)

n  =  hi  (mod  pi)

n  =  hr  (mod  pi)

where  hi  is  any  one  of  the  pi/fipi)  residue  classes  sifted  by  our  sieve.
The  system  (II)  is  equivalent  to  a  congruence

n  =  Hj  (mod  d)

and  there  are  (pi/f(pi))  •  •  •  (pr/f(pi))=d/f(d)  such  congruences.
For  each  such  congruence  there  are  iN/d+Ef)  n  which  are  ^TV  and
satisfy  the  congruence,  and  \Ej\  :£ 1.  Therefore

dlf(d)  ]y
E       1 =   E    (N/d +  Ej) =-—  +  Rd
7iea;d|<7(7i)  j=i  fid)

where | Rd |  =  | E^T  £, I £  d/M-
To  complete  the  proof  of  Theorem  1, we  need  only  show  that

-r-r/            1   V2             NNQ-1 +  z TT ( l-)     «-
pei\  /(/>)/  (log  TV) W

(III)    Q = (2(35) =   E  4,"  =   ^  i
de£>   gid)  deB   fid)

i97°]  on  4/m = 1/x+1/v+1/z  581

where  2D,- =  {d\ dE£>  and  p\d  implies  p=j  (mod  8)}  and  ti(d)  = total
number  of  primes  dividing  d.  (Since  d  is  square  free,  £l(d)  =u(d),  the
number  of  different  primes  dividing  d;  but  it  is  convenient  to  use  fi
rather  than  w.)
Hence,  we  need  estimates  on  sums  of  the  form:

JfiW
E —•
n

To  facilitate  these  estimates,  we  assume  until  further  notice  that
the  only  integers  n  we  deal  with  have  the  property  that  if  p\  n  then
p>b.
Let £Q(n>
T(y)  =  £'-

where  Z'  denotes  a  sum  over  square  free  numbers.  Also,  let

Si,x  =  {n  ^  x |  I2 is  the  largest  square  factor  of  «}.

Then

Z^=Z    Z  — = E   Z  V-
»si       «  >-l     ieSy|2,      »  ;=l    »es,„//     r»

K>l     7,Q(y2)  MU»)  Kx]     AiU/)  7,8<n)
= zv  E  — ^e  — 2: —
y-i            7            «eslTi/.2          w  y=i            r        n£SllS          n

/-I  J2  K»*>"\  ^2  p"  I

^  T(x)H(l  +Ci—\  ^c2T(x).
p>b  \  p2/

(ci  will  always  denote  an  unspecified  constant.)  Hence,

7,0 (n)  7,Q(n)
(iv)  £/f_£*2:  —•

Now E - ^*/ E -Y E -V E -V • • ( E -)
my     n  \nsv     »/\y_0    2> )\  j=0   3> /  \  y=0   />./

where  ps^b<ps+i.  Therefore

582  W. A. WEBB  [July

(V)  E  ~^^E    -^cslogy
n^y     n  m<y      m

where  the  last  sum  is  over  all  positive  integers  ±$y.
Now
 bsiM  A{n)      /  ^      1\"(vi)  E  —  £ E  —  = (  E  -)
mx        n  nix        n  \n<xlib        n  /

where  A in)  =  number  of  ways  n  can  be  written  as  a  product  of  b
numbers,  each  less  than  xllb.  That  &n(n)S:/l(«)  can  be  seen  from  the
fact  that  we  can  assign  each  prime  factor  of  n  to  any  one  of  b factors.
We  get  every  possible  factorization  of  n  in  this  way,  but  may  get
some  not  counted  in  A in).  Thus,  by  (IV),  (V),  and  (VI)  we  obtain:

££2(71)
(VII)  E'-£c,(log*)».
ti£i     n

Since
 TJ  (l-)      < c7   TJ  (l  -  —)       [4, Satz 5.5]

and
 TJ   ( 1-)      =  cs(log x)»    [4, Satz  4.1]
Kpsi  \  P /

by  (VII):
 baM  /  b \-1(viii)  e —^  n(i-4-)  •
n<,X       n  b<p<x\  p/

Let  L  be  any  set  of  primes,  q  an  element  of  I,  L'  =  L  — {q},
Ml=  {m\m  is  a  positive  integer  ^M,  and  p\m  implies  pEL},  and
Mu  defined  similarly.  We  now  show

ax)  n[}--)  ^  E'  —
p£L   \  P  /  m<EML       m

implies n(i--)  s*.  E'  —
pel'  \  ?> /  Beuv       W

If

i97o]  ON 4/«  =  l/x+l/y+l/z  583

n  i--      =cio Z'  —
peL   \  P  /  m£ML        m

then
 pel\  p)  PeL\  p  J      \  q /

&nc»>/  /3\
=sc10   Z     -(1-)
meML          m        \  q  /
-*.(  E'-Z'  —)

/  MUm)  AQ (m)\
sJS1--    Z'    —)

£Q(m)

=   ClO    /_,        -    '
mSAfi'        m

By  (VIII)  and  repeated  use  of  (IX)  we  have

SJ(d)
(x)        e    V**     n    (i-^V

where  h  =  2,  fr6 =  l  and  07=  4.  (The  condition  £>&y  is  vacuous  here.)
Now

.oS(       n        (1-*■)>-          s        *«(.-*•)
\PSAri/s.p_j(mod  8)  \  p  /      /  PSArl/9;j,sy(mod  8)  \  />  /

*,  fty log  log  iV1"
-  ^  —-7^-^  Cl1
j>£.Wl/9;p=;(mod  8)    p  <H°)

&y
^  — log log  TV* +  cu
4

and  therefore

(XI)  II  (l--)     =^p(~^oglogN  +  ci2)
psJVl/9:psj(mod  8)  \  p  /  \  4  /

=  cu(log  N)b,i\

Hence,  by  (III),  (X),  and  (XI)

584  W. A. WEBB

(2(35)  £  c14(logTV)(f'3+66+'.7)/4 =  Cl4(log  TV)7/4.

Note  that  if dE$>,- and  p\d,  then  p>bs.  Finally,

n  (i  -  tzv)  2 ^  n  (i  -  4)2  ^  c^ios ^8
ps<p \          ;(w  /              PsN  \            P  /

by  arguments  essentially  the  same  as  used  above.  Therefore

* II  (l  -  T^r)      =  ci.N^ilog  TV)8
pe& \  fiP)  /

and  so
 SiN)  g  TV       Cl6       +  Cl,iV*"(log  TV)*
(logTV)7/4

TV

(log  TV)7'4

This  completes  the  proof  of  Theorem  1.

III.  Concluding  remarks.  By  considering  the  primes  in  various
residue  classes  modulo  16,  the  results  of  Theorem  1 can  be  improved
to
 S(TV) «  TV/(log TV)2.

The  exponent  of  log  TV may  be  improved  to  9/4  —e  by  considering
primes  modulo  2k for  arbitrary  k  (e any  small  positive  number).
The  results  are  still  a  long  way  from  the  conjecture  that  5(TV) =0,
or  even  from  5(TV)<JCTV1_e, which  would  be  quite  desirable  to  prove.

References

1.  Alexander  Aigner,  Briiche  als  Summe  von  Stammbriichen,  J.  Reine  Angew.  Math.
214/215  (1964), 174-179. MR  28 #3969.
2.  L.  Bernstein,  Zur  Losung  der  diophantischen  Gleichung  m/n  =  l/x+l/y  +  l/z,
insbesondere im Fall ra = 4, J.  Reine Angew. Math.  211 (1962), 1-10. MR 26 #77.
3.  H.  Halberstam  and  K.  F.  Roth,  Sequences,  Vol.  1,  Clarendon  Press,  Oxford,
1966. MR 35 #1565.
4.  Karl  Prachar,  Primzahherteilung,  Springer-Verlag,  Berlin  and  New  York,  1957.
MR 19, 393.
5.  B.  M.  Stewart,  Theory  of  numbers,  2nd  ed.,  Macmillan,  New  York,  1964.
MR 37 #6232.
6.  B.  M.  Stewart  and  W.  A.  Webb,  Sums  of fractions  with  bounded  numerators,
Canad. J.  Math.  18 (1966), 999-1003. MR 33 #7297.

Pennsylvania  State  University,  University  Park,  Pennsylvania  16802  and
Washington  State  University,  Pullman  Washington  99163
