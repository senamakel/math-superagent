> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/crandall-1978-on-the-3x1-problem-ams.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

```claim
id: crandall-finite-cycles
statement: For any given period k there are finitely many cyclic trajectories of the 3x+1 map with period k (Corollary 7.2), via continued-fraction properties of log_2 3.
hypotheses: Crandall's map C on D+; period k of a cyclic trajectory.
holds-here: true — the foundational finiteness result for cycles.
evidence: proved in source (Crandall 1978, Math. Comp. 32, 1281-1292), using Diophantine approximation of log_2 3.
status: proved
falsifies: an infinite family of cycles with the same period k, or an error in the proof.
```

```claim
id: crandall-conjecture-H
statement: Crandall's Conjecture (3.1): H(x) ~ 2 log x / log(16/9) for the maximum height reached by x under iteration; if true it implies the main conjecture (no infinite heights).
hypotheses: H(x) the maximum value in the trajectory of x.
holds-here: true — a heuristic/stronger conjecture, not a theorem.
evidence: stated in source (Crandall 1978, Conjecture 3.1).
status: conjectured
falsifies: a counterexample x with infinite height, or a proof that H(x) grows faster.
```

```claim
id: reformulation-power-of-2
statement: The 3x+1 problem can be reduced to the statement that starting from any positive integer n, some iterate is a power of 2 (equivalently 1 in the accelerated form).
hypotheses: none — reformulation of the conjecture.
holds-here: true — used throughout the literature.
evidence: Lagarias overview Section 5(4); standard reformulation.
status: asserted-by-source
falsifies: a starting value whose orbit never hits a power of 2 but still reaches 1 (impossible by definition), or an error in the reformulation.
```

<!-- source: https://www.ams.org/journals/mcom/1978-32-144/S0025-5718-1978-0480321-3/S0025-5718-1978-0480321-3.pdf | converted from PDF -->

## What it claims

Received  March  28,  1977;  revised  March  20,  1978.
AMS  (MOS)  subject  classifications  (1970).    Primary  10A25.
Key  words  and  phrases.    Algorithm,  diophantine  equation.
Copyright  ©  1978,  American  Mathematical  Society

1281

1282  R- E- CRANDALL

Definition.    For  m  E D+  the  height  of  m,  denoted  h(m),  is the  cardinality  of

the  trajectory  Tm.    In  the  case  that  Tm is  a  finite  sequence,  h(m)  will  be  the  least
number  of  iterations  of  C required  to  reach  1.
Definition.  For  m  E D+,  we  denote  by  inf  Tm the  least  positive  integer  in

the  sequence  Tm.  Further,  if  Tm is  bounded,  we  denote  by  sup  Tm  the  greatest  in-

teger  in  the  sequence  Tm.    If  Tm  is  unbounded,  we  say  that  sup  Tm  is infinite.
The  following  table  should  serve as  an  example  for  the  previous  notation:

m  Tm  h(m)  sup  Tm

1  {1}  11
7  {11,17,13,5,1}  5  17
27  {41,...,  1}  41  3077
2iooo_1  {?}  4316  >io476
2iooo  +  1  {?j  2417  <10301

24096_j  {?}  19794  ?

It  is  partly  the  erratic  behavior  of  the  height…

## Statements it makes

Definition.    For  m  E  D+  the  trajectory  of  m  is the  sequence  Tm  =
{C(m),  C2(m),  .  .  .  },   where  it  is  understood  that  the  sequence  terminates  upon  the

Definition.    For  m  E D+  the  height  of  m,  denoted  h(m),  is the  cardinality  of

CONJECTURE (3.1).   H(x)  ~  2  log jc/log(16/9).
This  conjecture  is  stronger  than  the  main  conjecture  (2.1)  in  the  sense  that  if
there  be  even  one  m  E  D+  with  infinite  height,  then  (3.1)  is  false.

Lemma  (4.1).   Ifn  E D+  and  Ba.  ai(n)  is an  integer,  then  for  1 <i  <j  all
numbers  Baj  ai(n)  are  odd  integers;  and  further

Lemma  (4.2).  If  an  integer  m  =  Ba. ...ai(l)  and  ax  >  2,  then  the  trajectory  of
m is
 Tm  =  {Bahx...axH),Bai_2...ax{l),  ...,  Z?aj(l),  1}.

Lemma  (4.3).   ¿er  {a¡}  =  {a-, a-_j,  .  .  .  , ax }.   77/e« 5{aj.}(l)  /'s an  integer  of
height j  if and only if {a¡} E G.

Lemma  (5.2).   For  a real  number  z  >  0  the  number  of  sequences  of  length j  in
the  set  G with  ax  +  • • • +  ay <z  is greater  than  or  equal  to  (2[(z  -  2)/6j]  )'.
Proof.   Solutions  can be  restricted  by  the  inequalities

Theorem  (5.1).   Let  nh(x)  be  the  number  of  m  EM  with  h{m)  =  h  and  m
<  x.   Then  there  exist  real positive  constants  r,  x0  independent  of  h  such  that  for
x  >  max(*0,  2h,r),
 irh(x)>(logh2(xr))/h\.

Lemma (6.1). t"      i
lim  e  '   y      —  =  -•

Corollary  (7.1)  shows  that  if  the  main  conjecture  is  true  then  powers  of  two  and

Lemma  (7.1).  Let  pjqn  denote  the  nth  convergent  to  t  =  log2  3.    Then for

Lemma (7.2).  For  p„/q„  convergents to  t,

Lemma  (7.3).   For  p„/q„  convergents  to  t,  let y  <qm.    Then

Theorem  (7.2).  Let  p„/qn  be  convergents  to  t.    Let  1 <  m  =  inf  Tm and  let
k be the period of  Tm.   Then for  n >  4:

Corollary  (7.2).  For  any  given  k  there  are finitely  many  cyclic  trajectories
with period  k.

*[digest of a 30250 character source; every section, statement, and proof in full at `research/sources/crandall-1978-on-the-3x1-problem-ams.full.md`]*
